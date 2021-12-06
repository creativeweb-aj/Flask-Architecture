# Flask-Architecture
This is already have required python packages for flask project setup.
Root of project begin with application file.
application.py 
This file contains initialization for extensions with flask instance and flask object setup for run project with environment, host and port settings.
There is AppSetting folder in this have extensions, configuration and response file.
extensions.py
Extensions file have all objects of required libraries and we can use these in our project apps and initialize these with flask object in application file.
configurations.py
Configuration file have flask app config variables that need to config with flask object.
response.py
Response file have common api response model enum. 

In this have a .env file that's have your project host, port, environment settings and also having secret key, database schema url.
We just need to write our data in these varibales.
After that we just run our server
flask run

