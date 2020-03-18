# Django-TodoAPI


## Introduction

This API application supports a shared todo list that allows for users to mark when they are doing a task and when they have completed a task.

Any user is able to add any number of tasks to the list, however, the only owner is able to delete them.

This API application allows for the basic CRUD operations of the todo list, and users are able to notice whether a task is completed or not.

## REST API Service Via CRUD operations

This application is a REST API service via CRUD operations that provides a few functionalities

TodoAPI has 6 types of functionalities:

* `TodoList` : Get all the todo list via 'GET' method

* `ViewTask` : Get the detail of a task via 'GET' method

* `CreateTask` : Create a task in the todo list via 'POST' method

* `UpdateTask` : Update or edit a task via 'POST' method 

* `DeleteTask` : Delete a task only by an owner via 'DELETE' method

* `DoneTask` : Change the status of a task whether is is completed or not via 'POST' method

## Installation

### Using sources

Clone the repository and build:

```sh
$ git clone https://github.com/doyunbk/Django-TodoAPI
$ cd Django-TodoAPI
$ python3 manage.py runserver 0.0.0.0:8000
```

##### Dependency 
Install dependencies on local machine once your virtualenv is activated

```sh
$ pip3 install -r requirement.txt
```


##### Run Application

Run this application on command line

```sh
$ python3 manage.py runserver 0.0.0.0:8000
```

### Using Docker

Run this application using Docker
```sh
$ docker-compose build
$ docker-compose up
```

## Usage

##### Register User

Go to http://0.0.0.0:8000/api/register for the registration

##### API View

* `TodoList` : To see all the task in the todo list, go to http://0.0.0.0:8000/api/todolist

* `ViewTask` : To see the detail of a task, go to http://0.0.0.0:8000/api/viewtask/{task.id}

* `CreateTask` : To create the new task, go to http://0.0.0.0:8000/api/createtask

* `UpdateTask` : To update or edit a task, go to http://0.0.0.0:8000/api/updatetask/{task.id} 

* `DeleteTask` : To delete a task, go to http://0.0.0.0:8000/api/deletetask/{task.id}
 ** Login user must be an owner of a task, otherwise it gives an error message

##### Front-end View

After registeration, go to http://0.0.0.0:8000/ 
Then, login into an application and enjoy it :)