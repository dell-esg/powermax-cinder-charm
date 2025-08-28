Dell PowerMax Storage Backend for Cinder
-----------------------------------------

## Overview

This charm provides a Dell PowerMax storage backend for use with the Cinder charm.

## Configuration

This section covers common and/or important configuration options. See file `config.yaml` for the full list of options, along with their descriptions and default values. See the [Juju documentation][juju-docs-config-apps] for details on configuring applications.

[juju-docs-config-apps]: https://juju.is/docs/juju/juju-config

### `protocol`

Protocol to use with the array. Can be either FC or iSCSI.

### `san-ip`

UniSphere IP used to access the array.

### `san-login`

Username used to log on UniSphere.

### `san-password`

Password used to authenticate in UniSphere.

### `powermax-array`

Serial number of the array to connect to.

### `powermax_port_groups`

List of port groups containing frontend ports configured prior for server connection.

### `powermax-service-level`

Service level to use for provisioning storage. Setting this as an extra spec in pool_name is preferable.

### `powermax-srp`
    
Storage resource pool on array to use for provisioning.

### `retries`

Use this value to specify number of retries.

### `u4p-failover-autofailback`
    
If the driver should automatically failback to the primary instance of Unisphere when a successful connection is re-established.

### `use-multipath-for-image-xfer`

Use multipath for image xfer.


## Deployment

This charm's primary use is as a backend for the cinder charm. To do so, add a relation between both charms:
   
    juju deploy --config cinder-powermax-config.yaml cinder-powermax
    juju integrate cinder-powermax:storage-backend cinder:storage-backend


# Documentation

The OpenStack Charms project maintains two documentation guides:

* [OpenStack Charm Guide][cg]: for project information, including development
  and support notes
* [OpenStack Charms Deployment Guide][cdg]: for charm usage information

[cg]: https://docs.openstack.org/charm-guide
[cdg]: https://docs.openstack.org/project-deploy-guide/charm-deployment-guide

# Bugs

Please report bugs on [Launchpad](https://bugs.launchpad.net/charm-cinder-powermax/+filebug).
