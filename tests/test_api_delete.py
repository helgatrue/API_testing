import allure
import pytest
from src.client import JSONPlaceholder


class TestPosts:
    @pytest.fixture
    def api(self):
        return JSONPlaceholder('https://jsonplaceholder.typicode.com')

    @allure.title('Check request with valid url')
    def test_22_delete_valid_request(self, api):
        endpoint = "/posts/1"
        code, body = api.delete(endpoint)
        assert code == 200, \
            "Actual response code does not equal expected code: {} != {}" \
                .format(code, 200)

    @allure.title('Check request with valid url')
    def test_23_delete_valid_request(self, api):
        endpoint = "/posts/100"
        code, body = api.delete(endpoint)
        assert code == 200, \
            "Actual response code does not equal expected code: {} != {}" \
                .format(code, 200)

    @allure.title('Check request with invalid url')
    def test_24_delete_invalid_request(self, api):
        endpoint = "/posts/0"
        code, body = api.delete(endpoint)
        assert code == 404, \
            "Actual response code does not equal expected code: {} != {}" \
                .format(code, 404)

    @allure.title('Check request with invalid url')
    def test_25_delete_invalid_request(self, api):
        endpoint = "/posts/101"
        code, body = api.delete(endpoint)
        assert code == 404, \
            "Actual response code does not equal expected code: {} != {}" \
                .format(code, 404)

    @allure.title('Check request with invalid url')
    def test_26_delete_invalid_request(self, api):
        endpoint = "/posts/ "
        code, body = api.delete(endpoint)
        assert code == 404, \
            "Actual response code does not equal expected code: {} != {}" \
                .format(code, 404)