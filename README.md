# Flask-Architecture
This project has required python packages that's required in any flask normal or big project setup.

Files and folder structure are easy to use and configurable.

---
**Root file of this project begin with `application` file.**

1. `application.py `

This file contains initialization for extensions with flask instance and flask object setup for run project with environment, host and port settings.
There is AppSetting folder in this have extension, configuration and response file.

2. `extension.py`

Extensions file have all objects of required libraries and we can use these in our project apps and initialize these with flask object in application file.

3. `configuration.py`

Configuration file have flask app config variables that need to config with flask object.

4. `response.py`

Response file have common api response model enum.

---
**App Structure**

We already created app for you `AuthApp`. Use this for user related staff.
In this project structure we create apps like and create files with same names like `AuthApp`.
App have 5 files app, models, query, router and schema.

1. `app.py`

This file contains flask blueprint object and flask restx namespace object. Blueprint object and Namespace object initialize and add with flask object and rest api object that's imported from `extension` file.
We use this namespace object to create our routes.

2. `router.py`

This file is for create api using our namespace object.

3. `models.py`

Model file containing database model. In this we are using `db` object from `extension` file.

4. `schema.py`

Schema file work with marshmallow and database models. It's used to convert data types.

5. `query.py`

Query file use for create separate methods for `CRUD` operations on models.

---

On root have a .env file that's have your project details like host, port, environment settings and also having secret key, database schema url.
We just need to enter our details in this file according to variables.

---


**Setup this project on your local follow these steps.**
1. Create a virtual environment.
2. Activate created virtual environment.
3. Install all required python packages from `requirements.txt` file.
4. Update your `.env` file with your database url, server host & port, secret key, runtime environment.

Now we can run our server.

**Run flask server**
`flask run`

**Flask database migrations steps**
1. Initialize db migration `flask db init`.
2. Migrate models to database `flask db migrate -m "<message>"`.
3. To upgrade changes `flask db upgrade`.
4. To downgrade changes `flask db downgrade`.

---