import unittest
from zendesk.custom_exceptions import RequestException, BulkExceededLimit


class TestExceptions(unittest.TestCase):

    def test_raise_with_content(self):
        content = {u'error': u"Couldn't authenticate you"}
        e = RequestException(content=content)
        self.assertEqual(e.content, content)
        self.assertEqual(e.status_code, 500)
        message = "Status: 500. Problem with the request exiting."
        self.assertEqual(e.message, message)

    def test_raise_without_content(self):
        e = RequestException()
        self.assertEqual(e.content, None)
        self.assertEqual(e.status_code, 500)
        message = "Status: 500. Problem with the request exiting."
        self.assertEqual(e.message, message)

    def test_raise_with_content_and_status_code(self):
        content = {u'error': u"Couldn't authenticate you"}
        e = RequestException(status_code=401, content=content)
        self.assertEqual(e.content, content)
        self.assertEqual(e.status_code, 401)
        message = "Status: 401. Problem with the request exiting."
        self.assertEqual(e.message, message)

    def test_raise_with_status_code_and_not_content(self):
        e = RequestException(status_code=401)
        self.assertEqual(e.content, None)
        self.assertEqual(e.status_code, 401)
        message = "Status: 401. Problem with the request exiting."
        self.assertEqual(e.message, message)

    def test_BulkExceededLimit(self):
        e = BulkExceededLimit()
        message = "The bulk can not exceed 100 objects"
        self.assertEqual(e.message, message)
