=======================
Ansible 7 Release Notes
=======================

This changelog describes changes since Ansible 6.0.0.

.. contents::
  :local:
  :depth: 2

v7.5.0
======

.. contents::
  :local:
  :depth: 2

Release Summary
---------------

Release Date: 2023-04-26

`Porting Guide <https://docs.ansible.com/ansible/devel/porting_guides.html>`_

Added Collections
-----------------

- microsoft.ad (version 1.0.0)

Ansible-core
------------

Ansible 7.5.0 contains Ansible-core version 2.14.5.
This is a newer version than version 2.14.4 contained in the previous Ansible release.

The changes are reported in the combined changelog below.

Changed Collections
-------------------

If not mentioned explicitly, the changes are reported in the combined changelog below.

+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| Collection             | Ansible 7.4.0 | Ansible 7.5.0 | Notes                                                                                                                        |
+========================+===============+===============+==============================================================================================================================+
| ansible.posix          | 1.5.1         | 1.5.2         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| arista.eos             | 6.0.0         | 6.0.1         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.aci              | 2.4.0         | 2.6.0         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.dnac             | 6.6.4         | 6.7.1         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.intersight       | 1.0.24        | 1.0.27        | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.ios              | 4.4.0         | 4.5.0         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.mso              | 2.2.1         | 2.4.0         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.nxos             | 4.1.0         | 4.3.0         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.crypto       | 2.11.1        | 2.12.0        |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.dns          | 2.5.2         | 2.5.3         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.general      | 6.5.0         | 6.6.0         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.mongodb      | 1.5.1         | 1.5.2         | There are no changes recorded in the changelog.                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.zabbix       | 1.9.2         | 1.9.3         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| dellemc.powerflex      | 1.5.0         | 1.6.0         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| dellemc.unity          | 1.5.0         | 1.6.0         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| frr.frr                | 2.0.0         | 2.0.2         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| hetzner.hcloud         | 1.10.0        | 1.11.0        |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| microsoft.ad           |               | 1.0.0         | The collection was added to Ansible                                                                                          |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| netapp.ontap           | 22.4.1        | 22.5.0        |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| netbox.netbox          | 3.11.0        | 3.12.0        |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| purestorage.flashblade | 1.10.0        | 1.11.0        |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| purestorage.fusion     | 1.4.1         | 1.4.2         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| theforeman.foreman     | 3.9.0         | 3.10.0        |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| vyos.vyos              | 4.0.1         | 4.0.2         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+

Minor Changes
-------------

ansible.posix
~~~~~~~~~~~~~

- Add jsonl callback plugin to ansible.posix collection
- firewalld - add `protocol` parameter

cisco.aci
~~~~~~~~~

- Add aci_access_span_dst_group module for fabric access policies span destination group support (#405)
- Add aci_access_span_filter_group and aci_access_span_filter_group_entry modules for access span filter group support (#407)
- Add aci_config_export_policy module (#380)
- Add aci_igmp_interface_policy module (#381)
- Add aci_interface_config module for new interface configuration available in ACI v5.2(5)+ (#383)
- Add aci_interface_policy_spanning_tree  module (#387)

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

- ios_bgp_address_family - add option redistribute.ospf.include_connected when redistributing OSPF in IPv6 AFI
- ios_bgp_address_family - add option redistribute.ospf.match.externals.type_1 to allow
- ios_bgp_address_family - add option redistribute.ospf.match.externals.type_2 to allow
- specification of OSPF E1 routes
- specification of OSPF E2 routes

cisco.mso
~~~~~~~~~

- Add ip_data_plane_learning and preferred_group arguments to mso_schema_template_vrf module (#358)
- Add module mso_schema_site_anp_epg_bulk_staticport (#330)
- Add route_reachability attribute to mso_schema_site_external_epg module (#335)

cisco.nxos
~~~~~~~~~~

- `nxos_route_maps` - add support for 'set ip next-hop <>' command in route-maps
- `nxos_vxlan_vtep` - add support for 'advertise virtual-rmac' command under nve interface

community.crypto
~~~~~~~~~~~~~~~~

- get_certificate - add ``asn1_base64`` option to control whether the ASN.1 included in the ``extensions`` return value is binary data or Base64 encoded (https://github.com/ansible-collections/community.crypto/pull/592).

community.general
~~~~~~~~~~~~~~~~~

- cpanm - minor change, use feature from ``ModuleHelper`` (https://github.com/ansible-collections/community.general/pull/6385).
- dconf - be forgiving about boolean values: convert them to GVariant booleans automatically (https://github.com/ansible-collections/community.general/pull/6206).
- dconf - minor refactoring improving parameters and dependencies validation (https://github.com/ansible-collections/community.general/pull/6336).
- deps module utils - add function ``failed()`` providing the ability to check the dependency check result without triggering an exception (https://github.com/ansible-collections/community.general/pull/6383).
- dig lookup plugin - Support multiple domains to be queried as indicated in docs (https://github.com/ansible-collections/community.general/pull/6334).
- gitlab_project - add new option ``topics`` for adding topics to GitLab projects (https://github.com/ansible-collections/community.general/pull/6278).
- homebrew_cask - allows passing ``--greedy`` option to ``upgrade_all`` (https://github.com/ansible-collections/community.general/pull/6267).
- idrac_redfish_command - add ``job_id`` to ``CreateBiosConfigJob`` response (https://github.com/ansible-collections/community.general/issues/5603).
- ipa_hostgroup - add ``append`` parameter for adding a new hosts to existing hostgroups without changing existing hostgroup members (https://github.com/ansible-collections/community.general/pull/6203).
- keycloak_authentication - add flow type option to sub flows to allow the creation of 'form-flow' sub flows like in Keycloak's built-in registration flow (https://github.com/ansible-collections/community.general/pull/6318).
- mksysb - improved the output of the module in case of errors (https://github.com/ansible-collections/community.general/issues/6263).
- nmap inventory plugin - added environment variables for configure ``address`` and ``exclude`` (https://github.com/ansible-collections/community.general/issues/6351).
- nmcli - add ``macvlan`` connection type (https://github.com/ansible-collections/community.general/pull/6312).
- pipx - add ``system_site_packages`` parameter to give application access to system-wide packages (https://github.com/ansible-collections/community.general/pull/6308).
- pipx - ensure ``include_injected`` parameter works with ``state=upgrade`` and ``state=latest`` (https://github.com/ansible-collections/community.general/pull/6212).
- puppet - add new options ``skip_tags`` to exclude certain tagged resources during a puppet agent or apply (https://github.com/ansible-collections/community.general/pull/6293).
- terraform - remove state file check condition and error block, because in the native implementation of terraform will not cause errors due to the non-existent file (https://github.com/ansible-collections/community.general/pull/6296).
- udm_dns_record - minor refactor to the code (https://github.com/ansible-collections/community.general/pull/6382).

community.zabbix
~~~~~~~~~~~~~~~~

- httpapi plugin - updated to work with Zabbix 6.4.
- zabbix_action, zabbix_authentication, zabbix_discovery_rule, zabbix_mediatype, zabbix_user, zabbix_user_directory, zabbix_usergroup - updated to work with Zabbix 6.4.
- zabbix_agent role - Add support for SUSE Linux Enterprise Server for SAP Applications ("SLES_SAP").
- zabbix_host - add missing variants for SNMPv3 authprotocol and privprotocol introduced by Zabbix 6
- zabbix_proxy role - Add variable zabbix_proxy_dbpassword_hash_method to control whether you want postgresql user password to be hashed with md5 or want to use db default. When zabbix_proxy_dbpassword_hash_method is set to anything other than md5 then do not hash the password with md5 so you could use postgresql scram-sha-256 hashing method.
- zabbix_server role - Add variable zabbix_server_dbpassword_hash_method to control whether you want postgresql user password to be hashed with md5 or want to use db default. When zabbix_server_dbpassword_hash_method is set to anything other than md5 then do not hash the password with md5 so you could use postgresql scram-sha-256 hashing method.
- zabbix_usergroup module - userdirectory, hostgroup_rights and templategroup_rights parameters added (Zabbix >= 6.2)
- zabbix_web role - possibility to add custom includes in apache vhost config

dellemc.powerflex
~~~~~~~~~~~~~~~~~

- Info module is enhanced to support the listing of replication pairs.

dellemc.unity
~~~~~~~~~~~~~

- Add synchronous replication support for filesystem.
- Support addition of host from the Host List to NFS Export in nfs module.
- Support enable/disable advanced dedup in volume module.

hetzner.hcloud
~~~~~~~~~~~~~~

- hcloud_image_info - Add cpu architecture field to return value.
- hcloud_image_info - Allow filtering images by cpu architecture.
- hcloud_server - Select matching image for the cpu architecture of the server type on create & rebuild.
- hcloud_server_type_info - Add cpu architecture field to return value.
- inventory plugin - Add cpu architecture to server variables.

netapp.ontap
~~~~~~~~~~~~

- na_ontap_cifs - new options ``browsable`` and ``show_previous_versions`` added in REST.
- na_ontap_cifs - removed default value for ``unix_symlink`` as its not supported with ZAPI.
- na_ontap_cifs - updated documentation and examples for REST.
- na_ontap_file_security_permissions - updated module examples.
- na_ontap_ipspace - improved module fail error message in REST.
- na_ontap_rest_info - improved documentation for ``parameters`` option.
- na_ontap_security_config - updated documentation for ``supported_cipher_suites``.
- na_ontap_user - option ``vserver`` is not required with REST, ignore this option to create cluster scoped user.

netbox.netbox
~~~~~~~~~~~~~

- netbox_aggregate - Add tenant as parameter to module [#968](https://github.com/netbox-community/ansible_modules/pull/968)
- netbox_asn - Add module [#947](https://github.com/netbox-community/ansible_modules/pull/947)
- netbox_fhrp_group - Add module [#957](https://github.com/netbox-community/ansible_modules/pull/957)
- netbox_journal_entry - Add module [#961](https://github.com/netbox-community/ansible_modules/pull/961)

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
- fusion_hap - added missing 'windows' personality type

theforeman.foreman
~~~~~~~~~~~~~~~~~~

- content_export_library, content_export_repository, content_export_version - add ``format`` option to control the export format
- content_view_filter - add support for creating modulemd filters
- content_view_publish role - also accept a list of dicts as the ``content_views`` role for publishing (https://github.com/theforeman/foreman-ansible-modules/issues/1436)
- setting - document how to obtain valid setting names (https://bugzilla.redhat.com/show_bug.cgi?id=2174367)

Deprecated Features
-------------------

cisco.ios
~~~~~~~~~

- ios_bgp_address_family - deprecate redistribute.ospf.match.external with redistribute.ospf.match.externals which enables attributes for OSPF type E1 and E2 routes
- ios_bgp_address_family - deprecate redistribute.ospf.match.nssa_external with redistribute.ospf.match.nssa_externals which enables attributes for OSPF type N1 and N2 routes
- ios_bgp_address_family - deprecate redistribute.ospf.match.type_1 with redistribute.ospf.match.nssa_externals.type_1
- ios_bgp_address_family - deprecate redistribute.ospf.match.type_2 with redistribute.ospf.match.nssa_externals.type_2

Bugfixes
--------

Ansible-core
~~~~~~~~~~~~

- Windows - Display a warning if the module failed to cleanup any temporary files rather than failing the task. The warning contains a brief description of what failed to be deleted.
- Windows - Ensure the module temp directory contains more unique values to avoid conflicts with concurrent runs - https://github.com/ansible/ansible/issues/80294
- Windows - Improve temporary file cleanup used by modules. Will use a more reliable delete operation on Windows Server 2016 and newer to delete files that might still be open by other software like Anti Virus scanners. There are still scenarios where a file or directory cannot be deleted but the new method should work in more scenarios.
- ansible-doc - stop generating wrong module URLs for module see-alsos. The URLs for modules in ansible.builtin do now work, and URLs for modules outside ansible.builtin are no longer added (https://github.com/ansible/ansible/pull/80280).
- ansible-galaxy - Improve retries for collection installs, to properly retry, and extend retry logic to common URL related connection errors (https://github.com/ansible/ansible/issues/80170 https://github.com/ansible/ansible/issues/80174)
- ansible-galaxy - reduce API calls to servers by fetching signatures only for final candidates.
- ansible-test - Add support for ``argcomplete`` version 3.
- jinja2_native - fix intermittent 'could not find job' failures when a value of ``ansible_job_id`` from a result of an async task was inadvertently changed during execution; to prevent this a format of ``ansible_job_id`` was changed.
- password lookup now correctly reads stored ident fields.
- pep517 build backend - Use the documented ``import_module`` import from ``importlib``.
- roles - Fix templating ``public``, ``allow_duplicates`` and ``rolespec_validate`` (https://github.com/ansible/ansible/issues/80304).
- syntax check - Limit ``--syntax-check`` to ``ansible-playbook`` only, as that is the only CLI affected by this argument (https://github.com/ansible/ansible/issues/80506)

ansible.posix
~~~~~~~~~~~~~

- Fixed a bug where firewalld module fails to create/remove zones when the daemon is stopped
- rhel_facts - Call exit_json with all keyword arguments

arista.eos
~~~~~~~~~~

- fix ntp_global authenticate config.
- https://github.com/ansible-collections/arista.eos/issues/399.

cisco.aci
~~~~~~~~~

- Fix missing annotation field in aci_ntp_policy and aci_ntp_server (#392)
- Forced unicode encoding for lxml XML fragment validation output  to fix issue with Certificate authentication and aci_rest with XML payload (#341)

cisco.ios
~~~~~~~~~

- Fix parser to read groups in snmp-server.
- Fix parser to read transceiver in snmp-server.
- ios_acls - fix processing of source information on extended acls entries.
- ios_acls - prevent rendering of mac access-lists in facts.
- ios_bgp_address_family - fix issue where no commands are generated when redistributing OSPFv2 and OSPFv3
- ios_bgp_address_family - fix missing negations in overridden and replaced states when redistributing OSPF
- ios_bgp_address_family - fix option and syntax for OSPF E1 and E2 routes
- ios_bgp_address_family - fix option and syntax for OSPF N1 and N2 routes
- ios_bgp_address_family - fix order of generated OSPF redistribution command options to achieve idempotency
- ios_bgp_global - fix configuration of timers under neighbor. (https://github.com/ansible-collections/cisco.ios/issues/794)
- ios_l3_interfaces - prevent configuration line generation when enable is false.
- ios_logging_global - logging history configuration command fixed for supported appliance versions.
- ios_static_routes - fix configure generation order for ipv4 and ipv6 routes.
- ios_static_routes - fix module to be idempotent with replaced and overridden state.

cisco.mso
~~~~~~~~~

- Add attributes to payload for changed schema behaviour of deploymentImmediacy (deployImmediacy) and vmmDomainProperties (properties at domain level in payload) (#362)
- Fix idempotency for mso_schema_site_bd_l3out
- Fix mso_backup for NDO and ND-based MSO v3.2+ (#333)
- Fix validation condition for path in mso_schema_site_anp_epg_bulk_staticport module (#360)

cisco.nxos
~~~~~~~~~~

- `bgp` - Fix parsing remote-as for Nexus 3K (https://github.com/ansible-collections/cisco.nxos/issues/653).
- `facts` - Attempt to execute json output commands with | json-pretty first and fall back to | json if unsupported. This is a temporary workaround until https://github.com/ansible/pylibssh/issues/208 is fixed.
- `interfaces` - Correctly enable/disable VLAN interfaces (https://github.com/ansible-collections/cisco.nxos/issues/539).
- `route_maps` - resolve route-map description parameter idempotency
- `snmp_server` - fix community option to produce proper configuration with ipv4acl and ipv6acl.

community.dns
~~~~~~~~~~~~~

- Update Public Suffix List.

community.general
~~~~~~~~~~~~~~~~~

- archive - reduce RAM usage by generating CRC32 checksum over chunks (https://github.com/ansible-collections/community.general/pull/6274).
- flatpak - fixes idempotency detection issues. In some cases the module could fail to properly detect already existing Flatpaks because of a parameter witch only checks the installed apps (https://github.com/ansible-collections/community.general/pull/6289).
- icinga2_host - fix the data structure sent to Icinga to make use of host templates and template vars (https://github.com/ansible-collections/community.general/pull/6286).
- idrac_redfish_command - allow user to specify ``resource_id`` for ``CreateBiosConfigJob`` to specify an exact manager (https://github.com/ansible-collections/community.general/issues/2090).
- ini_file - make ``section`` parameter not required so it is possible to pass ``null`` as a value. This only was possible in the past due to a bug in ansible-core that now has been fixed (https://github.com/ansible-collections/community.general/pull/6404).
- keycloak - improve error messages (https://github.com/ansible-collections/community.general/pull/6318).
- one_vm - fix syntax error when creating VMs with a more complex template (https://github.com/ansible-collections/community.general/issues/6225).
- pipx - fixed handling of ``install_deps=true`` with ``state=latest`` and ``state=upgrade`` (https://github.com/ansible-collections/community.general/pull/6303).
- redhat_subscription - do not use D-Bus for registering when ``environment`` is specified, so it possible to specify again the environment names for registering, as the D-Bus APIs work only with IDs (https://github.com/ansible-collections/community.general/pull/6319).
- redhat_subscription - try to unregister only when already registered when ``force_register`` is specified (https://github.com/ansible-collections/community.general/issues/6258, https://github.com/ansible-collections/community.general/pull/6259).
- redhat_subscription - use the right D-Bus options for environments when registering a CentOS Stream 8 system and using ``environment`` (https://github.com/ansible-collections/community.general/pull/6275).
- rhsm_release - make ``release`` parameter not required so it is possible to pass ``null`` as a value. This only was possible in the past due to a bug in ansible-core that now has been fixed (https://github.com/ansible-collections/community.general/pull/6401).
- rundeck module utils - fix errors caused by the API empty responses (https://github.com/ansible-collections/community.general/pull/6300)
- rundeck_acl_policy - fix ``TypeError - byte indices must be integers or slices, not str`` error caused by empty API response. Update the module to use ``module_utils.rundeck`` functions (https://github.com/ansible-collections/community.general/pull/5887, https://github.com/ansible-collections/community.general/pull/6300).
- rundeck_project - update the module to use ``module_utils.rundeck`` functions (https://github.com/ansible-collections/community.general/issues/5742) (https://github.com/ansible-collections/community.general/pull/6300)
- snap_alias - module would only recognize snap names containing letter, numbers or the underscore character, failing to identify valid snap names such as ``lxd.lxc`` (https://github.com/ansible-collections/community.general/pull/6361).

community.zabbix
~~~~~~~~~~~~~~~~

- compatibility with ansible.netcommon 5.0.0
- treat sendto parameter in module zabbix_user according to real media type, do not rely on media name
- zabbix-proxy role - fix tags for postgresql task.
- zabbix_agent role - Fix MacOS install never executed because of the missing include_tasks "Darwin.yml" in the "main.yml" task file and wrong user permission on folder/files.
- zabbix_user module - ability to specify several e-mail addresses in Zabbix User's  media

hetzner.hcloud
~~~~~~~~~~~~~~

- hcloud_server - Prevent backups from being disabled when undefined
- hcloud_server - Server locked after attaching to placement group

netapp.ontap
~~~~~~~~~~~~

- na_ontap_cifs - throw error if set ``unix_symlink`` in ZAPI.
- na_ontap_cifs - throw error if used options that require recent ONTAP version.
- na_ontap_file_security_permissions - error if more than one desired ACLs has same user, access, access_control and apply_to.
- na_ontap_file_security_permissions - fix TypeError when current acls is None.
- na_ontap_file_security_permissions - fix idempotency issue on ``acls.propagation_mode`` option.
- na_ontap_ipspace - fix cannot delete ipspace if ``from_ipspace`` is present.
- na_ontap_iscsi_security - error module if use_rest never is set.
- na_ontap_iscsi_security - fix KeyError on ``outbound_username`` option.
- na_ontap_qtree - ignore job entry does not exist error when creating qtree with REST to bypass ONTAP issue with FSx.
- na_ontap_quotas - ignore job entry does not exist error when creating quota with REST to bypass ONTAP issue with FSx.
- na_ontap_security_config - fix error on specifying protocol version ``TLSv1.1`` when fips is enabled.
- na_ontap_snapmirror - Added option ``identity_preservation`` support from ONTAP 9.11.1 in REST.
- na_ontap_snapmirror - error if identity_preservation set in ZAPI.

netbox.netbox
~~~~~~~~~~~~~

- Fix partial updates of custom_fields [#944](https://github.com/netbox-community/ansible_modules/pull/944)
- nb_inventory - Fix nb_inventory group_by by site_group [#952](https://github.com/netbox-community/ansible_modules/pull/952)
- netbox_location - Add multiple filter options to make sure we find the unique location [#963](https://github.com/netbox-community/ansible_modules/pull/963)

purestorage.flashblade
~~~~~~~~~~~~~~~~~~~~~~

- purefa_info - Fixed issue when more than 10 buckets have lifecycle rules.
- purefb_s3user - Fix incorrect response when bad key/secret pair provided for new user

purestorage.fusion
~~~~~~~~~~~~~~~~~~

- fusion_array - correct required parameters
- fusion_hap - display name has now default value set to the value of name
- fusion_hw - correct required parameters
- fusion_pg - correct required parameters
- fusion_pp - correct required parameters
- fusion_sc - correct required parameters
- fusion_ss - allow updating hardware types, correct required parameters
- fusion_tn - fix attribute error
- fusion_volume - protection policy can now be unset by using '' as name

theforeman.foreman
~~~~~~~~~~~~~~~~~~

- auth_sources_ldap role - don't assume ``account`` and ``account_password`` are set, they are documented as optional
- auth_sources_ldap role, compute_resources role, repositories role - do not log loop data when it contains sensitive data (https://bugzilla.redhat.com/show_bug.cgi?id=2183357)

vyos.vyos
~~~~~~~~~

- bgp_global - changed to use `neighbor.password` rather than `neighbor.address` (https://github.com/ansible-collections/vyos.vyos/issues/304).

New Modules
-----------

community.general
~~~~~~~~~~~~~~~~~

- community.general.btrfs_info - Query btrfs filesystem info
- community.general.btrfs_subvolume - Manage btrfs subvolumes
- community.general.ilo_redfish_command - Manages Out-Of-Band controllers using Redfish APIs
- community.general.keycloak_authz_authorization_scope - Allows administration of Keycloak client authorization scopes via Keycloak API
- community.general.keycloak_clientscope_type - Set the type of aclientscope in realm or client via Keycloak API

dellemc.powerflex
~~~~~~~~~~~~~~~~~

- dellemc.powerflex.replication_pair - Manage replication pairs on Dell PowerFlex

netbox.netbox
~~~~~~~~~~~~~

- netbox.netbox.netbox_asn - Create, update or delete ASN in NetBox
- netbox.netbox.netbox_fhrp_group - Create, update or delete FHRP groups in NetBox
- netbox.netbox.netbox_journal_entry - Create journal entries in NetBox

purestorage.flashblade
~~~~~~~~~~~~~~~~~~~~~~

- purestorage.flashblade.purefb_pingtrace - Employ the internal FlashBlade ping and trace mechanisms

Unchanged Collections
---------------------

- amazon.aws (still version 5.4.0)
- ansible.netcommon (still version 4.1.0)
- ansible.utils (still version 2.9.0)
- ansible.windows (still version 1.13.0)
- awx.awx (still version 21.14.0)
- azure.azcollection (still version 1.15.0)
- check_point.mgmt (still version 4.0.0)
- chocolatey.chocolatey (still version 1.4.0)
- cisco.asa (still version 4.0.0)
- cisco.iosxr (still version 4.1.0)
- cisco.ise (still version 2.5.12)
- cisco.meraki (still version 2.15.1)
- cisco.nso (still version 1.0.3)
- cisco.ucs (still version 1.8.0)
- cloud.common (still version 2.1.3)
- cloudscale_ch.cloud (still version 2.2.4)
- community.aws (still version 5.4.0)
- community.azure (still version 2.0.0)
- community.ciscosmb (still version 1.0.5)
- community.digitalocean (still version 1.23.0)
- community.docker (still version 3.4.3)
- community.fortios (still version 1.0.0)
- community.google (still version 1.0.0)
- community.grafana (still version 1.5.4)
- community.hashi_vault (still version 4.2.0)
- community.hrobot (still version 1.8.0)
- community.libvirt (still version 1.2.0)
- community.mysql (still version 3.6.0)
- community.network (still version 5.0.0)
- community.okd (still version 2.3.0)
- community.postgresql (still version 2.3.2)
- community.proxysql (still version 1.5.1)
- community.rabbitmq (still version 1.2.3)
- community.routeros (still version 2.8.0)
- community.sap (still version 1.0.0)
- community.sap_libs (still version 1.4.1)
- community.skydive (still version 1.0.0)
- community.sops (still version 1.6.1)
- community.vmware (still version 3.5.0)
- community.windows (still version 1.12.0)
- containers.podman (still version 1.10.1)
- cyberark.conjur (still version 1.2.0)
- cyberark.pas (still version 1.0.17)
- dellemc.enterprise_sonic (still version 2.0.0)
- dellemc.openmanage (still version 6.3.0)
- dellemc.os10 (still version 1.1.1)
- dellemc.os6 (still version 1.0.7)
- dellemc.os9 (still version 1.0.4)
- f5networks.f5_modules (still version 1.23.0)
- fortinet.fortimanager (still version 2.1.7)
- fortinet.fortios (still version 2.2.3)
- gluster.gluster (still version 1.0.2)
- google.cloud (still version 1.1.3)
- grafana.grafana (still version 1.1.1)
- hpe.nimble (still version 1.1.4)
- ibm.qradar (still version 2.1.0)
- ibm.spectrum_virtualize (still version 1.11.0)
- infinidat.infinibox (still version 1.3.12)
- infoblox.nios_modules (still version 1.4.1)
- inspur.ispim (still version 1.3.0)
- inspur.sm (still version 2.3.0)
- junipernetworks.junos (still version 4.1.0)
- kubernetes.core (still version 2.4.0)
- lowlydba.sqlserver (still version 1.3.1)
- mellanox.onyx (still version 1.0.0)
- netapp.aws (still version 21.7.0)
- netapp.azure (still version 21.10.0)
- netapp.cloudmanager (still version 21.22.0)
- netapp.elementsw (still version 21.7.0)
- netapp.storagegrid (still version 21.11.1)
- netapp.um_info (still version 21.8.0)
- netapp_eseries.santricity (still version 1.4.0)
- ngine_io.cloudstack (still version 2.3.0)
- ngine_io.exoscale (still version 1.0.0)
- ngine_io.vultr (still version 1.1.3)
- openstack.cloud (still version 1.10.0)
- openvswitch.openvswitch (still version 2.1.0)
- ovirt.ovirt (still version 2.4.1)
- purestorage.flasharray (still version 1.17.2)
- sensu.sensu_go (still version 1.13.2)
- splunk.es (still version 2.1.0)
- t_systems_mms.icinga_director (still version 1.32.2)
- vmware.vmware_rest (still version 2.3.1)
- vultr.cloud (still version 1.7.0)
- wti.remote (still version 1.0.4)

v7.4.0
======

.. contents::
  :local:
  :depth: 2

Release Summary
---------------

Release Date: 2023-03-28

`Porting Guide <https://docs.ansible.com/ansible/devel/porting_guides.html>`_

Ansible-core
------------

Ansible 7.4.0 contains Ansible-core version 2.14.4.
This is a newer version than version 2.14.3 contained in the previous Ansible release.

The changes are reported in the combined changelog below.

Changed Collections
-------------------

If not mentioned explicitly, the changes are reported in the combined changelog below.

+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| Collection                    | Ansible 7.3.0 | Ansible 7.4.0 | Notes                                                                                                                        |
+===============================+===============+===============+==============================================================================================================================+
| amazon.aws                    | 5.2.0         | 5.4.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| awx.awx                       | 21.12.0       | 21.14.0       | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| azure.azcollection            | 1.14.0        | 1.15.0        | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.dnac                    | 6.6.3         | 6.6.4         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.intersight              | 1.0.23        | 1.0.24        | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.ios                     | 4.3.1         | 4.4.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cloud.common                  | 2.1.2         | 2.1.3         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.aws                 | 5.2.0         | 5.4.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.crypto              | 2.11.0        | 2.11.1        |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.dns                 | 2.5.1         | 2.5.2         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.docker              | 3.4.2         | 3.4.3         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.general             | 6.4.0         | 6.5.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.hashi_vault         | 4.1.0         | 4.2.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.hrobot              | 1.7.0         | 1.8.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.routeros            | 2.7.0         | 2.8.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.sap_libs            | 1.4.0         | 1.4.1         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.vmware              | 3.4.0         | 3.5.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| f5networks.f5_modules         | 1.22.1        | 1.23.0        |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| fortinet.fortios              | 2.2.2         | 2.2.3         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| google.cloud                  | 1.1.2         | 1.1.3         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| netapp.ontap                  | 22.3.0        | 22.4.1        |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| purestorage.flasharray        | 1.17.0        | 1.17.2        |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| purestorage.fusion            | 1.3.0         | 1.4.1         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| t_systems_mms.icinga_director | 1.32.0        | 1.32.2        |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| vmware.vmware_rest            | 2.2.0         | 2.3.1         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| vyos.vyos                     | 4.0.0         | 4.0.1         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+

Major Changes
-------------

community.hrobot
~~~~~~~~~~~~~~~~

- firewall - Hetzner added output rules support to the firewall. This change unfortunately means that using old versions of the firewall module will always set the output rule list to empty, thus disallowing the server to send out packets (https://github.com/ansible-collections/community.hrobot/issues/75, https://github.com/ansible-collections/community.hrobot/pull/76).

community.vmware
~~~~~~~~~~~~~~~~

- Use true/false (lowercase) for boolean values in documentation and examples (https://github.com/ansible-collections/community.vmware/issues/1660).

fortinet.fortios
~~~~~~~~~~~~~~~~

- Add annotations of member operation for every module.
- Update ``fortios.py`` for higher performance;
- supports temporary session key and pre/post login banner;
- update the examples on how to use member operation in Q&A.

purestorage.fusion
~~~~~~~~~~~~~~~~~~

- Patching of resource properties was brought to parity with underlying Python SDK
- fusion_volume - fixed and reorganized, arguments changed

Minor Changes
-------------

Ansible-core
~~~~~~~~~~~~

- ansible-test - Moved git handling out of the validate-modules sanity test and into ansible-test.
- ansible-test - Removed the ``--keep-git`` sanity test option, which was limited to testing ansible-core itself.
- ansible-test - Updated the Azure Pipelines CI plugin to work with newer versions of git.

amazon.aws
~~~~~~~~~~

- ec2_instance - more consistently return ``instances`` information (https://github.com/ansible-collections/amazon.aws/pull/964).
- ec2_instance - remove unused import (https://github.com/ansible-collections/amazon.aws/pull/1350).
- ec2_key - Add unit-tests coverage (https://github.com/ansible-collections/amazon.aws/pull/1288).
- ec2_spot_instance - add parameter ``terminate_instances`` to support terminate instances associated with spot requests. (https://github.com/ansible-collections/amazon.aws/pull/1402).
- ec2_vpc_nat_gateway - ensure allocation_id is defined before potential access (https://github.com/ansible-collections/amazon.aws/pull/1350).
- route53_health_check -  added support for enabling Latency graphs (MeasureLatency) during creation of a Route53 Health Check. (https://github.com/ansible-collections/amazon.aws/pull/1201).
- route53_zone - added support for associating multiple VPCs to route53 hosted zones (https://github.com/ansible-collections/amazon.aws/pull/1300).
- s3_bucket - add option to support creation of buckets with object lock enabled (https://github.com/ansible-collections/amazon.aws/pull/1372).

cisco.ios
~~~~~~~~~

- ios_facts - Add ip value to ansible_net_neighbors dictionary for cdp neighbours. (https://github.com/ansible-collections/cisco.ios/pull/748)
- ios_facts - Add ip value to ansible_net_neighbors dictionary for lldp neighbours. (https://github.com/ansible-collections/cisco.ios/pull/760)
- ios_interfaces - Add mode attribute in ios_interfaces, which supports layer2 and layer3 as options.

cloud.common
~~~~~~~~~~~~

- sanity - fix sanity errors (https://github.com/ansible-collections/cloud.common/issues/106)
- units - ensure tests/units follow the Ansible-defined unit tests structure (https://github.com/ansible-collections/cloud.common/issues/89)

community.aws
~~~~~~~~~~~~~

- aws_ssm - added support for specifying the endpoint to use when connecting to the S3 API (https://github.com/ansible-collections/community.aws/pull/1619).
- aws_ssm - remove unused imports (https://github.com/ansible-collections/community.aws/pull/1707).
- aws_ssm - rework environment variable handling to use built in Ansible plugin support (https://github.com/ansible-collections/community.aws/pull/514).
- batch_job_definition - make trailing comma tuple explicitly a tuple (https://github.com/ansible-collections/community.aws/pull/1707).
- ecs_service - ``task_definition`` is now optional when ``force_new_deployment`` is ``True`` (https://github.com/ansible-collections/community.aws/pull/1680).
- ecs_service - added new parameter ``enable_execute_command`` (https://github.com/ansible-collections/community.aws/pull/488).
- ecs_service - handle SDK errors more cleanly on update failures (https://github.com/ansible-collections/community.aws/pull/488).
- ecs_service - new parameter ``purge_placement_constraints``  to have the ability to remove the placement constraints of an ECS Service (https://github.com/ansible-collections/community.aws/pull/1716).
- ecs_service - new parameter ``purge_placement_strategy`` to have the ability to remove the placement strategy of an ECS Service (https://github.com/ansible-collections/community.aws/pull/1716).
- iam_role - added ``assume_role_policy_document_raw`` to the role return values, this doesn't convert policy document contents from CamelCase to snake_case (https://github.com/ansible-collections/community.aws/issues/551).
- iam_role_info - added ``assume_role_policy_document_raw`` to the role return values, this doesn't convert policy document contents from CamelCase to snake_case (https://github.com/ansible-collections/community.aws/issues/551).
- inspector_target - minor linting fix (https://github.com/ansible-collections/community.aws/pull/1707).
- s3_lifecycle - add parameter ``noncurrent_version_keep_newer`` to set the number of newest noncurrent versions to retain (https://github.com/ansible-collections/community.aws/pull/1606).
- secretsmanager_secret - added support for region replication using the ``replica`` parameter (https://github.com/ansible-collections/community.aws/pull/827).
- secretsmanager_secret - added the ``overwrite`` parameter to support only setting the secret if it doesn't exist (https://github.com/ansible-collections/community.aws/pull/1628).
- sns - Add support for ``message_group_id`` and ``message_deduplication_id`` (https://github.com/ansible-collections/community.aws/pull/1733).
- sns_topic - add support for ``content_based_deduplication`` parameter (https://github.com/ansible-collections/community.aws/pull/1693).
- sns_topic - add support for ``tags`` and ``purge_tags`` (https://github.com/ansible-collections/community.aws/pull/972).
- sqs_queue - add support for ``deduplication_scope`` parameter (https://github.com/ansible-collections/community.aws/pull/1603).
- sqs_queue - add support for ``fifo_throughput_limit`` parameter (https://github.com/ansible-collections/community.aws/pull/1603).
- ssm_parameter - add support for tags in ssm parameters (https://github.com/ansible-collections/community.aws/issues/1573).

community.general
~~~~~~~~~~~~~~~~~

- apt_rpm - adds ``clean``, ``dist_upgrade`` and ``update_kernel``  parameters for clear caches, complete upgrade system, and upgrade kernel packages (https://github.com/ansible-collections/community.general/pull/5867).
- dconf - parse GVariants for equality comparison when the Python module ``gi.repository`` is available (https://github.com/ansible-collections/community.general/pull/6049).
- gitlab_runner - allow to register group runner (https://github.com/ansible-collections/community.general/pull/3935).
- jira - add worklog functionality (https://github.com/ansible-collections/community.general/issues/6209, https://github.com/ansible-collections/community.general/pull/6210).
- ldap modules - add ``ca_path`` option (https://github.com/ansible-collections/community.general/pull/6185).
- make - add ``command`` return value to the module output (https://github.com/ansible-collections/community.general/pull/6160).
- nmap inventory plugin - add new option ``open`` for only returning open ports (https://github.com/ansible-collections/community.general/pull/6200).
- nmap inventory plugin - add new option ``port`` for port specific scan (https://github.com/ansible-collections/community.general/pull/6165).
- nmcli - add ``default`` and ``default-or-eui64`` to the list of valid choices for ``addr_gen_mode6`` parameter (https://github.com/ansible-collections/community.general/pull/5974).
- nmcli - add support for ``team.runner-fast-rate`` parameter for ``team`` connections (https://github.com/ansible-collections/community.general/issues/6065).
- openbsd_pkg - set ``TERM`` to ``'dumb'`` in ``execute_command()`` to make module less dependant on the ``TERM`` environment variable set on the Ansible controller (https://github.com/ansible-collections/community.general/pull/6149).
- pipx - optional ``install_apps`` parameter added to install applications from injected packages (https://github.com/ansible-collections/community.general/pull/6198).
- proxmox_kvm - add new ``archive`` parameter. This is needed to create a VM from an archive (backup) (https://github.com/ansible-collections/community.general/pull/6159).
- redfish_info - adds commands to retrieve the HPE ThermalConfiguration and FanPercentMinimum settings from iLO (https://github.com/ansible-collections/community.general/pull/6208).
- redhat_subscription - credentials (``username``, ``activationkey``, and so on) are required now only if a system needs to be registered, or ``force_register`` is specified (https://github.com/ansible-collections/community.general/pull/5664).
- redhat_subscription - the registration is done using the D-Bus ``rhsm`` service instead of spawning a ``subscription-manager register`` command, if possible; this avoids passing plain-text credentials as arguments to ``subscription-manager register``, which can be seen while that command runs (https://github.com/ansible-collections/community.general/pull/6122).
- ssh_config - add ``proxyjump`` option (https://github.com/ansible-collections/community.general/pull/5970).
- ssh_config - vendored StormSSH's config parser to avoid having to install StormSSH to use the module (https://github.com/ansible-collections/community.general/pull/6117).
- znode module - optional ``use_tls`` parameter added for encrypted communication (https://github.com/ansible-collections/community.general/issues/6154).

community.hrobot
~~~~~~~~~~~~~~~~

- firewall, firewall_info - add ``filter_ipv6`` and ``rules.output`` output to support the new IPv6 filtering and output rules features (https://github.com/ansible-collections/community.hrobot/issues/75, https://github.com/ansible-collections/community.hrobot/pull/76).
- firewall, firewall_info - add ``server_number`` option that can be used instead of ``server_ip`` to identify the server. Hetzner deprecated configuring the firewall by ``server_ip``, so using ``server_ip`` will stop at some point in the future (https://github.com/ansible-collections/community.hrobot/pull/77).

community.routeros
~~~~~~~~~~~~~~~~~~

- api_modify - adapt data for API paths ``ip dhcp-server network`` (https://github.com/ansible-collections/community.routeros/pull/156).
- api_modify - add support for API path ``snmp community`` (https://github.com/ansible-collections/community.routeros/pull/159).
- api_modify - add support for ``trap-interfaces`` in API path ``snmp`` (https://github.com/ansible-collections/community.routeros/pull/159).
- api_modify - add support to disable IPv6 in API paths ``ipv6 settings`` (https://github.com/ansible-collections/community.routeros/pull/158).
- api_modify - support API paths ``ip firewall layer7-protocol`` (https://github.com/ansible-collections/community.routeros/pull/153).
- command - workaround for extra characters in stdout in RouterOS versions between 6.49 and 7.1.5 (https://github.com/ansible-collections/community.routeros/issues/62, https://github.com/ansible-collections/community.routeros/pull/161).

community.vmware
~~~~~~~~~~~~~~~~

- vmware_migrate_vmk - Improve error handling (https://github.com/ansible-collections/community.vmware/issues/1118).
- vmware_tag - Allow to use category names for tag management (https://github.com/ansible-collections/community.vmware/issues/1614).
- vmware_tag_manager - Improve performance of tag attachments and detachments (https://github.com/ansible-collections/community.vmware/issues/1603).
- vmware_tools - ansible_vmware_guest_uuid added for easier use of vmware_tools connection plugin with vmware_vm_inventory plugin
- vmware_vm_info - Add several parameters to skip discovering some information (https://github.com/ansible-collections/community.vmware/issues/1682)

f5networks.f5_modules
~~~~~~~~~~~~~~~~~~~~~

- bigip_firewall_rule - the source and destination items can be set to `any` and port type is changed from int to str
- bigip_policy_rule - added host_contains parameter to http_host condition type
- bigip_sys_global - added gui_audit parameter to control audit log for changes through webui

netapp.ontap
~~~~~~~~~~~~

- na_ontap_rest_cli - returns changed only for verbs POST, PATCH and DELETE.
- na_ontap_security_config - Added support for protocol version ``TLSV1.3``.
- na_ontap_security_config - Replaced private cli with REST API for GET and PATCH.
- na_ontap_security_config - new option ``supported_cipher_suites`` added in REST.
- na_ontap_snapmirror - new option ``identity_preservation`` added in REST.
- na_ontap_snapmirror - wait 600 seconds for snapmirror creation to complete in REST.
- na_ontap_user_role - ``command_directory_name`` requires 9.11.1 or later with REST.
- na_ontap_user_role - add support for rest-role ``privileges.access`` choices ``read_create``, ``read_modify`` and ``read_create_modify``, supported only with REST and requires ONTAP 9.11.1 or later versions.

purestorage.fusion
~~~~~~~~~~~~~~~~~~

- errors_py - added opt-in global exception handler which produces simpler and cleaner messages on REST errors
- removed dependency on Python `netaddr` package

vmware.vmware_rest
~~~~~~~~~~~~~~~~~~

- set version in galaxy.yml to allow install from git repo

Breaking Changes / Porting Guide
--------------------------------

Ansible-core
~~~~~~~~~~~~

- ansible-test - Integration tests which depend on specific file permissions when running in an ansible-test managed host environment may require changes. Tests that require permissions other than ``755`` or ``644`` may need to be updated to set the necessary permissions as part of the test run.

Deprecated Features
-------------------

amazon.aws
~~~~~~~~~~

- support for passing both profile and security tokens through a mix of environment variables and parameters has been deprecated and support will be removed in release 6.0.0. After release 6.0.0 it will only be possible to pass either a profile or security tokens, regardless of mechanism used to pass them.  To explicitly block a parameter coming from an environment variable pass an empty string as the parameter value.  Support for passing profile and security tokens together was originally deprecated in release 1.2.0, however only partially implemented in release 5.0.0 (https://github.com/ansible-collections/amazon.aws/pull/1355).

community.aws
~~~~~~~~~~~~~

- ecs_service -  In a release after 2024-06-01, tha default value of ``purge_placement_constraints`` will be change from ``false`` to ``true`` (https://github.com/ansible-collections/community.aws/pull/1716).
- ecs_service -  In a release after 2024-06-01, tha default value of ``purge_placement_strategy`` will be change from ``false`` to ``true`` (https://github.com/ansible-collections/community.aws/pull/1716).
- iam_role - All top level return values other than ``iam_role`` and ``changed`` have been deprecated and will be removed in a release after 2023-12-01 (https://github.com/ansible-collections/community.aws/issues/551).
- iam_role - In a release after 2023-12-01 the contents of ``assume_role_policy_document`` will no longer be converted from CamelCase to snake_case.  The ``assume_role_policy_document_raw`` return value already returns the policy document in this future format (https://github.com/ansible-collections/community.aws/issues/551).
- iam_role_info - In a release after 2023-12-01 the contents of ``assume_role_policy_document`` will no longer be converted from CamelCase to snake_case.  The ``assume_role_policy_document_raw`` return value already returns the policy document in this future format (https://github.com/ansible-collections/community.aws/issues/551).

community.hashi_vault
~~~~~~~~~~~~~~~~~~~~~

- hashi_vault lookup - in ``v5.0.0`` duplicate term string options will raise an exception instead of showing a warning (https://github.com/ansible-collections/community.hashi_vault/issues/356).

purestorage.fusion
~~~~~~~~~~~~~~~~~~

- fusion_hw - hardware module is being removed as changing hardware type has never been supported by Pure Storage Fusion
- fusion_info - nigs subset is deprecated in favor of network_interface_groups and will be removed in the version 1.7.0
- fusion_info - placements subset is deprecated in favor of placement_groups and will be removed in the version 1.7.0
- fusion_pg - placement_engine option is deprecated because Fusion API does not longer support this parameter It will be removed in the version 2.0.0
- fusion_se - parameters 'addresses', 'gateway' and 'network_interface_groups' are deprecated in favor of 'iscsi' and will be removed in version 2.0.0
- fusion_tn - tenant networks are being replaced by storage endpoints ```fusion_se``` and Network Interface Groups ```fusion_nig```

Bugfixes
--------

Ansible-core
~~~~~~~~~~~~

- Fix ``MANIFEST.in`` to exclude unwanted files in the ``packaging/`` directory.
- Fix ``MANIFEST.in`` to include ``*.md`` files in the ``test/support/`` directory.
- Fix an issue where the value of ``become`` was ignored when used on a role used as a dependency in ``main/meta.yml`` (https://github.com/ansible/ansible/issues/79777)
- ``ansible_eval_concat`` - avoid redundant unsafe wrapping of templated strings converted to Python types
- ansible-galaxy role info - fix unhandled AttributeError by catching the correct exception.
- ansible-test - Always indicate the Python version being used before installing requirements. Resolves issue https://github.com/ansible/ansible/issues/72855
- ansible-test - Exclude ansible-core vendored Python packages from ansible-test payloads.
- ansible-test - Integration test target prefixes defined in a ``tests/integration/target-prefixes.{group}`` file can now contain an underscore (``_``) character. Resolves issue https://github.com/ansible/ansible/issues/79225
- ansible-test - Removed pointless comparison in diff evaluation logic.
- ansible-test - Set ``PYLINTHOME`` for the ``pylint`` sanity test to prevent failures due to ``pylint`` checking for the existence of an obsolete home directory.
- ansible-test - Support loading of vendored Python packages from ansible-core.
- ansible-test - Use consistent file permissions when delegating tests to a container or remote host. Files with any execute bit set will use permissions ``755``. All other files will use permissions ``644``. (Resolves issue https://github.com/ansible/ansible/issues/75079)
- copy - fix creating the dest directory in check mode with remote_src=True (https://github.com/ansible/ansible/issues/78611).
- copy - fix reporting changes to file attributes in check mode with remote_src=True (https://github.com/ansible/ansible/issues/77957).

amazon.aws
~~~~~~~~~~

- cloudtrail - support to disabling encryption using ``kms_key_id`` (https://github.com/ansible-collections/amazon.aws/pull/1384).
- ec2_key - fix issue when trying to update existing key pair with the same key material (https://github.com/ansible-collections/amazon.aws/pull/1383).
- ec2_metadata_facts - fix ``AttributeError`` when running the ec2_metadata_facts module on Python 2 managed nodes (https://github.com/ansible-collections/amazon.aws/issues/1358).
- ec2_vol - handle ec2_vol.tags when the associated instance already exists (https://github.com/ansible-collections/amazon.aws/pull/1071).
- module_utils/elbv2 - fix change detection by adding default values for ``Scope`` and ``SessionTimeout`` parameters in ``authenticate-oidc`` rules (https://github.com/ansible-collections/amazon.aws/pull/1270).
- module_utils/elbv2 - respect ``UseExistingClientSecret`` parameter in ``authenticate-oidc`` rules (https://github.com/ansible-collections/amazon.aws/pull/1270).
- rds_instance - Fixed ``TypeError`` when tagging RDS DB with storage type ``gp3`` (https://github.com/ansible-collections/amazon.aws/pull/1437).
- revert breaking change introduced in 5.2.0 when passing credentials through a mix of environment variables and parameters (https://github.com/ansible-collections/amazon.aws/issues/1353).
- route53_info - Add new return key ``health_check_observations`` for health check operations (https://github.com/ansible-collections/amazon.aws/pull/1419).
- route53_info - Fixed ``Key Error`` when getting status or failure_reason of a health check (https://github.com/ansible-collections/amazon.aws/pull/1419).
- s3_bucket - empty bucket policy was throwing a JSONDecodeError - deal with it gracefully instead (https://github.com/ansible-collections/amazon.aws/pull/1368)

cisco.dnac
~~~~~~~~~~

- A new method to compare changes for specific cases has been added.
- network_device - Used a new method to compare changes.

cisco.ios
~~~~~~~~~

- ios_acls - fix rendering of object-groups in source and destination at ace level.
- ios_bgp_address_family - fix facts generation of default originate option.
- ios_bgp_global - fix neighbor shutdown command on set value being false.
- ios_command - Run & evaluate commands at least once even when retries is set to 0 (https://github.com/ansible-collections/cisco.nxos/issues/607).
- ios_ospf_interfaces - fix dead-interval rendering wrong facts when hello-multiplier is configured.

cloud.common
~~~~~~~~~~~~

- module_utils/turbo/server - import needed library into the right place (https://github.com/ansible-collections/cloud.common/pull/120)

community.aws
~~~~~~~~~~~~~

- aws_ssm - fix copying empty file with older curl versions (https://github.com/ansible-collections/community.aws/issues/1686).
- eks_cluster - adding tags to eks cluster creation (https://github.com/ansible-collections/community.aws/pull/1591).
- sns_topic - avoid fetching attributes from subscribers when not setting them, this can cause permissions issues (https://github.com/ansible-collections/community.aws/pull/1418).

community.dns
~~~~~~~~~~~~~

- Update Public Suffix List.

community.general
~~~~~~~~~~~~~~~~~

- archive - avoid deprecated exception class on Python 3 (https://github.com/ansible-collections/community.general/pull/6180).
- gitlab_runner - fix ``KeyError`` on runner creation and update (https://github.com/ansible-collections/community.general/issues/6112).
- influxdb_user - fix running in check mode when the user does not exist yet (https://github.com/ansible-collections/community.general/pull/6111).
- interfaces_file - fix reading options in lines not starting with a space (https://github.com/ansible-collections/community.general/issues/6120).
- jail connection plugin - add ``inventory_hostname`` to vars under ``remote_addr``. This is needed for compatibility with ansible-core 2.13 (https://github.com/ansible-collections/community.general/pull/6118).
- memset - fix memset urlerror handling (https://github.com/ansible-collections/community.general/pull/6114).
- nmcli - fixed idempotency issue for bridge connections. Module forced default value of ``bridge.priority`` to nmcli if not set; if ``bridge.stp`` is disabled nmcli ignores it and keep default (https://github.com/ansible-collections/community.general/issues/3216, https://github.com/ansible-collections/community.general/issues/4683).
- nmcli - fixed idempotency issue when module params is set to ``may_fail4=false`` and ``method4=disabled``; in this case nmcli ignores change and keeps their own default value ``yes`` (https://github.com/ansible-collections/community.general/pull/6106).
- nmcli - implemented changing mtu value on vlan interfaces (https://github.com/ansible-collections/community.general/issues/4387).
- opkg - fixes bug when using ``update_cache=true`` (https://github.com/ansible-collections/community.general/issues/6004).
- redhat_subscription, rhsm_release, rhsm_repository - cleanly fail when not running as root, rather than hanging on an interactive ``console-helper`` prompt; they all interact with ``subscription-manager``, which already requires to be run as root (https://github.com/ansible-collections/community.general/issues/734, https://github.com/ansible-collections/community.general/pull/6211).
- xenorchestra inventory plugin - fix failure to receive objects from server due to not checking the id of the response (https://github.com/ansible-collections/community.general/pull/6227).
- yarn - fix ``global=true`` to not fail when `executable` wasn't specified (https://github.com/ansible-collections/community.general/pull/6132)
- yarn - fixes bug where yarn module tasks would fail when warnings were emitted from Yarn. The ``yarn.list`` method was not filtering out warnings (https://github.com/ansible-collections/community.general/issues/6127).

community.hashi_vault
~~~~~~~~~~~~~~~~~~~~~

- hashi_vault lookup - a term string with duplicate options would silently use the last value. The lookup now shows a warning on option duplication (https://github.com/ansible-collections/community.hashi_vault/issues/349).

community.routeros
~~~~~~~~~~~~~~~~~~

- api_info, api_modify - fix default and remove behavior for ``dhcp-options`` in path ``ip dhcp-client`` (https://github.com/ansible-collections/community.routeros/issues/148, https://github.com/ansible-collections/community.routeros/pull/154).
- api_modify - fix handling of disabled keys on creation (https://github.com/ansible-collections/community.routeros/pull/154).
- various plugins and modules - remove unnecessary imports (https://github.com/ansible-collections/community.routeros/pull/149).

community.sap_libs
~~~~~~~~~~~~~~~~~~

- fixes failures in sanity test for plugins/modules/sap_pyrfc.py
- fixes failures in sanity test for tests/unit/compat/builtins.py
- fixes failures in sanity test for tests/unit/plugins/modules/test_sap_system_facts.py
- fixes pipeline warnings
- sapcontrol_exec - This pr fixes problems on c(StartSystem), c(StopSystem), c(RestartSystem) which needs parameters they ca not provided by the parameters argument because of special format like c(waittimeout=1) without string quotes. This is caused by the suds module itself.

community.vmware
~~~~~~~~~~~~~~~~

- vmware_cross_vc_clone - Fix SSL Thumbprint validation to ignore if destination_vcenter_validate_certs is false (https://github.com/ansible-collections/community.vmware/issues/1433).
- vmware_guest - Fixes adding new NVDIMM device issue by connecting to ESXi host (https://github.com/ansible-collections/community.vmware/issues/1644).
- vmware_guest_cross_vc_clone - Fix vim.fault.NotAuthenticated issue (https://github.com/ansible-collections/community.vmware/issues/1223).
- vmware_guest_cross_vc_clone - New parameter timeout in order to allow clone running longer than 1 hour
- vmware_tag - Fix a performance issue during tag processing (https://github.com/ansible-collections/community.vmware/issues/1603).

f5networks.f5_modules
~~~~~~~~~~~~~~~~~~~~~

- bigip_device_info - Included additional attributes for actions in ltm policy rules
- bigip_ucs_fetch - fix a typo causing a bug that prevented ucs file from being encrypted with the provided passphrase

fortinet.fortios
~~~~~~~~~~~~~~~~

- Fix the issue that all the params with underscore cannot be set under member operation;
- Fix the login issue (#232);
- Fix the output path issue (#227);

google.cloud
~~~~~~~~~~~~

- gcp_compute_instance_info: fix incorrect documentation for filter which incorrectly pointed to the gcloud filter logic rather than the API (fixes #549)

netapp.ontap
~~~~~~~~~~~~

- na_ontap_interface - fix incorrect warning raised when try to rename interface.
- na_ontap_ldap_client - fix KeyError on ``name`` in ZAPI.
- na_ontap_ldap_client - fix duplicate entry error when used cluster vserver in REST.
- na_ontap_san_create - Role documentation correct to from nas to san
- na_ontap_snapmirror - fix invalid value error for return_timeout, modified the value to 120 seconds.
- na_ontap_user - fix KeyError vserver in ZAPI.
- na_ontap_user_role - report error when command/command directory path set in REST for ONTAP earlier versions.
- na_ontap_volume - fix error when try to unmount volume and modify snaplock attribute.
- na_ontap_volume - fix idempotent issue when try to offline and modify other volume options.
- na_ontap_vserver_audit - Added ``log_path`` option in modify.
- na_ontap_vserver_audit - fix invalid field value error of log retention count and duration.

purestorage.flasharray
~~~~~~~~~~~~~~~~~~~~~~

- purefa_info - Fix REST response backwards compatibility issue for array capacity REST response
- purefa_info - Resolves issue in AC environment where REST v2 host list mismatches REST v1 due to remote hosts.
- purefa_info - Resolves issue with destroyed pgroup snapshot on an offload target not have a time remaining value
- purefa_pg - Resolves issue with destroyed pgroup snapshot on an offload target not have a time remaining value

purestorage.fusion
~~~~~~~~~~~~~~~~~~

- fusion_api_client - error messages now mostly handled by errors_py
- fusion_hap - could not delete host access policy without iqn option. Now it needs only name option for deletion
- fusion_hap - error messages now mostly handled by errors_py
- fusion_hap - uppercase names were not supported. Now uppercase names are allowed
- fusion_info - fixes typo in output 'appiiances' -> 'appliances'
- fusion_info - network_interface_groups subset returned nothing. Now it collects the same information as nigs subset
- fusion_info - placements subset returned nothing. Now it collects the same information as placement_groups subset
- fusion_nig - add missing 'availability_zone' format param in error message
- fusion_nig - error messages now mostly handled by errors_py
- fusion_pg - create_pg always broke runtime. Now it executes and creates placement group successfully
- fusion_pg - error messages now mostly handled by errors_py
- fusion_pp - error messages now mostly handled by errors_py
- fusion_pp - fix call to parse_minutes where we were missing a required argument
- fusion_sc - error messages now mostly handled by errors_py
- fusion_se - add missing 'availability_zone' format param in error message
- fusion_se - error messages now mostly handled by errors_py
- fusion_se - fix call in get_nifg where provider_subnet was used instead of network_interface_group_name
- fusion_ss - error messages now mostly handled by errors_py
- fusion_tenant - error messages now mostly handled by errors_py
- fusion_ts - add missing 'tenant' format param in error message
- fusion_ts - error messages now mostly handled by errors_py
- fusion_volume - error messages now mostly handled by errors_py

vmware.vmware_rest
~~~~~~~~~~~~~~~~~~

- Allow filters with the space (See: https://github.com/ansible-collections/vmware.vmware_rest/issues/362).
- Handle spaces and special characters in resource names for lookup plugins (See: https://github.com/ansible-collections/vmware.vmware_rest/issues/356).

vyos.vyos
~~~~~~~~~

- vyos_command - Run commands at least once even when retries is set to 0 (https://github.com/ansible-collections/cisco.nxos/issues/607).

New Plugins
-----------

Lookup
~~~~~~

- community.general.merge_variables - merge variables with a certain suffix

New Modules
-----------

community.aws
~~~~~~~~~~~~~

- community.aws.eks_nodegroup - Manage EKS Nodegroup module

community.general
~~~~~~~~~~~~~~~~~

- community.general.kdeconfig - Manage KDE configuration files

community.hashi_vault
~~~~~~~~~~~~~~~~~~~~~

- community.hashi_vault.vault_kv2_write - Perform a write operation against a KVv2 secret in HashiCorp Vault

community.vmware
~~~~~~~~~~~~~~~~

- community.vmware.vmware_vsan_hcl_db - Manages the vSAN Hardware Compatibility List (HCL) database

netapp.ontap
~~~~~~~~~~~~

- netapp.ontap.na_ontap_ems_filter - NetApp ONTAP EMS Filter

vmware.vmware_rest
~~~~~~~~~~~~~~~~~~

- vmware.vmware_rest.vcenter_vm_guest_customization - Applies a customization specification on the virtual machine
- vmware.vmware_rest.vcenter_vm_guest_power - Issues a request to the guest operating system asking it to perform a soft shutdown, standby (suspend) or soft reboot
- vmware.vmware_rest.vcenter_vm_guest_power_info - Returns information about the guest operating system power state.
- vmware.vmware_rest.vcenter_vm_storage_policy_compliance - Returns the storage policy Compliance {@link Info} of a virtual machine after explicitly re-computing compliance check.
- vmware.vmware_rest.vcenter_vm_tools_installer - Connects the VMware Tools CD installer as a CD-ROM for the guest operating system
- vmware.vmware_rest.vcenter_vm_tools_installer_info - Get information about the VMware Tools installer.

Unchanged Collections
---------------------

- ansible.netcommon (still version 4.1.0)
- ansible.posix (still version 1.5.1)
- ansible.utils (still version 2.9.0)
- ansible.windows (still version 1.13.0)
- arista.eos (still version 6.0.0)
- check_point.mgmt (still version 4.0.0)
- chocolatey.chocolatey (still version 1.4.0)
- cisco.aci (still version 2.4.0)
- cisco.asa (still version 4.0.0)
- cisco.iosxr (still version 4.1.0)
- cisco.ise (still version 2.5.12)
- cisco.meraki (still version 2.15.1)
- cisco.mso (still version 2.2.1)
- cisco.nso (still version 1.0.3)
- cisco.nxos (still version 4.1.0)
- cisco.ucs (still version 1.8.0)
- cloudscale_ch.cloud (still version 2.2.4)
- community.azure (still version 2.0.0)
- community.ciscosmb (still version 1.0.5)
- community.digitalocean (still version 1.23.0)
- community.fortios (still version 1.0.0)
- community.google (still version 1.0.0)
- community.grafana (still version 1.5.4)
- community.libvirt (still version 1.2.0)
- community.mongodb (still version 1.5.1)
- community.mysql (still version 3.6.0)
- community.network (still version 5.0.0)
- community.okd (still version 2.3.0)
- community.postgresql (still version 2.3.2)
- community.proxysql (still version 1.5.1)
- community.rabbitmq (still version 1.2.3)
- community.sap (still version 1.0.0)
- community.skydive (still version 1.0.0)
- community.sops (still version 1.6.1)
- community.windows (still version 1.12.0)
- community.zabbix (still version 1.9.2)
- containers.podman (still version 1.10.1)
- cyberark.conjur (still version 1.2.0)
- cyberark.pas (still version 1.0.17)
- dellemc.enterprise_sonic (still version 2.0.0)
- dellemc.openmanage (still version 6.3.0)
- dellemc.os10 (still version 1.1.1)
- dellemc.os6 (still version 1.0.7)
- dellemc.os9 (still version 1.0.4)
- dellemc.powerflex (still version 1.5.0)
- dellemc.unity (still version 1.5.0)
- fortinet.fortimanager (still version 2.1.7)
- frr.frr (still version 2.0.0)
- gluster.gluster (still version 1.0.2)
- grafana.grafana (still version 1.1.1)
- hetzner.hcloud (still version 1.10.0)
- hpe.nimble (still version 1.1.4)
- ibm.qradar (still version 2.1.0)
- ibm.spectrum_virtualize (still version 1.11.0)
- infinidat.infinibox (still version 1.3.12)
- infoblox.nios_modules (still version 1.4.1)
- inspur.ispim (still version 1.3.0)
- inspur.sm (still version 2.3.0)
- junipernetworks.junos (still version 4.1.0)
- kubernetes.core (still version 2.4.0)
- lowlydba.sqlserver (still version 1.3.1)
- mellanox.onyx (still version 1.0.0)
- netapp.aws (still version 21.7.0)
- netapp.azure (still version 21.10.0)
- netapp.cloudmanager (still version 21.22.0)
- netapp.elementsw (still version 21.7.0)
- netapp.storagegrid (still version 21.11.1)
- netapp.um_info (still version 21.8.0)
- netapp_eseries.santricity (still version 1.4.0)
- netbox.netbox (still version 3.11.0)
- ngine_io.cloudstack (still version 2.3.0)
- ngine_io.exoscale (still version 1.0.0)
- ngine_io.vultr (still version 1.1.3)
- openstack.cloud (still version 1.10.0)
- openvswitch.openvswitch (still version 2.1.0)
- ovirt.ovirt (still version 2.4.1)
- purestorage.flashblade (still version 1.10.0)
- sensu.sensu_go (still version 1.13.2)
- splunk.es (still version 2.1.0)
- theforeman.foreman (still version 3.9.0)
- vultr.cloud (still version 1.7.0)
- wti.remote (still version 1.0.4)

v7.3.0
======

.. contents::
  :local:
  :depth: 2

Release Summary
---------------

Release Date: 2023-02-28

`Porting Guide <https://docs.ansible.com/ansible/devel/porting_guides.html>`_

Ansible-core
------------

Ansible 7.3.0 contains Ansible-core version 2.14.3.
This is a newer version than version 2.14.2 contained in the previous Ansible release.

The changes are reported in the combined changelog below.

Changed Collections
-------------------

If not mentioned explicitly, the changes are reported in the combined changelog below.

+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| Collection             | Ansible 7.2.0 | Ansible 7.3.0 | Notes                                                                                                                        |
+========================+===============+===============+==============================================================================================================================+
| awx.awx                | 21.11.0       | 21.12.0       | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.aci              | 2.3.0         | 2.4.0         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.meraki           | 2.15.0        | 2.15.1        |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.nxos             | 4.0.1         | 4.1.0         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.crypto       | 2.10.0        | 2.11.0        |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.dns          | 2.5.0         | 2.5.1         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.docker       | 3.4.0         | 3.4.2         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.general      | 6.3.0         | 6.4.0         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.grafana      | 1.5.3         | 1.5.4         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.mongodb      | 1.4.2         | 1.5.1         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.mysql        | 3.5.1         | 3.6.0         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.okd          | 2.2.0         | 2.3.0         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.sops         | 1.6.0         | 1.6.1         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.vmware       | 3.3.0         | 3.4.0         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.zabbix       | 1.9.1         | 1.9.2         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| f5networks.f5_modules  | 1.22.0        | 1.22.1        |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| grafana.grafana        | 1.1.0         | 1.1.1         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| hetzner.hcloud         | 1.9.1         | 1.10.0        |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| inspur.ispim           | 1.2.0         | 1.3.0         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| kubernetes.core        | 2.3.2         | 2.4.0         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| netapp.ontap           | 22.2.0        | 22.3.0        |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| netbox.netbox          | 3.10.0        | 3.11.0        |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| purestorage.flasharray | 1.16.2        | 1.17.0        |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| theforeman.foreman     | 3.8.0         | 3.9.0         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+

Major Changes
-------------

kubernetes.core
~~~~~~~~~~~~~~~

- refactor K8sAnsibleMixin into module_utils/k8s/ (https://github.com/ansible-collections/kubernetes.core/pull/481).

Minor Changes
-------------

Ansible-core
~~~~~~~~~~~~

- Make using blocks as handlers a parser error (https://github.com/ansible/ansible/issues/79968)
- ansible-test - Specify the configuration file location required by test plugins when the config file is not found. This resolves issue: https://github.com/ansible/ansible/issues/79411
- ansible-test - Update error handling code to use Python 3.x constructs, avoiding direct use of ``errno``.
- ansible-test acme test container - update version to update used Pebble version, underlying Python and Go base containers, and Python requirements (https://github.com/ansible/ansible/pull/79783).

cisco.aci
~~~~~~~~~

- Add Node Profile BGP Peer and Route Control Profile functionalities to aci_l3out_bgp_peer module (#340)
- Add SVI auto state support (auto_state attribute) to aci_l3out_interface (#348)
- Add aci_aaa_domain, aci_aaa_role and aci_custom_privilege modules (#226)
- Add aci_fabric_pod_policy_group module (#230)
- Add aci_interface_policy_leaf_profile_fex_policy_group module and add FEX support to aci_access_port_to_interface_policy_leaf_profile (#233)
- Add aci_tenant_span_src_group_src module (#344)
- Add action_groups for module_defaults (#316)
- Add support for filter direction in aci_contract_subject and aci_contract_subject_to_filter (#306)
- Update modules to assign roles and permissions to a user (#225)

cisco.nxos
~~~~~~~~~~

- `nxos_acls` - Support ICMPv6 option. Please refer to module doc for all new options (https://github.com/ansible-collections/cisco.nxos/issues/624).
- `nxos_facts` - Update facts gathering logic to ensure that `gather_network_resources: all` does not fail for NX-OS on MDS switches.
- `nxos_l2_interfaces` - Add new mode dot1q-tunnel (https://github.com/ansible-collections/cisco.nxos/issues/600).

community.crypto
~~~~~~~~~~~~~~~~

- get_certificate - adds ``ciphers`` option for custom cipher selection (https://github.com/ansible-collections/community.crypto/pull/571).

community.general
~~~~~~~~~~~~~~~~~

- dnsimple - set custom User-Agent for API requests to DNSimple (https://github.com/ansible-collections/community.general/pull/5927).
- flatpak_remote - add new boolean option ``enabled``. It controls, whether the remote is enabled or not (https://github.com/ansible-collections/community.general/pull/5926).
- gitlab_project - add ``releases_access_level``, ``environments_access_level``, ``feature_flags_access_level``, ``infrastructure_access_level``, ``monitor_access_level``, and ``security_and_compliance_access_level`` options (https://github.com/ansible-collections/community.general/pull/5986).
- jc filter plugin - added the ability to use parser plugins (https://github.com/ansible-collections/community.general/pull/6043).
- keycloak_group - add new optional module parameter ``parents`` to properly handle keycloak subgroups (https://github.com/ansible-collections/community.general/pull/5814).
- keycloak_user_federation - make ``org.keycloak.storage.ldap.mappers.LDAPStorageMapper`` the default value for mappers ``providerType`` (https://github.com/ansible-collections/community.general/pull/5863).
- ldap modules - add ``xorder_discovery`` option (https://github.com/ansible-collections/community.general/issues/6045, https://github.com/ansible-collections/community.general/pull/6109).
- lxd_container - add diff and check mode (https://github.com/ansible-collections/community.general/pull/5866).
- mattermost, rocketchat, slack - replace missing default favicon with docs.ansible.com favicon (https://github.com/ansible-collections/community.general/pull/5928).
- modprobe - add ``persistent`` option (https://github.com/ansible-collections/community.general/issues/4028, https://github.com/ansible-collections/community.general/pull/542).
- osx_defaults - include stderr in error messages (https://github.com/ansible-collections/community.general/pull/6011).
- proxmox - suppress urllib3 ``InsecureRequestWarnings`` when ``validate_certs`` option is ``false`` (https://github.com/ansible-collections/community.general/pull/5931).
- redfish_command - adding ``EnableSecureBoot`` functionality (https://github.com/ansible-collections/community.general/pull/5899).
- redfish_command - adding ``VerifyBiosAttributes`` functionality (https://github.com/ansible-collections/community.general/pull/5900).
- sefcontext - add support for path substitutions (https://github.com/ansible-collections/community.general/issues/1193).

community.grafana
~~~~~~~~~~~~~~~~~

- able to set `uid` for datasources in grafana via module grafana_datasource

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

- mysql_info - add ``connector_name`` and ``connector_version`` to returned values (https://github.com/ansible-collections/community.mysql/pull/497).
- mysql_role - enable auto_commit to avoid MySQL metadata table lock (https://github.com/ansible-collections/community.mysql/issues/479).
- mysql_user - add plugin_auth_string as optional parameter to use a specific pam service if pam/auth_pam plugin is used (https://github.com/ansible-collections/community.mysql/pull/445).
- mysql_user - add the ``session_vars`` argument to set session variables at the beginning of module execution (https://github.com/ansible-collections/community.mysql/issues/478).
- mysql_user - display a more informative invalid privilege exception. Changes the exception handling of the granting permission logic to show the query executed , params and the exception message granting privileges fails` (https://github.com/ansible-collections/community.mysql/issues/465).
- mysql_user - enable auto_commit to avoid MySQL metadata table lock (https://github.com/ansible-collections/community.mysql/issues/479).
- setup_mysql - update MySQL tarball URL (https://github.com/ansible-collections/community.mysql/pull/491).

community.vmware
~~~~~~~~~~~~~~~~

- vmware_guest_disk - Add support for IDE disk add, remove or reconfigure, and change to gather same VM disk info as in vmware_guest_disk_info (https://github.com/ansible-collections/community.vmware/issues/1428).
- vmware_guest_disk - Extend return value documentation for vmware_guest_disk (https://github.com/ansible-collections/community.vmware/pull/1641)
- vmware_guest_disk_info - Move gather VM disk info function to vm_device_helper.py (https://github.com/ansible-collections/community.vmware/issues/1617)
- vmware_vmotion - New parameter timeout in order to allow vmotions running longer than 1 hour (https://github.com/ansible-collections/community.vmware/pulls/1629).

grafana.grafana
~~~~~~~~~~~~~~~

- Updated the return message in grafana.grafana.folder module

hetzner.hcloud
~~~~~~~~~~~~~~

- hcloud_server - add private_networks_info containing name and private ip in responses
- hcloud_server_info - add private_networks_info containing name and private ip in responses
- inventory plugin - Add list of all private networks to server variables.
- inventory plugin - Add new connect_with setting public_ipv6 to connect to discovered servers via public IPv6 address.
- inventory plugin - Add public IPv6 address to server variables.
- inventory plugin - Log warning instead of crashing when some servers do not work with global connect_with setting.

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

netapp.ontap
~~~~~~~~~~~~

- na_ontap_aggregate - new option ``allow_flexgroups`` added.
- na_ontap_cifs - new options ``access_based_enumeration``, ``change_notify``, ``encryption``, ``home_directory``, ``oplocks``, ``show_snapshot``, ``allow_unencrypted_access``, ``namespace_caching`` and ``continuously_available`` added in REST.
- na_ontap_dns - ``skip_validation`` option requires 9.9.1 or later with REST and ignored for cluster DNS operations.
- na_ontap_dns - support cluster scope for modify and delete.
- na_ontap_interface - do not attempt to migrate FC interface if desired ``home_port``, ``home_node`` and ``current_port``, ``current_node`` are same.
- na_ontap_license - support for NLF v2 license files.
- na_ontap_nfs - new options ``root``, ``windows`` and ``security`` added in REST.
- na_ontap_user_role - ``command_directory_name`` is required if ``privileges`` not set in REST.
- na_ontap_user_role - ``path`` is required if ``privileges`` set in REST.
- na_ontap_volume_efficiency - REST support for ``policy`` requires 9.7 or later, ``path`` requires 9.9.1 or later and ``volume_efficiency`` and ``start_ve_scan_old_data`` requires 9.11.1 or later.
- na_ontap_volume_efficiency - ``schedule``, ``start_ve_scan_all``, ``start_ve_build_metadata``, ``start_ve_delete_checkpoint``, ``start_ve_queue_operation``, ``start_ve_qos_policy`` and ``stop_ve_all_operations`` options are not supported with REST.
- na_ontap_volume_efficiency - new option ``volume_name`` added.
- na_ontap_volume_efficiency - updated private cli with REST API.

netbox.netbox
~~~~~~~~~~~~~

- nb_inventory - Add serial and asset tag to extracted attributes [#826](https://github.com/netbox-community/ansible_modules/pull/826)

purestorage.flasharray
~~~~~~~~~~~~~~~~~~~~~~

- purefa_network - Added support for NVMe-RoCE and NVMe-TCP service types
- purefa_user - Added Ops Admin role to choices
- purefa_vlan - Added support for NVMe-TCP service type

Breaking Changes / Porting Guide
--------------------------------

hetzner.hcloud
~~~~~~~~~~~~~~

- inventory plugin - Python v3.5+ is now required.

Deprecated Features
-------------------

- Since the google.cloud collection seems to be maintained again, we `cancelled the removal process <https://github.com/ansible-collections/overview/blob/main/removal_from_ansible.rst#cancelling-removal-of-an-unmaintained-collection>`__. So contrary to an earlier announcement, this collection is NOT deprecated and will NOT be removed from Ansible 8 (https://github.com/ansible-community/community-topics/issues/105).

community.general
~~~~~~~~~~~~~~~~~

- gitlab_runner - the option ``access_level`` will lose its default value in community.general 8.0.0. From that version on, you have set this option to ``ref_protected`` explicitly, if you want to have a protected runner (https://github.com/ansible-collections/community.general/issues/5925).

Bugfixes
--------

Ansible-core
~~~~~~~~~~~~

- Ansible.Basic.cs - Ignore compiler warning (reported as an error) when running under PowerShell 7.3.x.
- Fix conditionally notifying ``include_tasks` handlers when ``force_handlers`` is used (https://github.com/ansible/ansible/issues/79776)
- TaskExecutor - don't ignore templated _raw_params that k=v parser failed to parse (https://github.com/ansible/ansible/issues/79862)
- ansible-galaxy - fix installing collections in git repositories/directories which contain a MANIFEST.json file (https://github.com/ansible/ansible/issues/79796).
- ansible-test - Support Podman 4.4.0+ by adding the ``SYS_CHROOT`` capability when running containers.
- ansible-test - fix warning message about failing to run an image to include the image name
- strategy plugins now correctly identify bad registered variables, even on skip.

cisco.aci
~~~~~~~~~

- Add snapshot job details in result of aci_config_snapshot to support query of snapshot results (#342)
- Fix aci_encap_pool_range by removing range_name from required parameters (#368)
- Fix query of all blacklisted interfaces using aci_interface_blacklist (#367)

cisco.meraki
~~~~~~~~~~~~

- Corrects constraints applied to local and remote status page settings to align with API behaviour (https://github.com/CiscoDevNet/ansible-meraki/issues/437)
- Enables meraki_network query by net_id (https://github.com/CiscoDevNet/ansible-meraki/issues/441)
- Resolved an issue where an empty response from the API triggered an exception in module meraki_webhook (https://github.com/CiscoDevNet/ansible-meraki/issues/433)
- Resolves issues with meraki_webhook shared_secret defaulting to null; (https://github.com/CiscoDevNet/ansible-meraki/issues/439); Also adds Test Coverage for shared secret idempotency and resolves test file lint issues.

cisco.nxos
~~~~~~~~~~

- `nxos_acls` - Fix how IPv6 prefixes are converted to hosts (https://github.com/ansible-collections/cisco.nxos/issues/623).
- `nxos_file_copy` - stop prepending redundant bootflash: to remote file names
- nxos_acls - Detect duplicate ACE error message from CLI and fail (https://github.com/ansible-collections/cisco.nxos/issues/611).
- nxos_command - Run & evaluate commands at least once even when retries is set to 0 (https://github.com/ansible-collections/cisco.nxos/issues/607).

community.crypto
~~~~~~~~~~~~~~~~

- action plugin helper - fix handling of deprecations for ansible-core 2.14.2 (https://github.com/ansible-collections/community.crypto/pull/572).
- execution environment binary dependencies (bindep.txt) - fix ``python3-pyOpenSSL`` dependency resolution on RHEL 9+ / CentOS Stream 9+ platforms (https://github.com/ansible-collections/community.crypto/pull/575).
- various plugins - remove unnecessary imports (https://github.com/ansible-collections/community.crypto/pull/569).

community.dns
~~~~~~~~~~~~~

- Update Public Suffix List.

community.docker
~~~~~~~~~~~~~~~~

- docker_api connection plugin, docker_container_exec, docker_container_copy_into - properly close socket to Daemon after executing commands in containers (https://github.com/ansible-collections/community.docker/pull/582).
- docker_container - fix ``tmfs_size`` and ``tmpfs_mode`` not being set (https://github.com/ansible-collections/community.docker/pull/580).
- docker_prune - return correct value for ``changed``. So far the module always claimed that nothing changed (https://github.com/ansible-collections/community.docker/pull/593).
- various plugins and modules - remove unnecessary imports (https://github.com/ansible-collections/community.docker/pull/574).

community.general
~~~~~~~~~~~~~~~~~

- cartesian and flattened lookup plugins - adjust to parameter deprecation in ansible-core 2.14's ``listify_lookup_plugin_terms`` helper function (https://github.com/ansible-collections/community.general/pull/6074).
- cloudflare_dns - fixed the idempotency for SRV DNS records (https://github.com/ansible-collections/community.general/pull/5972).
- cloudflare_dns - fixed the possiblity of setting a root-level SRV DNS record (https://github.com/ansible-collections/community.general/pull/5972).
- github_webhook - fix always changed state when no secret is provided (https://github.com/ansible-collections/community.general/pull/5994).
- jenkins_plugin - fix error due to undefined variable when updates file is not downloaded (https://github.com/ansible-collections/community.general/pull/6100).
- keycloak_client - fix accidental replacement of value for attribute ``saml.signing.private.key`` with ``no_log`` in wrong contexts (https://github.com/ansible-collections/community.general/pull/5934).
- lxd_* modules, lxd inventory plugin - fix TLS/SSL certificate validation problems by using the correct purpose when creating the TLS context (https://github.com/ansible-collections/community.general/issues/5616, https://github.com/ansible-collections/community.general/pull/6034).
- nmcli - fix change handling of values specified as an integer 0 (https://github.com/ansible-collections/community.general/pull/5431).
- nmcli - fix failure to handle WIFI settings when connection type not specified (https://github.com/ansible-collections/community.general/pull/5431).
- nmcli - fix improper detection of changes to ``wifi.wake-on-wlan`` (https://github.com/ansible-collections/community.general/pull/5431).
- nmcli - order is significant for lists of addresses (https://github.com/ansible-collections/community.general/pull/6048).
- onepassword lookup plugin - Changed to ignore errors from "op account get" calls. Previously, errors would prevent auto-signin code from executing (https://github.com/ansible-collections/community.general/pull/5942).
- terraform and timezone - slight refactoring to avoid linter reporting potentially undefined variables (https://github.com/ansible-collections/community.general/pull/5933).
- various plugins and modules - remove unnecessary imports (https://github.com/ansible-collections/community.general/pull/5940).
- yarn - fix ``global=true`` to check for the configured global folder instead of assuming the default (https://github.com/ansible-collections/community.general/pull/5829)
- yarn - fix ``state=absent`` not working with ``global=true`` when the package does not include a binary (https://github.com/ansible-collections/community.general/pull/5829)
- yarn - fix ``state=latest`` not working with ``global=true`` (https://github.com/ansible-collections/community.general/issues/5712).
- zfs_delegate_admin - zfs allow output can now be parsed when uids/gids are not known to the host system (https://github.com/ansible-collections/community.general/pull/5943).
- zypper - make package managing work on readonly filesystem of openSUSE MicroOS (https://github.com/ansible-collections/community.general/pull/5615).

community.grafana
~~~~~~~~~~~~~~~~~

- Fixed validate_certs missing parameter for --insecure option in grafana plugins
- URL encode issue in grafana_organization.py (method get_actual_org ) fixed.
- grafana_dashboard, now opens json files with utf-8 encoding (#191)

community.mysql
~~~~~~~~~~~~~~~

- mysql_user - when revoke privs consists only of ``GRANT``, a 2nd revoke query is executed with empty privs to revoke that ended in an SQL exception (https://github.com/ansible-collections/community.mysql/pull/503).
- mysql_variables - add uppercase character pattern to regex to allow GLOBAL variables containing uppercase characters. This recognizes variable names used in Galera, for example, ``wsrep_OSU_method``, which breaks the normal pattern of all lowercase characters (https://github.com/ansible-collections/community.mysql/pull/501).

community.okd
~~~~~~~~~~~~~

- openshift_adm_groups_sync - initialize OpenshiftGroupSync attributes early to avoid Attribute error (https://github.com/openshift/community.okd/issues/155).
- openshift_auth - Review the way the discard process is working, add openshift algorithm to convert token to resource object name (https://github.com/openshift/community.okd/issues/176).

community.sops
~~~~~~~~~~~~~~

- action plugin helper - fix handling of deprecations for ansible-core 2.14.2 (https://github.com/ansible-collections/community.sops/pull/136).
- various plugins - remove unnecessary imports (https://github.com/ansible-collections/community.sops/pull/133).

community.vmware
~~~~~~~~~~~~~~~~

- scenario guides - Fix broken references (https://github.com/ansible-collections/community.vmware/issues/1610).
- various - Fix new pylint issues (https://github.com/ansible-collections/community.vmware/pull/1637).
- vmware_cluster_info - Fix pylint issues (https://github.com/ansible-collections/community.vmware/issues/1618).
- vmware_dvswitch - Fix pylint issues (https://github.com/ansible-collections/community.vmware/issues/1618).
- vmware_dvswitch_lacp - Fix pylint issues (https://github.com/ansible-collections/community.vmware/issues/1618).
- vmware_dvswitch_uplink_pg - Fix pylint issues (https://github.com/ansible-collections/community.vmware/issues/1618).
- vmware_guest_custom_attributes - Fixes assigning attributes to new VMs (https://github.com/ansible-collections/community.vmware/issues/1606).
- vmware_guest_disk - Fix wrong key in the documentation of the return values (https://github.com/ansible-collections/community.vmware/issues/1615)
- vmware_object_rename - Add missing quotation mark to error message (https://github.com/ansible-collections/community.vmware/issues/1633)
- vmware_portgroup - Fix pylint issues (https://github.com/ansible-collections/community.vmware/issues/1618).
- vmware_vcenter_settings - Fix pylint issues (https://github.com/ansible-collections/community.vmware/issues/1618).
- vmware_vcenter_statistics - Fix pylint issues (https://github.com/ansible-collections/community.vmware/issues/1618).

community.zabbix
~~~~~~~~~~~~~~~~

- zabbix_agent and zabbix_proxy roles - fixed a bug whith ansible_python_interpreter not being set correctly in some corner cases
- zabbix_agent role - Fix MacOS install never executed because of the missing include_tasks "Darwin.yml" in the "main.yml" task file and wrong user permission on folder/files.
- zabbix_agent, zabbix_proxy and zabbix_server roles - make Ansible 2.14 compatible by removing warn parameter

f5networks.f5_modules
~~~~~~~~~~~~~~~~~~~~~

- bigip_device_license - Add fix for a bug that caused infinite loop when the auth token expired

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

netapp.ontap
~~~~~~~~~~~~

- na_ontap_aggregate - try to offline aggregate when disk add operation is in progress in ZAPI.
- na_ontap_interface - fix idempotency issue when ``home_port`` not set in creating FC interface.
- na_ontap_rest_info - fix field issue with private/cli and support/autosupport/check APIs.
- na_ontap_snapshot - fix cannot modify ``snapmirror_label``, ``expiry_time`` and ``comment`` if not configured in create.
- na_ontap_user_role - fix AttributeError 'NetAppOntapUserRole' object has no attribute 'name'.
- na_ontap_user_role - fix KeyError on ``vserver``, ``command_directory_name`` in ZAPI and ``path``, ``query`` in REST.
- na_ontap_user_role - fix duplicate entry error in ZAPI.
- na_ontap_user_role - fix entry does not exist error when trying to delete privilege in REST.
- na_ontap_volume_efficiency - fix idempotent issue when state is absent and efficiency options are set in ZAPI.

netbox.netbox
~~~~~~~~~~~~~

- nb_lookup - Fix pynetbox 7.0.1 compatibility [#934](https://github.com/netbox-community/ansible_modules/pull/934)
- netbox_cable - Fix NetBox 3.3 compatibility [#938](https://github.com/netbox-community/ansible_modules/pull/938)
- netbox_webhook - Fix conditions bug [#926](https://github.com/netbox-community/ansible_modules/pull/926)

purestorage.flasharray
~~~~~~~~~~~~~~~~~~~~~~

- purefa_host - Fixed parameter name
- purefa_info - Fix missing FC target ports for host
- purefa_pgsched - Fix error when setting schedule for pod based protection group
- purefa_vg - Fix issue with VG creation on newer Purity versions
- purefa_volume - Ensure promotion_stateus is returned correctly on creation
- purefa_volume - Fix bug when overwriting volume using invalid parmaeters
- purefa_volume - Fixed idempotency bug when creating volumes with QoS

theforeman.foreman
~~~~~~~~~~~~~~~~~~

- content_export_* - increase task timeout to 12h as export tasks can be time intensive (https://bugzilla.redhat.com/show_bug.cgi?id=2162678)

New Modules
-----------

community.okd
~~~~~~~~~~~~~

- community.okd.openshift_adm_prune_builds - Prune old completed and failed builds
- community.okd.openshift_build - Start a new build or Cancel running, pending, or new builds.

inspur.ispim
~~~~~~~~~~~~

- inspur.ispim.support_info - Get support information

kubernetes.core
~~~~~~~~~~~~~~~

- kubernetes.core.helm_pull - download a chart from a repository and (optionally) unpack it in local directory.

netapp.ontap
~~~~~~~~~~~~

- netapp.ontap.na_ontap_vserver_audit - NetApp Ontap - create, delete or modify vserver audit configuration.
- netapp.ontap.na_ontap_vserver_peer_permissions - NetApp Ontap - create, delete or modify vserver peer permission.

theforeman.foreman
~~~~~~~~~~~~~~~~~~

- theforeman.foreman.content_view_filter_info - Fetch information about a Content View Filter
- theforeman.foreman.content_view_filter_rule - Manage content view filter rules
- theforeman.foreman.content_view_filter_rule_info - Fetch information about a Content View Filter Rule
- theforeman.foreman.hostgroup_info - Get information about hostgroup(s)

Unchanged Collections
---------------------

- amazon.aws (still version 5.2.0)
- ansible.netcommon (still version 4.1.0)
- ansible.posix (still version 1.5.1)
- ansible.utils (still version 2.9.0)
- ansible.windows (still version 1.13.0)
- arista.eos (still version 6.0.0)
- azure.azcollection (still version 1.14.0)
- check_point.mgmt (still version 4.0.0)
- chocolatey.chocolatey (still version 1.4.0)
- cisco.asa (still version 4.0.0)
- cisco.dnac (still version 6.6.3)
- cisco.intersight (still version 1.0.23)
- cisco.ios (still version 4.3.1)
- cisco.iosxr (still version 4.1.0)
- cisco.ise (still version 2.5.12)
- cisco.mso (still version 2.2.1)
- cisco.nso (still version 1.0.3)
- cisco.ucs (still version 1.8.0)
- cloud.common (still version 2.1.2)
- cloudscale_ch.cloud (still version 2.2.4)
- community.aws (still version 5.2.0)
- community.azure (still version 2.0.0)
- community.ciscosmb (still version 1.0.5)
- community.digitalocean (still version 1.23.0)
- community.fortios (still version 1.0.0)
- community.google (still version 1.0.0)
- community.hashi_vault (still version 4.1.0)
- community.hrobot (still version 1.7.0)
- community.libvirt (still version 1.2.0)
- community.network (still version 5.0.0)
- community.postgresql (still version 2.3.2)
- community.proxysql (still version 1.5.1)
- community.rabbitmq (still version 1.2.3)
- community.routeros (still version 2.7.0)
- community.sap (still version 1.0.0)
- community.sap_libs (still version 1.4.0)
- community.skydive (still version 1.0.0)
- community.windows (still version 1.12.0)
- containers.podman (still version 1.10.1)
- cyberark.conjur (still version 1.2.0)
- cyberark.pas (still version 1.0.17)
- dellemc.enterprise_sonic (still version 2.0.0)
- dellemc.openmanage (still version 6.3.0)
- dellemc.os10 (still version 1.1.1)
- dellemc.os6 (still version 1.0.7)
- dellemc.os9 (still version 1.0.4)
- dellemc.powerflex (still version 1.5.0)
- dellemc.unity (still version 1.5.0)
- fortinet.fortimanager (still version 2.1.7)
- fortinet.fortios (still version 2.2.2)
- frr.frr (still version 2.0.0)
- gluster.gluster (still version 1.0.2)
- google.cloud (still version 1.1.2)
- hpe.nimble (still version 1.1.4)
- ibm.qradar (still version 2.1.0)
- ibm.spectrum_virtualize (still version 1.11.0)
- infinidat.infinibox (still version 1.3.12)
- infoblox.nios_modules (still version 1.4.1)
- inspur.sm (still version 2.3.0)
- junipernetworks.junos (still version 4.1.0)
- lowlydba.sqlserver (still version 1.3.1)
- mellanox.onyx (still version 1.0.0)
- netapp.aws (still version 21.7.0)
- netapp.azure (still version 21.10.0)
- netapp.cloudmanager (still version 21.22.0)
- netapp.elementsw (still version 21.7.0)
- netapp.storagegrid (still version 21.11.1)
- netapp.um_info (still version 21.8.0)
- netapp_eseries.santricity (still version 1.4.0)
- ngine_io.cloudstack (still version 2.3.0)
- ngine_io.exoscale (still version 1.0.0)
- ngine_io.vultr (still version 1.1.3)
- openstack.cloud (still version 1.10.0)
- openvswitch.openvswitch (still version 2.1.0)
- ovirt.ovirt (still version 2.4.1)
- purestorage.flashblade (still version 1.10.0)
- purestorage.fusion (still version 1.3.0)
- sensu.sensu_go (still version 1.13.2)
- splunk.es (still version 2.1.0)
- t_systems_mms.icinga_director (still version 1.32.0)
- vmware.vmware_rest (still version 2.2.0)
- vultr.cloud (still version 1.7.0)
- vyos.vyos (still version 4.0.0)
- wti.remote (still version 1.0.4)

v7.2.0
======

.. contents::
  :local:
  :depth: 2

Release Summary
---------------

Release Date: 2023-01-31

`Porting Guide <https://docs.ansible.com/ansible/devel/porting_guides.html>`_

Added Collections
-----------------

- dellemc.powerflex (version 1.5.0)
- dellemc.unity (version 1.5.0)

Ansible-core
------------

Ansible 7.2.0 contains Ansible-core version 2.14.2.
This is a newer version than version 2.14.1 contained in the previous Ansible release.

The changes are reported in the combined changelog below.

Changed Collections
-------------------

If not mentioned explicitly, the changes are reported in the combined changelog below.

+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| Collection                    | Ansible 7.1.0 | Ansible 7.2.0 | Notes                                                                                                                        |
+===============================+===============+===============+==============================================================================================================================+
| amazon.aws                    | 5.1.0         | 5.2.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| ansible.posix                 | 1.4.0         | 1.5.1         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| ansible.utils                 | 2.8.0         | 2.9.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| ansible.windows               | 1.12.0        | 1.13.0        |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| awx.awx                       | 21.10.0       | 21.11.0       | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| chocolatey.chocolatey         | 1.3.1         | 1.4.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.dnac                    | 6.6.1         | 6.6.3         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.intersight              | 1.0.22        | 1.0.23        | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.ios                     | 4.0.0         | 4.3.1         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.iosxr                   | 4.0.3         | 4.1.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.ise                     | 2.5.9         | 2.5.12        |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.meraki                  | 2.13.0        | 2.15.0        |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.mso                     | 2.1.0         | 2.2.1         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cloudscale_ch.cloud           | 2.2.3         | 2.2.4         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.aws                 | 5.0.0         | 5.2.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.crypto              | 2.9.0         | 2.10.0        |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.digitalocean        | 1.22.0        | 1.23.0        |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.dns                 | 2.4.2         | 2.5.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.docker              | 3.3.1         | 3.4.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.general             | 6.1.0         | 6.3.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.hashi_vault         | 4.0.0         | 4.1.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.hrobot              | 1.6.0         | 1.7.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.postgresql          | 2.3.1         | 2.3.2         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.proxysql            | 1.4.0         | 1.5.1         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.routeros            | 2.5.0         | 2.7.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.sops                | 1.5.0         | 1.6.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.vmware              | 3.2.0         | 3.3.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.windows             | 1.11.1        | 1.12.0        |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.zabbix              | 1.9.0         | 1.9.1         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cyberark.pas                  | 1.0.14        | 1.0.17        | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| dellemc.powerflex             |               | 1.5.0         | The collection was added to Ansible                                                                                          |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| dellemc.unity                 |               | 1.5.0         | The collection was added to Ansible                                                                                          |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| f5networks.f5_modules         | 1.21.0        | 1.22.0        |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| fortinet.fortios              | 2.2.1         | 2.2.2         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| google.cloud                  | 1.0.2         | 1.1.2         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| hetzner.hcloud                | 1.9.0         | 1.9.1         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| ibm.spectrum_virtualize       | 1.10.0        | 1.11.0        |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| lowlydba.sqlserver            | 1.2.1         | 1.3.1         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| netapp.cloudmanager           | 21.21.0       | 21.22.0       |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| netapp.ontap                  | 22.0.1        | 22.2.0        |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| netapp_eseries.santricity     | 1.3.1         | 1.4.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| netbox.netbox                 | 3.9.0         | 3.10.0        |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| ngine_io.vultr                | 1.1.2         | 1.1.3         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| purestorage.flasharray        | 1.15.0        | 1.16.2        |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| purestorage.fusion            | 1.2.0         | 1.3.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| sensu.sensu_go                | 1.13.1        | 1.13.2        |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| t_systems_mms.icinga_director | 1.31.4        | 1.32.0        |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| theforeman.foreman            | 3.7.0         | 3.8.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| vultr.cloud                   | 1.3.1         | 1.7.0         |                                                                                                                              |
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

Minor Changes
-------------

Ansible-core
~~~~~~~~~~~~

- ansible-test - A new ``audit`` option is available when running custom containers. This option can be used to indicate whether a container requires the AUDIT_WRITE capability. The default is ``required``, which most containers will need when using Podman. If necessary, the ``none`` option can be used to opt-out of the capability. This has no effect on Docker, which always provides the capability.
- ansible-test - A new ``cgroup`` option is available when running custom containers. This option can be used to indicate a container requires cgroup v1 or that it does not use cgroup. The default behavior assumes the container works with cgroup v2 (as well as v1).
- ansible-test - Additional log details are shown when containers fail to start or SSH connections to containers fail.
- ansible-test - Connection failures to remote provisioned hosts now show failure details as a warning.
- ansible-test - Containers included with ansible-test no longer disable seccomp by default.
- ansible-test - Failure to connect to a container over SSH now results in a clear error. Previously tests would be attempted even after initial connection attempts failed.
- ansible-test - Integration tests can be excluded from retries triggered by the ``--retry-on-error`` option by adding the ``retry/never`` alias. This is useful for tests that cannot pass on a retry or are too slow to make retries useful.
- ansible-test - More details are provided about an instance when provisioning fails.
- ansible-test - Reduce the polling limit for SSHD startup in containers from 60 retries to 10. The one second delay between retries remains in place.
- ansible-test - SSH connections from OpenSSH 8.8+ to CentOS 6 containers now work without additional configuration. However, clients older than OpenSSH 7.0 can no longer connect to CentOS 6 containers as a result. The container must have ``centos6`` in the image name for this work-around to be applied.
- ansible-test - SSH shell connections from OpenSSH 8.8+ to ansible-test provisioned network instances now work without additional configuration. However, clients older than OpenSSH 7.0 can no longer open shell sessions for ansible-test provisioned network instances as a result.
- ansible-test - The ``ansible-test env`` command now detects and reports the container ID if running in a container.
- ansible-test - Unit tests now support network disconnect by default when running under Podman. Previously this feature only worked by default under Docker.
- ansible-test - Use ``stop --time 0`` followed by ``rm`` to remove ephemeral containers instead of ``rm -f``. This speeds up teardown of ephemeral containers.
- ansible-test - Warnings are now shown when using containers that were built with VOLUME instructions.
- ansible-test - When setting the max open files for containers, the container host's limit will be checked. If the host limit is lower than the preferred value, it will be used and a warning will be shown.
- ansible-test - When using Podman, ansible-test will detect if the loginuid used in containers is incorrect. When this occurs a warning is displayed and the container is run with the AUDIT_CONTROL capability. Previously containers would fail under this situation, with no useful warnings or errors given.

amazon.aws
~~~~~~~~~~

- amazon.aws collection - refacterization of code to use argument specification ``fallback`` when falling back to environment variables for security credentials and AWS connection details (https://github.com/ansible-collections/amazon.aws/pull/1174).
- rds_instance - Split up the integration test-suite in a series of smaller tests (https://github.com/ansible-collections/amazon.aws/pull/1185).
- rds_instance - add support for gp3 storage type (https://github.com/ansible-collections/amazon.aws/pull/1266).

ansible.posix
~~~~~~~~~~~~~

- mount - Add ``absent_from_fstab`` state (https://github.com/ansible-collections/ansible.posix/pull/166).
- mount - Add ``ephemeral`` value for the ``state`` parameter, that allows to mount a filesystem without altering the ``fstab`` file (https://github.com/ansible-collections/ansible.posix/pull/267).
- r4e_rpm_ostree - new module for validating package state on RHEL for Edge
- rhel_facts - new facts module to handle RHEL specific facts
- rhel_rpm_ostree - new module to handle RHEL rpm-ostree specific package management functionality
- rpm_ostree_upgrade - new module to automate rpm-ostree upgrades
- rpm_ostree_upgrade - new module to manage upgrades for rpm-ostree based systems

ansible.utils
~~~~~~~~~~~~~

- to_xml - Added support to disable xml declartion with full_document flag.

ansible.windows
~~~~~~~~~~~~~~~

- win_reboot - Display connection messages under 4 v's ``-vvvv`` instead of 3

cisco.ios
~~~~~~~~~

- cliconf - Added support for commit confirm functionality and rollback based on timeout.
- ios_facts - default facts to show operating state data autonomous or controller mode.
- ios_l2_interfaces - more options for modes attribute added.
- ios_route_maps - added 32-bit number support (https://github.com/ansible-collections/cisco.ios/pull/692)

cisco.iosxr
~~~~~~~~~~~

- iosxr.iosxr_bgp_global - Add missing set option in fast-detect dict of bgp nbr.

cisco.meraki
~~~~~~~~~~~~

- New module - meraki_network_settings - Configure detailed settings of a network.
- meraki_webhook - Add payload template parameter

cisco.mso
~~~~~~~~~

- Add automatic creation of site bd when not existing in mso_schema_site_bd_subnet module (#263)
- Add automatic schema validation functionality to mso_schema_template_deploy and ndo_schema_template_deploy (#318)
- Add ndo_schema_template_deploy to support NDO 4+ deploy functionality (#305)
- Add support for l3out from different template or schema in mso_schema_site_bd_l3out (#304)
- Add support for orchestrator_only attribute for mso_tenant with state absent (#268)

cloudscale_ch.cloud
~~~~~~~~~~~~~~~~~~~

- Add UEFI firmware type option for custom images.

community.aws
~~~~~~~~~~~~~

- aws_ssm - add ``ansible_aws_ssm_s3_addressing_style`` to allow setting the S3 addressing style (https://github.com/ansible-collections/community.aws/pull/1633).
- aws_ssm - add support for custom SSM documents (https://github.com/ansible-collections/community.aws/pull/876).
- aws_ssm - avoid overloading ``subprocess`` (https://github.com/ansible-collections/community.aws/pull/1660).
- aws_ssm - cleanup logging output (https://github.com/ansible-collections/community.aws/pull/1660).
- aws_ssm - minor refactoring (https://github.com/ansible-collections/community.aws/pull/1660).
- aws_ssm - refactor boto3 client initialization (https://github.com/ansible-collections/community.aws/pull/1663).
- aws_ssm - refactor remote command generation (https://github.com/ansible-collections/community.aws/pull/1664).
- ecs_cluster - add support for ``capacity_providers`` and ``capacity_provider_strategy`` features (https://github.com/ansible-collections/community.aws/pull/1640).
- ecs_cluster - append default value to documentation (https://github.com/ansible-collections/community.aws/pull/1636).
- ecs_ecr - add ``encryption_configuration`` option (https://github.com/ansible-collections/community.aws/pull/1623).
- ecs_service - support load balancer update for existing ECS services (https://github.com/ansible-collections/community.aws/pull/1625).
- elasticache_parameter_group - add ``redis6.x`` group family on the module input choices (https://github.com/ansible-collections/community.aws/pull/1476).
- elb_target_group - add support for ``protocol_version`` parameter (https://github.com/ansible-collections/community.aws/pull/1496).
- iam_role - Drop deprecation warning, because the standard value for purge parameters is ``true`` (https://github.com/ansible-collections/community.aws/pull/1636).
- ssm_parameter - fix typo in examples ``paramater`` (https://github.com/ansible-collections/community.aws/issues/1642).

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

- docker_api connection plugin - when copying files to/from a container, stream the file contents instead of first reading them to memory (https://github.com/ansible-collections/community.docker/pull/545).
- docker_host_info - allow to list all containers with new option ``containers_all`` (https://github.com/ansible-collections/community.docker/issues/535, https://github.com/ansible-collections/community.docker/pull/538).

community.general
~~~~~~~~~~~~~~~~~

- apache2_module - add module argument ``warn_mpm_absent`` to control whether warning are raised in some edge cases (https://github.com/ansible-collections/community.general/pull/5793).
- bitwarden lookup plugin - can now retrieve secrets from custom fields (https://github.com/ansible-collections/community.general/pull/5694).
- bitwarden lookup plugin - implement filtering results by ``collection_id`` parameter (https://github.com/ansible-collections/community.general/issues/5849).
- dig lookup plugin - support CAA record type (https://github.com/ansible-collections/community.general/pull/5913).
- gitlab_project - add ``builds_access_level``, ``container_registry_access_level`` and ``forking_access_level`` options (https://github.com/ansible-collections/community.general/pull/5706).
- gitlab_runner - add new boolean option ``access_level_on_creation``. It controls, whether the value of ``access_level`` is used for runner registration or not. The option ``access_level`` has been ignored on registration so far and was only used on updates (https://github.com/ansible-collections/community.general/issues/5907, https://github.com/ansible-collections/community.general/pull/5908).
- ilo_redfish_utils module utils - change implementation of DNS Server IP and NTP Server IP update (https://github.com/ansible-collections/community.general/pull/5804).
- ipa_group - allow to add and remove external users with the ``external_user`` option (https://github.com/ansible-collections/community.general/pull/5897).
- iptables_state - minor refactoring within the module (https://github.com/ansible-collections/community.general/pull/5844).
- one_vm - add a new ``updateconf`` option which implements the ``one.vm.updateconf`` API call (https://github.com/ansible-collections/community.general/pull/5812).
- opkg - allow installing a package in a certain version (https://github.com/ansible-collections/community.general/pull/5688).
- opkg - refactored module to use ``CmdRunner`` for executing ``opkg`` (https://github.com/ansible-collections/community.general/pull/5718).
- proxmox - added new module parameter ``tags`` for use with PVE 7+ (https://github.com/ansible-collections/community.general/pull/5714).
- puppet - refactored module to use ``CmdRunner`` for executing ``puppet`` (https://github.com/ansible-collections/community.general/pull/5612).
- redhat_subscription - add a ``server_proxy_scheme`` parameter to configure the scheme for the proxy server (https://github.com/ansible-collections/community.general/pull/5662).
- redhat_subscription - adds ``token`` parameter for subscription-manager authentication using Red Hat API token (https://github.com/ansible-collections/community.general/pull/5725).
- snap - minor refactor when executing module (https://github.com/ansible-collections/community.general/pull/5773).
- snap_alias - refactored module to use ``CmdRunner`` to execute ``snap`` (https://github.com/ansible-collections/community.general/pull/5486).
- ssh_config - refactor code to module util to fix sanity check (https://github.com/ansible-collections/community.general/pull/5720).
- sudoers - add ``setenv`` parameters to support passing environment variables via sudo. (https://github.com/ansible-collections/community.general/pull/5883)
- sudoers - adds ``host`` parameter for setting hostname restrictions in sudoers rules (https://github.com/ansible-collections/community.general/issues/5702).

community.proxysql
~~~~~~~~~~~~~~~~~~

- roles/proxysql - add support for configuring REST API (https://github.com/ansible-collections/community.proxysql/pull/110).

community.routeros
~~~~~~~~~~~~~~~~~~

- api_modify, api_info - add field ``regexp`` to ``ip dns static`` (https://github.com/ansible-collections/community.routeros/issues/141).
- api_modify, api_info - support API paths ``interface wireguard``, ``interface wireguard peers`` (https://github.com/ansible-collections/community.routeros/pull/143).
- api_modify, api_info - support API paths ``ip arp``, ``ip firewall raw``, ``ipv6 firewall raw`` (https://github.com/ansible-collections/community.routeros/pull/144).

community.sops
~~~~~~~~~~~~~~

- install role - add ``sops_github_latest_detection`` option that allows to configure which method to use for detecting the latest release on GitHub. By default (``auto``) first tries to retrieve a list of recent releases using the API, and if that fails due to rate limiting, tries to obtain the latest GitHub release from a semi-documented URL (https://github.com/ansible-collections/community.sops/pull/133).
- install role - add ``sops_github_token`` option to allow passing a GitHub token. This can for example be used to avoid rate limits when using the role in GitHub Actions (https://github.com/ansible-collections/community.sops/pull/132).
- install role - implement another method to determine the latest release on GitHub than using the GitHub API, which can make installation fail due to rate-limiting (https://github.com/ansible-collections/community.sops/pull/131).

community.vmware
~~~~~~~~~~~~~~~~

- vmware_cluster_drs - Add predictive DRS Setting (https://github.com/ansible-collections/community.vmware/pull/1542).
- vmware_guest_network - Add PVRDMA network adapter type (https://github.com/ansible-collections/community.vmware/pull/1579).

community.windows
~~~~~~~~~~~~~~~~~

- win_dns_record - Added support for DHCID (RFC 4701) records
- win_domain_user - Added the ``display_name`` option to set the users display name attribute

community.zabbix
~~~~~~~~~~~~~~~~

- zabbix suport for rhel 9

f5networks.f5_modules
~~~~~~~~~~~~~~~~~~~~~

- bigip_device_auth_ldap - added a new parameter referrals
- bigip_device_group - added a new parameter, asm_sync to support ASM policy synchronization
- bigip_device_group - changed full_sync, auto_sync, save_on_auto_sync parameters only to set default value during creation, to work as documented.
- bigip_device_info - add data_increment parameter for better control of data gathering from API, addresses cases where large configurations were causing token timeouts during module operation
- bigip_device_info - added option for gathering info about device license.
- bigip_monitor_http - add up_interval parameter
- bigip_policy_rule - added ASM to disable_target list
- bigip_policy_rule - added host_begins_not_with_any and host_ends_not_with_any to conditions
- bigip_profile_http- add hsts_preload parameter
- bigip_profile_tcp - add keep_alive_interval parameter

google.cloud
~~~~~~~~~~~~

- GCE inventory plugin - a new option ``name_suffix``, to add a suffix to the name parameter.

ibm.spectrum_virtualize
~~~~~~~~~~~~~~~~~~~~~~~

- ibm_svc_host - Added support for modification of iSCSI host.
- ibm_svc_manage_migraiton - Added support for volume migration across pools.

lowlydba.sqlserver
~~~~~~~~~~~~~~~~~~

- Adding a new credential module
- Update login module documentation to indicate result will always be changed when a password is supplied. (https://github.com/lowlydba/lowlydba.sqlserver/pull/167)

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
- na_ontap_cifs_local_group_member - Added REST API support to retrieve, add and remove CIFS group member.
- na_ontap_cifs_local_group_member - REST support is from ONTAP 9.10.1 or later.
- na_ontap_cifs_server - skip ``service_state`` option if not set in create.
- na_ontap_interface - error when try to migrate fc interface in REST.
- na_ontap_interface - new option ``fail_if_subnet_conflicts`` - requires REST and ONTAP 9.11.1 or later.
- na_ontap_interface - new option ``probe_port`` for Azure load balancer.
- na_ontap_interface - option ``subnet_name`` is now supported with REST with ONTAP 9.11.1 or later.
- na_ontap_iscsi - new option ``target_alias`` added in REST.
- na_ontap_quotas - for qtree type, allow quota_target in path format /vol/vol_name/qtree_name in REST.
- na_ontap_snapmirror - support ``schedule`` with REST and ONTAP 9.11.1, add alias ``transfer_schedule``.
- na_ontap_snapmirror_policy - Added new choices sync and async for policy type in REST.
- na_ontap_snapmirror_policy - Added unsupported options in ZAPI.
- na_ontap_snapmirror_policy - add support for cluster scoped policy with REST.
- na_ontap_snapmirror_policy - new option ``copy_all_source_snapshots`` added in REST.
- na_ontap_snapmirror_policy - new option ``copy_latest_source_snapshot``, ``create_snapshot_on_source`` and ``sync_type`` added in REST.
- na_ontap_snapmirror_policy - new option ``transfer_schedule`` for async policy types.
- na_ontap_snapmirror_policy - warn when replacing policy type ``async_mirror``, ``mirror_vault`` and ``vault`` with policy type ``async`` and ``strict_sync_mirror``, ``sync_mirror`` with ``sync`` in REST.
- na_ontap_svm - warn in case of mismatch in language option spelling.
- na_ontap_volume - report error if vserver does not exist or is not a data vserver on create.

netapp_eseries.santricity
~~~~~~~~~~~~~~~~~~~~~~~~~

- netapp_eseries.santricity.na_santricity_iscsi_interface - Add support of iSCSI HIC speed.
- netapp_eseries.santricity.nar_santricity_host - Add support of iSCSI HIC speed.

netbox.netbox
~~~~~~~~~~~~~

- Add options for NetBox 3.4 [#905](https://github.com/netbox-community/ansible_modules/pull/905)
- netbox_custom_field - Add group_name [#882](https://github.com/netbox-community/ansible_modules/pull/882)
- netbox_device_type and netbox_device - Add airflow [#907](https://github.com/netbox-community/ansible_modules/pull/907)
- netbox_invventory_item_role - Add module [#885](https://github.com/netbox-community/ansible_modules/pull/885)
- netbox_module_type - Add module [#887](https://github.com/netbox-community/ansible_modules/pull/887)
- netbox_service_template - Add module [#908](https://github.com/netbox-community/ansible_modules/pull/908)

purestorage.flasharray
~~~~~~~~~~~~~~~~~~~~~~

- purefa_host - Add support for VLAN ID tagging for a host (Requires Purity//FA 6.3.5)
- purefa_info - Add new subset alerts
- purefa_info - Added default protection information to `config` section
- purefa_volume - Added support for volume promotion/demotion

sensu.sensu_go
~~~~~~~~~~~~~~

- Added support for Rocky and Alma linux
- Added support for ansible 2.14

t_systems_mms.icinga_director
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Add zone to user and notification template (https://github.com/T-Systems-MMS/ansible-collection-icinga-director/pull/198)

theforeman.foreman
~~~~~~~~~~~~~~~~~~

- job_template - add ``default`` option to the ``template_inputs`` parameter
- location, organization - add ``ignore_types`` parameter to adjust automatic association of resources
- redhat_manifest - Search by UUID on the server side if UUID is known. This is faster and allows fetching of manifest in big accounts (>1000 allocations).
- redhat_manifest - return the UUID of the manifest so it can be reused later
- redhat_manifest - set default ``quantity`` to 1 (https://github.com/theforeman/foreman-ansible-modules/pull/1499)

vultr.cloud
~~~~~~~~~~~

- instance - Added argument ``snapshot`` to support creation of instances via snapshot (https://github.com/vultr/ansible-collection-vultr/pull/56).
- instance - Implemented VPC support to attach/detach VPCs (https://github.com/vultr/ansible-collection-vultr/pull/46).
- inventory - Added IPv6 support by adding ``v6_main_ip`` to the attributes and improved docs (https://github.com/vultr/ansible-collection-vultr/pull/54).

Breaking Changes / Porting Guide
--------------------------------

community.general
~~~~~~~~~~~~~~~~~

- ModuleHelper module utils - when the module sets output variables named ``msg``, ``exception``, ``output``, ``vars``, or ``changed``, the actual output will prefix those names with ``_`` (underscore symbol) only when they clash with output variables generated by ModuleHelper itself, which only occurs when handling exceptions. Please note that this breaking change does not require a new major release since before this release, it was not possible to add such variables to the output `due to a bug <https://github.com/ansible-collections/community.general/pull/5755>`__ (https://github.com/ansible-collections/community.general/pull/5765).

Deprecated Features
-------------------

- The cisco.nso collection is considered unmaintained and will be removed from Ansible 9 if no one starts maintaining it again before Ansible 9. See `the removal process for details on how this works <https://github.com/ansible-collections/overview/blob/main/removal_from_ansible.rst#cancelling-removal-of-an-unmaintained-collection>`__ (https://github.com/ansible-community/community-topics/issues/155).
- The community.fortios collection is considered unmaintained and will be removed from Ansible 9 if no one starts maintaining it again before Ansible 9. See `the removal process for details on how this works <https://github.com/ansible-collections/overview/blob/main/removal_from_ansible.rst#cancelling-removal-of-an-unmaintained-collection>`__ (https://github.com/ansible-community/community-topics/issues/162).
- The community.google collection is considered unmaintained and will be removed from Ansible 9 if no one starts maintaining it again before Ansible 9. See `the removal process for details on how this works <https://github.com/ansible-collections/overview/blob/main/removal_from_ansible.rst#cancelling-removal-of-an-unmaintained-collection>`__ (https://github.com/ansible-community/community-topics/issues/160).
- The community.skydive collection is considered unmaintained and will be removed from Ansible 9 if no one starts maintaining it again before Ansible 9. See `the removal process for details on how this works <https://github.com/ansible-collections/overview/blob/main/removal_from_ansible.rst#cancelling-removal-of-an-unmaintained-collection>`__ (https://github.com/ansible-community/community-topics/issues/171).

chocolatey.chocolatey
~~~~~~~~~~~~~~~~~~~~~

- win_chocolatey - Deprecate side-by-side installs.

cisco.ios
~~~~~~~~~

- ios_bgp_address_family - deprecate neighbors.address/tag/ipv6_adddress with neighbor_address which enables common attributes for facts rendering
- ios_bgp_address_family - deprecate neighbors.password with password_options which allows encryption and password
- ios_bgp_address_family - deprecate slow_peer with slow_peer_options which supports a dict attribute

community.dns
~~~~~~~~~~~~~

- The default of the newly added option ``txt_character_encoding`` will change from ``octal`` to ``decimal`` in community.dns 3.0.0. The new default will be compatible with `RFC 1035 <https://www.ietf.org/rfc/rfc1035.txt>`__ (https://github.com/ansible-collections/community.dns/pull/134).

community.general
~~~~~~~~~~~~~~~~~

- consul - deprecate using parameters unused for ``state=absent`` (https://github.com/ansible-collections/community.general/pull/5772).
- gitlab_runner - the default of the new option ``access_level_on_creation`` will change from ``false`` to ``true`` in community.general 7.0.0. This will cause ``access_level`` to be used during runner registration as well, and not only during updates (https://github.com/ansible-collections/community.general/pull/5908).
- manageiq_policies - deprecate ``state=list`` in favour of using ``community.general.manageiq_policies_info`` (https://github.com/ansible-collections/community.general/pull/5721).
- rax - module relies on deprecates library ``pyrax``. Unless maintainers step up to work on the module, it will be marked as deprecated in community.general 7.0.0 and removed in version 9.0.0 (https://github.com/ansible-collections/community.general/pull/5733).
- rax_cbs - module relies on deprecates library ``pyrax``. Unless maintainers step up to work on the module, it will be marked as deprecated in community.general 7.0.0 and removed in version 9.0.0 (https://github.com/ansible-collections/community.general/pull/5733).
- rax_cbs_attachments - module relies on deprecates library ``pyrax``. Unless maintainers step up to work on the module, it will be marked as deprecated in community.general 7.0.0 and removed in version 9.0.0 (https://github.com/ansible-collections/community.general/pull/5733).
- rax_cdb - module relies on deprecates library ``pyrax``. Unless maintainers step up to work on the module, it will be marked as deprecated in community.general 7.0.0 and removed in version 9.0.0 (https://github.com/ansible-collections/community.general/pull/5733).
- rax_cdb_database - module relies on deprecates library ``pyrax``. Unless maintainers step up to work on the module, it will be marked as deprecated in community.general 7.0.0 and removed in version 9.0.0 (https://github.com/ansible-collections/community.general/pull/5733).
- rax_cdb_user - module relies on deprecates library ``pyrax``. Unless maintainers step up to work on the module, it will be marked as deprecated in community.general 7.0.0 and removed in version 9.0.0 (https://github.com/ansible-collections/community.general/pull/5733).
- rax_clb - module relies on deprecates library ``pyrax``. Unless maintainers step up to work on the module, it will be marked as deprecated in community.general 7.0.0 and removed in version 9.0.0 (https://github.com/ansible-collections/community.general/pull/5733).
- rax_clb_nodes - module relies on deprecates library ``pyrax``. Unless maintainers step up to work on the module, it will be marked as deprecated in community.general 7.0.0 and removed in version 9.0.0 (https://github.com/ansible-collections/community.general/pull/5733).
- rax_clb_ssl - module relies on deprecates library ``pyrax``. Unless maintainers step up to work on the module, it will be marked as deprecated in community.general 7.0.0 and removed in version 9.0.0 (https://github.com/ansible-collections/community.general/pull/5733).
- rax_dns - module relies on deprecates library ``pyrax``. Unless maintainers step up to work on the module, it will be marked as deprecated in community.general 7.0.0 and removed in version 9.0.0 (https://github.com/ansible-collections/community.general/pull/5733).
- rax_dns_record - module relies on deprecates library ``pyrax``. Unless maintainers step up to work on the module, it will be marked as deprecated in community.general 7.0.0 and removed in version 9.0.0 (https://github.com/ansible-collections/community.general/pull/5733).
- rax_facts - module relies on deprecates library ``pyrax``. Unless maintainers step up to work on the module, it will be marked as deprecated in community.general 7.0.0 and removed in version 9.0.0 (https://github.com/ansible-collections/community.general/pull/5733).
- rax_files - module relies on deprecates library ``pyrax``. Unless maintainers step up to work on the module, it will be marked as deprecated in community.general 7.0.0 and removed in version 9.0.0 (https://github.com/ansible-collections/community.general/pull/5733).
- rax_files_objects - module relies on deprecates library ``pyrax``. Unless maintainers step up to work on the module, it will be marked as deprecated in community.general 7.0.0 and removed in version 9.0.0 (https://github.com/ansible-collections/community.general/pull/5733).
- rax_identity - module relies on deprecates library ``pyrax``. Unless maintainers step up to work on the module, it will be marked as deprecated in community.general 7.0.0 and removed in version 9.0.0 (https://github.com/ansible-collections/community.general/pull/5733).
- rax_keypair - module relies on deprecates library ``pyrax``. Unless maintainers step up to work on the module, it will be marked as deprecated in community.general 7.0.0 and removed in version 9.0.0 (https://github.com/ansible-collections/community.general/pull/5733).
- rax_meta - module relies on deprecates library ``pyrax``. Unless maintainers step up to work on the module, it will be marked as deprecated in community.general 7.0.0 and removed in version 9.0.0 (https://github.com/ansible-collections/community.general/pull/5733).
- rax_mon_alarm - module relies on deprecates library ``pyrax``. Unless maintainers step up to work on the module, it will be marked as deprecated in community.general 7.0.0 and removed in version 9.0.0 (https://github.com/ansible-collections/community.general/pull/5733).
- rax_mon_check - module relies on deprecates library ``pyrax``. Unless maintainers step up to work on the module, it will be marked as deprecated in community.general 7.0.0 and removed in version 9.0.0 (https://github.com/ansible-collections/community.general/pull/5733).
- rax_mon_entity - module relies on deprecates library ``pyrax``. Unless maintainers step up to work on the module, it will be marked as deprecated in community.general 7.0.0 and removed in version 9.0.0 (https://github.com/ansible-collections/community.general/pull/5733).
- rax_mon_notification - module relies on deprecates library ``pyrax``. Unless maintainers step up to work on the module, it will be marked as deprecated in community.general 7.0.0 and removed in version 9.0.0 (https://github.com/ansible-collections/community.general/pull/5733).
- rax_mon_notification_plan - module relies on deprecates library ``pyrax``. Unless maintainers step up to work on the module, it will be marked as deprecated in community.general 7.0.0 and removed in version 9.0.0 (https://github.com/ansible-collections/community.general/pull/5733).
- rax_network - module relies on deprecates library ``pyrax``. Unless maintainers step up to work on the module, it will be marked as deprecated in community.general 7.0.0 and removed in version 9.0.0 (https://github.com/ansible-collections/community.general/pull/5733).
- rax_queue - module relies on deprecates library ``pyrax``. Unless maintainers step up to work on the module, it will be marked as deprecated in community.general 7.0.0 and removed in version 9.0.0 (https://github.com/ansible-collections/community.general/pull/5733).
- rax_scaling_group - module relies on deprecates library ``pyrax``. Unless maintainers step up to work on the module, it will be marked as deprecated in community.general 7.0.0 and removed in version 9.0.0 (https://github.com/ansible-collections/community.general/pull/5733).
- rax_scaling_policy - module relies on deprecates library ``pyrax``. Unless maintainers step up to work on the module, it will be marked as deprecated in community.general 7.0.0 and removed in version 9.0.0 (https://github.com/ansible-collections/community.general/pull/5733).

community.hashi_vault
~~~~~~~~~~~~~~~~~~~~~

- ansible-core - support for ``ansible-core`` versions ``2.11`` and ``2.12`` will be dropped in collection version ``5.0.0``, making ``2.13`` the minimum supported version of ``ansible-core`` (https://github.com/ansible-collections/community.hashi_vault/issues/340).
- hvac - the minimum version of ``hvac`` to be supported in collection version ``5.0.0`` will be at least ``1.0.2``; this minimum may be raised before ``5.0.0`` is released, so please subscribe to the linked issue and look out for new notices in the changelog (https://github.com/ansible-collections/community.hashi_vault/issues/324).

Bugfixes
--------

Ansible-core
~~~~~~~~~~~~

- Correctly count rescued tasks in play recap (https://github.com/ansible/ansible/issues/79711)
- Fix traceback when using the ``template`` module and running with ``ANSIBLE_DEBUG=1`` (https://github.com/ansible/ansible/issues/79763)
- Fix using ``GALAXY_IGNORE_CERTS`` in conjunction with collections in requirements files which specify a specific ``source`` that isn't in the configured servers.
- Fix using ``GALAXY_IGNORE_CERTS`` when downloading tarballs from Galaxy servers (https://github.com/ansible/ansible/issues/79557).
- Module and role argument validation - include the valid suboption choices in the error when an invalid suboption is provided.
- ansible-doc now will correctly display short descriptions on listing filters/tests no matter the directory sorting.
- ansible-inventory will not explicitly sort groups/hosts anymore, giving a chance (depending on output format) to match the order in the input sources.
- ansible-test - Added a work-around for a traceback under Python 3.11 when completing certain command line options.
- ansible-test - Avoid using ``exec`` after container startup when possible. This improves container startup performance and avoids intermittent startup issues with some old containers.
- ansible-test - Connection attempts to managed remote instances no longer abort on ``Permission denied`` errors.
- ansible-test - Detection for running in a Podman or Docker container has been fixed to detect more scenarios. The new detection relies on ``/proc/self/mountinfo`` instead of ``/proc/self/cpuset``. Detection now works with custom cgroups and private cgroup namespaces.
- ansible-test - Fix validate-modules error when retrieving PowerShell argspec when retrieved inside a Cmdlet
- ansible-test - Handle server errors when executing the ``docker info`` command.
- ansible-test - Multiple containers now work under Podman without specifying the ``--docker-network`` option.
- ansible-test - Pass the ``XDG_RUNTIME_DIR`` environment variable through to container commands.
- ansible-test - Perform PyPI proxy configuration after instances are ready and bootstrapping has been completed. Only target instances are affected, as controller instances were already handled this way. This avoids proxy configuration errors when target instances are not yet ready for use.
- ansible-test - Prevent concurrent / repeat inspections of the same container image.
- ansible-test - Prevent concurrent / repeat pulls of the same container image.
- ansible-test - Prevent concurrent execution of cached methods.
- ansible-test - Show the exception type when reporting errors during instance provisioning.
- ansible-test sanity - correctly report invalid YAML in validate-modules (https://github.com/ansible/ansible/issues/75837).
- argument spec validation - again report deprecated parameters for Python-based modules. This was accidentally removed in ansible-core 2.11 when argument spec validation was refactored (https://github.com/ansible/ansible/issues/79680, https://github.com/ansible/ansible/pull/79681).
- argument spec validation - ensure that deprecated aliases in suboptions are also reported (https://github.com/ansible/ansible/pull/79740).
- argument spec validation - fix warning message when two aliases of the same option are used for suboptions to also mention the option's name they are in (https://github.com/ansible/ansible/pull/79740).
- connection local now avoids traceback on invalid user being used to execuet ansible (valid in host, but not in container).
- file - touch action in check mode was always returning ok. Fix now evaluates the different conditions and returns the appropriate changed status. (https://github.com/ansible/ansible/issues/79360)
- get_url - Ensure we are passing ciphers to all url_get calls (https://github.com/ansible/ansible/issues/79717)
- plugin filter now works with rejectlist as documented (still falls back to blacklist if used).
- uri - improve JSON content type detection

amazon.aws
~~~~~~~~~~

- aws_rds - fixes bug in RDS inventory plugin where config file was ignored (https://github.com/ansible-collections/amazon.aws/issues/1304).
- lambda - fix flaky integration test which assumes there are no other lambdas in the account (https://github.com/ansible-collections/amazon.aws/issues/1277)

ansible.posix
~~~~~~~~~~~~~

- Removed contentious terminology to match reference documentation in profile_tasks.
- firewall - Fixed to output a more complete missing library message.
- synchronize - Fixed hosts involved in rsync require the same password

ansible.utils
~~~~~~~~~~~~~

- mac - reorganize regexes to work around 3.11 regex changes. (https://github.com/ansible-collections/ansible.utils/pull/231)

ansible.windows
~~~~~~~~~~~~~~~

- setup - Fallback to using the WMI Win32_Processor provider if the SMBIOS version is too old to return processor core counts
- setup - Fix calculation for ``ansible_processor_threads_per_core`` to reflect the number of threads per core instead of threads per processor
- setup - Ignore processors that are not enabled in the ``ansible_processor_count`` return value
- setup - Support core and thread counts greater than 256 in ``ansible_processor_count`` and ``ansible_processor_threads_per_core``
- win_dns_client - Fix failure to lookup registry DNS servers when it contains null characters
- win_powershell - Support PowerShell 7 script syntax when targeting ``executable: pwsh.exe`` - https://github.com/ansible-collections/ansible.windows/issues/452
- win_wait_for - fix incorrect function name during ``state=drained`` - https://github.com/ansible-collections/ansible.windows/issues/451

chocolatey.chocolatey
~~~~~~~~~~~~~~~~~~~~~

- win_chocolatey - Module fails to execute if powershell version is older than version 5.

cisco.dnac
~~~~~~~~~~

- netconf_credential - Removed to search by username.
- sda_fabric_border_device - fix Create example at EXAMPLES block
- site_intent - fix Case_1 return example at RETURN block
- snmpv2_read_community_credential - Removed to search by username.
- snmpv2_write_community_credential - Removed to search by username.
- swim_intent - fix functionality and tests

cisco.ios
~~~~~~~~~

- ios_acls - fix acl commands order on replaced and overridden state.
- ios_acls - fix eq to process protocol number as protocol name.
- ios_acls - fix object group for extended acls.
- ios_acls - fix parsers to accept precedence value in correct format.
- ios_acls - fix precedence attribute to take a string value as input.
- ios_bgp_address_family - Reorder parsers to generate correct oder of configuration lines.
- ios_bgp_address_family - aliased aggregate_address to aggregate_addresses that supports a list of dict attributes
- ios_bgp_address_family - aliased neighbor to neighbors that supports a list of dict attributes
- ios_bgp_address_family - aliased network to networks that supports a list of dict attributes
- ios_bgp_address_family - fix facts rendering with optimal parsers
- ios_bgp_address_family - fix fliter_list rendering
- ios_bgp_address_family - fix path_attribute to support float parameter
- ios_l2_interfaces - fix command to remove allowed_vlans and pruning_vlans from configuration.
- ios_l2_interfaces - fix dynamic option for mode attribute.
- ios_l2_interfaces - fix state operation for existing vlans.
- ios_l3_interfaces - fix command generation on attribute value being false.
- ios_lag_interfaces - fix deleted state to delete only sub attribute values.
- ios_route_maos - fix replaced state support. (https://github.com/ansible-collections/cisco.ios/issues/680)
- ios_route_maps - fix idempotency for `set community` operations. (https://github.com/ansible-collections/cisco.ios/issues/635)
- ios_route_maps - fix idempotency issues with as-path prepend (https://github.com/ansible-collections/cisco.ios/issues/678)
- ios_route_maps - fix idempotency issues with set community none (https://github.com/ansible-collections/cisco.ios/issues/679
- ios_route_maps - fix merge issues with route-maps where wanted config is not deployed if route map has existing sequence numbers (https://github.com/ansible-collections/cisco.ios/issues/641)
- ios_vlans - Added support for private VLAN configuration
- ios_vrf - fix issue where assigning interfaces to existing vrfs doesn't work (https://github.com/ansible-collections/cisco.ios/issues/707)

cisco.iosxr
~~~~~~~~~~~

- bgp_global -  Fix neighbor description parser issue.

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

- Fix checkmode on merak webhook payload template update
- Resolved issue
- Update pipeline to use newer version of action to detect changed files.
- meraki_alert - Fix situation where specifying emails may crash.
- meraki_mx_site_to_site_vpn - Check mode should no longer apply changes when enabled.
- meraki_webhook - First error when updating URL in a webhook

cisco.mso
~~~~~~~~~

- Fix MSO HTTPAPI plugin login domain issue (#317)
- Fix datetime support for python2.7 in mso_backup_schedule (#323)
- Fix deploymentImmediacy key inconsistency in the API used by mso_schema_site_anp and mso_schema_site_anp_epg (#283)
- Fix mso_schema_template_bd issue when created with unicast_routing as false (#278)
- Fix to be able to add multiple filter and filters with "-" in their names (#306)

community.aws
~~~~~~~~~~~~~

- aws_ssm - fix ``invalid literal for int`` error on some operating systems (https://github.com/ansible-collections/community.aws/issues/113).
- aws_ssm - fixes S3 bucket region detection by ensuring boto client has correct credentials and exists in correct partition (https://github.com/ansible-collections/community.aws/pull/1428).
- aws_ssm - fixes bug with presigned S3 URLs in post-2019 AWS regions (https://github.com/ansible-collections/community.aws/issues/1616).
- ec2_snapshot_copy - including tags caused the erorr "Tag specification resource type must have a value". Fix sets the ResourceType to snapshot to resolve this issue (https://github.com/ansible-collections/community.aws/pull/1419).
- ecs_ecr - fix a ``RepositoryNotFound`` exception when trying to create repositories in check mode (https://github.com/ansible-collections/community.aws/pull/1550).
- ecs_service - respect ``placement_constraints`` for existing ECS services (https://github.com/ansible-collections/community.aws/pull/1601).
- opensearch - Fix cluster creation when using advanced security options (https://github.com/ansible-collections/community.aws/pull/1613).
- s3_lifecycle - module no longer calls ``put_lifecycle_configuration`` if there is no change (https://github.com/ansible-collections/community.aws/issues/1624).
- ssm_parameter - fix a ``KeyError`` when adding a description to an existing parameter (https://github.com/ansible-collections/community.aws/issues/1471).

community.crypto
~~~~~~~~~~~~~~~~

- openssl_csr, openssl_csr_pipe - prevent invalid values for ``crl_distribution_points`` that do not have one of ``full_name``, ``relative_name``, and ``crl_issuer`` (https://github.com/ansible-collections/community.crypto/pull/560).
- openssl_publickey_info - do not crash with internal error when public key cannot be parsed (https://github.com/ansible-collections/community.crypto/pull/551).

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

- docker_api connection plugin - fix error handling when 409 Conflict is returned by the Docker daemon in case of a stopped container (https://github.com/ansible-collections/community.docker/pull/546).
- docker_container - when ``detach=false``, wait indefinitely and not at most one minute. This was the behavior with Docker SDK for Python, and was accidentally changed in 3.0.0 (https://github.com/ansible-collections/community.docker/issues/526, https://github.com/ansible-collections/community.docker/pull/527).
- docker_container_exec - fix error handling when 409 Conflict is returned by the Docker daemon in case of a stopped container (https://github.com/ansible-collections/community.docker/pull/546).
- docker_plugin - do not crash if plugin is installed in check mode (https://github.com/ansible-collections/community.docker/issues/552, https://github.com/ansible-collections/community.docker/pull/553).
- most modules - fix handling of ``DOCKER_TIMEOUT`` environment variable, and improve handling of other fallback environment variables (https://github.com/ansible-collections/community.docker/issues/551, https://github.com/ansible-collections/community.docker/pull/554).

community.general
~~~~~~~~~~~~~~~~~

- ModuleHelper - fix bug when adjusting the name of reserved output variables (https://github.com/ansible-collections/community.general/pull/5755).
- alternatives - support subcommands on Fedora 37, which uses ``follower`` instead of ``slave`` (https://github.com/ansible-collections/community.general/pull/5794).
- ansible_galaxy_install - set default to raise exception if command's return code is different from zero (https://github.com/ansible-collections/community.general/pull/5680).
- ansible_galaxy_install - try ``C.UTF-8`` and then fall back to ``en_US.UTF-8`` before failing (https://github.com/ansible-collections/community.general/pull/5680).
- bitwarden lookup plugin - clarify what to do, if the bitwarden vault is not unlocked (https://github.com/ansible-collections/community.general/pull/5811).
- dig lookup plugin - correctly handle DNSKEY record type's ``algorithm`` field (https://github.com/ansible-collections/community.general/pull/5914).
- gem - fix force parameter not being passed to gem command when uninstalling (https://github.com/ansible-collections/community.general/pull/5822).
- gem - fix hang due to interactive prompt for confirmation on specific version uninstall (https://github.com/ansible-collections/community.general/pull/5751).
- gitlab_deploy_key - also update ``title`` and not just ``can_push`` (https://github.com/ansible-collections/community.general/pull/5888).
- gitlab_group_variables - fix dropping variables accidentally when GitLab introduced new properties (https://github.com/ansible-collections/community.general/pull/5667).
- gitlab_project_variables - fix dropping variables accidentally when GitLab introduced new properties (https://github.com/ansible-collections/community.general/pull/5667).
- keycloak_user_federation - fixes federation creation issue. When a new federation was created and at the same time a default / standard mapper was also changed / updated the creation process failed as a bad None set variable led to a bad malformed url request (https://github.com/ansible-collections/community.general/pull/5750).
- keycloak_user_federation - fixes idempotency detection issues. In some cases the module could fail to properly detect already existing user federations because of a buggy seemingly superflous extra query parameter (https://github.com/ansible-collections/community.general/pull/5732).
- loganalytics callback plugin - adjust type of callback to ``notification``, it was incorrectly classified as ``aggregate`` before (https://github.com/ansible-collections/community.general/pull/5761).
- logdna callback plugin - adjust type of callback to ``notification``, it was incorrectly classified as ``aggregate`` before (https://github.com/ansible-collections/community.general/pull/5761).
- logstash callback plugin - adjust type of callback to ``notification``, it was incorrectly classified as ``aggregate`` before (https://github.com/ansible-collections/community.general/pull/5761).
- lxc_container - fix the arguments of the lxc command which broke the creation and cloning of containers (https://github.com/ansible-collections/community.general/issues/5578).
- nsupdate - fix zone lookup. The SOA record for an existing zone is returned as an answer RR and not as an authority RR (https://github.com/ansible-collections/community.general/issues/5817, https://github.com/ansible-collections/community.general/pull/5818).
- opkg - fix issue that ``force=reinstall`` would not reinstall an existing package (https://github.com/ansible-collections/community.general/pull/5705).
- proxmox_disk - fixed issue with read timeout on import action (https://github.com/ansible-collections/community.general/pull/5803).
- proxmox_disk - fixed possible issues with redundant ``vmid`` parameter (https://github.com/ansible-collections/community.general/issues/5492, https://github.com/ansible-collections/community.general/pull/5672).
- proxmox_nic - fixed possible issues with redundant ``vmid`` parameter (https://github.com/ansible-collections/community.general/issues/5492, https://github.com/ansible-collections/community.general/pull/5672).
- redfish_utils - removed basic auth HTTP header when performing a GET on the service root resource and when performing a POST to the session collection (https://github.com/ansible-collections/community.general/issues/5886).
- splunk callback plugin - adjust type of callback to ``notification``, it was incorrectly classified as ``aggregate`` before (https://github.com/ansible-collections/community.general/pull/5761).
- sumologic callback plugin - adjust type of callback to ``notification``, it was incorrectly classified as ``aggregate`` before (https://github.com/ansible-collections/community.general/pull/5761).
- syslog_json callback plugin - adjust type of callback to ``notification``, it was incorrectly classified as ``aggregate`` before (https://github.com/ansible-collections/community.general/pull/5761).
- terraform - fix ``current`` workspace never getting appended to the ``all`` key in the ``workspace_ctf`` object (https://github.com/ansible-collections/community.general/pull/5735).
- terraform - fix ``terraform init`` failure when there are multiple workspaces on the remote backend and when ``default`` workspace is missing by setting ``TF_WORKSPACE`` environmental variable to the value of ``workspace`` when used (https://github.com/ansible-collections/community.general/pull/5735).
- terraform module - disable ANSI escape sequences during validation phase (https://github.com/ansible-collections/community.general/pull/5843).
- unixy callback plugin - fix typo introduced when updating to use Ansible's configuration manager for handling options (https://github.com/ansible-collections/community.general/issues/5600).
- xml - fixed a bug where empty ``children`` list would not be set (https://github.com/ansible-collections/community.general/pull/5808).

community.postgresql
~~~~~~~~~~~~~~~~~~~~

- postgresql_pg_hba - fix ``changed`` return value for when ``overwrite`` is enabled (https://github.com/ansible-collections/community.postgresql/pull/378).
- postgresql_privs - fix quoting of the ``schema`` parameter in SQL statements (https://github.com/ansible-collections/community.postgresql/pull/382).
- postgresql_privs - raise an error when the ``objs: ALL_IN_SCHEMA`` is used with a value of ``type`` that is not ``table``, ``sequence``, ``function`` or ``procedure`` (https://github.com/ansible-collections/community.postgresql/issues/379).

community.proxysql
~~~~~~~~~~~~~~~~~~

- proxysql_manage_config - Fix ``check_mode`` (https://github.com/ansible-collections/community.proxysql/pull/138).
- proxysql_query_rules_fast_routing - fix query parameter order, that prevents updating ``destination_hostgroup`` parameter (https://github.com/ansible-collections/community.proxysql/pull/108).
- proxysql_query_rules_fast_routing - remove unnecessary ``flagIN`` check, that makes it impossible to update the ``destination_hostgroup`` parameter (https://github.com/ansible-collections/community.proxysql/pull/108).
- roles/proxysql - Fix wait_for task when `proxysql_admin_bind_address` is overridden (https://github.com/ansible-collections/community.proxysql/pull/115).
- roles/proxysql - Missing proxysql_global_variables module parameters (https://github.com/ansible-collections/community.proxysql/pull/116).

community.routeros
~~~~~~~~~~~~~~~~~~

- api_modify - do not use ``name`` as a unique key in ``ip dns static`` (https://github.com/ansible-collections/community.routeros/issues/141).
- api_modify, api_info - defaults corrected for fields in ``interface wireguard peers`` API path (https://github.com/ansible-collections/community.routeros/pull/144).
- api_modify, api_info - do not crash if router contains ``regexp`` DNS entries in ``ip dns static`` (https://github.com/ansible-collections/community.routeros/issues/141).

community.vmware
~~~~~~~~~~~~~~~~

- vmware_cluster_dpm - Fix an issue that the slider and the values of the host_power_action_rate works invertet in the vCenter
- vmware_cluster_drs - Fix drs_vmotion_rate so that the value corresponds to the vCenter UI. Previously, choosing 1 / 2 configured a migration threshold of 5 / 4 and vice versa (https://github.com/ansible-collections/community.vmware/pull/1542).
- vmware_guest - Fix check mode (https://github.com/ansible-collections/community.vmware/issues/1272).
- vmware_host_lockdown_exceptions - Avoid setting exception users to what they already are (https://github.com/ansible-collections/community.vmware/pull/1585).
- vmware_tools - Fix an issue with pyVmomi 8.0.0.1 (https://github.com/ansible-collections/community.vmware/issues/1578).

community.windows
~~~~~~~~~~~~~~~~~

- win_firewall_rule - fix problem in check mode with multiple ip addresses not in same order
- win_partition - fix problem in auto assigning a drive letter should the user use either a, u, t or o as a drive letter

community.zabbix
~~~~~~~~~~~~~~~~

- all modules - remove deprecation warnings for modules parameters related to zabbix-api when these parapmeters are not explicetely defined
- all roles and modules integration tests - replace deprecated include module whith include_tasks
- zabbix_agent, zabbix_proxy roles, all modules - make httpapi connection work with HTTP Basic Authorization
- zabbix_proxy - do not set ServerPort config parameter which was removed in Zabbix 6.0
- zabbix_server role Debian.yml task - remove warn: arg for shell module as the arg is deprecated since ansible-core above 2.13
- zabbix_user_role module - creation of a User Role with Super Admin type

f5networks.f5_modules
~~~~~~~~~~~~~~~~~~~~~

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

fortinet.fortios
~~~~~~~~~~~~~~~~

- Add required field for module log_fact;
- Fix runtime issue (#214);
- Fix sanity test errors in validate-modules test;

google.cloud
~~~~~~~~~~~~

- Disk has been fixed to send the sourceSnapshot parameter.
- fix `gcp_compute` no longer being a valid name of the inventory plugin
- fix collection to work with Python 2.7
- gcp_cloudtasks_queue - was not functional before, and is now functional.
- gcp_compute_* - these resources use the correct selflink (www.googleapis.com) as the domain, no longer erroneously reporting changes after an execution.
- gcp_compute_backend_service - no longer erroneously reports changes after an execution for ``capacity_scaler``.
- gcp_container_cluster - support GKE clusters greater than 1.19+, which cannot use basic-auth.
- gcp_crypto_key - skip_initial_version_creation defaults to the correct value.
- gcp_iam_role - now properly undeletes and recognizes soft deleted roles as absent.
- gcp_iam_role - update of a role is functional (GitHub
- gcp_spanner_database - recognize a non-existent resource as absent.
- gcp_storage_object - fix for correct version of dependency requirement.

hetzner.hcloud
~~~~~~~~~~~~~~

- hcloud_server - externally attached networks (using hcloud_server_network) were removed when not specified in the hcloud_server resource

lowlydba.sqlserver
~~~~~~~~~~~~~~~~~~

- Fixes to incorrect variable reference in Login module (https://github.com/lowlydba/lowlydba.sqlserver/pull/161)

netapp.ontap
~~~~~~~~~~~~

- na_ontap_active_directory - updated doc as only ZAPI is supported at present, force an error with use_rest always.
- na_ontap_aggregate - allow adding disks before trying to offline aggregate.
- na_ontap_aggregate - fix ``service_state`` option skipped if its set to offline in create.
- na_ontap_cg_snapshot - updated doc with deprecation warning as it is a ZAPI only module.
- na_ontap_cifs_server - fix ``service_state`` is stopped when trying to modify cifs server in REST.
- na_ontap_file_directory_policy - updated doc with deprecation warning as it is a ZAPI only module.
- na_ontap_file_security_permissions - updated notes to indicate ONTAP 9.9.1 or later is required.
- na_ontap_file_security_permissions_acl - updated notes to indicate ONTAP 9.9.1 or later is required.
- na_ontap_interface - fix cannot set ``location.node.name`` and ``location.home_node.name`` error when creating or modifying fc interface.
- na_ontap_interface - fix unexpected argument error with ``ipspace`` when trying to get fc interface.
- na_ontap_qtree - fix cannot get current qtree if enclosed in curly braces.
- na_ontap_quota_policy - updated doc with deprecation warning as it is a ZAPI only module.
- na_ontap_quotas - fix default tree quota rule gets modified when ``quota_target`` is set in REST.
- na_ontap_quotas - fix duplicate entry error when trying to add quota rule in REST.
- na_ontap_quotas - fix entry does not exist error when trying to modify quota status in REST.
- na_ontap_quotas - fix user/group quota rule without qtree gets modified when ``qtree`` is set.
- na_ontap_security_ipsec_policy - fix KeyError on ``authentication_method``.
- na_ontap_security_ipsec_policy - fix cannot get current security IPsec policy with ipspace.
- na_ontap_security_key_manager - requires 9.7+ to work with REST.
- na_ontap_snapmirror_policy - deleting all retention rules would trigger an error when the existing policy requires at least one rule.
- na_ontap_snapmirror_policy - fix desired policy type not configured in cli with REST.
- na_ontap_snapmirror_policy - fixed idempotency issue on ``identity_preservation`` option when using REST.
- na_ontap_snapmirror_policy - index error on rules with ONTAP 9.12.1 as not all fields are present.
- na_ontap_svm_options - updated doc with deprecation warning as it is a ZAPI only module.
- na_ontap_volume -- fixed bug preventing unmount and taking a volume off line at the same time

netapp_eseries.santricity
~~~~~~~~~~~~~~~~~~~~~~~~~

- netapp_eseries.santricity.na_santricity_mgmt_interface - Add the ability to configure DNS, NTP and SSH separately from management interfaces.
- netapp_eseries.santricity.nar_santricity_host - Fix default MTU value for NVMe RoCE.
- netapp_eseries.santricity.nar_santricity_management - Add tasks to set DNS, NTP and SSH globally separately from management interfaces.

netbox.netbox
~~~~~~~~~~~~~

- nb_inventory - Raise exception on missing packaging [#900](https://github.com/netbox-community/ansible_modules/pull/900)

ngine_io.vultr
~~~~~~~~~~~~~~

- iventory - Fixed ``allowed_bandwidth_gb`` to be returned as float (https://github.com/ngine-io/ansible-collection-vultr/pull/35).
- vultr_server - Fixed ``allowed_bandwidth_gb`` to be returned as float (https://github.com/ngine-io/ansible-collection-vultr/pull/35).
- vultr_server_baremetal - Fixed ``allowed_bandwidth_gb`` to be returned as float (https://github.com/ngine-io/ansible-collection-vultr/pull/35).

purestorage.flasharray
~~~~~~~~~~~~~~~~~~~~~~

- purefa - Remove unneeded REST version check as causes issues with REST mismatches
- purefa_ds - Fixed dict syntax error
- purefa_info - Fiexed issue with DNS reporting in Purity//FA 6.4.0 with non-FA-File system
- purefa_info - Fixed error in policies subsection due to API issue
- purefa_info - Fixed race condition with protection groups
- purefa_smtp - Fix parameter name
- purefa_volume - Fixed issue with promotion status not being called correctly

purestorage.fusion
~~~~~~~~~~~~~~~~~~

- fusion_pg - Add missing 'region' parameter
- fusion_tn - Add missing 'region' parameter

theforeman.foreman
~~~~~~~~~~~~~~~~~~

- activation_key - properly fetch *all* repositories when managing content overrides (https://bugzilla.redhat.com/show_bug.cgi?id=2134605)
- redhat_manifest - properly report http errors (https://github.com/theforeman/foreman-ansible-modules/issues/1497)
- repository_sync - report an error instead of syncing the whole product when the repository could not be found

vultr.cloud
~~~~~~~~~~~

- instance - An error that caused the start script not to be processed has been fixed. (https://github.com/vultr/ansible-collection-vultr/issues/49)
- instance_info - The problem that the module was missing in the runtime action group has been fixed.

Known Issues
------------

Ansible-core
~~~~~~~~~~~~

- ansible-test - Additional configuration may be required for certain container host and container combinations. Further details are available in the testing documentation.
- ansible-test - Custom containers with ``VOLUME`` instructions may be unable to start, when previously the containers started correctly. Remove the ``VOLUME`` instructions to resolve the issue. Containers with this condition will cause ``ansible-test`` to emit a warning.
- ansible-test - Systems with Podman networking issues may be unable to run containers, when previously the issue went unreported. Correct the networking issues to continue using ``ansible-test`` with Podman.
- ansible-test - Using Docker on systems with SELinux may require setting SELinux to permissive mode. Podman should work with SELinux in enforcing mode.

cisco.meraki
~~~~~~~~~~~~

- meraki_network - Updated documentation for `local_status_page_enabled` and `remote_status_page_enabled` as these no longer work.

New Plugins
-----------

Filter
~~~~~~

- community.crypto.openssl_csr_info - Retrieve information from OpenSSL Certificate Signing Requests (CSR)
- community.crypto.openssl_privatekey_info - Retrieve information from OpenSSL private keys
- community.crypto.openssl_publickey_info - Retrieve information from OpenSSL public keys in PEM format
- community.crypto.split_pem - Split PEM file contents into multiple objects
- community.crypto.x509_certificate_info - Retrieve information from X.509 certificates in PEM format
- community.crypto.x509_crl_info - Retrieve information from X.509 CRLs in PEM format

Inventory
~~~~~~~~~

- vultr.cloud.vultr - Retrieves list of instances via Vultr v2 API

Lookup
~~~~~~

- community.hashi_vault.vault_list - Perform a list operation against HashiCorp Vault

New Modules
-----------

community.docker
~~~~~~~~~~~~~~~~

- community.docker.docker_container_copy_into - Copy a file into a Docker container

community.general
~~~~~~~~~~~~~~~~~

- community.general.ocapi_command - Manages Out-Of-Band controllers using Open Composable API (OCAPI)
- community.general.ocapi_info - Manages Out-Of-Band controllers using Open Composable API (OCAPI)

community.hashi_vault
~~~~~~~~~~~~~~~~~~~~~

- community.hashi_vault.vault_list - Perform a list operation against HashiCorp Vault

community.hrobot
~~~~~~~~~~~~~~~~

- community.hrobot.v_switch - Manage Hetzner's vSwitch

community.vmware
~~~~~~~~~~~~~~~~

- community.vmware.vmware_guest_vgpu_info - Gather information about vGPU profiles of the specified virtual machine in the given vCenter infrastructure

ibm.spectrum_virtualize
~~~~~~~~~~~~~~~~~~~~~~~

- ibm.spectrum_virtualize.ibm_sv_manage_awss3_cloudaccount - Manages AWS cloud account configuration on Spectrum Virtualize systems
- ibm.spectrum_virtualize.ibm_sv_manage_cloud_backups - Manages cloud backup on Spectrum Virtualize systems
- ibm.spectrum_virtualize.ibm_sv_restore_cloud_backup - Allows user to restore an existing cloud backup on Spectrum Virtualize systems

lowlydba.sqlserver
~~~~~~~~~~~~~~~~~~

- lowlydba.sqlserver.credential - Configures a credential on a SQL server

netapp.ontap
~~~~~~~~~~~~

- netapp.ontap.na_ontap_cifs_local_group - NetApp Ontap - create, delete or modify CIFS local group.
- netapp.ontap.na_ontap_cifs_local_user - NetApp ONTAP local CIFS user.
- netapp.ontap.na_ontap_security_ipsec_ca_certificate - NetApp ONTAP module to add or delete ipsec ca certificate.
- netapp.ontap.na_ontap_security_ipsec_config - NetApp ONTAP module to configure IPsec config.
- netapp.ontap.na_ontap_security_ipsec_policy - NetApp ONTAP module to create, modify or delete security IPsec policy.

netbox.netbox
~~~~~~~~~~~~~

- netbox.netbox.netbox_inventory_item_role - Create, update or delete inventory item roles in NetBox
- netbox.netbox.netbox_module_type - Create, update or delete module types in NetBox
- netbox.netbox.netbox_service_template - Create, update or delete service templates in NetBox

purestorage.flasharray
~~~~~~~~~~~~~~~~~~~~~~

- purestorage.flasharray.purefa_snmp_agent - Configure the FlashArray SNMP Agent

theforeman.foreman
~~~~~~~~~~~~~~~~~~

- theforeman.foreman.snapshot_info - Fetch information about Foreman Snapshots

vultr.cloud
~~~~~~~~~~~

- vultr.cloud.instance_info - Get information about the Vultr instances
- vultr.cloud.snapshot - Manages snapshots on Vultr
- vultr.cloud.snapshot_info - Gather information about the Vultr snapshots

Unchanged Collections
---------------------

- ansible.netcommon (still version 4.1.0)
- arista.eos (still version 6.0.0)
- azure.azcollection (still version 1.14.0)
- check_point.mgmt (still version 4.0.0)
- cisco.aci (still version 2.3.0)
- cisco.asa (still version 4.0.0)
- cisco.nso (still version 1.0.3)
- cisco.nxos (still version 4.0.1)
- cisco.ucs (still version 1.8.0)
- cloud.common (still version 2.1.2)
- community.azure (still version 2.0.0)
- community.ciscosmb (still version 1.0.5)
- community.fortios (still version 1.0.0)
- community.google (still version 1.0.0)
- community.grafana (still version 1.5.3)
- community.libvirt (still version 1.2.0)
- community.mongodb (still version 1.4.2)
- community.mysql (still version 3.5.1)
- community.network (still version 5.0.0)
- community.okd (still version 2.2.0)
- community.rabbitmq (still version 1.2.3)
- community.sap (still version 1.0.0)
- community.sap_libs (still version 1.4.0)
- community.skydive (still version 1.0.0)
- containers.podman (still version 1.10.1)
- cyberark.conjur (still version 1.2.0)
- dellemc.enterprise_sonic (still version 2.0.0)
- dellemc.openmanage (still version 6.3.0)
- dellemc.os10 (still version 1.1.1)
- dellemc.os6 (still version 1.0.7)
- dellemc.os9 (still version 1.0.4)
- fortinet.fortimanager (still version 2.1.7)
- frr.frr (still version 2.0.0)
- gluster.gluster (still version 1.0.2)
- grafana.grafana (still version 1.1.0)
- hpe.nimble (still version 1.1.4)
- ibm.qradar (still version 2.1.0)
- infinidat.infinibox (still version 1.3.12)
- infoblox.nios_modules (still version 1.4.1)
- inspur.ispim (still version 1.2.0)
- inspur.sm (still version 2.3.0)
- junipernetworks.junos (still version 4.1.0)
- kubernetes.core (still version 2.3.2)
- mellanox.onyx (still version 1.0.0)
- netapp.aws (still version 21.7.0)
- netapp.azure (still version 21.10.0)
- netapp.elementsw (still version 21.7.0)
- netapp.storagegrid (still version 21.11.1)
- netapp.um_info (still version 21.8.0)
- ngine_io.cloudstack (still version 2.3.0)
- ngine_io.exoscale (still version 1.0.0)
- openstack.cloud (still version 1.10.0)
- openvswitch.openvswitch (still version 2.1.0)
- ovirt.ovirt (still version 2.4.1)
- purestorage.flashblade (still version 1.10.0)
- splunk.es (still version 2.1.0)
- vmware.vmware_rest (still version 2.2.0)
- vyos.vyos (still version 4.0.0)
- wti.remote (still version 1.0.4)

v7.1.0
======

.. contents::
  :local:
  :depth: 2

Release Summary
---------------

Release Date: 2022-12-07

`Porting Guide <https://docs.ansible.com/ansible/devel/porting_guides.html>`_

Added Collections
-----------------

- grafana.grafana (version 1.1.0)

Ansible-core
------------

Ansible 7.1.0 contains Ansible-core version 2.14.1.
This is a newer version than version 2.14.0 contained in the previous Ansible release.

The changes are reported in the combined changelog below.

Changed Collections
-------------------

If not mentioned explicitly, the changes are reported in the combined changelog below.

+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| Collection             | Ansible 7.0.0 | Ansible 7.1.0 | Notes                                                                                                                        |
+========================+===============+===============+==============================================================================================================================+
| ansible.utils          | 2.7.0         | 2.8.0         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| awx.awx                | 21.8.0        | 21.10.0       | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.dnac             | 6.6.0         | 6.6.1         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.intersight       | 1.0.20        | 1.0.22        | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.iosxr            | 4.0.2         | 4.0.3         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.meraki           | 2.11.0        | 2.13.0        |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.nxos             | 4.0.0         | 4.0.1         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cloudscale_ch.cloud    | 2.2.2         | 2.2.3         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.crypto       | 2.8.1         | 2.9.0         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.dns          | 2.4.1         | 2.4.2         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.docker       | 3.2.1         | 3.3.1         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.general      | 6.0.1         | 6.1.0         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.postgresql   | 2.3.0         | 2.3.1         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.routeros     | 2.3.1         | 2.5.0         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.sap_libs     | 1.3.0         | 1.4.0         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.sops         | 1.4.1         | 1.5.0         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.vmware       | 3.1.0         | 3.2.0         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.zabbix       | 1.8.0         | 1.9.0         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| containers.podman      | 1.9.4         | 1.10.1        |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| f5networks.f5_modules  | 1.20.0        | 1.21.0        |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| fortinet.fortios       | 2.1.7         | 2.2.1         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| grafana.grafana        |               | 1.1.0         | The collection was added to Ansible                                                                                          |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| hetzner.hcloud         | 1.8.2         | 1.9.0         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| infinidat.infinibox    | 1.3.7         | 1.3.12        | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| infoblox.nios_modules  | 1.4.0         | 1.4.1         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| junipernetworks.junos  | 4.0.0         | 4.1.0         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| lowlydba.sqlserver     | 1.0.4         | 1.2.1         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| netbox.netbox          | 3.8.1         | 3.9.0         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| ngine_io.cloudstack    | 2.2.4         | 2.3.0         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| ovirt.ovirt            | 2.3.1         | 2.4.1         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| purestorage.flasharray | 1.14.0        | 1.15.0        |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| purestorage.fusion     | 1.1.1         | 1.2.0         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+

Major Changes
-------------

cisco.meraki
~~~~~~~~~~~~

- meraki_mr_l7_firewall - New module
- meraki_webhook_payload_template - New module

community.zabbix
~~~~~~~~~~~~~~~~

- all modules are opting away from zabbix-api and using httpapi ansible.netcommon plugin. We will support zabbix-api for backwards compatibility until next major release. See our README.md for more information about how to migrate
- zabbix_agent and zabbix_proxy roles are opting away from zabbix-api and use httpapi ansible.netcommon plugin. We will support zabbix-api for backwards compatibility until next major release. See our README.md for more information about how to migrate

containers.podman
~~~~~~~~~~~~~~~~~

- New become plugin - podman_unshare
- Podman generate systemd module

fortinet.fortios
~~~~~~~~~~~~~~~~

- Support FortiOS v7.0.6, v7.0.7, v7.0.8, v7.2.1, v7.2.2.

Minor Changes
-------------

Ansible-core
~~~~~~~~~~~~

- ansible-test - Improve consistency of executed ``pylint`` commands by making the plugins ordered.

ansible.utils
~~~~~~~~~~~~~

- to_xml - Added support for using spaces to indent an XML doc via a new `indent` parameter.

cloudscale_ch.cloud
~~~~~~~~~~~~~~~~~~~

- Fixed a typo in region code.
- Fixed various documentation typos.
- Streamlined the flavors to the new format ``flex-y-x`` across the related modules and tests.

community.crypto
~~~~~~~~~~~~~~~~

- x509_certificate_info - adds ``issuer_uri`` field in return value based on Authority Information Access data (https://github.com/ansible-collections/community.crypto/pull/530).

community.docker
~~~~~~~~~~~~~~~~

- current_container_facts - make work with current Docker version, also support Podman (https://github.com/ansible-collections/community.docker/pull/510).
- docker_image - when using ``archive_path``, detect whether changes are necessary based on the image ID (hash). If the existing tar archive matches the source, do nothing. Previously, each task execution re-created the archive (https://github.com/ansible-collections/community.docker/pull/500).

community.general
~~~~~~~~~~~~~~~~~

- cmd_runner module utils - ``cmd_runner_fmt.as_bool()`` can now take an extra parameter to format when value is false (https://github.com/ansible-collections/community.general/pull/5647).
- gconftool2 - refactor using ``ModuleHelper`` and ``CmdRunner`` (https://github.com/ansible-collections/community.general/pull/5545).
- java_certs - add more detailed error output when extracting certificate from PKCS12 fails (https://github.com/ansible-collections/community.general/pull/5550).
- jenkins_plugin - refactor code to module util to fix sanity check (https://github.com/ansible-collections/community.general/pull/5565).
- lxd_project - refactored code out to module utils to clear sanity check (https://github.com/ansible-collections/community.general/pull/5549).
- nmap inventory plugin - add new options ``udp_scan``, ``icmp_timestamp``, and ``dns_resolve`` for different types of scans (https://github.com/ansible-collections/community.general/pull/5566).
- rax_scaling_group - refactored out code to the ``rax`` module utils to clear the sanity check (https://github.com/ansible-collections/community.general/pull/5563).
- redfish_command - add ``PerformRequestedOperations`` command to perform any operations necessary to continue the update flow (https://github.com/ansible-collections/community.general/issues/4276).
- redfish_command - add ``update_apply_time`` to ``SimpleUpdate`` command (https://github.com/ansible-collections/community.general/issues/3910).
- redfish_command - add ``update_status`` to output of ``SimpleUpdate`` command to allow a user monitor the update in progress (https://github.com/ansible-collections/community.general/issues/4276).
- redfish_info - add ``GetUpdateStatus`` command to check the progress of a previous update request (https://github.com/ansible-collections/community.general/issues/4276).
- redfish_utils module utils - added PUT (``put_request()``) functionality (https://github.com/ansible-collections/community.general/pull/5490).
- slack - add option ``prepend_hash`` which allows to control whether a ``#`` is prepended to ``channel_id``. The current behavior (value ``auto``) is to prepend ``#`` unless some specific prefixes are found. That list of prefixes is incomplete, and there does not seem to exist a documented condition on when exactly ``#`` must not be prepended. We recommend to explicitly set ``prepend_hash=always`` or ``prepend_hash=never`` to avoid any ambiguity (https://github.com/ansible-collections/community.general/pull/5629).
- spotinst_aws_elastigroup - add ``elements`` attribute when missing in ``list`` parameters (https://github.com/ansible-collections/community.general/pull/5553).
- ssh_config - add ``host_key_algorithms`` option (https://github.com/ansible-collections/community.general/pull/5605).
- udm_share - added ``elements`` attribute to ``list`` type parameters (https://github.com/ansible-collections/community.general/pull/5557).
- udm_user - add ``elements`` attribute when missing in ``list`` parameters (https://github.com/ansible-collections/community.general/pull/5559).

community.routeros
~~~~~~~~~~~~~~~~~~

- api* modules - Add new option ``force_no_cert`` to connect with ADH ciphers (https://github.com/ansible-collections/community.routeros/pull/124).
- api_info - new parameter ``include_builtin`` which allows to include "builtin" entries that are automatically generated by ROS and cannot be modified by the user (https://github.com/ansible-collections/community.routeros/pull/130).
- api_info, api_modify - support API paths ``interface ethernet poe``, ``interface gre6``, ``interface vrrp`` and also support all previously missing fields of entries in ``ip dhcp-server`` (https://github.com/ansible-collections/community.routeros/pull/137).
- api_modify, api_info - support API paths - ``interface bonding``, ``interface bridge mlag``, ``ipv6 firewall mangle``, ``ipv6 nd``, ``system scheduler``, ``system script``, ``system ups`` (https://github.com/ansible-collections/community.routeros/pull/133).
- api_modify, api_info - support API paths ``caps-man access-list``, ``caps-man configuration``, ``caps-man datapath``, ``caps-man manager``, ``caps-man provisioning``, ``caps-man security`` (https://github.com/ansible-collections/community.routeros/pull/126).
- api_modify, api_info - support API paths ``interface list`` and ``interface list member`` (https://github.com/ansible-collections/community.routeros/pull/120).
- api_modify, api_info - support API paths ``interface pppoe-client``, ``interface vlan``, ``interface bridge``, ``interface bridge vlan`` (https://github.com/ansible-collections/community.routeros/pull/125).
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

community.sops
~~~~~~~~~~~~~~

- Automatically install GNU Privacy Guard (GPG) in execution environments. To install Mozilla sops a manual step needs to be added to the EE definition, see the collection's documentation for details (https://github.com/ansible-collections/community.sops/pull/98).

community.vmware
~~~~~~~~~~~~~~~~

- vmware_guest - Add sub-option to configure virtual performance counters (https://github.com/ansible-collections/community.vmware/issues/1511).
- vmware_guest - Adding sub-options to configure CPU and memory shares (https://github.com/ansible-collections/community.vmware/issues/356).
- vmware_guest_boot_manager - Add a new parameter boot_hdd_name to specify the boot disk name(https://github.com/ansible-collections/community.vmware/pull/1543).
- vmware_guest_custom_attributes - Improve the code quality and added the return value for diff(https://github.com/ansible-collections/community.vmware/pull/1532).
- vmware_vm_info - Adding resource pool of the VM to result (https://github.com/ansible-collections/community.vmware/pull/1551).

community.zabbix
~~~~~~~~~~~~~~~~

- ansible_zabbix_url_path introduced to be able to specify non-default Zabbix WebUI path, e.g. http://<FQDN>/zabbixeu
- collection now supports creating ``module_defaults`` for ``group/community.zabbix.zabbix`` (see https://github.com/ansible-collections/community.zabbix/issues/326)
- fixed ``zabbix_server`` role failure running in check_mode (see https://github.com/ansible-collections/community.zabbix/issues/804)
- zabbix_agent - give Zabbix Agent access to the Linux DMI table allowing system.hw.chassis info to populate.
- zabbix_template - add support for template tags
- zabbix_user_role module added
- zabbix_web - add support for Ubuntu 22.04 jammy

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

hetzner.hcloud
~~~~~~~~~~~~~~

- dynamic inventory - add support changing the name of the top level group all servers are added to
- hcloud_firewall - add support for esp and gre protocols

infoblox.nios_modules
~~~~~~~~~~~~~~~~~~~~~

- Fix to allocate ip to a_record dynamically `#163 <https://github.com/infobloxopen/infoblox-ansible/pull/163>`_
- Fix to camelcase issue for updating 'nios_network_view' name `#163 <https://github.com/infobloxopen/infoblox-ansible/pull/163>`_
- Fix to changelog yaml file with linting issues `#161 <https://github.com/infobloxopen/infoblox-ansible/pull/161>`_
- Fix to specify network_view in lookup modules to return absolute network and ip `#157 <https://github.com/infobloxopen/infoblox-ansible/pull/157>`_
- Fix to update 'nios_a_record' name with multiple ips having same name `#164 <https://github.com/infobloxopen/infoblox-ansible/pull/164>`_

junipernetworks.junos
~~~~~~~~~~~~~~~~~~~~~

- Implement file_size as string.
- Used xmltodict to gather the sub-module chassis list and return it as a dictionary.

lowlydba.sqlserver
~~~~~~~~~~~~~~~~~~

- Fixed typo in the traceflag module's documentation. (https://github.com/lowlydba/lowlydba.sqlserver/pull/150)
- Return "RestartRequired" when a module performs changes that require an addition service restart to take effect. (https://github.com/lowlydba/lowlydba.sqlserver/pull/150/)
- modules - all modules now document their platform and support for check mode in their attributes documentation (https://github.com/lowlydba/lowlydba.sqlserver/pull/134).

netbox.netbox
~~~~~~~~~~~~~

- nb_lookup - Add 3.3 endpoints for lookup [#865](https://github.com/netbox-community/ansible_modules/pull/865)
- netbox_console_server and netbox_console_server_port - Add new field [#866](https://github.com/netbox-community/ansible_modules/pull/866)
- netbox_device_bay - Add label [#868](https://github.com/netbox-community/ansible_modules/pull/868)
- netbox_l2vpn - Add module [#846](https://github.com/netbox-community/ansible_modules/pull/846)

ngine_io.cloudstack
~~~~~~~~~~~~~~~~~~~

- cs_instance - The arguments ``cpu``, ``cpu_speed`` and ``memory`` are no longer required to be set together (https://github.com/ngine-io/ansible-collection-cloudstack/issues/111).
- cs_instance - The optional arguments ``pod`` and ``cluster`` has been added.

purestorage.flasharray
~~~~~~~~~~~~~~~~~~~~~~

- purefa_network - Added support for servicelist updates
- purefa_vlan - Extend VLAN support to cover NVMe-RoCE and file interfaces

purestorage.fusion
~~~~~~~~~~~~~~~~~~

- fusion_info - Added API Client information

Deprecated Features
-------------------

community.general
~~~~~~~~~~~~~~~~~

- The ``sap`` modules ``sapcar_extract``, ``sap_task_list_execute``, and ``hana_query``, will be removed from this collection in community.general 7.0.0 and replaced with redirects to ``community.sap_libs``. If you want to continue using these modules, make sure to also install ``community.sap_libs`` (it is part of the Ansible package) (https://github.com/ansible-collections/community.general/pull/5614).

Bugfixes
--------

Ansible-core
~~~~~~~~~~~~

- Fixes leftover _valid_attrs usage.
- ansible-galaxy - make initial call to Galaxy server on-demand only when installing, getting info about, and listing roles.
- copy module will no longer move 'non files' set as src when remote_src=true.
- display - reduce risk of post-fork output deadlocks (https://github.com/ansible/ansible/pull/79522)
- jinja2_native: preserve quotes in strings (https://github.com/ansible/ansible/issues/79083)
- updated error messages to include 'acl' and not just mode changes when failing to set required permissions on remote.

ansible.utils
~~~~~~~~~~~~~

- Accept int input for ipaddr filters.

cisco.dnac
~~~~~~~~~~

- DNA Center credentials can now be exported and used as env vars.
- sda_virtual_network_ip_pool - Now pass the site_name_hierarchy correctly in get method.

cisco.iosxr
~~~~~~~~~~~

- Fix issue of iosxr_config parellel uploads.
- Support commit confirmed functionality with replace option.

cisco.meraki
~~~~~~~~~~~~

- Update defaults in documentation for new sanity tests
- meraki_device - Fix URL for LLDP and CDP lookups

cisco.nxos
~~~~~~~~~~

- `nxos_acls` - Parse ICMP echo-reply and echo options correctly (https://github.com/ansible-collections/cisco.nxos/issues/583).
- `nxos_acls` - Parse ICMP port-unreachable and unreachable options correctly (https://github.com/ansible-collections/cisco.nxos/issues/529).
- `nxos_acls` - Parse port-protocol options with hypenated names correctly (https://github.com/ansible-collections/cisco.nxos/issues/557).

community.dns
~~~~~~~~~~~~~

- Update Public Suffix List.

community.docker
~~~~~~~~~~~~~~~~

- current_container_facts - make container detection work better in more cases (https://github.com/ansible-collections/community.docker/pull/522).
- docker_container - the ``kill_signal`` option erroneously did not accept strings anymore since 3.0.0 (https://github.com/ansible-collections/community.docker/issues/505, https://github.com/ansible-collections/community.docker/pull/506).
- docker_container_exec - fix ``chdir`` option which was ignored since community.docker 3.0.0 (https://github.com/ansible-collections/community.docker/issues/517, https://github.com/ansible-collections/community.docker/pull/518).
- vendored latest Docker SDK for Python bugfix (https://github.com/ansible-collections/community.docker/pull/513, https://github.com/docker/docker-py/issues/3045).

community.general
~~~~~~~~~~~~~~~~~

- chroot connection plugin - add ``inventory_hostname`` to vars under ``remote_addr``. This is needed for compatibility with ansible-core 2.13 (https://github.com/ansible-collections/community.general/pull/5570).
- cmd_runner module utils - fixed bug when handling default cases in ``cmd_runner_fmt.as_map()`` (https://github.com/ansible-collections/community.general/pull/5538).
- cmd_runner module utils - formatting arguments ``cmd_runner_fmt.as_fixed()`` was expecting an non-existing argument (https://github.com/ansible-collections/community.general/pull/5538).
- keycloak_client_rolemapping - calculate ``proposed`` and ``after`` return values properly (https://github.com/ansible-collections/community.general/pull/5619).
- keycloak_client_rolemapping - remove only listed mappings with ``state=absent`` (https://github.com/ansible-collections/community.general/pull/5619).
- proxmox inventory plugin - fix bug while templating when using templates for the ``url``, ``user``, ``password``, ``token_id``, or ``token_secret`` options (https://github.com/ansible-collections/community.general/pull/5640).
- proxmox inventory plugin - handle tags delimited by semicolon instead of comma, which happens from Proxmox 7.3 on (https://github.com/ansible-collections/community.general/pull/5602).
- redhat_subscription - do not ignore ``consumer_name`` and other variables if ``activationkey`` is specified (https://github.com/ansible-collections/community.general/issues/3486, https://github.com/ansible-collections/community.general/pull/5627).
- redhat_subscription - do not pass arguments to ``subscription-manager register`` for things already configured; now a specified ``rhsm_baseurl`` is properly set for subscription-manager (https://github.com/ansible-collections/community.general/pull/5583).
- unixy callback plugin - fix plugin to work with ansible-core 2.14 by using Ansible's configuration manager for handling options (https://github.com/ansible-collections/community.general/issues/5600).
- vdo - now uses ``yaml.safe_load()`` to parse command output instead of the deprecated ``yaml.load()`` which is potentially unsafe. Using ``yaml.load()`` without explicitely setting a ``Loader=`` is also an error in pyYAML 6.0 (https://github.com/ansible-collections/community.general/pull/5632).
- vmadm - fix for index out of range error in ``get_vm_uuid`` (https://github.com/ansible-collections/community.general/pull/5628).

community.postgresql
~~~~~~~~~~~~~~~~~~~~

- postgresql_privs - fails with ``type=default_privs``, ``privs=ALL``, ``objs=ALL_DEFAULT`` (https://github.com/ansible-collections/community.postgresql/issues/373).

community.routeros
~~~~~~~~~~~~~~~~~~

- api_modify - ``address-pool`` field of entries in API path ``ip dhcp-server`` is not required anymore (https://github.com/ansible-collections/community.routeros/pull/137).
- api_modify - ``ip route`` entry can be defined without the need of ``gateway`` field, which is correct for unreachable/blackhole type of routes (https://github.com/ansible-collections/community.routeros/pull/131).
- api_modify - ``queue interface`` path works now (https://github.com/ansible-collections/community.routeros/pull/131).
- api_modify, api_info - removed wrong field ``dynamic`` from API path ``ipv6 firewall address-list`` (https://github.com/ansible-collections/community.routeros/pull/133).
- api_modify, api_info - the default of the field ``ingress-filtering`` in ``interface bridge port`` is now ``true``, which is the default in ROS (https://github.com/ansible-collections/community.routeros/pull/125).
- command, facts - commands do not timeout in safe mode anymore (https://github.com/ansible-collections/community.routeros/pull/134).

community.sap_libs
~~~~~~~~~~~~~~~~~~

- fix a bug where some commands produces no output which cause to crash the module.
- modules - fix a "variable used before assignment" that cannot be reached but causes sanity test failures.

community.vmware
~~~~~~~~~~~~~~~~

- vmware_dvs_portgroup - Fix an issue when deleting portgroups (https://github.com/ansible-collections/community.vmware/issues/1522).
- vmware_guest_instant_clone - Fix an issue with pyVmomi 8.0.0.1 (https://github.com/ansible-collections/community.vmware/issues/1555).
- vmware_host_lockdown - Fix issue `'VmwareLockdownManager' object has no attribute 'warn'` (https://github.com/ansible-collections/community.vmware/pull/1540).
- vmware_object_custom_attributes_info - Fixed an issue that has occurred an error if a custom attribute is the global type(https://github.com/ansible-collections/community.vmware/pull/1541).
- vmware_portgroup_info - Fix an issue that can fail the module after manually updating a portgroup through vCenter (https://github.com/ansible-collections/community.vmware/issues/1544).

community.zabbix
~~~~~~~~~~~~~~~~

- The inventory script had insufficient error handling in case the Zabbix API provided an empty interfaces list. This bugfix checks for an exisiting interfaces element, then for the minimal length of 1 so that the first interface will only be accessed when it really exists in the api response. (https://github.com/ansible-collections/community.zabbix/issues/826)
- zabbix-proxy - updated to install correct sources for Debian arm64 family
- zabbix_agent - Filter IPv6 addresses from list of IP as Zabbix host creation expects IPv4
- zabbix_agent - installation on Windows will no longer fail when zabbix_agent2 is used
- zabbix_host - fix updating of host without interfaces
- zabbix_proxy - correctly provision tls_accept and tls_connect on Zabbix backend
- zabbix_proxy - updated the datafiles_path fact for the zabbix_proxy and zabbix_server roles due to upstream change
- zabbix_server - move location of the fping(6) variables to distribution specific files (https://github.com/ansible-collections/community.zabbix/issues/812)
- zabbix_server - updated the datafiles_path fact for the zabbix_proxy and zabbix_server roles due to upstream change

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

- bigip_software_image - fixed permission and ownership of the uploaded image file
- bigip_ucs - fixed permission and ownership of the ucs file

fortinet.fortios
~~~~~~~~~~~~~~~~

- Fix invalid arguments in version_schemas;
- Fix issue of filter content could not contain spaces (#208);
- Fix issue of missing some options for monitor modules (#196);
- Fix list type arguments inconsistency;
- Fix list type not match issue;
- Fix supports_check_mode issue for _info and _facts modules;

hetzner.hcloud
~~~~~~~~~~~~~~

- hcloud_firewall - the deletion could fail if the firewall was referenced right before
- hcloud_server - fix backup window was given out as "None" instead of null
- hcloud_server_info - fix backup window was given out as "None" instead of null
- hcloud_volume - fix server name was given out as "None" instead of null if no server was attached
- hcloud_volume_info - fix server name was given out as "None" instead of null if no server was attached

lowlydba.sqlserver
~~~~~~~~~~~~~~~~~~

- Added missing mapping for UseDestinationDefaultDirectories (https://github.com/lowlydba/lowlydba.sqlserver/pull/153)
- Removed default value for KeepCDC to fix compatability with SQL MI (https://github.com/lowlydba/lowlydba.sqlserver/pull/153)
- Removed default value for ReplaceDbNameInFile to fix compatability with SQL MI (https://github.com/lowlydba/lowlydba.sqlserver/pull/148)
- Removed default value for UseDestinationDefaultDirectories to fix compatability with SQL MI (https://github.com/lowlydba/lowlydba.sqlserver/pull/153)
- Removed default value for reuse_source_folder_structure to fix compatability with SQL MI (https://github.com/lowlydba/lowlydba.sqlserver/pull/145)
- Removed the default value for xp_dirtree to allow compatibility with Azure SQL Mangaed instances (https://github.com/lowlydba/lowlydba.sqlserver/pull/141)

netbox.netbox
~~~~~~~~~~~~~

- nb_inventory - Fix site_group in inventory plugin [#872](https://github.com/netbox-community/ansible_modules/pull/872)
- nb_inventory - Make sure inventory works with ansible < 2.11 [#861](https://github.com/netbox-community/ansible_modules/pull/861)
- netbox_virtual_machine - Fix idempotency with virtual machine and NetBox 3.0 [#859](https://github.com/netbox-community/ansible_modules/pull/859)

ovirt.ovirt
~~~~~~~~~~~

- cluster_upgrade - Add default random uuid to engine_correlation_id (https://github.com/oVirt/ovirt-ansible-collection/pull/624).
- cluster_upgrade - Fix the engine_correlation_id location (https://github.com/oVirt/ovirt-ansible-collection/pull/637).
- image_template - Add template_bios_type (https://github.com/oVirt/ovirt-ansible-collection/pull/620).

purestorage.flasharray
~~~~~~~~~~~~~~~~~~~~~~

- purefa.py - Fix issue in Purity versions numbers that are for development versions
- purefa_policy - Fixed missing parameters in function calls
- purefa_vg - Fix typeerror when using newer Purity versions and setting VG QoS

purestorage.fusion
~~~~~~~~~~~~~~~~~~

- fusion_info - Fixed issue with storage endpoint dict formatting

Known Issues
------------

community.routeros
~~~~~~~~~~~~~~~~~~

- api_modify - when limits for entries in ``queue tree`` are defined as human readable - for example ``25M`` -, the configuration will be correctly set in ROS, but the module will indicate the item is changed on every run even when there was no change done. This is caused by the ROS API which returns the number in bytes - for example ``25000000`` (which is inconsistent with the CLI behavior). In order to mitigate that, the limits have to be defined in bytes (those will still appear as human readable in the ROS CLI) (https://github.com/ansible-collections/community.routeros/pull/131).
- api_modify, api_info - ``routing ospf area``, ``routing ospf area range``, ``routing ospf instance``, ``routing ospf interface-template`` paths are not fully implemeted for ROS6 due to the significat changes between ROS6 and ROS7 (https://github.com/ansible-collections/community.routeros/pull/131).

New Modules
-----------

community.general
~~~~~~~~~~~~~~~~~

- community.general.gitlab_project_badge - Manage project badges on GitLab Server
- community.general.keycloak_clientsecret_info - Retrieve client secret via Keycloak API
- community.general.keycloak_clientsecret_regenerate - Regenerate Keycloak client secret via Keycloak API

community.vmware
~~~~~~~~~~~~~~~~

- community.vmware.vmware_custom_attribute - Manage custom attributes definitions
- community.vmware.vmware_custom_attribute_manager - Manage custom attributes from VMware for the given vSphere object

lowlydba.sqlserver
~~~~~~~~~~~~~~~~~~

- lowlydba.sqlserver.user - Configures a user within a database

netbox.netbox
~~~~~~~~~~~~~

- netbox.netbox.netbox_l2vpn - Create, update or delete L2VPN objects in NetBox

New Playbooks
-------------

- community.sops.install - Installs sops and GNU Privacy Guard on all remote hosts
- community.sops.install_localhost - Installs sops and GNU Privacy Guard on localhost

New Roles
---------

- community.sops.install - Install Mozilla sops

Unchanged Collections
---------------------

- amazon.aws (still version 5.1.0)
- ansible.netcommon (still version 4.1.0)
- ansible.posix (still version 1.4.0)
- ansible.windows (still version 1.12.0)
- arista.eos (still version 6.0.0)
- azure.azcollection (still version 1.14.0)
- check_point.mgmt (still version 4.0.0)
- chocolatey.chocolatey (still version 1.3.1)
- cisco.aci (still version 2.3.0)
- cisco.asa (still version 4.0.0)
- cisco.ios (still version 4.0.0)
- cisco.ise (still version 2.5.9)
- cisco.mso (still version 2.1.0)
- cisco.nso (still version 1.0.3)
- cisco.ucs (still version 1.8.0)
- cloud.common (still version 2.1.2)
- community.aws (still version 5.0.0)
- community.azure (still version 2.0.0)
- community.ciscosmb (still version 1.0.5)
- community.digitalocean (still version 1.22.0)
- community.fortios (still version 1.0.0)
- community.google (still version 1.0.0)
- community.grafana (still version 1.5.3)
- community.hashi_vault (still version 4.0.0)
- community.hrobot (still version 1.6.0)
- community.libvirt (still version 1.2.0)
- community.mongodb (still version 1.4.2)
- community.mysql (still version 3.5.1)
- community.network (still version 5.0.0)
- community.okd (still version 2.2.0)
- community.proxysql (still version 1.4.0)
- community.rabbitmq (still version 1.2.3)
- community.sap (still version 1.0.0)
- community.skydive (still version 1.0.0)
- community.windows (still version 1.11.1)
- cyberark.conjur (still version 1.2.0)
- cyberark.pas (still version 1.0.14)
- dellemc.enterprise_sonic (still version 2.0.0)
- dellemc.openmanage (still version 6.3.0)
- dellemc.os10 (still version 1.1.1)
- dellemc.os6 (still version 1.0.7)
- dellemc.os9 (still version 1.0.4)
- fortinet.fortimanager (still version 2.1.7)
- frr.frr (still version 2.0.0)
- gluster.gluster (still version 1.0.2)
- google.cloud (still version 1.0.2)
- hpe.nimble (still version 1.1.4)
- ibm.qradar (still version 2.1.0)
- ibm.spectrum_virtualize (still version 1.10.0)
- inspur.ispim (still version 1.2.0)
- inspur.sm (still version 2.3.0)
- kubernetes.core (still version 2.3.2)
- mellanox.onyx (still version 1.0.0)
- netapp.aws (still version 21.7.0)
- netapp.azure (still version 21.10.0)
- netapp.cloudmanager (still version 21.21.0)
- netapp.elementsw (still version 21.7.0)
- netapp.ontap (still version 22.0.1)
- netapp.storagegrid (still version 21.11.1)
- netapp.um_info (still version 21.8.0)
- netapp_eseries.santricity (still version 1.3.1)
- ngine_io.exoscale (still version 1.0.0)
- ngine_io.vultr (still version 1.1.2)
- openstack.cloud (still version 1.10.0)
- openvswitch.openvswitch (still version 2.1.0)
- purestorage.flashblade (still version 1.10.0)
- sensu.sensu_go (still version 1.13.1)
- splunk.es (still version 2.1.0)
- t_systems_mms.icinga_director (still version 1.31.4)
- theforeman.foreman (still version 3.7.0)
- vmware.vmware_rest (still version 2.2.0)
- vultr.cloud (still version 1.3.1)
- vyos.vyos (still version 4.0.0)
- wti.remote (still version 1.0.4)

v7.0.0
======

.. contents::
  :local:
  :depth: 2

Release Summary
---------------

Release Date: 2022-11-22

`Porting Guide <https://docs.ansible.com/ansible/devel/porting_guides.html>`_

Removed Collections
-------------------

- servicenow.servicenow (previously included version: 1.0.6)

Added Collections
-----------------

- ibm.spectrum_virtualize (version 1.10.0)
- inspur.ispim (version 1.2.0)
- lowlydba.sqlserver (version 1.0.4)
- purestorage.fusion (version 1.1.1)
- vultr.cloud (version 1.3.1)

Ansible-core
------------

Ansible 7.0.0 contains Ansible-core version 2.14.0.
This is a newer version than version 2.13.0 contained in the previous Ansible release.

The changes are reported in the combined changelog below.

Included Collections
--------------------

If not mentioned explicitly, the changes are reported in the combined changelog below.

+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Collection                    | Ansible 6.0.0 | Ansible 7.0.0 | Notes                                                                                                                                                                                                          |
+===============================+===============+===============+================================================================================================================================================================================================================+
| amazon.aws                    | 3.2.0         | 5.1.0         |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ansible.netcommon             | 3.0.1         | 4.1.0         |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ansible.utils                 | 2.6.1         | 2.7.0         |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ansible.windows               | 1.10.0        | 1.12.0        |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| arista.eos                    | 5.0.1         | 6.0.0         |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| awx.awx                       | 21.0.0        | 21.8.0        | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.                                                                                   |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| azure.azcollection            | 1.12.0        | 1.14.0        | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.                                                                                   |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| check_point.mgmt              | 2.3.0         | 4.0.0         |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| chocolatey.chocolatey         | 1.2.0         | 1.3.1         |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cisco.aci                     | 2.2.0         | 2.3.0         |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cisco.asa                     | 3.0.0         | 4.0.0         |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cisco.dnac                    | 6.4.0         | 6.6.0         |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cisco.intersight              | 1.0.19        | 1.0.20        | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.                                                                                   |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cisco.ios                     | 3.0.0         | 4.0.0         |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cisco.iosxr                   | 3.0.0         | 4.0.2         |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cisco.ise                     | 2.4.1         | 2.5.9         |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cisco.meraki                  | 2.6.2         | 2.11.0        |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cisco.mso                     | 2.0.0         | 2.1.0         |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cisco.nxos                    | 3.0.0         | 4.0.0         |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cloud.common                  | 2.1.1         | 2.1.2         |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.aws                 | 3.2.1         | 5.0.0         |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.azure               | 1.1.0         | 2.0.0         |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.crypto              | 2.3.2         | 2.8.1         |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.digitalocean        | 1.19.0        | 1.22.0        |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.dns                 | 2.1.1         | 2.4.1         |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.docker              | 2.6.0         | 3.2.1         |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.general             | 5.0.2         | 6.0.1         |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.grafana             | 1.4.0         | 1.5.3         |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.hashi_vault         | 3.0.0         | 4.0.0         |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.hrobot              | 1.3.1         | 1.6.0         |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.libvirt             | 1.1.0         | 1.2.0         |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.mongodb             | 1.4.0         | 1.4.2         | There are no changes recorded in the changelog.                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.mysql               | 3.2.1         | 3.5.1         |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.network             | 4.0.1         | 5.0.0         |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.postgresql          | 2.1.5         | 2.3.0         |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.rabbitmq            | 1.2.1         | 1.2.3         |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.routeros            | 2.1.0         | 2.3.1         |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.sap_libs            | 1.1.0         | 1.3.0         |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.sops                | 1.2.2         | 1.4.1         |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.vmware              | 2.5.0         | 3.1.0         |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.windows             | 1.10.0        | 1.11.1        |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.zabbix              | 1.7.0         | 1.8.0         |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| containers.podman             | 1.9.3         | 1.9.4         |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cyberark.conjur               | 1.1.0         | 1.2.0         | You can find the collection's changelog at `https://github.com/cyberark/ansible-conjur-collection/blob/master/CHANGELOG.md <https://github.com/cyberark/ansible-conjur-collection/blob/master/CHANGELOG.md>`_. |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| dellemc.enterprise_sonic      | 1.1.1         | 2.0.0         |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| dellemc.openmanage            | 5.4.0         | 6.3.0         |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| f5networks.f5_modules         | 1.17.0        | 1.20.0        |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| fortinet.fortimanager         | 2.1.5         | 2.1.7         |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| fortinet.fortios              | 2.1.6         | 2.1.7         |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| hetzner.hcloud                | 1.6.0         | 1.8.2         |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ibm.qradar                    | 2.0.0         | 2.1.0         |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ibm.spectrum_virtualize       |               | 1.10.0        | The collection was added to Ansible                                                                                                                                                                            |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| infinidat.infinibox           | 1.3.3         | 1.3.7         | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.                                                                                   |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| infoblox.nios_modules         | 1.2.2         | 1.4.0         |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| inspur.ispim                  |               | 1.2.0         | The collection was added to Ansible                                                                                                                                                                            |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| inspur.sm                     | 2.0.0         | 2.3.0         |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| junipernetworks.junos         | 3.0.1         | 4.0.0         |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| kubernetes.core               | 2.3.1         | 2.3.2         |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| lowlydba.sqlserver            |               | 1.0.4         | The collection was added to Ansible                                                                                                                                                                            |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| netapp.cloudmanager           | 21.17.0       | 21.21.0       |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| netapp.ontap                  | 21.19.1       | 22.0.1        |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| netapp.storagegrid            | 21.10.0       | 21.11.1       |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| netapp_eseries.santricity     | 1.3.0         | 1.3.1         |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| netbox.netbox                 | 3.7.1         | 3.8.1         |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ngine_io.vultr                | 1.1.1         | 1.1.2         |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| openstack.cloud               | 1.8.0         | 1.10.0        | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.                                                                                   |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ovirt.ovirt                   | 2.0.4         | 2.3.1         |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| purestorage.flasharray        | 1.13.0        | 1.14.0        |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| purestorage.flashblade        | 1.9.0         | 1.10.0        |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| purestorage.fusion            |               | 1.1.1         | The collection was added to Ansible                                                                                                                                                                            |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| splunk.es                     | 2.0.0         | 2.1.0         |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| t_systems_mms.icinga_director | 1.29.0        | 1.31.4        |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| theforeman.foreman            | 3.4.0         | 3.7.0         |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| vmware.vmware_rest            | 2.1.5         | 2.2.0         |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| vultr.cloud                   |               | 1.3.1         | The collection was added to Ansible                                                                                                                                                                            |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| vyos.vyos                     | 3.0.1         | 4.0.0         |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| wti.remote                    | 1.0.3         | 1.0.4         | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.                                                                                   |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Major Changes
-------------

Ansible-core
~~~~~~~~~~~~

- Move handler processing into new ``PlayIterator`` phase to use the configured strategy (https://github.com/ansible/ansible/issues/65067)
- ansible - At startup the filesystem encoding and locale are checked to verify they are UTF-8. If not, the process exits with an error reporting the errant encoding.
- ansible - Increase minimum Python requirement to Python 3.9 for CLI utilities and controller code
- ansible-test - At startup the filesystem encoding is checked to verify it is UTF-8. If not, the process exits with an error reporting the errant encoding.
- ansible-test - At startup the locale is configured as ``en_US.UTF-8``, with a fallback to ``C.UTF-8``. If neither encoding is available the process exits with an error. If the fallback is used, a warning is displayed. In previous versions the ``en_US.UTF-8`` locale was always requested. However, no startup checking was performed to verify the locale was successfully configured.

amazon.aws
~~~~~~~~~~

- amazon.aws collection - The amazon.aws collection has dropped support for ``botocore<1.20.0`` and ``boto3<1.17.0``. Most modules will continue to work with older versions of the AWS SDK, however compatibility with older versions of the SDK is not guaranteed and will not be tested. When using older versions of the SDK a warning will be emitted by Ansible (https://github.com/ansible-collections/amazon.aws/pull/574).
- autoscaling_group - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.autoscaling_group``.
- autoscaling_group_info - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.autoscaling_group_info``.
- cloudtrail - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.cloudtrail``.
- cloudwatch_metric_alarm - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.cloudwatch_metric_alarm``.
- cloudwatchevent_rule - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.cloudwatchevent_rule``.
- cloudwatchlogs_log_group - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.cloudwatchlogs_log_group``.
- cloudwatchlogs_log_group_info - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.cloudwatchlogs_log_group_info``.
- cloudwatchlogs_log_group_metric_filter - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.cloudwatchlogs_log_group_metric_filter``.
- ec2_eip - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.ec2_eip``.
- ec2_eip_info - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.ec2_eip_info``.
- elb_application_lb - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.elb_application_lb``.
- elb_application_lb_info - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.elb_application_lb_info``.
- execute_lambda - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.execute_lambda``.
- iam_policy - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.iam_policy``.
- iam_policy_info - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.iam_policy_info``.
- iam_user - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.iam_user``.
- iam_user_info - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.iam_user_info``.
- kms_key - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.kms_key``.
- kms_key_info - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.kms_key_info``.
- lambda - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.lambda``.
- lambda_alias - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.lambda_alias``.
- lambda_event - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.lambda_event``.
- lambda_execute - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.lambda_execute``.
- lambda_info - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.lambda_info``.
- lambda_policy - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.lambda_policy``.
- rds_cluster - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.rds_cluster``.
- rds_cluster_info - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.rds_cluster_info``.
- rds_cluster_snapshot - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.rds_cluster_snapshot``.
- rds_instance - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.rds_instance``.
- rds_instance_info - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.rds_instance_info``.
- rds_instance_snapshot - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.rds_instance_snapshot``.
- rds_option_group - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.rds_option_group``.
- rds_option_group_info - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.rds_option_group_info``.
- rds_param_group - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.rds_param_group``.
- rds_snapshot_info - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.rds_snapshot_info``.
- rds_subnet_group - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.rds_subnet_group``.
- route53 - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.route53``.
- route53_health_check - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.route53_health_check``.
- route53_info - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.route53_info``.
- route53_zone - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.route53_zone``.

arista.eos
~~~~~~~~~~

- Remove following EOS dprecated modules
- Use of connection: local and the provider option are no longer valid on any modules in this collection.
- eos_interface
- eos_l2_interface
- eos_l3_interface
- eos_linkagg
- eos_static_route
- eos_vlan

check_point.mgmt
~~~~~~~~~~~~~~~~

- plugins/httpapi/checkpoint - Support for Smart-1 Cloud with new variable 'ansible_cloud_mgmt_id'

chocolatey.chocolatey
~~~~~~~~~~~~~~~~~~~~~

- win_chocolatey - Added bootstrap_script option to allow users to target a script URL for installing Chocolatey on clients.
- win_chocolatey_facts - Added outdated packages list to data returned.

cisco.asa
~~~~~~~~~

- Please use either of the following connection types - network_cli, httpapi or netconf.
- This includes the following modules:
- This release drops support for `connection: local` and provider dictionary.
- This release removes all deprecated plugins that have reached their end-of-life.
- Use of connection: local and the provider option are no longer valid on any modules in this collection.
- asa_acl
- asa_og

cisco.ios
~~~~~~~~~

- Only valid connection types for this collection is network_cli.
- This release drops support for `connection: local` and provider dictionary.

cisco.iosxr
~~~~~~~~~~~

- Only valid connection types for this collection are network_cli and netconf.
- This release drops support for `connection: local` and provider dictionary.

cisco.nxos
~~~~~~~~~~

- Please use either of the following connection types - network_cli, httpapi or netconf.
- This release drops support for `connection: local` and provider dictionary.

community.aws
~~~~~~~~~~~~~

- community.aws collection - The amazon.aws collection has dropped support for ``botocore<1.20.0`` and ``boto3<1.17.0``. Most modules will continue to work with older versions of the AWS SDK, however compatibility with older versions of the SDK is not guaranteed and will not be tested. When using older versions of the SDK a warning will be emitted by Ansible (https://github.com/ansible-collections/community.aws/pull/956).

community.docker
~~~~~~~~~~~~~~~~

- The collection now contains vendored code from the Docker SDK for Python to talk to the Docker daemon. Modules and plugins using this code no longer need the Docker SDK for Python installed on the machine the module or plugin is running on (https://github.com/ansible-collections/community.docker/pull/398).
- docker_api connection plugin - no longer uses the Docker SDK for Python. It requires ``requests`` to be installed, and depending on the features used has some more requirements. If the Docker SDK for Python is installed, these requirements are likely met (https://github.com/ansible-collections/community.docker/pull/414).
- docker_container - no longer uses the Docker SDK for Python. It requires ``requests`` to be installed, and depending on the features used has some more requirements. If the Docker SDK for Python is installed, these requirements are likely met (https://github.com/ansible-collections/community.docker/pull/422).
- docker_container - the module was completely rewritten from scratch (https://github.com/ansible-collections/community.docker/pull/422).
- docker_container_exec - no longer uses the Docker SDK for Python. It requires ``requests`` to be installed, and depending on the features used has some more requirements. If the Docker SDK for Python is installed, these requirements are likely met (https://github.com/ansible-collections/community.docker/pull/401).
- docker_container_info - no longer uses the Docker SDK for Python. It requires ``requests`` to be installed, and depending on the features used has some more requirements. If the Docker SDK for Python is installed, these requirements are likely met (https://github.com/ansible-collections/community.docker/pull/402).
- docker_containers inventory plugin - no longer uses the Docker SDK for Python. It requires ``requests`` to be installed, and depending on the features used has some more requirements. If the Docker SDK for Python is installed, these requirements are likely met (https://github.com/ansible-collections/community.docker/pull/413).
- docker_host_info - no longer uses the Docker SDK for Python. It requires ``requests`` to be installed, and depending on the features used has some more requirements. If the Docker SDK for Python is installed, these requirements are likely met (https://github.com/ansible-collections/community.docker/pull/403).
- docker_image - no longer uses the Docker SDK for Python. It requires ``requests`` to be installed, and depending on the features used has some more requirements. If the Docker SDK for Python is installed, these requirements are likely met (https://github.com/ansible-collections/community.docker/pull/404).
- docker_image_info - no longer uses the Docker SDK for Python. It requires ``requests`` to be installed, and depending on the features used has some more requirements. If the Docker SDK for Python is installed, these requirements are likely met (https://github.com/ansible-collections/community.docker/pull/405).
- docker_image_load - no longer uses the Docker SDK for Python. It requires ``requests`` to be installed, and depending on the features used has some more requirements. If the Docker SDK for Python is installed, these requirements are likely met (https://github.com/ansible-collections/community.docker/pull/406).
- docker_login - no longer uses the Docker SDK for Python. It requires ``requests`` to be installed, and depending on the features used has some more requirements. If the Docker SDK for Python is installed, these requirements are likely met (https://github.com/ansible-collections/community.docker/pull/407).
- docker_network - no longer uses the Docker SDK for Python. It requires ``requests`` to be installed, and depending on the features used has some more requirements. If the Docker SDK for Python is installed, these requirements are likely met (https://github.com/ansible-collections/community.docker/pull/408).
- docker_network_info - no longer uses the Docker SDK for Python. It requires ``requests`` to be installed, and depending on the features used has some more requirements. If the Docker SDK for Python is installed, these requirements are likely met (https://github.com/ansible-collections/community.docker/pull/409).
- docker_plugin - no longer uses the Docker SDK for Python. It requires ``requests`` to be installed, and depending on the features used has some more requirements. If the Docker SDK for Python is installed, these requirements are likely met (https://github.com/ansible-collections/community.docker/pull/429).
- docker_prune - no longer uses the Docker SDK for Python. It requires ``requests`` to be installed, and depending on the features used has some more requirements. If the Docker SDK for Python is installed, these requirements are likely met (https://github.com/ansible-collections/community.docker/pull/410).
- docker_volume - no longer uses the Docker SDK for Python. It requires ``requests`` to be installed, and depending on the features used has some more requirements. If the Docker SDK for Python is installed, these requirements are likely met (https://github.com/ansible-collections/community.docker/pull/411).
- docker_volume_info - no longer uses the Docker SDK for Python. It requires ``requests`` to be installed, and depending on the features used has some more requirements. If the Docker SDK for Python is installed, these requirements are likely met (https://github.com/ansible-collections/community.docker/pull/412).

community.general
~~~~~~~~~~~~~~~~~

- The internal structure of the collection was changed for modules and action plugins. These no longer live in a directory hierarchy ordered by topic, but instead are now all in a single (flat) directory. This has no impact on users *assuming they did not use internal FQCNs*. These will still work, but result in deprecation warnings. They were never officially supported and thus the redirects are kept as a courtsey, and this is not labelled as a breaking change. Note that for example the Ansible VScode plugin started recommending these internal names. If you followed its recommendation, you will now have to change back to the short names to avoid deprecation warnings, and potential errors in the future as these redirects will be removed in community.general 9.0.0 (https://github.com/ansible-collections/community.general/pull/5461).
- newrelic_deployment - removed New Relic v1 API, added support for v2 API (https://github.com/ansible-collections/community.general/pull/5341).

community.mysql
~~~~~~~~~~~~~~~

- mysql_db - the ``pipefail`` argument's default value will be changed to ``true`` in community.mysql 4.0.0. If your target machines do not use ``bash`` as a default interpreter, set ``pipefail`` to ``false`` explicitly. However, we strongly recommend setting up ``bash`` as a default and ``pipefail=true`` as it will protect you from getting broken dumps you don't know about (https://github.com/ansible-collections/community.mysql/issues/407).

community.network
~~~~~~~~~~~~~~~~~

- The community.network collection no longer supports Ansible 2.9 and ansible-base 2.10. While we take no active measures to prevent usage, we will remove compatibility code and other compatility measures that will effectively prevent using most content from this collection with Ansible 2.9, and some content of this collection with ansible-base 2.10. Both Ansible 2.9 and ansible-base 2.10 will very soon be End of Life and if you are still using them, you should consider upgrading to ansible-core 2.11 or later as soon as possible (https://github.com/ansible-collections/community.network/pull/426).
- The internal structure of the collection was changed for modules and action plugins. These no longer live in a directory hierarchy ordered by topic, but instead are now all in a single (flat) directory. This has no impact on users *assuming they did not use internal FQCNs*. These will still work, but result in deprecation warnings. They were never officially supported and thus the redirects are kept as a courtsey, and this is not labelled as a breaking change. Note that for example the Ansible VScode plugin started recommending these internal names. If you followed its recommendation, you will now have to change back to the short names to avoid deprecation warnings, and potential errors in the future as these redirects will be removed in community.network 8.0.0 (https://github.com/ansible-collections/community.network/pull/482).

community.postgresql
~~~~~~~~~~~~~~~~~~~~

- postgresql_user - the ``groups`` argument has been deprecated and will be removed in ``community.postgresql 3.0.0``. Please use the ``postgresql_membership`` module to specify group/role memberships instead (https://github.com/ansible-collections/community.postgresql/issues/277).

dellemc.enterprise_sonic
~~~~~~~~~~~~~~~~~~~~~~~~

- Added 'static_routes' module to collection (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/82).
- Added a resource module for NTP support (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/99).
- Added a resource module for support of prefix lists (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/100).
- Updated backend REST API request formats in all applicable modules for compatibility with SONiC 4.x openconfig YANG compliant REST APIs. (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/53)

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- Added collection metadata for creating execution environments.
- Refactored the Markdown (MD) files and content for better readability.
- The share parameters are deprecated from the following modules - idrac_network, idrac_timezone_ntp, dellemc_configure_idrac_eventing, dellemc_configure_idrac_services, dellemc_idrac_lc_attributes, dellemc_system_lockdown_mode.
- idrac_bios - The module is enhanced to support clear pending BIOS attributes, reset BIOS to default settings, and configure BIOS attribute using Redfish.
- idrac_boot - Support for configuring the boot settings on iDRAC.
- idrac_redfish_storage_controller - This module is enhanced to support LockVirtualDisk operation.
- idrac_virtual_media - This module allows to configure Remote File Share settings.
- ome_device_group - The module is enhanced to support the removal of devices from a static device group.
- ome_devices - Support for performing device-specific operations on OpenManage Enterprise.

fortinet.fortimanager
~~~~~~~~~~~~~~~~~~~~~

- Fix compatibility issue for ansible 2.9.x and ansible-base 2.10.x.
- Many fixes for Ansible sanity test warnings & errors.
- Support FortiManager Schema 7.2.0 , 98 new modules
- support Ansible changelogs.

fortinet.fortios
~~~~~~~~~~~~~~~~

- Support Diff feature in check_mode.
- Support Fortios 7.2.0.

infoblox.nios_modules
~~~~~~~~~~~~~~~~~~~~~

- Feature for extra layer security , with `cert` and `key` parameters in playbooks for authenticating using certificate and key ``*.pem`` file absolute path `#154 <https://github.com/infobloxopen/infoblox-ansible/pull/154>`_
- Fix to remove issue causing due to template attr in deleting network using Ansible module nios network `#147 <https://github.com/infobloxopen/infoblox-ansible/pull/147>`_
- Update `text` field of TXT Record `#128 <https://github.com/infobloxopen/infoblox-ansible/pull/128>`_
- Update operation using `old_name` and `new_name` for the object with dummy name in `old_name` (which does not exist in system) will not create a new object in the system. An error will be thrown stating the object does not exist in the system `#129 <https://github.com/infobloxopen/infoblox-ansible/pull/129>`_

junipernetworks.junos
~~~~~~~~~~~~~~~~~~~~~

- Use of connection: local and the provider option are no longer valid on any modules in this collection.

vyos.vyos
~~~~~~~~~

- Use of connection: local and the provider option are no longer valid on any modules in this collection.

Minor Changes
-------------

Ansible-core
~~~~~~~~~~~~

- Add a new "INVENTORY_UNPARSED_WARNING" flag add to hide the "No inventory was parsed, only implicit localhost is available" warning
- Add an 'action_plugin' field for modules in runtime.yml plugin_routing.

  This fixes module_defaults by supporting modules-as-redirected-actions
  without redirecting module_defaults entries to the common action.

  .. code: yaml

     plugin_routing:
       action:
         facts:
           redirect: ns.coll.eos
         command:
           redirect: ns.coll.eos
       modules:
         facts:
           redirect: ns.coll.eos_facts
         command:
           redirect: ns.coll.eos_command

  With the runtime.yml above for ns.coll, a task such as

  .. code: yaml

     - hosts: all
       module_defaults:
         ns.coll.eos_facts: {'valid_for_eos_facts': 'value'}
         ns.coll.eos_command: {'not_valid_for_eos_facts': 'value'}
       tasks:
         - ns.coll.facts:

  will end up with defaults for eos_facts and eos_command
  since both modules redirect to the same action.

  To select an action plugin for a module without merging
  module_defaults, define an action_plugin field for the resolved
  module in the runtime.yml.

  .. code: yaml

     plugin_routing:
       modules:
         facts:
           redirect: ns.coll.eos_facts
           action_plugin: ns.coll.eos
         command:
           redirect: ns.coll.eos_command
           action_plugin: ns.coll.eos

  The action_plugin field can be a redirected action plugin, as
  it is resolved normally.

  Using the modified runtime.yml, the example task will only use
  the ns.coll.eos_facts defaults.
- Add support for parsing ``-a`` module options as JSON and not just key=value arguments - https://github.com/ansible/ansible/issues/78112
- Added Kylin Linux Advanced Server OS in RedHat OS Family.
- Allow ``when`` conditionals to be used on ``flush_handlers`` (https://github.com/ansible/ansible/issues/77616)
- Allow meta tasks to be used as handlers.
- Display - The display class will now proxy calls to Display.display via the queue from forks/workers to be handled by the parent process for actual display. This reduces some reliance on the fork start method and improves reliability of displaying messages.
- Jinja version test - Add pep440 version_type for version test. (https://github.com/ansible/ansible/issues/78288)
- Loops - Add new ``loop_control.extended_allitems`` to allow users to disable tracking all loop items for each loop (https://github.com/ansible/ansible/issues/75216)
- NetBSD - Add uptime_seconds fact
- Provide a `utc` option for strftime to show time in UTC rather than local time
- Raise a proper error when ``include_role`` or ``import_role`` is used as a handler.
- Remove the ``AnsibleContext.resolve`` method as its override is not necessary. Furthermore the ability to override the ``resolve`` method was deprecated in Jinja 3.0.0 and removed in Jinja 3.1.0.
- Utilize @classmethod and @property together to form classproperty (Python 3.9) to access field attributes of a class
- ``LoopControl`` is now templated through standard ``post_validate`` method (https://github.com/ansible/ansible/pull/75715)
- ``ansible-galaxy collection install`` - add an ``--offline`` option to prevent querying distribution servers (https://github.com/ansible/ansible/issues/77443).
- ansible - Add support for Python 3.11 to Python interpreter discovery.
- ansible - At startup the stdin/stdout/stderr file handles are checked to verify they are using blocking IO. If not, the process exits with an error reporting which file handle(s) are using non-blocking IO.
- ansible-config adds JSON and YAML output formats for list and dump actions.
- ansible-connection now supports verbosity directly on cli
- ansible-console added 'collections' command to match playbook keyword.
- ansible-doc - remove some of the manual formatting, and use YAML more uniformly. This in particular means that ``true`` and ``false`` are used for boolean values, instead of ``True`` and ``False`` (https://github.com/ansible/ansible/pull/78668).
- ansible-galaxy - Support resolvelib versions 0.6.x, 0.7.x, and 0.8.x. The full range of supported versions is now >= 0.5.3, < 0.9.0.
- ansible-galaxy now supports a user defined timeout,  instead of existing hardcoded 60s (now the default).
- ansible-test - Add FreeBSD 13.1 remote support.
- ansible-test - Add RHEL 9.0 remote support.
- ansible-test - Add support for Python 3.11.
- ansible-test - Add support for RHEL 8.6 remotes.
- ansible-test - Add support for Ubuntu VMs using the ``--remote`` option.
- ansible-test - Add support for exporting inventory with ``ansible-test shell --export {path}``.
- ansible-test - Add support for multi-arch remotes.
- ansible-test - Add support for provisioning Alpine 3.16 remote instances.
- ansible-test - Add support for provisioning Fedora 36 remote instances.
- ansible-test - Add support for provisioning Ubuntu 20.04 remote instances.
- ansible-test - Add support for provisioning remotes which require ``doas`` for become.
- ansible-test - Add support for running non-interactive commands with ``ansible-test shell``.
- ansible-test - Alpine remotes now use ``sudo`` for tests, using ``doas`` only for bootstrapping.
- ansible-test - An improved error message is shown when the download of a pip bootstrap script fails. The download now uses ``urllib2`` instead of ``urllib`` on Python 2.
- ansible-test - Avoid using the ``mock_use_standalone_module`` setting for unit tests running on Python 3.8 or later.
- ansible-test - Become support for remote instance provisioning is no longer tied to a fixed list of platforms.
- ansible-test - Blocking mode is now enforced for stdin, stdout and stderr. If any of these are non-blocking then ansible-test will exit during startup with an error.
- ansible-test - Distribution specific test containers are now multi-arch, supporting both x86_64 and aarch64.
- ansible-test - Distribution specific test containers no longer contain a ``/etc/ansible/hosts`` file.
- ansible-test - Enable loading of ``coverage`` data files created by older supported ansible-test releases.
- ansible-test - Fedora 36 has been added as a test container.
- ansible-test - FreeBSD remotes now use ``sudo`` for tests, using ``su`` only for bootstrapping.
- ansible-test - Improve consistency of output messages by using stdout or stderr for most output, but not both.
- ansible-test - Improve consistency of version specific documentation links.
- ansible-test - Remote Alpine instances now have the ``acl`` package installed.
- ansible-test - Remote Fedora instances now have the ``acl`` package installed.
- ansible-test - Remote FreeBSD instances now have ACLs enabled on the root filesystem.
- ansible-test - Remote Ubuntu instances now have the ``acl`` package installed.
- ansible-test - Remove Fedora 34 test container.
- ansible-test - Remove Fedora 35 test container.
- ansible-test - Remove FreeBSD 13.0 remote support.
- ansible-test - Remove RHEL 8.5 remote support.
- ansible-test - Remove Ubuntu 18.04 test container.
- ansible-test - Remove support for Python 2.7 on provisioned FreeBSD instances.
- ansible-test - Remove support for Python 3.8 on the controller.
- ansible-test - Remove the ``opensuse15py2`` container.
- ansible-test - Support multiple pinned versions of the ``coverage`` module. The version used now depends on the Python version in use.
- ansible-test - Test containers have been updated to remove the ``VOLUME`` instruction.
- ansible-test - The Alpine 3 test container has been updated to Alpine 3.16.0.
- ansible-test - The ``http-test-container`` container is now multi-arch, supporting both x86_64 and aarch64.
- ansible-test - The ``pypi-test-container`` container is now multi-arch, supporting both x86_64 and aarch64.
- ansible-test - The ``shell`` command can be used outside a collection if no controller delegation is required.
- ansible-test - The openSUSE test container has been updated to openSUSE Leap 15.4.
- ansible-test - Ubuntu 22.04 has been added as a test container.
- ansible-test - Update ``base`` and ``default`` containers to include Python 3.11.0.
- ansible-test - Update ``default`` containers to include new ``docs-build`` sanity test requirements.
- ansible-test - Update pinned sanity test requirements for all tests.
- ansible-test - Update the ``base`` container to 3.4.0.
- ansible-test - Update the ``default`` containers to 6.6.0.
- ansible-test validate-modules - Added support for validating module documentation stored in a sidecar file alongside the module (``{module}.yml`` or ``{module}.yaml``). Previously these files were ignored and documentation had to be placed in ``{module}.py``.
- apt_repository remove dependency on apt-key and use gpg + /usr/share/keyrings directly instead
- apt_repository will use the trust repo directories in order of preference (more appropriate to less) as they exist on the target.
- blockinfile - The presence of the multiline flag (?m) in the regular expression for insertafter opr insertbefore controls whether the match is done line by line or with multiple lines (https://github.com/ansible/ansible/pull/75090).
- calls to listify_lookup_plugin_terms in core do not pass in loader/dataloader anymore.
- collections - ``ansible-galaxy collection build`` can now utilize ``MANIFEST.in`` style directives from ``galaxy.yml`` instead of ``build_ignore`` effectively inverting the logic from include by default, to exclude by default. (https://github.com/ansible/ansible/pull/78422)
- config manager, move templating into main query function in config instead of constants
- config manager, remove updates to configdata as it is mostly unused
- configuration entry INTERPRETER_PYTHON_DISTRO_MAP is now 'private' and won't show up in normal configuration queries and docs, since it is not 'settable' this avoids user confusion.
- distribution - add distribution_minor_version for Debian Distro (https://github.com/ansible/ansible/issues/74481).
- documentation construction now gives more information on error.
- facts - add OSMC to Debian os_family mapping
- get_url - permit to pass to parameter ``checksum`` an URL pointing to a file containing only a checksum (https://github.com/ansible/ansible/issues/54390).
- new tests url, uri and urn will verify string as such, but they don't check existance of the resource
- plugin loader - add ansible_name and ansible_aliases attributes to plugin objects/classes.
- systemd is now systemd_service to better reflect the scope of the module, systemd is kept as an alias for backwards compatibility.
- templating - removed internal template cache
- uri - cleanup write_file method, remove overkill safety checks and report any exception, change shutilcopyfile to use module.atomic_move
- urls - Add support to specify SSL/TLS ciphers to use during a request (https://github.com/ansible/ansible/issues/78633)
- validate-modules - Allow ``type: raw`` on a module return type definition for values that have a dynamic type
- version output now includes the path to the python executable that Ansible is running under
- yum_repository - do not give the ``async`` parameter a default value anymore, since this option is deprecated in RHEL 8. This means that ``async = 1`` won't be added to repository files if omitted, but it can still be set explicitly if needed.

amazon.aws
~~~~~~~~~~

- Ability to record and replay the API interaction of a module for testing purpose. Show case the feature with an example (https://github.com/ansible-collections/amazon.aws/pull/998).
- Remove the empty __init__.py file from the distribution, they were not required anymore (https://github.com/ansible-collections/amazon.aws/pull/1018).
- amazon.aws collection - The ``aws_access_key`` parameter has been renamed to ``access_key``, ``access_key`` was previously an alias for this parameter and ``aws_access_key`` remains as an alias.  This change should have no observable effect for users outside the module/plugin documentation. (https://github.com/ansible-collections/amazon.aws/pull/1172).
- amazon.aws collection - The ``aws_secret_key`` parameter has been renamed to ``secret_key``, ``secret_key`` was previously an alias for this parameter and ``aws_secret_key`` remains as an alias.  This change should have no observable effect for users outside the module/plugin documentation. (https://github.com/ansible-collections/amazon.aws/pull/1172).
- amazon.aws collection - The ``security_token`` parameter has been renamed to ``session_token``, ``security_token`` was previously an alias for this parameter and ``security_token`` remains as an alias.  This change should have no observable effect for users outside the module/plugin documentation. (https://github.com/ansible-collections/amazon.aws/pull/1172).
- amazon.aws modules - the ``ec2_url`` parameter has been renamed to ``endpoint_url`` for consistency, ``ec2_url`` remains as an alias (https://github.com/ansible-collections/amazon.aws/pull/992).
- aws_account_attribute lookup plugin - use ``missing_required_lib`` for more consistent error message when boto3/botocore is not available (https://github.com/ansible-collections/amazon.aws/pull/1152).
- aws_caller_info - minor linting fixes (https://github.com/ansible-collections/amazon.aws/pull/968).
- aws_ec2 - introduce the ``allow_duplicated_hosts`` configuration key (https://github.com/ansible-collections/amazon.aws/pull/1026).
- aws_ec2 inventory - Allow for literal strings in hostname that don't match filter parameters in ec2 describe-instances (https://github.com/ansible-collections/amazon.aws/pull/826).
- aws_ec2 inventory - minor linting fixes (https://github.com/ansible-collections/amazon.aws/pull/1181).
- aws_ec2 inventory plugin - use ``missing_required_lib`` for more consistent error message when boto3/botocore is not available (https://github.com/ansible-collections/amazon.aws/pull/1152).
- aws_rds inventory plugin - use ``missing_required_lib`` for more consistent error message when boto3/botocore is not available (https://github.com/ansible-collections/amazon.aws/pull/1152).
- aws_s3 - Add ``validate_bucket_name`` option, to control bucket name validation (https://github.com/ansible-collections/amazon.aws/pull/615).
- aws_s3 - The ``aws_s3`` module has been renamed to ``s3_object`` (https://github.com/ansible-collections/amazon.aws/pull/869).
- aws_s3 - ``resource_tags`` has been added as an alias for the ``tags`` parameter (https://github.com/ansible-collections/amazon.aws/pull/845).
- aws_secret lookup plugin - use ``missing_required_lib`` for more consistent error message when boto3/botocore is not available (https://github.com/ansible-collections/amazon.aws/pull/1152).
- aws_ssm - Add support for ``endpoint`` parameter (https://github.com/ansible-collections/amazon.aws/pull/837).
- aws_ssm lookup plugin - use ``missing_required_lib`` for more consistent error message when boto3/botocore is not available (https://github.com/ansible-collections/amazon.aws/pull/1152).
- cloudformation - avoid catching ``Exception``, catch more specific errors instead (https://github.com/ansible-collections/amazon.aws/pull/968).
- cloudwatch_metric_alarm_info - Added a new module that describes the cloudwatch metric alarms (https://github.com/ansible-collections/amazon.aws/pull/988).
- ec2_eni - Change parameter ``device_index`` data type to string when passing to ``describe_network_inter`` api call (https://github.com/ansible-collections/amazon.aws/pull/877).
- ec2_eni - ``resource_tags`` has been added as an alias for the ``tags`` parameter (https://github.com/ansible-collections/amazon.aws/pull/845).
- ec2_group - The ``ec2_group`` module has been renamed to ``ec2_security_group``, ``ec2_group`` remains as an alias (https://github.com/ansible-collections/amazon.aws/pull/897).
- ec2_group - add ``egress_rules`` as an alias for ``rules_egress`` (https://github.com/ansible-collections/amazon.aws/pull/878).
- ec2_group - add ``purge_egress_rules`` as an alias for ``purge_rules_egress`` (https://github.com/ansible-collections/amazon.aws/pull/878).
- ec2_group_info - The ``ec2_group_info`` module has been renamed to ``ec2_security_group_info``, ``ec2_group_info`` remains as an alias (https://github.com/ansible-collections/amazon.aws/pull/897).
- ec2_instance - Add hibernation_options and volumes->ebs->encrypted keys to support stop-hibernate instance (https://github.com/ansible-collections/amazon.aws/pull/972).
- ec2_instance - Add missing ``metadata_options`` parameters (https://github.com/ansible-collections/amazon.aws/pull/715).
- ec2_instance - expanded the use of the automatic retries on temporary failures (https://github.com/ansible-collections/amazon.aws/issues/927).
- ec2_instance - expanded the use of the automatic retries to ``InsuffienctInstanceCapacity`` (https://github.com/ansible-collections/amazon.aws/issues/1038).
- ec2_instance - minor fix for launching an instance in specified AZ when ``vpc_subnet_id`` is not provided (https://github.com/ansible-collections/amazon.aws/pull/1150).
- ec2_instance - refacter ``tower_callback`` code to handle parameter validation as part of the argument specification (https://github.com/ansible-collections/amazon.aws/pull/1199).
- ec2_instance - the ``instance_role`` parameter has been renamed to ``iam_instance_profile`` to better reflect what it is, ``instance_role`` remains as an alias (https://github.com/ansible-collections/amazon.aws/pull/1151).
- ec2_instance - the ``tower_callback`` parameter has been renamed to ``aap_callback``, ``tower_callback`` remains as an alias.  This change should have no observable effect for users outside the module documentation (https://github.com/ansible-collections/amazon.aws/pull/1199).
- ec2_key - ``resource_tags`` has been added as an alias for the ``tags`` parameter (https://github.com/ansible-collections/amazon.aws/pull/845).
- ec2_metadata_facts - avoid catching ``Exception``, catch more specific errors instead (https://github.com/ansible-collections/amazon.aws/pull/968).
- ec2_security_group - minor linting fixes (https://github.com/ansible-collections/amazon.aws/pull/968).
- ec2_security_group - set type as ``list`` for rules->group_name as it can accept both ``str`` and ``list`` (https://github.com/ansible-collections/amazon.aws/pull/971).
- ec2_vpc_endpoint - avoid catching ``Exception``, catch more specific errors instead (https://github.com/ansible-collections/amazon.aws/pull/968).
- ec2_vpc_nat_gateway - minor linting fixes (https://github.com/ansible-collections/amazon.aws/pull/968).
- ec2_vpc_net - add support for managing VPCs by ID (https://github.com/ansible-collections/amazon.aws/pull/848).
- ec2_vpc_net_info - handle classic link check for shared VPCs by throwing a warning instead of an error (https://github.com/ansible-collections/amazon.aws/pull/984).
- ec2_vpc_subnet - add support for OutpostArn param (https://github.com/ansible-collections/amazon.aws/pull/598).
- elb_classic_lb - ``resource_tags`` has been added as an alias for the ``tags`` parameter (https://github.com/ansible-collections/amazon.aws/pull/845).
- module.utils.rds - add retry_codes to get_rds_method_attribute return data to use in call_method and add unit tests (https://github.com/ansible-collections/amazon.aws/pull/776).
- module.utils.rds - refactor to utilize get_rds_method_attribute return data (https://github.com/ansible-collections/amazon.aws/pull/776).
- module_utils - add new aliases ``aws_session_token`` and ``session_token`` to the ``security_token`` parameter to be more in-line with the boto SDK (https://github.com/ansible-collections/amazon.aws/pull/631).
- module_utils.rds - Add support and unit tests for addition/removal of IAM roles to/from a db instance in module_utils.rds with waiters (https://github.com/ansible-collections/amazon.aws/pull/714).
- module_utils/acm - Move to jittered backoff (https://github.com/ansible-collections/amazon.aws/pull/946).
- module_utils/elbv2 - ensures that ``ip_address_type`` is set on creation rather than re-setting it after creation (https://github.com/ansible-collections/amazon.aws/pull/940).
- module_utils/elbv2 - uses new waiters with retries for temporary failures (https://github.com/ansible-collections/amazon.aws/pull/940).
- module_utils/waf - Move to jittered backoff (https://github.com/ansible-collections/amazon.aws/pull/946).
- module_utils/waiters - Add waiters to manage eks_nodegroup module (https://github.com/ansible-collections/community.aws/pull/1415).
- s3_bucket - Add ``validate_bucket_name`` option, to control bucket name validation (https://github.com/ansible-collections/amazon.aws/pull/615).
- s3_bucket - ``resource_tags`` has been added as an alias for the ``tags`` parameter (https://github.com/ansible-collections/amazon.aws/pull/845).
- s3_bucket - ``rgw`` was added as an alias for the ``ceph`` parameter for consistency with the ``s3_object`` module (https://github.com/ansible-collections/amazon.aws/pull/994).
- s3_bucket - the ``s3_url`` parameter was merged into the ``endpoint_url`` parameter, ``s3_url`` remains as an alias (https://github.com/ansible-collections/amazon.aws/pull/994).
- s3_bucket - updated module to enable support for setting S3 Bucket Keys for SSE-KMS (https://github.com/ansible-collections/amazon.aws/pull/882).
- s3_object - added the ``sig_v4`` paramater, enbling the user to opt in to signature version 4 for download/get operations. (https://github.com/ansible-collections/amazon.aws/pull/1014)
- s3_object - minor linting fixes (https://github.com/ansible-collections/amazon.aws/pull/968).
- s3_object - the ``rgw`` parameter was renamed to ``ceph`` for consistency with the ``s3_bucket`` module, ``rgw`` remains as an alias (https://github.com/ansible-collections/amazon.aws/pull/994).
- s3_object - the ``s3_url`` parameter was merged into the ``endpoint_url`` parameter, ``s3_url`` remains as an alias (https://github.com/ansible-collections/amazon.aws/pull/994).
- s3_object - updated module to add support for handling file upload to a bucket with ACL disabled (https://github.com/ansible-collections/amazon.aws/pull/921).
- s3_object_info - Added a new module that describes S3 Objects (https://github.com/ansible-collections/amazon.aws/pull/977).
- s3_object_info - minor linting fixes (https://github.com/ansible-collections/amazon.aws/pull/1181).
- various modules - linting fixups (https://github.com/ansible-collections/amazon.aws/pull/953).

ansible.netcommon
~~~~~~~~~~~~~~~~~

- Add grpc connection plugin support.
- Add implementation for content_templates_parser.
- Adds a new option `terminal_errors` in network_cli, that determines how terminal setting failures are handled.
- libssh - Added `password_prompt` option to override default "password:" prompt used by pylibssh

ansible.utils
~~~~~~~~~~~~~

- Add support for content template parser
- Added new connection base class similar to ansible.netcommon's NetworkConnectionBase without the network-specific option masking (https://github.com/ansible-collections/ansible.utils/pull/213).
- ipsubnet - the index parameter should only ever be an integer if it is provided. this changes the argument type from str to int.

ansible.windows
~~~~~~~~~~~~~~~

- Raise minimum Ansible version to ``2.11`` or newer
- setup - also read ``*.json`` files in ``fact_path`` as raw JSON text in addition to ``.ps1`` scripts
- win_acl - Added the ``follow`` parameter with will follow the symlinks and junctions before applying ACLs to change the target instead of the link
- win_acl_inheritance - support for setting inheritance for registry keys
- win_command - Added the ``argv`` module option for specifying the command to run as a list to be escaped rather than the free form input
- win_command - Added the ``cmd`` module option for specifying the command to run as a module option rather than the free form input
- win_command - Migrated to the newer Ansible.Basic style module to improve module invocation output
- win_powershell - Add support for setting diff output with ``$Ansible.Diff`` in the script
- win_stat - Added ``get_size`` to control whether ``win_stat`` will calculate the size of files or directories - https://github.com/ansible-collections/ansible.windows/issues/384
- win_uri - Use SHA256 for file idempotency checks instead of SHA1

arista.eos
~~~~~~~~~~

- Add support for setting encryption_password for BGP neighbors in bgp_global module
- Add validate_config option to diff_against in eos_config

chocolatey.chocolatey
~~~~~~~~~~~~~~~~~~~~~

- All collection modules - assorted style/linting fixes in documentation and scripts.

cisco.aci
~~~~~~~~~

- Add aci_bulk_static_binding_to_epg module to bind multiple interfaces to an EPG in one API call
- Add aci_l3out_logical_interface_profile_ospf_policy module to apply ospfIfP policy to L3out logical interface profile (#301)
- Add aci_ntp_policy and aci_ntp_server modules (#229)
- Add cisco.aci.interface_range lookup plugin for interface range handling (#302)
- Add new aci_aaa_ssh_auth, aci_aaa_user_domain and aci_aaa_user_role modules (#223)
- Add support for active/stanby vmm uplinks in aci_epg_to_domain
- Add support for aggregate attribute, scope default and "import-rtctrl" to scope choices in aci_l3out_extsubnet module (#260)
- Added fex_port_channel and fex_vpc interface types to aci_access_port_to_interface_policy_leaf_profile (#241)
- Adding missing options to aci_epg_to_domain

cisco.dnac
~~~~~~~~~~

- Update dnacentersdk requirement from 2.4.7 to 2.5.0
- assign_device_to_site - new module.
- buildings_planned_access_points_info - new module.
- business_sda_virtual_network_summary_info - new module.
- event_config_connector_types_info - new module.
- event_email_config_create - new module.
- event_email_config_update - new module.
- event_webhook_create - new module.
- event_webhook_update - new module.
- file_import - new module.
- interface_info - new module.
- interface_operation_create - new module.
- interface_update - new module.
- lan_automation_count_info - new module.
- lan_automation_create - new module.
- lan_automation_delete - new module.
- lan_automation_log_info - new module.
- lan_automation_status_info - new module.
- network_device_custom_prompt - new module.
- network_device_custom_prompt_info - new module.
- pnp_intent - new module.
- site_intent - new module.
- swim_intent - new module.
- template_intent - new module.

cisco.ios
~~~~~~~~~

- Also collect a list of serial numbers comprised in a vss system as virtual_switch_serialnums
- Fixing Detection of Virtual Switch System to facts (https://github.com/ansible-collections/cisco.ios/pull/471)
- ios_interfaces - Add purged state to ios_interfaces.
- ios_l2_interfaces - Add vlan_name attribute to access.
- ios_l2_interfaces - Add vlan_name, vlan_tag attribute to voice.
- ios_ping - Add ipv6 options.

cisco.iosxr
~~~~~~~~~~~

- Add label and comment to commit_confirmed functionality in IOSXR.
- Add support for grpc connection plugin
- `iosxr_ping` - Add iosxr_ping module.
- iosxr_bgp_neighbor_address_family - add extra supported values l2vpn, link-state, vpnv4, vpnv6 to afi attribute.

cisco.ise
~~~~~~~~~

- Update requirements to use ciscoisesdk >= 2.0.3.

cisco.meraki
~~~~~~~~~~~~

- Add GPLv3 license. Always was GPLv3, but didn't have the file.
- Change shebang in Sublime utils to point to env instead of direct to the path
- meraki_action_batch - New module for CRUD operations on Meraki Action Batches
- meraki_alert - Change type for opbject to alert_type in examples
- meraki_ms_access_policies - New module to create, delete, update Access Policies in the Switch settings
- meraki_mx_network_vlan_settings - New module to enable or disable VLANs on a network
- meraki_mx_third_party_vpn_peers - New module for managing third party VPM peers
- meraki_network - Add support for `copy_from_network_id`.
- meraki_ssid - Add support for `ap_availability_tags`.
- meraki_ssid - Add support for `available_on_all_aps`
- meraki_ssid - Add support for `lan_isolation_enabled`.
- meraki_ssid - Add support for `visible`.
- meraki_switchport - Add support for flexible stacking

cisco.mso
~~~~~~~~~

- Add aci_remote_location module (#259)
- Add mso_backup_schedule module (#250)
- Add mso_chema_template_contract_service_graph module (#257)
- Add mso_schema_template_service_graph, mso_schema_site_service_graph and mso_service_node_type modules (#243)
- Add primary attribute to mso_schema_site_bd_subnet (#254)

cisco.nxos
~~~~~~~~~~

- `nxos_l3_interfaces` - Add support for toggling ipv6 redirects (https://github.com/ansible-collections/cisco.nxos/issues/569).
- `nxos_snmp_server` - Add support for localizedV2key (https://github.com/ansible-collections/cisco.nxos/issues/415).
- `nxos_snmp_server` - Add support for sha-256 based based user authentication.

community.aws
~~~~~~~~~~~~~

- acm_certificate - Move to jittered backoff (https://github.com/ansible-collections/amazon.aws/pull/946).
- acm_certificate_info - Move to jittered backoff (https://github.com/ansible-collections/amazon.aws/pull/946).
- api_gateway_domain - Move to jittered backoff (https://github.com/ansible-collections/community.aws/pull/1386).
- autoscaling_group_info - minor sanity test fixes (https://github.com/ansible-collections/community.aws/pull/1410).
- aws_acm - ``resource_tags`` has been added as an alias for the ``tags`` parameter (https://github.com/ansible-collections/community.aws/pull/1185).
- aws_acm - the ``aws_acm`` module has been renamed to ``acm_certificate``, ``aws_acm`` remains as an alias (https://github.com/ansible-collections/community.aws/pull/1263).
- aws_acm_info - the ``aws_acm_info`` module has been renamed to ``acm_certificate_info``, ``aws_acm_info`` remains as an alias (https://github.com/ansible-collections/community.aws/pull/1263).
- aws_api_gateway - the ``aws_api_gateway`` module has been renamed to ``api_gateway``, ``aws_api_gateway`` remains as an alias (https://github.com/ansible-collections/community.aws/pull/1288).
- aws_api_gateway_domain - the ``aws_api_gateway_domain`` module has been renamed to ``api_gateway_domain``, ``aws_api_gateway_domain`` remains as an alias (https://github.com/ansible-collections/community.aws/pull/1288).
- aws_application_scaling_policy - the ``aws_application_scaling_policy`` module has been renamed to ``application_autoscaling_policy``, ``aws_application_scaling_policy`` remains as an alias (https://github.com/ansible-collections/community.aws/pull/1314).
- aws_batch_compute_environment - the ``aws_batch_compute_environment`` module has been renamed to ``batch_compute_environment``, ``aws_batch_compute_environment`` remains as an alias (https://github.com/ansible-collections/community.aws/pull/1272).
- aws_batch_job_definition - the ``aws_batch_job_definition`` module has been renamed to ``batch_job_definition``, ``aws_batch_job_definition`` remains as an alias (https://github.com/ansible-collections/community.aws/pull/1272).
- aws_batch_job_queue - the ``aws_batch_job_queue`` module has been renamed to ``batch_job_queue``, ``aws_batch_job_queue`` remains as an alias (https://github.com/ansible-collections/community.aws/pull/1272).
- aws_codebuild - add support for ``purge_tags`` parameter (https://github.com/ansible-collections/community.aws/pull/1221).
- aws_codebuild - add the ``resource_tags`` parameter which takes the dictionary format for tags instead of the list of dictionaries format (https://github.com/ansible-collections/community.aws/pull/1221).
- aws_codebuild - add the ``resource_tags`` return value which returns the standard dictionary format for tags instead of the list of dictionaries format (https://github.com/ansible-collections/community.aws/pull/1221).
- aws_codebuild - the ``aws_codebuild`` module has been renamed to ``codebuild_project``, ``aws_codebuild`` remains as an alias (https://github.com/ansible-collections/community.aws/pull/1308).
- aws_codebuild - the ``source`` and ``artifacts`` parameters are now optional unless creating a new project (https://github.com/ansible-collections/community.aws/pull/1221).
- aws_codecommit - the ``aws_codecommit`` module has been renamed to ``codecommit_repository``, ``aws_codecommit`` remains as an alias (https://github.com/ansible-collections/community.aws/pull/1308).
- aws_codepipeline - the ``aws_codepipeline`` module has been renamed to ``codepipeline``, ``aws_codepipeline`` remains as an alias (https://github.com/ansible-collections/community.aws/pull/1308).
- aws_config_aggregation_authorization - the ``aws_config_aggregation_authorization`` module has been renamed to ``config_aggregation_authorization``, ``aws_config_aggregation_authorization`` remains as an alias (https://github.com/ansible-collections/community.aws/pull/1305).
- aws_config_aggregator - the ``aws_config_aggregator`` module has been renamed to ``config_aggregator``, ``aws_config_aggregator`` remains as an alias (https://github.com/ansible-collections/community.aws/pull/1305).
- aws_config_delivery_channel - the ``aws_config_delivery_channel`` module has been renamed to ``config_delivery_channel``, ``aws_config_delivery_channel`` remains as an alias (https://github.com/ansible-collections/community.aws/pull/1305).
- aws_config_recorder - the ``aws_config_recorder`` module has been renamed to ``config_recorder``, ``aws_config_recorder`` remains as an alias (https://github.com/ansible-collections/community.aws/pull/1305).
- aws_config_rule - the ``aws_config_rule`` module has been renamed to ``config_rule``, ``aws_config_rule`` remains as an alias (https://github.com/ansible-collections/community.aws/pull/1305).
- aws_direct_connect_confirm_connection - the ``aws_direct_connect_confirm_connection`` module has been renamed to ``directconnect_confirm_connection``, ``aws_direct_connect_confirm_connection`` remains as an alias (https://github.com/ansible-collections/community.aws/pull/1286).
- aws_direct_connect_connection - the ``aws_direct_connect_connection`` module has been renamed to ``directconnect_connection``, ``aws_direct_connect_connection`` remains as an alias (https://github.com/ansible-collections/community.aws/pull/1286).
- aws_direct_connect_gateway - the ``aws_direct_connect_gateway`` module has been renamed to ``directconnect_gateway``, ``aws_direct_connect_gateway`` remains as an alias (https://github.com/ansible-collections/community.aws/pull/1286).
- aws_direct_connect_link_aggregation_group - the ``aws_direct_connect_link_aggregation_group`` module has been renamed to ``directconnect_link_aggregation_group``, ``aws_direct_connect_link_aggregation_group`` remains as an alias (https://github.com/ansible-collections/community.aws/pull/1286).
- aws_direct_connect_virtual_interface - the ``aws_direct_connect_virtual_interface`` module has been renamed to ``directconnect_virtual_interface``, ``aws_direct_connect_virtual_interface`` remains as an alias (https://github.com/ansible-collections/community.aws/pull/1286).
- aws_eks_cluster - the ``aws_eks_cluster`` module has been renamed to ``eks_cluster``, ``aws_eks_cluster`` remains as an alias (https://github.com/ansible-collections/community.aws/pull/1269).
- aws_glue_connection - added new ``raw_connection_parameters`` return key which doesn't snake case the connection parameters (https://github.com/ansible-collections/community.aws/pull/518).
- aws_glue_connection - the ``aws_glue_connection`` module has been renamed to ``glue_connection``, ``aws_glue_connection`` remains as an alias (https://github.com/ansible-collections/community.aws/pull/1300).
- aws_glue_crawler - the ``aws_glue_crawler`` module has been renamed to ``glue_crawler``, ``aws_glue_crawler`` remains as an alias (https://github.com/ansible-collections/community.aws/pull/1300).
- aws_glue_job - ``resource_tags`` has been added as an alias for the ``tags`` parameter (https://github.com/ansible-collections/community.aws/pull/1182).
- aws_glue_job - the ``aws_glue_job`` module has been renamed to ``glue_job``, ``aws_glue_job`` remains as an alias (https://github.com/ansible-collections/community.aws/pull/1300).
- aws_inspector_target - the ``aws_inspector_target`` module has been renamed to ``inspector_target``, ``aws_inspector_target`` remains as an alias (https://github.com/ansible-collections/community.aws/pull/1318).
- aws_kms - ``resource_tags`` has been added as an alias for the ``tags`` parameter (https://github.com/ansible-collections/community.aws/pull/1185).
- aws_kms - add extra key/value pair to return data (key_policies) to return each policy as a dictionary rather than json string (https://github.com/ansible-collections/community.aws/pull/1052).
- aws_kms - fix some bugs in integration tests and add check mode support for key rotation as well as document issues with time taken for requested changes to be reflected on AWS (https://github.com/ansible-collections/community.aws/pull/1052).
- aws_kms - the ``aws_kms`` module has been renamed to ``kms_key``, ``aws_kms`` remains as an alias (https://github.com/ansible-collections/community.aws/pull/1284).
- aws_kms - the default value for ``tags`` has been updated, to remove all tags the ``tags`` parameter must be explicitly set to the empty dict ``{}`` and ``purge_tags`` to ``True`` (https://github.com/ansible-collections/community.aws/pull/1183).
- aws_kms_info - the ``aws_kms_info`` module has been renamed to ``kms_key_info``, ``aws_kms_info`` remains as an alias (https://github.com/ansible-collections/community.aws/pull/1284).
- aws_msk_cluster - ``resource_tags`` has been added as an alias for the ``tags`` parameter (https://github.com/ansible-collections/community.aws/pull/1182).
- aws_msk_cluster - the ``aws_msk_cluster`` module has been renamed to ``msk_cluster``, ``aws_msk_cluster`` remains as an alias (https://github.com/ansible-collections/community.aws/pull/1311).
- aws_msk_config - the ``aws_msk_config`` module has been renamed to ``msk_config``, ``aws_msk_config`` remains as an alias (https://github.com/ansible-collections/community.aws/pull/1311).
- aws_s3_bucket_info - the ``aws_s3_bucket_info`` module has been renamed to ``s3_bucket_info``, ``aws_s3_bucket_info`` remains as an alias (https://github.com/ansible-collections/community.aws/pull/1271).
- aws_s3_cors - the ``aws_s3_cors`` module has been renamed to ``s3_cors``, ``aws_s3_cors`` remains as an alias (https://github.com/ansible-collections/community.aws/pull/1271).
- aws_secret - ``resource_tags`` has been added as an alias for the ``tags`` parameter (https://github.com/ansible-collections/community.aws/pull/1182).
- aws_secret - addition of the ``purge_tags`` parameter (https://github.com/ansible-collections/community.aws/issues/1146).
- aws_secret - the ``aws_secret`` module has been renamed to ``secretsmanager_secret``, ``aws_secret`` remains as an alias (https://github.com/ansible-collections/community.aws/pull/1315).
- aws_ses_identity - the ``aws_ses_identity`` module has been renamed to ``ses_identity``, ``aws_ses_identity`` remains as an alias (https://github.com/ansible-collections/community.aws/pull/1264).
- aws_ses_identity_policy - the ``aws_ses_identity_policy`` module has been renamed to ``ses_identity_policy``, ``aws_ses_identity_policy`` remains as an alias (https://github.com/ansible-collections/community.aws/pull/1264).
- aws_ses_rule_set - the ``aws_ses_rule_set`` module has been renamed to ``ses_rule_set``, ``aws_ses_rule_set`` remains as an alias (https://github.com/ansible-collections/community.aws/pull/1264).
- aws_sgw_info - the ``aws_sgw_info`` module has been renamed to ``storagegateway_info``, ``aws_sgw_info`` remains as an alias (https://github.com/ansible-collections/community.aws/pull/1301).
- aws_ssm_parameter_store - add parameter_metadata to the returned values (https://github.com/ansible-collections/community.aws/pull/1241).
- aws_ssm_parameter_store - added support for check_mode (https://github.com/ansible-collections/community.aws/pull/1309).
- aws_ssm_parameter_store - the ``aws_ssm_parameter_store`` module has been renamed to ``ssm_parameter``, ``aws_ssm_parameter_store`` remains as an alias (https://github.com/ansible-collections/community.aws/pull/1313).
- aws_step_functions_state_machine - ``resource_tags`` has been added as an alias for the ``tags`` parameter (https://github.com/ansible-collections/community.aws/pull/1182).
- aws_step_functions_state_machine - the ``aws_step_functions_state_machine`` module has been renamed to ``stepfunctions_state_machine``, ``aws_step_functions_state_machine`` remains as an alias (https://github.com/ansible-collections/community.aws/pull/1310).
- aws_step_functions_state_machine_execution - the ``aws_step_functions_state_machine_execution`` module has been renamed to ``stepfunctions_state_machine_execution``, ``aws_step_functions_state_machine_execution`` remains as an alias (https://github.com/ansible-collections/community.aws/pull/1310).
- aws_waf_condition - the ``aws_waf_condition`` module has been renamed to ``waf_condition``, ``aws_waf_condition`` remains as an alias (https://github.com/ansible-collections/community.aws/pull/1299).
- aws_waf_info - the ``aws_waf_info`` module has been renamed to ``waf_info``, ``aws_waf_info`` remains as an alias (https://github.com/ansible-collections/community.aws/pull/1299).
- aws_waf_rule - the ``aws_waf_rule`` module has been renamed to ``waf_rule``, ``aws_waf_rule`` remains as an alias (https://github.com/ansible-collections/community.aws/pull/1299).
- aws_waf_web_acl - the ``aws_waf_web_acl`` module has been renamed to ``waf_web_acl``, ``aws_waf_web_acl`` remains as an alias (https://github.com/ansible-collections/community.aws/pull/1299).
- cloudfront_distribution - ``resource_tags`` has been added as an alias for the ``tags`` parameter (https://github.com/ansible-collections/community.aws/pull/1185).
- cloudfront_distribution - minor sanity test fixes (https://github.com/ansible-collections/community.aws/pull/1410).
- cloudfront_distribution - the default value for ``tags`` has been updated, to remove all tags the ``tags`` parameter must be explicitly set to the empty dict ``{}`` and ``purge_tags`` to ``True`` (https://github.com/ansible-collections/community.aws/pull/1183).
- cloudfront_info - the ``cloudfront_info`` module has been renamed to ``cloudfront_distribution_info``, ``cloudfront_info`` remains as an alias (https://github.com/ansible-collections/community.aws/pull/1352).
- cloudfront_origin_access_identity - minor sanity test fixes (https://github.com/ansible-collections/community.aws/pull/1410).
- cloudtrail - ``resource_tags`` has been added as an alias for the ``tags`` parameter (https://github.com/ansible-collections/community.aws/pull/1219).
- cloudtrail - minor sanity test fixes (https://github.com/ansible-collections/community.aws/pull/1410).
- cloudtrail - the default value for ``tags`` has been updated, to remove all tags the ``tags`` parameter must be explicitly set to the empty dict ``{}`` (https://github.com/ansible-collections/community.aws/pull/1219).
- cloudtrail - updated to pass tags as part of the create API call rather than tagging the trail after creation (https://github.com/ansible-collections/community.aws/pull/1219).
- cloudwatchevent_rule - Added ``targets.input_transformer.input_paths_map`` and ``targets.input_transformer.input_template`` parameters to support configuring on CloudWatch event rule input transformation (https://github.com/ansible-collections/community.aws/pull/623).
- cloudwatchevent_rule - Applied validation of ``targets`` arguments (https://github.com/ansible-collections/community.aws/issues/201).
- cloudwatchlogs_log_group - Added check_mode support (https://github.com/ansible-collections/community.aws/pull/1373).
- cloudwatchlogs_log_group - adds support for returning tags (https://github.com/ansible-collections/community.aws/pull/1233).
- cloudwatchlogs_log_group - adds support for updating tags (https://github.com/ansible-collections/community.aws/pull/1233).
- cloudwatchlogs_log_group - now consistently returns the values as defined in the return documentation (https://github.com/ansible-collections/community.aws/pull/1233).
- cloudwatchlogs_log_group_info - adds support for returning tags (https://github.com/ansible-collections/community.aws/pull/1233).
- community.aws modules - the ``ec2_url`` parameter has been renamed to ``endpoint_url`` for consistency, ``ec2_url`` remains as an alias (https://github.com/ansible-collections/amazon.aws/pull/992).
- data_pipeline - ``resource_tags`` has been added as an alias for the ``tags`` parameter (https://github.com/ansible-collections/community.aws/pull/1204).
- dms_endpoint - ``endpointtype`` and ``enginename`` no longer required when deleting an endpoint (https://github.com/ansible-collections/community.aws/pull/1234).
- dms_endpoint - ``resource_tags`` added as an alias for ``tags`` (https://github.com/ansible-collections/community.aws/pull/1234).
- dms_endpoint - added support for ``purge_tags`` (https://github.com/ansible-collections/community.aws/pull/1234).
- dms_endpoint - now returns details of the endpoint (https://github.com/ansible-collections/community.aws/pull/1234).
- dynamodb_table - ``resource_tags`` has been added as an alias for the ``tags`` parameter (https://github.com/ansible-collections/community.aws/pull/1199).
- ec2_ami_copy - ``resource_tags`` has been added as an alias for the ``tags`` parameter (https://github.com/ansible-collections/community.aws/pull/1204).
- ec2_asg - add check mode support (https://github.com/ansible-collections/community.aws/pull/1033).
- ec2_asg - bugfix to make test setup run once (https://github.com/ansible-collections/community.aws/pull/1061).
- ec2_asg - the ``ec2_asg`` module has been renamed to ``autoscaling_group``, ``ec2_asg`` remains as an alias (https://github.com/ansible-collections/community.aws/pull/1294).
- ec2_asg_info - the ``ec2_asg_info`` module has been renamed to ``autoscaling_group_info``, ``ec2_asg_info`` remains as an alias (https://github.com/ansible-collections/community.aws/pull/1294).
- ec2_asg_instance_refresh - the ``ec2_asg_instance_refresh`` module has been renamed to ``autoscaling_instance_refresh``, ``ec2_asg_instance_refresh`` remains as an alias (https://github.com/ansible-collections/community.aws/pull/1294).
- ec2_asg_instance_refresh_info - the ``ec2_asg_instance_refresh_info`` module has been renamed to ``autoscaling_instance_refresh_info``, ``ec2_asg_instance_refresh_info`` remains as an alias (https://github.com/ansible-collections/community.aws/pull/1294).
- ec2_asg_lifecycle_hook - Added check_mode support (https://github.com/ansible-collections/community.aws/pull/1060).
- ec2_asg_lifecycle_hook - add integration tests (https://github.com/ansible-collections/community.aws/pull/1048).
- ec2_asg_lifecycle_hook - module now returns info about Life Cycle Hook (https://github.com/ansible-collections/community.aws/pull/1048).
- ec2_asg_lifecycle_hook - the ``ec2_asg_lifecycle_hook`` module has been renamed to ``autoscaling_lifecycle_hool``, ``ec2_asg_lifecycle_hook`` remains as an alias (https://github.com/ansible-collections/community.aws/pull/1294).
- ec2_asg_scheduled_action - the ``ec2_asg_scheduled_action`` module has been renamed to ``autoscaling_scheduled_action``, ``ec2_asg_scheduled_action`` remains as an alias (https://github.com/ansible-collections/community.aws/pull/1294).
- ec2_eip - ``resource_tags`` has been added as an alias for the ``tags`` parameter (https://github.com/ansible-collections/community.aws/pull/1182).
- ec2_launch_template - Adds support for specifying the ``source_version`` upon which template updates are based (https://github.com/ansible-collections/community.aws/pull/239).
- ec2_launch_template - ``resource_tags`` has been added as an alias for the ``tags`` parameter (https://github.com/ansible-collections/community.aws/pull/1204).
- ec2_lc - the ``ec2_lc`` module has been renamed to ``autoscaling_launch_config``, ``ec2_lc`` remains as an alias (https://github.com/ansible-collections/community.aws/pull/1294).
- ec2_lc_find - the ``ec2_lc_find`` module has been renamed to ``autoscaling_launch_config_find``, ``ec2_lc_find`` remains as an alias (https://github.com/ansible-collections/community.aws/pull/1294).
- ec2_lc_info - the ``ec2_lc_info`` module has been renamed to ``autoscaling_launch_config_info``, ``ec2_lc_info`` remains as an alias (https://github.com/ansible-collections/community.aws/pull/1294).
- ec2_metric_alarm - the ``ec2_metric_alarm`` module has been renamed to ``cloudwatch_metric_alarm``, ``ec2_metric_alarm`` remains as an alias (https://github.com/ansible-collections/community.aws/pull/1304).
- ec2_scaling_policy - add TargetTrackingScaling as a scaling policy option (https://github.com/ansible-collections/community.aws/pull/771)
- ec2_scaling_policy - the ``ec2_scaling_policy`` module has been renamed to ``autoscaling_policy``, ``ec2_scaling_policy`` remains as an alias (https://github.com/ansible-collections/community.aws/pull/1294).
- ec2_snapshot_copy - ``resource_tags`` has been added as an alias for the ``tags`` parameter (https://github.com/ansible-collections/community.aws/pull/1201).
- ec2_snapshot_copy - updated to pass tags as part of the copy API call rather than tagging the snapshot after creation (https://github.com/ansible-collections/community.aws/pull/1201).
- ec2_transit_gateway - code updated to use common ``ensure_ec2_tags`` helper (https://github.com/ansible-collections/community.aws/pull/1183).
- ec2_transit_gateway - the default value for ``tags`` has been updated, to remove all tags the ``tags`` parameter must be explicitly set to the empty dict ``{}`` (https://github.com/ansible-collections/community.aws/pull/1183).
- ec2_transit_gateway - wait and retry if API returns an IncorrectState error.
- ec2_vpc_nacl - ``resource_tags`` has been added as an alias for the ``tags`` parameter (https://github.com/ansible-collections/community.aws/pull/1189).
- ec2_vpc_nacl - add support for ``purge_tags`` parameter (https://github.com/ansible-collections/community.aws/pull/1189).
- ec2_vpc_nacl - minor sanity test fixes (https://github.com/ansible-collections/community.aws/pull/1410).
- ec2_vpc_nacl - the default value for ``tags`` has been updated, to remove all tags the ``tags`` parameter must be explicitly set to the empty dict ``{}`` and ``purge_tags`` to ``True`` (https://github.com/ansible-collections/community.aws/pull/1189).
- ec2_vpc_peer - ``resource_tags`` has been added as an alias for the ``tags`` parameter (https://github.com/ansible-collections/community.aws/pull/1182).
- ec2_vpc_vgw - add support for ``purge_tags`` parameter (https://github.com/ansible-collections/community.aws/pull/1232).
- ec2_vpc_vgw - the default behaviour for ``tags`` has been updated, to remove all tags the ``tags`` parameter must be explicitly set to the empty dict ``{}`` and ``purge_tags`` to ``True`` (https://github.com/ansible-collections/community.aws/pull/1232).
- ec2_vpc_vgw - updated to set tags as part of VGW creation instead of tagging the VGW after creation (https://github.com/ansible-collections/community.aws/pull/1232).
- ec2_vpc_vgw_info - added ``resource_tags`` to the return values (https://github.com/ansible-collections/community.aws/pull/1232).
- ec2_vpc_vgw_info - updated to not throw an error when run in check_mode (https://github.com/ansible-collections/community.aws/issues/137).
- ec2_vpc_vpn - ``resource_tags`` has been added as an alias for the ``tags`` parameter (https://github.com/ansible-collections/community.aws/pull/1185).
- ec2_vpc_vpn - minor tweak to ``VPNConnectionException`` to pass message through to the superclass (https://github.com/ansible-collections/community.aws/pull/1407).
- ec2_vpc_vpn - the default value for ``tags`` has been updated, to remove all tags the ``tags`` parameter must be explicitly set to the empty dict ``{}`` and ``purge_tags`` to ``True`` (https://github.com/ansible-collections/community.aws/pull/1183).
- ecs_ecr - Will now return repository permission policy if it exists, even if we did not create or modify it. (https://github.com/ansible-collections/community.aws/pull/1171).
- ecs_ecr - add ``force_absent`` parameter for removing repositories that contain images (https://github.com/ansible-collections/community.aws/pull/1316).
- ecs_service - Now allows for a ``capacity_provider_strategy`` to be utilized when creating/updating a service (https://github.com/ansible-collections/community.aws/pull/1181).
- ecs_service - ``deployment_circuit_breaker`` has been added as a supported feature (https://github.com/ansible-collections/community.aws/pull/1215).
- ecs_service - add ``service`` alias to address the ecs service name with the same parameter as the ecs_service_info module is doing (https://github.com/ansible-collections/community.aws/pull/1187).
- ecs_service - add ``wait`` parameter and waiter for deleting services (https://github.com/ansible-collections/community.aws/pull/1209).
- ecs_service - added ``tags`` and ``tag_propagation`` support to the module (https://github.com/ansible-collections/community.aws/pull/543).
- ecs_service - added parameter ``deployment_controller`` so service can be controlled by Code Deploy (https://github.com/ansible-collections/community.aws/pull/340).
- ecs_service_info - add ``name`` alias to address the ecs service name with the same parameter as the ecs_service module is doing (https://github.com/ansible-collections/community.aws/pull/1187).
- ecs_tag - ``resource_tags`` has been added as an alias for the ``tags`` parameter (https://github.com/ansible-collections/community.aws/pull/1184).
- ecs_task - ``resource_tags`` has been added as an alias for the ``tags`` parameter (https://github.com/ansible-collections/community.aws/pull/1204).
- ecs_task - add ``wait`` parameter and waiter for running and stopping tasks (https://github.com/ansible-collections/community.aws/pull/1209).
- efs - the default value for ``tags`` has been updated, to remove all tags the ``tags`` parameter must be explicitly set to the empty dict ``{}`` (https://github.com/ansible-collections/community.aws/pull/1183).
- efs_tag - ``resource_tags`` has been added as an alias for the ``tags`` parameter (https://github.com/ansible-collections/community.aws/pull/1184).
- eks_fargate_profile - minor sanity test fixes (https://github.com/ansible-collections/community.aws/pull/1410).
- eks_fargate_profile - the default value for ``tags`` has been updated, to remove all tags the ``tags`` parameter must be explicitly set to the empty dict ``{}`` (https://github.com/ansible-collections/community.aws/pull/1183).
- elasticache_info - added ``replication_group`` to the returned information for an elasticache cluster (https://github.com/ansible-collections/community.aws/pull/646).
- elb_application_lb - ``resource_tags`` has been added as an alias for the ``tags`` parameter (https://github.com/ansible-collections/community.aws/pull/1182).
- elb_network_lb - ``resource_tags`` has been added as an alias for the ``tags`` parameter (https://github.com/ansible-collections/community.aws/pull/1182).
- elb_target_group - explicitly setting the ``tags`` parameter to the empty dict ``{}`` will now remove all tags unles ``purge_tags`` is explicitly set to ``False`` (https://github.com/ansible-collections/community.aws/pull/1183).
- elb_target_group - instead of completely ignoring ``health_check_path`` and ``successful_response_codes`` if ``health_check_protocol`` is not supplied, now raises an error (https://github.com/ansible-collections/community.aws/issues/29).
- iam_policy - added support for ``--diff`` mode (https://github.com/ansible-collections/community.aws/issues/560).
- iam_policy - attempts to continue when read requests are denied by IAM policy (https://github.com/ansible-collections/community.aws/pull/1375).
- iam_policy - update broken examples and add RETURN section to documentation; add extra integration tests for idempotency check mode runs (https://github.com/ansible-collections/community.aws/pull/1093).
- iam_role - ``resource_tags`` has been added as an alias for the ``tags`` parameter (https://github.com/ansible-collections/community.aws/pull/1182).
- iam_role - delete inline policies prior to deleting role (https://github.com/ansible-collections/community.aws/pull/1054).
- iam_role - remove global vars and refactor accordingly (https://github.com/ansible-collections/community.aws/pull/1054).
- iam_server_certificate - the deprecation for the ``iam_cert`` alias has been extended from release 4.0.0 to release 5.0.0 (https://github.com/ansible-collections/community.aws/pull/1257).
- iam_server_certificate - the deprecations for ``cert_chain``, ``cert``, ``key`` and ``dup_ok`` have been extended from release 4.0.0 to release 5.0.0 (https://github.com/ansible-collections/community.aws/pull/1256).
- iam_user - ``resource_tags`` has been added as an alias for the ``tags`` parameter (https://github.com/ansible-collections/community.aws/pull/1182).
- iam_user - add ``user`` value to return data structure to deprecate old ``iam_user`` (https://github.com/ansible-collections/community.aws/pull/1059).
- lambda - ``resource_tags`` has been added as an alias for the ``tags`` parameter (https://github.com/ansible-collections/community.aws/pull/1202).
- lambda - add kms_key_arn parameter (https://github.com/ansible-collections/community.aws/pull/1108).
- lambda - the behavior for ``tags`` has been updated, to remove all tags the ``tags`` parameter must be explicitly set to the empty dict ``{}`` and ``purge_tags`` to ``True`` (https://github.com/ansible-collections/community.aws/pull/1202).
- lambda_info - add return key ``functions`` which returns a list of dictionaries instead of the previously returned ``function``, which returned a dictionary of dictionaries (https://github.com/ansible-collections/community.aws/pull/1239).
- lambda_info - now returns basic configuration information of each lambda function, regardless of query (https://github.com/ansible-collections/community.aws/pull/1239).
- rds_cluster - ``resource_tags`` has been added as an alias for the ``tags`` parameter (https://github.com/ansible-collections/community.aws/pull/1182).
- rds_instance - ``resource_tags`` has been added as an alias for the ``tags`` parameter (https://github.com/ansible-collections/community.aws/pull/1182).
- rds_instance - add ``deletion_protection`` parameter (https://github.com/ansible-collections/community.aws/pull/1105).
- rds_instance - add snapshot tests to test suite to test restoring db from snapshot (https://github.com/ansible-collections/community.aws/pull/1081).
- rds_instance - add support for addition/removal of iam roles to db instance (https://github.com/ansible-collections/community.aws/pull/1002).
- rds_instance_info - add retries on common AWS failures (https://github.com/ansible-collections/community.aws/pull/1026).
- rds_instance_snapshot - ``resource_tags`` has been added as an alias for the ``tags`` parameter (https://github.com/ansible-collections/community.aws/pull/1200).
- rds_instance_snapshot - add ``check_mode`` (https://github.com/ansible-collections/community.aws/pull/789).
- rds_instance_snapshot - add copy_db_snapshot functionality (https://github.com/ansible-collections/community.aws/pull/1078).
- rds_instance_snapshot - add integration tests (https://github.com/ansible-collections/community.aws/pull/789).
- rds_instance_snapshot - the deprecation for the ``rds_snapshot`` alias has been extended from release 4.0.0 to release 5.0.0 (https://github.com/ansible-collections/community.aws/pull/1257).
- rds_instance_snapshot - update module to use handlers defined in module_utils/rds.py (https://github.com/ansible-collections/community.aws/pull/789).
- rds_option_group - ``resource_tags`` has been added as an alias for the ``tags`` parameter (https://github.com/ansible-collections/community.aws/pull/1182).
- rds_param_group - ``resource_tags`` has been added as an alias for the ``tags`` parameter (https://github.com/ansible-collections/community.aws/pull/1185).
- rds_param_group - the default value for ``tags`` has been updated, to remove all tags the ``tags`` parameter must be explicitly set to the empty dict ``{}`` and ``purge_tags`` to ``True`` (https://github.com/ansible-collections/community.aws/pull/1183).
- rds_subnet_group - ``resource_tags`` has been added as an alias for the ``tags`` parameter (https://github.com/ansible-collections/community.aws/pull/1182).
- redshift - ``resource_tags`` has been added as an alias for the ``tags`` parameter (https://github.com/ansible-collections/community.aws/pull/1182).
- redshift - minor sanity test fixes (https://github.com/ansible-collections/community.aws/pull/1410).
- route53 - add support for GeoLocation param (https://github.com/ansible-collections/amazon.aws/pull/1117).
- route53_health_check - Added new parameter ``health_check_id`` with alias ``id`` to allow update and delete health check by ID (https://github.com/ansible-collections/community.aws/pull/1143).
- route53_health_check - Added new parameter ``use_unique_names`` used with new parameter ``health_check_name`` with alias ``name`` to set health check name as unique identifier (https://github.com/ansible-collections/community.aws/pull/1143).
- route53_health_check - ``resource_tags`` has been added as an alias for the ``tags`` parameter (https://github.com/ansible-collections/community.aws/pull/1185).
- route53_info - add RETURN section to documentation (https://github.com/ansible-collections/community.aws/pull/1240).
- route53_zone - ``resource_tags`` has been added as an alias for the ``tags`` parameter (https://github.com/ansible-collections/community.aws/pull/1185).
- s3_bucket_info - minor sanity test fixes (https://github.com/ansible-collections/community.aws/pull/1410).
- s3_sync - improves error handling during ``HEAD`` operation to compare existing files (https://github.com/ansible-collections/community.aws/issues/58).
- secretsmanager_secret - add support for storing JSON in secrets (https://github.com/ansible-collections/community.aws/issues/656).
- sns_topic - Added ``attributes`` parameter to ``subscriptions`` items with support for RawMessageDelievery (SQS)
- sqs_queue - ``resource_tags`` has been added as an alias for the ``tags`` parameter (https://github.com/ansible-collections/community.aws/pull/1185).
- waf_condition - Move to jittered backoff (https://github.com/ansible-collections/amazon.aws/pull/946).
- waf_info - Move to jittered backoff (https://github.com/ansible-collections/amazon.aws/pull/946).
- waf_rule - Move to jittered backoff (https://github.com/ansible-collections/amazon.aws/pull/946).
- waf_web_acl - Move to jittered backoff (https://github.com/ansible-collections/amazon.aws/pull/946).
- wafv2_ip_set - Added support for ``purge_tags`` parameter (https://github.com/ansible-collections/community.aws/pull/1205).
- wafv2_ip_set - Added support for returning tags (https://github.com/ansible-collections/community.aws/pull/1205).
- wafv2_ip_set - Added support for updating tags (https://github.com/ansible-collections/community.aws/pull/1205).
- wafv2_ip_set_info - Added support for returning tags (https://github.com/ansible-collections/community.aws/pull/1205).
- wafv2_rule_group - Added support for ``purge_tags`` parameter (https://github.com/ansible-collections/community.aws/pull/1210).
- wafv2_rule_group - Added support for returning tags (https://github.com/ansible-collections/community.aws/pull/1210).
- wafv2_rule_group - Added support for updating tags (https://github.com/ansible-collections/community.aws/pull/1210).
- wafv2_rule_group_info - Added support for returning tags (https://github.com/ansible-collections/community.aws/pull/1210).
- wafv2_web_acl - Added support for ``purge_tags`` (https://github.com/ansible-collections/community.aws/pull/1218).
- wafv2_web_acl - Added support for updating tags (https://github.com/ansible-collections/community.aws/pull/1218).
- wafv2_web_acl - ``resource_tags`` has been added as an alias for the ``tags`` parameter (https://github.com/ansible-collections/community.aws/pull/1218).
- wafv2_web_acl - added support for returning tags (https://github.com/ansible-collections/community.aws/pull/1218).
- wafv2_web_acl - relax botocore requirement to bare minimum required (https://github.com/ansible-collections/community.aws/pull/1216).
- wafv2_web_acl_info - added support for returning tags (https://github.com/ansible-collections/community.aws/pull/1218).

community.crypto
~~~~~~~~~~~~~~~~

- All software licenses are now in the ``LICENSES/`` directory of the collection root. Moreover, ``SPDX-License-Identifier:`` is used to declare the applicable license for every file that is not automatically generated (https://github.com/ansible-collections/community.crypto/pull/491).
- acme* modules - also support the HTTP 503 Service Unavailable and 408 Request Timeout response status for automatic retries (https://github.com/ansible-collections/community.crypto/pull/513).
- acme* modules - support the HTTP 429 Too Many Requests response status (https://github.com/ansible-collections/community.crypto/pull/508).
- acme_* modules - handle more gracefully if CA's new nonce call does not return a nonce (https://github.com/ansible-collections/community.crypto/pull/525).
- acme_* modules - include symbolic HTTP status codes in error and log messages when available (https://github.com/ansible-collections/community.crypto/pull/524).
- openssh_keypair - added ``pkcs1``, ``pkcs8``, and ``ssh`` to the available choices for the ``private_key_format`` option (https://github.com/ansible-collections/community.crypto/pull/511).
- openssl_pkcs12 - add option ``encryption_level`` which allows to chose ``compatibility2022`` when cryptography >= 38.0.0 is used to enable a more backwards compatible encryption algorithm. If cryptography uses OpenSSL 3.0.0 or newer, the default algorithm is not compatible with older software (https://github.com/ansible-collections/community.crypto/pull/523).

community.digitalocean
~~~~~~~~~~~~~~~~~~~~~~

- collection - added an action group C(community.digitalocean.all) for use with module defaults (https://docs.ansible.com/ansible/latest/user_guide/playbooks_module_defaults.html) (https://github.com/ansible-collections/community.digitalocean/issues/281).
- digital_ocean - add sanity test ignores for Ansible 2.12 and 2.13 (https://github.com/ansible-collections/community.digitalocean/issues/247).
- digital_ocean_cdn_endpoints - update Spaces endpoint and add a few delays to the integration test (https://github.com/ansible-collections/community.digitalocean/issues/267).
- digital_ocean_load_balancer - Allow creating a load balancer and associating droplets by tag as an alternative to ``droplet_ids``.
- digital_ocean_vpc - add C(vpc) key to returned VPC data on create (https://github.com/ansible-collections/community.digitalocean/issues/276).
- integration tests - perform integration testing on all modules for changes in C(plugins/module_utils) or by changed module in C(plugins/modules) (https://github.com/ansible-collections/community.digitalocean/issues/286).
- integration tests - split the integration tests by module and run them serially (https://github.com/ansible-collections/community.digitalocean/issues/280).

community.dns
~~~~~~~~~~~~~

- Added a ``community.dns.hetzner`` module defaults group / action group. Use with ``group/community.dns.hetzner`` to provide options for all Hetzner DNS modules (https://github.com/ansible-collections/community.dns/pull/119).
- Added a ``community.dns.hosttech`` module defaults group / action group. Use with ``group/community.dns.hosttech`` to provide options for all Hosttech DNS modules (https://github.com/ansible-collections/community.dns/pull/119).
- All software licenses are now in the ``LICENSES/`` directory of the collection root. Moreover, ``SPDX-License-Identifier:`` is used to declare the applicable license for every file that is not automatically generated (https://github.com/ansible-collections/community.dns/pull/109).
- The collection repository conforms to the `REUSE specification <https://reuse.software/spec/>`__ except for the changelog fragments (https://github.com/ansible-collections/community.dns/pull/112).
- hetzner_dns_records and hosttech_dns_records inventory plugins - allow to template provider-specific credentials and the ``zone_name``, ``zone_id`` options (https://github.com/ansible-collections/community.dns/pull/106).
- wait_for_txt - improve error messages so that in case of SERVFAILs or other DNS errors it is clear which record was queried from which DNS server (https://github.com/ansible-collections/community.dns/pull/105).
- wait_for_txt - the module now supports check mode. The only practical change in behavior is that in check mode, the module is now executed instead of skipped. Since the module does not change anything, it should have been marked as supporting check mode since it was originally added (https://github.com/ansible-collections/community.dns/pull/119).

community.docker
~~~~~~~~~~~~~~~~

- All software licenses are now in the ``LICENSES/`` directory of the collection root. Moreover, ``SPDX-License-Identifier:`` is used to declare the applicable license for every file that is not automatically generated (https://github.com/ansible-collections/community.docker/pull/430).
- Move common utility functions from the ``common`` module_util to a new module_util called ``util``. This should not have any user-visible effect (https://github.com/ansible-collections/community.docker/pull/390).
- Remove vendored copy of ``distutils.version`` in favor of vendored copy included with ansible-core 2.12+. For ansible-core 2.11, uses ``distutils.version`` for Python < 3.12. There is no support for ansible-core 2.11 with Python 3.12+ (https://github.com/ansible-collections/community.docker/pull/271).
- The collection repository conforms to the `REUSE specification <https://reuse.software/spec/>`__ except for the changelog fragments (https://github.com/ansible-collections/community.docker/pull/462).
- docker_container - add a new parameter ``image_comparison`` to control the behavior for which image will be used for idempotency checks (https://github.com/ansible-collections/community.docker/issues/421, https://github.com/ansible-collections/community.docker/pull/428).
- docker_container - add support for ``cgroupns_mode`` (https://github.com/ansible-collections/community.docker/issues/338, https://github.com/ansible-collections/community.docker/pull/427).
- docker_container - added ``image_name_mismatch`` option which allows to control the behavior if the container uses the image specified, but the container's configuration uses a different name for the image than the one provided to the module (https://github.com/ansible-collections/community.docker/issues/485, https://github.com/ansible-collections/community.docker/pull/488).
- docker_container - allow to specify ``platform`` (https://github.com/ansible-collections/community.docker/issues/123, https://github.com/ansible-collections/community.docker/pull/426).
- docker_swarm - allows usage of the ``data_path_port`` parameter when initializing a swarm (https://github.com/ansible-collections/community.docker/issues/296).
- modules and plugins communicating directly with the Docker daemon - improve default TLS version selection for Python 3.6 and newer. This is only a change relative to older community.docker 3.0.0 pre-releases or with respect to Docker SDK for Python < 6.0.0. Docker SDK for Python 6.0.0 will also include this change (https://github.com/ansible-collections/community.docker/pull/434).
- modules and plugins communicating directly with the Docker daemon - simplify use of helper function that was removed in Docker SDK for Python to find executables (https://github.com/ansible-collections/community.docker/pull/438).
- socker_handler and socket_helper module utils - improve Python forward compatibilty, create helper functions for file blocking/unblocking (https://github.com/ansible-collections/community.docker/pull/415).

community.general
~~~~~~~~~~~~~~~~~

- Added MIT license as ``LICENSES/MIT.txt`` for tests/unit/plugins/modules/packaging/language/test_gem.py (https://github.com/ansible-collections/community.general/pull/5065).
- All software licenses are now in the ``LICENSES/`` directory of the collection root (https://github.com/ansible-collections/community.general/pull/5065, https://github.com/ansible-collections/community.general/pull/5079, https://github.com/ansible-collections/community.general/pull/5080, https://github.com/ansible-collections/community.general/pull/5083, https://github.com/ansible-collections/community.general/pull/5087, https://github.com/ansible-collections/community.general/pull/5095, https://github.com/ansible-collections/community.general/pull/5098, https://github.com/ansible-collections/community.general/pull/5106).
- ModuleHelper module utils - added property ``verbosity`` to base class (https://github.com/ansible-collections/community.general/pull/5035).
- ModuleHelper module utils - improved ``ModuleHelperException``, using ``to_native()`` for the exception message (https://github.com/ansible-collections/community.general/pull/4755).
- The collection repository conforms to the `REUSE specification <https://reuse.software/spec/>`__ except for the changelog fragments (https://github.com/ansible-collections/community.general/pull/5138).
- ali_instance - minor refactor when checking for installed dependency (https://github.com/ansible-collections/community.general/pull/5240).
- ali_instance_info - minor refactor when checking for installed dependency (https://github.com/ansible-collections/community.general/pull/5240).
- alternatives - add ``state=absent`` to be able to remove an alternative (https://github.com/ansible-collections/community.general/pull/4654).
- alternatives - add ``subcommands`` parameter (https://github.com/ansible-collections/community.general/pull/4654).
- ansible_galaxy_install - minor refactoring using latest ``ModuleHelper`` updates (https://github.com/ansible-collections/community.general/pull/4752).
- ansible_galaxy_install - refactored module to use ``CmdRunner`` to execute ``ansible-galaxy`` (https://github.com/ansible-collections/community.general/pull/5477).
- apk - add ``world`` parameter for supporting a custom world file (https://github.com/ansible-collections/community.general/pull/4976).
- bitwarden lookup plugin - add option ``search`` to search for other attributes than name (https://github.com/ansible-collections/community.general/pull/5297).
- cartesian lookup plugin - start using Ansible's configuration manager to parse options (https://github.com/ansible-collections/community.general/pull/5440).
- cmd_runner module util - added parameters ``check_mode_skip`` and ``check_mode_return`` to ``CmdRunner.context()``, so that the command is not executed when ``check_mode=True`` (https://github.com/ansible-collections/community.general/pull/4736).
- cmd_runner module utils - add ``__call__`` method to invoke context (https://github.com/ansible-collections/community.general/pull/4791).
- consul - adds ``ttl`` parameter for session  (https://github.com/ansible-collections/community.general/pull/4996).
- consul - minor refactoring (https://github.com/ansible-collections/community.general/pull/5367).
- consul_session - adds ``token`` parameter for session (https://github.com/ansible-collections/community.general/pull/5193).
- cpanm - refactored module to use ``CmdRunner`` to execute ``cpanm`` (https://github.com/ansible-collections/community.general/pull/5485).
- cpanm - using ``do_raise()`` to raise exceptions in ``ModuleHelper`` derived modules (https://github.com/ansible-collections/community.general/pull/4674).
- credstash lookup plugin - start using Ansible's configuration manager to parse options (https://github.com/ansible-collections/community.general/pull/5440).
- dependent lookup plugin - start using Ansible's configuration manager to parse options (https://github.com/ansible-collections/community.general/pull/5440).
- dig lookup plugin - add option ``fail_on_error`` to allow stopping execution on lookup failures (https://github.com/ansible-collections/community.general/pull/4973).
- dig lookup plugin - start using Ansible's configuration manager to parse options. All documented options can now also be passed as lookup parameters (https://github.com/ansible-collections/community.general/pull/5440).
- dnstxt lookup plugin - start using Ansible's configuration manager to parse options (https://github.com/ansible-collections/community.general/pull/5440).
- filetree lookup plugin - start using Ansible's configuration manager to parse options (https://github.com/ansible-collections/community.general/pull/5440).
- flattened lookup plugin - start using Ansible's configuration manager to parse options (https://github.com/ansible-collections/community.general/pull/5440).
- gitlab module util - minor refactor when checking for installed dependency (https://github.com/ansible-collections/community.general/pull/5259).
- gitlab_branch - minor refactor when checking for installed dependency (https://github.com/ansible-collections/community.general/pull/5259).
- gitlab_deploy_key - minor refactor when checking for installed dependency (https://github.com/ansible-collections/community.general/pull/5259).
- gitlab_group - minor refactor when checking for installed dependency (https://github.com/ansible-collections/community.general/pull/5259).
- gitlab_group_members - minor refactor when checking for installed dependency (https://github.com/ansible-collections/community.general/pull/5259).
- gitlab_group_variable - minor refactor when checking for installed dependency (https://github.com/ansible-collections/community.general/pull/5259).
- gitlab_hook - minor refactor when checking for installed dependency (https://github.com/ansible-collections/community.general/pull/5259).
- gitlab_hook - minor refactoring (https://github.com/ansible-collections/community.general/pull/5271).
- gitlab_project - minor refactor when checking for installed dependency (https://github.com/ansible-collections/community.general/pull/5259).
- gitlab_project_members - minor refactor when checking for installed dependency (https://github.com/ansible-collections/community.general/pull/5259).
- gitlab_project_variable - minor refactor when checking for installed dependency (https://github.com/ansible-collections/community.general/pull/5259).
- gitlab_protected_branch - minor refactor when checking for installed dependency (https://github.com/ansible-collections/community.general/pull/5259).
- gitlab_runner - minor refactor when checking for installed dependency (https://github.com/ansible-collections/community.general/pull/5259).
- gitlab_user - minor refactor when checking for installed dependency (https://github.com/ansible-collections/community.general/pull/5259).
- hiera lookup plugin - start using Ansible's configuration manager to parse options. The Hiera executable and config file can now also be passed as lookup parameters (https://github.com/ansible-collections/community.general/pull/5440).
- homebrew, homebrew_tap - added Homebrew on Linux path to defaults (https://github.com/ansible-collections/community.general/pull/5241).
- hponcfg - refactored module to use ``CmdRunner`` to execute ``hponcfg`` (https://github.com/ansible-collections/community.general/pull/5483).
- keycloak_* modules - add ``http_agent`` parameter with default value ``Ansible`` (https://github.com/ansible-collections/community.general/issues/5023).
- keyring lookup plugin - start using Ansible's configuration manager to parse options (https://github.com/ansible-collections/community.general/pull/5440).
- lastpass - use config manager for handling plugin options (https://github.com/ansible-collections/community.general/pull/5022).
- ldap_attrs - allow for DNs to have ``{x}`` prefix on first RDN (https://github.com/ansible-collections/community.general/issues/977, https://github.com/ansible-collections/community.general/pull/5450).
- linode inventory plugin - simplify option handling (https://github.com/ansible-collections/community.general/pull/5438).
- listen_ports_facts - add new ``include_non_listening`` option which adds ``-a`` option to ``netstat`` and ``ss``. This shows both listening and non-listening (for TCP this means established connections) sockets, and returns ``state`` and ``foreign_address`` (https://github.com/ansible-collections/community.general/issues/4762, https://github.com/ansible-collections/community.general/pull/4953).
- lmdb_kv lookup plugin - start using Ansible's configuration manager to parse options (https://github.com/ansible-collections/community.general/pull/5440).
- lxc_container - minor refactoring (https://github.com/ansible-collections/community.general/pull/5358).
- machinectl become plugin - can now be used with a password from another user than root, if a polkit rule is present (https://github.com/ansible-collections/community.general/pull/4849).
- machinectl become plugin - combine the success command when building the become command to be consistent with other become plugins (https://github.com/ansible-collections/community.general/pull/5287).
- manifold lookup plugin - start using Ansible's configuration manager to parse options (https://github.com/ansible-collections/community.general/pull/5440).
- maven_artifact - add a new ``unredirected_headers`` option that can be used with ansible-core 2.12 and above. The default value is to not use ``Authorization`` and ``Cookie`` headers on redirects for security reasons. With ansible-core 2.11, all headers are still passed on for redirects (https://github.com/ansible-collections/community.general/pull/4812).
- mksysb - refactored module to use ``CmdRunner`` to execute ``mksysb`` (https://github.com/ansible-collections/community.general/pull/5484).
- mksysb - using ``do_raise()`` to raise exceptions in ``ModuleHelper`` derived modules (https://github.com/ansible-collections/community.general/pull/4674).
- nagios - minor refactoring on parameter validation for different actions (https://github.com/ansible-collections/community.general/pull/5239).
- netcup_dnsapi - add ``timeout`` parameter (https://github.com/ansible-collections/community.general/pull/5301).
- nmcli - add ``transport_mode`` configuration for Infiniband devices (https://github.com/ansible-collections/community.general/pull/5361).
- nmcli - add bond option ``xmit_hash_policy`` to bond options (https://github.com/ansible-collections/community.general/issues/5148).
- nmcli - adds ``vpn`` type and parameter for supporting VPN with service type L2TP and PPTP (https://github.com/ansible-collections/community.general/pull/4746).
- nmcli - honor IP options for VPNs (https://github.com/ansible-collections/community.general/pull/5228).
- onepassword - support version 2 of the OnePassword CLI (https://github.com/ansible-collections/community.general/pull/4728)
- opentelemetry callback plugin - allow configuring opentelementry callback via config file (https://github.com/ansible-collections/community.general/pull/4916).
- opentelemetry callback plugin - send logs. This can be disabled by setting ``disable_logs=false`` (https://github.com/ansible-collections/community.general/pull/4175).
- pacman - added parameters ``reason`` and ``reason_for`` to set/change the install reason of packages (https://github.com/ansible-collections/community.general/pull/4956).
- passwordstore lookup plugin - allow options to be passed lookup options instead of being part of the term strings (https://github.com/ansible-collections/community.general/pull/5444).
- passwordstore lookup plugin - allow using alternative password managers by detecting wrapper scripts, allow explicit configuration of pass and gopass backends (https://github.com/ansible-collections/community.general/issues/4766).
- passwordstore lookup plugin - improve error messages to include stderr (https://github.com/ansible-collections/community.general/pull/5436)
- pipx - added state ``latest`` to the module (https://github.com/ansible-collections/community.general/pull/5105).
- pipx - changed implementation to use ``cmd_runner`` (https://github.com/ansible-collections/community.general/pull/5085).
- pipx - module fails faster when ``name`` is missing for states ``upgrade`` and ``reinstall`` (https://github.com/ansible-collections/community.general/pull/5100).
- pipx - using ``do_raise()`` to raise exceptions in ``ModuleHelper`` derived modules (https://github.com/ansible-collections/community.general/pull/4674).
- pipx module utils - created new module util ``pipx`` providing a ``cmd_runner`` specific for the ``pipx`` module (https://github.com/ansible-collections/community.general/pull/5085).
- portage - add knobs for Portage's ``--backtrack`` and ``--with-bdeps`` options (https://github.com/ansible-collections/community.general/pull/5349).
- portage - use Portage's python module instead of calling gentoolkit-provided program in shell (https://github.com/ansible-collections/community.general/pull/5349).
- proxmox inventory plugin - added new flag ``qemu_extended_statuses`` and new groups ``<group_prefix>prelaunch``, ``<group_prefix>paused``. They will be populated only when ``want_facts=true``, ``qemu_extended_statuses=true`` and only for ``QEMU`` machines (https://github.com/ansible-collections/community.general/pull/4723).
- proxmox inventory plugin - simplify option handling code (https://github.com/ansible-collections/community.general/pull/5437).
- proxmox module utils, the proxmox* modules - add ``api_task_ok`` helper to standardize API task status checks across all proxmox modules (https://github.com/ansible-collections/community.general/pull/5274).
- proxmox_kvm - allow ``agent`` argument to be a string (https://github.com/ansible-collections/community.general/pull/5107).
- proxmox_snap - add ``unbind`` param to support snapshotting containers with configured mountpoints (https://github.com/ansible-collections/community.general/pull/5274).
- puppet - adds ``confdir`` parameter to configure a custom confir location (https://github.com/ansible-collections/community.general/pull/4740).
- redfish - added new command GetVirtualMedia, VirtualMediaInsert and VirtualMediaEject to Systems category due to Redfish spec changes the virtualMedia resource location from Manager to System (https://github.com/ansible-collections/community.general/pull/5124).
- redfish_config - add ``SetSessionService`` to set default session timeout policy (https://github.com/ansible-collections/community.general/issues/5008).
- redfish_info - add ``GetManagerInventory`` to report list of Manager inventory information (https://github.com/ansible-collections/community.general/issues/4899).
- seport - added new argument ``local`` (https://github.com/ansible-collections/community.general/pull/5203)
- snap - using ``do_raise()`` to raise exceptions in ``ModuleHelper`` derived modules (https://github.com/ansible-collections/community.general/pull/4674).
- sudoers - will attempt to validate the proposed sudoers rule using visudo if available, optionally skipped, or required (https://github.com/ansible-collections/community.general/pull/4794, https://github.com/ansible-collections/community.general/issues/4745).
- terraform - adds capability to handle complex variable structures for ``variables`` parameter in the module. This must be enabled with the new ``complex_vars`` parameter (https://github.com/ansible-collections/community.general/pull/4797).
- terraform - run ``terraform init`` with ``-no-color`` not to mess up the stdout of the task (https://github.com/ansible-collections/community.general/pull/5147).
- wdc_redfish_command - add ``IndicatorLedOn`` and ``IndicatorLedOff`` commands for ``Chassis`` category (https://github.com/ansible-collections/community.general/pull/5059).
- wdc_redfish_command - add ``PowerModeLow`` and ``PowerModeNormal`` commands for ``Chassis`` category (https://github.com/ansible-collections/community.general/pull/5145).
- xfconf - add ``stdout``, ``stderr`` and ``cmd`` to the module results (https://github.com/ansible-collections/community.general/pull/5037).
- xfconf - changed implementation to use ``cmd_runner`` (https://github.com/ansible-collections/community.general/pull/4776).
- xfconf - use ``do_raise()`` instead of defining custom exception class (https://github.com/ansible-collections/community.general/pull/4975).
- xfconf - using ``do_raise()`` to raise exceptions in ``ModuleHelper`` derived modules (https://github.com/ansible-collections/community.general/pull/4674).
- xfconf module utils - created new module util ``xfconf`` providing a ``cmd_runner`` specific for ``xfconf`` modules (https://github.com/ansible-collections/community.general/pull/4776).
- xfconf_info - changed implementation to use ``cmd_runner`` (https://github.com/ansible-collections/community.general/pull/4776).
- xfconf_info - use ``do_raise()`` instead of defining custom exception class (https://github.com/ansible-collections/community.general/pull/4975).
- znode - possibility to use ZooKeeper ACL authentication (https://github.com/ansible-collections/community.general/pull/5306).

community.grafana
~~~~~~~~~~~~~~~~~

- Export dashboard with pretty printed JSON so that it becomes easier to compare changes with the previous version (#257)
- community.grafana.grafana_datasource supports grafana-azure-monitor-datasource.

community.hashi_vault
~~~~~~~~~~~~~~~~~~~~~

- community.hashi_vault collection - add support for ``azure`` auth method, for Azure service principal, managed identity, or plain JWT access token (https://github.com/ansible-collections/community.hashi_vault/issues/293).
- community.hashi_vault retries - `HTTP status code 412 <https://www.vaultproject.io/api-docs#412>`__ has been added to the default list of codes to be retried, for the new `Server Side Consistent Token feature <https://www.vaultproject.io/docs/faq/ssct#q-is-there-anything-else-i-need-to-consider-to-achieve-consistency-besides-upgrading-to-vault-1-10>`__ in Vault Enterprise (https://github.com/ansible-collections/community.hashi_vault/issues/290).
- modules - all modules now document their action group and support for check mode in their attributes documentation (https://github.com/ansible-collections/community.hashi_vault/issues/197).
- vault_pki_generate_certificate - the documentation has been updated to match the argspec for the default values of options ``alt_names``, ``ip_sans``, ``other_sans``, and ``uri_sans`` (https://github.com/ansible-collections/community.hashi_vault/pull/318).
- vault_token_create - creation or orphan tokens uses ``hvac``'s new v1 method for creating orphans, or falls back to the v0 method if needed (https://github.com/ansible-collections/community.hashi_vault/issues/301).

community.hrobot
~~~~~~~~~~~~~~~~

- Added a ``community.hrobot.robot`` module defaults group / action group. Use with ``group/community.hrobot.robot`` to provide options for all Hetzner Robot modules (https://github.com/ansible-collections/community.hrobot/pull/65).
- All software licenses are now in the ``LICENSES/`` directory of the collection root. Moreover, ``SPDX-License-Identifier:`` is used to declare the applicable license for every file that is not automatically generated (https://github.com/ansible-collections/community.hrobot/pull/52).
- The collection repository conforms to the `REUSE specification <https://reuse.software/spec/>`__ except for the changelog fragments (https://github.com/ansible-collections/community.hrobot/pull/60).
- robot inventory plugin - allow to template ``hetzner_user`` and ``hetzner_password`` (https://github.com/ansible-collections/community.hrobot/pull/49).

community.libvirt
~~~~~~~~~~~~~~~~~

- libvirt - add extra guest information to inventory (https://github.com/ansible-collections/community.libvirt/pull/113).
- libvirt - replace the calls to listDomainsID() and listDefinedDomains() with listAllDomains() in find_vm() (https://github.com/ansible-collections/community.libvirt/pull/117)

community.mysql
~~~~~~~~~~~~~~~

- mysql_db - add the ``chdir`` argument to avoid failings when a dump file contains relative paths (https://github.com/ansible-collections/community.mysql/issues/395).
- mysql_db - add the ``pipefail`` argument to avoid broken dumps when ``state`` is ``dump`` and compression is used (https://github.com/ansible-collections/community.mysql/issues/256).
- mysql_replication - add a new option: ``primary_ssl_verify_server_cert`` (https://github.com//pull/435).
- mysql_role - add the argument ``members_must_exist`` (boolean, default true). The assertion that the users supplied in the ``members`` argument exist is only executed when the new argument ``members_must_exist`` is ``true``, to allow opt-out (https://github.com/ansible-collections/community.mysql/pull/369).
- mysql_user - Add the option ``on_new_username`` to argument ``update_password`` to reuse the password (plugin and authentication_string) when creating a new user if some user with the same name already exists. If the existing user with the same name have varying passwords, the password from the arguments is used like with ``update_password: always`` (https://github.com/ansible-collections/community.mysql/pull/365).
- mysql_user - Add the result field ``password_changed`` (boolean). It is true, when the user got a new password. When the user was created with ``update_password: on_new_username`` and an existing password was reused, ``password_changed`` is false (https://github.com/ansible-collections/community.mysql/pull/365).

community.network
~~~~~~~~~~~~~~~~~

- community.network.ce_switchport - add support of decode a few stdout values from bitmap to human readable format(https://github.com/ansible-collections/community.network/issues/315)
- community.network.edgeos_config - append save command into result (https://github.com/ansible-collections/community.network/pull/189)

community.postgresql
~~~~~~~~~~~~~~~~~~~~

- postgresql_* - add the ``connect_params`` parameter dict to allow any additional ``libpg`` connection parameters (https://github.com/ansible-collections/community.postgresql/pull/329).
- postgresql_membership - add the ``exact`` state value to be able to specify a list of only groups a user must be a member of (https://github.com/ansible-collections/community.postgresql/issues/277).
- postgresql_pg_hba - add argument ``overwrite`` (bool, default: false) to remove unmanaged rules (https://github.com/ansible-collections/community.postgresql/issues/297).
- postgresql_pg_hba - add argument ``rules_behavior`` (choices: conflict (default), combine) to fail when ``rules`` and normal rule-specific arguments are given or, when ``combine``, use them as defaults for the ``rules`` items (https://github.com/ansible-collections/community.postgresql/issues/297).
- postgresql_pg_hba - add argument ``rules`` to specify a list of rules using the normal rule-specific argument in each item (https://github.com/ansible-collections/community.postgresql/issues/297).

community.rabbitmq
~~~~~~~~~~~~~~~~~~

- Various CI fixes (https://github.com/ansible-collections/community.rabbitmq/pull/139 & https://github.com/ansible-collections/community.rabbitmq/pull/141).
- rabbitmq_exchange - adding ability to specify exchange types that are enabled via plugins. I(x-random), I(x-consistent-hash) and I(x-recent-history) (https://github.com/ansible-collections/community.rabbitmq/pull/142).
- rabbitmq_publish - fixing issue with publishing to exchanges and adding exchange documentation examples. Publishing to an exchange or queue is now mutually exclusive  (https://github.com/ansible-collections/community.rabbitmq/pull/140).

community.routeros
~~~~~~~~~~~~~~~~~~

- All software licenses are now in the ``LICENSES/`` directory of the collection root. Moreover, ``SPDX-License-Identifier:`` is used to declare the applicable license for every file that is not automatically generated (https://github.com/ansible-collections/community.routeros/pull/101).
- The collection repository conforms to the `REUSE specification <https://reuse.software/spec/>`__ except for the changelog fragments (https://github.com/ansible-collections/community.routeros/pull/108).
- api* modules - added ``timeout`` parameter (https://github.com/ansible-collections/community.routeros/pull/109).
- api_modify, api_info - support API path ``ip firewall mangle`` (https://github.com/ansible-collections/community.routeros/pull/110).

community.sap_libs
~~~~~~~~~~~~~~~~~~

- License requirements are updated.
- The modules purposes are described clearer.
- The namespaces of the modules are removed to provide a flatter design.
- hana_query - module is moved to sap_hdbsql.
- sapcontrol - module is moved to sap_control_exec to have a clearer separation to other roles and references.

community.sops
~~~~~~~~~~~~~~

- All software licenses are now in the ``LICENSES/`` directory of the collection root, and the collection repository conforms to the `REUSE specification <https://reuse.software/spec/>`__ except for the changelog fragments (https://github.com/ansible-collections/community.crypto/sops/108, https://github.com/ansible-collections/community.sops/pull/113).
- Allow to specify age keys as ``age_key``, or age keyfiles as ``age_keyfile`` (https://github.com/ansible-collections/community.sops/issues/116, https://github.com/ansible-collections/community.sops/pull/117).
- sops vars plugin - added a configuration option to temporarily disable the vars plugin (https://github.com/ansible-collections/community.sops/pull/114).
- sops_encrypt - allow to specify age recipients (https://github.com/ansible-collections/community.sops/issues/116, https://github.com/ansible-collections/community.sops/pull/117).

community.vmware
~~~~~~~~~~~~~~~~

- vmware_cfg_backup - Improve error message (https://github.com/ansible-collections/community.vmware/pull/1388).
- vmware_cluster_ha - Add APD settings (https://github.com/ansible-collections/community.vmware/pull/1420).
- vmware_content_library_info - Add Subscribed Libraries (https://github.com/ansible-collections/community.vmware/issues/1430).
- vmware_drs_group_manager - Improve error handling (https://github.com/ansible-collections/community.vmware/pull/1448).
- vmware_dvs_portgroup - Add deprecaded securityPolicyOverrideAllowed because without it make problems if securityPolicyOverrideAllowed and macManagementOverrideAllowed has not the same value (https://github.com/ansible-collections/community.vmware/pull/1508)
- vmware_dvs_portgroup - Fix a `spec.numPorts is None` issue when the `num_ports` parameter isn't set (https://github.com/ansible-collections/community.vmware/pull/1419).
- vmware_dvswitch.py - Add Netflow Settings. (https://github.com/ansible-collections/community.vmware/pull/1352)
- vmware_dvswitch_nioc.py - Add backupNfc and nvmetcp to the resources. (https://github.com/ansible-collections/community.vmware/pull/1351)
- vmware_guest - Adding `script_text` parameter to execute scripts in Linux guests (https://github.com/ansible-collections/community.vmware/pull/1485).
- vmware_guest_disk - Add a new disk type to support add/reconfigure/remove vPMem disk (https://github.com/ansible-collections/community.vmware/pull/1382).
- vmware_guest_disk - Adding `iolimit` modifications of an existing disk without changing size (https://github.com/ansible-collections/community.vmware/pull/1466).
- vmware_guest_sendkey - Add CTRL_X binding support (https://github.com/ansible-collections/community.vmware/pull/1376).
- vmware_host_lockdown - Add the ability to enable ``strict`` lockdown mode (https://github.com/ansible-collections/community.vmware/pull/1514).
- vmware_host_lockdown - Add two new choices for ``state``, ``disabled`` and ``normal``, to replace ``absent`` and ``present``. Please note that ``absent`` and ``present`` will be removed in the next major release (https://github.com/ansible-collections/community.vmware/pull/1514).
- vmware_host_lockdown - Replace deprecated vSphere API calls (https://github.com/ansible-collections/community.vmware/pull/1514).
- vmware_host_passthrough - Support the PCI id in the devices parameter(https://github.com/ansible-collections/community.vmware/pull/1365).
- vmware_host_vmnic_info - add CDP information to output when applicable (https://github.com/ansible-collections/community.vmware/pull/1418).
- vmware_object_role_permission.py - Add StoragePod to the list of object_types. (https://github.com/ansible-collections/community.vmware/pull/1338)
- vmware_object_role_permission_info.py - Add StoragePod and DistributedVirtalPortgroup to the list of object_types. (https://github.com/ansible-collections/community.vmware/pull/1338)
- vmware_vmotion - Add the feature to use cluster and datastore cluster (storage pods) to define where the vmotion shold go. (https://github.com/ansible-collections/community.vmware/pull/1240)

community.windows
~~~~~~~~~~~~~~~~~

- Raise minimum Ansible version to ``2.11`` or newer
- win_psmodule module - add ``accept_license`` option to allow for installing modules that require license acceptance (https://github.com/ansible-collections/community.windows/issues/340).

community.zabbix
~~~~~~~~~~~~~~~~

- roles - Minimized the config templates for the zabbix_agent, zabbix_javagateway, zabbix_proxy, and zabbix_server roles to make them version independent.
- roles - Support for Zabbix 6.2 has been added
- roles - Updated the version defaults to select the latest version supported by an operating system.
- zabbix_action - added another condition operator naming options (contains, does not contain,...)
- zabbix_agent - Set a ansible_python_interpreter to localhost based on the env the playbook is executed from.
- zabbix_agent - add option to set host tags using ``zabbix_agent_tags``.
- zabbix_agent - add possiblity to set include file pattern using ``zabbix_agent(2)_include_pattern`` variable.
- zabbix_agent - is now able to manage directories and upload files for TLS PSK configuration used with Windows operating systems
- zabbix_agent - new options for Windows installations zabbix_win_install_dir_conf/bin
- zabbix_agent - when configuring firewalld, make sure the new rule is applied immediately
- zabbix_authentication - module updated to support Zabbix 6.2
- zabbix_host - using ``tls_psk_identity`` or ``tls_psk`` parameters with Zabbix >= 5.4 makes this module non-idempotent
- zabbix_host - will no longer wipe tls_connect en tls_accept settings when not specified on update
- zabbix_mediatype - added support for time units in ``attempt_interval`` parameter
- zabbix_template - added support for template groups (Zabbix >= 6.2)
- zabbix_template_info - add template_id return value
- zabbix_template_info - add yaml and none formats
- zabbix_user_directory - added new module to support multiple sources for LDAP authentication

containers.podman
~~~~~~~~~~~~~~~~~

- Remove distutils as deprecated
- Run CI on Ubuntu 22.04
- Use 2.13 Ansible version in CI jobs instead of 2.11

dellemc.enterprise_sonic
~~~~~~~~~~~~~~~~~~~~~~~~

- Added an execution-environment.yml file to the "meta" directory to enable use of Ansible execution environment infrastructure (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/88).
- bgp_af - Added support for BGP options to configure usage and advertisement of vxlan primary IP address related attributes (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/62).
- bgp_as_paths - updated module examples with 'permit' attribute (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/102)
- bgp_neighbors - Add BGP peer group support for multiple attributes. The added attributes correspond to the same set of attributes added for BGP neighbors with PR 72 (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/81).
- bgp_neighbors - Add support for multiple attributes (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/72).
- bgp_neighbors - add an auth_pwd dictionary and nbr_description attribute to the argspec (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/67).
- bgp_neighbors - added prefix-list related peer-group attributes (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/101).
- bgp_neighbors_af - added prefix-list related neighbor attributes (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/101).
- playbook - updated examples to reflect module changes (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/102)
- sonic_vxlans - Add configuration capability for the primary IP address of a vxlan vtep to facilitate vxlan path redundundancy (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/58).
- vlans - Added support for the vlan "description" attribute (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/98).
- workflow - Added stable-2.13 to the sanity test matrix (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/90).

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- idrac_redfish_storage_controller - This module is updated to use the Job Service URL instead of Task Service URL for job tracking.
- idrac_server_config_profile - This module is updated to use the Job Service URL instead of Task Service URL for job tracking.
- ome_configuration_compliance_info - The module is enhanced to report single device compliance information.
- redfish_firmware - This module is updated to use the Job Service URL instead of Task Service URL for job tracking.

f5networks.f5_modules
~~~~~~~~~~~~~~~~~~~~~

- bigip_pool - Added aliases for the parameters, monitor_type and quorum
- bigip_pool - add three new parameters named, min_up_members, min_up_members_action and min_up_members_checking
- bigip_qkview - added a new parameter, only_create_file
- module_utils/teem.py - add additional telemetry data fields with relevant tests

fortinet.fortimanager
~~~~~~~~~~~~~~~~~~~~~

- Best Practice Notes

hetzner.hcloud
~~~~~~~~~~~~~~

- inventory - allow filtering by server status
- inventory - support jinjia templating within `network`

ibm.qradar
~~~~~~~~~~

- Add Qradar Analytics rules resource module.
- Add Qradar Log Sources Management resource module.

inspur.sm
~~~~~~~~~

- Edit_dns adds new field to M6 model.
- Modify ansible-test to add asnible 2.13,2.14 version.
- Modify the authors and tags fields in Galaxy.yml.
- Modify the tags fields in Galaxy.yml.
- Update the document.
- edit_power_budget add 'domain' field.
- edit_snmp module add 'v1status','v2status','v3status','read_community','read_write_community' fields.
- edit_snmp_trap module modifies the version value.
- eidt_ad module add 'ssl_enalbe' field, modify the timeout field description.
- eidt_ldisk module add 'duration' field.
- eidt_pdisk module add 'duration' field.
- modify the edit_log_setting module description.
- modify the edit_ncsi module description and parameter values.
- user module add 'uid','access' fields.
- user_group module add 'general','power','media','kvm','security','debug','self' fields.

junipernetworks.junos
~~~~~~~~~~~~~~~~~~~~~

- Add mac-vrf instance type.

kubernetes.core
~~~~~~~~~~~~~~~

- helm_repository - mark `pass_credentials` as no_log=True to silence false warning (https://github.com/ansible-collections/kubernetes.core/issues/412).
- kubectl.py - replace distutils.spawn.find_executable with shutil.which in the kubectl connection plugin (https://github.com/ansible-collections/kubernetes.core/pull/456).

netapp.cloudmanager
~~~~~~~~~~~~~~~~~~~

- Add ``availability_zone`` option in CVO Azure on the location configuration.
- Add ``subnet_path`` option in CVO GCP.
- Support ``writing_speed_state`` modification on AWS, AZURE and GCP CVOs.
- na_cloudmanager_connector_azure - Support full ``subnet_id`` and ``vnet_id``.
- na_cloudmanager_connector_azure - expose connector managed system identity principal_id to perform role assignment
- na_cloudmanager_cvo_aws - Add new parameter ``cluster_key_pair_name`` to support SSH authentication method key pair.
- na_cloudmanager_cvo_azure - Add new ``storage_type`` value Premium_ZRS
- na_cloudmanager_cvo_azure - Add parameter ``availability_zone_node1`` and ``availability_zone_node2`` for CVO Azure HA location
- na_cloudmanager_volume - Support AWS FsxN working environment.

netapp.ontap
~~~~~~~~~~~~

- All REST GET's up to and including 9.11.1 that do not require a UUID/KEY to be past in are now supported
- all REST modules - new option ``force_ontap_version`` to bypass permission issues with custom vsadmin roles.
- all modules - do not fail on ZAPI EMS log when vserver does not exist.
- na_ontap_aggregate - updated ``disk_types`` in documentation.
- na_ontap_autosupport_invoke - warn when ``message`` alias is used as it will be removed - it conflicts with Ansible internal variable.
- na_ontap_cifs_local_user_set_password - Added REST support.
- na_ontap_cifs_server - Added ``security`` options in REST.
- na_ontap_cluster - ``timezone.name`` to modify cluster timezone. REST only.
- na_ontap_cluster_config role - support ``broadcast_domain`` and ``service_policy`` with REST.
- na_ontap_cluster_ha - added REST support.
- na_ontap_debug - report python executable version and path.
- na_ontap_ems_destination - improve error messages - augment UT coverage (thanks to bielawb).
- na_ontap_export_policy_rule - Add ``from_rule_index`` for both REST and ZAPI. Change ``rule_index`` to required.
- na_ontap_export_policy_rule - ``allow_device_creation`` and ``chown_mode`` is now supported in ZAPI.
- na_ontap_export_policy_rule - ``allow_suid``, ``allow_device_creation`` and ``chown_mode`` is now supported from ONTAP 9.9.1 or later in REST.
- na_ontap_export_policy_rule - ``rule_index`` is now optional for create and delete.
- na_ontap_export_policy_rule - new option ``force_delete_on_first_match`` to support duplicate entries on delete.
- na_ontap_info - add computed serial_hex and naa_id for lun_info.
- na_ontap_info - add quota-policy-info.
- na_ontap_interface - ``dns_domain_name`` is now supported from ONTAP 9.9 or later in REST.
- na_ontap_interface - ``is_dns_update_enabled`` is now supported from ONTAP 9.9.1 or later in REST.
- na_ontap_interface - allow setting ``netmask`` with netmask length in ZAPI.
- na_ontap_interface - attempt to set interface_type to ``ip`` when ``protocols`` is set to "none".
- na_ontap_interface - improved validations for unsupported options with FC interfaces.
- na_ontap_interface - support ``broadcast_domain`` with REST.
- na_ontap_job_schedule - new option ``cluster`` added.
- na_ontap_kerberos_realm - added REST support.
- na_ontap_kerberos_realm - change ``kdc_port`` option type to int.
- na_ontap_ldap - fall back to ZAPI when ``use_rest`` is set to ``auto`` or fail when REST is desired.
- na_ontap_ldap_client - Added REST support.
- na_ontap_ldap_client - Added ``ldaps_enabled`` option in ZAPI.
- na_ontap_ldap_client - new option ``skip_config_validation``.
- na_ontap_license - return list of updated package names.
- na_ontap_login_message - warn when ``message`` alias is used as it will be removed - it conflicts with Ansible internal variable.
- na_ontap_login_messages - support cluster scope when using REST.
- na_ontap_lun - support ``qos_adaptive_policy_group`` with REST.
- na_ontap_lun_copy - added REST support.
- na_ontap_lun_map_reporting_nodes - added REST support.
- na_ontap_motd - deprecated in favor of ``na_ontap_login_messages``.  Fail when use_rest is set to ``always`` as REST is not supported.
- na_ontap_motd - warn when ``message`` alias is used as it will be removed - it conflicts with Ansible internal variable.
- na_ontap_name_service_switch - added REST support.
- na_ontap_net_routes - ``metric`` option is supported from ONTAP 9.11.0 or later in REST.
- na_ontap_net_subnet - added REST support.
- na_ontap_nfs - warn when ``nfsv4.1`` alias is used as it will be removed - it does not match Ansible naming convention.
- na_ontap_ntp - for ONTAP version 9.6 or below fall back to ZAPI when ``use_rest`` is set to ``auto`` or fail when REST is desired.
- na_ontap_ntp - new option ``key_id`` added.
- na_ontap_ntp_key - fail for ONTAP version 9.6 or below when ``use_rest`` is set to ``auto`` or when REST is desired.
- na_ontap_nvme_namespace - Added REST support.
- na_ontap_nvme_subsystem - Added REST support.
- na_ontap_nvme_subsystem - report subsystem as absent if vserver cannot be found when attempting a delete.
- na_ontap_portset - Added REST support.
- na_ontap_qtree - Added ``unix_user`` and ``unix_group`` options in REST.
- na_ontap_quotas - Added REST support.
- na_ontap_rest_info - Allowed the support of multiple subsets and warn when using ``**`` in fields.
- na_ontap_rest_info - add computed serial_hex and naa_id for storage/luns when serial_number is present.
- na_ontap_rest_info - added support for ``network/ip/subnets``.
- na_ontap_rest_info - new option ``ignore_api_errors`` to report error in subset rather than breaking execution.
- na_ontap_rest_info - support added for cluster.
- na_ontap_rest_info - support added for cluster/counter/tables.
- na_ontap_rest_info - support added for cluster/licensing/capacity-pools.
- na_ontap_rest_info - support added for cluster/licensing/license-managers.
- na_ontap_rest_info - support added for cluster/metrocluster/svms.
- na_ontap_rest_info - support added for cluster/sensors.
- na_ontap_rest_info - support added for name-services/cache/group-membership/settings.
- na_ontap_rest_info - support added for name-services/cache/host/settings.
- na_ontap_rest_info - support added for name-services/cache/netgroup/settings.
- na_ontap_rest_info - support added for name-services/cache/setting.
- na_ontap_rest_info - support added for name-services/cache/unix-group/settings.
- na_ontap_rest_info - support added for name-services/ldap-schemas.
- na_ontap_rest_info - support added for network/fc/fabrics.
- na_ontap_rest_info - support added for network/fc/interfaces.
- na_ontap_rest_info - support added for network/ip/subnets.
- na_ontap_rest_info - support added for protocols/active-directory.
- na_ontap_rest_info - support added for protocols/cifs/connections.
- na_ontap_rest_info - support added for protocols/cifs/group-policies.
- na_ontap_rest_info - support added for protocols/cifs/netbios.
- na_ontap_rest_info - support added for protocols/cifs/session/files.
- na_ontap_rest_info - support added for protocols/cifs/shadow-copies.
- na_ontap_rest_info - support added for protocols/cifs/shadowcopy-sets.
- na_ontap_rest_info - support added for protocols/nfs/connected-client-maps.
- na_ontap_rest_info - support added for protocols/nfs/connected-client-settings.
- na_ontap_rest_info - support added for protocols/vscan/on-access-policies.
- na_ontap_rest_info - support added for protocols/vscan/on-demand-policies.
- na_ontap_rest_info - support added for protocols/vscan/scanner-pools.
- na_ontap_rest_info - support added for security.
- na_ontap_rest_info - support added for security/aws-kms.
- na_ontap_rest_info - support added for security/multi-admin-verify.
- na_ontap_rest_info - support added for security/multi-admin-verify/approval-groups.
- na_ontap_rest_info - support added for security/multi-admin-verify/requests.
- na_ontap_rest_info - support added for security/multi-admin-verify/rules.
- na_ontap_rest_info - support added for storage/file/moves.
- na_ontap_rest_info - support added for storage/pools.
- na_ontap_rest_info -- Will now include a message in return output about ``gather_subset`` not supported by your version of ONTAP.
- na_ontap_rest_info -- Will now warn you if a ``gather_subset`` is not supported by your version of ONTAP.
- na_ontap_restit - support multipart/form-data for read and write.
- na_ontap_s3_users - ``secret_key`` and ``access_token`` are now returned when creating a user.
- na_ontap_security_key_manager - added REST support.
- na_ontap_security_key_manager - indicate that ``node`` is not used and is deprecated.
- na_ontap_security_key_manager - new REST option ``onboard`` for onboard key manager.
- na_ontap_security_key_manager - new REST options ``external`` and ``vserver`` for external key manager.
- na_ontap_security_ssh - Updates the SSH server configuration for the specified SVM - REST only.
- na_ontap_service_policy - new options ``known_services`` and ``additional_services``.
- na_ontap_service_policy - update services for 9.11.1 - make it easier to add new services.
- na_ontap_service_processor_network - Added REST support.
- na_ontap_snapmirror - ``schedule`` is handled through ``policy`` for REST.
- na_ontap_snapmirror - improve errror messages to be more specific and consistent.
- na_ontap_snapmirror - new option ``peer_options`` to define source connection parameters.
- na_ontap_snapmirror - new option ``transferring_time_out`` to define how long to wait for transfer to complete on create or initialize.
- na_ontap_snapmirror - new option ``validate_source_path`` to disable this validation.
- na_ontap_snapmirror - rewrite update for REST using POST to initiate transfer.
- na_ontap_snapmirror - validate source endpoint for ZAPI and REST, accounting for vserver local name.
- na_ontap_snapmirror - wait for the relationship to come back to idle after a resync.
- na_ontap_snapmirror - when deleting, attempt to delete even when the relationship cannot be broken.
- na_ontap_snapmirror_policy - ``name`` added as an alias for ``policy_name``.
- na_ontap_snapmirror_policy - improve error reporting and report errors in check_mode.
- na_ontap_snapmirror_policy - new option ``identity_preservation`` added.
- na_ontap_snmp_traphosts - Added ``host`` option in REST.
- na_ontap_software_update - added REST support.
- na_ontap_software_update - deleting a software package is now supported with ZAPI and REST.
- na_ontap_svm - Added ``ndmp`` option to services in REST.
- na_ontap_svm - Added documentation for ``allowed_protocol``, ndmp is default in REST.
- na_ontap_svm - added vserver as a convenient alias for name when using module_defaults.
- na_ontap_ucadapter - added REST support.
- na_ontap_unix_group - added REST support.
- na_ontap_unix_user - Added REST support.
- na_ontap_unix_user - Added new option ``primary_gid`` aliased to ``group_id``.
- na_ontap_user - accept ``service_processor`` as an alias for ``service-processor`` with ZAPI, to be consistent with REST.
- na_ontap_user - add support for SAML authentication_method.
- na_ontap_user_role -- added REST support.
- na_ontap_volume - ``wait_for_completion`` and ``check_interval`` is now supported for volume move and encryption in REST.
- na_ontap_volume - attempt to delete volume even when unmounting or offlining failed.
- na_ontap_volume - new REST option ``analytics`` added.
- na_ontap_volume - new option ``max_wait_time`` added.
- na_ontap_volume - now defaults to REST with ``use_rest`` set to ``auto``, like every other module.  ZAPI can be forced with ``use_rest`` set to ``never``.
- na_ontap_vscan_on_access_policy - Added REST support.
- na_ontap_vscan_on_access_policy - new REST options ``scan_readonly_volumes`` and ``only_execute_access`` added.
- na_ontap_vscan_on_demand_task - Added REST support.
- na_ontap_vserver_cifs_security - Added ``use_ldaps_for_ad_ldap`` and ``use_start_tls_for_ad_ldap`` as mutually exclusive in ZAPI.
- na_ontap_vserver_cifs_security - Added option ``encryption_required_for_dc_connections`` and ``use_ldaps_for_ad_ldap`` in ZAPI.
- na_ontap_vserver_cifs_security - fall back to ZAPI when ``use_rest`` is set to ``auto`` or fail when REST is desired.
- na_ontap_vserver_create - ``firewall_policy`` is not set when ``service_policy`` is present, as ``service_policy`` is preferred.
- na_ontap_vserver_create - ``protocol`` is now optional.  ``role`` is not set when protocol is absent.
- na_ontap_vserver_create - added ``interface_type``.  Only a value of ``ip`` is currently supported.
- na_ontap_vserver_create - added support for vserver management interface when using REST.
- na_ontap_vserver_create role - support ``broadcast_domain``, ``ipspace``, and ``service_policy`` with REST.
- na_ontap_wait_for_condition - added REST support.
- na_ontap_wait_for_condition - added ``snapmirror_relationship`` to wait on ``state`` or ``transfer_state`` (REST only).
- tracing - allow to selectively trace headers and authentication.

netapp.storagegrid
~~~~~~~~~~~~~~~~~~

- na_sg_org_container - supports versioning configuration for S3 buckets available in StorageGRID 11.6+.

netapp_eseries.santricity
~~~~~~~~~~~~~~~~~~~~~~~~~

- Require Ansible 2.10 or later.
- na_santricity_volume - Add size_tolerance option to handle the difference in volume size with SANtricity System Manager.
- nar_santricity_common - utilize provided eseries management information to determine network to search.

netbox.netbox
~~~~~~~~~~~~~

- Add action_group to enable module defaults groups [#800](https://github.com/netbox-community/ansible_modules/pull/800)
- Expand on query_filter for site [#824](https://github.com/netbox-community/ansible_modules/pull/824)
- nb_inventory - Allow API token to be templated [#806](https://github.com/netbox-community/ansible_modules/pull/806)
- nb_inventory - Allow for jinja templating [#834](https://github.com/netbox-community/ansible_modules/pull/834)
- netbox_cable - Change length to float from int [#828](https://github.com/netbox-community/ansible_modules/pull/828)
- netbox_device_interface - Add PoE attribute [#820](https://github.com/netbox-community/ansible_modules/pull/820)
- netbox_location - Add tenant to module [#829](https://github.com/netbox-community/ansible_modules/pull/829)
- netbox_prefix - Add mark_utilized to module [#827](https://github.com/netbox-community/ansible_modules/pull/827)

ngine_io.vultr
~~~~~~~~~~~~~~

- Documentation fixes.

ovirt.ovirt
~~~~~~~~~~~

- Add convert_to_bytes filter (https://github.com/oVirt/ovirt-ansible-collection/pull/515).
- During he_setup, configure ovn with he_host_address (https://github.com/oVirt/ovirt-ansible-collection/pull/568).
- During he_setup, configure ovn with he_host_name for correct operation of ovn (https://github.com/oVirt/ovirt-ansible-collection/pull/563).
- Fix "ansible-lint" version 6.0.0 "yaml" violations for "disaster_recovery" role (https://github.com/oVirt/ovirt-ansible-collection/pull/543).
- Fix "ansible-lint" version 6.0.0 violations for "disaster_recovery" & "remove_stale_lun" roles (https://github.com/oVirt/ovirt-ansible-collection/pull/554).
- Fix ansible-lint for basic roles (https://github.com/oVirt/ovirt-ansible-collection/pull/280).
- Updating the documentation - "vm_name" / "vm_id" and/or disk "id" parameter(s) are required when extending disk with non-unique name (https://github.com/oVirt/ovirt-ansible-collection/pull/559).
- automation - Use python38 on el8 with ansible-core 2.12 and python39 on el9 with ansible-core 2.13  (https://github.com/oVirt/ovirt-ansible-collection/pull/518).
- cloud.py - Sync with orgin (https://github.com/oVirt/ovirt-ansible-collection/pull/519).
- engine_setup - Allow to disable cert validation (https://github.com/oVirt/ovirt-ansible-collection/pull/517).
- filters - Add documentation to all filters (https://github.com/oVirt/ovirt-ansible-collection/pull/603).
- gluster_heal_info - Replacing gluster module to CLI to support RHV automation hub (https://github.com/oVirt/ovirt-ansible-collection/pull/340).
- hosted_engine_setup - fix ovirt-provider-ovn-driver broken link (https://github.com/oVirt/ovirt-ansible-collection/pull/581).
- hosted_engine_setup - make vdsm config cleanup optional (https://github.com/oVirt/ovirt-ansible-collection/pull/521).
- ovirt - Remove deprecated distutils (https://github.com/oVirt/ovirt-ansible-collection/pull/516).
- ovirt_disk - Add read_only param for disk attachments (https://github.com/oVirt/ovirt-ansible-collection/pull/597).
- ovirt_disk - Add warning for disk attachments (https://github.com/oVirt/ovirt-ansible-collection/pull/347).
- ovirt_disk - Fix disk attachment to VM (https://github.com/oVirt/ovirt-ansible-collection/pull/361).
- ovirt_qos, ovirt_disk_profile, ovirt_disk - Add modules to allow for creation and updating of disk_profiles (https://github.com/oVirt/ovirt-ansible-collection/pull/422).
- ovirt_snapshot - Add vm_id to select VM (https://github.com/oVirt/ovirt-ansible-collection/pull/550).
- ovirt_vm - Add reset of VM (https://github.com/oVirt/ovirt-ansible-collection/pull/538).
- ovirt_vm - Add virtio_scsi_enabled and multi_queues_enabled (https://github.com/oVirt/ovirt-ansible-collection/pull/348).
- ovirt_vm - add volatile (https://github.com/oVirt/ovirt-ansible-collection/pull/539).
- ovirt_vm - add wait_after_lease (https://github.com/oVirt/ovirt-ansible-collection/pull/524).
- repositories - Add ovirt_repositories_rhsm_environment and FIPS fix (https://github.com/oVirt/ovirt-ansible-collection/pull/483).
- repositories - Replace redhat_subscription and rhsm_repository with command (https://github.com/oVirt/ovirt-ansible-collection/pull/346).

purestorage.flasharray
~~~~~~~~~~~~~~~~~~~~~~

- purefa_ad - Add support for TLS and joining existing AD account
- purefa_dns - Support multiple DNS configurations from Puritry//FA 6.3.3
- purefa_info - Add NFS policy user mapping status
- purefa_info - Add support for Virtual Machines and Snapshots
- purefa_info - Ensure global admin lockout duration is measured in seconds
- purefa_info - Support multiple DNS configurations
- purefa_inventory - Add REST 2.x support and SFP details for Purity//FA 6.3.4 and higher
- purefa_inventory - Change response dict name to `purefa_inv` so doesn't clash with info module response dict
- purefa_inventory - add chassis information to inventory
- purefa_pg - Changed parameter `pgroup` to `name`. Allow `pgroup` as alias for backwards compatability.
- purefa_policy - Add ``all_squash``, ``anonuid`` and ``anongid`` to NFS client rules options
- purefa_policy - Add support for NFS policy user mapping
- purefa_volume - Default Protection Group support added for volume creation and copying from Purity//FA 6.3.4

purestorage.flashblade
~~~~~~~~~~~~~~~~~~~~~~

- All - Update documentation examples with FQCNs
- purefb_ad - Allow service to be a list
- purefb_bucket - Allow setting of bucket type to support VSO - requires Purity//FB 3.3.3 or higher
- purefb_certs - Fix several misspellings of certificate
- purefb_info - Added filesystem default, user and group quotas where available
- purefb_info - Expose object store bucket type from Purity//FB 3.3.3
- purefb_info - Show information for current timezone
- purefb_policy - Allow rename of NFS Export Policies from Purity//FB 3.3.3
- purefb_tz - Add support for FlashBlade timezone management

splunk.es
~~~~~~~~~

- Added adaptive_response_notable_events resource module
- Added correlation_searches resource module
- Added data_inputs_monitors resource module
- Added data_inputs_networks resource module

t_systems_mms.icinga_director
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Add action_group to enable module default groups (https://github.com/T-Systems-MMS/ansible-collection-icinga-director/pull/175)
- Add flapping support to service template module (https://github.com/T-Systems-MMS/ansible-collection-icinga-director/pull/180)
- Add icon support to service template (https://github.com/T-Systems-MMS/ansible-collection-icinga-director/pull/179)

theforeman.foreman
~~~~~~~~~~~~~~~~~~

- add execution environment metadata
- installation_medium, operatingsystem, partition_table - add ``Fcos``, ``Rhcos``, ``VRP`` OS families
- job_template - add ``hidden_value`` to ``template_inputs`` parameters
- job_template - allow ``value_type`` to be ``resource``
- operatingsystems role - make ``provisioning_template`` parameter optional
- repositories role - add ``ansible_collection_requirements``
- repositories role - add ``arch`` and ``os_versions`` parameters
- repositories role - support ``mirroring_policy``
- repository - add support for ``include_tags`` and ``exclude_tags`` parameters for Katello 4.4+
- repository, smart_proxy - document deprecation/removal status of ``download_policy=background``
- setting - the ``foreman_setting`` return entry is deprecated and kept for backwards compatibility, please use ``entity`` as with any other module
- smart_proxy - add ``inherit`` to possible values of ``download_policy`` (https://github.com/theforeman/foreman-ansible-modules/issues/1438)
- smart_proxy - add ``streamed`` download policy
- snapshot - add include_ram option when creating VMWare snapshot
- subscription_manifest - increase the import timeout to 10 minutes (https://github.com/theforeman/foreman-ansible-modules/issues/1474)
- sync_plans role - document the ``enabled`` parameter (https://github.com/theforeman/foreman-ansible-modules/issues/1477)
- sync_plans role - expose the ``state`` parameter of the underlying module, thus allowing to delete plans (https://github.com/theforeman/foreman-ansible-modules/issues/1477)

vmware.vmware_rest
~~~~~~~~~~~~~~~~~~

- Add news example for clone, instant clone and template on Content Library.
- documentation - clarify that the VMware vCenter API doesn't allow the cloning of template if there are not if Library.
- vcenter_vm - Add new examples (clone and instant clone).

vyos.vyos
~~~~~~~~~

- Update fact gathering to support v1.3 show version output

Breaking Changes / Porting Guide
--------------------------------

- Ansible 7 requires Python 3.9 on the controller, same as ansible-core 2.14.

Ansible-core
~~~~~~~~~~~~

- Allow for lazy evaluation of Jinja2 expressions (https://github.com/ansible/ansible/issues/56017)
- The default ansible-galaxy role skeletons no longer contain .travis.yml files. You can configure ansible-galaxy to use a custom role skeleton that contains a .travis.yml file to continue using Galaxy's integration with Travis CI.
- ansible - At startup the filesystem encoding and locale are checked to verify they are UTF-8. If not, the process exits with an error reporting the errant encoding.
- ansible - Increase minimum Python requirement to Python 3.9 for CLI utilities and controller code
- ansible-test - At startup the filesystem encoding is checked to verify it is UTF-8. If not, the process exits with an error reporting the errant encoding.
- ansible-test - At startup the locale is configured as ``en_US.UTF-8``, with a fallback to ``C.UTF-8``. If neither encoding is available the process exits with an error. If the fallback is used, a warning is displayed. In previous versions the ``en_US.UTF-8`` locale was always requested. However, no startup checking was performed to verify the locale was successfully configured.
- ansible-test validate-modules - Removed the ``missing-python-doc`` error code in validate modules, ``missing-documentation`` is used instead for missing PowerShell module documentation.
- strategy plugins - Make ``ignore_unreachable`` to increase ``ignored`` and ``ok`` and  counter, not ``skipped`` and ``unreachable``. (https://github.com/ansible/ansible/issues/77690)

amazon.aws
~~~~~~~~~~

- Tags beginning with ``aws:`` will not be removed when purging tags, these tags are reserved by Amazon and may not be updated or deleted (https://github.com/ansible-collections/amazon.aws/issues/817).
- amazon.aws collection - Support for ansible-core < 2.11 has been dropped (https://github.com/ansible-collections/amazon.aws/pull/1087).
- amazon.aws collection - The amazon.aws collection has dropped support for ``botocore<1.21.0`` and ``boto3<1.18.0``. Most modules will continue to work with older versions of the AWS SDK, however compatibility with older versions of the SDK is not guaranteed and will not be tested. When using older versions of the SDK a warning will be emitted by Ansible (https://github.com/ansible-collections/amazon.aws/pull/934).
- amazon.aws collection - the ``profile`` parameter is now mutually exclusive with the ``aws_access_key``, ``aws_secret_key`` and ``security_token`` parameters (https://github.com/ansible-collections/amazon.aws/pull/834).
- aws_az_info - the module alias ``aws_az_facts`` was deprecated in Ansible 2.9 and has now been removed (https://github.com/ansible-collections/amazon.aws/pull/832).
- aws_s3 - the default value for ``ensure overwrite`` has been changed to ``different`` instead of ``always`` so that the module is idempotent by default (https://github.com/ansible-collections/amazon.aws/issues/811).
- aws_ssm - on_denied and on_missing now both default to error, for consistency with both aws_secret and the base Lookup class (https://github.com/ansible-collections/amazon.aws/issues/617).
- doc_fragments - remove minimum collection requirements from doc_fragments/aws.py and allow pulling those from doc_fragments/aws_boto3.py instead (https://github.com/ansible-collections/amazon.aws/pull/985).
- ec2 - The ``ec2`` module has been removed in release 4.0.0 and replaced by the ``ec2_instance`` module (https://github.com/ansible-collections/amazon.aws/pull/630).
- ec2_ami - the default value for ``purge_tags`` has been changed from ``False`` to ``True`` (https://github.com/ansible-collections/amazon.aws/pull/916).
- ec2_ami - the parameter aliases ``DeviceName``, ``VirtualName`` and ``NoDevice`` were previously deprecated and have been removed, please use ``device_name``, ``virtual_name`` and ``no_device`` instead (https://github.com/ansible-collections/amazon.aws/pull/913).
- ec2_eni_info - the mutual exclusivity of the ``eni_id`` and ``filters`` parameters is now enforced, previously ``filters`` would be ignored if ``eni_id`` was set (https://github.com/ansible-collections/amazon.aws/pull/954).
- ec2_instance - the default value for ``purge_tags`` has been changed from ``False`` to ``True`` (https://github.com/ansible-collections/amazon.aws/pull/916).
- ec2_key - the default value for ``purge_tags`` has been changed from ``False`` to ``True`` (https://github.com/ansible-collections/amazon.aws/pull/916).
- ec2_vol - the default value for ``purge_tags`` has been changed from ``False`` to ``True`` (https://github.com/ansible-collections/amazon.aws/pull/916).
- ec2_vpc_dhcp_option_info - the parameter aliases ``DhcpOptionIds`` and ``DryRun`` were previously deprecated and have been removed, please use ``dhcp_options_ids`` and ``no_device`` instead (https://github.com/ansible-collections/amazon.aws/pull/913).
- ec2_vpc_endpoint - the default value for ``purge_tags`` has been changed from ``False`` to ``True`` (https://github.com/ansible-collections/amazon.aws/pull/916).
- ec2_vpc_igw_info - The default value for ``convert_tags`` has been changed to ``True`` (https://github.com/ansible-collections/amazon.aws/pull/835).
- ec2_vpc_net - the default value for ``purge_tags`` has been changed from ``False`` to ``True`` (https://github.com/ansible-collections/amazon.aws/pull/916).
- ec2_vpc_route_table - the default value for ``purge_tags`` has been changed from ``False`` to ``True`` (https://github.com/ansible-collections/amazon.aws/pull/916).
- elb_classic_lb - the ``ec2_elb`` fact has been removed (https://github.com/ansible-collections/amazon.aws/pull/827).
- module_utils - Support for the original AWS SDK aka ``boto`` has been removed, including all relevant helper functions. All modules should now use the ``boto3``/``botocore`` AWS SDK (https://github.com/ansible-collections/amazon.aws/pull/630)
- s3_bucket - the previously deprecated alias ``S3_URL`` for the ``s3_url`` parameter has been removed.  Playbooks shuold be updated to use ``s3_url`` (https://github.com/ansible-collections/amazon.aws/pull/908).
- s3_object - the previously deprecated alias ``S3_URL`` for the ``s3_url`` parameter has been removed.  Playbooks should be updated to use ``s3_url`` (https://github.com/ansible-collections/amazon.aws/pull/908).

check_point.mgmt
~~~~~~~~~~~~~~~~

- cp_mgmt_access_role - the 'machines' parameter now accepts a single str and a new parameter 'machines_list' of type dict has been added. the 'users' parameter now accepts a single str and a new parameter 'users_list' of type dict has been added.
- cp_mgmt_access_rule - the 'vpn' parameter now accepts a single str and a new parameter 'vpn_list' of type dict has been added. the 'position_by_rule' parameter has been changed to 'relative_position' with support of positioning above/below a section (and not just a rule). the 'relative_position' parameter has also 'top' and 'bottom' suboptions which allows positioning a rule at the top and bottom of a section respectively. a new parameter 'search_entire_rulebase' has been added to allow the relative positioning to be unlimited (was previously limited to 50 rules)
- cp_mgmt_administrator - the 'permissions_profile' parameter now accepts a single str and a new parameter 'permissions_profile_list' of type dict has been added.
- cp_mgmt_publish - the 'uid' parameter has been removed.

community.aws
~~~~~~~~~~~~~

- Tags beginning with ``aws:`` will not be removed when purging tags, these tags are reserved by Amazon and may not be updated or deleted (https://github.com/ansible-collections/amazon.aws/issues/817).
- acm_certificate - the previously deprecated default value of ``purge_tags=False`` has been updated to ``purge_tags=True`` (https://github.com/ansible-collections/community.aws/pull/1343).
- autoscaling_group - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.autoscaling_group``.
- autoscaling_group_info - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.autoscaling_group_info``.
- aws_secret - tags are no longer removed when the ``tags`` parameter is not set.  To remove all tags set ``tags={}`` (https://github.com/ansible-collections/community.aws/issues/1146).
- cloudfront_distribution - the previously deprecated default value of ``purge_tags=False`` has been updated to ``purge_tags=True`` (https://github.com/ansible-collections/community.aws/pull/1343).
- cloudtrail - The module has been migrated to the ``amazon.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.cloudtrail``.
- cloudwatch_metric_alarm - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.cloudwatch_metric_alarm``.
- cloudwatchevent_rule - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.cloudwatchevent_rule``.
- cloudwatchlogs_log_group - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.cloudwatchlogs_log_group``.
- cloudwatchlogs_log_group_info - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.cloudwatchlogs_log_group_info``.
- cloudwatchlogs_log_group_metric_filter - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.cloudwatchlogs_log_group_metric_filter``.
- community.aws collection - Support for ansible-core < 2.11 has been dropped (https://github.com/ansible-collections/community.aws/pull/1541).
- community.aws collection - The ``community.aws`` collection has now dropped support for and any requirements upon the original ``boto`` AWS SDK, and now uses the ``boto3``/``botocore`` AWS SDK (https://github.com/ansible-collections/community.aws/pull/898).
- community.aws collection - The community.aws collection has dropped support for ``botocore<1.21.0`` and ``boto3<1.18.0``. Most modules will continue to work with older versions of the AWS SDK, however compatibility with older versions of the SDK is not guaranteed and will not be tested. When using older versions of the SDK a warning will be emitted by Ansible (https://github.com/ansible-collections/community.aws/pull/1362).
- community.aws collection - the ``profile`` parameter is now mutually exclusive with the ``aws_access_key``, ``aws_secret_key`` and ``security_token`` parameters (https://github.com/ansible-collections/amazon.aws/pull/834).
- ec2_eip - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.ec2_eip``.
- ec2_eip_info - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.ec2_eip_info``.
- ec2_vpc_route_table - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.ec2_vpc_route_table``.
- ec2_vpc_route_table_info - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.ec2_vpc_route_table_info``.
- ec2_vpc_vpn - the previously deprecated default value of ``purge_tags=False`` has been updated to ``purge_tags=True`` (https://github.com/ansible-collections/community.aws/pull/1343).
- elb_application_lb - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.elb_application_lb``.
- elb_application_lb_info - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.elb_application_lb_info``.
- elb_instance - the ``ec2_elbs`` fact has been removed, ``updated_elbs`` has been added the return values and includes the same information (https://github.com/ansible-collections/community.aws/pull/1173).
- elb_network_lb - the default value of ``state`` has changed from ``absent`` to ``present`` (https://github.com/ansible-collections/community.aws/pull/1167).
- execute_lambda - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.execute_lambda``.
- iam_policy - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.iam_policy``.
- iam_policy_info - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.iam_policy_info``.
- iam_server_certificate - Passing file names to the ``cert``, ``chain_cert`` and ``key`` parameters has been removed. We recommend using a lookup plugin to read the files instead, see the documentation for an example (https://github.com/ansible-collections/community.aws/pull/1265).
- iam_server_certificate - the default value for the ``dup_ok`` parameter has been changed to ``true``. To preserve the original behaviour explicitly set the ``dup_ok`` parameter to ``false`` (https://github.com/ansible-collections/community.aws/pull/1265).
- iam_user - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.iam_user``.
- iam_user_info - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.iam_user_info``.
- kms_key - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.kms_key``.
- kms_key - managing the KMS IAM Policy via ``policy_mode`` and ``policy_grant_types`` was previously deprecated and has been removed in favor of the ``policy`` option (https://github.com/ansible-collections/community.aws/pull/1344).
- kms_key - the previously deprecated default value of ``purge_tags=False`` has been updated to ``purge_tags=True`` (https://github.com/ansible-collections/community.aws/pull/1343).
- kms_key_info - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.kms_key_info``.
- lambda - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.lambda``.
- lambda_alias - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.lambda_alias``.
- lambda_event - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.lambda_event``.
- lambda_execute - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.lambda_execute``.
- lambda_info - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.lambda_info``.
- lambda_policy - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.lambda_policy``.
- rds_cluster - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.rds_cluster``.
- rds_cluster_info - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.rds_cluster_info``.
- rds_cluster_snapshot - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.rds_cluster_snapshot``.
- rds_instance - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.rds_instance``.
- rds_instance_info - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.rds_instance_info``.
- rds_instance_snapshot - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.rds_instance_snapshot``.
- rds_option_group - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.rds_option_group``.
- rds_option_group_info - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.rds_option_group_info``.
- rds_param_group - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.rds_param_group``.
- rds_param_group - the previously deprecated default value of ``purge_tags=False`` has been updated to ``purge_tags=True`` (https://github.com/ansible-collections/community.aws/pull/1343).
- rds_snapshot_info - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.rds_snapshot_info``.
- rds_subnet_group - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.rds_subnet_group``.
- route53 - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.route53``.
- route53_health_check - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.route53_health_check``.
- route53_health_check - the previously deprecated default value of ``purge_tags=False`` has been updated to ``purge_tags=True`` (https://github.com/ansible-collections/community.aws/pull/1343).
- route53_info - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.route53_info``.
- route53_zone - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.route53_zone``.
- route53_zone - the previously deprecated default value of ``purge_tags=False`` has been updated to ``purge_tags=True`` (https://github.com/ansible-collections/community.aws/pull/1343).
- script_inventory_ec2 - The ec2.py inventory script has been moved to a new repository. The script can now be downloaded from https://github.com/ansible-community/contrib-scripts/blob/main/inventory/ec2.py and has been removed from this collection. We recommend migrating from the script to the amazon.aws.ec2 inventory plugin.  (https://github.com/ansible-collections/community.aws/pull/898)
- sqs_queue - the previously deprecated default value of ``purge_tags=False`` has been updated to ``purge_tags=True`` (https://github.com/ansible-collections/community.aws/pull/1343).

community.docker
~~~~~~~~~~~~~~~~

- This collection does not work with ansible-core 2.11 on Python 3.12+. Please either upgrade to ansible-core 2.12+, or use Python 3.11 or earlier (https://github.com/ansible-collections/community.docker/pull/271).
- docker_container - ``exposed_ports`` is no longer ignored in ``comparisons``. Before, its value was assumed to be identical with the value of ``published_ports`` (https://github.com/ansible-collections/community.docker/pull/422).
- docker_container - ``log_options`` can no longer be specified when ``log_driver`` is not specified (https://github.com/ansible-collections/community.docker/pull/422).
- docker_container - ``publish_all_ports`` is no longer ignored in ``comparisons`` (https://github.com/ansible-collections/community.docker/pull/422).
- docker_container - ``restart_retries`` can no longer be specified when ``restart_policy`` is not specified (https://github.com/ansible-collections/community.docker/pull/422).
- docker_container - ``stop_timeout`` is no longer ignored for idempotency if told to be not ignored in ``comparisons``. So far it defaulted to ``ignore`` there, and setting it to ``strict`` had no effect (https://github.com/ansible-collections/community.docker/pull/422).
- modules and plugins communicating directly with the Docker daemon - when connecting by SSH and not using ``use_ssh_client=true``, reject unknown host keys instead of accepting them. This is only a breaking change relative to older community.docker 3.0.0 pre-releases or with respect to Docker SDK for Python < 6.0.0. Docker SDK for Python 6.0.0 will also include this change (https://github.com/ansible-collections/community.docker/pull/434).

community.general
~~~~~~~~~~~~~~~~~

- newrelic_deployment - ``revision`` is required for v2 API (https://github.com/ansible-collections/community.general/pull/5341).
- scaleway_container_registry_info - no longer replace ``secret_environment_variables`` in the output by ``SENSITIVE_VALUE`` (https://github.com/ansible-collections/community.general/pull/5497).

community.hashi_vault
~~~~~~~~~~~~~~~~~~~~~

- auth - the default value for ``token_validate`` has changed from ``true`` to ``false``, as previously announced (https://github.com/ansible-collections/community.hashi_vault/issues/248).
- vault_kv2_get lookup - as previously announced, the default value for ``engine_mount_point`` in the ``vault_kv2_get`` lookup has changed from ``kv`` to ``secret`` (https://github.com/ansible-collections/community.hashi_vault/issues/279).

community.vmware
~~~~~~~~~~~~~~~~

- Removed support for ansible-core version < 2.13.0.
- vmware_dvs_portgroup - Add a new sub-option `inherited` to the `in_traffic_shaping` parameter. This means you can keep the setting as-is by not defining the parameter, but also that you have to define the setting as not `inherited` if you want to override it at the PG level (https://github.com/ansible-collections/community.vmware/pull/1483).
- vmware_dvs_portgroup - Add a new sub-option `inherited` to the `out_traffic_shaping` parameter. This means you can keep the setting as-is by not defining the parameter, but also that you have to define the setting as not `inherited` if you want to override it at the PG level (https://github.com/ansible-collections/community.vmware/pull/1483).
- vmware_dvs_portgroup - Change the type of `net_flow` to string to allow setting it implicitly to inherited or to keep the value as-is. This means you can keep the setting as-is by not defining the parameter, but also that while `true` or `no` still work, `True` or `Off` (uppercase) won't (https://github.com/ansible-collections/community.vmware/pull/1483).
- vmware_dvs_portgroup - Remove support for vSphere API less than 6.7.
- vmware_dvs_portgroup - Remove the default for `network_policy` and add a new sub-option `inherited`. This means you can keep the setting as-is by not defining the parameter, but also that you have to define the setting as not `inherited` if you want to override it at the PG level (https://github.com/ansible-collections/community.vmware/pull/1483).
- vmware_dvs_portgroup_info - Remove support for vSphere API less than 6.7.
- vmware_dvswitch - Remove support for vSphere API less than 6.7.
- vmware_dvswitch_uplink_pg - Remove support for vSphere API less than 6.7.
- vmware_guest_boot_manager - Remove default for ``secure_boot_enabled`` parameter (https://github.com/ansible-collections/community.vmware/issues/1461).
- vmware_vm_config_option - Dict item names in result are changed from strings joined with spaces to strings joined with underlines, e.g. `Guest fullname` is changed to `guest_fullname` (https://github.com/ansible-collections/community.vmware/issues/1268).
- vmware_vspan_session - Remove support for vSphere API less than 6.7.

dellemc.enterprise_sonic
~~~~~~~~~~~~~~~~~~~~~~~~

- bgp_af - Add the route_advertise_list dictionary to the argspec to replace the deleted, obsolete advertise_prefix attribute used for SONiC 3.x images on the 1.x branch of this collection. This change corresponds to a SONiC 4.0 OC YANG REST compliance change for the BGP AF REST API. It enables specification of a route map in conjunction with each route advertisement prefix (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/63).
- bgp_af - remove the obsolete 'advertise_prefix' attribute from argspec and config code. This and subsequent co-req replacement with the new route advertise list argument structure require corresponding changes in playbooks previoulsly used for configuring route advertise prefixes for SONiC 3.x images. (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/60)
- bgp_neighbors - Replace the previously defined standalone "bfd" attribute with a bfd dictionary containing multiple attributes. This change corresponds to the revised SONiC 4.x implementation of OC YANG compatible REST APIs. Playbooks previously using the bfd attributes for SONiC 3.x images must be modified for useon SONiC 4.0 images to use the new definition for the bfd attribute argspec structure (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/72).
- bgp_neighbors - Replace, for BGP peer groups, the previously defined standalone "bfd" attribute with a bfd dictionary containing multiple attributes. This change corresponds to the revised SONiC 4.x implementation of OC YANG compatible REST APIs. Playbooks previously using the bfd attributes for SONiC 3.x images must be modified for useon SONiC 4.0 images to use the new definition for the bfd attribute argspec structure (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/81).

Deprecated Features
-------------------

- The dellemc.os10 collection is considered unmaintained and will be removed from Ansible 8 if no one starts maintaining it again before Ansible 8. See `the removal process for details on how this works <https://github.com/ansible-collections/overview/blob/main/removal_from_ansible.rst#cancelling-removal-of-an-unmaintained-collection>`__ (https://github.com/ansible-community/community-topics/issues/134).
- The dellemc.os6 collection is considered unmaintained and will be removed from Ansible 8 if no one starts maintaining it again before Ansible 8. See `the removal process for details on how this works <https://github.com/ansible-collections/overview/blob/main/removal_from_ansible.rst#cancelling-removal-of-an-unmaintained-collection>`__ (https://github.com/ansible-community/community-topics/issues/132).
- The dellemc.os9 collection is considered unmaintained and will be removed from Ansible 8 if no one starts maintaining it again before Ansible 8. See `the removal process for details on how this works <https://github.com/ansible-collections/overview/blob/main/removal_from_ansible.rst#cancelling-removal-of-an-unmaintained-collection>`__ (https://github.com/ansible-community/community-topics/issues/133).
- The google.cloud collection is considered unmaintained and will be removed from Ansible 8 if no one starts maintaining it again before Ansible 8. See `the removal process for details on how this works <https://github.com/ansible-collections/overview/blob/main/removal_from_ansible.rst#cancelling-removal-of-an-unmaintained-collection>`__ (https://github.com/ansible-community/community-topics/issues/105).
- The mellanox.onyx collection is considered unmaintained and will be removed from Ansible 8 if no one starts maintaining it again before Ansible 8. See `the removal process for details on how this works <https://github.com/ansible-collections/overview/blob/main/removal_from_ansible.rst#cancelling-removal-of-an-unmaintained-collection>`__ (https://github.com/ansible-community/community-topics/issues/136).

Ansible-core
~~~~~~~~~~~~

- Deprecate ability of lookup plugins to return arbitrary data. Lookup plugins must return lists, failing to do so will be an error in 2.18. (https://github.com/ansible/ansible/issues/77788)
- Encryption - Deprecate use of the Python crypt module due to it's impending removal from Python 3.13
- PlayContext.verbosity is deprecated and will be removed in 2.18. Use ansible.utils.display.Display().verbosity as the single source of truth.
- ``DEFAULT_FACT_PATH``, ``DEFAULT_GATHER_SUBSET`` and ``DEFAULT_GATHER_TIMEOUT`` are deprecated and will be removed in 2.18. Use ``module_defaults`` keyword instead.
- ``PlayIterator`` - deprecate ``cache_block_tasks`` and ``get_original_task`` which are noop and unused.
- ``Templar`` - deprecate ``shared_loader_obj`` option which is unused. ``ansible.plugins.loader`` is used directly instead.
- listify_lookup_plugin_terms, deprecate 'loader/dataloader' parameter as it not used.
- vars plugins - determining whether or not to run ansible.legacy vars plugins with the class attribute REQUIRES_WHITELIST is deprecated, set REQUIRES_ENABLED instead.

amazon.aws
~~~~~~~~~~

- amazon.aws collection - Support for the ``EC2_ACCESS_KEY`` environment variable has been deprecated and will be removed in a release after 2024-12-01.  Please use the ``access_key`` parameter or ``AWS_ACCESS_KEY_ID`` environment variable instead (https://github.com/ansible-collections/amazon.aws/pull/1172).
- amazon.aws collection - Support for the ``EC2_REGION`` environment variable has been deprecated and will be removed in a release after 2024-12-01.  Please use the ``region`` parameter or ``AWS_REGION`` environment variable instead (https://github.com/ansible-collections/amazon.aws/pull/1172).
- amazon.aws collection - Support for the ``EC2_SECRET_KEY`` environment variable has been deprecated and will be removed in a release after 2024-12-01.  Please use the ``secret_key`` parameter or ``AWS_SECRET_ACCESS_KEY`` environment variable instead (https://github.com/ansible-collections/amazon.aws/pull/1172).
- amazon.aws collection - Support for the ``EC2_SECURITY_TOKEN`` environment variable has been deprecated and will be removed in a release after 2024-12-01.  Please use the ``session_token`` parameter or ``AWS_SESSION_TOKEN`` environment variable instead (https://github.com/ansible-collections/amazon.aws/pull/1172).
- amazon.aws collection - Support for the ``EC2_URL`` and ``S3_URL`` environment variables has been deprecated and will be removed in a release after 2024-12-01.  Please use the ``endpoint_url`` parameter or ``AWS_ENDPOINT_URL`` environment variable instead (https://github.com/ansible-collections/amazon.aws/pull/1172).
- amazon.aws collection - The ``access_token`` alias for the ``session_token`` parameter has been deprecated and will be removed in a release after 2024-12-01.  Please use the ``session_token`` name instead (https://github.com/ansible-collections/amazon.aws/pull/1172).
- amazon.aws collection - The ``aws_security_token`` alias for the ``session_token`` parameter has been deprecated and will be removed in a release after 2024-12-01.  Please use the ``session_token`` name instead (https://github.com/ansible-collections/amazon.aws/pull/1172).
- amazon.aws collection - The ``ec2_access_key`` alias for the ``access_key`` parameter has been deprecated and will be removed in a release after 2024-12-01.  Please use the ``access_key`` name instead (https://github.com/ansible-collections/amazon.aws/pull/1172).
- amazon.aws collection - The ``ec2_region`` alias for the ``region`` parameter has been deprecated and will be removed in a release after 2024-12-01.  Please use the ``region`` name instead (https://github.com/ansible-collections/amazon.aws/pull/1172).
- amazon.aws collection - The ``ec2_secret_key`` alias for the ``secret_key`` parameter has been deprecated and will be removed in a release after 2024-12-01.  Please use the ``secret_key`` name instead (https://github.com/ansible-collections/amazon.aws/pull/1172).
- amazon.aws collection - The ``security_token`` alias for the ``session_token`` parameter has been deprecated and will be removed in a release after 2024-12-01.  Please use the ``session_token`` name instead (https://github.com/ansible-collections/amazon.aws/pull/1172).
- amazon.aws collection - due to the AWS SDKs announcing the end of support for Python less than 3.7 (https://aws.amazon.com/blogs/developer/python-support-policy-updates-for-aws-sdks-and-tools/) support for Python less than 3.7 by this collection has been deprecated and will be removed in a release after 2023-05-31 (https://github.com/ansible-collections/amazon.aws/pull/935).
- aws_s3 - The ``S3_URL`` alias for the s3_url option has been deprecated and will be removed in release 5.0.0 (https://github.com/ansible-collections/community.aws/pull/795).
- ec2_ami - The ``DeviceName`` alias for the device_name option has been deprecated and will be removed in release 5.0.0 (https://github.com/ansible-collections/community.aws/pull/795).
- ec2_ami - The ``NoDevice`` alias for the no_device option has been deprecated and will be removed in release 5.0.0 (https://github.com/ansible-collections/community.aws/pull/795).
- ec2_ami - The ``VirtualName`` alias for the virtual_name option has been deprecated and will be removed in release 5.0.0 (https://github.com/ansible-collections/community.aws/pull/795).
- ec2_ami - the current default value of ``False`` for ``purge_tags`` has been deprecated and will be updated in release 5.0.0 to ``True`` (https://github.com/ansible-collections/amazon.aws/pull/846).
- ec2_instance - The default value for ```instance_type``` has been deprecated, in the future release you must set an instance_type or a launch_template (https://github.com/ansible-collections/amazon.aws/pull/587).
- ec2_instance - the current default value of ``False`` for ``purge_tags`` has been deprecated and will be updated in release 5.0.0 to ``True`` (https://github.com/ansible-collections/amazon.aws/pull/849).
- ec2_key - the current default value of ``False`` for ``purge_tags`` has been deprecated and will be updated in release 5.0.0 to ``True`` (https://github.com/ansible-collections/amazon.aws/pull/846).
- ec2_security_group - support for passing nested lists to ``cidr_ip`` and ``cidr_ipv6`` has been deprecated. Nested lists can be passed through the ``flatten`` filter instead ``cidr_ip: '{{ my_cidrs | flatten }}'`` (https://github.com/ansible-collections/amazon.aws/pull/1213).
- ec2_vol - the current default value of ``False`` for ``purge_tags`` has been deprecated and will be updated in release 5.0.0 to ``True`` (https://github.com/ansible-collections/amazon.aws/pull/846).
- ec2_vpc_dhcp_option_info - The ``DhcpOptionIds`` alias for the dhcp_option_ids option has been deprecated and will be removed in release 5.0.0 (https://github.com/ansible-collections/community.aws/pull/795).
- ec2_vpc_dhcp_option_info - The ``DryRun`` alias for the dry_run option has been deprecated and will be removed in release 5.0.0 (https://github.com/ansible-collections/community.aws/pull/795).
- ec2_vpc_endpoint - the current default value of ``False`` for ``purge_tags`` has been deprecated and will be updated in release 5.0.0 to ``True`` (https://github.com/ansible-collections/amazon.aws/pull/846).
- ec2_vpc_net - the current default value of ``False`` for ``purge_tags`` has been deprecated and will be updated in release 5.0.0 to ``True`` (https://github.com/ansible-collections/amazon.aws/pull/848).
- ec2_vpc_route_table - the current default value of ``False`` for ``purge_tags`` has been deprecated and will be updated in release 5.0.0 to ``True`` (https://github.com/ansible-collections/amazon.aws/pull/846).
- inventory/aws_ec2 - the ``include_extra_api_calls`` is now deprecated, its value is silently ignored (https://github.com/ansible-collections/amazon.aws/pull/1097).
- module_utils.cloud - removal of the ``CloudRetry.backoff`` has been delayed until release 6.0.0.  It is recommended to update custom modules to use ``jittered_backoff`` or ``exponential_backoff`` instead (https://github.com/ansible-collections/amazon.aws/pull/951).
- module_utils.url - ``ansible_collections.amazon.aws.module_utils.urls`` is believed to be unused and has been deprecated and will be removed in release 7.0.0.
- s3_bucket - The ``S3_URL`` alias for the s3_url option has been deprecated and will be removed in release 5.0.0 (https://github.com/ansible-collections/community.aws/pull/795).
- s3_object - Support for creation and deletion of S3 buckets has been deprecated.  Please use the ``amazon.aws.s3_bucket`` module to create and delete buckets (https://github.com/ansible-collections/amazon.aws/pull/869).

cisco.ios
~~~~~~~~~

- Deprecated ios_linkagg_module in favor of ios_lag_interfaces.

cisco.mso
~~~~~~~~~

- The mso_schema_template_contract_filter contract_filter_type attribute is deprecated. The value is now deduced from filter_type.

community.aws
~~~~~~~~~~~~~

- aws_acm - the current default value of ``False`` for ``purge_tags`` has been deprecated and will be updated in release 5.0.0 to ``True``.
- aws_codebuild - The ``tags`` parameter currently uses a non-standard format and has been deprecated.  In release 6.0.0 this parameter will accept a simple key/value pair dictionary instead of the current list of dictionaries.  It is recommended to migrate to using the resource_tags parameter which already accepts the simple dictionary format (https://github.com/ansible-collections/community.aws/pull/1221).
- aws_glue_connection - the ``connection_parameters`` return key has been deprecated and will be removed in a release after 2024-06-01, it is being replaced by the ``raw_connection_parameters`` key (https://github.com/ansible-collections/community.aws/pull/518).
- aws_kms - the current default value of ``False`` for ``purge_tags`` has been deprecated and will be updated in release 5.0.0 to ``True``.
- cloudfront_distribution - the current default value of ``False`` for ``purge_tags`` has been deprecated and will be updated in release 5.0.0 to ``True``.
- community.aws collection - due to the AWS SDKs announcing the end of support for Python less than 3.7 (https://aws.amazon.com/blogs/developer/python-support-policy-updates-for-aws-sdks-and-tools/) support for Python less than 3.7 by this collection has been deprecated and will be removed in a release after 2023-05-31 (https://github.com/ansible-collections/community.aws/pull/1361).
- ec2_vpc_vpn - the current default value of ``False`` for ``purge_tags`` has been deprecated and will be updated in release 5.0.0 to ``True``.
- iam_policy - the ``policies`` return value has been renamed ``policy_names`` and will be removed in a release after 2024-08-01, both values are currently returned (https://github.com/ansible-collections/community.aws/pull/1375).
- lambda_info - The ``function`` return key returns a dictionary of dictionaries and has been deprecated. In a release after 2025-01-01, this key will be removed in favor of ``functions``, which returns a list of dictionaries (https://github.com/ansible-collections/community.aws/pull/1239).
- rds_param_group - the current default value of ``False`` for ``purge_tags`` has been deprecated and will be updated in release 5.0.0 to ``True``.
- route53_health_check - the current default value of ``False`` for ``purge_tags`` has been deprecated and will be updated in release 5.0.0 to ``True``.
- route53_info - The CamelCase return values for ``DelegationSets``, ``CheckerIpRanges``, and ``HealthCheck`` have been deprecated, in the future release you must use snake_case return values ``delegation_sets``, ``checker_ip_ranges``, and ``health_check`` instead respectively" (https://github.com/ansible-collections/community.aws/pull/1322).
- route53_info - The CamelCase return values for ``HostedZones``, ``ResourceRecordSets``, and ``HealthChecks`` have been deprecated, in the future release you must use snake_case return values ``hosted_zones``, ``resource_record_sets``, and ``health_checks`` instead respectively".
- route53_zone - the current default value of ``False`` for ``purge_tags`` has been deprecated and will be updated in release 5.0.0 to ``True``.
- sqs_queue - the current default value of ``False`` for ``purge_tags`` has been deprecated and will be updated in release 5.0.0 to ``True``.

community.crypto
~~~~~~~~~~~~~~~~

- Support for Ansible 2.9 and ansible-base 2.10 is deprecated, and will be removed in the next major release (community.crypto 3.0.0). Some modules might still work with these versions afterwards, but we will no longer keep compatibility code that was needed to support them (https://github.com/ansible-collections/community.crypto/pull/460).

community.docker
~~~~~~~~~~~~~~~~

- Support for Docker API version 1.20 to 1.24 has been deprecated and will be removed in community.docker 3.0.0. The first Docker version supporting API version 1.25 was Docker 1.13, released in January 2017. This affects the modules ``docker_container``, ``docker_container_exec``, ``docker_container_info``, ``docker_compose``, ``docker_login``, ``docker_image``, ``docker_image_info``, ``docker_image_load``, ``docker_host_info``, ``docker_network``, ``docker_network_info``, ``docker_node_info``, ``docker_swarm_info``, ``docker_swarm_service``, ``docker_swarm_service_info``, ``docker_volume_info``, and ``docker_volume``, whose minimally supported API version is between 1.20 and 1.24 (https://github.com/ansible-collections/community.docker/pull/396).
- Support for Python 2.6 is deprecated and will be removed in the next major release (community.docker 3.0.0). Some modules might still work with Python 2.6, but we will no longer try to ensure compatibility (https://github.com/ansible-collections/community.docker/pull/388).
- docker_container - the ``ignore_image`` option is deprecated and will be removed in community.docker 4.0.0. Use ``image: ignore`` in ``comparisons`` instead (https://github.com/ansible-collections/community.docker/pull/487).
- docker_container - the ``purge_networks`` option is deprecated and will be removed in community.docker 4.0.0. Use ``networks: strict`` in ``comparisons`` instead, and make sure to provide ``networks``, with value ``[]`` if all networks should be removed (https://github.com/ansible-collections/community.docker/pull/487).

community.general
~~~~~~~~~~~~~~~~~

- ArgFormat module utils - deprecated along ``CmdMixin``, in favor of the ``cmd_runner_fmt`` module util (https://github.com/ansible-collections/community.general/pull/5370).
- CmdMixin module utils - deprecated in favor of the ``CmdRunner`` module util (https://github.com/ansible-collections/community.general/pull/5370).
- CmdModuleHelper module utils - deprecated in favor of the ``CmdRunner`` module util (https://github.com/ansible-collections/community.general/pull/5370).
- CmdStateModuleHelper module utils - deprecated in favor of the ``CmdRunner`` module util (https://github.com/ansible-collections/community.general/pull/5370).
- cmd_runner module utils - deprecated ``fmt`` in favour of ``cmd_runner_fmt`` as the parameter format object (https://github.com/ansible-collections/community.general/pull/4777).
- django_manage - support for Django releases older than 4.1 has been deprecated and will be removed in community.general 9.0.0 (https://github.com/ansible-collections/community.general/pull/5400).
- django_manage - support for the commands ``cleanup``, ``syncdb`` and ``validate`` that have been deprecated in Django long time ago will be removed in community.general 9.0.0 (https://github.com/ansible-collections/community.general/pull/5400).
- django_manage - the behavior of "creating the virtual environment when missing" is being deprecated and will be removed in community.general version 9.0.0 (https://github.com/ansible-collections/community.general/pull/5405).
- gconftool2 - deprecates ``state=get`` in favor of using the module ``gconftool2_info`` (https://github.com/ansible-collections/community.general/pull/4778).
- lxc_container - the module will no longer make any effort to support Python 2 (https://github.com/ansible-collections/community.general/pull/5304).
- newrelic_deployment - ``appname`` and ``environment`` are no longer valid options in the v2 API. They will be removed in community.general 7.0.0 (https://github.com/ansible-collections/community.general/pull/5341).
- proxmox - deprecated the current ``unprivileged`` default value, will be changed to ``true`` in community.general 7.0.0 (https://github.com/pull/5224).
- xfconf - deprecated parameter ``disable_facts``, as since version 4.0.0 it only allows value ``true`` (https://github.com/ansible-collections/community.general/pull/4520).

community.hashi_vault
~~~~~~~~~~~~~~~~~~~~~

- vault_kv2_get lookup - the ``engine_mount_point option`` in the ``vault_kv2_get`` lookup only will change its default from ``kv`` to ``secret`` in community.hashi_vault version 4.0.0 (https://github.com/ansible-collections/community.hashi_vault/issues/279).

Removed Features (previously deprecated)
----------------------------------------

Ansible-core
~~~~~~~~~~~~

- PlayIterator - remove deprecated ``PlayIterator.ITERATING_*`` and ``PlayIterator.FAILED_*``
- Remove deprecated ``ALLOW_WORLD_READABLE_TMPFILES`` configuration option (https://github.com/ansible/ansible/issues/77393)
- Remove deprecated ``COMMAND_WARNINGS`` configuration option (https://github.com/ansible/ansible/issues/77394)
- Remove deprecated ``DISPLAY_SKIPPED_HOSTS`` environment variable (https://github.com/ansible/ansible/issues/77396)
- Remove deprecated ``LIBVIRT_LXC_NOSECLABEL`` environment variable (https://github.com/ansible/ansible/issues/77395)
- Remove deprecated ``NETWORK_GROUP_MODULES`` environment variable (https://github.com/ansible/ansible/issues/77397)
- Remove deprecated ``UnsafeProxy``
- Remove deprecated ``plugin_filters_cfg`` config option from ``default`` section (https://github.com/ansible/ansible/issues/77398)
- Remove deprecated functionality that allows loading cache plugins directly without using ``cache_loader``.
- Remove deprecated functionality that allows subclassing ``DefaultCallback`` without the corresponding ``doc_fragment``.
- Remove deprecated powershell functions ``Load-CommandUtils`` and ``Import-PrivilegeUtil``
- apt_key - remove deprecated ``key`` module param
- command/shell - remove deprecated ``warn`` module param
- get_url - remove deprecated ``sha256sum`` module param
- import_playbook - remove deprecated functionality that allows providing additional parameters in free form

amazon.aws
~~~~~~~~~~

- cloudformation - the ``template_format`` option has been removed. It has been ignored by the module since Ansible 2.3 (https://github.com/ansible-collections/amazon.aws/pull/833).
- ec2_key - the ``wait_timeout`` option had no effect, was deprecated in release 1.0.0, and has now been removed (https://github.com/ansible-collections/amazon.aws/pull/830).
- ec2_key - the ``wait`` option had no effect, was deprecated in release 1.0.0, and has now been removed (https://github.com/ansible-collections/amazon.aws/pull/830).
- ec2_tag - the previously deprecated state ``list`` has been removed.  To list tags on an EC2 resource the ``ec2_tag_info`` module can be used (https://github.com/ansible-collections/amazon.aws/pull/829).
- ec2_vol - the previously deprecated state ``list`` has been removed.  To list volumes the ``ec2_vol_info`` module can be used (https://github.com/ansible-collections/amazon.aws/pull/828).
- module_utils.batch - the class ``ansible_collections.amazon.aws.plugins.module_utils.batch.AWSConnection`` has been removed.  Please use ``AnsibleAWSModule.client()`` instead (https://github.com/ansible-collections/amazon.aws/pull/831).

ansible.netcommon
~~~~~~~~~~~~~~~~~

- napalm - Removed unused connection plugin.
- net_banner - Use <network_os>_banner instead.
- net_interface - Use <network_os>_interfaces instead.
- net_l2_interface - Use <network_os>_l2_interfaces instead.
- net_l3_interface - Use <network_os>_l3_interfaces instead.
- net_linkagg - Use <network_os>_lag_interfaces instead.
- net_lldp - Use <network_os>_lldp_global instead.
- net_lldp_interface - Use <network_os>_lldp_interfaces instead.
- net_logging - Use <network_os>_logging_global instead.
- net_static_route - Use <network_os>_static_routes instead.
- net_system - Use <network_os>_system instead.
- net_user - Use <network_os>_user instead.
- net_vlan - Use <network_os>_vlans instead.
- net_vrf - Use <network_os>_vrf instead.

cisco.ios
~~~~~~~~~

- ios_interface - use ios_interfaces instead.
- ios_l2_interface - use ios_l2_interfaces instead.
- ios_l3_interface - use ios_l3_interfaces instead.
- ios_static_route - use ios_static_routes instead.
- ios_vlan - use ios_vlans instead.

cisco.iosxr
~~~~~~~~~~~

- iosxr_interface - use iosxr_interfaces instead.

cisco.nxos
~~~~~~~~~~

- This release removes the following deprecated plugins that have reached their end-of-life.
- nxos_acl
- nxos_acl_interface
- nxos_interface
- nxos_interface_ospf
- nxos_l2_interface
- nxos_l3_interface
- nxos_linkagg
- nxos_lldp
- nxos_ospf
- nxos_ospf_vrf
- nxos_smu
- nxos_static_route
- nxos_vlan

community.aws
~~~~~~~~~~~~~

- aws_kms_info - the unused and deprecated ``keys_attr`` parameter has been removed (https://github.com/ansible-collections/amazon.aws/pull/1172).
- data_pipeline - the ``version`` option has always been ignored and has been removed (https://github.com/ansible-collections/community.aws/pull/1160"
- ec2_eip - The ``wait_timeout`` option has been removed. It has always been ignored by the module (https://github.com/ansible-collections/community.aws/pull/1159).
- ec2_lc - the ``associate_public_ip_address`` option has been removed. It has always been ignored by the module (https://github.com/ansible-collections/community.aws/pull/1158).
- ec2_metric_alarm - support for using the ``<=``, ``<``, ``>`` and ``>=`` operators for comparison has been dropped. Please use ``LessThanOrEqualToThreshold``, ``LessThanThreshold``, ``GreaterThanThreshold`` or ``GreaterThanOrEqualToThreshold`` instead (https://github.com/ansible-collections/amazon.aws/pull/1164).
- ecs_ecr - The deprecated alias ``delete_policy`` has been removed.  Please use ``purge_policy`` instead (https://github.com/ansible-collections/community.aws/pull/1161).
- iam_managed_policy - the unused ``fail_on_delete`` parameter has been removed (https://github.com/ansible-collections/community.aws/pull/1168)
- s3_lifecycle - the unused parameter ``requester_pays`` has been removed (https://github.com/ansible-collections/community.aws/pull/1165).
- s3_sync - remove unused ``retries`` parameter (https://github.com/ansible-collections/community.aws/pull/1166).

community.azure
~~~~~~~~~~~~~~~

- azure_rm_aks_facts, azure_rm_aks_info - the deprecated modules have been removed. Use azure.azcollection.azure_rm_aks_info instead  (https://github.com/ansible-collections/community.azure/pull/31).
- azure_rm_aksversion_facts, azure_rm_aksversion_info - the deprecated modules have been removed. Use azure.azcollection.azure_rm_aksversion_info instead  (https://github.com/ansible-collections/community.azure/pull/31).
- azure_rm_applicationsecuritygroup_facts, azure_rm_applicationsecuritygroup_info - the deprecated modules have been removed. Use azure.azcollection.azure_rm_applicationsecuritygroup_info instead  (https://github.com/ansible-collections/community.azure/pull/31).
- azure_rm_appserviceplan_facts, azure_rm_appserviceplan_info - the deprecated modules have been removed. Use azure.azcollection.azure_rm_appserviceplan_info instead  (https://github.com/ansible-collections/community.azure/pull/31).
- azure_rm_automationaccount_facts, azure_rm_automationaccount_info - the deprecated modules have been removed. Use azure.azcollection.azure_rm_automationaccount_info instead  (https://github.com/ansible-collections/community.azure/pull/31).
- azure_rm_autoscale_facts, azure_rm_autoscale_info - the deprecated modules have been removed. Use azure.azcollection.azure_rm_autoscale_info instead  (https://github.com/ansible-collections/community.azure/pull/31).
- azure_rm_availabilityset_facts, azure_rm_availabilityset_info - the deprecated modules have been removed. Use azure.azcollection.azure_rm_availabilityset_info instead  (https://github.com/ansible-collections/community.azure/pull/31).
- azure_rm_cdnendpoint_facts, azure_rm_cdnendpoint_info - the deprecated modules have been removed. Use azure.azcollection.azure_rm_cdnendpoint_info instead  (https://github.com/ansible-collections/community.azure/pull/31).
- azure_rm_cdnprofile_facts, azure_rm_cdnprofile_info - the deprecated modules have been removed. Use azure.azcollection.azure_rm_cdnprofile_info instead  (https://github.com/ansible-collections/community.azure/pull/31).
- azure_rm_containerinstance_facts, azure_rm_containerinstance_info - the deprecated modules have been removed. Use azure.azcollection.azure_rm_containerinstance_info instead  (https://github.com/ansible-collections/community.azure/pull/31).
- azure_rm_containerregistry_facts, azure_rm_containerregistry_info - the deprecated modules have been removed. Use azure.azcollection.azure_rm_containerregistry_info instead  (https://github.com/ansible-collections/community.azure/pull/31).
- azure_rm_cosmosdbaccount_facts, azure_rm_cosmosdbaccount_info - the deprecated modules have been removed. Use azure.azcollection.azure_rm_cosmosdbaccount_info instead  (https://github.com/ansible-collections/community.azure/pull/31).
- azure_rm_deployment_facts, azure_rm_deployment_info - the deprecated modules have been removed. Use azure.azcollection.azure_rm_deployment_info instead  (https://github.com/ansible-collections/community.azure/pull/31).
- azure_rm_devtestlab_facts, azure_rm_devtestlab_info - the deprecated modules have been removed. Use azure.azcollection.azure_rm_devtestlab_info instead  (https://github.com/ansible-collections/community.azure/pull/31).
- azure_rm_devtestlabarmtemplate_facts, azure_rm_devtestlabarmtemplate_info - the deprecated modules have been removed. Use azure.azcollection.azure_rm_devtestlabarmtemplate_info instead  (https://github.com/ansible-collections/community.azure/pull/31).
- azure_rm_devtestlabartifact_facts, azure_rm_devtestlabartifact_info - the deprecated modules have been removed. Use azure.azcollection.azure_rm_devtestlabartifact_info instead  (https://github.com/ansible-collections/community.azure/pull/31).
- azure_rm_devtestlabartifactsource_facts, azure_rm_devtestlabartifactsource_info - the deprecated modules have been removed. Use azure.azcollection.azure_rm_devtestlabartifactsource_info instead  (https://github.com/ansible-collections/community.azure/pull/31).
- azure_rm_devtestlabcustomimage_facts, azure_rm_devtestlabcustomimage_info - the deprecated modules have been removed. Use azure.azcollection.azure_rm_devtestlabcustomimage_info instead  (https://github.com/ansible-collections/community.azure/pull/31).
- azure_rm_devtestlabenvironment_facts, azure_rm_devtestlabenvironment_info - the deprecated modules have been removed. Use azure.azcollection.azure_rm_devtestlabenvironment_info instead  (https://github.com/ansible-collections/community.azure/pull/31).
- azure_rm_devtestlabpolicy_facts, azure_rm_devtestlabpolicy_info - the deprecated modules have been removed. Use azure.azcollection.azure_rm_devtestlabpolicy_info instead  (https://github.com/ansible-collections/community.azure/pull/31).
- azure_rm_devtestlabschedule_facts, azure_rm_devtestlabschedule_info - the deprecated modules have been removed. Use azure.azcollection.azure_rm_devtestlabschedule_info instead  (https://github.com/ansible-collections/community.azure/pull/31).
- azure_rm_devtestlabvirtualmachine_facts, azure_rm_devtestlabvirtualmachine_info - the deprecated modules have been removed. Use azure.azcollection.azure_rm_devtestlabvirtualmachine_info instead  (https://github.com/ansible-collections/community.azure/pull/31).
- azure_rm_devtestlabvirtualnetwork_facts, azure_rm_devtestlabvirtualnetwork_info - the deprecated modules have been removed. Use azure.azcollection.azure_rm_devtestlabvirtualnetwork_info instead  (https://github.com/ansible-collections/community.azure/pull/31).
- azure_rm_dnsrecordset_facts, azure_rm_dnsrecordset_info - the deprecated modules have been removed. Use azure.azcollection.azure_rm_dnsrecordset_info instead  (https://github.com/ansible-collections/community.azure/pull/31).
- azure_rm_dnszone_facts, azure_rm_dnszone_info - the deprecated modules have been removed. Use azure.azcollection.azure_rm_dnszone_info instead  (https://github.com/ansible-collections/community.azure/pull/31).
- azure_rm_functionapp_facts, azure_rm_functionapp_info - the deprecated modules have been removed. Use azure.azcollection.azure_rm_functionapp_info instead  (https://github.com/ansible-collections/community.azure/pull/31).
- azure_rm_hdinsightcluster_facts, azure_rm_hdinsightcluster_info - the deprecated modules have been removed. Use azure.azcollection.azure_rm_hdinsightcluster_info instead  (https://github.com/ansible-collections/community.azure/pull/31).
- azure_rm_image_facts, azure_rm_image_info - the deprecated modules have been removed. Use azure.azcollection.azure_rm_image_info instead  (https://github.com/ansible-collections/community.azure/pull/31).
- azure_rm_loadbalancer_facts, azure_rm_loadbalancer_info - the deprecated modules have been removed. Use azure.azcollection.azure_rm_loadbalancer_info instead  (https://github.com/ansible-collections/community.azure/pull/31).
- azure_rm_lock_facts, azure_rm_lock_info - the deprecated modules have been removed. Use azure.azcollection.azure_rm_lock_info instead  (https://github.com/ansible-collections/community.azure/pull/31).
- azure_rm_loganalyticsworkspace_facts, azure_rm_loganalyticsworkspace_info - the deprecated modules have been removed. Use azure.azcollection.azure_rm_loganalyticsworkspace_info instead  (https://github.com/ansible-collections/community.azure/pull/31).
- azure_rm_managed_disk, azure_rm_manageddisk - the deprecated modules have been removed. Use azure.azcollection.azure_rm_manageddisk instead  (https://github.com/ansible-collections/community.azure/pull/31).
- azure_rm_managed_disk_facts, azure_rm_manageddisk_facts, azure_rm_manageddisk_info - the deprecated modules have been removed. Use azure.azcollection.azure_rm_manageddisk_info instead  (https://github.com/ansible-collections/community.azure/pull/31).
- azure_rm_mariadbconfiguration_facts, azure_rm_mariadbconfiguration_info - the deprecated modules have been removed. Use azure.azcollection.azure_rm_mariadbconfiguration_info instead  (https://github.com/ansible-collections/community.azure/pull/31).
- azure_rm_mariadbdatabase_facts, azure_rm_mariadbdatabase_info - the deprecated modules have been removed. Use azure.azcollection.azure_rm_mariadbdatabase_info instead  (https://github.com/ansible-collections/community.azure/pull/31).
- azure_rm_mariadbfirewallrule_facts, azure_rm_mariadbfirewallrule_info - the deprecated modules have been removed. Use azure.azcollection.azure_rm_mariadbfirewallrule_info instead  (https://github.com/ansible-collections/community.azure/pull/31).
- azure_rm_mariadbserver_facts, azure_rm_mariadbserver_info - the deprecated modules have been removed. Use azure.azcollection.azure_rm_mariadbserver_info instead  (https://github.com/ansible-collections/community.azure/pull/31).
- azure_rm_mysqlconfiguration_facts, azure_rm_mysqlconfiguration_info - the deprecated modules have been removed. Use azure.azcollection.azure_rm_mysqlconfiguration_info instead  (https://github.com/ansible-collections/community.azure/pull/31).
- azure_rm_mysqldatabase_facts, azure_rm_mysqldatabase_info - the deprecated modules have been removed. Use azure.azcollection.azure_rm_mysqldatabase_info instead  (https://github.com/ansible-collections/community.azure/pull/31).
- azure_rm_mysqlfirewallrule_facts, azure_rm_mysqlfirewallrule_info - the deprecated modules have been removed. Use azure.azcollection.azure_rm_mysqlfirewallrule_info instead  (https://github.com/ansible-collections/community.azure/pull/31).
- azure_rm_mysqlserver_facts, azure_rm_mysqlserver_info - the deprecated modules have been removed. Use azure.azcollection.azure_rm_mysqlserver_info instead  (https://github.com/ansible-collections/community.azure/pull/31).
- azure_rm_networkinterface_facts, azure_rm_networkinterface_info - the deprecated modules have been removed. Use azure.azcollection.azure_rm_networkinterface_info instead  (https://github.com/ansible-collections/community.azure/pull/31).
- azure_rm_postgresqlconfiguration_facts, azure_rm_postgresqlconfiguration_info - the deprecated modules have been removed. Use azure.azcollection.azure_rm_postgresqlconfiguration_info instead  (https://github.com/ansible-collections/community.azure/pull/31).
- azure_rm_postgresqldatabase_facts, azure_rm_postgresqldatabase_info - the deprecated modules have been removed. Use azure.azcollection.azure_rm_postgresqldatabase_info instead  (https://github.com/ansible-collections/community.azure/pull/31).
- azure_rm_postgresqlfirewallrule_facts, azure_rm_postgresqlfirewallrule_info - the deprecated modules have been removed. Use azure.azcollection.azure_rm_postgresqlfirewallrule_info instead  (https://github.com/ansible-collections/community.azure/pull/31).
- azure_rm_postgresqlserver_facts, azure_rm_postgresqlserver_info - the deprecated modules have been removed. Use azure.azcollection.azure_rm_postgresqlserver_info instead  (https://github.com/ansible-collections/community.azure/pull/31).
- azure_rm_publicipaddress_facts, azure_rm_publicipaddress_info - the deprecated modules have been removed. Use azure.azcollection.azure_rm_publicipaddress_info instead  (https://github.com/ansible-collections/community.azure/pull/31).
- azure_rm_rediscache_facts, azure_rm_rediscache_info - the deprecated modules have been removed. Use azure.azcollection.azure_rm_rediscache_info instead  (https://github.com/ansible-collections/community.azure/pull/31).
- azure_rm_resource_facts, azure_rm_resource_info - the deprecated modules have been removed. Use azure.azcollection.azure_rm_resource_info instead  (https://github.com/ansible-collections/community.azure/pull/31).
- azure_rm_resourcegroup_facts, azure_rm_resourcegroup_info - the deprecated modules have been removed. Use azure.azcollection.azure_rm_resourcegroup_info instead  (https://github.com/ansible-collections/community.azure/pull/31).
- azure_rm_roleassignment_facts, azure_rm_roleassignment_info - the deprecated modules have been removed. Use azure.azcollection.azure_rm_roleassignment_info instead  (https://github.com/ansible-collections/community.azure/pull/31).
- azure_rm_roledefinition_facts, azure_rm_roledefinition_info - the deprecated modules have been removed. Use azure.azcollection.azure_rm_roledefinition_info instead  (https://github.com/ansible-collections/community.azure/pull/31).
- azure_rm_routetable_facts, azure_rm_routetable_info - the deprecated modules have been removed. Use azure.azcollection.azure_rm_routetable_info instead  (https://github.com/ansible-collections/community.azure/pull/31).
- azure_rm_securitygroup_facts, azure_rm_securitygroup_info - the deprecated modules have been removed. Use azure.azcollection.azure_rm_securitygroup_info instead  (https://github.com/ansible-collections/community.azure/pull/31).
- azure_rm_servicebus_facts, azure_rm_servicebus_info - the deprecated modules have been removed. Use azure.azcollection.azure_rm_servicebus_info instead  (https://github.com/ansible-collections/community.azure/pull/31).
- azure_rm_sqldatabase_facts, azure_rm_sqldatabase_info - the deprecated modules have been removed. Use azure.azcollection.azure_rm_sqldatabase_info instead  (https://github.com/ansible-collections/community.azure/pull/31).
- azure_rm_sqlfirewallrule_facts, azure_rm_sqlfirewallrule_info - the deprecated modules have been removed. Use azure.azcollection.azure_rm_sqlfirewallrule_info instead  (https://github.com/ansible-collections/community.azure/pull/31).
- azure_rm_sqlserver_facts, azure_rm_sqlserver_info - the deprecated modules have been removed. Use azure.azcollection.azure_rm_sqlserver_info instead  (https://github.com/ansible-collections/community.azure/pull/31).
- azure_rm_storageaccount_facts, azure_rm_storageaccount_info - the deprecated modules have been removed. Use azure.azcollection.azure_rm_storageaccount_info instead  (https://github.com/ansible-collections/community.azure/pull/31).
- azure_rm_subnet_facts, azure_rm_subnet_info - the deprecated modules have been removed. Use azure.azcollection.azure_rm_subnet_info instead  (https://github.com/ansible-collections/community.azure/pull/31).
- azure_rm_trafficmanagerendpoint_facts, azure_rm_trafficmanagerendpoint_info - the deprecated modules have been removed. Use azure.azcollection.azure_rm_trafficmanagerendpoint_info instead  (https://github.com/ansible-collections/community.azure/pull/31).
- azure_rm_trafficmanagerprofile_facts, azure_rm_trafficmanagerprofile_info - the deprecated modules have been removed. Use azure.azcollection.azure_rm_trafficmanagerprofile_info instead  (https://github.com/ansible-collections/community.azure/pull/31).
- azure_rm_virtualmachine_extension, azure_rm_virtualmachineextension - the deprecated modules have been removed. Use azure.azcollection.azure_rm_virtualmachineextension instead  (https://github.com/ansible-collections/community.azure/pull/31).
- azure_rm_virtualmachine_facts, azure_rm_virtualmachine_info - the deprecated modules have been removed. Use azure.azcollection.azure_rm_virtualmachine_info instead  (https://github.com/ansible-collections/community.azure/pull/31).
- azure_rm_virtualmachine_scaleset, azure_rm_virtualmachinescaleset - the deprecated modules have been removed. Use azure.azcollection.azure_rm_virtualmachinescaleset instead  (https://github.com/ansible-collections/community.azure/pull/31).
- azure_rm_virtualmachine_scaleset_facts, azure_rm_virtualmachinescaleset_facts, azure_rm_virtualmachinescaleset_info - the deprecated modules have been removed. Use azure.azcollection.azure_rm_virtualmachinescaleset_info instead  (https://github.com/ansible-collections/community.azure/pull/31).
- azure_rm_virtualmachineextension_facts, azure_rm_virtualmachineextension_info - the deprecated modules have been removed. Use azure.azcollection.azure_rm_virtualmachineextension_info instead  (https://github.com/ansible-collections/community.azure/pull/31).
- azure_rm_virtualmachineimage_facts, azure_rm_virtualmachineimage_info - the deprecated modules have been removed. Use azure.azcollection.azure_rm_virtualmachineimage_info instead  (https://github.com/ansible-collections/community.azure/pull/31).
- azure_rm_virtualmachinescalesetextension_facts, azure_rm_virtualmachinescalesetextension_info - the deprecated modules have been removed. Use azure.azcollection.azure_rm_virtualmachinescalesetextension_info instead  (https://github.com/ansible-collections/community.azure/pull/31).
- azure_rm_virtualmachinescalesetinstance_facts, azure_rm_virtualmachinescalesetinstance_info - the deprecated modules have been removed. Use azure.azcollection.azure_rm_virtualmachinescalesetinstance_info instead  (https://github.com/ansible-collections/community.azure/pull/31).
- azure_rm_virtualnetwork_facts, azure_rm_virtualnetwork_info - the deprecated modules have been removed. Use azure.azcollection.azure_rm_virtualnetwork_info instead  (https://github.com/ansible-collections/community.azure/pull/31).
- azure_rm_virtualnetworkpeering_facts, azure_rm_virtualnetworkpeering_info - the deprecated modules have been removed. Use azure.azcollection.azure_rm_virtualnetworkpeering_info instead  (https://github.com/ansible-collections/community.azure/pull/31).
- azure_rm_webapp_facts, azure_rm_webapp_info - the deprecated modules have been removed. Use azure.azcollection.azure_rm_webapp_info instead  (https://github.com/ansible-collections/community.azure/pull/31).

community.docker
~~~~~~~~~~~~~~~~

- Execution Environments built with community.docker no longer include docker-compose < 2.0.0. If you need to use it with the ``docker_compose`` module, please install that requirement manually (https://github.com/ansible-collections/community.docker/pull/400).
- Support for Ansible 2.9 and ansible-base 2.10 has been removed. If you need support for Ansible 2.9 or ansible-base 2.10, please use community.docker 2.x.y (https://github.com/ansible-collections/community.docker/pull/400).
- Support for Docker API versions 1.20 to 1.24 has been removed. If you need support for these API versions, please use community.docker 2.x.y (https://github.com/ansible-collections/community.docker/pull/400).
- Support for Python 2.6 has been removed. If you need support for Python 2.6, please use community.docker 2.x.y (https://github.com/ansible-collections/community.docker/pull/400).
- Various modules - the default of ``tls_hostname`` (``localhost``) has been removed. If you want to continue using ``localhost``, you need to specify it explicitly (https://github.com/ansible-collections/community.docker/pull/363).
- docker_container - the ``all`` value is no longer allowed in ``published_ports``. Use ``publish_all_ports=true`` instead (https://github.com/ansible-collections/community.docker/pull/399).
- docker_container - the default of ``command_handling`` was changed from ``compatibility`` to ``correct``. Older versions were warning for every invocation of the module when this would result in a change of behavior (https://github.com/ansible-collections/community.docker/pull/399).
- docker_stack - the return values ``out`` and ``err`` have been removed. Use ``stdout`` and ``stderr`` instead (https://github.com/ansible-collections/community.docker/pull/363).

community.general
~~~~~~~~~~~~~~~~~

- bitbucket* modules - ``username`` is no longer an alias of ``workspace``, but of ``user`` (https://github.com/ansible-collections/community.general/pull/5326).
- gem - the default of the ``norc`` option changed from ``false`` to ``true`` (https://github.com/ansible-collections/community.general/pull/5326).
- gitlab_group_members - ``gitlab_group`` must now always contain the full path, and no longer just the name or path (https://github.com/ansible-collections/community.general/pull/5326).
- keycloak_authentication - the return value ``flow`` has been removed. Use ``end_state`` instead (https://github.com/ansible-collections/community.general/pull/5326).
- keycloak_group - the return value ``group`` has been removed. Use ``end_state`` instead (https://github.com/ansible-collections/community.general/pull/5326).
- lxd_container - the default of the ``ignore_volatile_options`` option changed from ``true`` to ``false`` (https://github.com/ansible-collections/community.general/pull/5326).
- mail callback plugin - the ``sender`` option is now required (https://github.com/ansible-collections/community.general/pull/5326).
- module_helper module utils - remove the ``VarDict`` attribute from ``ModuleHelper``. Import ``VarDict`` from ``ansible_collections.community.general.plugins.module_utils.mh.mixins.vars`` instead (https://github.com/ansible-collections/community.general/pull/5326).
- proxmox inventory plugin - the default of the ``want_proxmox_nodes_ansible_host`` option changed from ``true`` to ``false`` (https://github.com/ansible-collections/community.general/pull/5326).
- vmadm - the ``debug`` option has been removed. It was not used anyway (https://github.com/ansible-collections/community.general/pull/5326).

community.network
~~~~~~~~~~~~~~~~~

- aireos modules - removed deprecated ``connection: local`` support. Use ``connection: network_cli`` instead (https://github.com/ansible-collections/community.network/pull/440).
- aireos modules - removed deprecated ``provider`` option. Use ``connection: network_cli`` instead (https://github.com/ansible-collections/community.network/pull/440).
- aruba modules - removed deprecated ``connection: local`` support. Use ``connection: network_cli`` instead (https://github.com/ansible-collections/community.network/pull/440).
- aruba modules - removed deprecated ``provider`` option. Use ``connection: network_cli`` instead (https://github.com/ansible-collections/community.network/pull/440).
- ce modules - removed deprecated ``connection: local`` support. Use ``connection: network_cli`` instead (https://github.com/ansible-collections/community.network/pull/440).
- ce modules - removed deprecated ``provider`` option. Use ``connection: network_cli`` instead (https://github.com/ansible-collections/community.network/pull/440).
- enos modules - removed deprecated ``connection: local`` support. Use ``connection: network_cli`` instead (https://github.com/ansible-collections/community.network/pull/440).
- enos modules - removed deprecated ``provider`` option. Use ``connection: network_cli`` instead (https://github.com/ansible-collections/community.network/pull/440).
- ironware modules - removed deprecated ``connection: local`` support. Use ``connection: network_cli`` instead (https://github.com/ansible-collections/community.network/pull/440).
- ironware modules - removed deprecated ``provider`` option. Use ``connection: network_cli`` instead (https://github.com/ansible-collections/community.network/pull/440).
- sros modules - removed deprecated ``connection: local`` support. Use ``connection: network_cli`` instead (https://github.com/ansible-collections/community.network/pull/440).
- sros modules - removed deprecated ``provider`` option. Use ``connection: network_cli`` instead (https://github.com/ansible-collections/community.network/pull/440).

community.vmware
~~~~~~~~~~~~~~~~

- vca_fw - The deprecated module ``vca_fw`` has been removed.
- vca_nat - The deprecated module ``vca_nat`` has been removed.
- vca_vapp - The deprecated module ``vca_vapp`` has been removed.
- vmware_dns_config - The deprecated module ``vmware_dns_config`` has been removed, you can use ``vmware_host_dns`` instead.
- vmware_guest_network - The deprecated parameter ``networks`` has been removed, use loops to handle multiple interfaces (https://github.com/ansible-collections/community.vmware/pull/1459).
- vmware_guest_vnc - The deprecated module ``vmware_guest_vnc`` has been removed. The VNC support has been dropped with vSphere 7 and later (https://github.com/ansible-collections/community.vmware/pull/1454).
- vmware_host_firewall_manager - The module doesn't accept a list for ``allowed_hosts`` anymore, use a dict instead. Additionally, ``all_ip`` is now a required sub-option of ``allowed_hosts`` (https://github.com/ansible-collections/community.vmware/pull/1463).
- vsphere_copy - The deprecated parameters ``host`` and ``login`` have been removed. Use ``hostname`` and ``username`` instead (https://github.com/ansible-collections/community.vmware/pull/1456).

junipernetworks.junos
~~~~~~~~~~~~~~~~~~~~~

- Remove following deprecated Junos Modules.
- junos_interface
- junos_l2_interface
- junos_l3_interface
- junos_linkagg
- junos_lldp
- junos_lldp_interface
- junos_static_route
- junos_vlan

vyos.vyos
~~~~~~~~~

- vyos_interface - use vyos_interfaces instead.
- vyos_l3_interface - use vyos_l3_interfaces instead.
- vyos_linkagg - use vyos_lag_interfaces instead.
- vyos_lldp - use vyos_lldp_global instead.
- vyos_lldp_interface - use vyos_lldp_interfaces instead.
- vyos_static_route - use vyos_static_routes instead.

Security Fixes
--------------

amazon.aws
~~~~~~~~~~

- ec2_instance - fixes leak of password into logs when using ``tower_callback.windows=True`` and ``tower_callback.set_password`` (https://github.com/ansible-collections/amazon.aws/pull/1199).

community.docker
~~~~~~~~~~~~~~~~

- modules and plugins communicating directly with the Docker daemon - when connecting by SSH and not using ``use_ssh_client=true``, reject unknown host keys instead of accepting them. This is only a change relative to older community.docker 3.0.0 pre-releases or with respect to Docker SDK for Python < 6.0.0. Docker SDK for Python 6.0.0 will also include this change (https://github.com/ansible-collections/community.docker/pull/434).

Bugfixes
--------

Ansible-core
~~~~~~~~~~~~

- "meta: refresh_inventory" does not clobber entries added by add_host/group_by anymore.
- Add PyYAML >= 5.1 as a dependency of ansible-core to be compatible with Python 3.8+.
- Avoid 'unreachable' error when chmod on AIX has 255 as return code.
- BSD network facts - Do not assume column indexes, look for ``netmask`` and ``broadcast`` for determining the correct columns when parsing ``inet`` line (https://github.com/ansible/ansible/issues/79117)
- Bug fix for when handlers were ran on failed hosts after an ``always`` section was executed (https://github.com/ansible/ansible/issues/52561)
- Do not allow handlers from dynamic includes to be notified (https://github.com/ansible/ansible/pull/78399)
- Do not crash when templating an expression with a test or filter that is not a valid Ansible filter name (https://github.com/ansible/ansible/issues/78912, https://github.com/ansible/ansible/pull/78913).
- Ensure handlers observe ``any_errors_fatal`` (https://github.com/ansible/ansible/issues/46447)
- Ensure syntax check errors include playbook filenames
- Ensure the correct ``environment_class`` is set on ``AnsibleJ2Template``
- Error for collection redirects that do not use fully qualified collection names, as the redirect would be determined by the ``collections`` keyword.
- Fix PluginLoader to mimic Python import machinery by adding module to sys.modules before exec
- Fix ``-vv`` output for meta tasks to not have an empty message when skipped, print the skip reason instead. (https://github.com/ansible/ansible/issues/77315)
- Fix an issue where ``ansible_play_hosts`` and ``ansible_play_batch`` were not properly updated when a failure occured in an explicit block inside the rescue section (https://github.com/ansible/ansible/issues/78612)
- Fix dnf module documentation to indicate that comparison operators for package version require spaces around them (https://github.com/ansible/ansible/issues/78295)
- Fix for linear strategy when tasks were executed in incorrect order or even removed from execution. (https://github.com/ansible/ansible/issues/64611, https://github.com/ansible/ansible/issues/64999, https://github.com/ansible/ansible/issues/72725, https://github.com/ansible/ansible/issues/72781)
- Fix for network_cli not getting all relevant connection options
- Fix handlers execution with ``serial`` in the ``linear`` strategy (https://github.com/ansible/ansible/issues/54991)
- Fix potential, but unlikely, cases of variable use before definition.
- Fix reusing a connection in a task loop that uses a redirected or aliased name - https://github.com/ansible/ansible/issues/78425
- Fix setting become activation in a task loop - https://github.com/ansible/ansible/issues/78425
- Fix traceback when installing a collection from a git repository and git is not installed (https://github.com/ansible/ansible/issues/77479).
- GALAXY_IGNORE_CERTS reworked to allow each server entry to override
- More gracefully handle separator errors in jinja2 template overrides (https://github.com/ansible/ansible/pull/77495).
- Move undefined check from concat to finalize (https://github.com/ansible/ansible/issues/78156)
- Prevent losing unsafe on results returned from lookups (https://github.com/ansible/ansible/issues/77535)
- Propagate ``ansible_failed_task`` and ``ansible_failed_result`` to an outer rescue (https://github.com/ansible/ansible/issues/43191)
- Properly execute rescue section when an include task fails in all loop iterations (https://github.com/ansible/ansible/issues/23161)
- Properly send a skipped message when a list in a ``loop`` is empty and comes from a template (https://github.com/ansible/ansible/issues/77934)
- Support colons in jinja2 template override values (https://github.com/ansible/ansible/pull/77495).
- ``ansible-galaxy`` - remove extra server api call during dependency resolution for requirements and dependencies that are already satisfied (https://github.com/ansible/ansible/issues/77443).
- `ansible-config init -f vars` will now use shorthand format
- action plugins now pass cannonical info to modules instead of 'temporary' info from play_context
- ansible - Exclude Python 2.6 from Python interpreter discovery.
- ansible-config dump - Only display plugin type headers when plugin options are changed if --only-changed is specified.
- ansible-config limit shorthand format to assigned values
- ansible-configi init should now skip internal reserved config entries
- ansible-connection - decrypt vaulted parameters before sending over the socket, as vault secrets are not available on the other side.
- ansible-console - Renamed the first argument of ``ConsoleCLI.default`` from ``arg`` to ``line`` to match the first argument of the same method on the base class ``Cmd``.
- ansible-console commands now all have a help entry.
- ansible-console fixed to load modules via fqcn, short names and handle redirects.
- ansible-console now shows installed collection modules.
- ansible-doc - fix listing plugins.
- ansible-doc will not add 'website for' in ":ref:" substitutions as it made them confusing.
- ansible-doc will not again warn and skip when missing docs, always show the doc file (for edit on github) and match legacy plugins.
- ansible-doc will not traceback when legacy plugins don't have docs nor adjacent file with docs
- ansible-doc will now also display until as an 'implicit' templating keyword.
- ansible-doc will now not display version_added_collection under same conditions it does not display version_added.
- ansible-galaxy - Fix detection of ``--role-file`` in arguments for implicit role invocation (https://github.com/ansible/ansible/issues/78204)
- ansible-galaxy - Fix exit codes for role search and delete (https://github.com/ansible/ansible/issues/78516)
- ansible-galaxy - Fix loading boolean server options so False doesn't become a truthy string (https://github.com/ansible/ansible/issues/77416).
- ansible-galaxy - Fix reinitializing the whole collection directory with ``ansible-galaxy collection init ns.coll --force``. Now directories and files that are not included in the collection skeleton will be removed.
- ansible-galaxy - Fix unhandled traceback if a role's dependencies in meta/main.yml or meta/requirements.yml are not lists.
- ansible-galaxy - do not require mandatory keys in the ``galaxy.yml`` of source collections when listing them (https://github.com/ansible/ansible/issues/70180).
- ansible-galaxy - fix installing collections that have dependencies in the metadata set to null instead of an empty dictionary (https://github.com/ansible/ansible/issues/77560).
- ansible-galaxy - fix listing collections that contains metadata but the namespace or name are not strings.
- ansible-galaxy - fix missing meta/runtime.yml in default galaxy skeleton used for ansible-galaxy collection init
- ansible-galaxy - fix setting the cache for paginated responses from Galaxy NG/AH (https://github.com/ansible/ansible/issues/77911).
- ansible-galaxy - handle unsupported versions of resolvelib gracefully.
- ansible-galaxy --ignore-certs now has proper precedence over configuration
- ansible-test - Add ``wheel < 0.38.0`` constraint for Python 3.6 and earlier.
- ansible-test - Allow disabled, unsupported, unstable and destructive integration test targets to be selected using their respective prefixes.
- ansible-test - Allow unstable tests to run when targeted changes are made and the ``--allow-unstable-changed`` option is specified (resolves https://github.com/ansible/ansible/issues/74213).
- ansible-test - Always remove containers after failing to create/run them. This avoids leaving behind created containers when using podman.
- ansible-test - Correctly detect when running as the ``root`` user (UID 0) on the origin host. The result of the detection was incorrectly being inverted.
- ansible-test - Delegation for commands which generate output for programmatic consumption no longer redirect all output to stdout. The affected commands and options are ``shell``, ``sanity --lint``, ``sanity --list-tests``, ``integration --list-targets``, ``coverage analyze``
- ansible-test - Delegation now properly handles arguments given after ``--`` on the command line.
- ansible-test - Don't fail if network cannot be disconnected (https://github.com/ansible/ansible/pull/77472)
- ansible-test - Fix bootstrapping of Python 3.9 on Ubuntu 20.04 remotes.
- ansible-test - Fix broken documentation link for ``aws`` test plugin error messages.
- ansible-test - Fix change detection for ansible-test's own integration tests.
- ansible-test - Fix internal validation of remote completion configuration.
- ansible-test - Fix skipping of tests marked ``needs/python`` on the origin host.
- ansible-test - Fix skipping of tests marked ``needs/root`` on the origin host.
- ansible-test - Prevent ``--target-`` prefixed options for the ``shell`` command from being combined with legacy environment options.
- ansible-test - Sanity test output with the ``--lint`` option is no longer mixed in with bootstrapping output.
- ansible-test - Subprocesses are now isolated from the stdin, stdout and stderr of ansible-test. This avoids issues with subprocesses tampering with the file descriptors, such as SSH making them non-blocking. As a result of this change, subprocess output from unit and integration tests on stderr now go to stdout.
- ansible-test - Subprocesses no longer have access to the TTY ansible-test is connected to, if any. This maintains consistent behavior between local testing and CI systems, which typically do not provide a TTY. Tests which require a TTY should use pexpect or another mechanism to create a PTY.
- ansible-test - Temporary executables are now verified as executable after creation. Without this check, path injected scripts may not be found, typically on systems with ``/tmp`` mounted using the "noexec" option. This can manifest as a missing Python interpreter, or use of the wrong Python interpreter, as well as other error conditions.
- ansible-test - Test configuration for collections is now parsed only once, prior to delegation. Fixes issue: https://github.com/ansible/ansible/issues/78334
- ansible-test - Test containers are now run with the ``--tmpfs`` option for ``/tmp``, ``/run`` and ``/run/lock``. This allows use of containers built without the ``VOLUME`` instruction. Additionally, containers with those volumes defined no longer create anonymous volumes for them. This avoids leaving behind volumes on the container host after the container is stopped and deleted.
- ansible-test - The ``shell`` command no longer redirects all output to stdout when running a provided command. Any command output written to stderr will be mixed with the stderr output from ansible-test.
- ansible-test - The ``shell`` command no longer requests a TTY when using delegation unless an interactive shell is being used. An interactive shell is the default behavior when no command is given to pass to the shell.
- ansible-test - Update the ``pylint`` sanity test requirements to resolve crashes on Python 3.11. (https://github.com/ansible/ansible/issues/78882)
- ansible-test - Update the ``pylint`` sanity test to use version 2.15.4.
- ansible-test - Update the ``pylint`` sanity test to use version 2.15.5.
- ansible-test - ansible-doc sanity test - Correctly determine the fully-qualified collection name for plugins in subdirectories, resolving https://github.com/ansible/ansible/issues/78490.
- ansible-test - validate-modules - Documentation-only modules, used for documenting actions, are now allowed to have docstrings (https://github.com/ansible/ansible/issues/77972).
- ansible-test compile sanity test - do not crash if a column could not be determined for an error (https://github.com/ansible/ansible/pull/77465).
- apt - Fix module failure when a package is not installed and only_upgrade=True. Skip that package and check the remaining requested packages for upgrades. (https://github.com/ansible/ansible/issues/78762)
- apt - don't actually update the cache in check mode with update_cache=true.
- apt - don't mark existing packages as manually installed in check mode (https://github.com/ansible/ansible/issues/66413).
- apt - fix package selection to include /etc/apt/preferences(.d) (https://github.com/ansible/ansible/issues/77969)
- apt module now correctly handles virtual packages.
- apt module should not traceback on invalid type given as package. issue 78663.
- arg_spec - Fix incorrect ``no_log`` warning when a parameter alias is used (https://github.com/ansible/ansible/pull/77576)
- callback plugins - do not crash when ``exception`` passed from a module is not a string (https://github.com/ansible/ansible/issues/75726, https://github.com/ansible/ansible/pull/77781).
- cli now emits clearer error on no hosts selected
- config, ensure that pulling values from configmanager are templated if possible.
- display itself should be single source of 'verbosity' level to the engine.
- dnf - Condense a few internal boolean returns.
- dnf - The ``nobest`` option now also works for ``state=latest``.
- dnf - The ``skip_broken`` option is now used in installs (https://github.com/ansible/ansible/issues/73072).
- dnf - fix output parsing on systems with ``LANGUAGE`` set to a language other than English (https://github.com/ansible/ansible/issues/78193)
- facts - fix IP address discovery for specific interface names (https://github.com/ansible/ansible/issues/77792).
- facts - fix processor facts on AIX: correctly detect number of cores and threads, turn ``processor`` into a list (https://github.com/ansible/ansible/pull/78223).
- fetch_file - Ensure we only use the filename when calculating a tempfile, and do not incude the query string (https://github.com/ansible/ansible/issues/29680)
- fetch_file - properly split files with multiple file extensions (https://github.com/ansible/ansible/pull/75257)
- file - setting attributes of symbolic links or files that are hard linked no longer fails when the link target is unspecified (https://github.com/ansible/ansible/issues/76142).
- file backed cache plugins now handle concurrent access by making atomic updates to the files.
- git module fix docs and proper use of ssh wrapper script and GIT_SSH_COMMAND depending on version.
- handlers - fix an issue where the ``flush_handlers`` meta task could not be used with FQCN: ``ansible.builtin.meta`` (https://github.com/ansible/ansible/issues/79023)
- if a config setting prevents running ansible it should at least show it's "origin".
- include module - add docs url to include deprecation message (https://github.com/ansible/ansible/issues/76684).
- items2dict - Handle error if an item is not a dictionary or is missing the required keys (https://github.com/ansible/ansible/issues/70337).
- keyword inheritance - Ensure that we do not squash keywords in validate (https://github.com/ansible/ansible/issues/79021)
- known_hosts - do not return changed status when a non-existing key is removed (https://github.com/ansible/ansible/issues/78598)
- local facts - if a local fact in the facts directory cannot be stated, store an error message as the fact value and emit a warning just as if just as if the facts execution has failed. The stat can fail e.g. on dangling symlinks.
- lookup plugin - catch KeyError when lookup returns dictionary (https://github.com/ansible/ansible/pull/77789).
- module_utils - Make distro.id() report newer versions of OpenSuSE (at least >=15) also report as ``opensuse``. They report themselves as ``opensuse-leap``.
- module_utils.service - daemonize - Avoid modifying the list of file descriptors while iterating over it.
- null_representation config entry changed to 'raw' as it must allow 'none/null' and empty string.
- omit on keywords was resetting to default value, ignoring inheritance.
- paramiko - Add a new option to allow paramiko >= 2.9 to easily work with all devices now that rsa-sha2 support was added to paramiko, which prevented communication with numerous platforms. (https://github.com/ansible/ansible/issues/76737)
- paramiko - Add back support for ``ssh_args``, ``ssh_common_args``, and ``ssh_extra_args`` for parsing the ``ProxyCommand`` (https://github.com/ansible/ansible/issues/78750)
- password lookup does not ignore k=v arguments anymore.
- pause module will now report proper 'echo' vs always being true.
- pip - fix cases where resolution of pip Python module fails when importlib.util has not already been imported
- plugin loader - Sort results when fuzzy matching plugin names (https://github.com/ansible/ansible/issues/77966).
- plugin loader will now load config data for plugin by name instead of by file to avoid issues with the same file being loaded under different names (fqcn + short name).
- plugin loader, fix detection for existing configuration before initializing for a plugin
- plugin loader, now when skipping a plugin due to an abstract method error we provide that in 'verbose' mode instead of totally obscuring the error. The current implementation assumed only the base classes would trigger this and failed to consider 'in development' plugins.
- prevent lusermod from using group name instead of group id (https://github.com/ansible/ansible/pull/77914)
- prevent type annotation shim failures from causing runtime failures (https://github.com/ansible/ansible/pull/77860)
- psrp connection now handles default to inventory_hostname correctly.
- roles, fixed issue with roles loading paths not contained in the role itself when using the `_from` options.
- service_facts - Use python re to parse service output instead of grep (https://github.com/ansible/ansible/issues/78541)
- setup - Adds a default value to ``lvm_facts`` when lvm or lvm2 is not installed on linux (https://github.com/ansible/ansible/issues/17393)
- shell plugins now give a more user friendly error when fed the wrong type of data.
- template module/lookup - fix ``convert_data`` option that was effectively always set to True for Jinja macros (https://github.com/ansible/ansible/issues/78141)
- unarchive - if unzip is available but zipinfo is not, use unzip -Z instead of zipinfo (https://github.com/ansible/ansible/issues/76959).
- uri - properly use uri parameter use_proxy (https://github.com/ansible/ansible/issues/58632)
- uri module - failed status when Authentication Bearer used with netrc, because Basic authentication was by default. Fix now allows to ignore netrc by changing use_netrc=False (https://github.com/ansible/ansible/issues/74397).
- urls - Guard imports of ``urllib3`` by catching ``Exception`` instead of ``ImportError`` to prevent exceptions in the import process of optional dependencies from preventing use of ``urls.py`` (https://github.com/ansible/ansible/issues/78648)
- user - Fix error "Permission denied" in user module while generating SSH keys (https://github.com/ansible/ansible/issues/78017).
- user - fix creating a local user if the user group already exists (https://github.com/ansible/ansible/pull/75042)
- user module - Replace uses of the deprecated ``spwd`` python module with ctypes (https://github.com/ansible/ansible/pull/78050)
- validate-modules - fix validating version_added for new options.
- variablemanager, more efficient read of vars files
- vault secrets file now executes in the correct context when it is a symlink (not resolved to canonical file).
- wait_for - Read file and perform comparisons using bytes to avoid decode errors (https://github.com/ansible/ansible/issues/78214)
- winrm - Ensure ``kinit`` is run with the same ``PATH`` env var as the Ansible process
- winrm connection now handles default to inventory_hostname correctly.
- yaml inventory plugin - fix the error message for non-string hostnames (https://github.com/ansible/ansible/issues/77519).
- yum - fix traceback when ``releasever`` is specified with ``latest`` (https://github.com/ansible/ansible/issues/78058)

amazon.aws
~~~~~~~~~~

- Include ``PSF-license.txt`` file for ``plugins/module_utils/_version.py``.
- aws_account_attribute lookup plugin - fix linting errors in documentation data (https://github.com/ansible-collections/amazon.aws/pull/701).
- aws_ec2 - address a regression introduced in 4.1.0 (https://github.com/ansible-collections/amazon.aws/pull/862) that cause the presnse of duplicated hosts in the inventory.
- aws_ec2 - ensure the correct number of hosts are returned when tags as hostnames are used (https://github.com/ansible-collections/amazon.aws/pull/862).
- aws_ec2 inventory plugin - fix linting errors in documentation data (https://github.com/ansible-collections/amazon.aws/pull/701).
- aws_rds inventory plugin - fix linting errors in documentation data (https://github.com/ansible-collections/amazon.aws/pull/701).
- aws_resource_actions callback plugin - fix linting errors in documentation data (https://github.com/ansible-collections/amazon.aws/pull/701).
- aws_secret lookup plugin - fix linting errors in documentation data (https://github.com/ansible-collections/amazon.aws/pull/701).
- aws_service_ip_ranges lookup plugin - fix linting errors in documentation data (https://github.com/ansible-collections/amazon.aws/pull/701).
- aws_ssm - Fix environment variables for client configuration (e.g., AWS_PROFILE, AWS_ACCESS_KEY_ID) (https://github.com/ansible-collections/amazon.aws/pull/837).
- aws_ssm lookup plugin - fix linting errors in documentation data (https://github.com/ansible-collections/amazon.aws/pull/701).
- cloudtrail - Fix key error TagList to TagsList (https://github.com/ansible-collections/amazon.aws/issues/1088).
- ec2_group - fix uncaught exception when running with ``--diff`` and ``--check`` to create a new security group (https://github.com/ansible-collections/amazon.aws/issues/440).
- ec2_instance - Add a condition to handle default ```instance_type``` value for fix breaking on instance creation with launch template (https://github.com/ansible-collections/amazon.aws/pull/587).
- ec2_instance - Only show the deprecation warning for the default value of ``instance_type`` when ``count`` or ``exact_count`` are specified (https://github.com//issues/980).
- ec2_instance - ec2_instance module broken in Python 3.8 - dict keys modified during iteration (https://github.com/ansible-collections/amazon.aws/issues/709).
- ec2_instance - fixes ``Invalid type for parameter TagSpecifications, value None`` error when tags aren't specified (https://github.com/ansible-collections/amazon.aws/issues/1148).
- ec2_instance - raise an error when missing permission to stop instance when ``state`` is set to ``rebooted``` (https://github.com/ansible-collections/amazon.aws/pull/671).
- ec2_metadata_facts - fix ``'NoneType' object is not callable`` exception when using Ansible 2.13+ (https://github.com/ansible-collections/amazon.aws/issues/942).
- ec2_metadata_facts - fixed ``AttributeError`` (https://github.com/ansible-collections/amazon.aws/issues/1134).
- ec2_vpc_igw - use gateway_id rather than filters to paginate if possible to fix 'NoneType' object is not subscriptable error (https://github.com/ansible-collections/amazon.aws/pull/766).
- ec2_vpc_net - fix a bug where CIDR configuration would be updated in check mode (https://github.com/ansible/ansible/issues/62678).
- ec2_vpc_net - fix a bug where the module would get stuck if DNS options were updated in check mode (https://github.com/ansible/ansible/issues/62677).
- ec2_vpc_net_info - fix KeyError (https://github.com/ansible-collections/amazon.aws/pull/1109).
- ec2_vpc_net_info - remove hardcoded ``ClassicLinkEnabled`` parameter when request for ``ClassicLinkDnsSupported`` failed (https://github.com/ansible-collections/amazon.aws/pull/1109).
- elb_application_lb - fix ``KeyError`` when balancing across two Target Groups (https://github.com/ansible-collections/community.aws/issues/1089).
- elb_classic_lb - fix ``'NoneType' object has no attribute`` bug when creating a new ELB in check mode with a health check (https://github.com/ansible-collections/amazon.aws/pull/915).
- elb_classic_lb - fix ``'NoneType' object has no attribute`` bug when creating a new ELB using security group names (https://github.com/ansible-collections/amazon.aws/issues/914).
- elb_classic_lb - modify the return value of _format_listeners method to resolve a failure creating https listeners (https://github.com/ansible-collections/amazon.aws/pull/860).
- module.utils.rds - Add waiter for promoting read replica to fix idempotency issue (https://github.com/ansible-collections/amazon.aws/pull/714).
- module.utils.rds - Catch InvalidDBSecurityGroupStateFault when modifying a db instance (https://github.com/ansible-collections/amazon.aws/pull/776).
- module.utils.s3 - Update validate_bucket_name minimum length to 3 (https://github.com/ansible-collections/amazon.aws/pull/802).
- module_utils.transformations - ensure that ``map_complex_type`` still returns transformed items if items exists that are not in the type_map (https://github.com/ansible-collections/amazon.aws/pull/1163).
- module_utils/botocore - fix ``object has no attribute 'fail'`` error in error handling (https://github.com/ansible-collections/amazon.aws/pull/1045).
- module_utils/cloud - Fix ``ValueError: ansible_collections.amazon.aws.plugins.module_utils.core.__spec__ is None`` error on Ansible 2.9 (https://github.com/ansible-collections/amazon.aws/issues/1083).
- module_utils/elbv2 - fixes ``KeyError`` when using ``UseExistingClientSecret`` rather than ``ClientSecret`` (https://github.com/ansible-collections/amazon.aws/pull/940).
- module_utils/elbv2 - improvements to idempotency when comparing listeners (https://github.com/ansible-collections/community.aws/issues/604).
- s3_object - also use ``ignore_nonexistent_bucket`` when listing a bucket (https://github.com/ansible-collections/amazon.aws/issues/966).
- s3_object - be more defensive when checking the results of ``s3.get_bucket_ownership_controls`` (https://github.com/ansible-collections/amazon.aws/issues/1115).

ansible.netcommon
~~~~~~~~~~~~~~~~~

- Fix a small number of potential use-before-assignment issues.
- Fix to set connection plugin options correctly.
- libssh - Removed the wording "Tech preview". From version 3.0.0 the default if installed.
- libssh - add ssh_args, ssh_common_args, and ssh_extra_args options. These options are exclusively for collecting proxy information from as an alternative to the proxy_command option.
- libssh - check for minimum ansible-pylibssh version before using password_prompt option. (https://github.com/ansible-collections/ansible.netcommon/pull/467)
- restconf_get - fix direction of XML deserialization when ``output == 'xml'``

ansible.utils
~~~~~~~~~~~~~

- Fix filters to only raise AnsibleFilterError exceptions (https://github.com/ansible-collections/ansible.utils/issues/209).
- ipsubnet - interacting with large subnets could cause performance constraints. the result would be the system would appear to hang while it built out a list of all possible subnets or stepped through all possible subnets one at a time. when sending a prefix that is a supernet of the passed in network the behavior wasn't consistent. this now returns an AnsibleFilterError in that scenario across all python releases. (https://github.com/ansible-collections/ansible.utils/issues/132)

ansible.windows
~~~~~~~~~~~~~~~

- setup - Ignore PATH entries with invalid roots when trying to find ``facter.exe`` - https://github.com/ansible-collections/ansible.windows/issues/397
- setup - Ignore invalid ``PATH`` entries when trying to find ``facter.exe`` - https://github.com/ansible-collections/ansible.windows/issues/364
- win_acl_inheritance - Fix broken pathqualifier when using a UNC path - (https://github.com/ansible-collections/ansible.windows/issues/408).
- win_certificate_store - Allow to reimport a certificate + key if the private key was not present the first time you imported it
- win_command - Fix bug that stopped win_command from finding executables that are located more than once in ``PATH`` - https://github.com/ansible-collections/ansible.windows/issues/403
- win_copy - Fix error message when failing to find ``src`` on the controller filesystem
- win_find - Fix up share checks when the share contains the ``'`` character
- win_package - Skip ``msix`` provider on older hosts that do not implement the required cmdlets
- win_powershell - Do not attempt to serialize ETS properties of primitive types - https://github.com/ansible-collections/ansible.windows/issues/360
- win_powershell - Make sure ``target_object`` on an error record uses the ``depth`` object when serializing the value - https://github.com/ansible-collections/ansible.windows/issues/375
- win_setup - Fix custom facts that return false are missing - https://github.com/ansible-collections/ansible.windows/issues/430
- win_stat - Fix up share checks when the share contains the ``'`` character
- win_updates - Fix broken call when logging a warning about updates with errors - https://github.com/ansible-collections/ansible.windows/issues/411
- win_updates - Handle running with a temp profile path that is deleted between reboots - https://github.com/ansible-collections/ansible.windows/issues/417
- win_updates - Try to display warnings on search suceeded with warnings - https://github.com/ansible-collections/ansible.windows/issues/366

check_point.mgmt
~~~~~~~~~~~~~~~~

- cp_mgmt_access_rule - support for relative positioning for rulebase with more than 50 rules (https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection/issues/69)
- cp_mgmt_administrator - specifying the administartor's permissions profile now works for both SMC and MDS (https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection/issues/83)
- meta/runtime.yml - update value of minimum ansible version and remove redirect (https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection/issues/84)

chocolatey.chocolatey
~~~~~~~~~~~~~~~~~~~~~

- win_chocolatey - Collection version 1.3.0 fails to install packages with explicit version number and state set to present.

cisco.aci
~~~~~~~~~

- Fix HTTP status returned by aci_rest (#279)
- Fix aci_aep_to_epg absent issue to only delete the correct binding (#263)
- Fix aci_interface_description query interface filtering (#238)
- Fix aci_interface_selector_to_switch_policy_leaf_profile error when querying interface_selector without specifying a switch policy leaf profile (#318)
- Fix aci_rest output_path issues when content is not JSON

cisco.asa
~~~~~~~~~

- Fix service-object port range rendering
- Fixes asa_ogs port object range issue and duplicate service cmd (https://github.com/ansible-collections/cisco.asa/issues/165, https://github.com/ansible-collections/cisco.asa/issues/166).
- Unit TC for svc src/dst port range

cisco.dnac
~~~~~~~~~~

- Update dnacentersdk requirement from 2.5.0 to 2.5.4
- application_sets - delete function fixed.
- applications - delete function fixed.
- business_sda_hostonboarding_ssid_ippool - create function added.
- event_subscription - delete function fixed.
- file_info - Improve the module documentation.
- sda_fabric_authentication_profile - delete function fixed.
- sda_fabric_border_device - delete function fixed.
- sda_fabric_control_plane_device - delete function fixed.
- sda_fabric_edge_device - Change required payload parameter to deviceManagementIpAddress
- sda_fabric_edge_device - delete function fixed.
- sda_virtual_network - delete function fixed.
- transit_peer_network - Added status check
- wireless_profile - create function fixed.

cisco.ios
~~~~~~~~~

- cliconf - get_device_info now tries to exit config mode if necessary before requesting device info. (https://github.com/ansible-collections/cisco.ios/pull/654)
- facts - fix operstatus having a white space after value.
- ios_acl - Handle ACL config parsing when match/matches are present.
- ios_acls - Fix regex to parse echo-reply command.
- ios_bgp_global - Parse local_as commands correctly.
- ios_interfaces - Fix enable attribute.
- ios_interfaces - Parse interface shutdown config correctly.
- ios_lag_interfaces - Fix commands generation on action states.
- ios_lag_interfaces - Module functionality not restricted to GigabitEthernet.
- ios_logging_global - Parse monitor and buffered config correctly.
- ios_ntp - Handle regex matching server attributes gracefully.
- ios_route_maps - Fix route maps failing on config parsed with tailing space.
- ios_snmp_server - Fix parsers for views and host + acl doc
- ios_snmp_server - Render group and views commands correctly when having common names.
- ios_static_routes - fix vrf for ipv6 static routes (https://github.com/ansible-collections/cisco.ios/issues/660).
- l2_interfaces - vlan_tag options fix.
- prefix_lists - fix prefix list facts generation to handle empty configuration correctly.
- snmp_server - add envmon options for traps.

cisco.iosxr
~~~~~~~~~~~

- Fix commit confirmed for IOSXR versions with atomic commands.
- Fix commit confirmed to render proper command without timeout.
- Fixing TenGigE Interface recognition for resource modules. (https://github.com/ansible-collections/cisco.iosxr/issues/270)
- Fixing model/version facts gathering (https://github.com/ansible-collections/cisco.iosxr/issues/282)
- Remove irrelevant warning from facts.
- `iosxr_ping` - Fix regex to parse ping failure correctly.
- iosxr_bgp_neighbor_address_family - Added alias to render as_overrride under vrfs as as_override.
- requirements: remove google dependency

cisco.ise
~~~~~~~~~

- A new method to compare changes for specific cases has been added.
- An error was corrected in galaxy publication
- Cisco ISE credentials can now be exported and used as env vars.
- Fixed ISE version 3.1.1 to 3.1_Patch_1 which is the correct version name.
- aci_settings - A validation has been added to the update method.
- allowed_protocols - A validation has been added to the update method.
- anc_policy - A validation has been added to the update method.
- authorization_profile - A validation has been added to the update method.
- byod_portal - A validation has been added to the update method.
- certificate_profile - A validation has been added to the update method.
- downloadable_acl - A validation has been added to the update method.
- downloadable_acl - update EXAMPLES block of module documentation.
- egress_matrix_cell - A validation has been added to the update method.
- endpoint - A validation has been added to the update method.
- endpoint - an unnecessary parameter name has been removed because it is automatically generated by the api.
- endpoint_group - A validation has been added to the update method.
- external_radius_server - A validation has been added to the update method.
- filter_policy - A validation has been added to the update method.
- filter_policy - removed the required id when it is a post method.
- guest_smtp_notification_settings - A validation has been added to the update method.
- guest_smtp_notification_settings - removed the required id when it is a post method.
- guest_ssid - A validation has been added to the update method.
- guest_type - A validation has been added to the update method.
- guest_user - A validation has been added to the update method.
- hotspot_portal - A validation has been added to the update method.
- id_store_sequence - A validation has been added to the update method.
- identity_group - A validation has been added to the update method.
- licensing_eval_license_info - corrected the response
- mnt_athentication_status_info - the following variable was renamed from rec_ord_s to records.
- mnt_athentication_status_info - the following variable was renamed from sec_ond_s to seconds.
- mnt_authentication_status_info - the following variable was renamed from rec_ord_s to records.
- mnt_authentication_status_info - the following variable was renamed from sec_ond_s to seconds.
- mnt_session_disconnect_info - the following variable was renamed from dis_con_nec_tty_pe to disconnect_type.
- mnt_session_disconnect_info - the following variable was renamed from end_poi_nti_p to endpoint_ip.
- mnt_session_disconnect_info - the following variable was renamed from psn_nam_e to psn_name.
- mnt_session_reauthentication_info - the following variable was renamed from end_poi_ntm_ac to endpoint_mac.
- mnt_session_reauthentication_info - the following variable was renamed from psn_nam_e to psn_name.
- mnt_session_reauthentication_info - the following variable was renamed from rea_uth_typ_e to reauth_type.
- my_device_portal - A validation has been added to the update method.
- native_supplicant_profile - A validation has been added to the update method.
- network_access_network_condition -  fixed a request body of the post and put method.
- network_access_network_condition - Updated description of deviceGroupList.
- network_device - A validation has been added to the update method.
- network_device_group - A validation has been added to the update method.
- node_primary_to_standalone - fixed ansible changed response
- node_secondary_to_primary - fixed ansible changed response
- node_services_profiler_probe_config - Used a new method to compare changes.
- node_standalone_to_primary - fixed ansible changed response
- personas_update_roles_services - fixed ansible status msg.
- personas_utils - Warning message removed.
- portal_global_setting - A validation has been added to the update method.
- portal_theme - A validation has been added to the update method.
- radius_server_sequence - A validation has been added to the update method.
- repository - Fixed a bug, now repositoryName and name are used to perform the search.
- repository_files_info - Fixed a bug that did not make the get call.
- rest_id_store - A validation has been added to the update method.
- self_registered_portal - A validation has been added to the update method.
- sg_acl - A validation has been added to the update method.
- sg_mapping - A validation has been added to the update method.
- sg_mapping_group - A validation has been added to the update method.
- sg_to_vn_to_vlan - A validation has been added to the update method.
- sgt - A validation has been added to the update method.
- sgt - Updated the fields required for creation.
- sgt - added new validation when updating a stg auto generated.
- sponsor_group - A validation has been added to the update method.
- sponsor_portal - A validation has been added to the update method.
- sponsored_guest_portal - A validation has been added to the update method.
- sxp_connections - A validation has been added to the update method.
- sxp_connections - removed the required id when it is a post method.
- sxp_local_bindings - A validation has been added to the update method.
- sxp_vpns - removed the required id when it is a post method.
- system_certificate - a missing parameter was added allowWildcardDelete
- tacacs_command_sets - A validation has been added to the update method.
- tacacs_external_servers - A validation has been added to the update method.
- tacacs_profile - A validation has been added to the update method.
- tacacs_server_sequence - A validation has been added to the update method.

cisco.meraki
~~~~~~~~~~~~

- meraki_mx_static_route - Add support for gateway_vlan_id otherwise requests could error
- meraki_switchport - Setting VLAN to 0 on trunk port clears the VLAN.

cisco.mso
~~~~~~~~~

- Fix time issue when host running ansible is in a different timezone then NDO
- Remove mso_guide from notes

cisco.nxos
~~~~~~~~~~

- Fix issue with modules related to OSPF interfaces failing when the target NXOS device has subinterfaces.
- `nxos_facts` - Fixes parsing of module info json data when TABLE_modinfo entry is a list (https://github.com/ansible-collections/cisco.nxos/issues/559).
- `nxos_file_copy` - Skip `vrf` when running against MDS switches (https://github.com/ansible-collections/cisco.nxos/issues/508).
- `nxos_interfaces` - Enable all virtual interfaces with `enabled` set to True (https://github.com/ansible-collections/cisco.nxos/issues/335).
- `nxos_ntp_global` - Ensure idempotence for aliased keys (https://github.com/ansible-collections/cisco.nxos/issues/484).
- `nxos_snmp_server` - Fix typo for traps link cisco-xcvr-mon-status-chg.
- `nxos_telemetry` - Allow destination-group & sensor-group id to be strings.
- `nxos_telemetry` - Allow sensor-group paths to be generated without additional properties.

cloud.common
~~~~~~~~~~~~

- Ensure we don't shutdown the server when we've still got some ongoing tasks (https://github.com/ansible-collections/cloud.common/pull/109).

community.aws
~~~~~~~~~~~~~

- aws_api_gateway_domain - added the ``aws_api_gateway_domain`` module to the aws module_defaults group (https://github.com/ansible-collections/community.aws/pull/1283).
- aws_codebuild - fix bug where the result may be spuriously flagged as ``changed`` when multiple tags were set on the project (https://github.com/ansible-collections/community.aws/pull/1221).
- aws_config_aggregator - Fix ``KeyError`` when updating existing aggregator (https://github.com/ansible-collections/community.aws/pull/645).
- aws_config_aggregator - Fix idempotency when ``account_sources`` parameter is not specified (https://github.com/ansible-collections/community.aws/pull/645).
- aws_ssm - pull S3 bucket region for session generated for file transfer during playbooks (https://github.com/ansible-collections/community.aws/issues/1190).
- aws_ssm connection plugin - fix linting errors in documentation data (https://github.com/ansible-collections/community.aws/pull/965).
- aws_ssm_parameter_store - fix exception when description was set without value (https://github.com/ansible-collections/community.aws/pull/1241).
- aws_ssm_parameter_store - fixed bug where module wasn't consistently idempotent (https://github.com/ansible-collections/community.aws/pull/1309).
- cloudfront_response_headers_policy - added the ``cloudfront_response_headers_policy`` module to the aws module_defaults group (https://github.com/ansible-collections/community.aws/pull/1283).
- don't require ``db_instance_identifier`` on state = present (https://github.com/ansible-collections/community.aws/pull/1078).
- dynamodb_table - fix an issue when creating secondary indexes with global_keys_only (https://github.com/ansible-collections/community.aws/issues/967).
- ec2_asg - Change the default value of ``purge_tags`` to ``false``. Restores previous behaviour (https://github.com/ansible-collections/community.aws/pull/1064).
- ec2_placement_group - Handle a potential race creation during the creation of a new Placement Group (https://github.com/ansible-collections/community.aws/pull/1477).
- ec2_vpc_peer - fix idempotency when requester/accepter is reversed (https://github.com/ansible-collections/community.aws/issues/580).
- ec2_vpc_vpn - fix exception when no tags are passed in check mode (https://github.com/ansible-collections/community.aws/pull/1242).
- ecs_service - add missing change detect of ``health_check_grace_period_seconds`` parameter (https://github.com/ansible-collections/community.aws/pull/1145).
- ecs_service - fix broken change detect of ``health_check_grace_period_seconds`` parameter when not specified (https://github.com/ansible-collections/community.aws/pull/1212).
- ecs_service - fix broken compare of ``task_definition`` that results always in a changed task (https://github.com/ansible-collections/community.aws/pull/1145).
- ecs_service - fix validation for ``placement_constraints``. It's possible to use ``distinctInstance`` placement constraint now (https://github.com/ansible-collections/community.aws/issues/1058)
- ecs_service - fixes KeyError for ``deployment_controller`` parameter (https://github.com/ansible-collections/community.aws/pull/1393).
- ecs_service - use default cluster name of ``default`` when not input (https://github.com/ansible-collections/community.aws/pull/1212).
- ecs_task - dont require ``cluster`` and use name of ``default`` when not input (https://github.com/ansible-collections/community.aws/pull/1212).
- ecs_taskdefinition - fix broken change detect of ``launch_type`` parameter (https://github.com/ansible-collections/community.aws/pull/1145).
- elb_application_lb_info - Up default value AWS backoff retries for paginated calls. (https://github.com/ansible-collections/community.aws/pull/1113).
- elb_network_lb - fixes bug where ``ip_address_type`` in return value was not updated (https://github.com/ansible-collections/community.aws/pull/1365).
- elb_target_group_info - Up default value AWS backoff retries for paginated calls. (https://github.com/ansible-collections/community.aws/pull/1113).
- execute_lamba - add waiter for function_updated (https://github.com/ansible-collections/community.aws/pull/1108).
- execute_lambda - add waiter for function_updated (https://github.com/ansible-collections/community.aws/pull/1108).
- execute_lambda - fix check mode and update RETURN documentation (https://github.com/ansible-collections/community.aws/pull/1115).
- iam_policy - require one of ``policy_document`` and ``policy_json`` when state is present to prevent MalformedPolicyDocumentException from being thrown (https://github.com/ansible-collections/community.aws/pull/1093).
- iam_user - don't delete user login profile on check mode (https://github.com/ansible-collections/community.aws/pull/1059).
- iam_user_info - gracefully handle when no users are found (https://github.com/ansible-collections/community.aws/pull/1059).
- kms_key_info - handle access denied errors more liberally (https://github.com/ansible-collections/community.aws/issues/206).
- lambda - fix bug where tag keys were mangled in the return values (https://github.com/ansible-collections/community.aws/pull/1202).
- lambda - fix bug where the lambda module was modifying tags in check mode (https://github.com/ansible-collections/community.aws/pull/1202).
- lambda - fix check mode on creation (https://github.com/ansible-collections/community.aws/pull/1108).
- lambda_info - fix bug that forces query=config when getting info for all lambdas. Now, if function name is specified, query will default to all.  This may have a performance impact when querying a large number of lambdas. If function name is not specified, query will default to config (https://github.com/ansible-collections/community.aws/pull/1152).
- rds_cluster - fixes bug where specifiying an rds cluster parameter group raises a `KeyError` (https://github.com/ansible-collections/community.aws/pull/1417).
- rds_instance - fix bugs associated with restoring db instance from snapshot (https://github.com/ansible-collections/community.aws/pull/1081).
- rds_instance - fix check_mode and idempotency issues and added integration tests for all tests in suite (https://github.com/ansible-collections/community.aws/pull/1002).
- rds_instance_snapshot - don't require ``db_instance_identifier`` on state = present (https://github.com/ansible-collections/community.aws/pull/1078).
- route53 - fixes bug preventing creating a DNS record with a weight of zero (https://github.com/ansible-collections/community.aws/issues/1378)
- route53_info - fix ``max_items`` parameter when used with non-paginated commands (https://github.com/ansible-collections/community.aws/issues/1383).
- s3_lifecycle - add support of value *0* for ``transition_days`` (https://github.com/ansible-collections/community.aws/pull/1077).
- s3_lifecycle - check that configuration is complete before returning (https://github.com/ansible-collections/community.aws/pull/1085).
- s3_lifecycle - fix bug when deleting rules with an empty prefix (https://github.com/ansible-collections/community.aws/pull/1398).
- s3_sync - fix etag generation when running in FIPS mode (https://github.com/ansible-collections/community.aws/issues/757).
- sns_topic - fix bug which prevented the module being used in GovCloud (https://github.com/ansible-collections/community.aws/issues/836).
- wafv2_ip_set - fix bug where incorrect changed state was returned when only changing the description (https://github.com/ansible-collections/community.aws/pull/1211).
- wafv2_rule_group - fix bug where description of resource state was missing when rule groups were updated (https://github.com/ansible-collections/community.aws/pull/1210).
- wafv2_rule_group - fix bug where updating just the description did not update the changed state (https://github.com/ansible-collections/community.aws/pull/1210).
- wafv2_web_acl - consistently return web ACL info as described in module documentation (https://github.com/ansible-collections/community.aws/pull/1216).
- wafv2_web_acl - fix ``changed`` status when description not specified (https://github.com/ansible-collections/community.aws/pull/1216).

community.crypto
~~~~~~~~~~~~~~~~

- Include ``Apache-2.0.txt`` file for ``plugins/module_utils/crypto/_obj2txt.py`` and ``plugins/module_utils/crypto/_objects_data.py``.
- acme_* modules - improve feedback when importing ``cryptography`` does not work (https://github.com/ansible-collections/community.crypto/issues/518, https://github.com/ansible-collections/community.crypto/pull/519).
- openssl_csr - the module no longer crashes with 'permitted_subtrees/excluded_subtrees must be a non-empty list or None' if only one of ``name_constraints_permitted`` and ``name_constraints_excluded`` is provided (https://github.com/ansible-collections/community.crypto/issues/481).
- openssl_pkcs12 - when using the pyOpenSSL backend, do not crash when trying to read non-existing other certificates (https://github.com/ansible-collections/community.crypto/issues/486, https://github.com/ansible-collections/community.crypto/pull/487).
- openssl_privatekey_pipe - ensure compatibility with newer versions of ansible-core (https://github.com/ansible-collections/community.crypto/pull/515).
- x509_crl - do not crash when signing CRL with Ed25519 or Ed448 keys (https://github.com/ansible-collections/community.crypto/issues/473, https://github.com/ansible-collections/community.crypto/pull/474).

community.digitalocean
~~~~~~~~~~~~~~~~~~~~~~

- digital_ocean_droplet - fix regression in droplet deletion where ``name`` and ``unique_name`` (set to true) are required and ``id`` alone is insufficient (though ``id`` is sufficient to uniquely identify a droplet for deletion). (https://github.com/ansible-collections/community.digitalocean/issues/260)
- digital_ocean_droplet - fix regression where droplet info (for example networking) doesn't update when waiting during creation unless ``unique_name`` is set to true (https://github.com/ansible-collections/community.digitalocean/issues/220).
- digital_ocean_droplet - if the JSON response lacks a key and the associated variable is set to ``None``, then don't treat that variable like a ``dict`` and call ``get()`` on it without first testing it (https://github.com/ansible-collections/community.digitalocean/issues/272).

community.dns
~~~~~~~~~~~~~

- Update Public Suffix List.
- wait_for_txt - also retrieve IPv6 addresses of nameservers. Prevents failures with IPv6 only nameservers (https://github.com/ansible-collections/community.dns/issues/120, https://github.com/ansible-collections/community.dns/pull/121).

community.docker
~~~~~~~~~~~~~~~~

- Docker SDK for Python based modules and plugins - if the API version is specified as an option, use that one to validate API version requirements of module/plugin options instead of the latest API version supported by the Docker daemon. This also avoids one unnecessary API call per module/plugin (https://github.com/ansible-collections/community.docker/pull/389).
- docker_container - fix handling of ``env_file`` (https://github.com/ansible-collections/community.docker/issues/451, https://github.com/ansible-collections/community.docker/pull/452).
- docker_image - fix build argument handling (https://github.com/ansible-collections/community.docker/issues/455, https://github.com/ansible-collections/community.docker/pull/456).
- docker_image - when composing the build context, trim trailing whitespace from ``.dockerignore`` entries. This is only a change relative to older community.docker 3.0.0 pre-releases or with respect to Docker SDK for Python < 6.0.0. Docker SDK for Python 6.0.0 will also include this change (https://github.com/ansible-collections/community.docker/pull/434).
- docker_plugin - fix crash when handling plugin options (https://github.com/ansible-collections/community.docker/issues/446, https://github.com/ansible-collections/community.docker/pull/447).
- docker_stack - fix broken string formatting when reporting error in case ``compose`` was containing invalid values (https://github.com/ansible-collections/community.docker/pull/448).
- modules and plugins communicating directly with the Docker daemon - do not create a subshell for SSH connections when using ``use_ssh_client=true``. This is only a change relative to older community.docker 3.0.0 pre-releases or with respect to Docker SDK for Python < 6.0.0. Docker SDK for Python 6.0.0 will also include this change (https://github.com/ansible-collections/community.docker/pull/434).
- modules and plugins communicating directly with the Docker daemon - fix ``ProxyCommand`` handling for SSH connections when not using ``use_ssh_client=true``. This is only a change relative to older community.docker 3.0.0 pre-releases or with respect to Docker SDK for Python < 6.0.0. Docker SDK for Python 6.0.0 will also include this change (https://github.com/ansible-collections/community.docker/pull/434).
- modules and plugins communicating directly with the Docker daemon - fix parsing of IPv6 addresses with a port in ``docker_host``. This is only a change relative to older community.docker 3.0.0 pre-releases or with respect to Docker SDK for Python < 6.0.0. Docker SDK for Python 6.0.0 will also include this change (https://github.com/ansible-collections/community.docker/pull/434).
- modules and plugins communicating directly with the Docker daemon - prevent crash when TLS is used (https://github.com/ansible-collections/community.docker/pull/432).

community.general
~~~~~~~~~~~~~~~~~

- Include ``PSF-license.txt`` file for ``plugins/module_utils/_mount.py``.
- Include ``simplified_bsd.txt`` license file for various module utils, the ``lxca_common`` docs fragment, and the ``utm_utils`` unit tests.
- alternatives - do not set the priority if the priority was not set by the user (https://github.com/ansible-collections/community.general/pull/4810).
- alternatives - only pass subcommands when they are specified as module arguments (https://github.com/ansible-collections/community.general/issues/4803, https://github.com/ansible-collections/community.general/issues/4804, https://github.com/ansible-collections/community.general/pull/4836).
- alternatives - when ``subcommands`` is specified, ``link`` must be given for every subcommand. This was already mentioned in the documentation, but not enforced by the code (https://github.com/ansible-collections/community.general/pull/4836).
- apache2_mod_proxy - avoid crash when reporting inability to parse balancer_member_page HTML caused by using an undefined variable in the error message (https://github.com/ansible-collections/community.general/pull/5111).
- archive - avoid crash when ``lzma`` is not present and ``format`` is not ``xz`` (https://github.com/ansible-collections/community.general/pull/5393).
- cmd_runner module utils - fix bug caused by using the ``command`` variable instead of ``self.command`` when looking for binary path (https://github.com/ansible-collections/community.general/pull/4903).
- consul - fixed bug introduced in PR 4590 (https://github.com/ansible-collections/community.general/issues/4680).
- credstash lookup plugin - pass plugin options to credstash for all terms, not just for the first (https://github.com/ansible-collections/community.general/pull/5440).
- dependent lookup plugin - avoid warning on deprecated parameter for ``Templar.template()`` (https://github.com/ansible-collections/community.general/pull/5543).
- dig lookup plugin - add option to return empty result without empty strings, and return empty list instead of ``NXDOMAIN`` (https://github.com/ansible-collections/community.general/pull/5439, https://github.com/ansible-collections/community.general/issues/5428).
- dig lookup plugin - fix evaluation of falsy values for boolean parameters ``fail_on_error`` and ``retry_servfail`` (https://github.com/ansible-collections/community.general/pull/5129).
- dnsimple_info - correctly report missing library as ``requests`` and not ``another_library`` (https://github.com/ansible-collections/community.general/pull/5111).
- dnstxt lookup plugin - add option to return empty result without empty strings, and return empty list instead of ``NXDOMAIN`` (https://github.com/ansible-collections/community.general/pull/5457, https://github.com/ansible-collections/community.general/issues/5428).
- dsv lookup plugin - do not ignore the ``tld`` parameter (https://github.com/ansible-collections/community.general/pull/4911).
- filesystem - handle ``fatresize --info`` output lines without ``:`` (https://github.com/ansible-collections/community.general/pull/4700).
- filesystem - improve error messages when output cannot be parsed by including newlines in escaped form (https://github.com/ansible-collections/community.general/pull/4700).
- funcd connection plugin - fix signature of ``exec_command`` (https://github.com/ansible-collections/community.general/pull/5111).
- ini_file - minor refactor fixing a python lint error (https://github.com/ansible-collections/community.general/pull/5307).
- iso_create - the module somtimes failed to add folders for Joliet and UDF formats (https://github.com/ansible-collections/community.general/issues/5275).
- jenkins_build - fix the logical flaw when deleting a Jenkins build (https://github.com/ansible-collections/community.general/pull/5514).
- keycloak_realm - fix default groups and roles (https://github.com/ansible-collections/community.general/issues/4241).
- keyring_info - fix the result from the keyring library never getting returned (https://github.com/ansible-collections/community.general/pull/4964).
- ldap_attrs - fix bug which caused a ``Bad search filter`` error. The error was occuring when the ldap attribute value contained special characters such as ``(`` or ``*`` (https://github.com/ansible-collections/community.general/issues/5434, https://github.com/ansible-collections/community.general/pull/5435).
- ldap_attrs - fix ordering issue by ignoring the ``{x}`` prefix on attribute values (https://github.com/ansible-collections/community.general/issues/977, https://github.com/ansible-collections/community.general/pull/5385).
- listen_ports_facts - removed leftover ``EnvironmentError`` . The ``else`` clause had a wrong indentation. The check is now handled in the ``split_pid_name`` function (https://github.com/ansible-collections/community.general/pull/5202).
- locale_gen - fix support for Ubuntu (https://github.com/ansible-collections/community.general/issues/5281).
- lxc_container - the module has been updated to support Python 3 (https://github.com/ansible-collections/community.general/pull/5304).
- lxd connection plugin - fix incorrect ``inventory_hostname`` in ``remote_addr``. This is needed for compatibility with ansible-core 2.13 (https://github.com/ansible-collections/community.general/issues/4886).
- manageiq_alert_profiles - avoid crash when reporting unknown profile caused by trying to return an undefined variable (https://github.com/ansible-collections/community.general/pull/5111).
- nmcli - avoid changed status for most cases with VPN connections (https://github.com/ansible-collections/community.general/pull/5126).
- nmcli - fix error caused by adding undefined module arguments for list options (https://github.com/ansible-collections/community.general/issues/4373, https://github.com/ansible-collections/community.general/pull/4813).
- nmcli - fix error when setting previously unset MAC address, ``gsm.apn`` or ``vpn.data``: current values were being normalized without checking if they might be ``None`` (https://github.com/ansible-collections/community.general/pull/5291).
- nmcli - fix int options idempotence (https://github.com/ansible-collections/community.general/issues/4998).
- nsupdate - compatibility with NS records (https://github.com/ansible-collections/community.general/pull/5112).
- nsupdate - fix silent failures when updating ``NS`` entries from Bind9 managed DNS zones (https://github.com/ansible-collections/community.general/issues/4657).
- one_vm - avoid splitting labels that are ``None`` (https://github.com/ansible-collections/community.general/pull/5489).
- onepassword_raw - add missing parameter to plugin documentation (https://github.com/ansible-collections/community.general/issues/5506).
- opentelemetry callback plugin - support opentelemetry-api 1.13.0 that removed support for ``_time_ns`` (https://github.com/ansible-collections/community.general/pull/5342).
- osx_defaults - no longer expand ``~`` in ``value`` to the user's home directory, or expand environment variables (https://github.com/ansible-collections/community.general/issues/5234, https://github.com/ansible-collections/community.general/pull/5243).
- packet_ip_subnet - fix error reporting in case of invalid CIDR prefix lengths (https://github.com/ansible-collections/community.general/pull/5111).
- pacman - fixed name resolution of URL packages (https://github.com/ansible-collections/community.general/pull/4959).
- passwordstore lookup plugin - fix ``returnall`` for gopass (https://github.com/ansible-collections/community.general/pull/5027).
- passwordstore lookup plugin - fix password store path detection for gopass (https://github.com/ansible-collections/community.general/pull/4955).
- pfexec become plugin - remove superflous quotes preventing exe wrap from working as expected (https://github.com/ansible-collections/community.general/issues/3671, https://github.com/ansible-collections/community.general/pull/3889).
- pip_package_info - remove usage of global variable (https://github.com/ansible-collections/community.general/pull/5111).
- pkgng - fix case when ``pkg`` fails when trying to upgrade all packages (https://github.com/ansible-collections/community.general/issues/5363).
- proxmox - fix error handling when getting VM by name when ``state=absent`` (https://github.com/ansible-collections/community.general/pull/4945).
- proxmox inventory plugin - fix crash when ``enabled=1`` is used in agent config string (https://github.com/ansible-collections/community.general/pull/4910).
- proxmox inventory plugin - fixed extended status detection for qemu (https://github.com/ansible-collections/community.general/pull/4816).
- proxmox_disk - avoid duplicate ``vmid`` reference (https://github.com/ansible-collections/community.general/issues/5492, https://github.com/ansible-collections/community.general/pull/5493).
- proxmox_kvm - fix ``agent`` parameter when boolean value is specified (https://github.com/ansible-collections/community.general/pull/5198).
- proxmox_kvm - fix error handling when getting VM by name when ``state=absent`` (https://github.com/ansible-collections/community.general/pull/4945).
- proxmox_kvm - fix exception when no ``agent`` argument is specified (https://github.com/ansible-collections/community.general/pull/5194).
- proxmox_kvm - fix wrong condition (https://github.com/ansible-collections/community.general/pull/5108).
- proxmox_kvm - replace new condition with proper condition to allow for using ``vmid`` on update (https://github.com/ansible-collections/community.general/pull/5206).
- rax_clb_nodes - fix code to be compatible with Python 3 (https://github.com/ansible-collections/community.general/pull/4933).
- redfish_command - fix the check if a virtual media is unmounted to just check for ``instered= false`` caused by Supermicro hardware that does not clear the ``ImageName`` (https://github.com/ansible-collections/community.general/pull/4839).
- redfish_command - the Supermicro Redfish implementation only supports the ``image_url`` parameter in the underlying API calls to ``VirtualMediaInsert`` and ``VirtualMediaEject``. Any values set (or the defaults) for ``write_protected`` or ``inserted`` will be ignored (https://github.com/ansible-collections/community.general/pull/4839).
- redfish_info - fix to ``GetChassisPower`` to correctly report power information when multiple chassis exist, but not all chassis report power information (https://github.com/ansible-collections/community.general/issues/4901).
- redfish_utils module utils - centralize payload checking when performing modification requests to a Redfish service (https://github.com/ansible-collections/community.general/issues/5210/).
- redhat_subscription - fix unsubscribing on RHEL 9 (https://github.com/ansible-collections/community.general/issues/4741).
- redhat_subscription - make module idempotent when ``pool_ids`` are used (https://github.com/ansible-collections/community.general/issues/5313).
- redis* modules - fix call to ``module.fail_json`` when failing because of missing Python libraries (https://github.com/ansible-collections/community.general/pull/4733).
- slack - fix incorrect channel prefix ``#`` caused by incomplete pattern detection by adding ``G0`` and ``GF`` as channel ID patterns (https://github.com/ansible-collections/community.general/pull/5019).
- slack - fix message update for channels which start with ``CP``. When ``message-id`` was passed it failed for channels which started with ``CP`` because the ``#`` symbol was added before the ``channel_id`` (https://github.com/ansible-collections/community.general/pull/5249).
- snap - allow values in the ``options`` parameter to contain whitespaces (https://github.com/ansible-collections/community.general/pull/5475).
- sudoers - ensure sudoers config files are created with the permissions requested by sudoers (0440) (https://github.com/ansible-collections/community.general/pull/4814).
- sudoers - fix incorrect handling of ``state: absent`` (https://github.com/ansible-collections/community.general/issues/4852).
- tss lookup plugin - adding support for updated Delinea library (https://github.com/DelineaXPM/python-tss-sdk/issues/9, https://github.com/ansible-collections/community.general/pull/5151).
- virtualbox inventory plugin - skip parsing values with keys that have both a value and nested data. Skip parsing values that are nested more than two keys deep (https://github.com/ansible-collections/community.general/issues/5332, https://github.com/ansible-collections/community.general/pull/5348).
- xcc_redfish_command - for compatibility due to Redfish spec changes the virtualMedia resource location changed from Manager to System (https://github.com/ansible-collections/community.general/pull/4682).
- xenserver_facts - fix broken ``AnsibleModule`` call that prevented the module from working at all (https://github.com/ansible-collections/community.general/pull/5383).
- xfconf - fix setting of boolean values (https://github.com/ansible-collections/community.general/issues/4999, https://github.com/ansible-collections/community.general/pull/5007).
- zfs - fix wrong quoting of properties (https://github.com/ansible-collections/community.general/issues/4707, https://github.com/ansible-collections/community.general/pull/4726).

community.grafana
~~~~~~~~~~~~~~~~~

- Add support for more elasticsearch version as datasource (#263)
- Ensure user email/login is url encoded when searching for the user (#264)
- Fix a bug that causes a fatal error when using `url` parameter in `grafana_dashboard` and `grafana_notification_channel` modules.
- Fix a bug that causes an update error when using the `grafana_datasource` module on Grafana >=9.0.0 (https://github.com/ansible-collections/community.grafana/issues/248).

community.hashi_vault
~~~~~~~~~~~~~~~~~~~~~

- Add SPDX license headers to individual files (https://github.com/ansible-collections/community.hashi_vault/pull/282).
- Add missing ``BSD-2-Clause.txt`` file for BSD licensed content (https://github.com/ansible-collections/community.hashi_vault/issues/275).
- Use the correct GPL license for plugin_utils (https://github.com/ansible-collections/community.hashi_vault/issues/276).
- community.hashi_vault plugins - tokens will be cast to a string type before being sent to ``hvac`` to prevent errors in ``requests`` when values are ``AnsibleUnsafe`` (https://github.com/ansible-collections/community.hashi_vault/issues/289).
- connection options - the ``namespace`` connection option will be forced into a string to ensure cmpatibility with recent ``requests`` versions (https://github.com/ansible-collections/community.hashi_vault/issues/309).
- modules - fix a "variable used before assignment" that cannot be reached but causes sanity test failures (https://github.com/ansible-collections/community.hashi_vault/issues/296).

community.libvirt
~~~~~~~~~~~~~~~~~

- virt_net - fix modify function which was not idempotent, depending on whether the network was active. See https://github.com/ansible-collections/community.libvirt/issues/107.
- virt_pool - crashed out if pool didn't contain a target path. Fix allows this not to be set. (https://github.com/ansible-collections/community.libvirt/issues/129).

community.mysql
~~~~~~~~~~~~~~~

- Include ``simplified_bsd.txt`` license file for various module utils.
- mysql_db - Using compression masks errors messages from mysql_dump. By default the fix is inactive to ensure retro-compatibility with system without bash. To activate the fix, use the module option ``pipefail=true`` (https://github.com/ansible-collections/community.mysql/issues/256).
- mysql_query - fix false change reports when ``IF EXISTS/IF NOT EXISTS`` clause is used (https://github.com/ansible-collections/community.mysql/issues/268).
- mysql_replication - when the ``primary_ssl`` argument is set to ``no``, the module will turn off SSL (https://github.com/ansible-collections/community.mysql/issues/393).
- mysql_role - don't add members to a role when creating the role and ``detach_members: true`` is set (https://github.com/ansible-collections/community.mysql/pull/367).
- mysql_role - in some cases (when "SHOW GRANTS" did not use backticks for quotes), no unwanted members were detached from the role (and redundant "GRANT" statements were executed for wanted members). This is fixed by querying the existing role members from the mysql.role_edges (MySQL) or mysql.roles_mapping (MariaDB) tables instead of parsing the "SHOW GRANTS" output (https://github.com/ansible-collections/community.mysql/pull/368).
- mysql_user - fix logic when ``update_password`` is set to ``on_create`` for users using ``plugin*`` arguments (https://github.com/ansible-collections/community.mysql/issues/334). The ``on_create`` sets ``password`` to None for old mysql_native_authentication but not for authentiation methods which uses the ``plugin*`` arguments. This PR changes this so ``on_create`` also exchange ``plugin``, ``plugin_hash_string``, ``plugin_auth_string`` to None in the list of arguments to change
- mysql_user - grant option was revoked accidentally when modifying users. This fix revokes grant option only when privs are setup to do that (https://github.com/ansible-collections/community.mysql/issues/77#issuecomment-1209693807).
- mysql_user, mysql_role - mysql/mariadb recent versions translate 'ALL PRIVILEGES' to a list of specific privileges. That caused a change every time we modified user privileges. This fix compares privs before and after user modification to avoid this infinite change (https://github.com/ansible-collections/community.mysql/issues/77).

community.network
~~~~~~~~~~~~~~~~~

- Collection core functions - use vendored version of ``distutils.version`` instead of the deprecated Python standard library ``distutils``.
- Include ``PSF-license.txt`` file for ``plugins/module_utils/_version.py``.
- Include ``simplified_bsd.txt`` license file for the ``icx`` and ``netvisor`` module utils.
- ce - Modify the bug in the query configuration method (https://github.com/ansible-collections/community.network/pull/56).
- community.network.ce_switchport - fix error causing by ``KeyError:`` ``host`` due to properties aren't used anywhere (https://github.com/ansible-collections/community.network/issues/313)
- exos_config - fix a hang due to an unexpected prompt during save_when (https://github.com/ansible-collections/community.network/pull/110).
- weos4 cliconf plugin - fix linting errors in documentation data (https://github.com/ansible-collections/community.network/pull/368).

community.postgresql
~~~~~~~~~~~~~~~~~~~~

- Include ``simplified_bsd.txt`` license file for various module utils.
- postgresql_info - fix pg version parsing (https://github.com/ansible-collections/community.postgresql/issues/315).
- postgresql_info - make arguments passed to SHOW command properly quoted to prevent the interpreter evaluating them (https://github.com/ansible-collections/community.postgresql/issues/314).
- postgresql_pg_hba - support the connection types ``hostgssenc`` and ``hostnogssenc`` (https://github.com/ansible-collections/community.postgresql/pull/351).
- postgresql_ping - fix pg version parsing (https://github.com/ansible-collections/community.postgresql/issues/315).
- postgresql_privs - add support for alter default privileges grant usage on schemas (https://github.com/ansible-collections/community.postgresql/issues/332).
- postgresql_privs - cannot grant select on objects in all schemas; add the ``not-specified`` value to the ``schema`` parameter to make this possible (https://github.com/ansible-collections/community.postgresql/issues/332).
- postgresql_privs.py - add functionality when the PostgreSQL version is 9.0.0 or greater to incorporate ``ALL x IN SCHEMA`` syntax (https://github.com/ansible-collections/community.postgresql/pull/282). Please see the official documentation for details regarding grants (https://www.postgresql.org/docs/9.0/sql-grant.html).
- postgresql_set - avoid postgres puts extra quotes when passing values containing commas (https://github.com/ansible-collections/community.postgresql/issues/78).
- postgresql_subscription - fix idempotence by casting the ``connparams`` dict variable (https://github.com/ansible-collections/community.postgresql/issues/280).
- postgresql_user - add ``alter user``-statements in the return value ``queries`` (https://github.com/ansible-collections/community.postgresql/issues/307).
- postgresql_user - make the module idempotent when password is scram hashed (https://github.com/ansible-collections/community.postgresql/issues/301).

community.rabbitmq
~~~~~~~~~~~~~~~~~~

- rabbitmq_queue - fixing an issue where a special character in the queue name would result in an API error (https://github.com/ansible-collections/community.rabbitmq/issues/114).
- user module - set supports_check_mode flag to False, as the module does not actually support check mode.

community.routeros
~~~~~~~~~~~~~~~~~~

- Include ``LICENSES/BSD-2-Clause.txt`` file for the ``routeros`` module utils (https://github.com/ansible-collections/community.routeros/pull/101).
- api_modify, api_info - make API path ``ip dhcp-server lease`` support ``server=all`` (https://github.com/ansible-collections/community.routeros/issues/104, https://github.com/ansible-collections/community.routeros/pull/107).
- api_modify, api_info - make API path ``ip dhcp-server network`` support missing options ``boot-file-name``, ``dhcp-option-set``, ``dns-none``, ``domain``, and ``next-server`` (https://github.com/ansible-collections/community.routeros/issues/104, https://github.com/ansible-collections/community.routeros/pull/106).
- api_modify, api_info - make API path ``ip dhcp-server`` support ``script``, and ``ip firewall nat`` support ``in-interface`` and ``in-interface-list`` (https://github.com/ansible-collections/community.routeros/pull/110).

community.sap_libs
~~~~~~~~~~~~~~~~~~

- syp_system_facts - fix a typo in the usage example which lead to an error if it used as supposed.

community.sops
~~~~~~~~~~~~~~

- load_vars - ensure compatibility with newer versions of ansible-core (https://github.com/ansible-collections/community.sops/pull/121).

community.vmware
~~~~~~~~~~~~~~~~

- 2.9.0 wasn't released correctly, some changes are missing from the package. Releasing 2.9.1 to fix this.
- vmware_cfg_backup - Fix a bug that failed the module when port 80 is blocked (https://github.com/ansible-collections/community.vmware/issues/1270).
- vmware_cfg_backup - Fix a bug that failed the restore when port 80 is blocked (https://github.com/ansible-collections/community.vmware/issues/1440).
- vmware_cfg_backup - Fix a possible urlopen error when connecting directly to an ESXi host (https://github.com/ansible-collections/community.vmware/issues/1383).
- vmware_content_deploy_ovf_template - Fixed a bug that ignored `resource_pool` in some cases. (https://github.com/ansible-collections/community.vmware/issues/1290).
- vmware_content_deploy_template - Fixed a bug that ignored `resource_pool` in some cases. (https://github.com/ansible-collections/community.vmware/issues/1290).
- vmware_dvs_portgroup - Fix update of NetFlow Setting (https://github.com/ansible-collections/community.vmware/pull/1443).
- vmware_guest - Fix no fail attribute issue (https://github.com/ansible-collections/community.vmware/issues/1401).
- vmware_guest_disk - Ignore datastores in maintenance mode (https://github.com/ansible-collections/community.vmware/pull/1321).
- vmware_guest_file_operation - Add a new parameter for timeout(https://github.com/ansible-collections/community.vmware/pull/1513).
- vmware_guest_instant_clone - Support FQPN in the folder parameter.
- vmware_guest_network - Fix a typo in the code for SR-IOV NICs (https://github.com/ansible-collections/community.vmware/issues/1317).
- vmware_guest_network - Fix an `AttributeError` when using SR-IOV NICs (https://github.com/ansible-collections/community.vmware/issues/1318).
- vmware_host_facts - Fix a bug that crashes the module when a host is disconnected (https://github.com/ansible-collections/vmware/issues/184).
- vmware_host_vmnic_info - Fix a bug that crashes the module when a host is disconnected (https://github.com/ansible-collections/community.vmware/pull/1337).
- vmware_tag_manager - Fix a performance issue during tag processing (https://github.com/ansible-collections/community.vmware/issues/1503).
- vmware_tag_manager - Fix an issue that causes a failure when changing a single cardinal tag category (https://github.com/ansible-collections/community.vmware/issues/1501).
- vmware_tag_manager - Fix idempotency for state `set` (https://github.com/ansible-collections/community.vmware/issues/1265).
- vmware_vm_info - Fix 'NoneType' object has no attribute 'datastoreUrl' for inaccessible VMs (https://github.com/ansible-collections/community.vmware/issues/1407).
- vmware_vswitch - Fix broken logic of `failback` parameter (https://github.com/ansible-collections/community.vmware/issues/1431).

community.windows
~~~~~~~~~~~~~~~~~

- win_dhcp_lease - call Get-DhcpServerv4Lease once when MAC and IP are defined (https://github.com/ansible-collections/community.windows/pull/427)
- win_dhcp_lease - fix mac address convert (https://github.com/ansible-collections/community.windows/issues/291)
- win_domain_user - Fix broken warning call when failing to get group membership - https://github.com/ansible-collections/community.windows/issues/412
- win_psmodule - Fix bootstrapping PowerShellGet with ``-AcceptLicense`` - https://github.com/ansible-collections/community.windows/issues/424
- win_psmodule - Source PowerShellGet and PackagementManagement from ``repository`` if specified
- win_region - did not allow regional format en-150 (= English(Europe); also referred as en-EU or en-Europe). This fix allows specifying en-150 as regional format (https://github.com/ansible-collections/community.windows/issues/438).
- win_scheduled_task - Fix the Monthly DOW trigger value ``run_on_last_week_of_month`` when ``weeks_of_month`` is also set - https://github.com/ansible-collections/community.windows/issues/414
- win_scoop - Fix idempotency checks with Scoop ``v0.2.3`` and newer.

community.zabbix
~~~~~~~~~~~~~~~~

- zabbix_host - fixed idempotency of the module when hostmacros or snmp interfaces are used
- zabbix_script - fix compatibility with Zabbix <5.4.
- zabbix_script - should no longer fail when description is not set

containers.podman
~~~~~~~~~~~~~~~~~

- connection_podman - Add missing docstring for method that executes the podman commands
- podman_container - Change IpcMode default to shareable
- podman_container - Disable memory idempotency
- podman_container - Fix typo in the documentation
- podman_image - Update `podman_image` to remove image with image id
- podman_load - Loop over image names when multiple images present in archive
- podman_login - Fix idempotency for podman_login
- podman_network - Allow specify podman_network options MTU and VLAN separately
- podman_network - Fix internal networks idempotency
- podman_play - Fix play_kube not working when yaml not installed on target
- podman_play - Pass errors as a string instead of list
- podman_pod - Change network attribute from str to list in pods
- podman_pod - Fix pod network idempotency
- podman_pod - Fix pod tests in CI
- podman_pod - Fix pods list retrieve

dellemc.enterprise_sonic
~~~~~~~~~~~~~~~~~~~~~~~~

- Fixed regression test bugs in multiple modules (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/103).
- Fixed regression test sequencing and other regression test bugs in multiple modules (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/85).
- aaa - Fixed a bug in facts gathering by providing required conditional branching (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/90)
- aaa - Modify regression test sequencing to enable correct testing of the functionality for this module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/78).
- bgp_neighbors - remove string conversion of timer attributes (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/60)
- port_breakout - Fixed a bug in formulation of port breakout REST APIs (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/88).
- sonic - Fix a bug in handling of interface names in standard interface naming mode (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/103).
- sonic_command - Fix bugs in handling of CLI commands involving a prompt and answer sequence (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/76/files).
- users - Fixed a bug in facts gathering (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/90).
- vxlan - update Vxlan test cases to comply with SONiC behavior (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/105).

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- idrac_server_config_profile - Issue(234817) – When an XML format is exported using the SCP, the module breaks while waiting for the job completion.
- ome_application_console_preferences - Issue(224690) - The module does not display a proper error message when an unsupported value is provided for the parameters report_row_limit, email_sender_settings, and metric_collection_settings, and the value is applied on OpenManage Enterprise

f5networks.f5_modules
~~~~~~~~~~~~~~~~~~~~~

- bigip_asm_policy_server_technology - fix issue with naming during discovery
- bigip_asm_policy_signature_set - fix issue with naming during discovery
- bigip_data_group - fixed bug discovered while updating records in internal data group
- bigip_device_info - fixed pagination bug for VLANS data
- bigip_gtm_monitor_bigip - fixed bug related to ip extraction from monitor.
- bigip_gtm_monitor_external - fixed bug related to ip extraction from monitor.
- bigip_gtm_monitor_firepass - fixed bug related to ip extraction from monitor.
- bigip_gtm_monitor_http - fixed bug related to ip extraction from monitor.
- bigip_gtm_monitor_https - fixed bug related to ip extraction from monitor.
- bigip_gtm_monitor_tcp - fixed bug related to ip extraction from monitor.
- bigip_gtm_monitor_tcp_half_open - fixed bug related to ip extraction from monitor.
- bigip_monitor_dns - fixed bug related to ip extraction from monitor.
- bigip_monitor_external - fixed bug related to ip extraction from monitor.
- bigip_monitor_ftp - fixed bug related to ip extraction from monitor.
- bigip_monitor_gateway_icmp - fixed bug related to ip extraction from monitor.
- bigip_monitor_ldap - fixed bug related to ip extraction from monitor.
- bigip_monitor_ldap - fixed bug related to password not set during create
- bigip_monitor_mysql - fixed bug related to ip extraction from monitor.
- bigip_monitor_oracle - fixed bug related to ip extraction from monitor.
- bigip_monitor_smtp - fixed bug related to ip extraction from monitor.
- bigip_monitor_tcp - fixed bug related to ip extraction from monitor.
- bigip_monitor_udp - fixed bug related to ip extraction from monitor.
- bigip_software_install - fixed bug related to idempotency and installation of different version of software
- bigip_software_install - fixed bug related to installing hotfix image on vcmp guest

fortinet.fortios
~~~~~~~~~~~~~~~~

- Fix the Github Issue 187.
- Fix the Github Issue 188 and 189.
- Fix the Github Issue 190.
- Fix the Github Issue 191.
- Fix the error message in the debugging log when using ``access_token``.
- Fix the issue when filtering out parameter with space in the module ``fortios_configuration_fact``.
- Fix typo in the documentation of ``Install FortiOS Galaxy Collection``.

hetzner.hcloud
~~~~~~~~~~~~~~

- dynamic inventory - fix crash when having servers without IPs (flexible networks)
- hcloud_server - When state stopped and server is created, do not start the server
- hcloud_server_info - fix crash when having servers without IPs (flexible networks)
- hcloud_server_network - fixes changed alias_ips by using sorted

infoblox.nios_modules
~~~~~~~~~~~~~~~~~~~~~

- Fix to create TXT record with equals sign `#128 <https://github.com/infobloxopen/infoblox-ansible/pull/128>`_

inspur.sm
~~~~~~~~~

- edit_snmp_trap module modifies input parameter errors in the example.

junipernetworks.junos
~~~~~~~~~~~~~~~~~~~~~

- fixes the nighbors list overwrite issue.

netapp.cloudmanager
~~~~~~~~~~~~~~~~~~~

- na_cloudmanager_connector_gcp - Fix default machine_type value on the GCP connector.
- new meta/execution-environment.yml is failing ansible-builder sanitize step.

netapp.ontap
~~~~~~~~~~~~

- iso8601 filters - fix documentation generation issue.
- na_ontap_autosupport - TypeError on ``ondemand_enabled`` field with ONTAP 9.11.
- na_ontap_autosupport - TypeError on ``support`` field with ONTAP 9.11.
- na_ontap_autosupport - fix idempotency issue on ``state`` field with ONTAP 9.11.
- na_ontap_cifs - fix KeyError on ``unix_symlink`` field when using REST.
- na_ontap_cifs_acl - use ``type`` if present when fetching existing ACL with ZAPI.
- na_ontap_cifs_acl - use ``type`` when deleting unix-user or unix-group from ACL in ZAPI.
- na_ontap_cifs_local_user_set_password - when using ZAPI, do not require cluster admin privileges.
- na_ontap_cluster_config - fix the role to be able to create intercluster LIFs with REST (ipspace is required).
- na_ontap_cluster_config Role - incorrect license was shown - updated to GNU General Public License v3.0
- na_ontap_cluster_peer - report an error if there is an attempt to use the already peered clusters.
- na_ontap_command - do not run command in check_mode (thanks to darksoul42).
- na_ontap_ems_destination - fix idempotency issue when ``type`` value is rest_api.
- na_ontap_firmware_upgrade - when enabled, disruptive_update would always update even when update is not required.
- na_ontap_flexcache - properly use ``origin_cluster`` in GET but not in POST when using REST.
- na_ontap_info - Added vserver in key_fields of net_interface_info.
- na_ontap_interface - FC interfaces - home_node should not be sent as location.home_node.
- na_ontap_interface - FC interfaces - home_port is not supported for ONTAP 9.7 or earlier.
- na_ontap_interface - FC interfaces - scope is not supported.
- na_ontap_interface - FC interfaces - service_policy is not supported.
- na_ontap_interface - enforce requirement for address/netmask for interfaces other than FC.
- na_ontap_interface - fix ``netmask`` not idempotent in REST.
- na_ontap_interface - fix error deleting fc interface if it is enabled in REST.
- na_ontap_interface - fix error where an ``address`` with an IPV6 ip would try to modify each time playbook was run.
- na_ontap_interface - fix idempotency issue for cluster scoped interfaces when using REST.
- na_ontap_interface - fix potential node and uuid issues with LIF migration.
- na_ontap_interface - ignore 'none' when using REST rather than reporting unexpected protocol.
- na_ontap_interface - ignore ``vserver`` when using REST if role is one of 'cluster', 'node-mgmt', 'intercluster', 'cluster-mgmt'.
- na_ontap_interface - improve error message when interface type is required with REST.
- na_ontap_kerberos_realm - fix cannot modify ``comment`` option in ZAPI.
- na_ontap_ldap_client - ``servers`` not accepted when using ZAPI and ``ldap_servers`` not handling a single server properly.
- na_ontap_license - fix intermittent KeyError when adding licenses with REST.
- na_ontap_lun - Added ``lun_modify`` after ``app_modify`` to fix idempotency issue.
- na_ontap_lun - catch ZAPI error on get LUN.
- na_ontap_lun - ignore resize error if no change was required.
- na_ontap_lun - report error if flexvol_name is missing when using ZAPI.
- na_ontap_lun_copy - fix key error on ``source_vserver`` option.
- na_ontap_mcc_mediator - Fix error that would prevent mediator deletion,
- na_ontap_name_service_switch - fix AttributeError 'NoneType' object has no attribute 'get_children' if ``sources`` is '-' in current.
- na_ontap_name_service_switch - fix idempotency issue on ``sources`` option.
- na_ontap_net_subnet - delete fails if ipspace is different than Default.
- na_ontap_net_subnet - fixed ``ipspace`` option ignored in getting net subnet.
- na_ontap_ntp - fixed typeError on ``key_id`` field with ZAPI.
- na_ontap_nvme - fixed ``status_admin`` option is ignored if set to False when creating nvme service in REST.
- na_ontap_nvme - fixed invalid boolean value error for ``status_admin`` when creating nvme service in ZAPI.
- na_ontap_portset - fixed error when trying to remove partial ports from portset if igroups are bound to it.
- na_ontap_portset - fixed idempotency issue when ``ports`` has identical values.
- na_ontap_qtree - fix KeyError on unix_permissions.
- na_ontap_qtree - fix idempotency issue on ``unix_permissions`` option.
- na_ontap_quotas - fix another quota operation is currently in progress issue.
- na_ontap_quotas - fix idempotency issue on ``threshold`` option.
- na_ontap_rest_cli - do not run command in check_mode (thanks to darksoul42).
- na_ontap_rest_info - fixed error where module would fail silently when using ``owning_resouce`` and a non-existent vserver.
- na_ontap_s3_buckets - Module will not fail on create if no ``policy`` is given.
- na_ontap_s3_buckets - Module will set ``enabled`` during create.
- na_ontap_s3_buckets - Module work currently when ``sid`` is a number.
- na_ontap_s3_buckets - fix TypeError if ``conditions`` not present in policy statements.
- na_ontap_s3_buckets - fix options that cannot be modified if not set in creating s3 buckets.
- na_ontap_s3_buckets - updated correct choices in options ``audit_event_selector.access`` and ``audit_event_selector.permission``.
- na_ontap_s3_groups - if `policies` is None module should no longer fail
- na_ontap_security_key_manager - fix KeyError on ``node``.
- na_ontap_service_policy - fixed error in modify by changing resulting json of an existing record in REST.
- na_ontap_service_processor_network - allow manually configuring network if all of ``ip_address``, ``netmask``, ''gateway_ip_address`` set and ``dhcp`` not present in REST.
- na_ontap_service_processor_network - fail module when trying to disable ``dhcp`` and not settting one of ``ip_address``, ``netmask``, ``gateway_ip_address`` different than current.
- na_ontap_service_processor_network - fix ``wait_for_completion`` ignored when trying to enable service processor network interface in ZAPI.
- na_ontap_service_processor_network - fix idempotency issue on ``dhcp`` option in ZAPI.
- na_ontap_service_processor_network - fix setting ``dhcp`` v4 takes more than ``wait_for_completion`` retries.
- na_ontap_snapmirror - fix error in snapmirror restore by changing option ``clean_up_failure`` as optional when using ZAPI.
- na_ontap_snapmirror - fix issues where there was no wait on quiesce before aborting.
- na_ontap_snapmirror - fix issues where there was no wait on the relationship to end transferring.
- na_ontap_snapmirror - fix potential issue when destination is using REST but source is using ZAPI.
- na_ontap_snapmirror - relax check for source when using REST.
- na_ontap_snapmirror - support for SSL certificate authentication for both sides when using ONTAP.
- na_ontap_snapmirror - when using REST with a policy, fix AttributeError - 'str' object has no attribute 'get'.
- na_ontap_snapmirror - when using ZAPI, wait for the relationship to be quiesced before breaking.
- na_ontap_software_update - improve error handling if image file is already present.
- na_ontap_software_update - improve error handling when node is rebooting with REST.
- na_ontap_software_update - now reports changed=False when the package is already present.
- na_ontap_software_update - when using REST with ONTAP 9.9 or later, timeout value is properly set.
- na_ontap_svm - KeyError on CIFS when using REST with ONTAP 9.8 or lower.
- na_ontap_user - enforce that all methods are under a single application.
- na_ontap_user - fix idempotency issue with 9.11 because of new is_ldap_fastbind field.
- na_ontap_user - fix idempotency issue with SSH with second_authentication_method.
- na_ontap_user - is_locked was not properly read with ZAPI, making the module not idempotent.
- na_ontap_user_role - fixed Invalid JSON input. Expecting "privileges" to be an array.
- na_ontap_volume - ``snapdir_access`` is not supported by REST and will currently inform you now if you try to use it with REST.
- na_ontap_volume - ``volume_security_style`` was not modified if other security options were present with ZAPI.
- na_ontap_volume - fix KeyError on ``aggregate_name`` when trying to unencrypt volume in ZAPI.
- na_ontap_volume - fix error when trying to move encrypted volume and ``encrypt`` is True in REST.
- na_ontap_volume - fix error when trying to unencrypt volume in REST.
- na_ontap_volume - fix idempotency issue on ``unix_permissions`` option.
- na_ontap_volume - when deleting a volume, don't report a warning when unmount is successful (error is None).
- na_ontap_volume_efficiency - Missing fields in REST get should return None and not crash module.
- na_ontap_vscan_on_access_policy - fixed options ``filters``, ``file_ext_to_exclude`` and ``paths_to_exclude`` cannot be reset to empty values in ZAPI.
- na_ontap_vserver_create role - add rule index as it is now required.
- na_ontap_zapit - fix failure in precluster mode.
- new meta/execution-environment.yml is failing ansible-builder sanitize step.
- tracing - redact headers and authentication secrets by default.

netapp.storagegrid
~~~~~~~~~~~~~~~~~~

- na_sg_org_container - fix versioning not enabled on initial bucket creation.

netapp_eseries.santricity
~~~~~~~~~~~~~~~~~~~~~~~~~

- na_santricity_mgmt_interface - Fix default required_if state option for na_santricity_mgmt_interface
- netapp_eseries.santricity.nar_santricity_host - Fix default MTU value for NVMe RoCE.

netbox.netbox
~~~~~~~~~~~~~

- Fix idempotency with custom_fields [#839](https://github.com/netbox-community/ansible_modules/pull/839)

ovirt.ovirt
~~~~~~~~~~~

- Fix ovirtvmipsv4 when using attribute (https://github.com/oVirt/ovirt-ansible-collection/pull/596).
- HE - Handle migration to hosts that use systemd-coredump (https://github.com/oVirt/ovirt-ansible-collection/pull/557).
- cluster_upgrade - Fix starting up pinned vms (https://github.com/oVirt/ovirt-ansible-collection/pull/532).
- cluster_upgrade - skip host upgrades without anything to update (https://github.com/oVirt/ovirt-ansible-collection/pull/580).
- filters - Fix ovirtvmipsv4 with attribute and network (https://github.com/oVirt/ovirt-ansible-collection/pull/607).
- filters - Fix ovirtvmipsv4 with filter to list (https://github.com/oVirt/ovirt-ansible-collection/pull/609).
- he - Align role with ansible-lint-6.0 (https://github.com/oVirt/ovirt-ansible-collection/pull/545).
- he-setup - fix static ipv6 ifcfg setup (https://github.com/oVirt/ovirt-ansible-collection/pull/592).
- hosted_engine - Specify fqcn for ovirt_system_option_info (https://github.com/oVirt/ovirt-ansible-collection/pull/536).
- hosted_engine_setup - Detect hosted-engine-ha version using /usr/libexec/platform-python (https://github.com/oVirt/ovirt-ansible-collection/pull/573).
- hosted_engine_setup - Fix "'ansible' ModuleNotFoundError" in Disaster Recovery scripts (https://github.com/oVirt/ovirt-ansible-collection/pull/503).
- hosted_engine_setup - Fix cleanup on el9 (https://github.com/oVirt/ovirt-ansible-collection/pull/533).
- hosted_engine_setup - Use command instead of firewalld module (https://github.com/oVirt/ovirt-ansible-collection/pull/508).
- hosted_engine_setup - fix hosted-engine.conf permissions and ownership (https://github.com/oVirt/ovirt-ansible-collection/pull/569).
- hosted_engine_setup - restore - remove host also based on name (https://github.com/oVirt/ovirt-ansible-collection/pull/567).
- hosted_engine_setup - update ansible version in README (https://github.com/oVirt/ovirt-ansible-collection/pull/571).
- image_template - Remove static (https://github.com/oVirt/ovirt-ansible-collection/pull/537).
- image_template - Remove static no - unsupported in ansible 2.12 (https://github.com/oVirt/ovirt-ansible-collection/pull/341).
- ovirt_host - Fix host wait (https://github.com/oVirt/ovirt-ansible-collection/pull/531).
- ovirt_host - Fix kernel_params elemets type (https://github.com/oVirt/ovirt-ansible-collection/pull/608).
- ovirt_host - Fix restarted wait condition (https://github.com/oVirt/ovirt-ansible-collection/pull/551).
- ovirt_host - Honor activate and reboot_after_installation when they are set to false with reinstalled host state (https://github.com/oVirt/ovirt-ansible-collection/pull/587).
- ovirt_storage_domain - Fix inaccessible exception (https://github.com/oVirt/ovirt-ansible-collection/pull/534).
- ovirt_vm - Fix parsing None arguments (https://github.com/oVirt/ovirt-ansible-collection/pull/486).
- ovirt_vm - check if the snapshot exists (https://github.com/oVirt/ovirt-ansible-collection/pull/525).
- ovirt_vm - check if user inputed graphical protocol (https://github.com/oVirt/ovirt-ansible-collection/pull/542).
- repositories - Add mod_auth_openidc:2.3 and nodejs:14 to dnf modules (https://github.com/oVirt/ovirt-ansible-collection/pull/578).
- repositories - Fix example variable names (https://github.com/oVirt/ovirt-ansible-collection/pull/582).
- repositories - Move fips check to satellite CA install block (https://github.com/oVirt/ovirt-ansible-collection/pull/553).
- repositories - RHV 4.4 SP1 is supported only on RHEL 8.6 EUS (https://github.com/oVirt/ovirt-ansible-collection/pull/576).
- shutdown_env - Align role with ansible-lint-6.0 (https://github.com/oVirt/ovirt-ansible-collection/pull/544).

purestorage.flasharray
~~~~~~~~~~~~~~~~~~~~~~

- purefa_dns - Corrects logic where API responds with an empty list rather than a list with a single empty string in it.
- purefa_ds - Add new parameter `force_bind_password` (default = True) to allow idempotency for module
- purefa_hg - Ensure volume disconnection from a hostgroup is idempotent
- purefa_ntp - Corrects workflow so that the state between desired and current are checked before marking the changed flag to true during an absent run
- purefa_pg - Corredt issue when target for protection group is not correctly amended
- purefa_pg - Ensure deleted protection group can be correctly recovered
- purefa_pg - Fix idempotency issue for protection group targets
- purefa_pgsched - Allow zero as a valid value for appropriate schedule parameters
- purefa_pgsched - Fix issue where 0 was not correctly handled for replication schedule
- purefa_pgsnap - Resolved intermittent error where `latest` snapshot is not complete and can fail. Only select latest completed snapshot to restore from.

purestorage.flashblade
~~~~~~~~~~~~~~~~~~~~~~

- purefb_connect - Resolve connection issues between two FBs that are throttling capable
- purefb_policy - Fix incorrect API call for NFS export policy rule creation

t_systems_mms.icinga_director
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Add exception handling to diff and exist functions (https://github.com/T-Systems-MMS/ansible-collection-icinga-director/pull/176)

theforeman.foreman
~~~~~~~~~~~~~~~~~~

- Properly use FQCN notation when redirecting the old ``foreman_*`` and ``katello_*`` module names. (https://github.com/theforeman/foreman-ansible-modules/issues/1484)
- convert2rhel role - Content views for activation keys (https://bugzilla.redhat.com/2118790)

vmware.vmware_rest
~~~~~~~~~~~~~~~~~~

- vcenter_datacenter - Ensure the idempotency works as expected.

Known Issues
------------

community.routeros
~~~~~~~~~~~~~~~~~~

- The ``community.routeros.command`` module claims to support check mode. Since it cannot judge whether the commands executed modify state or not, this behavior is incorrect. Since this potentially breaks existing playbooks, we will not change this behavior until community.routeros 3.0.0.

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- idrac_user - Issue(192043) The module may error out with the message ``unable to perform the import or export operation because there are pending attribute changes or a configuration job is in progress``. Wait for the job to complete and run the task again.
- ome_application_alerts_smtp - Issue(212310) - The module does not provide a proper error message if the destination_address is more than 255 characters.
- ome_application_alerts_syslog - Issue(215374) - The module does not provide a proper error message if the destination_address is more than 255 characters.
- ome_device_local_access_configuration - Issue(215035) - The module reports ``Successfully updated the local access setting`` if an unsupported value is provided for the parameter timeout_limit. However, this value is not actually applied on OpenManage Enterprise Modular.
- ome_device_local_access_configuration - Issue(217865) - The module does not display a proper error message if an unsupported value is provided for the user_defined and lcd_language parameters.
- ome_device_network_services - Issue(212681) - The module does not provide a proper error message if unsupported values are provided for the parameters- port_number, community_name, max_sessions, max_auth_retries, and idle_timeout.
- ome_device_power_settings - Issue(212679) - The module displays the following message if the value provided for the parameter ``power_cap`` is not within the supported range of 0 to 32767, ``Unable to complete the request because PowerCap does not exist or is not applicable for the resource URI.``
- ome_device_quick_deploy - Issue(216352) - The module does not display a proper error message if an unsupported value is provided for the ipv6_prefix_length and vlan_id parameters.
- ome_smart_fabric_uplink - Issue(186024) - The module does not allow the creation of multiple uplinks of the same name even though it is supported by OpenManage Enterprise Modular. If an uplink is created using the same name as an existing uplink, the existing uplink is modified.

netapp.ontap
~~~~~~~~~~~~

- na_ontap_snapshot - added documentation to use UTC format for ``expiry_time``.

New Plugins
-----------

Connection
~~~~~~~~~~

- ansible.netcommon.grpc - Provides a persistent connection using the gRPC protocol

Filter
~~~~~~

- community.general.counter - Counts hashable elements in a sequence

Lookup
~~~~~~

- community.general.bitwarden - Retrieve secrets from Bitwarden

Test
~~~~

- ansible.builtin.uri - is the string a valid URI
- ansible.builtin.url - is the string a valid URL
- ansible.builtin.urn - is the string a valid URN

New Modules
-----------

amazon.aws
~~~~~~~~~~

- amazon.aws.cloudtrail_info - Gather information about trails in AWS Cloud Trail.
- amazon.aws.cloudwatch_metric_alarm_info - Gather information about the alarms for the specified metric
- amazon.aws.s3_object_info - Gather information about objects in S3

ansible.netcommon
~~~~~~~~~~~~~~~~~

- ansible.netcommon.grpc_config - Fetch configuration/state data from gRPC enabled target hosts.
- ansible.netcommon.grpc_get - Fetch configuration/state data from gRPC enabled target hosts.

check_point.mgmt
~~~~~~~~~~~~~~~~

- check_point.mgmt.cp_mgmt_add_rules_batch - Creates new rules in batch. Use this API to achieve optimum performance when adding more than one rule.
- check_point.mgmt.cp_mgmt_approve_session - Workflow feature - Approve and Publish the session.
- check_point.mgmt.cp_mgmt_check_network_feed - Check if a target can reach or parse a network feed; can work with an existing feed object or with a new one (by providing all relevant feed parameters).
- check_point.mgmt.cp_mgmt_check_threat_ioc_feed - Check if a target can reach or parse a threat IOC feed; can work with an existing feed object or with a new one (by providing all relevant feed parameters).
- check_point.mgmt.cp_mgmt_cluster_members_facts - Retrieve all existing cluster members in domain.
- check_point.mgmt.cp_mgmt_connect_cloud_services - Securely connect the Management Server to Check Point's Infinity Portal. <br>This is a preliminary operation so that the management server can use various Check Point cloud-based security services hosted in the Infinity Portal.
- check_point.mgmt.cp_mgmt_delete_rules_batch - Delete rules in batch from the same layer. Use this API to achieve optimum performance when removing more than one rule.
- check_point.mgmt.cp_mgmt_disconnect_cloud_services - Disconnect the Management Server from Check Point's Infinity Portal.
- check_point.mgmt.cp_mgmt_domain_permissions_profile - Manages domain-permissions-profile objects on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_domain_permissions_profile_facts - Get domain-permissions-profile objects facts on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_get_platform - Get actual platform (Hardware, Version, OS) from gateway, cluster or Check Point host.
- check_point.mgmt.cp_mgmt_idp_administrator_group - Manages idp-administrator-group objects on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_idp_administrator_group_facts - Get idp-administrator-group objects facts on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_idp_to_domain_assignment_facts - Get idp-to-domain-assignment objects facts on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_import_outbound_inspection_certificate - Import Outbound Inspection certificate for HTTPS inspection.
- check_point.mgmt.cp_mgmt_install_lsm_policy - Executes the lsm-install-policy on a given list of targets. Install the LSM policy that defined on the attached LSM profile on the targets devices.
- check_point.mgmt.cp_mgmt_install_lsm_settings - Executes the lsm-install-settings on a given list of targets. Install the provisioning settings that defined on the object on the targets devices.
- check_point.mgmt.cp_mgmt_interoperable_device - Manages interoperable-device objects on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_interoperable_device_facts - Get interoperable-device objects facts on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_lsm_cluster_profile_facts - Get lsm-cluster-profile objects facts on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_lsm_gateway_profile_facts - Get lsm-gateway-profile objects facts on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_lsm_run_script - Executes the lsm-run-script on a given list of targets. Run the given script on the targets devices.
- check_point.mgmt.cp_mgmt_md_permissions_profile - Manages md-permissions-profile objects on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_md_permissions_profile_facts - Get md-permissions-profile objects facts on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_network_feed - Manages network-feed objects on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_network_feed_facts - Get network-feed objects facts on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_objects_facts - Get objects objects facts on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_provisioning_profile_facts - Get provisioning-profile objects facts on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_reject_session - Workflow feature - Return the session to the submitter administrator.
- check_point.mgmt.cp_mgmt_repository_script - Manages repository-script objects on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_repository_script_facts - Get repository-script objects facts on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_reset_sic - Reset Secure Internal Communication (SIC). To complete the reset operation need also to reset the device in the Check Point Configuration Tool (by running cpconfig in Clish or Expert mode). Communication will not be possible until you reset and re-initialize the device properly.
- check_point.mgmt.cp_mgmt_set_global_properties - Edit Global Properties.
- check_point.mgmt.cp_mgmt_set_idp_default_assignment - Set default Identity Provider assignment to be use for Management server administrator access.
- check_point.mgmt.cp_mgmt_set_idp_to_domain_assignment - Set Identity Provider assignment to domain, to allow administrator login to that domain using that identity provider, if there is no Identity Provider assigned to the domain the 'idp-default-assignment' will be used. This command only available  for Multi-Domain server.
- check_point.mgmt.cp_mgmt_set_outbound_inspection_certificate - Create or update a certificate to be used as outbound certificate for HTTPS inspection. <br>The outbound CA certificate will be used by the Gateway to inspect SSL traffic.
- check_point.mgmt.cp_mgmt_set_threat_advanced_settings - Edit Threat Prevention's Blades' Settings.
- check_point.mgmt.cp_mgmt_show_cloud_services - Show the connection status of the Management Server to Check Point's Infinity Portal.
- check_point.mgmt.cp_mgmt_show_global_properties - Retrieve Global Properties.
- check_point.mgmt.cp_mgmt_show_idp_default_assignment - Retrieve default Identity Provider assignment that used for Management server administrator access.
- check_point.mgmt.cp_mgmt_show_outbound_inspection_certificate - Show outbound inspection certificate.
- check_point.mgmt.cp_mgmt_show_servers_and_processes - Shows the status of all processes in the current machine (Multi-Domain Server and all Domain Management / Log Servers). <br>This command is available only on Multi-Domain Server.
- check_point.mgmt.cp_mgmt_show_threat_advanced_settings - Show Threat Prevention's Blades' Settings.
- check_point.mgmt.cp_mgmt_simple_cluster - Manages simple-cluster objects on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_simple_cluster_facts - Get simple-cluster objects facts on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_smtp_server - Manages smtp-server objects on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_smtp_server_facts - Get smtp-server objects facts on Checkpoint over Web Services API
- check_point.mgmt.cp_mgmt_submit_session - Workflow feature - Submit the session for approval.
- check_point.mgmt.cp_mgmt_test_sic_status - Test SIC Status reflects the state of the gateway after it has received the certificate issued by the ICA. If the SIC status is Unknown then there is no connection between the gateway and the Security Management Server. If the SIC status is No Communication, an error message will appear. It may contain specific instructions on how to fix the situation.
- check_point.mgmt.cp_mgmt_update_provisioned_satellites - Executes the update-provisioned-satellites on center gateways of VPN communities.

community.aws
~~~~~~~~~~~~~

- community.aws.accessanalyzer_validate_policy_info - Performs validation of IAM policies
- community.aws.autoscaling_complete_lifecycle_action - Completes the lifecycle action of an instance
- community.aws.aws_api_gateway_domain - Manage AWS API Gateway custom domains
- community.aws.aws_glue_crawler - Manage an AWS Glue crawler
- community.aws.ec2_transit_gateway_vpc_attachment - Create and delete AWS Transit Gateway VPC attachments
- community.aws.ec2_transit_gateway_vpc_attachment_info - describes AWS Transit Gateway VPC attachments
- community.aws.eks_fargate_profile - Manage EKS Fargate Profile
- community.aws.lightsail_static_ip - Manage static IP addresses in AWS Lightsail
- community.aws.networkfirewall - manage AWS Network Firewall firewalls
- community.aws.networkfirewall_info - describe AWS Network Firewall firewalls
- community.aws.networkfirewall_policy - manage AWS Network Firewall policies
- community.aws.networkfirewall_policy_info - describe AWS Network Firewall policies
- community.aws.networkfirewall_rule_group - create, delete and modify AWS Network Firewall rule groups
- community.aws.networkfirewall_rule_group_info - describe AWS Network Firewall rule groups
- community.aws.opensearch - Creates OpenSearch or ElasticSearch domain
- community.aws.opensearch_info - obtain information about one or more OpenSearch or ElasticSearch domain
- community.aws.rds_cluster_snapshot - Manage Amazon RDS snapshots of DB clusters

community.general
~~~~~~~~~~~~~~~~~

- community.general.gconftool2_info - Retrieve GConf configurations
- community.general.iso_customize - Add/remove/change files in ISO file
- community.general.keycloak_user_rolemapping - Allows administration of Keycloak user_rolemapping with the Keycloak API
- community.general.keyring - Set or delete a passphrase using the Operating System's native keyring
- community.general.keyring_info - Get a passphrase using the Operating System's native keyring
- community.general.manageiq_policies_info - Listing of resource policy_profiles in ManageIQ
- community.general.manageiq_tags_info - Retrieve resource tags in ManageIQ
- community.general.pipx_info - Rretrieves information about applications installed with pipx
- community.general.proxmox_disk - Management of a disk of a Qemu(KVM) VM in a Proxmox VE cluster.
- community.general.scaleway_compute_private_network - Scaleway compute - private network management
- community.general.scaleway_container - Scaleway Container management
- community.general.scaleway_container_info - Retrieve information on Scaleway Container
- community.general.scaleway_container_namespace - Scaleway Container namespace management
- community.general.scaleway_container_namespace_info - Retrieve information on Scaleway Container namespace
- community.general.scaleway_container_registry - Scaleway Container registry management module
- community.general.scaleway_container_registry_info - Scaleway Container registry info module
- community.general.scaleway_function - Scaleway Function management
- community.general.scaleway_function_info - Retrieve information on Scaleway Function
- community.general.scaleway_function_namespace - Scaleway Function namespace management
- community.general.scaleway_function_namespace_info - Retrieve information on Scaleway Function namespace
- community.general.wdc_redfish_command - Manages WDC UltraStar Data102 Out-Of-Band controllers using Redfish APIs
- community.general.wdc_redfish_info - Manages WDC UltraStar Data102 Out-Of-Band controllers using Redfish APIs

community.hashi_vault
~~~~~~~~~~~~~~~~~~~~~

- community.hashi_vault.vault_kv2_delete - Delete one or more versions of a secret from HashiCorp Vault's KV version 2 secret store

community.routeros
~~~~~~~~~~~~~~~~~~

- community.routeros.api_info - Retrieve information from API
- community.routeros.api_modify - Modify data at paths with API

community.sap_libs
~~~~~~~~~~~~~~~~~~

- community.sap_libs.sap_pyrfc - Ansible Module for use of SAP PyRFC to execute SAP RFCs (Remote Function Calls) to SAP remote-enabled function modules

community.vmware
~~~~~~~~~~~~~~~~

- community.vmware.vmware_datastore - Configure Datastores
- community.vmware.vmware_host_lockdown_exceptions - Manage Lockdown Mode Exception Users

dellemc.enterprise_sonic
~~~~~~~~~~~~~~~~~~~~~~~~

- dellemc.enterprise_sonic.sonic_ntp - Manage NTP configuration on SONiC.
- dellemc.enterprise_sonic.sonic_prefix_lists - prefix list configuration handling for SONiC
- dellemc.enterprise_sonic.sonic_static_routes - Manage static routes configuration on SONiC

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- dellemc.openmanage.idrac_attributes - Configure the iDRAC attributes
- dellemc.openmanage.idrac_boot - Configure the boot order settings.
- dellemc.openmanage.idrac_certificates - Configure certificates for iDRAC.
- dellemc.openmanage.idrac_virtual_media - Configure the virtual media settings.
- dellemc.openmanage.ome_devices - Perform device-specific operations on target devices

hetzner.hcloud
~~~~~~~~~~~~~~

Hetzner
^^^^^^^

Hcloud
......

- hetzner.hcloud.hcloud_primary_ip - Create and manage cloud Primary IPs on the Hetzner Cloud.

ibm.qradar
~~~~~~~~~~

Private
^^^^^^^

Var.Folders. 0.M716S5Gx1G3D5J1Dw S2W1Ph0000Gn.T.Antsibull-Changelog9Yvlq4Ax.Collections.Ansible Collections.Ibm.Qradar.Plugins.Modules
......................................................................................................................................

- ibm.qradar.qradar_analytics_rules - Qradar Analytics Rules Management resource module
- ibm.qradar.qradar_log_sources_management - Qradar Log Sources Management resource module

netapp.ontap
~~~~~~~~~~~~

- netapp.ontap.na_ontap_bgp_peer_group - NetApp ONTAP module to create, modify or delete bgp peer group.
- netapp.ontap.na_ontap_ems_destination - NetApp ONTAP configuration for EMS event destination
- netapp.ontap.na_ontap_file_security_permissions - NetApp ONTAP NTFS file security permissions
- netapp.ontap.na_ontap_file_security_permissions_acl - NetApp ONTAP file security permissions ACL
- netapp.ontap.na_ontap_local_hosts - NetApp ONTAP local hosts
- netapp.ontap.na_ontap_name_mappings - NetApp ONTAP name mappings
- netapp.ontap.na_ontap_ntp_key - NetApp ONTAP NTP key
- netapp.ontap.na_ontap_s3_groups - NetApp ONTAP S3 groups
- netapp.ontap.na_ontap_s3_policies - NetApp ONTAP S3 Policies
- netapp.ontap.na_ontap_s3_services - NetApp ONTAP S3 services
- netapp.ontap.na_ontap_s3_users - NetApp ONTAP S3 users
- netapp.ontap.na_ontap_security_ssh - NetApp ONTAP security ssh

netapp.storagegrid
~~~~~~~~~~~~~~~~~~

- netapp.storagegrid.na_sg_grid_client_certificate - Manage Client Certificates on StorageGRID.

purestorage.flasharray
~~~~~~~~~~~~~~~~~~~~~~

- purestorage.flasharray.purefa_default_protection - Manage SafeMode default protection for a Pure Storage FlashArray
- purestorage.flasharray.purefa_messages - List FlashArray Alert Messages

purestorage.flashblade
~~~~~~~~~~~~~~~~~~~~~~

- purestorage.flashblade.purefb_messages - List FlashBlade Alert Messages
- purestorage.flashblade.purefb_tz - Configure Pure Storage FlashBlade timezone

splunk.es
~~~~~~~~~

Ansible Collections
^^^^^^^^^^^^^^^^^^^

Splunk.Es.Plugins.Modules
.........................

- splunk.es.splunk_adaptive_response_notable_events - Manage Adaptive Responses notable events resource module
- splunk.es.splunk_correlation_searches - Splunk Enterprise Security Correlation searches resource module
- splunk.es.splunk_data_inputs_monitor - Splunk Data Inputs of type Monitor resource module
- splunk.es.splunk_data_inputs_network - Manage Splunk Data Inputs of type TCP or UDP resource module

theforeman.foreman
~~~~~~~~~~~~~~~~~~

- theforeman.foreman.content_export_info - List pulp3 content exports
- theforeman.foreman.content_export_library - Manage content exports
- theforeman.foreman.content_export_repository - Manage repository content exports
- theforeman.foreman.content_export_version - Manage content view version content exports
- theforeman.foreman.discovery_rule - Manage Host Discovery Rules

vmware.vmware_rest
~~~~~~~~~~~~~~~~~~

- vmware.vmware_rest.vcenter_vmtemplate_libraryitems - Creates a library item in content library from a virtual machine
- vmware.vmware_rest.vcenter_vmtemplate_libraryitems_info - Returns information about a virtual machine template contained in the library item specified by {@param.name templateLibraryItem}

Unchanged Collections
---------------------

- ansible.posix (still version 1.4.0)
- cisco.nso (still version 1.0.3)
- cisco.ucs (still version 1.8.0)
- cloudscale_ch.cloud (still version 2.2.2)
- community.ciscosmb (still version 1.0.5)
- community.fortios (still version 1.0.0)
- community.google (still version 1.0.0)
- community.okd (still version 2.2.0)
- community.proxysql (still version 1.4.0)
- community.sap (still version 1.0.0)
- community.skydive (still version 1.0.0)
- cyberark.pas (still version 1.0.14)
- dellemc.os10 (still version 1.1.1)
- dellemc.os6 (still version 1.0.7)
- dellemc.os9 (still version 1.0.4)
- frr.frr (still version 2.0.0)
- gluster.gluster (still version 1.0.2)
- google.cloud (still version 1.0.2)
- hpe.nimble (still version 1.1.4)
- mellanox.onyx (still version 1.0.0)
- netapp.aws (still version 21.7.0)
- netapp.azure (still version 21.10.0)
- netapp.elementsw (still version 21.7.0)
- netapp.um_info (still version 21.8.0)
- ngine_io.cloudstack (still version 2.2.4)
- ngine_io.exoscale (still version 1.0.0)
- openvswitch.openvswitch (still version 2.1.0)
- sensu.sensu_go (still version 1.13.1)
