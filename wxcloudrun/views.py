from datetime import datetime
from flask import render_template, request
from run import app
from wxcloudrun.user.views import user_api


app.register_blueprint(user_api, url_prefix="/user")
