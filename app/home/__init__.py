from flask import render_template, Blueprint

home = Blueprint('home',__name__)

from . import views
