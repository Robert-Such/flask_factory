from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Config


db = SQLAlchemy()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    with app.app_context():
        from app.main.routes import main
        from app import models

        db.create_all()
        print("DB created")

        from dashapp.dashboard_1 import dashboard_1
        app = dashboard_1(app)
        from dashapp.dashboard_2 import dashboard_2
        app = dashboard_2(app)
        from dashapp.dashboard_3 import dashboard_3
        app = dashboard_3(app)

        app.register_blueprint(main)

        return app