import requests
import json
import re
import pprint
import unittest
import re
from jsonschema import validate

endpoint1 = "https://jsonplaceholder.typicode.com/users/?username=Delphine"
endpoint2 = "https://jsonplaceholder.typicode.com/comments?postId=86"
endpoint3 = "https://jsonplaceholder.typicode.com/posts?userId=9"


class RequestHandler(unittest.TestCase):
    def get_request(self, url):
        # Get post
        # string_url = endpoint2
        payload = {}
        headers = {
            'Cookie': '__cfduid=daa0cc0a478cc4ff30bf22395f5d6bb321595026425'
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        self.assertTrue(response.ok)
        return response
        # print(response.text)


if __name__ == '__main__':
    unittest.main()
