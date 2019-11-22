#!/bin/sh

isort *.py text_validator/*.py text_validator/plugins/*.py
black *.py text_validator/*.py text_validator/plugins/*.py
flake8 *.py text_validator/*.py text_validator/plugins/*.py
