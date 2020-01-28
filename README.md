# Introduction to tests

Application developed in a webinar in the Youtube to *Digital Innovation One®* (https://digitalinnovation.one/). 
In this webinar was presents a introduction to tests in Flask applications.

**Webinar:** https://www.youtube.com/watch?v=P0aTDyw9N4g&t


## Install Requirements

$ pip install -r requirements.txt

## RUN Flask Application

$ export FLASK_APP=app.py  
$ flask run

## RUN Tests

$ py.test

## RUN Coverage

$ coverage run --source=app -m py.test  
$ coverage report -m   
$ coverage html
