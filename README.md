# Neutron Snap

This repository contains the source code of the snap for the OpenStack Network
service, Neutron.

This snap specifically provides the 'neutron-server' process as part of a
snap based OpenStack deployment.

## Installing this snap

The neutron snap can be installed directly from the snap store:

    sudo snap install [--edge] neutron

## Configuring Neutron

Snaps run in an AppArmor and seccomp confined profile, so don't read
configuration from `/etc/neutron` on the hosting operating system install.

This snap supports configuration via the $SNAP\_COMMON writable area for the
snap:

    etc
    ├── neutron
    │   ├── neutron.conf
    └── neutron.conf.d
        ├── database.conf
        ├── neutron-snap.conf
        └── keystone.conf

The neutron snap can be configured in a few ways.

Firstly the neutron-server daemon will detect and read `etc/neutron/neutron.conf`
if it exists so you can just place all configuration in this file.

Alternatively the neutron-server daemon will load all configuration files from
`etc/neutron.conf.d` - in the above example, database and keystone authtoken
are configured  using configuration snippets in separate files in
`etc/neutron.conf.d`.

For reference, $SNAP\_COMMON is typically located under
`/var/snap/neutron/common`.

## Managing Neutron

Currently all snap binaries must be run as root; for example, to run the
neutron-manage binary use:

    sudo neutron.manage

## Restarting Neutron services

To restart the neutron-service service:

    sudo systemctl restart snap.neutron.api

## Building the Neutron snap

Simply clone this repository and then install and run snapcraft:

    git clone https://github.com/openstack-snaps/snap-neutron
    sudo apt install snapcraft
    cd neutron
    snapcraft

## Support

Please report any bugs related to this snap on
[Launchpad](https://bugs.launchpad.net/snap-neutron/+filebug).

Alternatively you can find the OpenStack Snap team in `#openstack-snaps`
on Freenode IRC.
