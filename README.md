# Credicxo-assignment-api
Assignment to implement 3 user levels: 1. Super-admin, 2. Teacher, 3. Student


## Software Requirements
- Python 3.6 or higher 
- PostgreSQL

## Setup
clone repo
```bash
#setup the virtual environment
$ python3 -m venv assignment_api
#activate virtual environment
$ source assignment_api/bin/activate
#go to cloned repo
$ cd Credicxo-assignment-api
#install requirements
$ pip install -r requirements.txt
```
### Setup database (using Postgres)
- goto Credicxo-assignment-api/assignment
- edit the following in settings.py 
```
#db name
'NAME': 'mydb',
'USER': '',
'PASSWORD': '',
'HOST': 'localhost',
'PORT': '5432',
```
```bash
$ python manage.py makemigrations
$ python manage.py migrate
# to run server
$ python manage.py runserver
```

## How to Use
### Register as Superadmin/Student/Teacher
#### url 
* method: **post**
* register as superadmin:  **/registeradmin/**
  - example of post data for registration
  ```
  {
    "username":"example",
    "first_name":"example",
    "last_name":"",
    "email":"example@gmail.com",
    "password":"example"
  }
  ```
* register as student:  **/registerstudent/**
  - example of post data 
  ```
  {
      "user":{
          "username":"example",
          "first_name":"example",
          "last_name":"",
          "email":"example@gmail.com",
          "password":"example"
      },
      "student_class":"10"
  }

  ```
* register as teacher: **/registerteacher/**
  - example of post data 
  ```
  {
      "user":{
          "username":"example",
          "first_name":"example",
          "last_name":"",
          "email":"example@gmail.com",
          "password":"example"
      },
      "subject":"example"
  }
  ```

### to get tokens
#### url
  - token pair(reftesh and access token):  **/api/token/**
    - method: **post**
    - prams 
      ```
       username = user username
       password = user password
      ```
  - to refresh access token: **/api/token/refresh/**
    - prams 
      ```
       refresh = refreshtoken
      ```
### to get list of teachers
  - url : **/teachers/** 
    - method: **get**
### to add new teacher 
  - url: **/teachers/**
    - method : **post**
    - example of post data 
    ```
    {
        "user":{
            "username":"example",
            "first_name":"example",
            "last_name":"",
            "email":"example@gmail.com",
            "password":"example"
        },
        "subject":"example"
    }

    ```
### to get list of students
  - url : **/students/** 
    - method: **get**
### to add new student 
  - url: **/students/**
    - method : **post**
    - example of post data 
    ```
    {
        "user":{
            "username":"example",
            "first_name":"example",
            "last_name":"",
            "email":"example@gmail.com",
            "password":"example"
        },
        "student_class":"10"
    }

    ```
### to get detail of student account
  - url : **/studentdetail/**
  - method: **get**
