from lettuce import step
from lettuce import world

from journal import edit_entry
from cryptacular.bcrypt import BCRYPTPasswordManager
from pyramid import testing


@step('check if authorized')
def auth_req(step):
    manager = BCRYPTPasswordManager()
    settings = {
        'auth.username': 'admin',
        'auth.password': manager.encode('secret'),
    }
    testing.setUp(settings=settings)
    req = testing.DummyRequest()
    return req
