import allure
import pytest
from src.client import JSONPlaceholder


class TestPosts:
    @pytest.fixture
    def api(self):
        return JSONPlaceholder('https://jsonplaceholder.typicode.com')

    @allure.title('Check response for id 1')
    def test_01_get_valid_request(self, api):
        endpoint = "/posts/1"
        expected_data = {
            "userId": 1,
            "id": 1,
            "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
            "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
        }
        status_code, body = api.get(endpoint)
        assert status_code == 200, \
            "Actual response code does not equal expected code: {} != {}" \
                .format(status_code, 200)
        assert body.get("userId") == expected_data["userId"], "Post was created has wrong user id"
        assert body.get("id") == expected_data["id"], "Post has wrong id"
        assert body.get("title") == expected_data["title"], "Post was created has wrong title"
        assert body.get("body") == expected_data["body"], "Post was created has wrong body"

    @allure.title('Check that status code for all ids is 200')
    def test_02_get_valid_request(self, api):
        endpoint = "/posts/"
        status_code, body = api.get(endpoint)
        assert status_code == 200, \
            "Actual response code does not equal expected code: {} != {}" \
                .format(status_code, 200)
        assert body != None, "Body is empty"

    @allure.title('Check response for id 100')
    def test_03_get_valid_request(self, api):
        expected_data = {
            "userId": 10,
            "id": 100,
            "title": "at nam consequatur ea labore ea harum",
            "body": "cupiditate quo est a modi nesciunt soluta\nipsa voluptas error itaque dicta in\nautem qui minus magnam et distinctio eum\naccusamus ratione error aut"
        }
        endpoint = "/posts/100"
        status_code, body = api.get(endpoint)
        assert status_code == 200, \
            "Actual response code does not equal expected code: {} != {}" \
                .format(status_code, 200)
        assert body.get("userId") == expected_data["userId"], "Post was created has wrong user id"
        assert body.get("id") == expected_data["id"], "Post has wrong id"
        assert body.get("title") == expected_data["title"], "Post was created has wrong title"
        assert body.get("body") == expected_data["body"], "Post was created has wrong body"

    @allure.title('Check response for comments')
    def test_04_get_valid_request(self, api):
        endpoint = "/posts/1/comments"
        status_code, body = api.get(endpoint)
        assert status_code == 200, \
            "Actual response code does not equal expected code: {} != {}" \
                .format(status_code, 200)
        assert body != None, "Body is empty"

    @allure.title('Check response for invalid id')
    def test_05_get_invalid_request(self, api):
        endpoint = "posts/0"
        status_code, body = api.get(endpoint)
        assert status_code == 404, \
            "Actual response code does not equal expected code: {} != {}" \
                .format(status_code, 404)

    @allure.title('Check response for invalid id')
    def test_06_get_invalid_request(self, api):
        endpoint = "/posts/O"
        status_code, body = api.get(endpoint)
        assert status_code == 404, \
            "Actual response code does not equal expected code: {} != {}" \
                .format(status_code, 404)

    @allure.title('Check response for invalid id')
    def test_07_get_invalid_request(self, api):
        endpoint = "/posts/!"
        status_code, body = api.get(endpoint)
        assert status_code == 404, \
            "Actual response code does not equal expected code: {} != {}" \
                .format(status_code, 404)

    @allure.title('Check response for invalid id')
    def test_08_get_invalid_request(self, api):
        endpoint = "/posts/101"
        status_code, body = api.get(endpoint)
        assert status_code == 404, \
            "Actual response code does not equal expected code: {} != {}" \
                .format(status_code, 404)

    @allure.title('Check response for comments with invalid id')
    def test_09_get_invalid_request(self, api):
        endpoint = "/posts/101/comments"
        status_code, body = api.get(endpoint)
        assert status_code == 404, \
            "Actual response code does not equal expected code: {} != {}" \
                .format(status_code, 404)

    @allure.title('Check data in GET response for id 64')
    def test_10_get_request_for_id(self, api):
        endpoint = "/posts/64"
        expected_data = {
            "userId": 7,
            "id": 64,
            "title": "et fugit quas eum in in aperiam quod",
            "body": "id velit blanditiis\neum ea voluptatem\nmolestiae sint occaecati est eos perspiciatis\nincidunt a "
                    "error provident eaque aut aut qui"
        }
        status_code, body = api.get(endpoint)
        assert status_code == 200, \
            "Actual response code does not equal expected code: {} != {}" \
                .format(status_code, 200)
        assert body.get("userId") == expected_data["userId"], "Post was created has wrong user id"
        assert body.get("id") == expected_data["id"], "Post has wrong id"
        assert body.get("title") == expected_data["title"], "Post was created has wrong title"
        assert body.get("body") == expected_data["body"], "Post was created has wrong body"