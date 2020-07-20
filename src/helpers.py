import json
import re


class Helpers:
    def json_parser(self, input, attribute):
        slist = []
        my_string = json.loads(input)
        # print(response.text)
        for s in my_string:
            slist.append(s[attribute])
        return slist

    def is_email_valid(self, email):
        regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        if re.search(regex, email):
            print(email + ": is Valid Email")
            return True

        else:
            print(email + ": is Invalid Email")
            return False



