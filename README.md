# Example Python flask Rest API

## Overview

This documentation outlines the endpoints available in the example REST API built with flask and python.

## Dependencies

The following report links work only once the api is compiled in local

| Resource      | Documentation                                     | Info                                                             |
|:--------------|:--------------------------------------------------|:-----------------------------------------------------------------|
| python        | https://www.python.org/                           | No                                                               |
| pytest        | https://docs.pytest.org/en/8.0.x/                 | [Report](http://localhost:5000/)                                 |
| flask         | https://flask.palletsprojects.com/en/3.0.x/       | No                                                               |
| flask-restx   | https://flask-restx.readthedocs.io/en/latest/     | No                                                               |
| Swagger       | https://swagger.io/                               | [Report](http://localhost:5000/swagger/)                         | 
| pipenv        | https://pipenv.pypa.io/en/latest/                 | No                                                               | 


## Project Structure

The project structure is organized as follows:

```sh
├── app/
│   ├── common/
│   │   ├── exception/
│   │   ├── util/
│   │   └── models/
│   ├── controller/
│   ├── repository/
│   ├── service/
│   └── app.py
│
├── config/
│   ├── deploy/
│   ├── docker/
│   └── kubernates/
│
├── tests/
│    └── app/
│       ├── controller/
│       ├── repository/
│       └── service/
└── README.md 
```

## Base URL

The base URL for all endpoints is `http://localhost:5000/v1`.

## API Endpoints
The following endpoints are available:

* POST /v1/users: create user.
```sh
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{"name": "John Doe", "email": "john.doe@example.com"}' \
  http://localhost:5000/v1/users/
```

* GET /v1/users: Get all users.
```sh
curl -X GET \
  -H "Content-Type: application/json" \
  http://localhost:5000/v1/users/
```

* GET /v1/users/123: Get a user by ID.
```sh
curl -X GET \
  -H "Content-Type: application/json" \
  http://localhost:5000/users/123
```

* PUT /v1/users: Update a user by ID.
```sh
curl -X PUT \
  -H "Content-Type: application/json" \
  -d '{"id": 123, "name": "Updated Name", "email": "updated.email@example.com"}' \
  http://localhost:5000/users/

```

* PUT /v1/users/123: Delete a user by ID.
```sh
curl -X DELETE \
  -H "Content-Type: application/json" \
  http://localhost:5000/users/123

```

## Endpoint Documentation 

The openApi URL documentation in local environment is `http://localhost:5000/swagger`.

## Install
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