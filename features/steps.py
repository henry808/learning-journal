import datetime
import os
# from lettuce import *
from lettuce import step
from lettuce import world
from lettuce import before
from lettuce import after
# from journal import *
from journal import main
from journal import INSERT_ENTRY
from test_journal import run_query
# from journal import edit_entry

from webtest import TestApp

from journal import connect_db
from journal import DB_SCHEMA
from cryptacular.bcrypt import BCRYPTPasswordManager
from contextlib import closing

TEST_DSN = 'dbname=test_learning_journal user=JustinKan'




# @step('given authorized user and homepage')
# def authorized_edit_entry(step):
#     world.authorized = True


# @step('When on homepage')
# def on_homepage(step):
#     world.url = "http://127.0..0.1:5000/"


# @step('Then I will see buttons')
# def check_for_button(step):
#     assert world.url == '/'


@step(u'Given the edit page and id of (\d+)')
def given_the_edit_page_and_id_of_1(step, id):
    world.id = id
    assert False, 'This step must be implemented'


@step(u'When I finish loading the edit page the url is (\w+)')
def when_i_finish_loading_the_edit_page_the_url_is_edit_1(step, url_id):
    assert test == url_id
    assert False, 'This step must be implemented'


@step(u'Then I see the text for id = 1')
def then_i_see_the_text_for_id_1(step):
    assert False, 'This step must be implemented'


@step(u'Given the first entry of id 1')
def given_the_first_entry_of_id_1(step):
    assert False, 'This step must be implemented'


@step(u'When I finish editing the text and click submit')
def when_i_finish_editing_the_text_and_click_submit(step):
    assert False, 'This step must be implemented'


@step(u'Then I see the text for id = 1 in homepage')
def then_i_see_the_text_for_id_1_in_homepage(step):
    assert False, 'This step must be implemented'


@before.all
def setup_db():
    """set up database"""
    settings = {'db': TEST_DSN}
    with closing(connect_db(settings)) as db:
        db.cursor().execute(DB_SCHEMA)
        db.commit()
    world.settings = settings

    # setup test app
    app = main()
    world.app = TestApp(app)
    login_data = {'username': 'admin', 'password': 'secret'}
    world.app.post('/login', params=login_data)


@after.all
def teardown_db(total):
    """tear down a database"""
    with closing(connect_db(world.settings)) as db:
        db.cursor().execute("DROP TABLE entries")
        db.commit()



@before.each_scenario
def make_entry(scenario):
    """mock a request with a database attached"""
    now = datetime.datetime.utcnow()
    expected = ('Test Title', 'Test Text', now)
    with closing(connect_db(world.settings)) as db:
        run_query(db, INSERT_ENTRY, expected, False)
        db.commit()


@after.each_scenario
def clear_entries_after(sc):
    with closing(connect_db(world.settings)) as db:
        db.cursor().execute("DELETE FROM entries")
        db.commit()
