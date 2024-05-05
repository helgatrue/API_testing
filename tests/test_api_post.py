import allure
import pytest
from src.client import JSONPlaceholder


class TestPosts:
    @pytest.fixture
    def api(self):
        return JSONPlaceholder('https://jsonplaceholder.typicode.com')

    @allure.title('Check request with valid body')
    def test_11_post_valid_request(self, api):
        endpoint = "/posts/"
        data = {"title": "foo", "body": "bar", "userId": 1}
        status_code, body = api.post(endpoint, data)
        assert status_code == 201, \
            "Actual response code does not equal expected code: {} != {}" \
                .format(status_code, 201)
        assert body["title"] == data["title"], "Post was created has wrong title"
        assert body["body"] == data["body"], "Post was created has wrong body"
        assert body["userId"] == "1", "Post was created has wrong user id"
        assert body["id"] == 101

    @allure.title('Check request with invalid UserId')
    def test_12_post_invalid_request(self, api):
        endpoint = "/posts/"
        data = {"title": "foo", "body": "bar", "userId": "1"}
        status_code, body = api.post(endpoint, data)
        assert status_code == 400, \
            "Actual response code does not equal expected code: {} != {}" \
                .format(status_code, 400)

    @allure.title('Check request with invalid body')
    def test_13_post_invalid_request(self, api):
        endpoint = "/posts/"
        data = {"title": None, "body": None, "userId": None}
        status_code, body = api.post(endpoint, data)
        assert status_code == 400, \
            "Actual response code does not equal expected code: {} != {}" \
                .format(status_code, 400)

    @allure.title('Check request with missed userID')
    def test_14_post_invalid_request(self, api):
        endpoint = "/posts/ "
        data = {"title": "foo", "body": 'bar'}
        status_code, body = api.post(endpoint, data)
        assert status_code == 400, \
            "Actual response code does not equal expected code: {} != {}" \
                .format(status_code, 400)

    @allure.title('Check request with empty values in body')
    def test_15_post_invalid_request(self, api):
        endpoint = "/posts/"
        data = {"title": " ", "body": " ", "userId": " "}
        status_code, body = api.post(endpoint, data)
        assert status_code == 400, \
            "Actual response code does not equal expected code: {} != {}" \
                .format(status_code, 400)

    @allure.title('Check request with empty body')
    def test_16_post_invalid_request(self, api):
        endpoint = "/posts/"
        data = {}
        status_code, body = api.post(endpoint, data)
        assert status_code == 400, \
            "Actual response code does not equal expected code: {} != {}" \
                .format(status_code, 400)