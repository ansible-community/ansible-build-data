=======================
Ansible 8 Release Notes
=======================

This changelog describes changes since Ansible 7.0.0.

.. contents::
  :local:
  :depth: 2

v8.6.1
======

.. contents::
  :local:
  :depth: 2

Release Summary
---------------

Release Date: 2023-11-09

`Porting Guide <https://docs.ansible.com/ansible/devel/porting_guides.html>`_

Ansible-core
------------

Ansible 8.6.1 contains ansible-core version 2.15.6.
This is the same version of ansible-core as in the previous Ansible release.


Changed Collections
-------------------

If not mentioned explicitly, the changes are reported in the combined changelog below.

+--------------+---------------+---------------+-------+
| Collection   | Ansible 8.6.0 | Ansible 8.6.1 | Notes |
+==============+===============+===============+=======+
| netapp.ontap | 22.8.0        | 22.8.2        |       |
+--------------+---------------+---------------+-------+

Bugfixes
--------

netapp.ontap
~~~~~~~~~~~~

- na_ontap_dns - fix keyerror for uuid when DNS is set to vserver in REST.
- na_ontap_volume - fix invalid field error with 'space.snapshot.autodelete' in REST.

Unchanged Collections
---------------------

- amazon.aws (still version 6.5.0)
- ansible.netcommon (still version 5.3.0)
- ansible.posix (still version 1.5.4)
- ansible.utils (still version 2.11.0)
- ansible.windows (still version 1.14.0)
- arista.eos (still version 6.2.1)
- awx.awx (still version 22.7.0)
- azure.azcollection (still version 1.19.0)
- check_point.mgmt (still version 5.1.1)
- chocolatey.chocolatey (still version 1.5.1)
- cisco.aci (still version 2.8.0)
- cisco.asa (still version 4.0.3)
- cisco.dnac (still version 6.7.6)
- cisco.intersight (still version 1.0.27)
- cisco.ios (still version 4.6.1)
- cisco.iosxr (still version 5.0.3)
- cisco.ise (still version 2.5.16)
- cisco.meraki (still version 2.16.13)
- cisco.mso (still version 2.5.0)
- cisco.nso (still version 1.0.3)
- cisco.nxos (still version 4.4.0)
- cisco.ucs (still version 1.10.0)
- cloud.common (still version 2.1.4)
- cloudscale_ch.cloud (still version 2.3.1)
- community.aws (still version 6.4.0)
- community.azure (still version 2.0.0)
- community.ciscosmb (still version 1.0.7)
- community.crypto (still version 2.16.0)
- community.digitalocean (still version 1.24.0)
- community.dns (still version 2.6.3)
- community.docker (still version 3.4.10)
- community.fortios (still version 1.0.0)
- community.general (still version 7.5.1)
- community.google (still version 1.0.0)
- community.grafana (still version 1.6.1)
- community.hashi_vault (still version 5.0.1)
- community.hrobot (still version 1.8.1)
- community.libvirt (still version 1.3.0)
- community.mongodb (still version 1.6.3)
- community.mysql (still version 3.8.0)
- community.network (still version 5.0.2)
- community.okd (still version 2.3.0)
- community.postgresql (still version 2.4.3)
- community.proxysql (still version 1.5.1)
- community.rabbitmq (still version 1.2.3)
- community.routeros (still version 2.10.0)
- community.sap (still version 1.0.0)
- community.sap_libs (still version 1.4.1)
- community.skydive (still version 1.0.0)
- community.sops (still version 1.6.7)
- community.vmware (still version 3.11.1)
- community.windows (still version 1.13.0)
- community.zabbix (still version 2.1.0)
- containers.podman (still version 1.11.0)
- cyberark.conjur (still version 1.2.2)
- cyberark.pas (still version 1.0.23)
- dellemc.enterprise_sonic (still version 2.2.0)
- dellemc.openmanage (still version 7.6.1)
- dellemc.powerflex (still version 1.9.0)
- dellemc.unity (still version 1.7.1)
- f5networks.f5_modules (still version 1.27.0)
- fortinet.fortimanager (still version 2.3.0)
- fortinet.fortios (still version 2.3.4)
- frr.frr (still version 2.0.2)
- gluster.gluster (still version 1.0.2)
- google.cloud (still version 1.2.0)
- grafana.grafana (still version 2.2.3)
- hetzner.hcloud (still version 1.16.0)
- hpe.nimble (still version 1.1.4)
- ibm.qradar (still version 2.1.0)
- ibm.spectrum_virtualize (still version 1.12.0)
- ibm.storage_virtualize (still version 2.1.0)
- infinidat.infinibox (still version 1.3.12)
- infoblox.nios_modules (still version 1.5.0)
- inspur.ispim (still version 1.3.0)
- inspur.sm (still version 2.3.0)
- junipernetworks.junos (still version 5.3.0)
- kubernetes.core (still version 2.4.0)
- lowlydba.sqlserver (still version 2.2.2)
- microsoft.ad (still version 1.3.0)
- netapp.aws (still version 21.7.1)
- netapp.azure (still version 21.10.1)
- netapp.cloudmanager (still version 21.22.1)
- netapp.elementsw (still version 21.7.0)
- netapp.storagegrid (still version 21.11.1)
- netapp.um_info (still version 21.8.1)
- netapp_eseries.santricity (still version 1.4.0)
- netbox.netbox (still version 3.15.0)
- ngine_io.cloudstack (still version 2.3.0)
- ngine_io.exoscale (still version 1.1.0)
- ngine_io.vultr (still version 1.1.3)
- openstack.cloud (still version 2.1.0)
- openvswitch.openvswitch (still version 2.1.1)
- ovirt.ovirt (still version 3.2.0)
- purestorage.flasharray (still version 1.21.0)
- purestorage.flashblade (still version 1.14.0)
- purestorage.fusion (still version 1.6.0)
- sensu.sensu_go (still version 1.14.0)
- servicenow.servicenow (still version 1.0.6)
- splunk.es (still version 2.1.0)
- t_systems_mms.icinga_director (still version 1.33.1)
- telekom_mms.icinga_director (still version 1.34.1)
- theforeman.foreman (still version 3.14.0)
- vmware.vmware_rest (still version 2.3.1)
- vultr.cloud (still version 1.10.0)
- vyos.vyos (still version 4.1.0)
- wti.remote (still version 1.0.5)

v8.6.0
======

.. contents::
  :local:
  :depth: 2

Release Summary
---------------

Release Date: 2023-11-07

`Porting Guide <https://docs.ansible.com/ansible/devel/porting_guides.html>`_

Added Collections
-----------------

- ibm.storage_virtualize (version 2.1.0)

Ansible-core
------------

Ansible 8.6.0 contains ansible-core version 2.15.6.
This is a newer version than version 2.15.5 contained in the previous Ansible release.

The changes are reported in the combined changelog below.

Changed Collections
-------------------

If not mentioned explicitly, the changes are reported in the combined changelog below.

+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| Collection             | Ansible 8.5.0 | Ansible 8.6.0 | Notes                                                                                                                        |
+========================+===============+===============+==============================================================================================================================+
| ansible.netcommon      | 5.2.0         | 5.3.0         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| arista.eos             | 6.1.2         | 6.2.1         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| azure.azcollection     | 1.18.1        | 1.19.0        | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.aci              | 2.7.0         | 2.8.0         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.asa              | 4.0.2         | 4.0.3         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.dnac             | 6.7.5         | 6.7.6         | The collection did not have a changelog in this version.                                                                     |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.meraki           | 2.16.5        | 2.16.13       |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.aws          | 6.3.0         | 6.4.0         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.ciscosmb     | 1.0.6         | 1.0.7         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.crypto       | 2.15.1        | 2.16.0        |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.dns          | 2.6.2         | 2.6.3         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.docker       | 3.4.9         | 3.4.10        |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.general      | 7.5.0         | 7.5.1         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.grafana      | 1.5.4         | 1.6.1         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.hashi_vault  | 5.0.0         | 5.0.1         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.mysql        | 3.7.2         | 3.8.0         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.network      | 5.0.0         | 5.0.2         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.sops         | 1.6.6         | 1.6.7         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.vmware       | 3.10.0        | 3.11.1        |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| containers.podman      | 1.10.3        | 1.11.0        |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| f5networks.f5_modules  | 1.26.0        | 1.27.0        |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| fortinet.fortimanager  | 2.2.1         | 2.3.0         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| fortinet.fortios       | 2.3.2         | 2.3.4         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| ibm.storage_virtualize |               | 2.1.0         | The collection was added to Ansible                                                                                          |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| lowlydba.sqlserver     | 2.2.1         | 2.2.2         | The collection did not have a changelog in this version.                                                                     |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| netapp.aws             | 21.7.0        | 21.7.1        | The collection did not have a changelog in this version.                                                                     |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| netapp.azure           | 21.10.0       | 21.10.1       | The collection did not have a changelog in this version.                                                                     |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| netapp.cloudmanager    | 21.22.0       | 21.22.1       | The collection did not have a changelog in this version.                                                                     |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| netapp.ontap           | 22.7.0        | 22.8.0        |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| netapp.um_info         | 21.8.0        | 21.8.1        | The collection did not have a changelog in this version.                                                                     |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| netbox.netbox          | 3.14.0        | 3.15.0        |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+

Major Changes
-------------

community.mysql
~~~~~~~~~~~~~~~

- The community.mysql collection no longer supports ``ansible-core 2.12`` and ``ansible-core 2.13``. While we take no active measures to prevent usage and there are no plans to introduce incompatible code to the modules, we will stop testing those versions. Both are or will soon be End of Life and if you are still using them, you should consider upgrading to the ``latest Ansible / ansible-core 2.15 or later`` as soon as possible (https://github.com/ansible-collections/community.mysql/pull/574).
- mysql_role - the ``column_case_sensitive`` argument's default value will be changed to ``true`` in community.mysql 4.0.0. If your playbook expected the column to be automatically uppercased for your roles privileges, you should set this to false explicitly (https://github.com/ansible-collections/community.mysql/issues/578).
- mysql_user - the ``column_case_sensitive`` argument's default value will be changed to ``true`` in community.mysql 4.0.0. If your playbook expected the column to be automatically uppercased for your users privileges, you should set this to false explicitly (https://github.com/ansible-collections/community.mysql/issues/577).

fortinet.fortios
~~~~~~~~~~~~~~~~

- Add new fortios version 7.4.1.
- Format the contents in the changelog.yml file.
- Update Ansible version from 2.9 to 2.14.
- Update Q&A with a resolution for Ansible Always Sending GET/PUT Requests as POST Requests.
- Update the requirement.txt file to specify the sphinx_rtd_theme==1.3.0
- update the required Ansible version to 2.14.0 in the runtime.yml file.

Minor Changes
-------------

Ansible-core
~~~~~~~~~~~~

- ansible-test - Windows 2012 and 2012-R2 instances are now requested from Azure instead of AWS.

ansible.netcommon
~~~~~~~~~~~~~~~~~

- Add new module cli_backup that exclusively handles configuration backup.

arista.eos
~~~~~~~~~~

- arista_config - Relax restrictions on I(src) parameter so it can be used more like I(lines).

cisco.aci
~~~~~~~~~

- Add 8.0 option for dvs_version attribute in aci_vmm_controller
- Add Match Rules for aci_route_control_profile modules
- Add aci_bgp_timers_policy and aci_bgp_best_path_policy modules
- Add aci_fabric_interface_policy_group module
- Add aci_interface_policy_leaf_fc_policy_group and aci_interface_policy_spine_policy_group module
- Add aci_l3out_bgp_protocol_profile module
- Add aci_match_community_factor module.
- Add aci_route_control_context and aci_match_rule modules
- Add aci_route_control_profile module
- Add hmac-sha2-224, hmac-sha2-256, hmac-sha2-384, hmac-sha2-512 authentication types and description to aci_snmp_user module
- Add loopback interface profile as a child class for aci_l3out_logical_node.
- Add missing attributes in aci_interface_policy_leaf_policy_group
- Add missing attributes to aci_l3out_extepg module
- Add missing test cases, fix found issues and add missing attributes for aci_fabric_scheduler, aci_firmware_group, aci_firmware_group_node, aci_firmware_policy, aci_interface_policy_fc, aci_interface_policy_lldp, aci_interface_policy_mcp, aci_interface_policy_ospf, aci_interface_policy_port_channel, aci_maintenance_group, aci_maintenance_group_node, aci_maintenance_policy and aci_tenant_ep_retention_policy modules (#453)
- Add support for checkmode in aci_rest module
- Add support for configuration of fabric node control with aci_fabric_node_control module
- Add support for configuration of fabric pod selectors with aci_fabric_pod_selector module
- Add support for configuration of system banner and alias with aci_system_banner module
- Add support for configuration of system endpoint controls, ip aging, ep loop protection and roque endpoint control with aci_system_endpoint_controls module
- Add support for configuration of system fabric wide settings with aci_fabric_wide_settings module
- Add support for configuration of system global aes passphrase encryption with aci_system_global_aes_passphrase_encryption module
- Add support for global infra dhcp relay policy configuration in aci_dhcp_relay
- Add support for global infra dhcp relay policy configuration in aci_dhcp_relay_provider

community.aws
~~~~~~~~~~~~~

- ecs_taskdefinition - Add parameter ``runtime_platform`` (https://github.com/ansible-collections/community.aws/issues/1891).

community.crypto
~~~~~~~~~~~~~~~~

- luks_devices - add new options ``keyslot``, ``new_keyslot``, and ``remove_keyslot`` to allow adding/removing keys to/from specific keyslots (https://github.com/ansible-collections/community.crypto/pull/664).

community.grafana
~~~~~~~~~~~~~~~~~

- Add `grafana_organization_user` module
- Bump version of Python used in tests to 3.10
- Enable datasource option `time_interval` for prometheus
- Fix documentation url for Ansible doc website
- Now testing against Grafana 9.5.13, 8.5.27, 10.2.0

community.mysql
~~~~~~~~~~~~~~~

- mysql_info - add filter ``users_info`` (https://github.com/ansible-collections/community.mysql/pull/580).
- mysql_role - add ``column_case_sensitive`` option to prevent field names from being uppercased (https://github.com/ansible-collections/community.mysql/pull/569).
- mysql_user - add ``column_case_sensitive`` option to prevent field names from being uppercased (https://github.com/ansible-collections/community.mysql/pull/569).

community.vmware
~~~~~~~~~~~~~~~~

- community.vmware.vmware_host_snmp module now can configure SNMP agent on set of hosts (list in esxi_hostname parameter or as cluster in cluster_name parameter). The ability to configure the host directly remains
- vmware_deploy_ovf - New parameter enable_hidden_properties to force OVF properties marked as ovf:userConfigurable=false to become user configurable (https://github.com/ansible-collections/community.vmware/issues/802).

containers.podman
~~~~~~~~~~~~~~~~~

- Update docs
- podman_container - Add support for health-on-failure action
- podman_image -Add target support for podman build image
- podman_play - Add build and context_dir option to podman_play
- podman_pod - Add options for resource limits to podman_pod

f5networks.f5_modules
~~~~~~~~~~~~~~~~~~~~~

- bigip_policy_rule - added six more options for ssl_extension condition

fortinet.fortimanager
~~~~~~~~~~~~~~~~~~~~~

- Some arguments can support both list or string format input now.
- Support newest versions for FortiManager v6.2 ~ v7.4

netapp.ontap
~~~~~~~~~~~~

- na_ontap_broadcast_domain - changed documentation for ipspace as it is required while using REST.
- na_ontap_cg_snapshot - added REST support to the cg snapshot module, requires ONTAP 9.10.1 or later.
- na_ontap_cifs_server - new option `default_site` added in REST, requires ONTAP 9.13.1 or later.
- na_ontap_ems_destination - new option ``certificate``, ``ca`` added.
- na_ontap_kerberos_realm - add REST support for `admin_server_ip`, `admin_server_port`, `pw_server_ip`, `pw_server_port` and `clock_skew` from ONTAP 9.13.1 or later
- na_ontap_lun - new option `qtree_name` added in REST.
- na_ontap_net_ifgrp - return `name` and other details of a newly created interface group in module output in REST.
- na_ontap_qos_policy_group - added new REST only options `expected_iops_allocation` and `peak_iops_allocation`, requires ONTAP 9.10.1 or later.
- na_ontap_rest_info - new option `hal_linking` added to enable or disable HAL links.
- na_ontap_restit - returns changed as False for GET method.
- na_ontap_snmp - added REST support for snmpv3 user.
- na_ontap_user - Added warning message when password is not changed.
- na_ontap_volume - added REST support for `atime_update` requires ONTAP 9.8 or later, `snapdir_access` and `snapshot_auto_delete` requires ONTAP 9.13.1 or later.
- na_ontap_volume - added new REST only options `vol_nearly_full_threshold_percent` and `vol_full_threshold_percent`, requires ONTAP 9.9 or later.

netbox.netbox
~~~~~~~~~~~~~

- netbox_config_template - New module [#1090](https://github.com/netbox-community/ansible_modules/pull/1090)
- netbox_device - Add oob_ip to device [#1085](https://github.com/netbox-community/ansible_modules/pull/1085)
- netbox_device_type - Add default_platform [#1092](https://github.com/netbox-community/ansible_modules/pull/1092)

Deprecated Features
-------------------

- The collection ``ibm.spectrum_virtualize`` has been renamed to ``ibm.storage_virtualize``. For now, both collections are included in Ansible. The content in ``ibm.spectrum_virtualize`` will be replaced with deprecated redirects to the new collection in Ansible 10.0.0, and these redirects will eventually be removed from Ansible. Please update your FQCNs for ``ibm.spectrum_virtualize``.

Bugfixes
--------

Ansible-core
~~~~~~~~~~~~

- Fix ``run_once`` being incorrectly interpreted on handlers (https://github.com/ansible/ansible/issues/81666)
- Plugin loader does not dedupe nor cache filter/test plugins by file basename, but full path name.
- Properly template tags in parent blocks (https://github.com/ansible/ansible/issues/81053)
- Restoring the ability of filters/tests can have same file base name but different tests/filters defined inside.
- ``import_role`` reverts to previous behavior of exporting vars at compile time.
- ansible-galaxy - Provide a better error message when using a requirements file with an invalid format - https://github.com/ansible/ansible/issues/81901
- ansible-inventory - index available_hosts for major performance boost when dumping large inventories
- ansible-test - Fix parsing of cgroup entries which contain a ``:`` in the path (https://github.com/ansible/ansible/issues/81977).

ansible.netcommon
~~~~~~~~~~~~~~~~~

- Fix attribute types from string to str in filter plugins.

arista.eos
~~~~~~~~~~

- Fix command generated for local-interface with in ntp server attribute.
- Fix command generation for source_interface attribute.
- Fix secondary ip address parsing.
- fix line attribute fact generation and placement in ACE, when ACE is not fully parsed.

cisco.aci
~~~~~~~~~

- Fixed issue with default values for ssl, proxy, timeout in aci.py and the display of host in the url when the plugin httpapi is used
- Modified  aci_rest  and  aci_config_snapshot  modules to display the correct URL output string (#487)

cisco.meraki
~~~~~~~~~~~~

- Bad naming `networkId` parameter in `networks_appliance_traffic_shaping_custom_performance_classes`.
- Bad naming `networkId` parameter in `networks_appliance_warm_spare_swap`.
- Bad naming `networkId` parameter in `networks_bind`.
- Bad naming `networkId` parameter in `networks_clients_provision`.
- Bad naming `networkId` parameter in `networks_devices_remove` and `networks_devices_claim_vmx`
- Bad naming `networkId` parameter in `networks_firmware_upgrades_rollbacks`.
- Bad naming `networkId` parameter in `networks_firmware_upgrades_staged_events_rollbacks`.
- Bad naming `networkId` parameter in `networks_mqtt_brokers`.
- Bad naming `networkId` parameter in `networks_pii_requests_delete`.
- Bad naming `networkId` parameter in `networks_sm_devices_checkin`.
- Bad naming `networkId` parameter in `networks_sm_devices_fields`.
- Bad naming `networkId` parameter in `networks_sm_devices_lock`.
- Bad naming `networkId` parameter in `networks_sm_devices_modify_tags`.
- Bad naming `networkId` parameter in `networks_sm_devices_move`.
- Bad naming `networkId` parameter in `networks_sm_devices_refresh_details`.
- Bad naming `networkId` parameter in `networks_sm_devices_unenroll`.
- Bad naming `networkId` parameter in `networks_sm_devices_wipe`.
- Bad naming `networkId` parameter in `networks_sm_user_access_devices_delete`.
- Bad naming `networkId` parameter in `networks_split`.
- Bad naming `networkId` parameter in `networks_switch_stacks_add`.
- Bad naming `networkId` parameter in `networks_switch_stacks_remove`.
- Bad naming `networkId` parameter in `networks_unbind`.
- Devices module documentation fixed.
- Meraki Compare Equality 2 added.
- New condition added to Meraki Compare Equality.
- Returning requires_ansible to 2.9.10
- Returning requires_ansible to >=2.14.0
- Sanity fixes.
- runtime updated requires_ansible from 2.9.10 to '>=2.14.0'.

community.ciscosmb
~~~~~~~~~~~~~~~~~~

- added Cisco device config guide to address issue
- added extra "\n" to sending commands to address issue

community.crypto
~~~~~~~~~~~~~~~~

- openssl_pkcs12 - modify autodetect to not detect pyOpenSSL >= 23.3.0, which removed PKCS#12 support (https://github.com/ansible-collections/community.crypto/pull/666).

community.dns
~~~~~~~~~~~~~

- HTTP module utils - make compatible with ansible-core 2.17 (https://github.com/ansible-collections/community.dns/pull/165).
- Update Public Suffix List.

community.docker
~~~~~~~~~~~~~~~~

- docker_swarm - make init and join operations work again with Docker SDK for Python before 4.0.0 (https://github.com/ansible-collections/community.docker/issues/695, https://github.com/ansible-collections/community.docker/pull/696).

community.general
~~~~~~~~~~~~~~~~~

- composer - fix impossible to run ``working_dir`` dependent commands. The module was throwing an error when trying to run a ``working_dir`` dependent command, because it tried to get the command help without passing the ``working_dir`` (https://github.com/ansible-collections/community.general/issues/3787).
- github_deploy_key - fix pagination behaviour causing a crash when only a single page of deploy keys exist (https://github.com/ansible-collections/community.general/pull/7375).
- gitlab_group_members - fix gitlab constants call in ``gitlab_group_members`` module (https://github.com/ansible-collections/community.general/issues/7467).
- gitlab_project_members - fix gitlab constants call in ``gitlab_project_members`` module (https://github.com/ansible-collections/community.general/issues/7467).
- gitlab_protected_branches - fix gitlab constants call in ``gitlab_protected_branches`` module (https://github.com/ansible-collections/community.general/issues/7467).
- gitlab_user - fix gitlab constants call in ``gitlab_user`` module (https://github.com/ansible-collections/community.general/issues/7467).
- kernel_blacklist - simplified the mechanism to update the file, fixing the error (https://github.com/ansible-collections/community.general/pull/7382, https://github.com/ansible-collections/community.general/issues/7362).
- memset module utils - make compatible with ansible-core 2.17 (https://github.com/ansible-collections/community.general/pull/7379).
- proxmox_pool_member - absent state for type VM did not delete VMs from the pools (https://github.com/ansible-collections/community.general/pull/7464).
- redfish_command - fix usage of message parsing in ``SimpleUpdate`` and ``MultipartHTTPPushUpdate`` commands to treat the lack of a ``MessageId`` as no message (https://github.com/ansible-collections/community.general/issues/7465, https://github.com/ansible-collections/community.general/pull/7471).
- redhat_subscription - use the right D-Bus options for the consumer type when
  registering a RHEL system older than 9 or a RHEL 9 system older than 9.2
  and using ``consumer_type``
  (https://github.com/ansible-collections/community.general/pull/7378).
- selective callback plugin - fix length of task name lines in output always being 3 characters longer than desired (https://github.com/ansible-collections/community.general/pull/7374).

community.grafana
~~~~~~~~~~~~~~~~~

- Fix error with datasources configured without basicAuth
- grafana_folder, fix an issue during delete (starting Grafana 9.3)

community.hashi_vault
~~~~~~~~~~~~~~~~~~~~~

- vault_write - the ``vault_write`` lookup and module were not able to write data containing keys named ``path`` or ``wrap_ttl`` due to a bug in the ``hvac`` library. These plugins have now been updated to take advantage of fixes in ``hvac>=1.2`` to address this (https://github.com/ansible-collections/community.hashi_vault/issues/389).

community.network
~~~~~~~~~~~~~~~~~

- cnos_l3_interface - fix import errors (https://github.com/ansible-collections/community.network/pull/531).
- exos_config - missing whitespace in command with ``defaults: True``. It happened because the command is ``show configurationdetail`` instead of ``show configuration detail`` (https://github.com/ansible-collections/community.network/pull/516).
- exos_facts - returns timeout error when we use connection type ``network_cli``. It happened because we send command without ``no-refresh`` and script ``cli2json.py`` stuck in loop while reading console output (https://github.com/ansible-collections/community.network/pull/517).
- icx_l3_interface - fix import errors (https://github.com/ansible-collections/community.network/pull/531).
- slxos_l3_interface - fix import errors (https://github.com/ansible-collections/community.network/pull/531).

community.sops
~~~~~~~~~~~~~~

- sops_encrypt - ensure that output-type is set to ``yaml`` when the file extension ``.yml`` is used. Now both ``.yaml`` and ``.yml`` files use the SOPS ``--output-type=yaml`` formatting (https://github.com/ansible-collections/community.sops/issues/164).

community.vmware
~~~~~~~~~~~~~~~~

- The 3.11.0 release went wrong, so here is 3.11.1. No changes since 3.11.0, just hoping to get it correctly published on Galaxy.

containers.podman
~~~~~~~~~~~~~~~~~

- Fix common file for Python 2.7
- podman_network - Do not force network removal by default
- podman_network - Fix network DNS enable idempotency issue
- podman_pod - Fix idempotency when running inside Podman container

f5networks.f5_modules
~~~~~~~~~~~~~~~~~~~~~

- bigip_device_certificate - error-handling for connection error while running exec command function to fetch certificate details
- bigip_pool - Resolved a bug in the code to allow the module to remove monitors from the pool

fortinet.fortimanager
~~~~~~~~~~~~~~~~~~~~~

- Add 'access_token' in 'fmgr_generic'.
- Add param 'platform' in 'fmgr_wtpprofile' and param 'interface' in 'fmgr_fsp_vlan'.
- Fix a bug that collection may update the resource when it does not need to.
- Fix some modules missing revision (used for version warning).
- Fixed the bug that would report an error when providing access_token and username/password at the same time.
- Improve document.
- Improve fmgr_fact. 'changed' will not be true anymore if you get the result.
- Improve sanity tests.
- When the JSON data sent by FortiManager is not in the right format, the collection can still execute correctly.

fortinet.fortios
~~~~~~~~~~~~~~~~

- Fix the issue of one session remaining open after the task is finished.
- To optimize the json_generic module and reduce the time spent while sending GET requests.

netapp.ontap
~~~~~~~~~~~~

- na_ontap_dns - fix DNS not working with Cluster mode.
- na_ontap_ems_filter - fix delete operation not idempotent for filter.
- na_ontap_ems_filter - fix modify operation to add rule in existing filter.
- na_ontap_login_messages - fix idempotency issue in Cluster scope in REST.
- na_ontap_nfs - fix `default_user` under `windows` not getting modified if not set previously in REST.
- na_ontap_svm - fix REST version warning for `ndmp` under `services`.

netbox.netbox
~~~~~~~~~~~~~

- netbox_ device - Adjust device_role to role for NetBox 3.6 [#1066](https://github.com/netbox-community/ansible_modules/pull/1066)

New Modules
-----------

community.grafana
~~~~~~~~~~~~~~~~~

- community.grafana.grafana_organization_user - Manage Grafana Organization Users.

containers.podman
~~~~~~~~~~~~~~~~~

- containers.podman.podman_container_exec - Executes a command in a running container
- containers.podman.podman_runlabel - Run given label from given image

fortinet.fortimanager
~~~~~~~~~~~~~~~~~~~~~

- fortinet.fortimanager.fmgr_casb_profile - Configure CASB profile.
- fortinet.fortimanager.fmgr_casb_profile_saasapplication - CASB profile SaaS application.
- fortinet.fortimanager.fmgr_casb_profile_saasapplication_accessrule - CASB profile access rule.
- fortinet.fortimanager.fmgr_casb_profile_saasapplication_customcontrol - CASB profile custom control.
- fortinet.fortimanager.fmgr_casb_profile_saasapplication_customcontrol_option - CASB custom control option.
- fortinet.fortimanager.fmgr_casb_saasapplication - Configure CASB SaaS application.
- fortinet.fortimanager.fmgr_casb_useractivity - Configure CASB user activity.
- fortinet.fortimanager.fmgr_casb_useractivity_controloptions - CASB control options.
- fortinet.fortimanager.fmgr_casb_useractivity_controloptions_operations - CASB control option operations.
- fortinet.fortimanager.fmgr_casb_useractivity_match - CASB user activity match rules.
- fortinet.fortimanager.fmgr_casb_useractivity_match_rules - CASB user activity rules.
- fortinet.fortimanager.fmgr_dvmdb_upgrade - no description
- fortinet.fortimanager.fmgr_firewall_accessproxy6_apigateway6_quic - QUIC setting.
- fortinet.fortimanager.fmgr_firewall_accessproxy6_apigateway_quic - QUIC setting.
- fortinet.fortimanager.fmgr_firewall_accessproxy_apigateway6_quic - QUIC setting.
- fortinet.fortimanager.fmgr_firewall_accessproxy_apigateway_quic - QUIC setting.
- fortinet.fortimanager.fmgr_firewall_casbprofile - no description
- fortinet.fortimanager.fmgr_firewall_casbprofile_saasapplication - no description
- fortinet.fortimanager.fmgr_firewall_casbprofile_saasapplication_accessrule - no description
- fortinet.fortimanager.fmgr_firewall_casbprofile_saasapplication_customcontrol - no description
- fortinet.fortimanager.fmgr_firewall_casbprofile_saasapplication_customcontrol_option - no description
- fortinet.fortimanager.fmgr_firewall_vendormac - Show vendor and the MAC address they have.
- fortinet.fortimanager.fmgr_firewall_vip_quic - QUIC setting.
- fortinet.fortimanager.fmgr_pm_config_meta_reference - no description
- fortinet.fortimanager.fmgr_securityconsole_install_objects_v2 - no description
- fortinet.fortimanager.fmgr_switchcontroller_managedswitch_routeoffloadrouter - Configure route offload MCLAG IP address.
- fortinet.fortimanager.fmgr_switchcontroller_ptp_profile - Global PTP profile.
- fortinet.fortimanager.fmgr_system_csf - Add this device to a Security Fabric or set up a new Security Fabric on this device.
- fortinet.fortimanager.fmgr_system_csf_fabricconnector - Fabric connector configuration.
- fortinet.fortimanager.fmgr_system_csf_trustedlist - Pre-authorized and blocked security fabric nodes.
- fortinet.fortimanager.fmgr_system_sdnproxy - Configure SDN proxy.
- fortinet.fortimanager.fmgr_virtualpatch_profile - Configure virtual-patch profile.
- fortinet.fortimanager.fmgr_virtualpatch_profile_exemption - Exempt devices or rules.

netapp.ontap
~~~~~~~~~~~~

- netapp.ontap.na_ontap_ems_config - NetApp ONTAP module to modify EMS configuration.

Unchanged Collections
---------------------

- amazon.aws (still version 6.5.0)
- ansible.posix (still version 1.5.4)
- ansible.utils (still version 2.11.0)
- ansible.windows (still version 1.14.0)
- awx.awx (still version 22.7.0)
- check_point.mgmt (still version 5.1.1)
- chocolatey.chocolatey (still version 1.5.1)
- cisco.intersight (still version 1.0.27)
- cisco.ios (still version 4.6.1)
- cisco.iosxr (still version 5.0.3)
- cisco.ise (still version 2.5.16)
- cisco.mso (still version 2.5.0)
- cisco.nso (still version 1.0.3)
- cisco.nxos (still version 4.4.0)
- cisco.ucs (still version 1.10.0)
- cloud.common (still version 2.1.4)
- cloudscale_ch.cloud (still version 2.3.1)
- community.azure (still version 2.0.0)
- community.digitalocean (still version 1.24.0)
- community.fortios (still version 1.0.0)
- community.google (still version 1.0.0)
- community.hrobot (still version 1.8.1)
- community.libvirt (still version 1.3.0)
- community.mongodb (still version 1.6.3)
- community.okd (still version 2.3.0)
- community.postgresql (still version 2.4.3)
- community.proxysql (still version 1.5.1)
- community.rabbitmq (still version 1.2.3)
- community.routeros (still version 2.10.0)
- community.sap (still version 1.0.0)
- community.sap_libs (still version 1.4.1)
- community.skydive (still version 1.0.0)
- community.windows (still version 1.13.0)
- community.zabbix (still version 2.1.0)
- cyberark.conjur (still version 1.2.2)
- cyberark.pas (still version 1.0.23)
- dellemc.enterprise_sonic (still version 2.2.0)
- dellemc.openmanage (still version 7.6.1)
- dellemc.powerflex (still version 1.9.0)
- dellemc.unity (still version 1.7.1)
- frr.frr (still version 2.0.2)
- gluster.gluster (still version 1.0.2)
- google.cloud (still version 1.2.0)
- grafana.grafana (still version 2.2.3)
- hetzner.hcloud (still version 1.16.0)
- hpe.nimble (still version 1.1.4)
- ibm.qradar (still version 2.1.0)
- ibm.spectrum_virtualize (still version 1.12.0)
- infinidat.infinibox (still version 1.3.12)
- infoblox.nios_modules (still version 1.5.0)
- inspur.ispim (still version 1.3.0)
- inspur.sm (still version 2.3.0)
- junipernetworks.junos (still version 5.3.0)
- kubernetes.core (still version 2.4.0)
- microsoft.ad (still version 1.3.0)
- netapp.elementsw (still version 21.7.0)
- netapp.storagegrid (still version 21.11.1)
- netapp_eseries.santricity (still version 1.4.0)
- ngine_io.cloudstack (still version 2.3.0)
- ngine_io.exoscale (still version 1.1.0)
- ngine_io.vultr (still version 1.1.3)
- openstack.cloud (still version 2.1.0)
- openvswitch.openvswitch (still version 2.1.1)
- ovirt.ovirt (still version 3.2.0)
- purestorage.flasharray (still version 1.21.0)
- purestorage.flashblade (still version 1.14.0)
- purestorage.fusion (still version 1.6.0)
- sensu.sensu_go (still version 1.14.0)
- servicenow.servicenow (still version 1.0.6)
- splunk.es (still version 2.1.0)
- t_systems_mms.icinga_director (still version 1.33.1)
- telekom_mms.icinga_director (still version 1.34.1)
- theforeman.foreman (still version 3.14.0)
- vmware.vmware_rest (still version 2.3.1)
- vultr.cloud (still version 1.10.0)
- vyos.vyos (still version 4.1.0)
- wti.remote (still version 1.0.5)

v8.5.0
======

.. contents::
  :local:
  :depth: 2

Release Summary
---------------

Release Date: 2023-10-11

`Porting Guide <https://docs.ansible.com/ansible/devel/porting_guides.html>`_

Ansible-core
------------

Ansible 8.5.0 contains ansible-core version 2.15.5.
This is a newer version than version 2.15.4 contained in the previous Ansible release.

The changes are reported in the combined changelog below.

Changed Collections
-------------------

If not mentioned explicitly, the changes are reported in the combined changelog below.

+------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Collection             | Ansible 8.4.0 | Ansible 8.5.0 | Notes                                                                                                                                                                                                          |
+========================+===============+===============+================================================================================================================================================================================================================+
| amazon.aws             | 6.4.0         | 6.5.0         |                                                                                                                                                                                                                |
+------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| arista.eos             | 6.1.0         | 6.1.2         |                                                                                                                                                                                                                |
+------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| azure.azcollection     | 1.17.0        | 1.18.1        | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.                                                                                   |
+------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cisco.asa              | 4.0.1         | 4.0.2         | There are no changes recorded in the changelog.                                                                                                                                                                |
+------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cisco.dnac             | 6.7.4         | 6.7.5         | The collection did not have a changelog in this version.                                                                                                                                                       |
+------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cisco.ise              | 2.5.15        | 2.5.16        |                                                                                                                                                                                                                |
+------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cisco.meraki           | 2.16.0        | 2.16.5        |                                                                                                                                                                                                                |
+------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.dns          | 2.6.1         | 2.6.2         |                                                                                                                                                                                                                |
+------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.docker       | 3.4.8         | 3.4.9         |                                                                                                                                                                                                                |
+------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.general      | 7.4.0         | 7.5.0         |                                                                                                                                                                                                                |
+------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.libvirt      | 1.2.0         | 1.3.0         |                                                                                                                                                                                                                |
+------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.mongodb      | 1.6.1         | 1.6.3         | There are no changes recorded in the changelog.                                                                                                                                                                |
+------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.routeros     | 2.9.0         | 2.10.0        |                                                                                                                                                                                                                |
+------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.sops         | 1.6.5         | 1.6.6         |                                                                                                                                                                                                                |
+------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.vmware       | 3.9.0         | 3.10.0        |                                                                                                                                                                                                                |
+------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cyberark.conjur        | 1.2.0         | 1.2.2         | You can find the collection's changelog at `https://github.com/cyberark/ansible-conjur-collection/blob/master/CHANGELOG.md <https://github.com/cyberark/ansible-conjur-collection/blob/master/CHANGELOG.md>`_. |
+------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cyberark.pas           | 1.0.19        | 1.0.23        | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.                                                                                   |
+------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| dellemc.powerflex      | 1.8.0         | 1.9.0         |                                                                                                                                                                                                                |
+------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| grafana.grafana        | 2.1.8         | 2.2.3         |                                                                                                                                                                                                                |
+------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ovirt.ovirt            | 3.1.3         | 3.2.0         |                                                                                                                                                                                                                |
+------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| purestorage.flashblade | 1.13.1        | 1.14.0        |                                                                                                                                                                                                                |
+------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| vultr.cloud            | 1.9.0         | 1.10.0        |                                                                                                                                                                                                                |
+------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Minor Changes
-------------

Ansible-core
~~~~~~~~~~~~

- ansible-galaxy dependency resolution messages have changed the unexplained 'virtual' collection for the specific type ('scm', 'dir', etc) that is more user friendly

amazon.aws
~~~~~~~~~~

- ec2_ami - add support for ``org_arns`` and ``org_unit_arns`` in launch_permissions (https://github.com/ansible-collections/amazon.aws/pull/1690).
- elb_application_lb_info - drop redundant ``describe_load_balancers`` call fetching ``ip_address_type`` (https://github.com/ansible-collections/amazon.aws/pull/1768).

community.general
~~~~~~~~~~~~~~~~~

- cargo - add option ``executable``, which allows user to specify path to the cargo binary (https://github.com/ansible-collections/community.general/pull/7352).
- cargo - add option ``locked`` which allows user to specify install the locked version of dependency instead of latest compatible version (https://github.com/ansible-collections/community.general/pull/6134).
- dig lookup plugin - add TCP option to enable the use of TCP connection during DNS lookup (https://github.com/ansible-collections/community.general/pull/7343).
- gitlab_group - add option ``force_delete`` (default: false) which allows delete group even if projects exists in it (https://github.com/ansible-collections/community.general/pull/7364).
- ini_file - add ``ignore_spaces`` option (https://github.com/ansible-collections/community.general/pull/7273).
- newrelic_deployment - add option ``app_name_exact_match``, which filters results for the exact app_name provided (https://github.com/ansible-collections/community.general/pull/7355).
- onepassword lookup plugin - introduce ``account_id`` option which allows specifying which account to use (https://github.com/ansible-collections/community.general/pull/7308).
- onepassword_raw lookup plugin - introduce ``account_id`` option which allows specifying which account to use (https://github.com/ansible-collections/community.general/pull/7308).
- parted - on resize, use ``--fix`` option if available (https://github.com/ansible-collections/community.general/pull/7304).
- pnpm - set correct version when state is latest or version is not mentioned. Resolves previous idempotency problem (https://github.com/ansible-collections/community.general/pull/7339).
- proxmox - add ``vmid`` (and ``taskid`` when possible) to return values (https://github.com/ansible-collections/community.general/pull/7263).
- random_string - added new ``ignore_similar_chars`` and ``similar_chars`` option to ignore certain chars (https://github.com/ansible-collections/community.general/pull/7242).
- redfish_command - add new option ``update_oem_params`` for the ``MultipartHTTPPushUpdate`` command (https://github.com/ansible-collections/community.general/issues/7331).
- redfish_config - add ``CreateVolume`` command to allow creation of volumes on servers (https://github.com/ansible-collections/community.general/pull/6813).
- redfish_config - adding ``SetSecureBoot`` command (https://github.com/ansible-collections/community.general/pull/7129).
- redfish_info - add support for ``GetBiosRegistries`` command (https://github.com/ansible-collections/community.general/pull/7144).
- redfish_info - adds ``LinkStatus`` to NIC inventory (https://github.com/ansible-collections/community.general/pull/7318).
- redis_info - refactor the redis_info module to use the redis module_utils enabling to pass TLS parameters to the Redis client (https://github.com/ansible-collections/community.general/pull/7267).
- supervisorctl - allow to stop matching running processes before removing them with ``stop_before_removing=true`` (https://github.com/ansible-collections/community.general/pull/7284).

community.libvirt
~~~~~~~~~~~~~~~~~

- virt - add `mutate_flags` parameter to enable XML mutation (add UUID, MAC addresses from existing domain) (https://github.com/ansible-collections/community.libvirt/pull/142/).
- virt - support ``--diff`` for ``define`` command (https://github.com/ansible-collections/community.libvirt/pull/142/).

community.routeros
~~~~~~~~~~~~~~~~~~

- api_info - add new ``include_read_only`` option to select behavior for read-only values. By default these are not returned (https://github.com/ansible-collections/community.routeros/pull/213).
- api_info, api_modify - add support for ``address-list`` and ``match-subdomain`` introduced by RouterOS 7.7 in the ``ip dns static`` path (https://github.com/ansible-collections/community.routeros/pull/197).
- api_info, api_modify - add support for ``user``, ``time`` and ``gmt-offset`` under the ``system clock`` path (https://github.com/ansible-collections/community.routeros/pull/210).
- api_info, api_modify - add support for the ``interface ppp-client`` path (https://github.com/ansible-collections/community.routeros/pull/199).
- api_info, api_modify - add support for the ``interface wireless`` path (https://github.com/ansible-collections/community.routeros/pull/195).
- api_info, api_modify - add support for the ``iot modbus`` path (https://github.com/ansible-collections/community.routeros/pull/205).
- api_info, api_modify - add support for the ``ip dhcp-server option`` and ``ip dhcp-server option sets`` paths (https://github.com/ansible-collections/community.routeros/pull/223).
- api_info, api_modify - add support for the ``ip upnp interfaces``, ``tool graphing interface``, ``tool graphing resource`` paths (https://github.com/ansible-collections/community.routeros/pull/227).
- api_info, api_modify - add support for the ``ipv6 firewall nat`` path (https://github.com/ansible-collections/community.routeros/pull/204).
- api_info, api_modify - add support for the ``mode`` property in ``ip neighbor discovery-settings`` introduced in RouterOS 7.7 (https://github.com/ansible-collections/community.routeros/pull/198).
- api_info, api_modify - add support for the ``port remote-access`` path (https://github.com/ansible-collections/community.routeros/pull/224).
- api_info, api_modify - add support for the ``routing filter rule`` and ``routing filter select-rule`` paths (https://github.com/ansible-collections/community.routeros/pull/200).
- api_info, api_modify - add support for the ``routing table`` path in RouterOS 7 (https://github.com/ansible-collections/community.routeros/pull/215).
- api_info, api_modify - add support for the ``tool netwatch`` path in RouterOS 7 (https://github.com/ansible-collections/community.routeros/pull/216).
- api_info, api_modify - add support for the ``user settings`` path (https://github.com/ansible-collections/community.routeros/pull/201).
- api_info, api_modify - add support for the ``user`` path (https://github.com/ansible-collections/community.routeros/pull/211).
- api_info, api_modify - finalize fields for the ``interface wireless security-profiles`` path and enable it (https://github.com/ansible-collections/community.routeros/pull/203).
- api_info, api_modify - finalize fields for the ``ppp profile`` path and enable it (https://github.com/ansible-collections/community.routeros/pull/217).
- api_modify - add new ``handle_read_only`` and ``handle_write_only`` options to handle the module's behavior for read-only and write-only fields (https://github.com/ansible-collections/community.routeros/pull/213).
- api_modify, api_info - support API paths ``routing id``, ``routing bgp connection`` (https://github.com/ansible-collections/community.routeros/pull/220).

community.vmware
~~~~~~~~~~~~~~~~

- add moid property in the return value for the module(https://github.com/ansible-collections/community.vmware/pull/1855).
- add new snapshot_id option to the vmware_guest_snapshot module(https://github.com/ansible-collections/community.vmware/pull/1847).

dellemc.powerflex
~~~~~~~~~~~~~~~~~

- Added Ansible role to support installation and uninstallation of Gateway.
- Added Ansible role to support installation and uninstallation of SDR.
- Added Ansible role to support installation and uninstallation of Web UI.

grafana.grafana
~~~~~~~~~~~~~~~

- Add check for Curl and failure step if Agent Version is not retrieved
- Allow alert resource provisioning in Grafana Role
- Bump cryptography from 39.0.2 to 41.0.3
- Bump cryptography from 41.0.3 to 41.0.4
- Bump semver from 5.7.1 to 5.7.2
- Bump word-wrap from 1.2.3 to 1.2.5
- Create local dashboard directory in check mode
- Create missing notification directory in Grafana Role
- Remove check_mode from create local directory task in Grafana Role
- Remove dependency on local-fs.target from Grafana Agent role
- Update CI Testing
- Update Cloud Stack Module failures
- Use 'ansible_system' env variable to detect os typ in Grafana Agent Role
- hange grafana Agent Wal and Positions Directory in Grafana Agent Role

ovirt.ovirt
~~~~~~~~~~~

- ovirt_vm - Add tpm_enabled (https://github.com/oVirt/ovirt-ansible-collection/pull/722).
- storage_error_resume_behaviour - Support VM storage error resume behaviour "auto_resume", "kill", "leave_paused". (https://github.com/oVirt/ovirt-ansible-collection/pull/721)
- vm_infra - Support boot disk renaming and resizing. (https://github.com/oVirt/ovirt-ansible-collection/pull/705)

purestorage.flashblade
~~~~~~~~~~~~~~~~~~~~~~

- purefb_bucket_replica - Added support for cascading replica links
- purefb_info - New fields to display free space (remaining quota) for Accounts and Buckets. Space used by destroyed buckets is split out from virtual field to new destroyed_virtual field
- purefb_info - Report encryption state in SMB client policy rules
- purefb_info - Report more detailed space data from Purity//FB 4.3.0
- purefb_policy - Add deny effect for object store policy rules. Requires Purity//FB 4.3.0+
- purefb_policy - Added parameter to define object store policy description

vultr.cloud
~~~~~~~~~~~

- inventory - Added VPC/VPC 2.0 support by adding ``internal_ip`` to the attributes (https://github.com/vultr/ansible-collection-vultr/issues/86).

Deprecated Features
-------------------

community.general
~~~~~~~~~~~~~~~~~

- The next major release, community.general 8.0.0, will drop support for ansible-core 2.11 and 2.12, which have been End of Life for some time now. This means that this collection no longer supports Python 2.6 on the target. Individual content might still work with unsupported ansible-core versions, but that can change at any time. Also please note that from now on, for every new major community.general release, we will drop support for all ansible-core versions that have been End of Life for more than a few weeks on the date of the major release (https://github.com/ansible-community/community-topics/discussions/271, https://github.com/ansible-collections/community.general/pull/7259).
- redfish_info, redfish_config, redfish_command - the default value ``10`` for the ``timeout`` option is deprecated and will change to ``60`` in community.general 9.0.0 (https://github.com/ansible-collections/community.general/pull/7295).

Security Fixes
--------------

Ansible-core
~~~~~~~~~~~~

- ansible-galaxy - Prevent roles from using symlinks to overwrite files outside of the installation directory (CVE-2023-5115)

Bugfixes
--------

Ansible-core
~~~~~~~~~~~~

- Allow for searching handler subdir for included task via include_role (https://github.com/ansible/ansible/issues/81722)
- PluginLoader - fix Jinja plugin performance issues (https://github.com/ansible/ansible/issues/79652)
- ``ansible.module_utils.service`` - ensure binary data transmission in ``daemonize()``
- ``ansible.module_utils.service`` - fix inter-process communication in ``daemonize()``
- ansible-galaxy - started allowing the use of pre-releases for collections that do not have any stable versions published. (https://github.com/ansible/ansible/pull/81606)
- ansible-galaxy - started allowing the use of pre-releases for dependencies on any level of the dependency tree that specifically demand exact pre-release versions of collections and not version ranges. (https://github.com/ansible/ansible/pull/81606)
- ansible-galaxy error on dependency resolution will not error itself due to 'virtual' collections not having a name/namespace.
- ansible-galaxy info - fix reporting no role found when lookup_role_by_name returns None.
- role deduplication - don't deduplicate before a role has had a task run for that particular host (https://github.com/ansible/ansible/issues/81486).
- uri/urls - Add compat function to handle the ability to parse the filename from a Content-Disposition header (https://github.com/ansible/ansible/issues/81806)
- winrm - Better handle send input failures when communicating with hosts under load

amazon.aws
~~~~~~~~~~

- elb_application_lb_info - ensure all API queries use the retry decorator (https://github.com/ansible-collections/amazon.aws/issues/1767).

arista.eos
~~~~~~~~~~

- Skip compile testing for python <3.6.
- fix sanity issues w.r.t python27

cisco.ise
~~~~~~~~~

- Cannot get cisco.ise.active_directory_groups_by_domain_info to work.

cisco.meraki
~~~~~~~~~~~~

- Removing ignores.
- Updating collection docs link.
- Updating documentation, yml fixes - Documentation Broken.
- cisco.meraki.networks_devices_claim - got an unexpected keyword argument 'network_id', bug with parameter naming.
- cisco.meraki.organizations_login_security module will not update org api authentication - fixing for look at organizations_login_security.

community.dns
~~~~~~~~~~~~~

- Update Public Suffix List.

community.docker
~~~~~~~~~~~~~~~~

- vendored Docker SDK for Python code - cherry-pick changes from the Docker SDK for Python code to align code. These changes should not affect the parts used by the collection's code (https://github.com/ansible-collections/community.docker/pull/694).

community.general
~~~~~~~~~~~~~~~~~

- gitlab_group_variable - deleted all variables when used with ``purge=true`` due to missing ``raw`` property in KNOWN attributes (https://github.com/ansible-collections/community.general/issues/7250).
- gitlab_project_variable - deleted all variables when used with ``purge=true`` due to missing ``raw`` property in KNOWN attributes (https://github.com/ansible-collections/community.general/issues/7250).
- ldap_search - fix string normalization and the ``base64_attributes`` option on Python 3 (https://github.com/ansible-collections/community.general/issues/5704, https://github.com/ansible-collections/community.general/pull/7264).
- lxc connection plugin - properly evaluate options (https://github.com/ansible-collections/community.general/pull/7369).
- mail - skip headers containing equals characters due to missing ``maxsplit`` on header key/value parsing (https://github.com/ansible-collections/community.general/pull/7303).
- nmap inventory plugin - fix ``get_option`` calls (https://github.com/ansible-collections/community.general/pull/7323).
- onepassword - fix KeyError exception when trying to access value of a field that is not filled out in OnePassword item (https://github.com/ansible-collections/community.general/pull/7241).
- snap - change the change detection mechanism from "parsing installation" to "comparing end state with initial state" (https://github.com/ansible-collections/community.general/pull/7340, https://github.com/ansible-collections/community.general/issues/7265).
- terraform - prevents ``-backend-config`` option double encapsulating with ``shlex_quote`` function. (https://github.com/ansible-collections/community.general/pull/7301).

community.libvirt
~~~~~~~~~~~~~~~~~

- libvirt_qemu - connection plugin threw a warning about an improperly configured remote target. Fix adds `inventory_hostname` to `options.remote_addr.vars` (https://github.com/ansible-collections/community.libvirt/pull/147).
- libvirt_qemu - fix encoding errors on Windows guests for non-ASCII return values (https://github.com/ansible-collections/community.libvirt/pull/157)
- virt - fix virt module to undefine a domain with nvram, managed_save, snapshot_metadata or checkpoints_metadata (https://github.com/ansible-collections/community.libvirt/issues/40).
- virt_pool - replace discouraged function ``listAllVolumes`` with ``listAllVolumes`` to fix potential race conditions (https://github.com/ansible-collections/community.libvirt/pull/135).
- virt_pool - replace discouraged functions ``listStoragePools`` and ``listDefinedStoragePools`` with ``listAllStoragePools`` to fix potential race conditions (https://github.com/ansible-collections/community.libvirt/pull/134).

community.routeros
~~~~~~~~~~~~~~~~~~

- api_info, api_modify - in the ``snmp`` path, ensure that ``engine-id-suffix`` is only available on RouterOS 7.10+, and that ``engine-id`` is read-only on RouterOS 7.10+ (https://github.com/ansible-collections/community.routeros/issues/208, https://github.com/ansible-collections/community.routeros/pull/218).

community.sops
~~~~~~~~~~~~~~

- Fix RPM URL for the 3.8.0 release (https://github.com/ansible-collections/community.sops/pull/161).

community.vmware
~~~~~~~~~~~~~~~~

- fix problem when module try apply non global or non VM type custom attribute to VM object (https://github.com/ansible-collections/community.vmware/issues/1772)
- vmware_deploy_ovf: fix error in finding networks part of code https://github.com/ansible-collections/community.vmware/issues/1853

ovirt.ovirt
~~~~~~~~~~~

- ovirt_role - Fix administrative option when set to False (https://github.com/oVirt/ovirt-ansible-collection/pull/723).

purestorage.flashblade
~~~~~~~~~~~~~~~~~~~~~~

- purefb_userpolicy - Fixed `show` state for all user policies

New Modules
-----------

community.general
~~~~~~~~~~~~~~~~~

- community.general.consul_role - Manipulate Consul roles
- community.general.gio_mime - Set default handler for MIME type, for applications using Gnome GIO
- community.general.keycloak_authz_custom_policy - Allows administration of Keycloak client custom Javascript policies via Keycloak API
- community.general.keycloak_realm_key - Allows administration of Keycloak realm keys via Keycloak API
- community.general.simpleinit_msb - Manage services on Source Mage GNU/Linux

community.vmware
~~~~~~~~~~~~~~~~

- community.vmware.vcenter_root_password_expiration - root password expiration of vCSA
- community.vmware.vmware_host_graphics - Manage Host Graphic Settings

Unchanged Collections
---------------------

- ansible.netcommon (still version 5.2.0)
- ansible.posix (still version 1.5.4)
- ansible.utils (still version 2.11.0)
- ansible.windows (still version 1.14.0)
- awx.awx (still version 22.7.0)
- check_point.mgmt (still version 5.1.1)
- chocolatey.chocolatey (still version 1.5.1)
- cisco.aci (still version 2.7.0)
- cisco.intersight (still version 1.0.27)
- cisco.ios (still version 4.6.1)
- cisco.iosxr (still version 5.0.3)
- cisco.mso (still version 2.5.0)
- cisco.nso (still version 1.0.3)
- cisco.nxos (still version 4.4.0)
- cisco.ucs (still version 1.10.0)
- cloud.common (still version 2.1.4)
- cloudscale_ch.cloud (still version 2.3.1)
- community.aws (still version 6.3.0)
- community.azure (still version 2.0.0)
- community.ciscosmb (still version 1.0.6)
- community.crypto (still version 2.15.1)
- community.digitalocean (still version 1.24.0)
- community.fortios (still version 1.0.0)
- community.google (still version 1.0.0)
- community.grafana (still version 1.5.4)
- community.hashi_vault (still version 5.0.0)
- community.hrobot (still version 1.8.1)
- community.mysql (still version 3.7.2)
- community.network (still version 5.0.0)
- community.okd (still version 2.3.0)
- community.postgresql (still version 2.4.3)
- community.proxysql (still version 1.5.1)
- community.rabbitmq (still version 1.2.3)
- community.sap (still version 1.0.0)
- community.sap_libs (still version 1.4.1)
- community.skydive (still version 1.0.0)
- community.windows (still version 1.13.0)
- community.zabbix (still version 2.1.0)
- containers.podman (still version 1.10.3)
- dellemc.enterprise_sonic (still version 2.2.0)
- dellemc.openmanage (still version 7.6.1)
- dellemc.unity (still version 1.7.1)
- f5networks.f5_modules (still version 1.26.0)
- fortinet.fortimanager (still version 2.2.1)
- fortinet.fortios (still version 2.3.2)
- frr.frr (still version 2.0.2)
- gluster.gluster (still version 1.0.2)
- google.cloud (still version 1.2.0)
- hetzner.hcloud (still version 1.16.0)
- hpe.nimble (still version 1.1.4)
- ibm.qradar (still version 2.1.0)
- ibm.spectrum_virtualize (still version 1.12.0)
- infinidat.infinibox (still version 1.3.12)
- infoblox.nios_modules (still version 1.5.0)
- inspur.ispim (still version 1.3.0)
- inspur.sm (still version 2.3.0)
- junipernetworks.junos (still version 5.3.0)
- kubernetes.core (still version 2.4.0)
- lowlydba.sqlserver (still version 2.2.1)
- microsoft.ad (still version 1.3.0)
- netapp.aws (still version 21.7.0)
- netapp.azure (still version 21.10.0)
- netapp.cloudmanager (still version 21.22.0)
- netapp.elementsw (still version 21.7.0)
- netapp.ontap (still version 22.7.0)
- netapp.storagegrid (still version 21.11.1)
- netapp.um_info (still version 21.8.0)
- netapp_eseries.santricity (still version 1.4.0)
- netbox.netbox (still version 3.14.0)
- ngine_io.cloudstack (still version 2.3.0)
- ngine_io.exoscale (still version 1.1.0)
- ngine_io.vultr (still version 1.1.3)
- openstack.cloud (still version 2.1.0)
- openvswitch.openvswitch (still version 2.1.1)
- purestorage.flasharray (still version 1.21.0)
- purestorage.fusion (still version 1.6.0)
- sensu.sensu_go (still version 1.14.0)
- servicenow.servicenow (still version 1.0.6)
- splunk.es (still version 2.1.0)
- t_systems_mms.icinga_director (still version 1.33.1)
- telekom_mms.icinga_director (still version 1.34.1)
- theforeman.foreman (still version 3.14.0)
- vmware.vmware_rest (still version 2.3.1)
- vyos.vyos (still version 4.1.0)
- wti.remote (still version 1.0.5)

v8.4.0
======

.. contents::
  :local:
  :depth: 2

Release Summary
---------------

Release Date: 2023-09-12

`Porting Guide <https://docs.ansible.com/ansible/devel/porting_guides.html>`_

Ansible-core
------------

Ansible 8.4.0 contains ansible-core version 2.15.4.
This is a newer version than version 2.15.3 contained in the previous Ansible release.

The changes are reported in the combined changelog below.

Changed Collections
-------------------

If not mentioned explicitly, the changes are reported in the combined changelog below.

+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| Collection             | Ansible 8.3.0 | Ansible 8.4.0 | Notes                                                                                                                        |
+========================+===============+===============+==============================================================================================================================+
| amazon.aws             | 6.3.0         | 6.4.0         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| ansible.netcommon      | 5.1.2         | 5.2.0         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| ansible.utils          | 2.10.3        | 2.11.0        |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| arista.eos             | 6.0.1         | 6.1.0         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| awx.awx                | 22.6.0        | 22.7.0        | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| azure.azcollection     | 1.16.0        | 1.17.0        | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.dnac             | 6.7.3         | 6.7.4         | The collection did not have a changelog in this version.                                                                     |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.ise              | 2.5.14        | 2.5.15        |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.meraki           | 2.15.3        | 2.16.0        |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.aws          | 6.2.0         | 6.3.0         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.crypto       | 2.15.0        | 2.15.1        |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.dns          | 2.6.0         | 2.6.1         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.general      | 7.3.0         | 7.4.0         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.sops         | 1.6.4         | 1.6.5         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| containers.podman      | 1.10.2        | 1.10.3        |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| dellemc.powerflex      | 1.7.0         | 1.8.0         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| f5networks.f5_modules  | 1.25.1        | 1.26.0        |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| fortinet.fortios       | 2.3.1         | 2.3.2         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| grafana.grafana        | 2.1.5         | 2.1.8         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| junipernetworks.junos  | 5.2.0         | 5.3.0         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| lowlydba.sqlserver     | 2.1.0         | 2.2.1         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| netbox.netbox          | 3.13.0        | 3.14.0        |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| ngine_io.exoscale      | 1.0.0         | 1.1.0         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| ovirt.ovirt            | 3.1.2         | 3.1.3         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| purestorage.flasharray | 1.20.0        | 1.21.0        |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| purestorage.flashblade | 1.12.1        | 1.13.1        |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| theforeman.foreman     | 3.12.0        | 3.14.0        |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| vultr.cloud            | 1.8.0         | 1.9.0         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+

Major Changes
-------------

fortinet.fortios
~~~~~~~~~~~~~~~~

- Improve the document for adding notes and examples in Q&A for modules using Integer number as the mkey.

Minor Changes
-------------

amazon.aws
~~~~~~~~~~

- cloudformation - Add support for ``disable_rollback`` to update stack operation (https://github.com/ansible-collections/amazon.aws/issues/1681).
- ec2_key - add support for new parameter ``file_name`` to save private key in when new key is created by AWS. When this option is provided the generated private key will be removed from the module return (https://github.com/ansible-collections/amazon.aws/pull/1704).

ansible.netcommon
~~~~~~~~~~~~~~~~~

- Add a new cliconf plugin ``default`` that can be used when no cliconf plugin is found for a given network_os. This plugin only supports ``get()``. (https://github.com/ansible-collections/ansible.netcommon/pull/569)
- httpapi - Add additional option ``ca_path``, ``client_cert``, ``client_key``, and ``http_agent`` that are available in open_url but not to httpapi. (https://github.com/ansible-collections/ansible.netcommon/issues/528)
- telnet - add crlf option to send CRLF instead of just LF (https://github.com/ansible-collections/ansible.netcommon/pull/440).

ansible.utils
~~~~~~~~~~~~~

- Add ipcut filter plugin.(https://github.com/ansible-collections/ansible.utils/issues/251)
- Add ipv6form filter plugin.(https://github.com/ansible-collections/ansible.utils/issues/230)

arista.eos
~~~~~~~~~~

- Add support for overridden operation in bgp_global resource module.

cisco.meraki
~~~~~~~~~~~~

- administered_identities_me_info - new plugin.
- devices - new plugin.
- devices_appliance_performance_info - new plugin.
- devices_appliance_uplinks_settings - new plugin.
- devices_appliance_uplinks_settings_info - new plugin.
- devices_appliance_vmx_authentication_token - new plugin.
- devices_blink_leds - new plugin.
- devices_camera_analytics_live_info - new plugin.
- devices_camera_custom_analytics - new plugin.
- devices_camera_custom_analytics_info - new plugin.
- devices_camera_generate_snapshot - new plugin.
- devices_camera_quality_and_retention - new plugin.
- devices_camera_quality_and_retention_info - new plugin.
- devices_camera_sense - new plugin.
- devices_camera_sense_info - new plugin.
- devices_camera_video_link_info - new plugin.
- devices_camera_video_settings - new plugin.
- devices_camera_video_settings_info - new plugin.
- devices_camera_wireless_profiles - new plugin.
- devices_camera_wireless_profiles_info - new plugin.
- devices_cellular_gateway_lan - new plugin.
- devices_cellular_gateway_lan_info - new plugin.
- devices_cellular_gateway_port_forwarding_rules - new plugin.
- devices_cellular_gateway_port_forwarding_rules_info - new plugin.
- devices_cellular_sims - new plugin.
- devices_cellular_sims_info - new plugin.
- devices_info - new plugin.
- devices_live_tools_ping - new plugin.
- devices_live_tools_ping_device - new plugin.
- devices_live_tools_ping_device_info - new plugin.
- devices_live_tools_ping_info - new plugin.
- devices_lldp_cdp_info - new plugin.
- devices_management_interface - new plugin.
- devices_management_interface_info - new plugin.
- devices_sensor_relationships - new plugin.
- devices_sensor_relationships_info - new plugin.
- devices_switch_ports - new plugin.
- devices_switch_ports_cycle - new plugin.
- devices_switch_ports_info - new plugin.
- devices_switch_ports_statuses_info - new plugin.
- devices_switch_routing_interfaces - new plugin.
- devices_switch_routing_interfaces_dhcp - new plugin.
- devices_switch_routing_interfaces_dhcp_info - new plugin.
- devices_switch_routing_interfaces_info - new plugin.
- devices_switch_routing_static_routes - new plugin.
- devices_switch_routing_static_routes_info - new plugin.
- devices_switch_warm_spare - new plugin.
- devices_switch_warm_spare_info - new plugin.
- devices_wireless_bluetooth_settings - new plugin.
- devices_wireless_bluetooth_settings_info - new plugin.
- devices_wireless_connection_stats_info - new plugin.
- devices_wireless_latency_stats_info - new plugin.
- devices_wireless_radio_settings - new plugin.
- devices_wireless_radio_settings_info - new plugin.
- devices_wireless_status_info - new plugin.
- networks - new plugin.
- networks_alerts_history_info - new plugin.
- networks_alerts_settings - new plugin.
- networks_alerts_settings_info - new plugin.
- networks_appliance_connectivity_monitoring_destinations - new plugin.
- networks_appliance_connectivity_monitoring_destinations_info - new plugin.
- networks_appliance_content_filtering - new plugin.
- networks_appliance_content_filtering_categories_info - new plugin.
- networks_appliance_content_filtering_info - new plugin.
- networks_appliance_firewall_cellular_firewall_rules - new plugin.
- networks_appliance_firewall_cellular_firewall_rules_info - new plugin.
- networks_appliance_firewall_firewalled_services - new plugin.
- networks_appliance_firewall_firewalled_services_info - new plugin.
- networks_appliance_firewall_inbound_firewall_rules - new plugin.
- networks_appliance_firewall_inbound_firewall_rules_info - new plugin.
- networks_appliance_firewall_l3_firewall_rules - new plugin.
- networks_appliance_firewall_l3_firewall_rules_info - new plugin.
- networks_appliance_firewall_l7_firewall_rules - new plugin.
- networks_appliance_firewall_l7_firewall_rules_application_categories_info - new plugin.
- networks_appliance_firewall_l7_firewall_rules_info - new plugin.
- networks_appliance_firewall_one_to_many_nat_rules - new plugin.
- networks_appliance_firewall_one_to_many_nat_rules_info - new plugin.
- networks_appliance_firewall_one_to_one_nat_rules - new plugin.
- networks_appliance_firewall_one_to_one_nat_rules_info - new plugin.
- networks_appliance_firewall_port_forwarding_rules - new plugin.
- networks_appliance_firewall_port_forwarding_rules_info - new plugin.
- networks_appliance_firewall_settings - new plugin.
- networks_appliance_firewall_settings_info - new plugin.
- networks_appliance_ports - new plugin.
- networks_appliance_ports_info - new plugin.
- networks_appliance_prefixes_delegated_statics - new plugin.
- networks_appliance_prefixes_delegated_statics_info - new plugin.
- networks_appliance_security_intrusion - new plugin.
- networks_appliance_security_intrusion_info - new plugin.
- networks_appliance_security_malware - new plugin.
- networks_appliance_security_malware_info - new plugin.
- networks_appliance_settings - new plugin.
- networks_appliance_settings_info - new plugin.
- networks_appliance_single_lan - new plugin.
- networks_appliance_single_lan_info - new plugin.
- networks_appliance_ssids - new plugin.
- networks_appliance_ssids_info - new plugin.
- networks_appliance_static_routes  - new plugin.
- networks_appliance_static_routes_info  - new plugin.
- networks_appliance_traffic_shaping - new plugin.
- networks_appliance_traffic_shaping_custom_performance_classes - new plugin.
- networks_appliance_traffic_shaping_info - new plugin.
- networks_appliance_traffic_shaping_rules - new plugin.
- networks_appliance_traffic_shaping_rules_info - new plugin.
- networks_appliance_traffic_shaping_uplink_bandwidth - new plugin.
- networks_appliance_traffic_shaping_uplink_bandwidth_info - new plugin.
- networks_appliance_traffic_shaping_uplink_selection - new plugin.
- networks_appliance_traffic_shaping_uplink_selection_info - new plugin.
- networks_appliance_vlans - new plugin.
- networks_appliance_vlans_info - new plugin.
- networks_appliance_vlans_settings - new plugin.
- networks_appliance_vlans_settings_info - new plugin.
- networks_appliance_vpn_bgp - new plugin.
- networks_appliance_vpn_bgp_info - new plugin.
- networks_appliance_vpn_site_to_site_vpn - new plugin.
- networks_appliance_vpn_site_to_site_vpn_info - new plugin.
- networks_appliance_warm_spare - new plugin.
- networks_appliance_warm_spare_info - new plugin.
- networks_appliance_warm_spare_swap - new plugin.
- networks_bind - new plugin.
- networks_bluetooth_clients_info - new plugin.
- networks_camera_quality_retention_profiles - new plugin.
- networks_camera_quality_retention_profiles_info - new plugin.
- networks_camera_wireless_profiles - new plugin.
- networks_camera_wireless_profiles_info - new plugin.
- networks_cellular_gateway_connectivity_monitoring_destinations - new plugin.
- networks_cellular_gateway_connectivity_monitoring_destinations_info - new plugin.
- networks_cellular_gateway_dhcp - new plugin.
- networks_cellular_gateway_dhcp_info - new plugin.
- networks_cellular_gateway_subnet_pool - new plugin.
- networks_cellular_gateway_subnet_pool_info - new plugin.
- networks_cellular_gateway_uplink - new plugin.
- networks_cellular_gateway_uplink_info - new plugin.
- networks_clients_info - new plugin.
- networks_clients_overview_info - new plugin.
- networks_clients_policy - new plugin.
- networks_clients_policy_info - new plugin.
- networks_clients_provision - new plugin.
- networks_clients_splash_authorization_status - new plugin.
- networks_clients_splash_authorization_status_info - new plugin.
- networks_devices_claim - new plugin.
- networks_devices_claim_vmx - new plugin.
- networks_devices_remove - new plugin.
- networks_events_event_types_info - new plugin.
- networks_events_info - new plugin.
- networks_firmware_upgrades - new plugin.
- networks_firmware_upgrades_info - new plugin.
- networks_firmware_upgrades_rollbacks - new plugin.
- networks_firmware_upgrades_staged_events - new plugin.
- networks_firmware_upgrades_staged_events_defer - new plugin.
- networks_firmware_upgrades_staged_events_info - new plugin.
- networks_firmware_upgrades_staged_events_rollbacks - new plugin.
- networks_firmware_upgrades_staged_groups - new plugin.
- networks_firmware_upgrades_staged_groups_info - new plugin.
- networks_firmware_upgrades_staged_stages - new plugin.
- networks_firmware_upgrades_staged_stages_info - new plugin.
- networks_floor_plans - new plugin.
- networks_floor_plans_info - new plugin.
- networks_group_policies - new plugin.
- networks_group_policies_info - new plugin.
- networks_health_alerts_info - new plugin.
- networks_info - new plugin.
- networks_insight_applications_health_by_time_info - new plugin.
- networks_meraki_auth_users - new plugin.
- networks_meraki_auth_users_info - new plugin.
- networks_mqtt_brokers - new plugin.
- networks_netflow - new plugin.
- networks_netflow_info - new plugin.
- networks_pii_pii_keys_info - new plugin.
- networks_pii_requests_delete - new plugin.
- networks_pii_requests_info - new plugin.
- networks_pii_sm_devices_for_key_info - new plugin.
- networks_pii_sm_owners_for_key_info - new plugin.
- networks_policies_by_client_info - new plugin.
- networks_sensor_alerts_current_overview_by_metric_info - new plugin.
- networks_sensor_alerts_overview_by_metric_info - new plugin.
- networks_sensor_alerts_profiles - new plugin.
- networks_sensor_alerts_profiles_info - new plugin.
- networks_sensor_mqtt_brokers - new plugin.
- networks_sensor_mqtt_brokers_info - new plugin.
- networks_sensor_relationships_info - new plugin.
- networks_settings - new plugin.
- networks_settings_info - new plugin.
- networks_sm_bypass_activation_lock_attempts - new plugin.
- networks_sm_bypass_activation_lock_attempts_info - new plugin.
- networks_sm_devices_cellular_usage_history_info - new plugin.
- networks_sm_devices_certs_info - new plugin.
- networks_sm_devices_checkin - new plugin.
- networks_sm_devices_connectivity_info - new plugin.
- networks_sm_devices_desktop_logs_info - new plugin.
- networks_sm_devices_device_command_logs_info - new plugin.
- networks_sm_devices_device_profiles_info - new plugin.
- networks_sm_devices_fields - new plugin.
- networks_sm_devices_info - new plugin.
- networks_sm_devices_lock - new plugin.
- networks_sm_devices_modify_tags - new plugin.
- networks_sm_devices_move - new plugin.
- networks_sm_devices_network_adapters_info - new plugin.
- networks_sm_devices_performance_history_info - new plugin.
- networks_sm_devices_refresh_details - new plugin.
- networks_sm_devices_security_centers_info - new plugin.
- networks_sm_devices_unenroll - new plugin.
- networks_sm_devices_wipe - new plugin.
- networks_sm_devices_wlan_lists_info - new plugin.
- networks_sm_profiles_info - new plugin.
- networks_sm_target_groups - new plugin.
- networks_sm_target_groups_info - new plugin.
- networks_sm_trusted_access_configs_info - new plugin.
- networks_sm_user_access_devices_delete - new plugin.
- networks_sm_user_access_devices_info - new plugin.
- networks_sm_users_device_profiles_info - new plugin.
- networks_sm_users_info - new plugin.
- networks_sm_users_softwares_info - new plugin.
- networks_snmp - new plugin.
- networks_snmp_info - new plugin.
- networks_split - new plugin.
- networks_switch_access_control_lists - new plugin.
- networks_switch_access_control_lists_info - new plugin.
- networks_switch_access_policies - new plugin.
- networks_switch_access_policies_info - new plugin.
- networks_switch_alternate_management_interface - new plugin.
- networks_switch_alternate_management_interface_info - new plugin.
- networks_switch_dhcp_server_policy - new plugin.
- networks_switch_dhcp_server_policy_arp_inspection_trusted_servers - new plugin.
- networks_switch_dhcp_server_policy_arp_inspection_trusted_servers_info - new plugin.
- networks_switch_dhcp_server_policy_arp_inspection_warnings_by_device_info - new plugin.
- networks_switch_dhcp_server_policy_info - new plugin.
- networks_switch_dhcp_v4_servers_seen_info - new plugin.
- networks_switch_dscp_to_cos_mappings - new plugin.
- networks_switch_dscp_to_cos_mappings_info - new plugin.
- networks_switch_link_aggregations - new plugin.
- networks_switch_link_aggregations_info - new plugin.
- networks_switch_mtu - new plugin.
- networks_switch_mtu_info - new plugin.
- networks_switch_port_schedules - new plugin.
- networks_switch_port_schedules_info - new plugin.
- networks_switch_qos_rules_order - new plugin.
- networks_switch_qos_rules_order_info - new plugin.
- networks_switch_routing_multicast - new plugin.
- networks_switch_routing_multicast_info - new plugin.
- networks_switch_routing_multicast_rendezvous_points - new plugin.
- networks_switch_routing_multicast_rendezvous_points_info - new plugin.
- networks_switch_routing_ospf - new plugin.
- networks_switch_routing_ospf_info - new plugin.
- networks_switch_settings - new plugin.
- networks_switch_settings_info - new plugin.
- networks_switch_stacks - new plugin.
- networks_switch_stacks_add - new plugin.
- networks_switch_stacks_info - new plugin.
- networks_switch_stacks_remove - new plugin.
- networks_switch_stacks_routing_interfaces - new plugin.
- networks_switch_stacks_routing_interfaces_dhcp - new plugin.
- networks_switch_stacks_routing_interfaces_dhcp_info - new plugin.
- networks_switch_stacks_routing_interfaces_info - new plugin.
- networks_switch_stacks_routing_static_routes - new plugin.
- networks_switch_stacks_routing_static_routes_info - new plugin.
- networks_switch_storm_control - new plugin.
- networks_switch_storm_control_info - new plugin.
- networks_switch_stp - new plugin.
- networks_switch_stp_info - new plugin.
- networks_syslog_servers - new plugin.
- networks_syslog_servers_info - new plugin.
- networks_topology_link_layer_info - new plugin.
- networks_traffic_analysis - new plugin.
- networks_traffic_analysis_info - new plugin.
- networks_traffic_shaping_application_categories_info - new plugin.
- networks_traffic_shaping_dscp_tagging_options_info - new plugin.
- networks_unbind - new plugin.
- networks_webhooks_http_servers - new plugin.
- networks_webhooks_http_servers_info - new plugin.
- networks_webhooks_payload_templates - new plugin.
- networks_webhooks_payload_templates_info - new plugin.
- networks_webhooks_webhook_tests_info - new plugin.
- networks_wireless_alternate_management_interface - new plugin.
- networks_wireless_alternate_management_interface_info - new plugin.
- networks_wireless_billing - new plugin.
- networks_wireless_billing_info - new plugin.
- networks_wireless_bluetooth_settings - new plugin.
- networks_wireless_bluetooth_settings_info - new plugin.
- networks_wireless_channel_utilization_history_info - new plugin.
- networks_wireless_client_count_history_info - new plugin.
- networks_wireless_clients_connection_stats_info - new plugin.
- networks_wireless_clients_latency_stats_info - new plugin.
- networks_wireless_connection_stats_info - new plugin.
- networks_wireless_data_rate_history_info - new plugin.
- networks_wireless_devices_connection_stats_info - new plugin.
- networks_wireless_failed_connections_info - new plugin.
- networks_wireless_latency_history_info - new plugin.
- networks_wireless_latency_stats_info - new plugin.
- networks_wireless_mesh_statuses_info - new plugin.
- networks_wireless_rf_profiles - new plugin.
- networks_wireless_rf_profiles_info - new plugin.
- networks_wireless_settings - new plugin.
- networks_wireless_settings_info - new plugin.
- networks_wireless_signal_quality_history_info - new plugin.
- networks_wireless_ssids - new plugin.
- networks_wireless_ssids_bonjour_forwarding - new plugin.
- networks_wireless_ssids_bonjour_forwarding_info - new plugin.
- networks_wireless_ssids_device_type_group_policies - new plugin.
- networks_wireless_ssids_device_type_group_policies_info - new plugin.
- networks_wireless_ssids_eap_override - new plugin.
- networks_wireless_ssids_eap_override_info - new plugin.
- networks_wireless_ssids_firewall_l3_firewall_rules - new plugin.
- networks_wireless_ssids_firewall_l3_firewall_rules_info - new plugin.
- networks_wireless_ssids_firewall_l7_firewall_rules - new plugin.
- networks_wireless_ssids_firewall_l7_firewall_rules_info - new plugin.
- networks_wireless_ssids_hotspot20 - new plugin.
- networks_wireless_ssids_hotspot20_info - new plugin.
- networks_wireless_ssids_identity_psks - new plugin.
- networks_wireless_ssids_identity_psks_info - new plugin.
- networks_wireless_ssids_info - new plugin.
- networks_wireless_ssids_schedules - new plugin.
- networks_wireless_ssids_schedules_info - new plugin.
- networks_wireless_ssids_splash_settings - new plugin.
- networks_wireless_ssids_splash_settings_info - new plugin.
- networks_wireless_ssids_traffic_shaping_rules - new plugin.
- networks_wireless_ssids_traffic_shaping_rules_info - new plugin.
- networks_wireless_ssids_vpn - new plugin.
- networks_wireless_ssids_vpn_info - new plugin.
- networks_wireless_usage_history_info - new plugin.
- organizations - new plugin.
- organizations_action_batches - new plugin.
- organizations_action_batches_info - new plugin.
- organizations_adaptive_policy_acls - new plugin.
- organizations_adaptive_policy_acls_info - new plugin.
- organizations_adaptive_policy_groups - new plugin.
- organizations_adaptive_policy_groups_info - new plugin.
- organizations_adaptive_policy_overview_info - new plugin.
- organizations_adaptive_policy_policies - new plugin.
- organizations_adaptive_policy_policies_info - new plugin.
- organizations_adaptive_policy_settings - new plugin.
- organizations_adaptive_policy_settings_info - new plugin.
- organizations_admins - new plugin.
- organizations_admins_info - new plugin.
- organizations_alerts_profiles - new plugin.
- organizations_api_requests_info - new plugin.
- organizations_api_requests_overview_info - new plugin.
- organizations_api_requests_overview_response_codes_by_interval_info - new plugin.
- organizations_appliance_security_intrusion - new plugin.
- organizations_appliance_security_intrusion_info - new plugin.
- organizations_appliance_vpn_third_party_vpnpeers - new plugin.
- organizations_appliance_vpn_third_party_vpnpeers_info - new plugin.
- organizations_appliance_vpn_vpn_firewall_rules - new plugin.
- organizations_appliance_vpn_vpn_firewall_rules_info - new plugin.
- organizations_branding_policies - new plugin.
- organizations_branding_policies_info - new plugin.
- organizations_branding_policies_priorities - new plugin.
- organizations_branding_policies_priorities_info - new plugin.
- organizations_camera_custom_analytics_artifacts - new plugin.
- organizations_camera_custom_analytics_artifacts_info - new plugin.
- organizations_cellular_gateway_uplink_statuses_info - new plugin.
- organizations_claim - new plugin.
- organizations_clients_bandwidth_usage_history_info - new plugin.
- organizations_clients_overview_info - new plugin.
- organizations_clients_search_info - new plugin.
- organizations_clone - new plugin.
- organizations_config_templates - new plugin.
- organizations_config_templates_info - new plugin.
- organizations_config_templates_switch_profiles_info - new plugin.
- organizations_config_templates_switch_profiles_ports - new plugin.
- organizations_config_templates_switch_profiles_ports_info - new plugin.
- organizations_devices_availabilities_info - new plugin.
- organizations_devices_info - new plugin.
- organizations_devices_power_modules_statuses_by_device_info - new plugin.
- organizations_devices_provisioning_statuses_info - new plugin.
- organizations_devices_statuses_info - new plugin.
- organizations_devices_statuses_overview_info - new plugin.
- organizations_devices_uplinks_addresses_by_device_info - new plugin.
- organizations_devices_uplinks_loss_and_latency_info - new plugin.
- organizations_early_access_features_info - new plugin.
- organizations_early_access_features_opt_ins - new plugin.
- organizations_early_access_features_opt_ins_info - new plugin.
- organizations_firmware_upgrades_by_device_info - new plugin.
- organizations_firmware_upgrades_info - new plugin.
- organizations_info - new plugin.
- organizations_insight_applications_info - new plugin.
- organizations_insight_monitored_media_servers - new plugin.
- organizations_insight_monitored_media_servers_info - new plugin.
- organizations_inventory_claim - new plugin.
- organizations_inventory_devices_info - new plugin.
- organizations_inventory_onboarding_cloud_monitoring_export_events - new plugin.
- organizations_inventory_onboarding_cloud_monitoring_imports - new plugin.
- organizations_inventory_onboarding_cloud_monitoring_imports_info - new plugin.
- organizations_inventory_onboarding_cloud_monitoring_networks_info - new plugin.
- organizations_inventory_onboarding_cloud_monitoring_prepare - new plugin.
- organizations_inventory_release - new plugin.
- organizations_licenses - new plugin.
- organizations_licenses_assign_seats - new plugin.
- organizations_licenses_info - new plugin.
- organizations_licenses_move - new plugin.
- organizations_licenses_move_seats - new plugin.
- organizations_licenses_overview_info - new plugin.
- organizations_licenses_renew_seats - new plugin.
- organizations_licensing_coterm_licenses_info - new plugin.
- organizations_licensing_coterm_licenses_move - new plugin.
- organizations_login_security - new plugin.
- organizations_login_security_info - new plugin.
- organizations_networks_combine - new plugin.
- organizations_openapi_spec_info - new plugin.
- organizations_policy_objects - new plugin.
- organizations_policy_objects_groups - new plugin.
- organizations_policy_objects_groups_info - new plugin.
- organizations_policy_objects_info - new plugin.
- organizations_saml - new plugin.
- organizations_saml_idps - new plugin.
- organizations_saml_idps_info - new plugin.
- organizations_saml_info - new plugin.
- organizations_saml_roles - new plugin.
- organizations_saml_roles_info - new plugin.
- organizations_sensor_readings_history_info - new plugin.
- organizations_sensor_readings_latest_info - new plugin.
- organizations_sm_apns_cert_info - new plugin.
- organizations_sm_vpp_accounts_info - new plugin.
- organizations_snmp - new plugin.
- organizations_snmp_info - new plugin.
- organizations_summary_top_appliances_by_utilization_info - new plugin.
- organizations_summary_top_clients_by_usage_info - new plugin.
- organizations_summary_top_clients_manufacturers_by_usage_info - new plugin.
- organizations_summary_top_devices_by_usage_info - new plugin.
- organizations_summary_top_devices_models_by_usage_info - new plugin.
- organizations_summary_top_ssids_by_usage_info - new plugin.
- organizations_summary_top_switches_by_energy_usage_info - new plugin.
- organizations_switch_devices_clone - new plugin.
- organizations_switch_ports_by_switch_info - new plugin.
- organizations_uplinks_statuses_info - new plugin.
- organizations_users - new plugin.
- organizations_webhooks_logs_info - new plugin.
- organizations_wireless_devices_ethernet_statuses_info - new plugin.

community.general
~~~~~~~~~~~~~~~~~

- cobbler inventory plugin - add ``exclude_mgmt_classes`` and ``include_mgmt_classes`` options to exclude or include hosts based on management classes (https://github.com/ansible-collections/community.general/pull/7184).
- cpanm - minor refactor when creating the ``CmdRunner`` object (https://github.com/ansible-collections/community.general/pull/7231).
- gitlab_group_variable - add support for ``raw`` variables suboption (https://github.com/ansible-collections/community.general/pull/7132).
- gitlab_project_variable - add support for ``raw`` variables suboption (https://github.com/ansible-collections/community.general/pull/7132).
- jenkins_build - add new ``detach`` option, which allows the module to exit successfully as long as the build is created (default functionality is still waiting for the build to end before exiting) (https://github.com/ansible-collections/community.general/pull/7204).
- jenkins_build - add new ``time_between_checks`` option, which allows to configure the wait time between requests to the Jenkins server (https://github.com/ansible-collections/community.general/pull/7204).
- make - allows ``params`` to be used without value (https://github.com/ansible-collections/community.general/pull/7180).
- nmap inventory plugin - now has a ``use_arp_ping`` option to allow the user to disable the default ARP ping query for a more reliable form (https://github.com/ansible-collections/community.general/pull/7119).
- pagerduty - adds in option to use v2 API for creating pagerduty incidents (https://github.com/ansible-collections/community.general/issues/6151)
- pritunl module utils - ensure ``validate_certs`` parameter is honoured in all methods (https://github.com/ansible-collections/community.general/pull/7156).
- redfish_info - report ``Id`` in the output of ``GetManagerInventory`` (https://github.com/ansible-collections/community.general/pull/7140).
- redfish_utils module utils - support ``Volumes`` in response for ``GetDiskInventory`` (https://github.com/ansible-collections/community.general/pull/6819).
- unixy callback plugin - add support for ``check_mode_markers`` option (https://github.com/ansible-collections/community.general/pull/7179).

dellemc.powerflex
~~~~~~~~~~~~~~~~~

- Added Ansible role to support installation and uninstallation of LIA.
- Added Ansible role to support installation and uninstallation of MDM.
- Added Ansible role to support installation and uninstallation of SDS.
- Added Ansible role to support installation and uninstallation of TB.

grafana.grafana
~~~~~~~~~~~~~~~

- Add overrides.conf with CAP_NET_BIND_SERVICE for grafana-server unit
- Fix Grafana Dashboard Import for Grafana Role
- Fix grafana dashboard import in Grafana Role
- Make grafana_agent Idempotent
- Provisioning errors in YAML
- Use new standard to configure Grafana APT source for Grafana Role
- YAML Fixes

junipernetworks.junos
~~~~~~~~~~~~~~~~~~~~~

- add overridden state opperation support.

lowlydba.sqlserver
~~~~~~~~~~~~~~~~~~

- Added only_accessible as an optional parameter to the database module (https://github.com/lowlydba/lowlydba.sqlserver/pull/198)
- Fixes error handling for Remove-DbaDatabase when joined to AvailabilityGroup, exception was not being thrown so we have to parse Status

netbox.netbox
~~~~~~~~~~~~~

- API - Add possibility to use Bearer token [#1023](https://github.com/netbox-community/ansible_modules/pull/1023)
- custom fields - Add datetime as an custom field option [#1019](https://github.com/netbox-community/ansible_modules/pull/1019)
- netbox_cable - Add tenant [#1027](https://github.com/netbox-community/ansible_modules/pull/1027)
- netbox_circuit_type, netbox_device_interface - Add missing options [#1025](https://github.com/netbox-community/ansible_modules/pull/1025)
- netbox_custom_field - Add hidden-ifunset option [#1048](https://github.com/netbox-community/ansible_modules/pull/1048)
- netbox_inventory_item - Add role to module [#1050](https://github.com/netbox-community/ansible_modules/pull/1050)
- netbox_power_port - Add missing power port option [#1049](https://github.com/netbox-community/ansible_modules/pull/1049)

purestorage.flasharray
~~~~~~~~~~~~~~~~~~~~~~

- purefa_info - Add `hosts_balance` subset
- purefa_info - Add `port_connectivity` information for hosts
- purefa_info - Add promotion status information for volumes
- purefa_offload - Added a new profile parameter.
- purefa_pgsnap - Added new parameter to support snapshot throttling
- purefa_snap - Added new parameter to support snapshot throttling

purestorage.flashblade
~~~~~~~~~~~~~~~~~~~~~~

- purefb_policy - Add new and updated policy access rights

theforeman.foreman
~~~~~~~~~~~~~~~~~~

- compute_resource - add support for OpenStack
- repositories role - allow disabling/removing of repositories by setting the ``state`` parameter

Deprecated Features
-------------------

- The ``community.azure`` collection is officially unmaintained and has been archived. Therefore, it will be removed from Ansible 10. There is already a successor collection ``azure.azcollection`` in the community package which should cover the same functionality (https://github.com/ansible-community/community-topics/issues/263).
- The ``hpe.nimble`` collection is considered unmaintained and will be removed from Ansible 10 if no one starts maintaining it again before Ansible 10. See `the removal process for details on how this works <https://github.com/ansible-collections/overview/blob/main/removal_from_ansible.rst#cancelling-removal-of-an-unmaintained-collection>`__ (https://github.com/ansible-community/community-topics/issues/254).

Ansible-core
~~~~~~~~~~~~

- vault and unfault filters - the undocumented ``vaultid`` parameter is deprecated and will be removed in ansible-core 2.20. Use ``vault_id`` instead.

ansible.netcommon
~~~~~~~~~~~~~~~~~

- libssh - the ssh_*_args options are now marked that they will be removed after 2026-01-01.

Bugfixes
--------

Ansible-core
~~~~~~~~~~~~

- PowerShell - Remove some code which is no longer valid for dotnet 5+
- Prompting - add a short sleep between polling for user input to reduce CPU consumption (https://github.com/ansible/ansible/issues/81516).
- ansible-galaxy - Enabled the ``data`` tarfile filter during role installation for Python versions that support it. A probing mechanism is used to avoid Python versions with a broken implementation.
- ansible-test - Always use ansible-test managed entry points for ansible-core CLI tools when not running from source. This fixes issues where CLI entry points created during install are not compatible with ansible-test.
- first found lookup has been updated to use the normalized argument parsing (pythonic) matching the documented examples.
- handlers - the ``listen`` keyword can affect only one handler with the same name, the last one defined as it is a case with the ``notify`` keyword (https://github.com/ansible/ansible/issues/81013)
- include_role - expose variables from parent roles to role's handlers (https://github.com/ansible/ansible/issues/80459)
- tarfile - handle data filter deprecation warning message for extract and extractall (https://github.com/ansible/ansible/issues/80832).
- vault and unvault filters now properly take ``vault_id`` parameter.

amazon.aws
~~~~~~~~~~

- backup_selection - ensures that updating an existing selection will add new ``Conditions`` if there previously were not any (https://github.com/ansible-collections/amazon.aws/pull/1701).

ansible.netcommon
~~~~~~~~~~~~~~~~~

- Ensure that all connection plugin options that should be strings are actually strings (https://github.com/ansible-collections/ansible.netcommon/pull/549).
- Vendor telnetlib from cpython (https://github.com/ansible-collections/ansible.netcommon/pull/546)

ansible.utils
~~~~~~~~~~~~~

- Validate input for ipv4_hex(https://github.com/ansible-collections/ansible.utils/issues/281)

cisco.ise
~~~~~~~~~

- system_certificate - fixed get_object_by_id response.

community.aws
~~~~~~~~~~~~~

- opensearch - Don't try to read a non existing key from the domain config (https://github.com/ansible-collections/community.aws/pull/1910).

community.crypto
~~~~~~~~~~~~~~~~

- acme_* modules - correctly handle error documents without ``type`` (https://github.com/ansible-collections/community.crypto/issues/651, https://github.com/ansible-collections/community.crypto/pull/652).

community.dns
~~~~~~~~~~~~~

- Update Public Suffix List.

community.general
~~~~~~~~~~~~~~~~~

- CmdRunner module utils - does not attempt to resolve path if executable is a relative or absolute path (https://github.com/ansible-collections/community.general/pull/7200).
- nmap inventory plugin - now uses ``get_option`` in all cases to get its configuration information (https://github.com/ansible-collections/community.general/pull/7119).
- nsupdate - fix a possible ``list index out of range`` exception (https://github.com/ansible-collections/community.general/issues/836).
- oci_utils module util - fix inappropriate logical comparison expressions and makes them simpler. The previous checks had logical short circuits (https://github.com/ansible-collections/community.general/pull/7125).
- pritunl module utils - fix incorrect URL parameter for orgnization add method (https://github.com/ansible-collections/community.general/pull/7161).
- snap - an exception was being raised when snap list was empty (https://github.com/ansible-collections/community.general/pull/7124, https://github.com/ansible-collections/community.general/issues/7120).

community.sops
~~~~~~~~~~~~~~

- Avoid pre-releases when picking the latest version when using the GitHub API method (https://github.com/ansible-collections/community.sops/pull/159).
- Fix changed DEB and RPM URLs for 3.8.0 and its prerelease(s) (https://github.com/ansible-collections/community.sops/pull/159).

containers.podman
~~~~~~~~~~~~~~~~~

- podman_container - Add diff and change detection to systemd generation
- podman_container - Add example with quotes in command to docs
- podman_container - Fix healthcheck issue where defined in image
- podman_container - Fix idempoency issue with PID of container
- podman_container - Fix idempotency for RestartPolicy when MaximumRetryCount
- podman_container - Fix idempotency for devices
- podman_container - Fixed idempotency with cpus parameter
- podman_container - Improve docs about container env_file on remote machine
- podman_container - added cpu_quota parameter to podman_container
- podman_export,podman_import - Adding volume import and export option
- podman_generate_systemd - Add a force field to podman_generate_systemd
- podman_image - Add restart-sec and other options to systemd generation
- podman_image - Fix pulling short image name

f5networks.f5_modules
~~~~~~~~~~~~~~~~~~~~~

- bigip_ssl_key_cert - fixed flaw in code to make module work with same key and cert name when true_names set to true
- bigip_virtual_server - fixed an idempotency bug where the module send asm policy profile for update even when not specified explicitly by the user

fortinet.fortios
~~~~~~~~~~~~~~~~

- Fix the hyperlink issue for the supported FOS versions in USER's GUIDE.

junipernetworks.junos
~~~~~~~~~~~~~~~~~~~~~

- fix `no_advertise_adjacency_segment` config implementation.
- fix `no_eligible_backup` config implementation.
- fix `no_eligible_remote_backup` config implementation.
- fix `no_interface_state_traps` config implementation.
- fix `no_neighbor_down_notification` config implementation.
- fix `node_link_protection` implementation.
- fix md5 authentication which allows list of keys to be configured.

netbox.netbox
~~~~~~~~~~~~~

- Fix schema caching [#1053](https://github.com/netbox-community/ansible_modules/pull/1053)

ovirt.ovirt
~~~~~~~~~~~

- HE - add back dependency on python3-jmespath (https://github.com/oVirt/ovirt-ansible-collection/pull/701)
- HE - drop remaining filters using netaddr (https://github.com/oVirt/ovirt-ansible-collection/pull/702)
- HE - drop usage of ipaddr filters and remove dependency on python-netaddr (https://github.com/oVirt/ovirt-ansible-collection/pull/696)
- HE - fix ipv4 and ipv6 check after dropping netaddr (https://github.com/oVirt/ovirt-ansible-collection/pull/704)
- hosted_engine_setup -  Update README (https://github.com/oVirt/ovirt-ansible-collection/pull/706)
- ovirt_disk -  Fix issue in detaching the direct LUN (https://github.com/oVirt/ovirt-ansible-collection/pull/700)
- ovirt_quota - Convert storage size to integer (https://github.com/oVirt/ovirt-ansible-collection/pull/712)

purestorage.flasharray
~~~~~~~~~~~~~~~~~~~~~~

- purefa_certs - Resolved CSR issue and require export_file for state sign.
- purefa_info - Fix serial number generation issue for vVols
- purefa_snap - Fixed issue with remote snapshot retrieve. Mainly a workaround to an issue with Purity REST 1.x when remote snapshots are searched.
- purefa_volume - Fixed bug with NULL suffix for multiple volume creation.

purestorage.flashblade
~~~~~~~~~~~~~~~~~~~~~~

- purefb_info - Fixed missing atributes for SMB client policy rules

theforeman.foreman
~~~~~~~~~~~~~~~~~~

- content_view_publish role - correctly pass ``version`` not ``description`` to the module (https://bugzilla.redhat.com/show_bug.cgi?id=2234444)
- repository - don't fail when removing a content credential from a repository (https://bugzilla.redhat.com/show_bug.cgi?id=2224122)
- smart_class_parameter - correctly allow setting ``override`` to ``false`` (https://github.com/theforeman/foreman-ansible-modules/issues/1644)

vultr.cloud
~~~~~~~~~~~

- firewall_rule - Fixed an idempotency issue if parameter ``port`` is set on protocols other than TCP/UDP (https://github.com/vultr/ansible-collection-vultr/issues/76).

New Plugins
-----------

Cliconf
~~~~~~~

- ansible.netcommon.default - General purpose cliconf plugin for new platforms

Filter
~~~~~~

- ansible.utils.ipcut - This filter is designed to get 1st or last few bits of IP address.
- ansible.utils.ipv6form - This filter is designed to convert ipv6 address in different formats. For example expand, compressetc.

New Modules
-----------

amazon.aws
~~~~~~~~~~

- amazon.aws.ec2_key_info - Gather information about EC2 key pairs in AWS

community.aws
~~~~~~~~~~~~~

- community.aws.route53_wait - wait for changes in Amazons Route 53 DNS service to propagate

community.general
~~~~~~~~~~~~~~~~~

- community.general.jenkins_build_info - Get information about Jenkins builds
- community.general.pnpm - Manage node.js packages with pnpm

ngine_io.exoscale
~~~~~~~~~~~~~~~~~

- ngine_io.exoscale.instance_rdns_record - Manages reverse DNS records for Exoscale compute instances.

theforeman.foreman
~~~~~~~~~~~~~~~~~~

- theforeman.foreman.smart_class_parameter_override_value - Manage Smart Class Parameter Override Values
- theforeman.foreman.wait_for_task - Wait for a task

vultr.cloud
~~~~~~~~~~~

- vultr.cloud.bare_metal - Manages bare metal machines on Vultr.
- vultr.cloud.vpc2 - Manages VPCs 2.0 on Vultr
- vultr.cloud.vpc2_info - Gather information about the Vultr VPCs 2.0

Unchanged Collections
---------------------

- ansible.posix (still version 1.5.4)
- ansible.windows (still version 1.14.0)
- check_point.mgmt (still version 5.1.1)
- chocolatey.chocolatey (still version 1.5.1)
- cisco.aci (still version 2.7.0)
- cisco.asa (still version 4.0.1)
- cisco.intersight (still version 1.0.27)
- cisco.ios (still version 4.6.1)
- cisco.iosxr (still version 5.0.3)
- cisco.mso (still version 2.5.0)
- cisco.nso (still version 1.0.3)
- cisco.nxos (still version 4.4.0)
- cisco.ucs (still version 1.10.0)
- cloud.common (still version 2.1.4)
- cloudscale_ch.cloud (still version 2.3.1)
- community.azure (still version 2.0.0)
- community.ciscosmb (still version 1.0.6)
- community.digitalocean (still version 1.24.0)
- community.docker (still version 3.4.8)
- community.fortios (still version 1.0.0)
- community.google (still version 1.0.0)
- community.grafana (still version 1.5.4)
- community.hashi_vault (still version 5.0.0)
- community.hrobot (still version 1.8.1)
- community.libvirt (still version 1.2.0)
- community.mongodb (still version 1.6.1)
- community.mysql (still version 3.7.2)
- community.network (still version 5.0.0)
- community.okd (still version 2.3.0)
- community.postgresql (still version 2.4.3)
- community.proxysql (still version 1.5.1)
- community.rabbitmq (still version 1.2.3)
- community.routeros (still version 2.9.0)
- community.sap (still version 1.0.0)
- community.sap_libs (still version 1.4.1)
- community.skydive (still version 1.0.0)
- community.vmware (still version 3.9.0)
- community.windows (still version 1.13.0)
- community.zabbix (still version 2.1.0)
- cyberark.conjur (still version 1.2.0)
- cyberark.pas (still version 1.0.19)
- dellemc.enterprise_sonic (still version 2.2.0)
- dellemc.openmanage (still version 7.6.1)
- dellemc.unity (still version 1.7.1)
- fortinet.fortimanager (still version 2.2.1)
- frr.frr (still version 2.0.2)
- gluster.gluster (still version 1.0.2)
- google.cloud (still version 1.2.0)
- hetzner.hcloud (still version 1.16.0)
- hpe.nimble (still version 1.1.4)
- ibm.qradar (still version 2.1.0)
- ibm.spectrum_virtualize (still version 1.12.0)
- infinidat.infinibox (still version 1.3.12)
- infoblox.nios_modules (still version 1.5.0)
- inspur.ispim (still version 1.3.0)
- inspur.sm (still version 2.3.0)
- kubernetes.core (still version 2.4.0)
- microsoft.ad (still version 1.3.0)
- netapp.aws (still version 21.7.0)
- netapp.azure (still version 21.10.0)
- netapp.cloudmanager (still version 21.22.0)
- netapp.elementsw (still version 21.7.0)
- netapp.ontap (still version 22.7.0)
- netapp.storagegrid (still version 21.11.1)
- netapp.um_info (still version 21.8.0)
- netapp_eseries.santricity (still version 1.4.0)
- ngine_io.cloudstack (still version 2.3.0)
- ngine_io.vultr (still version 1.1.3)
- openstack.cloud (still version 2.1.0)
- openvswitch.openvswitch (still version 2.1.1)
- purestorage.fusion (still version 1.6.0)
- sensu.sensu_go (still version 1.14.0)
- servicenow.servicenow (still version 1.0.6)
- splunk.es (still version 2.1.0)
- t_systems_mms.icinga_director (still version 1.33.1)
- telekom_mms.icinga_director (still version 1.34.1)
- vmware.vmware_rest (still version 2.3.1)
- vyos.vyos (still version 4.1.0)
- wti.remote (still version 1.0.5)

v8.3.0
======

.. contents::
  :local:
  :depth: 2

Release Summary
---------------

Release Date: 2023-08-15

`Porting Guide <https://docs.ansible.com/ansible/devel/porting_guides.html>`_

Added Collections
-----------------

- telekom_mms.icinga_director (version 1.34.1)

Ansible-core
------------

Ansible 8.3.0 contains ansible-core version 2.15.3.
This is a newer version than version 2.15.2 contained in the previous Ansible release.

The changes are reported in the combined changelog below.

Changed Collections
-------------------

If not mentioned explicitly, the changes are reported in the combined changelog below.

+-----------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| Collection                  | Ansible 8.2.0 | Ansible 8.3.0 | Notes                                                                                                                        |
+=============================+===============+===============+==============================================================================================================================+
| amazon.aws                  | 6.2.0         | 6.3.0         |                                                                                                                              |
+-----------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| awx.awx                     | 22.5.0        | 22.6.0        | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+-----------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.aci                   | 2.6.0         | 2.7.0         |                                                                                                                              |
+-----------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.ise                   | 2.5.12        | 2.5.14        |                                                                                                                              |
+-----------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.mso                   | 2.4.0         | 2.5.0         |                                                                                                                              |
+-----------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.ucs                   | 1.9.0         | 1.10.0        | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+-----------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cloud.common                | 2.1.3         | 2.1.4         |                                                                                                                              |
+-----------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.aws               | 6.1.0         | 6.2.0         |                                                                                                                              |
+-----------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.crypto            | 2.14.1        | 2.15.0        |                                                                                                                              |
+-----------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.digitalocean      | 1.23.0        | 1.24.0        |                                                                                                                              |
+-----------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.dns               | 2.5.7         | 2.6.0         |                                                                                                                              |
+-----------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.general           | 7.2.0         | 7.3.0         |                                                                                                                              |
+-----------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.postgresql        | 2.4.2         | 2.4.3         |                                                                                                                              |
+-----------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.routeros          | 2.8.3         | 2.9.0         |                                                                                                                              |
+-----------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.vmware            | 3.8.0         | 3.9.0         |                                                                                                                              |
+-----------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| dellemc.unity               | 1.7.0         | 1.7.1         |                                                                                                                              |
+-----------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| f5networks.f5_modules       | 1.25.0        | 1.25.1        | There are no changes recorded in the changelog.                                                                              |
+-----------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| fortinet.fortimanager       | 2.2.0         | 2.2.1         |                                                                                                                              |
+-----------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| fortinet.fortios            | 2.3.0         | 2.3.1         |                                                                                                                              |
+-----------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| grafana.grafana             | 2.1.4         | 2.1.5         |                                                                                                                              |
+-----------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| lowlydba.sqlserver          | 2.0.0         | 2.1.0         |                                                                                                                              |
+-----------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| microsoft.ad                | 1.2.0         | 1.3.0         |                                                                                                                              |
+-----------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| purestorage.fusion          | 1.5.0         | 1.6.0         |                                                                                                                              |
+-----------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| sensu.sensu_go              | 1.13.2        | 1.14.0        |                                                                                                                              |
+-----------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| telekom_mms.icinga_director |               | 1.34.1        | The collection was added to Ansible                                                                                          |
+-----------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+

Major Changes
-------------

fortinet.fortios
~~~~~~~~~~~~~~~~

- Add readthedocs.yaml file.
- Update Q&A regarding setting up FortiToken multi-factor authentication;

Minor Changes
-------------

Ansible-core
~~~~~~~~~~~~

- Removed ``exclude`` and ``recursive-exclude`` commands for generated files from the ``MANIFEST.in`` file. These excludes were unnecessary since releases are expected to be built with a clean worktree.
- Removed ``exclude`` commands for sanity test files from the ``MANIFEST.in`` file. These tests were previously excluded because they did not pass when run from an sdist. However, sanity tests are not expected to pass from an sdist, so excluding some (but not all) of the failing tests makes little sense.
- Removed redundant ``include`` commands from the ``MANIFEST.in`` file. These includes either duplicated default behavior or another command.
- The ``ansible-core`` sdist no longer contains pre-generated man pages. Instead, a ``packaging/cli-doc/build.py`` script is included in the sdist. This script can generate man pages and standalone RST documentation for ``ansible-core`` CLI programs.
- The ``docs`` and ``examples`` directories are no longer included in the ``ansible-core`` sdist. These directories have been moved to the https://github.com/ansible/ansible-documentation repository.
- Use ``include`` where ``recursive-include`` is unnecessary in the ``MANIFEST.in`` file.
- ansible-test - Update the logic used to detect when ``ansible-test`` is running from source.
- ansible-test - Updated the CloudStack test container to version 1.6.1.

amazon.aws
~~~~~~~~~~

- rds_cluster - add support for another ``state`` choice called ``started``. This starts the rds cluster (https://github.com/ansible-collections/amazon.aws/pull/1647/files).
- rds_cluster - add support for another ``state`` choice called ``stopped``. This stops the rds cluster (https://github.com/ansible-collections/amazon.aws/pull/1647/files).
- route53 - add a ``wait_id`` return value when a change is done (https://github.com/ansible-collections/amazon.aws/pull/1683).
- route53_health_check - add support for a string list parameter called ``child_health_checks`` to specify health checks that must be healthy for the calculated health check (https://github.com/ansible-collections/amazon.aws/pull/1631).
- route53_health_check - add support for an integer parameter called ``health_threshold`` to specify the minimum number of healthy child health checks that must be healthy for the calculated health check (https://github.com/ansible-collections/amazon.aws/pull/1631).
- route53_health_check - add support for another ``type`` choice called ``CALCULATED`` (https://github.com/ansible-collections/amazon.aws/pull/1631).

cisco.aci
~~~~~~~~~

- Add ACI HTTPAPI plugin with multi host support (#114)
- Add OSPF parameters to aci_l3out module and create the associated test case.
- Add aci_access_span_src_group modules for access span source group support
- Add aci_access_span_src_group_src module for access span source support
- Add aci_access_span_src_group_src_path module for access span source path support
- Add aci_epg_subnet module (#424)
- Add aci_fabric_span_dst_group module for fabric span destination group support
- Add aci_fabric_span_src_group module for fabric span source group support
- Add aci_fabric_span_src_group_src module for fabric span source support
- Add aci_fabric_span_src_group_src_node module for fabric span source node support
- Add aci_fabric_span_src_group_src_path module for fabric span source path support
- Add aci_file_remote_path module (#379)
- Add aci_vrf_leak_internal_subnet module (#449)
- Add description parameter for aci_l3out_logical_interface_profile
- Add ip_data_plane_learning attribute to aci_bd_subnet and aci_vrf modules (#413)
- Add local_as_number_config and local_as_number attributes to support bgpLocalAsnP child object in aci_l3out_bgp_peer module (#416)
- Add node_type and remote_leaf_pool_id attributes to aci_fabric_node
- Add source_port, source_port_start, source_port_end, tcp_flags and match_only_fragments attributes to aci_filter_entry module (#426)

cisco.mso
~~~~~~~~~

- Add login domain attribute to mso httpapi connection plugin with restructure of connection parameter handling
- Add mso_schema_template_anp_epg_useg_attribute and mso_schema_site_anp_epg_useg_attribute modules to manage EPG uSeg attributes (#370)

community.aws
~~~~~~~~~~~~~

- api_gateway - add support for parameters ``name``, ``lookup``, ``tags`` and ``purge_tags`` (https://github.com/ansible-collections/community.aws/pull/1845).
- ec2_vpc_vpn - add support for connecting VPNs to a transit gateway (https://github.com/ansible-collections/community.aws/pull/1877).

community.crypto
~~~~~~~~~~~~~~~~

- openssh_keypair - fail when comment cannot be updated (https://github.com/ansible-collections/community.crypto/pull/646).

community.digitalocean
~~~~~~~~~~~~~~~~~~~~~~

- documentation - use C(true) and C(false) for boolean values in documentation and examples (https://github.com/ansible-collections/community.digitalocean/issues/303).
- inventory plugin - drop C(api_token) in favor of C(oauth_token) for consistency (https://github.com/ansible-collections/community.digitalocean/issues/300).
- tests - add C(sanity), C(units), and C(psf/black) back on merge into C(main) (https://github.com/ansible-collections/community.digitalocean/pull/311).
- tests - drop Ansible 2.9 and Ansible Core 2.10 and 2.11 (https://github.com/ansible-collections/community.digitalocean/pull/310).
- tests - remove the daily runs (https://github.com/ansible-collections/community.digitalocean/pull/310).
- tests - run C(psf/black) across all files (https://github.com/ansible-collections/community.digitalocean/pull/310).
- tests - test against Ansible Core 2.12, 2.13, and 2.14 (https://github.com/ansible-collections/community.digitalocean/pull/310).

community.dns
~~~~~~~~~~~~~

- wait_for_txt - add ``servfail_retries`` parameter that allows retrying after SERVFAIL errors (https://github.com/ansible-collections/community.dns/pull/159).
- wait_for_txt, resolver module utils - use `EDNS <https://en.wikipedia.org/wiki/Extension_Mechanisms_for_DNS>`__ (https://github.com/ansible-collections/community.dns/pull/158).

community.general
~~~~~~~~~~~~~~~~~

- chroot connection plugin - add ``disable_root_check`` option (https://github.com/ansible-collections/community.general/pull/7099).
- ejabberd_user - module now using ``CmdRunner`` to execute external command (https://github.com/ansible-collections/community.general/pull/7075).
- ipa_config - add module parameters to manage FreeIPA user and group objectclasses (https://github.com/ansible-collections/community.general/pull/7019).
- ipa_config - adds ``idp`` choice to ``ipauserauthtype`` parameter's choices (https://github.com/ansible-collections/community.general/pull/7051).
- npm - module now using ``CmdRunner`` to execute external commands (https://github.com/ansible-collections/community.general/pull/6989).
- proxmox_kvm - enabled force restart of VM, bringing the ``force`` parameter functionality in line with what is described in the docs (https://github.com/ansible-collections/community.general/pull/6914).
- proxmox_vm_info - ``node`` parameter is no longer required. Information can be obtained for the whole cluster (https://github.com/ansible-collections/community.general/pull/6976).
- proxmox_vm_info - non-existing provided by name/vmid VM would return empty results instead of failing (https://github.com/ansible-collections/community.general/pull/7049).
- redfish_config - add ``DeleteAllVolumes`` command to allow deletion of all volumes on servers (https://github.com/ansible-collections/community.general/pull/6814).
- redfish_utils - use ``Controllers`` key in redfish data to obtain Storage controllers properties (https://github.com/ansible-collections/community.general/pull/7081).
- redfish_utils module utils - add support for ``PowerCycle`` reset type for ``redfish_command`` responses feature (https://github.com/ansible-collections/community.general/issues/7083).
- redfish_utils module utils - add support for following ``@odata.nextLink`` pagination in ``software_inventory`` responses feature (https://github.com/ansible-collections/community.general/pull/7020).
- shutdown - use ``shutdown -p ...`` with FreeBSD to halt and power off machine (https://github.com/ansible-collections/community.general/pull/7102).
- sorcery - add grimoire (repository) management support (https://github.com/ansible-collections/community.general/pull/7012).

community.routeros
~~~~~~~~~~~~~~~~~~

- api_info, api_modify - add path ``caps-man channel`` and enable path ``caps-man manager interface`` (https://github.com/ansible-collections/community.routeros/issues/193, https://github.com/ansible-collections/community.routeros/pull/194).
- api_info, api_modify - add path ``ip traffic-flow target`` (https://github.com/ansible-collections/community.routeros/issues/191, https://github.com/ansible-collections/community.routeros/pull/192).

community.vmware
~~~~~~~~~~~~~~~~

- vmware_guest - add support for configuring vMotion and FT encryption (https://github.com/ansible-collections/community.vmware/issues/1069)
- vmware_host_datastore - added new datastore type 'vvol' for enabling creation/deletion of vVols datastores
- vmware_host_datastore - added new parameter resignature for supporting resignaturing an existing VMFS datastore on an imported/cloned LUN.
- vmware_vm_info -  Add `instance_uuid` to the result (https://github.com/ansible-collections/community.vmware/issues/1805)

dellemc.unity
~~~~~~~~~~~~~

- Patch update to fix import errors in utils file.

grafana.grafana
~~~~~~~~~~~~~~~

- Add Grafana Agent Version and CPU Arch to Downloaded ZIP in Grafana Agent Role
- Move _grafana_agent_base_download_url from /vars to /defaults in Grafana Agent Role

lowlydba.sqlserver
~~~~~~~~~~~~~~~~~~

- Add refresh workaround for agent schedule bug where properties returned are stale. (https://github.com/lowlydba/lowlydba.sqlserver/pull/185)
- Added SID as an optional parameter to the login module (https://github.com/lowlydba/lowlydba.sqlserver/pull/189)

microsoft.ad
~~~~~~~~~~~~

- AD objects will no longer be moved to the default AD path for their type if no ``path`` was specified. Use the value ``microsoft.ad.default_path`` to explicitly set the path to the default path if that behaviour is desired.
- microsoft.ad.ldap - Added the option ``filter_without_computer`` to not add the AND clause ``objectClass=computer`` to the final filter used - https://github.com/ansible-collections/microsoft.ad/issues/55

purestorage.fusion
~~~~~~~~~~~~~~~~~~

- all modules - return resource's id parameter on update and create.
- fusion_array - added `apartment_id` argument, which can be used when creating an array.
- fusion_pg - introduced `destroy_snapshots_on_delete` which, if set to true, ensures that before deleting placement group, snapshots within the placement group will be deleted.
- fusion_pp - 'local_rpo' duration parsing documented, 'local_retention' minimum value fixed
- fusion_pp - Allow leading zeros in duration strings
- fusion_pp - Change the minimum value of the protection policy local retention from 1 to 10
- fusion_pp - introduced `destroy_snapshots_on_delete` which, if set to true, ensures that before deleting protection policy, snapshots within the protection policy will be deleted.
- fusion_volume - Allow creating a new volume from already existing volume or volume snapshot

sensu.sensu_go
~~~~~~~~~~~~~~

- Added Docker file configurations for Ubuntu 20.04 and 22.04
- Added aditional parameters for Postgres resource to datastore module
- Added bcrypt check to user module
- Added docs for backends and package_name filter
- Added symlink for AlmaLinux.yml for alma linux 9 support

Deprecated Features
-------------------

- The collection ``t_systems_mms.icinga_director`` has been renamed to ``telekom_mms.icinga_director``. For now both collections are included in Ansible. The content in ``t_systems_mms.icinga_director`` will be replaced with deprecated redirects to the new collection in Ansible 9.0.0, and these redirects will eventually be removed from Ansible. Please update your FQCNs for ``t_systems_mms.icinga_director``.
- The netapp.azure collection is considered unmaintained and will be removed from Ansible 10 if no one starts maintaining it again before Ansible 10. See `the removal process for details on how this works <https://github.com/ansible-collections/overview/blob/main/removal_from_ansible.rst#cancelling-removal-of-an-unmaintained-collection>`__ (https://github.com/ansible-community/community-topics/issues/234).
- The netapp.elementsw collection is considered unmaintained and will be removed from Ansible 10 if no one starts maintaining it again before Ansible 10. See `the removal process for details on how this works <https://github.com/ansible-collections/overview/blob/main/removal_from_ansible.rst#cancelling-removal-of-an-unmaintained-collection>`__ (https://github.com/ansible-community/community-topics/issues/235).
- The netapp.um_info collection is considered unmaintained and will be removed from Ansible 10 if no one starts maintaining it again before Ansible 10. See `the removal process for details on how this works <https://github.com/ansible-collections/overview/blob/main/removal_from_ansible.rst#cancelling-removal-of-an-unmaintained-collection>`__ (https://github.com/ansible-community/community-topics/issues/244).
- The ngine_io.vultr collection is officially unmaintained and has been archived. Therefore, it will be removed from Ansible 9. There is already a successor collection ``vultr.cloud`` (using the recent v2 Vultr API) in the community package which covers the functionality but might not have compatible syntax (https://github.com/ansible-community/community-topics/issues/257).

community.crypto
~~~~~~~~~~~~~~~~

- get_certificate - the default ``false`` of the ``asn1_base64`` option is deprecated and will change to ``true`` in community.crypto 3.0.0 (https://github.com/ansible-collections/community.crypto/pull/600).

community.general
~~~~~~~~~~~~~~~~~

- ejabberd_user - deprecate the parameter ``logging`` in favour of producing more detailed information in the module output (https://github.com/ansible-collections/community.general/pull/7043).

community.postgresql
~~~~~~~~~~~~~~~~~~~~

- postgresql_lang - the module has been deprecated and will be removed in ``community.postgresql 4.0.0``. Please use the ``postgresql_ext`` module instead (https://github.com/ansible-collections/community.postgresql/issues/559).

Bugfixes
--------

Ansible-core
~~~~~~~~~~~~

- Exclude internal options from man pages and docs.
- Fix ``ansible-config init`` man page option indentation.
- The ``ansible-config init`` command now has a documentation description.
- The ``ansible-galaxy collection download`` command now has a documentation description.
- The ``ansible-galaxy collection install`` command documentation is now visible (previously hidden by a decorator).
- The ``ansible-galaxy collection verify`` command now has a documentation description.
- The ``ansible-galaxy role install`` command documentation is now visible (previously hidden by a decorator).
- The ``ansible-inventory`` command command now has a documentation description (previously used as the epilog).
- Update module_utils.urls unit test to work with cryptography >= 41.0.0.
- When generating man pages, use ``func`` to find the command function instead of looking it up by the command name.
- ``ansible-galaxy`` now considers all collection paths when identifying which collection requirements are already installed. Use the ``COLLECTIONS_PATHS`` and ``COLLECTIONS_SCAN_SYS_PATHS`` config options to modify these. Previously only the install path was considered when resolving the candidates. The install path will remain the only one potentially modified. (https://github.com/ansible/ansible/issues/79767, https://github.com/ansible/ansible/issues/81163)
- ansible-test - Fix several possible tracebacks when using the ``-e`` option with sanity tests.
- ansible-test - Pre-build a PyYAML wheel before installing requirements to avoid a potential Cython build failure.
- ansible-test - Remove redundant warning about missing programs before attempting to execute them.
- core will now also look at the connection plugin to force 'local' interpreter for networking path compatibility as just ansible_network_os could be misleading.
- man page build - Sub commands of ``ansible-galaxy role`` and ``ansible-galaxy collection`` are now documented.
- password_hash - fix salt format for ``crypt``  (only used if ``passlib`` is not installed) for the ``bcrypt`` algorithm.
- urls.py - fixed cert_file and key_file parameters when running on Python 3.12 - https://github.com/ansible/ansible/issues/80490

amazon.aws
~~~~~~~~~~

- ec2_vpc_route_table_info - default filters to empty dictionary (https://github.com/ansible-collections/amazon.aws/issues/1668).
- rds_cluster - Add ``AllocatedStorage``, ``DBClusterInstanceClass``, ``StorageType``, ``Iops``, and ``EngineMode`` to the list of parameters that can be passed when creating or modifying a Multi-AZ RDS cluster (https://github.com/ansible-collections/amazon.aws/pull/1657).
- rds_cluster - Allow to pass GlobalClusterIdentifier to rds cluster on creation (https://github.com/ansible-collections/amazon.aws/pull/1663).

cisco.aci
~~~~~~~~~

- Change input of prefix_suppression to type string to allow enable, disable and inherit options for aci_interface_policy_ospf

cisco.ise
~~~~~~~~~

- Cannot get cisco.ise.rest_id_store to work fixed.
- System Certificate Update does not work but always reports Object already present temporary solution.
- cisco.ise.mnt_session_active_count_info ise_reponse is null fixed.
- node_deployment tasks fail because of timeout, adding new collection param.
- system_certificate - added support for none value in the used_by param.

cisco.mso
~~~~~~~~~

- Fix mso_tenant_site "site not found" issue on absent (#368)

cloud.common
~~~~~~~~~~~~

- Ensure result is always defined in lookup plugins (https://github.com/ansible-collections/cloud.common/pull/116/files).
- Fix lookup modules failing on Ansible 2.15 (https://github.com/ansible-collections/cloud.common/pull/130).

community.aws
~~~~~~~~~~~~~

- Remove ``apigateway`` and ``apigateway_deployment`` from meta/runtime.yml (https://github.com/ansible-collections/community.aws/pull/1905).

community.crypto
~~~~~~~~~~~~~~~~

- openssh_cert, openssh_keypair - the modules ignored return codes of ``ssh`` and ``ssh-keygen`` in some cases (https://github.com/ansible-collections/community.crypto/issues/645, https://github.com/ansible-collections/community.crypto/pull/646).
- openssh_keypair - fix comment updating for OpenSSH before 6.5 (https://github.com/ansible-collections/community.crypto/pull/646).

community.digitalocean
~~~~~~~~~~~~~~~~~~~~~~

- digital_ocean_domain - fix ``all_domains`` by using ``get_paginated_data`` to retrieve all of the domains in the account from the paginated domains api endpoint (https://github.com/ansible-collections/community.digitalocean/pull/307).

community.dns
~~~~~~~~~~~~~

- Update Public Suffix List.
- wait_for_txt, resolver module utils - improve error handling (https://github.com/ansible-collections/community.dns/pull/158).

community.general
~~~~~~~~~~~~~~~~~

- bitwarden lookup plugin - the plugin made assumptions about the structure of a Bitwarden JSON object which may have been broken by an update in the Bitwarden API. Remove assumptions, and allow queries for general fields such as ``notes`` (https://github.com/ansible-collections/community.general/pull/7061).
- cmd_runner module utils - when a parameter in ``argument_spec`` has no type, meaning it is implicitly a ``str``, ``CmdRunner`` would fail trying to find the ``type`` key in that dictionary (https://github.com/ansible-collections/community.general/pull/6968).
- ejabberd_user - module was failing to detect whether user was already created and/or password was changed (https://github.com/ansible-collections/community.general/pull/7033).
- ejabberd_user - provide meaningful error message when the ``ejabberdctl`` command is not found (https://github.com/ansible-collections/community.general/pull/7028, https://github.com/ansible-collections/community.general/issues/6949).
- keycloak module util - fix missing ``http_agent``, ``timeout``, and ``validate_certs`` ``open_url()`` parameters (https://github.com/ansible-collections/community.general/pull/7067).
- keycloak_client inventory plugin - fix missing client secret (https://github.com/ansible-collections/community.general/pull/6931).
- lvol - add support for percentage of origin size specification when creating snapshot volumes (https://github.com/ansible-collections/community.general/issues/1630, https://github.com/ansible-collections/community.general/pull/7053).
- lxc connection plugin - now handles ``remote_addr`` defaulting to ``inventory_hostname`` correctly (https://github.com/ansible-collections/community.general/pull/7104).
- oci_utils module utils - avoid direct type comparisons (https://github.com/ansible-collections/community.general/pull/7085).
- proxmox module utils - fix proxmoxer library version check (https://github.com/ansible-collections/community.general/issues/6974, https://github.com/ansible-collections/community.general/issues/6975, https://github.com/ansible-collections/community.general/pull/6980).
- proxmox_kvm - when ``name`` option is provided without ``vmid`` and VM with that name already exists then no new VM will be created (https://github.com/ansible-collections/community.general/issues/6911, https://github.com/ansible-collections/community.general/pull/6981).
- proxmox_user_info - avoid direct type comparisons (https://github.com/ansible-collections/community.general/pull/7085).
- rundeck - fix ``TypeError`` on 404 API response (https://github.com/ansible-collections/community.general/pull/6983).
- snap - fix crash when multiple snaps are specified and one has ``---`` in its description (https://github.com/ansible-collections/community.general/pull/7046).
- sorcery - fix interruption of the multi-stage process (https://github.com/ansible-collections/community.general/pull/7012).
- sorcery - fix queue generation before the whole system rebuild (https://github.com/ansible-collections/community.general/pull/7012).
- sorcery - latest state no longer triggers update_cache (https://github.com/ansible-collections/community.general/pull/7012).

community.postgresql
~~~~~~~~~~~~~~~~~~~~

- postgresql_set - fixed error message in param_set function (https://github.com/ansible-collections/community.postgresql/pull/505).

community.routeros
~~~~~~~~~~~~~~~~~~

- api_modify, api_info - add missing parameter ``engine-id-suffix`` for the ``snmp`` path (https://github.com/ansible-collections/community.routeros/issues/189, https://github.com/ansible-collections/community.routeros/pull/190).

fortinet.fortimanager
~~~~~~~~~~~~~~~~~~~~~

- Fix a bug where the user may not be able to use workspace_locking_adom if the workspace mode is per-adom.
- Improve login logic in httpapi plugin.

fortinet.fortios
~~~~~~~~~~~~~~~~

- Fix the issue while comparing the changes in before and after data in check_mode;
- Fix the issues that some parameters are not in a specific fos vm versions.
- Fix the request error when updating global object;
- Fix the sanity test error;
- Fix the wrong credential error when using username/password in fos verion 6;

microsoft.ad
~~~~~~~~~~~~

- Added the missing dependency ``dpapi-ng`` to Ansible Execution Environments requirements file for LAPS decryption support
- Ensure renaming and moving an object will be done with the ``domain_server`` and ``domain_username`` credentials specified - https://github.com/ansible-collections/microsoft.ad/issues/54
- Fix up ``protect_from_deletion`` when creating new AD objects - https://github.com/ansible-collections/microsoft.ad/issues/47
- Fix up date_time attribute comparisons to be idempotent - https://github.com/ansible-collections/microsoft.ad/issues/57
- microsoft.ad.user - Ensure the ``spn`` diff after key is ``spn`` and not ``kerberos_encryption_types``
- microsoft.ad.user - treat an expired account as a password that needs to be changed

New Plugins
-----------

Filter
~~~~~~

- community.crypto.gpg_fingerprint - Retrieve a GPG fingerprint from a GPG public or private key

Lookup
~~~~~~

- community.crypto.gpg_fingerprint - Retrieve a GPG fingerprint from a GPG public or private key file
- community.dns.lookup - Look up DNS records
- community.dns.lookup_as_dict - Look up DNS records as dictionaries

New Modules
-----------

community.dns
~~~~~~~~~~~~~

- community.dns.nameserver_info - Look up nameservers for a DNS name
- community.dns.nameserver_record_info - Look up all records of a type from all nameservers for a DNS name

sensu.sensu_go
~~~~~~~~~~~~~~

- sensu.sensu_go.pipeline - Manage Sensu pipelines.
- sensu.sensu_go.pipeline_info - List Sensu pipelines.

Unchanged Collections
---------------------

- ansible.netcommon (still version 5.1.2)
- ansible.posix (still version 1.5.4)
- ansible.utils (still version 2.10.3)
- ansible.windows (still version 1.14.0)
- arista.eos (still version 6.0.1)
- azure.azcollection (still version 1.16.0)
- check_point.mgmt (still version 5.1.1)
- chocolatey.chocolatey (still version 1.5.1)
- cisco.asa (still version 4.0.1)
- cisco.dnac (still version 6.7.3)
- cisco.intersight (still version 1.0.27)
- cisco.ios (still version 4.6.1)
- cisco.iosxr (still version 5.0.3)
- cisco.meraki (still version 2.15.3)
- cisco.nso (still version 1.0.3)
- cisco.nxos (still version 4.4.0)
- cloudscale_ch.cloud (still version 2.3.1)
- community.azure (still version 2.0.0)
- community.ciscosmb (still version 1.0.6)
- community.docker (still version 3.4.8)
- community.fortios (still version 1.0.0)
- community.google (still version 1.0.0)
- community.grafana (still version 1.5.4)
- community.hashi_vault (still version 5.0.0)
- community.hrobot (still version 1.8.1)
- community.libvirt (still version 1.2.0)
- community.mongodb (still version 1.6.1)
- community.mysql (still version 3.7.2)
- community.network (still version 5.0.0)
- community.okd (still version 2.3.0)
- community.proxysql (still version 1.5.1)
- community.rabbitmq (still version 1.2.3)
- community.sap (still version 1.0.0)
- community.sap_libs (still version 1.4.1)
- community.skydive (still version 1.0.0)
- community.sops (still version 1.6.4)
- community.windows (still version 1.13.0)
- community.zabbix (still version 2.1.0)
- containers.podman (still version 1.10.2)
- cyberark.conjur (still version 1.2.0)
- cyberark.pas (still version 1.0.19)
- dellemc.enterprise_sonic (still version 2.2.0)
- dellemc.openmanage (still version 7.6.1)
- dellemc.powerflex (still version 1.7.0)
- frr.frr (still version 2.0.2)
- gluster.gluster (still version 1.0.2)
- google.cloud (still version 1.2.0)
- hetzner.hcloud (still version 1.16.0)
- hpe.nimble (still version 1.1.4)
- ibm.qradar (still version 2.1.0)
- ibm.spectrum_virtualize (still version 1.12.0)
- infinidat.infinibox (still version 1.3.12)
- infoblox.nios_modules (still version 1.5.0)
- inspur.ispim (still version 1.3.0)
- inspur.sm (still version 2.3.0)
- junipernetworks.junos (still version 5.2.0)
- kubernetes.core (still version 2.4.0)
- netapp.aws (still version 21.7.0)
- netapp.azure (still version 21.10.0)
- netapp.cloudmanager (still version 21.22.0)
- netapp.elementsw (still version 21.7.0)
- netapp.ontap (still version 22.7.0)
- netapp.storagegrid (still version 21.11.1)
- netapp.um_info (still version 21.8.0)
- netapp_eseries.santricity (still version 1.4.0)
- netbox.netbox (still version 3.13.0)
- ngine_io.cloudstack (still version 2.3.0)
- ngine_io.exoscale (still version 1.0.0)
- ngine_io.vultr (still version 1.1.3)
- openstack.cloud (still version 2.1.0)
- openvswitch.openvswitch (still version 2.1.1)
- ovirt.ovirt (still version 3.1.2)
- purestorage.flasharray (still version 1.20.0)
- purestorage.flashblade (still version 1.12.1)
- servicenow.servicenow (still version 1.0.6)
- splunk.es (still version 2.1.0)
- t_systems_mms.icinga_director (still version 1.33.1)
- theforeman.foreman (still version 3.12.0)
- vmware.vmware_rest (still version 2.3.1)
- vultr.cloud (still version 1.8.0)
- vyos.vyos (still version 4.1.0)
- wti.remote (still version 1.0.5)

v8.2.0
======

.. contents::
  :local:
  :depth: 2

Release Summary
---------------

Release Date: 2023-07-18

`Porting Guide <https://docs.ansible.com/ansible/devel/porting_guides.html>`_

Ansible-core
------------

Ansible 8.2.0 contains ansible-core version 2.15.2.
This is a newer version than version 2.15.1 contained in the previous Ansible release.

The changes are reported in the combined changelog below.

Changed Collections
-------------------

If not mentioned explicitly, the changes are reported in the combined changelog below.

+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| Collection             | Ansible 8.1.0 | Ansible 8.2.0 | Notes                                                                                                                        |
+========================+===============+===============+==============================================================================================================================+
| amazon.aws             | 6.1.0         | 6.2.0         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| ansible.netcommon      | 5.1.1         | 5.1.2         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| awx.awx                | 22.3.0        | 22.5.0        | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| chocolatey.chocolatey  | 1.4.0         | 1.5.1         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.dnac             | 6.7.2         | 6.7.3         | The collection did not have a changelog in this version.                                                                     |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.meraki           | 2.15.1        | 2.15.3        |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.ucs              | 1.8.0         | 1.9.0         | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.aws          | 6.0.0         | 6.1.0         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.crypto       | 2.14.0        | 2.14.1        |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.dns          | 2.5.6         | 2.5.7         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.general      | 7.1.0         | 7.2.0         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.hrobot       | 1.8.0         | 1.8.1         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.mongodb      | 1.6.0         | 1.6.1         | There are no changes recorded in the changelog.                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.routeros     | 2.8.2         | 2.8.3         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.sops         | 1.6.2         | 1.6.4         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.vmware       | 3.7.0         | 3.8.0         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.zabbix       | 2.0.1         | 2.1.0         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| dellemc.powerflex      | 1.6.0         | 1.7.0         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| dellemc.unity          | 1.6.0         | 1.7.0         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| google.cloud           | 1.1.3         | 1.2.0         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| grafana.grafana        | 2.0.0         | 2.1.4         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| hetzner.hcloud         | 1.11.0        | 1.16.0        |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| junipernetworks.junos  | 5.1.0         | 5.2.0         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| purestorage.flasharray | 1.19.1        | 1.20.0        |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| purestorage.flashblade | 1.11.0        | 1.12.1        |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| theforeman.foreman     | 3.11.0        | 3.12.0        |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+

Major Changes
-------------

chocolatey.chocolatey
~~~~~~~~~~~~~~~~~~~~~

- win_chocolatey - add options for specifying checksums
- win_chocolatey_facts - add filter / gather_subset option

community.vmware
~~~~~~~~~~~~~~~~

- vmware_vasa - added a new module to register/unregister a VASA provider
- vmware_vasa_info - added a new module to gather the information about existing VASA provider(s)

grafana.grafana
~~~~~~~~~~~~~~~

- Addition of Grafana Server role by @gardar
- Configurable agent user groups by @NormanJS
- Grafana Plugins support on-prem Grafana installation by @ishanjainn
- Updated Service for flow mode by @bentonam

Minor Changes
-------------

Ansible-core
~~~~~~~~~~~~

- Utilize gpg check provided internally by the ``transaction.run`` method as oppose to calling it manually.
- ansible-test - Add Fedora 38 remote.
- ansible-test - Use a context manager to perform cleanup at exit instead of using the built-in ``atexit`` module.
- dnf5 - enable environment groups installation testing in CI as its support was added.
- dnf5 - enable now implemented ``cacheonly`` functionality

amazon.aws
~~~~~~~~~~

- backup_selection - add validation and documentation for all conditions suboptions (https://github.com/ansible-collections/amazon.aws/pull/1633).
- ec2_instance - refactored ARN validation handling (https://github.com/ansible-collections/amazon.aws/pull/1619).
- iam_user - refactored ARN validation handling (https://github.com/ansible-collections/amazon.aws/pull/1619).
- module_utils.arn - add ``resource_id`` and ``resource_type`` to ``parse_aws_arn`` return values (https://github.com/ansible-collections/amazon.aws/pull/1619).
- module_utils.arn - added ``validate_aws_arn`` function to handle common pattern matching for ARNs (https://github.com/ansible-collections/amazon.aws/pull/1619).

chocolatey.chocolatey
~~~~~~~~~~~~~~~~~~~~~

- All modules - Ensure modules are compatible with both Chocolatey CLI v2.x and v1.x
- win_chocolatey - Improve error messages when installation of Chocolatey CLI v2.x fails due to unmet .NET Framework 4.8 dependency on client

cisco.meraki
~~~~~~~~~~~~

- meraki_mx_site_to_site_firewall - Fix updating VPN rules per issue 302.

community.aws
~~~~~~~~~~~~~

- dynamodb_table - added waiter when updating indexes to avoid concurrency issues (https://github.com/ansible-collections/community.aws/pull/1866).
- dynamodb_table - increased default timeout based on time to update indexes in CI (https://github.com/ansible-collections/community.aws/pull/1866).
- iam_group - refactored ARN validation handling (https://github.com/ansible-collections/community.aws/pull/1848).
- iam_role - refactored ARN validation handling (https://github.com/ansible-collections/community.aws/pull/1848).
- sns_topic - refactored ARN validation handling (https://github.com/ansible-collections/community.aws/pull/1848).

community.general
~~~~~~~~~~~~~~~~~

- cobbler inventory plugin - convert Ansible unicode strings to native Python unicode strings before passing user/password to XMLRPC client (https://github.com/ansible-collections/community.general/pull/6923).
- consul_session - drops requirement for the ``python-consul`` library to communicate with the Consul API, instead relying on the existing ``requests`` library requirement (https://github.com/ansible-collections/community.general/pull/6755).
- gitlab_project_variable - minor refactor removing unnecessary code statements (https://github.com/ansible-collections/community.general/pull/6928).
- gitlab_runner - minor refactor removing unnecessary code statements (https://github.com/ansible-collections/community.general/pull/6927).
- htpasswd - the parameter ``crypt_scheme`` is being renamed as ``hash_scheme`` and added as an alias to it (https://github.com/ansible-collections/community.general/pull/6841).
- keycloak_authentication - added provider ID choices, since Keycloak supports only those two specific ones (https://github.com/ansible-collections/community.general/pull/6763).
- keyring - minor refactor removing unnecessary code statements (https://github.com/ansible-collections/community.general/pull/6927).
- locale_gen - module has been refactored to use ``ModuleHelper`` and ``CmdRunner`` (https://github.com/ansible-collections/community.general/pull/6903).
- locale_gen - module now using ``CmdRunner`` to execute external commands (https://github.com/ansible-collections/community.general/pull/6820).
- make - add new ``targets`` parameter allowing multiple targets to be used with ``make`` (https://github.com/ansible-collections/community.general/pull/6882, https://github.com/ansible-collections/community.general/issues/4919).
- nmcli - add support for ``ipv4.dns-options`` and ``ipv6.dns-options`` (https://github.com/ansible-collections/community.general/pull/6902).
- npm - minor improvement on parameter validation (https://github.com/ansible-collections/community.general/pull/6848).
- opkg - add ``executable`` parameter allowing to specify the path of the ``opkg`` command (https://github.com/ansible-collections/community.general/pull/6862).
- pubnub_blocks - minor refactor removing unnecessary code statements (https://github.com/ansible-collections/community.general/pull/6928).
- redfish_command - add ``account_types`` and ``oem_account_types`` as optional inputs to ``AddUser`` (https://github.com/ansible-collections/community.general/issues/6823, https://github.com/ansible-collections/community.general/pull/6871).
- redfish_info - add ``AccountTypes`` and ``OEMAccountTypes`` to the output of ``ListUsers`` (https://github.com/ansible-collections/community.general/issues/6823, https://github.com/ansible-collections/community.general/pull/6871).
- redfish_info - adds ``ProcessorArchitecture`` to CPU inventory (https://github.com/ansible-collections/community.general/pull/6864).
- redfish_info - fix for ``GetVolumeInventory``, Controller name was getting populated incorrectly and duplicates were seen in the volumes retrieved (https://github.com/ansible-collections/community.general/pull/6719).
- rhsm_repository - the interaction with ``subscription-manager`` was
  refactored by grouping things together, removing unused bits, and hardening
  the way it is run; also, the parsing of ``subscription-manager repos --list``
  was improved and made slightly faster; no behaviour change is expected
  (https://github.com/ansible-collections/community.general/pull/6783,
  https://github.com/ansible-collections/community.general/pull/6837).
- scaleway_security_group_rule - minor refactor removing unnecessary code statements (https://github.com/ansible-collections/community.general/pull/6928).
- snap - add option ``dangerous`` to the module, that will map into the command line argument ``--dangerous``, allowing unsigned snap files to be installed (https://github.com/ansible-collections/community.general/pull/6908, https://github.com/ansible-collections/community.general/issues/5715).
- tss lookup plugin - allow to fetch secret by path. Previously, we could not fetch secret by path but now use ``secret_path`` option to indicate to fetch secret by secret path (https://github.com/ansible-collections/community.general/pull/6881).
- xenserver_guest_info - minor refactor removing unnecessary code statements (https://github.com/ansible-collections/community.general/pull/6928).
- xenserver_guest_powerstate - minor refactor removing unnecessary code statements (https://github.com/ansible-collections/community.general/pull/6928).
- yum_versionlock - add support to pin specific package versions instead of only the package itself (https://github.com/ansible-collections/community.general/pull/6861, https://github.com/ansible-collections/community.general/issues/4470).

community.vmware
~~~~~~~~~~~~~~~~

- autoselect_datastore - add support to also look at NFS mounted filesystems (previously was just VMFS)

community.zabbix
~~~~~~~~~~~~~~~~

- Multiple Roles - Replaced depricated 'include' statements with 'include_tasks'
- Update action_groups variable in runtime.yml
- all roles - Added support for Debian 12 (Bookworm)
- all roles - Delete gpg ids variable.
- all roles - Modified to allow a non-root user to run the role.
- all roles - Updated testing to account for the correct version of Zabbix
- zabbix_hostmacro module - Add description property for Host macro creation/update. Allow to set/update description of Zabbix host macros.
- zabbix_proxy - Added installation of PyMySQL pip package
- zabbix_proxy - Modified installation of Centos 7 MySQL client
- zabbix_proxy - Standardized MySQL client installed on Debian and Ubuntu
- zabbix_regexp module added
- zabbix_settings module added
- zabbix_token module added

dellemc.powerflex
~~~~~~~~~~~~~~~~~

- Added Ansible role to support installation and uninstallation of SDC.
- Added sample playbooks for the modules.
- Device module is enhanced to support force addition of device to the SDS.
- Info module is enhanced to list statistics in snapshot policies.
- Replication consistency group module is enhanced to support failover, restore, reverse, switchover, and sync operations.
- SDC module is enhanced to configure performance profile and to remove SDC.
- Updated modules to adhere with ansible community guidelines.

dellemc.unity
~~~~~~~~~~~~~

- Added replication session module to get details, pause, resume, sync, failover, failback and delete replication sessions.
- Added support for Unity XT SeaHawk 5.3
- Documentation updates for boolean values based on ansible community guidelines.

google.cloud
~~~~~~~~~~~~

- Add DataPlane V2 Support.
- Add auth support for GCP access tokens (#574).
- Add support for ip_allocation_policy->stack_type.

grafana.grafana
~~~~~~~~~~~~~~~

- Ability to configure date format in grafana server role by @RomainMou
- Avoid using shell for fetching latest version in Grafana Agent Role by @gardar
- Datasource test updates and minor fixes
- Fix Deleting datasources
- Fix alert_notification_policy failing on fresh instance
- Fix for invalid yaml with datasources list enclosed in quotes by @elkozmon
- Making Deleting folders idempotent
- Remove agent installation custom check by @VLZZZ
- Remove explicit user creation check by @v-zhuravlev
- Remove trailing slash automatically from grafana_url
- Update Download tasks in Grafana Agent Role
- indentation and Lint fixes to modules

hetzner.hcloud
~~~~~~~~~~~~~~

- Bundle hcloud python dependency inside the collection.
- hcloud_iso_info Create hcloud_iso_info module
- hcloud_network Add expose_routes_to_vswitch field.
- hcloud_network_info Return expose_routes_to_vswitch for network.
- hcloud_primary_ip_info Create hcloud_primary_ip_info module
- hcloud_server Show warning if used server_type is deprecated.
- hcloud_server_type_info - Add field included_traffic to returned server types
- hcloud_server_type_info Return deprecation info for server types.
- python-dateutil >= 2.7.5 is now required by the collection. If you already have the hcloud package installed, this dependency should also be installed.
- requests >= 2.20 is now required by the collection. If you already have the hcloud package installed, this dependency should also be installed.

junipernetworks.junos
~~~~~~~~~~~~~~~~~~~~~

- `junos_ospfv2` - Fix the authentication config when password is configured
- `junos_ospfv2` - Rename key ospf to ospfv2 in facts.
- `junos_ospfv2` - add area_ranges attribute which supports list of dict attributes.
- `junos_ospfv2` - add attributes `allow_route_leaking`, `stub_network` and `as-external` to overload dict.
- `junos_ospfv2` - add attributes `no_ignore_out_externals` to spf_options dict.
- `junos_ospfv2` - fix to gather reference_bandwidth and rfc1583compatibility.
- add acl_interfaces key for junos_facts output.

purestorage.flasharray
~~~~~~~~~~~~~~~~~~~~~~

- purefa_info - Added support for autodir policies
- purefa_policy - Added support for autodir policies
- purefa_proxy - Add new protocol parameter, defaults to https

purestorage.flashblade
~~~~~~~~~~~~~~~~~~~~~~

- purefb_fs - Added support for SMB client and share policies
- purefb_fs_replica - Added support to delete filesystem replica links from REST 2.10
- purefb_info - Add drive type in drives subset for //S and //E platforms. Only available from REST 2.9.
- purefb_info - Added support for SMB client and share policies
- purefb_policy - Added support for SMB client and share policies
- purefb_s3acc - Allow human readable quota sizes; eg. 1T, 230K, etc
- purefb_s3user - Add new boolean parameter I(multiple_keys) to limit access keys for a user to a single key.

theforeman.foreman
~~~~~~~~~~~~~~~~~~

- content_view_filter - add deb filter type
- content_view_filter_rule - add spec for deb filter rules
- locations role - New role to manage locations

Breaking Changes / Porting Guide
--------------------------------

hetzner.hcloud
~~~~~~~~~~~~~~

- hcloud-python 1.20.0 is now required for full compatibility

Deprecated Features
-------------------

- The collection ``community.sap`` has been renamed to ``community.sap_libs``. For now both collections are included in Ansible. The content in ``community.sap`` will be replaced with deprecated redirects to the new collection in Ansible 9.0.0, and the collection will be removed from Ansible 10 completely. Please update your FQCNs for ``community.sap``.
- The deprecated servicenow.servicenow collection has been removed from Ansible 7, but accidentally re-added to Ansible 8. It will be removed again from Ansible 9 (https://github.com/ansible-community/community-topics/issues/246).

community.general
~~~~~~~~~~~~~~~~~

- flowdock - module relies entirely on no longer responsive API endpoints, and it will be removed in community.general 9.0.0 (https://github.com/ansible-collections/community.general/pull/6930).
- proxmox - old feature flag ``proxmox_default_behavior`` will be removed in community.general 10.0.0 (https://github.com/ansible-collections/community.general/pull/6836).
- stackdriver - module relies entirely on no longer existent API endpoints, and it will be removed in community.general 9.0.0 (https://github.com/ansible-collections/community.general/pull/6887).
- webfaction_app - module relies entirely on no longer existent API endpoints, and it will be removed in community.general 9.0.0 (https://github.com/ansible-collections/community.general/pull/6909).
- webfaction_db - module relies entirely on no longer existent API endpoints, and it will be removed in community.general 9.0.0 (https://github.com/ansible-collections/community.general/pull/6909).
- webfaction_domain - module relies entirely on no longer existent API endpoints, and it will be removed in community.general 9.0.0 (https://github.com/ansible-collections/community.general/pull/6909).
- webfaction_mailbox - module relies entirely on no longer existent API endpoints, and it will be removed in community.general 9.0.0 (https://github.com/ansible-collections/community.general/pull/6909).
- webfaction_site - module relies entirely on no longer existent API endpoints, and it will be removed in community.general 9.0.0 (https://github.com/ansible-collections/community.general/pull/6909).

junipernetworks.junos
~~~~~~~~~~~~~~~~~~~~~

- `junos_ospfv2` - add deprecate warning for area_range.
- add deprecate warning for junos_acl_interfaces key for junos facts results.

Bugfixes
--------

Ansible-core
~~~~~~~~~~~~

- From issue https://github.com/ansible/ansible/issues/80880, when notifying a handler from another handler, handler notifications must be registered immediately as the flush_handler call is not recursive.
- ansible-galaxy - Fix issue installing collections containing directories with more than 100 characters on python versions before 3.10.6
- paramiko_ssh, psrp, and ssh connection plugins - ensure that all values for options that should be strings are actually converted to strings (https://github.com/ansible/ansible/pull/81029).
- templating - In the template action and lookup, use local jinja2 environment overlay overrides instead of mutating the templars environment

amazon.aws
~~~~~~~~~~

- backup_plan - Use existing ``scrub_none_values`` function from module_utils to remove None values from nested dicts in supplied params. Nested None values were being retained and causing an error when sent through to the boto3 client operation (https://github.com/ansible-collections/amazon.aws/pull/1611).
- backup_vault - fix error when updating tags on a backup vault by using the correct boto3 client methods for tagging and untagging backup resources (https://github.com/ansible-collections/amazon.aws/pull/1610).
- cloudwatchevent_rule - Fixes changed status to report False when no change has been made. The module had incorrectly always reported a change. (https://github.com/ansible-collections/amazon.aws/pull/1589)
- ec2_vpc_nat_gateway - adding a boolean parameter called ``default_create`` to allow users to have the option to choose whether they want to display an error message or create a NAT gateway when an EIP address is not found. The module (ec2_vpc_nat_gateway) had incorrectly failed silently if EIP didn't exist (https://github.com/ansible-collections/amazon.aws/issues/1295).
- ec2_vpc_nat_gateway - fixes to nat gateway so that when the user creates a private NAT gateway, an Elastic IP address should not be allocated. The module had inncorrectly always allocate elastic IP address when creating private nat gateway (https://github.com/ansible-collections/amazon.aws/pull/1632).
- lambda_execute - Fixes to the stack trace output, where it does not contain spaces between each character. The module had incorrectly always outputted extra spaces between each character. (https://github.com/ansible-collections/amazon.aws/pull/1615)
- module_utils.backup - get_selection_details fix empty list returned when multiple backup selections exist (https://github.com/ansible-collections/amazon.aws/pull/1633).

ansible.netcommon
~~~~~~~~~~~~~~~~~

- Ensure that all connection plugin options that should be strings are actually strings (https://github.com/ansible-collections/ansible.netcommon/pull/549).

chocolatey.chocolatey
~~~~~~~~~~~~~~~~~~~~~

- win-chocolatey - unable to install packages if a license is already installed and chocolatey.extension is not installed

cisco.meraki
~~~~~~~~~~~~

- Resolved the issue with link negotation at meraki_ms_switchport
- meraki_devices - Fix endpoints due to breaking change in Meraki API v1.33

community.aws
~~~~~~~~~~~~~

- batch_compute_environment - fixed incorrect handling of Gov Cloud ARNs in ``compute_environment_name`` parameter (https://github.com/ansible-collections/community.aws/issues/1846).
- cloudfront_distribution - The origins  recognises the s3 domains with region part now (https://github.com/ansible-collections/community.aws/issues/1819).
- cloudfront_distribution - no longer crashes when waiting for completion of creation (https://github.com/ansible-collections/community.aws/issues/255).
- cloudfront_distribution - now honours the ``enabled`` setting (https://github.com/ansible-collections/community.aws/issues/1823).
- dynamodb_table - secondary indexes are now created (https://github.com/ansible-collections/community.aws/issues/1825).
- ec2_launch_template - fixed incorrect handling of Gov Cloud ARNs in ``compute_environment_name`` parameter (https://github.com/ansible-collections/community.aws/issues/1846).
- elasticache_info - remove hard coded use of ``aws`` partition (https://github.com/ansible-collections/community.aws/issues/1846).
- iam_role - fixed incorrect rejection of Gov Cloud ARNs in ``boundary`` parameter (https://github.com/ansible-collections/community.aws/issues/1846).
- msk_cluster - remove hard coded use of ``aws`` partition (https://github.com/ansible-collections/community.aws/issues/1846).
- redshift - fixed hard coded use of ``aws`` partition (https://github.com/ansible-collections/community.aws/issues/1846).

community.crypto
~~~~~~~~~~~~~~~~

- Fix PEM detection/identification to also accept random other lines before the line starting with ``-----BEGIN`` (https://github.com/ansible-collections/community.crypto/issues/627, https://github.com/ansible-collections/community.crypto/pull/628).

community.dns
~~~~~~~~~~~~~

- Update Public Suffix List.

community.general
~~~~~~~~~~~~~~~~~

- cobbler inventory plugin - fix calculation of cobbler_ipv4/6_address (https://github.com/ansible-collections/community.general/pull/6925).
- datadog_downtime - presence of ``rrule`` param lead to the Datadog API returning Bad Request due to a missing recurrence type (https://github.com/ansible-collections/community.general/pull/6811).
- ipa_dnszone - fix 'idnsallowsyncptr' key error for reverse zone (https://github.com/ansible-collections/community.general/pull/6906, https://github.com/ansible-collections/community.general/issues/6905).
- keycloak_authentication - fix Keycloak authentication flow (step or sub-flow) indexing during update, if not specified by the user (https://github.com/ansible-collections/community.general/pull/6734).
- locale_gen - now works for locales without the underscore character such as ``C.UTF-8`` (https://github.com/ansible-collections/community.general/pull/6774, https://github.com/ansible-collections/community.general/issues/5142, https://github.com/ansible-collections/community.general/issues/4305).
- machinectl become plugin - mark plugin as ``require_tty`` to automatically disable pipelining, with which this plugin is not compatible (https://github.com/ansible-collections/community.general/issues/6932, https://github.com/ansible-collections/community.general/pull/6935).
- nmcli - fix support for empty list (in compare and scrape) (https://github.com/ansible-collections/community.general/pull/6769).
- openbsd_pkg - the pkg_info(1) behavior has changed in OpenBSD >7.3. The error message ``Can't find`` should not lead to an error case (https://github.com/ansible-collections/community.general/pull/6785).
- pacman - module recognizes the output of ``yay`` running as ``root`` (https://github.com/ansible-collections/community.general/pull/6713).
- proxmox - fix error when a configuration had no ``template`` field (https://github.com/ansible-collections/community.general/pull/6838, https://github.com/ansible-collections/community.general/issues/5372).
- proxmox module utils - add logic to detect whether an old Promoxer complains about the ``token_name`` and ``token_value`` parameters and provide a better error message when that happens (https://github.com/ansible-collections/community.general/pull/6839, https://github.com/ansible-collections/community.general/issues/5371).
- proxmox_disk - fix unable to create ``cdrom`` media due to ``size`` always being appended (https://github.com/ansible-collections/community.general/pull/6770).
- proxmox_kvm - ``absent`` state with ``force`` specified failed to stop the VM due to the ``timeout`` value not being passed to ``stop_vm`` (https://github.com/ansible-collections/community.general/pull/6827).
- proxmox_kvm - ``restarted`` state did not actually restart a VM in some VM configurations. The state now uses the Proxmox reboot endpoint instead of calling the ``stop_vm`` and ``start_vm`` functions (https://github.com/ansible-collections/community.general/pull/6773).
- proxmox_template - require ``requests_toolbelt`` module to fix issue with uploading large templates (https://github.com/ansible-collections/community.general/issues/5579, https://github.com/ansible-collections/community.general/pull/6757).
- redfish_info - fix ``ListUsers`` to not show empty account slots (https://github.com/ansible-collections/community.general/issues/6771, https://github.com/ansible-collections/community.general/pull/6772).
- refish_utils module utils - changing variable names to avoid issues occuring when fetching Volumes data (https://github.com/ansible-collections/community.general/pull/6883).
- snap - assume default track ``latest`` in parameter ``channel`` when not specified (https://github.com/ansible-collections/community.general/pull/6835, https://github.com/ansible-collections/community.general/issues/6821).
- snap - fix the processing of the commands' output, stripping spaces and newlines from it (https://github.com/ansible-collections/community.general/pull/6826, https://github.com/ansible-collections/community.general/issues/6803).

community.sops
~~~~~~~~~~~~~~

- install role - fix ``sops_github_latest_detection=latest-release``, which broke due to sops moving to another GitHub organization (https://github.com/ansible-collections/community.sops/pull/151).

community.vmware
~~~~~~~~~~~~~~~~

- vmware_deploy_ovf - Fix an issue with networks that are available on more than one cluster (https://github.com/ansible-collections/community.vmware/issues/1590).
- vmware_guest_disk - Fix idempotency for `absent` disks (https://github.com/ansible-collections/community.vmware/issues/1765).

community.zabbix
~~~~~~~~~~~~~~~~

- agent role - Added missing become statement to allow run to role as nonroot
- zabbix_host module - fix updating hosts that were discovered via LLD
- zabbix_proxy role - failed at version validation. Fix adds cast of zabbix_proxy_version to float, similarly to the other roles.
- zabbix_proxy role - undefined vars at updating proxy definition. Fix adds null defaults for zabbix_proxy_tlsaccept and zabbix_proxy_tlsconnect.
- zabbix_web role - removed 'ssl on;' nginx configuration, which is no longer supported since nginx version 1.25.1.

google.cloud
~~~~~~~~~~~~

- Use default service account if `service_account_email` is unset.

hetzner.hcloud
~~~~~~~~~~~~~~

- hcloud_image_info Fix facts modules deprecated result key
- hcloud_location_info Fix facts modules deprecation warnings
- hcloud_server - TypeError when trying to use deprecated image with allow_deprecated_image
- hcloud_server_type_info Fix facts modules deprecated result dict
- hcloud_server_type_info Fix facts modules deprecation warnings

purestorage.flasharray
~~~~~~~~~~~~~~~~~~~~~~

- purefa_pgsched - Resolved idempotency issue with snap and replication enabled flags
- purefa_pgsnap - Fixed issue with eradicating deleted pgsnapshot
- purefa_pgsnap - Update the accepted suffixes to include also numbers only. Fixed the logic to retrieve the latest completed snapshot
- purefa_policy - Set user_mapping parameter default to True

purestorage.flashblade
~~~~~~~~~~~~~~~~~~~~~~

- purefb_bucket - Fixed bucket type mode name typo
- purefb_fs - Fixed issue with incorrect promotion state setting

theforeman.foreman
~~~~~~~~~~~~~~~~~~

- convert2rhel role - Sync repos before CV publish (https://bugzilla.redhat.com/show_bug.cgi?id=2216907)

Known Issues
------------

Ansible-core
~~~~~~~~~~~~

- ansible-test - The Fedora 37 remote is known to occasionally hang during boot. It is no longer routinely tested as a result. If possible, use the Fedora 38 remote instead.

community.crypto
~~~~~~~~~~~~~~~~

- Ansible markup will show up in raw form on ansible-doc text output for ansible-core before 2.15. If you have trouble deciphering the documentation markup, please upgrade to ansible-core 2.15 (or newer), or read the HTML documentation on https://docs.ansible.com/ansible/devel/collections/community/crypto/.

community.hrobot
~~~~~~~~~~~~~~~~

- Ansible markup will show up in raw form on ansible-doc text output for ansible-core before 2.15. If you have trouble deciphering the documentation markup, please upgrade to ansible-core 2.15 (or newer), or read the HTML documentation on https://docs.ansible.com/ansible/devel/collections/community/hrobot/.

community.routeros
~~~~~~~~~~~~~~~~~~

- Ansible markup will show up in raw form on ansible-doc text output for ansible-core before 2.15. If you have trouble deciphering the documentation markup, please upgrade to ansible-core 2.15 (or newer), or read the HTML documentation on https://docs.ansible.com/ansible/devel/collections/community/routeros/.

community.sops
~~~~~~~~~~~~~~

- Ansible markup will show up in raw form on ansible-doc text output for ansible-core before 2.15. If you have trouble deciphering the documentation markup, please upgrade to ansible-core 2.15 (or newer), or read the HTML documentation on https://docs.ansible.com/ansible/devel/collections/community/sops/.

New Plugins
-----------

Inventory
~~~~~~~~~

- community.aws.aws_mq - MQ broker inventory source

Lookup
~~~~~~

- community.general.bitwarden_secrets_manager - Retrieve secrets from Bitwarden Secrets Manager

New Modules
-----------

amazon.aws
~~~~~~~~~~

- amazon.aws.iam_instance_profile - manage IAM instance profiles
- amazon.aws.iam_instance_profile_info - gather information on IAM instance profiles

community.general
~~~~~~~~~~~~~~~~~

- community.general.consul_policy - Manipulate Consul policies
- community.general.keycloak_authz_permission - Allows administration of Keycloak client authorization permissions via Keycloak API
- community.general.keycloak_authz_permission_info - Query Keycloak client authorization permissions information
- community.general.proxmox_vm_info - Retrieve information about one or more Proxmox VE virtual machines

community.vmware
~~~~~~~~~~~~~~~~

- community.vmware.vmware_vasa - Manage VMware Virtual Volumes storage provider
- community.vmware.vmware_vasa_info - Gather information about vSphere VASA providers.

community.zabbix
~~~~~~~~~~~~~~~~

- community.zabbix.zabbix_regexp - Create/update/delete Zabbix regular expression
- community.zabbix.zabbix_settings - Update Zabbix global settings.
- community.zabbix.zabbix_token - Create/Update/Generate/Delete Zabbix token.

dellemc.powerflex
~~~~~~~~~~~~~~~~~

- dellemc.powerflex.snapshot_policy - Manage snapshot policies on Dell PowerFlex

dellemc.unity
~~~~~~~~~~~~~

- dellemc.unity.replication_session - Manage replication session on the Unity storage system

Unchanged Collections
---------------------

- ansible.posix (still version 1.5.4)
- ansible.utils (still version 2.10.3)
- ansible.windows (still version 1.14.0)
- arista.eos (still version 6.0.1)
- azure.azcollection (still version 1.16.0)
- check_point.mgmt (still version 5.1.1)
- cisco.aci (still version 2.6.0)
- cisco.asa (still version 4.0.1)
- cisco.intersight (still version 1.0.27)
- cisco.ios (still version 4.6.1)
- cisco.iosxr (still version 5.0.3)
- cisco.ise (still version 2.5.12)
- cisco.mso (still version 2.4.0)
- cisco.nso (still version 1.0.3)
- cisco.nxos (still version 4.4.0)
- cloud.common (still version 2.1.3)
- cloudscale_ch.cloud (still version 2.3.1)
- community.azure (still version 2.0.0)
- community.ciscosmb (still version 1.0.6)
- community.digitalocean (still version 1.23.0)
- community.docker (still version 3.4.8)
- community.fortios (still version 1.0.0)
- community.google (still version 1.0.0)
- community.grafana (still version 1.5.4)
- community.hashi_vault (still version 5.0.0)
- community.libvirt (still version 1.2.0)
- community.mysql (still version 3.7.2)
- community.network (still version 5.0.0)
- community.okd (still version 2.3.0)
- community.postgresql (still version 2.4.2)
- community.proxysql (still version 1.5.1)
- community.rabbitmq (still version 1.2.3)
- community.sap (still version 1.0.0)
- community.sap_libs (still version 1.4.1)
- community.skydive (still version 1.0.0)
- community.windows (still version 1.13.0)
- containers.podman (still version 1.10.2)
- cyberark.conjur (still version 1.2.0)
- cyberark.pas (still version 1.0.19)
- dellemc.enterprise_sonic (still version 2.2.0)
- dellemc.openmanage (still version 7.6.1)
- f5networks.f5_modules (still version 1.25.0)
- fortinet.fortimanager (still version 2.2.0)
- fortinet.fortios (still version 2.3.0)
- frr.frr (still version 2.0.2)
- gluster.gluster (still version 1.0.2)
- hpe.nimble (still version 1.1.4)
- ibm.qradar (still version 2.1.0)
- ibm.spectrum_virtualize (still version 1.12.0)
- infinidat.infinibox (still version 1.3.12)
- infoblox.nios_modules (still version 1.5.0)
- inspur.ispim (still version 1.3.0)
- inspur.sm (still version 2.3.0)
- kubernetes.core (still version 2.4.0)
- lowlydba.sqlserver (still version 2.0.0)
- microsoft.ad (still version 1.2.0)
- netapp.aws (still version 21.7.0)
- netapp.azure (still version 21.10.0)
- netapp.cloudmanager (still version 21.22.0)
- netapp.elementsw (still version 21.7.0)
- netapp.ontap (still version 22.7.0)
- netapp.storagegrid (still version 21.11.1)
- netapp.um_info (still version 21.8.0)
- netapp_eseries.santricity (still version 1.4.0)
- netbox.netbox (still version 3.13.0)
- ngine_io.cloudstack (still version 2.3.0)
- ngine_io.exoscale (still version 1.0.0)
- ngine_io.vultr (still version 1.1.3)
- openstack.cloud (still version 2.1.0)
- openvswitch.openvswitch (still version 2.1.1)
- ovirt.ovirt (still version 3.1.2)
- purestorage.fusion (still version 1.5.0)
- sensu.sensu_go (still version 1.13.2)
- servicenow.servicenow (still version 1.0.6)
- splunk.es (still version 2.1.0)
- t_systems_mms.icinga_director (still version 1.33.1)
- vmware.vmware_rest (still version 2.3.1)
- vultr.cloud (still version 1.8.0)
- vyos.vyos (still version 4.1.0)
- wti.remote (still version 1.0.5)

v8.1.0
======

.. contents::
  :local:
  :depth: 2

Release Summary
---------------

Release Date: 2023-06-22

`Porting Guide <https://docs.ansible.com/ansible/devel/porting_guides.html>`_

Ansible-core
------------

Ansible 8.1.0 contains ansible-core version 2.15.1.
This is a newer version than version 2.15.0 contained in the previous Ansible release.

The changes are reported in the combined changelog below.

Changed Collections
-------------------

If not mentioned explicitly, the changes are reported in the combined changelog below.

+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| Collection                    | Ansible 8.0.0 | Ansible 8.1.0 | Notes                                                                                                                        |
+===============================+===============+===============+==============================================================================================================================+
| amazon.aws                    | 6.0.1         | 6.1.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| awx.awx                       | 22.2.0        | 22.3.0        | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| azure.azcollection            | 1.15.0        | 1.16.0        | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| check_point.mgmt              | 5.0.0         | 5.1.1         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.asa                     | 4.0.0         | 4.0.1         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.ios                     | 4.5.0         | 4.6.1         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.iosxr                   | 5.0.2         | 5.0.3         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.nxos                    | 4.3.0         | 4.4.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cloudscale_ch.cloud           | 2.2.4         | 2.3.1         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.ciscosmb            | 1.0.5         | 1.0.6         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.crypto              | 2.13.1        | 2.14.0        |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.dns                 | 2.5.4         | 2.5.6         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.docker              | 3.4.6         | 3.4.8         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.general             | 7.0.1         | 7.1.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.mongodb             | 1.5.2         | 1.6.0         | There are no changes recorded in the changelog.                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.mysql               | 3.7.1         | 3.7.2         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.postgresql          | 2.4.1         | 2.4.2         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.routeros            | 2.8.0         | 2.8.2         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.sops                | 1.6.1         | 1.6.2         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.vmware              | 3.6.0         | 3.7.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.zabbix              | 2.0.0         | 2.0.1         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| containers.podman             | 1.10.1        | 1.10.2        |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| dellemc.enterprise_sonic      | 2.0.0         | 2.2.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| dellemc.openmanage            | 7.5.0         | 7.6.1         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| f5networks.f5_modules         | 1.24.0        | 1.25.0        |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| fortinet.fortimanager         | 2.1.7         | 2.2.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| fortinet.fortios              | 2.2.3         | 2.3.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| microsoft.ad                  | 1.1.0         | 1.2.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| netapp.ontap                  | 22.6.0        | 22.7.0        |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| purestorage.flasharray        | 1.18.0        | 1.19.1        |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| purestorage.fusion            | 1.4.2         | 1.5.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| t_systems_mms.icinga_director | 1.32.2        | 1.33.1        |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| theforeman.foreman            | 3.10.0        | 3.11.0        |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| vultr.cloud                   | 1.7.1         | 1.8.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| vyos.vyos                     | 4.0.2         | 4.1.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| wti.remote                    | 1.0.4         | 1.0.5         | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+

Major Changes
-------------

cloudscale_ch.cloud
~~~~~~~~~~~~~~~~~~~

- Bump minimum required Ansible version to 2.13.0

fortinet.fortimanager
~~~~~~~~~~~~~~~~~~~~~

- Support all FortiManager versions in 6.2, 6.4, 7.0, 7.2 and 7.4. 139 new modules.
- Support token based authentication.

fortinet.fortios
~~~~~~~~~~~~~~~~

- Improve the `no_log` feature in some modules;
- Improve the documentation and example for `seq_num` in `fortios_router_static`;
- Improve the documentation for `member_path` in all the modules;
- Support new FOS versions.

Minor Changes
-------------

Ansible-core
~~~~~~~~~~~~

- ansible-test - Allow float values for the ``--timeout`` option to the ``env`` command. This simplifies testing.
- ansible-test - Refactored ``env`` command logic and timeout handling.
- ansible-test - Use ``datetime.datetime.now`` with ``tz`` specified instead of ``datetime.datetime.utcnow``.

amazon.aws
~~~~~~~~~~

- ec2_snapshot - Add support for modifying createVolumePermission (https://github.com/ansible-collections/amazon.aws/pull/1464).
- ec2_snapshot_info - Add createVolumePermission to output result (https://github.com/ansible-collections/amazon.aws/pull/1464).

check_point.mgmt
~~~~~~~~~~~~~~~~

- cp_mgmt_vpn_community_star - new fields added.
- show command modules  - no longer return result of changed=True.

cisco.ios
~~~~~~~~~

- ios_interfaces - Add template attribute to provide support for cisco ios templates.
- ios_service - Create module to manage service configuration on IOS switches

cisco.nxos
~~~~~~~~~~

- nxos_user - Add support for hashed passwords. (https://github.com/ansible-collections/cisco.nxos/issues/370).

community.ciscosmb
~~~~~~~~~~~~~~~~~~

- added Ansible playbook examples ``cismosmb_inventory_template.yml``, ``cismosmb_gather_facts.yml``, ``cismosmb_commands.yml``
- no longer testing for ansible 2.9 and for Python 2.6 / 2.7
- removed unused portion of code in cliconf/ciscosmb.yml
- test Ansible 2.14

community.crypto
~~~~~~~~~~~~~~~~

- acme_certificate - allow to use no challenge by providing ``no challenge`` for the ``challenge`` option. This is needed for ACME servers where validation is done without challenges (https://github.com/ansible-collections/community.crypto/issues/613, https://github.com/ansible-collections/community.crypto/pull/615).
- acme_certificate - validate and wait for challenges in parallel instead handling them one after another (https://github.com/ansible-collections/community.crypto/pull/617).
- x509_certificate_info - added support for certificates in DER format when using ``path`` parameter (https://github.com/ansible-collections/community.crypto/issues/603).

community.general
~~~~~~~~~~~~~~~~~

- The collection will start using semantic markup (https://github.com/ansible-collections/community.general/pull/6539).
- VarDict module utils - add method ``VarDict.as_dict()`` to convert to a plain ``dict`` object (https://github.com/ansible-collections/community.general/pull/6602).
- cobbler inventory plugin - add ``inventory_hostname`` option to allow using the system name for the inventory hostname (https://github.com/ansible-collections/community.general/pull/6502).
- cobbler inventory plugin - add ``want_ip_addresses`` option to collect all interface DNS name to IP address mapping (https://github.com/ansible-collections/community.general/pull/6711).
- cobbler inventory plugin - add primary IP addess to ``cobbler_ipv4_address`` and IPv6 address to ``cobbler_ipv6_address`` host variable (https://github.com/ansible-collections/community.general/pull/6711).
- cobbler inventory plugin - add warning for systems with empty profiles (https://github.com/ansible-collections/community.general/pull/6502).
- copr - respawn module to use the system python interpreter when the ``dnf`` python module is not available in ``ansible_python_interpreter`` (https://github.com/ansible-collections/community.general/pull/6522).
- datadog_monitor - adds ``notification_preset_name``, ``renotify_occurrences`` and ``renotify_statuses`` parameters (https://github.com/ansible-collections/community.general/issues/6521,https://github.com/ansible-collections/community.general/issues/5823).
- filesystem - add ``uuid`` parameter for UUID change feature (https://github.com/ansible-collections/community.general/pull/6680).
- keycloak_client_rolemapping - adds support for subgroups with additional parameter ``parents`` (https://github.com/ansible-collections/community.general/pull/6687).
- keycloak_role - add composite roles support for realm and client roles (https://github.com/ansible-collections/community.general/pull/6469).
- ldap_* - add new arguments ``client_cert`` and ``client_key`` to the LDAP modules in order to allow certificate authentication (https://github.com/ansible-collections/community.general/pull/6668).
- ldap_search - add a new ``page_size`` option to enable paged searches (https://github.com/ansible-collections/community.general/pull/6648).
- lvg - add ``active`` and ``inactive`` values to the ``state`` option for active state management feature (https://github.com/ansible-collections/community.general/pull/6682).
- lvg - add ``reset_vg_uuid``, ``reset_pv_uuid`` options for UUID reset feature (https://github.com/ansible-collections/community.general/pull/6682).
- mas - disable sign-in check for macOS 12+ as ``mas account`` is non-functional (https://github.com/ansible-collections/community.general/pull/6520).
- onepassword lookup plugin - add service account support (https://github.com/ansible-collections/community.general/issues/6635, https://github.com/ansible-collections/community.general/pull/6660).
- onepassword_raw lookup plugin - add service account support (https://github.com/ansible-collections/community.general/issues/6635, https://github.com/ansible-collections/community.general/pull/6660).
- opentelemetry callback plugin - add span attributes in the span event (https://github.com/ansible-collections/community.general/pull/6531).
- opkg - remove default value ``""`` for parameter ``force`` as it causes the same behaviour of not having that parameter (https://github.com/ansible-collections/community.general/pull/6513).
- proxmox - support ``timezone`` parameter at container creation (https://github.com/ansible-collections/community.general/pull/6510).
- proxmox inventory plugin - add composite variables support for Proxmox nodes (https://github.com/ansible-collections/community.general/issues/6640).
- proxmox_kvm - added support for ``tpmstate0`` parameter to configure TPM (Trusted Platform Module) disk. TPM is required for Windows 11 installations (https://github.com/ansible-collections/community.general/pull/6533).
- proxmox_kvm - re-use ``timeout`` module param to forcefully shutdown a virtual machine when ``state`` is ``stopped`` (https://github.com/ansible-collections/community.general/issues/6257).
- proxmox_snap - add ``retention`` parameter to delete old snapshots (https://github.com/ansible-collections/community.general/pull/6576).
- redfish_command - add ``MultipartHTTPPushUpdate`` command (https://github.com/ansible-collections/community.general/issues/6471, https://github.com/ansible-collections/community.general/pull/6612).
- redhat_subscription - the internal ``RegistrationBase`` class was folded
  into the other internal ``Rhsm`` class, as the separation had no purpose
  anymore
  (https://github.com/ansible-collections/community.general/pull/6658).
- rhsm_release - improve/harden the way ``subscription-manager`` is run;
  no behaviour change is expected
  (https://github.com/ansible-collections/community.general/pull/6669).
- snap - module is now aware of channel when deciding whether to install or refresh the snap (https://github.com/ansible-collections/community.general/pull/6435, https://github.com/ansible-collections/community.general/issues/1606).
- sorcery - minor refactor (https://github.com/ansible-collections/community.general/pull/6525).
- tss lookup plugin - allow to fetch secret IDs which are in a folder based on folder ID. Previously, we could not fetch secrets based on folder ID but now use ``fetch_secret_ids_from_folder`` option to indicate to fetch secret IDs based on folder ID (https://github.com/ansible-collections/community.general/issues/6223).

community.vmware
~~~~~~~~~~~~~~~~

- vmware_cluster_drs_recommendations - Add the Module to apply the drs recommendations (https://github.com/ansible-collections/community.vmware/pull/1736)
- vmware_guest_serial_port - add support for proxyURI parameter to enable use of a virtual serial port concentrator (https://github.com/ansible-collections/community.vmware/issues/1742)

dellemc.enterprise_sonic
~~~~~~~~~~~~~~~~~~~~~~~~

- galaxy_yml - Enable installation of Ansible Netcomon versions after 5.0.0 and update the enterprise_sonic release version (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/270).
- module_utils - Change the location for importing remove_empties from the obsolete Netcommon location to the offically required Ansible library location to fix sanity errors (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/172).
- sonic_aaa - Add replaced and overridden states support for AAA resource module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/237).
- sonic_aaa - Add unit tests for AAA resource module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/198).
- sonic_aaa - Revert breaking changes for AAA nodule (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/269).
- sonic_api - Add unit tests for api resource module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/218).
- sonic_bfd, sonic_copp - Update replaced methods (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/254).
- sonic_bgp - Add rt_delay attribute to module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/244).
- sonic_bgp - Add support for replaced and overridden states (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/240).
- sonic_bgp - Add unit tests for BGP resource module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/182).
- sonic_bgp_af - Add several attributes to support configuration of route distinguisher and route target (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/141).
- sonic_bgp_af - Add support for replaced and overridden states (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/246).
- sonic_bgp_af - Add unit tests for BGP AF resource module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/183).
- sonic_bgp_af - Modify BGP AF resource module unit tests to adjust for changes in the resource module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/191).
- sonic_bgp_as_paths - Add unit tests for BGP AS paths resource module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/184).
- sonic_bgp_communities - Add unit tests for BGP communities resource module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/185).
- sonic_bgp_ext_communities - Add unit tests for BGP ext communities resource module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/186).
- sonic_bgp_neighbors - Add unit tests for BGP neighbors resource module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/187).
- sonic_bgp_neighbors - Enhance unit tests for BGP Neighbors resource module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/245).
- sonic_bgp_neighbors_af - Add unit tests for BGP neighbors AF resource module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/188).
- sonic_command - Add unit tests for command resource module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/219).
- sonic_config - Add unit tests for config resource module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/220).
- sonic_dhcp_relay - Add a common unit tests module and unit tests for dhcp relay module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/148).
- sonic_dhcp_relay - Add support for replaced and overridden states (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/249).
- sonic_facts - Add unit tests for facts resource module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/222).
- sonic_interfaces - Add speed, auto-negotiate, advertised-speed and FEC to interface resource module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/128).
- sonic_interfaces - Add unit tests for interfaces resource module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/197).
- sonic_ip_neighbor - Add unit tests for IP neighbor resource module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/225).
- sonic_ip_neighbor - Change the replaced function in ip_neighbor resource module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/253).
- sonic_l2_interfaces - Add support for parsing configuration containing the OC Yang vlan range syntax (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/124).
- sonic_l2_interfaces - Add support for replaced and overridden states (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/221).
- sonic_l2_interfaces - Add support for specifying vlan trunk ranges in Ansible playbooks (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/149).
- sonic_l2_interfaces - Add unit tests for l2_interfaces resource module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/200).
- sonic_l3_interfaces - Add unit tests for l3_interfaces resource module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/202).
- sonic_lag_interface - Add replaced and overridden states support for LAG interface resource module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/196).
- sonic_lag_interfaces - Add unit tests for lag_interfaces resource module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/203).
- sonic_logging - Add replaced and overridden states support for logging resource module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/150).
- sonic_logging - Add unit tests for logging resource module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/226).
- sonic_logging - Change logging get facts for source_interface naming (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/258).
- sonic_mclag - Add delay_restore, gateway_mac, and peer_gateway attributes to module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/145).
- sonic_ntp - Add prefer attribute to NTP resource module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/118).
- sonic_ntp - Add replaced and overridden states support for NTP resource module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/151).
- sonic_ntp - Add unit tests for NTP resource module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/207).
- sonic_ntp - Change NTP get facts to get default parameters (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/106).
- sonic_ntp - Change NTP key values in NTP regression test script (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/107).
- sonic_ntp - Change NTP module name (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/113).
- sonic_ntp - Change NTP module names in NTP regression test script (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/114).
- sonic_ntp - Change NTP resource module to make minpoll and maxpoll be configured together (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/129).
- sonic_port_breakout - Add unit tests for port breakout resource module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/229).
- sonic_port_group - Add replaced and overridden states support for port group resource module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/227).
- sonic_port_group - Add unit tests for port group resource module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/228).
- sonic_prefix_lists - Add support for replaced and overridden states (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/255).
- sonic_prefix_lists - Add unit tests for prefix lists resource module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/209).
- sonic_radius_server - Add replaced and overridden states support for RADIUS server resource module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/239).
- sonic_radius_server - Add unit tests for RADIUS server resource module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/210).
- sonic_static_routes - Add support for replaced and overridden states (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/236).
- sonic_static_routes - Add unit tests for static routes resource module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/212).
- sonic_system - Add replaced and overridden states support for system resource module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/159).
- sonic_system - Add unit tests for system resource module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/223).
- sonic_tacacs_server - Add replaced and overridden states support for TACACS server resource module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/235).
- sonic_tacacs_server - Add unit tests for TACACS server resource module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/208).
- sonic_users - Add replaced and overridden states support for users resource module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/242).
- sonic_users - Add unit tests for users resource module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/213).
- sonic_vlans - Add replaced and overridden states support for VLAN resource module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/217).
- sonic_vlans - Add unit tests for Vlans resource module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/214).
- sonic_vrfs - Add replaced and overridden states support for VRF resource module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/156).
- sonic_vrfs - Add unit tests for VRFS resource module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/216).
- sonic_vxlans - Add support for replaced and overridden states (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/247).
- sonic_vxlans - Add unit tests for VxLans resource module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/215).

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- Updated the idrac_gather_facts role to use jinja template filters.

f5networks.f5_modules
~~~~~~~~~~~~~~~~~~~~~

- bigip_command - Added note to give appropriate timeout value for long running commands

fortinet.fortimanager
~~~~~~~~~~~~~~~~~~~~~

- Corrected the behavior of module fmgr_pkg_firewall_consolidated_policy_sectionvalue and fmgr_pkg_firewall_securitypolicy_sectionvalue.
- Improve documentation.

microsoft.ad
~~~~~~~~~~~~

- microsoft.ad.debug_ldap_client - Add ``dpapi_ng`` to list of packages checked
- microsoft.ad.ldap - Add support for decrypting LAPS encrypted password
- microsoft.ad.ldap - Allow setting LDAP connection and authentication options through environment variables - https://github.com/ansible-collections/microsoft.ad/issues/34

netapp.ontap
~~~~~~~~~~~~

- na_ontap_name_mappings - added choices ``s3_win`` and ``s3_unix`` to ``direction``, requires ONTAP 9.12.1 or later.
- na_ontap_s3_buckets - new option ``nas_path`` added, requires ONTAP 9.12.1 or later.

purestorage.fusion
~~~~~~~~~~~~~~~~~~

- FUSION_API_HOST && FUSION_HOST - changed logic, now this variables require host name without path
- Fusion authentication - add 'access_token' module's parameter and 'FUSION_ACCESS_TOKEN' environment variable, as an alternative way of the authentication.
- fusion - added private key password, which is used to decrypt private key files
- fusion_info - `array` is None if missing in `volume`
- fusion_info - `hardware_types` is None if missing in `storage_service`
- fusion_info - `network_interface_groups` is None if missing in `iscsi_interfaces` in `storage_endpoint`
- fusion_info - introduce 'availability_zones' subset option
- fusion_info - introduce 'host_access_policies' subset option
- fusion_info - introduce 'network_interfaces' subset option
- fusion_info - introduce 'regions' subset option
- fusion_info - rename 'appliances' in default dict to 'arrays' for consistency
- fusion_info - rename 'hosts' dict to 'host_access_policies' for consistency
- fusion_info - rename 'interfaces' dict to 'network_interfaces' for consistency
- fusion_info - rename 'placements_groups' in default dict to 'placement_groups' for consistency
- fusion_info - rename 'zones' dict to 'availability_zones' for consistency
- fusion_info - rename hardware to hardware_types in response for consistency
- fusion_info - rename storageclass to storage_classes in response for consistency
- fusion_pp - duration parsing improved. Supports combination of time units (E.g 5H5M)
- fusion_ra - added `api_client_key` argument, which can be used instead of `user` and `principal` argument
- fusion_ra - added `principal` argument, which is an ID of either API client or User and can be used instead of `user` argument
- fusion_se - add support for CBS Storage Endpoint

t_systems_mms.icinga_director
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Add Icinga Deploy handler and module (https://github.com/T-Systems-MMS/ansible-collection-icinga-director/pull/205)

theforeman.foreman
~~~~~~~~~~~~~~~~~~

- content_view_promote role - also accept all parameters of the `content_view_version` module (https://github.com/theforeman/foreman-ansible-modules/issues/1591)
- content_view_version - include information about the published version in the return value of the module
- job-invocation - add ``recurrence purpose`` and ``description_format`` parameters
- organizations role - accept ``parameters`` and ``ignore_types`` like the module does

vultr.cloud
~~~~~~~~~~~

- instance - Implemented a new ``state`` equal ``reinstalled`` to reinstall an existing instance (https://github.com/vultr/ansible-collection-vultr/pull/66).
- inventory - Bare metal support has been implemented (https://github.com/vultr/ansible-collection-vultr/pull/63).

vyos.vyos
~~~~~~~~~

- vyos-l3_interface_support - Add support for Tunnel, Bridge and Dummy interfaces. (https://github.com/ansible-collections/vyos.vyos/issues/265)

Breaking Changes / Porting Guide
--------------------------------

- Please note that the breaking change announced in the dellemc.enterprise_sonic changelog below is from dellemc.enterprise_sonic 2.1.0 and was reverted in dellemc.enterprise_sonic 2.2.0, so it is not contained in Ansible 8. For technical reasons, this entry is still shown here.

dellemc.enterprise_sonic
~~~~~~~~~~~~~~~~~~~~~~~~

- sonic_aaa - Add default_auth attribute to the argspec to replace the deleted group and local attributes. This change allows for ordered login authentication. (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/195).

Deprecated Features
-------------------

- The gluster.gluster collection is considered unmaintained and will be removed from Ansible 10 if no one starts maintaining it again before Ansible 10. See `the removal process for details on how this works <https://github.com/ansible-collections/overview/blob/main/removal_from_ansible.rst#cancelling-removal-of-an-unmaintained-collection>`__ (https://github.com/ansible-community/community-topics/issues/225).

amazon.aws
~~~~~~~~~~

- s3_object - support for passing object keys with a leading ``/`` has been deprecated and will be removed in a release after 2025-12-01 (https://github.com/ansible-collections/amazon.aws/pull/1549).

community.ciscosmb
~~~~~~~~~~~~~~~~~~

- support for Python 2.6 nad 2.7
- support for ansible 2.9

community.general
~~~~~~~~~~~~~~~~~

- CmdRunner module utils - deprecate ``cmd_runner_fmt.as_default_type()`` formatter (https://github.com/ansible-collections/community.general/pull/6601).
- MH VarsMixin module utils - deprecates ``VarsMixin`` and supporting classes in favor of plain ``vardict`` module util (https://github.com/ansible-collections/community.general/pull/6649).
- cpanm - value ``compatibility`` is deprecated as default for parameter ``mode`` (https://github.com/ansible-collections/community.general/pull/6512).
- redhat module utils - the ``module_utils.redhat`` module is deprecated, as
  effectively unused: the ``Rhsm``, ``RhsmPool``, and ``RhsmPools`` classes
  will be removed in community.general 9.0.0; the ``RegistrationBase`` class
  will be removed in community.general 10.0.0 together with the
  ``rhn_register`` module, as it is the only user of this class; this means
  that the whole ``module_utils.redhat`` module will be dropped in
  community.general 10.0.0, so importing it without even using anything of it
  will fail
  (https://github.com/ansible-collections/community.general/pull/6663).
- redhat_subscription - the ``autosubscribe`` alias for the ``auto_attach`` option has been
  deprecated for many years, although only in the documentation. Officially mark this alias
  as deprecated, and it will be removed in community.general 9.0.0
  (https://github.com/ansible-collections/community.general/pull/6646).
- redhat_subscription - the ``pool`` option is deprecated in favour of the
  more precise and flexible ``pool_ids`` option
  (https://github.com/ansible-collections/community.general/pull/6650).
- rhsm_repository - ``state=present`` has not been working as expected for many years,
  and it seems it was not noticed so far; also, "presence" is not really a valid concept
  for subscription repositories, which can only be enabled or disabled. Hence, mark the
  ``present`` and ``absent`` values of the ``state`` option as deprecated, slating them
  for removal in community.general 10.0.0
  (https://github.com/ansible-collections/community.general/pull/6673).

microsoft.ad
~~~~~~~~~~~~

- Deprecating support for Server 2012 and Server 2012 R2. These OS versions are reaching End of Life status from Microsoft and support for using them in Ansible are nearing its end.

purestorage.fusion
~~~~~~~~~~~~~~~~~~

- fusion_api_client - 'app_id' and 'key_file' parameters are deprecated in favor of 'issuer_id' and 'private_key_file' parameters and will be removed in the version 2.0.0, FUSION_APP_ID and FUSION_HOST env variables are deprecated in favor of FUSION_ISSUER_ID and FUSION_HOST and will be removed in the version 2.0.0
- fusion_array - 'app_id' and 'key_file' parameters are deprecated in favor of 'issuer_id' and 'private_key_file' parameters and will be removed in the version 2.0.0, FUSION_APP_ID and FUSION_HOST env variables are deprecated in favor of FUSION_ISSUER_ID and FUSION_HOST and will be removed in the version 2.0.0
- fusion_az - 'app_id' and 'key_file' parameters are deprecated in favor of 'issuer_id' and 'private_key_file' parameters and will be removed in the version 2.0.0, FUSION_APP_ID and FUSION_HOST env variables are deprecated in favor of FUSION_ISSUER_ID and FUSION_HOST and will be removed in the version 2.0.0
- fusion_hap - 'app_id' and 'key_file' parameters are deprecated in favor of 'issuer_id' and 'private_key_file' parameters and will be removed in the version 2.0.0, FUSION_APP_ID and FUSION_HOST env variables are deprecated in favor of FUSION_ISSUER_ID and FUSION_HOST and will be removed in the version 2.0.0
- fusion_hap - parameters `nqn`, `wwns`, `host_password`, `host_user`, `target_password`and `target_user` were deprecated
- fusion_hw - FUSION_APP_ID and FUSION_HOST env variables are deprecated in favor of FUSION_ISSUER_ID and FUSION_HOST and will be removed in the version 2.0.0
- fusion_info - 'app_id' and 'key_file' parameters are deprecated in favor of 'issuer_id' and 'private_key_file' parameters and will be removed in the version 2.0.0, FUSION_APP_ID and FUSION_HOST env variables are deprecated in favor of FUSION_ISSUER_ID and FUSION_HOST and will be removed in the version 2.0.0
- fusion_info - 'hosts' subset is deprecated in favor of 'host_access_policies' and will be removed in the version 2.0.0
- fusion_info - 'interfaces' subset is deprecated in favor of 'network_interfaces' and will be removed in the version 2.0.0
- fusion_info - 'zones' subset is deprecated in favor of 'availability_zones' and will be removed in the version 2.0.0
- fusion_ni - 'app_id' and 'key_file' parameters are deprecated in favor of 'issuer_id' and 'private_key_file' parameters and will be removed in the version 2.0.0, FUSION_APP_ID and FUSION_HOST env variables are deprecated in favor of FUSION_ISSUER_ID and FUSION_HOST and will be removed in the version 2.0.0
- fusion_nig - 'app_id' and 'key_file' parameters are deprecated in favor of 'issuer_id' and 'private_key_file' parameters and will be removed in the version 2.0.0, FUSION_APP_ID and FUSION_HOST env variables are deprecated in favor of FUSION_ISSUER_ID and FUSION_HOST and will be removed in the version 2.0.0
- fusion_pg - 'app_id' and 'key_file' parameters are deprecated in favor of 'issuer_id' and 'private_key_file' parameters and will be removed in the version 2.0.0, FUSION_APP_ID and FUSION_HOST env variables are deprecated in favor of FUSION_ISSUER_ID and FUSION_HOST and will be removed in the version 2.0.0
- fusion_pp - 'app_id' and 'key_file' parameters are deprecated in favor of 'issuer_id' and 'private_key_file' parameters and will be removed in the version 2.0.0, FUSION_APP_ID and FUSION_HOST env variables are deprecated in favor of FUSION_ISSUER_ID and FUSION_HOST and will be removed in the version 2.0.0
- fusion_ra - 'app_id' and 'key_file' parameters are deprecated in favor of 'issuer_id' and 'private_key_file' parameters and will be removed in the version 2.0.0, FUSION_APP_ID and FUSION_HOST env variables are deprecated in favor of FUSION_ISSUER_ID and FUSION_HOST and will be removed in the version 2.0.0
- fusion_region - 'app_id' and 'key_file' parameters are deprecated in favor of 'issuer_id' and 'private_key_file' parameters and will be removed in the version 2.0.0, FUSION_APP_ID and FUSION_HOST env variables are deprecated in favor of FUSION_ISSUER_ID and FUSION_HOST and will be removed in the version 2.0.0
- fusion_sc - 'app_id' and 'key_file' parameters are deprecated in favor of 'issuer_id' and 'private_key_file' parameters and will be removed in the version 2.0.0, FUSION_APP_ID and FUSION_HOST env variables are deprecated in favor of FUSION_ISSUER_ID and FUSION_HOST and will be removed in the version 2.0.0
- fusion_se - 'app_id' and 'key_file' parameters are deprecated in favor of 'issuer_id' and 'private_key_file' parameters and will be removed in the version 2.0.0, FUSION_APP_ID and FUSION_HOST env variables are deprecated in favor of FUSION_ISSUER_ID and FUSION_HOST and will be removed in the version 2.0.0
- fusion_se - `endpoint_type` parameter is now deprecated and will be removed in version 2.0.0
- fusion_ss - 'app_id' and 'key_file' parameters are deprecated in favor of 'issuer_id' and 'private_key_file' parameters and will be removed in the version 2.0.0, FUSION_APP_ID and FUSION_HOST env variables are deprecated in favor of FUSION_ISSUER_ID and FUSION_HOST and will be removed in the version 2.0.0
- fusion_tenant - 'app_id' and 'key_file' parameters are deprecated in favor of 'issuer_id' and 'private_key_file' parameters and will be removed in the version 2.0.0, FUSION_APP_ID and FUSION_HOST env variables are deprecated in favor of FUSION_ISSUER_ID and FUSION_HOST and will be removed in the version 2.0.0
- fusion_tn - FUSION_APP_ID and FUSION_HOST env variables are deprecated in favor of FUSION_ISSUER_ID and FUSION_HOST and will be removed in the version 2.0.0
- fusion_ts - 'app_id' and 'key_file' parameters are deprecated in favor of 'issuer_id' and 'private_key_file' parameters and will be removed in the version 2.0.0, FUSION_APP_ID and FUSION_HOST env variables are deprecated in favor of FUSION_ISSUER_ID and FUSION_HOST and will be removed in the version 2.0.0
- fusion_volume - 'app_id' and 'key_file' parameters are deprecated in favor of 'issuer_id' and 'private_key_file' parameters and will be removed in the version 2.0.0, FUSION_APP_ID and FUSION_HOST env variables are deprecated in favor of FUSION_ISSUER_ID and FUSION_HOST and will be removed in the version 2.0.0

Removed Features (previously deprecated)
----------------------------------------

community.ciscosmb
~~~~~~~~~~~~~~~~~~

- remove testing for Python 2.6 nad 2.7
- remove testing for ansible 2.9

Bugfixes
--------

Ansible-core
~~~~~~~~~~~~

- Properly disable ``jinja2_native`` in the template module when jinja2 override is used in the template (https://github.com/ansible/ansible/issues/80605)
- ansible-galaxy - Fix variable type error when installing subdir collections (https://github.com/ansible/ansible/issues/80943)
- ansible-test - Fix a traceback that occurs when attempting to test Ansible source using a different ansible-test. A clear error message is now given when this scenario occurs.
- ansible-test - Fix handling of timeouts exceeding one day.
- ansible-test - Fix various cases where the test timeout could expire without terminating the tests.
- ansible-test local change detection - use ``git merge-base <branch> HEAD`` instead of ``git merge-base --fork-point <branch>`` (https://github.com/ansible/ansible/pull/79734).
- deb822_repository - use http-agent for receiving content (https://github.com/ansible/ansible/issues/80809).
- dnf5 - Update dnf5 module to handle API change for setting the download directory (https://github.com/ansible/ansible/issues/80887)
- man page build - Remove the dependency on the ``docs`` directory for building man pages.
- pep517 build backend - Copy symlinks when copying the source tree. This avoids tracebacks in various scenarios, such as when a venv is present in the source tree.
- uri - fix search for JSON type to include complex strings containing '+'

amazon.aws
~~~~~~~~~~

- autoscaling_group - fix ValidationError when describing an autoscaling group that has more than 20 target groups attached to it by breaking the request into chunks (https://github.com/ansible-collections/amazon.aws/pull/1593).
- autoscaling_group_info - fix ValidationError when describing an autoscaling group that has more than 20 target groups attached to it by breaking the request into chunks (https://github.com/ansible-collections/amazon.aws/pull/1593).
- ec2_instance - fix check_mode issue when adding network interfaces (https://github.com/ansible-collections/amazon.aws/issues/1403).
- ec2_metadata_facts - Handle decompression when EC2 instance user-data is gzip compressed. The fetch_url method from ansible.module_utils.urls does not decompress the user-data unless the header explicitly contains ``Content-Encoding: gzip`` (https://github.com/ansible-collections/amazon.aws/pull/1575).
- elb_application_lb - fix missing attributes on creation of ALB. The ``create_or_update_alb()`` was including ALB-specific attributes when updating an existing ALB but not when creating a new ALB (https://github.com/ansible-collections/amazon.aws/issues/1510).
- module_utils.acm - fixes list_certificates returning only RSA_2048 certificates (https://github.com/ansible-collections/amazon.aws/issues/1567).
- rds_instance - add support for CACertificateIdentifier to create/update rds instance (https://github.com/ansible-collections/amazon.aws/pull/1459).

check_point.mgmt
~~~~~~~~~~~~~~~~

- cp_mgmt_access_rules - split vpn param that can accept either a String or list of objects to two
- module_utils/checkpoint.py - fixed compile issue (Syntax Error) on python 2.7

cisco.ios
~~~~~~~~~

- ios_facts - fix calculation of memory from bytes to megabytes; grab correct output element for free memory (https://github.com/ansible-collections/cisco.ios/issues/763)
- ios_l3_interfaces - account for secondary/primary when comparing ipv4 addresses. (https://github.com/ansible-collections/cisco.ios/issues/826)
- ios_lag_interfaces - Fix empty facts to be a list.
- ios_ospf_interface - Fix configuration rendering for ipv4 and ipv6 configurations.
- ios_ospf_interface - Fix replaced and overridden state, action to negate superfluous configuration.
- ios_snmp_server - Add default versions to version 3 users.
- ospfv2 - Fixed rendering of capability command with vrf_lite.
- ospfv3 - Fixed rendering of capability command with vrf_lite.
- snmp_server - update module to get snmp_server user configuration.

cisco.iosxr
~~~~~~~~~~~

- Fixing Bundle-Ether/-POS recognition for resource modules. (https://github.com/ansible-collections/cisco.iosxr/issues/369)
- acls - Fix issue in ``replaced`` state of not replacing ace entries with remark action. (https://github.com/ansible-collections/cisco.iosxr/issues/332)
- l3_interfaces - Fix issue in ``gather`` state of not gathering management interface. (https://github.com/ansible-collections/cisco.iosxr/issues/381)

cisco.nxos
~~~~~~~~~~

- l3_interfaces - Append tag when updating IP address with state replaced (https://github.com/ansible-collections/cisco.nxos/issues/678).
- ntp_global - Fix incorrect handling of prefer option (https://github.com/ansible-collections/cisco.nxos/issues/670).
- nxos_banner - Add support for a custom multiline delimiter
- nxos_facts - Fix missing SVI facts (https://github.com/ansible-collections/cisco.nxos/issues/440).
- terminal - attempt privilege escalation only when prompt does not end with #

cloudscale_ch.cloud
~~~~~~~~~~~~~~~~~~~

- Add missing modules to the "cloudscale_ch.cloud.cloudscale" action group.
- Remove outdated Ansible version requirement from the README.

community.dns
~~~~~~~~~~~~~

- Update Public Suffix List.

community.docker
~~~~~~~~~~~~~~~~

- docker_swarm_info - if ``service=true`` is used, do not crash when a service without an endpoint spec is encountered (https://github.com/ansible-collections/community.docker/issues/636, https://github.com/ansible-collections/community.docker/pull/637).

community.general
~~~~~~~~~~~~~~~~~

- MH DependencyMixin module utils - deprecation notice was popping up for modules not using dependencies (https://github.com/ansible-collections/community.general/pull/6644, https://github.com/ansible-collections/community.general/issues/6639).
- csv module utils - detects and remove unicode BOM markers from incoming CSV content (https://github.com/ansible-collections/community.general/pull/6662).
- gitlab_group - the module passed parameters to the API call even when not set. The module is now filtering out ``None`` values to remediate this (https://github.com/ansible-collections/community.general/pull/6712).
- icinga2_host - fix a key error when updating an existing host (https://github.com/ansible-collections/community.general/pull/6748).
- ini_file - add the ``follow`` paramter to follow the symlinks instead of replacing them (https://github.com/ansible-collections/community.general/pull/6546).
- ini_file - fix a bug where the inactive options were not used when possible (https://github.com/ansible-collections/community.general/pull/6575).
- keycloak module utils - fix ``is_struct_included`` handling of lists of lists/dictionaries (https://github.com/ansible-collections/community.general/pull/6688).
- keycloak module utils - the function ``get_user_by_username`` now return the user representation or ``None`` as stated in the documentation (https://github.com/ansible-collections/community.general/pull/6758).
- proxmox_kvm - allow creation of VM with existing name but new vmid (https://github.com/ansible-collections/community.general/issues/6155, https://github.com/ansible-collections/community.general/pull/6709).
- rhsm_repository - when using the ``purge`` option, the ``repositories``
  dictionary element in the returned JSON is now properly updated according
  to the pruning operation
  (https://github.com/ansible-collections/community.general/pull/6676).
- tss lookup plugin - fix multiple issues when using ``fetch_attachments=true`` (https://github.com/ansible-collections/community.general/pull/6720).

community.mysql
~~~~~~~~~~~~~~~

- mysql module utils - use the connection arguments ``db`` instead of ``database`` and ``passwd`` instead of ``password`` when running with MySQLdb < 2.0.0 (https://github.com/ansible-collections/community.mysql/pull/553).

community.postgresql
~~~~~~~~~~~~~~~~~~~~

- postgresql_db - when the task is completed successfully, close the database connection (https://github.com/ansible-collections/community.postgresql/issues/465).
- postgresql_info - when the task is completed successfully, close the database connection (https://github.com/ansible-collections/community.postgresql/issues/465).
- postgresql_ping - when the task is completed successfully, close the database connection (https://github.com/ansible-collections/community.postgresql/issues/465).
- postgresql_privs - when the task is completed successfully, close the database connection (https://github.com/ansible-collections/community.postgresql/issues/465).

community.routeros
~~~~~~~~~~~~~~~~~~

- api_modify, api_info - add missing parameter ``tls`` for the ``tool e-mail`` path (https://github.com/ansible-collections/community.routeros/issues/179, https://github.com/ansible-collections/community.routeros/pull/180).
- facts - do not crash in CLI output preprocessing in unexpected situations during line unwrapping (https://github.com/ansible-collections/community.routeros/issues/170, https://github.com/ansible-collections/community.routeros/pull/177).

community.sops
~~~~~~~~~~~~~~

- install role - make sure that the ``pkg_mgr`` fact is definitely available when installing on ``localhost``. This can improve error messages in some cases (https://github.com/ansible-collections/community.sops/issues/145, https://github.com/ansible-collections/community.sops/pull/146).

community.vmware
~~~~~~~~~~~~~~~~

- Add missing modules to runtime.yml (https://github.com/ansible-collections/community.vmware/pull/1764).
- vmware_vm_info - Add missing show_folder parameter (https://github.com/ansible-collections/community.vmware/issues/1709).

community.zabbix
~~~~~~~~~~~~~~~~

- Proxy and Agent Roles - Added `zabbix_api_use_ssl` variable to allow secure API connections
- Web Role - Added defaults and documentation for `zabbix_apache_custom_includes`
- agent - Handled undefined variable error for Windows default versions
- all roles - Added option to selectively disable a repo on Redhat installs

containers.podman
~~~~~~~~~~~~~~~~~

- Add hooks-dir parameter for containers
- Add idempotency for restart-policy for containers
- Add missing options to podman network
- Add more explanation about cmd_args command usage
- Add stdout to podman build and push actions
- Added support for "userns" parameter to "play" module
- CI - fix pip installation of the collection
- CI - fix podman play job for 4.4.x versions
- Change yes/no to true/false in the modules
- Convert str to json format before evaluating length.
- Fix CI for newest Ansible branch 2.16
- Fix idempotency for pods with uidmap and gidmap
- Fix idempotency lowercase for devices
- Fix network tests for Podman v4
- Fix podman logout tests for v4
- Fix pylint issues for CI ansible-test
- Fix undesirable splitting of IPv6 host addresses
- Improved documentation of `podman_generate_systemd` module
- Prepare CI for Podman v3 backward compatibility
- Support SHA256 tag for podman images
- Update podman_image to specify CPU arch when pulling image
- added podman_prune module
- become plugin podman_unshare become_user default
- fix for buildah improper remote target
- for pod kube recreate
- pod - Support passing multiple networks with params
- podman-login - fix FIPS md5 issue and registry requirement
- podman-pod - Fix idempotency for pods in 4.4.x versions
- podman_systemd - Ignore header when comparing systemd files content

dellemc.enterprise_sonic
~~~~~~~~~~~~~~~~~~~~~~~~

- Fix regression test bugs in multiple modules (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/180).
- Fix sanity check errors in the collection caused by Ansible library changes (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/160).
- install - Update the required ansible.netcommon version (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/176).
- sonic_bgp_af - Fix issue with vnis and advertise modification for a single BGP AF (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/201).
- sonic_bgp_as_paths - Fix issues with merged and deleted states (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/250).
- sonic_interfaces - Fix command timeout issue (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/261).
- sonic_l3_interfaces - Fix IP address deletion issue (GitHub issue#170) (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/231).
- sonic_lag_interfaces - Fix port name issue (GitHub issue#153) (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/119).
- sonic_neighbors - Fix handling of default attributes (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/233).
- sonic_ntp - Fix the issue (GitHub issue#205) with NTP clear all without config given (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/224).
- sonic_vlan_mapping - Remove platform checks (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/262).
- sonic_vrfs - Add tasks as a workaround to mgmt VRF bug (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/146).
- sonic_vrfs - Fix spacing issue in CLI test case (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/257).
- sonic_vrfs - Fix the issue (GitHub issue#194) with VRF when deleting interface(https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/230).
- sonic_vxlans - Remove required_together restriction for evpn_nvo and source_ip attributes (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/130).
- workflows - Fix dependency installation issue in the code coverage workflow (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/199).

f5networks.f5_modules
~~~~~~~~~~~~~~~~~~~~~

- bigip_provision_async - created module to address scenarios where infinite loops or timeouts happen

fortinet.fortimanager
~~~~~~~~~~~~~~~~~~~~~

- Corrected description of parameters in documentation.
- Fixed Many sanity test warnings and errors.
- Fixed a bug where users might not be able to login.
- Fixed version_added in the document. The value of this parameter is the version each module first supported in the FortiManager Ansible Collection.

fortinet.fortios
~~~~~~~~~~~~~~~~

- Fix the error of pure number password.

microsoft.ad
~~~~~~~~~~~~

- group - Fix idempotency check when ``scope: domainlocal`` is set - https://github.com/ansible-collections/microsoft.ad/issues/31
- microsoft.ad.group - ensure the ``scope`` and ``category`` values are checked as case insensitive to avoid changes when not needed - https://github.com/ansible-collections/microsoft.ad/issues/31

netapp.ontap
~~~~~~~~~~~~

- na_ontap_login_messages - fix ``banner`` and ``motd_message`` not idempotent when trailing '\n' is present.
- na_ontap_login_messages - fix idempotent issue on ``show_cluster_motd`` option when try to set banner or motd_message for the first time in REST.

purestorage.flasharray
~~~~~~~~~~~~~~~~~~~~~~

- purefa_info - Fixed missing arguments for google_offload and pods

purestorage.fusion
~~~~~~~~~~~~~~~~~~

- fusion_info - fix runtime errors caused when listing `interfaces`, `arrays` and `snapshots` dicts
- fusion_pg - freshly created placement group is now moved to correct array
- fusion_pp - 'local_rpo' changed to accept same input as 'local_retention'
- fusion_pp - updated retention description
- fusion_ra - 'name' deprecated and aliased to 'role'

t_systems_mms.icinga_director
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- add icinga_deploy_* to action_group and test it (https://github.com/T-Systems-MMS/ansible-collection-icinga-director/pull/214)

theforeman.foreman
~~~~~~~~~~~~~~~~~~

- compute_profile, host - properly support nested VMware clusters (https://bugzilla.redhat.com/show_bug.cgi?id=2211394)
- content_credential - don't require ``content_type`` and ``content`` parameters when removing credentials (https://github.com/theforeman/foreman-ansible-modules/issues/1588)
- content_credentials role - don't require ``content_type`` and ``content`` parameters when removing credentials
- content_view_filter - don't fail when creating a modulemd filter (https://github.com/theforeman/foreman-ansible-modules/issues/1608, https://bugzilla.redhat.com/show_bug.cgi?id=2208557)
- repositories role - don't log repository information when creating products (https://bugzilla.redhat.com/show_bug.cgi?id=2183357)

vyos.vyos
~~~~~~~~~

- vyos-l3_interface_facts - fixed error when using no-default-link-local option. (https://github.com/ansible-collections/vyos.vyos/issues/295)

Known Issues
------------

community.dns
~~~~~~~~~~~~~

- Ansible markup will show up in raw form on ansible-doc text output for ansible-core before 2.15. If you have trouble deciphering the documentation markup, please upgrade to ansible-core 2.15 (or newer), or read the HTML documentation on https://docs.ansible.com/ansible/devel/collections/community/dns/.

community.docker
~~~~~~~~~~~~~~~~

- Ansible markup will show up in raw form on ansible-doc text output for ansible-core before 2.15. If you have trouble deciphering the documentation markup, please upgrade to ansible-core 2.15 (or newer), or read the HTML documentation on https://docs.ansible.com/ansible/devel/collections/community/docker/.

community.general
~~~~~~~~~~~~~~~~~

- Ansible markup will show up in raw form on ansible-doc text output for ansible-core before 2.15. If you have trouble deciphering the documentation markup, please upgrade to ansible-core 2.15 (or newer), or read the HTML documentation on https://docs.ansible.com/ansible/devel/collections/community/general/ (https://github.com/ansible-collections/community.general/pull/6539).

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- idrac_redfish_storage_contoller - Issue(256164) - If incorrect value is provided for one of the attributes in the provided attribute list for controller configuration, then this module does not exit with error.
- ome_device_network_services - Issue(212681) - The module does not provide a proper error message if unsupported values are provided for the following parameters- port_number, community_name, max_sessions, max_auth_retries, and idle_timeout.
- ome_device_power_settings - Issue(212679) - The module displays the following message if the value provided for the parameter ``power_cap`` is not within the supported range of 0 to 32767, ``Unable to complete the request because PowerCap does not exist or is not applicable for the resource URI.``
- ome_smart_fabric_uplink - Issue(186024) - Despite the module supported by OpenManage Enterprise Modular, it does not allow the creation of multiple uplinks of the same name. If an uplink is created using the same name as an existing uplink, the existing uplink is modified.

New Modules
-----------

cisco.ios
~~~~~~~~~

- cisco.ios.ios_service - Resource module to configure service.

cloudscale_ch.cloud
~~~~~~~~~~~~~~~~~~~

- cloudscale_ch.cloud.load_balancer - Manages load balancers on the cloudscale.ch IaaS service
- cloudscale_ch.cloud.load_balancer_health_monitor - Manages load balancers on the cloudscale.ch IaaS service
- cloudscale_ch.cloud.load_balancer_listener - Manages load balancer listeners on the cloudscale.ch IaaS service
- cloudscale_ch.cloud.load_balancer_pool - Manages load balancer pools on the cloudscale.ch IaaS service
- cloudscale_ch.cloud.load_balancer_pool_member - Manages load balancer pool members on the cloudscale.ch IaaS service

community.general
~~~~~~~~~~~~~~~~~

- community.general.gitlab_instance_variable - Creates, updates, or deletes GitLab instance variables
- community.general.gitlab_merge_request - Create, update, or delete GitLab merge requests
- community.general.keycloak_authentication_required_actions - Allows administration of Keycloak authentication required actions
- community.general.keycloak_user - Create and configure a user in Keycloak
- community.general.lvg_rename - Renames LVM volume groups
- community.general.proxmox_pool - Pool management for Proxmox VE cluster
- community.general.proxmox_pool_member - Add or delete members from Proxmox VE cluster pools

community.vmware
~~~~~~~~~~~~~~~~

- community.vmware.vmware_cluster_drs_recommendations - Apply DRS Recommendations
- community.vmware.vmware_vsan_release_catalog - Uploads the vSAN Release Catalog

dellemc.enterprise_sonic
~~~~~~~~~~~~~~~~~~~~~~~~

- dellemc.enterprise_sonic.sonic_acl_interfaces - Manage access control list (ACL) to interface binding on SONiC
- dellemc.enterprise_sonic.sonic_bfd - Manage BFD configuration on SONiC
- dellemc.enterprise_sonic.sonic_copp - Manage CoPP configuration on SONiC
- dellemc.enterprise_sonic.sonic_dhcp_relay - Manage DHCP and DHCPv6 relay configurations on SONiC
- dellemc.enterprise_sonic.sonic_ip_neighbor - Manage IP neighbor global configuration on SONiC
- dellemc.enterprise_sonic.sonic_l2_acls - Manage Layer 2 access control lists (ACL) configurations on SONiC
- dellemc.enterprise_sonic.sonic_l3_acls - Manage Layer 3 access control lists (ACL) configurations on SONiC
- dellemc.enterprise_sonic.sonic_lldp_global - Manage Global LLDP configurations on SONiC
- dellemc.enterprise_sonic.sonic_logging - Manage logging configuration on SONiC
- dellemc.enterprise_sonic.sonic_mac - Manage MAC configuration on SONiC
- dellemc.enterprise_sonic.sonic_port_group - Manages port group configuration on SONiC
- dellemc.enterprise_sonic.sonic_route_maps - route map configuration handling for SONiC
- dellemc.enterprise_sonic.sonic_vlan_mapping - Configure vlan mappings on SONiC

f5networks.f5_modules
~~~~~~~~~~~~~~~~~~~~~

- f5networks.f5_modules.bigip_provision_async - Manage BIG-IP module provisioning

fortinet.fortimanager
~~~~~~~~~~~~~~~~~~~~~

- fortinet.fortimanager.fmgr_application_casi_profile - Cloud Access Security Inspection.
- fortinet.fortimanager.fmgr_application_casi_profile_entries - Application entries.
- fortinet.fortimanager.fmgr_application_internetservice - Show Internet service application.
- fortinet.fortimanager.fmgr_application_internetservice_entry - Entries in the Internet service database.
- fortinet.fortimanager.fmgr_application_internetservicecustom - Configure custom Internet service applications.
- fortinet.fortimanager.fmgr_application_internetservicecustom_disableentry - Disable entries in the Internet service database.
- fortinet.fortimanager.fmgr_application_internetservicecustom_disableentry_iprange - IP ranges in the disable entry.
- fortinet.fortimanager.fmgr_application_internetservicecustom_entry - Entries added to the Internet service database and custom database.
- fortinet.fortimanager.fmgr_application_internetservicecustom_entry_portrange - Port ranges in the custom entry.
- fortinet.fortimanager.fmgr_cloud_orchestaws - no description
- fortinet.fortimanager.fmgr_cloud_orchestawsconnector - no description
- fortinet.fortimanager.fmgr_cloud_orchestawstemplate_autoscaleexistingvpc - no description
- fortinet.fortimanager.fmgr_cloud_orchestawstemplate_autoscalenewvpc - no description
- fortinet.fortimanager.fmgr_cloud_orchestawstemplate_autoscaletgwnewvpc - no description
- fortinet.fortimanager.fmgr_cloud_orchestration - no description
- fortinet.fortimanager.fmgr_devprof_log_syslogd_filter_excludelist - no description
- fortinet.fortimanager.fmgr_devprof_log_syslogd_filter_excludelist_fields - no description
- fortinet.fortimanager.fmgr_devprof_log_syslogd_filter_freestyle - Free style filters.
- fortinet.fortimanager.fmgr_devprof_log_syslogd_setting_customfieldname - Custom field name for CEF format logging.
- fortinet.fortimanager.fmgr_dnsfilter_profile_urlfilter - URL filter settings.
- fortinet.fortimanager.fmgr_dnsfilter_urlfilter - Configure URL filter list.
- fortinet.fortimanager.fmgr_dnsfilter_urlfilter_entries - DNS URL filter.
- fortinet.fortimanager.fmgr_emailfilter_profile_yahoomail - Yahoo! Mail.
- fortinet.fortimanager.fmgr_extensioncontroller_dataplan - FortiExtender dataplan configuration.
- fortinet.fortimanager.fmgr_extensioncontroller_extenderprofile - FortiExtender extender profile configuration.
- fortinet.fortimanager.fmgr_extensioncontroller_extenderprofile_cellular - FortiExtender cellular configuration.
- fortinet.fortimanager.fmgr_extensioncontroller_extenderprofile_cellular_controllerreport - FortiExtender controller report configuration.
- fortinet.fortimanager.fmgr_extensioncontroller_extenderprofile_cellular_modem1 - Configuration options for modem 1.
- fortinet.fortimanager.fmgr_extensioncontroller_extenderprofile_cellular_modem1_autoswitch - FortiExtender auto switch configuration.
- fortinet.fortimanager.fmgr_extensioncontroller_extenderprofile_cellular_modem2 - Configuration options for modem 2.
- fortinet.fortimanager.fmgr_extensioncontroller_extenderprofile_cellular_modem2_autoswitch - FortiExtender auto switch configuration.
- fortinet.fortimanager.fmgr_extensioncontroller_extenderprofile_cellular_smsnotification - FortiExtender cellular SMS notification configuration.
- fortinet.fortimanager.fmgr_extensioncontroller_extenderprofile_cellular_smsnotification_alert - SMS alert list.
- fortinet.fortimanager.fmgr_extensioncontroller_extenderprofile_cellular_smsnotification_receiver - SMS notification receiver list.
- fortinet.fortimanager.fmgr_extensioncontroller_extenderprofile_lanextension - FortiExtender lan extension configuration.
- fortinet.fortimanager.fmgr_extensioncontroller_extenderprofile_lanextension_backhaul - LAN extension backhaul tunnel configuration.
- fortinet.fortimanager.fmgr_firewall_accessproxy6 - Configure IPv6 access proxy.
- fortinet.fortimanager.fmgr_firewall_accessproxy6_apigateway - Set IPv4 API Gateway.
- fortinet.fortimanager.fmgr_firewall_accessproxy6_apigateway6 - Set IPv6 API Gateway.
- fortinet.fortimanager.fmgr_firewall_accessproxy6_apigateway6_realservers - Select the real servers that this Access Proxy will distribute traffic to.
- fortinet.fortimanager.fmgr_firewall_accessproxy6_apigateway6_sslciphersuites - SSL/TLS cipher suites to offer to a server, ordered by priority.
- fortinet.fortimanager.fmgr_firewall_accessproxy6_apigateway_realservers - Select the real servers that this Access Proxy will distribute traffic to.
- fortinet.fortimanager.fmgr_firewall_accessproxy6_apigateway_sslciphersuites - SSL/TLS cipher suites to offer to a server, ordered by priority.
- fortinet.fortimanager.fmgr_firewall_address6_profilelist - List of NSX service profiles that use this address.
- fortinet.fortimanager.fmgr_firewall_address_profilelist - List of NSX service profiles that use this address.
- fortinet.fortimanager.fmgr_firewall_explicitproxyaddress - Explicit web proxy address configuration.
- fortinet.fortimanager.fmgr_firewall_explicitproxyaddress_headergroup - HTTP header group.
- fortinet.fortimanager.fmgr_firewall_explicitproxyaddrgrp - Explicit web proxy address group configuration.
- fortinet.fortimanager.fmgr_firewall_gtp_messagefilter - Message filter.
- fortinet.fortimanager.fmgr_firewall_ippoolgrp - Configure IPv4 pool groups.
- fortinet.fortimanager.fmgr_firewall_networkservicedynamic - Configure Dynamic Network Services.
- fortinet.fortimanager.fmgr_fmg_fabric_authorization_template - no description
- fortinet.fortimanager.fmgr_fmg_fabric_authorization_template_platforms - no description
- fortinet.fortimanager.fmgr_fmupdate_fwmsetting_upgradetimeout - Configure the timeout value of image upgrade process.
- fortinet.fortimanager.fmgr_fsp_vlan_dynamicmapping_interface_vrrp - VRRP configuration.
- fortinet.fortimanager.fmgr_fsp_vlan_dynamicmapping_interface_vrrp_proxyarp - VRRP Proxy ARP configuration.
- fortinet.fortimanager.fmgr_fsp_vlan_interface_vrrp_proxyarp - VRRP Proxy ARP configuration.
- fortinet.fortimanager.fmgr_ips_baseline_sensor - Configure IPS sensor.
- fortinet.fortimanager.fmgr_ips_baseline_sensor_entries - IPS sensor filter.
- fortinet.fortimanager.fmgr_ips_baseline_sensor_entries_exemptip - Traffic from selected source or destination IP addresses is exempt from this signature.
- fortinet.fortimanager.fmgr_ips_baseline_sensor_filter - no description
- fortinet.fortimanager.fmgr_ips_baseline_sensor_override - no description
- fortinet.fortimanager.fmgr_ips_baseline_sensor_override_exemptip - no description
- fortinet.fortimanager.fmgr_log_npuserver - Configure all the log servers and create the server groups.
- fortinet.fortimanager.fmgr_log_npuserver_servergroup - create server group.
- fortinet.fortimanager.fmgr_log_npuserver_serverinfo - configure server info.
- fortinet.fortimanager.fmgr_pkg_firewall_explicitproxypolicy - Configure Explicit proxy policies.
- fortinet.fortimanager.fmgr_pkg_firewall_explicitproxypolicy_identitybasedpolicy - Identity-based policy.
- fortinet.fortimanager.fmgr_pkg_firewall_explicitproxypolicy_sectionvalue - Configure Explicit proxy policies.
- fortinet.fortimanager.fmgr_pkg_firewall_hyperscalepolicy - Configure IPv4/IPv6 policies.
- fortinet.fortimanager.fmgr_pkg_firewall_hyperscalepolicy46 - Configure IPv4 to IPv6 policies.
- fortinet.fortimanager.fmgr_pkg_firewall_hyperscalepolicy6 - Configure IPv6 policies.
- fortinet.fortimanager.fmgr_pkg_firewall_hyperscalepolicy64 - Configure IPv6 to IPv4 policies.
- fortinet.fortimanager.fmgr_pkg_user_nacpolicy - Configure NAC policy matching pattern to identify matching NAC devices.
- fortinet.fortimanager.fmgr_pm_config_pblock_firewall_consolidated_policy - Configure consolidated IPv4/IPv6 policies.
- fortinet.fortimanager.fmgr_pm_config_pblock_firewall_consolidated_policy_sectionvalue - Configure consolidated IPv4/IPv6 policies.
- fortinet.fortimanager.fmgr_pm_config_pblock_firewall_policy6 - Configure IPv6 policies.
- fortinet.fortimanager.fmgr_pm_config_pblock_firewall_policy6_sectionvalue - Configure IPv6 policies.
- fortinet.fortimanager.fmgr_pm_devprof_scopemember - no description
- fortinet.fortimanager.fmgr_pm_pkg_scopemember - Policy package or folder.
- fortinet.fortimanager.fmgr_pm_wanprof_scopemember - no description
- fortinet.fortimanager.fmgr_securityconsole_template_cli_preview - no description
- fortinet.fortimanager.fmgr_switchcontroller_acl_group - Configure ACL groups to be applied on managed FortiSwitch ports.
- fortinet.fortimanager.fmgr_switchcontroller_acl_ingress - Configure ingress ACL policies to be applied on managed FortiSwitch ports.
- fortinet.fortimanager.fmgr_switchcontroller_acl_ingress_action - ACL actions.
- fortinet.fortimanager.fmgr_switchcontroller_acl_ingress_classifier - ACL classifiers.
- fortinet.fortimanager.fmgr_switchcontroller_dynamicportpolicy - Configure Dynamic port policy to be applied on the managed FortiSwitch ports through DPP device.
- fortinet.fortimanager.fmgr_switchcontroller_dynamicportpolicy_policy - Port policies with matching criteria and actions.
- fortinet.fortimanager.fmgr_switchcontroller_fortilinksettings - Configure integrated FortiLink settings for FortiSwitch.
- fortinet.fortimanager.fmgr_switchcontroller_fortilinksettings_nacports - NAC specific configuration.
- fortinet.fortimanager.fmgr_switchcontroller_macpolicy - Configure MAC policy to be applied on the managed FortiSwitch devices through NAC device.
- fortinet.fortimanager.fmgr_switchcontroller_managedswitch_dhcpsnoopingstaticclient - Configure FortiSwitch DHCP snooping static clients.
- fortinet.fortimanager.fmgr_switchcontroller_managedswitch_ports_dhcpsnoopoption82override - Configure DHCP snooping option 82 override.
- fortinet.fortimanager.fmgr_switchcontroller_managedswitch_staticmac - Configuration method to edit FortiSwitch Static and Sticky MAC.
- fortinet.fortimanager.fmgr_switchcontroller_managedswitch_stpinstance - Configuration method to edit Spanning Tree Protocol
- fortinet.fortimanager.fmgr_switchcontroller_switchinterfacetag - Configure switch object tags.
- fortinet.fortimanager.fmgr_switchcontroller_trafficpolicy - Configure FortiSwitch traffic policy.
- fortinet.fortimanager.fmgr_switchcontroller_vlanpolicy - Configure VLAN policy to be applied on the managed FortiSwitch ports through dynamic-port-policy.
- fortinet.fortimanager.fmgr_sys_cloud_orchest - no description
- fortinet.fortimanager.fmgr_system_npu_backgroundssescan - Configure driver background scan for SSE.
- fortinet.fortimanager.fmgr_system_npu_dosoptions - NPU DoS configurations.
- fortinet.fortimanager.fmgr_system_npu_dswdtsprofile - Configure NPU DSW DTS profile.
- fortinet.fortimanager.fmgr_system_npu_dswqueuedtsprofile - Configure NPU DSW Queue DTS profile.
- fortinet.fortimanager.fmgr_system_npu_hpe - Host protection engine configuration.
- fortinet.fortimanager.fmgr_system_npu_ipreassembly - IP reassebmly engine configuration.
- fortinet.fortimanager.fmgr_system_npu_npqueues - Configure queue assignment on NP7.
- fortinet.fortimanager.fmgr_system_npu_npqueues_ethernettype - Configure a NP7 QoS Ethernet Type.
- fortinet.fortimanager.fmgr_system_npu_npqueues_ipprotocol - Configure a NP7 QoS IP Protocol.
- fortinet.fortimanager.fmgr_system_npu_npqueues_ipservice - Configure a NP7 QoS IP Service.
- fortinet.fortimanager.fmgr_system_npu_npqueues_profile - Configure a NP7 class profile.
- fortinet.fortimanager.fmgr_system_npu_npqueues_scheduler - Configure a NP7 QoS Scheduler.
- fortinet.fortimanager.fmgr_system_npu_portpathoption - Configure port using NPU or Intel-NIC.
- fortinet.fortimanager.fmgr_system_npu_ssehascan - Configure driver HA scan for SSE.
- fortinet.fortimanager.fmgr_system_npu_swtrhash - Configure switch traditional hashing.
- fortinet.fortimanager.fmgr_system_npu_tcptimeoutprofile - Configure TCP timeout profile.
- fortinet.fortimanager.fmgr_system_npu_udptimeoutprofile - Configure UDP timeout profile.
- fortinet.fortimanager.fmgr_system_objecttag - Configure object tags.
- fortinet.fortimanager.fmgr_system_sdnconnector_compartmentlist - Configure OCI compartment list.
- fortinet.fortimanager.fmgr_system_sdnconnector_ociregionlist - Configure OCI region list.
- fortinet.fortimanager.fmgr_system_socfabric_trustedlist - Pre-authorized security fabric nodes
- fortinet.fortimanager.fmgr_um_image_upgrade - The older API for updating the firmware of specific device.
- fortinet.fortimanager.fmgr_um_image_upgrade_ext - Update the firmware of specific device.
- fortinet.fortimanager.fmgr_user_certificate - Configure certificate users.
- fortinet.fortimanager.fmgr_user_deviceaccesslist - Configure device access control lists.
- fortinet.fortimanager.fmgr_user_deviceaccesslist_devicelist - Device list.
- fortinet.fortimanager.fmgr_user_flexvm - no description
- fortinet.fortimanager.fmgr_user_json - no description
- fortinet.fortimanager.fmgr_user_saml_dynamicmapping - SAML server entry configuration.
- fortinet.fortimanager.fmgr_vpnsslweb_portal_landingpage - Landing page options.
- fortinet.fortimanager.fmgr_vpnsslweb_portal_landingpage_formdata - Form data.
- fortinet.fortimanager.fmgr_vpnsslweb_virtualdesktopapplist - SSL-VPN virtual desktop application list.
- fortinet.fortimanager.fmgr_vpnsslweb_virtualdesktopapplist_apps - Applications.
- fortinet.fortimanager.fmgr_wireless_accesscontrollist - Configure WiFi bridge access control list.
- fortinet.fortimanager.fmgr_wireless_accesscontrollist_layer3ipv4rules - AP ACL layer3 ipv4 rule list.
- fortinet.fortimanager.fmgr_wireless_accesscontrollist_layer3ipv6rules - AP ACL layer3 ipv6 rule list.
- fortinet.fortimanager.fmgr_wireless_address - Configure the client with its MAC address.
- fortinet.fortimanager.fmgr_wireless_addrgrp - Configure the MAC address group.
- fortinet.fortimanager.fmgr_wireless_ssidpolicy - Configure WiFi SSID policies.
- fortinet.fortimanager.fmgr_wireless_syslogprofile - Configure Wireless Termination Points

netapp.ontap
~~~~~~~~~~~~

- netapp.ontap.na_ontap_active_directory_domain_controllers - NetApp ONTAP configure active directory preferred domain controllers

purestorage.flasharray
~~~~~~~~~~~~~~~~~~~~~~

- purestorage.flasharray.purefa_logging - Manage Pure Storage FlashArray Audit and Session logs

t_systems_mms.icinga_director
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- t_systems_mms.icinga_director.icinga_deploy - Trigger deployment in Icinga2
- t_systems_mms.icinga_director.icinga_deploy_info - Get deployment information through the director API

New Roles
---------

- dellemc.openmanage.idrac_attributes - Role to configure iDRAC attributes.
- dellemc.openmanage.idrac_bios - Role to modify BIOS attributes, clear pending BIOS attributes, and reset the BIOS to default settings.
- dellemc.openmanage.idrac_reset - Role to reset and restart iDRAC (iDRAC8 and iDRAC9 only) for Dell PowerEdge servers.
- dellemc.openmanage.idrac_storage_controller - Role to configure the physical disk, virtual disk, and storage controller settings on iDRAC9 based PowerEdge servers.

Unchanged Collections
---------------------

- ansible.netcommon (still version 5.1.1)
- ansible.posix (still version 1.5.4)
- ansible.utils (still version 2.10.3)
- ansible.windows (still version 1.14.0)
- arista.eos (still version 6.0.1)
- chocolatey.chocolatey (still version 1.4.0)
- cisco.aci (still version 2.6.0)
- cisco.dnac (still version 6.7.2)
- cisco.intersight (still version 1.0.27)
- cisco.ise (still version 2.5.12)
- cisco.meraki (still version 2.15.1)
- cisco.mso (still version 2.4.0)
- cisco.nso (still version 1.0.3)
- cisco.ucs (still version 1.8.0)
- cloud.common (still version 2.1.3)
- community.aws (still version 6.0.0)
- community.azure (still version 2.0.0)
- community.digitalocean (still version 1.23.0)
- community.fortios (still version 1.0.0)
- community.google (still version 1.0.0)
- community.grafana (still version 1.5.4)
- community.hashi_vault (still version 5.0.0)
- community.hrobot (still version 1.8.0)
- community.libvirt (still version 1.2.0)
- community.network (still version 5.0.0)
- community.okd (still version 2.3.0)
- community.proxysql (still version 1.5.1)
- community.rabbitmq (still version 1.2.3)
- community.sap (still version 1.0.0)
- community.sap_libs (still version 1.4.1)
- community.skydive (still version 1.0.0)
- community.windows (still version 1.13.0)
- cyberark.conjur (still version 1.2.0)
- cyberark.pas (still version 1.0.19)
- dellemc.powerflex (still version 1.6.0)
- dellemc.unity (still version 1.6.0)
- frr.frr (still version 2.0.2)
- gluster.gluster (still version 1.0.2)
- google.cloud (still version 1.1.3)
- grafana.grafana (still version 2.0.0)
- hetzner.hcloud (still version 1.11.0)
- hpe.nimble (still version 1.1.4)
- ibm.qradar (still version 2.1.0)
- ibm.spectrum_virtualize (still version 1.12.0)
- infinidat.infinibox (still version 1.3.12)
- infoblox.nios_modules (still version 1.5.0)
- inspur.ispim (still version 1.3.0)
- inspur.sm (still version 2.3.0)
- junipernetworks.junos (still version 5.1.0)
- kubernetes.core (still version 2.4.0)
- lowlydba.sqlserver (still version 2.0.0)
- netapp.aws (still version 21.7.0)
- netapp.azure (still version 21.10.0)
- netapp.cloudmanager (still version 21.22.0)
- netapp.elementsw (still version 21.7.0)
- netapp.storagegrid (still version 21.11.1)
- netapp.um_info (still version 21.8.0)
- netapp_eseries.santricity (still version 1.4.0)
- netbox.netbox (still version 3.13.0)
- ngine_io.cloudstack (still version 2.3.0)
- ngine_io.exoscale (still version 1.0.0)
- ngine_io.vultr (still version 1.1.3)
- openstack.cloud (still version 2.1.0)
- openvswitch.openvswitch (still version 2.1.1)
- ovirt.ovirt (still version 3.1.2)
- purestorage.flashblade (still version 1.11.0)
- sensu.sensu_go (still version 1.13.2)
- servicenow.servicenow (still version 1.0.6)
- splunk.es (still version 2.1.0)
- vmware.vmware_rest (still version 2.3.1)

v8.0.0
======

.. contents::
  :local:
  :depth: 2

Release Summary
---------------

Release Date: 2023-05-30 `Porting Guide <https://docs.ansible.com/ansible/devel/porting_guides.html>`_

Removed Collections
-------------------

- dellemc.os10 (previously included version: 1.1.1)
- dellemc.os6 (previously included version: 1.0.7)
- dellemc.os9 (previously included version: 1.0.4)
- mellanox.onyx (previously included version: 1.0.0)

Added Collections
-----------------

- dellemc.powerflex (version 1.6.0)
- dellemc.unity (version 1.6.0)
- grafana.grafana (version 2.0.0)
- microsoft.ad (version 1.1.0)
- servicenow.servicenow (version 1.0.6)

Ansible-core
------------

Ansible 8.0.0 contains ansible-core version 2.15.0.
This is a newer version than version 2.14.0 contained in the previous Ansible release.

The changes are reported in the combined changelog below.

Included Collections
--------------------

If not mentioned explicitly, the changes are reported in the combined changelog below.

+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| Collection                    | Ansible 7.0.0 | Ansible 8.0.0 | Notes                                                                                                                        |
+===============================+===============+===============+==============================================================================================================================+
| amazon.aws                    | 5.1.0         | 6.0.1         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| ansible.netcommon             | 4.1.0         | 5.1.1         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| ansible.posix                 | 1.4.0         | 1.5.4         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| ansible.utils                 | 2.7.0         | 2.10.3        |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| ansible.windows               | 1.12.0        | 1.14.0        |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| arista.eos                    | 6.0.0         | 6.0.1         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| awx.awx                       | 21.8.0        | 22.2.0        | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| azure.azcollection            | 1.14.0        | 1.15.0        | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| check_point.mgmt              | 4.0.0         | 5.0.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| chocolatey.chocolatey         | 1.3.1         | 1.4.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.aci                     | 2.3.0         | 2.6.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.dnac                    | 6.6.0         | 6.7.2         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.intersight              | 1.0.20        | 1.0.27        | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.ios                     | 4.0.0         | 4.5.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.iosxr                   | 4.0.2         | 5.0.2         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.ise                     | 2.5.9         | 2.5.12        |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.meraki                  | 2.11.0        | 2.15.1        |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.mso                     | 2.1.0         | 2.4.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.nxos                    | 4.0.0         | 4.3.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cloud.common                  | 2.1.2         | 2.1.3         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cloudscale_ch.cloud           | 2.2.2         | 2.2.4         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.aws                 | 5.0.0         | 6.0.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.crypto              | 2.8.1         | 2.13.1        |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.digitalocean        | 1.22.0        | 1.23.0        |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.dns                 | 2.4.1         | 2.5.4         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.docker              | 3.2.1         | 3.4.6         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.general             | 6.0.1         | 7.0.1         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.grafana             | 1.5.3         | 1.5.4         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.hashi_vault         | 4.0.0         | 5.0.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.hrobot              | 1.6.0         | 1.8.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.mongodb             | 1.4.2         | 1.5.2         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.mysql               | 3.5.1         | 3.7.1         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.okd                 | 2.2.0         | 2.3.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.postgresql          | 2.3.0         | 2.4.1         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.proxysql            | 1.4.0         | 1.5.1         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.routeros            | 2.3.1         | 2.8.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.sap_libs            | 1.3.0         | 1.4.1         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.sops                | 1.4.1         | 1.6.1         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.vmware              | 3.1.0         | 3.6.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.windows             | 1.11.1        | 1.13.0        |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.zabbix              | 1.8.0         | 2.0.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| containers.podman             | 1.9.4         | 1.10.1        |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cyberark.pas                  | 1.0.14        | 1.0.19        | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| dellemc.openmanage            | 6.3.0         | 7.5.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| dellemc.powerflex             |               | 1.6.0         | The collection was added to Ansible                                                                                          |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| dellemc.unity                 |               | 1.6.0         | The collection was added to Ansible                                                                                          |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| f5networks.f5_modules         | 1.20.0        | 1.24.0        |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| fortinet.fortios              | 2.1.7         | 2.2.3         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| frr.frr                       | 2.0.0         | 2.0.2         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| google.cloud                  | 1.0.2         | 1.1.3         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| grafana.grafana               |               | 2.0.0         | The collection was added to Ansible                                                                                          |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| hetzner.hcloud                | 1.8.2         | 1.11.0        |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| ibm.spectrum_virtualize       | 1.10.0        | 1.12.0        |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| infinidat.infinibox           | 1.3.7         | 1.3.12        | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| infoblox.nios_modules         | 1.4.0         | 1.5.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| inspur.ispim                  | 1.2.0         | 1.3.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| junipernetworks.junos         | 4.0.0         | 5.1.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| kubernetes.core               | 2.3.2         | 2.4.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| lowlydba.sqlserver            | 1.0.4         | 2.0.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| microsoft.ad                  |               | 1.1.0         | The collection was added to Ansible                                                                                          |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| netapp.cloudmanager           | 21.21.0       | 21.22.0       |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| netapp.ontap                  | 22.0.1        | 22.6.0        |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| netapp_eseries.santricity     | 1.3.1         | 1.4.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| netbox.netbox                 | 3.8.1         | 3.13.0        |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| ngine_io.cloudstack           | 2.2.4         | 2.3.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| ngine_io.vultr                | 1.1.2         | 1.1.3         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| openstack.cloud               | 1.10.0        | 2.1.0         | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| openvswitch.openvswitch       | 2.1.0         | 2.1.1         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| ovirt.ovirt                   | 2.3.1         | 3.1.2         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| purestorage.flasharray        | 1.14.0        | 1.18.0        |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| purestorage.flashblade        | 1.10.0        | 1.11.0        |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| purestorage.fusion            | 1.1.1         | 1.4.2         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| sensu.sensu_go                | 1.13.1        | 1.13.2        |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| servicenow.servicenow         |               | 1.0.6         | The collection was added to Ansible                                                                                          |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| t_systems_mms.icinga_director | 1.31.4        | 1.32.2        |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| theforeman.foreman            | 3.7.0         | 3.10.0        |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| vmware.vmware_rest            | 2.2.0         | 2.3.1         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| vultr.cloud                   | 1.3.1         | 1.7.1         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| vyos.vyos                     | 4.0.0         | 4.0.2         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+

Major Changes
-------------

Ansible-core
~~~~~~~~~~~~

- ansible-test - Docker Desktop on WSL2 is now supported (additional configuration required).
- ansible-test - Docker and Podman are now supported on hosts with cgroup v2 unified. Previously only cgroup v1 and cgroup v2 hybrid were supported.
- ansible-test - Podman now works on container hosts without systemd. Previously only some containers worked, while others required rootfull or rootless Podman, but would not work with both. Some containers did not work at all.
- ansible-test - Podman on WSL2 is now supported.
- ansible-test - When additional cgroup setup is required on the container host, this will be automatically detected. Instructions on how to configure the host will be provided in the error message shown.

ansible.windows
~~~~~~~~~~~~~~~

- Set the minimum Ansible version supported by this collection to Ansible 2.12

chocolatey.chocolatey
~~~~~~~~~~~~~~~~~~~~~

- win_chocolatey - Allow users to select the TLS versions used for bootstrapping Chocolatey installation.

cisco.iosxr
~~~~~~~~~~~

- iosxr_l3_interfaces - fix issue in ipv4 address formatting. (https://github.com/ansible-collections/cisco.iosxr/issues/311).

cisco.meraki
~~~~~~~~~~~~

- meraki_mr_l7_firewall - New module
- meraki_webhook_payload_template - New module

community.hrobot
~~~~~~~~~~~~~~~~

- firewall - Hetzner added output rules support to the firewall. This change unfortunately means that using old versions of the firewall module will always set the output rule list to empty, thus disallowing the server to send out packets (https://github.com/ansible-collections/community.hrobot/issues/75, https://github.com/ansible-collections/community.hrobot/pull/76).

community.postgresql
~~~~~~~~~~~~~~~~~~~~

- postgresql_privs - the ``password`` argument is deprecated and will be removed in community.postgresql 4.0.0, use the ``login_password`` argument instead (https://github.com/ansible-collections/community.postgresql/issues/406).

community.vmware
~~~~~~~~~~~~~~~~

- Use true/false (lowercase) for boolean values in documentation and examples (https://github.com/ansible-collections/community.vmware/issues/1660).

community.zabbix
~~~~~~~~~~~~~~~~

- all modules are opting away from zabbix-api and using httpapi ansible.netcommon plugin. We will support zabbix-api for backwards compatibility until next major release. See our README.md for more information about how to migrate
- zabbix_agent and zabbix_proxy roles are opting away from zabbix-api and use httpapi ansible.netcommon plugin. We will support zabbix-api for backwards compatibility until next major release. See our README.md for more information about how to migrate

containers.podman
~~~~~~~~~~~~~~~~~

- New become plugin - podman_unshare
- Podman generate systemd module

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- Rebranded from Dell EMC to Dell.
- Support for IPv6 address for OMSDK dependent iDRAC modules.
- idrac_firmware - This module is enhanced to support proxy.
- idrac_redfish_storage_controller - This module is enhanced to configure controller attributes and online capacity expansion.
- idrac_server_config_profile - This module is enhanced to support proxy settings, import buffer, include in export, and ignore certificate warning.
- idrac_user_info - This module allows to retrieve iDRAC Local user information details.
- ome_domian_user_groups - This module allows to import the LDAP directory groups.
- ome_inventory - This plugin allows to create a inventory from the group on OpenManage Enterprise.
- ome_inventory - This plugin is enhanced to support inventory retrieval of System and Plugin Groups of OpenManage Enterprise.
- ome_profile_info - This module allows to retrieve profiles with attributes on OpenManage Enterprise or OpenManage Enterprise Modular.
- ome_smart_fabric_info - This module retrieves the list of smart fabrics in the inventory of OpenManage Enterprise Modular.
- ome_smart_fabric_uplink_info - This module retrieve details of fabric uplink on OpenManage Enterprise Modular.
- ome_template_network_vlan_info - This module allows to retrieve the network configuration of a template on OpenManage Enterprise or OpenManage Enterprise Modular.

fortinet.fortios
~~~~~~~~~~~~~~~~

- Add annotations of member operation for every module.
- Support FortiOS v7.0.6, v7.0.7, v7.0.8, v7.2.1, v7.2.2.
- Update ``fortios.py`` for higher performance;
- supports temporary session key and pre/post login banner;
- update the examples on how to use member operation in Q&A.

infoblox.nios_modules
~~~~~~~~~~~~~~~~~~~~~

- Added Grid Master Candidate feature `#152 <https://github.com/infobloxopen/infoblox-ansible/pull/152>`_
- Added Member Assignment to network and ranges `#152 <https://github.com/infobloxopen/infoblox-ansible/pull/152>`_
- Added NIOS Range module with Create, Update and Delete features `#152 <https://github.com/infobloxopen/infoblox-ansible/pull/152>`_
- Fixes issue unable to update/delete EAs using Ansible plugin `#180 <https://github.com/infobloxopen/infoblox-ansible/pull/180>`_
- Fixes static and dynamic allocation of IPV4 address of A Record `#182 <https://github.com/infobloxopen/infoblox-ansible/pull/182>`_
- Fixes to Update host name of  NIOS member `#176 <https://github.com/infobloxopen/infoblox-ansible/pull/176>`_
- Updates default WAPI version to 2.9 `#176 <https://github.com/infobloxopen/infoblox-ansible/pull/176>`_

junipernetworks.junos
~~~~~~~~~~~~~~~~~~~~~

- change gathered key from junos_acls to acls

kubernetes.core
~~~~~~~~~~~~~~~

- refactor K8sAnsibleMixin into module_utils/k8s/ (https://github.com/ansible-collections/kubernetes.core/pull/481).

purestorage.fusion
~~~~~~~~~~~~~~~~~~

- Patching of resource properties was brought to parity with underlying Python SDK
- fusion_volume - fixed and reorganized, arguments changed

Minor Changes
-------------

Ansible-core
~~~~~~~~~~~~

- Add support for custom salt for vault encoding to make it deterministic (https://github.com/ansible/ansible/issues/35480).
- Added the conditional that was False if ``when`` caused a task to skip under ``false_condition``.
- Allow force deletion of a group even when it is the primary group of a user. (https://github.com/ansible/ansible/issues/77849)
- Ansible.ModuleUtils.AddType - Add support for compiling ``unsafe`` code with the ``//AllowUnsafe`` directive
- Cache field attributes list on the playbook classes
- Cleaned up unused imports in core.
- Get user input for ``pause`` and ``paramiko_ssh`` from the strategy rather than access ``sys.stdin`` in the WorkerProcess.
- Introduce ``Delegatable`` and ``Notifiable`` mixin classes for playbook objects
- Make using blocks as handlers a parser error (https://github.com/ansible/ansible/issues/79968)
- Playbook objects - Replace deprecated stacked ``@classmethod`` and ``@property``
- Raise an error when an incorrect ``isa`` type is passed to ``FieldAttribute``.
- Remove fallback code for when ``defined``/``undefined`` tests were used on objects containing nested undefined variables; due to changes in lazy evalution of Jinja2 expressions it is no longer needed.
- Remove unused Python stdlib imports from module_utils which were not present for backwards compatibility in: common.file, compat.selectors, facts.network.iscsi, facts.network.nvme, yumdnf
- Remove unused internal imports from module_utils which were not present for backwards compatibility in: common.file, common.parameters, facts.system.caps, yumdnf
- Removed ``straight.plugin`` from the build and packaging requirements.
- Removed unused imports from the following action plugins: async_status, command, pause, set_stats, uri, validate_argument_spec
- Removed unused imports from the following lookup plugins: fileglob, template
- Removed unused imports from the following modules: apt, dnf, expect, pip, slurp, user, yum
- Removed unused imports from the following set of test plugins: files
- Removed unused imports from the following strategy plugins: debug
- Removed unused imports from the following vars plugins: host_group_vars
- The minimum required ``setuptools`` version is now 45.2.0, as it is the oldest version to support Python 3.10.
- Use ``ansible.module_utils.six.moves.collections_abc`` instead of ``ansible.module_utils.common._collections_compat`` in modules and module_utils.
- Use ``collections.abc`` instead of ``ansible.module_utils.common._collections_compat`` in controller code.
- Use ``package_data`` instead of ``include_package_data`` for ``setup.cfg`` to avoid ``setuptools`` warnings.
- ``AnsibleJ2Vars`` class that acts as a storage for all variables for templating purposes now uses ``collections.ChainMap`` internally.
- add parameter ``numeric`` to the iptables module to disable dns lookups when running list -action internally (https://github.com/ansible/ansible/issues/78793).
- allow user to set ansible specific env vars for selecting pager and editor, but still fall back to commonly used defaults.
- ansible-doc - support role extension for semantic markup spec so that ``O()`` and ``RV()`` referring to role entrypoints are rendered more readable (https://github.com/ansible/ansible/pull/80305).
- ansible-doc - support semantic markup in text output (https://github.com/ansible/ansible/pull/80242).
- ansible-doc text output - support ``seealso`` plugin record that was added for filter and test plugin documentation (https://github.com/ansible/ansible/pull/80212).
- ansible-galaxy - Add ability to specify collection versions on the CLI without the need for a colon. Such as ``namespace.name==1.2.3`` vs ``namespace.name:1.2.3``.
- ansible-galaxy - Use Python's native ``raise ... from`` instead of ``six.raise_from``.
- ansible-galaxy - support ``resolvelib >= 0.5.3, < 0.10.0``.
- ansible-galaxy - support ``resolvelib >= 0.5.3, < 1.1.0``.
- ansible-inventory now supports the limit command line options.
- ansible-test - A new ``audit`` option is available when running custom containers. This option can be used to indicate whether a container requires the AUDIT_WRITE capability. The default is ``required``, which most containers will need when using Podman. If necessary, the ``none`` option can be used to opt-out of the capability. This has no effect on Docker, which always provides the capability.
- ansible-test - A new ``cgroup`` option is available when running custom containers. This option can be used to indicate a container requires cgroup v1 or that it does not use cgroup. The default behavior assumes the container works with cgroup v2 (as well as v1).
- ansible-test - Add Alpine 3.17 remote.
- ansible-test - Add Fedora 37 container.
- ansible-test - Add Fedora 37 remote.
- ansible-test - Add FreeBSD 12.4 remote.
- ansible-test - Add RHEL 8.7 remote.
- ansible-test - Add RHEL 9.1 remote.
- ansible-test - Add macOS 13.2 remote.
- ansible-test - Additional log details are shown when containers fail to start or SSH connections to containers fail.
- ansible-test - Connection failures to remote provisioned hosts now show failure details as a warning.
- ansible-test - Containers included with ansible-test no longer disable seccomp by default.
- ansible-test - Disabled the ``ansible-format-automatic-specification`` rule from the ``pylint`` sanity test, now that Python 2.6 is no longer supported.
- ansible-test - Enable the ``trailing-comma-tuple`` rule in the ``pylint`` sanity test.
- ansible-test - Enable the ``unused-import`` rule for the ``pylint`` sanity test for collections.
- ansible-test - Failure to connect to a container over SSH now results in a clear error. Previously tests would be attempted even after initial connection attempts failed.
- ansible-test - Improve consistency of executed ``pylint`` commands by making the plugins ordered.
- ansible-test - Improve consistency of version specific documentation links.
- ansible-test - Integration tests can be excluded from retries triggered by the ``--retry-on-error`` option by adding the ``retry/never`` alias. This is useful for tests that cannot pass on a retry or are too slow to make retries useful.
- ansible-test - Minor cleanup and package updates in distro containers.
- ansible-test - More details are provided about an instance when provisioning fails.
- ansible-test - Moved git handling out of the validate-modules sanity test and into ansible-test.
- ansible-test - Reduce the polling limit for SSHD startup in containers from 60 retries to 10. The one second delay between retries remains in place.
- ansible-test - Removed test containers: fedora36
- ansible-test - Removed test remotes: alpine/3.16, fedora/36, freebsd/12.3, rhel/8.6, rhel/9.0, macos/12.0
- ansible-test - Removed the ``--keep-git`` sanity test option, which was limited to testing ansible-core itself.
- ansible-test - SSH connections from OpenSSH 8.8+ to CentOS 6 containers now work without additional configuration. However, clients older than OpenSSH 7.0 can no longer connect to CentOS 6 containers as a result. The container must have ``centos6`` in the image name for this work-around to be applied.
- ansible-test - SSH shell connections from OpenSSH 8.8+ to ansible-test provisioned network instances now work without additional configuration. However, clients older than OpenSSH 7.0 can no longer open shell sessions for ansible-test provisioned network instances as a result.
- ansible-test - Specify the configuration file location required by test plugins when the config file is not found. This resolves issue: https://github.com/ansible/ansible/issues/79411
- ansible-test - The ``ansible-test env`` command now detects and reports the container ID if running in a container.
- ansible-test - The ``pep8`` sanity test rule ``E203`` is now disabled since it is not PEP 8 compliant. This provides compatibility with output generated by the ``black`` code formatter.
- ansible-test - The ``validate-modules`` sanity test no longer limits the ``__future__`` imports that can be used. Other sanity tests that check ``__future__`` imports remain unchanged. As a result, the error code ``illegal-future-imports`` is no longer used.
- ansible-test - Unit tests now support network disconnect by default when running under Podman. Previously this feature only worked by default under Docker.
- ansible-test - Update Alpine 3 container to 3.17.
- ansible-test - Update Python requirements used for sanity tests.
- ansible-test - Update ``base`` and ``default`` containers to include Python 3.11.0.
- ansible-test - Update ``default`` containers to include new ``docs-build`` sanity test requirements.
- ansible-test - Update error handling code to use Python 3.x constructs, avoiding direct use of ``errno``.
- ansible-test - Update test container to ``7.4.0`` which includes the new PSScriptAnalyzer versions
- ansible-test - Update the CloudStack test plugin to use a newer test container with CloudStack 4.18.0.
- ansible-test - Update the NIOS test plugin to use a newer multi-arch test container.
- ansible-test - Update the ``ansible-bad-import-from`` rule in the ``pylint`` sanity test to recommend ``ansible.module_utils.six.moves.collections_abc`` instead of ``ansible.module_utils.common._collections_compat``.
- ansible-test - Update the ``base`` and ``default`` test containers with the latest requirements.
- ansible-test - Update the ``default`` containers to include the ``package-data`` requirements update.
- ansible-test - Update the ``default`` containers to include the ``pylint`` requirements update.
- ansible-test - Updated the Azure Pipelines CI plugin to work with newer versions of git.
- ansible-test - Use ``stop --time 0`` followed by ``rm`` to remove ephemeral containers instead of ``rm -f``. This speeds up teardown of ephemeral containers.
- ansible-test - Warnings are now shown when using containers that were built with VOLUME instructions.
- ansible-test - When setting the max open files for containers, the container host's limit will be checked. If the host limit is lower than the preferred value, it will be used and a warning will be shown.
- ansible-test - When using Podman, ansible-test will detect if the loginuid used in containers is incorrect. When this occurs a warning is displayed and the container is run with the AUDIT_CONTROL capability. Previously containers would fail under this situation, with no useful warnings or errors given.
- ansible-test acme test container - update version to update used Pebble version, underlying Python and Go base containers, and Python requirements (https://github.com/ansible/ansible/pull/79783).
- ansible-test pslint - Upgrade PSScriptAnalyzer to ``1.21.0`` which enables the ``AvoidMultipleTypeAttributes``, ``AvoidSemicolonsAsLineTerminators``, and ``AvoidUsingBrokenHashAlgorithms`` rules
- ansible-test runtime-metadata sanity test - ensure that ``redirect`` entries in ``meta/runtime.yml`` contain collection names, except for ``module_utils`` plugin redirects and ``import_redirect`` redirects (https://github.com/ansible/ansible/pull/78802).
- ansible-test sanity --test ansible-doc - now also lists documentation for test and filter plugins that are documented (https://github.com/ansible/ansible/pull/77737).
- ansible-test validate-modules - Added support for validating module documentation stored in a sidecar file alongside the module (``{module}.yml`` or ``{module}.yaml``). Previously these files were ignored and documentation had to be placed in ``{module}.py``.
- ansible-test validate-modules - no longer treat falsy non-``False`` values for defaults as ``None`` (https://github.com/ansible/ansible/pull/79267).
- apt - add allow-change-held-packages option to apt remove (https://github.com/ansible/ansible/issues/78131)
- apt_repository - adds ``sources_added`` and ``sources_removed`` to the return of the module (https://github.com/ansible/ansible/issues/79306).
- apt_repository will use the trust repo directories in order of preference (more appropriate to less) as they exist on the target.
- collections - Add additional ignores for commonly rejected file extensions
- collections - Add additional includes for REUSE license files (https://github.com/ansible/ansible/issues/79368)
- deb822_repository - Add new module for managing DEB822 formatted apt repositories
- debug - Perform argspec valdiation in debug action plugin (https://github.com/ansible/ansible/issues/79862)
- dnf5 - Add new module for managing packages and other artifacts via the next version of DNF (https://github.com/ansible/ansible/issues/78898)
- galaxy - include ``license_file`` in the default manifest directives (https://github.com/ansible/ansible/pull-request/79420)
- optimized var loading by caching results as there is no variance in input during run.
- pycompat24 module_utils - Remove support for Python 2.5 and earlier.
- sanity tests - updates the collection-deprecated-version tests to ignore the ``prerelease`` component of the collection version ().
- strftime filter, additional docs and links to source of truth.
- updated the vendored distro library to upstream version (https://github.com/ansible/ansible/pull/79227)
- validate-modules sanity test - add support for semantic markup (https://github.com/ansible/ansible/pull/80243).
- validate-modules sanity test - if the ``check_mode`` attribute is present, check that it coincides with the ``support_check_mode`` parameter of ``AnsibleModule`` (https://github.com/ansible/ansible/pull/80090).
- validate-modules sanity test - remove support for the never implemented ``forced_action_plugin`` attribute (https://github.com/ansible/ansible/pull/79317).
- validate-modules sanity test - support the ``plugin`` see-also part of the semantic markup specification (https://github.com/ansible/ansible/pull/80244).

amazon.aws
~~~~~~~~~~

- Add connectivity_type to ec2_vpc_nat_gateway module (https://github.com/ansible-collections/amazon.aws/pull/1267).
- Add github actions to run unit and sanity tests.(https://github.com/ansible-collections/amazon.aws/pull/1393).
- AnsibleAWSModule - add support to the ``client`` and ``resource`` methods for overriding the default parameters (https://github.com/ansible-collections/amazon.aws/pull/1303).
- CONTRIBUTING.md - refactors and adds to contributor documentation (https://github.com/ansible-collections/amazon.aws/issues/924)
- Refactor inventory plugins and add aws_rds inventory unit tests (https://github.com/ansible-collections/amazon.aws/pull/1218).
- Refactor module_utils/cloudfront_facts.py and add unit tests (https://github.com/ansible-collections/amazon.aws/pull/1265).
- The ``black`` code formatter has been run across the collection to improve code consistency (https://github.com/ansible-collections/amazon.aws/pull/1465).
- amazon.aws collection - refacterization of code to use argument specification ``fallback`` when falling back to environment variables for security credentials and AWS connection details (https://github.com/ansible-collections/amazon.aws/pull/1174).
- amazon.aws inventory plugins - additional refactorization of inventory plugin connection handling (https://github.com/ansible-collections/amazon.aws/pull/1271).
- amazon.aws lookup plugins - ``aws_access_key`` has been renamed to ``access_key`` for consistency between modules and plugins, ``aws_access_key`` remains as an alias. This change should have no observable effect for users outside the module/plugin documentation (https://github.com/ansible-collections/amazon.aws/pull/1225).
- amazon.aws lookup plugins - ``aws_profile`` has been renamed to ``profile`` for consistency between modules and plugins, ``aws_profile`` remains as an alias. This change should have no observable effect for users outside the module/plugin documentation (https://github.com/ansible-collections/amazon.aws/pull/1225).
- amazon.aws lookup plugins - ``aws_secret_key`` has been renamed to ``secret_key`` for consistency between modules and plugins, ``aws_secret_key`` remains as an alias. This change should have no observable effect for users outside the module/plugin documentation (https://github.com/ansible-collections/amazon.aws/pull/1225).
- amazon.aws lookup plugins - ``aws_security_token`` has been renamed to ``session_token`` for consistency between modules and plugins, ``aws_security_token`` remains as an alias. This change should have no observable effect for users outside the module/plugin documentation (https://github.com/ansible-collections/amazon.aws/pull/1225).
- amazon.aws modules - bulk update of import statements following various refactors (https://github.com/ansible-collections/amazon.aws/pull/1310).
- autoscaling_group - minor linting fixes (https://github.com/ansible-collections/amazon.aws/pull/1181).
- aws_account_attribute - the ``aws_account_attribute`` lookup plugin has been refactored to use ``AWSLookupBase`` as its base class (https://github.com/ansible-collections/amazon.aws/pull/1225).
- aws_ec2 inventory - minor linting fixes (https://github.com/ansible-collections/amazon.aws/pull/1181).
- aws_secret - the ``aws_secret`` lookup plugin has been refactored to use ``AWSLookupBase`` as its base class (https://github.com/ansible-collections/amazon.aws/pull/1225).
- aws_secret - the ``aws_secret`` lookup plugin has been renamed ``secretsmanager_secret``, ``aws_secret`` remains as an alias (https://github.com/ansible-collections/amazon.aws/pull/1225).
- aws_ssm - the ``aws_ssm`` lookup plugin has been refactored to use ``AWSLookupBase`` as its base class (https://github.com/ansible-collections/amazon.aws/pull/1225).
- aws_ssm - the ``aws_ssm`` lookup plugin has been renamed ``ssm_parameter``, ``aws_ssm`` remains as an alias (https://github.com/ansible-collections/amazon.aws/pull/1225).
- backup - Add logic for backup_selection* modules (https://github.com/ansible-collections/amazon.aws/pull/1530).
- bulk migration of ``%`` and ``.format()`` to fstrings (https://github.com/ansible-collections/amazon.aws/pull/1483).
- cloud module_utils - minor linting fixes (https://github.com/ansible-collections/amazon.aws/pull/1181).
- cloudtrail_info - minor linting fixes (https://github.com/ansible-collections/amazon.aws/pull/1181).
- cloudwatch - Add metrics and extended_statistic keys to cloudwatch module (https://github.com/ansible-collections/amazon.aws/pull/1133).
- cloudwatchlogs_log_group - minor linting fixes (https://github.com/ansible-collections/amazon.aws/pull/1181).
- docs_fragments - ``amazon.aws.boto3`` fragment now pulls the botocore version requirements from ``module_utils.botocore`` (https://github.com/ansible-collections/amazon.aws/pull/1248).
- docs_fragments - common parameters for modules and plugins have been synchronised and moved to ``amazon.aws.common.modules`` and ``amazon.aws.common.plugins`` (https://github.com/ansible-collections/amazon.aws/pull/1248).
- docs_fragments - region parameters for modules and plugins have been synchronised and moved to ``amazon.aws.region.modules`` and ``amazon.aws.region.plugins`` (https://github.com/ansible-collections/amazon.aws/pull/1248).
- ec2_ami - Extend the unit-test coverage of the module (https://github.com/ansible-collections/amazon.aws/pull/1159).
- ec2_ami - add support for BootMode, TpmSupport, UefiData params (https://github.com/ansible-collections/amazon.aws/pull/1037).
- ec2_ami - allow ``ImageAvailable`` waiter to retry when the image can't be found (https://github.com/ansible-collections/amazon.aws/pull/1321).
- ec2_ami_info - Add unit-tests coverage (https://github.com/ansible-collections/amazon.aws/pull/1252).
- ec2_eip - minor linting fixes (https://github.com/ansible-collections/amazon.aws/pull/1181).
- ec2_eni_info - Add unit-tests coverage (https://github.com/ansible-collections/amazon.aws/pull/1236).
- ec2_instance - avoid changing ``module.params`` (https://github.com/ansible-collections/amazon.aws/pull/1187).
- ec2_instance - more consistently return ``instances`` information (https://github.com/ansible-collections/amazon.aws/pull/964).
- ec2_instance - remove unused import (https://github.com/ansible-collections/amazon.aws/pull/1350).
- ec2_instance - updated to avoid manipulating ``module.params`` (https://github.com/ansible-collections/amazon.aws/pull/1337).
- ec2_key - Add unit-tests coverage (https://github.com/ansible-collections/amazon.aws/pull/1288).
- ec2_metadata_facts - added support to query instance tags in metadata (https://github.com/ansible-collections/amazon.aws/pull/1186).
- ec2_security_group - added rule options to argument specifications to improve handling of inputs (https://github.com/ansible-collections/amazon.aws/pull/1214).
- ec2_security_group - refacter ``get_target_from_rule()`` (https://github.com/ansible-collections/amazon.aws/pull/1221).
- ec2_security_group - refactor rule expansion and add unit tests (https://github.com/ansible-collections/amazon.aws/pull/1261).
- ec2_snapshot - Reenable the integration tests (https://github.com/ansible-collections/amazon.aws/pull/1235).
- ec2_snapshot_info - Add unit-tests coverage (https://github.com/ansible-collections/amazon.aws/pull/1211).
- ec2_spot_instance - add parameter ``terminate_instances`` to support terminate instances associated with spot requests. (https://github.com/ansible-collections/amazon.aws/pull/1402).
- ec2_vpc_nat_gateway - ensure allocation_id is defined before potential access (https://github.com/ansible-collections/amazon.aws/pull/1350).
- ec2_vpc_route_table - add support for Carrier Gateway entry (https://github.com/ansible-collections/amazon.aws/pull/926).
- ec2_vpc_subnet - retry fetching subnet details after creation if the first attempt fails (https://github.com/ansible-collections/amazon.aws/pull/1526).
- inventory aws ec2 - add parameter ``use_ssm_inventory`` allowing to query ssm inventory information for configured EC2 instances and populate hostvars (https://github.com/ansible-collections/amazon.aws/issues/704).
- inventory plugins - refactor cache handling (https://github.com/ansible-collections/amazon.aws/pull/1285).
- inventory plugins - refactor file verification handling (https://github.com/ansible-collections/amazon.aws/pull/1285).
- inventory_aws_ec2 integration tests - replace local module ``test_get_ssm_inventory`` by ``community.aws.ssm_inventory_info`` (https://github.com/ansible-collections/amazon.aws/pull/1416).
- kms_key - Add multi_region option to create_key (https://github.com/ansible-collections/amazon.aws/pull/1290).
- kms_key_info - minor linting fixes (https://github.com/ansible-collections/amazon.aws/pull/1181).
- lambda -  add support for function layers when creating or updating lambda function (https://github.com/ansible-collections/amazon.aws/pull/1118).
- lambda - minor linting fixes (https://github.com/ansible-collections/amazon.aws/pull/1181).
- lambda - use common ``get_aws_account_info`` helper rather than reimplementing (https://github.com/ansible-collections/amazon.aws/pull/1181).
- lambda_alias - refactored to avoid passing around the complex ``module`` resource (https://github.com/ansible-collections/amazon.aws/pull/1336).
- lambda_alias - updated to avoid manipulating ``module.params`` (https://github.com/ansible-collections/amazon.aws/pull/1336).
- lambda_event -  Added support to set FunctionResponseTypes when creating lambda event source mappings (https://github.com/ansible-collections/amazon.aws/pull/1209).
- lambda_execute - minor linting fixes (https://github.com/ansible-collections/amazon.aws/pull/1181).
- lambda_info - updated to avoid manipulating ``module.params`` (https://github.com/ansible-collections/amazon.aws/pull/1336).
- lambda_layer_info -  add support for parameter version_number to retrieve detailed information for a specific layer version (https://github.com/ansible-collections/amazon.aws/pull/1293).
- module_utils - move RetryingBotoClientWrapper into module_utils.retries for reuse with other plugin types (https://github.com/ansible-collections/amazon.aws/pull/1230).
- module_utils - move exceptions into dedicated python module (https://github.com/ansible-collections/amazon.aws/pull/1246).
- module_utils - refacter botocore version validation into module_utils.botocore for future reuse (https://github.com/ansible-collections/amazon.aws/pull/1227).
- module_utils.acm - Refactor ACMServiceManager class and add unit tests (https://github.com/ansible-collections/amazon.aws/pull/1273).
- module_utils.botocore - Add Ansible AWS User-Agent identification (https://github.com/ansible-collections/amazon.aws/pull/1306).
- module_utils.botocore - refactorization of ``get_aws_region``, ``get_aws_connection_info`` so that the code can be reused by non-module plugins (https://github.com/ansible-collections/amazon.aws/pull/1231).
- module_utils.policy - minor refacter of code to reduce complexity and improve test coverage (https://github.com/ansible-collections/amazon.aws/pull/1136).
- module_utils.s3 - Refactor get_s3_connection into a module_utils for S3 modules and expand module_utils.s3 unit tests (https://github.com/ansible-collections/amazon.aws/pull/1139).
- module_utils/botocore - added support to ``_boto3_conn`` for passing dictionaries of configuration (https://github.com/ansible-collections/amazon.aws/pull/1307).
- module_utils/elbv2 - removed compatibility code for ``botocore < 1.10.30`` (https://github.com/ansible-collections/amazon.aws/pull/1477).
- plugin_utils - Added ``AWSConnectionBase`` to support refactoring connection plugins (https://github.com/ansible-collections/amazon.aws/pull/1340).
- rds - AWS is phasing out aurora1. Integration tests use aurora2 (aurora-mysql) by default (https://github.com/ansible-collections/amazon.aws/pull/1233).
- rds_cluster - New ``engine_mode`` parameter (https://github.com/ansible-collections/amazon.aws/pull/941).
- rds_cluster - Split up the functional tests in smaller targets (https://github.com/ansible-collections/amazon.aws/pull/1175).
- rds_cluster - add new options (e.g., ``db_cluster_instance_class``, ``allocated_storage``, ``storage_type``, ``iops``) (https://github.com/ansible-collections/amazon.aws/pull/1191).
- rds_cluster - update list of supported engines with ``mysql`` and ``postgres`` (https://github.com/ansible-collections/amazon.aws/pull/1191).
- rds_cluster_snapshot - minor linting fixes (https://github.com/ansible-collections/amazon.aws/pull/1181).
- rds_instance - Split up the integration test-suite in a series of smaller tests (https://github.com/ansible-collections/amazon.aws/pull/1185).
- rds_instance - add support for gp3 storage type (https://github.com/ansible-collections/amazon.aws/pull/1266).
- rds_instance - minor linting fixes (https://github.com/ansible-collections/amazon.aws/pull/1181).
- rds_instance_info - Add unit-tests coverage (https://github.com/ansible-collections/amazon.aws/pull/1132).
- rds_instance_snapshot - minor linting fixes (https://github.com/ansible-collections/amazon.aws/pull/1181).
- rds_param_group - drop Python2 import fallbacks (https://github.com/ansible-collections/amazon.aws/pull/1513).
- route53_health_check -  added support for enabling Latency graphs (MeasureLatency) during creation of a Route53 Health Check. (https://github.com/ansible-collections/amazon.aws/pull/1201).
- route53_health_check - Drop deprecation warning (https://github.com/ansible-collections/community.aws/pull/1335).
- route53_health_check - minor fix for returning health check info while updating a Route53 health check (https://github.com/ansible-collections/amazon.aws/pull/1200).
- route53_health_check - minor linting fixes (https://github.com/ansible-collections/amazon.aws/pull/1181).
- route53_info - drop unused imports (https://github.com/ansible-collections/amazon.aws/pull/1462).
- route53_zone - added support for associating multiple VPCs to route53 hosted zones (https://github.com/ansible-collections/amazon.aws/pull/1300).
- s3_bucket - add option to support creation of buckets with object lock enabled (https://github.com/ansible-collections/amazon.aws/pull/1372).
- s3_bucket - add support for S3 dualstack endpoint (https://github.com/ansible-collections/amazon.aws/pull/1305).
- s3_bucket - ensure ``public_access`` is configured before updating policies (https://github.com/ansible-collections/amazon.aws/pull/1511).
- s3_bucket - handle missing read permissions more gracefully when possible (https://github.com/ansible-collections/amazon.aws/pull/1406).
- s3_bucket - refactor S3 connection code (https://github.com/ansible-collections/amazon.aws/pull/1305).
- s3_object - refactor S3 connection code (https://github.com/ansible-collections/amazon.aws/pull/1305).
- s3_object - refactor main to reduce complexity (https://github.com/ansible-collections/amazon.aws/pull/1193).
- s3_object_info - minor linting fixes (https://github.com/ansible-collections/amazon.aws/pull/1181).
- s3_object_info - refactor S3 connection code (https://github.com/ansible-collections/amazon.aws/pull/1305).

ansible.netcommon
~~~~~~~~~~~~~~~~~

- httpapi - Add option netcommon_httpapi_ciphers to allow overriding default SSL/TLS ciphers. (https://github.com/ansible-collections/ansible.netcommon/pull/494)
- libssh - add ``config_file`` option to specify an alternate SSH config file to use.
- parse_cli - add support for multiple matches inside a block by adding new dictionary key to result
- telnet - add ``stdout`` and ``stdout_lines`` to module output.
- telnet - add support for regexes to ``login_prompt`` and ``password_prompt``.
- telnet - apply ``timeout`` to command prompts.

ansible.posix
~~~~~~~~~~~~~

- Add jsonl callback plugin to ansible.posix collection
- firewalld - add `protocol` parameter
- json and jsonl - Add the ``ANSIBLE_JSON_INDENT`` parameter
- json and jsonl - Add the ``path`` attribute into the play and task output
- mount - Add ``absent_from_fstab`` state (https://github.com/ansible-collections/ansible.posix/pull/166).
- mount - Add ``ephemeral`` value for the ``state`` parameter, that allows to mount a filesystem without altering the ``fstab`` file (https://github.com/ansible-collections/ansible.posix/pull/267).
- r4e_rpm_ostree - new module for validating package state on RHEL for Edge
- rhel_facts - new facts module to handle RHEL specific facts
- rhel_rpm_ostree - new module to handle RHEL rpm-ostree specific package management functionality
- rpm_ostree_upgrade - new module to automate rpm-ostree upgrades
- rpm_ostree_upgrade - new module to manage upgrades for rpm-ostree based systems

ansible.utils
~~~~~~~~~~~~~

- to_xml - Added support for using spaces to indent an XML doc via a new `indent` parameter.
- to_xml - Added support to disable xml declartion with full_document flag.
- validate - Add option `check_format` for the jsonschema engine to disable JSON Schema format checking.
- validate - Add support for JSON Schema draft 2019-09 and 2020-12 as well as automatically choosing the draft from the `$schema` field of the criteria.

ansible.windows
~~~~~~~~~~~~~~~

- Process - Add support for starting a process with a custom parent
- win_reboot - Display connection messages under 4 v's ``-vvvv`` instead of 3
- win_updates - Added the ``rebooted`` return value to document if a host was rebooted - https://github.com/ansible-collections/ansible.windows/issues/485

cisco.aci
~~~~~~~~~

- Add Node Profile BGP Peer and Route Control Profile functionalities to aci_l3out_bgp_peer module (#340)
- Add SVI auto state support (auto_state attribute) to aci_l3out_interface (#348)
- Add aci_aaa_domain, aci_aaa_role and aci_custom_privilege modules (#226)
- Add aci_access_span_dst_group module for fabric access policies span destination group support (#405)
- Add aci_access_span_filter_group and aci_access_span_filter_group_entry modules for access span filter group support (#407)
- Add aci_config_export_policy module (#380)
- Add aci_fabric_pod_policy_group module (#230)
- Add aci_igmp_interface_policy module (#381)
- Add aci_interface_config module for new interface configuration available in ACI v5.2(5)+ (#383)
- Add aci_interface_policy_leaf_profile_fex_policy_group module and add FEX support to aci_access_port_to_interface_policy_leaf_profile (#233)
- Add aci_interface_policy_spanning_tree  module (#387)
- Add aci_tenant_span_src_group_src module (#344)
- Add action_groups for module_defaults (#316)
- Add support for filter direction in aci_contract_subject and aci_contract_subject_to_filter (#306)
- Update modules to assign roles and permissions to a user (#225)

cisco.dnac
~~~~~~~~~~

- accesspoint_configuration_details_by_task_id_info - new module
- authentication_policy_servers_info - new module
- credential_to_site_by_siteid_create_v2 - new module
- device_interface_info - attributes `lastInputTime` and `lastOutputTime` were added.
- device_reboot_apreboot_info - new module
- dnac_packages_info - new module
- eox_status_device_info - new module
- eox_status_summary_info - new module
- event_email_config - new module
- event_email_config_info - new module
- event_snmp_config_info - new module
- event_syslog_config - new module
- event_syslog_config_info - new module
- execute_suggested_actions_commands - new module
- global_credential_v2 - new module
- global_credential_v2_info - new module
- integration_settings_instances_itsm - new module
- integration_settings_instances_itsm_info - new module
- lan_automation_log_by_serial_number_info - new module
- network_device_user_defined_field - new module
- network_device_user_defined_field_info - new module
- network_v2 - new module
- network_v2_info - new module
- pnp_device_claim_to_site - attributes `removeInactive` and `hostname` were removed.
- role_permissions_info - new module
- roles_info - new module
- sda_fabric_border_device - attributes `routeDistributionProtocol` and `borderPriority` were added.
- sda_fabric_control_plane_device attribute `routeDistributionProtocol` was added.
- sda_fabric_edge_device - attribute `siteNameHierarchy` was added.
- sda_fabric_site - attribute `fabricType` was added.
- sda_port_assignment_for_user_device - attribute `interfaceNames` was added.
- sda_virtual_network - attribute `vManageVpnId` was added.
- sda_virtual_network_ip_pool - attribute `isBridgeModeVm` was added.
- sda_virtual_network_v2 - attribute `isBridgeModeVm` was added.
- service_provider_v2 - new module
- service_provider_v2_info - new module
- sp_profile_delete_v2 - new module
- user - new module
- user_info - new module
- users_external_servers_info - new module
- wireless_accespoint_configuration - new module
- wireless_accesspoint_configuration_summary_info - new module

cisco.ios
~~~~~~~~~

- cliconf - Added support for commit confirm functionality and rollback based on timeout.
- ios_bgp_address_family - add option redistribute.ospf.include_connected when redistributing OSPF in IPv6 AFI
- ios_bgp_address_family - add option redistribute.ospf.match.externals.type_1 to allow
- ios_bgp_address_family - add option redistribute.ospf.match.externals.type_2 to allow
- ios_facts - Add ip value to ansible_net_neighbors dictionary for cdp neighbours. (https://github.com/ansible-collections/cisco.ios/pull/748)
- ios_facts - Add ip value to ansible_net_neighbors dictionary for lldp neighbours. (https://github.com/ansible-collections/cisco.ios/pull/760)
- ios_facts - default facts to show operating state data autonomous or controller mode.
- ios_interfaces - Add mode attribute in ios_interfaces, which supports layer2 and layer3 as options.
- ios_l2_interfaces - more options for modes attribute added.
- ios_route_maps - added 32-bit number support (https://github.com/ansible-collections/cisco.ios/pull/692)
- specification of OSPF E1 routes
- specification of OSPF E2 routes

cisco.iosxr
~~~~~~~~~~~

- bgp_global - Add ``no_prepend`` option and  ``set`` and ``replace_as`` suboptions under local_as option. (https://github.com/ansible-collections/cisco.iosxr/issues/336)
- bgp_global - Add ``password`` option and  ``encrypted`` and ``inheritance_disable`` suboptions. (https://github.com/ansible-collections/cisco.iosxr/issues/337)
- bgp_global - Add ``use`` option and  ``neighbor_group`` and ``session_group`` suboptions. (https://github.com/ansible-collections/cisco.iosxr/issues/312)
- iosxr.iosxr_bgp_global - Add missing set option in fast-detect dict of bgp nbr.

cisco.meraki
~~~~~~~~~~~~

- New module - meraki_network_settings - Configure detailed settings of a network.
- meraki_webhook - Add payload template parameter

cisco.mso
~~~~~~~~~

- Add automatic creation of site bd when not existing in mso_schema_site_bd_subnet module (#263)
- Add automatic schema validation functionality to mso_schema_template_deploy and ndo_schema_template_deploy (#318)
- Add ip_data_plane_learning and preferred_group arguments to mso_schema_template_vrf module (#358)
- Add module mso_schema_site_anp_epg_bulk_staticport (#330)
- Add ndo_schema_template_deploy to support NDO 4+ deploy functionality (#305)
- Add route_reachability attribute to mso_schema_site_external_epg module (#335)
- Add support for l3out from different template or schema in mso_schema_site_bd_l3out (#304)
- Add support for orchestrator_only attribute for mso_tenant with state absent (#268)

cisco.nxos
~~~~~~~~~~

- `nxos_acls` - Support ICMPv6 option. Please refer to module doc for all new options (https://github.com/ansible-collections/cisco.nxos/issues/624).
- `nxos_facts` - Update facts gathering logic to ensure that `gather_network_resources: all` does not fail for NX-OS on MDS switches.
- `nxos_l2_interfaces` - Add new mode dot1q-tunnel (https://github.com/ansible-collections/cisco.nxos/issues/600).
- `nxos_route_maps` - add support for 'set ip next-hop <>' command in route-maps
- `nxos_vxlan_vtep` - add support for 'advertise virtual-rmac' command under nve interface

cloud.common
~~~~~~~~~~~~

- sanity - fix sanity errors (https://github.com/ansible-collections/cloud.common/issues/106)
- units - ensure tests/units follow the Ansible-defined unit tests structure (https://github.com/ansible-collections/cloud.common/issues/89)

cloudscale_ch.cloud
~~~~~~~~~~~~~~~~~~~

- Add UEFI firmware type option for custom images.
- Fixed a typo in region code.
- Fixed various documentation typos.
- Streamlined the flavors to the new format ``flex-y-x`` across the related modules and tests.

community.aws
~~~~~~~~~~~~~

- The ``black`` code formatter has been run across the collection to improve code consistency (https://github.com/ansible-collections/community.aws/pull/1784).
- aws_config_delivery_channel - add support for encrypted objects in S3 via KMS key (https://github.com/ansible-collections/community.aws/pull/1786).
- aws_ssm - Updated the documentation to explicitly mention that the ``ansible_user`` and ``remote_user`` variables are not supported by the plugin (https://github.com/ansible-collections/community.aws/pull/1682).
- aws_ssm - add ``ansible_aws_ssm_s3_addressing_style`` to allow setting the S3 addressing style (https://github.com/ansible-collections/community.aws/pull/1633).
- aws_ssm - add support for custom SSM documents (https://github.com/ansible-collections/community.aws/pull/876).
- aws_ssm - added support for specifying the endpoint to use when connecting to the S3 API (https://github.com/ansible-collections/community.aws/pull/1619).
- aws_ssm - avoid overloading ``subprocess`` (https://github.com/ansible-collections/community.aws/pull/1660).
- aws_ssm - cleanup logging output (https://github.com/ansible-collections/community.aws/pull/1660).
- aws_ssm - minor refactoring (https://github.com/ansible-collections/community.aws/pull/1660).
- aws_ssm - refactor boto3 client initialization (https://github.com/ansible-collections/community.aws/pull/1663).
- aws_ssm - refactor remote command generation (https://github.com/ansible-collections/community.aws/pull/1664).
- aws_ssm - remove unused imports (https://github.com/ansible-collections/community.aws/pull/1707).
- aws_ssm - rework environment variable handling to use built in Ansible plugin support (https://github.com/ansible-collections/community.aws/pull/514).
- batch_job_definition - make trailing comma tuple explicitly a tuple (https://github.com/ansible-collections/community.aws/pull/1707).
- bulk migration of ``%`` and ``.format()`` to fstrings (https://github.com/ansible-collections/community.aws/pull/1810).
- cloudfront_distribution - add ``http3`` support via parameter value ``http2and3`` for parameter ``http_version`` (https://github.com/ansible-collections/community.aws/pull/1753).
- cloudfront_distribution - add ``origin_shield`` options (https://github.com/ansible-collections/community.aws/pull/1557).
- cloudfront_distribution - documented ``connection_attempts`` and ``connection_timeout`` the module was already capable of using them
- community.aws - updated document fragments based on changes in amazon.aws (https://github.com/ansible-collections/community.aws/pull/1738).
- community.aws - updated imports based on changes in amazon.aws (https://github.com/ansible-collections/community.aws/pull/1738).
- ec2_launch_template - Add parameter ``version_description`` (https://github.com/ansible-collections/community.aws/pull/1763).
- ecs_cluster - add support for ``capacity_providers`` and ``capacity_provider_strategy`` features (https://github.com/ansible-collections/community.aws/pull/1640).
- ecs_cluster - append default value to documentation (https://github.com/ansible-collections/community.aws/pull/1636).
- ecs_ecr - add ``encryption_configuration`` option (https://github.com/ansible-collections/community.aws/pull/1623).
- ecs_ecr - use ``compare_policies`` when comparing lifecycle policies instead of naive ``sort_json_policy_dict`` comparisons (https://github.com/ansible-collections/community.aws/pull/1551).
- ecs_service - ``task_definition`` is now optional when ``force_new_deployment`` is ``True`` (https://github.com/ansible-collections/community.aws/pull/1680).
- ecs_service - added new parameter ``enable_execute_command`` (https://github.com/ansible-collections/community.aws/pull/488).
- ecs_service - handle SDK errors more cleanly on update failures (https://github.com/ansible-collections/community.aws/pull/488).
- ecs_service - new parameter ``purge_placement_constraints``  to have the ability to remove the placement constraints of an ECS Service (https://github.com/ansible-collections/community.aws/pull/1716).
- ecs_service - new parameter ``purge_placement_strategy`` to have the ability to remove the placement strategy of an ECS Service (https://github.com/ansible-collections/community.aws/pull/1716).
- ecs_service - support load balancer update for existing ECS services (https://github.com/ansible-collections/community.aws/pull/1625).
- elasticache - Use the ``cache.t3.small`` node type in the example. ``cache.m1.small`` is not deprecated.
- elasticache_parameter_group - add ``redis6.x`` group family on the module input choices (https://github.com/ansible-collections/community.aws/pull/1476).
- elb_target_group - add support for ``protocol_version`` parameter (https://github.com/ansible-collections/community.aws/pull/1496).
- iam_role - Drop deprecation warning, because the standard value for purge parameters is ``true`` (https://github.com/ansible-collections/community.aws/pull/1636).
- iam_role - added ``assume_role_policy_document_raw`` to the role return values, this doesn't convert policy document contents from CamelCase to snake_case (https://github.com/ansible-collections/community.aws/issues/551).
- iam_role_info - added ``assume_role_policy_document_raw`` to the role return values, this doesn't convert policy document contents from CamelCase to snake_case (https://github.com/ansible-collections/community.aws/issues/551).
- inspector_target - minor linting fix (https://github.com/ansible-collections/community.aws/pull/1707).
- minor code fixes and enable integration tests for modules cloudfront_distribution, cloudfront_invalidation and cloudfront_origin_access_identity (https://github.com/ansible-collections/community.aws/pull/1596).
- module_utils.botocore - Add Ansible AWS User-Agent identification (https://github.com/ansible-collections/community.aws/pull/1632).
- msk_cluster - add option for SASL/IAM authentication and add support to disable unauthenticated clients (https://github.com/ansible-collections/community.aws/issues/1761).
- s3_lifecycle - add parameter ``noncurrent_version_keep_newer`` to set the number of newest noncurrent versions to retain (https://github.com/ansible-collections/community.aws/pull/1606).
- secretsmanager_secret - added support for region replication using the ``replica`` parameter (https://github.com/ansible-collections/community.aws/pull/827).
- secretsmanager_secret - added the ``overwrite`` parameter to support only setting the secret if it doesn't exist (https://github.com/ansible-collections/community.aws/pull/1628).
- sns - Add support for ``message_group_id`` and ``message_deduplication_id`` (https://github.com/ansible-collections/community.aws/pull/1733).
- sns_topic - add support for ``content_based_deduplication`` parameter (https://github.com/ansible-collections/community.aws/pull/1693).
- sns_topic - add support for ``tags`` and ``purge_tags`` (https://github.com/ansible-collections/community.aws/pull/972).
- sqs_queue - add support for ``deduplication_scope`` parameter (https://github.com/ansible-collections/community.aws/pull/1603).
- sqs_queue - add support for ``fifo_throughput_limit`` parameter (https://github.com/ansible-collections/community.aws/pull/1603).
- ssm_parameter - add support for tags in ssm parameters (https://github.com/ansible-collections/community.aws/issues/1573).
- ssm_parameter - fix typo in examples ``paramater`` (https://github.com/ansible-collections/community.aws/issues/1642).
- wafv2_rule_group_info - remove unused and deprecated ``state`` parameter (https://github.com/ansible-collections/community.aws/pull/1555).

community.crypto
~~~~~~~~~~~~~~~~

- get_certificate - add ``asn1_base64`` option to control whether the ASN.1 included in the ``extensions`` return value is binary data or Base64 encoded (https://github.com/ansible-collections/community.crypto/pull/592).
- get_certificate - adds ``ciphers`` option for custom cipher selection (https://github.com/ansible-collections/community.crypto/pull/571).
- x509_certificate_info - adds ``issuer_uri`` field in return value based on Authority Information Access data (https://github.com/ansible-collections/community.crypto/pull/530).
- x509_crl - the ``crl_mode`` option has been added to replace the existing ``mode`` option (https://github.com/ansible-collections/community.crypto/issues/596).

community.digitalocean
~~~~~~~~~~~~~~~~~~~~~~

- digital_ocean_load_balancer - add support for C(size_unit) over deprecated C(size); deprecate C(algorithm) completely (https://github.com/ansible-collections/community.digitalocean/issues/270).
- documentation - refresh the "Testing and Development" section of the C(README.md) (https://github.com/ansible-collections/community.digitalocean/issues/268).
- integration tests - add a dedicated integration test for C(digital_ocean_database_info) (https://github.com/ansible-collections/community.digitalocean/issues/289).
- integration tests - set pull request integration tests to run against branch instead of last commit (https://github.com/ansible-collections/community.digitalocean/issues/291).

community.dns
~~~~~~~~~~~~~

- hosttech inventory plugin - allow to configure token, username, and password with ``ANSIBLE_HOSTTECH_DNS_TOKEN``, ``ANSIBLE_HOSTTECH_API_USERNAME``, and ``ANSIBLE_HOSTTECH_API_PASSWORD`` environment variables, respectively (https://github.com/ansible-collections/community.dns/pull/131).
- various modules and inventory plugins - add new option ``txt_character_encoding`` which controls whether numeric escape sequences are interpreted as octals or decimals when ``txt_transformation=quoted`` (https://github.com/ansible-collections/community.dns/pull/134).

community.docker
~~~~~~~~~~~~~~~~

- Restrict requests to versions before 2.29.0, and urllib3 to versions before 2.0.0. This is necessary until the vendored code from Docker SDK for Python has been fully adjusted to work with a feature of urllib3 that is used since requests 2.29.0 (https://github.com/ansible-collections/community.docker/issues/611, https://github.com/ansible-collections/community.docker/pull/612).
- current_container_facts - make work with current Docker version, also support Podman (https://github.com/ansible-collections/community.docker/pull/510).
- docker_api connection plugin - when copying files to/from a container, stream the file contents instead of first reading them to memory (https://github.com/ansible-collections/community.docker/pull/545).
- docker_host_info - allow to list all containers with new option ``containers_all`` (https://github.com/ansible-collections/community.docker/issues/535, https://github.com/ansible-collections/community.docker/pull/538).
- docker_image - when using ``archive_path``, detect whether changes are necessary based on the image ID (hash). If the existing tar archive matches the source, do nothing. Previously, each task execution re-created the archive (https://github.com/ansible-collections/community.docker/pull/500).

community.general
~~~~~~~~~~~~~~~~~

- apache2_module - add module argument ``warn_mpm_absent`` to control whether warning are raised in some edge cases (https://github.com/ansible-collections/community.general/pull/5793).
- apt_rpm - adds ``clean``, ``dist_upgrade`` and ``update_kernel``  parameters for clear caches, complete upgrade system, and upgrade kernel packages (https://github.com/ansible-collections/community.general/pull/5867).
- bitwarden lookup plugin - can now retrieve secrets from custom fields (https://github.com/ansible-collections/community.general/pull/5694).
- bitwarden lookup plugin - implement filtering results by ``collection_id`` parameter (https://github.com/ansible-collections/community.general/issues/5849).
- cmd_runner module utils - ``cmd_runner_fmt.as_bool()`` can now take an extra parameter to format when value is false (https://github.com/ansible-collections/community.general/pull/5647).
- cpanm - minor change, use feature from ``ModuleHelper`` (https://github.com/ansible-collections/community.general/pull/6385).
- dconf - be forgiving about boolean values: convert them to GVariant booleans automatically (https://github.com/ansible-collections/community.general/pull/6206).
- dconf - if ``gi.repository.GLib`` is missing, try to respawn in a Python interpreter that has it (https://github.com/ansible-collections/community.general/pull/6491).
- dconf - minor refactoring improving parameters and dependencies validation (https://github.com/ansible-collections/community.general/pull/6336).
- dconf - parse GVariants for equality comparison when the Python module ``gi.repository`` is available (https://github.com/ansible-collections/community.general/pull/6049).
- deps module utils - add function ``failed()`` providing the ability to check the dependency check result without triggering an exception (https://github.com/ansible-collections/community.general/pull/6383).
- dig lookup plugin - Support multiple domains to be queried as indicated in docs (https://github.com/ansible-collections/community.general/pull/6334).
- dig lookup plugin - support CAA record type (https://github.com/ansible-collections/community.general/pull/5913).
- dnsimple - set custom User-Agent for API requests to DNSimple (https://github.com/ansible-collections/community.general/pull/5927).
- dnsimple_info - minor refactor in the code (https://github.com/ansible-collections/community.general/pull/6440).
- flatpak_remote - add new boolean option ``enabled``. It controls, whether the remote is enabled or not (https://github.com/ansible-collections/community.general/pull/5926).
- gconftool2 - refactor using ``ModuleHelper`` and ``CmdRunner`` (https://github.com/ansible-collections/community.general/pull/5545).
- gitlab_group_variable, gitlab_project_variable - refactor function out to module utils (https://github.com/ansible-collections/community.general/pull/6384).
- gitlab_project - add ``builds_access_level``, ``container_registry_access_level`` and ``forking_access_level`` options (https://github.com/ansible-collections/community.general/pull/5706).
- gitlab_project - add ``releases_access_level``, ``environments_access_level``, ``feature_flags_access_level``, ``infrastructure_access_level``, ``monitor_access_level``, and ``security_and_compliance_access_level`` options (https://github.com/ansible-collections/community.general/pull/5986).
- gitlab_project - add new option ``topics`` for adding topics to GitLab projects (https://github.com/ansible-collections/community.general/pull/6278).
- gitlab_runner - add new boolean option ``access_level_on_creation``. It controls, whether the value of ``access_level`` is used for runner registration or not. The option ``access_level`` has been ignored on registration so far and was only used on updates (https://github.com/ansible-collections/community.general/issues/5907, https://github.com/ansible-collections/community.general/pull/5908).
- gitlab_runner - allow to register group runner (https://github.com/ansible-collections/community.general/pull/3935).
- homebrew_cask - allows passing ``--greedy`` option to ``upgrade_all`` (https://github.com/ansible-collections/community.general/pull/6267).
- idrac_redfish_command - add ``job_id`` to ``CreateBiosConfigJob`` response (https://github.com/ansible-collections/community.general/issues/5603).
- ilo_redfish_utils module utils - change implementation of DNS Server IP and NTP Server IP update (https://github.com/ansible-collections/community.general/pull/5804).
- ipa_group - allow to add and remove external users with the ``external_user`` option (https://github.com/ansible-collections/community.general/pull/5897).
- ipa_hostgroup - add ``append`` parameter for adding a new hosts to existing hostgroups without changing existing hostgroup members (https://github.com/ansible-collections/community.general/pull/6203).
- iptables_state - minor refactoring within the module (https://github.com/ansible-collections/community.general/pull/5844).
- java_certs - add more detailed error output when extracting certificate from PKCS12 fails (https://github.com/ansible-collections/community.general/pull/5550).
- jc filter plugin - added the ability to use parser plugins (https://github.com/ansible-collections/community.general/pull/6043).
- jenkins_plugin - refactor code to module util to fix sanity check (https://github.com/ansible-collections/community.general/pull/5565).
- jira - add worklog functionality (https://github.com/ansible-collections/community.general/issues/6209, https://github.com/ansible-collections/community.general/pull/6210).
- keycloak_authentication - add flow type option to sub flows to allow the creation of 'form-flow' sub flows like in Keycloak's built-in registration flow (https://github.com/ansible-collections/community.general/pull/6318).
- keycloak_group - add new optional module parameter ``parents`` to properly handle keycloak subgroups (https://github.com/ansible-collections/community.general/pull/5814).
- keycloak_user_federation - make ``org.keycloak.storage.ldap.mappers.LDAPStorageMapper`` the default value for mappers ``providerType`` (https://github.com/ansible-collections/community.general/pull/5863).
- ldap modules - add ``ca_path`` option (https://github.com/ansible-collections/community.general/pull/6185).
- ldap modules - add ``xorder_discovery`` option (https://github.com/ansible-collections/community.general/issues/6045, https://github.com/ansible-collections/community.general/pull/6109).
- ldap_search - the new ``base64_attributes`` allows to specify which attribute values should be Base64 encoded (https://github.com/ansible-collections/community.general/pull/6473).
- lxd_container - add diff and check mode (https://github.com/ansible-collections/community.general/pull/5866).
- lxd_project - refactored code out to module utils to clear sanity check (https://github.com/ansible-collections/community.general/pull/5549).
- make - add ``command`` return value to the module output (https://github.com/ansible-collections/community.general/pull/6160).
- mattermost, rocketchat, slack - replace missing default favicon with docs.ansible.com favicon (https://github.com/ansible-collections/community.general/pull/5928).
- mksysb - improved the output of the module in case of errors (https://github.com/ansible-collections/community.general/issues/6263).
- modprobe - add ``persistent`` option (https://github.com/ansible-collections/community.general/issues/4028, https://github.com/ansible-collections/community.general/pull/542).
- module_helper module utils - updated the imports to make more MH features available at ``plugins/module_utils/module_helper.py`` (https://github.com/ansible-collections/community.general/pull/6464).
- mssql_script - allow for ``GO`` statement to be mixed-case for scripts not using strict syntax (https://github.com/ansible-collections/community.general/pull/6457).
- mssql_script - handle error condition for empty resultsets to allow for non-returning SQL statements (for example ``UPDATE`` and ``INSERT``) (https://github.com/ansible-collections/community.general/pull/6457).
- mssql_script - improve batching logic to allow a wider variety of input scripts. For example, SQL scripts slurped from Windows machines which may contain carriage return (''\r'') characters (https://github.com/ansible-collections/community.general/pull/6457).
- nmap inventory plugin - add new option ``open`` for only returning open ports (https://github.com/ansible-collections/community.general/pull/6200).
- nmap inventory plugin - add new option ``port`` for port specific scan (https://github.com/ansible-collections/community.general/pull/6165).
- nmap inventory plugin - add new options ``udp_scan``, ``icmp_timestamp``, and ``dns_resolve`` for different types of scans (https://github.com/ansible-collections/community.general/pull/5566).
- nmap inventory plugin - added environment variables for configure ``address`` and ``exclude`` (https://github.com/ansible-collections/community.general/issues/6351).
- nmcli - add ``default`` and ``default-or-eui64`` to the list of valid choices for ``addr_gen_mode6`` parameter (https://github.com/ansible-collections/community.general/pull/5974).
- nmcli - add ``macvlan`` connection type (https://github.com/ansible-collections/community.general/pull/6312).
- nmcli - add support for ``team.runner-fast-rate`` parameter for ``team`` connections (https://github.com/ansible-collections/community.general/issues/6065).
- nmcli - new module option ``slave_type`` added to allow creation of various types of slave devices (https://github.com/ansible-collections/community.general/issues/473, https://github.com/ansible-collections/community.general/pull/6108).
- one_vm - add a new ``updateconf`` option which implements the ``one.vm.updateconf`` API call (https://github.com/ansible-collections/community.general/pull/5812).
- openbsd_pkg - set ``TERM`` to ``'dumb'`` in ``execute_command()`` to make module less dependant on the ``TERM`` environment variable set on the Ansible controller (https://github.com/ansible-collections/community.general/pull/6149).
- opkg - allow installing a package in a certain version (https://github.com/ansible-collections/community.general/pull/5688).
- opkg - refactored module to use ``CmdRunner`` for executing ``opkg`` (https://github.com/ansible-collections/community.general/pull/5718).
- osx_defaults - include stderr in error messages (https://github.com/ansible-collections/community.general/pull/6011).
- pipx - add ``system_site_packages`` parameter to give application access to system-wide packages (https://github.com/ansible-collections/community.general/pull/6308).
- pipx - ensure ``include_injected`` parameter works with ``state=upgrade`` and ``state=latest`` (https://github.com/ansible-collections/community.general/pull/6212).
- pipx - optional ``install_apps`` parameter added to install applications from injected packages (https://github.com/ansible-collections/community.general/pull/6198).
- proxmox - added new module parameter ``tags`` for use with PVE 7+ (https://github.com/ansible-collections/community.general/pull/5714).
- proxmox - suppress urllib3 ``InsecureRequestWarnings`` when ``validate_certs`` option is ``false`` (https://github.com/ansible-collections/community.general/pull/5931).
- proxmox_kvm - add new ``archive`` parameter. This is needed to create a VM from an archive (backup) (https://github.com/ansible-collections/community.general/pull/6159).
- proxmox_kvm - adds ``migrate`` parameter to manage online migrations between hosts (https://github.com/ansible-collections/community.general/pull/6448)
- puppet - add new options ``skip_tags`` to exclude certain tagged resources during a puppet agent or apply (https://github.com/ansible-collections/community.general/pull/6293).
- puppet - refactored module to use ``CmdRunner`` for executing ``puppet`` (https://github.com/ansible-collections/community.general/pull/5612).
- rax_scaling_group - refactored out code to the ``rax`` module utils to clear the sanity check (https://github.com/ansible-collections/community.general/pull/5563).
- redfish_command - add ``PerformRequestedOperations`` command to perform any operations necessary to continue the update flow (https://github.com/ansible-collections/community.general/issues/4276).
- redfish_command - add ``update_apply_time`` to ``SimpleUpdate`` command (https://github.com/ansible-collections/community.general/issues/3910).
- redfish_command - add ``update_status`` to output of ``SimpleUpdate`` command to allow a user monitor the update in progress (https://github.com/ansible-collections/community.general/issues/4276).
- redfish_command - adding ``EnableSecureBoot`` functionality (https://github.com/ansible-collections/community.general/pull/5899).
- redfish_command - adding ``VerifyBiosAttributes`` functionality (https://github.com/ansible-collections/community.general/pull/5900).
- redfish_info - add ``GetUpdateStatus`` command to check the progress of a previous update request (https://github.com/ansible-collections/community.general/issues/4276).
- redfish_info - adds commands to retrieve the HPE ThermalConfiguration and FanPercentMinimum settings from iLO (https://github.com/ansible-collections/community.general/pull/6208).
- redfish_utils module utils - added PUT (``put_request()``) functionality (https://github.com/ansible-collections/community.general/pull/5490).
- redhat_subscription - add a ``server_proxy_scheme`` parameter to configure the scheme for the proxy server (https://github.com/ansible-collections/community.general/pull/5662).
- redhat_subscription - adds ``token`` parameter for subscription-manager authentication using Red Hat API token (https://github.com/ansible-collections/community.general/pull/5725).
- redhat_subscription - credentials (``username``, ``activationkey``, and so on) are required now only if a system needs to be registered, or ``force_register`` is specified (https://github.com/ansible-collections/community.general/pull/5664).
- redhat_subscription - the registration is done using the D-Bus ``rhsm`` service instead of spawning a ``subscription-manager register`` command, if possible; this avoids passing plain-text credentials as arguments to ``subscription-manager register``, which can be seen while that command runs (https://github.com/ansible-collections/community.general/pull/6122).
- sefcontext - add support for path substitutions (https://github.com/ansible-collections/community.general/issues/1193).
- shutdown - if no shutdown commands are found in the ``search_paths`` then the module will attempt to shutdown the system using ``systemctl shutdown`` (https://github.com/ansible-collections/community.general/issues/4269, https://github.com/ansible-collections/community.general/pull/6171).
- slack - add option ``prepend_hash`` which allows to control whether a ``#`` is prepended to ``channel_id``. The current behavior (value ``auto``) is to prepend ``#`` unless some specific prefixes are found. That list of prefixes is incomplete, and there does not seem to exist a documented condition on when exactly ``#`` must not be prepended. We recommend to explicitly set ``prepend_hash=always`` or ``prepend_hash=never`` to avoid any ambiguity (https://github.com/ansible-collections/community.general/pull/5629).
- snap - minor refactor when executing module (https://github.com/ansible-collections/community.general/pull/5773).
- snap - refactor module to use ``CmdRunner`` to execute external commands (https://github.com/ansible-collections/community.general/pull/6468).
- snap_alias - refactor code to module utils (https://github.com/ansible-collections/community.general/pull/6441).
- snap_alias - refactored module to use ``CmdRunner`` to execute ``snap`` (https://github.com/ansible-collections/community.general/pull/5486).
- spotinst_aws_elastigroup - add ``elements`` attribute when missing in ``list`` parameters (https://github.com/ansible-collections/community.general/pull/5553).
- ssh_config - add ``host_key_algorithms`` option (https://github.com/ansible-collections/community.general/pull/5605).
- ssh_config - add ``proxyjump`` option (https://github.com/ansible-collections/community.general/pull/5970).
- ssh_config - refactor code to module util to fix sanity check (https://github.com/ansible-collections/community.general/pull/5720).
- ssh_config - vendored StormSSH's config parser to avoid having to install StormSSH to use the module (https://github.com/ansible-collections/community.general/pull/6117).
- sudoers - add ``setenv`` parameters to support passing environment variables via sudo. (https://github.com/ansible-collections/community.general/pull/5883)
- sudoers - adds ``host`` parameter for setting hostname restrictions in sudoers rules (https://github.com/ansible-collections/community.general/issues/5702).
- terraform - remove state file check condition and error block, because in the native implementation of terraform will not cause errors due to the non-existent file (https://github.com/ansible-collections/community.general/pull/6296).
- udm_dns_record - minor refactor to the code (https://github.com/ansible-collections/community.general/pull/6382).
- udm_share - added ``elements`` attribute to ``list`` type parameters (https://github.com/ansible-collections/community.general/pull/5557).
- udm_user - add ``elements`` attribute when missing in ``list`` parameters (https://github.com/ansible-collections/community.general/pull/5559).
- znode module - optional ``use_tls`` parameter added for encrypted communication (https://github.com/ansible-collections/community.general/issues/6154).

community.grafana
~~~~~~~~~~~~~~~~~

- able to set `uid` for datasources in grafana via module grafana_datasource

community.hrobot
~~~~~~~~~~~~~~~~

- firewall, firewall_info - add ``filter_ipv6`` and ``rules.output`` output to support the new IPv6 filtering and output rules features (https://github.com/ansible-collections/community.hrobot/issues/75, https://github.com/ansible-collections/community.hrobot/pull/76).
- firewall, firewall_info - add ``server_number`` option that can be used instead of ``server_ip`` to identify the server. Hetzner deprecated configuring the firewall by ``server_ip``, so using ``server_ip`` will stop at some point in the future (https://github.com/ansible-collections/community.hrobot/pull/77).

community.mongodb
~~~~~~~~~~~~~~~~~

- 491 mongodb_shell - Add feature to detect if mongo or mongosh is available.
- 494 mongodb_auth - Removes module_defaults from role.
- 494 mongodb_shutdown - Fix examples block.
- 511 mongodb_auth - Adds support for deletion of users.
- 514 mongodb_linux - Remove extended FQCN for pam_limits.
- 524 mongodb_auth - Add supports for Amazon Linux 2.
- 528 multiple roles - Use first ip address when multiple bind IPs provided.
- 530 mongodb_role - Adds new module to manage MongoDB roles.
- 536 mongodb_auth - Add user after enabling authentication.
- 544 mongodb_replicaset - Module documentation improvements.
- 547 mongodb_repository - Bump default of MongoDB to 6.0.

community.mysql
~~~~~~~~~~~~~~~

- mysql module utils - change deprecated connection parameters ``passwd`` and ``db`` to ``password`` and ``database`` (https://github.com/ansible-collections/community.mysql/pull/177).
- mysql_info - add ``connector_name`` and ``connector_version`` to returned values (https://github.com/ansible-collections/community.mysql/pull/497).
- mysql_role - enable auto_commit to avoid MySQL metadata table lock (https://github.com/ansible-collections/community.mysql/issues/479).
- mysql_user - add ``MAX_STATEMENT_TIME`` support for mariadb to the ``resource_limits`` argument (https://github.com/ansible-collections/community.mysql/issues/211).
- mysql_user - add plugin_auth_string as optional parameter to use a specific pam service if pam/auth_pam plugin is used (https://github.com/ansible-collections/community.mysql/pull/445).
- mysql_user - add the ``session_vars`` argument to set session variables at the beginning of module execution (https://github.com/ansible-collections/community.mysql/issues/478).
- mysql_user - display a more informative invalid privilege exception. Changes the exception handling of the granting permission logic to show the query executed , params and the exception message granting privileges fails` (https://github.com/ansible-collections/community.mysql/issues/465).
- mysql_user - enable auto_commit to avoid MySQL metadata table lock (https://github.com/ansible-collections/community.mysql/issues/479).
- setup_mysql - update MySQL tarball URL (https://github.com/ansible-collections/community.mysql/pull/491).

community.postgresql
~~~~~~~~~~~~~~~~~~~~

- Add support for module_defaults with action_group ``all`` (https://github.com/ansible-collections/community.postgresql/pull/430).
- postgresql - added new parameters ``ssl_cert`` and ``ssl_key`` for ssl connection (https://github.com/ansible-collections/community.postgresql/issues/424).
- postgresql - when receiving the connection parameters, the ``PGPORT`` and ``PGUSER`` environment variables are checked. The order of assigning values ``environment variables`` -> ``default values`` -> ``set values`` (https://github.com/ansible-collections/community.postgresql/issues/311).
- postgresql_query - a list of queries can be passed as the ``query`` argument's value, the results will be stored in the ``query_all_results`` return value (is not deprecated anymore, as well as ``query_list``) (https://github.com/ansible-collections/community.postgresql/issues/312).

community.proxysql
~~~~~~~~~~~~~~~~~~

- roles/proxysql - add support for configuring REST API (https://github.com/ansible-collections/community.proxysql/pull/110).

community.routeros
~~~~~~~~~~~~~~~~~~

- api* modules - Add new option ``force_no_cert`` to connect with ADH ciphers (https://github.com/ansible-collections/community.routeros/pull/124).
- api_info - new parameter ``include_builtin`` which allows to include "builtin" entries that are automatically generated by ROS and cannot be modified by the user (https://github.com/ansible-collections/community.routeros/pull/130).
- api_info, api_modify - support API paths ``interface ethernet poe``, ``interface gre6``, ``interface vrrp`` and also support all previously missing fields of entries in ``ip dhcp-server`` (https://github.com/ansible-collections/community.routeros/pull/137).
- api_modify - adapt data for API paths ``ip dhcp-server network`` (https://github.com/ansible-collections/community.routeros/pull/156).
- api_modify - add support for API path ``snmp community`` (https://github.com/ansible-collections/community.routeros/pull/159).
- api_modify - add support for ``trap-interfaces`` in API path ``snmp`` (https://github.com/ansible-collections/community.routeros/pull/159).
- api_modify - add support to disable IPv6 in API paths ``ipv6 settings`` (https://github.com/ansible-collections/community.routeros/pull/158).
- api_modify - support API paths ``ip firewall layer7-protocol`` (https://github.com/ansible-collections/community.routeros/pull/153).
- api_modify, api_info - add field ``regexp`` to ``ip dns static`` (https://github.com/ansible-collections/community.routeros/issues/141).
- api_modify, api_info - support API paths - ``interface bonding``, ``interface bridge mlag``, ``ipv6 firewall mangle``, ``ipv6 nd``, ``system scheduler``, ``system script``, ``system ups`` (https://github.com/ansible-collections/community.routeros/pull/133).
- api_modify, api_info - support API paths ``caps-man access-list``, ``caps-man configuration``, ``caps-man datapath``, ``caps-man manager``, ``caps-man provisioning``, ``caps-man security`` (https://github.com/ansible-collections/community.routeros/pull/126).
- api_modify, api_info - support API paths ``interface list`` and ``interface list member`` (https://github.com/ansible-collections/community.routeros/pull/120).
- api_modify, api_info - support API paths ``interface pppoe-client``, ``interface vlan``, ``interface bridge``, ``interface bridge vlan`` (https://github.com/ansible-collections/community.routeros/pull/125).
- api_modify, api_info - support API paths ``interface wireguard``, ``interface wireguard peers`` (https://github.com/ansible-collections/community.routeros/pull/143).
- api_modify, api_info - support API paths ``ip arp``, ``ip firewall raw``, ``ipv6 firewall raw`` (https://github.com/ansible-collections/community.routeros/pull/144).
- api_modify, api_info - support API paths ``ip ipsec identity``, ``ip ipsec peer``, ``ip ipsec policy``, ``ip ipsec profile``, ``ip ipsec proposal`` (https://github.com/ansible-collections/community.routeros/pull/129).
- api_modify, api_info - support API paths ``ip route`` and ``ip route vrf`` (https://github.com/ansible-collections/community.routeros/pull/123).
- api_modify, api_info - support API paths ``ipv6 address``, ``ipv6 dhcp-server``, ``ipv6 dhcp-server option``, ``ipv6 route``, ``queue tree``, ``routing ospf area``, ``routing ospf area range``, ``routing ospf instance``, ``routing ospf interface-template``, ``routing pimsm instance``, ``routing pimsm interface-template`` (https://github.com/ansible-collections/community.routeros/pull/131).
- api_modify, api_info - support API paths ``system logging``, ``system logging action`` (https://github.com/ansible-collections/community.routeros/pull/127).
- api_modify, api_info - support field ``hw-offload`` for path ``ip firewall filter`` (https://github.com/ansible-collections/community.routeros/pull/121).
- api_modify, api_info - support fields ``address-list``, ``address-list-timeout``, ``connection-bytes``, ``connection-limit``, ``connection-mark``, ``connection-rate``, ``connection-type``, ``content``, ``disabled``, ``dscp``, ``dst-address-list``, ``dst-address-type``, ``dst-limit``, ``fragment``, ``hotspot``, ``icmp-options``, ``in-bridge-port``, ``in-bridge-port-list``, ``ingress-priority``, ``ipsec-policy``, ``ipv4-options``, ``jump-target``, ``layer7-protocol``, ``limit``, ``log``, ``log-prefix``, ``nth``, ``out-bridge-port``, ``out-bridge-port-list``, ``packet-mark``, ``packet-size``, ``per-connection-classifier``, ``port``, ``priority``, ``psd``, ``random``, ``realm``, ``routing-mark``, ``same-not-by-dst``, ``src-address``, ``src-address-list``, ``src-address-type``, ``src-mac-address``, ``src-port``, ``tcp-mss``, ``time``, ``tls-host``, ``ttl`` in ``ip firewall nat`` path (https://github.com/ansible-collections/community.routeros/pull/133).
- api_modify, api_info - support fields ``combo-mode``, ``comment``, ``fec-mode``, ``mdix-enable``, ``poe-out``, ``poe-priority``, ``poe-voltage``, ``power-cycle-interval``, ``power-cycle-ping-address``, ``power-cycle-ping-enabled``, ``power-cycle-ping-timeout`` for path ``interface ethernet`` (https://github.com/ansible-collections/community.routeros/pull/121).
- api_modify, api_info - support fields ``jump-target``, ``reject-with`` in ``ip firewall filter`` API path, field ``comment`` in ``ip firwall address-list`` API path, field ``jump-target`` in ``ip firewall mangle`` API path, field ``comment`` in ``ipv6 firewall address-list`` API path, fields ``jump-target``, ``reject-with`` in ``ipv6 firewall filter`` API path (https://github.com/ansible-collections/community.routeros/pull/133).
- api_modify, api_info - support for API fields that can be disabled and have default value at the same time, support API paths ``interface gre``, ``interface eoip`` (https://github.com/ansible-collections/community.routeros/pull/128).
- api_modify, api_info - support for fields ``blackhole``, ``pref-src``, ``routing-table``, ``suppress-hw-offload``, ``type``, ``vrf-interface`` in ``ip route`` path (https://github.com/ansible-collections/community.routeros/pull/131).
- api_modify, api_info - support paths ``system ntp client servers`` and ``system ntp server`` available in ROS7, as well as new fields ``servers``, ``mode``, and ``vrf`` for ``system ntp client`` (https://github.com/ansible-collections/community.routeros/pull/122).
- command - workaround for extra characters in stdout in RouterOS versions between 6.49 and 7.1.5 (https://github.com/ansible-collections/community.routeros/issues/62, https://github.com/ansible-collections/community.routeros/pull/161).

community.sops
~~~~~~~~~~~~~~

- Automatically install GNU Privacy Guard (GPG) in execution environments. To install Mozilla sops a manual step needs to be added to the EE definition, see the collection's documentation for details (https://github.com/ansible-collections/community.sops/pull/98).
- install role - add ``sops_github_latest_detection`` option that allows to configure which method to use for detecting the latest release on GitHub. By default (``auto``) first tries to retrieve a list of recent releases using the API, and if that fails due to rate limiting, tries to obtain the latest GitHub release from a semi-documented URL (https://github.com/ansible-collections/community.sops/pull/133).
- install role - add ``sops_github_token`` option to allow passing a GitHub token. This can for example be used to avoid rate limits when using the role in GitHub Actions (https://github.com/ansible-collections/community.sops/pull/132).
- install role - implement another method to determine the latest release on GitHub than using the GitHub API, which can make installation fail due to rate-limiting (https://github.com/ansible-collections/community.sops/pull/131).

community.vmware
~~~~~~~~~~~~~~~~

- vmware_cluster_drs - Add predictive DRS Setting (https://github.com/ansible-collections/community.vmware/pull/1542).
- vmware_guest - Add sub-option to configure virtual performance counters (https://github.com/ansible-collections/community.vmware/issues/1511).
- vmware_guest - Adding sub-options to configure CPU and memory shares (https://github.com/ansible-collections/community.vmware/issues/356).
- vmware_guest_boot_manager - Add a new parameter boot_hdd_name to specify the boot disk name(https://github.com/ansible-collections/community.vmware/pull/1543).
- vmware_guest_custom_attributes - Improve the code quality and added the return value for diff(https://github.com/ansible-collections/community.vmware/pull/1532).
- vmware_guest_disk - Add support for IDE disk add, remove or reconfigure, and change to gather same VM disk info as in vmware_guest_disk_info (https://github.com/ansible-collections/community.vmware/issues/1428).
- vmware_guest_disk - Extend return value documentation for vmware_guest_disk (https://github.com/ansible-collections/community.vmware/pull/1641)
- vmware_guest_disk_info - Move gather VM disk info function to vm_device_helper.py (https://github.com/ansible-collections/community.vmware/issues/1617)
- vmware_guest_network - Add PVRDMA network adapter type (https://github.com/ansible-collections/community.vmware/pull/1579).
- vmware_migrate_vmk - Improve error handling (https://github.com/ansible-collections/community.vmware/issues/1118).
- vmware_tag - Allow to use category names for tag management (https://github.com/ansible-collections/community.vmware/issues/1614).
- vmware_tag_manager - Improve performance of tag attachments and detachments (https://github.com/ansible-collections/community.vmware/issues/1603).
- vmware_tools - ansible_vmware_guest_uuid added for easier use of vmware_tools connection plugin with vmware_vm_inventory plugin
- vmware_vm_info - Add several parameters to skip discovering some information (https://github.com/ansible-collections/community.vmware/issues/1682)
- vmware_vm_info - Adding resource pool of the VM to result (https://github.com/ansible-collections/community.vmware/pull/1551).
- vmware_vmotion - New parameter timeout in order to allow vmotions running longer than 1 hour (https://github.com/ansible-collections/community.vmware/pulls/1629).

community.windows
~~~~~~~~~~~~~~~~~

- Raise minimum Ansible version to ``2.12`` or newer
- win_dns_record - Add parameter ``aging`` for creating non-static DNS records.
- win_dns_record - Added support for DHCID (RFC 4701) records
- win_domain_computer - Add ActiveDirectory module import
- win_domain_object_info - Add ActiveDirectory module import
- win_domain_user - Added the ``display_name`` option to set the users display name attribute
- win_psmodule - add ``force`` option to allow overwriting/updating existing module dependency only if requested
- win_pssession_configuration - Add diff mode support

community.zabbix
~~~~~~~~~~~~~~~~

- Replaced usage of deprecated apt key management in Debian based distros - See https://wiki.debian.org/DebianRepository/UseThirdParty
- Standardized tags across all roles.
- Updated all roles to default to version 6.4 for install.
- all roles - removed unused variables from defaults
- all roles - standardized testing matrix to check all supported versions and operating systems.
- all roles - temporarily disable epel repo on zabbix installation tasks
- all roles - updated documentation.
- ansible_zabbix_url_path introduced to be able to specify non-default Zabbix WebUI path, e.g. http://<FQDN>/zabbixeu
- collection now supports creating ``module_defaults`` for ``group/community.zabbix.zabbix`` (see https://github.com/ansible-collections/community.zabbix/issues/326)
- fixed ``zabbix_server`` role failure running in check_mode (see https://github.com/ansible-collections/community.zabbix/issues/804)
- httpapi plugin - updated to work with Zabbix 6.4.
- inventory plugin - switched from using zabbix-api to custom implementation adding authentication with tokens
- inventory script - re-coded to stop using zabbix-api. API tokens support added.
- web role - removed support for htpasswd
- zabbix suport for rhel 9
- zabbix_action, zabbix_authentication, zabbix_discovery_rule, zabbix_mediatype, zabbix_user, zabbix_user_directory, zabbix_usergroup - updated to work with Zabbix 6.4.
- zabbix_agent - give Zabbix Agent access to the Linux DMI table allowing system.hw.chassis info to populate.
- zabbix_agent role - Add support for SUSE Linux Enterprise Server for SAP Applications ("SLES_SAP").
- zabbix_host - add missing variants for SNMPv3 authprotocol and privprotocol introduced by Zabbix 6
- zabbix_proxy role - Add variable zabbix_proxy_dbpassword_hash_method to control whether you want postgresql user password to be hashed with md5 or want to use db default. When zabbix_proxy_dbpassword_hash_method is set to anything other than md5 then do not hash the password with md5 so you could use postgresql scram-sha-256 hashing method.
- zabbix_server role - Add variable zabbix_server_dbpassword_hash_method to control whether you want postgresql user password to be hashed with md5 or want to use db default. When zabbix_server_dbpassword_hash_method is set to anything other than md5 then do not hash the password with md5 so you could use postgresql scram-sha-256 hashing method.
- zabbix_template - add support for template tags
- zabbix_user_role module added
- zabbix_usergroup module - userdirectory, hostgroup_rights and templategroup_rights parameters added (Zabbix >= 6.2)
- zabbix_web - add support for Ubuntu 22.04 jammy
- zabbix_web role - possibility to add custom includes in apache vhost config

containers.podman
~~~~~~~~~~~~~~~~~

- Add --sdnotify option for container
- Add example unittest for container lib
- Add missed docs for modules
- Add protection for systemd files deletion
- Add unittests for Ansible Podman modules
- Check for gha updates weekly using dependabot
- Fix PEP8 issue in podman_image
- Fix building image with buildah and become
- Fix docs issues in podman_image
- Warning about improperly configured remote target
- add required argument to example
- docs - added simple extra_args example
- generate_systemd - implement --wants, --after and --requires
- podman_image - add file parameter for Containerfile location

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- redfish_firmware - This module supports timeout option.

f5networks.f5_modules
~~~~~~~~~~~~~~~~~~~~~

- bigip_device_auth_ldap - added a new parameter referrals
- bigip_device_group - added a new parameter, asm_sync to support ASM policy synchronization
- bigip_device_group - changed full_sync, auto_sync, save_on_auto_sync parameters only to set default value during creation, to work as documented.
- bigip_device_info - add data_increment parameter for better control of data gathering from API, addresses cases where large configurations were causing token timeouts during module operation
- bigip_device_info - added option for gathering info about device license.
- bigip_firewall_rule - the source and destination items can be set to `any` and port type is changed from int to str
- bigip_monitor_http - add up_interval parameter
- bigip_policy_rule - added ASM to disable_target list
- bigip_policy_rule - added host_begins_not_with_any and host_ends_not_with_any to conditions
- bigip_policy_rule - added host_contains parameter to http_host condition type
- bigip_profile_http- add hsts_preload parameter
- bigip_profile_tcp - add keep_alive_interval parameter
- bigip_ssl_certificate - added an option to prevent adding .crt extension to cert names
- bigip_ssl_key - added an option to prevent adding .key extension to key names
- bigip_ssl_key_cert - added an option to prevent adding .key and .crt extensions to key and cert names respectively
- bigip_sys_global - added gui_audit parameter to control audit log for changes through webui

google.cloud
~~~~~~~~~~~~

- GCE inventory plugin - a new option ``name_suffix``, to add a suffix to the name parameter.

hetzner.hcloud
~~~~~~~~~~~~~~

- dynamic inventory - add support changing the name of the top level group all servers are added to
- hcloud_firewall - add support for esp and gre protocols
- hcloud_image_info - Add cpu architecture field to return value.
- hcloud_image_info - Allow filtering images by cpu architecture.
- hcloud_server - Select matching image for the cpu architecture of the server type on create & rebuild.
- hcloud_server - add private_networks_info containing name and private ip in responses
- hcloud_server_info - add private_networks_info containing name and private ip in responses
- hcloud_server_type_info - Add cpu architecture field to return value.
- inventory plugin - Add cpu architecture to server variables.
- inventory plugin - Add list of all private networks to server variables.
- inventory plugin - Add new connect_with setting public_ipv6 to connect to discovered servers via public IPv6 address.
- inventory plugin - Add public IPv6 address to server variables.
- inventory plugin - Log warning instead of crashing when some servers do not work with global connect_with setting.

ibm.spectrum_virtualize
~~~~~~~~~~~~~~~~~~~~~~~

- ibm_svc_host - Added support for NVMe ROCE host.
- ibm_svc_host - Added support for modification of iSCSI host.
- ibm_svc_info - Added new options for gather_subset parameter.
- ibm_svc_manage_migraiton - Added support for volume migration across pools.
- ibm_svc_manage_portset - Added support for FC portset and rename functionality.
- ibm_svc_mdiskgrp - Added more parameters for storage pool configuration.

infoblox.nios_modules
~~~~~~~~~~~~~~~~~~~~~

- Fix to allocate ip to a_record dynamically `#163 <https://github.com/infobloxopen/infoblox-ansible/pull/163>`_
- Fix to camelcase issue for updating 'nios_network_view' name `#163 <https://github.com/infobloxopen/infoblox-ansible/pull/163>`_
- Fix to changelog yaml file with linting issues `#161 <https://github.com/infobloxopen/infoblox-ansible/pull/161>`_
- Fix to specify network_view in lookup modules to return absolute network and ip `#157 <https://github.com/infobloxopen/infoblox-ansible/pull/157>`_
- Fix to update 'nios_a_record' name with multiple ips having same name `#164 <https://github.com/infobloxopen/infoblox-ansible/pull/164>`_

inspur.ispim
~~~~~~~~~~~~

- Change the ansible-test.yml application file version.
- Change the description of the edit_bios module file_url field.
- Modify the description information of the backup module item field.
- Modify the description of the media_attach, retry_count, and retry_time_interval fields of the edit_kvm module.
- Modify the description of the secure_channel field of the edit_media_instance module.
- Modify the description of the slot and vname fields of the add_ldisk module.
- Modify the edit_ntp module example.
- Modify the edit_snmp_trap module version field description information.
- Modify the mode field description information of update_fw module.
- Modify the name field description of the user_group module.
- Modify the restore module example.
- Modify the supporting properties and description information of the edit_ncsi module edit_ncsi field.
- The edit_power_budget module adds the except_action field.

junipernetworks.junos
~~~~~~~~~~~~~~~~~~~~~

- Adding unlink option to junos package installation.
- Implement file_size as string.
- Used xmltodict to gather the sub-module chassis list and return it as a dictionary.

kubernetes.core
~~~~~~~~~~~~~~~

- Adjust k8s_user_impersonation tests to be compatible with Kubernetes 1.24 (https://github.com/ansible-collections/kubernetes.core/pull/520).
- add support for dry run with kubernetes client version >=18.20 (https://github.com/ansible-collections/kubernetes.core/pull/245).
- added ignore.txt for Ansible 2.14 devel branch.
- fixed module_defaults by removing routing hacks from runtime.yml (https://github.com/ansible-collections/kubernetes.core/pull/347).
- helm - add support for -set-file, -set-json, -set and -set-string options when running helm install (https://github.com/ansible-collections/kubernetes.core/issues/533).
- helm - add support for helm dependency update (https://github.com/ansible-collections/kubernetes.core/pull/208).
- helm - add support for post-renderer flag (https://github.com/ansible-collections/kubernetes.core/issues/30).
- helm - add support for timeout cli parameter to allow setting Helm timeout independent of wait (https://github.com/ansible-collections/kubernetes.core/issues/67).
- helm - add support for wait parameter for helm uninstall command. (https://github.com/ansible-collections/kubernetes/core/issues/33).
- helm - support repo location for helm diff (https://github.com/ansible-collections/kubernetes.core/issues/174).
- helm - when ansible is executed in check mode, return the diff between what's deployed and what will be deployed.
- helm, helm_plugin, helm_info, helm_plugin_info, kubectl - add support for in-memory kubeconfig. (https://github.com/ansible-collections/kubernetes.core/issues/492).
- helm_info - add hooks, notes and manifest as part of returned information (https://github.com/ansible-collections/kubernetes.core/pull/546).
- helm_info - add release state as a module argument (https://github.com/ansible-collections/kubernetes.core/issues/377).
- helm_info - added possibility to get all values by adding get_all_values parameter (https://github.com/ansible-collections/kubernetes.core/pull/531).
- helm_plugin - Add plugin_version parameter to the helm_plugin module (https://github.com/ansible-collections/kubernetes.core/issues/157).
- helm_plugin - Add support for helm plugin update using state=update.
- helm_repository - Ability to replace (overwrite) the repo if it already exists by forcing (https://github.com/ansible-collections/kubernetes.core/issues/491).
- helm_repository - add support for pass-credentials cli parameter (https://github.com/ansible-collections/kubernetes.core/pull/282).
- helm_repository - added support for ``host``, ``api_key``, ``validate_certs``, and ``ca_cert``.
- helm_repository - mark `pass_credentials` as no_log=True to silence false warning (https://github.com/ansible-collections/kubernetes.core/issues/412).
- helm_template - add name (NAME of release) and disable_hook as optional module arguments (https://github.com/ansible-collections/kubernetes.core/issues/313).
- helm_template - add show_only and release_namespace as module arguments (https://github.com/ansible-collections/kubernetes.core/issues/313).
- helm_template - add support for -set-file, -set-json, -set and -set-string options when running helm template (https://github.com/ansible-collections/kubernetes.core/pull/546).
- k8s - add no_proxy support to k8s* (https://github.com/ansible-collections/kubernetes.core/pull/272).
- k8s - add support for server_side_apply. (https://github.com/ansible-collections/kubernetes.core/issues/87).
- k8s - add support for user impersonation. (https://github.com/ansible-collections/kubernetes/core/issues/40).
- k8s - allow resource definition using metadata.generateName (https://github.com/ansible-collections/kubernetes.core/issues/35).
- k8s lookup plugin - Enable turbo mode via environment variable  (https://github.com/ansible-collections/kubernetes.core/issues/291).
- k8s, k8s_scale, k8s_service - add support for resource definition as manifest via. (https://github.com/ansible-collections/kubernetes.core/issues/451).
- k8s_cp - remove dependency with 'find' executable on remote pod when state=from_pod (https://github.com/ansible-collections/kubernetes.core/issues/486).
- k8s_drain - Adds ``delete_emptydir_data`` option to ``k8s_drain.delete_options`` to evict pods with an ``emptyDir`` volume attached (https://github.com/ansible-collections/kubernetes.core/pull/322).
- k8s_exec - select first container from the pod if none specified (https://github.com/ansible-collections/kubernetes.core/issues/358).
- k8s_exec - update deprecation warning for `return_code` (https://github.com/ansible-collections/kubernetes.core/issues/417).
- k8s_json_patch - minor typo fix in the example section (https://github.com/ansible-collections/kubernetes.core/issues/411).
- k8s_log - add the ``all_containers`` for retrieving all containers' logs in the pod(s).
- k8s_log - added the `previous` parameter for retrieving the previously terminated pod logs (https://github.com/ansible-collections/kubernetes.core/issues/437).
- k8s_log - added the `tail_lines` parameter to limit the number of lines to be retrieved from the end of the logs (https://github.com/ansible-collections/kubernetes.core/issues/488).
- k8s_rollback - add support for check_mode. (https://github.com/ansible-collections/kubernetes/core/issues/243).
- k8s_scale - add support for check_mode. (https://github.com/ansible-collections/kubernetes/core/issues/244).
- kubectl - wait for dd command to complete before proceeding (https://github.com/ansible-collections/kubernetes.core/pull/321).
- kubectl.py - replace distutils.spawn.find_executable with shutil.which in the kubectl connection plugin (https://github.com/ansible-collections/kubernetes.core/pull/456).

lowlydba.sqlserver
~~~~~~~~~~~~~~~~~~

- Adding a new credential module
- Fixed typo in the traceflag module's documentation. (https://github.com/lowlydba/lowlydba.sqlserver/pull/150)
- Return "RestartRequired" when a module performs changes that require an addition service restart to take effect. (https://github.com/lowlydba/lowlydba.sqlserver/pull/150/)
- Update login module documentation to indicate result will always be changed when a password is supplied. (https://github.com/lowlydba/lowlydba.sqlserver/pull/167)
- modules - all modules now document their platform and support for check mode in their attributes documentation (https://github.com/lowlydba/lowlydba.sqlserver/pull/134).

netapp.cloudmanager
~~~~~~~~~~~~~~~~~~~

- Add ``svm_name`` option in CVO for AWS, AZURE and GCP creation and update.

netapp.ontap
~~~~~~~~~~~~

- na_ontap_active_directory - REST requires ONTAP 9.12.1 or later.
- na_ontap_active_directory - add ``fqdn`` as aliases for ``domain``.
- na_ontap_aggregate - add ``name`` to modify in module output if aggregate is renamed.
- na_ontap_aggregate - add support for ``service_state`` option from ONTAP 9.11.1 or later in REST.
- na_ontap_aggregate - error if ``unmount_volumes`` set in REST, by default REST unmount volumes when trying to offline aggregate.
- na_ontap_aggregate - fix examples in documentation.
- na_ontap_aggregate - new REST only option ``tags`` added, requires ONTAP 9.13.1 or later version.
- na_ontap_aggregate - new option ``allow_flexgroups`` added.
- na_ontap_broadcast_domain - skip checking modify when ``state`` is absent.
- na_ontap_cifs - new options ``access_based_enumeration``, ``change_notify``, ``encryption``, ``home_directory``, ``oplocks``, ``show_snapshot``, ``allow_unencrypted_access``, ``namespace_caching`` and ``continuously_available`` added in REST.
- na_ontap_cifs - new options ``browsable`` and ``show_previous_versions`` added in REST.
- na_ontap_cifs - removed default value for ``unix_symlink`` as its not supported with ZAPI.
- na_ontap_cifs - updated documentation and examples for REST.
- na_ontap_cifs_local_group_member - Added REST API support to retrieve, add and remove CIFS group member.
- na_ontap_cifs_local_group_member - REST support is from ONTAP 9.10.1 or later.
- na_ontap_cifs_server - skip ``service_state`` option if not set in create.
- na_ontap_dns - ``skip_validation`` option requires 9.9.1 or later with REST and ignored for cluster DNS operations.
- na_ontap_dns - support cluster scope for modify and delete.
- na_ontap_export_policy - added ``name`` to modify in module output if export policy is renamed.
- na_ontap_file_security_permissions - updated module examples.
- na_ontap_interface - do not attempt to migrate FC interface if desired ``home_port``, ``home_node`` and ``current_port``, ``current_node`` are same.
- na_ontap_interface - error when try to migrate fc interface in REST.
- na_ontap_interface - new option ``fail_if_subnet_conflicts`` - requires REST and ONTAP 9.11.1 or later.
- na_ontap_interface - new option ``probe_port`` for Azure load balancer.
- na_ontap_interface - option ``subnet_name`` is now supported with REST with ONTAP 9.11.1 or later.
- na_ontap_ipspace - improved module fail error message in REST.
- na_ontap_iscsi - new option ``target_alias`` added in REST.
- na_ontap_license - support for NLF v2 license files.
- na_ontap_nfs - new options ``root``, ``windows`` and ``security`` added in REST.
- na_ontap_qos_policy_group - new REST only option ``adaptive_qos_options.block_size`` added, requires ONTAP 9.10.1 or later version.
- na_ontap_qos_policy_group - skip checking modify when ``state`` is absent.
- na_ontap_quotas - for qtree type, allow quota_target in path format /vol/vol_name/qtree_name in REST.
- na_ontap_rest_cli - returns changed only for verbs POST, PATCH and DELETE.
- na_ontap_rest_info - improved documentation for ``parameters`` option.
- na_ontap_s3_buckets - new option ``type`` added, requires ONTAP 9.12.1 or later.
- na_ontap_security_config - Added support for protocol version ``TLSV1.3``.
- na_ontap_security_config - Replaced private cli with REST API for GET and PATCH.
- na_ontap_security_config - new option ``supported_cipher_suites`` added in REST.
- na_ontap_security_config - updated documentation for ``supported_cipher_suites``.
- na_ontap_snapmirror - new option ``identity_preservation`` added in REST.
- na_ontap_snapmirror - support ``schedule`` with REST and ONTAP 9.11.1, add alias ``transfer_schedule``.
- na_ontap_snapmirror - wait 600 seconds for snapmirror creation to complete in REST.
- na_ontap_snapmirror_policy - Added new choices sync and async for policy type in REST.
- na_ontap_snapmirror_policy - Added unsupported options in ZAPI.
- na_ontap_snapmirror_policy - add support for cluster scoped policy with REST.
- na_ontap_snapmirror_policy - new option ``copy_all_source_snapshots`` added in REST.
- na_ontap_snapmirror_policy - new option ``copy_latest_source_snapshot``, ``create_snapshot_on_source`` and ``sync_type`` added in REST.
- na_ontap_snapmirror_policy - new option ``transfer_schedule`` for async policy types.
- na_ontap_snapmirror_policy - warn when replacing policy type ``async_mirror``, ``mirror_vault`` and ``vault`` with policy type ``async`` and ``strict_sync_mirror``, ``sync_mirror`` with ``sync`` in REST.
- na_ontap_svm - warn in case of mismatch in language option spelling.
- na_ontap_user - option ``vserver`` is not required with REST, ignore this option to create cluster scoped user.
- na_ontap_user_role - ``command_directory_name`` is required if ``privileges`` not set in REST.
- na_ontap_user_role - ``command_directory_name`` requires 9.11.1 or later with REST.
- na_ontap_user_role - ``path`` is required if ``privileges`` set in REST.
- na_ontap_user_role - add support for rest-role ``privileges.access`` choices ``read_create``, ``read_modify`` and ``read_create_modify``, supported only with REST and requires ONTAP 9.11.1 or later versions.
- na_ontap_volume - new REST only option ``tags`` added, requires ONTAP 9.13.1 or later version.
- na_ontap_volume - report error if vserver does not exist or is not a data vserver on create.
- na_ontap_volume_efficiency - REST support for ``policy`` requires 9.7 or later, ``path`` requires 9.9.1 or later and ``volume_efficiency`` and ``start_ve_scan_old_data`` requires 9.11.1 or later.
- na_ontap_volume_efficiency - ``schedule``, ``start_ve_scan_all``, ``start_ve_build_metadata``, ``start_ve_delete_checkpoint``, ``start_ve_queue_operation``, ``start_ve_qos_policy`` and ``stop_ve_all_operations`` options are not supported with REST.
- na_ontap_volume_efficiency - new option ``volume_name`` added.
- na_ontap_volume_efficiency - updated private cli with REST API.
- retry create or modify when getting temporarily locked from changes error in REST.

netapp_eseries.santricity
~~~~~~~~~~~~~~~~~~~~~~~~~

- netapp_eseries.santricity.na_santricity_iscsi_interface - Add support of iSCSI HIC speed.
- netapp_eseries.santricity.nar_santricity_host - Add support of iSCSI HIC speed.

netbox.netbox
~~~~~~~~~~~~~

- Add options for NetBox 3.4 [#905](https://github.com/netbox-community/ansible_modules/pull/905)
- nb_inventory - Add serial and asset tag to extracted attributes [#826](https://github.com/netbox-community/ansible_modules/pull/826)
- nb_inventory - Enable NetBox 3.5 support [#999](https://github.com/netbox-community/ansible_modules/pull/999)
- nb_lookup - Add 3.3 endpoints for lookup [#865](https://github.com/netbox-community/ansible_modules/pull/865)
- netbox_aggregate - Add tenant as parameter to module [#968](https://github.com/netbox-community/ansible_modules/pull/968)
- netbox_asn - Add module [#947](https://github.com/netbox-community/ansible_modules/pull/947)
- netbox_console_server and netbox_console_server_port - Add new field [#866](https://github.com/netbox-community/ansible_modules/pull/866)
- netbox_custom_field - Add group_name [#882](https://github.com/netbox-community/ansible_modules/pull/882)
- netbox_device_bay - Add label [#868](https://github.com/netbox-community/ansible_modules/pull/868)
- netbox_device_type and netbox_device - Add airflow [#907](https://github.com/netbox-community/ansible_modules/pull/907)
- netbox_fhrp_group - Add module [#957](https://github.com/netbox-community/ansible_modules/pull/957)
- netbox_fhrp_group_assignment - Add module [#974](https://github.com/netbox-community/ansible_modules/pull/974)
- netbox_invventory_item_role - Add module [#885](https://github.com/netbox-community/ansible_modules/pull/885)
- netbox_journal_entry - Add module [#961](https://github.com/netbox-community/ansible_modules/pull/961)
- netbox_l2vpn - Add module [#846](https://github.com/netbox-community/ansible_modules/pull/846)
- netbox_lsvpn_termination - Add module [#994](https://github.com/netbox-community/ansible_modules/pull/994)
- netbox_module_type - Add module [#887](https://github.com/netbox-community/ansible_modules/pull/887)
- netbox_service_template - Add module [#908](https://github.com/netbox-community/ansible_modules/pull/908)

ngine_io.cloudstack
~~~~~~~~~~~~~~~~~~~

- cs_instance - The arguments ``cpu``, ``cpu_speed`` and ``memory`` are no longer required to be set together (https://github.com/ngine-io/ansible-collection-cloudstack/issues/111).
- cs_instance - The optional arguments ``pod`` and ``cluster`` has been added.

ovirt.ovirt
~~~~~~~~~~~

- Improving "ovirt_disk" and "disaster_recovery" documentation (https://github.com/oVirt/ovirt-ansible-collection/pull/562).
- ovirt_host - Add refreshed state (https://github.com/oVirt/ovirt-ansible-collection/pull/673).
- ovirt_network - Add default_route usage to the ovirt_network module (https://github.com/oVirt/ovirt-ansible-collection/pull/647).

purestorage.flasharray
~~~~~~~~~~~~~~~~~~~~~~

- purefa_hg - Changed parameter hostgroup to name for consistency. Added hostgroup as an alias for backwards compatability.
- purefa_hg - Exit gracefully, rather than failing when a specified volume does not exist
- purefa_host - Add support for VLAN ID tagging for a host (Requires Purity//FA 6.3.5)
- purefa_host - Exit gracefully, rather than failing when a specified volume does not exist
- purefa_info - Add new subset alerts
- purefa_info - Added default protection information to `config` section
- purefa_info - Added network neighbors info to `network` subset
- purefa_network - Added support for NVMe-RoCE and NVMe-TCP service types
- purefa_network - Added support for servicelist updates
- purefa_pod - Added support for pod quotas (from REST 2.23)
- purefa_snap - New response of 'suffix' when snapshot has been created.
- purefa_user - Added Ops Admin role to choices
- purefa_vlan - Added support for NVMe-TCP service type
- purefa_vlan - Extend VLAN support to cover NVMe-RoCE and file interfaces
- purefa_volume - Added additional volume facts for volume update, or for no change
- purefa_volume - Added support for volume promotion/demotion

purestorage.flashblade
~~~~~~~~~~~~~~~~~~~~~~

- purefb_info - Added `encryption` and `support_keys` information.
- purefb_info - Added bucket quota and safemode information per bucket
- purefb_info - Added security update version for Purity//FB 4.0.2, or higher
- purefb_info - Updated object store account information
- purefb_inventory - Added `part_number` to hardware item information.
- purefb_policy - Added support for multiple rules in snapshot policies
- purefb_proxy - Added new boolean parameter `secure`. Default of true (for backwards compatability) sets the protocol to be `https://`. False sets `http://`
- purefb_s3acc - Added support for default bucket quotas and hard limits
- purefb_s3acc - Added support for object account quota and hard limit

purestorage.fusion
~~~~~~~~~~~~~~~~~~

- added Python package dependency checks in prerequisites.py
- errors_py - added opt-in global exception handler which produces simpler and cleaner messages on REST errors
- fusion_hap - added missing 'windows' personality type
- fusion_info - Added API Client information
- removed dependency on Python `netaddr` package

sensu.sensu_go
~~~~~~~~~~~~~~

- Added support for Rocky and Alma linux
- Added support for ansible 2.14

t_systems_mms.icinga_director
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Add zone to user and notification template (https://github.com/T-Systems-MMS/ansible-collection-icinga-director/pull/198)

theforeman.foreman
~~~~~~~~~~~~~~~~~~

- content_export_library, content_export_repository, content_export_version - add ``format`` option to control the export format
- content_view_filter - add support for creating modulemd filters
- content_view_publish role - also accept a list of dicts as the ``content_views`` role for publishing (https://github.com/theforeman/foreman-ansible-modules/issues/1436)
- job_template - add ``default`` option to the ``template_inputs`` parameter
- location, organization - add ``ignore_types`` parameter to adjust automatic association of resources
- redhat_manifest - Search by UUID on the server side if UUID is known. This is faster and allows fetching of manifest in big accounts (>1000 allocations).
- redhat_manifest - return the UUID of the manifest so it can be reused later
- redhat_manifest - set default ``quantity`` to 1 (https://github.com/theforeman/foreman-ansible-modules/pull/1499)
- setting - document how to obtain valid setting names (https://bugzilla.redhat.com/show_bug.cgi?id=2174367)

vmware.vmware_rest
~~~~~~~~~~~~~~~~~~

- set version in galaxy.yml to allow install from git repo

vultr.cloud
~~~~~~~~~~~

- instance - Added argument ``snapshot`` to support creation of instances via snapshot (https://github.com/vultr/ansible-collection-vultr/pull/56).
- instance - Implemented VPC support to attach/detach VPCs (https://github.com/vultr/ansible-collection-vultr/pull/46).
- inventory - Added IPv6 support by adding ``v6_main_ip`` to the attributes and improved docs (https://github.com/vultr/ansible-collection-vultr/pull/54).

Breaking Changes / Porting Guide
--------------------------------

Ansible-core
~~~~~~~~~~~~

- ansible-doc - no longer treat plugins in collections whose name starts with ``_`` as deprecated (https://github.com/ansible/ansible/pull/79362).
- ansible-test - Integration tests which depend on specific file permissions when running in an ansible-test managed host environment may require changes. Tests that require permissions other than ``755`` or ``644`` may need to be updated to set the necessary permissions as part of the test run.
- ansible-test - The ``vcenter`` test plugin now defaults to using a user-provided static configuration instead of the ``govcsim`` simulator for collections. Set the ``ANSIBLE_VCSIM_CONTAINER`` environment variable to ``govcsim`` to use the simulator. Keep in mind that the simulator is deprecated and will be removed in a future release.
- ansible-test sanity - previously plugins and modules in collections whose name started with ``_`` were treated as deprecated, even when they were not marked as deprecated in ``meta/runtime.yml``. This is no longer the case (https://github.com/ansible/ansible/pull/79362).
- ansible-test validate-modules - Removed the ``missing-python-doc`` error code in validate modules, ``missing-documentation`` is used instead for missing PowerShell module documentation.

amazon.aws
~~~~~~~~~~

- The amazon.aws collection has dropped support for ``botocore<1.25.0`` and ``boto3<1.22.0``. Most modules will continue to work with older versions of the AWS SDK, however compatibility with older versions of the SDK is not guaranteed and will not be tested. When using older versions of the SDK a warning will be emitted by Ansible (https://github.com/ansible-collections/amazon.aws/pull/1342).
- amazon.aws - compatibility code for Python < 3.6 has been removed (https://github.com/ansible-collections/amazon.aws/pull/1257).
- ec2_eip - the previously deprecated ``instance_id`` alias for the ``device_id`` parameter has been removed. Please use the ``device_id`` parameter name instead (https://github.com/ansible-collections/amazon.aws/issues/1176).
- ec2_instance - the default value for ``instance_type`` has been removed. At least one of ``instance_type`` or ``launch_template`` must be specified when launching new instances (https://github.com/ansible-collections/amazon.aws/pull/1315).
- ec2_vpc_dhcp_options - the ``new_options`` return value has been deprecated after being renamed to ``dhcp_config``.  Please use the ``dhcp_config`` or ``dhcp_options`` return values (https://github.com/ansible-collections/amazon.aws/pull/1327).
- ec2_vpc_endpoint - the ``policy_file`` parameter has been removed.  I(policy) with a file lookup can be used instead (https://github.com/ansible-collections/amazon.aws/issues/1178).
- ec2_vpc_net - the ``classic_link_enabled`` return value has been removed. Support for EC2 Classic networking was dropped by AWS (https://github.com/ansible-collections/amazon.aws/pull/1374).
- ec2_vpc_net_info - the ``classic_link_dns_status`` return value has been removed. Support for EC2 Classic networking was dropped by AWS (https://github.com/ansible-collections/amazon.aws/pull/1374).
- ec2_vpc_net_info - the ``classic_link_enabled`` return value has been removed. Support for EC2 Classic networking was dropped by AWS (https://github.com/ansible-collections/amazon.aws/pull/1374).
- module_utils.cloud - the previously deprecated ``CloudRetry.backoff`` has been removed. Please use ``CloudRetry.exponential_backoff`` or ``CloudRetry.jittered_backoff`` instead (https://github.com/ansible-collections/amazon.aws/issues/1110).

ansible.netcommon
~~~~~~~~~~~~~~~~~

- NetworkConnectionBase now inherits from PersistentConnectionBase in ansible.utils. As a result, the minimum ansible.utils version has increased to 2.7.0.
- NetworkTemplate is no longer importable from ansible_collections.ansible.netcommon.plugins.module_utils.network.common and should now be found at its proper location ansible_collections.ansible.netcommon.plugins.module_utils.network.common.rm_base.network_template
- ResourceModule is no longer importable from ansible_collections.ansible.netcommon.plugins.module_utils.network.common and should now be found at its proper location ansible_collections.ansible.netcommon.plugins.module_utils.network.common.rm_base.resource_module
- VALID_MASKS, is_masklen, is_netmask, to_bits, to_ipv6_network, to_masklen, to_netmask, and to_subnet are no longer importable from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils and should now be found at their proper location ansible.module_utils.common.network

community.aws
~~~~~~~~~~~~~

- The community.aws collection has dropped support for ``botocore<1.25.0`` and ``boto3<1.22.0``. Most modules will continue to work with older versions of the AWS SDK, however compatability with older versions of the SDK is not guaranteed and will not be tested. When using older versions of the SDK a warning will be emitted by Ansible (https://github.com/ansible-collections/community.aws/pull/1743).
- aws_ssm - the AWS SSM plugin was incorrectly prepending ``sudo`` to most commands.  This behaviour was incorrect and has been removed. To execute commands as a specific user, including the ``root`` user, the ``become`` and ``become_user`` directives should be used.  See the `Ansible documentation for more information <https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_privilege_escalation.html>`_ (https://github.com/ansible-collections/community.aws/issues/853).
- codebuild_project - ``tags`` parameter now accepts a dict representing the tags, rather than the boto3 format (https://github.com/ansible-collections/community.aws/pull/1643).

community.general
~~~~~~~~~~~~~~~~~

- If you are not using this collection as part of Ansible, but installed (and/or upgraded) community.general manually, you need to make sure to also install ``community.sap_libs`` if you are using any of the ``sapcar_extract``, ``sap_task_list_execute``, and ``hana_query`` modules.
  Without that collection installed, the redirects for these modules do not work.
- ModuleHelper module utils - when the module sets output variables named ``msg``, ``exception``, ``output``, ``vars``, or ``changed``, the actual output will prefix those names with ``_`` (underscore symbol) only when they clash with output variables generated by ModuleHelper itself, which only occurs when handling exceptions. Please note that this breaking change does not require a new major release since before this release, it was not possible to add such variables to the output `due to a bug <https://github.com/ansible-collections/community.general/pull/5755>`__ (https://github.com/ansible-collections/community.general/pull/5765).
- gconftool2 - fix processing of ``gconftool-2`` when ``key`` does not exist, returning ``null`` instead of empty string for both ``value`` and ``previous_value`` return values (https://github.com/ansible-collections/community.general/issues/6028).
- gitlab_runner - the default of ``access_level_on_creation`` changed from ``false`` to ``true`` (https://github.com/ansible-collections/community.general/pull/6428).
- ldap_search - convert all string-like values to UTF-8 (https://github.com/ansible-collections/community.general/issues/5704, https://github.com/ansible-collections/community.general/pull/6473).
- nmcli - the default of the ``hairpin`` option changed from ``true`` to ``false`` (https://github.com/ansible-collections/community.general/pull/6428).
- proxmox - the default of the ``unprivileged`` option changed from ``false`` to ``true`` (https://github.com/ansible-collections/community.general/pull/6428).

community.hashi_vault
~~~~~~~~~~~~~~~~~~~~~

- Support for ``ansible-core`` 2.11 and 2.12 has been removed (https://github.com/ansible-collections/community.hashi_vault/issues/340).
- The minimum version of ``hvac`` for ``community.hashi_vault`` is now ``1.1.0`` (https://github.com/ansible-collections/community.hashi_vault/issues/324).
- hashi_vault lookup - duplicate option entries in the term string now raises an exception instead of a warning (https://github.com/ansible-collections/community.hashi_vault/issues/356).

community.zabbix
~~~~~~~~~~~~~~~~

- agent role - removed support for Darwin, Amazon, Fedora, XCP-ng, Suse, Mint, and Sangoma operating systems
- agent role - removed support for zabbix_create_host and replaced it with zabbix_agent_host_state
- agent role - removed support for zabbix_create_hostgroup and replaced it with zabbix_agent_hostgroups_state
- agent role - removed support for zabbix_http_password, zabbix_api_http_password, zabbix_api_pass, and zabbix_api_login_pass and replaced it with zabbix_api_login_pass
- agent role - removed support for zabbix_http_user, zabbix_api_http_user, zabbix_api_user, and zabbix_api_login_user and replaced it with zabbix_api_login_user
- agent role - removed support for zabbix_inventory_mode and replaced it with zabbix_agent_inventory_mode
- agent role - removed support for zabbix_link_templates adn replaced it with zabbix_agent_link_templates
- agent role - removed support for zabbix_macros and replaced it with zabbix_agent_macros
- agent role - removed support for zabbix_proxy and replaced it with zabbix_agent_proxy
- agent role - removed support for zabbix_update_host and replaced it with zabbix_agent_host_update
- all modules - dropped support of Zabbix versions < 6.0
- all roles  - removed support for the zabbix_version variable.
- all roles - removed support for all versions of Zabbix < 6.0.
- all roles - removed support for installation from epel and non-standard repositories
- dropped support of zabbix-api to make REST API calls to Zabbix
- proxy role - removed support for zabbix_database_creation  and replaced it with zabbix_proxy_database_creation
- proxy role - removed support for zabbix_database_sqlload  and replaced it with zabbix_proxy_database_sqlload
- proxy role - removed support for zabbix_selinux  and replaced it with zabbix_proxy_selinux
- server role - removed support for zabbix_server_mysql_login_password and replaced with zabbix_server_dbpassword
- server role - removed support for zabbix_server_mysql_login_user and replaced with zabbix_server_dbuser
- stopped supporting Ansible < 2.12
- stopped supporting Python < 3.9
- zabbix_action - message parameter renamed to op_message
- zabbix_group_facts module - removed in favour of zabbix_group_info
- zabbix_host_facts module - removed in favour of zabbix_host_info

hetzner.hcloud
~~~~~~~~~~~~~~

- inventory plugin - Python v3.5+ is now required.

lowlydba.sqlserver
~~~~~~~~~~~~~~~~~~

- Updating minimum DBATools version to v2.0.0 to allow for pwsh 7.3+ compatibility. There may also be breaking change behavior in DBATools, see https://blog.netnerds.net/2023/03/whats-new-dbatools-2.0/. (https://github.com/lowlydba/lowlydba.sqlserver/pull/181)

Deprecated Features
-------------------

- The cisco.nso collection is considered unmaintained and will be removed from Ansible 9 if no one starts maintaining it again before Ansible 9. See `the removal process for details on how this works <https://github.com/ansible-collections/overview/blob/main/removal_from_ansible.rst#cancelling-removal-of-an-unmaintained-collection>`__ (https://github.com/ansible-community/community-topics/issues/155).
- The community.fortios collection is considered unmaintained and will be removed from Ansible 9 if no one starts maintaining it again before Ansible 9. See `the removal process for details on how this works <https://github.com/ansible-collections/overview/blob/main/removal_from_ansible.rst#cancelling-removal-of-an-unmaintained-collection>`__ (https://github.com/ansible-community/community-topics/issues/162).
- The community.google collection is considered unmaintained and will be removed from Ansible 9 if no one starts maintaining it again before Ansible 9. See `the removal process for details on how this works <https://github.com/ansible-collections/overview/blob/main/removal_from_ansible.rst#cancelling-removal-of-an-unmaintained-collection>`__ (https://github.com/ansible-community/community-topics/issues/160).
- The community.skydive collection is considered unmaintained and will be removed from Ansible 9 if no one starts maintaining it again before Ansible 9. See `the removal process for details on how this works <https://github.com/ansible-collections/overview/blob/main/removal_from_ansible.rst#cancelling-removal-of-an-unmaintained-collection>`__ (https://github.com/ansible-community/community-topics/issues/171).
- The netapp.aws collection is considered unmaintained and will be removed from Ansible 10 if no one starts maintaining it again before Ansible 10. See `the removal process for details on how this works <https://github.com/ansible-collections/overview/blob/main/removal_from_ansible.rst#cancelling-removal-of-an-unmaintained-collection>`__ (https://github.com/ansible-community/community-topics/issues/223).

Ansible-core
~~~~~~~~~~~~

- The ``ConnectionBase()._new_stdin`` attribute is deprecated, use ``display.prompt_until(msg)`` instead.
- ansible-test - The ``foreman`` test plugin is now deprecated. It will be removed in a future release.
- ansible-test - The ``govcsim`` simulator in the ``vcenter`` test plugin is now deprecated. It will be removed in a future release. Users should switch to providing their own test environment through a static configuration file.
- password_hash - deprecate using passlib.hash.hashtype if hashtype isn't in the list of documented choices.
- vars - Specifying a list of dictionaries for ``vars:`` is deprecated in favor of specifying a dictionary.

amazon.aws
~~~~~~~~~~

- amazon.aws collection - due to the AWS SDKs Python support policies (https://aws.amazon.com/blogs/developer/python-support-policy-updates-for-aws-sdks-and-tools/) support for Python less than 3.8 by this collection is expected to be removed in a release after 2024-12-01 (https://github.com/ansible-collections/amazon.aws/pull/1342).
- amazon.aws collection - due to the AWS SDKs announcing the end of support for Python less than 3.7 (https://aws.amazon.com/blogs/developer/python-support-policy-updates-for-aws-sdks-and-tools/) support for Python less than 3.7 by this collection has been deprecated and will be removed in release 7.0.0. (https://github.com/ansible-collections/amazon.aws/pull/1342).
- amazon.aws lookup plugins - the ``boto3_profile`` alias for the ``profile`` option has been deprecated, please use ``profile`` instead (https://github.com/ansible-collections/amazon.aws/pull/1225).
- docs_fragments - ``amazon.aws.aws_credentials`` docs fragment has been deprecated please use ``amazon.aws.common.plugins`` instead (https://github.com/ansible-collections/amazon.aws/pull/1248).
- docs_fragments - ``amazon.aws.aws_region`` docs fragment has been deprecated please use ``amazon.aws.region.plugins`` instead (https://github.com/ansible-collections/amazon.aws/pull/1248).
- docs_fragments - ``amazon.aws.aws`` docs fragment has been deprecated please use ``amazon.aws.common.modules`` instead (https://github.com/ansible-collections/amazon.aws/pull/1248).
- docs_fragments - ``amazon.aws.ec2`` docs fragment has been deprecated please use ``amazon.aws.region.modules`` instead (https://github.com/ansible-collections/amazon.aws/pull/1248).
- module_utils.policy - ``ansible_collections.amazon.aws.module_utils.policy.sort_json_policy_dict`` has been deprecated consider using ``ansible_collections.amazon.aws.module_utils.poilcies.compare_policies`` instead (https://github.com/ansible-collections/amazon.aws/pull/1136).
- s3_object - Support for passing ``dualstack`` and ``endpoint_url`` at the same time has been deprecated, the ``dualstack`` parameter is ignored when ``endpoint_url`` is passed. Support will be removed in a release after 2024-12-01 (https://github.com/ansible-collections/amazon.aws/pull/1305).
- s3_object - Support for passing values of ``overwrite`` other than ``always``, ``never``, ``different`` or last ``last`` has been deprecated.  Boolean values should be replaced by the strings ``always`` or ``never`` Support will be removed in a release after 2024-12-01 (https://github.com/ansible-collections/amazon.aws/pull/1305).
- s3_object_info - Support for passing ``dualstack`` and ``endpoint_url`` at the same time has been deprecated, the ``dualstack`` parameter is ignored when ``endpoint_url`` is passed. Support will be removed in a release after 2024-12-01 (https://github.com/ansible-collections/amazon.aws/pull/1305).
- support for passing both profile and security tokens through a mix of environment variables and parameters has been deprecated and support will be removed in release 6.0.0. After release 6.0.0 it will only be possible to pass either a profile or security tokens, regardless of mechanism used to pass them.  To explicitly block a parameter coming from an environment variable pass an empty string as the parameter value.  Support for passing profile and security tokens together was originally deprecated in release 1.2.0, however only partially implemented in release 5.0.0 (https://github.com/ansible-collections/amazon.aws/pull/1355).

check_point.mgmt
~~~~~~~~~~~~~~~~

- add/set/delete nat-rule modules - will be replaced by the single cp_mgmt_nat_rule module.
- cp_mgmt_show_task/s modules - will be replaced by the by the single cp_mgmt_task_facts module.

chocolatey.chocolatey
~~~~~~~~~~~~~~~~~~~~~

- win_chocolatey - Deprecate side-by-side installs.

cisco.ios
~~~~~~~~~

- ios_bgp_address_family - deprecate neighbors.address/tag/ipv6_adddress with neighbor_address which enables common attributes for facts rendering
- ios_bgp_address_family - deprecate neighbors.password with password_options which allows encryption and password
- ios_bgp_address_family - deprecate redistribute.ospf.match.external with redistribute.ospf.match.externals which enables attributes for OSPF type E1 and E2 routes
- ios_bgp_address_family - deprecate redistribute.ospf.match.nssa_external with redistribute.ospf.match.nssa_externals which enables attributes for OSPF type N1 and N2 routes
- ios_bgp_address_family - deprecate redistribute.ospf.match.type_1 with redistribute.ospf.match.nssa_externals.type_1
- ios_bgp_address_family - deprecate redistribute.ospf.match.type_2 with redistribute.ospf.match.nssa_externals.type_2
- ios_bgp_address_family - deprecate slow_peer with slow_peer_options which supports a dict attribute

community.aws
~~~~~~~~~~~~~

- community.aws collection - due to the AWS SDKs Python support policies (https://aws.amazon.com/blogs/developer/python-support-policy-updates-for-aws-sdks-and-tools/) support for Python less than 3.8 by this collection is expected to be removed in a release after 2024-12-01 (https://github.com/ansible-collections/community.aws/pull/1743).
- community.aws collection - due to the AWS SDKs announcing the end of support for Python less than 3.7 (https://aws.amazon.com/blogs/developer/python-support-policy-updates-for-aws-sdks-and-tools/) support for Python less than 3.7 by this collection has been deprecated and will be removed in release 7.0.0. (https://github.com/ansible-collections/community.aws/pull/1743).
- ecs_service -  In a release after 2024-06-01, tha default value of ``purge_placement_constraints`` will be change from ``false`` to ``true`` (https://github.com/ansible-collections/community.aws/pull/1716).
- ecs_service -  In a release after 2024-06-01, tha default value of ``purge_placement_strategy`` will be change from ``false`` to ``true`` (https://github.com/ansible-collections/community.aws/pull/1716).
- iam_role - All top level return values other than ``iam_role`` and ``changed`` have been deprecated and will be removed in a release after 2023-12-01 (https://github.com/ansible-collections/community.aws/issues/551).
- iam_role - In a release after 2023-12-01 the contents of ``assume_role_policy_document`` will no longer be converted from CamelCase to snake_case.  The ``assume_role_policy_document_raw`` return value already returns the policy document in this future format (https://github.com/ansible-collections/community.aws/issues/551).
- iam_role_info - In a release after 2023-12-01 the contents of ``assume_role_policy_document`` will no longer be converted from CamelCase to snake_case.  The ``assume_role_policy_document_raw`` return value already returns the policy document in this future format (https://github.com/ansible-collections/community.aws/issues/551).

community.crypto
~~~~~~~~~~~~~~~~

- x509_crl - the ``mode`` option is deprecated; use ``crl_mode`` instead. The ``mode`` option will change its meaning in community.crypto 3.0.0, and will refer to the CRL file's mode instead (https://github.com/ansible-collections/community.crypto/issues/596).

community.dns
~~~~~~~~~~~~~

- The default of the newly added option ``txt_character_encoding`` will change from ``octal`` to ``decimal`` in community.dns 3.0.0. The new default will be compatible with `RFC 1035 <https://www.ietf.org/rfc/rfc1035.txt>`__ (https://github.com/ansible-collections/community.dns/pull/134).

community.general
~~~~~~~~~~~~~~~~~

- ModuleHelper module_utils - ``deps`` mixin for MH classes deprecated in favour of using the ``deps`` module_utils (https://github.com/ansible-collections/community.general/pull/6465).
- consul - deprecate using parameters unused for ``state=absent`` (https://github.com/ansible-collections/community.general/pull/5772).
- gitlab_runner - the default of the new option ``access_level_on_creation`` will change from ``false`` to ``true`` in community.general 7.0.0. This will cause ``access_level`` to be used during runner registration as well, and not only during updates (https://github.com/ansible-collections/community.general/pull/5908).
- gitlab_runner - the option ``access_level`` will lose its default value in community.general 8.0.0. From that version on, you have set this option to ``ref_protected`` explicitly, if you want to have a protected runner (https://github.com/ansible-collections/community.general/issues/5925).
- manageiq_policies - deprecate ``state=list`` in favour of using ``community.general.manageiq_policies_info`` (https://github.com/ansible-collections/community.general/pull/5721).
- manageiq_tags - deprecate ``state=list`` in favour of using ``community.general.manageiq_tags_info`` (https://github.com/ansible-collections/community.general/pull/5727).
- rax - module relies on deprecated library ``pyrax`` and will be removed in community.general 9.0.0 (https://github.com/ansible-collections/community.general/pull/5752).
- rax module utils - module utils code relies on deprecated library ``pyrax`` and will be removed in community.general 9.0.0 (https://github.com/ansible-collections/community.general/pull/5752).
- rax_cbs - module relies on deprecated library ``pyrax`` and will be removed in community.general 9.0.0 (https://github.com/ansible-collections/community.general/pull/5752).
- rax_cbs_attachments - module relies on deprecated library ``pyrax`` and will be removed in community.general 9.0.0 (https://github.com/ansible-collections/community.general/pull/5752).
- rax_cdb - module relies on deprecated library ``pyrax`` and will be removed in community.general 9.0.0 (https://github.com/ansible-collections/community.general/pull/5752).
- rax_cdb_database - module relies on deprecated library ``pyrax`` and will be removed in community.general 9.0.0 (https://github.com/ansible-collections/community.general/pull/5752).
- rax_cdb_user - module relies on deprecated library ``pyrax`` and will be removed in community.general 9.0.0 (https://github.com/ansible-collections/community.general/pull/5752).
- rax_clb - module relies on deprecated library ``pyrax`` and will be removed in community.general 9.0.0 (https://github.com/ansible-collections/community.general/pull/5752).
- rax_clb_nodes - module relies on deprecated library ``pyrax`` and will be removed in community.general 9.0.0 (https://github.com/ansible-collections/community.general/pull/5752).
- rax_clb_ssl - module relies on deprecated library ``pyrax`` and will be removed in community.general 9.0.0 (https://github.com/ansible-collections/community.general/pull/5752).
- rax_dns - module relies on deprecated library ``pyrax`` and will be removed in community.general 9.0.0 (https://github.com/ansible-collections/community.general/pull/5752).
- rax_dns_record - module relies on deprecated library ``pyrax`` and will be removed in community.general 9.0.0 (https://github.com/ansible-collections/community.general/pull/5752).
- rax_facts - module relies on deprecated library ``pyrax`` and will be removed in community.general 9.0.0 (https://github.com/ansible-collections/community.general/pull/5752).
- rax_files - module relies on deprecated library ``pyrax`` and will be removed in community.general 9.0.0 (https://github.com/ansible-collections/community.general/pull/5752).
- rax_files_objects - module relies on deprecated library ``pyrax`` and will be removed in community.general 9.0.0 (https://github.com/ansible-collections/community.general/pull/5752).
- rax_identity - module relies on deprecated library ``pyrax`` and will be removed in community.general 9.0.0 (https://github.com/ansible-collections/community.general/pull/5752).
- rax_keypair - module relies on deprecated library ``pyrax`` and will be removed in community.general 9.0.0 (https://github.com/ansible-collections/community.general/pull/5752).
- rax_meta - module relies on deprecated library ``pyrax`` and will be removed in community.general 9.0.0 (https://github.com/ansible-collections/community.general/pull/5752).
- rax_mon_alarm - module relies on deprecated library ``pyrax`` and will be removed in community.general 9.0.0 (https://github.com/ansible-collections/community.general/pull/5752).
- rax_mon_check - module relies on deprecated library ``pyrax`` and will be removed in community.general 9.0.0 (https://github.com/ansible-collections/community.general/pull/5752).
- rax_mon_entity - module relies on deprecated library ``pyrax`` and will be removed in community.general 9.0.0 (https://github.com/ansible-collections/community.general/pull/5752).
- rax_mon_notification - module relies on deprecated library ``pyrax`` and will be removed in community.general 9.0.0 (https://github.com/ansible-collections/community.general/pull/5752).
- rax_mon_notification_plan - module relies on deprecated library ``pyrax`` and will be removed in community.general 9.0.0 (https://github.com/ansible-collections/community.general/pull/5752).
- rax_network - module relies on deprecated library ``pyrax`` and will be removed in community.general 9.0.0 (https://github.com/ansible-collections/community.general/pull/5752).
- rax_queue - module relies on deprecated library ``pyrax`` and will be removed in community.general 9.0.0 (https://github.com/ansible-collections/community.general/pull/5752).
- rax_scaling_group - module relies on deprecated library ``pyrax`` and will be removed in community.general 9.0.0 (https://github.com/ansible-collections/community.general/pull/5752).
- rax_scaling_policy - module relies on deprecated library ``pyrax`` and will be removed in community.general 9.0.0 (https://github.com/ansible-collections/community.general/pull/5752).
- rhn_channel, rhn_register - RHN hosted at redhat.com was discontinued years
  ago, and Spacewalk 5 (which uses RHN) is EOL since 2020, May 31st;
  while these modules could work on Uyuni / SUSE Manager (fork of Spacewalk 5),
  we have not heard about anyone using them in those setups. Hence, these
  modules are deprecated, and will be removed in community.general 10.0.0
  in case there are no reports about being still useful, and potentially
  no one that steps up to maintain them
  (https://github.com/ansible-collections/community.general/pull/6493).

community.hashi_vault
~~~~~~~~~~~~~~~~~~~~~

- ansible-core - support for ``ansible-core`` versions ``2.11`` and ``2.12`` will be dropped in collection version ``5.0.0``, making ``2.13`` the minimum supported version of ``ansible-core`` (https://github.com/ansible-collections/community.hashi_vault/issues/340).
- hashi_vault lookup - in ``v5.0.0`` duplicate term string options will raise an exception instead of showing a warning (https://github.com/ansible-collections/community.hashi_vault/issues/356).
- hvac - the minimum version of ``hvac`` to be supported in collection version ``5.0.0`` will be at least ``1.0.2``; this minimum may be raised before ``5.0.0`` is released, so please subscribe to the linked issue and look out for new notices in the changelog (https://github.com/ansible-collections/community.hashi_vault/issues/324).

purestorage.fusion
~~~~~~~~~~~~~~~~~~

- fusion_hw - hardware module is being removed as changing hardware type has never been supported by Pure Storage Fusion
- fusion_info - nigs subset is deprecated in favor of network_interface_groups and will be removed in the version 1.7.0
- fusion_info - placements subset is deprecated in favor of placement_groups and will be removed in the version 1.7.0
- fusion_pg - placement_engine option is deprecated because Fusion API does not longer support this parameter It will be removed in the version 2.0.0
- fusion_se - parameters 'addresses', 'gateway' and 'network_interface_groups' are deprecated in favor of 'iscsi' and will be removed in version 2.0.0
- fusion_tn - tenant networks are being replaced by storage endpoints ```fusion_se``` and Network Interface Groups ```fusion_nig```

Removed Features (previously deprecated)
----------------------------------------

- ``dellemc.os10`` was considered unmaintained and removed from Ansible 8 as per the `removal from Ansible process <https://github.com/ansible-collections/overview/blob/main/removal_from_ansible.rst#unmaintained-collections>`_. Users can still install this collection with ``ansible-galaxy collection install dellemc.os10``.
- ``dellemc.os6`` was considered unmaintained and removed from Ansible 8 as per the `removal from Ansible process <https://github.com/ansible-collections/overview/blob/main/removal_from_ansible.rst#unmaintained-collections>`_. Users can still install this collection with ``ansible-galaxy collection install dellemc.os6``.
- ``dellemc.os9`` was considered unmaintained and removed from Ansible 8 as per the `removal from Ansible process <https://github.com/ansible-collections/overview/blob/main/removal_from_ansible.rst#unmaintained-collections>`_. Users can still install this collection with ``ansible-galaxy collection install dellemc.os9``.
- ``mellanox.onyx`` was considered unmaintained and removed from Ansible 8 as per the `removal from Ansible process <https://github.com/ansible-collections/overview/blob/main/removal_from_ansible.rst#unmaintained-collections>`_. Users can still install this collection with ``ansible-galaxy collection install mellanox.onyx``.

Ansible-core
~~~~~~~~~~~~

- Remove deprecated ``ANSIBLE_CALLBACK_WHITELIST`` configuration environment variable, use ``ANSIBLE_CALLBACKS_ENABLED`` instead. (https://github.com/ansible/ansible/issues/78821)
- Remove deprecated ``ANSIBLE_COW_WHITELIST`` configuration environment variable, use ``ANSIBLE_COW_ACCEPTLIST`` instead. (https://github.com/ansible/ansible/issues/78819)
- Remove deprecated ``callback_whitelist`` configuration option, use ``callbacks_enabled`` instead. (https://github.com/ansible/ansible/issues/78822)
- Remove deprecated ``cow_whitelist`` configuration option, use ``cowsay_enabled_stencils`` instead. (https://github.com/ansible/ansible/issues/78820)

amazon.aws
~~~~~~~~~~

- ec2_vpc_endpoint_info - support for the ``query`` parameter was removed. The ``amazon.aws.ec2_vpc_endpoint_info`` module now only queries for endpoints. Services can be queried using the ``amazon.aws.ec2_vpc_endpoint_service_info`` module (https://github.com/ansible-collections/amazon.aws/pull/1308).
- s3_object - support for creating and deleting buckets using the ``s3_object`` module has been removed. S3 buckets can be created and deleted using the ``amazon.aws.s3_bucket`` module (https://github.com/ansible-collections/amazon.aws/issues/1112).

ansible.netcommon
~~~~~~~~~~~~~~~~~

- cli_parse - This plugin was moved to ansible.utils in version 1.0.0, and the redirect to that collection has now been removed.

community.general
~~~~~~~~~~~~~~~~~

- All ``sap`` modules have been removed from this collection.
  They have been migrated to the `community.sap_libs <https://galaxy.ansible.com/community/sap_libs>`_ collection.
  Redirections have been provided.
  Following modules are affected:
  - sapcar_extract
  - sap_task_list_execute
  - hana_query
- cmd_runner module utils - the ``fmt`` alias of ``cmd_runner_fmt`` has been removed. Use ``cmd_runner_fmt`` instead (https://github.com/ansible-collections/community.general/pull/6428).
- newrelic_deployment - the ``appname`` and ``environment`` options have been removed. They did not do anything (https://github.com/ansible-collections/community.general/pull/6428).
- puppet - the alias ``show-diff`` of the ``show_diff`` option has been removed. Use ``show_diff`` instead (https://github.com/ansible-collections/community.general/pull/6428).
- xfconf - generating facts was deprecated in community.general 3.0.0, however three factoids, ``property``, ``channel`` and ``value`` continued to be generated by mistake. This behaviour has been removed and ``xfconf`` generate no facts whatsoever (https://github.com/ansible-collections/community.general/pull/5502).
- xfconf - generating facts was deprecated in community.general 3.0.0, however two factoids, ``previous_value`` and ``type`` continued to be generated by mistake. This behaviour has been removed and ``xfconf`` generate no facts whatsoever (https://github.com/ansible-collections/community.general/pull/5502).

community.zabbix
~~~~~~~~~~~~~~~~

- agent role - removed support to configure firewall
- web role - removed installation of apache, debian, and php

Bugfixes
--------

Ansible-core
~~~~~~~~~~~~

- Ansible.Basic.cs - Ignore compiler warning (reported as an error) when running under PowerShell 7.3.x.
- AnsibleModule.run_command - Only use selectors when needed, and rely on Python stdlib subprocess for the simple task of collecting stdout/stderr when prompt matching is not required.
- BSD network facts - Do not assume column indexes, look for ``netmask`` and ``broadcast`` for determining the correct columns when parsing ``inet`` line (https://github.com/ansible/ansible/issues/79117)
- Correctly count rescued tasks in play recap (https://github.com/ansible/ansible/issues/79711)
- Display - Defensively configure writing to stdout and stderr with a custom encoding error handler that will replace invalid characters while providing a deprecation warning that non-utf8 text will result in an error in a future version.
- Do not crash when templating an expression with a test or filter that is not a valid Ansible filter name (https://github.com/ansible/ansible/issues/78912, https://github.com/ansible/ansible/pull/78913).
- Fix ``MANIFEST.in`` to exclude unwanted files in the ``packaging/`` directory.
- Fix ``MANIFEST.in`` to include ``*.md`` files in the ``test/support/`` directory.
- Fix a traceback occuring when a task is named ``meta`` (https://github.com/ansible/ansible/issues/79459)
- Fix an issue where the value of ``become`` was ignored when used on a role used as a dependency in ``main/meta.yml`` (https://github.com/ansible/ansible/issues/79777)
- Fix bug in `vars` applied to roles, they were being incorrectly exported among others while only vars/main.yml was meant to be. Also adjusted the precedence to act the same as inline params.
- Fix conditionally notifying ``include_tasks` handlers when ``force_handlers`` is used (https://github.com/ansible/ansible/issues/79776)
- Fix post-validating looped task fields so the strategy uses the correct values after task execution.
- Fix reusing a connection in a task loop that uses a redirected or aliased name - https://github.com/ansible/ansible/issues/78425
- Fix setting become activation in a task loop - https://github.com/ansible/ansible/issues/78425
- Fix traceback when using the ``template`` module and running with ``ANSIBLE_DEBUG=1`` (https://github.com/ansible/ansible/issues/79763)
- Fix using ``GALAXY_IGNORE_CERTS`` in conjunction with collections in requirements files which specify a specific ``source`` that isn't in the configured servers.
- Fix using ``GALAXY_IGNORE_CERTS`` when downloading tarballs from Galaxy servers (https://github.com/ansible/ansible/issues/79557).
- Fixes leftover _valid_attrs usage.
- Fixes the password lookup to not rewrite files if they are not changed when using the "encrypt" parameter (#79430).
- Module and role argument validation - include the valid suboption choices in the error when an invalid suboption is provided.
- Perform type check on data passed to Display.display to enforce the requirement of being given a python3 unicode string
- Prevent running same handler multiple times when included via ``include_role`` (https://github.com/ansible/ansible/issues/73643)
- TaskExecutor - don't ignore templated _raw_params that k=v parser failed to parse (https://github.com/ansible/ansible/issues/79862)
- Windows - Display a warning if the module failed to cleanup any temporary files rather than failing the task. The warning contains a brief description of what failed to be deleted.
- Windows - Ensure the module temp directory contains more unique values to avoid conflicts with concurrent runs - https://github.com/ansible/ansible/issues/80294
- Windows - Improve temporary file cleanup used by modules. Will use a more reliable delete operation on Windows Server 2016 and newer to delete files that might still be open by other software like Anti Virus scanners. There are still scenarios where a file or directory cannot be deleted but the new method should work in more scenarios.
- ``ansible-galaxy search rolename`` - give a warning instead of non-zero return code when search results are empty. This is similar to the behavior when listing roles, which gives a warning if a role cannot be found and exits with a return code of ``0``.
- ``ansible_eval_concat`` - avoid redundant unsafe wrapping of templated strings converted to Python types
- ``pkg_mgr`` - fix the default dnf version detection
- ansible-config limit shorthand format to assigned values
- ansible-doc - stop generating wrong module URLs for module see-alsos. The URLs for modules in ansible.builtin do now work, and URLs for modules outside ansible.builtin are no longer added (https://github.com/ansible/ansible/pull/80280).
- ansible-doc now will correctly display short descriptions on listing filters/tests no matter the directory sorting.
- ansible-galaxy - Improve retries for collection installs, to properly retry, and extend retry logic to common URL related connection errors (https://github.com/ansible/ansible/issues/80170 https://github.com/ansible/ansible/issues/80174)
- ansible-galaxy - fix installing collections from directories that have a trailing path separator (https://github.com/ansible/ansible/issues/77803).
- ansible-galaxy - fix installing collections in git repositories/directories which contain a MANIFEST.json file (https://github.com/ansible/ansible/issues/79796).
- ansible-galaxy - fix installing signed collections (https://github.com/ansible/ansible/issues/80648).
- ansible-galaxy - make initial call to Galaxy server on-demand only when installing, getting info about, and listing roles.
- ansible-galaxy - reduce API calls to servers by fetching signatures only for final candidates.
- ansible-galaxy collection install - respect symlinks when installing from source or local repository (https://github.com/ansible/ansible/issues/78442)
- ansible-galaxy collection verify - fix verifying signed collections when the keyring is not configured.
- ansible-galaxy collection/role init - preserve symlinks (https://github.com/ansible/ansible/issues/39334).
- ansible-galaxy role info - fix unhandled AttributeError by catching the correct exception.
- ansible-inventory will no longer duplicate host entries if they were part of a group's childrens tree.
- ansible-inventory will not explicitly sort groups/hosts anymore, giving a chance (depending on output format) to match the order in the input sources.
- ansible-playbook -K breaks when passwords have quotes (https://github.com/ansible/ansible/issues/79836).
- ansible-test - Add ``wheel < 0.38.0`` constraint for Python 3.6 and earlier.
- ansible-test - Add support for ``argcomplete`` version 3.
- ansible-test - Add support for ``pytest`` assertion rewriting when running unit tests on Python 3.5 and later. Resolves issue https://github.com/ansible/ansible/issues/68032
- ansible-test - Added a work-around for a traceback under Python 3.11 when completing certain command line options.
- ansible-test - Allow disabled, unsupported, unstable and destructive integration test targets to be selected using their respective prefixes.
- ansible-test - Allow unstable tests to run when targeted changes are made and the ``--allow-unstable-changed`` option is specified (resolves https://github.com/ansible/ansible/issues/74213).
- ansible-test - Always indicate the Python version being used before installing requirements. Resolves issue https://github.com/ansible/ansible/issues/72855
- ansible-test - Avoid using ``exec`` after container startup when possible. This improves container startup performance and avoids intermittent startup issues with some old containers.
- ansible-test - Connection attempts to managed remote instances no longer abort on ``Permission denied`` errors.
- ansible-test - Detection for running in a Podman or Docker container has been fixed to detect more scenarios. The new detection relies on ``/proc/self/mountinfo`` instead of ``/proc/self/cpuset``. Detection now works with custom cgroups and private cgroup namespaces.
- ansible-test - Exclude ansible-core vendored Python packages from ansible-test payloads.
- ansible-test - Fix broken documentation link for ``aws`` test plugin error messages.
- ansible-test - Fix validate-modules error when retrieving PowerShell argspec when retrieved inside a Cmdlet
- ansible-test - Handle server errors when executing the ``docker info`` command.
- ansible-test - Integration test target prefixes defined in a ``tests/integration/target-prefixes.{group}`` file can now contain an underscore (``_``) character. Resolves issue https://github.com/ansible/ansible/issues/79225
- ansible-test - Multiple containers now work under Podman without specifying the ``--docker-network`` option.
- ansible-test - Pass the ``XDG_RUNTIME_DIR`` environment variable through to container commands.
- ansible-test - Perform PyPI proxy configuration after instances are ready and bootstrapping has been completed. Only target instances are affected, as controller instances were already handled this way. This avoids proxy configuration errors when target instances are not yet ready for use.
- ansible-test - Prevent concurrent / repeat inspections of the same container image.
- ansible-test - Prevent concurrent / repeat pulls of the same container image.
- ansible-test - Prevent concurrent execution of cached methods.
- ansible-test - Removed pointless comparison in diff evaluation logic.
- ansible-test - Set ``PYLINTHOME`` for the ``pylint`` sanity test to prevent failures due to ``pylint`` checking for the existence of an obsolete home directory.
- ansible-test - Show the exception type when reporting errors during instance provisioning.
- ansible-test - Support Podman 4.4.0+ by adding the ``SYS_CHROOT`` capability when running containers.
- ansible-test - Support loading of vendored Python packages from ansible-core.
- ansible-test - The ``validate-modules`` sanity test now properly enforces documentation before imports for plugins. Previously this was only enforced for modules due to a coding error.
- ansible-test - Update ``pylint`` to 2.17.2 to resolve several possible false positives.
- ansible-test - Update ``pylint`` to 2.17.3 to resolve several possible false positives.
- ansible-test - Update the ``pylint`` sanity test requirements to resolve crashes on Python 3.11. (https://github.com/ansible/ansible/issues/78882)
- ansible-test - Update the ``pylint`` sanity test to use version 2.15.4.
- ansible-test - Update the ``pylint`` sanity test to use version 2.15.5.
- ansible-test - Use consistent file permissions when delegating tests to a container or remote host. Files with any execute bit set will use permissions ``755``. All other files will use permissions ``644``. (Resolves issue https://github.com/ansible/ansible/issues/75079)
- ansible-test - When bootstrapping remote FreeBSD instances, use the OS packaged ``setuptools`` instead of installing the latest version from PyPI.
- ansible-test - fix warning message about failing to run an image to include the image name
- ansible-test runtime-metadata sanity test - do not crash on YAML parsing errors without a context mark (https://github.com/ansible/ansible/pull/78802).
- ansible-test sanity - correctly report invalid YAML in validate-modules (https://github.com/ansible/ansible/issues/75837).
- ansible-vault encrypt_string - started appending a line feed at the end of the encrypted string output. Missing newline character caused problems identifying where the string ends in some shells (like bash) or accidentally copying an extra trailing terminator symbol (e.g., zsh prints out a ``%`` sign to signal where the original output stops) (https://github.com/ansible/ansible/issues/78932).
- ansible_facts.hardware - Define all processor facts on s390x (https://github.com/ansible/ansible/issues/19755)
- apt - set locale to fix updating the cache (https://github.com/ansible/ansible/issues/79523).
- apt module should not traceback on invalid type given as package. issue 78663.
- apt_repository will no longer fail to detect key when unrelated errors/warnings are issued by apt-key.
- argument spec validation - again report deprecated parameters for Python-based modules. This was accidentally removed in ansible-core 2.11 when argument spec validation was refactored (https://github.com/ansible/ansible/issues/79680, https://github.com/ansible/ansible/pull/79681).
- argument spec validation - ensure that deprecated aliases in suboptions are also reported (https://github.com/ansible/ansible/pull/79740).
- argument spec validation - fix warning message when two aliases of the same option are used for suboptions to also mention the option's name they are in (https://github.com/ansible/ansible/pull/79740).
- basic.py module_utils - Perform Python version check much earlier to ensure it runs before other errors occur.
- connection local now avoids traceback on invalid user being used to execuet ansible (valid in host, but not in container).
- copy - fix creating the dest directory in check mode with remote_src=True (https://github.com/ansible/ansible/issues/78611).
- copy - fix reporting changes to file attributes in check mode with remote_src=True (https://github.com/ansible/ansible/issues/77957).
- copy module will no longer move 'non files' set as src when remote_src=true.
- copy remote_src=true - fix copying subdirs recursively when the dest exists and the src and dest have multiple common subdirectories in a common directory (https://github.com/ansible/ansible/issues/74536).
- copy remote_src=true - fix reporting changed for copying empty directories.
- display - reduce risk of post-fork output deadlocks (https://github.com/ansible/ansible/pull/79522)
- dnf5 - Use ``transaction.check_gpg_signatures`` API call to check package signatures AND possibly to recover from when keys are missing.
- dnf5 - fix module and package names in the message following failed module respawn attempt
- dnf5 - use the logs API to determine transaction problems
- file - touch action in check mode was always returning ok. Fix now evaluates the different conditions and returns the appropriate changed status. (https://github.com/ansible/ansible/issues/79360)
- file lookup now handles missing files more gracefully.
- file lookup now plays nice with generic lookup ``errors`` option.
- get_url - Ensure we are passing ciphers to all url_get calls (https://github.com/ansible/ansible/issues/79717)
- get_url module - Added a documentation reference to ``hashlib`` regarding algorithms, as well as a note about ``md5`` support on systems running in FIPS compliant mode.
- get_url module - Removed out-of-date documentation stating that ``hashlib`` is a third-party library.
- handlers - fix ``v2_playbook_on_notify`` callback not being called when notifying handlers
- handlers - fix an issue where the ``flush_handlers`` meta task could not be used with FQCN: ``ansible.builtin.meta`` (https://github.com/ansible/ansible/issues/79023)
- include_role - Inherit from role parents beyond a depth of 3 (https://github.com/ansible/ansible/issues/47023).
- jinja2_native - fix intermittent 'could not find job' failures when a value of ``ansible_job_id`` from a result of an async task was inadvertently changed during execution; to prevent this a format of ``ansible_job_id`` was changed.
- jinja2_native: preserve quotes in strings (https://github.com/ansible/ansible/issues/79083)
- keyword inheritance - Ensure that we do not squash keywords in validate (https://github.com/ansible/ansible/issues/79021)
- known_hosts - do not return changed status when a non-existing key is removed (https://github.com/ansible/ansible/issues/78598)
- list-tags now shows the 'never' tag, which was being excluded by default. To list all tasks you still need to add `--list-tasks --tags never,all`.
- loops/delegate_to - Do not double calculate the values of loops and ``delegate_to`` (https://github.com/ansible/ansible/issues/80038)
- module responses - Ensure that module responses are utf-8 adhereing to JSON RFC and expectations of the core code.
- module/role argument spec - validate the type for options that are None when the option is required or has a non-None default (https://github.com/ansible/ansible/issues/79656).
- module_utils/basic.py - Fix detection of available hashing algorithms on Python 3.x. All supported algorithms are now available instead of being limited to a hard-coded list. This affects modules such as ``get_url`` which accept an arbitrary checksum algorithm.
- normal action plugin - remove obsolete ``if`` (https://github.com/ansible/ansible/pull/79690).
- omit on keywords was resetting to default value, ignoring inheritance.
- paramiko - Add a new option to allow paramiko >= 2.9 to easily work with all devices now that rsa-sha2 support was added to paramiko, which prevented communication with numerous platforms. (https://github.com/ansible/ansible/issues/76737)
- paramiko - Add back support for ``ssh_args``, ``ssh_common_args``, and ``ssh_extra_args`` for parsing the ``ProxyCommand`` (https://github.com/ansible/ansible/issues/78750)
- paramiko connection was still using outdated playcontext, this should bring it up to date to use the 'correct' data for each task/loop.
- password lookup now correctly reads stored ident fields.
- password_hash - handle errors using unknown passlib hashtypes more gracefully (https://github.com/ansible/ansible/issues/45392).
- pep517 build backend - Use the documented ``import_module`` import from ``importlib``.
- plugin loader, fix detection for existing configuration before initializing for a plugin
- role deduplication - Always create new role object, regardless of deduplication. Deduplication will only affect whether a duplicate call to a role will execute, as opposed to re-using the same object. (https://github.com/ansible/ansible/pull/78661)
- roles - Fix templating ``public``, ``allow_duplicates`` and ``rolespec_validate`` (https://github.com/ansible/ansible/issues/80304).
- service_facts - Use python re to parse service output instead of grep (https://github.com/ansible/ansible/issues/78541)
- strategy plugins now correctly identify bad registered variables, even on skip.
- strategy plugins: get the correctly templated and validated run_once value on strategy linear (https://github.com/ansible/ansible/issues/78492)
- syntax check - Limit ``--syntax-check`` to ``ansible-playbook`` only, as that is the only CLI affected by this argument (https://github.com/ansible/ansible/issues/80506)
- systemd - daemon-reload and daemon-reexec ignore errors when running in a chroot (https://github.com/ansible/ansible/pull/79643)
- templates - Fixed ``TypeError`` when a lookup plugin has an option called ``name``.
- unarchive - allow relative path for ``dest`` (https://github.com/ansible/ansible/issues/64612)
- unarchive - log errors from commands to assist in debugging (https://github.com/ansible/ansible/issues/64612)
- updated error messages to include 'acl' and not just mode changes when failing to set required permissions on remote.
- uri - improve JSON content type detection
- user - fix comparing group IDs to existing group names so groups are not always updated (https://github.com/ansible/ansible/issues/79956).
- user module - Removed ``password_expire_max`` from the return docs, as it is not returned.
- user module - Removed ``password_expire_min`` from the return docs, as it is not returned.
- validate-modules sanity test - replace semantic markup parsing and validating code with the code from `antsibull-docs-parser 0.2.0 <https://github.com/ansible-community/antsibull-docs-parser/releases/tag/0.2.0>`__ (https://github.com/ansible/ansible/pull/80406).
- vault - show filename additionally if missing secrets prevents decryption (https://github.com/ansible/ansible/issues/79723)
- winrm - Increase the read timeout to 10 seconds later than the operation timeout reducing the chances of a false read timeout

amazon.aws
~~~~~~~~~~

- aws_ec2 inventory plugin - fix ``NoRegionError`` when no regions are provided and region isn't specified (https://github.com/ansible-collections/amazon.aws/issues/1551).
- aws_rds - fixes bug in RDS inventory plugin where config file was ignored (https://github.com/ansible-collections/amazon.aws/issues/1304).
- cloudtrail - support to disabling encryption using ``kms_key_id`` (https://github.com/ansible-collections/amazon.aws/pull/1384).
- cloudwatch_metric_alarm - Don't consider ``StateTransitionedTimestamp`` in change detection. (https://github.com/ansible-collections/amazon.aws/pull/1440).
- ec2_instance - Pick up ``app_callback -> set_password`` rather than ``app_callback -> set_passwd`` (https://github.com/ansible-collections/amazon.aws/issues/1449).
- ec2_key - fix issue when trying to update existing key pair with the same key material (https://github.com/ansible-collections/amazon.aws/pull/1383).
- ec2_metadata_facts - fix ``AttributeError`` when running the ec2_metadata_facts module on Python 2 managed nodes (https://github.com/ansible-collections/amazon.aws/issues/1358).
- ec2_security_group - file included unreachable code. Fix now removes unreachable code by removing an inapproproate logic (https://github.com/ansible-collections/amazon.aws/pull/1348).
- ec2_vol - handle ec2_vol.tags when the associated instance already exists (https://github.com/ansible-collections/amazon.aws/pull/1071).
- ec2_vpc_dhcp_option - retry ``describe_dhcp_options`` after creation when ``InvalidDhcpOptionID.NotFound`` is raised (https://github.com/ansible-collections/amazon.aws/pull/1320).
- lambda - fix flaky integration test which assumes there are no other lambdas in the account (https://github.com/ansible-collections/amazon.aws/issues/1277)
- lambda_execute - Fix waiter error when function_arn is passed instead of name(https://github.com/ansible-collections/amazon.aws/issues/1268).
- lambda_info - Do not convert environment variables to snake_case when querying lambda config. (https://github.com/ansible-collections/amazon.aws/pull/1457).
- module_utils - fixes ``TypeError: deciding_wrapper() got multiple values for argument 'aws_retry'`` when passing positional arguments to functions wrapped by AnsibleAWSModule.client (https://github.com/ansible-collections/amazon.aws/pull/1230).
- module_utils/elbv2 - fix change detection by adding default values for ``Scope`` and ``SessionTimeout`` parameters in ``authenticate-oidc`` rules (https://github.com/ansible-collections/amazon.aws/pull/1270).
- module_utils/elbv2 - respect ``UseExistingClientSecret`` parameter in ``authenticate-oidc`` rules (https://github.com/ansible-collections/amazon.aws/pull/1270).
- rds_instance - Fixed ``TypeError`` when tagging RDS DB with storage type ``gp3`` (https://github.com/ansible-collections/amazon.aws/pull/1437).
- rds_instance - fix type of ``promotion_tier`` as passed to the APIs (https://github.com/ansible-collections/amazon.aws/pull/1475).
- rds_param_group - added a check to fail the task while modifying/updating rds_param_group if trying to change DB parameter group family. (https://github.com/ansible-collections/amazon.aws/pull/1169).
- revert breaking change introduced in 5.2.0 when passing credentials through a mix of environment variables and parameters (https://github.com/ansible-collections/amazon.aws/issues/1353).
- route53_health_check - Fix ``Name`` tag key removal idempotentcy issue when creating health_check with ``use_unique_names`` and ``tags`` set (https://github.com/ansible-collections/amazon.aws/pull/1253).
- route53_info - Add new return key ``health_check_observations`` for health check operations (https://github.com/ansible-collections/amazon.aws/pull/1419).
- route53_info - Fixed ``Key Error`` when getting status or failure_reason of a health check (https://github.com/ansible-collections/amazon.aws/pull/1419).
- s3_bucket - Handle setting of permissions while acl is disabled.(https://github.com/ansible-collections/amazon.aws/pull/1168).
- s3_bucket - empty bucket policy was throwing a JSONDecodeError - deal with it gracefully instead (https://github.com/ansible-collections/amazon.aws/pull/1368)
- s3_bucket - fixes issue when deleting a bucket with unversioned objects (https://github.com/ansible-collections/amazon.aws/issues/1533).
- s3_object - fixes regression related to objects with a leading ``/`` (https://github.com/ansible-collections/amazon.aws/issues/1548).

ansible.netcommon
~~~~~~~~~~~~~~~~~

- Cast AnsibleUnsafeText to str in convert_doc_to_ansible_module_kwargs() to keep CSafeLoader happy. This fixes issues with content scaffolding tools.
- httpapi - ``send()`` method no longer applied leftover kwargs to ``open_url()``. Fix applies those arguments as intended (https://github.com/ansible-collections/ansible.netcommon/pull/524).
- network_cli - network cli connection avoids traceback when using invalid user
- network_cli - when receiving longer responses with libssh, parts of the response were sometimes repeated. The response is now returned as it is received (https://github.com/ansible-collections/community.routeros/issues/132).
- network_resource - do not append network_os to module names when building supported resources list. This fix is only valid for cases where FACTS_RESOURCE_SUBSETS is undefined.
- network_resource - fix a potential UnboundLocalError if the module fails to import a Resource Module. (https://github.com/ansible-collections/ansible.netcommon/pull/513)
- restconf - creation of new resources is no longer erroneously forced to use POST. (https://github.com/ansible-collections/ansible.netcommon/issues/502)

ansible.posix
~~~~~~~~~~~~~

- Fix sysctl integration test failing on newer versions of core. Previously NoneType was allowable, now it fails to convert to a str type.
- Fixed a bug where firewalld module fails to create/remove zones when the daemon is stopped
- Removed contentious terminology to match reference documentation in profile_tasks.
- Support new sanity test for the ansible-core devel branch CI test (https://github.com/ansible-collections/ansible.posix/issues/446).
- firewall - Fix issue where adding an interface to a zone would fail when the daemon is offline
- firewall - Fix issue where opening a specific port resulted in opening the whole protocol of the specified port
- firewall - Fixed to output a more complete missing library message.
- firewalld - Consider value of masquerade and icmp_block_inversion parameters when a boolean like value is passed
- rhel_facts - Call exit_json with all keyword arguments
- synchronize - Fixed hosts involved in rsync require the same password

ansible.utils
~~~~~~~~~~~~~

- Accept int input for ipaddr filters.
- mac - reorganize regexes to work around 3.11 regex changes. (https://github.com/ansible-collections/ansible.utils/pull/231)

ansible.windows
~~~~~~~~~~~~~~~

- setup - Be more resilient when parsing the BIOS release date - https://github.com/ansible-collections/ansible.windows/pull/496
- setup - Fallback to using the WMI Win32_Processor provider if the SMBIOS version is too old to return processor core counts
- setup - Fix calculation for ``ansible_processor_threads_per_core`` to reflect the number of threads per core instead of threads per processor
- setup - Ignore processors that are not enabled in the ``ansible_processor_count`` return value
- setup - Support core and thread counts greater than 256 in ``ansible_processor_count`` and ``ansible_processor_threads_per_core``
- win_dns_client - Fix failure to lookup registry DNS servers when it contains null characters
- win_package - Fix ``product_id`` check and skip downloaded requested file if the package is already installed - https://github.com/ansible-collections/ansible.windows/issues/479
- win_powershell - Support PowerShell 7 script syntax when targeting ``executable: pwsh.exe`` - https://github.com/ansible-collections/ansible.windows/issues/452
- win_updates - Add better handling for the polling output for connection plugins that might drop newlines on the output - https://github.com/ansible-collections/ansible.windows/issues/477
- win_updates - Ensure failure condition doesn't lock the polling file - https://github.com/ansible-collections/ansible.windows/issues/490
- win_updates - Improve batch task runner reliability and attempt to return more info on failures - https://github.com/ansible-collections/ansible.windows/issues/448
- win_wait_for - fix incorrect function name during ``state=drained`` - https://github.com/ansible-collections/ansible.windows/issues/451

arista.eos
~~~~~~~~~~

- fix ntp_global authenticate config.
- https://github.com/ansible-collections/arista.eos/issues/399.

chocolatey.chocolatey
~~~~~~~~~~~~~~~~~~~~~

- win_chocolatey - Module fails to execute if powershell version is older than version 5.

cisco.aci
~~~~~~~~~

- Add snapshot job details in result of aci_config_snapshot to support query of snapshot results (#342)
- Fix aci_encap_pool_range by removing range_name from required parameters (#368)
- Fix missing annotation field in aci_ntp_policy and aci_ntp_server (#392)
- Fix query of all blacklisted interfaces using aci_interface_blacklist (#367)
- Forced unicode encoding for lxml XML fragment validation output  to fix issue with Certificate authentication and aci_rest with XML payload (#341)

cisco.dnac
~~~~~~~~~~

- A new method to compare changes for specific cases has been added.
- DNA Center credentials can now be exported and used as env vars.
- netconf_credential - Removed to search by username.
- network_device - Used a new method to compare changes.
- sda_fabric_border_device - fix Create example at EXAMPLES block
- sda_virtual_network_ip_pool - Now pass the site_name_hierarchy correctly in get method.
- site_intent - fix Case_1 return example at RETURN block
- snmpv2_read_community_credential - Removed to search by username.
- snmpv2_write_community_credential - Removed to search by username.
- swim_intent - fix functionality and tests

cisco.ios
~~~~~~~~~

- Fix parser to read groups in snmp-server.
- Fix parser to read transceiver in snmp-server.
- ios_acls - fix acl commands order on replaced and overridden state.
- ios_acls - fix eq to process protocol number as protocol name.
- ios_acls - fix object group for extended acls.
- ios_acls - fix parsers to accept precedence value in correct format.
- ios_acls - fix precedence attribute to take a string value as input.
- ios_acls - fix processing of source information on extended acls entries.
- ios_acls - fix rendering of object-groups in source and destination at ace level.
- ios_acls - prevent rendering of mac access-lists in facts.
- ios_bgp_address_family - Reorder parsers to generate correct oder of configuration lines.
- ios_bgp_address_family - aliased aggregate_address to aggregate_addresses that supports a list of dict attributes
- ios_bgp_address_family - aliased neighbor to neighbors that supports a list of dict attributes
- ios_bgp_address_family - aliased network to networks that supports a list of dict attributes
- ios_bgp_address_family - fix facts generation of default originate option.
- ios_bgp_address_family - fix facts rendering with optimal parsers
- ios_bgp_address_family - fix fliter_list rendering
- ios_bgp_address_family - fix issue where no commands are generated when redistributing OSPFv2 and OSPFv3
- ios_bgp_address_family - fix missing negations in overridden and replaced states when redistributing OSPF
- ios_bgp_address_family - fix option and syntax for OSPF E1 and E2 routes
- ios_bgp_address_family - fix option and syntax for OSPF N1 and N2 routes
- ios_bgp_address_family - fix order of generated OSPF redistribution command options to achieve idempotency
- ios_bgp_address_family - fix path_attribute to support float parameter
- ios_bgp_global - fix configuration of timers under neighbor. (https://github.com/ansible-collections/cisco.ios/issues/794)
- ios_bgp_global - fix neighbor shutdown command on set value being false.
- ios_command - Run & evaluate commands at least once even when retries is set to 0 (https://github.com/ansible-collections/cisco.nxos/issues/607).
- ios_l2_interfaces - fix command to remove allowed_vlans and pruning_vlans from configuration.
- ios_l2_interfaces - fix dynamic option for mode attribute.
- ios_l2_interfaces - fix state operation for existing vlans.
- ios_l3_interfaces - fix command generation on attribute value being false.
- ios_l3_interfaces - prevent configuration line generation when enable is false.
- ios_lag_interfaces - fix deleted state to delete only sub attribute values.
- ios_logging_global - logging history configuration command fixed for supported appliance versions.
- ios_ospf_interfaces - fix dead-interval rendering wrong facts when hello-multiplier is configured.
- ios_route_maos - fix replaced state support. (https://github.com/ansible-collections/cisco.ios/issues/680)
- ios_route_maps - fix idempotency for `set community` operations. (https://github.com/ansible-collections/cisco.ios/issues/635)
- ios_route_maps - fix idempotency issues with as-path prepend (https://github.com/ansible-collections/cisco.ios/issues/678)
- ios_route_maps - fix idempotency issues with set community none (https://github.com/ansible-collections/cisco.ios/issues/679
- ios_route_maps - fix merge issues with route-maps where wanted config is not deployed if route map has existing sequence numbers (https://github.com/ansible-collections/cisco.ios/issues/641)
- ios_static_routes - fix configure generation order for ipv4 and ipv6 routes.
- ios_static_routes - fix module to be idempotent with replaced and overridden state.
- ios_vlans - Added support for private VLAN configuration
- ios_vrf - fix issue where assigning interfaces to existing vrfs doesn't work (https://github.com/ansible-collections/cisco.ios/issues/707)

cisco.iosxr
~~~~~~~~~~~

- Bgp_global, Bgp_neighbor_address_family, Bgp_address_family. Make all possible option mutually exclusive.
- Fix issue of iosxr_config parellel uploads.
- Fixing L2 Interface recognition for resource modules. (https://github.com/ansible-collections/cisco.iosxr/issues/366)
- Iosxr_interfaces - Fix issue in interfaces with interface type.
- Support commit confirmed functionality with replace option.
- bgp_global -  Fix neighbor description parser issue.
- bgp_neighbor_address_family - mark ``soft_reconfiguration`` suboptions ``set``, ``always``, and ``inheritance_disable`` as mutually exclusive. (https://github.com/ansible-collections/cisco.iosxr/issues/325)
- facts - fix ``ansible_net_model`` and ``ansible_net_seriulnum`` facts gathering issue (https://github.com/ansible-collections/cisco.iosxr/issues/308)
- interfaces - Fix issue in ``overridden`` state of interfaces RM. (https://github.com/ansible-collections/cisco.iosxr/issues/377)

cisco.ise
~~~~~~~~~

- network_access_authentication_rules - now read the ID correctly.
- network_access_authorization_rules - is now idempotent.
- network_access_authorization_rules - now read the ID correctly.
- network_access_authorization_rules - recognizes when there are changes.
- node_group - search was repaired.
- node_group_node_info - removed a validation that caused a failure.

cisco.meraki
~~~~~~~~~~~~

- Corrects constraints applied to local and remote status page settings to align with API behaviour (https://github.com/CiscoDevNet/ansible-meraki/issues/437)
- Enables meraki_network query by net_id (https://github.com/CiscoDevNet/ansible-meraki/issues/441)
- Fix checkmode on merak webhook payload template update
- Resolved an issue where an empty response from the API triggered an exception in module meraki_webhook (https://github.com/CiscoDevNet/ansible-meraki/issues/433)
- Resolved issue
- Resolves issues with meraki_webhook shared_secret defaulting to null; (https://github.com/CiscoDevNet/ansible-meraki/issues/439); Also adds Test Coverage for shared secret idempotency and resolves test file lint issues.
- Update defaults in documentation for new sanity tests
- Update pipeline to use newer version of action to detect changed files.
- meraki_alert - Fix situation where specifying emails may crash.
- meraki_device - Fix URL for LLDP and CDP lookups
- meraki_mx_site_to_site_vpn - Check mode should no longer apply changes when enabled.
- meraki_webhook - First error when updating URL in a webhook

cisco.mso
~~~~~~~~~

- Add attributes to payload for changed schema behaviour of deploymentImmediacy (deployImmediacy) and vmmDomainProperties (properties at domain level in payload) (#362)
- Fix MSO HTTPAPI plugin login domain issue (#317)
- Fix datetime support for python2.7 in mso_backup_schedule (#323)
- Fix deploymentImmediacy key inconsistency in the API used by mso_schema_site_anp and mso_schema_site_anp_epg (#283)
- Fix idempotency for mso_schema_site_bd_l3out
- Fix mso_backup for NDO and ND-based MSO v3.2+ (#333)
- Fix mso_schema_template_bd issue when created with unicast_routing as false (#278)
- Fix to be able to add multiple filter and filters with "-" in their names (#306)
- Fix validation condition for path in mso_schema_site_anp_epg_bulk_staticport module (#360)

cisco.nxos
~~~~~~~~~~

- `bgp` - Fix parsing remote-as for Nexus 3K (https://github.com/ansible-collections/cisco.nxos/issues/653).
- `facts` - Attempt to execute json output commands with | json-pretty first and fall back to | json if unsupported. This is a temporary workaround until https://github.com/ansible/pylibssh/issues/208 is fixed.
- `interfaces` - Correctly enable/disable VLAN interfaces (https://github.com/ansible-collections/cisco.nxos/issues/539).
- `nxos_acls` - Fix how IPv6 prefixes are converted to hosts (https://github.com/ansible-collections/cisco.nxos/issues/623).
- `nxos_acls` - Parse ICMP echo-reply and echo options correctly (https://github.com/ansible-collections/cisco.nxos/issues/583).
- `nxos_acls` - Parse ICMP port-unreachable and unreachable options correctly (https://github.com/ansible-collections/cisco.nxos/issues/529).
- `nxos_acls` - Parse port-protocol options with hypenated names correctly (https://github.com/ansible-collections/cisco.nxos/issues/557).
- `nxos_file_copy` - stop prepending redundant bootflash: to remote file names
- `route_maps` - resolve route-map description parameter idempotency
- `snmp_server` - fix community option to produce proper configuration with ipv4acl and ipv6acl.
- nxos_acls - Detect duplicate ACE error message from CLI and fail (https://github.com/ansible-collections/cisco.nxos/issues/611).
- nxos_command - Run & evaluate commands at least once even when retries is set to 0 (https://github.com/ansible-collections/cisco.nxos/issues/607).

cloud.common
~~~~~~~~~~~~

- module_utils/turbo/server - import needed library into the right place (https://github.com/ansible-collections/cloud.common/pull/120)

community.aws
~~~~~~~~~~~~~

- aws_ssm - fix ``invalid literal for int`` error on some operating systems (https://github.com/ansible-collections/community.aws/issues/113).
- aws_ssm - fix copying empty file with older curl versions (https://github.com/ansible-collections/community.aws/issues/1686).
- aws_ssm - fixes S3 bucket region detection by ensuring boto client has correct credentials and exists in correct partition (https://github.com/ansible-collections/community.aws/pull/1428).
- aws_ssm - fixes bug with presigned S3 URLs in post-2019 AWS regions (https://github.com/ansible-collections/community.aws/issues/1616).
- cloudformation_stack_set - add a waiter to ensure that update operation complete before adding stack instances (https://github.com/ansible-collections/community.aws/issues/1608).
- ec2_snapshot_copy - including tags caused the erorr ``Tag specification resource type must have a value``. Fix sets the ResourceType to snapshot to resolve this issue (https://github.com/ansible-collections/community.aws/pull/1419).
- ecs_ecr - fix a ``RepositoryNotFound`` exception when trying to create repositories in check mode (https://github.com/ansible-collections/community.aws/pull/1550).
- ecs_service - respect ``placement_constraints`` for existing ECS services (https://github.com/ansible-collections/community.aws/pull/1601).
- eks_cluster - adding tags to eks cluster creation (https://github.com/ansible-collections/community.aws/pull/1591).
- eks_nodegroup - fix handling of ``remote_access`` option (https://github.com/ansible-collections/community.aws/issues/1771).
- elasticache_info - ignore the ``CacheClusterNotFound`` exception when collecting tags (https://github.com/ansible-collections/community.aws/pull/1777).
- elb_target_group - ensure ``AvailabilityZone`` is kept in target definitions when ``Id`` and ``Port`` are passed (https://github.com/ansible-collections/community.aws/issues/1736).
- elb_target_group - get ``ProtocolVersion`` key from ``target_group`` attributes only when exists (https://github.com/ansible-collections/community.aws/pull/1800).
- msk_cluster - fix creating a cluster with SASL/SCRAM authentication (https://github.com/ansible-collections/community.aws/issues/1761).
- opensearch - Fix cluster creation when using advanced security options (https://github.com/ansible-collections/community.aws/pull/1613).
- opensearch_info - Fix the name of the domain_name key in the example (https://github.com/ansible-collections/community.aws/pull/1811).
- s3_lifecycle - fix invalid value type for transitions list (https://github.com/ansible-collections/community.aws/issues/1774)
- s3_lifecycle - module no longer calls ``put_lifecycle_configuration`` if there is no change (https://github.com/ansible-collections/community.aws/issues/1624).
- ses_identity - fix clearing notification topic (https://github.com/ansible-collections/community.aws/issues/150).
- sns_topic - avoid fetching attributes from subscribers when not setting them, this can cause permissions issues (https://github.com/ansible-collections/community.aws/pull/1418).
- ssm_parameter - fix a ``KeyError`` when adding a description to an existing parameter (https://github.com/ansible-collections/community.aws/issues/1471).

community.crypto
~~~~~~~~~~~~~~~~

- action plugin helper - fix handling of deprecations for ansible-core 2.14.2 (https://github.com/ansible-collections/community.crypto/pull/572).
- execution environment binary dependencies (bindep.txt) - fix ``python3-pyOpenSSL`` dependency resolution on RHEL 9+ / CentOS Stream 9+ platforms (https://github.com/ansible-collections/community.crypto/pull/575).
- execution environment definition - fix installation of ``python3-pyOpenSSL`` package on CentOS and RHEL (https://github.com/ansible-collections/community.crypto/pull/606).
- execution environment definition - fix source of ``python3-pyOpenSSL`` package for Rocky Linux 9+ (https://github.com/ansible-collections/community.crypto/pull/606).
- openssh_keypair - always generate a new key pair if the private key does not exist. Previously, the module would fail when ``regenerate=fail`` without an existing key, contradicting the documentation (https://github.com/ansible-collections/community.crypto/pull/598).
- openssl_csr, openssl_csr_pipe - prevent invalid values for ``crl_distribution_points`` that do not have one of ``full_name``, ``relative_name``, and ``crl_issuer`` (https://github.com/ansible-collections/community.crypto/pull/560).
- openssl_publickey_info - do not crash with internal error when public key cannot be parsed (https://github.com/ansible-collections/community.crypto/pull/551).
- various plugins - remove unnecessary imports (https://github.com/ansible-collections/community.crypto/pull/569).
- x509_crl - remove problem with ansible-core 2.16 due to ``AnsibleModule`` is now validating the ``mode`` parameter's values (https://github.com/ansible-collections/community.crypto/issues/596).

community.digitalocean
~~~~~~~~~~~~~~~~~~~~~~

- integration tests - add missing `environment` directive on pull request integration testing (https://github.com/ansible-collections/community.digitalocean/issues/293).
- inventory plugin - bugfix for baseurl parameter (https://github.com/ansible-collections/community.digitalocean/pull/297).

community.dns
~~~~~~~~~~~~~

- Update Public Suffix List.
- inventory plugins - document ``plugin`` option used by the ``ansible.builtin.auto`` inventory plugin and mention required file ending in the documentation (https://github.com/ansible-collections/community.dns/issues/130, https://github.com/ansible-collections/community.dns/pull/131).

community.docker
~~~~~~~~~~~~~~~~

- Make vendored Docker SDK for Python code compatible with requests 2.29.0 and urllib3 2.0 (https://github.com/ansible-collections/community.docker/pull/613).
- current_container_facts - make container detection work better in more cases (https://github.com/ansible-collections/community.docker/pull/522).
- docker_api connection plugin - fix error handling when 409 Conflict is returned by the Docker daemon in case of a stopped container (https://github.com/ansible-collections/community.docker/pull/546).
- docker_api connection plugin, docker_container_exec, docker_container_copy_into - properly close socket to Daemon after executing commands in containers (https://github.com/ansible-collections/community.docker/pull/582).
- docker_container - fix ``tmfs_size`` and ``tmpfs_mode`` not being set (https://github.com/ansible-collections/community.docker/pull/580).
- docker_container - the ``kill_signal`` option erroneously did not accept strings anymore since 3.0.0 (https://github.com/ansible-collections/community.docker/issues/505, https://github.com/ansible-collections/community.docker/pull/506).
- docker_container - when ``detach=false``, wait indefinitely and not at most one minute. This was the behavior with Docker SDK for Python, and was accidentally changed in 3.0.0 (https://github.com/ansible-collections/community.docker/issues/526, https://github.com/ansible-collections/community.docker/pull/527).
- docker_container_exec - fix ``chdir`` option which was ignored since community.docker 3.0.0 (https://github.com/ansible-collections/community.docker/issues/517, https://github.com/ansible-collections/community.docker/pull/518).
- docker_container_exec - fix error handling when 409 Conflict is returned by the Docker daemon in case of a stopped container (https://github.com/ansible-collections/community.docker/pull/546).
- docker_plugin - do not crash if plugin is installed in check mode (https://github.com/ansible-collections/community.docker/issues/552, https://github.com/ansible-collections/community.docker/pull/553).
- docker_prune - return correct value for ``changed``. So far the module always claimed that nothing changed (https://github.com/ansible-collections/community.docker/pull/593).
- most modules - fix handling of ``DOCKER_TIMEOUT`` environment variable, and improve handling of other fallback environment variables (https://github.com/ansible-collections/community.docker/issues/551, https://github.com/ansible-collections/community.docker/pull/554).
- socket_handler module utils - make sure this fully works when Docker SDK for Python is not available (https://github.com/ansible-collections/community.docker/pull/620).
- various plugins and modules - remove unnecessary imports (https://github.com/ansible-collections/community.docker/pull/574).
- vendored Docker SDK for Python code - fix for errors on pipe close in Windows (https://github.com/ansible-collections/community.docker/pull/619).
- vendored Docker SDK for Python code - respect timeouts on Windows named pipes (https://github.com/ansible-collections/community.docker/pull/619).
- vendored Docker SDK for Python code - use ``poll()`` instead of ``select()`` except on Windows (https://github.com/ansible-collections/community.docker/pull/619).
- vendored latest Docker SDK for Python bugfix (https://github.com/ansible-collections/community.docker/pull/513, https://github.com/docker/docker-py/issues/3045).

community.general
~~~~~~~~~~~~~~~~~

- ModuleHelper - fix bug when adjusting the name of reserved output variables (https://github.com/ansible-collections/community.general/pull/5755).
- alternatives - support subcommands on Fedora 37, which uses ``follower`` instead of ``slave`` (https://github.com/ansible-collections/community.general/pull/5794).
- ansible_galaxy_install - set default to raise exception if command's return code is different from zero (https://github.com/ansible-collections/community.general/pull/5680).
- ansible_galaxy_install - try ``C.UTF-8`` and then fall back to ``en_US.UTF-8`` before failing (https://github.com/ansible-collections/community.general/pull/5680).
- archive - avoid deprecated exception class on Python 3 (https://github.com/ansible-collections/community.general/pull/6180).
- archive - reduce RAM usage by generating CRC32 checksum over chunks (https://github.com/ansible-collections/community.general/pull/6274).
- bitwarden lookup plugin - clarify what to do, if the bitwarden vault is not unlocked (https://github.com/ansible-collections/community.general/pull/5811).
- cartesian and flattened lookup plugins - adjust to parameter deprecation in ansible-core 2.14's ``listify_lookup_plugin_terms`` helper function (https://github.com/ansible-collections/community.general/pull/6074).
- chroot connection plugin - add ``inventory_hostname`` to vars under ``remote_addr``. This is needed for compatibility with ansible-core 2.13 (https://github.com/ansible-collections/community.general/pull/5570).
- cloudflare_dns - fixed the idempotency for SRV DNS records (https://github.com/ansible-collections/community.general/pull/5972).
- cloudflare_dns - fixed the possiblity of setting a root-level SRV DNS record (https://github.com/ansible-collections/community.general/pull/5972).
- cmd_runner module utils - fixed bug when handling default cases in ``cmd_runner_fmt.as_map()`` (https://github.com/ansible-collections/community.general/pull/5538).
- cmd_runner module utils - formatting arguments ``cmd_runner_fmt.as_fixed()`` was expecting an non-existing argument (https://github.com/ansible-collections/community.general/pull/5538).
- dependent lookup plugin - avoid warning on deprecated parameter for ``Templar.template()`` (https://github.com/ansible-collections/community.general/pull/5543).
- deps module utils - do not fail when dependency cannot be found (https://github.com/ansible-collections/community.general/pull/6479).
- dig lookup plugin - correctly handle DNSKEY record type's ``algorithm`` field (https://github.com/ansible-collections/community.general/pull/5914).
- flatpak - fixes idempotency detection issues. In some cases the module could fail to properly detect already existing Flatpaks because of a parameter witch only checks the installed apps (https://github.com/ansible-collections/community.general/pull/6289).
- gconftool2 - fix ``changed`` result always being ``true`` (https://github.com/ansible-collections/community.general/issues/6028).
- gconftool2 - remove requirement of parameter ``value`` when ``state=absent`` (https://github.com/ansible-collections/community.general/issues/6028).
- gem - fix force parameter not being passed to gem command when uninstalling (https://github.com/ansible-collections/community.general/pull/5822).
- gem - fix hang due to interactive prompt for confirmation on specific version uninstall (https://github.com/ansible-collections/community.general/pull/5751).
- github_webhook - fix always changed state when no secret is provided (https://github.com/ansible-collections/community.general/pull/5994).
- gitlab_deploy_key - also update ``title`` and not just ``can_push`` (https://github.com/ansible-collections/community.general/pull/5888).
- gitlab_group_variables - fix dropping variables accidentally when GitLab introduced new properties (https://github.com/ansible-collections/community.general/pull/5667).
- gitlab_project_variables - fix dropping variables accidentally when GitLab introduced new properties (https://github.com/ansible-collections/community.general/pull/5667).
- gitlab_runner - fix ``KeyError`` on runner creation and update (https://github.com/ansible-collections/community.general/issues/6112).
- icinga2_host - fix the data structure sent to Icinga to make use of host templates and template vars (https://github.com/ansible-collections/community.general/pull/6286).
- idrac_redfish_command - allow user to specify ``resource_id`` for ``CreateBiosConfigJob`` to specify an exact manager (https://github.com/ansible-collections/community.general/issues/2090).
- influxdb_user - fix running in check mode when the user does not exist yet (https://github.com/ansible-collections/community.general/pull/6111).
- ini_file - make ``section`` parameter not required so it is possible to pass ``null`` as a value. This only was possible in the past due to a bug in ansible-core that now has been fixed (https://github.com/ansible-collections/community.general/pull/6404).
- interfaces_file - fix reading options in lines not starting with a space (https://github.com/ansible-collections/community.general/issues/6120).
- jail connection plugin - add ``inventory_hostname`` to vars under ``remote_addr``. This is needed for compatibility with ansible-core 2.13 (https://github.com/ansible-collections/community.general/pull/6118).
- jenkins_build - fix the logical flaw when deleting a Jenkins build (https://github.com/ansible-collections/community.general/pull/5514).
- jenkins_plugin - fix error due to undefined variable when updates file is not downloaded (https://github.com/ansible-collections/community.general/pull/6100).
- keycloak - improve error messages (https://github.com/ansible-collections/community.general/pull/6318).
- keycloak_client - fix accidental replacement of value for attribute ``saml.signing.private.key`` with ``no_log`` in wrong contexts (https://github.com/ansible-collections/community.general/pull/5934).
- keycloak_client_rolemapping - calculate ``proposed`` and ``after`` return values properly (https://github.com/ansible-collections/community.general/pull/5619).
- keycloak_client_rolemapping - remove only listed mappings with ``state=absent`` (https://github.com/ansible-collections/community.general/pull/5619).
- keycloak_user_federation - fixes federation creation issue. When a new federation was created and at the same time a default / standard mapper was also changed / updated the creation process failed as a bad None set variable led to a bad malformed url request (https://github.com/ansible-collections/community.general/pull/5750).
- keycloak_user_federation - fixes idempotency detection issues. In some cases the module could fail to properly detect already existing user federations because of a buggy seemingly superflous extra query parameter (https://github.com/ansible-collections/community.general/pull/5732).
- loganalytics callback plugin - adjust type of callback to ``notification``, it was incorrectly classified as ``aggregate`` before (https://github.com/ansible-collections/community.general/pull/5761).
- logdna callback plugin - adjust type of callback to ``notification``, it was incorrectly classified as ``aggregate`` before (https://github.com/ansible-collections/community.general/pull/5761).
- logstash callback plugin - adjust type of callback to ``notification``, it was incorrectly classified as ``aggregate`` before (https://github.com/ansible-collections/community.general/pull/5761).
- lxc_container - fix the arguments of the lxc command which broke the creation and cloning of containers (https://github.com/ansible-collections/community.general/issues/5578).
- lxd_* modules, lxd inventory plugin - fix TLS/SSL certificate validation problems by using the correct purpose when creating the TLS context (https://github.com/ansible-collections/community.general/issues/5616, https://github.com/ansible-collections/community.general/pull/6034).
- memset - fix memset urlerror handling (https://github.com/ansible-collections/community.general/pull/6114).
- nmcli - fix bond option ``xmit_hash_policy`` (https://github.com/ansible-collections/community.general/pull/6527).
- nmcli - fix change handling of values specified as an integer 0 (https://github.com/ansible-collections/community.general/pull/5431).
- nmcli - fix failure to handle WIFI settings when connection type not specified (https://github.com/ansible-collections/community.general/pull/5431).
- nmcli - fix improper detection of changes to ``wifi.wake-on-wlan`` (https://github.com/ansible-collections/community.general/pull/5431).
- nmcli - fixed idempotency issue for bridge connections. Module forced default value of ``bridge.priority`` to nmcli if not set; if ``bridge.stp`` is disabled nmcli ignores it and keep default (https://github.com/ansible-collections/community.general/issues/3216, https://github.com/ansible-collections/community.general/issues/4683).
- nmcli - fixed idempotency issue when module params is set to ``may_fail4=false`` and ``method4=disabled``; in this case nmcli ignores change and keeps their own default value ``yes`` (https://github.com/ansible-collections/community.general/pull/6106).
- nmcli - implemented changing mtu value on vlan interfaces (https://github.com/ansible-collections/community.general/issues/4387).
- nmcli - order is significant for lists of addresses (https://github.com/ansible-collections/community.general/pull/6048).
- nsupdate - fix zone lookup. The SOA record for an existing zone is returned as an answer RR and not as an authority RR (https://github.com/ansible-collections/community.general/issues/5817, https://github.com/ansible-collections/community.general/pull/5818).
- one_vm - avoid splitting labels that are ``None`` (https://github.com/ansible-collections/community.general/pull/5489).
- one_vm - fix syntax error when creating VMs with a more complex template (https://github.com/ansible-collections/community.general/issues/6225).
- onepassword lookup plugin - Changed to ignore errors from "op account get" calls. Previously, errors would prevent auto-signin code from executing (https://github.com/ansible-collections/community.general/pull/5942).
- onepassword_raw - add missing parameter to plugin documentation (https://github.com/ansible-collections/community.general/issues/5506).
- opkg - fix issue that ``force=reinstall`` would not reinstall an existing package (https://github.com/ansible-collections/community.general/pull/5705).
- opkg - fixes bug when using ``update_cache=true`` (https://github.com/ansible-collections/community.general/issues/6004).
- passwordstore lookup plugin - make compatible with ansible-core 2.16 (https://github.com/ansible-collections/community.general/pull/6447).
- pipx - fixed handling of ``install_deps=true`` with ``state=latest`` and ``state=upgrade`` (https://github.com/ansible-collections/community.general/pull/6303).
- portage - fix ``changed_use`` and ``newuse`` not triggering rebuilds (https://github.com/ansible-collections/community.general/issues/6008, https://github.com/ansible-collections/community.general/pull/6548).
- portage - update the logic for generating the emerge command arguments to ensure that ``withbdeps: false`` results in a passing an ``n`` argument with the ``--with-bdeps`` emerge flag (https://github.com/ansible-collections/community.general/issues/6451, https://github.com/ansible-collections/community.general/pull/6456).
- proxmox inventory plugin - fix bug while templating when using templates for the ``url``, ``user``, ``password``, ``token_id``, or ``token_secret`` options (https://github.com/ansible-collections/community.general/pull/5640).
- proxmox inventory plugin - handle tags delimited by semicolon instead of comma, which happens from Proxmox 7.3 on (https://github.com/ansible-collections/community.general/pull/5602).
- proxmox_disk - avoid duplicate ``vmid`` reference (https://github.com/ansible-collections/community.general/issues/5492, https://github.com/ansible-collections/community.general/pull/5493).
- proxmox_disk - fixed issue with read timeout on import action (https://github.com/ansible-collections/community.general/pull/5803).
- proxmox_disk - fixed possible issues with redundant ``vmid`` parameter (https://github.com/ansible-collections/community.general/issues/5492, https://github.com/ansible-collections/community.general/pull/5672).
- proxmox_nic - fixed possible issues with redundant ``vmid`` parameter (https://github.com/ansible-collections/community.general/issues/5492, https://github.com/ansible-collections/community.general/pull/5672).
- proxmox_tasks_info - remove ``api_user`` + ``api_password`` constraint from ``required_together`` as it causes to require ``api_password`` even when API token param is used (https://github.com/ansible-collections/community.general/issues/6201).
- puppet - handling ``noop`` parameter was not working at all, now it is has been fixed (https://github.com/ansible-collections/community.general/issues/6452, https://github.com/ansible-collections/community.general/issues/6458).
- redfish_utils - removed basic auth HTTP header when performing a GET on the service root resource and when performing a POST to the session collection (https://github.com/ansible-collections/community.general/issues/5886).
- redhat_subscription - do not ignore ``consumer_name`` and other variables if ``activationkey`` is specified (https://github.com/ansible-collections/community.general/issues/3486, https://github.com/ansible-collections/community.general/pull/5627).
- redhat_subscription - do not pass arguments to ``subscription-manager register`` for things already configured; now a specified ``rhsm_baseurl`` is properly set for subscription-manager (https://github.com/ansible-collections/community.general/pull/5583).
- redhat_subscription - do not use D-Bus for registering when ``environment`` is specified, so it possible to specify again the environment names for registering, as the D-Bus APIs work only with IDs (https://github.com/ansible-collections/community.general/pull/6319).
- redhat_subscription - try to unregister only when already registered when ``force_register`` is specified (https://github.com/ansible-collections/community.general/issues/6258, https://github.com/ansible-collections/community.general/pull/6259).
- redhat_subscription - use the right D-Bus options for environments when registering a CentOS Stream 8 system and using ``environment`` (https://github.com/ansible-collections/community.general/pull/6275).
- redhat_subscription, rhsm_release, rhsm_repository - cleanly fail when not running as root, rather than hanging on an interactive ``console-helper`` prompt; they all interact with ``subscription-manager``, which already requires to be run as root (https://github.com/ansible-collections/community.general/issues/734, https://github.com/ansible-collections/community.general/pull/6211).
- rhsm_release - make ``release`` parameter not required so it is possible to pass ``null`` as a value. This only was possible in the past due to a bug in ansible-core that now has been fixed (https://github.com/ansible-collections/community.general/pull/6401).
- rundeck module utils - fix errors caused by the API empty responses (https://github.com/ansible-collections/community.general/pull/6300)
- rundeck_acl_policy - fix ``TypeError - byte indices must be integers or slices, not str`` error caused by empty API response. Update the module to use ``module_utils.rundeck`` functions (https://github.com/ansible-collections/community.general/pull/5887, https://github.com/ansible-collections/community.general/pull/6300).
- rundeck_project - update the module to use ``module_utils.rundeck`` functions (https://github.com/ansible-collections/community.general/issues/5742) (https://github.com/ansible-collections/community.general/pull/6300)
- snap_alias - module would only recognize snap names containing letter, numbers or the underscore character, failing to identify valid snap names such as ``lxd.lxc`` (https://github.com/ansible-collections/community.general/pull/6361).
- splunk callback plugin - adjust type of callback to ``notification``, it was incorrectly classified as ``aggregate`` before (https://github.com/ansible-collections/community.general/pull/5761).
- sumologic callback plugin - adjust type of callback to ``notification``, it was incorrectly classified as ``aggregate`` before (https://github.com/ansible-collections/community.general/pull/5761).
- syslog_json callback plugin - adjust type of callback to ``notification``, it was incorrectly classified as ``aggregate`` before (https://github.com/ansible-collections/community.general/pull/5761).
- terraform - fix ``current`` workspace never getting appended to the ``all`` key in the ``workspace_ctf`` object (https://github.com/ansible-collections/community.general/pull/5735).
- terraform - fix ``terraform init`` failure when there are multiple workspaces on the remote backend and when ``default`` workspace is missing by setting ``TF_WORKSPACE`` environmental variable to the value of ``workspace`` when used (https://github.com/ansible-collections/community.general/pull/5735).
- terraform - fix broken ``warn()`` call (https://github.com/ansible-collections/community.general/pull/6497).
- terraform and timezone - slight refactoring to avoid linter reporting potentially undefined variables (https://github.com/ansible-collections/community.general/pull/5933).
- terraform module - disable ANSI escape sequences during validation phase (https://github.com/ansible-collections/community.general/pull/5843).
- tss lookup plugin - allow to download secret attachments. Previously, we could not download secret attachments but now use ``fetch_attachments`` and ``file_download_path`` variables to download attachments (https://github.com/ansible-collections/community.general/issues/6224).
- unixy callback plugin - fix plugin to work with ansible-core 2.14 by using Ansible's configuration manager for handling options (https://github.com/ansible-collections/community.general/issues/5600).
- unixy callback plugin - fix typo introduced when updating to use Ansible's configuration manager for handling options (https://github.com/ansible-collections/community.general/issues/5600).
- various plugins and modules - remove unnecessary imports (https://github.com/ansible-collections/community.general/pull/5940).
- vdo - now uses ``yaml.safe_load()`` to parse command output instead of the deprecated ``yaml.load()`` which is potentially unsafe. Using ``yaml.load()`` without explicitely setting a ``Loader=`` is also an error in pyYAML 6.0 (https://github.com/ansible-collections/community.general/pull/5632).
- vmadm - fix for index out of range error in ``get_vm_uuid`` (https://github.com/ansible-collections/community.general/pull/5628).
- xenorchestra inventory plugin - fix failure to receive objects from server due to not checking the id of the response (https://github.com/ansible-collections/community.general/pull/6227).
- xfs_quota - in case of a project quota, the call to ``xfs_quota`` did not initialize/reset the project (https://github.com/ansible-collections/community.general/issues/5143).
- xml - fixed a bug where empty ``children`` list would not be set (https://github.com/ansible-collections/community.general/pull/5808).
- yarn - fix ``global=true`` to check for the configured global folder instead of assuming the default (https://github.com/ansible-collections/community.general/pull/5829)
- yarn - fix ``global=true`` to not fail when `executable` wasn't specified (https://github.com/ansible-collections/community.general/pull/6132)
- yarn - fix ``state=absent`` not working with ``global=true`` when the package does not include a binary (https://github.com/ansible-collections/community.general/pull/5829)
- yarn - fix ``state=latest`` not working with ``global=true`` (https://github.com/ansible-collections/community.general/issues/5712).
- yarn - fixes bug where yarn module tasks would fail when warnings were emitted from Yarn. The ``yarn.list`` method was not filtering out warnings (https://github.com/ansible-collections/community.general/issues/6127).
- zfs_delegate_admin - zfs allow output can now be parsed when uids/gids are not known to the host system (https://github.com/ansible-collections/community.general/pull/5943).
- zypper - added handling of zypper exitcode 102. Changed state is set correctly now and rc 102 is still preserved to be evaluated by the playbook (https://github.com/ansible-collections/community.general/pull/6534).
- zypper - make package managing work on readonly filesystem of openSUSE MicroOS (https://github.com/ansible-collections/community.general/pull/5615).

community.grafana
~~~~~~~~~~~~~~~~~

- Fixed validate_certs missing parameter for --insecure option in grafana plugins
- URL encode issue in grafana_organization.py (method get_actual_org ) fixed.
- grafana_dashboard, now opens json files with utf-8 encoding (#191)

community.hashi_vault
~~~~~~~~~~~~~~~~~~~~~

- hashi_vault lookup - a term string with duplicate options would silently use the last value. The lookup now shows a warning on option duplication (https://github.com/ansible-collections/community.hashi_vault/issues/349).

community.mysql
~~~~~~~~~~~~~~~

- mysql module utils - use the connection arguments ``db`` instead of ``database`` and ``passwd`` instead of ``password`` when running with older mysql drivers (MySQLdb < 2.1.0 or PyMySQL < 1.0.0) (https://github.com/ansible-collections/community.mysql/pull/551).
- mysql_user - when revoke privs consists only of ``GRANT``, a 2nd revoke query is executed with empty privs to revoke that ended in an SQL exception (https://github.com/ansible-collections/community.mysql/pull/503).
- mysql_variables - add uppercase character pattern to regex to allow GLOBAL variables containing uppercase characters. This recognizes variable names used in Galera, for example, ``wsrep_OSU_method``, which breaks the normal pattern of all lowercase characters (https://github.com/ansible-collections/community.mysql/pull/501).

community.okd
~~~~~~~~~~~~~

- openshift_adm_groups_sync - initialize OpenshiftGroupSync attributes early to avoid Attribute error (https://github.com/openshift/community.okd/issues/155).
- openshift_auth - Review the way the discard process is working, add openshift algorithm to convert token to resource object name (https://github.com/openshift/community.okd/issues/176).

community.postgresql
~~~~~~~~~~~~~~~~~~~~

- postgresql_info - add support for non numeric extenstion version (https://github.com/ansible-collections/community.postgresql/issues/428).
- postgresql_info - when getting information about subscriptions, check the list of available columns in the pg_subscription table (https://github.com/ansible-collections/community.postgresql/issues/429).
- postgresql_pg_hba - fix ``changed`` return value for when ``overwrite`` is enabled (https://github.com/ansible-collections/community.postgresql/pull/378).
- postgresql_privs - fails with ``type=default_privs``, ``privs=ALL``, ``objs=ALL_DEFAULT`` (https://github.com/ansible-collections/community.postgresql/issues/373).
- postgresql_privs - fix a breaking change related to handling the ``password`` argument (https://github.com/ansible-collections/community.postgresql/pull/463).
- postgresql_privs - fix connect_params being ignored (https://github.com/ansible-collections/community.postgresql/issues/450).
- postgresql_privs - fix quoting of the ``schema`` parameter in SQL statements (https://github.com/ansible-collections/community.postgresql/pull/382).
- postgresql_privs - raise an error when the ``objs: ALL_IN_SCHEMA`` is used with a value of ``type`` that is not ``table``, ``sequence``, ``function`` or ``procedure`` (https://github.com/ansible-collections/community.postgresql/issues/379).
- postgresql_query - could crash under certain conditions because of a missing import to `psycopg2.extras` (https://github.com/ansible-collections/community.postgresql/issues/283).
- postgresql_set - avoid throwing ValueError for IP addresses and other values that may look like a number, but which are not (https://github.com/ansible-collections/community.postgresql/pull/422).
- postgresql_set - avoid wrong values for single-value parameters containing commas (https://github.com/ansible-collections/community.postgresql/pull/400).
- postgresql_user - properly close DB connections to prevent possible connection limit exhaustion (https://github.com/ansible-collections/community.postgresql/issues/431).

community.proxysql
~~~~~~~~~~~~~~~~~~

- proxysql_manage_config - Fix ``check_mode`` (https://github.com/ansible-collections/community.proxysql/pull/138).
- proxysql_query_rules_fast_routing - fix query parameter order, that prevents updating ``destination_hostgroup`` parameter (https://github.com/ansible-collections/community.proxysql/pull/108).
- proxysql_query_rules_fast_routing - remove unnecessary ``flagIN`` check, that makes it impossible to update the ``destination_hostgroup`` parameter (https://github.com/ansible-collections/community.proxysql/pull/108).
- roles/proxysql - Fix wait_for task when `proxysql_admin_bind_address` is overridden (https://github.com/ansible-collections/community.proxysql/pull/115).
- roles/proxysql - Missing proxysql_global_variables module parameters (https://github.com/ansible-collections/community.proxysql/pull/116).

community.routeros
~~~~~~~~~~~~~~~~~~

- api_info, api_modify - fix default and remove behavior for ``dhcp-options`` in path ``ip dhcp-client`` (https://github.com/ansible-collections/community.routeros/issues/148, https://github.com/ansible-collections/community.routeros/pull/154).
- api_modify - ``address-pool`` field of entries in API path ``ip dhcp-server`` is not required anymore (https://github.com/ansible-collections/community.routeros/pull/137).
- api_modify - ``ip route`` entry can be defined without the need of ``gateway`` field, which is correct for unreachable/blackhole type of routes (https://github.com/ansible-collections/community.routeros/pull/131).
- api_modify - ``queue interface`` path works now (https://github.com/ansible-collections/community.routeros/pull/131).
- api_modify - do not use ``name`` as a unique key in ``ip dns static`` (https://github.com/ansible-collections/community.routeros/issues/141).
- api_modify - fix handling of disabled keys on creation (https://github.com/ansible-collections/community.routeros/pull/154).
- api_modify, api_info - defaults corrected for fields in ``interface wireguard peers`` API path (https://github.com/ansible-collections/community.routeros/pull/144).
- api_modify, api_info - do not crash if router contains ``regexp`` DNS entries in ``ip dns static`` (https://github.com/ansible-collections/community.routeros/issues/141).
- api_modify, api_info - removed wrong field ``dynamic`` from API path ``ipv6 firewall address-list`` (https://github.com/ansible-collections/community.routeros/pull/133).
- api_modify, api_info - the default of the field ``ingress-filtering`` in ``interface bridge port`` is now ``true``, which is the default in ROS (https://github.com/ansible-collections/community.routeros/pull/125).
- command, facts - commands do not timeout in safe mode anymore (https://github.com/ansible-collections/community.routeros/pull/134).
- various plugins and modules - remove unnecessary imports (https://github.com/ansible-collections/community.routeros/pull/149).

community.sap_libs
~~~~~~~~~~~~~~~~~~

- fix a bug where some commands produces no output which cause to crash the module.
- fixes failures in sanity test for plugins/modules/sap_pyrfc.py
- fixes failures in sanity test for tests/unit/compat/builtins.py
- fixes failures in sanity test for tests/unit/plugins/modules/test_sap_system_facts.py
- fixes pipeline warnings
- modules - fix a "variable used before assignment" that cannot be reached but causes sanity test failures.
- sapcontrol_exec - This pr fixes problems on c(StartSystem), c(StopSystem), c(RestartSystem) which needs parameters they ca not provided by the parameters argument because of special format like c(waittimeout=1) without string quotes. This is caused by the suds module itself.

community.sops
~~~~~~~~~~~~~~

- action plugin helper - fix handling of deprecations for ansible-core 2.14.2 (https://github.com/ansible-collections/community.sops/pull/136).
- various plugins - remove unnecessary imports (https://github.com/ansible-collections/community.sops/pull/133).

community.vmware
~~~~~~~~~~~~~~~~

- scenario guides - Fix broken references (https://github.com/ansible-collections/community.vmware/issues/1610).
- various - Fix new pylint issues (https://github.com/ansible-collections/community.vmware/pull/1637).
- vmware_cluster_dpm - Fix an issue that the slider and the values of the host_power_action_rate works invertet in the vCenter
- vmware_cluster_drs - Fix drs_vmotion_rate so that the value corresponds to the vCenter UI. Previously, choosing 1 / 2 configured a migration threshold of 5 / 4 and vice versa (https://github.com/ansible-collections/community.vmware/pull/1542).
- vmware_cluster_info - Fix pylint issues (https://github.com/ansible-collections/community.vmware/issues/1618).
- vmware_cross_vc_clone - Fix SSL Thumbprint validation to ignore if destination_vcenter_validate_certs is false (https://github.com/ansible-collections/community.vmware/issues/1433).
- vmware_dvs_portgroup - Fix an issue when deleting portgroups (https://github.com/ansible-collections/community.vmware/issues/1522).
- vmware_dvswitch - Fix pylint issues (https://github.com/ansible-collections/community.vmware/issues/1618).
- vmware_dvswitch_lacp - Fix pylint issues (https://github.com/ansible-collections/community.vmware/issues/1618).
- vmware_dvswitch_uplink_pg - Fix pylint issues (https://github.com/ansible-collections/community.vmware/issues/1618).
- vmware_guest - Fix check mode (https://github.com/ansible-collections/community.vmware/issues/1272).
- vmware_guest - Fixed issue where custom attributes were not getting set on VM creation (https://github.com/ansible-collections/community.vmware/pull/1713)
- vmware_guest - Fixes adding new NVDIMM device issue by connecting to ESXi host (https://github.com/ansible-collections/community.vmware/issues/1644).
- vmware_guest_cross_vc_clone - Fix vim.fault.NotAuthenticated issue (https://github.com/ansible-collections/community.vmware/issues/1223).
- vmware_guest_cross_vc_clone - New parameter timeout in order to allow clone running longer than 1 hour
- vmware_guest_custom_attributes - Fixes assigning attributes to new VMs (https://github.com/ansible-collections/community.vmware/issues/1606).
- vmware_guest_disk - Fix wrong key in the documentation of the return values (https://github.com/ansible-collections/community.vmware/issues/1615)
- vmware_guest_instant_clone - Fix an issue with pyVmomi 8.0.0.1 (https://github.com/ansible-collections/community.vmware/issues/1555).
- vmware_host_lockdown - Fix issue `'VmwareLockdownManager' object has no attribute 'warn'` (https://github.com/ansible-collections/community.vmware/pull/1540).
- vmware_host_lockdown_exceptions - Avoid setting exception users to what they already are (https://github.com/ansible-collections/community.vmware/pull/1585).
- vmware_object_custom_attributes_info - Fixed an issue that has occurred an error if a custom attribute is the global type(https://github.com/ansible-collections/community.vmware/pull/1541).
- vmware_object_rename - Add missing quotation mark to error message (https://github.com/ansible-collections/community.vmware/issues/1633)
- vmware_portgroup - Fix pylint issues (https://github.com/ansible-collections/community.vmware/issues/1618).
- vmware_portgroup_info - Fix an issue that can fail the module after manually updating a portgroup through vCenter (https://github.com/ansible-collections/community.vmware/issues/1544).
- vmware_tag - Fix a performance issue during tag processing (https://github.com/ansible-collections/community.vmware/issues/1603).
- vmware_tools - Fix an issue with pyVmomi 8.0.0.1 (https://github.com/ansible-collections/community.vmware/issues/1578).
- vmware_vcenter_settings - Fix pylint issues (https://github.com/ansible-collections/community.vmware/issues/1618).
- vmware_vcenter_statistics - Fix pylint issues (https://github.com/ansible-collections/community.vmware/issues/1618).
- vmware_vsan_health_info - Fix return value (https://github.com/ansible-collections/community.vmware/pull/1706).

community.windows
~~~~~~~~~~~~~~~~~

- win_disk_facts - Fix issue when enumerating non-physical disks or disks without numbers - https://github.com/ansible-collections/community.windows/issues/474
- win_firewall_rule - fix problem in check mode with multiple ip addresses not in same order
- win_firewall_rule - fix program cannot be set to any on existing rules.
- win_partition - fix problem in auto assigning a drive letter should the user use either a, u, t or o as a drive letter
- win_psmodule - Fix missing AcceptLicense parameter that occurs when the pre-reqs have been installed - https://github.com/ansible-collections/community.windows/issues/487
- win_pssession_configuration - Fix parser error (Invalid JSON primitive: icrosoft.WSMan.Management.WSManConfigContainerElement)
- win_xml - Fixes the issue when no childnode is defined and will allow adding a new element to an empty element.
- win_zip - fix source appears to use backslashes as path separators issue when extracting Zip archve in non-Windows environment - https://github.com/ansible-collections/community.windows/issues/442

community.zabbix
~~~~~~~~~~~~~~~~

- The inventory script had insufficient error handling in case the Zabbix API provided an empty interfaces list. This bugfix checks for an exisiting interfaces element, then for the minimal length of 1 so that the first interface will only be accessed when it really exists in the api response. (https://github.com/ansible-collections/community.zabbix/issues/826)
- all modules - remove deprecation warnings for modules parameters related to zabbix-api when these parapmeters are not explicetely defined
- all roles and modules integration tests - replace deprecated include module whith include_tasks
- compatibility with ansible.netcommon 5.0.0
- treat sendto parameter in module zabbix_user according to real media type, do not rely on media name
- zabbix-proxy - updated to install correct sources for Debian arm64 family
- zabbix-proxy role - fix tags for postgresql task.
- zabbix_agent - Filter IPv6 addresses from list of IP as Zabbix host creation expects IPv4
- zabbix_agent - installation on Windows will no longer fail when zabbix_agent2 is used
- zabbix_agent and zabbix_proxy roles - fixed a bug whith ansible_python_interpreter not being set correctly in some corner cases
- zabbix_agent role - Fix MacOS install never executed because of the missing include_tasks "Darwin.yml" in the "main.yml" task file and wrong user permission on folder/files.
- zabbix_agent, zabbix_proxy and zabbix_server roles - make Ansible 2.14 compatible by removing warn parameter
- zabbix_agent, zabbix_proxy roles, all modules - make httpapi connection work with HTTP Basic Authorization
- zabbix_host - fix updating of host without interfaces
- zabbix_proxy - correctly provision tls_accept and tls_connect on Zabbix backend
- zabbix_proxy - do not set ServerPort config parameter which was removed in Zabbix 6.0
- zabbix_proxy - updated the datafiles_path fact for the zabbix_proxy and zabbix_server roles due to upstream change
- zabbix_server - move location of the fping(6) variables to distribution specific files (https://github.com/ansible-collections/community.zabbix/issues/812)
- zabbix_server - updated the datafiles_path fact for the zabbix_proxy and zabbix_server roles due to upstream change
- zabbix_server role Debian.yml task - remove warn: arg for shell module as the arg is deprecated since ansible-core above 2.13
- zabbix_user module - ability to specify several e-mail addresses in Zabbix User's  media
- zabbix_user_role module - creation of a User Role with Super Admin type

containers.podman
~~~~~~~~~~~~~~~~~

- Delete systemd files when container/pod is deleted
- Fix example in systemd generate module
- Fix expanduser in path for systemd generation
- Fix idempotency for labels in pods
- Fix podman load module for Podman 4
- Fix rerunning playbooks with generate_systemd --new
- Improve idempotency for devices mount of rootless podman
- Improve networks idempotency for v4
- Support passing multiple networks with params
- fix pod running status for older podman versions
- podman_container should ensure image by using os path if rootfs is used
- podman_systemd_generate - allow empty string for prefixes
- podman_unshare - Fix docs for podman_unshare become plugin

f5networks.f5_modules
~~~~~~~~~~~~~~~~~~~~~

- bigip_device_info - Included additional attributes for actions in ltm policy rules
- bigip_device_info - fix fqdn_up_interval and fqdn_down_interval to no longer cause string values not castable to int to raise an error
- bigip_device_info - fixed flaw in code to ignore fields that do not exist in the response for license info
- bigip_device_license - Add fix for a bug that caused infinite loop when the auth token expired
- bigip_monitor_dns - user can now pass route domain in the ip without error.
- bigip_monitor_external - user can now pass route domain in the ip without error.
- bigip_monitor_ftm - user can now pass route domain in the ip without error.
- bigip_monitor_gateway_icmp - user can now pass route domain in the ip without error.
- bigip_monitor_http - user can now pass route domain in the ip without error.
- bigip_monitor_https - user can now pass route domain in the ip without error.
- bigip_monitor_icmp - user can now pass route domain in the ip without error.
- bigip_monitor_ldap - user can now pass route domain in the ip without error.
- bigip_monitor_mysql - user can now pass route domain in the ip without error.
- bigip_monitor_oracle - user can now pass route domain in the ip without error.
- bigip_monitor_smtp - user can now pass route domain in the ip without error.
- bigip_monitor_tcp - user can now pass route domain in the ip without error.
- bigip_monitor_tcp_echo - user can now pass route domain in the ip without error.
- bigip_monitor_tcp_half_open - user can now pass route domain in the ip without error.
- bigip_monitor_udp - user can now pass route domain in the ip without error.
- bigip_software_image - fixed permission and ownership of the uploaded image file
- bigip_ucs - fixed permission and ownership of the ucs file
- bigip_ucs_fetch - fix a typo causing a bug that prevented ucs file from being encrypted with the provided passphrase

fortinet.fortios
~~~~~~~~~~~~~~~~

- Add required field for module log_fact;
- Fix invalid arguments in version_schemas;
- Fix issue of filter content could not contain spaces (#208);
- Fix issue of missing some options for monitor modules (#196);
- Fix list type arguments inconsistency;
- Fix list type not match issue;
- Fix runtime issue (#214);
- Fix sanity test errors in validate-modules test;
- Fix supports_check_mode issue for _info and _facts modules;
- Fix the issue that all the params with underscore cannot be set under member operation;
- Fix the login issue (#232);
- Fix the output path issue (#227);

google.cloud
~~~~~~~~~~~~

- Disk has been fixed to send the sourceSnapshot parameter.
- fix `gcp_compute` no longer being a valid name of the inventory plugin
- fix collection to work with Python 2.7
- gcp_cloudtasks_queue - was not functional before, and is now functional.
- gcp_compute_* - these resources use the correct selflink (www.googleapis.com) as the domain, no longer erroneously reporting changes after an execution.
- gcp_compute_backend_service - no longer erroneously reports changes after an execution for ``capacity_scaler``.
- gcp_compute_instance_info: fix incorrect documentation for filter which incorrectly pointed to the gcloud filter logic rather than the API (fixes #549)
- gcp_container_cluster - support GKE clusters greater than 1.19+, which cannot use basic-auth.
- gcp_crypto_key - skip_initial_version_creation defaults to the correct value.
- gcp_iam_role - now properly undeletes and recognizes soft deleted roles as absent.
- gcp_iam_role - update of a role is functional (GitHub
- gcp_spanner_database - recognize a non-existent resource as absent.
- gcp_storage_object - fix for correct version of dependency requirement.

hetzner.hcloud
~~~~~~~~~~~~~~

- hcloud_firewall - the deletion could fail if the firewall was referenced right before
- hcloud_server - Prevent backups from being disabled when undefined
- hcloud_server - Server locked after attaching to placement group
- hcloud_server - externally attached networks (using hcloud_server_network) were removed when not specified in the hcloud_server resource
- hcloud_server - fix backup window was given out as "None" instead of null
- hcloud_server_info - fix backup window was given out as "None" instead of null
- hcloud_volume - fix server name was given out as "None" instead of null if no server was attached
- hcloud_volume_info - fix server name was given out as "None" instead of null if no server was attached

infoblox.nios_modules
~~~~~~~~~~~~~~~~~~~~~

- Fixes Update A Record having multiple records with same name and different IP `#182 <https://github.com/infobloxopen/infoblox-ansible/pull/182>`_

junipernetworks.junos
~~~~~~~~~~~~~~~~~~~~~

- Fix enabled attribute implementation.
- Fix lldp_global_assertion.
- Fix sanity issues.
- Fix the snmp view and traps configuration.
- enable provider support for junos_scp and junos_package.
- fix diff to result when prepared diff exists.
- fix junos_security_zones facts gathering when we have single interface configured.
- fix the implementation of disabling interface.
- module should return with failure when rollback is 0 and device is not reachable.
- revert diff mode to default.

kubernetes.core
~~~~~~~~~~~~~~~

- Fix dry_run logic - Pass the value dry_run=All instead of dry_run=True to the client, add conditional check on kubernetes client version as this feature is supported only for kubernetes >= 18.20.0 (https://github.com/ansible-collections/kubernetes.core/pull/561).
- Fix kubeconfig parameter when multiple config files are provided (https://github.com/ansible-collections/kubernetes.core/issues/435).
- Helm - Fix issue with alternative kubeconfig provided with validate_certs=False (https://github.com/ansible-collections/kubernetes.core/issues/538).
- Various modules and plugins - use vendored version of ``distutils.version`` instead of the deprecated Python standard library ``distutils`` (https://github.com/ansible-collections/kubernetes.core/pull/314).
- add missing documentation for filter plugin kubernetes.core.k8s_config_resource_name (https://github.com/ansible-collections/kubernetes.core/issues/558).
- common - Ensure the label_selectors parameter of _wait_for method is optional.
- common - handle ``aliases`` passed from inventory and lookup plugins.
- helm_template - evaluate release_values after values_files, insuring highest precedence (now same behavior as in helm module). (https://github.com/ansible-collections/kubernetes.core/pull/348)
- import exception from ``kubernetes.client.rest``.
- k8s - Fix issue with check_mode when using server side apply (https://github.com/ansible-collections/kubernetes.core/issues/547).
- k8s - Fix issue with server side apply with kubernetes release '25.3.0' (https://github.com/ansible-collections/kubernetes.core/issues/548).
- k8s_cp - add support for check_mode (https://github.com/ansible-collections/kubernetes.core/issues/380).
- k8s_drain - fix error caused by accessing an undefined variable when pods have local storage (https://github.com/ansible-collections/kubernetes.core/issues/292).
- k8s_info - don't wait on empty List resources (https://github.com/ansible-collections/kubernetes.core/pull/253).
- k8s_info - fix issue when module returns successful true after the resource cache has been established during periods where communication to the api-server is not possible (https://github.com/ansible-collections/kubernetes.core/issues/508).
- k8s_log - Fix module traceback when no resource found (https://github.com/ansible-collections/kubernetes.core/issues/479).
- k8s_log - fix exception raised when the name is not provided for resources requiring. (https://github.com/ansible-collections/kubernetes.core/issues/514)
- k8s_scale - fix waiting on statefulset when scaled down to 0 replicas (https://github.com/ansible-collections/kubernetes.core/issues/203).
- module_utils.common - change default opening mode to read-bytes to avoid bad interpretation of non ascii characters and strings, often present in 3rd party manifests.
- module_utils/k8s/client.py - fix issue when trying to authenticate with host, client_cert and client_key parameters only.
- remove binary file from k8s_cp test suite (https://github.com/ansible-collections/kubernetes.core/pull/298).
- use resource prefix when finding resource and apiVersion is v1 (https://github.com/ansible-collections/kubernetes.core/issues/351).

lowlydba.sqlserver
~~~~~~~~~~~~~~~~~~

- Added missing mapping for UseDestinationDefaultDirectories (https://github.com/lowlydba/lowlydba.sqlserver/pull/153)
- Fixes to incorrect variable reference in Login module (https://github.com/lowlydba/lowlydba.sqlserver/pull/161)
- Removed default value for KeepCDC to fix compatability with SQL MI (https://github.com/lowlydba/lowlydba.sqlserver/pull/153)
- Removed default value for ReplaceDbNameInFile to fix compatability with SQL MI (https://github.com/lowlydba/lowlydba.sqlserver/pull/148)
- Removed default value for UseDestinationDefaultDirectories to fix compatability with SQL MI (https://github.com/lowlydba/lowlydba.sqlserver/pull/153)
- Removed default value for reuse_source_folder_structure to fix compatability with SQL MI (https://github.com/lowlydba/lowlydba.sqlserver/pull/145)
- Removed the default value for xp_dirtree to allow compatibility with Azure SQL Mangaed instances (https://github.com/lowlydba/lowlydba.sqlserver/pull/141)

netapp.ontap
~~~~~~~~~~~~

- na_ontap_active_directory - updated doc as only ZAPI is supported at present, force an error with use_rest always.
- na_ontap_aggregate - allow adding disks before trying to offline aggregate.
- na_ontap_aggregate - fix ``service_state`` option skipped if its set to offline in create.
- na_ontap_aggregate - try to offline aggregate when disk add operation is in progress in ZAPI.
- na_ontap_cg_snapshot - updated doc with deprecation warning as it is a ZAPI only module.
- na_ontap_cifs - throw error if set ``unix_symlink`` in ZAPI.
- na_ontap_cifs - throw error if used options that require recent ONTAP version.
- na_ontap_cifs_server - fix ``service_state`` is stopped when trying to modify cifs server in REST.
- na_ontap_export_policy - fix cannot delete export policy if ``from_name`` option is set.
- na_ontap_file_directory_policy - updated doc with deprecation warning as it is a ZAPI only module.
- na_ontap_file_security_permissions - error if more than one desired ACLs has same user, access, access_control and apply_to.
- na_ontap_file_security_permissions - fix TypeError when current acls is None.
- na_ontap_file_security_permissions - fix idempotency issue on ``acls.propagation_mode`` option.
- na_ontap_file_security_permissions - updated notes to indicate ONTAP 9.9.1 or later is required.
- na_ontap_file_security_permissions_acl - fix idempotent issue on ``propagation_mode`` option.
- na_ontap_file_security_permissions_acl - updated notes to indicate ONTAP 9.9.1 or later is required.
- na_ontap_interface - fix cannot set ``location.node.name`` and ``location.home_node.name`` error when creating or modifying fc interface.
- na_ontap_interface - fix idempotency issue when ``home_port`` not set in creating FC interface.
- na_ontap_interface - fix incorrect warning raised when try to rename interface.
- na_ontap_interface - fix unexpected argument error with ``ipspace`` when trying to get fc interface.
- na_ontap_ipspace - fix cannot delete ipspace if ``from_ipspace`` is present.
- na_ontap_iscsi_security - error module if use_rest never is set.
- na_ontap_iscsi_security - fix KeyError on ``outbound_username`` option.
- na_ontap_ldap_client - fix KeyError on ``name`` in ZAPI.
- na_ontap_ldap_client - fix duplicate entry error when used cluster vserver in REST.
- na_ontap_qos_adaptive_policy_group - rename group when from_name is present and state is present.
- na_ontap_qos_policy_group - one occurrence of msg missing in call to fail_json.
- na_ontap_qtree - fix cannot get current qtree if enclosed in curly braces.
- na_ontap_qtree - ignore job entry does not exist error when creating qtree with REST to bypass ONTAP issue with FSx.
- na_ontap_quota_policy - updated doc with deprecation warning as it is a ZAPI only module.
- na_ontap_quotas - fix default tree quota rule gets modified when ``quota_target`` is set in REST.
- na_ontap_quotas - fix duplicate entry error when trying to add quota rule in REST.
- na_ontap_quotas - fix entry does not exist error when trying to modify quota status in REST.
- na_ontap_quotas - fix user/group quota rule without qtree gets modified when ``qtree`` is set.
- na_ontap_quotas - ignore job entry does not exist error when creating quota with REST to bypass ONTAP issue with FSx.
- na_ontap_rest_info - fix field issue with private/cli and support/autosupport/check APIs.
- na_ontap_s3_groups - fix cannot modify ``policies`` if not configured in create.
- na_ontap_s3_groups - fix error when current s3 groups has no users configured.
- na_ontap_san_create - Role documentation correct to from nas to san
- na_ontap_security_certificates - fix duplicate entry error when ``vserver`` option is set with admin vserver.
- na_ontap_security_config - fix error on specifying protocol version ``TLSv1.1`` when fips is enabled.
- na_ontap_security_ipsec_policy - fix KeyError on ``authentication_method``.
- na_ontap_security_ipsec_policy - fix cannot get current security IPsec policy with ipspace.
- na_ontap_security_key_manager - requires 9.7+ to work with REST.
- na_ontap_snapmirror - Added option ``identity_preservation`` support from ONTAP 9.11.1 in REST.
- na_ontap_snapmirror - error if identity_preservation set in ZAPI.
- na_ontap_snapmirror - fix invalid value error for return_timeout, modified the value to 120 seconds.
- na_ontap_snapmirror_policy - deleting all retention rules would trigger an error when the existing policy requires at least one rule.
- na_ontap_snapmirror_policy - fix cannot disable ``is_network_compression_enabled`` in REST.
- na_ontap_snapmirror_policy - fix desired policy type not configured in cli with REST.
- na_ontap_snapmirror_policy - fixed idempotency issue on ``identity_preservation`` option when using REST.
- na_ontap_snapmirror_policy - index error on rules with ONTAP 9.12.1 as not all fields are present.
- na_ontap_snapshot - fix cannot modify ``snapmirror_label``, ``expiry_time`` and ``comment`` if not configured in create.
- na_ontap_svm - skip modify validation when trying to delete svm.
- na_ontap_svm_options - updated doc with deprecation warning as it is a ZAPI only module.
- na_ontap_user - fix KeyError vserver in ZAPI.
- na_ontap_user_role - fix AttributeError 'NetAppOntapUserRole' object has no attribute 'name'.
- na_ontap_user_role - fix KeyError on ``vserver``, ``command_directory_name`` in ZAPI and ``path``, ``query`` in REST.
- na_ontap_user_role - fix duplicate entry error in ZAPI.
- na_ontap_user_role - fix entry does not exist error when trying to delete privilege in REST.
- na_ontap_user_role - report error when command/command directory path set in REST for ONTAP earlier versions.
- na_ontap_volume - fix error when try to unmount volume and modify snaplock attribute.
- na_ontap_volume - fix idempotent issue when try to offline and modify other volume options.
- na_ontap_volume -- fixed bug preventing unmount and taking a volume off line at the same time
- na_ontap_volume_efficiency - fix idempotent issue when state is absent and efficiency options are set in ZAPI.
- na_ontap_vserver_audit - Added ``log_path`` option in modify.
- na_ontap_vserver_audit - fix invalid field value error of log retention count and duration.

netapp_eseries.santricity
~~~~~~~~~~~~~~~~~~~~~~~~~

- netapp_eseries.santricity.na_santricity_mgmt_interface - Add the ability to configure DNS, NTP and SSH separately from management interfaces.
- netapp_eseries.santricity.nar_santricity_host - Fix default MTU value for NVMe RoCE.
- netapp_eseries.santricity.nar_santricity_management - Add tasks to set DNS, NTP and SSH globally separately from management interfaces.

netbox.netbox
~~~~~~~~~~~~~

- Fix partial updates of custom_fields [#944](https://github.com/netbox-community/ansible_modules/pull/944)
- nb_inventory - Fix nb_inventory group_by by site_group [#952](https://github.com/netbox-community/ansible_modules/pull/952)
- nb_inventory - Fix site_group in inventory plugin [#872](https://github.com/netbox-community/ansible_modules/pull/872)
- nb_inventory - Make sure inventory works with ansible < 2.11 [#861](https://github.com/netbox-community/ansible_modules/pull/861)
- nb_inventory - Raise exception on missing packaging [#900](https://github.com/netbox-community/ansible_modules/pull/900)
- nb_lookup - Fix pynetbox 7.0.1 compatibility [#934](https://github.com/netbox-community/ansible_modules/pull/934)
- netbox_cable - Fix NetBox 3.3 compatibility [#938](https://github.com/netbox-community/ansible_modules/pull/938)
- netbox_cable - Fix idempotency [#990](https://github.com/netbox-community/ansible_modules/pull/990)
- netbox_location - Add multiple filter options to make sure we find the unique location [#963](https://github.com/netbox-community/ansible_modules/pull/963)
- netbox_virtual_machine - Fix idempotency with virtual machine and NetBox 3.0 [#859](https://github.com/netbox-community/ansible_modules/pull/859)
- netbox_webhook - Fix conditions bug [#926](https://github.com/netbox-community/ansible_modules/pull/926)

ngine_io.vultr
~~~~~~~~~~~~~~

- iventory - Fixed ``allowed_bandwidth_gb`` to be returned as float (https://github.com/ngine-io/ansible-collection-vultr/pull/35).
- vultr_server - Fixed ``allowed_bandwidth_gb`` to be returned as float (https://github.com/ngine-io/ansible-collection-vultr/pull/35).
- vultr_server_baremetal - Fixed ``allowed_bandwidth_gb`` to be returned as float (https://github.com/ngine-io/ansible-collection-vultr/pull/35).

openvswitch.openvswitch
~~~~~~~~~~~~~~~~~~~~~~~

- Fix galaxy version issue when installing this collection.

ovirt.ovirt
~~~~~~~~~~~

- Remove the 'warn:' argument (https://github.com/oVirt/ovirt-ansible-collection/pull/627).
- cluster_upgrade - Add default random uuid to engine_correlation_id (https://github.com/oVirt/ovirt-ansible-collection/pull/624).
- cluster_upgrade - Fix the engine_correlation_id location (https://github.com/oVirt/ovirt-ansible-collection/pull/637).
- engine_setup - Remove provision_docker from tests (https://github.com/oVirt/ovirt-ansible-collection/pull/677).
- filters - Fix ovirtvmipsv4 with attribute and network (https://github.com/oVirt/ovirt-ansible-collection/pull/607).
- filters - Fix ovirtvmipsv4 with filter to list (https://github.com/oVirt/ovirt-ansible-collection/pull/609).
- he-setup - Log the output sent to the serial console of the HostedEngineLocal VM to a file on the host, to allow diagnosing failures in that stage (https://github.com/oVirt/ovirt-ansible-collection/pull/664).
- he-setup - Run virt-install with options more suitable for debugging (https://github.com/oVirt/ovirt-ansible-collection/pull/664).
- he-setup - recently `virsh net-destroy default` doesn't delete the `virbr0`, so we need to delete it expicitly (https://github.com/oVirt/ovirt-ansible-collection/pull/661).
- hosted_engine_setup - Vdsm now uses -n flag for all qemu-img convert calls (https://github.com/oVirt/ovirt-ansible-collection/pull/682).
- image_template - Add template_bios_type (https://github.com/oVirt/ovirt-ansible-collection/pull/620).
- info modules - Bump the deprecation version of fetch_nested and nested_attributes (https://github.com/oVirt/ovirt-ansible-collection/pull/610).
- info modules - Use dynamic collection name instead of ovirt.ovirt for deprecation warning (https://github.com/oVirt/ovirt-ansible-collection/pull/653).
- module_utils - replace `getargspec` with `getfullargspec` to support newer python 3.y versions (https://github.com/oVirt/ovirt-ansible-collection/pull/663).
- ovirt_cluster_info - Fix example patter (https://github.com/oVirt/ovirt-ansible-collection/pull/684).
- ovirt_host - Fix kernel_params elemets type (https://github.com/oVirt/ovirt-ansible-collection/pull/608).
- ovirt_host - Fix refreshed state action (https://github.com/oVirt/ovirt-ansible-collection/pull/687).
- ovirt_host - Wait for host to be in result state during upgrade (https://github.com/oVirt/ovirt-ansible-collection/pull/621)
- ovirt_nic - Add network_filter_parameters (https://github.com/oVirt/ovirt-ansible-collection/pull/623).

purestorage.flasharray
~~~~~~~~~~~~~~~~~~~~~~

- purefa - Remove unneeded REST version check as causes issues with REST mismatches
- purefa.py - Fix issue in Purity versions numbers that are for development versions
- purefa_ds - Fixed dict syntax error
- purefa_host - Fixed parameter name
- purefa_info - Fiexed issue with DNS reporting in Purity//FA 6.4.0 with non-FA-File system
- purefa_info - Fix REST response backwards compatibility issue for array capacity REST response
- purefa_info - Fix missing FC target ports for host
- purefa_info - Fixed error in policies subsection due to API issue
- purefa_info - Fixed race condition with protection groups
- purefa_info - Resolves issue in AC environment where REST v2 host list mismatches REST v1 due to remote hosts.
- purefa_info - Resolves issue with destroyed pgroup snapshot on an offload target not have a time remaining value
- purefa_network - Resolves network port setting idempotency issue
- purefa_pg - Fixed issue where volumes could not be added to a PG when one of the arrays was undergoing a failover.
- purefa_pg - Resolves issue with destroyed pgroup snapshot on an offload target not have a time remaining value
- purefa_pgsched - Fix error when setting schedule for pod based protection group
- purefa_policy - Fixed missing parameters in function calls
- purefa_smtp - Fix parameter name
- purefa_snap - Fixed issue system generated suffixes not being allowed and removed unnecessary warning message.
- purefa_vg - Fix issue with VG creation on newer Purity versions
- purefa_vg - Fix typeerror when using newer Purity versions and setting VG QoS
- purefa_volume - Ensure promotion_stateus is returned correctly on creation
- purefa_volume - Fix bug when overwriting volume using invalid parmaeters
- purefa_volume - Fixed idempotency bug when creating volumes with QoS
- purefa_volume - Fixed issue with promotion status not being called correctly

purestorage.flashblade
~~~~~~~~~~~~~~~~~~~~~~

- purefa_info - Fixed issue when more than 10 buckets have lifecycle rules.
- purefb_s3user - Fix incorrect response when bad key/secret pair provided for new user

purestorage.fusion
~~~~~~~~~~~~~~~~~~

- fusion_api_client - error messages now mostly handled by errors_py
- fusion_array - correct required parameters
- fusion_hap - could not delete host access policy without iqn option. Now it needs only name option for deletion
- fusion_hap - display name has now default value set to the value of name
- fusion_hap - error messages now mostly handled by errors_py
- fusion_hap - uppercase names were not supported. Now uppercase names are allowed
- fusion_hw - correct required parameters
- fusion_info - Fixed issue with storage endpoint dict formatting
- fusion_info - fixes typo in output 'appiiances' -> 'appliances'
- fusion_info - network_interface_groups subset returned nothing. Now it collects the same information as nigs subset
- fusion_info - placements subset returned nothing. Now it collects the same information as placement_groups subset
- fusion_nig - add missing 'availability_zone' format param in error message
- fusion_nig - error messages now mostly handled by errors_py
- fusion_pg - Add missing 'region' parameter
- fusion_pg - correct required parameters
- fusion_pg - create_pg always broke runtime. Now it executes and creates placement group successfully
- fusion_pg - error messages now mostly handled by errors_py
- fusion_pp - correct required parameters
- fusion_pp - error messages now mostly handled by errors_py
- fusion_pp - fix call to parse_minutes where we were missing a required argument
- fusion_sc - correct required parameters
- fusion_sc - error messages now mostly handled by errors_py
- fusion_se - add missing 'availability_zone' format param in error message
- fusion_se - error messages now mostly handled by errors_py
- fusion_se - fix call in get_nifg where provider_subnet was used instead of network_interface_group_name
- fusion_ss - allow updating hardware types, correct required parameters
- fusion_ss - error messages now mostly handled by errors_py
- fusion_tenant - error messages now mostly handled by errors_py
- fusion_tn - Add missing 'region' parameter
- fusion_tn - fix attribute error
- fusion_ts - add missing 'tenant' format param in error message
- fusion_ts - error messages now mostly handled by errors_py
- fusion_volume - error messages now mostly handled by errors_py
- fusion_volume - protection policy can now be unset by using '' as name

theforeman.foreman
~~~~~~~~~~~~~~~~~~

- activation_key - properly fetch *all* repositories when managing content overrides (https://bugzilla.redhat.com/show_bug.cgi?id=2134605)
- auth_sources_ldap role - don't assume ``account`` and ``account_password`` are set, they are documented as optional
- auth_sources_ldap role, compute_resources role, repositories role - do not log loop data when it contains sensitive data (https://bugzilla.redhat.com/show_bug.cgi?id=2183357)
- content_export_* - increase task timeout to 12h as export tasks can be time intensive (https://bugzilla.redhat.com/show_bug.cgi?id=2162678)
- redhat_manifest - properly report http errors (https://github.com/theforeman/foreman-ansible-modules/issues/1497)
- repository_sync - report an error instead of syncing the whole product when the repository could not be found

vmware.vmware_rest
~~~~~~~~~~~~~~~~~~

- Allow filters with the space (See: https://github.com/ansible-collections/vmware.vmware_rest/issues/362).
- Handle spaces and special characters in resource names for lookup plugins (See: https://github.com/ansible-collections/vmware.vmware_rest/issues/356).

vultr.cloud
~~~~~~~~~~~

- instance - An error that caused the start script not to be processed has been fixed. (https://github.com/vultr/ansible-collection-vultr/issues/49)
- instance - Fixed an issue when deleting an instance in locked state. (https://github.com/vultr/ansible-collection-vultr/pull/68)
- instance_info - The problem that the module was missing in the runtime action group has been fixed.
- inventory - Fixed the issue instance tags were not returned (https://github.com/vultr/ansible-collection-vultr/issues/69)

vyos.vyos
~~~~~~~~~

- bgp_global - changed to use `neighbor.password` rather than `neighbor.address` (https://github.com/ansible-collections/vyos.vyos/issues/304).
- vyos_command - Run commands at least once even when retries is set to 0 (https://github.com/ansible-collections/cisco.nxos/issues/607).

Known Issues
------------

Ansible-core
~~~~~~~~~~~~

- ansible-test - Additional configuration may be required for certain container host and container combinations. Further details are available in the testing documentation.
- ansible-test - Custom containers with ``VOLUME`` instructions may be unable to start, when previously the containers started correctly. Remove the ``VOLUME`` instructions to resolve the issue. Containers with this condition will cause ``ansible-test`` to emit a warning.
- ansible-test - Systems with Podman networking issues may be unable to run containers, when previously the issue went unreported. Correct the networking issues to continue using ``ansible-test`` with Podman.
- ansible-test - Unit tests for collections do not support ``pytest`` assertion rewriting on Python 2.7.
- ansible-test - Using Docker on systems with SELinux may require setting SELinux to permissive mode. Podman should work with SELinux in enforcing mode.
- dnf5 - The DNF5 package manager currently does not provide all functionality to ensure feature parity between the existing ``dnf`` and the new ``dnf5`` module. As a result the following ``dnf5`` options are effectively a no-op: ``cacheonly``, ``enable_plugin``, ``disable_plugin`` and ``lock_timeout``.

cisco.meraki
~~~~~~~~~~~~

- meraki_network - Updated documentation for `local_status_page_enabled` and `remote_status_page_enabled` as these no longer work.

community.docker
~~~~~~~~~~~~~~~~

- The modules and plugins using the vendored code from Docker SDK for Python currently do not work with requests 2.29.0 and/or urllib3 2.0.0. The same is currently true for the latest version of Docker SDK for Python itself (https://github.com/ansible-collections/community.docker/issues/611, https://github.com/ansible-collections/community.docker/pull/612).
- docker_api connection plugin - does **not work with TCP TLS sockets**! This is caused by the inability to send an ``close_notify`` TLS alert without closing the connection with Python's ``SSLSocket`` (https://github.com/ansible-collections/community.docker/issues/605, https://github.com/ansible-collections/community.docker/pull/621).
- docker_container_exec - does **not work with TCP TLS sockets** when the ``stdin`` option is used! This is caused by the inability to send an ``close_notify`` TLS alert without closing the connection with Python's ``SSLSocket`` (https://github.com/ansible-collections/community.docker/issues/605, https://github.com/ansible-collections/community.docker/pull/621).

community.routeros
~~~~~~~~~~~~~~~~~~

- api_modify - when limits for entries in ``queue tree`` are defined as human readable - for example ``25M`` -, the configuration will be correctly set in ROS, but the module will indicate the item is changed on every run even when there was no change done. This is caused by the ROS API which returns the number in bytes - for example ``25000000`` (which is inconsistent with the CLI behavior). In order to mitigate that, the limits have to be defined in bytes (those will still appear as human readable in the ROS CLI) (https://github.com/ansible-collections/community.routeros/pull/131).
- api_modify, api_info - ``routing ospf area``, ``routing ospf area range``, ``routing ospf instance``, ``routing ospf interface-template`` paths are not fully implemented for ROS6 due to the significant changes between ROS6 and ROS7 (https://github.com/ansible-collections/community.routeros/pull/131).

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- idrac_firmware - Issue(249879) - Firmware update of iDRAC9-based Servers fails if SOCKS proxy with authentication is used.
- idrac_os_deployment- Issue(260496) - OS installation will support only NFS and CIFS share to store the custom ISO in the destination_path, HTTP/HTTPS/FTP not supported
- idrac_redfish_storage_contoller - Issue(256164) - If incorrect value is provided for one of the attributes in the provided attribute list for controller configuration, then this module does not exit with error.
- idrac_user - Issue(192043) The module may error out with the message ``Unable to perform the import or export operation because there are pending attribute changes or a configuration job is in progress``. Wait for the job to complete and run the task again.
- idrac_user - Issue(192043) The module may error out with the message ``unable to perform the import or export operation because there are pending attribute changes or a configuration job is in progress``. Wait for the job to complete and run the task again.
- ome_application_alerts_syslog - Issue(215374) - The module does not provide a proper error message if the destination_address is more than 255 characters.
- ome_device_network_services - Issue(212681) - The module does not provide a proper error message if unsupported values are provided for the following parameters- port_number, community_name, max_sessions, max_auth_retries, and idle_timeout.
- ome_device_network_services - Issue(212681) - The module does not provide a proper error message if unsupported values are provided for the parameters- port_number, community_name, max_sessions, max_auth_retries, and idle_timeout.
- ome_device_power_settings - Issue(212679) - The module displays the following message if the value provided for the parameter ``power_cap`` is not within the supported range of 0 to 32767, ``Unable to complete the request because PowerCap does not exist or is not applicable for the resource URI.``
- ome_inventory - Issue(256257) - All hosts are not retrieved for ``Modular System`` group and corresponding child groups.
- ome_inventory - Issue(256589) - All hosts are not retrieved for ``Custom Groups`` group and corresponding child groups.
- ome_inventory - Issue(256593) - All hosts are not retrieved for ``PLUGIN GROUPS`` group and corresponding child groups.
- ome_smart_fabric_uplink - Issue(186024) - Despite the module supported by OpenManage Enterprise Modular, it does not allow the creation of multiple uplinks of the same name. If an uplink is created using the same name as an existing uplink, the existing uplink is modified.
- ome_smart_fabric_uplink - Issue(186024) - The module does not allow the creation of multiple uplinks of the same name even though it is supported by OpenManage Enterprise Modular. If an uplink is created using the same name as an existing uplink, the existing uplink is modified.

New Plugins
-----------

Filter
~~~~~~

- ansible.builtin.commonpath - gets the common path
- ansible.builtin.normpath - Normalize a pathname
- community.crypto.openssl_csr_info - Retrieve information from OpenSSL Certificate Signing Requests (CSR)
- community.crypto.openssl_privatekey_info - Retrieve information from OpenSSL private keys
- community.crypto.openssl_publickey_info - Retrieve information from OpenSSL public keys in PEM format
- community.crypto.split_pem - Split PEM file contents into multiple objects
- community.crypto.x509_certificate_info - Retrieve information from X.509 certificates in PEM format
- community.crypto.x509_crl_info - Retrieve information from X.509 CRLs in PEM format

Inventory
~~~~~~~~~

- dellemc.openmanage.ome_inventory - Group inventory plugin on OpenManage Enterprise.
- vultr.cloud.vultr - Retrieves list of instances via Vultr v2 API

Lookup
~~~~~~

- amazon.aws.aws_collection_constants - expose various collection related constants
- community.general.merge_variables - merge variables with a certain suffix
- community.hashi_vault.vault_list - Perform a list operation against HashiCorp Vault

New Modules
-----------

Ansible-core
~~~~~~~~~~~~

Lib
^^^

Ansible.Modules
...............

- ansible.builtin.deb822_repository - Add and remove deb822 formatted repositories
- ansible.builtin.dnf5 - Manages packages with the I(dnf5) package manager

amazon.aws
~~~~~~~~~~

- amazon.aws.backup_plan - Manage AWS Backup Plans
- amazon.aws.backup_plan_info - Describe AWS Backup Plans
- amazon.aws.backup_restore_job_info - List information about backup restore jobs
- amazon.aws.backup_selection - Create, delete and modify AWS Backup selection
- amazon.aws.backup_selection_info - Describe AWS Backup Selections
- amazon.aws.backup_tag - Manage tags on backup plan, backup vault, recovery point
- amazon.aws.backup_tag_info - List tags on AWS Backup resources
- amazon.aws.backup_vault - Manage AWS Backup Vaults
- amazon.aws.backup_vault_info - Describe AWS Backup Vaults
- amazon.aws.lambda_layer - Creates an AWS Lambda layer or deletes an AWS Lambda layer version
- amazon.aws.lambda_layer_info - List lambda layer or lambda layer versions

check_point.mgmt
~~~~~~~~~~~~~~~~

- check_point.mgmt.cp_mgmt_abort_get_interfaces - Attempt to abort an on-going "get-interfaces" operation.
- check_point.mgmt.cp_mgmt_access_layers - Manages ACCESS LAYERS resource module
- check_point.mgmt.cp_mgmt_access_point_name - Manages access-point-name objects on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_access_point_name_facts - Get access-point-name objects facts on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_add_repository_package - Add the software package to the central repository.
- check_point.mgmt.cp_mgmt_add_updatable_object - Import an updatable object from the repository to the management server.
- check_point.mgmt.cp_mgmt_checkpoint_host - Manages checkpoint-host objects on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_checkpoint_host_facts - Get checkpoint-host objects facts on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_delete_repository_package - Delete the repository software package from the central repository.
- check_point.mgmt.cp_mgmt_delete_updatable_object - Delete existing object using object name or uid.
- check_point.mgmt.cp_mgmt_dynamic_global_network_object - Manages dynamic-global-network-object objects on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_dynamic_global_network_object_facts - Get dynamic-global-network-object objects facts on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_export_management - Export the primary Security Management Server database or the primary Multi-Domain Server database or the single Domain database and the applicable Check Point configuration.
- check_point.mgmt.cp_mgmt_export_smart_task - Export SmartTask to a file.
- check_point.mgmt.cp_mgmt_get_attachment - Retrieves a packet capture or blob data, according to the attributes of a log record.
- check_point.mgmt.cp_mgmt_get_interfaces - Get physical interfaces with or without their topology from a Gaia Security Gateway or Cluster.
- check_point.mgmt.cp_mgmt_gsn_handover_group - Manages gsn-handover-group objects on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_gsn_handover_group_facts - Get gsn-handover-group objects facts on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_ha_full_sync - Perform full sync from active server to standby peer.
- check_point.mgmt.cp_mgmt_hosts - Manages HOSTS resource module
- check_point.mgmt.cp_mgmt_https_layer - Manages https-layer objects on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_https_layer_facts - Get https-layer objects facts on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_import_management - Import the primary Security Management Server database or the primary Multi-Domain Server database or the single Domain database and the applicable Check Point configuration.
- check_point.mgmt.cp_mgmt_import_smart_task - Import SmartTask from a file.
- check_point.mgmt.cp_mgmt_ips_protection_extended_attribute_facts - Get ips-protection-extended-attribute objects facts on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_lock_object - Lock object using uid or {name and type}.
- check_point.mgmt.cp_mgmt_lsv_profile - Manages lsv-profile objects on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_lsv_profile_facts - Get lsv-profile objects facts on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_nat_rule - Manages nat-rule objects on Checkpoint over Web Services API.
- check_point.mgmt.cp_mgmt_radius_group - Manages radius-group objects on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_radius_group_facts - Get radius-group objects facts on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_radius_server - Manages radius-server objects on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_radius_server_facts - Get radius-server objects facts on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_repository_package_facts - Get repository-package objects facts on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_service_citrix_tcp - Manages service-citrix-tcp objects on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_service_citrix_tcp_facts - Get service-citrix-tcp objects facts on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_service_compound_tcp - Manages service-compound-tcp objects on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_service_compound_tcp_facts - Get service-compound-tcp objects facts on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_set_api_settings - Edit API settings, the changes will be applied after publish followed by running 'api restart' command.
- check_point.mgmt.cp_mgmt_set_cloud_services - Set the connection settings between the Management Server and Check Point's Infinity Portal.
- check_point.mgmt.cp_mgmt_set_global_domain - Edit Global domain object using domain name or UID.
- check_point.mgmt.cp_mgmt_set_ha_state - Switch domain server high availability state.
- check_point.mgmt.cp_mgmt_set_ips_update_schedule - Edit IPS Update Schedule.
- check_point.mgmt.cp_mgmt_set_login_message - Edit Login message.
- check_point.mgmt.cp_mgmt_set_policy_settings - Edit Policy settings, the changes will be applied after publish.
- check_point.mgmt.cp_mgmt_set_vpn_community_remote_access - Edit existing Remote Access object. Using object name or uid is optional.
- check_point.mgmt.cp_mgmt_show_api_settings - Retrieve API Settings.
- check_point.mgmt.cp_mgmt_show_api_versions - Shows all supported API versions and current API version (the latest one).
- check_point.mgmt.cp_mgmt_show_azure_ad_content - Retrieve AzureAD Objects from Azure AD Server.
- check_point.mgmt.cp_mgmt_show_changes - Show changes between two sessions.
- check_point.mgmt.cp_mgmt_show_commands - Retrieve all of the supported Management API commands with their description.
- check_point.mgmt.cp_mgmt_show_gateways_and_servers - Shows list of Gateways & Servers sorted by name.
- check_point.mgmt.cp_mgmt_show_global_domain - Retrieve existing object using object name or uid.
- check_point.mgmt.cp_mgmt_show_ha_state - Retrieve domain high availability state.
- check_point.mgmt.cp_mgmt_show_ips_status - show ips status on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_show_ips_update_schedule - Retrieve IPS Update Schedule.
- check_point.mgmt.cp_mgmt_show_layer_structure - Shows the entire layer structure.
- check_point.mgmt.cp_mgmt_show_login_message - Retrieve Login message.
- check_point.mgmt.cp_mgmt_show_place_holder - Retrieve existing object using object uid.
- check_point.mgmt.cp_mgmt_show_policy_settings - Show Policy settings.
- check_point.mgmt.cp_mgmt_show_software_packages_per_targets - Shows software packages on targets.
- check_point.mgmt.cp_mgmt_show_unused_objects - Retrieve all unused objects.
- check_point.mgmt.cp_mgmt_show_updatable_objects_repository_content - Shows the content of the available updatable objects from the Check Point User Center.
- check_point.mgmt.cp_mgmt_show_validations - Show all validation incidents limited to 500.
- check_point.mgmt.cp_mgmt_smart_task - Manages smart-task objects on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_smart_task_facts - Get smart-task objects facts on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_smart_task_trigger_facts - Get smart-task-trigger objects facts on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_tacacs_group - Manages tacacs-group objects on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_tacacs_group_facts - Get tacacs-group objects facts on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_tacacs_server - Manages tacacs-server objects on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_tacacs_server_facts - Get tacacs-server objects facts on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_task_facts - Get task objects facts on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_threat_layers - Manages THREAT LAYERS resource module
- check_point.mgmt.cp_mgmt_time_group - Manages time-group objects on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_time_group_facts - Get time-group objects facts on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_unlock_administrator - Unlock administrator.
- check_point.mgmt.cp_mgmt_unlock_object - Unlock object using uid or {name and type}.
- check_point.mgmt.cp_mgmt_updatable_object_facts - Get updatable-object objects facts on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_update_updatable_objects_repository_content - Updates the content of the Updatable Objects repository from the Check Point User Center.
- check_point.mgmt.cp_mgmt_user_group - Manages user-group objects on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_user_group_facts - Get user-group objects facts on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_vpn_community_remote_access_facts - Get vpn-community-remote-access objects facts on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_vsx_run_operation - Run the VSX operation by its name and parameters.
- check_point.mgmt.cp_mgmt_where_used - Searches for usage of the target object in other objects and rules.

community.aws
~~~~~~~~~~~~~

- community.aws.ec2_carrier_gateway - Manage an AWS VPC Carrier gateway
- community.aws.ec2_carrier_gateway_info - Gather information about carrier gateways in AWS
- community.aws.eks_nodegroup - Manage EKS Nodegroup module
- community.aws.lightsail_snapshot - Creates snapshots of AWS Lightsail instances
- community.aws.mq_broker - MQ broker management
- community.aws.mq_broker_config - Update Amazon MQ broker configuration
- community.aws.mq_broker_info - Retrieve MQ Broker details
- community.aws.mq_user - Manage users in existing Amazon MQ broker
- community.aws.mq_user_info - List users of an Amazon MQ broker
- community.aws.ssm_inventory_info - Get SSM inventory information for EC2 instance

community.docker
~~~~~~~~~~~~~~~~

- community.docker.docker_container_copy_into - Copy a file into a Docker container

community.general
~~~~~~~~~~~~~~~~~

- community.general.btrfs_info - Query btrfs filesystem info
- community.general.btrfs_subvolume - Manage btrfs subvolumes
- community.general.gitlab_project_badge - Manage project badges on GitLab Server
- community.general.ilo_redfish_command - Manages Out-Of-Band controllers using Redfish APIs
- community.general.ipbase_info - Retrieve IP geolocation and other facts of a host's IP address using the ipbase.com API
- community.general.kdeconfig - Manage KDE configuration files
- community.general.keycloak_authz_authorization_scope - Allows administration of Keycloak client authorization scopes via Keycloak API
- community.general.keycloak_clientscope_type - Set the type of aclientscope in realm or client via Keycloak API
- community.general.keycloak_clientsecret_info - Retrieve client secret via Keycloak API
- community.general.keycloak_clientsecret_regenerate - Regenerate Keycloak client secret via Keycloak API
- community.general.ocapi_command - Manages Out-Of-Band controllers using Open Composable API (OCAPI)
- community.general.ocapi_info - Manages Out-Of-Band controllers using Open Composable API (OCAPI)

community.hashi_vault
~~~~~~~~~~~~~~~~~~~~~

- community.hashi_vault.vault_kv2_write - Perform a write operation against a KVv2 secret in HashiCorp Vault
- community.hashi_vault.vault_list - Perform a list operation against HashiCorp Vault

community.hrobot
~~~~~~~~~~~~~~~~

- community.hrobot.v_switch - Manage Hetzner's vSwitch

community.okd
~~~~~~~~~~~~~

- community.okd.openshift_adm_prune_builds - Prune old completed and failed builds
- community.okd.openshift_build - Start a new build or Cancel running, pending, or new builds.

community.vmware
~~~~~~~~~~~~~~~~

- community.vmware.vmware_custom_attribute - Manage custom attributes definitions
- community.vmware.vmware_custom_attribute_manager - Manage custom attributes from VMware for the given vSphere object
- community.vmware.vmware_guest_vgpu_info - Gather information about vGPU profiles of the specified virtual machine in the given vCenter infrastructure
- community.vmware.vmware_vsan_hcl_db - Manages the vSAN Hardware Compatibility List (HCL) database
- community.vmware.vsan_health_silent_checks - Silence vSAN health checks

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- dellemc.openmanage.idrac_user_info - Retrieve iDRAC Local user details.
- dellemc.openmanage.ome_profile_info - Retrieve profiles with attribute details
- dellemc.openmanage.ome_smart_fabric_info - Retrieves the information of smart fabrics inventoried by OpenManage Enterprise Modular
- dellemc.openmanage.ome_smart_fabric_uplink_info - Retrieve details of fabric uplink on OpenManage Enterprise Modular.
- dellemc.openmanage.ome_template_network_vlan_info - Retrieves network configuration of template.

ibm.spectrum_virtualize
~~~~~~~~~~~~~~~~~~~~~~~

- ibm.spectrum_virtualize.ibm_sv_manage_awss3_cloudaccount - Manages AWS cloud account configuration on Spectrum Virtualize systems
- ibm.spectrum_virtualize.ibm_sv_manage_cloud_backups - Manages cloud backup on Spectrum Virtualize systems
- ibm.spectrum_virtualize.ibm_sv_manage_fc_partnership - Manages FC partnership on Spectrum Virtualize systems
- ibm.spectrum_virtualize.ibm_sv_manage_fcportsetmember - Manages addition or removal of ports from the Fibre Channel (FC) portsets on Spectrum Virtualize storage systems
- ibm.spectrum_virtualize.ibm_sv_restore_cloud_backup - Allows user to restore an existing cloud backup on Spectrum Virtualize systems

inspur.ispim
~~~~~~~~~~~~

- inspur.ispim.support_info - Get support information

kubernetes.core
~~~~~~~~~~~~~~~

- kubernetes.core.helm_pull - download a chart from a repository and (optionally) unpack it in local directory.

lowlydba.sqlserver
~~~~~~~~~~~~~~~~~~

- lowlydba.sqlserver.credential - Configures a credential on a SQL server
- lowlydba.sqlserver.user - Configures a user within a database

netapp.ontap
~~~~~~~~~~~~

- netapp.ontap.na_ontap_cifs_local_group - NetApp Ontap - create, delete or modify CIFS local group.
- netapp.ontap.na_ontap_cifs_local_user - NetApp ONTAP local CIFS user.
- netapp.ontap.na_ontap_ems_filter - NetApp ONTAP EMS Filter
- netapp.ontap.na_ontap_kerberos_interface - NetApp ONTAP module to modify kerberos interface.
- netapp.ontap.na_ontap_security_ipsec_ca_certificate - NetApp ONTAP module to add or delete ipsec ca certificate.
- netapp.ontap.na_ontap_security_ipsec_config - NetApp ONTAP module to configure IPsec config.
- netapp.ontap.na_ontap_security_ipsec_policy - NetApp ONTAP module to create, modify or delete security IPsec policy.
- netapp.ontap.na_ontap_vserver_audit - NetApp Ontap - create, delete or modify vserver audit configuration.
- netapp.ontap.na_ontap_vserver_peer_permissions - NetApp Ontap - create, delete or modify vserver peer permission.

netbox.netbox
~~~~~~~~~~~~~

- netbox.netbox.netbox_asn - Create, update or delete ASN in NetBox
- netbox.netbox.netbox_fhrp_group - Create, update or delete FHRP groups in NetBox
- netbox.netbox.netbox_fhrp_group_assignment - Creates, updates or removes FHRP group assignments from NetBox
- netbox.netbox.netbox_inventory_item_role - Create, update or delete inventory item roles in NetBox
- netbox.netbox.netbox_journal_entry - Create journal entries in NetBox
- netbox.netbox.netbox_l2vpn - Create, update or delete L2VPN objects in NetBox
- netbox.netbox.netbox_lsvpn_termination - Creates, updates or removes L2VPNs terminations from NetBox
- netbox.netbox.netbox_module_type - Create, update or delete module types in NetBox
- netbox.netbox.netbox_service_template - Create, update or delete service templates in NetBox

purestorage.flasharray
~~~~~~~~~~~~~~~~~~~~~~

- purestorage.flasharray.purefa_snmp_agent - Configure the FlashArray SNMP Agent

purestorage.flashblade
~~~~~~~~~~~~~~~~~~~~~~

- purestorage.flashblade.purefb_pingtrace - Employ the internal FlashBlade ping and trace mechanisms

theforeman.foreman
~~~~~~~~~~~~~~~~~~

- theforeman.foreman.content_view_filter_info - Fetch information about a Content View Filter
- theforeman.foreman.content_view_filter_rule - Manage content view filter rules
- theforeman.foreman.content_view_filter_rule_info - Fetch information about a Content View Filter Rule
- theforeman.foreman.hostgroup_info - Get information about hostgroup(s)
- theforeman.foreman.snapshot_info - Fetch information about Foreman Snapshots

vmware.vmware_rest
~~~~~~~~~~~~~~~~~~

- vmware.vmware_rest.vcenter_vm_guest_customization - Applies a customization specification on the virtual machine
- vmware.vmware_rest.vcenter_vm_guest_power - Issues a request to the guest operating system asking it to perform a soft shutdown, standby (suspend) or soft reboot
- vmware.vmware_rest.vcenter_vm_guest_power_info - Returns information about the guest operating system power state.
- vmware.vmware_rest.vcenter_vm_storage_policy_compliance - Returns the storage policy Compliance {@link Info} of a virtual machine after explicitly re-computing compliance check.
- vmware.vmware_rest.vcenter_vm_tools_installer - Connects the VMware Tools CD installer as a CD-ROM for the guest operating system
- vmware.vmware_rest.vcenter_vm_tools_installer_info - Get information about the VMware Tools installer.

vultr.cloud
~~~~~~~~~~~

- vultr.cloud.instance_info - Get information about the Vultr instances
- vultr.cloud.snapshot - Manages snapshots on Vultr
- vultr.cloud.snapshot_info - Gather information about the Vultr snapshots

New Playbooks
-------------

- community.sops.install - Installs sops and GNU Privacy Guard on all remote hosts
- community.sops.install_localhost - Installs sops and GNU Privacy Guard on localhost

New Roles
---------

- community.sops.install - Install Mozilla sops
- dellemc.openmanage.idrac_certificate - Role to manage the iDRAC certificates - generate CSR, import/export certificates, and reset configuration - for PowerEdge servers.
- dellemc.openmanage.idrac_export_server_config_profile - Role to export iDRAC Server Configuration Profile (SCP).
- dellemc.openmanage.idrac_firmware - Firmware update from a repository on a network share (CIFS, NFS, HTTP, HTTPS, FTP).
- dellemc.openmanage.idrac_gather_facts - Role to gather facts from the iDRAC Server.
- dellemc.openmanage.idrac_import_server_config_profile - Role to import iDRAC Server Configuration Profile (SCP).
- dellemc.openmanage.idrac_os_deployment - Role to deploy specified operating system and version on the servers.
- dellemc.openmanage.idrac_server_powerstate - Role to manage the different power states of the specified device.
- dellemc.openmanage.redfish_firmware - To perform a component firmware update using the image file available on the local or remote system.
- dellemc.openmanage.redfish_storage_volume - Role to manage the storage volume configuration.

Unchanged Collections
---------------------

- cisco.asa (still version 4.0.0)
- cisco.nso (still version 1.0.3)
- cisco.ucs (still version 1.8.0)
- community.azure (still version 2.0.0)
- community.ciscosmb (still version 1.0.5)
- community.fortios (still version 1.0.0)
- community.google (still version 1.0.0)
- community.libvirt (still version 1.2.0)
- community.network (still version 5.0.0)
- community.rabbitmq (still version 1.2.3)
- community.sap (still version 1.0.0)
- community.skydive (still version 1.0.0)
- cyberark.conjur (still version 1.2.0)
- dellemc.enterprise_sonic (still version 2.0.0)
- fortinet.fortimanager (still version 2.1.7)
- gluster.gluster (still version 1.0.2)
- hpe.nimble (still version 1.1.4)
- ibm.qradar (still version 2.1.0)
- inspur.sm (still version 2.3.0)
- netapp.aws (still version 21.7.0)
- netapp.azure (still version 21.10.0)
- netapp.elementsw (still version 21.7.0)
- netapp.storagegrid (still version 21.11.1)
- netapp.um_info (still version 21.8.0)
- ngine_io.exoscale (still version 1.0.0)
- splunk.es (still version 2.1.0)
- wti.remote (still version 1.0.4)
