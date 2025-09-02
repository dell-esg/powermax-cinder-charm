#!/usr/bin/env python3

import logging
import pathlib

import jubilant

logger = logging.getLogger(__name__)

APP_NAME = "cinder-powermax"


def test_deploy_powermax(juju: jubilant.juju) -> None:
    """Deploy PowerMax Charm."""
    charm_root = Path(__file__).resolve().parents[2]

    config = {
         "protocol": "ISCSI",
         "san-login": "admin",
         "san-password": "password",
         "san-ip": "10.20.30.40",
         "powermax-array": "012345678901",
         "powermax-port-groups": "[OS-ISCSI-PG]"
         "powermax-srp": "SRP_1",
     }
    juju.deploy(pack(charm_root).resolve(), app=APP_NAME, config=config)
