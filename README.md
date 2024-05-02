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

| Test | Scenario | 
| :---         |     :---      | 
| `test_01_get_request`    |**Positve**: response from `/posts/1` with  expected code **200**| 
|     |**Positve**: response from `/posts/` with  expected code **200**| 
|     |**Positve**: response from `/posts/100` with  expected code **200**| 
|     |**Positve**: response from `/posts/100/comments` with  expected code **200**| 
|     |**Negative**: response from `/posts/0` with  expected code **400**| 
|     |**Negative**: response from `/posts/O` with  expected code **400**| 
|     |**Negative**: response from `/posts/!` with  expected code **404**| 
|     |**Negative**: response from `/posts/101` with  expected code **404**| 
|     |**Negative**: response from `/posts/101/comments` with  expected code **404**| 
|`test_02_get_request_for_id`|**Positve**: check expected data for id=64| 
|`test_03_post_request` |**Positve**: testing POST request with valid data| 
| |**Negative**: testing POST request with invalid userId| 
| |**Negative**: testing POST request with invalid body| 
| |**Negative**: testing POST request without userId| 
| |**Negative**: testing POST request with empty value| 
| |**Negative**: testing POST request without body| 
|`test_04_put_request` |**Positve**: send `/posts/1` with valid data| 
| |**Positve**: send `/posts/1` with valid data| 
| |**Negative**: send `/posts/1` with empty value| 
| |**Negative**: send `/posts/1` with empty body| 
| |**Negative**: send `/posts/1` with id key| 
| |**Negative**: send `/posts/101` with invalid userId| 
|`test_05_delete_request` |**Positve**: send `/posts/1` with  expected code **200**| 
|  |**Positve**: send `/posts/100` with  expected code **200**| 
|  |**Negative**: send `/posts/0` with  expected code **404**| 
|  |**Negative**: send `/posts/101` with  expected code **404**| 
|  |**Negative**: send `/posts/ ` with  expected code **404**| 



# How to run tests

## Run locally
- Install [python3](https://www.python.org/downloads/)
- Go to the project folder and run

**Install all libraries from requirements.txt:**
```
pip3 install -r requirements.txt
```

**Run:**
```
pytest src/tests/test_posts.py
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
