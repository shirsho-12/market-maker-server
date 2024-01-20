# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.order import Order  # noqa: E501
from swagger_server.test import BaseTestCase


class TestMarketMakerController(BaseTestCase):
    """MarketMakerController integration test stubs"""

    def test_get_order_book(self):
        """Test case for get_order_book

        Get top 10 unfulfilled buy and sell orders
        """
        response = self.client.open(
            '/orderbook',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_place_order(self):
        """Test case for place_order

        Place an order
        """
        body = Order()
        response = self.client.open(
            '/users/{userId}/orders'.format(user_id='user_id_example'),
            method='POST',
            data=json.dumps(body),
            content_type='*/*')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
