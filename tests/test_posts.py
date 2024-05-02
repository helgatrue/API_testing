import allure
import pytest
from src.client import JSONPlaceholder


class TestPosts:
    @pytest.fixture
    def api(self):
        return JSONPlaceholder('https://jsonplaceholder.typicode.com')

    @allure.title('Check status code in response for GET request')
    @pytest.mark.parametrize(
        "endpoint, expected_code",
        [
            ("/posts/1", 200),
            ("/posts/", 200),
            ("/posts/100", 200),
            ("/posts/1/comments", 200),
            ("posts/0", 404),
            ("/posts/O", 404),
            ("/posts/!", 404),
            ("/posts/101", 404),
            ("/posts/101/comments", 404)
        ])
    def test_01_get_request(self, api, endpoint, expected_code):
        status_code, body = api.get(endpoint)
        assert status_code == expected_code, \
            "Actual response code does not equal expected code: {} != {}" \
            .format(status_code, expected_code)

    @allure.title('Check data in GET response for id 64')
    def test_02_get_request_for_id(self, api, endpoint="/posts/64", expected_code=200):
        expected_data = {
            "userId": 7,
            "id": 64,
            "title": "et fugit quas eum in in aperiam quod",
            "body": "id velit blanditiis\neum ea voluptatem\nmolestiae sint occaecati est eos perspiciatis\nincidunt a "
                    "error provident eaque aut aut qui"
        }
        status_code, body = api.get(endpoint)
        assert status_code == expected_code, \
            "Actual response code does not equal expected code: {} != {}" \
            .format(status_code, expected_code)
        assert body.get("userId") == expected_data["userId"], "Post was created has wrong user id"
        assert body.get("id") == expected_data["id"], "Post has wrong id"
        assert body.get("title") == expected_data["title"], "Post was created has wrong title"
        assert body.get("body") == expected_data["body"], "Post was created has wrong body"

    @allure.title('Check response in POST request')
    @pytest.mark.parametrize(
        "endpoint, data, expected_code",
        [
            ("/posts/", {"title": "foo", "body": "bar", "userId": 1}, 201),
            ("/posts/", {"title": "foo", "body": "bar", "userId": "1"}, 400),
            ("/posts/", {"title": None, "body": None, "userId": None}, 400),
            ("/posts/ ", {"title": "foo", "body": 'bar'}, 404),
            ("/posts/", {"title": " ", "body": " ", "userId": " "}, 400),
            ("/posts/", {}, 404),
        ])
    def test_03_post_request(self, api, endpoint, data, expected_code):
        status_code, body = api.post(endpoint)
        assert status_code == expected_code, \
            "Actual response code does not equal expected code: {} != {}" \
            .format(status_code, expected_code)
        assert data["title"] == data["title"], "Post was created has wrong title"
        assert data["body"] == data["body"], "Post was created has wrong body"
        assert data["userId"] == data["userId"], "Post was created has wrong user id"

    @allure.title('Check response in PUT request')
    @pytest.mark.parametrize(
        "endpoint, data, expected_code",
        [
            ("/posts/1", {"id": 1, "title": "foo", "body": "bar", "userId": 1}, 200),
            ("/posts/1", {"id": " ", "title": " ", "body": " ", "userId": " "}, 400),
            ("/posts/1", {}, 400),
            ("/posts/1", {"id": 101}, 400),
            ("/posts/101", {"title": "foo", "body": "bar", "userId": "1"}, 404)
        ])
    def test_04_put_request(self, api, endpoint, data, expected_code):
        status_code, body = api.put(endpoint)
        assert status_code == expected_code, \
            "Actual response code does not equal expected code: {} != {}" \
            .format(status_code, expected_code)
        assert data["id"] == data["id"], "Post was created has wrong id"
        assert data["title"] == data["title"], "Post was created has wrong title"
        assert data["body"] == data["body"], "Post was created has wrong body"
        assert data["userId"] == data["userId"], "Post was created has wrong user id"

    @allure.title('Check response in DELETE request')
    @pytest.mark.parametrize(
        "endpoint, expected_code",
        [
            ("/posts/1", 200),
            ("/posts/100", 200),
            ("/posts/0", 404),
            ("/posts/101", 404),
            ("/posts/ ", 404)
        ])
    def test_05_delete_request(self, api, endpoint, expected_code):
        code, body = api.delete(endpoint)
        assert code == expected_code, \
            "Actual response code does not equal expected code: {} != {}" \
            .format(code, expected_code)