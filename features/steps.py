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


# FEATURE: COLORIZE
@step(u"Given an entry with ```X = Y```")
def given_an_entry_with_print_group1(step):
    assert False, 'This step must be implemented'


@step(u'When I go to the detail page with id2')
def when_i_go_to_the_detail_page_with_id2(step):
    assert False, 'This step must be implemented'


@step(u'Then I will see the tag for .codehilite')
def then_i_will_see_the_tag_for_codehilite(step):
    assert False, 'This step must be implemented'


# FEATURE: EDIT ENTRY
@step(u'Given the edit page and id of 1')
def given_the_edit_page_and_id_of_1(step):
    world.response = world.app.get('/edit/1')
    assert world.response.status_code == 200


@step(u'When I finish loading the edit page the url is edit/1')
def when_i_finish_loading_the_edit_page_the_url_is_edit_1(step):
    # checks to see if we are in edit page
    assert '<h2>Edit</h2>' in world.response.body
    assert 'Test Text' in world.response.body
    # add something that checks the url later (pull this info out of headers)
    # assert world.response.  == '/edit/1'


@step(u'Then I see the text for id 1 in the text box')
def then_i_see_the_text_for_id_1_in_the_text_box(step):
    assert 'Test' in world.response.body


@step(u'Given the edit page of id of 1')
def given_the_edit_page_of_id_of_1(step):
    world.response = world.app.get('/edit/1')
    assert world.response.status_code == 200
    # checks to see if we are in edit page
    assert '<h2>Edit</h2>' in world.response.body
    assert 'Test Text' in world.response.body


@step(u"When I change the text to 'Edit now' and submit")
def change_text_and_submit(step):
    world.response = world.app.get('/edit/1')
    assert world.response.status_code == 200
    # check to make sure text contains 'Test Text' before
    assert world.response.form['text'].value == 'Test Text'
    world.response.form['text'] = 'Edit now'
    # check to make sure text contains 'Edit now' after
    assert world.response.form['text'].value == 'Edit now'

    world.response = world.response.form.submit()

    # used these lines for debugging:

    # print world.response
    # print "form: " + str(world.response.form.fields.values())
    # print "form: " + str(world.response.form.method)
    # print "body: " + str(world.response.body)


@step(u"Then I see 'Edited now' in homepage")
def edit_shows_up(step):
    # check to see if we were redirected
    assert world.response.status_code == 302
    # check to see if we are in homepage (not written)

    world.response = world.app.get('/')
    assert 'My Python Journal' in world.response.body
    # check to see if 'Edited now' is in homepage
    assert 'Edit now' in world.response.body


# FEATURE: HOMEPAGE
@step(u'Given the homepage')
def given_the_homepage(step):
    world.response = world.app.get('/')


@step(u'When I navigate to index.html')
def when_i_navigate_to_index_html(step):
    assert world.response.status_code == 200


@step(u'Then I see the homepage')
def then_i_see_the_homepage(step):
    assert 'My Python Journal' in world.response.body


# FEATURE: MARKDOWN
@step(u'Given Entry has text with \'([^\']*)\'')
def given_entry_has_text_with_group1(step, group1):
    assert False, 'This step must be implemented'


@step(u'When I go to the detail page of id 2')
def when_i_go_to_the_detail_page_of_id_2(step):
    assert False, 'This step must be implemented'


@step(u'Then I see a H1 tag')
def then_i_see_a_h1_tag(step):
    assert False, 'This step must be implemented'


# FEATURE: PERMALINK
@step(u'Given entry with id 1')
def given_entry_with_id_1(step):
    assert False, 'This step must be implemented'


@step(u'When I go to the url')
def when_i_go_to_the_url(step):
    assert False, 'This step must be implemented'


@step(u'Then I see that it is detail/1 and the text for id 1 displays')
def then_i_see_that_it_is_detail_1_and_the_text_for_id_1_displays(step):
    assert False, 'This step must be implemented'





# @step('given authorized user and homepage')
# def authorized_edit_entry(step):
#     world.authorized = True


# @step('When on homepage')
# def on_homepage(step):
#     world.url = "http://127.0..0.1:5000/"


# @step('Then I will see buttons')
# def check_for_button(step):
#     assert world.url == '/'


# @step(u'Given an entry with      print("Text")')
# def given_an_entry_with_print_group1(step, group1):
#     assert True
#     # world.make_entry("Title", '    print("Text")')


# @step(u'When I go to the detail page with id2')
# def when_i_go_to_the_detail_page_with_id2(step):
#     # response = world.app.get('/')
#     # response.click(href='detail/2')
#     assert True
#     # assert response.status_code == 200


# @step(u'Then I will see the tag for .codehilite')
# def then_i_will_see_the_tag_for_codehilite(step):
#     # response = world.app.get('/detail/2')
#     assert True
#     # assert 'class="codehilite"' in response.body


@before.all
def setup_db():
    """set up test database"""
    # set up test database
    settings = {'db': TEST_DSN}
    with closing(connect_db(settings)) as db:
        db.cursor().execute(DB_SCHEMA)
        db.commit()
    world.settings = settings

    # setup test app
    os.environ['DATABASE_URL'] = TEST_DSN
    app = main()
    world.app = TestApp(app)
    login_data = {'username': 'admin', 'password': 'secret'}
    world.app.post('/login', params=login_data)

    # add initial entry
    world.make_entry('Test Title', 'Test Text')


@after.all
def teardown_db(total):
    """tear down a database"""
    with closing(connect_db(world.settings)) as db:
        db.cursor().execute("DROP TABLE entries")
        db.commit()


@world.absorb
def make_entry(title, text):
    data = {'title': title, 'text': text}
    response = world.app.post('/add', params=data, status='3*')
    return response


# @before.each_scenario
# def make_init_entry(scenario):
#     """mock a request with a database attached"""
#     now = datetime.datetime.utcnow()
#     expected = ('Test Title', 'Test Text', now)
#     with closing(connect_db(world.settings)) as db:
#         run_query(db, INSERT_ENTRY, expected, False)
#         db.commit()

    # world.make_entry('Test Title 2', 'Test Text')


# @after.each_scenario
# def clear_entries_after(scenario):
#     with closing(connect_db(world.settings)) as db:
#         db.cursor().execute("DELETE FROM entries")
#         db.commit()
