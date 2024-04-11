# Example Python flask Rest API

## Overview

This documentation outlines the endpoints available in the example REST API built with flask and python.
[GIT](https://github.com/jorgecodelia/apiFlaskExample)

## Dependencies

More details [here](requirements.txt)

| Resource          | Documentation                                             | 
|:------------------|:----------------------------------------------------------|
| python            | https://www.python.org/                                   |
| pytest            | https://docs.pytest.org/en/8.0.x/                         |
| pytest-html       | https://docs.pytest.org/en/8.0.x/                         |
| flask             | https://flask.palletsprojects.com/en/3.0.x/               |
| flask-restx       | https://flask-restx.readthedocs.io/en/latest/             |
| flask-SQLAlchemy  | https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/    |
| Swagger           | https://swagger.io/                                       |
| pyyaml            | https://pypi.org/project/PyYAML/                          |
| python-dotenv     | https://pypi.org/project/python-dotenv/                   | 



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

* **POST `/v1/users`: create user.**
```sh
curl --location 'http://localhost:5000/v1/user' \
--header 'Content-Type: application/json' \
--data-raw '{
    "name": "Charles",
    "email": "charles.white@example.com"
}'
```

* **GET `/v1/users`: Get all users.**
```sh
curl --location 'http://localhost:5000/v1/users'
```

* **GET `/v1/user/123`: Get a user by ID.**
```sh
curl --location 'http://localhost:5000/v1/user?id=4'
```

* **PUT `/v1/user`: Update a user by ID.**
```sh
curl --location --request PUT 'http://localhost:5000/v1/user?id=3' \
--header 'Content-Type: application/json' \
--data-raw '{
    "id": 3,
    "name": "Mike",
    "email": "mike.jhonson@example.com"
}'
```

* **DELETE `/v1/user/123`: Delete a user by ID.**
```sh
curl --location --request DELETE 'http://localhost:5000/v1/user?id=4'
```

## Endpoint Documentation 

The openApi URL documentation in local environment is `http://localhost:5000/api-doc.html`.

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
* Step 4:
```sh
pip install -e .
```

## Run unit test
Report [URL](http://127.0.0.1:3000/.build/report.html?sort=result)
```sh
pytest
```

## Run
```sh
flask run
```

## License
This Api is distributed under the terms of the MIT License. See the [license](LICENSE.md) for details.