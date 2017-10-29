#!/usr/bin/env bash
pytest
behave
pylint *.py
mypy *.py --disallow-untyped-calls --disallow-untyped-defs --python-version 3.6
