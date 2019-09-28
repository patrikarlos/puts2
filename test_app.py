import requests

url = 'http://127.0.0.1:5000' # The root url of the flask app


def test_index_page():
    r = requests.get(url + '/') # Assumses that it has a path of "/"
    assert r.status_code == 200 # Assumes that it will return a 200 response


def test_addition():
    r = requests.get(url + '/add?A=10&B=20')
    assert r.status_code == 200
    assert r.text == "30 \n"


def test_subtraction():
    r = requests.get(url + '/subtract?A=10&B=20')
    assert r.status_code == 200
    assert r.text == "-10 \n"


def test_multiplication():
    r = requests.get(url + '/multiply?A=10&B=20')
    assert r.status_code == 200
    assert r.text == "200 \n"


def test_division():
    r = requests.get(url + '/divide?A=10&B=2')
    assert r.status_code == 200
    assert r.text == "5 \n"
