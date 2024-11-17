from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_read_root_retorna_ok():
    client = TestClient(app)

    res = client.get("/")

    assert res.status_code == HTTPStatus.OK
    assert res.json() == {"message": "Hello World!"}

    return res
