# Example Python flask Rest API

## Overview

This documentation outlines the endpoints available in the example REST API built with flask and python.

## Dependencies

The following report links work only once the api is compiled in local

| Resource          | Documentation                                             | Info                                                             |
|:------------------|:----------------------------------------------------------|:-----------------------------------------------------------------|
| python            | https://www.python.org/                                   | No                                                               |
| pytest            | https://docs.pytest.org/en/8.0.x/                         | [Report](http://localhost:5000/)                                 |
| pytest-html       | https://docs.pytest.org/en/8.0.x/                         | No                                 |
| flask             | https://flask.palletsprojects.com/en/3.0.x/               | No                                                               |
| flask-restx       | https://flask-restx.readthedocs.io/en/latest/             | No                                                               |
| flask-SQLAlchemy  | https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/    | No                                                               |
| Swagger           | https://swagger.io/                                       | [Report](http://localhost:5000/)                         | 
| pyyaml            | https://pypi.org/project/PyYAML/                          | No                                                               | 
| python-dotenv     | https://pypi.org/project/python-dotenv/                   | No                                                               | 



## Project Structure

The project structure is organized as follows:

```sh
├── app/
│   ├── api/
│   │   ├── controller/
│   │   ├── exception/
│   │   ├── model/
│   │   ├── repository/
│   │   ├── service/
│   │   └── util/
│   ├── resources/
│   └── test/
│
├── ci/
│   ├── deploy/
│   ├── docker/
│   └── kubernates/
│
├── README.md
├── requirements.txt
├── .flaskenv
└── .gitignore
```

## Base URL

The base URL for all endpoints is `http://localhost:5000/v1/user`.

## API Endpoints
The following endpoints are available:

* POST /v1/users: create user.
```sh
curl -X 'POST' \
  'http://localhost:5000/v1/user' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "id": 4,
  "name": "john",
  "email": "john@email.com"
}'
```

* GET /v1/users: Get all users.
```sh
curl -X 'GET' \
  'http://localhost:5000/v1/users' \
  -H 'accept: application/json'
```

* GET /v1/users/123: Get a user by ID.
```sh
curl -X 'GET' \
  'http://localhost:5000/v1/user?id=2' \
  -H 'accept: application/json'
```

* PUT /v1/users: Update a user by ID.
```sh
curl -X 'PUT' \
  'http://localhost:5000/v1/user' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "id": 1,
  "name": "ana",
  "email": "lee@email.com"
}'

```

* PUT /v1/users/123: Delete a user by ID.
```sh
curl -X 'DELETE' \
  'http://localhost:5000/v1/user?id=3' \
  -H 'accept: application/json'

```

## Endpoint Documentation 

The openApi URL documentation in local environment is `http://localhost:5000/swagger`.

## Install
* Step 1:
```sh
python -m venv env
```
* Step 2:
```sh
source env/bin/activate
```
* Step 3:
```sh
pip install -r requirements.txt
```

## Run unit test
```sh
pytest
```

## Run
```sh
flask run
```

## License
This Api is distributed under the terms of the MIT License. See the [license](LICENSE.md) for details.