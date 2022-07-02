from cgi import test
import email
import imp
import unittest
from peewee import *
from requests import request

# importing TimelinePost class from the blog
from app import TimelinePost

MODELS = [TimelinePost]

# use an in-memory SQLite for tests
test_db = SqliteDatabase(':memory:')

class TestTimelinePost(unittest.TestCase):
    def setUp(self):
        # Bind model classes to test db
        # Since we have a complete list of all models, we do not need to recursively bind dependencies
        test_db.bind(MODELS, bind_refs=False, bind_backrefs=False)

        test_db.connect()
        test_db.create_tables(MODELS)

    def tearDown(self):
        # Not strictly necessary since SQLite in-memory databases only life for the duration of the connection
        test_db.drop_tables(MODELS)

        # Close connection to db
        test_db.close()

    def test_timeline_post(self):
        # Create two timeline posts
        first_post = TimelinePost.create(name='Kristen Zhang', email='intentuskristen@gmail.com', 
        content='First post with test!')
        assert first_post.id == 1

        second_post = TimelinePost.create(name='Krimsten Zhang', email='kzhan353@uwo.ca', 
        content='Second post with test!')
        assert second_post.id == 2
        # TODO: Get timeline posts and assert that they are correct
        assert (TimelinePost.get_by_id('1')) == first_post
        assert (TimelinePost.get_by_id('2')) == second_post



    