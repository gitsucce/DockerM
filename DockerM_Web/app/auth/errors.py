# -*- coding: utf-8 -*-
from flask import render_template
from . import dockermAuth


@dockerm.app_errorhandler(404)
def page_not_found(e):
    return render_template('errorPage/404.html'), 404


@dockerm.app_errorhandler(500)
def internal_server_error(e):
    return render_template('errorPage/500.html'), 500

