========================
Ansible 12 Release Notes
========================

This changelog describes changes since Ansible 11.0.0.

.. contents::
  :depth: 2

v12.0.0a4
=========

.. contents::
  :local:
  :depth: 2

Release Summary
---------------

Release Date: 2025-05-12

`Porting Guide <https://docs.ansible.com/ansible/devel/porting_guides.html>`_

Ansible-core
------------

Ansible 12.0.0a4 contains ansible-core version 2.19.0b4.
This is a newer version than version 2.19.0b3 contained in the previous Ansible release.

The changes are reported in the combined changelog below.

Changed Collections
-------------------

If not mentioned explicitly, the changes are reported in the combined changelog below.

+--------------------+------------------+------------------+------------------------------------------------------------------------------------------------------------------------------+
| Collection         | Ansible 12.0.0a3 | Ansible 12.0.0a4 | Notes                                                                                                                        |
+====================+==================+==================+==============================================================================================================================+
| amazon.aws         | 9.4.0            | 9.5.0            |                                                                                                                              |
+--------------------+------------------+------------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.meraki       | 2.21.0           | 2.21.1           |                                                                                                                              |
+--------------------+------------------+------------------+------------------------------------------------------------------------------------------------------------------------------+
| cyberark.pas       | 1.0.32           | 1.0.35           | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+--------------------+------------------+------------------+------------------------------------------------------------------------------------------------------------------------------+
| netapp.ontap       | 22.14.0          | 23.0.0           |                                                                                                                              |
+--------------------+------------------+------------------+------------------------------------------------------------------------------------------------------------------------------+
| netapp.storagegrid | 21.14.0          | 21.15.0          |                                                                                                                              |
+--------------------+------------------+------------------+------------------------------------------------------------------------------------------------------------------------------+

Major Changes
-------------

netapp.ontap
~~~~~~~~~~~~

- library `netapp-lib` is now an optional requirement.
- na_ontap_lun - added compatibility for ASA r2 systems.
- na_ontap_lun_copy - added check to prevent use on unsupported ASA r2 systems.
- na_ontap_lun_map - added compatibility for ASA r2 systems.
- na_ontap_lun_map_reporting_nodes - added compatibility for ASA r2 systems.
- na_ontap_nvme_namespace - added compatibility for ASA r2 systems.
- na_ontap_nvme_subsystem - added compatibility for ASA r2 systems.

Minor Changes
-------------

Ansible-core
~~~~~~~~~~~~

