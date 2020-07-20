import unittest
import json
import os
from src.request_handler import RequestHandler
from src.helpers import Helpers

endpoint1 = "https://jsonplaceholder.typicode.com/users/?username=Delphine"
endpoint2 = "https://jsonplaceholder.typicode.com/comments?postId="
endpoint3 = "https://jsonplaceholder.typicode.com/posts?userId="


class TestSet(unittest.TestCase):
    def setUp(self):
        response = RequestHandler.get_request(self, endpoint1)
        user_id = Helpers.json_parser(self, response.text, 'id')

        post_response = RequestHandler.get_request(self, endpoint3 + str(user_id[0]))
        global post_id
        post_id = Helpers.json_parser(self, post_response.text, 'id')

        """ for comment_id in post_id:
            comment_response = RequestHandler.get_request(self, endpoint2 + str(comment_id))
            comment_emails = Helpers.json_parser(self, comment_response.text, 'email')
            for commentemail in comment_emails:
                self.assertTrue(Helpers.is_email_valid(self, commentemail)) """

    def test_validate_comment_emails(self):
        for comment_id in post_id:
            comment_response = RequestHandler.get_request(self, endpoint2 + str(comment_id))
            comment_emails = Helpers.json_parser(self, comment_response.text, 'email')
            for comment_email in comment_emails:
               self.assertTrue(Helpers.is_email_valid(self, comment_email))

    def test_validate_empty_body(self):
        for comment_id in post_id:
            comment_response = RequestHandler.get_request(self, endpoint2 + str(comment_id))
            comment_body = Helpers.json_parser(self, comment_response.text, 'body')
            for body in comment_body:
                self.assertTrue(not str(body).__eq__(''))

    def test_validate_empty_email(self):
        for comment_id in post_id:
            comment_response = RequestHandler.get_request(self, endpoint2 + str(comment_id))
            comment_emails = Helpers.json_parser(self, comment_response.text, 'email')
            for comment_email in comment_emails:
               self.assertTrue(not str(comment_email).__eq__(''))

    def test_validate_empty_name(self):
        for comment_id in post_id:
            comment_response = RequestHandler.get_request(self, endpoint2 + str(comment_id))
            comment_names = Helpers.json_parser(self, comment_response.text, 'name')
            for comment_name in comment_names:
                self.assertTrue(not str(comment_name).__eq__(''))    


if __name__ == '__main__':
    unittest.main()
