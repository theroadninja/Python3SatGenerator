#!/bin/bash

#to install gunicorn on ubuntu:
# sudo apt-get install -y gunicorn

#to install gunicorn on some other linux flavor:
# wipe os and install ubuntu
# sudo apt-get install -y gunicorn

#gunicorn run command:
#the 0.0.0.0 must be used instead of localhost, because localhost
#will make it ONLY listen on loopback.
#    gunicorn satgen.wsgiadapter:application -b 0.0.0.0:8000


#set python path so you can call it from any folder
f=`dirname $0`
f=$f/..
PYTHONPATH=$PYTHONPATH:$f gunicorn satgen.wsgiadapter:application -b 0.0.0.0:8000
