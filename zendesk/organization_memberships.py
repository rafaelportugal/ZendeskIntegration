# encoding: utf-8
from base import BaseRest
from objects import OrganizationMembership
from custom_exceptions import RequestException


class OrganizationMemberships(BaseRest):
    '''
        Customers (end-users) can be segmented into organization_memberships
        url: https://developer.zendesk.com/rest_api/docs/core/organization_memberships
    '''

    def __init__(self, base):
        super(OrganizationMemberships, self).__init__(
            base, 'organization_memberships', OrganizationMembership)

    @classmethod
    def save_bulk(self, organization_memberships):
        pass

    def get_id(self, organization_id, user_id):
        endpoint = 'organizations/{organization_id}/\
organization_memberships.json'.format(organization_id=organization_id)
        resp = self.base._request(endpoint)
        if resp.status_code == 404:
            return None

        elif resp.status_code != 200:
            content = resp.json() if getattr(resp, 'json') else {}
            raise RequestException(resp.status_code, content=content)
        resp = resp.json()
        for organization in resp['organization_memberships']:
            if organization['user_id'] == user_id:
                return organization['id']
        return None
