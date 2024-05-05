import allure
import pytest
from src.client import JSONPlaceholder


class TestPosts:
    @pytest.fixture
    def api(self):
        return JSONPlaceholder('https://jsonplaceholder.typicode.com')

    @allure.title('Check that PUT request with valid body is send')
    def test_17_put_valid_request(self, api):
        endpoint = "/posts/1"
        data = {"id": 1, "title": "foo", "body": "bar", "userId": 1}
        status_code, body = api.put(endpoint, data)
        assert status_code == 200, \
            "Actual response code does not equal expected code: {} != {}" \
                .format(status_code, 200)
        assert body["id"] == data["id"], "Post was created has wrong id"
        assert body["title"] == data["title"], "Post was created has wrong title"
        assert body["body"] == data["body"], "Post was created has wrong body"
        assert body["userId"] == "1", "Post was created has wrong user id"

    @allure.title('Check that PUT request with invalid body has status code 400')
    def test_18_put_valid_request(self, api):
        endpoint = "/posts/1"
        data = {"id": " ", "title": " ", "body": " ", "userId": " "}
        status_code, body = api.put(endpoint, data)
        assert status_code == 400, \
            "Actual response code does not equal expected code: {} != {}" \
                .format(status_code, 400)

    @allure.title('Check that PUT request with empty body has status code 400')
    def test_19_put_valid_request(self, api):
        endpoint = "/posts/1"
        data = {}
        status_code, body = api.put(endpoint, data)
        assert status_code == 400, \
            "Actual response code does not equal expected code: {} != {}" \
                .format(status_code, 400)

    @allure.title('Check that PUT request with invalid id has status code 400')
    def test_20_put_valid_request(self, api):
        endpoint = "/posts/1"
        data = {"id": 101}
        status_code, body = api.put(endpoint, data)
        assert status_code == 400, \
            "Actual response code does not equal expected code: {} != {}" \
                .format(status_code, 400)

    @allure.title('Check that PUT request with invalid endpoint has status code 404')
    def test_21_put_valid_request(self, api):
        endpoint = "/posts/101"
        data = {"title": "foo", "body": "bar", "userId": "1"}
        status_code, body = api.put(endpoint, data)
        assert status_code == 404, \
            "Actual response code does not equal expected code: {} != {}" \
                .format(status_code, 404)