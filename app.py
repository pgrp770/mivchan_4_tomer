from controller.target_controller import target_blueprint

from flask import Flask

from repository.database import drop_tables, create_tables
from seed.seed import insert_data_to_normalize_tables


def create_app():
    flask_app = Flask(__name__)
    return flask_app


if __name__ == '__main__':
    drop_tables()
    create_tables()
    insert_data_to_normalize_tables()
    app = create_app()
    app.register_blueprint(target_blueprint, url_prefix="/api/targets")
    app.run(debug=True)
