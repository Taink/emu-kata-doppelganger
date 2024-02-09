from mail_sender import MailSender, Request
from dataclasses import dataclass

@dataclass
class Response:
    code: int

@dataclass
class User:
    name: str
    email: str

class FakeHttpClient():
    def __init__(self, status_code=200):
        self.post_calls = []
        self.status_code = status_code

    def post(self, url, request):
        self.post_calls.append(request)
        return Response(self.status_code)


def test_send_v1():

    user = User("benjamin", "benjamin@hotmail.fr" )
    message = "coucou"
    fake_http_client = FakeHttpClient()
    mail_sender = MailSender(fake_http_client)
    mail_sender.send_v1(user, message)

    assert fake_http_client.post_calls[0] == Request(user.name, user.email, "New notification", message)



def test_send_v2():
    fake_http_client = FakeHttpClient(503)
    fake_message = "coucou"
    mail_sender = MailSender(fake_http_client)
    fake_user = User("benjamin" , "benjamin@hotmail.fr" )
    response = mail_sender.send_v2(fake_user, 'coucou')
    assert response == (Request(fake_user.name, fake_user.email,"New notification", fake_message))

