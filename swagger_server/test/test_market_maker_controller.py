# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.order import Order  # noqa: E501
from swagger_server.test import BaseTestCase


class TestMarketMakerController(BaseTestCase):
    """MarketMakerController integration test stubs"""

    def test_place_order(self):
        """Test case for place_order

        Place an order
        """
        order = Order()
        response = self.client.open(
            '/users/{userId}/orders'.format(userId='userId_example'),
            method='POST',
            data=json.dumps(order),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
