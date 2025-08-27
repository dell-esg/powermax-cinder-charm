from zaza.openstack.charm_tests.cinder_backend.tests import CinderBackendTest
from os import environ


class CinderPowerMaxTest(CinderBackendTest):
    """Encapsulate cinder-powermax tests."""

    backend_name = 'cinder-powermax'

    expected_config_content = {
        'cinder-powermax': {
            'volume_driver': ['cinder.volume.drivers.dell_emc.powermax.fc.PowerMaxFCDriver'],
            'san_ip': environ['TEST_VMAX_SAN_IP'],
            'san_login': environ['TEST_VMAX_SAN_USERNAME'],
            'san_password': environ['TEST_VMAX_SAN_PASSWORD']
        }}
