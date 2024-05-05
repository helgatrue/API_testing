# Overview
REST API functional tests for https://jsonplaceholder.typicode.com/

## Software requirements 
- Python v3.10.12 and higher
- Pytest v8.2.0
- Allure v2.13.5

## Test structure
The tests are written against a black box and cover the `/posts` resource with actions on it (get, create, update, delete).
The tests are written using the following test design techniques: Boundary Value Analysis, Equivalence Partitioning, Use Case Testing, Error Guessing.
Information about available resources is taken from https://jsonplaceholder.typicode.com/.

The tests are separated by the following tests, parameterized and contain several test scenarios:

| Test                           | Scenario                                                                      | 
|:-------------------------------|:------------------------------------------------------------------------------| 
| `test_01_get_valid_request`    | **Positve**: response from `/posts/1` with  expected code **200**             | 
| `test_02_get_valid_request`    | **Positve**: response from `/posts/` with  expected code **200**              | 
| `test_03_get_valid_request`    | **Positve**: response from `/posts/100` with  expected code **200**           | 
| `test_04_get_valid_request`    | **Positve**: response from `/posts/100/comments` with  expected code **200**  | 
| `test_05_get_invalid_request`  | **Negative**: response from `/posts/0` with  expected code **400**            | 
| `test_06_get_invalid_request`  | **Negative**: response from `/posts/O` with  expected code **400**            | 
| `test_07_get_invalid_request`  | **Negative**: response from `/posts/!` with  expected code **404**            | 
| `test_08_get_invalid_request`  | **Negative**: response from `/posts/101` with  expected code **404**          | 
| `test_09_get_invalid_request`  | **Negative**: response from `/posts/101/comments` with  expected code **404** | 
| `test_10_get_request_for_id`   | **Positve**: check expected data for id=64                                    | 
| `test_11_post_valid_request`   | **Positve**: testing POST request with valid data                             | 
| `test_12_post_invalid_request` | **Negative**: testing POST request with invalid userId                        | 
| `test_13_post_invalid_request` | **Negative**: testing POST request with invalid body                          | 
| `test_14_post_invalid_request` | **Negative**: testing POST request without userId                             | 
| `test_15_post_invalid_request` | **Negative**: testing POST request with empty value                           | 
| `test_16_post_invalid_request` | **Negative**: testing POST request without body                               | 
| `test_17_put_valid_request`    | **Positve**: send `/posts/1` with valid data                                  | 
| `test_18_put_invalid_request`  | **Negative**: send `/posts/1` with empty value                                | 
| `test_19_put_invalid_request`  | **Negative**: send `/posts/1` with empty body                                 | 
| `test_20_put_invalid_request`  | **Negative**: send `/posts/1` with invalid id                                 | 
| `test_21_put_invalid_request`  | **Negative**: send `/posts/101` with invalid userId                           |
| `test_22_delete_valid_request`       | **Positve**: send `/posts/1` with  expected code **200**                      | 
|      `test_23_delete_valid_request`                           | **Positve**: send `/posts/100` with  expected code **200**                    | 
|      `test_24_delete_invalid_request`                            | **Negative**: send `/posts/0` with  expected code **404**                     | 
|    `test_25_delete_invalid_request`                              | **Negative**: send `/posts/101` with  expected code **404**                   | 
|    `test_26_delete_invalid_request`                              | **Negative**: send `/posts/ ` with  expected code **404**                     | 



# How to run tests
- [Locally](https://github.com/helgatrue/API_testing/blob/main/README.md#run-locally)
- [In Docker](https://github.com/helgatrue/API_testing/blob/main/README.md#run-tests-in-docker)
- [With Allure](https://github.com/helgatrue/API_testing/blob/main/README.md#if-youd-like-to-see-test-report)

## Run locally
- Install [python3](https://www.python.org/downloads/)
- Go to the project folder and run

**Install all libraries from requirements.txt:**
```
pip3 install -r requirements.txt
```

**Run**

To run one specification use the following command:
```
pytest src/tests/test_api_get.py
```

## Run tests in docker
```
docker-compose build
docker-compose up
```

## If you'd like to see test report
- Install [allure](https://allurereport.org/docs/pytest/).
- Run tests:
```
pytest --alluredir=reports tests/test_posts.py
```

**Create allure report:**
```
allure serve reports
```
The results of the test run will be build in the visual report.
