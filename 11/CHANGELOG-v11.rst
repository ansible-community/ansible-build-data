========================
Ansible 11 Release Notes
========================

This changelog describes changes since Ansible 10.0.0.

.. contents::
  :depth: 2

v11.6.0
=======

.. contents::
  :local:
  :depth: 2

Release Summary
---------------

Release Date: 2025-05-20

`Porting Guide <https://docs.ansible.com/ansible/devel/porting_guides.html>`_

Ansible-core
------------

Ansible 11.6.0 contains ansible-core version 2.18.6.
This is a newer version than version 2.18.5 contained in the previous Ansible release.

The changes are reported in the combined changelog below.

Changed Collections
-------------------

If not mentioned explicitly, the changes are reported in the combined changelog below.

+-----------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| Collection                  | Ansible 11.5.0 | Ansible 11.6.0 | Notes                                                                                                                        |
+=============================+================+================+==============================================================================================================================+
| amazon.aws                  | 9.4.0          | 9.5.0          |                                                                                                                              |
+-----------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.intersight            | 2.0.20         | 2.1.0          | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+-----------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.meraki                | 2.20.10        | 2.21.1         |                                                                                                                              |
+-----------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| cloud.common                | 4.0.0          | 4.1.0          |                                                                                                                              |
+-----------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.aws               | 9.2.0          | 9.3.0          |                                                                                                                              |
+-----------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.crypto            | 2.26.0         | 2.26.1         |                                                                                                                              |
+-----------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.dns               | 3.2.3          | 3.2.4          |                                                                                                                              |
+-----------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.docker            | 4.5.2          | 4.6.0          |                                                                                                                              |
+-----------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.general           | 10.6.0         | 10.7.0         |                                                                                                                              |
+-----------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.grafana           | 2.1.0          | 2.2.0          |                                                                                                                              |
+-----------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.hrobot            | 2.2.0          | 2.3.0          |                                                                                                                              |
+-----------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.postgresql        | 3.14.0         | 3.14.1         |                                                                                                                              |
+-----------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| cyberark.pas                | 1.0.30         | 1.0.35         | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+-----------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| dellemc.openmanage          | 9.11.0         | 9.12.0         |                                                                                                                              |
+-----------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| google.cloud                | 1.5.1          | 1.5.3          |                                                                                                                              |
+-----------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| hitachivantara.vspone_block | 3.3.0          | 3.4.1          |                                                                                                                              |
+-----------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| kubernetes.core             | 5.2.0          | 5.3.0          |                                                                                                                              |
+-----------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| kubevirt.core               | 2.1.0          | 2.2.2          | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+-----------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| lowlydba.sqlserver          | 2.6.0          | 2.6.1          |                                                                                                                              |
+-----------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| microsoft.ad                | 1.8.1          | 1.9.0          |                                                                                                                              |
+-----------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| netapp.storagegrid          | 21.14.0        | 21.15.0        |                                                                                                                              |
+-----------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| purestorage.flashblade      | 1.19.2         | 1.20.0         |                                                                                                                              |
+-----------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+

Major Changes
-------------

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- idrac_gather_facts - This role is enhanced to support iDRAC10.
- idrac_lifecycle_controller_job_status_info - This module is enhanced to support iDRAC10.
- idrac_system_info - This module is enhanced to support iDRAC10.

Minor Changes
-------------

Ansible-core
~~~~~~~~~~~~

- ansible-test - Use the ``-t`` option to set the stop timeout when stopping a container. This avoids use of the ``--time`` option which was deprecated in Docker v28.0.

amazon.aws
~~~~~~~~~~

- Bump version of ansible-lint to 25.1.2 (https://github.com/ansible-collections/amazon.aws/pull/2590).
- iam_user_info - Add tags to ListUsers or GetGroup results (https://github.com/ansible-collections/amazon.aws/pull/2567).
- iam_user_info - Return empty user list when invalid group name is provided instead of python error (https://github.com/ansible-collections/amazon.aws/pull/2567).
- module_utils/modules.py - call to ``deprecate()`` without specifying ``collection_name``, ``version`` or ``date`` arguments raises a sanity errors (https://github.com/ansible-collections/amazon.aws/pull/2607).

cisco.meraki
~~~~~~~~~~~~

- plugins/action/devices_sensor_commands - new plugin.
- plugins/action/devices_sensor_commands_info - new plugin.
- plugins/action/networks_appliance_firewall_multicast_forwarding - new plugin.
- plugins/action/organizations_appliance_dns_local_profiles - new plugin.
- plugins/action/organizations_appliance_dns_local_profiles_assignments_bulk_create - new plugin.
- plugins/action/organizations_appliance_dns_local_profiles_assignments_bulk_delete - new plugin.
- plugins/action/organizations_appliance_dns_local_profiles_assignments_info - new plugin.
- plugins/action/organizations_appliance_dns_local_profiles_info - new plugin.
- plugins/action/organizations_appliance_dns_local_records - new plugin.
- plugins/action/organizations_appliance_dns_local_records_info - new plugin.
- plugins/action/organizations_appliance_dns_split_profiles - new plugin.
- plugins/action/organizations_appliance_dns_split_profiles_assignments_bulk_create - new plugin.
- plugins/action/organizations_appliance_dns_split_profiles_assignments_bulk_delete - new plugin.
- plugins/action/organizations_appliance_dns_split_profiles_assignments_info - new plugin.
- plugins/action/organizations_appliance_dns_split_profiles_info - new plugin.
- plugins/action/organizations_appliance_firewall_multicast_forwarding_by_network_info - new plugin.
- plugins/action/organizations_devices_controller_migrations - new plugin.
- plugins/action/organizations_devices_controller_migrations_info - new plugin.
- plugins/action/organizations_devices_system_memory_usage_history_by_interval_info - new plugin.
- plugins/action/organizations_integrations_xdr_networks_disable - new plugin.
- plugins/action/organizations_integrations_xdr_networks_enable - new plugin.
- plugins/action/organizations_integrations_xdr_networks_info - new plugin.
- plugins/action/organizations_switch_ports_usage_history_by_device_by_interval_info - new plugin.
- plugins/action/organizations_wireless_devices_power_mode_history_info - new plugin.
- plugins/action/organizations_wireless_devices_system_cpu_load_history_info - new plugin.
- plugins/action/organizations_wireless_ssids_firewall_isolation_allowlist_entries - new plugin.
- plugins/action/organizations_wireless_ssids_firewall_isolation_allowlist_entries_info - new plugin.

cloud.common
~~~~~~~~~~~~

- Bump version of ansible-lint to minimum 25.1.2
- module_utils/turbo/module - Add support for 2.19 by returning a json compatible arg obj instead of a dict if possible (https://github.com/ansible-collections/cloud.common/pull/167).
- module_utils/turbo/server - Add support for 2.19 by making FakeStdin implement the IOBase ABC (https://github.com/ansible-collections/cloud.common/pull/167).

community.aws
~~~~~~~~~~~~~

- Bump version of ansible-lint to 25.1.2.
- aws_ssm - Move the ``aws_ssm`` connection plugin's plugin_utils into a dedicated folder (https://github.com/ansible-collections/community.aws/pull/2279).
- aws_ssm - Refactor S3 operations methods for improved clarity (https://github.com/ansible-collections/community.aws/pull/2275).
- aws_ssm - Refactor connection/aws_ssm to add new TerminalManager class and move relevant methods to the new class (https://github.com/ansible-collections/community.aws/pull/2270).
- aws_ssm - Refactor connection/aws_ssm to add new ``FileTransferManager`` class and move relevant methods to the new class (https://github.com/ansible-collections/community.aws/pull/2273).
- aws_ssm - Refactor connection/aws_ssm to add new ``SSMSessionManager`` and ``ProcessManager`` classes and move relevant methods to the new class (https://github.com/ansible-collections/community.aws/pull/2272).

community.docker
~~~~~~~~~~~~~~~~

- docker_container_copy_into - add ``mode_parse`` parameter which determines how ``mode`` is parsed (https://github.com/ansible-collections/community.docker/pull/1074).

community.general
~~~~~~~~~~~~~~~~~

- cobbler inventory plugin - add ``connection_timeout`` option to specify the connection timeout to the cobbler server (https://github.com/ansible-collections/community.general/pull/11063).
- cobbler inventory plugin - add ``facts_level`` option to allow requesting fully rendered variables for Cobbler systems (https://github.com/ansible-collections/community.general/issues/9419, https://github.com/ansible-collections/community.general/pull/9975).
- ini_file - modify an inactive option also when there are spaces in front of the comment symbol (https://github.com/ansible-collections/community.general/pull/10102, https://github.com/ansible-collections/community.general/issues/8539).
- pipx - parameter ``name`` now accepts Python package specifiers (https://github.com/ansible-collections/community.general/issues/7815, https://github.com/ansible-collections/community.general/pull/10031).
- pipx module_utils - filtering application list by name now happens in the modules (https://github.com/ansible-collections/community.general/pull/10031).
- pipx_info - filtering application list by name now happens in the module  (https://github.com/ansible-collections/community.general/pull/10031).

community.grafana
~~~~~~~~~~~~~~~~~

- Add argument `tls_servername` for `grafana_datasource`
- Support `alertmanager` as type for `grafana_datasource`
- grafana_dashboard - allow creating dashboards in subfolders

hitachivantara.vspone_block
~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Added back 'mu_number' parameter to the `hv_gad` module.
- Added iSCSI target support for GAD, TrueCopy, HUR, ShadowImage, and Snapshot/ThinImage modules.
- Added new module `hv_ddp_pool_facts` to retrieve DDP-based pool details on VSP One Block storage models.
- Added new module `hv_ddp_pool` to create, update, and delete DDP-based pools on VSP One Block storage models.
- Added support to delete SVOL post-pair deletion for GAD, TrueCopy, HUR, ShadowImage, and Snapshot/ThinImage modules.
- Enhanced `hv_ldev_facts` module to support query parameters.
- Enhanced `hv_shadow_image` module: support for local copy group and copy pair name for shadow image pair management; group management of shadow image pairs.
- Enhanced `hv_snapshot_group` module to support retention period.
- Enhanced `hv_snapshot` module: added copy speed, clones automation, retention period, support for Floating Snapshot, and pair creation with specific or auto-selected SVOL and mirror unit.
- Enhanced `hv_storage_port` module to support attributes like connection, speed, and type.
- Removed gateway connection type from all the modules.
- Resolved various documentation inconsistencies.

kubernetes.core
~~~~~~~~~~~~~~~

- Bump version of ansible-lint to 25.1.2 (https://github.com/ansible-collections/kubernetes.core/pull/919).
- action/k8s_info - update templating mechanism with changes from ``ansible-core 2.19`` (https://github.com/ansible-collections/kubernetes.core/pull/888).
- helm - add reset_then_reuse_values support to helm module (https://github.com/ansible-collections/kubernetes.core/issues/803).
- helm - add support for ``insecure_skip_tls_verify`` option to helm and helm_repository(https://github.com/ansible-collections/kubernetes.core/issues/694).

lowlydba.sqlserver
~~~~~~~~~~~~~~~~~~

- Added support for Ansible 2.19
- Updated the test matrix to include Ansible 2.19 and remove Ansible 2.16

microsoft.ad
~~~~~~~~~~~~

- Set minimum supported Ansible version to 2.16 to align with the versions still supported by Ansible.

netapp.storagegrid
~~~~~~~~~~~~~~~~~~

- na_sg_grid_ha_group - added check mode support in the module.
- na_sg_org_container - Enhanced the Consistency setting.
- na_sg_org_container - new option `capacity_limit` added for bucket, requires storageGRID 11.9 or later.

purestorage.flashblade
~~~~~~~~~~~~~~~~~~~~~~

- purefb_ad - Add support for Global Catalog Servers
- purefb_dns - Added support for multiple DNS configurations.
- purefb_ds - SMB directory services deprecated from Purity//FB 4.5.2
- purefb_info - Add support for Active Directory Global Catalog Servers
- purefb_info - Added snapshot creation date-time and time_remaining, if snapshot is not deleted, to the ``snapshots`` response.
- purefb_info - Added support for multiple DNS configurations.
- purefb_policy - Snapshot policies can now have specific filesystems and/or replica links added or deletred from the policy
- purefb_proxy - Added support to update existing proxy
- purefb_proxy - Updated to REST v2
- purefb_s3user - Changed ``key_state`` state to be ``keystate`` as ``key_state`` is reserved.
- purefb_s3user - Changed ``remove_key`` parameter to ``key_name`` and add new ``state`` of ``key_state`` to allow a specificed key to be enabled/disabled using the new parameter ``enable_key``.
- purefb_s3user - Updated failure messages for applying policies to an object user account.
- purefb_subnet - ``prefix`` removed as a required parameter for updating an existing subnet

Breaking Changes / Porting Guide
--------------------------------

netapp.storagegrid
~~~~~~~~~~~~~~~~~~

- all modules - added ability to authenticate using `username/password` and `tenant_id` (for Tenant) in the module.

Deprecated Features
-------------------

community.general
~~~~~~~~~~~~~~~~~

- The proxmox content (modules and plugins) is being moved to the `new collection community.proxmox <https://github.com/ansible-collections/community.proxmox>`__. In community.general 11.0.0, these modules and plugins will be replaced by deprecated redirections to community.proxmox. You need to explicitly install community.proxmox, for example with ``ansible-galaxy collection install community.proxmox``. We suggest to update your roles and playbooks to use the new FQCNs as soon as possible to avoid getting deprecation messages (https://github.com/ansible-collections/community.general/pull/10109).
- pipx module_utils - function ``make_process_list()`` is deprecated and will be removed in community.general 13.0.0 (https://github.com/ansible-collections/community.general/pull/10031).

Bugfixes
--------

Ansible-core
~~~~~~~~~~~~

- Ansible will now ensure predictable permissions on remote artifacts, until now it only ensured executable and relied on system masks for the rest.
- ansible-doc - fix indentation for first line of descriptions of suboptions and sub-return values (https://github.com/ansible/ansible/pull/84690).
- ansible-doc - fix line wrapping for first line of description of options and return values (https://github.com/ansible/ansible/pull/84690).
- dnf5 - avoid generating excessive transaction entries in the dnf5 history (https://github.com/ansible/ansible/issues/85046)
- dnf5 - when ``bugfix`` and/or ``security`` is specified, skip packages that do not have any such updates, even for new versions of libdnf5 where this functionality changed and it is considered failure
- script - Fix up become support for Windows scripts when become was set through host variables and not on the task directly - https://github.com/ansible/ansible/issues/85076

amazon.aws
~~~~~~~~~~

- iam_user_info - Actually call GetUser when only user name is supplied instead of listing and filtering from all users (https://github.com/ansible-collections/amazon.aws/pull/2567).
- iam_user_info - Actually filter users by path prefix when one is provided (https://github.com/ansible-collections/amazon.aws/pull/2567).
- route53_info - removes jijna delimiters from example using when (https://github.com/ansible-collections/amazon.aws/issues/2594).

cisco.meraki
~~~~~~~~~~~~

- cisco.meraki.devices_switch_ports - fix get_object_by_name method.

community.crypto
~~~~~~~~~~~~~~~~

- luks_device - mark parameter ``passphrase_encoding`` as ``no_log=False`` to avoid confusing warning (https://github.com/ansible-collections/community.crypto/pull/867).
- luks_device - removing a specific keyslot with ``remove_keyslot`` caused the module to hang while cryptsetup was waiting for a passphrase from stdin, while the module did not supply one. Since a keyslot is not necessary, do not provide one (https://github.com/ansible-collections/community.crypto/issues/864, https://github.com/ansible-collections/community.crypto/pull/868).

community.dns
~~~~~~~~~~~~~

- Update Public Suffix List.

community.general
~~~~~~~~~~~~~~~~~

- cobbler_system - fix bug with Cobbler >= 3.4.0 caused by giving more than 2 positional arguments to ``CobblerXMLRPCInterface.get_system_handle()`` (https://github.com/ansible-collections/community.general/issues/8506, https://github.com/ansible-collections/community.general/pull/10145).
- kdeconfig - allow option values beginning with a dash (https://github.com/ansible-collections/community.general/issues/10127, https://github.com/ansible-collections/community.general/pull/10128).
- keycloak_user_rolemapping - fix ``--diff`` mode (https://github.com/ansible-collections/community.general/issues/10067, https://github.com/ansible-collections/community.general/pull/10075).
- pickle cache plugin - avoid extra JSON serialization with ansible-core >= 2.19 (https://github.com/ansible-collections/community.general/pull/10136).
- proxmox - fix crash in module when the used on an existing LXC container with ``state=present`` and ``force=true`` (https://github.com/ansible-collections/community.proxmox/pull/91, https://github.com/ansible-collections/community.general/pull/10155).
- rundeck_acl_policy - ensure that project ACLs are sent to the correct endpoint (https://github.com/ansible-collections/community.general/pull/10097).
- sysrc - split the output of ``sysrc -e -a`` on the first ``=`` only (https://github.com/ansible-collections/community.general/issues/10120, https://github.com/ansible-collections/community.general/pull/10121).

community.grafana
~~~~~~~~~~~~~~~~~

- Remove field `apiVersion` from return of current `grafana_datasource` for working diff
- grafana_dashboard - add uid to payload
- test: replace more deprecated `TestCase.assertEquals` to support Python 3.12

community.postgresql
~~~~~~~~~~~~~~~~~~~~

- postgresql_alter_system - fix failure when max_val contains a huge number written in scientific notation (https://github.com/ansible-collections/community.postgresql/issues/853).

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- idrac_system_info - (Issue 812) - idrac_system_info fails on iDRAC10.

google.cloud
~~~~~~~~~~~~

- gcp_compute - fixed get_project_disks to process all responses (https://github.com/ansible-collections/google.cloud/pull/677).
- updated README to match required format (https://github.com/ansible-collections/google.cloud/pull/682).

kubernetes.core
~~~~~~~~~~~~~~~

- module_utils/k8s/service - fix issue when trying to delete resource using `delete_options` and `check_mode=true` (https://github.com/ansible-collections/kubernetes.core/issues/892).

microsoft.ad
~~~~~~~~~~~~

- ldap inventory - Fix up support for Ansible 2.19.

netapp.storagegrid
~~~~~~~~~~~~~~~~~~

- na_sg_org_user - fix where existing users with no groups attached were not getting any groups added.

purestorage.flashblade
~~~~~~~~~~~~~~~~~~~~~~

- purefb_bucket - Resolved issue with removing bucket quota
- purefb_info - Fixed issue after SMD Directory Services no longer avaible from REST 2.16
- purefb_policy - Fixed creation of snapshot policies with assigned filesystems and/or replica links
- purefb_s3acc - Fixed issue with public access config settings not being correctly for an account

Known Issues
------------

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- idrac_diagnostics - Issue(285322) - This module doesn't support export of diagnostics file to HTTP and HTTPS share via SOCKS proxy.
- idrac_firmware - Issue(279282) - This module does not support firmware update using HTTP, HTTPS, and FTP shares with authentication on iDRAC8.
- ome_smart_fabric_uplink - Issue(186024) - The module supported by OpenManage Enterprise Modular, however it does not allow the creation of multiple uplinks of the same name. If an uplink is created using the same name as an existing uplink, then the existing uplink is modified.

New Plugins
-----------

Callback
~~~~~~~~

- community.general.print_task - Prints playbook task snippet to job output.

Filter
~~~~~~

- community.general.to_prettytable - Format a list of dictionaries as an ASCII table.

New Modules
-----------

community.general
~~~~~~~~~~~~~~~~~

- community.general.xdg_mime - Set default handler for MIME types, for applications using XDG tools.

community.hrobot
~~~~~~~~~~~~~~~~

- community.hrobot.storagebox_snapshot - Create, update, or delete a snapshot of a storage box.

hitachivantara.vspone_block
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Vsp
^^^

- hitachivantara.vspone_block.hv_ddp_pool - Manages DDP Pools on Hitachi VSP storage systems.
- hitachivantara.vspone_block.hv_ddp_pool_facts - Get facts of DDP Pools on Hitachi VSP storage systems.

netapp.storagegrid
~~~~~~~~~~~~~~~~~~

- netapp.storagegrid.na_sg_grid_alert_receiver - NetApp StorageGRID manage alert receiver.
- netapp.storagegrid.na_sg_grid_audit_destination - Configure audit log destinations on StorageGRID.
- netapp.storagegrid.na_sg_grid_autosupport - Configure autosupport on StorageGRID.
- netapp.storagegrid.na_sg_grid_domain_name - Configure endpoint domain name on StorageGRID.
- netapp.storagegrid.na_sg_grid_hotfix - Apply hotfixes on StorageGRID.
- netapp.storagegrid.na_sg_grid_proxy_settings - NetApp StorageGRID manage proxy settings for the grid.
- netapp.storagegrid.na_sg_grid_snmp - Configure SNMP agent on StorageGRID.
- netapp.storagegrid.na_sg_grid_tenant - NetApp StorageGRID manage tenant accounts.
- netapp.storagegrid.na_sg_grid_vlan_interface - Configure VLAN interface on StorageGRID.
- netapp.storagegrid.na_sg_org_bucket - Manage buckets on StorageGRID.

purestorage.flashblade
~~~~~~~~~~~~~~~~~~~~~~

- purestorage.flashblade.purefb_bucket_access - Manage FlashBlade bucket access policies
- purestorage.flashblade.purefb_fleet - Manage Fusion Fleet
- purestorage.flashblade.purefb_server - Manage FlashBlade servers

Unchanged Collections
---------------------

- ansible.netcommon (still version 7.2.0)
- ansible.posix (still version 1.6.2)
- ansible.utils (still version 5.1.2)
- ansible.windows (still version 2.8.0)
- arista.eos (still version 10.1.1)
- awx.awx (still version 24.6.1)
- azure.azcollection (still version 3.3.1)
- check_point.mgmt (still version 6.4.0)
- chocolatey.chocolatey (still version 1.5.3)
- cisco.aci (still version 2.11.0)
- cisco.asa (still version 6.1.0)
- cisco.dnac (still version 6.31.3)
- cisco.ios (still version 9.2.0)
- cisco.iosxr (still version 10.3.1)
- cisco.ise (still version 2.10.0)
- cisco.mso (still version 2.10.0)
- cisco.nxos (still version 9.4.0)
- cisco.ucs (still version 1.16.0)
- cloudscale_ch.cloud (still version 2.4.1)
- community.ciscosmb (still version 1.0.10)
- community.digitalocean (still version 1.27.0)
- community.hashi_vault (still version 6.2.0)
- community.library_inventory_filtering_v1 (still version 1.1.1)
- community.libvirt (still version 1.3.1)
- community.mongodb (still version 1.7.9)
- community.mysql (still version 3.13.0)
- community.network (still version 5.1.0)
- community.okd (still version 4.0.1)
- community.proxysql (still version 1.6.0)
- community.rabbitmq (still version 1.4.0)
- community.routeros (still version 3.6.0)
- community.sap_libs (still version 1.4.2)
- community.sops (still version 2.0.5)
- community.vmware (still version 5.6.0)
- community.windows (still version 2.4.0)
- community.zabbix (still version 3.3.0)
- containers.podman (still version 1.16.3)
- cyberark.conjur (still version 1.3.3)
- dellemc.enterprise_sonic (still version 2.5.1)
- dellemc.powerflex (still version 2.6.0)
- dellemc.unity (still version 2.0.0)
- f5networks.f5_modules (still version 1.35.0)
- fortinet.fortimanager (still version 2.9.1)
- fortinet.fortios (still version 2.4.0)
- grafana.grafana (still version 5.7.0)
- hetzner.hcloud (still version 4.3.0)
- ibm.qradar (still version 4.0.0)
- ibm.spectrum_virtualize (still version 2.0.0)
- ibm.storage_virtualize (still version 2.7.3)
- ieisystem.inmanage (still version 3.0.0)
- infinidat.infinibox (still version 1.4.5)
- infoblox.nios_modules (still version 1.8.0)
- inspur.ispim (still version 2.2.3)
- junipernetworks.junos (still version 9.1.0)
- kaytus.ksmanage (still version 2.0.0)
- microsoft.iis (still version 1.0.2)
- netapp.cloudmanager (still version 21.24.0)
- netapp.ontap (still version 22.14.0)
- netapp_eseries.santricity (still version 1.4.1)
- netbox.netbox (still version 3.21.0)
- ngine_io.cloudstack (still version 2.5.0)
- openstack.cloud (still version 2.4.1)
- ovirt.ovirt (still version 3.2.0)
- purestorage.flasharray (still version 1.34.1)
- sensu.sensu_go (still version 1.14.0)
- splunk.es (still version 4.0.0)
- telekom_mms.icinga_director (still version 2.2.2)
- theforeman.foreman (still version 4.2.0)
- vmware.vmware (still version 1.11.0)
- vmware.vmware_rest (still version 4.7.0)
- vultr.cloud (still version 1.13.0)
- vyos.vyos (still version 5.0.0)
- wti.remote (still version 1.0.10)

v11.5.0
=======

.. contents::
  :local:
  :depth: 2

Release Summary
---------------

Release Date: 2025-04-22

`Porting Guide <https://docs.ansible.com/ansible/devel/porting_guides.html>`_

Added Collections
-----------------

- hitachivantara.vspone_block (version 3.3.0)
- microsoft.iis (version 1.0.2)

Ansible-core
------------

Ansible 11.5.0 contains ansible-core version 2.18.5.
This is a newer version than version 2.18.4 contained in the previous Ansible release.

The changes are reported in the combined changelog below.

Changed Collections
-------------------

If not mentioned explicitly, the changes are reported in the combined changelog below.

+------------------------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| Collection                               | Ansible 11.4.0 | Ansible 11.5.0 | Notes                                                                                                                        |
+==========================================+================+================+==============================================================================================================================+
| amazon.aws                               | 9.3.0          | 9.4.0          |                                                                                                                              |
+------------------------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| ansible.netcommon                        | 7.1.0          | 7.2.0          |                                                                                                                              |
+------------------------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.aci                                | 2.10.1         | 2.11.0         |                                                                                                                              |
+------------------------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.dnac                               | 6.31.0         | 6.31.3         |                                                                                                                              |
+------------------------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.ios                                | 9.1.2          | 9.2.0          |                                                                                                                              |
+------------------------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.iosxr                              | 10.3.0         | 10.3.1         |                                                                                                                              |
+------------------------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.meraki                             | 2.20.8         | 2.20.10        |                                                                                                                              |
+------------------------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.mso                                | 2.9.0          | 2.10.0         |                                                                                                                              |
+------------------------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.nxos                               | 9.3.0          | 9.4.0          |                                                                                                                              |
+------------------------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.ucs                                | 1.15.0         | 1.16.0         | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+------------------------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.aws                            | 9.1.0          | 9.2.0          |                                                                                                                              |
+------------------------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.dns                            | 3.2.2          | 3.2.3          |                                                                                                                              |
+------------------------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.general                        | 10.5.0         | 10.6.0         |                                                                                                                              |
+------------------------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.library_inventory_filtering_v1 | 1.0.2          | 1.1.1          |                                                                                                                              |
+------------------------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.postgresql                     | 3.12.0         | 3.14.0         |                                                                                                                              |
+------------------------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.routeros                       | 3.5.0          | 3.6.0          |                                                                                                                              |
+------------------------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.sops                           | 2.0.3          | 2.0.5          |                                                                                                                              |
+------------------------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.vmware                         | 5.5.0          | 5.6.0          |                                                                                                                              |
+------------------------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| dellemc.openmanage                       | 9.10.0         | 9.11.0         |                                                                                                                              |
+------------------------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| f5networks.f5_modules                    | 1.34.1         | 1.35.0         |                                                                                                                              |
+------------------------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| fortinet.fortios                         | 2.3.9          | 2.4.0          |                                                                                                                              |
+------------------------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| hitachivantara.vspone_block              |                | 3.3.0          | The collection was added to Ansible                                                                                          |
+------------------------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| ibm.storage_virtualize                   | 2.6.0          | 2.7.3          |                                                                                                                              |
+------------------------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| kubernetes.core                          | 5.1.0          | 5.2.0          |                                                                                                                              |
+------------------------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| lowlydba.sqlserver                       | 2.5.0          | 2.6.0          |                                                                                                                              |
+------------------------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| microsoft.ad                             | 1.8.0          | 1.8.1          |                                                                                                                              |
+------------------------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| microsoft.iis                            |                | 1.0.2          | The collection was added to Ansible                                                                                          |
+------------------------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| purestorage.flasharray                   | 1.33.1         | 1.34.1         |                                                                                                                              |
+------------------------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| vmware.vmware                            | 1.10.1         | 1.11.0         |                                                                                                                              |
+------------------------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| vmware.vmware_rest                       | 4.6.0          | 4.7.0          |                                                                                                                              |
+------------------------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+

Major Changes
-------------

fortinet.fortios
~~~~~~~~~~~~~~~~

- Supported new versions 7.6.1 and 7.6.2.
- Updated the examples with correct values that have minimum or maximum values.

Minor Changes
-------------

amazon.aws
~~~~~~~~~~

- inventory/aws_ec2 - Update templating mechanism to support ansible-core 2.19 changes (https://github.com/ansible-collections/amazon.aws/pull/2552).

ansible.netcommon
~~~~~~~~~~~~~~~~~

- Exposes new libssh options to configure publickey_accepted_algorithms and hostkeys. This requires ansible-pylibssh v1.1.0 or higher.

cisco.aci
~~~~~~~~~

- Add aci_endpoint_tag_ip and aci_endpoint_tag_mac modules to manage Endpoint IP and MAC Tags.
- Add aci_ip_sla_monitoring_policy module.
- Add management_epg and management_epg_type attributes in aci_dns_profile module.
- Add stratum attribute to aci_ntp_policy module.
- Add support for Ansible 2.18 and dropped support for Ansible 2.15 as required by Ansible Galaxy.

cisco.dnac
~~~~~~~~~~

- .ansible-lint is added to handle a formatting issue in Red Hat.
- The file format was changed to conform to the requested standards.
- noqa all is used to ignore rules in some files.

cisco.ios
~~~~~~~~~

- Add ios_evpn_ethernet resource module.

cisco.mso
~~~~~~~~~

- Add ep_move_detection_mode attribute in mso_schema_template_bd.
- Add mso_schema_template_anp_epg_annotation module.
- Add mso_schema_template_anp_epg_intra_epg_contract module.
- Add name attribute to mso_schema_template_external_epg_subnet module.
- Add ndo_ipsla_track_list and ndo_ipsla_monitoring_policy modules.
- Add ndo_l3out_node_routing_policy, ndo_l3out_interface_routing_policy, and ndo_tenant_bgp_peer_prefix_policy modules.
- Add ndo_l3out_template, ndo_l3out_annotation, ndo_l3out_interface_group_policy, and ndo_l3out_node_group_policy modules.
- Add ndo_mcp_global_policy module.
- Add ndo_ntp_policy, ndo_ptp_policy, and ndo_ptp_policy_profiles modules.
- Add ndo_physical_interface, ndo_port_channel_interface, ndo_virtual_port_channel_interface, ndo_node_profile, and ndo_fex_device modules to support NDO Fabric Resource Policies.
- Add ndo_qos_dscp_cos_translation_policy module.
- Add ndo_synce_interface_policy, ndo_interface_setting, ndo_node_setting, and ndo_macsec_policy modules.
- Add ndo_tenant_custom_qos_policy module.
- Add ndo_tenant_igmp_interface_policy, ndo_tenant_igmp_snooping_policy, and ndo_tenant_mld_snooping_policy modules.
- Add qos_level attribute to the mso_schema_template_external_epg module.
- Add support for Ansible 2.18 and dropped support for Ansible 2.15 as required by Ansible Galaxy.
- Add support for site configuration for tenant policy template in ndo_template module.

cisco.nxos
~~~~~~~~~~

- nxos_vpc - Added support for peer-switch feature configuration.

community.aws
~~~~~~~~~~~~~

- aws_ssm - Refactor ``_exec_transport_commands``, ``_generate_commands``, and ``_exec_transport_commands`` methods for improved clarity (https://github.com/ansible-collections/community.aws/pull/2248).
- aws_ssm - Refactor connection/aws_ssm to add new S3ClientManager class and move relevant methods to the new class (https://github.com/ansible-collections/community.aws/pull/2255).
- aws_ssm - Refactor display/verbosity-related methods in aws_ssm to simplify the code and avoid repetition (https://github.com/ansible-collections/community.aws/pull/2264).

community.general
~~~~~~~~~~~~~~~~~

- apache2_module - added workaround for new PHP module name, from ``php7_module`` to ``php_module`` (https://github.com/ansible-collections/community.general/pull/9951).
- gitlab_project - add option ``build_timeout`` (https://github.com/ansible-collections/community.general/pull/9960).
- gitlab_project_members - extend choices parameter ``access_level`` by missing upstream valid value ``owner`` (https://github.com/ansible-collections/community.general/pull/9953).
- hpilo_boot - add option to get an idempotent behavior while powering on server, resulting in success instead of failure when using ``state: boot_once`` option (https://github.com/ansible-collections/community.general/pull/9646).
- idrac_redfish_command, idrac_redfish_config, idrac_redfish_info - add ``validate_certs``, ``ca_path``, and ``ciphers`` options to configure TLS/SSL (https://github.com/ansible-collections/community.general/issues/3686, https://github.com/ansible-collections/community.general/pull/9964).
- ilo_redfish_command, ilo_redfish_config, ilo_redfish_info - add ``validate_certs``, ``ca_path``, and ``ciphers`` options to configure TLS/SSL (https://github.com/ansible-collections/community.general/issues/3686, https://github.com/ansible-collections/community.general/pull/9964).
- keycloak module_utils - user groups can now be referenced by their name, like ``staff``, or their path, like ``/staff/engineering``. The path syntax allows users to reference subgroups, which is not possible otherwise (https://github.com/ansible-collections/community.general/pull/9898).
- keycloak_user module - user groups can now be referenced by their name, like ``staff``, or their path, like ``/staff/engineering``. The path syntax allows users to reference subgroups, which is not possible otherwise (https://github.com/ansible-collections/community.general/pull/9898).
- nmcli - add support for Infiniband MAC setting when ``type`` is ``infiniband`` (https://github.com/ansible-collections/community.general/pull/9962).
- one_vm - update allowed values for ``updateconf`` to include new parameters as per the latest OpenNebula API documentation.
  Added parameters:

  * ``OS``: ``FIRMWARE``;
  * ``CPU_MODEL``: ``MODEL``, ``FEATURES``;
  * ``FEATURES``: ``VIRTIO_BLK_QUEUES``, ``VIRTIO_SCSI_QUEUES``, ``IOTHREADS``;
  * ``GRAPHICS``: ``PORT``, ``COMMAND``;
  * ``VIDEO``: ``ATS``, ``IOMMU``, ``RESOLUTION``, ``TYPE``, ``VRAM``;
  * ``RAW``: ``VALIDATE``;
  * ``BACKUP_CONFIG``: ``FS_FREEZE``, ``KEEP_LAST``, ``BACKUP_VOLATILE``, ``MODE``, ``INCREMENT_MODE``.

  (https://github.com/ansible-collections/community.general/pull/9959).
- proxmox and proxmox_kvm modules - allow uppercase characters in VM/container tags (https://github.com/ansible-collections/community.general/issues/9895, https://github.com/ansible-collections/community.general/pull/10024).
- puppet - improve parameter formatting, no impact to user (https://github.com/ansible-collections/community.general/pull/10014).
- redfish module utils - add ``REDFISH_COMMON_ARGUMENT_SPEC``, a corresponding ``redfish`` docs fragment, and support for its ``validate_certs``, ``ca_path``, and ``ciphers`` options (https://github.com/ansible-collections/community.general/issues/3686, https://github.com/ansible-collections/community.general/pull/9964).
- redfish_command, redfish_config, redfish_info - add ``validate_certs`` and ``ca_path`` options to configure TLS/SSL (https://github.com/ansible-collections/community.general/issues/3686, https://github.com/ansible-collections/community.general/pull/9964).
- rocketchat - fix duplicate JSON conversion for Rocket.Chat < 7.4.0 (https://github.com/ansible-collections/community.general/pull/9965).
- wdc_redfish_command, wdc_redfish_info - add ``validate_certs``, ``ca_path``, and ``ciphers`` options to configure TLS/SSL (https://github.com/ansible-collections/community.general/issues/3686, https://github.com/ansible-collections/community.general/pull/9964).
- xcc_redfish_command - add ``validate_certs``, ``ca_path``, and ``ciphers`` options to configure TLS/SSL (https://github.com/ansible-collections/community.general/issues/3686, https://github.com/ansible-collections/community.general/pull/9964).
- zypper - adds ``skip_post_errors`` that allows to skip RPM post-install errors (Zypper return code 107) (https://github.com/ansible-collections/community.general/issues/9972).

community.library_inventory_filtering_v1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Add typing information for the ``inventory_filter`` plugin utils (https://github.com/ansible-collections/community.library_inventory_filtering/pull/22).

community.routeros
~~~~~~~~~~~~~~~~~~

- api_info, api_modify - add ``mdns-repeat-ifaces`` to ``ip dns`` for RouterOS 7.16 and newer (https://github.com/ansible-collections/community.routeros/pull/358).
- api_info, api_modify - field name change in ``routing bgp connection`` path implemented by RouterOS 7.19 and newer (https://github.com/ansible-collections/community.routeros/pull/360).
- api_info, api_modify - rename ``is-responder`` property in ``interface wireguard peers`` to ``responder`` for RouterOS 7.17 and newer (https://github.com/ansible-collections/community.routeros/pull/364).

community.vmware
~~~~~~~~~~~~~~~~

- module_utils.vmware - Move ``vmware_argument_spec`` to a dedicated file (https://github.com/ansible-collections/community.vmware/pull/2370).
- module_utils.vmware_rest_client - Move ``vmware_client_argument_spec`` to a dedicated file (https://github.com/ansible-collections/community.vmware/pull/2370).
- vmware_dvs_portgroup - New option ``network_policy.mac_learning`` to replace ``mac_learning`` (https://github.com/ansible-collections/community.vmware/pull/2360).
- vmware_object_role_permission - Document setting permissions on vCenter level (https://github.com/ansible-collections/community.vmware/pull/2374).

ibm.storage_virtualize
~~~~~~~~~~~~~~~~~~~~~~

- ibm_sv_manage_replication_policy - Added support for highly-available snapshots
- ibm_sv_manage_snapshot- Add support for restoring highly-available volumes and volumegroups from local snapshots
- ibm_sv_manage_truststore_for_replication - Added support for creating truststore for flashsystem grid
- ibm_svc_host - Added support for specifying host location in PBHA, support for FDMI discovery, suppressing offline alert, updating IO groups, and for specifying fcscsi and iscsi protocols during host creation
- ibm_svc_info - Added support for flashsystem grid
- ibm_svc_initial_setup - Added support for vdisk protection settings, iscsiauthmethod and improved REST API calls
- ibm_svc_manage_flashcopy - Added support for enabling cleanrate during flashcopy creation and update
- ibm_svc_manage_replication - Added support for highly-available snapshots
- ibm_svc_manage_volume - Added support for unmapping hosts, remote-copy and flashcopy during volume deletion
- ibm_svc_mdisk - Added support for updating tier
- ibm_svc_mdiskgrp - Improved probe function for storage pools

kubernetes.core
~~~~~~~~~~~~~~~

- k8s - Extend hidden_fields to allow the expression of more complex field types to be hidden (https://github.com/ansible-collections/kubernetes.core/pull/872)
- k8s_info - Extend hidden_fields to allow the expression of more complex field types to be hidden (https://github.com/ansible-collections/kubernetes.core/pull/872)
- waiter.py - add ClusterOperator support. The module can now check OpenShift cluster health by verifying ClusterOperator status requiring 'Available: True', 'Degraded: False', and 'Progressing: False' for success. (https://github.com/ansible-collections/kubernetes.core/issues/869)

lowlydba.sqlserver
~~~~~~~~~~~~~~~~~~

- Added support for contained Availability Groups using dbatools 2.1.15 (https://github.com/lowlydba/lowlydba.sqlserver/pull/249).

purestorage.flasharray
~~~~~~~~~~~~~~~~~~~~~~

- purefa_timeout - Convert to REST v2
- purefa_user - Added parameter for SSH public keys and API token timeout
- purefa_user - Converted to use REST v2
- purefa_user - When changing API token or timout for an existing user, the user role must be provided or it will revert to ``readonly``

vmware.vmware
~~~~~~~~~~~~~

- _module_pyvmomi_base - Make sure to use the folder param when searching for VMs based on other common params in get_vms_using_params
- added vm_resource_info module to collect cpu/memory facts about vms
- clients/_pyvmomi - adds explicit init params instead of using dict
- clients/_rest - adds explicit init params instead of using dict
- esxi_hosts - Add inventory host filtering based on jinja statements
- esxi_hosts inventory - include moid property in output always
- pyvmomi - update object search by name method to use propertycollector, which speeds up results significantly
- upload_content_library_ovf - Add module to upload an ovf/ova to a content library
- vm_powerstate - migrate vmware_guest_powerstate module from community to here
- vms - Add inventory host filtering based on jinja statements
- vms inventory - include moid property in output always

vmware.vmware_rest
~~~~~~~~~~~~~~~~~~

- Deprecated modules with redundant functionality in vmware.vmware. The next major release is currently not planned, so no removal date is provided. See https://github.com/ansible-collections/vmware.vmware_rest/issues/589

Deprecated Features
-------------------

ansible.netcommon
~~~~~~~~~~~~~~~~~

- Added deprecation warnings for the above plugins, displayed when running respective filter plugins.
- `parse_cli_textfsm` filter plugin is deprecated and will be removed in a future release after 2027-02-01. Use `ansible.utils.cli_parse` with the `ansible.utils.textfsm_parser` parser as a replacement.
- `parse_cli` filter plugin is deprecated and will be removed in a future release after 2027-02-01. Use `ansible.utils.cli_parse` as a replacement.
- `parse_xml` filter plugin is deprecated and will be removed in a future release after 2027-02-01. Use `ansible.utils.cli_parse` with the `ansible.utils.xml_parser` parser as a replacement.

cisco.ios
~~~~~~~~~

- ios_vlans - deprecate mtu, please use ios_interfaces to configure mtu to the interface where vlans is applied.

community.general
~~~~~~~~~~~~~~~~~

- manifold lookup plugin - plugin is deprecated and will be removed in community.general 11.0.0 (https://github.com/ansible-collections/community.general/pull/10028).
- stackpath_compute inventory plugin - plugin is deprecated and will be removed in community.general 11.0.0 (https://github.com/ansible-collections/community.general/pull/10026).

community.postgresql
~~~~~~~~~~~~~~~~~~~~

- postgresql_copy - the parameter aliases db and database are deprecated and will be removed in community.postgresql 5.0.0. Use login_db instead.
- postgresql_db - the ``rename`` choice of the state option is deprecated and will be removed in version 5.0.0, use the ``postgresql_query`` module instead.
- postgresql_ext - the parameter aliases db and database are deprecated and will be removed in community.postgresql 5.0.0. Use login_db instead.
- postgresql_idx - the parameter aliases db and database are deprecated and will be removed in community.postgresql 5.0.0. Use login_db instead.
- postgresql_membership - the parameter aliases db and database are deprecated and will be removed in community.postgresql 5.0.0. Use login_db instead.
- postgresql_owner - the parameter aliases db and database are deprecated and will be removed in community.postgresql 5.0.0. Use login_db instead.
- postgresql_ping - the parameter aliases db and database are deprecated and will be removed in community.postgresql 5.0.0. Use login_db instead.
- postgresql_privs - the parameter aliases db and database are deprecated and will be removed in community.postgresql 5.0.0. Use login_db instead.
- postgresql_publication - the parameter aliases db and database are deprecated and will be removed in community.postgresql 5.0.0. Use login_db instead.
- postgresql_query - the parameter aliases db and database are deprecated and will be removed in community.postgresql 5.0.0. Use login_db instead.
- postgresql_schema - the parameter aliases db and database are deprecated and will be removed in community.postgresql 5.0.0. Use login_db instead.
- postgresql_script - the parameter aliases db and database are deprecated and will be removed in community.postgresql 5.0.0. Use login_db instead.
- postgresql_sequence - the ``rename_to`` option is deprecated and will be removed in version 5.0.0, use the ``postgresql_query`` module instead.
- postgresql_sequence - the parameter aliases db and database are deprecated and will be removed in community.postgresql 5.0.0. Use login_db instead.
- postgresql_set - the parameter aliases db and database are deprecated and will be removed in community.postgresql 5.0.0. Use login_db instead.
- postgresql_slot - the parameter aliases db and database are deprecated and will be removed in community.postgresql 5.0.0. Use login_db instead.
- postgresql_subscription - the parameter aliases db and database are deprecated and will be removed in community.postgresql 5.0.0. Use login_db instead.
- postgresql_table - the ``rename`` option is deprecated and will be removed in version 5.0.0, use the ``postgresql_query module`` instead.
- postgresql_table - the parameter aliases db and database are deprecated and will be removed in community.postgresql 5.0.0. Use login_db instead.
- postgresql_tablespace - the ``rename_to`` option is deprecated and will be removed in version 5.0.0, use the ``postgresql_query`` module instead.
- postgresql_tablespace - the parameter aliases db and database are deprecated and will be removed in community.postgresql 5.0.0. Use login_db instead.
- postgresql_user_obj_stat_info - the parameter aliases db and database are deprecated and will be removed in community.postgresql 5.0.0. Use login_db instead.

community.vmware
~~~~~~~~~~~~~~~~

- vmware_dvs_portgroup - ``mac_learning`` is deprecated in favour of ``network_policy.mac_learning`` (https://github.com/ansible-collections/community.vmware/pull/2360).

Bugfixes
--------

Ansible-core
~~~~~~~~~~~~

- build - Pin ``wheel`` in ``pyproject.toml`` to ensure compatibility with supported ``setuptools`` versions.
- dnf5 - Handle forwarded exceptions from dnf5-5.2.13 where a generic ``RuntimeError`` was previously raised
- find - skip ENOENT error code while recursively enumerating files. find module will now be tolerant to race conditions that remove files or directories from the target it is currently inspecting. (https://github.com/ansible/ansible/issues/84873).
- gather_facts action, will now add setup when 'smart' appears with other modules in the FACTS_MODULES setting (#84750).
- uri - Form location correctly when the server returns a relative redirect (https://github.com/ansible/ansible/issues/84540)

amazon.aws
~~~~~~~~~~

- lookup/aws_account_attribute - plugin should return a list when ``wantlist=True`` (https://github.com/ansible-collections/amazon.aws/pull/2552).

ansible.netcommon
~~~~~~~~~~~~~~~~~

- libssh connection plugin - stop using long-deprecated and now removed internal field from ansible-core's base connection plugin class (https://github.com/ansible-collections/ansible.netcommon/issues/522, https://github.com/ansible-collections/ansible.netcommon/issues/690, https://github.com/ansible-collections/ansible.netcommon/pull/691).

cisco.aci
~~~~~~~~~

- Fix aci_rest module to only add annotation when the value is a dictionary
- Fix payload to define the correct vPC member side in aci_l3out_logical_interface_vpc_member (#663)
- Fix subclass issue in aci_domain_to_vlan_pool to fix deletion of binding (#695)
- Modify interface_configs requirement using required_if dependency for aci_bulk_static_binding_to_epg

cisco.ios
~~~~~~~~~

- ios_logging_global - Fixed issue where cisco.ios.logging_global module was not showing idempotent behaviour when trap was set to informational.
- ios_vlans - Defaut mtu would be captured (1500) and no configuration for mtu is allowed via ios_vlans module.
- ios_vlans - Fixed an issue in the `cisco.ios.ios_vlans` module on Cisco Catalyst 9000 switches where using state:purged generated an incorrect command syntax (`no vlan configuration <vlan_id>` instead of `no vlan <vlan_id>`).
- ios_vlans - Resolved a failure in the `cisco.ios.ios_vlans` module when using state:deleted, where the module incorrectly attempted to remove VLANs using `no mtu <value>`, causing an invalid input error. The fix ensures that the module does not generate `no mtu` commands during VLAN deletion, aligning with the correct VLAN removal behavior on Catalyst 9000 switches.

cisco.iosxr
~~~~~~~~~~~

- Fixes a bug to allow connections to IOS XRd with cliconf.
- Fixes idempotency for static routes with encap interfaces

cisco.meraki
~~~~~~~~~~~~

- Added validation for `radiusServerAttemptsLimit` with choices `[1, 2, 3, 4, 5]`.
- Added validation for `radiusServerTimeout` with a range of valid values `[1-10]`.
- Fixed parameter handling for `update_by_id_params` in cisco.meraki.networks_wireless_ssids to correctly map the following parameters - `perClientBandwidthLimitDown` - `perClientBandwidthLimitUp` - `perSsidBandwidthLimitDown` - `perSsidBandwidthLimitUp` - `defaultVlanId` - `radiusAccountingInterimInterval` - `radiusGuestVlanId` - `vlanId` - `radiusServerAttemptsLimit` - `radiusServerTimeout`
- cisco.meraki.devices_wireless_radio_settings changed compare equality method to use `meraki_compare_equality`
- cisco.meraki.networks_wireless_ssids refactor parameter handling to avoid None values

cisco.mso
~~~~~~~~~

- Fix query results for bulk query to display correct static_paths in mso_schema_site_anp_epg_staticport module
- Fix replace operation for bulk present without force replace in mso_schema_site_anp_epg_staticport module

cisco.nxos
~~~~~~~~~~

- nxos_facts - Fixes an issue in nxos_facts where IPv6 addresses within VRF contexts were not being collected in `net_all_ipv6_addresses`.
- nxos_user - fixes wrong command being generated for purge function
- nxos_vpc - fixes failure due to kickstart_ver_str not being present

community.dns
~~~~~~~~~~~~~

- Update Public Suffix List.

community.general
~~~~~~~~~~~~~~~~~

- dependent look plugin - make compatible with ansible-core's Data Tagging feature (https://github.com/ansible-collections/community.general/pull/9833).
- diy callback plugin - make compatible with ansible-core's Data Tagging feature (https://github.com/ansible-collections/community.general/pull/9833).
- github_deploy_key - check that key really exists on 422 to avoid masking other errors (https://github.com/ansible-collections/community.general/issues/6718, https://github.com/ansible-collections/community.general/pull/10011).
- hashids and unicode_normalize filter plugins - avoid deprecated ``AnsibleFilterTypeError`` on ansible-core 2.19 (https://github.com/ansible-collections/community.general/pull/9992).
- homebrew - emit a useful error message if ``brew info`` reports a package tap is ``null`` (https://github.com/ansible-collections/community.general/pull/10013, https://github.com/ansible-collections/community.general/issues/10012).
- java_cert - the module no longer fails if the optional parameters ``pkcs12_alias`` and ``cert_alias`` are not provided (https://github.com/ansible-collections/community.general/pull/9970).
- keycloak_authentication - fix authentification config duplication for Keycloak < 26.2.0 (https://github.com/ansible-collections/community.general/pull/9987).
- keycloak_client - fix the idempotency regression by normalizing the Keycloak response for ``after_client`` (https://github.com/ansible-collections/community.general/issues/9905, https://github.com/ansible-collections/community.general/pull/9976).
- proxmox inventory plugin - fix ``ansible_host`` staying empty for certain Proxmox nodes (https://github.com/ansible-collections/community.general/issues/5906, https://github.com/ansible-collections/community.general/pull/9952).
- proxmox_disk - fail gracefully if ``storage`` is required but not provided by the user (https://github.com/ansible-collections/community.general/issues/9941, https://github.com/ansible-collections/community.general/pull/9963).
- reveal_ansible_type filter plugin and ansible_type test plugin - make compatible with ansible-core's Data Tagging feature (https://github.com/ansible-collections/community.general/pull/9833).
- sysrc - no longer always reporting ``changed=true`` when ``state=absent``. This fixes the method ``exists()`` (https://github.com/ansible-collections/community.general/issues/10004, https://github.com/ansible-collections/community.general/pull/10005).
- yaml callback plugin - use ansible-core internals to avoid breakage with Data Tagging (https://github.com/ansible-collections/community.general/pull/9833).

community.library_inventory_filtering_v1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- inventory_filter plugin utils - make compatible with ansible-core's Data Tagging feature (https://github.com/ansible-collections/community.library_inventory_filtering/pull/24).
- inventory_plugin plugin util - ``parse_filters`` now filters ``None`` values with allowed keys (https://github.com/ansible-collections/community.library_inventory_filtering/pull/27).

community.postgresql
~~~~~~~~~~~~~~~~~~~~

- postgresql_table - consider schema name when checking for table (https://github.com/ansible-collections/community.postgresql/issues/817).  Table names are only unique within a schema. This allows using the same table name in multiple schemas.

community.sops
~~~~~~~~~~~~~~

- load_vars - make evaluation compatible with Data Tagging in upcoming ansible-core release (https://github.com/ansible-collections/community.sops/pull/225).

community.vmware
~~~~~~~~~~~~~~~~

- vmware_dvs_portgroup - Fix idempotency issue with ``mac_learning`` (https://github.com/ansible-collections/community.vmware/issues/1873).

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- Internal defect fixes were done for the following modules - ``idrac_network_attributes``, ``idrac_certificates``, ``idrac_redfish_storage_controller``, ``idrac_boot_order`` and ``idrac_firmware``
- Resolved the issue in ``idrac_redfish_storage_volume`` module where it returns 404 error on job creation when enabling encryption for virtual drives. (https://github.com/dell/dellemc-openmanage-ansible-modules/issues /713)

f5networks.f5_modules
~~~~~~~~~~~~~~~~~~~~~

- bigip_firewall_address_list to support both cidr and route domain
- bigip_profile_server_ssl to support parent's [None, "", "None"] profiles

fortinet.fortios
~~~~~~~~~~~~~~~~

- Github Issue
- Mantis Issue

ibm.storage_virtualize
~~~~~~~~~~~~~~~~~~~~~~

- ibm_svc_manage_replication - Added checks for mutually-exclusive parameters and policing for updating remote-copy relationship

purestorage.flasharray
~~~~~~~~~~~~~~~~~~~~~~

- purefa_dsrole - Fixed bug with DS role having no group or group base cannot be updated
- purefa_pgsnap - Fixed issue with overwrite failing
- purefa_vg - Fixed idempotency issue when clearing volume group QoS settings
- purefa_vg - Fixed issue with creating non-QoS volume groups
- purefa_vlan - Allow LACP bonds to be subnet interfaces

vmware.vmware
~~~~~~~~~~~~~

- vms inventory - fix handling of VMs within VApps

Known Issues
------------

community.general
~~~~~~~~~~~~~~~~~

- reveal_ansible_type filter plugin and ansible_type test plugin - note that ansible-core's Data Tagging feature implements new aliases, such as ``_AnsibleTaggedStr`` for ``str``, ``_AnsibleTaggedInt`` for ``int``, and ``_AnsibleTaggedFloat`` for ``float`` (https://github.com/ansible-collections/community.general/pull/9833).

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- idrac_diagnostics - Issue(285322) - This module doesn't support export of diagnostics file to HTTP and HTTPS share via SOCKS proxy.
- idrac_firmware - Issue(279282) - This module does not support firmware update using HTTP, HTTPS, and FTP shares with authentication on iDRAC8.
- ome_smart_fabric_uplink - Issue(186024) - The module supported by OpenManage Enterprise Modular, however it does not allow the creation of multiple uplinks of the same name. If an uplink is created using the same name as an existing uplink, then the existing uplink is modified.

New Plugins
-----------

Connection
~~~~~~~~~~

- community.general.wsl - Run tasks in WSL distribution using wsl.exe CLI via SSH.

New Modules
-----------

cisco.ios
~~~~~~~~~

- cisco.ios.ios_evpn_ethernet - Resource module to configure L2VPN EVPN Ethernet Segment.

community.postgresql
~~~~~~~~~~~~~~~~~~~~

- community.postgresql.postgresql_alter_system - Change a PostgreSQL server configuration parameter

ibm.storage_virtualize
~~~~~~~~~~~~~~~~~~~~~~

- ibm.storage_virtualize.ibm_sv_manage_flashsystem_grid - Manages operations of Flashsystem grid containing multiple Storage Virtualize systems

Unchanged Collections
---------------------

- ansible.posix (still version 1.6.2)
- ansible.utils (still version 5.1.2)
- ansible.windows (still version 2.8.0)
- arista.eos (still version 10.1.1)
- awx.awx (still version 24.6.1)
- azure.azcollection (still version 3.3.1)
- check_point.mgmt (still version 6.4.0)
- chocolatey.chocolatey (still version 1.5.3)
- cisco.asa (still version 6.1.0)
- cisco.intersight (still version 2.0.20)
- cisco.ise (still version 2.10.0)
- cloud.common (still version 4.0.0)
- cloudscale_ch.cloud (still version 2.4.1)
- community.ciscosmb (still version 1.0.10)
- community.crypto (still version 2.26.0)
- community.digitalocean (still version 1.27.0)
- community.docker (still version 4.5.2)
- community.grafana (still version 2.1.0)
- community.hashi_vault (still version 6.2.0)
- community.hrobot (still version 2.2.0)
- community.libvirt (still version 1.3.1)
- community.mongodb (still version 1.7.9)
- community.mysql (still version 3.13.0)
- community.network (still version 5.1.0)
- community.okd (still version 4.0.1)
- community.proxysql (still version 1.6.0)
- community.rabbitmq (still version 1.4.0)
- community.sap_libs (still version 1.4.2)
- community.windows (still version 2.4.0)
- community.zabbix (still version 3.3.0)
- containers.podman (still version 1.16.3)
- cyberark.conjur (still version 1.3.3)
- cyberark.pas (still version 1.0.30)
- dellemc.enterprise_sonic (still version 2.5.1)
- dellemc.powerflex (still version 2.6.0)
- dellemc.unity (still version 2.0.0)
- fortinet.fortimanager (still version 2.9.1)
- google.cloud (still version 1.5.1)
- grafana.grafana (still version 5.7.0)
- hetzner.hcloud (still version 4.3.0)
- ibm.qradar (still version 4.0.0)
- ibm.spectrum_virtualize (still version 2.0.0)
- ieisystem.inmanage (still version 3.0.0)
- infinidat.infinibox (still version 1.4.5)
- infoblox.nios_modules (still version 1.8.0)
- inspur.ispim (still version 2.2.3)
- junipernetworks.junos (still version 9.1.0)
- kaytus.ksmanage (still version 2.0.0)
- kubevirt.core (still version 2.1.0)
- netapp.cloudmanager (still version 21.24.0)
- netapp.ontap (still version 22.14.0)
- netapp.storagegrid (still version 21.14.0)
- netapp_eseries.santricity (still version 1.4.1)
- netbox.netbox (still version 3.21.0)
- ngine_io.cloudstack (still version 2.5.0)
- openstack.cloud (still version 2.4.1)
- ovirt.ovirt (still version 3.2.0)
- purestorage.flashblade (still version 1.19.2)
- sensu.sensu_go (still version 1.14.0)
- splunk.es (still version 4.0.0)
- telekom_mms.icinga_director (still version 2.2.2)
- theforeman.foreman (still version 4.2.0)
- vultr.cloud (still version 1.13.0)
- vyos.vyos (still version 5.0.0)
- wti.remote (still version 1.0.10)

v11.4.0
=======

.. contents::
  :local:
  :depth: 2

Release Summary
---------------

Release Date: 2025-03-25

`Porting Guide <https://docs.ansible.com/ansible/devel/porting_guides.html>`_

Ansible-core
------------

Ansible 11.4.0 contains ansible-core version 2.18.4.
This is a newer version than version 2.18.3 contained in the previous Ansible release.

The changes are reported in the combined changelog below.

Changed Collections
-------------------

If not mentioned explicitly, the changes are reported in the combined changelog below.

+-----------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Collection            | Ansible 11.3.0 | Ansible 11.4.0 | Notes                                                                                                                                                                                                           |
+=======================+================+================+=================================================================================================================================================================================================================+
| amazon.aws            | 9.2.0          | 9.3.0          |                                                                                                                                                                                                                 |
+-----------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ansible.windows       | 2.7.0          | 2.8.0          |                                                                                                                                                                                                                 |
+-----------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| azure.azcollection    | 3.2.0          | 3.3.1          | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.                                                                                    |
+-----------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cisco.dnac            | 6.30.0         | 6.31.0         |                                                                                                                                                                                                                 |
+-----------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cisco.ios             | 9.1.1          | 9.1.2          |                                                                                                                                                                                                                 |
+-----------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.aws         | 9.0.0          | 9.1.0          |                                                                                                                                                                                                                 |
+-----------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.crypto      | 2.25.0         | 2.26.0         |                                                                                                                                                                                                                 |
+-----------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.dns         | 3.2.1          | 3.2.2          |                                                                                                                                                                                                                 |
+-----------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.docker      | 4.4.0          | 4.5.2          |                                                                                                                                                                                                                 |
+-----------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.general     | 10.4.0         | 10.5.0         |                                                                                                                                                                                                                 |
+-----------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.hrobot      | 2.1.0          | 2.2.0          |                                                                                                                                                                                                                 |
+-----------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.mysql       | 3.12.0         | 3.13.0         |                                                                                                                                                                                                                 |
+-----------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.postgresql  | 3.10.2         | 3.12.0         |                                                                                                                                                                                                                 |
+-----------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.routeros    | 3.4.0          | 3.5.0          |                                                                                                                                                                                                                 |
+-----------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.sops        | 2.0.2          | 2.0.3          |                                                                                                                                                                                                                 |
+-----------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.vmware      | 5.4.0          | 5.5.0          |                                                                                                                                                                                                                 |
+-----------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.windows     | 2.3.0          | 2.4.0          |                                                                                                                                                                                                                 |
+-----------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.zabbix      | 3.2.0          | 3.3.0          |                                                                                                                                                                                                                 |
+-----------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cyberark.conjur       | 1.3.2          | 1.3.3          | You can find the collection's changelog at `https://github.com/cyberark/ansible-conjur-collection/blob/master/CHANGELOG.md <https://github.com/cyberark/ansible-conjur-collection/blob/master/CHANGELOG.md>`__. |
+-----------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| fortinet.fortimanager | 2.9.0          | 2.9.1          |                                                                                                                                                                                                                 |
+-----------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| hetzner.hcloud        | 4.2.2          | 4.3.0          |                                                                                                                                                                                                                 |
+-----------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| netbox.netbox         | 3.20.0         | 3.21.0         |                                                                                                                                                                                                                 |
+-----------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Major Changes
-------------

community.zabbix
~~~~~~~~~~~~~~~~

- All Roles - Updated to support version 7.2

Minor Changes
-------------

amazon.aws
~~~~~~~~~~

- s3_object - support passing metadata in ``create`` mode (https://github.com/ansible-collections/amazon.aws/pull/2529).

ansible.windows
~~~~~~~~~~~~~~~

- setup - Remove dependency on shared function loaded by Ansible
- win_get_url - Added ``checksum`` and ``checksum_algorithm`` to verify the package before installation. Also returns ``checksum`` if ``checksum_algorithm`` is provided - https://github.com/ansible-collections/ansible.windows/issues/596

cisco.dnac
~~~~~~~~~~

- Adding Unit Test automation in github actions
- Changes in device_credential_workflow_manager module
- Changes in network_settings_workflow_manager module
- Changes in provision_workflow_manager module
- Changes in sda_fabric_site_zones_workflow_manager module
- Changes in sda_fabric_virtual_networks_workflow_manager module
- Changes in swim_workflow_manager module
- Changes in swim_workflow_manager module to support list of images
- Update Readme
- sda_fabric_site_zones_workflow_manager - attributes 'apply_pending_events',  'pre_auth_acl', was added

community.aws
~~~~~~~~~~~~~

- aws_ssm -  Refactor ``_init_clients`` Method for Improved Clarity and Efficiency (https://github.com/ansible-collections/community.aws/pull/2223).
- aws_ssm -  Refactor ``_prepare_terminal()`` Method for Improved Clarity and Efficiency (https://github.com/ansible-collections/community.aws/pull/).
- aws_ssm -  Refactor exec_command Method for Improved Clarity and Efficiency (https://github.com/ansible-collections/community.aws/pull/2224).
- aws_ssm - Add the possibility to define ``aws_ssm plugin`` variable via environment variable and by default use the version found on the $PATH rather than require that you provide an absolute path (https://github.com/ansible-collections/community.aws/issues/1990).
- aws_ssm - add function to generate random strings for SSM CLI delimitation (https://github.com/ansible-collections/community.aws/pull/2235).
- dms_endpoint - improve resilience of parameter comparison (https://github.com/ansible-collections/community.aws/pull/2221).
- s3_lifecycle - Support for min and max object size when applying the filter rules (https://github.com/ansible-collections/community.aws/pull/2205).
- various modules - linting fixups (https://github.com/ansible-collections/community.aws/pull/2221).
- waf_condition - adds missing options validation to filters (https://github.com/ansible-collections/community.aws/pull/2220).

community.crypto
~~~~~~~~~~~~~~~~

- openssl_pkcs12 - the module now supports ``certificate_content``/``other_certificates_content`` for cases where the data already exists in memory and not yet in a file (https://github.com/ansible-collections/community.crypto/issues/847, https://github.com/ansible-collections/community.crypto/pull/848).

community.docker
~~~~~~~~~~~~~~~~

- docker_compose_v2 - add ``assume_yes`` parameter for ``docker compose up`` (https://github.com/ansible-collections/community.docker/pull/1045).
- docker_network - add ``enable_ipv4`` option (https://github.com/ansible-collections/community.docker/issues/1047, https://github.com/ansible-collections/community.docker/pull/1049).

community.general
~~~~~~~~~~~~~~~~~

- CmdRunner module utils - the convenience method ``cmd_runner_fmt.as_fixed()`` now accepts multiple arguments as a list (https://github.com/ansible-collections/community.general/pull/9893).
- apache2_mod_proxy - code simplification, no change in functionality (https://github.com/ansible-collections/community.general/pull/9457).
- consul_token - fix idempotency when ``policies`` or ``roles`` are supplied by name (https://github.com/ansible-collections/community.general/issues/9841, https://github.com/ansible-collections/community.general/pull/9845).
- keycloak_realm - remove ID requirement when creating a realm to allow Keycloak generating its own realm ID (https://github.com/ansible-collections/community.general/pull/9768).
- nmap inventory plugin - adds ``dns_servers`` option for specifying DNS servers for name resolution. Accepts hostnames or IP addresses in the same format as the ``exclude`` option (https://github.com/ansible-collections/community.general/pull/9849).
- proxmox_kvm - add missing audio hardware device handling (https://github.com/ansible-collections/community.general/issues/5192, https://github.com/ansible-collections/community.general/pull/9847).
- redfish_config - add command ``SetPowerRestorePolicy`` to set the desired power state of the system when power is restored (https://github.com/ansible-collections/community.general/pull/9837).
- redfish_info - add command ``GetPowerRestorePolicy`` to get the desired power state of the system when power is restored (https://github.com/ansible-collections/community.general/pull/9824).
- rocketchat - option ``is_pre740`` has been added to control the format of the payload. For Rocket.Chat 7.4.0 or newer, it must be set to ``false`` (https://github.com/ansible-collections/community.general/pull/9882).
- slack callback plugin - add ``http_agent`` option to enable the user to set a custom user agent for slack callback plugin (https://github.com/ansible-collections/community.general/issues/9813, https://github.com/ansible-collections/community.general/pull/9836).
- systemd_info - add wildcard expression support in ``unitname`` option (https://github.com/ansible-collections/community.general/pull/9821).
- systemd_info - extend support to timer units (https://github.com/ansible-collections/community.general/pull/9891).
- vmadm - add new options ``flexible_disk_size`` and ``owner_uuid`` (https://github.com/ansible-collections/community.general/pull/9892).

community.mysql
~~~~~~~~~~~~~~~

- Integration tests for MariaDB 11.4 have replaced those for 10.5. The previous version is now 10.11.
- mysql_user - add ``locked`` option to lock/unlock users, this is mainly used to have users that will act as definers on stored procedures.

community.postgresql
~~~~~~~~~~~~~~~~~~~~

- postgresql_pg_hba - adds 'pg_hba_string' which contains the string that is written to the file to the output of the module (https://github.com/ansible-collections/community.postgresql/pull/778)
- postgresql_pg_hba - adds a parameter 'sort_rules' that allows the user to disable sorting in the module, the default is the previous behavior (https://github.com/ansible-collections/community.postgresql/pull/778)
- postgresql_pg_hba - regarding #795 will read all kinds of includes and add them to the end of the file in the same order as they were in the original file, does not allow to add includes (https://github.com/ansible-collections/community.postgresql/pull/778)
- postgresql_publication - added ``rowfilters`` parameter that adds support for row filtering on PG publications (https://github.com/ansible-collections/community.postgresql/pull/813)
- postgresql_user - now there is a ``quote_configuration_values`` parameter that allows to turn off quoting for values which when set to ``false`` allows to set ``search_path`` (https://github.com/ansible-collections/community.postgresql/pull/806)

community.routeros
~~~~~~~~~~~~~~~~~~

- api_info, api_modify - change default for ``/ip/cloud/ddns-enabled`` for RouterOS 7.17 and newer from ``yes`` to ``auto`` (https://github.com/ansible-collections/community.routeros/pull/350).

community.vmware
~~~~~~~~~~~~~~~~

- vcenter_standard_key_provider - Drop unused HAS_PYVMOMI (https://github.com/ansible-collections/community.vmware/pull/2327).
- vmware_category - Don't test for vSphere < 7 anymore (https://github.com/ansible-collections/community.vmware/pull/2326).
- vmware_guest - Drop unused HAS_PYVMOMI (https://github.com/ansible-collections/community.vmware/pull/2327).
- vmware_guest_storage_policy - Drop unnecessary HAS_PYVMOMI (https://github.com/ansible-collections/community.vmware/pull/2328).
- vmware_guest_tpm - Drop unused HAS_PYVMOMI (https://github.com/ansible-collections/community.vmware/pull/2327).
- vmware_host_graphics - Drop unnecessary HAS_PYVMOMI (https://github.com/ansible-collections/community.vmware/pull/2328).
- vmware_host_lockdown - Drop unnecessary HAS_PYVMOMI (https://github.com/ansible-collections/community.vmware/pull/2328).
- vmware_host_lockdown_exceptions - Drop unnecessary HAS_PYVMOMI (https://github.com/ansible-collections/community.vmware/pull/2328).
- vmware_host_snmp - Drop unnecessary HAS_PYVMOMI (https://github.com/ansible-collections/community.vmware/pull/2328).
- vmware_migrate_vmk - Drop unnecessary HAS_PYVMOMI (https://github.com/ansible-collections/community.vmware/pull/2328).
- vmware_migrate_vmk - Inherit from / sub-class PyVmomi (https://github.com/ansible-collections/community.vmware/pull/2324).
- vmware_resource_pool - Drop unnecessary HAS_PYVMOMI (https://github.com/ansible-collections/community.vmware/pull/2328).
- vmware_vc_infraprofile_info - Don't test for vSphere < 7 anymore (https://github.com/ansible-collections/community.vmware/pull/2326).
- vmware_vm_config_option - Drop unused HAS_PYVMOMI (https://github.com/ansible-collections/community.vmware/pull/2327).
- vmware_vm_vss_dvs_migrate - Inherit from / sub-class PyVmomi (https://github.com/ansible-collections/community.vmware/pull/2325).
- vmware_vsan_health_info - Drop unused HAS_PYVMOMI (https://github.com/ansible-collections/community.vmware/pull/2327).

community.windows
~~~~~~~~~~~~~~~~~

- Added support for Windows Server 2025
- This issue fixes installation of requirements as it requires a confirmation when installed as a depedency to PowershellGet. Installing it by itself prevents this confirmation dialog and allows required components to be installed (https://github.com/ansible-collections/community.windows/issues/147).
- win_file_version - Add file_version_raw result for cases where file_version might be empty or in not in the right format.
- win_iis_webapppool  - this pull request fixes the portion where building an app pool with the word "value" in it fails unexpectedly. https://github.com/ansible-collections/community.windows/issues/410.
- win_psrepository_copy - Add Force option that deletes repositories that are not present in the source

community.zabbix
~~~~~~~~~~~~~~~~

- added support for Zabbix 7.2 for all modules
- zabbix_action module - added Add host tags and Remove host tags operations
- zabbix_action module fixed SNMP discovery check condition in discovery rule.
- zabbix_agent role - accept several IPs in `zabbix_agent_listenip` variable.
- zabbix_connector module added
- zabbix_discoveryrule - add support for renaming discoveryrules
- zabbix_group_events_info - add tag support
- zabbix_item - add support for renaming items
- zabbix_itemprototype - add support for renaming itemprototypes
- zabbix_maintenance - Added ability to append host or host groups to existing maintenance.
- zabbix_mediatype module - fix failure that started to happen since Zabbix 7.0.9
- zabbix_proxy role - fix Zabbix proxy creation/update at Zabbix >= 7.0
- zabbix_proxy role - fix Zabbix proxy creation/update at Zabbix server when PSK used
- zabbix_regexp_info module added
- zabbix_settings - add support for additional timeout settings
- zabbix_settings - allow setting ``auditlog_mode`` on Zabbix 7.0 or higher. With this setting you can enable or disable audit logging of system actions.
- zabbix_trigger - add support for renaming triggers
- zabbix_triggerprototype - add support for renaming triggerprototypes

hetzner.hcloud
~~~~~~~~~~~~~~

- server - Add `created` state that creates a server but do not start it.

netbox.netbox
~~~~~~~~~~~~~

- Add `label`, `description` and `enabled` to `netbox_device_interface_template` (https://github.com/netbox-community/ansible_modules/issues/1333)
- Add example for using ansible variables in lookup
- Add name as option to netbox_fhrp_group
- Add support for custom headers
- netbox_cluster - Add options scope and scope_type for NetBox 4.2+
- netbox_device_interface - Add primary_mac_address option for NetBox 4.2+
- netbox_prefix - Add options scope and scope_type for NetBox 4.2+
- netbox_vm_interface - Add primary_mac_address option for NetBox 4.2+

Breaking Changes / Porting Guide
--------------------------------

community.postgresql
~~~~~~~~~~~~~~~~~~~~

- postgresql_info - the ``db`` alias is deprecated and will be removed in the next major release, use the ``login_db`` argument instead.
- postgresql_pg_hba - regarding #776 'keep_comments_at_rules' has been deprecated and won't do anything, the default is to keep the comments at the rules they are specified with. keep_comments_at_rules will be removed in 5.0.0 (https://github.com/ansible-collections/community.postgresql/pull/778)
- postgresql_user - the ``db`` alias is deprecated and will be removed in the next major release, use the ``login_db`` argument instead.

Deprecated Features
-------------------

community.vmware
~~~~~~~~~~~~~~~~

- vcenter_folder - the module has been deprecated and will be removed in community.vmware 7.0.0 (https://github.com/ansible-collections/community.vmware/pull/2340).
- vmware_cluster_ha - the module has been deprecated and will be removed in community.vmware 7.0.0 (https://github.com/ansible-collections/community.vmware/pull/2321).
- vmware_content_deploy_ovf_template - the module has been deprecated and will be removed in community.vmware 7.0.0 (https://github.com/ansible-collections/community.vmware/pull/2332).
- vmware_content_deploy_template - the module has been deprecated and will be removed in community.vmware 7.0.0 (https://github.com/ansible-collections/community.vmware/pull/2332).
- vmware_content_library_manager - the module has been deprecated and will be removed in community.vmware 7.0.0 (https://github.com/ansible-collections/community.vmware/pull/2345).
- vmware_host - the module has been deprecated and will be removed in community.vmware 7.0.0 (https://github.com/ansible-collections/community.vmware/pull/2337).

Bugfixes
--------

Ansible-core
~~~~~~~~~~~~

- Windows - add support for running on system where WDAC is in audit mode with ``Dynamic Code Security`` enabled.
- dnf5 - fix ``is_installed`` check for packages that are not installed but listed as provided by an installed package (https://github.com/ansible/ansible/issues/84578)
- dnf5 - libdnf5 - use ``conf.pkg_gpgcheck`` instead of deprecated ``conf.gpgcheck`` which is used only as a fallback
- facts - gather pagesize and calculate respective values depending upon architecture (https://github.com/ansible/ansible/issues/84773).
- module respawn - limit to supported Python versions

ansible.windows
~~~~~~~~~~~~~~~

- setup - Add better detection for VMWare base virtualization platforms - https://github.com/ansible-collections/ansible.windows/issues/753
- win_package - Support check mode with local file path sources

cisco.ios
~~~~~~~~~

- ios_acls - Fixed issue where cisco.ios.ios_acls module failed to process IPv6 ACL remarks, causing unsupported parameter errors.
- ios_route_maps - Fixes an issue where 'no description value' is an invalid command on the latest devices.

community.aws
~~~~~~~~~~~~~

- aws_ssm - use ``head_bucket`` to access bucket locations in foreign aws accounts (https://github.com/ansible-collections/community.aws/pull/1987).
- ssm - strip Powershell CLIXML from stdout (https://github.com/ansible-collections/community.aws/issues/1952).

community.dns
~~~~~~~~~~~~~

- Update Public Suffix List.

community.docker
~~~~~~~~~~~~~~~~

- docker_compose_v2 - fix version check for ``assume_yes`` (https://github.com/ansible-collections/community.docker/pull/1054).
- docker_compose_v2 - rename flag for ``assume_yes`` parameter for ``docker compose up`` to ``-y`` (https://github.com/ansible-collections/community.docker/pull/1054).
- docker_compose_v2 - use ``--yes`` instead of ``-y`` from Docker Compose 2.34.0 on (https://github.com/ansible-collections/community.docker/pull/1060).

community.general
~~~~~~~~~~~~~~~~~

- cloudlare_dns - handle exhausted response stream in case of HTTP errors to show nice error message to the user (https://github.com/ansible-collections/community.general/issues/9782, https://github.com/ansible-collections/community.general/pull/9818).
- dnf_versionlock - add support for dnf5 (https://github.com/ansible-collections/community.general/issues/9556).
- homebrew - fix crash when package names include tap (https://github.com/ansible-collections/community.general/issues/9777, https://github.com/ansible-collections/community.general/pull/9803).
- homebrew_cask - handle unusual brew version strings (https://github.com/ansible-collections/community.general/issues/8432, https://github.com/ansible-collections/community.general/pull/9881).
- nmcli - enable changing only the order of DNS servers or search suffixes (https://github.com/ansible-collections/community.general/issues/8724, https://github.com/ansible-collections/community.general/pull/9880).
- proxmox - add missing key selection of ``'status'`` key to ``get_lxc_status`` (https://github.com/ansible-collections/community.general/issues/9696, https://github.com/ansible-collections/community.general/pull/9809).
- proxmox_vm_info - the module no longer expects that the key ``template`` exists in a dictionary returned by Proxmox (https://github.com/ansible-collections/community.general/issues/9875, https://github.com/ansible-collections/community.general/pull/9910).
- sudoers - display stdout and stderr raised while failed validation (https://github.com/ansible-collections/community.general/issues/9674, https://github.com/ansible-collections/community.general/pull/9871).

community.mysql
~~~~~~~~~~~~~~~

- mysql_db - fix dump and import to find MariaDB binaries (mariadb and mariadb-dump) when MariaDB 11+ is used and symbolic links to MySQL binaries are absent.

community.postgresql
~~~~~~~~~~~~~~~~~~~~

- postgresql_pg_hba - fixes #776 the module won't be adding/moving comments repeatedly if 'keep_comments_at_rules' is 'false' (https://github.com/ansible-collections/community.postgresql/pull/778)

community.sops
~~~~~~~~~~~~~~

- install role - ``sops_install_on_localhost=false`` was not working properly if the role was running on more than one host due to a bug in ansible-core (https://github.com/ansible-collections/community.sops/issues/223, https://github.com/ansible-collections/community.sops/pull/224).

community.vmware
~~~~~~~~~~~~~~~~

- vmware_object_role_permission - The module ignores changing ``recursive`` (https://github.com/ansible-collections/community.vmware/pull/2350).

community.zabbix
~~~~~~~~~~~~~~~~

- Java Gateway Role - Temporary work around to solve failure on RHEL9.
- zabbix inventory plugin - do not require ``login_user`` and ``login_password`` to be present when ``auth_token`` is provided (https://github.com/ansible-collections/community.zabbix/pull/1439).

fortinet.fortimanager
~~~~~~~~~~~~~~~~~~~~~

- Changed the default playbook examples for each module to pass ansible-lint.
- Corrected mainkey of some modules.

netbox.netbox
~~~~~~~~~~~~~

- Fix missing netbox_config_template module in module_defaults
- Fixed an isssue with module_default parameter inheritance for modules netbox_config_template, netbox_custom_field_choice_set, netbox_permission, netbox_token, netbox_user, and netbox_user_group.
- fix call /api/status/ instead /api/status in nb_inventory plugin. (https://github.com/netbox-community/ansible_modules/issues/1335).
- netbox_ip_address - Fixed the problem preventing assignment of an IP address to a network interface

New Modules
-----------

amazon.aws
~~~~~~~~~~

- amazon.aws.ec2_dedicated_host - Create, update or delete (release) EC2 dedicated host
- amazon.aws.ec2_dedicated_host_info - Gather information about EC2 Dedicated Hosts in AWS

community.general
~~~~~~~~~~~~~~~~~

- community.general.pacemaker_resource - Manage pacemaker resources.

community.hrobot
~~~~~~~~~~~~~~~~

- community.hrobot.reset_info - Query information on the resetter of a dedicated server.

community.zabbix
~~~~~~~~~~~~~~~~

- community.zabbix.zabbix_connector - Create/Delete/Update Zabbix connectors
- community.zabbix.zabbix_regexp_info - Retrieve Zabbix regular expression

netbox.netbox
~~~~~~~~~~~~~

- netbox.netbox.netbox_mac_address - Create, update or delete MAC addresses within NetBox

Unchanged Collections
---------------------

- ansible.netcommon (still version 7.1.0)
- ansible.posix (still version 1.6.2)
- ansible.utils (still version 5.1.2)
- arista.eos (still version 10.1.1)
- awx.awx (still version 24.6.1)
- check_point.mgmt (still version 6.4.0)
- chocolatey.chocolatey (still version 1.5.3)
- cisco.aci (still version 2.10.1)
- cisco.asa (still version 6.1.0)
- cisco.intersight (still version 2.0.20)
- cisco.iosxr (still version 10.3.0)
- cisco.ise (still version 2.10.0)
- cisco.meraki (still version 2.20.8)
- cisco.mso (still version 2.9.0)
- cisco.nxos (still version 9.3.0)
- cisco.ucs (still version 1.15.0)
- cloud.common (still version 4.0.0)
- cloudscale_ch.cloud (still version 2.4.1)
- community.ciscosmb (still version 1.0.10)
- community.digitalocean (still version 1.27.0)
- community.grafana (still version 2.1.0)
- community.hashi_vault (still version 6.2.0)
- community.library_inventory_filtering_v1 (still version 1.0.2)
- community.libvirt (still version 1.3.1)
- community.mongodb (still version 1.7.9)
- community.network (still version 5.1.0)
- community.okd (still version 4.0.1)
- community.proxysql (still version 1.6.0)
- community.rabbitmq (still version 1.4.0)
- community.sap_libs (still version 1.4.2)
- containers.podman (still version 1.16.3)
- cyberark.pas (still version 1.0.30)
- dellemc.enterprise_sonic (still version 2.5.1)
- dellemc.openmanage (still version 9.10.0)
- dellemc.powerflex (still version 2.6.0)
- dellemc.unity (still version 2.0.0)
- f5networks.f5_modules (still version 1.34.1)
- fortinet.fortios (still version 2.3.9)
- google.cloud (still version 1.5.1)
- grafana.grafana (still version 5.7.0)
- ibm.qradar (still version 4.0.0)
- ibm.spectrum_virtualize (still version 2.0.0)
- ibm.storage_virtualize (still version 2.6.0)
- ieisystem.inmanage (still version 3.0.0)
- infinidat.infinibox (still version 1.4.5)
- infoblox.nios_modules (still version 1.8.0)
- inspur.ispim (still version 2.2.3)
- junipernetworks.junos (still version 9.1.0)
- kaytus.ksmanage (still version 2.0.0)
- kubernetes.core (still version 5.1.0)
- kubevirt.core (still version 2.1.0)
- lowlydba.sqlserver (still version 2.5.0)
- microsoft.ad (still version 1.8.0)
- netapp.cloudmanager (still version 21.24.0)
- netapp.ontap (still version 22.14.0)
- netapp.storagegrid (still version 21.14.0)
- netapp_eseries.santricity (still version 1.4.1)
- ngine_io.cloudstack (still version 2.5.0)
- openstack.cloud (still version 2.4.1)
- ovirt.ovirt (still version 3.2.0)
- purestorage.flasharray (still version 1.33.1)
- purestorage.flashblade (still version 1.19.2)
- sensu.sensu_go (still version 1.14.0)
- splunk.es (still version 4.0.0)
- telekom_mms.icinga_director (still version 2.2.2)
- theforeman.foreman (still version 4.2.0)
- vmware.vmware (still version 1.10.1)
- vmware.vmware_rest (still version 4.6.0)
- vultr.cloud (still version 1.13.0)
- vyos.vyos (still version 5.0.0)
- wti.remote (still version 1.0.10)

v11.3.0
=======

.. contents::
  :local:
  :depth: 2

Release Summary
---------------

Release Date: 2025-02-25

`Porting Guide <https://docs.ansible.com/ansible/devel/porting_guides.html>`_

Ansible-core
------------

Ansible 11.3.0 contains ansible-core version 2.18.3.
This is a newer version than version 2.18.2 contained in the previous Ansible release.

The changes are reported in the combined changelog below.

Changed Collections
-------------------

If not mentioned explicitly, the changes are reported in the combined changelog below.

+------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| Collection             | Ansible 11.2.0 | Ansible 11.3.0 | Notes                                                                                                                        |
+========================+================+================+==============================================================================================================================+
| amazon.aws             | 9.1.1          | 9.2.0          |                                                                                                                              |
+------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| arista.eos             | 10.0.1         | 10.1.1         |                                                                                                                              |
+------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| azure.azcollection     | 3.1.0          | 3.2.0          | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| check_point.mgmt       | 6.2.1          | 6.4.0          |                                                                                                                              |
+------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.dnac             | 6.28.0         | 6.30.0         |                                                                                                                              |
+------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.ios              | 9.1.0          | 9.1.1          |                                                                                                                              |
+------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.meraki           | 2.20.5         | 2.20.8         |                                                                                                                              |
+------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.crypto       | 2.24.0         | 2.25.0         |                                                                                                                              |
+------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.dns          | 3.1.2          | 3.2.1          |                                                                                                                              |
+------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.docker       | 4.3.1          | 4.4.0          |                                                                                                                              |
+------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.general      | 10.3.0         | 10.4.0         |                                                                                                                              |
+------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.routeros     | 3.3.0          | 3.4.0          |                                                                                                                              |
+------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.sops         | 2.0.1          | 2.0.2          |                                                                                                                              |
+------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.vmware       | 5.3.0          | 5.4.0          |                                                                                                                              |
+------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| containers.podman      | 1.16.2         | 1.16.3         |                                                                                                                              |
+------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| fortinet.fortimanager  | 2.8.2          | 2.9.0          |                                                                                                                              |
+------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| google.cloud           | 1.5.0          | 1.5.1          |                                                                                                                              |
+------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| infoblox.nios_modules  | 1.7.1          | 1.8.0          |                                                                                                                              |
+------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| netapp.ontap           | 22.13.0        | 22.14.0        |                                                                                                                              |
+------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| netapp.storagegrid     | 21.13.0        | 21.14.0        |                                                                                                                              |
+------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| purestorage.flasharray | 1.32.0         | 1.33.1         |                                                                                                                              |
+------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| vmware.vmware          | 1.9.0          | 1.10.1         |                                                                                                                              |
+------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| vmware.vmware_rest     | 4.5.0          | 4.6.0          | There are no changes recorded in the changelog.                                                                              |
+------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+

Minor Changes
-------------

Ansible-core
~~~~~~~~~~~~

- ansible-test - Automatically retry HTTP GET/PUT/DELETE requests on exceptions.
- ansible-test - Use Python's ``urllib`` instead of ``curl`` for HTTP requests.

amazon.aws
~~~~~~~~~~

- autoscaling_group - avoid assignment to unused variable in except block (https://github.com/ansible-collections/amazon.aws/pull/2464).
- ec2_ami - avoid redefining ``delete_snapshot`` inside ``DeregisterImage.do`` (https://github.com/ansible-collections/amazon.aws/pull/2444).
- ec2_transit_gateway - avoid assignment to unused ``retry_decorator`` variable (https://github.com/ansible-collections/amazon.aws/pull/2464).
- ec2_vpc_egress_igw - avoid assignment to unused ``vpc_id`` variable (https://github.com/ansible-collections/amazon.aws/pull/2464).
- ec2_vpc_nacl - avoid assignment to unused ``result`` variable (https://github.com/ansible-collections/amazon.aws/pull/2464).
- ec2_vpc_vpn - minor linting fixups (https://github.com/ansible-collections/amazon.aws/pull/2444).
- iam_password_policy - avoid assignment to unused variable in except block (https://github.com/ansible-collections/amazon.aws/pull/2464).
- iam_role - avoid assignment to unused variable in except block (https://github.com/ansible-collections/amazon.aws/pull/2464).
- inventory/aws_ec2 - Support jinja2 expression in ``hostnames`` variable(https://github.com/ansible-collections/amazon.aws/issues/2402).
- kms_key - avoid assignment to unused variable in except block (https://github.com/ansible-collections/amazon.aws/pull/2464).
- lambda - avoid assignment to unused ``architecture`` variable (https://github.com/ansible-collections/amazon.aws/pull/2464).
- lambda - avoid assignment to unused ``required_by`` variable (https://github.com/ansible-collections/amazon.aws/pull/2464).
- module_utils._s3 - explicitly cast super to the parent type (https://github.com/ansible-collections/amazon.aws/pull/2497).
- module_utils.botocore - avoid assigning unused parts of exc_info return (https://github.com/ansible-collections/amazon.aws/pull/2497).
- module_utils.exceptions - avoid assigning unused parts of exc_info return (https://github.com/ansible-collections/amazon.aws/pull/2497).
- module_utils.iam - avoid assignment to unused ``result`` variable (https://github.com/ansible-collections/amazon.aws/pull/2464).
- module_utils.s3 - avoid assignment to unused ``endpoint`` variable (https://github.com/ansible-collections/amazon.aws/pull/2464).
- plugin_utils/inventory - Add ``filters`` to list of templatable inventory options (https://github.com/ansible-collections/amazon.aws/pull/2379)
- route53 - Add support for type ``SSHFP`` records (https://github.com/ansible-collections/amazon.aws/pull/2430).
- route53_zone - Add support for enabling DNSSEC signing in a specific hosted zone (https://github.com/ansible-collections/amazon.aws/issues/1976).
- route53_zone - avoid assignmenta to unused ``current_vpc_ids`` and ``current_vpc_regions`` variables (https://github.com/ansible-collections/amazon.aws/pull/2464).
- s3_bucket - avoid assignment to unused variable in except block (https://github.com/ansible-collections/amazon.aws/pull/2464).
- s3_bucket - avoid redefining ``id`` inside ``handle_bucket_inventory`` and ``delete_bucket_inventory`` (https://github.com/ansible-collections/amazon.aws/pull/2444).
- s3_object - avoid redefining ``key_check`` inside ``_head_object`` (https://github.com/ansible-collections/amazon.aws/pull/2444).
- s3_object - simplify ``path_check`` logic (https://github.com/ansible-collections/amazon.aws/pull/2444).
- s3_object - use the ``copy`` rather than ``copy_object`` method when performing an S3 to S3 copy (https://github.com/ansible-collections/amazon.aws/issues/2117).
- s3_object_info - add support to list objects under a specific prefix (https://github.com/ansible-collections/amazon.aws/issues/2477).
- s3_object_info - avoid assignment to unused variable in except block (https://github.com/ansible-collections/amazon.aws/pull/2464).

arista.eos
~~~~~~~~~~

- Adds a new module `eos_vrf_global` in favor of `eos_vrf` legacy module to manage VRF global configurations on Arista EOS devices.

check_point.mgmt
~~~~~~~~~~~~~~~~

- added missing parameters such as 'filter', 'domains_to_process' and 'async_response' to the relevant resources modules.
- check_point.mgmt.cp_mgmt_lsm_cluster - support additional parameters (dynamic-objects, tags and topology)
- check_point.mgmt.cp_mgmt_lsm_gateway - support additional parameters (device_id, dynamic-objects, tags and topology)

cisco.dnac
~~~~~~~~~~

- Bug fixes in sda_fabric_devices_workflow_manager
- Bug fixes in sda_fabric_transits_workflow_manager
- Bug fixes in sda_fabric_transits_workflow_manager module
- Bug fixes in site_workflow_manager module
- Bug fixes in swim_workflow_manager module
- Bug fixes in template_workflow_manager module
- Bug fixes in user_role_workflow_manager module
- Changes in device_credential_workflow_manager module
- Changes in inventory_workflow_manager module
- Changes in ise_radius_integration_workflow_manager module
- Changes in network_settings_workflow_manager module
- Changes in pnp_workflow_manager module
- Changes in provision_workflow_manager module
- Changes in sda_fabric_virtual_networks_workflow_manager module
- Changes in sda_host_port_onboarding_workflow_manager module
- Changes in site_workflow_manager module
- Enhancements in provision_workflow_manager module
- Some parameters were modified in tag_member_v1_info
- playbooks were added
- sda_fabric_devices_workflow_manager - attribute 'route_distribution_protocol' was removed
- site_workflow_manager - attribute 'force_upload_floor_image' was added
- template_workflow_manager - attribute 'new_template_name' was added

community.crypto
~~~~~~~~~~~~~~~~

- luks_device - allow passphrases to contain newlines (https://github.com/ansible-collections/community.crypto/pull/844).

community.dns
~~~~~~~~~~~~~

- all filter, inventory, and lookup plugins, and plugin utils - add type hints to all Python 3 only code (https://github.com/ansible-collections/community.dns/pull/239).
- get_public_suffix, get_registrable_domain, remove_public_suffix, and remove_registrable_domain filter plugin - validate parameters, and correctly handle byte strings when passed for input (https://github.com/ansible-collections/community.dns/pull/239).

community.general
~~~~~~~~~~~~~~~~~

- bitwarden lookup plugin - add new option ``collection_name`` to filter results by collection name, and new option ``result_count`` to validate number of results (https://github.com/ansible-collections/community.general/pull/9728).
- incus connection plugin - adds ``remote_user`` and ``incus_become_method`` parameters for allowing a non-root user to connect to an Incus instance (https://github.com/ansible-collections/community.general/pull/9743).
- iocage inventory plugin - the new parameter ``hooks_results`` of the plugin is a list of files inside a jail that provide configuration parameters for the inventory. The inventory plugin reads the files from the jails and put the contents into the items of created variable ``iocage_hooks`` (https://github.com/ansible-collections/community.general/issues/9650, https://github.com/ansible-collections/community.general/pull/9651).
- jira - adds ``client_cert`` and ``client_key`` parameters for supporting client certificate authentification when connecting to Jira (https://github.com/ansible-collections/community.general/pull/9753).
- lldp - adds ``multivalues`` parameter to control behavior when lldpctl outputs an attribute multiple times (https://github.com/ansible-collections/community.general/pull/9657).
- lvg - add ``remove_extra_pvs`` parameter to control if ansible should remove physical volumes which are not in the ``pvs`` parameter (https://github.com/ansible-collections/community.general/pull/9698).
- lxd connection plugin - adds ``remote_user`` and ``lxd_become_method`` parameters for allowing a non-root user to connect to an LXD instance (https://github.com/ansible-collections/community.general/pull/9659).
- nmcli - adds VRF support with new ``type`` value ``vrf`` and new ``slave_type`` value ``vrf`` as well as new ``table`` parameter (https://github.com/ansible-collections/community.general/pull/9658, https://github.com/ansible-collections/community.general/issues/8014).
- onepassword_ssh_key - refactor to move code to lookup class (https://github.com/ansible-collections/community.general/pull/9633).
- proxmox_kvm - allow hibernation and suspending of VMs (https://github.com/ansible-collections/community.general/issues/9620, https://github.com/ansible-collections/community.general/pull/9653).
- redfish_command - add ``PowerFullPowerCycle`` to power command options (https://github.com/ansible-collections/community.general/pull/9729).
- ssh_config - add ``other_options`` option (https://github.com/ansible-collections/community.general/issues/8053, https://github.com/ansible-collections/community.general/pull/9684).
- xen_orchestra inventory plugin - add ``use_vm_uuid`` and ``use_host_uuid`` boolean options to allow switching over to using VM/Xen name labels instead of UUIDs as item names (https://github.com/ansible-collections/community.general/pull/9787).

community.routeros
~~~~~~~~~~~~~~~~~~

- api_info, api_modify - add support for the ``ip dns forwarders`` path implemented by RouterOS 7.17 and newer (https://github.com/ansible-collections/community.routeros/pull/343).

community.vmware
~~~~~~~~~~~~~~~~

- vmware_guest - Print details about the error message when the returned task result contains (https://github.com/ansible-collections/community.vmware/pull/2301).

fortinet.fortimanager
~~~~~~~~~~~~~~~~~~~~~

- Supported FortiManager 7.2.9, 7.4.6, 7.6.2. Added 3 new modules.

netapp.ontap
~~~~~~~~~~~~

- Multiple modules - Standardize hostname, username, and password parameters to use netapp_hostname, netapp_username, and netapp_password as values.
- Multiple modules - Update examples to use Fully Qualified Collection Name.
- Update dead link in doc_fragments.
- na_ontap_dns - updated documentation for `vserver`.
- na_ontap_flexcache - new options `relative_size`, `override_encryption`, `atime_scrub`, `cifs_change_notify_enabled`, `global_file_locking_enabled`, `guarantee_type`, `dr_cache` added in REST.
- na_ontap_rest_cli - Add POST and DELETE examples.
- na_ontap_snapmirror - new option `quiesced_time_out` added to wait for quiesce job to complete.
- na_ontap_svm - updated documentation for `allowed_protocols` & `services`.
- na_ontap_volume - new option `large_size_enabled` added in REST, requires ONTAP 9.12 or later.

netapp.storagegrid
~~~~~~~~~~~~~~~~~~

- na_sg_grid_account - new option `allow_compliance_mode` and `max_retention_days` added for tenant account, requires storageGRID 11.9 or later.
- na_sg_grid_gateway - new option `enable_tenant_manager`, `enable_grid_manager` and `node_type` added to support management interfaces.
- na_sg_grid_group - new option `read_only` added for grid groups.
- na_sg_grid_info - LB endpoints and HA group in info module.
- na_sg_org_group - new option `read_only` added for tenant groups.

purestorage.flasharray
~~~~~~~~~~~~~~~~~~~~~~

- all - Minimum ``py-pure-client`` version increased to 1.57.0 due to release of Realms feature
- purefa_hg - Added support for Fusion
- purefa_host - Added Fusion support
- purefa_info - Add performance data for network interfaces
- purefa_info - Added new section ``realms``.
- purefa_info - Added new subset ``fleet``
- purefa_info - Deprecate ``network.<interface>.hwaddr`` - replaced by ``network.<interface>.mac_address``
- purefa_info - Deprecate ``network.<interface>.slaves`` - replaced by ``network.<interface>.subinterfaces``
- purefa_info - VNC feature deprecated from Purity//FA 6.8.0.
- purefa_pg - Added Fusion support.
- purefa_pgsched - Added support for Fusion.
- purefa_pgsnap - Added support for Fusion.
- purefa_pod_replica - Added Fusion support.
- purefa_pods - Added support for Fusion with ``context`` parameter.
- purefa_smtp - Added support for additional parameters, including encryption mode and email prefixs and email sender name.
- purefa_snap - Added Fusion support.
- purefa_vg - Added support for Fusion
- purefa_vlan - Convert to REST v2
- purefa_vnc - VNC feature deprecated from Purity//FA 6.8.0.
- purefa_volume - Added ``context`` parameter to support fleet operations

vmware.vmware
~~~~~~~~~~~~~

- cluster_ha - migrate the vmware_cluster_ha module from community to here
- deploy_content_library_ovf - migrate the vmware_content_deploy_ovf_template module from community to here
- deploy_content_library_ovf - update parameters to be consistent with other deploy modules
- deploy_content_library_template - migrate the vmware_content_deploy_template module from community to here
- deploy_content_library_template - update parameters to be consistent with other deploy modules
- deploy_folder_template - add module to deploy a vm from a template in a vsphere folder
- esxi_connection - migrate the vmware_host module from community to here
- esxi_host - migrate the vmware_host module from community to here
- folder - migrate vmware_folder module from community to here
- local_content_library - migrate the vmware_content_library_manager module from community to here
- subscribed_content_library - migrate the vmware_content_library_manager module from community to here

Deprecated Features
-------------------

community.general
~~~~~~~~~~~~~~~~~

- profitbricks - module is deprecated and will be removed in community.general 11.0.0 (https://github.com/ansible-collections/community.general/pull/9733).
- profitbricks_datacenter - module is deprecated and will be removed in community.general 11.0.0 (https://github.com/ansible-collections/community.general/pull/9733).
- profitbricks_nic - module is deprecated and will be removed in community.general 11.0.0 (https://github.com/ansible-collections/community.general/pull/9733).
- profitbricks_volume - module is deprecated and will be removed in community.general 11.0.0 (https://github.com/ansible-collections/community.general/pull/9733).
- profitbricks_volume_attachments - module is deprecated and will be removed in community.general 11.0.0 (https://github.com/ansible-collections/community.general/pull/9733).

community.vmware
~~~~~~~~~~~~~~~~

- module_utils.vmware - host_version_at_least is deprecated and will be removed in community.vmware 7.0.0 (https://github.com/ansible-collections/community.vmware/pull/2303).
- plugin_utils.inventory - this plugin util is deprecated and will be removed in community.vmware 7.0.0 (https://github.com/ansible-collections/community.vmware/pull/2304).
- plugins.httpapi - this is deprecated and will be removed in community.vmware 7.0.0 (https://github.com/ansible-collections/community.vmware/pull/2306).
- vm_device_helper.py - is_nvdimm_controller is deprecated and will be removed in community.vmware 7.0.0 (https://github.com/ansible-collections/community.vmware/pull/2311).
- vm_device_helper.py - is_nvdimm_device is deprecated and will be removed in community.vmware 7.0.0 (https://github.com/ansible-collections/community.vmware/pull/2311).
- vmware - find_host_portgroup_by_name is deprecated and will be removed in community.vmware 7.0.0 (https://github.com/ansible-collections/community.vmware/pull/2311).
- vmware - find_vmdk_file is deprecated and will be removed in community.vmware 7.0.0 (https://github.com/ansible-collections/community.vmware/pull/2311).
- vmware - network_exists_by_name is deprecated and will be removed in community.vmware 7.0.0 (https://github.com/ansible-collections/community.vmware/pull/2311).
- vmware - vmdk_disk_path_split is deprecated and will be removed in community.vmware 7.0.0 (https://github.com/ansible-collections/community.vmware/pull/2311).
- vmware_host_inventory - the inventory plugin is deprecated and will be removed in community.vmware 7.0.0 (https://github.com/ansible-collections/community.vmware/pull/2283).
- vmware_maintenancemode - the module has been deprecated and will be removed in community.vmware 7.0.0 (https://github.com/ansible-collections/community.vmware/pull/2293).
- vmware_rest_client - get_folder_by_name is deprecated and will be removed in community.vmware 7.0.0 (https://github.com/ansible-collections/community.vmware/pull/2311).
- vmware_vm_inventory - the inventory plugin is deprecated and will be removed in community.vmware 7.0.0 (https://github.com/ansible-collections/community.vmware/pull/2283).

Bugfixes
--------

Ansible-core
~~~~~~~~~~~~

- include_vars - fixed erroneous warning if an unreserved variable name contains a single character that matches a reserved variable. (https://github.com/ansible/ansible/issues/84623)
- linear strategy - fix executing ``end_role`` meta tasks for each host, instead of handling these as implicit run_once tasks (https://github.com/ansible/ansible/issues/84660).

amazon.aws
~~~~~~~~~~

- ec2_instance - Fix issue where EC2 instance module failed to apply security groups when both ``network`` and ``vpc_subnet_id`` were specified, caused by passing ``None`` to discover_security_groups() (https://github.com/ansible-collections/amazon.aws/pull/2488).
- ec2_vpc_nacl_info - Fix failure when listing NetworkACLs and no ACLs are found (https://github.com/ansible-collections/amazon.aws/issues/2425).
- iam_access_key - add missing requirements checks (https://github.com/ansible-collections/amazon.aws/pull/2465).
- module_utils.botocore - fixed type aliasing (https://github.com/ansible-collections/amazon.aws/pull/2497).
- plugin_utils.botocore - fixed type aliasing (https://github.com/ansible-collections/amazon.aws/pull/2497).
- s3_bucket - Do not use default region as location constraint when creating bucket on ceph cluster (https://github.com/ansible-collections/amazon.aws/issues/2420).

arista.eos
~~~~~~~~~~

- Fixed an issue in the `compare_configs` method where unnecessary negate commands were generated for ACL entries already present in both `have` and `want` configurations.
- Improved validation logic for ACL sequence numbers and content matching to ensure idempotency.
- Prevented redundant configuration updates for Access Control Lists.
- fix facts gathering for ebgp-multihop attribute.

cisco.ios
~~~~~~~~~

- Added support for FourHundredGigE, FiftyGigE and FourHundredGigabitEthernet.

cisco.meraki
~~~~~~~~~~~~

- Changes at compare equality function.
- Unable to create Syslog Server Object. Action module manually fixing.
- cisco.meraki.devices_switch_ports idempotency error fixed.
- cisco.meraki.networks_appliance_traffic_shaping_rules Always Pushes Configuration Even When Unchanged.
- cisco.meraki.organizations_login_security module update organization security settings.

community.dns
~~~~~~~~~~~~~

- Fix various issues and potential bugs pointed out by linters (https://github.com/ansible-collections/community.dns/pull/242, https://github.com/ansible-collections/community.dns/pull/243).
- Update Public Suffix List.

community.docker
~~~~~~~~~~~~~~~~

- docker_compose_v2_run - the module has a conflict between the type of parameter it expects and the one it tries to sanitize. Fix removes the label sanitization step because they are already validated by the parameter definition (https://github.com/ansible-collections/community.docker/pull/1034).
- vendored Docker SDK for Python - do not assume that ``KeyError`` is always for ``ApiVersion`` when querying version fails (https://github.com/ansible-collections/community.docker/issues/1033, https://github.com/ansible-collections/community.docker/pull/1034).

community.general
~~~~~~~~~~~~~~~~~

- apache2_mod_proxy - make compatible with Python 3 (https://github.com/ansible-collections/community.general/pull/9762).
- apache2_mod_proxy - passing the cluster's page as referer for the member's pages. This makes the module actually work again for halfway modern Apache versions. According to some comments founds on the net the referer was required since at least 2019 for some versions of Apache 2 (https://github.com/ansible-collections/community.general/pull/9762).
- cloudflare_dns - fix crash when deleting a DNS record or when updating a record with ``solo=true`` (https://github.com/ansible-collections/community.general/issues/9652, https://github.com/ansible-collections/community.general/pull/9649).
- elasticsearch_plugin - fix ``ERROR: D is not a recognized option`` issue when configuring proxy settings (https://github.com/ansible-collections/community.general/pull/9774, https://github.com/ansible-collections/community.general/issues/9773).
- homebrew - make package name parsing more resilient (https://github.com/ansible-collections/community.general/pull/9665, https://github.com/ansible-collections/community.general/issues/9641).
- ipa_host - module revoked existing host certificates even if ``user_certificate`` was not given (https://github.com/ansible-collections/community.general/pull/9694).
- keycloak module utils - replaces missing return in get_role_composites method which caused it to return None instead of composite roles (https://github.com/ansible-collections/community.general/issues/9678, https://github.com/ansible-collections/community.general/pull/9691).
- keycloak_client - fix and improve existing tests. The module showed a diff without actual changes, solved by improving the ``normalise_cr()`` function (https://github.com/ansible-collections/community.general/pull/9644).
- keycloak_client - in check mode, detect whether the lists in before client (for example redirect URI list) contain items that the lists in the desired client do not contain (https://github.com/ansible-collections/community.general/pull/9739).
- lldp - fix crash caused by certain lldpctl output where an attribute is defined as branch and leaf (https://github.com/ansible-collections/community.general/pull/9657).
- onepassword_doc lookup plugin - ensure that 1Password Connect support also works for this plugin (https://github.com/ansible-collections/community.general/pull/9625).
- passwordstore lookup plugin - fix subkey creation even when ``create=false`` (https://github.com/ansible-collections/community.general/issues/9105, https://github.com/ansible-collections/community.general/pull/9106).
- proxmox - adds the ``pubkey`` parameter (back to) the ``update`` state (https://github.com/ansible-collections/community.general/issues/9642, https://github.com/ansible-collections/community.general/pull/9645).
- proxmox - fixes a typo in the translation of the ``pubkey`` parameter to proxmox' ``ssh-public-keys`` (https://github.com/ansible-collections/community.general/issues/9642, https://github.com/ansible-collections/community.general/pull/9645).
- proxmox inventory plugin - plugin did not update cache correctly after ``meta: refresh_inventory`` (https://github.com/ansible-collections/community.general/issues/9710, https://github.com/ansible-collections/community.general/pull/9760).
- redhat_subscription - use the "enable_content" option (when available) when
  registering using D-Bus, to ensure that subscription-manager enables the
  content on registration; this is particular important on EL 10+ and Fedora
  41+
  (https://github.com/ansible-collections/community.general/pull/9778).
- xml - ensure file descriptor is closed (https://github.com/ansible-collections/community.general/pull/9695).
- zfs - fix handling of multi-line values of user-defined ZFS properties (https://github.com/ansible-collections/community.general/pull/6264).
- zfs_facts - parameter ``type`` now accepts multple values as documented (https://github.com/ansible-collections/community.general/issues/5909, https://github.com/ansible-collections/community.general/pull/9697).

community.routeros
~~~~~~~~~~~~~~~~~~

- api_info, api_modify - remove the primary key ``action`` from the ``interface wifi provisioning`` path, since RouterOS also allows to create completely duplicate entries (https://github.com/ansible-collections/community.routeros/issues/344, https://github.com/ansible-collections/community.routeros/pull/345).

community.sops
~~~~~~~~~~~~~~

- install role - when used with Debian on ARM architecture, the architecture name is now correctly translated from ``aarch64`` to ``arm64`` (https://github.com/ansible-collections/community.sops/issues/220, https://github.com/ansible-collections/community.sops/pull/221).

containers.podman
~~~~~~~~~~~~~~~~~

- Don't pull image when state is absent or pull=never (#889)
- Fix idempotency for containers with env vars containing MAX_SIZE (#893)
- Fix list tags failure in podman_search (#875)
- Fix podman_container_copy examples (#882)
- docs(podman_container) - improve comments on network property (#878)

fortinet.fortimanager
~~~~~~~~~~~~~~~~~~~~~

- Changed parameter type of some parameters.

google.cloud
~~~~~~~~~~~~

- run integration test with Ansible 2.16 to match `requires_ansible` version

netapp.ontap
~~~~~~~~~~~~

- Resolved Ansible lint issues.
- na_ontap_aggregate - fix issue with 'raid_type' change in REST.
- na_ontap_kerberos_interface - updated example in module documentation.
- na_ontap_qtree - fix timeout issue with qtree delete in REST.

purestorage.flasharray
~~~~~~~~~~~~~~~~~~~~~~

- purefa_ds - Fixed issue with trying to create a pre-existing system-defined role
- purefa_hg - Fixed issue when ``check_mode = true`` not reporting correct status when adding new hosts to hostgroup.
- purefa_host - Fix issue with no VLAN provided when Purity//FA is a recent version.
- purefa_host - Fix issue with setting preferred_arrays for a host.
- purefa_pod - Errored out when setting failover preference for pod
- purefa_ra - Fixed duration check logic
- purefa_volume - Fixes issue of moving protected volume into volume group

vmware.vmware
~~~~~~~~~~~~~

- folder - replaced non-existent 'storage' type with 'datastore' type
- module_deploy_vm_base - fix attribute error when deploying to a resource pool

Known Issues
------------

purestorage.flasharray
~~~~~~~~~~~~~~~~~~~~~~

- All Fusion fleet members will be assumed to be at the same Purity//FA version level as the array connected to by Ansible.
- FlashArray//CBS is not currently supported as a member of a Fusion fleet

New Plugins
-----------

Lookup
~~~~~~

- infoblox.nios_modules.nios_next_vlan_id - Return the next available VLAN ID

New Modules
-----------

amazon.aws
~~~~~~~~~~

- amazon.aws.route53_key_signing_key - Manages a key-signing key (KSK)

check_point.mgmt
~~~~~~~~~~~~~~~~

- check_point.mgmt.cp_mgmt_user - Manages user objects on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_user_facts - Get user objects facts on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_user_template - Manages user-template objects on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_user_template_facts - Get user-template objects facts on Checkpoint over Web Services API

community.docker
~~~~~~~~~~~~~~~~

- community.docker.docker_context_info - Retrieve information on Docker contexts for the current user.

community.general
~~~~~~~~~~~~~~~~~

- community.general.systemd_info - Gather C(systemd) unit info.

fortinet.fortimanager
~~~~~~~~~~~~~~~~~~~~~

- fortinet.fortimanager.fmgr_gtp_ieallowlist - IE allow list.
- fortinet.fortimanager.fmgr_gtp_ieallowlist_entries - Entries of allow list for unknown or out-of-state IEs.
- fortinet.fortimanager.fmgr_ums_setting - Ums setting

infoblox.nios_modules
~~~~~~~~~~~~~~~~~~~~~

- infoblox.nios_modules.nios_adminuser - Configure Infoblox NIOS Admin Users
- infoblox.nios_modules.nios_vlan - Configure Infoblox NIOS VLANs

netapp.storagegrid
~~~~~~~~~~~~~~~~~~

- netapp.storagegrid.na_sg_grid_ec_profile - Manage EC profiles on StorageGRID.
- netapp.storagegrid.na_sg_grid_ilm_policy - Manage ILM policies on StorageGRID.
- netapp.storagegrid.na_sg_grid_ilm_policy_tag - Manage ILM policy tags on StorageGRID.
- netapp.storagegrid.na_sg_grid_ilm_pool - Manage ILM pools on StorageGRID.
- netapp.storagegrid.na_sg_grid_ilm_rule - Manage ILM rules on StorageGRID.

purestorage.flasharray
~~~~~~~~~~~~~~~~~~~~~~

- purestorage.flasharray.purefa_fleet - Manage Fusion Fleet
- purestorage.flasharray.purefa_realm - Manage realms on Pure Storage FlashArrays

Unchanged Collections
---------------------

- ansible.netcommon (still version 7.1.0)
- ansible.posix (still version 1.6.2)
- ansible.utils (still version 5.1.2)
- ansible.windows (still version 2.7.0)
- awx.awx (still version 24.6.1)
- chocolatey.chocolatey (still version 1.5.3)
- cisco.aci (still version 2.10.1)
- cisco.asa (still version 6.1.0)
- cisco.intersight (still version 2.0.20)
- cisco.iosxr (still version 10.3.0)
- cisco.ise (still version 2.10.0)
- cisco.mso (still version 2.9.0)
- cisco.nxos (still version 9.3.0)
- cisco.ucs (still version 1.15.0)
- cloud.common (still version 4.0.0)
- cloudscale_ch.cloud (still version 2.4.1)
- community.aws (still version 9.0.0)
- community.ciscosmb (still version 1.0.10)
- community.digitalocean (still version 1.27.0)
- community.grafana (still version 2.1.0)
- community.hashi_vault (still version 6.2.0)
- community.hrobot (still version 2.1.0)
- community.library_inventory_filtering_v1 (still version 1.0.2)
- community.libvirt (still version 1.3.1)
- community.mongodb (still version 1.7.9)
- community.mysql (still version 3.12.0)
- community.network (still version 5.1.0)
- community.okd (still version 4.0.1)
- community.postgresql (still version 3.10.2)
- community.proxysql (still version 1.6.0)
- community.rabbitmq (still version 1.4.0)
- community.sap_libs (still version 1.4.2)
- community.windows (still version 2.3.0)
- community.zabbix (still version 3.2.0)
- cyberark.conjur (still version 1.3.2)
- cyberark.pas (still version 1.0.30)
- dellemc.enterprise_sonic (still version 2.5.1)
- dellemc.openmanage (still version 9.10.0)
- dellemc.powerflex (still version 2.6.0)
- dellemc.unity (still version 2.0.0)
- f5networks.f5_modules (still version 1.34.1)
- fortinet.fortios (still version 2.3.9)
- grafana.grafana (still version 5.7.0)
- hetzner.hcloud (still version 4.2.2)
- ibm.qradar (still version 4.0.0)
- ibm.spectrum_virtualize (still version 2.0.0)
- ibm.storage_virtualize (still version 2.6.0)
- ieisystem.inmanage (still version 3.0.0)
- infinidat.infinibox (still version 1.4.5)
- inspur.ispim (still version 2.2.3)
- junipernetworks.junos (still version 9.1.0)
- kaytus.ksmanage (still version 2.0.0)
- kubernetes.core (still version 5.1.0)
- kubevirt.core (still version 2.1.0)
- lowlydba.sqlserver (still version 2.5.0)
- microsoft.ad (still version 1.8.0)
- netapp.cloudmanager (still version 21.24.0)
- netapp_eseries.santricity (still version 1.4.1)
- netbox.netbox (still version 3.20.0)
- ngine_io.cloudstack (still version 2.5.0)
- openstack.cloud (still version 2.4.1)
- ovirt.ovirt (still version 3.2.0)
- purestorage.flashblade (still version 1.19.2)
- sensu.sensu_go (still version 1.14.0)
- splunk.es (still version 4.0.0)
- telekom_mms.icinga_director (still version 2.2.2)
- theforeman.foreman (still version 4.2.0)
- vultr.cloud (still version 1.13.0)
- vyos.vyos (still version 5.0.0)
- wti.remote (still version 1.0.10)

v11.2.0
=======

.. contents::
  :local:
  :depth: 2

Release Summary
---------------

Release Date: 2025-01-28

`Porting Guide <https://docs.ansible.com/ansible/devel/porting_guides.html>`_

Ansible-core
------------

Ansible 11.2.0 contains ansible-core version 2.18.2.
This is a newer version than version 2.18.1 contained in the previous Ansible release.

The changes are reported in the combined changelog below.

Changed Collections
-------------------

If not mentioned explicitly, the changes are reported in the combined changelog below.

+-----------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Collection                  | Ansible 11.1.0 | Ansible 11.2.0 | Notes                                                                                                                                                                                                           |
+=============================+================+================+=================================================================================================================================================================================================================+
| amazon.aws                  | 9.0.0          | 9.1.1          |                                                                                                                                                                                                                 |
+-----------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ansible.windows             | 2.5.0          | 2.7.0          |                                                                                                                                                                                                                 |
+-----------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cisco.asa                   | 6.0.0          | 6.1.0          |                                                                                                                                                                                                                 |
+-----------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cisco.dnac                  | 6.25.0         | 6.28.0         |                                                                                                                                                                                                                 |
+-----------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cisco.ios                   | 9.0.3          | 9.1.0          |                                                                                                                                                                                                                 |
+-----------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cisco.iosxr                 | 10.2.2         | 10.3.0         |                                                                                                                                                                                                                 |
+-----------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cisco.ise                   | 2.9.6          | 2.10.0         |                                                                                                                                                                                                                 |
+-----------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cisco.meraki                | 2.18.3         | 2.20.5         |                                                                                                                                                                                                                 |
+-----------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cisco.nxos                  | 9.2.1          | 9.3.0          |                                                                                                                                                                                                                 |
+-----------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cisco.ucs                   | 1.14.0         | 1.15.0         | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.                                                                                    |
+-----------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cloudscale_ch.cloud         | 2.4.0          | 2.4.1          |                                                                                                                                                                                                                 |
+-----------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.ciscosmb          | 1.0.9          | 1.0.10         |                                                                                                                                                                                                                 |
+-----------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.crypto            | 2.22.3         | 2.24.0         |                                                                                                                                                                                                                 |
+-----------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.dns               | 3.1.0          | 3.1.2          |                                                                                                                                                                                                                 |
+-----------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.docker            | 4.1.0          | 4.3.1          |                                                                                                                                                                                                                 |
+-----------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.general           | 10.1.0         | 10.3.0         |                                                                                                                                                                                                                 |
+-----------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.hrobot            | 2.0.2          | 2.1.0          |                                                                                                                                                                                                                 |
+-----------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.libvirt           | 1.3.0          | 1.3.1          |                                                                                                                                                                                                                 |
+-----------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.mongodb           | 1.7.8          | 1.7.9          | There are no changes recorded in the changelog.                                                                                                                                                                 |
+-----------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.mysql             | 3.11.0         | 3.12.0         |                                                                                                                                                                                                                 |
+-----------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.okd               | 4.0.0          | 4.0.1          |                                                                                                                                                                                                                 |
+-----------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.postgresql        | 3.9.0          | 3.10.2         |                                                                                                                                                                                                                 |
+-----------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.rabbitmq          | 1.3.0          | 1.4.0          |                                                                                                                                                                                                                 |
+-----------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.routeros          | 3.1.0          | 3.3.0          |                                                                                                                                                                                                                 |
+-----------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.sops              | 2.0.0          | 2.0.1          |                                                                                                                                                                                                                 |
+-----------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.vmware            | 5.2.0          | 5.3.0          |                                                                                                                                                                                                                 |
+-----------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cyberark.conjur             | 1.3.1          | 1.3.2          | You can find the collection's changelog at `https://github.com/cyberark/ansible-conjur-collection/blob/master/CHANGELOG.md <https://github.com/cyberark/ansible-conjur-collection/blob/master/CHANGELOG.md>`__. |
+-----------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| dellemc.openmanage          | 9.9.0          | 9.10.0         |                                                                                                                                                                                                                 |
+-----------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| dellemc.powerflex           | 2.5.0          | 2.6.0          |                                                                                                                                                                                                                 |
+-----------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| f5networks.f5_modules       | 1.32.1         | 1.34.1         |                                                                                                                                                                                                                 |
+-----------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| fortinet.fortios            | 2.3.8          | 2.3.9          |                                                                                                                                                                                                                 |
+-----------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| google.cloud                | 1.4.1          | 1.5.0          |                                                                                                                                                                                                                 |
+-----------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| grafana.grafana             | 5.6.0          | 5.7.0          |                                                                                                                                                                                                                 |
+-----------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ibm.storage_virtualize      | 2.5.0          | 2.6.0          |                                                                                                                                                                                                                 |
+-----------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| kubernetes.core             | 5.0.0          | 5.1.0          |                                                                                                                                                                                                                 |
+-----------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| lowlydba.sqlserver          | 2.3.4          | 2.5.0          |                                                                                                                                                                                                                 |
+-----------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| microsoft.ad                | 1.7.1          | 1.8.0          |                                                                                                                                                                                                                 |
+-----------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| openstack.cloud             | 2.3.0          | 2.4.1          | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.                                                                                    |
+-----------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| purestorage.flashblade      | 1.19.1         | 1.19.2         |                                                                                                                                                                                                                 |
+-----------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| telekom_mms.icinga_director | 2.2.1          | 2.2.2          |                                                                                                                                                                                                                 |
+-----------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| vmware.vmware               | 1.7.1          | 1.9.0          |                                                                                                                                                                                                                 |
+-----------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| vmware.vmware_rest          | 4.3.0          | 4.5.0          |                                                                                                                                                                                                                 |
+-----------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Major Changes
-------------

community.vmware
~~~~~~~~~~~~~~~~

- vmware_dvswitch_pvlans - The VLAN ID type has been updated to be handled as an integer (https://github.com/ansible-collections/community.vmware/pull/2267).

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- omevv_firmware - This module allows to update firmware of the single host and single cluster.

fortinet.fortios
~~~~~~~~~~~~~~~~

- Support check_mode on all the configuration modules.

google.cloud
~~~~~~~~~~~~

- google_cloud_ops_agents - role submodule removed because it prevents the collection from passing sanity and lint tests

grafana.grafana
~~~~~~~~~~~~~~~

- Ability to set custom directory path for *.alloy config files by @voidquark in https://github.com/grafana/grafana-ansible-collection/pull/294
- Fix 'dict object' has no attribute 'path' when running with --check by @JMLX42 in https://github.com/grafana/grafana-ansible-collection/pull/283
- Update grafana template by @santilococo in https://github.com/grafana/grafana-ansible-collection/pull/300
- add loki bloom support by @voidquark in https://github.com/grafana/grafana-ansible-collection/pull/298
- grafana.ini yaml syntax by @intermittentnrg in https://github.com/grafana/grafana-ansible-collection/pull/232

Minor Changes
-------------

amazon.aws
~~~~~~~~~~

- autoscaling_group - adds ``group_name`` as an alias for the ``name`` parameter (https://github.com/ansible-collections/amazon.aws/pull/2396).
- autoscaling_group_info - adds ``group_name`` as an alias for the ``name`` parameter (https://github.com/ansible-collections/amazon.aws/pull/2396).
- autoscaling_instance_refresh - adds ``group_name`` as an alias for the ``name`` parameter (https://github.com/ansible-collections/amazon.aws/pull/2396).
- autoscaling_instance_refresh_info - adds ``group_name`` as an alias for the ``name`` parameter (https://github.com/ansible-collections/amazon.aws/pull/2396).
- ec2_instance - Fix the issue when trying to run instances using launch template in an AWS environment where no default subnet is defined(https://github.com/ansible-collections/amazon.aws/issues/2321).
- ec2_metadata_facts - add ``ansible_ec2_instance_tags`` to return values (https://github.com/ansible-collections/amazon.aws/pull/2398).
- ec2_transit_gateway - handle empty description while deleting transit gateway (https://github.com/ansible-collections/community.aws/pull/2086).

ansible.windows
~~~~~~~~~~~~~~~

- Added support for Windows Server 2025
- setup - Added ``ansible_os_install_date`` as the OS installation date in the ISO 8601 format ``yyyy-MM-ddTHH:mm:ssZ``. This date is represented in the UTC timezone - https://github.com/ansible-collections/ansible.windows/issues/663
- win_get_url - if checksum is passed and destination file exists with different checksum file is always downloaded (https://github.com/ansible-collections/ansible.windows/issues/717)
- win_get_url - if checksum is passed and destination file exists with identical checksum no download is done unless force=yes (https://github.com/ansible-collections/ansible.windows/issues/717)
- win_group - Added ``--diff`` output support.
- win_group - Added ``members`` option to set the group membership. This is designed to replace the functionality of the ``win_group_membership`` module.
- win_group - Added ``sid`` return value representing the security identifier of the group when ``state=present``.
- win_group - Migrate to newer Ansible.Basic fragment for better input validation and testing support.

cisco.asa
~~~~~~~~~

- cisco.asa.asa - add support to fetch hardware specific information in facts
- cisco.asa.asa_acls - add support for specifying object-group as protocol

cisco.dnac
~~~~~~~~~~

- Added sample playbook for Device Configs Backup Module
- Bug fixes in [sda_fabric_sites_zones_workflow_manager module
- Bug fixes in accesspoint_workflow_manager module
- Bug fixes in lan_automation_workflow_manager module
- Bug fixes in pnp_workflow_manager module
- Bug fixes in sda_fabric_devices_workflow_manager
- Bug fixes in sda_fabric_transits_workflow_manager
- Bug fixes in template_workflow_manager module
- Changes in dnac.py file
- Changes in inventory_workflow_manager module
- Changes in ise_radius_integration_workflow_manager
- Changes in network_compliance_workflow_manager
- Changes in network_settings_workflow_manager
- Changes in sda_fabric_devices_workflow_manager module
- Changes in site_workflow_manager module
- Changes in swim_workflow_manager module
- Changes in template_workflow_manager
- Enhancements in [sda_fabric_virtual_networks_workflow_manager module to support batch operation.
- Enhancements in device_configs_backup_workflow_manager module to support unzipped backup file after download
- Enhancements in device_credential_workflow_manager module
- Enhancements in provision_workflow_manager module
- Enhancements in sda_host_port_onboarding_workflow_manager module
- Fixed issues in module sda_anycast_gateways_v1
- Fixed issues in module sda_layer3_virtual_networks_v1
- Supporting unmarking the devices in rma_workflow_manager module
- Unit test modules added for pnp_workflow_manager module
- aaa_services_count_v1_info - new module
- aaa_services_id_trend_analytics_v1 - new module
- aaa_services_id_v1_info - new module
- aaa_services_query_count_v1 - new module
- aaa_services_query_v1 - new module
- aaa_services_summary_analytics_v1 - new module
- aaa_services_top_n_analytics_v1 - new module
- aaa_services_trend_analytics_v1 - new module
- aaa_services_v1_info - new module
- application of the changes made in pull request 207
- application_visibility_network_devices_count_v1_info - new module
- application_visibility_network_devices_disable_app_telemetry_v1 - new module
- application_visibility_network_devices_disable_cbar_v1 - new module
- application_visibility_network_devices_enable_app_telemetry_v1 - new module
- application_visibility_network_devices_enable_cbar_v1 - new module
- application_visibility_network_devices_v1_info - new module
- assurance_tasks_count_v1_info - new module
- assurance_tasks_id_v1_info - new module
- assurance_tasks_v1_info - new module
- cisco_imcs_id_v1 - new module
- cisco_imcs_id_v1_info - new module
- cisco_imcs_v1 - new module
- cisco_imcs_v1_info - new module
- compliance_device_create_v1 - new module
- connection_modesetting_v1 - new module
- connection_modesetting_v1_info - new module
- device_configs_backup_workflow_manager - attribute 'unzip_backup' was added
- dhcp_services_count_v1_info - new module
- dhcp_services_id_trend_analytics_v1 - new module
- dhcp_services_id_v1_info - new module
- dhcp_services_query_count_v1 - new module
- dhcp_services_query_v1 - new module
- dhcp_services_summary_analytics_v1 - new module
- dhcp_services_top_n_analytics_v1 - new module
- dhcp_services_trend_analytics_v1 - new module
- dhcp_services_v1_info - new module
- diagnostic_tasks_id_detail_v1_info - new module
- diagnostic_tasks_id_v1_info - new module
- dna_health_score_definitions_count_v1_info - new module
- dna_network_devices_query_count_v1 - new module
- dns_services_count_v1_info - new module
- dns_services_id_trend_analytics_v1 - new module
- dns_services_id_v1_info - new module
- dns_services_query_count_v1 - new module
- dns_services_query_v1 - new module
- dns_services_summary_analytics_v1 - new module
- dns_services_top_n_analytics_v1 - new module
- dns_services_trend_analytics_v1 - new module
- dns_services_v1_info - new module
- fabric_site_health_summaries_count_v1_info - new module
- fabric_site_health_summaries_id_trend_analytics_v1_info - new module
- fabric_site_health_summaries_id_v1_info - new module
- fabric_site_health_summaries_v1_info - new module
- fabric_summary_v1_info - new module
- fabrics_fabric_id_switch_wireless_setting_reload_v1 - new module
- fabrics_fabric_id_switch_wireless_setting_v1 - new module
- fabrics_fabric_id_switch_wireless_setting_v1_info - new module
- fabrics_fabric_id_wireless_multicast_v1 - new module
- fabrics_fabric_id_wireless_multicast_v1_info - new module
- field_notices_results_network_devices_count_v1_info - new module
- field_notices_results_network_devices_network_device_id_notices_count_v1_info - new module
- field_notices_results_network_devices_network_device_id_notices_id_v1_info - new module
- field_notices_results_network_devices_network_device_id_notices_v1_info - new module
- field_notices_results_network_devices_network_device_id_v1_info - new module
- field_notices_results_network_devices_v1_info - new module
- field_notices_results_notices_id_network_devices_count_v1_info - new module
- field_notices_results_notices_id_network_devices_network_device_id_v1_info - new module
- field_notices_results_notices_id_network_devices_v1_info - new module
- field_notices_results_notices_id_v1_info - new module
- field_notices_results_notices_v1_info - new module
- field_notices_trials_v1 - new module
- field_notices_trials_v1_info - new module
- field_notices_trigger_scan_v1 - new module
- floors_floor_id_access_point_positions_bulk_change_v2 - new module
- floors_floor_id_access_point_positions_count_v2_info - new module
- floors_floor_id_access_point_positions_v2_info - new module
- floors_floor_id_planned_access_point_positions_assign_access_point_positions_v2 - new module
- floors_floor_id_planned_access_point_positions_bulk_change_v2 - new module
- floors_floor_id_planned_access_point_positions_bulk_v2 - new module
- floors_floor_id_planned_access_point_positions_count_v2_info - new module
- floors_floor_id_planned_access_point_positions_id_v2 - new module
- floors_floor_id_planned_access_point_positions_v2_info - new module
- icap_capture_files_count_v1_info - new module
- icap_capture_files_id_download_v1_info - new module
- icap_capture_files_id_v1_info - new module
- icap_capture_files_v1_info - new module
- icap_clients_id_stats_v1 - new module
- icap_radios_id_stats_v1 - new module
- icap_settings_configuration_models_id_delete_deploy_v1 - new module
- icap_settings_configuration_models_preview_activity_id_deploy_v1 - new module
- icap_settings_configuration_models_preview_activity_id_network_device_status_details_v1_info - new module
- icap_settings_configuration_models_preview_activity_id_network_devices_network_device_id_config_v1 - new module
- icap_settings_configuration_models_preview_activity_id_network_devices_network_device_id_config_v1_info - new module
- icap_settings_configuration_models_preview_activity_id_v1 - new module
- icap_settings_configuration_models_v1 - new module
- icap_settings_count_v1_info - new module
- icap_settings_deploy_id_delete_deploy_v1 - new module
- icap_settings_deploy_v1 - new module
- icap_settings_device_deployments_count_v1_info - new module
- icap_settings_device_deployments_v1_info - new module
- icap_settings_v1_info - new module
- icap_spectrum_interference_device_reports_v1_info - new module
- icap_spectrum_sensor_reports_v1_info - new module
- images_cco_sync_v1 - new module
- images_id_sites_site_id_tag_golden_v1 - new module
- images_id_sites_site_id_untag_golden_v1 - new module
- images_id_v1 - new module
- intent_network_devices_query_count_v1 - new module
- intent_network_devices_query_v1 - new module
- interfaces_id_trend_analytics_v1 - new module
- ipam_global_ip_address_pools_count_v1_info - new module
- ipam_global_ip_address_pools_global_ip_address_pool_id_subpools_count_v1_info - new module
- ipam_global_ip_address_pools_global_ip_address_pool_id_subpools_v1_info - new module
- ipam_global_ip_address_pools_id_v1 - new module
- ipam_global_ip_address_pools_id_v1_info - new module
- ipam_global_ip_address_pools_v1 - new module
- ipam_global_ip_address_pools_v1_info - new module
- ipam_site_ip_address_pools_count_v1_info - new module
- ipam_site_ip_address_pools_id_v1 - new module
- ipam_site_ip_address_pools_id_v1_info - new module
- ipam_site_ip_address_pools_v1 - new module
- ipam_site_ip_address_pools_v1_info - new module
- license_deregister_v1 - new module
- license_last_operation_status_v1_info - new module
- license_register_v1 - new module
- license_renew_v1 - new module
- license_status_v1_info - new module
- network_applications_count_v1_info - new module
- network_applications_trend_analytics_v1 - new module
- network_applications_v1_info - new module
- network_bugs_results_bugs_count_v1_info - new module
- network_bugs_results_bugs_id_network_devices_count_v1_info - new module
- network_bugs_results_bugs_id_network_devices_network_device_id_v1_info - new module
- network_bugs_results_bugs_id_network_devices_v1_info - new module
- network_bugs_results_bugs_id_v1_info - new module
- network_bugs_results_bugs_v1_info - new module
- network_bugs_results_network_devices_count_v1_info - new module
- network_bugs_results_network_devices_network_device_id_bugs_count_v1_info - new module
- network_bugs_results_network_devices_network_device_id_bugs_id_v1_info - new module
- network_bugs_results_network_devices_network_device_id_bugs_v1_info - new module
- network_bugs_results_network_devices_network_device_id_v1_info - new module
- network_bugs_results_network_devices_v1_info - new module
- network_bugs_results_trend_count_v1_info - new module
- network_bugs_results_trend_v1_info - new module
- network_bugs_trials_v1 - new module
- network_bugs_trials_v1_info - new module
- network_bugs_trigger_scan_v1 - new module
- network_device_config_files_count_v1_info - new module
- network_device_config_files_id_download_masked_v1 - new module
- network_device_config_files_id_download_unmasked_v1 - new module
- network_device_config_files_id_v1_info - new module
- network_device_config_files_v1_info - new module
- network_device_maintenance_schedules_count_v1_info - new module
- network_device_maintenance_schedules_id_v1 - new module
- network_device_maintenance_schedules_id_v1_info - new module
- network_device_maintenance_schedules_v1 - new module
- network_device_maintenance_schedules_v1_info - new module
- network_device_replacements_id_v1_info - new module
- network_device_replacements_v1_info - new module
- network_devices_delete_with_cleanup_v1 - new module
- network_devices_delete_without_cleanup_v1 - new module
- network_devices_id_v1_info - new module
- network_devices_intent_count_v1_info - new module
- network_devices_intent_v1_info - new module
- network_devices_top_n_analytics_v1 - new module
- network_profiles_for_sites_profile_id_templates_count_v1_info - new module
- network_profiles_for_sites_profile_id_templates_v1_info - new module
- network_settings_workflow_manager - attribute 'force_delete' was added
- projects_count_v1_info - new module
- projects_project_id_v1 - new module
- projects_project_id_v1_info - new module
- projects_v1 - new module
- projects_v1_info - new module
- qos_policy_setting_v1 - new module
- qos_policy_setting_v1_info - new module
- sda_fabric_devices_workflow_manager - attribute 'delete_fabric_device' was removed
- sda_host_port_onboarding_workflow_manager - attributes 'port_channel_details', 'port_assignment_details' were removed
- sda_host_port_onboarding_workflow_manager - attributes 'port_channels', 'fabric_site_name_hierarchy', 'port_assignments', 'wireless_ssids' were added
- sda_pending_fabric_events_apply_v1 - new module
- sda_pending_fabric_events_v1_info - new module
- security_advisories_results_advisories_count_v1_info - new module
- security_advisories_results_advisories_id_network_devices_count_v1_info - new module
- security_advisories_results_advisories_id_network_devices_network_device_id_v1_info - new module
- security_advisories_results_advisories_id_network_devices_v1_info - new module
- security_advisories_results_advisories_id_v1_info - new module
- security_advisories_results_advisories_v1_info - new module
- security_advisories_results_network_devices_network_device_id_advisories_count_v1_info - new module
- security_advisories_results_network_devices_network_device_id_advisories_id_v1_info - new module
- security_advisories_results_network_devices_network_device_id_advisories_v1_info - new module
- security_advisories_results_network_devices_network_device_id_v1_info - new module
- security_advisories_results_network_devices_v1_info - new module
- security_advisories_results_trend_count_v1_info - new module
- security_advisories_results_trend_v1_info - new module
- security_advisories_trials_v1 - new module
- security_advisories_trials_v1_info - new module
- security_advisories_trigger_scan_v1 - new module
- site_health_summaries_id_trend_analytics_v1_info - new module
- site_health_summaries_trend_analytics_v1_info - new module
- site_kpi_summaries_count_v1_info - new module
- site_kpi_summaries_id_v1_info - new module
- site_kpi_summaries_query_count_v1 - new module
- site_kpi_summaries_query_v1 - new module
- site_kpi_summaries_summary_analytics_v1 - new module
- site_kpi_summaries_summary_analytics_v1_info - new module
- site_kpi_summaries_top_n_analytics_v1_info - new module
- site_kpi_summaries_trend_analytics_v1 - new module
- site_kpi_summaries_v1_info - new module
- site_wise_images_summary_v1_info - new module
- sites_site_id_wireless_settings_ssids_id_update_v1 - new module
- tags_interfaces_members_associations_bulk_v1 - new module
- tags_network_devices_members_associations_bulk_v1 - new module
- templates_template_id_network_profiles_for_sites_bulk_create_v1 - new module
- templates_template_id_network_profiles_for_sites_bulk_delete_v1 - new module
- templates_template_id_network_profiles_for_sites_count_v1_info - new module
- templates_template_id_network_profiles_for_sites_profile_id_delete_v1 - new module
- templates_template_id_network_profiles_for_sites_v1 - new module
- templates_template_id_network_profiles_for_sites_v1_info - new module
- templates_template_id_versions_commit_v1 - new module
- templates_template_id_versions_count_v1_info - new module
- templates_template_id_versions_v1_info - new module
- templates_template_id_versions_version_id_v1_info - new module
- transit_network_health_summaries_count_v1_info - new module
- transit_network_health_summaries_id_trend_analytics_v1_info - new module
- transit_network_health_summaries_id_v1_info - new module
- transit_network_health_summaries_v1_info - new module
- virtual_network_health_summaries_count_v1_info - new module
- virtual_network_health_summaries_id_trend_analytics_v1_info - new module
- virtual_network_health_summaries_id_v1_info - new module
- virtual_network_health_summaries_v1_info - new module
- wireless_accesspoint_configuration_count_v1_info - new module
- wireless_controllers_anchor_capable_devices_v1_info - new module
- wireless_controllers_mesh_ap_neighbours_count_v1_info - new module
- wireless_controllers_mesh_ap_neighbours_v1_info - new module
- wireless_controllers_network_device_id_ap_authorization_lists_v1_info - new module
- wireless_profiles_id_policy_tags_bulk_v1 - new module
- wireless_profiles_id_policy_tags_count_v1_info - new module
- wireless_profiles_id_policy_tags_policy_tag_id_v1 - new module
- wireless_profiles_id_policy_tags_policy_tag_id_v1_info - new module
- wireless_profiles_id_site_tags_bulk_v1 - new module
- wireless_profiles_id_site_tags_count_v1_info - new module
- wireless_profiles_id_site_tags_site_tag_id_v1 - new module
- wireless_profiles_id_site_tags_site_tag_id_v1_info - new module
- wireless_profiles_id_site_tags_v1_info - new module
- wireless_settings_anchor_groups_count_v1_info - new module
- wireless_settings_anchor_groups_id_v1 - new module
- wireless_settings_anchor_groups_id_v1_info - new module
- wireless_settings_anchor_groups_v1 - new module
- wireless_settings_anchor_groups_v1_info - new module
- wireless_settings_ap_authorization_lists_count_v1_info - new module
- wireless_settings_ap_authorization_lists_id_v1 - new module
- wireless_settings_ap_authorization_lists_id_v1_info - new module
- wireless_settings_ap_authorization_lists_v1 - new module
- wireless_settings_ap_authorization_lists_v1_info - new module
- wireless_settings_ap_profiles_count_v1_info - new module
- wireless_settings_ap_profiles_id_v1 - new module
- wireless_settings_ap_profiles_id_v1_info - new module
- wireless_settings_ap_profiles_v1 - new module
- wireless_settings_ap_profiles_v1_info - new module
- wireless_settings_network_device_id_assign_anchor_managed_ap_locations_v1 - new module
- wireless_settings_power_profiles_count_v1_info - new module
- wireless_settings_power_profiles_id_v1 - new module
- wireless_settings_power_profiles_id_v1_info - new module
- wireless_settings_power_profiles_v1 - new module
- wireless_settings_power_profiles_v1_info - new module
- wireless_settings_ssids_override_at_sites_v1_info - new module

cisco.ios
~~~~~~~~~

- Added ios_vrf_interfaces resource module,that helps with configuration of vrfs within interface
- Adds a new module `ios_vrf_address_family` to manage VRFs address families on Cisco IOS devices.

cisco.iosxr
~~~~~~~~~~~

- Added iosxr_vrf_interfaces resource module, that helps with configuration of vrfs within interface.
- Adds support for setting local-preference with plus/minus values in route policies

cisco.ise
~~~~~~~~~

- Fix linting issues.

cisco.meraki
~~~~~~~~~~~~

- Sanity and CI fixes.
- administered_identities_me_api_keys_info - new plugin.
- administered_identities_me_api_keys_revoke - new plugin.
- devices_live_tools_leds_blink - new plugin.
- devices_wireless_electronic_shelf_label - new plugin.
- devices_wireless_electronic_shelf_label_info - new plugin.
- networks_appliance_sdwan_internet_policies - new plugin.
- networks_cancel - new plugin.
- networks_floor_plans_auto_locate_jobs_batch - new plugin.
- networks_floor_plans_devices_batch_update - new plugin.
- networks_publish - new plugin.
- networks_recalculate - new plugin.
- networks_wireless_air_marshal_rules - new plugin.
- networks_wireless_air_marshal_rules_delete - new plugin.
- networks_wireless_air_marshal_rules_update - new plugin.
- networks_wireless_air_marshal_settings - new plugin.
- networks_wireless_electronic_shelf_label - new plugin.
- organizations_assets - new plugin.
- organizations_assurance_alerts_info - new plugin.
- organizations_assurance_alerts_overview_by_network_info - new plugin.
- organizations_assurance_alerts_overview_by_type_info - new plugin.
- organizations_assurance_alerts_overview_historical_info - new plugin.
- organizations_assurance_alerts_overview_info - new plugin.
- organizations_assurance_alerts_restore - new plugin.
- organizations_cellular_gateway_esims_inventory_info - new plugin.
- organizations_cellular_gateway_esims_service_providers_accounts - new plugin.
- organizations_cellular_gateway_esims_service_providers_accounts_communication_plans_info - new plugin.
- organizations_cellular_gateway_esims_service_providers_accounts_info - new plugin.
- organizations_cellular_gateway_esims_service_providers_accounts_rate_plans_info - new plugin.
- organizations_cellular_gateway_esims_service_providers_info - new plugin.
- organizations_cellular_gateway_esims_swap - new plugin.
- organizations_devices_details_bulk_update - new plugin.
- organizations_devices_overview_by_model_info - new plugin.
- organizations_floor_plans_auto_locate_devices_info - new plugin.
- organizations_floor_plans_auto_locate_statuses_info - new plugin.
- organizations_splash_themes - new plugin.
- organizations_splash_themes_info - new plugin.
- organizations_summary_top_applications_by_usage_info - new plugin.
- organizations_summary_top_applications_categories_by_usage_info - new plugin.
- organizations_switch_ports_clients_overview_by_device_info - new plugin.
- organizations_switch_ports_overview_info - new plugin.
- organizations_switch_ports_statuses_by_switch_info - new plugin.
- organizations_switch_ports_topology_discovery_by_device_info - new plugin.
- organizations_wireless_air_marshal_rules_info - new plugin.
- organizations_wireless_air_marshal_settings_by_network_info - new plugin.
- organizations_wireless_clients_overview_by_device_info - new plugin.
- organizations_wireless_controller_clients_overview_history_by_device_by_interval_info - new plugin.
- organizations_wireless_controller_connections_info - new plugin.
- organizations_wireless_controller_devices_interfaces_l2_by_device_info - new plugin.
- organizations_wireless_controller_devices_interfaces_l2_statuses_change_history_by_device_info - new plugin.
- organizations_wireless_controller_devices_interfaces_l2_usage_history_by_interval_info - new plugin.
- organizations_wireless_controller_devices_interfaces_l3_by_device_info - new plugin.
- organizations_wireless_controller_devices_interfaces_l3_statuses_change_history_by_device_info - new plugin.
- organizations_wireless_controller_devices_interfaces_l3_usage_history_by_interval_info - new plugin.
- organizations_wireless_controller_devices_interfaces_packets_overview_by_device_info - new plugin.
- organizations_wireless_controller_devices_interfaces_usage_history_by_interval_info - new plugin.
- organizations_wireless_controller_devices_redundancy_failover_history_info - new plugin.
- organizations_wireless_controller_devices_redundancy_statuses_info - new plugin.
- organizations_wireless_controller_devices_system_utilization_history_by_interval_info - new plugin.
- organizations_wireless_controller_overview_by_device_info - new plugin.
- organizations_wireless_devices_wireless_controllers_by_device_info - new plugin.
- organizations_wireless_radio_auto_rf_channels_recalculate - new plugin.
- organizations_wireless_rf_profiles_assignments_by_device_info - new plugin.
- organizations_wireless_ssids_statuses_by_device_info - new plugin.

cisco.nxos
~~~~~~~~~~

- Add support for VRF address family via `vrf_address_family` resource module.
- Added nxos_vrf_interfaces resource module, that helps with configuration of vrfs within interface in favor of nxos_vrf_interface module.
- nxos_telemetry - Added support for 'overridden' state to provide complete configuration override capabilities.

community.ciscosmb
~~~~~~~~~~~~~~~~~~

- added Catalyst 1300 to supported platforms
- parsing neighbour table allowes empty 4th column to allow Cisco Catalyst 1300 support

community.crypto
~~~~~~~~~~~~~~~~

- acme_certificate - add compatibility for ACME CAs that are not fully RFC8555 compliant and do not provide ``challenges`` in authz objects (https://github.com/ansible-collections/community.crypto/issues/824, https://github.com/ansible-collections/community.crypto/pull/832).
- acme_certificate - add options ``order_creation_error_strategy`` and ``order_creation_max_retries`` which allow to configure the error handling behavior if creating a new ACME order fails. This is particularly important when using the ``include_renewal_cert_id`` option, and the default value ``auto`` for ``order_creation_error_strategy`` tries to gracefully handle related errors (https://github.com/ansible-collections/community.crypto/pull/842).
- acme_certificate - allow to chose a profile for certificate generation, in case the CA supports this using Internet-Draft `draft-aaron-acme-profiles <https://datatracker.ietf.org/doc/draft-aaron-acme-profiles/>`__ (https://github.com/ansible-collections/community.crypto/pull/835).
- acme_certificate_renewal_info - add ``exists`` and ``parsable`` return values and ``treat_parsing_error_as_non_existing`` option (https://github.com/ansible-collections/community.crypto/pull/838).
- luks_device - allow to provide passphrases base64-encoded (https://github.com/ansible-collections/community.crypto/issues/827, https://github.com/ansible-collections/community.crypto/pull/829).
- x509_certificate_convert - add new option ``verify_cert_parsable`` which allows to check whether the certificate can actually be parsed (https://github.com/ansible-collections/community.crypto/issues/809, https://github.com/ansible-collections/community.crypto/pull/830).

community.docker
~~~~~~~~~~~~~~~~

- docker_compose_v2 - add ``ignore_build_events`` option (default value ``true``) which allows to (not) ignore build events for change detection (https://github.com/ansible-collections/community.docker/issues/1005, https://github.com/ansible-collections/community.docker/issues/pull/1011).
- docker_compose_v2* modules - determine compose version with ``docker compose version`` and only then fall back to ``docker info`` (https://github.com/ansible-collections/community.docker/pull/1021).
- docker_image_build - ``outputs[].name`` can now be a list of strings (https://github.com/ansible-collections/community.docker/pull/1006).
- docker_image_build - the executed command is now returned in the ``command`` return value in case of success and some errors (https://github.com/ansible-collections/community.docker/pull/1006).
- docker_network - added ``ingress`` option (https://github.com/ansible-collections/community.docker/pull/999).

community.general
~~~~~~~~~~~~~~~~~

- MH module utils - delegate ``debug`` to the underlying ``AnsibleModule`` instance or issues a warning if an attribute already exists with that name (https://github.com/ansible-collections/community.general/pull/9577).
- apache2_mod_proxy - better handling regexp extraction (https://github.com/ansible-collections/community.general/pull/9609).
- apache2_mod_proxy - change type of ``state`` to a list of strings. No change for the users (https://github.com/ansible-collections/community.general/pull/9600).
- apache2_mod_proxy - improve readability when using results from ``fecth_url()`` (https://github.com/ansible-collections/community.general/pull/9608).
- apache2_mod_proxy - refactor repeated code into method (https://github.com/ansible-collections/community.general/pull/9599).
- apache2_mod_proxy - remove unused parameter and code from ``Balancer`` constructor (https://github.com/ansible-collections/community.general/pull/9614).
- apache2_mod_proxy - simplified and improved string manipulation (https://github.com/ansible-collections/community.general/pull/9614).
- apache2_mod_proxy - use ``deps`` to handle dependencies (https://github.com/ansible-collections/community.general/pull/9612).
- bitwarden lookup plugin - use f-strings instead of interpolations or ``format`` (https://github.com/ansible-collections/community.general/pull/9324).
- cgroup_memory_recap callback plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9583).
- cgroup_memory_recap callback plugin - use f-strings instead of interpolations or ``format`` (https://github.com/ansible-collections/community.general/pull/9321).
- chef_databag lookup plugin - use f-strings instead of interpolations or ``format`` (https://github.com/ansible-collections/community.general/pull/9324).
- chroot connection plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9584).
- chroot connection plugin - clean up string conversions (https://github.com/ansible-collections/community.general/pull/9379).
- chroot connection plugin - use f-strings instead of interpolations or ``format`` (https://github.com/ansible-collections/community.general/pull/9322).
- cloud_init_data_facts - open file using ``open()`` as a context manager (https://github.com/ansible-collections/community.general/pull/9579).
- cobbler inventory plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9584).
- cobbler inventory plugin - clean up string conversions (https://github.com/ansible-collections/community.general/pull/9379).
- cobbler inventory plugin - use f-strings instead of interpolations or ``format`` (https://github.com/ansible-collections/community.general/pull/9323).
- collection_version lookup plugin - use f-strings instead of interpolations or ``format`` (https://github.com/ansible-collections/community.general/pull/9324).
- consul_kv lookup plugin - use f-strings instead of interpolations or ``format`` (https://github.com/ansible-collections/community.general/pull/9324).
- context_demo callback plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9583).
- context_demo callback plugin - use f-strings instead of interpolations or ``format`` (https://github.com/ansible-collections/community.general/pull/9321).
- counter filter plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9585).
- counter_enabled callback plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9583).
- counter_enabled callback plugin - use f-strings instead of interpolations or ``format`` (https://github.com/ansible-collections/community.general/pull/9321).
- cpanm - enable usage of option ``--with-recommends`` (https://github.com/ansible-collections/community.general/issues/9554, https://github.com/ansible-collections/community.general/pull/9555).
- cpanm - enable usage of option ``--with-suggests`` (https://github.com/ansible-collections/community.general/pull/9555).
- crc32 filter plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9585).
- credstash lookup plugin - use f-strings instead of interpolations or ``format`` (https://github.com/ansible-collections/community.general/pull/9324).
- cronvar - open file using ``open()`` as a context manager (https://github.com/ansible-collections/community.general/pull/9579).
- crypttab - open file using ``open()`` as a context manager (https://github.com/ansible-collections/community.general/pull/9579).
- cyberarkpassword lookup plugin - clean up string conversions (https://github.com/ansible-collections/community.general/pull/9379).
- cyberarkpassword lookup plugin - use f-strings instead of interpolations or ``format`` (https://github.com/ansible-collections/community.general/pull/9324).
- default_without_diff callback plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9583).
- dense callback plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9583).
- dense callback plugin - use f-strings instead of interpolations or ``format`` (https://github.com/ansible-collections/community.general/pull/9321).
- dependent lookup plugin - use f-strings instead of interpolations or ``format`` (https://github.com/ansible-collections/community.general/pull/9324).
- dict filter plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9585).
- dict_kv filter plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9585).
- dig lookup plugin - clean up string conversions (https://github.com/ansible-collections/community.general/pull/9379).
- dig lookup plugin - use f-strings instead of interpolations or ``format`` (https://github.com/ansible-collections/community.general/pull/9324).
- diy callback plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9583).
- diy callback plugin - use f-strings instead of interpolations or ``format`` (https://github.com/ansible-collections/community.general/pull/9321).
- dnstxt lookup plugin - clean up string conversions (https://github.com/ansible-collections/community.general/pull/9379).
- dnstxt lookup plugin - use f-strings instead of interpolations or ``format`` (https://github.com/ansible-collections/community.general/pull/9324).
- doas become plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9583).
- doas become plugin - use f-strings instead of interpolations or ``format`` (https://github.com/ansible-collections/community.general/pull/9319).
- dsv lookup plugin - use f-strings instead of interpolations or ``format`` (https://github.com/ansible-collections/community.general/pull/9324).
- dzdo become plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9583).
- dzdo become plugin - use f-strings instead of interpolations or ``format`` (https://github.com/ansible-collections/community.general/pull/9319).
- elastic callback plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9583).
- elastic callback plugin - use f-strings instead of interpolations or ``format`` (https://github.com/ansible-collections/community.general/pull/9321).
- etcd lookup plugin - use f-strings instead of interpolations or ``format`` (https://github.com/ansible-collections/community.general/pull/9324).
- etcd3 lookup plugin - clean up string conversions (https://github.com/ansible-collections/community.general/pull/9379).
- etcd3 lookup plugin - use f-strings instead of interpolations or ``format`` (https://github.com/ansible-collections/community.general/pull/9324).
- filetree lookup plugin - use f-strings instead of interpolations or ``format`` (https://github.com/ansible-collections/community.general/pull/9324).
- from_csv filter plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9585).
- from_csv filter plugin - clean up string conversions (https://github.com/ansible-collections/community.general/pull/9379).
- from_ini filter plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9585).
- from_ini filter plugin - clean up string conversions (https://github.com/ansible-collections/community.general/pull/9379).
- funcd connection plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9584).
- funcd connection plugin - use f-strings instead of interpolations or ``format`` (https://github.com/ansible-collections/community.general/pull/9322).
- github_app_access_token lookup plugin - use f-strings instead of interpolations or ``format`` (https://github.com/ansible-collections/community.general/pull/9324).
- gitlab_instance_variable - add support for ``raw`` variables suboption (https://github.com/ansible-collections/community.general/pull/9425).
- gitlab_runners inventory plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9584).
- gitlab_runners inventory plugin - clean up string conversions (https://github.com/ansible-collections/community.general/pull/9379).
- gitlab_runners inventory plugin - use f-strings instead of interpolations or ``format`` (https://github.com/ansible-collections/community.general/pull/9323).
- groupby_as_dict filter plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9585).
- hashids filter plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9585).
- hiera lookup plugin - use f-strings instead of interpolations or ``format`` (https://github.com/ansible-collections/community.general/pull/9324).
- icinga2 inventory plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9584).
- icinga2 inventory plugin - use f-strings instead of interpolations or ``format`` (https://github.com/ansible-collections/community.general/pull/9323).
- incus connection plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9584).
- incus connection plugin - use f-strings instead of interpolations or ``format`` (https://github.com/ansible-collections/community.general/pull/9322).
- iocage connection plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9584).
- iocage connection plugin - use f-strings instead of interpolations or ``format`` (https://github.com/ansible-collections/community.general/pull/9322).
- iocage inventory plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9584).
- iocage inventory plugin - clean up string conversions (https://github.com/ansible-collections/community.general/pull/9379).
- iocage inventory plugin - the new parameter ``sudo`` of the plugin lets the command ``iocage list -l`` to run as root on the iocage host. This is needed to get the IPv4 of a running DHCP jail (https://github.com/ansible-collections/community.general/issues/9572, https://github.com/ansible-collections/community.general/pull/9573).
- iptables_state action plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9583).
- iptables_state action plugin - use f-strings instead of interpolations or ``format`` (https://github.com/ansible-collections/community.general/pull/9318).
- jabber callback plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9583).
- jabber callback plugin - use f-strings instead of interpolations or ``format`` (https://github.com/ansible-collections/community.general/pull/9321).
- jail connection plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9584).
- jail connection plugin - use f-strings instead of interpolations or ``format`` (https://github.com/ansible-collections/community.general/pull/9322).
- jc filter plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9585).
- jira - transition operation now has ``status_id`` to directly reference wanted transition (https://github.com/ansible-collections/community.general/pull/9602).
- json_query filter plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9585).
- keep_keys filter plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9585).
- keycloak - add an action group for Keycloak modules to allow ``module_defaults`` to be set for Keycloak tasks (https://github.com/ansible-collections/community.general/pull/9284).
- keycloak_* modules - ``refresh_token`` parameter added. When multiple authentication parameters are provided (``token``, ``refresh_token``, and ``auth_username``/``auth_password``), modules will now automatically retry requests upon authentication errors (401), using in order the token, refresh token, and username/password (https://github.com/ansible-collections/community.general/pull/9494).
- keyring lookup plugin - use f-strings instead of interpolations or ``format`` (https://github.com/ansible-collections/community.general/pull/9324).
- known_hosts - open file using ``open()`` as a context manager (https://github.com/ansible-collections/community.general/pull/9579).
- ksu become plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9583).
- ksu become plugin - use f-strings instead of interpolations or ``format`` (https://github.com/ansible-collections/community.general/pull/9319).
- lastpass lookup plugin - use f-strings instead of interpolations or ``format`` (https://github.com/ansible-collections/community.general/pull/9324).
- linode inventory plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9584).
- linode inventory plugin - use f-strings instead of interpolations or ``format`` (https://github.com/ansible-collections/community.general/pull/9323).
- lists filter plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9585).
- lists_mergeby filter plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9585).
- lmdb_kv lookup plugin - clean up string conversions (https://github.com/ansible-collections/community.general/pull/9379).
- lmdb_kv lookup plugin - use f-strings instead of interpolations or ``format`` (https://github.com/ansible-collections/community.general/pull/9324).
- locale_gen - invert the logic to determine ``ubuntu_mode``, making it look first for ``/etc/locale.gen`` (set ``ubuntu_mode`` to ``False``) and only then looking for ``/var/lib/locales/supported.d/`` (set ``ubuntu_mode`` to ``True``) (https://github.com/ansible-collections/community.general/pull/9238, https://github.com/ansible-collections/community.general/issues/9131, https://github.com/ansible-collections/community.general/issues/8487).
- locale_gen - new return value ``mechanism`` to better express the semantics of the ``ubuntu_mode``, with the possible values being either ``glibc`` (``ubuntu_mode=False``) or ``ubuntu_legacy`` (``ubuntu_mode=True``) (https://github.com/ansible-collections/community.general/pull/9238).
- log_plays callback plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9583).
- log_plays callback plugin - use f-strings instead of interpolations or ``format`` (https://github.com/ansible-collections/community.general/pull/9321).
- loganalytics callback plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9583).
- loganalytics callback plugin - use f-strings instead of interpolations or ``format`` (https://github.com/ansible-collections/community.general/pull/9321).
- logdna callback plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9583).
- logdna callback plugin - use f-strings instead of interpolations or ``format`` (https://github.com/ansible-collections/community.general/pull/9321).
- logentries callback plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9583).
- logentries callback plugin - clean up string conversions (https://github.com/ansible-collections/community.general/pull/9379).
- logentries callback plugin - use f-strings instead of interpolations or ``format`` (https://github.com/ansible-collections/community.general/pull/9321).
- logstash callback plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9583).
- lxc connection plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9584).
- lxc connection plugin - use f-strings instead of interpolations or ``format`` (https://github.com/ansible-collections/community.general/pull/9322).
- lxd connection plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9584).
- lxd connection plugin - use f-strings instead of interpolations or ``format`` (https://github.com/ansible-collections/community.general/pull/9322).
- lxd inventory plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9584).
- lxd inventory plugin - clean up string conversions (https://github.com/ansible-collections/community.general/pull/9379).
- lxd inventory plugin - use f-strings instead of interpolations or ``format`` (https://github.com/ansible-collections/community.general/pull/9323).
- machinectl become plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9583).
- machinectl become plugin - use f-strings instead of interpolations or ``format`` (https://github.com/ansible-collections/community.general/pull/9319).
- mail callback plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9583).
- mail callback plugin - use f-strings instead of interpolations or ``format`` (https://github.com/ansible-collections/community.general/pull/9321).
- manageiq_alert_profiles - improve handling of parameter requirements (https://github.com/ansible-collections/community.general/pull/9449).
- manifold lookup plugin - clean up string conversions (https://github.com/ansible-collections/community.general/pull/9379).
- manifold lookup plugin - use f-strings instead of interpolations or ``format`` (https://github.com/ansible-collections/community.general/pull/9324).
- memcached cache plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9583).
- memcached cache plugin - use f-strings instead of interpolations or ``format`` (https://github.com/ansible-collections/community.general/pull/9320).
- merge_variables lookup plugin - use f-strings instead of interpolations or ``format`` (https://github.com/ansible-collections/community.general/pull/9324).
- nmap inventory plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9584).
- nmap inventory plugin - clean up string conversions (https://github.com/ansible-collections/community.general/pull/9379).
- nmap inventory plugin - use f-strings instead of interpolations or ``format`` (https://github.com/ansible-collections/community.general/pull/9323).
- nmcli - add a option ``fail_over_mac`` (https://github.com/ansible-collections/community.general/issues/9570, https://github.com/ansible-collections/community.general/pull/9571).
- nrdp callback plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9583).
- nrdp callback plugin - use f-strings instead of interpolations or ``format`` (https://github.com/ansible-collections/community.general/pull/9321).
- null callback plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9583).
- one_template - adds ``filter`` option for retrieving templates which are not owned by the user (https://github.com/ansible-collections/community.general/pull/9547, https://github.com/ansible-collections/community.general/issues/9278).
- onepassword lookup plugin - clean up string conversions (https://github.com/ansible-collections/community.general/pull/9379).
- onepassword lookup plugin - use f-strings instead of interpolations or ``format`` (https://github.com/ansible-collections/community.general/pull/9324).
- onepassword_doc lookup plugin - use f-strings instead of interpolations or ``format`` (https://github.com/ansible-collections/community.general/pull/9324).
- online inventory plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9584).
- online inventory plugin - use f-strings instead of interpolations or ``format`` (https://github.com/ansible-collections/community.general/pull/9323).
- opennebula inventory plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9584).
- opennebula inventory plugin - clean up string conversions (https://github.com/ansible-collections/community.general/pull/9379).
- opennebula inventory plugin - use f-strings instead of interpolations or ``format`` (https://github.com/ansible-collections/community.general/pull/9323).
- opentelemetry callback plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9583).
- opentelemetry callback plugin - remove code handling Python versions prior to 3.7 (https://github.com/ansible-collections/community.general/pull/9482).
- opentelemetry callback plugin - remove code handling Python versions prior to 3.7 (https://github.com/ansible-collections/community.general/pull/9503).
- opentelemetry callback plugin - use f-strings instead of interpolations or ``format`` (https://github.com/ansible-collections/community.general/pull/9321).
- pacemaker_cluster - remove unused code (https://github.com/ansible-collections/community.general/pull/9471).
- pacemaker_cluster - using safer mechanism to run external command (https://github.com/ansible-collections/community.general/pull/9471).
- parted - open file using ``open()`` as a context manager (https://github.com/ansible-collections/community.general/pull/9579).
- passwordstore lookup plugin - use f-strings instead of interpolations or ``format`` (https://github.com/ansible-collections/community.general/pull/9324).
- pbrun become plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9583).
- pbrun become plugin - use f-strings instead of interpolations or ``format`` (https://github.com/ansible-collections/community.general/pull/9319).
- pfexec become plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9583).
- pfexec become plugin - use f-strings instead of interpolations or ``format`` (https://github.com/ansible-collections/community.general/pull/9319).
- pickle cache plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9583).
- pmrun become plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9583).
- pmrun become plugin - use f-strings instead of interpolations or ``format`` (https://github.com/ansible-collections/community.general/pull/9319).
- proxmox - refactors the proxmox module (https://github.com/ansible-collections/community.general/pull/9225).
- proxmox inventory plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9584).
- proxmox inventory plugin - clean up string conversions (https://github.com/ansible-collections/community.general/pull/9379).
- proxmox inventory plugin - strip whitespace from ``user``, ``token_id``, and ``token_secret`` (https://github.com/ansible-collections/community.general/issues/9227, https://github.com/ansible-collections/community.general/pull/9228/).
- proxmox inventory plugin - use f-strings instead of interpolations or ``format`` (https://github.com/ansible-collections/community.general/pull/9323).
- proxmox module utils - add method ``api_task_complete`` that can wait for task completion and return error message (https://github.com/ansible-collections/community.general/pull/9256).
- proxmox_backup - refactor permission checking to improve code readability and maintainability (https://github.com/ansible-collections/community.general/pull/9239).
- proxmox_pct_remote connection plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9584).
- proxmox_template - add support for checksum validation with new options ``checksum_algorithm`` and ``checksum`` (https://github.com/ansible-collections/community.general/issues/9553, https://github.com/ansible-collections/community.general/pull/9601).
- pulp_repo - open file using ``open()`` as a context manager (https://github.com/ansible-collections/community.general/pull/9579).
- qubes connection plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9584).
- qubes connection plugin - use f-strings instead of interpolations or ``format`` (https://github.com/ansible-collections/community.general/pull/9322).
- random_mac filter plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9585).
- random_pet lookup plugin - use f-strings instead of interpolations or ``format`` (https://github.com/ansible-collections/community.general/pull/9324).
- redfish_info - add command ``GetAccountServiceConfig`` to get full information about AccountService configuration (https://github.com/ansible-collections/community.general/pull/9403).
- redhat_subscription - open file using ``open()`` as a context manager (https://github.com/ansible-collections/community.general/pull/9579).
- redis cache plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9583).
- redis cache plugin - clean up string conversions (https://github.com/ansible-collections/community.general/pull/9379).
- redis cache plugin - use f-strings instead of interpolations or ``format`` (https://github.com/ansible-collections/community.general/pull/9320).
- redis lookup plugin - use f-strings instead of interpolations or ``format`` (https://github.com/ansible-collections/community.general/pull/9324).
- remove_keys filter plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9585).
- replace_keys filter plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9585).
- revbitspss lookup plugin - use f-strings instead of interpolations or ``format`` (https://github.com/ansible-collections/community.general/pull/9324).
- reveal_ansible_type filter plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9585).
- run0 become plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9583).
- saltstack connection plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9584).
- saltstack connection plugin - use f-strings instead of interpolations or ``format`` (https://github.com/ansible-collections/community.general/pull/9322).
- say callback plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9583).
- say callback plugin - use f-strings instead of interpolations or ``format`` (https://github.com/ansible-collections/community.general/pull/9321).
- scaleway inventory plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9584).
- scaleway inventory plugin - clean up string conversions (https://github.com/ansible-collections/community.general/pull/9379).
- scaleway inventory plugin - use f-strings instead of interpolations or ``format`` (https://github.com/ansible-collections/community.general/pull/9323).
- selective callback plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9583).
- selective callback plugin - use f-strings instead of interpolations or ``format`` (https://github.com/ansible-collections/community.general/pull/9321).
- sesu become plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9583).
- sesu become plugin - use f-strings instead of interpolations or ``format`` (https://github.com/ansible-collections/community.general/pull/9319).
- shelvefile lookup plugin - use f-strings instead of interpolations or ``format`` (https://github.com/ansible-collections/community.general/pull/9324).
- shutdown action plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9583).
- shutdown action plugin - clean up string conversions (https://github.com/ansible-collections/community.general/pull/9379).
- shutdown action plugin - use f-strings instead of interpolations or ``format`` (https://github.com/ansible-collections/community.general/pull/9318).
- slack callback plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9583).
- slack callback plugin - clean up string conversions (https://github.com/ansible-collections/community.general/pull/9379).
- slack callback plugin - use f-strings instead of interpolations or ``format`` (https://github.com/ansible-collections/community.general/pull/9321).
- snap - add return value ``version`` (https://github.com/ansible-collections/community.general/pull/9598).
- snap_alias - add return value ``version`` (https://github.com/ansible-collections/community.general/pull/9598).
- solaris_zone - open file using ``open()`` as a context manager (https://github.com/ansible-collections/community.general/pull/9579).
- sorcery - open file using ``open()`` as a context manager (https://github.com/ansible-collections/community.general/pull/9579).
- splunk callback plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9583).
- splunk callback plugin - use f-strings instead of interpolations or ``format`` (https://github.com/ansible-collections/community.general/pull/9321).
- stackpath_compute inventory plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9584).
- stackpath_compute inventory plugin - use f-strings instead of interpolations or ``format`` (https://github.com/ansible-collections/community.general/pull/9323).
- sudosu become plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9583).
- sudosu become plugin - use f-strings instead of interpolations or ``format`` (https://github.com/ansible-collections/community.general/pull/9319).
- sumologic callback plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9583).
- syslog_json callback plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9583).
- time filter plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9585).
- timestamp callback plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9583).
- timestamp callback plugin - use f-strings instead of interpolations or ``format`` (https://github.com/ansible-collections/community.general/pull/9321).
- timezone - open file using ``open()`` as a context manager (https://github.com/ansible-collections/community.general/pull/9579).
- to_ini filter plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9585).
- to_ini filter plugin - clean up string conversions (https://github.com/ansible-collections/community.general/pull/9379).
- tss lookup plugin - clean up string conversions (https://github.com/ansible-collections/community.general/pull/9379).
- tss lookup plugin - use f-strings instead of interpolations or ``format`` (https://github.com/ansible-collections/community.general/pull/9324).
- ufw - add support for ``vrrp`` protocol (https://github.com/ansible-collections/community.general/issues/9562, https://github.com/ansible-collections/community.general/pull/9582).
- unicode_normalize filter plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9585).
- unixy callback plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9583).
- unixy callback plugin - use f-strings instead of interpolations or ``format`` (https://github.com/ansible-collections/community.general/pull/9321).
- version_sort filter plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9585).
- virtualbox inventory plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9584).
- virtualbox inventory plugin - clean up string conversions (https://github.com/ansible-collections/community.general/pull/9379).
- virtualbox inventory plugin - use f-strings instead of interpolations or ``format`` (https://github.com/ansible-collections/community.general/pull/9323).
- xbps - add ``root`` and ``repository`` options to enable bootstrapping new void installations (https://github.com/ansible-collections/community.general/pull/9174).
- xen_orchestra inventory plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9584).
- xen_orchestra inventory plugin - use f-strings instead of interpolations or ``format`` (https://github.com/ansible-collections/community.general/pull/9323).
- xfconf - add return value ``version`` (https://github.com/ansible-collections/community.general/pull/9226).
- xfconf_info - add return value ``version`` (https://github.com/ansible-collections/community.general/pull/9226).
- yaml cache plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9583).
- yaml callback plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9583).
- yaml callback plugin - use f-strings instead of interpolations or ``format`` (https://github.com/ansible-collections/community.general/pull/9321).
- zone connection plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9584).
- zone connection plugin - use f-strings instead of interpolations or ``format`` (https://github.com/ansible-collections/community.general/pull/9322).
- zypper - add ``quiet`` option (https://github.com/ansible-collections/community.general/pull/9270).
- zypper - add ``simple_errors`` option (https://github.com/ansible-collections/community.general/pull/9270).

community.hrobot
~~~~~~~~~~~~~~~~

- All modules and plugins now have a ``rate_limit_retry_timeout`` option, which allows to configure for how long to wait in case of rate limiting errors. By default, the modules wait indefinitely. Setting the option to ``0`` does not retry (this was the behavior in previous versions), and a positive value sets a number of seconds to wait at most (https://github.com/ansible-collections/community.hrobot/pull/140).
- boot - it is now possible to specify SSH public keys in ``authorized_keys``. The fingerprint needed by the Robot API will be extracted automatically (https://github.com/ansible-collections/community.hrobot/pull/134).
- v_switch - the module is now part of the ``community.hrobot.robot`` action group, despite already being documented as part of it (https://github.com/ansible-collections/community.hrobot/pull/136).

community.mysql
~~~~~~~~~~~~~~~

- mysql_db - added ``zstd`` (de)compression support for ``import``/``dump`` states (https://github.com/ansible-collections/community.mysql/issues/696).
- mysql_query - returns the ``execution_time_ms`` list containing execution time per query in milliseconds.

community.okd
~~~~~~~~~~~~~

- openshift_auth - fix issue where openshift_auth module sometimes does not delete the auth token. Based on stale PR (https://github.com/openshift/community.okd/pull/194).

community.postgresql
~~~~~~~~~~~~~~~~~~~~

- postgresql_query - returns the `execution_time_ms` list containing execution time per query in milliseconds (https://github.com/ansible-collections/community.postgresql/issues/787).

community.rabbitmq
~~~~~~~~~~~~~~~~~~

- rabbitmq_policy - adjust the `apply_to` parameter to also accept the new options `classic_queues`, `quorum_queues` and `streams` which are supported since rabbitmq 3.12

community.routeros
~~~~~~~~~~~~~~~~~~

- api_info, api_modify - add missing attribute ``require-message-auth`` for the ``radius`` path which exists since RouterOS version 7.15 (https://github.com/ansible-collections/community.routeros/issues/338, https://github.com/ansible-collections/community.routeros/pull/339).
- api_info, api_modify - add support for the ``routing filter community-list`` path implemented by RouterOS 7 and newer (https://github.com/ansible-collections/community.routeros/pull/331).
- api_info, api_modify - add the ``interface 6to4`` path. Used to manage IPv6 tunnels via tunnel-brokers like HE, where native IPv6 is not provided (https://github.com/ansible-collections/community.routeros/pull/342).
- api_info, api_modify - add the ``interface wireless access-list`` and ``interface wireless connect-list`` paths (https://github.com/ansible-collections/community.routeros/issues/284, https://github.com/ansible-collections/community.routeros/pull/340).
- api_info, api_modify - add the ``use-interface-duid`` option for ``ipv6 dhcp-client`` path. This option prevents issues with Fritzbox modems and routers, when using virtual interfaces (like VLANs) may create duplicated records in hosts config, this breaks original "expose-host" function. Also add the ``script``, ``custom-duid`` and ``validate-server-duid`` as backport from 7.15 version update (https://github.com/ansible-collections/community.routeros/pull/341).

community.vmware
~~~~~~~~~~~~~~~~

- vmware_guest - Add new cutomization spec param `domainOU`. (https://github.com/ansible-collections/community.vmware/issues/2275)
- vmware_guest - Speedup network search (https://github.com/ansible-collections/community.vmware/pull/2278).
- vmware_guest_network - Speedup network search (https://github.com/ansible-collections/community.vmware/pull/2277).

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- idrac_certificates -  This module is enhanced to support SSL CSR generation for 4096 key size.
- omevv_firmware_repository_profile - This module allows to resync the repository profiles from the OpenManage Update Manager Plug-in.

dellemc.powerflex
~~~~~~~~~~~~~~~~~

- Added Ansible role to support installation and uninstallation of SDT.
- Info module is enhanced to support the listing of SDTs and NVMe hosts.

f5networks.f5_modules
~~~~~~~~~~~~~~~~~~~~~

- bigip_virtual_server - Fixed issue - Disabling/Enabling Virtual Server does not require profiles, type in Update

google.cloud
~~~~~~~~~~~~

- gcp_pubsub_subscription - allows to create GCS subscription

ibm.storage_virtualize
~~~~~~~~~~~~~~~~~~~~~~

- ibm_sv_manage_replication_policy - Added support for disaster recovery
- ibm_sv_manage_storage_partition - Added support for partition migration and disaster recovery
- ibm_sv_manage_truststore_for_replication - Added support for enabling various options (syslog, RESTAPI, vasa, ipsec, snmp and email) for existing truststore
- ibm_svc_initial_setup - Added support for flashcopy default grain size and SI (Storage Insights) to be able to control partition migration
- ibm_svc_manage_portset - Added support for linking portset of 2 clusters for PBHA
- ibm_svc_manage_volume - Added support for converting thinclone volume(s) to clone
- ibm_svc_manage_volumegroup - Added support for disaster recovery and converting thinclone volumegroup to clone

kubernetes.core
~~~~~~~~~~~~~~~

- Bump version of ansible-lint to minimum 24.7.0 (https://github.com/ansible-collections/kubernetes.core/pull/765).
- Parameter insecure_registry added to helm_template as equivalent of insecure-skip-tls-verify (https://github.com/ansible-collections/kubernetes.core/pull/805).
- k8s_drain - Improve error message for pod disruption budget when draining a node (https://github.com/ansible-collections/kubernetes.core/issues/797).

lowlydba.sqlserver
~~~~~~~~~~~~~~~~~~

- Add new `login_role` module to add/remove server roles for logins (https://github.com/lowlydba/lowlydba.sqlserver/pull/293).
- Add new user_role module to manage users' membership to database roles (https://github.com/lowlydba/lowlydba.sqlserver/pull/292).

microsoft.ad
~~~~~~~~~~~~

- Added support for Windows Server 2025
- domain - Added ``replication_source_dc`` to specify the domain controller to use as the replication source for the new domain - https://github.com/ansible-collections/microsoft.ad/issues/159
- domain_controller - Added ``replication_source_dc`` to specify the domain controller to use as the replication source for the new domain controller - https://github.com/ansible-collections/microsoft.ad/issues/159
- microsoft.ad.user - Added ``groups.permissions_failure_action`` to control the behaviour when failing to modify the user's groups - (https://github.com/ansible-collections/microsoft.ad/issues/140).

vmware.vmware
~~~~~~~~~~~~~

- _vmware - standardize getter method names and documentation
- argument specs - Remove redundant argument specs. Update pyvmomi modules to use new consolidated spec
- content_template - Fix bad reference of library variable that was refactored to library_id
- doc fragments - Remove redundant fragments. Update pyvmomi modules to use new consolidated docs
- esxi_host - Added inventory plugin to gather info about ESXi hosts
- esxi_maintenance_mode - migrate esxi maintenance module from community
- info - Made vm_name variable required only when state is set to present in content_template module
- pyvmomi module base - refactor class to use the pyvmomi shared client util class as a base
- rest module base - refactor class to use the rest shared client util class as a base
- vms - added vms inventory plugin. consolidated shared docs/code with esxi hosts inventory plugin

vmware.vmware_rest
~~~~~~~~~~~~~~~~~~

- info - changed relative links in README.md to absolute links

Deprecated Features
-------------------

- The ``cisco.asa`` collection has been deprecated.
  It will be removed from Ansible 12 if no one starts maintaining it again before Ansible 12.
  See `Collections Removal Process for unmaintained collections <https://docs.ansible.com/ansible/devel/community/collection_contributors/collection_package_removal.html#unmaintained-collections>`__ for more details (`https://forum.ansible.com/t/38960 <https://forum.ansible.com/t/38960>`__).

amazon.aws
~~~~~~~~~~

- autoscaling_group - the ``decrement_desired_capacity`` parameter has been deprecated and will be removed in release 14.0.0 of this collection. Management of instances attached an autoscaling group can be performed using the  ``amazon.aws.autoscaling_instance`` module (https://github.com/ansible-collections/amazon.aws/pull/2396).
- autoscaling_group - the ``replace_batch_size``, ``lc_check`` and ``lt_check`` parameters have been deprecated and will be removed in release 14.0.0 of this collection. Rolling replacement of instances in an autoscaling group can be performed using the  ``amazon.aws.autoscaling_instance_refresh`` module (https://github.com/ansible-collections/amazon.aws/pull/2396).
- autoscaling_group - the functionality provided through the ``detach_instances`` parameter has been deprecated and will be removed in release 14.0.0 of this collection. Management of instances attached an autoscaling group can be performed using the  ``amazon.aws.autoscaling_instance`` module (https://github.com/ansible-collections/amazon.aws/pull/2396).
- autoscaling_group - the functionality provided through the ``replace_all_instances`` parameter has been deprecated and will be removed in release 14.0.0 of this collection. Rolling replacement of instances in an autoscaling group can be performed using the  ``amazon.aws.autoscaling_instance_refresh`` module (https://github.com/ansible-collections/amazon.aws/pull/2396).
- autoscaling_group - the functionality provided through the ``replace_instances`` parameter has been deprecated and will be removed in release 14.0.0 of this collection. Management of instances attached an autoscaling group can be performed using the  ``amazon.aws.autoscaling_instance`` module (https://github.com/ansible-collections/amazon.aws/pull/2396).

community.crypto
~~~~~~~~~~~~~~~~

- Support for ansible-core 2.11, 2.12, 2.13, 2.14, 2.15, and 2.16 is deprecated, and will be removed in the next major release (community.crypto 3.0.0). Some modules might still work with some of these versions afterwards, but we will no longer keep compatibility code that was needed to support them. Note that this means that support for all Python versions before 3.7 will be dropped, also on the target side (https://github.com/ansible-collections/community.crypto/issues/559, https://github.com/ansible-collections/community.crypto/pull/839).
- Support for cryptography < 3.4 is deprecated, and will be removed in the next major release (community.crypto 3.0.0). Some modules might still work with older versions of cryptography, but we will no longer keep compatibility code that was needed to support them (https://github.com/ansible-collections/community.crypto/issues/559, https://github.com/ansible-collections/community.crypto/pull/839).
- openssl_pkcs12 - the PyOpenSSL based backend is deprecated and will be removed from community.crypto 3.0.0. From that point on you need cryptography 3.0 or newer to use this module (https://github.com/ansible-collections/community.crypto/issues/667, https://github.com/ansible-collections/community.crypto/pull/831).

community.general
~~~~~~~~~~~~~~~~~

- MH module utils - attribute ``debug`` definition in subclasses of MH is now deprecated, as that name will become a delegation to ``AnsibleModule`` in community.general 12.0.0, and any such attribute will be overridden by that delegation in that version (https://github.com/ansible-collections/community.general/pull/9577).
- atomic_container - module is deprecated and will be removed in community.general 13.0.0 (https://github.com/ansible-collections/community.general/pull/9487).
- atomic_host - module is deprecated and will be removed in community.general 13.0.0 (https://github.com/ansible-collections/community.general/pull/9487).
- atomic_image - module is deprecated and will be removed in community.general 13.0.0 (https://github.com/ansible-collections/community.general/pull/9487).
- facter - module is deprecated and will be removed in community.general 12.0.0, use ``community.general.facter_facts`` instead (https://github.com/ansible-collections/community.general/pull/9451).
- locale_gen - ``ubuntu_mode=True``, or ``mechanism=ubuntu_legacy`` is deprecated and will be removed in community.general 13.0.0 (https://github.com/ansible-collections/community.general/pull/9238).
- proxmox - removes default value ``false`` of ``update`` parameter. This will be changed to a default of ``true`` in community.general 11.0.0 (https://github.com/ansible-collections/community.general/pull/9225).
- pure module utils - the module utils is deprecated and will be removed from community.general 12.0.0. The modules using this were removed in community.general 3.0.0 (https://github.com/ansible-collections/community.general/pull/9432).
- purestorage doc fragments - the doc fragment is deprecated and will be removed from community.general 12.0.0. The modules using this were removed in community.general 3.0.0 (https://github.com/ansible-collections/community.general/pull/9432).
- sensu_check - module is deprecated and will be removed in community.general 13.0.0, use collection ``sensu.sensu_go`` instead (https://github.com/ansible-collections/community.general/pull/9483).
- sensu_client - module is deprecated and will be removed in community.general 13.0.0, use collection ``sensu.sensu_go`` instead (https://github.com/ansible-collections/community.general/pull/9483).
- sensu_handler - module is deprecated and will be removed in community.general 13.0.0, use collection ``sensu.sensu_go`` instead (https://github.com/ansible-collections/community.general/pull/9483).
- sensu_silence - module is deprecated and will be removed in community.general 13.0.0, use collection ``sensu.sensu_go`` instead (https://github.com/ansible-collections/community.general/pull/9483).
- sensu_subscription - module is deprecated and will be removed in community.general 13.0.0, use collection ``sensu.sensu_go`` instead (https://github.com/ansible-collections/community.general/pull/9483).
- slack - the default value ``auto`` of the ``prepend_hash`` option is deprecated and will change to ``never`` in community.general 12.0.0 (https://github.com/ansible-collections/community.general/pull/9443).
- yaml callback plugin - deprecate plugin in favor of ``result_format=yaml`` in plugin ``ansible.bulitin.default`` (https://github.com/ansible-collections/community.general/pull/9456).

community.hrobot
~~~~~~~~~~~~~~~~

- boot - the various ``arch`` suboptions have been deprecated and will be removed from community.hrobot 3.0.0 (https://github.com/ansible-collections/community.hrobot/pull/134).

community.vmware
~~~~~~~~~~~~~~~~

- vmware_cluster_info - the module has been deprecated and will be removed in community.vmware 7.0.0 (https://github.com/ansible-collections/community.vmware/pull/2260).

Security Fixes
--------------

cloudscale_ch.cloud
~~~~~~~~~~~~~~~~~~~

- Validate API tokens before passing them to Ansible, to ensure that a badly formed one (i.e., one with newlines) is not accidentally logged.

community.general
~~~~~~~~~~~~~~~~~

- keycloak_authentication - API calls did not properly set the ``priority`` during update resulting in incorrectly sorted authentication flows. This apparently only affects Keycloak 25 or newer (https://github.com/ansible-collections/community.general/pull/9263).
- keycloak_client - Sanitize ``saml.encryption.private.key`` so it does not show in the logs (https://github.com/ansible-collections/community.general/pull/9621).

Bugfixes
--------

Ansible-core
~~~~~~~~~~~~

- Ansible will now also warn when reserved keywords are set via a module (set_fact, include_vars, etc).
- Ansible.Basic - Fix ``required_if`` check when the option value to check is unset or set to null.
- Use consistent multiprocessing context for action write locks
- ansible-test - Fix up coverage reporting to properly translate the temporary path of integration test modules to the expected static test module path.
- ansible-vault will now correctly handle `--prompt`, previously it would issue an error about stdin if no 2nd argument was passed
- copy action now prevents user from setting internal options.
- gather_facts action now defaults to `ansible.legacy.setup` if `smart` was set, no network OS was found and no other alias for `setup` was present.
- gather_facts action will now issues errors and warnings as appropriate if a network OS is detected but no facts modules are defined for it.
- ssh - Improve the logic for parsing CLIXML data in stderr when working with Windows host. This fixes issues when the raw stderr contains invalid UTF-8 byte sequences and improves embedded CLIXML sequences.
- ssh - connection options were incorrectly templated during ``reset_connection`` tasks (https://github.com/ansible/ansible/pull/84238).

amazon.aws
~~~~~~~~~~

- cloudformation - Fix bug where termination protection is not updated when create_changeset=true is used for stack updates (https://github.com/ansible-collections/amazon.aws/pull/2391).
- ec2_security_group - Fix the diff mode issue when creating a security group containing a rule with a managed prefix list (https://github.com/ansible-collections/amazon.aws/issues/2373).
- ec2_vpc_net - handle ipv6_cidr ``false`` and no Ipv6CidrBlockAssociationSet in vpc (https://github.com/ansible-collections/amazon.aws/pull/2374).
- elbv2 - Fix load balancer listener comparison when DefaultActions contain any action other than forward (https://github.com/ansible-collections/amazon.aws/issues/2377).
- lambda - Remove non UTF-8 data (contents of Lambda ZIP file) from the module output to avoid Ansible error (https://github.com/ansible-collections/amazon.aws/issues/2386).
- module_utils/ec2 - catch error code ``InvalidElasticIpID.NotFound`` on function ``create_nat_gateway()``, sometimes the ``allocate_address`` API calls will return the ID for a new elastic IP resource before it can be consistently referenced (https://github.com/ansible-collections/amazon.aws/issues/1872).
- rds_cluster - Fix issue occurring when updating RDS cluster domain (https://github.com/ansible-collections/amazon.aws/issues/2390).

ansible.windows
~~~~~~~~~~~~~~~

- ansible.windows.win_powershell - Add extra checks to avoid ``GetType`` error when converting the output object - ttps://github.com/ansible-collections/ansible.windows/issues/708
- win_group_membership - Fix bug when input ``members`` contained duplicate members that were not already present in the group - https://github.com/ansible-collections/ansible.windows/issues/736
- win_powershell - Ensure ``$Ansible.Result = @()`` as an empty array is returned as an empty list and not null - https://github.com/ansible-collections/ansible.windows/issues/686
- win_updates - Only set the Access control sections on the temporary directory created by the module. This avoids the error when the ``SeSecurityPrivilege`` privilege isn't present.

cisco.asa
~~~~~~~~~

- cisco.asa - fixed Cliconf.edit_config() got an unexpected keyword argument 'candidate' error
- cisco.asa.asa_acls - fixed ace parsing when source is object-group and its name contains dots
- cisco.asa.asa_acls - fixed acl modification commands order if object/group name contains `no`

cisco.ios
~~~~~~~~~

- Added a test to validate the gathered state for VLAN configuration context, improving reliability.
- Cleaned up unit tests that were passing for the wrong reasons. The updated tests now ensure the right config sections are verified for VLAN configurations.
- Fix overridden state operations to ensure excluded VLANs in the provided configuration are removed, thus overriding the VLAN configuration.
- Fix purged state operation to enable users to completely remove VLAN configurations.
- Fixed an issue with VLAN configuration gathering where pre-filled data was blocking proper fetching of dynamic VLAN details. Now VLAN facts are populated correctly for all cases.
- Fixes an issue with facts gathering failing when an sub interface is in a deleted state.
- Improve documentation to provide clarity on the "shutdown" variable.
- Improve unit tests to align with the changes made.
- Made improvements to ensure VLAN facts are gathered properly, both for specific configurations and general VLAN settings.
- ios_route_maps - Fix removal of ACLs in replaced state to properly remove unspecified ACLs while leaving specified ones intact.
- ios_route_maps - Fix removal of ACLs logic in replaced state to properly remove unspecified ACLs while leaving specified ones intact.

cisco.ise
~~~~~~~~~

- personas_promote_primary - fix timeout issue.

cisco.meraki
~~~~~~~~~~~~

- Ansible utils requirements updated.
- Change alias 'message' to 'message_rule' due is a reserved ansible word in meraki_mx_intrusion_prevention module.
- Issue fixes for workflow-ansible-lint.
- Old playbook tests removed.
- README fixes.
- cisco.meraki.networks_appliance_firewall_l3_firewall_rules fails with "Unexpected failure during module execution 'rules' - specific 'rules' extraction has been removed.
- cisco.meraki.networks_appliance_vlans_settings fails with "msg" "Object does not exists, plugin only has update" - specific 'vlansEnabled' extraction has been removed.
- cisco.meraki.networks_clients_info - incorrect API endpoint, fixing info module.
- cisco.meraki.networks_devices_claim failed with error unexpected keyword argument 'add_atomically' - bad naming solved.
- cisco.meraki.networks_switch_stacks delete stack not working, fixing path parameters.
- runtime updated requires_ansible from 2.14.0 to '>=2.15.0'.

cisco.nxos
~~~~~~~~~~

- Fixed hardware fact gathering failure for CPU utilization parsing on NX-OS 9.3(3) by handling both list and single value formats of onemin_percent
- Fixed the invalid feature name error for port-security by updating the feature mapping from `eth_port_sec` to `eth-port-sec`.
- Fixes mixed usage of f-string and format string in action plugin for consistency.
- Fixes nxos_user purge deleting non-local users,ensuring only local users are removed.
- [bgp_templates] - fix the show commands used to ensure task does not fail if BGP is not enabled on the device.
- lag_interfaces - Fix bug where lag interfaces was not erroring on command failure. (https://github.com/ansible-collections/cisco.nxos/pull/923)
- nxos_l2_interfaces - Fixed handling of 'none' value in allowed_vlans to properly set trunk VLAN none

community.crypto
~~~~~~~~~~~~~~~~

- crypto_info - when running the module on Fedora 41 with ``cryptography`` installed from the package repository, the module crashed apparently due to some elliptic curves being removed from libssl against which cryptography is running, which cryptography did not expect (https://github.com/ansible-collections/community.crypto/pull/834).

community.dns
~~~~~~~~~~~~~

- Update Public Suffix List.

community.docker
~~~~~~~~~~~~~~~~

- Fix label sanitization code to avoid crashes in case of errors (https://github.com/ansible-collections/community.docker/issues/1028, https://github.com/ansible-collections/community.docker/pull/1029).
- docker_compose_v2 - when using Compose 2.31.0 or newer, revert to the old behavior that image rebuilds, for example if ``rebuild=always``, only result in ``changed`` if a container has been restarted (https://github.com/ansible-collections/community.docker/issues/1005, https://github.com/ansible-collections/community.docker/issues/pull/1011).
- docker_image_build - work around bug resp. very unexpected behavior in Docker buildx that overwrites all image names in ``--output`` parameters if ``--tag`` is provided, which the module did by default in the past. The module now only supplies ``--tag`` if ``outputs`` is empty. If ``outputs`` has entries, it will add an additional entry with ``type=image`` if no entry of ``type=image`` contains the image name specified by the ``name`` and ``tag`` options (https://github.com/ansible-collections/community.docker/issues/1001, https://github.com/ansible-collections/community.docker/pull/1006).
- docker_network - added waiting while container actually disconnect from Swarm network (https://github.com/ansible-collections/community.docker/pull/999).
- docker_network - containers are only reconnected to a network if they really exist (https://github.com/ansible-collections/community.docker/pull/999).
- docker_network - enabled "force" option in Docker network container disconnect API call (https://github.com/ansible-collections/community.docker/pull/999).
- docker_swarm_info - do not crash when finding Swarm jobs if ``services=true`` (https://github.com/ansible-collections/community.docker/issues/1003).

community.general
~~~~~~~~~~~~~~~~~

- dig lookup plugin - correctly handle ``NoNameserver`` exception (https://github.com/ansible-collections/community.general/pull/9363, https://github.com/ansible-collections/community.general/issues/9362).
- homebrew - fix incorrect handling of aliased homebrew modules when the alias is requested (https://github.com/ansible-collections/community.general/pull/9255, https://github.com/ansible-collections/community.general/issues/9240).
- homebrew - fix incorrect handling of homebrew modules when a tap is requested (https://github.com/ansible-collections/community.general/pull/9546, https://github.com/ansible-collections/community.general/issues/9533).
- htpasswd - report changes when file permissions are adjusted (https://github.com/ansible-collections/community.general/issues/9485, https://github.com/ansible-collections/community.general/pull/9490).
- iocage inventory plugin - the plugin parses the IP4 tab of the jails list and put the elements into the new variable ``iocage_ip4_dict``. In multiple interface format the variable ``iocage_ip4`` keeps the comma-separated list of IP4 (https://github.com/ansible-collections/community.general/issues/9538).
- pipx - honor option ``global`` when ``state=latest`` (https://github.com/ansible-collections/community.general/pull/9623).
- proxmox - fixes idempotency of template conversions (https://github.com/ansible-collections/community.general/pull/9225, https://github.com/ansible-collections/community.general/issues/8811).
- proxmox - fixes incorrect parsing for bind-only mounts (https://github.com/ansible-collections/community.general/pull/9225, https://github.com/ansible-collections/community.general/issues/8982).
- proxmox - fixes issues with disk_volume variable (https://github.com/ansible-collections/community.general/pull/9225, https://github.com/ansible-collections/community.general/issues/9065).
- proxmox module utils - fixes ignoring of ``choose_first_if_multiple`` argument in ``get_vmid`` (https://github.com/ansible-collections/community.general/pull/9225).
- proxmox_backup - fix incorrect key lookup in vmid permission check (https://github.com/ansible-collections/community.general/pull/9223).
- proxmox_disk - fix async method and make ``resize_disk`` method handle errors correctly (https://github.com/ansible-collections/community.general/pull/9256).
- proxmox_template - fix the wrong path called on ``proxmox_template.task_status`` (https://github.com/ansible-collections/community.general/issues/9276, https://github.com/ansible-collections/community.general/pull/9277).
- qubes connection plugin - fix the printing of debug information (https://github.com/ansible-collections/community.general/pull/9334).
- redfish_utils module utils - Fix ``VerifyBiosAttributes`` command on multi system resource nodes (https://github.com/ansible-collections/community.general/pull/9234).
- redhat_subscription - do not try to unsubscribe (i.e. remove subscriptions)
  when unregistering a system: newer versions of subscription-manager, as
  available in EL 10 and Fedora 41+, do not support entitlements anymore, and
  thus unsubscribing will fail
  (https://github.com/ansible-collections/community.general/pull/9578).

community.libvirt
~~~~~~~~~~~~~~~~~

- libvirt_lxc - add configuration for libvirt_lxc_noseclabel.

community.postgresql
~~~~~~~~~~~~~~~~~~~~

- postgresql_info - fix failure when a default database is used (neither ``db`` nor ``login_db`` are specified) (https://github.com/ansible-collections/community.postgresql/issues/794).
- postgresql_info - fix issue when gathering information fails if user doesn't have access to all databases (https://github.com/ansible-collections/community.postgresql/pull/788).
- postgresql_info - fix module failure when the ``db`` parameter is used instead of ``login_db`` (https://github.com/ansible-collections/community.postgresql/issues/794).
- postgresql_pg_hba - fixes #777 the module will ignore the 'address' and 'netmask' options again when the contype is 'local' (https://github.com/ansible-collections/community.postgresql/pull/779)
- postgresql_privs -  fix the error occurring when trying to grant a function execution and set the schema to not-specified (https://github.com/ansible-collections/community.postgresql/pull/783).

community.rabbitmq
~~~~~~~~~~~~~~~~~~

- rabbitmq_publish - fix support for publishing headers as a part of a message (https://github.com/ansible-collections/community.rabbitmq/pull/182)

community.vmware
~~~~~~~~~~~~~~~~

- vmware_guest - setting vApp properties on virtual machines without vApp options raised an AttributeError. Fix now gracefully handles a `None` value for vApp options when retrieving current vApp properties (https://github.com/ansible-collections/community.vmware/pull/2220).

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- idrac_certificates - (Issue 737) - Fixed SSL CSR generation for 4096 key size.

f5networks.f5_modules
~~~~~~~~~~~~~~~~~~~~~

- bigip_monitor_external - external monitor user-defined variables not reflected for non-common partition
- bigip_profile_server_ssl - Fixed bug - create server SSL profile if SSL key is passphrase protected
- bigip_snmp_community - Allow v3 usernames that begin with a number or contains any special characters.

fortinet.fortios
~~~~~~~~~~~~~~~~

- Fix errors in Ansible sanity test with Ansible-core 2.18
- Github

google.cloud
~~~~~~~~~~~~

- ansible - 2.17 is now the minimum version supported
- ansible - 3.11 is now the minimum Python version
- ansible-test - fixed sanity tests
- ansible-test - integration tests are now run against 2.17 and 2.18
- gcp_bigquery_table - properly handle BigQuery table clustering fields
- gcp_pubsub_subscription - fixed improper subscription uprade PATCH request

ibm.storage_virtualize
~~~~~~~~~~~~~~~~~~~~~~

- ibm_svc_manage_flashcopy - Added support for creating flashcopy with existing target volume

kubernetes.core
~~~~~~~~~~~~~~~

- helm - Helm version checks did not support RC versions. They now accept any version tags. (https://github.com/ansible-collections/kubernetes.core/pull/745).
- helm_pull - Apply no_log=True to pass_credentials to silence false positive warning. (https://github.com/ansible-collections/kubernetes.core/pull/796).
- k8s_drain - Fix k8s_drain does not wait for single pod (https://github.com/ansible-collections/kubernetes.core/issues/769).
- k8s_drain - Fix k8s_drain runs into a timeout when evicting a pod which is part of a stateful set  (https://github.com/ansible-collections/kubernetes.core/issues/792).
- kubeconfig option should not appear in module invocation log (https://github.com/ansible-collections/kubernetes.core/issues/782).
- kustomize - kustomize plugin fails with deprecation warnings (https://github.com/ansible-collections/kubernetes.core/issues/639).
- waiter - Fix waiting for daemonset when desired number of pods is 0. (https://github.com/ansible-collections/kubernetes.core/pull/756).

lowlydba.sqlserver
~~~~~~~~~~~~~~~~~~

- Fix error that occurred when creating a login with `skip_password_reset` as true. (https://github.com/lowlydba/lowlydba.sqlserver/pull/287)
- Fix error when creating an agent job schedule with `enabled` as true. (https://github.com/lowlydba/lowlydba.sqlserver/pull/288)

purestorage.flashblade
~~~~~~~~~~~~~~~~~~~~~~

- purefb_bucket - Fixed issue with idempotency reported when ``hard_limit`` not provided.
- purefb_info - Fixed ``AttributeError`` for ``snapshot`` subset when snapshot had been created manually, rather than using a snapshot policy
- purefb_info - Fixed issue with admin token creation time and bucket policies
- purefb_policy - Fixed syntax error is account name.
- purefb_smtp - Fix errors that occurred after adding support for smtp encrpytion and using the module on older FlashBlades.
- purefb_snap - Fixed issue where ``target`` incorrectly required for a regular snapshot

vmware.vmware
~~~~~~~~~~~~~

- client utils - Fixed error message when required library could not be imported

vmware.vmware_rest
~~~~~~~~~~~~~~~~~~

- module_utils - fixed return value for vmware.vmware_rest.vcenter_vm_guest_filesystem_directories module
- vcenter_ovf_libraryitem - Update documentation to mention the metadata cannot be updated via conventional means. Added example showing workaround (https://github.com/ansible-collections/vmware.vmware_rest/issues/385)

Known Issues
------------

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- idrac_diagnostics - Issue(285322) - This module doesn't support export of diagnostics file to HTTP and HTTPS share via SOCKS proxy.
- idrac_firmware - Issue(279282) - This module does not support firmware update using HTTP, HTTPS, and FTP shares with authentication on iDRAC8.
- ome_smart_fabric_uplink - Issue(186024) - The module supported by OpenManage Enterprise Modular, however it does not allow the creation of multiple uplinks of the same name. If an uplink is created using the same name as an existing uplink, then the existing uplink is modified.

New Plugins
-----------

Connection
~~~~~~~~~~

- community.general.proxmox_pct_remote - Run tasks in Proxmox LXC container instances using pct CLI via SSH.

Filter
~~~~~~

- community.general.json_diff - Create a JSON patch by comparing two JSON files.
- community.general.json_patch - Apply a JSON-Patch (RFC 6902) operation to an object.
- community.general.json_patch_recipe - Apply JSON-Patch (RFC 6902) operations to an object.
- microsoft.ad.split_dn - Splits an LDAP DistinguishedName.

Inventory
~~~~~~~~~

- community.general.iocage - iocage inventory source.

Lookup
~~~~~~

- community.general.onepassword_ssh_key - Fetch SSH keys stored in 1Password.

New Modules
-----------

amazon.aws
~~~~~~~~~~

- amazon.aws.rds_instance_param_group_info - Describes the RDS parameter group.

ansible.windows
~~~~~~~~~~~~~~~

- ansible.windows.win_audit_policy_system - Used to make changes to the system wide Audit Policy
- ansible.windows.win_audit_rule - Adds an audit rule to files, folders, or registry keys
- ansible.windows.win_auto_logon - Adds or Sets auto logon registry keys.
- ansible.windows.win_certificate_info - Get information on certificates from a Windows Certificate Store
- ansible.windows.win_computer_description - Set windows description, owner and organization
- ansible.windows.win_credential - Manages Windows Credentials in the Credential Manager
- ansible.windows.win_dhcp_lease - Manage Windows Server DHCP Leases
- ansible.windows.win_dns_record - Manage Windows Server DNS records
- ansible.windows.win_dns_zone - Manage Windows Server DNS Zones
- ansible.windows.win_eventlog - Manage Windows event logs
- ansible.windows.win_feature_info - Gather information about Windows features
- ansible.windows.win_file_compression - Alters the compression of files and directories on NTFS partitions.
- ansible.windows.win_firewall - Enable or disable the Windows Firewall
- ansible.windows.win_hosts - Manages hosts file entries on Windows.
- ansible.windows.win_hotfix - Install and uninstalls Windows hotfixes
- ansible.windows.win_http_proxy - Manages proxy settings for WinHTTP
- ansible.windows.win_inet_proxy - Manages proxy settings for WinINet and Internet Explorer
- ansible.windows.win_listen_ports_facts - Recopilates the facts of the listening ports of the machine
- ansible.windows.win_mapped_drive - Map network drives for users
- ansible.windows.win_product_facts - Provides Windows product and license information
- ansible.windows.win_region - Set the region and format settings
- ansible.windows.win_route - Add or remove a static route
- ansible.windows.win_timezone - Sets Windows machine timezone
- ansible.windows.win_user_profile - Manages the Windows user profiles.

cisco.iosxr
~~~~~~~~~~~

- cisco.iosxr.iosxr_vrf_interfaces - Resource module to configure VRF interfaces.

cisco.nxos
~~~~~~~~~~

- cisco.nxos.nxos_vrf_address_family - Resource module to configure VRF address family definitions.

community.crypto
~~~~~~~~~~~~~~~~

- community.crypto.acme_certificate_order_create - Create an ACME v2 order.
- community.crypto.acme_certificate_order_finalize - Finalize an ACME v2 order.
- community.crypto.acme_certificate_order_info - Obtain information for an ACME v2 order.
- community.crypto.acme_certificate_order_validate - Validate authorizations of an ACME v2 order.

community.general
~~~~~~~~~~~~~~~~~

- community.general.android_sdk - Manages Android SDK packages.
- community.general.ldap_inc - Use the Modify-Increment LDAP V3 feature to increment an attribute value.
- community.general.proxmox_backup_info - Retrieve information on Proxmox scheduled backups.
- community.general.systemd_creds_decrypt - C(systemd)'s C(systemd-creds decrypt) plugin.
- community.general.systemd_creds_encrypt - C(systemd)'s C(systemd-creds encrypt) plugin.

community.hrobot
~~~~~~~~~~~~~~~~

- community.hrobot.storagebox - Modify a storage box's basic configuration.
- community.hrobot.storagebox_info - Query information on one or more storage boxes.
- community.hrobot.storagebox_set_password - (Re)set the password for a storage box.
- community.hrobot.storagebox_snapshot_plan - Modify a storage box's snapshot plans.
- community.hrobot.storagebox_snapshot_plan_info - Query the snapshot plans for a storage box.

dellemc.powerflex
~~~~~~~~~~~~~~~~~

- dellemc.powerflex.nvme_host - Manage NVMe Hosts on Dell PowerFlex
- dellemc.powerflex.sdt - Manage SDTs on Dell PowerFlex

kubernetes.core
~~~~~~~~~~~~~~~

- kubernetes.core.helm_registry_auth - Helm registry authentication module

lowlydba.sqlserver
~~~~~~~~~~~~~~~~~~

- lowlydba.sqlserver.login_role - Configures a login's  server roles.
- lowlydba.sqlserver.user_role - Configures a user's role in a database.

Unchanged Collections
---------------------

- ansible.netcommon (still version 7.1.0)
- ansible.posix (still version 1.6.2)
- ansible.utils (still version 5.1.2)
- arista.eos (still version 10.0.1)
- awx.awx (still version 24.6.1)
- azure.azcollection (still version 3.1.0)
- check_point.mgmt (still version 6.2.1)
- chocolatey.chocolatey (still version 1.5.3)
- cisco.aci (still version 2.10.1)
- cisco.intersight (still version 2.0.20)
- cisco.mso (still version 2.9.0)
- cloud.common (still version 4.0.0)
- community.aws (still version 9.0.0)
- community.digitalocean (still version 1.27.0)
- community.grafana (still version 2.1.0)
- community.hashi_vault (still version 6.2.0)
- community.library_inventory_filtering_v1 (still version 1.0.2)
- community.network (still version 5.1.0)
- community.proxysql (still version 1.6.0)
- community.sap_libs (still version 1.4.2)
- community.windows (still version 2.3.0)
- community.zabbix (still version 3.2.0)
- containers.podman (still version 1.16.2)
- cyberark.pas (still version 1.0.30)
- dellemc.enterprise_sonic (still version 2.5.1)
- dellemc.unity (still version 2.0.0)
- fortinet.fortimanager (still version 2.8.2)
- hetzner.hcloud (still version 4.2.2)
- ibm.qradar (still version 4.0.0)
- ibm.spectrum_virtualize (still version 2.0.0)
- ieisystem.inmanage (still version 3.0.0)
- infinidat.infinibox (still version 1.4.5)
- infoblox.nios_modules (still version 1.7.1)
- inspur.ispim (still version 2.2.3)
- junipernetworks.junos (still version 9.1.0)
- kaytus.ksmanage (still version 2.0.0)
- kubevirt.core (still version 2.1.0)
- netapp.cloudmanager (still version 21.24.0)
- netapp.ontap (still version 22.13.0)
- netapp.storagegrid (still version 21.13.0)
- netapp_eseries.santricity (still version 1.4.1)
- netbox.netbox (still version 3.20.0)
- ngine_io.cloudstack (still version 2.5.0)
- ovirt.ovirt (still version 3.2.0)
- purestorage.flasharray (still version 1.32.0)
- sensu.sensu_go (still version 1.14.0)
- splunk.es (still version 4.0.0)
- theforeman.foreman (still version 4.2.0)
- vultr.cloud (still version 1.13.0)
- vyos.vyos (still version 5.0.0)
- wti.remote (still version 1.0.10)

v11.1.0
=======

.. contents::
  :local:
  :depth: 2

Release Summary
---------------

Release Date: 2024-12-03

`Porting Guide <https://docs.ansible.com/ansible/devel/porting_guides.html>`_

Ansible-core
------------

Ansible 11.1.0 contains ansible-core version 2.18.1.
This is a newer version than version 2.18.0 contained in the previous Ansible release.

The changes are reported in the combined changelog below.

Changed Collections
-------------------

If not mentioned explicitly, the changes are reported in the combined changelog below.

+-----------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| Collection                  | Ansible 11.0.0 | Ansible 11.1.0 | Notes                                                                                                                        |
+=============================+================+================+==============================================================================================================================+
| azure.azcollection          | 3.0.0          | 3.1.0          | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+-----------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.dnac                  | 6.22.0         | 6.25.0         |                                                                                                                              |
+-----------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.ise                   | 2.9.5          | 2.9.6          |                                                                                                                              |
+-----------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.dns               | 3.0.7          | 3.1.0          |                                                                                                                              |
+-----------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.docker            | 4.0.1          | 4.1.0          |                                                                                                                              |
+-----------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.general           | 10.0.1         | 10.1.0         |                                                                                                                              |
+-----------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.mysql             | 3.10.3         | 3.11.0         |                                                                                                                              |
+-----------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.postgresql        | 3.7.0          | 3.9.0          |                                                                                                                              |
+-----------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.routeros          | 3.0.0          | 3.1.0          |                                                                                                                              |
+-----------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.vmware            | 5.1.0          | 5.2.0          |                                                                                                                              |
+-----------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.zabbix            | 3.1.2          | 3.2.0          |                                                                                                                              |
+-----------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| cyberark.pas                | 1.0.27         | 1.0.30         | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+-----------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| dellemc.openmanage          | 9.8.0          | 9.9.0          |                                                                                                                              |
+-----------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| fortinet.fortimanager       | 2.7.0          | 2.8.2          |                                                                                                                              |
+-----------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| hetzner.hcloud              | 4.2.1          | 4.2.2          |                                                                                                                              |
+-----------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| infoblox.nios_modules       | 1.7.0          | 1.7.1          |                                                                                                                              |
+-----------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| netapp.ontap                | 22.12.0        | 22.13.0        |                                                                                                                              |
+-----------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| openstack.cloud             | 2.2.0          | 2.3.0          | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+-----------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| purestorage.flasharray      | 1.31.1         | 1.32.0         |                                                                                                                              |
+-----------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| telekom_mms.icinga_director | 2.2.0          | 2.2.1          |                                                                                                                              |
+-----------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| vmware.vmware               | 1.6.0          | 1.7.1          |                                                                                                                              |
+-----------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| vmware.vmware_rest          | 4.2.0          | 4.3.0          |                                                                                                                              |
+-----------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+

Major Changes
-------------

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- omevv_baseline_profile - This module allows to manage baseline profile.
- omevv_baseline_profile_info - This module allows to retrieve baseline profile information.
- omevv_compliance_info - This module allows to retrieve firmware compliance reports.

Minor Changes
-------------

Ansible-core
~~~~~~~~~~~~

- ansible-test - When detection of the current container network fails, a warning is now issued and execution continues. This simplifies usage in cases where the current container cannot be inspected, such as when running in GitHub Codespaces.

cisco.dnac
~~~~~~~~~~

- Added support for bulk operations on multiple access points in accesspoint_workflow_manager
- Aliases were implemented to handle v1 and v2 of the API.
- Bug fixes in inventory_workflow_manager
- Bug fixes in network_settings_workflow_manager
- Bug fixes in sda_fabric_virtual_networks_workflow_manager.py
- Changes in circleci and yaml lint files
- Changes in circleci to run test cases in integration branch
- Changes in sda_extranet_policy_workflow_manager
- Changes in site_workflow_manager
- Enhancements in sda_fabric_devices_workflow_manager.py to support route distribution protocol
- Enhancements in sda_fabric_sites_zones_workflow_manager.py
- Modifications due to documentation errors
- Removing duplicates in the discovery.py module. snmpRwCommunity property.
- accesspoint_workflow_manager - added attribute bulk_update_aps
- sda_fabric_devices_workflow_manager.py - added attribute route_distribution_protocol
- sda_fabric_sites_zones_workflow_manager.py - added attribute site_name_hierarchy and removed attribute site_name

community.dns
~~~~~~~~~~~~~

- all controller code - modernize Python code (https://github.com/ansible-collections/community.dns/pull/231).

community.docker
~~~~~~~~~~~~~~~~

- docker_stack - allow to add ``--detach=false`` option to ``docker stack deploy`` command (https://github.com/ansible-collections/community.docker/pull/987).

community.general
~~~~~~~~~~~~~~~~~

- alternatives - add ``family`` parameter that allows to utilize the ``--family`` option available in RedHat version of update-alternatives (https://github.com/ansible-collections/community.general/issues/5060, https://github.com/ansible-collections/community.general/pull/9096).
- cloudflare_dns - add support for ``comment`` and ``tags`` (https://github.com/ansible-collections/community.general/pull/9132).
- deps module utils - add ``deps.clear()`` to clear out previously declared dependencies (https://github.com/ansible-collections/community.general/pull/9179).
- homebrew - greatly speed up module when multiple packages are passed in the ``name`` option (https://github.com/ansible-collections/community.general/pull/9181).
- homebrew - remove duplicated package name validation (https://github.com/ansible-collections/community.general/pull/9076).
- iso_extract - adds ``password`` parameter that is passed to 7z (https://github.com/ansible-collections/community.general/pull/9159).
- launchd - add ``plist`` option for services such as sshd, where the plist filename doesn't match the service name (https://github.com/ansible-collections/community.general/pull/9102).
- nmcli - add ``sriov`` parameter that enables support for SR-IOV settings (https://github.com/ansible-collections/community.general/pull/9168).
- pipx - add return value ``version`` (https://github.com/ansible-collections/community.general/pull/9180).
- pipx_info - add return value ``version`` (https://github.com/ansible-collections/community.general/pull/9180).
- proxmox_template - add server side artifact fetching support (https://github.com/ansible-collections/community.general/pull/9113).
- redfish_command - add ``update_custom_oem_header``, ``update_custom_oem_params``, and ``update_custom_oem_mime_type`` options (https://github.com/ansible-collections/community.general/pull/9123).
- redfish_utils module utils - remove redundant code (https://github.com/ansible-collections/community.general/pull/9190).
- rpm_ostree_pkg - added the options ``apply_live`` (https://github.com/ansible-collections/community.general/pull/9167).
- rpm_ostree_pkg - added the return value ``needs_reboot`` (https://github.com/ansible-collections/community.general/pull/9167).
- scaleway_lb - minor simplification in the code (https://github.com/ansible-collections/community.general/pull/9189).
- ssh_config - add ``dynamicforward`` option (https://github.com/ansible-collections/community.general/pull/9192).

community.mysql
~~~~~~~~~~~~~~~

- mysql_info - adds the count of tables for each database to the returned values. It is possible to exclude this new field using the ``db_table_count`` exclusion filter. (https://github.com/ansible-collections/community.mysql/pull/691)

community.postgresql
~~~~~~~~~~~~~~~~~~~~

- postgresql_pg_hba - changes ordering of entries that are identical except for the ip-range, but only if the ranges are of the same size, this isn't breaking as ranges of equal size can't overlap (https://github.com/ansible-collections/community.postgresql/pull/772)
- postgresql_pg_hba - orders auth-options alphabetically, this isn't breaking as the order of those options is not relevant to postgresql (https://github.com/ansible-collections/community.postgresql/pull/772)
- postgresql_pg_hba - show the number of the line with the issue if parsing a file fails (https://github.com/ansible-collections/community.postgresql/pull/766)
- postgresql_publication - add possibility of creating publication with column list (https://github.com/ansible-collections/community.postgresql/pull/763).

community.routeros
~~~~~~~~~~~~~~~~~~

- api_info, api_modify - add missing fields ``comment``, ``next-pool`` to ``ip pool`` path (https://github.com/ansible-collections/community.routeros/pull/327).

community.vmware
~~~~~~~~~~~~~~~~

- vmware.py - Add logic for handling the case where the `datacenter` property is not provided.
- vmware_guest_info - `datacenter` property is now optional as it only required in cases where the VM is not uniquely identified by `name`.

fortinet.fortimanager
~~~~~~~~~~~~~~~~~~~~~

- Supported FortiManager 6.2.13, 6.4.15, 7.0.13, 7.2.8, 7.4.5, 7.6.1. Added 1 new module.
- Supported check diff for some modules except "fmgr_generic". You can use "ansible-playbook -i <your-host-file> <your-playbook> --check --diff" to check what changes your playbook will make to the FortiManager.

netapp.ontap
~~~~~~~~~~~~

- all modules supporting only REST - change in documentation for `use_rest`.
- all modules supporting only REST - updated `extends_documentation_fragment` & argument spec.
- na_ontap_active_directory - return error message when attempting to modify `account_name`.
- na_ontap_bgp_config - REST only support for managing BGP configuration for a node, requires ONTAP 9.6 or later.
- na_ontap_cifs_privileges - REST only support for managing privileges of the local or Active Directory user or group, requires ONTAP 9.10.1 or later.
- na_ontap_cifs_server - added new option `comment` for cifs server, requires ONTAP 9.6 or later.
- na_ontap_flexcache - new option to enable `writeback` added in REST, requires ONTAP 9.12 or later.
- na_ontap_rest_info - removed example which has option `gather_subset` set to `all` from documentation.
- na_ontap_rest_info - updated `extends_documentation_fragment` & argument spec.
- na_ontap_s3_buckets - added new option `versioning_state`, requires ONTAP 9.11.1 or later.
- na_ontap_s3_buckets - updated `extends_documentation_fragment` & argument spec.
- na_ontap_s3_services - added `is_http_enabled`, `is_https_enabled`, `port` and `secure_port` option for `s3` service, requires ONTAP 9.8 or later.
- na_ontap_s3_users - new option `regenerate_keys` and `delete_keys` added in REST, `delete_keys` requires ONTAP 9.14 or later.
- na_ontap_svm - added `allowed` option for `s3` service, requires ONTAP 9.7 or later.
- na_ontap_volume - new option `granular_data` added in REST, requires ONTAP 9.12 or later.
- na_ontap_volume - new option `nas_application_template.cifs_share_name` added in REST, requires ONTAP 9.11 or later.
- na_ontap_volume - new option `nas_application_template.snaplock.*` added in REST, requires ONTAP 9.12 or later.
- na_ontap_volume - new option `nas_application_template.snapshot_locking_enabled` added in REST, requires ONTAP 9.13.1 or later.

purestorage.flasharray
~~~~~~~~~~~~~~~~~~~~~~

- purefa_dsrole - Add support for non-system-defined directory service roles with new parameter `name`
- purefa_info - Add ``enabled`` value for network subnets
- purefa_info - Add ``policies` list of dicts to ``filesystem`` subset for each share.
- purefa_info - Add ``time_remaining`` field for non-deleted directory snapshots
- purefa_info - Expose directory service role management access policies if they exist
- purefa_info - Exposed password policy information
- purefa_info - SnaptoNFS support removed from Purity//FA 6.6.0 and higher.
- purefa_info - Update KMIP information collection to use REST v2, exposing full certifcate content
- purefa_offload - Add support for S3 Offload ``uri`` and ``auth_region`` parameters
- purefa_pgsnap - Expose created protection group snapshot data in the module return dict
- purefa_policy - New policy type of ``password`` added. Currently the only default management policy can be updated
- purefa_subnet - Remove default value for MTU t ostop restting to default on enable/disable of subnet. Creation will still default to 1500 if not provided.

vmware.vmware
~~~~~~~~~~~~~

- cluster_info - Migrate cluster_info module from the community.vmware collection to here
- content_library_item_info - Migrate content_library_item_info module from the vmware.vmware_rest collection to here

Deprecated Features
-------------------

- The collection ``ibm.spectrum_virtualize`` was renamed to ``ibm.storage_virtualize``.
  For now both collections are included in Ansible.
  The collection will be completely removed from Ansible 12.
  Please update your FQCNs from ``ibm.spectrum_virtualize`` to ``ibm.storage_virtualize``.

community.general
~~~~~~~~~~~~~~~~~

- opkg - deprecate value ``""`` for parameter ``force`` (https://github.com/ansible-collections/community.general/pull/9172).
- redfish_utils module utils - deprecate method ``RedfishUtils._init_session()`` (https://github.com/ansible-collections/community.general/pull/9190).

vmware.vmware_rest
~~~~~~~~~~~~~~~~~~

- content_library_item_info - the module has been deprecated and will be removed in vmware.vmware_rest 5.0.0

Security Fixes
--------------

Ansible-core
~~~~~~~~~~~~

- Templating will not prefer AnsibleUnsafe when a variable is referenced via hostvars - CVE-2024-11079

Bugfixes
--------

Ansible-core
~~~~~~~~~~~~

- Fix returning 'unreachable' for the overall task result. This prevents false positives when a looped task has unignored unreachable items (https://github.com/ansible/ansible/issues/84019).
- ansible-test - Fix traceback that occurs after an interactive command fails.
- dnf5 - fix installing a package using ``state=latest`` when a binary of the same name as the package is already installed (https://github.com/ansible/ansible/issues/84259)
- dnf5 - matching on a binary can be achieved only by specifying a full path (https://github.com/ansible/ansible/issues/84334)
- runas become - Fix up become logic to still get the SYSTEM token with the most privileges when running as SYSTEM.

cisco.ise
~~~~~~~~~

- network_device - Fix mask validation to handle None values in NetworkDeviceIPList

community.dns
~~~~~~~~~~~~~

- Update Public Suffix List.

community.docker
~~~~~~~~~~~~~~~~

- docker_compose_v2_exec, docker_compose_v2_run - fix missing ``--env`` flag while assembling env arguments (https://github.com/ansible-collections/community.docker/pull/992).
- docker_host_info - ensure that the module always returns ``can_talk_to_docker``, and that it provides the correct value even if ``api_version`` is specified (https://github.com/ansible-collections/community.docker/issues/993, https://github.com/ansible-collections/community.docker/pull/995).

community.general
~~~~~~~~~~~~~~~~~

- dnf_config_manager - fix hanging when prompting to import GPG keys (https://github.com/ansible-collections/community.general/pull/9124, https://github.com/ansible-collections/community.general/issues/8830).
- dnf_config_manager - forces locale to ``C`` before module starts. If the locale was set to non-English, the output of the ``dnf config-manager`` could not be parsed (https://github.com/ansible-collections/community.general/pull/9157, https://github.com/ansible-collections/community.general/issues/9046).
- flatpak - force the locale language to ``C`` when running the flatpak command (https://github.com/ansible-collections/community.general/pull/9187, https://github.com/ansible-collections/community.general/issues/8883).
- gio_mime - fix command line when determining version of ``gio`` (https://github.com/ansible-collections/community.general/pull/9171, https://github.com/ansible-collections/community.general/issues/9158).
- github_key - in check mode, a faulty call to ```datetime.strftime(...)``` was being made which generated an exception (https://github.com/ansible-collections/community.general/issues/9185).
- homebrew_cask - allow ``+`` symbol in Homebrew cask name validation regex (https://github.com/ansible-collections/community.general/pull/9128).
- keycloak_clientscope_type - sort the default and optional clientscope lists to improve the diff (https://github.com/ansible-collections/community.general/pull/9202).
- slack - fail if Slack API response is not OK with error message (https://github.com/ansible-collections/community.general/pull/9198).

community.mysql
~~~~~~~~~~~~~~~

- mysql_user,mysql_role - The sql_mode ANSI_QUOTES affects how the modules mysql_user and mysql_role compare the existing privileges with the configured privileges, as well as decide whether double quotes or backticks should be used in the GRANT statements. Pointing out in issue 671, the modules mysql_user and mysql_role allow users to enable/disable ANSI_QUOTES in session variable (within a DB session, the session variable always overwrites the global one). But due to the issue, the modules do not check for ANSI_MODE in the session variable, instead, they only check in the GLOBAL one.That behavior is not only limiting the users' flexibility, but also not allowing users to explicitly disable ANSI_MODE to work around such bugs like https://bugs.mysql.com/bug.php?id=115953. (https://github.com/ansible-collections/community.mysql/issues/671)

community.postgresql
~~~~~~~~~~~~~~~~~~~~

- postgresql_pg_hba - fixes #420 by properly handling hash-symbols in quotes (https://github.com/ansible-collections/community.postgresql/pull/766)
- postgresql_pg_hba - fixes #705 by preventing invalid strings to be written (https://github.com/ansible-collections/community.postgresql/pull/761)
- postgresql_pg_hba - fixes #730 by extending the key we use to identify a rule with the connection type (https://github.com/ansible-collections/community.postgresql/pull/770)
- postgresql_pg_hba - improves parsing of quoted strings and escaped newlines (https://github.com/ansible-collections/community.postgresql/pull/761)
- postgresql_user - doesn't take password_encryption into account when checking if a password should be updated (https://github.com/ansible-collections/community.postgresql/issues/688).

community.routeros
~~~~~~~~~~~~~~~~~~

- api_info, api_modify - fields ``log`` and ``log-prefix`` in paths ``ip firewall filter``, ``ip firewall mangle``, ``ip firewall nat``, ``ip firewall raw`` now have the correct default values (https://github.com/ansible-collections/community.routeros/pull/324).

community.vmware
~~~~~~~~~~~~~~~~

- vm_device_helper - Fix 'invalid configuration for device' error caused by missing fileoperation parameter. (https://github.com/ansible-collections/community.vmware/pull/2009).
- vmware_guest - Fix errors occuring during hardware version upgrade not being reported. (https://github.com/ansible-collections/community.vmware/pull/2010).
- vmware_guest - Fix vmware_guest always reporting change when using dvswitch. (https://github.com/ansible-collections/community.vmware/pull/2000).
- vmware_guest_tools_upgrade - Account for all possible tools status (https://github.com/ansible-collections/community.vmware/issues/2237).

community.zabbix
~~~~~~~~~~~~~~~~

- zabbix_agent Role - Add Zabbix 7.0 LTS in supported versions for windows.
- zabbix_agent Role - Added ability to set the monitored_by and proxy_group values.
- zabbix_agent Role - Set become parameter explicitly to false for API tasks to run without sudo on the local computer.

fortinet.fortimanager
~~~~~~~~~~~~~~~~~~~~~

- Changed all input argument name in ansible built-in documentation to the underscore format. E.g., changed "var-name" to "var_name".
- Fixed a bug where rc_failed and rc_succeeded did not work.
- Improved code logic, reduced redundant requests for system information.
- Modified built-in document to support sanity tests in ansible-core 2.18.0. No functionality changed.

hetzner.hcloud
~~~~~~~~~~~~~~

- hcloud_load_balancer_service - Improve unknown certificate id or name error.
- hcloud_server - Only rebuild existing servers, skip rebuild if the server was just created.

infoblox.nios_modules
~~~~~~~~~~~~~~~~~~~~~

- For Host IPv6, the mac parameter has been renamed to duid.
- Refined Host record return fields to ensure use_nextserver and nextserver are only included for IPv4, as these fields are not applicable to IPv6.

netapp.ontap
~~~~~~~~~~~~

- all modules supporting REST - avoid duplicate calls to api/cluster to get ONTAP version.
- na_ontap_broadcast_domain - fix issue with port modification in REST.
- na_ontap_flexcache - fix typo error in the query 'origins.cluster.name' in REST.
- na_ontap_rest_info - rectified subset name to `cluster/firmware/history`.
- na_ontap_snapshot_policy - fix issue with 'retention_period' in REST.

purestorage.flasharray
~~~~~~~~~~~~~~~~~~~~~~

- purefa_alert - Fix unreferenced variable error
- purefa_audits - Fix issue when ``start`` parameter not supplied
- purefa_dirsnap - Fixed issues with ``keep_for`` setting and issues related to recovery of deleted snapshots
- purefa_dsrole - Fixed bug in role creation.
- purefa_eradication - Fix incorrect timer settings
- purefa_info - Cater for zero used space in NFS offloads
- purefa_info - ``exports`` dict for each share changed to a list of dicts in ``filesystm`` subset
- purefa_inventory - Fixed quiet failures due to attribute errors
- purefa_network - Allow LACP bonds to be children of a VIF
- purefa_network - Fix compatability issue with ``netaddr>=1.2.0``
- purefa_ntp - Fix issue with deletion of NTP servers
- purefa_offload - Corrected version check logic
- purefa_pod - Allow pd to be deleted with contents if ``delete_contents`` specified
- purefa_sessions - Correctly report sessions with no start or end time
- purefa_smtp - Fixed SMTP deletion issue
- purefa_snmp - Fix issues with deleting SNMP entries
- purefa_snmp_agent - Fix issues with deleting v3 agent
- purefa_volume - Added error message to warn about moving protected volume
- purefa_volume - Errors out when pgroup and add_to_pgs used incorrectly
- purefa_volume - Fixed issue of unable to move volume from pod to vgroup

telekom_mms.icinga_director
~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Add Icinga notification template imports (https://github.com/telekom-mms/ansible-collection-icinga-director/pull/267)

vmware.vmware
~~~~~~~~~~~~~

- content_library_item_info - Library name and ID are ignored if item ID is provided so updated docs and arg parse rules to reflect this

vmware.vmware_rest
~~~~~~~~~~~~~~~~~~

- lookup plugins - Fixed issue where datacenter search filter was never properly set

Known Issues
------------

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- idrac_diagnostics - Issue(285322) - This module doesn't support export of diagnostics file to HTTP and HTTPS share via SOCKS proxy.
- idrac_firmware - Issue(279282) - This module does not support firmware update using HTTP, HTTPS, and FTP shares with authentication on iDRAC8.
- ome_smart_fabric_uplink - Issue(186024) - The module supported by OpenManage Enterprise Modular, however it does not allow the creation of multiple uplinks of the same name. If an uplink is created using the same name as an existing uplink, then the existing uplink is modified.

New Plugins
-----------

Filter
~~~~~~

- community.dns.reverse_pointer - Convert an IP address into a DNS name for reverse lookup.
- community.general.accumulate - Produce a list of accumulated sums of the input list contents.

Lookup
~~~~~~

- community.dns.reverse_lookup - Reverse-look up IP addresses.

New Modules
-----------

community.general
~~~~~~~~~~~~~~~~~

- community.general.decompress - Decompresses compressed files.
- community.general.proxmox_backup - Start a VM backup in Proxmox VE cluster.

community.vmware
~~~~~~~~~~~~~~~~

- community.vmware.vmware_drs_override - Configure DRS behavior for a specific VM in vSphere

fortinet.fortimanager
~~~~~~~~~~~~~~~~~~~~~

- fortinet.fortimanager.fmgr_pkg_videofilter_youtubekey - Configure YouTube API keys.

netapp.ontap
~~~~~~~~~~~~

- netapp.ontap.na_ontap_bgp_config - NetApp ONTAP network BGP configuration
- netapp.ontap.na_ontap_cifs_privileges - NetApp ONTAP CIFS privileges

Unchanged Collections
---------------------

- amazon.aws (still version 9.0.0)
- ansible.netcommon (still version 7.1.0)
- ansible.posix (still version 1.6.2)
- ansible.utils (still version 5.1.2)
- ansible.windows (still version 2.5.0)
- arista.eos (still version 10.0.1)
- awx.awx (still version 24.6.1)
- check_point.mgmt (still version 6.2.1)
- chocolatey.chocolatey (still version 1.5.3)
- cisco.aci (still version 2.10.1)
- cisco.asa (still version 6.0.0)
- cisco.intersight (still version 2.0.20)
- cisco.ios (still version 9.0.3)
- cisco.iosxr (still version 10.2.2)
- cisco.meraki (still version 2.18.3)
- cisco.mso (still version 2.9.0)
- cisco.nxos (still version 9.2.1)
- cisco.ucs (still version 1.14.0)
- cloud.common (still version 4.0.0)
- cloudscale_ch.cloud (still version 2.4.0)
- community.aws (still version 9.0.0)
- community.ciscosmb (still version 1.0.9)
- community.crypto (still version 2.22.3)
- community.digitalocean (still version 1.27.0)
- community.grafana (still version 2.1.0)
- community.hashi_vault (still version 6.2.0)
- community.hrobot (still version 2.0.2)
- community.library_inventory_filtering_v1 (still version 1.0.2)
- community.libvirt (still version 1.3.0)
- community.mongodb (still version 1.7.8)
- community.network (still version 5.1.0)
- community.okd (still version 4.0.0)
- community.proxysql (still version 1.6.0)
- community.rabbitmq (still version 1.3.0)
- community.sap_libs (still version 1.4.2)
- community.sops (still version 2.0.0)
- community.windows (still version 2.3.0)
- containers.podman (still version 1.16.2)
- cyberark.conjur (still version 1.3.1)
- dellemc.enterprise_sonic (still version 2.5.1)
- dellemc.powerflex (still version 2.5.0)
- dellemc.unity (still version 2.0.0)
- f5networks.f5_modules (still version 1.32.1)
- fortinet.fortios (still version 2.3.8)
- google.cloud (still version 1.4.1)
- grafana.grafana (still version 5.6.0)
- ibm.qradar (still version 4.0.0)
- ibm.spectrum_virtualize (still version 2.0.0)
- ibm.storage_virtualize (still version 2.5.0)
- ieisystem.inmanage (still version 3.0.0)
- infinidat.infinibox (still version 1.4.5)
- inspur.ispim (still version 2.2.3)
- junipernetworks.junos (still version 9.1.0)
- kaytus.ksmanage (still version 2.0.0)
- kubernetes.core (still version 5.0.0)
- kubevirt.core (still version 2.1.0)
- lowlydba.sqlserver (still version 2.3.4)
- microsoft.ad (still version 1.7.1)
- netapp.cloudmanager (still version 21.24.0)
- netapp.storagegrid (still version 21.13.0)
- netapp_eseries.santricity (still version 1.4.1)
- netbox.netbox (still version 3.20.0)
- ngine_io.cloudstack (still version 2.5.0)
- ovirt.ovirt (still version 3.2.0)
- purestorage.flashblade (still version 1.19.1)
- sensu.sensu_go (still version 1.14.0)
- splunk.es (still version 4.0.0)
- theforeman.foreman (still version 4.2.0)
- vultr.cloud (still version 1.13.0)
- vyos.vyos (still version 5.0.0)
- wti.remote (still version 1.0.10)

v11.0.0
=======

.. contents::
  :local:
  :depth: 2

Release Summary
---------------

Release Date: 2024-11-19

`Porting Guide <https://docs.ansible.com/ansible/devel/porting_guides.html>`_

Removed Collections
-------------------

- frr.frr (previously included version: 2.0.2)
- inspur.sm (previously included version: 2.3.0)
- ngine_io.exoscale (previously included version: 1.1.0)
- openvswitch.openvswitch (previously included version: 2.1.1)
- t_systems_mms.icinga_director (previously included version: 2.0.1)

You can still install a removed collection manually with ``ansible-galaxy collection install <name-of-collection>``.

Added Collections
-----------------

- ieisystem.inmanage (version 3.0.0)
- kubevirt.core (version 2.1.0)
- vmware.vmware (version 1.6.0)

Ansible-core
------------

Ansible 11.0.0 contains ansible-core version 2.18.0.
This is a newer version than version 2.17.0 contained in the previous Ansible release.

The changes are reported in the combined changelog below.

Included Collections
--------------------

If not mentioned explicitly, the changes are reported in the combined changelog below.

+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Collection                               | Ansible 10.0.0 | Ansible 11.0.0 | Notes                                                                                                                                                                                                           |
+==========================================+================+================+=================================================================================================================================================================================================================+
| amazon.aws                               | 8.0.0          | 9.0.0          |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ansible.netcommon                        | 6.1.2          | 7.1.0          |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ansible.posix                            | 1.5.4          | 1.6.2          |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ansible.utils                            | 4.1.0          | 5.1.2          |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ansible.windows                          | 2.3.0          | 2.5.0          |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| arista.eos                               | 9.0.0          | 10.0.1         |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| awx.awx                                  | 24.3.1         | 24.6.1         | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.                                                                                    |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| azure.azcollection                       | 2.3.0          | 3.0.0          | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.                                                                                    |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| check_point.mgmt                         | 5.2.3          | 6.2.1          |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| chocolatey.chocolatey                    | 1.5.1          | 1.5.3          |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cisco.aci                                | 2.9.0          | 2.10.1         |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cisco.asa                                | 5.0.1          | 6.0.0          |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cisco.dnac                               | 6.13.3         | 6.22.0         |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cisco.intersight                         | 2.0.9          | 2.0.20         | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.                                                                                    |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cisco.ios                                | 8.0.0          | 9.0.3          |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cisco.iosxr                              | 9.0.0          | 10.2.2         |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cisco.ise                                | 2.9.1          | 2.9.5          |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cisco.meraki                             | 2.18.1         | 2.18.3         |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cisco.mso                                | 2.6.0          | 2.9.0          |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cisco.nxos                               | 8.0.0          | 9.2.1          |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cisco.ucs                                | 1.10.0         | 1.14.0         | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.                                                                                    |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cloud.common                             | 3.0.0          | 4.0.0          |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cloudscale_ch.cloud                      | 2.3.1          | 2.4.0          |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.aws                            | 8.0.0          | 9.0.0          |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.crypto                         | 2.20.0         | 2.22.3         |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.digitalocean                   | 1.26.0         | 1.27.0         | There are no changes recorded in the changelog.                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.dns                            | 3.0.0          | 3.0.7          |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.docker                         | 3.10.3         | 4.0.1          |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.general                        | 9.0.1          | 10.0.1         |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.grafana                        | 1.9.1          | 2.1.0          |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.hrobot                         | 2.0.0          | 2.0.2          |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.library_inventory_filtering_v1 | 1.0.1          | 1.0.2          |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.mongodb                        | 1.7.4          | 1.7.8          | There are no changes recorded in the changelog.                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.mysql                          | 3.9.0          | 3.10.3         |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.network                        | 5.0.2          | 5.1.0          |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.okd                            | 3.0.1          | 4.0.0          |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.postgresql                     | 3.4.1          | 3.7.0          |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.proxysql                       | 1.5.1          | 1.6.0          |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.routeros                       | 2.15.0         | 3.0.0          |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.sops                           | 1.6.7          | 2.0.0          |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.vmware                         | 4.4.0          | 5.1.0          |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.windows                        | 2.2.0          | 2.3.0          |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.zabbix                         | 2.4.0          | 3.1.2          |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| containers.podman                        | 1.13.0         | 1.16.2         |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cyberark.conjur                          | 1.2.2          | 1.3.1          | You can find the collection's changelog at `https://github.com/cyberark/ansible-conjur-collection/blob/master/CHANGELOG.md <https://github.com/cyberark/ansible-conjur-collection/blob/master/CHANGELOG.md>`__. |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cyberark.pas                             | 1.0.25         | 1.0.27         | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.                                                                                    |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| dellemc.enterprise_sonic                 | 2.4.0          | 2.5.1          |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| dellemc.openmanage                       | 9.2.0          | 9.8.0          |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| dellemc.powerflex                        | 2.4.0          | 2.5.0          |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| f5networks.f5_modules                    | 1.28.0         | 1.32.1         |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| fortinet.fortimanager                    | 2.5.0          | 2.7.0          |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| fortinet.fortios                         | 2.3.6          | 2.3.8          |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| google.cloud                             | 1.3.0          | 1.4.1          |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| grafana.grafana                          | 5.2.0          | 5.6.0          |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| hetzner.hcloud                           | 3.1.1          | 4.2.1          |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ibm.qradar                               | 3.0.0          | 4.0.0          |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ibm.storage_virtualize                   | 2.3.1          | 2.5.0          |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ieisystem.inmanage                       |                | 3.0.0          | The collection was added to Ansible                                                                                                                                                                             |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| infoblox.nios_modules                    | 1.6.1          | 1.7.0          |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| inspur.ispim                             | 2.2.1          | 2.2.3          |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| junipernetworks.junos                    | 8.0.0          | 9.1.0          |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| kaytus.ksmanage                          | 1.2.1          | 2.0.0          |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| kubernetes.core                          | 3.1.0          | 5.0.0          |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| kubevirt.core                            |                | 2.1.0          | The collection was added to Ansible                                                                                                                                                                             |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| lowlydba.sqlserver                       | 2.3.2          | 2.3.4          |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| microsoft.ad                             | 1.5.0          | 1.7.1          |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| netapp.cloudmanager                      | 21.22.1        | 21.24.0        |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| netapp.ontap                             | 22.11.0        | 22.12.0        |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| netapp.storagegrid                       | 21.12.0        | 21.13.0        | There are no changes recorded in the changelog.                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| netapp_eseries.santricity                | 1.4.0          | 1.4.1          |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| netbox.netbox                            | 3.18.0         | 3.20.0         |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ngine_io.cloudstack                      | 2.3.0          | 2.5.0          |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| purestorage.flasharray                   | 1.28.0         | 1.31.1         |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| purestorage.flashblade                   | 1.17.0         | 1.19.1         |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| splunk.es                                | 3.0.0          | 4.0.0          |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| telekom_mms.icinga_director              | 2.1.2          | 2.2.0          |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| theforeman.foreman                       | 4.0.0          | 4.2.0          |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| vmware.vmware                            |                | 1.6.0          | The collection was added to Ansible                                                                                                                                                                             |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| vmware.vmware_rest                       | 3.0.1          | 4.2.0          |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| vultr.cloud                              | 1.12.1         | 1.13.0         |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| vyos.vyos                                | 4.1.0          | 5.0.0          |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| wti.remote                               | 1.0.5          | 1.0.10         | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.                                                                                    |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Major Changes
-------------

amazon.aws
~~~~~~~~~~

- autoscaling_instance_refresh - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.autoscaling_instance_refresh`` (https://github.com/ansible-collections/amazon.aws/pull/2338).
- autoscaling_instance_refresh_info - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.autoscaling_instance_refresh_info`` (https://github.com/ansible-collections/amazon.aws/pull/2338).
- ec2_launch_template - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.ec2_launch_template`` (https://github.com/ansible-collections/amazon.aws/pull/2348).
- ec2_placement_group - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.ec2_placement_group``.
- ec2_placement_group_info - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.ec2_placement_group_info``.
- ec2_transit_gateway - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.ec2_transit_gateway``.
- ec2_transit_gateway_info - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.ec2_transit_gateway_info``.
- ec2_transit_gateway_vpc_attachment - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.ec2_transit_gateway_vpc_attachment``.
- ec2_transit_gateway_vpc_attachment_info - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.ec2_transit_gateway_vpc_attachment_info``.
- ec2_vpc_egress_igw - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.ec2_vpc_egress_igw`` (https://api.github.com/repos/ansible-collections/amazon.aws/pulls/2327).
- ec2_vpc_nacl - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.ec2_vpc_nacl`` (https://github.com/ansible-collections/amazon.aws/pull/2339).
- ec2_vpc_nacl_info - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.ec2_vpc_nacl_info`` (https://github.com/ansible-collections/amazon.aws/pull/2339).
- ec2_vpc_peer - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.ec2_vpc_peer``.
- ec2_vpc_peering_info - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.ec2_vpc_peering_info``.
- ec2_vpc_vgw - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.ec2_vpc_vgw``.
- ec2_vpc_vgw_info - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.ec2_vpc_vgw_info``.
- ec2_vpc_vpn - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.ec2_vpc_vpn``.
- ec2_vpc_vpn_info - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.ec2_vpc_vpn_info``.
- elb_classic_lb_info - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.elb_classic_lb_info``.

ansible.netcommon
~~~~~~~~~~~~~~~~~

- Bumping `requires_ansible` to `>=2.15.0`, since previous ansible-core versions are EoL now.

ansible.posix
~~~~~~~~~~~~~

- Dropping support for Ansible 2.9, ansible-core 2.15 will be minimum required version for this release

ansible.utils
~~~~~~~~~~~~~

- Bumping `requires_ansible` to `>=2.15.0`, since previous ansible-core versions are EoL now.

arista.eos
~~~~~~~~~~

- Bumping `requires_ansible` to `>=2.15.0` due to the end-of-life status of previous `ansible-core` versions.

check_point.mgmt
~~~~~~~~~~~~~~~~

- New R82 Resource Modules
- Support relative positioning for sections

cisco.asa
~~~~~~~~~

- Bumping `requires_ansible` to `>=2.15.0`, since previous ansible-core versions are EoL now.

cisco.ios
~~~~~~~~~

- Bumping `requires_ansible` to `>=2.15.0`, since previous ansible-core versions are EoL now.

cisco.iosxr
~~~~~~~~~~~

- Bumping `requires_ansible` to `>=2.15.0`, since previous ansible-core versions are EoL now.

cisco.nxos
~~~~~~~~~~

- Bumping `requires_ansible` to `>=2.15.0`, since previous ansible-core versions are EoL now.

community.vmware
~~~~~~~~~~~~~~~~

- vmware_guest_tools_upgrade - Subsitute the deprecated ``guest.toolsStatus`` (https://github.com/ansible-collections/community.vmware/pull/2174).
- vmware_vm_shell - Subsitute the deprecated ``guest.toolsStatus`` (https://github.com/ansible-collections/community.vmware/pull/2174).

community.zabbix
~~~~~~~~~~~~~~~~

- All Roles - Add support for openSUSE Leap 15 and SLES 15.
- All Roles - Separate installation of Zabbix repo from all other roles and link them together.

containers.podman
~~~~~~~~~~~~~~~~~

- Add mount and unmount for volumes
- Add multiple subnets for networks
- Add new options for podman_container
- Add new options to pod module
- Add podman search
- Improve idempotency for networking in podman_container
- Redesign idempotency for Podman Pod module

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- Added support to use session ID for authentication of iDRAC, OpenManage Enterprise and OpenManage Enterprise Modular.
- idrac_secure_boot - This module allows to Configure attributes, import, or export secure boot certificate, and reset keys.
- idrac_secure_boot - This module allows to import the secure boot certificate.
- idrac_server_config_profile - This module is enhanced to allow you to export and import custom defaults on iDRAC.
- idrac_support_assist - This module allows to run and export SupportAssist collection logs on iDRAC.
- idrac_system_erase - This module allows to Erase system and storage components of the server on iDRAC.
- ome_configuration_compliance_baseline - This module is enhanced to schedule the remediation job and stage the reboot.
- ome_session - This module allows you to create and delete the sessions on OpenManage Enterprise and OpenManage Enterprise Modular.
- omevv_firmware_repository_profile - This module allows to manage firmware repository profile.
- omevv_firmware_repository_profile_info - This module allows to retrieve firmware repository profile information.
- omevv_vcenter_info - This module allows to retrieve vCenter information.

fortinet.fortios
~~~~~~~~~~~~~~~~

- Add a sanity_test.yaml file to trigger CI tests in GitHub.
- Improve the logic for SET function to send GET request first then PUT or POST
- Mantis
- Remove Tokens from URLs for Improved Security
- Support Ansible-core 2.17.
- Support new FOS versions 7.4.4.
- Support new FOS versions 7.6.0.

grafana.grafana
~~~~~~~~~~~~~~~

- Add a config check before restarting mimir by @panfantastic in https://github.com/grafana/grafana-ansible-collection/pull/198
- Add support for configuring feature_toggles in grafana role by @LexVar in https://github.com/grafana/grafana-ansible-collection/pull/173
- Adding "distributor" section support to mimir config file by @HamzaKhait in https://github.com/grafana/grafana-ansible-collection/pull/247
- Allow alloy_user_groups variable again by @pjezek in https://github.com/grafana/grafana-ansible-collection/pull/276
- Alloy Role Improvements by @voidquark in https://github.com/grafana/grafana-ansible-collection/pull/281
- Backport post-setup healthcheck from agent to alloy by @v-zhuravlev in https://github.com/grafana/grafana-ansible-collection/pull/213
- Bump ansible-lint from 24.2.3 to 24.5.0 by @dependabot in https://github.com/grafana/grafana-ansible-collection/pull/207
- Bump ansible-lint from 24.5.0 to 24.6.0 by @dependabot in https://github.com/grafana/grafana-ansible-collection/pull/216
- Bump ansible-lint from 24.6.0 to 24.9.2 by @dependabot in https://github.com/grafana/grafana-ansible-collection/pull/270
- Bump braces from 3.0.2 to 3.0.3 in the npm_and_yarn group across 1 directory by @dependabot in https://github.com/grafana/grafana-ansible-collection/pull/218
- Bump pylint from 3.1.0 to 3.1.1 by @dependabot in https://github.com/grafana/grafana-ansible-collection/pull/200
- Bump pylint from 3.1.1 to 3.2.2 by @dependabot in https://github.com/grafana/grafana-ansible-collection/pull/208
- Bump pylint from 3.2.2 to 3.2.3 by @dependabot in https://github.com/grafana/grafana-ansible-collection/pull/217
- Bump pylint from 3.2.3 to 3.2.5 by @dependabot in https://github.com/grafana/grafana-ansible-collection/pull/234
- Bump pylint from 3.2.5 to 3.3.1 by @dependabot in https://github.com/grafana/grafana-ansible-collection/pull/273
- Change from config.river to config.alloy by @cardasac in https://github.com/grafana/grafana-ansible-collection/pull/225
- Ensure check-mode works for otel collector by @pieterlexis-tomtom in https://github.com/grafana/grafana-ansible-collection/pull/264
- Fix Grafana Configuration for Unified and Legacy Alerting Based on Version by @voidquark in https://github.com/grafana/grafana-ansible-collection/pull/215
- Fix message argument of dashboard task by @Nemental in https://github.com/grafana/grafana-ansible-collection/pull/256
- Support adding alloy user to extra groups by @v-zhuravlev in https://github.com/grafana/grafana-ansible-collection/pull/212
- Update Alloy variables to use the `grafana_alloy_` namespace so they are unique by @Aethylred in https://github.com/grafana/grafana-ansible-collection/pull/209
- Update README.md by @aioue in https://github.com/grafana/grafana-ansible-collection/pull/272
- Update README.md by @aioue in https://github.com/grafana/grafana-ansible-collection/pull/275
- Update main.yml by @aioue in https://github.com/grafana/grafana-ansible-collection/pull/274
- Updated result.json['message'] to result.json()['message'] by @CPreun in https://github.com/grafana/grafana-ansible-collection/pull/223
- add grafana_plugins_ops to defaults and docs by @weakcamel in https://github.com/grafana/grafana-ansible-collection/pull/251
- add option to populate google_analytics_4_id value by @copolycube in https://github.com/grafana/grafana-ansible-collection/pull/249
- fix ansible-lint warnings on Forbidden implicit octal value "0640" by @copolycube in https://github.com/grafana/grafana-ansible-collection/pull/279
- fix:mimir molecule should use ansible core 2.16 by @GVengelen in https://github.com/grafana/grafana-ansible-collection/pull/254

ibm.qradar
~~~~~~~~~~

- Bumping `requires_ansible` to `>=2.15.0`, since previous ansible-core versions are EoL now.

junipernetworks.junos
~~~~~~~~~~~~~~~~~~~~~

- Bumping `requires_ansible` to `>=2.15.0`, since previous ansible-core versions are EoL now.

kaytus.ksmanage
~~~~~~~~~~~~~~~

- Add new modules system_lock_mode_info, edit_system_lock_mode(https://github.com/ieisystem/kaytus.ksmanage/pull/27).

splunk.es
~~~~~~~~~

- Bumping `requires_ansible` to `>=2.15.0`, since previous ansible-core versions are EoL now.

vyos.vyos
~~~~~~~~~

- Bumping `requires_ansible` to `>=2.15.0`, since previous ansible-core versions are EoL now.

Minor Changes
-------------

Ansible-core
~~~~~~~~~~~~

- Add ``gid_min``, ``gid_max`` to the group plugin to overwrite the defaults provided by the ``/etc/login.defs`` file (https://github.com/ansible/ansible/pull/81770).
- Add ``python3.13`` to the default ``INTERPRETER_PYTHON_FALLBACK`` list.
- Add ``uid_min``, ``uid_max`` to the user plugin to overwrite the defaults provided by the ``/etc/login.defs`` file (https://github.com/ansible/ansible/pull/81770).
- Add a new meta task ``end_role`` (https://github.com/ansible/ansible/issues/22286)
- Add a new mount_facts module to support gathering information about mounts that are excluded by default fact gathering.
- Introducing COLOR_INCLUDED parameter. This can set a specific color for "included" events.
- Removed the shell ``environment`` config entry as this is already covered by the play/task directives documentation and the value itself is not used in the shell plugins. This should remove any confusion around how people set the environment for a task.
- Suppress cryptography deprecation warnings for Blowfish and TripleDES when the ``paramiko`` Python module is installed.
- The minimum supported Python version on targets is now Python 3.8.
- ``ansible-galaxy collection publish`` - add configuration options for the initial poll interval and the exponential when checking the import status of a collection, since the default is relatively slow.
- ansible-config has new 'validate' option to find mispelled/forgein configurations in ini file or environment variables.
- ansible-doc - show examples in role entrypoint argument specs (https://github.com/ansible/ansible/pull/82671).
- ansible-galaxy - Handle authentication errors and token expiration
- ansible-test - Add Ubuntu 24.04 remote.
- ansible-test - Add support for Python 3.13.
- ansible-test - An ``ansible_core.egg-info`` directory is no longer generated when running tests.
- ansible-test - Connection options can be set for ansible-test managed remote Windows instances.
- ansible-test - Default to Python 3.13 in the ``base`` and ``default`` containers.
- ansible-test - Disable the ``deprecated-`` prefixed ``pylint`` rules as their results vary by Python version.
- ansible-test - Improve container runtime probe error handling. When unexpected probe output is encountered, an error with more useful debugging information is provided.
- ansible-test - Improve the error message shown when an unknown ``--remote`` or ``--docker`` option is given.
- ansible-test - Remove Python 2.7 compatibility imports.
- ansible-test - Removed the ``vyos/1.1.8`` network remote as it is no longer functional.
- ansible-test - Replace Alpine 3.19 container and remote with Alpine 3.20.
- ansible-test - Replace Fedora 39 container and remote with Fedora 40.
- ansible-test - Replace FreeBSD 14.0 remote with FreeBSD 14.1.
- ansible-test - Replace RHEL 9.3 remote with RHEL 9.4.
- ansible-test - Replace Ubuntu 20.04 container with Ubuntu 24.04 container.
- ansible-test - The ``empty-init`` sanity test no longer applies to ``module_utils`` packages.
- ansible-test - Update ``ansible-test-utility-container`` to version 3.1.0.
- ansible-test - Update ``base`` and ``default`` containers to omit Python 3.7.
- ansible-test - Update ``coverage`` to version 7.6.1.
- ansible-test - Update ``http-test-container`` to version 3.0.0.
- ansible-test - Update ``nios-test-container`` to version 5.0.0.
- ansible-test - Update ``pylint`` sanity test to use version 3.3.1.
- ansible-test - Update ``pypi-test-container`` to version 3.2.0.
- ansible-test - Update the ``base`` and ``default`` containers.
- ansible-test - Updated the frozen requirements for all sanity tests.
- ansible-test - Upgrade ``pip`` used in ansible-test managed virtual environments from version 24.0 to 24.2.
- ansible-test - Virtual environments created by ansible-test no longer include the ``wheel`` or ``setuptools`` packages.
- ansible-test - update HTTP test container to 3.2.0 (https://github.com/ansible/ansible/pull/83469).
- ansible.log now also shows log severity field
- distribution.py - Added SL-Micro in Suse OS Family. (https://github.com/ansible/ansible/pull/83541)
- dnf - minor internal changes in how the errors from the dnf API are handled; rely solely on the exceptions rather than inspecting text embedded in them
- dnf - remove legacy code for unsupported dnf versions
- dnf5 - implement ``enable_plugin`` and ``disable_plugin`` options
- fact gathering - Gather /proc/sysinfo facts on s390 Linux on Z
- facts - add systemd version and features
- find - change the datatype of ``elements`` to ``path`` in option ``paths`` (https://github.com/ansible/ansible/pull/83575).
- ini lookup - add new ``interpolation`` option (https://github.com/ansible/ansible/issues/83755)
- isidentifier - remove unwanted Python 2 specific code.
- loop_control - add a break_when option to to break out of a task loop early based on Jinja2 expressions (https://github.com/ansible/ansible/issues/83442).
- package_facts module now supports using aliases for supported package managers, for example managers=yum or managers=dnf will resolve to using the underlying rpm.
- plugins, deprecations and warnings concerning configuration are now displayed to the user, technical issue that prevented 'de-duplication' have been resolved.
- psrp - Remove connection plugin extras vars lookup. This should have no affect on existing users as all options have been documented.
- remove extraneous selinux import (https://github.com/ansible/ansible/issues/83657).
- replace random with secrets library.
- rpm_key - allow validation of gpg key with a subkey fingerprint
- rpm_key - enable gpg validation that requires presence of multiple fingerprints
- service_mgr - add support for dinit service manager (https://github.com/ansible/ansible/pull/83489).
- task timeout now returns timedout key with frame/code that was in execution when the timeout is triggered.
- timedout test for checking if a task result represents a 'timed out' task.
- unarchive - Remove Python 2.7 compatibility imports.
- validate-modules sanity test - detect if names of an option (option name + aliases) do not match between argument spec and documentation (https://github.com/ansible/ansible/issues/83598, https://github.com/ansible/ansible/pull/83599).
- validate-modules sanity test - reject option/aliases names that are identical up to casing but belong to different options (https://github.com/ansible/ansible/pull/83530).
- vaulted_file test filter added, to test if the provided path is an 'Ansible vaulted' file
- yum_repository - add ``excludepkgs`` alias to the ``exclude`` option.

amazon.aws
~~~~~~~~~~

- Add support for transit gateway vpc attachment module (https://github.com/ansible-collections/amazon.aws/pull/2314).
- Bump version of ansible-lint to minimum 24.7.0 (https://github.com/ansible-collections/amazon.aws/pull/2201).
- Move function ``determine_iam_role`` from module ``ec2_instance`` to module_utils/ec2 so that it can be used by ``community.aws.ec2_launch_template`` module (https://github.com/ansible-collections/amazon.aws/pull/2319).
- aws_az_info - refactored code to use ``AnsibleEC2Error`` as well as moving shared code into module_utils.ec2 (https://github.com/ansible-collections/amazon.aws/pull/2163).  - aws_region_info - refactored code to use ``AnsibleEC2Error`` as well as moving shared code into module_utils.ec2 (https://github.com/ansible-collections/amazon.aws/pull/2163).
- backup_vault - Update code to remove unnecessary return values returned as None (https://github.com/ansible-collections/amazon.aws/pull/2105).
- cloudwatch_metric_alarm - add  support for ``evaluate_low_sample_count_percentile`` parameter.
- cloudwatch_metric_alarm - support DatapointsToAlarm config (https://github.com/ansible-collections/amazon.aws/pull/2196).
- cloudwatchlogs_log_group_metric_filter - Add support for ``unit`` and ``dimensions`` options (https://github.com/ansible-collections/amazon.aws/pull/2286)
- ec2_ami - Add support for uefi-preferred boot mode (https://github.com/ansible-collections/amazon.aws/pull/2253).
- ec2_ami - refactored code to use ``AnsibleEC2Error`` as well as moving shared code into module_utils.ec2 (https://github.com/ansible-collections/amazon.aws/pull/2164).
- ec2_ami_info - refactored code to use ``AnsibleEC2Error`` as well as moving shared code into module_utils.ec2 (https://github.com/ansible-collections/amazon.aws/pull/2164).
- ec2_eip - Add support to update reverse DNS record of an EIP (https://github.com/ansible-collections/amazon.aws/pull/2292).
- ec2_eip - refactored code to use ``AnsibleEC2Error`` as well as moving shared code into module_utils.ec2 (https://github.com/ansible-collections/amazon.aws/pull/2165).  - ec2_eip_info - refactored code to use ``AnsibleEC2Error`` as well as moving shared code into module_utils.ec2 (https://github.com/ansible-collections/amazon.aws/pull/2165).
- ec2_eni - refactored code to use ``AnsibleEC2Error`` as well as moving shared code into module_utils.ec2 (https://github.com/ansible-collections/amazon.aws/pull/2166).
- ec2_eni_info - refactored code to use ``AnsibleEC2Error`` as well as moving shared code into module_utils.ec2 (https://github.com/ansible-collections/amazon.aws/pull/2166).
- ec2_import_image - refactored code to use ``AnsibleEC2Error`` as well as moving shared code into module_utils.ec2 (https://github.com/ansible-collections/amazon.aws/pull/2167).
- ec2_import_image_info - refactored code to use ``AnsibleEC2Error`` as well as moving shared code into module_utils.ec2 (https://github.com/ansible-collections/amazon.aws/pull/2167).
- ec2_instance - Add support for ``network_interfaces`` and ``network_interfaces_ids`` options replacing deprecated option ``network`` (https://github.com/ansible-collections/amazon.aws/pull/2123).
- ec2_instance - Pass variables ``client`` and ``module`` as function arguments instead of global variables (https://github.com/ansible-collections/amazon.aws/pull/2192).
- ec2_instance - ``network.source_dest_check`` option has been deprecated and replaced by new option ``source_dest_check`` (https://github.com/ansible-collections/amazon.aws/pull/2123).
- ec2_instance - add the possibility to create instance with multiple network interfaces (https://github.com/ansible-collections/amazon.aws/pull/2123).
- ec2_instance - add the possibility to upgrade / downgrade existing ec2 instance type (https://github.com/ansible-collections/amazon.aws/issues/469).
- ec2_instance - refactored code to use ``AnsibleEC2Error`` and shared code from module_utils.ec2 (https://github.com/ansible-collections/amazon.aws/pull/2192).
- ec2_instance_info - Replaced call to deprecated function ``datetime.utcnow()`` by ``datetime.now(timezone.utc)`` (https://github.com/ansible-collections/amazon.aws/pull/2192).
- ec2_instance_info - refactored code to use ``AnsibleEC2Error`` and shared code from module_utils.ec2 (https://github.com/ansible-collections/amazon.aws/pull/2192).
- ec2_key - refactored code to use ``AnsibleEC2Error`` as well as moving shared code into module_utils.ec2 (https://github.com/ansible-collections/amazon.aws/pull/2168).
- ec2_key_info - refactored code to use ``AnsibleEC2Error`` as well as moving shared code into module_utils.ec2 (https://github.com/ansible-collections/amazon.aws/pull/2168).
- ec2_metadata_facts - Add parameter ``metadata_token_ttl_seconds`` (https://github.com/ansible-collections/amazon.aws/pull/2209).
- ec2_security_group - refactored code to use ``AnsibleEC2Error`` as well as moving shared code into module_utils.ec2 (https://github.com/ansible-collections/amazon.aws/pull/2169).
- ec2_security_group_info - refactored code to use ``AnsibleEC2Error`` as well as moving shared code into module_utils.ec2 (https://github.com/ansible-collections/amazon.aws/pull/2169).
- ec2_snapshot - refactored code to use ``AnsibleEC2Error`` as well as moving shared code into module_utils.ec2 (https://github.com/ansible-collections/amazon.aws/pull/2099).
- ec2_snapshot_info - refactored code to use ``AnsibleEC2Error`` as well as moving shared code into module_utils.ec2 (https://github.com/ansible-collections/amazon.aws/pull/2099).
- ec2_spot_instance - refactored code to use ``AnsibleEC2Error`` as well as moving shared code into module_utils.ec2 (https://github.com/ansible-collections/amazon.aws/pull/2099).
- ec2_spot_instance_info - refactored code to use ``AnsibleEC2Error`` as well as moving shared code into module_utils.ec2 (https://github.com/ansible-collections/amazon.aws/pull/2099).
- ec2_vol - refactored code to use ``AnsibleEC2Error`` as well as moving shared code into module_utils.ec2 (https://github.com/ansible-collections/amazon.aws/pull/2170).
- ec2_vol_info - refactored code to use ``AnsibleEC2Error`` as well as moving shared code into module_utils.ec2 (https://github.com/ansible-collections/amazon.aws/pull/2170).
- ec2_vpc_dhcp_option - refactored code to use ``AnsibleEC2Error`` as well as moving shared code into module_utils.ec2 (https://github.com/ansible-collections/amazon.aws/pull/2097).
- ec2_vpc_dhcp_option_info - refactored code to use ``AnsibleEC2Error`` as well as moving shared code into module_utils.ec2 (https://github.com/ansible-collections/amazon.aws/pull/2097).
- ec2_vpc_endpoint - refactored code to use ``AnsibleEC2Error`` as well as moving shared code into module_utils.ec2 (https://github.com/ansible-collections/amazon.aws/pull/2097).
- ec2_vpc_endpoint_info - refactored code to use ``AnsibleEC2Error`` as well as moving shared code into module_utils.ec2 (https://github.com/ansible-collections/amazon.aws/pull/2097).
- ec2_vpc_endpoint_service_info - refactored code to use ``AnsibleEC2Error`` as well as moving shared code into module_utils.ec2 (https://github.com/ansible-collections/amazon.aws/pull/2097).
- ec2_vpc_igw - refactored code to use ``AnsibleEC2Error`` as well as moving shared code into module_utils.ec2 (https://github.com/ansible-collections/amazon.aws/pull/2099).
- ec2_vpc_igw_info - refactored code to use ``AnsibleEC2Error`` as well as moving shared code into module_utils.ec2 (https://github.com/ansible-collections/amazon.aws/pull/2099).
- ec2_vpc_nat_gateway - refactored code to use ``AnsibleEC2Error`` as well as moving shared code into module_utils.ec2 (https://github.com/ansible-collections/amazon.aws/pull/2099).
- ec2_vpc_nat_gateway_info - refactored code to use ``AnsibleEC2Error`` as well as moving shared code into module_utils.ec2 (https://github.com/ansible-collections/amazon.aws/pull/2099).
- ec2_vpc_net - refactored code to use ``AnsibleEC2Error`` as well as moving shared code into module_utils.ec2 (https://github.com/ansible-collections/amazon.aws/pull/2158).
- ec2_vpc_net_info - refactored code to use ``AnsibleEC2Error`` as well as moving shared code into module_utils.ec2 (https://github.com/ansible-collections/amazon.aws/pull/2158).
- ec2_vpc_route_table - refactored code to use ``AnsibleEC2Error`` as well as moving shared code into module_utils.ec2 (https://github.com/ansible-collections/amazon.aws/pull/2159).
- ec2_vpc_route_table - update the ec2_vpc_route_table routes parameter to support the transit gateway id (https://github.com/ansible-collections/amazon.aws/pull/2291).
- ec2_vpc_route_table_info - refactored code to use ``AnsibleEC2Error`` as well as moving shared code into module_utils.ec2 (https://github.com/ansible-collections/amazon.aws/pull/2159).
- ec2_vpc_subnet - refactored code to use ``AnsibleEC2Error`` as well as moving shared code into module_utils.ec2 (https://github.com/ansible-collections/amazon.aws/pull/2160).
- ec2_vpc_subnet_info - refactored code to use ``AnsibleEC2Error`` as well as moving shared code into module_utils.ec2 (https://github.com/ansible-collections/amazon.aws/pull/2160).
- module_utils.botocore - replace use of ``botocore.Session`` with ``boto3.Session`` for consistency (https://github.com/ansible-collections/amazon.aws/pull/2157).
- module_utils.botocore - the ``boto3_conn`` method now catches ``BotoCoreError`` rather than an incomplete list of subclasses (https://github.com/ansible-collections/amazon.aws/pull/2157).
- module_utils/autoscaling - create utils to handle AWS call for the ``autoscaling`` client (https://github.com/ansible-collections/amazon.aws/pull/2301).
- module_utils/ec2 - add some shared code for Launch template AWS API calls (https://github.com/ansible-collections/amazon.aws/pull/2319).
- module_utils/ec2 - add utils for the ec2_placement_group* modules (https://github.com/ansible-collections/amazon.aws/pull/2322).
- module_utils/ec2 - add utils for the ec2_transit_gateway_* modules (https://github.com/ansible-collections/amazon.aws/pull/2325).
- module_utils/ec2 - add utils for the ec2_vpc_peer* modules (https://github.com/ansible-collections/amazon.aws/pull/2303).
- module_utils/ec2 - add utils for the ec2_vpc_vgw_* modules (https://github.com/ansible-collections/amazon.aws/pull/2331).
- module_utils/ec2 - add utils for the ec2_vpc_vpn* modules (https://github.com/ansible-collections/amazon.aws/pull/2312).
- module_utils/ec2 - move shared code for ec2 client (https://github.com/ansible-collections/amazon.aws/pull/2302).
- module_utils/elbv2 - Refactor listeners and rules comparison logic (https://github.com/ansible-collections/amazon.aws/issues/1981).
- module_utils/rds.py - Add shared functionality from rds snapshot modules (https://github.com/ansible-collections/amazon.aws/pull/2138).
- module_utils/rds.py - Refactor shared boto3 client functionality, add type hinting and function docstrings (https://github.com/ansible-collections/amazon.aws/pull/2119).
- plugin_utils.botocore - the ``boto3_conn`` method now catches ``BotoCoreError`` rather than an incomplete list of subclasses (https://github.com/ansible-collections/amazon.aws/pull/2157).
- rds_cluster - Add support for I/O-Optimized storage configuration for aurora clusters (https://github.com/ansible-collections/amazon.aws/pull/2063).
- rds_cluster_snapshot - Refactor shared boto3 client functionality, add type hinting and function docstrings (https://github.com/ansible-collections/amazon.aws/pull/2138).
- rds_instance - Add support for  Multi-Tenant CDB Databases(https://github.com/ansible-collections/amazon.aws/pull/2275).
- rds_instance - Refactor shared boto3 client functionality, add type hinting and function docstrings (https://github.com/ansible-collections/amazon.aws/pull/2119).
- rds_instance - Remove shared functioanlity added to module_utils/rds.py (https://github.com/ansible-collections/amazon.aws/pull/2138).
- rds_instance - snake case for parameter ``performance_insights_kms_key_id`` was incorrect according to boto documentation (https://github.com/ansible-collections/amazon.aws/pull/2163).
- rds_instance_info - Refactor shared boto3 client functionality, add type hinting and function docstrings (https://github.com/ansible-collections/amazon.aws/pull/2119).
- rds_instance_info - Refactor shared boto3 client functionality, add type hinting and function docstrings (https://github.com/ansible-collections/amazon.aws/pull/2138).
- rds_instance_snapshot - Refactor shared boto3 client functionality, add type hinting and function docstrings (https://github.com/ansible-collections/amazon.aws/pull/2138).
- rds_snapshot_info - Refactor shared boto3 client functionality, add type hinting and function docstrings (https://github.com/ansible-collections/amazon.aws/pull/2138).
- s3_bucket - Add ``object_lock_default_retention`` to set Object Lock default retention configuration for S3 buckets (https://github.com/ansible-collections/amazon.aws/pull/2062).
- s3_bucket - Add support for bucket inventories (https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-inventory.html)
- s3_bucket - Add support for enabling Amazon S3 Transfer Acceleration by setting the ``accelerate_enabled`` option (https://github.com/ansible-collections/amazon.aws/pull/2046).
- s3_object - Add support for ``expected_bucket_owner`` option (https://github.com/ansible-collections/amazon.aws/issues/2114).
- s3_object_info - Added support for ``max_keys`` and ``marker`` parameter (https://github.com/ansible-collections/amazon.aws/pull/2328).
- ssm parameter lookup - add new option ``droppath`` to drop the hierarchical search path from ssm parameter lookup results (https://github.com/ansible-collections/amazon.aws/pull/1756).

ansible.netcommon
~~~~~~~~~~~~~~~~~

- ansible.netcommon.persistent - Connection local is marked deprecated and all dependent collections are advised to move to a proper connection plugin, complete support of connection local will be removed in a release after 01-01-2027.

ansible.posix
~~~~~~~~~~~~~

- Add summary_only parameter to profile_roles and profile_tasks callbacks.
- firewalld - add functionality to set forwarding (https://github.com/ansible-collections/ansible.posix/pull/548).
- firewalld - added offline flag implementation (https://github.com/ansible-collections/ansible.posix/pull/484)
- firewalld - respawn module to use the system python interpreter when the ``firewall`` python module is not available for ``ansible_python_interpreter`` (https://github.com/ansible-collections/ansible.posix/pull/460).
- firewalld_info - Only warn about ignored zones, when there are zones ignored.
- firewalld_info - respawn module to use the system python interpreter when the ``firewall`` python module is not available for ``ansible_python_interpreter`` (https://github.com/ansible-collections/ansible.posix/pull/460).
- mount - add no_log option for opts parameter (https://github.com/ansible-collections/ansible.posix/pull/563).
- seboolean - respawn module to use the system python interpreter when the ``selinux`` python module is not available for ``ansible_python_interpreter`` (https://github.com/ansible-collections/ansible.posix/pull/460).
- selinux - respawn module to use the system python interpreter when the ``selinux`` python module is not available for ``ansible_python_interpreter`` (https://github.com/ansible-collections/ansible.posix/pull/460).

ansible.utils
~~~~~~~~~~~~~

- Allows the cli_parse module to find parser.template_path inside roles or collections when a path relative to the role/collection directory is provided.
- Fix cli_parse module to require a connection.
- Previously, the ansible.utils.ipcut filter only supported IPv6 addresses, leading to confusing error messages when used with IPv4 addresses. This fix ensures that the filter now appropriately handles both IPv4 and IPv6 addresses.
- Removed conditional check for deprecated ansible.netcommon.cli_parse from ansible.utils.cli_parse
- The from_xml filter returns a python dictionary instead of a json string.

ansible.windows
~~~~~~~~~~~~~~~

- Set minimum supported Ansible version to 2.15 to align with the versions still supported by Ansible.
- owner - Migrated to ``Ansible.Basic`` format to add basic checks like invocation args checking
- win_powershell - Added the ``sensitive_parameters`` option that can be used to pass in a SecureString or PSCredential parameter value.
- win_powershell - Changed `sensitive_parameters` to use `New-Object`, rather than `::new()`
- win_setup - Added the ``ansible_win_rm_certificate_thumbprint`` fact to display the thumbprint of the certificate in use
- win_user - Added the ability to set an account expiration date using the ``account_expires`` option - https://github.com/ansible-collections/ansible.windows/issues/610

chocolatey.chocolatey
~~~~~~~~~~~~~~~~~~~~~

- Remove support for End of Life ansible-core 2.13, 2.14

cisco.aci
~~~~~~~~~

- Add aci_esg_to_contract module for esg contract relationship objects fvRsCons (consumer), fvRsConsIf (consumer interface), fvRsProv (provider) and fvRsIntraEpg (intra_esg)
- Add aci_system_connectivity_preference module (#601)
- Added suppress-previous flag option to reduce the number of API calls. (#636)
- Enable relative path and/or filename of private key for the aci httpapi plugin.

cisco.dnac
~~~~~~~~~~

- Added 'accesspoint_workflow_manager' module to manage access point configurations.
- Added 'fabric_sites_zones_workflow_manager.py' to manage fabric sites/zones and update the authentication profile template.
- Added 'fabric_transits_workflow_manager.py' to perform operations on SDA fabric transits.
- Added 'lan_automation_workflow_manager' to automate network discovery, deployment, and device configuration with LAN Automation.
- Added 'rma_workflow_manager' module to manage RMA workflow.
- Added 'sda_extranet_policies_workflow_manager' to manage SDA Extranet Policies.
- Added 'sda_extranet_policies_workflow_manager' to provide SDA Extranet Policies for managing SDA Extranet Policy.
- Added 'sda_fabric_devices_workflow_manager' to manage SDA fabric devices.
- Added 'sda_fabric_virtual_networks_workflow_manager' to configure fabric VLANs, Virtual Networks, and Anycast Gateways.
- Added 'sda_host_port_onboarding_workflow_manager' to manage host port onboarding in SD-Access Fabric.
- Added 'user_role_workflow_manager' module to manage operations to create, update, and delete users and roles.
- Added API to validate the server address
- Added Circle CI support for integration testing.
- Added detailed documentation in network_settings_workflow_manager.py
- Added example playbooks in device_provision_workflow.yml
- Added example playbooks in network_compliance_workflow_manager.py
- Added new attribute 'ise_integration_wait_time' in ise_radius_integration_workflow_manager.py
- Added the code for creating/updating/deleting events subscription notification with specified destination and added the playbook and documentation with examples
- Adding  support to update  password  in user_role_workflow_manager module.
- Adding pyzipper support in device_configs workflow manager module.
- Adding run_compliance_batch_size support in network_compliance module.
- Ansible utils requirement updated.
- Bug fixes in accesspoint_workflow_manager module
- Bug fixes in network_settings_workflow_manager module
- Bug fixes in pnp_workflow_manager module
- Bug fixes in user_role_workflow_manager module.
- Changes in accesspoint_workflow_manager module.
- Changes in device_configs_backup_workflow_manager module
- Changes in device_configs_backup_workflow_manager to support name of the site to which the device is assigned.
- Changes in device_credential_workflow_manager module.
- Changes in dnac.py
- Changes in dnac.py to support common APIs
- Changes in events_and_notifications_workflow_manager module.
- Changes in inventory and swim workflow manager modules.
- Changes in inventory_workflow_manager module.
- Changes in inventory_workflow_manager to support maximum devices to resync, and resync timeout.
- Changes in ise_radius_integration_workflow_manager module to check ise certification status.
- Changes in ise_radius_integration_workflow_manager module.
- Changes in network_compliance_workflow_manager module.
- Changes in network_settings_workflow_manager module to support exception handling.
- Changes in network_settings_workflow_manager to support reserve ip subpools.
- Changes in provision workflow manager module.
- Changes in provision_workflow_manager to support enhanced log messages.
- Changes in rma_workflow_manager module to support pre check for device replacement.
- Changes in rma_workflow_manager module.
- Changes in sda_extranet_policies_workflow_manager module.
- Changes in sda_fabric_transits_workflow_manager module.
- Changes in swim_workflow_manager module to support CCO image.
- Changes in user_role_workflow_manager module.
- Checking SNMP versions in events_and_notifications_workflow_manager.py module
- Checking the device list in swim workflow manager module.
- Code change in template_workflow_manager module
- Code change in user_role_manager module
- Code changes in network_compliance_workflow_manager module
- Code changes in rma_workflow_manager module
- Code changes in sda_fabric_devices_workflow_manager module
- Code changes in sda_fabric_sites_zones_workflow_manager module
- Code changes in sda_fabric_virtual_networks_workflow_manager module
- Code changes in sda_host_port_onboarding_workflow_manager module
- Code changes in site_workflow_manager module
- Code changes in swim_workflow_manager module
- Code enhancements in device_credential_workflow_manager module
- Enhancements in ise_radius_integration_workflow_manager module
- Enhancements in network_settings_workflow_manager module.
- Enhancements in swim_workflow_manager module.
- Exporting export_device_details_limit in inventory workflow module.
- Fix family name from userand_roles to user_and_roles.
- Fix module name from network_device_config__info to configuration_archive_details_info.
- Minor bug fixes in device_credential_workflow_manager.py module
- Minor bug fixes in network_compliance_workflow_manager module.
- Removed sda_extranet_policies_workflow_manager.py module.
- Removing git release workflows.
- Setting dnac versions and compare for version based routing.
- UT and IT cases for worflow manager modules.
- Unit test automation for worflow_manager modules.
- access_point_workflow_manager module.py - added attributes 'hostname' and 'management_ip_address'
- accesspoint_workflow_manager.py - added attribute 'factory_reset_aps'.
- accesspoint_workflow_manager.py - added attribute 'reboot_aps'.
- accesspoint_workflow_manager.py - added attributes 'is_assigned_site_as_location', and other new attributes.
- application_policy_application_set - new module
- application_policy_application_set_count_info - new module
- application_policy_application_set_info - new module
- applications_count_v2_info - new module
- applications_v2 - new module
- applications_v2_info - new module
- auth_token_create - new module
- authentication_policy_servers - new module
- device_configs_backup_workflow_manager - New workflow manager module for device configuration backup functions.
- device_configs_backup_workflow_manager.py - added attributes 'hostname_list' and 'ip_address_list', 'site_list', 'mac_address_list', 'serial_number_list'
- device_configs_backup_workflow_manager.py - removed attributes 'hostname', 'ip_address', 'site', 'mac_address' and 'serial_number'
- device_configs_backup_workflow_manager.py. added attribute 'site'.
- device_credential_workflow_manager - Updated the log messages.
- device_credential_workflow_manager.py - added attribute 'apply_credentials_to_site'.
- device_reboot_apreboot - new module
- discovery_intent.py - Changed attribute name 'desc' to 'description'.
- discovery_workflow_manager.py - Changed attribute name 'desc' to 'description'.
- dna_event_snmp_config_info - new module
- event_snmp_config - new module
- event_webhook_read_info - new module
- events_and_notifications_worflow_manager.py - Changed attribute names from 'from_email', 'to_email', 'to send_email' and 'recipient_email'.
- events_and_notifications_workflow_manager - New workflow manager for configuring various types of destinations(Webhook, Email, Syslog, SNMP, ITSM) to deliver event notifications.
- events_and_notifications_workflow_manager.py - Added attributes 'webhook_event_notification', 'email_event_notification', 'syslog_event_notification'
- fabric_sites_zones_workflow_manager.py - added attribute 'fabric_type'.
- fabric_sites_zones_workflow_manager.py - removed attribute 'site_type'.
- flexible_report_content_info - new module
- flexible_report_execute - new module
- flexible_report_executions_info - new module
- flexible_report_schedule  - new module
- flexible_report_schedule_info - new module
- integration_settings_itsm_instances_info - new module
- integration_settings_status_info - new module
- inventory_intent.py - added attribute 'export_device_details_limit'.
- inventory_workflow_manager - Updated changes related to provisioning devices.
- inventory_workflow_manager.py - Removed attribute hostname_list, serial_number_list and mac_address_list
- inventory_workflow_manager.py - added attribute 'export_device_details_limit'.
- inventory_workflow_manager.py - added attribute hostnames, serial_numbers and mac_addresses
- inventory_workflow_manager.py - added attributes resync_device_count and resync_max_timeout
- ise_integration_status_info - new module
- ise_radius_integration_workflow_manager - New workflow manager for Authentication and Policy Servers(ISE/AAA).
- ise_radius_integration_workflow_manager - Removed the attributes 'port' and 'subscriber_name'. Added the attribute 'ise_integration_wait_time'.
- ise_radius_integration_workflow_manager.py - changed the type of 'authentication_policy_server' from 'dict' to 'list'.
- lan_automation_sessions_info - new module
- lan_automation_update - new module
- lan_automation_update_device - new module
- lan_automation_update_v2 - new module
- lan_automation_v2 - new module
- network_compliance_workflow_manager - New workflow manager for Network Compliance module for managing network compliance tasks on reachable device(s).
- network_compliance_workflow_manager.py - added attribute 'run_compliance_batch_size'.
- network_device_user_defined_field_delete - new module
- network_settings_workflow_manager - Added attributes 'ipv4_global_pool_name'.
- network_settings_workflow_manager.py - added attributes 'wired_data_collection', 'wireless_telemetry', and 'netflow_collector'.
- network_settings_workflow_manager.py - changed the type of network_management_details from 'dic' to 'list'.
- provision_workflow_manager - Updated changes related to handle errors.
- provision_workflow_manager.py - Added attribute 'provisioning'
- provision_workflow_manager.py - added attribute 'force_provisioning'.
- site_workflow_manager - Updated changes in Site updation.
- swim_workflow_manager.py - added attribute 'cco_image_details'.
- template_workflow_manager - Removed attributes 'create_time', 'failure_policy', 'last_update_time', 'latest_version_time', 'parent_template_id', 'project_id', 'validation_errors', 'rollback_template_params' and 'rollback_template_content'.
- template_workflow_manager.py - Added attributes 'choices', 'failure_policy'
- template_workflow_manager.py - added project_file and payload.
- user_role_workflow_manager - added attribute 'password_update'.
- users_external_authentication - new module
- users_external_servers_aaa_attribute - new module

cisco.ios
~~~~~~~~~

- Add ios_vrf_global resource module in favor of ios_vrf module (fixes - https://github.com/ansible-collections/cisco.ios/pull/1055)

cisco.iosxr
~~~~~~~~~~~

- Added iosxr_route_maps resource module, that helps with configuration of route-policy.
- Adds a new module `iosxr_vrf_address_family` to manage VRFs address families on Cisco IOS-XR devices (https://github.com/ansible-collections/cisco.iosxr/pull/489).
- Adds a new module `iosxr_vrf_global` to manage VRF global configurations on Cisco IOS-XR devices (https://github.com/ansible-collections/cisco.iosxr/pull/467).

cisco.meraki
~~~~~~~~~~~~

- Include networks_appliance_traffic_shaping_custom_performance_classes_info plugin.

cisco.mso
~~~~~~~~~

- Add module mso_schema_template_vrf_rp to support multicast vrf rp in application templates
- Add module ndo_dhcp_option_policy to support dhcp option policy configuration in tenant templates
- Add module ndo_dhcp_relay_policy to support dhcp relay policy configuration in tenant templates
- Add module ndo_l3_domain and ndo_physical_domain to support domain configuration in fabric policy templates
- Add module ndo_vlan_pool to support vlan pool configuration in fabric policy templates
- Add new module ndo_schema_template_bd_dhcp_policy to support BD DHCP Policy configuration in NDO version 4.1 and later
- Add site_aware_policy_enforcement and bd_enforcement_status arguments to the mso_schema_template_vrf module
- Add support for multicast route map filters in mso_schema_template_bd
- Add support to use an APIC DN as VRF reference in mso_schema_site_bd_l3out
- Added module ndo_route_map_policy_multicast to support multicast route map policies configuration in tenant templates
- Added module ndo_template to support creation of tenant, l3out, fabric_policy, fabric_resource, monitoring_tenant, monitoring_access and service_device templates

cisco.nxos
~~~~~~~~~~

- Add nxos_vrf_global resource module in favor of nxos_vrf module (https://github.com/ansible-collections/cisco.nxos/pull/870).
- nxos_bgp_global - Deprecate local_as with local_as_config which supports more configuration attributes, under neighbor.
- route_maps - support simple route-maps that do not contain set or match statements. it allows for the creation and management of purely basic route-map entries like 'route-map test-1 permit 10'.

cloudscale_ch.cloud
~~~~~~~~~~~~~~~~~~~

- Update source_format of custom images with actually available choices.

community.aws
~~~~~~~~~~~~~

- autoscaling_instance_refresh - Add support for ``skip_matching`` and ``max_healthy_percentage`` in ``preference`` (https://github.com/ansible-collections/community.aws/pull/2150).
- autoscaling_instance_refresh - refactor module to use shared code from ``ansible_collections.amazon.aws.plugins.module_utils.autoscaling`` and add type hinting (https://github.com/ansible-collections/community.aws/pull/2150).
- autoscaling_instance_refresh_info - refactor module to use shared code from ``ansible_collections.amazon.aws.plugins.module_utils.autoscaling`` and add type hinting (https://github.com/ansible-collections/community.aws/pull/2150).
- ec2_launch_template - Add option ``tag_specifications`` to define tags to be applied to the resources created with the launch template (https://github.com/ansible-collections/community.aws/issues/176).
- ec2_launch_template - Add suboption ``throughput`` to ``block_device_mappings`` argument (https://github.com/ansible-collections/community.aws/issues/1944).
- ec2_launch_template - Add support ``purge_tags`` parameter (https://github.com/ansible-collections/community.aws/issues/176).
- ec2_launch_template - Add the possibility to delete specific versions of a launch template using ``versions_to_delete`` (https://github.com/ansible-collections/community.aws/pull/2164).
- ec2_launch_template - Refactor module to use shared code from ``amazon.aws.plugins.module_utils.ec2`` and update ``RETURN`` block (https://github.com/ansible-collections/community.aws/pull/2164).
- ec2_placement_group - Added support for creating with ``tags`` (https://github.com/ansible-collections/community.aws/pull/2081).
- ec2_placement_group - Refactor module to use shared code from ``amazon.aws.plugins.module_utils.ec2`` and update ``RETURN`` block (https://github.com/ansible-collections/community.aws/pull/2167).
- ec2_transit_gateway - Refactor module to use shared code from ``amazon.aws.plugins.module_utils.ec2`` and update ``RETURN`` block (https://github.com/ansible-collections/community.aws/pull/2158).
- ec2_transit_gateway - Support for enable multicast on Transit Gateway (https://github.com/ansible-collections/community.aws/pull/2063).
- ec2_transit_gateway - Support for enabling multicast on Transit Gateway (https://github.com/ansible-collections/community.aws/pull/2063).
- ec2_transit_gateway_info - Refactor module to use shared code from ``amazon.aws.plugins.module_utils.ec2`` and update ``RETURN`` block (https://github.com/ansible-collections/community.aws/pull/2158).
- ec2_transit_gateway_vpc_attachment - Modify doumentation and refactor to adhere to coding guidelines (https://github.com/ansible-collections/community.aws/pull/2157).
- ec2_vpc_egress_igw - Add the possibility to update/add tags on Egress only internet gateway (https://github.com/ansible-collections/community.aws/pull/2152).
- ec2_vpc_egress_igw - Refactor module to use shared code from ``amazon.aws.plugins.module_utils.ec2`` util (https://github.com/ansible-collections/community.aws/pull/2152).
- ec2_vpc_nacl - Refactor module to use shared code from `amazon.aws.plugins.module_utils.ec2` (https://github.com/ansible-collections/community.aws/pull/2159).
- ec2_vpc_nacl_info - Refactor module to use shared code from `amazon.aws.plugins.module_utils.ec2` (https://github.com/ansible-collections/community.aws/pull/2159).
- ec2_vpc_peer - Refactor module to use shared code from ``amazon.aws.plugins.module_utils.ec2`` (https://github.com/ansible-collections/community.aws/pull/2153).
- ec2_vpc_peering_info - Refactor module to use shared code from ``amazon.aws.plugins.module_utils.ec2`` (https://github.com/ansible-collections/community.aws/pull/2153).
- ec2_vpc_vgw - Fix call to parent static method in class ``VGWRetry`` (https://github.com/ansible-collections/community.aws/pull/2140).
- ec2_vpc_vgw - Refactor module to use shared code from ``amazon.aws.plugins.module_utils.ec2`` and update ``RETURN`` block (https://github.com/ansible-collections/community.aws/pull/2171).
- ec2_vpc_vgw_info - Refactor module to use shared code from ``amazon.aws.plugins.module_utils.ec2`` and update ``RETURN`` block (https://github.com/ansible-collections/community.aws/pull/2171).
- ec2_vpc_vpn - Refactor module to use shared code from ``amazon.aws.plugins.module_utils.ec2`` (https://github.com/ansible-collections/community.aws/pull/2160).
- ec2_vpc_vpn_info - Refactor module to use shared code from ``amazon.aws.plugins.module_utils.ec2`` (https://github.com/ansible-collections/community.aws/pull/2160).
- elb_classic_lb_info - Refactor elb_classic_lb_info module (https://github.com/ansible-collections/community.aws/pull/2139).

community.crypto
~~~~~~~~~~~~~~~~

- certificate_complete_chain - add ability to identify Ed25519 and Ed448 complete chains (https://github.com/ansible-collections/community.crypto/pull/777).
- get_certificate - adds ``tls_ctx_options`` option for specifying SSL CTX options (https://github.com/ansible-collections/community.crypto/pull/779).
- get_certificate - allow to obtain the certificate chain sent by the server, and the one used for validation, with the new ``get_certificate_chain`` option. Note that this option only works if the module is run with Python 3.10 or newer (https://github.com/ansible-collections/community.crypto/issues/568, https://github.com/ansible-collections/community.crypto/pull/784).
- openssl_privatekey, openssl_privatekey_pipe - add default value ``auto`` for ``cipher`` option, which happens to be the only supported value for this option anyway. Therefore it is no longer necessary to specify ``cipher=auto`` when providing ``passphrase`` (https://github.com/ansible-collections/community.crypto/issues/793, https://github.com/ansible-collections/community.crypto/pull/794).

community.docker
~~~~~~~~~~~~~~~~

- docker, docker_api connection plugins - allow to determine the working directory when executing commands with the new ``working_dir`` option (https://github.com/ansible-collections/community.docker/pull/943).
- docker, docker_api connection plugins - allow to execute commands with extended privileges with the new ``privileges`` option (https://github.com/ansible-collections/community.docker/pull/943).
- docker, docker_api connection plugins - allow to pass extra environment variables when executing commands with the new ``extra_env`` option (https://github.com/ansible-collections/community.docker/issues/937, https://github.com/ansible-collections/community.docker/pull/940).
- docker_compose_v2 - add ``renew_anon_volumes`` parameter for ``docker compose up`` (https://github.com/ansible-collections/community.docker/pull/977).
- docker_compose_v2* modules - support Docker Compose 2.29.0's ``json`` progress writer to avoid having to parse text output (https://github.com/ansible-collections/community.docker/pull/931).
- docker_compose_v2_pull - add new options ``ignore_buildable``, ``include_deps``, and ``services`` (https://github.com/ansible-collections/community.docker/issues/941, https://github.com/ansible-collections/community.docker/pull/942).
- docker_container - add support for ``device_cgroup_rules`` (https://github.com/ansible-collections/community.docker/pull/910).
- docker_container - the new ``state=healthy`` allows to wait for a container to become healthy on startup. The ``healthy_wait_timeout`` option allows to configure the maximum time to wait for this to happen (https://github.com/ansible-collections/community.docker/issues/890, https://github.com/ansible-collections/community.docker/pull/921).
- docker_container - when creating a container, directly pass all networks to connect to to the Docker Daemon for API version 1.44 and newer. This makes creation more efficient and works around a bug in Docker Daemon that does not use the specified MAC address in at least some cases, though only for creation (https://github.com/ansible-collections/community.docker/pull/933).

community.general
~~~~~~~~~~~~~~~~~

- CmdRunner module util - argument formats can be specified as plain functions without calling ``cmd_runner_fmt.as_func()`` (https://github.com/ansible-collections/community.general/pull/8479).
- CmdRunner module utils - the parameter ``force_lang`` now supports the special value ``auto`` which will automatically try and determine the best parsable locale in the system (https://github.com/ansible-collections/community.general/pull/8517).
- MH module utils - add parameter ``when`` to ``cause_changes`` decorator (https://github.com/ansible-collections/community.general/pull/8766).
- MH module utils - minor refactor in decorators (https://github.com/ansible-collections/community.general/pull/8766).
- alternatives - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8833).
- ansible_galaxy_install - add return value ``version`` (https://github.com/ansible-collections/community.general/pull/9060).
- ansible_galaxy_install - add upgrade feature (https://github.com/ansible-collections/community.general/pull/8431, https://github.com/ansible-collections/community.general/issues/8351).
- ansible_galaxy_install - minor refactor in the module (https://github.com/ansible-collections/community.general/pull/8413).
- apache2_mod_proxy - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8814).
- apache2_mod_proxy - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8833).
- cargo - add option ``directory``, which allows source directory to be specified (https://github.com/ansible-collections/community.general/pull/8480).
- cgroup_memory_recap, hipchat, jabber, log_plays, loganalytics, logentries, logstash, slack, splunk, sumologic, syslog_json callback plugins - make sure that all options are typed (https://github.com/ansible-collections/community.general/pull/8628).
- chef_databag, consul_kv, cyberarkpassword, dsv, etcd, filetree, hiera, onepassword, onepassword_doc, onepassword_raw, passwordstore, redis, shelvefile, tss lookup plugins - make sure that all options are typed (https://github.com/ansible-collections/community.general/pull/8626).
- chroot, funcd, incus, iocage, jail, lxc, lxd, qubes, zone connection plugins - make sure that all options are typed (https://github.com/ansible-collections/community.general/pull/8627).
- cmd_runner module utils - add decorator ``cmd_runner_fmt.stack`` (https://github.com/ansible-collections/community.general/pull/8415).
- cmd_runner module utils - refactor argument formatting code to its own Python module (https://github.com/ansible-collections/community.general/pull/8964).
- cmd_runner_fmt module utils - simplify implementation of ``cmd_runner_fmt.as_bool_not()`` (https://github.com/ansible-collections/community.general/pull/8512).
- cobbler, linode, lxd, nmap, online, scaleway, stackpath_compute, virtualbox inventory plugins - make sure that all options are typed (https://github.com/ansible-collections/community.general/pull/8625).
- consul_acl - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8833).
- consul_kv - add argument for the datacenter option on Consul API (https://github.com/ansible-collections/community.general/pull/9026).
- copr - Added ``includepkgs`` and ``excludepkgs`` parameters to limit the list of packages fetched or excluded from the repository(https://github.com/ansible-collections/community.general/pull/8779).
- cpanm - add return value ``cpanm_version`` (https://github.com/ansible-collections/community.general/pull/9061).
- credstash lookup plugin - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8822).
- csv module utils - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8814).
- deco MH module utils - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8822).
- dig lookup plugin - add ``port`` option to specify DNS server port (https://github.com/ansible-collections/community.general/pull/8966).
- django module utils - always retrieve version (https://github.com/ansible-collections/community.general/pull/9063).
- django_check - add return value ``version`` (https://github.com/ansible-collections/community.general/pull/9063).
- django_command - add return value ``version`` (https://github.com/ansible-collections/community.general/pull/9063).
- django_createcachetable - add return value ``version`` (https://github.com/ansible-collections/community.general/pull/9063).
- doas, dzdo, ksu, machinectl, pbrun, pfexec, pmrun, sesu, sudosu become plugins - make sure that all options are typed (https://github.com/ansible-collections/community.general/pull/8623).
- etcd3 - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8822).
- flatpak - improve the parsing of Flatpak application IDs based on official guidelines (https://github.com/ansible-collections/community.general/pull/8909).
- gconftool2 - make use of ``ModuleHelper`` features to simplify code (https://github.com/ansible-collections/community.general/pull/8711).
- gcontool2 - add return value ``version`` (https://github.com/ansible-collections/community.general/pull/9064).
- gcontool2 module utils - add argument formatter ``version`` (https://github.com/ansible-collections/community.general/pull/9064).
- gcontool2_info - add return value ``version`` (https://github.com/ansible-collections/community.general/pull/9064).
- gio_mime - add return value ``version`` (https://github.com/ansible-collections/community.general/pull/9067).
- gio_mime - adjust code ahead of the old ``VardDict`` deprecation (https://github.com/ansible-collections/community.general/pull/8855).
- gio_mime - mute the  old ``VarDict`` deprecation (https://github.com/ansible-collections/community.general/pull/8776).
- gio_mime module utils - add argument formatter ``version`` (https://github.com/ansible-collections/community.general/pull/9067).
- github_app_access_token lookup plugin - adds new ``private_key`` parameter (https://github.com/ansible-collections/community.general/pull/8989).
- gitlab_deploy_key - better construct when using ``dict.items()`` (https://github.com/ansible-collections/community.general/pull/8876).
- gitlab_group - add many new parameters (https://github.com/ansible-collections/community.general/pull/8908).
- gitlab_group - better construct when using ``dict.items()`` (https://github.com/ansible-collections/community.general/pull/8876).
- gitlab_group - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8814).
- gitlab_issue - better construct when using ``dict.items()`` (https://github.com/ansible-collections/community.general/pull/8876).
- gitlab_merge_request - better construct when using ``dict.items()`` (https://github.com/ansible-collections/community.general/pull/8876).
- gitlab_project - add option ``container_expiration_policy`` to schedule container registry cleanup (https://github.com/ansible-collections/community.general/pull/8674).
- gitlab_project - add option ``issues_access_level`` to enable/disable project issues (https://github.com/ansible-collections/community.general/pull/8760).
- gitlab_project - add option ``model_registry_access_level`` to disable model registry (https://github.com/ansible-collections/community.general/pull/8688).
- gitlab_project - add option ``pages_access_level`` to disable project pages (https://github.com/ansible-collections/community.general/pull/8688).
- gitlab_project - add option ``repository_access_level`` to disable project repository (https://github.com/ansible-collections/community.general/pull/8674).
- gitlab_project - add option ``service_desk_enabled`` to disable service desk (https://github.com/ansible-collections/community.general/pull/8688).
- gitlab_project - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8822).
- gitlab_project - sorted parameters in order to avoid future merge conflicts (https://github.com/ansible-collections/community.general/pull/8759).
- gitlab_runner - better construct when using ``dict.items()`` (https://github.com/ansible-collections/community.general/pull/8876).
- hashids filter plugin - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8814).
- homebrew - speed up brew install and upgrade (https://github.com/ansible-collections/community.general/pull/9022).
- hwc_ecs_instance - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8822).
- hwc_evs_disk - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8822).
- hwc_vpc_eip - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8822).
- hwc_vpc_peering_connect - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8822).
- hwc_vpc_port - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8822).
- hwc_vpc_subnet - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8822).
- icinga2_host - replace loop with dict comprehension (https://github.com/ansible-collections/community.general/pull/8876).
- imc_rest - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8833).
- ipa_dnsrecord - adds ``SSHFP`` record type for managing SSH fingerprints in FreeIPA DNS (https://github.com/ansible-collections/community.general/pull/8404).
- ipa_otptoken - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8822).
- jenkins_node - add ``offline_message`` parameter for updating a Jenkins node offline cause reason when the state is "disabled" (offline) (https://github.com/ansible-collections/community.general/pull/9084)."
- jira - adjust code ahead of the old ``VardDict`` deprecation (https://github.com/ansible-collections/community.general/pull/8856).
- jira - mute the  old ``VarDict`` deprecation (https://github.com/ansible-collections/community.general/pull/8776).
- jira - replace deprecated params when using decorator ``cause_changes`` (https://github.com/ansible-collections/community.general/pull/8791).
- keep_keys filter plugin - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8814).
- keycloak module utils - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8822).
- keycloak_client - add ``client-x509`` choice to ``client_authenticator_type`` (https://github.com/ansible-collections/community.general/pull/8973).
- keycloak_client - assign auth flow by name (https://github.com/ansible-collections/community.general/pull/8428).
- keycloak_client - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8814).
- keycloak_clientscope - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8814).
- keycloak_identity_provider - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8814).
- keycloak_realm - add boolean toggle to configure organization support for a given keycloak realm (https://github.com/ansible-collections/community.general/issues/9027, https://github.com/ansible-collections/community.general/pull/8927/).
- keycloak_user_federation - add module argument allowing users to optout of the removal of unspecified mappers, for example to keep the keycloak default mappers (https://github.com/ansible-collections/community.general/pull/8764).
- keycloak_user_federation - add the user federation config parameter ``referral`` to the module arguments (https://github.com/ansible-collections/community.general/pull/8954).
- keycloak_user_federation - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8814).
- keycloak_user_federation - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8822).
- keycloak_user_federation - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8833).
- linode - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8814).
- locale_gen - add support for multiple locales (https://github.com/ansible-collections/community.general/issues/8677, https://github.com/ansible-collections/community.general/pull/8682).
- lxc_container - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8822).
- lxd_container - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8814).
- manageiq_provider - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8814).
- mattermost - adds support for message priority (https://github.com/ansible-collections/community.general/issues/9068, https://github.com/ansible-collections/community.general/pull/9087).
- memcached, pickle, redis, yaml cache plugins - make sure that all options are typed (https://github.com/ansible-collections/community.general/pull/8624).
- memset_dns_reload - replace loop with ``dict()`` (https://github.com/ansible-collections/community.general/pull/8876).
- memset_memstore_info - replace loop with ``dict()`` (https://github.com/ansible-collections/community.general/pull/8876).
- memset_server_info - replace loop with ``dict()`` (https://github.com/ansible-collections/community.general/pull/8876).
- memset_zone - replace loop with ``dict()`` (https://github.com/ansible-collections/community.general/pull/8876).
- memset_zone_domain - replace loop with ``dict()`` (https://github.com/ansible-collections/community.general/pull/8876).
- memset_zone_record - replace loop with ``dict()`` (https://github.com/ansible-collections/community.general/pull/8876).
- nmcli - add ``conn_enable`` param to reload connection (https://github.com/ansible-collections/community.general/issues/3752, https://github.com/ansible-collections/community.general/issues/8704, https://github.com/ansible-collections/community.general/pull/8897).
- nmcli - add ``state=up`` and ``state=down`` to enable/disable connections (https://github.com/ansible-collections/community.general/issues/3752, https://github.com/ansible-collections/community.general/issues/8704, https://github.com/ansible-collections/community.general/issues/7152, https://github.com/ansible-collections/community.general/pull/8897).
- nmcli - better construct when using ``dict.items()`` (https://github.com/ansible-collections/community.general/pull/8876).
- npm - add ``force`` parameter to allow ``--force`` (https://github.com/ansible-collections/community.general/pull/8885).
- ocapi_utils - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8833).
- one_image - add ``create``, ``template`` and ``datastore_id`` arguments for image creation (https://github.com/ansible-collections/community.general/pull/9075).
- one_image - add ``wait_timeout`` argument for adjustable timeouts (https://github.com/ansible-collections/community.general/pull/9075).
- one_image - add option ``persistent`` to manage image persistence (https://github.com/ansible-collections/community.general/issues/3578, https://github.com/ansible-collections/community.general/pull/8889).
- one_image - extend xsd scheme to make it return a lot more info about image (https://github.com/ansible-collections/community.general/pull/8889).
- one_image - refactor code to make it more similar to ``one_template`` and ``one_vnet`` (https://github.com/ansible-collections/community.general/pull/8889).
- one_image_info - extend xsd scheme to make it return a lot more info about image (https://github.com/ansible-collections/community.general/pull/8889).
- one_image_info - refactor code to make it more similar to ``one_template`` and ``one_vnet`` (https://github.com/ansible-collections/community.general/pull/8889).
- one_service - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8814).
- one_vm - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8814).
- onepassword lookup plugin - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8833).
- open_iscsi - allow login to a portal with multiple targets without specifying any of them (https://github.com/ansible-collections/community.general/pull/8719).
- openbsd_pkg - adds diff support to show changes in installed package list. This does not yet work for check mode (https://github.com/ansible-collections/community.general/pull/8402).
- opennebula.py - add VM ``id`` and VM ``host`` to inventory host data (https://github.com/ansible-collections/community.general/pull/8532).
- opentelemetry callback plugin - fix default value for ``store_spans_in_file`` causing traces to be produced to a file named ``None`` (https://github.com/ansible-collections/community.general/issues/8566, https://github.com/ansible-collections/community.general/pull/8741).
- opkg - add return value ``version`` (https://github.com/ansible-collections/community.general/pull/9086).
- passwordstore lookup plugin - add subkey creation/update support (https://github.com/ansible-collections/community.general/pull/8952).
- passwordstore lookup plugin - add the current user to the lockfile file name to address issues on multi-user systems (https://github.com/ansible-collections/community.general/pull/8689).
- pids - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8833).
- pipx - add parameter ``suffix`` to module (https://github.com/ansible-collections/community.general/pull/8675, https://github.com/ansible-collections/community.general/issues/8656).
- pipx - added new states ``install_all``, ``uninject``, ``upgrade_shared``, ``pin``, and ``unpin`` (https://github.com/ansible-collections/community.general/pull/8809).
- pipx - added parameter ``global`` to module (https://github.com/ansible-collections/community.general/pull/8793).
- pipx - refactor out parsing of ``pipx list`` output to module utils (https://github.com/ansible-collections/community.general/pull/9044).
- pipx - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8833).
- pipx_info - add new return value ``pinned`` (https://github.com/ansible-collections/community.general/pull/9044).
- pipx_info - added parameter ``global`` to module (https://github.com/ansible-collections/community.general/pull/8793).
- pipx_info - refactor out parsing of ``pipx list`` output to module utils (https://github.com/ansible-collections/community.general/pull/9044).
- pipx_info - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8833).
- pkg5_publisher - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8833).
- pkgng - add option ``use_globs`` (default ``true``) to optionally disable glob patterns (https://github.com/ansible-collections/community.general/issues/8632, https://github.com/ansible-collections/community.general/pull/8633).
- proxmox - add ``disk_volume`` and ``mount_volumes`` keys for better readability (https://github.com/ansible-collections/community.general/pull/8542).
- proxmox - allow specification of the API port when using proxmox_* (https://github.com/ansible-collections/community.general/issues/8440, https://github.com/ansible-collections/community.general/pull/8441).
- proxmox - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8814).
- proxmox - translate the old ``disk`` and ``mounts`` keys to the new handling internally (https://github.com/ansible-collections/community.general/pull/8542).
- proxmox inventory plugin - add new fact for LXC interface details (https://github.com/ansible-collections/community.general/pull/8713).
- proxmox inventory plugin - clean up authentication code (https://github.com/ansible-collections/community.general/pull/8917).
- proxmox inventory plugin - fix urllib3 ``InsecureRequestWarnings`` not being suppressed when a token is used (https://github.com/ansible-collections/community.general/pull/9099).
- proxmox_disk - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8814).
- proxmox_kvm - adds the ``ciupgrade`` parameter to specify whether cloud-init should upgrade system packages at first boot (https://github.com/ansible-collections/community.general/pull/9066).
- proxmox_kvm - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8814).
- proxmox_kvm - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8822).
- proxmox_template - small refactor in logic for determining whether a template exists or not (https://github.com/ansible-collections/community.general/pull/8516).
- proxmox_vm_info - add ``network`` option to retrieve current network information (https://github.com/ansible-collections/community.general/pull/8471).
- redfish_* modules - adds ``ciphers`` option for custom cipher selection (https://github.com/ansible-collections/community.general/pull/8533).
- redfish_command - add ``UpdateUserAccountTypes`` command (https://github.com/ansible-collections/community.general/issues/9058, https://github.com/ansible-collections/community.general/pull/9059).
- redfish_command - add ``wait`` and ``wait_timeout`` options to allow a user to block a command until a service is accessible after performing the requested command (https://github.com/ansible-collections/community.general/issues/8051, https://github.com/ansible-collections/community.general/pull/8434).
- redfish_command - add handling of the ``PasswordChangeRequired`` message from services in the ``UpdateUserPassword`` command to directly modify the user's password if the requested user is the one invoking the operation (https://github.com/ansible-collections/community.general/issues/8652, https://github.com/ansible-collections/community.general/pull/8653).
- redfish_confg - remove ``CapacityBytes`` from required paramaters of the ``CreateVolume`` command (https://github.com/ansible-collections/community.general/pull/8956).
- redfish_config - add parameter ``storage_none_volume_deletion`` to ``CreateVolume`` command in order to control the automatic deletion of non-RAID volumes (https://github.com/ansible-collections/community.general/pull/8990).
- redfish_info - add command ``CheckAvailability`` to check if a service is accessible (https://github.com/ansible-collections/community.general/issues/8051, https://github.com/ansible-collections/community.general/pull/8434).
- redfish_info - adds ``RedfishURI`` and ``StorageId`` to Disk inventory (https://github.com/ansible-collections/community.general/pull/8937).
- redfish_utils - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8833).
- redfish_utils module utils - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8822).
- redfish_utils module utils - schedule a BIOS configuration job at next reboot when the BIOS config is changed (https://github.com/ansible-collections/community.general/pull/9012).
- redis cache plugin - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8833).
- redis, redis_info - add ``client_cert`` and ``client_key`` options to specify path to certificate for Redis authentication  (https://github.com/ansible-collections/community.general/pull/8654).
- redis_info - adds support for getting cluster info (https://github.com/ansible-collections/community.general/pull/8464).
- remove_keys filter plugin - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8814).
- replace_keys filter plugin - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8814).
- scaleway - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8833).
- scaleway module utils - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8822).
- scaleway_compute - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8833).
- scaleway_container - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8858).
- scaleway_container_info - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8858).
- scaleway_container_namespace - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8858).
- scaleway_container_namespace_info - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8858).
- scaleway_container_registry - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8858).
- scaleway_container_registry_info - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8858).
- scaleway_function - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8858).
- scaleway_function_info - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8858).
- scaleway_function_namespace - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8858).
- scaleway_function_namespace_info - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8858).
- scaleway_ip - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8833).
- scaleway_lb - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8833).
- scaleway_security_group - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8822).
- scaleway_security_group - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8833).
- scaleway_user_data - better construct when using ``dict.items()`` (https://github.com/ansible-collections/community.general/pull/8876).
- scaleway_user_data - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8833).
- sensu_silence - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8833).
- snmp_facts - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8833).
- sorcery - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8833).
- sudosu become plugin - added an option (``alt_method``) to enhance compatibility with more versions of ``su`` (https://github.com/ansible-collections/community.general/pull/8214).
- udm_dns_record - replace loop with ``dict.update()`` (https://github.com/ansible-collections/community.general/pull/8876).
- ufw - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8822).
- unsafe plugin utils - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8814).
- vardict module utils - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8814).
- vars MH module utils - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8814).
- virtualbox inventory plugin - expose a new parameter ``enable_advanced_group_parsing`` to change how the VirtualBox dynamic inventory parses VM groups (https://github.com/ansible-collections/community.general/issues/8508, https://github.com/ansible-collections/community.general/pull/8510).
- vmadm - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8822).
- wdc_redfish_command - minor change to handle upgrade file for Redfish WD platforms (https://github.com/ansible-collections/community.general/pull/8444).

community.grafana
~~~~~~~~~~~~~~~~~

- Add `grafana_contact_point` module
- Add support of `grafana_contact_point` in grafana role
- Manage subfolders for `grafana_folder` and specify uid
- add org switch by `org_id` and `org_name` in `grafana_silence`

community.mysql
~~~~~~~~~~~~~~~

- mysql_info - Add ``tls_requires`` returned value for the ``users_info`` filter (https://github.com/ansible-collections/community.mysql/pull/628).
- mysql_info - return a database server engine used (https://github.com/ansible-collections/community.mysql/issues/644).
- mysql_replication - Adds support for `CHANGE REPLICATION SOURCE TO` statement (https://github.com/ansible-collections/community.mysql/issues/635).
- mysql_replication - Adds support for `SHOW BINARY LOG STATUS` and `SHOW BINLOG STATUS` on getprimary mode.
- mysql_replication - Improve detection of IsReplica and IsPrimary by inspecting the dictionary returned from the SQL query instead of relying on variable types. This ensures compatibility with changes in the connector or the output of SHOW REPLICA STATUS and SHOW MASTER STATUS, allowing for easier maintenance if these change in the future.
- mysql_user - Add salt parameter to generate static hash for `caching_sha2_password` and `sha256_password` plugins.

community.okd
~~~~~~~~~~~~~

- connection/oc - added support of local enviroment variable that will be used for ``oc`` and may be requried for establishing connections ifself (https://github.com/openshift/community.okd/pull/225).
- inventory/openshift.py - Defer removal of k8s inventory plugin to version 5.0.0 (https://github.com/openshift/community.okd/pull/224).

community.postgresql
~~~~~~~~~~~~~~~~~~~~

- postgres - add support for postgres ``infinity`` timestamps by replacing them with ``datetime.min`` / ``datetime.max`` values (https://github.com/ansible-collections/community.postgresql/pull/714).
- postgresql_privs - adds support for granting and revoking privileges on foreign tables (https://github.com/ansible-collections/community.postgresql/issues/724).
- postgresql_publication - add the ``tables_in_schema`` argument to implement ``FOR TABLES IN SCHEMA`` feature (https://github.com/ansible-collections/community.postgresql/issues/709).
- postgresql_set - adds the ``queries`` return value to return executed DML statements.
- postgresql_subscription - adds support for managing subscriptions in the situation where the ``subconninfo`` column is unavailable (such as in CloudSQL) (https://github.com/ansible-collections/community.postgresql/issues/726).
- postgresql_user - adds the ``configuration`` argument that allows to manage user-specific default configuration (https://github.com/ansible-collections/community.postgresql/issues/598).

community.proxysql
~~~~~~~~~~~~~~~~~~

- proxysql role - add the pidfile location management (https://github.com/ansible-collections/community.proxysql/pull/145).
- role_proxysql - Update default proxysql version and fix small bugs (https://github.com/ansible-collections/community.proxysql/pull/92).

community.routeros
~~~~~~~~~~~~~~~~~~

- api_info - allow to restrict the output by limiting fields to specific values with the new ``restrict`` option (https://github.com/ansible-collections/community.routeros/pull/305).
- api_info, api_modify - add ``system health settings`` path (https://github.com/ansible-collections/community.routeros/pull/294).
- api_info, api_modify - add missing path ``/ppp secret`` (https://github.com/ansible-collections/community.routeros/pull/286).
- api_info, api_modify - add missing path ``/system resource irq rps`` (https://github.com/ansible-collections/community.routeros/pull/295).
- api_info, api_modify - add new parameters from the RouterOS 7.16 release (https://github.com/ansible-collections/community.routeros/pull/323).
- api_info, api_modify - add parameter ``host-key-type`` for ``ip ssh`` path (https://github.com/ansible-collections/community.routeros/issues/280, https://github.com/ansible-collections/community.routeros/pull/297).
- api_info, api_modify - add support ``interface l2tp-client`` configuration (https://github.com/ansible-collections/community.routeros/pull/322).
- api_info, api_modify - add support for the ``cpu-frequency``, ``memory-frequency``, ``preboot-etherboot`` and ``preboot-etherboot-server`` properties in ``system routerboard settings`` (https://github.com/ansible-collections/community.routeros/pull/320).
- api_info, api_modify - add support for the ``ip dhcp-server matcher`` path (https://github.com/ansible-collections/community.routeros/pull/300).
- api_info, api_modify - add support for the ``ip dns adlist`` path implemented by RouterOS 7.15 and newer (https://github.com/ansible-collections/community.routeros/pull/310).
- api_info, api_modify - add support for the ``ipv6 nd prefix`` path (https://github.com/ansible-collections/community.routeros/pull/303).
- api_info, api_modify - add support for the ``matching-type`` property in ``ip dhcp-server matcher`` introduced by RouterOS 7.16 (https://github.com/ansible-collections/community.routeros/pull/321).
- api_info, api_modify - add support for the ``mld-version`` and ``multicast-querier`` properties in ``interface bridge`` (https://github.com/ansible-collections/community.routeros/pull/315).
- api_info, api_modify - add support for the ``name`` and ``is-responder`` properties under the ``interface wireguard peers`` path introduced in RouterOS 7.15 (https://github.com/ansible-collections/community.routeros/pull/304).
- api_info, api_modify - add support for the ``routing filter num-list`` path implemented by RouterOS 7 and newer (https://github.com/ansible-collections/community.routeros/pull/313).
- api_info, api_modify - add support for the ``routing igmp-proxy`` path (https://github.com/ansible-collections/community.routeros/pull/309).
- api_info, api_modify - add support for the ``routing ospf static-neighbor`` path in RouterOS 7 (https://github.com/ansible-collections/community.routeros/pull/302).
- api_info, api_modify - minor changes ``/interface ethernet`` path fields (https://github.com/ansible-collections/community.routeros/pull/288).
- api_info, api_modify - set default for ``force`` in ``ip dhcp-server option`` to an explicit ``false`` (https://github.com/ansible-collections/community.routeros/pull/300).
- api_modify - allow to restrict what is updated by limiting fields to specific values with the new ``restrict`` option (https://github.com/ansible-collections/community.routeros/pull/305).
- api_modify, api_info - add read-only ``default`` field to ``snmp community`` (https://github.com/ansible-collections/community.routeros/pull/311).

community.sops
~~~~~~~~~~~~~~

- Detect SOPS 3.9.0 and use new ``decrypt`` and ``encrypt`` subcommands (https://github.com/ansible-collections/community.sops/pull/190).
- decrypt filter plugin - now supports the input and output type ``ini`` (https://github.com/ansible-collections/community.sops/pull/204).
- sops lookup plugin - new option ``extract`` allows extracting a single key out of a JSON or YAML file, equivalent to sops' ``decrypt --extract`` (https://github.com/ansible-collections/community.sops/pull/200).
- sops lookup plugin - now supports the input and output type ``ini`` (https://github.com/ansible-collections/community.sops/pull/204).
- sops vars plugin - allow to configure the valid extensions with an ``ansible.cfg`` entry or with an environment variable (https://github.com/ansible-collections/community.sops/pull/185).
- sops vars plugin - new option ``handle_unencrypted_files`` allows to control behavior when encountering unencrypted files with SOPS 3.9.0+ (https://github.com/ansible-collections/community.sops/pull/190).

community.vmware
~~~~~~~~~~~~~~~~

- vmware_host_logbundle - Add timeout parameter (https://github.com/ansible-collections/community.vmware/pull/2092).
- vmware_vm_info - Improve performance when parsing custom attributes information (https://github.com/ansible-collections/community.vmware/pull/2194)
- vmware_vm_vm_drs_rule - added datacenter argument to correctly deal with multiple clusters with same name(https://github.com/ansible-collections/community.vmware/issues/2101).
- vsphere_file - Fix examples in documentation (https://github.com/ansible-collections/community.vmware/issues/2110).

community.windows
~~~~~~~~~~~~~~~~~

- Set minimum supported Ansible version to 2.15 to align with the versions still supported by Asnible.

community.zabbix
~~~~~~~~~~~~~~~~

- All Roles - Add support for yum authentication on RHEL based operating systems.
- All Roles - Add the `zabbix_manage_repo` variable.
- All Roles - Added support for Ubuntu 24.04 (Noble Numbat)
- All Roles - Changed logic for installing selinux related changes based the status of selinux on the target system.
- All Roles - Include installation of GPG key for RHEL based operating systems.
- All Roles - Updated all Zabbix configuration bool variables to be `true`/`false`.
- All Roles - Updated include option to include all .conf files.
- added new module zabbix_proxy_group (Zabbix 7.0)
- httpapi - added ability to switch username/password during playbook execution.
- zabbix_agent Role - Fixes assert warning 'conditional statements should not include jinja2 templating delimiters such as..'
- zabbix_agent Role - Reworked Include logic based on Alias logic
- zabbix_agent Role - Set `no_log` parameter to hostmacro API call.
- zabbix_agent role - Standardized all configuration variables using the `zabbix_agent` prefix vs `zabbix_agent2`.  Support for `zabbix_agent2` to be removed in 3.0.0
- zabbix_agent role - Standardized templating of agent.conf file
- zabbix_agent role - Updated defaults to be inline with Zabbix defaults.
- zabbix_agent role - added 10 retries to agent API calls to workaround connection problems on macOS
- zabbix_agent role - refactored userparameter tasks to be more efficient.
- zabbix_discovery_rule, zabbix_group_events_info, zabbix_host, zabbix_host_events_info, zabbix_proxy, zabbix_proxy_info modules updated to work wih Zabbix 7.0
- zabbix_discoveryrule module added
- zabbix_host_events_info - add tag support
- zabbix_host_events_update module added
- zabbix_inventory Plugin - Add support for jinja2 templating for auth_token in zabbix_inventory.yml
- zabbix_item - add support for setting master items by name
- zabbix_item module added
- zabbix_itemprototype - add support for setting master items by name
- zabbix_itemprototype module added
- zabbix_mfa module added
- zabbix_trigger module added
- zabbix_triggerprototype module added

containers.podman
~~~~~~~~~~~~~~~~~

- Add arch to podman build command explicitly
- Add autodiscovery for build context in podman_image
- Add docs, tests and more examples for podman_pod
- Add extra_args for podman_image push and pull
- Add group_add parameter for podman quadlet
- Add idempotency for mounts and volumes in podman_container
- Add new functionality tests for podman_secret
- Add option for inline Containerfile in podman_image
- Add path and env options for podman_secret
- Add route, dns and ipam_driver to podman_network
- Add support for check_mode in Quadlet
- CI Update python for latest Ansible to 3.11 in CI
- Create podman secret when skip_existing=True and it does not exist
- Trigger a new image build when we detect that the Containerfile has changed.
- Update inspection info about objects in modules

dellemc.enterprise_sonic
~~~~~~~~~~~~~~~~~~~~~~~~

- bgp_af - Add support for 'import vrf' commands (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/351).
- sonic_bfd - Add playbook check and diff modes support for bfd module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/346).
- sonic_bgp - Add playbook check and diff modes support for bgp module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/350).
- sonic_bgp - Add support BGP Asn Notation (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/417).
- sonic_bgp - Fix GitHub issue# 416 (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/418).
- sonic_bgp_af - Add playbook check and diff modes support for bgp_af module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/350).
- sonic_bgp_af - Add support for BGP Asn Notation (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/417).
- sonic_bgp_af - Add support for aggregate address configuration(https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/398).
- sonic_bgp_af - Update replaced state handling (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/400)
- sonic_bgp_as_paths - Add playbook check and diff modes support for bgp_as_paths module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/350).
- sonic_bgp_communities - Add playbook check and diff modes support for bgp_communities module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/350).
- sonic_bgp_ext_communities - Add playbook check and diff modes support for bgp_ext_communities module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/350).
- sonic_bgp_neighbors - Add playbook check and diff modes support for bgp_neighbors module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/360).
- sonic_bgp_neighbors - Add support for BGP Asn Notation (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/417).
- sonic_bgp_neighbors - Add support for replaced and overridden states (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/335).
- sonic_bgp_neighbors - Add support for replaced and overridden states (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/336).
- sonic_bgp_neighbors - Add support for the "fabric_external" option (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/336).
- sonic_bgp_neighbors_af - Add playbook check and diff modes support for bgp_neighbors_af module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/360).
- sonic_bgp_neighbors_af - Add support for BGP Asn Notation (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/417).
- sonic_copp - Add playbook check and diff modes support for copp module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/346).
- sonic_dhcp_relay - Add playbook check and diff modes support for dhcp_relay module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/346).
- sonic_dhcp_snooping - Add playbook check and diff modes support for dhcp_snooping module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/346).
- sonic_interfaces - Add description, enabled option support for Loopback interfaces (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/364).
- sonic_interfaces - Fix GitHub issue 357 - set proper default value when deleted (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/366).
- sonic_interfaces - Update replaced state handling (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/364).
- sonic_l3_interfaces - Add playbook check and diff modes support for l3_interfaces module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/328).
- sonic_l3_interfaces - Add support for USGv6R1 related features (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/374).
- sonic_l3_interfaces - Fix IPv6 default dad configuration handling (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/428).
- sonic_lag_interfaces - Add evpn ethernet-segment support for LAG interfaces (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/403).
- sonic_lldp_global - Add playbook check and diff modes support for lldp_global module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/338).
- sonic_logging - Add support for protocol option in logging module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/317).
- sonic_mac - Add playbook check and diff modes support for mac module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/338).
- sonic_mclag - Add playbook check and diff modes support for mclag module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/337).
- sonic_mclag - Enable session-vrf command support in mclag(https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/299).
- sonic_port_breakout - Add playbook check and diff modes support for port_breakout module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/337).
- sonic_port_group - Make error message for port group facts gathering more descriptive (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/396).
- sonic_prefix_lists - Add playbook check and diff modes support for prefix_lists module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/331).
- sonic_qos_maps - Comment out PFC priority group map tests cases (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/395).
- sonic_qos_scheduler - Update states implementation (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/373).
- sonic_route_maps - Add UT for route maps module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/384).
- sonic_route_maps - Add playbook check and diff modes support for route_maps module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/331).
- sonic_route_maps - Add support for BGP Asn Notation (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/417).
- sonic_route_maps - Add support for the 'set tag' option and synchronize module documentation with argspec and model (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/413).
- sonic_stp - Add playbook check and diff modes support for stp module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/338).
- sonic_system - Add support for 'standard_extended' interface-naming mode (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/352).
- sonic_system - Add support for configuring auto-breakout feature (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/342).
- sonic_system - Adding Versatile Hash feature.(https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/401).
- sonic_system - Enable auditd command support(https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/405).
- sonic_system - Update replaced state handling (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/388).
- sonic_vxlan - Fix GitHub issue 376 - Change vxlan module get_fact function (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/393).
- sonic_vxlans - Add playbook check and diff modes support for vxlans module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/337).
- sonic_vxlans - Add support for the "external_ip" vxlan option (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/330).

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- Added support for Python 3.12.
- Added time_to_wait option in ``idrac_storage_volume`` module.
- idrac_firmware_info - This module is enhanced to support iDRAC10.
- idrac_redfish_powerstate - This module is enhanced to support full virtual A/C power cycle.
- idrac_redfish_storage_controller - This module is enhanced to support secure and/or cryptographic erase of the physical disk.
- idrac_reset - This module is enhanced to provide default username and default password for the reset operation.
- ome_application_certificate - This module is enhanced to support the upload of certificate chain.
- ome_application_network_proxy - This module is enhanced to manage the Proxy Exclusion List and Certificate Validation.

dellemc.powerflex
~~~~~~~~~~~~~~~~~

- Added support for PowerFlex Onyx version(4.6.x).
- Fixed the roles to support attaching the MDM cluster to the gateway.
- The storage pool module has been enhanced to support more features.

f5networks.f5_modules
~~~~~~~~~~~~~~~~~~~~~

- bigip_asm_dos_application - add support for creating dos profile.
- bigip_device_info - virtual-servers - return per_flow_request_access_policy if defined.
- bigip_gtm_server - Added check for datacenter existence in Check Mode.
- bigip_pool_member - Removed state from the Returnables.
- bigip_ucs - Fix for bigip_ucs module to restore UCS file on BIG-IP devices.
- bigip_virtual_server - set per_flow_request_access_policy and stay idempotent.

fortinet.fortimanager
~~~~~~~~~~~~~~~~~~~~~

- Supported FortiManager 7.4.3. 7 new modules.
- Supported FortiManager 7.6.0. Added 7 new modules.
- Supported ansible-core 2.17.
- Supported check mode for all modules except "fmgr_generic". You can use "ansible-playbook -i <your-host-file> <your-playbook> --check" to validate whether your playbook will make any changes to the FortiManager.

google.cloud
~~~~~~~~~~~~

- ansible - 2.16.0 is now the minimum version supported
- ansible - 3.10 is now the minimum Python version
- ansible-test - integration tests are now run against 2.16.0 and 2.17.0
- gcloud role - use dnf instead of yum on RHEL
- gcp_secret_manager - add as a module and lookup plugin (https://github.com/ansible-collections/google.cloud/pull/578)
- gcp_secret_manager - support more than 10 versions (https://github.com/ansible-collections/google.cloud/pull/634)
- restore google_cloud_ops_agents submodule (https://github.com/ansible-collections/google.cloud/pull/594)

hetzner.hcloud
~~~~~~~~~~~~~~

- Use a truncated exponential backoff algorithm when polling actions from the API.
- load_balancer_status - Add new filter to compute the status of a Load Balancer based on its targets.
- server_type_info - The 'included_traffic' return value is deprecated and will be set to 'None' on 5 August 2024. See https://docs.hetzner.cloud/changelog#2024-07-25-cloud-api-returns-traffic-information-in-different-format.

ibm.storage_virtualize
~~~~~~~~~~~~~~~~~~~~~~

- ibm_sv_manage_security - Added support to allow automatic download of security patches
- ibm_sv_manage_storage_partition - Added support for creating draft partition, publishing a draft partition, and merging 2 partitions
- ibm_sv_manage_syslog_server - Added support for creating TLS syslog server, and modifying existing UDP or TCP servers to TLS server
- ibm_sv_manage_truststore_for_replication - Added support for enabling various options (syslog, RESTAPI, vasa, ipsec, snmp and email) during truststore creation
- ibm_svc_host - Added support to add host into draft partition and to create an NVMeFC host
- ibm_svc_info - Added support to display concise view of all SVC objects not covered by I(gather_subset), detailed view for all SVC objects, concise view of a subset of objects allowing a I(filtervalue)
- ibm_svc_manage_portset - Added support to create a high-speed replication portset
- ibm_svc_manage_volumegroup - Added support to add existing volumegroups into draft partition
- ibm_svcinfo_command - Added support for sainfo commands
- ibm_svctask_command - Added support for satask commands

infoblox.nios_modules
~~~~~~~~~~~~~~~~~~~~~

- Added IPv6 network container support for the `nios_next_network` lookup plugin.
- Added `use_range` parameter to the nios_next_ip lookup plugin, enabling lookup for the next available IP from a network range.
- Added support for the `use_dns_ea_inheritance` parameter in Host Record to inherit EA from associated zone.
- Added support for the `use_for_ea_inheritance` parameter in Host Record to inherit EA from Host address.
- Enabled IPv4 support for PXE server configuration in the Host Record module.
- Improved handling of DHCP options in DHCP Range, Network, and Network Container.
- Introduced `use_logic_filter_rules` & `logic_filter_rules` support for both IPv4 and IPv6 network and network container.
- Upgraded the base WAPI version to 2.12.3.

junipernetworks.junos
~~~~~~~~~~~~~~~~~~~~~

- Add implementation to gather ether-channels for gig-ether-options.
- Added support for virtual-switch instances.
- Based on ether-option-type create supported commands for config module.
- Implemented bridge-domains configuration management for routing instances.
- Implemented support for setting the Maximum Transmission Unit (MTU) in Layer 3 (L3) Internet Protocol (IP) interfaces.
- Tested successfully on Junos MX204.

kubernetes.core
~~~~~~~~~~~~~~~

- connection/kubectl.py - Added an example of using the kubectl connection plugin to the documentation (https://github.com/ansible-collections/kubernetes.core/pull/741).
- inventory/k8s.py - Defer removal of k8s inventory plugin to version 5.0 (https://github.com/ansible-collections/kubernetes.core/pull/723).
- inventory/k8s.py - Defer removal of k8s inventory plugin to version 6.0.0 (https://github.com/ansible-collections/kubernetes.core/pull/734).
- k8s - The module and K8sService were changed so warnings returned by the K8S API are now displayed to the user.
- k8s_drain - Improve error message for pod disruption budget when draining a node (https://github.com/ansible-collections/kubernetes.core/issues/797).

microsoft.ad
~~~~~~~~~~~~

- Set minimum supported Ansible version to 2.15 to align with the versions still supported by Ansible.
- microsoft.ad AD modules - Added ``domain_credentials`` as a common module option that can be used to specify credentials for specific AD servers.
- microsoft.ad AD modules - Added ``lookup_failure_action`` on all modules that can specify a list of distinguishedName values to control what should happen if the lookup fails.
- microsoft.ad.computer - Added the ``do_not_append_dollar_to_sam`` option which can create a computer account without the ``$`` suffix when an explicit ``sam_account_name`` was provided without one.
- microsoft.ad.computer - Added the ability to lookup a distinguishedName on a specific domain server for ``delegates`` and ``managed_by``.
- microsoft.ad.domain - Added ``reboot_timeout`` option to control how long a reboot can go for.
- microsoft.ad.domain_child - Added ``reboot_timeout`` option to control how long a reboot can go for.
- microsoft.ad.domain_controller - Added ``reboot_timeout`` option to control how long a reboot can go for.
- microsoft.ad.group - Added the ability to lookup a distinguishedName on a specific domain server for ``managed_by`` and ``members``.
- microsoft.ad.membership - Added ``domain_server`` option to specify the DC to use for domain join operations - https://github.com/ansible-collections/microsoft.ad/issues/131#issuecomment-2201151651
- microsoft.ad.membership - Added ``reboot_timeout`` option to control how long a reboot can go for.
- microsoft.ad.ou - Added the ability to lookup a distinguishedName on a specific domain server for ``managed_by``.
- microsoft.ad.user - Added the ability to lookup a distinguishedName on a specific domain server for ``delegates``.
- microsoft.ad.user - Rename the option ``groups.missing_action`` to ``groups.lookup_failure_action`` to make the option more consistent with other modules. The ``missing_action`` option is still supported as an alias.
- microsoft.ad.user - Support group member lookup on alternative server using the DN lookup syntax. This syntax uses a dictionary where ``name`` defined the group to lookup and ``server`` defines the server to lookup the group on.

netapp.cloudmanager
~~~~~~~~~~~~~~~~~~~

- na_cloudmanager_cvo_aws - increase timeout for creating cvo to 90 mins.
- na_cloudmanager_cvo_azure - increase timeout for creating cvo to 90 mins.
- na_cloudmanager_cvo_gcp - increase timeout for creating cvo to 90 mins.

netapp.ontap
~~~~~~~~~~~~

- all modules supporting ZAPI & REST - throw authentication error instead of falling back to ZAPI when username/password is incorrect.
- na_ontap_bgp_peer_group - added new option `use_peer_as_next_hop`, requires ONTAP 9.9 or later.
- na_ontap_cifs - added REST support for option `vscan_fileop_profile`, requires ONTAP 9.15.1 or later.
- na_ontap_rest_cli - return command output for GET and OPTIONS verbs during check mode.
- na_ontap_security_key_manager - added warning message in REST when passphrase is not changed.
- na_ontap_snapshot_policy - new option `retention_period` added in REST, requires ONTAP 9.12 or later.
- na_ontap_volume - new option `activity_tracking` added in REST, requires ONTAP 9.10 or later.
- na_ontap_volume - new option `snapshot_locking` added in REST, requires ONTAP 9.12 or later.

netbox.netbox
~~~~~~~~~~~~~

- Add ``facility`` to ``location`` (https://github.com/netbox-community/ansible_modules/issues/1280)
- Add ``related_object_type`` to ``netbox_custom_filed`` (https://github.com/netbox-community/ansible_modules/issues/1268)
- Add ``status`` to ``location`` (https://github.com/netbox-community/ansible_modules/issues/1279)
- Add `description` to `netbox_cluster_group` module (https://github.com/netbox-community/ansible_modules/issues/1276)
- Add `serial` to `netbox_virtual_machine` module (https://github.com/netbox-community/ansible_modules/issues/1309)
- Add `status` to `netbox_cluster` (https://github.com/netbox-community/ansible_modules/issues/1275)
- Add `vid_ranges` to `netbox_vlan_group` module (https://github.com/netbox-community/ansible_modules/issues/1307)
- Add ability to rename variables set on the host by ``netbox.netbox.nb_inventory`` through configuration.
- Add cluster host to dynamic inventory response `#1219 <https://github.com/netbox-community/ansible_modules/pull/1219>`_
- Add galaxy-importer to CI process `#1245 <https://github.com/netbox-community/ansible_modules/issues/1245>`_
- Added option `hostname_field` to ``nb_inventory`` to be able to set the inventory hostname from a field in custom_fields
- Adjust modules to support NetBox v4.0.0 `#1234 <https://github.com/netbox-community/ansible_modules/pull/1234>`_
- Adjust tests for various modules
- Bump jinja2 from 3.1.2 to 3.1.4 `#1226 <https://github.com/netbox-community/ansible_modules/pull/1226>`_
- Bump requests from 2.31.0 to 2.32.0 `#1236 <https://github.com/netbox-community/ansible_modules/pull/1236>`_
- Bump version 3.19.1
- Drop obsolete Ansible and Python versions and fix tests `#1241 <https://github.com/netbox-community/ansible_modules/issues/1241>`_
- Fix the form_factor option on netbox_rack
- Get ansible-lint passing again (sequence after `#1241 <https://github.com/netbox-community/ansible_modules/issues/1241>`_) `#1243 <https://github.com/netbox-community/ansible_modules/issues/1243>`_
- Update CI for NetBox 4.1
- Update CI process to follow Ansible Collection Standards `#1247 <https://github.com/netbox-community/ansible_modules/issues/1247>`_
- Update CI to use master instead of main. `#1253 <https://github.com/netbox-community/ansible_modules/issues/1253>`_
- Update ansible-lint to ignore changelog file for yaml indentation. `#1256 <https://github.com/netbox-community/ansible_modules/issues/1256>`_
- Update top-level README with new minimum Ansible version (sequence after `#1241 <https://github.com/netbox-community/ansible_modules/issues/1241>`_ `#1244 <https://github.com/netbox-community/ansible_modules/issues/1244>`_
- Updated CI to only run changelog job if PR into devel branch is detected. `#1251 <https://github.com/netbox-community/ansible_modules/issues/1251>`_
- Updated CI to support NetBox 4.0 `#1230 <https://github.com/netbox-community/ansible_modules/pull/1230>`_
- Updates to top-level README.md to align collection with Ansible best practices `#1238 <https://github.com/netbox-community/ansible_modules/issues/1238>`_

ngine_io.cloudstack
~~~~~~~~~~~~~~~~~~~

- Added possiblity to disable certs validation using ``validate_certs`` argument (https://github.com/ngine-io/ansible-collection-cloudstack/pull/131).
- cs_instance - Added new arguments ``user_data_name`` and ``user_data_details`` (https://github.com/ngine-io/ansible-collection-cloudstack/pull/134).
- cs_project - Extended to pass ``cleanup=true`` to the deleteProject API when deleting a project (https://github.com/ngine-io/ansible-collection-cloudstack/pull/122).
- cs_service_offering - Add support for storagetag (https://github.com/ngine-io/ansible-collection-cloudstack/pull/118).

purestorage.flasharray
~~~~~~~~~~~~~~~~~~~~~~

- all - add ``disable_warnings`` parameters
- purefa_alert - Add new ``state`` of ``test`` to check alert manager configuration
- purefa_alert - Converted to REST v2
- purefa_connect - Add support for TLS encrypted array connections
- purefa_connect - Convert to REST v2
- purefa_console - Convert to REST v2
- purefa_dns - Convert to REST v2
- purefa_ds - Add new ``state`` of ``test`` to check directory services configuration
- purefa_ds - Convert to REST v2 removing all parameters used unsupported Purity versions
- purefa_dsrole - Convert to REST v2
- purefa_info - Add SMTP server information
- purefa_info - Fix regression of code that caused volume host connectivity info to be lost
- purefa_info - Provide array connection path information
- purefa_kmip - Add new ``state`` of ``test`` to check KMIP object configuration
- purefa_ntp - Add new ``state`` of ``test`` to check NTP configuration
- purefa_phonehome - Convert to REST v2
- purefa_pod - Add ``delete_contents`` parameter for eradication of pods.
- purefa_pod - Add support for ``throttle`` parameter from REST 2.31.
- purefa_pod - Convert to REST v2.
- purefa_ra - Add new ``state`` of ``test`` to check remote support configuration
- purefa_saml - Add new ``state`` of ``test`` to check SAML2 IdP configuration
- purefa_snmp - Add new ``state`` of ``test`` to check SNMP manager configuration
- purefa_syslog - Add new ``state`` of ``test`` to check syslog server configuration
- purefa_token - Add ``disable_warnings`` support

purestorage.flashblade
~~~~~~~~~~~~~~~~~~~~~~

- all - add ``disable_warnings`` parameters
- multiple - YAML lint fixes based on updated ``ansible-lint`` version
- purefb_bucket - Add ``safemode`` option for ``retention_mode``
- purefb_bucket - Allow bucket quotas to be modified.
- purefb_certs - Update module to use REST v2 code. This brings in new parameters for certificate management.
- purefb_fs - Set default for group_ownership to be creator
- purefb_info - Add ``time_remaining_status`` to bucket information from REST 2.14
- purefb_info - Expose SMTP encryption mode
- purefb_policy - Add new policy type of ``worm`` which is availble from Purity//FB 4.5.0
- purefb_ra - Add ``duration`` option from REST 2.14
- purefb_ra - Update to REST2
- purefb_smtp - Add encryption mode support from Purity//FB 4.5.0
- purefb_snap - Change ``targets`` to ``target` and from ``list`` to ``str``. ``targets`` added as alias and code to ensure existing list in playbooks is translated as a string.
- purefb_syslog - Enable ``services`` parameter and also the ability update existing syslog servers from REST 2.14

telekom_mms.icinga_director
~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Add vars parameter to user_template and user modules (https://github.com/telekom-mms/ansible-collection-icinga-director/pull/262)

theforeman.foreman
~~~~~~~~~~~~~~~~~~

- content_export_* - document that ``chunk_size_gb`` parameter is only applicable for ``importable`` exports (https://github.com/theforeman/foreman-ansible-modules/issues/1738)
- lifecycle_environments role - allow setting ``state`` for the LCE, allowing deletion of existing ones
- location, locations role - add ``description`` parameter to set the description
- redhat_manifest - report ``changed`` when manifest is regenerated and downloaded (https://github.com/theforeman/foreman-ansible-modules/issues/1473)

vmware.vmware_rest
~~~~~~~~~~~~~~~~~~

- add a new ci job to the collection to run integration tests on bm vmware env
- cluster_moid - Fix bug where lookup would return incosistent results for objects in nested paths. Fixes issues https://github.com/ansible-collections/vmware.vmware_rest/issues/500 https://github.com/ansible-collections/vmware.vmware_rest/pull/445 https://github.com/ansible-collections/vmware.vmware_rest/issues/324 (https://github.com/ansible-collections/vmware.vmware_rest/pull/523)
- cluster_moid - updated documentation around lookup plugin usage
- datacenter_moid - Fix bug where lookup would return incosistent results for objects in nested paths Fixes issues https://github.com/ansible-collections/vmware.vmware_rest/issues/500 https://github.com/ansible-collections/vmware.vmware_rest/pull/445 https://github.com/ansible-collections/vmware.vmware_rest/issues/324 (https://github.com/ansible-collections/vmware.vmware_rest/pull/523)
- datacenter_moid - updated documentation around lookup plugin usage
- datastore_moid - Fix bug where lookup would return incosistent results for objects in nested paths Fixes issues https://github.com/ansible-collections/vmware.vmware_rest/issues/500 https://github.com/ansible-collections/vmware.vmware_rest/pull/445 https://github.com/ansible-collections/vmware.vmware_rest/issues/324 (https://github.com/ansible-collections/vmware.vmware_rest/pull/523)
- datastore_moid - updated documentation around lookup plugin usage
- folder_moid - Fix bug where lookup would return incosistent results for objects in nested paths Fixes issues https://github.com/ansible-collections/vmware.vmware_rest/issues/500 https://github.com/ansible-collections/vmware.vmware_rest/pull/445 https://github.com/ansible-collections/vmware.vmware_rest/issues/324 (https://github.com/ansible-collections/vmware.vmware_rest/pull/523)
- folder_moid - updated documentation around lookup plugin usage
- host_moid - Fix bug where lookup would return incosistent results for objects in nested paths Fixes issues https://github.com/ansible-collections/vmware.vmware_rest/issues/500 https://github.com/ansible-collections/vmware.vmware_rest/pull/445 https://github.com/ansible-collections/vmware.vmware_rest/issues/324 (https://github.com/ansible-collections/vmware.vmware_rest/pull/523)
- host_moid - updated documentation around lookup plugin usage
- network_moid - Fix bug where lookup would return incosistent results for objects in nested paths Fixes issues https://github.com/ansible-collections/vmware.vmware_rest/issues/500 https://github.com/ansible-collections/vmware.vmware_rest/pull/445 https://github.com/ansible-collections/vmware.vmware_rest/issues/324 (https://github.com/ansible-collections/vmware.vmware_rest/pull/523)
- network_moid - updated documentation around lookup plugin usage
- resource_pool_moid - Fix bug where lookup would return incosistent results for objects in nested paths Fixes issues https://github.com/ansible-collections/vmware.vmware_rest/issues/500 https://github.com/ansible-collections/vmware.vmware_rest/pull/445 https://github.com/ansible-collections/vmware.vmware_rest/issues/324 (https://github.com/ansible-collections/vmware.vmware_rest/pull/523)
- resource_pool_moid - updated documentation around lookup plugin usage
- vcenter_vm_guest_customization - Added better examples that cover more use-cases (https://github.com/ansible-collections/vmware.vmware_rest/pull/534).
- vm_moid - Fix bug where lookup would return incosistent results for objects in nested paths Fixes issues https://github.com/ansible-collections/vmware.vmware_rest/issues/500 https://github.com/ansible-collections/vmware.vmware_rest/pull/445 https://github.com/ansible-collections/vmware.vmware_rest/issues/324 (https://github.com/ansible-collections/vmware.vmware_rest/pull/523)
- vm_moid - updated documentation around lookup plugin usage

vultr.cloud
~~~~~~~~~~~

- instance, bare_metal - Implemented a new option ``skip_wait`` (https://github.com/vultr/ansible-collection-vultr/issues/119).

vyos.vyos
~~~~~~~~~

- All GHA workflows have been updated to use ones from ansible-content-actions.
- Passes latest ansible-lint with production profile.
- Removes deprecation notice for vyos.vyos.
- Uncaps supported ansible-core versions, this collection now supports ansible-core>=2.15.

Breaking Changes / Porting Guide
--------------------------------

Ansible-core
~~~~~~~~~~~~

- Stopped wrapping all commands sent over SSH on a Windows target with a ``powershell.exe`` executable. This results in one less process being started on each command for Windows to improve efficiency, simplify the code, and make ``raw`` an actual raw command run with the default shell configured on the Windows sshd settings. This should have no affect on most tasks except for ``raw`` which now is not guaranteed to always be running in a PowerShell shell and from having the console output codepage set to UTF-8. To avoid this issue either swap to using ``ansible.windows.win_command``, ``ansible.windows.win_shell``, ``ansible.windows.win_powershell`` or manually wrap the raw command with the shell commands needed to set the output console encoding.
- persistent connection plugins - The ``ANSIBLE_CONNECTION_PATH`` config option no longer has any effect.

amazon.aws
~~~~~~~~~~

- The amazon.aws collection has dropped support for ``botocore<1.31.0`` and ``boto3<1.28.0``. Most modules will continue to work with older versions of the AWS SDK.  However, compatability with older versions of the SDK is not guaranteed and will not be tested. When using older versions of the SDK a warning will be emitted by Ansible (https://github.com/ansible-collections/amazon.aws/pull/2161).
- aws_ec2 - the parameter ``include_extra_api_calls`` was previously deprecated and has been removed (https://github.com/ansible-collections/amazon.aws/pull/2320).
- iam_policy - the ``policies`` return key was previously deprecated and has been removed, please use ``policy_names`` instead (https://github.com/ansible-collections/amazon.aws/pull/2320).
- module_utils.botocore - ``boto3_conn``'s  ``conn_type`` parameter is now mandatory (https://github.com/ansible-collections/amazon.aws/pull/2157).

cloud.common
~~~~~~~~~~~~

- cloud.common collection - Support for ansible-core < 2.15 has been dropped (https://github.com/ansible-collections/cloud.common/pull/145/files).

community.aws
~~~~~~~~~~~~~

- The community.aws collection has dropped support for ``botocore<1.31.0`` and ``boto3<1.28.0``. Most modules will continue to work with older versions of the AWS SDK.  However, compatability with older versions of the SDK is not guaranteed and will not be tested. When using older versions of the SDK a warning will be emitted by Ansible (https://github.com/ansible-collections/community.aws/pull/2195).
- autoscaling_instance_refresh - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.autoscaling_instance_refresh`` (https://github.com/ansible-collections/community.aws/pull/2177).
- autoscaling_instance_refresh_info - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.autoscaling_instance_refresh_info`` (https://github.com/ansible-collections/community.aws/pull/2177).
- ec2_launch_template - Tags defined using option ``tags`` are now applied to the launch template resources not the resource created using this launch template (https://github.com/ansible-collections/community.aws/issues/176).
- ec2_launch_template - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.ec2_launch_template`` (https://github.com/ansible-collections/community.aws/pull/2185).
- ec2_placement_group - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.ec2_placement_group``.
- ec2_placement_group_info - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.ec2_placement_group_info``.
- ec2_transit_gateway - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.ec2_transit_gateway``.
- ec2_transit_gateway_info - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.ec2_transit_gateway_info``.
- ec2_transit_gateway_vpc_attachment - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.ec2_transit_gateway_vpc_attachment``.
- ec2_transit_gateway_vpc_attachment_info - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.ec2_transit_gateway_vpc_attachment_info``.
- ec2_vpc_egress_igw - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.ec2_vpc_egress_igw`` (https://api.github.com/repos/ansible-collections/community.aws/pulls/2169).
- ec2_vpc_nacl - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.ec2_vpc_nacl`` (https://github.com/ansible-collections/community.aws/pull/2178).
- ec2_vpc_nacl_info - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.ec2_vpc_nacl_info`` (https://github.com/ansible-collections/community.aws/pull/2178).
- ec2_vpc_peer - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.ec2_vpc_peer``.
- ec2_vpc_peering_info - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.ec2_vpc_peering_info``.
- ec2_vpc_vgw - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.ec2_vpc_vgw``.
- ec2_vpc_vgw_info - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.ec2_vpc_vgw_info``.
- ec2_vpc_vpn - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.ec2_vpc_vpn``.
- ec2_vpc_vpn_info - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.ec2_vpc_vpn_info``.
- ecs_cluster - the parameter ``purge_capacity_providers`` defaults to true. (https://github.com/ansible-collections/community.aws/pull/2165).
- elb_classic_lb_info - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.elb_classic_lb_info``.
- iam_policy - the ``connection_properties`` return key was previously deprecated and has been removed, please use ``raw_connection_properties`` instead (https://github.com/ansible-collections/community.aws/pull/2165).

community.docker
~~~~~~~~~~~~~~~~

- docker_container - the default of ``image_name_mismatch`` changed from ``ignore`` to ``recreate`` (https://github.com/ansible-collections/community.docker/pull/971).

community.general
~~~~~~~~~~~~~~~~~

- The collection no longer supports ansible-core 2.13 and ansible-core 2.14. While most (or even all) modules and plugins might still work with these versions, they are no longer tested in CI and breakages regarding them will not be fixed (https://github.com/ansible-collections/community.general/pull/8921).
- cmd_runner module utils - CLI arguments created directly from module parameters are no longer assigned a default formatter (https://github.com/ansible-collections/community.general/pull/8928).
- irc - the defaults of ``use_tls`` and ``validate_certs`` changed from ``false`` to ``true`` (https://github.com/ansible-collections/community.general/pull/8918).
- rhsm_repository - the states ``present`` and ``absent`` have been removed. Use ``enabled`` and ``disabled`` instead (https://github.com/ansible-collections/community.general/pull/8918).

community.routeros
~~~~~~~~~~~~~~~~~~

- command - the module no longer declares that it supports check mode (https://github.com/ansible-collections/community.routeros/pull/318).

community.vmware
~~~~~~~~~~~~~~~~

- Adding a dependency on the ``vmware.vmware`` collection (https://github.com/ansible-collections/community.vmware/pull/2159).
- Depending on ``vmware-vcenter`` and ``vmware-vapi-common-client`` instead of ``https://github.com/vmware/vsphere-automation-sdk-python.git`` (https://github.com/ansible-collections/community.vmware/pull/2163).
- Dropping support for pyVmomi < 8.0.3.0.1 (https://github.com/ansible-collections/community.vmware/pull/2163).
- Module utils - Removed ``vmware.run_command_in_guest()`` (https://github.com/ansible-collections/community.vmware/pull/2175).
- Removed support for ansible-core version < 2.17.0.
- vmware_dvs_portgroup - Removed ``security_override`` alias for ``mac_management_override`` and support for ``securityPolicyOverrideAllowed`` which has been deprected in the vSphere API (https://github.com/ansible-collections/community.vmware/issues/1998).
- vmware_dvs_portgroup_info - Removed ``security_override`` because it's deprecated in the vSphere API (https://github.com/ansible-collections/community.vmware/issues/1998).
- vmware_guest_tools_info - Removed deprecated ``vm_tools_install_status`` from the result (https://github.com/ansible-collections/community.vmware/issues/2078).

community.zabbix
~~~~~~~~~~~~~~~~

- All Roles - Remove support for Centos 7
- All Roles - Remove support for Python2
- All Roles - Removed support for Debian 10.
- All Roles - Removed support for Ubuntu 18.08 (Bionic)
- Remove support for Ansible < 2.15 and Python < 3.9
- Remove support for Zabbix 6.2
- Removed support for Zabbix 6.2
- zabbix_agent role - Remove support for `zabbix_agent_zabbix_alias`.
- zabbix_agent role - Remove support for `zabbix_get_package` variable.
- zabbix_agent role - Remove support for `zabbix_sender_package` variable.
- zabbix_agent role - Remove support for all `zabbix_agent2_*` variables.

hetzner.hcloud
~~~~~~~~~~~~~~

- Drop support for ansible-core 2.14.

kubernetes.core
~~~~~~~~~~~~~~~

- Remove support for ``ansible-core<2.15`` (https://github.com/ansible-collections/kubernetes.core/pull/737).

vmware.vmware_rest
~~~~~~~~~~~~~~~~~~

- Removing any support for ansible-core <=2.14

Deprecated Features
-------------------

- The ``community.network`` collection has been deprecated.
  It will be removed from Ansible 12 if no one starts maintaining it again before Ansible 12.
  See `Collections Removal Process for unmaintained collections <https://docs.ansible.com/ansible/devel/community/collection_contributors/collection_package_removal.html#unmaintained-collections>`__ for more details (`https://forum.ansible.com/t/8030 <https://forum.ansible.com/t/8030>`__).
- The google.cloud collection will be removed from Ansible 12 due to violations of the Ansible inclusion requirements.
  The collection has \ `unresolved sanity test failures <https://github.com/ansible-collections/google.cloud/issues/613>`__.
  See `Collections Removal Process for collections not satisfying the collection requirements <https://docs.ansible.com/ansible/devel/community/collection_contributors/collection_package_removal.html#collections-not-satisfying-the-collection-requirements>`__ for more details, including for how this can be cancelled (`https://forum.ansible.com/t/8609 <https://forum.ansible.com/t/8609>`__).
  After removal, users can still install this collection with ``ansible-galaxy collection install google.cloud``.
- The sensu.sensu_go collection will be removed from Ansible 12 due to violations of the Ansible inclusion requirements.
  The collection has \ `unresolved sanity test failures <https://github.com/sensu/sensu-go-ansible/issues/362>`__.
  See `Collections Removal Process for collections not satisfying the collection requirements <https://docs.ansible.com/ansible/devel/community/collection_contributors/collection_package_removal.html#collections-not-satisfying-the-collection-requirements>`__ for more details, including for how this can be cancelled (`https://forum.ansible.com/t/8380 <https://forum.ansible.com/t/8380>`__).
  After removal, users can still install this collection with ``ansible-galaxy collection install sensu.sensu_go``.

Ansible-core
~~~~~~~~~~~~

- Deprecate ``ansible.module_utils.basic.AnsibleModule.safe_eval`` and ``ansible.module_utils.common.safe_eval`` as they are no longer used.
- persistent connection plugins - The ``ANSIBLE_CONNECTION_PATH`` config option no longer has any effect, and will be removed in a future release.
- yum_repository - deprecate ``async`` option as it has been removed in RHEL 8 and will be removed in ansible-core 2.22.
- yum_repository - the following options are deprecated: ``deltarpm_metadata_percentage``, ``gpgcakey``, ``http_caching``, ``keepalive``, ``metadata_expire_filter``, ``mirrorlist_expire``, ``protect``, ``ssl_check_cert_permissions``, ``ui_repoid_vars`` as they have no effect for dnf as an underlying package manager. The options will be removed in ansible-core 2.22.

amazon.aws
~~~~~~~~~~

- amazon.aws collection - due to the AWS SDKs announcing the end of support for Python less than 3.8 (https://aws.amazon.com/blogs/developer/python-support-policy-updates-for-aws-sdks-and-tools/) support for Python less than 3.8 by this collection has been deprecated and will removed in release 10.0.0 (https://github.com/ansible-collections/amazon.aws/pull/2161).
- ec2_vpc_peer - the ``ec2_vpc_peer`` module has been renamed to ``ec2_vpc_peering``. The usage of the module has not changed. The ec2_vpc_peer alias will be removed in version 13.0.0 (https://github.com/ansible-collections/amazon.aws/pull/2356).
- ec2_vpc_peering_info - ``result`` return key has been deprecated and will be removed in release 11.0.0.  Use the ``vpc_peering_connections`` return key instead (https://github.com/ansible-collections/amazon.aws/pull/2359).
- iam_role - support for creating and deleting IAM instance profiles using the ``create_instance_profile`` and ``delete_instance_profile`` options has been deprecated and will be removed in a release after 2026-05-01.  To manage IAM instance profiles the ``amazon.aws.iam_instance_profile`` module can be used instead (https://github.com/ansible-collections/amazon.aws/pull/2221).
- s3_object - Support for ``mode=list`` has been deprecated.  ``amazon.aws.s3_object_info`` should be used instead (https://github.com/ansible-collections/amazon.aws/pull/2328).

cisco.ios
~~~~~~~~~

- ios_bgp_address_family - deprecated attribute password in favour of password_options within neigbhors.
- ios_bgp_global - deprecated attributes aggregate_address, bestpath, inject_map, ipv4_with_subnet, ipv6_with_subnet, nopeerup_delay, distribute_list, address, tag, ipv6_addresses, password, route_map, route_server_context and scope
- ios_linkagg - deprecate legacy module ios_linkagg
- ios_lldp - deprecate legacy module ios_lldp

community.aws
~~~~~~~~~~~~~

- community.aws collection - due to the AWS SDKs announcing the end of support for Python less than 3.8 (https://aws.amazon.com/blogs/developer/python-support-policy-updates-for-aws-sdks-and-tools/) support for Python less than 3.8 by this collection has been deprecated and will removed in release 10.0.0 (https://github.com/ansible-collections/community.aws/pull/2195).

community.docker
~~~~~~~~~~~~~~~~

- The collection deprecates support for all ansible-core versions that are currently End of Life, `according to the ansible-core support matrix <https://docs.ansible.com/ansible-core/devel/reference_appendices/release_and_maintenance.html#ansible-core-support-matrix>`__. This means that the next major release of the collection will no longer support ansible-core 2.11, ansible-core 2.12, ansible-core 2.13, and ansible-core 2.14.

community.general
~~~~~~~~~~~~~~~~~

- CmdRunner module util - setting the value of the ``ignore_none`` parameter within a ``CmdRunner`` context is deprecated and that feature should be removed in community.general 12.0.0 (https://github.com/ansible-collections/community.general/pull/8479).
- MH decorator cause_changes module utils - deprecate parameters ``on_success`` and ``on_failure`` (https://github.com/ansible-collections/community.general/pull/8791).
- git_config - the ``list_all`` option has been deprecated and will be removed in community.general 11.0.0. Use the ``community.general.git_config_info`` module instead (https://github.com/ansible-collections/community.general/pull/8453).
- git_config - using ``state=present`` without providing ``value`` is deprecated and will be disallowed in community.general 11.0.0. Use the ``community.general.git_config_info`` module instead to read a value (https://github.com/ansible-collections/community.general/pull/8453).
- hipchat - the hipchat service has been discontinued and the self-hosted variant has been End of Life since 2020. The module is therefore deprecated and will be removed from community.general 11.0.0 if nobody provides compelling reasons to still keep it (https://github.com/ansible-collections/community.general/pull/8919).
- pipx - support for versions of the command line tool ``pipx`` older than ``1.7.0`` is deprecated and will be removed in community.general 11.0.0 (https://github.com/ansible-collections/community.general/pull/8793).
- pipx_info - support for versions of the command line tool ``pipx`` older than ``1.7.0`` is deprecated and will be removed in community.general 11.0.0 (https://github.com/ansible-collections/community.general/pull/8793).

community.grafana
~~~~~~~~~~~~~~~~~

- Deprecate `grafana_notification_channel`. It will be removed in version 3.0.0

community.mysql
~~~~~~~~~~~~~~~

- collection - support of mysqlclient connector is deprecated - use PyMySQL connector instead! We will stop testing against it in collection version 4.0.0 and remove the related code in 5.0.0 (https://github.com/ansible-collections/community.mysql/issues/654).
- mysql_info - The ``users_info`` filter returned variable ``plugin_auth_string`` contains the hashed password and it's misleading, it will be removed from community.mysql 4.0.0. Use the `plugin_hash_string` return value instead (https://github.com/ansible-collections/community.mysql/pull/629).
- mysql_user - the ``user`` alias of the ``name`` argument has been deprecated and will be removed in collection version 5.0.0. Use the ``name`` argument instead.

community.network
~~~~~~~~~~~~~~~~~

- This collection and all content in it is unmaintained and deprecated (https://forum.ansible.com/t/8030). If you are interested in maintaining parts of the collection, please copy them to your own repository, and tell others about in the Forum discussion. See the `collection creator path <https://docs.ansible.com/ansible/devel/dev_guide/developing_collections_path.html>`__ for details.

community.routeros
~~~~~~~~~~~~~~~~~~

- The collection deprecates support for all Ansible/ansible-base/ansible-core versions that are currently End of Life, `according to the ansible-core support matrix <https://docs.ansible.com/ansible-core/devel/reference_appendices/release_and_maintenance.html#ansible-core-support-matrix>`__. This means that the next major release of the collection will no longer support Ansible 2.9, ansible-base 2.10, ansible-core 2.11, ansible-core 2.12, ansible-core 2.13, and ansible-core 2.14.

community.sops
~~~~~~~~~~~~~~

- The collection deprecates support for all Ansible/ansible-base/ansible-core versions that are currently End of Life, `according to the ansible-core support matrix <https://docs.ansible.com/ansible-core/devel/reference_appendices/release_and_maintenance.html#ansible-core-support-matrix>`__. This means that the next major release of the collection will no longer support Ansible 2.9, ansible-base 2.10, ansible-core 2.11, ansible-core 2.12, ansible-core 2.13, and ansible-core 2.14.

community.vmware
~~~~~~~~~~~~~~~~

- vmware_cluster - the module has been deprecated and will be removed in community.vmware 6.0.0 (https://github.com/ansible-collections/community.vmware/pull/2143).
- vmware_cluster_dpm - the module has been deprecated and will be removed in community.vmware 6.0.0 (https://github.com/ansible-collections/community.vmware/pull/2217).
- vmware_cluster_drs - the module has been deprecated and will be removed in community.vmware 6.0.0 (https://github.com/ansible-collections/community.vmware/pull/2136).
- vmware_cluster_drs_recommendations - the module has been deprecated and will be removed in community.vmware 6.0.0 (https://github.com/ansible-collections/community.vmware/pull/2218).
- vmware_cluster_vcls - the module has been deprecated and will be removed in community.vmware 6.0.0 (https://github.com/ansible-collections/community.vmware/pull/2156).

Removed Features (previously deprecated)
----------------------------------------

- The ``inspur.sm`` collection was considered unmaintained and has been removed from Ansible 11 (`https://forum.ansible.com/t/2854 <https://forum.ansible.com/t/2854>`__).
  Users can still install this collection with ``ansible-galaxy collection install inspur.sm``.
- The collection ``t_systems_mms.icinga_director`` has been completely removed from Ansible.
  It has been renamed to ``telekom_mms.icinga_director``.
  ``t_systems_mms.icinga_director`` has been replaced by deprecated redirects to ``telekom_mms.icinga_director`` in Ansible 9.0.0.
  Please update your FQCNs from ``t_systems_mms.icinga_director`` to ``telekom_mms.icinga_director``.
- The deprecated ``frr.frr`` collection has been removed (`https://forum.ansible.com/t/6243 <https://forum.ansible.com/t/6243>`__).
- The deprecated ``ngine_io.exoscale`` collection has been removed (`https://forum.ansible.com/t/2572 <https://forum.ansible.com/t/2572>`__).
- The deprecated ``openvswitch.openvswitch`` collection has been removed (`https://forum.ansible.com/t/6245 <https://forum.ansible.com/t/6245>`__).

Ansible-core
~~~~~~~~~~~~

- Play - removed deprecated ``ROLE_CACHE`` property in favor of ``role_cache``.
- Remove deprecated `VariableManager._get_delegated_vars` method (https://github.com/ansible/ansible/issues/82950)
- Removed Python 3.10 as a supported version on the controller. Python 3.11 or newer is required.
- Removed support for setting the ``vars`` keyword to lists of dictionaries. It is now required to be a single dictionary.
- loader - remove deprecated non-inclusive words (https://github.com/ansible/ansible/issues/82947).
- paramiko_ssh - removed deprecated ssh_args from the paramiko_ssh connection plugin (https://github.com/ansible/ansible/issues/82939).
- paramiko_ssh - removed deprecated ssh_common_args from the paramiko_ssh connection plugin (https://github.com/ansible/ansible/issues/82940).
- paramiko_ssh - removed deprecated ssh_extra_args from the paramiko_ssh connection plugin (https://github.com/ansible/ansible/issues/82941).
- play_context - remove deprecated PlayContext.verbosity property (https://github.com/ansible/ansible/issues/82945).
- utils/listify - remove deprecated 'loader' argument from listify_lookup_plugin_terms API (https://github.com/ansible/ansible/issues/82949).

community.docker
~~~~~~~~~~~~~~~~

- The collection no longer supports ansible-core 2.11, 2.12, 2.13, and 2.14. You need ansible-core 2.15.0 or newer to use community.docker 4.x.y (https://github.com/ansible-collections/community.docker/pull/971).
- The docker_compose module has been removed. Please migrate to community.docker.docker_compose_v2 (https://github.com/ansible-collections/community.docker/pull/971).
- docker_container - the ``ignore_image`` option has been removed. Use ``image: ignore`` in ``comparisons`` instead (https://github.com/ansible-collections/community.docker/pull/971).
- docker_container - the ``purge_networks`` option has been removed. Use ``networks: strict`` in ``comparisons`` instead and make sure that ``networks`` is specified (https://github.com/ansible-collections/community.docker/pull/971).
- various modules and plugins - remove the ``ssl_version`` option (https://github.com/ansible-collections/community.docker/pull/971).

community.general
~~~~~~~~~~~~~~~~~

- The consul_acl module has been removed. Use community.general.consul_token and/or community.general.consul_policy instead (https://github.com/ansible-collections/community.general/pull/8921).
- The hipchat callback plugin has been removed. The hipchat service has been discontinued and the self-hosted variant has been End of Life since 2020 (https://github.com/ansible-collections/community.general/pull/8921).
- The redhat module utils has been removed (https://github.com/ansible-collections/community.general/pull/8921).
- The rhn_channel module has been removed (https://github.com/ansible-collections/community.general/pull/8921).
- The rhn_register module has been removed (https://github.com/ansible-collections/community.general/pull/8921).
- consul - removed the ``ack_params_state_absent`` option. It had no effect anymore (https://github.com/ansible-collections/community.general/pull/8918).
- ejabberd_user - removed the ``logging`` option (https://github.com/ansible-collections/community.general/pull/8918).
- gitlab modules - remove basic auth feature (https://github.com/ansible-collections/community.general/pull/8405).
- proxmox_kvm - removed the ``proxmox_default_behavior`` option. Explicitly specify the old default values if you were using ``proxmox_default_behavior=compatibility``, otherwise simply remove it (https://github.com/ansible-collections/community.general/pull/8918).
- redhat_subscriptions - removed the ``pool`` option. Use ``pool_ids`` instead (https://github.com/ansible-collections/community.general/pull/8918).

community.grafana
~~~~~~~~~~~~~~~~~

- removed check and handling of mangled api key in `grafana_dashboard` lookup
- removed deprecated `message` argument in `grafana_dashboard`

community.okd
~~~~~~~~~~~~~

- k8s - Support for ``merge_type=json`` has been removed in version 4.0.0. Please use ``kubernetes.core.k8s_json_patch`` instead (https://github.com/openshift/community.okd/pull/226).

community.routeros
~~~~~~~~~~~~~~~~~~

- The collection no longer supports Ansible 2.9, ansible-base 2.10, ansible-core 2.11, ansible-core 2.12, ansible-core 2.13, and ansible-core 2.14. If you need to continue using End of Life versions of Ansible/ansible-base/ansible-core, please use community.routeros 2.x.y (https://github.com/ansible-collections/community.routeros/pull/318).

community.sops
~~~~~~~~~~~~~~

- The collection no longer supports Ansible 2.9, ansible-base 2.10, ansible-core 2.11, ansible-core 2.12, ansible-core 2.13, and ansible-core 2.14. If you need to continue using End of Life versions of Ansible/ansible-base/ansible-core, please use community.sops 1.x.y (https://github.com/ansible-collections/community.sops/pull/206).

kubernetes.core
~~~~~~~~~~~~~~~

- k8s - Support for ``merge_type=json`` has been removed in version 4.0.0. Please use ``kubernetes.core.k8s_json_patch`` instead (https://github.com/ansible-collections/kubernetes.core/pull/722).
- k8s_exec - the previously deprecated ``result.return_code`` return value has been removed, consider using ``result.rc`` instead (https://github.com/ansible-collections/kubernetes.core/pull/726).
- module_utils/common.py - the previously deprecated ``K8sAnsibleMixin`` class has been removed (https://github.com/ansible-collections/kubernetes.core/pull/726).
- module_utils/common.py - the previously deprecated ``configuration_digest()`` function has been removed (https://github.com/ansible-collections/kubernetes.core/pull/726).
- module_utils/common.py - the previously deprecated ``get_api_client()`` function has been removed (https://github.com/ansible-collections/kubernetes.core/pull/726).
- module_utils/common.py - the previously deprecated ``unique_string()`` function has been removed (https://github.com/ansible-collections/kubernetes.core/pull/726).

Security Fixes
--------------

Ansible-core
~~~~~~~~~~~~

- include_vars action - Ensure that result masking is correctly requested when vault-encrypted files are read. (CVE-2024-8775)
- task result processing - Ensure that action-sourced result masking (``_ansible_no_log=True``) is preserved. (CVE-2024-8775)
- user action won't allow ssh-keygen, chown and chmod to run on existing ssh public key file, avoiding traversal on existing symlinks (CVE-2024-9902).

Bugfixes
--------

Ansible-core
~~~~~~~~~~~~

- -> runas become - Generate new token for the SYSTEM token to use for become. This should result in the full SYSTEM token being used and problems starting the process that fails with ``The process creation has been blocked``.
- Add a version ceiling constraint for pypsrp to avoid potential breaking changes in the 1.0.0 release.
- Add descriptions for ``ansible-galaxy install --help` and ``ansible-galaxy role|collection install --help``.
- Avoid truncating floats when casting into int, as it can lead to truncation and unexpected results. 0.99999 will be 0, not 1.
- COLOR_SKIP will not alter "included" events color display anymore.
- Callbacks now correctly get the resolved connection plugin name as the connection used.
- Darwin - add unit tests for Darwin hardware fact gathering.
- Errors now preserve stacked error messages even when YAML is involved.
- Fix ``SemanticVersion.parse()`` to store the version string so that ``__repr__`` reports it instead of ``None`` (https://github.com/ansible/ansible/pull/83831).
- Fix a traceback when an environment variable contains certain special characters (https://github.com/ansible/ansible/issues/83498)
- Fix an issue when setting a plugin name from an unsafe source resulted in ``ValueError: unmarshallable object`` (https://github.com/ansible/ansible/issues/82708)
- Fix an issue where registered variable was not available for templating in ``loop_control.label`` on skipped looped tasks (https://github.com/ansible/ansible/issues/83619)
- Fix disabling SSL verification when installing collections and roles from git repositories. If ``--ignore-certs`` isn't provided, the value for the ``GALAXY_IGNORE_CERTS`` configuration option will be used (https://github.com/ansible/ansible/issues/83326).
- Fix for ``meta`` tasks breaking host/fork affinity with ``host_pinned`` strategy (https://github.com/ansible/ansible/issues/83294)
- Fix handlers not being executed in lockstep using the linear strategy in some cases (https://github.com/ansible/ansible/issues/82307)
- Fix rapid memory usage growth when notifying handlers using the ``listen`` keyword (https://github.com/ansible/ansible/issues/83392)
- Fix the task attribute ``resolved_action`` to show the FQCN instead of ``None`` when ``action`` or ``local_action`` is used in the playbook.
- Fix using ``module_defaults`` with ``local_action``/``action`` (https://github.com/ansible/ansible/issues/81905).
- Fix using the current task's directory for looking up relative paths within roles (https://github.com/ansible/ansible/issues/82695).
- Improve performance on large inventories by reducing the number of implicit meta tasks.
- Remove deprecated config options DEFAULT_FACT_PATH, DEFAULT_GATHER_SUBSET, and DEFAULT_GATHER_TIMEOUT in favor of setting ``fact_path``, ``gather_subset`` and ``gather_timeout`` as ``module_defaults`` for ``ansible.builtin.setup``.
  These will apply to both the ``gather_facts`` play keyword, and any ``ansible.builtin.setup`` tasks.
  To configure these options only for the ``gather_facts`` keyword, set these options as play keywords also.
- Set LANGUAGE environment variable is set to a non-English locale (https://github.com/ansible/ansible/issues/83608).
- Use the requested error message in the ansible.module_utils.facts.timeout timeout function instead of hardcoding one.
- ``ansible-galaxy install --help`` - Fix the usage text and document that the requirements file passed to ``-r`` can include collections and roles.
- ``ansible-galaxy role install`` - update the default timeout to download archive URLs from 20 seconds to 60 (https://github.com/ansible/ansible/issues/83521).
- ``end_host`` - fix incorrect return code when executing ``end_host`` in the ``rescue`` section (https://github.com/ansible/ansible/issues/83447)
- ``package``/``dnf`` action plugins - provide the reason behind the failure to gather the ``ansible_pkg_mgr`` fact to identify the package backend
- addressed issue of trailing text been ignored, non-ASCII characters are parsed, enhance white space handling and fixed overly permissive issue of human_to_bytes filter(https://github.com/ansible/ansible/issues/82075)
- ansible-config will now properly template defaults before dumping them.
- ansible-doc - fixed "inicates" typo in output
- ansible-doc - format top-level descriptions with multiple paragraphs as multiple paragraphs, instead of concatenating them (https://github.com/ansible/ansible/pull/83155).
- ansible-doc - handle no_fail condition for role.
- ansible-doc - make colors configurable.
- ansible-galaxy collection install - remove old installation info when installing collections (https://github.com/ansible/ansible/issues/83182).
- ansible-galaxy role install - fix symlinks (https://github.com/ansible/ansible/issues/82702, https://github.com/ansible/ansible/issues/81965).
- ansible-test - Enable the ``sys.unraisablehook`` work-around for the ``pylint`` sanity test on Python 3.11. Previously the work-around was only enabled for Python 3.12 and later. However, the same issue has been discovered on Python 3.11.
- ansible-test - The ``pylint`` sanity test now includes the controller/target context of files when grouping them. This allows the ``--py-version`` option to be passed to ``pylint`` to indicate the minimum supported Python version for each test context, preventing ``pylint`` from defaulting to the Python version used to invoke the test.
- ansible-test action-plugin-docs - Fix to check for sidecar documentation for action plugins
- ansible_managed restored it's 'templatability' by ensuring the possible injection routes are cut off earlier in the process.
- apt - report changed=True when some packages are being removed (https://github.com/ansible/ansible/issues/46314).
- apt_* - add more info messages raised while updating apt cache (https://github.com/ansible/ansible/issues/77941).
- assemble - update argument_spec with 'decrypt' option which is required by action plugin (https://github.com/ansible/ansible/issues/80840).
- atomic_move - fix using the setgid bit on the parent directory when creating files (https://github.com/ansible/ansible/issues/46742, https://github.com/ansible/ansible/issues/67177).
- config, restored the ability to set module compression via a variable
- connection plugins using the 'extras' option feature would need variables to match the plugin's loaded name, sometimes requiring fqcn, which is not the same as the documented/declared/expected variables. Now we fall back to the 'basename' of the fqcn, but plugin authors can still set the expected value directly.
- copy - mtime/atime not updated. Fix now update mtime/atime(https://github.com/ansible/ansible/issues/83013)
- csvfile lookup - give an error when no search term is provided using modern config syntax (https://github.com/ansible/ansible/issues/83689).
- debconf - fix normalization of value representation for boolean vtypes in new packages (https://github.com/ansible/ansible/issues/83594)
- debconf - set empty password values (https://github.com/ansible/ansible/issues/83214).
- delay keyword is now a float, matching the underlying 'time' API and user expectations.
- display - warn user about empty log filepath (https://github.com/ansible/ansible/issues/79959).
- display now does a better job of mapping warnings/errors to the proper log severity when using ansible.log. We still use color as a fallback mapping (now prioritiezed by severity) but mostly rely on it beind directly set by warnning/errors calls.
- distro package - update the distro package version from 1.8.0 to 1.9.0  (https://github.com/ansible/ansible/issues/82935)
- dnf - Ensure that we are handling DownloadError properly in the dnf module
- dnf - Substitute variables in DNF cache path (https://github.com/ansible/ansible/pull/80094).
- dnf - fix an issue where two packages of the same ``evr`` but different arch failed to install (https://github.com/ansible/ansible/issues/83406)
- dnf - honor installroot for ``cachedir``, ``logdir`` and ``persistdir``
- dnf - perform variable substitutions in ``logdir`` and ``persistdir``
- dnf, dnf5 - fix for installing a set of packages by specifying them using a wildcard character (https://github.com/ansible/ansible/issues/83373)
- dnf5 - fix traceback when ``enable_plugins``/``disable_plugins`` is used on ``python3-libdnf5`` versions that do not support this functionality
- dnf5 - re-introduce the ``state: installed`` alias to ``state: present`` (https://github.com/ansible/ansible/issues/83960)
- dnf5 - replace removed API calls
- ensure we have logger before we log when we have increased verbosity.
- facts - `support_discard` now returns `0` if either `discard_granularity` or `discard_max_hw_bytes` is zero; otherwise it returns the value of `discard_granularity`, as before (https://github.com/ansible/ansible/pull/83480).
- facts - add a generic detection for VMware in product name.
- facts - add facts about x86_64 flags to detect microarchitecture (https://github.com/ansible/ansible/issues/83331).
- facts - skip if distribution file path is directory, instead of raising error (https://github.com/ansible/ansible/issues/84006).
- fetch - add error message when using ``dest`` with a trailing slash that becomes a local directory - https://github.com/ansible/ansible/issues/82878
- file - retrieve the link's full path when hard linking a soft link with follow (https://github.com/ansible/ansible/issues/33911).
- fixed the issue of creating user directory using tilde(~) always reported "changed".(https://github.com/ansible/ansible/issues/82490)
- fixed unit test test_borken_cowsay to address mock not been properly applied when existing unix system already have cowsay installed.
- freebsd - refactor dmidecode fact gathering code for simplicity.
- freebsd - update disk and slices regex for fact gathering (https://github.com/ansible/ansible/pull/82081).
- get_url - Verify checksum using tmpsrc, not dest (https://github.com/ansible/ansible/pull/64092)
- git - check if git version is available or not before using it for comparison (https://github.com/ansible/ansible/issues/72321).
- include_tasks - Display location when attempting to load a task list where ``include_*`` did not specify any value - https://github.com/ansible/ansible/issues/83874
- known_hosts - the returned module invocation now accurately reflects the module arguments.
- linear strategy now provides a properly templated task name to the v2_runner_on_started callback event.
- linear strategy: fix handlers included via ``include_tasks`` handler to be executed in lockstep (https://github.com/ansible/ansible/issues/83019)
- linux - remove extraneous get_bin_path API call.
- local - handle error while parsing values in ini files (https://github.com/ansible/ansible/issues/82717).
- lookup - Fixed examples of csv lookup plugin (https://github.com/ansible/ansible/issues/83031).
- module_defaults - do not display action/module deprecation warnings when using an action_group that contains a deprecated plugin (https://github.com/ansible/ansible/issues/83490).
- module_utils atomic_move (used by most file based modules), now correctly handles permission copy and setting mtime correctly across all paths
- package_facts - apk fix when cache is empty (https://github.com/ansible/ansible/issues/83126).
- package_facts - no longer fails silently when the selected package manager is unable to list packages.
- package_facts - returns the correct warning when package listing fails.
- persistent connection plugins - The correct Ansible persistent connection helper is now always used. Previously, the wrong script could be used, depending on the value of the ``PATH`` environment variable. As a result, users were sometimes required to set ``ANSIBLE_CONNECTION_PATH`` to use the correct script.
- powershell - Implement more robust deletion mechanism for C# code compilation temporary files. This should avoid scenarios where the underlying temporary directory may be temporarily locked by antivirus tools or other IO problems. A failure to delete one of these temporary directories will result in a warning rather than an outright failure.
- powershell - Improve CLIXML decoding to decode all control characters and unicode characters that are encoded as surrogate pairs.
- psrp - Fix bug when attempting to fetch a file path that contains special glob characters like ``[]``
- replace - Updated before/after example (https://github.com/ansible/ansible/issues/83390).
- runtime-metadata sanity test - do not crash on deprecations if ``galaxy.yml`` contains an empty ``version`` field (https://github.com/ansible/ansible/pull/83831).
- service - fix order of CLI arguments on FreeBSD (https://github.com/ansible/ansible/pull/81377).
- service_facts - don't crash if OpenBSD rcctl variable contains '=' character (https://github.com/ansible/ansible/issues/83457)
- service_facts will now detect failed services more accurately across systemd implementations.
- setup module (fact gathering), added fallbcak code path to handle mount fact gathering in linux when threading is not available
- setup/gather_facts will skip missing ``sysctl`` instead of being a fatal error (https://github.com/ansible/ansible/pull/81297).
- shell plugin - properly quote all needed components of shell commands (https://github.com/ansible/ansible/issues/82535)
- ssh - Fix bug when attempting to fetch a file path with characters that should be quoted when using the ``piped`` transfer method
- support the countme option when using yum_repository
- systemd - extend systemctl is-enabled check to handle "enabled-runtime" (https://github.com/ansible/ansible/pull/77754).
- systemd facts - handle AttributeError raised while gathering facts on non-systemd hosts.
- systemd_service - handle mask operation failure (https://github.com/ansible/ansible/issues/81649).
- templating hostvars under native jinja will not cause serialization errors anymore.
- the raw arguments error now just displays the short names of modules instead of every possible variation
- unarchive - Better handling of files with an invalid timestamp in zip file (https://github.com/ansible/ansible/issues/81092).
- unarchive - trigger change when size and content differ when other properties are unchanged (https://github.com/ansible/ansible/pull/83454).
- unsafe data - Address an incompatibility when iterating or getting a single index from ``AnsibleUnsafeBytes``
- unsafe data - Address an incompatibility with ``AnsibleUnsafeText`` and ``AnsibleUnsafeBytes`` when pickling with ``protocol=0``
- unsafe data - Enable directly using ``AnsibleUnsafeText`` with Python ``pathlib`` (https://github.com/ansible/ansible/issues/82414)
- uri - deprecate 'yes' and 'no' value for 'follow_redirects' parameter.
- user action will now require O(force) to overwrite the public part of an ssh key when generating ssh keys, as was already the case for the private part.
- user module now avoids changing ownership of files symlinked in provided home dir skeleton
- vault - handle vault password file value when it is directory (https://github.com/ansible/ansible/issues/42960).
- vault.is_encrypted_file is now optimized to be called in runtime and not for being called in tests
- vault_encrypted test documentation, name and examples have been fixed, other parts were clarified
- winrm - Add retry after exceeding commands per user quota that can occur in loops and action plugins running multiple commands.

amazon.aws
~~~~~~~~~~

- aws_ec2 - fix SSM inventory collection for multiple (>40) hosts  (https://github.com/ansible-collections/amazon.aws/pull/2227).
- backup_plan_info - Bugfix to enable getting info of all backup plans (https://github.com/ansible-collections/amazon.aws/pull/2083).
- cloudformation - Fix bug where termination protection is not updated when create_changeset=true is used for stack updates (https://github.com/ansible-collections/amazon.aws/pull/2391).
- cloudwatch_metric_alarm - Fix idempotency when creating cloudwatch metric alarm without dimensions (https://github.com/ansible-collections/amazon.aws/pull/1865).
- ec2_instance - Fix issue where EC2 instance module failed to apply security groups when both ``network`` and ``vpc_subnet_id`` were specified, caused by passing ``None`` to discover_security_groups() (https://github.com/ansible-collections/amazon.aws/pull/2488).
- ec2_instance - do not ignore IPv6 addresses when a single network interface is specified (https://github.com/ansible-collections/amazon.aws/pull/1979).
- ec2_instance - fix state processing when exact_count is used (https://github.com/ansible-collections/amazon.aws/pull/1659).
- ec2_security_group - Fix the diff mode issue when creating a security group containing a rule with a managed prefix list (https://github.com/ansible-collections/amazon.aws/issues/2373).
- ec2_vol - output volume informations when volume exists in check mode (https://github.com/ansible-collections/amazon.aws/pull/2133).
- ec2_vpc_net - handle ipv6_cidr ``false`` and no Ipv6CidrBlockAssociationSet in vpc (https://github.com/ansible-collections/amazon.aws/pull/2374).
- iam_role - fixes ``EntityAlreadyExists`` exception when ``create_instance_profile`` was set to ``false`` and the instance profile already existed (https://github.com/ansible-collections/amazon.aws/issues/2102).
- iam_role - fixes issue where IAM instance profiles were created when ``create_instance_profile`` was set to ``false`` (https://github.com/ansible-collections/amazon.aws/issues/2281).
- lambda - Remove non UTF-8 data (contents of Lambda ZIP file) from the module output to avoid Ansible error (https://github.com/ansible-collections/amazon.aws/issues/2386).
- rds_cluster - Fix issue occurring when updating RDS cluster domain (https://github.com/ansible-collections/amazon.aws/issues/2390).
- rds_cluster - Limit params sent to api call to DBClusterIdentifier when using state started or stopped (https://github.com/ansible-collections/amazon.aws/issues/2197).
- route53 - modify the return value to return diff only when ``module._diff`` is set to true (https://github.com/ansible-collections/amazon.aws/pull/2136).
- s3_bucket - Do not use default region as location constraint when creating bucket on ceph cluster (https://github.com/ansible-collections/amazon.aws/issues/2420).
- s3_bucket - Fixes Python 3.7 compilation issue due to addition of typing information (https://github.com/ansible-collections/amazon.aws/issues/2287).
- s3_bucket - catch ``UnsupportedArgument`` when calling API ``GetBucketAccelerationConfig`` on region where it is not supported (https://github.com/ansible-collections/amazon.aws/issues/2180).
- s3_bucket - change the default behaviour of the new ``accelerate_enabled`` option to only update the configuration if explicitly passed (https://github.com/ansible-collections/amazon.aws/issues/2220).
- s3_bucket - fixes ``MethodNotAllowed`` exceptions caused by fetching transfer acceleration state in regions that don't support it (https://github.com/ansible-collections/amazon.aws/issues/2266).
- s3_bucket - fixes ``TypeError: cannot unpack non-iterable NoneType object`` errors related to bucket versioning, policies, tags or encryption (https://github.com/ansible-collections/amazon.aws/pull/2228).
- s3_object - Fixed an issue where ``max_keys`` was not respected (https://github.com/ansible-collections/amazon.aws/pull/2328).
- s3_object - fixed issue which was causing ``MemoryError`` exceptions when downloading large files (https://github.com/ansible-collections/amazon.aws/issues/2107).

ansible.netcommon
~~~~~~~~~~~~~~~~~

- Fix get api call during scp with libssh.
- Handle sftp error messages for file not present for routerOS.
- The v6.1.2 release introduced a change in cliconfbase's edit_config() signature which broke many platform cliconfs. This patch release reverts that change.
- Updated the error message for the content_templates parser to include the correct parser name and detailed error information.

ansible.posix
~~~~~~~~~~~~~

- Bugfix in the documentation regarding the path option for authorised_key(https://github.com/ansible-collections/ansible.posix/issues/483).
- acl - Fixed to set ACLs on paths mounted with NFS version 4 correctly (https://github.com/ansible-collections/ansible.posix/issues/240).
- backport - Drop ansible-core 2.14 and set 2.15 minimum version (https://github.com/ansible-collections/ansible.posix/issues/578).
- mount - Handle ``boot`` option on Linux, NetBSD and OpenBSD correctly (https://github.com/ansible-collections/ansible.posix/issues/364).
- seboolean - make it work with disabled SELinux
- skippy - Revert removal of skippy plugin. It will be removed in version 2.0.0 (https://github.com/ansible-collections/ansible.posix/issues/573).
- synchronize - maintain proper formatting of the remote paths (https://github.com/ansible-collections/ansible.posix/pull/361).
- sysctl - fix sysctl to work properly on symlinks (https://github.com/ansible-collections/ansible.posix/issues/111).

ansible.utils
~~~~~~~~~~~~~

- keep_keys - Fixes issue where all keys are removed when data is passed in as a dict.
- keep_keys - Fixes keep_keys filter to retain the entire node when a key match occurs, rather than just the leaf node values.

ansible.windows
~~~~~~~~~~~~~~~

- setup - Better handle orphaned users when attempting to retrieve ``ansible_machine_id`` - https://github.com/ansible-collections/ansible.windows/issues/606
- setup - Provide WMI/CIM fallback for facts that rely on SMBIOS when that is unavailable
- win_owner - Try to enable extra privileges if available to set the owner even when the caller may not have explicit rights to do so normally - https://github.com/ansible-collections/ansible.windows/issues/633
- win_powershell - Fix up depth handling on ``$Ansible.Result`` when using a custom ``executable`` - https://github.com/ansible-collections/ansible.windows/issues/642
- win_powershell - increase open timeout for ``executable`` parameter to prevent exceptions on first-run or slower targets. (https://github.com/ansible-collections/ansible.windows/issues/644).
- win_updates - Base64 encode the update wrapper and payload to prevent locale-specific encoding issues.
- win_updates - Handle race condition when ``Wait-Process`` did not handle when the process had ended - https://github.com/ansible-collections/ansible.windows/issues/623

arista.eos
~~~~~~~~~~

- Adds a missing word in the 'bgp client-to-client reflection' command in eos_bgp_global module.
- Ensure IPv6 static route definitions are correctly filtered during facts gathering.
- Fixes a typo in always-compare-med attribute in eos_bgp_global module.
- Handles exception when translating an unknown port to its service name.
- This fix make sure to fetch timer with `lldp` string at the start.
- Update integration tests for parse operations to ensure that ordering or address family (AF) does not affect assertions.
- Update the filter to accurately retrieve relevant static route configurations.

check_point.mgmt
~~~~~~~~~~~~~~~~

- module_utils/checkpoint.py - Remove usage of CertificateError causing failures in ansible-core 2.17.

chocolatey.chocolatey
~~~~~~~~~~~~~~~~~~~~~

- win_chocolatey - task crashes if PATH contains multiple choco.exe on the target machine

cisco.aci
~~~~~~~~~

- Remove duplicate alias name for attribute epg in aci_epg_subnet module

cisco.ios
~~~~~~~~~

- bgp_global - fix ebgp_multihop recognnition and hop_count settings
- ios_acls - fix incorrect mapping of port 135/udp to msrpc.
- ios_bgp_address_family - Add support for maximum-paths configuration.
- ios_bgp_address_family - Add support for maximum-secondary-paths configuration.
- ios_bgp_address_family - fix parsing of password_options while gathering password configuration from appliance.
- ios_bgp_global - fix parsing of password_options while gathering password configuration from appliance.
- ios_interfaces - Fixes rendering of FiftyGigabitEthernet as it was wrongly rendering FiftyGigabitEthernet as FiveGigabitEthernet.
- ios_l3_interfaces - Fix gathering wrong facts for source interface in ipv4.
- ios_service - Add tcp_small_servers and udp_small_servers attributes, to generate configuration.
- ios_service - Fix a typo causing log timestamps not being configurable
- ios_service - Fix timestamps attribute, to generate right configuration.
- ios_snmp_server - Fixes an issue where enabling the read-only (ro) attribute in communities was not idempotent.
- ios_static_routes - Fix gathering facts by properly distinguising routes.
- ios_static_routes - Fix processing of metric_distance as it was wrongly populated under the forward_router_address attribute.
- ios_vlans - Make the module fail when vlan name is longer than 32 characters with configuration as VTPv1 and VTPv2.
- l2_interfaces - If a large number of VLANs are affected, the configuration will now be correctly split into several commands.
- snmp_server - Fix configuration command for snmp-server host.
- snmp_server - Fix wrong syntax of snmp-server host command generation.
- static_routes - add TenGigabitEthernet as valid interface

cisco.iosxr
~~~~~~~~~~~

- iosxr_acls_facts - Fix incorrect rendering of some acl facts causing errors.
- iosxr_static_routes - Fix incorrect handling of the vrf keyword between the destination address and next-hop interface in both global and VRF contexts for IPv4 and IPv6 static_route configurations.

cisco.ise
~~~~~~~~~

- Added main.yml to aws_deployment role
- Collection not compatible with ansible.utils 5.x.y
- Getting deployment info for entire deployment does not work
- Update min_ansible_version to 2.15.0 in runtime.yml and roles
- cisco.ise.pan_ha object has no attribute 'enable_pan_ha'
- cisco.ise.support_bundle_download keeps failing after downloading the file
- endpoint_group - add missing parameter parentID.
- mnt_session_active_list_info - fix response xml.
- network_device - mask param can be string or int, cast to int at the end.
- reservation - remove duplicate parameter.
- support_bundle_download - remove duplicate parameter.
- trusted_certificate - fix comparison between request and current object.

cisco.meraki
~~~~~~~~~~~~

- Ansible utils requirements updated.
- cisco.meraki.networks_clients_info - incorrect API endpoint, fixing info module.
- cisco.meraki.networks_switch_stacks delete stack not working, fixing path parameters.

cisco.mso
~~~~~~~~~

- Fix to avoid making updates to attributes that are not provided which could lead to removal of configuration in mso_schema_template_bd
- Fix to avoid making updates to attributes that are not provided which could lead to removal of configuration in mso_schema_template_vrf
- Fix to be able to reference APIC only L3Out in mso_schema_site_external_epg

cisco.nxos
~~~~~~~~~~

- acls - Fix lookup of range port conversion from int to string to allow strings (https://github.com/ansible-collections/cisco.nxos/pull/888).
- facts - Fixes issue where the LLDP neighbor information returns an error when empty.
- nxos_l3_interfaces - fail if encapsulation exists on a different sub-interface.
- nxos_snmp_server - correctly render entity traps (https://github.com/ansible-collections/cisco.nxos/issues/820).
- nxos_static_routes - correctly generate command when track parameter is specified.

cloud.common
~~~~~~~~~~~~

- module_utils/turbo/server - Ensure all import statements in run_as_lookup_plugin() are in a try/except block (https://github.com/ansible-collections/cloud.common/pull/143).

community.aws
~~~~~~~~~~~~~

- autoscaling_instance_refresh - Fix typo in module ``exit_json`` (https://github.com/ansible-collections/community.aws/issues/2019).
- ecs_taskdefinition - Avoid throttling exceptions on task definitions with a large number of revisions by using the retry mechanism (https://github.com/ansible-collections/community.aws/issues/2123).
- ecs_taskdefinition - avoid throttling exceptions on task definitions with a large number of revisions by using the retry mechanism (https://github.com/ansible-collections/community.aws/issues/2123).

community.crypto
~~~~~~~~~~~~~~~~

- When using cryptography >= 43.0.0, use offset-aware ``datetime.datetime`` objects (with timezone UTC) instead of offset-naive UTC timestamps for the ``InvalidityDate`` X.509 CRL extension (https://github.com/ansible-collections/community.crypto/issues/726, https://github.com/ansible-collections/community.crypto/pull/730).
- acme_* modules - when querying renewal information, make sure to insert a slash between the base URL and the certificate identifier (https://github.com/ansible-collections/community.crypto/issues/801, https://github.com/ansible-collections/community.crypto/pull/802).
- acme_* modules - when using the OpenSSL backend, explicitly use the UTC timezone in Python code (https://github.com/ansible-collections/community.crypto/pull/811).
- acme_certificate - fix authorization failure when CSR contains SANs with mixed case (https://github.com/ansible-collections/community.crypto/pull/803).
- time module utils - fix conversion of naive ``datetime`` objects to UNIX timestamps for Python 3 (https://github.com/ansible-collections/community.crypto/issues/808, https://github.com/ansible-collections/community.crypto/pull/810).
- various modules - pass absolute paths to ``module.atomic_move()`` (https://github.com/ansible/ansible/issues/83950, https://github.com/ansible-collections/community.crypto/pull/799).

community.dns
~~~~~~~~~~~~~

- Update Public Suffix List.

community.docker
~~~~~~~~~~~~~~~~

- docker_compose - make sure that the module uses the ``api_version`` parameter (https://github.com/ansible-collections/community.docker/pull/881).
- docker_compose_v2 - handle yet another random unstructured error output from pre-2.29.0 Compose versions (https://github.com/ansible-collections/community.docker/issues/948, https://github.com/ansible-collections/community.docker/pull/949).
- docker_compose_v2 - improve parsing of dry-run image build operations from JSON events (https://github.com/ansible-collections/community.docker/issues/975, https://github.com/ansible-collections/community.docker/pull/976).
- docker_compose_v2 - make sure that services provided in ``services`` are appended to the command line after ``--`` and not before it (https://github.com/ansible-collections/community.docker/pull/942).
- docker_compose_v2* modules - fix parsing of skipped pull messages for Docker Compose 2.28.x (https://github.com/ansible-collections/community.docker/issues/911, https://github.com/ansible-collections/community.docker/pull/916).
- docker_compose_v2* modules - there was no check to make sure that one of ``project_src`` and ``definition`` is provided. The modules crashed if none were provided (https://github.com/ansible-collections/community.docker/issues/885, https://github.com/ansible-collections/community.docker/pull/886).
- docker_compose_v2* modules, docker_image_build - provide better error message when required fields are not present in ``docker version`` or ``docker info`` output. This can happen if Podman is used instead of Docker (https://github.com/ansible-collections/community.docker/issues/891, https://github.com/ansible-collections/community.docker/pull/935).
- docker_compose_v2*, docker_stack*, docker_image_build modules - using ``cli_context`` no longer leads to an invalid parameter combination being passed to the corresponding Docker CLI tool, unless ``docker_host`` is also provided. Combining ``cli_context`` and ``docker_host`` is no longer allowed (https://github.com/ansible-collections/community.docker/issues/892, https://github.com/ansible-collections/community.docker/pull/895).
- docker_compose_v2_run - make sure to sanitize ``labels`` before sending them to the Docker Daemon (https://github.com/ansible-collections/community.docker/pull/985).
- docker_config - make sure to sanitize ``labels`` before sending them to the Docker Daemon (https://github.com/ansible-collections/community.docker/pull/985).
- docker_container - fix idempotency if ``network_mode=default`` and Docker 26.1.0 or later is used. There was a breaking change in Docker 26.1.0 regarding normalization of ``NetworkMode`` (https://github.com/ansible-collections/community.docker/issues/934, https://github.com/ansible-collections/community.docker/pull/936).
- docker_container - fix possible infinite loop if ``removal_wait_timeout`` is set (https://github.com/ansible-collections/community.docker/pull/922).
- docker_container - restore behavior of the module from community.docker 2.x.y that passes the first network to the Docker Deamon while creating the container (https://github.com/ansible-collections/community.docker/pull/933).
- docker_image_build - fix ``--output`` parameter composition for ``type=docker`` and ``type=image`` (https://github.com/ansible-collections/community.docker/issues/946, https://github.com/ansible-collections/community.docker/pull/947).
- docker_network - make sure to sanitize ``labels`` before sending them to the Docker Daemon (https://github.com/ansible-collections/community.docker/pull/985).
- docker_node - make sure to sanitize ``labels`` before sending them to the Docker Daemon (https://github.com/ansible-collections/community.docker/pull/985).
- docker_prune - fix handling of lists for the filter options (https://github.com/ansible-collections/community.docker/issues/961, https://github.com/ansible-collections/community.docker/pull/966).
- docker_secret - make sure to sanitize ``labels`` before sending them to the Docker Daemon (https://github.com/ansible-collections/community.docker/pull/985).
- docker_swarm - make sure to sanitize ``labels`` before sending them to the Docker Daemon (https://github.com/ansible-collections/community.docker/pull/985).
- docker_swarm_service - make sure to sanitize ``labels`` and ``container_labels`` before sending them to the Docker Daemon (https://github.com/ansible-collections/community.docker/pull/985).
- docker_volume - make sure to sanitize ``labels`` before sending them to the Docker Daemon (https://github.com/ansible-collections/community.docker/pull/985).
- vendored Docker SDK for Python - use ``LooseVersion`` instead of ``StrictVersion`` to compare urllib3 versions. This is needed for development versions (https://github.com/ansible-collections/community.docker/pull/902).

community.general
~~~~~~~~~~~~~~~~~

- bitwarden lookup plugin - fix ``KeyError`` in ``search_field`` (https://github.com/ansible-collections/community.general/issues/8549, https://github.com/ansible-collections/community.general/pull/8557).
- bitwarden lookup plugin - support BWS v0.3.0 syntax breaking change (https://github.com/ansible-collections/community.general/pull/9028).
- cloudflare_dns - fix changing Cloudflare SRV records (https://github.com/ansible-collections/community.general/issues/8679, https://github.com/ansible-collections/community.general/pull/8948).
- cmd_runner module utils - call to ``get_best_parsable_locales()`` was missing parameter (https://github.com/ansible-collections/community.general/pull/8929).
- collection_version lookup plugin - use ``importlib`` directly instead of the deprecated and in ansible-core 2.19 removed ``ansible.module_utils.compat.importlib`` (https://github.com/ansible-collections/community.general/pull/9084).
- cpanm - use new ``VarDict`` to prevent deprecation warning (https://github.com/ansible-collections/community.general/issues/8410, https://github.com/ansible-collections/community.general/pull/8411).
- dig lookup plugin - fix using only the last nameserver specified (https://github.com/ansible-collections/community.general/pull/8970).
- django module utils - use new ``VarDict`` to prevent deprecation warning (https://github.com/ansible-collections/community.general/issues/8410, https://github.com/ansible-collections/community.general/pull/8411).
- django_command - option ``command`` is now split lexically before passed to underlying PythonRunner (https://github.com/ansible-collections/community.general/pull/8944).
- gconftool2_info - use new ``VarDict`` to prevent deprecation warning (https://github.com/ansible-collections/community.general/issues/8410, https://github.com/ansible-collections/community.general/pull/8411).
- git_config - fix behavior of ``state=absent`` if ``value`` is present (https://github.com/ansible-collections/community.general/issues/8436, https://github.com/ansible-collections/community.general/pull/8452).
- gitlab_group_access_token - fix crash in check mode caused by attempted access to a newly created access token (https://github.com/ansible-collections/community.general/pull/8796).
- gitlab_label - update label's color (https://github.com/ansible-collections/community.general/pull/9010).
- gitlab_project - fix ``container_expiration_policy`` not being applied when creating a new project (https://github.com/ansible-collections/community.general/pull/8790).
- gitlab_project - fix crash caused by old Gitlab projects not having a ``container_expiration_policy`` attribute (https://github.com/ansible-collections/community.general/pull/8790).
- gitlab_project_access_token - fix crash in check mode caused by attempted access to a newly created access token (https://github.com/ansible-collections/community.general/pull/8796).
- gitlab_runner - fix ``paused`` parameter being ignored (https://github.com/ansible-collections/community.general/pull/8648).
- homebrew - do not fail when brew prints warnings (https://github.com/ansible-collections/community.general/pull/8406, https://github.com/ansible-collections/community.general/issues/7044).
- homebrew_cask - fix ``upgrade_all`` returns ``changed`` when nothing upgraded (https://github.com/ansible-collections/community.general/issues/8707, https://github.com/ansible-collections/community.general/pull/8708).
- homectl - the module now tries to use ``legacycrypt`` on Python 3.13+ (https://github.com/ansible-collections/community.general/issues/4691, https://github.com/ansible-collections/community.general/pull/8987).
- hponcfg - use new ``VarDict`` to prevent deprecation warning (https://github.com/ansible-collections/community.general/issues/8410, https://github.com/ansible-collections/community.general/pull/8411).
- ini_file - pass absolute paths to ``module.atomic_move()`` (https://github.com/ansible/ansible/issues/83950, https://github.com/ansible-collections/community.general/pull/8925).
- ipa_host - add ``force_create``, fix ``enabled`` and ``disabled`` states (https://github.com/ansible-collections/community.general/issues/1094, https://github.com/ansible-collections/community.general/pull/8920).
- ipa_hostgroup - fix ``enabled `` and ``disabled`` states (https://github.com/ansible-collections/community.general/issues/8408, https://github.com/ansible-collections/community.general/pull/8900).
- java_keystore - pass absolute paths to ``module.atomic_move()`` (https://github.com/ansible/ansible/issues/83950, https://github.com/ansible-collections/community.general/pull/8925).
- jenkins_node - fixed ``enabled``, ``disable`` and ``absent`` node state redirect authorization issues, same as was present for ``present`` (https://github.com/ansible-collections/community.general/pull/9084).
- jenkins_plugin - pass absolute paths to ``module.atomic_move()`` (https://github.com/ansible/ansible/issues/83950, https://github.com/ansible-collections/community.general/pull/8925).
- kdeconfig - pass absolute paths to ``module.atomic_move()`` (https://github.com/ansible/ansible/issues/83950, https://github.com/ansible-collections/community.general/pull/8925).
- kernel_blacklist - use new ``VarDict`` to prevent deprecation warning (https://github.com/ansible-collections/community.general/issues/8410, https://github.com/ansible-collections/community.general/pull/8411).
- keycloak_client - fix TypeError when sanitizing the ``saml.signing.private.key`` attribute in the module's diff or state output. The ``sanitize_cr`` function expected a dict where in some cases a list might occur (https://github.com/ansible-collections/community.general/pull/8403).
- keycloak_client - fix diff by removing code that turns the attributes dict which contains additional settings into a list (https://github.com/ansible-collections/community.general/pull/9077).
- keycloak_clientscope - fix diff and ``end_state`` by removing the code that turns the attributes dict, which contains additional config items, into a list (https://github.com/ansible-collections/community.general/pull/9082).
- keycloak_clientscope - remove IDs from clientscope and its protocol mappers on comparison for changed check (https://github.com/ansible-collections/community.general/pull/8545).
- keycloak_clientscope_type - fix detect changes in check mode (https://github.com/ansible-collections/community.general/issues/9092, https://github.com/ansible-collections/community.general/pull/9093).
- keycloak_group - fix crash caused in subgroup creation. The crash was caused by a missing or empty ``subGroups`` property in Keycloak ≥23 (https://github.com/ansible-collections/community.general/issues/8788, https://github.com/ansible-collections/community.general/pull/8979).
- keycloak_realm - add normalizations for ``attributes`` and ``protocol_mappers`` (https://github.com/ansible-collections/community.general/pull/8496).
- keycloak_realm - fix change detection in check mode by sorting the lists in the realms beforehand (https://github.com/ansible-collections/community.general/pull/8877).
- keycloak_realm_key - fix invalid usage of ``parent_id`` (https://github.com/ansible-collections/community.general/issues/7850, https://github.com/ansible-collections/community.general/pull/8823).
- keycloak_user_federation - add module argument allowing users to configure the update mode for the parameter ``bindCredential`` (https://github.com/ansible-collections/community.general/pull/8898).
- keycloak_user_federation - fix key error when removing mappers during an update and new mappers are specified in the module args (https://github.com/ansible-collections/community.general/pull/8762).
- keycloak_user_federation - fix the ``UnboundLocalError`` that occurs when an ID is provided for a user federation mapper (https://github.com/ansible-collections/community.general/pull/8831).
- keycloak_user_federation - get cleartext IDP ``clientSecret`` from full realm info to detect changes to it (https://github.com/ansible-collections/community.general/issues/8294, https://github.com/ansible-collections/community.general/pull/8735).
- keycloak_user_federation - minimize change detection by setting ``krbPrincipalAttribute`` to ``''`` in Keycloak responses if missing (https://github.com/ansible-collections/community.general/pull/8785).
- keycloak_user_federation - remove ``lastSync`` parameter from Keycloak responses to minimize diff/changes (https://github.com/ansible-collections/community.general/pull/8812).
- keycloak_user_federation - remove existing user federation mappers if they are not present in the federation configuration and will not be updated (https://github.com/ansible-collections/community.general/issues/7169, https://github.com/ansible-collections/community.general/pull/8695).
- keycloak_user_federation - sort desired and after mapper list by name (analog to before mapper list) to minimize diff and make change detection more accurate (https://github.com/ansible-collections/community.general/pull/8761).
- keycloak_userprofile - fix empty response when fetching userprofile component by removing ``parent=parent_id`` filter (https://github.com/ansible-collections/community.general/pull/8923).
- keycloak_userprofile - improve diff by deserializing the fetched ``kc.user.profile.config`` and serialize it only when sending back (https://github.com/ansible-collections/community.general/pull/8940).
- launched - correctly report changed status in check mode (https://github.com/ansible-collections/community.general/pull/8406).
- locale_gen - use new ``VarDict`` to prevent deprecation warning (https://github.com/ansible-collections/community.general/issues/8410, https://github.com/ansible-collections/community.general/pull/8411).
- lxd_container - fix bug introduced in previous commit (https://github.com/ansible-collections/community.general/pull/8895, https://github.com/ansible-collections/community.general/issues/8888).
- mksysb - use new ``VarDict`` to prevent deprecation warning (https://github.com/ansible-collections/community.general/issues/8410, https://github.com/ansible-collections/community.general/pull/8411).
- modprobe - fix check mode not being honored for ``persistent`` option (https://github.com/ansible-collections/community.general/issues/9051, https://github.com/ansible-collections/community.general/pull/9052).
- nsupdate - fix 'index out of range' error when changing NS records by falling back to authority section of the response (https://github.com/ansible-collections/community.general/issues/8612, https://github.com/ansible-collections/community.general/pull/8614).
- one_host - fix if statements for cases when ``ID=0`` (https://github.com/ansible-collections/community.general/issues/1199, https://github.com/ansible-collections/community.general/pull/8907).
- one_image - fix module failing due to a class method typo (https://github.com/ansible-collections/community.general/pull/9056).
- one_image_info - fix module failing due to a class method typo (https://github.com/ansible-collections/community.general/pull/9056).
- one_service - fix service creation after it was deleted with ``unique`` parameter (https://github.com/ansible-collections/community.general/issues/3137, https://github.com/ansible-collections/community.general/pull/8887).
- one_vnet - fix module failing due to a variable typo (https://github.com/ansible-collections/community.general/pull/9019).
- opennebula inventory plugin - fix invalid reference to IP when inventory runs against NICs with no IPv4 address (https://github.com/ansible-collections/community.general/pull/8489).
- opentelemetry callback - do not save the JSON response when using the ``ansible.builtin.uri`` module (https://github.com/ansible-collections/community.general/pull/8430).
- opentelemetry callback - do not save the content response when using the ``ansible.builtin.slurp`` module (https://github.com/ansible-collections/community.general/pull/8430).
- pam_limits - pass absolute paths to ``module.atomic_move()`` (https://github.com/ansible/ansible/issues/83950, https://github.com/ansible-collections/community.general/pull/8925).
- paman - do not fail if an empty list of packages has been provided and there is nothing to do (https://github.com/ansible-collections/community.general/pull/8514).
- pipx - it was ignoring ``global`` when listing existing applications (https://github.com/ansible-collections/community.general/pull/9044).
- pipx module utils - add missing command line formatter for argument ``spec_metadata`` (https://github.com/ansible-collections/community.general/pull/9044).
- pipx_info - use new ``VarDict`` to prevent deprecation warning (https://github.com/ansible-collections/community.general/issues/8410, https://github.com/ansible-collections/community.general/pull/8411).
- proxmox - fix idempotency on creation of mount volumes using Proxmox' special ``<storage>:<size>`` syntax (https://github.com/ansible-collections/community.general/issues/8407, https://github.com/ansible-collections/community.general/pull/8542).
- proxmox - fixed an issue where the new volume handling incorrectly converted ``null`` values into ``"None"`` strings (https://github.com/ansible-collections/community.general/pull/8646).
- proxmox - fixed an issue where volume strings where overwritten instead of appended to in the new ``build_volume()`` method (https://github.com/ansible-collections/community.general/pull/8646).
- proxmox - removed the forced conversion of non-string values to strings to be consistent with the module documentation (https://github.com/ansible-collections/community.general/pull/8646).
- proxmox inventory plugin - fixed a possible error on concatenating responses from proxmox. In case an API call unexpectedly returned an empty result, the inventory failed with a fatal error. Added check for empty response (https://github.com/ansible-collections/community.general/issues/8798, https://github.com/ansible-collections/community.general/pull/8794).
- python_runner module utils - parameter ``path_prefix`` was being handled as string when it should be a list (https://github.com/ansible-collections/community.general/pull/8944).
- redfish_utils module utils - do not fail when language is not exactly "en" (https://github.com/ansible-collections/community.general/pull/8613).
- redfish_utils module utils - fix issue with URI parsing to gracefully handling trailing slashes when extracting member identifiers (https://github.com/ansible-collections/community.general/issues/9047, https://github.com/ansible-collections/community.general/pull/9057).
- redfish_utils module utils - remove undocumented default applytime (https://github.com/ansible-collections/community.general/pull/9114).
- snap - use new ``VarDict`` to prevent deprecation warning (https://github.com/ansible-collections/community.general/issues/8410, https://github.com/ansible-collections/community.general/pull/8411).
- snap_alias - use new ``VarDict`` to prevent deprecation warning (https://github.com/ansible-collections/community.general/issues/8410, https://github.com/ansible-collections/community.general/pull/8411).
- udm_user - the module now tries to use ``legacycrypt`` on Python 3.13+ (https://github.com/ansible-collections/community.general/issues/4690, https://github.com/ansible-collections/community.general/pull/8987).

community.grafana
~~~~~~~~~~~~~~~~~

- Add missing function argument in `grafana_contact_point` for org handling
- Fix var prefixes in silence-task in role
- Fixed check if grafana_api_key is defined for `grafana_dashboard` lookup

community.hrobot
~~~~~~~~~~~~~~~~

- boot - use PHP array form encoding when sending multiple ``authorized_key`` (https://github.com/ansible-collections/community.hrobot/issues/112, https://github.com/ansible-collections/community.hrobot/pull/113).

community.mysql
~~~~~~~~~~~~~~~

- mysql_info - Add ``plugin_hash_string`` to ``users_info`` filter's output. The existing ``plugin_auth_string`` contained the hashed password and thus is missleading, it will be removed from community.mysql 4.0.0. (https://github.com/ansible-collections/community.mysql/pull/629).
- mysql_user - Added a warning to update_password's on_new_username option if multiple accounts with the same username but different passwords exist (https://github.com/ansible-collections/community.mysql/pull/642).
- mysql_user - Fix ``tls_requires`` not removing ``SSL`` and ``X509`` when sets as empty (https://github.com/ansible-collections/community.mysql/pull/628).
- mysql_user - Fix idempotence when using variables from the ``users_info`` filter of ``mysql_info`` as an input (https://github.com/ansible-collections/community.mysql/pull/628).
- mysql_user - Fixed an IndexError in the update_password functionality introduced in PR https://github.com/ansible-collections/community.mysql/pull/580 and released in community.mysql 3.8.0. If you used this functionality, please avoid versions 3.8.0 to 3.9.0 (https://github.com/ansible-collections/community.mysql/pull/642).
- mysql_user - add correct ``ed25519`` auth plugin handling (https://github.com/ansible-collections/community.mysql/issues/6).
- mysql_user - add correct ``ed25519`` auth plugin handling when creating a user (https://github.com/ansible-collections/community.mysql/issues/672).
- mysql_user - add correct ``ed25519`` auth plugin handling when creating a user (https://github.com/ansible-collections/community.mysql/pull/676).
- mysql_user - module makes changes when is executed with ``plugin_auth_string`` parameter and check mode.
- mysql_variables - fix the module always changes on boolean values (https://github.com/ansible-collections/community.mysql/issues/652).

community.network
~~~~~~~~~~~~~~~~~

- exos - Add error handling of ``Permission denied`` errors (https://github.com/ansible-collections/community.network/pull/571).

community.postgresql
~~~~~~~~~~~~~~~~~~~~

- postgres - psycopg2 automatically sets the datestyle on the connection to iso whenever it encounters a datestyle configuration it doesn't recognize, but psycopg3 does not. Fix now enforces iso datestyle when using psycopg3 (https://github.com/ansible-collections/community.postgresql/issues/711).
- postgresql_db - fix issues due to columns in pg_database changing in Postgres 17. (https://github.com/ansible-collections/community.postgresql/issues/729).
- postgresql_info - Use a server check that works on beta and rc versions as well as on actual releases.
- postgresql_set - fixes resetting logic to allow resetting shared_preload_libraries with ``reset: true`` (https://github.com/ansible-collections/community.postgresql/issues/744).
- postgresql_set - forbids resetting shared_preload_libraries by passing an empty string (https://github.com/ansible-collections/community.postgresql/issues/744).
- postgresql_user - remove a comment from unit tests that breaks pre-compile (https://github.com/ansible-collections/community.postgresql/issues/737).

community.proxysql
~~~~~~~~~~~~~~~~~~

- module_utils - fix ProxySQL version parsing that fails when a suffix wasn't present in the version (https://github.com/ansible-collections/community.proxysql/issues/154).
- role_proxysql - Correct package name (python3-mysqldb instead of python-mysqldb) (https://github.com/ansible-collections/community.proxysql/pull/89).
- role_proxysql - Dynamic user/password in .my.cnf (https://github.com/ansible-collections/community.proxysql/pull/89).

community.routeros
~~~~~~~~~~~~~~~~~~

- api_modify, api_info - change the default of ``ingress-filtering`` in paths ``interface bridge`` and ``interface bridge port`` back to ``false`` for RouterOS before version 7 (https://github.com/ansible-collections/community.routeros/pull/305).

community.sops
~~~~~~~~~~~~~~

- Fix RPM URL for the 3.9.0 release (https://github.com/ansible-collections/community.sops/pull/188).
- Pass ``config_path`` on SOPS 3.9.0 before the subcommand instead of after it (https://github.com/ansible-collections/community.sops/issues/195, https://github.com/ansible-collections/community.sops/pull/197).
- sops_encrypt - pass absolute paths to ``module.atomic_move()`` (https://github.com/ansible/ansible/issues/83950, https://github.com/ansible-collections/community.sops/pull/208).
- sops_encrypt - properly support ``path_regex`` in ``.sops.yaml`` when SOPS 3.9.0 or later is used (https://github.com/ansible-collections/community.sops/issues/153, https://github.com/ansible-collections/community.sops/pull/190).

community.vmware
~~~~~~~~~~~~~~~~

- Document dependency on requests (https://github.com/ansible-collections/community.vmware/issues/2127).
- vcenter_folder - removed documentation that incorrectly said `folder_type` had no effect when `parent_folder` was set
- vcenter_standard_key_provider - Fix documentation (https://github.com/ansible-collections/community.vmware/pull/2192).
- vmware_all_snapshots_info - fixed the datacenter parameter was ignored(https://github.com/ansible-collections/community.vmware/pull/2165).
- vmware_cluster_vcls - fixed bug caused by pyvmomi >=7.0.3 returning the vlcs cluster config attribute as None when it was previously undefined. Now if the vCLS config is not initialized on the cluster, the module will initialize it using the user's desired state.
- vmware_dvswitch - Fix Pylint issue (https://github.com/ansible-collections/community.vmware/pull/2186).
- vmware_dvswitch_nioc - Fix documentation (https://github.com/ansible-collections/community.vmware/pull/2192).
- vmware_dvswitch_pvlans - Fix Pylint issue (https://github.com/ansible-collections/community.vmware/pull/2186).
- vmware_guest - Fix documentation (https://github.com/ansible-collections/community.vmware/pull/2192).
- vmware_guest - Fix existing disk erroneously being re-created when modifying vm with 8 or more disks. (https://github.com/ansible-collections/community.vmware/pull/2173).
- vmware_guest_controller - Fix documentation (https://github.com/ansible-collections/community.vmware/pull/2192).
- vmware_guest_disk - Fix documentation (https://github.com/ansible-collections/community.vmware/pull/2192).
- vmware_guest_disk - round size to int, supporting float values properly (https://github.com/ansible-collections/community.vmware/issues/123).
- vmware_guest_serial_port - Fix documentation (https://github.com/ansible-collections/community.vmware/pull/2192).
- vmware_guest_snapshot - Update documentation regarding snapshot_id parameter (https://github.com/ansible-collections/community.vmware/issues/2145).
- vmware_guest_tpm - Fix Pylint issue (https://github.com/ansible-collections/community.vmware/pull/2186).
- vmware_host - Fix Pylint issue (https://github.com/ansible-collections/community.vmware/pull/2186).
- vmware_host_dns - Fix Pylint issue (https://github.com/ansible-collections/community.vmware/pull/2186).
- vmware_host_inventory - Fix Pylint issue (https://github.com/ansible-collections/community.vmware/pull/2186).
- vmware_host_logbundle - Manifests previously was separared by "&", thus selecting first manifest. Fix now separates manifests with URL encoded space, thus correctly supplying the manifests.  (https://github.com/ansible-collections/community.vmware/pull/2090).
- vmware_host_powerstate - Fix Pylint issue (https://github.com/ansible-collections/community.vmware/pull/2186).
- vmware_tools - Fix documentation (https://github.com/ansible-collections/community.vmware/pull/2192).
- vmware_vm_inventory - Fix Pylint issue (https://github.com/ansible-collections/community.vmware/pull/2186).
- vmware_vmotion - Fix Pylint issue (https://github.com/ansible-collections/community.vmware/pull/2186).
- vmware_vmotion - Fix a `list index out of range` error when vSphere doesn't provide a placement recommendation (https://github.com/ansible-collections/community.vmware/pull/2208).

community.windows
~~~~~~~~~~~~~~~~~

- win_mapped_drive - Use correct P/Invoke signature to fix mapped network drives on 32 Bit OS.
- win_mapped_drive - better handle failures when attempting to set mapped drive that already exists but was seen as a local path.

community.zabbix
~~~~~~~~~~~~~~~~

- remove references to tags in LLD rules
- zabbix_actions - fix proxy get compatibility for zabbix 7.0
- zabbix_agent Role - Fix Configure zabbix_agent
- zabbix_agent Role - Fix for userparameter because include_dir is list
- zabbix_agent Role - Fix include_dir directory creation logic
- zabbix_agent Role - Fixed several issues related to `zabbix_agent_include_dir` and `zabbix_agent_include`
- zabbix_agent Role - Fixes a mispelling of the `zabbix_agent_logfile` variable
- zabbix_agent Role - Fixes error in the double assignment of values for the `zabbix_agent_tlspskidentity_check` and `zabbix_agent_tlspskcheck` variables.
- zabbix_agent Role - Fixes multiple errors related to the Windows install
- zabbix_agent Role - fix TLSAccept parameter provisioning in zabbix_agentd.conf
- zabbix_agent Role - fixed problem with Windows include dir.
- zabbix_agent role - Fix for removal of wrong agent include directory (https://github.com/ansible-collections/community.zabbix/issues/1236)
- zabbix_agent role - Fix reading existing psk
- zabbix_agent role - Fix role when zabbix_agent_listenip is undefined
- zabbix_agent role - Fix windows agent installation issue
- zabbix_agent role - Fixed logic problem that would break if anything other than PSK was used.
- zabbix_agent role - Fixed missing setting for `zabbix_agent_persistentbuffer`
- zabbix_agent role - fix error when ``zabbix_agent_tlsaccept`` is not set
- zabbix_agent role - fix error when ``zabbix_agent_tlsconnect`` is not set
- zabbix_agent role - fix name of Zabbix Agent 2 config filename
- zabbix_agent role - in ``zabbix_agent_interfaces`` directly use ``zabbix_agent_listenport``, which does already contains the agent2 value if needed
- zabbix_agent, zabbix_proxy, and zabbix_server roles - Fixed problem with include file
- zabbix_authentication - fix inability to set passwd_check_rules to empty list
- zabbix_authentication - fix inability to update passwd_check_rules
- zabbix_host - delete denied parameter from interfaces
- zabbix_proxy Role - Fixed TLS configuration
- zabbix_repo Role - Fixes error that attempts to use the repo name as a variable.
- zabbix_server Role - fixed creating TimescaleDB hypertables for Zabbix 7.0
- zabbix_web - make the FPM socket group-writable so the web server can properly forward requests to the FPM process

containers.podman
~~~~~~~~~~~~~~~~~

- Add missing parameters for podman container quadlet
- Add new options for podman_network
- Add option to specify kube file content in module
- Add quadlet file mode option to specify file permission
- Add secret to login module
- CI - Add images removal for tests
- CI - Fix podman CI test container images
- CI - add ignore list for Ansible sanity for 2.19
- CI - bump artifacts versions for GHactions
- CI - change k8s.gcr.io to registry.k8s.io in tests
- CI - fix Podman search of invalid image
- Disable idempotency for pod_id_file
- Don't check image availability in Quadlet
- Fix command idempotency with quotes
- Fix health-startup-cmd
- Fix idempotency for empty values
- Fix idempotency for pod with 0.0.0.0
- Fix idempotency for pods in case of systemd generation
- Fix idempotency for systemd generations
- Fix issue with pushing podman image to repo name and org
- Fix logic in Podman images
- Fix max_size idempotency issue
- Fix missing entries in network quadlet generated file
- Fix podman image permissions issue and runlable test
- Fix quadlet parameters for restart policy
- Fix quadlet parameters when container uses rootfs
- Fix transports issues in podman_image
- Fix typo in quadlet generator
- Fix unsupported pull policy in example on podman_container.py
- Idempotency improvements
- don't document quadlet_dir as required when setting state=quadlet
- fix for tls_verify being ignored
- fix quadlet cmd_args append mistake
- fix(#747) set correct HealthCmd
- fix(podman_image) - skip empty volume items
- fix(podman_save) - always changed when force
- modify error and docs
- params gpus should be exit_policy
- podman_login does not support check_mode

dellemc.enterprise_sonic
~~~~~~~~~~~~~~~~~~~~~~~~

- ConnectionError - Add the needed import of the Ansible ConnectionError exception class for all files where it was previously missing. (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/445).
- Update regex search expression for 'not found' error message in httpapi/sonic.py 'edit_config' method (https://github.com/ansible-collection/dellemc.enterprise_sonic/pull/443).
- sonic_bfd - Fix BFD states implementation bug (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/383).
- sonic_bgp_neighbors - Fix issues with deleted state (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/335).
- sonic_copp - Fix CoPP states implementation bug (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/381).
- sonic_interfaces - Fix exception when gathering facts (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/377).
- sonic_interfaces - Fix replaced and overridden state handling for Loopback interfaces (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/364).
- sonic_l2_interfaces - Fix exception when gathering facts (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/410).
- sonic_l3_interfaces - Fix replaced state handling (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/431).
- sonic_mac - Fix MAC states implementation bug (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/383).
- sonic_prefix_lists - Fix idempotency failure (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/354).
- sonic_prefix_lists - Fix replaced state handling (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/354).
- sonic_qos_pfc - Add back accidentally deleted line of code  (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/391).
- sonic_static_routes - Fix static routes states implementation bug (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/383).
- sonic_system - Catch the ConnectionError exception caused by unconditional fetching of auditd and ip loadshare hash algorithm configuration, and return empty configuration instead of allowing the uncaught exception to abort all "system" operations on SONiC images older than version 4.4.0 (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/441).
- sonic_vlans - Fix exception when gathering facts (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/377).

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- Resolved the issue in ``idrac_certificates`` module where subject_alt_name parameter was only accepting first item in list. (https://github.com/dell/dellemc-openmanage-ansible-modules/issues/584)
- Resolved the issue in ``idrac_gather_facts`` role where it was failing for some component in iDRAC8. (https://github.com/dell/dellemc-openmanage-ansible-modules/issues/718)
- Resolved the issue in ``idrac_reset`` module where it fails when iDRAC is in busy state. (https://github.com/dell/dellemc-openmanage-ansible-modules/issues/652)
- Resolved the issue in ``idrac_virtual_media`` module where the Authorization request header was included in the request. (https://github.com/dell/dellemc-openmanage-ansible-modules/issues/612)
- Resolved the issue in ``ome_application_certificate`` module related to a padding error in generated CSR file. (https://github.com/dell/dellemc-openmanage-ansible-modules/issues/370)
- idrac_storage_volume - Issue(290766) - The module will report success instead of showing failure for new virtual creation on the BOSS-N1 controller if a virtual disk is already present on the same controller.
- idrac_support_assist - Issue(308550) - This module fails when the NFS share path contains sub directory.
- ome_diagnostics - Issue(279193) - Export of SupportAssist collection logs to the share location fails on OME version 4.0.0.

f5networks.f5_modules
~~~~~~~~~~~~~~~~~~~~~

- bigip_imish_config - fixed a bug that resulted in incomplete config when using BGV route domain

fortinet.fortimanager
~~~~~~~~~~~~~~~~~~~~~

- Added more description in the documentation.
- Deleted 9 fmgr_switchcontroller_managedswitch_* modules. Will support them in FortiManager Device Ansible.
- Fixed Bug in "fmgr_fact"
- Improved documentation.
- Improved fmgr_fact, fmgr_clone, fmgr_move.

fortinet.fortios
~~~~~~~~~~~~~~~~

- Fix some issues in sanity test.
- Fix the issue using diff feature in check_mode.
- Github
- Github issue
- Mantis
- Return invalid json content instead of error while adding redundant comma at the end of the last variable in `fortios_json_generic`.
- mantis issue

google.cloud
~~~~~~~~~~~~

- ansible-lint - remove jinja templates from test assertions
- gcp_kms_filters - add DOCUMENTATION string
- gcp_secret_manager - make an f-string usage backward compatible

hetzner.hcloud
~~~~~~~~~~~~~~

- server - Keep `force_upgrade` deprecated alias for another major version.
- server - Wait up to 30 minutes for every action returned from server create

ibm.storage_virtualize
~~~~~~~~~~~~~~~~~~~~~~

- ibm_svc_manage_callhome - Added support to change a subset of proxy settings
- ibm_svc_manage_callhome - Setting censorcallhome does not work
- ibm_svc_utils - REST API timeout due to slow response
- ibm_svc_utils - Return correct error in case of error code 500

infoblox.nios_modules
~~~~~~~~~~~~~~~~~~~~~

- Adjusted unit test assertions for Mock.called_once_with.
- Fixed an issue in the `nios_host_record` module where the `mac` parameter was not handled correctly.
- Fixed the update operation in the `nios_network` module where the `network` parameter was not handled correctly.
- Omits DNS view from filter criteria when renaming a host object and DNS is bypassed. (https://github.com/infobloxopen/infoblox-ansible/issues/230)
- nios_host_record - rename logic included DNS view in filter criteria, even when DNS had been bypassed.

inspur.ispim
~~~~~~~~~~~~

- Change the ansible version in meta/runtime.yml to 2.15.0(https://github.com/ispim/inspur.ispim/pull/37).
- Remove venv files that were accidentally bundled in 2.2.1 (https://github.com/ispim/inspur.ispim/pull/35).

junipernetworks.junos
~~~~~~~~~~~~~~~~~~~~~

- Fix the lag_interfaces facts for gigether supported model.

kaytus.ksmanage
~~~~~~~~~~~~~~~

- Edit ansible devel version tests to our CI test scripts (https://github.com/ieisystem/kaytus.ksmanage/pull/26).
- Modify the title information in changelogs config.yaml (https://github.com/ieisystem/kaytus.ksmanage/pull/25).
- Remove venv files that were accidentally bundled in 1.2.2(https://github.com/ieisystem/kaytus.ksmanage/pull/23).

kubernetes.core
~~~~~~~~~~~~~~~

- Resolve Collections util resource discovery fails when complex subresources present (https://github.com/ansible-collections/kubernetes.core/pull/676).
- align `helmdiff_check()` function commandline rendering with the `deploy()` function (https://github.com/ansible-collections/kubernetes.core/pull/670).
- avoid unsafe conditions in integration tests (https://github.com/ansible-collections/kubernetes.core/pull/665).
- helm - Helm version checks did not support RC versions. They now accept any version tags. (https://github.com/ansible-collections/kubernetes.core/pull/745).
- helm - use ``reuse-values`` when running ``helm diff`` command (https://github.com/ansible-collections/kubernetes.core/issues/680).
- helm_pull - Apply no_log=True to pass_credentials to silence false positive warning. (https://github.com/ansible-collections/kubernetes.core/pull/796).
- integrations test helm_kubeconfig - set helm version to v3.10.3 to avoid incompatability with new bitnami charts (https://github.com/ansible-collections/kubernetes.core/pull/670).
- k8s_drain - Fix k8s_drain does not wait for single pod (https://github.com/ansible-collections/kubernetes.core/issues/769).
- k8s_drain - Fix k8s_drain runs into a timeout when evicting a pod which is part of a stateful set  (https://github.com/ansible-collections/kubernetes.core/issues/792).
- kubeconfig option should not appear in module invocation log (https://github.com/ansible-collections/kubernetes.core/issues/782).
- kustomize - kustomize plugin fails with deprecation warnings (https://github.com/ansible-collections/kubernetes.core/issues/639).
- waiter - Fix waiting for daemonset when desired number of pods is 0. (https://github.com/ansible-collections/kubernetes.core/pull/756).

lowlydba.sqlserver
~~~~~~~~~~~~~~~~~~

- Include warning logs in failure output for the restore module to indicate root causes (https://github.com/lowlydba/lowlydba.sqlserver/pull/266).
- fixed the expected type of the ip_address, subnet_ip, and subnet_mask parameters to be lists instead of strings (lowlydba.sqlserver.ag_listener)

microsoft.ad
~~~~~~~~~~~~

- Fix ``microsoft.ad.debug_ldap_client`` documentation problem so it appears in the ``ansible-doc`` plugin list and online documentation.
- Removed usages of the python call ``datetime.datetime.utcnow()`` in favour of ``datetime.datetime.now(datetime.timezone.utc)``. The original method is now deprecated in Python 3.12 and will be removed in a later version.
- group - fix error when creating a group with no members explicitly set - https://github.com/ansible-collections/microsoft.ad/issues/141
- ldap - Filter out managed service accounts in the default LDAP filter used. The ``filter_without_computer`` can be used to disable the default filter if needed.
- membership - allow domain join with hostname change if the account for that host already exists - https://github.com/ansible-collections/microsoft.ad/pull/145
- microsoft.ad.computer - Added fallback ``identity`` lookup for ``sAMAccountName`` with the ``$`` suffix. This ensures that finding the computer object will work with or without the ``$`` suffix. - https://github.com/ansible-collections/microsoft.ad/issues/124
- microsoft.ad.group - Fix setting group members of Builtin groups of a domain controller - https://github.com/ansible-collections/microsoft.ad/issues/130
- microsoft.ad.membership - Fix hostname check to work with hostnames longer than 15 characters long - https://github.com/ansible-collections/microsoft.ad/issues/113
- microsoft.ad.user - Fix issue when creating a new user account with ``account_locked: false`` - https://github.com/ansible-collections/microsoft.ad/issues/108

netapp.ontap
~~~~~~~~~~~~

- na_ontap_export_policy_rule - fix issue with idempotency in REST.
- na_ontap_file_security_permissions - set `apply_to` as optional and default value as true.
- na_ontap_flexcache - add warning for flexcache relationship deletion in ZAPI.
- na_ontap_qtree - add warning for job still running for deletion operation in REST, when wait_for_completion is not set.
- na_ontap_quotas - fix error with `quota_target` while trying to set default user quota rule in REST.
- na_ontap_rest_info - fixed issue with capturing error.
- na_ontap_snapshot_policy - fix issue with idempotency when `snapmirror_label` is set to empty in REST.
- na_ontap_user_role - fix issue with setting multiple permissions with REST.
- na_ontap_volume - added error message while trying to modify efficiency configuration for a volume in REST, when efficiency is disabled.
- na_ontap_volume_efficiency - fix issue with modifying volume efficiency in REST.

netapp_eseries.santricity
~~~~~~~~~~~~~~~~~~~~~~~~~

- Fixed pep8, pylint, and validate-modules issues found by ansible-test.
- Updated outdated command in unit tests.

netbox.netbox
~~~~~~~~~~~~~

- Added ALLOWED_QUERY_PARAMS module_bay by device `#1228 <https://github.com/netbox-community/ansible_modules/pull/1228>`_
- Added label to power outlet `#1222 <https://github.com/netbox-community/ansible_modules/pull/1222>`_
- Added power outlet type iec-60320-c21 to power outlet template and power outlet modules `#1229 <https://github.com/netbox-community/ansible_modules/issues/1229>`_
- Extend query param for parent_location `#1233 <https://github.com/netbox-community/ansible_modules/issues/1233>`_
- If `fetch_all` is `false`, prefix lookup depends on site lookup, so move it to secondary lookup (https://github.com/netbox-community/ansible_modules/issues/733)

ngine_io.cloudstack
~~~~~~~~~~~~~~~~~~~

- Fixed a bug related to the new option ``validate_certs`` (https://github.com/ngine-io/ansible-collection-cloudstack/pull/135).

purestorage.flasharray
~~~~~~~~~~~~~~~~~~~~~~

- purefa_dsrole - Fix function name typo
- purefa_dsrole - Fix version check logic
- purefa_hg - Fix edge case with incorrectly deleted hostgroup when empty array sent for volumes or hosts
- purefa_info - Fix typo from PR
- purefa_info - Fixed issue trying to collect deleted volumes perfomance stats
- purefa_info - Resolve issue with performance stats trying to report for remote hosts
- purefa_network - Fix issue with clearing network interface addresses
- purefa_network - Resolve issue when setting a network port on a new array
- purefa_pg - Fix parameter name typo
- purefa_pod - Fix issue with pod not creating correctly
- purefa_policy - Enhanced idempotency for snapshot policy rules
- purefa_subnet - Initialize varaible correctly
- purefa_syslog_settings - Initialize varaible correctly
- purefa_volume - Fix issue with creating volume using old Purity version (6.1.19)
- purefa_volume - Fixes ``eradicate`` so it doesn't report success when it hasn't actually eradicated
- purefa_volume - Fixes ``volfact`` response when in ``check_mode``
- purefa_volume - Fixes issue where malformed ``volfact`` will cause the ``move`` to apparently fail.

purestorage.flashblade
~~~~~~~~~~~~~~~~~~~~~~

- purefb_certs - Fix issue with importing certificates
- purefb_certs - Fix parameter mispelling of ``intermeadiate_cert`` to ``intermediate_cert``. Keep original mispelling as an alias.
- purefb_ds - Initialize variable correctly
- purefb_fs - Fix conflict with SMB mode and ACL safeguarding
- purefb_fs - Fix error checking for SMB parameter in non-SMB filesystem
- purefb_info - Fix space reporting issue
- purefb_policy - Initialize variable correctly
- purefb_ra - Fix incorrect import statement
- purefb_snap - Fix issue with immeadiate remote snapshots not executing

theforeman.foreman
~~~~~~~~~~~~~~~~~~

- callback plugin - correctly catch facts with vault data and replace it with ``ENCRYPTED_VAULT_VALUE_NOT_REPORTED``, preventing ``Object of type AnsibleVaultEncryptedUnicode is not JSON serializable`` errors
- redhat_manifest - do not send empty JSON bodies in GET requests which confuse the portal sometimes (https://github.com/theforeman/foreman-ansible-modules/issues/1768)

vmware.vmware_rest
~~~~~~~~~~~~~~~~~~

- Fixed grammatical error in vcenter_rest_log_file parameter description
- README - fixed various typos in documentation
- Removed the scenario guides which are pretty much unmaintained and, therefor, possibly outdated and misleading (https://github.com/ansible-collections/vmware.vmware_rest/pull/524).
- lookup - fixed issue where searching for datacenter contents would throw an exception instead of returning expected results
- vcenter_vm_guest_customization - Fixed typos and spacing in the module examples

Known Issues
------------

Ansible-core
~~~~~~~~~~~~

- ansible-test - When using ansible-test containers with Podman on a Ubuntu 24.04 host, ansible-test must be run as a non-root user to avoid permission issues caused by AppArmor.
- ansible-test - When using the Fedora 40 container with Podman on a Ubuntu 24.04 host, the ``unix-chkpwd`` AppArmor profile must be disabled on the host to allow SSH connections to the container.

ansible.netcommon
~~~~~~~~~~~~~~~~~

- libssh - net_put and net_get fail when the destination file intended to be fetched is not present.

community.docker
~~~~~~~~~~~~~~~~

- docker_container - when specifying a MAC address for a container's network, and the network is attached after container creation (for example, due to idempotency checks), the MAC address is at least in some cases ignored by the Docker Daemon (https://github.com/ansible-collections/community.docker/pull/933).

community.general
~~~~~~~~~~~~~~~~~

- jenkins_node - the module is not able to update offline message when node is already offline due to internally using toggleOffline API (https://github.com/ansible-collections/community.general/pull/9084).

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- idrac_diagnostics - Issue(285322) - This module doesn't support export of diagnostics file to HTTP and HTTPS share via SOCKS proxy.
- idrac_firmware - Issue(279282) - This module does not support firmware update using HTTP, HTTPS, and FTP shares with authentication on iDRAC8.
- idrac_storage_volume - Issue(290766) - The module will report success instead of showing failure for new virtual creation on the BOSS-N1 controller if a virtual disk is already present on the same controller.
- idrac_support_assist - Issue(308550) - This module fails when the NFS share path contains sub directory.
- ome_diagnostics - Issue(279193) - Export of SupportAssist collection logs to the share location fails on OME version 4.0.0.
- ome_smart_fabric_uplink - Issue(186024) - The module supported by OpenManage Enterprise Modular, however it does not allow the creation of multiple uplinks of the same name. If an uplink is created using the same name as an existing uplink, then the existing uplink is modified.

New Plugins
-----------

Filter
~~~~~~

- community.general.keep_keys - Keep specific keys from dictionaries in a list.
- community.general.remove_keys - Remove specific keys from dictionaries in a list.
- community.general.replace_keys - Replace specific keys in a list of dictionaries.
- community.general.reveal_ansible_type - Return input type.

Test
~~~~

- ansible.builtin.timedout - did the task time out
- ansible.builtin.vaulted_file - Is this file an encrypted vault
- community.general.ansible_type - Validate input type.

New Modules
-----------

Ansible-core
~~~~~~~~~~~~

Lib
^^^

Ansible.Modules
...............

- ansible.builtin.mount_facts - Retrieve mount information.

amazon.aws
~~~~~~~~~~

- amazon.aws.autoscaling_instance - manage instances associated with AWS AutoScaling Groups (ASGs)
- amazon.aws.autoscaling_instance_info - describe instances associated with AWS AutoScaling Groups (ASGs)
- amazon.aws.ec2_launch_template_info - Gather information about launch templates and versions
- amazon.aws.ec2_vpc_egress_igw_info - Gather information about AWS VPC Egress Only Internet gateway

check_point.mgmt
~~~~~~~~~~~~~~~~

- check_point.mgmt.cp_mgmt_add_custom_trusted_ca_certificate - Create new custom trusted CA certificate.
- check_point.mgmt.cp_mgmt_add_outbound_inspection_certificate - Add outbound-inspection-certificate
- check_point.mgmt.cp_mgmt_cp_trusted_ca_certificate_facts - Retrieve existing Check Point trusted CA certificate objects facts on Checkpoint devices.
- check_point.mgmt.cp_mgmt_custom_trusted_ca_certificate_facts - Retrieve existing custom trusted CA certificate objects facts on Checkpoint devices.
- check_point.mgmt.cp_mgmt_data_type_compound_group - Manages data-type-compound-group objects on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_data_type_compound_group_facts - Get data-type-compound-group objects facts on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_data_type_file_attributes - Manages data-type-file-attributes objects on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_data_type_file_attributes_facts - Get data-type-file-attributes objects facts on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_data_type_file_group_facts - Get data-type-file-group objects facts on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_data_type_group - Manages data-type-group objects on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_data_type_group_facts - Get data-type-group objects facts on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_data_type_keywords - Manages data-type-keywords objects on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_data_type_keywords_facts - Get data-type-keywords objects facts on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_data_type_patterns - Manages data-type-patterns objects on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_data_type_patterns_facts - Get data-type-patterns objects facts on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_data_type_traditional_group - Manages data-type-traditional-group objects on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_data_type_traditional_group_facts - Get data-type-traditional-group objects facts on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_data_type_weighted_keywords - Manages data-type-weighted-keywords objects on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_data_type_weighted_keywords_facts - Get data-type-weighted-keywords objects facts on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_delete_custom_trusted_ca_certificate - Delete existing custom trusted CA certificate using name or uid.
- check_point.mgmt.cp_mgmt_delete_infinity_idp - Delete Infinity Identity Provider from the Infinity Portal using object name or uid.
- check_point.mgmt.cp_mgmt_delete_infinity_idp_object - Delete users/groups/machines from the Identity Provider using object name or uid.
- check_point.mgmt.cp_mgmt_delete_outbound_inspection_certificate - Delete outbound-inspection-certificate
- check_point.mgmt.cp_mgmt_external_trusted_ca - Manages external-trusted-ca objects on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_external_trusted_ca_facts - Get external-trusted-ca objects facts on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_https_rule - Manages https-rule objects on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_https_rule_facts - Get https-rule objects facts on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_import_outbound_inspection_certificate - Import Outbound Inspection certificate for HTTPS inspection.
- check_point.mgmt.cp_mgmt_infinity_idp_facts - Get Infinity Identity Provider objects facts from the Infinity Portal.
- check_point.mgmt.cp_mgmt_infinity_idp_object_facts - Retrieve users/groups/machines objects facts from the Identity Provider.
- check_point.mgmt.cp_mgmt_interface - Manages interface objects on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_interface_facts - Get interface objects facts on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_limit - Manages limit objects on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_limit_facts - Get limit objects facts on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_mobile_access_profile_rule - Manages mobile-access-profile-rule objects on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_mobile_access_profile_rule_facts - Get mobile-access-profile-rule objects facts on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_mobile_access_profile_section - Manages mobile-access-profile-section objects on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_mobile_access_rule - Manages mobile-access-rule objects on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_mobile_access_rule_facts - Get mobile-access-rule objects facts on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_mobile_access_section - Manages mobile-access-section objects on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_mobile_profile - Manages mobile-profile objects on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_mobile_profile_facts - Get mobile-profile objects facts on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_multiple_key_exchanges - Manages multiple-key-exchanges objects on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_multiple_key_exchanges_facts - Get multiple-key-exchanges objects facts on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_network_probe - Manages network-probe objects on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_network_probe_facts - Get network-probe objects facts on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_opsec_trusted_ca - Manages opsec-trusted-ca objects on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_opsec_trusted_ca_facts - Get opsec-trusted-ca objects facts on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_outbound_inspection_certificate_facts - Get outbound-inspection-certificate objects facts on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_override_categorization - Manages override-categorization objects on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_override_categorization_facts - Get override-categorization objects facts on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_passcode_profile - Manages passcode-profile objects on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_passcode_profile_facts - Get passcode-profile objects facts on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_resource_cifs - Manages resource-cifs objects on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_resource_cifs_facts - Get resource-cifs objects facts on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_resource_ftp - Manages resource-ftp objects on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_resource_ftp_facts - Get resource-ftp objects facts on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_resource_smtp - Manages resource-smtp objects on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_resource_smtp_facts - Get resource-smtp objects facts on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_resource_uri - Manages resource-uri objects on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_resource_uri_facts - Get resource-uri objects facts on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_set_app_control_advanced_settings - Edit Application Control & URL Filtering Blades' Settings.
- check_point.mgmt.cp_mgmt_set_content_awareness_advanced_settings - Edit Content Awareness Blades' Settings.
- check_point.mgmt.cp_mgmt_set_cp_trusted_ca_certificate - Edit existing Check Point trusted CA certificate using name or uid.
- check_point.mgmt.cp_mgmt_set_gateway_global_use - Enable or disable global usage on a specific target.
- check_point.mgmt.cp_mgmt_set_https_advanced_settings - Configure advanced settings for HTTPS Inspection.
- check_point.mgmt.cp_mgmt_set_internal_trusted_ca - Edit existing Internal CA object.
- check_point.mgmt.cp_mgmt_set_outbound_inspection_certificate - Edit outbound-inspection-certificate
- check_point.mgmt.cp_mgmt_show_app_control_advanced_settings - Show Application Control & URL Filtering Blades' Settings.
- check_point.mgmt.cp_mgmt_show_content_awareness_advanced_settings - Show Content Awareness Blades' Settings.
- check_point.mgmt.cp_mgmt_show_gateway_capabilities - Show supported Check Point Gateway capabilities such as versions, hardwares, platforms and blades.
- check_point.mgmt.cp_mgmt_show_gateway_global_use - Show global usage of a specific target.
- check_point.mgmt.cp_mgmt_show_https_advanced_settings - Show advanced settings for HTTPS Inspection.
- check_point.mgmt.cp_mgmt_show_internal_trusted_ca - Retrieve existing Internal CA object.
- check_point.mgmt.cp_mgmt_show_last_published_session - Shows the last published session.
- check_point.mgmt.cp_mgmt_show_mobile_access_profile_section - Retrieve existing Mobile Access Profile section using section name or uid.
- check_point.mgmt.cp_mgmt_show_mobile_access_section - Retrieve existing Mobile Access section using section name or uid.
- check_point.mgmt.cp_mgmt_verify_management_license - Check how many Security Gateway objects the Management Server license supports.
- check_point.mgmt.cp_mgmt_vsx_provisioning_tool - Run the VSX provisioning tool with the specified parameters.

cisco.iosxr
~~~~~~~~~~~

- cisco.iosxr.iosxr_route_maps - Resource module to configure route maps.

community.docker
~~~~~~~~~~~~~~~~

- community.docker.docker_compose_v2_exec - Run command in a container of a Compose service.
- community.docker.docker_compose_v2_run - Run command in a new container of a Compose service.

community.general
~~~~~~~~~~~~~~~~~

- community.general.bootc_manage - Bootc Switch and Upgrade.
- community.general.consul_agent_check - Add, modify, and delete checks within a consul cluster.
- community.general.consul_agent_service - Add, modify and delete services within a consul cluster.
- community.general.django_check - Wrapper for C(django-admin check).
- community.general.django_createcachetable - Wrapper for C(django-admin createcachetable).
- community.general.homebrew_services - Services manager for Homebrew.
- community.general.ipa_getkeytab - Manage keytab file in FreeIPA.
- community.general.jenkins_node - Manage Jenkins nodes.
- community.general.keycloak_component - Allows administration of Keycloak components via Keycloak API.
- community.general.keycloak_realm_keys_metadata_info - Allows obtaining Keycloak realm keys metadata via Keycloak API.
- community.general.keycloak_userprofile - Allows managing Keycloak User Profiles.
- community.general.krb_ticket - Kerberos utils for managing tickets.
- community.general.one_vnet - Manages OpenNebula virtual networks.
- community.general.zypper_repository_info - List Zypper repositories.

community.grafana
~~~~~~~~~~~~~~~~~

- community.grafana.grafana_contact_point - Manage Grafana Contact Points

community.zabbix
~~~~~~~~~~~~~~~~

- community.zabbix.zabbix_mfa - Create/update/delete Zabbix MFA method

containers.podman
~~~~~~~~~~~~~~~~~

- containers.podman.podman_container_copy - Copy file to or from a container
- containers.podman.podman_search - Search for remote images using podman

dellemc.enterprise_sonic
~~~~~~~~~~~~~~~~~~~~~~~~

- dellemc.enterprise_sonic.sonic_ldap - Configure global LDAP server settings on SONiC.
- dellemc.enterprise_sonic.sonic_login_lockout - Manage Global Login Lockout configurations on SONiC.
- dellemc.enterprise_sonic.sonic_mgmt_servers - Manage management servers configuration on SONiC.
- dellemc.enterprise_sonic.sonic_ospf_area - configure OSPF area settings on SONiC.
- dellemc.enterprise_sonic.sonic_ospfv2 - Configure global OSPFv2 protocol settings on SONiC.
- dellemc.enterprise_sonic.sonic_ospfv2_interfaces - Configure OSPFv2 interface mode protocol settings on SONiC.
- dellemc.enterprise_sonic.sonic_pim_global - Manage global PIM configurations on SONiC.
- dellemc.enterprise_sonic.sonic_pim_interfaces - Manage interface-specific PIM configurations on SONiC.
- dellemc.enterprise_sonic.sonic_poe - Manage PoE configuration on SONiC.
- dellemc.enterprise_sonic.sonic_qos_buffer - Manage QoS buffer configuration on SONiC.
- dellemc.enterprise_sonic.sonic_qos_interfaces - Manage QoS interfaces configuration on SONiC.
- dellemc.enterprise_sonic.sonic_qos_maps - Manage QoS maps configuration on SONiC.
- dellemc.enterprise_sonic.sonic_qos_pfc - Manage QoS PFC configuration on SONiC.
- dellemc.enterprise_sonic.sonic_qos_scheduler - Manage QoS scheduler configuration on SONiC.
- dellemc.enterprise_sonic.sonic_qos_wred - Manage QoS WRED profiles configuration on SONiC.
- dellemc.enterprise_sonic.sonic_roce - Manage RoCE QoS configuration on SONiC.
- dellemc.enterprise_sonic.sonic_sflow - configure sflow settings on SONiC.
- dellemc.enterprise_sonic.sonic_vrrp - Configure VRRP protocol settings on SONiC.

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- dellemc.openmanage.ome_session - This module allows you to create and delete sessions on OpenManage Enterprise and OpenManage Enterprise Modular.

fortinet.fortimanager
~~~~~~~~~~~~~~~~~~~~~

- fortinet.fortimanager.fmgr_extensioncontroller_extenderprofile_wifi - FortiExtender wifi configuration.
- fortinet.fortimanager.fmgr_extensioncontroller_extenderprofile_wifi_radio1 - Radio-1 config for Wi-Fi 2.
- fortinet.fortimanager.fmgr_extensioncontroller_extenderprofile_wifi_radio2 - Radio-2 config for Wi-Fi 5GHz
- fortinet.fortimanager.fmgr_firewall_sslsshprofile_echoutersni - ClientHelloOuter SNIs to be blocked.
- fortinet.fortimanager.fmgr_fmg_sasemanager_settings - Fmg sase manager settings
- fortinet.fortimanager.fmgr_fmg_sasemanager_status - Fmg sase manager status
- fortinet.fortimanager.fmgr_pm_config_pblock_firewall_proxypolicy - Configure proxy policies.
- fortinet.fortimanager.fmgr_pm_config_pblock_firewall_proxypolicy_sectionvalue - Configure proxy policies.
- fortinet.fortimanager.fmgr_system_admin_user_policyblock - Policy block write access.
- fortinet.fortimanager.fmgr_system_fmgcluster - fmg clsuter.
- fortinet.fortimanager.fmgr_system_fmgcluster_peer - Peer.
- fortinet.fortimanager.fmgr_system_log_ueba - UEBAsettings.
- fortinet.fortimanager.fmgr_system_npu_icmpratectrl - Configure the rate of ICMP messages generated by this FortiGate.
- fortinet.fortimanager.fmgr_user_externalidentityprovider - Configure external identity provider.

infoblox.nios_modules
~~~~~~~~~~~~~~~~~~~~~

- infoblox.nios_modules.nios_extensible_attribute - Configure Infoblox NIOS extensible attribute definition
- infoblox.nios_modules.nios_nsgroup_delegation - Configure InfoBlox DNS Nameserver Delegation Groups
- infoblox.nios_modules.nios_nsgroup_forwardingmember - Configure InfoBlox DNS Nameserver Forward/Stub Server Groups
- infoblox.nios_modules.nios_nsgroup_forwardstubserver - Configure InfoBlox DNS Nameserver Forwarding Member Groups
- infoblox.nios_modules.nios_nsgroup_stubmember - Configure InfoBlox DNS Nameserver Stub Member Groups

kaytus.ksmanage
~~~~~~~~~~~~~~~

- kaytus.ksmanage.edit_system_lock_mode - Set system lock mode information
- kaytus.ksmanage.system_lock_mode_info - Get system lock mode information

microsoft.ad
~~~~~~~~~~~~

- microsoft.ad.service_account - Manage Active Directory service account objects

netbox.netbox
~~~~~~~~~~~~~

- netbox.netbox.netbox_permission - Creates or removes permissions from NetBox
- netbox.netbox.netbox_token - Creates or removes tokens from NetBox
- netbox.netbox.netbox_tunnel - Create, update or delete tunnels within NetBox
- netbox.netbox.netbox_tunnel_group - Create, update or delete tunnel groups within NetBox
- netbox.netbox.netbox_user - Creates or removes users from NetBox
- netbox.netbox.netbox_user_group - Creates or removes user groups from NetBox

purestorage.flasharray
~~~~~~~~~~~~~~~~~~~~~~

- purestorage.flasharray.purefa_audits - List FlashArray Audit Events
- purestorage.flasharray.purefa_dsrole_old - Configure FlashArray Directory Service Roles (pre-6.6.3)
- purestorage.flasharray.purefa_sessions - List FlashArray Sessions

purestorage.flashblade
~~~~~~~~~~~~~~~~~~~~~~

- purestorage.flashblade.purefb_saml - Manage FlashBlade SAML2 service and identity providers

theforeman.foreman
~~~~~~~~~~~~~~~~~~

- theforeman.foreman.content_import_info - List content imports
- theforeman.foreman.content_import_library - Manage library content imports
- theforeman.foreman.content_import_repository - Manage repository content imports
- theforeman.foreman.content_import_version - Manage content view version content imports

Unchanged Collections
---------------------

- community.ciscosmb (still version 1.0.9)
- community.hashi_vault (still version 6.2.0)
- community.libvirt (still version 1.3.0)
- community.rabbitmq (still version 1.3.0)
- community.sap_libs (still version 1.4.2)
- dellemc.unity (still version 2.0.0)
- ibm.spectrum_virtualize (still version 2.0.0)
- infinidat.infinibox (still version 1.4.5)
- openstack.cloud (still version 2.2.0)
- ovirt.ovirt (still version 3.2.0)
- sensu.sensu_go (still version 1.14.0)
