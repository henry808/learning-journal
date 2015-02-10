from lettuce import step
from lettuce import world
from lettuce import before
from lettuce import after

from journal import main
# from journal import edit_entry

from webtest import TestApp

from journal import connect_db
from journal import DB_SCHEMA
from cryptacular.bcrypt import BCRYPTPasswordManager
from contextlib import closing

TEST_DSN = 'dbname=test_learning_journal user=JustinKan'

@step('given authorized user and homepage')
def authorized_edit_entry(step):
    world.authorized = True

@step('When on homepage')
def on_homepage(step):
    world.url = 
    pass

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
>>>>>>> 83500b73b2825143e7d7418c11b9c30c27f2f1da
