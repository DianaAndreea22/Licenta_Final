from flask import render_template
from flask import Blueprint


bp = Blueprint('errors', __name__)

def page_not_found(e):
    return render_template('errors/404.html'), 404

def internal_server_error(e):
    return render_template('errors/500.html'), 500  


def forbidden(e):
    return render_template('errors/403.html'), 403 


def initialize_error_handlers(app):
    app.register_error_handler(500, internal_server_error)
    app.register_error_handler(404, page_not_found)
    app.register_error_handler(403, forbidden)
