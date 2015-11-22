# encoding: utf-8
import random
import string
from datetime import datetime, timedelta


def random_string(len_str=15):
    return ''.join(random.choice(
        string.ascii_uppercase + string.digits) for _ in range(len_str))


def random_bool():
    return random.choice((True, False))


def random_int():
    return int(random.random()*100000)


def now():
    return datetime.strftime(datetime.now(), "%Y-%m-%dT%H:%M:%SZ")


def past_datetime(days_ago=None):
    days_ago = days_ago or int(random.random()*10000)
    dt = datetime.now() - timedelta(days=days_ago)
    return datetime.strftime(dt, "%Y-%m-%dT%H:%M:%SZ")


def generate_items(host, resource, qtd=100):
    start_sequence = random_int()

    def generate_item(sequence):
        return {
            "name": random_string(),
            "shared_comments": random_bool(),
            "url": "{host}/{resource}/{sequence}.json".format(
                host=host, resource=resource, sequence=sequence),
            "{}_fields".format(resource): {
                "test": "test",
            },
            "created_at": past_datetime(),
            "tags": [random_string(5), random_string(5)],
            "updated_at": now(),
            "domain_names": [],
            "details": random_string(30),
            "notes": random_string(50),
            "group_id": None,
            "external_id": random_int(),
            "id": sequence,
            "shared_tickets": random_bool()
        }
    return map(lambda x: generate_item(start_sequence+x), range(qtd))


class BaseJson(object):
    def __init__(self, host, resource, qtd):
        self.host = host
        self.resource = resource
        self.qtd = qtd
        self.items = generate_items(host, resource, qtd)

    def get_json(self, page=1, per_page=10):
        url = "{host}/{resource}".format(host=self.host, resource=self.resource)
        url_format = url + ".json?page={page}&per_page={per_page}"
        start = (page - 1)*per_page
        end = start + per_page
        has_next_page = end < self.qtd
        has_previous_page = page > 1
        next_page = url_format.format(
            page=page+1, per_page=per_page) if has_next_page else None
        previous_page = url_format.format(
            page=page-1, per_page=per_page) if has_previous_page else None
        items = self.items[start:end]
        return {
            "count": self.qtd,
            "next_page": next_page,
            "previous_page": previous_page,
            "{}".format(self.resource): items,
        }
