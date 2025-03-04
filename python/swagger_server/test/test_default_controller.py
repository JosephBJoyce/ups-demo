# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.device import Device  # noqa: E501
from swagger_server.models.package import Package  # noqa: E501
from swagger_server.models.package_response import PackageResponse  # noqa: E501
from swagger_server.models.tracking_info import TrackingInfo  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_devices_get(self):
        """Test case for devices_get

        Get list of UPS delivery devices
        """
        response = self.client.open(
            '/devices',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_packages_package_id_get(self):
        """Test case for packages_package_id_get

        Get UPS package details
        """
        response = self.client.open(
            '/packages/{packageId}'.format(package_id='package_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_packages_post(self):
        """Test case for packages_post

        Create a new UPS package
        """
        body = Package()
        response = self.client.open(
            '/packages',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_track_tracking_number_get(self):
        """Test case for track_tracking_number_get

        Track a UPS package
        """
        response = self.client.open(
            '/track/{trackingNumber}'.format(tracking_number='tracking_number_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
