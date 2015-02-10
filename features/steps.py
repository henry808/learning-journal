from lettuce import step
from lettuce import world

from cryptacular.bcrypt import BCRYPTPasswordManager
from pyramid import testing


@step('authorize test')
def auth_req(step):
    manager = BCRYPTPasswordManager()
    settings = {
        'auth.username': 'admin',
        'auth.password': manager.encode('secret'),
    }
    testing.setUp(settings=settings)
    req = testing.DummyRequest()
    return req




"""
@step('check if homepage')
def
"""

@step('check if edit button is present')
def see_edit_button(auth_req):

