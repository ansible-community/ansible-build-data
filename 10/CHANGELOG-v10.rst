========================
Ansible 10 Release Notes
========================

This changelog describes changes since Ansible 9.0.0.

.. contents::
  :depth: 2

v10.7.0
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

Ansible 10.7.0 contains ansible-core version 2.17.7.
This is a newer version than version 2.17.6 contained in the previous Ansible release.

The changes are reported in the combined changelog below.

Changed Collections
-------------------

If not mentioned explicitly, the changes are reported in the combined changelog below.

+-----------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| Collection                  | Ansible 10.6.0 | Ansible 10.7.0 | Notes                                                                                                                        |
+=============================+================+================+==============================================================================================================================+
| cisco.dnac                  | 6.22.0         | 6.25.0         |                                                                                                                              |
+-----------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.ise                   | 2.9.5          | 2.9.6          |                                                                                                                              |
+-----------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.dns               | 3.0.6          | 3.1.0          |                                                                                                                              |
+-----------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.docker            | 3.13.1         | 3.13.3         |                                                                                                                              |
+-----------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.general           | 9.5.1          | 9.5.2          |                                                                                                                              |
+-----------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.mysql             | 3.10.3         | 3.11.0         |                                                                                                                              |
+-----------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.postgresql        | 3.7.0          | 3.9.0          |                                                                                                                              |
+-----------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.vmware            | 4.8.0          | 4.8.1          |                                                                                                                              |
+-----------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| cyberark.pas                | 1.0.27         | 1.0.30         | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+-----------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| dellemc.openmanage          | 9.8.0          | 9.9.0          |                                                                                                                              |
+-----------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| fortinet.fortimanager       | 2.7.0          | 2.8.2          |                                                                                                                              |
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

Major Changes
-------------

- The removal of netapp.storagegrid was cancelled. The collection will not be removed from Ansible 11 (`https://forum.ansible.com/t/2811 <https://forum.ansible.com/t/2811>`__).
  Maintenance of the collection has been taken over by another team at NetApp.

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- omevv_baseline_profile - This module allows to manage baseline profile.
- omevv_baseline_profile_info - This module allows to retrieve baseline profile information.
- omevv_compliance_info - This module allows to retrieve firmware compliance reports.

Minor Changes
-------------

Ansible-core
~~~~~~~~~~~~

- remove extraneous selinux import (https://github.com/ansible/ansible/issues/83657).

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

community.general
~~~~~~~~~~~~~~~~~

- proxmox inventory plugin - fix urllib3 ``InsecureRequestWarnings`` not being suppressed when a token is used (https://github.com/ansible-collections/community.general/pull/9099).

community.mysql
~~~~~~~~~~~~~~~

- mysql_info - adds the count of tables for each database to the returned values. It is possible to exclude this new field using the ``db_table_count`` exclusion filter. (https://github.com/ansible-collections/community.mysql/pull/691)

community.postgresql
~~~~~~~~~~~~~~~~~~~~

- postgresql_pg_hba - changes ordering of entries that are identical except for the ip-range, but only if the ranges are of the same size, this isn't breaking as ranges of equal size can't overlap (https://github.com/ansible-collections/community.postgresql/pull/772)
- postgresql_pg_hba - orders auth-options alphabetically, this isn't breaking as the order of those options is not relevant to postgresql (https://github.com/ansible-collections/community.postgresql/pull/772)
- postgresql_pg_hba - show the number of the line with the issue if parsing a file fails (https://github.com/ansible-collections/community.postgresql/pull/766)
- postgresql_publication - add possibility of creating publication with column list (https://github.com/ansible-collections/community.postgresql/pull/763).

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

cisco.ise
~~~~~~~~~

- network_device - Fix mask validation to handle None values in NetworkDeviceIPList

community.dns
~~~~~~~~~~~~~

- Update Public Suffix List.

community.docker
~~~~~~~~~~~~~~~~

- docker_compose_v2_exec, docker_compose_v2_run - fix missing ``--env`` flag while assembling env arguments (https://github.com/ansible-collections/community.docker/pull/992).
- docker_compose_v2_run - make sure to sanitize ``labels`` before sending them to the Docker Daemon (https://github.com/ansible-collections/community.docker/pull/985).
- docker_config - make sure to sanitize ``labels`` before sending them to the Docker Daemon (https://github.com/ansible-collections/community.docker/pull/985).
- docker_host_info - ensure that the module always returns ``can_talk_to_docker``, and that it provides the correct value even if ``api_version`` is specified (https://github.com/ansible-collections/community.docker/issues/993, https://github.com/ansible-collections/community.docker/pull/995).
- docker_network - make sure to sanitize ``labels`` before sending them to the Docker Daemon (https://github.com/ansible-collections/community.docker/pull/985).
- docker_node - make sure to sanitize ``labels`` before sending them to the Docker Daemon (https://github.com/ansible-collections/community.docker/pull/985).
- docker_secret - make sure to sanitize ``labels`` before sending them to the Docker Daemon (https://github.com/ansible-collections/community.docker/pull/985).
- docker_swarm - make sure to sanitize ``labels`` before sending them to the Docker Daemon (https://github.com/ansible-collections/community.docker/pull/985).
- docker_swarm_service - make sure to sanitize ``labels`` and ``container_labels`` before sending them to the Docker Daemon (https://github.com/ansible-collections/community.docker/pull/985).
- docker_volume - make sure to sanitize ``labels`` before sending them to the Docker Daemon (https://github.com/ansible-collections/community.docker/pull/985).

community.general
~~~~~~~~~~~~~~~~~

- dnf_config_manager - fix hanging when prompting to import GPG keys (https://github.com/ansible-collections/community.general/pull/9124, https://github.com/ansible-collections/community.general/issues/8830).
- dnf_config_manager - forces locale to ``C`` before module starts. If the locale was set to non-English, the output of the ``dnf config-manager`` could not be parsed (https://github.com/ansible-collections/community.general/pull/9157, https://github.com/ansible-collections/community.general/issues/9046).
- flatpak - force the locale language to ``C`` when running the flatpak command (https://github.com/ansible-collections/community.general/pull/9187, https://github.com/ansible-collections/community.general/issues/8883).
- github_key - in check mode, a faulty call to ```datetime.strftime(...)``` was being made which generated an exception (https://github.com/ansible-collections/community.general/issues/9185).
- homebrew_cask - allow ``+`` symbol in Homebrew cask name validation regex (https://github.com/ansible-collections/community.general/pull/9128).
- keycloak_client - fix diff by removing code that turns the attributes dict which contains additional settings into a list (https://github.com/ansible-collections/community.general/pull/9077).
- keycloak_clientscope - fix diff and ``end_state`` by removing the code that turns the attributes dict, which contains additional config items, into a list (https://github.com/ansible-collections/community.general/pull/9082).
- keycloak_clientscope_type - sort the default and optional clientscope lists to improve the diff (https://github.com/ansible-collections/community.general/pull/9202).
- redfish_utils module utils - remove undocumented default applytime (https://github.com/ansible-collections/community.general/pull/9114).
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

community.vmware
~~~~~~~~~~~~~~~~

- vm_device_helper - Fix 'invalid configuration for device' error caused by missing fileoperation parameter. (https://github.com/ansible-collections/community.vmware/pull/2009).
- vmware_guest - Fix errors occuring during hardware version upgrade not being reported. (https://github.com/ansible-collections/community.vmware/pull/2010).
- vmware_guest - Fix vmware_guest always reporting change when using dvswitch. (https://github.com/ansible-collections/community.vmware/pull/2000).

fortinet.fortimanager
~~~~~~~~~~~~~~~~~~~~~

- Changed all input argument name in ansible built-in documentation to the underscore format. E.g., changed "var-name" to "var_name".
- Fixed a bug where rc_failed and rc_succeeded did not work.
- Improved code logic, reduced redundant requests for system information.
- Modified built-in document to support sanity tests in ansible-core 2.18.0. No functionality changed.

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

Lookup
~~~~~~

- community.dns.reverse_lookup - Reverse-look up IP addresses.

New Modules
-----------

fortinet.fortimanager
~~~~~~~~~~~~~~~~~~~~~

- fortinet.fortimanager.fmgr_pkg_videofilter_youtubekey - Configure YouTube API keys.

netapp.ontap
~~~~~~~~~~~~

- netapp.ontap.na_ontap_bgp_config - NetApp ONTAP network BGP configuration
- netapp.ontap.na_ontap_cifs_privileges - NetApp ONTAP CIFS privileges

Unchanged Collections
---------------------

- amazon.aws (still version 8.2.1)
- ansible.netcommon (still version 6.1.3)
- ansible.posix (still version 1.6.2)
- ansible.utils (still version 4.1.0)
- ansible.windows (still version 2.5.0)
- arista.eos (still version 9.0.0)
- awx.awx (still version 24.6.1)
- azure.azcollection (still version 2.7.0)
- check_point.mgmt (still version 5.2.3)
- chocolatey.chocolatey (still version 1.5.3)
- cisco.aci (still version 2.10.1)
- cisco.asa (still version 5.0.1)
- cisco.intersight (still version 2.0.20)
- cisco.ios (still version 8.0.0)
- cisco.iosxr (still version 9.0.0)
- cisco.meraki (still version 2.18.3)
- cisco.mso (still version 2.9.0)
- cisco.nxos (still version 8.1.0)
- cisco.ucs (still version 1.14.0)
- cloud.common (still version 3.0.0)
- cloudscale_ch.cloud (still version 2.4.0)
- community.aws (still version 8.0.0)
- community.ciscosmb (still version 1.0.9)
- community.crypto (still version 2.22.3)
- community.digitalocean (still version 1.27.0)
- community.grafana (still version 1.9.1)
- community.hashi_vault (still version 6.2.0)
- community.hrobot (still version 2.0.2)
- community.library_inventory_filtering_v1 (still version 1.0.2)
- community.libvirt (still version 1.3.0)
- community.mongodb (still version 1.7.8)
- community.network (still version 5.1.0)
- community.okd (still version 3.0.1)
- community.proxysql (still version 1.6.0)
- community.rabbitmq (still version 1.3.0)
- community.routeros (still version 2.20.0)
- community.sap_libs (still version 1.4.2)
- community.sops (still version 1.9.1)
- community.windows (still version 2.3.0)
- community.zabbix (still version 2.5.1)
- containers.podman (still version 1.16.2)
- cyberark.conjur (still version 1.3.1)
- dellemc.enterprise_sonic (still version 2.5.1)
- dellemc.powerflex (still version 2.5.0)
- dellemc.unity (still version 2.0.0)
- f5networks.f5_modules (still version 1.32.1)
- fortinet.fortios (still version 2.3.8)
- frr.frr (still version 2.0.2)
- google.cloud (still version 1.4.1)
- grafana.grafana (still version 5.6.0)
- hetzner.hcloud (still version 3.1.1)
- ibm.qradar (still version 3.0.0)
- ibm.spectrum_virtualize (still version 2.0.0)
- ibm.storage_virtualize (still version 2.5.0)
- ieisystem.inmanage (still version 2.0.0)
- infinidat.infinibox (still version 1.4.5)
- inspur.ispim (still version 2.2.3)
- inspur.sm (still version 2.3.0)
- junipernetworks.junos (still version 8.0.0)
- kaytus.ksmanage (still version 1.2.2)
- kubernetes.core (still version 3.2.0)
- kubevirt.core (still version 1.5.0)
- lowlydba.sqlserver (still version 2.3.4)
- microsoft.ad (still version 1.7.1)
- netapp.cloudmanager (still version 21.24.0)
- netapp.storagegrid (still version 21.13.0)
- netapp_eseries.santricity (still version 1.4.1)
- netbox.netbox (still version 3.20.0)
- ngine_io.cloudstack (still version 2.5.0)
- ngine_io.exoscale (still version 1.1.0)
- openvswitch.openvswitch (still version 2.1.1)
- ovirt.ovirt (still version 3.2.0)
- purestorage.flashblade (still version 1.19.1)
- sensu.sensu_go (still version 1.14.0)
- splunk.es (still version 3.0.0)
- t_systems_mms.icinga_director (still version 2.0.1)
- theforeman.foreman (still version 4.2.0)
- vmware.vmware_rest (still version 3.2.0)
- vultr.cloud (still version 1.13.0)
- vyos.vyos (still version 4.1.0)
- wti.remote (still version 1.0.10)

v10.6.0
=======

.. contents::
  :local:
  :depth: 2

Release Summary
---------------

Release Date: 2024-11-05

`Porting Guide <https://docs.ansible.com/ansible/devel/porting_guides.html>`_

Ansible-core
------------

Ansible 10.6.0 contains ansible-core version 2.17.6.
This is a newer version than version 2.17.5 contained in the previous Ansible release.

The changes are reported in the combined changelog below.

Changed Collections
-------------------

If not mentioned explicitly, the changes are reported in the combined changelog below.

+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Collection                               | Ansible 10.5.0 | Ansible 10.6.0 | Notes                                                                                                                                                                                                           |
+==========================================+================+================+=================================================================================================================================================================================================================+
| ansible.posix                            | 1.5.4          | 1.6.2          |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cisco.dnac                               | 6.20.0         | 6.22.0         |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cisco.ise                                | 2.9.3          | 2.9.5          |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cisco.meraki                             | 2.18.2         | 2.18.3         |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.crypto                         | 2.22.1         | 2.22.3         |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.dns                            | 3.0.5          | 3.0.6          |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.docker                         | 3.13.0         | 3.13.1         |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.general                        | 9.5.0          | 9.5.1          |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.library_inventory_filtering_v1 | 1.0.1          | 1.0.2          |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.mongodb                        | 1.7.7          | 1.7.8          | There are no changes recorded in the changelog.                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.network                        | 5.0.3          | 5.1.0          |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.postgresql                     | 3.6.1          | 3.7.0          |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.routeros                       | 2.19.0         | 2.20.0         |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.vmware                         | 4.7.1          | 4.8.0          |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| containers.podman                        | 1.16.1         | 1.16.2         |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cyberark.conjur                          | 1.3.0          | 1.3.1          | You can find the collection's changelog at `https://github.com/cyberark/ansible-conjur-collection/blob/master/CHANGELOG.md <https://github.com/cyberark/ansible-conjur-collection/blob/master/CHANGELOG.md>`__. |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| dellemc.openmanage                       | 9.7.0          | 9.8.0          |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| f5networks.f5_modules                    | 1.31.0         | 1.32.1         |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| fortinet.fortios                         | 2.3.7          | 2.3.8          |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| grafana.grafana                          | 5.5.1          | 5.6.0          |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| netapp.cloudmanager                      | 21.22.1        | 21.24.0        |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| netapp.storagegrid                       | 21.12.0        | 21.13.0        | There are no changes recorded in the changelog.                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| purestorage.flashblade                   | 1.18.0         | 1.19.1         |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| telekom_mms.icinga_director              | 2.1.2          | 2.2.0          |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| vmware.vmware                            | 1.5.0          | 1.6.0          |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Major Changes
-------------

ansible.posix
~~~~~~~~~~~~~

- Dropping support for Ansible 2.9, ansible-core 2.15 will be minimum required version for this release

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- omevv_firmware_repository_profile - This module allows to manage firmware repository profile.
- omevv_firmware_repository_profile_info - This module allows to retrieve firmware repository profile information.
- omevv_vcenter_info - This module allows to retrieve vCenter information.

fortinet.fortios
~~~~~~~~~~~~~~~~

- Improve the logic for SET function to send GET request first then PUT or POST
- Mantis
- Support new FOS versions 7.6.0.

grafana.grafana
~~~~~~~~~~~~~~~

- Adding "distributor" section support to mimir config file by @HamzaKhait in https://github.com/grafana/grafana-ansible-collection/pull/247
- Allow alloy_user_groups variable again by @pjezek in https://github.com/grafana/grafana-ansible-collection/pull/276
- Alloy Role Improvements by @voidquark in https://github.com/grafana/grafana-ansible-collection/pull/281
- Bump ansible-lint from 24.6.0 to 24.9.2 by @dependabot in https://github.com/grafana/grafana-ansible-collection/pull/270
- Bump pylint from 3.2.5 to 3.3.1 by @dependabot in https://github.com/grafana/grafana-ansible-collection/pull/273
- Ensure check-mode works for otel collector by @pieterlexis-tomtom in https://github.com/grafana/grafana-ansible-collection/pull/264
- Fix message argument of dashboard task by @Nemental in https://github.com/grafana/grafana-ansible-collection/pull/256
- Update Alloy variables to use the `grafana_alloy_` namespace so they are unique by @Aethylred in https://github.com/grafana/grafana-ansible-collection/pull/209
- Update README.md by @aioue in https://github.com/grafana/grafana-ansible-collection/pull/272
- Update README.md by @aioue in https://github.com/grafana/grafana-ansible-collection/pull/275
- Update main.yml by @aioue in https://github.com/grafana/grafana-ansible-collection/pull/274
- add grafana_plugins_ops to defaults and docs by @weakcamel in https://github.com/grafana/grafana-ansible-collection/pull/251
- add option to populate google_analytics_4_id value by @copolycube in https://github.com/grafana/grafana-ansible-collection/pull/249
- fix ansible-lint warnings on Forbidden implicit octal value "0640" by @copolycube in https://github.com/grafana/grafana-ansible-collection/pull/279

Minor Changes
-------------

Ansible-core
~~~~~~~~~~~~

- ansible-test - Improve container runtime probe error handling. When unexpected probe output is encountered, an error with more useful debugging information is provided.

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

cisco.dnac
~~~~~~~~~~

- Added 'lan_automation_workflow_manager' to automate network discovery, deployment, and device configuration with LAN Automation.
- Added 'sda_extranet_policies_workflow_manager' to manage SDA Extranet Policies.
- Added 'sda_fabric_devices_workflow_manager' to manage SDA fabric devices.
- Added 'sda_fabric_virtual_networks_workflow_manager' to configure fabric VLANs, Virtual Networks, and Anycast Gateways.
- Added 'sda_host_port_onboarding_workflow_manager' to manage host port onboarding in SD-Access Fabric.
- Ansible utils requirement updated.
- Bug fixes in accesspoint_workflow_manager module
- Bug fixes in network_settings_workflow_manager module
- Bug fixes in pnp_workflow_manager module
- Changes in accesspoint_workflow_manager module.
- Changes in device_configs_backup_workflow_manager module
- Changes in device_credential_workflow_manager module.
- Changes in dnac.py
- Changes in dnac.py to support common APIs
- Changes in events_and_notifications_workflow_manager module.
- Changes in inventory_workflow_manager module.
- Changes in ise_radius_integration_workflow_manager module.
- Changes in sda_fabric_transits_workflow_manager module.
- Changes in user_role_workflow_manager module.
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
- accesspoint_workflow_manager.py - added attribute 'factory_reset_aps'.
- device_credential_workflow_manager.py - added attribute 'apply_credentials_to_site'.
- inventory_workflow_manager.py - Removed attribute hostname_list, serial_number_list and mac_address_list
- inventory_workflow_manager.py - added attribute hostnames, serial_numbers and mac_addresses

community.general
~~~~~~~~~~~~~~~~~

- redfish_utils module utils - schedule a BIOS configuration job at next reboot when the BIOS config is changed (https://github.com/ansible-collections/community.general/pull/9012).

community.postgresql
~~~~~~~~~~~~~~~~~~~~

- postgresql_set - adds the ``queries`` return value to return executed DML statements.

community.routeros
~~~~~~~~~~~~~~~~~~

- api_info, api_modify - add new parameters from the RouterOS 7.16 release (https://github.com/ansible-collections/community.routeros/pull/323).
- api_info, api_modify - add support ``interface l2tp-client`` configuration (https://github.com/ansible-collections/community.routeros/pull/322).
- api_info, api_modify - add support for the ``cpu-frequency``, ``memory-frequency``, ``preboot-etherboot`` and ``preboot-etherboot-server`` properties in ``system routerboard settings`` (https://github.com/ansible-collections/community.routeros/pull/320).
- api_info, api_modify - add support for the ``matching-type`` property in ``ip dhcp-server matcher`` introduced by RouterOS 7.16 (https://github.com/ansible-collections/community.routeros/pull/321).

community.vmware
~~~~~~~~~~~~~~~~

- vmware_vm_info - Improve performance when parsing custom attributes information (https://github.com/ansible-collections/community.vmware/pull/2194)

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- idrac_firmware_info - This module is enhanced to support iDRAC10 and OMSDK dependency is removed.

f5networks.f5_modules
~~~~~~~~~~~~~~~~~~~~~

- bigip_gtm_server - Added check for datacenter existence in Check Mode.

netapp.cloudmanager
~~~~~~~~~~~~~~~~~~~

- na_cloudmanager_cvo_aws - increase timeout for creating cvo to 90 mins.
- na_cloudmanager_cvo_azure - increase timeout for creating cvo to 90 mins.
- na_cloudmanager_cvo_gcp - increase timeout for creating cvo to 90 mins.

purestorage.flashblade
~~~~~~~~~~~~~~~~~~~~~~

- multiple - YAML lint fixes based on updated ``ansible-lint`` version
- purefb_bucket - Allow bucket quotas to be modified.
- purefb_info - Add ``time_remaining_status`` to bucket information from REST 2.14
- purefb_info - Expose SMTP encryption mode
- purefb_policy - Add new policy type of ``worm`` which is availble from Purity//FB 4.5.0
- purefb_smtp - Add encryption mode support from Purity//FB 4.5.0
- purefb_snap - Change ``targets`` to ``target` and from ``list`` to ``str``. ``targets`` added as alias and code to ensure existing list in playbooks is translated as a string.
- purefb_syslog - Enable ``services`` parameter and also the ability update existing syslog servers from REST 2.14

telekom_mms.icinga_director
~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Add vars parameter to user_template and user modules (https://github.com/telekom-mms/ansible-collection-icinga-director/pull/262)

vmware.vmware
~~~~~~~~~~~~~

- cluster_dpm - Migrated module from community.vmware to configure DPM in a vCenter cluster
- cluster_drs_recommendations - Migrated module from community.vmware to apply any DRS recommendations the vCenter cluster may have

Deprecated Features
-------------------

- The ``community.network`` collection has been deprecated.
  It will be removed from Ansible 12 if no one starts maintaining it again before Ansible 12.
  See `Collections Removal Process for unmaintained collections <https://docs.ansible.com/ansible/devel/community/collection_contributors/collection_package_removal.html#unmaintained-collections>`__ for more details (`https://forum.ansible.com/t/8030 <https://forum.ansible.com/t/8030>`__).
- The google.cloud collection will be removed from Ansible 12 due to violations of the Ansible inclusion requirements.
  The collection has \ `unresolved sanity test failures <https://github.com/ansible-collections/google.cloud/issues/613>`__.
  See `Collections Removal Process for collections not satisfying the collection requirements <https://docs.ansible.com/ansible/devel/community/collection_contributors/collection_package_removal.html#collections-not-satisfying-the-collection-requirements>`__ for more details, including for how this can be cancelled (`https://forum.ansible.com/t/8609 <https://forum.ansible.com/t/8609>`__).
  After removal, users can still install this collection with ``ansible-galaxy collection install google.cloud``.

community.network
~~~~~~~~~~~~~~~~~

- This collection and all content in it is unmaintained and deprecated (https://forum.ansible.com/t/8030). If you are interested in maintaining parts of the collection, please copy them to your own repository, and tell others about in the Forum discussion. See the `collection creator path <https://docs.ansible.com/ansible/devel/dev_guide/developing_collections_path.html>`__ for details.

community.vmware
~~~~~~~~~~~~~~~~

- vmware_cluster_dpm - the module has been deprecated and will be removed in community.vmware 6.0.0 (https://github.com/ansible-collections/community.vmware/pull/2217).
- vmware_cluster_drs_recommendations - the module has been deprecated and will be removed in community.vmware 6.0.0 (https://github.com/ansible-collections/community.vmware/pull/2218).

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

- Fix disabling SSL verification when installing collections and roles from git repositories. If ``--ignore-certs`` isn't provided, the value for the ``GALAXY_IGNORE_CERTS`` configuration option will be used (https://github.com/ansible/ansible/issues/83326).
- Improve performance on large inventories by reducing the number of implicit meta tasks.
- Use the requested error message in the ansible.module_utils.facts.timeout timeout function instead of hardcoding one.
- ansible-test - Enable the ``sys.unraisablehook`` work-around for the ``pylint`` sanity test on Python 3.11. Previously the work-around was only enabled for Python 3.12 and later. However, the same issue has been discovered on Python 3.11.
- debconf - set empty password values (https://github.com/ansible/ansible/issues/83214).
- facts - skip if distribution file path is directory, instead of raising error (https://github.com/ansible/ansible/issues/84006).
- user action will now require O(force) to overwrite the public part of an ssh key when generating ssh keys, as was already the case for the private part.
- user module now avoids changing ownership of files symlinked in provided home dir skeleton

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

cisco.ise
~~~~~~~~~

- Collection not compatible with ansible.utils 5.x.y
- Getting deployment info for entire deployment does not work
- cisco.ise.pan_ha object has no attribute 'enable_pan_ha'
- cisco.ise.support_bundle_download keeps failing after downloading the file

cisco.meraki
~~~~~~~~~~~~

- Ansible utils requirements updated.
- cisco.meraki.networks_clients_info - incorrect API endpoint, fixing info module.
- cisco.meraki.networks_switch_stacks delete stack not working, fixing path parameters.

community.crypto
~~~~~~~~~~~~~~~~

- acme_* modules - when using the OpenSSL backend, explicitly use the UTC timezone in Python code (https://github.com/ansible-collections/community.crypto/pull/811).
- acme_certificate - fix authorization failure when CSR contains SANs with mixed case (https://github.com/ansible-collections/community.crypto/pull/803).
- time module utils - fix conversion of naive ``datetime`` objects to UNIX timestamps for Python 3 (https://github.com/ansible-collections/community.crypto/issues/808, https://github.com/ansible-collections/community.crypto/pull/810).

community.dns
~~~~~~~~~~~~~

- Update Public Suffix List.

community.docker
~~~~~~~~~~~~~~~~

- docker_compose_v2 - improve parsing of dry-run image build operations from JSON events (https://github.com/ansible-collections/community.docker/issues/975, https://github.com/ansible-collections/community.docker/pull/976).

community.general
~~~~~~~~~~~~~~~~~

- bitwarden lookup plugin - support BWS v0.3.0 syntax breaking change (https://github.com/ansible-collections/community.general/pull/9028).
- collection_version lookup plugin - use ``importlib`` directly instead of the deprecated and in ansible-core 2.19 removed ``ansible.module_utils.compat.importlib`` (https://github.com/ansible-collections/community.general/pull/9084).
- gitlab_label - update label's color (https://github.com/ansible-collections/community.general/pull/9010).
- keycloak_clientscope_type - fix detect changes in check mode (https://github.com/ansible-collections/community.general/issues/9092, https://github.com/ansible-collections/community.general/pull/9093).
- keycloak_group - fix crash caused in subgroup creation. The crash was caused by a missing or empty ``subGroups`` property in Keycloak ≥23 (https://github.com/ansible-collections/community.general/issues/8788, https://github.com/ansible-collections/community.general/pull/8979).
- modprobe - fix check mode not being honored for ``persistent`` option (https://github.com/ansible-collections/community.general/issues/9051, https://github.com/ansible-collections/community.general/pull/9052).
- one_host - fix if statements for cases when ``ID=0`` (https://github.com/ansible-collections/community.general/issues/1199, https://github.com/ansible-collections/community.general/pull/8907).
- one_image - fix module failing due to a class method typo (https://github.com/ansible-collections/community.general/pull/9056).
- one_image_info - fix module failing due to a class method typo (https://github.com/ansible-collections/community.general/pull/9056).
- one_vnet - fix module failing due to a variable typo (https://github.com/ansible-collections/community.general/pull/9019).
- redfish_utils module utils - fix issue with URI parsing to gracefully handling trailing slashes when extracting member identifiers (https://github.com/ansible-collections/community.general/issues/9047, https://github.com/ansible-collections/community.general/pull/9057).

community.postgresql
~~~~~~~~~~~~~~~~~~~~

- postgresql_set - fixes resetting logic to allow resetting shared_preload_libraries with ``reset: true`` (https://github.com/ansible-collections/community.postgresql/issues/744).
- postgresql_set - forbids resetting shared_preload_libraries by passing an empty string (https://github.com/ansible-collections/community.postgresql/issues/744).

community.vmware
~~~~~~~~~~~~~~~~

- vmware_guest - Fix existing disk erroneously being re-created when modifying vm with 8 or more disks. (https://github.com/ansible-collections/community.vmware/pull/2173).
- vmware_vmotion - Fix a `list index out of range` error when vSphere doesn't provide a placement recommendation (https://github.com/ansible-collections/community.vmware/pull/2208).

containers.podman
~~~~~~~~~~~~~~~~~

- Add missing parameters for podman container quadlet
- Add new options for podman_network
- Add option to specify kube file content in module
- Add quadlet file mode option to specify file permission
- Add secret to login module
- Don't check image availability in Quadlet
- Fix max_size idempotency issue
- Fix typo in quadlet generator
- Fix unsupported pull policy in example on podman_container.py
- fix quadlet cmd_args append mistake
- podman_login does not support check_mode

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- idrac_storage_volume - Issue(290766) - The module will report success instead of showing failure for new virtual creation on the BOSS-N1 controller if a virtual disk is already present on the same controller.
- idrac_support_assist - Issue(308550) - This module fails when the NFS share path contains sub directory.
- ome_diagnostics - Issue(279193) - Export of SupportAssist collection logs to the share location fails on OME version 4.0.0.

f5networks.f5_modules
~~~~~~~~~~~~~~~~~~~~~

- bigip_imish_config - fixed a bug that resulted in incomplete config when using BGV route domain

fortinet.fortios
~~~~~~~~~~~~~~~~

- Github
- Mantis
- Return invalid json content instead of error while adding redundant comma at the end of the last variable in `fortios_json_generic`.

purestorage.flashblade
~~~~~~~~~~~~~~~~~~~~~~

- purefb_certs - Fix issue with importing certificates
- purefb_certs - Fix parameter mispelling of ``intermeadiate_cert`` to ``intermediate_cert``. Keep original mispelling as an alias.
- purefb_ds - Initialize variable correctly
- purefb_policy - Initialize variable correctly
- purefb_ra - Fix incorrect import statement
- purefb_snap - Fix issue with immeadiate remote snapshots not executing

vmware.vmware
~~~~~~~~~~~~~

- Fix typos in all module documentation and README
- cluster_drs - fixed backwards vMotion rate (input 1 set rate to 5 in vCenter) (https://github.com/ansible-collections/vmware.vmware/issues/68)

Known Issues
------------

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- idrac_diagnostics - Issue(285322) - This module doesn't support export of diagnostics file to HTTP and HTTPS share via SOCKS proxy.
- idrac_firmware - Issue(279282) - This module does not support firmware update using HTTP, HTTPS, and FTP shares with authentication on iDRAC8.
- ome_smart_fabric_uplink - Issue(186024) - The module supported by OpenManage Enterprise Modular, however it does not allow the creation of multiple uplinks of the same name. If an uplink is created using the same name as an existing uplink, then the existing uplink is modified.

New Modules
-----------

purestorage.flashblade
~~~~~~~~~~~~~~~~~~~~~~

- purestorage.flashblade.purefb_saml - Manage FlashBlade SAML2 service and identity providers

Unchanged Collections
---------------------

- amazon.aws (still version 8.2.1)
- ansible.netcommon (still version 6.1.3)
- ansible.utils (still version 4.1.0)
- ansible.windows (still version 2.5.0)
- arista.eos (still version 9.0.0)
- awx.awx (still version 24.6.1)
- azure.azcollection (still version 2.7.0)
- check_point.mgmt (still version 5.2.3)
- chocolatey.chocolatey (still version 1.5.3)
- cisco.aci (still version 2.10.1)
- cisco.asa (still version 5.0.1)
- cisco.intersight (still version 2.0.20)
- cisco.ios (still version 8.0.0)
- cisco.iosxr (still version 9.0.0)
- cisco.mso (still version 2.9.0)
- cisco.nxos (still version 8.1.0)
- cisco.ucs (still version 1.14.0)
- cloud.common (still version 3.0.0)
- cloudscale_ch.cloud (still version 2.4.0)
- community.aws (still version 8.0.0)
- community.ciscosmb (still version 1.0.9)
- community.digitalocean (still version 1.27.0)
- community.grafana (still version 1.9.1)
- community.hashi_vault (still version 6.2.0)
- community.hrobot (still version 2.0.2)
- community.libvirt (still version 1.3.0)
- community.mysql (still version 3.10.3)
- community.okd (still version 3.0.1)
- community.proxysql (still version 1.6.0)
- community.rabbitmq (still version 1.3.0)
- community.sap_libs (still version 1.4.2)
- community.sops (still version 1.9.1)
- community.windows (still version 2.3.0)
- community.zabbix (still version 2.5.1)
- cyberark.pas (still version 1.0.27)
- dellemc.enterprise_sonic (still version 2.5.1)
- dellemc.powerflex (still version 2.5.0)
- dellemc.unity (still version 2.0.0)
- fortinet.fortimanager (still version 2.7.0)
- frr.frr (still version 2.0.2)
- google.cloud (still version 1.4.1)
- hetzner.hcloud (still version 3.1.1)
- ibm.qradar (still version 3.0.0)
- ibm.spectrum_virtualize (still version 2.0.0)
- ibm.storage_virtualize (still version 2.5.0)
- ieisystem.inmanage (still version 2.0.0)
- infinidat.infinibox (still version 1.4.5)
- infoblox.nios_modules (still version 1.7.0)
- inspur.ispim (still version 2.2.3)
- inspur.sm (still version 2.3.0)
- junipernetworks.junos (still version 8.0.0)
- kaytus.ksmanage (still version 1.2.2)
- kubernetes.core (still version 3.2.0)
- kubevirt.core (still version 1.5.0)
- lowlydba.sqlserver (still version 2.3.4)
- microsoft.ad (still version 1.7.1)
- netapp.ontap (still version 22.12.0)
- netapp_eseries.santricity (still version 1.4.1)
- netbox.netbox (still version 3.20.0)
- ngine_io.cloudstack (still version 2.5.0)
- ngine_io.exoscale (still version 1.1.0)
- openstack.cloud (still version 2.2.0)
- openvswitch.openvswitch (still version 2.1.1)
- ovirt.ovirt (still version 3.2.0)
- purestorage.flasharray (still version 1.31.1)
- sensu.sensu_go (still version 1.14.0)
- splunk.es (still version 3.0.0)
- t_systems_mms.icinga_director (still version 2.0.1)
- theforeman.foreman (still version 4.2.0)
- vmware.vmware_rest (still version 3.2.0)
- vultr.cloud (still version 1.13.0)
- vyos.vyos (still version 4.1.0)
- wti.remote (still version 1.0.10)

v10.5.0
=======

.. contents::
  :local:
  :depth: 2

Release Summary
---------------

Release Date: 2024-10-08

`Porting Guide <https://docs.ansible.com/ansible/devel/porting_guides.html>`_

Ansible-core
------------

Ansible 10.5.0 contains ansible-core version 2.17.5.
This is a newer version than version 2.17.4 contained in the previous Ansible release.

The changes are reported in the combined changelog below.

Changed Collections
-------------------

If not mentioned explicitly, the changes are reported in the combined changelog below.

+---------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| Collection                | Ansible 10.4.0 | Ansible 10.5.0 | Notes                                                                                                                        |
+===========================+================+================+==============================================================================================================================+
| chocolatey.chocolatey     | 1.5.1          | 1.5.3          |                                                                                                                              |
+---------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.dnac                | 6.18.0         | 6.20.0         |                                                                                                                              |
+---------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.intersight          | 2.0.17         | 2.0.20         | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+---------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.meraki              | 2.18.1         | 2.18.2         |                                                                                                                              |
+---------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.ucs                 | 1.11.0         | 1.14.0         | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+---------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.crypto          | 2.22.0         | 2.22.1         |                                                                                                                              |
+---------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.dns             | 3.0.4          | 3.0.5          |                                                                                                                              |
+---------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.docker          | 3.12.1         | 3.13.0         |                                                                                                                              |
+---------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.general         | 9.4.0          | 9.5.0          |                                                                                                                              |
+---------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.hrobot          | 2.0.1          | 2.0.2          |                                                                                                                              |
+---------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.mongodb         | 1.7.6          | 1.7.7          | There are no changes recorded in the changelog.                                                                              |
+---------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.postgresql      | 3.5.0          | 3.6.1          |                                                                                                                              |
+---------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.sops            | 1.9.0          | 1.9.1          |                                                                                                                              |
+---------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.vmware          | 4.7.0          | 4.7.1          |                                                                                                                              |
+---------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| containers.podman         | 1.15.4         | 1.16.1         |                                                                                                                              |
+---------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| dellemc.enterprise_sonic  | 2.5.0          | 2.5.1          |                                                                                                                              |
+---------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| dellemc.openmanage        | 9.6.0          | 9.7.0          |                                                                                                                              |
+---------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| f5networks.f5_modules     | 1.30.1         | 1.31.0         |                                                                                                                              |
+---------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| grafana.grafana           | 5.5.0          | 5.5.1          |                                                                                                                              |
+---------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| ibm.storage_virtualize    | 2.4.1          | 2.5.0          |                                                                                                                              |
+---------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| infoblox.nios_modules     | 1.6.1          | 1.7.0          |                                                                                                                              |
+---------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| lowlydba.sqlserver        | 2.3.3          | 2.3.4          |                                                                                                                              |
+---------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| netapp_eseries.santricity | 1.4.0          | 1.4.1          |                                                                                                                              |
+---------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| netbox.netbox             | 3.19.1         | 3.20.0         |                                                                                                                              |
+---------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| ngine_io.cloudstack       | 2.4.0          | 2.5.0          |                                                                                                                              |
+---------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| vmware.vmware_rest        | 3.1.0          | 3.2.0          |                                                                                                                              |
+---------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| wti.remote                | 1.0.8          | 1.0.10         | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+---------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+

Major Changes
-------------

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- idrac_secure_boot - This module allows to Configure attributes, import, or export secure boot certificate, and reset keys.
- idrac_system_erase - This module allows to Erase system and storage components of the server on iDRAC.

Minor Changes
-------------

chocolatey.chocolatey
~~~~~~~~~~~~~~~~~~~~~

- Remove support for End of Life ansible-core 2.13, 2.14

cisco.dnac
~~~~~~~~~~

- Added 'fabric_transits_workflow_manager.py' to perform operations on SDA fabric transits.
- Adding  support to update  password  in user_role_workflow_manager module.
- Changes in inventory_workflow_manager module.
- Changes in ise_radius_integration_workflow_manager module to check ise certification status.
- Changes in network_compliance_workflow_manager module.
- Changes in network_settings_workflow_manager module to support exception handling.
- Changes in rma_workflow_manager module.
- Changes in sda_extranet_policies_workflow_manager module.
- Changes in swim_workflow_manager module to support CCO image.
- Changes in user_role_workflow_manager module.
- Minor bug fixes in network_compliance_workflow_manager module.
- Removed sda_extranet_policies_workflow_manager.py module.
- Removing git release workflows.
- Setting dnac versions and compare for version based routing.
- Unit test automation for worflow_manager modules.

cisco.meraki
~~~~~~~~~~~~

- Include networks_appliance_traffic_shaping_custom_performance_classes_info plugin.

community.general
~~~~~~~~~~~~~~~~~

- dig lookup plugin - add ``port`` option to specify DNS server port (https://github.com/ansible-collections/community.general/pull/8966).
- flatpak - improve the parsing of Flatpak application IDs based on official guidelines (https://github.com/ansible-collections/community.general/pull/8909).
- gio_mime - adjust code ahead of the old ``VardDict`` deprecation (https://github.com/ansible-collections/community.general/pull/8855).
- gitlab_deploy_key - better construct when using ``dict.items()`` (https://github.com/ansible-collections/community.general/pull/8876).
- gitlab_group - add many new parameters (https://github.com/ansible-collections/community.general/pull/8908).
- gitlab_group - better construct when using ``dict.items()`` (https://github.com/ansible-collections/community.general/pull/8876).
- gitlab_issue - better construct when using ``dict.items()`` (https://github.com/ansible-collections/community.general/pull/8876).
- gitlab_merge_request - better construct when using ``dict.items()`` (https://github.com/ansible-collections/community.general/pull/8876).
- gitlab_runner - better construct when using ``dict.items()`` (https://github.com/ansible-collections/community.general/pull/8876).
- icinga2_host - replace loop with dict comprehension (https://github.com/ansible-collections/community.general/pull/8876).
- jira - adjust code ahead of the old ``VardDict`` deprecation (https://github.com/ansible-collections/community.general/pull/8856).
- keycloak_client - add ``client-x509`` choice to ``client_authenticator_type`` (https://github.com/ansible-collections/community.general/pull/8973).
- keycloak_user_federation - add the user federation config parameter ``referral`` to the module arguments (https://github.com/ansible-collections/community.general/pull/8954).
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
- one_image - add option ``persistent`` to manage image persistence (https://github.com/ansible-collections/community.general/issues/3578, https://github.com/ansible-collections/community.general/pull/8889).
- one_image - extend xsd scheme to make it return a lot more info about image (https://github.com/ansible-collections/community.general/pull/8889).
- one_image - refactor code to make it more similar to ``one_template`` and ``one_vnet`` (https://github.com/ansible-collections/community.general/pull/8889).
- one_image_info - extend xsd scheme to make it return a lot more info about image (https://github.com/ansible-collections/community.general/pull/8889).
- one_image_info - refactor code to make it more similar to ``one_template`` and ``one_vnet`` (https://github.com/ansible-collections/community.general/pull/8889).
- open_iscsi - allow login to a portal with multiple targets without specifying any of them (https://github.com/ansible-collections/community.general/pull/8719).
- opennebula.py - add VM ``id`` and VM ``host`` to inventory host data (https://github.com/ansible-collections/community.general/pull/8532).
- passwordstore lookup plugin - add subkey creation/update support (https://github.com/ansible-collections/community.general/pull/8952).
- proxmox inventory plugin - clean up authentication code (https://github.com/ansible-collections/community.general/pull/8917).
- redfish_command - add handling of the ``PasswordChangeRequired`` message from services in the ``UpdateUserPassword`` command to directly modify the user's password if the requested user is the one invoking the operation (https://github.com/ansible-collections/community.general/issues/8652, https://github.com/ansible-collections/community.general/pull/8653).
- redfish_confg - remove ``CapacityBytes`` from required paramaters of the ``CreateVolume`` command (https://github.com/ansible-collections/community.general/pull/8956).
- redfish_config - add parameter ``storage_none_volume_deletion`` to ``CreateVolume`` command in order to control the automatic deletion of non-RAID volumes (https://github.com/ansible-collections/community.general/pull/8990).
- redfish_info - adds ``RedfishURI`` and ``StorageId`` to Disk inventory (https://github.com/ansible-collections/community.general/pull/8937).
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
- scaleway_user_data - better construct when using ``dict.items()`` (https://github.com/ansible-collections/community.general/pull/8876).
- udm_dns_record - replace loop with ``dict.update()`` (https://github.com/ansible-collections/community.general/pull/8876).

community.postgresql
~~~~~~~~~~~~~~~~~~~~

- postgresql_privs - adds support for granting and revoking privileges on foreign tables (https://github.com/ansible-collections/community.postgresql/issues/724).
- postgresql_subscription - adds support for managing subscriptions in the situation where the ``subconninfo`` column is unavailable (such as in CloudSQL) (https://github.com/ansible-collections/community.postgresql/issues/726).

containers.podman
~~~~~~~~~~~~~~~~~

- Add arch to podman build command explicitly
- Add group_add parameter for podman quadlet
- Add support for check_mode in Quadlet
- Trigger a new image build when we detect that the Containerfile has changed.
- Update inspection info about objects in modules

f5networks.f5_modules
~~~~~~~~~~~~~~~~~~~~~

- bigip_asm_dos_application - add support for creating dos profile.
- bigip_device_info - virtual-servers - return per_flow_request_access_policy if defined.
- bigip_virtual_server - set per_flow_request_access_policy and stay idempotent.

ibm.storage_virtualize
~~~~~~~~~~~~~~~~~~~~~~

- ibm_sv_manage_storage_partition - Added support for creating draft partition, publishing a draft partition, and merging 2 partitions
- ibm_sv_manage_syslog_server - Added support for creating TLS syslog server, and modifying existing UDP or TCP servers to TLS server
- ibm_sv_manage_truststore_for_replication - Added support for enabling various options (syslog, RESTAPI, vasa, ipsec, snmp and email) during truststore creation
- ibm_svc_host - Added support to add host into draft partition and to create an NVMeFC host
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
- Added option `hostname_field` to ``nb_inventory`` to be able to set the inventory hostname from a field in custom_fields
- Adjust tests for various modules
- Fix the form_factor option on netbox_rack
- Update CI for NetBox 4.1

ngine_io.cloudstack
~~~~~~~~~~~~~~~~~~~

- cs_instance - Added new arguments ``user_data_name`` and ``user_data_details`` (https://github.com/ngine-io/ansible-collection-cloudstack/pull/134).
- cs_service_offering - Add support for storagetag (https://github.com/ngine-io/ansible-collection-cloudstack/pull/118).

vmware.vmware_rest
~~~~~~~~~~~~~~~~~~

- Removed the scenario guides which are pretty much unmaintained and, therefor, possibly outdated and misleading (https://github.com/ansible-collections/vmware.vmware_rest/pull/524).

Deprecated Features
-------------------

- The ``ngine_io.exoscale`` collection has been deprecated.
  It will be removed from Ansible 11 if no one starts maintaining it again before Ansible 11.
  See `Collections Removal Process for unmaintained collections <https://docs.ansible.com/ansible/devel/community/collection_contributors/collection_package_removal.html#unmaintained-collections>`__ for more details (`https://forum.ansible.com/t/2572 <https://forum.ansible.com/t/2572>`__).
- The collection ``t_systems_mms.icinga_director`` was renamed to ``telekom_mms.icinga_director``.
  For now both collections are included in Ansible.
  The content in ``t_systems_mms.icinga_director`` has been replaced by deprecated redirects in Ansible 9.0.0.
  The collection will be completely removed from Ansible 11.
  Please update your FQCNs from ``t_systems_mms.icinga_director`` to ``telekom_mms.icinga_director``.
- The sensu.sensu_go collection will be removed from Ansible 12 due to violations of the Ansible inclusion requirements.
  The collection has \ `unresolved sanity test failures <https://github.com/sensu/sensu-go-ansible/issues/362>`__.
  See `Collections Removal Process for collections not satisfying the collection requirements <https://docs.ansible.com/ansible/devel/community/collection_contributors/collection_package_removal.html#collections-not-satisfying-the-collection-requirements>`__ for more details, including for how this can be cancelled (`https://forum.ansible.com/t/8380 <https://forum.ansible.com/t/8380>`__).
  After removal, users can still install this collection with ``ansible-galaxy collection install sensu.sensu_go``.

community.general
~~~~~~~~~~~~~~~~~

- hipchat - the hipchat service has been discontinued and the self-hosted variant has been End of Life since 2020. The module is therefore deprecated and will be removed from community.general 11.0.0 if nobody provides compelling reasons to still keep it (https://github.com/ansible-collections/community.general/pull/8919).

Bugfixes
--------

Ansible-core
~~~~~~~~~~~~

- Add descriptions for ``ansible-galaxy install --help` and ``ansible-galaxy role|collection install --help``.
- Errors now preserve stacked error messages even when YAML is involved.
- ``ansible-galaxy install --help`` - Fix the usage text and document that the requirements file passed to ``-r`` can include collections and roles.
- copy - mtime/atime not updated. Fix now update mtime/atime(https://github.com/ansible/ansible/issues/83013)
- delay keyword is now a float, matching the underlying 'time' API and user expectations.
- dnf5 - re-introduce the ``state: installed`` alias to ``state: present`` (https://github.com/ansible/ansible/issues/83960)
- module_utils atomic_move (used by most file based modules), now correctly handles permission copy and setting mtime correctly across all paths

chocolatey.chocolatey
~~~~~~~~~~~~~~~~~~~~~

- win_chocolatey - task crashes if PATH contains multiple choco.exe on the target machine

community.crypto
~~~~~~~~~~~~~~~~

- acme_* modules - when querying renewal information, make sure to insert a slash between the base URL and the certificate identifier (https://github.com/ansible-collections/community.crypto/issues/801, https://github.com/ansible-collections/community.crypto/pull/802).
- various modules - pass absolute paths to ``module.atomic_move()`` (https://github.com/ansible/ansible/issues/83950, https://github.com/ansible-collections/community.crypto/pull/799).

community.dns
~~~~~~~~~~~~~

- Update Public Suffix List.

community.docker
~~~~~~~~~~~~~~~~

- docker_prune - fix handling of lists for the filter options (https://github.com/ansible-collections/community.docker/issues/961, https://github.com/ansible-collections/community.docker/pull/966).

community.general
~~~~~~~~~~~~~~~~~

- cloudflare_dns - fix changing Cloudflare SRV records (https://github.com/ansible-collections/community.general/issues/8679, https://github.com/ansible-collections/community.general/pull/8948).
- cmd_runner module utils - call to ``get_best_parsable_locales()`` was missing parameter (https://github.com/ansible-collections/community.general/pull/8929).
- dig lookup plugin - fix using only the last nameserver specified (https://github.com/ansible-collections/community.general/pull/8970).
- django_command - option ``command`` is now split lexically before passed to underlying PythonRunner (https://github.com/ansible-collections/community.general/pull/8944).
- homectl - the module now tries to use ``legacycrypt`` on Python 3.13+ (https://github.com/ansible-collections/community.general/issues/4691, https://github.com/ansible-collections/community.general/pull/8987).
- ini_file - pass absolute paths to ``module.atomic_move()`` (https://github.com/ansible/ansible/issues/83950, https://github.com/ansible-collections/community.general/pull/8925).
- ipa_host - add ``force_create``, fix ``enabled`` and ``disabled`` states (https://github.com/ansible-collections/community.general/issues/1094, https://github.com/ansible-collections/community.general/pull/8920).
- ipa_hostgroup - fix ``enabled `` and ``disabled`` states (https://github.com/ansible-collections/community.general/issues/8408, https://github.com/ansible-collections/community.general/pull/8900).
- java_keystore - pass absolute paths to ``module.atomic_move()`` (https://github.com/ansible/ansible/issues/83950, https://github.com/ansible-collections/community.general/pull/8925).
- jenkins_plugin - pass absolute paths to ``module.atomic_move()`` (https://github.com/ansible/ansible/issues/83950, https://github.com/ansible-collections/community.general/pull/8925).
- kdeconfig - pass absolute paths to ``module.atomic_move()`` (https://github.com/ansible/ansible/issues/83950, https://github.com/ansible-collections/community.general/pull/8925).
- keycloak_realm - fix change detection in check mode by sorting the lists in the realms beforehand (https://github.com/ansible-collections/community.general/pull/8877).
- keycloak_user_federation - add module argument allowing users to configure the update mode for the parameter ``bindCredential`` (https://github.com/ansible-collections/community.general/pull/8898).
- keycloak_user_federation - minimize change detection by setting ``krbPrincipalAttribute`` to ``''`` in Keycloak responses if missing (https://github.com/ansible-collections/community.general/pull/8785).
- keycloak_user_federation - remove ``lastSync`` parameter from Keycloak responses to minimize diff/changes (https://github.com/ansible-collections/community.general/pull/8812).
- keycloak_userprofile - fix empty response when fetching userprofile component by removing ``parent=parent_id`` filter (https://github.com/ansible-collections/community.general/pull/8923).
- keycloak_userprofile - improve diff by deserializing the fetched ``kc.user.profile.config`` and serialize it only when sending back (https://github.com/ansible-collections/community.general/pull/8940).
- lxd_container - fix bug introduced in previous commit (https://github.com/ansible-collections/community.general/pull/8895, https://github.com/ansible-collections/community.general/issues/8888).
- one_service - fix service creation after it was deleted with ``unique`` parameter (https://github.com/ansible-collections/community.general/issues/3137, https://github.com/ansible-collections/community.general/pull/8887).
- pam_limits - pass absolute paths to ``module.atomic_move()`` (https://github.com/ansible/ansible/issues/83950, https://github.com/ansible-collections/community.general/pull/8925).
- python_runner module utils - parameter ``path_prefix`` was being handled as string when it should be a list (https://github.com/ansible-collections/community.general/pull/8944).
- udm_user - the module now tries to use ``legacycrypt`` on Python 3.13+ (https://github.com/ansible-collections/community.general/issues/4690, https://github.com/ansible-collections/community.general/pull/8987).

community.postgresql
~~~~~~~~~~~~~~~~~~~~

- postgresql_db - fix issues due to columns in pg_database changing in Postgres 17. (https://github.com/ansible-collections/community.postgresql/issues/729).
- postgresql_info - Use a server check that works on beta and rc versions as well as on actual releases.
- postgresql_user - remove a comment from unit tests that breaks pre-compile (https://github.com/ansible-collections/community.postgresql/issues/737).

community.sops
~~~~~~~~~~~~~~

- sops_encrypt - pass absolute paths to ``module.atomic_move()`` (https://github.com/ansible/ansible/issues/83950, https://github.com/ansible-collections/community.sops/pull/208).

community.vmware
~~~~~~~~~~~~~~~~

- vcenter_standard_key_provider - Fix documentation (https://github.com/ansible-collections/community.vmware/pull/2192).
- vmware_all_snapshots_info - fixed the datacenter parameter was ignored(https://github.com/ansible-collections/community.vmware/pull/2165).
- vmware_dvswitch - Fix Pylint issue (https://github.com/ansible-collections/community.vmware/pull/2186).
- vmware_dvswitch_nioc - Fix documentation (https://github.com/ansible-collections/community.vmware/pull/2192).
- vmware_dvswitch_pvlans - Fix Pylint issue (https://github.com/ansible-collections/community.vmware/pull/2186).
- vmware_guest - Fix documentation (https://github.com/ansible-collections/community.vmware/pull/2192).
- vmware_guest_controller - Fix documentation (https://github.com/ansible-collections/community.vmware/pull/2192).
- vmware_guest_disk - Fix documentation (https://github.com/ansible-collections/community.vmware/pull/2192).
- vmware_guest_serial_port - Fix documentation (https://github.com/ansible-collections/community.vmware/pull/2192).
- vmware_guest_tpm - Fix Pylint issue (https://github.com/ansible-collections/community.vmware/pull/2186).
- vmware_host - Fix Pylint issue (https://github.com/ansible-collections/community.vmware/pull/2186).
- vmware_host_dns - Fix Pylint issue (https://github.com/ansible-collections/community.vmware/pull/2186).
- vmware_host_inventory - Fix Pylint issue (https://github.com/ansible-collections/community.vmware/pull/2186).
- vmware_host_powerstate - Fix Pylint issue (https://github.com/ansible-collections/community.vmware/pull/2186).
- vmware_tools - Fix documentation (https://github.com/ansible-collections/community.vmware/pull/2192).
- vmware_vm_inventory - Fix Pylint issue (https://github.com/ansible-collections/community.vmware/pull/2186).
- vmware_vmotion - Fix Pylint issue (https://github.com/ansible-collections/community.vmware/pull/2186).

containers.podman
~~~~~~~~~~~~~~~~~

- CI - Add images removal for tests
- CI - Fix podman CI test container images
- CI - add ignore list for Ansible sanity for 2.19
- CI - bump artifacts versions for GHactions
- CI - change k8s.gcr.io to registry.k8s.io in tests
- CI - fix Podman search of invalid image
- Disable idempotency for pod_id_file
- Fix command idempotency with quotes
- Fix health-startup-cmd
- Fix logic in Podman images
- Fix podman image permissions issue and runlable test
- Fix quadlet parameters when container uses rootfs
- don't document quadlet_dir as required when setting state=quadlet
- fix for tls_verify being ignored
- fix(podman_image) - skip empty volume items
- fix(podman_save) - always changed when force
- modify error and docs

dellemc.enterprise_sonic
~~~~~~~~~~~~~~~~~~~~~~~~

- ConnectionError - Add the needed import of the Ansible ConnectionError exception class for all files where it was previously missing. (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/445).
- Update regex search expression for 'not found' error message in httpapi/sonic.py 'edit_config' method (https://github.com/ansible-collection/dellemc.enterprise_sonic/pull/443).
- sonic_system - Catch the ConnectionError exception caused by unconditional fetching of auditd and ip loadshare hash algorithm configuration, and return empty configuration instead of allowing the uncaught exception to abort all "system" operations on SONiC images older than version 4.4.0 (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/441).

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- Resolved the issue in ``idrac_gather_facts`` role where it was failing for some component in iDRAC8. (https://github.com/dell/dellemc-openmanage-ansible-modules/issues/718)

ibm.storage_virtualize
~~~~~~~~~~~~~~~~~~~~~~

- ibm_svc_manage_callhome - Added support to change a subset of proxy settings

infoblox.nios_modules
~~~~~~~~~~~~~~~~~~~~~

- Adjusted unit test assertions for Mock.called_once_with.
- Fixed an issue in the `nios_host_record` module where the `mac` parameter was not handled correctly.
- Fixed the update operation in the `nios_network` module where the `network` parameter was not handled correctly.
- Omits DNS view from filter critera when renaming a host object and DNS is bypassed. (https://github.com/infobloxopen/infoblox-ansible/issues/230)
- nios_host_record - rename logic included DNS view in filter critera, even when DNS had been bypassed.

lowlydba.sqlserver
~~~~~~~~~~~~~~~~~~

- Include warning logs in failure output for the restore module to indicate root causes (https://github.com/lowlydba/lowlydba.sqlserver/pull/266).

netapp_eseries.santricity
~~~~~~~~~~~~~~~~~~~~~~~~~

- Fixed pep8, pylint, and validate-modules issues found by ansible-test.
- Updated outdated command in unit tests.

netbox.netbox
~~~~~~~~~~~~~

- If `fetch_all` is `false`, prefix lookup depends on site lookup, so move it to secondary lookup (https://github.com/netbox-community/ansible_modules/issues/733)

ngine_io.cloudstack
~~~~~~~~~~~~~~~~~~~

- Fixed a bug related to the new option ``validate_certs`` (https://github.com/ngine-io/ansible-collection-cloudstack/pull/135).

Known Issues
------------

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- idrac_diagnostics - Issue(285322) - This module doesn't support export of diagnostics file to HTTP and HTTPS share via SOCKS proxy.
- idrac_firmware - Issue(279282) - This module does not support firmware update using HTTP, HTTPS, and FTP shares with authentication on iDRAC8.
- idrac_storage_volume - Issue(290766) - The module will report success instead of showing failure for new virtual creation on the BOSS-N1 controller if a virtual disk is already present on the same controller.
- idrac_support_assist - Issue(308550) - This module fails when the NFS share path contains sub directory.
- ome_diagnostics - Issue(279193) - Export of SupportAssist collection logs to the share location fails on OME version 4.0.0.
- ome_smart_fabric_uplink - Issue(186024) - The module supported by OpenManage Enterprise Modular, however it does not allow the creation of multiple uplinks of the same name. If an uplink is created using the same name as an existing uplink, then the existing uplink is modified.

New Modules
-----------

community.docker
~~~~~~~~~~~~~~~~

- community.docker.docker_compose_v2_exec - Run command in a container of a Compose service.
- community.docker.docker_compose_v2_run - Run command in a new container of a Compose service.

community.general
~~~~~~~~~~~~~~~~~

- community.general.ipa_getkeytab - Manage keytab file in FreeIPA.

containers.podman
~~~~~~~~~~~~~~~~~

- containers.podman.podman_container_copy - Copy file to or from a container

infoblox.nios_modules
~~~~~~~~~~~~~~~~~~~~~

- infoblox.nios_modules.nios_extensible_attribute - Configure Infoblox NIOS extensible attribute definition
- infoblox.nios_modules.nios_nsgroup_delegation - Configure InfoBlox DNS Nameserver Delegation Groups
- infoblox.nios_modules.nios_nsgroup_forwardingmember - Configure InfoBlox DNS Nameserver Forward/Stub Server Groups
- infoblox.nios_modules.nios_nsgroup_forwardstubserver - Configure InfoBlox DNS Nameserver Forwarding Member Groups
- infoblox.nios_modules.nios_nsgroup_stubmember - Configure InfoBlox DNS Nameserver Stub Member Groups

netbox.netbox
~~~~~~~~~~~~~

- netbox.netbox.netbox_permission - Creates or removes permissions from NetBox
- netbox.netbox.netbox_token - Creates or removes tokens from NetBox
- netbox.netbox.netbox_tunnel - Create, update or delete tunnels within NetBox
- netbox.netbox.netbox_tunnel_group - Create, update or delete tunnel groups within NetBox
- netbox.netbox.netbox_user - Creates or removes users from NetBox
- netbox.netbox.netbox_user_group - Creates or removes user groups from NetBox

Unchanged Collections
---------------------

- amazon.aws (still version 8.2.1)
- ansible.netcommon (still version 6.1.3)
- ansible.posix (still version 1.5.4)
- ansible.utils (still version 4.1.0)
- ansible.windows (still version 2.5.0)
- arista.eos (still version 9.0.0)
- awx.awx (still version 24.6.1)
- azure.azcollection (still version 2.7.0)
- check_point.mgmt (still version 5.2.3)
- cisco.aci (still version 2.10.1)
- cisco.asa (still version 5.0.1)
- cisco.ios (still version 8.0.0)
- cisco.iosxr (still version 9.0.0)
- cisco.ise (still version 2.9.3)
- cisco.mso (still version 2.9.0)
- cisco.nxos (still version 8.1.0)
- cloud.common (still version 3.0.0)
- cloudscale_ch.cloud (still version 2.4.0)
- community.aws (still version 8.0.0)
- community.ciscosmb (still version 1.0.9)
- community.digitalocean (still version 1.27.0)
- community.grafana (still version 1.9.1)
- community.hashi_vault (still version 6.2.0)
- community.library_inventory_filtering_v1 (still version 1.0.1)
- community.libvirt (still version 1.3.0)
- community.mysql (still version 3.10.3)
- community.network (still version 5.0.3)
- community.okd (still version 3.0.1)
- community.proxysql (still version 1.6.0)
- community.rabbitmq (still version 1.3.0)
- community.routeros (still version 2.19.0)
- community.sap_libs (still version 1.4.2)
- community.windows (still version 2.3.0)
- community.zabbix (still version 2.5.1)
- cyberark.conjur (still version 1.3.0)
- cyberark.pas (still version 1.0.27)
- dellemc.powerflex (still version 2.5.0)
- dellemc.unity (still version 2.0.0)
- fortinet.fortimanager (still version 2.7.0)
- fortinet.fortios (still version 2.3.7)
- frr.frr (still version 2.0.2)
- google.cloud (still version 1.4.1)
- hetzner.hcloud (still version 3.1.1)
- ibm.qradar (still version 3.0.0)
- ibm.spectrum_virtualize (still version 2.0.0)
- ieisystem.inmanage (still version 2.0.0)
- infinidat.infinibox (still version 1.4.5)
- inspur.ispim (still version 2.2.3)
- inspur.sm (still version 2.3.0)
- junipernetworks.junos (still version 8.0.0)
- kaytus.ksmanage (still version 1.2.2)
- kubernetes.core (still version 3.2.0)
- kubevirt.core (still version 1.5.0)
- microsoft.ad (still version 1.7.1)
- netapp.cloudmanager (still version 21.22.1)
- netapp.ontap (still version 22.12.0)
- netapp.storagegrid (still version 21.12.0)
- ngine_io.exoscale (still version 1.1.0)
- openstack.cloud (still version 2.2.0)
- openvswitch.openvswitch (still version 2.1.1)
- ovirt.ovirt (still version 3.2.0)
- purestorage.flasharray (still version 1.31.1)
- purestorage.flashblade (still version 1.18.0)
- sensu.sensu_go (still version 1.14.0)
- splunk.es (still version 3.0.0)
- t_systems_mms.icinga_director (still version 2.0.1)
- telekom_mms.icinga_director (still version 2.1.2)
- theforeman.foreman (still version 4.2.0)
- vmware.vmware (still version 1.5.0)
- vultr.cloud (still version 1.13.0)
- vyos.vyos (still version 4.1.0)

v10.4.0
=======

.. contents::
  :local:
  :depth: 2

Release Summary
---------------

Release Date: 2024-09-10

`Porting Guide <https://docs.ansible.com/ansible/devel/porting_guides.html>`_

Ansible-core
------------

Ansible 10.4.0 contains ansible-core version 2.17.4.
This is a newer version than version 2.17.3 contained in the previous Ansible release.

The changes are reported in the combined changelog below.

Changed Collections
-------------------

If not mentioned explicitly, the changes are reported in the combined changelog below.

+--------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| Collection               | Ansible 10.3.0 | Ansible 10.4.0 | Notes                                                                                                                        |
+==========================+================+================+==============================================================================================================================+
| amazon.aws               | 8.1.0          | 8.2.1          |                                                                                                                              |
+--------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| ansible.windows          | 2.4.0          | 2.5.0          |                                                                                                                              |
+--------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| azure.azcollection       | 2.6.0          | 2.7.0          | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+--------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.dnac               | 6.17.1         | 6.18.0         |                                                                                                                              |
+--------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.intersight         | 2.0.10         | 2.0.17         | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+--------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.ucs                | 1.10.0         | 1.11.0         | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+--------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.crypto         | 2.21.1         | 2.22.0         |                                                                                                                              |
+--------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.digitalocean   | 1.26.0         | 1.27.0         | There are no changes recorded in the changelog.                                                                              |
+--------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.dns            | 3.0.3          | 3.0.4          |                                                                                                                              |
+--------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.general        | 9.3.0          | 9.4.0          |                                                                                                                              |
+--------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.mysql          | 3.9.0          | 3.10.3         |                                                                                                                              |
+--------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.postgresql     | 3.4.1          | 3.5.0          |                                                                                                                              |
+--------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.routeros       | 2.18.0         | 2.19.0         |                                                                                                                              |
+--------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.sops           | 1.8.2          | 1.9.0          |                                                                                                                              |
+--------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.vmware         | 4.5.0          | 4.7.0          |                                                                                                                              |
+--------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.windows        | 2.2.0          | 2.3.0          |                                                                                                                              |
+--------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| dellemc.enterprise_sonic | 2.4.0          | 2.5.0          |                                                                                                                              |
+--------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| dellemc.openmanage       | 9.5.0          | 9.6.0          |                                                                                                                              |
+--------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| fortinet.fortimanager    | 2.6.0          | 2.7.0          |                                                                                                                              |
+--------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| google.cloud             | 1.3.0          | 1.4.1          |                                                                                                                              |
+--------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| grafana.grafana          | 5.4.0          | 5.5.0          |                                                                                                                              |
+--------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| microsoft.ad             | 1.6.0          | 1.7.1          |                                                                                                                              |
+--------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| ngine_io.cloudstack      | 2.3.0          | 2.4.0          |                                                                                                                              |
+--------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| purestorage.flasharray   | 1.30.2         | 1.31.1         |                                                                                                                              |
+--------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| theforeman.foreman       | 4.1.0          | 4.2.0          |                                                                                                                              |
+--------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| vmware.vmware            | 1.4.0          | 1.5.0          |                                                                                                                              |
+--------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| vmware.vmware_rest       | 3.0.1          | 3.1.0          |                                                                                                                              |
+--------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| wti.remote               | 1.0.5          | 1.0.8          | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+--------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+

Major Changes
-------------

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- idrac_secure_boot - This module allows to import the secure boot certificate.
- idrac_support_assist - This module allows to run and export SupportAssist collection logs on iDRAC.

grafana.grafana
~~~~~~~~~~~~~~~

- fix:mimir molecule should use ansible core 2.16 by @GVengelen in https://github.com/grafana/grafana-ansible-collection/pull/254

Minor Changes
-------------

amazon.aws
~~~~~~~~~~

- cloudwatch_metric_alarm - add  support for ``evaluate_low_sample_count_percentile``` parameter.
- cloudwatch_metric_alarm - support DatapointsToAlarm config (https://github.com/ansible-collections/amazon.aws/pull/2196).
- ec2_ami - Add support for uefi-preferred boot mode (https://github.com/ansible-collections/amazon.aws/pull/2253).
- ec2_instance - Add support for ``network_interfaces`` and ``network_interfaces_ids`` options replacing deprecated option ``network`` (https://github.com/ansible-collections/amazon.aws/pull/2123).
- ec2_instance - ``network.source_dest_check`` option has been deprecated and replaced by new option ``source_dest_check`` (https://github.com/ansible-collections/amazon.aws/pull/2123).
- ec2_instance - add the possibility to create instance with multiple network interfaces (https://github.com/ansible-collections/amazon.aws/pull/2123).
- ec2_metadata_facts - Add parameter ``metadata_token_ttl_seconds`` (https://github.com/ansible-collections/amazon.aws/pull/2209).
- rds_cluster - Add support for I/O-Optimized storage configuration for aurora clusters (https://github.com/ansible-collections/amazon.aws/pull/2063).
- rds_instance - snake case for parameter ``performance_insights_kms_key_id`` was incorrect according to boto documentation (https://github.com/ansible-collections/amazon.aws/pull/2163).
- s3_bucket - Add support for bucket inventories (https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-inventory.html)
- s3_object - Add support for ``expected_bucket_owner`` option (https://github.com/ansible-collections/amazon.aws/issues/2114).
- ssm parameter lookup - add new option ``droppath`` to drop the hierarchical search path from ssm parameter lookup results (https://github.com/ansible-collections/amazon.aws/pull/1756).

ansible.windows
~~~~~~~~~~~~~~~

- Set minimum supported Ansible version to 2.15 to align with the versions still supported by Ansible.
- owner - Migrated to ``Ansible.Basic`` format to add basic checks like invocation args checking
- win_powershell - Changed `sensitive_parameters` to use `New-Object`, rather than `::new()`

cisco.dnac
~~~~~~~~~~

- Added 'fabric_sites_zones_workflow_manager.py' to manage fabric sites/zones and update the authentication profile template.
- Added 'sda_extranet_policies_workflow_manager' to provide SDA Extranet Policies for managing SDA Extranet Policy.
- Added Circle CI support for integration testing.
- Bug fixes in user_role_workflow_manager module.
- Changes in accesspoint_workflow_manager module.
- Changes in device_configs_backup_workflow_manager to support name of the site to which the device is assigned.
- Changes in inventory_workflow_manager to support maximum devices to resync, and resync timeout.
- Changes in network_settings_workflow_manager to support reserve ip subpools.
- Changes in provision_workflow_manager to support enhanced log messages.
- Changes in rma_workflow_manager module to support pre check for device replacement.
- device_configs_backup_workflow_manager.py. added attribute 'site'.

community.crypto
~~~~~~~~~~~~~~~~

- openssl_privatekey, openssl_privatekey_pipe - add default value ``auto`` for ``cipher`` option, which happens to be the only supported value for this option anyway. Therefore it is no longer necessary to specify ``cipher=auto`` when providing ``passphrase`` (https://github.com/ansible-collections/community.crypto/issues/793, https://github.com/ansible-collections/community.crypto/pull/794).

community.general
~~~~~~~~~~~~~~~~~

- MH module utils - add parameter ``when`` to ``cause_changes`` decorator (https://github.com/ansible-collections/community.general/pull/8766).
- MH module utils - minor refactor in decorators (https://github.com/ansible-collections/community.general/pull/8766).
- alternatives - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8833).
- apache2_mod_proxy - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8814).
- apache2_mod_proxy - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8833).
- consul_acl - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8833).
- copr - Added ``includepkgs`` and ``excludepkgs`` parameters to limit the list of packages fetched or excluded from the repository(https://github.com/ansible-collections/community.general/pull/8779).
- credstash lookup plugin - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8822).
- csv module utils - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8814).
- deco MH module utils - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8822).
- etcd3 - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8822).
- gio_mime - mute the  old ``VarDict`` deprecation (https://github.com/ansible-collections/community.general/pull/8776).
- gitlab_group - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8814).
- gitlab_project - add option ``issues_access_level`` to enable/disable project issues (https://github.com/ansible-collections/community.general/pull/8760).
- gitlab_project - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8822).
- gitlab_project - sorted parameters in order to avoid future merge conflicts (https://github.com/ansible-collections/community.general/pull/8759).
- hashids filter plugin - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8814).
- hwc_ecs_instance - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8822).
- hwc_evs_disk - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8822).
- hwc_vpc_eip - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8822).
- hwc_vpc_peering_connect - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8822).
- hwc_vpc_port - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8822).
- hwc_vpc_subnet - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8822).
- imc_rest - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8833).
- ipa_otptoken - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8822).
- jira - mute the  old ``VarDict`` deprecation (https://github.com/ansible-collections/community.general/pull/8776).
- jira - replace deprecated params when using decorator ``cause_changes`` (https://github.com/ansible-collections/community.general/pull/8791).
- keep_keys filter plugin - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8814).
- keycloak module utils - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8822).
- keycloak_client - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8814).
- keycloak_clientscope - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8814).
- keycloak_identity_provider - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8814).
- keycloak_user_federation - add module argument allowing users to optout of the removal of unspecified mappers, for example to keep the keycloak default mappers (https://github.com/ansible-collections/community.general/pull/8764).
- keycloak_user_federation - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8814).
- keycloak_user_federation - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8822).
- keycloak_user_federation - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8833).
- linode - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8814).
- lxc_container - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8822).
- lxd_container - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8814).
- manageiq_provider - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8814).
- ocapi_utils - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8833).
- one_service - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8814).
- one_vm - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8814).
- onepassword lookup plugin - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8833).
- pids - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8833).
- pipx - added new states ``install_all``, ``uninject``, ``upgrade_shared``, ``pin``, and ``unpin`` (https://github.com/ansible-collections/community.general/pull/8809).
- pipx - added parameter ``global`` to module (https://github.com/ansible-collections/community.general/pull/8793).
- pipx - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8833).
- pipx_info - added parameter ``global`` to module (https://github.com/ansible-collections/community.general/pull/8793).
- pipx_info - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8833).
- pkg5_publisher - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8833).
- proxmox - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8814).
- proxmox_disk - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8814).
- proxmox_kvm - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8814).
- proxmox_kvm - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8822).
- redfish_utils - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8833).
- redfish_utils module utils - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8822).
- redis cache plugin - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8833).
- remove_keys filter plugin - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8814).
- replace_keys filter plugin - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8814).
- scaleway - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8833).
- scaleway module utils - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8822).
- scaleway_compute - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8833).
- scaleway_ip - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8833).
- scaleway_lb - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8833).
- scaleway_security_group - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8822).
- scaleway_security_group - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8833).
- scaleway_user_data - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8833).
- sensu_silence - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8833).
- snmp_facts - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8833).
- sorcery - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8833).
- ufw - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8822).
- unsafe plugin utils - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8814).
- vardict module utils - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8814).
- vars MH module utils - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8814).
- vmadm - replace Python 2.6 construct with dict comprehensions (https://github.com/ansible-collections/community.general/pull/8822).

community.mysql
~~~~~~~~~~~~~~~

- mysql_info - Add ``tls_requires`` returned value for the ``users_info`` filter (https://github.com/ansible-collections/community.mysql/pull/628).
- mysql_info - return a database server engine used (https://github.com/ansible-collections/community.mysql/issues/644).
- mysql_replication - Adds support for `CHANGE REPLICATION SOURCE TO` statement (https://github.com/ansible-collections/community.mysql/issues/635).
- mysql_replication - Adds support for `SHOW BINARY LOG STATUS` and `SHOW BINLOG STATUS` on getprimary mode.
- mysql_replication - Improve detection of IsReplica and IsPrimary by inspecting the dictionary returned from the SQL query instead of relying on variable types. This ensures compatibility with changes in the connector or the output of SHOW REPLICA STATUS and SHOW MASTER STATUS, allowing for easier maintenance if these change in the future.
- mysql_user - Add salt parameter to generate static hash for `caching_sha2_password` and `sha256_password` plugins.

community.postgresql
~~~~~~~~~~~~~~~~~~~~

- postgres - add support for postgres ``infinity`` timestamps by replacing them with ``datetime.min`` / ``datetime.max`` values (https://github.com/ansible-collections/community.postgresql/pull/714).
- postgresql_publication - add the ``tables_in_schema`` argument to implement ``FOR TABLES IN SCHEMA`` feature (https://github.com/ansible-collections/community.postgresql/issues/709).
- postgresql_user - adds the ``configuration`` argument that allows to manage user-specific default configuration (https://github.com/ansible-collections/community.postgresql/issues/598).

community.routeros
~~~~~~~~~~~~~~~~~~

- api_info, api_modify - add support for the ``ip dns adlist`` path implemented by RouterOS 7.15 and newer (https://github.com/ansible-collections/community.routeros/pull/310).
- api_info, api_modify - add support for the ``mld-version`` and ``multicast-querier`` properties in ``interface bridge`` (https://github.com/ansible-collections/community.routeros/pull/315).
- api_info, api_modify - add support for the ``routing filter num-list`` path implemented by RouterOS 7 and newer (https://github.com/ansible-collections/community.routeros/pull/313).
- api_info, api_modify - add support for the ``routing igmp-proxy`` path (https://github.com/ansible-collections/community.routeros/pull/309).
- api_modify, api_info - add read-only ``default`` field to ``snmp community`` (https://github.com/ansible-collections/community.routeros/pull/311).

community.sops
~~~~~~~~~~~~~~

- decrypt filter plugin - now supports the input and output type ``ini`` (https://github.com/ansible-collections/community.sops/pull/204).
- sops lookup plugin - new option ``extract`` allows extracting a single key out of a JSON or YAML file, equivalent to sops' ``decrypt --extract`` (https://github.com/ansible-collections/community.sops/pull/200).
- sops lookup plugin - now supports the input and output type ``ini`` (https://github.com/ansible-collections/community.sops/pull/204).

community.vmware
~~~~~~~~~~~~~~~~

- vmware_vm_vm_drs_rule - added datacenter argument to correctly deal with multiple clusters with same name(https://github.com/ansible-collections/community.vmware/issues/2101).
- vsphere_file - Fix examples in documentation (https://github.com/ansible-collections/community.vmware/issues/2110).

community.windows
~~~~~~~~~~~~~~~~~

- Set minimum supported Ansible version to 2.15 to align with the versions still supported by Asnible.

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

- ome_application_certificate - This module is enhanced to support the upload of certificate chain.

fortinet.fortimanager
~~~~~~~~~~~~~~~~~~~~~

- Supported FortiManager 7.6.0. Added 7 new modules.
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

microsoft.ad
~~~~~~~~~~~~

- Set minimum supported Ansible version to 2.15 to align with the versions still supported by Ansible.
- microsoft.ad.computer - Added the ``do_not_append_dollar_to_sam`` option which can create a computer account without the ``$`` suffix when an explicit ``sam_account_name`` was provided without one.
- microsoft.ad.domain - Added ``reboot_timeout`` option to control how long a reboot can go for.
- microsoft.ad.domain_child - Added ``reboot_timeout`` option to control how long a reboot can go for.
- microsoft.ad.domain_controller - Added ``reboot_timeout`` option to control how long a reboot can go for.
- microsoft.ad.membership - Added ``domain_server`` option to specify the DC to use for domain join operations - https://github.com/ansible-collections/microsoft.ad/issues/131#issuecomment-2201151651
- microsoft.ad.membership - Added ``reboot_timeout`` option to control how long a reboot can go for.

ngine_io.cloudstack
~~~~~~~~~~~~~~~~~~~

- Added possiblity to disable certs validation using ``validate_certs`` argument (https://github.com/ngine-io/ansible-collection-cloudstack/pull/131).
- cs_project - Extended to pass ``cleanup=true`` to the deleteProject API when deleting a project (https://github.com/ngine-io/ansible-collection-cloudstack/pull/122).

purestorage.flasharray
~~~~~~~~~~~~~~~~~~~~~~

- purefa_token - Add ``disable_warnings`` support

theforeman.foreman
~~~~~~~~~~~~~~~~~~

- content_export_* - document that ``chunk_size_gb`` parameter is only applicable for ``importable`` exports (https://github.com/theforeman/foreman-ansible-modules/issues/1738)
- lifecycle_environments role - allow setting ``state`` for the LCE, allowing deletion of existing ones
- location, locations role - add ``description`` parameter to set the description

vmware.vmware
~~~~~~~~~~~~~

- Add action group (https://github.com/ansible-collections/vmware.vmware/pull/59).
- cluster - Added cluster module, which is meant to succeed the community.vmware.vmware_cluster module (https://github.com/ansible-collections/vmware.vmware/pull/60).
- cluster_vcls - Added module to manage vCLS settings, based on community.vmware.vmware_cluster_vcls (https://github.com/ansible-collections/vmware.vmware/pull/61).
- folder_template_from_vm - Use a more robust method when waiting for tasks to complete to improve accuracy (https://github.com/ansible-collections/vmware.vmware/pull/64).

vmware.vmware_rest
~~~~~~~~~~~~~~~~~~

- cluster_moid - updated documentation around lookup plugin usage
- datacenter_moid - updated documentation around lookup plugin usage
- datastore_moid - updated documentation around lookup plugin usage
- folder_moid - updated documentation around lookup plugin usage
- host_moid - updated documentation around lookup plugin usage
- network_moid - updated documentation around lookup plugin usage
- resource_pool_moid - updated documentation around lookup plugin usage
- vm_moid - updated documentation around lookup plugin usage

Deprecated Features
-------------------

amazon.aws
~~~~~~~~~~

- iam_role - support for creating and deleting IAM instance profiles using the ``create_instance_profile`` and ``delete_instance_profile`` options has been deprecated and will be removed in a release after 2026-05-01.  To manage IAM instance profiles the ``amazon.aws.iam_instance_profile`` module can be used instead (https://github.com/ansible-collections/amazon.aws/pull/2221).

community.general
~~~~~~~~~~~~~~~~~

- MH decorator cause_changes module utils - deprecate parameters ``on_success`` and ``on_failure`` (https://github.com/ansible-collections/community.general/pull/8791).
- pipx - support for versions of the command line tool ``pipx`` older than ``1.7.0`` is deprecated and will be removed in community.general 11.0.0 (https://github.com/ansible-collections/community.general/pull/8793).
- pipx_info - support for versions of the command line tool ``pipx`` older than ``1.7.0`` is deprecated and will be removed in community.general 11.0.0 (https://github.com/ansible-collections/community.general/pull/8793).

community.mysql
~~~~~~~~~~~~~~~

- collection - support of mysqlclient connector is deprecated - use PyMySQL connector instead! We will stop testing against it in collection version 4.0.0 and remove the related code in 5.0.0 (https://github.com/ansible-collections/community.mysql/issues/654).
- mysql_info - The ``users_info`` filter returned variable ``plugin_auth_string`` contains the hashed password and it's misleading, it will be removed from community.mysql 4.0.0. Use the `plugin_hash_string` return value instead (https://github.com/ansible-collections/community.mysql/pull/629).
- mysql_user - the ``user`` alias of the ``name`` argument has been deprecated and will be removed in collection version 5.0.0. Use the ``name`` argument instead.

community.vmware
~~~~~~~~~~~~~~~~

- vmware_cluster - the module has been deprecated and will be removed in community.vmware 6.0.0 (https://github.com/ansible-collections/community.vmware/pull/2143).
- vmware_cluster_drs - the module has been deprecated and will be removed in community.vmware 6.0.0 (https://github.com/ansible-collections/community.vmware/pull/2136).
- vmware_cluster_vcls - the module has been deprecated and will be removed in community.vmware 6.0.0 (https://github.com/ansible-collections/community.vmware/pull/2156).

Bugfixes
--------

Ansible-core
~~~~~~~~~~~~

- Fix ``SemanticVersion.parse()`` to store the version string so that ``__repr__`` reports it instead of ``None`` (https://github.com/ansible/ansible/pull/83831).
- Fix an issue where registered variable was not available for templating in ``loop_control.label`` on skipped looped tasks (https://github.com/ansible/ansible/issues/83619)
- Fix for ``meta`` tasks breaking host/fork affinity with ``host_pinned`` strategy (https://github.com/ansible/ansible/issues/83294)
- Fix using the current task's directory for looking up relative paths within roles (https://github.com/ansible/ansible/issues/82695).
- atomic_move - fix using the setgid bit on the parent directory when creating files (https://github.com/ansible/ansible/issues/46742, https://github.com/ansible/ansible/issues/67177).
- connection plugins using the 'extras' option feature would need variables to match the plugin's loaded name, sometimes requiring fqcn, which is not the same as the documented/declared/expected variables. Now we fall back to the 'basename' of the fqcn, but plugin authors can still set the expected value directly.
- csvfile lookup - give an error when no search term is provided using modern config syntax (https://github.com/ansible/ansible/issues/83689).
- include_tasks - Display location when attempting to load a task list where ``include_*`` did not specify any value - https://github.com/ansible/ansible/issues/83874
- powershell - Improve CLIXML decoding to decode all control characters and unicode characters that are encoded as surrogate pairs.
- psrp - Fix bug when attempting to fetch a file path that contains special glob characters like ``[]``
- runtime-metadata sanity test - do not crash on deprecations if ``galaxy.yml`` contains an empty ``version`` field (https://github.com/ansible/ansible/pull/83831).
- ssh - Fix bug when attempting to fetch a file path with characters that should be quoted when using the ``piped`` transfer method

amazon.aws
~~~~~~~~~~

- cloudwatch_metric_alarm - Fix idempotency when creating cloudwatch metric alarm without dimensions (https://github.com/ansible-collections/amazon.aws/pull/1865).
- ec2_instance - fix state processing when exact_count is used (https://github.com/ansible-collections/amazon.aws/pull/1659).
- iam_role - fixes ``EntityAlreadyExists`` exception when ``create_instance_profile`` was set to ``false`` and the instance profile already existed (https://github.com/ansible-collections/amazon.aws/issues/2102).
- iam_role - fixes issue where IAM instance profiles were created when ``create_instance_profile`` was set to ``false`` (https://github.com/ansible-collections/amazon.aws/issues/2281).
- rds_cluster - Limit params sent to api call to DBClusterIdentifier when using state started or stopped (https://github.com/ansible-collections/amazon.aws/issues/2197).
- route53 - modify the return value to return diff only when ``module._diff`` is set to true (https://github.com/ansible-collections/amazon.aws/pull/2136).
- s3_bucket - catch ``UnsupportedArgument`` when calling API ``GetBucketAccelerationConfig`` on region where it is not supported (https://github.com/ansible-collections/amazon.aws/issues/2180).
- s3_bucket - change the default behaviour of the new ``accelerate_enabled`` option to only update the configuration if explicitly passed (https://github.com/ansible-collections/amazon.aws/issues/2220).
- s3_bucket - fixes ``MethodNotAllowed`` exceptions caused by fetching transfer acceleration state in regions that don't support it (https://github.com/ansible-collections/amazon.aws/issues/2266).
- s3_bucket - fixes ``TypeError: cannot unpack non-iterable NoneType object`` errors related to bucket versioning, policies, tags or encryption (https://github.com/ansible-collections/amazon.aws/pull/2228).

ansible.windows
~~~~~~~~~~~~~~~

- setup - Better handle orphaned users when attempting to retrieve ``ansible_machine_id`` - https://github.com/ansible-collections/ansible.windows/issues/606
- win_owner - Try to enable extra privileges if available to set the owner even when the caller may not have explicit rights to do so normally - https://github.com/ansible-collections/ansible.windows/issues/633
- win_powershell - Fix up depth handling on ``$Ansible.Result`` when using a custom ``executable`` - https://github.com/ansible-collections/ansible.windows/issues/642
- win_powershell - increase open timeout for ``executable`` parameter to prevent exceptions on first-run or slower targets. (https://github.com/ansible-collections/ansible.windows/issues/644).
- win_updates - Base64 encode the update wrapper and payload to prevent locale-specific encoding issues.
- win_updates - Handle race condition when ``Wait-Process`` did not handle when the process had ended - https://github.com/ansible-collections/ansible.windows/issues/623

community.dns
~~~~~~~~~~~~~

- Update Public Suffix List.

community.general
~~~~~~~~~~~~~~~~~

- gitlab_group_access_token - fix crash in check mode caused by attempted access to a newly created access token (https://github.com/ansible-collections/community.general/pull/8796).
- gitlab_project - fix ``container_expiration_policy`` not being applied when creating a new project (https://github.com/ansible-collections/community.general/pull/8790).
- gitlab_project - fix crash caused by old Gitlab projects not having a ``container_expiration_policy`` attribute (https://github.com/ansible-collections/community.general/pull/8790).
- gitlab_project_access_token - fix crash in check mode caused by attempted access to a newly created access token (https://github.com/ansible-collections/community.general/pull/8796).
- keycloak_realm_key - fix invalid usage of ``parent_id`` (https://github.com/ansible-collections/community.general/issues/7850, https://github.com/ansible-collections/community.general/pull/8823).
- keycloak_user_federation - fix key error when removing mappers during an update and new mappers are specified in the module args (https://github.com/ansible-collections/community.general/pull/8762).
- keycloak_user_federation - fix the ``UnboundLocalError`` that occurs when an ID is provided for a user federation mapper (https://github.com/ansible-collections/community.general/pull/8831).
- keycloak_user_federation - sort desired and after mapper list by name (analog to before mapper list) to minimize diff and make change detection more accurate (https://github.com/ansible-collections/community.general/pull/8761).
- proxmox inventory plugin - fixed a possible error on concatenating responses from proxmox. In case an API call unexpectedly returned an empty result, the inventory failed with a fatal error. Added check for empty response (https://github.com/ansible-collections/community.general/issues/8798, https://github.com/ansible-collections/community.general/pull/8794).

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

community.postgresql
~~~~~~~~~~~~~~~~~~~~

- postgres - psycopg2 automatically sets the datestyle on the connection to iso whenever it encounters a datestyle configuration it doesn't recognize, but psycopg3 does not. Fix now enforces iso datestyle when using psycopg3 (https://github.com/ansible-collections/community.postgresql/issues/711).

community.vmware
~~~~~~~~~~~~~~~~

- Document dependency on requests (https://github.com/ansible-collections/community.vmware/issues/2127).
- vmware_guest_disk - round size to int, supporting float values properly (https://github.com/ansible-collections/community.vmware/issues/123).
- vmware_guest_snapshot - Update documentation regarding snapshot_id parameter (https://github.com/ansible-collections/community.vmware/issues/2145).

community.windows
~~~~~~~~~~~~~~~~~

- win_mapped_drive - Use correct P/Invoke signature to fix mapped network drives on 32 Bit OS.
- win_mapped_drive - better handle failures when attempting to set mapped drive that already exists but was seen as a local path.

dellemc.enterprise_sonic
~~~~~~~~~~~~~~~~~~~~~~~~

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
- sonic_vlans - Fix exception when gathering facts (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/377).

fortinet.fortimanager
~~~~~~~~~~~~~~~~~~~~~

- Fixed Bug in "fmgr_fact"
- Improved documentation.

google.cloud
~~~~~~~~~~~~

- ansible-lint - remove jinja templates from test assertions
- gcp_kms_filters - add DOCUMENTATION string
- gcp_secret_manager - make an f-string usage backward compatible

microsoft.ad
~~~~~~~~~~~~

- Fix ``microsoft.ad.debug_ldap_client`` documentation problem so it appears in the ``ansible-doc`` plugin list and online documentation.
- Removed usages of the python call ``datetime.datetime.utcnow()`` in favour of ``datetime.datetime.now(datetime.timezone.utc)``. The original method is now deprecated in Python 3.12 and will be removed in a later version.
- group - fix error when creating a group with no members explicitly set - https://github.com/ansible-collections/microsoft.ad/issues/141
- ldap - Filter out managed service accounts in the default LDAP filter used. The ``filter_without_computer`` can be used to disable the default filter if needed.
- membership - allow domain join with hostname change if the account for that host already exists - https://github.com/ansible-collections/microsoft.ad/pull/145
- microsoft.ad.computer - Added fallback ``identity`` lookup for ``sAMAccountName`` with the ``$`` suffix. This ensures that finding the computer object will work with or without the ``$`` suffix. - https://github.com/ansible-collections/microsoft.ad/issues/124
- microsoft.ad.group - Fix setting group members of Builtin groups of a domain controller - https://github.com/ansible-collections/microsoft.ad/issues/130

purestorage.flasharray
~~~~~~~~~~~~~~~~~~~~~~

- purefa_dsrole - Fix version check logic
- purefa_pod - Fix issue with pod not creating correctly
- purefa_subnet - Initialize varaible correctly
- purefa_syslog_settings - Initialize varaible correctly
- purefa_volume - Fixes ``eradicate`` so it doesn't report success when it hasn't actually eradicated
- purefa_volume - Fixes ``volfact`` response when in ``check_mode``
- purefa_volume - Fixes issue where malformed ``volfact`` will cause the ``move`` to apparently fail.

theforeman.foreman
~~~~~~~~~~~~~~~~~~

- callback plugin - correctly catch facts with vault data and replace it with ``ENCRYPTED_VAULT_VALUE_NOT_REPORTED``, preventing ``Object of type AnsibleVaultEncryptedUnicode is not JSON serializable`` errors
- redhat_manifest - do not send empty JSON bodies in GET requests which confuse the portal sometimes (https://github.com/theforeman/foreman-ansible-modules/issues/1768)

vmware.vmware
~~~~~~~~~~~~~

- README - Fix typos in README (https://github.com/ansible-collections/vmware.vmware/pull/66).

Known Issues
------------

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- idrac_diagnostics - Issue(285322) - This module doesn't support export of diagnostics file to HTTP and HTTPS share via SOCKS proxy.
- idrac_firmware - Issue(279282) - This module does not support firmware update using HTTP, HTTPS, and FTP shares with authentication on iDRAC8.
- idrac_storage_volume - Issue(290766) - The module will report success instead of showing failure for new virtual creation on the BOSS-N1 controller if a virtual disk is already present on the same controller.
- idrac_support_assist - Issue(308550) - This module fails when the NFS share path contains sub directory.
- ome_diagnostics - Issue(279193) - Export of SupportAssist collection logs to the share location fails on OME version 4.0.0.
- ome_smart_fabric_uplink - Issue(186024) - The module supported by OpenManage Enterprise Modular, however it does not allow the creation of multiple uplinks of the same name. If an uplink is created using the same name as an existing uplink, then the existing uplink is modified.

New Modules
-----------

community.general
~~~~~~~~~~~~~~~~~

- community.general.keycloak_userprofile - Allows managing Keycloak User Profiles.
- community.general.one_vnet - Manages OpenNebula virtual networks.

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

fortinet.fortimanager
~~~~~~~~~~~~~~~~~~~~~

- fortinet.fortimanager.fmgr_fmg_sasemanager_settings - Fmg sase manager settings
- fortinet.fortimanager.fmgr_fmg_sasemanager_status - Fmg sase manager status
- fortinet.fortimanager.fmgr_pm_config_pblock_firewall_proxypolicy - Configure proxy policies.
- fortinet.fortimanager.fmgr_pm_config_pblock_firewall_proxypolicy_sectionvalue - Configure proxy policies.
- fortinet.fortimanager.fmgr_system_admin_user_policyblock - Policy block write access.
- fortinet.fortimanager.fmgr_system_fmgcluster - fmg clsuter.
- fortinet.fortimanager.fmgr_system_fmgcluster_peer - Peer.

microsoft.ad
~~~~~~~~~~~~

- microsoft.ad.service_account - Manage Active Directory service account objects

purestorage.flasharray
~~~~~~~~~~~~~~~~~~~~~~

- purestorage.flasharray.purefa_dsrole_old - Configure FlashArray Directory Service Roles (pre-6.6.3)

Unchanged Collections
---------------------

- ansible.netcommon (still version 6.1.3)
- ansible.posix (still version 1.5.4)
- ansible.utils (still version 4.1.0)
- arista.eos (still version 9.0.0)
- awx.awx (still version 24.6.1)
- check_point.mgmt (still version 5.2.3)
- chocolatey.chocolatey (still version 1.5.1)
- cisco.aci (still version 2.10.1)
- cisco.asa (still version 5.0.1)
- cisco.ios (still version 8.0.0)
- cisco.iosxr (still version 9.0.0)
- cisco.ise (still version 2.9.3)
- cisco.meraki (still version 2.18.1)
- cisco.mso (still version 2.9.0)
- cisco.nxos (still version 8.1.0)
- cloud.common (still version 3.0.0)
- cloudscale_ch.cloud (still version 2.4.0)
- community.aws (still version 8.0.0)
- community.ciscosmb (still version 1.0.9)
- community.docker (still version 3.12.1)
- community.grafana (still version 1.9.1)
- community.hashi_vault (still version 6.2.0)
- community.hrobot (still version 2.0.1)
- community.library_inventory_filtering_v1 (still version 1.0.1)
- community.libvirt (still version 1.3.0)
- community.mongodb (still version 1.7.6)
- community.network (still version 5.0.3)
- community.okd (still version 3.0.1)
- community.proxysql (still version 1.6.0)
- community.rabbitmq (still version 1.3.0)
- community.sap_libs (still version 1.4.2)
- community.zabbix (still version 2.5.1)
- containers.podman (still version 1.15.4)
- cyberark.conjur (still version 1.3.0)
- cyberark.pas (still version 1.0.27)
- dellemc.powerflex (still version 2.5.0)
- dellemc.unity (still version 2.0.0)
- f5networks.f5_modules (still version 1.30.1)
- fortinet.fortios (still version 2.3.7)
- frr.frr (still version 2.0.2)
- hetzner.hcloud (still version 3.1.1)
- ibm.qradar (still version 3.0.0)
- ibm.spectrum_virtualize (still version 2.0.0)
- ibm.storage_virtualize (still version 2.4.1)
- ieisystem.inmanage (still version 2.0.0)
- infinidat.infinibox (still version 1.4.5)
- infoblox.nios_modules (still version 1.6.1)
- inspur.ispim (still version 2.2.3)
- inspur.sm (still version 2.3.0)
- junipernetworks.junos (still version 8.0.0)
- kaytus.ksmanage (still version 1.2.2)
- kubernetes.core (still version 3.2.0)
- kubevirt.core (still version 1.5.0)
- lowlydba.sqlserver (still version 2.3.3)
- netapp.cloudmanager (still version 21.22.1)
- netapp.ontap (still version 22.12.0)
- netapp.storagegrid (still version 21.12.0)
- netapp_eseries.santricity (still version 1.4.0)
- netbox.netbox (still version 3.19.1)
- ngine_io.exoscale (still version 1.1.0)
- openstack.cloud (still version 2.2.0)
- openvswitch.openvswitch (still version 2.1.1)
- ovirt.ovirt (still version 3.2.0)
- purestorage.flashblade (still version 1.18.0)
- sensu.sensu_go (still version 1.14.0)
- splunk.es (still version 3.0.0)
- t_systems_mms.icinga_director (still version 2.0.1)
- telekom_mms.icinga_director (still version 2.1.2)
- vultr.cloud (still version 1.13.0)
- vyos.vyos (still version 4.1.0)

v10.3.0
=======

.. contents::
  :local:
  :depth: 2

Release Summary
---------------

Release Date: 2024-08-13

`Porting Guide <https://docs.ansible.com/ansible/devel/porting_guides.html>`_

Ansible-core
------------

Ansible 10.3.0 contains ansible-core version 2.17.3.
This is a newer version than version 2.17.2 contained in the previous Ansible release.

The changes are reported in the combined changelog below.

Changed Collections
-------------------

If not mentioned explicitly, the changes are reported in the combined changelog below.

+------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| Collection             | Ansible 10.2.0 | Ansible 10.3.0 | Notes                                                                                                                        |
+========================+================+================+==============================================================================================================================+
| cisco.dnac             | 6.16.0         | 6.17.1         |                                                                                                                              |
+------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.intersight       | 2.0.9          | 2.0.10         | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.ise              | 2.9.2          | 2.9.3          |                                                                                                                              |
+------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.mso              | 2.8.0          | 2.9.0          |                                                                                                                              |
+------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| cloudscale_ch.cloud    | 2.3.1          | 2.4.0          |                                                                                                                              |
+------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.crypto       | 2.21.0         | 2.21.1         |                                                                                                                              |
+------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.dns          | 3.0.2          | 3.0.3          |                                                                                                                              |
+------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.docker       | 3.11.0         | 3.12.1         |                                                                                                                              |
+------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.general      | 9.2.0          | 9.3.0          |                                                                                                                              |
+------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.mongodb      | 1.7.5          | 1.7.6          | There are no changes recorded in the changelog.                                                                              |
+------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.routeros     | 2.17.0         | 2.18.0         |                                                                                                                              |
+------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.sops         | 1.8.0          | 1.8.2          |                                                                                                                              |
+------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| cyberark.pas           | 1.0.25         | 1.0.27         | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| dellemc.openmanage     | 9.4.0          | 9.5.0          |                                                                                                                              |
+------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| f5networks.f5_modules  | 1.29.0         | 1.30.1         |                                                                                                                              |
+------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| fortinet.fortimanager  | 2.5.0          | 2.6.0          |                                                                                                                              |
+------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| grafana.grafana        | 5.3.0          | 5.4.0          |                                                                                                                              |
+------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| netapp.ontap           | 22.11.0        | 22.12.0        |                                                                                                                              |
+------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| purestorage.flasharray | 1.30.0         | 1.30.2         |                                                                                                                              |
+------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| purestorage.flashblade | 1.17.0         | 1.18.0         |                                                                                                                              |
+------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| theforeman.foreman     | 4.0.0          | 4.1.0          |                                                                                                                              |
+------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| vmware.vmware          | 1.3.0          | 1.4.0          |                                                                                                                              |
+------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+

Minor Changes
-------------

Ansible-core
~~~~~~~~~~~~

- ansible-test - Improve the error message shown when an unknown ``--remote`` or ``--docker`` option is given.
- ansible-test - Removed the ``vyos/1.1.8`` network remote as it is no longer functional.

cisco.dnac
~~~~~~~~~~

- Added 'accesspoint_workflow_manager' module to manage access point configurations.
- Added 'rma_workflow_manager' module to manage RMA workflow.
- Added 'user_role_workflow_manager' module to manage operations to create, update, and delete users and roles.
- Added Circle CI support for integration testing.
- Adding pyzipper support in device_configs workflow manager module.
- Adding run_compliance_batch_size support in network_compliance module.
- Changes in provision workflow manager module.
- Checking the device list in swim workflow manager module.
- Exporting export_device_details_limit in inventory workflow module.
- Fix family name from userand_roles to user_and_roles.
- UT and IT cases for worflow manager modules.

cisco.mso
~~~~~~~~~

- Add new module ndo_schema_template_bd_dhcp_policy to support BD DHCP Policy configuration in NDO version 4.1 and later
- Add support to use an APIC DN as VRF reference in mso_schema_site_bd_l3out

cloudscale_ch.cloud
~~~~~~~~~~~~~~~~~~~

- Update source_format of custom images with actually available choices.

community.docker
~~~~~~~~~~~~~~~~

- docker, docker_api connection plugins - allow to determine the working directory when executing commands with the new ``working_dir`` option (https://github.com/ansible-collections/community.docker/pull/943).
- docker, docker_api connection plugins - allow to execute commands with extended privileges with the new ``privileges`` option (https://github.com/ansible-collections/community.docker/pull/943).
- docker, docker_api connection plugins - allow to pass extra environment variables when executing commands with the new ``extra_env`` option (https://github.com/ansible-collections/community.docker/issues/937, https://github.com/ansible-collections/community.docker/pull/940).
- docker_compose_v2* modules - support Docker Compose 2.29.0's ``json`` progress writer to avoid having to parse text output (https://github.com/ansible-collections/community.docker/pull/931).
- docker_compose_v2_pull - add new options ``ignore_buildable``, ``include_deps``, and ``services`` (https://github.com/ansible-collections/community.docker/issues/941, https://github.com/ansible-collections/community.docker/pull/942).
- docker_container - when creating a container, directly pass all networks to connect to to the Docker Daemon for API version 1.44 and newer. This makes creation more efficient and works around a bug in Docker Daemon that does not use the specified MAC address in at least some cases, though only for creation (https://github.com/ansible-collections/community.docker/pull/933).

community.general
~~~~~~~~~~~~~~~~~

- cgroup_memory_recap, hipchat, jabber, log_plays, loganalytics, logentries, logstash, slack, splunk, sumologic, syslog_json callback plugins - make sure that all options are typed (https://github.com/ansible-collections/community.general/pull/8628).
- chef_databag, consul_kv, cyberarkpassword, dsv, etcd, filetree, hiera, onepassword, onepassword_doc, onepassword_raw, passwordstore, redis, shelvefile, tss lookup plugins - make sure that all options are typed (https://github.com/ansible-collections/community.general/pull/8626).
- chroot, funcd, incus, iocage, jail, lxc, lxd, qubes, zone connection plugins - make sure that all options are typed (https://github.com/ansible-collections/community.general/pull/8627).
- cobbler, linode, lxd, nmap, online, scaleway, stackpath_compute, virtualbox inventory plugins - make sure that all options are typed (https://github.com/ansible-collections/community.general/pull/8625).
- doas, dzdo, ksu, machinectl, pbrun, pfexec, pmrun, sesu, sudosu become plugins - make sure that all options are typed (https://github.com/ansible-collections/community.general/pull/8623).
- gconftool2 - make use of ``ModuleHelper`` features to simplify code (https://github.com/ansible-collections/community.general/pull/8711).
- gitlab_project - add option ``container_expiration_policy`` to schedule container registry cleanup (https://github.com/ansible-collections/community.general/pull/8674).
- gitlab_project - add option ``model_registry_access_level`` to disable model registry (https://github.com/ansible-collections/community.general/pull/8688).
- gitlab_project - add option ``pages_access_level`` to disable project pages (https://github.com/ansible-collections/community.general/pull/8688).
- gitlab_project - add option ``repository_access_level`` to disable project repository (https://github.com/ansible-collections/community.general/pull/8674).
- gitlab_project - add option ``service_desk_enabled`` to disable service desk (https://github.com/ansible-collections/community.general/pull/8688).
- locale_gen - add support for multiple locales (https://github.com/ansible-collections/community.general/issues/8677, https://github.com/ansible-collections/community.general/pull/8682).
- memcached, pickle, redis, yaml cache plugins - make sure that all options are typed (https://github.com/ansible-collections/community.general/pull/8624).
- opentelemetry callback plugin - fix default value for ``store_spans_in_file`` causing traces to be produced to a file named ``None`` (https://github.com/ansible-collections/community.general/issues/8566, https://github.com/ansible-collections/community.general/pull/8741).
- passwordstore lookup plugin - add the current user to the lockfile file name to address issues on multi-user systems (https://github.com/ansible-collections/community.general/pull/8689).
- pipx - add parameter ``suffix`` to module (https://github.com/ansible-collections/community.general/pull/8675, https://github.com/ansible-collections/community.general/issues/8656).
- pkgng - add option ``use_globs`` (default ``true``) to optionally disable glob patterns (https://github.com/ansible-collections/community.general/issues/8632, https://github.com/ansible-collections/community.general/pull/8633).
- proxmox inventory plugin - add new fact for LXC interface details (https://github.com/ansible-collections/community.general/pull/8713).
- redis, redis_info - add ``client_cert`` and ``client_key`` options to specify path to certificate for Redis authentication  (https://github.com/ansible-collections/community.general/pull/8654).

community.routeros
~~~~~~~~~~~~~~~~~~

- api_info - allow to restrict the output by limiting fields to specific values with the new ``restrict`` option (https://github.com/ansible-collections/community.routeros/pull/305).
- api_info, api_modify - add support for the ``ip dhcp-server matcher`` path (https://github.com/ansible-collections/community.routeros/pull/300).
- api_info, api_modify - add support for the ``ipv6 nd prefix`` path (https://github.com/ansible-collections/community.routeros/pull/303).
- api_info, api_modify - add support for the ``name`` and ``is-responder`` properties under the ``interface wireguard peers`` path introduced in RouterOS 7.15 (https://github.com/ansible-collections/community.routeros/pull/304).
- api_info, api_modify - add support for the ``routing ospf static-neighbor`` path in RouterOS 7 (https://github.com/ansible-collections/community.routeros/pull/302).
- api_info, api_modify - set default for ``force`` in ``ip dhcp-server option`` to an explicit ``false`` (https://github.com/ansible-collections/community.routeros/pull/300).
- api_modify - allow to restrict what is updated by limiting fields to specific values with the new ``restrict`` option (https://github.com/ansible-collections/community.routeros/pull/305).

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- idrac_redfish_powerstate - This module is enhanced to support full virtual A/C power cycle.
- idrac_redfish_storage_controller - This module is enhanced to support secure and/or cryptographic erase of the physical disk.
- ome_application_network_proxy - This module is enhanced to manage the Proxy Exclusion List and Certificate Validation.

f5networks.f5_modules
~~~~~~~~~~~~~~~~~~~~~

- bigip_ucs - Fix for bigip_ucs module to restore UCS file on BIG-IP devices.

fortinet.fortimanager
~~~~~~~~~~~~~~~~~~~~~

- Supported FortiManager 7.4.3. 7 new modules.
- Supported ansible-core 2.17.

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

purestorage.flashblade
~~~~~~~~~~~~~~~~~~~~~~

- all - add ``disable_warnings`` parameters
- purefb_bucket - Add ``safemode`` option for ``retention_mode``
- purefb_certs - Update module to use REST v2 code. This brings in new parameters for certificate management.
- purefb_fs - Set default for group_ownership to be creator
- purefb_ra - Add ``duration`` option from REST 2.14
- purefb_ra - Update to REST2

theforeman.foreman
~~~~~~~~~~~~~~~~~~

- redhat_manifest - report ``changed`` when manifest is regenerated and downloaded (https://github.com/theforeman/foreman-ansible-modules/issues/1473)

vmware.vmware
~~~~~~~~~~~~~

- cluster_drs - added cluster_drs module to manage DRS settings in vcenter
- folder_template_from_vm - add module and tests to create a template from an existing VM in vcenter and store the template in a folder
- guest_info - migrated functionality from community vmware_guest_info and vmware_vm_info into guest_info. Changes are backwards compatible but legacy outputs are deprecated
- module_utils/vmware_tasks - added shared utils to monitor long running tasks in vcenter
- module_utils/vmware_type_utils - added shared utils for validating, transforming, and comparing vcenter settings with python variables
- vm_portgroup_info - add module to get all the portgroups that associated with VMs

Deprecated Features
-------------------

community.docker
~~~~~~~~~~~~~~~~

- The collection deprecates support for all ansible-core versions that are currently End of Life, `according to the ansible-core support matrix <https://docs.ansible.com/ansible-core/devel/reference_appendices/release_and_maintenance.html#ansible-core-support-matrix>`__. This means that the next major release of the collection will no longer support ansible-core 2.11, ansible-core 2.12, ansible-core 2.13, and ansible-core 2.14.

community.routeros
~~~~~~~~~~~~~~~~~~

- The collection deprecates support for all Ansible/ansible-base/ansible-core versions that are currently End of Life, `according to the ansible-core support matrix <https://docs.ansible.com/ansible-core/devel/reference_appendices/release_and_maintenance.html#ansible-core-support-matrix>`__. This means that the next major release of the collection will no longer support Ansible 2.9, ansible-base 2.10, ansible-core 2.11, ansible-core 2.12, ansible-core 2.13, and ansible-core 2.14.

community.sops
~~~~~~~~~~~~~~

- The collection deprecates support for all Ansible/ansible-base/ansible-core versions that are currently End of Life, `according to the ansible-core support matrix <https://docs.ansible.com/ansible-core/devel/reference_appendices/release_and_maintenance.html#ansible-core-support-matrix>`__. This means that the next major release of the collection will no longer support Ansible 2.9, ansible-base 2.10, ansible-core 2.11, ansible-core 2.12, ansible-core 2.13, and ansible-core 2.14.

Bugfixes
--------

Ansible-core
~~~~~~~~~~~~

- Warning now includes filename and line number of variable when specifying a list of dictionaries for vars (https://github.com/ansible/ansible/issues/82528).
- config, restored the ability to set module compression via a variable
- debconf - fix normalization of value representation for boolean vtypes in new packages (https://github.com/ansible/ansible/issues/83594)
- linear strategy: fix handlers included via ``include_tasks`` handler to be executed in lockstep (https://github.com/ansible/ansible/issues/83019)

cisco.ise
~~~~~~~~~

- endpoint_group - add missing parameter parentID.
- mnt_session_active_list_info - fix response xml.
- network_device - mask param can be string or int, cast to int at the end.
- reservation - remove duplicate parameter.
- support_bundle_download - remove duplicate parameter.
- trusted_certificate - fix comparison between request and current object.

cisco.mso
~~~~~~~~~

- Fix to be able to reference APIC only L3Out in mso_schema_site_external_epg

community.crypto
~~~~~~~~~~~~~~~~

- When using cryptography >= 43.0.0, use offset-aware ``datetime.datetime`` objects (with timezone UTC) instead of offset-naive UTC timestamps for the ``InvalidityDate`` X.509 CRL extension (https://github.com/ansible-collections/community.crypto/issues/726, https://github.com/ansible-collections/community.crypto/pull/730).

community.dns
~~~~~~~~~~~~~

- Update Public Suffix List.

community.docker
~~~~~~~~~~~~~~~~

- docker_compose_v2 - handle yet another random unstructured error output from pre-2.29.0 Compose versions (https://github.com/ansible-collections/community.docker/issues/948, https://github.com/ansible-collections/community.docker/pull/949).
- docker_compose_v2 - make sure that services provided in ``services`` are appended to the command line after ``--`` and not before it (https://github.com/ansible-collections/community.docker/pull/942).
- docker_compose_v2* modules, docker_image_build - provide better error message when required fields are not present in ``docker version`` or ``docker info`` output. This can happen if Podman is used instead of Docker (https://github.com/ansible-collections/community.docker/issues/891, https://github.com/ansible-collections/community.docker/pull/935).
- docker_container - fix idempotency if ``network_mode=default`` and Docker 26.1.0 or later is used. There was a breaking change in Docker 26.1.0 regarding normalization of ``NetworkMode`` (https://github.com/ansible-collections/community.docker/issues/934, https://github.com/ansible-collections/community.docker/pull/936).
- docker_container - restore behavior of the module from community.docker 2.x.y that passes the first network to the Docker Deamon while creating the container (https://github.com/ansible-collections/community.docker/pull/933).
- docker_image_build - fix ``--output`` parameter composition for ``type=docker`` and ``type=image`` (https://github.com/ansible-collections/community.docker/issues/946, https://github.com/ansible-collections/community.docker/pull/947).

community.general
~~~~~~~~~~~~~~~~~

- gitlab_runner - fix ``paused`` parameter being ignored (https://github.com/ansible-collections/community.general/pull/8648).
- homebrew_cask - fix ``upgrade_all`` returns ``changed`` when nothing upgraded (https://github.com/ansible-collections/community.general/issues/8707, https://github.com/ansible-collections/community.general/pull/8708).
- keycloak_user_federation - get cleartext IDP ``clientSecret`` from full realm info to detect changes to it (https://github.com/ansible-collections/community.general/issues/8294, https://github.com/ansible-collections/community.general/pull/8735).
- keycloak_user_federation - remove existing user federation mappers if they are not present in the federation configuration and will not be updated (https://github.com/ansible-collections/community.general/issues/7169, https://github.com/ansible-collections/community.general/pull/8695).
- proxmox - fixed an issue where the new volume handling incorrectly converted ``null`` values into ``"None"`` strings (https://github.com/ansible-collections/community.general/pull/8646).
- proxmox - fixed an issue where volume strings where overwritten instead of appended to in the new ``build_volume()`` method (https://github.com/ansible-collections/community.general/pull/8646).
- proxmox - removed the forced conversion of non-string values to strings to be consistent with the module documentation (https://github.com/ansible-collections/community.general/pull/8646).

community.routeros
~~~~~~~~~~~~~~~~~~

- api_modify, api_info - change the default of ``ingress-filtering`` in paths ``interface bridge`` and ``interface bridge port`` back to ``false`` for RouterOS before version 7 (https://github.com/ansible-collections/community.routeros/pull/305).

community.sops
~~~~~~~~~~~~~~

- Pass ``config_path`` on SOPS 3.9.0 before the subcommand instead of after it (https://github.com/ansible-collections/community.sops/issues/195, https://github.com/ansible-collections/community.sops/pull/197).

fortinet.fortimanager
~~~~~~~~~~~~~~~~~~~~~

- Added more description in the documentation.
- Deleted 9 fmgr_switchcontroller_managedswitch_* modules. Will support them in FortiManager Device Ansible.
- Improved fmgr_fact, fmgr_clone, fmgr_move.

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

purestorage.flasharray
~~~~~~~~~~~~~~~~~~~~~~

- purefa_dsrole - Fix function name typo
- purefa_info - Fixed issue trying to collect deleted volumes perfomance stats
- purefa_pg - Fix parameter name typo
- purefa_volume - Fix issue with creating volume using old Purity version (6.1.19)

purestorage.flashblade
~~~~~~~~~~~~~~~~~~~~~~

- purefb_fs - Fix conflict with SMB mode and ACL safeguarding
- purefb_fs - Fix error checking for SMB parameter in non-SMB filesystem
- purefb_info - Fix space reporting issue

vmware.vmware
~~~~~~~~~~~~~

- _vmware_facts - fixed typo in hw_interfaces fact key and added missing annotation fact key and value
- _vmware_folder_paths - fixed issue where resolved folder paths incorrectly included a leading slash
- guest_info - added more optional attributes to the example
- module_utils/vmware_rest_client - rename get_vm_by_name method as there is same signature already

Known Issues
------------

community.docker
~~~~~~~~~~~~~~~~

- docker_container - when specifying a MAC address for a container's network, and the network is attached after container creation (for example, due to idempotency checks), the MAC address is at least in some cases ignored by the Docker Daemon (https://github.com/ansible-collections/community.docker/pull/933).

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- idrac_diagnostics - Issue(285322) - This module doesn't support export of diagnostics file to HTTP and HTTPS share via SOCKS proxy.
- idrac_firmware - Issue(279282) - This module does not support firmware update using HTTP, HTTPS, and FTP shares with authentication on iDRAC8.
- idrac_storage_volume - Issue(290766) - The module will report success instead of showing failure for new virtual creation on the BOSS-N1 controller if a virtual disk is already present on the same controller.
- ome_diagnostics - Issue(279193) - Export of SupportAssist collection logs to the share location fails on OME version 4.0.0.
- ome_smart_fabric_uplink - Issue(186024) - The module supported by OpenManage Enterprise Modular, however it does not allow the creation of multiple uplinks of the same name. If an uplink is created using the same name as an existing uplink, then the existing uplink is modified.

New Modules
-----------

community.general
~~~~~~~~~~~~~~~~~

- community.general.bootc_manage - Bootc Switch and Upgrade.
- community.general.homebrew_services - Services manager for Homebrew.
- community.general.keycloak_realm_keys_metadata_info - Allows obtaining Keycloak realm keys metadata via Keycloak API.

fortinet.fortimanager
~~~~~~~~~~~~~~~~~~~~~

- fortinet.fortimanager.fmgr_extensioncontroller_extenderprofile_wifi - FortiExtender wifi configuration.
- fortinet.fortimanager.fmgr_extensioncontroller_extenderprofile_wifi_radio1 - Radio-1 config for Wi-Fi 2.
- fortinet.fortimanager.fmgr_extensioncontroller_extenderprofile_wifi_radio2 - Radio-2 config for Wi-Fi 5GHz
- fortinet.fortimanager.fmgr_firewall_sslsshprofile_echoutersni - ClientHelloOuter SNIs to be blocked.
- fortinet.fortimanager.fmgr_system_log_ueba - UEBAsettings.
- fortinet.fortimanager.fmgr_system_npu_icmpratectrl - Configure the rate of ICMP messages generated by this FortiGate.
- fortinet.fortimanager.fmgr_user_externalidentityprovider - Configure external identity provider.

theforeman.foreman
~~~~~~~~~~~~~~~~~~

- theforeman.foreman.content_import_info - List content imports
- theforeman.foreman.content_import_library - Manage library content imports
- theforeman.foreman.content_import_repository - Manage repository content imports
- theforeman.foreman.content_import_version - Manage content view version content imports

vmware.vmware
~~~~~~~~~~~~~

- vmware.vmware.vm_portgroup_info - Returns information about the portgroups of virtual machines

Unchanged Collections
---------------------

- amazon.aws (still version 8.1.0)
- ansible.netcommon (still version 6.1.3)
- ansible.posix (still version 1.5.4)
- ansible.utils (still version 4.1.0)
- ansible.windows (still version 2.4.0)
- arista.eos (still version 9.0.0)
- awx.awx (still version 24.6.1)
- azure.azcollection (still version 2.6.0)
- check_point.mgmt (still version 5.2.3)
- chocolatey.chocolatey (still version 1.5.1)
- cisco.aci (still version 2.10.1)
- cisco.asa (still version 5.0.1)
- cisco.ios (still version 8.0.0)
- cisco.iosxr (still version 9.0.0)
- cisco.meraki (still version 2.18.1)
- cisco.nxos (still version 8.1.0)
- cisco.ucs (still version 1.10.0)
- cloud.common (still version 3.0.0)
- community.aws (still version 8.0.0)
- community.ciscosmb (still version 1.0.9)
- community.digitalocean (still version 1.26.0)
- community.grafana (still version 1.9.1)
- community.hashi_vault (still version 6.2.0)
- community.hrobot (still version 2.0.1)
- community.library_inventory_filtering_v1 (still version 1.0.1)
- community.libvirt (still version 1.3.0)
- community.mysql (still version 3.9.0)
- community.network (still version 5.0.3)
- community.okd (still version 3.0.1)
- community.postgresql (still version 3.4.1)
- community.proxysql (still version 1.6.0)
- community.rabbitmq (still version 1.3.0)
- community.sap_libs (still version 1.4.2)
- community.vmware (still version 4.5.0)
- community.windows (still version 2.2.0)
- community.zabbix (still version 2.5.1)
- containers.podman (still version 1.15.4)
- cyberark.conjur (still version 1.3.0)
- dellemc.enterprise_sonic (still version 2.4.0)
- dellemc.powerflex (still version 2.5.0)
- dellemc.unity (still version 2.0.0)
- fortinet.fortios (still version 2.3.7)
- frr.frr (still version 2.0.2)
- google.cloud (still version 1.3.0)
- hetzner.hcloud (still version 3.1.1)
- ibm.qradar (still version 3.0.0)
- ibm.spectrum_virtualize (still version 2.0.0)
- ibm.storage_virtualize (still version 2.4.1)
- ieisystem.inmanage (still version 2.0.0)
- infinidat.infinibox (still version 1.4.5)
- infoblox.nios_modules (still version 1.6.1)
- inspur.ispim (still version 2.2.3)
- inspur.sm (still version 2.3.0)
- junipernetworks.junos (still version 8.0.0)
- kaytus.ksmanage (still version 1.2.2)
- kubernetes.core (still version 3.2.0)
- kubevirt.core (still version 1.5.0)
- lowlydba.sqlserver (still version 2.3.3)
- microsoft.ad (still version 1.6.0)
- netapp.cloudmanager (still version 21.22.1)
- netapp.storagegrid (still version 21.12.0)
- netapp_eseries.santricity (still version 1.4.0)
- netbox.netbox (still version 3.19.1)
- ngine_io.cloudstack (still version 2.3.0)
- ngine_io.exoscale (still version 1.1.0)
- openstack.cloud (still version 2.2.0)
- openvswitch.openvswitch (still version 2.1.1)
- ovirt.ovirt (still version 3.2.0)
- sensu.sensu_go (still version 1.14.0)
- splunk.es (still version 3.0.0)
- t_systems_mms.icinga_director (still version 2.0.1)
- telekom_mms.icinga_director (still version 2.1.2)
- vmware.vmware_rest (still version 3.0.1)
- vultr.cloud (still version 1.13.0)
- vyos.vyos (still version 4.1.0)
- wti.remote (still version 1.0.5)

v10.2.0
=======

.. contents::
  :local:
  :depth: 2

Release Summary
---------------

Release Date: 2024-07-16

`Porting Guide <https://docs.ansible.com/ansible/devel/porting_guides.html>`_

Added Collections
-----------------

- kubevirt.core (version 1.5.0)
- vmware.vmware (version 1.3.0)

Ansible-core
------------

Ansible 10.2.0 contains ansible-core version 2.17.2.
This is a newer version than version 2.17.1 contained in the previous Ansible release.

The changes are reported in the combined changelog below.

Changed Collections
-------------------

If not mentioned explicitly, the changes are reported in the combined changelog below.

+------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| Collection             | Ansible 10.1.0 | Ansible 10.2.0 | Notes                                                                                                                        |
+========================+================+================+==============================================================================================================================+
| amazon.aws             | 8.0.1          | 8.1.0          |                                                                                                                              |
+------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| awx.awx                | 24.5.0         | 24.6.1         | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| azure.azcollection     | 2.4.0          | 2.6.0          | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.aci              | 2.9.0          | 2.10.1         |                                                                                                                              |
+------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.mso              | 2.6.0          | 2.8.0          |                                                                                                                              |
+------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.crypto       | 2.20.0         | 2.21.0         |                                                                                                                              |
+------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.dns          | 3.0.1          | 3.0.2          |                                                                                                                              |
+------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.docker       | 3.10.4         | 3.11.0         |                                                                                                                              |
+------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.general      | 9.1.0          | 9.2.0          |                                                                                                                              |
+------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.mongodb      | 1.7.4          | 1.7.5          | There are no changes recorded in the changelog.                                                                              |
+------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.proxysql     | 1.5.1          | 1.6.0          |                                                                                                                              |
+------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.routeros     | 2.16.0         | 2.17.0         |                                                                                                                              |
+------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.sops         | 1.6.7          | 1.8.0          |                                                                                                                              |
+------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.vmware       | 4.4.0          | 4.5.0          |                                                                                                                              |
+------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| containers.podman      | 1.15.2         | 1.15.4         |                                                                                                                              |
+------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| dellemc.openmanage     | 9.3.0          | 9.4.0          |                                                                                                                              |
+------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| f5networks.f5_modules  | 1.28.0         | 1.29.0         |                                                                                                                              |
+------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| fortinet.fortios       | 2.3.6          | 2.3.7          |                                                                                                                              |
+------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| grafana.grafana        | 5.2.0          | 5.3.0          |                                                                                                                              |
+------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| ibm.storage_virtualize | 2.3.1          | 2.4.1          |                                                                                                                              |
+------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| kubevirt.core          |                | 1.5.0          | The collection was added to Ansible                                                                                          |
+------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| purestorage.flasharray | 1.28.1         | 1.30.0         |                                                                                                                              |
+------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| vmware.vmware          |                | 1.3.0          | The collection was added to Ansible                                                                                          |
+------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+

Major Changes
-------------

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- idrac_server_config_profile - This module is enhanced to allow you to export and import custom defaults on iDRAC.
- ome_configuration_compliance_baseline - This module is enhanced to schedule the remediation job and stage the reboot.

fortinet.fortios
~~~~~~~~~~~~~~~~

- Add a sanity_test.yaml file to trigger CI tests in GitHub.
- Support Ansible-core 2.17.
- Support new FOS versions 7.4.4.

grafana.grafana
~~~~~~~~~~~~~~~

- Add a config check before restarting mimir by @panfantastic in https://github.com/grafana/grafana-ansible-collection/pull/198
- Add support for configuring feature_toggles in grafana role by @LexVar in https://github.com/grafana/grafana-ansible-collection/pull/173
- Backport post-setup healthcheck from agent to alloy by @v-zhuravlev in https://github.com/grafana/grafana-ansible-collection/pull/213
- Bump ansible-lint from 24.2.3 to 24.5.0 by @dependabot in https://github.com/grafana/grafana-ansible-collection/pull/207
- Bump ansible-lint from 24.5.0 to 24.6.0 by @dependabot in https://github.com/grafana/grafana-ansible-collection/pull/216
- Bump braces from 3.0.2 to 3.0.3 in the npm_and_yarn group across 1 directory by @dependabot in https://github.com/grafana/grafana-ansible-collection/pull/218
- Bump pylint from 3.1.0 to 3.1.1 by @dependabot in https://github.com/grafana/grafana-ansible-collection/pull/200
- Bump pylint from 3.1.1 to 3.2.2 by @dependabot in https://github.com/grafana/grafana-ansible-collection/pull/208
- Bump pylint from 3.2.2 to 3.2.3 by @dependabot in https://github.com/grafana/grafana-ansible-collection/pull/217
- Bump pylint from 3.2.3 to 3.2.5 by @dependabot in https://github.com/grafana/grafana-ansible-collection/pull/234
- Change from config.river to config.alloy by @cardasac in https://github.com/grafana/grafana-ansible-collection/pull/225
- Fix Grafana Configuration for Unified and Legacy Alerting Based on Version by @voidquark in https://github.com/grafana/grafana-ansible-collection/pull/215
- Support adding alloy user to extra groups by @v-zhuravlev in https://github.com/grafana/grafana-ansible-collection/pull/212
- Updated result.json['message'] to result.json()['message'] by @CPreun in https://github.com/grafana/grafana-ansible-collection/pull/223

Minor Changes
-------------

amazon.aws
~~~~~~~~~~

- s3_bucket - Add ``object_lock_default_retention`` to set Object Lock default retention configuration for S3 buckets (https://github.com/ansible-collections/amazon.aws/pull/2062).
- s3_bucket - Add support for enabling Amazon S3 Transfer Acceleration by setting the ``accelerate_enabled`` option (https://github.com/ansible-collections/amazon.aws/pull/2046).

cisco.aci
~~~~~~~~~

- Add aci_esg_to_contract module for esg contract relationship objects fvRsCons (consumer), fvRsConsIf (consumer interface), fvRsProv (provider) and fvRsIntraEpg (intra_esg)
- Add aci_system_connectivity_preference module (#601)
- Added suppress-previous flag option to reduce the number of API calls. (#636)
- Enable relative path and/or filename of private key for the aci httpapi plugin.

cisco.mso
~~~~~~~~~

- Add module mso_schema_template_vrf_rp to support multicast vrf rp in application templates
- Add module ndo_dhcp_option_policy to support dhcp option policy configuration in tenant templates
- Add module ndo_dhcp_relay_policy to support dhcp relay policy configuration in tenant templates
- Add module ndo_l3_domain and ndo_physical_domain to support domain configuration in fabric policy templates
- Add module ndo_vlan_pool to support vlan pool configuration in fabric policy templates
- Add site_aware_policy_enforcement and bd_enforcement_status arguments to the mso_schema_template_vrf module
- Add support for multicast route map filters in mso_schema_template_bd
- Added module ndo_route_map_policy_multicast to support multicast route map policies configuration in tenant templates
- Added module ndo_template to support creation of tenant, l3out, fabric_policy, fabric_resource, monitoring_tenant, monitoring_access and service_device templates

community.crypto
~~~~~~~~~~~~~~~~

- certificate_complete_chain - add ability to identify Ed25519 and Ed448 complete chains (https://github.com/ansible-collections/community.crypto/pull/777).
- get_certificate - adds ``tls_ctx_options`` option for specifying SSL CTX options (https://github.com/ansible-collections/community.crypto/pull/779).
- get_certificate - allow to obtain the certificate chain sent by the server, and the one used for validation, with the new ``get_certificate_chain`` option. Note that this option only works if the module is run with Python 3.10 or newer (https://github.com/ansible-collections/community.crypto/issues/568, https://github.com/ansible-collections/community.crypto/pull/784).

community.docker
~~~~~~~~~~~~~~~~

- docker_container - add support for ``device_cgroup_rules`` (https://github.com/ansible-collections/community.docker/pull/910).
- docker_container - the new ``state=healthy`` allows to wait for a container to become healthy on startup. The ``healthy_wait_timeout`` option allows to configure the maximum time to wait for this to happen (https://github.com/ansible-collections/community.docker/issues/890, https://github.com/ansible-collections/community.docker/pull/921).

community.general
~~~~~~~~~~~~~~~~~

- CmdRunner module utils - the parameter ``force_lang`` now supports the special value ``auto`` which will automatically try and determine the best parsable locale in the system (https://github.com/ansible-collections/community.general/pull/8517).
- proxmox - add ``disk_volume`` and ``mount_volumes`` keys for better readability (https://github.com/ansible-collections/community.general/pull/8542).
- proxmox - translate the old ``disk`` and ``mounts`` keys to the new handling internally (https://github.com/ansible-collections/community.general/pull/8542).
- proxmox_template - small refactor in logic for determining whether a template exists or not (https://github.com/ansible-collections/community.general/pull/8516).
- redfish_* modules - adds ``ciphers`` option for custom cipher selection (https://github.com/ansible-collections/community.general/pull/8533).
- sudosu become plugin - added an option (``alt_method``) to enhance compatibility with more versions of ``su`` (https://github.com/ansible-collections/community.general/pull/8214).
- virtualbox inventory plugin - expose a new parameter ``enable_advanced_group_parsing`` to change how the VirtualBox dynamic inventory parses VM groups (https://github.com/ansible-collections/community.general/issues/8508, https://github.com/ansible-collections/community.general/pull/8510).
- wdc_redfish_command - minor change to handle upgrade file for Redfish WD platforms (https://github.com/ansible-collections/community.general/pull/8444).

community.proxysql
~~~~~~~~~~~~~~~~~~

- proxysql role - add the pidfile location management (https://github.com/ansible-collections/community.proxysql/pull/145).
- role_proxysql - Update default proxysql version and fix small bugs (https://github.com/ansible-collections/community.proxysql/pull/92).

community.routeros
~~~~~~~~~~~~~~~~~~

- api_info, api_modify - add ``system health settings`` path (https://github.com/ansible-collections/community.routeros/pull/294).
- api_info, api_modify - add missing path ``/system resource irq rps`` (https://github.com/ansible-collections/community.routeros/pull/295).
- api_info, api_modify - add parameter ``host-key-type`` for ``ip ssh`` path (https://github.com/ansible-collections/community.routeros/issues/280, https://github.com/ansible-collections/community.routeros/pull/297).

community.sops
~~~~~~~~~~~~~~

- Detect SOPS 3.9.0 and use new ``decrypt`` and ``encrypt`` subcommands (https://github.com/ansible-collections/community.sops/pull/190).
- sops vars plugin - allow to configure the valid extensions with an ``ansible.cfg`` entry or with an environment variable (https://github.com/ansible-collections/community.sops/pull/185).
- sops vars plugin - new option ``handle_unencrypted_files`` allows to control behavior when encountering unencrypted files with SOPS 3.9.0+ (https://github.com/ansible-collections/community.sops/pull/190).

community.vmware
~~~~~~~~~~~~~~~~

- vmware_host_logbundle - Add timeout parameter (https://github.com/ansible-collections/community.vmware/pull/2092).

containers.podman
~~~~~~~~~~~~~~~~~

- CI Update python for latest Ansible to 3.11 in CI

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- idrac_reset - This module is enhanced to provide default username and default password for the reset operation.

f5networks.f5_modules
~~~~~~~~~~~~~~~~~~~~~

- bigip_pool_member - Removed state from the Returnables.

ibm.storage_virtualize
~~~~~~~~~~~~~~~~~~~~~~

- ibm_sv_manage_security - Added support to allow automatic download of security patches
- ibm_svc_info - Added support to display concise view of all SVC objects not covered by I(gather_subset), detailed view for all SVC objects, concise view of a subset of objects allowing a I(filtervalue)

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

Deprecated Features
-------------------

- The ``frr.frr`` collection has been deprecated.
  It will be removed from Ansible 11 if no one starts maintaining it again before Ansible 11.
  See `Collections Removal Process for unmaintained collections <https://docs.ansible.com/ansible/devel/community/collection_contributors/collection_package_removal.html#unmaintained-collections>`__ for more details (`https://forum.ansible.com/t/6243 <https://forum.ansible.com/t/6243>`__).
- The ``openvswitch.openvswitch`` collection has been deprecated.
  It will be removed from Ansible 11 if no one starts maintaining it again before Ansible 11.
  See `Collections Removal Process for unmaintained collections <https://docs.ansible.com/ansible/devel/community/collection_contributors/collection_package_removal.html#unmaintained-collections>`__ for more details (`https://forum.ansible.com/t/6245 <https://forum.ansible.com/t/6245>`__).

Bugfixes
--------

Ansible-core
~~~~~~~~~~~~

- Fix a traceback when an environment variable contains certain special characters (https://github.com/ansible/ansible/issues/83498)
- dnf - reverted incomplete fix from 2.17.2rc1 (https://github.com/ansible/ansible/pull/83504)
- dnf, dnf5 - fix for installing a set of packages by specifying them using a wildcard character (https://github.com/ansible/ansible/issues/83373)
- linear strategy now provides a properly templated task name to the v2_runner_on_started callback event.
- package_facts - ignore warnings sent by apk on stderr (https://github.com/ansible/ansible/issues/83501).
- replace - Updated before/after example (https://github.com/ansible/ansible/issues/83390).
- templating hostvars under native jinja will not cause serialization errors anymore.

cisco.aci
~~~~~~~~~

- Remove duplicate alias name for attribute epg in aci_epg_subnet module

cisco.mso
~~~~~~~~~

- Fix to avoid making updates to attributes that are not provided which could lead to removal of configuration in mso_schema_template_bd
- Fix to avoid making updates to attributes that are not provided which could lead to removal of configuration in mso_schema_template_vrf

community.dns
~~~~~~~~~~~~~

- Update Public Suffix List.

community.docker
~~~~~~~~~~~~~~~~

- docker_compose_v2* modules - fix parsing of skipped pull messages for Docker Compose 2.28.x (https://github.com/ansible-collections/community.docker/issues/911, https://github.com/ansible-collections/community.docker/pull/916).
- docker_compose_v2*, docker_stack*, docker_image_build modules - using ``cli_context`` no longer leads to an invalid parameter combination being passed to the corresponding Docker CLI tool, unless ``docker_host`` is also provided. Combining ``cli_context`` and ``docker_host`` is no longer allowed (https://github.com/ansible-collections/community.docker/issues/892, https://github.com/ansible-collections/community.docker/pull/895).
- docker_container - fix possible infinite loop if ``removal_wait_timeout`` is set (https://github.com/ansible-collections/community.docker/pull/922).
- vendored Docker SDK for Python - use ``LooseVersion`` instead of ``StrictVersion`` to compare urllib3 versions. This is needed for development versions (https://github.com/ansible-collections/community.docker/pull/902).

community.general
~~~~~~~~~~~~~~~~~

- bitwarden lookup plugin - fix ``KeyError`` in ``search_field`` (https://github.com/ansible-collections/community.general/issues/8549, https://github.com/ansible-collections/community.general/pull/8557).
- keycloak_clientscope - remove IDs from clientscope and its protocol mappers on comparison for changed check (https://github.com/ansible-collections/community.general/pull/8545).
- nsupdate - fix 'index out of range' error when changing NS records by falling back to authority section of the response (https://github.com/ansible-collections/community.general/issues/8612, https://github.com/ansible-collections/community.general/pull/8614).
- proxmox - fix idempotency on creation of mount volumes using Proxmox' special ``<storage>:<size>`` syntax (https://github.com/ansible-collections/community.general/issues/8407, https://github.com/ansible-collections/community.general/pull/8542).
- redfish_utils module utils - do not fail when language is not exactly "en" (https://github.com/ansible-collections/community.general/pull/8613).

community.proxysql
~~~~~~~~~~~~~~~~~~

- module_utils - fix ProxySQL version parsing that fails when a suffix wasn't present in the version (https://github.com/ansible-collections/community.proxysql/issues/154).
- role_proxysql - Correct package name (python3-mysqldb instead of python-mysqldb) (https://github.com/ansible-collections/community.proxysql/pull/89).
- role_proxysql - Dynamic user/password in .my.cnf (https://github.com/ansible-collections/community.proxysql/pull/89).

community.sops
~~~~~~~~~~~~~~

- Fix RPM URL for the 3.9.0 release (https://github.com/ansible-collections/community.sops/pull/188).
- sops_encrypt - properly support ``path_regex`` in ``.sops.yaml`` when SOPS 3.9.0 or later is used (https://github.com/ansible-collections/community.sops/issues/153, https://github.com/ansible-collections/community.sops/pull/190).

community.vmware
~~~~~~~~~~~~~~~~

- vcenter_folder - removed documentation that incorrectly said `folder_type` had no effect when `parent_folder` was set
- vmware_cluster_vcls - fixed bug caused by pyvmomi >=7.0.3 returning the vlcs cluster config attribute as None when it was previously undefined. Now if the vCLS config is not initialized on the cluster, the module will initialize it using the user's desired state.
- vmware_host_logbundle - Manifests previously was separared by "&", thus selecting first manifest. Fix now separates manifests with URL encoded space, thus correctly supplying the manifests.  (https://github.com/ansible-collections/community.vmware/pull/2090).

containers.podman
~~~~~~~~~~~~~~~~~

- Fix idempotency for empty values
- Fix missing entries in network quadlet generated file
- Fix quadlet parameters for restart policy
- Idempotency improvements
- params gpus should be exit_policy

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- Resolved the issue in ``idrac_reset`` module where it fails when iDRAC is in busy state. (https://github.com/dell/dellemc-openmanage-ansible-modules/issues/652)

fortinet.fortios
~~~~~~~~~~~~~~~~

- Fix some issues in sanity test.
- Github issue
- mantis issue

ibm.storage_virtualize
~~~~~~~~~~~~~~~~~~~~~~

- ibm_svc_manage_callhome - Setting censorcallhome does not work
- ibm_svc_utils - REST API timeout due to slow response
- ibm_svc_utils - Return correct error in case of error code 500

purestorage.flasharray
~~~~~~~~~~~~~~~~~~~~~~

- purefa_hg - Fix edge case with incorrectly deleted hostgroup when empty array sent for volumes or hosts
- purefa_info - Fix typo from PR
- purefa_info - Resolve issue with performance stats trying to report for remote hosts

Known Issues
------------

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- idrac_diagnostics - Issue(285322) - This module doesn't support export of diagnostics file to HTTP and HTTPS share via SOCKS proxy.
- idrac_firmware - Issue(279282) - This module does not support firmware update using HTTP, HTTPS, and FTP shares with authentication on iDRAC8.
- idrac_storage_volume - Issue(290766) - The module will report success instead of showing failure for new virtual creation on the BOSS-N1 controller if a virtual disk is already present on the same controller.
- ome_diagnostics - Issue(279193) - Export of SupportAssist collection logs to the share location fails on OME version 4.0.0.
- ome_smart_fabric_uplink - Issue(186024) - The module supported by OpenManage Enterprise Modular, however it does not allow the creation of multiple uplinks of the same name. If an uplink is created using the same name as an existing uplink, then the existing uplink is modified.

New Plugins
-----------

Filter
~~~~~~

- community.general.reveal_ansible_type - Return input type.

Test
~~~~

- community.general.ansible_type - Validate input type.

New Modules
-----------

purestorage.flasharray
~~~~~~~~~~~~~~~~~~~~~~

- purestorage.flasharray.purefa_audits - List FlashArray Audit Events
- purestorage.flasharray.purefa_sessions - List FlashArray Sessions

Unchanged Collections
---------------------

- ansible.netcommon (still version 6.1.3)
- ansible.posix (still version 1.5.4)
- ansible.utils (still version 4.1.0)
- ansible.windows (still version 2.4.0)
- arista.eos (still version 9.0.0)
- check_point.mgmt (still version 5.2.3)
- chocolatey.chocolatey (still version 1.5.1)
- cisco.asa (still version 5.0.1)
- cisco.dnac (still version 6.16.0)
- cisco.intersight (still version 2.0.9)
- cisco.ios (still version 8.0.0)
- cisco.iosxr (still version 9.0.0)
- cisco.ise (still version 2.9.2)
- cisco.meraki (still version 2.18.1)
- cisco.nxos (still version 8.1.0)
- cisco.ucs (still version 1.10.0)
- cloud.common (still version 3.0.0)
- cloudscale_ch.cloud (still version 2.3.1)
- community.aws (still version 8.0.0)
- community.ciscosmb (still version 1.0.9)
- community.digitalocean (still version 1.26.0)
- community.grafana (still version 1.9.1)
- community.hashi_vault (still version 6.2.0)
- community.hrobot (still version 2.0.1)
- community.library_inventory_filtering_v1 (still version 1.0.1)
- community.libvirt (still version 1.3.0)
- community.mysql (still version 3.9.0)
- community.network (still version 5.0.3)
- community.okd (still version 3.0.1)
- community.postgresql (still version 3.4.1)
- community.rabbitmq (still version 1.3.0)
- community.sap_libs (still version 1.4.2)
- community.windows (still version 2.2.0)
- community.zabbix (still version 2.5.1)
- cyberark.conjur (still version 1.3.0)
- cyberark.pas (still version 1.0.25)
- dellemc.enterprise_sonic (still version 2.4.0)
- dellemc.powerflex (still version 2.5.0)
- dellemc.unity (still version 2.0.0)
- fortinet.fortimanager (still version 2.5.0)
- frr.frr (still version 2.0.2)
- google.cloud (still version 1.3.0)
- hetzner.hcloud (still version 3.1.1)
- ibm.qradar (still version 3.0.0)
- ibm.spectrum_virtualize (still version 2.0.0)
- ieisystem.inmanage (still version 2.0.0)
- infinidat.infinibox (still version 1.4.5)
- infoblox.nios_modules (still version 1.6.1)
- inspur.ispim (still version 2.2.3)
- inspur.sm (still version 2.3.0)
- junipernetworks.junos (still version 8.0.0)
- kaytus.ksmanage (still version 1.2.2)
- kubernetes.core (still version 3.2.0)
- lowlydba.sqlserver (still version 2.3.3)
- microsoft.ad (still version 1.6.0)
- netapp.cloudmanager (still version 21.22.1)
- netapp.ontap (still version 22.11.0)
- netapp.storagegrid (still version 21.12.0)
- netapp_eseries.santricity (still version 1.4.0)
- netbox.netbox (still version 3.19.1)
- ngine_io.cloudstack (still version 2.3.0)
- ngine_io.exoscale (still version 1.1.0)
- openstack.cloud (still version 2.2.0)
- openvswitch.openvswitch (still version 2.1.1)
- ovirt.ovirt (still version 3.2.0)
- purestorage.flashblade (still version 1.17.0)
- sensu.sensu_go (still version 1.14.0)
- splunk.es (still version 3.0.0)
- t_systems_mms.icinga_director (still version 2.0.1)
- telekom_mms.icinga_director (still version 2.1.2)
- theforeman.foreman (still version 4.0.0)
- vmware.vmware_rest (still version 3.0.1)
- vultr.cloud (still version 1.13.0)
- vyos.vyos (still version 4.1.0)
- wti.remote (still version 1.0.5)

v10.1.0
=======

.. contents::
  :local:
  :depth: 2

Release Summary
---------------

Release Date: 2024-06-18

`Porting Guide <https://docs.ansible.com/ansible/devel/porting_guides.html>`_

Added Collections
-----------------

- ieisystem.inmanage (version 2.0.0)

Ansible-core
------------

Ansible 10.1.0 contains ansible-core version 2.17.1.
This is a newer version than version 2.17.0 contained in the previous Ansible release.

The changes are reported in the combined changelog below.

Changed Collections
-------------------

If not mentioned explicitly, the changes are reported in the combined changelog below.

+------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Collection             | Ansible 10.0.1 | Ansible 10.1.0 | Notes                                                                                                                                                                                                           |
+========================+================+================+=================================================================================================================================================================================================================+
| amazon.aws             | 8.0.0          | 8.0.1          |                                                                                                                                                                                                                 |
+------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ansible.netcommon      | 6.1.2          | 6.1.3          |                                                                                                                                                                                                                 |
+------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ansible.windows        | 2.3.0          | 2.4.0          |                                                                                                                                                                                                                 |
+------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| awx.awx                | 24.3.1         | 24.5.0         | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.                                                                                    |
+------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| azure.azcollection     | 2.3.0          | 2.4.0          | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.                                                                                    |
+------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cisco.dnac             | 6.13.3         | 6.16.0         |                                                                                                                                                                                                                 |
+------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cisco.ise              | 2.9.1          | 2.9.2          |                                                                                                                                                                                                                 |
+------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cisco.nxos             | 8.0.0          | 8.1.0          |                                                                                                                                                                                                                 |
+------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.dns          | 3.0.0          | 3.0.1          |                                                                                                                                                                                                                 |
+------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.docker       | 3.10.3         | 3.10.4         |                                                                                                                                                                                                                 |
+------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.general      | 9.0.1          | 9.1.0          |                                                                                                                                                                                                                 |
+------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.hrobot       | 2.0.0          | 2.0.1          |                                                                                                                                                                                                                 |
+------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.network      | 5.0.2          | 5.0.3          |                                                                                                                                                                                                                 |
+------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.routeros     | 2.15.0         | 2.16.0         |                                                                                                                                                                                                                 |
+------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.zabbix       | 2.4.0          | 2.5.1          |                                                                                                                                                                                                                 |
+------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| containers.podman      | 1.13.0         | 1.15.2         |                                                                                                                                                                                                                 |
+------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cyberark.conjur        | 1.2.2          | 1.3.0          | You can find the collection's changelog at `https://github.com/cyberark/ansible-conjur-collection/blob/master/CHANGELOG.md <https://github.com/cyberark/ansible-conjur-collection/blob/master/CHANGELOG.md>`__. |
+------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| dellemc.openmanage     | 9.2.0          | 9.3.0          |                                                                                                                                                                                                                 |
+------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| dellemc.powerflex      | 2.4.0          | 2.5.0          |                                                                                                                                                                                                                 |
+------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ieisystem.inmanage     |                | 2.0.0          | The collection was added to Ansible                                                                                                                                                                             |
+------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| inspur.ispim           | 2.2.2          | 2.2.3          |                                                                                                                                                                                                                 |
+------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| kubernetes.core        | 3.1.0          | 3.2.0          |                                                                                                                                                                                                                 |
+------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| lowlydba.sqlserver     | 2.3.2          | 2.3.3          |                                                                                                                                                                                                                 |
+------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| microsoft.ad           | 1.5.0          | 1.6.0          |                                                                                                                                                                                                                 |
+------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| netbox.netbox          | 3.18.0         | 3.19.1         |                                                                                                                                                                                                                 |
+------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| purestorage.flasharray | 1.28.0         | 1.28.1         |                                                                                                                                                                                                                 |
+------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| vultr.cloud            | 1.12.1         | 1.13.0         |                                                                                                                                                                                                                 |
+------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Major Changes
-------------

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
- ome_session - This module allows you to create and delete the sessions on OpenManage Enterprise and OpenManage Enterprise Modular.

Minor Changes
-------------

Ansible-core
~~~~~~~~~~~~

- ansible-test - Update ``pypi-test-container`` to version 3.1.0.

ansible.windows
~~~~~~~~~~~~~~~

- win_powershell - Added the ``sensitive_parameters`` option that can be used to pass in a SecureString or PSCredential parameter value.
- win_setup - Added the ``ansible_win_rm_certificate_thumbprint`` fact to display the thumbprint of the certificate in use
- win_user - Added the ability to set an account expiration date using the ``account_expires`` option - https://github.com/ansible-collections/ansible.windows/issues/610

cisco.dnac
~~~~~~~~~~

- Added API to validate the server address
- Added detailed documentation in network_settings_workflow_manager.py
- Added example playbooks in device_provision_workflow.yml
- Added example playbooks in network_compliance_workflow_manager.py
- Added new attribute 'ise_integration_wait_time' in ise_radius_integration_workflow_manager.py
- Added the code for creating/updating/deleting events subscription notification with specified destination and added the playbook and documentation with examples
- Changes in inventory and swim workflow manager modules.
- Checking SNMP versions in events_and_notifications_workflow_manager.py module
- Fix module name from network_device_config__info to configuration_archive_details_info.
- Minor bug fixes in device_credential_workflow_manager.py module
- application_policy_application_set - new module
- application_policy_application_set_count_info - new module
- application_policy_application_set_info - new module
- applications_count_v2_info - new module
- applications_v2 - new module
- applications_v2_info - new module
- auth_token_create - new module
- authentication_policy_servers - new module
- device_configs_backup_workflow_manager - New workflow manager module for device configuration backup functions.
- device_credential_workflow_manager - Updated the log messages.
- device_reboot_apreboot - new module
- dna_event_snmp_config_info - new module
- event_snmp_config - new module
- event_webhook_read_info - new module
- events_and_notifications_workflow_manager - New workflow manager for configuring various types of destinations(Webhook, Email, Syslog, SNMP, ITSM) to deliver event notifications.
- events_and_notifications_workflow_manager.py - Added attributes 'webhook_event_notification', 'email_event_notification', 'syslog_event_notification'
- flexible_report_content_info - new module
- flexible_report_execute - new module
- flexible_report_executions_info - new module
- flexible_report_schedule  - new module
- flexible_report_schedule_info - new module
- integration_settings_itsm_instances_info - new module
- integration_settings_status_info - new module
- inventory_workflow_manager - Updated changes related to provisioning devices.
- ise_integration_status_info - new module
- ise_radius_integration_workflow_manager - New workflow manager for Authentication and Policy Servers(ISE/AAA).
- ise_radius_integration_workflow_manager - Removed the attributes 'port' and 'subscriber_name'. Added the attribute 'ise_integration_wait_time'.
- lan_automation_sessions_info - new module
- lan_automation_update - new module
- lan_automation_update_device - new module
- lan_automation_update_v2 - new module
- lan_automation_v2 - new module
- network_compliance_workflow_manager - New workflow manager for Network Compliance module for managing network compliance tasks on reachable device(s).
- network_device_user_defined_field_delete - new module
- network_settings_workflow_manager - Added attributes 'ipv4_global_pool_name'.
- provision_workflow_manager - Updated changes related to handle errors.
- provision_workflow_manager.py - Added attribute 'provisioning'
- site_workflow_manager - Updated changes in Site updation.
- template_workflow_manager - Removed attributes 'create_time', 'failure_policy', 'last_update_time', 'latest_version_time', 'parent_template_id', 'project_id', 'validation_errors', 'rollback_template_params' and 'rollback_template_content'.
- template_workflow_manager.py - Added attributes 'choices', 'failure_policy'
- users_external_authentication - new module
- users_external_servers_aaa_attribute - new module

cisco.nxos
~~~~~~~~~~

- route_maps - support simple route-maps that do not contain set or match statements. it allows for the creation and management of purely basic route-map entries like 'route-map test-1 permit 10'.

community.general
~~~~~~~~~~~~~~~~~

- CmdRunner module util - argument formats can be specified as plain functions without calling ``cmd_runner_fmt.as_func()`` (https://github.com/ansible-collections/community.general/pull/8479).
- ansible_galaxy_install - add upgrade feature (https://github.com/ansible-collections/community.general/pull/8431, https://github.com/ansible-collections/community.general/issues/8351).
- cargo - add option ``directory``, which allows source directory to be specified (https://github.com/ansible-collections/community.general/pull/8480).
- cmd_runner module utils - add decorator ``cmd_runner_fmt.stack`` (https://github.com/ansible-collections/community.general/pull/8415).
- cmd_runner_fmt module utils - simplify implementation of ``cmd_runner_fmt.as_bool_not()`` (https://github.com/ansible-collections/community.general/pull/8512).
- ipa_dnsrecord - adds ``SSHFP`` record type for managing SSH fingerprints in FreeIPA DNS (https://github.com/ansible-collections/community.general/pull/8404).
- keycloak_client - assign auth flow by name (https://github.com/ansible-collections/community.general/pull/8428).
- openbsd_pkg - adds diff support to show changes in installed package list. This does not yet work for check mode (https://github.com/ansible-collections/community.general/pull/8402).
- proxmox - allow specification of the API port when using proxmox_* (https://github.com/ansible-collections/community.general/issues/8440, https://github.com/ansible-collections/community.general/pull/8441).
- proxmox_vm_info - add ``network`` option to retrieve current network information (https://github.com/ansible-collections/community.general/pull/8471).
- redfish_command - add ``wait`` and ``wait_timeout`` options to allow a user to block a command until a service is accessible after performing the requested command (https://github.com/ansible-collections/community.general/issues/8051, https://github.com/ansible-collections/community.general/pull/8434).
- redfish_info - add command ``CheckAvailability`` to check if a service is accessible (https://github.com/ansible-collections/community.general/issues/8051, https://github.com/ansible-collections/community.general/pull/8434).
- redis_info - adds support for getting cluster info (https://github.com/ansible-collections/community.general/pull/8464).

community.routeros
~~~~~~~~~~~~~~~~~~

- api_info, api_modify - add missing path ``/ppp secret`` (https://github.com/ansible-collections/community.routeros/pull/286).
- api_info, api_modify - minor changes ``/interface ethernet`` path fields (https://github.com/ansible-collections/community.routeros/pull/288).

community.zabbix
~~~~~~~~~~~~~~~~

- agent role - Standardized all configuration variables using the `zabbix_agent` prefix vs `zabbix_agent2`.  Support for `zabbix_agent2` to be removed in 3.0.0
- agent role - Standardized templating of agent.conf file
- all roles - Added support for Ubuntu 24.04 (Noble Numbat)
- zabbix_discoveryrule module added
- zabbix_host_events_update module added
- zabbix_item - add support for setting master items by name
- zabbix_item module added
- zabbix_itemprototype - add support for setting master items by name
- zabbix_itemprototype module added
- zabbix_trigger module added
- zabbix_triggerprototype module added

containers.podman
~~~~~~~~~~~~~~~~~

- Add autodiscovery for build context in podman_image
- Add docs, tests and more examples for podman_pod
- Add extra_args for podman_image push and pull
- Add idempotency for mounts and volumes in podman_container
- Add new functionality tests for podman_secret
- Add option for inline Containerfile in podman_image
- Add path and env options for podman_secret
- Add route, dns and ipam_driver to podman_network
- Create podman secret when skip_existing=True and it does not exist

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- Added support for Python 3.12.
- Added time_to_wait option in ``idrac_storage_volume`` module.

dellemc.powerflex
~~~~~~~~~~~~~~~~~

- Added support for PowerFlex Onyx version(4.6.x).
- Fixed the roles to support attaching the MDM cluster to the gateway.
- The storage pool module has been enhanced to support more features.

kubernetes.core
~~~~~~~~~~~~~~~

- connection/kubectl.py - Added an example of using the kubectl connection plugin to the documentation (https://github.com/ansible-collections/kubernetes.core/pull/741).
- inventory/k8s.py - Defer removal of k8s inventory plugin to version 6.0.0 (https://github.com/ansible-collections/kubernetes.core/pull/734).

microsoft.ad
~~~~~~~~~~~~

- microsoft.ad AD modules - Added ``domain_credentials`` as a common module option that can be used to specify credentials for specific AD servers.
- microsoft.ad AD modules - Added ``lookup_failure_action`` on all modules that can specify a list of distinguishedName values to control what should happen if the lookup fails.
- microsoft.ad.computer - Added the ability to lookup a distinguishedName on a specific domain server for ``delegates`` and ``managed_by``.
- microsoft.ad.group - Added the ability to lookup a distinguishedName on a specific domain server for ``managed_by`` and ``members``.
- microsoft.ad.ou - Added the ability to lookup a distinguishedName on a specific domain server for ``managed_by``.
- microsoft.ad.user - Added the ability to lookup a distinguishedName on a specific domain server for ``delegates``.
- microsoft.ad.user - Rename the option ``groups.missing_action`` to ``groups.lookup_failure_action`` to make the option more consistent with other modules. The ``missing_action`` option is still supported as an alias.
- microsoft.ad.user - Support group member lookup on alternative server using the DN lookup syntax. This syntax uses a dictionary where ``name`` defined the group to lookup and ``server`` defines the server to lookup the group on.

netbox.netbox
~~~~~~~~~~~~~

- Add cluster host to dynamic inventory response `#1219 <https://github.com/netbox-community/ansible_modules/pull/1219>`_
- Add galaxy-importer to CI process `#1245 <https://github.com/netbox-community/ansible_modules/issues/1245>`_
- Adjust modules to support NetBox v4.0.0 `#1234 <https://github.com/netbox-community/ansible_modules/pull/1234>`_
- Bump jinja2 from 3.1.2 to 3.1.4 `#1226 <https://github.com/netbox-community/ansible_modules/pull/1226>`_
- Bump requests from 2.31.0 to 2.32.0 `#1236 <https://github.com/netbox-community/ansible_modules/pull/1236>`_
- Bump version 3.19.1
- Drop obsolete Ansible and Python versions and fix tests `#1241 <https://github.com/netbox-community/ansible_modules/issues/1241>`_
- Get ansible-lint passing again (sequence after `#1241 <https://github.com/netbox-community/ansible_modules/issues/1241>`_) `#1243 <https://github.com/netbox-community/ansible_modules/issues/1243>`_
- Update CI process to follow Ansible Collection Standards `#1247 <https://github.com/netbox-community/ansible_modules/issues/1247>`_
- Update CI to use master instead of main. `#1253 <https://github.com/netbox-community/ansible_modules/issues/1253>`_
- Update ansible-lint to ignore changelog file for yaml indentation. `#1256 <https://github.com/netbox-community/ansible_modules/issues/1256>`_
- Update top-level README with new minimum Ansible version (sequence after `#1241 <https://github.com/netbox-community/ansible_modules/issues/1241>`_ `#1244 <https://github.com/netbox-community/ansible_modules/issues/1244>`_
- Updated CI to only run changelog job if PR into devel branch is detected. `#1251 <https://github.com/netbox-community/ansible_modules/issues/1251>`_
- Updated CI to support NetBox 4.0 `#1230 <https://github.com/netbox-community/ansible_modules/pull/1230>`_
- Updates to top-level README.md to align collection with Ansible best practices `#1238 <https://github.com/netbox-community/ansible_modules/issues/1238>`_

vultr.cloud
~~~~~~~~~~~

- instance, bare_metal - Implemented a new option ``skip_wait`` (https://github.com/vultr/ansible-collection-vultr/issues/119).

Deprecated Features
-------------------

community.general
~~~~~~~~~~~~~~~~~

- CmdRunner module util - setting the value of the ``ignore_none`` parameter within a ``CmdRunner`` context is deprecated and that feature should be removed in community.general 12.0.0 (https://github.com/ansible-collections/community.general/pull/8479).
- git_config - the ``list_all`` option has been deprecated and will be removed in community.general 11.0.0. Use the ``community.general.git_config_info`` module instead (https://github.com/ansible-collections/community.general/pull/8453).
- git_config - using ``state=present`` without providing ``value`` is deprecated and will be disallowed in community.general 11.0.0. Use the ``community.general.git_config_info`` module instead to read a value (https://github.com/ansible-collections/community.general/pull/8453).

Bugfixes
--------

Ansible-core
~~~~~~~~~~~~

- Fix rapid memory usage growth when notifying handlers using the ``listen`` keyword (https://github.com/ansible/ansible/issues/83392)
- Fix the task attribute ``resolved_action`` to show the FQCN instead of ``None`` when ``action`` or ``local_action`` is used in the playbook.
- Fix using ``module_defaults`` with ``local_action``/``action`` (https://github.com/ansible/ansible/issues/81905).
- fixed unit test test_borken_cowsay to address mock not been properly applied when existing unix system already have cowsay installed.
- powershell - Implement more robust deletion mechanism for C# code compilation temporary files. This should avoid scenarios where the underlying temporary directory may be temporarily locked by antivirus tools or other IO problems. A failure to delete one of these temporary directories will result in a warning rather than an outright failure.
- shell plugin - properly quote all needed components of shell commands (https://github.com/ansible/ansible/issues/82535)

amazon.aws
~~~~~~~~~~

- backup_plan_info - Bugfix to enable getting info of all backup plans (https://github.com/ansible-collections/amazon.aws/pull/2083).
- ec2_instance - do not ignore IPv6 addresses when a single network interface is specified (https://github.com/ansible-collections/amazon.aws/pull/1979).
- s3_object - fixed issue which was causing ``MemoryError`` exceptions when downloading large files (https://github.com/ansible-collections/amazon.aws/issues/2107).

ansible.netcommon
~~~~~~~~~~~~~~~~~

- The v6.1.2 release introduced a change in cliconfbase's edit_config() signature which broke many platform cliconfs. This patch release reverts that change.

ansible.windows
~~~~~~~~~~~~~~~

- setup - Provide WMI/CIM fallback for facts that rely on SMBIOS when that is unavailable

cisco.ise
~~~~~~~~~

- Added main.yml to aws_deployment role
- Update min_ansible_version to 2.15.0 in runtime.yml and roles

cisco.nxos
~~~~~~~~~~

- nxos_l3_interfaces - fail if encapsulation exists on a different sub-interface.
- nxos_static_routes - correctly generate command when track parameter is specified.

community.dns
~~~~~~~~~~~~~

- Update Public Suffix List.

community.docker
~~~~~~~~~~~~~~~~

- docker_compose - make sure that the module uses the ``api_version`` parameter (https://github.com/ansible-collections/community.docker/pull/881).
- docker_compose_v2* modules - there was no check to make sure that one of ``project_src`` and ``definition`` is provided. The modules crashed if none were provided (https://github.com/ansible-collections/community.docker/issues/885, https://github.com/ansible-collections/community.docker/pull/886).

community.general
~~~~~~~~~~~~~~~~~

- git_config - fix behavior of ``state=absent`` if ``value`` is present (https://github.com/ansible-collections/community.general/issues/8436, https://github.com/ansible-collections/community.general/pull/8452).
- keycloak_realm - add normalizations for ``attributes`` and ``protocol_mappers`` (https://github.com/ansible-collections/community.general/pull/8496).
- launched - correctly report changed status in check mode (https://github.com/ansible-collections/community.general/pull/8406).
- opennebula inventory plugin - fix invalid reference to IP when inventory runs against NICs with no IPv4 address (https://github.com/ansible-collections/community.general/pull/8489).
- opentelemetry callback - do not save the JSON response when using the ``ansible.builtin.uri`` module (https://github.com/ansible-collections/community.general/pull/8430).
- opentelemetry callback - do not save the content response when using the ``ansible.builtin.slurp`` module (https://github.com/ansible-collections/community.general/pull/8430).
- paman - do not fail if an empty list of packages has been provided and there is nothing to do (https://github.com/ansible-collections/community.general/pull/8514).

community.hrobot
~~~~~~~~~~~~~~~~

- boot - use PHP array form encoding when sending multiple ``authorized_key`` (https://github.com/ansible-collections/community.hrobot/issues/112, https://github.com/ansible-collections/community.hrobot/pull/113).

community.network
~~~~~~~~~~~~~~~~~

- exos - Add error handling of ``Permission denied`` errors (https://github.com/ansible-collections/community.network/pull/571).

community.zabbix
~~~~~~~~~~~~~~~~

- zabbix_agent - Fix reading existing psk
- zabbix_agent - Fix role when zabbix_agent_listenip is undefined
- zabbix_web - make the FPM socket group-writable so the web server can properly forward requests to the FPM process

containers.podman
~~~~~~~~~~~~~~~~~

- Fix idempotency for pod with 0.0.0.0
- Fix idempotency for pods in case of systemd generation
- Fix idempotency for systemd generations
- Fix issue with pushing podman image to repo name and org
- Fix transports issues in podman_image
- fix(#747) set correct HealthCmd

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- Resolved the issue in ``idrac_certificates`` module where subject_alt_name parameter was only accepting first item in list. (https://github.com/dell/dellemc-openmanage-ansible-modules/issues/584)
- Resolved the issue in ``idrac_virtual_media`` module where the Authorization request header was included in the request. (https://github.com/dell/dellemc-openmanage-ansible-modules/issues/612)
- Resolved the issue in ``ome_application_certificate`` module related to a padding error in generated CSR file. (https://github.com/dell/dellemc-openmanage-ansible-modules/issues/370)

inspur.ispim
~~~~~~~~~~~~

- Change the ansible version in meta/runtime.yml to 2.15.0(https://github.com/ispim/inspur.ispim/pull/37).

lowlydba.sqlserver
~~~~~~~~~~~~~~~~~~

- fixed the expected type of the ip_address, subnet_ip, and subnet_mask parameters to be lists instead of strings (lowlydba.sqlserver.ag_listener)

microsoft.ad
~~~~~~~~~~~~

- microsoft.ad.membership - Fix hostname check to work with hostnames longer than 15 characters long - https://github.com/ansible-collections/microsoft.ad/issues/113
- microsoft.ad.user - Fix issue when creating a new user account with ``account_locked: false`` - https://github.com/ansible-collections/microsoft.ad/issues/108

netbox.netbox
~~~~~~~~~~~~~

- Added ALLOWED_QUERY_PARAMS module_bay by device `#1228 <https://github.com/netbox-community/ansible_modules/pull/1228>`_
- Added label to power outlet `#1222 <https://github.com/netbox-community/ansible_modules/pull/1222>`_
- Added power outlet type iec-60320-c21 to power outlet template and power outlet modules `#1229 <https://github.com/netbox-community/ansible_modules/issues/1229>`_
- Extend query param for parent_location `#1233 <https://github.com/netbox-community/ansible_modules/issues/1233>`_

purestorage.flasharray
~~~~~~~~~~~~~~~~~~~~~~

- purefa_network - Fix issue with clearing network interface addresses
- purefa_network - Resolve issue when setting a network port on a new array
- purefa_policy - Enhanced idempotency for snapshot policy rules

Known Issues
------------

community.general
~~~~~~~~~~~~~~~~~

- homectl - the module does not work under Python 3.13 or newer, since it relies on the removed ``crypt`` standard library module (https://github.com/ansible-collections/community.general/issues/4691, https://github.com/ansible-collections/community.general/pull/8497).
- udm_user - the module does not work under Python 3.13 or newer, since it relies on the removed ``crypt`` standard library module (https://github.com/ansible-collections/community.general/issues/4690, https://github.com/ansible-collections/community.general/pull/8497).

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- idrac_diagnostics - Issue(285322) - This module doesn't support export of diagnostics file to HTTP and HTTPS share via SOCKS proxy.
- idrac_firmware - Issue(279282) - This module does not support firmware update using HTTP, HTTPS, and FTP shares with authentication on iDRAC8.
- idrac_storage_volume - Issue(290766) - The module will report success instead of showing failure for new virtual creation on the BOSS-N1 controller if a virtual disk is already present on the same controller.
- ome_diagnostics - Issue(279193) - Export of SupportAssist collection logs to the share location fails on OME version 4.0.0.
- ome_smart_fabric_uplink - Issue(186024) - The module supported by OpenManage Enterprise Modular, however it does not allow the creation of multiple uplinks of the same name. If an uplink is created using the same name as an existing uplink, then the existing uplink is modified.

New Plugins
-----------

Filter
~~~~~~

- community.general.keep_keys - Keep specific keys from dictionaries in a list.
- community.general.remove_keys - Remove specific keys from dictionaries in a list.
- community.general.replace_keys - Replace specific keys in a list of dictionaries.

New Modules
-----------

community.general
~~~~~~~~~~~~~~~~~

- community.general.consul_agent_check - Add, modify, and delete checks within a consul cluster.
- community.general.consul_agent_service - Add, modify and delete services within a consul cluster.
- community.general.django_check - Wrapper for C(django-admin check).
- community.general.django_createcachetable - Wrapper for C(django-admin createcachetable).

containers.podman
~~~~~~~~~~~~~~~~~

- containers.podman.podman_search - Search for remote images using podman

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- dellemc.openmanage.ome_session - This module allows you to create and delete sessions on OpenManage Enterprise and OpenManage Enterprise Modular.

Unchanged Collections
---------------------

- ansible.posix (still version 1.5.4)
- ansible.utils (still version 4.1.0)
- arista.eos (still version 9.0.0)
- check_point.mgmt (still version 5.2.3)
- chocolatey.chocolatey (still version 1.5.1)
- cisco.aci (still version 2.9.0)
- cisco.asa (still version 5.0.1)
- cisco.intersight (still version 2.0.9)
- cisco.ios (still version 8.0.0)
- cisco.iosxr (still version 9.0.0)
- cisco.meraki (still version 2.18.1)
- cisco.mso (still version 2.6.0)
- cisco.ucs (still version 1.10.0)
- cloud.common (still version 3.0.0)
- cloudscale_ch.cloud (still version 2.3.1)
- community.aws (still version 8.0.0)
- community.ciscosmb (still version 1.0.9)
- community.crypto (still version 2.20.0)
- community.digitalocean (still version 1.26.0)
- community.grafana (still version 1.9.1)
- community.hashi_vault (still version 6.2.0)
- community.library_inventory_filtering_v1 (still version 1.0.1)
- community.libvirt (still version 1.3.0)
- community.mongodb (still version 1.7.4)
- community.mysql (still version 3.9.0)
- community.okd (still version 3.0.1)
- community.postgresql (still version 3.4.1)
- community.proxysql (still version 1.5.1)
- community.rabbitmq (still version 1.3.0)
- community.sap_libs (still version 1.4.2)
- community.sops (still version 1.6.7)
- community.vmware (still version 4.4.0)
- community.windows (still version 2.2.0)
- cyberark.pas (still version 1.0.25)
- dellemc.enterprise_sonic (still version 2.4.0)
- dellemc.unity (still version 2.0.0)
- f5networks.f5_modules (still version 1.28.0)
- fortinet.fortimanager (still version 2.5.0)
- fortinet.fortios (still version 2.3.6)
- frr.frr (still version 2.0.2)
- google.cloud (still version 1.3.0)
- grafana.grafana (still version 5.2.0)
- hetzner.hcloud (still version 3.1.1)
- ibm.qradar (still version 3.0.0)
- ibm.spectrum_virtualize (still version 2.0.0)
- ibm.storage_virtualize (still version 2.3.1)
- infinidat.infinibox (still version 1.4.5)
- infoblox.nios_modules (still version 1.6.1)
- inspur.sm (still version 2.3.0)
- junipernetworks.junos (still version 8.0.0)
- kaytus.ksmanage (still version 1.2.2)
- netapp.cloudmanager (still version 21.22.1)
- netapp.ontap (still version 22.11.0)
- netapp.storagegrid (still version 21.12.0)
- netapp_eseries.santricity (still version 1.4.0)
- ngine_io.cloudstack (still version 2.3.0)
- ngine_io.exoscale (still version 1.1.0)
- openstack.cloud (still version 2.2.0)
- openvswitch.openvswitch (still version 2.1.1)
- ovirt.ovirt (still version 3.2.0)
- purestorage.flashblade (still version 1.17.0)
- sensu.sensu_go (still version 1.14.0)
- splunk.es (still version 3.0.0)
- t_systems_mms.icinga_director (still version 2.0.1)
- telekom_mms.icinga_director (still version 2.1.2)
- theforeman.foreman (still version 4.0.0)
- vmware.vmware_rest (still version 3.0.1)
- vyos.vyos (still version 4.1.0)
- wti.remote (still version 1.0.5)

v10.0.1
=======

.. contents::
  :local:
  :depth: 2

Release Summary
---------------

Release Date: 2024-06-06

`Porting Guide <https://docs.ansible.com/ansible/devel/porting_guides.html>`_

This release updates 10.0.0 by removing binary files from a Windows venv that accidentally were included in two collection releases.

Ansible-core
------------

Ansible 10.0.1 contains ansible-core version 2.17.0.
This is the same version of ansible-core as in the previous Ansible release.

Changed Collections
-------------------

If not mentioned explicitly, the changes are reported in the combined changelog below.

+-----------------+----------------+----------------+-------+
| Collection      | Ansible 10.0.0 | Ansible 10.0.1 | Notes |
+=================+================+================+=======+
| inspur.ispim    | 2.2.1          | 2.2.2          |       |
+-----------------+----------------+----------------+-------+
| kaytus.ksmanage | 1.2.1          | 1.2.2          |       |
+-----------------+----------------+----------------+-------+

Bugfixes
--------

inspur.ispim
~~~~~~~~~~~~

- Remove venv files that were accidentally bundled in 2.2.1 (https://github.com/ispim/inspur.ispim/pull/35).

kaytus.ksmanage
~~~~~~~~~~~~~~~

- Remove venv files that were accidentally bundled in 1.2.2(https://github.com/ieisystem/kaytus.ksmanage/pull/23).

Unchanged Collections
---------------------

- amazon.aws (still version 8.0.0)
- ansible.netcommon (still version 6.1.2)
- ansible.posix (still version 1.5.4)
- ansible.utils (still version 4.1.0)
- ansible.windows (still version 2.3.0)
- arista.eos (still version 9.0.0)
- awx.awx (still version 24.3.1)
- azure.azcollection (still version 2.3.0)
- check_point.mgmt (still version 5.2.3)
- chocolatey.chocolatey (still version 1.5.1)
- cisco.aci (still version 2.9.0)
- cisco.asa (still version 5.0.1)
- cisco.dnac (still version 6.13.3)
- cisco.intersight (still version 2.0.9)
- cisco.ios (still version 8.0.0)
- cisco.iosxr (still version 9.0.0)
- cisco.ise (still version 2.9.1)
- cisco.meraki (still version 2.18.1)
- cisco.mso (still version 2.6.0)
- cisco.nxos (still version 8.0.0)
- cisco.ucs (still version 1.10.0)
- cloud.common (still version 3.0.0)
- cloudscale_ch.cloud (still version 2.3.1)
- community.aws (still version 8.0.0)
- community.ciscosmb (still version 1.0.9)
- community.crypto (still version 2.20.0)
- community.digitalocean (still version 1.26.0)
- community.dns (still version 3.0.0)
- community.docker (still version 3.10.3)
- community.general (still version 9.0.1)
- community.grafana (still version 1.9.1)
- community.hashi_vault (still version 6.2.0)
- community.hrobot (still version 2.0.0)
- community.library_inventory_filtering_v1 (still version 1.0.1)
- community.libvirt (still version 1.3.0)
- community.mongodb (still version 1.7.4)
- community.mysql (still version 3.9.0)
- community.network (still version 5.0.2)
- community.okd (still version 3.0.1)
- community.postgresql (still version 3.4.1)
- community.proxysql (still version 1.5.1)
- community.rabbitmq (still version 1.3.0)
- community.routeros (still version 2.15.0)
- community.sap_libs (still version 1.4.2)
- community.sops (still version 1.6.7)
- community.vmware (still version 4.4.0)
- community.windows (still version 2.2.0)
- community.zabbix (still version 2.4.0)
- containers.podman (still version 1.13.0)
- cyberark.conjur (still version 1.2.2)
- cyberark.pas (still version 1.0.25)
- dellemc.enterprise_sonic (still version 2.4.0)
- dellemc.openmanage (still version 9.2.0)
- dellemc.powerflex (still version 2.4.0)
- dellemc.unity (still version 2.0.0)
- f5networks.f5_modules (still version 1.28.0)
- fortinet.fortimanager (still version 2.5.0)
- fortinet.fortios (still version 2.3.6)
- frr.frr (still version 2.0.2)
- google.cloud (still version 1.3.0)
- grafana.grafana (still version 5.2.0)
- hetzner.hcloud (still version 3.1.1)
- ibm.qradar (still version 3.0.0)
- ibm.spectrum_virtualize (still version 2.0.0)
- ibm.storage_virtualize (still version 2.3.1)
- infinidat.infinibox (still version 1.4.5)
- infoblox.nios_modules (still version 1.6.1)
- inspur.sm (still version 2.3.0)
- junipernetworks.junos (still version 8.0.0)
- kubernetes.core (still version 3.1.0)
- lowlydba.sqlserver (still version 2.3.2)
- microsoft.ad (still version 1.5.0)
- netapp.cloudmanager (still version 21.22.1)
- netapp.ontap (still version 22.11.0)
- netapp.storagegrid (still version 21.12.0)
- netapp_eseries.santricity (still version 1.4.0)
- netbox.netbox (still version 3.18.0)
- ngine_io.cloudstack (still version 2.3.0)
- ngine_io.exoscale (still version 1.1.0)
- openstack.cloud (still version 2.2.0)
- openvswitch.openvswitch (still version 2.1.1)
- ovirt.ovirt (still version 3.2.0)
- purestorage.flasharray (still version 1.28.0)
- purestorage.flashblade (still version 1.17.0)
- sensu.sensu_go (still version 1.14.0)
- splunk.es (still version 3.0.0)
- t_systems_mms.icinga_director (still version 2.0.1)
- telekom_mms.icinga_director (still version 2.1.2)
- theforeman.foreman (still version 4.0.0)
- vmware.vmware_rest (still version 3.0.1)
- vultr.cloud (still version 1.12.1)
- vyos.vyos (still version 4.1.0)
- wti.remote (still version 1.0.5)

v10.0.0
=======

.. contents::
  :local:
  :depth: 2

Release Summary
---------------

Release Date: 2024-06-04

`Porting Guide <https://docs.ansible.com/ansible/devel/porting_guides.html>`_

Removed Collections
-------------------

- community.azure (previously included version: 2.0.0)
- community.sap (previously included version: 2.0.0)
- gluster.gluster (previously included version: 1.0.2)
- hpe.nimble (previously included version: 1.1.4)
- netapp.aws (previously included version: 21.7.1)
- netapp.azure (previously included version: 21.10.1)
- netapp.elementsw (previously included version: 21.7.0)
- netapp.um_info (previously included version: 21.8.1)
- purestorage.fusion (previously included version: 1.6.0)

You can still install a removed collection manually with ``ansible-galaxy collection install <name-of-collection>``.

Added Collections
-----------------

- community.library_inventory_filtering_v1 (version 1.0.1)
- kaytus.ksmanage (version 1.2.1)

Ansible-core
------------

Ansible 10.0.0 contains ansible-core version 2.17.0.
This is a newer version than version 2.16.0 contained in the previous Ansible release.

The changes are reported in the combined changelog below.

Included Collections
--------------------

If not mentioned explicitly, the changes are reported in the combined changelog below.

+------------------------------------------+---------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| Collection                               | Ansible 9.0.0 | Ansible 10.0.0 | Notes                                                                                                                        |
+==========================================+===============+================+==============================================================================================================================+
| amazon.aws                               | 7.0.0         | 8.0.0          |                                                                                                                              |
+------------------------------------------+---------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| ansible.netcommon                        | 5.3.0         | 6.1.2          |                                                                                                                              |
+------------------------------------------+---------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| ansible.utils                            | 2.11.0        | 4.1.0          |                                                                                                                              |
+------------------------------------------+---------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| ansible.windows                          | 2.1.0         | 2.3.0          |                                                                                                                              |
+------------------------------------------+---------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| arista.eos                               | 6.2.1         | 9.0.0          |                                                                                                                              |
+------------------------------------------+---------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| awx.awx                                  | 23.3.1        | 24.3.1         | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+------------------------------------------+---------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| azure.azcollection                       | 1.19.0        | 2.3.0          | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+------------------------------------------+---------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| check_point.mgmt                         | 5.1.1         | 5.2.3          |                                                                                                                              |
+------------------------------------------+---------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.aci                                | 2.8.0         | 2.9.0          |                                                                                                                              |
+------------------------------------------+---------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.asa                                | 4.0.3         | 5.0.1          |                                                                                                                              |
+------------------------------------------+---------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.dnac                               | 6.7.6         | 6.13.3         |                                                                                                                              |
+------------------------------------------+---------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.intersight                         | 2.0.3         | 2.0.9          | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+------------------------------------------+---------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.ios                                | 5.2.0         | 8.0.0          |                                                                                                                              |
+------------------------------------------+---------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.iosxr                              | 6.1.0         | 9.0.0          |                                                                                                                              |
+------------------------------------------+---------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.ise                                | 2.5.16        | 2.9.1          |                                                                                                                              |
+------------------------------------------+---------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.meraki                             | 2.16.14       | 2.18.1         |                                                                                                                              |
+------------------------------------------+---------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.mso                                | 2.5.0         | 2.6.0          |                                                                                                                              |
+------------------------------------------+---------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.nxos                               | 5.2.1         | 8.0.0          |                                                                                                                              |
+------------------------------------------+---------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| cloud.common                             | 2.1.4         | 3.0.0          |                                                                                                                              |
+------------------------------------------+---------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.aws                            | 7.0.0         | 8.0.0          |                                                                                                                              |
+------------------------------------------+---------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.ciscosmb                       | 1.0.7         | 1.0.9          |                                                                                                                              |
+------------------------------------------+---------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.crypto                         | 2.16.0        | 2.20.0         |                                                                                                                              |
+------------------------------------------+---------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.digitalocean                   | 1.24.0        | 1.26.0         |                                                                                                                              |
+------------------------------------------+---------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.dns                            | 2.6.3         | 3.0.0          |                                                                                                                              |
+------------------------------------------+---------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.docker                         | 3.4.11        | 3.10.3         |                                                                                                                              |
+------------------------------------------+---------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.general                        | 8.0.2         | 9.0.1          |                                                                                                                              |
+------------------------------------------+---------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.grafana                        | 1.6.1         | 1.9.1          |                                                                                                                              |
+------------------------------------------+---------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.hashi_vault                    | 6.0.0         | 6.2.0          |                                                                                                                              |
+------------------------------------------+---------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.hrobot                         | 1.8.2         | 2.0.0          |                                                                                                                              |
+------------------------------------------+---------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.library_inventory_filtering_v1 |               | 1.0.1          | The collection was added to Ansible                                                                                          |
+------------------------------------------+---------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.mongodb                        | 1.6.3         | 1.7.4          | There are no changes recorded in the changelog.                                                                              |
+------------------------------------------+---------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.mysql                          | 3.8.0         | 3.9.0          |                                                                                                                              |
+------------------------------------------+---------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.okd                            | 2.3.0         | 3.0.1          |                                                                                                                              |
+------------------------------------------+---------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.postgresql                     | 3.2.0         | 3.4.1          |                                                                                                                              |
+------------------------------------------+---------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.rabbitmq                       | 1.2.3         | 1.3.0          |                                                                                                                              |
+------------------------------------------+---------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.routeros                       | 2.10.0        | 2.15.0         |                                                                                                                              |
+------------------------------------------+---------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.sap_libs                       | 1.4.1         | 1.4.2          |                                                                                                                              |
+------------------------------------------+---------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.vmware                         | 4.0.0         | 4.4.0          |                                                                                                                              |
+------------------------------------------+---------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.windows                        | 2.0.0         | 2.2.0          |                                                                                                                              |
+------------------------------------------+---------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.zabbix                         | 2.1.0         | 2.4.0          |                                                                                                                              |
+------------------------------------------+---------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| containers.podman                        | 1.11.0        | 1.13.0         |                                                                                                                              |
+------------------------------------------+---------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| cyberark.pas                             | 1.0.23        | 1.0.25         | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+------------------------------------------+---------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| dellemc.enterprise_sonic                 | 2.2.0         | 2.4.0          |                                                                                                                              |
+------------------------------------------+---------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| dellemc.openmanage                       | 8.4.0         | 9.2.0          |                                                                                                                              |
+------------------------------------------+---------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| dellemc.powerflex                        | 2.0.1         | 2.4.0          |                                                                                                                              |
+------------------------------------------+---------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| dellemc.unity                            | 1.7.1         | 2.0.0          |                                                                                                                              |
+------------------------------------------+---------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| f5networks.f5_modules                    | 1.27.0        | 1.28.0         |                                                                                                                              |
+------------------------------------------+---------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| fortinet.fortimanager                    | 2.3.0         | 2.5.0          |                                                                                                                              |
+------------------------------------------+---------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| fortinet.fortios                         | 2.3.4         | 2.3.6          |                                                                                                                              |
+------------------------------------------+---------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| google.cloud                             | 1.2.0         | 1.3.0          |                                                                                                                              |
+------------------------------------------+---------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| grafana.grafana                          | 2.2.3         | 5.2.0          |                                                                                                                              |
+------------------------------------------+---------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| hetzner.hcloud                           | 2.3.0         | 3.1.1          |                                                                                                                              |
+------------------------------------------+---------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| ibm.qradar                               | 2.1.0         | 3.0.0          |                                                                                                                              |
+------------------------------------------+---------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| ibm.storage_virtualize                   | 2.1.0         | 2.3.1          |                                                                                                                              |
+------------------------------------------+---------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| infinidat.infinibox                      | 1.3.12        | 1.4.5          | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+------------------------------------------+---------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| infoblox.nios_modules                    | 1.5.0         | 1.6.1          |                                                                                                                              |
+------------------------------------------+---------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| inspur.ispim                             | 2.1.0         | 2.2.1          |                                                                                                                              |
+------------------------------------------+---------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| junipernetworks.junos                    | 5.3.0         | 8.0.0          |                                                                                                                              |
+------------------------------------------+---------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| kaytus.ksmanage                          |               | 1.2.1          | The collection was added to Ansible                                                                                          |
+------------------------------------------+---------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| kubernetes.core                          | 2.4.0         | 3.1.0          |                                                                                                                              |
+------------------------------------------+---------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| lowlydba.sqlserver                       | 2.2.2         | 2.3.2          |                                                                                                                              |
+------------------------------------------+---------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| microsoft.ad                             | 1.3.0         | 1.5.0          |                                                                                                                              |
+------------------------------------------+---------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| netapp.ontap                             | 22.8.2        | 22.11.0        |                                                                                                                              |
+------------------------------------------+---------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| netapp.storagegrid                       | 21.11.1       | 21.12.0        |                                                                                                                              |
+------------------------------------------+---------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| netbox.netbox                            | 3.15.0        | 3.18.0         |                                                                                                                              |
+------------------------------------------+---------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| openstack.cloud                          | 2.1.0         | 2.2.0          | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+------------------------------------------+---------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| purestorage.flasharray                   | 1.22.0        | 1.28.0         |                                                                                                                              |
+------------------------------------------+---------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| purestorage.flashblade                   | 1.14.0        | 1.17.0         |                                                                                                                              |
+------------------------------------------+---------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| splunk.es                                | 2.1.0         | 3.0.0          |                                                                                                                              |
+------------------------------------------+---------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| telekom_mms.icinga_director              | 1.34.1        | 2.1.2          |                                                                                                                              |
+------------------------------------------+---------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| theforeman.foreman                       | 3.14.0        | 4.0.0          |                                                                                                                              |
+------------------------------------------+---------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| vmware.vmware_rest                       | 2.3.1         | 3.0.1          |                                                                                                                              |
+------------------------------------------+---------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| vultr.cloud                              | 1.10.0        | 1.12.1         |                                                                                                                              |
+------------------------------------------+---------------+----------------+------------------------------------------------------------------------------------------------------------------------------+

Major Changes
-------------

Ansible-core
~~~~~~~~~~~~

- urls.py - Removed support for Python 2

ansible.netcommon
~~~~~~~~~~~~~~~~~

- Bumping `requires_ansible` to `>=2.14.0`, since previous ansible-core versions are EoL now.

ansible.utils
~~~~~~~~~~~~~

- Bumping `netaddr` to `>=0.10.1`, means that starting from this release, the minimum `netaddr` version this collection requires is `>=0.10.1`.
- Bumping `requires_ansible` to `>=2.14.0`, since previous ansible-core versions are EoL now.
- This release mainly addresses the breaking changes in the `netaddr` library.
- With the new release of `netaddr` 1.0.0, the `IPAddress.is_private()` method has been removed and instead, the `IPAddress.is_global()` method has been extended to support the same functionality. This change has been reflected in the `ipaddr` filter plugin.

arista.eos
~~~~~~~~~~

- Bumping `requires_ansible` to `>=2.14.0`, since previous ansible-core versions are EoL now.
- This release removes previously deprecated modules and attributes from this collection. Please refer to the **Removed Features** section for details.
- Update the netcommon base version 6.1.0 to support cli_restore plugin.

cisco.asa
~~~~~~~~~

- Bumping `requires_ansible` to `>=2.14.0`, since previous ansible-core versions are EoL now.

cisco.ios
~~~~~~~~~

- Bumping `requires_ansible` to `>=2.14.0`, since previous ansible-core versions are EoL now.
- Update the netcommon base version 6.1.0 to support cli_restore plugin.
- ios_ntp - Remove deprecated ntp legacy module

cisco.iosxr
~~~~~~~~~~~

- Bumping `requires_ansible` to `>=2.14.0`, since previous ansible-core versions are EoL now.
- This release removes previously deprecated module and attributes from this collection. Please refer to the **Removed Features** section for details.
- Update the netcommon base version to support cli_restore plugin.

cisco.nxos
~~~~~~~~~~

- Bumping `requires_ansible` to `>=2.14.0`, since previous ansible-core versions are EoL now.
- This release removes four previously deprecated modules from this collection. Please refer to the **Removed Features** section for details.
- Updated the minimum required ansible.netcommon version to 6.1.0 to support the cli_restore module.

community.dns
~~~~~~~~~~~~~

- The ``community.dns`` collection now depends on the ``community.library_inventory_filtering_v1`` collection. This utility collection provides host filtering functionality for inventory plugins. If you use the Ansible community package, both collections are included and you do not have to do anything special. If you install the collection with ``ansible-galaxy collection install``, it will be installed automatically. If you install the collection by copying the files of the collection to a place where ansible-core can find it, for example by cloning the git repository, you need to make sure that you also have to install the dependency if you are using the inventory plugins (https://github.com/ansible-collections/community.dns/pull/196).

community.docker
~~~~~~~~~~~~~~~~

- The ``community.docker`` collection now depends on the ``community.library_inventory_filtering_v1`` collection. This utility collection provides host filtering functionality for inventory plugins. If you use the Ansible community package, both collections are included and you do not have to do anything special. If you install the collection with ``ansible-galaxy collection install``, it will be installed automatically. If you install the collection by copying the files of the collection to a place where ansible-core can find it, for example by cloning the git repository, you need to make sure that you also have to install the dependency if you are using the inventory plugins (https://github.com/ansible-collections/community.docker/pull/698).

community.hashi_vault
~~~~~~~~~~~~~~~~~~~~~

- requirements - the ``requests`` package which is required by ``hvac`` now has a more restrictive range for this collection in certain use cases due to breaking security changes in ``ansible-core`` that were backported (https://github.com/ansible-collections/community.hashi_vault/pull/416).

community.hrobot
~~~~~~~~~~~~~~~~

- The ``community.hrobot`` collection now depends on the ``community.library_inventory_filtering_v1`` collection. This utility collection provides host filtering functionality for inventory plugins. If you use the Ansible community package, both collections are included and you do not have to do anything special. If you install the collection with ``ansible-galaxy collection install``, it will be installed automatically. If you install the collection by copying the files of the collection to a place where ansible-core can find it, for example by cloning the git repository, you need to make sure that you also have to install the dependency if you are using the inventory plugin (https://github.com/ansible-collections/community.hrobot/pull/101).

community.mysql
~~~~~~~~~~~~~~~

- Collection version 2.*.* is EOL, no more bugfixes will be backported. Please consider upgrading to the latest version.

containers.podman
~~~~~~~~~~~~~~~~~

- Add quadlet support for Podman modules

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- All OME modules are enhanced to support the environment variables `OME_USERNAME` and `OME_PASSWORD` as fallback for credentials.
- All iDRAC and Redfish modules are enhanced to support the environment variables `IDRAC_USERNAME` and `IDRAC_PASSWORD` as fallback for credentials.
- idrac_certificates - The module is enhanced to support the import and export of `CUSTOMCERTIFICATE`.
- idrac_diagnostics - The module is introduced to run and export diagnostics on iDRAC.
- idrac_gather_facts - This role is enhanced to support secure boot.
- idrac_license - The module is introduced to configure iDRAC licenses.
- idrac_session - This module allows you to create and delete the sessions on iDRAC.
- idrac_user - This role is introduced to manage local users of iDRAC.

dellemc.unity
~~~~~~~~~~~~~

- Adding support for Unity Puffin v5.4.

fortinet.fortios
~~~~~~~~~~~~~~~~

- Add notes for backup modules in the documentation in both monitor and monitor_fact modules.
- Supported new FOS versions 7.4.2 and 7.4.3, and support data type mac_address in the collection.
- Update all the boolean values to true/false in the documents and examples.
- Update the document of log_fact.
- Update the documentation for the supported versions from latest to a fix version number.
- Update the mismatched version message with version ranges.
- Update the required ansible version to 2.14.
- Update the required ansible version to 2.15.
- Update the supported version ranges instead of concrete version numbers to reduce the collection size.

grafana.grafana
~~~~~~~~~~~~~~~

- Add Grafana Loki role by @voidquark in https://github.com/grafana/grafana-ansible-collection/pull/188
- Add Grafana Mimir role by @GVengelen in https://github.com/grafana/grafana-ansible-collection/pull/183
- Add a new config part to configure KeyCloak based auth by @he0s in https://github.com/grafana/grafana-ansible-collection/pull/191
- Add an Ansible role for Grafana Alloy by @ishanjainn in https://github.com/grafana/grafana-ansible-collection/pull/169
- Add an Ansible role for OpenTelemetry Collector by @ishanjainn in https://github.com/grafana/grafana-ansible-collection/pull/138
- Add promtail role by @voidquark in https://github.com/grafana/grafana-ansible-collection/pull/197
- Bump ansible-lint from 24.2.2 to 24.2.3 by @dependabot in https://github.com/grafana/grafana-ansible-collection/pull/195

ibm.qradar
~~~~~~~~~~

- Bumping `requires_ansible` to `>=2.14.0`, since previous ansible-core versions are EoL now.

infoblox.nios_modules
~~~~~~~~~~~~~~~~~~~~~

- Upgrade Ansible version support from 2.13 to 2.16.
- Upgrade Python version support from 3.8 to 3.10.

junipernetworks.junos
~~~~~~~~~~~~~~~~~~~~~

- Bumping `requires_ansible` to `>=2.14.0`, since previous ansible-core versions are EoL now.
- This release removes previously deprecated modules from this collection. Please refer to the **Removed Features** section for details.
- Update the netcommon base version 6.1.0 to support cli_restore plugin.

splunk.es
~~~~~~~~~

- Bumping `requires_ansible` to `>=2.14.0`, since previous ansible-core versions are EoL now.

Minor Changes
-------------

Ansible-core
~~~~~~~~~~~~

- Add ``dump`` and ``passno`` mount information to facts component (https://github.com/ansible/ansible/issues/80478)
- Added MIRACLE LINUX 9.2 in RedHat OS Family.
- Interpreter Discovery - Remove hardcoded references to specific python interpreters to use for certain distro versions, and modify logic for python3 to become the default.
- Use Python's built-in ``functools.update_wrapper`` instead an inline copy from Python 3.7.
- User can now set ansible.log to record higher verbosity than what is specified for display via new configuration item LOG_VERBOSITY.
- ``DEFAULT_PRIVATE_ROLE_VARS`` is now overridden by explicit setting of ``public`` for ``include_roles`` and ``import_roles``.
- ``ansible-galaxy role|collection init`` - accept ``--extra-vars`` to supplement/override the variables ``ansible-galaxy`` injects for templating ``.j2`` files in the skeleton.
- ``import_role`` action now also gets a ``public`` option that controls variable exports,  default depending on ``DEFAULT_PRIVATE_ROLE_VARS`` (if using defaults equates to ``public=True``).
- added configuration item ``TARGET_LOG_INFO`` that allows the user/author to add an information string to the log output on targets.
- ansible-doc - treat double newlines in documentation strings as paragraph breaks. This is useful to create multi-paragraph notes in module/plugin documentation (https://github.com/ansible/ansible/pull/82465).
- ansible-doc output has been revamped to make it more visually pleasing when going to a terminal, also more concise, use -v to show extra information.
- ansible-galaxy - Started normalizing build directory with a trailing separator when building collections, internally. (https://github.com/ansible/ansible/pull/81619).
- ansible-galaxy dependency resolution messages have changed the unexplained 'virtual' collection for the specific type ('scm', 'dir', etc) that is more user friendly
- ansible-test - Add Alpine 3.19 container.
- ansible-test - Add Alpine 3.19 to remotes.
- ansible-test - Add Fedora 39 container.
- ansible-test - Add Fedora 39 remote.
- ansible-test - Add a work-around for permission denied errors when using ``pytest >= 8`` on multi-user systems with an installed version of ``ansible-test``.
- ansible-test - Add support for RHEL 9.3 remotes.
- ansible-test - Added a macOS 14.3 remote VM.
- ansible-test - Bump the ``nios-test-container`` from version 2.0.0 to version 3.0.0.
- ansible-test - Containers and remotes managed by ansible-test will have their Python ``EXTERNALLY-MANAGED`` marker (PEP668) removed. This provides backwards compatibility for existing tests running in newer environments which mark their Python as externally managed. A future version of ansible-test may change this behavior, requiring tests to be adapted to such environments.
- ansible-test - Make Python 3.12 the default version used in the ``base`` and ``default`` containers.
- ansible-test - Remove Alpine 3(.18) container.
- ansible-test - Remove Alpine 3.18 from remotes.
- ansible-test - Remove Fedora 38 remote support.
- ansible-test - Remove Fedora 38 test container.
- ansible-test - Remove rhel/9.2 test remote
- ansible-test - Remove the FreeBSD 13.2 remote.
- ansible-test - Removed fallback to ``virtualenv`` when ``-m venv`` is non-functional.
- ansible-test - Removed test remotes: macos/13.2
- ansible-test - Removed the ``no-basestring`` sanity test. The test is no longer necessary now that Python 3 is required.
- ansible-test - Removed the ``no-dict-iteritems``, ``no-dict-iterkeys`` and ``no-dict-itervalues`` sanity tests. The tests are no longer necessary since Python 3 is required.
- ansible-test - Removed the ``no-main-display`` sanity test. The unwanted pattern is unlikely to occur, since the test has existed since Ansible 2.8.
- ansible-test - Removed the ``no-unicode-literals`` sanity test. The test is unnecessary now that Python 3 is required and the ``unicode_literals`` feature has no effect.
- ansible-test - Special handling for installation of ``cryptography`` has been removed, as it is no longer necessary.
- ansible-test - The ``shellcheck`` sanity test no longer disables the ``SC2164`` check. In most cases, seeing this error means the script is missing ``set -e``.
- ansible-test - The ``unidiomatic-typecheck`` rule has been enabled in the ``pylint`` sanity test.
- ansible-test - The ``unidiomatic-typecheck`` rule has been removed from the ``validate-modules`` sanity test.
- ansible-test - Update the base and default containers to use Ubuntu 22.04 for the base image. This also updates PowerShell to version 7.4.0 with .NET 8.0.0 and ShellCheck to version 0.8.0.
- ansible-test - Updated the CloudStack test container to version 1.7.0.
- ansible-test - Updated the distro test containers to version 6.3.0 to include coverage 7.3.2 for Python 3.8+. The alpine3 container is now based on 3.18 instead of 3.17 and includes Python 3.11 instead of Python 3.10.
- ansible-test - Updated the distro test containers to version 7.1.0.
- ansible-test - When ansible-test installs requirements, it now instructs pip to allow installs on externally managed environments as defined by PEP 668. This only occurs in ephemeral environments managed by ansible-test, such as containers, or when the `--requirements` option is used.
- ansible-test - When invoking ``sleep`` in containers during container setup, the ``env`` command is used to avoid invoking the shell builtin, if present.
- ansible-test - document block name now included in error message for YAML parsing errors (https://github.com/ansible/ansible/issues/82353).
- ansible-test - sanity test allows ``EXAMPLES`` to be multi-document YAML (https://github.com/ansible/ansible/issues/82353).
- ansible-test now has FreeBSD 13.3 and 14.0 support
- ansible.builtin.user - Remove user not found warning (https://github.com/ansible/ansible/issues/80267)
- apt_repository.py - use api.launchpad.net endpoint instead of launchpad.net/api
- async tasks can now also support check mode at the same time.
- async_status now supports check mode.
- constructed inventory plugin - Adding a note that only group_vars of explicit groups are loaded (https://github.com/ansible/ansible/pull/82580).
- csvfile - add a keycol parameter to specify in which column to search.
- dnf - add the ``best`` option
- dnf5 - add the ``best`` option
- filter plugin - Add the count and mandatory_count parameters in the regex_replace filter
- find - add a encoding parameter to specify which encoding of the files to be searched.
- git module - gpg_allowlist name was added in 2.17 and we will eventually deprecate the gpg_whitelist alias.
- import_role - allow subdirectories with ``_from`` options for parity with ``include_role`` (https://github.com/ansible/ansible/issues/82584).
- module argument spec - Allow module authors to include arbitrary additional context in the argument spec, by making use of a new top level key called ``context``. This key should be a dict type. This allows for users to customize what they place in the argument spec, without having to ignore sanity tests that validate the schema.
- modules - Add the ability for an action plugin to call ``self._execute_module(*, ignore_unknown_opts=True)`` to execute a module with options that may not be supported for the version being called. This tells the module basic wrapper to ignore validating the options provided match the arg spec.
- package action now has a configuration that overrides the detected package manager, it is still overridden itself by the use option.
- py3compat - Remove ``ansible.utils.py3compat`` as it is no longer necessary
- removed the unused argument ``create_new_password`` from ``CLI.build_vault_ids`` (https://github.com/ansible/ansible/pull/82066).
- urls - Add support for TLS 1.3 post handshake certificate authentication - https://github.com/ansible/ansible/issues/81782
- urls - reduce complexity of ``Request.open``
- user - accept yescrypt hash as user password
- validate-modules tests now correctly handles ``choices`` in dictionary format.

amazon.aws
~~~~~~~~~~

- AnsibeAWSModule - added ``fail_json_aws_error()`` as a wrapper for ``fail_json()`` and ``fail_json_aws()`` when passed an ``AnsibleAWSError`` exception (https://github.com/ansible-collections/amazon.aws/pull/1997).
- autoscaling_group - minor PEP8 whitespace sanity fixes (https://github.com/ansible-collections/amazon.aws/pull/1846).
- autoscaling_group - removed unused code (https://github.com/ansible-collections/amazon.aws/pull/1996).
- backup_plan - Let user to set ``schedule_expression_timezone`` for backup plan rules when when using botocore >= 1.31.36 (https://github.com/ansible-collections/amazon.aws/issues/1952).
- cloudformation - apply automatic retries when paginating through stack events without a filter (https://github.com/ansible-collections/amazon.aws/pull/2049).
- cloudtrail - removed unused code (https://github.com/ansible-collections/amazon.aws/pull/1996).
- ec2_ami_info - simplify parameters to ``get_image_attribute`` to only pass ID of image (https://github.com/ansible-collections/amazon.aws/pull/1846).
- ec2_eip - use ``ResourceTags`` to set initial tags upon creation (https://github.com/ansible-collections/amazon.aws/issues/1843)
- ec2_instance - Add support for modifying metadata options of an existing instance (https://github.com/ansible-collections/amazon.aws/pull/1918).
- ec2_instance - add support for AdditionalInfo option when creating an instance (https://github.com/ansible-collections/amazon.aws/pull/1828).
- ec2_instance - add support for ``host`` option in placement.tenancy (https://github.com/ansible-collections/amazon.aws/pull/2026).
- ec2_instance - removed unused code (https://github.com/ansible-collections/amazon.aws/pull/1996).
- ec2_security_group - use ``ResourceTags`` to set initial tags upon creation (https://github.com/ansible-collections/amazon.aws/pull/1844)
- ec2_vol - Ensure volume state is not one of ``deleted`` or ``deleting`` when trying to delete volume, to guaranty idempotency (https://github.com/ansible-collections/amazon.aws/pull/2052).
- ec2_vol - removed unused code (https://github.com/ansible-collections/amazon.aws/pull/1996).
- ec2_vpc_igw - use ``ResourceTags`` to set initial tags upon creation (https://github.com/ansible-collections/amazon.aws/issues/1843)
- ec2_vpc_route_table - use ``ResourceTags`` to set initial tags upon creation (https://github.com/ansible-collections/amazon.aws/issues/1843)
- ec2_vpc_subnet - the default value for ``tags`` has been changed from ``{}`` to ``None``, to remove tags from a subnet an empty map must be explicitly passed to the module (https://github.com/ansible-collections/amazon.aws/pull/1876).
- ec2_vpc_subnet - use ``ResourceTags`` to set initial tags upon creation (https://github.com/ansible-collections/amazon.aws/issues/1843)
- ec2_vpc_subnet - use ``wait_timeout`` to also control maximum time to wait for initial creation of subnets (https://github.com/ansible-collections/amazon.aws/pull/1848).
- elb_classic_lb - removed unused code (https://github.com/ansible-collections/amazon.aws/pull/1996).
- iam_access_key - refactored code to use ``AnsibleIAMError`` and ``IAMErrorHandler`` as well as moving shared code into module_utils.iam (https://github.com/ansible-collections/amazon.aws/pull/1998).
- iam_access_key_info - refactored code to use ``AnsibleIAMError`` and ``IAMErrorHandler`` as well as moving shared code into module_utils.iam (https://github.com/ansible-collections/amazon.aws/pull/1998).
- iam_group - Basic testing of ``name`` and ``path`` has been added to improve error messages (https://github.com/ansible-collections/amazon.aws/pull/1933).
- iam_group - ``group_name`` has been added as an alias to ``name`` for consistency with other IAM modules (https://github.com/ansible-collections/amazon.aws/pull/1933).
- iam_group - add support for setting group path (https://github.com/ansible-collections/amazon.aws/pull/1892).
- iam_group - adds attached_policies return value (https://github.com/ansible-collections/amazon.aws/pull/1892).
- iam_group - code refactored to avoid single long function (https://github.com/ansible-collections/amazon.aws/pull/1892).
- iam_group - refactored code to use ``AnsibleIAMError`` and ``IAMErrorHandler`` as well as moving shared code into module_utils.iam (https://github.com/ansible-collections/amazon.aws/pull/1998).
- iam_instance_profile - Basic testing of ``name`` and ``path`` has been added to improve error messages (https://github.com/ansible-collections/amazon.aws/pull/1933).
- iam_instance_profile - attempting to change the ``path`` for an existing profile will now generate a warning, previously this was silently ignored (https://github.com/ansible-collections/amazon.aws/pull/1933).
- iam_instance_profile - refactored code to use ``AnsibleIAMError`` and ``IAMErrorHandler`` as well as moving shared code into module_utils.iam (https://github.com/ansible-collections/amazon.aws/pull/1998).
- iam_instance_profile - the ``prefix`` parameter has been renamed ``path`` for consistency with other IAM modules, ``prefix`` remains as an alias. No change to playbooks is required (https://github.com/ansible-collections/amazon.aws/pull/1933).
- iam_instance_profile - the default value for ``path`` has been removed.  New instances will still be created with a default path of ``/``. No change to playbooks is required (https://github.com/ansible-collections/amazon.aws/pull/1933).
- iam_instance_profile_info - refactored code to use ``AnsibleIAMError`` and ``IAMErrorHandler`` as well as moving shared code into module_utils.iam (https://github.com/ansible-collections/amazon.aws/pull/1998).
- iam_managed_policy - Basic testing of ``name`` and ``path`` has been added to improve error messages (https://github.com/ansible-collections/amazon.aws/pull/1933).
- iam_managed_policy - ``description`` attempting to update the description now results in a warning, previously it was simply ignored (https://github.com/ansible-collections/amazon.aws/pull/1936).
- iam_managed_policy - ``policy`` is no longer a required parameter (https://github.com/ansible-collections/amazon.aws/pull/1936).
- iam_managed_policy - added support for tagging managed policies (https://github.com/ansible-collections/amazon.aws/pull/1936).
- iam_managed_policy - more consistently perform retries on rate limiting errors (https://github.com/ansible-collections/amazon.aws/pull/1936).
- iam_managed_policy - refactored code to use ``AnsibleIAMError`` and ``IAMErrorHandler`` as well as moving shared code into module_utils.iam (https://github.com/ansible-collections/amazon.aws/pull/1998).
- iam_managed_policy - support for setting ``path`` (https://github.com/ansible-collections/amazon.aws/pull/1936).
- iam_managed_policy - the ``policy_description`` parameter has been renamed ``description`` for consistency with other IAM modules, ``policy_description`` remains as an alias. No change to playbooks is required (https://github.com/ansible-collections/amazon.aws/pull/1933).
- iam_managed_policy - the ``policy_name`` parameter has been renamed ``name`` for consistency with other IAM modules, ``policy_name`` remains as an alias. No change to playbooks is required (https://github.com/ansible-collections/amazon.aws/pull/1933).
- iam_mfa_device_info - refactored code to use ``AnsibleIAMError`` and ``IAMErrorHandler`` as well as moving shared code into module_utils.iam (https://github.com/ansible-collections/amazon.aws/pull/1998).
- iam_role - Basic testing of ``name`` and ``path`` has been added to improve error messages (https://github.com/ansible-collections/amazon.aws/pull/1933).
- iam_role - ``prefix`` and ``path_prefix`` have been added as aliases to ``path`` for consistency with other IAM modules (https://github.com/ansible-collections/amazon.aws/pull/1933).
- iam_role - ``role_name`` has been added as an alias to ``name`` for consistency with other IAM modules (https://github.com/ansible-collections/amazon.aws/pull/1933).
- iam_role - attempting to change the ``path`` for an existing profile will now generate a warning, previously this was silently ignored (https://github.com/ansible-collections/amazon.aws/pull/1933).
- iam_role - refactored code to use ``AnsibleIAMError`` and ``IAMErrorHandler`` as well as moving shared code into module_utils.iam (https://github.com/ansible-collections/amazon.aws/pull/1998).
- iam_role - the default value for ``path`` has been removed.  New roles will still be created with a default path of ``/``. No change to playbooks is required (https://github.com/ansible-collections/amazon.aws/pull/1933).
- iam_role_info - ``path`` and ``prefix`` have been added as aliases to ``path_prefix`` for consistency with other IAM modules (https://github.com/ansible-collections/amazon.aws/pull/1933).
- iam_role_info - refactored code to use ``AnsibleIAMError`` and ``IAMErrorHandler`` as well as moving shared code into module_utils.iam (https://github.com/ansible-collections/amazon.aws/pull/1998).
- iam_user - Basic testing of ``name`` and ``path`` has been added to improve error messages (https://github.com/ansible-collections/amazon.aws/pull/1933).
- iam_user - ``user_name`` has been added as an alias to ``name`` for consistency with other IAM modules (https://github.com/ansible-collections/amazon.aws/pull/1933).
- iam_user - add ``boundary`` parameter to support managing boundary policy on users (https://github.com/ansible-collections/amazon.aws/pull/1912).
- iam_user - add ``path`` parameter to support managing user path (https://github.com/ansible-collections/amazon.aws/pull/1912).
- iam_user - added ``attached_policies`` to return value (https://github.com/ansible-collections/amazon.aws/pull/1912).
- iam_user - refactored code to reduce complexity (https://github.com/ansible-collections/amazon.aws/pull/1912).
- iam_user - refactored code to use ``AnsibleIAMError`` and ``IAMErrorHandler`` as well as moving shared code into module_utils.iam (https://github.com/ansible-collections/amazon.aws/pull/1998).
- iam_user - refactored error handling to use a decorator (https://github.com/ansible-collections/amazon.aws/pull/1951).
- iam_user_info - Add ``login_profile`` to return info that is get from a user, to know if they can login from AWS console (https://github.com/ansible-collections/amazon.aws/pull/2012).
- iam_user_info - ``prefix`` has been added as an alias to ``path_prefix`` for consistency with other IAM modules (https://github.com/ansible-collections/amazon.aws/pull/1933).
- iam_user_info - refactored code to use ``AnsibleIAMError`` and ``IAMErrorHandler`` as well as moving shared code into module_utils.iam (https://github.com/ansible-collections/amazon.aws/pull/1998).
- iam_user_info - the ``path`` parameter has been renamed ``path_prefix`` for consistency with other IAM modules, ``path`` remains as an alias. No change to playbooks is required (https://github.com/ansible-collections/amazon.aws/pull/1933).
- kms_key - removed unused code (https://github.com/ansible-collections/amazon.aws/pull/1996).
- lambda - added support for using ECR images for the function (https://github.com/ansible-collections/amazon.aws/pull/1939).
- lambda_event - Add support for setting the ``maximum_batching_window_in_seconds`` option (https://github.com/ansible-collections/amazon.aws/pull/2025).
- module_uils/botocore - support sets and tuples of errors as well as lists (https://github.com/ansible-collections/amazon.aws/pull/1829).
- module_utils.errors - added a basic error handler decorator (https://github.com/ansible-collections/amazon.aws/pull/1951).
- module_utils.iam - refactored normalization functions to use ``boto3_resource_to_ansible_dict()`` and ``boto3_resource_list_to_ansible_dict()`` (https://github.com/ansible-collections/amazon.aws/pull/2006).
- module_utils.transformations - add ``boto3_resource_to_ansible_dict()`` and ``boto3_resource_list_to_ansible_dict()`` helpers (https://github.com/ansible-collections/amazon.aws/pull/2006).
- module_utils/elbv2 - Add support for adding listener with multiple certificates during ALB creation. Allows elb_application_elb module to handle mentioned use case. (https://github.com/ansible-collections/amazon.aws/pull/1950).
- module_utils/elbv2 - Add the possibility to update ``SslPolicy``, ``Certificates`` and ``AlpnPolicy`` for TLS listeners (https://github.com/ansible-collections/amazon.aws/issues/1198).
- rds_cluster - Add support for ServerlessV2ScalingConfiguration to create and modify cluster operations (https://github.com/ansible-collections/amazon.aws/pull/1839).
- rds_instance - Allow passing empty list to ``enable_cloudwatch_logs_exports`` in order to remove all existing exports (https://github.com/ansible-collections/amazon.aws/pull/1917).
- rds_instance_snapshot - minor PEP8 whitespace sanity fixes (https://github.com/ansible-collections/amazon.aws/pull/1846).
- s3_bucket - refactor s3_bucket module code for improved readability and maintainability (https://github.com/ansible-collections/amazon.aws/pull/2057).
- s3_bucket_info - add parameter ``bucket_versioning`` to return the versioning state of a bucket (https://github.com/ansible-collections/amazon.aws/pull/1919).
- s3_object - removed unused code (https://github.com/ansible-collections/amazon.aws/pull/1996).
- s3_object_info - fix exception raised when listing objects from empty bucket (https://github.com/ansible-collections/amazon.aws/pull/1919).

ansible.netcommon
~~~~~~~~~~~~~~~~~

- Add new module cli_restore that exclusively handles restoring of backup configuration to target applaince.

ansible.utils
~~~~~~~~~~~~~

- Add support in fact_diff filter plugin to show common lines.(https://github.com/ansible-collections/ansible.utils/issues/311)
- Fact_diff filter plugin - Add fact_diff filter plugin. (https://github.com/ansible-collections/ansible.utils/issues/78).

ansible.windows
~~~~~~~~~~~~~~~

- Set minimum supported Ansible version to 2.14 to align with the versions still supported by Ansible.
- win_share - Added a new param called ``scope_name`` that allows file shares to be scoped for Windows Server failover cluster roles.
- win_uri - Max depth for json object conversion used to be 2. Can now send json objects with up to 20 levels of nesting

arista.eos
~~~~~~~~~~

- Add support for cli_restore functionality.
- Please refer the PR to know more about core changes (https://github.com/ansible-collections/ansible.netcommon/pull/618).
- cli_restore module is part of netcommon.

check_point.mgmt
~~~~~~~~~~~~~~~~

- New resource modules for R81.20 JHF Take 43
- meta/runtime.yml - update minimum Ansible version required to 2.14.0.

cisco.aci
~~~~~~~~~

- Add Authentification option for EIGRP interface profile.
- Add L3out Floating SVI modules (aci_l3out_floating_svi, aci_l3out_floating_svi_path, aci_l3out_floating_svi_path_secondary_ip and aci_l3out_floating_svi_secondary_ip) (#478)
- Add No-verification flag option to reduce the number of API calls. If true, a verifying GET will not be sent after a POST update to APIC
- Add access spine interface selector and port block binding in aci_access_port_block_to_access_port
- Add aci_access_spine_interface_selector module
- Add aci_action_rule_additional_communities module
- Add aci_action_rule_set_as_path and aci_action_rule_set_as_path_asn modules
- Add aci_bgp_peer_prefix_policy, aci_bgp_route_summarization_policy and aci_bgp_address_family_context_policy modules
- Add aci_fabric_pod, aci_fabric_pod_external_tep, aci_fabric_pod_profile, aci_fabric_pod_remote_pool modules (#558)
- Add aci_hsrp_interface_policy, aci_l3out_hsrp_group, aci_l3out_hsrp_interface_profile and aci_l3out_hsrp_secondary_vip modules (#505)
- Add aci_interface_policy_eigrp (class:eigrpIfPol) module
- Add aci_interface_policy_pim module
- Add aci_interface_policy_storm_control module
- Add aci_keychain_policy and aci_key_policy modules
- Add aci_l3out_bfd_multihop_interface_profile, aci_l3out_bfd_interface_profile, aci_interface_policy_bfd_multihop, aci_interface_policy_bfd and aci_bfd_multihop_node_policy modules (#492)
- Add aci_l3out_dhcp_relay_label, aci_dhcp_option_policy and aci_dhcp_option modules
- Add aci_l3out_eigrp_interface_profile module
- Add aci_listify filter plugin to flattens nested dictionaries
- Add aci_netflow_exporter_policy module
- Add aci_netflow_monitor_policy and aci_netflow_record_policy modules
- Add aci_netflow_monitor_to_exporter module
- Add aci_node_block module
- Add aci_pim_route_map_policy and aci_pim_route_map_entry modules
- Add aci_qos_custom_policy and aci_qos_dscp_class modules
- Add aci_qos_dot1p_class module
- Add action rules attributes to aci_tenant_action_rule_profile.
- Add auto to speed attribute options in aci_interface_policy_link_level module (#577)
- Add missing options to aci_bd module
- Add modules aci_bd_to_netflow_monitor_policy and aci_bd_rogue_exception_mac (#600)
- Add modules for Fabric External Connection Policies and its childs
- Add option to set delimiter to  _  in aci_epg_to_domain module
- Add qos_custom_policy, pim_interface_policy and igmp_interface_policy as new child_classes for aci_l3out_logical_interface_profile.
- Add support for annotation in aci_rest module (#437)
- Add support for block statements in useg attributes with the aci_epg_useg_attribute_block_statement module
- Add support for configuration of access switch policy groups with aci_access_switch_policy_group module
- Add support for configuration of certificate authorities in aci_aaa_certificate_authority
- Add support for configuration of fabric management access policies in aci_fabric_management_access
- Add support for configuration of vrf multicast with aci_vrf_multicast module
- Add support for configuring Azure cloud subnets using the aci_cloud_subnet module
- Add support for encap scope in aci_l3out_interface
- Add support for https ssl cipher configuration in aci_fabric_management_access_https_cipher
- Add support for infra l3out nodes bgp-evpn loopback, mpls transport loopback and segment id in aci_l3out_logical_node
- Add support for infra sr mpls micro bfd in aci_l3out_interface
- Add support for intra epg, taboo, and contract interface in aci_epg_to_contract
- Add support for key ring configuration in aci_aaa_key_ring
- Add support for mac and description in aci_l3out_interface
- Add support for mpls custom qos policy for infra sr mpls l3outs node profiles in aci_l3out_logical_node_profile
- Add support for security default settings configuration in aci_aaa_security_default_settings
- Add support for simple statements in useg attributes with the aci_epg_useg_attribute_simple_statement module
- Add support for sr-mpls bgpInfraPeerP and bgp_password in aci_l3out_bgp_peer module (#543)
- Add support for sr-mpls in aci_l3out module
- Add support for sr-mpls l3out to infra l3out in aci_l3out_to_sr_mpls_infra_l3out
- Add support for subject labels for EPG, EPG Contract, ESG, Contract Subject, L2Out External EPG, L3out External EPG, and L3out External EPG Contract with the aci_subject_label module
- Add support for taboo contract, contract interface and intra_epg contract in aci_l3out_extepg_to_contract
- Add support for useg default block statement configuration for useg epg in aci_epg
- Modify child class node block conditions to be optional in aci_switch_leaf_selector

cisco.dnac
~~~~~~~~~~

- Added a method to validate IP addresses.
- Added attributes 'dnac_api_task_timeout' and 'dnac_task_poll_interval' in intent and workflow_manager modules.
- Added the op_modifies=True when calling SDK APIs in the workflow manager modules.
- Adding support to importing a template using JSON file
- Addressed image un-tagging issues in inherited site settings.
- Changes in discovery workflow manager modules  relating to different states of the discovery job
- Changes the minimum supported version from Ansible v2.9.10 to v2.14.0
- Corrected site creation issues in the site module when optional parameters are missing.
- Fixed a minor issue in the site workflow manager module.
- Fixed management IP updates for devices on SNMP version v2.
- Introduced sample playbooks for the discovery module.
- Provided documentation for EWLC templates in Cisco Catalyst Center version 2.3.7.x.
- Resolved a 'NoneType' error in discovery module credentials.
- Updating galaxy.yml ansible.utils dependencies.
- inventory_workflow_manager - Added attributes 'add_user_defined_field', 'update_interface_details', 'export_device_list' and 'admin_status'
- inventory_workflow_manager - Removed attributes 'provision_wireless_device', 'reprovision_wired_device'

cisco.ios
~~~~~~~~~

- Add support for cli_restore functionality.
- Added ios_evpn_evi resource module.
- Added ios_evpn_global resource module.
- Added ios_vxlan_vtep resource module.
- Fixed ios_evpn_evi resource module integration test failure - code to remove VLAN config.
- Please refer the PR to know more about core changes (https://github.com/ansible-collections/ansible.netcommon/pull/618).
- cli_restore module is part of netcommon.
- ios_bgp_address_family - Fixed an issue with inherit peer-policy CLI
- ios_bgp_address_family - added 'advertise' key
- ios_bgp_global - added 'bgp.default.ipv4_unicast' and 'bgp.default.route_target.filter' key
- ios_l3_interfaces - added 'autostate', 'mac_address', 'ipv4.source_interface', and 'ipv6.enable' key
- ios_vlans - Add purged state to deal with toplevel vlan and vlan configuration config.
- ios_vlans - added vlan config CLI feature.
- ios_vrf - added MDT related keys

cisco.iosxr
~~~~~~~~~~~

- Add missing options in afi and safi in address-family of bgp_templates RM.
- Add support for cli_restore functionality.
- Please refer the PR to know more about core changes (https://github.com/ansible-collections/ansible.netcommon/pull/618).
- cli_restore module is part of netcommon.
- iosxr_facts - Add cdp neighbors in ansible_net_neighbors dictionary (https://github.com/ansible-collections/cisco.iosxr/pull/457).

cisco.ise
~~~~~~~~~

- Changes the minimum supported version from Ansible v2.9.10 to v2.14.0
- Services included configuration, edda, dataconnect_services, subscriber.
- cisco.ise collection now supports ansible.utils v3

cisco.meraki
~~~~~~~~~~~~

- Adding support to ansible.utils ">=2.0.0, <4.00".
- Ansible collection now support v1.44.1 of Dashboard Api.
- Fixing problem of naming in `organizations_appliance_vpn_third_party_vpnpeers_info`.
- Removing `state` from allowed parameters for `networks_syslog_servers` module.
- The `id` parameter is change type to an `integer` in `networks_appliance_vlans` module.
- The `id` parameter is now required for `networks_appliance_vlans` module.
- administered_licensing_subscription_entitlements_info - new plugin.
- administered_licensing_subscription_subscriptions_bind - new plugin.
- administered_licensing_subscription_subscriptions_claim - new plugin.
- administered_licensing_subscription_subscriptions_claim_key_validate - new plugin.
- administered_licensing_subscription_subscriptions_compliance_statuses_info - new plugin.
- administered_licensing_subscription_subscriptions_info - new plugin.
- devices_appliance_radio_settings - new plugin.
- devices_appliance_radio_settings_info - new plugin.
- devices_live_tools_arp_table - new plugin.
- devices_live_tools_arp_table_info - new plugin.
- devices_live_tools_cable_test - new plugin.
- devices_live_tools_cable_test_info - new plugin.
- devices_live_tools_throughput_test - new plugin.
- devices_live_tools_throughput_test_info - new plugin.
- devices_live_tools_wake_on_lan - new plugin.
- devices_live_tools_wake_on_lan_info - new plugin.
- devices_wireless_alternate_management_interface_ipv6 - new plugin.
- networks_appliance_rf_profiles - new plugin.
- networks_appliance_rf_profiles_info - new plugin.
- networks_appliance_traffic_shaping_vpn_exclusions - new plugin.
- networks_sm_devices_install_apps - new plugin.
- networks_sm_devices_reboot - new plugin.
- networks_sm_devices_shutdown - new plugin.
- networks_sm_devices_uninstall_apps - new plugin.
- networks_vlan_profiles - new plugin.
- networks_vlan_profiles_assignments_by_device_info - new plugin.
- networks_vlan_profiles_assignments_reassign - new plugin.
- networks_vlan_profiles_info - new plugin.
- networks_wireless_ethernet_ports_profiles - new plugin.
- networks_wireless_ethernet_ports_profiles_assign - new plugin.
- networks_wireless_ethernet_ports_profiles_info - new plugin.
- networks_wireless_ethernet_ports_profiles_set_default - new plugin.
- organizations_appliance_traffic_shaping_vpn_exclusions_by_network_info - new plugin.
- organizations_appliance_uplinks_statuses_overview_info - new plugin.
- organizations_appliance_uplinks_usage_by_network_info - new plugin.
- organizations_camera_boundaries_areas_by_device_info - new plugin.
- organizations_camera_boundaries_lines_by_device_info - new plugin.
- organizations_camera_detections_history_by_boundary_by_interval_info - new plugin.
- organizations_camera_permissions_info - new plugin.
- organizations_camera_roles - new plugin.
- organizations_camera_roles_info - new plugin.
- organizations_devices_availabilities_change_history_info - new plugin.
- organizations_devices_boots_history_info - new plugin.
- organizations_sm_admins_roles - new plugin.
- organizations_sm_admins_roles_info - new plugin.
- organizations_sm_sentry_policies_assignments - new plugin.
- organizations_sm_sentry_policies_assignments_by_network_info - new plugin.
- organizations_summary_top_networks_by_status_info - new plugin.
- organizations_webhooks_callbacks_statuses_info - new plugin.
- organizations_wireless_devices_channel_utilization_by_device_info - new plugin.
- organizations_wireless_devices_channel_utilization_by_network_info - new plugin.
- organizations_wireless_devices_channel_utilization_history_by_device_by_interval_info - new plugin.
- organizations_wireless_devices_channel_utilization_history_by_network_by_interval_info - new plugin.
- organizations_wireless_devices_packet_loss_by_client_info - new plugin.
- organizations_wireless_devices_packet_loss_by_device_info - new plugin.
- organizations_wireless_devices_packet_loss_by_network_info - new plugin.

cisco.mso
~~~~~~~~~

- Add Azure Cloud site support to mso_schema_site_contract_service_graph
- Add Azure Cloud site support to mso_schema_site_service_graph
- Add functionality to resolve same name in remote and local user.
- Add l3out_template and l3out_schema arguments to mso_schema_site_external_epg (#394)
- Add mso_schema_site_contract_service_graph module to manage site contract service graph
- Add mso_schema_site_contract_service_graph_listener module to manage Azure site contract service graph listeners and update other modules
- Add new parameter remote_user to add multiple remote users associated with multiple login domains
- Add support for replacing all existing contracts with new provided contracts in a single operation with one request and adding/removing multiple contracts in multiple operations with a single request in mso_schema_template_anp_epg_contract module
- Add support for replacing all existing static ports with new provided static ports in a single operation with one request and adding/removing multiple static ports in multiple operations with a single request in mso_schema_template_anp_epg_staticport module
- Add support for required attributes introduced in NDO 4.2 for mso_schema_site_anp_epg_domain
- Support for creation of schemas without templates with the mso_schema module

cisco.nxos
~~~~~~~~~~

- Add support for cli_restore functionality.
- Please refer the PR to know more about core changes (https://github.com/ansible-collections/ansible.netcommon/pull/618). The cli_restore module is a part of ansible.netcommon.
- nxos_config - Relax restrictions on I(src) parameter so it can be used more like I(lines). (https://github.com/ansible-collections/cisco.nxos/issues/89).

community.aws
~~~~~~~~~~~~~

- api_gateway - use fstrings where appropriate (https://github.com/ansible-collections/amazon.aws/pull/1962).
- api_gateway_info - use fstrings where appropriate (https://github.com/ansible-collections/amazon.aws/pull/1962).
- aws_ssm - Updated the documentation to explicitly state that an S3 bucket is required, the behavior of the files in that bucket, and requirements around that. (https://github.com/ansible-collections/community.aws/issues/1775).
- cloudfront_distribution - added support for ``cache_policy_id`` and ``origin_request_policy_id`` for behaviors (https://github.com/ansible-collections/community.aws/pull/1589)
- community.aws collection - apply isort code formatting to ensure consistent formatting of code (https://github.com/ansible-collections/community.aws/pull/1962)
- ecs_taskdefinition - Add parameter ``runtime_platform`` (https://github.com/ansible-collections/community.aws/issues/1891).
- eks_nodegroup - ensure wait also waits for deletion to complete when ``wait==True`` (https://github.com/ansible-collections/community.aws/pull/1994).
- elb_network_lb - add support for Application-Layer Protocol Negotiation (ALPN) policy ``AlpnPolicy`` for TLS listeners (https://github.com/ansible-collections/community.aws/issues/1566).
- elb_network_lb - add the possibly to update ``SslPolicy`` and ``Certificates`` for TLS listeners ().
- glue_job - add support for 2 new instance types which are G.4X and G.8X (https://github.com/ansible-collections/community.aws/pull/2048).
- mq_broker - add support to wait for broker state via ``wait`` and ``wait_timeout`` parameter values (https://github.com/ansible-collections/community.aws/pull/1879).
- msk_cluster - Support for additional ``m5`` and ``m7g`` types of MSK clusters (https://github.com/ansible-collections/community.aws/pull/1947).

community.ciscosmb
~~~~~~~~~~~~~~~~~~

- added additional attribute - add interface 'bandwidth' attribute
- docs - addeed info about SG-250 support and testing
- reverted attribute change - keep interface 'bandwith' attribute

community.crypto
~~~~~~~~~~~~~~~~

- When using cryptography >= 42.0.0, use offset-aware ``datetime.datetime`` objects (with timezone UTC) instead of offset-naive UTC timestamps (https://github.com/ansible-collections/community.crypto/issues/726, https://github.com/ansible-collections/community.crypto/pull/727).
- acme_certificate - add ``include_renewal_cert_id`` option to allow requesting renewal of a specific certificate according to the current ACME Renewal Information specification draft (https://github.com/ansible-collections/community.crypto/pull/739).
- luks_device - add allow discards option (https://github.com/ansible-collections/community.crypto/pull/693).
- openssh_cert - avoid UTC functions deprecated in Python 3.12 when using Python 3 (https://github.com/ansible-collections/community.crypto/pull/727).
- x509_crl - the new option ``serial_numbers`` allow to configure in which format serial numbers can be provided to ``revoked_certificates[].serial_number``. The default is as integers (``serial_numbers=integer``) for backwards compatibility; setting ``serial_numbers=hex-octets`` allows to specify colon-separated hex octet strings like ``00:11:22:FF`` (https://github.com/ansible-collections/community.crypto/issues/687, https://github.com/ansible-collections/community.crypto/pull/715).

community.digitalocean
~~~~~~~~~~~~~~~~~~~~~~

- digital_ocean_kubernetes - add project_name parameter (https://github.com/ansible-collections/community.digitalocean/issues/264).
- fix sanity tests (https://github.com/ansible-collections/community.digitalocean/issues/323).

community.dns
~~~~~~~~~~~~~

- hetzner_dns_records and hosttech_dns_records inventory plugins - the ``filters`` option has been renamed to ``simple_filters``. The old name still works until community.hrobot 2.0.0. Then it will change to allow more complex filtering with the ``community.library_inventory_filtering_v1`` collection's functionality (https://github.com/ansible-collections/community.dns/pull/181).
- inventory plugins - add ``filter`` option which allows to include and exclude hosts based on Jinja2 conditions (https://github.com/ansible-collections/community.dns/pull/196).
- lookup, lookup_as_dict - it is now possible to configure whether the input should be treated as an absolute domain name (``search=false``), or potentially as a relative domain name (``search=true``)  (https://github.com/ansible-collections/community.dns/issues/200, https://github.com/ansible-collections/community.dns/pull/201).
- nameserver_info and nameserver_record_info - add ``server`` parameter to specify custom DNS servers (https://github.com/ansible-collections/community.dns/pull/168, https://github.com/ansible-collections/community.dns/pull/178).
- wait_for_txt - add ``server`` parameter to specify custom DNS servers (https://github.com/ansible-collections/community.dns/pull/178).

community.docker
~~~~~~~~~~~~~~~~

- The EE requirements now include PyYAML, since the ``docker_compose_v2*`` modules depend on it when the ``definition`` option is used. This should not have a noticable effect on generated EEs since ansible-core itself depends on PyYAML as well, and ansible-builder explicitly ignores this dependency (https://github.com/ansible-collections/community.docker/pull/832).
- The ``ca_cert`` option available to almost all modules and plugins has been renamed to ``ca_path``. The name ``ca_path`` is also used for similar options in ansible-core and other collections. The old name has been added as an alias and can still be used (https://github.com/ansible-collections/community.docker/pull/744).
- The ``docker_stack*`` modules now use the common CLI-based module code added for the ``docker_image_build`` and ``docker_compose_v2`` modules. This means that the modules now have various more configuration options with respect to talking to the Docker Daemon, and now also are part of the ``community.docker.docker`` and ``docker`` module default groups (https://github.com/ansible-collections/community.docker/pull/745).
- docker_compose_v2 - add ``scale`` option to allow to explicitly scale services (https://github.com/ansible-collections/community.docker/pull/776).
- docker_compose_v2 - allow to wait until containers are running/health when running ``docker compose up`` with the new ``wait`` option (https://github.com/ansible-collections/community.docker/issues/794, https://github.com/ansible-collections/community.docker/pull/796).
- docker_compose_v2* - the new option ``check_files_existing`` allows to disable the check for one of the files ``compose.yaml``, ``compose.yml``, ``docker-compose.yaml``, and ``docker-compose.yml`` in ``project_src`` if ``files`` is not specified. This is necessary if a non-standard compose filename is specified through other means, like the ``COMPOSE_FILE`` environment variable (https://github.com/ansible-collections/community.docker/issues/838, https://github.com/ansible-collections/community.docker/pull/839).
- docker_compose_v2* modules - allow to provide an inline definition of the compose content instead of having to provide a ``project_src`` directory with the compose file written into it (https://github.com/ansible-collections/community.docker/issues/829, https://github.com/ansible-collections/community.docker/pull/832).
- docker_compose_v2, docker_compose_v2_pull - support ``files`` parameter to specify multiple Compose files (https://github.com/ansible-collections/community.docker/issues/772, https://github.com/ansible-collections/community.docker/pull/775).
- docker_container - add ``networks[].mac_address`` option for Docker API 1.44+. Note that Docker API 1.44 no longer uses the global ``mac_address`` option, this new option is the only way to set the MAC address for a container (https://github.com/ansible-collections/community.docker/pull/763).
- docker_container - adds ``healthcheck.start_interval`` to support healthcheck start interval setting on containers (https://github.com/ansible-collections/community.docker/pull/848).
- docker_container - adds ``healthcheck.test_cli_compatible`` to allow omit test option on containers without remove existing image test (https://github.com/ansible-collections/community.docker/pull/847).
- docker_container - implement better ``platform`` string comparisons to improve idempotency (https://github.com/ansible-collections/community.docker/issues/654, https://github.com/ansible-collections/community.docker/pull/705).
- docker_container - internal refactorings which allow comparisons to use more information like details of the current image or the Docker host config (https://github.com/ansible-collections/community.docker/pull/713).
- docker_container - the ``pull_check_mode_behavior`` option now allows to control the module's behavior in check mode when ``pull=always`` (https://github.com/ansible-collections/community.docker/issues/792, https://github.com/ansible-collections/community.docker/pull/797).
- docker_container - the ``pull`` option now accepts the three values ``never``, ``missing_image`` (default), and ``never``, next to the previously valid values ``true`` (equivalent to ``always``) and ``false`` (equivalent to ``missing_image``). This allows the equivalent to ``--pull=never`` from the Docker command line (https://github.com/ansible-collections/community.docker/issues/783, https://github.com/ansible-collections/community.docker/pull/797).
- docker_image - allow to specify labels and ``/dev/shm`` size when building images (https://github.com/ansible-collections/community.docker/issues/726, https://github.com/ansible-collections/community.docker/pull/727).
- docker_image - allow to specify memory size and swap memory size in other units than bytes (https://github.com/ansible-collections/community.docker/pull/727).
- docker_image_build - add ``outputs`` option to allow configuring outputs for the build (https://github.com/ansible-collections/community.docker/pull/852).
- docker_image_build - add ``secrets`` option to allow passing secrets to the build (https://github.com/ansible-collections/community.docker/pull/852).
- docker_image_build - allow ``platform`` to be a list of platforms instead of only a single platform for multi-platform builds (https://github.com/ansible-collections/community.docker/pull/852).
- docker_network - adds ``config_only`` and ``config_from`` to support creating and using config only networks (https://github.com/ansible-collections/community.docker/issues/395).
- docker_prune - add new options ``builder_cache_all``, ``builder_cache_filters``, and ``builder_cache_keep_storage``, and a new return value ``builder_cache_caches_deleted`` for pruning build caches (https://github.com/ansible-collections/community.docker/issues/844, https://github.com/ansible-collections/community.docker/issues/845).
- docker_swarm_service - adds ``sysctls`` to support sysctl settings on swarm services (https://github.com/ansible-collections/community.docker/issues/190).
- inventory plugins - add ``filter`` option which allows to include and exclude hosts based on Jinja2 conditions (https://github.com/ansible-collections/community.docker/pull/698, https://github.com/ansible-collections/community.docker/issues/610).
- vendored Docker SDK for Python - remove unused code that relies on functionality deprecated in Python 3.12 (https://github.com/ansible-collections/community.docker/pull/834).

community.general
~~~~~~~~~~~~~~~~~

- PythonRunner module utils - specialisation of ``CmdRunner`` to execute Python scripts (https://github.com/ansible-collections/community.general/pull/8289).
- Use offset-aware ``datetime.datetime`` objects (with timezone UTC) instead of offset-naive UTC timestamps, which are deprecated in Python 3.12 (https://github.com/ansible-collections/community.general/pull/8222).
- aix_lvol - refactor module to pass list of arguments to ``module.run_command()`` instead of relying on interpretation by a shell (https://github.com/ansible-collections/community.general/pull/8264).
- ansible_galaxy_install - minor refactor in the module (https://github.com/ansible-collections/community.general/pull/8413).
- apt_rpm - add new states ``latest`` and ``present_not_latest``. The value ``latest`` is equivalent to the current behavior of ``present``, which will upgrade a package if a newer version exists. ``present_not_latest`` does what most users would expect ``present`` to do: it does not upgrade if the package is already installed. The current behavior of ``present`` will be deprecated in a later version, and eventually changed to that of ``present_not_latest`` (https://github.com/ansible-collections/community.general/issues/8217, https://github.com/ansible-collections/community.general/pull/8247).
- apt_rpm - refactor module to pass list of arguments to ``module.run_command()`` instead of relying on interpretation by a shell (https://github.com/ansible-collections/community.general/pull/8264).
- bitwarden lookup plugin - add ``bw_session`` option, to pass session key instead of reading from env (https://github.com/ansible-collections/community.general/pull/7994).
- bitwarden lookup plugin - add support to filter by organization ID (https://github.com/ansible-collections/community.general/pull/8188).
- bitwarden lookup plugin - allows to fetch all records of a given collection ID, by allowing to pass an empty value for ``search_value`` when ``collection_id`` is provided (https://github.com/ansible-collections/community.general/pull/8013).
- bitwarden lookup plugin - when looking for items using an item ID, the item is now accessed directly with ``bw get item`` instead of searching through all items. This doubles the lookup speed (https://github.com/ansible-collections/community.general/pull/7468).
- btrfs_subvolume - refactor module to pass list of arguments to ``module.run_command()`` instead of relying on interpretation by a shell (https://github.com/ansible-collections/community.general/pull/8264).
- cmd_runner module_utils - add validation for minimum and maximum length in the value passed to ``cmd_runner_fmt.as_list()`` (https://github.com/ansible-collections/community.general/pull/8288).
- consul_auth_method, consul_binding_rule, consul_policy, consul_role, consul_session, consul_token - added action group ``community.general.consul`` (https://github.com/ansible-collections/community.general/pull/7897).
- consul_policy - added support for diff and check mode (https://github.com/ansible-collections/community.general/pull/7878).
- consul_policy, consul_role, consul_session - removed dependency on ``requests`` and factored out common parts (https://github.com/ansible-collections/community.general/pull/7826, https://github.com/ansible-collections/community.general/pull/7878).
- consul_role - ``node_identities`` now expects a ``node_name`` option to match the Consul API, the old ``name`` is still supported as alias (https://github.com/ansible-collections/community.general/pull/7878).
- consul_role - ``service_identities`` now expects a ``service_name`` option to match the Consul API, the old ``name`` is still supported as alias (https://github.com/ansible-collections/community.general/pull/7878).
- consul_role - added support for diff mode (https://github.com/ansible-collections/community.general/pull/7878).
- consul_role - added support for templated policies (https://github.com/ansible-collections/community.general/pull/7878).
- elastic callback plugin - close elastic client to not leak resources (https://github.com/ansible-collections/community.general/pull/7517).
- filesystem - add bcachefs support (https://github.com/ansible-collections/community.general/pull/8126).
- gandi_livedns - adds support for personal access tokens (https://github.com/ansible-collections/community.general/issues/7639, https://github.com/ansible-collections/community.general/pull/8337).
- gconftool2 - use ``ModuleHelper`` with ``VarDict`` (https://github.com/ansible-collections/community.general/pull/8226).
- git_config - allow multiple git configs for the same name with the new ``add_mode`` option (https://github.com/ansible-collections/community.general/pull/7260).
- git_config - the ``after`` and ``before`` fields in the ``diff`` of the return value can be a list instead of a string in case more configs with the same key are affected (https://github.com/ansible-collections/community.general/pull/7260).
- git_config - when a value is unset, all configs with the same key are unset (https://github.com/ansible-collections/community.general/pull/7260).
- gitlab modules - add ``ca_path`` option (https://github.com/ansible-collections/community.general/pull/7472).
- gitlab modules - remove duplicate ``gitlab`` package check (https://github.com/ansible-collections/community.general/pull/7486).
- gitlab_deploy_key, gitlab_group_members, gitlab_group_variable, gitlab_hook, gitlab_instance_variable, gitlab_project_badge, gitlab_project_variable, gitlab_user - improve API pagination and compatibility with different versions of ``python-gitlab`` (https://github.com/ansible-collections/community.general/pull/7790).
- gitlab_hook - adds ``releases_events`` parameter for supporting Releases events triggers on GitLab hooks (https://github.com/ansible-collections/community.general/pull/7956).
- gitlab_runner - add support for new runner creation workflow (https://github.com/ansible-collections/community.general/pull/7199).
- homebrew - adds ``force_formula`` parameter to disambiguate a formula from a cask of the same name (https://github.com/ansible-collections/community.general/issues/8274).
- homebrew, homebrew_cask - refactor common argument validation logic into a dedicated ``homebrew`` module utils (https://github.com/ansible-collections/community.general/issues/8323, https://github.com/ansible-collections/community.general/pull/8324).
- icinga2 inventory plugin - add Jinja2 templating support to ``url``, ``user``, and ``password`` paramenters (https://github.com/ansible-collections/community.general/issues/7074, https://github.com/ansible-collections/community.general/pull/7996).
- icinga2 inventory plugin - adds new parameter ``group_by_hostgroups`` in order to make grouping by Icinga2 hostgroups optional (https://github.com/ansible-collections/community.general/pull/7998).
- ini_file - add an optional parameter ``section_has_values``. If the target ini file contains more than one ``section``, use ``section_has_values`` to specify which one should be updated (https://github.com/ansible-collections/community.general/pull/7505).
- ini_file - support optional spaces between section names and their surrounding brackets (https://github.com/ansible-collections/community.general/pull/8075).
- installp - refactor module to pass list of arguments to ``module.run_command()`` instead of relying on interpretation by a shell (https://github.com/ansible-collections/community.general/pull/8264).
- ipa_config - adds ``passkey`` choice to ``ipauserauthtype`` parameter's choices (https://github.com/ansible-collections/community.general/pull/7588).
- ipa_dnsrecord - adds ability to manage NS record types (https://github.com/ansible-collections/community.general/pull/7737).
- ipa_pwpolicy - refactor module and exchange a sequence ``if`` statements with a ``for`` loop (https://github.com/ansible-collections/community.general/pull/7723).
- ipa_pwpolicy - update module to support ``maxrepeat``, ``maxsequence``, ``dictcheck``, ``usercheck``, ``gracelimit`` parameters in FreeIPA password policies (https://github.com/ansible-collections/community.general/pull/7723).
- ipa_sudorule - adds options to include denied commands or command groups (https://github.com/ansible-collections/community.general/pull/7415).
- ipa_user - adds ``idp`` and ``passkey`` choice to ``ipauserauthtype`` parameter's choices (https://github.com/ansible-collections/community.general/pull/7589).
- irc - add ``validate_certs`` option, and rename ``use_ssl`` to ``use_tls``, while keeping ``use_ssl`` as an alias. The default value for ``validate_certs`` is ``false`` for backwards compatibility. We recommend to every user of this module to explicitly set ``use_tls=true`` and `validate_certs=true`` whenever possible, especially when communicating to IRC servers over the internet (https://github.com/ansible-collections/community.general/pull/7550).
- java_cert - add ``cert_content`` argument (https://github.com/ansible-collections/community.general/pull/8153).
- java_cert - enable ``owner``, ``group``, ``mode``, and other generic file arguments (https://github.com/ansible-collections/community.general/pull/8116).
- kernel_blacklist - use ``ModuleHelper`` with ``VarDict`` (https://github.com/ansible-collections/community.general/pull/8226).
- keycloak module utils - expose error message from Keycloak server for HTTP errors in some specific situations (https://github.com/ansible-collections/community.general/pull/7645).
- keycloak_client, keycloak_clientscope, keycloak_clienttemplate - added ``docker-v2`` protocol support, enhancing alignment with Keycloak's protocol options (https://github.com/ansible-collections/community.general/issues/8215, https://github.com/ansible-collections/community.general/pull/8216).
- keycloak_realm_key - the ``config.algorithm`` option now supports 8 additional key algorithms (https://github.com/ansible-collections/community.general/pull/7698).
- keycloak_realm_key - the ``config.certificate`` option value is no longer defined with ``no_log=True`` (https://github.com/ansible-collections/community.general/pull/7698).
- keycloak_realm_key - the ``provider_id`` option now supports RSA encryption key usage (value ``rsa-enc``) (https://github.com/ansible-collections/community.general/pull/7698).
- keycloak_user_federation - add option for ``krbPrincipalAttribute`` (https://github.com/ansible-collections/community.general/pull/7538).
- keycloak_user_federation - allow custom user storage providers to be set through ``provider_id`` (https://github.com/ansible-collections/community.general/pull/7789).
- ldap_attrs - module now supports diff mode, showing which attributes are changed within an operation (https://github.com/ansible-collections/community.general/pull/8073).
- lvg - refactor module to pass list of arguments to ``module.run_command()`` instead of relying on interpretation by a shell (https://github.com/ansible-collections/community.general/pull/8264).
- lvol - change ``pvs`` argument type to list of strings (https://github.com/ansible-collections/community.general/pull/7676, https://github.com/ansible-collections/community.general/issues/7504).
- lvol - refactor module to pass list of arguments to ``module.run_command()`` instead of relying on interpretation by a shell (https://github.com/ansible-collections/community.general/pull/8264).
- lxd connection plugin - tighten the detection logic for lxd ``Instance not found`` errors, to avoid false detection on unrelated errors such as ``/usr/bin/python3: not found`` (https://github.com/ansible-collections/community.general/pull/7521).
- lxd_container - uses ``/1.0/instances`` API endpoint, if available. Falls back to ``/1.0/containers`` or ``/1.0/virtual-machines``. Fixes issue when using Incus or LXD 5.19 due to migrating to ``/1.0/instances`` endpoint (https://github.com/ansible-collections/community.general/pull/7980).
- macports - refactor module to pass list of arguments to ``module.run_command()`` instead of relying on interpretation by a shell (https://github.com/ansible-collections/community.general/pull/8264).
- mail - add ``Message-ID`` header; which is required by some mail servers (https://github.com/ansible-collections/community.general/pull/7740).
- mail module, mail callback plugin - allow to configure the domain name of the Message-ID header with a new ``message_id_domain`` option (https://github.com/ansible-collections/community.general/pull/7765).
- mssql_script - adds transactional (rollback/commit) support via optional boolean param ``transaction`` (https://github.com/ansible-collections/community.general/pull/7976).
- netcup_dns - adds support for record types ``OPENPGPKEY``, ``SMIMEA``, and ``SSHFP`` (https://github.com/ansible-collections/community.general/pull/7489).
- nmcli - add support for new connection type ``loopback`` (https://github.com/ansible-collections/community.general/issues/6572).
- nmcli - adds OpenvSwitch support with new ``type`` values ``ovs-port``, ``ovs-interface``, and ``ovs-bridge``, and new ``slave_type`` value ``ovs-port`` (https://github.com/ansible-collections/community.general/pull/8154).
- nmcli - allow for ``infiniband`` slaves of ``bond`` interface types (https://github.com/ansible-collections/community.general/pull/7569).
- nmcli - allow for the setting of ``MTU`` for ``infiniband`` and ``bond`` interface types (https://github.com/ansible-collections/community.general/pull/7499).
- nmcli - allow setting ``MTU`` for ``bond-slave`` interface types (https://github.com/ansible-collections/community.general/pull/8118).
- onepassword lookup plugin - support 1Password Connect with the opv2 client by setting the connect_host and connect_token parameters (https://github.com/ansible-collections/community.general/pull/7116).
- onepassword_raw lookup plugin - support 1Password Connect with the opv2 client by setting the connect_host and connect_token parameters (https://github.com/ansible-collections/community.general/pull/7116)
- opentelemetry - add support for HTTP trace_exporter and configures the behavior via ``OTEL_EXPORTER_OTLP_TRACES_PROTOCOL`` (https://github.com/ansible-collections/community.general/issues/7888, https://github.com/ansible-collections/community.general/pull/8321).
- opentelemetry - add support for exporting spans in a file via ``ANSIBLE_OPENTELEMETRY_STORE_SPANS_IN_FILE`` (https://github.com/ansible-collections/community.general/issues/7888, https://github.com/ansible-collections/community.general/pull/8363).
- opkg - use ``ModuleHelper`` with ``VarDict`` (https://github.com/ansible-collections/community.general/pull/8226).
- osx_defaults - add option ``check_types`` to enable changing the type of existing defaults on the fly (https://github.com/ansible-collections/community.general/pull/8173).
- parted - refactor module to pass list of arguments to ``module.run_command()`` instead of relying on interpretation by a shell (https://github.com/ansible-collections/community.general/pull/8264).
- passwordstore - adds ``timestamp`` and ``preserve`` parameters to modify the stored password format (https://github.com/ansible-collections/community.general/pull/7426).
- passwordstore lookup - add ``missing_subkey`` parameter defining the behavior of the lookup when a passwordstore subkey is missing (https://github.com/ansible-collections/community.general/pull/8166).
- pipx - use ``ModuleHelper`` with ``VarDict`` (https://github.com/ansible-collections/community.general/pull/8226).
- pkg5 - add support for non-silent execution (https://github.com/ansible-collections/community.general/issues/8379, https://github.com/ansible-collections/community.general/pull/8382).
- pkgin - refactor module to pass list of arguments to ``module.run_command()`` instead of relying on interpretation by a shell (https://github.com/ansible-collections/community.general/pull/8264).
- portage - adds the possibility to explicitely tell portage to write packages to world file (https://github.com/ansible-collections/community.general/issues/6226, https://github.com/ansible-collections/community.general/pull/8236).
- portinstall - refactor module to pass list of arguments to ``module.run_command()`` instead of relying on interpretation by a shell (https://github.com/ansible-collections/community.general/pull/8264).
- proxmox - adds ``startup`` parameters to configure startup order, startup delay and shutdown delay (https://github.com/ansible-collections/community.general/pull/8038).
- proxmox - adds ``template`` value to the ``state`` parameter, allowing conversion of container to a template (https://github.com/ansible-collections/community.general/pull/7143).
- proxmox - adds ``update`` parameter, allowing update of an already existing containers configuration (https://github.com/ansible-collections/community.general/pull/7540).
- proxmox inventory plugin - adds an option to exclude nodes from the dynamic inventory generation. The new setting is optional, not using this option will behave as usual (https://github.com/ansible-collections/community.general/issues/6714, https://github.com/ansible-collections/community.general/pull/7461).
- proxmox* modules - there is now a ``community.general.proxmox`` module defaults group that can be used to set default options for all Proxmox modules (https://github.com/ansible-collections/community.general/pull/8334).
- proxmox_disk - add ability to manipulate CD-ROM drive (https://github.com/ansible-collections/community.general/pull/7495).
- proxmox_kvm - add parameter ``update_unsafe`` to avoid limitations when updating dangerous values (https://github.com/ansible-collections/community.general/pull/7843).
- proxmox_kvm - adds ``template`` value to the ``state`` parameter, allowing conversion of a VM to a template (https://github.com/ansible-collections/community.general/pull/7143).
- proxmox_kvm - adds``usb`` parameter for setting USB devices on proxmox KVM VMs (https://github.com/ansible-collections/community.general/pull/8199).
- proxmox_kvm - support the ``hookscript`` parameter (https://github.com/ansible-collections/community.general/issues/7600).
- proxmox_ostype - it is now possible to specify the ``ostype`` when creating an LXC container (https://github.com/ansible-collections/community.general/pull/7462).
- proxmox_vm_info - add ability to retrieve configuration info (https://github.com/ansible-collections/community.general/pull/7485).
- puppet - new feature to set ``--waitforlock`` option (https://github.com/ansible-collections/community.general/pull/8282).
- redfish_command - add command ``ResetToDefaults`` to reset manager to default state (https://github.com/ansible-collections/community.general/issues/8163).
- redfish_config - add command ``SetServiceIdentification`` to set service identification (https://github.com/ansible-collections/community.general/issues/7916).
- redfish_info - add boolean return value ``MultipartHttpPush`` to ``GetFirmwareUpdateCapabilities`` (https://github.com/ansible-collections/community.general/issues/8194, https://github.com/ansible-collections/community.general/pull/8195).
- redfish_info - add command ``GetServiceIdentification`` to get service identification (https://github.com/ansible-collections/community.general/issues/7882).
- redfish_info - adding the ``BootProgress`` property when getting ``Systems`` info (https://github.com/ansible-collections/community.general/pull/7626).
- revbitspss lookup plugin - removed a redundant unicode prefix. The prefix was not necessary for Python 3 and has been cleaned up to streamline the code (https://github.com/ansible-collections/community.general/pull/8087).
- rundeck module utils - allow to pass ``Content-Type`` to API requests (https://github.com/ansible-collections/community.general/pull/7684).
- slackpkg - refactor module to pass list of arguments to ``module.run_command()`` instead of relying on interpretation by a shell (https://github.com/ansible-collections/community.general/pull/8264).
- ssh_config - adds ``controlmaster``, ``controlpath`` and ``controlpersist`` parameters (https://github.com/ansible-collections/community.general/pull/7456).
- ssh_config - allow ``accept-new`` as valid value for ``strict_host_key_checking`` (https://github.com/ansible-collections/community.general/pull/8257).
- ssh_config - new feature to set ``AddKeysToAgent`` option to ``yes`` or ``no`` (https://github.com/ansible-collections/community.general/pull/7703).
- ssh_config - new feature to set ``IdentitiesOnly`` option to ``yes`` or ``no`` (https://github.com/ansible-collections/community.general/pull/7704).
- sudoers - add support for the ``NOEXEC`` tag in sudoers rules (https://github.com/ansible-collections/community.general/pull/7983).
- svr4pkg - refactor module to pass list of arguments to ``module.run_command()`` instead of relying on interpretation by a shell (https://github.com/ansible-collections/community.general/pull/8264).
- swdepot - refactor module to pass list of arguments to ``module.run_command()`` instead of relying on interpretation by a shell (https://github.com/ansible-collections/community.general/pull/8264).
- terraform - add support for ``diff_mode`` for terraform resource_changes (https://github.com/ansible-collections/community.general/pull/7896).
- terraform - fix ``diff_mode`` in state ``absent`` and when terraform ``resource_changes`` does not exist (https://github.com/ansible-collections/community.general/pull/7963).
- xcc_redfish_command - added support for raw POSTs (``command=PostResource`` in ``category=Raw``) without a specific action info (https://github.com/ansible-collections/community.general/pull/7746).
- xfconf - use ``ModuleHelper`` with ``VarDict`` (https://github.com/ansible-collections/community.general/pull/8226).
- xfconf_info - use ``ModuleHelper`` with ``VarDict`` (https://github.com/ansible-collections/community.general/pull/8226).

community.grafana
~~~~~~~~~~~~~~~~~

- Add Quickwit search engine datasource (https://quickwit.io).
- Add new module `grafana_silence` to create and delete silences through the API
- Add parameter `org_name` to `grafana_dashboard`
- Add parameter `org_name` to `grafana_datasource`
- Add parameter `org_name` to `grafana_organization_user`
- Add role components for `grafana_silence` module
- Add support for Grafana Tempo datasource type (https://grafana.com/docs/grafana/latest/datasources/tempo/)
- Manage `grafana_folder` for organizations
- Merged ansible role telekom-mms/ansible-role-grafana into ansible-collections/community.grafana
- added `community.grafana.notification_channel` to role
- default to true/false in docs and code
- grafana_dashboard - add check_mode support
- lookup - grafana_dashboards - add `validate_certs` and `ca_path` options to plugin for custom certs validation

community.hashi_vault
~~~~~~~~~~~~~~~~~~~~~

- cert auth - add option to set the ``cert_auth_public_key`` and ``cert_auth_private_key`` parameters using the variables ``ansible_hashi_vault_cert_auth_public_key`` and ``ansible_hashi_vault_cert_auth_private_key`` (https://github.com/ansible-collections/community.hashi_vault/issues/428).

community.hrobot
~~~~~~~~~~~~~~~~

- robot inventory plugin - add ``filter`` option which allows to include and exclude hosts based on Jinja2 conditions (https://github.com/ansible-collections/community.hrobot/pull/101).
- robot inventory plugin - the ``filters`` option has been renamed to ``simple_filters``. The old name still works until community.hrobot 2.0.0. Then it will change to allow more complex filtering with the ``community.library_inventory_filtering_v1`` collection's functionality (https://github.com/ansible-collections/community.hrobot/pull/94).

community.mysql
~~~~~~~~~~~~~~~

- mysql_user - add the ``password_expire`` and ``password_expire_interval`` arguments to implement the password expiration management for mysql user (https://github.com/ansible-collections/community.mysql/pull/598).
- mysql_user - add user attribute support via the ``attributes`` parameter and return value (https://github.com/ansible-collections/community.mysql/pull/604).

community.postgresql
~~~~~~~~~~~~~~~~~~~~

- postgresql_db - add the ``comment`` argument (https://github.com/ansible-collections/community.postgresql/issues/614).
- postgresql_db - add the ``icu_locale`` argument (https://github.com/ansible-collections/community.postgresql/issues/666).
- postgresql_db - add the ``locale_provider`` argument (https://github.com/ansible-collections/community.postgresql/issues/666).
- postgresql_ext - add the ``comment`` argument (https://github.com/ansible-collections/community.postgresql/issues/354).
- postgresql_publication - add the ``comment`` argument (https://github.com/ansible-collections/community.postgresql/issues/354).
- postgresql_schema - add the ``comment`` argument (https://github.com/ansible-collections/community.postgresql/issues/354).
- postgresql_subscription - add the ``comment`` argument (https://github.com/ansible-collections/community.postgresql/issues/354).
- postgresql_tablespace - add the ``comment`` argument (https://github.com/ansible-collections/community.postgresql/issues/354).

community.rabbitmq
~~~~~~~~~~~~~~~~~~

- rabbitmq_user - add support to user manipulation through RabbitMQ API (https://github.com/ansible-collections/community.rabbitmq/issues/76)

community.routeros
~~~~~~~~~~~~~~~~~~

- api_info, api_modify - Add RouterOS 7.x support to ``/mpls ldp`` path (https://github.com/ansible-collections/community.routeros/pull/271).
- api_info, api_modify - add ``/ip route rule`` path for RouterOS 6.x (https://github.com/ansible-collections/community.routeros/pull/278).
- api_info, api_modify - add ``/routing filter`` path for RouterOS 6.x (https://github.com/ansible-collections/community.routeros/pull/279).
- api_info, api_modify - add ``interface ovpn-client`` path (https://github.com/ansible-collections/community.routeros/issues/242, https://github.com/ansible-collections/community.routeros/pull/244).
- api_info, api_modify - add ``radius`` path (https://github.com/ansible-collections/community.routeros/issues/241, https://github.com/ansible-collections/community.routeros/pull/245).
- api_info, api_modify - add ``routing rule`` path (https://github.com/ansible-collections/community.routeros/issues/162, https://github.com/ansible-collections/community.routeros/pull/246).
- api_info, api_modify - add default value for ``from-pool`` field in ``/ipv6 address`` (https://github.com/ansible-collections/community.routeros/pull/270).
- api_info, api_modify - add missing DoH parameters ``doh-max-concurrent-queries``, ``doh-max-server-connections``, and ``doh-timeout`` to the ``ip dns`` path (https://github.com/ansible-collections/community.routeros/issues/230, https://github.com/ansible-collections/community.routeros/pull/235)
- api_info, api_modify - add missing parameters ``address-list``, ``address-list-timeout``, ``randomise-ports``, and ``realm`` to subpaths of the ``ip firewall`` path (https://github.com/ansible-collections/community.routeros/issues/236, https://github.com/ansible-collections/community.routeros/pull/237).
- api_info, api_modify - add missing path ``/interface pppoe-server server`` (https://github.com/ansible-collections/community.routeros/pull/273).
- api_info, api_modify - add missing path ``/ip dhcp-relay`` (https://github.com/ansible-collections/community.routeros/pull/276).
- api_info, api_modify - add missing path ``/queue simple`` (https://github.com/ansible-collections/community.routeros/pull/269).
- api_info, api_modify - add missing path ``/queue type`` (https://github.com/ansible-collections/community.routeros/pull/274).
- api_info, api_modify - add missing path ``routing bgp template`` (https://github.com/ansible-collections/community.routeros/pull/243).
- api_info, api_modify - add missing paths ``/routing bgp aggregate``, ``/routing bgp network`` and ``/routing bgp peer`` (https://github.com/ansible-collections/community.routeros/pull/277).
- api_info, api_modify - add read-only fields ``installed-version``, ``latest-version`` and ``status`` in ``system package update`` (https://github.com/ansible-collections/community.routeros/pull/263).
- api_info, api_modify - add support for paths ``/mpls interface``, ``/mpls ldp accept-filter``, ``/mpls ldp advertise-filter`` and ``mpls ldp interface`` (https://github.com/ansible-collections/community.routeros/pull/272).
- api_info, api_modify - add support for the ``tx-power`` attribute in ``interface wireless`` (https://github.com/ansible-collections/community.routeros/pull/239).
- api_info, api_modify - added support for ``interface wifi`` and its sub-paths (https://github.com/ansible-collections/community.routeros/pull/266).
- api_info, api_modify - make path ``user group`` modifiable and add ``comment`` attribute (https://github.com/ansible-collections/community.routeros/issues/256, https://github.com/ansible-collections/community.routeros/pull/257).
- api_info, api_modify - mark the ``interface wireless`` parameter ``running`` as read-only (https://github.com/ansible-collections/community.routeros/pull/233).
- api_info, api_modify - remove default value for read-only ``running`` field in ``interface wireless`` (https://github.com/ansible-collections/community.routeros/pull/264).
- api_info, api_modify - removed ``host`` primary key in ``tool netwatch`` path (https://github.com/ansible-collections/community.routeros/pull/248).
- api_info, api_modify - set the default value to ``false`` for the  ``disabled`` parameter in some more paths where it can be seen in the documentation (https://github.com/ansible-collections/community.routeros/pull/237).
- api_modify - add missing ``comment`` attribute to ``/routing id`` (https://github.com/ansible-collections/community.routeros/pull/234).
- api_modify - add missing attributes to the ``routing bgp connection`` path (https://github.com/ansible-collections/community.routeros/pull/234).
- api_modify - add versioning to the ``/tool e-mail`` path (RouterOS 7.12 release) (https://github.com/ansible-collections/community.routeros/pull/234).
- api_modify - make ``/ip traffic-flow target`` a multiple value attribute (https://github.com/ansible-collections/community.routeros/pull/234).
- api_modify, api_info - add support for the ``ip vrf`` path in RouterOS 7  (https://github.com/ansible-collections/community.routeros/pull/259)
- api_modify, api_info - added support for ``interface wifiwave2`` (https://github.com/ansible-collections/community.routeros/pull/226).

community.vmware
~~~~~~~~~~~~~~~~

- Add standard function vmware_argument_spec() from module_utils for using default env fallback function. https://github.com/ansible-collections/community.vmware/issues/1977
- Document that all parameters and VMware object names are case sensitive (https://github.com/ansible-collections/community.vmware/issues/2019).
- Drop the outdated (and actually unmaintained) scenario guides (https://github.com/ansible-collections/community.vmware/pull/2022).
- vmware_dvs_portgroup - Make `state` default to `present` instead of having it as a required parameter (https://github.com/ansible-collections/community.vmware/pull/2055).
- vmware_dvswitch - Add switchIpAddress/switch_ip parameter for netflow config
- vmware_first_class_disk_info - Add a module to gather informations about first class disks. (https://github.com/ansible-collections/community.vmware/pull/1996). (https://github.com/ansible-collections/community.vmware/issues/1988).
- vmware_guest - Add IPv6 support for VM network interfaces (https://github.com/ansible-collections/community.vmware/pull/1937).
- vmware_guest_sendkey - Add Windows key (https://github.com/ansible-collections/community.vmware/issues/1959).
- vmware_guest_tools_info - Use `toolsVersionStatus2` instead of `toolsVersionStatus` (https://github.com/ansible-collections/community.vmware/issues/2033).
- vmware_guest_tools_upgrade - Add parameter `installer_options` to pass command line options to the installer to modify the installation procedure for tools (https://github.com/ansible-collections/community.vmware/pull/1059).
- vmware_host_facts - Add the possibility to get the related datacenter. (https://github.com/ansible-collections/community.vmware/pull/1994).
- vmware_vm_inventory - Add parameter `subproperties` (https://github.com/ansible-collections/community.vmware/pull/1972).
- vmware_vmkernel - Add the function to set the enable_backup_nfc setting (https://github.com/ansible-collections/community.vmware/pull/1978)
- vsphere_copy - Add parameter to tell vsphere_copy which diskformat is being uploaded (https://github.com/ansible-collections/community.vmware/pull/1995).

community.windows
~~~~~~~~~~~~~~~~~

- Set minimum supported Ansible version to 2.14 to align with the versions still supported by Ansible.
- win_regmerge - Add content 'content' parameter for specifying registry file contents directly

community.zabbix
~~~~~~~~~~~~~~~~

- Add slash at the end of the location directives, to prevent path traversal attacks.
- Added active_since and active_till in zabbix_maintenance
- Added content_type for email in zabbix_mediatypes
- Added zabbix_group_events_info module
- Introduce flag `enable_version_check` to allow installations on non-supported platforms.
- action module - Added notify_if_canceled property
- agent and proxy roles - Set default `zabbix_api_server_port` to 80 or 443 based on `zabbix_api_use_ssl`
- agent role - Removed duplicative Windows agent task
- agent role - Standardized default yum priority to 99
- agent, javagateway, proxy, server, and web role - added the http_proxy and https_proxy environment variables to "Debian | Download gpg key" analog to other tasks
- agent, javagateway, proxy, server, and web role - introduced default variable zabbix_repo_deb_gpg_key_url with value http://repo.zabbix.com/zabbix-official-repo.key
- agent, javagateway, proxy, server, and web role - introduced default variable zabbix_repo_deb_include_deb_src with value true
- agent, javagateway, proxy, server, and web role - removed superfluous slash in zabbix_gpg_key of the Debian vars and renamed key to zabbix-repo instead of zabbix-official-repo
- agent, javagateway, proxy, server, and web role - used variable zabbix_repo_deb_include_deb_src in "Debian | Installing repository" to determine whether deb-src should be added to /etc/apt/sources.list.d/zabbix.sources
- agent, javagateway, proxy, server, and web role - used zabbix_repo_deb_gpg_key_url in "Debian | Download gpg key" instead of hardcoded url
- all roles - Re-added ability to override Debian repo source
- all roles - Updated Debian repository format to 822 standard
- api_requests - Handled error from depricated CertificateError class
- multiple roles - Removed unneeded Apt Clean commands.
- proxy role - Updated MariaDB version for Centos 7 to 10.11
- various - updated testing modules
- various - updated to fully qualified module names
- zabbix agent - Added capability to add additional configuration includes
- zabbix web - Allowed the independent configuration of php-fpm without creating vhost.
- zabbix_api_info module added
- zabbix_correlation module added
- zabbix_host_info - added ability to get all the hosts configured in Zabbix
- zabbix_proxy role - Add variable zabbix_proxy_dbpassword_hash_method to control whether you want postgresql user password to be hashed with md5 or want to use db default. When zabbix_proxy_dbpassword_hash_method is set to anything other than md5 then do not hash the password with md5 so you could use postgresql scram-sha-256 hashing method.
- zabbix_server role - Add variable zabbix_server_dbpassword_hash_method to control whether you want postgresql user password to be hashed with md5 or want to use db default. When zabbix_server_dbpassword_hash_method is set to anything other than md5 then do not hash the password with md5 so you could use postgresql scram-sha-256 hashing method.
- zabbix_service_info module added
- zabbix_template - Add template_yaml parameter.
- zabbix_templategroup module added
- zabbix_user module - add current_passwd optional parameter to enable password updating of the currently logged in user (https://www.zabbix.com/documentation/6.4/en/manual/api/reference/user/update)
- zabbix_web role, Refactored zabbix_selinux variable names to correlate with selinux boolean names.

containers.podman
~~~~~~~~~~~~~~~~~

- Add log_opt and annotaion options to podman_play module
- Add option to parse CreateCommand easily for diff calc
- Add support for setting underlying interface in podman_network
- Alias generate systemd options stop_timeout and time
- CI - Fix rootfs test in CI
- CI - add custom podman path to tasks
- CI - add parametrized executables to tests
- Fix CI rootfs for podman_container
- Fix broken conmon version in CI install
- Improve security_opt comparison between existing container
- podman_container - Add new arguments to podman status commands
- podman_container - Add pasta as default network mode after v5
- podman_container - Update env_file to accept a list of files instead of a single file
- podman_container_exec - Return data for podman exec module
- podman_generate_systemd - Fix broken example for podman_generate_systemd (#708)
- podman_login - Update podman_login.py
- podman_play - Add support for kube yaml files with multi-documents (#724)
- podman_play - Update the logic for deleting pods/containers in podman_play
- podman_pod_info - handle return being list in Podman 5 (#713)
- podman_secret_info - Add secrets info module

dellemc.enterprise_sonic
~~~~~~~~~~~~~~~~~~~~~~~~

- sonic_aaa - Add support for playbook check and diff modes (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/304).
- sonic_aaa - Enhance config diff generation function (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/318).
- sonic_acl_interfaces - Add support for playbook check and diff modes (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/306).
- sonic_acl_interfaces - Enhance config diff generation function (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/318).
- sonic_bgp_as_paths - Add support for replaced and overridden states (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/290).
- sonic_bgp_communities - Add support for replaced and overridden states (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/251).
- sonic_bgp_ext_communities - Add support for replaced and overridden states (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/252).
- sonic_interfaces - Add support for playbook check and diff modes (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/301).
- sonic_interfaces - Add support for replaced and overridden states (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/314).
- sonic_interfaces - Change deleted design for interfaces module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/310).
- sonic_interfaces - Enhance config diff generation function (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/318).
- sonic_ip_neighbor - Add support for playbook check and diff modes (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/285).
- sonic_ip_neighbor - Enhance config diff generation function (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/318).
- sonic_l2_acls - Add support for playbook check and diff modes (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/306).
- sonic_l2_acls - Enhance config diff generation function (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/318).
- sonic_l2_interfaces - Add support for playbook check and diff modes (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/303).
- sonic_l2_interfaces - Enhance config diff generation function (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/318).
- sonic_l3_acls - Add support for playbook check and diff modes (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/306).
- sonic_l3_acls - Enhance config diff generation function (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/318).
- sonic_l3_interfaces - Add support for replaced and overridden states (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/241).
- sonic_lag_interfaces - Add support for playbook check and diff modes (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/303).
- sonic_lag_interfaces - Enhance config diff generation function (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/318).
- sonic_logging - Add support for playbook check and diff modes (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/285).
- sonic_logging - Enhance config diff generation function (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/318).
- sonic_mclag - Add VLAN range support for 'unique_ip' and 'peer_gateway' options (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/288).
- sonic_mclag - Add support for replaced and overridden states (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/288).
- sonic_ntp - Add support for playbook check and diff modes (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/281).
- sonic_ntp - Enhance config diff generation function (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/318).
- sonic_port_breakout - Add Ansible support for all port breakout modes now allowed in Enterprise SONiC (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/276).
- sonic_port_breakout - Add support for replaced and overridden states (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/291).
- sonic_port_group - Add support for playbook check and diff modes (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/284).
- sonic_port_group - Enhance config diff generation function (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/318).
- sonic_radius_server - Add support for playbook check and diff modes (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/279).
- sonic_radius_server - Enhance config diff generation function (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/318).
- sonic_static_routes - Add playbook check and diff modes support for static routes resource module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/313).
- sonic_static_routes - Enhance config diff generation function (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/318).
- sonic_system - Add support for playbook check and diff modes (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/284).
- sonic_system - Enhance config diff generation function (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/318).
- sonic_tacacs_server - Add support for playbook check and diff modes (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/281).
- sonic_tacacs_server - Enhance config diff generation function (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/318).
- sonic_users - Add support for playbook check and diff modes (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/304).
- sonic_users - Enhance config diff generation function (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/318).
- sonic_vlans - Add support for playbook check and diff modes (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/301).
- sonic_vlans - Enhance config diff generation function (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/318).
- sonic_vrfs - Add mgmt VRF replaced state handling to sonic_vrfs module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/298).
- sonic_vrfs - Add mgmt VRF support to sonic_vrfs module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/293).
- sonic_vrfs - Add support for playbook check and diff modes (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/285).
- sonic_vrfs - Enhance config diff generation function (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/318).
- tests - Add UTs for BFD, COPP, and MAC modules (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/287).
- tests - Enable contiguous execution of all regression integration tests on an S5296f (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/277).
- tests - Fix the bgp CLI test base_cfg_path derivation of the bgp role_path by avoiding relative pathing from the possibly external playbook_dir (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/283).

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- Ansible lint issues are fixed for the collections.
- For idrac_certificate role, added support for import operation of `HTTPS` certificate with the SSL key.
- For idrac_certificates module, below enhancements are made: Added support for import operation of `HTTPS` certificate with the SSL key. The `email_address` has been made as an optional parameter.
- For idrac_gather_facts role, added storage controller details in the role output.
- Module ``redfish_storage_volume`` is enhanced to support reboot options and job tracking operation.
- idrac_reset - This module allows you to reset the iDRAC to factory default settings.
- redfish_storage_volume - This module is enhanced to support iDRAC8.

dellemc.powerflex
~~~~~~~~~~~~~~~~~

- Added support for PowerFlex Denver version(4.5.x) to TB and Config role.
- Added support for PowerFlex ansible modules and roles on Azure.
- Added support for executing Ansible PowerFlex modules and roles on AWS environment.
- Added support for resource group provisioning to validate, deploy, edit, add nodes and delete a resource group.
- The Info module is enhanced to list the firmware repositories.
- The Info module is enhanced to retrieve lists related to fault sets, service templates, deployments, and managed devices.
- The SDS module has been enhanced to facilitate SDS creation within a fault set.

f5networks.f5_modules
~~~~~~~~~~~~~~~~~~~~~

- bigiq_device_discovery - Changes in documentation related to Provider block

fortinet.fortimanager
~~~~~~~~~~~~~~~~~~~~~

- Added deprecated warning to invalid argument name, please change the invalid argument name such as "var-name", "var name" to "var_name".
- Renamed the input argument "message" to "fmgr_message" to comply with Ansible requirements.
- Supported fortimanager 7.4.2, 21 new modules.

google.cloud
~~~~~~~~~~~~

- anisble-test - integration tests are now run against 2.14.0 and 2.15.0
- ansible - 2.14.0 is now the minimum version supported
- ansible-lint - fixed over a thousand reported errors
- ansible-lint - upgraded to 6.22
- ansible-test - add support for GCP application default credentials (https://github.com/ansible-collections/google.cloud/issues/359).
- gcp_serviceusage_service - added backoff when checking for operation completion.
- gcp_serviceusage_service - use alloyb API for the integration test as spanner conflicts with other tests
- gcp_sql_ssl_cert - made sha1_fingerprint optional, which enables resource creation
- gcp_storage_default_object_acl - removed non-existent fields; the resource is not usable.

grafana.grafana
~~~~~~~~~~~~~~~

- Add 'run_once' to download&unzip tasks by @v-zhuravlev in https://github.com/grafana/grafana-ansible-collection/pull/136
- Adding `oauth_allow_insecure_email_lookup` to fix oauth user sync error by @hypery2k in https://github.com/grafana/grafana-ansible-collection/pull/132
- Bump ansible-core from 2.15.4 to 2.15.8 by @dependabot in https://github.com/grafana/grafana-ansible-collection/pull/137
- Bump ansible-lint from 24.2.0 to 24.2.1 by @dependabot in https://github.com/grafana/grafana-ansible-collection/pull/164
- Bump ansible-lint from 24.2.0 to 24.2.1 by @dependabot in https://github.com/grafana/grafana-ansible-collection/pull/168
- Bump ansible-lint from 6.13.1 to 6.14.3 by @dependabot in https://github.com/grafana/grafana-ansible-collection/pull/139
- Bump ansible-lint from 6.14.3 to 6.22.2 by @dependabot in https://github.com/grafana/grafana-ansible-collection/pull/142
- Bump ansible-lint from 6.22.2 to 24.2.0 by @dependabot in https://github.com/grafana/grafana-ansible-collection/pull/150
- Bump black from 24.1.1 to 24.3.0 by @dependabot in https://github.com/grafana/grafana-ansible-collection/pull/165
- Bump cryptography from 41.0.4 to 41.0.6 by @dependabot in https://github.com/grafana/grafana-ansible-collection/pull/126
- Bump jinja2 from 3.1.2 to 3.1.3 by @dependabot in https://github.com/grafana/grafana-ansible-collection/pull/129
- Bump pylint from 2.16.2 to 3.0.3 by @dependabot in https://github.com/grafana/grafana-ansible-collection/pull/141
- Bump pylint from 3.0.3 to 3.1.0 by @dependabot in https://github.com/grafana/grafana-ansible-collection/pull/158
- Bump pylint from 3.0.3 to 3.1.0 by @dependabot in https://github.com/grafana/grafana-ansible-collection/pull/161
- Bump the pip group across 1 directories with 1 update by @dependabot in https://github.com/grafana/grafana-ansible-collection/pull/156
- Bump yamllint from 1.29.0 to 1.33.0 by @dependabot in https://github.com/grafana/grafana-ansible-collection/pull/140
- Bump yamllint from 1.29.0 to 1.33.0 by @dependabot in https://github.com/grafana/grafana-ansible-collection/pull/143
- Bump yamllint from 1.33.0 to 1.34.0 by @dependabot in https://github.com/grafana/grafana-ansible-collection/pull/151
- Bump yamllint from 1.33.0 to 1.35.1 by @dependabot in https://github.com/grafana/grafana-ansible-collection/pull/155
- Bump yamllint from 1.33.0 to 1.35.1 by @dependabot in https://github.com/grafana/grafana-ansible-collection/pull/159
- Change handler to systemd by @v-zhuravlev in https://github.com/grafana/grafana-ansible-collection/pull/135
- Clarify grafana-server configuration in README by @VGerris in https://github.com/grafana/grafana-ansible-collection/pull/177
- Drop curl check by @v-zhuravlev in https://github.com/grafana/grafana-ansible-collection/pull/120
- ExecStartPre and EnvironmentFile settings to system unit file by @fabiiw05 in https://github.com/grafana/grafana-ansible-collection/pull/157
- Fix check mode for grafana role by @Boschung-Mecatronic-AG-Infrastructure in https://github.com/grafana/grafana-ansible-collection/pull/125
- Fix check mode in Grafana Agent by @AmandaCameron in https://github.com/grafana/grafana-ansible-collection/pull/124
- Fix links in grafana_agent/defaults/main.yaml by @PabloCastellano in https://github.com/grafana/grafana-ansible-collection/pull/134
- Topic/grafana agent idempotency by @ohdearaugustin in https://github.com/grafana/grafana-ansible-collection/pull/147
- Update description to match module by @brmurphy in https://github.com/grafana/grafana-ansible-collection/pull/179
- Update tags in README by @ishanjainn in https://github.com/grafana/grafana-ansible-collection/pull/121
- datasources url parameter fix by @dergudzon in https://github.com/grafana/grafana-ansible-collection/pull/162

hetzner.hcloud
~~~~~~~~~~~~~~

- Add the `hetzner.hcloud.all` group to configure all the modules using `module_defaults`.
- Allow to set the `api_endpoint` module argument using the `HCLOUD_ENDPOINT` environment variable.
- Removed the `hcloud_` prefix from all modules names, e.g. `hetzner.hcloud.hcloud_firewall` was renamed to `hetzner.hcloud.firewall`. Old module names will continue working.
- Renamed the `endpoint` module argument to `api_endpoint`, backward compatibility is maintained using an alias.
- Replace deprecated `ansible.netcommon` ip utils with python `ipaddress` module. The `ansible.netcommon` collection is no longer required by the collections.
- firewall - Allow forcing the deletion of firewalls that are still in use.
- firewall - Do not silence 'firewall still in use' delete failures.
- firewall - Return resources the firewall is `applied_to`.
- firewall_info - Add new `firewall_info` module to gather firewalls info.
- firewall_resource - Add new `firewall_resource` module to manage firewalls resources.
- hcloud inventory - Add the `api_endpoint` option.
- hcloud inventory - Deprecate the `api_token_env` option, suggest using a lookup plugin (`{{ lookup('ansible.builtin.env', 'YOUR_ENV_VAR') }}`) or use the well-known `HCLOUD_TOKEN` environment variable name.
- hcloud inventory - Rename the `token_env` option to `api_token_env`, use aliases for backward compatibility.
- hcloud inventory - Rename the `token` option to `api_token`, use aliases for backward compatibility.
- inventory - Add `hostname` option used to template the hostname of the instances.
- inventory - Add `hostvars_prefix` and hostvars_suffix` options to customize the inventory host variables keys.
- network - Allow renaming networks.
- primary_ip - Use the `server` option to assign a Primary IP being created to a server.
- server - Allow passing Datacenter name or ID to the `datacenter` argument.
- server - Allow passing Image name or ID to the `image` argument.
- server - Allow passing Location name or ID to the `location` argument.
- server - Allow passing SSH Keys names or IDs to the `ssh_keys` argument.
- server - Allow passing Volume names or IDs to the `volumes` argument.
- server - Renamed the `allow_deprecated_image` option to `image_allow_deprecated`.

ibm.storage_virtualize
~~~~~~~~~~~~~~~~~~~~~~

- ibm_sv_manage_replication_policy - Added support to configure a 2-site-ha policy.
- ibm_sv_manage_snapshot - Added support to restore entire volumegroup from a snapshot of that volumegroup.
- ibm_sv_manage_snapshot - Added support to restore subset of volumes of a volumegroup from a snapshot
- ibm_svc_host - Added support to create nvmetcp host.
- ibm_svc_info - Added support to display information about partition, quorum, IO group, VG replication and enclosure, snmp server and ldap server
- ibm_svc_info - Added support to display information about thinclone/clone volumes and volumegroups.
- ibm_svc_manage_volume - Added support to create clone or thinclone from snapshot
- ibm_svc_manage_volumgroup - Added support to create clone or thinkclone volumegroup from snapshot from a subset of volumes
- ibm_svc_manage_volumgroup - Added support to delete volumegroups keeping volumes via 'evictvolumes'.

infoblox.nios_modules
~~~~~~~~~~~~~~~~~~~~~

- Ansible core version in the dependencies updated to 2.14 or later.

inspur.ispim
~~~~~~~~~~~~

- Modify ansible-test.yml to add the ansible 2.17 test https://github.com/ispim/inspur.ispim/pull/33.
- Modify ansible-test.yml to add the ansible2.16 test.
- Modify edit_smtp_com and add description information.

junipernetworks.junos
~~~~~~~~~~~~~~~~~~~~~

- Add support for cli_restore functionality.
- Please refer the PR to know more about core changes (https://github.com/ansible-collections/ansible.netcommon/pull/618).
- cli_restore module is part of netcommon.

kubernetes.core
~~~~~~~~~~~~~~~

- helm - add ``reuse_values`` and ``reset_values`` support to helm module (https://github.com/ansible-collections/kubernetes.core/issues/394).
- k8s - add new option ``delete_all`` to support deletion of all resources when state is set to ``absent``. (https://github.com/ansible-collections/kubernetes.core/issues/504)
- k8s, k8s_info - add a hidden_fields option to allow fields to be hidden in the results of k8s and k8s_info
- k8s_drain - add ability to filter the list of pods to be drained by a pod label selector (https://github.com/ansible-collections/kubernetes.core/issues/474).
- kubectl - added support of local enviroment variable that will be used for kubectl and may be requried for establishing connections ifself (https://github.com/ansible-collections/kubernetes.core/pull/702)
- kustomize - new parameter added to --enable-helm (https://github.com/ansible-collections/kubernetes.core/issues/568)

lowlydba.sqlserver
~~~~~~~~~~~~~~~~~~

- Add ability to prevent changing login's password, even if password supplied.
- Add new input strings to be compatible with dbops v0.9.x (https://github.com/lowlydba/lowlydba.sqlserver/pull/231)

microsoft.ad
~~~~~~~~~~~~

- Added ``group/microsoft.ad.domain`` module defaults group for the ``computer``, ``group``, ``object_info``, ``object``, ``ou``, and ``user`` module. Users can use this defaults group to set common connection options for these modules such as the ``domain_server``, ``domain_username``, and ``domain_password`` options.
- Added support for Jinja2 templating in ldap inventory.
- Make ``name`` an optional parameter for the AD modules. Either ``name`` or ``identity`` needs to be set with their respective behaviours. If creating a new AD user and only ``identity`` is set, that will be the value used for the name of the object.
- Set minimum supported Ansible version to 2.14 to align with the versions still supported by Ansible.
- object_info - Add ActiveDirectory module import

netapp.ontap
~~~~~~~~~~~~

- na_ontap_cifs - new option `offline_files` added in REST, requires ONTAP 9.10 or later.
- na_ontap_cifs_server - new option `is_multichannel_enabled` added in REST, requires ONTAP 9.10 or later.
- na_ontap_cifs_server - new option `lm_compatibility_level` added in REST, requires ONTAP 9.8 or later.
- na_ontap_cluster - new option `certificate.uuid` added in REST, requires ONTAP 9.10 or later.
- na_ontap_cluster_peer - added REST only support for modifying remote intercluster addresses in cluster peer relation.
- na_ontap_ems_destination - new options `syslog`, `port`, `transport`, `message_format`, `timestamp_format_override` and `hostname_format_override` added in REST, requires ONTAP 9.12.1 or later.
- na_ontap_export_policy_rule - added `actions` and `modify` in module output.
- na_ontap_file_security_permissions_acl - added `actions` and `modify` in module output.
- na_ontap_igroup_initiator - added `actions` in module output.
- na_ontap_lun_map - added `actions` in module output.
- na_ontap_lun_map_reporting_nodes - added `actions` in module output.
- na_ontap_name_mappings - added `actions` and `modify` in module output.
- na_ontap_net_ifgrp - updated documentation for parameter `name`.
- na_ontap_node - added `modify` in module output.
- na_ontap_rest_info - added warning message if given subset doesn't support option `owning_resource`.
- na_ontap_s3_services - create, modify S3 service returns `s3_service_info` in module output.
- na_ontap_snapmirror - updated resync and resume operation for synchronous snapmirror relationship in REST.
- na_ontap_storage_auto_giveback - added information on modified attributes in module output.
- na_ontap_vscan_scanner_pool - added REST support to Vscan Scanner Pools Configuration module, requires ONTAP 9.6 or later.
- na_ontap_vserver_audit - new options `schedule.*` added under `log.rotation`, requires ONTAP 9.6 or later.

netapp.storagegrid
~~~~~~~~~~~~~~~~~~

- na_sg_grid_account - New option ``allow_select_object_content`` for enabling use of the S3 SelectObjectContent API.
- na_sg_grid_account - New option ``description`` for setting additional identifying information for the tenant account.

netbox.netbox
~~~~~~~~~~~~~

- CI - CI adjustments [#1154](https://github.com/netbox-community/ansible_modules/pull/1154) [#1155](https://github.com/netbox-community/ansible_modules/pull/1155) [#1157](https://github.com/netbox-community/ansible_modules/pull/1157)
- nb_inventory - Add Virtual Disks to inventory [#1188](https://github.com/netbox-community/ansible_modules/pull/1188)
- nb_inventory - Add facility group_by option [#1059](https://github.com/netbox-community/ansible_modules/pull/1059)
- nb_inventory - Don't extract null values from custom fields [#1184](https://github.com/netbox-community/ansible_modules/pull/1184)
- nb_inventory - Enable ansible-vault strings in config-context data [#1114](https://github.com/netbox-community/ansible_modules/pull/1114)
- nb_inventory - Improve documentation for oob_ip_as_primary_ip [#1218](https://github.com/netbox-community/ansible_modules/pull/1218)
- nb_inventory - Make oob_ip available regardless of oob_ip_as_primary_ip option [#1211](https://github.com/netbox-community/ansible_modules/pull/1211)
- nb_lookup - Add custom field choice set [#1186](https://github.com/netbox-community/ansible_modules/pull/1186)
- nb_lookup - Add endpoint for Virtual Disks [#1177](https://github.com/netbox-community/ansible_modules/pull/1177)
- nb_lookup - Add new VPN endpoints for NetBox 3.7 support [#1162](https://github.com/netbox-community/ansible_modules/pull/1162)
- netbox_device_type and netbox_rack - Change u_height to float [#1200](https://github.com/netbox-community/ansible_modules/pull/1200)
- netbox_export_templates - Update documentation [#1214](https://github.com/netbox-community/ansible_modules/pull/1214)
- netbox_platform - Add config_template option to netbox_platform [#1119](https://github.com/netbox-community/ansible_modules/pull/1119)
- netbox_power_port - Add label [#1202](https://github.com/netbox-community/ansible_modules/pull/1202)
- netbox_power_port_template - Add option module_type to netbox_power_port_template [#1105](https://github.com/netbox-community/ansible_modules/pull/1105)
- netbox_rack_role - Add description option [#1143](https://github.com/netbox-community/ansible_modules/pull/1143)
- netbox_virtual_disk - New module [#1153](https://github.com/netbox-community/ansible_modules/pull/1153)
- netbox_virtual_machine and netbox_device - Add option config_template [#1171](https://github.com/netbox-community/ansible_modules/pull/1171)

purestorage.flasharray
~~~~~~~~~~~~~~~~~~~~~~

- all - ``distro`` package added as a pre-requisite
- multiple - Remove packaging pre-requisite.
- multiple - Where only REST 2.x endpoints are used, convert to REST 2.x methodology.
- purefa_arrayname - Convert to REST v2
- purefa_dns - Added facility to add a CA certifcate to management DNS and check peer.
- purefa_eula - Only sign if not previously signed. From REST 2.30 name, title and company are no longer required
- purefa_hg - Add support to rename existing hostgroup
- purefa_info - Add NSID value for NVMe namespace in `hosts` response
- purefa_info - Add ``is_local`` parameter for snapshots
- purefa_info - Add performance data for some subsets
- purefa_info - Add service_mode to identify if array is Evergreen//One or standard FlashArray
- purefa_info - Add support for controller uptime from Purity//FA 6.6.3
- purefa_info - Expose NFS security flavor for policies
- purefa_info - Expose cloud capacity details if array is a Cloud Block Store.
- purefa_info - Subset `pgroups` now also provides a new dict called `deleted_pgroups`
- purefa_inventory - Convert to REST v2
- purefa_ntp - Convert to REST v2
- purefa_offload - Convert to REST v2
- purefa_offload - Remove `nfs` as an option when Purity//FA 6.6.0 or higher is detected
- purefa_pg - Enhance ``state absent`` to work on volumes, hosts and hostgroups
- purefa_pgsnap - Module now requires minimum FlashArray Purity//FA 6.1.0
- purefa_policy - Add SMB user based enumeration parameter
- purefa_policy - Added NFS security flavors for accessing files in the mount point.
- purefa_policy - Remove default setting for nfs_version to allow for change of version at policy level
- purefa_ra - Add ``present`` and ``absent`` as valid ``state`` options
- purefa_ra - Add connecting as valid status of RA to perform operations on
- purefa_ra - Convert to REST v2
- purefa_snap - Add ``created_epoch`` parameter in response
- purefa_snap - Add support for suffix on remote offload snapshots
- purefa_syslog - ``name`` becomes a required parameter as module converts to full REST 2 support
- purefa_vnc - Convert to REST v2

purestorage.flashblade
~~~~~~~~~~~~~~~~~~~~~~

- purefb_bucket - Add support for public buckets
- purefb_bucket - Add support for strict 17a-4 WORM compliance.
- purefb_bucket - From REST 2.12 the `mode` parameter default changes to `multi-site-writable`.
- purefb_connect - Increase Fan-In and Fan-Out maximums
- purefb_ds - Add `force_bind_password` parameter to allow module to be idempotent.
- purefb_fs - Add ``group_ownership`` parameter from Purity//FB 4.4.0.
- purefb_fs - Added SMB Continuous Availability parameter. Requires REST 2.12 or higher.
- purefb_info - Added enhanced information for buckets, filesystems and snapshots, based on new features in REST 2.12
- purefb_info - Show array network access policy from Purity//FB 4.4.0
- purefb_policy - Add support for network access policies from Purity//FB 4.4.0
- purefb_s3acc - Add support for public buckets
- purefb_s3acc - Remove default requirements for ``hard_limit`` and ``default_hard_limit``

telekom_mms.icinga_director
~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Extended docs and examples for multiple assign_filter conditions (https://github.com/telekom-mms/ansible-collection-icinga-director/pull/227)
- Increase sleep to 5 seconds (https://github.com/telekom-mms/ansible-collection-icinga-director/pull/245)

theforeman.foreman
~~~~~~~~~~~~~~~~~~

- content_view_publish role - allow passing ``async`` and ``poll`` to the module (https://github.com/theforeman/foreman-ansible-modules/pull/1676)
- convert2rhel role - install ``convert2rhel`` from ``cdn-public.redhat.com``, dropping the requirement of a custom CA cert

vmware.vmware_rest
~~~~~~~~~~~~~~~~~~

- Add requires_ansible to manifest (https://github.com/ansible-community/ansible.content_builder/pull/76).
- Generate action_groups for the vmware.vmware_rest collection (https://github.com/ansible-community/ansible.content_builder/issues/75).
- Use 7.0 U3 API spec to build the modules (https://github.com/ansible-collections/vmware.vmware_rest/pull/449).
- Use folder attribute for host and dc module only (https://github.com/ansible-community/ansible.content_builder/pull/79).

vultr.cloud
~~~~~~~~~~~

- Added retry on HTTP 504 returned by the API (https://github.com/vultr/ansible-collection-vultr/pull/104).
- Implemented a feature to distinguish resources by region if available. This allows to have identical name per region e.g. a VPC named ``default`` in each region. (https://github.com/vultr/ansible-collection-vultr/pull/98).
- instance - Added a new param ``user_scheme`` to change user scheme to non-root on Linux while creating the instance (https://github.com/vultr/ansible-collection-vultr/issues/96).

Breaking Changes / Porting Guide
--------------------------------

Ansible-core
~~~~~~~~~~~~

- assert - Nested templating may result in an inability for the conditional to be evaluated. See the porting guide for more information.

amazon.aws
~~~~~~~~~~

- amazon.aws collection - Support for ansible-core < 2.15 has been dropped (https://github.com/ansible-collections/amazon.aws/pull/2093).
- iam_role - ``iam_role.assume_role_policy_document`` is no longer converted from CamelCase to snake_case (https://github.com/ansible-collections/amazon.aws/pull/2040).
- iam_role_info - ``iam_role.assume_role_policy_document`` is no longer converted from CamelCase to snake_case (https://github.com/ansible-collections/amazon.aws/pull/2040).
- kms_key - the ``policies`` return value has been renamed to ``key_policies`` the contents has not been changed (https://github.com/ansible-collections/amazon.aws/pull/2040).
- kms_key_info - the ``policies`` return value has been renamed to ``key_policies`` the contents has not been changed (https://github.com/ansible-collections/amazon.aws/pull/2040).
- lambda_event - | ``batch_size`` no longer defaults to 100. According to the boto3 API (https://boto3.amazonaws.com/v1/documentation/api/1.26.78/reference/services/lambda.html#Lambda.Client.create_event_source_mapping), ``batch_size`` defaults to 10 for sqs sources and to 100 for stream sources (https://github.com/ansible-collections/amazon.aws/pull/2025).

cloud.common
~~~~~~~~~~~~

- Bump minimum Python supported version to 3.9.
- Remove support for ansible-core < 2.14.

community.aws
~~~~~~~~~~~~~

- The community.aws collection has dropped support for ``botocore<1.29.0`` and ``boto3<1.26.0``. Most modules will continue to work with older versions of the AWS SDK, however compatability with older versions of the SDK is not guaranteed and will not be tested. When using older versions of the SDK a warning will be emitted by Ansible (https://github.com/ansible-collections/amazon.aws/pull/1763).
- aws_region_info - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.aws_region_info``.
- aws_s3_bucket_info - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.aws_s3_bucket_info``.
- community.aws collection - Support for ansible-core < 2.15 has been dropped (https://github.com/ansible-collections/community.aws/pull/2074).
- community.aws collection - due to the AWS SDKs announcing the end of support for Python less than 3.7 (https://aws.amazon.com/blogs/developer/python-support-policy-updates-for-aws-sdks-and-tools/) support for Python less than 3.7 by this collection wss been deprecated in release 6.0.0 and removed in release 7.0.0. (https://github.com/ansible-collections/amazon.aws/pull/1763).
- iam_access_key - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.iam_access_key``.
- iam_access_key_info - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.iam_access_key_info``.
- iam_group - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.iam_group`` (https://github.com/ansible-collections/community.aws/pull/1945).
- iam_managed_policy - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.iam_managed_policy`` (https://github.com/ansible-collections/community.aws/pull/1954).
- iam_mfa_device_info - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.iam_mfa_device_info`` (https://github.com/ansible-collections/community.aws/pull/1953).
- iam_password_policy - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.iam_password_policy``.
- iam_role - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.iam_role`` (https://github.com/ansible-collections/community.aws/pull/1948).
- iam_role_info - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.iam_role_info`` (https://github.com/ansible-collections/community.aws/pull/1948).
- s3_bucket_info - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.s3_bucket_info``.
- sts_assume_role - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.sts_assume_role``.

community.ciscosmb
~~~~~~~~~~~~~~~~~~

- in facts of interface 'bandwith' changed to 'bandwidth'

community.dns
~~~~~~~~~~~~~

- The default for the ``txt_character_encoding`` options in various modules and plugins changed from ``octal`` to ``decimal`` (https://github.com/ansible-collections/community.dns/pull/196).
- inventory plugins - ``filters`` is now no longer an alias of ``simple_filters``, but a new, different option (https://github.com/ansible-collections/community.dns/pull/196).
- inventory plugins - the ``plugin`` option is now required (https://github.com/ansible-collections/community.dns/pull/196).
- lookup, lookup_as_dict - the default for ``search`` changed from ``false`` (implicit default for community.dns 2.x.y) to ``true`` (https://github.com/ansible-collections/community.dns/issues/200, https://github.com/ansible-collections/community.dns/pull/201).

community.general
~~~~~~~~~~~~~~~~~

- cpanm - the default of the ``mode`` option changed from ``compatibility`` to ``new`` (https://github.com/ansible-collections/community.general/pull/8198).
- django_manage - the module now requires Django >= 4.1 (https://github.com/ansible-collections/community.general/pull/8198).
- django_manage - the module will now fail if ``virtualenv`` is specified but no virtual environment exists at that location (https://github.com/ansible-collections/community.general/pull/8198).
- redfish_command, redfish_config, redfish_info - change the default for ``timeout`` from 10 to 60 (https://github.com/ansible-collections/community.general/pull/8198).

community.hrobot
~~~~~~~~~~~~~~~~

- robot inventory plugin - ``filters`` is now no longer an alias of ``simple_filters``, but a new, different option (https://github.com/ansible-collections/community.hrobot/pull/101).

community.okd
~~~~~~~~~~~~~

- Bump minimum Python suupported version to 3.9 (https://github.com/openshift/community.okd/pull/202).
- Remove support for ansible-core < 2.14 (https://github.com/openshift/community.okd/pull/202).

hetzner.hcloud
~~~~~~~~~~~~~~

- Drop support for ansible-core 2.13.
- certificate - The `not_valid_before` and `not_valid_after` values are now returned as ISO-8601 formatted strings.
- certificate_info - The `not_valid_before` and `not_valid_after` values are now returned as ISO-8601 formatted strings.
- inventory - Remove the deprecated `api_token_env` option, you may use the `ansible.builtin.env` lookup as alternative.
- iso_info - The `deprecated` value is now returned as ISO-8601 formatted strings.

kubernetes.core
~~~~~~~~~~~~~~~

- Remove support for ansible-core < 2.14
- Update python kubernetes library to 24.2.0, helm/kind-action to 1.8.0, kubernetes >= 1.24.

theforeman.foreman
~~~~~~~~~~~~~~~~~~

- content_view_filter - stop managing rules from this module, ``content_view_filter_rule`` should be used for that
- inventory plugin - do not default to ``http://localhost:3000`` as the Foreman URL, providing a URL is now mandatory

vmware.vmware_rest
~~~~~~~~~~~~~~~~~~

- Remove support for ansible-core < 2.14

Deprecated Features
-------------------

- The ``inspur.sm`` collection is considered unmaintained and will be removed from Ansible 11 if no one starts maintaining it again before Ansible 11.
  See `Collections Removal Process for unmaintained collections <https://docs.ansible.com/ansible/devel/community/collection_contributors/collection_package_removal.html#unmaintained-collections>`__ for more details, including for how this can be cancelled (`https://forum.ansible.com/t/2854 <https://forum.ansible.com/t/2854>`__).
  After removal, users can still install this collection with ``ansible-galaxy collection install inspur.sm``.
- The ``netapp.storagegrid`` collection is considered unmaintained and will be removed from Ansible 11 if no one starts maintaining it again before Ansible 11.
  See `Collections Removal Process for unmaintained collections <https://docs.ansible.com/ansible/devel/community/collection_contributors/collection_package_removal.html#unmaintained-collections>`__ for more details, including for how this can be cancelled (`https://forum.ansible.com/t/2811 <https://forum.ansible.com/t/2811>`__).
  After removal, users can still install this collection with ``ansible-galaxy collection install netapp.storagegrid``.

Ansible-core
~~~~~~~~~~~~

- Old style vars plugins which use the entrypoints `get_host_vars` or `get_group_vars` are deprecated. The plugin should be updated to inherit from `BaseVarsPlugin` and define a `get_vars` method as the entrypoint.
- The 'required' parameter in 'ansible.module_utils.common.process.get_bin_path' API is deprecated (https://github.com/ansible/ansible/issues/82464).
- ``module_utils`` - importing the following convenience helpers from ``ansible.module_utils.basic`` has been deprecated: ``get_exception``, ``literal_eval``, ``_literal_eval``, ``datetime``, ``signal``, ``types``, ``chain``, ``repeat``, ``PY2``, ``PY3``, ``b``, ``binary_type``, ``integer_types``, ``iteritems``, ``string_types``, ``test_type``, ``map`` and ``shlex_quote``.
- ansible-doc - role entrypoint attributes are deprecated and eventually will no longer be shown in ansible-doc from ansible-core 2.20 on (https://github.com/ansible/ansible/issues/82639, https://github.com/ansible/ansible/pull/82678).
- paramiko connection plugin, configuration items in the global scope are being deprecated and will be removed in favor or the existing same options in the plugin itself. Users should not need to change anything (how to configure them are the same) but plugin authors using the global constants should move to using the plugin's get_option().

amazon.aws
~~~~~~~~~~

- aws_ec2 inventory plugin - removal of the previously deprecated ``include_extra_api_calls`` option has been assigned to release 9.0.0 (https://github.com/ansible-collections/amazon.aws/pull/2040).
- cloudformation - the ``template`` parameter has been deprecated and will be removed in a release after 2026-05-01.  The ``template_body`` parameter can be used in conjungtion with the lookup plugin (https://github.com/ansible-collections/amazon.aws/pull/2048).
- iam_policy - removal of the previously deprecated ``policies`` return key has been assigned to release 9.0.0.  Use the ``policy_names`` return key instead (https://github.com/ansible-collections/amazon.aws/pull/2040).
- iam_role_info - in a release after 2026-05-01 paths must begin and end with ``/`` (https://github.com/ansible-collections/amazon.aws/pull/1998).
- module_utils.botocore - the ``boto3`` parameter for ``get_aws_connection_info()`` will be removed in a release after 2025-05-01. The ``boto3`` parameter has been ignored since release 4.0.0 (https://github.com/ansible-collections/amazon.aws/pull/2047).
- module_utils.botocore - the ``boto3`` parameter for ``get_aws_region()`` will be removed in a release after 2025-05-01. The ``boto3`` parameter has been ignored since release 4.0.0 (https://github.com/ansible-collections/amazon.aws/pull/2047).
- module_utils.ec2 - the ``boto3`` parameter for ``get_ec2_security_group_ids_from_names()`` will be removed in a release after 2025-05-01. The ``boto3`` parameter has been ignored since release 4.0.0 (https://github.com/ansible-collections/amazon.aws/pull/2047).
- rds_param_group - the ``rds_param_group`` module has been renamed to ``rds_instance_param_group``. The usage of the module has not changed. The rds_param_group alias will be removed in version 10.0.0 (https://github.com/ansible-collections/amazon.aws/pull/2058).

community.aws
~~~~~~~~~~~~~

- aws_glue_connection - updated the deprecation for removal of the ``connection_parameters`` return key from ``after 2024-06-01`` to release version ``9.0.0``, it is being replaced by the ``raw_connection_parameters`` key (https://github.com/ansible-collections/community.aws/pull/518).
- ecs_cluster - updated the deprecation for updated default of ``purge_capacity_providers``, the current default of ``False`` will be changed to ``True`` in release ``9.0.0``.  To maintain the current behaviour explicitly set ``purge_capacity_providers=False`` (https://github.com/ansible-collections/community.aws/pull/1640).
- ecs_service - updated the deprecation for updated default of ``purge_placement_constraints``, the current default of ``False`` will be changed to ``True`` in release ``9.0.0``.  To maintain the current behaviour explicitly set ``purge_placement_constraints=False`` (https://github.com/ansible-collections/community.aws/pull/1716).
- ecs_service - updated the deprecation for updated default of ``purge_placement_strategy``, the current default of ``False`` will be changed to ``True`` in release ``9.0.0``.  To maintain the current behaviour explicitly set ``purge_placement_strategy=False`` (https://github.com/ansible-collections/community.aws/pull/1716).

community.crypto
~~~~~~~~~~~~~~~~

- acme documentation fragment - the default ``community.crypto.acme[.documentation]`` docs fragment is deprecated and will be removed from community.crypto 3.0.0. Replace it with both the new ``community.crypto.acme.basic`` and ``community.crypto.acme.account`` fragments (https://github.com/ansible-collections/community.crypto/pull/735).
- acme.backends module utils - from community.crypto on, all implementations of ``CryptoBackend`` must override ``get_ordered_csr_identifiers()``. The current default implementation, which simply sorts the result of ``get_csr_identifiers()``, will then be removed (https://github.com/ansible-collections/community.crypto/pull/725).
- acme.backends module utils - the ``get_cert_information()`` method for a ACME crypto backend must be implemented from community.crypto 3.0.0 on (https://github.com/ansible-collections/community.crypto/pull/736).
- crypto.module_backends.common module utils - the ``crypto.module_backends.common`` module utils is deprecated and will be removed from community.crypto 3.0.0. Use the improved ``argspec`` module util instead (https://github.com/ansible-collections/community.crypto/pull/749).
- openssl_csr_pipe, openssl_privatekey_pipe, x509_certificate_pipe - the current behavior of check mode is deprecated and will change in community.crypto 3.0.0. The current behavior is similar to the modules without ``_pipe``: if the object needs to be (re-)generated, only the ``changed`` status is set, but the object is not updated. From community.crypto 3.0.0 on, the modules will ignore check mode and always act as if check mode is not active. This behavior can already achieved now by adding ``check_mode: false`` to the task. If you think this breaks your use-case of this module, please `create an issue in the community.crypto repository <https://github.com/ansible-collections/community.crypto/issues/new/choose>`__ (https://github.com/ansible-collections/community.crypto/issues/712, https://github.com/ansible-collections/community.crypto/pull/714).

community.dns
~~~~~~~~~~~~~

- hetzner_dns_records and hosttech_dns_records inventory plugins - the ``filters`` option has been renamed to ``simple_filters``. The old name will stop working in community.hrobot 2.0.0 (https://github.com/ansible-collections/community.dns/pull/181).

community.docker
~~~~~~~~~~~~~~~~

- docker_compose - the Docker Compose v1 module is deprecated and will be removed from community.docker 4.0.0. Please migrate to the ``community.docker.docker_compose_v2`` module, which works with Docker Compose v2 (https://github.com/ansible-collections/community.docker/issues/823, https://github.com/ansible-collections/community.docker/pull/833).
- docker_container - the default ``ignore`` for the ``image_name_mismatch`` parameter has been deprecated and will switch to ``recreate`` in community.docker 4.0.0. A deprecation warning will be printed in situations where the default value is used and where a behavior would change once the default changes (https://github.com/ansible-collections/community.docker/pull/703).
- various modules and plugins - the ``ssl_version`` option has been deprecated and will be removed from community.docker 4.0.0. It has already been removed from Docker SDK for Python 7.0.0, and was only necessary in the past to work around SSL/TLS issues (https://github.com/ansible-collections/community.docker/pull/853).

community.general
~~~~~~~~~~~~~~~~~

- MH DependencyCtxMgr module_utils - deprecate ``module_utils.mh.mixin.deps.DependencyCtxMgr`` in favour of ``module_utils.deps`` (https://github.com/ansible-collections/community.general/pull/8280).
- ModuleHelper module_utils - deprecate ``plugins.module_utils.module_helper.AnsibleModule`` (https://github.com/ansible-collections/community.general/pull/8280).
- ModuleHelper module_utils - deprecate ``plugins.module_utils.module_helper.DependencyCtxMgr`` (https://github.com/ansible-collections/community.general/pull/8280).
- ModuleHelper module_utils - deprecate ``plugins.module_utils.module_helper.StateMixin`` (https://github.com/ansible-collections/community.general/pull/8280).
- ModuleHelper module_utils - deprecate ``plugins.module_utils.module_helper.VarDict,`` (https://github.com/ansible-collections/community.general/pull/8280).
- ModuleHelper module_utils - deprecate ``plugins.module_utils.module_helper.VarMeta`` (https://github.com/ansible-collections/community.general/pull/8280).
- ModuleHelper module_utils - deprecate ``plugins.module_utils.module_helper.VarsMixin`` (https://github.com/ansible-collections/community.general/pull/8280).
- ModuleHelper module_utils - deprecate use of ``VarsMixin`` in favor of using the ``VardDict`` module_utils (https://github.com/ansible-collections/community.general/pull/8226).
- ModuleHelper vars module_utils - bump deprecation of ``VarMeta``, ``VarDict`` and ``VarsMixin`` to version 11.0.0 (https://github.com/ansible-collections/community.general/pull/8226).
- apt_rpm - the behavior of ``state=present`` and ``state=installed`` is deprecated and will change in community.general 11.0.0. Right now the module will upgrade a package to the latest version if one of these two states is used. You should explicitly use ``state=latest`` if you want this behavior, and switch to ``state=present_not_latest`` if you do not want to upgrade the package if it is already installed. In community.general 11.0.0 the behavior of ``state=present`` and ``state=installed`` will change to that of ``state=present_not_latest`` (https://github.com/ansible-collections/community.general/issues/8217, https://github.com/ansible-collections/community.general/pull/8285).
- consul_acl - the module has been deprecated and will be removed in community.general 10.0.0. ``consul_token`` and ``consul_policy`` can be used instead (https://github.com/ansible-collections/community.general/pull/7901).
- django_manage - the ``ack_venv_creation_deprecation`` option has no more effect and will be removed from community.general 11.0.0 (https://github.com/ansible-collections/community.general/pull/8198).
- gitlab modules - the basic auth method on GitLab API have been deprecated and will be removed in community.general 10.0.0 (https://github.com/ansible-collections/community.general/pull/8383).
- hipchat callback plugin - the hipchat service has been discontinued and the self-hosted variant has been End of Life since 2020. The callback plugin is therefore deprecated and will be removed from community.general 10.0.0 if nobody provides compelling reasons to still keep it (https://github.com/ansible-collections/community.general/issues/8184, https://github.com/ansible-collections/community.general/pull/8189).
- irc - the defaults ``false`` for ``use_tls`` and ``validate_certs`` have been deprecated and will change to ``true`` in community.general 10.0.0 to improve security. You can already improve security now by explicitly setting them to ``true``. Specifying values now disables the deprecation warning (https://github.com/ansible-collections/community.general/pull/7578).

community.hrobot
~~~~~~~~~~~~~~~~

- robot inventory plugin - the ``filters`` option has been renamed to ``simple_filters``. The old name will stop working in community.hrobot 2.0.0 (https://github.com/ansible-collections/community.hrobot/pull/94).

community.okd
~~~~~~~~~~~~~

- openshift - the ``openshift`` inventory plugin has been deprecated and will be removed in release 4.0.0 (https://github.com/ansible-collections/kubernetes.core/issues/31).

community.vmware
~~~~~~~~~~~~~~~~

- vmware_guest_tools_info - `vm_tools_install_status` will be removed from next major version (5.0.0) of the collection since the API call that provides this information has been deprecated by VMware. Use `vm_tools_running_status` / `vm_tools_version_status` instead (https://github.com/ansible-collections/community.vmware/issues/2033).

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- The ``dellemc_idrac_storage_volume`` module is deprecated and replaced with ``idrac_storage_volume``.

kubernetes.core
~~~~~~~~~~~~~~~

- k8s - the ``k8s`` inventory plugin has been deprecated and will be removed in release 4.0.0 (https://github.com/ansible-collections/kubernetes.core/issues/31).

Removed Features (previously deprecated)
----------------------------------------

- The ``community.azure`` collection was considered unmaintained and has been removed from Ansible 10 (`https://github.com/ansible-community/community-topics/issues/263 <https://github.com/ansible-community/community-topics/issues/263>`__).
  Users can still install this collection with ``ansible-galaxy collection install community.azure``.
- The ``gluster.gluster`` collection was considered unmaintained and has been removed from Ansible 10 (`https://github.com/ansible-community/community-topics/issues/225 <https://github.com/ansible-community/community-topics/issues/225>`__).
  Users can still install this collection with ``ansible-galaxy collection install gluster.gluster``.
- The ``hpe.nimble`` collection was considered unmaintained and has been removed from Ansible 10 (`https://github.com/ansible-community/community-topics/issues/254 <https://github.com/ansible-community/community-topics/issues/254>`__).
  Users can still install this collection with ``ansible-galaxy collection install hpe.nimble``.
- The ``netapp.aws`` collection was considered unmaintained and has been removed from Ansible 10 (`https://github.com/ansible-community/community-topics/issues/223 <https://github.com/ansible-community/community-topics/issues/223>`__).
  Users can still install this collection with ``ansible-galaxy collection install netapp.aws``.
- The ``netapp.azure`` collection was considered unmaintained and has been removed from Ansible 10 (`https://github.com/ansible-community/community-topics/issues/234 <https://github.com/ansible-community/community-topics/issues/234>`__).
  Users can still install this collection with ``ansible-galaxy collection install netapp.azure``.
- The ``netapp.elementsw`` collection was considered unmaintained and has been removed from Ansible 10 (`https://github.com/ansible-community/community-topics/issues/235 <https://github.com/ansible-community/community-topics/issues/235>`__).
  Users can still install this collection with ``ansible-galaxy collection install netapp.elementsw``.
- The ``netapp.um_info`` collection was considered unmaintained and has been removed from Ansible 10 (`https://github.com/ansible-community/community-topics/issues/244 <https://github.com/ansible-community/community-topics/issues/244>`__).
  Users can still install this collection with ``ansible-galaxy collection install netapp.um_info``.
- The collection ``community.sap`` has been completely removed from Ansible.
  It has been renamed to ``community.sap_libs``.
  The collection will be completely removed from Ansible eventually.
  Please update your FQCNs from ``community.sap`` to ``community.sap_libs``.
- The deprecated ``purestorage.fusion`` collection has been removed (`https://forum.ansible.com/t/3712 <https://forum.ansible.com/t/3712>`__).

Ansible-core
~~~~~~~~~~~~

- Remove deprecated APIs from ansible-docs (https://github.com/ansible/ansible/issues/81716).
- Remove deprecated JINJA2_NATIVE_WARNING environment variable (https://github.com/ansible/ansible/issues/81714)
- Remove deprecated ``scp_if_ssh`` from ssh connection plugin (https://github.com/ansible/ansible/issues/81715).
- Remove deprecated crypt support from ansible.utils.encrypt (https://github.com/ansible/ansible/issues/81717)
- Removed Python 2.7 and Python 3.6 as a supported remote version. Python 3.7+ is now required for target execution.
- With the removal of Python 2 support, the yum module and yum action plugin are removed and redirected to ``dnf``.

amazon.aws
~~~~~~~~~~

- iam_role - the ``iam_role.assume_role_policy_document_raw`` return value has been deprecated.  ``iam_role.assume_role_policy_document`` now returns the same format as ``iam_role.assume_role_policy_document_raw`` (https://github.com/ansible-collections/amazon.aws/pull/2040).
- iam_role_info - the ``iam_role.assume_role_policy_document_raw`` return value has been deprecated.  ``iam_role.assume_role_policy_document`` now returns the same format as ``iam_role.assume_role_policy_document_raw`` (https://github.com/ansible-collections/amazon.aws/pull/2040).
- module_utils.policy - the previously deprecated ``sort_json_policy_dict()`` function has been removed, consider using ``compare_policies()`` instead (https://github.com/ansible-collections/amazon.aws/pull/2052).

arista.eos
~~~~~~~~~~

- Remove depreacted eos_bgp module which is replaced with eos_bgp_global and eos_bgp_address_family.
- Remove deprecated eos_logging module which is replaced with eos_logging_global resource module.
- Remove deprecated timers.throttle attribute.

cisco.ios
~~~~~~~~~

- Deprecated ios_ntp module in favor of ios_ntp_global.
- Removed previously deprecated ios_bgp module in favor of ios_bgp_global and ios_bgp_address_family.

cisco.iosxr
~~~~~~~~~~~

- Remove deprecated iosxr_logging module which is replaced with iosxr_logging_global resource module.

cisco.nxos
~~~~~~~~~~

- The nxos_logging module has been removed with this release.
- The nxos_ntp module has been removed with this release.
- The nxos_ntp_auth module has been removed with this release.
- The nxos_ntp_options module has been removed with this release.

community.dns
~~~~~~~~~~~~~

- The collection no longer supports Ansible, ansible-base, and ansible-core releases that are currently End of Life at the time of the 3.0.0 release. This means that Ansible 2.9, ansible-base 2.10, ansible-core 2.11, ansible-core 2.12, and ansible-core 2.13 are no longer supported. The collection might still work with these versions, but it can stop working at any moment without advance notice, and this will not be considered a bug (https://github.com/ansible-collections/community.dns/pull/196).
- hetzner_dns_record_set, hetzner_dns_record - the deprecated alias ``name`` of the prefix option was removed (https://github.com/ansible-collections/community.dns/pull/196).
- hosttech_dns_records - the redirect to the ``hosttech_dns_record_sets`` module has been removed (https://github.com/ansible-collections/community.dns/pull/196).

community.general
~~~~~~~~~~~~~~~~~

- The deprecated redirects for internal module names have been removed. These internal redirects were extra-long FQCNs like ``community.general.packaging.os.apt_rpm`` that redirect to the short FQCN ``community.general.apt_rpm``. They were originally needed to implement flatmapping; as various tooling started to recommend users to use the long names flatmapping was removed from the collection and redirects were added for users who already followed these incorrect recommendations (https://github.com/ansible-collections/community.general/pull/7835).
- ansible_galaxy_install - the ``ack_ansible29`` and ``ack_min_ansiblecore211`` options have been removed. They no longer had any effect (https://github.com/ansible-collections/community.general/pull/8198).
- cloudflare_dns - remove support for SPF records. These are no longer supported by CloudFlare (https://github.com/ansible-collections/community.general/pull/7782).
- django_manage - support for the ``command`` values ``cleanup``, ``syncdb``, and ``validate`` were removed. Use ``clearsessions``, ``migrate``, and ``check`` instead, respectively (https://github.com/ansible-collections/community.general/pull/8198).
- flowdock - this module relied on HTTPS APIs that do not exist anymore and was thus removed (https://github.com/ansible-collections/community.general/pull/8198).
- mh.mixins.deps module utils - the ``DependencyMixin`` has been removed. Use the ``deps`` module utils instead (https://github.com/ansible-collections/community.general/pull/8198).
- proxmox - the ``proxmox_default_behavior`` option has been removed (https://github.com/ansible-collections/community.general/pull/8198).
- rax* modules, rax module utils, rax docs fragment - the Rackspace modules relied on the deprecated package ``pyrax`` and were thus removed (https://github.com/ansible-collections/community.general/pull/8198).
- redhat module utils - the classes ``Rhsm``, ``RhsmPool``, and ``RhsmPools`` have been removed (https://github.com/ansible-collections/community.general/pull/8198).
- redhat_subscription - the alias ``autosubscribe`` of the ``auto_attach`` option was removed (https://github.com/ansible-collections/community.general/pull/8198).
- stackdriver - this module relied on HTTPS APIs that do not exist anymore and was thus removed (https://github.com/ansible-collections/community.general/pull/8198).
- webfaction_* modules - these modules relied on HTTPS APIs that do not exist anymore and were thus removed (https://github.com/ansible-collections/community.general/pull/8198).

community.grafana
~~~~~~~~~~~~~~~~~

- removed deprecated `message` argument in `grafana_dashboard`

community.hrobot
~~~~~~~~~~~~~~~~

- The collection no longer supports Ansible, ansible-base, and ansible-core releases that are currently End of Life at the time of the 2.0.0 release. This means that Ansible 2.9, ansible-base 2.10, ansible-core 2.11, ansible-core 2.12, and ansible-core 2.13 are no longer supported. The collection might still work with these versions, but it can stop working at any moment without advance notice, and this will not be considered a bug (https://github.com/ansible-collections/community.hrobot/pull/101).

junipernetworks.junos
~~~~~~~~~~~~~~~~~~~~~

- Remove deprected junos_logging module which is replaced by junos_logging_global resource module.

Security Fixes
--------------

Ansible-core
~~~~~~~~~~~~

- ANSIBLE_NO_LOG - Address issue where ANSIBLE_NO_LOG was ignored (CVE-2024-0690)
- ansible-galaxy - Prevent roles from using symlinks to overwrite files outside of the installation directory (CVE-2023-5115)
- templating - Address issues where internal templating can cause unsafe variables to lose their unsafe designation (CVE-2023-5764)

community.dns
~~~~~~~~~~~~~

- hosttech_dns_records and hetzner_dns_records inventory plugins - make sure all data received from the remote servers is marked as unsafe, so remote code execution by obtaining texts that can be evaluated as templates is not possible (https://www.die-welt.net/2024/03/remote-code-execution-in-ansible-dynamic-inventory-plugins/, https://github.com/ansible-collections/community.dns/pull/189).

community.docker
~~~~~~~~~~~~~~~~

- docker_containers, docker_machine, and docker_swarm inventory plugins - make sure all data received from the Docker daemon / Docker machine is marked as unsafe, so remote code execution by obtaining texts that can be evaluated as templates is not possible (https://www.die-welt.net/2024/03/remote-code-execution-in-ansible-dynamic-inventory-plugins/, https://github.com/ansible-collections/community.docker/pull/815).

community.general
~~~~~~~~~~~~~~~~~

- cobbler, gitlab_runners, icinga2, linode, lxd, nmap, online, opennebula, proxmox, scaleway, stackpath_compute, virtualbox, and xen_orchestra inventory plugin - make sure all data received from the remote servers is marked as unsafe, so remote code execution by obtaining texts that can be evaluated as templates is not possible (https://www.die-welt.net/2024/03/remote-code-execution-in-ansible-dynamic-inventory-plugins/, https://github.com/ansible-collections/community.general/pull/8098).
- keycloak_identity_provider - the client secret was not correctly sanitized by the module. The return values ``proposed``, ``existing``, and ``end_state``, as well as the diff, did contain the client secret unmasked (https://github.com/ansible-collections/community.general/pull/8355).

community.hrobot
~~~~~~~~~~~~~~~~

- robot inventory plugin - make sure all data received from the Hetzner robot service server is marked as unsafe, so remote code execution by obtaining texts that can be evaluated as templates is not possible (https://www.die-welt.net/2024/03/remote-code-execution-in-ansible-dynamic-inventory-plugins/, https://github.com/ansible-collections/community.hrobot/pull/99).

Bugfixes
--------

Ansible-core
~~~~~~~~~~~~

- Add a version ceiling constraint for pypsrp to avoid potential breaking changes in the 1.0.0 release.
- All core lookups now use set_option(s) even when doing their own custom parsing. This ensures that the options are always the proper type.
- Allow for searching handler subdir for included task via include_role (https://github.com/ansible/ansible/issues/81722)
- AnsibleModule.atomic_move - fix preserving extended ACLs of the destination when it exists (https://github.com/ansible/ansible/issues/72929).
- Cache host_group_vars after instantiating it once and limit the amount of repetitive work it needs to do every time it runs.
- Call PluginLoader.all() once for vars plugins, and load vars plugins that run automatically or are enabled specifically by name subsequently.
- Consolidate systemd detection logic into one place (https://github.com/ansible/ansible/issues/80975).
- Consolidated the list of internal static vars, centralized them as constant and completed from some missing entries.
- Do not print undefined error message twice (https://github.com/ansible/ansible/issues/78703).
- Enable file cache for vaulted files during vars lookup to fix a strong performance penalty in huge and complex playbboks.
- Fix NEVRA parsing of package names that include digit(s) in them (https://github.com/ansible/ansible/issues/76463, https://github.com/ansible/ansible/issues/81018)
- Fix ``force_handlers`` not working with ``any_errors_fatal`` (https://github.com/ansible/ansible/issues/36308)
- Fix ``run_once`` being incorrectly interpreted on handlers (https://github.com/ansible/ansible/issues/81666)
- Fix an issue when setting a plugin name from an unsafe source resulted in ``ValueError: unmarshallable object`` (https://github.com/ansible/ansible/issues/82708)
- Fix check for missing _sub_plugin attribute in older connection plugins (https://github.com/ansible/ansible/pull/82954)
- Fix condition for unquoting configuration strings from ini files (https://github.com/ansible/ansible/issues/82387).
- Fix for when ``any_errors_fatal`` was ignored if error occurred in a block with always (https://github.com/ansible/ansible/issues/31543)
- Fix handlers not being executed in lockstep using the linear strategy in some cases (https://github.com/ansible/ansible/issues/82307)
- Fix handling missing urls in ansible.module_utils.urls.fetch_file for Python 3.
- Fix issue where an ``include_tasks`` handler in a role was not able to locate a file in ``tasks/`` when ``tasks_from`` was used as a role entry point and ``main.yml`` was not present (https://github.com/ansible/ansible/issues/82241)
- Fix issues when tasks withing nested blocks wouldn't run when ``force_handlers`` is set (https://github.com/ansible/ansible/issues/81533)
- Fix loading vars_plugins in roles (https://github.com/ansible/ansible/issues/82239).
- Fix notifying role handlers by listen keyword topics with the "role_name : " prefix (https://github.com/ansible/ansible/issues/82849).
- Fix setting proper locale for git executable when running on non english systems, ensuring git output can always be parsed.
- Fix tasks in always section not being executed for nested blocks with ``any_errors_fatal`` (https://github.com/ansible/ansible/issues/73246)
- Fixes permission for cache json file from 600 to 644 (https://github.com/ansible/ansible/issues/82683).
- Give the tombstone error for ``include`` pre-fork like other tombstoned action/module plugins.
- Harden python templates for respawn and ansiballz around str literal quoting
- Include the task location when a module or action plugin is deprecated (https://github.com/ansible/ansible/issues/82450).
- Interpreter discovery - Add ``Amzn`` to ``OS_FAMILY_MAP`` for correct family fallback for interpreter discovery (https://github.com/ansible/ansible/issues/80882).
- Mirror the behavior of dnf on the command line when handling NEVRAs with omitted epoch (https://github.com/ansible/ansible/issues/71808)
- Plugin loader does not dedupe nor cache filter/test plugins by file basename, but full path name.
- Properly template tags in parent blocks (https://github.com/ansible/ansible/issues/81053)
- Provide additional information about the alternative plugin in the deprecation message (https://github.com/ansible/ansible/issues/80561).
- Remove the galaxy_info field ``platforms`` from the role templates (https://github.com/ansible/ansible/issues/82453).
- Restoring the ability of filters/tests can have same file base name but different tests/filters defined inside.
- Reword the error message when the module fails to parse parameters in JSON format (https://github.com/ansible/ansible/issues/81188).
- Reword warning if the reserved keyword _ansible_ used as a module parameter (https://github.com/ansible/ansible/issues/82514).
- Run all handlers with the same ``listen`` topic, even when notified from another handler (https://github.com/ansible/ansible/issues/82363).
- Slight optimization to hostvars (instantiate template only once per host, vs per call to var).
- Stopped misleadingly advertising ``async`` mode support in the ``reboot`` module (https://github.com/ansible/ansible/issues/71517).
- ``ansible-galaxy role import`` - fix using the ``role_name`` in a standalone role's ``galaxy_info`` metadata by disabling automatic removal of the ``ansible-role-`` prefix. This matches the behavior of the Galaxy UI which also no longer implicitly removes the ``ansible-role-`` prefix. Use the ``--role-name`` option or add a ``role_name`` to the ``galaxy_info`` dictionary in the role's ``meta/main.yml`` to use an alternate role name.
- ``ansible-test sanity --test runtime-metadata`` - add ``action_plugin`` as a valid field for modules in the schema (https://github.com/ansible/ansible/pull/82562).
- ``ansible.module_utils.service`` - ensure binary data transmission in ``daemonize()``
- ``any_errors_fatal`` should fail all hosts and rescue all of them when a ``rescue`` section is specified (https://github.com/ansible/ansible/issues/80981)
- ``include_role`` - properly execute ``v2_playbook_on_include`` and ``v2_runner_on_failed`` callbacks as well as increase ``ok`` and ``failed`` stats in the play recap, when appropriate (https://github.com/ansible/ansible/issues/77336)
- allow_duplicates - fix evaluating if the current role allows duplicates instead of using the initial value from the duplicate's cached role.
- ansible-config init will now dedupe ini entries from plugins.
- ansible-config will now properly template defaults before dumping them.
- ansible-doc - fixed "inicates" typo in output
- ansible-doc - format top-level descriptions with multiple paragraphs as multiple paragraphs, instead of concatenating them (https://github.com/ansible/ansible/pull/83155).
- ansible-galaxy - Deprecate use of the Galaxy v2 API (https://github.com/ansible/ansible/issues/81781)
- ansible-galaxy - Provide a better error message when using a requirements file with an invalid format - https://github.com/ansible/ansible/issues/81901
- ansible-galaxy - Resolve issue with the dataclass used for galaxy.yml manifest caused by using future annotations
- ansible-galaxy - ensure path to ansible collection when installing or downloading doesn't have a backslash (https://github.com/ansible/ansible/pull/79705).
- ansible-galaxy - started allowing the use of pre-releases for collections that do not have any stable versions published. (https://github.com/ansible/ansible/pull/81606)
- ansible-galaxy - started allowing the use of pre-releases for dependencies on any level of the dependency tree that specifically demand exact pre-release versions of collections and not version ranges. (https://github.com/ansible/ansible/pull/81606)
- ansible-galaxy error on dependency resolution will not error itself due to 'virtual' collections not having a name/namespace.
- ansible-galaxy info - fix reporting no role found when lookup_role_by_name returns None.
- ansible-galaxy role import - exit with 1 when the import fails (https://github.com/ansible/ansible/issues/82175).
- ansible-galaxy role install - fix installing roles from Galaxy that have version ``None`` (https://github.com/ansible/ansible/issues/81832).
- ansible-galaxy role install - fix symlinks (https://github.com/ansible/ansible/issues/82702, https://github.com/ansible/ansible/issues/81965).
- ansible-galaxy role install - normalize tarfile paths and symlinks using ``ansible.utils.path.unfrackpath`` and consider them valid as long as the realpath is in the tarfile's role directory (https://github.com/ansible/ansible/issues/81965).
- ansible-inventory - index available_hosts for major performance boost when dumping large inventories
- ansible-pull now will expand relative paths for the ``-d|--directory`` option is now expanded before use.
- ansible-pull will now correctly handle become and connection password file options for ansible-playbook.
- ansible-test - Add a ``pylint`` plugin to work around a known issue on Python 3.12.
- ansible-test - Explicitly supply ``ControlPath=none`` when setting up port forwarding over SSH to address the scenario where the local ssh configuration uses ``ControlPath`` for all hosts, and would prevent ports to be forwarded after the initial connection to the host.
- ansible-test - Fix parsing of cgroup entries which contain a ``:`` in the path (https://github.com/ansible/ansible/issues/81977).
- ansible-test - Include missing ``pylint`` requirements for Python 3.10.
- ansible-test - Properly detect docker host when using ``ssh://`` protocol for connecting to the docker daemon.
- ansible-test - The ``libexpat`` package is automatically upgraded during remote bootstrapping to maintain compatibility with newer Python packages.
- ansible-test - The ``validate-modules`` sanity test no longer attempts to process files with unrecognized extensions as Python (resolves https://github.com/ansible/ansible/issues/82604).
- ansible-test - Update ``pylint`` to version 3.0.1.
- ansible-test ansible-doc sanity test - do not remove underscores from plugin names in collections before calling ``ansible-doc`` (https://github.com/ansible/ansible/pull/82574).
- ansible-test validate-modules sanity test - do not treat leading underscores for plugin names in collections as an attempted deprecation (https://github.com/ansible/ansible/pull/82575).
- ansible-test — Python 3.8–3.12 will use ``coverage`` v7.3.2.
- ansible.builtin.apt - calling clean = true does not properly clean certain cache files such as /var/cache/apt/pkgcache.bin and /var/cache/apt/pkgcache.bin (https://github.com/ansible/ansible/issues/82611)
- ansible.builtin.uri - the module was ignoring the ``force`` parameter and always requesting a cached copy (via the ``If-Modified-Since`` header) when downloading to an existing local file. Disable caching when ``force`` is ``true``, as documented (https://github.com/ansible/ansible/issues/82166).
- ansible_managed restored it's 'templatability' by ensuring the possible injection routes are cut off earlier in the process.
- apt - honor install_recommends and dpkg_options while installing python3-apt library (https://github.com/ansible/ansible/issues/40608).
- apt - install recommended packages when installing package via deb file (https://github.com/ansible/ansible/issues/29726).
- apt_repository - do not modify repo files if the file is a symlink (https://github.com/ansible/ansible/issues/49809).
- apt_repository - update PPA URL to point to https URL (https://github.com/ansible/ansible/issues/82463).
- assemble - fixed missing parameter 'content' in _get_diff_data API (https://github.com/ansible/ansible/issues/82359).
- async - Fix bug that stopped running async task in ``--check`` when ``check_mode: False`` was set as a task attribute - https://github.com/ansible/ansible/issues/82811
- blockinfile - when ``create=true`` is used with a filename without path, the module crashed (https://github.com/ansible/ansible/pull/81638).
- check if there are attributes to set before attempting to set them (https://github.com/ansible/ansible/issues/76727)
- copy action now also generates temprary files as hidden ('.' prefixed) to avoid accidental pickup by running services that glob by extension.
- copy action now ensures that tempfiles use the same suffix as destination, to allow for ``validate`` to work with utilities that check extensions.
- deb822_repository - handle idempotency if the order of parameters is changed (https://github.com/ansible/ansible/issues/82454).
- debconf - allow user to specify a list for value when vtype is multiselect (https://github.com/ansible/ansible/issues/81345).
- delegate_to when set to an empty or undefined variable will now give a proper error.
- distribution.py - Recognize ALP-Dolomite as part of the SUSE OS family in Ansible, fixing its previous misidentification (https://github.com/ansible/ansible/pull/82496).
- distro - bump bundled distro version from 1.6.0 to 1.8.0 (https://github.com/ansible/ansible/issues/81713).
- dnf - fix an issue when cached RPMs were left in the cache directory even when the keepcache setting was unset (https://github.com/ansible/ansible/issues/81954)
- dnf - fix an issue when installing a package by specifying a file it provides could result in installing a different package providing the same file than the package already installed resulting in resolution failure (https://github.com/ansible/ansible/issues/82461)
- dnf - properly set gpg check options on enabled repositories according to the ``disable_gpg_check`` option (https://github.com/ansible/ansible/issues/80110)
- dnf - properly skip unavailable packages when ``skip_broken`` is enabled (https://github.com/ansible/ansible/issues/80590)
- dnf - the ``nobest`` option only overrides the distribution default when explicitly used, and is used for all supported operations (https://github.com/ansible/ansible/issues/82616)
- dnf5 - replace removed API calls
- dnf5 - respect ``allow_downgrade`` when installing packages directly from rpm files
- dnf5 - the ``nobest`` option only overrides the distribution default when used
- dwim functions for lookups should be better at detectging role context even in abscense of tasks/main.
- ensure we have logger before we log when we have increased verbosity.
- expect - fix argument spec error using timeout=null (https://github.com/ansible/ansible/issues/80982).
- fact gathering on linux now handles thread count by using rounding vs dropping decimals, it should give slightly more accurate numbers.
- facts - add a generic detection for VMware in product name.
- facts - detect VMware ESXi 8.0 virtualization by product name VMware20,1
- fetch - Do not calculate the file size for Windows fetch targets to improve performance.
- fetch - add error message when using ``dest`` with a trailing slash that becomes a local directory - https://github.com/ansible/ansible/issues/82878
- find - do not fail on Permission errors (https://github.com/ansible/ansible/issues/82027).
- first_found lookup now always returns a full (absolute) and normalized path
- first_found lookup now always takes into account k=v options
- flush_handlers - properly handle a handler failure in a nested block when ``force_handlers`` is set (http://github.com/ansible/ansible/issues/81532)
- galaxy - skip verification for unwanted Python compiled bytecode files (https://github.com/ansible/ansible/issues/81628).
- handle exception raised while validating with elements='int' and value is not within choices (https://github.com/ansible/ansible/issues/82776).
- include_tasks - include `ansible_loop_var` and `ansible_index_var` in a loop (https://github.com/ansible/ansible/issues/82655).
- include_vars - fix calculating ``depth`` relative to the root and ensure all files are included (https://github.com/ansible/ansible/issues/80987).
- interpreter_discovery - handle AnsibleError exception raised while interpreter discovery (https://github.com/ansible/ansible/issues/78264).
- iptables - add option choices 'src,src' and 'dst,dst' in match_set_flags (https://github.com/ansible/ansible/issues/81281).
- iptables - set jump to DSCP when set_dscp_mark or set_dscp_mark_class is set (https://github.com/ansible/ansible/issues/77077).
- known_hosts - Fix issue with `@cert-authority` entries in known_hosts incorrectly being removed.
- module no_log will no longer affect top level booleans, for example ``no_log_module_parameter='a'`` will no longer hide ``changed=False`` as a 'no log value' (matches 'a').
- moved assemble, raw, copy, fetch, reboot, script and wait_for_connection to query task instead of play_context ensuring they get the lastest and most correct data.
- reboot action now handles connections with 'timeout' vs only 'connection_timeout' settings.
- role params now have higher precedence than host facts again, matching documentation, this had unintentionally changed in 2.15.
- roles, code cleanup and performance optimization of dependencies, now cached,  and ``public`` setting is now determined once, at role instantiation.
- roles, the ``static`` property is now correctly set, this will fix issues with ``public`` and ``DEFAULT_PRIVATE_ROLE_VARS`` controls on exporting vars.
- set_option method for plugins to update config now properly passes through type casting and validation.
- ssh - add tests for the SSH connection plugin.
- support url-encoded credentials in URLs like http://x%40:%40@example.com (https://github.com/ansible/ansible/pull/82552)
- syslog - Handle ValueError exception raised when sending Null Characters to syslog with Python 3.12.
- systemd_services - update documentation regarding required_one_of and required_by parameters (https://github.com/ansible/ansible/issues/82914).
- template - Fix error when templating an unsafe string which corresponds to an invalid type in Python (https://github.com/ansible/ansible/issues/82600).
- template action will also inherit the behavior from copy (as it uses it internally).
- templating - ensure syntax errors originating from a template being compiled into Python code object result in a failure (https://github.com/ansible/ansible/issues/82606)
- unarchive - add support for 8 character permission strings for zip archives (https://github.com/ansible/ansible/pull/81705).
- unarchive - force unarchive if symlink target changes (https://github.com/ansible/ansible/issues/30420).
- unarchive modules now uses zipinfo options without relying on implementation defaults, making it more compatible with all OS/distributions.
- unsafe data - Address an incompatibility when iterating or getting a single index from ``AnsibleUnsafeBytes``
- unsafe data - Address an incompatibility with ``AnsibleUnsafeText`` and ``AnsibleUnsafeBytes`` when pickling with ``protocol=0``
- unsafe data - Enable directly using ``AnsibleUnsafeText`` with Python ``pathlib`` (https://github.com/ansible/ansible/issues/82414)
- uri - update the documentation for follow_redirects.
- uri action plugin now skipped during check mode (not supported) instead of even trying to execute the module, which already skipped, this does not really change the result, but returns much faster.
- vars - handle exception while combining VarsWithSources and dict (https://github.com/ansible/ansible/issues/81659).
- wait_for should not handle 'non mmapable files' again.
- winrm - Better handle send input failures when communicating with hosts under load
- winrm - Do not raise another exception during cleanup when a task is timed out - https://github.com/ansible/ansible/issues/81095
- winrm - does not hang when attempting to get process output when stdin write failed

amazon.aws
~~~~~~~~~~

- backup_plan - Fix idempotency issue when using botocore >= 1.31.36 (https://github.com/ansible-collections/amazon.aws/issues/1952).
- cloudwatchevent_rule - Fix to avoid adding quotes to JSON input for provided input_template (https://github.com/ansible-collections/amazon.aws/pull/1883).
- cloudwatchlogs_log_group_info - Implement exponential backoff when making API calls to prevent throttling exceptions (https://github.com/ansible-collections/amazon.aws/issues/2011).
- ec2_vpc_subnet - cleanly handle failure when subnet isn't created in time (https://github.com/ansible-collections/amazon.aws/pull/1848).
- elb_classic_lb - fixes bug where ``proxy_protocol`` not being set or being set to ``None`` may result in unexpected behaviour or errors (https://github.com/ansible-collections/amazon.aws/pull/2049).
- iam_managed_policy - fixed an issue where only partial results were returned (https://github.com/ansible-collections/amazon.aws/pull/1936).
- iam_managed_policy - fixes bug that causes ``ParamValidationError`` when attempting to delete a policy that's attached to a role or a user (https://github.com/ansible-collections/amazon.aws/issues/2067).
- iam_role_info - fixes bug in handling paths missing the ``/`` prefix and/or suffix (https://github.com/ansible-collections/amazon.aws/issues/2065).
- lambda_event - Fix when ``batch_size`` is greater than 10, by enabling support for setting ``maximum_batching_window_in_seconds`` (https://github.com/ansible-collections/amazon.aws/pull/2025).
- lambda_event - Retrieve function ARN using AWS API (get_function) instead of building it with AWS account information (https://github.com/ansible-collections/amazon.aws/issues/1859).
- lookup/secretsmanager_secret - fix the issue when the nested secret is missing and on_missing is set to warn, the lookup was raising an error instead of a warning message (https://github.com/ansible-collections/amazon.aws/issues/1781).
- module_utils/elbv2 - Fix issue when creating or modifying Load balancer rule type authenticate-oidc using ``ClientSecret`` parameter and ``UseExistingClientSecret=true`` (https://github.com/ansible-collections/amazon.aws/issues/1877).
- plugin_utils.inventory - Ensure templated options in lookup plugins are converted (https://github.com/ansible-collections/amazon.aws/issues/1955).
- plugins/inventory/aws_ec2 - Fix failure when retrieving information for more than 40 instances with use_ssm_inventory (https://github.com/ansible-collections/amazon.aws/issues/1713).
- s3_object - Fix the issue when copying an object with overriding metadata. (https://github.com/ansible-collections/amazon.aws/issues/1991).
- s3_object - Fix typo that caused false deprecation warning when setting ``overwrite=latest`` (https://github.com/ansible-collections/amazon.aws/pull/1847).
- s3_object - fix idempotency issue when copying object uploaded using multipart upload (https://github.com/ansible-collections/amazon.aws/issues/2016).
- s3_object - when doing a put and specifying ``Content-Type`` in metadata, this module (since 6.0.0) erroneously set the ``Content-Type`` to ``None`` causing the put to fail. Fix now correctly honours the specified ``Content-Type`` (https://github.com/ansible-collections/amazon.aws/issues/1881).

ansible.netcommon
~~~~~~~~~~~~~~~~~

- Added guidance for users to open an issue for the respective platform if plugin support is needed.
- Improved module execution to gracefully handle cases where plugin support is required, providing a clear error message to the user.
- libssh connection plugin - stop using deprecated ``PlayContext.verbosity`` property that is no longer present in ansible-core 2.18 (https://github.com/ansible-collections/ansible.netcommon/pull/626).
- network_cli - removed deprecated play_context.verbosity property.

ansible.utils
~~~~~~~~~~~~~

- Avoid unnecessary use of persistent connection in `cli_parse`, `fact_diff`, `update_fact` and `validate` as this action does not require a connection.

ansible.windows
~~~~~~~~~~~~~~~

- Process.cs - Fix up the ``ProcessCreationFlags.CreateProtectedProcess`` typo in the enum name
- setup - Fix up typo ``collection -> collect`` when a timeout occurred during a fact subset
- win_acl - Fix broken path in case of volume junction
- win_get_url - Fix Tls1.3 getting removed from the list of security protocols
- win_powershell - Remove unecessary using in code causing stray error records in output - https://github.com/ansible-collections/ansible.windows/issues/571
- win_service_info - Warn and not fail if ERROR_FILE_NOT_FOUND when trying to query a service - https://github.com/ansible-collections/ansible.windows/issues/556
- win_updates - Fix up typo for Download progress event messages - https://github.com/ansible-collections/ansible.windows/issues/554

arista.eos
~~~~~~~~~~

- This fix is needed because static_routes and vlans are not returning anything when resources are not configured.
- This got noticed in this issue (https://github.com/network-automation/toolkit/issues/47)
- correct a missing whitespace and add 'auth' string.
- correct the parsing of the elements in 'name_servers' in 'eos_system' module.
- correct the reference of string attribute 'reference_bandwith'.
- when static_routes and vlans are not confirgured then return empty list.

check_point.mgmt
~~~~~~~~~~~~~~~~

- httpapi/checkpoint.py - Raise a fatal error if login wasn't successful.

cisco.aci
~~~~~~~~~

- Fix auto logout issue in aci connection plugin to keep connection active between tasks
- Fix idempotency for l3out configuration when l3protocol is used in aci_l3out
- Fix issues with new attributes in aci_interface_policy_leaf_policy_group module by adding conditions to include attributes in the payload only when they are specified by the user (#578)
- Fix query in aci_vmm_controller

cisco.asa
~~~~~~~~~

- Prevents module_defaults from were being incorrectly applied to the platform action, instead of the concerned module.

cisco.ios
~~~~~~~~~

- Prevents module_defaults from were being incorrectly applied to the platform action, instead of the concerned module.
- Updated the ios_ping ping module to support size param.
- ios_acls - Adds back existing remarks for an ace entry when updated with replaced or overridden state, as all remarks for a specific sequence gets removed when ace entry is updated.
- ios_acls - Fix replaced state to consider remarks and ace entries while comparing configuration.
- ios_acls - correctly match the different line for ACL without sequence number
- ios_acls - make sequence optional for rendering of standard acls.
- ios_acls - take correctly in case where we want to push an ACL from a different type
- ios_acls - update module to apply remarks entry with sequence numbers.
- ios_bgp_address_family - description attribute, evalutated as complex object casted to string.
- ios_bgp_global - Explicitly add neighbor address to every parser.
- ios_bgp_global - Shutdown attributes generates negate command on set as false.
- ios_bgp_global - description attribute, evalutated as complex object casted to string.
- ios_bgp_global - fix template attribute to generate configuration commands.
- ios_bgp_global - remote_as not mendatory for neighbors.
- ios_interfaces - description attribute, evalutated as complex object casted to string.
- ios_l3_interfaces - remove validation from ipv6 address parameter.
- ios_ospfv2 - Fix improper rendering of admin_distance attribute.
- ios_prefix_lists - description attribute, evalutated as complex object casted to string.
- ios_route_maps - description attribute, evalutated as complex object casted to string.
- ios_snmp_server - fix group and user IPv6 ACL commands.
- ios_snmp_server - fixed config issue with snmp user password update being idempotent on consecutive runs.
- ios_user - Fix configuration of hashed passwords and secrets.
- ios_user - fix configuration of user with hashed password.
- ios_user - fixed configuration removal of ssh users using purge.
- ios_vlans - Make behaviour of the action states consistent.
- ios_vlans - Top level configuration attribute is not required, the module works with vlan and vlan configuration both.
- ios_vlans - fixes behaviour of shutdown attribute with action states.
- ios_vrf - Update and add missing argspec keys that define the attributes.
- ios_vrf - added MDT related keys

cisco.iosxr
~~~~~~~~~~~

- Fix 'afi' value in bgp_templates RM to valid values.
- Fix issue in gathered state of interfaces and l3_interfaces RMs(https://github.com/ansible-collections/cisco.iosxr/issues/452, https://github.com/ansible-collections/cisco.iosxr/issues/451)

cisco.ise
~~~~~~~~~

- Added missing import re in endpoint module
- Service included active_directories.
- Service included ad_groups.
- Service included custom_attributes.
- Service included duo_identity_sync.
- Service included duo_mfa.
- Service included enable_mfa.
- Service included endpoint_stop_replication_service.
- Service included endpoints.
- Service included full_upgrade.
- Service included is_mfa_enabled.
- Service included native_ipsec.
- Service included px_grid_direct.
- Service included sgt_range_reservation.
- Service included user_equipment.
- Updated to use ciscoisesdk v2.1.1 or newer fixing ciscoisesdk problem.
- ansible.utils changes to `">=2.0.0,<5.0"` in galaxy.yml dependencies.
- network_device_group - change parameter name from ndgtype to othername.
- network_device_group_info - change parameter name from ndgtype to othername.

cisco.meraki
~~~~~~~~~~~~

- Adding `network_clients_info` and `network_client_info`.
- Adding `platform_meraki.rst` to docs.
- Adding `product_types` for update request on networks.
- Adding `smartquotes = False` to `conf.py` and romoving `'` from rst files.
- Adding build_ignore property to galaxy file.
- Adding support to ansible.utils >=3.0
- Idempotency bugs fixed in devices_switch_ports.
- Parameter`organization_id` change to `organizationId` organizations_claim.
- Parameter`organization_id` change to `organizationId` organizations_clone.
- Parameter`organization_id` change to `organizationId` organizations_inventory_claim.
- Parameter`organization_id` change to `organizationId` organizations_inventory_onboarding_cloud_monitoring_export_events.
- Parameter`organization_id` change to `organizationId` organizations_inventory_onboarding_cloud_monitoring_prepare.
- Parameter`organization_id` change to `organizationId` organizations_inventory_release.
- Parameter`organization_id` change to `organizationId` organizations_licenses_assign_seats.
- Parameter`organization_id` change to `organizationId` organizations_licenses_move.
- Parameter`organization_id` change to `organizationId` organizations_licenses_move_seats.
- Parameter`organization_id` change to `organizationId` organizations_licenses_renew_seats.
- Parameter`organization_id` change to `organizationId` organizations_licensing_coterm_licenses_move.
- Parameter`organization_id` change to `organizationId` organizations_networks_combine.
- Parameter`organization_id` change to `organizationId` organizations_switch_devices_clone.
- Parameter`organization_id` change to `organizationId` organizations_users.
- Removing logs in meraki.py.
- networks_syslog_servers is now just an Update action to API.

cisco.mso
~~~~~~~~~

- Fix TypeError for iteration on NoneType in mso_schema_template
- Fixed the useg_subnet logic in mso_schema_template_anp_epg_useg_attribute

cisco.nxos
~~~~~~~~~~

- Prevents module_defaults from were being incorrectly applied to the platform action, instead of the concerned module.
- nxos_acls - Fix parsing of ace entries with range in it. (https://github.com/ansible-collections/cisco.nxos/issues/788)
- nxos_facts - correct parse JSON output when multiple interfaces have IPv6 address assigned (https://github.com/ansible-collections/cisco.nxos/issues/771).
- nxos_file_copy - correctly set file_pull_timeout/persistent_command_timeout value.
- nxos_interfaces - Correctly enable L3 interfaces on supported N3K platforms (https://github.com/ansible-collections/cisco.nxos/issues/749).

community.aws
~~~~~~~~~~~~~

- aws_ssm - disable ``enable-bracketed-paste`` to fix issue with amazon linux 2023 and other OSes (https://github.com/ansible-collections/community.aws/issues/1756)
- mq_broker - ensure broker is created with ``tags`` when passed (https://github.com/ansible-collections/community.aws/issues/1832).
- opensearch - Don't try to read a non existing key from the domain config (https://github.com/ansible-collections/community.aws/pull/1910).
- ssm(connection) - fix bucket region logic when region is ``us-east-1`` (https://github.com/ansible-collections/community.aws/pull/1908).

community.ciscosmb
~~~~~~~~~~~~~~~~~~

- issue
- solved issue
- typo in changelog fragment template
- typo in test script

community.crypto
~~~~~~~~~~~~~~~~

- acme_* modules - also retry requests in case of socket errors, bad status lines, and unknown connection errors; improve error messages in these cases (https://github.com/ansible-collections/community.crypto/issues/680).
- acme_* modules - directly react on bad return data for account creation/retrieval/updating requests (https://github.com/ansible-collections/community.crypto/pull/682).
- acme_* modules - fix improved error reporting in case of socket errors, bad status lines, and unknown connection errors (https://github.com/ansible-collections/community.crypto/pull/684).
- acme_* modules - increase number of retries from 5 to 10 to increase stability with unstable ACME endpoints (https://github.com/ansible-collections/community.crypto/pull/685).
- acme_* modules - make account registration handling more flexible to accept 404 instead of 400 send by DigiCert's ACME endpoint when an account does not exist (https://github.com/ansible-collections/community.crypto/pull/681).
- acme_certificate - respect the order of the CNAME and SAN identifiers that are passed on when creating an ACME order (https://github.com/ansible-collections/community.crypto/issues/723, https://github.com/ansible-collections/community.crypto/pull/725).
- crypto.math module utils - change return values for ``quick_is_not_prime()`` and ``convert_int_to_bytes(0, 0)`` for special cases that do not appear when using the collection (https://github.com/ansible-collections/community.crypto/pull/733).
- ecs_certificate - fixed ``csr`` option to be empty and allow renewal of a specific certificate according to the Renewal Information specification (https://github.com/ansible-collections/community.crypto/pull/740).
- luks_device - fixed module a bug that prevented using ``remove_keyslot`` with the value ``0`` (https://github.com/ansible-collections/community.crypto/pull/710).
- luks_device - fixed module falsely outputting ``changed=false`` when trying to add a new slot with a key that is already present in another slot. The module now rejects adding keys that are already present in another slot (https://github.com/ansible-collections/community.crypto/pull/710).
- luks_device - fixed testing of LUKS passphrases in when specifying a keyslot for cryptsetup version 2.0.3. The output of this cryptsetup version slightly differs from later versions (https://github.com/ansible-collections/community.crypto/pull/710).
- openssl_dhparam - was using an internal function instead of the public API to load DH param files when using the ``cryptography`` backend. The internal function was removed in cryptography 42.0.0. The module now uses the public API, which has been available since support for DH params was added to cryptography (https://github.com/ansible-collections/community.crypto/pull/698).
- openssl_privatekey_info - ``check_consistency=true`` no longer works for RSA keys with cryptography 42.0.0+ (https://github.com/ansible-collections/community.crypto/pull/701).
- openssl_privatekey_info - ``check_consistency=true`` now reports a warning if it cannot determine consistency (https://github.com/ansible-collections/community.crypto/pull/705).
- x509_certificate - since community.crypto 2.19.0 the module was no longer idempotent with respect to ``not_before`` and ``not_after`` times. This is now fixed (https://github.com/ansible-collections/community.crypto/issues/753, https://github.com/ansible-collections/community.crypto/pull/754).
- x509_crl, x509_certificate, x509_certificate_info - when parsing absolute timestamps which omitted the second count, the first digit of the minutes was used as a one-digit minutes count, and the second digit of the minutes as a one-digit second count (https://github.com/ansible-collections/community.crypto/pull/745).

community.digitalocean
~~~~~~~~~~~~~~~~~~~~~~

- The C(project_name) parameter for many modules was used by alias C(project) internally in the codebase, but to work properly C(project_name) must be used in the code. Replace self.module.params.get("project") with self.module.params.get("project_name") (https://github.com/ansible-collections/community.digitalocean/issues/326).
- digital_ocean_kubernetes - module didn't return kubeconfig properly, return documentation was invalid. Fixed version returns data with the same structure all the time, also it is aligned with M(community.digitalocean.digital_ocean_kubernetes_info) documentation return data now. (https://github.com/ansible-collections/community.digitalocean/issues/322).
- inventory plugin - restore reading auth token from env variables (https://github.com/ansible-collections/community.digitalocean/pull/315).

community.dns
~~~~~~~~~~~~~

- DNS record modules, inventory plugins - fix the TXT entry encoder to avoid splitting up escape sequences for quotes and backslashes over multiple TXT strings (https://github.com/ansible-collections/community.dns/issues/190, https://github.com/ansible-collections/community.dns/pull/191).
- Update Public Suffix List.
- inventory plugins - add unsafe wrapper to avoid marking strings that do not contain ``{`` or ``}`` as unsafe, to work around a bug in AWX (https://github.com/ansible-collections/community.dns/pull/197).
- nameserver_record_info - fix crash when more than one record is retrieved (https://github.com/ansible-collections/community.dns/pull/172).
- wait_for_txt, nameserver_info, nameserver_record_info - when looking up nameservers for a domain, do not treat ``NXDOMAIN`` as a fatal error (https://github.com/ansible-collections/community.dns/pull/177).

community.docker
~~~~~~~~~~~~~~~~

- Use ``unix:///var/run/docker.sock`` instead of the legacy ``unix://var/run/docker.sock`` as default for ``docker_host`` (https://github.com/ansible-collections/community.docker/pull/736).
- docker and nsenter connection plugins, docker_container_exec module - avoid using the deprecated ``ansible.module_utils.compat.selectors`` module util with Python 3 (https://github.com/ansible-collections/community.docker/issues/870, https://github.com/ansible-collections/community.docker/pull/871).
- docker_compose_v2 - do not consider a ``Waiting`` event as an action/change (https://github.com/ansible-collections/community.docker/pull/804).
- docker_compose_v2 - do not fail when non-fatal errors occur. This can happen when pulling an image fails, but then the image can be built for another service. Docker Compose emits an error in that case, but ``docker compose up`` still completes successfully (https://github.com/ansible-collections/community.docker/issues/807, https://github.com/ansible-collections/community.docker/pull/810, https://github.com/ansible-collections/community.docker/pull/811).
- docker_compose_v2 - do not treat service-level pull events as changes to avoid incorrect ``changed=true`` return value of ``pull=always`` (https://github.com/ansible-collections/community.docker/issues/802, https://github.com/ansible-collections/community.docker/pull/803).
- docker_compose_v2 - properly parse dry-run build events from ``stderr`` (https://github.com/ansible-collections/community.docker/issues/778, https://github.com/ansible-collections/community.docker/pull/779).
- docker_compose_v2* - allow ``project_src`` to be a relative path, by converting it to an absolute path before using it (https://github.com/ansible-collections/community.docker/issues/827, https://github.com/ansible-collections/community.docker/pull/828).
- docker_compose_v2* modules - abort with a nice error message instead of crash when the Docker Compose CLI plugin version is ``dev`` (https://github.com/ansible-collections/community.docker/issues/825, https://github.com/ansible-collections/community.docker/pull/826).
- docker_compose_v2* modules - correctly parse ``Warning`` events emitted by Docker Compose (https://github.com/ansible-collections/community.docker/issues/807, https://github.com/ansible-collections/community.docker/pull/811).
- docker_compose_v2* modules - parse ``logfmt`` warnings emitted by Docker Compose (https://github.com/ansible-collections/community.docker/issues/787, https://github.com/ansible-collections/community.docker/pull/811).
- docker_compose_v2, docker_compose_v2_pull - fix parsing of pull messages for Docker Compose 2.20.0 (https://github.com/ansible-collections/community.docker/issues/785, https://github.com/ansible-collections/community.docker/pull/786).
- docker_compose_v2_pull - fixing idempotence by checking actual pull progress events instead of service-level pull request when ``policy=always``. This stops the module from reporting ``changed=true`` if no actual change happened when pulling. In check mode, it has to assume that a change happens though (https://github.com/ansible-collections/community.docker/issues/813, https://github.com/ansible-collections/community.docker/pull/814).
- docker_compose_v2_pull - the module was documented as part of the ``community.docker.docker`` action group, but was not actually part of it. That has now been fixed (https://github.com/ansible-collections/community.docker/pull/773).
- docker_image - fix archiving idempotency with Docker API 1.44 or later (https://github.com/ansible-collections/community.docker/pull/765).
- inventory plugins - add unsafe wrapper to avoid marking strings that do not contain ``{`` or ``}`` as unsafe, to work around a bug in AWX (https://github.com/ansible-collections/community.docker/pull/835).
- modules and plugins using the Docker SDK for Python - remove ``ssl_version`` from the parameters passed to Docker SDK for Python 7.0.0+. Explicitly fail with a nicer error message if it was explicitly set in this case (https://github.com/ansible-collections/community.docker/pull/715).
- modules and plugins using the Docker SDK for Python - remove ``tls_hostname`` from the parameters passed to Docker SDK for Python 7.0.0+. Explicitly fail with a nicer error message if it was explicitly set in this case (https://github.com/ansible-collections/community.docker/pull/721).
- vendored Docker SDK for Python - avoid passing on ``ssl_version`` and ``tls_hostname`` if they were not provided by the user. Remove dead code. (https://github.com/ansible-collections/community.docker/pull/722).
- vendored Docker SDK for Python - include a fix requests 2.32.2+ compatibility (https://github.com/ansible-collections/community.docker/issues/860, https://github.com/psf/requests/issues/6707, https://github.com/ansible-collections/community.docker/pull/864).
- vendored Docker SDK for Python - include a hotfix for requests 2.32.0 compatibility (https://github.com/ansible-collections/community.docker/issues/860, https://github.com/docker/docker-py/issues/3256, https://github.com/ansible-collections/community.docker/pull/861).

community.general
~~~~~~~~~~~~~~~~~

- aix_filesystem - fix ``_validate_vg`` not passing VG name to ``lsvg_cmd`` (https://github.com/ansible-collections/community.general/issues/8151).
- aix_filesystem - fix issue with empty list items in crfs logic and option order (https://github.com/ansible-collections/community.general/pull/8052).
- apt-rpm - the module did not upgrade packages if a newer version exists. Now the package will be reinstalled if the candidate is newer than the installed version (https://github.com/ansible-collections/community.general/issues/7414).
- apt_rpm - when checking whether packages were installed after running ``apt-get -y install <packages>``, only the last package name was checked (https://github.com/ansible-collections/community.general/pull/8263).
- bitwarden_secrets_manager lookup plugin - implements retry with exponential backoff to avoid lookup errors when Bitwardn's API rate limiting is encountered (https://github.com/ansible-collections/community.general/issues/8230, https://github.com/ansible-collections/community.general/pull/8238).
- cargo - fix idempotency issues when using a custom installation path for packages (using the ``--path`` parameter). The initial installation runs fine, but subsequent runs use the ``get_installed()`` function which did not check the given installation location, before running ``cargo install``. This resulted in a false ``changed`` state. Also the removal of packeges using ``state: absent`` failed, as the installation check did not use the given parameter (https://github.com/ansible-collections/community.general/pull/7970).
- cloudflare_dns - fix Cloudflare lookup of SHFP records (https://github.com/ansible-collections/community.general/issues/7652).
- consul_token - fix token creation without ``accessor_id`` (https://github.com/ansible-collections/community.general/pull/8091).
- cpanm - use new ``VarDict`` to prevent deprecation warning (https://github.com/ansible-collections/community.general/issues/8410, https://github.com/ansible-collections/community.general/pull/8411).
- django module utils - use new ``VarDict`` to prevent deprecation warning (https://github.com/ansible-collections/community.general/issues/8410, https://github.com/ansible-collections/community.general/pull/8411).
- from_ini filter plugin - disabling interpolation of ``ConfigParser`` to allow converting values with a ``%`` sign (https://github.com/ansible-collections/community.general/issues/8183, https://github.com/ansible-collections/community.general/pull/8185).
- gconftool2_info - use new ``VarDict`` to prevent deprecation warning (https://github.com/ansible-collections/community.general/issues/8410, https://github.com/ansible-collections/community.general/pull/8411).
- gitlab_group_members - fix gitlab constants call in ``gitlab_group_members`` module (https://github.com/ansible-collections/community.general/issues/7467).
- gitlab_issue - fix behavior to search GitLab issue, using ``search`` keyword instead of ``title`` (https://github.com/ansible-collections/community.general/issues/7846).
- gitlab_issue, gitlab_label, gitlab_milestone - avoid crash during version comparison when the python-gitlab Python module is not installed (https://github.com/ansible-collections/community.general/pull/8158).
- gitlab_project_members - fix gitlab constants call in ``gitlab_project_members`` module (https://github.com/ansible-collections/community.general/issues/7467).
- gitlab_protected_branches - fix gitlab constants call in ``gitlab_protected_branches`` module (https://github.com/ansible-collections/community.general/issues/7467).
- gitlab_runner - fix pagination when checking for existing runners (https://github.com/ansible-collections/community.general/pull/7790).
- gitlab_user - fix gitlab constants call in ``gitlab_user`` module (https://github.com/ansible-collections/community.general/issues/7467).
- haproxy - fix an issue where HAProxy could get stuck in DRAIN mode when the backend was unreachable (https://github.com/ansible-collections/community.general/issues/8092).
- homebrew - detect already installed formulae and casks using JSON output from ``brew info`` (https://github.com/ansible-collections/community.general/issues/864).
- homebrew - do not fail when brew prints warnings (https://github.com/ansible-collections/community.general/pull/8406, https://github.com/ansible-collections/community.general/issues/7044).
- homebrew - error returned from brew command was ignored and tried to parse empty JSON. Fix now checks for an error and raises it to give accurate error message to users (https://github.com/ansible-collections/community.general/issues/8047).
- hponcfg - use new ``VarDict`` to prevent deprecation warning (https://github.com/ansible-collections/community.general/issues/8410, https://github.com/ansible-collections/community.general/pull/8411).
- incus connection plugin - treats ``inventory_hostname`` as a variable instead of a literal in remote connections (https://github.com/ansible-collections/community.general/issues/7874).
- interface_files - also consider ``address_family`` when changing ``option=method`` (https://github.com/ansible-collections/community.general/issues/7610, https://github.com/ansible-collections/community.general/pull/7612).
- inventory plugins - add unsafe wrapper to avoid marking strings that do not contain ``{`` or ``}`` as unsafe, to work around a bug in AWX ((https://github.com/ansible-collections/community.general/issues/8212, https://github.com/ansible-collections/community.general/pull/8225).
- ipa - fix get version regex in IPA module_utils (https://github.com/ansible-collections/community.general/pull/8175).
- ipa_hbacrule - the module uses a string for ``ipaenabledflag`` for new FreeIPA versions while the returned value is a boolean (https://github.com/ansible-collections/community.general/pull/7880).
- ipa_otptoken - the module expect ``ipatokendisabled`` as string but the ``ipatokendisabled`` value is returned as a boolean (https://github.com/ansible-collections/community.general/pull/7795).
- ipa_sudorule - the module uses a string for ``ipaenabledflag`` for new FreeIPA versions while the returned value is a boolean (https://github.com/ansible-collections/community.general/pull/7880).
- iptables_state - fix idempotency issues when restoring incomplete iptables dumps (https://github.com/ansible-collections/community.general/issues/8029).
- irc - replace ``ssl.wrap_socket`` that was removed from Python 3.12 with code for creating a proper SSL context (https://github.com/ansible-collections/community.general/pull/7542).
- kernel_blacklist - use new ``VarDict`` to prevent deprecation warning (https://github.com/ansible-collections/community.general/issues/8410, https://github.com/ansible-collections/community.general/pull/8411).
- keycloak_* - fix Keycloak API client to quote ``/`` properly (https://github.com/ansible-collections/community.general/pull/7641).
- keycloak_authz_permission - resource payload variable for scope-based permission was constructed as a string, when it needs to be a list, even for a single item (https://github.com/ansible-collections/community.general/issues/7151).
- keycloak_client - add sorted ``defaultClientScopes`` and ``optionalClientScopes`` to normalizations (https://github.com/ansible-collections/community.general/pull/8223).
- keycloak_client - fix TypeError when sanitizing the ``saml.signing.private.key`` attribute in the module's diff or state output. The ``sanitize_cr`` function expected a dict where in some cases a list might occur (https://github.com/ansible-collections/community.general/pull/8403).
- keycloak_client - fixes issue when metadata is provided in desired state when task is in check mode (https://github.com/ansible-collections/community.general/issues/1226, https://github.com/ansible-collections/community.general/pull/7881).
- keycloak_identity_provider - ``mappers`` processing was not idempotent if the mappers configuration list had not been sorted by name (in ascending order). Fix resolves the issue by sorting mappers in the desired state using the same key which is used for obtaining existing state (https://github.com/ansible-collections/community.general/pull/7418).
- keycloak_identity_provider - it was not possible to reconfigure (add, remove) ``mappers`` once they were created initially. Removal was ignored, adding new ones resulted in dropping the pre-existing unmodified mappers. Fix resolves the issue by supplying correct input to the internal update call (https://github.com/ansible-collections/community.general/pull/7418).
- keycloak_realm - add normalizations for ``enabledEventTypes`` and ``supportedLocales`` (https://github.com/ansible-collections/community.general/pull/8224).
- keycloak_user - when ``force`` is set, but user does not exist, do not try to delete it (https://github.com/ansible-collections/community.general/pull/7696).
- keycloak_user_federation - fix diff of empty ``krbPrincipalAttribute`` (https://github.com/ansible-collections/community.general/pull/8320).
- ldap - previously the order number (if present) was expected to follow an equals sign in the DN. This makes it so the order number string is identified correctly anywhere within the DN (https://github.com/ansible-collections/community.general/issues/7646).
- linode inventory plugin - add descriptive error message for linode inventory plugin (https://github.com/ansible-collections/community.general/pull/8133).
- locale_gen - use new ``VarDict`` to prevent deprecation warning (https://github.com/ansible-collections/community.general/issues/8410, https://github.com/ansible-collections/community.general/pull/8411).
- log_entries callback plugin - replace ``ssl.wrap_socket`` that was removed from Python 3.12 with code for creating a proper SSL context (https://github.com/ansible-collections/community.general/pull/7542).
- lvol - test for output messages in both ``stdout`` and ``stderr`` (https://github.com/ansible-collections/community.general/pull/7601, https://github.com/ansible-collections/community.general/issues/7182).
- merge_variables lookup plugin - fixing cross host merge: providing access to foreign hosts variables to the perspective of the host that is performing the merge (https://github.com/ansible-collections/community.general/pull/8303).
- mksysb - use new ``VarDict`` to prevent deprecation warning (https://github.com/ansible-collections/community.general/issues/8410, https://github.com/ansible-collections/community.general/pull/8411).
- modprobe - listing modules files or modprobe files could trigger a FileNotFoundError if ``/etc/modprobe.d`` or ``/etc/modules-load.d`` did not exist. Relevant functions now return empty lists if the directories do not exist to avoid crashing the module (https://github.com/ansible-collections/community.general/issues/7717).
- mssql_script - make the module work with Python 2 (https://github.com/ansible-collections/community.general/issues/7818, https://github.com/ansible-collections/community.general/pull/7821).
- nmcli - fix ``connection.slave-type`` wired to ``bond`` and not with parameter ``slave_type`` in case of connection type ``wifi`` (https://github.com/ansible-collections/community.general/issues/7389).
- ocapi_utils, oci_utils, redfish_utils module utils - replace ``type()`` calls with ``isinstance()`` calls (https://github.com/ansible-collections/community.general/pull/7501).
- onepassword lookup plugin - failed for fields that were in sections and had uppercase letters in the label/ID. Field lookups are now case insensitive in all cases (https://github.com/ansible-collections/community.general/pull/7919).
- onepassword lookup plugin - field and section titles are now case insensitive when using op CLI version two or later. This matches the behavior of version one (https://github.com/ansible-collections/community.general/pull/7564).
- opentelemetry callback plugin - close spans always (https://github.com/ansible-collections/community.general/pull/8367).
- opentelemetry callback plugin - honour the ``disable_logs`` option to avoid storing task results since they are not used regardless (https://github.com/ansible-collections/community.general/pull/8373).
- pacemaker_cluster - actually implement check mode, which the module claims to support. This means that until now the module also did changes in check mode (https://github.com/ansible-collections/community.general/pull/8081).
- pam_limits - when the file does not exist, do not create it in check mode (https://github.com/ansible-collections/community.general/issues/8050, https://github.com/ansible-collections/community.general/pull/8057).
- pipx module utils - change the CLI argument formatter for the ``pip_args`` parameter (https://github.com/ansible-collections/community.general/issues/7497, https://github.com/ansible-collections/community.general/pull/7506).
- pipx_info - use new ``VarDict`` to prevent deprecation warning (https://github.com/ansible-collections/community.general/issues/8410, https://github.com/ansible-collections/community.general/pull/8411).
- pkgin - pkgin (pkgsrc package manager used by SmartOS) raises erratic exceptions and spurious ``changed=true`` (https://github.com/ansible-collections/community.general/pull/7971).
- proxmox - fix updating a container config if the setting does not already exist (https://github.com/ansible-collections/community.general/pull/7872).
- proxmox_kvm - fixed status check getting from node-specific API endpoint (https://github.com/ansible-collections/community.general/issues/7817).
- proxmox_kvm - running ``state=template`` will first check whether VM is already a template (https://github.com/ansible-collections/community.general/pull/7792).
- proxmox_pool_member - absent state for type VM did not delete VMs from the pools (https://github.com/ansible-collections/community.general/pull/7464).
- puppet - add option ``environment_lang`` to set the environment language encoding. Defaults to lang ``C``. It is recommended to set it to ``C.UTF-8`` or ``en_US.UTF-8`` depending on what is available on your system. (https://github.com/ansible-collections/community.general/issues/8000)
- redfish_command - fix usage of message parsing in ``SimpleUpdate`` and ``MultipartHTTPPushUpdate`` commands to treat the lack of a ``MessageId`` as no message (https://github.com/ansible-collections/community.general/issues/7465, https://github.com/ansible-collections/community.general/pull/7471).
- redfish_info - allow for a GET operation invoked by ``GetUpdateStatus`` to allow for an empty response body for cases where a service returns 204 No Content (https://github.com/ansible-collections/community.general/issues/8003).
- redfish_info - correct uncaught exception when attempting to retrieve ``Chassis`` information (https://github.com/ansible-collections/community.general/pull/7952).
- redhat_subscription - use the D-Bus registration on RHEL 7 only on 7.4 and
  greater; older versions of RHEL 7 do not have it
  (https://github.com/ansible-collections/community.general/issues/7622,
  https://github.com/ansible-collections/community.general/pull/7624).
- riak - support ``riak admin`` sub-command in newer Riak KV versions beside the legacy ``riak-admin`` main command (https://github.com/ansible-collections/community.general/pull/8211).
- snap - use new ``VarDict`` to prevent deprecation warning (https://github.com/ansible-collections/community.general/issues/8410, https://github.com/ansible-collections/community.general/pull/8411).
- snap_alias - use new ``VarDict`` to prevent deprecation warning (https://github.com/ansible-collections/community.general/issues/8410, https://github.com/ansible-collections/community.general/pull/8411).
- statusio_maintenance - fix error caused by incorrectly formed API data payload. Was raising "Failed to create maintenance HTTP Error 400 Bad Request" caused by bad data type for date/time and deprecated dict keys (https://github.com/ansible-collections/community.general/pull/7754).
- terraform - fix multiline string handling in complex variables (https://github.com/ansible-collections/community.general/pull/7535).
- to_ini filter plugin - disabling interpolation of ``ConfigParser`` to allow converting values with a ``%`` sign (https://github.com/ansible-collections/community.general/issues/8183, https://github.com/ansible-collections/community.general/pull/8185).
- xml - make module work with lxml 5.1.1, which removed some internals that the module was relying on (https://github.com/ansible-collections/community.general/pull/8169).

community.grafana
~~~~~~~~~~~~~~~~~

- Add `grafana_organiazion_user` to `action_groups.grafana`
- Fixed orgId handling in diff comparison for `grafana_datasource` if using org_name
- Handling of desired default state for first `grafana_datasource`
- Ignore `type` argument for diff comparison if `grafana-postgresq-datasource` alias `postgres` is used
- Set umask for `grafana_plugin` command
- test: replace deprecated `TestCase.assertEquals` to support Python 3.12
- undo removed deprecated `message` argument in `grafana_dashboard`

community.hrobot
~~~~~~~~~~~~~~~~

- inventory plugins - add unsafe wrapper to avoid marking strings that do not contain ``{`` or ``}`` as unsafe, to work around a bug in AWX (https://github.com/ansible-collections/community.hrobot/pull/102).

community.mysql
~~~~~~~~~~~~~~~

- mysql_info - the ``slave_status`` filter was returning an empty list on MariaDB with multiple replication channels. It now returns all channels by running ``SHOW ALL SLAVES STATUS`` for MariaDB servers (https://github.com/ansible-collections/community.mysql/issues/603).

community.postgresql
~~~~~~~~~~~~~~~~~~~~

- postgresql_db - ``restore`` custom format as file instead of stdin to allow the use of --job flag in ``target_opts`` (https://github.com/ansible-collections/community.postgresql/issues/594).
- postgresql_ext - Reconnect before upgrade to avoid accidental load of the upgraded extension (https://github.com/ansible-collections/community.postgresql/pull/689).
- postgresql_idx - consider schema name when checking for index (https://github.com/ansible-collections/community.postgresql/issues/692).  Index names are only unique within a schema. This allows using the same index name in multiple schemas.
- postgresql_privs - Enables the ability to revoke functions from user (https://github.com/ansible-collections/community.postgresql/issues/687).
- postgresql_privs - fix a failure when altering privileges with ``grant_option: true`` (https://github.com/ansible-collections/community.postgresql/issues/668).
- postgresql_query - now reports not changed for queries starting with "SHOW" (https://github.com/ansible-collections/community.postgresql/pull/592).
- postgresql_user - module failed when running against an SQL_ASCII encoded database as the user's current password was returned as bytes as opposed to a str. Fix now checks for this case and decodes the bytes as an ascii encoded string. (https://github.com/ansible-collections/community.postgresql/issues/584).

community.routeros
~~~~~~~~~~~~~~~~~~

- facts - fix date not getting removed for idempotent config export (https://github.com/ansible-collections/community.routeros/pull/262).

community.sap_libs
~~~~~~~~~~~~~~~~~~

- fixes failures in sanity test for all modules

community.vmware
~~~~~~~~~~~~~~~~

- Clarify pyVmomi requirement (https://github.com/ansible-collections/community.vmware/pull/2071).
- Fix InsecureRequestWarning for modules based on the VmwareRestClient module util when setting ``validate_certs`` to ``False`` (https://github.com/ansible-collections/community.vmware/pull/1969).
- Use `isinstance()` instead of `type()` for a typecheck (https://github.com/ansible-collections/community.vmware/pull/2011).
- module_utils/vmware.py - remove ssl.wrap_socet() function. Replaced for code based on ssl.get_server_certificate (https://github.com/ansible-collections/community.vmware/issues/1930).
- vmware_cluster_dpm - Handle case where DPM config has not been initialized yet and is None (https://github.com/ansible-collections/community.vmware/pull/2057).
- vmware_dvs_portgroup - Fix erroneously reporting a change when `port_binding` is static and `num_ports` not specified (https://github.com/ansible-collections/community.vmware/pull/2053).
- vmware_guest - Fix a error while updating the VM by adding a new disk. While adding a disk to an  existing VM, it leaves it in invalid state. (https://github.com/ansible-collections/community.vmware/pull/2044).
- vmware_guest - Fix a missing error message while setting a template parameter with inconsistency guest_os ID (https://github.com/ansible-collections/community.vmware/pull/2036).
- vmware_guest - Fix failure of vm reconfiguration with enabled virt_based_security (https://github.com/ansible-collections/community.vmware/pull/1848).
- vmware_vm_info - Fix an AttributeError when gathering network information (https://github.com/ansible-collections/community.vmware/pull/1919).

community.windows
~~~~~~~~~~~~~~~~~

- Remove some code which is no longer valid for dotnet 5+
- community.windows.win_psmodule_info - exception thrown when host has no Installed Module. Fix now checks that variable $installedModules is not null before calling the .Contains(..) function on it.
- win_format, win_partition - Add support for Windows failover cluster disks
- win_psmodule - Fix up error message with ``state=latest``
- win_rabbitmq_plugin - Avoid using ``Invoke-Expression`` when running external commands
- win_rds_rap - The module crashed when creating a RAP with Gateway Managed Computer Group (https://github.com/ansible-collections/community.windows/issues/184).
- win_robocopy - Fix up ``cmd`` return value to include the executable ``robocopy``

community.zabbix
~~~~~~~~~~~~~~~~

- Avoid to update user-directory configuration in dry run.
- api module - Fixed certificiate errors
- proxy and server roles - Defaulted location of fping and fping6 based on OS.
- proxy role - Removed requirement for mysql group definition.
- server role - typo in configuration var StasAllowedIP to StatsAllowedIP
- zabbix-{agent, javagateway, proxy, server, web} - support raspberry pi without repository url specification
- zabbix_agent - Fixed IPMI authentication algorithm default setting
- zabbix_agent - Fixed issue to where scripts can be deployed alongside userparameters
- zabbix_host - Don't reset IPMI setting when update inventory data of a host
- zabbix_host - Finish task with failed if host_group parameter is empty list
- zabbix_inventory - fixed handeling of add_zabbix_groups option
- zabbix_server - proper indentaion of become in selinux.yaml
- zabbix_template - fix template export when template's content has "error" word
- zabbix_web - Added missing semicolon to nginx vhost template.
- zabbix_web role - fix variable naming issues (undefined) to zabbix_web_version and zabbix_web_apt_repository
- zabbix_web role, Add missing selinux.yml tasks.

containers.podman
~~~~~~~~~~~~~~~~~

- Add idempotency for podman_secret module
- Catch exceptions when no JSON output in podman_image
- Fail if systemd generation failed and it's explicitly set
- Fix example name
- Fix idempotency for podman_network
- Fix idempotency when using 0.0.0.0 in ports
- Fix multi-image support for podman_save
- Fix pod info for non-existant pods
- Fix volume inspection by name in podman_volume
- Recreate stopped containers if recreate flag is enabled
- podman_container - Add check and fixed for v5 network diff
- podman_container - Fix pasta networking idempotency for v5 (#728)
- podman_container_exec - Remove unnecessary quotes in podman_container_exec module
- podman_image_info - Fix wrong return data type in podman_image_info
- podman_play - Fix kube play annotations
- podman_pod - Fix broken info of pods in Podman v5
- podman_pod - Fix pod for Podman v5
- podman_pod - Fix podman pod v5 broken info issue

dellemc.enterprise_sonic
~~~~~~~~~~~~~~~~~~~~~~~~

- requirements - Update requires_ansible version in meta/runtime.yml to the oldest supported version (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/321).
- sonic_bgp_communities - Fix incorrect "facts" handling for parsing of a BGP community list configured with an empty "members" list (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/319).
- sonic_bgp_neighbors - Fix prefix-limit issue (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/289).
- sonic_interfaces - Add warnings when speed and auto_negotiate is configured at same time (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/314).
- sonic_interfaces - Fix support for standard naming interfaces (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/314).
- sonic_interfaces - Prevent configuring speed in port group interfaces (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/314).
- sonic_stp - Correct the commands list for STP delete state (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/302).

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- Added support for RAID creation using NVMe disks.(https://github.com/dell/dellemc-openmanage-ansible-modules/issues/635)
- Fixed the issue for ignoring the environment variable `NO_PROXY` earlier. (https://github.com/dell/dellemc-openmanage-ansible-modules/issues/554)
- For idrac_certificates module, the `email_address` has been made as an optional parameter. (https://github.com/dell/dellemc-openmanage-ansible-modules/issues/582).
- Issue is fixed for deploying a new configuration on quick deploy slot when IPv6 is disabled.(https://github.com/dell/dellemc-openmanage-ansible-modules/issues/533)
- idrac_network_attributes - Issue(279049) -  If unsupported values are provided for the parameter ``ome_network_attributes``, then this module does not provide a correct error message.
- ome_device_network_services - Issue(212681) - The module does not provide a proper error message if unsupported values are provided for the following parameters- port_number, community_name, max_sessions, max_auth_retries, and idle_timeout.
- ome_device_power_settings - Issue(212679) - The module displays the following message if the value provided for the parameter ``power_cap`` is not within the supported range of 0 to 32767, ``Unable to complete the request because PowerCap does not exist or is not applicable for the resource URI.``
- ome_inventory - The plugin returns 50 results when a group is specified. No results are shown when a group is not specified. (https://github.com/dell/dellemc-openmanage-ansible-modules/issues/575).
- redfish_storage_volume is enhanced to support iDRAC8.(https://github.com/dell/dellemc-openmanage-ansible-modules/issues/625)

f5networks.f5_modules
~~~~~~~~~~~~~~~~~~~~~

- bigip_gtm_monitor_bigip - fixed an issue where IP and port were not applied correctly when creating new monitor.
- bigip_gtm_monitor_firepass - fixed an issue where IP and port were not applied correctly when creating new monitor.
- bigip_gtm_monitor_http - fixed an issue where IP and port were not applied correctly when creating new monitor.
- bigip_gtm_monitor_https- fixed an issue where IP and port were not applied correctly when creating new monitor.
- bigip_gtm_monitor_tcp - fixed an issue where IP and port were not applied correctly when creating new monitor.
- bigip_gtm_monitor_tcp_half_open - fixed an issue where IP and port were not applied correctly when creating new monitor.
- bigip_gtm_topology_region - fixed an issue where if multiple states with spaces in values were defined, module would throw invalid command error
- bigip_gtm_topology_region - fixed an issue where states names that contained spaces caused the idempotency to break.
- bigip_ssl_key_cert - fixed an issue where the passphrase was not being properly send to the BIG-IP.

fortinet.fortimanager
~~~~~~~~~~~~~~~~~~~~~

- Added missing enum values for some arguments.
- Change minimum required ansible-core version to 2.14.0
- Changed revision to v_range to reduce the size of the code.
- Fixed a bug where ansible may skip update incorrectly.
- Fixed the behavior of module fmgr_firewall_internetservicecustom.
- Fixed the behavior of some modules that contain the argument policyid.
- Improved bypass_validation. If you now set bypass_validation to true, it will allow you to send parameters that are not defined in the schema.
- Improved documentation, added description for all "no description" modules.
- Improved documentation.
- Improved example ansible playbooks.
- Improved the logic of fmgr_fact, fmgr_clone, fmgr_rename, fmgr_move. Usage remains unchanged.
- Reduced the size of module_arg_spec in each module.
- Removed most of the sanity test ignores.
- Support FortiManager 7.0.10
- Supported "state:absent" for all modules end with "_objectmember", "_scopemember", and "_scetionvalue".
- Supported FortiManager 6.4.14, 7.0.11, 7.0.12, 7.2.5.

fortinet.fortios
~~~~~~~~~~~~~~~~

- Fix the issue that ssl-certificate cannot be set in `fortios_firewall_vip` and `fortios_firewall_vip6`.
- Github issue
- mantis issue

hetzner.hcloud
~~~~~~~~~~~~~~

- hcloud inventory - Ensure the API client use a new cache for every *cached session*.
- inventory - Ensure inventory host variables are serializable and can be cached.
- load_balancer_info - Correctly return the `cookie_lifetime` value.
- load_balancer_service - Correctly return the `cookie_lifetime` value.
- primary_ip - Added the missing `auto_delete` field to the return values.
- primary_ip - The `auto_delete` option is now used when creating or updating a Primary IP.
- primary_ip_info - Added the missing `auto_delete` field to the return values.
- server - Do not remove the server from its placement group when the `placement_group` argument is not specified.
- server - Pass an empty string to the `placement_group` argument to remove a server from its placement group.
- server_network - The returned `alias_ips` list is now sorted.

ibm.qradar
~~~~~~~~~~

- A bunch of ansible-lint and ansible-test sanity issues have been fixed.

ibm.storage_virtualize
~~~~~~~~~~~~~~~~~~~~~~

- ibm_svc_info - Command and release mapping to remove errors in gather_subset=all
- ibm_svc_info - Return error in listing entities that require object name

infoblox.nios_modules
~~~~~~~~~~~~~~~~~~~~~

- Fixes environment variable max_results using INFOBLOX_MAX_RESULTS `#209 <https://github.com/infobloxopen/infoblox-ansible/pull/209>`_
- Fixes index error for transform fields in DTC LBDN (auth_zone and Pool) and DTC POOL (servers and monitors). `#209 <https://github.com/infobloxopen/infoblox-ansible/pull/209>`_
- Fixes typo for environment variable INFOBLOX_WAPI_VERSION `#209 <https://github.com/infobloxopen/infoblox-ansible/pull/209>`_

junipernetworks.junos
~~~~~~~~~~~~~~~~~~~~~

- Fix the empty facts list placement
- Prevents module_defaults from were being incorrectly applied to the platform action, instead of the concerned module.
- acls
- fix to gather l2_interfaces facts with default port-mode access.
- initialize facts dictionary with empty containers for respective resources mentioned below
- lldp_global
- lldp_interfaces
- logging_global
- ntp_global
- ospf_interfaces
- ospfv2
- ospfv3
- prefix_lists
- routing_instances
- routing_options
- security_policies
- security_policies_global
- security_zones
- snmp_server
- static_routes
- vlans

kubernetes.core
~~~~~~~~~~~~~~~

- Resolve Collections util resource discovery fails when complex subresources present (https://github.com/ansible-collections/kubernetes.core/pull/676).
- align `helmdiff_check()` function commandline rendering with the `deploy()` function (https://github.com/ansible-collections/kubernetes.core/pull/670).
- helm - Put the chart_ref into quotes when running ``helm show chart``, ``helm upgrade`` and ``helm dependency update`` commands (https://github.com/ansible-collections/kubernetes.core/issues/653).
- helm - delete temporary file created when deploying chart with option ``release_values`` set (https://github.com/ansible-collections/kubernetes.core/issues/530).
- helm - expand kubeconfig path with user's home directory for consistency with k8s
- helm - fix issue occurring when uninstalling chart with statues others than ``deployed`` (https://github.com/ansible-collections/kubernetes.core/issues/319).
- helm - fix post_renderer argument breaking the helm deploy_command (https://github.com/ansible-collections/kubernetes.core/pull/586).
- helm - use ``reuse-values`` when running ``helm diff`` command (https://github.com/ansible-collections/kubernetes.core/issues/680).
- helm - use post_renderer when checking ``changed`` status for a helm release (https://github.com/ansible-collections/kubernetes.core/pull/588).
- integrations test helm_kubeconfig - set helm version to v3.10.3 to avoid incompatability with new bitnami charts (https://github.com/ansible-collections/kubernetes.core/pull/670).
- k8s_json_patch - rename action symlink to ensure k8s action plugin is used (https://github.com/ansible-collections/kubernetes.core/pull/652).
- k8s_scale - clean handling of ResourceTimeout exception (https://github.com/ansible-collections/kubernetes.core/issues/583).
- k8s_scale - fix issue when scaling StatefulSets with ``updateStrategy=OnDelete`` (https://github.com/ansible-collections/kubernetes.core/issues/579).

lowlydba.sqlserver
~~~~~~~~~~~~~~~~~~

- Add ActiveStartDate to the compare properties so this item is marked accurately as changed.
- Fixed the formatting of the SPN by updating the backslash to a forward-slash for the $spn var (lowlydba.sqlserver.spn)
- Update documentation for agent_job_schedule to reflect proper input formatting. (https://github.com/lowlydba/lowlydba.sqlserver/pull/229)

microsoft.ad
~~~~~~~~~~~~

- debug_ldap_client - handle failures when attempting to get the krb5 context and default CCache rather than fail with a traceback
- microsoft.ad.group - Support membership lookup of groups that are longer than 20 characters long
- microsoft.ad.membership - Add helpful hint when the failure was due to a missing/invalid ``domain_ou_path`` - https://github.com/ansible-collections/microsoft.ad/issues/88

netapp.ontap
~~~~~~~~~~~~

- na_ontap_dns - fix issue with modifying DNS servers in REST.
- na_ontap_ems_destination - fix field error with `certificate.name` for ONTAP 9.11.1 or later in REST.
- na_ontap_fpolicy_policy - fixed issue with idempotency in REST.
- na_ontap_igroup_initiator - fixed issue with idempotency.
- na_ontap_nfs - fix error with `windows` in REST for ONTAP 9.10 or earlier.
- na_ontap_quotas - fixed issue with idempotency in REST.
- na_ontap_security_certificates - fix error with ontap_info returned in module output in REST.
- na_ontap_security_config - added warning for missing `supported_cipher_suites` to maintain idempotency in REST.
- na_ontap_snapshot_policy - fix issue with modifying snapshot policy in REST.
- na_ontap_volume - modified `type` to be case insensitive in REST.
- na_ontap_vserver_peer - fix issue with peering multiple clusters with same vserver name in REST.

netapp.storagegrid
~~~~~~~~~~~~~~~~~~

- Removed fetch limit in API request and implemented pagination.

netbox.netbox
~~~~~~~~~~~~~

- Improve error reporting for missing module [#1126](https://github.com/netbox-community/ansible_modules/pull/1126)
- nb_inventory - Fix API cache failure [#1111](https://github.com/netbox-community/ansible_modules/pull/1111)
- nb_lookup - Allow multiple IDs in nb_lookup [#1042](https://github.com/netbox-community/ansible_modules/pull/1042)
- netbox_vlan - Fix documentation of vlan_group [#1138](https://github.com/netbox-community/ansible_modules/pull/1138)

purestorage.flasharray
~~~~~~~~~~~~~~~~~~~~~~

- purefa_cert - Fixed issue where parts of the subject where not included in the CSR if they did not exist in the currently used cert.
- purefa_certs - Allow certificates of over 3000 characters to be imported.
- purefa_dns - Fixed attribute error on deletion of management DNS
- purefa_ds - Fix issue with SDK returning empty data for data directory services even when it does exist
- purefa_host - Allows all current host inititators to be correctly removed
- purefa_host - Fix idempotency issue with connected volume
- purefa_info - Resolved issue with KeyError when LACP bonds are in use
- purefa_inventory - Fix issue with iSCSI-only FlashArrays
- purefa_pg - Allows a protection group to be correctly created when `target` is specified as well as other objects, such as `volumes` or `hosts`
- purefa_pgsched - Fixed issue with disabling schedules
- purefa_pgsnap - Add support for restoring volumes connected to hosts in a host-based protection group and hosts in a hostgroup-based protection group.
- purefa_pgsnap - Fixed incorrect parameter name
- purefa_policy - Fix incorrect call of psot instead of patch for NFS policies
- purefa_volume - Ensure module response for creation of volume and rerun are the same
- purefa_volume - Fix idempotency issue with delete volume

purestorage.flashblade
~~~~~~~~~~~~~~~~~~~~~~

- purefb_bucket - Changed logic to allow complex buckets to be created in a single call, rather than having to split into two tasks.
- purefb_info - Added missing object lock retention details if enabledd
- purefb_lag - Enable LAG port configuration with multi-chassis
- purefb_timeout - Fixed arithmetic error that resulted in module incorrectly reporting changed when no change was required.

splunk.es
~~~~~~~~~

- Fixed argspec validation for plugins with empty task attributes when run with Ansible 2.9.

telekom_mms.icinga_director
~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Fixes #190 - Workaround for service apply bug (https://github.com/telekom-mms/ansible-collection-icinga-director/pull/239)
- change notification interval variable to int-type (https://github.com/telekom-mms/ansible-collection-icinga-director/pull/254)
- set user_groups in notification to empty list (https://github.com/telekom-mms/ansible-collection-icinga-director/pull/255)

theforeman.foreman
~~~~~~~~~~~~~~~~~~

- compute_profile, host - refer to VMware storage pods by name, not id (https://github.com/theforeman/foreman-ansible-modules/issues/1247)
- content_view_filter_rule - handle multiple rules for the same package but different architectures and versions correctly (https://bugzilla.redhat.com/show_bug.cgi?id=2189687)

vmware.vmware_rest
~~~~~~~~~~~~~~~~~~

- content_library_item_info - fixed error with unsupported property
- lookup plugins - Refactor to use native options configuration via doc_fragment, which ensures that vcenter_validate_certs=false is honored (https://github.com/ansible-collections/vmware.vmware_rest/issues/425).

vultr.cloud
~~~~~~~~~~~

- Fixed an error while waiting for a specific state and the API returns an empty response. (https://github.com/vultr/ansible-collection-vultr/issues/108).
- Fixed an issue with waiting for state (https://github.com/vultr/ansible-collection-vultr/pull/102).
- instance - Fixed an issue detecting the instance state returned by the API (https://github.com/vultr/ansible-collection-vultr/pull/89).
- instance_info - Fixed the alias ``name`` being was used on the wrong argument. (https://github.com/vultr/ansible-collection-vultr/issues/105).
- reserved_ip - Fixed an issue which caused the module to fail, also enabled integration tests (https://github.com/vultr/ansible-collection-vultr/issues/92).

Known Issues
------------

community.docker
~~~~~~~~~~~~~~~~

- Please note that the fix for requests 2.32.0 included in community.docker 3.10.1 only
  fixes problems with the *vendored* Docker SDK for Python code. Modules and plugins that
  use Docker SDK for Python can still fail due to the SDK currently being incompatible
  with requests 2.32.0.

  If you still experience problems with requests 2.32.0, such as error messages like
  ``Not supported URL scheme http+docker``, please restrict requests to ``<2.32.0``.

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- idrac_diagnostics - Issue(285322) - This module doesn't support export of diagnostics file to HTTP and HTTPS share via SOCKS proxy.
- idrac_firmware - Issue(279282) - This module does not support firmware update using HTTP, HTTPS, and FTP shares with authentication on iDRAC8.
- idrac_network_attributes - Issue(279049) -  If unsupported values are provided for the parameter ``ome_network_attributes``, then this module does not provide a correct error message.
- idrac_storage_volume - Issue(290766) - The module will report success instead of showing failure for new virtual creation on the BOSS-N1 controller if a virtual disk is already present on the same controller.
- ome_device_network_services - Issue(212681) - The module does not provide a proper error message if unsupported values are provided for the following parameters- port_number, community_name, max_sessions, max_auth_retries, and idle_timeout.
- ome_device_power_settings - Issue(212679) - The module displays the following message if the value provided for the parameter ``power_cap`` is not within the supported range of 0 to 32767, ``Unable to complete the request because PowerCap does not exist or is not applicable for the resource URI.``
- ome_device_quick_deploy - Issue(275231) - This module does not deploy a new configuration to a slot that has disabled IPv6.
- ome_diagnostics - Issue(279193) - Export of SupportAssist collection logs to the share location fails on OME version 4.0.0.
- ome_smart_fabric_uplink - Issue(186024) - The module supported by OpenManage Enterprise Modular, however it does not allow the creation of multiple uplinks of the same name. If an uplink is created using the same name as an existing uplink, then the existing uplink is modified.

New Plugins
-----------

Become
~~~~~~

- community.general.run0 - Systemd's run0.

Callback
~~~~~~~~

- community.general.default_without_diff - The default ansible callback without diff output.
- community.general.timestamp - Adds simple timestamp for each header.

Connection
~~~~~~~~~~

- community.general.incus - Run tasks in Incus instances via the Incus CLI.

Filter
~~~~~~

- ansible.utils.fact_diff - Find the difference between currently set facts
- community.crypto.parse_serial - Convert a serial number as a colon-separated list of hex numbers to an integer
- community.crypto.to_serial - Convert an integer to a colon-separated list of hex numbers
- community.dns.quote_txt - Quotes a string to use as a TXT record entry
- community.dns.unquote_txt - Unquotes a TXT record entry to a string
- community.general.from_ini - Converts INI text input into a dictionary.
- community.general.lists_difference - Difference of lists with a predictive order.
- community.general.lists_intersect - Intersection of lists with a predictive order.
- community.general.lists_symmetric_difference - Symmetric Difference of lists with a predictive order.
- community.general.lists_union - Union of lists with a predictive order.
- community.general.to_ini - Converts a dictionary to the INI file format.
- microsoft.ad.dn_escape - Escape an LDAP DistinguishedName value string.
- microsoft.ad.parse_dn - Parses an LDAP DistinguishedName string into an object.

Lookup
~~~~~~

- community.general.github_app_access_token - Obtain short-lived Github App Access tokens.
- community.general.onepassword_doc - Fetch documents stored in 1Password.

Test
~~~~

- community.general.fqdn_valid - Validates fully-qualified domain names against RFC 1123.

New Modules
-----------

amazon.aws
~~~~~~~~~~

- amazon.aws.rds_cluster_param_group - Manage RDS cluster parameter groups
- amazon.aws.rds_cluster_param_group_info - Describes the properties of specific RDS cluster parameter group.
- amazon.aws.rds_engine_versions_info - Describes the properties of specific versions of DB engines.

ansible.netcommon
~~~~~~~~~~~~~~~~~

- ansible.netcommon.cli_restore - Restore device configuration to network devices over network_cli

check_point.mgmt
~~~~~~~~~~~~~~~~

- check_point.mgmt.cp_mgmt_add_central_license - Add central license.
- check_point.mgmt.cp_mgmt_central_license_facts - Get central-license objects facts on Checkpoint over Web Services API.
- check_point.mgmt.cp_mgmt_delete_central_license - Delete central license.
- check_point.mgmt.cp_mgmt_distribute_cloud_licenses - Distribute licenses to target CloudGuard gateways.
- check_point.mgmt.cp_mgmt_show_cloud_licenses_usage - Show attached licenses usage.
- check_point.mgmt.cp_mgmt_show_ha_status - Retrieve domain high availability status.

cisco.ios
~~~~~~~~~

- cisco.ios.ios_evpn_evi - Resource module to configure L2VPN EVPN EVI.
- cisco.ios.ios_evpn_global - Resource module to configure L2VPN EVPN.
- cisco.ios.ios_vxlan_vtep - Resource module to configure VXLAN VTEP interface.

community.aws
~~~~~~~~~~~~~

- community.aws.dynamodb_table_info - Returns information about a Dynamo DB table

community.crypto
~~~~~~~~~~~~~~~~

- community.crypto.acme_ari_info - Retrieves ACME Renewal Information (ARI) for a certificate.
- community.crypto.acme_certificate_deactivate_authz - Deactivate all authz for an ACME v2 order.
- community.crypto.acme_certificate_renewal_info - Determine whether a certificate should be renewed or not.
- community.crypto.x509_certificate_convert - Convert X.509 certificates

community.digitalocean
~~~~~~~~~~~~~~~~~~~~~~

- community.digitalocean.digital_ocean_project_resource_info - Gather information about DigitalOcean Project Resources

community.docker
~~~~~~~~~~~~~~~~

- community.docker.docker_compose_v2 - Manage multi-container Docker applications with Docker Compose CLI plugin
- community.docker.docker_compose_v2_pull - Pull a Docker compose project
- community.docker.docker_image_build - Build Docker images using Docker buildx
- community.docker.docker_image_export - Export (archive) Docker images
- community.docker.docker_image_pull - Pull Docker images from registries
- community.docker.docker_image_push - Push Docker images to registries
- community.docker.docker_image_remove - Remove Docker images
- community.docker.docker_image_tag - Tag Docker images with new names and/or tags

community.general
~~~~~~~~~~~~~~~~~

- community.general.consul_acl_bootstrap - Bootstrap ACLs in Consul.
- community.general.consul_auth_method - Manipulate Consul auth methods.
- community.general.consul_binding_rule - Manipulate Consul binding rules.
- community.general.consul_token - Manipulate Consul tokens.
- community.general.django_command - Run Django admin commands.
- community.general.dnf_config_manager - Enable or disable dnf repositories using config-manager.
- community.general.git_config_info - Read git configuration.
- community.general.gitlab_group_access_token - Manages GitLab group access tokens.
- community.general.gitlab_issue - Create, update, or delete GitLab issues.
- community.general.gitlab_label - Creates/updates/deletes GitLab Labels belonging to project or group.
- community.general.gitlab_milestone - Creates/updates/deletes GitLab Milestones belonging to project or group.
- community.general.gitlab_project_access_token - Manages GitLab project access tokens.
- community.general.keycloak_client_rolescope - Allows administration of Keycloak client roles scope to restrict the usage of certain roles to a other specific client applications.
- community.general.keycloak_component_info - Retrive component info in Keycloak.
- community.general.keycloak_realm_rolemapping - Allows administration of Keycloak realm role mappings into groups with the Keycloak API.
- community.general.nomad_token - Manage Nomad ACL tokens.
- community.general.proxmox_node_info - Retrieve information about one or more Proxmox VE nodes.
- community.general.proxmox_storage_contents_info - List content from a Proxmox VE storage.
- community.general.usb_facts - Allows listing information about USB devices.

community.hashi_vault
~~~~~~~~~~~~~~~~~~~~~

- community.hashi_vault.vault_database_connection_configure - Configures the database engine
- community.hashi_vault.vault_database_connection_delete - Delete a Database Connection
- community.hashi_vault.vault_database_connection_read - Returns the configuration settings for a O(connection_name)
- community.hashi_vault.vault_database_connection_reset - Closes a O(connection_name) and its underlying plugin and restarts it with the configuration stored
- community.hashi_vault.vault_database_connections_list - Returns a list of available connections
- community.hashi_vault.vault_database_role_create - Creates or updates a (dynamic) role definition
- community.hashi_vault.vault_database_role_delete - Delete a role definition
- community.hashi_vault.vault_database_role_read - Queries a dynamic role definition
- community.hashi_vault.vault_database_roles_list - Returns a list of available (dynamic) roles
- community.hashi_vault.vault_database_rotate_root_credentials - Rotates the root credentials stored for the database connection. This user must have permissions to update its own password.
- community.hashi_vault.vault_database_static_role_create - Create or update a static role
- community.hashi_vault.vault_database_static_role_get_credentials - Returns the current credentials based on the named static role
- community.hashi_vault.vault_database_static_role_read - Queries a static role definition
- community.hashi_vault.vault_database_static_role_rotate_credentials - Trigger the credential rotation for a static role
- community.hashi_vault.vault_database_static_roles_list - Returns a list of available static roles

community.zabbix
~~~~~~~~~~~~~~~~

- community.zabbix.zabbix_correlation - Create/update/delete Zabbix correlation

containers.podman
~~~~~~~~~~~~~~~~~

- containers.podman.podman_secret_info - Secrets info module

dellemc.enterprise_sonic
~~~~~~~~~~~~~~~~~~~~~~~~

- dellemc.enterprise_sonic.sonic_dhcp_snooping - Manage DHCP Snooping on SONiC
- dellemc.enterprise_sonic.sonic_pki - Manages PKI attributes of Enterprise Sonic
- dellemc.enterprise_sonic.sonic_stp - Manage STP configuration on SONiC

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- dellemc.openmanage.idrac_diagnostics - This module allows to run and export diagnostics on iDRAC.
- dellemc.openmanage.idrac_license - This module allows to import, export, and delete licenses on iDRAC.
- dellemc.openmanage.idrac_session - Allows you to create and delete the sessions on iDRAC.
- dellemc.openmanage.idrac_storage_volume - Configures the RAID configuration attributes.

dellemc.powerflex
~~~~~~~~~~~~~~~~~

- dellemc.powerflex.fault_set - Manage Fault Sets on Dell PowerFlex
- dellemc.powerflex.resource_group - Manage resource group deployments on Dell PowerFlex

fortinet.fortimanager
~~~~~~~~~~~~~~~~~~~~~

- fortinet.fortimanager.fmgr_diameterfilter_profile - Configure Diameter filter profiles.
- fortinet.fortimanager.fmgr_firewall_accessproxysshclientcert - Configure Access Proxy SSH client certificate.
- fortinet.fortimanager.fmgr_firewall_accessproxysshclientcert_certextension - Configure certificate extension for user certificate.
- fortinet.fortimanager.fmgr_firewall_vip6_quic - QUIC setting.
- fortinet.fortimanager.fmgr_firewall_vip_gslbpublicips - Publicly accessible IP addresses for the FortiGSLB service.
- fortinet.fortimanager.fmgr_sctpfilter_profile - Configure SCTP filter profiles.
- fortinet.fortimanager.fmgr_sctpfilter_profile_ppidfilters - PPID filters list.
- fortinet.fortimanager.fmgr_switchcontroller_managedswitch_vlan - Configure VLAN assignment priority.
- fortinet.fortimanager.fmgr_system_admin_profile_writepasswdprofiles - Profile list.
- fortinet.fortimanager.fmgr_system_admin_profile_writepasswduserlist - User list.
- fortinet.fortimanager.fmgr_system_npu_nputcam - Configure NPU TCAM policies.
- fortinet.fortimanager.fmgr_system_npu_nputcam_data - Data fields of TCAM.
- fortinet.fortimanager.fmgr_system_npu_nputcam_mask - Mask fields of TCAM.
- fortinet.fortimanager.fmgr_system_npu_nputcam_miract - Mirror action of TCAM.
- fortinet.fortimanager.fmgr_system_npu_nputcam_priact - Priority action of TCAM.
- fortinet.fortimanager.fmgr_system_npu_nputcam_sact - Source action of TCAM.
- fortinet.fortimanager.fmgr_system_npu_nputcam_tact - Target action of TCAM.
- fortinet.fortimanager.fmgr_videofilter_keyword - Configure video filter keywords.
- fortinet.fortimanager.fmgr_videofilter_keyword_word - List of keywords.
- fortinet.fortimanager.fmgr_videofilter_profile_filters - YouTube filter entries.
- fortinet.fortimanager.fmgr_videofilter_youtubekey - Configure YouTube API keys.

hetzner.hcloud
~~~~~~~~~~~~~~

- hetzner.hcloud.firewall_resource - Manage Resources a Hetzner Cloud Firewall is applied to.

infoblox.nios_modules
~~~~~~~~~~~~~~~~~~~~~

- infoblox.nios_modules.nios_dtc_monitor_http - Configures the Infoblox NIOS DTC HTTP monitor.
- infoblox.nios_modules.nios_dtc_monitor_icmp - Configures the Infoblox NIOS DTC ICMP monitor
- infoblox.nios_modules.nios_dtc_monitor_pdp - Configures the Infoblox NIOS DTC PDP monitor
- infoblox.nios_modules.nios_dtc_monitor_sip - Configures the Infoblox NIOS DTC SIP monitor
- infoblox.nios_modules.nios_dtc_monitor_snmp - Configures the Infoblox NIOS DTC SNMP monitor
- infoblox.nios_modules.nios_dtc_monitor_tcp - Configures the Infoblox NIOS DTC TCP monitor
- infoblox.nios_modules.nios_dtc_topology - Configures the Infoblox NIOS DTC Topology

netapp.ontap
~~~~~~~~~~~~

- netapp.ontap.na_ontap_cifs_unix_symlink_mapping - NetApp ONTAP module to manage UNIX symbolic link mapping for CIFS clients.
- netapp.ontap.na_ontap_cli_timeout - NetApp ONTAP module to set the CLI inactivity timeout value.
- netapp.ontap.na_ontap_snmp_config - NetApp ONTAP module to modify SNMP configuration.

netbox.netbox
~~~~~~~~~~~~~

- netbox.netbox.netbox_custom_field_choice_set - Create, updates, or removes Custom Field Choice sets
- netbox.netbox.netbox_module_bay - Create, updates, or removes Module Bay
- netbox.netbox.netbox_virtual_disk - Create, updates, or removes a disk from a Virtual Machine

purestorage.flasharray
~~~~~~~~~~~~~~~~~~~~~~

- purestorage.flasharray.purefa_hardware - Manage FlashArray Hardware Identification

purestorage.flashblade
~~~~~~~~~~~~~~~~~~~~~~

- purestorage.flashblade.purefb_hardware - Manage FlashBlade Hardware

theforeman.foreman
~~~~~~~~~~~~~~~~~~

- theforeman.foreman.registration_command - Manage Registration Command
- theforeman.foreman.webhook - Manage Webhooks

vultr.cloud
~~~~~~~~~~~

- vultr.cloud.object_storage - Manages object storages on Vultr

New Roles
---------

- dellemc.openmanage.idrac_user - Role to manage local users of iDRAC.

Unchanged Collections
---------------------

- ansible.posix (still version 1.5.4)
- chocolatey.chocolatey (still version 1.5.1)
- cisco.ucs (still version 1.10.0)
- cloudscale_ch.cloud (still version 2.3.1)
- community.libvirt (still version 1.3.0)
- community.network (still version 5.0.2)
- community.proxysql (still version 1.5.1)
- community.sops (still version 1.6.7)
- cyberark.conjur (still version 1.2.2)
- frr.frr (still version 2.0.2)
- ibm.spectrum_virtualize (still version 2.0.0)
- inspur.sm (still version 2.3.0)
- netapp.cloudmanager (still version 21.22.1)
- netapp_eseries.santricity (still version 1.4.0)
- ngine_io.cloudstack (still version 2.3.0)
- ngine_io.exoscale (still version 1.1.0)
- openvswitch.openvswitch (still version 2.1.1)
- ovirt.ovirt (still version 3.2.0)
- sensu.sensu_go (still version 1.14.0)
- t_systems_mms.icinga_director (still version 2.0.1)
- vyos.vyos (still version 4.1.0)
- wti.remote (still version 1.0.5)
