#!/bin/bash

coverage run --source=. -m unittest discover -v && coverage report -m --omit=*/test_*,setup.py,*__init__*,bridge/dds/* && coverage html --omit=*/test_*,setup.py,*__init__*,bridge/dds/*