#!/bin/bash

cd /python3satgenerator
gunicorn satgen.wsgiadapter:application -b 0.0.0.0:8000