import unittest
import base64
import responses
import json
import requests
from zendesk.base import BaseZenDesk
from zendesk.base import BaseRest
from zendesk.objects import Organization
from base_json import BaseJson


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


# import responses
# import requests

# @responses.activate
# def test_my_api():
#     responses.add(responses.GET, 'http://twitter.com/api/1/foobar',
#                   body='{"error": "not found"}', status=404,
#                   content_type='application/json')

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
        self.count_objects = 123
        self.base_json = BaseJson(base.host, self.resource, self.count_objects)

    def test_init(self):
        self.assertIsInstance(self.base_rest.base, BaseZenDesk)
        self.assertEqual(self.base_rest.class_object, Organization)
        self.assertEqual(self.base_rest.resource, self.resource)

    # @responses.activate
    # def test_get_success(self):
    #     url = "{host}{resource}.json?page={page}&per_page={per_page}".format(
    #         host=self.base_rest.base.host, resource=self.resource, page=1,
    #         per_page=10)
    #     print url
    #     body = json.dumps(self.base_json.get_json(page=1, per_page=10))
    #     responses.add(responses.GET, url, body=body, status=200,
    #                   content_type='application/json')
    #     resp = requests.get(url)
    #     print resp.json()

    @responses.activate
    def test_my_api():
        responses.add(responses.GET, 'http://twitter.com/api/1/foobar',
                      json={"error": "not found"}, status=404)

        resp = requests.get('http://twitter.com/api/1/foobar')

        assert resp.json() == {"error": "not found"}

        assert len(responses.calls) == 1
        assert responses.calls[0].request.url == 'http://twitter.com/api/1/foobar'
        assert responses.calls[0].response.text == '{"error": "not found"}'

        # resp = self.base_rest.get()
        # self.assertEqual(len(resp.get('items')), 10)
        # self.assertIsInstance(resp.get('items')[0], Organization)
        # self.assertTrue(resp.get('next_page'))
        # self.assertTrue(resp.get('previous_page'))
        # self.assertEqual(resp.get('count'), self.count_objects)
