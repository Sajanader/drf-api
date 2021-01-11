# Lab: Django REST Framework & Docker /Permissions & Postgresql
## Overview
* Use Django REST Framework to create an API, then “containerize” it with Docker.
* adding Permissions and Postgresql Database.

## Feature Tasks and Requirements
* Rebuild a custom version of Blog API demo project from scratch.
* Replace Blog and Post with your own application and model.
* The model must have at least as many fields as demo’s model.
* The model must have one field that is a foreign key to user.
* job is to merge the functionality of both demos.
* Customize your project to use different application features/models than Blog and Post
* Make your site a DRF powered API as you did in previous lab.
* Adjust project’s permissions so that only authenticated user’s have access to API.
* Add a custom permission so that only author of blog post can update or delete it.
* Add ability to switch user’s directly from browsable API.

## Features - Docker
* NOTE Refer to the class demo for built out Dockerfile and docker-compose.yml examples.
* Update Dockerfile and docker-compose.yml if needed.
* NOTE Refer to demo for built out Dockerfile and docker-compose.yml examples.
* create Dockerfile based off python:3.8-slim
* create docker-compose.yml to run Django app as a web service.
* enter docker-compose up --build to start your site.
* add postgres 11 as a service
* Note: It is not required to include a volume so that data can persist when container is shut down.
* Go to browsable api and confirm site properly restricts users based on their permissions


## Implementation Notes
Here need to run a command to convert pyproject.toml dependencies to requirements.txt
``` poetry export -f requirements.txt -o requirements.txt ```

If you get an allowed host error examine the bug details and update code as needed.
* When Docker installed and docker files are ready to go then run…
```$ docker-compose up```
* To shut docker down enter ctrl+c

## User Acceptance Tests
* Modify provided unit tests in demo to work for your project.

## Configuration
* Use poetry to initialize drf-api project.

```$ mkdir drf-api```

```$ cd drf-api```

```$ poetry init -n```

```$ poetry shell```

* Then continue to build the Django project.

Use the drf-api folder as the root of your project’s git repository.

Refer to Lab Submission Instructions for detailed instructions.
