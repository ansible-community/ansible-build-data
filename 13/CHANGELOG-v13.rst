========================
Ansible 13 Release Notes
========================

This changelog describes changes since Ansible 12.0.0.

.. contents::
  :depth: 2

v13.0.0a4
=========

.. contents::
  :local:
  :depth: 2

Release Summary
---------------

Release Date: 2025-10-21

`Porting Guide <https://docs.ansible.com/ansible/devel/porting_guides.html>`_

Ansible-core
------------

Ansible 13.0.0a4 contains ansible-core version 2.20.0rc2.
This is a newer version than version 2.20.0rc1 contained in the previous Ansible release.

The changes are reported in the combined changelog below.

Changed Collections
-------------------

If not mentioned explicitly, the changes are reported in the combined changelog below.

+-----------------+------------------+------------------+------------------------------------------------------------------------------------------------------------------------------+
| Collection      | Ansible 13.0.0a3 | Ansible 13.0.0a4 | Notes                                                                                                                        |
+=================+==================+==================+==============================================================================================================================+
| community.mysql | 4.0.0            | 4.0.1            |                                                                                                                              |
+-----------------+------------------+------------------+------------------------------------------------------------------------------------------------------------------------------+
| cyberark.pas    | 1.0.35           | 1.0.36           | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+-----------------+------------------+------------------+------------------------------------------------------------------------------------------------------------------------------+

Bugfixes
--------

Ansible-core
~~~~~~~~~~~~

- psrp - ReadTimeout exceptions now mark host as unreachable instead of fatal (https://github.com/ansible/ansible/issues/85966)

community.mysql
~~~~~~~~~~~~~~~

- mysql_info - Fix slave status for source terminology introduced in MySQL 8.0.23 (https://github.com/ansible-collections/community.mysql/issues/682).
- mysql_user, mysql_role - fix not existent grant when revoking perms on user/role which do not have any other perms than grant option (https://github.com/ansible-collections/community.mysql/issues/664).

Unchanged Collections
---------------------

- amazon.aws (still version 10.1.2)
- ansible.netcommon (still version 8.1.0)
- ansible.posix (still version 2.1.0)
- ansible.utils (still version 6.0.0)
- ansible.windows (still version 3.2.0)
- arista.eos (still version 12.0.0)
- awx.awx (still version 24.6.1)
- azure.azcollection (still version 3.9.0)
- check_point.mgmt (still version 6.5.0)
- chocolatey.chocolatey (still version 1.5.3)
- cisco.aci (still version 2.12.0)
- cisco.dnac (still version 6.40.0)
- cisco.intersight (still version 2.6.0)
- cisco.ios (still version 11.1.1)
- cisco.iosxr (still version 12.0.0)
- cisco.meraki (still version 2.21.8)
- cisco.mso (still version 2.11.0)
- cisco.nxos (still version 11.0.0)
- cisco.ucs (still version 1.16.0)
- cloudscale_ch.cloud (still version 2.5.2)
- community.aws (still version 10.0.0)
- community.ciscosmb (still version 1.0.11)
- community.crypto (still version 3.0.4)
- community.digitalocean (still version 1.27.0)
- community.dns (still version 3.3.4)
- community.docker (still version 4.8.1)
- community.general (still version 11.4.0)
- community.grafana (still version 2.3.0)
- community.hashi_vault (still version 7.0.0)
- community.hrobot (still version 2.6.1)
- community.library_inventory_filtering_v1 (still version 1.1.4)
- community.libvirt (still version 2.0.0)
- community.mongodb (still version 1.7.10)
- community.okd (still version 5.0.0)
- community.postgresql (still version 4.1.0)
- community.proxmox (still version 1.3.0)
- community.proxysql (still version 1.7.0)
- community.rabbitmq (still version 1.6.0)
- community.routeros (still version 3.12.1)
- community.sap_libs (still version 1.5.0)
- community.sops (still version 2.2.4)
- community.vmware (still version 6.0.0)
- community.windows (still version 3.0.1)
- community.zabbix (still version 4.1.1)
- containers.podman (still version 1.18.0)
- cyberark.conjur (still version 1.3.8)
- dellemc.enterprise_sonic (still version 3.2.0)
- dellemc.openmanage (still version 10.0.1)
- dellemc.powerflex (still version 3.0.0)
- dellemc.unity (still version 2.1.0)
- f5networks.f5_modules (still version 1.39.0)
- fortinet.fortimanager (still version 2.11.0)
- fortinet.fortios (still version 2.4.1)
- google.cloud (still version 1.9.0)
- grafana.grafana (still version 6.0.5)
- hetzner.hcloud (still version 5.4.0)
- hitachivantara.vspone_block (still version 4.3.0)
- hitachivantara.vspone_object (still version 1.0.0)
- ibm.storage_virtualize (still version 3.1.0)
- ieisystem.inmanage (still version 3.0.0)
- infinidat.infinibox (still version 1.6.3)
- infoblox.nios_modules (still version 1.8.0)
- inspur.ispim (still version 2.2.3)
- junipernetworks.junos (still version 11.0.0)
- kaytus.ksmanage (still version 2.0.0)
- kubernetes.core (still version 6.2.0)
- kubevirt.core (still version 2.2.3)
- lowlydba.sqlserver (still version 2.7.0)
- microsoft.ad (still version 1.9.2)
- microsoft.iis (still version 1.0.3)
- netapp.cloudmanager (still version 21.24.0)
- netapp.ontap (still version 23.1.0)
- netapp.storagegrid (still version 21.15.0)
- netapp_eseries.santricity (still version 1.4.1)
- netbox.netbox (still version 3.21.0)
- ngine_io.cloudstack (still version 2.5.0)
- openstack.cloud (still version 2.4.1)
- ovirt.ovirt (still version 3.2.1)
- purestorage.flasharray (still version 1.39.0)
- purestorage.flashblade (still version 1.22.0)
- ravendb.ravendb (still version 1.0.3)
- splunk.es (still version 4.0.0)
- telekom_mms.icinga_director (still version 2.4.0)
- theforeman.foreman (still version 5.7.0)
- vmware.vmware (still version 2.4.0)
- vmware.vmware_rest (still version 4.9.0)
- vultr.cloud (still version 1.13.0)
- vyos.vyos (still version 6.0.0)
- wti.remote (still version 1.0.10)

v13.0.0a3
=========

.. contents::
  :local:
  :depth: 2

Release Summary
---------------

Release Date: 2025-10-15

`Porting Guide <https://docs.ansible.com/ansible/devel/porting_guides.html>`_

Ansible-core
------------

Ansible 13.0.0a3 contains ansible-core version 2.20.0rc1.
This is a newer version than version 2.20.0b2 contained in the previous Ansible release.

The changes are reported in the combined changelog below.

Changed Collections
-------------------

If not mentioned explicitly, the changes are reported in the combined changelog below.

+-----------------------------+------------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Collection                  | Ansible 13.0.0a2 | Ansible 13.0.0a3 | Notes                                                                                                                                                                                                           |
+=============================+==================+==================+=================================================================================================================================================================================================================+
| cisco.ios                   | 11.1.0           | 11.1.1           |                                                                                                                                                                                                                 |
+-----------------------------+------------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.hrobot            | 2.5.2            | 2.6.1            |                                                                                                                                                                                                                 |
+-----------------------------+------------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.proxysql          | 1.6.0            | 1.7.0            |                                                                                                                                                                                                                 |
+-----------------------------+------------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cyberark.conjur             | 1.3.7            | 1.3.8            | You can find the collection's changelog at `https://github.com/cyberark/ansible-conjur-collection/blob/master/CHANGELOG.md <https://github.com/cyberark/ansible-conjur-collection/blob/master/CHANGELOG.md>`__. |
+-----------------------------+------------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| dellemc.enterprise_sonic    | 3.0.0            | 3.2.0            |                                                                                                                                                                                                                 |
+-----------------------------+------------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| grafana.grafana             | 6.0.4            | 6.0.5            |                                                                                                                                                                                                                 |
+-----------------------------+------------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| hitachivantara.vspone_block | 4.2.2            | 4.3.0            |                                                                                                                                                                                                                 |
+-----------------------------+------------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ibm.storage_virtualize      | 3.0.0            | 3.1.0            |                                                                                                                                                                                                                 |
+-----------------------------+------------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| kubernetes.core             | 6.1.0            | 6.2.0            |                                                                                                                                                                                                                 |
+-----------------------------+------------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| purestorage.flashblade      | 1.21.2           | 1.22.0           |                                                                                                                                                                                                                 |
+-----------------------------+------------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| theforeman.foreman          | 5.6.0            | 5.7.0            |                                                                                                                                                                                                                 |
+-----------------------------+------------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Major Changes
-------------

grafana.grafana
~~~~~~~~~~~~~~~

- Fallback to empty dict in case grafana_ini is undefined by @root-expert in https://github.com/grafana/grafana-ansible-collection/pull/403
- Fix Mimir config file validation task by @Windos in https://github.com/grafana/grafana-ansible-collection/pull/428
- Fixes issue by @digiserg in https://github.com/grafana/grafana-ansible-collection/pull/421
- Import custom dashboards only when directory exists by @mahendrapaipuri in https://github.com/grafana/grafana-ansible-collection/pull/430
- Updated YUM repo urls from `packages.grafana.com` to `rpm.grafana.com` by @DejfCold in https://github.com/grafana/grafana-ansible-collection/pull/414
- Use credentials from grafana_ini when importing dashboards by @root-expert in https://github.com/grafana/grafana-ansible-collection/pull/402
- do not skip scrape latest github version even in check_mode by @cmehat in https://github.com/grafana/grafana-ansible-collection/pull/408
- fix datasource documentation by @jeremad in https://github.com/grafana/grafana-ansible-collection/pull/437
- fix mimir_download_url_deb & mimir_download_url_rpm by @germebl in https://github.com/grafana/grafana-ansible-collection/pull/400
- update catalog info by @Duologic in https://github.com/grafana/grafana-ansible-collection/pull/434
- use deb822 for newer debian versions by @Lukas-Heindl in https://github.com/grafana/grafana-ansible-collection/pull/440

Minor Changes
-------------

Ansible-core
~~~~~~~~~~~~

- ansible-test - Default to Python 3.14 in the ``base`` and ``default`` test containers.
- ansible-test - Filter out pylint messages for invalid filenames and display a notice when doing so.
- ansible-test - Update astroid imports in custom pylint checkers.
- ansible-test - Update pinned ``pip`` version to 25.2.
- ansible-test - Update pinned sanity test requirements, including upgrading to pylint 4.0.0.

community.proxysql
~~~~~~~~~~~~~~~~~~

- proxysql_mysql_users - Creating users with the ``caching_sha2_password`` plugin (https://github.com/ansible-collections/community.proxysql/pull/173).

dellemc.enterprise_sonic
~~~~~~~~~~~~~~~~~~~~~~~~

- bgp_af - Add support for 'dup-addr-detection' commands (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/452).
- sonic_aaa - Add MFA support for AAA module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/532).
- sonic_bgp - Add support for graceful restart attributes (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/538).
- sonic_bgp - Added Ansible support for the bandwidth option (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/557).
- sonic_bgp_neighbors - Add support for discard-extra option for BGP peer-group maximum-prefix(https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/545).
- sonic_bgp_neighbors - Added Ansible support for the extended_link_bandwidth option (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/557).
- sonic_bgp_neighbors - Remove mutual exclusion for peer_group allowas_in options (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/586).
- sonic_bgp_neighbors_af - Add support for discard-extra option for BGP neighbor maximum-prefix(https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/545).
- sonic_bgp_neighbors_af - Remove mutual exclusion for neighbor allowas_in options (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/586).
- sonic_copp - Add 'copp_traps' to CoPP module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/461).
- sonic_interfaces - Add support for configuring speed and advertised speed for 800 GB interfaces (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/590).
- sonic_interfaces - Add support for speed 200GB (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/534).
- sonic_interfaces - Enhancing port-group and interface speed error handling (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/487).
- sonic_l3_interfaces - Add support for ipv6 'anycast_addresses' option (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/491).
- sonic_l3_interfaces - Added support for Proxy-ARP/ND-Proxy feature (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/576).
- sonic_lag_interfaces - Add support for 'fallback', 'fast_rate', 'graceful_shutdown', 'lacp_individual', 'min_links' and 'system_mac' options (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/475).
- sonic_lldp_interfaces - Add playbook check and diff modes support for lldp_interfaces module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/524).
- sonic_lldp_interfaces - Add support for LLDP TLVs i.e., 'port_vlan_id', 'vlan_name', 'link_aggregation', 'max_frame_size', and 'vlan_name_tlv' attributes (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/406).
- sonic_lldp_interfaces - Add support for network policy configuration (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/582).
- sonic_logging - Add support for 'security_profile' option (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/555).
- sonic_logging - Adding the ability to delete a specific attribute of a logging server into the logging module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/486).
- sonic_mclag - Added Ansible support for the yang leafs added as part of the  MCLAG Split Brain Detection and Recovery feature (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/496).
- sonic_port_breakout - Add support for modes 1x800G, 2x400G, 4x200G, and 8x100G (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/585).
- sonic_port_group - Add support for speed 200GB (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/534).
- sonic_qos_interfaces - Add 'cable_length' attribute (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/468).
- sonic_route_maps - Add support for set ARS object (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/581).
- sonic_route_maps - Added Ansible support for bandwidth feature and suboptions bandwidth_value and transitive_value (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/557).
- sonic_sflow - Add max header size support in sonic_sflow module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/419).
- sonic_system - Add concurrent session limit support for sonic_system module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/505).
- sonic_system - Add password complexity support for sonic_system module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/519).
- sonic_system - Add support for Tx/Rx clock frequency adjustment (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/562).
- sonic_system - Add switching-mode functionality to the sonic_system module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/504).
- sonic_users - Add support for user ssh key configuration (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/512).
- sonic_vlans - Add support for autostate attribute configuration on a VLAN (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/533).