- facts - add "CloudStack KVM Hypervisor" for Linux VM in virtual facts (https://github.com/ansible/ansible/issues/85089).
- modules - use ``AnsibleModule.warn`` instead of passing ``warnings`` to ``exit_json`` or ``fail_json`` which is deprecated.

amazon.aws
~~~~~~~~~~

- Bump version of ansible-lint to 25.1.2 (https://github.com/ansible-collections/amazon.aws/pull/2590).
- iam_user_info - Add tags to ListUsers or GetGroup results (https://github.com/ansible-collections/amazon.aws/pull/2567).
- iam_user_info - Return empty user list when invalid group name is provided instead of python error (https://github.com/ansible-collections/amazon.aws/pull/2567).
- module_utils/modules.py - call to ``deprecate()`` without specifying ``collection_name``, ``version`` or ``date`` arguments raises a sanity errors (https://github.com/ansible-collections/amazon.aws/pull/2607).

netapp.ontap
~~~~~~~~~~~~

- all modules - defaults to certificate based authentication if `username,password` and `cert_filepath/key_filepath` are set.
- na_ontap_ndmp - Added get method to generate and retrieve ndmp user passowrd in REST.
- na_ontap_volume - updated documentation for `snapshot_auto_delete`.
- updated ZAPI deprecation warnings in README & module utilities.

netapp.storagegrid
~~~~~~~~~~~~~~~~~~

- na_sg_grid_ha_group - added check mode support in the module.
- na_sg_org_container - Enhanced the Consistency setting.
- na_sg_org_container - new option `capacity_limit` added for bucket, requires storageGRID 11.9 or later.

Breaking Changes / Porting Guide
--------------------------------

netapp.storagegrid
~~~~~~~~~~~~~~~~~~

- all modules - added ability to authenticate using `username/password` and `tenant_id` (for Tenant) in the module.

Bugfixes
--------

Ansible-core
~~~~~~~~~~~~

- ansible-test - Updated the ``pylint`` sanity test to skip some deprecation validation checks when all arguments are dynamic.
- config - Preserve or apply Origin tag to values returned by config.
- config - Prevented fatal errors when ``MODULE_IGNORE_EXTS`` configuration was set.
- config - Templating failures on config defaults now issue a warning. Previously, failures silently returned an unrendered and untrusted template to the caller.
- config - ``ensure_type`` correctly propagates trust and other tags on returned values.
- config - ``ensure_type`` now converts mappings to ``dict`` when requested, instead of returning the mapping.
- config - ``ensure_type`` now converts sequences to ``list`` when requested, instead of returning the sequence.
- config - ``ensure_type`` now correctly errors when ``pathlist`` or ``pathspec`` types encounter non-string list items.
- config - ``ensure_type`` now reports an error when ``bytes`` are provided for any known ``value_type``. Previously, the behavior was undefined, but often resulted in an unhandled exception or incorrect return type.
- config - ``ensure_type`` with expected type ``int`` now properly converts ``True`` and ``False`` values to ``int``. Previously, these values were silently returned unmodified.
- convert_bool.boolean API conversion function - Unhashable values passed to ``boolean`` behave like other non-boolean convertible values, returning False or raising ``TypeError`` depending on the value of ``strict``. Previously, unhashable values always raised ``ValueError`` due to an invalid set membership check.
- dnf5 - when ``bugfix`` and/or ``security`` is specified, skip packages that do not have any such updates, even for new versions of libdnf5 where this functionality changed and it is considered failure
- plugin loader - Apply template trust to strings loaded from plugin configuration definitions and doc fragments.
- template action - Template files where the entire file's output renders as ``None`` are no longer emitted as the string "None", but instead render to an empty file as in previous releases.

amazon.aws
~~~~~~~~~~

- iam_user_info - Actually call GetUser when only user name is supplied instead of listing and filtering from all users (https://github.com/ansible-collections/amazon.aws/pull/2567).
- iam_user_info - Actually filter users by path prefix when one is provided (https://github.com/ansible-collections/amazon.aws/pull/2567).
- route53_info - removes jijna delimiters from example using when (https://github.com/ansible-collections/amazon.aws/issues/2594).

cisco.meraki
~~~~~~~~~~~~

- cisco.meraki.devices_switch_ports - fix get_object_by_name method.

netapp.ontap
~~~~~~~~~~~~

- na_ontap_ems_config - fix issue with support check mode when proxy_password is not set in REST.
- na_ontap_quotas - changed examples in documentation for `type`.
- na_ontap_snapmirror - fix delete snapmirror timeout issue by retrying in REST.
- na_ontap_software_update - Updated documentation for `https`.
- na_ontap_user_role - fix issue with modifying privileges in REST.

netapp.storagegrid
~~~~~~~~~~~~~~~~~~

- na_sg_org_user - fix where existing users with no groups attached were not getting any groups added.

New Modules
-----------

netapp.ontap
~~~~~~~~~~~~

- netapp.ontap.na_ontap_mav_approval_group - NetApp ONTAP multi-admin verification (MAV) approval group
- netapp.ontap.na_ontap_mav_config - NetApp ONTAP multi-admin verification (MAV) global setting
- netapp.ontap.na_ontap_mav_rule - NetApp ONTAP multi-admin verification (MAV) rule
- netapp.ontap.na_ontap_storage_unit - NetApp ONTAP ASA r2 storage unit
- netapp.ontap.na_ontap_storage_unit_snapshot - NetApp ONTAP ASA r2 storage unit snapshot
- netapp.ontap.na_ontap_support_config_backup - NetApp ONTAP support configuration backup

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

Unchanged Collections
---------------------

- ansible.netcommon (still version 8.0.0)
- ansible.posix (still version 2.0.0)
- ansible.utils (still version 5.1.2)
- ansible.windows (still version 3.0.0)
- arista.eos (still version 11.0.0)
- awx.awx (still version 24.6.1)
- azure.azcollection (still version 3.3.1)
- check_point.mgmt (still version 6.4.0)
- chocolatey.chocolatey (still version 1.5.3)
- cisco.aci (still version 2.11.0)
- cisco.dnac (still version 6.31.3)
- cisco.intersight (still version 2.0.20)
- cisco.ios (still version 10.0.0)
- cisco.iosxr (still version 11.0.0)
- cisco.ise (still version 2.10.0)
- cisco.mso (still version 2.10.0)
- cisco.nxos (still version 10.0.0)
- cisco.ucs (still version 1.16.0)
- cloud.common (still version 4.0.0)
- cloudscale_ch.cloud (still version 2.4.1)
- community.aws (still version 9.3.0)
- community.ciscosmb (still version 1.0.10)
- community.crypto (still version 2.26.1)
- community.digitalocean (still version 1.27.0)
- community.dns (still version 3.2.3)
- community.docker (still version 4.6.0)
- community.general (still version 10.6.0)
- community.grafana (still version 2.2.0)
- community.hashi_vault (still version 6.2.0)
- community.hrobot (still version 2.3.0)
- community.library_inventory_filtering_v1 (still version 1.1.1)
- community.libvirt (still version 1.3.1)
- community.mongodb (still version 1.7.9)
- community.mysql (still version 3.13.0)
- community.okd (still version 4.0.1)
- community.postgresql (still version 4.0.0)
- community.proxysql (still version 1.6.0)
- community.rabbitmq (still version 1.4.0)
- community.routeros (still version 3.6.0)
- community.sap_libs (still version 1.4.2)
- community.sops (still version 2.0.5)
- community.vmware (still version 5.6.0)
- community.windows (still version 3.0.0)
- community.zabbix (still version 3.3.0)
- containers.podman (still version 1.16.3)
- cyberark.conjur (still version 1.3.3)
- dellemc.enterprise_sonic (still version 3.0.0)
- dellemc.openmanage (still version 9.12.0)
- dellemc.powerflex (still version 2.6.0)
- dellemc.unity (still version 2.0.0)
- f5networks.f5_modules (still version 1.35.0)
- fortinet.fortimanager (still version 2.9.1)
- fortinet.fortios (still version 2.4.0)
- grafana.grafana (still version 6.0.1)
- hetzner.hcloud (still version 4.3.0)
- hitachivantara.vspone_block (still version 3.4.0)
- ibm.qradar (still version 4.0.0)
- ibm.storage_virtualize (still version 2.7.3)
- ieisystem.inmanage (still version 3.0.0)
- infinidat.infinibox (still version 1.4.5)
- infoblox.nios_modules (still version 1.8.0)
- inspur.ispim (still version 2.2.3)
- junipernetworks.junos (still version 10.0.0)
- kaytus.ksmanage (still version 2.0.0)
- kubernetes.core (still version 5.2.0)
- kubevirt.core (still version 2.2.0)
- lowlydba.sqlserver (still version 2.6.1)
- microsoft.ad (still version 1.9.0)
- microsoft.iis (still version 1.0.2)
- netapp.cloudmanager (still version 21.24.0)
- netapp_eseries.santricity (still version 1.4.1)
- netbox.netbox (still version 3.21.0)
- ngine_io.cloudstack (still version 2.5.0)
- openstack.cloud (still version 2.4.1)
- ovirt.ovirt (still version 3.2.0)
- purestorage.flasharray (still version 1.34.1)
- purestorage.flashblade (still version 1.20.0)
- splunk.es (still version 4.0.0)
- telekom_mms.icinga_director (still version 2.2.2)
- theforeman.foreman (still version 5.3.0)
- vmware.vmware (still version 2.0.0)
- vmware.vmware_rest (still version 4.7.0)
- vultr.cloud (still version 1.13.0)
- vyos.vyos (still version 5.0.0)
- wti.remote (still version 1.0.10)

v12.0.0a3
=========

.. contents::
  :local:
  :depth: 2

Release Summary
---------------

Release Date: 2025-05-06

`Porting Guide <https://docs.ansible.com/ansible/devel/porting_guides.html>`_

Ansible-core
------------

Ansible 12.0.0a3 contains ansible-core version 2.19.0b3.
This is a newer version than version 2.19.0b2 contained in the previous Ansible release.

The changes are reported in the combined changelog below.

Changed Collections
-------------------

If not mentioned explicitly, the changes are reported in the combined changelog below.

+------------------------+------------------+------------------+------------------------------------------------------------------------------------------------------------------------------+
| Collection             | Ansible 12.0.0a2 | Ansible 12.0.0a3 | Notes                                                                                                                        |
+========================+==================+==================+==============================================================================================================================+
| ansible.windows        | 2.8.0            | 3.0.0            |                                                                                                                              |
+------------------------+------------------+------------------+------------------------------------------------------------------------------------------------------------------------------+
| community.aws          | 9.2.0            | 9.3.0            |                                                                                                                              |
+------------------------+------------------+------------------+------------------------------------------------------------------------------------------------------------------------------+
| community.crypto       | 2.26.0           | 2.26.1           |                                                                                                                              |
+------------------------+------------------+------------------+------------------------------------------------------------------------------------------------------------------------------+
| community.docker       | 4.5.2            | 4.6.0            |                                                                                                                              |
+------------------------+------------------+------------------+------------------------------------------------------------------------------------------------------------------------------+
| community.grafana      | 2.1.0            | 2.2.0            |                                                                                                                              |
+------------------------+------------------+------------------+------------------------------------------------------------------------------------------------------------------------------+
| community.hrobot       | 2.2.0            | 2.3.0            |                                                                                                                              |
+------------------------+------------------+------------------+------------------------------------------------------------------------------------------------------------------------------+
| community.postgresql   | 3.14.0           | 4.0.0            |                                                                                                                              |
+------------------------+------------------+------------------+------------------------------------------------------------------------------------------------------------------------------+
| community.windows      | 2.4.0            | 3.0.0            |                                                                                                                              |
+------------------------+------------------+------------------+------------------------------------------------------------------------------------------------------------------------------+
| cyberark.pas           | 1.0.30           | 1.0.32           | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+------------------------+------------------+------------------+------------------------------------------------------------------------------------------------------------------------------+
| dellemc.openmanage     | 9.11.0           | 9.12.0           |                                                                                                                              |
+------------------------+------------------+------------------+------------------------------------------------------------------------------------------------------------------------------+
| grafana.grafana        | 6.0.0            | 6.0.1            |                                                                                                                              |
+------------------------+------------------+------------------+------------------------------------------------------------------------------------------------------------------------------+
| kubevirt.core          | 2.1.0            | 2.2.0            | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+------------------------+------------------+------------------+------------------------------------------------------------------------------------------------------------------------------+
| lowlydba.sqlserver     | 2.6.0            | 2.6.1            |                                                                                                                              |
+------------------------+------------------+------------------+------------------------------------------------------------------------------------------------------------------------------+
| microsoft.ad           | 1.8.1            | 1.9.0            |                                                                                                                              |
+------------------------+------------------+------------------+------------------------------------------------------------------------------------------------------------------------------+
| purestorage.flashblade | 1.19.2           | 1.20.0           |                                                                                                                              |
+------------------------+------------------+------------------+------------------------------------------------------------------------------------------------------------------------------+
| vmware.vmware          | 1.11.0           | 2.0.0            |                                                                                                                              |
+------------------------+------------------+------------------+------------------------------------------------------------------------------------------------------------------------------+

Major Changes
-------------

community.postgresql
~~~~~~~~~~~~~~~~~~~~

- the collection does not test against Python 2 and starts accepting content written in Python 3 since collection version 4.0.0 (https://github.com/ansible-collections/community.postgresql/issues/829).

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- idrac_gather_facts - This role is enhanced to support iDRAC10.
- idrac_lifecycle_controller_job_status_info - This module is enhanced to support iDRAC10.
- idrac_system_info - This module is enhanced to support iDRAC10.

vmware.vmware
~~~~~~~~~~~~~

- cluster modules - Add identifying information about the cluster managed to the output of cluster modules
- folder_paths - Throw an error when a relative folder path is provided and the datacenter name is not provided
- module_utils/argument_spec - make argument specs public so other collections can use them https://github.com/ansible-collections/vmware.vmware/issues/144
- module_utils/clients - make client utils public so other collections can use them https://github.com/ansible-collections/vmware.vmware/issues/144
- update query file to include cluster module queries

Minor Changes
-------------

Ansible-core
~~~~~~~~~~~~

- ansible-config will now show internal, but not test configuration entries. This allows for debugging but still denoting the configurations as internal use only (_ prefix).
- ansible-test - Improved ``pylint`` checks for Ansible-specific deprecation functions.
- ansible-test - Use the ``-t`` option to set the stop timeout when stopping a container. This avoids use of the ``--time`` option which was deprecated in Docker v28.0.
- collection metadata - The collection loader now parses scalar values from ``meta/runtime.yml`` as strings. This avoids issues caused by unquoted values such as versions or dates being parsed as types other than strings.
- deprecation warnings - Deprecation warning APIs automatically capture the identity of the deprecating plugin. The ``collection_name`` argument is only required to correctly attribute deprecations that occur in module_utils or other non-plugin code.
- deprecation warnings - Improved deprecation messages to more clearly indicate the affected content, including plugin name when available.
- deprecations - Collection name strings not of the form ``ns.coll`` passed to deprecation API functions will result in an error.
- deprecations - Removed support for specifying deprecation dates as a ``datetime.date``, which was included in an earlier 2.19 pre-release.
- deprecations - Some argument names to ``deprecate_value`` for consistency with existing APIs. An earlier 2.19 pre-release included a ``removal_`` prefix on the ``date`` and ``version`` arguments.
- modules - The ``AnsibleModule.deprecate`` function no longer sends deprecation messages to the target host's logging system.

ansible.windows
~~~~~~~~~~~~~~~

- Set minimum supported Ansible version to 2.16 to align with the versions still supported by Ansible.
- win_template - Added ``comment_start_string`` and ``comment_end_string`` as options to align with the builtin ``template`` module.

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

community.grafana
~~~~~~~~~~~~~~~~~

- Add argument `tls_servername` for `grafana_datasource`
- Support `alertmanager` as type for `grafana_datasource`
- grafana_dashboard - allow creating dashboards in subfolders

community.postgresql
~~~~~~~~~~~~~~~~~~~~

- postgresql_user - return a PostgreSQL error message when a user cannot be removed.

community.windows
~~~~~~~~~~~~~~~~~

- Set minimum supported Ansible version to 2.16 to align with the versions still supported by Ansible.

grafana.grafana
~~~~~~~~~~~~~~~

- Remove Node modules from Ansible Collection build

lowlydba.sqlserver
~~~~~~~~~~~~~~~~~~

- Added support for Ansible 2.19
- Updated the test matrix to include Ansible 2.19 and remove Ansible 2.16

microsoft.ad
~~~~~~~~~~~~

- Set minimum supported Ansible version to 2.16 to align with the versions still supported by Ansible.

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

vmware.vmware
~~~~~~~~~~~~~

- Warn the user when more than one host has the same name in the inventory plugins. Throw an error if strict is true
- content_template - Added more options to search for the source VM like uuid and moid. Also made argument validation more accurate
- guest_info - Allow user to specify folder path to help select the VM to query
- rename private module_utils to drop the redundant vmware prefix
- vcsa_backup_schedule - Add module to manage the vCenter backup schedule
- vcsa_backup_schedule_info - Add module to gather info about the vCenter backup schedules
- vm_advanced_settings - Add module to manage the advanced settings on a VM
- vm_powerstate - Add better error message when scheduling a power state task in the past
- vm_snapshot - migrate vmware_guest_snapshot module from community to here
- vms inventory - Fixed issue where a user could accidentally not collect a required parameter, config.guestId

Breaking Changes / Porting Guide
--------------------------------

vmware.vmware
~~~~~~~~~~~~~

- drop support for ansible 2.15 since it is EOL https://github.com/ansible-collections/vmware.vmware/issues/103
- updated minimum pyVmomi version to 8.0.3.0.1 https://github.com/ansible-collections/vmware.vmware/issues/56

Deprecated Features
-------------------

Ansible-core
~~~~~~~~~~~~

- Passing a ``warnings` or ``deprecations`` key to ``exit_json`` or ``fail_json`` is deprecated. Use ``AnsibleModule.warn`` or ``AnsibleModule.deprecate`` instead.
- plugins - Accessing plugins with ``_``-prefixed filenames without the ``_`` prefix is deprecated.

community.postgresql
~~~~~~~~~~~~~~~~~~~~

- postgresql modules = the ``login``, ``unix_socket`` and ``host`` aliases are deprecated and will be removed in ``community.postgresql 5.0.0``, use the ``login_user``, ``login_unix_socket`` and ``login_host`` arguments instead.
- postgresql_set - the module has been deprecated and will be removed in ``community.postgresql 5.0.0``. Please use the ``community.postgresql.postgresql_alter_system`` module instead (https://github.com/ansible-collections/community.postgresql/issues/823).

community.windows
~~~~~~~~~~~~~~~~~

- win_audit_policy_system - Deprecated module and will be redirected to ``ansible.windows.win_audit_policy_system``. Use ``ansible.windows.win_audit_policy_system`` instead as the redirection will be removed in 4.0.0
- win_audit_rule - Deprecated module and will be redirected to ``ansible.windows.win_audit_rule``. Use ``ansible.windows.win_audit_rule`` instead as the redirection will be removed in 4.0.0
- win_auto_logon - Deprecated module and will be redirected to ``ansible.windows.win_auto_logon``. Use ``ansible.windows.win_auto_logon`` instead as the redirection will be removed in 4.0.0
- win_certificate_info - Deprecated module and will be redirected to ``ansible.windows.win_certificate_info``. Use ``ansible.windows.win_certificate_info`` instead as the redirection will be removed in 4.0.0
- win_computer_description - Deprecated module and will be redirected to ``ansible.windows.win_computer_description``. Use ``ansible.windows.win_computer_description`` instead as the redirection will be removed in 4.0.0
- win_credential - Deprecated module and will be redirected to ``ansible.windows.win_credential``. Use ``ansible.windows.win_credential`` instead as the redirection will be removed in 4.0.0
- win_dhcp_lease - Deprecated module and will be redirected to ``ansible.windows.win_dhcp_lease``. Use ``ansible.windows.win_dhcp_lease`` instead as the redirection will be removed in 4.0.0
- win_dns_record - Deprecated module and will be redirected to ``ansible.windows.win_dns_record``. Use ``ansible.windows.win_dns_record`` instead as the redirection will be removed in 4.0.0
- win_dns_zone - Deprecated module and will be redirected to ``ansible.windows.win_dns_zone``. Use ``ansible.windows.win_dns_zone`` instead as the redirection will be removed in 4.0.0
- win_eventlog - Deprecated module and will be redirected to ``ansible.windows.win_eventlog``. Use ``ansible.windows.win_eventlog`` instead as the redirection will be removed in 4.0.0
- win_feature_info - Deprecated module and will be redirected to ``ansible.windows.win_feature_info``. Use ``ansible.windows.win_feature_info`` instead as the redirection will be removed in 4.0.0
- win_file_compression - Deprecated module and will be redirected to ``ansible.windows.win_file_compression``. Use ``ansible.windows.win_file_compression`` instead as the redirection will be removed in 4.0.0
- win_firewall - Deprecated module and will be redirected to ``ansible.windows.win_firewall``. Use ``ansible.windows.win_firewall`` instead as the redirection will be removed in 4.0.0
- win_hosts - Deprecated module and will be redirected to ``ansible.windows.win_hosts``. Use ``ansible.windows.win_hosts`` instead as the redirection will be removed in 4.0.0
- win_hotfix - Deprecated module and will be redirected to ``ansible.windows.win_hotfix``. Use ``ansible.windows.win_hotfix`` instead as the redirection will be removed in 4.0.0
- win_http_proxy - Deprecated module and will be redirected to ``ansible.windows.win_http_proxy``. Use ``ansible.windows.win_http_proxy`` instead as the redirection will be removed in 4.0.0
- win_iis_virtualdirectory - Deprecated module, use ``microsoft.iis.virtual_directory`` instead as the module will be removed in 4.0.0
- win_iis_webapplication - Deprecated module, use ``microsoft.iis.web_application`` instead instead as the module will be removed in 4.0.0
- win_iis_webapppool - Deprecated module, use ``microsoft.iis.web_app_pool`` instead instead as the module will be removed in 4.0.0
- win_iis_webbinding - Deprecated module, use ``microsoft.iis.website`` instead instead as the module will be removed in 4.0.0
- win_iis_website - Deprecated module, use ``microsoft.iis.website`` instead instead as the module will be removed in 4.0.0
- win_inet_proxy - Deprecated module and will be redirected to ``ansible.windows.win_inet_proxy``. Use ``ansible.windows.win_inet_proxy`` instead as the redirection will be removed in 4.0.0
- win_listen_ports_facts - Deprecated module and will be redirected to ``ansible.windows.win_listen_ports_facts``. Use ``ansible.windows.win_listen_ports_facts`` instead as the redirection will be removed in 4.0.0
- win_mapped_drive - Deprecated module and will be redirected to ``ansible.windows.win_mapped_drive``. Use ``ansible.windows.win_mapped_drive`` instead as the redirection will be removed in 4.0.0
- win_product_facts - Deprecated module and will be redirected to ``ansible.windows.win_product_facts``. Use ``ansible.windows.win_product_facts`` instead as the redirection will be removed in 4.0.0
- win_region - Deprecated module and will be redirected to ``ansible.windows.win_region``. Use ``ansible.windows.win_region`` instead as the redirection will be removed in 4.0.0
- win_route - Deprecated module and will be redirected to ``ansible.windows.win_route``. Use ``ansible.windows.win_route`` instead as the redirection will be removed in 4.0.0
- win_timezone - Deprecated module and will be redirected to ``ansible.windows.win_timezone``. Use ``ansible.windows.win_timezone`` instead as the redirection will be removed in 4.0.0
- win_user_profile - Deprecated module and will be redirected to ``ansible.windows.win_user_profile``. Use ``ansible.windows.win_user_profile`` instead as the redirection will be removed in 4.0.0

Removed Features (previously deprecated)
----------------------------------------

ansible.windows
~~~~~~~~~~~~~~~

- win_domain - Removed deprecated module, use ``microsoft.ad.domain`` instead
- win_domain_controller - Removed deprecated module, use ``microsoft.ad.domain_controller`` instead
- win_domain_membership - Removed deprecated module, use ``microsoft.ad.membership`` instead
- win_feature - Removed deprecated return value ``restart_needed`` in ``feature_result``, use ``reboot_required`` instead
- win_updates - Removed deprecated return value ``filtered_reason``, use ``filtered_reasons`` instead

community.postgresql
~~~~~~~~~~~~~~~~~~~~

- postgresql_info - the db alias has been removed in ``community.postgresql 4.0.0``. Please use the ``login_db`` option instead (https://github.com/ansible-collections/community.postgresql/issues/801).
- postgresql_lang - the module has been removed in ``community.postgresql 4.0.0``. Please use the ``community.postgresql.postgresql_ext`` module instead (https://github.com/ansible-collections/community.postgresql/issues/561).
- postgresql_privs - the ``password`` argument has been removed in ``community.postgresql 4.0.0``. Use the ``login_password`` argument instead (https://github.com/ansible-collections/community.postgresql/issues/408).
- postgresql_user - the ``priv`` argument has been removed in ``community.postgresql 4.0.0``. Please use the ``community.postgresql.postgresql_privs`` module to grant/revoke privileges instead (https://github.com/ansible-collections/community.postgresql/issues/493).

community.windows
~~~~~~~~~~~~~~~~~

- win_domain_computer - Removed deprecated module, use ``microsoft.ad.computer`` instead
- win_domain_group - Removed deprecated module, use ``microsoft.ad.group`` instead
- win_domain_group_membership - Removed deprecated module, use ``microsoft.ad.membership`` instead
- win_domain_object_info - Removed deprecated module, use ``microsoft.ad.object_info`` instead
- win_domain_ou - Removed deprecated module, use ``microsoft.ad.ou`` instead
- win_domain_user - Removed deprecated module, use ``microsoft.ad.user`` instead
- win_lineinfile - Removed deprecated return value ``backup``, use ``backup_file`` instead
- win_xml - Removed deprecated, and undocumented, return value ``backup``, use ``backup_file`` instead

vmware.vmware
~~~~~~~~~~~~~

- vm_list_group_by_clusters - Tombstone module in favor of vmware.vmware.vm_list_group_by_clusters_info

Bugfixes
--------

Ansible-core
~~~~~~~~~~~~

- Ansible will now ensure predictable permissions on remote artifacts, until now it only ensured executable and relied on system masks for the rest.
- dnf5 - avoid generating excessive transaction entries in the dnf5 history (https://github.com/ansible/ansible/issues/85046)

ansible.windows
~~~~~~~~~~~~~~~

- win_find - allow users case sensitive match the filename (https://github.com/ansible-collections/ansible.windows/issues/473).
- win_powershell - Handle failure on output conversion when the output object uses a custom adapter set that fails to enumerate the method members. This is seen when using the output from ``Get-WmiObject`` - https://github.com/ansible-collections/ansible.windows/issues/767
- win_regedit - Handle decimal values with no decimal values which may be the result of a Jinja2 template
- win_template - Added support for Ansible 2.19 and the introduction of the data tagging feature.

community.crypto
~~~~~~~~~~~~~~~~

- luks_device - mark parameter ``passphrase_encoding`` as ``no_log=False`` to avoid confusing warning (https://github.com/ansible-collections/community.crypto/pull/867).
- luks_device - removing a specific keyslot with ``remove_keyslot`` caused the module to hang while cryptsetup was waiting for a passphrase from stdin, while the module did not supply one. Since a keyslot is not necessary, do not provide one (https://github.com/ansible-collections/community.crypto/issues/864, https://github.com/ansible-collections/community.crypto/pull/868).

community.grafana
~~~~~~~~~~~~~~~~~

- Remove field `apiVersion` from return of current `grafana_datasource` for working diff
- grafana_dashboard - add uid to payload
- test: replace more deprecated `TestCase.assertEquals` to support Python 3.12

community.windows
~~~~~~~~~~~~~~~~~

- win_format - fix crash when using path parameter without force option (https://github.com/ansible-collections/community.windows/pull/615).
- win_toast - fix title and message in the notification.

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- idrac_system_info - (Issue 812) - idrac_system_info fails on iDRAC10.

microsoft.ad
~~~~~~~~~~~~

- ldap inventory - Fix up support for Ansible 2.19.

purestorage.flashblade
~~~~~~~~~~~~~~~~~~~~~~

- purefb_bucket - Resolved issue with removing bucket quota
- purefb_info - Fixed issue after SMD Directory Services no longer avaible from REST 2.16
- purefb_policy - Fixed creation of snapshot policies with assigned filesystems and/or replica links
- purefb_s3acc - Fixed issue with public access config settings not being correctly for an account

vmware.vmware
~~~~~~~~~~~~~

- cluster_ha - Fix exception when cluster ha module checks for differences with VM monitoring configs
- fix method to lookup datastore clusters by name or moid https://github.com/ansible-collections/vmware.vmware/issues/152
- vm_snapshot - Make sure snapshot output is always included if state is present

Known Issues
------------

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- idrac_diagnostics - Issue(285322) - This module doesn't support export of diagnostics file to HTTP and HTTPS share via SOCKS proxy.
- idrac_firmware - Issue(279282) - This module does not support firmware update using HTTP, HTTPS, and FTP shares with authentication on iDRAC8.
- ome_smart_fabric_uplink - Issue(186024) - The module supported by OpenManage Enterprise Modular, however it does not allow the creation of multiple uplinks of the same name. If an uplink is created using the same name as an existing uplink, then the existing uplink is modified.

New Modules
-----------

community.hrobot
~~~~~~~~~~~~~~~~

- community.hrobot.storagebox_snapshot - Create, update, or delete a snapshot of a storage box.

purestorage.flashblade
~~~~~~~~~~~~~~~~~~~~~~

- purestorage.flashblade.purefb_bucket_access - Manage FlashBlade bucket access policies
- purestorage.flashblade.purefb_fleet - Manage Fusion Fleet
- purestorage.flashblade.purefb_server - Manage FlashBlade servers

Unchanged Collections
---------------------

- amazon.aws (still version 9.4.0)
- ansible.netcommon (still version 8.0.0)
- ansible.posix (still version 2.0.0)
- ansible.utils (still version 5.1.2)
- arista.eos (still version 11.0.0)
- awx.awx (still version 24.6.1)
- azure.azcollection (still version 3.3.1)
- check_point.mgmt (still version 6.4.0)
- chocolatey.chocolatey (still version 1.5.3)
- cisco.aci (still version 2.11.0)
- cisco.dnac (still version 6.31.3)
- cisco.intersight (still version 2.0.20)
- cisco.ios (still version 10.0.0)
- cisco.iosxr (still version 11.0.0)
- cisco.ise (still version 2.10.0)
- cisco.meraki (still version 2.21.0)
- cisco.mso (still version 2.10.0)
- cisco.nxos (still version 10.0.0)
- cisco.ucs (still version 1.16.0)
- cloud.common (still version 4.0.0)
- cloudscale_ch.cloud (still version 2.4.1)
- community.ciscosmb (still version 1.0.10)
- community.digitalocean (still version 1.27.0)
- community.dns (still version 3.2.3)
- community.general (still version 10.6.0)
- community.hashi_vault (still version 6.2.0)
- community.library_inventory_filtering_v1 (still version 1.1.1)
- community.libvirt (still version 1.3.1)
- community.mongodb (still version 1.7.9)
- community.mysql (still version 3.13.0)
- community.okd (still version 4.0.1)
- community.proxysql (still version 1.6.0)
- community.rabbitmq (still version 1.4.0)
- community.routeros (still version 3.6.0)
- community.sap_libs (still version 1.4.2)
- community.sops (still version 2.0.5)
- community.vmware (still version 5.6.0)
- community.zabbix (still version 3.3.0)
- containers.podman (still version 1.16.3)
- cyberark.conjur (still version 1.3.3)
- dellemc.enterprise_sonic (still version 3.0.0)
- dellemc.powerflex (still version 2.6.0)
- dellemc.unity (still version 2.0.0)
- f5networks.f5_modules (still version 1.35.0)
- fortinet.fortimanager (still version 2.9.1)
- fortinet.fortios (still version 2.4.0)
- hetzner.hcloud (still version 4.3.0)
- hitachivantara.vspone_block (still version 3.4.0)
- ibm.qradar (still version 4.0.0)
- ibm.storage_virtualize (still version 2.7.3)
- ieisystem.inmanage (still version 3.0.0)
- infinidat.infinibox (still version 1.4.5)
- infoblox.nios_modules (still version 1.8.0)
- inspur.ispim (still version 2.2.3)
- junipernetworks.junos (still version 10.0.0)
- kaytus.ksmanage (still version 2.0.0)
- kubernetes.core (still version 5.2.0)
- microsoft.iis (still version 1.0.2)
- netapp.cloudmanager (still version 21.24.0)
- netapp.ontap (still version 22.14.0)
- netapp.storagegrid (still version 21.14.0)
- netapp_eseries.santricity (still version 1.4.1)
- netbox.netbox (still version 3.21.0)
- ngine_io.cloudstack (still version 2.5.0)
- openstack.cloud (still version 2.4.1)
- ovirt.ovirt (still version 3.2.0)
- purestorage.flasharray (still version 1.34.1)
- splunk.es (still version 4.0.0)
- telekom_mms.icinga_director (still version 2.2.2)
- theforeman.foreman (still version 5.3.0)
- vmware.vmware_rest (still version 4.7.0)
- vultr.cloud (still version 1.13.0)
- vyos.vyos (still version 5.0.0)
- wti.remote (still version 1.0.10)

v12.0.0a2
=========

.. contents::
  :local:
  :depth: 2

Release Summary
---------------

Release Date: 2025-04-24

`Porting Guide <https://docs.ansible.com/ansible/devel/porting_guides.html>`_

Ansible-core
------------

Ansible 12.0.0a2 contains ansible-core version 2.19.0b2.
This is a newer version than version 2.19.0b1 contained in the previous Ansible release.

The changes are reported in the combined changelog below.

Changed Collections
-------------------

If not mentioned explicitly, the changes are reported in the combined changelog below.

+------------------------------------------+------------------+------------------+-------+
| Collection                               | Ansible 12.0.0a1 | Ansible 12.0.0a2 | Notes |
+==========================================+==================+==================+=======+
| cisco.aci                                | 2.10.1           | 2.11.0           |       |
+------------------------------------------+------------------+------------------+-------+
| cisco.meraki                             | 2.20.8           | 2.21.0           |       |
+------------------------------------------+------------------+------------------+-------+
| cisco.mso                                | 2.9.0            | 2.10.0           |       |
+------------------------------------------+------------------+------------------+-------+
| community.dns                            | 3.2.2            | 3.2.3            |       |
+------------------------------------------+------------------+------------------+-------+
| community.general                        | 10.5.0           | 10.6.0           |       |
+------------------------------------------+------------------+------------------+-------+
| community.library_inventory_filtering_v1 | 1.1.0            | 1.1.1            |       |
+------------------------------------------+------------------+------------------+-------+
| community.routeros                       | 3.5.0            | 3.6.0            |       |
+------------------------------------------+------------------+------------------+-------+
| community.sops                           | 2.0.4            | 2.0.5            |       |
+------------------------------------------+------------------+------------------+-------+
| community.vmware                         | 5.5.0            | 5.6.0            |       |
+------------------------------------------+------------------+------------------+-------+
| grafana.grafana                          | 5.7.0            | 6.0.0            |       |
+------------------------------------------+------------------+------------------+-------+
| hitachivantara.vspone_block              | 3.3.0            | 3.4.0            |       |
+------------------------------------------+------------------+------------------+-------+

Major Changes
-------------

grafana.grafana
~~~~~~~~~~~~~~~

- Add tempo role by @CSTDev in https://github.com/grafana/grafana-ansible-collection/pull/323
- Do not log grafana.ini contents when setting facts by @root-expert in https://github.com/grafana/grafana-ansible-collection/pull/325
- Fix loki_operational_config section not getting rendered in config.yml by @olegkaspersky in https://github.com/grafana/grafana-ansible-collection/pull/330
- Fix sectionless items edge case by @santilococo in https://github.com/grafana/grafana-ansible-collection/pull/303
- Fix tags Inherit default vars by @MJurayev in https://github.com/grafana/grafana-ansible-collection/pull/341
- Fix the markdown code fences for install command by @benmatselby in https://github.com/grafana/grafana-ansible-collection/pull/306
- Grafana fix facts in main.yml by @voidquark in https://github.com/grafana/grafana-ansible-collection/pull/315
- Make dashboard imports more flexible by @torfbolt in https://github.com/grafana/grafana-ansible-collection/pull/308
- force temporary directory even in check mode for  dashboards.yml by @cmehat in https://github.com/grafana/grafana-ansible-collection/pull/339
- integrate sles legacy init-script support by @floerica in https://github.com/grafana/grafana-ansible-collection/pull/184
- management of the config.river with the conversion of the config.yaml by @lbrule in https://github.com/grafana/grafana-ansible-collection/pull/149

Minor Changes
-------------

Ansible-core
~~~~~~~~~~~~

- comment filter - Improve the error message shown when an invalid ``style`` argument is provided.

cisco.aci
~~~~~~~~~

- Add aci_endpoint_tag_ip and aci_endpoint_tag_mac modules to manage Endpoint IP and MAC Tags.
- Add aci_ip_sla_monitoring_policy module.
- Add management_epg and management_epg_type attributes in aci_dns_profile module.
- Add stratum attribute to aci_ntp_policy module.
- Add support for Ansible 2.18 and dropped support for Ansible 2.15 as required by Ansible Galaxy.

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

hitachivantara.vspone_block
~~~~~~~~~~~~~~~~~~~~~~~~~~~

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

Deprecated Features
-------------------

community.general
~~~~~~~~~~~~~~~~~

- manifold lookup plugin - plugin is deprecated and will be removed in community.general 11.0.0 (https://github.com/ansible-collections/community.general/pull/10028).
- stackpath_compute inventory plugin - plugin is deprecated and will be removed in community.general 11.0.0 (https://github.com/ansible-collections/community.general/pull/10026).

community.vmware
~~~~~~~~~~~~~~~~

- vmware_dvs_portgroup - ``mac_learning`` is deprecated in favour of ``network_policy.mac_learning`` (https://github.com/ansible-collections/community.vmware/pull/2360).

Bugfixes
--------

Ansible-core
~~~~~~~~~~~~

- Remove use of `required` parameter in `get_bin_path` which has been deprecated.
- ansible-doc - fix indentation for first line of descriptions of suboptions and sub-return values (https://github.com/ansible/ansible/pull/84690).
- ansible-doc - fix line wrapping for first line of description of options and return values (https://github.com/ansible/ansible/pull/84690).

cisco.aci
~~~~~~~~~

- Fix aci_rest module to only add annotation when the value is a dictionary
- Fix payload to define the correct vPC member side in aci_l3out_logical_interface_vpc_member (#663)
- Fix subclass issue in aci_domain_to_vlan_pool to fix deletion of binding (#695)
- Modify interface_configs requirement using required_if dependency for aci_bulk_static_binding_to_epg

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

community.vmware
~~~~~~~~~~~~~~~~

- vmware_dvs_portgroup - Fix idempotency issue with ``mac_learning`` (https://github.com/ansible-collections/community.vmware/issues/1873).

Known Issues
------------

community.general
~~~~~~~~~~~~~~~~~

- reveal_ansible_type filter plugin and ansible_type test plugin - note that ansible-core's Data Tagging feature implements new aliases, such as ``_AnsibleTaggedStr`` for ``str``, ``_AnsibleTaggedInt`` for ``int``, and ``_AnsibleTaggedFloat`` for ``float`` (https://github.com/ansible-collections/community.general/pull/9833).

New Plugins
-----------

Connection
~~~~~~~~~~

- community.general.wsl - Run tasks in WSL distribution using wsl.exe CLI via SSH.

New Modules
-----------

hitachivantara.vspone_block
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Vsp
^^^

- hitachivantara.vspone_block.hv_ddp_pool - Manages DDP Pools on Hitachi VSP storage systems.
- hitachivantara.vspone_block.hv_ddp_pool_facts - Get facts of DDP Pools on Hitachi VSP storage systems.

Unchanged Collections
---------------------

- amazon.aws (still version 9.4.0)
- ansible.netcommon (still version 8.0.0)
- ansible.posix (still version 2.0.0)
- ansible.utils (still version 5.1.2)
- ansible.windows (still version 2.8.0)
- arista.eos (still version 11.0.0)
- awx.awx (still version 24.6.1)
- azure.azcollection (still version 3.3.1)
- check_point.mgmt (still version 6.4.0)
- chocolatey.chocolatey (still version 1.5.3)
- cisco.dnac (still version 6.31.3)
- cisco.intersight (still version 2.0.20)
- cisco.ios (still version 10.0.0)
- cisco.iosxr (still version 11.0.0)
- cisco.ise (still version 2.10.0)
- cisco.nxos (still version 10.0.0)
- cisco.ucs (still version 1.16.0)
- cloud.common (still version 4.0.0)
- cloudscale_ch.cloud (still version 2.4.1)
- community.aws (still version 9.2.0)
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
- community.okd (still version 4.0.1)
- community.postgresql (still version 3.14.0)
- community.proxysql (still version 1.6.0)
- community.rabbitmq (still version 1.4.0)
- community.sap_libs (still version 1.4.2)
- community.windows (still version 2.4.0)
- community.zabbix (still version 3.3.0)
- containers.podman (still version 1.16.3)
- cyberark.conjur (still version 1.3.3)
- cyberark.pas (still version 1.0.30)
- dellemc.enterprise_sonic (still version 3.0.0)
- dellemc.openmanage (still version 9.11.0)
- dellemc.powerflex (still version 2.6.0)
- dellemc.unity (still version 2.0.0)
- f5networks.f5_modules (still version 1.35.0)
- fortinet.fortimanager (still version 2.9.1)
- fortinet.fortios (still version 2.4.0)
- hetzner.hcloud (still version 4.3.0)
- ibm.qradar (still version 4.0.0)
- ibm.storage_virtualize (still version 2.7.3)
- ieisystem.inmanage (still version 3.0.0)
- infinidat.infinibox (still version 1.4.5)
- infoblox.nios_modules (still version 1.8.0)
- inspur.ispim (still version 2.2.3)
- junipernetworks.junos (still version 10.0.0)
- kaytus.ksmanage (still version 2.0.0)
- kubernetes.core (still version 5.2.0)
- kubevirt.core (still version 2.1.0)
- lowlydba.sqlserver (still version 2.6.0)
- microsoft.ad (still version 1.8.1)
- microsoft.iis (still version 1.0.2)
- netapp.cloudmanager (still version 21.24.0)
- netapp.ontap (still version 22.14.0)
- netapp.storagegrid (still version 21.14.0)
- netapp_eseries.santricity (still version 1.4.1)
- netbox.netbox (still version 3.21.0)
- ngine_io.cloudstack (still version 2.5.0)
- openstack.cloud (still version 2.4.1)
- ovirt.ovirt (still version 3.2.0)
- purestorage.flasharray (still version 1.34.1)
- purestorage.flashblade (still version 1.19.2)
- splunk.es (still version 4.0.0)
- telekom_mms.icinga_director (still version 2.2.2)
- theforeman.foreman (still version 5.3.0)
- vmware.vmware (still version 1.11.0)
- vmware.vmware_rest (still version 4.7.0)
- vultr.cloud (still version 1.13.0)
- vyos.vyos (still version 5.0.0)
- wti.remote (still version 1.0.10)

v12.0.0a1
=========

.. contents::
  :local:
  :depth: 2

Release Summary
---------------

Release Date: 2025-04-16

`Porting Guide <https://docs.ansible.com/ansible/devel/porting_guides.html>`_

Removed Collections
-------------------

- cisco.asa (previously included version: 6.0.0)
- community.network (previously included version: 5.1.0)
- google.cloud (previously included version: 1.4.1)
- ibm.spectrum_virtualize (previously included version: 2.0.0)
- sensu.sensu_go (previously included version: 1.14.0)

You can still install a removed collection manually with ``ansible-galaxy collection install <name-of-collection>``.

Added Collections
-----------------

- hitachivantara.vspone_block (version 3.3.0)
- microsoft.iis (version 1.0.2)

Ansible-core
------------

Ansible 12.0.0a1 contains ansible-core version 2.19.0b1.
This is a newer version than version 2.18.0 contained in the previous Ansible release.

The changes are reported in the combined changelog below.

Included Collections
--------------------

If not mentioned explicitly, the changes are reported in the combined changelog below.

+------------------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Collection                               | Ansible 11.0.0 | Ansible 12.0.0a1 | Notes                                                                                                                                                                                                           |
+==========================================+================+==================+=================================================================================================================================================================================================================+
| amazon.aws                               | 9.0.0          | 9.4.0            |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ansible.netcommon                        | 7.1.0          | 8.0.0            |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ansible.posix                            | 1.6.2          | 2.0.0            |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ansible.windows                          | 2.5.0          | 2.8.0            |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| arista.eos                               | 10.0.1         | 11.0.0           |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| azure.azcollection                       | 3.0.0          | 3.3.1            | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.                                                                                    |
+------------------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| check_point.mgmt                         | 6.2.1          | 6.4.0            |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cisco.dnac                               | 6.22.0         | 6.31.3           |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cisco.ios                                | 9.0.3          | 10.0.0           |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cisco.iosxr                              | 10.2.2         | 11.0.0           |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cisco.ise                                | 2.9.5          | 2.10.0           |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cisco.meraki                             | 2.18.3         | 2.20.8           |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cisco.nxos                               | 9.2.1          | 10.0.0           |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cisco.ucs                                | 1.14.0         | 1.16.0           | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.                                                                                    |
+------------------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cloudscale_ch.cloud                      | 2.4.0          | 2.4.1            |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.aws                            | 9.0.0          | 9.2.0            |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.ciscosmb                       | 1.0.9          | 1.0.10           |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.crypto                         | 2.22.3         | 2.26.0           |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.dns                            | 3.0.7          | 3.2.2            |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.docker                         | 4.0.1          | 4.5.2            |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.general                        | 10.0.1         | 10.5.0           |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.hrobot                         | 2.0.2          | 2.2.0            |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.library_inventory_filtering_v1 | 1.0.2          | 1.1.0            |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.libvirt                        | 1.3.0          | 1.3.1            |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.mongodb                        | 1.7.8          | 1.7.9            | There are no changes recorded in the changelog.                                                                                                                                                                 |
+------------------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.mysql                          | 3.10.3         | 3.13.0           |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.okd                            | 4.0.0          | 4.0.1            |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.postgresql                     | 3.7.0          | 3.14.0           |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.rabbitmq                       | 1.3.0          | 1.4.0            |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.routeros                       | 3.0.0          | 3.5.0            |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.sops                           | 2.0.0          | 2.0.4            |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.vmware                         | 5.1.0          | 5.5.0            |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.windows                        | 2.3.0          | 2.4.0            |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.zabbix                         | 3.1.2          | 3.3.0            |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| containers.podman                        | 1.16.2         | 1.16.3           |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cyberark.conjur                          | 1.3.1          | 1.3.3            | You can find the collection's changelog at `https://github.com/cyberark/ansible-conjur-collection/blob/master/CHANGELOG.md <https://github.com/cyberark/ansible-conjur-collection/blob/master/CHANGELOG.md>`__. |
+------------------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cyberark.pas                             | 1.0.27         | 1.0.30           | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.                                                                                    |
+------------------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| dellemc.enterprise_sonic                 | 2.5.1          | 3.0.0            |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| dellemc.openmanage                       | 9.8.0          | 9.11.0           |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| dellemc.powerflex                        | 2.5.0          | 2.6.0            |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| f5networks.f5_modules                    | 1.32.1         | 1.35.0           |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| fortinet.fortimanager                    | 2.7.0          | 2.9.1            |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| fortinet.fortios                         | 2.3.8          | 2.4.0            |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| grafana.grafana                          | 5.6.0          | 5.7.0            |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| hetzner.hcloud                           | 4.2.1          | 4.3.0            |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| hitachivantara.vspone_block              |                | 3.3.0            | The collection was added to Ansible                                                                                                                                                                             |
+------------------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ibm.storage_virtualize                   | 2.5.0          | 2.7.3            |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| infoblox.nios_modules                    | 1.7.0          | 1.8.0            |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| junipernetworks.junos                    | 9.1.0          | 10.0.0           |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| kubernetes.core                          | 5.0.0          | 5.2.0            |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| lowlydba.sqlserver                       | 2.3.4          | 2.6.0            |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| microsoft.ad                             | 1.7.1          | 1.8.1            |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| microsoft.iis                            |                | 1.0.2            | The collection was added to Ansible                                                                                                                                                                             |
+------------------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| netapp.ontap                             | 22.12.0        | 22.14.0          |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| netapp.storagegrid                       | 21.13.0        | 21.14.0          |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| netbox.netbox                            | 3.20.0         | 3.21.0           |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| openstack.cloud                          | 2.2.0          | 2.4.1            | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.                                                                                    |
+------------------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| purestorage.flasharray                   | 1.31.1         | 1.34.1           |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| purestorage.flashblade                   | 1.19.1         | 1.19.2           |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| telekom_mms.icinga_director              | 2.2.0          | 2.2.2            |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| theforeman.foreman                       | 4.2.0          | 5.3.0            |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| vmware.vmware                            | 1.6.0          | 1.11.0           |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| vmware.vmware_rest                       | 4.2.0          | 4.7.0            |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Major Changes
-------------

Ansible-core
~~~~~~~~~~~~

- Jinja plugins - Jinja builtin filter and test plugins are now accessible via their fully-qualified names ``ansible.builtin.{name}``.
- Task Execution / Forks - Forks no longer inherit stdio from the parent ``ansible-playbook`` process. ``stdout``, ``stderr``, and ``stdin`` within a worker are detached from the terminal, and non-functional. All needs to access stdio from a fork for controller side plugins requires use of ``Display``.
- ansible-test - Packages beneath ``module_utils`` can now contain ``__init__.py`` files.
- variables - The type system underlying Ansible's variable storage has been significantly overhauled and formalized. Attempts to store unsupported Python object types in variables will now result in an error.
- variables - To support new Ansible features, many variable objects are now represented by subclasses of their respective native Python types. In most cases, they behave indistinguishably from their original types, but some Python libraries do not handle builtin object subclasses properly. Custom plugins that interact with such libraries may require changes to convert and pass the native types.

ansible.netcommon
~~~~~~~~~~~~~~~~~

- Bumping `requires_ansible` to `>=2.16.0`, since previous ansible-core versions are EoL now.

arista.eos
~~~~~~~~~~

- Bumping `requires_ansible` to `>=2.16.0`, since previous ansible-core versions are EoL now.

cisco.ios
~~~~~~~~~

- Bumping `requires_ansible` to `>=2.16.0`, since previous ansible-core versions are EoL now.

cisco.iosxr
~~~~~~~~~~~

- Bumping `requires_ansible` to `>=2.16.0`, since previous ansible-core versions are EoL now.

cisco.nxos
~~~~~~~~~~

- Bumping `requires_ansible` to `>=2.16.0`, since previous ansible-core versions are EoL now.

community.vmware
~~~~~~~~~~~~~~~~

- vmware_dvswitch_pvlans - The VLAN ID type has been updated to be handled as an integer (https://github.com/ansible-collections/community.vmware/pull/2267).

community.zabbix
~~~~~~~~~~~~~~~~

- All Roles - Updated to support version 7.2

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- omevv_baseline_profile - This module allows to manage baseline profile.
- omevv_baseline_profile_info - This module allows to retrieve baseline profile information.
- omevv_compliance_info - This module allows to retrieve firmware compliance reports.
- omevv_firmware - This module allows to update firmware of the single host and single cluster.

fortinet.fortios
~~~~~~~~~~~~~~~~

- Support check_mode on all the configuration modules.
- Supported new versions 7.6.1 and 7.6.2.
- Updated the examples with correct values that have minimum or maximum values.

grafana.grafana
~~~~~~~~~~~~~~~

- Ability to set custom directory path for *.alloy config files by @voidquark in https://github.com/grafana/grafana-ansible-collection/pull/294
- Fix 'dict object' has no attribute 'path' when running with --check by @JMLX42 in https://github.com/grafana/grafana-ansible-collection/pull/283
- Update grafana template by @santilococo in https://github.com/grafana/grafana-ansible-collection/pull/300
- add loki bloom support by @voidquark in https://github.com/grafana/grafana-ansible-collection/pull/298
- grafana.ini yaml syntax by @intermittentnrg in https://github.com/grafana/grafana-ansible-collection/pull/232

junipernetworks.junos
~~~~~~~~~~~~~~~~~~~~~

- Bumping `requires_ansible` to `>=2.16.0`, since previous ansible-core versions are EoL now.

Minor Changes
-------------

Ansible-core
~~~~~~~~~~~~

- Added a -vvvvv log message indicating when a host fails to produce output within the timeout period.
- AnsibleModule.uri - Add option ``multipart_encoding`` for ``form-multipart`` files in body to change default base64 encoding for files
- INVENTORY_IGNORE_EXTS config, removed ``ini`` from the default list, inventory scripts using a corresponding .ini configuration are rare now and inventory.ini files are more common. Those that need to ignore the ini files for inventory scripts can still add it to configuration.
- Jinja plugins - Plugins can declare support for undefined values.
- Jinja2 version 3.1.0 or later is now required on the controller.
- Move ``follow_redirects`` parameter to module_utils so external modules can reuse it.
- PlayIterator - do not return tasks from already executed roles so specific strategy plugins do not have to do the filtering of such tasks themselves
- SSH Escalation-related -vvv log messages now include the associated host information.
- Windows - Add support for Windows Server 2025 to Ansible and as an ``ansible-test`` remote target - https://github.com/ansible/ansible/issues/84229
- Windows - refactor the async implementation to better handle errors during bootstrapping and avoid WMI when possible.
- ``ansible-galaxy collection install`` — the collection dependency resolver now prints out conflicts it hits during dependency resolution when it's taking too long and it ends up backtracking a lot. It also displays suggestions on how to help it compute the result more quickly.
- ansible, ansible-console, ansible-pull - add --flush-cache option (https://github.com/ansible/ansible/issues/83749).
- ansible-galaxy - Add support for Keycloak service accounts
- ansible-galaxy - support ``resolvelib >= 0.5.3, < 2.0.0`` (https://github.com/ansible/ansible/issues/84217).
- ansible-test - Added a macOS 15.3 remote VM, replacing 14.3.
- ansible-test - Automatically retry HTTP GET/PUT/DELETE requests on exceptions.
- ansible-test - Default to Python 3.13 in the ``base`` and ``default`` containers.
- ansible-test - Disable the ``deprecated-`` prefixed ``pylint`` rules as their results vary by Python version.
- ansible-test - Disable the ``pep8`` sanity test rules ``E701`` and ``E704`` to improve compatibility with ``black``.
- ansible-test - Improve container runtime probe error handling. When unexpected probe output is encountered, an error with more useful debugging information is provided.
- ansible-test - Replace container Alpine 3.20 with 3.21.
- ansible-test - Replace container Fedora 40 with 41.
- ansible-test - Replace remote Alpine 3.20 with 3.21.
- ansible-test - Replace remote Fedora 40 with 41.
- ansible-test - Replace remote FreeBSD 13.3 with 13.5.
- ansible-test - Replace remote FreeBSD 14.1 with 14.2.
- ansible-test - Replace remote RHEL 9.4 with 9.5.
- ansible-test - Show a more user-friendly error message when a ``runme.sh`` script is not executable.
- ansible-test - The ``yamllint`` sanity test now enforces string values for the ``!vault`` tag.
- ansible-test - Update ``nios-test-container`` to version 7.0.0.
- ansible-test - Update ``pylint`` sanity test to use version 3.3.1.
- ansible-test - Update distro containers to remove unnecessary pakages (apache2, subversion, ruby).
- ansible-test - Update sanity test requirements to latest available versions.
- ansible-test - Update the HTTP test container.
- ansible-test - Update the PyPI test container.
- ansible-test - Update the ``base`` and ``default`` containers.
- ansible-test - Update the utility container.
- ansible-test - Use Python's ``urllib`` instead of ``curl`` for HTTP requests.
- ansible-test - When detection of the current container network fails, a warning is now issued and execution continues. This simplifies usage in cases where the current container cannot be inspected, such as when running in GitHub Codespaces.
- ansible-test acme test container - bump `version to 2.3.0 <https://github.com/ansible/acme-test-container/releases/tag/2.3.0>`__ to include newer versions of Pebble, dependencies, and runtimes. This adds support for ACME profiles, ``dns-account-01`` support, and some smaller improvements (https://github.com/ansible/ansible/pull/84547).
- apt_key module - add notes to docs and errors to point at the CLI tool deprecation by Debian and alternatives
- apt_repository module - add notes to errors to point at the CLI tool deprecation by Debian and alternatives
- become plugins get new property 'pipelining' to show support or lack there of for the feature.
- callback plugins - add has_option() to CallbackBase to match other functions overloaded from AnsiblePlugin
- callback plugins - fix get_options() for CallbackBase
- copy - fix sanity test failures (https://github.com/ansible/ansible/pull/83643).
- copy - parameter ``local_follow`` was incorrectly documented as having default value ``True`` (https://github.com/ansible/ansible/pull/83643).
- cron - Provide additional error information while writing cron file (https://github.com/ansible/ansible/issues/83223).
- csvfile - let the config system do the typecasting (https://github.com/ansible/ansible/pull/82263).
- display - Deduplication of warning and error messages considers the full content of the message (including source and traceback contexts, if enabled). This may result in fewer messages being omitted.
- distribution - Added openSUSE MicroOS to Suse OS family (#84685).
- dnf5, apt - add ``auto_install_module_deps`` option (https://github.com/ansible/ansible/issues/84206)
- docs - add collection name in message from which the module is being deprecated (https://github.com/ansible/ansible/issues/84116).
- env lookup - The error message generated for a missing environment variable when ``default`` is an undefined value (e.g. ``undef('something')``) will contain the hint from that undefined value, except when the undefined value is the default of ``undef()`` with no arguments. Previously, any existing undefined hint would be ignored.
- file - enable file module to disable diff_mode (https://github.com/ansible/ansible/issues/80817).
- file - make code more readable and simple.
- filter - add support for URL-safe encoding and decoding in b64encode and b64decode (https://github.com/ansible/ansible/issues/84147).
- find - add a checksum_algorithm parameter to specify which type of checksum the module will return
- from_json filter - The filter accepts a ``profile`` argument, which defaults to ``tagless``.
- handlers - Templated handler names with syntax errors, or that resolve to ``omit`` are now skipped like handlers with undefined variables in their name.
- improved error message for yaml parsing errors in plugin documentation
- local connection plugin - A new ``become_strip_preamble`` config option (default True) was added; disable to preserve diagnostic ``become`` output in task results.
- local connection plugin - A new ``become_success_timeout`` operation-wide timeout config (default 10s) was added for ``become``.
- local connection plugin - When a ``become`` plugin's ``prompt`` value is a non-string after the ``check_password_prompt`` callback has completed, no prompt stripping will occur on stderr.
- lookup_template - add an option to trim blocks while templating (https://github.com/ansible/ansible/issues/75962).
- module - set ipv4 and ipv6 rules simultaneously in iptables module (https://github.com/ansible/ansible/issues/84404).
- module_utils - Add ``NoReturn`` type annotations to functions which never return.
- modules - PowerShell modules can now receive ``datetime.date``, ``datetime.time`` and ``datetime.datetime`` values as ISO 8601 strings.
- modules - PowerShell modules can now receive strings sourced from inline vault-encrypted strings.
- modules - Unhandled exceptions during Python module execution are now returned as structured data from the target. This allows the new traceback handling to be applied to exceptions raised on targets.
- pipelining logic has mostly moved to connection plugins so they can decide/override settings.
- plugin error handling - When raising exceptions in an exception handler, be sure to use ``raise ... from`` as appropriate. This supersedes the use of the ``AnsibleError`` arg ``orig_exc`` to represent the cause. Specifying ``orig_exc`` as the cause is still permitted. Failure to use ``raise ... from`` when ``orig_exc`` is set will result in a warning. Additionally, if the two cause exceptions do not match, a warning will be issued.
- removed harcoding of su plugin as it now works with pipelining.
- runtime-metadata sanity test - improve validation of ``action_groups`` (https://github.com/ansible/ansible/pull/83965).
- service_facts module got freebsd support added.
- ssh connection plugin - Support ``SSH_ASKPASS`` mechanism to provide passwords, making it the default, but still offering an explicit choice to use ``sshpass`` (https://github.com/ansible/ansible/pull/83936)
- ssh connection plugin now overrides pipelining when a tty is requested.
- ssh-agent - ``ansible``, ``ansible-playbook`` and ``ansible-console`` are capable of spawning or reusing an ssh-agent, allowing plugins to interact with the ssh-agent. Additionally a pure python ssh-agent client has been added, enabling easy interaction with the agent. The ssh connection plugin contains new functionality via ``ansible_ssh_private_key`` and ``ansible_ssh_private_key_passphrase``, for loading an SSH private key into the agent from a variable.
- templating - Access to an undefined variable from inside a lookup, filter, or test (which raises MarkerError) no longer ends processing of the current template. The triggering undefined value is returned as the result of the offending plugin invocation, and the template continues to execute.
- templating - Embedding ``range()`` values in containers such as lists will result in an error on use. Previously the value would be converted to a string representing the range parameters, such as ``range(0, 3)``.
- templating - Handling of omitted values is now a first-class feature of the template engine, and is usable in all Ansible Jinja template contexts. Any template that resolves to ``omit`` is automatically removed from its parent container during templating.
- templating - Template evaluation is lazier than in previous versions. Template expressions which resolve only portions of a data structure no longer result in the entire structure being templated.
- templating - Templating errors now provide more information about both the location and context of the error, especially for deeply-nested and/or indirected templating scenarios.
- templating - Unified ``omit`` behavior now requires that plugins calling ``Templar.template()`` handle cases where the entire template result is omitted, by catching the ``AnsibleValueOmittedError`` that is raised. Previously, this condition caused a randomly-generated string marker to appear in the template result.
- templating - Variables of type ``set`` and ``tuple`` are now converted to ``list`` when exiting the final pass of templating.
- to_json / to_nice_json filters - The filters accept a ``profile`` argument, which defaults to ``tagless``.
- troubleshooting - Tracebacks can be collected and displayed for most errors, warnings, and deprecation warnings (including those generated by modules). Tracebacks are no longer enabled with ``-vvv``; the behavior is directly configurable via the ``DISPLAY_TRACEBACK`` config option. Module tracebacks passed to ``fail_json`` via the ``exception`` kwarg will not be included in the task result unless error tracebacks are configured.
- undef jinja function - The ``undef`` jinja function now raises an error if a non-string hint is given. Attempting to use an undefined hint also results in an error, ensuring incorrect use of the function can be distinguished from the function's normal behavior.
- validate-modules sanity test - make sure that ``module`` and ``plugin`` ``seealso`` entries use FQCNs (https://github.com/ansible/ansible/pull/84325).
- vault - improved vault filter documentation by adding missing example content for dump_template_data.j2, refining examples for clarity, and ensuring variable consistency (https://github.com/ansible/ansible/issues/83583).
- warnings - All warnings (including deprecation warnings) issued during a task's execution are now accessible via the ``warnings`` and ``deprecations`` keys on the task result.
- when the ``dict`` lookup is given a non-dict argument, show the value of the argument and its type in the error message.
- windows - add hard minimum limit for PowerShell to 5.1. Ansible dropped support for older versions of PowerShell in the 2.16 release but this reqirement is now enforced at runtime.
- windows - refactor windows exec runner to improve efficiency and add better error reporting on failures.
- winrm - Remove need for pexpect on macOS hosts when using ``kinit`` to retrieve the Kerberos TGT. By default the code will now only use the builtin ``subprocess`` library which should handle issues with select and a high fd count and also simplify the code.

amazon.aws
~~~~~~~~~~

- autoscaling_group - adds ``group_name`` as an alias for the ``name`` parameter (https://github.com/ansible-collections/amazon.aws/pull/2396).
- autoscaling_group - avoid assignment to unused variable in except block (https://github.com/ansible-collections/amazon.aws/pull/2464).
- autoscaling_group_info - adds ``group_name`` as an alias for the ``name`` parameter (https://github.com/ansible-collections/amazon.aws/pull/2396).
- autoscaling_instance_refresh - adds ``group_name`` as an alias for the ``name`` parameter (https://github.com/ansible-collections/amazon.aws/pull/2396).
- autoscaling_instance_refresh_info - adds ``group_name`` as an alias for the ``name`` parameter (https://github.com/ansible-collections/amazon.aws/pull/2396).
- ec2_ami - avoid redefining ``delete_snapshot`` inside ``DeregisterImage.do`` (https://github.com/ansible-collections/amazon.aws/pull/2444).
- ec2_instance - Fix the issue when trying to run instances using launch template in an AWS environment where no default subnet is defined(https://github.com/ansible-collections/amazon.aws/issues/2321).
- ec2_metadata_facts - add ``ansible_ec2_instance_tags`` to return values (https://github.com/ansible-collections/amazon.aws/pull/2398).
- ec2_transit_gateway - avoid assignment to unused ``retry_decorator`` variable (https://github.com/ansible-collections/amazon.aws/pull/2464).
- ec2_transit_gateway - handle empty description while deleting transit gateway (https://github.com/ansible-collections/community.aws/pull/2086).
- ec2_vpc_egress_igw - avoid assignment to unused ``vpc_id`` variable (https://github.com/ansible-collections/amazon.aws/pull/2464).
- ec2_vpc_nacl - avoid assignment to unused ``result`` variable (https://github.com/ansible-collections/amazon.aws/pull/2464).
- ec2_vpc_vpn - minor linting fixups (https://github.com/ansible-collections/amazon.aws/pull/2444).
- iam_password_policy - avoid assignment to unused variable in except block (https://github.com/ansible-collections/amazon.aws/pull/2464).
- iam_role - avoid assignment to unused variable in except block (https://github.com/ansible-collections/amazon.aws/pull/2464).
- inventory/aws_ec2 - Support jinja2 expression in ``hostnames`` variable(https://github.com/ansible-collections/amazon.aws/issues/2402).
- inventory/aws_ec2 - Update templating mechanism to support ansible-core 2.19 changes (https://github.com/ansible-collections/amazon.aws/pull/2552).
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
- s3_object - support passing metadata in ``create`` mode (https://github.com/ansible-collections/amazon.aws/pull/2529).
- s3_object - use the ``copy`` rather than ``copy_object`` method when performing an S3 to S3 copy (https://github.com/ansible-collections/amazon.aws/issues/2117).
- s3_object_info - add support to list objects under a specific prefix (https://github.com/ansible-collections/amazon.aws/issues/2477).
- s3_object_info - avoid assignment to unused variable in except block (https://github.com/ansible-collections/amazon.aws/pull/2464).

ansible.netcommon
~~~~~~~~~~~~~~~~~

- Exposes new libssh options to configure publickey_accepted_algorithms and hostkeys. This requires ansible-pylibssh v1.1.0 or higher.

ansible.posix
~~~~~~~~~~~~~

- authorized_keys - allow using absolute path to a file as a SSH key(s) source (https://github.com/ansible-collections/ansible.posix/pull/568)
- callback plugins - Add recap information to timer, profile_roles and profile_tasks callback outputs (https://github.com/ansible-collections/ansible.posix/pull/387).

ansible.windows
~~~~~~~~~~~~~~~

- Added support for Windows Server 2025
- setup - Added ``ansible_os_install_date`` as the OS installation date in the ISO 8601 format ``yyyy-MM-ddTHH:mm:ssZ``. This date is represented in the UTC timezone - https://github.com/ansible-collections/ansible.windows/issues/663
- setup - Remove dependency on shared function loaded by Ansible
- win_get_url - Added ``checksum`` and ``checksum_algorithm`` to verify the package before installation. Also returns ``checksum`` if ``checksum_algorithm`` is provided - https://github.com/ansible-collections/ansible.windows/issues/596
- win_get_url - if checksum is passed and destination file exists with different checksum file is always downloaded (https://github.com/ansible-collections/ansible.windows/issues/717)
- win_get_url - if checksum is passed and destination file exists with identical checksum no download is done unless force=yes (https://github.com/ansible-collections/ansible.windows/issues/717)
- win_group - Added ``--diff`` output support.
- win_group - Added ``members`` option to set the group membership. This is designed to replace the functionality of the ``win_group_membership`` module.
- win_group - Added ``sid`` return value representing the security identifier of the group when ``state=present``.
- win_group - Migrate to newer Ansible.Basic fragment for better input validation and testing support.

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

- .ansible-lint is added to handle a formatting issue in Red Hat.
- Added sample playbook for Device Configs Backup Module
- Added support for bulk operations on multiple access points in accesspoint_workflow_manager
- Adding Unit Test automation in github actions
- Aliases were implemented to handle v1 and v2 of the API.
- Bug fixes in [sda_fabric_sites_zones_workflow_manager module
- Bug fixes in accesspoint_workflow_manager module
- Bug fixes in inventory_workflow_manager
- Bug fixes in lan_automation_workflow_manager module
- Bug fixes in network_settings_workflow_manager
- Bug fixes in pnp_workflow_manager module
- Bug fixes in sda_fabric_devices_workflow_manager
- Bug fixes in sda_fabric_transits_workflow_manager
- Bug fixes in sda_fabric_transits_workflow_manager module
- Bug fixes in sda_fabric_virtual_networks_workflow_manager.py
- Bug fixes in site_workflow_manager module
- Bug fixes in swim_workflow_manager module
- Bug fixes in template_workflow_manager module
- Bug fixes in user_role_workflow_manager module
- Changes in circleci and yaml lint files
- Changes in circleci to run test cases in integration branch
- Changes in device_credential_workflow_manager module
- Changes in dnac.py file
- Changes in inventory_workflow_manager module
- Changes in ise_radius_integration_workflow_manager
- Changes in ise_radius_integration_workflow_manager module
- Changes in network_compliance_workflow_manager
- Changes in network_settings_workflow_manager
- Changes in network_settings_workflow_manager module
- Changes in pnp_workflow_manager module
- Changes in provision_workflow_manager module
- Changes in sda_extranet_policy_workflow_manager
- Changes in sda_fabric_devices_workflow_manager module
- Changes in sda_fabric_site_zones_workflow_manager module
- Changes in sda_fabric_virtual_networks_workflow_manager module
- Changes in sda_host_port_onboarding_workflow_manager module
- Changes in site_workflow_manager
- Changes in site_workflow_manager module
- Changes in swim_workflow_manager module
- Changes in swim_workflow_manager module to support list of images
- Changes in template_workflow_manager
- Enhancements in [sda_fabric_virtual_networks_workflow_manager module to support batch operation.
- Enhancements in device_configs_backup_workflow_manager module to support unzipped backup file after download
- Enhancements in device_credential_workflow_manager module
- Enhancements in provision_workflow_manager module
- Enhancements in sda_fabric_devices_workflow_manager.py to support route distribution protocol
- Enhancements in sda_fabric_sites_zones_workflow_manager.py
- Enhancements in sda_host_port_onboarding_workflow_manager module
- Fixed issues in module sda_anycast_gateways_v1
- Fixed issues in module sda_layer3_virtual_networks_v1
- Modifications due to documentation errors
- Removing duplicates in the discovery.py module. snmpRwCommunity property.
- Some parameters were modified in tag_member_v1_info
- Supporting unmarking the devices in rma_workflow_manager module
- The file format was changed to conform to the requested standards.
- Unit test modules added for pnp_workflow_manager module
- Update Readme
- aaa_services_count_v1_info - new module
- aaa_services_id_trend_analytics_v1 - new module
- aaa_services_id_v1_info - new module
- aaa_services_query_count_v1 - new module
- aaa_services_query_v1 - new module
- aaa_services_summary_analytics_v1 - new module
- aaa_services_top_n_analytics_v1 - new module
- aaa_services_trend_analytics_v1 - new module
- aaa_services_v1_info - new module
- accesspoint_workflow_manager - added attribute bulk_update_aps
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
- noqa all is used to ignore rules in some files.
- playbooks were added
- projects_count_v1_info - new module
- projects_project_id_v1 - new module
- projects_project_id_v1_info - new module
- projects_v1 - new module
- projects_v1_info - new module
- qos_policy_setting_v1 - new module
- qos_policy_setting_v1_info - new module
- sda_fabric_devices_workflow_manager - attribute 'delete_fabric_device' was removed
- sda_fabric_devices_workflow_manager - attribute 'route_distribution_protocol' was removed
- sda_fabric_devices_workflow_manager.py - added attribute route_distribution_protocol
- sda_fabric_site_zones_workflow_manager - attributes 'apply_pending_events',  'pre_auth_acl', was added
- sda_fabric_sites_zones_workflow_manager.py - added attribute site_name_hierarchy and removed attribute site_name
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
- site_workflow_manager - attribute 'force_upload_floor_image' was added
- sites_site_id_wireless_settings_ssids_id_update_v1 - new module
- tags_interfaces_members_associations_bulk_v1 - new module
- tags_network_devices_members_associations_bulk_v1 - new module
- template_workflow_manager - attribute 'new_template_name' was added
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

- Add ios_evpn_ethernet resource module.
- Added ios_vrf_interfaces resource module,that helps with configuration of vrfs within interface
- Adds a new module `ios_vrf_address_family` to manage VRFs address families on Cisco IOS devices.
- ios_interfaces - Added service-policy, logging and snmp configuration options for interface.
- ios_l2_interfaces - Added a few switchport and spanning-tree configuration options for interface.
- ios_l3_interfaces - Added a few ip configuration options for interface.

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
- nxos_vpc - Added support for peer-switch feature configuration.

community.aws
~~~~~~~~~~~~~

- aws_ssm -  Refactor ``_init_clients`` Method for Improved Clarity and Efficiency (https://github.com/ansible-collections/community.aws/pull/2223).
- aws_ssm -  Refactor ``_prepare_terminal()`` Method for Improved Clarity and Efficiency (https://github.com/ansible-collections/community.aws/pull/).
- aws_ssm -  Refactor exec_command Method for Improved Clarity and Efficiency (https://github.com/ansible-collections/community.aws/pull/2224).
- aws_ssm - Add the possibility to define ``aws_ssm plugin`` variable via environment variable and by default use the version found on the $PATH rather than require that you provide an absolute path (https://github.com/ansible-collections/community.aws/issues/1990).
- aws_ssm - Refactor ``_exec_transport_commands``, ``_generate_commands``, and ``_exec_transport_commands`` methods for improved clarity (https://github.com/ansible-collections/community.aws/pull/2248).
- aws_ssm - Refactor connection/aws_ssm to add new S3ClientManager class and move relevant methods to the new class (https://github.com/ansible-collections/community.aws/pull/2255).
- aws_ssm - Refactor display/verbosity-related methods in aws_ssm to simplify the code and avoid repetition (https://github.com/ansible-collections/community.aws/pull/2264).
- aws_ssm - add function to generate random strings for SSM CLI delimitation (https://github.com/ansible-collections/community.aws/pull/2235).
- dms_endpoint - improve resilience of parameter comparison (https://github.com/ansible-collections/community.aws/pull/2221).
- s3_lifecycle - Support for min and max object size when applying the filter rules (https://github.com/ansible-collections/community.aws/pull/2205).
- various modules - linting fixups (https://github.com/ansible-collections/community.aws/pull/2221).
- waf_condition - adds missing options validation to filters (https://github.com/ansible-collections/community.aws/pull/2220).

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
- luks_device - allow passphrases to contain newlines (https://github.com/ansible-collections/community.crypto/pull/844).
- luks_device - allow to provide passphrases base64-encoded (https://github.com/ansible-collections/community.crypto/issues/827, https://github.com/ansible-collections/community.crypto/pull/829).
- openssl_pkcs12 - the module now supports ``certificate_content``/``other_certificates_content`` for cases where the data already exists in memory and not yet in a file (https://github.com/ansible-collections/community.crypto/issues/847, https://github.com/ansible-collections/community.crypto/pull/848).
- x509_certificate_convert - add new option ``verify_cert_parsable`` which allows to check whether the certificate can actually be parsed (https://github.com/ansible-collections/community.crypto/issues/809, https://github.com/ansible-collections/community.crypto/pull/830).

community.dns
~~~~~~~~~~~~~

- all controller code - modernize Python code (https://github.com/ansible-collections/community.dns/pull/231).
- all filter, inventory, and lookup plugins, and plugin utils - add type hints to all Python 3 only code (https://github.com/ansible-collections/community.dns/pull/239).
- get_public_suffix, get_registrable_domain, remove_public_suffix, and remove_registrable_domain filter plugin - validate parameters, and correctly handle byte strings when passed for input (https://github.com/ansible-collections/community.dns/pull/239).

community.docker
~~~~~~~~~~~~~~~~

- docker_compose_v2 - add ``assume_yes`` parameter for ``docker compose up`` (https://github.com/ansible-collections/community.docker/pull/1045).
- docker_compose_v2 - add ``ignore_build_events`` option (default value ``true``) which allows to (not) ignore build events for change detection (https://github.com/ansible-collections/community.docker/issues/1005, https://github.com/ansible-collections/community.docker/issues/pull/1011).
- docker_compose_v2* modules - determine compose version with ``docker compose version`` and only then fall back to ``docker info`` (https://github.com/ansible-collections/community.docker/pull/1021).
- docker_image_build - ``outputs[].name`` can now be a list of strings (https://github.com/ansible-collections/community.docker/pull/1006).
- docker_image_build - the executed command is now returned in the ``command`` return value in case of success and some errors (https://github.com/ansible-collections/community.docker/pull/1006).
- docker_network - add ``enable_ipv4`` option (https://github.com/ansible-collections/community.docker/issues/1047, https://github.com/ansible-collections/community.docker/pull/1049).
- docker_network - added ``ingress`` option (https://github.com/ansible-collections/community.docker/pull/999).
- docker_stack - allow to add ``--detach=false`` option to ``docker stack deploy`` command (https://github.com/ansible-collections/community.docker/pull/987).

community.general
~~~~~~~~~~~~~~~~~

- CmdRunner module utils - the convenience method ``cmd_runner_fmt.as_fixed()`` now accepts multiple arguments as a list (https://github.com/ansible-collections/community.general/pull/9893).
- MH module utils - delegate ``debug`` to the underlying ``AnsibleModule`` instance or issues a warning if an attribute already exists with that name (https://github.com/ansible-collections/community.general/pull/9577).
- alternatives - add ``family`` parameter that allows to utilize the ``--family`` option available in RedHat version of update-alternatives (https://github.com/ansible-collections/community.general/issues/5060, https://github.com/ansible-collections/community.general/pull/9096).
- apache2_mod_proxy - better handling regexp extraction (https://github.com/ansible-collections/community.general/pull/9609).
- apache2_mod_proxy - change type of ``state`` to a list of strings. No change for the users (https://github.com/ansible-collections/community.general/pull/9600).
- apache2_mod_proxy - code simplification, no change in functionality (https://github.com/ansible-collections/community.general/pull/9457).
- apache2_mod_proxy - improve readability when using results from ``fecth_url()`` (https://github.com/ansible-collections/community.general/pull/9608).
- apache2_mod_proxy - refactor repeated code into method (https://github.com/ansible-collections/community.general/pull/9599).
- apache2_mod_proxy - remove unused parameter and code from ``Balancer`` constructor (https://github.com/ansible-collections/community.general/pull/9614).
- apache2_mod_proxy - simplified and improved string manipulation (https://github.com/ansible-collections/community.general/pull/9614).
- apache2_mod_proxy - use ``deps`` to handle dependencies (https://github.com/ansible-collections/community.general/pull/9612).
- bitwarden lookup plugin - add new option ``collection_name`` to filter results by collection name, and new option ``result_count`` to validate number of results (https://github.com/ansible-collections/community.general/pull/9728).
- bitwarden lookup plugin - use f-strings instead of interpolations or ``format`` (https://github.com/ansible-collections/community.general/pull/9324).
- cgroup_memory_recap callback plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9583).
- cgroup_memory_recap callback plugin - use f-strings instead of interpolations or ``format`` (https://github.com/ansible-collections/community.general/pull/9321).
- chef_databag lookup plugin - use f-strings instead of interpolations or ``format`` (https://github.com/ansible-collections/community.general/pull/9324).
- chroot connection plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9584).
- chroot connection plugin - clean up string conversions (https://github.com/ansible-collections/community.general/pull/9379).
- chroot connection plugin - use f-strings instead of interpolations or ``format`` (https://github.com/ansible-collections/community.general/pull/9322).
- cloud_init_data_facts - open file using ``open()`` as a context manager (https://github.com/ansible-collections/community.general/pull/9579).
- cloudflare_dns - add support for ``comment`` and ``tags`` (https://github.com/ansible-collections/community.general/pull/9132).
- cobbler inventory plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9584).
- cobbler inventory plugin - clean up string conversions (https://github.com/ansible-collections/community.general/pull/9379).
- cobbler inventory plugin - use f-strings instead of interpolations or ``format`` (https://github.com/ansible-collections/community.general/pull/9323).
- collection_version lookup plugin - use f-strings instead of interpolations or ``format`` (https://github.com/ansible-collections/community.general/pull/9324).
- consul_kv lookup plugin - use f-strings instead of interpolations or ``format`` (https://github.com/ansible-collections/community.general/pull/9324).
- consul_token - fix idempotency when ``policies`` or ``roles`` are supplied by name (https://github.com/ansible-collections/community.general/issues/9841, https://github.com/ansible-collections/community.general/pull/9845).
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
- deps module utils - add ``deps.clear()`` to clear out previously declared dependencies (https://github.com/ansible-collections/community.general/pull/9179).
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
- homebrew - greatly speed up module when multiple packages are passed in the ``name`` option (https://github.com/ansible-collections/community.general/pull/9181).
- homebrew - remove duplicated package name validation (https://github.com/ansible-collections/community.general/pull/9076).
- icinga2 inventory plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9584).
- icinga2 inventory plugin - use f-strings instead of interpolations or ``format`` (https://github.com/ansible-collections/community.general/pull/9323).
- incus connection plugin - adds ``remote_user`` and ``incus_become_method`` parameters for allowing a non-root user to connect to an Incus instance (https://github.com/ansible-collections/community.general/pull/9743).
- incus connection plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9584).
- incus connection plugin - use f-strings instead of interpolations or ``format`` (https://github.com/ansible-collections/community.general/pull/9322).
- iocage connection plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9584).
- iocage connection plugin - use f-strings instead of interpolations or ``format`` (https://github.com/ansible-collections/community.general/pull/9322).
- iocage inventory plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9584).
- iocage inventory plugin - clean up string conversions (https://github.com/ansible-collections/community.general/pull/9379).
- iocage inventory plugin - the new parameter ``hooks_results`` of the plugin is a list of files inside a jail that provide configuration parameters for the inventory. The inventory plugin reads the files from the jails and put the contents into the items of created variable ``iocage_hooks`` (https://github.com/ansible-collections/community.general/issues/9650, https://github.com/ansible-collections/community.general/pull/9651).
- iocage inventory plugin - the new parameter ``sudo`` of the plugin lets the command ``iocage list -l`` to run as root on the iocage host. This is needed to get the IPv4 of a running DHCP jail (https://github.com/ansible-collections/community.general/issues/9572, https://github.com/ansible-collections/community.general/pull/9573).
- iptables_state action plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9583).
- iptables_state action plugin - use f-strings instead of interpolations or ``format`` (https://github.com/ansible-collections/community.general/pull/9318).
- iso_extract - adds ``password`` parameter that is passed to 7z (https://github.com/ansible-collections/community.general/pull/9159).
- jabber callback plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9583).
- jabber callback plugin - use f-strings instead of interpolations or ``format`` (https://github.com/ansible-collections/community.general/pull/9321).
- jail connection plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9584).
- jail connection plugin - use f-strings instead of interpolations or ``format`` (https://github.com/ansible-collections/community.general/pull/9322).
- jc filter plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9585).
- jira - adds ``client_cert`` and ``client_key`` parameters for supporting client certificate authentification when connecting to Jira (https://github.com/ansible-collections/community.general/pull/9753).
- jira - transition operation now has ``status_id`` to directly reference wanted transition (https://github.com/ansible-collections/community.general/pull/9602).
- json_query filter plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9585).
- keep_keys filter plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9585).
- keycloak - add an action group for Keycloak modules to allow ``module_defaults`` to be set for Keycloak tasks (https://github.com/ansible-collections/community.general/pull/9284).
- keycloak_* modules - ``refresh_token`` parameter added. When multiple authentication parameters are provided (``token``, ``refresh_token``, and ``auth_username``/``auth_password``), modules will now automatically retry requests upon authentication errors (401), using in order the token, refresh token, and username/password (https://github.com/ansible-collections/community.general/pull/9494).
- keycloak_realm - remove ID requirement when creating a realm to allow Keycloak generating its own realm ID (https://github.com/ansible-collections/community.general/pull/9768).
- keyring lookup plugin - use f-strings instead of interpolations or ``format`` (https://github.com/ansible-collections/community.general/pull/9324).
- known_hosts - open file using ``open()`` as a context manager (https://github.com/ansible-collections/community.general/pull/9579).
- ksu become plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9583).
- ksu become plugin - use f-strings instead of interpolations or ``format`` (https://github.com/ansible-collections/community.general/pull/9319).
- lastpass lookup plugin - use f-strings instead of interpolations or ``format`` (https://github.com/ansible-collections/community.general/pull/9324).
- launchd - add ``plist`` option for services such as sshd, where the plist filename doesn't match the service name (https://github.com/ansible-collections/community.general/pull/9102).
- linode inventory plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9584).
- linode inventory plugin - use f-strings instead of interpolations or ``format`` (https://github.com/ansible-collections/community.general/pull/9323).
- lists filter plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9585).
- lists_mergeby filter plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9585).
- lldp - adds ``multivalues`` parameter to control behavior when lldpctl outputs an attribute multiple times (https://github.com/ansible-collections/community.general/pull/9657).
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
- lvg - add ``remove_extra_pvs`` parameter to control if ansible should remove physical volumes which are not in the ``pvs`` parameter (https://github.com/ansible-collections/community.general/pull/9698).
- lxc connection plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9584).
- lxc connection plugin - use f-strings instead of interpolations or ``format`` (https://github.com/ansible-collections/community.general/pull/9322).
- lxd connection plugin - adds ``remote_user`` and ``lxd_become_method`` parameters for allowing a non-root user to connect to an LXD instance (https://github.com/ansible-collections/community.general/pull/9659).
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
- nmap inventory plugin - adds ``dns_servers`` option for specifying DNS servers for name resolution. Accepts hostnames or IP addresses in the same format as the ``exclude`` option (https://github.com/ansible-collections/community.general/pull/9849).
- nmap inventory plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9584).
- nmap inventory plugin - clean up string conversions (https://github.com/ansible-collections/community.general/pull/9379).
- nmap inventory plugin - use f-strings instead of interpolations or ``format`` (https://github.com/ansible-collections/community.general/pull/9323).
- nmcli - add ``sriov`` parameter that enables support for SR-IOV settings (https://github.com/ansible-collections/community.general/pull/9168).
- nmcli - add a option ``fail_over_mac`` (https://github.com/ansible-collections/community.general/issues/9570, https://github.com/ansible-collections/community.general/pull/9571).
- nmcli - adds VRF support with new ``type`` value ``vrf`` and new ``slave_type`` value ``vrf`` as well as new ``table`` parameter (https://github.com/ansible-collections/community.general/pull/9658, https://github.com/ansible-collections/community.general/issues/8014).
- nrdp callback plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9583).
- nrdp callback plugin - use f-strings instead of interpolations or ``format`` (https://github.com/ansible-collections/community.general/pull/9321).
- null callback plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9583).
- one_template - adds ``filter`` option for retrieving templates which are not owned by the user (https://github.com/ansible-collections/community.general/pull/9547, https://github.com/ansible-collections/community.general/issues/9278).
- onepassword lookup plugin - clean up string conversions (https://github.com/ansible-collections/community.general/pull/9379).
- onepassword lookup plugin - use f-strings instead of interpolations or ``format`` (https://github.com/ansible-collections/community.general/pull/9324).
- onepassword_doc lookup plugin - use f-strings instead of interpolations or ``format`` (https://github.com/ansible-collections/community.general/pull/9324).
- onepassword_ssh_key - refactor to move code to lookup class (https://github.com/ansible-collections/community.general/pull/9633).
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
- pipx - add return value ``version`` (https://github.com/ansible-collections/community.general/pull/9180).
- pipx_info - add return value ``version`` (https://github.com/ansible-collections/community.general/pull/9180).
- pmrun become plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9583).
- pmrun become plugin - use f-strings instead of interpolations or ``format`` (https://github.com/ansible-collections/community.general/pull/9319).
- proxmox - refactors the proxmox module (https://github.com/ansible-collections/community.general/pull/9225).
- proxmox inventory plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9584).
- proxmox inventory plugin - clean up string conversions (https://github.com/ansible-collections/community.general/pull/9379).
- proxmox inventory plugin - strip whitespace from ``user``, ``token_id``, and ``token_secret`` (https://github.com/ansible-collections/community.general/issues/9227, https://github.com/ansible-collections/community.general/pull/9228/).
- proxmox inventory plugin - use f-strings instead of interpolations or ``format`` (https://github.com/ansible-collections/community.general/pull/9323).
- proxmox module utils - add method ``api_task_complete`` that can wait for task completion and return error message (https://github.com/ansible-collections/community.general/pull/9256).
- proxmox_backup - refactor permission checking to improve code readability and maintainability (https://github.com/ansible-collections/community.general/pull/9239).
- proxmox_kvm - add missing audio hardware device handling (https://github.com/ansible-collections/community.general/issues/5192, https://github.com/ansible-collections/community.general/pull/9847).
- proxmox_kvm - allow hibernation and suspending of VMs (https://github.com/ansible-collections/community.general/issues/9620, https://github.com/ansible-collections/community.general/pull/9653).
- proxmox_pct_remote connection plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9584).
- proxmox_template - add server side artifact fetching support (https://github.com/ansible-collections/community.general/pull/9113).
- proxmox_template - add support for checksum validation with new options ``checksum_algorithm`` and ``checksum`` (https://github.com/ansible-collections/community.general/issues/9553, https://github.com/ansible-collections/community.general/pull/9601).
- pulp_repo - open file using ``open()`` as a context manager (https://github.com/ansible-collections/community.general/pull/9579).
- qubes connection plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9584).
- qubes connection plugin - use f-strings instead of interpolations or ``format`` (https://github.com/ansible-collections/community.general/pull/9322).
- random_mac filter plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9585).
- random_pet lookup plugin - use f-strings instead of interpolations or ``format`` (https://github.com/ansible-collections/community.general/pull/9324).
- redfish_command - add ``PowerFullPowerCycle`` to power command options (https://github.com/ansible-collections/community.general/pull/9729).
- redfish_command - add ``update_custom_oem_header``, ``update_custom_oem_params``, and ``update_custom_oem_mime_type`` options (https://github.com/ansible-collections/community.general/pull/9123).
- redfish_config - add command ``SetPowerRestorePolicy`` to set the desired power state of the system when power is restored (https://github.com/ansible-collections/community.general/pull/9837).
- redfish_info - add command ``GetAccountServiceConfig`` to get full information about AccountService configuration (https://github.com/ansible-collections/community.general/pull/9403).
- redfish_info - add command ``GetPowerRestorePolicy`` to get the desired power state of the system when power is restored (https://github.com/ansible-collections/community.general/pull/9824).
- redfish_utils module utils - remove redundant code (https://github.com/ansible-collections/community.general/pull/9190).
- redhat_subscription - open file using ``open()`` as a context manager (https://github.com/ansible-collections/community.general/pull/9579).
- redis cache plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9583).
- redis cache plugin - clean up string conversions (https://github.com/ansible-collections/community.general/pull/9379).
- redis cache plugin - use f-strings instead of interpolations or ``format`` (https://github.com/ansible-collections/community.general/pull/9320).
- redis lookup plugin - use f-strings instead of interpolations or ``format`` (https://github.com/ansible-collections/community.general/pull/9324).
- remove_keys filter plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9585).
- replace_keys filter plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9585).
- revbitspss lookup plugin - use f-strings instead of interpolations or ``format`` (https://github.com/ansible-collections/community.general/pull/9324).
- reveal_ansible_type filter plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9585).
- rocketchat - option ``is_pre740`` has been added to control the format of the payload. For Rocket.Chat 7.4.0 or newer, it must be set to ``false`` (https://github.com/ansible-collections/community.general/pull/9882).
- rpm_ostree_pkg - added the options ``apply_live`` (https://github.com/ansible-collections/community.general/pull/9167).
- rpm_ostree_pkg - added the return value ``needs_reboot`` (https://github.com/ansible-collections/community.general/pull/9167).
- run0 become plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9583).
- saltstack connection plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9584).
- saltstack connection plugin - use f-strings instead of interpolations or ``format`` (https://github.com/ansible-collections/community.general/pull/9322).
- say callback plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9583).
- say callback plugin - use f-strings instead of interpolations or ``format`` (https://github.com/ansible-collections/community.general/pull/9321).
- scaleway inventory plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9584).
- scaleway inventory plugin - clean up string conversions (https://github.com/ansible-collections/community.general/pull/9379).
- scaleway inventory plugin - use f-strings instead of interpolations or ``format`` (https://github.com/ansible-collections/community.general/pull/9323).
- scaleway_lb - minor simplification in the code (https://github.com/ansible-collections/community.general/pull/9189).
- selective callback plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9583).
- selective callback plugin - use f-strings instead of interpolations or ``format`` (https://github.com/ansible-collections/community.general/pull/9321).
- sesu become plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9583).
- sesu become plugin - use f-strings instead of interpolations or ``format`` (https://github.com/ansible-collections/community.general/pull/9319).
- shelvefile lookup plugin - use f-strings instead of interpolations or ``format`` (https://github.com/ansible-collections/community.general/pull/9324).
- shutdown action plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9583).
- shutdown action plugin - clean up string conversions (https://github.com/ansible-collections/community.general/pull/9379).
- shutdown action plugin - use f-strings instead of interpolations or ``format`` (https://github.com/ansible-collections/community.general/pull/9318).
- slack callback plugin - add ``http_agent`` option to enable the user to set a custom user agent for slack callback plugin (https://github.com/ansible-collections/community.general/issues/9813, https://github.com/ansible-collections/community.general/pull/9836).
- slack callback plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9583).
- slack callback plugin - clean up string conversions (https://github.com/ansible-collections/community.general/pull/9379).
- slack callback plugin - use f-strings instead of interpolations or ``format`` (https://github.com/ansible-collections/community.general/pull/9321).
- snap - add return value ``version`` (https://github.com/ansible-collections/community.general/pull/9598).
- snap_alias - add return value ``version`` (https://github.com/ansible-collections/community.general/pull/9598).
- solaris_zone - open file using ``open()`` as a context manager (https://github.com/ansible-collections/community.general/pull/9579).
- sorcery - open file using ``open()`` as a context manager (https://github.com/ansible-collections/community.general/pull/9579).
- splunk callback plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9583).
- splunk callback plugin - use f-strings instead of interpolations or ``format`` (https://github.com/ansible-collections/community.general/pull/9321).
- ssh_config - add ``dynamicforward`` option (https://github.com/ansible-collections/community.general/pull/9192).
- ssh_config - add ``other_options`` option (https://github.com/ansible-collections/community.general/issues/8053, https://github.com/ansible-collections/community.general/pull/9684).
- stackpath_compute inventory plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9584).
- stackpath_compute inventory plugin - use f-strings instead of interpolations or ``format`` (https://github.com/ansible-collections/community.general/pull/9323).
- sudosu become plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9583).
- sudosu become plugin - use f-strings instead of interpolations or ``format`` (https://github.com/ansible-collections/community.general/pull/9319).
- sumologic callback plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9583).
- syslog_json callback plugin - adjust standard preamble for Python 3 (https://github.com/ansible-collections/community.general/pull/9583).
- systemd_info - add wildcard expression support in ``unitname`` option (https://github.com/ansible-collections/community.general/pull/9821).
- systemd_info - extend support to timer units (https://github.com/ansible-collections/community.general/pull/9891).
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
- vmadm - add new options ``flexible_disk_size`` and ``owner_uuid`` (https://github.com/ansible-collections/community.general/pull/9892).
- xbps - add ``root`` and ``repository`` options to enable bootstrapping new void installations (https://github.com/ansible-collections/community.general/pull/9174).
- xen_orchestra inventory plugin - add ``use_vm_uuid`` and ``use_host_uuid`` boolean options to allow switching over to using VM/Xen name labels instead of UUIDs as item names (https://github.com/ansible-collections/community.general/pull/9787).
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

community.library_inventory_filtering_v1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Add typing information for the ``inventory_filter`` plugin utils (https://github.com/ansible-collections/community.library_inventory_filtering/pull/22).

community.mysql
~~~~~~~~~~~~~~~

- Integration tests for MariaDB 11.4 have replaced those for 10.5. The previous version is now 10.11.
- mysql_db - added ``zstd`` (de)compression support for ``import``/``dump`` states (https://github.com/ansible-collections/community.mysql/issues/696).
- mysql_info - adds the count of tables for each database to the returned values. It is possible to exclude this new field using the ``db_table_count`` exclusion filter. (https://github.com/ansible-collections/community.mysql/pull/691)
- mysql_query - returns the ``execution_time_ms`` list containing execution time per query in milliseconds.
- mysql_user - add ``locked`` option to lock/unlock users, this is mainly used to have users that will act as definers on stored procedures.

community.okd
~~~~~~~~~~~~~

- openshift_auth - fix issue where openshift_auth module sometimes does not delete the auth token. Based on stale PR (https://github.com/openshift/community.okd/pull/194).

community.postgresql
~~~~~~~~~~~~~~~~~~~~

- postgresql_pg_hba - adds 'pg_hba_string' which contains the string that is written to the file to the output of the module (https://github.com/ansible-collections/community.postgresql/pull/778)
- postgresql_pg_hba - adds a parameter 'sort_rules' that allows the user to disable sorting in the module, the default is the previous behavior (https://github.com/ansible-collections/community.postgresql/pull/778)
- postgresql_pg_hba - changes ordering of entries that are identical except for the ip-range, but only if the ranges are of the same size, this isn't breaking as ranges of equal size can't overlap (https://github.com/ansible-collections/community.postgresql/pull/772)
- postgresql_pg_hba - orders auth-options alphabetically, this isn't breaking as the order of those options is not relevant to postgresql (https://github.com/ansible-collections/community.postgresql/pull/772)
- postgresql_pg_hba - regarding #795 will read all kinds of includes and add them to the end of the file in the same order as they were in the original file, does not allow to add includes (https://github.com/ansible-collections/community.postgresql/pull/778)
- postgresql_pg_hba - show the number of the line with the issue if parsing a file fails (https://github.com/ansible-collections/community.postgresql/pull/766)
- postgresql_publication - add possibility of creating publication with column list (https://github.com/ansible-collections/community.postgresql/pull/763).
- postgresql_publication - added ``rowfilters`` parameter that adds support for row filtering on PG publications (https://github.com/ansible-collections/community.postgresql/pull/813)
- postgresql_query - returns the `execution_time_ms` list containing execution time per query in milliseconds (https://github.com/ansible-collections/community.postgresql/issues/787).
- postgresql_user - now there is a ``quote_configuration_values`` parameter that allows to turn off quoting for values which when set to ``false`` allows to set ``search_path`` (https://github.com/ansible-collections/community.postgresql/pull/806)

community.rabbitmq
~~~~~~~~~~~~~~~~~~

- rabbitmq_policy - adjust the `apply_to` parameter to also accept the new options `classic_queues`, `quorum_queues` and `streams` which are supported since rabbitmq 3.12

community.routeros
~~~~~~~~~~~~~~~~~~

- api_info, api_modify - add missing attribute ``require-message-auth`` for the ``radius`` path which exists since RouterOS version 7.15 (https://github.com/ansible-collections/community.routeros/issues/338, https://github.com/ansible-collections/community.routeros/pull/339).
- api_info, api_modify - add missing fields ``comment``, ``next-pool`` to ``ip pool`` path (https://github.com/ansible-collections/community.routeros/pull/327).
- api_info, api_modify - add support for the ``ip dns forwarders`` path implemented by RouterOS 7.17 and newer (https://github.com/ansible-collections/community.routeros/pull/343).
- api_info, api_modify - add support for the ``routing filter community-list`` path implemented by RouterOS 7 and newer (https://github.com/ansible-collections/community.routeros/pull/331).
- api_info, api_modify - add the ``interface 6to4`` path. Used to manage IPv6 tunnels via tunnel-brokers like HE, where native IPv6 is not provided (https://github.com/ansible-collections/community.routeros/pull/342).
- api_info, api_modify - add the ``interface wireless access-list`` and ``interface wireless connect-list`` paths (https://github.com/ansible-collections/community.routeros/issues/284, https://github.com/ansible-collections/community.routeros/pull/340).
- api_info, api_modify - add the ``use-interface-duid`` option for ``ipv6 dhcp-client`` path. This option prevents issues with Fritzbox modems and routers, when using virtual interfaces (like VLANs) may create duplicated records in hosts config, this breaks original "expose-host" function. Also add the ``script``, ``custom-duid`` and ``validate-server-duid`` as backport from 7.15 version update (https://github.com/ansible-collections/community.routeros/pull/341).
- api_info, api_modify - change default for ``/ip/cloud/ddns-enabled`` for RouterOS 7.17 and newer from ``yes`` to ``auto`` (https://github.com/ansible-collections/community.routeros/pull/350).

community.vmware
~~~~~~~~~~~~~~~~

- vcenter_standard_key_provider - Drop unused HAS_PYVMOMI (https://github.com/ansible-collections/community.vmware/pull/2327).
- vmware.py - Add logic for handling the case where the `datacenter` property is not provided.
- vmware_category - Don't test for vSphere < 7 anymore (https://github.com/ansible-collections/community.vmware/pull/2326).
- vmware_guest - Add new cutomization spec param `domainOU`. (https://github.com/ansible-collections/community.vmware/issues/2275)
- vmware_guest - Drop unused HAS_PYVMOMI (https://github.com/ansible-collections/community.vmware/pull/2327).
- vmware_guest - Print details about the error message when the returned task result contains (https://github.com/ansible-collections/community.vmware/pull/2301).
- vmware_guest - Speedup network search (https://github.com/ansible-collections/community.vmware/pull/2278).
- vmware_guest_info - `datacenter` property is now optional as it only required in cases where the VM is not uniquely identified by `name`.
- vmware_guest_network - Speedup network search (https://github.com/ansible-collections/community.vmware/pull/2277).
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

dellemc.enterprise_sonic
~~~~~~~~~~~~~~~~~~~~~~~~

- sonic_image_management - Add support for image GPG Key installation and verification feature in sonic_image_management module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/380).
- sonic_interfaces - Add new unreliable-los option to interface resource module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/453).
- sonic_ldap - Add ldap security profile support for sonic_ldap module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/414).
- sonic_logging - Add "severity" option to the logging module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/478).
- sonic_logging - Add TLS protocol in sonic_logging module(https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/423).
- sonic_logging - Add audit message-type in sonic_logging module(https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/424).
- sonic_logging - Add new 'auditd_system' choice to the 'message_type' choices for the logging resource module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/459).
- sonic_mgmt_servers - Add REST server cipher suite support for sonic_mgmt_servers module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/464).
- sonic_qos_buffer - Add 'buffer_init' attribute (https://github.com/ansible-collection/dellemc.enterprise_sonic/pull/444).
- sonic_route_maps - Add the set ip/ipv6 next_hop 'native' option (https://github.com/ansible-collection/dellemc.enterprise_sonic/pull/421).
- sonic_vxlan - Add 'suppress_vlan_neigh' vlan list option (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/448).

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

fortinet.fortimanager
~~~~~~~~~~~~~~~~~~~~~

- Supported FortiManager 6.2.13, 6.4.15, 7.0.13, 7.2.8, 7.4.5, 7.6.1. Added 1 new module.
- Supported FortiManager 7.2.9, 7.4.6, 7.6.2. Added 3 new modules.
- Supported check diff for some modules except "fmgr_generic". You can use "ansible-playbook -i <your-host-file> <your-playbook> --check --diff" to check what changes your playbook will make to the FortiManager.

hetzner.hcloud
~~~~~~~~~~~~~~

- server - Add `created` state that creates a server but do not start it.

ibm.storage_virtualize
~~~~~~~~~~~~~~~~~~~~~~

- ibm_sv_manage_replication_policy - Added support for disaster recovery
- ibm_sv_manage_replication_policy - Added support for highly-available snapshots
- ibm_sv_manage_snapshot- Add support for restoring highly-available volumes and volumegroups from local snapshots
- ibm_sv_manage_storage_partition - Added support for partition migration and disaster recovery
- ibm_sv_manage_truststore_for_replication - Added support for creating truststore for flashsystem grid
- ibm_sv_manage_truststore_for_replication - Added support for enabling various options (syslog, RESTAPI, vasa, ipsec, snmp and email) for existing truststore
- ibm_svc_host - Added support for specifying host location in PBHA, support for FDMI discovery, suppressing offline alert, updating IO groups, and for specifying fcscsi and iscsi protocols during host creation
- ibm_svc_info - Added support for flashsystem grid
- ibm_svc_initial_setup - Added support for flashcopy default grain size and SI (Storage Insights) to be able to control partition migration
- ibm_svc_initial_setup - Added support for vdisk protection settings, iscsiauthmethod and improved REST API calls
- ibm_svc_manage_flashcopy - Added support for enabling cleanrate during flashcopy creation and update
- ibm_svc_manage_portset - Added support for linking portset of 2 clusters for PBHA
- ibm_svc_manage_replication - Added support for highly-available snapshots
- ibm_svc_manage_volume - Added support for converting thinclone volume(s) to clone
- ibm_svc_manage_volume - Added support for unmapping hosts, remote-copy and flashcopy during volume deletion
- ibm_svc_manage_volumegroup - Added support for disaster recovery and converting thinclone volumegroup to clone
- ibm_svc_mdisk - Added support for updating tier
- ibm_svc_mdiskgrp - Improved probe function for storage pools

kubernetes.core
~~~~~~~~~~~~~~~

- Bump version of ansible-lint to minimum 24.7.0 (https://github.com/ansible-collections/kubernetes.core/pull/765).
- Parameter insecure_registry added to helm_template as equivalent of insecure-skip-tls-verify (https://github.com/ansible-collections/kubernetes.core/pull/805).
- k8s - Extend hidden_fields to allow the expression of more complex field types to be hidden (https://github.com/ansible-collections/kubernetes.core/pull/872)
- k8s_drain - Improve error message for pod disruption budget when draining a node (https://github.com/ansible-collections/kubernetes.core/issues/797).
- k8s_info - Extend hidden_fields to allow the expression of more complex field types to be hidden (https://github.com/ansible-collections/kubernetes.core/pull/872)
- waiter.py - add ClusterOperator support. The module can now check OpenShift cluster health by verifying ClusterOperator status requiring 'Available: True', 'Degraded: False', and 'Progressing: False' for success. (https://github.com/ansible-collections/kubernetes.core/issues/869)

lowlydba.sqlserver
~~~~~~~~~~~~~~~~~~

- Add new `login_role` module to add/remove server roles for logins (https://github.com/lowlydba/lowlydba.sqlserver/pull/293).
- Add new user_role module to manage users' membership to database roles (https://github.com/lowlydba/lowlydba.sqlserver/pull/292).
- Added support for contained Availability Groups using dbatools 2.1.15 (https://github.com/lowlydba/lowlydba.sqlserver/pull/249).

microsoft.ad
~~~~~~~~~~~~

- Added support for Windows Server 2025
- domain - Added ``replication_source_dc`` to specify the domain controller to use as the replication source for the new domain - https://github.com/ansible-collections/microsoft.ad/issues/159
- domain_controller - Added ``replication_source_dc`` to specify the domain controller to use as the replication source for the new domain controller - https://github.com/ansible-collections/microsoft.ad/issues/159
- microsoft.ad.user - Added ``groups.permissions_failure_action`` to control the behaviour when failing to modify the user's groups - (https://github.com/ansible-collections/microsoft.ad/issues/140).

netapp.ontap
~~~~~~~~~~~~

- Multiple modules - Standardize hostname, username, and password parameters to use netapp_hostname, netapp_username, and netapp_password as values.
- Multiple modules - Update examples to use Fully Qualified Collection Name.
- Update dead link in doc_fragments.
- all modules supporting only REST - change in documentation for `use_rest`.
- all modules supporting only REST - updated `extends_documentation_fragment` & argument spec.
- na_ontap_active_directory - return error message when attempting to modify `account_name`.
- na_ontap_bgp_config - REST only support for managing BGP configuration for a node, requires ONTAP 9.6 or later.
- na_ontap_cifs_privileges - REST only support for managing privileges of the local or Active Directory user or group, requires ONTAP 9.10.1 or later.
- na_ontap_cifs_server - added new option `comment` for cifs server, requires ONTAP 9.6 or later.
- na_ontap_dns - updated documentation for `vserver`.
- na_ontap_flexcache - new option to enable `writeback` added in REST, requires ONTAP 9.12 or later.
- na_ontap_flexcache - new options `relative_size`, `override_encryption`, `atime_scrub`, `cifs_change_notify_enabled`, `global_file_locking_enabled`, `guarantee_type`, `dr_cache` added in REST.
- na_ontap_rest_cli - Add POST and DELETE examples.
- na_ontap_rest_info - removed example which has option `gather_subset` set to `all` from documentation.
- na_ontap_rest_info - updated `extends_documentation_fragment` & argument spec.
- na_ontap_s3_buckets - added new option `versioning_state`, requires ONTAP 9.11.1 or later.
- na_ontap_s3_buckets - updated `extends_documentation_fragment` & argument spec.
- na_ontap_s3_services - added `is_http_enabled`, `is_https_enabled`, `port` and `secure_port` option for `s3` service, requires ONTAP 9.8 or later.
- na_ontap_s3_users - new option `regenerate_keys` and `delete_keys` added in REST, `delete_keys` requires ONTAP 9.14 or later.
- na_ontap_snapmirror - new option `quiesced_time_out` added to wait for quiesce job to complete.
- na_ontap_svm - added `allowed` option for `s3` service, requires ONTAP 9.7 or later.
- na_ontap_svm - updated documentation for `allowed_protocols` & `services`.
- na_ontap_volume - new option `granular_data` added in REST, requires ONTAP 9.12 or later.
- na_ontap_volume - new option `large_size_enabled` added in REST, requires ONTAP 9.12 or later.
- na_ontap_volume - new option `nas_application_template.cifs_share_name` added in REST, requires ONTAP 9.11 or later.
- na_ontap_volume - new option `nas_application_template.snaplock.*` added in REST, requires ONTAP 9.12 or later.
- na_ontap_volume - new option `nas_application_template.snapshot_locking_enabled` added in REST, requires ONTAP 9.13.1 or later.

netapp.storagegrid
~~~~~~~~~~~~~~~~~~

- na_sg_grid_account - new option `allow_compliance_mode` and `max_retention_days` added for tenant account, requires storageGRID 11.9 or later.
- na_sg_grid_gateway - new option `enable_tenant_manager`, `enable_grid_manager` and `node_type` added to support management interfaces.
- na_sg_grid_group - new option `read_only` added for grid groups.
- na_sg_grid_info - LB endpoints and HA group in info module.
- na_sg_org_group - new option `read_only` added for tenant groups.

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

purestorage.flasharray
~~~~~~~~~~~~~~~~~~~~~~

- all - Minimum ``py-pure-client`` version increased to 1.57.0 due to release of Realms feature
- purefa_dsrole - Add support for non-system-defined directory service roles with new parameter `name`
- purefa_hg - Added support for Fusion
- purefa_host - Added Fusion support
- purefa_info - Add ``enabled`` value for network subnets
- purefa_info - Add ``policies` list of dicts to ``filesystem`` subset for each share.
- purefa_info - Add ``time_remaining`` field for non-deleted directory snapshots
- purefa_info - Add performance data for network interfaces
- purefa_info - Added new section ``realms``.
- purefa_info - Added new subset ``fleet``
- purefa_info - Deprecate ``network.<interface>.hwaddr`` - replaced by ``network.<interface>.mac_address``
- purefa_info - Deprecate ``network.<interface>.slaves`` - replaced by ``network.<interface>.subinterfaces``
- purefa_info - Expose directory service role management access policies if they exist
- purefa_info - Exposed password policy information
- purefa_info - SnaptoNFS support removed from Purity//FA 6.6.0 and higher.
- purefa_info - Update KMIP information collection to use REST v2, exposing full certifcate content
- purefa_info - VNC feature deprecated from Purity//FA 6.8.0.
- purefa_offload - Add support for S3 Offload ``uri`` and ``auth_region`` parameters
- purefa_pg - Added Fusion support.
- purefa_pgsched - Added support for Fusion.
- purefa_pgsnap - Added support for Fusion.
- purefa_pgsnap - Expose created protection group snapshot data in the module return dict
- purefa_pod_replica - Added Fusion support.
- purefa_pods - Added support for Fusion with ``context`` parameter.
- purefa_policy - New policy type of ``password`` added. Currently the only default management policy can be updated
- purefa_smtp - Added support for additional parameters, including encryption mode and email prefixs and email sender name.
- purefa_snap - Added Fusion support.
- purefa_subnet - Remove default value for MTU t ostop restting to default on enable/disable of subnet. Creation will still default to 1500 if not provided.
- purefa_timeout - Convert to REST v2
- purefa_user - Added parameter for SSH public keys and API token timeout
- purefa_user - Converted to use REST v2
- purefa_user - When changing API token or timout for an existing user, the user role must be provided or it will revert to ``readonly``
- purefa_vg - Added support for Fusion
- purefa_vlan - Convert to REST v2
- purefa_vnc - VNC feature deprecated from Purity//FA 6.8.0.
- purefa_volume - Added ``context`` parameter to support fleet operations

theforeman.foreman
~~~~~~~~~~~~~~~~~~

- Support Kerberos/GSSAPI authentication by passing ``use_gssapi: true`` instead of ``username`` and ``password``.
- Support setting a specific CA file for certificate validation
- activation_keys, content_credentials, content_view_publish, content_views, lifecycle_environments, repositories, sync_plans roles - Allow specifying the organization for each item individually (https://github.com/theforeman/foreman-ansible-modules/issues/1653)
- host, hostgroup, domain, operatingsystem, subnet, organization, location - support setting hidden parameters
- snapshot - add ``quiesce`` option (https://github.com/theforeman/foreman-ansible-modules/pull/1810)
- templates_import - Support configuring HTTP Proxy behaviour for template import

vmware.vmware
~~~~~~~~~~~~~

- _module_pyvmomi_base - Make sure to use the folder param when searching for VMs based on other common params in get_vms_using_params
- _vmware - standardize getter method names and documentation
- added vm_resource_info module to collect cpu/memory facts about vms
- argument specs - Remove redundant argument specs. Update pyvmomi modules to use new consolidated spec
- clients/_pyvmomi - adds explicit init params instead of using dict
- clients/_rest - adds explicit init params instead of using dict
- cluster_ha - migrate the vmware_cluster_ha module from community to here
- cluster_info - Migrate cluster_info module from the community.vmware collection to here
- content_library_item_info - Migrate content_library_item_info module from the vmware.vmware_rest collection to here
- content_template - Fix bad reference of library variable that was refactored to library_id
- deploy_content_library_ovf - migrate the vmware_content_deploy_ovf_template module from community to here
- deploy_content_library_ovf - update parameters to be consistent with other deploy modules
- deploy_content_library_template - migrate the vmware_content_deploy_template module from community to here
- deploy_content_library_template - update parameters to be consistent with other deploy modules
- deploy_folder_template - add module to deploy a vm from a template in a vsphere folder
- doc fragments - Remove redundant fragments. Update pyvmomi modules to use new consolidated docs
- esxi_connection - migrate the vmware_host module from community to here
- esxi_host - Added inventory plugin to gather info about ESXi hosts
- esxi_host - migrate the vmware_host module from community to here
- esxi_hosts - Add inventory host filtering based on jinja statements
- esxi_hosts inventory - include moid property in output always
- esxi_maintenance_mode - migrate esxi maintenance module from community
- folder - migrate vmware_folder module from community to here
- info - Made vm_name variable required only when state is set to present in content_template module
- local_content_library - migrate the vmware_content_library_manager module from community to here
- pyvmomi - update object search by name method to use propertycollector, which speeds up results significantly
- pyvmomi module base - refactor class to use the pyvmomi shared client util class as a base
- rest module base - refactor class to use the rest shared client util class as a base
- subscribed_content_library - migrate the vmware_content_library_manager module from community to here
- upload_content_library_ovf - Add module to upload an ovf/ova to a content library
- vm_powerstate - migrate vmware_guest_powerstate module from community to here
- vms - Add inventory host filtering based on jinja statements
- vms - added vms inventory plugin. consolidated shared docs/code with esxi hosts inventory plugin
- vms inventory - include moid property in output always

vmware.vmware_rest
~~~~~~~~~~~~~~~~~~

- Deprecated modules with redundant functionality in vmware.vmware. The next major release is currently not planned, so no removal date is provided. See https://github.com/ansible-collections/vmware.vmware_rest/issues/589
- info - changed relative links in README.md to absolute links

Breaking Changes / Porting Guide
--------------------------------

Ansible-core
~~~~~~~~~~~~

- Support for the ``toml`` library has been removed from TOML inventory parsing and dumping. Use ``tomli`` for parsing on Python 3.10. Python 3.11 and later have built-in support for parsing. Use ``tomli-w`` to support outputting inventory in TOML format.
- assert - The ``quiet`` argument must be a commonly-accepted boolean value. Previously, unrecognized values were silently treated as False.
- callback plugins - The structure of the ``exception``, ``warnings`` and ``deprecations`` values visible to callbacks has changed. Callbacks that inspect or serialize these values may require special handling.
- conditionals - Conditional expressions that result in non-boolean values are now an error by default. Such results often indicate unintentional use of templates where they are not supported, resulting in a conditional that is always true. When this option is enabled, conditional expressions which are a literal ``None`` or empty string will evaluate as true, for backwards compatibility. The error can be temporarily changed to a deprecation warning by enabling the ``ALLOW_BROKEN_CONDITIONALS`` config option.
- first_found lookup - When specifying ``files`` or ``paths`` as a templated list containing undefined values, the undefined list elements will be discarded with a warning. Previously, the entire list would be discarded without any warning.
- internals - The ``AnsibleLoader`` and ``AnsibleDumper`` classes for working with YAML are now factory functions and cannot be extended.
- internals - The ``ansible.utils.native_jinja`` Python module has been removed.
- inventory - Invalid variable names provided by inventories result in an inventory parse failure. This behavior is now consistent with other variable name usages throughout Ansible.
- lookup plugins - Lookup plugins called as `with_(lookup)` will no longer have the `_subdir` attribute set.
- lookup plugins - ``terms`` will always be passed to ``run`` as the first positional arg, where previously it was sometimes passed as a keyword arg when using ``with_`` syntax.
- loops - Omit placeholders no longer leak between loop item templating and task templating. Previously, ``omit`` placeholders could remain embedded in loop items after templating and be used as an ``omit`` for task templating. Now, values resolving to ``omit`` are dropped immediately when loop items are templated. To turn missing values into an ``omit`` for task templating, use ``| default(omit)``. This solution is backwards compatible with previous versions of ansible-core.
- modules - Ansible modules using ``sys.excepthook`` must use a standard ``try/except`` instead.
- plugins - Any plugin that sources or creates templates must properly tag them as trusted.
- plugins - Custom Jinja plugins that accept undefined top-level arguments must opt in to receiving them.
- plugins - Custom Jinja plugins that use ``environment.getitem`` to retrieve undefined values will now trigger a ``MarkerError`` exception. This exception must be handled to allow the plugin to return a ``Marker``, or the plugin must opt-in to accepting ``Marker`` values.
- public API - The ``ansible.vars.fact_cache.FactCache`` wrapper has been removed.
- serialization of ``omit`` sentinel - Serialization of variables containing ``omit`` sentinels (e.g., by the ``to_json`` and ``to_yaml`` filters or ``ansible-inventory``) will fail if the variable has not completed templating. Previously, serialization succeeded with placeholder strings emitted in the serialized output.
- set_fact - The string values "yes", "no", "true" and "false" were previously converted (ignoring case) to boolean values when not using Jinja2 native mode. Since Jinja2 native mode is always used, this conversion no longer occurs. When boolean values are required, native boolean syntax should be used where variables are defined, such as in YAML. When native boolean syntax is not an option, the ``bool`` filter can be used to parse string values into booleans.
- template lookup - The ``convert_data`` option is deprecated and no longer has any effect. Use the ``from_json`` filter on the lookup result instead.
- templating - Access to ``_`` prefixed attributes and methods, and methods with known side effects, is no longer permitted. In cases where a matching mapping key is present, the associated value will be returned instead of an error. This increases template environment isolation and ensures more consistent behavior between the ``.`` and ``[]`` operators.
- templating - Conditionals and lookups which use embedded inline templates in Jinja string constants now display a warning. These templates should be converted to their expression equivalent.
- templating - Many Jinja plugins (filters, lookups, tests) and methods previously silently ignored undefined inputs, which often masked subtle errors. Passing an undefined argument to a Jinja plugin or method that does not declare undefined support now results in an undefined value.
- templating - Templates are always rendered in Jinja2 native mode. As a result, non-string values are no longer automatically converted to strings.
- templating - Templates resulting in ``None`` are no longer automatically converted to an empty string.
- templating - Templates with embedded inline templates that were not contained within a Jinja string constant now result in an error, as support for multi-pass templating was removed for security reasons. In most cases, such templates can be easily rewritten to avoid the use of embedded inline templates.
- templating - The ``allow_unsafe_lookups`` option no longer has any effect. Lookup plugins are responsible for tagging strings containing templates to allow evaluation as a template.
- templating - The result of the ``range()`` global function cannot be returned from a template- it should always be passed to a filter (e.g., ``random``). Previously, range objects returned from an intermediate template were always converted to a list, which is inconsistent with inline consumption of range objects.
- templating - ``#jinja2:`` overrides in templates with invalid override names or types are now templating errors.

ansible.posix
~~~~~~~~~~~~~

- firewalld - Changed the type of forward and masquerade options from str to bool (https://github.com/ansible-collections/ansible.posix/issues/582).
- firewalld - Changed the type of icmp_block_inversion option from str to bool (https://github.com/ansible-collections/ansible.posix/issues/586).

community.postgresql
~~~~~~~~~~~~~~~~~~~~

- postgresql_info - the ``db`` alias is deprecated and will be removed in the next major release, use the ``login_db`` argument instead.
- postgresql_pg_hba - regarding #776 'keep_comments_at_rules' has been deprecated and won't do anything, the default is to keep the comments at the rules they are specified with. keep_comments_at_rules will be removed in 5.0.0 (https://github.com/ansible-collections/community.postgresql/pull/778)
- postgresql_user - the ``db`` alias is deprecated and will be removed in the next major release, use the ``login_db`` argument instead.

dellemc.enterprise_sonic
~~~~~~~~~~~~~~~~~~~~~~~~

- sonic_aaa - Update AAA module to align with SONiC functionality (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/382).
- sonic_bgp_communities - Change 'aann' option as a suboption of 'members' and update its type from string to list of strings (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/440).
- sonic_route_maps - Change the 'set ip_next_hop' option from a single-line option to a dictionary (https://github.com/ansible-collection/dellemc.enterprise_sonic/pull/421).
- sonic_vlan_mapping - New vlan_mapping resource module. The users of the vlan_mapping resource module with playbooks written for the SONiC 4.1 will need to revise their playbooks based on the new argspec to use those playbooks for SONiC 4.2 and later versions. (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/296).

theforeman.foreman
~~~~~~~~~~~~~~~~~~

- Drop support for Ansible 2.9.
- Drop support for Python 2.7 and 3.5.

Deprecated Features
-------------------

Ansible-core
~~~~~~~~~~~~

- CLI - The ``--inventory-file`` option alias is deprecated. Use the ``-i`` or ``--inventory`` option instead.
- Stategy Plugins - Use of strategy plugins not provided in ``ansible.builtin`` are deprecated and do not carry any backwards compatibility guarantees going forward. A future release will remove the ability to use external strategy plugins. No alternative for third party strategy plugins is currently planned.
- ``ansible.module_utils.compat.datetime`` - The datetime compatibility shims are now deprecated. They are scheduled to be removed in ``ansible-core`` v2.21. This includes ``UTC``, ``utcfromtimestamp()`` and ``utcnow`` importable from said module (https://github.com/ansible/ansible/pull/81874).
- bool filter - Support for coercing unrecognized input values (including None) has been deprecated. Consult the filter documentation for acceptable values, or consider use of the ``truthy`` and ``falsy`` tests.
- cache plugins - The `ansible.plugins.cache.base` Python module is deprecated. Use `ansible.plugins.cache` instead.
- callback plugins - The `v2_on_any` callback method is deprecated. Use specific callback methods instead.
- callback plugins - The v1 callback API (callback methods not prefixed with `v2_`) is deprecated. Use `v2_` prefixed methods instead.
- conditionals - Conditionals using Jinja templating delimiters (e.g., ``{{``, ``{%``) should be rewritten as expressions without delimiters, unless the entire conditional value is a single template that resolves to a trusted string expression. This is useful for dynamic indirection of conditional expressions, but is limited to trusted literal string expressions.
- config - The ``ACTION_WARNINGS`` config has no effect. It previously disabled command warnings, which have since been removed.
- config - The ``DEFAULT_JINJA2_NATIVE`` option has no effect. Jinja2 native mode is now the default and only option.
- config - The ``DEFAULT_NULL_REPRESENTATION`` option has no effect. Null values are no longer automatically converted to another value during templating of single variable references.
- display - The ``Display.get_deprecation_message`` method has been deprecated. Call ``Display.deprecated`` to display a deprecation message, or call it with ``removed=True`` to raise an ``AnsibleError``.
- file loading - Loading text files with ``DataLoader`` containing data that cannot be decoded under the expected encoding is deprecated. In most cases the encoding must be UTF-8, although some plugins allow choosing a different encoding. Previously, invalid data was silently wrapped in Unicode surrogate escape sequences, often resulting in later errors or other data corruption.
- first_found lookup - Splitting of file paths on ``,;:`` is deprecated. Pass a list of paths instead. The ``split`` method on strings can be used to split variables into a list as needed.
- interpreter discovery - The ``auto_legacy`` and ``auto_legacy_silent`` options for ``INTERPRETER_PYTHON`` are deprecated. Use ``auto`` or ``auto_silent`` options instead, as they have the same effect.
- oneline callback - The ``oneline`` callback and its associated ad-hoc CLI args (``-o``, ``--one-line``) are deprecated.
- paramiko - The paramiko connection plugin has been deprecated with planned removal in 2.21.
- playbook variables - The ``play_hosts`` variable has been deprecated, use ``ansible_play_batch`` instead.
- plugin error handling - The ``AnsibleError`` constructor arg ``suppress_extended_error`` is deprecated. Using ``suppress_extended_error=True`` has the same effect as ``show_content=False``.
- plugins - The ``listify_lookup_plugin_terms`` function is obsolete and in most cases no longer needed.
- template lookup - The jinja2_native option is no longer used in the Ansible Core code base. Jinja2 native mode is now the default and only option.
- templating - Support for enabling Jinja2 extensions (not plugins) has been deprecated.
- templating - The ``ansible_managed`` variable available for certain templating scenarios, such as the ``template`` action and ``template`` lookup has been deprecated. Define and use a custom variable instead of relying on ``ansible_managed``.
- templating - The ``disable_lookups`` option has no effect, since plugins must be updated to apply trust before any templating can be performed.
- to_yaml/to_nice_yaml filters - Implicit YAML dumping of vaulted value ciphertext is deprecated. Set `dump_vault_tags` to explicitly specify the desired behavior.
- tree callback - The ``tree`` callback and its associated ad-hoc CLI args (``-t``, ``--tree``) are deprecated.

amazon.aws
~~~~~~~~~~

- autoscaling_group - the ``decrement_desired_capacity`` parameter has been deprecated and will be removed in release 14.0.0 of this collection. Management of instances attached an autoscaling group can be performed using the  ``amazon.aws.autoscaling_instance`` module (https://github.com/ansible-collections/amazon.aws/pull/2396).
- autoscaling_group - the ``replace_batch_size``, ``lc_check`` and ``lt_check`` parameters have been deprecated and will be removed in release 14.0.0 of this collection. Rolling replacement of instances in an autoscaling group can be performed using the  ``amazon.aws.autoscaling_instance_refresh`` module (https://github.com/ansible-collections/amazon.aws/pull/2396).
- autoscaling_group - the functionality provided through the ``detach_instances`` parameter has been deprecated and will be removed in release 14.0.0 of this collection. Management of instances attached an autoscaling group can be performed using the  ``amazon.aws.autoscaling_instance`` module (https://github.com/ansible-collections/amazon.aws/pull/2396).
- autoscaling_group - the functionality provided through the ``replace_all_instances`` parameter has been deprecated and will be removed in release 14.0.0 of this collection. Rolling replacement of instances in an autoscaling group can be performed using the  ``amazon.aws.autoscaling_instance_refresh`` module (https://github.com/ansible-collections/amazon.aws/pull/2396).
- autoscaling_group - the functionality provided through the ``replace_instances`` parameter has been deprecated and will be removed in release 14.0.0 of this collection. Management of instances attached an autoscaling group can be performed using the  ``amazon.aws.autoscaling_instance`` module (https://github.com/ansible-collections/amazon.aws/pull/2396).

ansible.netcommon
~~~~~~~~~~~~~~~~~

- Added deprecation warnings for the above plugins, displayed when running respective filter plugins.
- `parse_cli_textfsm` filter plugin is deprecated and will be removed in a future release after 2027-02-01. Use `ansible.utils.cli_parse` with the `ansible.utils.textfsm_parser` parser as a replacement.
- `parse_cli` filter plugin is deprecated and will be removed in a future release after 2027-02-01. Use `ansible.utils.cli_parse` as a replacement.
- `parse_xml` filter plugin is deprecated and will be removed in a future release after 2027-02-01. Use `ansible.utils.cli_parse` with the `ansible.utils.xml_parser` parser as a replacement.

cisco.ios
~~~~~~~~~

- ios_vlans - deprecate mtu, please use ios_interfaces to configure mtu to the interface where vlans is applied.

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
- opkg - deprecate value ``""`` for parameter ``force`` (https://github.com/ansible-collections/community.general/pull/9172).
- profitbricks - module is deprecated and will be removed in community.general 11.0.0 (https://github.com/ansible-collections/community.general/pull/9733).
- profitbricks_datacenter - module is deprecated and will be removed in community.general 11.0.0 (https://github.com/ansible-collections/community.general/pull/9733).
- profitbricks_nic - module is deprecated and will be removed in community.general 11.0.0 (https://github.com/ansible-collections/community.general/pull/9733).
- profitbricks_volume - module is deprecated and will be removed in community.general 11.0.0 (https://github.com/ansible-collections/community.general/pull/9733).
- profitbricks_volume_attachments - module is deprecated and will be removed in community.general 11.0.0 (https://github.com/ansible-collections/community.general/pull/9733).
- proxmox - removes default value ``false`` of ``update`` parameter. This will be changed to a default of ``true`` in community.general 11.0.0 (https://github.com/ansible-collections/community.general/pull/9225).
- pure module utils - the module utils is deprecated and will be removed from community.general 12.0.0. The modules using this were removed in community.general 3.0.0 (https://github.com/ansible-collections/community.general/pull/9432).
- purestorage doc fragments - the doc fragment is deprecated and will be removed from community.general 12.0.0. The modules using this were removed in community.general 3.0.0 (https://github.com/ansible-collections/community.general/pull/9432).
- redfish_utils module utils - deprecate method ``RedfishUtils._init_session()`` (https://github.com/ansible-collections/community.general/pull/9190).
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

- module_utils.vmware - host_version_at_least is deprecated and will be removed in community.vmware 7.0.0 (https://github.com/ansible-collections/community.vmware/pull/2303).
- plugin_utils.inventory - this plugin util is deprecated and will be removed in community.vmware 7.0.0 (https://github.com/ansible-collections/community.vmware/pull/2304).
- plugins.httpapi - this is deprecated and will be removed in community.vmware 7.0.0 (https://github.com/ansible-collections/community.vmware/pull/2306).
- vcenter_folder - the module has been deprecated and will be removed in community.vmware 7.0.0 (https://github.com/ansible-collections/community.vmware/pull/2340).
- vm_device_helper.py - is_nvdimm_controller is deprecated and will be removed in community.vmware 7.0.0 (https://github.com/ansible-collections/community.vmware/pull/2311).
- vm_device_helper.py - is_nvdimm_device is deprecated and will be removed in community.vmware 7.0.0 (https://github.com/ansible-collections/community.vmware/pull/2311).
- vmware - find_host_portgroup_by_name is deprecated and will be removed in community.vmware 7.0.0 (https://github.com/ansible-collections/community.vmware/pull/2311).
- vmware - find_vmdk_file is deprecated and will be removed in community.vmware 7.0.0 (https://github.com/ansible-collections/community.vmware/pull/2311).
- vmware - network_exists_by_name is deprecated and will be removed in community.vmware 7.0.0 (https://github.com/ansible-collections/community.vmware/pull/2311).
- vmware - vmdk_disk_path_split is deprecated and will be removed in community.vmware 7.0.0 (https://github.com/ansible-collections/community.vmware/pull/2311).
- vmware_cluster_ha - the module has been deprecated and will be removed in community.vmware 7.0.0 (https://github.com/ansible-collections/community.vmware/pull/2321).
- vmware_cluster_info - the module has been deprecated and will be removed in community.vmware 7.0.0 (https://github.com/ansible-collections/community.vmware/pull/2260).
- vmware_content_deploy_ovf_template - the module has been deprecated and will be removed in community.vmware 7.0.0 (https://github.com/ansible-collections/community.vmware/pull/2332).
- vmware_content_deploy_template - the module has been deprecated and will be removed in community.vmware 7.0.0 (https://github.com/ansible-collections/community.vmware/pull/2332).
- vmware_content_library_manager - the module has been deprecated and will be removed in community.vmware 7.0.0 (https://github.com/ansible-collections/community.vmware/pull/2345).
- vmware_host - the module has been deprecated and will be removed in community.vmware 7.0.0 (https://github.com/ansible-collections/community.vmware/pull/2337).
- vmware_host_inventory - the inventory plugin is deprecated and will be removed in community.vmware 7.0.0 (https://github.com/ansible-collections/community.vmware/pull/2283).
- vmware_maintenancemode - the module has been deprecated and will be removed in community.vmware 7.0.0 (https://github.com/ansible-collections/community.vmware/pull/2293).
- vmware_rest_client - get_folder_by_name is deprecated and will be removed in community.vmware 7.0.0 (https://github.com/ansible-collections/community.vmware/pull/2311).
- vmware_vm_inventory - the inventory plugin is deprecated and will be removed in community.vmware 7.0.0 (https://github.com/ansible-collections/community.vmware/pull/2283).

vmware.vmware_rest
~~~~~~~~~~~~~~~~~~

- content_library_item_info - the module has been deprecated and will be removed in vmware.vmware_rest 5.0.0

Removed Features (previously deprecated)
----------------------------------------

- The collection ``ibm.spectrum_virtualize`` has been completely removed from Ansible.
  It has been renamed to ``ibm.storage_virtualize``.
  The collection will be completely removed from Ansible eventually.
  Please update your FQCNs from ``ibm.spectrum_virtualize`` to ``ibm.storage_virtualize``.
- The deprecated ``cisco.asa`` collection has been removed (`https://forum.ansible.com/t/38960 <https://forum.ansible.com/t/38960>`__).
- The deprecated ``community.network`` collection has been removed (`https://forum.ansible.com/t/8030 <https://forum.ansible.com/t/8030>`__).
- The google.cloud collection has been removed from Ansible 12 due to violations of the Ansible inclusion requirements.
  The collection has \ `unresolved sanity test failures <https://github.com/ansible-collections/google.cloud/issues/613>`__.
  See `Collections Removal Process for collections not satisfying the collection requirements <https://docs.ansible.com/ansible/devel/community/collection_contributors/collection_package_removal.html#collections-not-satisfying-the-collection-requirements>`__ for more details (`https://forum.ansible.com/t/8609 <https://forum.ansible.com/t/8609>`__).
  Users can still install this collection with ``ansible-galaxy collection install google.cloud``.
- The sensu.sensu_go collection has been removed from Ansible 12 due to violations of the Ansible inclusion requirements.
  The collection has \ `unresolved sanity test failures <https://github.com/sensu/sensu-go-ansible/issues/362>`__.
  See `Collections Removal Process for collections not satisfying the collection requirements <https://docs.ansible.com/ansible/devel/community/collection_contributors/collection_package_removal.html#collections-not-satisfying-the-collection-requirements>`__ for more details (`https://forum.ansible.com/t/8380 <https://forum.ansible.com/t/8380>`__).
  Users can still install this collection with ``ansible-galaxy collection install sensu.sensu_go``.

Ansible-core
~~~~~~~~~~~~

- Remove deprecated plural form of collection path (https://github.com/ansible/ansible/pull/84156).
- Removed deprecated STRING_CONVERSION_ACTION (https://github.com/ansible/ansible/issues/84220).
- encrypt - passing unsupported passlib hashtype now raises AnsibleFilterError.
- manager - remove deprecated include_delegate_to parameter from get_vars API.
- modules - Modules returning non-UTF8 strings now result in an error. The ``MODULE_STRICT_UTF8_RESPONSE`` setting can be used to disable this check.
- removed deprecated pycompat24 and compat.importlib.
- selector - remove deprecated compat.selector related files (https://github.com/ansible/ansible/pull/84155).
- windows - removed common module functions ``ConvertFrom-AnsibleJson``, ``Format-AnsibleException`` from Windows modules as they are not used and add uneeded complexity to the code.

ansible.posix
~~~~~~~~~~~~~

- skippy - Remove skippy pluglin as it is no longer supported(https://github.com/ansible-collections/ansible.posix/issues/350).

cisco.nxos
~~~~~~~~~~

- This release removes all deprecated plugins that have reached their end-of-life, including:
- nxos_snmp_community
- nxos_snmp_contact
- nxos_snmp_host
- nxos_snmp_location
- nxos_snmp_user

junipernetworks.junos
~~~~~~~~~~~~~~~~~~~~~

- This includes the following modules:
- This release removes all deprecated plugins that have reached their end-of-life.
- junos_scp

Security Fixes
--------------

Ansible-core
~~~~~~~~~~~~

- include_vars action - Ensure that result masking is correctly requested when vault-encrypted files are read. (CVE-2024-8775)
- task result processing - Ensure that action-sourced result masking (``_ansible_no_log=True``) is preserved. (CVE-2024-8775)
- templating - Ansible's template engine no longer processes Jinja templates in strings unless they are marked as coming from a trusted source. Untrusted strings containing Jinja template markers are ignored with a warning. Examples of trusted sources include playbooks, vars files, and many inventory sources. Examples of untrusted sources include module results and facts. Plugins which have not been updated to preserve trust while manipulating strings may inadvertently cause them to lose their trusted status.
- templating - Changes to conditional expression handling removed numerous instances of insecure multi-pass templating (which could result in execution of untrusted template expressions).
- user action won't allow ssh-keygen, chown and chmod to run on existing ssh public key file, avoiding traversal on existing symlinks (CVE-2024-9902).

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
- Correctly return ``False`` when using the ``filter`` and ``test`` Jinja tests on plugin names which are not filters or tests, respectively. (resolves issue https://github.com/ansible/ansible/issues/82084)
- Do not run implicit ``flush_handlers`` meta tasks when the whole play is excluded from the run due to tags specified.
- Errors now preserve stacked error messages even when YAML is involved.
- Fix a display.debug statement with the wrong param in _get_diff_data() method
- Fix disabling SSL verification when installing collections and roles from git repositories. If ``--ignore-certs`` isn't provided, the value for the ``GALAXY_IGNORE_CERTS`` configuration option will be used (https://github.com/ansible/ansible/issues/83326).
- Fix ipv6 pattern bug in lib/ansible/parsing/utils/addresses.py (https://github.com/ansible/ansible/issues/84237)
- Fix returning 'unreachable' for the overall task result. This prevents false positives when a looped task has unignored unreachable items (https://github.com/ansible/ansible/issues/84019).
- Implicit ``meta: flush_handlers`` tasks now have a parent block to prevent potential tracebacks when calling methods like ``get_play()`` on them internally.
- Improve performance on large inventories by reducing the number of implicit meta tasks.
- Jinja plugins - Errors raised will always be derived from ``AnsibleTemplatePluginError``.
- Optimize the way tasks from within ``include_tasks``/``include_role`` are inserted into the play.
- Time out waiting on become is an unreachable error (https://github.com/ansible/ansible/issues/84468)
- Use consistent multiprocessing context for action write locks
- Use the requested error message in the ansible.module_utils.facts.timeout timeout function instead of hardcoding one.
- Windows - add support for running on system where WDAC is in audit mode with ``Dynamic Code Security`` enabled.
- YAML parsing - The `!unsafe` tag no longer coerces non-string scalars to strings.
- ``ansible-galaxy`` — the collection dependency resolver now treats version specifiers starting with ``!=`` as unpinned.
- ``package``/``dnf`` action plugins - provide the reason behind the failure to gather the ``ansible_pkg_mgr`` fact to identify the package backend
- action plugins - Action plugins that raise unhandled exceptions no longer terminate playbook loops. Previously, exceptions raised by an action plugin caused abnormal loop termination and loss of loop iteration results.
- ansible-config - format galaxy server configs while dumping in JSON format (https://github.com/ansible/ansible/issues/84840).
- ansible-doc - If none of the files in files exists, path will be undefined and a direct reference will throw an UnboundLocalError (https://github.com/ansible/ansible/pull/84464).
- ansible-galaxy - Small adjustments to URL building for ``download_url`` and relative redirects.
- ansible-pull change detection will now work independently of callback or result format settings.
- ansible-test - Enable the ``sys.unraisablehook`` work-around for the ``pylint`` sanity test on Python 3.11. Previously the work-around was only enabled for Python 3.12 and later. However, the same issue has been discovered on Python 3.11.
- ansible-test - Ensure CA certificates are installed on managed FreeBSD instances.
- ansible-test - Fix support for PowerShell module_util imports with the ``-Optional`` flag.
- ansible-test - Fix support for detecting PowerShell modules importing module utils with the newer ``#AnsibleRequires`` format.
- ansible-test - Fix traceback that occurs after an interactive command fails.
- ansible-test - Fix up coverage reporting to properly translate the temporary path of integration test modules to the expected static test module path.
- ansible-test - Fixed traceback when handling certain YAML errors in the ``yamllint`` sanity test.
- ansible-test - Managed macOS instances now use the ``sudo_chdir`` option for the ``sudo`` become plugin to avoid permission errors when dropping privileges.
- ansible-vault will now correctly handle `--prompt`, previously it would issue an error about stdin if no 2nd argument was passed
- ansible_uptime_second - added ansible_uptime_seconds fact support for AIX (https://github.com/ansible/ansible/pull/84321).
- apt_key module - prevent tests from running when apt-key was removed
- base.yml - deprecated libvirt_lxc_noseclabel config.
- build - Pin ``wheel`` in ``pyproject.toml`` to ensure compatibility with supported ``setuptools`` versions.
- config - various fixes to config lookup plugin (https://github.com/ansible/ansible/pull/84398).
- copy - refactor copy module for simplicity.
- copy action now prevents user from setting internal options.
- debconf - set empty password values (https://github.com/ansible/ansible/issues/83214).
- debug - hide loop vars in debug var display (https://github.com/ansible/ansible/issues/65856).
- default callback - Error context is now shown for failing tasks that use the ``debug`` action.
- display - The ``Display.deprecated`` method once again properly handles the ``removed=True`` argument (https://github.com/ansible/ansible/issues/82358).
- distro - add support for Linux Mint Debian Edition (LMDE) (https://github.com/ansible/ansible/issues/84934).
- distro - detect Debian as os_family for LMDE 6 (https://github.com/ansible/ansible/issues/84934).
- dnf5 - Handle forwarded exceptions from dnf5-5.2.13 where a generic ``RuntimeError`` was previously raised
- dnf5 - fix ``is_installed`` check for packages that are not installed but listed as provided by an installed package (https://github.com/ansible/ansible/issues/84578)
- dnf5 - fix installing a package using ``state=latest`` when a binary of the same name as the package is already installed (https://github.com/ansible/ansible/issues/84259)
- dnf5 - fix traceback when ``enable_plugins``/``disable_plugins`` is used on ``python3-libdnf5`` versions that do not support this functionality
- dnf5 - libdnf5 - use ``conf.pkg_gpgcheck`` instead of deprecated ``conf.gpgcheck`` which is used only as a fallback
- dnf5 - matching on a binary can be achieved only by specifying a full path (https://github.com/ansible/ansible/issues/84334)
- facts - gather pagesize and calculate respective values depending upon architecture (https://github.com/ansible/ansible/issues/84773).
- facts - skip if distribution file path is directory, instead of raising error (https://github.com/ansible/ansible/issues/84006).
- find - skip ENOENT error code while recursively enumerating files. find module will now be tolerant to race conditions that remove files or directories from the target it is currently inspecting. (https://github.com/ansible/ansible/issues/84873).
- first_found lookup - Corrected return value documentation to reflect None (not empty string) for no files found.
- gather_facts action now defaults to `ansible.legacy.setup` if `smart` was set, no network OS was found and no other alias for `setup` was present.
- gather_facts action will now issues errors and warnings as appropriate if a network OS is detected but no facts modules are defined for it.
- gather_facts action, will now add setup when 'smart' appears with other modules in the FACTS_MODULES setting (#84750).
- get_url - add support for BSD-style checksum digest file (https://github.com/ansible/ansible/issues/84476).
- get_url - fix honoring ``filename`` from the ``content-disposition`` header even when the type is ``inline`` (https://github.com/ansible/ansible/issues/83690)
- host_group_vars - fixed defining the 'key' variable if the get_vars method is called with cache=False (https://github.com/ansible/ansible/issues/84384)
- include_vars - fix including previously undefined hash variables with hash_behaviour merge (https://github.com/ansible/ansible/issues/84295).
- iptables - Allows the wait parameter to be used with iptables chain creation (https://github.com/ansible/ansible/issues/84490)
- linear strategy - fix executing ``end_role`` meta tasks for each host, instead of handling these as implicit run_once tasks (https://github.com/ansible/ansible/issues/84660).
- local connection plugin - Become timeout errors now include all received data. Previously, the most recently-received data was discarded.
- local connection plugin - Ensure ``become`` success validation always occurs, even when an active plugin does not set ``prompt``.
- local connection plugin - Fixed cases where the internal ``BECOME-SUCCESS`` message appeared in task output.
- local connection plugin - Fixed hang or spurious failure when data arrived concurrently on stdout and stderr during a successful ``become`` operation validation.
- local connection plugin - Fixed hang when a become plugin expects a prompt but a password was not provided.
- local connection plugin - Fixed hang when an active become plugin incorrectly signals lack of prompt.
- local connection plugin - Fixed hang when an internal become read timeout expired before the password prompt was written.
- local connection plugin - Fixed hang when only one of stdout or stderr was closed by the ``become_exe`` subprocess.
- local connection plugin - Fixed long timeout/hang for ``become`` plugins that repeat their prompt on failure (e.g., ``sudo``, some ``su`` implementations).
- local connection plugin - Fixed silent ignore of ``become`` failures and loss of task output when data arrived concurrently on stdout and stderr during ``become`` operation validation.
- local connection plugin - Fixed task output header truncation when post-become data arrived before ``become`` operation validation had completed.
- lookup plugins - The ``terms`` arg to the ``run`` method is now always a list. Previously, there were cases where a non-list could be received.
- module arg templating - When using a templated raw task arg and a templated ``args`` keyword, args are now merged. Previously use of templated raw task args silently ignored all values from the templated ``args`` keyword.
- module defaults - Module defaults are no longer templated unless they are used by a task that does not override them. Previously, all module defaults for all modules were templated for every task.
- module respawn - limit to supported Python versions
- omitting task args - Use of omit for task args now properly falls back to args of lower precedence, such as module defaults. Previously an omitted value would obliterate values of lower precedence.
- package_facts module when using 'auto' will return the first package manager found that provides an output, instead of just the first one, as this can be foreign and not have any packages.
- psrp - Improve stderr parsing when running raw commands that emit error records or stderr lines.
- regex_search filter - Corrected return value documentation to reflect None (not empty string) for no match.
- respawn - use copy of env variables to update existing PYTHONPATH value (https://github.com/ansible/ansible/issues/84954).
- runas become - Fix up become logic to still get the SYSTEM token with the most privileges when running as SYSTEM.
- sequence lookup - sequence query/lookups without positional arguments now return a valid list if their kwargs comprise a valid sequence expression (https://github.com/ansible/ansible/issues/82921).
- service_facts - skip lines which does not contain service names in openrc output (https://github.com/ansible/ansible/issues/84512).
- ssh - Improve the logic for parsing CLIXML data in stderr when working with Windows host. This fixes issues when the raw stderr contains invalid UTF-8 byte sequences and improves embedded CLIXML sequences.
- ssh - Raise exception when sshpass returns error code (https://github.com/ansible/ansible/issues/58133).
- ssh - connection options were incorrectly templated during ``reset_connection`` tasks (https://github.com/ansible/ansible/pull/84238).
- stability - Fixed silent process failure on unhandled IOError/OSError under ``linear`` strategy.
- su become plugin - Ensure generated regex from ``prompt_l10n`` config values is properly escaped.
- su become plugin - Ensure that password prompts are correctly detected in the presence of leading output. Previously, this case resulted in a timeout or hang.
- su become plugin - Ensure that trailing colon is expected on all ``prompt_l10n`` config values.
- sudo become plugin - The `sudo_chdir` config option allows the current directory to be set to the specified value before executing sudo to avoid permission errors when dropping privileges.
- sunos - remove hard coding of virtinfo command in facts gathering code (https://github.com/ansible/ansible/pull/84357).
- to_yaml/to_nice_yaml filters - Eliminated possibility of keyword arg collisions with internally-set defaults.
- unarchive - Clamp timestamps from beyond y2038 to representible values when unpacking zip files on platforms that use 32-bit time_t (e.g. Debian i386).
- uri - Form location correctly when the server returns a relative redirect (https://github.com/ansible/ansible/issues/84540)
- uri - Handle HTTP exceptions raised while reading the content (https://github.com/ansible/ansible/issues/83794).
- uri - mark ``url`` as required (https://github.com/ansible/ansible/pull/83642).
- user - Create Buildroot subclass as alias to Busybox (https://github.com/ansible/ansible/issues/83665).
- user - Set timeout for passphrase interaction.
- user - Update prompt for SSH key passphrase (https://github.com/ansible/ansible/issues/84484).
- user - Use higher precedence HOME_MODE as UMASK for path provided (https://github.com/ansible/ansible/pull/84482).
- user action will now require O(force) to overwrite the public part of an ssh key when generating ssh keys, as was already the case for the private part.
- user module now avoids changing ownership of files symlinked in provided home dir skeleton
- vars lookup - The ``default`` substitution only applies when trying to look up a variable which is not defined. If the variable is defined, but templates to an undefined value, the ``default`` substitution will not apply. Use the ``default`` filter to coerce those values instead.
- wait_for_connection - a warning was displayed if any hosts used a local connection (https://github.com/ansible/ansible/issues/84419)

amazon.aws
~~~~~~~~~~

- cloudformation - Fix bug where termination protection is not updated when create_changeset=true is used for stack updates (https://github.com/ansible-collections/amazon.aws/pull/2391).
- ec2_instance - Fix issue where EC2 instance module failed to apply security groups when both ``network`` and ``vpc_subnet_id`` were specified, caused by passing ``None`` to discover_security_groups() (https://github.com/ansible-collections/amazon.aws/pull/2488).
- ec2_security_group - Fix the diff mode issue when creating a security group containing a rule with a managed prefix list (https://github.com/ansible-collections/amazon.aws/issues/2373).
- ec2_vpc_nacl_info - Fix failure when listing NetworkACLs and no ACLs are found (https://github.com/ansible-collections/amazon.aws/issues/2425).
- ec2_vpc_net - handle ipv6_cidr ``false`` and no Ipv6CidrBlockAssociationSet in vpc (https://github.com/ansible-collections/amazon.aws/pull/2374).
- elbv2 - Fix load balancer listener comparison when DefaultActions contain any action other than forward (https://github.com/ansible-collections/amazon.aws/issues/2377).
- iam_access_key - add missing requirements checks (https://github.com/ansible-collections/amazon.aws/pull/2465).
- lambda - Remove non UTF-8 data (contents of Lambda ZIP file) from the module output to avoid Ansible error (https://github.com/ansible-collections/amazon.aws/issues/2386).
- lookup/aws_account_attribute - plugin should return a list when ``wantlist=True`` (https://github.com/ansible-collections/amazon.aws/pull/2552).
- module_utils.botocore - fixed type aliasing (https://github.com/ansible-collections/amazon.aws/pull/2497).
- module_utils/ec2 - catch error code ``InvalidElasticIpID.NotFound`` on function ``create_nat_gateway()``, sometimes the ``allocate_address`` API calls will return the ID for a new elastic IP resource before it can be consistently referenced (https://github.com/ansible-collections/amazon.aws/issues/1872).
- plugin_utils.botocore - fixed type aliasing (https://github.com/ansible-collections/amazon.aws/pull/2497).
- rds_cluster - Fix issue occurring when updating RDS cluster domain (https://github.com/ansible-collections/amazon.aws/issues/2390).
- s3_bucket - Do not use default region as location constraint when creating bucket on ceph cluster (https://github.com/ansible-collections/amazon.aws/issues/2420).

ansible.netcommon
~~~~~~~~~~~~~~~~~

- libssh connection plugin - stop using long-deprecated and now removed internal field from ansible-core's base connection plugin class (https://github.com/ansible-collections/ansible.netcommon/issues/522, https://github.com/ansible-collections/ansible.netcommon/issues/690, https://github.com/ansible-collections/ansible.netcommon/pull/691).

ansible.posix
~~~~~~~~~~~~~

- acl - Fixed to set ACLs on paths mounted with NFS version 4 correctly (https://github.com/ansible-collections/ansible.posix/issues/240).
- mount - Handle ``boot`` option on Linux, NetBSD and OpenBSD correctly (https://github.com/ansible-collections/ansible.posix/issues/364).
- mount - If a comment is appended to a fstab entry, state present creates a double-entry (https://github.com/ansible-collections/ansible.posix/issues/595).

ansible.windows
~~~~~~~~~~~~~~~

- ansible.windows.win_powershell - Add extra checks to avoid ``GetType`` error when converting the output object - ttps://github.com/ansible-collections/ansible.windows/issues/708
- setup - Add better detection for VMWare base virtualization platforms - https://github.com/ansible-collections/ansible.windows/issues/753
- win_group_membership - Fix bug when input ``members`` contained duplicate members that were not already present in the group - https://github.com/ansible-collections/ansible.windows/issues/736
- win_package - Support check mode with local file path sources
- win_powershell - Ensure ``$Ansible.Result = @()`` as an empty array is returned as an empty list and not null - https://github.com/ansible-collections/ansible.windows/issues/686
- win_updates - Only set the Access control sections on the temporary directory created by the module. This avoids the error when the ``SeSecurityPrivilege`` privilege isn't present.

arista.eos
~~~~~~~~~~

- Fixed an issue in the `compare_configs` method where unnecessary negate commands were generated for ACL entries already present in both `have` and `want` configurations.
- Improved validation logic for ACL sequence numbers and content matching to ensure idempotency.
- Prevented redundant configuration updates for Access Control Lists.
- fix facts gathering for ebgp-multihop attribute.

cisco.ios
~~~~~~~~~

- Added a test to validate the gathered state for VLAN configuration context, improving reliability.
- Added support for FourHundredGigE, FiftyGigE and FourHundredGigabitEthernet.
- Cleaned up unit tests that were passing for the wrong reasons. The updated tests now ensure the right config sections are verified for VLAN configurations.
- Fix overridden state operations to ensure excluded VLANs in the provided configuration are removed, thus overriding the VLAN configuration.
- Fix purged state operation to enable users to completely remove VLAN configurations.
- Fixed an issue with VLAN configuration gathering where pre-filled data was blocking proper fetching of dynamic VLAN details. Now VLAN facts are populated correctly for all cases.
- Fixes an issue with facts gathering failing when an sub interface is in a deleted state.
- Improve documentation to provide clarity on the "shutdown" variable.
- Improve unit tests to align with the changes made.
- Made improvements to ensure VLAN facts are gathered properly, both for specific configurations and general VLAN settings.
- ios_acls - Fixed issue where cisco.ios.ios_acls module failed to process IPv6 ACL remarks, causing unsupported parameter errors.
- ios_logging_global - Fixed issue where cisco.ios.logging_global module was not showing idempotent behaviour when trap was set to informational.
- ios_route_maps - Fix removal of ACLs in replaced state to properly remove unspecified ACLs while leaving specified ones intact.
- ios_route_maps - Fix removal of ACLs logic in replaced state to properly remove unspecified ACLs while leaving specified ones intact.
- ios_route_maps - Fixes an issue where 'no description value' is an invalid command on the latest devices.
- ios_vlans - Defaut mtu would be captured (1500) and no configuration for mtu is allowed via ios_vlans module.
- ios_vlans - Fixed an issue in the `cisco.ios.ios_vlans` module on Cisco Catalyst 9000 switches where using state:purged generated an incorrect command syntax (`no vlan configuration <vlan_id>` instead of `no vlan <vlan_id>`).
- ios_vlans - Resolved a failure in the `cisco.ios.ios_vlans` module when using state:deleted, where the module incorrectly attempted to remove VLANs using `no mtu <value>`, causing an invalid input error. The fix ensures that the module does not generate `no mtu` commands during VLAN deletion, aligning with the correct VLAN removal behavior on Catalyst 9000 switches.

cisco.iosxr
~~~~~~~~~~~

- Fixes a bug to allow connections to IOS XRd with cliconf.
- Fixes idempotency for static routes with encap interfaces

cisco.ise
~~~~~~~~~

- network_device - Fix mask validation to handle None values in NetworkDeviceIPList
- personas_promote_primary - fix timeout issue.

cisco.meraki
~~~~~~~~~~~~

- Ansible utils requirements updated.
- Change alias 'message' to 'message_rule' due is a reserved ansible word in meraki_mx_intrusion_prevention module.
- Changes at compare equality function.
- Issue fixes for workflow-ansible-lint.
- Old playbook tests removed.
- README fixes.
- Unable to create Syslog Server Object. Action module manually fixing.
- cisco.meraki.devices_switch_ports idempotency error fixed.
- cisco.meraki.networks_appliance_firewall_l3_firewall_rules fails with "Unexpected failure during module execution 'rules' - specific 'rules' extraction has been removed.
- cisco.meraki.networks_appliance_traffic_shaping_rules Always Pushes Configuration Even When Unchanged.
- cisco.meraki.networks_appliance_vlans_settings fails with "msg" "Object does not exists, plugin only has update" - specific 'vlansEnabled' extraction has been removed.
- cisco.meraki.networks_clients_info - incorrect API endpoint, fixing info module.
- cisco.meraki.networks_devices_claim failed with error unexpected keyword argument 'add_atomically' - bad naming solved.
- cisco.meraki.networks_switch_stacks delete stack not working, fixing path parameters.
- cisco.meraki.organizations_login_security module update organization security settings.
- runtime updated requires_ansible from 2.14.0 to '>=2.15.0'.

cisco.nxos
~~~~~~~~~~

- Fixed hardware fact gathering failure for CPU utilization parsing on NX-OS 9.3(3) by handling both list and single value formats of onemin_percent
- Fixed the invalid feature name error for port-security by updating the feature mapping from `eth_port_sec` to `eth-port-sec`.
- Fixes mixed usage of f-string and format string in action plugin for consistency.
- Fixes nxos_user purge deleting non-local users,ensuring only local users are removed.
- [bgp_templates] - fix the show commands used to ensure task does not fail if BGP is not enabled on the device.
- lag_interfaces - Fix bug where lag interfaces was not erroring on command failure. (https://github.com/ansible-collections/cisco.nxos/pull/923)
- nxos_facts - Fixes an issue in nxos_facts where IPv6 addresses within VRF contexts were not being collected in `net_all_ipv6_addresses`.
- nxos_l2_interfaces - Fixed handling of 'none' value in allowed_vlans to properly set trunk VLAN none
- nxos_user - fixes wrong command being generated for purge function
- nxos_vpc - fixes failure due to kickstart_ver_str not being present

community.aws
~~~~~~~~~~~~~

- aws_ssm - use ``head_bucket`` to access bucket locations in foreign aws accounts (https://github.com/ansible-collections/community.aws/pull/1987).
- ssm - strip Powershell CLIXML from stdout (https://github.com/ansible-collections/community.aws/issues/1952).

community.crypto
~~~~~~~~~~~~~~~~

- crypto_info - when running the module on Fedora 41 with ``cryptography`` installed from the package repository, the module crashed apparently due to some elliptic curves being removed from libssl against which cryptography is running, which cryptography did not expect (https://github.com/ansible-collections/community.crypto/pull/834).

community.dns
~~~~~~~~~~~~~

- Fix various issues and potential bugs pointed out by linters (https://github.com/ansible-collections/community.dns/pull/242, https://github.com/ansible-collections/community.dns/pull/243).
- Update Public Suffix List.

community.docker
~~~~~~~~~~~~~~~~

- Fix label sanitization code to avoid crashes in case of errors (https://github.com/ansible-collections/community.docker/issues/1028, https://github.com/ansible-collections/community.docker/pull/1029).
- docker_compose_v2 - fix version check for ``assume_yes`` (https://github.com/ansible-collections/community.docker/pull/1054).
- docker_compose_v2 - rename flag for ``assume_yes`` parameter for ``docker compose up`` to ``-y`` (https://github.com/ansible-collections/community.docker/pull/1054).
- docker_compose_v2 - use ``--yes`` instead of ``-y`` from Docker Compose 2.34.0 on (https://github.com/ansible-collections/community.docker/pull/1060).
- docker_compose_v2 - when using Compose 2.31.0 or newer, revert to the old behavior that image rebuilds, for example if ``rebuild=always``, only result in ``changed`` if a container has been restarted (https://github.com/ansible-collections/community.docker/issues/1005, https://github.com/ansible-collections/community.docker/issues/pull/1011).
- docker_compose_v2_exec, docker_compose_v2_run - fix missing ``--env`` flag while assembling env arguments (https://github.com/ansible-collections/community.docker/pull/992).
- docker_compose_v2_run - the module has a conflict between the type of parameter it expects and the one it tries to sanitize. Fix removes the label sanitization step because they are already validated by the parameter definition (https://github.com/ansible-collections/community.docker/pull/1034).
- docker_host_info - ensure that the module always returns ``can_talk_to_docker``, and that it provides the correct value even if ``api_version`` is specified (https://github.com/ansible-collections/community.docker/issues/993, https://github.com/ansible-collections/community.docker/pull/995).
- docker_image_build - work around bug resp. very unexpected behavior in Docker buildx that overwrites all image names in ``--output`` parameters if ``--tag`` is provided, which the module did by default in the past. The module now only supplies ``--tag`` if ``outputs`` is empty. If ``outputs`` has entries, it will add an additional entry with ``type=image`` if no entry of ``type=image`` contains the image name specified by the ``name`` and ``tag`` options (https://github.com/ansible-collections/community.docker/issues/1001, https://github.com/ansible-collections/community.docker/pull/1006).
- docker_network - added waiting while container actually disconnect from Swarm network (https://github.com/ansible-collections/community.docker/pull/999).
- docker_network - containers are only reconnected to a network if they really exist (https://github.com/ansible-collections/community.docker/pull/999).
- docker_network - enabled "force" option in Docker network container disconnect API call (https://github.com/ansible-collections/community.docker/pull/999).
- docker_swarm_info - do not crash when finding Swarm jobs if ``services=true`` (https://github.com/ansible-collections/community.docker/issues/1003).
- vendored Docker SDK for Python - do not assume that ``KeyError`` is always for ``ApiVersion`` when querying version fails (https://github.com/ansible-collections/community.docker/issues/1033, https://github.com/ansible-collections/community.docker/pull/1034).

community.general
~~~~~~~~~~~~~~~~~

- apache2_mod_proxy - make compatible with Python 3 (https://github.com/ansible-collections/community.general/pull/9762).
- apache2_mod_proxy - passing the cluster's page as referer for the member's pages. This makes the module actually work again for halfway modern Apache versions. According to some comments founds on the net the referer was required since at least 2019 for some versions of Apache 2 (https://github.com/ansible-collections/community.general/pull/9762).
- cloudflare_dns - fix crash when deleting a DNS record or when updating a record with ``solo=true`` (https://github.com/ansible-collections/community.general/issues/9652, https://github.com/ansible-collections/community.general/pull/9649).
- cloudlare_dns - handle exhausted response stream in case of HTTP errors to show nice error message to the user (https://github.com/ansible-collections/community.general/issues/9782, https://github.com/ansible-collections/community.general/pull/9818).
- dig lookup plugin - correctly handle ``NoNameserver`` exception (https://github.com/ansible-collections/community.general/pull/9363, https://github.com/ansible-collections/community.general/issues/9362).
- dnf_config_manager - fix hanging when prompting to import GPG keys (https://github.com/ansible-collections/community.general/pull/9124, https://github.com/ansible-collections/community.general/issues/8830).
- dnf_config_manager - forces locale to ``C`` before module starts. If the locale was set to non-English, the output of the ``dnf config-manager`` could not be parsed (https://github.com/ansible-collections/community.general/pull/9157, https://github.com/ansible-collections/community.general/issues/9046).
- dnf_versionlock - add support for dnf5 (https://github.com/ansible-collections/community.general/issues/9556).
- elasticsearch_plugin - fix ``ERROR: D is not a recognized option`` issue when configuring proxy settings (https://github.com/ansible-collections/community.general/pull/9774, https://github.com/ansible-collections/community.general/issues/9773).
- flatpak - force the locale language to ``C`` when running the flatpak command (https://github.com/ansible-collections/community.general/pull/9187, https://github.com/ansible-collections/community.general/issues/8883).
- gio_mime - fix command line when determining version of ``gio`` (https://github.com/ansible-collections/community.general/pull/9171, https://github.com/ansible-collections/community.general/issues/9158).
- github_key - in check mode, a faulty call to ```datetime.strftime(...)``` was being made which generated an exception (https://github.com/ansible-collections/community.general/issues/9185).
- homebrew - fix crash when package names include tap (https://github.com/ansible-collections/community.general/issues/9777, https://github.com/ansible-collections/community.general/pull/9803).
- homebrew - fix incorrect handling of aliased homebrew modules when the alias is requested (https://github.com/ansible-collections/community.general/pull/9255, https://github.com/ansible-collections/community.general/issues/9240).
- homebrew - fix incorrect handling of homebrew modules when a tap is requested (https://github.com/ansible-collections/community.general/pull/9546, https://github.com/ansible-collections/community.general/issues/9533).
- homebrew - make package name parsing more resilient (https://github.com/ansible-collections/community.general/pull/9665, https://github.com/ansible-collections/community.general/issues/9641).
- homebrew_cask - allow ``+`` symbol in Homebrew cask name validation regex (https://github.com/ansible-collections/community.general/pull/9128).
- homebrew_cask - handle unusual brew version strings (https://github.com/ansible-collections/community.general/issues/8432, https://github.com/ansible-collections/community.general/pull/9881).
- htpasswd - report changes when file permissions are adjusted (https://github.com/ansible-collections/community.general/issues/9485, https://github.com/ansible-collections/community.general/pull/9490).
- iocage inventory plugin - the plugin parses the IP4 tab of the jails list and put the elements into the new variable ``iocage_ip4_dict``. In multiple interface format the variable ``iocage_ip4`` keeps the comma-separated list of IP4 (https://github.com/ansible-collections/community.general/issues/9538).
- ipa_host - module revoked existing host certificates even if ``user_certificate`` was not given (https://github.com/ansible-collections/community.general/pull/9694).
- keycloak module utils - replaces missing return in get_role_composites method which caused it to return None instead of composite roles (https://github.com/ansible-collections/community.general/issues/9678, https://github.com/ansible-collections/community.general/pull/9691).
- keycloak_client - fix and improve existing tests. The module showed a diff without actual changes, solved by improving the ``normalise_cr()`` function (https://github.com/ansible-collections/community.general/pull/9644).
- keycloak_client - in check mode, detect whether the lists in before client (for example redirect URI list) contain items that the lists in the desired client do not contain (https://github.com/ansible-collections/community.general/pull/9739).
- keycloak_clientscope_type - sort the default and optional clientscope lists to improve the diff (https://github.com/ansible-collections/community.general/pull/9202).
- lldp - fix crash caused by certain lldpctl output where an attribute is defined as branch and leaf (https://github.com/ansible-collections/community.general/pull/9657).
- nmcli - enable changing only the order of DNS servers or search suffixes (https://github.com/ansible-collections/community.general/issues/8724, https://github.com/ansible-collections/community.general/pull/9880).
- onepassword_doc lookup plugin - ensure that 1Password Connect support also works for this plugin (https://github.com/ansible-collections/community.general/pull/9625).
- passwordstore lookup plugin - fix subkey creation even when ``create=false`` (https://github.com/ansible-collections/community.general/issues/9105, https://github.com/ansible-collections/community.general/pull/9106).
- pipx - honor option ``global`` when ``state=latest`` (https://github.com/ansible-collections/community.general/pull/9623).
- proxmox - add missing key selection of ``'status'`` key to ``get_lxc_status`` (https://github.com/ansible-collections/community.general/issues/9696, https://github.com/ansible-collections/community.general/pull/9809).
- proxmox - adds the ``pubkey`` parameter (back to) the ``update`` state (https://github.com/ansible-collections/community.general/issues/9642, https://github.com/ansible-collections/community.general/pull/9645).
- proxmox - fixes a typo in the translation of the ``pubkey`` parameter to proxmox' ``ssh-public-keys`` (https://github.com/ansible-collections/community.general/issues/9642, https://github.com/ansible-collections/community.general/pull/9645).
- proxmox - fixes idempotency of template conversions (https://github.com/ansible-collections/community.general/pull/9225, https://github.com/ansible-collections/community.general/issues/8811).
- proxmox - fixes incorrect parsing for bind-only mounts (https://github.com/ansible-collections/community.general/pull/9225, https://github.com/ansible-collections/community.general/issues/8982).
- proxmox - fixes issues with disk_volume variable (https://github.com/ansible-collections/community.general/pull/9225, https://github.com/ansible-collections/community.general/issues/9065).
- proxmox inventory plugin - plugin did not update cache correctly after ``meta: refresh_inventory`` (https://github.com/ansible-collections/community.general/issues/9710, https://github.com/ansible-collections/community.general/pull/9760).
- proxmox module utils - fixes ignoring of ``choose_first_if_multiple`` argument in ``get_vmid`` (https://github.com/ansible-collections/community.general/pull/9225).
- proxmox_backup - fix incorrect key lookup in vmid permission check (https://github.com/ansible-collections/community.general/pull/9223).
- proxmox_disk - fix async method and make ``resize_disk`` method handle errors correctly (https://github.com/ansible-collections/community.general/pull/9256).
- proxmox_template - fix the wrong path called on ``proxmox_template.task_status`` (https://github.com/ansible-collections/community.general/issues/9276, https://github.com/ansible-collections/community.general/pull/9277).
- proxmox_vm_info - the module no longer expects that the key ``template`` exists in a dictionary returned by Proxmox (https://github.com/ansible-collections/community.general/issues/9875, https://github.com/ansible-collections/community.general/pull/9910).
- qubes connection plugin - fix the printing of debug information (https://github.com/ansible-collections/community.general/pull/9334).
- redfish_utils module utils - Fix ``VerifyBiosAttributes`` command on multi system resource nodes (https://github.com/ansible-collections/community.general/pull/9234).
- redhat_subscription - do not try to unsubscribe (i.e. remove subscriptions)
  when unregistering a system: newer versions of subscription-manager, as
  available in EL 10 and Fedora 41+, do not support entitlements anymore, and
  thus unsubscribing will fail
  (https://github.com/ansible-collections/community.general/pull/9578).
- redhat_subscription - use the "enable_content" option (when available) when
  registering using D-Bus, to ensure that subscription-manager enables the
  content on registration; this is particular important on EL 10+ and Fedora
  41+
  (https://github.com/ansible-collections/community.general/pull/9778).
- slack - fail if Slack API response is not OK with error message (https://github.com/ansible-collections/community.general/pull/9198).
- sudoers - display stdout and stderr raised while failed validation (https://github.com/ansible-collections/community.general/issues/9674, https://github.com/ansible-collections/community.general/pull/9871).
- xml - ensure file descriptor is closed (https://github.com/ansible-collections/community.general/pull/9695).
- zfs - fix handling of multi-line values of user-defined ZFS properties (https://github.com/ansible-collections/community.general/pull/6264).
- zfs_facts - parameter ``type`` now accepts multple values as documented (https://github.com/ansible-collections/community.general/issues/5909, https://github.com/ansible-collections/community.general/pull/9697).

community.library_inventory_filtering_v1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- inventory_filter plugin utils - make compatible with ansible-core's Data Tagging feature (https://github.com/ansible-collections/community.library_inventory_filtering/pull/24).
- inventory_plugin plugin util - ``parse_filters`` now filters ``None`` values with allowed keys (https://github.com/ansible-collections/community.library_inventory_filtering/pull/27).

community.libvirt
~~~~~~~~~~~~~~~~~

- libvirt_lxc - add configuration for libvirt_lxc_noseclabel.

community.mysql
~~~~~~~~~~~~~~~

- mysql_db - fix dump and import to find MariaDB binaries (mariadb and mariadb-dump) when MariaDB 11+ is used and symbolic links to MySQL binaries are absent.
- mysql_user,mysql_role - The sql_mode ANSI_QUOTES affects how the modules mysql_user and mysql_role compare the existing privileges with the configured privileges, as well as decide whether double quotes or backticks should be used in the GRANT statements. Pointing out in issue 671, the modules mysql_user and mysql_role allow users to enable/disable ANSI_QUOTES in session variable (within a DB session, the session variable always overwrites the global one). But due to the issue, the modules do not check for ANSI_MODE in the session variable, instead, they only check in the GLOBAL one.That behavior is not only limiting the users' flexibility, but also not allowing users to explicitly disable ANSI_MODE to work around such bugs like https://bugs.mysql.com/bug.php?id=115953. (https://github.com/ansible-collections/community.mysql/issues/671)

community.postgresql
~~~~~~~~~~~~~~~~~~~~

- postgresql_info - fix failure when a default database is used (neither ``db`` nor ``login_db`` are specified) (https://github.com/ansible-collections/community.postgresql/issues/794).
- postgresql_info - fix issue when gathering information fails if user doesn't have access to all databases (https://github.com/ansible-collections/community.postgresql/pull/788).
- postgresql_info - fix module failure when the ``db`` parameter is used instead of ``login_db`` (https://github.com/ansible-collections/community.postgresql/issues/794).
- postgresql_pg_hba - fixes #420 by properly handling hash-symbols in quotes (https://github.com/ansible-collections/community.postgresql/pull/766)
- postgresql_pg_hba - fixes #705 by preventing invalid strings to be written (https://github.com/ansible-collections/community.postgresql/pull/761)
- postgresql_pg_hba - fixes #730 by extending the key we use to identify a rule with the connection type (https://github.com/ansible-collections/community.postgresql/pull/770)
- postgresql_pg_hba - fixes #776 the module won't be adding/moving comments repeatedly if 'keep_comments_at_rules' is 'false' (https://github.com/ansible-collections/community.postgresql/pull/778)
- postgresql_pg_hba - fixes #777 the module will ignore the 'address' and 'netmask' options again when the contype is 'local' (https://github.com/ansible-collections/community.postgresql/pull/779)
- postgresql_pg_hba - improves parsing of quoted strings and escaped newlines (https://github.com/ansible-collections/community.postgresql/pull/761)
- postgresql_privs -  fix the error occurring when trying to grant a function execution and set the schema to not-specified (https://github.com/ansible-collections/community.postgresql/pull/783).
- postgresql_table - consider schema name when checking for table (https://github.com/ansible-collections/community.postgresql/issues/817).  Table names are only unique within a schema. This allows using the same table name in multiple schemas.
- postgresql_user - doesn't take password_encryption into account when checking if a password should be updated (https://github.com/ansible-collections/community.postgresql/issues/688).

community.rabbitmq
~~~~~~~~~~~~~~~~~~

- rabbitmq_publish - fix support for publishing headers as a part of a message (https://github.com/ansible-collections/community.rabbitmq/pull/182)

community.routeros
~~~~~~~~~~~~~~~~~~

- api_info, api_modify - fields ``log`` and ``log-prefix`` in paths ``ip firewall filter``, ``ip firewall mangle``, ``ip firewall nat``, ``ip firewall raw`` now have the correct default values (https://github.com/ansible-collections/community.routeros/pull/324).
- api_info, api_modify - remove the primary key ``action`` from the ``interface wifi provisioning`` path, since RouterOS also allows to create completely duplicate entries (https://github.com/ansible-collections/community.routeros/issues/344, https://github.com/ansible-collections/community.routeros/pull/345).

community.sops
~~~~~~~~~~~~~~

- install role - ``sops_install_on_localhost=false`` was not working properly if the role was running on more than one host due to a bug in ansible-core (https://github.com/ansible-collections/community.sops/issues/223, https://github.com/ansible-collections/community.sops/pull/224).
- install role - when used with Debian on ARM architecture, the architecture name is now correctly translated from ``aarch64`` to ``arm64`` (https://github.com/ansible-collections/community.sops/issues/220, https://github.com/ansible-collections/community.sops/pull/221).
- load_vars - make evaluation compatible with Data Tagging in upcoming ansible-core release (https://github.com/ansible-collections/community.sops/pull/225).

community.vmware
~~~~~~~~~~~~~~~~

- vm_device_helper - Fix 'invalid configuration for device' error caused by missing fileoperation parameter. (https://github.com/ansible-collections/community.vmware/pull/2009).
- vmware_guest - Fix errors occuring during hardware version upgrade not being reported. (https://github.com/ansible-collections/community.vmware/pull/2010).
- vmware_guest - Fix vmware_guest always reporting change when using dvswitch. (https://github.com/ansible-collections/community.vmware/pull/2000).
- vmware_guest - setting vApp properties on virtual machines without vApp options raised an AttributeError. Fix now gracefully handles a `None` value for vApp options when retrieving current vApp properties (https://github.com/ansible-collections/community.vmware/pull/2220).
- vmware_guest_tools_upgrade - Account for all possible tools status (https://github.com/ansible-collections/community.vmware/issues/2237).
- vmware_object_role_permission - The module ignores changing ``recursive`` (https://github.com/ansible-collections/community.vmware/pull/2350).

community.zabbix
~~~~~~~~~~~~~~~~

- Java Gateway Role - Temporary work around to solve failure on RHEL9.
- zabbix inventory plugin - do not require ``login_user`` and ``login_password`` to be present when ``auth_token`` is provided (https://github.com/ansible-collections/community.zabbix/pull/1439).
- zabbix_agent Role - Add Zabbix 7.0 LTS in supported versions for windows.
- zabbix_agent Role - Added ability to set the monitored_by and proxy_group values.
- zabbix_agent Role - Set become parameter explicitly to false for API tasks to run without sudo on the local computer.

containers.podman
~~~~~~~~~~~~~~~~~

- Don't pull image when state is absent or pull=never (#889)
- Fix idempotency for containers with env vars containing MAX_SIZE (#893)
- Fix list tags failure in podman_search (#875)
- Fix podman_container_copy examples (#882)
- docs(podman_container) - improve comments on network property (#878)

dellemc.enterprise_sonic
~~~~~~~~~~~~~~~~~~~~~~~~

- ConnectionError - Add the needed import of the Ansible ConnectionError exception class for all files where it was previously missing. (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/445).
- Update 'update_url' method to handle multiple interface names (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/455).
- Update regex search expression for 'not found' error message in httpapi/sonic.py 'edit_config' method (https://github.com/ansible-collection/dellemc.enterprise_sonic/pull/443).
- sonic_bgp_communities - Fix issues in merged state for standard community-lists (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/440).
- sonic_copp - Update reserved CoPP names list (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/481).
- sonic_interfaces - Remove the restriction preventing configuration of interface speed for port channel member interfaces (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/470).
- sonic_l3_interfaces - Eliminate unconditional sending of the new autoconf REST API option during replaced and overridden state handling (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/474).
- sonic_mclag - Delete any remaining PortChannel members for an mclag domain before attempting to delete the mclag domain (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/463).
- sonic_ospf_area - Fix OSPF area bug (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/466).
- sonic_qos_interfaces - Fix command deletion bug (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/473).
- sonic_qos_wred - Update QoS WRED regression test case based on SONiC code changes (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/465).
- sonic_stp - Change the criteria for converting vlans and vlan ranges to handle vlan IDs with more than one digit (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/460).
- sonic_stp - Fix functionality to allow a value of 0 to be configured for the appropriate integer attributes and refactor module code(https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/477).
- sonic_system - Catch the ConnectionError exception caused by unconditional fetching of auditd and ip loadshare hash algorithm configuration, and return empty configuration instead of allowing the uncaught exception to abort all "system" operations on SONiC images older than version 4.4.0 (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/441).
- sonic_vrrp - Update delete handling to fix regression failure (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/455).
- sonic_vxlan - Fix failing regression tests for sonic_vxlan (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/471).

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- Internal defect fixes were done for the following modules - ``idrac_network_attributes``, ``idrac_certificates``, ``idrac_redfish_storage_controller``, ``idrac_boot_order`` and ``idrac_firmware``
- Resolved the issue in ``idrac_redfish_storage_volume`` module where it returns 404 error on job creation when enabling encryption for virtual drives. (https://github.com/dell/dellemc-openmanage-ansible-modules/issues /713)
- idrac_certificates - (Issue 737) - Fixed SSL CSR generation for 4096 key size.

f5networks.f5_modules
~~~~~~~~~~~~~~~~~~~~~

- bigip_firewall_address_list to support both cidr and route domain
- bigip_monitor_external - external monitor user-defined variables not reflected for non-common partition
- bigip_profile_server_ssl - Fixed bug - create server SSL profile if SSL key is passphrase protected
- bigip_profile_server_ssl to support parent's [None, "", "None"] profiles
- bigip_snmp_community - Allow v3 usernames that begin with a number or contains any special characters.

fortinet.fortimanager
~~~~~~~~~~~~~~~~~~~~~

- Changed all input argument name in ansible built-in documentation to the underscore format. E.g., changed "var-name" to "var_name".
- Changed parameter type of some parameters.
- Changed the default playbook examples for each module to pass ansible-lint.
- Corrected mainkey of some modules.
- Fixed a bug where rc_failed and rc_succeeded did not work.
- Improved code logic, reduced redundant requests for system information.
- Modified built-in document to support sanity tests in ansible-core 2.18.0. No functionality changed.

fortinet.fortios
~~~~~~~~~~~~~~~~

- Fix errors in Ansible sanity test with Ansible-core 2.18
- Github
- Github Issue
- Mantis Issue

hetzner.hcloud
~~~~~~~~~~~~~~

- hcloud_load_balancer_service - Improve unknown certificate id or name error.
- hcloud_server - Only rebuild existing servers, skip rebuild if the server was just created.

ibm.storage_virtualize
~~~~~~~~~~~~~~~~~~~~~~

- ibm_svc_manage_flashcopy - Added support for creating flashcopy with existing target volume
- ibm_svc_manage_replication - Added checks for mutually-exclusive parameters and policing for updating remote-copy relationship

infoblox.nios_modules
~~~~~~~~~~~~~~~~~~~~~

- For Host IPv6, the mac parameter has been renamed to duid.
- Refined Host record return fields to ensure use_nextserver and nextserver are only included for IPv4, as these fields are not applicable to IPv6.

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

netapp.ontap
~~~~~~~~~~~~

- Resolved Ansible lint issues.
- all modules supporting REST - avoid duplicate calls to api/cluster to get ONTAP version.
- na_ontap_aggregate - fix issue with 'raid_type' change in REST.
- na_ontap_broadcast_domain - fix issue with port modification in REST.
- na_ontap_flexcache - fix typo error in the query 'origins.cluster.name' in REST.
- na_ontap_kerberos_interface - updated example in module documentation.
- na_ontap_qtree - fix timeout issue with qtree delete in REST.
- na_ontap_rest_info - rectified subset name to `cluster/firmware/history`.
- na_ontap_snapshot_policy - fix issue with 'retention_period' in REST.

netbox.netbox
~~~~~~~~~~~~~

- Fix missing netbox_config_template module in module_defaults
- Fixed an isssue with module_default parameter inheritance for modules netbox_config_template, netbox_custom_field_choice_set, netbox_permission, netbox_token, netbox_user, and netbox_user_group.
- fix call /api/status/ instead /api/status in nb_inventory plugin. (https://github.com/netbox-community/ansible_modules/issues/1335).
- netbox_ip_address - Fixed the problem preventing assignment of an IP address to a network interface

purestorage.flasharray
~~~~~~~~~~~~~~~~~~~~~~

- purefa_alert - Fix unreferenced variable error
- purefa_audits - Fix issue when ``start`` parameter not supplied
- purefa_dirsnap - Fixed issues with ``keep_for`` setting and issues related to recovery of deleted snapshots
- purefa_ds - Fixed issue with trying to create a pre-existing system-defined role
- purefa_dsrole - Fixed bug in role creation.
- purefa_dsrole - Fixed bug with DS role having no group or group base cannot be updated
- purefa_eradication - Fix incorrect timer settings
- purefa_hg - Fixed issue when ``check_mode = true`` not reporting correct status when adding new hosts to hostgroup.
- purefa_host - Fix issue with no VLAN provided when Purity//FA is a recent version.
- purefa_host - Fix issue with setting preferred_arrays for a host.
- purefa_info - Cater for zero used space in NFS offloads
- purefa_info - ``exports`` dict for each share changed to a list of dicts in ``filesystm`` subset
- purefa_inventory - Fixed quiet failures due to attribute errors
- purefa_network - Allow LACP bonds to be children of a VIF
- purefa_network - Fix compatability issue with ``netaddr>=1.2.0``
- purefa_ntp - Fix issue with deletion of NTP servers
- purefa_offload - Corrected version check logic
- purefa_pgsnap - Fixed issue with overwrite failing
- purefa_pod - Allow pd to be deleted with contents if ``delete_contents`` specified
- purefa_pod - Errored out when setting failover preference for pod
- purefa_ra - Fixed duration check logic
- purefa_sessions - Correctly report sessions with no start or end time
- purefa_smtp - Fixed SMTP deletion issue
- purefa_snmp - Fix issues with deleting SNMP entries
- purefa_snmp_agent - Fix issues with deleting v3 agent
- purefa_vg - Fixed idempotency issue when clearing volume group QoS settings
- purefa_vg - Fixed issue with creating non-QoS volume groups
- purefa_vlan - Allow LACP bonds to be subnet interfaces
- purefa_volume - Added error message to warn about moving protected volume
- purefa_volume - Errors out when pgroup and add_to_pgs used incorrectly
- purefa_volume - Fixed issue of unable to move volume from pod to vgroup
- purefa_volume - Fixes issue of moving protected volume into volume group

purestorage.flashblade
~~~~~~~~~~~~~~~~~~~~~~

- purefb_bucket - Fixed issue with idempotency reported when ``hard_limit`` not provided.
- purefb_info - Fixed ``AttributeError`` for ``snapshot`` subset when snapshot had been created manually, rather than using a snapshot policy
- purefb_info - Fixed issue with admin token creation time and bucket policies
- purefb_policy - Fixed syntax error is account name.
- purefb_smtp - Fix errors that occurred after adding support for smtp encrpytion and using the module on older FlashBlades.
- purefb_snap - Fixed issue where ``target`` incorrectly required for a regular snapshot

telekom_mms.icinga_director
~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Add Icinga notification template imports (https://github.com/telekom-mms/ansible-collection-icinga-director/pull/267)

theforeman.foreman
~~~~~~~~~~~~~~~~~~

- callback plugin - fix another exception when serializing secrets (https://github.com/theforeman/foreman-ansible-modules/pull/1819)
- inventory - Drop fallback to Host API when Reports API fails, as this leads to possibly wrong data being used

vmware.vmware
~~~~~~~~~~~~~

- client utils - Fixed error message when required library could not be imported
- content_library_item_info - Library name and ID are ignored if item ID is provided so updated docs and arg parse rules to reflect this
- folder - replaced non-existent 'storage' type with 'datastore' type
- module_deploy_vm_base - fix attribute error when deploying to a resource pool
- vms inventory - fix handling of VMs within VApps

vmware.vmware_rest
~~~~~~~~~~~~~~~~~~

- lookup plugins - Fixed issue where datacenter search filter was never properly set
- module_utils - fixed return value for vmware.vmware_rest.vcenter_vm_guest_filesystem_directories module
- vcenter_ovf_libraryitem - Update documentation to mention the metadata cannot be updated via conventional means. Added example showing workaround (https://github.com/ansible-collections/vmware.vmware_rest/issues/385)

Known Issues
------------

Ansible-core
~~~~~~~~~~~~

- templating - Any string value starting with ``#jinja2:`` which is templated will always be interpreted as Jinja2 configuration overrides. To include this literal value at the start of a string, a space or other character must precede it.
- variables - Tagged values cannot be used for dictionary keys in many circumstances.
- variables - The values ``None``, ``True`` and ``False`` cannot be tagged because they are singletons. Attempts to apply tags to these values will be silently ignored.

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- idrac_diagnostics - Issue(285322) - This module doesn't support export of diagnostics file to HTTP and HTTPS share via SOCKS proxy.
- idrac_firmware - Issue(279282) - This module does not support firmware update using HTTP, HTTPS, and FTP shares with authentication on iDRAC8.
- ome_smart_fabric_uplink - Issue(186024) - The module supported by OpenManage Enterprise Modular, however it does not allow the creation of multiple uplinks of the same name. If an uplink is created using the same name as an existing uplink, then the existing uplink is modified.

purestorage.flasharray
~~~~~~~~~~~~~~~~~~~~~~

- All Fusion fleet members will be assumed to be at the same Purity//FA version level as the array connected to by Ansible.
- FlashArray//CBS is not currently supported as a member of a Fusion fleet

New Plugins
-----------

Connection
~~~~~~~~~~

- community.general.proxmox_pct_remote - Run tasks in Proxmox LXC container instances using pct CLI via SSH.

Filter
~~~~~~

- community.dns.reverse_pointer - Convert an IP address into a DNS name for reverse lookup.
- community.general.accumulate - Produce a list of accumulated sums of the input list contents.
- community.general.json_diff - Create a JSON patch by comparing two JSON files.
- community.general.json_patch - Apply a JSON-Patch (RFC 6902) operation to an object.
- community.general.json_patch_recipe - Apply JSON-Patch (RFC 6902) operations to an object.
- microsoft.ad.split_dn - Splits an LDAP DistinguishedName.

Inventory
~~~~~~~~~

- community.general.iocage - iocage inventory source.

Lookup
~~~~~~

- community.dns.reverse_lookup - Reverse-look up IP addresses.
- community.general.onepassword_ssh_key - Fetch SSH keys stored in 1Password.
- infoblox.nios_modules.nios_next_vlan_id - Return the next available VLAN ID

New Modules
-----------

amazon.aws
~~~~~~~~~~

- amazon.aws.ec2_dedicated_host - Create, update or delete (release) EC2 dedicated host
- amazon.aws.ec2_dedicated_host_info - Gather information about EC2 Dedicated Hosts in AWS
- amazon.aws.rds_instance_param_group_info - Describes the RDS parameter group.
- amazon.aws.route53_key_signing_key - Manages a key-signing key (KSK)

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

check_point.mgmt
~~~~~~~~~~~~~~~~

- check_point.mgmt.cp_mgmt_user - Manages user objects on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_user_facts - Get user objects facts on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_user_template - Manages user-template objects on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_user_template_facts - Get user-template objects facts on Checkpoint over Web Services API

cisco.ios
~~~~~~~~~

- cisco.ios.ios_evpn_ethernet - Resource module to configure L2VPN EVPN Ethernet Segment.

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

community.docker
~~~~~~~~~~~~~~~~

- community.docker.docker_context_info - Retrieve information on Docker contexts for the current user.

community.general
~~~~~~~~~~~~~~~~~

- community.general.android_sdk - Manages Android SDK packages.
- community.general.decompress - Decompresses compressed files.
- community.general.ldap_inc - Use the Modify-Increment LDAP V3 feature to increment an attribute value.
- community.general.pacemaker_resource - Manage pacemaker resources.
- community.general.proxmox_backup - Start a VM backup in Proxmox VE cluster.
- community.general.proxmox_backup_info - Retrieve information on Proxmox scheduled backups.
- community.general.systemd_creds_decrypt - C(systemd)'s C(systemd-creds decrypt) plugin.
- community.general.systemd_creds_encrypt - C(systemd)'s C(systemd-creds encrypt) plugin.
- community.general.systemd_info - Gather C(systemd) unit info.

community.hrobot
~~~~~~~~~~~~~~~~

- community.hrobot.reset_info - Query information on the resetter of a dedicated server.
- community.hrobot.storagebox - Modify a storage box's basic configuration.
- community.hrobot.storagebox_info - Query information on one or more storage boxes.
- community.hrobot.storagebox_set_password - (Re)set the password for a storage box.
- community.hrobot.storagebox_snapshot_plan - Modify a storage box's snapshot plans.
- community.hrobot.storagebox_snapshot_plan_info - Query the snapshot plans for a storage box.

community.postgresql
~~~~~~~~~~~~~~~~~~~~

- community.postgresql.postgresql_alter_system - Change a PostgreSQL server configuration parameter

community.vmware
~~~~~~~~~~~~~~~~

- community.vmware.vmware_drs_override - Configure DRS behavior for a specific VM in vSphere

community.zabbix
~~~~~~~~~~~~~~~~

- community.zabbix.zabbix_connector - Create/Delete/Update Zabbix connectors
- community.zabbix.zabbix_regexp_info - Retrieve Zabbix regular expression

dellemc.enterprise_sonic
~~~~~~~~~~~~~~~~~~~~~~~~

- dellemc.enterprise_sonic.sonic_ssh - Manage SSH configurations on SONiC.

dellemc.powerflex
~~~~~~~~~~~~~~~~~

- dellemc.powerflex.nvme_host - Manage NVMe Hosts on Dell PowerFlex
- dellemc.powerflex.sdt - Manage SDTs on Dell PowerFlex

fortinet.fortimanager
~~~~~~~~~~~~~~~~~~~~~

- fortinet.fortimanager.fmgr_gtp_ieallowlist - IE allow list.
- fortinet.fortimanager.fmgr_gtp_ieallowlist_entries - Entries of allow list for unknown or out-of-state IEs.
- fortinet.fortimanager.fmgr_pkg_videofilter_youtubekey - Configure YouTube API keys.
- fortinet.fortimanager.fmgr_ums_setting - Ums setting

ibm.storage_virtualize
~~~~~~~~~~~~~~~~~~~~~~

- ibm.storage_virtualize.ibm_sv_manage_flashsystem_grid - Manages operations of Flashsystem grid containing multiple Storage Virtualize systems

infoblox.nios_modules
~~~~~~~~~~~~~~~~~~~~~

- infoblox.nios_modules.nios_adminuser - Configure Infoblox NIOS Admin Users
- infoblox.nios_modules.nios_vlan - Configure Infoblox NIOS VLANs

kubernetes.core
~~~~~~~~~~~~~~~

- kubernetes.core.helm_registry_auth - Helm registry authentication module

lowlydba.sqlserver
~~~~~~~~~~~~~~~~~~

- lowlydba.sqlserver.login_role - Configures a login's  server roles.
- lowlydba.sqlserver.user_role - Configures a user's role in a database.

netapp.ontap
~~~~~~~~~~~~

- netapp.ontap.na_ontap_bgp_config - NetApp ONTAP network BGP configuration
- netapp.ontap.na_ontap_cifs_privileges - NetApp ONTAP CIFS privileges

netapp.storagegrid
~~~~~~~~~~~~~~~~~~

- netapp.storagegrid.na_sg_grid_ec_profile - Manage EC profiles on StorageGRID.
- netapp.storagegrid.na_sg_grid_ilm_policy - Manage ILM policies on StorageGRID.
- netapp.storagegrid.na_sg_grid_ilm_policy_tag - Manage ILM policy tags on StorageGRID.
- netapp.storagegrid.na_sg_grid_ilm_pool - Manage ILM pools on StorageGRID.
- netapp.storagegrid.na_sg_grid_ilm_rule - Manage ILM rules on StorageGRID.

netbox.netbox
~~~~~~~~~~~~~

- netbox.netbox.netbox_mac_address - Create, update or delete MAC addresses within NetBox

purestorage.flasharray
~~~~~~~~~~~~~~~~~~~~~~

- purestorage.flasharray.purefa_fleet - Manage Fusion Fleet
- purestorage.flasharray.purefa_realm - Manage realms on Pure Storage FlashArrays

Unchanged Collections
---------------------

- ansible.utils (still version 5.1.2)
- awx.awx (still version 24.6.1)
- chocolatey.chocolatey (still version 1.5.3)
- cisco.aci (still version 2.10.1)
- cisco.intersight (still version 2.0.20)
- cisco.mso (still version 2.9.0)
- cloud.common (still version 4.0.0)
- community.digitalocean (still version 1.27.0)
- community.grafana (still version 2.1.0)
- community.hashi_vault (still version 6.2.0)
- community.proxysql (still version 1.6.0)
- community.sap_libs (still version 1.4.2)
- dellemc.unity (still version 2.0.0)
- ibm.qradar (still version 4.0.0)
- ieisystem.inmanage (still version 3.0.0)
- infinidat.infinibox (still version 1.4.5)
- inspur.ispim (still version 2.2.3)
- kaytus.ksmanage (still version 2.0.0)
- kubevirt.core (still version 2.1.0)
- netapp.cloudmanager (still version 21.24.0)
- netapp_eseries.santricity (still version 1.4.1)
- ngine_io.cloudstack (still version 2.5.0)
- ovirt.ovirt (still version 3.2.0)
- splunk.es (still version 4.0.0)
- vultr.cloud (still version 1.13.0)
- vyos.vyos (still version 5.0.0)
- wti.remote (still version 1.0.10)
