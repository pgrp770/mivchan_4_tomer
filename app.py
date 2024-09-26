from config.base import session_factory
from controller.target_controller import target_blueprint

from flask import Flask


def create_app():
    flask_app = Flask(__name__)
    return flask_app


if __name__ == '__main__':
    app = create_app()
    app.register_blueprint(target_blueprint, url_prefix="/api/targets")
    app.run(debug=True)
