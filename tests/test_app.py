from flask import Flask

from app import app

def test_index_route():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert "ECM" in response.data.decode("utf-8")


def test_index_user():
    client = app.test_client()
    response = client.get("/user/adrien")
    assert response.status_code == 200
    result = response.data.decode("utf-8")
    assert "Hello, adrien" in result


def test_user_template():
    client = app.test_client()
    response = client.get("/user/adrien")
    template = app.jinja_env.get_template('user.html')
    assert template.render(name="adrien") == response.get_data(as_text=True)



def test_todoz(app, client, session):
    task = TaskFactory()
    session.commit()

    response = client.get("/todoz")
    assert len(response.json["results"]) > 0
