from flask import Flask
import random
import string


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = random.choices(string.ascii_letters, k=24)

    from .views import views
    app.register_blueprint(views, url_prefix='/')

    return app
