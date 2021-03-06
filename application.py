#!/usr/bin/env python
from __future__ import print_function
import os

import sentry_sdk

from flask import Flask
from sentry_sdk.integrations.flask import FlaskIntegration
from werkzeug.contrib.fixers import ProxyFix

from app import create_app

from dotenv import load_dotenv

load_dotenv()

sentry_sdk.init(
    dsn=os.environ.get('SENTRY_URL', ''),
    integrations=[FlaskIntegration()]
)

application = Flask('app')
application.wsgi_app = ProxyFix(application.wsgi_app)
create_app(application)
