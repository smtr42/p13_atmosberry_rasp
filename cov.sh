#!/bin/sh

black --line-length=79 .
docformatter --recursive --in-place .
isort .

coverage run -m pytest -v
coverage report
coverage html
