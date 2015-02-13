# from lettuce import *
from lettuce import step
from lettuce import world
from lettuce import before
from lettuce import after
# from journal import *
from journal import main
# from journal import edit_entry

from webtest import TestApp

from journal import connect_db
from journal import DB_SCHEMA
from cryptacular.bcrypt import BCRYPTPasswordManager
from contextlib import closing

TEST_DSN = 'dbname=test_learning_journal user=JustinKan'

"""

# CREATE DB AND POPULATE
@before.all
def app():
    from journal import *
    from webtest import TestApp
    import os

    #set up and tear down a database
    settings = {'db': TEST_DSN}
    init_db(settings)

# ADD AN ENTRY SO WE CAN TEST
@before.each_feature    
def add_entry(): 
    # mock a request with a database attached
    settings = db
    req = testing.DummyRequest()
    with closing(connect_db(settings)) as db:
        req.db = db
        req.exception = None
        yield req

        # after a test has run, we clear out entries for isolation
        clear_entries(settings)
    

    os.environ['DATABASE_URL'] = TEST_DSN
    app = main()
    world.app = Testapp(app)

@after.all
def clean_up_db(settings):
    with closing(connect_db(settings)) as db:
        db.cursor().execute("DROP TABLE entries")
        db.commit()

@step(r'I go to the URL or home "(.*)"')
def access_url(step, url):
    response = world.browser.get(url)
    world.dom = html.fromstring(response.content)

@step(r'I see the permalink button "(.*)"')
def see_button(step, text):
    button = world.dom.cssselect('button')[0]
    assert button.type == text
"""


@step('given authorized user and homepage')
def authorized_edit_entry(step):
    world.authorized = True


@step('When on homepage')
def on_homepage(step):
    world.url = "http://127.0..0.1:5000/"

@step('Then I will see buttons')
def check_for_button(step):
    assert world.url == '/'





@before.all
def setup_db():
    """set up database"""
    settings = {'db': TEST_DSN}
    init_db(settings)

    return settings

@after.all
def teardown_db(total):
    """tear down a database"""
    settings = {'db': TEST_DSN}

    clear_db(settings)

def init_db(settings):
    with closing(connect_db(settings)) as db:
        db.cursor().execute(DB_SCHEMA)
        db.commit()


def clear_db(settings):
    with closing(connect_db(settings)) as db:
        db.cursor().execute("DROP TABLE entries")
        db.commit()


def clear_entries(settings):
    with closing(connect_db(settings)) as db:
        db.cursor().execute("DELETE FROM entries")
        db.commit()


def run_query(db, query, params=(), get_results=True):
    cursor = db.cursor()
    cursor.execute(query, params)
    db.commit()
    results = None
    if get_results:
        results = cursor.fetchall()
    return results
