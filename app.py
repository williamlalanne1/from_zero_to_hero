from flask_marshmallow import Marshmallow
from flask_smorest import Api, Blueprint, abort

ma = Marshmallow()

import os
from flask import Flask, render_template
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
   pass

basedir = os.path.abspath(os.path.dirname(__file__))
db = SQLAlchemy(model_class=Base)

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(basedir, 'data.sqlite')}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['API_TITLE'] = 'My ECM API'
    app.config["API_VERSION"] = "1"
    app.config["OPENAPI_VERSION"] = "3.0.2"
    app.config["OPENAPI_URL_PREFIX"] = "/openapi"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/api"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

    db.init_app(app)

    from tasks.models import Task

    Migrate(app, db)


    @app.route('/')
    def index():
        return '<h1>ECM Bonjour</h1>'


    @app.route('/user/<name>')
    def user(name):
        return render_template('user.html', name=name)

    @app.route('/todoz')
    def my_api_route():
        tasks = Task.query.all()
        return {
            "results": [
                {
                    field: getattr(task, field)
                    for field in Task.__table__.columns.keys()
                }
                for task in tasks
            ]
        }

    @app.route('/todoz')
    def my_better_api_route():
        tasks = Task.query.all()
        return {"results": TaskSchema(many=True).dump(tasks)}

    
    api = Api(app)
    ma.init_app(app)

    from tasks.views import task_blueprint
    api.register_blueprint(task_blueprint)


    return app


