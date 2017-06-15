# Neutron Snap

This repository contains the source code of the snap for the OpenStack Network
service, Neutron.

This snap specifically provides the 'neutron-server' process as part of a
snap based OpenStack deployment.

## Installing this snap

The neutron snap can be installed directly from the snap store:

    sudo snap install --edge neutron

The neutron snap is working towards publication across tracks for
OpenStack releases. The edge channel for each track will contain the tip
of the OpenStack project's master or stable branch, with the beta, candidate,
and stable channels being reserved for released versions. The same version
will be published progressively to beta, then candidate, and then stable once
CI validation completes for the channel. This should result in an experience
such as:

    sudo snap install --channel=ocata/stable neutron
    sudo snap install --channel=pike/edge neutron

## Configuring neutron

The neutron snap gets its default configuration from the following $SNAP
and $SNAP_COMMON locations:

    /snap/neutron/current/etc/
    └── neutron
        ├── neutron.conf
        └── plugins
            └── ml2
                └── ml2_conf.ini

    /var/snap/neutron/common/etc/
    └── neutron
        └── neutron.conf.d
            └── neutron-snap.conf

The neutron snap supports configuration updates via its $SNAP_COMMON writable
area. The default neutron configuration can be overridden as follows:

    /var/snap/neutron/common/etc/
    └── neutron
        ├── neutron.conf.d
        │   ├── neutron-snap.conf
        │   ├── database.conf
        │   ├── keystone.conf
        │   └── nova.conf
        ├── neutron.conf
        └── plugins
            └── ml2
                └── ml2_conf.ini

The neutron configuration can be overridden or augmented by writing
configuration snippets to files in the neutron.conf.d directory.

Alternatively, neutron configuration can be overridden by adding a
neutron/neutron.conf file or a neutron/plugins/ml2/ml2_conf.ini file. If
overriding in this way, you may need to update your config to point at
additional config files located in $SNAP, or add those to $SNAP_COMMON as
well.

## Logging neutron

The services for the neutron snap will log to its $SNAP_COMMON writable area:
/var/snap/neutron/common/log.

## Managing neutron

The neutron snap has alias support that enables use of the well-known
neutron-db-manage command. To enable the alias, run the following prior to
using the command:

    sudo snap alias neutron.manage neutron-db-manage

## Restarting neutron services

To restart all neutron services:

    sudo systemctl restart snap.neutron.*

or an individual service can be restarted by dropping the wildcard and
specifying the full service name.

## Building the neutron snap

Simply clone this repository and then install and run snapcraft:

    git clone https://github.com/openstack/snap-neutron
    sudo apt install snapcraft
    cd snap-neutron
    snapcraft

## Support

Please report any bugs related to this snap at:
[Launchpad](https://bugs.launchpad.net/snap-neutron/+filebug).

Alternatively you can find the OpenStack Snap team in `#openstack-snaps` on
Freenode IRC.
