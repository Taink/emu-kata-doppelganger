from mail_sender import MailSender, Request
from unittest.mock import MagicMock, Mock
from dataclasses import dataclass

@dataclass
class Response:
    code: int

@dataclass
class User:
    name: str
    email: str

def test_send_v1():
    user = User("benjamin", "benjamin@hotmail.fr" )
    message = "coucou"
    fake_http_client = MagicMock()
    mail_sender = MailSender(fake_http_client)
    mail_sender.send_v1(user, message)
    
    expected_request = Request(user.name, user.email, "New notification", message)

    assert expected_request == fake_http_client.post.call_args.args[1]

def test_send_v2():
    fake_http_client = MagicMock()
    fake_http_client.post = Mock(return_value=Response(503))

    fake_message = "coucou"
    mail_sender = MailSender(fake_http_client)
    fake_user = User("benjamin", "benjamin@hotmail.fr")

    expected = Request(fake_user.name, fake_user.email,"New notification", fake_message)
    actual = mail_sender.send_v2(fake_user, 'coucou')

    assert fake_http_client.post.call_count > 1
    assert expected == actual