hitachivantara.vspone_block
~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Added a new "hv_sds_block_compute_port" module to change the settings and protocol of the compute port on Hitachi SDS Block storage systems.
- Added a new "hv_sds_block_remote_iscsi_port" module to register a remote iSCSI port and delete information about registered remote iSCSI ports on Hitachi SDS Block storage systems.
- Added a new "hv_sds_block_remote_iscsi_port_facts" module to retrieve remote iSCSI ports from Hitachi SDS Block storage systems.
- Added a new "hv_sds_block_software_update_file_facts" module to retrieve information of the update file of the storage software which performed transfer (upload) in the Hitachi SDS Block storage systems.
- Added a new "hv_sds_block_storage_node_bmc_connection" module allows to update the BMC connection settings of Hitachi SDS Block storage systems.
- Added a new "hv_sds_block_storage_software_update" module allows software update and downgrade on Hitachi SDS Block storage systems.
- Added a new "hv_vsp_one_port" module to retrieve volume's information from servers on VSP E series and VSP One B2X storages.
- Added a new "hv_vsp_one_port_facts" module to retrieve port information from VSP E series and VSP One B2X storages.
- Added a new "hv_vsp_one_server" module enables register, modification, and deletion of servers, as well as various server operations on VSP E series and VSP One B2X storages.
- Added a new "hv_vsp_one_server_facts" module to retrieve information about servers from servers on VSP E series and VSP One B2X storages.
- Added a new "hv_vsp_one_server_hba_facts" module to retrieve HBA (Host Bus Adapter) information about servers from servers on VSP E series and VSP One B2X storages.
- Added support for latest software version 1.18.1 for SDS block on AWS, GCP and Bare metal.
- Added support for listing storage node primary role status in the output to hv_sds_block_storage_node_facts module.
- Added support to "Add storage node to the SDS cluster on AWS cloud" to hv_sds_block_cluster module.
- Added support to "Allow CHAP users to access the compute port" to hv_sds_block_compute_port_authentication module
- Added support to "Attach multiple volumes to multiple servers in one operation" to hv_vsp_one_volume module.
- Added support to "Cancel compute port access permission for CHAP users" to hv_sds_block_compute_port_authentication module
- Added support to "Get Drive by ID" to hv_sds_block_drives_facts module
- Added support to "Get Protection Domain Information by ID" to hv_sds_block_protection_domain_facts module
- Added support to "Stop removing storage nodes" to hv_sds_block_cluster module.
- Added support to take ldev input in HEX value in all hitachivantara.vspone_block.vsp modules.
- Updated input parameter name from "saving_setting" to "capacity_saving" in hv_vsp_one_volume module.

ibm.storage_virtualize
~~~~~~~~~~~~~~~~~~~~~~

- ibm_svc_manage_ip - Changes for updating VLAN, gateway and IP address
- ibm_svc_utils - Improved error message for unreachable systems

kubernetes.core
~~~~~~~~~~~~~~~

