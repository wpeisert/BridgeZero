#!/bin/bash

python -m pip install --upgrade setuptools wheel
rm dist/*
python setup.py sdist bdist_wheel
python -m pip install --upgrade twine
python -m twine upload --repository testpypi dist/*