#!/usr/bin/env bash

set -o errexit
set -o pipefail

FLASK_APP=app.py
FLASK_ENV=production
flask run --host=0.0.0.0
