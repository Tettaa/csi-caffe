from fastapi.testclient import TestClient
from app.services import api
import json


def test_caffe_status():
    json = api.current_status()
    assert json is not None