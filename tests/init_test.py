import unittest
from zendesk import Zendesk
from zendesk.tickets import Tickets
from zendesk.users import Users
from zendesk.organizations import Organizations
from zendesk.organization_memberships import OrganizationMemberships


class TestInitFile(unittest.TestCase):

    def setUp(self):
        self.hostname = "test_host"
        self.user = "john_tdd"
        self.password = "123Change"
        self.timeout = 15
        self.set_instances()

    def set_instances(self):
        self.zendesk = Zendesk(self.hostname, self.user, self.password,
                               self.timeout)

    def test_init_zendesk(self):
        self.assertIsInstance(self.zendesk.Tickets, Tickets)
        self.assertIsInstance(self.zendesk.Users, Users)
        self.assertIsInstance(self.zendesk.Organizations, Organizations)
        self.assertIsInstance(self.zendesk.OrganizationMemberships,
                              OrganizationMemberships)
