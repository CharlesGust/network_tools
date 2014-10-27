import pytest
from echo_client import send_message
from echo_server import echo


def test_send_message():
    send_message("Hello")
