from chalice.test import Client # type: ignore
from app import app


def test_s3_handler():
    with Client(app) as client:
        event = client.events.generate_s3_event(
            bucket='teste-lambda-with-python-rendell', key='teste.txt')
        client.lambda_.invoke('s3_handler', event)
