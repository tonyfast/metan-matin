"""Application setup"""

import os

from flask import Flask
# from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)

# load common settings for all environments
# app.config.from_object('foh.settings.default')

# load environment-specific settings, default to development

#############
# Ignore below because it is for the database
# MOdified from Foh
#############
# env = os.environ.get('FOH_ENV', 'development')
# env_settings = 'foh.settings.' + env
# app.config.from_object(env_settings)
#
# sa = SQLAlchemy(app)

# import modules containing routes

app.config['GH_USER'] = os.environ['GH_USER']
app.config['GH_KEY'] = os.environ['GH_KEY']

from metaregistry import views
