# Simple URL API
A simple Flask backend API that allows you to manage URLs and their comments.

### Description
The API server is currently running on an AWS EC2 instance and can be accessed using the already provided URL.  It is connected to a PostgreSQL database running on AWS RDS. 

The database consists of 2 tables: *urls* and *comments* .  They have a one-to-many relationship where 1 *url* can have many *comments*.

The API is written in Python using the Flask framework.

### Usage
API endpoints can be tested using an application such as Postman or by running the Simple URL APP React frontend application locally. (See [Simple URL APP](https://github.com/gabalmat/simple-url-app) for details.)

### RESTful API:
Available endpoints and their descriptions:

| Method | Endpoint           | Description                                                                                     |
|--------|--------------------|-------------------------------------------------------------------------------------------------|
| GET    | '/api/urls'        | Returns a ist of all URLS                                                                       |
| GET    | '/api/url/{url_id} | Returns the URL with the given `id` url parameter                                                            |
| POST   | '/api/addurl/'     | Adds the provided `url`. Will also optionally add a `comment` if one is present in the request |
| POST   | '/api/addcomment'  | Adds the provided `comment` and associates it with  the provided `url`                          |

- GET requests do not require any special headers.
- POST requests should have the *Content-Type* header set to *application/json* and the request data should be in json format.

    For example: 
  - '/api/addurl' (*Note: the *comment* parameter is optional)
    ```
    {"uri": "https://www.google.com/", "comment": "Some generic comment"}
	```
	
	
  - '/api/addcomment'
    ```
    {"url_id": 1, "Another generic comment"}
    ```

### Run Locally
If you prefer to run this API locally, follow the steps below and please pay close attention to the assumptions:

Assumptions:
 - This repo has been cloned locally
 - PostgreSQL DB running locally
 - python3, pip3, and virtualenv installed locally
 - cwd is the top-level `simple-url-api` directory
 
Create a virtualenv and activate it:
```
python3 -m <name_of_env>
. venv/bin/activate
```

Install Dependencies:
```
pip3 install -r requirements.txt
```

Set environment variables (replace values in <> with desired configuration):
```
export FLASK_APP=application.py
export FLASK_CONFIG=development
export POSTGRES_USER=<username>
export POSTGRES_PASSWORD=<password>
export DB_SERVER=<db servername or localhost>
export DB_PORT=<db port or 5432>
export DB_NAME=<desired db name>
```

Run:
```
flask run
```

The API should be running on http://localhost:5000


