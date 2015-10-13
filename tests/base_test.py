import unittest
import base64
from zendesk.base import BaseZenDesk
from zendesk.base import BaseRest
from zendesk.objects import Organization
from mock import Mock


class TestBaseZenDesk(unittest.TestCase):

    def setUp(self):
        self.hostname = "test_host"
        self.user = "john_tdd"
        self.password = "123Change"
        self.timeout = 15
        self.set_instance()

    def set_instance(self):
        self.baseZendesk = BaseZenDesk(self.hostname, self.user, self.password,
                                       self.timeout)

    def get_base64(self):
        base64string = base64.encodestring('{}:{}'.format(
            self.user, self.password))[:-1]
        return "Basic {}".format(base64string)

    def test__init__(self):
        host = "https://{}.zendesk.com/api/v2/".format(self.hostname)
        self.assertEqual(self.baseZendesk.auth, (self.user, self.password))
        self.assertEqual(self.baseZendesk.host, host)
        self.assertEqual(self.baseZendesk.timeout, self.timeout)

    def test_method_get(self):
        resource = "organizations"
        host = "https://{}.zendesk.com/api/v2/{}".format(self.hostname,
                                                         resource)
        r = self.baseZendesk._request(resource)
        auth = r.request.headers.get('Authorization')
        content_type = r.request.headers.get('Content-type')
        accept = r.request.headers.get('Accept')

        self.assertEqual(content_type, 'application/json')
        self.assertEqual(accept, 'text/plain')
        self.assertEqual(r.request.method, 'GET')
        self.assertEqual(r.request.url, host)
        self.assertEqual(auth, self.get_base64())

    def test_method_post(self):
        resource = "organizations"
        host = "https://{}.zendesk.com/api/v2/{}".format(self.hostname,
                                                         resource)
        r = self.baseZendesk._request(resource, method='POST')
        auth = r.request.headers.get('Authorization')
        content_type = r.request.headers.get('Content-type')
        accept = r.request.headers.get('Accept')

        self.assertEqual(content_type, 'application/json')
        self.assertEqual(accept, 'text/plain')
        self.assertEqual(r.request.method, 'POST')
        self.assertEqual(r.request.url, host)
        self.assertEqual(auth, self.get_base64())

    def test_method_put(self):
        resource = "organizations"
        host = "https://{}.zendesk.com/api/v2/{}".format(self.hostname,
                                                         resource)
        r = self.baseZendesk._request(resource, method='PUT')
        auth = r.request.headers.get('Authorization')
        content_type = r.request.headers.get('Content-type')
        accept = r.request.headers.get('Accept')

        self.assertEqual(content_type, 'application/json')
        self.assertEqual(accept, 'text/plain')
        self.assertEqual(r.request.method, 'PUT')
        self.assertEqual(r.request.url, host)
        self.assertEqual(auth, self.get_base64())

    def test_method_delete(self):
        resource = "organizations"
        host = "https://{}.zendesk.com/api/v2/{}".format(self.hostname,
                                                         resource)
        r = self.baseZendesk._request(resource, method='DELETE')
        auth = r.request.headers.get('Authorization')
        content_type = r.request.headers.get('Content-type')
        accept = r.request.headers.get('Accept')

        self.assertEqual(content_type, 'application/json')
        self.assertEqual(accept, 'text/plain')
        self.assertEqual(r.request.method, 'DELETE')
        self.assertEqual(r.request.url, host)
        self.assertEqual(auth, self.get_base64())


class TestBaseRest(unittest.TestCase):
    def setUp(self):
        self.hostname = "test_host"
        self.user = "john_tdd"
        self.password = "123Change"
        self.timeout = 15
        self.resource = 'Organizations'
        self.class_obj = Organization
        self.set_instance()

    def set_instance(self):
        base = BaseZenDesk(self.hostname, self.user, self.password,
                           self.timeout)
        self.base_rest = BaseRest(base, self.resource, self.class_obj)

    # def set_mock_request(self, status_code, resp_json={}):
    #     self.base_rest.base._request = Mock(status_code=status_code,
    #                                         **{'json.return_value': resp_json})

    def test_init(self):
        self.assertIsInstance(self.base_rest.base, BaseZenDesk)
        self.assertEqual(self.base_rest.class_object, Organization)
        self.assertEqual(self.base_rest.resource, self.resource)

    # def test_get(self):
    #     self.set_mock_request(200, {'test': 1})
    #     resp = self.base_rest.get()
    #     self.assertEqual(resp, {'test': 1})
