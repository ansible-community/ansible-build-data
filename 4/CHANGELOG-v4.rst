=======================
Ansible 4 Release Notes
=======================

This changelog describes changes since Ansible 3.0.0.

.. contents::
  :local:
  :depth: 2

v4.5.0
======

.. contents::
  :local:
  :depth: 2

Release Summary
---------------

Release Date: 2021-08-31

`Porting Guide <https://docs.ansible.com/ansible/devel/porting_guides.html>`_

Ansible-core
------------

Ansible 4.5.0 contains Ansible-core version 2.11.4.
This is a newer version than version 2.11.3 contained in the previous Ansible release.

The changes are reported in the combined changelog below.

Changed Collections
-------------------

If not mentioned explicitly, the changes are reported in the combined changelog below.

+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| Collection                    | Ansible 4.4.0 | Ansible 4.5.0 | Notes                                                                                                                        |
+===============================+===============+===============+==============================================================================================================================+
| ansible.netcommon             | 2.3.0         | 2.4.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| ansible.posix                 | 1.2.0         | 1.3.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| ansible.utils                 | 2.3.1         | 2.4.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| azure.azcollection            | 1.8.0         | 1.9.0         | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.asa                     | 2.0.2         | 2.0.3         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.intersight              | 1.0.16        | 1.0.17        | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.ios                     | 2.3.1         | 2.4.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.nxos                    | 2.5.0         | 2.5.1         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.crypto              | 1.8.0         | 1.9.2         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.digitalocean        | 1.8.0         | 1.9.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.docker              | 1.9.0         | 1.9.1         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.general             | 3.5.0         | 3.6.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.mongodb             | 1.3.0         | 1.3.1         | There are no changes recorded in the changelog.                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.mysql               | 2.1.0         | 2.1.1         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.proxysql            | 1.1.0         | 1.2.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.vmware              | 1.12.0        | 1.13.0        |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| containers.podman             | 1.6.2         | 1.7.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| hetzner.hcloud                | 1.4.4         | 1.6.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| inspur.sm                     | 1.2.0         | 1.3.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| junipernetworks.junos         | 2.4.0         | 2.5.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| netapp.ontap                  | 21.9.0        | 21.10.0       |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| ovirt.ovirt                   | 1.5.4         | 1.6.2         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| sensu.sensu_go                | 1.11.1        | 1.12.0        |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| t_systems_mms.icinga_director | 1.20.0        | 1.21.1        |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| theforeman.foreman            | 2.1.2         | 2.2.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| vyos.vyos                     | 2.5.0         | 2.5.1         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+

Major Changes
-------------

hetzner.hcloud
~~~~~~~~~~~~~~

- Introduction of placement groups

ovirt.ovirt
~~~~~~~~~~~

- remove_stale_lun - Add role for removing stale LUN (https://bugzilla.redhat.com/1966873).

Minor Changes
-------------

ansible.netcommon
~~~~~~~~~~~~~~~~~

- Add network_resource plugin to manage and provide single entry point for all resource modules for higher oder roles.

ansible.posix
~~~~~~~~~~~~~

- acl - add new alias ``recurse`` for ``recursive`` parameter (https://github.com/ansible-collections/ansible.posix/issues/124).
- added 2.11 branch to test matrix, added ignore-2.12.txt.
- authorized_key - add ``no_log=False`` in ``argument_spec`` to clear false-positives of ``no-log-needed`` (https://github.com/ansible-collections/ansible.posix/pull/156).
- authorized_key - add a list of valid key types (https://github.com/ansible-collections/ansible.posix/issues/134).
- mount - Change behavior of ``boot`` option to set ``noauto`` on BSD nodes (https://github.com/ansible-collections/ansible.posix/issues/28).
- mount - Change behavior of ``boot`` option to set ``noauto`` on Linux nodes (https://github.com/ansible-collections/ansible.posix/issues/28).
- mount - add ``no_log=False`` in ``argument_spec`` to clear false-positives of ``no-log-needed`` (https://github.com/ansible-collections/ansible.posix/pull/156).
- mount - returns ``backup_file`` value when a backup fstab is created.
- synchronize - add ``delay_updates`` option (https://github.com/ansible-collections/ansible.posix/issues/157).
- synchronize - fix typo (https://github.com/ansible-collections/ansible.posix/pull/198).

ansible.utils
~~~~~~~~~~~~~

- Add new plugin param_list_compare that generates the final param list after comparing base and provided/target param list.

cisco.ios
~~~~~~~~~

- Add support for VRF configuration under NTP server.

community.crypto
~~~~~~~~~~~~~~~~

- get_certificate - added ``starttls`` option to retrieve certificates from servers which require clients to request an encrypted connection (https://github.com/ansible-collections/community.crypto/pull/264).
- openssh_keypair - added ``diff`` support (https://github.com/ansible-collections/community.crypto/pull/260).

community.digitalocean
~~~~~~~~~~~~~~~~~~~~~~

- digital_ocean - running and enforcing psf/black in the codebase (https://github.com/ansible-collections/community.digitalocean/issues/136).
- digital_ocean_floating_ip_info - new integration test for the `digital_ocean_floating_ip_info` module (https://github.com/ansible-collections/community.digitalocean/issues/130).

community.general
~~~~~~~~~~~~~~~~~

- dig lookup plugin - add ``retry_servfail`` option (https://github.com/ansible-collections/community.general/pull/3247).
- gitlab_group_members - ``gitlab_user`` can now also be a list of users (https://github.com/ansible-collections/community.general/pull/3047).
- gitlab_group_members - added functionality to set all members exactly as given (https://github.com/ansible-collections/community.general/pull/3047).
- ini_file - add abbility to define multiple options with the same name but different values (https://github.com/ansible-collections/community.general/issues/273, https://github.com/ansible-collections/community.general/issues/1204).
- ini_file - add module option ``exclusive`` (boolean) for the ability to add/remove single ``option=value`` entries without overwriting existing options with the same name but different values (https://github.com/ansible-collections/community.general/pull/3033).
- keycloak_realm - add ``events_enabled`` parameter to allow activation or deactivation of login events (https://github.com/ansible-collections/community.general/pull/3231).
- linode inventory plugin - adds the ``ip_style`` configuration key. Set to ``api`` to get more detailed network details back from the remote Linode host (https://github.com/ansible-collections/community.general/pull/3203).
- module_helper cmd module utils - added the ``ArgFormat`` style ``BOOLEAN_NOT``, to add CLI parameters when the module argument is false-ish (https://github.com/ansible-collections/community.general/pull/3290).
- module_helper module_utils - added classmethod to trigger the execution of MH modules (https://github.com/ansible-collections/community.general/pull/3206).
- nmcli - add ``gre`` tunnel support (https://github.com/ansible-collections/community.general/issues/3105, https://github.com/ansible-collections/community.general/pull/3262).
- nmcli - query ``nmcli`` directly to determine available WiFi options (https://github.com/ansible-collections/community.general/pull/3141).
- open_iscsi - minor refactoring (https://github.com/ansible-collections/community.general/pull/3286).
- openwrt_init - minor refactoring (https://github.com/ansible-collections/community.general/pull/3284).
- pamd - minor refactorings (https://github.com/ansible-collections/community.general/pull/3285).
- redfish_info - include ``Status`` property for Thermal objects when querying Thermal properties via ``GetChassisThermals`` command (https://github.com/ansible-collections/community.general/issues/3232).
- scaleway plugin inventory - parse scw-cli config file for ``oauth_token`` (https://github.com/ansible-collections/community.general/pull/3250).
- slack - minor refactoring (https://github.com/ansible-collections/community.general/pull/3205).
- snap - improved module error handling, especially for the case when snap server is down (https://github.com/ansible-collections/community.general/issues/2970).
- tss lookup plugin - added new parameter for domain authorization (https://github.com/ansible-collections/community.general/pull/3228).
- tss lookup plugin - refactored to decouple the supporting third-party library (``python-tss-sdk``) (https://github.com/ansible-collections/community.general/pull/3252).
- vdo - minor refactoring of the code (https://github.com/ansible-collections/community.general/pull/3191).
- zfs - added diff mode support (https://github.com/ansible-collections/community.general/pull/502).
- zypper - prefix zypper commands with ``/sbin/transactional-update --continue --drop-if-no-change --quiet run`` if transactional updates are detected (https://github.com/ansible-collections/community.general/issues/3159).

community.mysql
~~~~~~~~~~~~~~~

- mysql_query - correctly reflect changed status in replace statements (https://github.com/ansible-collections/community.mysql/pull/193).

community.proxysql
~~~~~~~~~~~~~~~~~~

- refactor ``perform_checks`` function and move ``login_port`` check to ``module_utils/mysql.py`` (https://github.com/ansible-collections/community.proxysql/pull/63).

community.vmware
~~~~~~~~~~~~~~~~

- vm_device_helper - Add new functions for create, remove or reconfigure virutal NVDIMM device (https://github.com/ansible-collections/community.vmware/issues/853).
- vmware - the scenario guides from Ansible repo migrated to collection repo.
- vmware_guest - Add new parameter 'nvdimm' for add, remove or reconfigure virutal NVDIMM device of virtual machine (https://github.com/ansible-collections/community.vmware/issues/853).
- vmware_guest_disk - add the capability to create and remove RDM disks from Virtual Machines.
- vmware_guest_snapshot_info - add quiesced status in VM snapshot info (https://github.com/ansible-collections/community.vmware/pull/978)
- vmware_host_datastore - added a new parameter to expand a datastore capacity (https://github.com/ansible-collections/community.vmware/pull/915).
- vmware_host_inventory - filter hosts before templating hostnames (https://github.com/ansible-collections/community.vmware/issues/850).
- vmware_portgroup - Disable traffic shaping without defining ``traffic_shaping.average_bandwidth``, ``traffic_shaping.burst_size`` and ``traffic_shaping.peak_bandwidth`` (https://github.com/ansible-collections/community.vmware/issues/955).
- vmware_spbm - Add a new function 'find_storage_profile_by_name' (https://github.com/ansible-collections/community.vmware/issues/853).
- vmware_vm_inventory - filter guests before templating hostnames (https://github.com/ansible-collections/community.vmware/issues/850).

containers.podman
~~~~~~~~~~~~~~~~~

- Podman secret module

hetzner.hcloud
~~~~~~~~~~~~~~

- hcloud_firewall Add description field to firewall rules
- hcloud_rdns Add support for load balancer

inspur.sm
~~~~~~~~~

- The user module adds the mailbox field.

junipernetworks.junos
~~~~~~~~~~~~~~~~~~~~~

- Improve junos ospfv2 integration and unit tests coverage and router id assignment check implemented.
- Improve junos vlans integration and unit tests coverage and facts gathering logic modification.

netapp.ontap
~~~~~~~~~~~~

- na_ontap_cifs_server - ``force`` option is supported when state is absent to ignore communication errors.

ovirt.ovirt
~~~~~~~~~~~

- engine_setup - Wait for webserver up after engine-config reboot (https://github.com/oVirt/ovirt-ansible-collection/pull/324).
- hosted_engine_setup - Pause deployment on failure of `engine-backup --mode=restore` (https://github.com/oVirt/ovirt-ansible-collection/pull/327).
- hosted_engine_setup - Text change - Consistently use 'bootstrap engine VM' (https://github.com/oVirt/ovirt-ansible-collection/pull/328).
- hosted_engine_setup - Update Ansible requirements in README (https://github.com/oVirt/ovirt-ansible-collection/pull/321)
- readme - Update Ansible requirement (https://github.com/oVirt/ovirt-ansible-collection/pull/326).
- remove_stale_lun - Fix example for `remote_stale_lun` role to be able to run it from engine (https://github.com/oVirt/ovirt-ansible-collection/pull/334).

sensu.sensu_go
~~~~~~~~~~~~~~

- Add Sensu Go 6.4.0 Windows metadata.
- Add Sensu Go 6.4.1 Windows metadata.
- Add support for OracleLinux.

t_systems_mms.icinga_director
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Add event_command parameter to icinga_service_apply module (https://github.com/T-Systems-MMS/ansible-collection-icinga-director/pull/132)
- Add event_command parameter to service apply playbook to enable usage (https://github.com/T-Systems-MMS/ansible-collection-icinga-director/pull/133)

theforeman.foreman
~~~~~~~~~~~~~~~~~~

- repository - add support for filtering repositories by OS version based on API feature apidoc/v2/repositories/create.html

Deprecated Features
-------------------

ansible.netcommon
~~~~~~~~~~~~~~~~~

- network_cli - The paramiko_ssh setting ``look_for_keys`` was set automatically based on the values of the ``password`` and ``private_key_file`` options passed to network_cli. This option can now be set explicitly, and the automatic setting of ``look_for_keys`` will be removed after 2024-01-01  (https://github.com/ansible-collections/ansible.netcommon/pull/271).

cisco.ios
~~~~~~~~~

- Deprecated ios_bgp in favor of ios_bgp_global and ios_bgp_address_family.
- Remove testing with provider for ansible-test integration jobs. This helps prepare us to move to network-ee integration tests.

junipernetworks.junos
~~~~~~~~~~~~~~~~~~~~~

- Deprecated router_id from ospfv3 resource module.

Bugfixes
--------

Ansible-core
~~~~~~~~~~~~

- Fix ``when`` evaluation on Native Jinja and Python 3.10.
- Jinja2 globals should be accessible even when importing a template without the context (https://github.com/ansible/ansible/issues/75371)
- ansible-test - add packaging python module to ``ansible-doc`` sanity test requirements.
- ansible-test validate-modules - correctly validate positional parameters to ``AnsibleModules`` (https://github.com/ansible/ansible/pull/75332).
- cli defaults for ssh args set to None as '' was bypassing normal default.
- dnf module - Use all components of a package name to determine if it's installed (https://github.com/ansible/ansible/issues/75311).
- do not trigger interpreter discovery in the forced_local module path as they should use the ansible playbook python unless otherwise configured.
- find action, correctly convert path to text when warning about skiping.
- remote tmpdir permissions - fix type error in macOS chmod ACL fallback (https://github.com/ansible/ansible/pull/74613).
- template - ensure Jinja2 overrides from template header are used (https://github.com/ansible/ansible/issues/75275)
- unarchive - move failure for missing binary to ``can_handle_archive()`` rather than ``__init__()``

ansible.netcommon
~~~~~~~~~~~~~~~~~

- network_cli - Add ability to set options inherited from paramiko/libssh in ansible >= 2.11 (https://github.com/ansible-collections/ansible.netcommon/pull/271).

ansible.posix
~~~~~~~~~~~~~

- Synchronize module not recognizing remote ssh key (https://github.com/ansible-collections/ansible.posix/issues/24).
- Synchronize not using quotes around arguments like --out-format (https://github.com/ansible-collections/ansible.posix/issues/190).
- at - append line-separator to the end of the ``command`` (https://github.com/ansible-collections/ansible.posix/issues/169).
- csh - define ``ECHO`` and ``COMMAND_SEP`` (https://github.com/ansible-collections/ansible.posix/issues/204).
- firewalld - enable integration after migration (https://github.com/ansible-collections/ansible.posix/pull/239).
- firewalld - ensure idempotency with firewalld 0.9.3 (https://github.com/ansible-collections/ansible.posix/issues/179).
- firewalld - fix setting zone target to ``%%REJECT%%`` (https://github.com/ansible-collections/ansible.posix/pull/215).
- mount - Handle ``boot`` option on Solaris correctly (https://github.com/ansible-collections/ansible.posix/issues/184).
- synchronize - add ``community.podman.podman`` to the list of supported connection plugins (https://github.com/ansible-community/molecule-podman/issues/45).
- synchronize - complete podman support for synchronize module.
- synchronize - properly quote rsync CLI parameters (https://github.com/ansible-collections/ansible.posix/pull/241).
- synchronize - replace removed ``ansible_ssh_user`` by ``ansible_user`` everywhere; do the same for ``ansible_ssh_port`` and ``ansible_ssh_host`` (https://github.com/ansible-collections/ansible.posix/issues/60).
- synchronize - use SSH args from SSH connection plugin (https://github.com/ansible-collections/ansible.posix/issues/222).
- synchronize - use become_user when invoking rsync on remote with sudo (https://github.com/ansible-collections/ansible.posix/issues/186).
- sysctl - modifying conditional check for docker to fix tests being skipped (https://github.com/ansible-collections/ansible.posix/pull/226).

ansible.utils
~~~~~~~~~~~~~

- Update validate to use 2.11 ArgumentSpecValidator if available.

cisco.asa
~~~~~~~~~

- Fix TypeError argument of type 'NoneType' is not iterable in service-group when service-group does not exists.
- Fixes asa_ogs protocol object to except protocol number as input (https://github.com/ansible-collections/cisco.asa/issues/116).
- Fixes description for "passwords" parameter in documentation (https://github.com/ansible-collections/cisco.asa/issues/132).
- Implement the replace block mode that is described in the docs for asa_acl (https://github.com/ansible-collections/cisco.asa/issues/97).
- To fix asa_acls port range implementation, (https://github.com/ansible-collections/cisco.asa/issues/120, https://github.com/ansible-collections/cisco.asa/issues/121, https://github.com/ansible-collections/cisco.asa/issues/122).
- To fix asa_ogs for empty object traceback failure, (https://github.com/ansible-collections/cisco.asa/issues/124).
- To fix asa_ogs for parsing network object with ipv6 host address as expected (https://github.com/ansible-collections/cisco.asa/issues/128).

cisco.ios
~~~~~~~~~

- Logging command template fixed supporting Jinja version for centos-8 EEs.
- Updated ios_l3_interface as the newer Resource Module implementation and added features.

cisco.nxos
~~~~~~~~~~

- `nxos_facts` - Fix gathering CDP neighbor facts from certain N7Ks (https://github.com/ansible-collections/cisco.nxos/issues/329).
- `nxos_zone_zoneset` - zone member addition with smart zoning in an already existing zone should be a no-op (https://github.com/ansible-collections/cisco.nxos/issues/339).

community.crypto
~~~~~~~~~~~~~~~~

- keypair_backend module utils - simplify code to pass sanity tests (https://github.com/ansible-collections/community.crypto/pull/263).
- openssh_keypair - fixed ``cryptography`` backend to preserve original file permissions when regenerating a keypair requires existing files to be overwritten (https://github.com/ansible-collections/community.crypto/pull/260).
- openssh_keypair - fixed error handling to restore original keypair if regeneration fails (https://github.com/ansible-collections/community.crypto/pull/260).
- x509_crl - restore inherited function signature to pass sanity tests (https://github.com/ansible-collections/community.crypto/pull/263).

community.digitalocean
~~~~~~~~~~~~~~~~~~~~~~

- digital_ocean_database - increase the database creation integration test timeout (https://github.com/ansible-collections/community.digitalocean).
- digital_ocean_floating_ip - delete all Floating IPs initially during the integration test run (https://github.com/ansible-collections/community.digitalocean/issues/129).
- digitalocean inventory - respect the TRANSFORM_INVALID_GROUP_CHARS configuration setting (https://github.com/ansible-collections/community.digitalocean/pull/138).
- info modules - adding missing check mode support (https://github.com/ansible-collections/community.digitalocean/issues/139).

community.docker
~~~~~~~~~~~~~~~~

- docker_compose - fixed incorrect ``changed`` status for services with ``profiles`` defined, but none enabled (https://github.com/ansible-collections/community.docker/pull/192).

community.general
~~~~~~~~~~~~~~~~~

- apache2_module - fix ``a2enmod``/``a2dismod`` detection, and error message when not found (https://github.com/ansible-collections/community.general/issues/3253).
- django_manage - argument ``command`` is being splitted again as it should (https://github.com/ansible-collections/community.general/issues/3215).
- keycloak_realm - element type for ``events_listeners`` parameter should be ``string`` instead of ``dict`` (https://github.com/ansible-collections/community.general/pull/3231).
- launchd - use private attribute to fix sanity errors (https://github.com/ansible-collections/community.general/pull/3194).
- logdns callback plugin - improve split call to fix sanity errors (https://github.com/ansible-collections/community.general/pull/3194).
- maven_artifact - improve split call to fix sanity errors (https://github.com/ansible-collections/community.general/pull/3194).
- memcached cache plugin - change function argument names to fix sanity errors (https://github.com/ansible-collections/community.general/pull/3194).
- netapp module utils - remove always-true conditional to fix sanity errors (https://github.com/ansible-collections/community.general/pull/3194).
- nmcli - added ip4/ip6 configuration arguments for ``sit`` and ``ipip`` tunnels (https://github.com/ansible-collections/community.general/issues/3238, https://github.com/ansible-collections/community.general/pull/3239).
- one_template - change function argument name to fix sanity errors (https://github.com/ansible-collections/community.general/pull/3194).
- online inventory plugin - improve split call to fix sanity errors (https://github.com/ansible-collections/community.general/pull/3194).
- online module utils - improve split call to fix sanity errors (https://github.com/ansible-collections/community.general/pull/3194).
- open_iscsi - calling ``run_command`` with arguments as ``list`` instead of ``str`` (https://github.com/ansible-collections/community.general/pull/3286).
- openwrt_init - calling ``run_command`` with arguments as ``list`` instead of ``str`` (https://github.com/ansible-collections/community.general/pull/3284).
- packet_device - use generator to fix sanity errors (https://github.com/ansible-collections/community.general/pull/3194).
- packet_sshkey - use generator to fix sanity errors (https://github.com/ansible-collections/community.general/pull/3194).
- pamd - code for ``state=updated`` when dealing with the pam module arguments, made no distinction between ``None`` and an empty list (https://github.com/ansible-collections/community.general/issues/3260).
- proxmox_kvm - clone operation should return the VMID of the target VM and not that of the source VM. This was failing when the target VM with the chosen name already existed (https://github.com/ansible-collections/community.general/pull/3266).
- saltstack connection plugin - fix function signature (https://github.com/ansible-collections/community.general/pull/3194).
- scaleway inventory script - improve split call to fix sanity errors (https://github.com/ansible-collections/community.general/pull/3195).
- scaleway module utils - improve split call to fix sanity errors (https://github.com/ansible-collections/community.general/pull/3194).
- tss lookup plugin - fixed backwards compatibility issue with ``python-tss-sdk`` version <=0.0.5 (https://github.com/ansible-collections/community.general/issues/3192, https://github.com/ansible-collections/community.general/pull/3199).
- udm_dns_record - fixed managing of PTR records, which can never have worked before (https://github.com/ansible-collections/community.general/pull/3256).
- ufw - use generator to fix sanity errors (https://github.com/ansible-collections/community.general/pull/3194).
- vbox inventory script - change function argument name to fix sanity errors (https://github.com/ansible-collections/community.general/pull/3195).
- vdo - boolean arguments now compared with proper ``true`` and ``false`` values instead of string representations like ``"yes"`` or ``"no"`` (https://github.com/ansible-collections/community.general/pull/3191).
- zfs - treated received properties as local (https://github.com/ansible-collections/community.general/pull/502).

community.vmware
~~~~~~~~~~~~~~~~

- vmware - changed to use from isinstance to type in the if condition of option_diff method (https://github.com/ansible-collections/community.vmware/pull/983).
- vmware_guest - add message for `deploy_vm` method when it fails with timeout error while customizing the VM (https://github.com/ansible-collections/community.vmware/pull/933).
- vmware_guest_instant_clone - fixed an issue that the module should be required the guestinfo_vars parameter when executing (https://github.com/ansible-collections/community.vmware/pull/962).
- vmware_guest_powerstate - added the datacenter parameter to fix an issue that datacenter key error has been occurring (https://github.com/ansible-collections/community.vmware/pull/924).
- vmware_host_datastore - fixed an issue that the right error message isn't displayed (https://github.com/ansible-collections/community.vmware/pull/976).

hetzner.hcloud
~~~~~~~~~~~~~~

- hcloud_rdns improve error message on not existing server/Floating IP
- hcloud_server backups property defaults to None now instead of False

netapp.ontap
~~~~~~~~~~~~

- all modules - traceback on ONTAP 9.3 (and earlier) when trying to detect REST support.
- na_ontap_vserver_delete role - delete iSCSI igroups and CIFS server before deleting vserver.

ovirt.ovirt
~~~~~~~~~~~

- hosted_engine_setup - Use default bridge for IPv6 advertisements (https://github.com/oVirt/ovirt-ansible-collection/pull/331)
- ovirt_auth - Fix password and username requirements (https://github.com/oVirt/ovirt-ansible-collection/pull/325).
- ovirt_auth - Fix token no_log (https://github.com/oVirt/ovirt-ansible-collection/pull/332).
- ovirt_disk - Fix update_check with no VM (https://github.com/oVirt/ovirt-ansible-collection/pull/323).

t_systems_mms.icinga_director
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Changed place in the creation order of service object in ansible_icinga role (https://github.com/T-Systems-MMS/ansible-collection-icinga-director/pull/135)

theforeman.foreman
~~~~~~~~~~~~~~~~~~

- host, hostgroup - don't accidentally duplicate ``kt_activation_keys`` param (https://github.com/theforeman/foreman-ansible-modules/issues/1268)

vyos.vyos
~~~~~~~~~

- fix issue in firewall rules facts code when IPV6 ICMP type name in vyos.vyos.vyos_firewall_rules is not idempotent

New Modules
-----------

ansible.netcommon
~~~~~~~~~~~~~~~~~

- ansible.netcommon.network_resource - Manage resource modules

community.general
~~~~~~~~~~~~~~~~~

Identity
^^^^^^^^

Keycloak
........

- community.general.keycloak_identity_provider - Allows administration of Keycloak identity providers via Keycloak API

community.proxysql
~~~~~~~~~~~~~~~~~~

- community.proxysql.proxysql_info - Gathers information about proxysql server

containers.podman
~~~~~~~~~~~~~~~~~

- containers.podman.podman_secret - Manage podman secrets

Unchanged Collections
---------------------

- amazon.aws (still version 1.5.0)
- ansible.windows (still version 1.7.2)
- arista.eos (still version 2.2.0)
- awx.awx (still version 19.2.2)
- check_point.mgmt (still version 2.0.0)
- chocolatey.chocolatey (still version 1.1.0)
- cisco.aci (still version 2.0.0)
- cisco.iosxr (still version 2.4.0)
- cisco.meraki (still version 2.4.2)
- cisco.mso (still version 1.2.0)
- cisco.nso (still version 1.0.3)
- cisco.ucs (still version 1.6.0)
- cloudscale_ch.cloud (still version 2.2.0)
- community.aws (still version 1.5.0)
- community.azure (still version 1.0.0)
- community.fortios (still version 1.0.0)
- community.google (still version 1.0.0)
- community.grafana (still version 1.2.1)
- community.hashi_vault (still version 1.3.2)
- community.hrobot (still version 1.1.1)
- community.kubernetes (still version 1.2.1)
- community.kubevirt (still version 1.0.0)
- community.libvirt (still version 1.0.2)
- community.network (still version 3.0.0)
- community.okd (still version 1.1.2)
- community.postgresql (still version 1.4.0)
- community.rabbitmq (still version 1.1.0)
- community.routeros (still version 1.2.0)
- community.skydive (still version 1.0.0)
- community.sops (still version 1.1.0)
- community.windows (still version 1.6.0)
- community.zabbix (still version 1.4.0)
- cyberark.conjur (still version 1.1.0)
- cyberark.pas (still version 1.0.7)
- dellemc.enterprise_sonic (still version 1.1.0)
- dellemc.openmanage (still version 3.6.0)
- dellemc.os10 (still version 1.1.1)
- dellemc.os6 (still version 1.0.7)
- dellemc.os9 (still version 1.0.4)
- f5networks.f5_modules (still version 1.11.0)
- fortinet.fortimanager (still version 2.1.3)
- fortinet.fortios (still version 2.1.2)
- frr.frr (still version 1.0.3)
- gluster.gluster (still version 1.0.1)
- google.cloud (still version 1.0.2)
- hpe.nimble (still version 1.1.3)
- ibm.qradar (still version 1.0.3)
- infinidat.infinibox (still version 1.2.4)
- kubernetes.core (still version 1.2.1)
- mellanox.onyx (still version 1.0.0)
- netapp.aws (still version 21.6.0)
- netapp.azure (still version 21.8.1)
- netapp.cloudmanager (still version 21.9.0)
- netapp.elementsw (still version 21.6.1)
- netapp.um_info (still version 21.7.0)
- netapp_eseries.santricity (still version 1.2.13)
- netbox.netbox (still version 3.1.1)
- ngine_io.cloudstack (still version 2.1.0)
- ngine_io.exoscale (still version 1.0.0)
- ngine_io.vultr (still version 1.1.0)
- openstack.cloud (still version 1.5.0)
- openvswitch.openvswitch (still version 2.0.0)
- purestorage.flasharray (still version 1.10.0)
- purestorage.flashblade (still version 1.6.0)
- servicenow.servicenow (still version 1.0.6)
- splunk.es (still version 1.0.2)
- wti.remote (still version 1.0.1)

v4.4.0
======

.. contents::
  :local:
  :depth: 2

Release Summary
---------------

Release Date: 2021-08-10

`Porting Guide <https://docs.ansible.com/ansible/devel/porting_guides.html>`_

Ansible-core
------------

Ansible 4.4.0 contains Ansible-core version 2.11.3.
This is the same version of Ansible-core as in the previous Ansible release.


Changed Collections
-------------------

If not mentioned explicitly, the changes are reported in the combined changelog below.

+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| Collection             | Ansible 4.3.0 | Ansible 4.4.0 | Notes                                                                                                                        |
+========================+===============+===============+==============================================================================================================================+
| ansible.netcommon      | 2.2.0         | 2.3.0         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| ansible.utils          | 2.3.0         | 2.3.1         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| ansible.windows        | 1.7.0         | 1.7.2         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| azure.azcollection     | 1.7.0         | 1.8.0         | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.intersight       | 1.0.15        | 1.0.16        | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.ios              | 2.3.0         | 2.3.1         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.iosxr            | 2.3.0         | 2.4.0         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.nxos             | 2.4.0         | 2.5.0         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.crypto       | 1.7.1         | 1.8.0         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.docker       | 1.8.0         | 1.9.0         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.general      | 3.4.0         | 3.5.0         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.libvirt      | 1.0.1         | 1.0.2         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.mongodb      | 1.2.1         | 1.3.0         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.proxysql     | 1.0.0         | 1.1.0         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.rabbitmq     | 1.0.3         | 1.1.0         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.windows      | 1.5.0         | 1.6.0         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| containers.podman      | 1.6.1         | 1.6.2         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| dellemc.openmanage     | 3.5.0         | 3.6.0         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| f5networks.f5_modules  | 1.10.1        | 1.11.0        |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| junipernetworks.junos  | 2.3.0         | 2.4.0         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| netapp.cloudmanager    | 21.8.0        | 21.9.0        |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| netapp.ontap           | 21.8.1        | 21.9.0        |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| ovirt.ovirt            | 1.5.3         | 1.5.4         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| purestorage.flasharray | 1.9.0         | 1.10.0        |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| vyos.vyos              | 2.4.0         | 2.5.0         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+

Minor Changes
-------------

ansible.netcommon
~~~~~~~~~~~~~~~~~

- Add vlan_expander filter
- Persistent connection options (persistent_command_timeout, persistent_log_messages, etc.) have been unified across all persistent connections. New persistent connections may also now get these options by extending the connection_persistent documentation fragment.

cisco.iosxr
~~~~~~~~~~~

- Add iosxr_logging_global resource module.

cisco.nxos
~~~~~~~~~~

- Add nxos_logging_global resource module.

community.crypto
~~~~~~~~~~~~~~~~

- Avoid internal ansible-core module_utils in favor of equivalent public API available since at least Ansible 2.9 (https://github.com/ansible-collections/community.crypto/pull/253).
- openssh certificate module utils - new module_utils for parsing OpenSSH certificates (https://github.com/ansible-collections/community.crypto/pull/246).
- openssh_cert - added ``regenerate`` option to validate additional certificate parameters which trigger regeneration of an existing certificate (https://github.com/ansible-collections/community.crypto/pull/256).
- openssh_cert - adding ``diff`` support (https://github.com/ansible-collections/community.crypto/pull/255).

community.docker
~~~~~~~~~~~~~~~~

- docker_* modules - include ``ImportError`` traceback when reporting that Docker SDK for Python could not be found (https://github.com/ansible-collections/community.docker/pull/188).
- docker_compose - added ``env_file`` option for specifying custom environment files (https://github.com/ansible-collections/community.docker/pull/174).
- docker_container - added ``publish_all_ports`` option to publish all exposed ports to random ports except those explicitly bound with ``published_ports`` (this was already added in community.docker 1.8.0) (https://github.com/ansible-collections/community.docker/pull/162).
- docker_container - added new ``command_handling`` option with current deprecated default value ``compatibility`` which allows to control how the module handles shell quoting when interpreting lists, and how the module handles empty lists/strings. The default will switch to ``correct`` in community.docker 3.0.0 (https://github.com/ansible-collections/community.docker/pull/186).
- docker_container - lifted restriction preventing the creation of anonymous volumes with the ``mounts`` option (https://github.com/ansible-collections/community.docker/pull/181).

community.general
~~~~~~~~~~~~~~~~~

- apache2_module - minor refactoring improving code quality, readability and speed (https://github.com/ansible-collections/community.general/pull/3106).
- dnsimple - module rewrite to include support for python-dnsimple>=2.0.0; also add ``sandbox`` parameter (https://github.com/ansible-collections/community.general/pull/2946).
- github_repo - add new option ``api_url``  to allow working with on premises installations (https://github.com/ansible-collections/community.general/pull/3038).
- gunicorn - search for ``gunicorn`` binary in more paths (https://github.com/ansible-collections/community.general/pull/3092).
- hana_query - added the abillity to use hdbuserstore (https://github.com/ansible-collections/community.general/pull/3125).
- hpilo_info - added ``host_power_status`` return value to report power state of machine with ``OFF``, ``ON`` or ``UNKNOWN`` (https://github.com/ansible-collections/community.general/pull/3079).
- nmcli - add ``dummy`` interface support (https://github.com/ansible-collections/community.general/issues/724).
- nmcli - add ``wifi-sec`` option change detection to support managing secure Wi-Fi connections (https://github.com/ansible-collections/community.general/pull/3136).
- nmcli - add ``wifi`` option to support managing Wi-Fi settings such as ``hidden`` or ``mode`` (https://github.com/ansible-collections/community.general/pull/3081).
- pkgin - in case of ``pkgin`` tool failue, display returned standard output ``stdout`` and standard error ``stderr`` to ease debugging (https://github.com/ansible-collections/community.general/issues/3146).
- proxmox inventory plugin - added snapshots to host facts (https://github.com/ansible-collections/community.general/pull/3044).
- redfish_command - add ``boot_override_mode`` argument to BootSourceOverride commands (https://github.com/ansible-collections/community.general/issues/3134).
- supervisorctl - using standard Ansible mechanism to validate ``signalled`` state required parameter (https://github.com/ansible-collections/community.general/pull/3068).

community.mongodb
~~~~~~~~~~~~~~~~~

- 338 - role monogdb_repository - Variablize repository details.
- 345 - roles mongodb_config, mongodb_mongod, mongodb_mongos - Make security.keyFile configurable.
- 346 - roles mongodb_config, mongodb_mongod, mongodb_mongos - Allow using net.bindIpAll instead of net.bindIp.
- 347 - roles mongodb_config, mongodb_mongod, mongodb_mongos - Allow overriding net.compression.compressors in mongo*.conf

community.proxysql
~~~~~~~~~~~~~~~~~~

- Refactoring of connector presence checking (https://github.com/ansible-collections/community.proxysql/pull/50).
- Replace MySQL-Python with mysqlclient in the import error message (https://github.com/ansible-collections/community.proxysql/pull/50).
- proxysql_query_rules - added new parameters ``cache_empty_result``, ``multiplex``, ``OK_msg`` (https://github.com/ansible-collections/community.proxysql/issues/24).

community.windows
~~~~~~~~~~~~~~~~~

- win_dns_record - Added txt Support
- win_scheduled_task - Added support for setting a ``session_state_change`` trigger by documenting the human friendly values for ``state_change``
- win_scheduled_task_state - Added ``state_change_str`` to the trigger output to give a human readable description of the value

junipernetworks.junos
~~~~~~~~~~~~~~~~~~~~~

- Add junos_logging_global Resource Module.
- Add support for backup_format option in junos_config
- support l3_interface in junos vlans

netapp.cloudmanager
~~~~~~~~~~~~~~~~~~~

- na_cloudmanager - Support pd-balanced in ``gcp_volume_type`` for CVO GCP, ``provider_volume_type`` in na_cloudmanager_snapmirror and na_cloudmanager_volume.
- na_cloudmanager_connector_azure - Change default value of ``virtual_machine_size`` to Standard_DS3_v2.
- na_cloudmanager_cvo_gcp - Add selflink support on subnet_id, vpc0_node_and_data_connectivity, vpc1_cluster_connectivity, vpc2_ha_connectivity, vpc3_data_replication, subnet0_node_and_data_connectivity, subnet1_cluster_connectivity, subnet2_ha_connectivity, and subnet3_data_replication.

netapp.ontap
~~~~~~~~~~~~

- na_ontap_job_schedule - new option ``month_offset`` to explictly select 0 or 1 for January.
- na_ontap_object_store - new option ``port``, ``certificate_validation_enabled``, ``ssl_enabled`` for target server.
- na_ontap_rest_info - All Info that exist in ``na_ontap_info`` that has REST equivalents have been implemented. Note that the returned structure for REST and the variable names in the structure is different from the ZAPI based ``na_ontap_info``. Some default variables in ZAPI are no longer returned by default in REST and will need to be specified using the ``field`` option.
- na_ontap_rest_info - The Default for ``gather_subset`` has been changed to demo which returns ``cluster/software``, ``svm/svms``, ``cluster/nodes``. To return all Info must specificly list ``all`` in your playbook. Do note ``all`` is a very resource-intensive action and it is highly recommended to call just the info/APIs you need.
- na_ontap_rest_info - The following info subsets have been added ``system_node_info``, ``net_interface_info``, ``net_port_info``, ``security_login_account_info``, ``vserver_peer_info``, ``cluster_image_info``, ``cluster_log_forwarding_info``, ``metrocluster_info``, ``metrocluster_node_info``, ``net_dns_info``, ``net_interface_service_policy_info``, ``vserver_nfs_info``, ``clock_info``, ``igroup_info``, ``vscan_status_info``, ``vscan_connection_status_all_info``, ``storage_bridge_info``, ``nvme_info``, ``nvme_interface_info``, ``nvme_subsystem_info``, ``cluster_switch_info``, ``export_policy_info``, ``kerberos_realm_info``,``sis_info``, ``sis_policy_info``, ``snapmirror_info``, ``snapmirror_destination_info``, ``snapmirror_policy_info``, ``sys_cluster_alerts``, ``cifs_vserver_security_info``
- na_ontap_rest_info - added file_directory_security to return the effective permissions of the directory. When using file_directory_security it must be called with gather_subsets and path and vserver must be specified in parameters.
- na_ontap_rest_info - new option ``use_python_keys`` to replace ``svm/svms`` with ``svm_svms`` to simplify post processing.
- na_ontap_snmp - Added REST support to the SNMP module

ovirt.ovirt
~~~~~~~~~~~

- hosted_engine_setup - Allow FIPS on HE VM (https://github.com/oVirt/ovirt-ansible-collection/pull/313)

purestorage.flasharray
~~~~~~~~~~~~~~~~~~~~~~

- purefa_ds - Add ``join_ou`` parameter for AD account creation
- purefa_kmip - Add support for KMIP server management

vyos.vyos
~~~~~~~~~

- vyos_logging_global logging resource module.

Deprecated Features
-------------------

cisco.iosxr
~~~~~~~~~~~

- The iosxr_logging module has been deprecated in favor of the new iosxr_logging_global resource module and will be removed in a release after '2023-08-01'.

cisco.nxos
~~~~~~~~~~

- The nxos_logging module has been deprecated in favor of the new nxos_logging_global resource module and will be removed in a release after '2023-08-01'.

community.docker
~~~~~~~~~~~~~~~~

- docker_container - the new ``command_handling``'s default value, ``compatibility``, is deprecated and will change to ``correct`` in community.docker 3.0.0. A deprecation warning is emitted by the module in cases where the behavior will change. Please note that ansible-core will output a deprecation warning only once, so if it is shown for an earlier task, there could be more tasks with this warning where it is not shown (https://github.com/ansible-collections/community.docker/pull/186).

junipernetworks.junos
~~~~~~~~~~~~~~~~~~~~~

- The junos_logging module has been deprecated in favor of the new junos_logging_global resource module and will be removed in a release after '2023-08-01'.

vyos.vyos
~~~~~~~~~

- The vyos_logging module has been deprecated in favor of the new vyos_logging_global resource module and will be removed in a release after "2023-08-01".

Security Fixes
--------------

community.general
~~~~~~~~~~~~~~~~~

- nmcli - do not pass WiFi secrets on the ``nmcli`` command line. Use ``nmcli con edit`` instead and pass secrets as ``stdin`` (https://github.com/ansible-collections/community.general/issues/3145).

community.mongodb
~~~~~~~~~~~~~~~~~

- 312 - Set no_log True for ssl_keyfile.

community.windows
~~~~~~~~~~~~~~~~~

- win_psexec - Ensure password is masked in ``psexec_command`` return result - https://github.com/ansible-collections/community.windows/issues/43

Bugfixes
--------

ansible.utils
~~~~~~~~~~~~~

- Add support for the validation of formats to the jsonschema validator.
- Improve test coverage

ansible.windows
~~~~~~~~~~~~~~~

- win_dsc - Fix import errors when running against host that wasn't installed with the ``en-US`` locale - https://github.com/ansible-collections/ansible.windows/issues/83
- win_group - fixed ``description`` setting for a group that doesn't exist when running in check_mode (https://github.com/ansible-collections/ansible.windows/pull/260).
- win_state - Fixed the ``creationtime``, ``lastaccesstime``, and ``lastwritetime`` to report the time in UTC. This matches the ``stat`` module's behaviour and what many would expect for a epoch based timestamp - https://github.com/ansible-collections/ansible.windows/issues/240
- win_updates - Fixed ``win_updates`` output to not cast to an integer to preserve original behaviour and issues with non integer values - https://github.com/ansible-collections/ansible.windows/issues/247
- win_updates - fallback to run as SYSTEM if current user does not have batch logon rights - https://github.com/ansible-collections/ansible.windows/issues/253

cisco.ios
~~~~~~~~~

- Updated ios_command module doc example section with appropriate punctuation.
- ios_user fails to add password when configured in separate task with update_password.

cisco.iosxr
~~~~~~~~~~~

- fix issue in prefix-lists facts code when prefix-lists facts are empty. (https://github.com/ansible-collections/cisco.iosxr/pull/161)

cisco.nxos
~~~~~~~~~~

- Convert vlan lists to ranges in nxos_l2_interfaces (https://github.com/ansible-collections/cisco.nxos/issues/95).
- Do not expand direction 'both' into 'import' and 'export' for Nexus 9000 platforms (https://github.com/ansible-collections/cisco.nxos/issues/303).
- Prevent traceback when parsing unexpected line in nxos_static_routes.

community.crypto
~~~~~~~~~~~~~~~~

- openssh_cert - fixed certificate generation to restore original certificate if an error is encountered (https://github.com/ansible-collections/community.crypto/pull/255).
- openssh_keypair - fixed a bug that prevented custom file attributes being applied to public keys (https://github.com/ansible-collections/community.crypto/pull/257).

community.docker
~~~~~~~~~~~~~~~~

- docker_compose - fixes task failures when bringing up services while using ``docker-compose <1.17.0`` (https://github.com/ansible-collections/community.docker/issues/180).
- docker_container - make sure to also return ``container`` on ``detached=false`` when status code is non-zero (https://github.com/ansible-collections/community.docker/pull/178).
- docker_stack_info - make sure that module isn't skipped in check mode (https://github.com/ansible-collections/community.docker/pull/183).
- docker_stack_task_info - make sure that module isn't skipped in check mode (https://github.com/ansible-collections/community.docker/pull/183).

community.general
~~~~~~~~~~~~~~~~~

- ali_instance_info - added support to check mode (https://github.com/ansible-collections/community.general/pull/3084).
- archive - fixing archive root determination when longest common root is ``/`` (https://github.com/ansible-collections/community.general/pull/3036).
- deploy_helper - improved parameter checking by using standard Ansible construct (https://github.com/ansible-collections/community.general/pull/3104).
- django_manage - refactor to call ``run_command()`` passing command as a list instead of string (https://github.com/ansible-collections/community.general/pull/3098).
- ejabberd_user - replaced in-code check with ``required_if``, using ``get_bin_path()`` for the command, passing args to ``run_command()`` as list instead of string (https://github.com/ansible-collections/community.general/pull/3093).
- gitlab_group_members - fixes issue when gitlab group has more then 20 members, pagination problem (https://github.com/ansible-collections/community.general/issues/3041).
- gitlab_project_members - fixes issue when gitlab group has more then 20 members, pagination problem (https://github.com/ansible-collections/community.general/issues/3041).
- idrac_redfish_info - added support to check mode (https://github.com/ansible-collections/community.general/pull/3084).
- ini_file - fix inconsistency between empty value and no value (https://github.com/ansible-collections/community.general/issues/3031).
- java_cert - import private key as well as public certificate from PKCS#12 (https://github.com/ansible-collections/community.general/issues/2460).
- memset_memstore_info - added support to check mode (https://github.com/ansible-collections/community.general/pull/3084).
- memset_server_info - added support to check mode (https://github.com/ansible-collections/community.general/pull/3084).
- oneview_datacenter_info - added support to check mode (https://github.com/ansible-collections/community.general/pull/3084).
- oneview_enclosure_info - added support to check mode (https://github.com/ansible-collections/community.general/pull/3084).
- oneview_ethernet_network_info - added support to check mode (https://github.com/ansible-collections/community.general/pull/3084).
- oneview_fc_network_info - added support to check mode (https://github.com/ansible-collections/community.general/pull/3084).
- oneview_fcoe_network_info - added support to check mode (https://github.com/ansible-collections/community.general/pull/3084).
- oneview_logical_interconnect_group_info - added support to check mode (https://github.com/ansible-collections/community.general/pull/3084).
- oneview_network_set_info - added support to check mode (https://github.com/ansible-collections/community.general/pull/3084).
- oneview_san_manager_info - added support to check mode (https://github.com/ansible-collections/community.general/pull/3084).
- openbsd_pkg - fix regexp matching crash. This bug could trigger on package names with special characters, for example ``g++`` (https://github.com/ansible-collections/community.general/pull/3161).
- pids - avoid crashes for older ``psutil`` versions, like on RHEL6 and RHEL7 (https://github.com/ansible-collections/community.general/pull/2808).
- proxmox inventory plugin - fixed plugin failure when a ``qemu`` guest has no ``template`` key (https://github.com/ansible-collections/community.general/pull/3052).
- proxmox_kvm - fix result of clone, now returns ``newid`` instead of ``vmid`` (https://github.com/ansible-collections/community.general/pull/3034).
- rax_facts - added support to check mode (https://github.com/ansible-collections/community.general/pull/3084).
- redfish_info - added support to check mode (https://github.com/ansible-collections/community.general/pull/3084).
- smartos_image_info - added support to check mode (https://github.com/ansible-collections/community.general/pull/3084).
- snmp_facts - added support to check mode (https://github.com/ansible-collections/community.general/pull/3084).
- supervisorctl - state ``signalled`` was not working (https://github.com/ansible-collections/community.general/pull/3068).
- taiga - some constructs in the module fixed to work also in Python 3 (https://github.com/ansible-collections/community.general/pull/3067).
- tss lookup plugin - fixed incompatibility with ``python-tss-sdk`` version 1.0.0 (https://github.com/ansible-collections/community.general/issues/3057, https://github.com/ansible-collections/community.general/pull/3139).
- utm_aaa_group_info - added support to check mode (https://github.com/ansible-collections/community.general/pull/3084).
- utm_ca_host_key_cert_info - added support to check mode (https://github.com/ansible-collections/community.general/pull/3084).
- utm_network_interface_address_info - added support to check mode (https://github.com/ansible-collections/community.general/pull/3084).
- utm_proxy_frontend_info - added support to check mode (https://github.com/ansible-collections/community.general/pull/3084).
- utm_proxy_location_info - added support to check mode (https://github.com/ansible-collections/community.general/pull/3084).
- xenserver_facts - added support to check mode (https://github.com/ansible-collections/community.general/pull/3084).
- xfconf_info - added support to check mode (https://github.com/ansible-collections/community.general/pull/3084).

community.libvirt
~~~~~~~~~~~~~~~~~

- libvirt inventory plugin - Use FQCN for the inventory plugin name for compatibility with Ansible 2.10 and above (https://github.com/ansible-collections/community.libvirt/pull/73).

community.mongodb
~~~~~~~~~~~~~~~~~

- 315 - Fix exception handling for mongodb_stepdown module on python3.6
- 320 - Fix exception handling for modules mongodb_balancer, mongodb_shard, and mongodb_status.
- 352 - Add ansible.posix collection to dependencies list.

community.rabbitmq
~~~~~~~~~~~~~~~~~~

- rabbitmq_policy - The ``_policy_check`` piece of the policy module (``policy_data``) is typically list based on a split of the variable ``policy``. However ``policy`` in some cases does not contain data. The fix allows ``tags`` to attempt to load as json first but in the case of failure, assign ``tags`` without using the json loader (https://github.com/ansible-collections/community.rabbitmq/pull/28).

containers.podman
~~~~~~~~~~~~~~~~~

- Add meta/runtime.yml which is required for Galaxy now
- Avoid exposing pipelining support for podman connections
- Change present state to be as created state
- Disable no-hosts idempotency
- Fix idempotency with systemd podman files
- Remove idempotency for volume UID/GID

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- dellemc_idrac_storage_volume - Module fails if the BlockSize, FreeSize, or Size state of the physical disk is set to "Not Available".

f5networks.f5_modules
~~~~~~~~~~~~~~~~~~~~~

- Add syn_cookie_enable parameter to bigip_profile_fastl4 module
- Fix for bigip_firewall_rule not idempotent when using address_list as source or destination
- Fix for bigip_software_install module with state activated
- Fix for inactive volume handling issue for bigip_software_install module
- Fix snat pool issue in device info module
- Include serialNumber for ssl-certs gather_subset

junipernetworks.junos
~~~~~~~~~~~~~~~~~~~~~

- fix lacp force-up without port-priority in junos_lacp_interfaces
- fix netconf test-case for lacp revert
- junos_acls failed to parse acl when multiple addresses defined within a single term (https://github.com/ansible-collections/junipernetworks.junos/issues/190)

netapp.ontap
~~~~~~~~~~~~

- na_ontap_job_schedule - fix documentation for REST ranges for months.
- na_ontap_object_store - when using REST, wait for job status to correctly report errors.
- na_ontap_quotas - attempt to retry on ``13001:success`` ZAPI error.  Add debug data.
- na_ontap_rest_cli - removed incorrect statement indicating that console access is required.

ovirt.ovirt
~~~~~~~~~~~

- hosted_engine_setup - Use forward network during an IPv6 deployment (https://github.com/oVirt/ovirt-ansible-collection/pull/315)
- hosted_engine_setup - remove duplicate tasks (https://github.com/oVirt/ovirt-ansible-collection/pull/314)
- ovirt_permission - fix group search that has space in it's name (https://github.com/oVirt/ovirt-ansible-collection/pull/318)

vyos.vyos
~~~~~~~~~

- fix issue in route-maps facts code when route-maps facts are empty.

Known Issues
------------

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- idrac_user - Issue(192043) Module may error out with the message ``unable to perform the import or export operation because there are pending attribute changes or a configuration job is in progress``. Wait for the job to complete and run the task again.

New Plugins
-----------

Connection
~~~~~~~~~~

- community.docker.nsenter - execute on host running controller container

New Modules
-----------

cisco.iosxr
~~~~~~~~~~~

- cisco.iosxr.iosxr_logging_global - Manages logging attributes of Cisco IOSXR network devices

cisco.nxos
~~~~~~~~~~

- cisco.nxos.nxos_logging_global - Logging resource module.

community.general
~~~~~~~~~~~~~~~~~

Identity
^^^^^^^^

Keycloak
........

- community.general.keycloak_client_rolemapping - Allows administration of Keycloak client_rolemapping with the Keycloak API

Packaging
^^^^^^^^^

Language
........

- community.general.ansible_galaxy_install - Install Ansible roles or collections using ansible-galaxy

System
^^^^^^

- community.general.sap_task_list_execute - Perform SAP Task list execution
- community.general.xfconf_info - Retrieve XFCE4 configurations

community.mongodb
~~~~~~~~~~~~~~~~~

- community.mongodb.mongodb_monitoring - Manages the free monitoring feature.
- community.mongodb.mongodb_schema - Manages MongoDB Document Schema Validators.
- community.mongodb.mongodb_shard_tag - Manage Shard Tags.
- community.mongodb.mongodb_shard_zone - Manage Shard Zones.

community.proxysql
~~~~~~~~~~~~~~~~~~

- community.proxysql.proxysql_query_rules_fast_routing - Modifies query rules for fast routing policies using the proxysql admin interface

community.rabbitmq
~~~~~~~~~~~~~~~~~~

- community.rabbitmq.rabbitmq_feature_flag - Enables feature flag
- community.rabbitmq.rabbitmq_upgrade - Execute rabbitmq-upgrade commands
- community.rabbitmq.rabbitmq_user_limits - Manage RabbitMQ user limits

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- dellemc.openmanage.ome_chassis_slots - Rename sled slots on OpenManage Enterprise Modular.
- dellemc.openmanage.ome_diagnostics - Manages export of application logs and SupportAssist device collection logs from OpenManage Enterprise Modular and export of SupportAssist device collection logs from OpenManage Enterprise.

junipernetworks.junos
~~~~~~~~~~~~~~~~~~~~~

- junipernetworks.junos.junos_logging_global - Manage logging configuration on Junos devices.

purestorage.flasharray
~~~~~~~~~~~~~~~~~~~~~~

- purestorage.flasharray.purefa_kmip - Manage FlashArray KMIP server objects

Unchanged Collections
---------------------

- amazon.aws (still version 1.5.0)
- ansible.posix (still version 1.2.0)
- arista.eos (still version 2.2.0)
- awx.awx (still version 19.2.2)
- check_point.mgmt (still version 2.0.0)
- chocolatey.chocolatey (still version 1.1.0)
- cisco.aci (still version 2.0.0)
- cisco.asa (still version 2.0.2)
- cisco.meraki (still version 2.4.2)
- cisco.mso (still version 1.2.0)
- cisco.nso (still version 1.0.3)
- cisco.ucs (still version 1.6.0)
- cloudscale_ch.cloud (still version 2.2.0)
- community.aws (still version 1.5.0)
- community.azure (still version 1.0.0)
- community.digitalocean (still version 1.8.0)
- community.fortios (still version 1.0.0)
- community.google (still version 1.0.0)
- community.grafana (still version 1.2.1)
- community.hashi_vault (still version 1.3.2)
- community.hrobot (still version 1.1.1)
- community.kubernetes (still version 1.2.1)
- community.kubevirt (still version 1.0.0)
- community.mysql (still version 2.1.0)
- community.network (still version 3.0.0)
- community.okd (still version 1.1.2)
- community.postgresql (still version 1.4.0)
- community.routeros (still version 1.2.0)
- community.skydive (still version 1.0.0)
- community.sops (still version 1.1.0)
- community.vmware (still version 1.12.0)
- community.zabbix (still version 1.4.0)
- cyberark.conjur (still version 1.1.0)
- cyberark.pas (still version 1.0.7)
- dellemc.enterprise_sonic (still version 1.1.0)
- dellemc.os10 (still version 1.1.1)
- dellemc.os6 (still version 1.0.7)
- dellemc.os9 (still version 1.0.4)
- fortinet.fortimanager (still version 2.1.3)
- fortinet.fortios (still version 2.1.2)
- frr.frr (still version 1.0.3)
- gluster.gluster (still version 1.0.1)
- google.cloud (still version 1.0.2)
- hetzner.hcloud (still version 1.4.4)
- hpe.nimble (still version 1.1.3)
- ibm.qradar (still version 1.0.3)
- infinidat.infinibox (still version 1.2.4)
- inspur.sm (still version 1.2.0)
- kubernetes.core (still version 1.2.1)
- mellanox.onyx (still version 1.0.0)
- netapp.aws (still version 21.6.0)
- netapp.azure (still version 21.8.1)
- netapp.elementsw (still version 21.6.1)
- netapp.um_info (still version 21.7.0)
- netapp_eseries.santricity (still version 1.2.13)
- netbox.netbox (still version 3.1.1)
- ngine_io.cloudstack (still version 2.1.0)
- ngine_io.exoscale (still version 1.0.0)
- ngine_io.vultr (still version 1.1.0)
- openstack.cloud (still version 1.5.0)
- openvswitch.openvswitch (still version 2.0.0)
- purestorage.flashblade (still version 1.6.0)
- sensu.sensu_go (still version 1.11.1)
- servicenow.servicenow (still version 1.0.6)
- splunk.es (still version 1.0.2)
- t_systems_mms.icinga_director (still version 1.20.0)
- theforeman.foreman (still version 2.1.2)
- wti.remote (still version 1.0.1)

v4.3.0
======

.. contents::
  :local:
  :depth: 2

Release Summary
---------------

Release Date: 2021-07-20

`Porting Guide <https://docs.ansible.com/ansible/devel/porting_guides.html>`_

Ansible-core
------------

Ansible 4.3.0 contains Ansible-core version 2.11.3.
This is a newer version than version 2.11.2 contained in the previous Ansible release.

The changes are reported in the combined changelog below.

Changed Collections
-------------------

If not mentioned explicitly, the changes are reported in the combined changelog below.

+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| Collection                    | Ansible 4.2.0 | Ansible 4.3.0 | Notes                                                                                                                        |
+===============================+===============+===============+==============================================================================================================================+
| community.digitalocean        | 1.7.0         | 1.8.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.general             | 3.3.0         | 3.4.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.hashi_vault         | 1.3.0         | 1.3.2         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.postgresql          | 1.3.0         | 1.4.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.vmware              | 1.11.0        | 1.12.0        |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.zabbix              | 1.3.0         | 1.4.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| fortinet.fortimanager         | 2.1.2         | 2.1.3         | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| fortinet.fortios              | 2.1.1         | 2.1.2         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| hetzner.hcloud                | 1.4.3         | 1.4.4         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| netapp.aws                    | 21.2.0        | 21.6.0        |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| netapp.azure                  | 21.7.0        | 21.8.1        |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| netapp.cloudmanager           | 21.7.0        | 21.8.0        |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| netapp.ontap                  | 21.7.0        | 21.8.1        |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| netapp.um_info                | 21.6.0        | 21.7.0        |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| purestorage.flasharray        | 1.8.0         | 1.9.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| t_systems_mms.icinga_director | 1.18.0        | 1.20.0        |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| theforeman.foreman            | 2.1.1         | 2.1.2         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| vyos.vyos                     | 2.3.1         | 2.4.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+

Major Changes
-------------

netapp.cloudmanager
~~~~~~~~~~~~~~~~~~~

- Adding stage environment to all modules in cloudmanager

Minor Changes
-------------

Ansible-core
~~~~~~~~~~~~

- ansible-test - aws creates and exposes a new tiny_prefix variable to provide a shorter prefix for the AWS tests.

community.digitalocean
~~~~~~~~~~~~~~~~~~~~~~

- digital_ocean_database - add support for MongoDB (https://github.com/ansible-collections/community.digitalocean/issues/124).

community.general
~~~~~~~~~~~~~~~~~

- archive - added ``dest_state`` return value to describe final state of ``dest`` after successful task execution (https://github.com/ansible-collections/community.general/pull/2913).
- archive - refactoring prior to fix for idempotency checks. The fix will be a breaking change and only appear in community.general 4.0.0 (https://github.com/ansible-collections/community.general/pull/2987).
- datadog_monitor - allow creation of composite datadog monitors (https://github.com/ansible-collections/community.general/issues/2956).
- filesystem - extend support for FreeBSD. Avoid potential data loss by checking existence of a filesystem with ``fstyp`` (native command) if ``blkid`` (foreign command) doesn't find one. Add support for character devices and ``ufs`` filesystem type (https://github.com/ansible-collections/community.general/pull/2902).
- gitlab_project - add new options ``allow_merge_on_skipped_pipeline``, ``only_allow_merge_if_all_discussions_are_resolved``, ``only_allow_merge_if_pipeline_succeeds``, ``packages_enabled``, ``remove_source_branch_after_merge``, ``squash_option`` (https://github.com/ansible-collections/community.general/pull/3002).
- jenkins_job_info - the ``password`` and ``token`` parameters can also be omitted to retrieve only public information (https://github.com/ansible-collections/community.general/pull/2948).
- keycloak_authentication - enhanced diff mode to also return before and after state when the authentication flow is updated (https://github.com/ansible-collections/community.general/pull/2963).
- keycloak_client - add ``authentication_flow_binding_overrides`` option (https://github.com/ansible-collections/community.general/pull/2949).
- module_helper module utils - added feature flag parameters to ``CmdMixin`` to control whether ``rc``, ``out`` and ``err`` are automatically added to the module output (https://github.com/ansible-collections/community.general/pull/2922).
- nmcli - add ``runner`` and ``runner_hwaddr_policy`` options (https://github.com/ansible-collections/community.general/issues/2901).
- rax_mon_notification_plan - fixed validation checks by specifying type ``str`` as the ``elements`` of parameters ``ok_state``, ``warning_state`` and ``critical_state`` (https://github.com/ansible-collections/community.general/pull/2955).

community.hashi_vault
~~~~~~~~~~~~~~~~~~~~~

- hashi_vault collection - add ``execution-environment.yml`` and a python requirements file to better support ``ansible-builder`` (https://github.com/ansible-collections/community.hashi_vault/pull/105).

community.postgresql
~~~~~~~~~~~~~~~~~~~~

- postgresql_db - add support for the ``directory`` format when the ``state`` option is ``dump`` or ``restore`` (https://github.com/ansible-collections/community.postgresql/pull/108).
- postgresql_db - add the ``rename`` value to the ``state`` option (https://github.com/ansible-collections/community.postgresql/pull/107).

community.vmware
~~~~~~~~~~~~~~~~

- vmware - add processing to answer if the answer question is occurred in starting the vm (https://github.com/ansible-collections/community.vmware/pull/821).
- vmware - find_folder_by_fqpn added to support specifying folders by their fully qualified path name, defined as I(datacenter)/I(folder_type)/subfolder1/subfolder2/.
- vmware - folder field default changed from None to vm.
- vmware_content_deploy_ovf_template - storage_provisioning default changed from None to thin, in keeping with VMware best practices for flash storage.
- vmware_dvs_host - implement adding pNICs to LAGs (https://github.com/ansible-collections/community.vmware/issues/112).
- vmware_guest_instant_clone - added a new option to wait until the vmware tools start (https://github.com/ansible-collections/community.vmware/pull/904).
- vmware_guest_instant_clone - added a reboot processing to reflect the customization parameters to an instant clone vm (https://github.com/ansible-collections/community.vmware/pull/904).
- vmware_guest_powerstate - Add an option that answers whether it was copied or moved the vm if the vm is blocked (https://github.com/ansible-collections/community.vmware/pull/821).
- vmware_host_inventory - support api access via proxy (https://github.com/ansible-collections/community.vmware/pull/817).
- vmware_object_role_permission_info - added principal to provide list of individual permissions on specified entity (https://github.com/ansible-collections/community.vmware/issues/868).
- vmware_rest_client - support proxy feature for module using this API (https://github.com/ansible-collections/community.vmware/pull/848).
- vmware_vm_inventory - support api access via proxy (https://github.com/ansible-collections/community.vmware/pull/817).

community.zabbix
~~~~~~~~~~~~~~~~

- all roles were updated to support Zabbix 5.4 release (https://github.com/ansible-collections/community.zabbix/pull/405)
- new inventory plugin zabbix_inventory (https://github.com/ansible-collections/community.zabbix/pull/373)
- new module plugin zabbix_globalmacro (https://github.com/ansible-collections/community.zabbix/pull/377)
- zabbix_agent - `zabbix_agent_src_reinstall` now defaults to `False` (https://github.com/ansible-collections/community.zabbix/pull/403)
- zabbix_agent - now supports setting AllowKey (https://github.com/ansible-collections/community.zabbix/pull/358)
- zabbix_globalmacros - it is now possible to create global macros using this module (https://github.com/ansible-collections/community.zabbix/pull/377).
- zabbix_inventory - Created Ansible - Zabbix inventory plugin to create dynamic inventory from Zabbix.
- zabbix_maintenance - it is now possible to target hosts by their technical name if it differs from the visible name
- zabbix_proxy - Add MySQL Python 3 package installation.
- zabbix_server - Add MySQL Python 3 package installation.
- zabbix_server - now supports setting StartLLDProcessors (https://github.com/ansible-collections/community.zabbix/pull/361)
- zabbix_user - now supports parameter `username` as an alternative to `alias` (https://github.com/ansible-collections/community.zabbix/pull/406)
- zabbix_user - removed some of the default values because a configuration should be changed only if specified as a parameter (https://github.com/ansible-collections/community.zabbix/pull/382).
- zabbix_web - now supports setting SAML certificates (https://github.com/ansible-collections/community.zabbix/pull/408)

netapp.aws
~~~~~~~~~~

- all modules - ability to trace API calls and responses.

netapp.cloudmanager
~~~~~~~~~~~~~~~~~~~

- na_cloudmanager - Support service account with new options ``sa_client_id`` and ``sa_secret_key`` to use for API operations.

netapp.ontap
~~~~~~~~~~~~

- na_ontap_cluster_peer - new option ``peer_options`` to use different credentials on peer.
- na_ontap_debug - additional checks when REST is available to help debug vserver connectivity issues.
- na_ontap_flexcache - corrected module name in documentation Examples
- na_ontap_net_port - change option types to bool and int respectively for ``autonegotiate_admin`` and ``mtu``.
- na_ontap_net_port - new option ``up_admin`` to set administrative state.
- na_ontap_rest_info - add examples for ``parameters`` option.
- na_ontap_snapshot - add REST support to create, modify, rename, and delete snapshot.
- na_ontap_snapshot - new option ``expiry_time``.
- na_ontap_volume - show warning when resize is ignored because threshold is not reached.
- na_ontap_vserver_create role - add ``nfsv3``, ``nfsv4``, ``nfsv41`` options.
- na_ontap_vserver_peer - new option ``peer_options`` to use different credentials on peer.

netapp.um_info
~~~~~~~~~~~~~~

- all modules - ability to trace API calls and responses.
- all modules - new ``max_records`` option to limit the amount of data in a single GET response.

purestorage.flasharray
~~~~~~~~~~~~~~~~~~~~~~

- purefa_ad - Increase number of kerberos and directory servers to be 3 for each.
- purefa_ad - New module to manage Active Directory accounts
- purefa_dirsnap - New modules to manage FA-Files directory snapshots
- purefa_eradication - New module to set deleted items eradication timer
- purefa_info - Add data-at-rest and eradication timer information to default dict
- purefa_info - Add high-level count for directory quotas and details for all FA-Files policies
- purefa_info - Add volume Page 83 NAA information for volume details
- purefa_network - Add support for enable/diable FC ports
- purefa_policy - Add support for FA-files Directory Quotas and associated rules and members
- purefa_sso - Add support for setting FlashArray Single Sign-On from Pure1 Manage
- purefa_volume - Add volume Page 83 NAA information to response dict

t_systems_mms.icinga_director
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Add some more documentation on command template (https://github.com/T-Systems-MMS/ansible-collection-icinga-director/pull/128)
- add "vars" variable to icinga_notification in the role (https://github.com/T-Systems-MMS/ansible-collection-icinga-director/pull/129)
- add notification_template to role (https://github.com/T-Systems-MMS/ansible-collection-icinga-director/pull/125)

vyos.vyos
~~~~~~~~~

- Add vyos_prefix_lists Resource Module.

Deprecated Features
-------------------

community.hashi_vault
~~~~~~~~~~~~~~~~~~~~~

- hashi_vault collection - support for Python 3.5 will be dropped in version ``2.0.0`` of ``community.hashi_vault`` (https://github.com/ansible-collections/community.hashi_vault/issues/81).

Bugfixes
--------

Ansible-core
~~~~~~~~~~~~

- Add unicode support to ``ansible-inventory`` CLI (https://github.com/ansible/ansible/issues/57378)
- Ensure we get full path for extra vars into cliargs to avoid realpath issues after initial load.
- ansible-doc - in text output, do not show empty ``version_added_collection`` values (https://github.com/ansible/ansible/pull/74999).
- ansible-test - restrict ``packaging`` to ``< 21.0`` for Python ``< 3.6`` (https://github.com/ansible/ansible/pull/75186).
- command - remove unreachable code path when trying to convert the value for ``chdir`` to bytes (https://github.com/ansible/ansible/pull/75036)
- module_common - handle exception when multiple workers try to create the cache directory
- roles - make sure argspec validation task templates suboptions (https://github.com/ansible/ansible/issues/75070).
- slurp - improve the logic in the error handling and remove ``os.stat()`` call (https://github.com/ansible/ansible/pull/75038)
- ssh_connection - rename ``retries`` to ``reconnection_retries`` to avoid conflicts with task vars (https://github.com/ansible/ansible/issues/75142).
- ssh_connection - set the default for ``reconnection_retries`` back to ``0`` (https://github.com/ansible/ansible/issues/75142).
- task_executor/ssh_connection - use the ``retries`` value from ``ssh_connection`` settings, not the default from the ``Task`` field attributes (https://github.com/ansible/ansible/issues/75142).

community.digitalocean
~~~~~~~~~~~~~~~~~~~~~~

- digital_ocean - integration tests need community.general and jmespath (https://github.com/ansible-collections/community.digitalocean/issues/121).
- digital_ocean_firewall - fixed idempotence (https://github.com/ansible-collections/community.digitalocean/issues/122).

community.general
~~~~~~~~~~~~~~~~~

- archive - fixed task failure when using the ``remove`` option with a ``path`` containing nested files for ``format``s other than ``zip`` (https://github.com/ansible-collections/community.general/issues/2919).
- keycloak_authentication - fix bug when two identical executions are in the same authentication flow (https://github.com/ansible-collections/community.general/pull/2904).
- launchd - fixed sanity check in the module's code (https://github.com/ansible-collections/community.general/pull/2960).
- lvol - honor ``check_mode`` on thinpool (https://github.com/ansible-collections/community.general/issues/2934).
- module_helper module utils - avoid failing when non-zero ``rc`` is present on regular exit (https://github.com/ansible-collections/community.general/pull/2912).
- module_helper module utils - fixed change-tracking for dictionaries and lists (https://github.com/ansible-collections/community.general/pull/2951).
- npm - correctly handle cases where a dependency does not have a ``version`` property because it is either missing or invalid (https://github.com/ansible-collections/community.general/issues/2917).
- pacman - fix changed status when ignorepkg has been defined (https://github.com/ansible-collections/community.general/issues/1758).
- pamd - fixed problem with files containing only one or two lines (https://github.com/ansible-collections/community.general/issues/2925).
- proxmox inventory plugin - fixed parsing failures when some cluster nodes are offline (https://github.com/ansible-collections/community.general/issues/2931).
- redfish_command - fix extraneous error caused by missing ``bootdevice`` argument when using the ``DisableBootOverride`` sub-command (https://github.com/ansible-collections/community.general/issues/3005).
- snap - fix formatting of ``--channel`` argument when the ``channel`` option is used (https://github.com/ansible-collections/community.general/pull/3028).
- snap - fix various bugs which prevented the module from working at all, and which resulted in ``state=absent`` fail on absent snaps (https://github.com/ansible-collections/community.general/issues/2835, https://github.com/ansible-collections/community.general/issues/2906, https://github.com/ansible-collections/community.general/pull/2912).
- snap - fixed the order of the ``--classic`` parameter in the command line invocation (https://github.com/ansible-collections/community.general/issues/2916).

community.vmware
~~~~~~~~~~~~~~~~

- vmware_content_deploy_ovf_template - no longer requires host, datastore, resource_pool.
- vmware_content_deploy_xxx - deploys to recommended datastore in specified datastore_cluster.
- vmware_content_deploy_xxx - honors folder specified by fully qualified path name.
- vmware_guest - Use hostname parameter in customization only if value is not None (https://github.com/ansible-collections/community.vmware/issues/655)

community.zabbix
~~~~~~~~~~~~~~~~

- zabbix_agent - StatusPort will be configured only when `zabbix_agent2_statusport` is defined (https://github.com/ansible-collections/community.zabbix/pull/378)
- zabbix_agent - fixed issue preventing installation of zabbix-agent 4.2 on Ubuntu Focal 20.04 (https://github.com/ansible-collections/community.zabbix/pull/390)
- zabbix_agent - role will now configure correct port for hostinterface in Zabbix Server if `zabbix_agent2_listenport` is defined (https://github.com/ansible-collections/community.zabbix/pull/400)
- zabbix_agent - should no longer be failing on Windows platform due to re-running all of the tasks for the 2nd time (https://github.com/ansible-collections/community.zabbix/pull/376)
- zabbix_agent - should no longer fail while cleaning up zabbix_agent installation if Zabbix Agent2 is being used (https://github.com/ansible-collections/community.zabbix/pull/409)
- zabbix_agent - will no longer install zabbix_get package on Debian systems when `zabbix_agent_install_agent_only` is defined (https://github.com/ansible-collections/community.zabbix/pull/363)
- zabbix_host - fixed issue where module was idempotent when multiple host interfaces of the same type were present (https://github.com/ansible-collections/community.zabbix/pull/391)
- zabbix_proxy (role) - will no longer fail on proxy creation in Zabbix Server when TLS parameters are used (https://github.com/ansible-collections/community.zabbix/pull/388)
- zabbix_server - Removed the removal everything from /tmp directory command as it removes things that it shouldnt do.
- zabbix_template - first time import of template now works with Zabbix 5.4 (https://github.com/ansible-collections/community.zabbix/pull/407), please note that rerunning the task will fail as there are breaking changes in Zabbix 5.4 API that module not yet covers.
- zabbix_user - now works with Zabbix 5.4 (https://github.com/ansible-collections/community.zabbix/pull/406)

fortinet.fortios
~~~~~~~~~~~~~~~~

- Fix a regression bug caused by non-required attributes.
- Fix an intentional exception for listed options.

hetzner.hcloud
~~~~~~~~~~~~~~

- hcloud_server Improve Error Message when attaching a not existing firewall to a server
- hcloud_volume Force detaching of volumes on servers before deletion

netapp.aws
~~~~~~~~~~

- all modules - fix traceback TypeError 'NoneType' object is not subscriptable when URL points to a web server.

netapp.azure
~~~~~~~~~~~~

- Hub Automation cannot generate documentation (cannot use doc fragments from another collection).
- fix CI pipeline as azcollection does not support python 2.6.
- fix CI pipeline as ignores are not required with latest azcollection.

netapp.cloudmanager
~~~~~~~~~~~~~~~~~~~

- na_cloudmanager_aggregate - accept client_id end with or without 'clients'
- na_cloudmanager_cifs_server - accept client_id end with or without 'clients'
- na_cloudmanager_connector_aws - accept client_id end with or without 'clients'
- na_cloudmanager_connector_azure - accept client_id end with or without 'clients'
- na_cloudmanager_connector_gcp - accept client_id end with or without 'clients'
- na_cloudmanager_cvo_aws - accept client_id end with or without 'clients'
- na_cloudmanager_cvo_azure - accept client_id end with or without 'clients'
- na_cloudmanager_cvo_gcp - accept client_id end with or without 'clients'
- na_cloudmanager_info - accept client_id end with or without 'clients'
- na_cloudmanager_nss_account - accept client_id end with or without 'clients'
- na_cloudmanager_snapmirror - accept client_id end with or without 'clients'
- na_cloudmanager_volume - accept client_id end with or without 'clients'

netapp.ontap
~~~~~~~~~~~~

- all REST modules - 9.4 and 9.5 were incorrectly detected as supporting REST.
- all modules - fix traceback TypeError 'NoneType' object is not subscriptable when hostname points to a web server.
- na_ontap_cluster_peer - KeyError on dest_cluster_name if destination is unreachable.
- na_ontap_cluster_peer - KeyError on username when using certicate.
- na_ontap_export_policy_rule - change ``anonymous_user_id`` type to str to accept user name and user id.   (A warning is now triggered when a number is not quoted.)
- na_ontap_snapmirror - improve error message when option is not supported with ZAPI.
- na_ontap_volume_clone - ``parent_vserver`` can not be given with ``junction_path``, ``uid``, or ``gid``
- na_ontap_vserver_peer - KeyError on username when using certicate.

netapp.um_info
~~~~~~~~~~~~~~

- all modules - report error when connecting to a server that does not run AIQUM.
- all modules - return all records rather than the first 1000 records (mostly for volumes).
- rename na_um_list_volumes.p to na_um_list_volumes.py

purestorage.flasharray
~~~~~~~~~~~~~~~~~~~~~~

- purefa_host - Rollback host creation if initiators already used by another host
- purefa_policy - Fix incorrect protocol endpoint invocation
- purefa_ra - fix disable feature for remote assist, this didn't work due to error in check logic
- purefa_vg - Correct issue when setting or changing Volume Group QoS
- purefa_volume - Fix incorrect API version check for ActiveDR support

theforeman.foreman
~~~~~~~~~~~~~~~~~~

- activation_key - submit organization_id when querying subs, required for Katello 4.1
- content_view_version_cleanup - sort content view versions before deleting (https://github.com/RedHatSatellite/satellite-ansible-collection/issues/30, https://bugzilla.redhat.com/show_bug.cgi?id=1980274)
- content_view_version_cleanup role - properly clean up when users set keep=0 (https://bugzilla.redhat.com/show_bug.cgi?id=1974314)
- host, compute_profile - when resolving cluster and other values in vm_attrs, compare them as strings (https://github.com/theforeman/foreman-ansible-modules/issues/1245)
- subscription_info - mark ``organization`` parameter as required, to match Katello

New Plugins
-----------

Inventory
~~~~~~~~~

- community.zabbix.zabbix_inventory - Zabbix Inventory Plugin

New Modules
-----------

community.general
~~~~~~~~~~~~~~~~~

Identity
^^^^^^^^

Keycloak
........

- community.general.keycloak_clientscope - Allows administration of Keycloak client_scopes via Keycloak API
- community.general.keycloak_role - Allows administration of Keycloak roles via Keycloak API

Source Control
^^^^^^^^^^^^^^

Gitlab
......

- community.general.gitlab_protected_branch - (un)Marking existing branches for protection

community.zabbix
~~~~~~~~~~~~~~~~

- community.zabbix.zabbix_globalmacro - Create/update/delete Zabbix Global macros

netapp.ontap
~~~~~~~~~~~~

- netapp.ontap.na_ontap_cifs_local_user_set_password - NetApp ONTAP set local CIFS user password
- netapp.ontap.na_ontap_fdsd - NetApp ONTAP create or remove a File Directory security descriptor.
- netapp.ontap.na_ontap_fdsp - NetApp ONTAP create or delete a file directory security policy
- netapp.ontap.na_ontap_fdspt - NetApp ONTAP create, delete or modify File Directory security policy tasks
- netapp.ontap.na_ontap_fdss - NetApp ONTAP File Directory Security Set.
- netapp.ontap.na_ontap_partitions - NetApp ONTAP Assign partitions and disks to nodes.

purestorage.flasharray
~~~~~~~~~~~~~~~~~~~~~~

- purestorage.flasharray.purefa_ad - Manage FlashArray Active Directory Account
- purestorage.flasharray.purefa_dirsnap - Manage FlashArray File System Directory Snapshots
- purestorage.flasharray.purefa_eradication - Configure Pure Storage FlashArray Eradication Timer
- purestorage.flasharray.purefa_sso - Configure Pure Storage FlashArray Single Sign-On

vyos.vyos
~~~~~~~~~

- vyos.vyos.vyos_prefix_lists - Prefix-Lists resource module for VyOS

Unchanged Collections
---------------------

- amazon.aws (still version 1.5.0)
- ansible.netcommon (still version 2.2.0)
- ansible.posix (still version 1.2.0)
- ansible.utils (still version 2.3.0)
- ansible.windows (still version 1.7.0)
- arista.eos (still version 2.2.0)
- awx.awx (still version 19.2.2)
- azure.azcollection (still version 1.7.0)
- check_point.mgmt (still version 2.0.0)
- chocolatey.chocolatey (still version 1.1.0)
- cisco.aci (still version 2.0.0)
- cisco.asa (still version 2.0.2)
- cisco.intersight (still version 1.0.15)
- cisco.ios (still version 2.3.0)
- cisco.iosxr (still version 2.3.0)
- cisco.meraki (still version 2.4.2)
- cisco.mso (still version 1.2.0)
- cisco.nso (still version 1.0.3)
- cisco.nxos (still version 2.4.0)
- cisco.ucs (still version 1.6.0)
- cloudscale_ch.cloud (still version 2.2.0)
- community.aws (still version 1.5.0)
- community.azure (still version 1.0.0)
- community.crypto (still version 1.7.1)
- community.docker (still version 1.8.0)
- community.fortios (still version 1.0.0)
- community.google (still version 1.0.0)
- community.grafana (still version 1.2.1)
- community.hrobot (still version 1.1.1)
- community.kubernetes (still version 1.2.1)
- community.kubevirt (still version 1.0.0)
- community.libvirt (still version 1.0.1)
- community.mongodb (still version 1.2.1)
- community.mysql (still version 2.1.0)
- community.network (still version 3.0.0)
- community.okd (still version 1.1.2)
- community.proxysql (still version 1.0.0)
- community.rabbitmq (still version 1.0.3)
- community.routeros (still version 1.2.0)
- community.skydive (still version 1.0.0)
- community.sops (still version 1.1.0)
- community.windows (still version 1.5.0)
- containers.podman (still version 1.6.1)
- cyberark.conjur (still version 1.1.0)
- cyberark.pas (still version 1.0.7)
- dellemc.enterprise_sonic (still version 1.1.0)
- dellemc.openmanage (still version 3.5.0)
- dellemc.os10 (still version 1.1.1)
- dellemc.os6 (still version 1.0.7)
- dellemc.os9 (still version 1.0.4)
- f5networks.f5_modules (still version 1.10.1)
- frr.frr (still version 1.0.3)
- gluster.gluster (still version 1.0.1)
- google.cloud (still version 1.0.2)
- hpe.nimble (still version 1.1.3)
- ibm.qradar (still version 1.0.3)
- infinidat.infinibox (still version 1.2.4)
- inspur.sm (still version 1.2.0)
- junipernetworks.junos (still version 2.3.0)
- kubernetes.core (still version 1.2.1)
- mellanox.onyx (still version 1.0.0)
- netapp.elementsw (still version 21.6.1)
- netapp_eseries.santricity (still version 1.2.13)
- netbox.netbox (still version 3.1.1)
- ngine_io.cloudstack (still version 2.1.0)
- ngine_io.exoscale (still version 1.0.0)
- ngine_io.vultr (still version 1.1.0)
- openstack.cloud (still version 1.5.0)
- openvswitch.openvswitch (still version 2.0.0)
- ovirt.ovirt (still version 1.5.3)
- purestorage.flashblade (still version 1.6.0)
- sensu.sensu_go (still version 1.11.1)
- servicenow.servicenow (still version 1.0.6)
- splunk.es (still version 1.0.2)
- wti.remote (still version 1.0.1)

v4.2.0
======

.. contents::
  :local:
  :depth: 2

Release Summary
---------------

Release Date: 2021-06-29

`Porting Guide <https://docs.ansible.com/ansible/devel/porting_guides.html>`_

Ansible-core
------------

Ansible 4.2.0 contains Ansible-core version 2.11.2.
This is a newer version than version 2.11.1 contained in the previous Ansible release.

The changes are reported in the combined changelog below.

Changed Collections
-------------------

If not mentioned explicitly, the changes are reported in the combined changelog below.

+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| Collection                    | Ansible 4.1.0 | Ansible 4.2.0 | Notes                                                                                                                        |
+===============================+===============+===============+==============================================================================================================================+
| ansible.netcommon             | 2.1.0         | 2.2.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| ansible.utils                 | 2.2.0         | 2.3.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| ansible.windows               | 1.6.0         | 1.7.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| arista.eos                    | 2.1.2         | 2.2.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| awx.awx                       | 19.2.0        | 19.2.2        | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.ios                     | 2.2.0         | 2.3.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.iosxr                   | 2.2.0         | 2.3.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.meraki                  | 2.4.0         | 2.4.2         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.nxos                    | 2.3.0         | 2.4.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.crypto              | 1.7.0         | 1.7.1         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.digitalocean        | 1.5.1         | 1.7.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.docker              | 1.7.0         | 1.8.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.general             | 3.2.0         | 3.3.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.hashi_vault         | 1.1.3         | 1.3.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.routeros            | 1.1.0         | 1.2.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.sops                | 1.0.6         | 1.1.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.vmware              | 1.10.0        | 1.11.0        |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.windows             | 1.4.0         | 1.5.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| dellemc.openmanage            | 3.4.0         | 3.5.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| f5networks.f5_modules         | 1.9.1         | 1.10.1        |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| fortinet.fortimanager         | 2.0.3         | 2.1.2         | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| fortinet.fortios              | 2.0.2         | 2.1.1         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| junipernetworks.junos         | 2.2.0         | 2.3.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| netapp_eseries.santricity     | 1.2.12        | 1.2.13        |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| openstack.cloud               | 1.4.0         | 1.5.0         | The collection did not have a changelog in this version.                                                                     |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| ovirt.ovirt                   | 1.5.0         | 1.5.3         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| t_systems_mms.icinga_director | 1.17.0        | 1.18.0        | The collection did not have a changelog in this version.                                                                     |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| theforeman.foreman            | 2.1.0         | 2.1.1         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| vyos.vyos                     | 2.3.0         | 2.3.1         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+

Major Changes
-------------

community.vmware
~~~~~~~~~~~~~~~~

- vmware_object_custom_attributes_info - added a new module to gather custom attributes of an object (https://github.com/ansible-collections/community.vmware/pull/851).

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- idrac_server_config_profile - Added support for exporting and importing Server Configuration Profile through HTTP/HTTPS share.
- ome_device_group - Added support for adding devices to a group using the IP addresses of the devices and group ID.

fortinet.fortios
~~~~~~~~~~~~~~~~

- New module fortios_monitor_fact.
- Support Fortios 7.0.
- Support Log APIs.

Minor Changes
-------------

ansible.netcommon
~~~~~~~~~~~~~~~~~

- Add variable to control ProxyCommand with libssh connection.
- NetworkTemplate and ResouceModule base classes have been moved under module_utils.network.common.rm_base. Stubs have been kept for backwards compatibility. These will be removed after 2023-01-01. Please update imports for existing modules that subclass them. The `cli_rm_builder <https://github.com/ansible-network/cli_rm_builder>`_ has been updated to use the new imports.

ansible.utils
~~~~~~~~~~~~~

- Add usable_range test plugin

ansible.windows
~~~~~~~~~~~~~~~

- win_updates - Added ``accept_list`` and ``reject_list`` to replace ``whitelist`` and ``blacklist``
- win_updates - Added ``failure_msg`` result to the return value of each update that gives a human readable error message if the update failed to download or install
- win_updates - Added ``filtered_reasons`` that list all the reasons why the update has been filtered - https://github.com/ansible-collections/ansible.windows/issues/226
- win_updates - Added progress logs to display on higher verbosities the download and install progress for each host
- win_updates - Added the ``downloaded`` result to the return value of each update to indicate if an update was downloaded or not
- win_updates - Added the category ``*`` that matches all categories
- win_updates - Improve Windows Update HRESULT error messages
- win_updates - Improve the details present in the ``log_path`` log entries for better monitoring

arista.eos
~~~~~~~~~~

- Add eos_prefix_lists resource module.

cisco.ios
~~~~~~~~~

- Deprecated next_hop_self type bool and introduced nexthop_self as dict under bgp_address_family.
- Move ios_config idempotent warning message with the task response under `warnings` key if `changed` is `True`
- PR adds the implementation of object group param to acls source and destination parameters (https://github.com/ansible-collections/cisco.ios/issues/339).
- PR to fix the bgp global activate rendering and fix bgp address family round trip failure (https://github.com/ansible-collections/cisco.ios/issues/353).
- To add ospfv2 passive_interfaces param with added functionality (https://github.com/ansible-collections/cisco.ios/issues/336).
- To add updated prefix lists and route maps params to Bgp AF RM (https://github.com/ansible-collections/cisco.ios/issues/267).
- To update prefix list and acls merge behaviour and update prefix list description position in model (https://github.com/ansible-collections/cisco.ios/issues/345).

cisco.iosxr
~~~~~~~~~~~

- Add `iosxr_prefix_lists` resource module.

cisco.nxos
~~~~~~~~~~

- Add `advertise_l2vpn_evpn` option in `nxos_bgp_address_family` module (https://github.com/ansible-collections/cisco.nxos/issues/302).
- Add `nxos_prefix_lists` resource module.

community.digitalocean
~~~~~~~~~~~~~~~~~~~~~~

- digital_ocean_kubernetes - set "latest" as the default version for new clusters (https://github.com/ansible-collections/community.digitalocean/issues/114).

community.docker
~~~~~~~~~~~~~~~~

- Avoid internal ansible-core module_utils in favor of equivalent public API available since at least Ansible 2.9 (https://github.com/ansible-collections/community.docker/pull/164).
- docker_compose - added ``profiles`` option to specify service profiles when starting services (https://github.com/ansible-collections/community.docker/pull/167).
- docker_containers inventory plugin - when ``connection_type=docker-api``, now pass Docker daemon connection options from inventory plugin to connection plugin. This can be disabled by setting ``configure_docker_daemon=false`` (https://github.com/ansible-collections/community.docker/pull/157).
- docker_host_info - allow values for keys in ``containers_filters``, ``images_filters``, ``networks_filters``, and ``volumes_filters`` to be passed as YAML lists (https://github.com/ansible-collections/community.docker/pull/160).
- docker_plugin - added ``alias`` option to specify local names for docker plugins (https://github.com/ansible-collections/community.docker/pull/161).

community.general
~~~~~~~~~~~~~~~~~

- Avoid internal ansible-core module_utils in favor of equivalent public API available since at least Ansible 2.9 (https://github.com/ansible-collections/community.general/pull/2877).
- datadog_event - adding parameter ``api_host`` to allow selecting a datadog API endpoint instead of using the default one (https://github.com/ansible-collections/community.general/issues/2774, https://github.com/ansible-collections/community.general/pull/2775).
- flatpak - allows installing or uninstalling a list of packages (https://github.com/ansible-collections/community.general/pull/2521).
- gem - add ``bindir`` option to specify an installation path for executables such as ``/home/user/bin`` or ``/home/user/.local/bin`` (https://github.com/ansible-collections/community.general/pull/2837).
- gem - add ``norc`` option to avoid loading any ``.gemrc`` file (https://github.com/ansible-collections/community.general/pull/2837).
- gitlab_project - projects can be created under other user's namespaces with the new ``username`` option (https://github.com/ansible-collections/community.general/pull/2824).
- gitlab_user - add functionality for adding external identity providers to a GitLab user (https://github.com/ansible-collections/community.general/pull/2691).
- gitlab_user - allow to reset an existing password with the new ``reset_password`` option (https://github.com/ansible-collections/community.general/pull/2691).
- gitlab_user - specifying a password is no longer necessary (https://github.com/ansible-collections/community.general/pull/2691).
- jenkins_build - support stopping a running jenkins build (https://github.com/ansible-collections/community.general/pull/2850).
- jenkins_plugin - add fallback url(s) for failure of plugin installation/download (https://github.com/ansible-collections/community.general/pull/1334).
- nmcli - add ``disabled`` value to ``method6`` option (https://github.com/ansible-collections/community.general/issues/2730).
- nmcli - add ``routing_rules4`` and ``may_fail4`` options (https://github.com/ansible-collections/community.general/issues/2730).
- nrdp callback plugin - parameters are now converted to strings, except ``validate_certs`` which is converted to boolean (https://github.com/ansible-collections/community.general/pull/2878).
- redhat_subscription - add ``server_prefix`` and ``server_port`` parameters (https://github.com/ansible-collections/community.general/pull/2779).
- redis - allow to use the term ``replica`` instead of ``slave``, which has been the official Redis terminology since 2018 (https://github.com/ansible-collections/community.general/pull/2867).
- snap - added ``enabled`` and ``disabled`` states (https://github.com/ansible-collections/community.general/issues/1990).
- splunk callback plugin - add ``batch`` option for user-configurable correlation ID's (https://github.com/ansible-collections/community.general/issues/2790).
- terraform - add ``check_destroy`` optional parameter to check for deletion of resources before it is applied (https://github.com/ansible-collections/community.general/pull/2874).
- timezone - print error message to debug instead of warning when timedatectl fails (https://github.com/ansible-collections/community.general/issues/1942).

community.hashi_vault
~~~~~~~~~~~~~~~~~~~~~

- hashi_vault lookup - add ``ANSIBLE_HASHI_VAULT_CA_CERT`` env var (with ``VAULT_CACERT`` low-precedence fallback) for ``ca_cert`` option (https://github.com/ansible-collections/community.hashi_vault/pull/97).
- hashi_vault lookup - add ``ANSIBLE_HASHI_VAULT_PASSWORD`` env var and ``ansible_hashi_vault_password`` ansible var for ``password`` option (https://github.com/ansible-collections/community.hashi_vault/pull/96).
- hashi_vault lookup - add ``ANSIBLE_HASHI_VAULT_USERNAME`` env var and ``ansible_hashi_vault_username`` ansible var for ``username`` option (https://github.com/ansible-collections/community.hashi_vault/pull/96).
- hashi_vault lookup - add ``ansible_hashi_vault_auth_method`` Ansible vars entry to the ``proxies`` option (https://github.com/ansible-collections/community.hashi_vault/pull/86).
- hashi_vault lookup - add ``ansible_hashi_vault_ca_cert`` ansible var for ``ca_cert`` option (https://github.com/ansible-collections/community.hashi_vault/pull/97).
- hashi_vault lookup - add ``ansible_hashi_vault_namespace`` Ansible vars entry to the ``namespace`` option (https://github.com/ansible-collections/community.hashi_vault/pull/86).
- hashi_vault lookup - add ``ansible_hashi_vault_proxies`` Ansible vars entry to the ``proxies`` option (https://github.com/ansible-collections/community.hashi_vault/pull/86).
- hashi_vault lookup - add ``ansible_hashi_vault_role_id`` Ansible vars entry to the ``proxies`` option (https://github.com/ansible-collections/community.hashi_vault/pull/86).
- hashi_vault lookup - add ``ansible_hashi_vault_secret_id`` Ansible vars entry to the ``proxies`` option (https://github.com/ansible-collections/community.hashi_vault/pull/86).
- hashi_vault lookup - add ``ansible_hashi_vault_token_file`` Ansible vars entry to the ``token_file`` option (https://github.com/ansible-collections/community.hashi_vault/pull/95).
- hashi_vault lookup - add ``ansible_hashi_vault_token_path`` Ansible vars entry to the ``token_path`` option (https://github.com/ansible-collections/community.hashi_vault/pull/95).
- hashi_vault lookup - add ``ansible_hashi_vault_token_validate`` Ansible vars entry to the ``proxies`` option (https://github.com/ansible-collections/community.hashi_vault/pull/86).
- hashi_vault lookup - add ``ansible_hashi_vault_token`` Ansible vars entry to the ``proxies`` option (https://github.com/ansible-collections/community.hashi_vault/pull/86).
- hashi_vault lookup - add ``ansible_hashi_vault_url`` and ``ansible_hashi_vault_addr`` Ansible vars entries to the ``url`` option (https://github.com/ansible-collections/community.hashi_vault/pull/86).
- hashi_vault lookup - add ``ansible_hashi_vault_validate_certs`` Ansible vars entry to the ``validate_certs`` option (https://github.com/ansible-collections/community.hashi_vault/pull/95).
- hashi_vault lookup - add ``ca_cert`` INI config file key ``ca_cert`` option (https://github.com/ansible-collections/community.hashi_vault/pull/97).
- hashi_vault lookup - add ``none`` auth type which allows for passive auth via a Vault agent (https://github.com/ansible-collections/community.hashi_vault/pull/80).
- hashi_vault lookup - add ``retries`` and ``retry_action`` to enable built-in retry on failure (https://github.com/ansible-collections/community.hashi_vault/pull/71).
- hashi_vault lookup - add ``timeout`` option to control connection timeouts (https://github.com/ansible-collections/community.hashi_vault/pull/100).

community.routeros
~~~~~~~~~~~~~~~~~~

- Avoid internal ansible-core module_utils in favor of equivalent public API available since at least Ansible 2.9 (https://github.com/ansible-collections/community.routeros/pull/38).
- api - add options ``validate_certs`` (default value ``true``), ``validate_cert_hostname`` (default value ``false``), and ``ca_path`` to control certificate validation (https://github.com/ansible-collections/community.routeros/pull/37).
- api - rename option ``ssl`` to ``tls``, and keep the old name as an alias (https://github.com/ansible-collections/community.routeros/pull/37).
- fact - add fact ``ansible_net_config_nonverbose`` to get idempotent config (no date, no verbose) (https://github.com/ansible-collections/community.routeros/pull/23).

community.sops
~~~~~~~~~~~~~~

- Avoid internal ansible-core module_utils in favor of equivalent public API available since at least Ansible 2.9 (https://github.com/ansible-collections/community.sops/pull/73).

community.vmware
~~~~~~~~~~~~~~~~

- vmware - added a new method to search Managed Object based on moid and object type (https://github.com/ansible-collections/community.vmware/pull/879).
- vmware_dvswitch - Dynamically check the DVS versions vCenter supports (https://github.com/ansible-collections/community.vmware/issues/839).
- vmware_dvswitch - Implement network_policy parameter with suboptions promiscuous, forged_transmits and mac_changes (https://github.com/ansible-collections/community.vmware/issues/833).
- vmware_guest - Make the requirements for Virtualization Based Security explicit (https://github.com/ansible-collections/community.vmware/pull/816).
- vmware_guest - New parameter ``secure_boot`` to manage (U)EFI secure boot on VMs (https://github.com/ansible-collections/community.vmware/pull/816).
- vmware_guest - New parameter ``vvtd`` to manage Intel Virtualization Technology for Directed I/O on VMs (https://github.com/ansible-collections/community.vmware/pull/816).
- vmware_guest_controller - added bus_sharing property to scsi controllers (https://github.com/ansible-collections/community.vmware/pull/878).
- vmware_guest_instant_clone - added the the guestinfo_vars parameter to provide GuestOS Customization functionality in instant cloned VM (https://github.com/ansible-collections/community.vmware/pull/796).
- vmware_host_custom_attributes - new module (https://github.com/ansible-collections/community.vmware/pull/838).
- vmware_host_inventory - added ability for username to be a vault encrypted variable, and updated documentation to reflect ability for username and password to be vaulted. (https://github.com/ansible-collections/community.vmware/issues/854).
- vmware_host_passthrough - added a new module to enable or disable passthrough of PCI devices with ESXi host has (https://github.com/ansible-collections/community.vmware/pull/872).
- vmware_host_tcpip_stacks - added ipv6_gateway parameter and nsx_overlay as an alias of vxlan (https://github.com/ansible-collections/community.vmware/pull/834).
- vmware_host_vmnic_info - add LLDP information to output when applicable (https://github.com/ansible-collections/community.vmware/pull/828).
- vmware_object_custom_attributes_info - added a new parameter to support moid (https://github.com/ansible-collections/community.vmware/pull/879).
- vmware_vcenter_settings.py - Add advanced_settings parameter (https://github.com/ansible-collections/community.vmware/pull/819).
- vmware_vm_inventory - added ability for username to be a vault encrypted variable, and updated documentation to reflect ability for username and password to be vaulted. (https://github.com/ansible-collections/community.vmware/issues/854).

f5networks.f5_modules
~~~~~~~~~~~~~~~~~~~~~

- Add address_matches_with_external_datagroup condition to bigip_policy_rule module
- Add persistence target for disable action to bigip_policy_rule module
- Add rule_order parameter to bigip_policy_rule module

junipernetworks.junos
~~~~~~~~~~~~~~~~~~~~~

- Add junos_prefix_lists Resource Module.

ovirt.ovirt
~~~~~~~~~~~

- Don't rely on safe_eval being able to do math/concat (https://github.com/oVirt/ovirt-ansible-collection/pull/307)
- hosted_engine_setup - Do not try to sync at end of full_execution (https://github.com/oVirt/ovirt-ansible-collection/pull/305)
- hosted_engine_setup - Fix engine vm add_host for the target machine (https://github.com/oVirt/ovirt-ansible-collection/pull/311)
- hosted_engine_setup - Minor doc update (https://github.com/oVirt/ovirt-ansible-collection/pull/310)
- hosted_engine_setup - use-ansible-host (https://github.com/oVirt/ovirt-ansible-collection/pull/277).
- infra role - Add external_provider parameter on networks role of infra role (https://github.com/oVirt/ovirt-ansible-collection/pull/297)
- ovirt_vm - Add default return value to check_placement_policy (https://github.com/oVirt/ovirt-ansible-collection/pull/301).
- ovirt_vm - Add placement_policy_hosts (https://github.com/oVirt/ovirt-ansible-collection/pull/294).

Deprecated Features
-------------------

- The community.kubernetes collection is being renamed to kubernetes.core. In Ansible 5, community.kubernetes will be replaced by an empty collection which has deprecated redirects for all the current content to kubernetes.core. If you are using FQCNs starting with ``community.kubernetes.``, please update them to ``kubernetes.core.`` now. Note that kubernetes.core has been included in Ansible since Ansible 3.0.0 (https://github.com/ansible-community/community-topics/issues/22).

ansible.windows
~~~~~~~~~~~~~~~

- win_updates - Deprecated the ``filtered_reason`` return value for each filtered up in favour of ``filtered_reasons``. This has been done to show all the reasons why an update was filtered and not just the first reason.
- win_updates - Deprecated the ``use_scheduled_task`` option as it is no longer used.
- win_updates - Deprecated the ``whitelist`` and ``blacklist`` options in favour of ``accept_list`` and ``reject_list`` respectively to conform to the new standards used in Ansible for these types of options.

community.general
~~~~~~~~~~~~~~~~~

- ali_instance_info - marked removal version of deprecated parameters ``availability_zone`` and ``instance_names`` (https://github.com/ansible-collections/community.general/issues/2429).
- serverless - deprecating parameter ``functions`` because it was not used in the code (https://github.com/ansible-collections/community.general/pull/2845).

community.hashi_vault
~~~~~~~~~~~~~~~~~~~~~

- hashi_vault collection - support for Python 2 will be dropped in version ``2.0.0`` of ``community.hashi_vault`` (https://github.com/ansible-collections/community.hashi_vault/issues/81).

Security Fixes
--------------

Ansible-core
~~~~~~~~~~~~

- templating engine fix for not preserving usnafe status when trying to preserve newlines. CVE-2021-3583

Bugfixes
--------

Ansible-core
~~~~~~~~~~~~

- AnsibleModule.set_mode_if_different - don't check file existence when check_mode is activated (https://github.com/ansible/ansible/issues/61185).
- Apply ``display_failed_stderr`` callback option on loop item results. (https://github.com/ansible/ansible/issues/74864)
- Avoid task executor from ending early as vars can come from delegated to host.
- ansible-pull - update documentation for ``--directory`` option to clarify path must be absolute.
- config, ensure 'quoted' lists from ini or env do not take the quotes literally as part of the list item.
- gather_facts, package, service - fix using module_defaults for the modules in addition to the action plugins. (https://github.com/ansible/ansible/issues/72918)
- psrp - Always cleanup the last run pipeline if a second pipeline is invoked to avoid violating any resource limits.
- psrp - Fix error when resetting a connection that was initialised but not connected - (https://github.com/ansible/ansible/issues/74092).
- psrp - Try to clean up any server-side resources when resetting a connection.
- roles - make sure argspec validation task is tagged with ``always`` (https://github.com/ansible/ansible/pull/74994).
- slurp - Fix error messages for unreadable files and directories (https://github.com/ansible/ansible/issues/67340).
- slurp - handle error when ``path`` is a directory and not a file (https://github.com/ansible/ansible/pull/74930).
- ssh connection - fix interaction between transfer settings options.
- subversion - fix stack trace when getting information about the repository (https://github.com/ansible/ansible/issues/36498)
- version test - improve error message when an empty version is provided

ansible.netcommon
~~~~~~~~~~~~~~~~~

- libssh - Fix fromatting of authenticity error message when not prompting for input (https://github.com/ansible-collections/ansible.netcommon/issues/283)
- netconf - Fix connection with ncclient versions < 0.6.10
- network_cli - Fix for execution failing when ansible_ssh_password is used to specify password (https://github.com/ansible-collections/ansible.netcommon/issues/288)

ansible.utils
~~~~~~~~~~~~~

- Also include empty lists and mappings into the output dictionary (https://github.com/ansible-collections/ansible.utils/pull/58).

ansible.windows
~~~~~~~~~~~~~~~

- win_reboot - Handle connection failures when getting the first boot time command
- win_updates - Always return the ``failed_updates_count`` on a standard failure - https://github.com/ansible-collections/ansible.windows/issues/13
- win_updates - Always use a scheduled task which should be less prone to random token errors when trying to connect to Windows Update - https://github.com/ansible-collections/ansible.windows/issues/193
- win_updates - Attempt a reboot once when ``reboot=True`` is set and a failure occurred - https://github.com/ansible-collections/ansible.windows/issues/22
- win_updates - Improve the reboot detection behaviour when ``reboot=True`` is set - https://github.com/ansible-collections/ansible.windows/issues/25
- win_updates - Improve the reboot mechanism - https://github.com/ansible-collections/ansible.windows/issues/143
- win_updates - Reboot the host when ``reboot=True`` if the first search result indicates a reboot is required - https://github.com/ansible-collections/ansible.windows/issues/49

arista.eos
~~~~~~~~~~

- Add alias to neighbor and network in bgp_global so that lists of objects are plural.
- Fix typo in eos_bgp_address_family redirection.

cisco.ios
~~~~~~~~~

- Add support for autoconfig and dhcp keywords for IPv6 addresses in l3_interfaces (https://github.com/ansible-collections/cisco.ios/pull/269).
- Reordering names of interface for proper value assignment
- fixes Serial interface configuration for l3_interfaces module and Unit Test cases added.
- fixes banner module with new attribute introduced
- fixes soft_reconfiguration and prefix_list command formation.

cisco.iosxr
~~~~~~~~~~~

- To add updated route policy params to Bgp nbr AF RM
- fix backword compatibility issue for iosxr 6.x.
- fix intermittent issue on CI for iosxr_banner module.
- fix iosxr_config issue for prefix-set,route-policy config
- fix static routes interface parsing issue.

cisco.meraki
~~~~~~~~~~~~

- Fix some flake8 sanity errors as reported by Ansible Galaxy. Should be no functional change.

cisco.nxos
~~~~~~~~~~

- Render neighbor peer_type command correctly (https://github.com/ansible-collections/cisco.nxos/issues/308).

community.crypto
~~~~~~~~~~~~~~~~

- openssl_pkcs12 - fix crash when loading passphrase-protected PKCS#12 files with ``cryptography`` backend (https://github.com/ansible-collections/community.crypto/issues/247, https://github.com/ansible-collections/community.crypto/pull/248).

community.digitalocean
~~~~~~~~~~~~~~~~~~~~~~

- digital_ocean_certificate - fixing integration test (https://github.com/ansible-collections/community.digitalocean/issues/114).
- digital_ocean_certificate_info - ensure return type is a list (https://github.com/ansible-collections/community.digitalocean/issues/55).
- digital_ocean_domain_info - ensure return type is a list (https://github.com/ansible-collections/community.digitalocean/issues/55).
- digital_ocean_droplet - state `present` with `wait` was not waiting (https://github.com/ansible-collections/community.digitalocean/issues/116).
- digital_ocean_firewall - fixing integration test (https://github.com/ansible-collections/community.digitalocean/issues/114).
- digital_ocean_firewall_info - ensure return type is a list (https://github.com/ansible-collections/community.digitalocean/issues/55).
- digital_ocean_load_balancer_info - ensure return type is a list (https://github.com/ansible-collections/community.digitalocean/issues/55).
- digital_ocean_tag - fixing integration test (https://github.com/ansible-collections/community.digitalocean/issues/114).
- digital_ocean_tag_info - ensure return type is a list (https://github.com/ansible-collections/community.digitalocean/issues/55).
- digitalocean - update README.md with project_info and project module (https://github.com/ansible-collections/community.digitalocean/pull/112).
- digitalocean inventory plugin - attributes available to filters are limited to explicitly required attributes and are prefixed with ``var_prefix`` (https://github.com/ansible-collections/community.digitalocean/pull/102).

community.docker
~~~~~~~~~~~~~~~~

- docker_compose - fix idempotence bug when using ``stopped: true`` (https://github.com/ansible-collections/community.docker/issues/142, https://github.com/ansible-collections/community.docker/pull/159).

community.general
~~~~~~~~~~~~~~~~~

- _mount module utils - fixed the sanity checks (https://github.com/ansible-collections/community.general/pull/2883).
- archive - fixed ``exclude_path`` values causing incorrect archive root (https://github.com/ansible-collections/community.general/pull/2816).
- archive - fixed improper file names for single file zip archives (https://github.com/ansible-collections/community.general/issues/2818).
- archive - fixed incorrect ``state`` result value documentation (https://github.com/ansible-collections/community.general/pull/2816).
- gitlab_project - user projects are created using namespace ID now, instead of user ID (https://github.com/ansible-collections/community.general/pull/2881).
- ini_file - fix Unicode processing for Python 2 (https://github.com/ansible-collections/community.general/pull/2875).
- ipa_sudorule - call ``sudorule_add_allow_command`` method instead of  ``sudorule_add_allow_command_group`` (https://github.com/ansible-collections/community.general/issues/2442).
- java_keystore - add parameter ``keystore_type`` to control output file format and override ``keytool``'s default, which depends on Java version (https://github.com/ansible-collections/community.general/issues/2515).
- jenkins_build - examine presence of ``build_number`` before deleting a jenkins build (https://github.com/ansible-collections/community.general/pull/2850).
- modprobe - added additional checks to ensure module load/unload is effective (https://github.com/ansible-collections/community.general/issues/1608).
- nmcli - fixes team-slave configuration by adding connection.slave-type (https://github.com/ansible-collections/community.general/issues/766).
- npm - when the ``version`` option is used the comparison of installed vs missing will use name@version instead of just name, allowing version specific updates (https://github.com/ansible-collections/community.general/issues/2021).
- proxmox_kvm - fix parsing of Proxmox VM information with device info not containing a comma, like disks backed by ZFS zvols (https://github.com/ansible-collections/community.general/issues/2840).
- scaleway plugin inventory - fix ``JSON object must be str, not 'bytes'`` with Python 3.5 (https://github.com/ansible-collections/community.general/issues/2769).
- yum_versionlock - fix idempotency when using wildcard (asterisk) in ``name`` option (https://github.com/ansible-collections/community.general/issues/2761).

community.routeros
~~~~~~~~~~~~~~~~~~

- api - when using TLS/SSL, remove explicit cipher configuration to insecure values, which also makes it impossible to connect to newer RouterOS versions (https://github.com/ansible-collections/community.routeros/pull/34).

community.vmware
~~~~~~~~~~~~~~~~

- vmware - fix that the return value should be returned None if moId doesn't exist of a virtual machine (https://github.com/ansible-collections/community.vmware/pull/867).
- vmware_vmotion - implement new parameter named destination_datacenter to fix failure to move storage when datastores are shared across datacenters (https://github.com/ansible-collections/community.vmware/issues/858)

community.windows
~~~~~~~~~~~~~~~~~

- win_dns_zone - Fix idempotency when using a DNS zone with forwarders - https://github.com/ansible-collections/community.windows/issues/259
- win_domain_group_member - Fix faulty logic when comparing existing group members - https://github.com/ansible-collections/community.windows/issues/256
- win_lineinfile - Avoid stripping the newline at the end of a file - https://github.com/ansible-collections/community.windows/pull/219
- win_product_facts - fixed an issue that the module doesn't correctly convert a product id (https://github.com/ansible-collections/community.windows/pull/251).

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- Handled invalid share and unused imports cleanup for iDRAC modules (https://github.com/dell/dellemc-openmanage-ansible-modules/issues/268)

f5networks.f5_modules
~~~~~~~~~~~~~~~~~~~~~

- Add negate as3,do,ts,cfe filter for bigip_device_info
- Fix asm policy stats to return complete info in bigip_device_info module
- Fix bigip_device_info with correct attribute "insert_xforwarded_for"
- Fix ignoring of partition parameter when creating external datagroups
- Fix incorrect duplication of entries when creating new ACLs
- Fix index out of range error when comparing user and device's ACLs
- Fix ltm policy conditions to return complete data in bigip_device_info module
- Fix query filters in bigip_asm_* modules to allow policy names subsets
- Fix teem call when bigip_command and bigip_wait modules are using CLI as transport

fortinet.fortios
~~~~~~~~~~~~~~~~

- Disable check_mode feature from all global objects of configuration modules due to 'state' issue.
- Fix a bug in IP_PREFIX.match().
- Fix the KeyError caused by non-required multi-value attributes in an object.
- Fix the issue that the ``server_type`` is not updated in ``fortios_system_central_management``.
- Fix the unexpected warning caused by optinal params in ``fortios_monitor_fact`` and ``fortios_monitor``.

netapp_eseries.santricity
~~~~~~~~~~~~~~~~~~~~~~~~~

- Fix availability of client certificate change.

ovirt.ovirt
~~~~~~~~~~~

- hosted_engine_setup - Filter VLAN devices with bad names (https://github.com/oVirt/ovirt-ansible-collection/pull/238)
- hosted_engine_setup - Remove cloud-init configuration (https://github.com/oVirt/ovirt-ansible-collection/pull/295).
- ovirt inventory plugin - allow several valid values for the `plugin` key (https://github.com/oVirt/ovirt-ansible-collection/pull/293).

theforeman.foreman
~~~~~~~~~~~~~~~~~~

- external_usergroup - always lookup the ID of the usergroup, instead of passing the name to the API (https://bugzilla.redhat.com/show_bug.cgi?id=1967649)
- host, hostgroup - don't override already set parameters when passing an activation key only (and vice versa) (https://bugzilla.redhat.com/show_bug.cgi?id=1967904)

vyos.vyos
~~~~~~~~~

- Fix KeyError 'source' - vyos_firewall_rules
- Updated docs resolving spelling typos
- change interface to next-hop-interface while generating static_routes nexthop command.

Known Issues
------------

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- idrac_user - Issue(192043) Module may error out with the message ``unable to perform the import or export operation because there are pending attribute changes or a configuration job is in progress``. Wait for the job to complete and run the task again.
- ome_smart_fabric_uplink - Issue(186024) ome_smart_fabric_uplink module does not allow the creation of multiple uplinks of the same name even though this is supported by OpenManage Enterprise Modular. If an uplink is created using the same name as an existing uplink, the existing uplink is modified.

New Plugins
-----------

Filter
~~~~~~

- community.sops.decrypt - Decrypt sops-encrypted data

Inventory
~~~~~~~~~

- community.vmware.vmware_host_inventory - VMware ESXi hostsystem inventory source

New Modules
-----------

arista.eos
~~~~~~~~~~

- arista.eos.eos_prefix_lists - Manages Prefix lists resource module

cisco.iosxr
~~~~~~~~~~~

- cisco.iosxr.iosxr_prefix_lists - Prefix-Lists resource module.

cisco.nxos
~~~~~~~~~~

- cisco.nxos.nxos_prefix_lists - Prefix-Lists resource module.

community.digitalocean
~~~~~~~~~~~~~~~~~~~~~~

- community.digitalocean.digital_ocean_project - Manage a DigitalOcean project
- community.digitalocean.digital_ocean_project_info - Gather information about DigitalOcean Projects
- community.digitalocean.digital_ocean_snapshot - Create and delete DigitalOcean snapshots
- community.digitalocean.digital_ocean_vpc - Create and delete DigitalOcean VPCs
- community.digitalocean.digital_ocean_vpc_info - Gather information about DigitalOcean VPCs

community.general
~~~~~~~~~~~~~~~~~

Identity
^^^^^^^^

Keycloak
........

- community.general.keycloak_authentication - Configure authentication in Keycloak

community.vmware
~~~~~~~~~~~~~~~~

- community.vmware.vmware_host_custom_attributes - Manage custom attributes from VMware for the given ESXi host
- community.vmware.vmware_host_passthrough - Manage PCI device passthrough settings on host
- community.vmware.vmware_object_custom_attributes_info - Gather custom attributes of an object
- community.vmware.vmware_object_role_permission_info - Gather information about object's permissions
- community.vmware.vmware_recommended_datastore - Returns the recommended datastore from a SDRS-enabled datastore cluster

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- dellemc.openmanage.ome_groups - Manages static device groups on OpenManage Enterprise

Unchanged Collections
---------------------

- amazon.aws (still version 1.5.0)
- ansible.posix (still version 1.2.0)
- azure.azcollection (still version 1.7.0)
- check_point.mgmt (still version 2.0.0)
- chocolatey.chocolatey (still version 1.1.0)
- cisco.aci (still version 2.0.0)
- cisco.asa (still version 2.0.2)
- cisco.intersight (still version 1.0.15)
- cisco.mso (still version 1.2.0)
- cisco.nso (still version 1.0.3)
- cisco.ucs (still version 1.6.0)
- cloudscale_ch.cloud (still version 2.2.0)
- community.aws (still version 1.5.0)
- community.azure (still version 1.0.0)
- community.fortios (still version 1.0.0)
- community.google (still version 1.0.0)
- community.grafana (still version 1.2.1)
- community.hrobot (still version 1.1.1)
- community.kubernetes (still version 1.2.1)
- community.kubevirt (still version 1.0.0)
- community.libvirt (still version 1.0.1)
- community.mongodb (still version 1.2.1)
- community.mysql (still version 2.1.0)
- community.network (still version 3.0.0)
- community.okd (still version 1.1.2)
- community.postgresql (still version 1.3.0)
- community.proxysql (still version 1.0.0)
- community.rabbitmq (still version 1.0.3)
- community.skydive (still version 1.0.0)
- community.zabbix (still version 1.3.0)
- containers.podman (still version 1.6.1)
- cyberark.conjur (still version 1.1.0)
- cyberark.pas (still version 1.0.7)
- dellemc.enterprise_sonic (still version 1.1.0)
- dellemc.os10 (still version 1.1.1)
- dellemc.os6 (still version 1.0.7)
- dellemc.os9 (still version 1.0.4)
- frr.frr (still version 1.0.3)
- gluster.gluster (still version 1.0.1)
- google.cloud (still version 1.0.2)
- hetzner.hcloud (still version 1.4.3)
- hpe.nimble (still version 1.1.3)
- ibm.qradar (still version 1.0.3)
- infinidat.infinibox (still version 1.2.4)
- inspur.sm (still version 1.2.0)
- kubernetes.core (still version 1.2.1)
- mellanox.onyx (still version 1.0.0)
- netapp.aws (still version 21.2.0)
- netapp.azure (still version 21.7.0)
- netapp.cloudmanager (still version 21.7.0)
- netapp.elementsw (still version 21.6.1)
- netapp.ontap (still version 21.7.0)
- netapp.um_info (still version 21.6.0)
- netbox.netbox (still version 3.1.1)
- ngine_io.cloudstack (still version 2.1.0)
- ngine_io.exoscale (still version 1.0.0)
- ngine_io.vultr (still version 1.1.0)
- openvswitch.openvswitch (still version 2.0.0)
- purestorage.flasharray (still version 1.8.0)
- purestorage.flashblade (still version 1.6.0)
- sensu.sensu_go (still version 1.11.1)
- servicenow.servicenow (still version 1.0.6)
- splunk.es (still version 1.0.2)
- wti.remote (still version 1.0.1)

v4.1.0
======

.. contents::
  :local:
  :depth: 2

Release Summary
---------------

Release Date: 2021-06-10

`Porting Guide <https://docs.ansible.com/ansible/devel/porting_guides.html>`_

Ansible-core
------------

Ansible 4.1.0 contains Ansible-core version 2.11.1.
This is a newer version than version 2.11.0 contained in the previous Ansible release.

The changes are reported in the combined changelog below.

Changed Collections
-------------------

If not mentioned explicitly, the changes are reported in the combined changelog below.

+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| Collection                    | Ansible 4.0.0 | Ansible 4.1.0 | Notes                                                                                                                        |
+===============================+===============+===============+==============================================================================================================================+
| ansible.netcommon             | 2.0.2         | 2.1.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| ansible.utils                 | 2.1.0         | 2.2.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| ansible.windows               | 1.5.0         | 1.6.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| arista.eos                    | 2.1.1         | 2.1.2         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| awx.awx                       | 19.0.0        | 19.2.0        | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| azure.azcollection            | 1.5.0         | 1.7.0         | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.asa                     | 2.0.1         | 2.0.2         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.ios                     | 2.0.1         | 2.2.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.iosxr                   | 2.1.0         | 2.2.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.meraki                  | 2.2.1         | 2.4.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.mso                     | 1.1.0         | 1.2.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.nxos                    | 2.2.0         | 2.3.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cloudscale_ch.cloud           | 2.1.0         | 2.2.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.crypto              | 1.6.2         | 1.7.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.digitalocean        | 1.1.1         | 1.5.1         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.docker              | 1.5.0         | 1.7.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.general             | 3.0.2         | 3.2.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.postgresql          | 1.2.0         | 1.3.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.vmware              | 1.9.0         | 1.10.0        |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.windows             | 1.3.0         | 1.4.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| containers.podman             | 1.5.0         | 1.6.1         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cyberark.pas                  | 1.0.6         | 1.0.7         | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| dellemc.enterprise_sonic      | 1.0.3         | 1.1.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| dellemc.openmanage            | 3.3.0         | 3.4.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| f5networks.f5_modules         | 1.9.0         | 1.9.1         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| fortinet.fortimanager         | 2.0.2         | 2.0.3         | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| fortinet.fortios              | 2.0.1         | 2.0.2         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| inspur.sm                     | 1.1.4         | 1.2.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| junipernetworks.junos         | 2.1.0         | 2.2.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| netapp.azure                  | 21.5.0        | 21.7.0        |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| netapp.cloudmanager           | 21.5.1        | 21.7.0        |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| netapp.elementsw              | 21.3.0        | 21.6.1        |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| netapp.ontap                  | 21.5.0        | 21.7.0        |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| netapp.um_info                | 21.5.0        | 21.6.0        |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| netapp_eseries.santricity     | 1.2.7         | 1.2.12        |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| netbox.netbox                 | 3.0.0         | 3.1.1         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| ovirt.ovirt                   | 1.4.2         | 1.5.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| sensu.sensu_go                | 1.9.4         | 1.11.1        |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| servicenow.servicenow         | 1.0.5         | 1.0.6         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| t_systems_mms.icinga_director | 1.16.0        | 1.17.0        | The collection did not have a changelog in this version.                                                                     |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| theforeman.foreman            | 2.0.1         | 2.1.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| vyos.vyos                     | 2.2.0         | 2.3.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+

Major Changes
-------------

cloudscale_ch.cloud
~~~~~~~~~~~~~~~~~~~

- Add custom_image module

community.postgresql
~~~~~~~~~~~~~~~~~~~~

- postgresql_query - the default value of the ``as_single_query`` option will be changed to ``yes`` in community.postgresql 2.0.0 (https://github.com/ansible-collections/community.postgresql/issues/85).

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- ome_firmware_baseline - Module supports check mode, and allows the modification and deletion of firmware baselines.
- ome_firmware_catalog - Module supports check mode, and allows the modification and deletion of firmware catalogs.

fortinet.fortios
~~~~~~~~~~~~~~~~

- Improve ``fortios_configuration_fact`` to use multiple selectors concurrently.
- Support ``check_mode`` in all cofigurationAPI-based modules.
- Support filtering for fact gathering modules ``fortios_configuration_fact`` and ``fortios_monitor_fact``.
- Support moving policy in ``firewall_central_snat_map``.
- Unify schemas for monitor API.

netbox.netbox
~~~~~~~~~~~~~

- packages is now a required Python package and gets installed via Ansible 2.10+.

Minor Changes
-------------

Ansible-core
~~~~~~~~~~~~

- ansible adhoc, clarified the help to some options, also added some comments to code.
- command - update the user warning message to point out command name (https://github.com/ansible/ansible/pull/74475).

ansible.netcommon
~~~~~~~~~~~~~~~~~

- Add support for ProxyCommand with netconf connection.

ansible.utils
~~~~~~~~~~~~~

- Add in_any_network, in_network, in_one_network test plugins
- Add ip, ip_address test plugins
- Add ipv4, ipv4_address, ipv4_hostmask, ipv4_netmask test plugins
- Add ipv6, ipv6_address, ipv6_ipv4_mapped, ipv6_sixtofour, ipv6_teredo test plugins
- Add loopback, mac, multicast test plugins
- Add private, public, reserved test plugins
- Add resolvable test plugins
- Add subnet_of, supernet_of, unspecified test plugins

ansible.windows
~~~~~~~~~~~~~~~

- win_reboot - Change the default ``test_command`` run after a reboot to wait for more services to start up before the plugin finished. This should better handle waiting until the logon screen appears rather than just when WinRM is first online.

cisco.ios
~~~~~~~~~

- Add ios_logging_global module.
- Add ios_route_maps Resource Module (https://github.com/ansible-collections/cisco.ios/pull/297).
- Add support for ansible_network_resources key allows to fetch the available resources for a platform (https://github.com/ansible-collections/cisco.ios/pull/292).
- IOS Prefix list resource module.

cisco.iosxr
~~~~~~~~~~~

- Add new keys for iosxr_l2_interface, iosxr_logging.
- Fix integration tests for iosxr_config, iosxr_smoke,iosxr_facts,iosxr_l2_interfaces,iosxr_lag_interfaces, iosxr_logging,iosxr_user.

cisco.meraki
~~~~~~~~~~~~

- meraki_ms_switchport - Adding additional functionality to support the access_policy_types "MAC allow list" and "Sticky MAC allow list" port security configuration options. (https://github.com/CiscoDevNet/ansible-meraki/issues/227).
- meraki_mx_intrusion_prevention - Rename message to rule_message to avoid conflicts with internal Ansible variables.
- meraki_mx_switchport - Improve documentation for response

cisco.mso
~~~~~~~~~

- Add Ansible common HTTPAPI dependancy in galaxy.yml
- Add HTTPAPI connection plugin support and HTTPAPI MSO connection plugin
- Add primary and unicast_routing attributes to mso_schema_template_bd
- Add requirements.txt for Ansible Environment support
- Add schema and template cloning modules mso_schema_clone and mso_schema_template_clone
- Add support cisco.nd.nd connection plugin
- Add support for multiple DCHP policies in a BD and new module mso_schema_template_bd_dhcp_policy
- Upgrade CI to latest Ansible version and Python 3.8

cisco.nxos
~~~~~~~~~~

- Add `default_passive_interface` option in `nxos_ospf_interfaces`.
- Add a netconf subplugin to make netconf_* modules work with older NX-OS versions (https://github.com/ansible-collections/ansible.netcommon/issues/252).

cloudscale_ch.cloud
~~~~~~~~~~~~~~~~~~~

- Increase api_timeout to 45
- Read CLOUDSCALE_API_TIMEOUT environment variable

community.crypto
~~~~~~~~~~~~~~~~

- cryptography_openssh module utils - new module_utils for managing asymmetric keypairs and OpenSSH formatted/encoded asymmetric keypairs (https://github.com/ansible-collections/community.crypto/pull/213).
- openssh_keypair - added ``backend`` parameter for selecting between the cryptography library or the OpenSSH binary for the execution of actions performed by ``openssh_keypair`` (https://github.com/ansible-collections/community.crypto/pull/236).
- openssh_keypair - added ``passphrase`` parameter for encrypting/decrypting OpenSSH private keys (https://github.com/ansible-collections/community.crypto/pull/225).
- openssl_csr - add diff mode (https://github.com/ansible-collections/community.crypto/issues/38, https://github.com/ansible-collections/community.crypto/pull/150).
- openssl_csr_info - now returns ``public_key_type`` and ``public_key_data`` (https://github.com/ansible-collections/community.crypto/pull/233).
- openssl_csr_info - refactor module to allow code re-use for diff mode (https://github.com/ansible-collections/community.crypto/pull/204).
- openssl_csr_pipe - add diff mode (https://github.com/ansible-collections/community.crypto/issues/38, https://github.com/ansible-collections/community.crypto/pull/150).
- openssl_pkcs12 - added option ``select_crypto_backend`` and a ``cryptography`` backend. This requires cryptography 3.0 or newer, and does not support the ``iter_size`` and ``maciter_size`` options (https://github.com/ansible-collections/community.crypto/pull/234).
- openssl_privatekey - add diff mode (https://github.com/ansible-collections/community.crypto/issues/38, https://github.com/ansible-collections/community.crypto/pull/150).
- openssl_privatekey_info - refactor module to allow code re-use for diff mode (https://github.com/ansible-collections/community.crypto/pull/205).
- openssl_privatekey_pipe - add diff mode (https://github.com/ansible-collections/community.crypto/issues/38, https://github.com/ansible-collections/community.crypto/pull/150).
- openssl_publickey - add diff mode (https://github.com/ansible-collections/community.crypto/issues/38, https://github.com/ansible-collections/community.crypto/pull/150).
- x509_certificate - add diff mode (https://github.com/ansible-collections/community.crypto/issues/38, https://github.com/ansible-collections/community.crypto/pull/150).
- x509_certificate_info - now returns ``public_key_type`` and ``public_key_data`` (https://github.com/ansible-collections/community.crypto/pull/233).
- x509_certificate_info - refactor module to allow code re-use for diff mode (https://github.com/ansible-collections/community.crypto/pull/206).
- x509_certificate_pipe - add diff mode (https://github.com/ansible-collections/community.crypto/issues/38, https://github.com/ansible-collections/community.crypto/pull/150).
- x509_crl - add diff mode (https://github.com/ansible-collections/community.crypto/issues/38, https://github.com/ansible-collections/community.crypto/pull/150).
- x509_crl_info - add ``list_revoked_certificates`` option to avoid enumerating all revoked certificates (https://github.com/ansible-collections/community.crypto/pull/232).
- x509_crl_info - refactor module to allow code re-use for diff mode (https://github.com/ansible-collections/community.crypto/pull/203).

community.digitalocean
~~~~~~~~~~~~~~~~~~~~~~

- digital_ocean - ``ssh_key_ids`` list entries are now validated to be strings (https://github.com/ansible-collections/community.digitalocean/issues/13).
- digital_ocean_droplet - ``ssh_keys``, ``tags``, and ``volumes`` list entries are now validated to be strings (https://github.com/ansible-collections/community.digitalocean/issues/13).
- digital_ocean_droplet - adding ``active`` and ``inactive`` states (https://github.com/ansible-collections/community.digitalocean/issues/23).
- digital_ocean_droplet - adds Droplet resize functionality (https://github.com/ansible-collections/community.digitalocean/issues/4).
- digitalocean - Filter droplets in dynamic inventory plugin using arbitrary. jinja2 expressions (https://github.com/ansible-collections/community.digitalocean/pull/96).
- digitalocean - Support templates in API tokens when using the dynamic inventory plugin (https://github.com/ansible-collections/community.digitalocean/pull/98).

community.docker
~~~~~~~~~~~~~~~~

- common module utils - correct error messages for guiding to install proper Docker SDK for Python module (https://github.com/ansible-collections/community.docker/pull/125).
- docker_container - allow ``memory_swap: -1`` to set memory swap limit to unlimited. This is useful when the user cannot set memory swap limits due to cgroup limitations or other reasons, as by default Docker will try to set swap usage to two times the value of ``memory`` (https://github.com/ansible-collections/community.docker/pull/138).
- docker_image - allow to tag images by ID (https://github.com/ansible-collections/community.docker/pull/149).

community.general
~~~~~~~~~~~~~~~~~

- ModuleHelper module utils - improved mechanism for customizing the calculation of ``changed`` (https://github.com/ansible-collections/community.general/pull/2514).
- Remove unnecessary ``__init__.py`` files from ``plugins/`` (https://github.com/ansible-collections/community.general/pull/2632).
- archive - added ``exclusion_patterns`` option to exclude files or subdirectories from archives (https://github.com/ansible-collections/community.general/pull/2616).
- chroot connection - minor refactor to make lints and IDEs happy (https://github.com/ansible-collections/community.general/pull/2520).
- cloud_init_data_facts - minor refactor (https://github.com/ansible-collections/community.general/pull/2557).
- cmd (Module Helper) module utils - ``CmdMixin`` now pulls the value for ``run_command()`` params from ``self.vars``, as opposed to previously retrieving those from ``self.module.params`` (https://github.com/ansible-collections/community.general/pull/2517).
- composer - add ``composer_executable`` option (https://github.com/ansible-collections/community.general/issues/2649).
- filesystem - cleanup and revamp module, tests and doc. Pass all commands to ``module.run_command()`` as lists. Move the device-vs-mountpoint logic to ``grow()`` method. Give to all ``get_fs_size()`` the same logic and error handling. (https://github.com/ansible-collections/community.general/pull/2472).
- flatpak - add ``no_dependencies`` parameter (https://github.com/ansible/ansible/pull/55452, https://github.com/ansible-collections/community.general/pull/2751).
- funcd connection - minor refactor to make lints and IDEs happy (https://github.com/ansible-collections/community.general/pull/2520).
- gitlab_user - add ``expires_at`` option (https://github.com/ansible-collections/community.general/issues/2325).
- idrac_redfish_config - modified set_manager_attributes function to skip invalid attribute instead of returning. Added skipped attributes to output. Modified module exit to add warning variable (https://github.com/ansible-collections/community.general/issues/1995).
- influxdb_retention_policy - add ``state`` parameter with allowed values ``present`` and ``absent`` to support deletion of existing retention policies (https://github.com/ansible-collections/community.general/issues/2383).
- influxdb_retention_policy - simplify duration logic parsing (https://github.com/ansible-collections/community.general/pull/2385).
- ini_file - opening file with encoding ``utf-8-sig`` (https://github.com/ansible-collections/community.general/issues/2189).
- iocage connection - minor refactor to make lints and IDEs happy (https://github.com/ansible-collections/community.general/pull/2520).
- jail connection - minor refactor to make lints and IDEs happy (https://github.com/ansible-collections/community.general/pull/2520).
- java_keystore - added ``ssl_backend`` parameter for using the cryptography library instead of the OpenSSL binary (https://github.com/ansible-collections/community.general/pull/2485).
- java_keystore - replace envvar by stdin to pass secret to ``keytool`` (https://github.com/ansible-collections/community.general/pull/2526).
- jira - add comment visibility parameter for comment operation (https://github.com/ansible-collections/community.general/pull/2556).
- linode - added proper traceback when failing due to exceptions (https://github.com/ansible-collections/community.general/pull/2410).
- linode - parameter ``additional_disks`` is now validated as a list of dictionaries (https://github.com/ansible-collections/community.general/pull/2410).
- lxc connection - minor refactor to make lints and IDEs happy (https://github.com/ansible-collections/community.general/pull/2520).
- maven_artifact - added ``checksum_alg`` option to support SHA1 checksums in order to support FIPS systems (https://github.com/ansible-collections/community.general/pull/2662).
- module_helper module utils - break down of the long file into smaller pieces (https://github.com/ansible-collections/community.general/pull/2393).
- module_helper module utils - method ``CmdMixin.run_command()`` now accepts ``process_output`` specifying a function to process the outcome of the underlying ``module.run_command()`` (https://github.com/ansible-collections/community.general/pull/2564).
- nmcli - add new options to ignore automatic DNS servers and gateways (https://github.com/ansible-collections/community.general/issues/1087).
- nmcli - remove dead code, ``options`` never contains keys from ``param_alias`` (https://github.com/ansible-collections/community.general/pull/2417).
- onepassword lookup plugin - add ``domain`` option (https://github.com/ansible-collections/community.general/issues/2734).
- open_iscsi - add ``auto_portal_startup`` parameter to allow ``node.startup`` setting per portal (https://github.com/ansible-collections/community.general/issues/2685).
- open_iscsi - also consider ``portal`` and ``port`` to check if already logged in or not (https://github.com/ansible-collections/community.general/issues/2683).
- pacman - add ``executable`` option to use an alternative pacman binary (https://github.com/ansible-collections/community.general/issues/2524).
- passwordstore lookup - add option ``missing`` to choose what to do if the password file is missing (https://github.com/ansible-collections/community.general/pull/2500).
- proxmox_group_info - minor refactor (https://github.com/ansible-collections/community.general/pull/2557).
- proxmox_kvm - minor refactor (https://github.com/ansible-collections/community.general/pull/2557).
- qubes connection - minor refactor to make lints and IDEs happy (https://github.com/ansible-collections/community.general/pull/2520).
- redfish_config - modified module exit to add warning variable (https://github.com/ansible-collections/community.general/issues/1995).
- redfish_utils module utils - modified set_bios_attributes function to skip invalid attribute instead of returning. Added skipped attributes to output (https://github.com/ansible-collections/community.general/issues/1995).
- rhevm - minor refactor (https://github.com/ansible-collections/community.general/pull/2557).
- saltstack connection - minor refactor to make lints and IDEs happy (https://github.com/ansible-collections/community.general/pull/2520).
- serverless - minor refactor (https://github.com/ansible-collections/community.general/pull/2557).
- spotinst_aws_elastigroup - elements of list parameters are now validated (https://github.com/ansible-collections/community.general/pull/2355).
- stacki_host - minor refactoring (https://github.com/ansible-collections/community.general/pull/2681).
- terraform - add option ``overwrite_init`` to skip init if exists (https://github.com/ansible-collections/community.general/pull/2573).
- terraform - minor refactor (https://github.com/ansible-collections/community.general/pull/2557).
- zfs_delegate_admin - drop choices from permissions, allowing any permission supported by the underlying zfs commands (https://github.com/ansible-collections/community.general/pull/2540).
- zone connection - minor refactor to make lints and IDEs happy (https://github.com/ansible-collections/community.general/pull/2520).

community.vmware
~~~~~~~~~~~~~~~~

- vmware_cluster_drs - Make enable_drs an alias of enable and add a warning that the default will change from false to true in a future version (https://github.com/ansible-collections/community.vmware/pull/766)
- vmware_cluster_ha - Make enable_ha an alias of enable and add a warning that the default will change from false to true in a future version (https://github.com/ansible-collections/community.vmware/pull/766)
- vmware_cluster_vsan - Make enable_vsan an alias of enable and add a warning that the default will change from false to true in a future version (https://github.com/ansible-collections/community.vmware/pull/766)
- vmware_dvs_portgroup - Implement 'elastic' port group configuration (https://github.com/ansible-collections/community.vmware/issues/410).
- vmware_dvs_portgroup - Implement MAC learning configuration (https://github.com/ansible-collections/community.vmware/issues/644).
- vmware_dvs_portgroup - Implement configuration of active and standby uplinks (https://github.com/ansible-collections/community.vmware/issues/709).
- vmware_dvs_portgroup - Remove default for teaming_policy.inbound_policy (https://github.com/ansible-collections/community.vmware/pull/743).
- vmware_dvs_portgroup_info - Return information about MAC learning configuration (https://github.com/ansible-collections/community.vmware/issues/644).
- vmware_dvs_portgroup_info - Return information about uplinks (https://github.com/ansible-collections/community.vmware/issues/709).
- vmware_guest - add more documentation about ``is_template`` (https://github.com/ansible-collections/community.vmware/pull/794).
- vmware_host_iscsi_info - added a list(detected_iscsi_drives) of detected iscsi drives to the return value after set an iscsi config (https://github.com/ansible-collections/community.vmware/pull/729).
- vmware_tag - modified the category_id parameter to required (https://github.com/ansible-collections/community.vmware/pull/790).
- vmware_vm_inventory - set default to ``True`` for ``with_nested_properties`` (https://github.com/ansible-collections/community.vmware/issues/712).

containers.podman
~~~~~~~~~~~~~~~~~

- Add Ansible 2.11 to all tests and use Ubuntu 20.04
- Add Ansible 2.11 to testing
- Add RPM building scripts
- Add support for timezones in containers

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- ome_firmware_catalog - Added support for repositories available on the Dell support site.
- ome_template_network_vlan - Added the input option which allows to apply the modified VLAN settings immediately on the associated modular-system servers.

f5networks.f5_modules
~~~~~~~~~~~~~~~~~~~~~

- Add ENV variable with better name, it should make it easier to understand when disabling F5 TEEM telemetry
- Add new choices to request/response chunking parameter to accomodate TMOS v15 and above

inspur.sm
~~~~~~~~~

- Compatible with M6 models, add M6 specific fields.

junipernetworks.junos
~~~~~~~~~~~~~~~~~~~~~

- Change src element from str to path for junos_scp.
- Improve junos_bgp_address_family unit test coverage.

netapp.azure
~~~~~~~~~~~~

- azure_rm_netapp_account - support additional authentication schemes provided by AzureRMModuleBase.
- azure_rm_netapp_capacity_pool - support additional authentication schemes provided by AzureRMModuleBase, and tags.
- azure_rm_netapp_capacity_pool - wait for completion when creating, modifying, or deleting a pool.
- azure_rm_netapp_snapshot - support additional authentication schemes provided by AzureRMModuleBase.
- azure_rm_netapp_snapshot - wait for completion when creating, modifying, or deleting a pool.
- azure_rm_netapp_volume - support additional authentication schemes provided by AzureRMModuleBase, and tags.

netapp.cloudmanager
~~~~~~~~~~~~~~~~~~~

- na_cloudmanager_aggregate - Add provider_volume_type gp3 support.
- na_cloudmanager_connector_gcp - rename option ``service_account_email`` and ``service_account_path`` to ``gcp_service_account_email`` and ``gcp_service_account_path`` respectively.
- na_cloudmanager_cvo_aws - Add ebs_volume_type gp3 support.
- na_cloudmanager_snapmirror - Add provider_volume_type gp3 support.
- na_cloudmanager_volume - Add aggregate_name support on volume creation.
- na_cloudmanager_volume - Add provider_volume_type gp3 support.

netapp.ontap
~~~~~~~~~~~~

- License displayed correctly in Github
- na_ontap_cifs - new option ``comment`` to associate a description to a CIFS share.
- na_ontap_disks - added REST support for the module.
- na_ontap_disks - added functionality to reassign spare disks from a partner node to the desired node.
- na_ontap_disks - new option min_spares.
- na_ontap_lun - new suboption ``exclude_aggregates`` for SAN application.
- na_ontap_rest_info - Added "autosupport_check_info"/"support/autosupport/check" to the attributes that will be collected when gathering info using the module.
- na_ontap_users - new option ``application_dicts`` to associate multiple authentication methods to an application.
- na_ontap_users - new option ``application_strs`` to disambiguate ``applications``.
- na_ontap_users - new option ``replace_existing_apps_and_methods``.
- na_ontap_users - new suboption ``second_authentication_method`` with ``application_dicts`` option.
- na_ontap_volume - new suboption ``exclude_aggregates`` for NAS application.
- na_ontap_vserver_peer - new options ``local_name_for_source`` and ``local_name_for_peer`` added.

netapp.um_info
~~~~~~~~~~~~~~

- na_um_list_aggregates has been renamed na_um_aggregates_info.
- na_um_list_clusters has been renamed na_um_clusters_info.
- na_um_list_nodes has been renamed na_um_nodes_info.
- na_um_list_svms has been renamed na_um_svms_info.
- na_um_list_volumes has been renamed na_um_volumes_info.

netapp_eseries.santricity
~~~~~~~~~~~~~~~~~~~~~~~~~

- Add eseries_system_old_password variable to faciliate changing the storage system's admin password.
- Add login banner message to na_santricity_global module and nar_santricity_management role.
- Add remove_unspecified_user_certificates variable to the client certificates module.
- Add usable drive option for na_santricity_storagepool module and nar_santricity_host role which can be used to choose selected drives for storage pool/volumes or define a pattern drive selection.

netbox.netbox
~~~~~~~~~~~~~

- netbox_device_interface - Add custom_fields [#514](https://github.com/netbox-community/ansible_modules/pull/514)
- netbox_device_interface - Add label option.
- netbox_device_interface - Add mark_connected option.
- netbox_power_panel - Add location option.
- netbox_rack - Add location option.
- netbox_vlan_group - Add custom_fields option.
- netbox_vlan_group - Add description option.
- netbox_vlan_group - Add scope option.
- netbox_vlan_group - Add scope_type option.

ovirt.ovirt
~~~~~~~~~~~

- disaster_recovery - Change conf paths (https://github.com/oVirt/ovirt-ansible-collection/pull/286).
- hosted_engine_setup - Add-pause-option-before-engine-setup (https://github.com/oVirt/ovirt-ansible-collection/pull/273).
- hosted_engine_setup - Remove leftover code and omit parameters (https://github.com/oVirt/ovirt-ansible-collection/pull/281).
- infra - Storage fix parameters typo (https://github.com/oVirt/ovirt-ansible-collection/pull/282).
- ovirt_host - Update iscsi target struct (https://github.com/oVirt/ovirt-ansible-collection/pull/274).

sensu.sensu_go
~~~~~~~~~~~~~~

- Add argument specification to the agent role.
- Add argument specification to the backend role.
- Add argument specification to the install role.
- Add modules for managing Sensu Go authentication providers.

theforeman.foreman
~~~~~~~~~~~~~~~~~~

- Add a domain_info module
- Add a hostgroups role (https://github.com/theforeman/foreman-ansible-modules/issues/1116)
- Add a role `content_rhel` to perform basic setup for registering and syncing RHEL content hosts
- Add content credentials role
- callback plugin - collect facts during the run, merge them correctly and upload them once at the end
- compute_resource - add ``cloud`` param for the AzureRm provider, to select which Azure cloud to use
- compute_resource - add ``sub_id`` parameter for handling the Azure Subscription ID instead of the ``user`` parameter
- host - Add ``Redfish`` to list of possible BMC providers of an interface
- host, compute_profile - look up the correct id for storage pods and domains given as part of ``volumes_attributes`` (https://bugzilla.redhat.com/show_bug.cgi?id=1885234)
- hostgroup - add a ``ansible_roles`` parameter (https://github.com/theforeman/foreman-ansible-modules/issues/1123)
- new ``content_views`` role to manage content views (https://github.com/theforeman/foreman-ansible-modules/issues/1111)
- new ``organizations`` role to manage organizations (https://github.com/theforeman/foreman-ansible-modules/issues/1109)
- subnet - add ``bmc_proxy`` parameter to configure BMC proxies for subnets

vyos.vyos
~~~~~~~~~

- Add vyos_route_maps resource module (https://github.com/ansible-collections/vyos.vyos/pull/156.).

Deprecated Features
-------------------

ansible.windows
~~~~~~~~~~~~~~~

- win_reboot - Unreachable hosts can be ignored with ``ignore_errors: True``, this ability will be removed in a future version. Use ``ignore_unreachable: True`` to ignore unreachable hosts instead. - https://github.com/ansible-collections/ansible.windows/issues/62

community.docker
~~~~~~~~~~~~~~~~

- docker_* modules and plugins, except ``docker_swarm`` connection plugin and ``docker_compose`` and ``docker_stack*` modules - the current default ``localhost`` for ``tls_hostname`` is deprecated. In community.docker 2.0.0 it will be computed from ``docker_host`` instead (https://github.com/ansible-collections/community.docker/pull/134).

community.general
~~~~~~~~~~~~~~~~~

- All inventory and vault scripts will be removed from community.general in version 4.0.0. If you are referencing them, please update your references to the new `contrib-scripts GitHub repository <https://github.com/ansible-community/contrib-scripts>`_ so your workflow will not break once community.general 4.0.0 is released (https://github.com/ansible-collections/community.general/pull/2697).
- The nios, nios_next_ip, nios_next_network lookup plugins, the nios documentation fragment, and the nios_host_record, nios_ptr_record, nios_mx_record, nios_fixed_address, nios_zone, nios_member, nios_a_record, nios_aaaa_record, nios_network, nios_dns_view, nios_txt_record, nios_naptr_record, nios_srv_record, nios_cname_record, nios_nsgroup, and nios_network_view module have been deprecated and will be removed from community.general 5.0.0. Please install the `infoblox.nios_modules <https://galaxy.ansible.com/infoblox/nios_modules>`_ collection instead and use its plugins and modules (https://github.com/ansible-collections/community.general/pull/2458).
- The vendored copy of ``ipaddress`` will be removed in community.general 4.0.0. Please switch to ``ipaddress`` from the Python 3 standard library, or `from pypi <https://pypi.org/project/ipaddress/>`_, if your code relies on the vendored version of ``ipaddress`` (https://github.com/ansible-collections/community.general/pull/2459).
- linode - parameter ``backupsenabled`` is deprecated and will be removed in community.general 5.0.0 (https://github.com/ansible-collections/community.general/pull/2410).
- lxd inventory plugin - the plugin will require ``ipaddress`` installed when used with Python 2 from community.general 4.0.0 on. ``ipaddress`` is part of the Python 3 standard library, but can be installed for Python 2 from pypi (https://github.com/ansible-collections/community.general/pull/2459).
- scaleway_security_group_rule - the module will require ``ipaddress`` installed when used with Python 2 from community.general 4.0.0 on. ``ipaddress`` is part of the Python 3 standard library, but can be installed for Python 2 from pypi (https://github.com/ansible-collections/community.general/pull/2459).

inspur.sm
~~~~~~~~~

- add_ad_group - This feature will be removed in inspur.sm.add_ad_group 3.0.0. replaced with inspur.sm.ad_group.
- add_ldap_group - This feature will be removed in inspur.sm.add_ldap_group 3.0.0. replaced with inspur.sm.ldap_group.
- add_user - This feature will be removed in inspur.sm.add_user 3.0.0. replaced with inspur.sm.user.
- add_user_group - This feature will be removed in inspur.sm.add_user_group 3.0.0. replaced with inspur.sm.user_group.
- del_ad_group - This feature will be removed in inspur.sm.del_ad_group 3.0.0. replaced with inspur.sm.ad_group.
- del_ldap_group - This feature will be removed in inspur.sm.del_ldap_group 3.0.0. replaced with inspur.sm.ldap_group.
- del_user - This feature will be removed in inspur.sm.del_user 3.0.0. replaced with inspur.sm.user.
- del_user_group - This feature will be removed in inspur.sm.del_user_group 3.0.0. replaced with inspur.sm.user_group.
- edit_ad_group - This feature will be removed in inspur.sm.edit_ad_group 3.0.0. replaced with inspur.sm.ad_group.
- edit_ldap_group - This feature will be removed in inspur.sm.edit_ldap_group 3.0.0. replaced with inspur.sm.ldap_group.
- edit_user - This feature will be removed in inspur.sm.edit_user 3.0.0. replaced with inspur.sm.user.
- edit_user_group - This feature will be removed in inspur.sm.edit_user_group 3.0.0. replaced with inspur.sm.user_group.

Removed Features (previously deprecated)
----------------------------------------

ansible.windows
~~~~~~~~~~~~~~~

- win_reboot - Removed ``shutdown_timeout`` and ``shutdown_timeout_sec`` which has not done anything since Ansible 2.5.

Security Fixes
--------------

cisco.ios
~~~~~~~~~

- To fix Cisco IOS no log issue and add ignore txt for 2.12 (https://github.com/ansible-collections/cisco.ios/pull/304).

Bugfixes
--------

Ansible-core
~~~~~~~~~~~~

- Add RockyLinux to fact gathering (https://github.com/ansible/ansible/pull/74530).
- Improve resilience of ``ansible-galaxy collection`` by increasing the page size to make fewer requests overall and retrying queries with a jittered exponential backoff when rate limiting HTTP codes (520 and 429) occur. (https://github.com/ansible/ansible/issues/74191)
- Prevent ``ansible_failed_task`` from further templating (https://github.com/ansible/ansible/issues/74036)
- Remove 'default' from ssh plugin as we want to rely on default from ssh itself or ssh/config.
- The error message about the failure to import a ``gpg`` key by the ``apt_key`` module was incorrect (https://github.com/ansible/ansible/issues/74423).
- ansible-test - Avoid publishing the port used by the ``pypi-test-container`` since it is only accessed by other containers. This avoids issues when trying to run tests in parallel on a single host.
- ansible-test - Fix docker container IP address detection. The ``bridge`` network is no longer assumed to be the default.
- ansible-test - Use documented API to retrieve build information from Azure Pipelines.
- ansible.builtin.cron - Keep non-empty crontabs, when removing cron jobs (https://github.com/ansible/ansible/pull/74497).
- ansible.utils.encrypt now handles missing or unusable 'crypt' library.
- ansible_test - add constraint for ``MarkupSafe`` (https://github.com/ansible/ansible/pull/74666)
- apt_key - Binary GnuPG keys downloaded via URLs were corrupted so GnuPG could not import them (https://github.com/ansible/ansible/issues/74424).
- become - fix a regression on Solaris where chmod can return 5 which we interpret as auth failure and stop trying become tmpdir permission fallbacks
- become - work around setfacl not existing on modern Solaris (and possibly failing on some filesystems even when it does exist)
- callback default, now uses task delegate_to instead of delegate vars to display delegate to host
- callbacks, restores missing delegate_vars
- correct doc links for become on warnings over world readable settings.
- correctly use world readable setting since old constant is not 'settable' anymore.
- facts - detect homebrew installed at /opt/homebrew/bin/brew
- filter plugins - patch new versions of Jinja2 to prevent warnings/errors on renamed filter decorators (https://github.com/ansible/ansible/issues/74667)
- get_url - Fixed checksum validation for binary files (leading asterisk) in checksum files (https://github.com/ansible/ansible/pull/74502).
- hostname - Add Rocky Linux support
- ini lookup - handle errors for duplicate keys and missing sections (https://github.com/ansible/ansible/issues/74601)
- interpreter discovery - Debian 8 and lower will avoid unsupported Python3 version in interpreter discovery
- pause - ensure control characters are always set to an appropriate value (https://github.com/ansible/ansible/issues/73264)
- playbook loaded from collection subdir now does not ignore subdirs.
- plugin config now allows list type options to have multiple valid choices (#74225).
- replace - better handling of file operation exceptions (https://github.com/ansible/ansible/pull/74686).
- roles - allow for role arg specs in new meta file (https://github.com/ansible/ansible/issues/74525).
- service - compare version without LooseVersion API (https://github.com/ansible/ansible/issues/74488).

ansible.netcommon
~~~~~~~~~~~~~~~~~

- Variables in play_context will now be updated for netconf connections on each task run.
- fix SCP/SFTP when using network_cli with libssh

ansible.windows
~~~~~~~~~~~~~~~

- win_certificate_store - Make sure `store_name: CertificateAuthority` refers to the `CA` store for backwards compatibility - https://github.com/ansible-collections/ansible.windows/pull/216
- win_reboot - Ensure documented return values are always returned even on a failure
- win_reboot - Handle more connection failures during the reboot phases
- win_reboot - User defined commands are run wrapped as a PowerShell command so they work on all shells - https://github.com/ansible-collections/ansible.windows/issues/36

arista.eos
~~~~~~~~~~

- Add support to accomodate change in username config cli in latest eos software version.
- Fix regex for password prompt.
- argspec key 'shut_down' changed to 'shutdown'.

cisco.asa
~~~~~~~~~

- To fix Cisco ASA network_object object config which wasn't working as expected.
- To fix asa_acls where ipv6 with host wasn't getting rendered as expected and facts was skipping.

cisco.ios
~~~~~~~~~

- Fix IOS bgp global RM tracback while there's no bestpath/nopeerup_delay configured.
- Fix logging commands for v12 versions (https://github.com/ansible-collections/cisco.ios/issues/207).
- To fix IOS vlans RM where traceback was thrown if show vlan wasn't supported on the device and also fix replace and overridden state behaviour.
- To fix Spelling glitch.
- To fix ios acls overridden and replaced state of their inconsistent behaviour (https://github.com/ansible-collections/cisco.ios/issues/250).
- To fix ios_bgp_address_family neighbor next_hop_self param (https://github.com/ansible-collections/cisco.ios/issues/319).
- To fix the wrong arg being passed in acls template function (https://github.com/ansible-collections/cisco.ios/pull/305).

cisco.iosxr
~~~~~~~~~~~

- Add warning when comment is not supported by IOSXR.
- Fix issue of commit operation which was not failing for invalid inputs.

cisco.meraki
~~~~~~~~~~~~

- Allow a state of absent in voice vlan to allow the value to be nulled out(https://github.com/CiscoDevNet/ansible-meraki/issues/238)
- meraki_ms_switchport - access_policy_types choices are incorrect causing failures. (https://github.com/CiscoDevNet/ansible-meraki/issues/227).
- meraki_ms_switchport - link_negotiation choice for 100 Megabit Auto is incorrect causing failures. (https://github.com/CiscoDevNet/ansible-meraki/issues/235).

cisco.mso
~~~~~~~~~

- Add test case and small fixes to mso_schema_site_bd_l3out module
- Fix documentation issues accross modules
- Fix fail_json usage accross module_utils/mso.py
- Fix mso_rest to support HTTPAPI plugin and tests to support ND platform
- Fix mso_user to due to error in v1 API in MSO 3.2
- Fix path issue in mso_schema_template_migrate
- Fixes for site level external epgs and site level L3Outs
- Fixes to support MSO 3.3
- Remove query of all schemas to get schema ID and only query schema ID indentity list API

cisco.nxos
~~~~~~~~~~

- Fix how `send_community` attribute is handled in `nxos_bgp_neighbor_address_family` (https://github.com/ansible-collections/cisco.nxos/issues/281).
- Make `passive_interface` work properly when set to False.

community.crypto
~~~~~~~~~~~~~~~~

- openssh_keypair - fix ``check_mode`` to populate return values for existing keypairs (https://github.com/ansible-collections/community.crypto/issues/113, https://github.com/ansible-collections/community.crypto/pull/230).
- various modules - prevent crashes when modules try to set attributes on not yet existing files in check mode. This will be fixed in ansible-core 2.12, but it is not backported to every Ansible version we support (https://github.com/ansible-collections/community.crypto/issue/242, https://github.com/ansible-collections/community.crypto/pull/243).
- x509_certificate - fix crash when ``assertonly`` provider is used and some error conditions should be reported (https://github.com/ansible-collections/community.crypto/issues/240, https://github.com/ansible-collections/community.crypto/pull/241).

community.digitalocean
~~~~~~~~~~~~~~~~~~~~~~

- digital_ocean inventory script - fail cleaner on invalid ``HOST`` argument to ``--host`` option (https://github.com/ansible-collections/community.digitalocean/pull/44).
- digital_ocean inventory script - implement unimplemented ``use_private_network`` option and register missing ``do_ip_address``, ``do_private_ip_address`` host vars (https://github.com/ansible-collections/community.digitalocean/pull/45/files).
- digital_ocean inventory script - return JSON consistent with specification with ``--host`` (https://github.com/ansible-collections/community.digitalocean/pull/44).
- digital_ocean_database - Fixed DB attribute settings (https://github.com/ansible-collections/community.digitalocean/issues/94).
- digital_ocean_database_info - Cleanup unused attribs (https://github.com/ansible-collections/community.digitalocean/pulls/100).
- digital_ocean_domain - return zone records when creating a new zone (https://github.com/ansible-collections/community.digitalocean/issues/46).
- digital_ocean_droplet - Add integration tests for Droplet active and inactive states (https://github.com/ansible-collections/community.digitalocean/issues/66).
- digital_ocean_droplet - Fix Droplet inactive state (https://github.com/ansible-collections/community.digitalocean/issues/83).
- digital_ocean_droplet - Fixed Droplet inactive state (https://github.com/ansible-collections/community.digitalocean/pull/88).
- digital_ocean_droplet - add missing ``required=True`` on ``do_oauth_token`` in ``argument_spec`` (https://github.com/ansible-collections/community.digitalocean/issues/13).
- digital_ocean_droplet_info - Fix documentation link for `digital_ocean_droplet_info` (https://github.com/ansible-collections/community.digitalocean/pull/81).
- digital_ocean_floating_ip - fixes idempotence (https://github.com/ansible-collections/community.digitalocean/issues/5).
- digital_ocean_snapshot_info - Fix lookup of snapshot_info by_id (https://github.com/ansible-collections/community.digitalocean/issues/92).
- digital_ocean_sshkey - Fixed SSH Key Traceback Issue (https://github.com/ansible-collections/community.digitalocean/issues/68).
- digital_ocean_tag - Fix tag idempotency (https://github.com/ansible-collections/community.digitalocean/issues/61).
- digitalocean - Fix return docs for digital_ocean_sshkey_info (https://github.com/ansible-collections/community.digitalocean/issues/56).
- digitalocean - Update README.md for K8s and databases (https://github.com/ansible-collections/community.digitalocean/pull/80).
- digitalocean inventory plugin - Wire up advertised caching functionality (https://github.com/ansible-collections/community.digitalocean/pull/97).

community.docker
~~~~~~~~~~~~~~~~

- docker-compose - fix not pulling when ``state: present`` and ``stopped: true`` (https://github.com/ansible-collections/community.docker/issues/12, https://github.com/ansible-collections/community.docker/pull/119).
- docker_* modules and plugins, except ``docker_swarm`` connection plugin and ``docker_compose`` and ``docker_stack*` modules - only emit ``tls_hostname`` deprecation message if TLS is actually used (https://github.com/ansible-collections/community.docker/pull/143).
- docker_plugin - also configure plugin after installing (https://github.com/ansible-collections/community.docker/issues/118, https://github.com/ansible-collections/community.docker/pull/135).
- docker_swarm_services - avoid crash during idempotence check if ``published_port`` is not specified (https://github.com/ansible-collections/community.docker/issues/107, https://github.com/ansible-collections/community.docker/pull/136).

community.general
~~~~~~~~~~~~~~~~~

- consul_acl - update the hcl allowlist to include all supported options (https://github.com/ansible-collections/community.general/pull/2495).
- consul_kv lookup plugin - allow to set ``recurse``, ``index``, ``datacenter`` and ``token`` as keyword arguments (https://github.com/ansible-collections/community.general/issues/2124).
- cpanm - also use ``LC_ALL`` to enforce locale choice (https://github.com/ansible-collections/community.general/pull/2731).
- filesystem - repair ``reiserfs`` fstype support after adding it to integration tests (https://github.com/ansible-collections/community.general/pull/2472).
- influxdb_user - allow creation of admin users when InfluxDB authentication is enabled but no other user exists on the database. In this scenario, InfluxDB 1.x allows only ``CREATE USER`` queries and rejects any other query (https://github.com/ansible-collections/community.general/issues/2364).
- influxdb_user - fix bug where an influxdb user has no privileges for 2 or more databases (https://github.com/ansible-collections/community.general/pull/2499).
- influxdb_user - fix bug which removed current privileges instead of appending them to existing ones (https://github.com/ansible-collections/community.general/issues/2609, https://github.com/ansible-collections/community.general/pull/2614).
- iptables_state - call ``async_status`` action plugin rather than its module (https://github.com/ansible-collections/community.general/issues/2700).
- iptables_state - fix a 'FutureWarning' in a regex and do some basic code clean up (https://github.com/ansible-collections/community.general/pull/2525).
- iptables_state - fix a broken query of ``async_status`` result with current ansible-core development version (https://github.com/ansible-collections/community.general/issues/2627, https://github.com/ansible-collections/community.general/pull/2671).
- iptables_state - fix initialization of iptables from null state when adressing more than one table (https://github.com/ansible-collections/community.general/issues/2523).
- java_cert - fix issue with incorrect alias used on PKCS#12 certificate import (https://github.com/ansible-collections/community.general/pull/2560).
- jenkins_plugin - use POST method for sending request to jenkins API when ``state`` option is one of ``enabled``, ``disabled``, ``pinned``, ``unpinned``, or ``absent`` (https://github.com/ansible-collections/community.general/issues/2510).
- json_query filter plugin - avoid 'unknown type' errors for more Ansible internal types (https://github.com/ansible-collections/community.general/pull/2607).
- keycloak_realm - ``ssl_required`` changed from a boolean type to accept the strings ``none``, ``external`` or ``all``. This is not a breaking change since the module always failed when a boolean was supplied (https://github.com/ansible-collections/community.general/pull/2693).
- keycloak_realm - remove warning that ``reset_password_allowed`` needs to be marked as ``no_log`` (https://github.com/ansible-collections/community.general/pull/2694).
- module_helper module utils - ``CmdMixin`` must also use ``LC_ALL`` to enforce locale choice (https://github.com/ansible-collections/community.general/pull/2731).
- netcup_dns - use ``str(ex)`` instead of unreliable ``ex.message`` in exception handling to fix ``AttributeError`` in error cases (https://github.com/ansible-collections/community.general/pull/2590).
- nmap inventory plugin - fix local variable error when cache is disabled (https://github.com/ansible-collections/community.general/issues/2512).
- ovir4 inventory script - improve configparser creation to avoid crashes for options without values (https://github.com/ansible-collections/community.general/issues/674).
- proxmox_kvm - fixed ``vmid`` return value when VM with ``name`` already exists (https://github.com/ansible-collections/community.general/issues/2648).
- redis cache - improved connection string parsing (https://github.com/ansible-collections/community.general/issues/497).
- rhsm_release - fix the issue that module considers 8, 7Client and 7Workstation as invalid releases (https://github.com/ansible-collections/community.general/pull/2571).
- ssh_config - reduce stormssh searches based on host (https://github.com/ansible-collections/community.general/pull/2568/).
- stacki_host - when adding a new server, ``rack`` and ``rank`` must be passed, and network parameters are optional (https://github.com/ansible-collections/community.general/pull/2681).
- terraform - ensure the workspace is set back to its previous value when the apply fails (https://github.com/ansible-collections/community.general/pull/2634).
- xfconf - also use ``LC_ALL`` to enforce locale choice (https://github.com/ansible-collections/community.general/issues/2715).
- zypper_repository - fix idempotency on adding repository with ``$releasever`` and ``$basearch`` variables (https://github.com/ansible-collections/community.general/issues/1985).

community.postgresql
~~~~~~~~~~~~~~~~~~~~

- postgresql_privs - fix ``fail_on_role`` check (https://github.com/ansible-collections/community.postgresql/pull/82).

community.vmware
~~~~~~~~~~~~~~~~

- vmware - fixed a bug that the guest_guestion in the facts doesn't convert to the dictionary (https://github.com/ansible-collections/community.vmware/pull/825).
- vmware - handle exception raised in ``get_all_objs`` and ``find_object_by_name`` which occurs due to multiple parallel operations (https://github.com/ansible-collections/community.vmware/issues/791).
- vmware_cluster_info - Fix a bug that returned enabled_vsan and vsan_auto_claim_storage as lists instead of just true or false (https://github.com/ansible-collections/community.vmware/issues/805).
- vmware_evc_mode - fixed an issue that evc_mode is required when the state parameter set to absent (https://github.com/ansible-collections/community.vmware/pull/764).
- vmware_guest - skip customvalues while deploying VM on a standalone ESXi (https://github.com/ansible-collections/community.vmware/issues/721).
- vmware_host_iscsi_info - fixed an issue that an error occurs gathering iSCSI information against an ESXi Host with iSCSI disabled (https://github.com/ansible-collections/community.vmware/pull/729).
- vmware_vm_info - handle vApp parent logic (https://github.com/ansible-collections/community.vmware/issues/777).
- vmware_vm_shell - handle exception raised while performing the operation (https://github.com/ansible-collections/community.vmware/issues/732).
- vmware_vm_storage_policy_info - fixed an issue that the module can't get storage policy info when the policy has the tag base rules (https://github.com/ansible-collections/community.vmware/pull/788).
- vmware_vmotion - Provide an meaningful error message when providing a bad ESXi node as ``destination_host`` (https://github.com/ansible-collections/vmware/pull/804).

community.windows
~~~~~~~~~~~~~~~~~

- win_domain_group_membership - Handle timeouts when dealing with group with lots of members - https://github.com/ansible-collections/community.windows/pull/204
- win_domain_user - Make sure a password is set to change when it is marked as password needs to be changed before logging in - https://github.com/ansible-collections/community.windows/issues/223
- win_domain_user - fix reporting on user when running in check mode - https://github.com/ansible-collections/community.windows/pull/248
- win_lineinfile - Fix crash when using ``insertbefore`` and ``insertafter`` at the same time - https://github.com/ansible-collections/community.windows/issues/220
- win_partition - Fix gtp_type setting in win_partition - https://github.com/ansible-collections/community.windows/issues/241
- win_psmodule - Makes sure ``-AllowClobber`` is used when updating pre-requisites if requested - https://github.com/ansible-collections/community.windows/issues/42
- win_pssession_configuration - the ``async_poll`` option was not actually used and polling mode was always used with the default poll delay; this change also formally disables ``async_poll=0`` (https://github.com/ansible-collections/community.windows/pull/212).
- win_wait_for_process - Fix bug when specifying multiple ``process_name_exact`` values - https://github.com/ansible-collections/community.windows/issues/203

containers.podman
~~~~~~~~~~~~~~~~~

- Fix ansible-test issues for CI
- Fix failure when listing containers
- Fix idempotency for environment
- Fix ipv6=false issue
- Fix multi-containers options
- Fix overlayfs issue in CI for buildah connection

f5networks.f5_modules
~~~~~~~~~~~~~~~~~~~~~

- Disable cert validaton for Teem
- Fix bigip_gtm_wide_ip to support wildcard type a wide ips
- Fix bigiq non local provider backport from f5_bigip collection
- Fix for bigip_data_group accepts address object without value
- Fix for bigip_pool_member aggregate fails to member comparison
- Fix imish config issue where last character is chopped off by adding extra space to commands
- Fix issue in bigip_firewall_dos_policy where in TMOS v15 and above creating dos vector containers requires additional step in the API
- Fix issue in bigip_gtm_topology_region where parameter region_members being set to empty list returned an error
- Fix issue in bigip_pool_member with module idempotency when pool member status was fqdn-down
- Fix issue where bigip_firewall_port_list was failing when removing objects (#1988)
- Fix issue where empty irules property on device would throw exception during comparison
- Fix issue where viprion platrform interfaces interface naming scheme prevented the use of module
- Fix issue with new telemetry environment variable not populated in provider
- Fix issue with send_teem function ignoring environment variable
- Fix teem version in constants.py
- Fix validation function for bigip_virtual_server module to include new api endpoints for checking SIP profiles
- Fix various minor regressions and improved functional testing in collection

fortinet.fortios
~~~~~~~~~~~~~~~~

- Fix the authorization fails at log in with username and password in FOS7.0.
- Github Issue 103
- Github Issue 105

netapp.azure
~~~~~~~~~~~~

- fix CI pipeline to work with azcollection, and isolate UTs from azcollection.

netapp.cloudmanager
~~~~~~~~~~~~~~~~~~~

- na_cloudmanager_aggregate - Improve error message
- na_cloudmanager_cifs_server - Fix incorrect API call when is_workgroup is true
- na_cloudmanager_connector_azure - Add subnet_name as aliases of subnet_id, vnet_name as aliases of vnet_id.
- na_cloudmanager_connector_azure - Change client_id as optional
- na_cloudmanager_connector_azure - Fix KeyError client_id
- na_cloudmanager_connector_azure - Fix python error - msrest.exceptions.ValidationError. Parameter 'Deployment.properties' can not be None.
- na_cloudmanager_connector_azure - Fix wrong example on the document and update account_id is required field on deletion.
- na_cloudmanager_cvo_gcp - Apply network_project_id check on vpc1_cluster_connectivity, vpc2_ha_connectivity, vpc3_data_replication, subnet1_cluster_connectivity, subnet2_ha_connectivity, subnet3_data_replication
- na_cloudmanager_cvo_gcp - Change vpc_id from optional to required.
- na_cloudmanager_nss_account - Improve error message
- na_cloudmanager_volume - Improve error message

netapp.elementsw
~~~~~~~~~~~~~~~~

- requirements.txt - point to the correct python dependency

netapp.ontap
~~~~~~~~~~~~

- na_ontap_autosupport - KeyError - No element by given name validate-digital-certificate.
- na_ontap_autosupport - TypeError - '>' not supported between instances of 'str' and 'list'.
- na_ontap_flexcache - one occurrence of msg missing in call to fail_json.
- na_ontap_igroup - one occurrence of msg missing in call to fail_json.
- na_ontap_igroups - nested igroups are not supported on ONTAP 9.9.0 but are on 9.9.1.
- na_ontap_iscsi_security - IndexError list index out of range if vserver does not exist
- na_ontap_iscsi_security - cannot change authentication_type
- na_ontap_lun - three occurrencse of msg missing in call to fail_json.
- na_ontap_lun_map_reporting_nodes - one occurrence of msg missing in call to fail_json.
- na_ontap_quotas - fail to reinitialize on create if quota is already on.
- na_ontap_snapmirror - one occurrence of msg missing in call to fail_json.

netapp_eseries.santricity
~~~~~~~~~~~~~~~~~~~~~~~~~

- Fix PEM certificate/key imports in the na_santricity_server_certificate module.
- Fix host and host port names from being changed to lower case.
- Fix login banner message option bytes error in na_santricity_global.
- Fix missing proxy client and server certificate in management role.
- Fix missing proxy validate_certs and change current proxy password variables.
- Fix na_santricity_mgmt_interface IPv4 and IPv6 form validation.
- Fix pkcs8 private key passphrase issue.
- Fix server certificate module not forwarding certificate imports to the embedded web services.
- Fix storage system admin password change from web services proxy in na_santricity_auth module.

netbox.netbox
~~~~~~~~~~~~~

- Allow ``virtual_chassis`` to be found via name [#402](https://github.com/netbox-community/ansible_modules/issues/402)
- Fix mapping between power_outlet_template and power_port_template.
- Inventory - Update plugin to support location for NetBox 2.11+ [#510](https://github.com/netbox-community/ansible_modules/pull/510)
- inventory - Fix rack-group -> location for NetBox 2.11 changes.
- inventory - Properly handle interface tags.
- netbox_tenant - Fix example to match argspec.

ovirt.ovirt
~~~~~~~~~~~

- hosted_engine_setup - Use ovirt_host module to discover iscsi (https://github.com/oVirt/ovirt-ansible-collection/pull/275).
- hosted_engine_setup - align with ansible-lint 5.0.0 (https://github.com/oVirt/ovirt-ansible-collection/pull/271).

servicenow.servicenow
~~~~~~~~~~~~~~~~~~~~~

- makes auth backwards compatible by defaulting to OAuth if client_id is present without specifying auth
- order_by again working by locally sorting return list of records

theforeman.foreman
~~~~~~~~~~~~~~~~~~

- host - pass the right image id to the compute resource when creating a host (https://github.com/theforeman/foreman-ansible-modules/issues/1160, https://bugzilla.redhat.com/show_bug.cgi?id=1911670)

vyos.vyos
~~~~~~~~~

- change admin_distance to distance while generating static_routes nexthop command.
- firewall_global - port-groups were not added (https://github.com/ansible-collections/vyos.vyos/issues/107)

Known Issues
------------

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- idrac_user - Issue(192043) Module may error out with the message ``unable to perform the import or export operation because there are pending attribute changes or a configuration job is in progress``. Wait for the job to complete and run the task again.
- ome_smart_fabric_uplink - Issue(186024) ome_smart_fabric_uplink module does not allow the creation of multiple uplinks of the same name even though this is supported by OpenManage Enterprise Modular. If an uplink is created using the same name as an existing uplink, the existing uplink is modified.

New Plugins
-----------

Filter
~~~~~~

- community.general.groupby_as_dict - Transform a sequence of dictionaries to a dictionary where the dictionaries are indexed by an attribute

Httpapi
~~~~~~~

- cisco.mso.mso - MSO Ansible HTTPAPI Plugin.

Lookup
~~~~~~

- community.general.dependent - Composes a list with nested elements of other lists or dicts which can depend on previous loop variables
- community.general.random_pet - Generates random pet names
- community.general.random_string - Generates random string

Netconf
~~~~~~~

- cisco.nxos.nxos - Use nxos netconf plugin to run netconf commands on Cisco NX-OS platform.

New Modules
-----------

cisco.ios
~~~~~~~~~

- cisco.ios.ios_logging_global - Logging resource module.
- cisco.ios.ios_prefix_lists - Prefix Lists resource module.
- cisco.ios.ios_route_maps - Route Maps resource module.

cloudscale_ch.cloud
~~~~~~~~~~~~~~~~~~~

- cloudscale_ch.cloud.custom_image - Manage custom images on the cloudscale.ch IaaS service

community.crypto
~~~~~~~~~~~~~~~~

- community.crypto.openssl_publickey_info - Provide information for OpenSSL public keys

community.digitalocean
~~~~~~~~~~~~~~~~~~~~~~

- community.digitalocean.digital_ocean_balance_info - Display DigitalOcean customer balance
- community.digitalocean.digital_ocean_database - Create and delete a DigitalOcean database
- community.digitalocean.digital_ocean_database_info - Gather information about DigitalOcean databases
- community.digitalocean.digital_ocean_droplet_info - Gather information about DigitalOcean Droplets
- community.digitalocean.digital_ocean_kubernetes - Create and delete a DigitalOcean Kubernetes cluster
- community.digitalocean.digital_ocean_kubernetes_info - Returns information about an existing DigitalOcean Kubernetes cluster

community.general
~~~~~~~~~~~~~~~~~

Cloud
^^^^^

Misc
....

- community.general.proxmox_nic - Management of a NIC of a Qemu(KVM) VM in a Proxmox VE cluster.

Database
^^^^^^^^

Saphana
.......

- community.general.hana_query - Execute SQL on HANA

Files
^^^^^

- community.general.sapcar_extract - Manages SAP SAPCAR archives

Notification
^^^^^^^^^^^^

- community.general.discord - Send Discord messages

Packaging
^^^^^^^^^

Os
..

- community.general.pacman_key - Manage pacman's list of trusted keys

community.vmware
~~~~~~~~~~~~~~~~

- community.vmware.vmware_host_tcpip_stacks - Manage the TCP/IP Stacks configuration of ESXi host

community.windows
~~~~~~~~~~~~~~~~~

- community.windows.win_feature_info - Gather information about Windows features

containers.podman
~~~~~~~~~~~~~~~~~

- containers.podman.podman_play - Play Kubernetes YAML files with Podman

dellemc.enterprise_sonic
~~~~~~~~~~~~~~~~~~~~~~~~

- dellemc.enterprise_sonic.sonic_aaa - AAA resource module.
- dellemc.enterprise_sonic.sonic_radius_server - RADIUS resource module.
- dellemc.enterprise_sonic.sonic_system - SYSTEM resource module.
- dellemc.enterprise_sonic.sonic_tacacs_server - TACACS Server resource module.

netapp.cloudmanager
~~~~~~~~~~~~~~~~~~~

- netapp.cloudmanager.na_cloudmanager_snapmirror - NetApp Cloud Manager SnapMirror

netapp.ontap
~~~~~~~~~~~~

- netapp.ontap.na_ontap_publickey - NetApp ONTAP publickey configuration
- netapp.ontap.na_ontap_service_policy - NetApp ONTAP service policy configuration

sensu.sensu_go
~~~~~~~~~~~~~~

- sensu.sensu_go.ad_auth_provider - Manage Sensu AD authentication provider
- sensu.sensu_go.auth_provider_info - List Sensu authentication providers
- sensu.sensu_go.ldap_auth_provider - Manage Sensu LDAP authentication provider
- sensu.sensu_go.oidc_auth_provider - Manage Sensu OIDC authentication provider

theforeman.foreman
~~~~~~~~~~~~~~~~~~

- theforeman.foreman.content_view_info - Fetch information about Content Views
- theforeman.foreman.content_view_version_info - Fetch information about Content Views
- theforeman.foreman.domain_info - Fetch information about Domains
- theforeman.foreman.host_errata_info - Fetch information about Host Errata
- theforeman.foreman.repository_set_info - Fetch information about Red Hat Repositories
- theforeman.foreman.setting_info - Fetch information about Settings
- theforeman.foreman.subnet_info - Fetch information about Subnets
- theforeman.foreman.subscription_info - Fetch information about Subscriptions

vyos.vyos
~~~~~~~~~

- vyos.vyos.vyos_route_maps - Route Map Resource Module.

Unchanged Collections
---------------------

- amazon.aws (still version 1.5.0)
- ansible.posix (still version 1.2.0)
- check_point.mgmt (still version 2.0.0)
- chocolatey.chocolatey (still version 1.1.0)
- cisco.aci (still version 2.0.0)
- cisco.intersight (still version 1.0.15)
- cisco.nso (still version 1.0.3)
- cisco.ucs (still version 1.6.0)
- community.aws (still version 1.5.0)
- community.azure (still version 1.0.0)
- community.fortios (still version 1.0.0)
- community.google (still version 1.0.0)
- community.grafana (still version 1.2.1)
- community.hashi_vault (still version 1.1.3)
- community.hrobot (still version 1.1.1)
- community.kubernetes (still version 1.2.1)
- community.kubevirt (still version 1.0.0)
- community.libvirt (still version 1.0.1)
- community.mongodb (still version 1.2.1)
- community.mysql (still version 2.1.0)
- community.network (still version 3.0.0)
- community.okd (still version 1.1.2)
- community.proxysql (still version 1.0.0)
- community.rabbitmq (still version 1.0.3)
- community.routeros (still version 1.1.0)
- community.skydive (still version 1.0.0)
- community.sops (still version 1.0.6)
- community.zabbix (still version 1.3.0)
- cyberark.conjur (still version 1.1.0)
- dellemc.os10 (still version 1.1.1)
- dellemc.os6 (still version 1.0.7)
- dellemc.os9 (still version 1.0.4)
- frr.frr (still version 1.0.3)
- gluster.gluster (still version 1.0.1)
- google.cloud (still version 1.0.2)
- hetzner.hcloud (still version 1.4.3)
- hpe.nimble (still version 1.1.3)
- ibm.qradar (still version 1.0.3)
- infinidat.infinibox (still version 1.2.4)
- kubernetes.core (still version 1.2.1)
- mellanox.onyx (still version 1.0.0)
- netapp.aws (still version 21.2.0)
- ngine_io.cloudstack (still version 2.1.0)
- ngine_io.exoscale (still version 1.0.0)
- ngine_io.vultr (still version 1.1.0)
- openstack.cloud (still version 1.4.0)
- openvswitch.openvswitch (still version 2.0.0)
- purestorage.flasharray (still version 1.8.0)
- purestorage.flashblade (still version 1.6.0)
- splunk.es (still version 1.0.2)
- wti.remote (still version 1.0.1)

v4.0.0
======

.. contents::
  :local:
  :depth: 2

Release Summary
---------------

Release Date: 2021-05-11

`Porting Guide <https://docs.ansible.com/ansible/devel/porting_guides.html>`_

Ansible-core
------------

Ansible 4.0.0 contains Ansible-core version 2.11.0.
This is a newer version than version 2.10.5 contained in the previous Ansible release.

The changes are reported in the combined changelog below.

Included Collections
--------------------

If not mentioned explicitly, the changes are reported in the combined changelog below.

+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| Collection                    | Ansible 3.0.0 | Ansible 4.0.0 | Notes                                                                                                                        |
+===============================+===============+===============+==============================================================================================================================+
| amazon.aws                    | 1.3.0         | 1.5.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| ansible.netcommon             | 1.5.0         | 2.0.2         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| ansible.posix                 | 1.1.1         | 1.2.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| ansible.utils                 | 2.0.0         | 2.1.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| ansible.windows               | 1.3.0         | 1.5.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| arista.eos                    | 1.3.0         | 2.1.1         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| awx.awx                       | 17.0.1        | 19.0.0        | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| azure.azcollection            | 1.4.0         | 1.5.0         | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| chocolatey.chocolatey         | 1.0.2         | 1.1.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.asa                     | 1.0.4         | 2.0.1         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.intersight              | 1.0.10        | 1.0.15        | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.ios                     | 1.3.0         | 2.0.1         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.iosxr                   | 1.2.1         | 2.1.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.meraki                  | 2.2.0         | 2.2.1         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.nxos                    | 1.4.0         | 2.2.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cloudscale_ch.cloud           | 2.0.0         | 2.1.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.aws                 | 1.3.0         | 1.5.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.crypto              | 1.4.0         | 1.6.2         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.digitalocean        | 1.0.0         | 1.1.1         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.docker              | 1.2.2         | 1.5.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.general             | 2.0.1         | 3.0.2         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.grafana             | 1.1.0         | 1.2.1         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.hashi_vault         | 1.0.0         | 1.1.3         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.hrobot              | 1.1.0         | 1.1.1         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.kubernetes          | 1.1.1         | 1.2.1         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.libvirt             | 1.0.0         | 1.0.1         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.mongodb             | 1.2.0         | 1.2.1         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.mysql               | 1.2.0         | 2.1.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.network             | 2.0.1         | 3.0.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.okd                 | 1.0.1         | 1.1.2         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.postgresql          | 1.1.1         | 1.2.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.rabbitmq            | 1.0.1         | 1.0.3         | The collection did not have a changelog in this version.                                                                     |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.sops                | 1.0.4         | 1.0.6         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.vmware              | 1.7.0         | 1.9.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.windows             | 1.2.0         | 1.3.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.zabbix              | 1.2.0         | 1.3.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| containers.podman             | 1.4.1         | 1.5.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cyberark.pas                  | 1.0.5         | 1.0.6         | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| dellemc.enterprise_sonic      |               | 1.0.3         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| dellemc.openmanage            | 3.0.0         | 3.3.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| dellemc.os6                   | 1.0.6         | 1.0.7         | There are no changes recorded in the changelog.                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| dellemc.os9                   | 1.0.3         | 1.0.4         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| f5networks.f5_modules         | 1.7.1         | 1.9.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| fortinet.fortimanager         | 2.0.1         | 2.0.2         | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| fortinet.fortios              | 1.1.8         | 2.0.1         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| hetzner.hcloud                | 1.2.1         | 1.4.3         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| hpe.nimble                    |               | 1.1.3         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| inspur.sm                     | 1.1.2         | 1.1.4         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| junipernetworks.junos         | 1.3.0         | 2.1.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| kubernetes.core               | 1.1.1         | 1.2.1         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| netapp.aws                    | 20.9.0        | 21.2.0        |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| netapp.azure                  |               | 21.5.0        |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| netapp.cloudmanager           |               | 21.5.1        |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| netapp.elementsw              | 20.11.0       | 21.3.0        |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| netapp.ontap                  | 21.1.1        | 21.5.0        |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| netapp.um_info                |               | 21.5.0        |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| netapp_eseries.santricity     | 1.1.0         | 1.2.7         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| netbox.netbox                 | 2.0.0         | 3.0.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| ngine_io.cloudstack           | 2.0.0         | 2.1.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| openstack.cloud               | 1.2.1         | 1.4.0         | The collection did not have a changelog in this version.                                                                     |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| openvswitch.openvswitch       | 1.1.0         | 2.0.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| ovirt.ovirt                   | 1.3.0         | 1.4.2         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| purestorage.flasharray        | 1.5.1         | 1.8.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| purestorage.flashblade        | 1.4.0         | 1.6.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| sensu.sensu_go                | 1.8.0         | 1.9.4         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| servicenow.servicenow         | 1.0.4         | 1.0.5         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| t_systems_mms.icinga_director | 1.13.0        | 1.16.0        | The collection did not have a changelog in this version.                                                                     |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| theforeman.foreman            | 1.5.1         | 2.0.1         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| vyos.vyos                     | 1.1.1         | 2.2.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+

Major Changes
-------------

Ansible-core
~~~~~~~~~~~~

- A collection can be reinstalled with new version requirements without using the ``--force`` flag. The collection's dependencies will also be updated if necessary with the new requirements. Use ``--upgrade`` to force transitive dependency updates.
- AnsibleModule - use ``ArgumentSpecValidator`` class for validating argument spec and remove private methods related to argument spec validation. Any modules using private methods should now use the ``ArgumentSpecValidator`` class or the appropriate validation function.
- Declared ``resolvelib >= 0.5.3, < 0.6.0`` a direct dependency of
  ansible-core. Refs:
  - https://github.com/sarugaku/resolvelib
  - https://pypi.org/p/resolvelib
  - https://pradyunsg.me/blog/2020/03/27/pip-resolver-testing
- It became possible to install Ansible Collections from local folders and namespaces folder similar to SCM structure with multiple collections.
- It became possible to upgrade Ansible collections from Galaxy servers using the ``--upgrade`` option with ``ansible-galaxy collection install``.
- Support for role argument specification validation at role execution time. When a role contains an argument spec, an implicit validation task is inserted at the start of role execution.
- add ``ArgumentSpecValidator`` class for validating parameters against an argument spec outside of ``AnsibleModule`` (https://github.com/ansible/ansible/pull/73335)
- ansible-test - Tests run with the ``centos6`` and ``default`` test containers now use a PyPI proxy container to access PyPI when Python 2.6 is used. This allows tests running under Python 2.6 to continue functioning even though PyPI is discontinuing support for non-SNI capable clients.

ansible.netcommon
~~~~~~~~~~~~~~~~~

- Remove deprecated connection arguments from netconf_config

arista.eos
~~~~~~~~~~

- Requires ansible.netcommon v2.0.0+ to support `ansible_network_single_user_mode` and `ansible_network_import_modules` - Please refer to ansible.netcommon `changelog <https://github.com/ansible-collections/ansible.netcommon/blob/main/changelogs/CHANGELOG.rst#ansible-netcommon-collection-release-notes>`_ for more details.

cisco.asa
~~~~~~~~~

- Please refer to ansible.netcommon `changelog <https://github.com/ansible-collections/ansible.netcommon/blob/main/changelogs/CHANGELOG.rst#ansible-netcommon-collection-release-notes>` for more details.
- Requires ansible.netcommon v2.0.0+ to support `ansible_network_single_user_mode` and `ansible_network_import_modules`.

cisco.ios
~~~~~~~~~

- Please refer to ansible.netcommon `changelog <https://github.com/ansible-collections/ansible.netcommon/blob/main/changelogs/CHANGELOG.rst#ansible-netcommon-collection-release-notes>`_ for more details.
- Requires ansible.netcommon v2.0.0+ to support `ansible_network_single_user_mode` and `ansible_network_import_modules`.

cisco.iosxr
~~~~~~~~~~~

- Please refer to ansible.netcommon `changelog <https://github.com/ansible-collections/ansible.netcommon/blob/main/changelogs/CHANGELOG.rst#ansible-netcommon-collection-release-notes>`_ for more details.
- Requires ansible.netcommon v2.0.0+ to support `ansible_network_single_user_mode` and `ansible_network_import_modules`.
- ipaddress is no longer in ansible.netcommon. For Python versions without ipaddress (< 3.0), the ipaddress package is now required.

cisco.nxos
~~~~~~~~~~

- Please refer to ansible.netcommon `changelog <https://github.com/ansible-collections/ansible.netcommon/blob/main/changelogs/CHANGELOG.rst#ansible-netcommon-collection-release-notes>`_ for more details.
- Requires ansible.netcommon v2.0.0+ to support `ansible_network_single_user_mode` and `ansible_network_import_modules`.

community.grafana
~~~~~~~~~~~~~~~~~

- introduce "skip_version_check" parameter in grafana_teams and grafana_folder modules (#147)

community.mysql
~~~~~~~~~~~~~~~

- mysql_replication - add deprecation warning that the ``Is_Slave`` and ``Is_Master`` return values will be replaced with ``Is_Primary`` and ``Is_Replica`` in ``community.mysql`` 3.0.0 (https://github.com/ansible-collections/community.mysql/pull/147).
- mysql_replication - the choices of the ``state`` option containing ``master`` will be finally replaced with the alternative ``primary`` choices in ``community.mysql`` 3.0.0, add deprecation warnings (https://github.com/ansible-collections/community.mysql/pull/150).
- mysql_replication - the mode options values ``getslave``, ``startslave``, ``stopslave``, ``resetslave``, ``resetslaveall` and the master_use_gtid option ``slave_pos`` are deprecated (see the alternative values) and will be removed in ``community.mysql`` 3.0.0 (https://github.com/ansible-collections/community.mysql/pull/97).
- mysql_replication - the return value ``Is_Slave`` and ``Is_Master`` will be replaced with ``Is_Replica`` and ``Is_Primary`` in ``community.mysql`` 3.0.0 (https://github.com/ansible-collections/community.mysql/issues/145).
- mysql_replication - the word ``SLAVE`` in messages returned by the module will be changed to ``REPLICA`` in ``community.mysql`` 2.0.0 (https://github.com/ansible-collections/community.mysql/issues/98).
- mysql_replication - the word ``master`` in messages returned by the module will be replaced with ``primary`` in ``community.mysql`` 3.0.0 (https://github.com/ansible-collections/community.mysql/issues/145).
- mysql_replication - the word ``slave`` in messages returned by the module replaced with ``replica`` (https://github.com/ansible-collections/community.mysql/issues/98).
- mysql_user - the ``REQUIRESSL`` is an alias for the ``ssl`` key in the ``tls_requires`` option in ``community.mysql`` 2.0.0 and support will be dropped altogether in ``community.mysql`` 3.0.0 (https://github.com/ansible-collections/community.mysql/issues/121).

fortinet.fortios
~~~~~~~~~~~~~~~~

- New module fortios_configuration_fact
- New module fortios_json_generic
- New module fortios_monitor
- New module fortios_monitor_fact

junipernetworks.junos
~~~~~~~~~~~~~~~~~~~~~

- Please refer to ansible.netcommon `changelog <https://github.com/ansible-collections/ansible.netcommon/blob/main/changelogs/CHANGELOG.rst#ansible-netcommon-collection-release-notes>`_ for more details.
- Requires ansible.netcommon v2.0.0+ to support `ansible_network_single_user_mode` and `ansible_network_import_modules`.

netapp.ontap
~~~~~~~~~~~~

- na_ontap_autosupport - Added REST support to the module.

servicenow.servicenow
~~~~~~~~~~~~~~~~~~~~~

- refactored client to inherit from AnsibleModule
- supports OpenID Connect authentication protocol
- supports bearer tokens for authentication

vyos.vyos
~~~~~~~~~

- Please refer to ansible.netcommon `changelog <https://github.com/ansible-collections/ansible.netcommon/blob/main/changelogs/CHANGELOG.rst#ansible-netcommon-collection-release-notes>`_ for more details.
- Requires ansible.netcommon v2.0.0+ to support `ansible_network_single_user_mode` and `ansible_network_import_modules`
- ipaddress is no longer in ansible.netcommon. For Python versions without ipaddress (< 3.0), the ipaddress package is now required.

Minor Changes
-------------

Ansible-core
~~~~~~~~~~~~

- Add ``--format`` CLI option to ``ansible-galaxy collection list`` which allows for ``human`` (default), ``yaml``, or ``json``. (https://github.com/ansible/ansible/pull/73474)
- Add an example for using var in with_sequence (https://github.com/ansible/ansible/issues/68836).
- Add new rolespec_validate option to the import/include_role modules do allow disabling of the implicit role arg validation task on a per-role basis.
- Add option to pass extra vars to ansible-inventory
- Add path of collection location in Ansible CLI version info.
- Add standard Python 2/3 compatibility boilerplate to setup script, module_utils and docs_fragments which were missing them.
- Add support for `argument_specs` data in role metadata.
- Add support for datetime.date object type in module result (https://github.com/ansible/ansible/issues/70583).
- Add which conditional is being evaluated at each step when debugging.
- Add yum/dnf version comparison documentation for package install
- Added NO_COLOR environment var to ansible color configuration, allowing it to integrate with existing convention.
- Added name of aliases in user error (https://github.com/ansible/ansible/issues/58752).
- Added support for GSSAPI/Kerberos authentication with ``urls.py`` that is used by ``uri`` and ``get_url``.
- Added support for specify custom credentials for GSSAPI authentication.
- Allow an attribute to be passed to the min and max filters with Jinja 2.10+
- Allow for the skipped filter to be used on a registered looped task results. (https://github.com/ansible/ansible/issues/16949)
- Allow inventory plugins access to extra vars by default
- Allow unsafe_writes to be set on target via env var, for those targets that need a blanket setting.
- Also added extra vars cli option to console CLI.
- AnsiballZ - Improve performance of ``ModuleDepFinder`` by using faster lookups and reducing the object types that are walked while looking for ``import`` statements. (https://github.com/ansible/ansible/pull/70475)
- CLI - Specify jinja version in ``--version`` output
- CLI - Specify whether PyYAML includes libyaml support in version output
- CLI version displays clarified as core version
- Callbacks - Migrate more places in the ``TaskExecutor`` to sending callbacks directly over the queue, instead of sending them as ``TaskResult`` and short circuiting in the Strategy to send the callback. This enables closer to real time callbacks of retries and loop results (https://github.com/ansible/ansible/issues/73899)
- Collection routing: Cisco NSO content from community.network migrated to cisco.nso (https://github.com/ansible/ansible/pull/73046).
- Collection routing: DellEMC content from community.general migrated to dellemc.openmanage (https://github.com/ansible/ansible/pull/73046).
- Collection routing: FortiOS content from community.network migrated to community.fortios (https://github.com/ansible/ansible/pull/73046).
- Collection routing: Google content from community.general migrated to community.google (https://github.com/ansible/ansible/pull/73046).
- Collection routing: Hashi Vault content from community.general migrated to community.hashi_vault (https://github.com/ansible/ansible/pull/73046).
- Collection routing: Hetzner Robot content from community.general migrated to community.hrobot (https://github.com/ansible/ansible/pull/73046).
- Collection routing: KubeVirt content from community.general migrated to community.kubevirt (https://github.com/ansible/ansible/pull/73046).
- Collection routing: OC content from community.general migrated to community.okd (https://github.com/ansible/ansible/pull/73046).
- Collection routing: PostgreSQL content from community.general migrated to community.postgresql (https://github.com/ansible/ansible/pull/73046).
- Collection routing: RouterOS content from community.network migrated to community.routeros (https://github.com/ansible/ansible/pull/73046).
- Collection routing: docker content from community.general migrated to community.docker (https://github.com/ansible/ansible/pull/73046).
- Controller - Add warning for Ansible 2.11 when running a Python version older than Python 3.8 to inform users that 2.12 will only support Python 3.8 and newer on the controller. Starting with Ansible 2.11, the project will only be packaged for Python 3.8 and newer.
- Discourage the use of 'hexdigits' in password lookup, as it distorts expected entropy.
- Enable extra vars for inventory plugin options
- Errors - Ensure that errors passed with ``orig_exc`` include the context of that exception (https://github.com/ansible/ansible/issues/68605)
- Filters - Add new ``split`` filter for splitting strings
- Fixed ansible-doc to not substitute for words followed by parenthesis.  For instance, ``IBM(International Business Machines)`` will no longer be substituted with a link to a non-existent module. https://github.com/ansible/ansible/pull/71070
- Force the template module to use non-native Jinja2 (https://github.com/ansible/ansible/issues/46169)
- Internal config entries will not be documented, to mark an entry as internal it must start with `_`.
- Interpreter Discovery - Add Python 3.8 and Python 3.9 to the fallback list
- Minor code cleanup in plugin loader.
- Module API - libselinux-python is no longer required for basic module API selinux operations (affects core modules assemble, blockinfile, copy, cron, file, get_url, lineinfile, setup, replace, unarchive, uri, user, yum_repository)
- Module API - new module_respawn API allows modules that need to run under a specific Python interpreter to respawn in place under that interpreter
- Module iptables multiport destination support added (https://github.com/ansible/ansible/pull/72928)
- Module iptables set/ipset support added (https://github.com/ansible/ansible/pull/72984)
- New 'timeout' feature added to adhoc and console CLIs, corresponding to the recent 'timeout' task keyword.
- New virtualization facts, ``virtualization_tech_guest`` and ``virtualization_tech_host`` now allow for conveying when a system is a host or guest of multiple virtualization technologies.
- Now 'choices' keyword in config definitions also restricts valid values for the entry.
- Refactored ``ansible-galaxy collection [download|install|list|verify]`` CLI subcommands with the public interface kept intact.
- Restructured _fixup_perms2() in ansible.plugins.action to make it more linear
- Shadow prompt input to ansible-vault encrypt-string unless the ``--show-input`` flag is set
- Switch to hashlib.sha256() for ansible-test to allow for FIPs mode.
- TOML inventory plugin is no longer in preview status
- Templar - reduce the complexity of ``Templar._lookup`` (https://github.com/ansible/ansible/pull/73277)
- The ``csvfile`` lookup plugin now uses ``parse_kv()`` internally. As a result, multi-word search keys can now be passed.
- The ``csvfile`` lookup plugin's documentation has been fixed; it erroneously said that the delimiter could be ``t`` which was never true. We now accept ``\t``, however, and the error in the documentation has been fixed to note that.
- The constructed inventory plugin has new option to force using vars plugins on previouslly processed inventory sources.
- The find module is now more specific about the reasons it skips candidate files.
- The logging functionality in module_utils.basic now returns a nicer error when it falls back to syslog but ends up getting a TypeError thrown back.
- The new dependency resolver prefers ``MANIFEST.json`` over ``galaxy.yml`` if it exists in the target directory.
- The plugin loader now keeps track of the collection where a plugin was resolved to, in particular whether the plugin was loaded from ansible-core's internal paths (``ansible.builtin``) or from user-supplied paths (no collection name).
- Toggle allowing usage of extra_vars in compose
- When connecting as an unprivileged user, and becoming an unprivileged user, we now fall back to also trying ``chmod +a`` which works on macOS and makes use of ACLs.
- allow tree callback plugin to be configurable, for use with playbooks.
- ansible-doc - In Windows setup steps, ``ExecutionPolicy`` should be restored to default value ``RemoteSigned`` (https://github.com/ansible/ansible/pull/72993).
- ansible-doc - provide ``has_action`` field in JSON output for modules. That information is currently only available in the text view (https://github.com/ansible/ansible/pull/72359).
- ansible-doc has new option to show keyword documentation.
- ansible-doc will now format, ``L()``, ``R()``, and ``HORIZONTALLINE`` in plugin docs just as the website docs do.  https://github.com/ansible/ansible/pull/71070
- ansible-galaxy - Add installation successful message
- ansible-galaxy - Added caching mechanisms when retrieving collection info to speed up installs and downloads
- ansible-galaxy - Change the output verbosity level of the download message from 3 to 0 (https://github.com/ansible/ansible/issues/70010)
- ansible-galaxy - Ensure ``get_collection_versions`` returns an empty list when a collection does not exist for consistency across API versions.
- ansible-galaxy - find any collection dependencies in the globally configured Galaxy servers and not just the server the parent collection is from.
- ansible-galaxy CLI - ``collection verify`` command now exits with a non-zero exit code on verification failure
- ansible-galaxy CLI - ``collection verify`` command now supports a ``--offline`` option for local-only verification
- ansible-test - A warning is no longer emitted when a ``pip*`` or ``python*`` binary is found without a matching couterpart.
- ansible-test - Add ``macos/10.15`` as a supported value for the ``--remote`` option.
- ansible-test - Add a ``--docker-network`` option to choose the network for running containers when using the ``--docker`` option.
- ansible-test - Add constraint for ``decorator`` for Python versions prior to 3.5.
- ansible-test - Add support for running tests on Fedora 33 (https://github.com/ansible/ansible/pull/72861).
- ansible-test - Added Ubuntu 20.04 LTS image to the default completion list
- ansible-test - Added a ``--export`` option to the ``ansible-test coverage combine`` command to facilitate multi-stage aggregation of coverage in CI pipelines.
- ansible-test - Added the ``-remote rhel/7.9`` option to run tests on RHEL 7.9
- ansible-test - Allow custom ``--remote-stage`` options for development and testing.
- ansible-test - CentOS 8 container is now 8.2.2004 (https://github.com/ansible/distro-test-containers/pull/45).
- ansible-test - Changed the internal name of the custom plugin used to identify use of unwanted imports and functions.
- ansible-test - Cleaned up code to resolve warnings and errors reported by PyCharm.
- ansible-test - Code cleanup in the ``import`` sanity test.
- ansible-test - Code cleanup in the internal logic for code coverage collection of PowerShell modules.
- ansible-test - Collections can now specify pip constraints for unit and integration test requirements using ``tests/unit/constraints.txt`` and ``tests/integration/constraints.txt`` respectively.
- ansible-test - Containers used with the ``--remote`` option have been updated to version 1.29.0 to include the latest Ansible requirements.
- ansible-test - Files used to track remote instances no longer have a region suffix.
- ansible-test - Fix ``ansible-test coverage`` reporting sub-commands (``report``, ``html``, ``xml``) on Python 2.6.
- ansible-test - Fix container hostname/IP discovery for the ``acme`` test plugin.
- ansible-test - FreeBSD 11.4 and 12.2 provisioning can now be used with the ``--python 3.8`` option.
- ansible-test - FreeBSD instances provisioned with ``--remote`` now make ``libyaml`` available for use with PyYAML installation.
- ansible-test - Generation of an ``egg-info`` directory, if needed, is now done after installing test dependencies and before running tests. When running from an installed version of ``ansible-test`` a temporary directory is used to avoid permissions issues. Previously it was done before installing test dependencies and adjacent to the installed directory.
- ansible-test - Implemented CloudStack test container selection by ENV variable `ANSIBLE_CLOUDSTACK_CONTAINER` with a default to `quay.io/ansible/cloudstack-test-container:1.4.0`.
- ansible-test - Improved handling of minimum Python version requirements for sanity tests. Supported versions are now included in warning messages displayed when tests are skipped.
- ansible-test - More sanity test requirements have been pinned to specific versions to provide consistent test results.
- ansible-test - Most sanity test specific ``pip`` constraints are now used only when running sanity tests. This should reduce conflicts with ``pip`` requirements and constraints when testing collections.
- ansible-test - Most sanity tests are now skipped on Python 3.5 and earlier with a warning. Previously this was done for Python 2.7 and earlier.
- ansible-test - Now supports freebsd/11.4 remote (https://github.com/ansible/ansible/issues/48782).
- ansible-test - Now supports freebsd/12.2 remote (https://github.com/ansible/ansible/issues/72366).
- ansible-test - OpenSuse container now uses Leap 15.2 (https://github.com/ansible/distro-test-containers/pull/48).
- ansible-test - Pin the ``virtualenv`` version used for ``--remote`` pip installs to the latest version supported by Python 2.x, which is version 16.7.10.
- ansible-test - Provisioning of RHEL instances now includes installation of pinned versions of ``packaging`` and ``pyparsing`` to match the downstream vendored versions.
- ansible-test - RHEL 8.2+ provisioning can now be used with the ``--python 3.8`` option, taking advantage of the Python 3.8 AppStream.
- ansible-test - Raise the number of bytes scanned by ansible-test to determine if a file is binary to 4096.
- ansible-test - Refactor code for installing ``cryptography`` to allow re-use in the future.
- ansible-test - Refactor code to remove unused logic for obsolete support of multiple provisioning endpoints.
- ansible-test - Remove ``pytest < 6.0.0`` constraint for managed installations on Python 3.x now that pytest 6 is supported.
- ansible-test - Remove em dash from the Pytest configuration file in order to be readable on systems where preferred encoding is ASCII. (https://github.com/ansible/ansible/issues/71739)
- ansible-test - Remove outdated ``--docker`` completion entries: fedora30, fedora31, ubuntu1604
- ansible-test - Remove outdated ``--remote`` completion entries: freebsd/11.1, freebsd/12.1, osx/10.11, macos/10.15, rhel/7.6, rhel/7.8, rhel/8.1, rhel/8.2
- ansible-test - Remove outdated ``--windows`` completion entries: 2008, 2008-R2
- ansible-test - Remove the discontinued ``us-east-2`` choice from the ``--remote-aws-region`` option.
- ansible-test - Remove unused ``--remote`` completion entry: power/centos/7
- ansible-test - Removed ``pip`` constraints related to integration tests that have been moved to collections. This should reduce conflicts with ``pip`` requirements and constraints when testing collections.
- ansible-test - Removed the obsolete ``--remote-aws-region`` provisioning option.
- ansible-test - Removed the obsolete ``tower`` test plugin for testing Tower modules.
- ansible-test - Removed unused provisioning code and cleaned up remote provider management logic.
- ansible-test - Rename internal functions to match associated constant names that were previously updated.
- ansible-test - Reorganize internal ``pylint`` configuration files for easier comparison and maintenance.
- ansible-test - Report the correct line number in the ``yamllint`` sanity test when reporting ``libyaml`` parse errors in module documentation.
- ansible-test - Request remote resources by provider name for all provider types.
- ansible-test - Show a warning when the obsolete ``--remote-aws-region`` option is used.
- ansible-test - Silence ``pip`` warnings about Python 3.5 being EOL when installing requirements.
- ansible-test - Support custom remote endpoints with the ``--remote-endpoint`` option.
- ansible-test - The ``--remote`` option no longer pre-installs the ``virtualenv`` module on Python 3.x instances. The Python built-in ``venv`` module should be used instead.
- ansible-test - The ``default`` container for both collections and core have been updated to versions 2.11.0 and 1.9.0 respectively.
- ansible-test - The ``pylint`` sanity test is now skipped with a warning on Python 3.9 due to unresolved upstream regressions.
- ansible-test - The ``pylint`` sanity test is now supported on Python 3.8.
- ansible-test - The ``rstcheck`` sanity test is no longer used for collections, but continues to be used for ansible-core.
- ansible-test - The generated ``resource_prefix`` variable now meets the host name syntax requirements specified in RFC 1123 and RFC 952. The value used for local tests now places the random number before the hostname component, rather than after. If the resulting value is too long, it will be truncated.
- ansible-test - Ubuntu containers as well as ``default-test-container`` and ``ansible-base-test-container`` are now slightly smaller due to apt cleanup (https://github.com/ansible/distro-test-containers/pull/46).
- ansible-test - Update ``pylint`` and its dependencies to the latest available versions to support Python 3.9.
- ansible-test - Update built-in service endpoints for the ``--remote`` option.
- ansible-test - Update distribution test containers from version 2.0.1 to 2.0.2.
- ansible-test - Update the Ansible Core and Ansible Collection default test containers to 3.2.0 and 3.2.2 respectively.
- ansible-test - Updated the default test containers to version 3.1.0.
- ansible-test - Upgrade ansible-runner version used in compatibility tests, remove some tasks that were only needed with older versions, and skip in python2 because ansible-runner is soon dropping it.
- ansible-test - Use new endpoint for Parallels based instances with the ``--remote`` option.
- ansible-test - ``default-test-container`` and ``ansible-base-test-container`` now use Python 3.9.0 instead of 3.9.0rc1.
- ansible-test - add https endpoint for ansible-test
- ansible-test - add macOS 11.1 as a remote target (https://github.com/ansible/ansible/pull/72622)
- ansible-test - add the collection plugin directories ``plugin_utils`` and ``sub_plugins`` to list of plugin types. This ensures such plugins are tested for the ``import`` sanity test (https://github.com/ansible/ansible/pull/73599).
- ansible-test - centos6 end of life - container image updated to point to vault base repository (https://github.com/ansible/distro-test-containers/pull/54)
- ansible-test - centos6 image now has multiple fallback yum repositories for CentOS Vault.
- ansible-test - default container now uses default-test-container 2.7.0 and ansible-base-test-container 1.6.0. This brings in Python 3.9.0rc1 for testing.
- ansible-test - now makes a better attempt to support podman when calling ``docker images`` and asking for JSON format.
- ansible-test - python-cryptography is now bounded at <3.2, as 3.2 drops support for OpenSSL 1.0.2 upon which some of our CI infrastructure still depends.
- ansible-test - remote macOS instances no longer install ``virtualenv`` during provisioning
- ansible-test - the ACME test container was updated, it now supports external account creation and has a basic OCSP responder (https://github.com/ansible/ansible/pull/71097, https://github.com/ansible/acme-test-container/releases/tag/2.0.0).
- ansible-test - the ``import`` sanity test now also tries to import all non-module and non-module_utils Python files in ``lib/ansible/`` resp. ``plugins/`` (https://github.com/ansible/ansible/pull/72497).
- ansible-test - virtualenv helper scripts now prefer ``venv`` on Python 3 over ``virtualenv``
- ansible-test Now supports RHEL 8.3
- ansible-test pylint - ensure that removal collection version numbers conform to the semantic versioning specification at https://semver.org/ (https://github.com/ansible/ansible/pull/71679).
- ansible-test pylint sanity test - stop ignoring ``used-before-assignment`` errors (https://github.com/ansible/ansible/pull/73639).
- ansible-test runtime-metadata - compare deprecation and tombstone versions to the current version to ensure that they are correct (https://github.com/ansible/ansible/pull/72625).
- ansible-test runtime-metadata - ensure that removal collection version numbers conform to the semantic versioning specification at https://semver.org/ (https://github.com/ansible/ansible/pull/71679).
- ansible-test runtime-metadata - ensure that the tombstone removal date is not in the future (https://github.com/ansible/ansible/pull/72625).
- ansible-test runtime-metadata - validate removal version numbers, and check removal dates more strictly (https://github.com/ansible/ansible/pull/71679).
- ansible-test validate-modules - ensure that removal collection version numbers and version_added collection version numbers conform to the semantic versioning specification at https://semver.org/ (https://github.com/ansible/ansible/pull/71679).
- ansible-test validate-modules - no longer assume that ``default`` for ``type=bool`` options is ``false``, as the default is ``none`` and for some modules, ``none`` and ``false`` mean different things (https://github.com/ansible/ansible/issues/69561).
- ansible-test validate-modules - option names that seem to indicate they contain secret information that should be marked ``no_log=True`` are now flagged in the validate-modules sanity test. False positives can be marked by explicitly setting ``no_log=False`` for these options in the argument spec. Please note that many false positives are expected; the assumption is that it is by far better to have false positives than false negatives (https://github.com/ansible/ansible/pull/73508).
- ansible-test validate-modules - validate removal version numbers (https://github.com/ansible/ansible/pull/71679).
- ansible.utils.encrypt now returns `AnsibleError` instead of crypt.crypt's `OSError` on Python 3.9
- apt - module now works under any supported Python interpreter
- apt_repository - module now works under any supported Python interpreter
- callback plugins - ``meta`` tasks now get sent to ``v2_playbook_on_task_start``. Explicit tasks are always sent. Plugins can opt in to receiving implicit ones.
- callbacks - Add feature allowing forks to send callback events (https://github.com/ansible/ansible/issues/14681)
- conditionals - change the default of CONDITIONAL_BARE_VARS to False (https://github.com/ansible/ansible/issues/70682).
- config - more types are now automatically coerced to string when ``type: str`` is used and the value is parsed as a different type
- constructed - Add a toggle to allow the separator to be omitted if no prefix has been provided.
- constructed inventory plugin - Sanitize group names created from the ``groups`` option silently.
- create ``get_type_validator`` standalone function and move that functionality out of ``AnsibleModule`` (https://github.com/ansible/ansible/pull/72667)
- create ``get_unsupported_parameters`` validation function (https://github.com/ansible/ansible/pull/72447/files)
- debconf - add a note about no_log=True since module might expose sensitive information to logs (https://github.com/ansible/ansible/issues/32386).
- default callback - add ``show_task_path_on_failure`` option to display file and line number of tasks only on failed tasks when running at normal verbosity level (https://github.com/ansible/ansible/issues/64625)
- default callback - task name is now shown for ``include_tasks`` when using the ``free`` strategy (https://github.com/ansible/ansible/issues/71277).
- default callback - task name is now shown for ``include_tasks`` when using the ``linear`` strategy with ``ANSIBLE_DISPLAY_SKIPPED_HOSTS=0``.
- default_callback - moving 'check_mode_markers' documentation in default_callback doc_fragment (https://github.com/ansible-collections/community.general/issues/565).
- distribution - add facts about Amazon Linux Distribution facts (https://github.com/ansible/ansible/issues/73742).
- distribution - add support for DragonFly distribution (https://github.com/ansible/ansible/issues/43739).
- distribution - added distribution fact and hostname support for Parrot OS (https://github.com/ansible/ansible/pull/69158).
- distribution - handle NetBSD OS Family (https://github.com/ansible/ansible/issues/43739).
- distribution facts - ``distribution_release`` is now ``"Stream"`` on CentOS Stream (https://github.com/ansible/ansible/issues/73027).
- dnf - Add nobest option (https://github.com/ansible/ansible/issues/69983)
- dnf - When ``state: absent``, package names are now matched similarly to how the ``dnf`` CLI matches them (https://github.com/ansible/ansible/issues/72809).
- dnf - module now works under any supported Python interpreter
- dnf - now shows specific package changes (installations/removals) under ``results`` in check_mode. (https://github.com/ansible/ansible/issues/66132)
- facts - ``/dev/kvm`` is now consulted in Linux virtualization facts, and the host is considered a KVM host if this file exists and none of the pre-existing checks matched.
- facts - add new fact ``date_time['tz_dst']``, which returns the daylight saving timezone (https://github.com/ansible/ansible/issues/69004).
- facts - add uptime to openbsd
- find module - Now has a ``read_whole_file`` boolean parameter which allows for reading the whole file and doing an ``re.search()`` regex evaluation on it when searching using the ``contains`` option. This allows (for example) for ensuring the very end of the file matches a pattern.
- galaxy - add documentation about galaxy parameters in examples/ansible.cfg (https://github.com/ansible/ansible/issues/68402).
- galaxy - handle token as dict while loading from yaml file (https://github.com/ansible/ansible/issues/70887).
- get_url - allow checksum urls to point to file:// resources, moving scheme test to function
- get_url - handle same SHA sum for checksum file (https://github.com/ansible/ansible/issues/71420).
- git - add ``single_branch`` parameter (https://github.com/ansible/ansible/pull/28465)
- hash filter - fail when unsupported hash type is passed as an argument (https://github.com/ansible/ansible/issues/70258)
- inventory cache - do not show a warning when the cache file does not (yet) exist.
- iptables - add a note about ipv6-icmp in protocol parameter (https://github.com/ansible/ansible/issues/70905).
- iptables - fixed get_chain_policy API (https://github.com/ansible/ansible/issues/68612).
- iptables - reorder comment postition to be at the end (https://github.com/ansible/ansible/issues/71444).
- lineinfile - add search_string parameter for non-regexp searching (https://github.com/ansible/ansible/issues/70470)
- linux facts - Add additional check to ensure 'container' virtual fact gets added to guest_tech when appropriate (https://github.com/ansible/ansible/pull/71385)
- meta - now include a ``skip_reason`` when skipped (https://github.com/ansible/ansible/pull/71355).
- module payload builder - module_utils imports in any nested block (eg, ``try``, ``if``) are treated as optional during module payload builds; this allows modules to implement runtime fallback behavior for module_utils that do not exist in older versions of Ansible.
- module_utils - ``get_file_attributes()`` now takes an optional ``include_version`` boolean parameter. When ``True`` (default), the file's version/generation number is included in the result (but requires ``lsattr -v`` to work on the target platform).
- now !unsafe works on all types of data, not just strings, even recursively for mappings and sequences.
- package_facts - module support for apt and rpm now works under any supported Python interpreter
- pipe lookup - update docs for Popen with shell=True usages (https://github.com/ansible/ansible/issues/70159).
- plugin examples - Allow non-YAML examples, so that examples for plugins like the INI and TOML inventory plugins can be directly represented (https://github.com/ansible/ansible/pull/71184)
- plugin option validation - now the option type ``dict``/``dictionary`` is also validated by the config manager (https://github.com/ansible/ansible/pull/71928).
- reboot - add ``reboot_command`` parameter to allow specifying the command used to reboot the system (https://github.com/ansible/ansible/issues/51359)
- remove ``excommunicate`` debug command from AnsiballZ
- selinux - return selinux_getpolicytype facts correctly.
- service_facts - return service state information on AIX.
- service_facts - return service state information on OpenBSD.
- setup - allow list of filters (https://github.com/ansible/ansible/pull/68551).
- setup - fix distribution facts for Older Amazon Linux with ``/etc/os-release`` (https://github.com/ansible/ansible/issues/73946).
- setup.py - Declare that Python 3.9 is now supported (https://github.com/ansible/ansible/pull/72861).
- setup.py - Skip doing conflict checks for ``sdist`` and ``egg_info`` commands (https://github.com/ansible/ansible/pull/71310)
- subelements - clarify the lookup plugin documentation for parameter handling (https://github.com/ansible/ansible/issues/38182).
- subversion - ``validate_certs`` option, which, when true, will avoid passing ``--trust-server-cert`` to ``svn`` commands (https://github.com/ansible/ansible/issues/22599).
- unarchive - Add support for .tar.zst (zstd compression) (https://github.com/ansible/ansible/pull/73265).
- unarchive - add ``RETURN`` documentation (https://github.com/ansible/ansible/issues/67445).
- unarchive - add ``include`` parameter to allow extracting specific files from an archive (https://github.com/ansible/ansible/pull/40522)
- update sphinx to 2.1.2 and rstcheck to 3.3.1 for building documentation.
- uri - add ``ca_path`` argument to allow specification of a CA certificate (https://github.com/ansible/ansible/pull/71979).
- user - add new parameters ``password_expire_max`` and ``password_expire_min`` for controlling password expiration (https://github.com/ansible/ansible/issues/68775)
- varnames lookup plugin - Fixed grammar error in exception message when the plugin is given a non-string term.
- vault - Provide better error for single value encrypted values to indicate the file, line, and column of the errant vault (https://github.com/ansible/ansible/issues/72276)
- version test - Add semantic version functionality
- virtual facts - containerd cgroup is now recognized as container tech (https://github.com/ansible/ansible/issues/66304).
- virtualization facts - Detect ``vdsmd`` in addition to ``vdsm`` when trying to detect RHEV hosts. (https://github.com/ansible/ansible/issues/66147)
- winrm - Added ``ansible_winrm_kinit_args`` that can be used to control the args that are sent to the ``kinit`` call for Kerberos authentication.
- yum - module now works under any supported Python interpreter
- yum_repository - added boolean option module_hotfixes which allows to enable functionality for dnf.

amazon.aws
~~~~~~~~~~

- AWS inventory plugins - use shared HAS_BOTO3 helper rather than copying code (https://github.com/ansible-collections/amazon.aws/pull/288).
- AWS lookup plugins - use shared HAS_BOTO3 helper rather than copying code (https://github.com/ansible-collections/amazon.aws/pull/288).
- aws_account_attribute - add retries on common AWS failures (https://github.com/ansible-collections/amazon.aws/pull/295).
- aws_ec2 - Add hostname options concatenation
- aws_ec2 inventory - expose a new configuration key ``use_contrib_script_compatible_ec2_tag_keys`` to reproduce a behavior of the old ``ec2.py`` inventory script. With this option enabled, each tag is exposed using a ``ec2_tag_TAGNAME`` key (https://github.com/ansible-collections/amazon.aws/pull/331).
- aws_ec2 inventory - expose to new keys called ``include_filters`` and ``exclude_filters`` to give the user the ability to compose an inventory with multiple queries (https://github.com/ansible-collections/amazon.aws/pull/328).
- aws_ec2 inventory plugin - Added support for using Jinja2 templates in the authentication fields (https://github.com/ansible-collections/amazon.aws/pull/57).
- aws_ec2 inventory plugin - avoid a superfluous import of ``ansible.utils.display.Display`` (https://github.com/ansible-collections/amazon.aws/pull/226).
- aws_ec2 module - Replace inverse aws instance-state-name filters !terminated, !shutting-down in favor of postive filters pending, running, stopping, stopped. Issue 235. (https://github.com/ansible-collections/amazon.aws/pull/237)
- aws_secret - add ``bypath`` functionality (https://github.com/ansible-collections/amazon.aws/pull/192).
- cloudformation - added support for StackPolicyDuringUpdateBody (https://github.com/ansible-collections/amazon.aws/pull/155).
- ec2_key - add AWSRetry decorator to automatically retry on common temporary failures (https://github.com/ansible-collections/amazon.aws/pull/213).
- ec2_metadata_facts - add support for IMDSv2 (https://github.com/ansible-collections/amazon.aws/pull/43).
- ec2_snapshot_info - add the ``max_results`` along with ``next_token_id`` option (https://github.com/ansible-collections/amazon.aws/pull/321).
- ec2_tag - use common code for tagging resources (https://github.com/ansible-collections/amazon.aws/pull/309).
- ec2_tag_info - use common code for tagging resources (https://github.com/ansible-collections/amazon.aws/pull/309).
- ec2_vol - Add support for gp3 volumes and support for modifying existing volumes (https://github.com/ansible-collections/amazon.aws/issues/55).
- ec2_vol - add the ``purge_tags`` option (https://github.com/ansible-collections/amazon.aws/pull/242).
- ec2_vol - use common code for tagging resources (https://github.com/ansible-collections/amazon.aws/pull/309).
- ec2_vpc_net - use a custom waiter which can handle API rate limiting (https://github.com/ansible-collections/amazon.aws/pull/270).
- ec2_vpc_subnet - use AWSRetry decorator to more consistently handle API rate limiting (https://github.com/ansible-collections/amazon.aws/pull/270).
- ec2_vpc_subnet - use common code for tagging resources (https://github.com/ansible-collections/amazon.aws/pull/309).
- module_utils - the ipaddress module utility has been vendored into this collection.  This eliminates the collection dependency on ansible.netcommon (which had removed the library in its 2.0 release).  The ipaddress library is provided for internal use in this collection only. (https://github.com/ansible-collections/amazon.aws/issues/273)-
- module_utils.cloudfront_facts - linting cleanup (https://github.com/ansible-collections/amazon.aws/pull/291).
- module_utils.ec2 - linting cleanup (https://github.com/ansible-collections/amazon.aws/pull/291).
- module_utils/core - add a helper function ``normalize_boto3_result`` (https://github.com/ansible-collections/amazon.aws/pull/271).
- module_utils/core - add parameter ``descend_into_lists`` to ``scrub_none_parameters`` helper function (https://github.com/ansible-collections/amazon.aws/pull/262).
- module_utils/ec2 - added additional helper functions for tagging EC2 resources (https://github.com/ansible-collections/amazon.aws/pull/309).
- module_utils/elbv2 - add logic to compare_rules to suit Values list nested within dicts unique to each field type. Fixes issue (https://github.com/ansible-collections/amazon.aws/issues/187)
- sanity tests - add ignore.txt for 2.12 (https://github.com/ansible-collections/amazon.aws/pull/315).
- various AWS plugins and module_utils - Cleanup unused imports (https://github.com/ansible-collections/amazon.aws/pull/217).

ansible.netcommon
~~~~~~~~~~~~~~~~~

- Add SCP support when using ssh_type libssh
- Add `single_user_mode` option for command output caching.
- Move cli_config idempotent warning message with the task response under `warnings` key if `changed` is `True`
- Reduce CPU usage and network module run time when using `ansible_network_import_modules`
- Several module_utils files were intended to be licensed BSD, but missing a license preamble in the files. The preamble has been added, and all authors for the files have given their assent to the intended license https://github.com/ansible-collections/ansible.netcommon/pull/122
- Support any() and all() filters in Jinja2.

ansible.posix
~~~~~~~~~~~~~

- firewalld - bring the ``target`` feature back (https://github.com/ansible-collections/ansible.posix/issues/112).
- fix sanity test for various modules.
- synchronize - add the ``ssh_connection_multiplexing`` option to allow SSH connection multiplexing (https://github.com/ansible/ansible/issues/24365).

ansible.utils
~~~~~~~~~~~~~

- Add from_xml and to_xml fiter plugin (https://github.com/ansible-collections/ansible.utils/pull/56).

ansible.windows
~~~~~~~~~~~~~~~

- setup - Added more virtualization types to the virtual facts based on the Linux setup module
- win_certificate_store - Added functionality to open the store for a service account using ``store_type=service store_location=<service name>``
- win_user - Support specifying groups using the SecurityIdentifier - https://github.com/ansible-collections/ansible.windows/issues/153

arista.eos
~~~~~~~~~~

- Add eos_route_maps resource module.
- Add support for available_network_resources key, which allows to fetch the available resources for a platform (https://github.com/ansible-collections/arista.eos/issues/184).
- Add support for configuration caching (single_user_mode).
- Add support for syntax changes in ospf bfd command in 4.23 (https://github.com/ansible-collections/arista.eos/pull/134/)
- Move eos_config idempotent warning message with the task response under `warnings` key if `changed` is `True`
- Re-use device_info dictionary in cliconf

chocolatey.chocolatey
~~~~~~~~~~~~~~~~~~~~~

- win_chocolatey - Support for removing dependencies added with remove_dependencies option.

cisco.asa
~~~~~~~~~

- Add ignore-2.12.txt (https://github.com/ansible-collections/cisco.asa/pull/102).
- Adds support for single_user_mode command output caching. (https://github.com/ansible-collections/cisco.ios/pull/204).
- Remove tests/sanity/requirements.txt (https://github.com/ansible-collections/cisco.asa/pull/94).

cisco.ios
~~~~~~~~~

- Add ios_bgp_address_family Resource Module. (https://github.com/ansible-collections/cisco.ios/pull/219).
- Adds support for `single_user_mode` command output caching. (https://github.com/ansible-collections/cisco.ios/pull/204).
- Remove tests/sanity/requirements.txt (https://github.com/ansible-collections/cisco.ios/pull/261).

cisco.iosxr
~~~~~~~~~~~

- Add iosxr_bgp_address_family resource module (https://github.com/ansible-collections/cisco.iosxr/pull/105.).
- Add iosxr_bgp_global resource module (https://github.com/ansible-collections/cisco.iosxr/pull/101.).
- Add iosxr_bgp_neighbor_address_family resource module (https://github.com/ansible-collections/cisco.iosxr/pull/107.).
- Add missing examples for bgp_address_family module.
- Add support for available_network_resources key, which allows to fetch the available resources for a platform (https://github.com/ansible-collections/cisco.iosxr/issues/119).
- Add support for single_user_mode.
- Fix integration testcases for bgp_address_family and bgp_neighbor_address_family.
- Fix issue in delete state in bgp_address_family (https://github.com/ansible-collections/cisco.iosxr/pull/109).
- Move iosxr_config idempotent warning message with the task response under `warnings` key if `changed` is `True`
- Re-use device_info dict instead of building it every time.
- Update psudo-atomic operation scenario tests with correct assertion.

cisco.nxos
~~~~~~~~~~

- Add bfd option for neighbors (https://github.com/ansible-collections/cisco.nxos/issues/241).
- Add hello_interval_ms option in nxos_pim_interface module to support sub-second intervals (https://github.com/ansible-collections/cisco.nxos/issues/226).
- Add nxos_bgp_address_family Resource Module.
- Add nxos_bgp_neighbor_address_family Resource Module.
- Add nxos_route_maps resource module.
- Add support df_bit and size option for nxos_ping (https://github.com/ansible-collections/cisco.nxos/pull/237).
- Add support for ansible_network_resources key allows to fetch the available resources for a platform (https://github.com/ansible-collections/cisco.nxos/issues/268).
- Add support for state purged in nxos_interfaces.
- Adds support for `single_user_mode` command output caching.
- Move nxos_config idempotent warning message with the task response under `warnings` key if `changed` is `True`

cloudscale_ch.cloud
~~~~~~~~~~~~~~~~~~~

- Add interface parameter to server module (https://github.com/cloudscale-ch/ansible-collection-cloudscale/pull/54).
- Rename server_uuids parameter to servers in volume module (https://github.com/cloudscale-ch/ansible-collection-cloudscale/pull/54).

community.aws
~~~~~~~~~~~~~

- aws_config_aggregator - Fix typos in attribute names (https://github.com/ansible-collections/community.aws/pull/553).
- aws_glue_connection - Added multple connection types (https://github.com/ansible-collections/community.aws/pull/503).
- aws_glue_connection - Added support for check mode (https://github.com/ansible-collections/community.aws/pull/503).
- aws_glue_job - added ``number_of_workers``, ``worker_type`` and ``glue_version`` attributes to the module (https://github.com/ansible-collections/community.aws/pull/370).
- aws_kms - add support for setting the deletion window using `pending_window` (PendingWindowInDays) (https://github.com/ansible-collections/community.aws/pull/200).
- aws_kms_info - Add ``key_id`` and ``alias`` parameters to support fetching a single key (https://github.com/ansible-collections/community.aws/pull/200).
- aws_region_info - Add retries on common AWS failures (https://github.com/ansible-collections/community.aws/pull/422).
- aws_s3_bucket_info - new module options ``name``, ``name_filter``, ``bucket_facts`` and ``transform_location`` (https://github.com/ansible-collections/community.aws/pull/260).
- aws_ssm connection plugin - add support for specifying a profile to be used when connecting (https://github.com/ansible-collections/community.aws/pull/278).
- aws_ssm_parameter_store - added tier parameter option (https://github.com/ansible/ansible/issues/59738).
- dynamodb_ttl - use ``botocore_at_least`` helper for checking the available botocore version (https://github.com/ansible-collections/community.aws/pull/280).
- ec2_asg module - add support for all mixed_instances_policy parameters (https://github.com/ansible-collections/community.aws/issues/231).
- ec2_asg_info - gather information about asg lifecycle hooks (https://github.com/ansible-collections/community.aws/pull/233).
- ec2_instance - add automatic retries on all paginated queries for temporary errors (https://github.com/ansible-collections/community.aws/pull/373).
- ec2_instance - migrate to shared implementation of get_ec2_security_group_ids_from_names. The module will now return an error if the subnet provided isn't in the requested VPC. (https://github.com/ansible-collections/community.aws/pull/214)
- ec2_instance - wait for new instances to return a status before attempting to set additional parameters (https://github.com/ansible-collections/community.aws/pull/533).
- ec2_instance_info - add retries on common AWS failures (https://github.com/ansible-collections/community.aws/pull/521).
- ec2_instance_info - added ``minimum_uptime`` option with alias ``uptime`` for filtering instances that have only been online for certain duration of time in minutes (https://github.com/ansible-collections/community.aws/pull/356).
- ec2_launch_template - Add retries on common AWS failures (https://github.com/ansible-collections/community.aws/pull/326).
- ec2_launch_template - added ``metadata_options`` parameter to support changing the IMDS configuration for instances (https://github.com/ansible-collections/community.aws/pull/322).
- ec2_metric_alarm - Added support for check mode (https://github.com/ansible-collections/community.aws/pull/470).
- ec2_metric_alarm - Made ``unit`` parameter optional (https://github.com/ansible-collections/community.aws/pull/470).
- ec2_vpc_egress_igw - Add retries on common AWS failures (https://github.com/ansible-collections/community.aws/pull/421).
- ec2_vpc_endpoint - Add retries on common AWS failures. (https://github.com/ansible-collections/community.aws/pull/473)
- ec2_vpc_endpoint - Added support for specifying ``vpc_endpoint_type`` (https://github.com/ansible-collections/community.aws/pull/460).
- ec2_vpc_endpoint - The module now supports tagging endpoints. (https://github.com/ansible-collections/community.aws/pull/473)
- ec2_vpc_endpoint - The module will now lookup existing endpoints and try to match on the provided parameters before creating a new endpoint for better idempotency.  (https://github.com/ansible-collections/community.aws/pull/473)
- ec2_vpc_endpoint_info - ensure paginated endpoint description is retried on common AWS failures (https://github.com/ansible-collections/community.aws/pull/537).
- ec2_vpc_endpoint_info - use boto3 paginator when fetching services (https://github.com/ansible-collections/community.aws/pull/537).
- ec2_vpc_endpoint_service_info - new module added for fetching information about available VPC endpoint services (https://github.com/ansible-collections/community.aws/pull/346).
- ec2_vpc_nacl - add support for IPv6 (https://github.com/ansible-collections/community.aws/pull/398).
- ec2_vpc_nat_gateway - add AWSRetry decorators to improve reliability (https://github.com/ansible-collections/community.aws/pull/427).
- ec2_vpc_nat_gateway - code cleaning (https://github.com/ansible-collections/community.aws/pull/445)
- ec2_vpc_nat_gateway - imporove documentation (https://github.com/ansible-collections/community.aws/pull/445)
- ec2_vpc_nat_gateway - improve error handling (https://github.com/ansible-collections/community.aws/pull/445)
- ec2_vpc_nat_gateway - use custom waiters to manage NAT gateways states (deleted and available) (https://github.com/ansible-collections/community.aws/pull/445)
- ec2_vpc_nat_gateway - use pagination on describe calls to ensure all results are fetched (https://github.com/ansible-collections/community.aws/pull/427).
- ec2_vpc_nat_gateway_info - Add paginator (https://github.com/ansible-collections/community.aws/pull/472).
- ec2_vpc_nat_gateway_info - Improve documentation (https://github.com/ansible-collections/community.aws/pull/472).
- ec2_vpc_nat_gateway_info - Improve error handling (https://github.com/ansible-collections/community.aws/pull/472)
- ec2_vpc_nat_gateway_info - Use normalize_boto3_result (https://github.com/ansible-collections/community.aws/pull/472)
- ec2_vpc_nat_gateway_info - solve RequestLimitExceeded error by adding retry decorator (https://github.com/ansible-collections/community.aws/pull/446)
- ec2_vpc_peer - More return info added, also simplified module code a bit and extended tests (https://github.com/ansible-collections/community.aws/pull/355)
- ec2_vpc_peer - add support for waiting on state changes (https://github.com/ansible-collections/community.aws/pull/501).
- ec2_vpc_peer - use ``botocore_at_least`` helper for checking the available botocore version (https://github.com/ansible-collections/community.aws/pull/280).
- ec2_vpc_peering_info - add ``vpc_peering_connections`` return value to be consistent with boto3 modules (https://github.com/ansible-collections/community.aws/pull/501).
- ec2_vpc_peering_info - add retries on common AWS failures (https://github.com/ansible-collections/community.aws/pull/536).
- ec2_vpc_route_table - add AWSRetry decorators to improve reliability (https://github.com/ansible-collections/community.aws/pull/442).
- ec2_vpc_route_table - add boto3 pagination for some searches (https://github.com/ansible-collections/community.aws/pull/442).
- ec2_vpc_route_table_info - migrate to boto3 (https://github.com/ansible-collections/community.aws/pull/442).
- ec2_vpc_vgw - Add automatic retries for recoverable errors (https://github.com/ansible-collections/community.aws/pull/162).
- ec2_vpc_vpn - Add automatic retries for recoverable errors (https://github.com/ansible-collections/community.aws/pull/162).
- ecs_service - Add ``platform_version`` parameter to ``ecs_service`` (https://github.com/ansible-collections/community.aws/pull/353).
- ecs_task - added ``assign_public_ip`` option for network_configuration (https://github.com/ansible-collections/community.aws/pull/395).
- ecs_task - use ``botocore_at_least`` helper for checking the available botocore version (https://github.com/ansible-collections/community.aws/pull/280).
- ecs_taskdefinition - Documentation improvement (https://github.com/ansible-collections/community.aws/issues/520)
- elasticache - Improve docs a little, add intgration tests (https://github.com/ansible-collections/community.aws/pull/410).
- elb_classic_info - If the provided load balancer doesn't exist, return an empty list instead of throwing an error. (https://github.com/ansible-collections/community.aws/pull/215).
- elb_target_group - Add elb target group attributes ``stickiness_app_cookie_name`` and ``stickiness_app_cookie_duration_seconds``. Also update docs for stickiness_type to mention application cookie (https://github.com/ansible-collections/community.aws/pull/548)
- iam - Make iam module more predictable when returning the ``user_name`` it creates or deletes (https://github.com/ansible-collections/community.aws/pull/369).
- iam_saml_federation - module now returns the state of the provider when no changes are made (https://github.com/ansible-collections/community.aws/pull/419).
- kinesis_stream - check_mode is now based on the live settings rather than comparisons with a hard coded/fake stream definition (https://github.com/ansible-collections/community.aws/pull/27).
- kinesis_stream - now returns changed more accurately (https://github.com/ansible-collections/community.aws/pull/27).
- kinesis_stream - now returns tags consistently (https://github.com/ansible-collections/community.aws/pull/27).
- kinesis_stream - return values are now the same format when working with both encrypted and un-encrypted streams (https://github.com/ansible-collections/community.aws/pull/27).
- lambda_alias - add retries on common AWS failures (https://github.com/ansible-collections/community.aws/pull/396).
- lambda_alias - use common helper functions to create AWS connections (https://github.com/ansible-collections/community.aws/pull/396).
- lambda_alias - use common helper functions to perform snake_case to CamelCase conversions (https://github.com/ansible-collections/community.aws/pull/396).
- rds_instance - new ``purge_security_groups`` parameter (https://github.com/ansible-collections/community.aws/issues/385).
- rds_param_group - Add AWSRetry (https://github.com/ansible-collections/community.aws/pull/532).
- rds_param_group - Fix integration tests (https://github.com/ansible-collections/community.aws/pull/532).
- rds_param_group - Support check_mode (https://github.com/ansible-collections/community.aws/pull/532).
- rds_snapshot - added to the aws module_defaults group (https://github.com/ansible-collections/community.aws/pull/515).
- route53 - fixes AWS API error when attempting to create Alias records (https://github.com/ansible-collections/community.aws/issues/434).
- route53 - migrated from boto to boto3 (https://github.com/ansible-collections/community.aws/pull/405).
- s3_lifecycle - Add a ``wait`` parameter to wait for changes to propagate after being set (https://github.com/ansible-collections/community.aws/pull/448).
- s3_lifecycle - Add retries on common AWS failures (https://github.com/ansible-collections/community.aws/pull/448).
- s3_lifecycle - Fix idempotency when using dates instead of days (https://github.com/ansible-collections/community.aws/pull/448).
- s3_logging - added support for check_mode (https://github.com/ansible-collections/community.aws/pull/447).
- s3_logging - migrated from boto to boto3 (https://github.com/ansible-collections/community.aws/pull/447).
- s3_sync - new ``storage_class`` feature allowing to specify the storage class when any object is added to an S3 bucket (https://github.com/ansible-collections/community.aws/issues/358).
- sanity tests - add ignore.txt for 2.12 (https://github.com/ansible-collections/community.aws/pull/527).
- state_machine_arn - return ``state_machine_arn`` when state is unchanged (https://github.com/ansible-collections/community.aws/pull/302).
- various community.aws modules - cleanup error handling to use ``is_boto3_error_code`` and ``is_boto3_error_message`` helpers (https://github.com/ansible-collections/community.aws/pull/268).
- various community.aws modules - cleanup of Python imports (https://github.com/ansible-collections/community.aws/pull/360).
- various community.aws modules - improve consistency of handling Boto3 exceptions (https://github.com/ansible-collections/community.aws/pull/268).
- various community.aws modules - migrate exception error message handling from fail_json to fail_json_aws (https://github.com/ansible-collections/community.aws/pull/361).

community.crypto
~~~~~~~~~~~~~~~~

- acme module_utils - the ``acme`` module_utils has been split up into several Python modules (https://github.com/ansible-collections/community.crypto/pull/184).
- acme_* modules - codebase refactor which should not be visible to end-users (https://github.com/ansible-collections/community.crypto/pull/184).
- acme_* modules - support account key passphrases for ``cryptography`` backend (https://github.com/ansible-collections/community.crypto/issues/197, https://github.com/ansible-collections/community.crypto/pull/207).
- acme_account_info - when ``retrieve_orders`` is not ``ignore`` and the ACME server allows to query orders, the new return value ``order_uris`` is always populated with a list of URIs (https://github.com/ansible-collections/community.crypto/pull/178).
- acme_certificate_revoke - support revoking by private keys that are passphrase protected for ``cryptography`` backend (https://github.com/ansible-collections/community.crypto/pull/207).
- acme_challenge_cert_helper - add ``private_key_passphrase`` parameter (https://github.com/ansible-collections/community.crypto/pull/207).
- luks_device - allow to specify sector size for LUKS2 containers with new ``sector_size`` parameter (https://github.com/ansible-collections/community.crypto/pull/193).

community.digitalocean
~~~~~~~~~~~~~~~~~~~~~~

- digital_ocean_block_storage - included ability to resize Block Storage Volumes (https://github.com/ansible-collections/community.digitalocean/issues/38).

community.docker
~~~~~~~~~~~~~~~~

- Add the ``use_ssh_client`` option to most docker modules and plugins (https://github.com/ansible-collections/community.docker/issues/108, https://github.com/ansible-collections/community.docker/pull/114).
- docker_container - add ``storage_opts`` option to specify storage options (https://github.com/ansible-collections/community.docker/issues/91, https://github.com/ansible-collections/community.docker/pull/93).
- docker_image - allows to specify platform to pull for ``source=pull`` with new option ``pull_platform`` (https://github.com/ansible-collections/community.docker/issues/79, https://github.com/ansible-collections/community.docker/pull/89).
- docker_image - properly support image IDs (hashes) for loading and tagging images (https://github.com/ansible-collections/community.docker/issues/86, https://github.com/ansible-collections/community.docker/pull/87).
- docker_swarm_service - adding support for maximum number of tasks per node (``replicas_max_per_node``) when running swarm service in replicated mode. Introduced in API 1.40 (https://github.com/ansible-collections/community.docker/issues/7, https://github.com/ansible-collections/community.docker/pull/92).
- docker_swarm_service - change ``publish.published_port`` option from mandatory to optional. Docker will assign random high port if not specified (https://github.com/ansible-collections/community.docker/issues/99).

community.general
~~~~~~~~~~~~~~~~~

- apache2_mod_proxy - refactored/cleaned-up part of the code (https://github.com/ansible-collections/community.general/pull/2142).
- archive - refactored some reused code out into a couple of functions (https://github.com/ansible-collections/community.general/pull/2061).
- atomic_container - using ``get_bin_path()`` before calling ``run_command()`` (https://github.com/ansible-collections/community.general/pull/2144).
- atomic_host - using ``get_bin_path()`` before calling ``run_command()`` (https://github.com/ansible-collections/community.general/pull/2144).
- atomic_image - using ``get_bin_path()`` before calling ``run_command()`` (https://github.com/ansible-collections/community.general/pull/2144).
- beadm - minor refactor converting multiple statements to a single list literal (https://github.com/ansible-collections/community.general/pull/2160).
- bitbucket_pipeline_variable - removed unreachable code (https://github.com/ansible-collections/community.general/pull/2157).
- bundler - elements of list parameters are now validated (https://github.com/ansible-collections/community.general/pull/1885).
- clc_* modules - elements of list parameters are now validated (https://github.com/ansible-collections/community.general/pull/1771).
- consul - elements of list parameters are now validated (https://github.com/ansible-collections/community.general/pull/1885).
- consul_acl - elements of list parameters are now validated (https://github.com/ansible-collections/community.general/pull/1885).
- consul_io inventory script - conf options - allow custom configuration options via env variables (https://github.com/ansible-collections/community.general/pull/620).
- consul_session - elements of list parameters are now validated (https://github.com/ansible-collections/community.general/pull/1885).
- cpanm - honor and install specified version when running in ``new`` mode; that feature is not available in ``compatibility`` mode (https://github.com/ansible-collections/community.general/issues/208).
- cpanm - rewritten using ``ModuleHelper`` (https://github.com/ansible-collections/community.general/pull/2218).
- csv module utils - new module_utils for shared functions between ``from_csv`` filter and ``read_csv`` module (https://github.com/ansible-collections/community.general/pull/2037).
- datadog_monitor - add missing monitor types ``query alert``, ``trace-analytics alert``, ``rum alert`` (https://github.com/ansible-collections/community.general/pull/1723).
- datadog_monitor - elements of list parameters are now validated (https://github.com/ansible-collections/community.general/pull/1885).
- dnsimple - add CAA records to the whitelist of valid record types (https://github.com/ansible-collections/community.general/pull/1814).
- dnsimple - elements of list parameters ``record_ids`` are now validated (https://github.com/ansible-collections/community.general/pull/1795).
- gitlab_deploy_key - when the given key title already exists but has a different public key, the public key will now be updated to given value (https://github.com/ansible-collections/community.general/pull/1661).
- gitlab_runner - elements of list parameters ``tag_list`` are now validated (https://github.com/ansible-collections/community.general/pull/1795).
- grove - the option ``message`` has been renamed to ``message_content``. The old name ``message`` is kept as an alias and will be removed for community.general 4.0.0. This was done because ``message`` is used internally by Ansible (https://github.com/ansible-collections/community.general/pull/1929).
- heroku_collaborator - elements of list parameters are now validated (https://github.com/ansible-collections/community.general/pull/1970).
- hiera lookup - minor refactor converting multiple statements to a single list literal (https://github.com/ansible-collections/community.general/pull/2160).
- homebrew_tap - add support to specify search path for ``brew`` executable (https://github.com/ansible-collections/community.general/issues/1702).
- ipa_config - add new options ``ipaconfigstring``, ``ipadefaultprimarygroup``, ``ipagroupsearchfields``, ``ipahomesrootdir``, ``ipabrkauthzdata``, ``ipamaxusernamelength``, ``ipapwdexpadvnotify``, ``ipasearchrecordslimit``, ``ipasearchtimelimit``, ``ipauserauthtype``, and ``ipausersearchfields`` (https://github.com/ansible-collections/community.general/pull/2116).
- ipa_sudorule - add support for setting sudo runasuser (https://github.com/ansible-collections/community.general/pull/2031).
- ipa_user - fix ``userauthtype`` option to take in list of strings for the multi-select field instead of single string (https://github.com/ansible-collections/community.general/pull/2174).
- ipwcli_dns - minor refactor converting multiple statements to a single list literal (https://github.com/ansible-collections/community.general/pull/2160).
- java_cert - change ``state: present`` to check certificates by hash, not just alias name (https://github.com/ansible/ansible/issues/43249).
- java_keystore - add options ``certificate_path`` and ``private_key_path``, mutually exclusive with ``certificate`` and ``private_key`` respectively, and targetting files on remote hosts rather than their contents on the controller. (https://github.com/ansible-collections/community.general/issues/1669).
- jenkins_job - add a ``validate_certs`` parameter that allows disabling TLS/SSL certificate validation (https://github.com/ansible-collections/community.general/issues/255).
- jira - added ``attach`` operation, which allows a user to attach a file to an issue (https://github.com/ansible-collections/community.general/pull/2192).
- jira - added parameter ``account_id`` for compatibility with recent versions of JIRA (https://github.com/ansible-collections/community.general/issues/818, https://github.com/ansible-collections/community.general/pull/1978).
- jira - revamped the module as a class using ``ModuleHelper`` (https://github.com/ansible-collections/community.general/pull/2208).
- keycloak_* modules - allow the keycloak modules to use a token for the authentication, the modules can take either a token or the credentials (https://github.com/ansible-collections/community.general/pull/2250).
- keycloak_client - elements of list parameters ``default_roles``, ``redirect_uris``, ``web_origins`` are now validated (https://github.com/ansible-collections/community.general/pull/1795).
- kibana_plugin - add parameter for passing ``--allow-root`` flag to kibana and kibana-plugin commands (https://github.com/ansible-collections/community.general/pull/2014).
- known_hosts module utils - minor refactor converting multiple statements to a single list literal (https://github.com/ansible-collections/community.general/pull/2160).
- librato_annotation - elements of list parameters ``links`` are now validated (https://github.com/ansible-collections/community.general/pull/1795).
- linode_v4 - add support for ``private_ip`` option (https://github.com/ansible-collections/community.general/pull/2249).
- linode_v4 - elements of list parameters are now validated (https://github.com/ansible-collections/community.general/pull/1970).
- lvol - added proper support for ``+-`` options when extending or reducing the logical volume (https://github.com/ansible-collections/community.general/issues/1988).
- lxd_container - ``client_key`` and ``client_cert`` are now of type ``path`` and no longer ``str``. A side effect is that certain expansions are made, like ``~`` is replaced by the user's home directory, and environment variables like ``$HOME`` or ``$TEMP`` are evaluated (https://github.com/ansible-collections/community.general/pull/1741).
- lxd_container - elements of list parameter ``profiles`` are now validated (https://github.com/ansible-collections/community.general/pull/1795).
- lxd_profile - ``client_key`` and ``client_cert`` are now of type ``path`` and no longer ``str``. A side effect is that certain expansions are made, like ``~`` is replaced by the user's home directory, and environment variables like ``$HOME`` or ``$TEMP`` are evaluated (https://github.com/ansible-collections/community.general/pull/1741).
- lxd_profile - added ``merge_profile`` parameter to merge configurations from the play to an existing profile (https://github.com/ansible-collections/community.general/pull/1813).
- mail - elements of list parameters ``to``, ``cc``, ``bcc``, ``attach``, ``headers`` are now validated (https://github.com/ansible-collections/community.general/pull/1795).
- manageiq_alert_profiles - elements of list parameters are now validated (https://github.com/ansible-collections/community.general/pull/1970).
- manageiq_policies - elements of list parameters are now validated (https://github.com/ansible-collections/community.general/pull/1970).
- manageiq_tags - elements of list parameters are now validated (https://github.com/ansible-collections/community.general/pull/1970).
- manageiq_tags and manageiq_policies - added new parameter ``resource_id``. This parameter can be used instead of parameter ``resource_name`` (https://github.com/ansible-collections/community.general/pull/719).
- module_helper module utils - ``CmdMixin.run_command()`` now accepts ``dict`` command arguments, providing the parameter and its value (https://github.com/ansible-collections/community.general/pull/1867).
- module_helper module utils - added management of facts and adhoc setting of the initial value for variables (https://github.com/ansible-collections/community.general/pull/2188).
- module_helper module utils - added mechanism to manage variables, providing automatic output of variables, change status and diff information (https://github.com/ansible-collections/community.general/pull/2162).
- na_ontap_gather_facts - elements of list parameters ``gather_subset`` are now validated (https://github.com/ansible-collections/community.general/pull/1795).
- nexmo - elements of list parameters ``dest`` are now validated (https://github.com/ansible-collections/community.general/pull/1795).
- nictagadm - minor refactor converting multiple statements to a single list literal (https://github.com/ansible-collections/community.general/pull/2160).
- nmcli - add ability to connect to a Wifi network and also to attach it to a master (bond) (https://github.com/ansible-collections/community.general/pull/2220).
- nmcli - do not set IP configuration on slave connection (https://github.com/ansible-collections/community.general/pull/2223).
- nmcli - don't restrict the ability to manually set the MAC address to the bridge (https://github.com/ansible-collections/community.general/pull/2224).
- npm - add ``no_bin_links`` option (https://github.com/ansible-collections/community.general/issues/2128).
- nsupdate - elements of list parameters ``value`` are now validated (https://github.com/ansible-collections/community.general/pull/1795).
- oci_vcn - ``api_user_key_file`` is now of type ``path`` and no longer ``str``. A side effect is that certain expansions are made, like ``~`` is replaced by the user's home directory, and environment variables like ``$HOME`` or ``$TEMP`` are evaluated (https://github.com/ansible-collections/community.general/pull/1741).
- omapi_host - elements of list parameters ``statements`` are now validated (https://github.com/ansible-collections/community.general/pull/1795).
- one_host - elements of list parameters are now validated (https://github.com/ansible-collections/community.general/pull/1970).
- one_image_info - elements of list parameters are now validated (https://github.com/ansible-collections/community.general/pull/1970).
- one_vm - elements of list parameters are now validated (https://github.com/ansible-collections/community.general/pull/1970).
- oneandone_firewall_policy - elements of list parameters are now validated (https://github.com/ansible-collections/community.general/pull/1885).
- oneandone_load_balancer - elements of list parameters are now validated (https://github.com/ansible-collections/community.general/pull/1885).
- oneandone_monitoring_policy - elements of list parameters are now validated (https://github.com/ansible-collections/community.general/pull/1885).
- oneandone_private_network - elements of list parameters are now validated (https://github.com/ansible-collections/community.general/pull/1885).
- oneandone_server - elements of list parameters are now validated (https://github.com/ansible-collections/community.general/pull/1885).
- onepassword_info - elements of list parameters ``search_terms`` are now validated (https://github.com/ansible-collections/community.general/pull/1795).
- oneview_datacenter_info - elements of list parameters are now validated (https://github.com/ansible-collections/community.general/pull/1970).
- oneview_enclosure_info - elements of list parameters are now validated (https://github.com/ansible-collections/community.general/pull/1970).
- oneview_ethernet_network_info - elements of list parameters are now validated (https://github.com/ansible-collections/community.general/pull/1970).
- oneview_network_set_info - elements of list parameters are now validated (https://github.com/ansible-collections/community.general/pull/1970).
- ovh_ip_failover - removed unreachable code (https://github.com/ansible-collections/community.general/pull/2157).
- packet_device - elements of list parameters ``device_ids``, ``hostnames`` are now validated (https://github.com/ansible-collections/community.general/pull/1795).
- pagerduty - elements of list parameters ``service`` are now validated (https://github.com/ansible-collections/community.general/pull/1795).
- pids - new options ``pattern`` and  `ignore_case`` for retrieving PIDs of processes matching a supplied pattern (https://github.com/ansible-collections/community.general/pull/2280).
- plugins/module_utils/oracle/oci_utils.py - elements of list parameter ``key_by`` are now validated (https://github.com/ansible-collections/community.general/pull/1795).
- profitbricks - elements of list parameters are now validated (https://github.com/ansible-collections/community.general/pull/1885).
- profitbricks_volume - elements of list parameters are now validated (https://github.com/ansible-collections/community.general/pull/1885).
- proxmox - added ``purge`` module parameter for use when deleting lxc's with HA options (https://github.com/ansible-collections/community.general/pull/2013).
- proxmox inventory plugin - added ``Constructable`` class to the inventory to provide options ``strict``, ``keyed_groups``, ``groups``, and ``compose`` (https://github.com/ansible-collections/community.general/pull/2180).
- proxmox inventory plugin - added ``proxmox_agent_interfaces`` fact describing network interfaces returned from a QEMU guest agent (https://github.com/ansible-collections/community.general/pull/2148).
- proxmox inventory plugin - added ``tags_parsed`` fact containing tags parsed as a list (https://github.com/ansible-collections/community.general/pull/1949).
- proxmox inventory plugin - allow to select whether ``ansible_host`` should be set for the proxmox nodes (https://github.com/ansible-collections/community.general/pull/2263).
- proxmox_kvm - added new module parameter ``tags`` for use with PVE 6+ (https://github.com/ansible-collections/community.general/pull/2000).
- proxmox_kvm module - actually implemented ``vmid`` and ``status`` return values. Updated documentation to reflect current situation (https://github.com/ansible-collections/community.general/issues/1410, https://github.com/ansible-collections/community.general/pull/1715).
- pubnub_blocks - elements of list parameters ``event_handlers`` are now validated (https://github.com/ansible-collections/community.general/pull/1795).
- rax - elements of list parameters are now validated (https://github.com/ansible-collections/community.general/pull/2006).
- rax_cdb_user - elements of list parameters are now validated (https://github.com/ansible-collections/community.general/pull/2006).
- rax_scaling_group - elements of list parameters are now validated (https://github.com/ansible-collections/community.general/pull/2006).
- read_csv - refactored read_csv module to use shared csv functions from csv module_utils (https://github.com/ansible-collections/community.general/pull/2037).
- redfish modules - explicitly setting lists' elements to ``str`` (https://github.com/ansible-collections/community.general/pull/1761).
- redfish_* modules, redfish_utils module utils - add support for Redfish session create, delete, and authenticate (https://github.com/ansible-collections/community.general/issues/1975).
- redfish_config - case insensitive search for situations where the hostname/FQDN case on iLO doesn't match variable's case (https://github.com/ansible-collections/community.general/pull/1744).
- redhat_subscription - elements of list parameters ``pool_ids``, ``addons`` are now validated (https://github.com/ansible-collections/community.general/pull/1795).
- rhevm - removed unreachable code (https://github.com/ansible-collections/community.general/pull/2157).
- rocketchat - elements of list parameters ``attachments`` are now validated (https://github.com/ansible-collections/community.general/pull/1795).
- scaleway_compute - elements of list parameters are now validated (https://github.com/ansible-collections/community.general/pull/1970).
- scaleway_lb - elements of list parameters are now validated (https://github.com/ansible-collections/community.general/pull/1970).
- sendgrid - elements of list parameters ``to_addresses``, ``cc``, ``bcc``, ``attachments`` are now validated (https://github.com/ansible-collections/community.general/pull/1795).
- sensu_check - elements of list parameters are now validated (https://github.com/ansible-collections/community.general/pull/1885).
- sensu_client - elements of list parameters are now validated (https://github.com/ansible-collections/community.general/pull/1885).
- sensu_handler - elements of list parameters are now validated (https://github.com/ansible-collections/community.general/pull/1885).
- sl_vm - elements of list parameters ``disks``, ``ssh_keys`` are now validated (https://github.com/ansible-collections/community.general/pull/1795).
- slack - elements of list parameters ``attachments`` are now validated (https://github.com/ansible-collections/community.general/pull/1795).
- smartos_image_info - minor refactor converting multiple statements to a single list literal (https://github.com/ansible-collections/community.general/pull/2160).
- snmp_facts - added parameters ``timeout`` and ``retries`` to module (https://github.com/ansible-collections/community.general/issues/980).
- statusio_maintenance - elements of list parameters ``components``, ``containers`` are now validated (https://github.com/ansible-collections/community.general/pull/1795).
- svr4pkg - minor refactor converting multiple statements to a single list literal (https://github.com/ansible-collections/community.general/pull/2160).
- terraform - add ``plugin_paths`` parameter which allows disabling Terraform from performing plugin discovery and auto-download (https://github.com/ansible-collections/community.general/pull/2308).
- timezone - add Gentoo and Alpine Linux support (https://github.com/ansible-collections/community.general/issues/781).
- twilio - elements of list parameters ``to_numbers`` are now validated (https://github.com/ansible-collections/community.general/pull/1795).
- udm_dns_zone - elements of list parameters ``nameserver``, ``interfaces``, and ``mx`` are now validated (https://github.com/ansible-collections/community.general/pull/2268).
- vdo - add ``force`` option (https://github.com/ansible-collections/community.general/issues/2101).
- vmadm - elements of list parameters ``disks``, ``nics``, ``resolvers``, ``filesystems`` are now validated (https://github.com/ansible-collections/community.general/pull/1795).
- webfaction_domain - elements of list parameters are now validated (https://github.com/ansible-collections/community.general/pull/1885).
- webfaction_site - elements of list parameters are now validated (https://github.com/ansible-collections/community.general/pull/1885).
- xattr - minor refactor converting multiple statements to a single list literal (https://github.com/ansible-collections/community.general/pull/2160).
- xfconf - added option ``disable_facts`` to disable facts and its associated deprecation warning (https://github.com/ansible-collections/community.general/issues/1475).
- xfconf - changed implementation to use ``ModuleHelper`` new features (https://github.com/ansible-collections/community.general/pull/2188).
- xml - elements of list parameters ``add_children``, ``set_children`` are now validated (https://github.com/ansible-collections/community.general/pull/1795).
- yum_versionlock - Do the lock/unlock concurrently to speed up (https://github.com/ansible-collections/community.general/pull/1912).
- zfs_facts - minor refactor converting multiple statements to a single list literal (https://github.com/ansible-collections/community.general/pull/2160).
- zpool_facts - minor refactor converting multiple statements to a single list literal (https://github.com/ansible-collections/community.general/pull/2160).

community.hashi_vault
~~~~~~~~~~~~~~~~~~~~~

- hashi_vault - add ``proxies`` option (https://github.com/ansible-collections/community.hashi_vault/pull/50).

community.kubernetes
~~~~~~~~~~~~~~~~~~~~

- Adjust the documentation to clarify the fact ``wait_condition.status`` is a string.
- Adjust the name of parameters of ``helm`` and ``helm_info`` to match the documentation. No playbook change required.
- The Helm modules (``helm``, ``helm_info``, ``helm_plugin``, ``helm_plugin_info``, ``helm_plugin_repository``) accept the K8S environment variables like the other modules of the collections.
- helm - add a ``skip_crds`` option to skip the installation of CRDs when installing or upgrading a chart (https://github.com/ansible-collections/community.kubernetes/issues/296).
- helm - add optional support for helm diff (https://github.com/ansible-collections/community.kubernetes/issues/248).
- helm_template - add helm_template module to support template functionality (https://github.com/ansible-collections/community.kubernetes/issues/367).
- k8s - add a ``delete_options`` parameter to control garbage collection behavior when deleting a resource (https://github.com/ansible-collections/community.kubernetes/issues/253).
- k8s - add an example for downloading manifest file and applying (https://github.com/ansible-collections/community.kubernetes/issues/352).
- k8s - check if kubeconfig file is located on remote node or on Ansible Controller (https://github.com/ansible-collections/community.kubernetes/issues/307).
- k8s - check if src file is located on remote node or on Ansible Controller (https://github.com/ansible-collections/community.kubernetes/issues/307).
- k8s_exec - add a note about required permissions for the module (https://github.com/ansible-collections/community.kubernetes/issues/339).
- k8s_info - add information about api_version while returning facts (https://github.com/ansible-collections/community.kubernetes/pull/308).
- runtime.yml - update minimum Ansible version required for Kubernetes collection (https://github.com/ansible-collections/community.kubernetes/issues/314).

community.mongodb
~~~~~~~~~~~~~~~~~

- 304 - Adds validate parameter to mongodb_status module.

community.mysql
~~~~~~~~~~~~~~~

- mysql module utils - change deprecated connection parameters ``passwd`` and ``db`` to ``password`` and ``database`` (https://github.com/ansible-collections/community.mysql/pull/116).
- mysql_collection - introduce codebabse split to handle divergences between MySQL and MariaDB (https://github.com/ansible-collections/community.mysql/pull/103).
- mysql_info - add `version.full` and `version.suffix` return values (https://github.com/ansible-collections/community.mysql/issues/114).
- mysql_replication - add alternative (``primary``) choices to the ``state`` option choices containing ``master`` (https://github.com/ansible-collections/community.mysql/pull/150).
- mysql_replication - add the ``Is_Primary`` and ``Is_Replica`` alternatives to the ``Is_Slave`` and ``Is_Master`` return values as a preparation for replacement in ``community.mysql`` 3.0.0 (https://github.com/ansible-collections/community.mysql/pull/147).
- mysql_replication - change ``master_`` options to ``primary_`` options, add aliases to keep compatibility (https://github.com/ansible-collections/community.mysql/pull/150).
- mysql_replication - deprecate offending terminology, add alternative choices to the ``mode`` option (https://github.com/ansible-collections/community.mysql/issues/78).
- mysql_user - deprecate the ``REQUIRESSL`` privilege (https://github.com/ansible-collections/community.mysql/issues/101).

community.network
~~~~~~~~~~~~~~~~~

- edgeos_config - match the space after ``set`` and ``delete`` commands (https://github.com/ansible-collections/community.network/pull/199).
- nclu - execute ``net commit description <description>`` only if changed ``net pending``'s diff field (https://github.com/ansible-collections/community.network/pull/219).

community.okd
~~~~~~~~~~~~~

- increase the kubernetes.core dependency version number (https://github.com/ansible-collections/community.okd/pull/71).
- restrict the version of kubernetes.core dependency (https://github.com/ansible-collections/community.okd/pull/66).

community.postgresql
~~~~~~~~~~~~~~~~~~~~

- postgresql_info - add the ``patch``, ``full``, and ``raw`` values of the ``version`` return value (https://github.com/ansible-collections/community.postgresql/pull/68).
- postgresql_ping - add the ``patch``, ``full``, and ``raw`` values of the ``server_version`` return value (https://github.com/ansible-collections/community.postgresql/pull/70).

community.vmware
~~~~~~~~~~~~~~~~

- Define sub-options of disk in argument_spec (https://github.com/ansible-collections/community.vmware/pull/640).
- vmware_guest - Remove unnecessary hardware version check (https://github.com/ansible-collections/community.vmware/issues/636).
- vmware_guest_instant_clone - supported esxi_hostname parameter as an alias (https://github.com/ansible-collections/community.vmware/pull/745).
- vmware_resource_pool - Add parent_resource_pool parameter which is mutually exclusive with cluster and esxi_hostname (https://github.com/ansible-collections/community.vmware/issues/717)
- vmware_vcenter_settings - supported the diff mode (https://github.com/ansible-collections/community.vmware/pull/641).
- vmware_vm_inventory - add an example of FQDN as hostname (https://github.com/ansible-collections/community.vmware/issues/678).
- vmware_vm_inventory - skip disconnected VMs.

community.windows
~~~~~~~~~~~~~~~~~

- Extend win_domain_computer adding managedBy parameter.

community.zabbix
~~~~~~~~~~~~~~~~

- zabbix_agent - added support for installations on arm64 systems (https://github.com/ansible-collections/community.zabbix/pull/320).
- zabbix_proxy - now supports configuring StatsAllowedIP (https://github.com/ansible-collections/community.zabbix/pull/337).
- zabbix_server - added support for installtions on arm64 systems (https://github.com/ansible-collections/community.zabbix/pull/320).
- zabbix_web - added support for installtions on arm64 systems (https://github.com/ansible-collections/community.zabbix/pull/320).

containers.podman
~~~~~~~~~~~~~~~~~

- Podman login module

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- ome_firmware_baseline - Allows to retrieve the device even if it not in the first 50 device IDs
- ome_template - Allows to deploy a template on device groups.

f5networks.f5_modules
~~~~~~~~~~~~~~~~~~~~~

- Add disable action and appropriate scenarios to bigip_policy_rule module
- Add ends_with_any condition to bigip_policy_rule module
- Add http_header condition type with header_is_any condition to bigip_policy_rule module
- Add insert action and appropriate scenarios to bigip_policy_rule module
- Add path_contains condition to bigip_policy_rule module
- Add path_is_any option to conditions in bigip_policy_rule module
- Add remove action and appropriate scenarios to bigip_policy_rule module
- Add replace action and appropriate scenarios to bigip_policy_rule module
- Add token refresh handling to bigiq local client
- Added requirement to install ipaddress package for python versions earlier than 3.5
- Event types are now supported with forward type action
- Event types are now supported with reset type action
- Policy support with condition type TCP match with any of address/datagroup

fortinet.fortios
~~~~~~~~~~~~~~~~

- fixed pylint testing errors.

hetzner.hcloud
~~~~~~~~~~~~~~

- Add firewalls to hcloud_server module
- hcloud_server - improve the handling of deprecated images
- hcloud_server - improve the validation and error response for not existing images
- inventory - support jinjia templating within `token`

junipernetworks.junos
~~~~~~~~~~~~~~~~~~~~~

- Add junos_bgp_address_family resource module.
- Add junos_routing_instances Resource Module.
- Add support df_bit and size option for junos_ping (https://github.com/ansible-collections/junipernetworks.junos/pull/136).
- Add support for autonomous-system routing-options for bgp global and updating tests and documentation.
- Add support for available_network_resources key, which allows to fetch the available resources for a platform (https://github.com/ansible-collections/junipernetworks.junos/issues/160).
- Add support for bgp group and neighbors in bgp_global resource module.
- Add support for configuration caching (single_user_mode).
- Re-use device_info dictionary in cliconf.
- Replace unsupported parameter `vlan-id` in junipernetworks.junos.junos_vlans module with `vlan_id`

kubernetes.core
~~~~~~~~~~~~~~~

- Adjust the documentation to clarify the fact ``wait_condition.status`` is a string.
- Adjust the name of parameters of ``helm`` and ``helm_info`` to match the documentation. No playbook change required.
- The Helm modules (``helm``, ``helm_info``, ``helm_plugin``, ``helm_plugin_info``, ``helm_plugin_repository``) accept the K8S environment variables like the other modules of the collections.
- helm - add a ``skip_crds`` option to skip the installation of CRDs when installing or upgrading a chart (https://github.com/ansible-collections/kubernetes.core/issues/296).
- helm - add optional support for helm diff (https://github.com/ansible-collections/kubernetes.core/issues/248).
- helm_template - add helm_template module to support template functionality (https://github.com/ansible-collections/kubernetes.core/issues/367).
- k8s - add a ``delete_options`` parameter to control garbage collection behavior when deleting a resource (https://github.com/ansible-collections/kubernetes.core/issues/253).
- k8s - add an example for downloading manifest file and applying (https://github.com/ansible-collections/kubernetes.core/issues/352).
- k8s - check if kubeconfig file is located on remote node or on Ansible Controller (https://github.com/ansible-collections/kubernetes.core/issues/307).
- k8s - check if src file is located on remote node or on Ansible Controller (https://github.com/ansible-collections/kubernetes.core/issues/307).
- k8s_exec - add a note about required permissions for the module (https://github.com/ansible-collections/kubernetes.core/issues/339).
- k8s_info - add information about api_version while returning facts (https://github.com/ansible-collections/kubernetes.core/pull/308).
- runtime.yml - update minimum Ansible version required for Kubernetes collection (https://github.com/ansible-collections/kubernetes.core/issues/314).

netapp.azure
~~~~~~~~~~~~

- azure_rm_netapp_account - new option ``active_directories`` to support SMB volumes.
- azure_rm_netapp_account - new option ``tags``.
- azure_rm_netapp_account - new suboptions ``ad_name``, ``kdc_ip``, ``service_root_ca_certificate``` for Active Directory.
- azure_rm_netapp_capacity_pool - Updated ANF capacity pool modify function for size parameter mandatory issue.
- azure_rm_netapp_capacity_pool - new option ``service_level``.
- azure_rm_netapp_capacity_pool - now allows modify for size.
- azure_rm_netapp_volume - enable changes in volume size.
- azure_rm_netapp_volume - new option ``protocol_types`` to support SMB volumes.
- azure_rm_netapp_volume - new option ``size``.
- azure_rm_netapp_volume - new option ``subnet_name`` as subnet_id is ambiguous.  subnet_id is now aliased to subnet_name.
- azure_rm_netapp_volume - new option ``vnet_resource_group_for_subnet``, resource group for virtual_network and subnet_id to be used.
- azure_rm_netapp_volume - now returns complete mount_path of the volume specified.
- azure_rm_netapp_volume - now returns mount_path of the volume specified.
- azure_rm_netapp_volume - rename msg to mount_path, as documented in RETURN.
- use a three group format for version_added. So 2.7 becomes 2.7.0. Same thing for 2.8 and 2.9.

netapp.cloudmanager
~~~~~~~~~~~~~~~~~~~

- na_cloudmanager_connector_aws - Return newly created Azure client ID in cloud manager, instance ID and account ID. New option ``proxy_certificates``.
- na_cloudmanager_cvo_aws - Return newly created AWS working_environment_id.
- na_cloudmanager_cvo_azure - Return newly created AZURE working_environment_id.
- na_cloudmanager_cvo_gcp - Return newly created GCP working_environment_id.

netapp.elementsw
~~~~~~~~~~~~~~~~

- na_elementsw_info - add ``cluster_nodes`` and ``cluster_drives``.
- na_elementsw_qos_policy - explicitly define ``minIOPS``, ``maxIOPS``, ``burstIOPS`` as int.

netapp.ontap
~~~~~~~~~~~~

- azure_rm_netapp_account - new option ``active_directories`` to support SMB volumes.
- azure_rm_netapp_volume - new option ``protocol_types`` to support SMB volumes.
- na_ontap_autosupport - new option ``local_collection_enabled`` to specify whether collection of AutoSupport data when the AutoSupport daemon is disabled.
- na_ontap_autosupport - new option ``max_http_size`` to specify delivery size limit for the HTTP transport protocol (in bytes).
- na_ontap_autosupport - new option ``max_smtp_size`` to specify delivery size limit for the SMTP transport protocol (in bytes).
- na_ontap_autosupport - new option ``nht_data_enabled`` to specify whether the disk health data is collected as part of the AutoSupport data.
- na_ontap_autosupport - new option ``ondemand_enabled`` to specify whether the AutoSupport OnDemand Download feature is enabled.
- na_ontap_autosupport - new option ``perf_data_enabled`` to specify whether the performance data is collected as part of the AutoSupport data.
- na_ontap_autosupport - new option ``private_data_removed`` to specify the removal of customer-supplied data.
- na_ontap_autosupport - new option ``reminder_enabled`` to specify whether AutoSupport reminders are enabled or disabled.
- na_ontap_autosupport - new option ``retry_count`` to specify the maximum number of delivery attempts for an AutoSupport message.
- na_ontap_autosupport - new option ``validate_digital_certificate`` which when set to true each node will validate the digital certificates that it receives.
- na_ontap_debug - improve error reporting for import errors on netapp_lib.
- na_ontap_flexcache - mount/unmount the FlexCache volume when using REST.
- na_ontap_flexcache - support REST APIs in addition to ZAPI for create and delete.
- na_ontap_flexcache - support for ``prepopulate`` option when using REST (requires ONTAP 9.8).
- na_ontap_igroup - added REST support for ONTAP igroup creation, modification, and deletion.
- na_ontap_igroups - new option ``igroups`` to support nested igroups (requires ONTAP 9.9).
- na_ontap_igroups - new option ``initiator_names`` as a replacement for ``initiators`` (still supported as an alias).
- na_ontap_igroups - new option ``initiator_objects`` to support initiator comments (requires ONTAP 9.9).
- na_ontap_info - Added "autosupport_check_info" to the attributes that will be collected when gathering info using the module.
- na_ontap_info - improve error reporting for import errors on netapp_lib, json, xlmtodict.
- na_ontap_lun - add ``comment`` option.
- na_ontap_lun - allow new LUNs to use different igroup or os_type when using SAN application.
- na_ontap_lun - convert existing LUNs and supporting volume to a smart container within a SAN application.
- na_ontap_lun - ignore small increase (lower than provisioned) and small decrease (< 10%) in ``total_size``.
- na_ontap_lun - new option ``qos_adaptive_policy_group``.
- na_ontap_lun - new option ``scope`` to explicitly force operations on the SAN application or a single LUN.
- na_ontap_motd - deprecated module warning and to use na_ontap_login_messages.
- na_ontap_node - added REST support for ONTAP node modify and rename.
- na_ontap_node - added modify function for location and asset tag for node.
- na_ontap_snapmirror - add new options ``source_endpoint`` and ``destination_endpoint`` to group endpoint suboptions.
- na_ontap_snapmirror - add new suboptions ``consistency_group_volumes`` and ``ipspace`` to endpoint options.
- na_ontap_snapmirror - deprecate older options for source and destination paths, volumes, vservers, and clusters.
- na_ontap_snapmirror - improve error reporting or warn when REST option is not supported.
- na_ontap_snapmirror - report warning when relationship is present but not healthy.
- na_ontap_volume - new suboption ``dr_cache`` when creating flexcache using NAS application template.
- na_ontap_volume - warn when attempting to modify application only options.
- na_ontap_volume_efficiency - new option 'start_ve_build_metadata' scan the entire and generate fingerprint database.
- na_ontap_volume_efficiency - new option 'start_ve_delete_checkpoint' delete checkpoint and start the operation from the begining.
- na_ontap_volume_efficiency - new option 'start_ve_qos_policy' defines the QoS policy for the operation.
- na_ontap_volume_efficiency - new option 'start_ve_queue_operation' queue if an exisitng operation is already running.
- na_ontap_volume_efficiency - new option 'start_ve_scan_all' scan the entire volume without applying share block optimization.
- na_ontap_volume_efficiency - new option 'start_ve_scan_old_data' scan the file system to process all the existing data.
- na_ontap_volume_efficiency - new option 'stop_ve_all_operations' all running and queued operations to be stopped.
- na_ontap_volume_efficiency - new option to allow volume efficiency to be started and stopped 'volume_efficiency'.
- na_ontap_volume_efficiency - to allow for FAS ONTAP systems to enable volume efficiency when it does not exist and apply additional parameters.
- na_ontap_volume_efficiency - to allow for FAS ONTAP systems to enable volume efficiency when it does not exist.

netapp.um_info
~~~~~~~~~~~~~~

- minor changes to meet Red Hat requirements to be certified.
- na_um_list_aggregates - Now sort by performance_capacity.used
- na_um_list_nodes - Now sort by performance_capacity.used

netapp_eseries.santricity
~~~~~~~~~~~~~~~~~~~~~~~~~

- Add IPv6 and FQDN support for NTP
- Add IPv6 support for DNS
- Add criteria_drive_max_size option to na_santricity_storagepool and nar_santricity_host role.
- Add resource-provisioned volumes option to globals and nar_santricity_management role.
- Added nvme4k as a drive type interface to the na_santricity_storagepool module.
- Added options for critical and warning threshold setting in na_santricity_storagepool module and nar_santricity_host role.
- Fix dynamic disk pool critical and warning threshold settings.
- Remove resource-provisioned volumes setting from na_santicity_global module and nar_santricity_management role."
- na_santricity_discover - Add support for discovering storage systems directly using devmgr/v2/storage-systems/1/about endpoint since its old method of discover is being deprecated.
- na_santricity_facts - Add storage system information to facilitate ``netapp_eseries.host`` collection various protocol configuration.
- na_santricity_server_certificate - New module to configure storage system's web server certificate configuration.
- na_santricity_snapshot - New module to configure NetApp E-Series Snapshot consistency groups any number of base volumes.
- na_santricity_volume - Add percentage size unit (pct) and which allows the creates volumes based on the total storage pool size.
- nar_santricity_host - Add eseries_storage_pool_configuration list options, criteria_volume_count, criteria_reserve_free_capacity_pct, and common_volume_host to facilitate volumes based on percentages of storage pool or volume group.
- nar_santricity_host - Add support for snapshot group creation.
- nar_santricity_host - Improve host mapping information discovery.
- nar_santricity_host - Improve storage system discovery related error messages.
- nar_santricity_management - Add support for server certificate management.

netbox.netbox
~~~~~~~~~~~~~

- Allow rack to be in query_param_ids [#443](https://github.com/netbox-community/ansible_modules/pull/443)
- Inventory - Added ansible_host_dns_name to set ansible_host to dns_name
- netbox_cable -  Add tags option [#455](https://github.com/netbox-community/ansible_modules/pull/455)
- netbox_cluster_type - Add description option [#451](https://github.com/netbox-community/ansible_modules/pull/451)
- netbox_device_role - Added description option
- netbox_ipam_role - Add description option [#451](https://github.com/netbox-community/ansible_modules/pull/451)
- netbox_manufacturer - Add description option [#451](https://github.com/netbox-community/ansible_modules/pull/451)
- netbox_platform -  Added description option
- netbox_rir - Add description option [#451](https://github.com/netbox-community/ansible_modules/pull/451)
- netbox_tenant_group - Add parent_tenant_group option [#460](https://github.com/netbox-community/ansible_modules/pull/460)

ngine_io.cloudstack
~~~~~~~~~~~~~~~~~~~

- cs_physical_network - Added VXLAN as an option of isolation methods (https://github.com/ngine-io/ansible-collection-cloudstack/pull/73).
- instance - New style inventory plugin implemented for instances (https://github.com/ngine-io/ansible-collection-cloudstack/pull/66)

openvswitch.openvswitch
~~~~~~~~~~~~~~~~~~~~~~~

- Allow setting multiple properties on a port (https://github.com/ansible-collections/openvswitch.openvswitch/issues/63).

ovirt.ovirt
~~~~~~~~~~~

- cluster_upgrade - Add correlation-id header (https://github.com/oVirt/ovirt-ansible-collection/pull/222).
- engine_setup - Add skip renew pki confirm (https://github.com/oVirt/ovirt-ansible-collection/pull/228).
- examples - Add recipe for removing DM device (https://github.com/oVirt/ovirt-ansible-collection/pull/233).
- hosted_engine_setup - Add an error message for FIPS on CentOS (https://github.com/oVirt/ovirt-ansible-collection/pull/250).
- hosted_engine_setup - Disable reboot_after_installation (https://github.com/oVirt/ovirt-ansible-collection/pull/218).
- hosted_engine_setup - Filter devices with unsupported bond mode (https://github.com/oVirt/ovirt-ansible-collection/pull/226).
- hosted_engine_setup - Fix the appliance distribution (https://github.com/oVirt/ovirt-ansible-collection/pull/249).
- infra - Add reboot host parameters (https://github.com/oVirt/ovirt-ansible-collection/pull/231).
- infra - remove target from ovirt_storage_connection (https://github.com/oVirt/ovirt-ansible-collection/pull/252).
- ovirt_disk - Add SATA support (https://github.com/oVirt/ovirt-ansible-collection/pull/225).
- ovirt_host - Add reboot_after_installation option (https://github.com/oVirt/ovirt-ansible-collection/pull/217).
- ovirt_user - Add ssh_public_key (https://github.com/oVirt/ovirt-ansible-collection/pull/232)
- ovirt_vm - Allow migration between clusters (https://github.com/oVirt/ovirt-ansible-collection/pull/236).
- repositories - Add host ppc (https://github.com/oVirt/ovirt-ansible-collection/pull/248).
- repositories - Remove ansible channels from RHV 4.4 (https://github.com/oVirt/ovirt-ansible-collection/pull/242).
- repositories - fix ppc repos (https://github.com/oVirt/ovirt-ansible-collection/pull/254).

purestorage.flasharray
~~~~~~~~~~~~~~~~~~~~~~

- purefa_certs - New module for managing SSL certificates
- purefa_connect - Add support for FC-based array replication
- purefa_ds - Add Purity v6 support for Directory Services, including Data DS and updating services
- purefa_info - Add support for FC Replication
- purefa_info - Add support for Remote Volume Snapshots
- purefa_info - Update directory_services dictionary to cater for FA-Files data DS. Change DS dict forward. Add deprecation warning.
- purefa_maintenance - New module to set maintenance windows
- purefa_ntp - Ignore NTP configuration for CBS-based arrays
- purefa_pg - Add support for Protection Groups in AC pods
- purefa_pg - Add support to rename protection groups
- purefa_snap - Add support for remote snapshot of individual volumes to offload targets
- purefa_syslog - Add support for naming SYSLOG servers for Purity//FA 6.1 or higher
- purefa_volume - New parameter pgroup to specify an existing protection group to put crwated volume(s) in.

purestorage.flashblade
~~~~~~~~~~~~~~~~~~~~~~

- purefa_virtualhost - New module to manage API Clients
- purefb_ad - New module to manage Active Directory Account
- purefb_certs - Add update functionality for array cert
- purefb_eula - New module to sign EULA
- purefb_fs - Add multiprotocol ACL support
- purefb_info - Add Active Directory, Kerberos and Object Store Account information
- purefb_info - Add extra info for Purity//FB 3.2+ systems
- purefb_info - Add information regarding filesystem multiprotocol (where available)
- purefb_info - Add new parameter to provide details on admin users
- purefb_info - Add replication performace statistics
- purefb_keytabs - New module to manage Kerberos Keytabs
- purefb_s3user - Add ability to remove an S3 users existing access key
- purefb_s3user - Add access policy option to user creation
- purefb_timeout - Add module to set GUI idle timeout
- purefb_userpolicy - New module to manage object store user access policies
- purefb_virtualhost - New module to manage Object Store Virtual Hosts

sensu.sensu_go
~~~~~~~~~~~~~~

- Add modules for managing Sensu Go clusters.
- Add modules for managing etcd replicatiors, which form the basis of the Sensu Go federation.
- Update list of available Sensu Go agent packages for Windows installations.

servicenow.servicenow
~~~~~~~~~~~~~~~~~~~~~

- standardized invocation output

theforeman.foreman
~~~~~~~~~~~~~~~~~~

- Add a role `activation_keys` to manage activation keys
- Add a role `lifecycle_environments` to manage lifecycle environments
- Add a role `repositories` to manage products, repositories, and repository_sets
- Add a role `sync_plans` to manage sync plans
- activation_key - add support for selecting subscriptions by ``upstream_pool_id``
- compute_resource - add ``set_console_password``, ``keyboard_layout`` and ``public_key`` parameters (https://github.com/theforeman/foreman-ansible-modules/issues/1052)
- host - clarify that ``owner`` refers to a users login, not their full name (https://github.com/theforeman/foreman-ansible-modules/issues/1045)
- host - look up the correct network id for a network given as part of ``interfaces_attributes`` (https://github.com/theforeman/foreman-ansible-modules/issues/1104)
- host, hostgroup - add ``activation_keys`` parameter to ease configuring activation keys for deploments

vyos.vyos
~~~~~~~~~

- Add regex for delete failures to terminal_stderr_re
- Add support for available_network_resources key, which allows to fetch the available resources for a platform (https://github.com/ansible-collections/vyos.vyos/issues/138).
- Add support for configuration caching (single_user_mode).
- Add vyos BGP address_family resource module (https://github.com/ansible-collections/vyos.vyos/pull/132).
- Add vyos BGP global resource module.(https://github.com/ansible-collections/vyos.vyos/pull/125).
- Enabled addition and parsing of wireguard interface.
- Re-use device_info dictionary in cliconf.

Breaking Changes / Porting Guide
--------------------------------

Ansible-core
~~~~~~~~~~~~

- Made SCM collections be reinstalled regardless of ``--force`` being present.
- NetBSD virtualization facts (specifically ``ansible_virtualization_type``) now returns a more accurate value by checking the value of the ``machdep.hypervisor`` ``sysctl`` key. This change is breaking because in some cases previously, we would erroneously report ``xen`` even when the target is not running on Xen. This prevents that behavior in most cases. (https://github.com/ansible/ansible/issues/69352)
- Replaced the in-tree dependency resolver with an external implementation that pip >= 20.3 uses now by default — ``resolvelib``. (https://github.com/ansible/ansible/issues/71784)
- The ``meta`` module now supports tags for user-defined tasks. Internal ``meta`` tasks continue to always run. (https://github.com/ansible/ansible/issues/64558)
- ansible-galaxy login command has been removed (see https://github.com/ansible/ansible/issues/71560)

ansible.netcommon
~~~~~~~~~~~~~~~~~

- Removed vendored ipaddress package from collection. If you use ansible_collections.ansible.netcommon.plugins.module_utils.compat.ipaddress in your collection, you will need to change this to import ipaddress instead. If your content using ipaddress supports Python 2.7, you will additionally need to make sure that the user has the ipaddress package installed. Please refer to https://docs.ansible.com/ansible/latest/dev_guide/developing_modules_best_practices.html#importing-and-using-shared-code to see how to safely import external packages that may be missing from the user's system A backport of ipaddress for Python 2.7 is available at https://pypi.org/project/ipaddress/

community.docker
~~~~~~~~~~~~~~~~

- docker_swarm - if ``join_token`` is specified, a returned join token with the same value will be replaced by ``VALUE_SPECIFIED_IN_NO_LOG_PARAMETER``. Make sure that you do not blindly use the join tokens from the return value of this module when the module is invoked with ``join_token`` specified! This breaking change appears in a minor release since it is necessary to fix a security issue (https://github.com/ansible-collections/community.docker/pull/103).

community.general
~~~~~~~~~~~~~~~~~

- If you use Ansible 2.9 and these plugins or modules from this collection, community.general 3.0.0 results in errors when trying to use the DellEMC content by FQCN, like ``community.general.idrac_firmware``.
  Since Ansible 2.9 is not able to use redirections, you will have to adjust your playbooks and roles manually to use the new FQCNs (``dellemc.openmanage.idrac_firmware`` for the previous example) and to make sure that you have ``dellemc.openmanage`` installed.

  If you use ansible-base 2.10 or newer and did not install Ansible 4.0.0, but installed (and/or upgraded) community.general manually, you need to make sure to also install the ``dellemc.openmanage`` collection if you are using any of these plugins or modules.
  While ansible-base 2.10 or newer can use the redirects that community.general 3.0.0 adds, the collection they point to (such as dellemc.openmanage) must be installed for them to work.
- gitlab_deploy_key - if for an already existing key title a different public key was given as parameter nothing happened, now this changed so that the public key is updated to the new value (https://github.com/ansible-collections/community.general/pull/1661).
- java_keystore - instead of failing, now overwrites keystore if the alias (name) is changed. This was originally the intended behavior, but did not work due to a logic error. Make sure that your playbooks and roles do not depend on the old behavior of failing instead of overwriting (https://github.com/ansible-collections/community.general/issues/1671).
- java_keystore - instead of failing, now overwrites keystore if the passphrase is changed. Make sure that your playbooks and roles do not depend on the old behavior of failing instead of overwriting (https://github.com/ansible-collections/community.general/issues/1671).
- one_image - use pyone instead of python-oca (https://github.com/ansible-collections/community.general/pull/2032).
- utm_proxy_auth_profile - the ``frontend_cookie_secret`` return value now contains a placeholder string instead of the module's ``frontend_cookie_secret`` parameter (https://github.com/ansible-collections/community.general/pull/1736).

fortinet.fortios
~~~~~~~~~~~~~~~~

- Generic FortiOS Module - FOS module to issue generic request with Ansible.
- Support for FOS Monitor API - several modules are new for monitor API.
- Unified Collection - The fortios collection itself will be adapting any FOS platforms.

servicenow.servicenow
~~~~~~~~~~~~~~~~~~~~~

- auth field now required for anything other than Basic authentication

theforeman.foreman
~~~~~~~~~~~~~~~~~~

- All role variables are now prefixed with ``foreman_`` to avoid clashes with similarly named variables from roles outside this collection.

Deprecated Features
-------------------

Ansible-core
~~~~~~~~~~~~

- Starting in 2.14, shell and command modules will no longer have the option to warn and suggest modules in lieu of commands. The ``warn`` parameter to these modules is now deprecated and defaults to ``False``. Similarly, the ``COMMAND_WARNINGS`` configuration option is also deprecated and defaults to ``False``. These will be removed and their presence will become an error in 2.14.
- apt_key - the parameter ``key`` does not have any effect, has been deprecated and will be removed in ansible-core version 2.14 (https://github.com/ansible/ansible/pull/70319).
- psrp - Set the minimum version of ``pypsrp`` to ``0.4.0``.

ansible.netcommon
~~~~~~~~~~~~~~~~~

- Deprecate cli_parse module and textfsm, ttp, xml, json parser plugins as they are moved to ansible.utils collection (https://github.com/ansible-collections/ansible.netcommon/pull/182 https://github.com/ansible-collections/ansible.utils/pull/28)

cisco.nxos
~~~~~~~~~~

- Deprecated nxos_bgp_af in favour of nxos_bgp_address_family resource module.
- Deprecated nxos_bgp_neighbor_af in favour of nxos_bgp_neighbor_address_family resource module.

cloudscale_ch.cloud
~~~~~~~~~~~~~~~~~~~

- The aliases ``server_uuids`` and ``server_uuid`` of the servers parameter in the volume module will be removed in version 3.0.0.

community.aws
~~~~~~~~~~~~~

- ec2_eip - formally deprecate the ``instance_id`` alias for ``device_id`` (https://github.com/ansible-collections/community.aws/pull/349).
- ec2_vpc_endpoint - deprecate the policy_file option and recommend using policy with a lookup (https://github.com/ansible-collections/community.aws/pull/366).
- ec2_vpc_endpoint_info - the ``query`` option has been deprecated and will be removed after 2022-12-01 (https://github.com/ansible-collections/community.aws/pull/346). The ec2_vpc_endpoint_info now defaults to listing information about endpoints. The ability to search for information about available services has been moved to the dedicated module ``ec2_vpc_endpoint_service_info``.

community.crypto
~~~~~~~~~~~~~~~~

- acme module_utils - the ``acme`` module_utils (``ansible_collections.community.crypto.plugins.module_utils.acme``) is deprecated and will be removed in community.crypto 2.0.0. Use the new Python modules in the ``acme`` package instead (``ansible_collections.community.crypto.plugins.module_utils.acme.xxx``) (https://github.com/ansible-collections/community.crypto/pull/184).
- acme_account_info - when ``retrieve_orders=url_list``, ``orders`` will no longer be returned in community.crypto 2.0.0. Use ``order_uris`` instead (https://github.com/ansible-collections/community.crypto/pull/178).

community.general
~~~~~~~~~~~~~~~~~

- apt_rpm - deprecated invalid parameter alias ``update-cache``, will be removed in 5.0.0 (https://github.com/ansible-collections/community.general/pull/1927).
- composer - deprecated invalid parameter aliases ``working-dir``, ``global-command``, ``prefer-source``, ``prefer-dist``, ``no-dev``, ``no-scripts``, ``no-plugins``, ``optimize-autoloader``, ``classmap-authoritative``, ``apcu-autoloader``, ``ignore-platform-reqs``, will be removed in 5.0.0 (https://github.com/ansible-collections/community.general/pull/1927).
- cpanm - parameter ``system_lib`` deprecated in favor of using ``become`` (https://github.com/ansible-collections/community.general/pull/2218).
- github_deploy_key - deprecated invalid parameter alias ``2fa_token``, will be removed in 5.0.0 (https://github.com/ansible-collections/community.general/pull/1927).
- grove - the option ``message`` will be removed in community.general 4.0.0. Use the new option ``message_content`` instead (https://github.com/ansible-collections/community.general/pull/1929).
- homebrew - deprecated invalid parameter alias ``update-brew``, will be removed in 5.0.0 (https://github.com/ansible-collections/community.general/pull/1927).
- homebrew_cask - deprecated invalid parameter alias ``update-brew``, will be removed in 5.0.0 (https://github.com/ansible-collections/community.general/pull/1927).
- opkg - deprecated invalid parameter alias ``update-cache``, will be removed in 5.0.0 (https://github.com/ansible-collections/community.general/pull/1927).
- pacman - deprecated invalid parameter alias ``update-cache``, will be removed in 5.0.0 (https://github.com/ansible-collections/community.general/pull/1927).
- puppet - deprecated undocumented parameter ``show_diff``, will be removed in 7.0.0. (https://github.com/ansible-collections/community.general/pull/1927).
- runit - unused parameter ``dist`` marked for deprecation (https://github.com/ansible-collections/community.general/pull/1830).
- slackpkg - deprecated invalid parameter alias ``update-cache``, will be removed in 5.0.0 (https://github.com/ansible-collections/community.general/pull/1927).
- urmpi - deprecated invalid parameter aliases ``update-cache`` and ``no-recommends``, will be removed in 5.0.0 (https://github.com/ansible-collections/community.general/pull/1927).
- xbps - deprecated invalid parameter alias ``update-cache``, will be removed in 5.0.0 (https://github.com/ansible-collections/community.general/pull/1927).
- xfconf - returning output as facts is deprecated, this will be removed in community.general 4.0.0. Please register the task output in a variable and use it instead. You can already switch to the new behavior now by using the new ``disable_facts`` option (https://github.com/ansible-collections/community.general/pull/1747).

community.vmware
~~~~~~~~~~~~~~~~

- vmware_vmkernel_ip_config - deprecate in favor of vmware_vmkernel (https://github.com/ansible-collections/community.vmware/pull/667).

f5networks.f5_modules
~~~~~~~~~~~~~~~~~~~~~

- Support for Python versions earlier than 3.5 is being deprecated

Removed Features (previously deprecated)
----------------------------------------

Ansible-core
~~~~~~~~~~~~

- Removed `SharedPluginLoaderObj` class from ansible.plugins.strategy. It was deprecated in favor of using the standard plugin loader.
- Removed `_get_item()` alias from callback plugin base class which had been deprecated in favor of `_get_item_label()`.
- The "user" parameter was previously deprecated and is now removed in favor of "scope"
- The deprecated ``ansible.constants.BECOME_METHODS`` has been removed.
- The deprecated ``ansible.constants.get_config()`` has been removed.
- The deprecated ``ansible.constants.mk_boolean()`` has been removed.
- `with_*` loops are no longer optimized for modules whose `name` parameters can take lists (mostly package managers). Use `name` instead of looping over individual names with `with_items` and friends.

community.general
~~~~~~~~~~~~~~~~~

- The ``ome_device_info``, ``idrac_firmware`` and ``idrac_server_config_profile``  modules have now been migrated from community.general to the `dellemc.openmanage <https://galaxy.ansible.com/dellemc/openmanage>`_ Ansible collection.
  If you use ansible-base 2.10 or newer, redirections have been provided.

  If you use Ansible 2.9 and installed this collection, you need to adjust the FQCNs (``community.general.idrac_firmware`` → ``dellemc.openmanage.idrac_firmware``) and make sure to install the dellemc.openmanage collection.
- The deprecated ali_instance_facts module has been removed. Use ali_instance_info instead (https://github.com/ansible-collections/community.general/pull/1924).
- The deprecated gluster_heal_info module has been removed. Use gluster.gluster.gluster_heal_info instead (https://github.com/ansible-collections/community.general/pull/1924).
- The deprecated gluster_peer module has been removed. Use gluster.gluster.gluster_peer instead (https://github.com/ansible-collections/community.general/pull/1924).
- The deprecated gluster_volume module has been removed. Use gluster.gluster.gluster_volume instead (https://github.com/ansible-collections/community.general/pull/1924).
- The deprecated helm module has been removed. Use community.kubernetes.helm instead (https://github.com/ansible-collections/community.general/pull/1924).
- The deprecated hpilo_facts module has been removed. Use hpilo_info instead (https://github.com/ansible-collections/community.general/pull/1924).
- The deprecated idrac_redfish_facts module has been removed. Use idrac_redfish_info instead (https://github.com/ansible-collections/community.general/pull/1924).
- The deprecated jenkins_job_facts module has been removed. Use jenkins_job_info instead (https://github.com/ansible-collections/community.general/pull/1924).
- The deprecated ldap_attr module has been removed. Use ldap_attrs instead (https://github.com/ansible-collections/community.general/pull/1924).
- The deprecated memset_memstore_facts module has been removed. Use memset_memstore_info instead (https://github.com/ansible-collections/community.general/pull/1924).
- The deprecated memset_server_facts module has been removed. Use memset_server_info instead (https://github.com/ansible-collections/community.general/pull/1924).
- The deprecated na_ontap_gather_facts module has been removed. Use netapp.ontap.na_ontap_info instead (https://github.com/ansible-collections/community.general/pull/1924).
- The deprecated nginx_status_facts module has been removed. Use nginx_status_info instead (https://github.com/ansible-collections/community.general/pull/1924).
- The deprecated one_image_facts module has been removed. Use one_image_info instead (https://github.com/ansible-collections/community.general/pull/1924).
- The deprecated onepassword_facts module has been removed. Use onepassword_info instead (https://github.com/ansible-collections/community.general/pull/1924).
- The deprecated oneview_datacenter_facts module has been removed. Use oneview_datacenter_info instead (https://github.com/ansible-collections/community.general/pull/1924).
- The deprecated oneview_enclosure_facts module has been removed. Use oneview_enclosure_info instead (https://github.com/ansible-collections/community.general/pull/1924).
- The deprecated oneview_ethernet_network_facts module has been removed. Use oneview_ethernet_network_info instead (https://github.com/ansible-collections/community.general/pull/1924).
- The deprecated oneview_fc_network_facts module has been removed. Use oneview_fc_network_info instead (https://github.com/ansible-collections/community.general/pull/1924).
- The deprecated oneview_fcoe_network_facts module has been removed. Use oneview_fcoe_network_info instead (https://github.com/ansible-collections/community.general/pull/1924).
- The deprecated oneview_logical_interconnect_group_facts module has been removed. Use oneview_logical_interconnect_group_info instead (https://github.com/ansible-collections/community.general/pull/1924).
- The deprecated oneview_network_set_facts module has been removed. Use oneview_network_set_info instead (https://github.com/ansible-collections/community.general/pull/1924).
- The deprecated oneview_san_manager_facts module has been removed. Use oneview_san_manager_info instead (https://github.com/ansible-collections/community.general/pull/1924).
- The deprecated online_server_facts module has been removed. Use online_server_info instead (https://github.com/ansible-collections/community.general/pull/1924).
- The deprecated online_user_facts module has been removed. Use online_user_info instead (https://github.com/ansible-collections/community.general/pull/1924).
- The deprecated ovirt module has been removed. Use ovirt.ovirt.ovirt_vm instead (https://github.com/ansible-collections/community.general/pull/1924).
- The deprecated ovirt_affinity_label_facts module has been removed. Use ovirt.ovirt.ovirt_affinity_label_info instead (https://github.com/ansible-collections/community.general/pull/1924).
- The deprecated ovirt_api_facts module has been removed. Use ovirt.ovirt.ovirt_api_info instead (https://github.com/ansible-collections/community.general/pull/1924).
- The deprecated ovirt_cluster_facts module has been removed. Use ovirt.ovirt.ovirt_cluster_info instead (https://github.com/ansible-collections/community.general/pull/1924).
- The deprecated ovirt_datacenter_facts module has been removed. Use ovirt.ovirt.ovirt_datacenter_info instead (https://github.com/ansible-collections/community.general/pull/1924).
- The deprecated ovirt_disk_facts module has been removed. Use ovirt.ovirt.ovirt_disk_info instead (https://github.com/ansible-collections/community.general/pull/1924).
- The deprecated ovirt_event_facts module has been removed. Use ovirt.ovirt.ovirt_event_info instead (https://github.com/ansible-collections/community.general/pull/1924).
- The deprecated ovirt_external_provider_facts module has been removed. Use ovirt.ovirt.ovirt_external_provider_info instead (https://github.com/ansible-collections/community.general/pull/1924).
- The deprecated ovirt_group_facts module has been removed. Use ovirt.ovirt.ovirt_group_info instead (https://github.com/ansible-collections/community.general/pull/1924).
- The deprecated ovirt_host_facts module has been removed. Use ovirt.ovirt.ovirt_host_info instead (https://github.com/ansible-collections/community.general/pull/1924).
- The deprecated ovirt_host_storage_facts module has been removed. Use ovirt.ovirt.ovirt_host_storage_info instead (https://github.com/ansible-collections/community.general/pull/1924).
- The deprecated ovirt_network_facts module has been removed. Use ovirt.ovirt.ovirt_network_info instead (https://github.com/ansible-collections/community.general/pull/1924).
- The deprecated ovirt_nic_facts module has been removed. Use ovirt.ovirt.ovirt_nic_info instead (https://github.com/ansible-collections/community.general/pull/1924).
- The deprecated ovirt_permission_facts module has been removed. Use ovirt.ovirt.ovirt_permission_info instead (https://github.com/ansible-collections/community.general/pull/1924).
- The deprecated ovirt_quota_facts module has been removed. Use ovirt.ovirt.ovirt_quota_info instead (https://github.com/ansible-collections/community.general/pull/1924).
- The deprecated ovirt_scheduling_policy_facts module has been removed. Use ovirt.ovirt.ovirt_scheduling_policy_info instead (https://github.com/ansible-collections/community.general/pull/1924).
- The deprecated ovirt_snapshot_facts module has been removed. Use ovirt.ovirt.ovirt_snapshot_info instead (https://github.com/ansible-collections/community.general/pull/1924).
- The deprecated ovirt_storage_domain_facts module has been removed. Use ovirt.ovirt.ovirt_storage_domain_info instead (https://github.com/ansible-collections/community.general/pull/1924).
- The deprecated ovirt_storage_template_facts module has been removed. Use ovirt.ovirt.ovirt_storage_template_info instead (https://github.com/ansible-collections/community.general/pull/1924).
- The deprecated ovirt_storage_vm_facts module has been removed. Use ovirt.ovirt.ovirt_storage_vm_info instead (https://github.com/ansible-collections/community.general/pull/1924).
- The deprecated ovirt_tag_facts module has been removed. Use ovirt.ovirt.ovirt_tag_info instead (https://github.com/ansible-collections/community.general/pull/1924).
- The deprecated ovirt_template_facts module has been removed. Use ovirt.ovirt.ovirt_template_info instead (https://github.com/ansible-collections/community.general/pull/1924).
- The deprecated ovirt_user_facts module has been removed. Use ovirt.ovirt.ovirt_user_info instead (https://github.com/ansible-collections/community.general/pull/1924).
- The deprecated ovirt_vm_facts module has been removed. Use ovirt.ovirt.ovirt_vm_info instead (https://github.com/ansible-collections/community.general/pull/1924).
- The deprecated ovirt_vmpool_facts module has been removed. Use ovirt.ovirt.ovirt_vmpool_info instead (https://github.com/ansible-collections/community.general/pull/1924).
- The deprecated purefa_facts module has been removed. Use purestorage.flasharray.purefa_info instead (https://github.com/ansible-collections/community.general/pull/1924).
- The deprecated purefb_facts module has been removed. Use purestorage.flasharray.purefb_info instead (https://github.com/ansible-collections/community.general/pull/1924).
- The deprecated python_requirements_facts module has been removed. Use python_requirements_info instead (https://github.com/ansible-collections/community.general/pull/1924).
- The deprecated redfish_facts module has been removed. Use redfish_info instead (https://github.com/ansible-collections/community.general/pull/1924).
- The deprecated scaleway_image_facts module has been removed. Use scaleway_image_info instead (https://github.com/ansible-collections/community.general/pull/1924).
- The deprecated scaleway_ip_facts module has been removed. Use scaleway_ip_info instead (https://github.com/ansible-collections/community.general/pull/1924).
- The deprecated scaleway_organization_facts module has been removed. Use scaleway_organization_info instead (https://github.com/ansible-collections/community.general/pull/1924).
- The deprecated scaleway_security_group_facts module has been removed. Use scaleway_security_group_info instead (https://github.com/ansible-collections/community.general/pull/1924).
- The deprecated scaleway_server_facts module has been removed. Use scaleway_server_info instead (https://github.com/ansible-collections/community.general/pull/1924).
- The deprecated scaleway_snapshot_facts module has been removed. Use scaleway_snapshot_info instead (https://github.com/ansible-collections/community.general/pull/1924).
- The deprecated scaleway_volume_facts module has been removed. Use scaleway_volume_info instead (https://github.com/ansible-collections/community.general/pull/1924).
- The deprecated smartos_image_facts module has been removed. Use smartos_image_info instead (https://github.com/ansible-collections/community.general/pull/1924).
- The deprecated vertica_facts module has been removed. Use vertica_info instead (https://github.com/ansible-collections/community.general/pull/1924).
- The deprecated xenserver_guest_facts module has been removed. Use xenserver_guest_info instead (https://github.com/ansible-collections/community.general/pull/1924).
- The ovirt_facts docs fragment has been removed (https://github.com/ansible-collections/community.general/pull/1924).
- airbrake_deployment - removed deprecated ``token`` parameter. Use ``project_id`` and ``project_key`` instead (https://github.com/ansible-collections/community.general/pull/1926).
- bigpanda - the alias ``message`` has been removed. Use ``deployment_message`` instead (https://github.com/ansible-collections/community.general/pull/1926).
- cisco_spark, cisco_webex - the alias ``message`` has been removed. Use ``msg`` instead (https://github.com/ansible-collections/community.general/pull/1926).
- clc_aa_policy - the ``wait`` parameter has been removed. It did not have any effect (https://github.com/ansible-collections/community.general/pull/1926).
- datadog_monitor - the alias ``message`` has been removed. Use ``notification_message`` instead (https://github.com/ansible-collections/community.general/pull/1926).
- django_manage - the parameter ``liveserver`` has been removed (https://github.com/ansible-collections/community.general/pull/1926).
- idrac_redfish_config - the parameters ``manager_attribute_name`` and ``manager_attribute_value`` have been removed. Use ``manager_attributes`` instead (https://github.com/ansible-collections/community.general/pull/1926).
- iso_extract - the alias ``thirsty`` has been removed. Use ``force`` instead (https://github.com/ansible-collections/community.general/pull/1926).
- ldap_entry - the ``params`` parameter is now completely removed. Using it already triggered an error since community.general 0.1.2 (https://github.com/ansible-collections/community.general/pull/2257).
- pulp_repo - the ``feed_client_cert`` parameter no longer defaults to the value of the ``client_cert`` parameter (https://github.com/ansible-collections/community.general/pull/1926).
- pulp_repo - the ``feed_client_key`` parameter no longer defaults to the value of the ``client_key`` parameter (https://github.com/ansible-collections/community.general/pull/1926).
- pulp_repo - the alias ``ca_cert`` has been removed. Use ``feed_ca_cert`` instead (https://github.com/ansible-collections/community.general/pull/1926).
- rax - unused parameter ``service`` removed (https://github.com/ansible-collections/community.general/pull/2020).
- redfish modules - issuing a data modification command without specifying the ID of the target System, Chassis or Manager resource when there is more than one is no longer allowed. Use the ``resource_id`` option to specify the target ID (https://github.com/ansible-collections/community.general/pull/1926).
- redfish_config - the parameters ``bios_attribute_name`` and ``bios_attribute_value`` have been removed. Use ``bios_attributes`` instead (https://github.com/ansible-collections/community.general/pull/1926).
- syspatch - the ``apply`` parameter has been removed. This is the default mode, so simply removing it will not change the behavior (https://github.com/ansible-collections/community.general/pull/1926).
- xbps - the ``force`` parameter has been removed. It did not have any effect (https://github.com/ansible-collections/community.general/pull/1926).

community.network
~~~~~~~~~~~~~~~~~

- The deprecated ``community.network.ce_sflow`` parameters: ``rate_limit``, ``rate_limit_slot``, and ``forward_enp_slot`` have been removed (https://github.com/ansible-collections/community.network/pull/255).
- The deprecated ``community.network.sros`` netconf plugin has been removed. Use ``nokia.sros.md`` instead (https://github.com/ansible-collections/community.network/pull/255).

f5networks.f5_modules
~~~~~~~~~~~~~~~~~~~~~

- Removed TMOS v11 support for bigip_gtm_pool and bigip_gtm_wide_ip modules
- Removed quorum and monitor_type parameters in bigip_node module. See porting guides section at https://clouddocs.f5.com/products/orchestration/ansible/devel/usage/porting-guides.html
- Removed syslog_settings and pool_settings parameters in bigip_log_destination moduke. See porting guides section at https://clouddocs.f5.com/products/orchestration/ansible/devel/usage/porting-guides.html

fortinet.fortios
~~~~~~~~~~~~~~~~

- Removed module fortios_facts
- Removed module fortios_registration_forticare
- Removed module fortios_registration_vdom
- Removed module fortios_system_config_backup_restore
- Removed module fortios_system_vmlicense

Security Fixes
--------------

Ansible-core
~~~~~~~~~~~~

- **security issue** - Mask default and fallback values for ``no_log`` module options (CVE-2021-20228)
- **security issue** - copy - Redact the value of the no_log 'content' parameter in the result's invocation.module_args in check mode. Previously when used with check mode and with '-vvv', the module would not censor the content if a change would be made to the destination path. (CVE-2020-14332)
- Sanitize no_log values from any response keys that might be returned from the uri module (CVE-2020-14330).
- dnf - Previously, regardless of the ``disable_gpg_check`` option, packages were not GPG validated. They are now. (CVE-2020-14365)

arista.eos
~~~~~~~~~~

- Mask values of sensitive keys in module result.

cisco.iosxr
~~~~~~~~~~~

- Properly mask values of sensitive keys in module result.

cisco.nxos
~~~~~~~~~~

- Properly mask values of sensitive keys in module result.

community.aws
~~~~~~~~~~~~~

- aws_direct_connect_virtual_interface - mark the ``authentication_key`` parameter as ``no_log`` to avoid accidental leaking of secrets in logs (https://github.com/ansible-collections/community.aws/pull/475).
- aws_secret - flag the ``secret`` parameter as containing sensitive data which shouldn't be logged (https://github.com/ansible-collections/community.aws/pull/471).
- sts_assume_role - mark the ``mfa_token`` parameter as ``no_log`` to avoid accidental leaking of secrets in logs (https://github.com/ansible-collections/community.aws/pull/475).
- sts_session_token - mark the ``mfa_token`` parameter as ``no_log`` to avoid accidental leaking of secrets in logs (https://github.com/ansible-collections/community.aws/pull/475).

community.docker
~~~~~~~~~~~~~~~~

- docker_swarm - the ``join_token`` option is now marked as ``no_log`` so it is no longer written into logs (https://github.com/ansible-collections/community.docker/pull/103).

community.general
~~~~~~~~~~~~~~~~~

- dnsmadeeasy - mark the ``account_key`` parameter as ``no_log`` to avoid leakage of secrets (https://github.com/ansible-collections/community.general/pull/1736).
- gitlab_runner - mark the ``registration_token`` parameter as ``no_log`` to avoid leakage of secrets (https://github.com/ansible-collections/community.general/pull/1736).
- hwc_ecs_instance - mark the ``admin_pass`` parameter as ``no_log`` to avoid leakage of secrets (https://github.com/ansible-collections/community.general/pull/1736).
- ibm_sa_host - mark the ``iscsi_chap_secret`` parameter as ``no_log`` to avoid leakage of secrets (https://github.com/ansible-collections/community.general/pull/1736).
- java_cert - remove password from ``run_command`` arguments (https://github.com/ansible-collections/community.general/pull/2008).
- java_keystore - pass secret to keytool through an environment variable to not expose it as a commandline argument (https://github.com/ansible-collections/community.general/issues/1668).
- keycloak_* modules - mark the ``auth_client_secret`` parameter as ``no_log`` to avoid leakage of secrets (https://github.com/ansible-collections/community.general/pull/1736).
- keycloak_client - mark the ``registration_access_token`` parameter as ``no_log`` to avoid leakage of secrets (https://github.com/ansible-collections/community.general/pull/1736).
- librato_annotation - mark the ``api_key`` parameter as ``no_log`` to avoid leakage of secrets (https://github.com/ansible-collections/community.general/pull/1736).
- logentries_msg - mark the ``token`` parameter as ``no_log`` to avoid leakage of secrets (https://github.com/ansible-collections/community.general/pull/1736).
- module_utils/_netapp, na_ontap_gather_facts - enabled ``no_log`` for the options ``api_key`` and ``secret_key`` to prevent accidental disclosure (CVE-2021-20191, https://github.com/ansible-collections/community.general/pull/1725).
- module_utils/identity/keycloak, keycloak_client, keycloak_clienttemplate, keycloak_group - enabled ``no_log`` for the option ``auth_client_secret`` to prevent accidental disclosure (CVE-2021-20191, https://github.com/ansible-collections/community.general/pull/1725).
- nios_nsgroup - mark the ``tsig_key`` parameter as ``no_log`` to avoid leakage of secrets (https://github.com/ansible-collections/community.general/pull/1736).
- oneandone_firewall_policy, oneandone_load_balancer, oneandone_monitoring_policy, oneandone_private_network, oneandone_public_ip - mark the ``auth_token`` parameter as ``no_log`` to avoid leakage of secrets (https://github.com/ansible-collections/community.general/pull/1736).
- ovirt - mark the ``instance_key`` parameter as ``no_log`` to avoid leakage of secrets (https://github.com/ansible-collections/community.general/pull/1736).
- ovirt - mark the ``instance_rootpw`` parameter as ``no_log`` to avoid leakage of secrets (https://github.com/ansible-collections/community.general/pull/1736).
- pagerduty_alert - mark the ``api_key``, ``service_key`` and ``integration_key`` parameters as ``no_log`` to avoid leakage of secrets (https://github.com/ansible-collections/community.general/pull/1736).
- pagerduty_change - mark the ``integration_key`` parameter as ``no_log`` to avoid leakage of secrets (https://github.com/ansible-collections/community.general/pull/1736).
- pingdom - mark the ``key`` parameter as ``no_log`` to avoid leakage of secrets (https://github.com/ansible-collections/community.general/pull/1736).
- pulp_repo - mark the ``feed_client_key`` parameter as ``no_log`` to avoid leakage of secrets (https://github.com/ansible-collections/community.general/pull/1736).
- rax_clb_ssl - mark the ``private_key`` parameter as ``no_log`` to avoid leakage of secrets (https://github.com/ansible-collections/community.general/pull/1736).
- redfish_command - mark the ``update_creds.password`` parameter as ``no_log`` to avoid leakage of secrets (https://github.com/ansible-collections/community.general/pull/1736).
- rollbar_deployment - mark the ``token`` parameter as ``no_log`` to avoid leakage of secrets (https://github.com/ansible-collections/community.general/pull/1736).
- spotinst_aws_elastigroup - mark the ``multai_token`` and ``token`` parameters as ``no_log`` to avoid leakage of secrets (https://github.com/ansible-collections/community.general/pull/1736).
- stackdriver - mark the ``key`` parameter as ``no_log`` to avoid leakage of secrets (https://github.com/ansible-collections/community.general/pull/1736).
- utm_proxy_auth_profile - enabled ``no_log`` for the option ``frontend_cookie_secret`` to prevent accidental disclosure (CVE-2021-20191, https://github.com/ansible-collections/community.general/pull/1725).
- utm_proxy_auth_profile - mark the ``frontend_cookie_secret`` parameter as ``no_log`` to avoid leakage of secrets. This causes the ``utm_proxy_auth_profile`` return value to no longer containing the correct value, but a placeholder (https://github.com/ansible-collections/community.general/pull/1736).

community.network
~~~~~~~~~~~~~~~~~

- avi_cloudconnectoruser - mark the ``azure_userpass``, ``gcp_credentials``, ``oci_credentials``, and ``tencent_credentials`` parameters as ``no_log`` to prevent leaking of secret values (https://github.com/ansible-collections/community.network/pull/223).
- avi_sslkeyandcertificate - mark the ``enckey_base64`` parameter as ``no_log`` to prevent potential leaking of secret values (https://github.com/ansible-collections/community.network/pull/223).
- avi_webhook - mark the ``verification_token`` parameter as ``no_log`` to prevent potential leaking of secret values (https://github.com/ansible-collections/community.network/pull/223).
- ce_vrrp - mark the ``auth_key`` parameter as ``no_log`` to avoid leakage of secrets (https://github.com/ansible-collections/community.network/pull/206).
- cloudengine/ce_vrrp - enabled ``no_log`` for the options ``auth_key`` to prevent accidental disclosure (CVE-2021-20191, https://github.com/ansible-collections/community.network/pull/203).
- cnos_* modules - mark the ``passwords`` parameter as ``no_log`` to avoid leakage of secrets (https://github.com/ansible-collections/community.network/pull/206).
- enos_* modules - mark the ``passwords`` parameter as ``no_log`` to avoid leakage of secrets (https://github.com/ansible-collections/community.network/pull/206).
- iap_start_workflow - mark the ``token_key`` parameter as ``no_log`` to avoid leakage of secrets (https://github.com/ansible-collections/community.network/pull/206).
- icx_system - mark the ``auth_key`` parameter as ``no_log`` to avoid leakage of secrets (https://github.com/ansible-collections/community.network/pull/206).
- itential/iap_start_workflow - enabled ``no_log`` for the options ``token_key`` to prevent accidental disclosure (CVE-2021-20191, https://github.com/ansible-collections/community.network/pull/203).
- netscaler/netscaler_lb_monitor - enabled ``no_log`` for the options ``radkey`` to prevent accidental disclosure (CVE-2021-20191, https://github.com/ansible-collections/community.network/pull/203).
- netscaler_lb_monitor - mark the ``password`` and ``secondarypassword`` parameters as ``no_log`` to avoid leakage of secrets (https://github.com/ansible-collections/community.network/pull/206).

community.vmware
~~~~~~~~~~~~~~~~

- vmware_host_iscsi - mark the ``chap_secret`` parameter as ``no_log`` to avoid accidental leaking of secrets in logs (https://github.com/ansible-collections/community.vmware/pull/715).
- vmware_host_iscsi - mark the ``mutual_chap_secret`` parameter as ``no_log`` to avoid accidental leaking of secrets in logs (https://github.com/ansible-collections/community.vmware/pull/715).
- vmware_vc_infraprofile_info - mark the ``decryption_key`` parameter as ``no_log`` to avoid accidental leaking of secrets in logs (https://github.com/ansible-collections/community.vmware/pull/715).
- vmware_vc_infraprofile_info - mark the ``encryption_key`` parameter as ``no_log`` to avoid accidental leaking of secrets in logs (https://github.com/ansible-collections/community.vmware/pull/715).

community.zabbix
~~~~~~~~~~~~~~~~

- zabbix_action - no longer exposes remote SSH command password used in operations, recovery & acknowledge operations to system logs (https://github.com/ansible-collections/community.zabbix/pull/345).
- zabbix_discovery_rule - no longer exposes SNMPv3 auth and priv passphrases to system logs (https://github.com/ansible-collections/community.zabbix/pull/345).
- zabbix_host - no longer exposes SNMPv3 auth and priv passphrases to system logs (https://github.com/ansible-collections/community.zabbix/pull/345).

hetzner.hcloud
~~~~~~~~~~~~~~

- hcloud_certificate - mark the ``private_key`` parameter as ``no_log`` to prevent potential leaking of secret values (https://github.com/ansible-collections/hetzner.hcloud/pull/70).

junipernetworks.junos
~~~~~~~~~~~~~~~~~~~~~

- Mask values of sensitive keys in module result(https://github.com/ansible-collections/junipernetworks.junos/issues/165).

vyos.vyos
~~~~~~~~~

- Mask values of sensitive keys in module result.

Bugfixes
--------

Ansible-core
~~~~~~~~~~~~

- A handler defined within a role will now search handlers subdir for included tasks (issue https://github.com/ansible/ansible/issues/71222).
- ALLOW_WORLD_READABLE_TMP, switched to 'moved' message as 'deprecation' is misleading since config settings still work w/o needing change.
- ANSIBLE_COLLECTIONS_PATHS - remove deprecation so that users of Ansible 2.9 and 2.10+ can use the same var when specifying a collection path without a warning.
- Added unsafe_writes test.
- Address compat with rpmfluff-0.6 for integration tests
- Address the deprecation of the use of stdlib distutils in packaging. It's a short-term hotfix for the problem (https://github.com/ansible/ansible/issues/70456, https://github.com/pypa/setuptools/issues/2230, https://github.com/pypa/setuptools/commit/bd110264)
- Adjust various hard-coded action names to also include their ``ansible.builtin.`` and ``ansible.legacy.`` prefixed version (https://github.com/ansible/ansible/issues/71817, https://github.com/ansible/ansible/issues/71818, https://github.com/ansible/ansible/pull/71824).
- Allow TypeErrors on Undefined variables in filters to be handled or deferred when processing for loops.
- Allow `~` to be present in file names in galaxy roles (https://github.com/ansible/ansible/issues/72966)
- Always mention the name of the deprecated or tombstoned plugin in routing deprecation/tombstone messages (https://github.com/ansible/ansible/pull/73059).
- Ansible output now uses stdout to determine column width instead of stdin
- AnsibleModule - added arg ``ignore_invalid_cwd`` to ``AnsibleModule.run_command()``, to control its behaviour when ``cwd`` is invalid. (https://github.com/ansible/ansible/pull/72390)
- Apply ``_wrap_native_text`` only for builtin filters specified in STRING_TYPE_FILTERS.
- Automatically remove async cache files for polled async tasks that have completed (issue https://github.com/ansible/ansible/issues/73206).
- Be smarter about collection paths ending with ansible_collections, emulating a-galaxy behaviour. Issue 72628
- CLI - Restore git information in version output when running from source
- Collection callbacks were ignoring options and rules for stdout and adhoc cases.
- Collections - Ensure ``action_loader.get`` is called with ``collection_list`` to properly find collections when ``collections:`` search is specified (https://github.com/ansible/ansible/issues/72170)
- Command module now returns stdout & stderr if executable is missing or an unknown error occurs
- ConfigManager - Normalize ConfigParser between Python2 and Python3 to for handling comments (https://github.com/ansible/ansible/issues/73709)
- Continue execution when  'flatten' filter when it hits a None/null value as part of the list.
- Correct the inventory source error parse handling, specifically make the config INVENTORY_ANY_UNPARSED_IS_FAILED work as expected.
- Correctly set template_path and template_fullpath for usage in template lookup and action plugins.
- Deal with failures when sorting JSON and you have incompatible key types.
- Display - Use wcswidth to calculate printable width of a text string (https://github.com/ansible/ansible/issues/63105)
- Enabled unsafe_writes for get_url which was ignoring the paramter.
- Ensure Ansible's unique filter preserves order (https://github.com/ansible/ansible/issues/63417)
- Ensure if a traceback halts ``strategy.run`` that we still attempt to clean up (https://github.com/ansible/ansible/issues/23958)
- Ensure password passed in by -k is used on delegated hosts that do not have ansible_password set
- Ensure the correct options are used when ssh executables are used that don't match ssh executable names.
- Facts collection - get serial number of NVMe device without sg_inq (https://github.com/ansible/ansible/issues/66663).
- Fix --list-tasks format `role_name : task_name` when task name contains the role name. (https://github.com/ansible/ansible/issues/72505)
- Fix ``RecursionError`` when templating large vars structures (https://github.com/ansible/ansible/issues/71920)
- Fix ``delegate_facts: true`` when ``ansible_python_interpreter`` is not set. (https://github.com/ansible/ansible/issues/70168)
- Fix adding unrelated candidate names to the plugin loader redirect list.
- Fix an exit code for a non-failing playbook (https://github.com/ansible/ansible/issues/71306)
- Fix ansible-galaxy collection list to show collections in site-packages (https://github.com/ansible/ansible/issues/70147)
- Fix bytestring vs string comparison in module_utils.basic.is_special_selinux_path() so that special-cased filesystems which don't support SELinux context attributes still allow files to be manipulated on them. (https://github.com/ansible/ansible/issues/70244)
- Fix execution of the meta tasks 'clear_facts', 'clear_host_errors', 'end_play', 'end_host', and 'reset_connection' when the CLI flag '--flush-cache' is provided.
- Fix fileglob bug where it could return different results for different order of parameters (https://github.com/ansible/ansible/issues/72873).
- Fix incorrect msg in the results dict in loops
- Fix incorrect re-run of roles with tags (https://github.com/ansible/ansible/issues/69848)
- Fix incorrect variable scoping when using ``import with context`` in Jinja2 templates. (https://github.com/ansible/ansible/issues/72615)
- Fix jsonfile cache plugin option '_uri' to be a type path instead of a string. (https://github.com/ansible/ansible/issues/38002)
- Fix notifying handlers via `role_name : handler_name` when handler name contains the role name. (https://github.com/ansible/ansible/issues/70582)
- Fix parsing of values when using empty string as a key (https://github.com/ansible/ansible/issues/57132)
- Fix statistics reporting when rescue block contains another block (issue https://github.com/ansible/ansible/issues/61253).
- Fix to previous deprecation change (#70504) which caused command warning deprecation to show in all cases, even when not specified by the user.
- Fixed TypeError instancemethod expecting at least 2 arguments for apt_repository(issue https://github.com/ansible/ansible/issues/69308, PR https://github.com/ansible/ansible/pull/69463)
- Fixed issue when `netstat` is either missing or doesn't have execution permissions leading to incorrect command being executed.
- Fixes ``ansible-galaxy role info`` to support multiple roles on the command line (https://github.com/ansible/ansible/pull/70148)
- Fixes ansible-test traceback when plugin author is not a string or a list of strings (https://github.com/ansible/ansible/pull/70507)
- Handle more varnames that can create conflicts, expand a function in general, handle jinja2 globals in particular (https://github.com/ansible/ansible/issues/41955).
- INTERPRETER_PYTHON_DISTRO_MAP - prefer ``/usr/libexec/platform-python`` on ``oraclelinux 8`` when other pythons are present.
- Improve Ansible config deprecations to show the source of the deprecation (ansible-core). Also remove space before a comma in config deprecations (https://github.com/ansible/ansible/pull/72697).
- Improved/fixed regular expressions in ``validate-modules/validate_modules/schema.py`` and ``utils/collection_loader/_collection_finder.py`` (https://github.com/ansible/ansible/pull/73577).
- Includes - Explicitly get the include task, and not assume it is the parent (https://github.com/ansible/ansible/issues/65710)
- InventoryManager - Fix unhandled exception when given limit file was actually a directory.
- InventoryManager - Fix unhandled exception when inventory directory was empty or contained empty subdirectories (https://github.com/ansible/ansible/issues/73658).
- JSON Encoder - Ensure we treat single vault encrypted values as strings (https://github.com/ansible/ansible/issues/70784)
- Lookup user by UID in password database if login name is not found (https://github.com/ansible/ansible/issues/17029)
- OpenBSD module_utils - update sysctl variable name
- Pass expression in angle-bracket notation as filename argument to a ``compile()`` built-in function, so that Python debuggers do not try to parse it as filename.
- Pass the connection's timeout to connection plugins instead of the task's timeout.
- Provide more information in AnsibleUndefinedVariable (https://github.com/ansible/ansible/issues/55152)
- Python module_utils finder - refactor logic to eliminate many corner cases, remove recursion, fix base module_utils redirections
- Remove an embedded function from RoleMixin and add tests for it (https://github.com/ansible/ansible/pull/72754).
- Remove the warning displayed when validating the arg spec of a role with dependencies and add it to the documentation.
- Restore the ability for changed_when/failed_when to function with group_by (#70844).
- Restored unsafe_writes functionality which was being skipped.
- Restructured pipelining settings to be at the connection plugins leaving base config as global and for backwards compatiblity.
- SSH plugin - Improve error message when ssh client is not found on the host
- Setup virtualization_facts - add RHV and oVirt type. This change will fully work for VMs in clusters at cluster level 4.4 or newer (https://github.com/ansible/ansible/pull/72876).
- Skip invalid collection names when listing in ansible-doc instead of throwing exception. Issue#72257
- Skip literal_eval for string filters results in native jinja. (https://github.com/ansible/ansible/issues/70831)
- Stop adding the connection variables to the output results
- Strategy - When building the task in the Strategy from the Worker, ensure it is properly marked as finalized and squashed. Addresses an issue with ``ansible_failed_task``. (https://github.com/ansible/ansible/issues/57399)
- Suppress warning when user directory used in --playbook-dir option with ansible-inventory command (https://github.com/ansible/ansible/issues/65262).
- TOML inventory - Ensure we register dump functions for ``AnsibleUnsafe`` to support dumping unsafe values. Note that the TOML format has no functionality to mark that the data is unsafe for re-consumption. (https://github.com/ansible/ansible/issues/71307)
- Terminal plugins - add "\e[m" to the list of ANSI sequences stripped from device output
- The ``docker`` and ``k8s`` action groups / module default groups now also support the moved modules in `community.docker <https://galaxy.ansible.com/community/docker>`_, `community.kubevirt <https://github.com/ansible-collections/community.kubevirt>`_, `community.okd <https://galaxy.ansible.com/community/okd>`_, and `kubernetes.core <https://galaxy.ansible.com/kubernetes/core>`_ (https://github.com/ansible/ansible/pull/72428).
- The ``flush()`` method of ``CachePluginAdjudicator`` now calls the plugin's ``flush()`` method instead of iterating over the keys that the adjudicator knows about and deleting those from the cache. (https://github.com/ansible/ansible/issues/68770)
- The `ansible_become` value was not being treated as a boolean value when set in an INI format inventory file (fixes bug https://github.com/ansible/ansible/issues/70476).
- The machine-readable changelog ``changelogs/changelog.yaml`` is now contained in the release.
- Try to avoid kernel 'blocking' state on reading files while fact gathering.
- Updated docs and added warning on max_fail_percentage and free strategy usage. fixes issue 16666.
- VariableManager - Add the 'vars' key before getting delegated variables (https://github.com/ansible/ansible/issues/71092).
- Vault - Allow single vault encrypted values to be used directly as module parameters. (https://github.com/ansible/ansible/issues/68275)
- WorkerProcess - Implement workaround for stdout deadlock in multiprocessing shutdown to avoid process hangs.
- WorkerProcess - Python 3.5 fix for workaround for stdout deadlock in multiprocessing shutdown to avoid process hangs. (https://github.com/ansible/ansible/issues/74149)
- [set_fact] Corrected and expanded documentation as well as now raise errors that were previously ignored.
- account for bug in Python 2.6 that occurs during interpreter shutdown to avoid stack trace
- action plugins - change all action/module delegations to use FQ names while allowing overrides (https://github.com/ansible/ansible/issues/69788)
- add AlmaLinux to fact gathering (https://github.com/ansible/ansible/pull/73458)
- add constraints file for ``ansible_runner`` test since an update to ``psutil`` is now causing test failures
- add magic/connection vars updates from delegated host info.
- add support for alpine linux 'apk' package manager in package_facts
- allow become method 'su' to work on 'local' connection by allocating a fake tty.
- ansible-console - Ctrl+C (in a task) abort current task, and put you back on prompt (this behavior doesn't change) (ditto)
- ansible-console - Ctrl+C (on prompt) used to exit the shell, unlike most shells, it should just reset the current line (ie. abort it and spawn a new prompt) (https://github.com/ansible/ansible/issues/68529)
- ansible-console - Ctrl+D (on prompt) now exit the shell, this is the expected behavior in a shell (cf bash, sh, zsh, ipython, ...) (ditto)
- ansible-console - add more documentation, specifically on various commands[1] (https://github.com/ansible/ansible/issues/72195)
- ansible-console - fixes few strings' typos
- ansible-console - remove useless and poorly formatted comment section (replaced with [1])
- ansible-doc - account for an empty ``meta/main.yml`` file when displaying role information (https://github.com/ansible/ansible/pull/73590)
- ansible-doc - collection name for plugin top-level deprecation was not inserted when deprecating by version (https://github.com/ansible/ansible/pull/70344).
- ansible-doc - improve error message in text formatter when ``description`` is missing for a (sub-)option or a return value or its ``contains`` (https://github.com/ansible/ansible/pull/70046).
- ansible-doc - improve man page formatting to avoid problems when YAML anchors are used (https://github.com/ansible/ansible/pull/70045).
- ansible-doc - include the collection name in the text output (https://github.com/ansible/ansible/pull/70401).
- ansible-doc - plugin option deprecations now also get ``collection_name`` added (https://github.com/ansible/ansible/pull/71735).
- ansible-doc - properly show plugin name when ``name:`` is used instead of ``<plugin_type>:`` (https://github.com/ansible/ansible/pull/71966).
- ansible-galaxy - Cache the responses for available collection versions after getting all pages. (https://github.com/ansible/ansible/issues/73071)
- ansible-galaxy - Instead of assuming the first defined server is galaxy, filter based on the servers that support the v1 API, and return the first of those (https://github.com/ansible/ansible/issues/65440)
- ansible-galaxy - Use ``sys.exit`` instead of ``exit`` when reporting an error for the removed login command.
- ansible-galaxy - correct ``collections-path`` command line argument (https://github.com/ansible/ansible/issues/73127)
- ansible-galaxy - fixed galaxy role init command (https://github.com/ansible/ansible/issues/71977).
- ansible-galaxy collection download - fix downloading tar.gz files and collections in git repositories (https://github.com/ansible/ansible/issues/70429)
- ansible-galaxy collection install - fix fallback mechanism if the AH server did not have the collection requested - https://github.com/ansible/ansible/issues/70940
- ansible-galaxy download - fix bug when downloading a collection in a SCM subdirectory
- ansible-pull - Run all playbooks that when multiple are supplied via the command line (https://github.com/ansible/ansible/issues/72708)
- ansible-test - Add ``pytest < 6.0.0`` constraint for managed installations on Python 3.x to avoid issues with relative imports.
- ansible-test - Add a ``six < 1.14.0`` constraint for Python 2.6.
- ansible-test - Always connect additional Docker containers to the network used by the current container (if any).
- ansible-test - Always map ``/var/run/docker.sock`` into test containers created by the ``--docker`` option if the docker host is not ``localhost``.
- ansible-test - Attempt to detect the Docker hostname instead of assuming ``localhost``.
- ansible-test - Avoid using ``/tmp`` to resolve occasional failures starting tests with the ``--docker`` option.
- ansible-test - Change classification using ``--changed`` now consistently handles common configuration files for supported CI providers.
- ansible-test - Change detection now properly resolves relative imports instead of treating them as absolute imports.
- ansible-test - Correctly detect changes in a GitHub pull request when running on Azure Pipelines.
- ansible-test - Correctly detect running in a Docker container on Azure Pipelines.
- ansible-test - Do not try to validate PowerShell modules ``setup.ps1``, ``slurp.ps1``, and ``async_status.ps1``
- ansible-test - Prefer container IP at ``.NetworkSettings.Networks.{NetworkName}.IPAddress`` over ``.NetworkSettings.IPAddress``.
- ansible-test - Running tests using an installed version of ``ansible-test`` against one Python version from another no longer fails due to a missing ``egg-info`` directory. This could occur when testing plugins which import ``pkg_resources``.
- ansible-test - Running tests using an installed version of ``ansible-test`` no longer generates an error attempting to create an ``egg-info`` directory when an existing one is not found in the expected location. This could occur if the existing ``egg-info`` directory included a Python version specifier in the name.
- ansible-test - Skip installing requirements if they are already installed.
- ansible-test - Symbolic links are no longer used to inject ``python`` into the environment, since they do not work reliably in all cases. Instead, the existing Python based exec wrapper is always used.
- ansible-test - Temporarily limit ``cryptography`` to versions before 3.4 to enable tests to function.
- ansible-test - The ``--export`` option for ``ansible-test coverage`` is now limited to the ``combine`` command. It was previously available for reporting commands on which it had no effect.
- ansible-test - The ``--raw`` option for ``ansible-test shell --remote`` now uses ``sh`` for the shell instead of ``bash``, which may not be present.
- ansible-test - The ``--remote`` option has been updated for Python 2.7 to work around breaking changes in the newly released ``get-pip.py`` bootstrapper.
- ansible-test - The ``--remote`` option has been updated to use a versioned ``get-pip.py`` bootstrapper to avoid issues with future releases.
- ansible-test - The ``ansible-doc`` sanity test now works for ``netconf`` plugins.
- ansible-test - The ``ansible-test coverage combine`` option ``--export`` now exports relative paths. This avoids loss of coverage data when aggregating across systems with different absolute paths. Paths will be converted back to absolute when generating reports.
- ansible-test - The ``changelog`` sanity test has been updated to ensure ``rstcheck`` does not load the ``sphinx`` module.
- ansible-test - The ``cs`` and ``openshift`` test plugins now search for containers on the current network instead of assuming the ``bridge`` network.
- ansible-test - The ``resource_prefix`` variable provided to tests running on Azure Pipelines is now converted to lowercase to match other CI providers.
- ansible-test - Unified SSH key management for all instances created with the ``--remote`` or ``--docker`` options.
- ansible-test - Using the ``--remote`` option on Azure Pipelines now works from a job running in a container.
- ansible-test - ``cryptography`` is now limited to versions prior to 3.2 only when an incompatible OpenSSL version (earlier than 1.1.0) is detected
- ansible-test - add constraint for ``cffi`` to prevent failure on systems with older versions of ``gcc`` (https://foss.heptapod.net/pypy/cffi/-/issues/480)
- ansible-test - convert target paths to unicode on Python 2 to avoid ``UnicodeDecodeError`` (https://github.com/ansible/ansible/issues/68398, https://github.com/ansible/ansible/pull/72623).
- ansible-test - ensure the correct unit test target is given when the ``__init__.py`` file is modified inside the connection plugins directory
- ansible-test - ensure unit test paths for connection and inventory plugins are correctly identified for collections (https://github.com/ansible/ansible/issues/73876).
- ansible-test - improve classification of changes to ``.gitignore``, ``COPYING``, ``LICENSE``, ``Makefile``, and all files ending with one of ``.in`, ``.md`, ``.rst``, ``.toml``, ``.txt`` in the collection root directory (https://github.com/ansible/ansible/pull/72353).
- ansible-test - integration and unit test change detection now works for filter, lookup and test plugins
- ansible-test now always uses the ``--python`` option for ``virtualenv`` to select the correct interpreter when creating environments with the ``--venv`` option
- ansible-test sanity changelog test - bump dependency on antsibull-changelog to 0.9.0 so that `fragments that add new plugins or objects <https://github.com/ansible-community/antsibull-changelog/blob/main/docs/changelogs.rst#adding-new-roles-playbooks-test-and-filter-plugins>`_ will not fail validation (https://github.com/ansible/ansible/pull/73428).
- ansible-test units - fixed collection location code to work under pytest >= 6.0.0
- ansible-test validate-modules - ``version_added`` on module level was not validated for modules in collections (https://github.com/ansible/ansible/pull/70869).
- ansible-test validate-modules - return correct error codes ``option-invalid-version-added`` resp. ``return-invalid-version-added`` instead of the wrong error ``deprecation-either-date-or-version`` when an invalid value of ``version_added`` is specified for an option or a return value (https://github.com/ansible/ansible/pull/70869).
- ansible-test validate-modules - when a module uses ``add_file_common_args=True`` and does not use a keyword argument for ``argument_spec`` in ``AnsibleModule()``, the common file arguments were not considered added during validation (https://github.com/ansible/ansible/pull/72334).
- ansible_pkg_mgr fact - now correctly returns ``atomic_container`` when run on "RHEL for Edge" images and Fedora/RHEL/CentOS Atomic Host (https://github.com/ansible/ansible/issues/73084).
- api - time.clock is removed in Python 3.8, add backward compatible code (https://github.com/ansible/ansible/issues/70649).
- apt - add ``fail_on_autoremove`` param to apt module to avoid unintended package removals (https://github.com/ansible/ansible/issues/63231)
- apt - fix policy_rc_d parameter throwing an exception when restoring original file (https://github.com/ansible/ansible/issues/66211)
- apt - include exception message from apt python library in error output
- apt_key - Specifying ``file`` as mutually exclusive with ``data``, ``keyserver``, ``url`` (https://github.com/ansible/ansible/pull/70492).
- apt_repository - fixes ``mode`` doc to remove ineffective default (https://github.com/ansible/ansible/pull/70319).
- argument spec validation - fix behavior of ``apply_defaults=True`` when an empty dictionary is specified for such an option (https://github.com/ansible/ansible/pull/74029).
- assemble - fix decrypt argument in the module (https://github.com/ansible/ansible/issues/65450).
- async - Fix Python 3 interpreter parsing from module by comparing with bytes (https://github.com/ansible/ansible/issues/70690)
- async_wrapper - Fix race condition when ``~/.ansible_async`` folder tries to be created by multiple async tasks at the same time - https://github.com/ansible/ansible/issues/59306
- avoid possible errors accessing os.environ by not assuming existance of variables.
- basic - handle exceptions for default selectors in Python 2.7 (https://github.com/ansible/ansible/issues/71704).
- basic - use PollSelector implementation when DefaultSelector fails (https://github.com/ansible/ansible/issues/70238).
- bcrypt hashing - Ensure we repair the salt, to avoid warnings (https://github.com/ansible/ansible/issues/36129)
- blockinfile - properly insert a block at the end of a file that does not have a trailing newline character (https://github.com/ansible/ansible/issues/72055)
- blockinfile now returns name of backup file when this option is used.
- clarified changed status to reflect existing rule that had never been written down.
- collection loader - fix bogus code coverage entries for synthetic packages
- collection metadata - ensure collection loader uses libyaml/CSafeLoader to parse collection metadata if available
- connection/ssh, ensure parameters come from correct source get_option, so functionality matches docs.
- connection/ssh, fix reset to use same parameters to check if socket exists as actually used, was hardcoded to default string construction previouslly.
- cron - cron file should not be empty after adding var (https://github.com/ansible/ansible/pull/71207)
- cron - encode and decode crontab files in UTF-8 explicitly to allow non-ascii chars in cron filepath and job (https://github.com/ansible/ansible/issues/69492)
- debug action, prevent setting facts when displaying ansible_facts.
- default callback - Ensure that the ``host_pinned`` strategy is not treated as lockstep (https://github.com/ansible/ansible/issues/73364)
- delegate_to - Ensure that calculating ``delegate_to`` vars with a loop uses the correct context to correctly evaluate the loop (https://github.com/ansible/ansible/issues/37132)
- display correct error information when an error exists in the last line of the file (https://github.com/ansible/ansible/issues/16456)
- distribution - add support for Pardus Linux distribution (https://github.com/ansible/ansible/issues/71636).
- distribution facts - Allow ``distribution_major_version`` and ``distribution_version`` to work for RC and PRERELEASE versions of FreeBSD (and derived distributions) (https://github.com/ansible/ansible/issues/72331).
- dnf - fix filtering to avoid dependncy conflicts (https://github.com/ansible/ansible/issues/72316)
- dnf - it is now possible to specify both ``security: true`` and ``bugfix: true`` to install updates of both types. Previously, only security would get installed if both were true. (https://github.com/ansible/ansible/issues/70854)
- ensure 'local' connection always has the correct default user for actions to consume.
- ensure delegated vars can resolve hostvars object and access vars from hostvars[inventory_hostname].
- ensure find_mount_point consistently returns text.
- ensure we don't clobber role vars data when getting an empty file
- expect - Operate pexpect with bytes to avoid potential encoding issues (https://github.com/ansible/ansible/issues/29351)
- facts - account for Slackware OS with ``+`` in the name (https://github.com/ansible/ansible/issues/38760)
- facts - fix distribution fact for SLES4SAP (https://github.com/ansible/ansible/pull/71559).
- facts - fix incorrect UTC timestamp in ``iso8601_micro`` and ``iso8601``
- facts - properly report virtualization facts for Linux guests running on bhyve (https://github.com/ansible/ansible/issues/73167)
- file - prevent link src from being rewritten when src is not specified explicitly (https://github.com/ansible/ansible/issues/65448)
- file - the module should warn in check_mode when path an owner/group don't exist (https://github.com/ansible/ansible/issues/67307).
- find module - Don't treat empty excludes as a match (https://github.com/ansible/ansible/issues/70640)
- find module - Stop traversing directories past the requested depth. (https://github.com/ansible/ansible/issues/73627)
- find module, fix default pattern when use_regex is true.
- fix issue with inventory_hostname and delegated host vars mixing on connection settings.
- fortimanager httpapi plugin - fix redirect to point to the ``fortinet.fortimanager`` collection (https://github.com/ansible/ansible/pull/71073).
- galaxy - handle plus sign in user token appearing in role url (https://github.com/ansible/ansible/issues/45475).
- get_sysctl now handles multiline values and does not die silently anymore.
- get_url - skip checksum during ``--check`` (https://github.com/ansible/ansible/issues/61369).
- git - Only pass ``--raw`` flag to git verify commands (verify-tag, verify-commit) when ``gpg_whitelist`` is in use. Otherwise don't pass it so that non-whitelist GPG validation still works on older Git versions. (https://github.com/ansible/ansible/issues/64469)
- gluster modules - fix redirect to point to the ``gluster.gluster`` collection (https://github.com/ansible/ansible/pull/71240).
- hostname - Fixed an issue where the hostname on the alinux could not be set.
- hostname - add Almalinux support (https://github.com/ansible/ansible/pull/73619)
- hostname - add macOS support (https://github.com/ansible/ansible/pull/54439)
- if the ``type`` for a module parameter in the argument spec is callable, do not pass ``kwargs`` to avoid errors (https://github.com/ansible/ansible/issues/70017)
- import_playbook - change warning about extra parameters to deprecation (https://github.com/ansible/ansible/issues/72745)
- improve deprecation message when using bare variable (https://github.com/ansible/ansible/pull/70687)
- inventory - pass the vars dictionary to combine_vars instead of an individual key's value (https://github.com/ansible/ansible/issues/72975).
- inventory plugins - Let plugins define the sanitization method for the constructed ``groups`` feature.
- inventory_hostnames - Use ``InventoryManager`` instead of trying to replicate its behavior (https://github.com/ansible/ansible/issues/17268)
- is_string/vault - Ensure the is_string helper properly identifies AnsibleVaultEncryptedUnicode as a string (https://github.com/ansible/ansible/pull/71609)
- j2 plugin loader clarified comments, made note with better fqcn detection.
- lineinfile - fix not subscriptable error in exception handling around file creation
- linux network facts - get the correct value for broadcast address (https://github.com/ansible/ansible/issues/64384)
- native jinja2 types - properly handle Undefined in nested data.
- notify keyword is not ignored anymore on import_tasks, also able to apply to blocks now.
- package - use list of built in package managers from facts rather than creating a new list
- paramiko connection plugin - Ensure we only reset the connection when one has been previously established (https://github.com/ansible/ansible/issues/65812)
- password hashing - Ensure we validate salts against allowed characters and length when using ``crypt`` (https://github.com/ansible/ansible/issues/71107)
- password lookup - Try to automatically generate salts using known salt sizes (https://github.com/ansible/ansible/issues/53750)
- pause - Fix indefinite hang when using a pause task on a background process (https://github.com/ansible/ansible/issues/32142)
- pause - catch additional error on setting up curses (https://github.com/ansible/ansible/pull/73588).
- pause - do not accept enter to continue when a timeout is set (https://github.com/ansible/ansible/issues/73948)
- pause - do not warn when running in the background if a timeout is provided (https://github.com/ansible/ansible/issues/73042)
- pause - handle exception when there is no stdout (https://github.com/ansible/ansible/pull/47851)
- powershell - fix escaping of strings that broken modules like fetch when dealing with special chars - https://github.com/ansible/ansible/issues/62781
- powershell - fix the CLIXML parser when it contains nested CLIXML objects - https://github.com/ansible/ansible/issues/69550
- powershell - remove getting the PowerShell version from the env var ``POWERSHELL_VERSION``. This feature never worked properly and can cause conflicts with other libraries that use this var
- psrp - Fix hang when copying an empty file to the remote target
- psrp - Use native PSRP mechanism when copying files to support custom endpoints
- quote filter - normalize how ``None`` is handled, to match Python3 behavior (https://github.com/ansible/ansible/issues/32174)
- reboot - Add support for the runit init system, used on Void Linux, that does not support the normal Linux syntax.
- remove contradictory recomendation from template docs. https://github.com/ansible/ansible/issues/63484
- remove redundant remote_user setting in play_context for local as plugin already does it, also removes fork/thread issue from use of pwd library.
- reset logging level to INFO due to CVE-2019-14846.
- restrict module valid JSON parsed output to objects as lists are not valid responses.
- runas - create a new token when running as ``SYSTEM`` to ensure it has the full privileges assigned to that account
- service - Fix for the BSD rcconf code using a Python 2 specific string replace function
- set_mode_if_different - handle symlink if it is inside a directory with sticky bit set (https://github.com/ansible/ansible/pull/45198)
- setup module, fix error handling on bad subset given
- setup, don't give up on all local facts gathering if one script file fails.
- several fixes to make apt_key better at identifying needs for change and also to avoid changes in check_mode.
- shell - fix quoting of mkdir command in creation of remote_tmp in order to allow spaces and other special characters (https://github.com/ansible/ansible/issues/69577).
- splunk httpapi plugin - switch from splunk.enterprise_security to splunk.es in runtime.yml to reflect upstream change of Collection Name
- ssh connection plugin - use ``get_option()`` rather than ``_play_context`` to ensure ``ANSBILE_SSH_ARGS`` are applied properly (https://github.com/ansible/ansible/issues/70437)
- stat - handle colons in filename while parsing the mimetype output (https://github.com/ansible/ansible/issues/70256).
- strftime filter - Input epoch is allowed to be a float (https://github.com/ansible/ansible/issues/71257)
- su become plugin, ensure correct type for localization option.
- systemd - account for templated unit files using ``@`` when searching for the unit file (https://github.com/ansible/ansible/pull/72347#issuecomment-730626228)
- systemd - fixed chroot usage on new versions of systemd, that broke because of upstream changes in systemctl output
- systemd - follow up fix to https://github.com/ansible/ansible/issues/72338 to use ``list-unit-files`` rather than ``list-units`` in order to show all units files on the system.
- systemd - made the systemd module work correctly when the SYSTEMD_OFFLINE environment variable is set
- systemd - preserve the full unit name when using a templated service and ``systemd`` failed to parse dbus due to a known bug in ``systemd`` (https://github.com/ansible/ansible/pull/72985)
- systemd - work around bug with ``systemd`` 245 and 5.8 kernel that does not correctly report service state (https://github.com/ansible/ansible/issues/71528)
- task parsing - strip spaces from action name when using ``action: foo bar=baz`` form. (https://github.com/ansible/ansible/issues/62136)
- templating - fix error message for ``x in y`` when y is undefined (https://github.com/ansible/ansible/issues/70984)
- the unvault lookup plugin returned a byte string. Now returns a real string.
- to_text(stdout) before json.loads in psrp.Connection.put_file in case stdout is bytes
- unarchive - ``zip`` unarchive no longer errors on RHEL/CentOS 6 and old Fedora when attempting to use a numeric gid (https://github.com/ansible/ansible/issues/71903).
- unarchive - check ``fut_gid`` against ``run_gid`` in addition to supplemental groups (https://github.com/ansible/ansible/issues/49284)
- undeprecate hash_merge setting and add more docs clarifying its use and why not to use it.
- uri - ``status_code`` elements are type ``int``
- url lookup - make sure that options supplied in ansible.cfg are actually used (https://github.com/ansible/ansible/pull/71736).
- url lookup - set default user agent to ``ansible-httpget`` (https://github.com/ansible/ansible/pull/72324)
- urls - Close filedescriptor of certificate chain tempfile to prevent stale filedescriptor leakage (https://github.com/ansible/ansible/pull/71825).
- user - AnsibleModule.run_command returns a tuple of return code, stdout and stderr. The module main function of the user module expects user.create_user to return a tuple of return code, stdout and stderr. Fix the locations where stdout and stderr got reversed.
- user - Local users with an expiry date cannot be created as the ``luseradd`` / ``lusermod`` commands do not support the ``-e`` option. Set the expiry time in this case via ``lchage`` after the user was created / modified. (https://github.com/ansible/ansible/issues/71942)
- user - do the right thing when ``password_lock=True`` and ``password`` are used together (https://github.com/ansible/ansible/issues/72992)
- user - don't create home directory and missing parents when create_home == false (https://github.com/ansible/ansible/pull/70600).
- validate-modules - do not raise an ``AttributeError`` if a value is assigned to a module attribute in a try/except block.
- vault - Support reading raw binary data from stdin under python3
- virtual facts - kubevirt is now identified as "KubeVirt" and with a "guest" role instead of "kvm" and "host" role (https://github.com/ansible/ansible/issues/72001).
- wait_for - catch and ignore errors when getting active connections with psutil (https://github.com/ansible/ansible/issues/72322)
- wait_for module, move missing socket into function to get proper comparrison in time.
- win setup - Fix redirection path for the windows setup module
- windows async - use full path when calling PowerShell to reduce reliance on environment vars being correct - https://github.com/ansible/ansible/issues/70655
- winrm - preserve winrm forensic data on put_file failures
- yamllint - do not raise an ``AttributeError`` if a value is assigned to a module attribute at the top of the module.

amazon.aws
~~~~~~~~~~

- ec2_vol - a creation or update now returns a structure with an up to date list of tags (https://github.com/ansible-collections/amazon.aws/pull/241).
- ec2_vol - create or update now preserves the existing tags, including Name (https://github.com/ansible-collections/amazon.aws/issues/229)
- ec2_vol - fix exception when platform information isn't available (https://github.com/ansible-collections/amazon.aws/issues/305).

ansible.netcommon
~~~~~~~~~~~~~~~~~

- Allow setting `host_key_checking` through a play/task var for `network_cli`.
- Ensure passed-in terminal_initial_prompt and terminal_initial_answer values are cast to bytes before using
- Expose connection class object to rm_template (https://github.com/ansible-collections/ansible.netcommon/pull/180)
- Fix cli_parse issue with parsers in utils collection (https://github.com/ansible-collections/ansible.netcommon/pull/270)
- Support single_user_mode with Ansible 2.9.
- Update valid documentation for net_ping module.
- ncclient - catch and handle exception to prevent stack trace when running in FIPS mode
- net_put - Remove temp file created when file already exist on destination when mode is 'text'.
- network_cli - When using ssh_type libssh, handle closed connection gracefully instead of throwing an exception

ansible.posix
~~~~~~~~~~~~~

- at - add AIX support (https://github.com/ansible-collections/ansible.posix/pull/99).
- synchronize - add ``community.docker.docker`` to the list of supported transports (https://github.com/ansible-collections/ansible.posix/issues/132).
- synchronize - do not prepend PWD when path is in form user@server:path or server:path (https://github.com/ansible-collections/ansible.posix/pull/118).
- synchronize - fix for private_key overriding in synchronize module.
- sysctl - do not persist sysctl when value is invalid (https://github.com/ansible-collections/ansible.posix/pull/101).

ansible.utils
~~~~~~~~~~~~~

- Add missing test requirements (https://github.com/ansible-collections/ansible.utils/pull/57).
- Fix ansible.utils.cli_parse action plugin to support old cli_parse sub-plugin structure in ansible.netcommon collection.
- Fix cli_parse template_path read error (https://github.com/ansible-collections/ansible.utils/pull/51).
- Fix jsonschema input data format checking (https://github.com/ansible-collections/ansible.utils/pull/50).

ansible.windows
~~~~~~~~~~~~~~~

- setup - Return correct epoch integer value for the ``ansible_date_time.epoch_int`` fact
- win_package - fix msi detection when the msi product is already installed under a different version - https://github.com/ansible-collections/ansible.windows/issues/166
- win_package - treat a missing ``creates_path`` when ``creates_version`` as though the package was not installed instead of a failure - https://github.com/ansible-collections/ansible.windows/issues/169
- win_template - Fix changed internal API that win_template uses to work with devel again
- win_user - Compare existing vs desired groups in a case insenstive way - https://github.com/ansible-collections/ansible.windows/issues/168

arista.eos
~~~~~~~~~~

- Add 'virtual' key to denote the existence of virtual address on an interface.(https://github.com/ansible-collections/arista.eos/pull/170).
- Add _remove_config before starting every integration test.
- Fixed the regex to parse the running config correctly.(https://github.com/ansible-collections/arista.eos/issues/150)
- Modify the split pattern while checking for eapi url in eos_eapi.
- Normalize interface name before any operaion.
- Skip when there are alpha values present following vlan keyword.
- cliconf plugin - Prevent `get_capabilities()` from getting larger every time it is called
- galaxy.yml - change wrong dependency ``ansible.netcommon`` from ``2.0.0`` to ``>= 2.0.0`` (https://github.com/ansible-collections/overview/issues/43).

chocolatey.chocolatey
~~~~~~~~~~~~~~~~~~~~~

- All modules - Added fallback to default choco install path for auxiliary modules to workaround issue in OpenSSH library under Windows. (https://github.com/PowerShell/Win32-OpenSSH#1329)
- win_chocolatey - Module can now handle uninstallation correctly for both side-by-side and normal package installations.

cisco.asa
~~~~~~~~~

- Added save_when param support in asa_config module (https://github.com/ansible-collections/cisco.asa/pull/75).
- To fix ASA acls module where replace wasn't working as expected (https://github.com/ansible-collections/cisco.asa/pull/92).
- To fix Cisco ASA network_object object config which wasn't working as expected (https://github.com/ansible-collections/cisco.asa/pull/103).

cisco.ios
~~~~~~~~~

- Doc update to update users WRT to idempotence issue in ios_logging when logging is ON (https://github.com/ansible-collections/cisco.ios/pull/287).
- PR to fix ios_l2_interfaces issue where it wasn't working with range of vlans as expected (https://github.com/ansible-collections/cisco.ios/pull/264).
- To add support for TwoGigabitEthernet interface option from IOS standpoint (https://github.com/ansible-collections/cisco.ios/pull/262).
- To fix ios_acls Nonetype error when aces are empty (https://github.com/ansible-collections/cisco.ios/pull/260).
- To fix ios_acls log and log_input params (https://github.com/ansible-collections/cisco.ios/pull/265).
- To fix ios_acls parsed state example under module doc (https://github.com/ansible-collections/cisco.ios/pull/244).
- To fix ios_acls resource module acl_name traceback over some switches (https://github.com/ansible-collections/cisco.ios/pull/285).
- To fix ios_vlans traceback error when empty line with just Ports information is available in config (https://github.com/ansible-collections/cisco.ios/pull/273).
- fix error when comparing two vlan using string instead of the int value (https://github.com/ansible-collections/cisco.ios/pull/249).

cisco.iosxr
~~~~~~~~~~~

- Add fix for interfaces which are not in running config should get merged when state is merged. (https://github.com/ansible-collections/cisco.iosxr/issues/106)
- Avoid using default value for comment for iosxr version > 7.2(Module=iosxr_config)
- Avoid using default value for comment when "comment is not supported" by device.
- Fix to accurately report configuration failure during pseudo-atomic operation fior iosxr-6.6.3 (https://github.com/ansible-collections/cisco.iosxr/issues/92).
- For versions >=2.0.1, this collection requires ansible.netcommon >=2.0.1.
- Re-releasing this collection with ansible.netcommon dependency requirements updated.
- Update valid hostname info in iosxr_facs using show running-conf hostname command. (https://github.com/ansible-collections/cisco.iosxr/issues/103)

cisco.meraki
~~~~~~~~~~~~

- meraki_mx_content_filtering - Fix crash with idempotent condition due to improper sorting

cisco.nxos
~~~~~~~~~~

- Allow commands to be properly generated with Jinja2 2.10.3 (workaround for https://github.com/pallets/jinja/issues/710).
- Allow integer values to be set for dscp key (https://github.com/ansible-collections/cisco.nxos/issues/253).
- Do not fail when parsing non rule entries in access-list config (https://github.com/ansible-collections/cisco.nxos/issues/262).
- Fail gracefully when BGP is already configured with a different ASN when states merged or replaced is used.
- Fixes to nxos_logging, nxos_igmp_snooping, nxos_l3_interfaces, nxos_ospf_interfaces and nxos_static_routes to conform with latest CLI behaviour.
- For versions >=2.1.0, this collection requires ansible.netcommon >=2.0.1.
- Properly configure neighbor timers and shutdown state (https://github.com/ansible-collections/cisco.nxos/issues/240).
- Re-releasing this collection with ansible.netcommon dependency requirements updated.

community.aws
~~~~~~~~~~~~~

- aws_kms - fixes issue where module execution fails without the kms:GetKeyRotationStatus permission. (https://github.com/ansible-collections/community.aws/pull/200).
- aws_kms_info - ensure that searching by tag works when tag only exists on some CMKs (https://github.com/ansible-collections/community.aws/issues/276).
- aws_s3_cors - fix element type for rules parameter. (https://github.com/ansible-collections/community.aws/pull/408).
- aws_ssm - Adds destructor to SSM connection plugin to ensure connections are properly cleaned up after usage (https://github.com/ansible-collections/community.aws/pull/542).
- aws_ssm - enable aws ssm connections if **AWS_SESSION_TOKEN** is missing (https://github.com/ansible-collections/community.aws/pull/535).
- aws_ssm - fix the generation of CURL URL used to download Ansible Python file from S3 bucket by ```_get_url()``` due to due to non-assignment of aws region in the URL and not using V4 signature as specified for AWS S3 signature URL by ```_get_boto_client()``` in (https://github.com/ansible-collections/community.aws/pull/352).
- aws_ssm - fixed ``UnicodeEncodeError`` error when using unicode file names (https://github.com/ansible-collections/community.aws/pull/295).
- cloudtrail - fix always reporting changed = true when kms alias used (https://github.com/ansible-collections/community.aws/pull/506).
- cloudtrail - fix lower casing of tag keys (https://github.com/ansible-collections/community.aws/pull/506).
- ec2_asg - fix target group update logic (https://github.com/ansible-collections/community.aws/pull/493).
- ec2_eip - fix eip association by instance id & private ip address due to case-sensitivity of the ``PrivateIpAddress`` parameter (https://github.com/ansible-collections/community.aws/pull/328).
- ec2_instance - ensure that termination protection isn't modified when using check_mode (https://github.com/ansible/ansible/issues/67716).
- ec2_instance - fix key errors when instance has no tags (https://github.com/ansible-collections/community.aws/pull/476).
- ec2_launch_template - ensure that empty parameters are properly removed before passing to AWS (https://github.com/ansible-collections/community.aws/issues/230).
- ec2_launch_template - fixes parameter validation failure when passing a instance profile ARN instead of just the role name (https://github.com/ansible-collections/community.aws/pull/371).
- ec2_vpc_endpoint - ensure ``changed`` is correctly set when deleting an endpoint (https://github.com/ansible-collections/community.aws/pull/362).
- ec2_vpc_endpoint - fix exception when attempting to delete an endpoint which has already been deleted (https://github.com/ansible-collections/community.aws/pull/362).
- ec2_vpc_peer - fix idempotency when rejecting and deleting peering connections (https://github.com/ansible-collections/community.aws/pull/501).
- ec2_vpc_route_table - catch RouteAlreadyExists error when rerunning same task twice to make module idempotent (https://github.com/ansible-collections/community.aws/issues/357).
- ecs_task - use `required_if` to enforce mandatory parameters based on specified operation (https://github.com/ansible-collections/community.aws/pull/402).
- elasticache - Fix ``KeyError`` issue when updating security group (https://github.com/ansible-collections/community.aws/pull/410).
- elb_application_lb - during the removal of an instance, the associated listeners are also removed.
- kinesis_stream - fixed issue where streams get marked as changed even if no encryption actions were necessary (https://github.com/ansible/ansible/issues/65928).
- rds_instance - fixes bug preventing the use of tags when creating an RDS instance from a snapshot (https://github.com/ansible-collections/community.aws/issues/530).
- route53 - ensure that the old return values are re-added along side the new ones (https://github.com/ansible-collections/community.aws/issues/523).
- route53 - fix ``AttributeError`` in ``get_zone_id_by_name`` when a vpc_id on a private zone is provided (https://github.com/ansible-collections/community.aws/issues/509).
- route53 - fix handling for characters escaped by AWS in record names, like ``*`` and ``@``. This fixes idempotency for such record names (https://github.com/ansible-collections/community.aws/issues/524).
- route53 - fix when using ``state=get`` on private DNS zones and add tests to cover this scenario (https://github.com/ansible-collections/community.aws/pull/424).
- route53 - make sure that CAA values order is again ignored during idempotency comparsion (https://github.com/ansible-collections/community.aws/issues/524).
- sns_topic - Add ``+`` to allowable characters in SMS endpoints (https://github.com/ansible-collections/community.aws/pull/454).
- sqs_queue - fix UnboundLocalError when passing a boolean parameter (https://github.com/ansible-collections/community.aws/issues/172).

community.crypto
~~~~~~~~~~~~~~~~

- acme_* modules - avoid crashing for ACME servers where the ``meta`` directory key is not present (https://github.com/ansible-collections/community.crypto/issues/220, https://github.com/ansible-collections/community.crypto/pull/221).
- acme_* modules - fix wrong usages of ``ACMEProtocolException`` (https://github.com/ansible-collections/community.crypto/pull/216, https://github.com/ansible-collections/community.crypto/pull/217).
- action_module plugin helper - make compatible with latest changes in ansible-core 2.11.0b3 (https://github.com/ansible-collections/community.crypto/pull/202).
- openssl_csr - no longer fails when comparing CSR without basic constraint when ``basic_constraints`` is specified (https://github.com/ansible-collections/community.crypto/issues/179, https://github.com/ansible-collections/community.crypto/pull/180).
- openssl_privatekey_pipe - make compatible with latest changes in ansible-core 2.11.0b3 (https://github.com/ansible-collections/community.crypto/pull/202).

community.digitalocean
~~~~~~~~~~~~~~~~~~~~~~

- digital_ocean_certificate_info - fix retrieving certificate by ID (https://github.com/ansible-collections/community.digitalocean/issues/35).
- digital_ocean_domain - module is now idempotent when called without IP (https://github.com/ansible-collections/community.digitalocean/issues/21).
- digital_ocean_load_balancer_info - fix retrieving load balancer by ID (https://github.com/ansible-collections/community.digitalocean/issues/35).
- digitalocean - Drop collection version from README.md (https://github.com/ansible-collections/community.digitalocean/issues/63).

community.docker
~~~~~~~~~~~~~~~~

- ``docker_swarm_service`` - fix KeyError on caused by reference to deprecated option ``update_failure_action`` (https://github.com/ansible-collections/community.docker/pull/100).
- all modules - use ``to_native`` to convert exceptions to strings (https://github.com/ansible-collections/community.docker/pull/121).
- docker_container - fix healthcheck disabling idempotency issue with strict comparison (https://github.com/ansible-collections/community.docker/issues/85).
- docker_image - prevent module failure when removing image that is removed between inspection and removal (https://github.com/ansible-collections/community.docker/pull/87).
- docker_image - prevent module failure when removing non-existant image by ID (https://github.com/ansible-collections/community.docker/pull/87).
- docker_image_info - prevent module failure when image vanishes between listing and inspection (https://github.com/ansible-collections/community.docker/pull/87).
- docker_image_info - prevent module failure when querying non-existant image by ID (https://github.com/ansible-collections/community.docker/pull/87).
- docker_swarm_service - mark ``secrets`` module option with ``no_log=False`` since it does not leak secrets (https://github.com/ansible-collections/community.general/pull/2001).

community.general
~~~~~~~~~~~~~~~~~

- Mark various module options with ``no_log=False`` which have a name that potentially could leak secrets, but which do not (https://github.com/ansible-collections/community.general/pull/2001).
- aerospike_migration - fix typo that caused ``migrate_tx_key`` instead of ``migrate_rx_key`` being used (https://github.com/ansible-collections/community.general/pull/1739).
- alternatives - internal refactoring: replaced uses of ``_`` with ``dummy`` (https://github.com/ansible-collections/community.general/pull/1819).
- beadm - internal refactoring: replaced uses of ``_`` with ``dummy`` (https://github.com/ansible-collections/community.general/pull/1819).
- bigpanda - actually use the ``deployment_message`` option (https://github.com/ansible-collections/community.general/pull/1928).
- chef_databag lookup plugin - wrapped usages of ``dict.keys()`` in ``list()`` for Python 3 compatibility (https://github.com/ansible-collections/community.general/pull/1861).
- cloudforms inventory - fixed issue that non-existing (archived) VMs were synced (https://github.com/ansible-collections/community.general/pull/720).
- cobbler_sync, cobbler_system - fix SSL/TLS certificate check when ``validate_certs`` set to ``false`` (https://github.com/ansible-collections/community.general/pull/1880).
- composer - use ``no-interaction`` option when discovering available options to avoid an issue where composer hangs (https://github.com/ansible-collections/community.general/pull/2348).
- consul_io inventory script - kv_groups - fix byte chain decoding for Python 3 (https://github.com/ansible-collections/community.general/pull/620).
- cronvar - internal refactoring: replaced uses of ``_`` with ``dummy`` (https://github.com/ansible-collections/community.general/pull/1819).
- dconf - internal refactoring: replaced uses of ``_`` with ``dummy`` (https://github.com/ansible-collections/community.general/pull/1819).
- deploy_helper - allow ``state=clean`` to be used without defining a ``release`` (https://github.com/ansible-collections/community.general/issues/1852).
- dimensiondata_network - bug when formatting message, instead of % a simple comma was used (https://github.com/ansible-collections/community.general/pull/2139).
- diy callback plugin - wrapped usages of ``dict.keys()`` in ``list()`` for Python 3 compatibility (https://github.com/ansible-collections/community.general/pull/1861).
- elasticsearch_plugin - ``state`` parameter choices must use ``list()`` in python3 (https://github.com/ansible-collections/community.general/pull/1830).
- filesystem - do not fail when ``resizefs=yes`` and ``fstype=xfs`` if there is nothing to do, even if the filesystem is not mounted. This only covers systems supporting access to unmounted XFS filesystems. Others will still fail (https://github.com/ansible-collections/community.general/issues/1457, https://github.com/ansible-collections/community.general/pull/1478).
- filesystem - internal refactoring: replaced uses of ``_`` with ``dummy`` (https://github.com/ansible-collections/community.general/pull/1819).
- filesystem - remove ``swap`` from list of FS supported by ``resizefs=yes`` (https://github.com/ansible-collections/community.general/issues/790).
- funcd connection plugin - can now load (https://github.com/ansible-collections/community.general/pull/2235).
- git_config - fixed scope ``file`` behaviour and added integraton test for it (https://github.com/ansible-collections/community.general/issues/2117).
- git_config - prevent ``run_command`` from expanding values (https://github.com/ansible-collections/community.general/issues/1776).
- github_repo - PyGithub bug does not allow explicit port in ``base_url``. Specifying port is not required (https://github.com/PyGithub/PyGithub/issues/1913).
- gitlab_runner - parameter ``registration_token`` was required but is used only when ``state`` is ``present`` (https://github.com/ansible-collections/community.general/issues/1714).
- gitlab_user - make updates to the ``isadmin``, ``password`` and ``confirm`` options of an already existing GitLab user work (https://github.com/ansible-collections/community.general/pull/1724).
- haproxy - fix a bug preventing haproxy from properly entering ``DRAIN`` mode (https://github.com/ansible-collections/community.general/issues/1913).
- hiera lookup plugin - converts the return type of plugin to unicode string (https://github.com/ansible-collections/community.general/pull/2329).
- hipchat - internal refactoring: replaced uses of ``_`` with ``dummy`` (https://github.com/ansible-collections/community.general/pull/1819).
- idrac_redfish_command - wrapped usages of ``dict.keys()`` in ``list()`` for Python 3 compatibility (https://github.com/ansible-collections/community.general/pull/1861).
- idrac_redfish_config - wrapped usages of ``dict.keys()`` in ``list()`` for Python 3 compatibility (https://github.com/ansible-collections/community.general/pull/1861).
- idrac_redfish_info - wrapped usages of ``dict.keys()`` in ``list()`` for Python 3 compatibility (https://github.com/ansible-collections/community.general/pull/1861).
- imc_rest - explicitly logging out instead of registering the call in ```atexit``` (https://github.com/ansible-collections/community.general/issues/1735).
- influxdb_retention_policy - ensure idempotent module execution with different duration and shard duration parameter values (https://github.com/ansible-collections/community.general/issues/2281).
- influxdb_retention_policy - fix bug where ``INF`` duration values failed parsing (https://github.com/ansible-collections/community.general/pull/2385).
- infoblox inventory script - make sure that the script also works with Ansible 2.9, and returns a more helpful error when community.general is not installed as part of Ansible 2.10/3 (https://github.com/ansible-collections/community.general/pull/1871).
- ini_file - allows an empty string as a value for an option (https://github.com/ansible-collections/community.general/pull/1972).
- interfaces_file - internal refactoring: replaced uses of ``_`` with ``dummy`` (https://github.com/ansible-collections/community.general/pull/1819).
- inventory and vault scripts - change file permissions to make vendored inventory and vault scripts exectuable (https://github.com/ansible-collections/community.general/pull/2337).
- ipa_user - allow ``sshpubkey`` to permit multiple word comments (https://github.com/ansible-collections/community.general/pull/2159).
- iso_extract - use proper alias deprecation mechanism for ``thirsty`` alias of ``force`` (https://github.com/ansible-collections/community.general/pull/1830).
- java_cert - allow setting ``state: absent`` by providing just the ``cert_alias`` (https://github.com/ansible/ansible/issues/27982).
- java_cert - internal refactoring: replaced uses of ``_`` with ``dummy`` (https://github.com/ansible-collections/community.general/pull/1819).
- java_cert - properly handle proxy arguments when the scheme is provided (https://github.com/ansible/ansible/issues/54481).
- java_keystore - improve error handling and return ``cmd`` as documented. Force ``LANG``, ``LC_ALL`` and ``LC_MESSAGES`` environment variables to ``C`` to rely on ``keytool`` output parsing. Fix pylint's ``unused-variable`` and ``no-else-return`` hints (https://github.com/ansible-collections/community.general/pull/2183).
- java_keystore - use tempfile lib to create temporary files with randomized names, and remove the temporary PKCS#12 keystore as well as other materials (https://github.com/ansible-collections/community.general/issues/1667).
- jenkins_plugin - fixes Python 2 compatibility issue (https://github.com/ansible-collections/community.general/pull/2340).
- jira - fixed calling of ``isinstance`` (https://github.com/ansible-collections/community.general/issues/2234).
- jira - fixed error when loading base64-encoded content as attachment (https://github.com/ansible-collections/community.general/pull/2349).
- jira - fixed fields' update in ticket transitions (https://github.com/ansible-collections/community.general/issues/818).
- kibana_plugin - ``state`` parameter choices must use ``list()`` in python3 (https://github.com/ansible-collections/community.general/pull/1830).
- kibana_plugin - added missing parameters to ``remove_plugin`` when using ``state=present force=true``, and fix potential quoting errors when invoking ``kibana`` (https://github.com/ansible-collections/community.general/pull/2143).
- linode_v4 - changed the error message to point to the correct bugtracker URL (https://github.com/ansible-collections/community.general/pull/2430).
- logstash_plugin - wrapped ``dict.keys()`` with ``list`` for use in ``choices`` setting (https://github.com/ansible-collections/community.general/pull/1830).
- lvg - internal refactoring: replaced uses of ``_`` with ``dummy`` (https://github.com/ansible-collections/community.general/pull/1819).
- lvol - fixed rounding errors (https://github.com/ansible-collections/community.general/issues/2370).
- lvol - fixed size unit capitalization to match units used between different tools for comparison (https://github.com/ansible-collections/community.general/issues/2360).
- lvol - fixed sizing calculation rounding to match the underlying tools (https://github.com/ansible-collections/community.general/issues/1988).
- lvol - internal refactoring: replaced uses of ``_`` with ``dummy`` (https://github.com/ansible-collections/community.general/pull/1819).
- lxc - internal refactoring: replaced uses of ``_`` with ``dummy`` (https://github.com/ansible-collections/community.general/pull/1819).
- lxc_container - internal refactoring: replaced uses of ``_`` with ``dummy`` (https://github.com/ansible-collections/community.general/pull/1819).
- lxc_container - wrapped usages of ``dict.keys()`` in ``list()`` for Python 3 compatibility (https://github.com/ansible-collections/community.general/pull/1861).
- lxd_container - wrapped usages of ``dict.keys()`` in ``list()`` for Python 3 compatibility (https://github.com/ansible-collections/community.general/pull/1861).
- manageiq_provider - wrapped ``dict.keys()`` with ``list`` for use in ``choices`` setting (https://github.com/ansible-collections/community.general/pull/1970).
- memcached cache plugin - wrapped usages of ``dict.keys()`` in ``list()`` for Python 3 compatibility (https://github.com/ansible-collections/community.general/pull/1861).
- meta/runtime.yml - improve deprecation messages (https://github.com/ansible-collections/community.general/pull/1918).
- module_helper module utils - actually ignoring formatting of parameters with value ``None`` (https://github.com/ansible-collections/community.general/pull/2024).
- module_helper module utils - fixed decorator ``cause_changes`` (https://github.com/ansible-collections/community.general/pull/2203).
- module_helper module utils - handling ``ModuleHelperException`` now properly calls ``fail_json()`` (https://github.com/ansible-collections/community.general/pull/2024).
- module_helper module utils - use the command name as-is in ``CmdMixin`` if it fails ``get_bin_path()`` - allowing full path names to be passed (https://github.com/ansible-collections/community.general/pull/2024).
- net_tools.nios.api module_utils - wrapped usages of ``dict.keys()`` in ``list()`` for Python 3 compatibility (https://github.com/ansible-collections/community.general/pull/1861).
- nios* modules - fix modules to work with ansible-core 2.11 (https://github.com/ansible-collections/community.general/pull/2057).
- nios_host_record - allow DNS Bypass for views other than default (https://github.com/ansible-collections/community.general/issues/1786).
- nmap inventory plugin - fix cache and constructed group support (https://github.com/ansible-collections/community.general/issues/2242).
- nmcli - add ``method4`` and ``method6`` options (https://github.com/ansible-collections/community.general/pull/1894).
- nmcli - compare MAC addresses case insensitively to fix idempotency issue (https://github.com/ansible-collections/community.general/issues/2409).
- nmcli - ensure the ``slave-type`` option is passed to ``nmcli`` for type ``bond-slave`` (https://github.com/ansible-collections/community.general/pull/1882).
- nmcli - if type is ``bridge-slave`` add ``slave-type bridge`` to ``nmcli`` command (https://github.com/ansible-collections/community.general/issues/2408).
- nomad_job_info - fix module failure when nomad client returns no jobs (https://github.com/ansible-collections/community.general/pull/1721).
- nsot inventory script - wrapped usages of ``dict.keys()`` in ``list()`` for Python 3 compatibility (https://github.com/ansible-collections/community.general/pull/1861).
- oci_vcn - wrapped usages of ``dict.keys()`` in ``list()`` for Python 3 compatibility (https://github.com/ansible-collections/community.general/pull/1861).
- one_vm - Allow missing NIC keys (https://github.com/ansible-collections/community.general/pull/2435).
- oneandone_monitoring_policy - wrapped usages of ``dict.keys()`` in ``list()`` for Python 3 compatibility (https://github.com/ansible-collections/community.general/pull/1861).
- packet_volume_attachment - removed extraneous ``print`` call - old debug? (https://github.com/ansible-collections/community.general/pull/1970).
- parted - change the regex that decodes the partition size to better support different formats that parted uses. Change the regex that validates parted's version string (https://github.com/ansible-collections/community.general/pull/1695).
- parted - internal refactoring: replaced uses of ``_`` with ``dummy`` (https://github.com/ansible-collections/community.general/pull/1819).
- pkgutil - fixed calls to ``list.extend()`` (https://github.com/ansible-collections/community.general/pull/2161).
- proxmox - removed requirement that root password is provided when containter state is ``present`` (https://github.com/ansible-collections/community.general/pull/1999).
- proxmox inventory - added handling of commas in KVM agent configuration string (https://github.com/ansible-collections/community.general/pull/2245).
- proxmox inventory - added handling of extra trailing slashes in the URL (https://github.com/ansible-collections/community.general/pull/1914).
- proxmox inventory - exclude qemu templates from inclusion to the inventory via pools (https://github.com/ansible-collections/community.general/issues/1986, https://github.com/ansible-collections/community.general/pull/1991).
- proxmox inventory plugin - allowed proxomox tag string to contain commas when returned as fact (https://github.com/ansible-collections/community.general/pull/1949).
- proxmox inventory plugin - support network interfaces without IP addresses, multiple network interfaces and unsupported/commanddisabled guest error (https://github.com/ansible-collections/community.general/pull/2263).
- proxmox lxc - only add the features flag when module parameter ``features`` is set. Before an empty string was send to proxmox in case the parameter was not used, which required to use ``root@pam`` for module execution (https://github.com/ansible-collections/community.general/pull/1763).
- proxmox* modules - refactored some parameter validation code into use of ``env_fallback``, ``required_if``, ``required_together``, ``required_one_of`` (https://github.com/ansible-collections/community.general/pull/1765).
- proxmox_kvm - do not add ``args`` if ``proxmox_default_behavior`` is set to no_defaults  (https://github.com/ansible-collections/community.general/issues/1641).
- proxmox_kvm - fix parameter ``vmid`` passed twice to ``exit_json`` while creating a virtual machine without cloning (https://github.com/ansible-collections/community.general/issues/1875, https://github.com/ansible-collections/community.general/pull/1895).
- proxmox_kvm - fix undefined local variable ``status`` when the parameter ``state`` is either ``stopped``, ``started``, ``restarted`` or ``absent`` (https://github.com/ansible-collections/community.general/pull/1847).
- proxmox_kvm - stop implicitly adding ``force`` equal to ``false``. Proxmox API requires not implemented parameters otherwise, and assumes ``force`` to be ``false`` by default anyways (https://github.com/ansible-collections/community.general/pull/1783).
- puppet - replace ``console` with ``stdout`` in ``logdest`` option when ``all`` has been chosen (https://github.com/ansible-collections/community.general/issues/1190).
- redfish_command - wrapped usages of ``dict.keys()`` in ``list()`` for Python 3 compatibility (https://github.com/ansible-collections/community.general/pull/1861).
- redfish_config - wrapped usages of ``dict.keys()`` in ``list()`` for Python 3 compatibility (https://github.com/ansible-collections/community.general/pull/1861).
- redfish_config module, redfish_utils module utils - fix IndexError in ``SetManagerNic`` command (https://github.com/ansible-collections/community.general/issues/1692).
- redfish_info module, redfish_utils module utils - add ``Name`` and ``Id`` properties to output of Redfish inventory commands (https://github.com/ansible-collections/community.general/issues/1650).
- redhat_subscription - ``mutually_exclusive`` was referring to parameter alias instead of name (https://github.com/ansible-collections/community.general/pull/1795).
- redhat_subscription - wrapped usages of ``dict.keys()`` in ``list()`` for Python 3 compatibility (https://github.com/ansible-collections/community.general/pull/1861).
- redis cache plugin - wrapped usages of ``keys()`` in ``list()`` for Python 3 compatibility (https://github.com/ansible-collections/community.general/pull/1861).
- riak - parameters ``wait_for_handoffs`` and ``wait_for_ring`` are ``int`` but the default value was ``false`` (https://github.com/ansible-collections/community.general/pull/1830).
- rundeck_acl_policy - internal refactoring: replaced uses of ``_`` with ``dummy`` (https://github.com/ansible-collections/community.general/pull/1819).
- runit - removed unused code, and passing command as ``list`` instead of ``str`` to ``run_command()`` (https://github.com/ansible-collections/community.general/pull/1830).
- scaleway inventory plugin - fix pagination on scaleway inventory plugin (https://github.com/ansible-collections/community.general/pull/2036).
- selective callback plugin - adjust import so that the plugin also works with ansible-core 2.11 (https://github.com/ansible-collections/community.general/pull/1807).
- selective callback plugin - wrapped usages of ``dict.keys()`` in ``list()`` for Python 3 compatibility (https://github.com/ansible-collections/community.general/pull/1861).
- sensu-silence module - fix json parsing of sensu API responses on Python 3.5 (https://github.com/ansible-collections/community.general/pull/1703).
- sensu_check - wrapped usages of ``dict.keys()`` in ``list()`` for Python 3 compatibility (https://github.com/ansible-collections/community.general/pull/1861).
- spotinst_aws_elastigroup - wrapped usages of ``dict.keys()`` in ``list()`` for Python 3 compatibility (https://github.com/ansible-collections/community.general/pull/1861).
- stacki_host - replaced ``default`` to environment variables with ``fallback`` to them (https://github.com/ansible-collections/community.general/pull/2072).
- stackpath_compute inventory script - fix broken validation checks for client ID and client secret (https://github.com/ansible-collections/community.general/pull/2448).
- statusio_maintenance - internal refactoring: replaced uses of ``_`` with ``dummy`` (https://github.com/ansible-collections/community.general/pull/1819).
- svr4pkg - convert string to a bytes-like object to avoid ``TypeError`` with Python 3 (https://github.com/ansible-collections/community.general/issues/2373).
- terraform - fix issue that cause the destroy to fail because from Terraform 0.15 on, the ``terraform destroy -force`` option is replaced with ``terraform destroy -auto-approve`` (https://github.com/ansible-collections/community.general/issues/2247).
- terraform - fix issue that cause the execution fail because from Terraform 0.15 on, the ``-var`` and ``-var-file`` options are no longer available on ``terraform validate`` (https://github.com/ansible-collections/community.general/pull/2246).
- terraform - remove uses of ``use_unsafe_shell=True`` (https://github.com/ansible-collections/community.general/pull/2246).
- timezone - internal refactoring: replaced uses of ``_`` with ``dummy`` (https://github.com/ansible-collections/community.general/pull/1819).
- udm_dns_record - fixed default value of parameter ``data`` to match its type (https://github.com/ansible-collections/community.general/pull/2268).
- utm_utils module_utils - wrapped usages of ``dict.keys()`` in ``list()`` for Python 3 compatibility (https://github.com/ansible-collections/community.general/pull/1861).
- vdo - wrapped usages of ``dict.keys()`` in ``list()`` for Python 3 compatibility (https://github.com/ansible-collections/community.general/pull/1861).
- vmadm - correct type of list elements in ``resolvers`` parameter (https://github.com/ansible-collections/community.general/issues/2135).
- xfconf - module was not honoring check mode when ``state`` was ``absent`` (https://github.com/ansible-collections/community.general/pull/2185).
- xfs_quota - the feedback for initializing project quota using xfs_quota binary from ``xfsprogs`` has changed since the version it was written for (https://github.com/ansible-collections/community.general/pull/1596).
- zfs - certain ZFS properties, especially sizes, would lead to a task being falsely marked as "changed" even when no actual change was made (https://github.com/ansible-collections/community.general/issues/975, https://github.com/ansible-collections/community.general/pull/2454).
- zfs - some ZFS properties could be passed when the dataset/volume did not exist, but would fail if the dataset already existed, even if the property matched what was specified in the ansible task (https://github.com/ansible-collections/community.general/issues/868, https://github.com/ansible-collections/community.general/pull/1833).
- zfs_delegate_admin - the elements of ``users``, ``groups`` and ``permissions`` are now enforced to be strings (https://github.com/ansible-collections/community.general/pull/1766).
- zypper, zypper_repository - respect ``PATH`` environment variable when resolving zypper executable path (https://github.com/ansible-collections/community.general/pull/2094).

community.grafana
~~~~~~~~~~~~~~~~~

- Fix issue with grafana_user that failed to create admin user (#142)
- Fix issue with url when grafana_url has a trailing slash (#135)
- grafana_dashboard, Fix reference before assignment issue (#146)

community.hashi_vault
~~~~~~~~~~~~~~~~~~~~~

- hashi_vault - restore use of ``VAULT_ADDR`` environment variable as a low preference env var (https://github.com/ansible-collections/community.hashi_vault/pull/61).
- hashi_vault - userpass authentication did not work with hvac 0.9.6 or higher (https://github.com/ansible-collections/community.hashi_vault/pull/68).

community.hrobot
~~~~~~~~~~~~~~~~

- robot - force HTTP basic authentication to reduce number of HTTPS requests (https://github.com/ansible-collections/community.hrobot/pull/9).

community.kubernetes
~~~~~~~~~~~~~~~~~~~~

- fix missing requirements.txt file in kubernetes.core (https://github.com/ansible-collections/community.kubernetes/pull/401).
- helm - ``release_values`` makes ansible always show changed state (https://github.com/ansible-collections/community.kubernetes/issues/274)
- helm - make helm-diff plugin detection more reliable by splitting by any whitespace instead of explicit whitespace (``\s``) (https://github.com/ansible-collections/community.kubernetes/pull/362).
- helm - return values in check mode when release is not present (https://github.com/ansible-collections/community.kubernetes/issues/280).
- helm_plugin - make unused ``release_namespace`` parameter as optional (https://github.com/ansible-collections/community.kubernetes/issues/357).
- helm_plugin_info - make unused ``release_namespace`` parameter as optional (https://github.com/ansible-collections/community.kubernetes/issues/357).
- k8s - fix check_mode always showing changes when using stringData on Secrets (https://github.com/ansible-collections/community.kubernetes/issues/282).
- k8s - handle ValueError when namespace is not provided (https://github.com/ansible-collections/community.kubernetes/pull/330).
- pin molecule version to <3.3.0 to fix breaking changes (https://github.com/ansible-collections/community.kubernetes/pull/403).
- respect the ``wait_timeout`` parameter in the ``k8s`` and ``k8s_info`` modules when a resource does not exist (https://github.com/ansible-collections/community.kubernetes/issues/344).

community.libvirt
~~~~~~~~~~~~~~~~~

- libvirt_qemu - Mitigate a CPU hammering active wait loop
- libvirt_qemu - add import error handling
- virt - Correctly get the error message from libvirt
- virt - Return "changed" status when using "define" command and domain XML was updated
- virt - The define action searchs for the domain name into the xml definition to determine if the domain needs to be created or updated. The xml variable contains the parsed definition but doesn't guarantee the existence of the name tag. This change targets to fix the scenario where the xml var is not empty but doesn't contain a name tag.
- virt_net - The name parameter is not required for the list_nets or facts command so we adjust the module to allow for that.

community.mysql
~~~~~~~~~~~~~~~

- mysql - revert changes of connector arguments made in pull request 116 causing the invalid keyword argument error (https://github.com/ansible-collections/community.mysql/pull/116).
- mysql_user - add support for ``REPLICA MONITOR`` privilege (https://github.com/ansible-collections/community.mysql/issues/105).
- mysql_user - fix handling of INSERT, UPDATE, REFERENCES on columns (https://github.com/ansible-collections/community.mysql/issues/106).
- mysql_user - the module is not idempotent when SELECT on columns granted (https://github.com/ansible-collections/community.mysql/issues/99).

community.network
~~~~~~~~~~~~~~~~~

- nclu - fix ``net pending`` delimiter string (https://github.com/ansible-collections/community.network/pull/219).
- {cnos,icx}_static_route modules - fix modules to work with ansible-core 2.11 (https://github.com/ansible-collections/community.network/pull/228).

community.okd
~~~~~~~~~~~~~

- add missing requirements.txt file needed for execution environments (https://github.com/ansible-collections/community.okd/pull/78).
- include requirements.txt in downstream build process (https://github.com/ansible-collections/community.okd/pull/81).
- openshift_route - default to ``no_log=False`` for the ``key`` parameter in TLS configuration to fix sanity failures (https://github.com/ansible-collections/community.okd/pull/77).
- restrict molecule version to <3.3.0 to address breaking change (https://github.com/ansible-collections/community.okd/pull/77).
- update CI to work with ansible 2.11 (https://github.com/ansible-collections/community.okd/pull/80).

community.sops
~~~~~~~~~~~~~~

- action_module plugin helper - make compatible with latest changes in ansible-core 2.11.0b3 (https://github.com/ansible-collections/community.sops/pull/58).
- community.sops.load_vars - make compatible with latest changes in ansible-core 2.11.0b3 (https://github.com/ansible-collections/community.sops/pull/58).
- community.sops.sops_encrypt - use output type ``yaml`` when path ends with ``.yaml`` (https://github.com/ansible-collections/community.sops/pull/56).

community.vmware
~~~~~~~~~~~~~~~~

- vcenter_license - fixed a bug that the license doesn't assign in VCSA 7.0u1c (https://github.com/ansible-collections/community.vmware/pull/643).
- vmware - add the default value of parameter resource_pool_name in the find_resource_pool_by_name function (https://github.com/ansible-collections/community.vmware/pull/670).
- vmware - fixed an issue that a port group name doesn't compare correctly in the find_network_by_name function (https://github.com/ansible-collections/community.vmware/pull/661).
- vmware_category - append namespace to associable types (https://github.com/ansible-collections/community.vmware/issues/579).
- vmware_cluster_ha - fix enabling APD or PDL response (https://github.com/ansible-collections/community.vmware/issues/676).
- vmware_cluster_info - return VSAN status correctly (https://github.com/ansible-collections/community.vmware/issues/673).
- vmware_cluster_vsan - fixed a bug that made the module fail when advanced_options is not set (https://github.com/ansible-collections/community.vmware/issues/728).
- vmware_deploy_ovf - fixed an issue that a return value hasn't the instance key when the power_on parameter is False (https://github.com/ansible-collections/community.vmware/pull/698).
- vmware_deploy_ovf - fixed an issue that an error message doesn't show when not finding a port group name (https://github.com/ansible-collections/community.vmware/pull/661).
- vmware_deploy_ovf - fixed an issue that deploy template in datacenter with more than one standalone hosts (https://github.com/ansible-collections/community.vmware/pull/670).
- vmware_dvs_portgroup - fixed the issue that the VLAN configuration isn't compared correctly in the module (https://github.com/ansible-collections/community.vmware/pull/638).
- vmware_dvs_portgroup_find - fixed to decode the special characters URL-encoded in the dvs port group name (https://github.com/ansible-collections/community.vmware/pull/648).
- vmware_dvs_portgroup_info - fixed to decode the special characters URL-encoded in the dvs port group name (https://github.com/ansible-collections/community.vmware/pull/648).
- vmware_guest - add support for ``advanced settings`` in vmware_guest (https://github.com/ansible-collections/community.vmware/issues/602).
- vmware_guest - fixed a bug that made the module fail when disk.controller_number or disk.unit_number are 0 (https://github.com/ansible-collections/community.vmware/issues/703).
- vmware_guest_register_operation - fixed an issue that an error has been occurring when not specifying a datacenter name (https://github.com/ansible-collections/community.vmware/pull/693).
- vmware_local_user_manager - fixed to require local_user_password when the state is present (https://github.com/ansible-collections/community.vmware/pull/724).
- vmware_vm_inventory - Skip over ghost tags attached to virtual machines (https://github.com/ansible-collections/community.vmware/issues/681).
- vmware_vm_storage_policy - fixed an issue that an error for pyvmomi(SDK) occurred when a tag or category doesn't exist (https://github.com/ansible-collections/community.vmware/pull/682).

community.windows
~~~~~~~~~~~~~~~~~

- win_firewall_rule - Ensure ``service: any`` is set to match any service instead of the literal service called ``any`` as per the docs
- win_scoop - Make sure we enable TLS 1.2 when installing scoop
- win_xml - Fix ``PropertyNotFound`` exception when creating a new attribute - https://github.com/ansible-collections/community.windows/issues/166

community.zabbix
~~~~~~~~~~~~~~~~

- zabbix_action - now properly filters discovery rule checks by name (https://github.com/ansible-collections/community.zabbix/pull/349).
- zabbix_agent - corrected version for Windows agents (https://github.com/ansible-collections/community.zabbix/pull/316).
- zabbix_agent - fixed download URL for MacOS (https://github.com/ansible-collections/community.zabbix/pull/325).
- zabbix_server - now installs correct MySQL client packages on RHEL8 systems (https://github.com/ansible-collections/community.zabbix/pull/343).
- zabbix_template - fixed an issue with Python2 where module wouldn't decode Unicode characters (https://github.com/ansible-collections/community.zabbix/pull/322).
- zabbix_web - fixed installation of python3-libsemanage package RHEL7 and older systems (https://github.com/ansible-collections/community.zabbix/pull/330).
- zabbix_web - role should now correctly determine naming of PHP packages on older systems (https://github.com/ansible-collections/community.zabbix/pull/344).
- zabbix_web - updated default PHP version for Debian10 (https://github.com/ansible-collections/community.zabbix/pull/323).

containers.podman
~~~~~~~~~~~~~~~~~

- Add IPv6 support for publishing ports
- Add docs generation
- Add sigrtmin+3 signal (required for systemd containers)
- Add support for Podman Pod restart
- Attempt graceful stop when recreating container
- Convert IPv6 to shorten form
- Don't calculate image digest in check mode
- Fix error with images info where no images
- Fix idempotency for rootless networks from v3
- Fix internal networks and DNS plugin for v3
- Fix no_log for newer ansible-test
- Fix podman_pod* modules for Podman v3
- Fix uppercase labels idempotency issue
- Fixes for podman_container for Podman v3
- Stop pods without recreating them
- Update documentation
- documentation - Add docs to Github
- podman_container - Add 'created' state for podman_container
- podman_container - Change default log level for 3+ versions
- podman_container - Convert systemd option to a string
- podman_container - Don't recreate container if env_file is specified
- podman_container - Fix 'cap_add' and 'cap_drop' idempotency
- podman_container - Fix idempotency for multiple ports
- podman_container - Fix slirp4netns options idempotency
- podman_container - Fix uid/gid checks for podman 1.6.4 volumes
- podman_container - Handle slash removals for root volumes mount
- podman_container - Restart container in a simple manner
- podman_container - podman_container_lib - fix command idempotency
- podman_image - Add debug log and podman_actions to podman_image
- podman_image - Don't set default for validate-certs in podman_image

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- ome_firmware_baseline_compliance_info - OMEnt firmware baseline compliance info pagination support added (https://github.com/dell/dellemc-openmanage-ansible-modules/issues/171)
- ome_network_proxy - OMEnt network proxy check mode support added (https://github.com/dell/dellemc-openmanage-ansible-modules/issues/187)

dellemc.os9
~~~~~~~~~~~

- Fix issue in using list of strings for commands argument for os10_command module (https://github.com/ansible-collections/dellemc.os9/issues/15)
- Fixed sanity error found during the sanity tst of automation hub upload

f5networks.f5_modules
~~~~~~~~~~~~~~~~~~~~~

- Added Fix for bigip_config check mode issue
- Fix a bug with replace_with_all logic to consider ports in bigip_pool_member module
- Fix control characters causing url encoding errors in bigip_policy module
- Fix for bigip_device_license license reactivation
- Fix for documentation bigip_data_group module doesn't check records content
- Fix issue in bigip_pool_member module invwhere incorrect IF statement in function preveninv ted from reusing FQDN nodes for new pool members
- Fix issue where error messages were replaced by generic error message in bigip_device_policy module
- Fix issue with destination_address and destination_port parameters not being properly returned by bigip_device_info module
- Fix issue with expired tokens causing module run to fail in bigiq_device_discovery
- Fix issue with removal action not allowing atomic rule updates in bigip_policy_rule module
- Fix lookup plugin support for bigiq_license
- Fix virtual server type value displaying incorrect information in bigip_device_info module
- Fixes issues with downloading ASM policies in binary format

fortinet.fortios
~~~~~~~~~~~~~~~~

- Deprecated second-layer state module parameter
- enable_log - Explicit logging option.

hetzner.hcloud
~~~~~~~~~~~~~~

- hcloud_firewall - fix idempotence related to rules comparison (https://github.com/ansible-collections/hetzner.hcloud/pull/71).
- hcloud_load_balancer_service - fix imported wrong HealthCheck from hcloud-python (https://github.com/ansible-collections/hetzner.hcloud/pull/73).
- hcloud_server - fix a crash related to check mode if ``state=started`` or ``state=stopped`` (https://github.com/ansible-collections/hetzner.hcloud/issues/54).
- hcloud_server - fix idempotence related to firewall handling (https://github.com/ansible-collections/hetzner.hcloud/pull/71).
- hcloud_server Fix incompatbility with python < 3.6
- hcloud_server Improve error handling when using not existing server types
- inventory fix image name was set as server type instead of the correct server type

inspur.sm
~~~~~~~~~

- Add ansible 2.11 test.
- Add the no_log=true attribute to some modules.

kubernetes.core
~~~~~~~~~~~~~~~

- fix missing requirements.txt file in kubernetes.core (https://github.com/ansible-collections/kubernetes.core/pull/401).
- helm - ``release_values`` makes ansible always show changed state (https://github.com/ansible-collections/kubernetes.core/issues/274)
- helm - make helm-diff plugin detection more reliable by splitting by any whitespace instead of explicit whitespace (``\s``) (https://github.com/ansible-collections/kubernetes.core/pull/362).
- helm - return values in check mode when release is not present (https://github.com/ansible-collections/kubernetes.core/issues/280).
- helm_plugin - make unused ``release_namespace`` parameter as optional (https://github.com/ansible-collections/kubernetes.core/issues/357).
- helm_plugin_info - make unused ``release_namespace`` parameter as optional (https://github.com/ansible-collections/kubernetes.core/issues/357).
- k8s - fix check_mode always showing changes when using stringData on Secrets (https://github.com/ansible-collections/kubernetes.core/issues/282).
- k8s - handle ValueError when namespace is not provided (https://github.com/ansible-collections/kubernetes.core/pull/330).
- pin molecule version to <3.3.0 to fix breaking changes (https://github.com/ansible-collections/kubernetes.core/pull/403).
- respect the ``wait_timeout`` parameter in the ``k8s`` and ``k8s_info`` modules when a resource does not exist (https://github.com/ansible-collections/kubernetes.core/issues/344).

netapp.aws
~~~~~~~~~~

- all modules - disable logging for ``api_key`` and ``secret_key`` values.
- all modules - prevent infinite loop when asynchronous action fails.
- all modules - report error if response does not contain valid JSON.
- aws_netapp_cvs_filesystems - fix KeyError when exportPolicy is not present.

netapp.azure
~~~~~~~~~~~~

- azure_rm_netapp_account - wait for job completion for asynchroneous requests, and report belated errors.
- azure_rm_netapp_capacity_pool - fixed idempotency for delete operation.
- azure_rm_netapp_volume - fix 'Nonetype' object is not subscriptable exception when mount target is not created.
- fix changes to azure-mgmt-netapp as per new release.
- galaxy.yml - fix path to github repository.
- removed ONTAP dependency import.
- support for azure-mgmt-netapp 1.0.0, while maintaining compatibility with 0.10.0.

netapp.cloudmanager
~~~~~~~~~~~~~~~~~~~

- na_cloudmanager_cvo_aws - Fix incorrect placement of platformSerialNumber in the resulting json structure

netapp.elementsw
~~~~~~~~~~~~~~~~

- na_elementsw_drive - lastest SDK does not accept ``force_during_bin_sync`` and ``force_during_upgrade``.
- na_elementsw_qos_policy - loop would convert `minIOPS`, `maxIOPS`, `burstIOPS` to str, causing type mismatch issues in comparisons.
- na_elementsw_snapshot_schedule - change of interface in SDK ('ScheduleInfo' object has no attribute 'minutes')

netapp.ontap
~~~~~~~~~~~~

- All REST modules - ONTAP 9.4 and 9.5 are incorrectly detected as supporting REST with ``use_rest:auto``.
- na_ontap_autosupport - warn when password is present in ``proxy_url`` as it makes the operation not idempotent.
- na_ontap_cluster - ignore ZAPI EMS log error when in pre-cluster mode.
- na_ontap_igroup - report error when attempting to modify an option that cannot be changed.
- na_ontap_ldap_client - ``port`` was incorrectly used instead of ``tcp_port``.
- na_ontap_lun - SAN application is not supported on 9.6 and only partially supported on 9.7 (no modify).
- na_ontap_lun - ``qos_policy_group`` could not be modified if a value was not provided at creation.
- na_ontap_lun - tiering options were ignored in san_application_template.
- na_ontap_node - KeyError fix for location ans asset-tag parameters in get_node().
- na_ontap_qtree - wait for completion when creating or modifying a qtree with REST.
- na_ontap_snapmirror - SVM scoped policies were not found when using a destination path with REST application.
- na_ontap_snapmirror - check for consistency_group_volumes always fails on 9.7, and cluster or ipspace when using endpoints with ZAPI.
- na_ontap_svm - iscsi current status is not read correctly (mispelled issi).
- na_ontap_volume - changes in ``encrypt`` settings were ignored.
- na_ontap_volume - ignore read error because of insufficient privileges for efficiency options so that the module can be run as vsadmin.
- na_ontap_volume - report error from resize operation when using REST.
- na_ontap_volume - returns an error now if deleting a volume with REST api fails.
- na_ontap_volume - unmount volume before deleting it when using REST.

netapp_eseries.santricity
~~~~~~~~~~~~~~~~~~~~~~~~~

- Add missing http(s) proxy username and password parameters from na_santricity_asup module and nar_santricity_management role."
- Add missing storage pool configuration parameter, criteria_drive_interface_type, to nar_santricity_host role.
- Fix drive firmware upgrade issue that prevented updating firware when drive was in use.
- Fix jinja issue with collecting certificates paths in nar_santricity_management role.
- nar_santricity_host - Fix README.md examples.

netbox.netbox
~~~~~~~~~~~~~

- Remove ansible.netcommon and community.general dependencies from collection
- netbox_ip_address - Added assigned_object to ALLOWED_QUERY_PARAMS

openvswitch.openvswitch
~~~~~~~~~~~~~~~~~~~~~~~

- Allow deleting key from table without specifying value (https://github.com/ansible-collections/openvswitch.openvswitch/issues/64).

ovirt.ovirt
~~~~~~~~~~~

- Set ``auth`` options into argument spec definition so Ansible will validate the user options
- Set ``no_log`` on ``password`` and ``token`` in the ``auth`` dict so the values are exposed in the invocation log
- hosted_engine_setup - Fix auth revoke (https://github.com/oVirt/ovirt-ansible-collection/pull/237).

purestorage.flasharray
~~~~~~~~~~~~~~~~~~~~~~

- purefa_dsrole - If using None for group or group_base incorrect change state applied
- purefa_hg - Ensure all hostname chacks are lowercase for consistency
- purefa_info - Fix missing protection group snapshot info for local snapshots
- purefa_info - Resolve crash when an offload target is offline
- purefa_network - Allow gateway paremeter to be set as None - needed for non-routing iSCSI ports
- purefa_pg - Check to ensure protection group name meets naming convention
- purefa_pgsnap - Add check to ensure suffix name meets naming conventions
- purefa_pgsnap - Ensure pgsnap restores work for AC PGs
- purefa_pgsnap - Ensure suffix rules only implemented for state=present
- purefa_pgsnap - Fail with warning if trying to restore to a stretched ActiveCluster pod
- purefa_pod - Ensure all pod names are lowercase for consistency
- purefa_snap - Update suffix regex pattern
- purefa_user - Do not allow role changed for breakglass user (pureuser)
- purefa_user - Do not change role for existing user unless requested
- purefa_volume - Add missing variable initialization
- purefa_volume - Ensure REST version is high enough to support promotion_status
- purefa_volume - Fix issues with moving volumes into demoted or linked pods

purestorage.flashblade
~~~~~~~~~~~~~~~~~~~~~~

- purefb_* - Return a correct value for `changed` in all modules when in check mode
- purefb_dns - Deprecate search paramerter
- purefb_dsrole - Resolve idempotency issue
- purefb_lifecycle - Fix error when creating new bucket lifecycle rule.
- purefb_policy - Ensure undeclared variables are set correctly
- purefb_s3user - Fix maximum access_key count logic

sensu.sensu_go
~~~~~~~~~~~~~~

- Add ansible.windows dependency that we forgot to add when we introducted the Sensu Go agent installation on Windows.
- Allow downgrading Sensu Go packages on Linux distributions that use yum or dnf for package management.
- Make sure we lazy-load Windows-related content.

theforeman.foreman
~~~~~~~~~~~~~~~~~~

- content_view_version - make the ``version`` parameter not fail when the version was entered without a minor part (https://github.com/theforeman/foreman-ansible-modules/issues/1087)
- host - allow moving hosts between Organizations and Locations (https://bugzilla.redhat.com/show_bug.cgi?id=1901716)
- host - don't filter ``false`` values for ``interfaces_attributes`` (https://github.com/theforeman/foreman-ansible-modules/issues/1148)
- host - fix subnet/domain assignment when multiple interfaces are defined (https://github.com/theforeman/foreman-ansible-modules/issues/1095)
- host, hostgroup - select kickstart_repository based on lifecycle_environment and content_view if those are set (https://github.com/theforeman/foreman-ansible-modules/issues/1090, https://bugzilla.redhat.com/1915872)
- host_info, repository_info - correctly fetch all entities when neither ``name`` nor ``search`` is set
- host_info, repository_info - enforce mutual exclusivity of ``name`` and ``search``
- resource_info - correctly show the exact resource when passing ``id`` in ``params``

vyos.vyos
~~~~~~~~~

- Update docs to clarify the idemptonecy related caveat and add it in the output warnings (https://github.com/ansible-collections/ansible.netcommon/pull/189)
- cliconf plugin - Prevent `get_capabilities()` from getting larger every time it is called

Known Issues
------------

Ansible-core
~~~~~~~~~~~~

- ansible-test - The ``pylint`` sanity test no longer correctly detects "bad" variable names for non-constants. See https://github.com/PyCQA/pylint/issues/3701 for additional details.

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- idrac_user - Issue(192043) Module may error out with the message ``unable to perform the import or export operation because there are pending attribute changes or a configuration job is in progress``. Wait for the job to complete and run the task again.
- ome_configuration_compliance_info - Issue(195592) Module may error out with the message ``unable to process the request because an error occurred``. If the issue persists, report it to the system administrator.
- ome_smart_fabric - Issue(185322) Only three design types are supported by OpenManage Enterprise Modular but the module successfully creates a fabric when the design type is not supported.
- ome_smart_fabric_uplink - Issue(186024) ome_smart_fabric_uplink module does not allow the creation of multiple uplinks of the same name even though this is supported by OpenManage Enterprise Modular. If an uplink is created using the same name as an existing uplink, the existing uplink is modified.

fortinet.fortios
~~~~~~~~~~~~~~~~

- Modules for monitor API are not versioned yet.

New Plugins
-----------

Become
~~~~~~

- community.general.sudosu - Run tasks using sudo su -

Cache
~~~~~

- ansible.netcommon.memory - RAM backed, non persistent cache.

Callback
~~~~~~~~

- community.general.loganalytics - Posts task results to Azure Log Analytics

Cliconf
~~~~~~~

- community.network.weos4 - Use weos4 cliconf to run commands on Westermo platform
- dellemc.enterprise_sonic.sonic - Use Ansible CLICONF to run commands on Enterprise SONiC.

Filter
~~~~~~

- community.general.dict - The ``dict`` function as a filter: converts a list of tuples to a dictionary
- community.general.from_csv - Converts CSV text input into list of dicts
- community.general.hashids_decode - Decodes a sequence of numbers from a YouTube-like hash
- community.general.hashids_encode - Encodes YouTube-like hashes from a sequence of integers
- community.general.path_join - Redirects to ansible.builtin.path_join for ansible-base 2.10 or newer, and provides a compatible implementation for Ansible 2.9
- community.general.version_sort - Sort a list according to version order instead of pure alphabetical one

Httpapi
~~~~~~~

- dellemc.enterprise_sonic.sonic - Use Ansible HTTPAPI to run commands on Enterprise SONiC.

Inventory
~~~~~~~~~

- community.digitalocean.digitalocean - DigitalOcean Inventory Plugin
- community.general.lxd - Returns Ansible inventory from lxd host
- ngine_io.cloudstack.instance - Apache CloudStack instance inventory source

New Modules
-----------

Ansible-core
~~~~~~~~~~~~

- ansible.builtin.validate_argument_spec - Validate role argument specs.

ansible.windows
~~~~~~~~~~~~~~~

- ansible.windows.win_powershell - Run PowerShell scripts

cisco.ios
~~~~~~~~~

- cisco.ios.ios_bgp_address_family - BGP Address Family resource module.

cisco.iosxr
~~~~~~~~~~~

- cisco.iosxr.iosxr_bgp_address_family - Manages BGP Address Family resource module.
- cisco.iosxr.iosxr_bgp_global - Manages BGP global resource module.
- cisco.iosxr.iosxr_bgp_neighbor_address_family - Manages BGP neighbor address family resource module.

cisco.nxos
~~~~~~~~~~

- cisco.nxos.nxos_bgp_address_family - BGP Address Family resource module.
- cisco.nxos.nxos_bgp_neighbor_address_family - BGP Neighbor Address Family resource module.
- cisco.nxos.nxos_route_maps - Route Maps resource module.

community.aws
~~~~~~~~~~~~~

- community.aws.ec2_vpc_endpoint_service_info - retrieves AWS VPC endpoint service details
- community.aws.wafv2_ip_set - wafv2_ip_set
- community.aws.wafv2_ip_set_info - Get information about wafv2 ip sets
- community.aws.wafv2_resources - wafv2_web_acl
- community.aws.wafv2_resources_info - wafv2_resources_info
- community.aws.wafv2_rule_group - wafv2_web_acl
- community.aws.wafv2_rule_group_info - wafv2_web_acl_info
- community.aws.wafv2_web_acl - wafv2_web_acl
- community.aws.wafv2_web_acl_info - wafv2_web_acl

community.digitalocean
~~~~~~~~~~~~~~~~~~~~~~

- community.digitalocean.digital_ocean_domain_record - Manage DigitalOcean domain records
- community.digitalocean.digital_ocean_firewall - Manage cloud firewalls within DigitalOcean

community.docker
~~~~~~~~~~~~~~~~

- community.docker.docker_container_exec - Execute command in a docker container
- community.docker.docker_image_load - Load docker image(s) from archives
- community.docker.docker_plugin - Manage Docker plugins

community.general
~~~~~~~~~~~~~~~~~

Cloud
^^^^^

Misc
....

- community.general.proxmox_storage_info - Retrieve information about one or more Proxmox VE storages

Opennebula
..........

- community.general.one_template - Manages OpenNebula templates

Files
^^^^^

- community.general.filesize - Create a file with a given size, or resize it if it exists

Identity
^^^^^^^^

Ipa
...

- community.general.ipa_otpconfig - Manage FreeIPA OTP Configuration Settings
- community.general.ipa_otptoken - Manage FreeIPA OTPs

Keycloak
........

- community.general.keycloak_realm - Allows administration of Keycloak realm via Keycloak API

Monitoring
^^^^^^^^^^

- community.general.spectrum_model_attrs - Enforce a model's attributes in CA Spectrum.
- community.general.statsd - Send metrics to StatsD

Net Tools
^^^^^^^^^

- community.general.gandi_livedns - Manage Gandi LiveDNS records

Pritunl
.......

- community.general.pritunl_org - Manages Pritunl Organizations using the Pritunl API
- community.general.pritunl_org_info - List Pritunl Organizations using the Pritunl API
- community.general.pritunl_user - Manage Pritunl Users using the Pritunl API
- community.general.pritunl_user_info - List Pritunl Users using the Pritunl API

Remote Management
^^^^^^^^^^^^^^^^^

Lenovoxcc
.........

- community.general.xcc_redfish_command - Manages Lenovo Out-Of-Band controllers using Redfish APIs

Source Control
^^^^^^^^^^^^^^

Github
......

- community.general.github_repo - Manage your repositories on Github

Gitlab
......

- community.general.gitlab_project_members - Manage project members on GitLab Server

Web Infrastructure
^^^^^^^^^^^^^^^^^^

- community.general.jenkins_build - Manage jenkins builds

community.vmware
~~~~~~~~~~~~~~~~

- community.vmware.vmware_guest_instant_clone - Instant Clone VM
- community.vmware.vmware_guest_storage_policy - Set VM Home and disk(s) storage policy profiles.

community.windows
~~~~~~~~~~~~~~~~~

- community.windows.win_psrepository_copy - Copies registered PSRepositories to other user profiles

containers.podman
~~~~~~~~~~~~~~~~~

- containers.podman.podman_login - Login to a container registry using podman

dellemc.enterprise_sonic
~~~~~~~~~~~~~~~~~~~~~~~~

- dellemc.enterprise_sonic.sonic_api - Perform REST operations through the Management Framework REST API.
- dellemc.enterprise_sonic.sonic_bgp - BGP resource module.
- dellemc.enterprise_sonic.sonic_bgp_af - BGP AF resource module.
- dellemc.enterprise_sonic.sonic_bgp_as_paths - BGP AS path resource module.
- dellemc.enterprise_sonic.sonic_bgp_communities - BGP communities resource module.
- dellemc.enterprise_sonic.sonic_bgp_ext_communities - BGP Ext communities resource module.
- dellemc.enterprise_sonic.sonic_bgp_neighbors - BGP neighbors resource module.
- dellemc.enterprise_sonic.sonic_bgp_neighbors_af - BGP neighbors AF resource module.
- dellemc.enterprise_sonic.sonic_command - Run commands through Management Framework CLI.
- dellemc.enterprise_sonic.sonic_config - Manage configuration through the Management Framework CLI.
- dellemc.enterprise_sonic.sonic_interfaces - Interface resource module.
- dellemc.enterprise_sonic.sonic_l2_interfaces - Layer 2 interface resource module.
- dellemc.enterprise_sonic.sonic_l3_interfaces - Layer 3 interface resource module.
- dellemc.enterprise_sonic.sonic_lag_interfaces - Link aggregation (LAG) resource module.
- dellemc.enterprise_sonic.sonic_mclag - MCLAG resource module.
- dellemc.enterprise_sonic.sonic_port_breakout - port breakout resource module.
- dellemc.enterprise_sonic.sonic_users - USERS resource module.
- dellemc.enterprise_sonic.sonic_vlans - VLAN resource module.
- dellemc.enterprise_sonic.sonic_vrfs - VRF resource module.
- dellemc.enterprise_sonic.sonic_vxlans - VxLAN EVPN resource module.

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- dellemc.openmanage.ome_configuration_compliance_baseline - Create, modify, delete and remediate a compliance configuration baseline on OpenManage Enterprise
- dellemc.openmanage.ome_configuration_compliance_info - Device compliance report for devices managed in OpenManage Enterprise
- dellemc.openmanage.ome_device_group - Manages device group settings on OpenManage Enterprise
- dellemc.openmanage.ome_discovery - Create, modify or delete a discovery job on OpenManage Enterprise
- dellemc.openmanage.ome_profile - Create, modify, delete, assign, unassign and migrate a profile on OpenManage Enterprise

hetzner.hcloud
~~~~~~~~~~~~~~

- hetzner.hcloud.hcloud_firewall - Manage Hetzner Cloud Firewalls

hpe.nimble
~~~~~~~~~~

- hpe.nimble.hpe_nimble_access_control_record - Manage the HPE Nimble Storage access control records.
- hpe.nimble.hpe_nimble_array - Manage the HPE Nimble Storage array.
- hpe.nimble.hpe_nimble_chap_user - Manage the HPE Nimble Storage CHAP user.
- hpe.nimble.hpe_nimble_disk - Manage the HPE Nimble Storage disk.
- hpe.nimble.hpe_nimble_encryption - Manage the HPE Nimble Storage encryption.
- hpe.nimble.hpe_nimble_fc - Manage the HPE Nimble Storage Fibre Channel.
- hpe.nimble.hpe_nimble_group - Manage the HPE Nimble Storage group.
- hpe.nimble.hpe_nimble_info - Collect information from HPE Nimble Storage array.
- hpe.nimble.hpe_nimble_initiator_group - Manage the HPE Nimble Storage initiator groups.
- hpe.nimble.hpe_nimble_network - Manage the HPE Nimble Storage network configuration.
- hpe.nimble.hpe_nimble_partner - Manage the HPE Nimble Storage Replication Partner.
- hpe.nimble.hpe_nimble_performance_policy - Manage the HPE Nimble Storage performance policies
- hpe.nimble.hpe_nimble_pool - Manage the HPE Nimble Storage pools.
- hpe.nimble.hpe_nimble_protection_schedule - Manage the HPE Nimble Storage protection schedules.
- hpe.nimble.hpe_nimble_protection_template - Manage the HPE Nimble Storage protection templates.
- hpe.nimble.hpe_nimble_shelf - Manage the HPE Nimble Storage shelves.
- hpe.nimble.hpe_nimble_snapshot - Manage the HPE Nimble Storage snapshots.
- hpe.nimble.hpe_nimble_snapshot_collection - Manage the HPE Nimble Storage snapshot collections.
- hpe.nimble.hpe_nimble_user - Manage the HPE Nimble Storage users.
- hpe.nimble.hpe_nimble_user_policy - Manage the HPE Nimble Storage user policies.
- hpe.nimble.hpe_nimble_volume - Manage the HPE Nimble Storage volumes.
- hpe.nimble.hpe_nimble_volume_collection - Manage the HPE Nimble Storage volume collections.

junipernetworks.junos
~~~~~~~~~~~~~~~~~~~~~

- junipernetworks.junos.junos_bgp_address_family - Manage BGP Address Family attributes of interfaces on Junos devices.
- junipernetworks.junos.junos_routing_instances - Manage routing instances on Junos devices.

netapp.azure
~~~~~~~~~~~~

- netapp.azure.azure_rm_netapp_account - Manage NetApp Azure Files Account
- netapp.azure.azure_rm_netapp_capacity_pool - Manage NetApp Azure Files capacity pool
- netapp.azure.azure_rm_netapp_snapshot - Manage NetApp Azure Files Snapshot
- netapp.azure.azure_rm_netapp_volume - Manage NetApp Azure Files Volume

netapp.cloudmanager
~~~~~~~~~~~~~~~~~~~

- netapp.cloudmanager.na_cloudmanager_aggregate - NetApp Cloud Manager Aggregate
- netapp.cloudmanager.na_cloudmanager_cifs_server - NetApp Cloud Manager cifs server
- netapp.cloudmanager.na_cloudmanager_connector_aws - NetApp Cloud Manager connector for AWS
- netapp.cloudmanager.na_cloudmanager_connector_azure - NetApp Cloud Manager connector for Azure.
- netapp.cloudmanager.na_cloudmanager_connector_gcp - NetApp Cloud Manager connector for GCP.
- netapp.cloudmanager.na_cloudmanager_cvo_aws - NetApp Cloud Manager CVO for AWS
- netapp.cloudmanager.na_cloudmanager_cvo_azure - NetApp Cloud Manager CVO/working environment in single or HA mode for Azure.
- netapp.cloudmanager.na_cloudmanager_info - NetApp Cloud Manager info
- netapp.cloudmanager.na_cloudmanager_nss_account - NetApp Cloud Manager nss account
- netapp.cloudmanager.na_cloudmanager_volume - NetApp Cloud Manager volume

netapp.ontap
~~~~~~~~~~~~

- netapp.ontap.na_ontap_cifs_local_group_member - NetApp Ontap - Add or remove CIFS local group member
- netapp.ontap.na_ontap_cifs_local_user_modify - NetApp ONTAP modify local CIFS user.
- netapp.ontap.na_ontap_disk_options - NetApp ONTAP modify storage disk options
- netapp.ontap.na_ontap_domain_tunnel - NetApp ONTAP domain tunnel
- netapp.ontap.na_ontap_fpolicy_event - NetApp ONTAP FPolicy policy event configuration
- netapp.ontap.na_ontap_fpolicy_ext_engine - NetApp ONTAP fPolicy external engine configuration.
- netapp.ontap.na_ontap_fpolicy_policy - NetApp ONTAP - Create, delete or modify an FPolicy policy.
- netapp.ontap.na_ontap_fpolicy_scope - NetApp ONTAP - Create, delete or modify an FPolicy policy scope configuration.
- netapp.ontap.na_ontap_fpolicy_status - NetApp ONTAP - Enables or disables the specified fPolicy policy
- netapp.ontap.na_ontap_log_forward - NetApp ONTAP Log Forward Configuration
- netapp.ontap.na_ontap_lun_map_reporting_nodes - NetApp ONTAP LUN maps reporting nodes
- netapp.ontap.na_ontap_security_config - NetApp ONTAP modify security config for SSL.
- netapp.ontap.na_ontap_snaplock_clock - NetApp ONTAP Sets the snaplock compliance clock.
- netapp.ontap.na_ontap_storage_auto_giveback - Enables or disables NetApp ONTAP storage auto giveback for a specified node
- netapp.ontap.na_ontap_storage_failover - Enables or disables NetApp Ontap storage failover for a specified node
- netapp.ontap.na_ontap_volume_efficiency - NetApp Ontap enables, disables or modifies volume efficiency

netapp.um_info
~~~~~~~~~~~~~~

- netapp.um_info.na_um_list_aggregates - NetApp Unified Manager list aggregates.
- netapp.um_info.na_um_list_clusters - NetApp Unified Manager list cluster.
- netapp.um_info.na_um_list_nodes - NetApp Unified Manager list nodes.
- netapp.um_info.na_um_list_svms - NetApp Unified Manager list svms.
- netapp.um_info.na_um_list_volumes - NetApp Unified Manager list volumes.

purestorage.flasharray
~~~~~~~~~~~~~~~~~~~~~~

- purestorage.flasharray.purefa_certs - Manage FlashArray SSL Certificates
- purestorage.flasharray.purefa_maintenance - Configure Pure Storage FlashArray Maintence Windows

purestorage.flashblade
~~~~~~~~~~~~~~~~~~~~~~

- purestorage.flashblade.purefb_ad - Manage FlashBlade Active Directory Account
- purestorage.flashblade.purefb_apiclient - Manage FlashBlade API Clients
- purestorage.flashblade.purefb_eula - Sign Pure Storage FlashBlade EULA
- purestorage.flashblade.purefb_keytabs - Manage FlashBlade Kerberos Keytabs
- purestorage.flashblade.purefb_timeout - Configure Pure Storage FlashBlade GUI idle timeout
- purestorage.flashblade.purefb_userpolicy - Manage FlashBlade Object Store User Access Policies
- purestorage.flashblade.purefb_virtualhost - Manage FlashBlade Object Store Virtual Hosts

sensu.sensu_go
~~~~~~~~~~~~~~

- sensu.sensu_go.cluster - Manage Sensu Go clusters
- sensu.sensu_go.cluster_info - List available Sensu Go clusters
- sensu.sensu_go.etcd_replicator - Manage Sensu Go etcd replicators
- sensu.sensu_go.etcd_replicator_info - List Sensu Go etcd replicators

theforeman.foreman
~~~~~~~~~~~~~~~~~~

- theforeman.foreman.host_info - Fetch information about Hosts
- theforeman.foreman.puppetclasses_import - Import Puppet Classes from a Proxy
- theforeman.foreman.repository_info - Fetch information about Repositories

vyos.vyos
~~~~~~~~~

- vyos.vyos.vyos_bgp_address_family - BGP Address Family Resource Module.
- vyos.vyos.vyos_bgp_global - BGP Global Resource Module.

Unchanged Collections
---------------------

- check_point.mgmt (still version 2.0.0)
- cisco.aci (still version 2.0.0)
- cisco.mso (still version 1.1.0)
- cisco.nso (still version 1.0.3)
- cisco.ucs (still version 1.6.0)
- community.azure (still version 1.0.0)
- community.fortios (still version 1.0.0)
- community.google (still version 1.0.0)
- community.kubevirt (still version 1.0.0)
- community.proxysql (still version 1.0.0)
- community.routeros (still version 1.1.0)
- community.skydive (still version 1.0.0)
- cyberark.conjur (still version 1.1.0)
- dellemc.os10 (still version 1.1.1)
- frr.frr (still version 1.0.3)
- gluster.gluster (still version 1.0.1)
- google.cloud (still version 1.0.2)
- ibm.qradar (still version 1.0.3)
- infinidat.infinibox (still version 1.2.4)
- mellanox.onyx (still version 1.0.0)
- ngine_io.exoscale (still version 1.0.0)
- ngine_io.vultr (still version 1.1.0)
- splunk.es (still version 1.0.2)
- wti.remote (still version 1.0.1)
