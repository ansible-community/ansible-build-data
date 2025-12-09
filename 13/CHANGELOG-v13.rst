========================
Ansible 13 Release Notes
========================

This changelog describes changes since Ansible 12.0.0.

.. contents::
  :depth: 2

v13.1.0
=======

.. contents::
  :local:
  :depth: 2

Release Summary
---------------

Release Date: 2025-12-09

`Porting Guide <https://docs.ansible.com/projects/ansible/devel/porting_guides.html>`_

Ansible-core
------------

Ansible 13.1.0 contains ansible-core version 2.20.1.
This is a newer version than version 2.20.0 contained in the previous Ansible release.

The changes are reported in the combined changelog below.

Changed Collections
-------------------

If not mentioned explicitly, the changes are reported in the combined changelog below.

+------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Collection                   | Ansible 13.0.0 | Ansible 13.1.0 | Notes                                                                                                                                                                                                           |
+==============================+================+================+=================================================================================================================================================================================================================+
| ansible.netcommon            | 8.1.0          | 8.2.0          |                                                                                                                                                                                                                 |
+------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ansible.windows              | 3.2.0          | 3.3.0          |                                                                                                                                                                                                                 |
+------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| azure.azcollection           | 3.10.1         | 3.12.0         | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.                                                                                    |
+------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| check_point.mgmt             | 6.6.0          | 6.7.0          | The collection did not have a changelog in this version.                                                                                                                                                        |
+------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cisco.aci                    | 2.12.0         | 2.13.0         |                                                                                                                                                                                                                 |
+------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cisco.dnac                   | 6.41.0         | 6.43.0         |                                                                                                                                                                                                                 |
+------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cisco.intersight             | 2.7.0          | 2.12.0         | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.                                                                                    |
+------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cisco.meraki                 | 2.21.8         | 2.21.9         |                                                                                                                                                                                                                 |
+------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cisco.mso                    | 2.11.0         | 2.12.0         |                                                                                                                                                                                                                 |
+------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cisco.nxos                   | 11.0.0         | 11.1.0         |                                                                                                                                                                                                                 |
+------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.dns                | 3.4.0          | 3.4.1          |                                                                                                                                                                                                                 |
+------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.docker             | 5.0.1          | 5.0.4          |                                                                                                                                                                                                                 |
+------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.general            | 12.0.1         | 12.1.0         |                                                                                                                                                                                                                 |
+------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.postgresql         | 4.1.0          | 4.2.0          |                                                                                                                                                                                                                 |
+------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.routeros           | 3.13.0         | 3.14.0         |                                                                                                                                                                                                                 |
+------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.windows            | 3.0.1          | 3.1.0          |                                                                                                                                                                                                                 |
+------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cyberark.conjur              | 1.3.8          | 1.3.9          | You can find the collection's changelog at `https://github.com/cyberark/ansible-conjur-collection/blob/master/CHANGELOG.md <https://github.com/cyberark/ansible-conjur-collection/blob/master/CHANGELOG.md>`__. |
+------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| google.cloud                 | 1.9.0          | 1.10.2         |                                                                                                                                                                                                                 |
+------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| hetzner.hcloud               | 6.0.0          | 6.2.1          |                                                                                                                                                                                                                 |
+------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| hitachivantara.vspone_block  | 4.4.0          | 4.5.0          |                                                                                                                                                                                                                 |
+------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| hitachivantara.vspone_object | 1.0.0          | 1.1.1          |                                                                                                                                                                                                                 |
+------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| inspur.ispim                 | 2.2.3          | 2.2.4          |                                                                                                                                                                                                                 |
+------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| microsoft.ad                 | 1.9.2          | 1.10.0         |                                                                                                                                                                                                                 |
+------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| microsoft.iis                | 1.0.3          | 1.1.0          |                                                                                                                                                                                                                 |
+------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| purestorage.flasharray       | 1.39.0         | 1.40.0         |                                                                                                                                                                                                                 |
+------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| telekom_mms.icinga_director  | 2.4.0          | 2.5.0          |                                                                                                                                                                                                                 |
+------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| vmware.vmware                | 2.4.0          | 2.6.0          |                                                                                                                                                                                                                 |
+------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Major Changes
-------------

vmware.vmware
~~~~~~~~~~~~~

