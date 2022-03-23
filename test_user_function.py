# Tests (copy to tests/test_user_functions.py)
import pytest
import io
from email_function import *

def test_email_with_user_input_no_at_sign(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('petra.adaltas.com'))
    assert get_email_from_input() is None

def test_email_with_user_input_no_dot(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('petra@adaltascom'))
    assert get_email_from_input() is None

def test_email_with_user_input_correct(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('petra@adaltas.com'))
    assert get_email_from_input() == 'petra@adaltas.com'


def test_username_with_user_input_correct(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('wigins'))
    assert get_user_name_from_input() == 'wigins'

def test_password_with_user_input_correct(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('Fake@password'))
    assert get_password_from_input() == "At least one digit required"