- Add support of skip-schema-validation in ``helm`` module (https://github.com/ansible-collections/kubernetes.core/pull/995)
- kustomize - Add support of local environ (https://github.com/ansible-collections/kubernetes.core/pull/786).

purestorage.flashblade
~~~~~~~~~~~~~~~~~~~~~~

- module_utils/purefb - Remove `get_blade()` function as not required for REST v2
- purefb_admin - Remove references to unsupported API versions
- purefb_alert - Add new ``state`` of ``test`` to check alert manager configuration
- purefb_alert - Upgraded to REST v2
- purefb_banner - Upgraded to REST v2
- purefb_bladename - Upgraded to REST v2
- purefb_bucket - Added Fusion support
- purefb_bucket - Updated to REST v2
- purefb_bucket_access - Fusion support added
- purefb_bucket_replica - Add Fusion support
- purefb_bucket_replica - Upgraded to REST v2
- purefb_certgrp - Upgraded to REST v2
- purefb_connect - Added Fusion support
- purefb_connect - Remove references to unsupported API versions
- purefb_connect - Upgraded to REST v2
- purefb_ds - Added new state of ``test`` to enable directory services to run diagnostics test
- purefb_ds - Updated to REST v2
- purefb_dsrole - Upgraded to REST v2
- purefb_eula - Converted to REST v2
- purefb_fs - Added support for Fusion
- purefb_fs - Upgraded to use REST 2
- purefb_fs_replica - Upgraded to REST v2
- purefb_groupquota - Fusion support added
- purefb_groupquota - Upgraded to REST v2
- purefb_info - Upgraded to REST v2
- purefb_inventory - Upgraded to REST v2
- purefb_lifecycle - Fusion support added
- purefb_lifecycle - Upgraded to REST v2
- purefb_network - Upgraded to REST v2
- purefb_ntp - Upgraded to REST v2
- purefb_phonehome - Add new ``state`` of ``test`` to check phonehome configuration
- purefb_phonehome - Upgrwded to REST v2
- purefb_pingtrace - Ehanced JSON response for ping
- purefb_policy - Add Fusion support
- purefb_policy - Remove references to unsupported API versions
- purefb_policy - Upgraded to REST v2
- purefb_ra - Add new ``state`` of ``test`` to check remote support configuration
- purefb_remote_cred - Fusion support added
- purefb_remote_cred - Upgraded to REST v2
- purefb_s3acc - Fusion support added
- purefb_s3acc - Remove references to unsupported API versions
- purefb_s3user - Fusion support added
- purefb_snamp_agent - Upgraded to REST v2
- purefb_snap - Fusion support added
- purefb_snap - Upgraded to REST v2
- purefb_snmp_mgr - Add new ``state`` of ``test`` to check SNMP manager configuration
- purefb_snmp_mgr - Upgraded to REST v2
- purefb_subnet - Upgraded to REST v2
- purefb_syslog - Converted to REST v2
- purefb_target - Upgraded to REST v2
- purefb_userpolicy - Fusion support added
- purefb_userquota - Added Fusion support
- purefb_userquota - Upgraded to REST v2
- purefb_virtualhost - Fusion support added

Deprecated Features
-------------------

community.hrobot
~~~~~~~~~~~~~~~~

- storagebox\* modules - membership in the ``community.hrobot.robot`` action group (module defaults group) is deprecated; the modules will be removed from the group in community.hrobot 3.0.0. Use ``community.hrobot.api`` instead (https://github.com/ansible-collections/community.hrobot/pull/178).
- storagebox\* modules - the ``hetzner_token`` option for these modules will be required from community.hrobot 3.0.0 on (https://github.com/ansible-collections/community.hrobot/pull/178).
- storagebox\* modules - the ``hetzner_user`` and ``hetzner_pass`` options for these modules are deprecated; support will be removed in community.hrobot 3.0.0. Use ``hetzner_token`` instead (https://github.com/ansible-collections/community.hrobot/pull/178).
- storagebox_info - the ``storageboxes[].login``, ``storageboxes[].disk_quota``, ``storageboxes[].disk_usage``, ``storageboxes[].disk_usage_data``, ``storageboxes[].disk_usage_snapshot``, ``storageboxes[].webdav``, ``storageboxes[].samba``, ``storageboxes[].ssh``, ``storageboxes[].external_reachability``, and ``storageboxes[].zfs`` return values are deprecated and will be removed from community.routeros. Check out the documentation to find out their new names according to the new API (https://github.com/ansible-collections/community.hrobot/pull/178).
- storagebox_snapshot_info - the ``snapshots[].timestamp``, ``snapshots[].size``, ``snapshots[].filesystem_size``, ``snapshots[].automatic``, and ``snapshots[].comment`` return values are deprecated and will be removed from community.routeros. Check out the documentation to find out their new names according to the new API (https://github.com/ansible-collections/community.hrobot/pull/178).
- storagebox_snapshot_plan - the ``plans[].month`` return value is deprecated, since it only returns ``null`` with the new API and cannot be set to any other value (https://github.com/ansible-collections/community.hrobot/pull/178).
- storagebox_snapshot_plan_info - the ``plans[].month`` return value is deprecated, since it only returns ``null`` with the new API and cannot be set to any other value (https://github.com/ansible-collections/community.hrobot/pull/178).
- storagebox_subaccount - the ``subaccount.homedirectory``, ``subaccount.samba``, ``subaccount.ssh``, ``subaccount.external_reachability``, ``subaccount.webdav``, ``subaccount.readonly``, ``subaccount.createtime``, and ``subaccount.comment`` return values are deprecated and will be removed from community.routeros. Check out the documentation to find out their new names according to the new API (https://github.com/ansible-collections/community.hrobot/pull/178).
- storagebox_subaccount_info - the ``subaccounts[].accountid``, ``subaccounts[].homedirectory``, ``subaccounts[].samba``, ``subaccounts[].ssh``, ``subaccounts[].external_reachability``, ``subaccounts[].webdav``, ``subaccounts[].readonly``, ``subaccounts[].createtime``, and ``subaccounts[].comment`` return values are deprecated and will be removed from community.routeros. Check out the documentation to find out their new names according to the new API (https://github.com/ansible-collections/community.hrobot/pull/178).

Bugfixes
--------

Ansible-core
~~~~~~~~~~~~

- SIGINT/SIGTERM Handling - Make SIGINT/SIGTERM handling more robust by splitting concerns between forks and the parent.

cisco.ios
~~~~~~~~~

- cisco.ios.ios_bgp_address_family - Encrypted strings as password are not evaluated rather treated as string forcefully.
- cisco.ios.ios_hsrp_interfaces - Fixed default values for version and priority.
- cisco.ios.ios_hsrp_interfaces - Fixed overridden state to be idempotent with ipv6 configuration.
- cisco.ios.ios_hsrp_interfaces - Fixed parsers to group HSRP configuration and optimize parsing time.
- cisco.ios.ios_hsrp_interfaces - Fixed removal of HSRP configuration when state is deleted, replaced, overridden.
- cisco.ios.ios_hsrp_interfaces - Fixed rendered output for standby redirect advertisement authentication key-chain.
- cisco.ios.ios_hsrp_interfaces - Fixed rendered output for standby redirect advertisement authentication key-string with encryption.
- cisco.ios.ios_hsrp_interfaces - Fixed rendered output for standby redirect advertisement authentication.
- cisco.ios.ios_hsrp_interfaces - Handle operation of list attributes like ipv6, ip, track.
- cisco.ios.ios_l2_interfaces - Add private-vlan support to switchport.

community.hrobot
~~~~~~~~~~~~~~~~

- Avoid using ``ansible.module_utils.six`` in more places to avoid deprecation warnings with ansible-core 2.20 (https://github.com/ansible-collections/community.hrobot/pull/179).

dellemc.enterprise_sonic
~~~~~~~~~~~~~~~~~~~~~~~~

- sonic-vlan-mapping - Avoid sending a deletion REST API containing a comma-separated list of vlan IDs (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/563).
- sonic_aaa - Update AAA module to account for SONiC code changes (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/495).
- sonic_bgp - Remove CLI regression test cases for BGP (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/566).
- sonic_bgp_nbr - Fix 'auth_pwd' diff calculation bug (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/583).
- sonic_evpn_esi_multihome - Fix EVPN ESI multihome delete all bug (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/578).
- sonic_interfaces - Fix port-group interface error handling for speed configuration (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/575).
- sonic_l2_interfaces - Fix VLAN deletion bug (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/526).
- sonic_l3_interfaces - Fix check mode behavior for ipv4 primary address (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/491).
- sonic_lag_interfaces - Fix 'mode' value not retrieved in facts (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/475).
- sonic_logging - Addressing bug found in https://github.com/ansible-collections/dellemc.enterprise_sonic/issues/508 where a traceback is thrown if the "severity" value is not specified in the incoming playbook or if the incoming playbook specifies a 'severity' value of None. (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/537).
- sonic_mclag - Fix domain ID creation bug (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/591).
- sonic_mirroring - Fix mirroring regression test failures (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/577).
- sonic_ospf_area - Fix OSPF area bug (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/541).
- sonic_qos_buffer - Modify buffer profile handling to match new CVL requirements (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/543).
- sonic_stp - Add handling for removal of empty data structures for merge state (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/511).
- sonic_stp - Fix STP check mode bug (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/518).
- sonic_stp - Update request method to use post for enabled_protocol (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/587).
- sonic_tacacs_server - Add sleep to allow TACACS server config updates to apply to SONiC PAM modules (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/509).
- sonic_vrfs - Fix VRFs bug for overridden state (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/569).
- sonic_vxlans - Fix evpn_nvo request bug (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/589).

ibm.storage_virtualize
~~~~~~~~~~~~~~~~~~~~~~

- ibm_svc_manage_ip - Fixed issues with IP address probe
- ibm_svc_manage_volume - Fixed data-type conversion issue for grainsize
- ibm_svc_start_stop_flashcopy - Fixed flashcopy start issues when mapping belonged to flashcopy consistency group

kubernetes.core
~~~~~~~~~~~~~~~

- Remove ``ansible.module_utils.six`` imports to avoid warnings (https://github.com/ansible-collections/kubernetes.core/pull/998).
- Update the `k8s_cp` module to also work for init containers (https://github.com/ansible-collections/kubernetes.core/pull/971).

New Modules
-----------

community.proxysql
~~~~~~~~~~~~~~~~~~

- community.proxysql.proxysql_mysql_hostgroup_attributes - Manages hostgroup attributes using the ProxySQL admin interface

dellemc.enterprise_sonic
~~~~~~~~~~~~~~~~~~~~~~~~

- dellemc.enterprise_sonic.sonic_ars - Manage adaptive routing and switching (ARS) configuration on SONiC.
- dellemc.enterprise_sonic.sonic_br_l2pt - Manage L2PT configurations on SONiC.
- dellemc.enterprise_sonic.sonic_dcbx - Manage DCBx configurations on SONiC.
- dellemc.enterprise_sonic.sonic_drop_counter - Manage drop counter configuration on SONiC.
- dellemc.enterprise_sonic.sonic_ecmp_load_share - IP ECMP load share mode configuration handling for SONiC.
- dellemc.enterprise_sonic.sonic_evpn_esi_multihome - Manage EVPN ESI multihoming configuration on SONiC.
- dellemc.enterprise_sonic.sonic_fbs_classifiers - Manage flow based services (FBS) classifiers configuration on SONiC.
- dellemc.enterprise_sonic.sonic_fbs_groups - Manage flow based services (FBS) groups configuration on SONiC.
- dellemc.enterprise_sonic.sonic_fbs_policies - Manage flow based services (FBS) policies configuration on SONiC.
- dellemc.enterprise_sonic.sonic_ip_neighbor_interfaces - Manage interface-specific IP neighbor configurations on SONiC.
- dellemc.enterprise_sonic.sonic_ipv6_router_advertisement - Manage interface-specific IPv6 Router Advertisement configurations on SONiC.
- dellemc.enterprise_sonic.sonic_lst - Manage link state tracking (LST) configuration on SONiC.
- dellemc.enterprise_sonic.sonic_mirroring - Manage port mirroring configuration on SONiC.
- dellemc.enterprise_sonic.sonic_network_policy - Manage network policy configuration on SONiC.
- dellemc.enterprise_sonic.sonic_ospfv3 - Configure global OSPFv3 protocol settings on SONiC.
- dellemc.enterprise_sonic.sonic_ospfv3_area - Configure OSPFv3 area settings on SONiC.
- dellemc.enterprise_sonic.sonic_ospfv3_interfaces - Configure OSPFv3 interface mode protocol settings on SONiC.
- dellemc.enterprise_sonic.sonic_pms - Configure interface mode port security settings on SONiC.
- dellemc.enterprise_sonic.sonic_ptp_default_ds - Manage global PTP configurations on SONiC.
- dellemc.enterprise_sonic.sonic_ptp_port_ds - Manage port specific PTP configurations on SONiC.
- dellemc.enterprise_sonic.sonic_ssh_server - Manage SSH server configurations on SONiC.

hitachivantara.vspone_block
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Sds Block
^^^^^^^^^

- hitachivantara.vspone_block.hv_sds_block_compute_port - Manages compute port on Hitachi SDS Block storage systems.
- hitachivantara.vspone_block.hv_sds_block_software_update_file_facts - Get the information of the update file of the storage software which performed transfer (upload) in the storage cluster.
- hitachivantara.vspone_block.hv_sds_block_storage_node_bmc_connection - Manages BMC connection settings for a storage node on Hitachi SDS Block storage systems.
- hitachivantara.vspone_block.hv_sds_block_storage_software_update - Manages software update and downgrade on Hitachi SDS Block storage systems.

Vsp
^^^

- hitachivantara.vspone_block.hv_vsp_one_port - Manages port configuration on Hitachi VSP One storage systems.
- hitachivantara.vspone_block.hv_vsp_one_port_facts - Retrieves port information from Hitachi VSP One storage systems.
- hitachivantara.vspone_block.hv_vsp_one_server - Manages servers on Hitachi VSP One storage systems.
- hitachivantara.vspone_block.hv_vsp_one_server_facts - Retrieves server information from Hitachi VSP One storage systems.
- hitachivantara.vspone_block.hv_vsp_one_server_hba_facts - Retrieves server HBA information from Hitachi VSP One storage systems.

ibm.storage_virtualize
~~~~~~~~~~~~~~~~~~~~~~

- ibm.storage_virtualize.ibm_sv_manage_system_certificate - Manages system certificates and truststore for replication, high availability and FlashSystem grid on IBM Storage Virtualize family systems

purestorage.flashblade
~~~~~~~~~~~~~~~~~~~~~~

- purestorage.flashblade.purefb_kmip - Manage FlashBlade KMIP server objects

theforeman.foreman
~~~~~~~~~~~~~~~~~~

- theforeman.foreman.content_view_history_info - Fetch history of a Content View

Unchanged Collections
---------------------

- amazon.aws (still version 10.1.2)
- ansible.netcommon (still version 8.1.0)
- ansible.posix (still version 2.1.0)
- ansible.utils (still version 6.0.0)
- ansible.windows (still version 3.2.0)
- arista.eos (still version 12.0.0)
- awx.awx (still version 24.6.1)
- azure.azcollection (still version 3.9.0)
- check_point.mgmt (still version 6.5.0)
- chocolatey.chocolatey (still version 1.5.3)
- cisco.aci (still version 2.12.0)
- cisco.dnac (still version 6.40.0)
- cisco.intersight (still version 2.6.0)
- cisco.iosxr (still version 12.0.0)
- cisco.meraki (still version 2.21.8)
- cisco.mso (still version 2.11.0)
- cisco.nxos (still version 11.0.0)
- cisco.ucs (still version 1.16.0)
- cloudscale_ch.cloud (still version 2.5.2)
- community.aws (still version 10.0.0)
- community.ciscosmb (still version 1.0.11)
- community.crypto (still version 3.0.4)
- community.digitalocean (still version 1.27.0)
- community.dns (still version 3.3.4)
- community.docker (still version 4.8.1)
- community.general (still version 11.4.0)
- community.grafana (still version 2.3.0)
- community.hashi_vault (still version 7.0.0)
- community.library_inventory_filtering_v1 (still version 1.1.4)
- community.libvirt (still version 2.0.0)
- community.mongodb (still version 1.7.10)
- community.mysql (still version 4.0.0)
- community.okd (still version 5.0.0)
- community.postgresql (still version 4.1.0)
- community.proxmox (still version 1.3.0)
- community.rabbitmq (still version 1.6.0)
- community.routeros (still version 3.12.1)
- community.sap_libs (still version 1.5.0)
- community.sops (still version 2.2.4)
- community.vmware (still version 6.0.0)
- community.windows (still version 3.0.1)
- community.zabbix (still version 4.1.1)
- containers.podman (still version 1.18.0)
- cyberark.pas (still version 1.0.35)
- dellemc.openmanage (still version 10.0.1)
- dellemc.powerflex (still version 3.0.0)
- dellemc.unity (still version 2.1.0)
- f5networks.f5_modules (still version 1.39.0)
- fortinet.fortimanager (still version 2.11.0)
- fortinet.fortios (still version 2.4.1)
- google.cloud (still version 1.9.0)
- hetzner.hcloud (still version 5.4.0)
- hitachivantara.vspone_object (still version 1.0.0)
- ieisystem.inmanage (still version 3.0.0)
- infinidat.infinibox (still version 1.6.3)
- infoblox.nios_modules (still version 1.8.0)
- inspur.ispim (still version 2.2.3)
- junipernetworks.junos (still version 11.0.0)
- kaytus.ksmanage (still version 2.0.0)
- kubevirt.core (still version 2.2.3)
- lowlydba.sqlserver (still version 2.7.0)
- microsoft.ad (still version 1.9.2)
- microsoft.iis (still version 1.0.3)
- netapp.cloudmanager (still version 21.24.0)
- netapp.ontap (still version 23.1.0)
- netapp.storagegrid (still version 21.15.0)
- netapp_eseries.santricity (still version 1.4.1)
- netbox.netbox (still version 3.21.0)
- ngine_io.cloudstack (still version 2.5.0)
- openstack.cloud (still version 2.4.1)
- ovirt.ovirt (still version 3.2.1)
- purestorage.flasharray (still version 1.39.0)
- ravendb.ravendb (still version 1.0.3)
- splunk.es (still version 4.0.0)
- telekom_mms.icinga_director (still version 2.4.0)
- vmware.vmware (still version 2.4.0)
- vmware.vmware_rest (still version 4.9.0)
- vultr.cloud (still version 1.13.0)
- vyos.vyos (still version 6.0.0)
- wti.remote (still version 1.0.10)

v13.0.0a2
=========

.. contents::
  :local:
  :depth: 2

Release Summary
---------------

Release Date: 2025-10-07

`Porting Guide <https://docs.ansible.com/ansible/devel/porting_guides.html>`_

Added Collections
-----------------

- hitachivantara.vspone_object (version 1.0.0)

Ansible-core
------------

Ansible 13.0.0a2 contains ansible-core version 2.20.0b2.
This is a newer version than version 2.20.0b1 contained in the previous Ansible release.

The changes are reported in the combined changelog below.

Changed Collections
-------------------

If not mentioned explicitly, the changes are reported in the combined changelog below.

+------------------------------------------+------------------+------------------+------------------------------------------------------------------------------------------------------------------------------+
| Collection                               | Ansible 13.0.0a1 | Ansible 13.0.0a2 | Notes                                                                                                                        |
+==========================================+==================+==================+==============================================================================================================================+
| amazon.aws                               | 10.1.1           | 10.1.2           |                                                                                                                              |
+------------------------------------------+------------------+------------------+------------------------------------------------------------------------------------------------------------------------------+
| azure.azcollection                       | 3.8.0            | 3.9.0            | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+------------------------------------------+------------------+------------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.intersight                         | 2.3.0            | 2.6.0            | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+------------------------------------------+------------------+------------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.ios                                | 11.0.0           | 11.1.0           |                                                                                                                              |
+------------------------------------------+------------------+------------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.meraki                             | 2.21.5           | 2.21.8           |                                                                                                                              |
+------------------------------------------+------------------+------------------+------------------------------------------------------------------------------------------------------------------------------+
| community.crypto                         | 3.0.3            | 3.0.4            |                                                                                                                              |
+------------------------------------------+------------------+------------------+------------------------------------------------------------------------------------------------------------------------------+
| community.dns                            | 3.3.3            | 3.3.4            |                                                                                                                              |
+------------------------------------------+------------------+------------------+------------------------------------------------------------------------------------------------------------------------------+
| community.docker                         | 4.7.0            | 4.8.1            |                                                                                                                              |
+------------------------------------------+------------------+------------------+------------------------------------------------------------------------------------------------------------------------------+
| community.general                        | 11.3.0           | 11.4.0           |                                                                                                                              |
+------------------------------------------+------------------+------------------+------------------------------------------------------------------------------------------------------------------------------+
| community.hrobot                         | 2.5.0            | 2.5.2            |                                                                                                                              |
+------------------------------------------+------------------+------------------+------------------------------------------------------------------------------------------------------------------------------+
| community.library_inventory_filtering_v1 | 1.1.1            | 1.1.4            |                                                                                                                              |
+------------------------------------------+------------------+------------------+------------------------------------------------------------------------------------------------------------------------------+
| community.routeros                       | 3.11.0           | 3.12.1           |                                                                                                                              |
+------------------------------------------+------------------+------------------+------------------------------------------------------------------------------------------------------------------------------+
| community.sap_libs                       | 1.4.2            | 1.5.0            |                                                                                                                              |
+------------------------------------------+------------------+------------------+------------------------------------------------------------------------------------------------------------------------------+
| community.sops                           | 2.2.2            | 2.2.4            |                                                                                                                              |
+------------------------------------------+------------------+------------------+------------------------------------------------------------------------------------------------------------------------------+
| dellemc.openmanage                       | 10.0.0           | 10.0.1           |                                                                                                                              |
+------------------------------------------+------------------+------------------+------------------------------------------------------------------------------------------------------------------------------+
| dellemc.powerflex                        | 2.6.1            | 3.0.0            |                                                                                                                              |
+------------------------------------------+------------------+------------------+------------------------------------------------------------------------------------------------------------------------------+
| f5networks.f5_modules                    | 1.38.0           | 1.39.0           | There are no changes recorded in the changelog.                                                                              |
+------------------------------------------+------------------+------------------+------------------------------------------------------------------------------------------------------------------------------+
| fortinet.fortimanager                    | 2.10.0           | 2.11.0           |                                                                                                                              |
+------------------------------------------+------------------+------------------+------------------------------------------------------------------------------------------------------------------------------+
| fortinet.fortios                         | 2.4.0            | 2.4.1            |                                                                                                                              |
+------------------------------------------+------------------+------------------+------------------------------------------------------------------------------------------------------------------------------+
| google.cloud                             | 1.8.0            | 1.9.0            |                                                                                                                              |
+------------------------------------------+------------------+------------------+------------------------------------------------------------------------------------------------------------------------------+
| grafana.grafana                          | 6.0.3            | 6.0.4            |                                                                                                                              |
+------------------------------------------+------------------+------------------+------------------------------------------------------------------------------------------------------------------------------+
| hetzner.hcloud                           | 5.2.0            | 5.4.0            |                                                                                                                              |
+------------------------------------------+------------------+------------------+------------------------------------------------------------------------------------------------------------------------------+
| hitachivantara.vspone_block              | 4.2.0            | 4.2.2            | The collection did not have a changelog in this version.                                                                     |
+------------------------------------------+------------------+------------------+------------------------------------------------------------------------------------------------------------------------------+
| hitachivantara.vspone_object             |                  | 1.0.0            | The collection was added to Ansible                                                                                          |
+------------------------------------------+------------------+------------------+------------------------------------------------------------------------------------------------------------------------------+
| purestorage.flasharray                   | 1.38.0           | 1.39.0           |                                                                                                                              |
+------------------------------------------+------------------+------------------+------------------------------------------------------------------------------------------------------------------------------+
| vmware.vmware                            | 2.3.0            | 2.4.0            |                                                                                                                              |
+------------------------------------------+------------------+------------------+------------------------------------------------------------------------------------------------------------------------------+

Major Changes
-------------

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- The OpenManage Enterprise, OpenManage Enterprise Modular and OpenManage Enterprise Integration for VMware vCenter modules are now compatible with Ansible Core version 2.19.

fortinet.fortios
~~~~~~~~~~~~~~~~

- Supported new versions 7.6.3 and 7.6.4.
- Supported the authentication method when using username and password in v7.6.4.

grafana.grafana
~~~~~~~~~~~~~~~

- Add SUSE support to Alloy role by @pozsa in https://github.com/grafana/grafana-ansible-collection/pull/423
- Fixes to foldersFromFilesStructure option by @root-expert in https://github.com/grafana/grafana-ansible-collection/pull/351
- Migrate RedHat install to ansible.builtin.package by @r65535 in https://github.com/grafana/grafana-ansible-collection/pull/431
- add macOS support to alloy role by @l50 in https://github.com/grafana/grafana-ansible-collection/pull/418
- replace None with [] for safe length checks by @voidquark in https://github.com/grafana/grafana-ansible-collection/pull/426

Minor Changes
-------------

Ansible-core
~~~~~~~~~~~~

- DataLoader - Update ``DataLoader.get_basedir`` to be an abspath
- known_hosts - return rc and stderr when ssh-keygen command fails for further debugging (https://github.com/ansible/ansible/issues/85850).

cisco.ios
~~~~~~~~~

- ios_config - added answering prompt functionality while working in config mode on ios device
- ios_facts - Add chassis_id value to ansible_net_neighbors dictionary for lldp neighbours.

community.dns
~~~~~~~~~~~~~

- Note that some new code in ``plugins/module_utils/_six.py`` is MIT licensed (https://github.com/ansible-collections/community.dns/pull/287).

community.docker
~~~~~~~~~~~~~~~~

- Note that some new code in ``plugins/module_utils/_six.py`` is MIT licensed (https://github.com/ansible-collections/community.docker/pull/1138).
- docker_container - support missing fields and new mount types in ``mounts`` (https://github.com/ansible-collections/community.docker/issues/1129, https://github.com/ansible-collections/community.docker/pull/1134).

community.general
~~~~~~~~~~~~~~~~~

- github_app_access_token lookup plugin - add support for GitHub Enterprise Server (https://github.com/ansible-collections/community.general/issues/10879, https://github.com/ansible-collections/community.general/pull/10880).
- gitlab_group_variable - add ``description`` option (https://github.com/ansible-collections/community.general/pull/10812).
- gitlab_instance_variable - add ``description`` option (https://github.com/ansible-collections/community.general/pull/10812).
- gitlab_project_variable - add ``description`` option (https://github.com/ansible-collections/community.general/pull/10812, https://github.com/ansible-collections/community.general/issues/8584, https://github.com/ansible-collections/community.general/issues/10809).
- keycloak_client - add idempotent support for ``optional_client_scopes`` and ``optional_client_scopes``, and ensure consistent change detection between check mode and live run (https://github.com/ansible-collections/community.general/issues/5495, https://github.com/ansible-collections/community.general/pull/10842).
- pipx module_utils - use ``PIPX_USE_EMOJI`` to disable emojis in the output of ``pipx`` 1.8.0 (https://github.com/ansible-collections/community.general/pull/10874).

community.routeros
~~~~~~~~~~~~~~~~~~

- api_modify - add ``vrf`` for ``system logging action`` with a default of ``main`` for RouterOS 7.19 and newer (https://github.com/ansible-collections/community.routeros/pull/401).
- api_modify, api_info - field ``instance`` in ``routing bgp connection`` path is required, and ``router-id`` has been moved to ``routing bgp instance`` by RouterOS 7.20 and newer (https://github.com/ansible-collections/community.routeros/pull/404).
- api_modify, api_info - support for field ``new-priority`` in API path ``ipv6 firewall mangle``` (https://github.com/ansible-collections/community.routeros/pull/402).

community.sap_libs
~~~~~~~~~~~~~~~~~~

- collection - Enhance `ansible-test`` CI action, remove Python 2 and fix detected issues (https://github.com/sap-linuxlab/community.sap_libs/pull/60)
- collection - Pipeline fixes and drop test support for ansible below 2.13 (https://github.com/sap-linuxlab/community.sap_libs/pull/43)
- collection - Update documentation and changelog for `1.5.0` release (https://github.com/sap-linuxlab/community.sap_libs/pull/61)
- collection - Update workflow `ansible-test` to include latest versions (https://github.com/sap-linuxlab/community.sap_libs/pull/54)
- sap_control_exec - Remove unsupported functions (https://github.com/sap-linuxlab/community.sap_libs/pull/45)
- sap_hdbsql - add -E option to filepath command (https://github.com/sap-linuxlab/community.sap_libs/pull/42)

community.sops
~~~~~~~~~~~~~~

- Note that some new code in ``plugins/module_utils/_six.py`` is MIT licensed (https://github.com/ansible-collections/community.sops/pull/268).

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- idrac_support_assist - Introduced aliases for the module parameters share_username and share_password to align with the naming conventions used across other modules, ensuring consistency and improving usability.

dellemc.powerflex
~~~~~~~~~~~~~~~~~

- Added support for executing activemq, lia, mdm and tb roles on PowerFlex Gen2.
- Added support for executing mdm_cluster, nvme_host, sdc, sdt and snapshot_policy modules on PowerFlex Gen2.

fortinet.fortimanager
~~~~~~~~~~~~~~~~~~~~~

- Supported new schemas in FortiManager 7.0.14, 7.2.10, 7.2.11.

google.cloud
~~~~~~~~~~~~

- iap - added scp_if_ssh option (https://github.com/ansible-collections/google.cloud/pull/716).

hetzner.hcloud
~~~~~~~~~~~~~~

- server_type_info - Return new Server Type ``category`` property.
- server_type_info - Return new Server Type ``locations`` property.
- zone - New module to manage DNS Zones in Hetzner Cloud.
- zone_info - New module to fetch DNS Zones details.
- zone_rrset - New module to manage DNS Zone RRSets in the Hetzner Cloud.
- zone_rrset_info - New module to fetch DNS RRSets details.

purestorage.flasharray
~~~~~~~~~~~~~~~~~~~~~~

- purefa_arrayname - Added Fusion support
- purefa_audits - Added Fusion support
- purefa_banner - Added Fusion support
- purefa_connect - Added Fusion support
- purefa_console - Added Fusion support
- purefa_directory - Added Fusion support
- purefa_dirsnap - Added Fusion support
- purefa_ds - Added Fusion support
- purefa_dsrole - Added Fusion support
- purefa_endpoint - Added Fusion support
- purefa_eradication - Added Fusion support
- purefa_export - Added Fusion support
- purefa_fs - Added Fusion support
- purefa_maintenance - Timeout window updated
- purefa_messages - Added Fusion support
- purefa_offload - Added Fusion support
- purefa_policy - Added Fusion support
- purefa_syslog_settings - Added Fusion support
- purefa_timeout - Added Fusion support

vmware.vmware
~~~~~~~~~~~~~

- Add module for importing iso images to content library.
- Remove six imports from _facts.py and _vsphere_tasks.py due to new sanity rules. Python 2 (already not supported) will fail to execute these files.
- tag_associations - Add module to manage tag associations with objects
- tag_categories - Add module to manage tag categories
- tags - Add module to manage tags
- vms - Add option to inventory plugin to gather cluster and ESXi host name for VMs. (Fixes https://github.com/ansible-collections/vmware.vmware/issues/215)

Deprecated Features
-------------------

dellemc.powerflex
~~~~~~~~~~~~~~~~~

- The device, info, protection_domain, snapshot, storagepool and volume modules are supported only on PowerFlex Gen1. They are replaced by v2 modules on PowerFlex Gen2.
- The fault_set, replication_consistency_group, replication_pair, resource_group and sds modules are not supported on PowerFlex Gen2.

hetzner.hcloud
~~~~~~~~~~~~~~

- server_type_info - Deprecate Server Type ``deprecation`` property.

Removed Features (previously deprecated)
----------------------------------------

Ansible-core
~~~~~~~~~~~~

- ansible-galaxy - remove support for resolvelib >= 0.5.3, < 0.8.0.

Bugfixes
--------

Ansible-core
~~~~~~~~~~~~

- Fix issue where play tags prevented executing notified handlers (https://github.com/ansible/ansible/issues/85475)
- Fix issues with keywords being incorrectly validated on ``import_tasks`` (https://github.com/ansible/ansible/issues/85855, https://github.com/ansible/ansible/issues/85856)
- Fix traceback when trying to import non-existing file via nested ``import_tasks`` (https://github.com/ansible/ansible/issues/69882)
- ansible-doc - prevent crash when scanning collections in paths that have more than one ``ansible_collections`` in it (https://github.com/ansible/ansible/issues/84909, https://github.com/ansible/ansible/pull/85361).
- fetch - also return ``file`` in the result when changed is ``True`` (https://github.com/ansible/ansible/pull/85729).

amazon.aws
~~~~~~~~~~

- Remove ``ansible.module_utils.six`` imports to avoid warnings (https://github.com/ansible-collections/amazon.aws/pull/2727).
- amazon.aws.autoscaling_instance - setting the state to ``terminated`` had no effect. The fix implements missing instance termination state (https://github.com/ansible-collections/amazon.aws/issues/2719).
- ec2_vpc_nacl - Fix issue when trying to update existing Network ACL rule (https://github.com/ansible-collections/amazon.aws/issues/2592).
- s3_object - Honor headers for content and content_base64 uploads by promoting supported keys (e.g. ContentType, ContentDisposition, CacheControl) to top-level S3 arguments and placing remaining keys under Metadata. This makes content uploads consistent with src uploads. (https://github.com/ansible-collections/amazon.aws)

cisco.ios
~~~~~~~~~

- Fixed an issue where configuration within an address family (ipv6) was ignored by the parser.
- cisco.ios.ios_vrf_global - fixed issue preventing idempotent configuration of multiple import/export route-targets for a VRF.
- ios_hsrp_interfaces - Device defaults version to 1 if standby_groups is present but version is not configured. and module would also consider priority as 100 if not configured, to maintain idempotency.
- ios_hsrp_interfaces - Fixed operation for ipv6 standby configuration.
- ios_static_routes - Fix parsing of static routes with interface and distance in gathered state

cisco.meraki
~~~~~~~~~~~~

- Enhanced networks_switch_qos_rules_order object lookup logic to properly match QoS rules by vlan, protocol, srcPort, and dstPort parameters
- Fixed VLAN parameter handling in networks_switch_qos_rules_order changed name parameter to vlan parameter for proper object lookup
- Fixed comparison function call in networks_switch_dscp_to_cos_mappings changed 'meraki_compare_equality2' to 'meraki_compare_equality'
- Fixed function name typo in organizations_appliance_vpn_third_party_vpnpeers changed 'getOrganizationApplianceVpnThirdPartyVpnpeers' to 'getOrganizationApplianceVpnThirdPartyVPNPeers'
- Fixed function name typo in organizations_appliance_vpn_third_party_vpnpeers changed 'updateOrganizationApplianceVpnThirdPartyVpnpeers' to 'updateOrganizationApplianceVpnThirdPartyVPNPeers'
- Fixed parameter handling in networks_switch_qos_rules_order to use qosRuleId instead of id for object identification
- Improved dictionary comparison logic in meraki.py plugin utils to handle nested dictionaries correctly
- Improved meraki_compare_equality2 function to handle None value comparisons more accurately
- Updated networks_switch_qos_rules_order playbook with corrected parameter values and VLAN configuration
- networks_switch_qos_rules_order: extend object lookup to include srcPortRange and dstPortRange when matching existing QoS rules to improve idempotency

community.crypto
~~~~~~~~~~~~~~~~

- Avoid deprecated functionality in ansible-core 2.20 (https://github.com/ansible-collections/community.crypto/pull/953).

community.dns
~~~~~~~~~~~~~

- Avoid using ``ansible.module_utils.six`` to avoid deprecation warnings with ansible-core 2.20 (https://github.com/ansible-collections/community.dns/pull/287).
- Update Public Suffix List.

community.docker
~~~~~~~~~~~~~~~~

- Avoid deprecated functionality in ansible-core 2.20 (https://github.com/ansible-collections/community.docker/pull/1117).
- Avoid remaining usages of deprecated ``ansible.module_utils.six`` (https://github.com/ansible-collections/community.docker/pull/1133).
- Avoid usage of deprecated ``ansible.module_utils.six`` in all code that does not have to support Python 2 (https://github.com/ansible-collections/community.docker/pull/1137, https://github.com/ansible-collections/community.docker/pull/1139).
- Avoid usage of deprecated ``ansible.module_utils.six`` in some of the code that still supports Python 2 (https://github.com/ansible-collections/community.docker/pull/1138).

community.general
~~~~~~~~~~~~~~~~~

- Avoid usage of deprecated ``ansible.module_utils.six`` in all code that does not have to support Python 2 (https://github.com/ansible-collections/community.general/pull/10873).
- gem - fix soundness issue when uninstalling default gems on Ubuntu  (https://github.com/ansible-collections/community.general/issues/10451, https://github.com/ansible-collections/community.general/pull/10689).
- github_app_access_token lookup plugin - fix compatibility imports for using jwt (https://github.com/ansible-collections/community.general/issues/10807, https://github.com/ansible-collections/community.general/pull/10810).
- github_deploy_key - fix bug during error handling if no body was present in the result (https://github.com/ansible-collections/community.general/issues/10853, https://github.com/ansible-collections/community.general/pull/10857).
- homebrew - do not fail when cask or formula name has changed in homebrew repo (https://github.com/ansible-collections/community.general/issues/10804, https://github.com/ansible-collections/community.general/pull/10805).
- keycloak_group - fixes an issue where module ignores realm when searching subgroups by name (https://github.com/ansible-collections/community.general/pull/10840).
- keycloak_role - fixes an issue where the module incorrectly returns ``changed=true`` when using the alias ``clientId`` in composite roles (https://github.com/ansible-collections/community.general/pull/10829).
- parted - variable is a list, not text (https://github.com/ansible-collections/community.general/pull/10823, https://github.com/ansible-collections/community.general/issues/10817).
- rocketchat - fix message delivery in Rocket Chat >= 7.5.3 by forcing ``Content-Type`` header to ``application/json`` instead of the default ``application/x-www-form-urlencoded`` (https://github.com/ansible-collections/community.general/issues/10796, https://github.com/ansible-collections/community.general/pull/10796).
- yaml cache plugin - make compatible with ansible-core 2.19 (https://github.com/ansible-collections/community.general/issues/10849, https://github.com/ansible-collections/community.general/issues/10852).

community.hrobot
~~~~~~~~~~~~~~~~

- Avoid deprecated functionality in ansible-core 2.20 (https://github.com/ansible-collections/community.hrobot/pull/174).
- Avoid using ``ansible.module_utils.six`` to avoid deprecation warnings with ansible-core 2.20 (https://github.com/ansible-collections/community.hrobot/pull/177).

community.library_inventory_filtering_v1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Avoid deprecated functionality in ansible-core 2.20 (https://github.com/ansible-collections/community.library_inventory_filtering/pull/38).
- Fix accidental type extensions (https://github.com/ansible-collections/community.library_inventory_filtering/pull/40).
- Stop using ``ansible.module_utils.six`` to avoid user-facing deprecation messages with ansible-core 2.20, while still supporting older ansible-core versions (https://github.com/ansible-collections/community.library_inventory_filtering/pull/39).

community.routeros
~~~~~~~~~~~~~~~~~~

- Avoid using ``ansible.module_utils.six`` to avoid deprecation warnings with ansible-core 2.20 (https://github.com/ansible-collections/community.routeros/pull/405).
- Fix accidental type extensions (https://github.com/ansible-collections/community.routeros/pull/406).

community.sops
~~~~~~~~~~~~~~

- Avoid using ``ansible.module_utils.six`` to avoid deprecation warnings with ansible-core 2.20 (https://github.com/ansible-collections/community.sops/pull/268).
- Fix accidental type extensions (https://github.com/ansible-collections/community.sops/pull/269).

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- Fixed the UT test execution through ansible-test - (Issue 1003) - Tests Pass Using Tox But Not Ansible-Test (https://github.com/dell/dellemc-openmanage-ansible-modules)
- idrac_support_assist - Updated module playbook examples to use the correct casing for protocol names, for CIFS and HTTPS.
- idrac_system_info - (Issue 1017) - System info not being returned on gen17s with v10.0.0 (https://github.com/dell/dellemc-openmanage-ansible-modules/issues/1017)
- redfish_storage_volume - (Issue 1027) Module fails on force reboot. (https://github.com/dell/dellemc-openmanage-ansible-modules/issues/1027)

fortinet.fortimanager
~~~~~~~~~~~~~~~~~~~~~

- Changed the logic of getting FortiManager system information to prevent permission denied error.
- Supported module_defaults. General variables can be specified in one place by using module_defaults.

fortinet.fortios
~~~~~~~~~~~~~~~~

- Fix the issue in check_modu when backend returns invallid IP address.
- Fix the issue in configuration_fact and monitor_fact when omitting vdom or assigning vdom to "".

hetzner.hcloud
~~~~~~~~~~~~~~

- floating_ip - Wait for the Floating IP assign action to complete to reduce chances of running into ``locked`` errors.
- server - Also check server type deprecation after server creation.

purestorage.flasharray
~~~~~~~~~~~~~~~~~~~~~~

- purefa_eradication - Idempotency fix
- purefa_info - Fixed AttributeError for hgroups subset
- purefa_pg - Fixed AttributeError adding target to PG

vmware.vmware
~~~~~~~~~~~~~

- Drop incorrect requirement on aiohttp (https://github.com/ansible-collections/vmware.vmware/pull/230).
- cluster_ha - Fix admission control policy not being updated when ac is disabled
- content_template - Fix typo in code for check mode that tried to access a module param which doesn't exist.
- import_content_library_ovf - Fix large file import by using requests instead of open_url. Requests allows for streaming uploads, instead of reading the entire file into memory. (Fixes https://github.com/ansible-collections/vmware.vmware/issues/220)
- vm_powerstate - Ensure timeout option also applies to the shutdown-guest state

Known Issues
------------

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- Formal qualification of module ome_smart_fabric_info for Ansible Core version 2.19 is still pending.
- idrac_diagnostics - This module does not support export of diagnostics file to HTTP and HTTPS share via SOCKS proxy.
- idrac_license - Due to API limitation, proxy parameters are ignored during the import operation.
- idrac_license - The module will give different error messages for iDRAC9 and iDRAC10 when user imports license with invalid share name.
- idrac_os_deployment - The module continues to return a 200 response and marks the job as completed, even when an outdated date is supplied in the Expose duration.
- idrac_redfish_storage_controller - PatrolReadRatePercent attribute cannot be set in iDRAC10.
- idrac_server_config_profile - When attempting to revert iDRAC settings using a previously exported SCP file, the import operation will complete with errors if a new user was created after the export (Instead of restoring the system to its previous state, including the removal of newly added users).
- idrac_system_info - The module will show empty video list despite having Embedded VIDEO controller.
- ome_smart_fabric_uplink - The module supported by OpenManage Enterprise Modular, however it does not allow the creation of multiple uplinks of the same name. If an uplink is created using the same name as an existing uplink, then the existing uplink is modified.
- redfish_storage_volume - Encryption type and block_io_size bytes will be read only property in iDRAC9 and iDRAC10 and hence the module ignores these parameters.

New Modules
-----------

dellemc.powerflex
~~~~~~~~~~~~~~~~~

- dellemc.powerflex.device_v2 - Manage device on Dell PowerFlex Gen2
- dellemc.powerflex.info_v2 - Gathering information about Dell PowerFlex Gen2
- dellemc.powerflex.protection_domain_v2 - Manage Protection Domain on Dell PowerFlex Gen2
- dellemc.powerflex.snapshot_v2 - Manage Snapshots on Dell PowerFlex Gen2
- dellemc.powerflex.storagepool_v2 - Managing Dell PowerFlex storage pool Gen2
- dellemc.powerflex.volume_v2 - Manage volumes on Dell PowerFlex Gen2

Unchanged Collections
---------------------

- ansible.netcommon (still version 8.1.0)
- ansible.posix (still version 2.1.0)
- ansible.utils (still version 6.0.0)
- ansible.windows (still version 3.2.0)
- arista.eos (still version 12.0.0)
- awx.awx (still version 24.6.1)
- check_point.mgmt (still version 6.5.0)
- chocolatey.chocolatey (still version 1.5.3)
- cisco.aci (still version 2.12.0)
- cisco.dnac (still version 6.40.0)
- cisco.iosxr (still version 12.0.0)
- cisco.mso (still version 2.11.0)
- cisco.nxos (still version 11.0.0)
- cisco.ucs (still version 1.16.0)
- cloudscale_ch.cloud (still version 2.5.2)
- community.aws (still version 10.0.0)
- community.ciscosmb (still version 1.0.11)
- community.digitalocean (still version 1.27.0)
- community.grafana (still version 2.3.0)
- community.hashi_vault (still version 7.0.0)
- community.libvirt (still version 2.0.0)
- community.mongodb (still version 1.7.10)
- community.mysql (still version 4.0.0)
- community.okd (still version 5.0.0)
- community.postgresql (still version 4.1.0)
- community.proxmox (still version 1.3.0)
- community.proxysql (still version 1.6.0)
- community.rabbitmq (still version 1.6.0)
- community.vmware (still version 6.0.0)
- community.windows (still version 3.0.1)
- community.zabbix (still version 4.1.1)
- containers.podman (still version 1.18.0)
- cyberark.conjur (still version 1.3.7)
- cyberark.pas (still version 1.0.35)
- dellemc.enterprise_sonic (still version 3.0.0)
- dellemc.unity (still version 2.1.0)
- ibm.storage_virtualize (still version 3.0.0)
- ieisystem.inmanage (still version 3.0.0)
- infinidat.infinibox (still version 1.6.3)
- infoblox.nios_modules (still version 1.8.0)
- inspur.ispim (still version 2.2.3)
- junipernetworks.junos (still version 11.0.0)
- kaytus.ksmanage (still version 2.0.0)
- kubernetes.core (still version 6.1.0)
- kubevirt.core (still version 2.2.3)
- lowlydba.sqlserver (still version 2.7.0)
- microsoft.ad (still version 1.9.2)
- microsoft.iis (still version 1.0.3)
- netapp.cloudmanager (still version 21.24.0)
- netapp.ontap (still version 23.1.0)
- netapp.storagegrid (still version 21.15.0)
- netapp_eseries.santricity (still version 1.4.1)
- netbox.netbox (still version 3.21.0)
- ngine_io.cloudstack (still version 2.5.0)
- openstack.cloud (still version 2.4.1)
- ovirt.ovirt (still version 3.2.1)
- purestorage.flashblade (still version 1.21.2)
- ravendb.ravendb (still version 1.0.3)
- splunk.es (still version 4.0.0)
- telekom_mms.icinga_director (still version 2.4.0)
- theforeman.foreman (still version 5.6.0)
- vmware.vmware_rest (still version 4.9.0)
- vultr.cloud (still version 1.13.0)
- vyos.vyos (still version 6.0.0)
- wti.remote (still version 1.0.10)

v13.0.0a1
=========

.. contents::
  :local:
  :depth: 2

Release Summary
---------------

Release Date: 2025-09-24

`Porting Guide <https://docs.ansible.com/ansible/devel/porting_guides.html>`_

Removed Collections
-------------------

- ibm.qradar (previously included version: 4.0.0)

You can still install a removed collection manually with ``ansible-galaxy collection install <name-of-collection>``.

Added Collections
-----------------

- ravendb.ravendb (version 1.0.3)

Ansible-core
------------

Ansible 13.0.0a1 contains ansible-core version 2.20.0b1.
This is a newer version than version 2.19.1 contained in the previous Ansible release.

The changes are reported in the combined changelog below.

Included Collections
--------------------

If not mentioned explicitly, the changes are reported in the combined changelog below.

+-----------------------------+----------------+------------------+------------------------------------------------------------------------------------------------------------------------------+
| Collection                  | Ansible 12.0.0 | Ansible 13.0.0a1 | Notes                                                                                                                        |
+=============================+================+==================+==============================================================================================================================+
| check_point.mgmt            | 6.4.1          | 6.5.0            |                                                                                                                              |
+-----------------------------+----------------+------------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.dnac                  | 6.39.0         | 6.40.0           |                                                                                                                              |
+-----------------------------+----------------+------------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.intersight            | 2.2.0          | 2.3.0            | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+-----------------------------+----------------+------------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.meraki                | 2.21.4         | 2.21.5           |                                                                                                                              |
+-----------------------------+----------------+------------------+------------------------------------------------------------------------------------------------------------------------------+
| community.dns               | 3.3.2          | 3.3.3            |                                                                                                                              |
+-----------------------------+----------------+------------------+------------------------------------------------------------------------------------------------------------------------------+
| community.general           | 11.2.1         | 11.3.0           |                                                                                                                              |
+-----------------------------+----------------+------------------+------------------------------------------------------------------------------------------------------------------------------+
| community.mysql             | 3.15.0         | 4.0.0            |                                                                                                                              |
+-----------------------------+----------------+------------------+------------------------------------------------------------------------------------------------------------------------------+
| community.routeros          | 3.10.0         | 3.11.0           |                                                                                                                              |
+-----------------------------+----------------+------------------+------------------------------------------------------------------------------------------------------------------------------+
| community.vmware            | 5.7.2          | 6.0.0            |                                                                                                                              |
+-----------------------------+----------------+------------------+------------------------------------------------------------------------------------------------------------------------------+
| community.zabbix            | 4.1.0          | 4.1.1            |                                                                                                                              |
+-----------------------------+----------------+------------------+------------------------------------------------------------------------------------------------------------------------------+
| containers.podman           | 1.17.0         | 1.18.0           |                                                                                                                              |
+-----------------------------+----------------+------------------+------------------------------------------------------------------------------------------------------------------------------+
| dellemc.openmanage          | 9.12.3         | 10.0.0           |                                                                                                                              |
+-----------------------------+----------------+------------------+------------------------------------------------------------------------------------------------------------------------------+
| google.cloud                | 1.7.0          | 1.8.0            |                                                                                                                              |
+-----------------------------+----------------+------------------+------------------------------------------------------------------------------------------------------------------------------+
| hitachivantara.vspone_block | 4.1.0          | 4.2.0            |                                                                                                                              |
+-----------------------------+----------------+------------------+------------------------------------------------------------------------------------------------------------------------------+
| ibm.storage_virtualize      | 2.7.4          | 3.0.0            |                                                                                                                              |
+-----------------------------+----------------+------------------+------------------------------------------------------------------------------------------------------------------------------+
| purestorage.flasharray      | 1.36.0         | 1.38.0           |                                                                                                                              |
+-----------------------------+----------------+------------------+------------------------------------------------------------------------------------------------------------------------------+
| purestorage.flashblade      | 1.20.0         | 1.21.2           |                                                                                                                              |
+-----------------------------+----------------+------------------+------------------------------------------------------------------------------------------------------------------------------+
| ravendb.ravendb             |                | 1.0.3            | The collection was added to Ansible                                                                                          |
+-----------------------------+----------------+------------------+------------------------------------------------------------------------------------------------------------------------------+
| theforeman.foreman          | 5.5.0          | 5.6.0            |                                                                                                                              |
+-----------------------------+----------------+------------------+------------------------------------------------------------------------------------------------------------------------------+

Major Changes
-------------

Ansible-core
~~~~~~~~~~~~

- ansible - Add support for Python 3.14.
- ansible - Drop support for Python 3.11 on the controller.
- ansible - Drop support for Python 3.8 on targets.

community.vmware
~~~~~~~~~~~~~~~~

- Re-use code from ``vmware.vmware`` (https://github.com/ansible-collections/community.vmware/pull/2459).

containers.podman
~~~~~~~~~~~~~~~~~

- Add inventory plugins for buildah and podman
- Add podman system connection modules

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- idrac_certificate - This role is enhanced to support iDRAC10.
- idrac_export_server_config_profile - This role is enhanced to support iDRAC10.
- idrac_firmware - This role is enhanced to support iDRAC10.
- idrac_import_server_config_profile - This role is enhanced to support iDRAC10.
- idrac_license - This module is enhanced to support iDRAC10.
- idrac_os_deployment - This module is enhanced to support iDRAC10.
- idrac_os_deployment - This role is enhanced to support iDRAC10.
- idrac_redfish_storage_controller - This module is enhanced to support iDRAC10.
- idrac_server_config_profile - This module is enhanced to support iDRAC10.
- idrac_storage_controller - This role is enhanced to support iDRAC10.
- idrac_storage_volume - This module is enhanced to support iDRAC10.
- redfish_firmware - This role is enhanced to support iDRAC10.
- redfish_firmware_rollback - This module is enhanced to support iDRAC10.
- redfish_storage_volume - This module is enhanced to support iDRAC10.
- redfish_storage_volume - This role is enhanced to support iDRAC10.

Minor Changes
-------------

Ansible-core
~~~~~~~~~~~~

- Add tech preview play argument spec validation, which can be enabled by setting the play keyword ``validate_argspec`` to ``True`` or the name of an argument spec. When ``validate_argspec`` is set to ``True``, a play ``name`` is required and used as the argument spec name. When enabled, the argument spec is loaded from a file matching the pattern <playbook_name>.meta.yml. At minimum, this file should contain ``{"argument_specs": {"name": {"options": {}}}}``, where "name" is the name of the play or configured argument spec.
- Added Univention Corporate Server as a part of Debian OS distribution family (https://github.com/ansible/ansible/issues/85490).
- AnsibleModule - Add temporary internal monkeypatch-able hook to alter module result serialization by splitting serialization from ``_return_formatted`` into ``_record_module_result``.
- Python type hints applied to ``to_text`` and ``to_bytes`` functions for better type hint interactions with code utilizing these functions.
- ansible now warns if you use reserved tags that were only meant for selection and not for use in play.
- ansible-doc - Return a more verbose error message when the ``description`` field is missing.
- ansible-doc - show ``notes``, ``seealso``, and top-level ``version_added`` for role entrypoints (https://github.com/ansible/ansible/pull/81796).
- ansible-doc adds support for RETURN documentation to support doc fragment plugins
- ansible-test - Implement new authentication methods for accessing the Ansible Core CI service.
- ansible-test - Improve formatting of generated coverage config file.
- ansible-test - Removed support for automatic provisioning of obsolete instances for network-integration tests.
- ansible-test - Replace FreeBSD 14.2 with 14.3.
- ansible-test - Replace RHEL 9.5 with 9.6.
- ansible-test - Update Ubuntu containers.
- ansible-test - Update base/default containers to include Python 3.14.0.
- ansible-test - Update pinned sanity test requirements.
- ansible-test - Update test containers.
- ansible-test - Upgrade Alpine 3.21 to 3.22.
- ansible-test - Upgrade Fedora 41 to Fedora 42.
- ansible-test - Upgrade to ``coverage`` version 7.10.7 for Python 3.9 and later.
- ansible-test - Use OS packages to satisfy controller requirements on FreeBSD 13.5 during managed instance bootstrapping.
- apt_repository - use correct debug method to print debug message.
- blockinfile - add new module option ``encoding`` to support files in encodings other than UTF-8 (https://github.com/ansible/ansible/pull/85291).
- deb822_repository - Add automatic installation of the ``python3-debian`` package if it is missing by adding the parameter ``install_python_debian``
- default callback plugin - add option to configure indentation for JSON and YAML output (https://github.com/ansible/ansible/pull/85497).
- encrypt - check datatype of salt_size in password_hash filter.
- fetch_file - add ca_path and cookies parameter arguments (https://github.com/ansible/ansible/issues/85172).
- include_vars - Raise an error if 'extensions' is not specified as a list.
- include_vars - Raise an error if 'ignore_files' is not specified as a list.
- lineinfile - add new module option ``encoding`` to support files in encodings other than UTF-8 (https://github.com/ansible/ansible/pull/84999).
- regex - Document the match_type fullmatch.
- regex - Ensure that match_type is one of match, fullmatch, or search (https://github.com/ansible/ansible/pull/85629).
- replace - read/write files in text-mode as unicode chars instead of as bytes and switch regex matching to unicode chars instead of bytes. (https://github.com/ansible/ansible/pull/85785).
- service_facts - handle keyerror exceptions with warning.
- service_facts - warn user about missing service details instead of ignoring.
- setup - added new subkey ``lvs`` within each entry of ``ansible_facts['vgs']`` to provide complete logical volume data scoped by volume group. The top level ``lvs`` fact by comparison, deduplicates logical volume names across volume groups and may be incomplete. (https://github.com/ansible/ansible/issues/85632)
- six - bump six version from 1.16.0 to 1.17.0 (https://github.com/ansible/ansible/issues/85408).
- stat module - add SELinux context as a return value, and add a new option to trigger this return, which is False by default. (https://github.com/ansible/ansible/issues/85217).
- tags now warn when using reserved keywords.
- wrapt - bump version from 1.15.0 to 1.17.2 (https://github.com/ansible/ansible/issues/85407).

check_point.mgmt
~~~~~~~~~~~~~~~~

- added new parameter 'ips_settings' to 'cp_mgmt_simple_cluster' and 'cp_mgmt_simple_gateway' modules.
- added new parameter 'override_vpn_domains' to 'cp_mgmt_set_vpn_community_remote_access' module.
- added new parameter 'show_installation_targets' to 'cp_mgmt_package_facts' module.
- added new parameters (such as 'permanent_tunnels', excluded_services, etc.) to 'cp_mgmt_vpn_community_meshed' and 'cp_mgmt_vpn_community_star' modules.

cisco.dnac
~~~~~~~~~~

- Added attribute 'slots' in assurance_icap_settings_workflow_manager module
- Added attribute 'transit_site_hierarchy' in sda_fabric_transits_workflow_manager module
- Added attributes 'wireless_flooding_enable', 'resource_guard_enable', 'flooding_address_assignment', 'flooding_address' in sda_fabric_transits_workflow_manager module
- Changes in assurance_icap_settings_workflow_manager module
- Changes in assurance_issue_workflow_manager module
- Changes in inventory_workflow_manager module
- Changes in network_profile_switching_workflow_manager module
- Changes in network_settings_workflow_manager module
- Changes in sda_fabric_devices_workflow_manager module
- Changes in sda_fabric_sites_zones_workflow_manager module
- Changes in sda_fabric_transits_workflow_manager module
- Changes in sda_virtual_networks_workflow_manager module
- Changes in template_workflow_manager module
- Removed attribute 'slot' in assurance_icap_settings_workflow_manager module

community.general
~~~~~~~~~~~~~~~~~

- android_sdk - minor refactor to improve readability (https://github.com/ansible-collections/community.general/pull/10712).
- django module utils - simplify/consolidate the common settings for the command line (https://github.com/ansible-collections/community.general/pull/10684).
- django_check - rename parameter ``database`` to ``databases``, add alias for compatibility (https://github.com/ansible-collections/community.general/pull/10700).
- django_check - simplify/consolidate the common settings for the command line (https://github.com/ansible-collections/community.general/pull/10684).
- django_createcachetable - simplify/consolidate the common settings for the command line (https://github.com/ansible-collections/community.general/pull/10684).
- elasticsearch_plugin - minor refactor to improve readability (https://github.com/ansible-collections/community.general/pull/10712).
- filesize - minor refactor to simplify string formatting (https://github.com/ansible-collections/community.general/pull/10727).
- github_app_access_token lookup plugin - support both ``jwt`` and ``pyjwt`` to avoid conflict with other modules requirements (https://github.com/ansible-collections/community.general/issues/10299).
- gitlab_group_access_token - add ``planner`` access level (https://github.com/ansible-collections/community.general/pull/10679).
- gitlab_group_access_token - add missing scopes (https://github.com/ansible-collections/community.general/pull/10785).
- gitlab_group_variable - support masked-and-hidden variables (https://github.com/ansible-collections/community.general/pull/10787).
- gitlab_label - minor refactor to improve readability (https://github.com/ansible-collections/community.general/pull/10711).
- gitlab_milestone - minor refactor to improve readability (https://github.com/ansible-collections/community.general/pull/10711).
- gitlab_project_access_token - add ``planner`` access level (https://github.com/ansible-collections/community.general/pull/10679).
- gitlab_project_access_token - add missing scopes (https://github.com/ansible-collections/community.general/pull/10785).
- gitlab_project_variable - support masked-and-hidden variables (https://github.com/ansible-collections/community.general/pull/10787).
- gitlab_protected_branch - add ``allow_force_push``, ``code_owner_approval_required`` (https://github.com/ansible-collections/community.general/pull/10795, https://github.com/ansible-collections/community.general/issues/6432, https://github.com/ansible-collections/community.general/issues/10289, https://github.com/ansible-collections/community.general/issues/10765).
- gitlab_protected_branch - update protected branches if possible instead of recreating them (https://github.com/ansible-collections/community.general/pull/10795).
- iocage inventory plugin - minor refactor to improve readability (https://github.com/ansible-collections/community.general/pull/10712).
- ipa_host - minor refactor to improve readability (https://github.com/ansible-collections/community.general/pull/10711).
- iptables_state - minor refactor to simplify string formatting (https://github.com/ansible-collections/community.general/pull/10727).
- keycloak_realm - add support for WebAuthn policy configuration options, including both regular and passwordless WebAuthn policies (https://github.com/ansible-collections/community.general/pull/10791).
- lvg_rename - minor refactor to improve readability (https://github.com/ansible-collections/community.general/pull/10711).
- manageiq - minor refactor to improve readability (https://github.com/ansible-collections/community.general/pull/10712).
- manageiq_alert_profiles - minor refactor to improve readability (https://github.com/ansible-collections/community.general/pull/10712).
- manageiq_group - minor refactor to simplify string formatting (https://github.com/ansible-collections/community.general/pull/10727).
- manageiq_tenant - minor refactor to simplify string formatting (https://github.com/ansible-collections/community.general/pull/10727).
- mssql_db - minor refactor to simplify string formatting (https://github.com/ansible-collections/community.general/pull/10727).
- one_vm - minor refactor to improve readability (https://github.com/ansible-collections/community.general/pull/10712).
- openbsd_pkg - add ``autoremove`` parameter to remove unused dependencies (https://github.com/ansible-collections/community.general/pull/10705).
- openbsd_pkg - minor refactor to simplify string formatting (https://github.com/ansible-collections/community.general/pull/10727).
- pacemaker_resource - add ``state=cleanup`` for cleaning up pacemaker resources (https://github.com/ansible-collections/community.general/pull/10413)
- pacemaker_resource - add ``state=cloned`` for cloning pacemaker resources or groups (https://github.com/ansible-collections/community.general/issues/10322, https://github.com/ansible-collections/community.general/pull/10665).
- pacemaker_resource - the parameter ``name`` is no longer a required parameter in community.general 11.3.0 (https://github.com/ansible-collections/community.general/pull/10413)
- parted - using safer mechanism to run external command (https://github.com/ansible-collections/community.general/pull/10642).
- random_string lookup plugin - allow to specify seed while generating random string (https://github.com/ansible-collections/community.general/issues/5362, https://github.com/ansible-collections/community.general/pull/10710).
- scaleway modules - add a ``scaleway`` group to use ``module_defaults`` (https://github.com/ansible-collections/community.general/pull/10647).
- scaleway_container - add a ``cpu_limit`` argument (https://github.com/ansible-collections/community.general/pull/10646).
- terraform - minor refactor to improve readability (https://github.com/ansible-collections/community.general/pull/10711).
- ufw - minor refactor to simplify string formatting (https://github.com/ansible-collections/community.general/pull/10727).
- xenserver module utils - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10769).
- xenserver_facts - minor refactor to simplify string formatting (https://github.com/ansible-collections/community.general/pull/10727).
- zfs_facts - minor refactor to simplify string formatting (https://github.com/ansible-collections/community.general/pull/10727).
- zypper - support the ``--gpg-auto-import-keys`` option in zypper (https://github.com/ansible-collections/community.general/issues/10660, https://github.com/ansible-collections/community.general/pull/10661).

community.mysql
~~~~~~~~~~~~~~~

- `mysql_query` - add new `session_vars` argument, similar to ansible-collections/community.mysql#489.

community.routeros
~~~~~~~~~~~~~~~~~~

- api_find_and_modify, api_modify - instead of comparing supplied values as-is to values retrieved from the API and converted to some types (int, bool) by librouteros, instead compare values by converting them to strings first, using similar conversion rules that librouteros uses (https://github.com/ansible-collections/community.routeros/issues/389, https://github.com/ansible-collections/community.routeros/issues/370, https://github.com/ansible-collections/community.routeros/issues/325, https://github.com/ansible-collections/community.routeros/issues/169, https://github.com/ansible-collections/community.routeros/pull/397).

community.vmware
~~~~~~~~~~~~~~~~

- vcenter_license - Add support for VCF license keys. (https://github.com/ansible-collections/community.vmware/pull/2451)
- vsphere_file - Remove ``ansible.module_utils.six.PY2`` (https://github.com/ansible-collections/community.vmware/pull/2475).

community.zabbix
~~~~~~~~~~~~~~~~

- repo role - Added proxy support when downloading RedHat GPG key.
- repo role - Added support for `zabbix_repo_deb_schema`
- repo role - defaulting `zabbix_repo_apt_priority` to 1001
- repo role - defaulting `zabbix_repo_version` to 7.4
- repo role - defaulting `zabbix_repo_yum_gpgcheck` to 1
- roles/agent, check to see if zabbix_agent_version_long is already supplied
- roles/agent, swap uri with win_uri
- server role - fixing zabbix_repo_package to repo role
- zabbix_agent - Removed zabbix_win_install_dir variable and replaced with zabbix_agent_win_install_dir
- zabbix_agent - Removed zabbix_win_install_dir_conf variable and replaced with zabbix_agent_win_install_dir_conf
- zabbix_maintenance - Added support for multiple outage periods within a single event
- zabbix_maintenance - Added support for recuring maintenance windows
- zabbix_script - Added support for type 'url'
- zabbix_script - Added support for user input.

containers.podman
~~~~~~~~~~~~~~~~~

- Add building Podman from source
- Add podman image scp option
- Add unittests for podman_image
- Improve docs and guides
- Rewrite podman_image and add tests
- Update docs and script

google.cloud
~~~~~~~~~~~~

- iap - enable use of Identity Aware Proxy ssh connections to compute instances (https://github.com/ansible-collections/google.cloud/pull/709).

hitachivantara.vspone_block
~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Added a new `"hv_sds_block_capacity_management_settings_facts"` module to retrieve capacity management settings from SDS block cluster.
- Added a new `"hv_sds_block_drive"` module to turn ON and Off the drive locator LED, remove a drive from SDS block cluster.
- Added a new `"hv_sds_block_storage_controller"` module to edit storage controller settings on SDS block cluster.
- Added a new `"hv_sds_block_storage_node_bmc_connection_facts"` module to retrieve BMC connection details from SDS block cluster.
- Added a new `"hv_sds_block_storage_pool_estimated_capacity_facts"` module to retrieve storage pool estimated capacity from SDS block cluster on AWS.
- Added a new `"hv_vsp_one_volume"` module to enable creation, modification, and deletion of volumes, as well as attaching and detaching to servers on VSP E series and VSP One B2X storages.
- Added a new `"hv_vsp_one_volume_facts"` module to retrieve volumes information from servers on VSP E series and VSP One B2X storages.
- Added support for SDS block cluster on Microsoft Azure.
- Added support to "Edit storage pool settings" to hv_sds_block_storage_pool module.
- Added support to "Edit the capacity balancing settings" to hv_sds_block_cluster module.
- Added support with new parameters "start_ldev", "end_ldev", "external_parity_groups" to hv_resource_group module.

ibm.storage_virtualize
~~~~~~~~~~~~~~~~~~~~~~

- ibm_sv_manage_flashsystem_grid - Added support for new FlashSystem grid APIs
- ibm_sv_manage_storage_partition - Added support for management portset and renaming partition
- ibm_sv_manage_truststore_for_replication - Added support for new FlashSystem grid APIs
- ibm_svc_hostcluster - Added support for partition and for managing host mappings during hostcluster deletion
- ibm_svc_info - Added support for new FlashSystem grid APIs
- ibm_svc_manage_ip - Changes for management portset
- ibm_svc_manage_portset - Added support for management portset
- ibm_svc_manage_volume - Added support for HA volumes volume expansion, volumegroup, volume rename and grainsize

purestorage.flasharray
~~~~~~~~~~~~~~~~~~~~~~

- plugins/module_utils/purefa.py - Removed ``get_system`` function as REST v1 no longer supported by Collection
- purefa_connect - Allow asynchronous FC-based replication
- purefa_default_protection - Added Fusion support.
- purefa_dsrole_old - Upgraded to REST v2
- purefa_info - Added new subsets ``workloads`` and ``presets``
- purefa_info - Converted to use REST 2
- purefa_network - Converted to REST v2
- purefa_ntp - Added Fusion support.
- purefa_pod - Added support for SafeMode protection group configuration
- purefa_policy - Upgraded to REST v2
- purefa_syslog - Added Fusion support.
- purefa_user - All AD users to have SSH keys and/or API tokens assigned, even if they have never accessed the FlashArray before. AD users must have ``ad_user`` set as ``true``.
- purefa_volume_tags - Add `tag` parameter to specify tag to be deleted by key name
- purefa_volume_tags - Upgraded to REST v2 and added Fusion support

purestorage.flashblade
~~~~~~~~~~~~~~~~~~~~~~

- purefb_ad - Revert removal of ``service`` parameter (breaking change). Added more logic to use of ``service`` parameter and recommend use of ``service_principals`` with service incorporated.
- purefb_ad - ``service`` parameter removed to comply with underlying API structure. ``service`` should be included in the ``service_principals`` strings as shown in the documentation.
- purefb_saml - Added ``entity_id`` parameter
- purefb_snap - Add support to delete/eradicate remote snapshots, including the latest replica
- purefb_user - All AD users to have SSH keys and/or API tokens assigned, even if they have never accessed the FlashArray before. AD users must have ``ad_user`` set as ``true``.

theforeman.foreman
~~~~~~~~~~~~~~~~~~

- content_upload - fall-back to rpm binary when library can't be imported
- registration_command - clarify example to show where the generated command needs to be executed

Breaking Changes / Porting Guide
--------------------------------

Ansible-core
~~~~~~~~~~~~

- powershell - Removed code that tried to remote quotes from paths when performing Windows operations like copying and fetching file. This should not affect normal playbooks unless a value is quoted too many times.

community.mysql
~~~~~~~~~~~~~~~

- Since version 4.0.0, the collection accepts code written in Python 3. Modules aren't tested against Python 2 and might not work in Python 2 environments.
- collection - stop testing against mysqlclient connector as its support was deprecated in this collection - use PyMySQL connector instead! It'll stop working in 5.0.0 when we remove all related code (https://github.com/ansible-collections/community.mysql/issues/654).
- mysql_db - the ``pipefail`` argument's default value is set to ``true``.  If your target machines do not use ``bash`` as a default interpreter, set ``pipefail`` to ``false`` explicitly. However, we strongly recommend setting up ``bash`` as a default and ``pipefail=true`` as it will protect you from getting broken dumps you don't know about (https://github.com/ansible-collections/community.mysql/issues/407).
- mysql_info - The ``users_info`` filter does not return the ``plugin_auth_string`` field anymore. Use the `plugin_hash_string` return value instead (https://github.com/ansible-collections/community.mysql/pull/629).
- mysql_role - the ``column_case_sensitive`` argument's default value has been changed to ``true``. If your playbook expected the column to be automatically uppercased for your users privileges, you should set this to ``false`` explicitly (https://github.com/ansible-collections/community.mysql/issues/578).
- mysql_user - the ``column_case_sensitive`` argument's default value has been changed to ``true``. If your playbook expected the column to be automatically uppercased for your users privileges, you should set this to ``false`` explicitly (https://github.com/ansible-collections/community.mysql/issues/577).

community.vmware
~~~~~~~~~~~~~~~~

- Removed support for ansible-core < 2.19.0.
- Removed support for vmware.vmware < 2.0.0.
- Replace the dependencies on ``pyvmomi``, ``vmware-vcenter`` and ``vmware-vapi-common-client`` with ``vcf-sdk`` (https://github.com/ansible-collections/community.vmware/pull/2457).

ibm.storage_virtualize
~~~~~~~~~~~~~~~~~~~~~~

- ibm_sv_manage_flashsystem_grid - The flashsystem grid module now uses newer FlashSystem REST APIs to perform tasks.

Deprecated Features
-------------------

Ansible-core
~~~~~~~~~~~~

- Deprecated the shell plugin's ``wrap_for_exec`` function. This API is not used in Ansible or any known collection and is being removed to simplify the plugin API. Plugin authors should wrap their command to execute within an explicit shell or other known executable.
- INJECT_FACTS_AS_VARS configuration currently defaults to ``True``, this is now deprecated and it will switch to ``False`` by Ansible 2.24. You will only get notified if you are accessing 'injected' facts (for example, ansible_os_distribution vs ansible_facts['os_distribution']).
- hash_params function in roles/__init__ is being deprecated as it is not in use.
- include_vars - Specifying 'ignore_files' as a string is deprecated.
- vars, the internal variable cache will be removed in 2.24. This cache, once used internally exposes variables in inconsistent states, the 'vars' and 'varnames' lookups should be used instead.

community.general
~~~~~~~~~~~~~~~~~

- hiera lookup plugin - retrieving data with Hiera has been deprecated a long time ago; because of that this plugin will be removed from community.general 13.0.0. If you disagree with this deprecation, please create an issue in the community.general repository (https://github.com/ansible-collections/community.general/issues/4462, https://github.com/ansible-collections/community.general/pull/10779).
- oci_utils module utils - utils is deprecated and will be removed in community.general 13.0.0 (https://github.com/ansible-collections/community.general/issues/10318, https://github.com/ansible-collections/community.general/pull/10652).
- oci_vcn - module is deprecated and will be removed in community.general 13.0.0 (https://github.com/ansible-collections/community.general/issues/10318, https://github.com/ansible-collections/community.general/pull/10652).
- oracle* doc fragments - fragments are deprecated and will be removed in community.general 13.0.0 (https://github.com/ansible-collections/community.general/issues/10318, https://github.com/ansible-collections/community.general/pull/10652).

community.vmware
~~~~~~~~~~~~~~~~

- vmware_guest_snapshot - the module has been deprecated and will be removed in community.vmware 8.0.0 (https://github.com/ansible-collections/community.vmware/pull/2467).

community.zabbix
~~~~~~~~~~~~~~~~

- zabbix_maintenance module - Depreicated `minutes` argument for `time_periods`

purestorage.flasharray
~~~~~~~~~~~~~~~~~~~~~~

- purefa_volume_tags - Deprecated due to removal of REST 1.x support. Will be removed in Collection 2.0.0

Removed Features (previously deprecated)
----------------------------------------

- The deprecated ``ibm.qradar`` collection has been removed (`https://forum.ansible.com/t/44259 <https://forum.ansible.com/t/44259>`__).

Ansible-core
~~~~~~~~~~~~

- Removed the option to set the ``DEFAULT_TRANSPORT`` configuration to ``smart`` that selects the default transport as either ``ssh`` or ``paramiko`` based on the underlying platform configuraton.
- ``vault``/``unvault`` filters - remove the deprecated ``vaultid`` parameter.
- ansible-doc - role entrypoint attributes are no longer shown
- ansible-galaxy - removed the v2 Galaxy server API. Galaxy servers hosting collections must support v3.
- dnf/dnf5 - remove deprecated ``install_repoquery`` option.
- encrypt - remove deprecated passlib_or_crypt API.
- paramiko - Removed the ``PARAMIKO_HOST_KEY_AUTO_ADD`` and ``PARAMIKO_LOOK_FOR_KEYS`` configuration keys, which were previously deprecated.
- py3compat - remove deprecated ``py3compat.environ`` call.
- vars plugins - removed the deprecated ``get_host_vars`` or ``get_group_vars`` fallback for vars plugins that do not inherit from ``BaseVarsPlugin`` and define a ``get_vars`` method.
- yum_repository - remove deprecated ``keepcache`` option.

community.vmware
~~~~~~~~~~~~~~~~

- vmware_cluster - The deprecated module has been removed. Use ``vmware.vmware.cluster`` instead (https://github.com/ansible-collections/community.vmware/pull/2455).
- vmware_cluster_dpm - The deprecated module has been removed. Use ``vmware.vmware.cluster_dpm`` instead (https://github.com/ansible-collections/community.vmware/pull/2455).
- vmware_cluster_drs - The deprecated module has been removed. Use ``vmware.vmware.cluster_drs`` instead (https://github.com/ansible-collections/community.vmware/pull/2455).
- vmware_cluster_drs_recommendations - The deprecated module has been removed. Use ``vmware.vmware.cluster_drs_recommendations`` instead (https://github.com/ansible-collections/community.vmware/pull/2455).
- vmware_cluster_vcls - The deprecated module has been removed. Use ``vmware.vmware.cluster_vcls`` instead (https://github.com/ansible-collections/community.vmware/pull/2455).

Bugfixes
--------

Ansible-core
~~~~~~~~~~~~

- Do not re-add ``tags`` on blocks from within ``import_tasks``.
- The ``ansible_failed_task`` variable is now correctly exposed in a rescue section, even when a failing handler is triggered by the ``flush_handlers`` task in the corresponding ``block`` (https://github.com/ansible/ansible/issues/85682)
- Windows async - Handle running PowerShell modules with trailing data after the module result
- ``ansible-galaxy collection list`` - fail when none of the configured collection paths exist.
- ``ternary`` filter - evaluate values lazily (https://github.com/ansible/ansible/issues/85743)
- ansible-doc --list/--list_files/--metadata-dump - fixed relative imports in nested filter/test plugin files (https://github.com/ansible/ansible/issues/85753).
- ansible-galaxy - Use the provided import task url, instead of parsing to get the task id and reconstructing the URL
- ansible-galaxy no longer shows the internal protomatter collection when listing.
- ansible-test - Always exclude the ``tests/output/`` directory from a collection's code coverage. (https://github.com/ansible/ansible/issues/84244)
- ansible-test - Fix a traceback that can occur when using delegation before the ansible-test temp directory is created.
- ansible-test - Limit package install retries during managed remote instance bootstrapping.
- ansible-test - Use a consistent coverage config for all collection testing.
- apt - mark dependencies installed as part of deb file installation as auto (https://github.com/ansible/ansible/issues/78123).
- argspec validation - The ``str`` argspec type treats ``None`` values as empty string for better consistency with pre-2.19 templating conversions.
- cache plugins - close temp cache file before moving it to fix error on WSL. (https://github.com/ansible/ansible/pull/85816)
- callback plugins - fix displaying the rendered ``ansible_host`` variable with ``delegate_to`` (https://github.com/ansible/ansible/issues/84922).
- callback plugins - improve consistency accessing the Task object's resolved_action attribute.
- conditionals - When displaying a broken conditional error or deprecation warning, the origin of the non-boolean result is included (if available), and the raw result is omitted.
- display - Fixed reference to undefined `_DeferredWarningContext` when issuing early warnings during startup. (https://github.com/ansible/ansible/issues/85886)
- dnf - Check if installroot is directory or not (https://github.com/ansible/ansible/issues/85680).
- failed_when - When using ``failed_when`` to suppress an error, the ``exception`` key in the result is renamed to ``failed_when_suppressed_exception``. This prevents the error from being displayed by callbacks after being suppressed. (https://github.com/ansible/ansible/issues/85505)
- import_tasks - fix templating parent include arguments.
- include_role - allow host specific values in all ``*_from`` arguments (https://github.com/ansible/ansible/issues/66497)
- pip - Fix pip module output so that it returns changed when the only operation is initializing a venv.
- plugins config, get_option_and_origin now correctly displays the value and origin of the option.
- run_command - Fixed premature selector unregistration on empty read from stdout/stderr that caused truncated output or hangs in rare situations.
- script inventory plugin will now show correct 'incorrect' type when doing implicit conversions on groups.
- ssh connection - fix documented variables for the ``host`` option. Connection options can be configured with delegated variables in general.
- template lookup - Skip finalization on the internal templating operation to allow markers to be returned and handled by, e.g. the ``default`` filter. Previously, finalization tripped markers, causing an exception to end processing of the current template pipeline. (https://github.com/ansible/ansible/issues/85674)
- templating - Avoid tripping markers within Jinja generated code. (https://github.com/ansible/ansible/issues/85674)
- templating - Ensure filter plugin result processing occurs under the correct call context. (https://github.com/ansible/ansible/issues/85585)
- templating - Fix slicing of tuples in templating (https://github.com/ansible/ansible/issues/85606).
- templating - Multi-node template results coerce embedded ``None`` nodes to empty string (instead of rendering literal ``None`` to the output).
- templating - Undefined marker values sourced from the Jinja ``getattr->getitem`` fallback are now accessed correctly, raising AnsibleUndefinedVariable for user plugins that do not understand markers. Previously, these values were erroneously returned to user plugin code that had not opted in to marker acceptance.
- tqm - use display.error_as_warning instead of display.warning_as_error.
- tqm - use display.error_as_warning instead of self.warning.
- uri - fix form-multipart file not being found when task is retried (https://github.com/ansible/ansible/issues/85009)
- validate-modules sanity test - fix handling of missing doc fragments (https://github.com/ansible/ansible/pull/85638).

cisco.meraki
~~~~~~~~~~~~

- cisco.meraki.devices_appliance_uplinks_settings - fix idempotency error.

community.dns
~~~~~~~~~~~~~

- Update Public Suffix List.

community.general
~~~~~~~~~~~~~~~~~

- kdeconfig - ``kwriteconfig`` executable could not be discovered automatically on systems with only ``kwriteconfig6`` installed. ``kwriteconfig6`` can now be discovered by Ansible (https://github.com/ansible-collections/community.general/issues/10746, https://github.com/ansible-collections/community.general/pull/10751).
- monit - fix crash caused by an unknown status value returned from the monit service (https://github.com/ansible-collections/community.general/issues/10742, https://github.com/ansible-collections/community.general/pull/10743).
- pacemaker - use regex for matching ``maintenance-mode`` output to determine cluster maintenance status (https://github.com/ansible-collections/community.general/issues/10426, https://github.com/ansible-collections/community.general/pull/10707).
- selective callback plugin - specify ``ansible_loop_var`` instead of the explicit value ``item`` when printing task result (https://github.com/ansible-collections/community.general/pull/10752).

community.routeros
~~~~~~~~~~~~~~~~~~

- api - allow querying for keys containing ``id``, as long as the key itself is not ``id`` (https://github.com/ansible-collections/community.routeros/issues/396, https://github.com/ansible-collections/community.routeros/pull/398).

community.vmware
~~~~~~~~~~~~~~~~

- vmware_guest_file_operation - fix ``replace() argument 2 must be str, not int`` error (https://github.com/ansible-collections/community.vmware/issues/2447).
- vmware_tools - fix ``replace() argument 2 must be str, not int`` error (https://github.com/ansible-collections/community.vmware/issues/2447).

community.zabbix
~~~~~~~~~~~~~~~~

- Proxy Role - Fixed a deprication error with `ProxyConfigFrequency`
- web role - Fixed a value test in nginx_vhost.conf
- zabbix_agent - Fix all variables related to windows installation paths
- zabbix_agent role - Fix windows paths to download and install zabbix agent msi
- zabbix_agent role - fixes too many requests to check latest zabbix release
- zabbix_maintenance - Fixed a bug that caused start time to update across multiple runs
- zabbix_template - Removed need for PY2
- zabbix_template_info - Removed need for PY2

containers.podman
~~~~~~~~~~~~~~~~~

- Fix podman logout for newer Podman
- Fix podman_image correct delimiter logic for version@digest tags
- Remove quiet mode from pulling image

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- idrac_server_config_profile - (Issue 959) Can't export SCP (Server configuration profile) on iDRAC 10. (https://github.com/dell/dellemc-openmanage-ansible-modules/issues/959)
- idrac_system_info - (Issue 967) - idrac_system_info fails on iDRAC10 with GPU. (https://github.com/dell/dellemc-openmanage-ansible-modules/issues/967)

google.cloud
~~~~~~~~~~~~

- gcp_compute_instance - add suppport for attaching disks to compute instances (https://github.com/ansible-collections/google.cloud/pull/711).
- gcp_secret_manager - use service_account_contents instead of service_account_info (https://github.com/ansible-collections/google.cloud/pull/703).

ibm.storage_virtualize
~~~~~~~~~~~~~~~~~~~~~~

- ibm_svc_mdiskgrp - Removed mandatory system mask setting during pool-linking

purestorage.flasharray
~~~~~~~~~~~~~~~~~~~~~~

- purefa_certs - Resolved error with incorrect use of ``key_size`` for imported certificates
- purefa_connect - Ensured that encrypted connections use encrypted connection keys
- purefa_eradication - Fixed idempotency issue
- purefa_eula - Fix AttributeError when first sogning EULA
- purefa_host - Fixed Pydantic error when updating preferred_arrays
- purefa_info - Ensured that volumes, hosts, host_groups and transfers are correctly listed for protection groups
- purefa_info - Fixed AttributeError in config section related to SSO SAML2
- purefa_info - Fixed issue with replication connection throttle reporting
- purefa_info - Fixed issue with undo-demote pods not reporting correctly
- purefa_info - Resolved AttributeError in volume subset
- purefa_network - Resolve typo that causes network updates to not apply correctly
- purefa_pg - Changing target for PG no longer requires a ``FixedReference``
- purefa_subnet - Fixed failure when trying to update a subnet with no gateway defined

purestorage.flashblade
~~~~~~~~~~~~~~~~~~~~~~

- purefb_ad - Fixed issue where updating an AD account required unnecessary parameters.
- purefb_bucket - Fix versioning control and access rules for public buckets
- purefb_bucket - Fixed issue where a bucket with no versioning defined was incorrectly created.
- purefb_bucket - Fixed issue with default retention parameter
- purefb_bucket_access - Fixed typo in CORS rule definition
- purefb_certs - Fixed issues with importing external certificates
- purefb_certs - Updated email regex pattern to fix ``re`` failures
- purefb_dns - Fixed multiple issues for data DNS configuration
- purefb_fs - Ensured that NFS rules are emprty if requested filesystem is SMB only
- purefb_info - Fixed error when ``default`` subset fails if SMD has been disabled on the FLashBlade
- purefb_policy - Fixed typo when calling object store policy rule deletion
- purefb_s3user - Fixed typo in imported keys code
- purefb_subnet - Ensured prefix is required for subnet creation or update

Known Issues
------------

Ansible-core
~~~~~~~~~~~~

- templating - Exceptions raised in a Jinja ``set`` or ``with`` block which are not accessed by the template are ignored in the same manner as undefined values.
- templating - Passing a container created in a Jinja ``set`` or ``with`` block to a method results in a copy of that container. Mutations to that container which are not returned by the method will be discarded.

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- idrac_attributes - The module accepts both the string as well as integer value for the field "SNMP.1.AgentCommunity" for iDRAC10.
- idrac_diagnostics - This module does not support export of diagnostics file to HTTP and HTTPS share via SOCKS proxy.
- idrac_license - Due to API limitation, proxy parameters are ignored during the import operation.
- idrac_license - The module will fail to export license to NFS Share.
- idrac_license - The module will give different error messages for iDRAC9 and iDRAC10 when user imports license with invalid share name.
- idrac_os_deployment - The module continues to return a 200 response and marks the job as completed, even when an outdated date is supplied in the Expose duration.
- idrac_redfish_storage_controller - PatrolReadRatePercent attribute cannot be set in iDRAC10.
- idrac_server_config_profile - When attempting to revert iDRAC settings using a previously exported SCP file, the import operation will complete with errors if a new user was created after the export (Instead of restoring the system to its previous state, including the removal of newly added users).
- idrac_system_info - The module will show empty video list despite having Embedded VIDEO controller.
- ome_smart_fabric_uplink - The module supported by OpenManage Enterprise Modular, however it does not allow the creation of multiple uplinks of the same name. If an uplink is created using the same name as an existing uplink, then the existing uplink is modified.
- redfish_storage_volume - Encryption type and block_io_size bytes will be read only property in iDRAC 9 and iDRAC 10 and hence the module ignores these parameters.

New Plugins
-----------

Filter
~~~~~~

- community.general.to_nice_yaml - Convert variable to YAML string.
- community.general.to_yaml - Convert variable to YAML string.

Inventory
~~~~~~~~~

- containers.podman.buildah_containers - Inventory plugin that discovers Buildah working containers as hosts
- containers.podman.podman_containers - Inventory plugin that discovers Podman containers as hosts

New Modules
-----------

check_point.mgmt
~~~~~~~~~~~~~~~~

- check_point.mgmt.cp_mgmt_identity_provider - Manages identity-provider objects on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_identity_provider_facts - Get identity-provider objects facts on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_if_map_server - Manages if-map-server objects on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_if_map_server_facts - Get if-map-server objects facts on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_ldap_group - Manages ldap-group objects on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_ldap_group_facts - Get ldap-group objects facts on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_log_exporter - Manages log-exporter objects on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_log_exporter_facts - Get log-exporter objects facts on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_resource_mms - Manages resource-mms objects on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_resource_mms_facts - Get resource-mms objects facts on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_resource_tcp - Manages resource-tcp objects on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_resource_tcp_facts - Get resource-tcp objects facts on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_resource_uri_for_qos - Manages resource-uri-for-qos objects on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_resource_uri_for_qos_facts - Get resource-uri-for-qos objects facts on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_run_app_control_update - Runs Application Control & URL Filtering database update.
- check_point.mgmt.cp_mgmt_securemote_dns_server - Manages securemote-dns-server objects on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_securemote_dns_server_facts - Get securemote-dns-server objects facts on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_securid_server - Manages securid-server objects on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_securid_server_facts - Get securid-server objects facts on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_set_anti_malware_update_schedule - Set both Anti-Bot and Anti-Virus update schedules.
- check_point.mgmt.cp_mgmt_set_app_control_update_schedule - Set the Application Control and URL Filtering update schedule.
- check_point.mgmt.cp_mgmt_show_anti_malware_update_schedule - Retrieve existing Anti-Bot and Anti-Virus update schedules.
- check_point.mgmt.cp_mgmt_show_app_control_status - Get app-control-status objects facts on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_show_app_control_update_schedule - Get app-control-status objects facts on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_syslog_server - Manages syslog-server objects on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_syslog_server_facts - Get syslog-server objects facts on Checkpoint over Web Services API

community.general
~~~~~~~~~~~~~~~~~

- community.general.django_dumpdata - Wrapper for C(django-admin dumpdata).
- community.general.django_loaddata - Wrapper for C(django-admin loaddata).
- community.general.pacemaker_stonith - Manage Pacemaker STONITH.

containers.podman
~~~~~~~~~~~~~~~~~

- containers.podman.podman_system_connection - Manage Podman system connections
- containers.podman.podman_system_connection_info - Get info about Podman system connections

hitachivantara.vspone_block
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Sds Block
^^^^^^^^^

- hitachivantara.vspone_block.hv_sds_block_capacity_management_settings_facts - Get capacity management settings from storage system.
- hitachivantara.vspone_block.hv_sds_block_drive - Manages drive on Hitachi SDS Block storage systems.
- hitachivantara.vspone_block.hv_sds_block_storage_controller - Edits the settings for the storage controller on Hitachi SDS Block storage systems.
- hitachivantara.vspone_block.hv_sds_block_storage_node_bmc_connection_facts - Get storage node BMC access settings from storage system.
- hitachivantara.vspone_block.hv_sds_block_storage_pool_estimated_capacity_facts - Obtains the preliminary calculation results of the storage pool logical capacity (unit TiB).

Vsp
^^^

- hitachivantara.vspone_block.hv_vsp_one_volume - Manages volumes on Hitachi VSP One storage systems.
- hitachivantara.vspone_block.hv_vsp_one_volume_facts - Retrieves facts about Hitachi VSP One storage system volumes.

Unchanged Collections
---------------------

- amazon.aws (still version 10.1.1)
- ansible.netcommon (still version 8.1.0)
- ansible.posix (still version 2.1.0)
- ansible.utils (still version 6.0.0)
- ansible.windows (still version 3.2.0)
- arista.eos (still version 12.0.0)
- awx.awx (still version 24.6.1)
- azure.azcollection (still version 3.8.0)
- chocolatey.chocolatey (still version 1.5.3)
- cisco.aci (still version 2.12.0)
- cisco.ios (still version 11.0.0)
- cisco.iosxr (still version 12.0.0)
- cisco.mso (still version 2.11.0)
- cisco.nxos (still version 11.0.0)
- cisco.ucs (still version 1.16.0)
- cloudscale_ch.cloud (still version 2.5.2)
- community.aws (still version 10.0.0)
- community.ciscosmb (still version 1.0.11)
- community.crypto (still version 3.0.3)
- community.digitalocean (still version 1.27.0)
- community.docker (still version 4.7.0)
- community.grafana (still version 2.3.0)
- community.hashi_vault (still version 7.0.0)
- community.hrobot (still version 2.5.0)
- community.library_inventory_filtering_v1 (still version 1.1.1)
- community.libvirt (still version 2.0.0)
- community.mongodb (still version 1.7.10)
- community.okd (still version 5.0.0)
- community.postgresql (still version 4.1.0)
- community.proxmox (still version 1.3.0)
- community.proxysql (still version 1.6.0)
- community.rabbitmq (still version 1.6.0)
- community.sap_libs (still version 1.4.2)
- community.sops (still version 2.2.2)
- community.windows (still version 3.0.1)
- cyberark.conjur (still version 1.3.7)
- cyberark.pas (still version 1.0.35)
- dellemc.enterprise_sonic (still version 3.0.0)
- dellemc.powerflex (still version 2.6.1)
- dellemc.unity (still version 2.1.0)
- f5networks.f5_modules (still version 1.38.0)
- fortinet.fortimanager (still version 2.10.0)
- fortinet.fortios (still version 2.4.0)
- grafana.grafana (still version 6.0.3)
- hetzner.hcloud (still version 5.2.0)
- ieisystem.inmanage (still version 3.0.0)
- infinidat.infinibox (still version 1.6.3)
- infoblox.nios_modules (still version 1.8.0)
- inspur.ispim (still version 2.2.3)
- junipernetworks.junos (still version 11.0.0)
- kaytus.ksmanage (still version 2.0.0)
- kubernetes.core (still version 6.1.0)
- kubevirt.core (still version 2.2.3)
- lowlydba.sqlserver (still version 2.7.0)
- microsoft.ad (still version 1.9.2)
- microsoft.iis (still version 1.0.3)
- netapp.cloudmanager (still version 21.24.0)
- netapp.ontap (still version 23.1.0)
- netapp.storagegrid (still version 21.15.0)
- netapp_eseries.santricity (still version 1.4.1)
- netbox.netbox (still version 3.21.0)
- ngine_io.cloudstack (still version 2.5.0)
- openstack.cloud (still version 2.4.1)
- ovirt.ovirt (still version 3.2.1)
- splunk.es (still version 4.0.0)
- telekom_mms.icinga_director (still version 2.4.0)
- vmware.vmware (still version 2.3.0)
- vmware.vmware_rest (still version 4.9.0)
- vultr.cloud (still version 1.13.0)
- vyos.vyos (still version 6.0.0)
- wti.remote (still version 1.0.10)
