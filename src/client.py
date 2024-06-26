import requests
from urllib.parse import urljoin


def parse_response(fn):
    def wrapper(*args, **kwargs):
        resp = fn(*args, **kwargs)
        try:
            decoded_json = resp.json()
        except Exception:
            decoded_json = None
        return resp.status_code, decoded_json
    return wrapper


class JSONPlaceholder(object):

    def __init__(self, url):
        self.url = url

    def _make_url(self, endpoint=None):
        """Make full url for given resource endpoint.

        :param endpoint: str, resource endpoint
        :return: str, full url
        """
        if endpoint:
            return urljoin(self.url, endpoint)
        return self.url

    @parse_response
    def get(self, endpoint=None, **kwargs):
        return requests.get(self._make_url(endpoint), **kwargs)

    @parse_response
    def post(self, endpoint=None, data={}):
        return requests.post(self._make_url(endpoint), data=data)

    @parse_response
    def put(self, endpoint=None, data={}):
        return requests.put(self._make_url(endpoint), data=data)

    @parse_response
    def delete(self, endpoint=None, **kwargs):
        return requests.delete(self._make_url(endpoint), **kwargs)