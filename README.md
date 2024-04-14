

# Introduction

The goal of this project is to provide to introduce online food booking of a restauraunt to the cutomers.

Template is written with django 5.0.4 and python 3.12 in mind.

### Main features

* Separated dev and production settings

* Website with custom user model

* Bootstrap static files included

* User registration and logging in

* Procfile for easy deployments

* Separated requirements files

* SQLite database is used as backend database

# Usage

To use this template to start your own project:

### Existing virtualenv

If your project is already in an existing python3 virtualenv first install django by running

    $ pip install django
    
And then run the `django-admin.py` command to start the new project:

    $ django-admin.py startproject <project_name>

# Getting Started

But here already the project is created itself run these commands to run the server.

Activate the virtualenv for your project( if it is not activated).
    
Install project dependencies:

    $ pip install -r requirements/local.txt
    
    
Then simply apply the migrations:

    $ python manage.py migrate
    

You can now run the development server:

    $ python manage.py runserver