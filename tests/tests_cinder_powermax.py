from zaza.openstack.charm_tests.cinder_backend.tests import CinderBackendTest
from os import environ


class CinderPowerMaxTest(CinderBackendTest):
    """Encapsulate cinder-powermax tests."""

    def test_cinder_config(self):
        """Test that configuration options match our expectations."""
        zaza.model.run_on_leader(
            "cinder",
            "sudo cp /etc/cinder/cinder.conf /tmp/",
        )
        zaza.model.block_until_oslo_config_entries_match(
            "cinder",
            "/tmp/cinder.conf",
            {
                "cinder-powermaxr": {
                    # sanity test a few common params
                    "driver": ["cinder.volume.drivers.dell_emc.powermax.fc.PowerMaxFCDriver"],
                    "volume_backend_name": ["cinder-powermaxr"],
                    "san_ip": ["10.20.30.40"],
                    "san_login": ["admin"],
                    "san_password": ["password"],
                    "powermax_array": ["0123456789012"],
                    "powermax_port_groups": ["OS-FC-PG"],
                    "powermax_srp": ["SRP_1"],
                }
            },
            timeout=2,
        )
