import pytest
from flask import template_rendered
from app import create_app, db as _db


def user_name(): [...]
def captured_templates(app): [...]

@pytest.fixture(scope='session')
def app(request):
   app = create_app()
   # Establish an application context before running the tests.
   ctx = app.app_context()
   ctx.push()
   def teardown():
       ctx.pop()

   request.addfinalizer(teardown)
   return app

@pytest.fixture(scope="session")
def db(app, request):
   def teardown():
       _db.drop_all()

   _db.app = app
   _db.create_all()
   request.addfinalizer(teardown)
   return _db

@pytest.fixture(scope="function")
def session(db, request):
   connection = db.engine.connect()
   transaction = connection.begin()
   session = common.Session(bind=connection)
   db.session = common.Session

   def teardown():
       transaction.rollback()
       connection.close()
       common.Session.remove()
   request.addfinalizer(teardown)
   return session