- Replace ``ansible.module_utils._text`` (https://github.com/ansible-collections/vmware.vmware/issues/268).
- Replace ``ansible.module_utils.common._collections_compat`` (https://github.com/ansible-collections/vmware.vmware/issues/271).

Minor Changes
-------------

ansible.netcommon
~~~~~~~~~~~~~~~~~

- Exposes new libssh option to configure key_exchange_algorithms. This requires ansible-pylibssh v1.3.0 or higher.

ansible.windows
~~~~~~~~~~~~~~~

- Add official support for Ansible 2.20
- win_environment - Add the return value ``env_values`` which is a copy of the existing ``values`` return value. The documentation for ``values`` has been removed to discourage use of that version due to the inability to use ``values`` with dot notation in a Jinja2 template due to the conflict with the Python ``values`` attribute.

cisco.aci
~~~~~~~~~

- Add contract_type option to aci_contract_subject_to_filter and aci_contract_subject.
- Add l3out, l3out_tenant, external_epg and redistribute options to aci_l4l7_device_selection_interface_context.
- Add normalize_payload_values option to aci_rest for Ansible Core 2.19 support.
- Add set_communities, set_as_path and set_policy_tag options to aci_tenant_action_rule_profile.

cisco.dnac
~~~~~~~~~~

- Added 'ap_authorization_list_name', 'authorize_mesh_and_non_mesh_aps', 'feature_template'  attributes in provision_workflow_manager module
- Added 'authorize' attribute in network_profile_wireless_workflow_manager module
- Added 'backup_task_timeout' and 'restore_task_timeout'  attributes in backup_and_restore_workflow_manager module
- Added 'convert_to_wlc'  attribute in swim_workflow_manager module
- Added 'feature_template_config'  attribute in wireless_design_workflow_manager module
- Added 'feature_template_designs' attribute in network_profile_wireless_workflow_manager module
- Added 'image_name', sync_cco, image_distribution_timeout, device_tag, image_activation_timeout, compatible_devices in swim_workflow_manager module
- Added 'profile_names' in template_workflow_manager module
- Added 'sda_fabric_port_channel_limit'  attribute in sda_host_port_onboarding_workflow_manager module
- Changes in accesspoint_workflow_manager module
- Changes in application_policy_workflow_manager module
- Changes in backup_and_restore_workflow_manager module
- Changes in inventory_workflow_manager module
- Changes in ise_radius_integration_workflow_manager module
- Changes in lan_automation_workflow_manager module
- Changes in network_devices_info_workflow_manager module
- Changes in network_profile_wireless_workflow_manager module
- Changes in network_settings_workflow_manager module
- Changes in pnp_workflow_manager module
- Changes in provision_workflow_manager module
- Changes in reports_workflow_manager module
- Changes in sda_fabric_sites_zones_workflow_manager module
- Changes in sda_fabric_virtual_networks_workflow_manager module
- Changes in sda_host_port_onboarding_workflow_manager module
- Changes in swim_workflow_manager module
- Changes in template_workflow_manager module
- Changes in wireless_design_workflow_manager module
- Enhancements in 'lan_automation_workflow_manager' to support port channel
- Enhancements in 'pnp_workflow_manager' to support authorization
- New module 'accesspoint_location_workflow_manager' to manage Access point planned position in the floor
- New module 'backup_and_restore_workflow_manager' for backup and restore workflow management
- New module 'fabric_devices_info_workflow_manager' for gathering fabric device information
- New module 'network_devices_info_workflow_manager' for gathering network device information
- New module 'reports_workflow_manager' for managing reports
- New module 'wired_campus_automation_workflow_manager' for managing wired campus automation

cisco.mso
~~~~~~~~~

- Add parent_type, node_id, path, port_channel, virtual_port_channel, encapsulation_type and encapsulation_value options to ndo_l3out_bgp_peer.
- Add ptp option to ndo_l3out_routed_interface and ndo_l3out_routed_sub_interface.

cisco.nxos
~~~~~~~~~~

- Added alias for mode option as switchport_mode for nxos_l2_interfaces

community.general
~~~~~~~~~~~~~~~~~

- The last code included in the collection that was licensed under the PSF 2.0 license was removed form the collection. This means that now all code is either GPLv3+ licensed, MIT licensed, or BSD-2-clause licensed (https://github.com/ansible-collections/community.general/pull/11232).
- _mount module utils - simplify return of boolean values in functions (https://github.com/ansible-collections/community.general/pull/11119).
- _stormssh module utils - fix cases of unused variables in loops (https://github.com/ansible-collections/community.general/pull/11115).
- a_module test plugin - add proper parameter checking and type hints (https://github.com/ansible-collections/community.general/pull/11167).
- aerospike_migrations - simplify return of boolean values in functions (https://github.com/ansible-collections/community.general/pull/11119).
- aix_filesystem - improve code by using native Python construct (https://github.com/ansible-collections/community.general/pull/11215).
- ali_instance - fix cases of unused variables in loops (https://github.com/ansible-collections/community.general/pull/11115).
- ansible_type plugin utils - add type hints (https://github.com/ansible-collections/community.general/pull/11167).
- ansible_type test plugin - add type hints (https://github.com/ansible-collections/community.general/pull/11167).
- apk - simplify return of boolean values in functions (https://github.com/ansible-collections/community.general/pull/11119).
- apt_rpm - fix cases of unused variables in loops (https://github.com/ansible-collections/community.general/pull/11115).
- apt_rpm - simplify return of boolean values in functions (https://github.com/ansible-collections/community.general/pull/11119).
- atomic_container - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11102).
- atomic_container modules - replace ``%`` templating with f-strings or ``format()`` (https://github.com/ansible-collections/community.general/pull/11223).
- atomic_host - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11098).
- atomic_image - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11098).
- atomic_image modules - replace ``%`` templating with f-strings or ``format()`` (https://github.com/ansible-collections/community.general/pull/11223).
- awall - simplify return of boolean values in functions (https://github.com/ansible-collections/community.general/pull/11119).
- beadm - simplify return of boolean values in functions (https://github.com/ansible-collections/community.general/pull/11119).
- bigpanda - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11098).
- binary_file lookup plugin - use ``raise ... from ...`` when passing on exceptions (https://github.com/ansible-collections/community.general/pull/11095).
- bitbucket module utils - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11112).
- bitbucket_access_key modules - replace ``%`` templating with f-strings or ``format()`` (https://github.com/ansible-collections/community.general/pull/11223).
- bitbucket_pipeline_key_pair modules - replace ``%`` templating with f-strings or ``format()`` (https://github.com/ansible-collections/community.general/pull/11223).
- bitbucket_pipeline_known_host modules - replace ``%`` templating with f-strings or ``format()`` (https://github.com/ansible-collections/community.general/pull/11223).
- bitbucket_pipeline_variable modules - replace ``%`` templating with f-strings or ``format()`` (https://github.com/ansible-collections/community.general/pull/11223).
- chef_databag lookup plugin - use ``raise ... from ...`` when passing on exceptions (https://github.com/ansible-collections/community.general/pull/11095).
- chroot connection plugin - use ``raise ... from ...`` when passing on exceptions (https://github.com/ansible-collections/community.general/pull/11095).
- circonus_annotation - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11102).
- cloudflare_dns - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/1114).
- cmd_runner module utils - use ``raise ... from ...`` when passing on exceptions (https://github.com/ansible-collections/community.general/pull/11097).
- cobbler inventory plugin - fix cases of unused variables in loops (https://github.com/ansible-collections/community.general/pull/11115).
- cobbler_sync - remove conditional code handling SSL for unsupported versions of Python (https://github.com/ansible-collections/community.general/pull/11078).
- cobbler_sync - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11105).
- cobbler_system - remove conditional code handling SSL for unsupported versions of Python (https://github.com/ansible-collections/community.general/pull/11078).
- cobbler_system - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11105).
- collection_version lookup plugin - use ``raise ... from ...`` when passing on exceptions (https://github.com/ansible-collections/community.general/pull/11095).
- composer - improve code by using native Python construct (https://github.com/ansible-collections/community.general/pull/11215).
- consul_kv lookup plugin - use ``raise ... from ...`` when passing on exceptions (https://github.com/ansible-collections/community.general/pull/11095).
- counter filter plugin - use ``raise ... from ...`` when passing on exceptions (https://github.com/ansible-collections/community.general/pull/11095).
- credstash lookup plugin - use ``raise ... from ...`` when passing on exceptions (https://github.com/ansible-collections/community.general/pull/11095).
- cronvar - use ``raise ... from ...`` when passing on exceptions (https://github.com/ansible-collections/community.general/pull/11097).
- crypttab - simplify return of boolean values in functions (https://github.com/ansible-collections/community.general/pull/11119).
- csv module utils - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11112).
- csv module utils - use ``raise ... from ...`` when passing on exceptions (https://github.com/ansible-collections/community.general/pull/11097).
- cyberarkpassword lookup plugin - use ``raise ... from ...`` when passing on exceptions (https://github.com/ansible-collections/community.general/pull/11095).
- database module utils - improve code by using native Python construct (https://github.com/ansible-collections/community.general/pull/11215).
- database module utils - use ``raise ... from ...`` when passing on exceptions (https://github.com/ansible-collections/community.general/pull/11097).
- datadog_event - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11098).
- datadog_monitor - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11098).
- dconf - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/1114).
- dependent lookup plugin - improve templating of strings (https://github.com/ansible-collections/community.general/pull/11189).
- dependent lookup plugin - use ``raise ... from ...`` when passing on exceptions (https://github.com/ansible-collections/community.general/pull/11095).
- deps module utils - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11112).
- dig lookup plugin - use ``raise ... from ...`` when passing on exceptions (https://github.com/ansible-collections/community.general/pull/11095).
- dimensiondata_network - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11102).
- dimensiondata_network modules - replace ``%`` templating with f-strings or ``format()`` (https://github.com/ansible-collections/community.general/pull/11223).
- dnf_config_manager - fix cases of unused variables in loops (https://github.com/ansible-collections/community.general/pull/11115).
- dnstxt lookup plugin - use ``raise ... from ...`` when passing on exceptions (https://github.com/ansible-collections/community.general/pull/11095).
- dsv lookup plugin - use ``raise ... from ...`` when passing on exceptions (https://github.com/ansible-collections/community.general/pull/11095).
- elastic callback plugin - fix cases of unused variables in loops (https://github.com/ansible-collections/community.general/pull/11115).
- etcd3 lookup plugin - use ``raise ... from ...`` when passing on exceptions (https://github.com/ansible-collections/community.general/pull/11095).
- exceptions module utils - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11112).
- filesize - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11104).
- filesize - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11106).
- flatpak - improve code by using native Python construct (https://github.com/ansible-collections/community.general/pull/11215).
- flatpak_remote - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11106).
- fqdn_valid test plugin - add proper parameter checking, and add type hints (https://github.com/ansible-collections/community.general/pull/11167).
- from_csv filter plugin - use ``raise ... from ...`` when passing on exceptions (https://github.com/ansible-collections/community.general/pull/11095).
- from_ini filter plugin - use ``raise ... from ...`` when passing on exceptions (https://github.com/ansible-collections/community.general/pull/11095).
- gandi_livedns_api module utils - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11112).
- github_app_access_token lookup plugin - use ``raise ... from ...`` when passing on exceptions (https://github.com/ansible-collections/community.general/pull/11095).
- gitlab_group_access_token - simplify return of boolean values in functions (https://github.com/ansible-collections/community.general/pull/11119).
- gitlab_group_members - improve code by using native Python construct (https://github.com/ansible-collections/community.general/pull/11215).
- gitlab_project_access_token - simplify return of boolean values in functions (https://github.com/ansible-collections/community.general/pull/11119).
- gitlab_project_members - improve code by using native Python construct (https://github.com/ansible-collections/community.general/pull/11215).
- gitlab_runner - allow maximum timeout to be disabled by passing ``0`` to ``maximum_timeout``  (https://github.com/ansible-collections/community.general/pull/11174).
- gitlab_runners inventory plugin - use ``raise ... from ...`` when passing on exceptions (https://github.com/ansible-collections/community.general/pull/11095).
- haproxy - fix cases of unused variables in loops (https://github.com/ansible-collections/community.general/pull/11115).
- hashids filter - replace ``%`` templating with f-strings or ``format()`` (https://github.com/ansible-collections/community.general/pull/11223).
- hashids filter plugin - use ``raise ... from ...`` when passing on exceptions (https://github.com/ansible-collections/community.general/pull/11095).
- hg - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11106).
- hg - simplify return of boolean values in functions (https://github.com/ansible-collections/community.general/pull/11119).
- hpilo_info - fix cases of unused variables in loops (https://github.com/ansible-collections/community.general/pull/11115).
- hpilo_info - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11098).
- htpasswd - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11098).
- hwc_ecs_instance - fix cases of unused variables in loops (https://github.com/ansible-collections/community.general/pull/11115).
- hwc_utils module utils - improve code by using native Python construct (https://github.com/ansible-collections/community.general/pull/11215).
- hwc_utils module utils - use ``raise ... from ...`` when passing on exceptions (https://github.com/ansible-collections/community.general/pull/11097).
- hwc_vpc_port - fix cases of unused variables in loops (https://github.com/ansible-collections/community.general/pull/11115).
- ibm_sa_utils module utils - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11112).
- icinga2 inventory plugin - use ``raise ... from ...`` when passing on exceptions (https://github.com/ansible-collections/community.general/pull/11095).
- icinga2_host - simplify return of boolean values in functions (https://github.com/ansible-collections/community.general/pull/11119).
- identity.keycloak.keycloak module utils - use ``raise ... from ...`` when passing on exceptions (https://github.com/ansible-collections/community.general/pull/11097).
- idrac_redfish_command - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11110).
- idrac_redfish_command - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/1114).
- idrac_redfish_config - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11098).
- idrac_redfish_config - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11102).
- idrac_redfish_config - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11110).
- idrac_redfish_config - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/1114).
- idrac_redfish_info - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11110).
- idrac_redfish_info - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/1114).
- ilo_redfish_command - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11110).
- ilo_redfish_command - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/1114).
- ilo_redfish_config - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11110).
- ilo_redfish_config - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/1114).
- imc_rest modules - replace ``%`` templating with f-strings or ``format()`` (https://github.com/ansible-collections/community.general/pull/11223).
- incus connection plugin - add support for Windows virtual machines (https://github.com/ansible-collections/community.general/pull/11199).
- influxdb_query - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11098).
- influxdb_user - fix cases of unused variables in loops (https://github.com/ansible-collections/community.general/pull/11115).
- influxdb_user - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11098).
- influxdb_write - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11098).
- iocage inventory plugin - fix cases of unused variables in loops (https://github.com/ansible-collections/community.general/pull/11115).
- ip_netns - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11104).
- ip_netns - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11105).
- ip_netns - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11106).
- ipa module utils - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11112).
- ipa module utils - use ``raise ... from ...`` when passing on exceptions (https://github.com/ansible-collections/community.general/pull/11097).
- ipa_config - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11098).
- ipa_dnsrecord - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11098).
- ipa_dnszone - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11098).
- ipa_group - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11098).
- ipa_hbacrule - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11098).
- ipa_host - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11098).
- ipa_hostgroup - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11098).
- ipa_otpconfig - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11098).
- ipa_otptoken - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11098).
- ipa_pwpolicy - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11098).
- ipa_pwpolicy - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11106).
- ipa_role - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11098).
- ipa_service - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11098).
- ipa_subca - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11104).
- ipa_sudocmd - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11098).
- ipa_sudocmdgroup - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11098).
- ipa_sudorule - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11098).
- ipa_user - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11098).
- ipa_vault - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11098).
- iptables_state action plugin - add type hints (https://github.com/ansible-collections/community.general/pull/11167).
- iso_customize - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11106).
- jail connection plugin - use ``raise ... from ...`` when passing on exceptions (https://github.com/ansible-collections/community.general/pull/11095).
- jc filter plugin - use ``raise ... from ...`` when passing on exceptions (https://github.com/ansible-collections/community.general/pull/11095).
- jenkins_job - simplify return of boolean values in functions (https://github.com/ansible-collections/community.general/pull/11119).
- jenkins_job_info - remove conditional code handling SSL for unsupported versions of Python (https://github.com/ansible-collections/community.general/pull/11078).
- jenkins_plugin - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11102).
- jenkins_plugin - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/1114).
- jenkins_plugin - use ``raise ... from ...`` when passing on exceptions (https://github.com/ansible-collections/community.general/pull/11097).
- jenkins_plugin modules - replace ``%`` templating with f-strings or ``format()`` (https://github.com/ansible-collections/community.general/pull/11223).
- jenkins_script - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/1114).
- jira - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11104).
- jira - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/1114).
- jira - use ``raise ... from ...`` when passing on exceptions (https://github.com/ansible-collections/community.general/pull/11097).
- json_query filter plugin - use ``raise ... from ...`` when passing on exceptions (https://github.com/ansible-collections/community.general/pull/11095).
- keycloak module utils - fix cases of unused variables in loops (https://github.com/ansible-collections/community.general/pull/11115).
- keycloak module utils - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11112).
- keycloak module_utils - replace ``%`` templating with f-strings or ``format()`` (https://github.com/ansible-collections/community.general/pull/11223).
- keycloak_authentication - fix cases of unused variables in loops (https://github.com/ansible-collections/community.general/pull/11115).
- keycloak_client_rolemapping - fix cases of unused variables in loops (https://github.com/ansible-collections/community.general/pull/11115).
- keycloak_component - fix cases of unused variables in loops (https://github.com/ansible-collections/community.general/pull/11115).
- keycloak_realm - add ``webAuthnPolicyPasswordlessPasskeysEnabled`` parameter (https://github.com/ansible-collections/community.general/pull/11197).
- keycloak_realm_key - fix cases of unused variables in loops (https://github.com/ansible-collections/community.general/pull/11115).
- keycloak_realm_rolemapping - fix cases of unused variables in loops (https://github.com/ansible-collections/community.general/pull/11115).
- keycloak_user_rolemapping - fix cases of unused variables in loops (https://github.com/ansible-collections/community.general/pull/11115).
- keycloak_userprofile - fix cases of unused variables in loops (https://github.com/ansible-collections/community.general/pull/11115).
- keys_filter plugin_utils plugin - use ``raise ... from ...`` when passing on exceptions (https://github.com/ansible-collections/community.general/pull/11095).
- keys_filter.py plugin utils - add type hints (https://github.com/ansible-collections/community.general/pull/11167).
- known_hosts module utils - improve code by using native Python construct (https://github.com/ansible-collections/community.general/pull/11215).
- layman - use ``raise ... from ...`` when passing on exceptions (https://github.com/ansible-collections/community.general/pull/11097).
- ldap module utils - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11112).
- ldap_attrs - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11102).
- ldap_entry - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11102).
- ldap_inc - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11102).
- ldap_search - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11104).
- ldap_search - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11106).
- linode inventory plugin - use ``raise ... from ...`` when passing on exceptions (https://github.com/ansible-collections/community.general/pull/11095).
- listen_ports_facts - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11098).
- listen_ports_facts - use ``raise ... from ...`` when passing on exceptions (https://github.com/ansible-collections/community.general/pull/11097).
- lmdb_kv lookup plugin - use ``raise ... from ...`` when passing on exceptions (https://github.com/ansible-collections/community.general/pull/11095).
- locale_gen - extend the search for available locales to include ``/usr/local/share/i18n/SUPPORTED`` in Debian and Ubuntu systems (https://github.com/ansible-collections/community.general/issues/10964, https://github.com/ansible-collections/community.general/pull/11046).
- logentries - simplify return of boolean values in functions (https://github.com/ansible-collections/community.general/pull/11119).
- lxc connection plugin - use ``raise ... from ...`` when passing on exceptions (https://github.com/ansible-collections/community.general/pull/11095).
- lxd connection plugin - use ``raise ... from ...`` when passing on exceptions (https://github.com/ansible-collections/community.general/pull/11095).
- lxd inventory plugin - use ``raise ... from ...`` when passing on exceptions (https://github.com/ansible-collections/community.general/pull/11095).
- lxd module utils - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11112).
- lxd module utils - use ``raise ... from ...`` when passing on exceptions (https://github.com/ansible-collections/community.general/pull/11097).
- lxd_container - improve code by using native Python construct (https://github.com/ansible-collections/community.general/pull/11215).
- macports - simplify return of boolean values in functions (https://github.com/ansible-collections/community.general/pull/11119).
- mail - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/1114).
- maven_artifact - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/1114).
- merge_variables - extend type detection failure message to allow users for easier failure debugging (https://github.com/ansible-collections/community.general/pull/11107).
- merge_variables lookup plugin - simplify return of boolean values in functions (https://github.com/ansible-collections/community.general/pull/11119).
- modprobe - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11098).
- net_tools.pritunl.api module utils - use ``raise ... from ...`` when passing on exceptions (https://github.com/ansible-collections/community.general/pull/11097).
- nmap inventory plugin - use ``raise ... from ...`` when passing on exceptions (https://github.com/ansible-collections/community.general/pull/11095).
- nmcli - fix cases of unused variables in loops (https://github.com/ansible-collections/community.general/pull/11115).
- nmcli - fix comparison of type (https://github.com/ansible-collections/community.general/pull/11121).
- nmcli modules - replace ``%`` templating with f-strings or ``format()`` (https://github.com/ansible-collections/community.general/pull/11223).
- nomad_job - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11098).
- nomad_job - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11106).
- nomad_job_info - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11098).
- nomad_token - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11098).
- nosh - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11106).
- ocapi_command - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11106).
- ocapi_command - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11110).
- ocapi_info - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11106).
- ocapi_utils module utils - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11112).
- oci_utils module utils - improve code by using native Python construct (https://github.com/ansible-collections/community.general/pull/11215).
- oci_utils module utils - improve templating of strings (https://github.com/ansible-collections/community.general/pull/11189).
- oneandone_firewall_policy - simplify return of boolean values in functions (https://github.com/ansible-collections/community.general/pull/11119).
- oneandone_load_balancer - simplify return of boolean values in functions (https://github.com/ansible-collections/community.general/pull/11119).
- oneandone_monitoring_policy - simplify return of boolean values in functions (https://github.com/ansible-collections/community.general/pull/11119).
- oneandone_private_network - simplify return of boolean values in functions (https://github.com/ansible-collections/community.general/pull/11119).
- oneandone_server - replace ``%`` templating with f-strings or ``format()`` (https://github.com/ansible-collections/community.general/pull/11231).
- oneandone_server modules - mark ``%`` templating as ``noqa`` (https://github.com/ansible-collections/community.general/pull/11223).
- onepassword lookup plugin - use ``raise ... from ...`` when passing on exceptions (https://github.com/ansible-collections/community.general/pull/11095).
- onepassword_info - execute external commands using Ansible construct (https://github.com/ansible-collections/community.general/pull/11193).
- onepassword_info - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11102).
- onepassword_info - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/1114).
- oneview module utils - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11112).
- online inventory plugin - use ``raise ... from ...`` when passing on exceptions (https://github.com/ansible-collections/community.general/pull/11095).
- opennebula inventory plugin - use ``raise ... from ...`` when passing on exceptions (https://github.com/ansible-collections/community.general/pull/11095).
- opentelemetry callback plugin - fix cases of unused variables in loops (https://github.com/ansible-collections/community.general/pull/11115).
- osx_defaults - use ``raise ... from ...`` when passing on exceptions (https://github.com/ansible-collections/community.general/pull/11097).
- packet_device - replace ``%`` templating with f-strings or ``format()`` (https://github.com/ansible-collections/community.general/pull/11231).
- packet_device modules - mark ``%`` templating as ``noqa`` (https://github.com/ansible-collections/community.general/pull/11223).
- packet_ip_subnet - use ``raise ... from ...`` when passing on exceptions (https://github.com/ansible-collections/community.general/pull/11097).
- packet_project - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11106).
- packet_sshkey - use ``raise ... from ...`` when passing on exceptions (https://github.com/ansible-collections/community.general/pull/11097).
- packet_volume - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11106).
- packet_volume - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/1114).
- pamd - simplify return of boolean values in functions (https://github.com/ansible-collections/community.general/pull/11119).
- parted - simplify return of boolean values in functions (https://github.com/ansible-collections/community.general/pull/11119).
- passwordstore lookup plugin - use ``raise ... from ...`` when passing on exceptions (https://github.com/ansible-collections/community.general/pull/11095).
- pear - fix cases of unused variables in loops (https://github.com/ansible-collections/community.general/pull/11115).
- pids - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11098).
- pids - use ``raise ... from ...`` when passing on exceptions (https://github.com/ansible-collections/community.general/pull/11097).
- portage - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11106).
- pritunl_org - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11098).
- pritunl_org_info - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11098).
- pritunl_user - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11098).
- pritunl_user_info - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11098).
- pushbullet modules - replace ``%`` templating with f-strings or ``format()`` (https://github.com/ansible-collections/community.general/pull/11223).
- read_csv - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11098).
- redfish_command - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11110).
- redfish_command - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/1114).
- redfish_config - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11110).
- redfish_config - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/1114).
- redfish_utils module utils - fix cases of unused variables in loops (https://github.com/ansible-collections/community.general/pull/11115).
- redfish_utils module utils - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11112).
- redhat_subscription - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11106).
- redhat_subscription - simplify return of boolean values in functions (https://github.com/ansible-collections/community.general/pull/11119).
- redis cache plugin - use ``raise ... from ...`` when passing on exceptions (https://github.com/ansible-collections/community.general/pull/11095).
- redis lookup plugin - use ``raise ... from ...`` when passing on exceptions (https://github.com/ansible-collections/community.general/pull/11095).
- revbitspss lookup plugin - use ``raise ... from ...`` when passing on exceptions (https://github.com/ansible-collections/community.general/pull/11095).
- rhevm - use ``raise ... from ...`` when passing on exceptions (https://github.com/ansible-collections/community.general/pull/11097).
- riak - simplify return of boolean values in functions (https://github.com/ansible-collections/community.general/pull/11119).
- rundeck module utils - improve handling the return value ``exception``. It now contains the full stack trace of the exception, while the message is included in ``msg`` (https://github.com/ansible-collections/community.general/pull/11149).
- scaleway inventory plugin - use ``raise ... from ...`` when passing on exceptions (https://github.com/ansible-collections/community.general/pull/11095).
- scaleway_user_data modules - replace ``%`` templating with f-strings or ``format()`` (https://github.com/ansible-collections/community.general/pull/11223).
- selinux_permissive - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11098).
- sensu_check - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11098).
- sensu_silence - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/1114).
- sensu_silence modules - replace ``%`` templating with f-strings or ``format()`` (https://github.com/ansible-collections/community.general/pull/11223).
- sensu_subscription - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11098).
- sensu_subscription - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11102).
- shelvefile lookup plugin - use ``raise ... from ...`` when passing on exceptions (https://github.com/ansible-collections/community.general/pull/11095).
- shutdown action plugin - add type hints (https://github.com/ansible-collections/community.general/pull/11167).
- shutdown action plugin - use ``raise ... from ...`` when passing on exceptions (https://github.com/ansible-collections/community.general/pull/11095).
- slack - simplify return of boolean values in functions (https://github.com/ansible-collections/community.general/pull/11119).
- slackpkg - simplify return of boolean values in functions (https://github.com/ansible-collections/community.general/pull/11119).
- snap - improve templating of strings (https://github.com/ansible-collections/community.general/pull/11189).
- snmp_facts - simplify and improve code using standard Ansible validations (https://github.com/ansible-collections/community.general/pull/11148).
- solaris_zone - execute external commands using Ansible construct (https://github.com/ansible-collections/community.general/pull/11192).
- solaris_zone - simplify return of boolean values in functions (https://github.com/ansible-collections/community.general/pull/11119).
- spectrum_model_attrs - convert ``%`` templating to f-string (https://github.com/ansible-collections/community.general/pull/11229).
- statusio_maintenance - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11102).
- sudoers - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11098).
- svc - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/1114).
- svr4pkg - simplify return of boolean values in functions (https://github.com/ansible-collections/community.general/pull/11119).
- swupd - simplify return of boolean values in functions (https://github.com/ansible-collections/community.general/pull/11119).
- to_ini filter plugin - use ``raise ... from ...`` when passing on exceptions (https://github.com/ansible-collections/community.general/pull/11095).
- tss lookup plugin - use ``raise ... from ...`` when passing on exceptions (https://github.com/ansible-collections/community.general/pull/11095).
- univention_umc module utils - update code to Python 3 (https://github.com/ansible-collections/community.general/pull/11122).
- unsafe.py plugin utils - add type hints (https://github.com/ansible-collections/community.general/pull/11167).
- urpmi - simplify return of boolean values in functions (https://github.com/ansible-collections/community.general/pull/11119).
- utm_aaa_group - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11098).
- utm_aaa_group_info - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11098).
- utm_ca_host_key_cert - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11098).
- utm_ca_host_key_cert_info - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11098).
- utm_dns_host - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11098).
- utm_network_interface_address - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11098).
- utm_network_interface_address_info - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11098).
- utm_proxy_auth_profile - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11098).
- utm_proxy_exception - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11098).
- utm_proxy_frontend - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11098).
- utm_proxy_frontend_info - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11098).
- utm_proxy_location - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11098).
- utm_proxy_location_info - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11098).
- utm_utils module utils - improve code by using native Python construct (https://github.com/ansible-collections/community.general/pull/11215).
- utm_utils module utils - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11112).
- vertica_configuration - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11098).
- vertica_configuration - simplify return of boolean values in functions (https://github.com/ansible-collections/community.general/pull/11119).
- vertica_info - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11098).
- vertica_role - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11098).
- vertica_role - simplify return of boolean values in functions (https://github.com/ansible-collections/community.general/pull/11119).
- vertica_schema - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11098).
- vertica_schema - simplify return of boolean values in functions (https://github.com/ansible-collections/community.general/pull/11119).
- vertica_schema - use ``raise ... from ...`` when passing on exceptions (https://github.com/ansible-collections/community.general/pull/11097).
- vertica_user - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11098).
- vertica_user - simplify return of boolean values in functions (https://github.com/ansible-collections/community.general/pull/11119).
- vertica_user - use ``raise ... from ...`` when passing on exceptions (https://github.com/ansible-collections/community.general/pull/11097).
- virtualbox inventory plugin - use ``raise ... from ...`` when passing on exceptions (https://github.com/ansible-collections/community.general/pull/11095).
- vmadm - in case of failure, the module no longer returns the stderr output as ``exception``, but instead as ``stderr``. Other information (``stdout``, ``rc``) is now also returned (https://github.com/ansible-collections/community.general/pull/11149).
- vmadm - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11102).
- wakeonlan - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11098).
- wdc_redfish_command - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11110).
- wdc_redfish_command - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/1114).
- wdc_redfish_info - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11110).
- wdc_redfish_info - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/1114).
- wsl connection plugin - adjust variable name for integration tests (https://github.com/ansible-collections/community.general/pull/11190).
- wsl connection plugin - fix cases of unused variables in loops (https://github.com/ansible-collections/community.general/pull/11115).
- wsl connection plugin - use ``raise ... from ...`` when passing on exceptions (https://github.com/ansible-collections/community.general/pull/11095).
- xbps - fix cases of unused variables in loops (https://github.com/ansible-collections/community.general/pull/11115).
- xbps - simplify return of boolean values in functions (https://github.com/ansible-collections/community.general/pull/11119).
- xcc_redfish_command - fix cases of unused variables in loops (https://github.com/ansible-collections/community.general/pull/11115).
- xcc_redfish_command - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11110).
- xcc_redfish_command - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/1114).
- xenserver module utils - improve code by using native Python construct (https://github.com/ansible-collections/community.general/pull/11215).
- xenserver module utils - simplify return of boolean values in functions (https://github.com/ansible-collections/community.general/pull/11119).
- xenserver_guest modules - replace ``%`` templating with f-strings or ``format()`` (https://github.com/ansible-collections/community.general/pull/11223).
- xml - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11106).
- xml - simplify return of boolean values in functions (https://github.com/ansible-collections/community.general/pull/11119).
- yum_versionlock - remove redundant conversion to unicode in command output (https://github.com/ansible-collections/community.general/pull/11093).
- zfs - simplify return of boolean values in functions (https://github.com/ansible-collections/community.general/pull/11119).
- zone connection plugin - use ``raise ... from ...`` when passing on exceptions (https://github.com/ansible-collections/community.general/pull/11095).

community.postgresql
~~~~~~~~~~~~~~~~~~~~

- postgresql_privs - support MAINTAIN privilege on tables (added in PostgreSQL 17) (https://github.com/ansible-collections/community.postgresql/pull/888).

community.routeros
~~~~~~~~~~~~~~~~~~

- api_info, api_modify - add missing attribute ``radsec-timeout`` for the ``radius`` path which exists since RouterOS version 7.19.6 (https://github.com/ansible-collections/community.routeros/pull/412).
- api_info, api_modify - add support for path ``interface dot1x client`` (https://github.com/ansible-collections/community.routeros/pull/414).
- api_info, api_modify - add support for path ``interface dot1x server`` (https://github.com/ansible-collections/community.routeros/pull/413).
- api_info, api_modify - add support for paths ``ip hotspot``, ``ip hotspot profile``, ``ip hotspot user``, ``ip hotspot user profile``, ``ip hotspot walled-garden``, and ``ip hotspot walled-garden ip`` (https://github.com/ansible-collections/community.routeros/pull/418).
- api_info, api_modify - allow the ``fib`` parameter to be disabled for the ``routing table`` path (https://github.com/ansible-collections/community.routeros/issues/368, https://github.com/ansible-collections/community.routeros/pull/417).
- api_info, api_modify - remove primary key constraint on 'peer' for path ``ip ipsec identity`` (https://github.com/ansible-collections/community.routeros/pull/421).

community.windows
~~~~~~~~~~~~~~~~~

- Add official support for Ansible 2.20

google.cloud
~~~~~~~~~~~~

- gcp_alloydb_* - added gcp_alloydb_cluster, gcp_alloydb_instance, gcp_alloydb_backup, and gcp_alloydb_user modules (https://github.com/ansible-collections/google.cloud/pull/722)

hetzner.hcloud
~~~~~~~~~~~~~~

- DNS support is now generally available.
- load_balancer_network - Add ``ip_range`` argument to attach a load balancer to a specific subnet.
- server_network - Add ``ip_range`` argument to attach a load balancer to a specific subnet.
- txt_record - Add new txt_record filter to help format TXT , e.g. ``"{{ 'v=spf1 include:_spf.example.net ~all' | hetzner.hcloud.txt_record }}"``.

hitachivantara.vspone_block
~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Added a new "hv_sds_block_encryption_environment_setting_facts" module to retrieve encryption environment configuration settings from VSP One SDS Block and Cloud systems.
- Added a new "hv_sds_block_encryption_environment_settings" module to enable or disable encryption functionality on VSP One SDS Block and Cloud systems.
- Added a new "hv_sds_block_encryption_key" module to create and delete encryption keys on VSP One SDS Block and Cloud systems.
- Added a new "hv_sds_block_encryption_key_count_facts" module to retrieve information about the number of encryption keys from VSP One SDS Block and Cloud systems.
- Added a new "hv_sds_block_encryption_key_facts" module to retrieve detailed information about encryption keys from VSP One SDS Block and Cloud systems.
- Added a new "hv_sds_block_protection_domain" module to manage protection domains including creation, modification, and data relocation operations on VSP One SDS Block and Cloud systems.
- Added a new "hv_sds_block_remote_path_group" module to create remote path group, add remote path to a remote path group, remove remote path from remote path group, and delete remote path group on VSP One SDS Block systems.
- Added a new "hv_sds_block_remote_path_group_facts" module to retrieve information about remote path groups from VSP One SDS Block systems.
- Added a new "hv_sds_block_session" module to generate and discard session on VSP One SDS Block and Cloud systems.
- Added a new "hv_sds_block_session_facts" module to retrieve information about sessions on VSP One SDS Block and Cloud systems.
- Added a new "hv_sds_block_snmp_settings" module to manage SNMP settings including agent enablement, version configuration, trap settings, authentication settings, and system group information on VSP One SDS Block and Cloud systems.
- Added a new "hv_sds_block_snmp_settings_facts" module to retrieve SNMP settings including agent status, version configuration, trap settings, authentication settings, and system group information from VSP One SDS Block and Cloud systems.
- Added a new "hv_sds_block_spare_node" module to manage spare node configuration including node identification, fault domain assignment, network configuration, and BMC settings on VSP One SDS Block and Cloud systems.
- Added a new "hv_sds_block_spare_node_facts" module to retrieves spare node information and configuration details from VSP One SDS Block and Cloud systems.
- Added a new "hv_sds_block_storage_system" module to manage storage system configuration including certificate management, cache settings, and other system-level configurations on VSP One SDS Block and Cloud systems.
- Added a new "hv_sds_block_user_group" module to Create and update user groups on VSP One SDS Block and Cloud systems.
- Added a new "hv_sds_block_user_group_facts" module to retrieve user groups from VSP One SDS Block and Cloud systems.
- Added a new "hv_sds_block_web_server" module to manages the web server access setting for VSP One SDS Block and Cloud systems.
- Added a new "hv_sds_block_web_server_facts" module to retrieve the web server access setting from VSP One SDS Block and Cloud systems.
- Added support for latest software version 01.18.02 for VSP One SDS Block and Cloud systems.
- Added support to "Add user to user groups" to hv_sds_block_user module.
- Added support to "Delete a user" to hv_sds_block_user module.
- Added support to "Disable encryption for storage pool using ID" to hv_sds_block_storage_pool module.
- Added support to "Disable encryption for storage pool" to hv_sds_block_storage_pool module.
- Added support to "Enable encryption for storage pool by ID" to hv_sds_block_storage_pool module.
- Added support to "Enable encryption for storage pool by name" to hv_sds_block_storage_pool module.
- Added support to "Remove user from user groups" to hv_sds_block_user module.
- Added support to "Update user settings" to hv_sds_block_user module.

hitachivantara.vspone_object
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Enhanced `hv_storage_component` module to support storage components of type ARRAY for VSP One B20 series storage systems.

microsoft.ad
~~~~~~~~~~~~

- Add official support for Ansible 2.20

microsoft.iis
~~~~~~~~~~~~~

- Add official support for Ansible 2.20

purestorage.flasharray
~~~~~~~~~~~~~~~~~~~~~~

- purefa_connection - Add new parameters for key refresh and connection refresh, as well as ability to update existing connection
- purefa_info - Added more data to hostgroup volume information to support NVMe connections
- purefa_info - Added tags info to entities that support them
- purefa_network - Addressed issues found in update_interface
- purefa_phonehome - Added ``excludes`` parameter, supported from Purity//FA 6.10.0
- purefa_pod - Fixed pydantic issue from lastest SDK version
- purefa_policy - Added Continuous Availability support for SMB policies

telekom_mms.icinga_director
~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Feat: add some parameters to the icinga service module (https://github.com/telekom-mms/ansible-collection-icinga-director/pull/289)

vmware.vmware
~~~~~~~~~~~~~

- content_library_item_info - Add item storage information to item result
- esxi_hosts - Added option to rename reserved variables to avoid potential conflicts with ansible-core and resolve warnings. fixes https://github.com/ansible-collections/vmware.vmware/issues/273
- module_deploy_vm_base - Removed redundant code by using new vm placement service methods in deploy modules
- vm - Add module to manage virtual machines
- vm_apply_customization - Added module to apply different customization specs to a VM
- vms - Added option to rename reserved variables to avoid potential conflicts with ansible-core and resolve warnings. fixes https://github.com/ansible-collections/vmware.vmware/issues/273

Deprecated Features
-------------------

- The ``junipernetworks.junos`` collection has been deprecated.
  It will be removed from Ansible 14 if no one starts maintaining it again before Ansible 14.
  See `Collections Removal Process for unmaintained collections <https://docs.ansible.com/projects/ansible/devel/community/collection_contributors/collection_package_removal.html#unmaintained-collections>`__ for more details (`https://forum.ansible.com/t/44869 <https://forum.ansible.com/t/44869>`__).

community.general
~~~~~~~~~~~~~~~~~

- cloud module utils - this module utils is not used by community.general and will thus be removed from community.general 13.0.0. If you are using it from another collection, please copy it over (https://github.com/ansible-collections/community.general/pull/11205).
- database module utils - this module utils is not used by community.general and will thus be removed from community.general 13.0.0. If you are using it from another collection, please copy it over (https://github.com/ansible-collections/community.general/pull/11205).
- dconf - deprecate fallback mechanism when ``gi.repository`` is not available; fallback will be removed in community.general 15.0.0 (https://github.com/ansible-collections/community.general/pull/11088).
- known_hosts module utils - this module utils is not used by community.general and will thus be removed from community.general 13.0.0. If you are using it from another collection, please copy it over (https://github.com/ansible-collections/community.general/pull/11205).
- layman - ClearLinux was made EOL in July 2025.; the module will be removed from community.general 15.0.0 (https://github.com/ansible-collections/community.general/pull/11087).
- layman - Gentoo deprecated ``layman`` in mid-2023; the module will be removed from community.general 14.0.0 (https://github.com/ansible-collections/community.general/pull/11070).
- pushbullet - module relies on Python package supporting Python 3.2 only; the module will be removed from community.general 13.0.0 (https://github.com/ansible-collections/community.general/pull/11224).
- saslprep module utils - this module utils is not used by community.general and will thus be removed from community.general 13.0.0. If you are using it from another collection, please copy it over (https://github.com/ansible-collections/community.general/pull/11205).
- spotinst_aws_elastigroup - module relies on Python package supporting Python 2.7 only; the module will be removed from community.general 13.0.0 (https://github.com/ansible-collections/community.general/pull/11069).

Bugfixes
--------

Ansible-core
~~~~~~~~~~~~

- Fix ``AnsibleModule.human_to_bytes()``, which was never adjusted after the standalone ``human_to_bytes()`` got a new parameter ``default_unit`` (https://github.com/ansible/ansible/pull/85259).
- Variable loading now uses file source instead of variables when invalidly formmated vars file is loaded.
- ansible-test - The runtime-metadata sanity test now ignores pre-release and build identifiers in collection versions. This prevents errors if a tombstone version is ``X.0.0``, while the collection's version is ``X.0.0-prerelease`` (https://github.com/ansible/ansible/issues/85193)."
- display - Fix ``getuser`` fallback error handling on Python 3.13 and later. (https://github.com/ansible/ansible/issues/86142)
- first_found - Correct the "Include tasks only if one of the files exists, otherwise skip" example.
- get_url - fix regex for GNU Digest line which is used in comparing checksums (https://github.com/ansible/ansible/issues/86132).
- local connection - Fix ``getuser`` fallback error handling on Python 3.13 and later.

ansible.netcommon
~~~~~~~~~~~~~~~~~

- Added support for private key passphrase in libssh connection plugin, when using encrypted private keys specified by the C(ansible_private_key_file) attribute.
- Avoid legacy imports deprecated in ansible-core 2.20 (https://github.com/ansible-collections/ansible.netcommon/pull/720).
- Avoid merging module_defaults for all ansible.netcommon.grpc_* modules.
- Set libssh logging level to DEBUG when Ansible verbosity is greater than 3, to aid in troubleshooting connection issues.

ansible.windows
~~~~~~~~~~~~~~~

- Update various action plugin calls to avoid some deprecated or old methods.
- win_get_url - Fix force=no not doing HEAD request if checksum is not set
- win_powershell - Fix up async support for Ansible 2.19 when running ``win_powershell`` - https://github.com/ansible-collections/ansible.windows/issues/828
- win_reboot - Use full path to ``shutdown.exe`` to avoid relying on ``PATH`` lookups to find - https://github.com/ansible-collections/ansible.windows/issues/826

cisco.aci
~~~~~~~~~

- Fix allowed ranges of interface option in aci_interface_config module.
- Fix descriptions of options in aci_maintenance_policy.
- Fix querying description in aci_l4l7_service_graph_template.

cisco.meraki
~~~~~~~~~~~~

- administered_licensing_subscription_subscriptions_bind - Fixed parameter naming from 'subscription_id' to 'subscriptionId' for proper API compatibility
- meraki.py plugin utils - Added type checking in has_diff_elem2 function to prevent errors when comparing lists of non-dictionary elements
- networks_appliance_content_filtering - Enhanced idempotency by extracting category IDs from blockedUrlCategories before comparison

cisco.mso
~~~~~~~~~

- Fix updates of multicast_route_map_policy in mso_schema_template_vrf_rp.
- Fix updates of multicast_route_map_source_filter and multicast_route_map_destination_filter in mso_schema_template_bd.

cisco.nxos
~~~~~~~~~~

- cisco.nxos.nxos_facts - Fix handling of facts for httapi type connection.
- cisco.nxos.nxos_hsrp_interfaces - Fix parsers for preempt and priority
- cisco.nxos.nxos_l2_interfaces - Fix cdp_enable config parsing.
- cisco.nxos.nxos_l3_interfaces - Improved the code logic for handling redirects.
- cisco.nxos.nxos_snmp_server - fixed communities parsing issue
- cisco.nxos.nxos_static_routes - Fix facts parser to filter inline VRF routes from global route collection preventing incorrect VRF route deletion.

community.dns
~~~~~~~~~~~~~

- Update Public Suffix List.

community.docker
~~~~~~~~~~~~~~~~

- CLI-based modules - when parsing JSON output fails, also provide standard error output. Also provide information on the command and its result in machine-readable way (https://github.com/ansible-collections/community.docker/issues/1216, https://github.com/ansible-collections/community.docker/pull/1221).
- Docker CLI based modules - work around bug in Docker 29.0.0 that caused a breaking change in ``docker version --format json`` output (https://github.com/ansible-collections/community.docker/issues/1185, https://github.com/ansible-collections/community.docker/pull/1187).
- docker_compose_v2, docker_compose_v2_pull - adjust parsing from image pull events to changes in Docker Compose 5.0.0 (https://github.com/ansible-collections/community.docker/pull/1219).
- docker_container - fix ``pull`` idempotency with Docker 29.0.0 (https://github.com/ansible-collections/community.docker/pull/1192).
- docker_container - fix handling of exposed port ranges. So far, the module used an undocumented feature of Docker that was removed from Docker 29.0.0, that allowed to pass the range to the deamon and let handle it. Now the module explodes ranges into a list of all contained ports, same as the Docker CLI does. For backwards compatibility with Docker < 29.0.0, it also explodes ranges returned by the API for existing containers so that comparison should only indicate a difference if the ranges actually change (https://github.com/ansible-collections/community.docker/pull/1192).
- docker_container - fix idempotency for IPv6 addresses with Docker 29.0.0 (https://github.com/ansible-collections/community.docker/pull/1192).
- docker_container - when the same port is mapped more than once for the same protocol without specifying an interface, a bug caused an invalid value to be passed for the interface (https://github.com/ansible-collections/community.docker/issues/1213, https://github.com/ansible-collections/community.docker/pull/1214).
- docker_image - fix ``source=pull`` idempotency with Docker 29.0.0 (https://github.com/ansible-collections/community.docker/pull/1192).
- docker_image, docker_image_push - adjust image push detection to Docker 29 (https://github.com/ansible-collections/community.docker/pull/1199).
- docker_image_pull - fix idempotency with Docker 29.0.0 (https://github.com/ansible-collections/community.docker/pull/1192).
- docker_network - fix idempotency for IPv6 addresses and networks with Docker 29.0.0 (https://github.com/ansible-collections/community.docker/pull/1201).

community.general
~~~~~~~~~~~~~~~~~

- _filelock module utils - add type hints. Fix bug if ``set_lock()`` is called with ``lock_timeout=None`` (https://github.com/ansible-collections/community.general/pull/11222).
- aix_filesystem - remove compatibility code for ancient Python versions (https://github.com/ansible-collections/community.general/pull/11232).
- ansible_type plugin utils - avoid potential concatenation of non-strings when ``alias`` has non-string values (https://github.com/ansible-collections/community.general/pull/11167).
- ansible_type test plugin - fix parameter checking (https://github.com/ansible-collections/community.general/pull/11167).
- cobbler_system - compare the version as a float which is the type returned by the Cobbler API (https://github.com/ansible-collections/community.general/issues/11044).
- datetime module utils - fix bug in ``fromtimestamp()`` that caused the function to crash. This function is not used in community.general (https://github.com/ansible-collections/community.general/pull/11206).
- gitlab module utils - add type hints. Pass API version to python-gitlab as string and not as integer (https://github.com/ansible-collections/community.general/pull/11222).
- homebrew_service - slightly refactor code (https://github.com/ansible-collections/community.general/pull/11168).
- ipinfoio_facts - fix handling of HTTP errors consulting the service (https://github.com/ansible-collections/community.general/pull/11145).
- keys_filter.py plugin utils - fixed requirements check so that other sequences than lists and strings are checked, and corrected broken formatting during error reporting (https://github.com/ansible-collections/community.general/pull/11167).
- mas - parse CLI output correctly when listing installed apps with mas 3.0.0+ (https://github.com/ansible-collections/community.general/pull/11179).
- pam_limits - remove ``%`` templating no longer used in f-string (https://github.com/ansible-collections/community.general/pull/11229).
- xcc_redfish_command - fix templating of dictionary keys as list (https://github.com/ansible-collections/community.general/pull/11144).
- zfs - mark change correctly when updating properties whose current value differs, even if they already have a non-default value (https://github.com/ansible-collections/community.general/issues/11019, https://github.com/ansible-collections/community.general/pull/11172).

community.postgresql
~~~~~~~~~~~~~~~~~~~~

- postgresql_db - Fix connection limit not being set when value is "0" (https://github.com/ansible-collections/community.postgresql/issues/879).
- postgresql_db - fixed ``session_role`` parameter that was being ignored for raw connections (https://github.com/ansible-collections/community.postgresql/pull/865)
- postgresql_db - restoring from ``.sql`` files would execute the file twice. The module now avoids using both ``--file`` and stdin redirection simultaneously (https://github.com/ansible-collections/community.postgresql/issues/882).

community.routeros
~~~~~~~~~~~~~~~~~~

- api_modify, api_info - in the ``routing bgp connection`` and ``bgp templates`` paths, fix spelling of the ``output.remove-private-as`` parameter (https://github.com/ansible-collections/community.routeros/issues/415, https://github.com/ansible-collections/community.routeros/pull/416).
- api_modify, api_info - in the ``routing bgp instance`` path, fix 'Cannot add new entry to this path' error (https://github.com/ansible-collections/community.routeros/issues/409, https://github.com/ansible-collections/community.routeros/pull/420).
- api_modify, api_info - in the ``routing bgp templates`` path, remove ``address-families`` for RouterOS 7.19+ (https://github.com/ansible-collections/community.routeros/issues/415, https://github.com/ansible-collections/community.routeros/pull/416).
- api_modify, api_info - in the ``routing bgp templates`` path, remove ``router-id`` for RouterOS 7.20+ (https://github.com/ansible-collections/community.routeros/issues/415, https://github.com/ansible-collections/community.routeros/pull/416).
- api_modify, api_info - in the ``routing bgp templates`` path, support ``afi`` (RouterOS 7.19+) (RouterOS 7.19 and before) (https://github.com/ansible-collections/community.routeros/issues/415, https://github.com/ansible-collections/community.routeros/pull/416).

community.windows
~~~~~~~~~~~~~~~~~

- Unify the TLS protocol handling logic for the modules that need it to ensure they use the configured OS policies.
- win_disk_facts - fixed an issue when a disk may not have a number (https://github.com/ansible-collections/community.windows/pull/652).
- win_initialize_disk - disks that are formatted but offline cannot be brought online without erasing them (https://github.com/ansible-collections/community.windows/issues/149).
- win_psmodule - Improve error message, if a module exists in multiple repositories - https://github.com/ansible-collections/community.windows/issues/641
- win_psrepository_copy - Fix idempotence check to not rely on .NET runtime implementation details. This should avoid any false positive changed indicators

google.cloud
~~~~~~~~~~~~

- Fix runtime.yml to correctly note Ansible 2.17 minimum version (https://github.com/ansible-collections/google.cloud/pull/730)
- Revert removal of Ansible 2.16 support (https://github.com/ansible-collections/google.cloud/pull/734)
- gcp_secret_manager - return the secret value as type `str` rather than `bytes` (https://github.com/ansible-collections/google.cloud/pull/721)

hetzner.hcloud
~~~~~~~~~~~~~~

- firewall - Ensure idempotency when using non canonical ipv6 representation in Firewall rules.
- zone_rrset - Records order is not guaranteed, the module will not generate a diff if the order of records changes.
- zone_rrset - Records without comments will not generate a diff anymore.

hitachivantara.vspone_block
~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Resolved issue during GAD pair creation when resource lock is enabled.
- Resolved issue with quorum disk creation on VSP One Block 85 storage systems.
- Resolved issue with remote connection creation on VSP One Block 85 storage systems.
- Resolved issue with storage system facts retrieval module for VSP One Block 85 storage systems.
- Various additional bug fixes and enhancements for VSP One Block 85 storage systems.
- Various additional bug fixes and enhancements for VSP One storage systems and VSP One SDS Block storage systems.

inspur.ispim
~~~~~~~~~~~~

- Edit ansible devel version tests to our CI test scripts  (https://github.com/ispim/inspur.ispim/pull/39).
- Modify the automated tests and add support for version 2.18. (https://github.com/ispim/inspur.ispim/pull/40).
- Modify the automated tests and add support for version 2.18. (https://github.com/ispim/inspur.ispim/pull/45).
- Modify the ism.py file in the module_utils directory, and change the reference path of iteritems to be a reference from within Python. (https://github.com/ispim/inspur.ispim/pull/46).

microsoft.ad
~~~~~~~~~~~~

- microsoft.ad.domain_child - Fix return document key so it displays when using the standard Ansible documentation tools.
- microsoft.ad.ldap - Fix issue where auth_protocol config option was never used when creating the spnego client.
- microsoft.ad.service_account - Fix return document key so it displays when using the standard Ansible documentation tools.

microsoft.iis
~~~~~~~~~~~~~

- website_info - Fix error when retrieving website information but none exist - https://github.com/ansible-collections/microsoft.iis/issues/44

purestorage.flasharray
~~~~~~~~~~~~~~~~~~~~~~

- purefa_info - Resolves issue with hosthgroup info when NVMe connected volumes are in a hostgroup

telekom_mms.icinga_director
~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Fix diff in check mode by normalising the boolean values (https://github.com/telekom-mms/ansible-collection-icinga-director/pull/295)
- Fix doc generation and remove need for iteritems (https://github.com/telekom-mms/ansible-collection-icinga-director/pull/296)
- Fix: remove default for states parameter in icinga_dependency_apply (https://github.com/telekom-mms/ansible-collection-icinga-director/pull/290)

vmware.vmware
~~~~~~~~~~~~~

- Fix issue where modules that used the proxy_host and proxy_port arguments were ignoring these arguments when initializing clients. (https://github.com/ansible-collections/vmware.vmware/issues/259)
- Updated common VM deployment module docs to mention that name or MOID can be used for the resource pool, cluster, datastore, and datastore cluster parameters. This allows users to work around issues where the name is not unique. Fixes https://github.com/ansible-collections/vmware.vmware/issues/239
- deploy_content_library_ovf - Remove invalid storage provisioning option 'eagerzeroedthick' from module's argument spec. (Fixes https://github.com/ansible-collections/vmware.vmware/issues/278)

Known Issues
------------

community.docker
~~~~~~~~~~~~~~~~

- docker_image, docker_image_export - idempotency for archiving images depends on whether the image IDs used by the image storage backend correspond to the IDs used in the tarball's ``manifest.json`` files. The new default backend in Docker 29 apparently uses image IDs that no longer correspond, whence idempotency no longer works (https://github.com/ansible-collections/community.docker/pull/1199).

New Modules
-----------

cisco.aci
~~~~~~~~~

- cisco.aci.aci_fabric_node_decommission - Manage the Commissioning and Decommissioning of the Fabric Node (fabric:RsDecommissionNode)
- cisco.aci.aci_management_network_instance_profile - Manage external management network instance profiles (mgmt:InstP).
- cisco.aci.aci_management_network_instance_profile_to_contract - Bind Consumed Contract to External Management Network Instance Profiles (mgmt:RsOoBCons)
- cisco.aci.aci_switch_access_config - Manage Switch Access Policy Configuration of Leaf and Spine nodes (infra:NodeConfig).
- cisco.aci.aci_switch_fabric_config - Manage Switch Fabric Policy Configuration of Leaf and Spine nodes (fabric:NodeConfig).

cisco.mso
~~~~~~~~~

- cisco.mso.ndo_l3out_floating_svi_interface - Manage L3Out Floating SVI Interfaces on Cisco Nexus Dashboard Orchestrator (NDO).
- cisco.mso.ndo_l3out_floating_svi_interface_path_attributes - Manage L3Out Floating SVI Interface Path Attributes on Cisco Nexus Dashboard Orchestrator (NDO).
- cisco.mso.ndo_l3out_secondary_ip - Manage L3Out Secondary IP Address on Cisco Nexus Dashboard Orchestrator (NDO).
- cisco.mso.ndo_l3out_svi_interface - Manage L3Out SVI Interfaces on Cisco Nexus Dashboard Orchestrator (NDO).
- cisco.mso.ndo_match_rule_community_term - Manage Match Community Terms on Cisco Nexus Dashboard Orchestrator (NDO).
- cisco.mso.ndo_match_rule_policy - Manage Match Rule Policies on Cisco Nexus Dashboard Orchestrator (NDO).
- cisco.mso.ndo_match_rule_prefix - Manage Match Prefix List on Cisco Nexus Dashboard Orchestrator (NDO).
- cisco.mso.ndo_route_map_policy_route_control - Manage Route Map Policy for Route Control on Cisco Nexus Dashboard Orchestrator (NDO).
- cisco.mso.ndo_route_map_policy_route_control_context - Manage Route Map Policy for Route Control Context on Cisco Nexus Dashboard Orchestrator (NDO).
- cisco.mso.ndo_set_rule_policy - Manage Tenant Set Rule Policies on Cisco Nexus Dashboard Orchestrator (NDO).

community.general
~~~~~~~~~~~~~~~~~

- community.general.file_remove - Remove files matching a pattern from a directory.
- community.general.lxd_storage_pool_info - Retrieve information about LXD storage pools.
- community.general.lxd_storage_volume_info - Retrieve information about LXD storage volumes.

hitachivantara.vspone_block
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Sds Block
^^^^^^^^^

- hitachivantara.vspone_block.hv_sds_block_encryption_environment_setting_facts - Retrieves encryption environment settings from VSP One SDS Block and Cloud systems.
- hitachivantara.vspone_block.hv_sds_block_encryption_environment_settings - Manages encryption environment settings on VSP One SDS Block and Cloud systems.
- hitachivantara.vspone_block.hv_sds_block_encryption_key - Manage encryption keys on VSP One SDS Block and Cloud systems.
- hitachivantara.vspone_block.hv_sds_block_encryption_key_count_facts - Get encryption key count information from VSP One SDS Block and Cloud systems.
- hitachivantara.vspone_block.hv_sds_block_encryption_key_facts - Retrieves encryption key information from VSP One SDS Block and Cloud systems.
- hitachivantara.vspone_block.hv_sds_block_remote_path_group - Manages remote path groups on VSP One SDS Block and Cloud systems.
- hitachivantara.vspone_block.hv_sds_block_remote_path_group_facts - Get information about remote path groups from VSP One SDS Block and Cloud systems.
- hitachivantara.vspone_block.hv_sds_block_session - Manages sessions on VSP One SDS Block and Cloud systems.
- hitachivantara.vspone_block.hv_sds_block_session_facts - Retrieves information about sessions on VSP One SDS Block and Cloud systems.
- hitachivantara.vspone_block.hv_sds_block_user_group - Create and update user groups on the storage system.
- hitachivantara.vspone_block.hv_sds_block_web_server - Manages the web server access setting for VSP One SDS Block and Cloud systems.
- hitachivantara.vspone_block.hv_sds_block_web_server_facts - Get the web server access setting from VSP One SDS Block and Cloud systems.

Unchanged Collections
---------------------

- amazon.aws (still version 10.1.2)
- ansible.posix (still version 2.1.0)
- ansible.utils (still version 6.0.0)
- arista.eos (still version 12.0.0)
- awx.awx (still version 24.6.1)
- chocolatey.chocolatey (still version 1.5.3)
- cisco.ios (still version 11.1.1)
- cisco.iosxr (still version 12.1.0)
- cisco.ucs (still version 1.16.0)
- cloudscale_ch.cloud (still version 2.5.2)
- community.aws (still version 10.0.0)
- community.ciscosmb (still version 1.0.11)
- community.crypto (still version 3.0.5)
- community.grafana (still version 2.3.0)
- community.hashi_vault (still version 7.1.0)
- community.hrobot (still version 2.7.0)
- community.library_inventory_filtering_v1 (still version 1.1.5)
- community.libvirt (still version 2.0.0)
- community.mongodb (still version 1.7.10)
- community.mysql (still version 4.0.1)
- community.okd (still version 5.0.0)
- community.proxmox (still version 1.4.0)
- community.proxysql (still version 1.7.0)
- community.rabbitmq (still version 1.6.0)
- community.sap_libs (still version 1.5.0)
- community.sops (still version 2.2.7)
- community.vmware (still version 6.1.0)
- community.zabbix (still version 4.1.1)
- containers.podman (still version 1.18.0)
- cyberark.pas (still version 1.0.36)
- dellemc.enterprise_sonic (still version 3.2.0)
- dellemc.openmanage (still version 10.0.1)
- dellemc.powerflex (still version 3.0.0)
- dellemc.unity (still version 2.1.0)
- f5networks.f5_modules (still version 1.39.0)
- fortinet.fortimanager (still version 2.11.0)
- fortinet.fortios (still version 2.4.2)
- grafana.grafana (still version 6.0.6)
- ibm.storage_virtualize (still version 3.1.0)
- ieisystem.inmanage (still version 4.0.0)
- infinidat.infinibox (still version 1.6.3)
- infoblox.nios_modules (still version 1.8.0)
- junipernetworks.junos (still version 11.0.0)
- kaytus.ksmanage (still version 2.0.0)
- kubernetes.core (still version 6.2.0)
- kubevirt.core (still version 2.2.3)
- lowlydba.sqlserver (still version 2.7.0)
- netapp.cloudmanager (still version 21.24.0)
- netapp.ontap (still version 23.2.0)
- netapp.storagegrid (still version 21.15.0)
- netapp_eseries.santricity (still version 1.4.1)
- netbox.netbox (still version 3.21.0)
- ngine_io.cloudstack (still version 3.0.0)
- openstack.cloud (still version 2.5.0)
- ovirt.ovirt (still version 3.2.1)
- purestorage.flashblade (still version 1.22.0)
- ravendb.ravendb (still version 1.0.4)
- splunk.es (still version 4.0.0)
- theforeman.foreman (still version 5.7.0)
- vmware.vmware_rest (still version 4.9.0)
- vultr.cloud (still version 1.13.0)
- vyos.vyos (still version 6.0.0)
- wti.remote (still version 1.0.10)

v13.0.0
=======

.. contents::
  :local:
  :depth: 2

Release Summary
---------------

Release Date: 2025-11-19

`Porting Guide <https://docs.ansible.com/projects/ansible/devel/porting_guides.html>`_

Removed Collections
-------------------

- community.digitalocean (previously included version: 1.27.0)
- ibm.qradar (previously included version: 4.0.0)

You can still install a removed collection manually with ``ansible-galaxy collection install <name-of-collection>``.

Added Collections
-----------------

- hitachivantara.vspone_object (version 1.0.0)
- ravendb.ravendb (version 1.0.4)

Ansible-core
------------

Ansible 13.0.0 contains ansible-core version 2.20.0.
This is a newer version than version 2.19.1 contained in the previous Ansible release.

The changes are reported in the combined changelog below.

Included Collections
--------------------

If not mentioned explicitly, the changes are reported in the combined changelog below.

+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Collection                               | Ansible 12.0.0 | Ansible 13.0.0 | Notes                                                                                                                                                                                                           |
+==========================================+================+================+=================================================================================================================================================================================================================+
| amazon.aws                               | 10.1.1         | 10.1.2         |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| azure.azcollection                       | 3.8.0          | 3.10.1         | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.                                                                                    |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| check_point.mgmt                         | 6.4.1          | 6.6.0          |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cisco.dnac                               | 6.39.0         | 6.41.0         |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cisco.intersight                         | 2.2.0          | 2.7.0          | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.                                                                                    |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cisco.ios                                | 11.0.0         | 11.1.1         |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cisco.iosxr                              | 12.0.0         | 12.1.0         |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cisco.meraki                             | 2.21.4         | 2.21.8         |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.crypto                         | 3.0.3          | 3.0.5          |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.dns                            | 3.3.2          | 3.4.0          |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.docker                         | 4.7.0          | 5.0.1          |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.general                        | 11.2.1         | 12.0.1         |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.hashi_vault                    | 7.0.0          | 7.1.0          |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.hrobot                         | 2.5.0          | 2.7.0          |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.library_inventory_filtering_v1 | 1.1.1          | 1.1.5          |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.mysql                          | 3.15.0         | 4.0.1          |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.proxmox                        | 1.3.0          | 1.4.0          |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.proxysql                       | 1.6.0          | 1.7.0          |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.routeros                       | 3.10.0         | 3.13.0         |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.sap_libs                       | 1.4.2          | 1.5.0          |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.sops                           | 2.2.2          | 2.2.7          |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.vmware                         | 5.7.2          | 6.1.0          |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.zabbix                         | 4.1.0          | 4.1.1          |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| containers.podman                        | 1.17.0         | 1.18.0         |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cyberark.conjur                          | 1.3.7          | 1.3.8          | You can find the collection's changelog at `https://github.com/cyberark/ansible-conjur-collection/blob/master/CHANGELOG.md <https://github.com/cyberark/ansible-conjur-collection/blob/master/CHANGELOG.md>`__. |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cyberark.pas                             | 1.0.35         | 1.0.36         | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.                                                                                    |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| dellemc.enterprise_sonic                 | 3.0.0          | 3.2.0          |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| dellemc.openmanage                       | 9.12.3         | 10.0.1         |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| dellemc.powerflex                        | 2.6.1          | 3.0.0          |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| f5networks.f5_modules                    | 1.38.0         | 1.39.0         | There are no changes recorded in the changelog.                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| fortinet.fortimanager                    | 2.10.0         | 2.11.0         |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| fortinet.fortios                         | 2.4.0          | 2.4.2          |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| google.cloud                             | 1.7.0          | 1.9.0          |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| grafana.grafana                          | 6.0.3          | 6.0.6          |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| hetzner.hcloud                           | 5.2.0          | 6.0.0          |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| hitachivantara.vspone_block              | 4.1.0          | 4.4.0          |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| hitachivantara.vspone_object             |                | 1.0.0          | The collection was added to Ansible                                                                                                                                                                             |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ibm.storage_virtualize                   | 2.7.4          | 3.1.0          |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ieisystem.inmanage                       | 3.0.0          | 4.0.0          |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| kubernetes.core                          | 6.1.0          | 6.2.0          |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| netapp.ontap                             | 23.1.0         | 23.2.0         |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ngine_io.cloudstack                      | 2.5.0          | 3.0.0          |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| openstack.cloud                          | 2.4.1          | 2.5.0          | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.                                                                                    |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| purestorage.flasharray                   | 1.36.0         | 1.39.0         |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| purestorage.flashblade                   | 1.20.0         | 1.22.0         |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ravendb.ravendb                          |                | 1.0.4          | The collection was added to Ansible                                                                                                                                                                             |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| theforeman.foreman                       | 5.5.0          | 5.7.0          |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| vmware.vmware                            | 2.3.0          | 2.4.0          |                                                                                                                                                                                                                 |
+------------------------------------------+----------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

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
- Replace ``ansible.module_utils._text`` (https://github.com/ansible-collections/community.vmware/issues/2497).
- Replace ``ansible.module_utils.common._collections_compat`` (https://github.com/ansible-collections/community.vmware/issues/2497).
- Replace ``ansible.module_utils.six`` (https://github.com/ansible-collections/community.vmware/pull/2495).

containers.podman
~~~~~~~~~~~~~~~~~

- Add inventory plugins for buildah and podman
- Add podman system connection modules

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- The OpenManage Enterprise, OpenManage Enterprise Modular and OpenManage Enterprise Integration for VMware vCenter modules are now compatible with Ansible Core version 2.19.
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

fortinet.fortios
~~~~~~~~~~~~~~~~

- Supported default_group feature for the all of the modules.
- Supported new versions 7.6.3 and 7.6.4.
- Supported the authentication method when using username and password in v7.6.4.

grafana.grafana
~~~~~~~~~~~~~~~

- Add SUSE support to Alloy role by @pozsa in https://github.com/grafana/grafana-ansible-collection/pull/423
- Fallback to empty dict in case grafana_ini is undefined by @root-expert in https://github.com/grafana/grafana-ansible-collection/pull/403
- Fix Mimir config file validation task by @Windos in https://github.com/grafana/grafana-ansible-collection/pull/428
- Fixes issue by @digiserg in https://github.com/grafana/grafana-ansible-collection/pull/421
- Fixes to foldersFromFilesStructure option by @root-expert in https://github.com/grafana/grafana-ansible-collection/pull/351
- Import custom dashboards only when directory exists by @mahendrapaipuri in https://github.com/grafana/grafana-ansible-collection/pull/430
- Migrate RedHat install to ansible.builtin.package by @r65535 in https://github.com/grafana/grafana-ansible-collection/pull/431
- Restore default listen address and port in Mimir by @56quarters in https://github.com/grafana/grafana-ansible-collection/pull/456
- Updated YUM repo urls from `packages.grafana.com` to `rpm.grafana.com` by @DejfCold in https://github.com/grafana/grafana-ansible-collection/pull/414
- Use credentials from grafana_ini when importing dashboards by @root-expert in https://github.com/grafana/grafana-ansible-collection/pull/402
- add macOS support to alloy role by @l50 in https://github.com/grafana/grafana-ansible-collection/pull/418
- do not skip scrape latest github version even in check_mode by @cmehat in https://github.com/grafana/grafana-ansible-collection/pull/408
- fix broken Grafana apt repository addition by @kleini in https://github.com/grafana/grafana-ansible-collection/pull/454
- fix datasource documentation by @jeremad in https://github.com/grafana/grafana-ansible-collection/pull/437
- fix mimir_download_url_deb & mimir_download_url_rpm by @germebl in https://github.com/grafana/grafana-ansible-collection/pull/400
- replace None with [] for safe length checks by @voidquark in https://github.com/grafana/grafana-ansible-collection/pull/426
- update catalog info by @Duologic in https://github.com/grafana/grafana-ansible-collection/pull/434
- use deb822 for newer debian versions by @Lukas-Heindl in https://github.com/grafana/grafana-ansible-collection/pull/440

ieisystem.inmanage
~~~~~~~~~~~~~~~~~~

- The edit_m6_log_setting.py module has added the 'server_status' attribute; The edit_network_bond.py module modifies the attribute descriptions; The edit_snmp.py and edit_snmp_trap.py module modifies the allowable value ranges for the auth_protocol and priv_protocol attributes. (https://github.com/ieisystem/ieisystem.inmanage/pull/30).

ngine_io.cloudstack
~~~~~~~~~~~~~~~~~~~

- Ensuring backwards compatibility and integration tests with CloudStack 4.17 and 4.18.
- General overhaul (black code style) and renaming of all modules (dropping ``cs_`` prefix) (https://github.com/ngine-io/ansible-collection-cloudstack/pull/141).
- Update cs dependency to >=3.4.0.

Minor Changes
-------------

Ansible-core
~~~~~~~~~~~~

- Add tech preview play argument spec validation, which can be enabled by setting the play keyword ``validate_argspec`` to ``True`` or the name of an argument spec. When ``validate_argspec`` is set to ``True``, a play ``name`` is required and used as the argument spec name. When enabled, the argument spec is loaded from a file matching the pattern <playbook_name>.meta.yml. At minimum, this file should contain ``{"argument_specs": {"name": {"options": {}}}}``, where "name" is the name of the play or configured argument spec.
- Added Univention Corporate Server as a part of Debian OS distribution family (https://github.com/ansible/ansible/issues/85490).
- AnsibleModule - Add temporary internal monkeypatch-able hook to alter module result serialization by splitting serialization from ``_return_formatted`` into ``_record_module_result``.
- DataLoader - Update ``DataLoader.get_basedir`` to be an abspath
- Python type hints applied to ``to_text`` and ``to_bytes`` functions for better type hint interactions with code utilizing these functions.
- ansible now warns if you use reserved tags that were only meant for selection and not for use in play.
- ansible-doc - Return a more verbose error message when the ``description`` field is missing.
- ansible-doc - show ``notes``, ``seealso``, and top-level ``version_added`` for role entrypoints (https://github.com/ansible/ansible/pull/81796).
- ansible-doc adds support for RETURN documentation to support doc fragment plugins
- ansible-test - Default to Python 3.14 in the ``base`` and ``default`` test containers.
- ansible-test - Filter out pylint messages for invalid filenames and display a notice when doing so.
- ansible-test - Implement new authentication methods for accessing the Ansible Core CI service.
- ansible-test - Improve formatting of generated coverage config file.
- ansible-test - Removed support for automatic provisioning of obsolete instances for network-integration tests.
- ansible-test - Replace FreeBSD 14.2 with 14.3.
- ansible-test - Replace RHEL 9.5 with 9.6.
- ansible-test - Update Ubuntu containers.
- ansible-test - Update astroid imports in custom pylint checkers.
- ansible-test - Update base/default containers to include Python 3.14.0.
- ansible-test - Update default containers.
- ansible-test - Update pinned ``pip`` version to 25.2.
- ansible-test - Update pinned sanity test requirements, including upgrading to pylint 4.0.0.
- ansible-test - Update pinned sanity test requirements.
- ansible-test - Update test containers.
- ansible-test - Update the pylint sanity test to pylint 4.0.2.
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
- known_hosts - return rc and stderr when ssh-keygen command fails for further debugging (https://github.com/ansible/ansible/issues/85850).
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

- Support check mode (--check)
- added new parameter 'ips_settings' to 'cp_mgmt_simple_cluster' and 'cp_mgmt_simple_gateway' modules.
- added new parameter 'override_vpn_domains' to 'cp_mgmt_set_vpn_community_remote_access' module.
- added new parameter 'show_installation_targets' to 'cp_mgmt_package_facts' module.
- added new parameters (such as 'permanent_tunnels', excluded_services, etc.) to 'cp_mgmt_vpn_community_meshed' and 'cp_mgmt_vpn_community_star' modules.
- check_point.mgmt.cp_mgmt_access_rule_facts - support async-response with customized HF.

cisco.dnac
~~~~~~~~~~

- Added attribute 'slots' in assurance_icap_settings_workflow_manager module
- Added attribute 'transit_site_hierarchy' in sda_fabric_transits_workflow_manager module
- Added attribute native_vlan_id and allowed_vlan_ranges in sda_host_port_onboarding_workflow_manager module
- Added attributes 'wireless_flooding_enable', 'resource_guard_enable', 'flooding_address_assignment', 'flooding_address' in sda_fabric_transits_workflow_manager module
- Changes in assurance_icap_settings_workflow_manager module
- Changes in assurance_issue_workflow_manager module
- Changes in inventory_workflow_manager module
- Changes in network_profile_switching_workflow_manager module
- Changes in network_settings_workflow_manager module
- Changes in path_trace_workflow_manager module
- Changes in sda_fabric_devices_workflow_manager module
- Changes in sda_fabric_sites_zones_workflow_manager module
- Changes in sda_fabric_transits_workflow_manager module
- Changes in sda_fabric_virtual_networks_workflow_manager module
- Changes in sda_host_port_onboarding_workflow_manager module
- Changes in sda_virtual_networks_workflow_manager module
- Changes in template_workflow_manager module
- Changes limit and offset from float to int in all info modules
- Removed attribute 'slot' in assurance_icap_settings_workflow_manager module

cisco.ios
~~~~~~~~~

- ios_config - added answering prompt functionality while working in config mode on ios device
- ios_facts - Add chassis_id value to ansible_net_neighbors dictionary for lldp neighbours.

cisco.iosxr
~~~~~~~~~~~

- Added few parameters to iosxr_l3_interface module to support new features.

community.dns
~~~~~~~~~~~~~

- Note that some new code in ``plugins/module_utils/_six.py`` is MIT licensed (https://github.com/ansible-collections/community.dns/pull/287).
- lookup_* plugins - support ``type=HTTPS`` and ``type=SVCB`` (https://github.com/ansible-collections/community.dns/issues/299, https://github.com/ansible-collections/community.dns/pull/300).
- nameserver_record_info - support ``type=HTTPS`` and ``type=SVCB`` (https://github.com/ansible-collections/community.dns/issues/299, https://github.com/ansible-collections/community.dns/pull/300).
- nameserver_record_info - the return value ``results[].result[].values`` has been renamed to ``results[].result[].entries``. The old name will still be available for a longer time (https://github.com/ansible-collections/community.dns/issues/289, https://github.com/ansible-collections/community.dns/pull/298).
- wait_for_txt - the option ``records[].values`` now has an alias ``records[].entries`` (https://github.com/ansible-collections/community.dns/pull/298).
- wait_for_txt - the return value ``records[].values`` has been renamed to ``records[].entries``. The old name will still be available for a longer time (https://github.com/ansible-collections/community.dns/issues/289, https://github.com/ansible-collections/community.dns/pull/298).

community.docker
~~~~~~~~~~~~~~~~

- Note that some new code in ``plugins/module_utils/_six.py`` is MIT licensed (https://github.com/ansible-collections/community.docker/pull/1138).
- docker_container - add ``driver_opts`` option in ``networks`` (https://github.com/ansible-collections/community.docker/issues/1142, https://github.com/ansible-collections/community.docker/pull/1143).
- docker_container - add ``gw_priority`` option in ``networks`` (https://github.com/ansible-collections/community.docker/issues/1142, https://github.com/ansible-collections/community.docker/pull/1143).
- docker_container - support missing fields and new mount types in ``mounts`` (https://github.com/ansible-collections/community.docker/issues/1129, https://github.com/ansible-collections/community.docker/pull/1134).

community.general
~~~~~~~~~~~~~~~~~

- Modernize code for Python 3.7+. This includes code reformatting, and adding new checks to CI, including a type checker (mypy). Most of the code does not have type hints yet, but now it is possible to add typing hints and have these validated (https://github.com/ansible-collections/community.general/pull/10285, https://github.com/ansible-collections/community.general/pull/10886, https://github.com/ansible-collections/community.general/pull/10891, https://github.com/ansible-collections/community.general/pull/10892, https://github.com/ansible-collections/community.general/pull/10897, https://github.com/ansible-collections/community.general/pull/10899, https://github.com/ansible-collections/community.general/pull/10902, https://github.com/ansible-collections/community.general/pull/10903, https://github.com/ansible-collections/community.general/pull/10904, https://github.com/ansible-collections/community.general/pull/10907, https://github.com/ansible-collections/community.general/pull/10908, https://github.com/ansible-collections/community.general/pull/10909, https://github.com/ansible-collections/community.general/pull/10939, https://github.com/ansible-collections/community.general/pull/10940, https://github.com/ansible-collections/community.general/pull/10941, https://github.com/ansible-collections/community.general/pull/10942, https://github.com/ansible-collections/community.general/pull/10945, https://github.com/ansible-collections/community.general/pull/10947, https://github.com/ansible-collections/community.general/pull/10958, https://github.com/ansible-collections/community.general/pull/10959, https://github.com/ansible-collections/community.general/pull/10968, https://github.com/ansible-collections/community.general/pull/10969, https://github.com/ansible-collections/community.general/pull/10970, https://github.com/ansible-collections/community.general/pull/10971, https://github.com/ansible-collections/community.general/pull/10973, https://github.com/ansible-collections/community.general/pull/10974, https://github.com/ansible-collections/community.general/pull/10975, https://github.com/ansible-collections/community.general/pull/10976, https://github.com/ansible-collections/community.general/pull/10977, https://github.com/ansible-collections/community.general/pull/10978, https://github.com/ansible-collections/community.general/pull/10979, https://github.com/ansible-collections/community.general/pull/10980, https://github.com/ansible-collections/community.general/pull/10981, https://github.com/ansible-collections/community.general/pull/10992, https://github.com/ansible-collections/community.general/pull/10993, https://github.com/ansible-collections/community.general/pull/10997, https://github.com/ansible-collections/community.general/pull/10999, https://github.com/ansible-collections/community.general/pull/11015, https://github.com/ansible-collections/community.general/pull/11016, https://github.com/ansible-collections/community.general/pull/11017).
- aerospike_migrations - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10494).
- airbrake_deployment - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10494).
- android_sdk - minor refactor to improve readability (https://github.com/ansible-collections/community.general/pull/10712).
- apk - using safer mechanism to run external command (https://github.com/ansible-collections/community.general/issues/10479, https://github.com/ansible-collections/community.general/pull/10520).
- bigpanda - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10494).
- bootc_manage - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10494).
- bower - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10494).
- btrfs_subvolume - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10494).
- bundler - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10494).
- bzr - using safer mechanism to run external command (https://github.com/ansible-collections/community.general/pull/10523).
- campfire - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10494).
- capabilities - using safer mechanism to run external command (https://github.com/ansible-collections/community.general/pull/10524).
- cargo - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10494).
- catapult - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10494).
- cisco_webex - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10494).
- cloudflare_dns - adds support for PTR records (https://github.com/ansible-collections/community.general/pull/10267).
- cloudflare_dns - remove redundant brackets in conditionals, no functional changes (https://github.com/ansible-collections/community.general/pull/10328).
- cloudflare_dns - simplify validations and refactor some code, no functional changes (https://github.com/ansible-collections/community.general/pull/10269).
- composer - using safer mechanism to run external command (https://github.com/ansible-collections/community.general/pull/10525).
- consul_kv - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10494).
- consul_policy - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10494).
- copr - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10494).
- crypttab - remove redundant brackets in conditionals, no functional changes (https://github.com/ansible-collections/community.general/pull/10328).
- datadog_downtime - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10494).
- datadog_monitor - remove redundant brackets in conditionals, no functional changes (https://github.com/ansible-collections/community.general/pull/10328).
- datadog_monitor - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10494).
- datetime module utils - remove code for unsupported Python version (https://github.com/ansible-collections/community.general/pull/11048).
- dconf - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10494).
- dimensiondata_network - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10494).
- dimensiondata_vlan - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10494).
- django module utils - remove deprecated parameter ``_DjangoRunner`` call (https://github.com/ansible-collections/community.general/pull/10574).
- django module utils - simplify/consolidate the common settings for the command line (https://github.com/ansible-collections/community.general/pull/10684).
- django_check - rename parameter ``database`` to ``databases``, add alias for compatibility (https://github.com/ansible-collections/community.general/pull/10700).
- django_check - simplify/consolidate the common settings for the command line (https://github.com/ansible-collections/community.general/pull/10684).
- django_createcachetable - simplify/consolidate the common settings for the command line (https://github.com/ansible-collections/community.general/pull/10684).
- dnf_config_manager - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10494).
- dnsimple_info - use Ansible construct to validate parameters (https://github.com/ansible-collections/community.general/pull/11052).
- dnsmadeeasy - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10494).
- dpkg_divert - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10494).
- easy_install - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10494).
- easy_install - using safer mechanism to run external command (https://github.com/ansible-collections/community.general/pull/10526).
- elasticsearch_plugin - minor refactor to improve readability (https://github.com/ansible-collections/community.general/pull/10712).
- elasticsearch_plugin - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10494).
- facter - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10494).
- filesize - minor refactor to simplify string formatting (https://github.com/ansible-collections/community.general/pull/10727).
- filesystem - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10494).
- filetree - add ``exclude`` option (https://github.com/ansible-collections/community.general/issues/10936, https://github.com/ansible-collections/community.general/pull/10936).
- gem - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10505).
- git_config_info - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10505).
- github_app_access_token lookup plugin - add support for GitHub Enterprise Server (https://github.com/ansible-collections/community.general/issues/10879, https://github.com/ansible-collections/community.general/pull/10880).
- github_app_access_token lookup plugin - support both ``jwt`` and ``pyjwt`` to avoid conflict with other modules requirements (https://github.com/ansible-collections/community.general/issues/10299).
- github_deploy_key - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10505).
- github_repo - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10505).
- github_webhook - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10505).
- github_webhook_info - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10505).
- gitlab_branch - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10505).
- gitlab_deploy_key - remove redundant brackets in conditionals, no functional changes (https://github.com/ansible-collections/community.general/pull/10328).
- gitlab_group_access_token - add ``planner`` access level (https://github.com/ansible-collections/community.general/pull/10679).
- gitlab_group_access_token - add missing scopes (https://github.com/ansible-collections/community.general/pull/10785).
- gitlab_group_access_token - remove redundant brackets in conditionals, no functional changes (https://github.com/ansible-collections/community.general/pull/10328).
- gitlab_group_access_token - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10505).
- gitlab_group_variable - add ``description`` option (https://github.com/ansible-collections/community.general/pull/10812).
- gitlab_group_variable - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10505).
- gitlab_group_variable - support masked-and-hidden variables (https://github.com/ansible-collections/community.general/pull/10787).
- gitlab_hook - remove redundant brackets in conditionals, no functional changes (https://github.com/ansible-collections/community.general/pull/10328).
- gitlab_hook - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10505).
- gitlab_instance_variable - add ``description`` option (https://github.com/ansible-collections/community.general/pull/10812).
- gitlab_instance_variable - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10505).
- gitlab_issue - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10505).
- gitlab_label - minor refactor to improve readability (https://github.com/ansible-collections/community.general/pull/10711).
- gitlab_label - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10505).
- gitlab_merge_request - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10505).
- gitlab_milestone - minor refactor to improve readability (https://github.com/ansible-collections/community.general/pull/10711).
- gitlab_milestone - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10505).
- gitlab_project - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10505).
- gitlab_project_access_token - add ``planner`` access level (https://github.com/ansible-collections/community.general/pull/10679).
- gitlab_project_access_token - add missing scopes (https://github.com/ansible-collections/community.general/pull/10785).
- gitlab_project_access_token - remove redundant brackets in conditionals, no functional changes (https://github.com/ansible-collections/community.general/pull/10328).
- gitlab_project_access_token - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10505).
- gitlab_project_variable - add ``description`` option (https://github.com/ansible-collections/community.general/pull/10812, https://github.com/ansible-collections/community.general/issues/8584, https://github.com/ansible-collections/community.general/issues/10809).
- gitlab_project_variable - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10505).
- gitlab_project_variable - support masked-and-hidden variables (https://github.com/ansible-collections/community.general/pull/10787).
- gitlab_protected_branch - add ``allow_force_push``, ``code_owner_approval_required`` (https://github.com/ansible-collections/community.general/pull/10795, https://github.com/ansible-collections/community.general/issues/6432, https://github.com/ansible-collections/community.general/issues/10289, https://github.com/ansible-collections/community.general/issues/10765).
- gitlab_protected_branch - update protected branches if possible instead of recreating them (https://github.com/ansible-collections/community.general/pull/10795).
- gitlab_runner - remove redundant brackets in conditionals, no functional changes (https://github.com/ansible-collections/community.general/pull/10328).
- grove - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10505).
- hg - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10505).
- homebrew - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10505).
- homebrew_cask - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10505).
- homebrew_tap - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10505).
- honeybadger_deployment - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10505).
- htpasswd - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10505).
- icinga2_host - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10505).
- imgadm - using safer mechanism to run external command (https://github.com/ansible-collections/community.general/pull/10536).
- infinity - consolidate double and triple whitespaces (https://github.com/ansible-collections/community.general/pull/11029).
- influxdb_user - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10505).
- ini_file - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10505).
- iocage inventory plugin - minor refactor to improve readability (https://github.com/ansible-collections/community.general/pull/10712).
- ipa_dnsrecord - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10505).
- ipa_dnszone - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10505).
- ipa_group - remove redundant brackets in conditionals, no functional changes (https://github.com/ansible-collections/community.general/pull/10328).
- ipa_host - add ``userclass`` and ``locality`` parameters (https://github.com/ansible-collections/community.general/pull/10935).
- ipa_host - minor refactor to improve readability (https://github.com/ansible-collections/community.general/pull/10711).
- ipa_otptoken - consolidate double and triple whitespaces (https://github.com/ansible-collections/community.general/pull/11029).
- ipa_service - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10505).
- ipbase_info - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10505).
- iptables_state - minor refactor to simplify string formatting (https://github.com/ansible-collections/community.general/pull/10727).
- ipwcli_dns - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10505).
- irc - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10505).
- irc - use proper boolean value in loops (https://github.com/ansible-collections/community.general/pull/11076).
- jabber - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10505).
- java_keystore - remove redundant function (https://github.com/ansible-collections/community.general/pull/10905).
- jenkins_build - remove redundant brackets in conditionals, no functional changes (https://github.com/ansible-collections/community.general/pull/10328).
- jenkins_build_info - remove redundant brackets in conditionals, no functional changes (https://github.com/ansible-collections/community.general/pull/10328).
- jenkins_credential - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10505).
- jenkins_job - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10505).
- jenkins_node - remove code for unsupported Python version (https://github.com/ansible-collections/community.general/pull/11048).
- jenkins_plugin - install dependencies for specific version (https://github.com/ansible-collections/community.general/issue/4995, https://github.com/ansible-collections/community.general/pull/10346).
- jenkins_script - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10505).
- keycloak - add support for ``grant_type=client_credentials`` to all keycloak modules, so that specifying ``auth_client_id`` and ``auth_client_secret`` is sufficient for authentication (https://github.com/ansible-collections/community.general/pull/10231).
- keycloak module utils - remove redundant brackets in conditionals, no functional changes (https://github.com/ansible-collections/community.general/pull/10328).
- keycloak_authz_authorization_scope - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10507).
- keycloak_authz_permission - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10507).
- keycloak_client - add idempotent support for ``optional_client_scopes`` and ``optional_client_scopes``, and ensure consistent change detection between check mode and live run (https://github.com/ansible-collections/community.general/issues/5495, https://github.com/ansible-collections/community.general/pull/10842).
- keycloak_identity_provider – add support for ``fromUrl`` to automatically fetch OIDC endpoints from the well-known discovery URL, simplifying identity provider configuration (https://github.com/ansible-collections/community.general/pull/10527).
- keycloak_realm - add support for WebAuthn policy configuration options, including both regular and passwordless WebAuthn policies (https://github.com/ansible-collections/community.general/pull/10791).
- keycloak_realm - add support for ``brute_force_strategy`` and ``max_temporary_lockouts`` (https://github.com/ansible-collections/community.general/issues/10412, https://github.com/ansible-collections/community.general/pull/10415).
- keycloak_realm - add support for client-related options and Oauth2 device (https://github.com/ansible-collections/community.general/pull/10538).
- keycloak_role - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10507).
- keycloak_user - return user created boolean flag (https://github.com/ansible-collections/community.general/pull/10950).
- keycloak_userprofile - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10507).
- keyring - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10507).
- kibana_plugin - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10507).
- layman - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10507).
- ldap_attrs - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10507).
- ldap_inc - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10507).
- librato_annotation - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10507).
- linode module utils - remove redundant code for ancient versions of Ansible (https://github.com/ansible-collections/community.general/pull/10906).
- lldp - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10507).
- logentries - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10507).
- logstash callback plugin - remove redundant brackets in conditionals, no functional changes (https://github.com/ansible-collections/community.general/pull/10328).
- logstash_plugin - using safer mechanism to run external command (https://github.com/ansible-collections/community.general/issues/10479, https://github.com/ansible-collections/community.general/pull/10520).
- lvg_rename - minor refactor to improve readability (https://github.com/ansible-collections/community.general/pull/10711).
- lxca_cmms - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10507).
- lxca_nodes - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10507).
- macports - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10507).
- mail - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10507).
- manageiq - minor refactor to improve readability (https://github.com/ansible-collections/community.general/pull/10712).
- manageiq_alert_profiles - minor refactor to improve readability (https://github.com/ansible-collections/community.general/pull/10712).
- manageiq_alerts - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10507).
- manageiq_group - minor refactor to simplify string formatting (https://github.com/ansible-collections/community.general/pull/10727).
- manageiq_group - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10507).
- manageiq_policies - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10507).
- manageiq_policies_info - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10507).
- manageiq_tags - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10507).
- manageiq_tenant - minor refactor to simplify string formatting (https://github.com/ansible-collections/community.general/pull/10727).
- manageiq_tenant - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10507).
- matrix - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10507).
- mattermost - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10507).
- maven_artifact - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10507).
- memset_dns_reload - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10507).
- memset_zone - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10507).
- memset_zone_record - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10507).
- mqtt - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10507).
- mssql_db - minor refactor to simplify string formatting (https://github.com/ansible-collections/community.general/pull/10727).
- mssql_db - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10507).
- mssql_script - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10507).
- nagios - make parameter ``services`` a ``list`` instead of a ``str`` (https://github.com/ansible-collections/community.general/pull/10493).
- netcup_dns - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10507).
- newrelic_deployment - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10507).
- nmcli - remove redundant brackets in conditionals, no functional changes (https://github.com/ansible-collections/community.general/pull/10328).
- nmcli - simplify validations and refactor some code, no functional changes (https://github.com/ansible-collections/community.general/pull/10323).
- npm - improve parameter validation using Ansible construct (https://github.com/ansible-collections/community.general/pull/10983).
- nsupdate - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10507).
- oci_vcn - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10512).
- one_image_info - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10512).
- one_template - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10512).
- one_vm - minor refactor to improve readability (https://github.com/ansible-collections/community.general/pull/10712).
- one_vnet - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10512).
- oneandone_firewall_policy - remove redundant brackets in conditionals, no functional changes (https://github.com/ansible-collections/community.general/pull/10328).
- oneandone_load_balancer - remove redundant brackets in conditionals, no functional changes (https://github.com/ansible-collections/community.general/pull/10328).
- oneandone_monitoring_policy - remove redundant brackets in conditionals, no functional changes (https://github.com/ansible-collections/community.general/pull/10328).
- onepassword_info - remove redundant brackets in conditionals, no functional changes (https://github.com/ansible-collections/community.general/pull/10328).
- onepassword_info - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10512).
- oneview_fc_network_info - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10512).
- open_iscsi - using safer mechanism to run external command (https://github.com/ansible-collections/community.general/pull/10599).
- openbsd_pkg - add ``autoremove`` parameter to remove unused dependencies (https://github.com/ansible-collections/community.general/pull/10705).
- openbsd_pkg - minor refactor to simplify string formatting (https://github.com/ansible-collections/community.general/pull/10727).
- opendj_backendprop - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10512).
- opendj_backendprop - use Ansible construct to perform check for external commands (https://github.com/ansible-collections/community.general/pull/11072).
- osx_defaults - remove redundant brackets in conditionals, no functional changes (https://github.com/ansible-collections/community.general/pull/10328).
- ovh_ip_loadbalancing_backend - remove redundant brackets in conditionals, no functional changes (https://github.com/ansible-collections/community.general/pull/10328).
- ovh_monthly_billing - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10512).
- pacemaker_cluster - add ``state=maintenance`` for managing pacemaker maintenance mode (https://github.com/ansible-collections/community.general/issues/10200, https://github.com/ansible-collections/community.general/pull/10227).
- pacemaker_cluster - rename ``node`` to ``name`` and add ``node`` alias (https://github.com/ansible-collections/community.general/pull/10227).
- pacemaker_resource - add ``state=cleanup`` for cleaning up pacemaker resources (https://github.com/ansible-collections/community.general/pull/10413)
- pacemaker_resource - add ``state=cloned`` for cloning pacemaker resources or groups (https://github.com/ansible-collections/community.general/issues/10322, https://github.com/ansible-collections/community.general/pull/10665).
- pacemaker_resource - enhance module by removing duplicative code (https://github.com/ansible-collections/community.general/pull/10227).
- pacemaker_resource - the parameter ``name`` is no longer a required parameter in community.general 11.3.0 (https://github.com/ansible-collections/community.general/pull/10413)
- packet_device - remove redundant brackets in conditionals, no functional changes (https://github.com/ansible-collections/community.general/pull/10328).
- pagerduty - remove redundant brackets in conditionals, no functional changes (https://github.com/ansible-collections/community.general/pull/10328).
- pagerduty - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10512).
- pagerduty_change - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10512).
- pagerduty_user - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10512).
- pam_limits - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10512).
- parted - using safer mechanism to run external command (https://github.com/ansible-collections/community.general/pull/10642).
- pear - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10512).
- pear - using safer mechanism to run external command (https://github.com/ansible-collections/community.general/pull/10601).
- pingdom - remove redundant brackets in conditionals, no functional changes (https://github.com/ansible-collections/community.general/pull/10328).
- pipx module_utils - use ``PIPX_USE_EMOJI`` to disable emojis in the output of ``pipx`` 1.8.0 (https://github.com/ansible-collections/community.general/pull/10874).
- pkgng - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10512).
- pnpm - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10512).
- portage - add a ``changed_deps`` option (https://github.com/ansible-collections/community.general/pull/11023).
- portage - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10512).
- portage - using safer mechanism to run external command (https://github.com/ansible-collections/community.general/pull/10602).
- pritunl_org - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10512).
- pritunl_org_info - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10512).
- pritunl_user - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10512).
- pritunl_user_info - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10512).
- pubnub_blocks - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10512).
- pushbullet - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10512).
- pushover - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10512).
- python_runner module utils - remove redundant brackets in conditionals, no functional changes (https://github.com/ansible-collections/community.general/pull/10328).
- random_string lookup plugin - allow to specify seed while generating random string (https://github.com/ansible-collections/community.general/issues/5362, https://github.com/ansible-collections/community.general/pull/10710).
- redis_data - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10512).
- redis_data_incr - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10512).
- rhevm - consolidate double and triple whitespaces (https://github.com/ansible-collections/community.general/pull/11029).
- rhevm - remove redundant brackets in conditionals, no functional changes (https://github.com/ansible-collections/community.general/pull/10328).
- riak - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10512).
- riak - using safer mechanism to run external command (https://github.com/ansible-collections/community.general/pull/10603).
- rocketchat - remove redundant brackets in conditionals, no functional changes (https://github.com/ansible-collections/community.general/pull/10328).
- rocketchat - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10512).
- rollbar_deployment - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10512).
- say - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10512).
- scaleway modules - add a ``scaleway`` group to use ``module_defaults`` (https://github.com/ansible-collections/community.general/pull/10647).
- scaleway_* modules, scaleway inventory plugin - update available zones and API URLs (https://github.com/ansible-collections/community.general/issues/10383, https://github.com/ansible-collections/community.general/pull/10424).
- scaleway_container - add a ``cpu_limit`` argument (https://github.com/ansible-collections/community.general/pull/10646).
- scaleway_database_backup - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10512).
- sendgrid - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10512).
- sensu_silence - remove redundant brackets in conditionals, no functional changes (https://github.com/ansible-collections/community.general/pull/10328).
- sensu_silence - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10512).
- sensu_subscription - normalize quotes in the module output (https://github.com/ansible-collections/community.general/pull/10483).
- sl_vm - remove redundant brackets in conditionals, no functional changes (https://github.com/ansible-collections/community.general/pull/10328).
- slack - consolidate double and triple whitespaces (https://github.com/ansible-collections/community.general/pull/11029).
- solaris_zone - using safer mechanism to run external command (https://github.com/ansible-collections/community.general/pull/10604).
- sorcery - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10512).
- ssh_config - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10512).
- statusio_maintenance - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10512).
- svr4pkg - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10512).
- swdepot - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10512).
- swupd - using safer mechanism to run external command (https://github.com/ansible-collections/community.general/pull/10605).
- syslogger - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10512).
- sysrc - adjustments to the code (https://github.com/ansible-collections/community.general/pull/10417).
- sysrc - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10512).
- systemd_creds_decrypt - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10512).
- systemd_creds_encrypt - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10512).
- taiga_issue - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10513).
- tasks_only callback plugin - add ``result_format`` and ``pretty_results`` options similarly to the default callback (https://github.com/ansible-collections/community.general/pull/10422).
- terraform - minor refactor to improve readability (https://github.com/ansible-collections/community.general/pull/10711).
- timezone - using safer mechanism to run external command (https://github.com/ansible-collections/community.general/pull/10612).
- tss lookup plugin - fixed ``AccessTokenAuthorizer`` initialization to include ``base_url`` parameter for proper token authentication (https://github.com/ansible-collections/community.general/pull/11031).
- twilio - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10513).
- ufw - minor refactor to simplify string formatting (https://github.com/ansible-collections/community.general/pull/10727).
- urpmi - remove redundant brackets in conditionals, no functional changes (https://github.com/ansible-collections/community.general/pull/10328).
- urpmi - using safer mechanism to run external command (https://github.com/ansible-collections/community.general/pull/10606).
- utm_aaa_group - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10513).
- utm_ca_host_key_cert - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10513).
- utm_dns_host - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10513).
- utm_network_interface_address - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10513).
- utm_proxy_auth_profile - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10513).
- utm_proxy_exception - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10513).
- utm_proxy_frontend - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10513).
- utm_proxy_location - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10513).
- vertica_configuration - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10513).
- vertica_info - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10513).
- vertica_role - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10513).
- xattr - remove redundant brackets in conditionals, no functional changes (https://github.com/ansible-collections/community.general/pull/10328).
- xbps - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10513).
- xbps - using safer mechanism to run external command (https://github.com/ansible-collections/community.general/pull/10608).
- xenserver module utils - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10769).
- xenserver_facts - minor refactor to simplify string formatting (https://github.com/ansible-collections/community.general/pull/10727).
- xfconf - minor adjustments the the code (https://github.com/ansible-collections/community.general/pull/10311).
- xfs_quota - using safer mechanism to run external command (https://github.com/ansible-collections/community.general/pull/10609).
- xml - remove redundant brackets in conditionals, no functional changes (https://github.com/ansible-collections/community.general/pull/10328).
- yarn - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10513).
- zfs_facts - minor refactor to simplify string formatting (https://github.com/ansible-collections/community.general/pull/10727).
- zfs_facts - use Ansible construct to check result of external command (https://github.com/ansible-collections/community.general/pull/11054).
- zypper - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10513).
- zypper - support the ``--gpg-auto-import-keys`` option in zypper (https://github.com/ansible-collections/community.general/issues/10660, https://github.com/ansible-collections/community.general/pull/10661).
- zypper_repository - remove redundant constructs from argument specs (https://github.com/ansible-collections/community.general/pull/10513).

community.hashi_vault
~~~~~~~~~~~~~~~~~~~~~

- community.hashi_vault collection - add support for ``gcp`` auth method (https://github.com/ansible-collections/community.hashi_vault/pull/442).

community.hrobot
~~~~~~~~~~~~~~~~

- storagebox_subaccount - filter by username when looking for existing accounts by username (https://github.com/ansible-collections/community.hrobot/pull/182).
- storagebox_subaccount - use the new ``change_home_directory`` action to update a subaccount's home directory, instead of using the now deprecated way using the ``update_access_settings`` action (https://github.com/ansible-collections/community.hrobot/pull/181).

community.mysql
~~~~~~~~~~~~~~~

- `mysql_query` - add new `session_vars` argument, similar to ansible-collections/community.mysql#489.

community.proxmox
~~~~~~~~~~~~~~~~~

- proxmox - Add delete parameter to delete settings (https://github.com/ansible-collections/community.proxmox/pull/195).
- proxmox_cluster -  Add master_api_password for authentication against master node (https://github.com/ansible-collections/community.proxmox/pull/140).
- proxmox_cluster - added link0 and link1 to join command (https://github.com/ansible-collections/community.proxmox/issues/168, https://github.com/ansible-collections/community.proxmox/pull/172).
- proxmox_kvm - update description of machine parameter in proxmox_kvm.py (https://github.com/ansible-collections/community.proxmox/pull/186)
- proxmox_storage - added `dir` and `zfspool` storage types (https://github.com/ansible-collections/community.proxmox/pull/184)
- proxmox_tasks_info - add source option to specify tasks to consider (https://github.com/ansible-collections/community.proxmox/pull/179)
- proxmox_template -  Add 'import' to allowed content types of proxmox_template, so disk images and can be used as disk images on VM creation (https://github.com/ansible-collections/community.proxmox/pull/162).

community.proxysql
~~~~~~~~~~~~~~~~~~

- proxysql_mysql_users - Creating users with the ``caching_sha2_password`` plugin (https://github.com/ansible-collections/community.proxysql/pull/173).

community.routeros
~~~~~~~~~~~~~~~~~~

- api_find_and_modify, api_modify - instead of comparing supplied values as-is to values retrieved from the API and converted to some types (int, bool) by librouteros, instead compare values by converting them to strings first, using similar conversion rules that librouteros uses (https://github.com/ansible-collections/community.routeros/issues/389, https://github.com/ansible-collections/community.routeros/issues/370, https://github.com/ansible-collections/community.routeros/issues/325, https://github.com/ansible-collections/community.routeros/issues/169, https://github.com/ansible-collections/community.routeros/pull/397).
- api_modify - add ``vrf`` for ``snmp`` with a default of ``main`` for RouterOS 7.3 and newer (https://github.com/ansible-collections/community.routeros/pull/411).
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

community.vmware
~~~~~~~~~~~~~~~~

- vcenter_license - Add support for VCF license keys. (https://github.com/ansible-collections/community.vmware/pull/2451)
- vmware_dvs_portgroup - add ``portgroup_description`` parameter (https://github.com/ansible-collections/community.vmware/issues/2487).
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
- iap - enable use of Identity Aware Proxy ssh connections to compute instances (https://github.com/ansible-collections/google.cloud/pull/709).

hetzner.hcloud
~~~~~~~~~~~~~~

- server_type_info - Return new Server Type ``category`` property.
- server_type_info - Return new Server Type ``locations`` property.
- zone - New module to manage DNS Zones in Hetzner Cloud.
- zone_info - New module to fetch DNS Zones details.
- zone_rrset - New module to manage DNS Zone RRSets in the Hetzner Cloud.
- zone_rrset_info - New module to fetch DNS RRSets details.

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
- Added a new "hv_vsp_one_snapshot" module to create, modify and delete snapshots on VSP E series and VSP One B2X storages.
- Added a new "hv_vsp_one_snapshot_facts" module to retrieve snapshot information from VSP E series and VSP One B2X storages.
- Added a new "hv_vsp_one_snapshot_group" module to manage snapshot group operations on VSP E series and VSP One B2X storages.
- Added a new "hv_vsp_one_snapshot_group_facts" module to retrieve snapshot group information from VSP E series and VSP One B2X storages.
- Added a new `"hv_sds_block_capacity_management_settings_facts"` module to retrieve capacity management settings from SDS block cluster.
- Added a new `"hv_sds_block_drive"` module to turn ON and Off the drive locator LED, remove a drive from SDS block cluster.
- Added a new `"hv_sds_block_storage_controller"` module to edit storage controller settings on SDS block cluster.
- Added a new `"hv_sds_block_storage_node_bmc_connection_facts"` module to retrieve BMC connection details from SDS block cluster.
- Added a new `"hv_sds_block_storage_pool_estimated_capacity_facts"` module to retrieve storage pool estimated capacity from SDS block cluster on AWS.
- Added a new `"hv_vsp_one_volume"` module to enable creation, modification, and deletion of volumes, as well as attaching and detaching to servers on VSP E series and VSP One B2X storages.
- Added a new `"hv_vsp_one_volume_facts"` module to retrieve volumes information from servers on VSP E series and VSP One B2X storages.
- Added support for SDS block cluster on Microsoft Azure.
- Added support for latest software version 1.18.1 for SDS block on AWS, GCP and Bare metal.
- Added support for listing storage node primary role status in the output to hv_sds_block_storage_node_facts module.
- Added support to "Add storage node to the SDS cluster on AWS cloud" to hv_sds_block_cluster module.
- Added support to "Allow CHAP users to access the compute port" to hv_sds_block_compute_port_authentication module
- Added support to "Attach multiple volumes to multiple servers in one operation" to hv_vsp_one_volume module.
- Added support to "Cancel compute port access permission for CHAP users" to hv_sds_block_compute_port_authentication module
- Added support to "Create a VPS" to hv_sds_block_vps module.
- Added support to "Create a compute node in a VPS by VPS ID" to hv_sds_block_compute_node module.
- Added support to "Create a compute node in a VPS by VPS name" to hv_sds_block_compute_node module.
- Added support to "Create a volume in a VPS by VPS ID" to hv_sds_block_volume module.
- Added support to "Create a volume in a VPS by VPS name" to hv_sds_block_volume module.
- Added support to "Create the cluster configuration file for replace_storage_node export file type for AWS" to hv_sds_block_cluster module.
- Added support to "Create the cluster configuration file for replace_storage_node export file type for GCP" to hv_sds_block_cluster module.
- Added support to "Delete a VPS by ID" to hv_sds_block_vps module.
- Added support to "Delete a VPS by name" to hv_sds_block_vps module.
- Added support to "Delete compute node by name in a VPS by VPS ID" to hv_sds_block_compute_node module.
- Added support to "Delete compute node by name in a VPS by VPS name" to hv_sds_block_compute_node module.
- Added support to "Delete volume by name in a VPS by VPS ID" to hv_sds_block_volume module.
- Added support to "Delete volume by name in a VPS by VPS name" to hv_sds_block_volume module.
- Added support to "Edit storage pool settings" to hv_sds_block_storage_pool module.
- Added support to "Edit the capacity balancing settings" to hv_sds_block_cluster module.
- Added support to "Get Drive by ID" to hv_sds_block_drives_facts module
- Added support to "Get Protection Domain Information by ID" to hv_sds_block_protection_domain_facts module
- Added support to "Get Snapshots using master volume name in a VPS" to hv_sds_block_snapshot_facts module.
- Added support to "Get compute nodes for a VPS by VPS ID" to hv_sds_block_compute_node_facts module.
- Added support to "Get compute nodes for a VPS by VPS name" to hv_sds_block_compute_node_facts module.
- Added support to "Get volumes for a VPS by VPS ID" to hv_sds_block_volume_facts module.
- Added support to "Get volumes for a VPS by VPS name" to hv_sds_block_volume_facts module.
- Added support to "Import system requirements file for performing replace storage node on Bare metal" to hv_sds_block_cluster module.
- Added support to "Replace storage node in the cluster by storage node ID on AWS" to hv_sds_block_cluster module.
- Added support to "Replace storage node in the cluster by storage node ID on Azure" to hv_sds_block_cluster module.
- Added support to "Replace storage node in the cluster by storage node ID on Bare Metal" to hv_sds_block_cluster module.
- Added support to "Replace storage node in the cluster by storage node ID on GCP" to hv_sds_block_cluster module.
- Added support to "Stop removing storage nodes" to hv_sds_block_cluster module.
- Added support to "Update settings of a VPS" to hv_sds_block_vps module.
- Added support to take ldev input in HEX value in all hitachivantara.vspone_block.vsp modules.
- Added support with new parameters "start_ldev", "end_ldev", "external_parity_groups" to hv_resource_group module.
- Updated input parameter name from "saving_setting" to "capacity_saving" in hv_vsp_one_volume module.

ibm.storage_virtualize
~~~~~~~~~~~~~~~~~~~~~~

- ibm_sv_manage_flashsystem_grid - Added support for new FlashSystem grid APIs
- ibm_sv_manage_storage_partition - Added support for management portset and renaming partition
- ibm_sv_manage_truststore_for_replication - Added support for new FlashSystem grid APIs
- ibm_svc_hostcluster - Added support for partition and for managing host mappings during hostcluster deletion
- ibm_svc_info - Added support for new FlashSystem grid APIs
- ibm_svc_manage_ip - Changes for management portset
- ibm_svc_manage_ip - Changes for updating VLAN, gateway and IP address
- ibm_svc_manage_portset - Added support for management portset
- ibm_svc_manage_volume - Added support for HA volumes volume expansion, volumegroup, volume rename and grainsize
- ibm_svc_utils - Improved error message for unreachable systems

kubernetes.core
~~~~~~~~~~~~~~~

- Add support of skip-schema-validation in ``helm`` module (https://github.com/ansible-collections/kubernetes.core/pull/995)
- kustomize - Add support of local environ (https://github.com/ansible-collections/kubernetes.core/pull/786).

netapp.ontap
~~~~~~~~~~~~

- Modified ZAPI deprecation messages and warnings.
- na_ontap_aggregate - AWS Lambda support added to the module.
- na_ontap_autosupport - Replaced private cli with REST API.
- na_ontap_cg_snapshot - new option `consistency_type` added in REST.
- na_ontap_job_schedule - new option `interval` added in REST.
- na_ontap_job_schedule - new option `vserver` added in REST.
- na_ontap_lun - new option `provisioning_options` added in REST, requires ONTAP 9.16.1 or later.
- na_ontap_net_port - Added REST support for `flowcontrol_admin` and `ipspace`.
- na_ontap_nfs - added REST support for the option `nfsv3_fsid_change` (requires ONTAP 9.11.0 or later), and for `nfsv4_fsid_change`, `nfsv40_referrals`, and `nfsv41_referrals` (requires ONTAP 9.13.1 or later).
- na_ontap_nfs - new protocol options added in REST.
- na_ontap_quotas - updated docs for 'quota_target' and 'type'.
- na_ontap_rest_info - support added for `application/consistency-groups/metrics`.
- na_ontap_rest_info - support added for `application/consistency-groups/snapshots`.
- na_ontap_security_ssh - new option `host_key_algorithms`, requires ONTAP 9.16.1 or later.
- na_ontap_snapshot - new option `snaplock_expiry_time` added in REST, requires ONTAP 9.15.1 or later.
- na_ontap_software_update - Updated documentation for `validate_after_download` parameter.
- na_ontap_svm - new option `storage_limit_threshold_alert` added in REST, requires ONTAP 9.13.1 or later.
- na_ontap_svm - new options `auto_enable_analytics`, `auto_enable_activity_tracking` added in REST, requires ONTAP 9.12.1 or later.
- na_ontap_user - updated docs for 'vserver' option.
- na_ontap_volume - AWS Lambda support added to the module.
- na_ontap_volume_autosize - updated docs for `increment_size` & `reset`.
- na_ontap_volume_clone - new options `time_out`, `wait_for_completion` added in REST.
- updated `README` template; added 'Support' section.

purestorage.flasharray
~~~~~~~~~~~~~~~~~~~~~~

- plugins/module_utils/purefa.py - Removed ``get_system`` function as REST v1 no longer supported by Collection
- purefa_arrayname - Added Fusion support
- purefa_audits - Added Fusion support
- purefa_banner - Added Fusion support
- purefa_connect - Added Fusion support
- purefa_connect - Allow asynchronous FC-based replication
- purefa_console - Added Fusion support
- purefa_default_protection - Added Fusion support.
- purefa_directory - Added Fusion support
- purefa_dirsnap - Added Fusion support
- purefa_ds - Added Fusion support
- purefa_dsrole - Added Fusion support
- purefa_dsrole_old - Upgraded to REST v2
- purefa_endpoint - Added Fusion support
- purefa_eradication - Added Fusion support
- purefa_export - Added Fusion support
- purefa_fs - Added Fusion support
- purefa_info - Added new subsets ``workloads`` and ``presets``
- purefa_info - Converted to use REST 2
- purefa_maintenance - Timeout window updated
- purefa_messages - Added Fusion support
- purefa_network - Converted to REST v2
- purefa_ntp - Added Fusion support.
- purefa_offload - Added Fusion support
- purefa_pod - Added support for SafeMode protection group configuration
- purefa_policy - Added Fusion support
- purefa_policy - Upgraded to REST v2
- purefa_syslog - Added Fusion support.
- purefa_syslog_settings - Added Fusion support
- purefa_timeout - Added Fusion support
- purefa_user - All AD users to have SSH keys and/or API tokens assigned, even if they have never accessed the FlashArray before. AD users must have ``ad_user`` set as ``true``.
- purefa_volume_tags - Add `tag` parameter to specify tag to be deleted by key name
- purefa_volume_tags - Upgraded to REST v2 and added Fusion support

purestorage.flashblade
~~~~~~~~~~~~~~~~~~~~~~

- module_utils/purefb - Remove `get_blade()` function as not required for REST v2
- purefb_ad - Revert removal of ``service`` parameter (breaking change). Added more logic to use of ``service`` parameter and recommend use of ``service_principals`` with service incorporated.
- purefb_ad - ``service`` parameter removed to comply with underlying API structure. ``service`` should be included in the ``service_principals`` strings as shown in the documentation.
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
- purefb_saml - Added ``entity_id`` parameter
- purefb_snamp_agent - Upgraded to REST v2
- purefb_snap - Add support to delete/eradicate remote snapshots, including the latest replica
- purefb_snap - Fusion support added
- purefb_snap - Upgraded to REST v2
- purefb_snmp_mgr - Add new ``state`` of ``test`` to check SNMP manager configuration
- purefb_snmp_mgr - Upgraded to REST v2
- purefb_subnet - Upgraded to REST v2
- purefb_syslog - Converted to REST v2
- purefb_target - Upgraded to REST v2
- purefb_user - All AD users to have SSH keys and/or API tokens assigned, even if they have never accessed the FlashArray before. AD users must have ``ad_user`` set as ``true``.
- purefb_userpolicy - Fusion support added
- purefb_userquota - Added Fusion support
- purefb_userquota - Upgraded to REST v2
- purefb_virtualhost - Fusion support added

theforeman.foreman
~~~~~~~~~~~~~~~~~~

- content_upload - fall-back to rpm binary when library can't be imported
- registration_command - clarify example to show where the generated command needs to be executed

vmware.vmware
~~~~~~~~~~~~~

- Add module for importing iso images to content library.
- Remove six imports from _facts.py and _vsphere_tasks.py due to new sanity rules. Python 2 (already not supported) will fail to execute these files.
- tag_associations - Add module to manage tag associations with objects
- tag_categories - Add module to manage tag categories
- tags - Add module to manage tags
- vms - Add option to inventory plugin to gather cluster and ESXi host name for VMs. (Fixes https://github.com/ansible-collections/vmware.vmware/issues/215)

Breaking Changes / Porting Guide
--------------------------------

Ansible-core
~~~~~~~~~~~~

- powershell - Removed code that tried to remote quotes from paths when performing Windows operations like copying and fetching file. This should not affect normal playbooks unless a value is quoted too many times.

community.docker
~~~~~~~~~~~~~~~~

- All doc fragments, module utils, and plugin utils are from now on private. They can change at any time, and have breaking changes even in bugfix releases (https://github.com/ansible-collections/community.docker/pull/1144).

community.general
~~~~~~~~~~~~~~~~~

- mh.base module utils - ``debug`` will now always be delegated to the underlying ``AnsibleModule`` object (https://github.com/ansible-collections/community.general/pull/10883).
- oneview module utils - remove import of standard library ``os`` (https://github.com/ansible-collections/community.general/pull/10644).
- slack - the default of ``prepend_hash`` changed from ``auto`` to ``never`` (https://github.com/ansible-collections/community.general/pull/10883).

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

hetzner.hcloud
~~~~~~~~~~~~~~

- Drop support for Python 3.9
- Drop support for ansible-core 2.17

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

- catapult - module is deprecated and will be removed in community.general 13.0.0 (https://github.com/ansible-collections/community.general/issues/10318, https://github.com/ansible-collections/community.general/pull/10329).
- cpanm - deprecate ``mode=compatibility``, ``mode=new`` should be used instead (https://github.com/ansible-collections/community.general/pull/10434).
- dimensiondata doc_fragments plugin - fragments is deprecated and will be removed in community.general 13.0.0 (https://github.com/ansible-collections/community.general/pull/10986).
- dimensiondata module_utils plugin - utils is deprecated and will be removed in community.general 13.0.0 (https://github.com/ansible-collections/community.general/pull/10986).
- dimensiondata_network - module is deprecated and will be removed in community.general 13.0.0 (https://github.com/ansible-collections/community.general/pull/10986).
- dimensiondata_vlan - module is deprecated and will be removed in community.general 13.0.0 (https://github.com/ansible-collections/community.general/pull/10986).
- dimensiondata_wait doc_fragments plugin - fragments is deprecated and will be removed in community.general 13.0.0 (https://github.com/ansible-collections/community.general/pull/10986).
- github_repo - deprecate ``force_defaults=true`` (https://github.com/ansible-collections/community.general/pull/10435).
- hiera lookup plugin - retrieving data with Hiera has been deprecated a long time ago; because of that this plugin will be removed from community.general 13.0.0. If you disagree with this deprecation, please create an issue in the community.general repository (https://github.com/ansible-collections/community.general/issues/4462, https://github.com/ansible-collections/community.general/pull/10779).
- oci_utils module utils - utils is deprecated and will be removed in community.general 13.0.0 (https://github.com/ansible-collections/community.general/issues/10318, https://github.com/ansible-collections/community.general/pull/10652).
- oci_vcn - module is deprecated and will be removed in community.general 13.0.0 (https://github.com/ansible-collections/community.general/issues/10318, https://github.com/ansible-collections/community.general/pull/10652).
- oneandone module utils - DNS fails to resolve the API endpoint used by the module. The module is deprecated and will be removed in community.general 13.0.0 (https://github.com/ansible-collections/community.general/pull/10994).
- oneandone_firewall_policy - DNS fails to resolve the API endpoint used by the module. The module is deprecated and will be removed in community.general 13.0.0 (https://github.com/ansible-collections/community.general/pull/10994).
- oneandone_load_balancer - DNS fails to resolve the API endpoint used by the module. The module is deprecated and will be removed in community.general 13.0.0 (https://github.com/ansible-collections/community.general/pull/10994).
- oneandone_monitoring_policy - DNS fails to resolve the API endpoint used by the module. The module is deprecated and will be removed in community.general 13.0.0 (https://github.com/ansible-collections/community.general/pull/10994).
- oneandone_private_network - DNS fails to resolve the API endpoint used by the module. The module is deprecated and will be removed in community.general 13.0.0 (https://github.com/ansible-collections/community.general/pull/10994).
- oneandone_public_ip - DNS fails to resolve the API endpoint used by the module. The module is deprecated and will be removed in community.general 13.0.0 (https://github.com/ansible-collections/community.general/pull/10994).
- oneandone_server - DNS fails to resolve the API endpoint used by the module. The module is deprecated and will be removed in community.general 13.0.0 (https://github.com/ansible-collections/community.general/pull/10994).
- oracle* doc fragments - fragments are deprecated and will be removed in community.general 13.0.0 (https://github.com/ansible-collections/community.general/issues/10318, https://github.com/ansible-collections/community.general/pull/10652).
- pacemaker_cluster - the state ``cleanup`` will be removed from community.general 14.0.0 (https://github.com/ansible-collections/community.general/pull/10741).
- rocketchat - the default value for ``is_pre740``, currently ``true``, is deprecated and will change to ``false`` in community.general 13.0.0 (https://github.com/ansible-collections/community.general/pull/10490).
- typetalk - module is deprecated and will be removed in community.general 13.0.0 (https://github.com/ansible-collections/community.general/pull/9499).

community.hrobot
~~~~~~~~~~~~~~~~

- storagebox\* modules - membership in the ``community.hrobot.robot`` action group (module defaults group) is deprecated; the modules will be removed from the group in community.hrobot 3.0.0. Use ``community.hrobot.api`` instead (https://github.com/ansible-collections/community.hrobot/pull/178).
- storagebox\* modules - the ``hetzner_token`` option for these modules will be required from community.hrobot 3.0.0 on (https://github.com/ansible-collections/community.hrobot/pull/178).
- storagebox\* modules - the ``hetzner_user`` and ``hetzner_pass`` options for these modules are deprecated; support will be removed in community.hrobot 3.0.0. Use ``hetzner_token`` instead (https://github.com/ansible-collections/community.hrobot/pull/178).
- storagebox_info - the ``storageboxes[].login``, ``storageboxes[].disk_quota``, ``storageboxes[].disk_usage``, ``storageboxes[].disk_usage_data``, ``storageboxes[].disk_usage_snapshot``, ``storageboxes[].webdav``, ``storageboxes[].samba``, ``storageboxes[].ssh``, ``storageboxes[].external_reachability``, and ``storageboxes[].zfs`` return values are deprecated and will be removed from community.routeros. Check out the documentation to find out their new names according to the new API (https://github.com/ansible-collections/community.hrobot/pull/178).
- storagebox_snapshot_info - the ``snapshots[].timestamp``, ``snapshots[].size``, ``snapshots[].filesystem_size``, ``snapshots[].automatic``, and ``snapshots[].comment`` return values are deprecated and will be removed from community.routeros. Check out the documentation to find out their new names according to the new API (https://github.com/ansible-collections/community.hrobot/pull/178).
- storagebox_snapshot_plan - the ``plans[].month`` return value is deprecated, since it only returns ``null`` with the new API and cannot be set to any other value (https://github.com/ansible-collections/community.hrobot/pull/178).
- storagebox_snapshot_plan_info - the ``plans[].month`` return value is deprecated, since it only returns ``null`` with the new API and cannot be set to any other value (https://github.com/ansible-collections/community.hrobot/pull/178).
- storagebox_subaccount - ``password_mode=set-to-random`` is deprecated and will be removed from community.hrobot 3.0.0. Hetzner's new API does not support this anyway, it can only be used with the legacy API (https://github.com/ansible-collections/community.hrobot/pull/183).
- storagebox_subaccount - the ``subaccount.homedirectory``, ``subaccount.samba``, ``subaccount.ssh``, ``subaccount.external_reachability``, ``subaccount.webdav``, ``subaccount.readonly``, ``subaccount.createtime``, and ``subaccount.comment`` return values are deprecated and will be removed from community.routeros. Check out the documentation to find out their new names according to the new API (https://github.com/ansible-collections/community.hrobot/pull/178).
- storagebox_subaccount_info - the ``subaccounts[].accountid``, ``subaccounts[].homedirectory``, ``subaccounts[].samba``, ``subaccounts[].ssh``, ``subaccounts[].external_reachability``, ``subaccounts[].webdav``, ``subaccounts[].readonly``, ``subaccounts[].createtime``, and ``subaccounts[].comment`` return values are deprecated and will be removed from community.routeros. Check out the documentation to find out their new names according to the new API (https://github.com/ansible-collections/community.hrobot/pull/178).

community.vmware
~~~~~~~~~~~~~~~~

- vmware_guest_snapshot - the module has been deprecated and will be removed in community.vmware 8.0.0 (https://github.com/ansible-collections/community.vmware/pull/2467).

community.zabbix
~~~~~~~~~~~~~~~~

- zabbix_maintenance module - Depreicated `minutes` argument for `time_periods`

dellemc.powerflex
~~~~~~~~~~~~~~~~~

- The device, info, protection_domain, snapshot, storagepool and volume modules are supported only on PowerFlex Gen1. They are replaced by v2 modules on PowerFlex Gen2.
- The fault_set, replication_consistency_group, replication_pair, resource_group and sds modules are not supported on PowerFlex Gen2.

hetzner.hcloud
~~~~~~~~~~~~~~

- server_type_info - Deprecate Server Type ``deprecation`` property.

purestorage.flasharray
~~~~~~~~~~~~~~~~~~~~~~

- purefa_volume_tags - Deprecated due to removal of REST 1.x support. Will be removed in Collection 2.0.0

Removed Features (previously deprecated)
----------------------------------------

- The deprecated ``community.digitalocean`` collection has been removed (`https://forum.ansible.com/t/44602 <https://forum.ansible.com/t/44602>`__).
- The deprecated ``ibm.qradar`` collection has been removed (`https://forum.ansible.com/t/44259 <https://forum.ansible.com/t/44259>`__).

Ansible-core
~~~~~~~~~~~~

- Removed the option to set the ``DEFAULT_TRANSPORT`` configuration to ``smart`` that selects the default transport as either ``ssh`` or ``paramiko`` based on the underlying platform configuraton.
- ``vault``/``unvault`` filters - remove the deprecated ``vaultid`` parameter.
- ansible-doc - role entrypoint attributes are no longer shown
- ansible-galaxy - remove support for resolvelib >= 0.5.3, < 0.8.0.
- ansible-galaxy - removed the v2 Galaxy server API. Galaxy servers hosting collections must support v3.
- dnf/dnf5 - remove deprecated ``install_repoquery`` option.
- encrypt - remove deprecated passlib_or_crypt API.
- paramiko - Removed the ``PARAMIKO_HOST_KEY_AUTO_ADD`` and ``PARAMIKO_LOOK_FOR_KEYS`` configuration keys, which were previously deprecated.
- py3compat - remove deprecated ``py3compat.environ`` call.
- vars plugins - removed the deprecated ``get_host_vars`` or ``get_group_vars`` fallback for vars plugins that do not inherit from ``BaseVarsPlugin`` and define a ``get_vars`` method.
- yum_repository - remove deprecated ``keepcache`` option.

community.docker
~~~~~~~~~~~~~~~~

- Remove support for Docker SDK for Python version 1.x.y, also known as ``docker-py``. Modules and plugins that use Docker SDK for Python require version 2.0.0+ (https://github.com/ansible-collections/community.docker/pull/1171).
- The collection no longer supports Python 3.6 and before. Note that this coincides with the Python requirements of ansible-core 2.17+ (https://github.com/ansible-collections/community.docker/pull/1123).
- The collection no longer supports ansible-core 2.15 and 2.16. You need ansible-core 2.17.0 or newer to use community.docker 5.x.y (https://github.com/ansible-collections/community.docker/pull/1123).

community.general
~~~~~~~~~~~~~~~~~

- Ansible-core 2.16 is no longer supported. This also means that the collection now requires Python 3.7+ (https://github.com/ansible-collections/community.general/pull/10884).
- bearychat - the module has been removed as the chat service is no longer available (https://github.com/ansible-collections/community.general/pull/10883).
- cmd_runner module utils - the parameter ``ignore_value_none`` to ``CmdRunner.__call__()`` has been removed (https://github.com/ansible-collections/community.general/pull/10883).
- cmd_runner_fmt module utils - the parameter ``ctx_ignore_none`` to argument formatters has been removed (https://github.com/ansible-collections/community.general/pull/10883).
- facter - the module has been replaced by ``community.general.facter_facts`` (https://github.com/ansible-collections/community.general/pull/10883).
- mh.deco module utils - the parameters ``on_success`` and ``on_failure`` of ``cause()`` have been removed; use ``when="success"`` and ``when="failure"`` instead (https://github.com/ansible-collections/community.general/pull/10883).
- opkg - the value ``""`` for the option ``force`` is no longer allowed. Omit ``force`` instead (https://github.com/ansible-collections/community.general/pull/10883).
- pacemaker_cluster - the option ``state`` is now required (https://github.com/ansible-collections/community.general/pull/10883).
- pure module utils - the modules using this module utils have been removed from community.general 3.0.0 (https://github.com/ansible-collections/community.general/pull/10883).
- purestorage doc fragment - the modules using this doc fragment have been removed from community.general 3.0.0 (https://github.com/ansible-collections/community.general/pull/10883).
- yaml callback plugin - the deprecated plugin has been removed. Use the default callback with ``result_format=yaml`` instead (https://github.com/ansible-collections/community.general/pull/10883).

community.vmware
~~~~~~~~~~~~~~~~

- vmware_cluster - The deprecated module has been removed. Use ``vmware.vmware.cluster`` instead (https://github.com/ansible-collections/community.vmware/pull/2455).
- vmware_cluster_dpm - The deprecated module has been removed. Use ``vmware.vmware.cluster_dpm`` instead (https://github.com/ansible-collections/community.vmware/pull/2455).
- vmware_cluster_drs - The deprecated module has been removed. Use ``vmware.vmware.cluster_drs`` instead (https://github.com/ansible-collections/community.vmware/pull/2455).
- vmware_cluster_drs_recommendations - The deprecated module has been removed. Use ``vmware.vmware.cluster_drs_recommendations`` instead (https://github.com/ansible-collections/community.vmware/pull/2455).
- vmware_cluster_vcls - The deprecated module has been removed. Use ``vmware.vmware.cluster_vcls`` instead (https://github.com/ansible-collections/community.vmware/pull/2455).

Security Fixes
--------------

community.general
~~~~~~~~~~~~~~~~~

- keycloak_user - the parameter ``credentials[].value`` is now marked as ``no_log=true``. Before it was logged by Ansible, unless the task was marked as ``no_log: true``. Since this parameter can be used for passwords, this resulted in credential leaking (https://github.com/ansible-collections/community.general/issues/11000, https://github.com/ansible-collections/community.general/pull/11005).

Bugfixes
--------

Ansible-core
~~~~~~~~~~~~

- Do not re-add ``tags`` on blocks from within ``import_tasks``.
- Fix issue where play tags prevented executing notified handlers (https://github.com/ansible/ansible/issues/85475)
- Fix issues with keywords being incorrectly validated on ``import_tasks`` (https://github.com/ansible/ansible/issues/85855, https://github.com/ansible/ansible/issues/85856)
- Fix traceback when trying to import non-existing file via nested ``import_tasks`` (https://github.com/ansible/ansible/issues/69882)
- SIGINT/SIGTERM Handling - Make SIGINT/SIGTERM handling more robust by splitting concerns between forks and the parent.
- The ``ansible_failed_task`` variable is now correctly exposed in a rescue section, even when a failing handler is triggered by the ``flush_handlers`` task in the corresponding ``block`` (https://github.com/ansible/ansible/issues/85682)
- Windows - ignore temporary file cleanup warning when using AnsibleModule to compile C# utils. This should reduce the number of warnings that can safely be ignored when running PowerShell modules - https://github.com/ansible/ansible/issues/85976
- Windows async - Handle running PowerShell modules with trailing data after the module result
- ``ansible-galaxy collection list`` - fail when none of the configured collection paths exist.
- ``ternary`` filter - evaluate values lazily (https://github.com/ansible/ansible/issues/85743)
- ansible-doc - prevent crash when scanning collections in paths that have more than one ``ansible_collections`` in it (https://github.com/ansible/ansible/issues/84909, https://github.com/ansible/ansible/pull/85361).
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
- config lookup now properly factors in variables and show_origin when checking entries from the global configuration.
- display - Fixed reference to undefined `_DeferredWarningContext` when issuing early warnings during startup. (https://github.com/ansible/ansible/issues/85886)
- dnf - Check if installroot is directory or not (https://github.com/ansible/ansible/issues/85680).
- failed_when - When using ``failed_when`` to suppress an error, the ``exception`` key in the result is renamed to ``failed_when_suppressed_exception``. This prevents the error from being displayed by callbacks after being suppressed. (https://github.com/ansible/ansible/issues/85505)
- fetch - also return ``file`` in the result when changed is ``True`` (https://github.com/ansible/ansible/pull/85729).
- import_tasks - fix templating parent include arguments.
- include_role - allow host specific values in all ``*_from`` arguments (https://github.com/ansible/ansible/issues/66497)
- option argument deprecations now have a proper alternative help text.
- package_facts - typecast bytes to string while returning facts (https://github.com/ansible/ansible/issues/85937).
- pip - Fix pip module output so that it returns changed when the only operation is initializing a venv.
- plugins config, get_option_and_origin now correctly displays the value and origin of the option.
- psrp - ReadTimeout exceptions now mark host as unreachable instead of fatal (https://github.com/ansible/ansible/issues/85966)
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

amazon.aws
~~~~~~~~~~

- Remove ``ansible.module_utils.six`` imports to avoid warnings (https://github.com/ansible-collections/amazon.aws/pull/2727).
- amazon.aws.autoscaling_instance - setting the state to ``terminated`` had no effect. The fix implements missing instance termination state (https://github.com/ansible-collections/amazon.aws/issues/2719).
- ec2_vpc_nacl - Fix issue when trying to update existing Network ACL rule (https://github.com/ansible-collections/amazon.aws/issues/2592).
- s3_object - Honor headers for content and content_base64 uploads by promoting supported keys (e.g. ContentType, ContentDisposition, CacheControl) to top-level S3 arguments and placing remaining keys under Metadata. This makes content uploads consistent with src uploads. (https://github.com/ansible-collections/amazon.aws)

cisco.ios
~~~~~~~~~

- Fixed an issue where configuration within an address family (ipv6) was ignored by the parser.
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
- cisco.meraki.devices_appliance_uplinks_settings - fix idempotency error.
- networks_switch_qos_rules_order: extend object lookup to include srcPortRange and dstPortRange when matching existing QoS rules to improve idempotency

community.crypto
~~~~~~~~~~~~~~~~

- Avoid deprecated functionality in ansible-core 2.20 (https://github.com/ansible-collections/community.crypto/pull/953).
- Smaller code cleanup (https://github.com/ansible-collections/community.crypto/pull/963).

community.dns
~~~~~~~~~~~~~

- Avoid using ``ansible.module_utils.six`` in more places to avoid deprecation warnings with ansible-core 2.20 (https://github.com/ansible-collections/community.dns/pull/291).
- Avoid using ``ansible.module_utils.six`` to avoid deprecation warnings with ansible-core 2.20 (https://github.com/ansible-collections/community.dns/pull/287).
- Update Public Suffix List.

community.docker
~~~~~~~~~~~~~~~~

- Avoid deprecated functionality in ansible-core 2.20 (https://github.com/ansible-collections/community.docker/pull/1117).
- Avoid remaining usages of deprecated ``ansible.module_utils.six`` (https://github.com/ansible-collections/community.docker/pull/1133).
- Avoid usage of deprecated ``ansible.module_utils.six`` in all code that does not have to support Python 2 (https://github.com/ansible-collections/community.docker/pull/1137, https://github.com/ansible-collections/community.docker/pull/1139).
- Avoid usage of deprecated ``ansible.module_utils.six`` in some of the code that still supports Python 2 (https://github.com/ansible-collections/community.docker/pull/1138).
- docker connection plugin - fix crash instead of warning if Docker version does not support ``remote_user`` (https://github.com/ansible-collections/community.docker/pull/1161).
- docker, nsenter connection plugins - fix handling of ``become`` plugin password prompt handling in case multiple events arrive at the same time (https://github.com/ansible-collections/community.docker/pull/1158).
- docker_api connection plugin - fix bug that could lead to loss of data when waiting for ``become`` plugin prompt (https://github.com/ansible-collections/community.docker/pull/1152).
- docker_compose_v2_exec - fix crash instead of reporting error if ``detach=true`` and ``stdin`` is provided (https://github.com/ansible-collections/community.docker/pull/1161).
- docker_compose_v2_run - fix crash instead of reporting error if ``detach=true`` and ``stdin`` is provided (https://github.com/ansible-collections/community.docker/pull/1161).
- docker_compose_v2_run - when ``detach=true``, ensure that the returned container ID is not a bytes string (https://github.com/ansible-collections/community.docker/pull/1183).
- docker_container_exec - fix bug that could lead to loss of stdout/stderr data (https://github.com/ansible-collections/community.docker/pull/1152).
- docker_container_exec - make ``detach=true`` work. So far this resulted in no execution being done (https://github.com/ansible-collections/community.docker/pull/1145).
- docker_image - fix 'Cannot locate specified Dockerfile' error (https://github.com/ansible-collections/community.docker/pull/1184).
- docker_plugin - fix diff mode for plugin options (https://github.com/ansible-collections/community.docker/pull/1146).

community.general
~~~~~~~~~~~~~~~~~

- Avoid deprecated functionality in ansible-core 2.20 (https://github.com/ansible-collections/community.general/pull/10687).
- Avoid usage of deprecated ``ansible.module_utils.six`` in all code that does not have to support Python 2 (https://github.com/ansible-collections/community.general/pull/10873).
- Remove all usage of ``ansible.module_utils.six`` (https://github.com/ansible-collections/community.general/pull/10888).
- _filelock module utils - improve Python code (https://github.com/ansible-collections/community.general/pull/11043).
- aerospike_migrations - improve Python code by removing unnecessary variables (https://github.com/ansible-collections/community.general/pull/11049).
- aix_lvol - improve Python code by removing unnecessary variables (https://github.com/ansible-collections/community.general/pull/11049).
- ali_instance - improve Python code (https://github.com/ansible-collections/community.general/pull/11043).
- ali_instance - improve Python code by removing unnecessary variables (https://github.com/ansible-collections/community.general/pull/11049).
- ali_instance_info - improve Python code (https://github.com/ansible-collections/community.general/pull/11043).
- apache2_module - avoid ansible-core 2.19 deprecation (https://github.com/ansible-collections/community.general/pull/10459).
- apache2_module - check the ``cgi`` module restrictions only during activation (https://github.com/ansible-collections/community.general/pull/10423).
- apk - fix check for empty/whitespace-only package names (https://github.com/ansible-collections/community.general/pull/10532).
- apk - handle empty name strings properly (https://github.com/ansible-collections/community.general/issues/10441, https://github.com/ansible-collections/community.general/pull/10442).
- apt_rpm - improve Python code (https://github.com/ansible-collections/community.general/pull/11043).
- apt_rpm - improve Python code by removing unnecessary variables (https://github.com/ansible-collections/community.general/pull/11049).
- btrfs module utils - improve Python code (https://github.com/ansible-collections/community.general/pull/11043).
- btrfs module utils - improve Python code by removing unnecessary variables (https://github.com/ansible-collections/community.general/pull/11049).
- btrfs_subvolume - improve Python code (https://github.com/ansible-collections/community.general/pull/11043).
- btrfs_subvolume - improve Python code by removing unnecessary variables (https://github.com/ansible-collections/community.general/pull/11049).
- capabilities - using invalid path (symlink/directory/...) returned unrelated and incoherent error messages (https://github.com/ansible-collections/community.general/issues/5649, https://github.com/ansible-collections/community.general/pull/10455).
- chef_databag lookup plugin - improve Python code by removing unnecessary variables (https://github.com/ansible-collections/community.general/pull/11049).
- cloudflare_dns - roll back changes to CAA record validation (https://github.com/ansible-collections/community.general/issues/10934, https://github.com/ansible-collections/community.general/pull/10956).
- cloudflare_dns - roll back changes to SRV record validation (https://github.com/ansible-collections/community.general/issues/10934, https://github.com/ansible-collections/community.general/pull/10937).
- consul - improve Python code (https://github.com/ansible-collections/community.general/pull/11043).
- consul_kv lookup plugin - improve Python code by removing unnecessary variables (https://github.com/ansible-collections/community.general/pull/11049).
- cronvar - fix crash on missing ``cron_file`` parent directories (https://github.com/ansible-collections/community.general/issues/10460, https://github.com/ansible-collections/community.general/pull/10461).
- cronvar - handle empty strings on ``value`` properly  (https://github.com/ansible-collections/community.general/issues/10439, https://github.com/ansible-collections/community.general/pull/10445).
- cronvar - improve Python code (https://github.com/ansible-collections/community.general/pull/11043).
- dependent lookup plugin - avoid deprecated ansible-core 2.19 functionality (https://github.com/ansible-collections/community.general/pull/10359).
- discord - improve Python code by removing unnecessary variables (https://github.com/ansible-collections/community.general/pull/11049).
- dnf_versionlock - improve Python code (https://github.com/ansible-collections/community.general/pull/11043).
- dnsmadeeasy - improve Python code (https://github.com/ansible-collections/community.general/pull/11043).
- doas become plugin - disable pipelining on ansible-core 2.19+. The plugin does not work with pipelining, and since ansible-core 2.19 become plugins can indicate that they do not work with pipelining (https://github.com/ansible-collections/community.general/issues/9977, https://github.com/ansible-collections/community.general/pull/10537).
- dpkg_divert - improve Python code by removing unnecessary variables (https://github.com/ansible-collections/community.general/pull/11049).
- elastic callback plugin - improve Python code by removing unnecessary variables (https://github.com/ansible-collections/community.general/pull/11049).
- filesystem - avoid false positive change detection on XFS resize due to unusable slack space (https://github.com/ansible-collections/community.general/pull/11033).
- gem - fix soundness issue when uninstalling default gems on Ubuntu  (https://github.com/ansible-collections/community.general/issues/10451, https://github.com/ansible-collections/community.general/pull/10689).
- github_app_access_token lookup plugin - fix compatibility imports for using jwt (https://github.com/ansible-collections/community.general/issues/10807, https://github.com/ansible-collections/community.general/pull/10810).
- github_deploy_key - fix bug during error handling if no body was present in the result (https://github.com/ansible-collections/community.general/issues/10853, https://github.com/ansible-collections/community.general/pull/10857).
- github_release - support multiple types of GitHub tokens; no longer failing when ``ghs_`` token type is provided (https://github.com/ansible-collections/community.general/issues/10338, https://github.com/ansible-collections/community.general/pull/10339).
- gitlab module utils - improve Python code by removing unnecessary variables (https://github.com/ansible-collections/community.general/pull/11049).
- gitlab_branch - improve Python code by removing unnecessary variables (https://github.com/ansible-collections/community.general/pull/11049).
- gitlab_group_members - improve Python code by removing unnecessary variables (https://github.com/ansible-collections/community.general/pull/11049).
- gitlab_issue - improve Python code (https://github.com/ansible-collections/community.general/pull/11043).
- gitlab_merge_request - improve Python code (https://github.com/ansible-collections/community.general/pull/11043).
- gitlab_project - improve Python code (https://github.com/ansible-collections/community.general/pull/11043).
- gitlab_project_members - improve Python code by removing unnecessary variables (https://github.com/ansible-collections/community.general/pull/11049).
- gitlab_protected_branch - improve Python code by removing unnecessary variables (https://github.com/ansible-collections/community.general/pull/11049).
- gitlab_runner - fix exception in check mode when a new runner is created (https://github.com/ansible-collections/community.general/issues/8854).
- gitlab_user - improve Python code (https://github.com/ansible-collections/community.general/pull/11043).
- haproxy - improve Python code (https://github.com/ansible-collections/community.general/pull/11043).
- homebrew - do not fail when cask or formula name has changed in homebrew repo (https://github.com/ansible-collections/community.general/issues/10804, https://github.com/ansible-collections/community.general/pull/10805).
- homebrew - improve Python code (https://github.com/ansible-collections/community.general/pull/11043).
- homebrew_services - improve Python code (https://github.com/ansible-collections/community.general/pull/11043).
- hpilo_boot - improve Python code (https://github.com/ansible-collections/community.general/pull/11043).
- htpasswd - avoid ansible-core 2.19 deprecation (https://github.com/ansible-collections/community.general/pull/10459).
- icinga2 inventory plugin - avoid using deprecated option when templating options (https://github.com/ansible-collections/community.general/pull/10271).
- incus connection plugin - fix error handling to return more useful Ansible errors to the user (https://github.com/ansible-collections/community.general/issues/10344, https://github.com/ansible-collections/community.general/pull/10349).
- infinity - improve Python code by removing unnecessary variables (https://github.com/ansible-collections/community.general/pull/11049).
- ini_file - improve Python code (https://github.com/ansible-collections/community.general/pull/11043).
- interfaces_file - improve Python code by removing unnecessary variables (https://github.com/ansible-collections/community.general/pull/11049).
- ipa_group - improve Python code by removing unnecessary variables (https://github.com/ansible-collections/community.general/pull/11049).
- ipa_otptoken - improve Python code (https://github.com/ansible-collections/community.general/pull/11043).
- ipa_vault - improve Python code by removing unnecessary variables (https://github.com/ansible-collections/community.general/pull/11049).
- ipmi_boot - improve Python code by removing unnecessary variables (https://github.com/ansible-collections/community.general/pull/11049).
- irc - pass hostname to ``wrap_socket()`` if ``use_tls=true`` and ``validate_certs=true`` (https://github.com/ansible-collections/community.general/issues/10472, https://github.com/ansible-collections/community.general/pull/10491).
- jenkins_build - improve Python code by removing unnecessary variables (https://github.com/ansible-collections/community.general/pull/11049).
- jenkins_build_info - improve Python code by removing unnecessary variables (https://github.com/ansible-collections/community.general/pull/11049).
- jenkins_credential - improve Python code (https://github.com/ansible-collections/community.general/pull/11043).
- jenkins_plugin - improve Python code (https://github.com/ansible-collections/community.general/pull/11043).
- jenkins_plugin - improve Python code by removing unnecessary variables (https://github.com/ansible-collections/community.general/pull/11049).
- jenkins_plugin - install latest compatible version instead of latest (https://github.com/ansible-collections/community.general/issues/854, https://github.com/ansible-collections/community.general/pull/10346).
- jenkins_plugin - separate Jenkins and external URL credentials (https://github.com/ansible-collections/community.general/issues/4419, https://github.com/ansible-collections/community.general/pull/10346).
- json_patch filter plugin - improve Python code (https://github.com/ansible-collections/community.general/pull/11043).
- json_query filter plugin - make compatible with lazy evaluation list and dictionary types of ansible-core 2.19 (https://github.com/ansible-collections/community.general/pull/10539).
- kdeconfig - ``kwriteconfig`` executable could not be discovered automatically on systems with only ``kwriteconfig6`` installed. ``kwriteconfig6`` can now be discovered by Ansible (https://github.com/ansible-collections/community.general/issues/10746, https://github.com/ansible-collections/community.general/pull/10751).
- kea_command - improve Python code (https://github.com/ansible-collections/community.general/pull/11043).
- keycloak_authz_permission - improve Python code (https://github.com/ansible-collections/community.general/pull/11043).
- keycloak_clientscope_type - improve Python code (https://github.com/ansible-collections/community.general/pull/11043).
- keycloak_clientsecret, keycloak_clientsecret_info - make ``client_auth`` work (https://github.com/ansible-collections/community.general/issues/10932, https://github.com/ansible-collections/community.general/pull/10933).
- keycloak_component - improve Python code by removing unnecessary variables (https://github.com/ansible-collections/community.general/pull/11049).
- keycloak_group - fixes an issue where module ignores realm when searching subgroups by name (https://github.com/ansible-collections/community.general/pull/10840).
- keycloak_realm - support setting ``adminPermissionsEnabled`` for a realm (https://github.com/ansible-collections/community.general/issues/10962).
- keycloak_realm_key - improve Python code by removing unnecessary variables (https://github.com/ansible-collections/community.general/pull/11049).
- keycloak_role - fixes an issue where the module incorrectly returns ``changed=true`` when using the alias ``clientId`` in composite roles (https://github.com/ansible-collections/community.general/pull/10829).
- keycloak_user_execute_actions_email - improve Python code (https://github.com/ansible-collections/community.general/pull/11043).
- keycloak_user_federation - improve Python code (https://github.com/ansible-collections/community.general/pull/11043).
- keycloak_userprofile - improve Python code by removing unnecessary variables (https://github.com/ansible-collections/community.general/pull/11049).
- launchd - improve Python code by removing unnecessary variables (https://github.com/ansible-collections/community.general/pull/11049).
- linode inventory plugin - avoid using deprecated option when templating options (https://github.com/ansible-collections/community.general/pull/10271).
- linode inventory plugin - improve Python code (https://github.com/ansible-collections/community.general/pull/11043).
- listen_port_facts - avoid crash when required commands are missing (https://github.com/ansible-collections/community.general/issues/10457, https://github.com/ansible-collections/community.general/pull/10458).
- listen_ports_facts - improve Python code (https://github.com/ansible-collections/community.general/pull/11043).
- listen_ports_facts - improve Python code by removing unnecessary variables (https://github.com/ansible-collections/community.general/pull/11049).
- logentries callback plugin - improve Python code by removing unnecessary variables (https://github.com/ansible-collections/community.general/pull/11049).
- logstash callback plugin - remove reference to Python 2 library (https://github.com/ansible-collections/community.general/pull/10345).
- lvm_pv - properly detect SCSI or NVMe devices to rescan (https://github.com/ansible-collections/community.general/issues/10444, https://github.com/ansible-collections/community.general/pull/10596).
- lxc_container - improve Python code (https://github.com/ansible-collections/community.general/pull/11043).
- lxd_container - improve Python code (https://github.com/ansible-collections/community.general/pull/11043).
- machinectl become plugin - disable pipelining on ansible-core 2.19+. The plugin does not work with pipelining, and since ansible-core 2.19 become plugins can indicate that they do not work with pipelining (https://github.com/ansible-collections/community.general/pull/10537).
- manageiq_alert_profiles - improve Python code by removing unnecessary variables (https://github.com/ansible-collections/community.general/pull/11049).
- manageiq_provider - improve Python code by removing unnecessary variables (https://github.com/ansible-collections/community.general/pull/11049).
- manageiq_tenant - improve Python code by removing unnecessary variables (https://github.com/ansible-collections/community.general/pull/11049).
- matrix - improve Python code (https://github.com/ansible-collections/community.general/pull/11043).
- maven_artifact - improve Python code (https://github.com/ansible-collections/community.general/pull/11043).
- memset_memstore_info - improve Python code by removing unnecessary variables (https://github.com/ansible-collections/community.general/pull/11049).
- memset_server_info - improve Python code by removing unnecessary variables (https://github.com/ansible-collections/community.general/pull/11049).
- memset_zone - improve Python code by removing unnecessary variables (https://github.com/ansible-collections/community.general/pull/11049).
- merge_variables lookup plugin - avoid deprecated functionality from ansible-core 2.19 (https://github.com/ansible-collections/community.general/pull/10566).
- module_helper module utils - improve Python code (https://github.com/ansible-collections/community.general/pull/11043).
- monit - fix crash caused by an unknown status value returned from the monit service (https://github.com/ansible-collections/community.general/issues/10742, https://github.com/ansible-collections/community.general/pull/10743).
- monit - improve Python code (https://github.com/ansible-collections/community.general/pull/11043).
- netcup_dns - improve Python code (https://github.com/ansible-collections/community.general/pull/11043).
- nmcli - improve Python code (https://github.com/ansible-collections/community.general/pull/11043).
- nomad_job - improve Python code (https://github.com/ansible-collections/community.general/pull/11043).
- nosh - improve Python code by removing unnecessary variables (https://github.com/ansible-collections/community.general/pull/11049).
- npm - improve Python code (https://github.com/ansible-collections/community.general/pull/11043).
- odbc - improve Python code by removing unnecessary variables (https://github.com/ansible-collections/community.general/pull/11049).
- omapi_host - make return values compatible with ansible-core 2.19 and Python 3 (https://github.com/ansible-collections/community.general/pull/11001).
- one_host - improve Python code (https://github.com/ansible-collections/community.general/pull/11043).
- one_image - improve Python code (https://github.com/ansible-collections/community.general/pull/11043).
- one_service - improve Python code by removing unnecessary variables (https://github.com/ansible-collections/community.general/pull/11049).
- one_template - improve Python code (https://github.com/ansible-collections/community.general/pull/11043).
- one_vm - improve Python code (https://github.com/ansible-collections/community.general/pull/11043).
- one_vm - improve Python code by removing unnecessary variables (https://github.com/ansible-collections/community.general/pull/11049).
- one_vnet - improve Python code (https://github.com/ansible-collections/community.general/pull/11043).
- oneandone module utils - improve Python code (https://github.com/ansible-collections/community.general/pull/11043).
- onepassword_doc and onepassword_ssh_key lookup plugins - ensure that all connection parameters are passed to CLI class (https://github.com/ansible-collections/community.general/pull/10965).
- onepassword_info - improve Python code (https://github.com/ansible-collections/community.general/pull/11043).
- online inventory plugin - improve Python code by removing unnecessary variables (https://github.com/ansible-collections/community.general/pull/11049).
- opendj_backendprop - improve Python code by removing unnecessary variables (https://github.com/ansible-collections/community.general/pull/11049).
- opennebula module utils - improve Python code (https://github.com/ansible-collections/community.general/pull/11043).
- opentelemetry callback plugin - improve Python code by removing unnecessary variables (https://github.com/ansible-collections/community.general/pull/11049).
- ovh_monthly_billing - improve Python code by removing unnecessary variables (https://github.com/ansible-collections/community.general/pull/11049).
- pacemaker - use regex for matching ``maintenance-mode`` output to determine cluster maintenance status (https://github.com/ansible-collections/community.general/issues/10426, https://github.com/ansible-collections/community.general/pull/10707).
- pacemaker_resource - fix ``resource_type`` parameter formatting (https://github.com/ansible-collections/community.general/issues/10426, https://github.com/ansible-collections/community.general/pull/10663).
- pamd - improve Python code (https://github.com/ansible-collections/community.general/pull/11043).
- parted - variable is a list, not text (https://github.com/ansible-collections/community.general/pull/10823, https://github.com/ansible-collections/community.general/issues/10817).
- pids - prevent error when an empty string is provided for ``name`` (https://github.com/ansible-collections/community.general/issues/10672, https://github.com/ansible-collections/community.general/pull/10688).
- pkgin - improve Python code (https://github.com/ansible-collections/community.general/pull/11043).
- portinstall - improve Python code by removing unnecessary variables (https://github.com/ansible-collections/community.general/pull/11049).
- pritunl_user - improve resilience when comparing user parameters if remote fields are ``null`` or missing. List parameters (``groups``, ``mac_addresses``) now safely default to empty lists for comparison and avoids ``KeyError`` issues (https://github.com/ansible-collections/community.general/issues/10954, https://github.com/ansible-collections/community.general/pull/10955).
- pulp_repo - improve Python code (https://github.com/ansible-collections/community.general/pull/11043).
- random_string lookup plugin - replace ``random.SystemRandom()`` with ``secrets.SystemRandom()`` when generating strings. This has no practical effect, as both are the same (https://github.com/ansible-collections/community.general/pull/10893).
- redfish_utils module utils - improve Python code by removing unnecessary variables (https://github.com/ansible-collections/community.general/pull/11049).
- redhat_subscription - improve Python code (https://github.com/ansible-collections/community.general/pull/11043).
- redhat_subscription - improve Python code by removing unnecessary variables (https://github.com/ansible-collections/community.general/pull/11049).
- redis_data_incr - improve Python code by removing unnecessary variables (https://github.com/ansible-collections/community.general/pull/11049).
- rhevm - improve Python code (https://github.com/ansible-collections/community.general/pull/11043).
- rocketchat - fix message delivery in Rocket Chat >= 7.5.3 by forcing ``Content-Type`` header to ``application/json`` instead of the default ``application/x-www-form-urlencoded`` (https://github.com/ansible-collections/community.general/issues/10796, https://github.com/ansible-collections/community.general/pull/10796).
- scaleway module utils - improve Python code by removing unnecessary variables (https://github.com/ansible-collections/community.general/pull/11049).
- scaleway_sshkey - improve Python code by removing unnecessary variables (https://github.com/ansible-collections/community.general/pull/11049).
- selective callback plugin - specify ``ansible_loop_var`` instead of the explicit value ``item`` when printing task result (https://github.com/ansible-collections/community.general/pull/10752).
- sensu_check - improve Python code (https://github.com/ansible-collections/community.general/pull/11043).
- simpleinit_msb - improve Python code (https://github.com/ansible-collections/community.general/pull/11043).
- sorcery - improve Python code (https://github.com/ansible-collections/community.general/pull/11043).
- spectrum_model_attrs - improve Python code by removing unnecessary variables (https://github.com/ansible-collections/community.general/pull/11049).
- spotinst_aws_elastigroup - improve Python code by removing unnecessary variables (https://github.com/ansible-collections/community.general/pull/11049).
- svc - improve Python code by removing unnecessary variables (https://github.com/ansible-collections/community.general/pull/11049).
- syslog_json callback plugin - improve Python code by removing unnecessary variables (https://github.com/ansible-collections/community.general/pull/11049).
- syspatch - avoid ansible-core 2.19 deprecation (https://github.com/ansible-collections/community.general/pull/10459).
- sysrc - fixes parsing with multi-line variables (https://github.com/ansible-collections/community.general/issues/10394, https://github.com/ansible-collections/community.general/pull/10417).
- sysupgrade - avoid ansible-core 2.19 deprecation (https://github.com/ansible-collections/community.general/pull/10459).
- terraform - fix bug when ``null`` values inside complex vars are throwing error instead of being passed to terraform. Now terraform can handle ``null``s in ``complex_vars`` itself (https://github.com/ansible-collections/community.general/pull/10961).
- terraform - improve Python code (https://github.com/ansible-collections/community.general/pull/11043).
- timestamp callback plugin - improve Python code (https://github.com/ansible-collections/community.general/pull/11043).
- timezone - improve Python code (https://github.com/ansible-collections/community.general/pull/11043).
- to_* time filter plugins - improve Python code (https://github.com/ansible-collections/community.general/pull/11043).
- to_prettytable filter plugin - improve Python code by removing unnecessary variables (https://github.com/ansible-collections/community.general/pull/11049).
- vmadm - improve Python code by removing unnecessary variables (https://github.com/ansible-collections/community.general/pull/11049).
- wsl connection plugin - avoid deprecated ansible-core paramiko import helper, import paramiko directly instead (https://github.com/ansible-collections/community.general/issues/10515, https://github.com/ansible-collections/community.general/pull/10531).
- wsl connection plugin - improve Python code (https://github.com/ansible-collections/community.general/pull/11043).
- wsl connection plugin - rename variable to fix type checking (https://github.com/ansible-collections/community.general/pull/11030).
- xen_orchestra inventory plugin - improve Python code by removing unnecessary variables (https://github.com/ansible-collections/community.general/pull/11049).
- xenserver module utils - improve Python code by removing unnecessary variables (https://github.com/ansible-collections/community.general/pull/11049).
- xenserver_guest - improve Python code (https://github.com/ansible-collections/community.general/pull/11043).
- xenserver_guest - improve Python code by removing unnecessary variables (https://github.com/ansible-collections/community.general/pull/11049).
- xfconf - fix handling of empty array properties (https://github.com/ansible-collections/community.general/pull/11026).
- xfconf_info - fix handling of empty array properties (https://github.com/ansible-collections/community.general/pull/11026).
- xfs_quota - improve Python code by removing unnecessary variables (https://github.com/ansible-collections/community.general/pull/11049).
- xml - improve Python code by removing unnecessary variables (https://github.com/ansible-collections/community.general/pull/11049).
- yaml cache plugin - make compatible with ansible-core 2.19 (https://github.com/ansible-collections/community.general/issues/10849, https://github.com/ansible-collections/community.general/issues/10852).
- zypper_repository - avoid ansible-core 2.19 deprecation (https://github.com/ansible-collections/community.general/pull/10459).
- zypper_repository - improve Python code (https://github.com/ansible-collections/community.general/pull/11043).

community.hrobot
~~~~~~~~~~~~~~~~

- Avoid deprecated functionality in ansible-core 2.20 (https://github.com/ansible-collections/community.hrobot/pull/174).
- Avoid using ``ansible.module_utils.six`` in more places to avoid deprecation warnings with ansible-core 2.20 (https://github.com/ansible-collections/community.hrobot/pull/179).
- Avoid using ``ansible.module_utils.six`` to avoid deprecation warnings with ansible-core 2.20 (https://github.com/ansible-collections/community.hrobot/pull/177).

community.library_inventory_filtering_v1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Avoid deprecated functionality in ansible-core 2.20 (https://github.com/ansible-collections/community.library_inventory_filtering/pull/38).
- Fix accidental type extensions (https://github.com/ansible-collections/community.library_inventory_filtering/pull/40).
- Improve and stricten typing information (https://github.com/ansible-collections/community.library_inventory_filtering/pull/42).
- Stop using ``ansible.module_utils.six`` to avoid user-facing deprecation messages with ansible-core 2.20, while still supporting older ansible-core versions (https://github.com/ansible-collections/community.library_inventory_filtering/pull/39).

community.mysql
~~~~~~~~~~~~~~~

- mysql_info - Fix slave status for source terminology introduced in MySQL 8.0.23 (https://github.com/ansible-collections/community.mysql/issues/682).
- mysql_user, mysql_role - fix not existent grant when revoking perms on user/role which do not have any other perms than grant option (https://github.com/ansible-collections/community.mysql/issues/664).

community.proxmox
~~~~~~~~~~~~~~~~~

- proxmox inventory plugin and proxmox module utils - avoid Python 2 compatibility imports (https://github.com/ansible-collections/community.proxmox/pull/175).
- proxmox_kvm - remove limited choice for vga option in proxmox_kvm (https://github.com/ansible-collections/community.proxmox/pull/185)
- proxmox_kvm, proxmox_template - remove ``ansible.module_utils.six`` dependency (https://github.com/ansible-collections/community.proxmox/pull/201).
- proxmox_storage - fixed adding PBS-type storage by ensuring its parameters (server, datastore, etc.) are correctly sent to the Proxmox API (https://github.com/ansible-collections/community.proxmox/pull/171).
- proxmox_user - added a third case when testing for not-yet-existant user (https://github.com/ansible-collections/community.proxmox/issues/163)
- proxmox_vm_info - do not throw exception when iterating through machines and optional api results are missing (https://github.com/ansible-collections/community.proxmox/pull/191)

community.routeros
~~~~~~~~~~~~~~~~~~

- Avoid using ``ansible.module_utils.six`` to avoid deprecation warnings with ansible-core 2.20 (https://github.com/ansible-collections/community.routeros/pull/405).
- Fix accidental type extensions (https://github.com/ansible-collections/community.routeros/pull/406).
- api - allow querying for keys containing ``id``, as long as the key itself is not ``id`` (https://github.com/ansible-collections/community.routeros/issues/396, https://github.com/ansible-collections/community.routeros/pull/398).

community.sops
~~~~~~~~~~~~~~

- Avoid using ``ansible.module_utils.six`` to avoid deprecation warnings with ansible-core 2.20 (https://github.com/ansible-collections/community.sops/pull/268).
- Clean up plugin code that does not run on the target (https://github.com/ansible-collections/community.sops/pull/275).
- Fix accidental type extensions (https://github.com/ansible-collections/community.sops/pull/269).
- Note that the MIT licenced code in ``plugins/module_utils/_six.py`` has been removed (https://github.com/ansible-collections/community.sops/pull/275).
- load_vars action - avoid another deprecated module utils from ansible-core (https://github.com/ansible-collections/community.sops/pull/270).
- load_vars action - avoid deprecated import from ansible-core that will be removed in ansible-core 2.21 (https://github.com/ansible-collections/community.sops/pull/272).
- sops vars plugin - ensure that loaded vars are evaluated also with ansible-core 2.19+ (https://github.com/ansible-collections/community.sops/pull/273).

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

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- Fixed the UT test execution through ansible-test - (Issue 1003) - Tests Pass Using Tox But Not Ansible-Test (https://github.com/dell/dellemc-openmanage-ansible-modules)
- idrac_server_config_profile - (Issue 959) Can't export SCP (Server configuration profile) on iDRAC 10. (https://github.com/dell/dellemc-openmanage-ansible-modules/issues/959)
- idrac_support_assist - Updated module playbook examples to use the correct casing for protocol names, for CIFS and HTTPS.
- idrac_system_info - (Issue 1017) - System info not being returned on gen17s with v10.0.0 (https://github.com/dell/dellemc-openmanage-ansible-modules/issues/1017)
- idrac_system_info - (Issue 967) - idrac_system_info fails on iDRAC10 with GPU. (https://github.com/dell/dellemc-openmanage-ansible-modules/issues/967)
- redfish_storage_volume - (Issue 1027) Module fails on force reboot. (https://github.com/dell/dellemc-openmanage-ansible-modules/issues/1027)

fortinet.fortimanager
~~~~~~~~~~~~~~~~~~~~~

- Changed the logic of getting FortiManager system information to prevent permission denied error.
- Supported module_defaults. General variables can be specified in one place by using module_defaults.

fortinet.fortios
~~~~~~~~~~~~~~~~

- Fix the issue in check_modu when backend returns invallid IP address.
- Fix the issue in configuration_fact and monitor_fact when omitting vdom or assigning vdom to "".
- Fixed authentication issue in v7.6.4 when using access_token.

google.cloud
~~~~~~~~~~~~

- gcp_compute_instance - add suppport for attaching disks to compute instances (https://github.com/ansible-collections/google.cloud/pull/711).
- gcp_secret_manager - use service_account_contents instead of service_account_info (https://github.com/ansible-collections/google.cloud/pull/703).

hetzner.hcloud
~~~~~~~~~~~~~~

- floating_ip - Wait for the Floating IP assign action to complete to reduce chances of running into ``locked`` errors.
- server - Also check server type deprecation after server creation.

ibm.storage_virtualize
~~~~~~~~~~~~~~~~~~~~~~

- ibm_svc_manage_ip - Fixed issues with IP address probe
- ibm_svc_manage_volume - Fixed data-type conversion issue for grainsize
- ibm_svc_mdiskgrp - Removed mandatory system mask setting during pool-linking
- ibm_svc_start_stop_flashcopy - Fixed flashcopy start issues when mapping belonged to flashcopy consistency group

ieisystem.inmanage
~~~~~~~~~~~~~~~~~~

- Modify the automated tests and add support for version 2.18. (https://github.com/ieisystem/ieisystem.inmanage/pull/28).
- Modify the failure details returned in module_utils (https://github.com/ieisystem/ieisystem.inmanage/pull/26).
- Modify the inmanage.py file in the module_utils directory, and change the reference path of iteritems to be a reference from within Python. (https://github.com/ieisystem/ieisystem.inmanage/pull/29).
- Modify the method referenced in the support_info.py file to be support_info_nf . (https://github.com/ieisystem/ieisystem.inmanage/pull/31).

kubernetes.core
~~~~~~~~~~~~~~~

- Remove ``ansible.module_utils.six`` imports to avoid warnings (https://github.com/ansible-collections/kubernetes.core/pull/998).
- Update the `k8s_cp` module to also work for init containers (https://github.com/ansible-collections/kubernetes.core/pull/971).

netapp.ontap
~~~~~~~~~~~~

- Added manual utf-8 encoding to handle unicode characters in passwords for HTTP Basic Authentication in netapp module utilities.
- na_ontap_ntfs_dacl - fixed typo in short description.
- na_ontap_rest_info - added error handling when API doesn't return zero records.
- na_ontap_snapmirror - fixed intermittent issue with creating relationship.
- na_ontap_volume - fix idempotency issue with `nas_application_template` and `size_change_threshold`.

ngine_io.cloudstack
~~~~~~~~~~~~~~~~~~~

- Ensure tags are applied when creating or updating a template (https://github.com/ngine-io/ansible-collection-cloudstack/pull/154).

purestorage.flasharray
~~~~~~~~~~~~~~~~~~~~~~

- purefa_certs - Resolved error with incorrect use of ``key_size`` for imported certificates
- purefa_connect - Ensured that encrypted connections use encrypted connection keys
- purefa_eradication - Fixed idempotency issue
- purefa_eradication - Idempotency fix
- purefa_eula - Fix AttributeError when first sogning EULA
- purefa_host - Fixed Pydantic error when updating preferred_arrays
- purefa_info - Ensured that volumes, hosts, host_groups and transfers are correctly listed for protection groups
- purefa_info - Fixed AttributeError for hgroups subset
- purefa_info - Fixed AttributeError in config section related to SSO SAML2
- purefa_info - Fixed issue with replication connection throttle reporting
- purefa_info - Fixed issue with undo-demote pods not reporting correctly
- purefa_info - Resolved AttributeError in volume subset
- purefa_network - Resolve typo that causes network updates to not apply correctly
- purefa_pg - Changing target for PG no longer requires a ``FixedReference``
- purefa_pg - Fixed AttributeError adding target to PG
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

vmware.vmware
~~~~~~~~~~~~~

- Drop incorrect requirement on aiohttp (https://github.com/ansible-collections/vmware.vmware/pull/230).
- cluster_ha - Fix admission control policy not being updated when ac is disabled
- content_template - Fix typo in code for check mode that tried to access a module param which doesn't exist.
- import_content_library_ovf - Fix large file import by using requests instead of open_url. Requests allows for streaming uploads, instead of reading the entire file into memory. (Fixes https://github.com/ansible-collections/vmware.vmware/issues/220)
- vm_powerstate - Ensure timeout option also applies to the shutdown-guest state

Known Issues
------------

Ansible-core
~~~~~~~~~~~~

- templating - Exceptions raised in a Jinja ``set`` or ``with`` block which are not accessed by the template are ignored in the same manner as undefined values.
- templating - Passing a container created in a Jinja ``set`` or ``with`` block to a method results in a copy of that container. Mutations to that container which are not returned by the method will be discarded.

community.sops
~~~~~~~~~~~~~~

- When using the ``community.sops.load_vars`` with ansible-core 2.20, note that the deprecation of ``INJECT_FACTS_AS_VARS`` causes deprecation warnings to be shown every time a variable loaded with ``community.sops.load_vars`` is used. This is due to ansible-core deprecating ``INJECT_FACTS_AS_VARS`` without providing an alternative for modules like ``community.sops.load_vars`` to use. If you do not like these deprecation warnings, you have to explicitly set ``INJECT_FACTS_AS_VARS`` to ``true``. **DO NOT** change the use of SOPS encrypted variables to ``ansible_facts``. The situation will hopefully improve in ansible-core 2.21 through the promised API that allows action plugins to set variables; community.sops will adapt to use it, which will make the warning go away. (The API was originally promised for ansible-core 2.20, but then delayed.)

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- Formal qualification of module ome_smart_fabric_info for Ansible Core version 2.19 is still pending.
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
- redfish_storage_volume - Encryption type and block_io_size bytes will be read only property in iDRAC9 and iDRAC10 and hence the module ignores these parameters.

New Plugins
-----------

Callback
~~~~~~~~

- community.general.tasks_only - Only show tasks.

Filter
~~~~~~

- community.general.to_nice_yaml - Convert variable to YAML string.
- community.general.to_yaml - Convert variable to YAML string.

Inventory
~~~~~~~~~

- community.general.incus - Incus inventory source.
- containers.podman.buildah_containers - Inventory plugin that discovers Buildah working containers as hosts
- containers.podman.podman_containers - Inventory plugin that discovers Podman containers as hosts

Lookup
~~~~~~

- community.dns.lookup_rfc8427 - Look up DNS records and return RFC 8427 JSON format.
- community.general.binary_file - Read binary file and return it Base64 encoded.

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

- community.general.django_dumpdata - Wrapper for ``django-admin dumpdata``.
- community.general.django_loaddata - Wrapper for ``django-admin loaddata``.
- community.general.jenkins_credential - Manage Jenkins credentials and domains through API.
- community.general.kea_command - Submits generic command to ISC KEA server on target.
- community.general.keycloak_user_execute_actions_email - Send a Keycloak execute-actions email to a user.
- community.general.lvm_pv_move_data - Move data between LVM Physical Volumes (PVs).
- community.general.pacemaker_info - Gather information about Pacemaker cluster.
- community.general.pacemaker_stonith - Manage Pacemaker STONITH.

community.proxmox
~~~~~~~~~~~~~~~~~

- community.proxmox.proxmox_cluster_ha_rules - Management of HA rules.
- community.proxmox.proxmox_firewall - Manage firewall rules in Proxmox.
- community.proxmox.proxmox_firewall_info - Manage firewall rules in Proxmox.
- community.proxmox.proxmox_ipam_info - Retrieve information about IPAMs.
- community.proxmox.proxmox_subnet - Create/Update/Delete subnets from SDN.
- community.proxmox.proxmox_vnet - Manage virtual networks in Proxmox SDN.
- community.proxmox.proxmox_vnet_info - Retrieve information about one or more Proxmox VE SDN vnets.
- community.proxmox.proxmox_zone - Manage Proxmox zone configurations.
- community.proxmox.proxmox_zone_info - Get Proxmox zone info.

community.proxysql
~~~~~~~~~~~~~~~~~~

- community.proxysql.proxysql_mysql_hostgroup_attributes - Manages hostgroup attributes using the ProxySQL admin interface

containers.podman
~~~~~~~~~~~~~~~~~

- containers.podman.podman_system_connection - Manage Podman system connections
- containers.podman.podman_system_connection_info - Get info about Podman system connections

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

dellemc.powerflex
~~~~~~~~~~~~~~~~~

- dellemc.powerflex.device_v2 - Manage device on Dell PowerFlex Gen2
- dellemc.powerflex.info_v2 - Gathering information about Dell PowerFlex Gen2
- dellemc.powerflex.protection_domain_v2 - Manage Protection Domain on Dell PowerFlex Gen2
- dellemc.powerflex.snapshot_v2 - Manage Snapshots on Dell PowerFlex Gen2
- dellemc.powerflex.storagepool_v2 - Managing Dell PowerFlex storage pool Gen2
- dellemc.powerflex.volume_v2 - Manage volumes on Dell PowerFlex Gen2

hitachivantara.vspone_block
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Sds Block
^^^^^^^^^

- hitachivantara.vspone_block.hv_sds_block_capacity_management_settings_facts - Get capacity management settings from storage system.
- hitachivantara.vspone_block.hv_sds_block_compute_port - Manages compute port on Hitachi SDS Block storage systems.
- hitachivantara.vspone_block.hv_sds_block_drive - Manages drive on Hitachi SDS Block storage systems.
- hitachivantara.vspone_block.hv_sds_block_software_update_file_facts - Get the information of the update file of the storage software which performed transfer (upload) in the storage cluster.
- hitachivantara.vspone_block.hv_sds_block_storage_controller - Edits the settings for the storage controller on Hitachi SDS Block storage systems.
- hitachivantara.vspone_block.hv_sds_block_storage_node_bmc_connection - Manages BMC connection settings for a storage node on Hitachi SDS Block storage systems.
- hitachivantara.vspone_block.hv_sds_block_storage_node_bmc_connection_facts - Get storage node BMC access settings from storage system.
- hitachivantara.vspone_block.hv_sds_block_storage_pool_estimated_capacity_facts - Obtains the preliminary calculation results of the storage pool logical capacity (unit TiB).
- hitachivantara.vspone_block.hv_sds_block_storage_software_update - Manages software update and downgrade on Hitachi SDS Block storage systems.

Vsp
^^^

- hitachivantara.vspone_block.hv_vsp_one_port - Manages port configuration on Hitachi VSP One storage systems.
- hitachivantara.vspone_block.hv_vsp_one_port_facts - Retrieves port information from Hitachi VSP One storage systems.
- hitachivantara.vspone_block.hv_vsp_one_server - Manages servers on Hitachi VSP One storage systems.
- hitachivantara.vspone_block.hv_vsp_one_server_facts - Retrieves server information from Hitachi VSP One storage systems.
- hitachivantara.vspone_block.hv_vsp_one_server_hba_facts - Retrieves server HBA information from Hitachi VSP One storage systems.
- hitachivantara.vspone_block.hv_vsp_one_snapshot - Manages snapshots on Hitachi VSP One storage systems.
- hitachivantara.vspone_block.hv_vsp_one_snapshot_facts - Retrieves snapshot information from Hitachi VSP One storage systems.
- hitachivantara.vspone_block.hv_vsp_one_snapshot_group - Manages snapshot group operations in Hitachi VSP One storage systems.
- hitachivantara.vspone_block.hv_vsp_one_snapshot_group_facts - Retrieves snapshot group information from Hitachi VSP One storage systems.
- hitachivantara.vspone_block.hv_vsp_one_volume - Manages volumes on Hitachi VSP One storage systems.
- hitachivantara.vspone_block.hv_vsp_one_volume_facts - Retrieves facts about Hitachi VSP One storage system volumes.

ibm.storage_virtualize
~~~~~~~~~~~~~~~~~~~~~~

- ibm.storage_virtualize.ibm_sv_manage_system_certificate - Manages system certificates and truststore for replication, high availability and FlashSystem grid on IBM Storage Virtualize family systems

ieisystem.inmanage
~~~~~~~~~~~~~~~~~~

- ieisystem.inmanage.generate_ssl - Generate SSL certificate
- ieisystem.inmanage.ssl_info - Get SSL certificate information
- ieisystem.inmanage.upload_ssl - Upload SSL certificate

ngine_io.cloudstack
~~~~~~~~~~~~~~~~~~~

- ngine_io.cloudstack.configuration_info - Gathering information about configurations from Apache CloudStack based clouds.

purestorage.flashblade
~~~~~~~~~~~~~~~~~~~~~~

- purestorage.flashblade.purefb_kmip - Manage FlashBlade KMIP server objects

theforeman.foreman
~~~~~~~~~~~~~~~~~~

- theforeman.foreman.content_view_history_info - Fetch history of a Content View

Unchanged Collections
---------------------

- ansible.netcommon (still version 8.1.0)
- ansible.posix (still version 2.1.0)
- ansible.utils (still version 6.0.0)
- ansible.windows (still version 3.2.0)
- arista.eos (still version 12.0.0)
- awx.awx (still version 24.6.1)
- chocolatey.chocolatey (still version 1.5.3)
- cisco.aci (still version 2.12.0)
- cisco.mso (still version 2.11.0)
- cisco.nxos (still version 11.0.0)
- cisco.ucs (still version 1.16.0)
- cloudscale_ch.cloud (still version 2.5.2)
- community.aws (still version 10.0.0)
- community.ciscosmb (still version 1.0.11)
- community.grafana (still version 2.3.0)
- community.libvirt (still version 2.0.0)
- community.mongodb (still version 1.7.10)
- community.okd (still version 5.0.0)
- community.postgresql (still version 4.1.0)
- community.rabbitmq (still version 1.6.0)
- community.windows (still version 3.0.1)
- dellemc.unity (still version 2.1.0)
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
- netapp.storagegrid (still version 21.15.0)
- netapp_eseries.santricity (still version 1.4.1)
- netbox.netbox (still version 3.21.0)
- ovirt.ovirt (still version 3.2.1)
- splunk.es (still version 4.0.0)
- telekom_mms.icinga_director (still version 2.4.0)
- vmware.vmware_rest (still version 4.9.0)
- vultr.cloud (still version 1.13.0)
- vyos.vyos (still version 6.0.0)
- wti.remote (still version 1.0.10)
