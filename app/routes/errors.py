from flask import render_template
from ..app import *


@app.errorhandler(404)
def not_found(error):
    return render_template('errors/404.html'), 404


@app.errorhandler(500)
def internal_server_error(error):
    return render_template('errors/500.html'), 500
