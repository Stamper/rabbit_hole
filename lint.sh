#!/bin/bash
echo "*** isort ***"
isort .
echo "*** black ***"
black --line-length 79 .
echo "*** flake8 ***"
flake8 client server
echo "*** mypy ***"
mypy .