========================
Ansible 14 Release Notes
========================

This changelog describes changes since Ansible 13.0.0.

.. contents::
  :depth: 2

v14.0.0a4
=========

.. contents::
  :local:
  :depth: 2

Release Summary
---------------

Release Date: 2026-04-29

`Porting Guide <https://docs.ansible.com/projects/ansible/devel/porting_guides.html>`_

Ansible-core
------------

Ansible 14.0.0a4 contains ansible-core version 2.21.0rc1.
This is a newer version than version 2.21.0b3 contained in the previous Ansible release.

The changes are reported in the combined changelog below.

Changed Collections
-------------------

If not mentioned explicitly, the changes are reported in the combined changelog below.

+--------------------+------------------+------------------+------------------------------------------------------------------------------------------------------------------------------+
| Collection         | Ansible 14.0.0a3 | Ansible 14.0.0a4 | Notes                                                                                                                        |
+====================+==================+==================+==============================================================================================================================+
| azure.azcollection | 3.16.0           | 3.17.0           | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+--------------------+------------------+------------------+------------------------------------------------------------------------------------------------------------------------------+
| community.dns      | 3.5.4            | 4.0.0-b1         |                                                                                                                              |
+--------------------+------------------+------------------+------------------------------------------------------------------------------------------------------------------------------+
| community.proxysql | 1.7.0            | 1.8.0            |                                                                                                                              |
+--------------------+------------------+------------------+------------------------------------------------------------------------------------------------------------------------------+
| grafana.grafana    | 6.0.6            | 6.1.0            |                                                                                                                              |
+--------------------+------------------+------------------+------------------------------------------------------------------------------------------------------------------------------+
| hetzner.hcloud     | 6.8.0            | 6.9.0            |                                                                                                                              |
+--------------------+------------------+------------------+------------------------------------------------------------------------------------------------------------------------------+
| kubernetes.core    | 6.3.0            | 6.4.0            |                                                                                                                              |
+--------------------+------------------+------------------+------------------------------------------------------------------------------------------------------------------------------+

Major Changes
-------------

grafana.grafana
~~~~~~~~~~~~~~~

- Run molecule only when required by @voidquark in https://github.com/grafana/grafana-ansible-collection/pull/441
- migrate stack create/update/delete to stacks-api by @KucicM in https://github.com/grafana/grafana-ansible-collection/pull/494

Minor Changes
-------------

community.dns
~~~~~~~~~~~~~

- Migrate codebase to Python 3 only (https://github.com/ansible-collections/community.dns/pull/319, https://github.com/ansible-collections/community.dns/pull/320, https://github.com/ansible-collections/community.dns/pull/321).

community.proxysql
~~~~~~~~~~~~~~~~~~

- Add PostgreSQL support with the new ``proxysql_pgsql_users``, ``proxysql_pgsql_servers``, ``proxysql_pgsql_hostgroup_attributes``, ``proxysql_pgsql_query_rules``, ``proxysql_pgsql_query_rules_fast_routing``, and ``proxysql_pgsql_replication_hostgroups`` modules.

hetzner.hcloud
~~~~~~~~~~~~~~

- primary_ip - Primary IP support upcoming ``assignee_type`` behavior change.
- server_type_info - Added the Server Type Location ``available`` property to the return values (``hcloud_server_type_info[].locations[].available``).
- server_type_info - Added the Server Type Location ``recommended`` property to the return values (``hcloud_server_type_info[].locations[].recommended``).

kubernetes.core
~~~~~~~~~~~~~~~

- helm_info - Ensure compatibility with Helm v4 (https://github.com/ansible-collections/kubernetes.core/issues/1038).
- helm_plugin - Ensure compatibility with Helm v4 (https://github.com/ansible-collections/kubernetes.core/issues/1038).
- helm_plugin_info - Ensure compatibility with Helm v4 (https://github.com/ansible-collections/kubernetes.core/issues/1038).
- helm_pull - Ensure compatibility with Helm v4 (https://github.com/ansible-collections/kubernetes.core/issues/1038).
- helm_registry_auth - Ensure compatibility with Helm v4 (https://github.com/ansible-collections/kubernetes.core/issues/1038).
- helm_registry_auth - add new option plain_http to allow insecure http connection when running ``helm registry login`` (https://github.com/ansible-collections/kubernetes.core/pull/1090).
- helm_repository - Ensure compatibility with Helm v4 (https://github.com/ansible-collections/kubernetes.core/issues/1038).
- k8s_drain - Add support for ``check_mode`` (https://github.com/ansible-collections/kubernetes.core/pull/1086).
- k8s_drain - Convert module warnings into informational displays when users explicitly request the deletion of unmanaged pods, pods with local storage, or those managed by a ``DaemonSet`` (https://github.com/ansible-collections/kubernetes.core/issues/1037).

Breaking Changes / Porting Guide
--------------------------------

community.dns
~~~~~~~~~~~~~

- Ansible-core versions before 2.17 are no longer supported by the collection. This also means that all Python versions before 3.8 are no longer supported (https://github.com/ansible-collections/community.dns/pull/317).

Deprecated Features
-------------------

hetzner.hcloud
~~~~~~~~~~~~~~

- datacenter_info - The ``hcloud_datacenter_info[].server_types`` return value is deprecated and will be removed after 1 October 2026. Please use the ``hcloud_server_type_info[].locations[].available`` return value instead.

Removed Features (previously deprecated)
----------------------------------------

community.dns
~~~~~~~~~~~~~

- Drop support for dnspython < 2.0.0. All modules and plugins that require dnspython will no longer work with older versions (https://github.com/ansible-collections/community.dns/pull/323).

Bugfixes
--------

Ansible-core
~~~~~~~~~~~~

- git - use the branch configured in ``.gitmodules`` or the remote HEAD instead of hardcoding ``master`` when ``track_submodules=yes`` (https://github.com/ansible/ansible/issues/77691).

community.dns
~~~~~~~~~~~~~

- Update Public Suffix List.
- nameserver_info, nameserver_record_info, wait_for_txt - fix handling of DNSPython ``Nameserver`` objects when default resolver addresses are used (https://github.com/ansible-collections/community.dns/pull/321).

kubernetes.core
~~~~~~~~~~~~~~~

- Helm - Allow taking ownership of existing Kubernetes resources on the first installation of a Helm release. Previously, the ``take_ownership`` parameter was always disabled during the initial install, preventing resource adoption (https://github.com/ansible-collections/kubernetes.core/pull/1034).

New Modules
-----------

community.proxysql
~~~~~~~~~~~~~~~~~~

- community.proxysql.proxysql_pgsql_hostgroup_attributes - Manages PostgreSQL hostgroup attributes using the ProxySQL admin interface
- community.proxysql.proxysql_pgsql_query_rules - Modifies pgsql query rules using the proxysql admin interface
- community.proxysql.proxysql_pgsql_query_rules_fast_routing - Modifies query rules for fast routing policies using the proxysql admin interface
- community.proxysql.proxysql_pgsql_replication_hostgroups - Manages replication hostgroups using the proxysql admin interface
- community.proxysql.proxysql_pgsql_servers - Adds or removes pgsql hosts from proxysql admin interface
- community.proxysql.proxysql_pgsql_users - Adds or removes postgresql users from proxysql admin interface

Unchanged Collections
---------------------

- amazon.aws (still version 11.2.0)
- ansible.netcommon (still version 8.5.0)
- ansible.posix (still version 2.1.0)
- ansible.utils (still version 6.0.2)
- ansible.windows (still version 3.5.0)
- arista.eos (still version 12.0.1)
- check_point.mgmt (still version 6.9.0)
- chocolatey.chocolatey (still version 1.6.0)
- cisco.aci (still version 2.13.0)
- cisco.intersight (still version 2.18.0)
- cisco.ios (still version 11.3.0)
- cisco.iosxr (still version 12.2.1)
- cisco.meraki (still version 2.23.2)
- cisco.mso (still version 2.13.0)
- cisco.nxos (still version 11.1.3)
- cisco.ucs (still version 1.16.0)
- cloudscale_ch.cloud (still version 2.5.3)
- community.aws (still version 11.0.0)
- community.ciscosmb (still version 1.0.11)
- community.clickhouse (still version 2.1.0)
- community.crypto (still version 3.2.0)
- community.docker (still version 5.2.0)
- community.general (still version 12.6.0)
- community.grafana (still version 2.3.0)
- community.hashi_vault (still version 7.1.0)
- community.hrobot (still version 2.7.1)
- community.library_inventory_filtering_v1 (still version 1.1.5)
- community.libvirt (still version 2.2.0)
- community.mongodb (still version 1.7.12)
- community.mysql (still version 4.2.0)
- community.okd (still version 5.0.0)
- community.postgresql (still version 4.2.0)
- community.proxmox (still version 2.0.0-beta1)
- community.rabbitmq (still version 1.6.0)
- community.routeros (still version 3.20.0)
- community.sap_libs (still version 1.7.0)
- community.sops (still version 2.3.0)
- community.vmware (still version 6.2.0)
- community.windows (still version 3.1.0)
- community.zabbix (still version 4.2.0)
- containers.podman (still version 1.19.2)
- cyberark.conjur (still version 1.3.9)
- cyberark.pas (still version 1.0.39)
- dellemc.enterprise_sonic (still version 4.1.0)
- dellemc.openmanage (still version 10.0.2)
- dellemc.powerflex (still version 3.0.0)
- dellemc.unity (still version 2.1.0)
- f5networks.f5_modules (still version 1.39.0)
- fortinet.fortimanager (still version 2.13.0)
- fortinet.fortios (still version 2.5.1)
- google.cloud (still version 1.13.0)
- graphiant.naas (still version 26.3.0)
- hitachivantara.vspone_block (still version 4.7.0)
- hitachivantara.vspone_object (still version 1.1.1)
- ibm.storage_virtualize (still version 3.3.0)
- ieisystem.inmanage (still version 4.0.0)
- infinidat.infinibox (still version 1.6.3)
- infoblox.nios_modules (still version 1.9.0)
- inspur.ispim (still version 2.2.4)
- kaytus.ksmanage (still version 4.0.0)
- kubevirt.core (still version 2.2.4)
- lowlydba.sqlserver (still version 2.8.1)
- microsoft.ad (still version 1.10.0)
- microsoft.iis (still version 1.1.0)
- netapp.cloudmanager (still version 21.24.0)
- netapp.ontap (still version 23.4.0)
- netapp.storagegrid (still version 21.16.0)
- netapp_eseries.santricity (still version 2.0.1)
- netbox.netbox (still version 3.22.0)
- ngine_io.cloudstack (still version 3.0.0)
- openstack.cloud (still version 2.5.0)
- ovirt.ovirt (still version 3.2.2)
- pcg.alpaca_operator (still version 2.2.0)
- purestorage.flasharray (still version 1.42.0)
- purestorage.flashblade (still version 1.24.0)
- ravendb.ravendb (still version 1.0.4)
- splunk.es (still version 6.0.0)
- telekom_mms.icinga_director (still version 2.5.1)
- theforeman.foreman (still version 5.11.0)
- vmware.vmware (still version 2.8.0)
- vmware.vmware_rest (still version 4.10.0)
- vultr.cloud (still version 1.14.0)
- vyos.vyos (still version 6.0.0)
- wti.remote (still version 1.0.11)

v14.0.0a3
=========

.. contents::
  :local:
  :depth: 2

Release Summary
---------------

Release Date: 2026-04-21

`Porting Guide <https://docs.ansible.com/projects/ansible/devel/porting_guides.html>`_

Ansible-core
------------

Ansible 14.0.0a3 contains ansible-core version 2.21.0b3.
This is a newer version than version 2.21.0b2 contained in the previous Ansible release.

The changes are reported in the combined changelog below.

Changed Collections
-------------------

If not mentioned explicitly, the changes are reported in the combined changelog below.

+-----------------------------+------------------+------------------+-------+
| Collection                  | Ansible 14.0.0a2 | Ansible 14.0.0a3 | Notes |
+=============================+==================+==================+=======+
| cisco.iosxr                 | 12.1.1           | 12.2.1           |       |
+-----------------------------+------------------+------------------+-------+
| community.crypto            | 3.1.1            | 3.2.0            |       |
+-----------------------------+------------------+------------------+-------+
| community.dns               | 3.5.3            | 3.5.4            |       |
+-----------------------------+------------------+------------------+-------+
| community.general           | 12.5.0           | 12.6.0           |       |
+-----------------------------+------------------+------------------+-------+
| community.routeros          | 3.19.0           | 3.20.0           |       |
+-----------------------------+------------------+------------------+-------+
| community.sops              | 2.3.0-b1         | 2.3.0            |       |
+-----------------------------+------------------+------------------+-------+
| community.zabbix            | 4.1.1            | 4.2.0            |       |
+-----------------------------+------------------+------------------+-------+
| fortinet.fortios            | 2.5.0            | 2.5.1            |       |
+-----------------------------+------------------+------------------+-------+
| hitachivantara.vspone_block | 4.6.1            | 4.7.0            |       |
+-----------------------------+------------------+------------------+-------+
| splunk.es                   | 5.1.0            | 6.0.0            |       |
+-----------------------------+------------------+------------------+-------+
| theforeman.foreman          | 5.10.0           | 5.11.0           |       |
+-----------------------------+------------------+------------------+-------+

Major Changes
-------------

fortinet.fortios
~~~~~~~~~~~~~~~~

- Added a generic `headers` parameter to `fortios_json_generic` to support admin-password confirmation headers and future custom request headers.
- Updated FAQ to illustrate the use of `headers` in `fortios_json_generic` module.
- Updated deprecated import of to_text from ansible.module_utils._text to the supported implementation.

splunk.es
~~~~~~~~~

- Remove dependency on the ``ansible.netcommon`` collection. Utility functions (``remove_empties``, ``dict_diff``, ``dict_merge``) are now bundled locally, and the httpapi plugin inherits directly from ansible-core's ``HttpApiBase``.

Minor Changes
-------------

Ansible-core
~~~~~~~~~~~~

- task results - Python and Powershell modules do not include the ``invocation`` task result key by default. Injection of the ``invocation`` task result key for Python and Powershell modules may be enabled with the var-settable ``INJECT_INVOCATION`` config item. Most callbacks mask ``invocation`` when displaying a task or loop item result.
- worker process - When controller and forked child workers must share a TTY, the ``WORKER_SESSION_ISOLATION`` config item can be set to ``false`` (via variable/config/envvar) to disable forked worker session isolation.

cisco.iosxr
~~~~~~~~~~~

- iosxr_l3_interfaces - Added support for `flow.ipv4.direction` and `flow.ipv6.direction` value `bidirectional`. The module now expands bidirectional flow configuration into both ingress and egress IOS-XR flow monitor commands.

community.crypto
~~~~~~~~~~~~~~~~

- acme_* modules - experimentally support ``dns-account-01`` challenge type according to `acme-dns-account-label draft 02 <https://datatracker.ietf.org/doc/html/draft-ietf-acme-dns-account-label-02>`__. Note that breaking changes to this challenge type can also happen in minor releases until the acme-dns-account-label draft has been finalized as an RFC (https://github.com/ansible-collections/community.crypto/pull/996).
- acme_* modules - experimentally support ``dns-persist-01`` challenge type according to `acme-dns-persist draft 01 <https://www.ietf.org/archive/id/draft-ietf-acme-dns-persist-01.html>`__. Note that breaking changes to this challenge type can also happen in minor releases until the acme-dns-persist draft has been finalized as an RFC (https://github.com/ansible-collections/community.crypto/pull/997).

community.general
~~~~~~~~~~~~~~~~~

- cobbler_sync - minor code cleanup (https://github.com/ansible-collections/community.general/pull/11879).
- cobbler_system - minor code cleanup (https://github.com/ansible-collections/community.general/pull/11879).
- composer - add ``force`` parameter; when ``command=create-project``, the module now checks whether a ``composer.json`` already exists in ``working_dir`` and skips the command if so, making the task idempotent. Set ``force=true`` to always run the command regardless (https://github.com/ansible-collections/community.general/issues/725, https://github.com/ansible-collections/community.general/pull/11689).
- consul_kv - add ``ca_path`` option to specify a CA bundle for HTTPS connections (https://github.com/ansible-collections/community.general/pull/11817).
- consul_kv lookup plugin - add ``ca_path`` option to specify a CA bundle for HTTPS connections (https://github.com/ansible-collections/community.general/issues/2876, https://github.com/ansible-collections/community.general/pull/11817).
- dconf - add support for C(dbus-broker) (https://github.com/ansible-collections/community.general/issues/495, https://github.com/ansible-collections/community.general/pull/11772).
- filesystem - migrate ``LVM.get_fs_size()`` to use ``CmdRunner``, ensuring locale-independent output parsing (https://github.com/ansible-collections/community.general/pull/11888).
- flatpak - add new parameter ``from_url`` to install a flatpak from a ``.flatpakref`` URL (https://github.com/ansible-collections/community.general/issues/4000, https://github.com/ansible-collections/community.general/pull/11748).
- gem - refactor module to use ``CmdRunner`` (https://github.com/ansible-collections/community.general/pull/11733).
- homebrew_services - remove various redundancies including dead state validation, unused return values, and unnecessary locale environment variables (https://github.com/ansible-collections/community.general/pull/11839).
- homebrew_tap - avoid redundant ``brew tap`` calls when processing multiple taps by fetching the tap list once upfront (https://github.com/ansible-collections/community.general/pull/11848).
- ipa_dnsrecord - add ``exclusive`` parameter to allow appending values to existing records without replacing them (https://github.com/ansible-collections/community.general/issues/682, https://github.com/ansible-collections/community.general/pull/11694).
- java_cert - support proxy authentication when ``https_proxy`` environment variable includes credentials (https://github.com/ansible-collections/community.general/issues/4126, https://github.com/ansible-collections/community.general/pull/11753).
- jira - add ``cloud`` option to support Jira Cloud's new search endpoint ``/rest/api/2/search/jql``, since the legacy ``/rest/api/2/search`` endpoint has been removed on Jira Cloud (https://github.com/ansible-collections/community.general/issues/10786, https://github.com/ansible-collections/community.general/pull/11701).
- jira - when ``cloud=true``, user-type fields (``assignee``, ``reporter``, and any listed in the new ``custom_user_fields`` parameter) containing an email address are automatically resolved to Jira Cloud account IDs (https://github.com/ansible-collections/community.general/issues/11734, https://github.com/ansible-collections/community.general/pull/11735).
- logrotate - adds optional ``backup`` parameter to create a backup of the existing configuration file before writing changes (https://github.com/ansible-collections/community.general/pull/11764).
- lvg - migrate to ``CmdRunner``, removing direct ``run_command`` calls and ``run_command_environ_update`` (https://github.com/ansible-collections/community.general/pull/11835).
- lvm_pv - migrate to ``CmdRunner`` using shared runners from ``module_utils/_lvm`` (https://github.com/ansible-collections/community.general/pull/11811).
- lvol - migrate to ``CmdRunner`` (https://github.com/ansible-collections/community.general/pull/11887).
- manageiq module utils - minor code cleanup (https://github.com/ansible-collections/community.general/pull/11879).
- manageiq_alert_profiles - minor code cleanup (https://github.com/ansible-collections/community.general/pull/11879).
- manageiq_alerts - minor code cleanup (https://github.com/ansible-collections/community.general/pull/11879).
- oneview module utils - minor code cleanup (https://github.com/ansible-collections/community.general/pull/11879).
- oneview_san_manager - minor code cleanup (https://github.com/ansible-collections/community.general/pull/11879).
- opendj_backendprop - refactor to use ``CmdRunner`` (https://github.com/ansible-collections/community.general/pull/11728).
- packet_device - minor code cleanup (https://github.com/ansible-collections/community.general/pull/11879).
- packet_ip_subnet - minor code cleanup (https://github.com/ansible-collections/community.general/pull/11879).
- pacman - add ``root``, ``cachedir``, and ``config`` options to support installing packages into an alternative root directory (https://github.com/ansible-collections/community.general/issues/438, https://github.com/ansible-collections/community.general/pull/11681).
- parted - add ``unit_preserve_case`` option to control the case of the ``unit`` field in the return value, fixing the round-trip use case where the returned unit is fed back as input (https://github.com/ansible-collections/community.general/issues/1860, https://github.com/ansible-collections/community.general/pull/11813).
- pubnub_blocks - minor code cleanup (https://github.com/ansible-collections/community.general/pull/11879).
- terraform - minor code cleanup (https://github.com/ansible-collections/community.general/pull/11879).
- xenserver_guest - use ``enumerate()`` instead of manual index variable in ``for`` loop (https://github.com/ansible-collections/community.general/pull/11721).

community.routeros
~~~~~~~~~~~~~~~~~~

- api_info, api_modify - add 46 new parameters to the ``interface ethernet switch port`` path for RouterOS >= 7.15 (CRS1xx/2xx variant) including QoS, mirroring, VLAN, and learning control parameters (https://github.com/ansible-collections/community.routeros/pull/463).
- api_info, api_modify - add ``comment``, ``disabled``, ``independent-learning``, ``qos-group``, ``svl``, and ``switch`` parameters to the ``interface ethernet switch vlan`` path for RouterOS >= 7.15 (CRS1xx/2xx variant) (https://github.com/ansible-collections/community.routeros/pull/463).
- api_info, api_modify - add ``switch-all-ports`` parameter in the ``interface ethernet switch`` path for RouterOS >= 7.22 (https://github.com/ansible-collections/community.routeros/pull/463).
- api_info, api_modify - add support for ``interface ethernet switch acl policer`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/463).
- api_info, api_modify - add support for ``interface ethernet switch acl`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/463).
- api_info, api_modify - add support for ``interface ethernet switch dscp-qos-map`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/463).
- api_info, api_modify - add support for ``interface ethernet switch dscp-to-dscp`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/463).
- api_info, api_modify - add support for ``interface ethernet switch egress-vlan-tag`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/463).
- api_info, api_modify - add support for ``interface ethernet switch egress-vlan-translation`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/463).
- api_info, api_modify - add support for ``interface ethernet switch ingress-port-policer`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/463).
- api_info, api_modify - add support for ``interface ethernet switch ingress-vlan-translation`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/463).
- api_info, api_modify - add support for ``interface ethernet switch mac-based-vlan`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/463).
- api_info, api_modify - add support for ``interface ethernet switch multicast-fdb`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/463).
- api_info, api_modify - add support for ``interface ethernet switch one2one-vlan-switching`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/463).
- api_info, api_modify - add support for ``interface ethernet switch policer-qos-map`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/463).
- api_info, api_modify - add support for ``interface ethernet switch port-leakage`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/463).
- api_info, api_modify - add support for ``interface ethernet switch protocol-based-vlan`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/463).
- api_info, api_modify - add support for ``interface ethernet switch qos-group`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/463).
- api_info, api_modify - add support for ``interface ethernet switch reserved-fdb`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/463).
- api_info, api_modify - add support for ``interface ethernet switch shaper`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/463).
- api_info, api_modify - add support for ``interface ethernet switch stats`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/463).
- api_info, api_modify - add support for ``interface ethernet switch trunk`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/463).
- api_info, api_modify - add support for ``interface ethernet switch unicast-fdb`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/463).
- api_info, api_modify - add support for dynamic hardware detection of CRS1xx/2xx switch variants. Operations on ``interface ethernet switch`` and ``interface ethernet switch port-isolation`` paths now automatically adapt to detected hardware (single-entry vs multi-entry switch chips) (https://github.com/ansible-collections/community.routeros/pull/463).

community.sops
~~~~~~~~~~~~~~

- all modules and plugins - allow retrieving private age keys and private SSH keys through commands with the new ``age_key_cmd`` and ``age_ssh_private_key_cmd`` options (https://github.com/ansible-collections/community.sops/issues/282, https://github.com/ansible-collections/community.sops/pull/286).
- all modules and plugins - allow to configure GCP access with the ``gcp_oauth_access_token`` and ``gcp_kms_client_type`` options (https://github.com/ansible-collections/community.sops/issues/282, https://github.com/ansible-collections/community.sops/pull/286).
- sops_encrypt - support providing HuaweiCloud KMS key IDs with the ``huawei_cloud_kms`` option (https://github.com/ansible-collections/community.sops/issues/282, https://github.com/ansible-collections/community.sops/pull/286).

community.zabbix
~~~~~~~~~~~~~~~~

- host - Added support for vault passwords.
- web role - added support for IPv6
- zabbix frontend and server encryption support: https://www.zabbix.com/documentation/7.4/en/manual/introduction/whatsnew#tls-encryption-between-frontend-and-server & https://www.zabbix.com/documentation/current/en/manual/appendix/install/frontend_encrypt
- zabbix_agent - [WINDOWS] Add INSTALLFOLDER parameter to msi install
- zabbix_agent - add variable for customizing releases url (https://services.zabbix.com/updates/v1)
- zabbix_triggerprototype - use templated and templateid=0 when host_name is given, only templated for template_name
- zabbix_valuemap - add value mappings type suboption which specifies the mapping match type (https://github.com/ansible-collections/community.zabbix/issues/1636).

hitachivantara.vspone_block
~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Added a new "hv_gad_bulk" module for batch creation of multiple GAD pairs on VSP block storage systems.
- Added a new "hv_hg_bulk" module for bulk host group management operations with multithreading support for parallel processing across multiple ports on VSP block storage systems.
- Added a new "hv_hur_bulk" module for bulk creation of HUR pairs on VSP block storage systems.
- Added a new "hv_iscsi_target_bulk" module for bulk iSCSI target management operations with multithreading support for parallel processing across multiple ports on VSP block storage systems.
- Added a new "hv_ldev_bulk" module for bulk operations on logical devices (LDEVs) on VSP block storage systems.
- Added a new "hv_truecopy_bulk" module for bulk creation of TrueCopy pairs in VSP block storage systems.
- Added new "hv_vsp_create_primary_and_secondary_diskless_quorum_disk" role for automated diskless quorum disk creation on VSP block storage systems.
- Added new "hv_vsp_create_primary_and_secondary_quorum_disk" role for automated disk-based quorum disk creation on VSP block storage systems.
- Added new "hv_vsp_gad_pairs_creation" role to automate GAD pairs provisioning on VSP block storage systems.
- Added new "hv_vsp_hur_pairs_creation" role to automate HUR pairs provisioning on VSP block storage systems.
- Added new "hv_vsp_primary_secondary_journal_creation" role for automated journal creation on VSP block storage systems.
- Added support for Ansible core version 2.20.
- Added support for SVOS 10.5.2 for VSP One B24/B26/B28 storage models.
- Added support for SVOS 9.8.7 for VSP 5100/5500 & VSP 5200/5600 storage models.
- Added support for VSP One SDS Block version 1.19.00.
- Added support for input parameter "copy_pace" to the "hv_shadow_image_pair", "hv_gad", "hv_hur", "hv_truecopy", and "hv_journal" modules.
- Added support to "hv_ldev" module to create ldev on a specific resource group.
- Added support to "hv_resource_group" module to add multiple hostgroups by ids of a port to an existing Resource Group by ID.
- Added support to "hv_resource_group" module to add multiple hostgroups by providing a range of IDs of a port to an existing Resource Group by ID.
- Added support to "hv_resource_group" module to remove multiple hostgroups by ids of a port from an existing Resource Group by ID.
- Added support to "hv_resource_group" module to remove multiple hostgroups by providing a range of IDs of a port from an existing Resource Group by ID.
- Added support to "hv_storagepool" module to stop the shrink operation of a storage pool.

splunk.es
~~~~~~~~~

- ci - Add ansible-core version matrix (stable-2.16 through stable-2.21) to the network integration test workflow, aligning with the ITSI pattern. Lower minimum supported ansible-core version to 2.16.0.

theforeman.foreman
~~~~~~~~~~~~~~~~~~

- Support OAuth1 authentication by passing ``oauth1_consumer_key`` and ``oauth1_consumer_secret`` instead of ``username`` and ``password``.
- registration_command - add support for the setup_container_registry_certs parameter (https://github.com/theforeman/foreman-ansible-modules/pull/1966)

Breaking Changes / Porting Guide
--------------------------------

hitachivantara.vspone_block
~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Renamed the following input and output parameters in the "hv_gad" module - "mu_number" to "mirror_unit_number".
- Renamed the following input and output parameters in the "hv_hg" module - "nick_name" to "nickname", "ports" to "port_ids", "port" to "port_id", "should_delete_all_ldevs" to "should_delete_all_volumes".
- Renamed the following input and output parameters in the "hv_hg_facts" module - "nick_name" to "nickname", "ports" to "port_ids", "port" to "port_id".
- Renamed the following input and output parameters in the "hv_hur" module - "mirror_unit_id" to "mirror_unit_number", "primary_journal_pool" to "primary_journal_id", "secondary_journal_pool" to "secondary_journal_id".
- Renamed the following input and output parameters in the "hv_iscsi_target" module - "nick_name" to "nickname", "ports" to "port_ids", "port" to "port_id", "should_delete_all_ldevs" to "should_delete_all_volumes".
- Renamed the following input and output parameters in the "hv_iscsi_target_facts" module - "nick_name" to "nickname", "ports" to "port_ids", "port" to "port_id".
- Renamed the following input and output parameters in the "hv_ldev" module - "parity_group" to "parity_group_id".
- Renamed the following input and output parameters in the "hv_resource_group" module - "start_ldev" to "begin_ldev_id", "end_ldev" to "end_ldev_id", "parity_groups" to "parity_group_ids", "ports" to "port_ids", "port" to "port_id".
- Renamed the following input and output parameters in the "hv_resource_group_facts" module - "ports" to "port_ids", "port" to "port_id".
- Renamed the following input and output parameters in the "hv_sds_block_compute_port" module - "nick_name" to "nickname".
- Renamed the following input and output parameters in the "hv_sds_block_journal" module - "mirror_unit" to "mirror_unit_number".
- Renamed the following input and output parameters in the "hv_sds_block_remote_iscsi_port" module - "remote_ip_address" to "remote_storage_port_ip_address".
- Renamed the following input and output parameters in the "hv_shadow_image_pair" module - "pvol_mu_number" to "mirror_unit_number" , "copy_pace_track_size" to "copy_pace".
- Renamed the following input and output parameters in the "hv_snapshot" module - "mirror_unit_id" to "mirror_unit_number".
- Renamed the following input and output parameters in the "hv_snapshot_group" module - "mirror_unit_id" to "mirror_unit_number".
- Renamed the following input and output parameters in the "hv_storage_port" module - "ports" to "port_ids", "port" to "port_id".
- Renamed the following input and output parameters in the "hv_storage_port_facts" module - "ports" to "port_ids", "port" to "port_id".
- Renamed the following input and output parameters in the "hv_vsp_one_server" module - "nick_name" to "nickname".
- Renamed the following input and output parameters in the "hv_vsp_one_server_facts" module - "nick_name" to "nickname".
- Renamed the following input and output parameters in the "hv_vsp_one_server_hba_facts" module - "nick_name" to "nickname".
- Renamed the following output parameters in the "hv_gad" module - "primary_volume_storage_id" to "primary_volume_storage_serial_number", "secondary_volume_storage_id" to "secondary_volume_storage_serial_number".
- Renamed the following output parameters in the "hv_gad_facts" module - "primary_volume_storage_id" to "primary_volume_storage_serial_number", "secondary_volume_storage_id" to "secondary_volume_storage_serial_number".
- Renamed the following output parameters in the "hv_hur" module - "pvol_status" to "primary_volume_status", "svol_status" to "secondary_volume_status", "storage_serial_number" to "primary_volume_storage_serial_number", "secondary_storage_serial" to "secondary_volume_storage_serial_number".
- Renamed the following output parameters in the "hv_hur_facts" module - "mirror_unit_id" to "mirror_unit_number", "primary_journal_pool" to "primary_journal_id", "secondary_journal_pool" to "secondary_journal_id", "pvol_status" to "primary_volume_status", "svol_status" to "secondary_volume_status", "primary_storage_serial" to "primary_volume_storage_serial_number", "secondary_storage_serial" to "secondary_volume_storage_serial_number".
- Renamed the following output parameters in the "hv_ldev_facts" module - "parity_group" to "parity_group_id".
- Renamed the following output parameters in the "hv_resource_group_facts" module - "start_ldev" to "begin_ldev_id", "end_ldev" to "end_ldev_id", "parity_groups" to "parity_group_ids", "ports" to "port_ids", "port" to "port_id".
- Renamed the following output parameters in the "hv_shadow_image_pair_facts" module - "mirror_unit_id" to "mirror_unit_number", "pvol_host_groups" to "primary_volume_host_groups", "pvol_iscsi_targets" to "primary_volume_iscsi_targets", "pvol_nvm_subsystem_name" to "primary_volume_nvm_subsystem_name", "svol_host_groups" to "secondary_volume_host_groups", "svol_iscsi_targets" to "secondary_volume_iscsi_targets", "svol_nvm_subsystem_name" to "secondary_volume_nvm_subsystem_name".
- Renamed the following output parameters in the "hv_snapshot_facts" module - "mirror_unit_id" to "mirror_unit_number", "pvol_host_groups" to "primary_volume_host_groups", "pvol_iscsi_targets" to "primary_volume_iscsi_targets", "pvol_nvm_subsystem_name" to "primary_volume_nvm_subsystem_name", "svol_host_groups" to "secondary_volume_host_groups", "svol_iscsi_targets" to "secondary_volume_iscsi_targets", "svol_nvm_subsystem_name" to "secondary_volume_nvm_subsystem_name", "pvol_processing_status" to "primary_volume_processing_status", "svol_processing_status" to "secondary_volume_processing_status".
- Renamed the following output parameters in the "hv_snapshot_group_facts" module - "mirror_unit_id" to "mirror_unit_number".
- Renamed the following output parameters in the "hv_truecopy" module - "pvol_status" to "primary_volume_status", "svol_status" to "secondary_volume_status", "storage_serial_number" to "primary_volume_storage_serial_number".
- Renamed the following output parameters in the "hv_truecopy_facts" module - "pvol_status" to "primary_volume_status", "svol_status" to "secondary_volume_status", "storage_serial_number" to "primary_volume_storage_serial_number".
- Renamed the following output parameters in the "hv_vsp_one_volume_facts" module - "start_volume_id" to "begin_volume_id".

Deprecated Features
-------------------

Ansible-core
~~~~~~~~~~~~

- task result - Inferred task failure from a non-zero ``rc`` key and absence of a ``failed`` key will be deprecated in Ansible Core 2.22. Actions and modules must explicitly communicate failure by setting the ``failed`` key, using APIs that do so, or raising an unhandled exception. In future releases, the ``rc`` key will receive no special handling during task result processing.

hitachivantara.vspone_block
~~~~~~~~~~~~~~~~~~~~~~~~~~~

- The old parameter names renamed in this release are retained as aliases for backward compatibility but will be removed in the next major release. Affected parameters across modules are - "start_ldev", "end_ldev", "parity_groups", "ports", "port" (hv_resource_group, hv_resource_group_facts), "ports", "port" (hv_storage_port, hv_storage_port_facts), "mirror_unit" (hv_sds_block_journal), "nick_name", "should_delete_all_ldevs" (hv_hg, hv_iscsi_target), "nick_name" (hv_hg_facts, hv_iscsi_target_facts, hv_sds_block_compute_port, hv_vsp_one_server, hv_vsp_one_server_facts, hv_vsp_one_server_hba_facts), "parity_group" (hv_ldev, hv_ldev_facts), "remote_ip_address" (hv_sds_block_remote_iscsi_port), "start_volume_id" (hv_vsp_one_volume_facts), "mirror_unit_id", "primary_journal_pool", "secondary_journal_pool" (hv_hur), "mirror_unit_id", "pvol_status", "svol_status", "primary_storage_serial", "secondary_storage_serial", "primary_journal_pool", "secondary_journal_pool" (hv_hur_facts), "mu_number" (hv_gad), "pvol_status", "svol_status", "storage_serial_number" (hv_truecopy, hv_truecopy_facts, hv_hur), "secondary_storage_serial" (hv_hur), "primary_volume_storage_id", "secondary_volume_storage_id" (hv_gad, hv_gad_facts), "mirror_unit_id" (hv_snapshot, hv_snapshot_group, hv_snapshot_facts, hv_snapshot_group_facts), "pvol_host_groups", "pvol_iscsi_targets", "pvol_nvm_subsystem_name", "svol_host_groups", "svol_iscsi_targets", "svol_nvm_subsystem_name", "pvol_processing_status", "svol_processing_status" (hv_snapshot_facts), "pvol_mu_number", "copy_pace_track_size" (hv_shadow_image_pair), "mirror_unit_id", "pvol_host_groups", "pvol_iscsi_targets", "pvol_nvm_subsystem_name", "svol_host_groups", "svol_iscsi_targets", "svol_nvm_subsystem_name" (hv_shadow_image_pair_facts).

Removed Features (previously deprecated)
----------------------------------------

hitachivantara.vspone_block
~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Removed playbooks "ddp_pool.yml" and "ddp_pool_facts.yml".

Bugfixes
--------

Ansible-core
~~~~~~~~~~~~

- ansible-test remote alias - Alias values for ``--controller`` and ``--target`` are properly resolved for ``remote``. Previously, remote alias values (e.g. ``fedora/latest``) resolved to the correct name only for the legacy ``--remote`` arg, failing with an unknown image error for the newer args.
- task results - The ``invocation`` item result key omitted from registered values for looped task results, unless enabled via ``INJECT_INVOCATION``. Previously, it was deleted from registered non-loop results and only available to callbacks.

cisco.iosxr
~~~~~~~~~~~

- Fixed iosxr_user module to correctly handle MD5 hashed passwords when updating user credentials.

community.crypto
~~~~~~~~~~~~~~~~

- acme_* modules - improve handling of authz deactivation, and improve error message in case of bad authz states (https://github.com/ansible-collections/community.crypto/pull/998).

community.dns
~~~~~~~~~~~~~

- Update Public Suffix List.

community.general
~~~~~~~~~~~~~~~~~

- alternatives - normalize locale environment for ``run_command()`` calls to ``LANGUAGE=C``, ``LC_ALL=C`` (https://github.com/ansible-collections/community.general/issues/11737, https://github.com/ansible-collections/community.general/pull/11738).
- apache2_module - ensure ``LANGUAGE=C`` and ``LC_ALL=C`` are set when running commands that parse output (https://github.com/ansible-collections/community.general/issues/11737, https://github.com/ansible-collections/community.general/pull/11768).
- apk - normalize locale environment for ``run_command()`` calls to ``LANGUAGE=C``, ``LC_ALL=C`` (https://github.com/ansible-collections/community.general/issues/11737, https://github.com/ansible-collections/community.general/pull/11738).
- apt_repo - set ``LANGUAGE`` and ``LC_ALL`` to ``C`` in ``run_command()`` calls to ensure locale-independent output parsing (https://github.com/ansible-collections/community.general/issues/11737, https://github.com/ansible-collections/community.general/pull/11782).
- apt_rpm - normalize locale environment for ``run_command()`` calls to ``LANGUAGE=C``, ``LC_ALL=C`` (https://github.com/ansible-collections/community.general/issues/11737, https://github.com/ansible-collections/community.general/pull/11738).
- awall - set ``LANGUAGE`` and ``LC_ALL`` to ``C`` in ``run_command()`` calls to ensure locale-independent output parsing (https://github.com/ansible-collections/community.general/issues/11737, https://github.com/ansible-collections/community.general/pull/11784).
- beadm - set ``LANGUAGE`` and ``LC_ALL`` to ``C`` in ``run_command()`` calls to ensure locale-independent output parsing (https://github.com/ansible-collections/community.general/issues/11737, https://github.com/ansible-collections/community.general/pull/11780).
- bower - set ``LANGUAGE`` and ``LC_ALL`` to ``C`` in ``run_command()`` calls to ensure locale-independent output parsing (https://github.com/ansible-collections/community.general/issues/11737, https://github.com/ansible-collections/community.general/pull/11783).
- btrfs module_utils - set ``LANGUAGE`` and ``LC_ALL`` environment variables to ``C`` in all ``run_command()`` calls (https://github.com/ansible-collections/community.general/issues/11737, https://github.com/ansible-collections/community.general/pull/11787).
- bundler - set ``LANGUAGE`` and ``LC_ALL`` to ``C`` in ``run_command()`` calls to ensure locale-independent output parsing (https://github.com/ansible-collections/community.general/issues/11737, https://github.com/ansible-collections/community.general/pull/11783).
- bzr - set ``LANGUAGE`` and ``LC_ALL`` to ``C`` in ``run_command()`` calls to ensure locale-independent output parsing (https://github.com/ansible-collections/community.general/issues/11737, https://github.com/ansible-collections/community.general/pull/11785).
- capabilities - set ``LANGUAGE`` and ``LC_ALL`` to ``C`` in ``run_command()`` calls to ensure locale-independent output parsing (https://github.com/ansible-collections/community.general/issues/11737, https://github.com/ansible-collections/community.general/pull/11779).
- cargo - normalize locale environment for ``run_command()`` calls to ``LANGUAGE=C``, ``LC_ALL=C`` (https://github.com/ansible-collections/community.general/issues/11737, https://github.com/ansible-collections/community.general/pull/11738).
- composer - ensure ``LANGUAGE=C`` and ``LC_ALL=C`` are set when running commands that parse output (https://github.com/ansible-collections/community.general/issues/11737, https://github.com/ansible-collections/community.general/pull/11768).
- cronvar - ensure ``LANGUAGE=C`` and ``LC_ALL=C`` are set when running commands that parse output (https://github.com/ansible-collections/community.general/issues/11737, https://github.com/ansible-collections/community.general/pull/11773).
- dconf - ensure ``LANGUAGE=C`` and ``LC_ALL=C`` are set when running commands that parse output (https://github.com/ansible-collections/community.general/issues/11737, https://github.com/ansible-collections/community.general/pull/11765).
- dnf_versionlock - ensure ``LANGUAGE=C`` and ``LC_ALL=C`` are set when running commands that parse output (https://github.com/ansible-collections/community.general/issues/11737, https://github.com/ansible-collections/community.general/pull/11773).
- dpkg_divert - ensure ``LANGUAGE=C`` and ``LC_ALL=C`` are set when running commands that parse output (https://github.com/ansible-collections/community.general/issues/11737, https://github.com/ansible-collections/community.general/pull/11773).
- easy_install - set ``LANGUAGE`` and ``LC_ALL`` to ``C`` in ``run_command()`` calls to ensure locale-independent output parsing (https://github.com/ansible-collections/community.general/issues/11737, https://github.com/ansible-collections/community.general/pull/11782).
- etcd3 lookup plugin - improve HTTPS endpoint handling by stripping URL schemes from the ``host`` option and warning when ``ca_cert`` is not provided for HTTPS endpoints (https://github.com/ansible-collections/community.general/issues/1664, https://github.com/ansible-collections/community.general/pull/11861).
- facter_facts - ensure ``LANGUAGE=C`` and ``LC_ALL=C`` are set when running commands that parse output (https://github.com/ansible-collections/community.general/issues/11737, https://github.com/ansible-collections/community.general/pull/11768).
- filesystem - normalize locale environment for ``run_command()`` calls to ``LANGUAGE=C``, ``LC_ALL=C`` (https://github.com/ansible-collections/community.general/issues/11737, https://github.com/ansible-collections/community.general/pull/11738).
- flatpak - fix removal of runtimes, which was broken because the module was filtering the installed flatpak list to apps only, so runtimes could never be matched for uninstallation (https://github.com/ansible-collections/community.general/issues/553, https://github.com/ansible-collections/community.general/pull/11688).
- flatpak - support new output message when an update resulted in no action that appears on Fedora 44 (https://github.com/ansible-collections/community.general/pull/11836).
- flatpak_remote - ensure ``LANGUAGE=C`` and ``LC_ALL=C`` are set when running commands that parse output (https://github.com/ansible-collections/community.general/issues/11737, https://github.com/ansible-collections/community.general/pull/11773).
- git_config - normalize locale environment for ``run_command()`` calls to ``LANGUAGE=C``, ``LC_ALL=C`` (https://github.com/ansible-collections/community.general/issues/11737, https://github.com/ansible-collections/community.general/pull/11738).
- git_config_info - normalize locale environment for ``run_command()`` calls to ``LANGUAGE=C``, ``LC_ALL=C`` (https://github.com/ansible-collections/community.general/issues/11737, https://github.com/ansible-collections/community.general/pull/11738).
- gitlab_project_members - fail with a clear error when multiple projects match the given name, instead of silently operating on the first result (https://github.com/ansible-collections/community.general/issues/2767, https://github.com/ansible-collections/community.general/pull/11851).
- gitlab_project_variable - use ``find_project()`` from module utils for project lookup, consistent with all other GitLab modules in the collection (https://github.com/ansible-collections/community.general/issues/3157, https://github.com/ansible-collections/community.general/pull/11878).
- hg - ensure ``LANGUAGE=C`` and ``LC_ALL=C`` are set when running commands that parse output (https://github.com/ansible-collections/community.general/issues/11737, https://github.com/ansible-collections/community.general/pull/11773).
- homebrew - normalize locale environment for ``run_command()`` calls to ``LANGUAGE=C``, ``LC_ALL=C`` (https://github.com/ansible-collections/community.general/issues/11737, https://github.com/ansible-collections/community.general/pull/11740).
- homebrew_cask - fix ``sudo_password`` failing when the password contains single quotes or other special shell characters (https://github.com/ansible-collections/community.general/issues/4957, https://github.com/ansible-collections/community.general/pull/11850).
- homebrew_cask - fix failure when ``brew --version`` returns a placeholder version string (https://github.com/ansible-collections/community.general/issues/4708, https://github.com/ansible-collections/community.general/pull/11849).
- homebrew_cask - fix false task failure when upgrading casks with ``version=latest``; the post-upgrade check incorrectly re-ran ``brew outdated`` (which always lists ``latest`` casks as outdated under ``--greedy``), now uses the command exit code instead (https://github.com/ansible-collections/community.general/issues/1647, https://github.com/ansible-collections/community.general/pull/11838).
- homebrew_cask - normalize locale environment for ``run_command()`` calls to ``LANGUAGE=C``, ``LC_ALL=C`` (https://github.com/ansible-collections/community.general/issues/11737, https://github.com/ansible-collections/community.general/pull/11740).
- homebrew_tap - fix ``None`` being passed as a command argument when adding a tap without a URL (https://github.com/ansible-collections/community.general/pull/11848).
- homectl - allow to use passlib instead of legacycrypt for Python 3.13+ (https://github.com/ansible-collections/community.general/pull/11860).
- homectl - set ``LANGUAGE`` and ``LC_ALL`` to ``C`` in ``run_command()`` calls to ensure locale-independent output parsing (https://github.com/ansible-collections/community.general/issues/11737, https://github.com/ansible-collections/community.general/pull/11774).
- icinga2_feature - normalize locale environment for ``run_command()`` calls to ``LANGUAGE=C``, ``LC_ALL=C`` (https://github.com/ansible-collections/community.general/issues/11737, https://github.com/ansible-collections/community.general/pull/11740).
- imgadm - set ``LANGUAGE`` and ``LC_ALL`` to ``C`` in ``run_command()`` calls to ensure locale-independent output parsing (https://github.com/ansible-collections/community.general/issues/11737, https://github.com/ansible-collections/community.general/pull/11781).
- incus connection plugin - work when the active become plugin sets ``require_tty`` instead of failing silently (https://github.com/ansible-collections/community.general/pull/11771).
- ip_netns - set ``LANGUAGE`` and ``LC_ALL`` to ``C`` in ``run_command()`` calls to ensure locale-independent output parsing (https://github.com/ansible-collections/community.general/issues/11737, https://github.com/ansible-collections/community.general/pull/11779).
- ipa module utils - fix failure to detect errors reported in the ``failed`` field of the IPA API response, which is returned with HTTP 200 on partial or full failures in member add/remove operations (https://github.com/ansible-collections/community.general/issues/1239, https://github.com/ansible-collections/community.general/pull/11698).
- ipa_dnsrecord - fix errors when module is used with existing record with default TTL (https://github.com/ansible-collections/community.general/pull/11717).
- ipa_host - fix logic to disable existing hosts (https://github.com/ansible-collections/community.general/issues/11483, https://github.com/ansible-collections/community.general/pull/11487).
- iptables_state - normalize locale environment for ``run_command()`` calls to ``LANGUAGE=C``, ``LC_ALL=C`` (https://github.com/ansible-collections/community.general/issues/11737, https://github.com/ansible-collections/community.general/pull/11740).
- iso_extract - retry ``umount`` up to 5 times preventing ``OSError`` on cleanup (https://github.com/ansible-collections/community.general/issues/5333, https://github.com/ansible-collections/community.general/pull/11837).
- iso_extract - strip leading path separator from file entries so files with a leading ``/`` are extracted correctly (https://github.com/ansible-collections/community.general/issues/5283, https://github.com/ansible-collections/community.general/pull/11825).
- java_cert - set ``LANGUAGE`` and ``LC_ALL`` to ``C`` in ``run_command()`` calls to ensure locale-independent output parsing (https://github.com/ansible-collections/community.general/issues/11737, https://github.com/ansible-collections/community.general/pull/11774).
- java_keystore - normalize locale environment for ``run_command()`` calls to ``LANGUAGE=C``, ``LC_ALL=C`` (https://github.com/ansible-collections/community.general/issues/11737, https://github.com/ansible-collections/community.general/pull/11740).
- keyring - set ``LANGUAGE`` and ``LC_ALL`` to ``C`` in ``run_command()`` calls to ensure locale-independent output parsing (https://github.com/ansible-collections/community.general/issues/11737, https://github.com/ansible-collections/community.general/pull/11774).
- keyring_info - set ``LANGUAGE`` and ``LC_ALL`` to ``C`` in ``run_command()`` calls to ensure locale-independent output parsing (https://github.com/ansible-collections/community.general/issues/11737, https://github.com/ansible-collections/community.general/pull/11786).
- kibana_plugin - set ``LANGUAGE`` and ``LC_ALL`` to ``C`` in ``run_command()`` calls to ensure locale-independent output parsing (https://github.com/ansible-collections/community.general/issues/11737, https://github.com/ansible-collections/community.general/pull/11783).
- known_hosts module utils - ensure ``LANGUAGE=C`` and ``LC_ALL=C`` are set when running commands that parse output (https://github.com/ansible-collections/community.general/issues/11737, https://github.com/ansible-collections/community.general/pull/11768).
- launchd - set ``LANGUAGE`` and ``LC_ALL`` to ``C`` in ``run_command()`` calls to ensure locale-independent output parsing (https://github.com/ansible-collections/community.general/issues/11737, https://github.com/ansible-collections/community.general/pull/11774).
- lbu - set ``LANGUAGE`` and ``LC_ALL`` to ``C`` in ``run_command()`` calls to ensure locale-independent output parsing (https://github.com/ansible-collections/community.general/issues/11737, https://github.com/ansible-collections/community.general/pull/11781).
- listen_ports_facts - set ``LANGUAGE`` and ``LC_ALL`` to ``C`` in ``run_command()`` calls to ensure locale-independent output parsing (https://github.com/ansible-collections/community.general/issues/11737, https://github.com/ansible-collections/community.general/pull/11774).
- lldp - set ``LANGUAGE`` and ``LC_ALL`` to ``C`` in ``run_command()`` calls to ensure locale-independent output parsing (https://github.com/ansible-collections/community.general/issues/11737, https://github.com/ansible-collections/community.general/pull/11785).
- locale_gen - add missing locale entries to ``/etc/locale.gen`` when not already present (https://github.com/ansible-collections/community.general/issues/2399, https://github.com/ansible-collections/community.general/pull/11824).
- logrotate - adds missing default values for ``state`` and ``config_dir`` parameters, and adds ``required_by`` declarations for shred and compression parameters (https://github.com/ansible-collections/community.general/pull/11764).
- logrotate - fixes ``TypeError`` when ``shred_cycles`` is ``None`` and corrects ``enabled=None`` handling in ``get_config_path()`` (https://github.com/ansible-collections/community.general/pull/11764).
- logrotate - writes configuration files to a temporary file first and validates before atomically moving to the destination, and properly wraps all ``os.remove()`` and ``atomic_move()`` calls in error handling (https://github.com/ansible-collections/community.general/pull/11764).
- logstash_plugin - set ``LANGUAGE`` and ``LC_ALL`` to ``C`` in ``run_command()`` calls to ensure locale-independent output parsing (https://github.com/ansible-collections/community.general/issues/11737, https://github.com/ansible-collections/community.general/pull/11775).
- lvg - set ``LANGUAGE`` and ``LC_ALL`` to ``C`` in ``run_command()`` calls to ensure locale-independent output parsing (https://github.com/ansible-collections/community.general/issues/11737, https://github.com/ansible-collections/community.general/pull/11775).
- lvol - fix LVM version parsing (https://github.com/ansible-collections/community.general/issues/5445, https://github.com/ansible-collections/community.general/pull/11823).
- lvol - normalize locale environment for ``run_command()`` calls to ``LANGUAGE=C``, ``LC_ALL=C`` (https://github.com/ansible-collections/community.general/issues/11737, https://github.com/ansible-collections/community.general/pull/11740).
- lxc_container - set ``LANGUAGE`` and ``LC_ALL`` to ``C`` in ``run_command()`` calls to ensure locale-independent output parsing (https://github.com/ansible-collections/community.general/issues/11737, https://github.com/ansible-collections/community.general/pull/11779).
- machinectl become plugin - prevent printing ANSI terminal color sequences (https://github.com/ansible-collections/community.general/pull/11771).
- macports - ensure ``LANGUAGE=C`` and ``LC_ALL=C`` are set when running commands that parse output (https://github.com/ansible-collections/community.general/issues/11737, https://github.com/ansible-collections/community.general/pull/11768).
- mas - set ``LANGUAGE`` and ``LC_ALL`` to ``C`` in ``run_command()`` calls to ensure locale-independent output parsing (https://github.com/ansible-collections/community.general/issues/11737, https://github.com/ansible-collections/community.general/pull/11775).
- modprobe - ensure ``LANGUAGE=C`` and ``LC_ALL=C`` are set when running commands that parse output (https://github.com/ansible-collections/community.general/issues/11737, https://github.com/ansible-collections/community.general/pull/11768).
- monit - ensure ``LANGUAGE=C`` and ``LC_ALL=C`` are set when running commands that parse output (https://github.com/ansible-collections/community.general/issues/11737, https://github.com/ansible-collections/community.general/pull/11768).
- mssql_db - fail with a clear error message when a named instance (``server\instance`` format) is used together with ``login_port``, since these are mutually exclusive connection methods (https://github.com/ansible-collections/community.general/issues/5693, https://github.com/ansible-collections/community.general/pull/11664).
- mssql_script - fail with a clear error message when a named instance (``server\instance`` format) is used together with ``login_port``, since these are mutually exclusive connection methods (https://github.com/ansible-collections/community.general/issues/5693, https://github.com/ansible-collections/community.general/pull/11664).
- mssql_script - only passes ``params`` to ``cursor.execute()`` when the user actually provides them (https://github.com/ansible-collections/community.general/issues/11699, https://github.com/ansible-collections/community.general/pull/11754).
- nmcli - use ``get_best_parsable_locale()`` to set locale environment for ``run_command()`` calls, fixing UTF-8 connection names being corrupted to ``????`` under ``LC_ALL=C`` (https://github.com/ansible-collections/community.general/issues/10384, https://github.com/ansible-collections/community.general/issues/11737, https://github.com/ansible-collections/community.general/pull/11742).
- nsupdate - fix GSS-TSIG support (accidentally broken by https://github.com/ansible-collections/community.general/pull/11461, https://github.com/ansible-collections/community.general/pull/11712)
- ohai - set ``LANGUAGE`` and ``LC_ALL`` to ``C`` in ``run_command()`` calls to ensure locale-independent output parsing (https://github.com/ansible-collections/community.general/issues/11737, https://github.com/ansible-collections/community.general/pull/11785).
- onepassword_info - set ``LANGUAGE`` and ``LC_ALL`` to ``C`` in ``run_command()`` calls to ensure locale-independent output parsing (https://github.com/ansible-collections/community.general/issues/11737, https://github.com/ansible-collections/community.general/pull/11786).
- open_iscsi - ensure ``LANGUAGE=C`` and ``LC_ALL=C`` are set when running commands that parse output (https://github.com/ansible-collections/community.general/issues/11737, https://github.com/ansible-collections/community.general/pull/11768).
- openbsd_pkg - ensure ``LANGUAGE=C`` and ``LC_ALL=C`` are set when running commands that parse output (https://github.com/ansible-collections/community.general/issues/11737, https://github.com/ansible-collections/community.general/pull/11767).
- openwrt_init - set ``LANGUAGE`` and ``LC_ALL`` to ``C`` in ``run_command()`` calls to ensure locale-independent output parsing (https://github.com/ansible-collections/community.general/issues/11737, https://github.com/ansible-collections/community.general/pull/11784).
- osx_defaults - set ``LANGUAGE`` and ``LC_ALL`` to ``C`` in ``run_command()`` calls to ensure locale-independent output parsing (https://github.com/ansible-collections/community.general/issues/11737, https://github.com/ansible-collections/community.general/pull/11775).
- pacemaker_resource, pacemaker_stonith - fix resource and stonith creation race condition by polling PCS status (https://github.com/ansible-collections/community.general/issues/11574, https://github.com/ansible-collections/community.general/pull/11750).
- pacman - normalize locale environment for ``run_command()`` calls to ``LANGUAGE=C``, ``LC_ALL=C`` (https://github.com/ansible-collections/community.general/issues/11737, https://github.com/ansible-collections/community.general/pull/11740).
- pacman_key - ensure ``LANGUAGE=C`` and ``LC_ALL=C`` are set when running commands that parse output (https://github.com/ansible-collections/community.general/issues/11737, https://github.com/ansible-collections/community.general/pull/11768).
- parted - normalize locale environment for ``run_command()`` calls to ``LANGUAGE=C``, ``LC_ALL=C`` (https://github.com/ansible-collections/community.general/issues/11737, https://github.com/ansible-collections/community.general/pull/11740).
- pear - set ``LANGUAGE`` and ``LC_ALL`` to ``C`` in ``run_command()`` calls to ensure locale-independent output parsing (https://github.com/ansible-collections/community.general/issues/11737, https://github.com/ansible-collections/community.general/pull/11782).
- pip_package_info - set ``LANGUAGE`` and ``LC_ALL`` to ``C`` in ``run_command()`` calls to ensure locale-independent output parsing (https://github.com/ansible-collections/community.general/issues/11737, https://github.com/ansible-collections/community.general/pull/11784).
- pkg5 - set ``LANGUAGE`` and ``LC_ALL`` to ``C`` in ``run_command()`` calls to ensure locale-independent output parsing (https://github.com/ansible-collections/community.general/issues/11737, https://github.com/ansible-collections/community.general/pull/11780).
- pkg5_publisher - set ``LANGUAGE`` and ``LC_ALL`` to ``C`` in ``run_command()`` calls to ensure locale-independent output parsing (https://github.com/ansible-collections/community.general/issues/11737, https://github.com/ansible-collections/community.general/pull/11780).
- pkgin - normalize locale environment for ``run_command()`` calls to ``LANGUAGE=C``, ``LC_ALL=C`` (https://github.com/ansible-collections/community.general/issues/11737, https://github.com/ansible-collections/community.general/pull/11741).
- pkgng - ensure ``LANGUAGE=C`` and ``LC_ALL=C`` are set when running commands that parse output (https://github.com/ansible-collections/community.general/issues/11737, https://github.com/ansible-collections/community.general/pull/11765).
- pkgutil - set ``LANGUAGE`` and ``LC_ALL`` to ``C`` in ``run_command()`` calls to ensure locale-independent output parsing (https://github.com/ansible-collections/community.general/issues/11737, https://github.com/ansible-collections/community.general/pull/11775).
- pnpm - set ``LANGUAGE`` and ``LC_ALL`` to ``C`` in ``run_command()`` calls to ensure locale-independent output parsing (https://github.com/ansible-collections/community.general/issues/11737, https://github.com/ansible-collections/community.general/pull/11776).
- portage - set ``LANGUAGE`` and ``LC_ALL`` to ``C`` in ``run_command()`` calls to ensure locale-independent output parsing (https://github.com/ansible-collections/community.general/issues/11737, https://github.com/ansible-collections/community.general/pull/11781).
- portinstall - set ``LANGUAGE`` and ``LC_ALL`` to ``C`` in ``run_command()`` calls to ensure locale-independent output parsing (https://github.com/ansible-collections/community.general/issues/11737, https://github.com/ansible-collections/community.general/pull/11781).
- redhat_subscription - normalize locale environment for ``run_command()`` calls to ``LANGUAGE=C``, ``LC_ALL=C`` (https://github.com/ansible-collections/community.general/issues/11737, https://github.com/ansible-collections/community.general/pull/11741).
- rhsm_release - ensure ``LANGUAGE=C`` and ``LC_ALL=C`` are set when running commands that parse output (https://github.com/ansible-collections/community.general/issues/11737, https://github.com/ansible-collections/community.general/pull/11768).
- rhsm_repository - normalize locale environment for ``run_command()`` calls to ``LANGUAGE=C``, ``LC_ALL=C`` (https://github.com/ansible-collections/community.general/issues/11737, https://github.com/ansible-collections/community.general/pull/11741).
- riak - set ``LANGUAGE`` and ``LC_ALL`` to ``C`` in ``run_command()`` calls to ensure locale-independent output parsing (https://github.com/ansible-collections/community.general/issues/11737, https://github.com/ansible-collections/community.general/pull/11786).
- rpm_ostree_pkg - ensure ``LANGUAGE=C`` and ``LC_ALL=C`` are set when running commands that parse output (https://github.com/ansible-collections/community.general/issues/11737, https://github.com/ansible-collections/community.general/pull/11768).
- run0 become plugin - mark the plugin as incompatible with connection pipelining (see https://github.com/ansible/ansible/issues/81254, https://github.com/ansible-collections/community.general/pull/11771).
- run0 become plugin - prevent printing ANSI terminal color sequences (https://github.com/ansible-collections/community.general/pull/11771).
- runit - normalize locale environment for ``run_command()`` calls to ``LANGUAGE=C``, ``LC_ALL=C`` (https://github.com/ansible-collections/community.general/issues/11737, https://github.com/ansible-collections/community.general/pull/11741).
- sefcontext - flush the in-process ``matchpathcon`` cache after applying changes, so subsequent tasks running in the same process (for example via the Mitogen connection plugin) see the updated SELinux file context rules instead of stale cached data (https://github.com/ansible-collections/community.general/issues/888, https://github.com/ansible-collections/community.general/pull/11812).
- smartos_image_info - set ``LANGUAGE`` and ``LC_ALL`` to ``C`` in ``run_command()`` calls to ensure locale-independent output parsing (https://github.com/ansible-collections/community.general/issues/11737, https://github.com/ansible-collections/community.general/pull/11781).
- snmp_facts - the module now also supports pysnmp >= 7.1 (https://github.com/ansible-collections/community.general/issues/8852, https://github.com/ansible-collections/community.general/pull/11683).
- sorcery - ensure ``LANGUAGE=C`` and ``LC_ALL=C`` are set when running commands that parse output (https://github.com/ansible-collections/community.general/issues/11737, https://github.com/ansible-collections/community.general/pull/11767).
- supervisorctl - normalize locale environment for ``run_command()`` calls to ``LANGUAGE=C``, ``LC_ALL=C`` (https://github.com/ansible-collections/community.general/issues/11737, https://github.com/ansible-collections/community.general/pull/11741).
- svc - normalize locale environment for ``run_command()`` calls to ``LANGUAGE=C``, ``LC_ALL=C`` (https://github.com/ansible-collections/community.general/issues/11737, https://github.com/ansible-collections/community.general/pull/11741).
- swdepot - set ``LANGUAGE`` and ``LC_ALL`` to ``C`` in ``run_command()`` calls to ensure locale-independent output parsing (https://github.com/ansible-collections/community.general/issues/11737, https://github.com/ansible-collections/community.general/pull/11780).
- syspatch - set ``LANGUAGE`` and ``LC_ALL`` to ``C`` in ``run_command()`` calls to ensure locale-independent output parsing (https://github.com/ansible-collections/community.general/issues/11737, https://github.com/ansible-collections/community.general/pull/11781).
- sysrc - set ``LANGUAGE`` and ``LC_ALL`` to ``C`` in ``run_command()`` calls to ensure locale-independent output parsing (https://github.com/ansible-collections/community.general/issues/11737, https://github.com/ansible-collections/community.general/pull/11776).
- sysupgrade - ensure ``LANGUAGE=C`` and ``LC_ALL=C`` are set when running commands that parse output (https://github.com/ansible-collections/community.general/issues/11737, https://github.com/ansible-collections/community.general/pull/11768).
- terraform - ensure ``LANGUAGE=C`` and ``LC_ALL=C`` are set when running commands that parse output (https://github.com/ansible-collections/community.general/issues/11737, https://github.com/ansible-collections/community.general/pull/11765).
- timezone - set ``LANGUAGE`` and ``LC_ALL`` to ``C`` in ``run_command()`` calls to ensure locale-independent output parsing (https://github.com/ansible-collections/community.general/issues/11737, https://github.com/ansible-collections/community.general/pull/11776).
- udm_user - allow to use passlib instead of legacycrypt for Python 3.13+ (https://github.com/ansible-collections/community.general/issues/4690, https://github.com/ansible-collections/community.general/pull/11860).
- udm_user - fix alias-to-canonical parameter name mismatch that caused all camelCase-aliased parameters such as ``display_name`` and ``primary_group`` to be silently ignored (https://github.com/ansible-collections/community.general/issues/2950, https://github.com/ansible-collections/community.general/issues/3691, https://github.com/ansible-collections/community.general/pull/11859).
- ufw - normalize locale environment for ``run_command()`` calls to ``LANGUAGE=C``, ``LC_ALL=C`` (https://github.com/ansible-collections/community.general/issues/11737, https://github.com/ansible-collections/community.general/pull/11741).
- xattr - set ``LANGUAGE`` and ``LC_ALL`` to ``C`` in ``run_command()`` calls to ensure locale-independent output parsing (https://github.com/ansible-collections/community.general/issues/11737, https://github.com/ansible-collections/community.general/pull/11776).
- xbps - set ``LANGUAGE`` and ``LC_ALL`` to ``C`` in ``run_command()`` calls to ensure locale-independent output parsing (https://github.com/ansible-collections/community.general/issues/11737, https://github.com/ansible-collections/community.general/pull/11781).
- xenserver_guest - fix an issue where booting from ISO is not possible because CD-ROM device is placed in position above number 3. Position number 3 is now reserved for CD-ROM device and cannot be occupied by a disk (https://github.com/ansible-collections/community.general/issues/11624, https://github.com/ansible-collections/community.general/pull/11702).
- yarn - set ``LANGUAGE`` and ``LC_ALL`` to ``C`` in ``run_command()`` calls to ensure locale-independent output parsing (https://github.com/ansible-collections/community.general/issues/11737, https://github.com/ansible-collections/community.general/pull/11776).
- yum_versionlock - set ``LANGUAGE`` and ``LC_ALL`` to ``C`` in ``run_command()`` calls to ensure locale-independent output parsing (https://github.com/ansible-collections/community.general/issues/11737, https://github.com/ansible-collections/community.general/pull/11777).
- zfs - set ``LANGUAGE`` and ``LC_ALL`` to ``C`` in ``run_command()`` calls to ensure locale-independent output parsing (https://github.com/ansible-collections/community.general/issues/11737, https://github.com/ansible-collections/community.general/pull/11778).
- zfs_delegate_admin - set ``LANGUAGE`` and ``LC_ALL`` to ``C`` in ``run_command()`` calls to ensure locale-independent output parsing (https://github.com/ansible-collections/community.general/issues/11737, https://github.com/ansible-collections/community.general/pull/11778).
- zfs_facts - set ``LANGUAGE`` and ``LC_ALL`` to ``C`` in ``run_command()`` calls to ensure locale-independent output parsing (https://github.com/ansible-collections/community.general/issues/11737, https://github.com/ansible-collections/community.general/pull/11778).
- zpool_facts - set ``LANGUAGE`` and ``LC_ALL`` to ``C`` in ``run_command()`` calls to ensure locale-independent output parsing (https://github.com/ansible-collections/community.general/issues/11737, https://github.com/ansible-collections/community.general/pull/11778).
- zypper - normalize locale environment for ``run_command()`` calls to ``LANGUAGE=C``, ``LC_ALL=C`` (https://github.com/ansible-collections/community.general/issues/11737, https://github.com/ansible-collections/community.general/pull/11741).
- zypper_repository - set ``LANGUAGE`` and ``LC_ALL`` to ``C`` in ``run_command()`` calls to ensure locale-independent output parsing (https://github.com/ansible-collections/community.general/issues/11737, https://github.com/ansible-collections/community.general/pull/11777).
- zypper_repository_info - set ``LANGUAGE`` and ``LC_ALL`` to ``C`` in ``run_command()`` calls to ensure locale-independent output parsing (https://github.com/ansible-collections/community.general/issues/11737, https://github.com/ansible-collections/community.general/pull/11782).

community.zabbix
~~~~~~~~~~~~~~~~

- Added 'status' handling to sanatize_params in zabbix_itemprototype module to allow for 'enabled'/'disabled' values.
- Updated tests to reflect the change in parameter handling.
- add zabbix_agent 7.4 as valid for windows
- all modules - fixed password handeling
- fix zabbix_agent_version_long version comparison
- server role - fixed issues with mysql import
- use architecture2 in map for amd64/i386
- web role - Fixed ownership of `/etc/zabbix/web` directory to match Debian distributions packages
- zabbix_agent - add fallback to first ipv4 address if default cant be determined for zabbix_agent_ip
- zabbix_proxy - add fallback to first ipv4 address if default cant be determined for zabbix_proxy_ip
- zabbix_server - Adapt all the PostgresDB related task to be schema aware (https://github.com/ansible-collections/community.zabbix/issues/1647).
- zabbix_template - prevent false reporting of password change
- zabbix_trigger - add selectDependencies and selectTags when requesting triggers to detect changes to those values
- zabbix_valuemap - add missing host_name option which is required by the Zabbix API (https://github.com/ansible-collections/community.zabbix/issues/1636).
- zabbix_web - define zabbix_server_dbschema default value
- zabbix_web - nginx vhost template did not support http2 configuration (https://github.com/ansible-collections/community.zabbix/issues/1668).

fortinet.fortios
~~~~~~~~~~~~~~~~

- Fixed an issue where parameters ending with _dict always returned changed, even in check mode or when no changes were made.
- Fixed an issue where some modules could not be configured globally.
- Fixed an issue where the generate-key.system.api-user selector in the fortios_monitor module required an admin password to function.

hitachivantara.vspone_block
~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Fixed performance for "hv_snapshot_group_facts" module.

splunk.es
~~~~~~~~~

- splunk_finding, splunk_finding_info - Fix query by ref_id failing to find findings due to sub-second time precision mismatch. The ``earliest`` time extracted from the ref_id now includes a 1-second buffer to ensure the finding falls within the search window.

New Plugins
-----------

Filter
~~~~~~

- community.crypto.acme_dns_persist_record - Craft a DNS record for ACME :literal:`dns\-persist\-01` challenges.
- community.crypto.acme_dns_persist_record_parse - Parse a DNS record for ACME :literal:`dns\-persist\-01` challenges.

New Modules
-----------

community.general
~~~~~~~~~~~~~~~~~

- community.general.snap_connect - Manages snap interface connections.

hitachivantara.vspone_block
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Vsp
^^^

- hitachivantara.vspone_block.hv_gad_bulk - Manages batch GAD pairs on VSP block storage systems.
- hitachivantara.vspone_block.hv_hg_bulk - Manages host groups in bulk on VSP block storage system with parallel processing.
- hitachivantara.vspone_block.hv_iscsi_target_bulk - Manages iscsi targets in bulk mode on VSP block storage systems.
- hitachivantara.vspone_block.hv_ldev_bulk - Manages multiple logical devices (LDEVs) in bulk on VSP block storage systems.
- hitachivantara.vspone_block.hv_truecopy_bulk - Manages bulk TrueCopy pairs on VSP block storage systems.

Unchanged Collections
---------------------

- amazon.aws (still version 11.2.0)
- ansible.netcommon (still version 8.5.0)
- ansible.posix (still version 2.1.0)
- ansible.utils (still version 6.0.2)
- ansible.windows (still version 3.5.0)
- arista.eos (still version 12.0.1)
- azure.azcollection (still version 3.16.0)
- check_point.mgmt (still version 6.9.0)
- chocolatey.chocolatey (still version 1.6.0)
- cisco.aci (still version 2.13.0)
- cisco.intersight (still version 2.18.0)
- cisco.ios (still version 11.3.0)
- cisco.meraki (still version 2.23.2)
- cisco.mso (still version 2.13.0)
- cisco.nxos (still version 11.1.3)
- cisco.ucs (still version 1.16.0)
- cloudscale_ch.cloud (still version 2.5.3)
- community.aws (still version 11.0.0)
- community.ciscosmb (still version 1.0.11)
- community.clickhouse (still version 2.1.0)
- community.docker (still version 5.2.0)
- community.grafana (still version 2.3.0)
- community.hashi_vault (still version 7.1.0)
- community.hrobot (still version 2.7.1)
- community.library_inventory_filtering_v1 (still version 1.1.5)
- community.libvirt (still version 2.2.0)
- community.mongodb (still version 1.7.12)
- community.mysql (still version 4.2.0)
- community.okd (still version 5.0.0)
- community.postgresql (still version 4.2.0)
- community.proxmox (still version 2.0.0-beta1)
- community.proxysql (still version 1.7.0)
- community.rabbitmq (still version 1.6.0)
- community.sap_libs (still version 1.7.0)
- community.vmware (still version 6.2.0)
- community.windows (still version 3.1.0)
- containers.podman (still version 1.19.2)
- cyberark.conjur (still version 1.3.9)
- cyberark.pas (still version 1.0.39)
- dellemc.enterprise_sonic (still version 4.1.0)
- dellemc.openmanage (still version 10.0.2)
- dellemc.powerflex (still version 3.0.0)
- dellemc.unity (still version 2.1.0)
- f5networks.f5_modules (still version 1.39.0)
- fortinet.fortimanager (still version 2.13.0)
- google.cloud (still version 1.13.0)
- grafana.grafana (still version 6.0.6)
- graphiant.naas (still version 26.3.0)
- hetzner.hcloud (still version 6.8.0)
- hitachivantara.vspone_object (still version 1.1.1)
- ibm.storage_virtualize (still version 3.3.0)
- ieisystem.inmanage (still version 4.0.0)
- infinidat.infinibox (still version 1.6.3)
- infoblox.nios_modules (still version 1.9.0)
- inspur.ispim (still version 2.2.4)
- kaytus.ksmanage (still version 4.0.0)
- kubernetes.core (still version 6.3.0)
- kubevirt.core (still version 2.2.4)
- lowlydba.sqlserver (still version 2.8.1)
- microsoft.ad (still version 1.10.0)
- microsoft.iis (still version 1.1.0)
- netapp.cloudmanager (still version 21.24.0)
- netapp.ontap (still version 23.4.0)
- netapp.storagegrid (still version 21.16.0)
- netapp_eseries.santricity (still version 2.0.1)
- netbox.netbox (still version 3.22.0)
- ngine_io.cloudstack (still version 3.0.0)
- openstack.cloud (still version 2.5.0)
- ovirt.ovirt (still version 3.2.2)
- pcg.alpaca_operator (still version 2.2.0)
- purestorage.flasharray (still version 1.42.0)
- purestorage.flashblade (still version 1.24.0)
- ravendb.ravendb (still version 1.0.4)
- telekom_mms.icinga_director (still version 2.5.1)
- vmware.vmware (still version 2.8.0)
- vmware.vmware_rest (still version 4.10.0)
- vultr.cloud (still version 1.14.0)
- vyos.vyos (still version 6.0.0)
- wti.remote (still version 1.0.11)

v14.0.0a2
=========

.. contents::
  :local:
  :depth: 2

Release Summary
---------------

Release Date: 2026-04-14

`Porting Guide <https://docs.ansible.com/projects/ansible/devel/porting_guides.html>`_

Ansible-core
------------

Ansible 14.0.0a2 contains ansible-core version 2.21.0b2.
This is a newer version than version 2.21.0b1 contained in the previous Ansible release.

The changes are reported in the combined changelog below.

Changed Collections
-------------------

If not mentioned explicitly, the changes are reported in the combined changelog below.

+--------------------+------------------+------------------+------------------------------------------------------------------------------------------------------------------------------+
| Collection         | Ansible 14.0.0a1 | Ansible 14.0.0a2 | Notes                                                                                                                        |
+====================+==================+==================+==============================================================================================================================+
| ansible.netcommon  | 8.4.0            | 8.5.0            |                                                                                                                              |
+--------------------+------------------+------------------+------------------------------------------------------------------------------------------------------------------------------+
| ansible.utils      | 6.0.1            | 6.0.2            |                                                                                                                              |
+--------------------+------------------+------------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.intersight   | 2.17.0           | 2.18.0           | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+--------------------+------------------+------------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.meraki       | 2.23.1           | 2.23.2           |                                                                                                                              |
+--------------------+------------------+------------------+------------------------------------------------------------------------------------------------------------------------------+
| community.docker   | 5.1.0            | 5.2.0            |                                                                                                                              |
+--------------------+------------------+------------------+------------------------------------------------------------------------------------------------------------------------------+
| community.routeros | 3.18.0           | 3.19.0           |                                                                                                                              |
+--------------------+------------------+------------------+------------------------------------------------------------------------------------------------------------------------------+
| containers.podman  | 1.19.0           | 1.19.2           |                                                                                                                              |
+--------------------+------------------+------------------+------------------------------------------------------------------------------------------------------------------------------+
| lowlydba.sqlserver | 2.7.0            | 2.8.1            |                                                                                                                              |
+--------------------+------------------+------------------+------------------------------------------------------------------------------------------------------------------------------+

Minor Changes
-------------

Ansible-core
~~~~~~~~~~~~

- ansible-test - Generate ``dist_info`` when running tests.
- ansible-test - Upgrade the distro-specific test containers.

ansible.netcommon
~~~~~~~~~~~~~~~~~

- The dependency on ansible-pylibssh (for ssh_type=libssh / network_cli) is now ansible-pylibssh>=1.4.0 in requirements.txt, raised from the previous >=0.2.0 requirement. Installations still on ansible-pylibssh 0.x or 1.x below 1.4.0 must upgrade to use the libssh connection path with this collection release.
- libssh connection - When log_path is set (e.g. via ANSIBLE_LOG_PATH or log_path in ansible.cfg), the plugin now routes ansible-pylibssh (libssh) logs into the same Ansible log file. Log level is derived from display.verbosity using Python standard logging: verbosity 0 -> WARNING, 1-2 -> INFO, 3+ -> DEBUG. This allows SSH/libssh debug and trace output to appear in the configured log file for troubleshooting without changing ansible-pylibssh configuration manually.
- network_cli - The in-collection paramiko path supports the same host key policy behavior (including host_key_auto_add and known_hosts handling) and persistent connection caching as the previous ansible-core paramiko integration.
- network_cli - When ssh_type is set to paramiko, the connection plugin now uses an in-collection paramiko implementation instead of loading ansible-core's paramiko connection plugin. This allows network_cli to work with versions of ansible-core, where the paramiko connection plugin was removed.

community.docker
~~~~~~~~~~~~~~~~

- docker_image_export - adds ``platform`` parameter to allow exporting a specific platform variant from a multi-arch image (https://github.com/ansible-collections/community.docker/issues/1064, https://github.com/ansible-collections/community.docker/pull/1251).

community.routeros
~~~~~~~~~~~~~~~~~~

- api_info - add missing ``numbers`` parameter across numerous existing paths for RouterOS >= 7.15.2 (https://github.com/ansible-collections/community.routeros/pull/458).
- api_info - add support for the ``interface dot1x server active``, ``ip hotspot active``, ``ip ipsec active-peers``, ``ip proxy cache-contents``, ``ip socks connections``, ``user active``, and ``user-manager session`` paths as info-only (read-only) paths (https://github.com/ansible-collections/community.routeros/pull/458).
- api_info - adds support for additional read-only parameters in the ``app`` path for RouterOS >= 7.22 (https://github.com/ansible-collections/community.routeros/pull/457).
- api_info, api_modify - add ``color`` parameter to the ``zerotier interface`` path for RouterOS >= 7.22.1 (https://github.com/ansible-collections/community.routeros/pull/459).
- api_info, api_modify - add ``current-defaults`` parameter to the ``ip dns`` path for RouterOS >= 7.22.1 (https://github.com/ansible-collections/community.routeros/pull/459).
- api_info, api_modify - add ``mld-datapath`` parameter to the ``interface wifi cap`` path for RouterOS >= 7.22.1 (https://github.com/ansible-collections/community.routeros/pull/459).
- api_info, api_modify - adds support for multiple ``healthcheck-*`` parameters in the ``container`` path for RouterOS >= 7.22 (https://github.com/ansible-collections/community.routeros/pull/457).
- api_info, api_modify - adds support for new ``input.add-path`` and ``output.add-path`` parameters replacing ``add-path-out`` in BGP-related paths for RouterOS >= 7.22 (https://github.com/ansible-collections/community.routeros/pull/457).
- api_info, api_modify - adds support for the ``add-topics-string`` and ``script`` parameters in the ``system logging action`` path for RouterOS >= 7.22 (https://github.com/ansible-collections/community.routeros/pull/457).
- api_info, api_modify - adds support for the ``app-store-urls`` parameter in the ``app settings`` path for RouterOS >= 7.22 (https://github.com/ansible-collections/community.routeros/pull/457).
- api_info, api_modify - adds support for the ``chain``, ``realm``, and ``vrf`` parameters in the ``routing rule`` path for RouterOS >= 7.22 (https://github.com/ansible-collections/community.routeros/pull/457).
- api_info, api_modify - adds support for the ``channel.preamble-puncturing`` parameter in the ``interface wifi configuration`` path for RouterOS >= 7.22 (https://github.com/ansible-collections/community.routeros/pull/457).
- api_info, api_modify - adds support for the ``channel.preamble-puncturing``, ``mld-interface``, and ``mld-name`` parameters in the ``interface wifi`` path for RouterOS >= 7.22 (https://github.com/ansible-collections/community.routeros/pull/457).
- api_info, api_modify - adds support for the ``comment`` parameter in the ``system logging`` path for RouterOS >= 7.22 (https://github.com/ansible-collections/community.routeros/pull/457).
- api_info, api_modify - adds support for the ``ddos-cookie-threshold`` parameter in the ``ip ipsec settings`` path for RouterOS >= 7.22 (https://github.com/ansible-collections/community.routeros/pull/457).
- api_info, api_modify - adds support for the ``dhcp6-pd-preferred`` parameter in the ``ipv6 nd prefix`` and ``ipv6 nd prefix default`` paths for RouterOS >= 7.22 (https://github.com/ansible-collections/community.routeros/pull/457).
- api_info, api_modify - adds support for the ``from-pool`` parameter in the ``ipv6 pool`` path for RouterOS >= 7.22 (https://github.com/ansible-collections/community.routeros/pull/457).
- api_info, api_modify - adds support for the ``interface wifi network`` and ``interface wifi network radio`` paths for RouterOS >= 7.22 (https://github.com/ansible-collections/community.routeros/pull/457).
- api_info, api_modify - adds support for the ``interframe-gap`` parameter in the ``iot modbus`` path for RouterOS >= 7.22 (https://github.com/ansible-collections/community.routeros/pull/457).
- api_info, api_modify - adds support for the ``ip reverse-proxy`` path for RouterOS >= 7.22 (https://github.com/ansible-collections/community.routeros/pull/457).
- api_info, api_modify - adds support for the ``mlag-heartbeat``, ``mlag-peer-port``, ``mlag-priority``, and ``ra-guard`` parameters in the ``interface bridge`` path for RouterOS >= 7.22 (https://github.com/ansible-collections/community.routeros/pull/457).
- api_info, api_modify - adds support for the ``mld-static`` parameter in the ``interface wifi cap`` path for RouterOS >= 7.22 (https://github.com/ansible-collections/community.routeros/pull/457).
- api_info, api_modify - adds support for the ``multi-link-mode`` and ``supported-hw-caps`` parameters in the ``interface wifi provisioning`` path for RouterOS >= 7.22 (https://github.com/ansible-collections/community.routeros/pull/457).
- api_info, api_modify - adds support for the ``multipath`` parameter in the ``routing bgp instance`` path for RouterOS >= 7.22 (https://github.com/ansible-collections/community.routeros/pull/457).
- api_info, api_modify - adds support for the ``name`` parameter in the ``ip dhcp-client`` path for RouterOS >= 7.22 (https://github.com/ansible-collections/community.routeros/pull/457).
- api_info, api_modify - adds support for the ``otp-secret`` parameter in the ``ip hotspot user`` path for RouterOS >= 7.21.3 (https://github.com/ansible-collections/community.routeros/pull/457).
- api_info, api_modify - adds support for the ``password`` parameter in the ``system package local-update update-package-source`` path for RouterOS >= 7.22 (https://github.com/ansible-collections/community.routeros/pull/457).
- api_info, api_modify - adds support for the ``policy-rules`` parameter in the ``routing settings`` path for RouterOS >= 7.22 (https://github.com/ansible-collections/community.routeros/pull/457).
- api_info, api_modify - adds support for the ``preamble-puncturing`` parameter in the ``interface wifi channel`` path for RouterOS >= 7.22 (https://github.com/ansible-collections/community.routeros/pull/457).
- api_info, api_modify - adds support for the ``preferred-architecture`` parameter in the ``system routerboard settings`` path for RouterOS >= 7.22 (https://github.com/ansible-collections/community.routeros/pull/457).
- api_info, api_modify - adds support for the ``pvid``, ``use-https``, and ``yaml`` parameters in the ``app`` path for RouterOS >= 7.22 (https://github.com/ansible-collections/community.routeros/pull/457).
- api_info, api_modify - adds support for the ``request-interval`` parameter in the ``interface detect-internet`` path for RouterOS >= 7.22 (https://github.com/ansible-collections/community.routeros/pull/457).
- api_info, api_modify - adds support for the ``trusted-ra`` parameter in the ``interface bridge port`` path for RouterOS >= 7.22 (https://github.com/ansible-collections/community.routeros/pull/457).
- api_info, api_modify - adjusts handling of required parameters in the ``interface wifi`` path by removing ``default-name`` from ``required_one_of`` for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/457).
- api_info, api_modify - removed support for the ``add-path-out`` parameter in BGP-related paths for RouterOS >= 7.22 (https://github.com/ansible-collections/community.routeros/pull/457).
- api_info, api_modify - removed support for the ``system package local-update`` path for RouterOS >= 7.22 (https://github.com/ansible-collections/community.routeros/pull/457).
- api_modify, api_info - sort versioned buckets numerically so tighter bounds match before broader ones (https://github.com/ansible-collections/community.routeros/pull/456).

containers.podman
~~~~~~~~~~~~~~~~~

- Add --platform option to podman_image

lowlydba.sqlserver
~~~~~~~~~~~~~~~~~~

- user_role - Added ``roles`` parameter with ``add``/``remove``/``set`` pattern to manage multiple roles. The existing ``role`` parameter is deprecated and will be removed in 3.0.0. (#352)

Deprecated Features
-------------------

ansible.netcommon
~~~~~~~~~~~~~~~~~

- network_cli - The in-collection paramiko support (used when ssh_type is paramiko) is a compatibility layer for environments where ansible-core's paramiko connection is no longer available. This layer is deprecated and will be removed in a release after 2028-02-01. Migrate to ssh_type=libssh by installing the ansible-pylibssh package.

community.routeros
~~~~~~~~~~~~~~~~~~

- api_modify - all existing ``numbers`` fields are deprecated for writing and support for them will be removed in community.routeros 4.0.0 (https://github.com/ansible-collections/community.routeros/pull/460).
- api_modify - in ``routing bfd configuration``, the fields ``copy-from`` and ``place-before`` are deprecated for writing and support for them will be removed in community.routeros 4.0.0 (https://github.com/ansible-collections/community.routeros/pull/460).

Bugfixes
--------

Ansible-core
~~~~~~~~~~~~

- Fix ``validate_argspec`` when tags are defined on the play. The ``always`` tag is only added if the play has no tags.
- ``--start-at-task`` - fix starting at the requested task instead of starting at the next block or play. Play level tasks run first. (https://github.com/ansible/ansible/issues/86268)

ansible.netcommon
~~~~~~~~~~~~~~~~~

- filter plugins - Add plugin_routing redirects for ``ipaddr``, ``ipv4``, and ``ipv6`` to ``ansible.utils`` so short names work when ``ansible.netcommon`` is in the play's collection list (https://github.com/ansible-collections/ansible.utils/issues/404).
- filter plugins - Convert filter arguments to native Python types before ``AnsibleArgSpecValidator`` so filters work with Ansible 2.19+ lazy containers that cannot be deep-copied (e.g. ``vlan_parser``, ``vlan_expander``, ``hash_salt``, ``type5_pw``, ``comp_type5``, ``parse_cli``, ``parse_cli_textfsm``, ``parse_xml``, ``pop_ace``).
- libssh connection - Fixed test_libssh_put_file unit test so the put_file code path (used by net_put, copy module, and other file transfer over libssh) is properly tested in CI. The test now sets connection options and mocks Session so put_file does not trigger a real connection attempt with an unset host (was failing with "Hostname required").
- network action plugin - Fall back when remove_internal_keys is not importable from ansible.vars.clean (e.g. some ansible-core builds), so direct module execution still cleans module return data.
- network_cli - Fixed file transfer (net_put / net_get) when ssh_type=libssh. For put_file, no longer call_connect_uncached() before delegating to the libssh connection the libssh plugin's put_file() calls _connect() internally. For fetch_file, call _connect() then fetch_file() for libssh instead of _connect_uncached(), so connection caching and the correct flow are used. Paramiko branch unchanged (still uses _connect_uncached() for scp/sftp).

ansible.utils
~~~~~~~~~~~~~

- cidr_merge - Fix filter failing when used inside a Jinja2 macro called with ``with context`` by unwrapping Ansible lazy template lists before validation.
- cli_parse - Honor ttp_results.results flat_list in TTP parser so output is a single-level list instead of double-wrapped (https://github.com/ansible-collections/ansible.utils/issues/402).
- ipaddress_utils - Support Python 3.14+ by using the public ``version`` attribute instead of the removed private ``_version`` on ``ipaddress`` network objects (bpo-118710).
- update_fact - Use task_vars at top-level instead of the deprecated ``vars`` key for compatibility with ansible-core 2.24 (ansible/ansible issue

cisco.meraki
~~~~~~~~~~~~

- devices_switch_ports - Fixed AttributeError crash in ``update()`` caused by ``get_object_by_name`` returning the full port list instead of ``None`` when no port matched by name. Added ``isinstance(prev_obj_name, dict)`` guard to prevent calling ``.get()`` on a list.
- devices_switch_ports - Fixed idempotency regression where the module always reported ``changed`` due to ``serial`` (a path parameter absent from the API response) and ``portId`` (int/string type mismatch) being incorrectly included in the ``requires_update`` comparison.

containers.podman
~~~~~~~~~~~~~~~~~

- podman_container - Fix quadlet_options placement when restart_policy is set
- podman_network - Add diff and idempotency to ip_ranges in net_config

Unchanged Collections
---------------------

- amazon.aws (still version 11.2.0)
- ansible.posix (still version 2.1.0)
- ansible.windows (still version 3.5.0)
- arista.eos (still version 12.0.1)
- azure.azcollection (still version 3.16.0)
- check_point.mgmt (still version 6.9.0)
- chocolatey.chocolatey (still version 1.6.0)
- cisco.aci (still version 2.13.0)
- cisco.ios (still version 11.3.0)
- cisco.iosxr (still version 12.1.1)
- cisco.mso (still version 2.13.0)
- cisco.nxos (still version 11.1.3)
- cisco.ucs (still version 1.16.0)
- cloudscale_ch.cloud (still version 2.5.3)
- community.aws (still version 11.0.0)
- community.ciscosmb (still version 1.0.11)
- community.clickhouse (still version 2.1.0)
- community.crypto (still version 3.1.1)
- community.dns (still version 3.5.3)
- community.general (still version 12.5.0)
- community.grafana (still version 2.3.0)
- community.hashi_vault (still version 7.1.0)
- community.hrobot (still version 2.7.1)
- community.library_inventory_filtering_v1 (still version 1.1.5)
- community.libvirt (still version 2.2.0)
- community.mongodb (still version 1.7.12)
- community.mysql (still version 4.2.0)
- community.okd (still version 5.0.0)
- community.postgresql (still version 4.2.0)
- community.proxmox (still version 2.0.0-beta1)
- community.proxysql (still version 1.7.0)
- community.rabbitmq (still version 1.6.0)
- community.sap_libs (still version 1.7.0)
- community.sops (still version 2.3.0-b1)
- community.vmware (still version 6.2.0)
- community.windows (still version 3.1.0)
- community.zabbix (still version 4.1.1)
- cyberark.conjur (still version 1.3.9)
- cyberark.pas (still version 1.0.39)
- dellemc.enterprise_sonic (still version 4.1.0)
- dellemc.openmanage (still version 10.0.2)
- dellemc.powerflex (still version 3.0.0)
- dellemc.unity (still version 2.1.0)
- f5networks.f5_modules (still version 1.39.0)
- fortinet.fortimanager (still version 2.13.0)
- fortinet.fortios (still version 2.5.0)
- google.cloud (still version 1.13.0)
- grafana.grafana (still version 6.0.6)
- graphiant.naas (still version 26.3.0)
- hetzner.hcloud (still version 6.8.0)
- hitachivantara.vspone_block (still version 4.6.1)
- hitachivantara.vspone_object (still version 1.1.1)
- ibm.storage_virtualize (still version 3.3.0)
- ieisystem.inmanage (still version 4.0.0)
- infinidat.infinibox (still version 1.6.3)
- infoblox.nios_modules (still version 1.9.0)
- inspur.ispim (still version 2.2.4)
- kaytus.ksmanage (still version 4.0.0)
- kubernetes.core (still version 6.3.0)
- kubevirt.core (still version 2.2.4)
- microsoft.ad (still version 1.10.0)
- microsoft.iis (still version 1.1.0)
- netapp.cloudmanager (still version 21.24.0)
- netapp.ontap (still version 23.4.0)
- netapp.storagegrid (still version 21.16.0)
- netapp_eseries.santricity (still version 2.0.1)
- netbox.netbox (still version 3.22.0)
- ngine_io.cloudstack (still version 3.0.0)
- openstack.cloud (still version 2.5.0)
- ovirt.ovirt (still version 3.2.2)
- pcg.alpaca_operator (still version 2.2.0)
- purestorage.flasharray (still version 1.42.0)
- purestorage.flashblade (still version 1.24.0)
- ravendb.ravendb (still version 1.0.4)
- splunk.es (still version 5.1.0)
- telekom_mms.icinga_director (still version 2.5.1)
- theforeman.foreman (still version 5.10.0)
- vmware.vmware (still version 2.8.0)
- vmware.vmware_rest (still version 4.10.0)
- vultr.cloud (still version 1.14.0)
- vyos.vyos (still version 6.0.0)
- wti.remote (still version 1.0.11)

v14.0.0a1
=========

.. contents::
  :local:
  :depth: 2

Release Summary
---------------

Release Date: 2026-04-07

`Porting Guide <https://docs.ansible.com/projects/ansible/devel/porting_guides.html>`_

Removed Collections
-------------------

- awx.awx (previously included version: 24.6.1)
- cisco.dnac (previously included version: 6.41.0)
- junipernetworks.junos (previously included version: 11.0.0)

You can still install a removed collection manually with ``ansible-galaxy collection install <name-of-collection>``.

Added Collections
-----------------

- community.clickhouse (version 2.1.0)
- graphiant.naas (version 26.3.0)
- pcg.alpaca_operator (version 2.2.0)

Ansible-core
------------

Ansible 14.0.0a1 contains ansible-core version 2.21.0b1.
This is a newer version than version 2.20.0 contained in the previous Ansible release.

The changes are reported in the combined changelog below.

Included Collections
--------------------

If not mentioned explicitly, the changes are reported in the combined changelog below.

+------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Collection                   | Ansible 13.0.0 | Ansible 14.0.0a1 | Notes                                                                                                                                                                                                           |
+==============================+================+==================+=================================================================================================================================================================================================================+
| amazon.aws                   | 10.1.2         | 11.2.0           |                                                                                                                                                                                                                 |
+------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ansible.netcommon            | 8.1.0          | 8.4.0            |                                                                                                                                                                                                                 |
+------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ansible.utils                | 6.0.0          | 6.0.1            |                                                                                                                                                                                                                 |
+------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ansible.windows              | 3.2.0          | 3.5.0            |                                                                                                                                                                                                                 |
+------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| arista.eos                   | 12.0.0         | 12.0.1           |                                                                                                                                                                                                                 |
+------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| azure.azcollection           | 3.10.1         | 3.16.0           | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.                                                                                    |
+------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| check_point.mgmt             | 6.6.0          | 6.9.0            | The collection did not have a changelog in this version.                                                                                                                                                        |
+------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| chocolatey.chocolatey        | 1.5.3          | 1.6.0            |                                                                                                                                                                                                                 |
+------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cisco.aci                    | 2.12.0         | 2.13.0           |                                                                                                                                                                                                                 |
+------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cisco.intersight             | 2.7.0          | 2.17.0           | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.                                                                                    |
+------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cisco.ios                    | 11.1.1         | 11.3.0           |                                                                                                                                                                                                                 |
+------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cisco.iosxr                  | 12.1.0         | 12.1.1           |                                                                                                                                                                                                                 |
+------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cisco.meraki                 | 2.21.8         | 2.23.1           |                                                                                                                                                                                                                 |
+------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cisco.mso                    | 2.11.0         | 2.13.0           |                                                                                                                                                                                                                 |
+------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cisco.nxos                   | 11.0.0         | 11.1.3           |                                                                                                                                                                                                                 |
+------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cloudscale_ch.cloud          | 2.5.2          | 2.5.3            |                                                                                                                                                                                                                 |
+------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.aws                | 10.0.0         | 11.0.0           |                                                                                                                                                                                                                 |
+------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.clickhouse         |                | 2.1.0            | The collection was added to Ansible                                                                                                                                                                             |
+------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.crypto             | 3.0.5          | 3.1.1            |                                                                                                                                                                                                                 |
+------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.dns                | 3.4.0          | 3.5.3            |                                                                                                                                                                                                                 |
+------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.docker             | 5.0.1          | 5.1.0            |                                                                                                                                                                                                                 |
+------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.general            | 12.0.1         | 12.5.0           |                                                                                                                                                                                                                 |
+------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.hrobot             | 2.7.0          | 2.7.1            |                                                                                                                                                                                                                 |
+------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.libvirt            | 2.0.0          | 2.2.0            |                                                                                                                                                                                                                 |
+------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.mongodb            | 1.7.10         | 1.7.12           | There are no changes recorded in the changelog.                                                                                                                                                                 |
+------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.mysql              | 4.0.1          | 4.2.0            |                                                                                                                                                                                                                 |
+------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.postgresql         | 4.1.0          | 4.2.0            |                                                                                                                                                                                                                 |
+------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.proxmox            | 1.4.0          | 2.0.0-beta1      |                                                                                                                                                                                                                 |
+------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.routeros           | 3.13.0         | 3.18.0           |                                                                                                                                                                                                                 |
+------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.sap_libs           | 1.5.0          | 1.7.0            |                                                                                                                                                                                                                 |
+------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.sops               | 2.2.7          | 2.3.0-b1         |                                                                                                                                                                                                                 |
+------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.vmware             | 6.1.0          | 6.2.0            |                                                                                                                                                                                                                 |
+------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.windows            | 3.0.1          | 3.1.0            |                                                                                                                                                                                                                 |
+------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| containers.podman            | 1.18.0         | 1.19.0           |                                                                                                                                                                                                                 |
+------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cyberark.conjur              | 1.3.8          | 1.3.9            | You can find the collection's changelog at `https://github.com/cyberark/ansible-conjur-collection/blob/master/CHANGELOG.md <https://github.com/cyberark/ansible-conjur-collection/blob/master/CHANGELOG.md>`__. |
+------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cyberark.pas                 | 1.0.36         | 1.0.39           | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.                                                                                    |
+------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| dellemc.enterprise_sonic     | 3.2.0          | 4.1.0            |                                                                                                                                                                                                                 |
+------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| dellemc.openmanage           | 10.0.1         | 10.0.2           |                                                                                                                                                                                                                 |
+------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| fortinet.fortimanager        | 2.11.0         | 2.13.0           |                                                                                                                                                                                                                 |
+------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| fortinet.fortios             | 2.4.2          | 2.5.0            |                                                                                                                                                                                                                 |
+------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| google.cloud                 | 1.9.0          | 1.13.0           |                                                                                                                                                                                                                 |
+------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| graphiant.naas               |                | 26.3.0           | The collection was added to Ansible                                                                                                                                                                             |
+------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| hetzner.hcloud               | 6.0.0          | 6.8.0            |                                                                                                                                                                                                                 |
+------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| hitachivantara.vspone_block  | 4.4.0          | 4.6.1            |                                                                                                                                                                                                                 |
+------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| hitachivantara.vspone_object | 1.0.0          | 1.1.1            |                                                                                                                                                                                                                 |
+------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ibm.storage_virtualize       | 3.1.0          | 3.3.0            |                                                                                                                                                                                                                 |
+------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| infoblox.nios_modules        | 1.8.0          | 1.9.0            |                                                                                                                                                                                                                 |
+------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| inspur.ispim                 | 2.2.3          | 2.2.4            |                                                                                                                                                                                                                 |
+------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| kaytus.ksmanage              | 2.0.0          | 4.0.0            |                                                                                                                                                                                                                 |
+------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| kubernetes.core              | 6.2.0          | 6.3.0            |                                                                                                                                                                                                                 |
+------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| kubevirt.core                | 2.2.3          | 2.2.4            | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.                                                                                    |
+------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| microsoft.ad                 | 1.9.2          | 1.10.0           |                                                                                                                                                                                                                 |
+------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| microsoft.iis                | 1.0.3          | 1.1.0            |                                                                                                                                                                                                                 |
+------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| netapp.ontap                 | 23.2.0         | 23.4.0           |                                                                                                                                                                                                                 |
+------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| netapp.storagegrid           | 21.15.0        | 21.16.0          |                                                                                                                                                                                                                 |
+------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| netapp_eseries.santricity    | 1.4.1          | 2.0.1            | The collection did not have a changelog in this version.                                                                                                                                                        |
+------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| netbox.netbox                | 3.21.0         | 3.22.0           |                                                                                                                                                                                                                 |
+------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ovirt.ovirt                  | 3.2.1          | 3.2.2            |                                                                                                                                                                                                                 |
+------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| pcg.alpaca_operator          |                | 2.2.0            | The collection was added to Ansible                                                                                                                                                                             |
+------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| purestorage.flasharray       | 1.39.0         | 1.42.0           |                                                                                                                                                                                                                 |
+------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| purestorage.flashblade       | 1.22.0         | 1.24.0           |                                                                                                                                                                                                                 |
+------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| splunk.es                    | 4.0.0          | 5.1.0            |                                                                                                                                                                                                                 |
+------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| telekom_mms.icinga_director  | 2.4.0          | 2.5.1            |                                                                                                                                                                                                                 |
+------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| theforeman.foreman           | 5.7.0          | 5.10.0           |                                                                                                                                                                                                                 |
+------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| vmware.vmware                | 2.4.0          | 2.8.0            |                                                                                                                                                                                                                 |
+------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| vmware.vmware_rest           | 4.9.0          | 4.10.0           |                                                                                                                                                                                                                 |
+------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| vultr.cloud                  | 1.13.0         | 1.14.0           |                                                                                                                                                                                                                 |
+------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| wti.remote                   | 1.0.10         | 1.0.11           | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.                                                                                    |
+------------------------------+----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Major Changes
-------------

Ansible-core
~~~~~~~~~~~~

- ``ansible-galaxy install`` and ``ansible-galaxy collection install|download`` - collections that declare a ``requires_ansible`` version that is not compatible with the running ansible-core version are now excluded from installation and download by default. In previous versions, ansible-galaxy would install such collections even if doing so resulted in an error at load time. To restore the previous behavior, set ``COLLECTIONS_ON_ANSIBLE_VERSION_MISMATCH`` to ``ignore`` in your configuration. (https://github.com/ansible/ansible/issues/78539)
- action plugins - Actions can directly register variables at several precedence layers using the ``register_host_variables`` method on ``ActionBase``. Previously, variable registration could only be simulated by user action plugins by returning ``ansible_facts`` with insecure fact injection.
- register projections - The ``register`` task keyword allows mapping multiple variable names to Jinja expressions to transform task results and other variables. The mapping form can replace many usages of ``set_fact`` and allows order-independent chained access to other variable expressions within the same task.
- task implicit object - A new ``_task`` implicit object is available for use in ``register`` and task conditional expressions (e.g., ``failed_when``). The result of the current task can be accessed via the ``_task.result`` property, without the use of ``register``. Under a loop, ``_task.result`` is the most recently completed result and ``_task.loop_result`` provides access to accumulated loop results. The ``_task.polymorphic_result`` property provides compatibility with classic name-only ``register`` in loops. The value is the result of the most recent loop iteration, then becomes the final list loop result once the loop is complete.

amazon.aws
~~~~~~~~~~

- amazon.aws collection - ``awscli`` version has been bumped to 1.34.0 (https://github.com/ansible-collections/amazon.aws/pull/2774).
- amazon.aws collection - ``botocore`` and ``boto3`` versions have been bumped to 1.35.0 (https://github.com/ansible-collections/amazon.aws/pull/2774).
- ec2_security_group - Support for passing nested lists of strings to ``rules.cidr_ip`` and ``rules.cidr_ipv6`` have been removed (https://github.com/ansible-collections/amazon.aws/issues/2777).
- iam_user - Support for ``iam_user`` return key has been removed; only ``user`` is now returned (https://github.com/ansible-collections/amazon.aws/issues/2777).
- lambda_info - Support for ``function`` has been removed (https://github.com/ansible-collections/amazon.aws/issues/2777).
- route53_info - Support for CamelCased lists (``ResourceRecordSets``, ``HostedZones``, ``HealthChecks``, ``CheckerIpRanges``, ``DelegationSets``, ``HealthCheck``) have been removed (https://github.com/ansible-collections/amazon.aws/issues/2777).
- s3_object - Support for ``list`` mode has been removed; use ``s3_object_info`` instead (https://github.com/ansible-collections/amazon.aws/issues/2777).
- s3_object - Support for passing the leading ``/`` has been removed (https://github.com/ansible-collections/amazon.aws/issues/2777).
- s3_object_info - Support for passing ``dualstack`` and ``endpoint_url`` at the same time has been removed (https://github.com/ansible-collections/amazon.aws/issues/2777).

chocolatey.chocolatey
~~~~~~~~~~~~~~~~~~~~~

- win_chocolatey - add option to ignore pinned status of pinned packages

community.aws
~~~~~~~~~~~~~

- community.aws collection - ``awscli`` version has been bumped to 1.34.0 (https://github.com/ansible-collections/community.aws/pull/2375).
- community.aws collection - ``botocore`` and ``boto3`` versions have been bumped to 1.35.0 (https://github.com/ansible-collections/community.aws/pull/2375).

community.proxmox
~~~~~~~~~~~~~~~~~

- proxmox - Add ca_path option to specify a ca-certificate for tls validation (https://github.com/ansible-collections/community.proxmox/pull/256).

community.routeros
~~~~~~~~~~~~~~~~~~

- api_info, api_modify - multiple parameters can no longer be disabled for the``tool netwatch`` path (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - parameter ``name-format`` can no longer be disabled for the ``interface wifi provisioning`` path (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - parameter ``script`` can no longer be disabled for the ``ip dhcp-client`` path (https://github.com/ansible-collections/community.routeros/pull/433).

community.vmware
~~~~~~~~~~~~~~~~

- Bump required ``vmware.vmware`` collection version to 2.5.0 (https://github.com/ansible-collections/community.vmware/pull/2503).

containers.podman
~~~~~~~~~~~~~~~~~

- Add podman Quadlet modules
- Rewrite podman and buildah connections

fortinet.fortios
~~~~~~~~~~~~~~~~

- Supported new versions 7.6.5 and 7.6.6.
- Updated the Q&A for using the default_group feature in modules.

kaytus.ksmanage
~~~~~~~~~~~~~~~

- Add new modules upload_ssl,ssl_info,generate_ssl. (https://github.com/ieisystem/kaytus.ksmanage/pull/34).
- Change the name of the used SDK. (https://github.com/ieisystem/kaytus.ksmanage/pull/37).
- Modify the URL address path when the owner is changed. (https://github.com/ieisystem/kaytus.ksmanage/pull/38).
- The edit_m6_log_setting.py module has added the 'server_status' attribute; The edit_network_bond.py module modifies the attribute descriptions; The edit_snmp.py and edit_snmp_trap.py module modifies the allowable value ranges for the auth_protocol and priv_protocol attributes. (https://github.com/ieisystem/kaytus.ksmanage/pull/33).

netapp.ontap
~~~~~~~~~~~~

- na_ontap_autoupdate_config - REST only support for managing configurations for automatic updates, requires ONTAP 9.10.1 or later.
- na_ontap_cg - REST only support for managing consistency groups, requires ONTAP 9.10.1 or later.
- na_ontap_cifs - AWS Lambda support added to the module.
- na_ontap_cifs_acl - AWS Lambda support added to the module.
- na_ontap_cifs_local_group - AWS Lambda support added to the module.
- na_ontap_cifs_local_group_member - AWS Lambda support added to the module.
- na_ontap_cifs_local_user - AWS Lambda support added to the module.
- na_ontap_cifs_local_user_set_password - AWS Lambda support added to the module.
- na_ontap_cifs_privileges - AWS Lambda support added to the module.
- na_ontap_cifs_server - AWS Lambda support added to the module.
- na_ontap_cifs_unix_symlink_mapping - AWS Lambda support added to the module.
- na_ontap_cluster_peer - AWS Lambda support added to the module.
- na_ontap_igroup - AWS Lambda support added to the module.
- na_ontap_igroup_initiator - AWS Lambda support added to the module.
- na_ontap_interface - AWS Lambda support added to the module.
- na_ontap_lun - AWS Lambda support added to the module.
- na_ontap_lun_copy - AWS Lambda support added to the module.
- na_ontap_lun_map - AWS Lambda support added to the module.
- na_ontap_lun_map_reporting_nodes - AWS Lambda support added to the module.
- na_ontap_s3_buckets - AWS Lambda support added to the module.
- na_ontap_s3_groups - AWS Lambda support added to the module.
- na_ontap_s3_policies - AWS Lambda support added to the module.
- na_ontap_s3_services - AWS Lambda support added to the module.
- na_ontap_s3_users - AWS Lambda support added to the module.
- na_ontap_snapmirror - AWS Lambda support added to the module.
- na_ontap_snapshot - AWS Lambda support added to the module.
- na_ontap_svm - AWS Lambda support added to the module.
- na_ontap_volume_autosize - AWS Lambda support added to the module.
- na_ontap_volume_clone - AWS Lambda support added to the module.
- na_ontap_vserver_peer - AWS Lambda support added to the module.

splunk.es
~~~~~~~~~

- Bumped the minimum supported Ansible version to ``>=2.17.0`` (Ansible 2.15/2.16 are EoL).

vmware.vmware
~~~~~~~~~~~~~

- Replace ``ansible.module_utils._text`` (https://github.com/ansible-collections/vmware.vmware/issues/268).
- Replace ``ansible.module_utils.common._collections_compat`` (https://github.com/ansible-collections/vmware.vmware/issues/271).

Minor Changes
-------------

Ansible-core
~~~~~~~~~~~~

- DataLoader - Update ``DataLoader`` to deal exclusively in str
- PowerShell 7 - Add support for running PowerShell written modules on POSIX hosts. PowerShell modules run with the ``pwsh`` interpreter and can access the same module utils that Windows PowerShell modules can use. Some PowerShell based module utils may not be compatible due to their reliance on Windows APIs but ``Ansible.Basic.cs`` for module input and output handling works.
- PowerShell AddType Util - Will only include the debug information when ``DISPLAY_TRACEBACK`` contains ``error`` or ``always``. In the past the debug information would have been included if ``-vvv`` or higher was used but this new behavior aligns the logic with the new option added in Ansible 2.19.
- The minimum required ``setuptools`` version is now ``77.0.3``, as it is needed for the new PEP 639 license format
- ansiballz - Add tech preview to embed arbitrary files, not relying on python ``import``
- ansible-playbook - consolidated block and task loading code to remove duplicated logic (https://github.com/ansible/ansible/pull/86603).
- ansible-test - Add PowerShell support to managed containers and remotes.
- ansible-test - Add container/remote aliases for more loosely specifying managed test environments.
- ansible-test - Add limited RHEL8 integration test remote supporting Python 3.12 only
- ansible-test - Add support for using the Ansible Core CI service from GitHub Actions.
- ansible-test - Expand functions covered by the ``unwanted`` rule for the ``pylint`` sanity test. It now includes various ``os.*`` and ``subprocess.*`` subprocess functions in Ansible modules and module_utils.
- ansible-test - Optimize DNF configuration for managed remote RHEL instances.
- ansible-test - Remove ``use-run-command-not-popen`` and ``use-run-command-not-os-call`` error codes from the ``validate-modules`` sanity test. These scenarios are now covered by the ``pylint`` sanity test.
- ansible-test - Remove pylint check for ``urllib2`` usage.
- ansible-test - Remove support for an obsolete remote authentication method.
- ansible-test - Replace Alpine 3.22 container and remote with 3.23.
- ansible-test - Replace Fedora 42 with 43.
- ansible-test - Replace FreeBSD 13.5 remote with 15.0.
- ansible-test - Replace FreeBSD 14.3 remote with 14.4.
- ansible-test - Replace RHEL 10.0 remote with 10.1.
- ansible-test - Replace RHEL 9.6 remote with 9.7.
- ansible-test - Replace macOS 15.3 remote with macOS 26.3.
- ansible-test - Replace the ``parallels`` managed macOS provider with a new ``mac`` provider.
- ansible-test - Support automatic loading of test collections in core integration tests.
- ansible-test - Switch managed macOS remotes from x86_64 to aarch64.
- ansible-test - Update URL used to download FreeBSD wheels for managed remotes.
- ansible-test - Update ansible-test-utility-container.
- ansible-test - Update base and default containers.
- ansible-test - Update http-test-container.
- ansible-test - Update pypi-test-container.
- ansible-test - Update sanity test requirements.
- ansible-test - Update the pylint sanity test to pylint 4.0.2.
- ansible-test - Use the new API endpoint for the Ansible Core CI service.
- ansible-test - add ``.winrm`` and ``.networking`` as valid JSON/YAML inventory file extensions. This should not affect any public facing code as it is used internally for inventories generated by ``ansible-test``.
- ansible-test - update galaxy_ng container to current version deployed to galaxy.ansible.com
- ansible-test acme cloud plugin - update to the 2.4.0 ACME test image, which upgrades Pebble to 2.10.0, Go to 1.26, and Python to 3.14, and generally updates all contained Python dependencies (https://github.com/ansible/ansible/pull/86740).
- ansible-test validate-modules sanity test - now reports bad return value keys that cannot be used with the dot notation in Jinja expressions (https://github.com/ansible/ansible/issues/86079).
- ansible-vault - improved error messages for better clarity and context when vault operations fail, helping users diagnose configuration or file access issues more easily (https://github.com/ansible/ansible/pull/86602).
- ansible-vault - keep the original contents when the EDITOR returns failure when using ``ansible-vault edit``.
- break_when - A ``break_when_result`` key is always present in results when a ``break_when`` expression is used.
- break_when - A ``break_when_suppressed_exception`` key is added to a result when a ``break_when`` expression fails and masks an existing exception in a result.
- break_when - A failed ``break_when`` expression now preserves the loop structure of a result and any loop item results.
- callback - filter key starting with _ansible_ from debug messages (https://github.com/ansible/ansible/issues/69731).
- callback plugins - support configuration using extra variables.
- changed_when - A ``changed_when_result`` key is always present in results when a ``changed_when`` expression is used.
- changed_when - A ``changed_when_suppressed_exception`` key is added to a result when a ``changed_when`` expression fails and masks an existing exception in a result.
- core - The ``ActionBase._low_level_execute_command`` method no longer adds ``&& sleep 0`` to commands. This was a work-around for a 10+ year old Linux kernel bug affecting OpenSSH. By August of 2016 the fix had been included in kernel versions 4.1.26, 4.4.12, 4.5.6, 4.6.1 and 4.7. Linux kernel bug report: https://lore.kernel.org/lkml/alpine.LNX.2.00.1512091358290.9574@fanir.tuyoix.net/ OpenSSH bug report: https://bugzilla.mindrot.org/show_bug.cgi?id=2492
- deb822_repository - add include and exclude parameter arguments (https://github.com/ansible/ansible/issues/86155)
- default callback - add ``display_included_hosts`` option to control the ``included:`` banner lines for ``include_tasks``/``include_role`` (https://github.com/ansible/ansible/issues/84499).
- default callback plugin - add option to configure line width for YAML output. This allows to disable line wrapping (https://github.com/ansible/ansible/issues/84657, https://github.com/ansible/ansible/pull/85498).
- default callback plugin - add variable configuration for ``display_skipped_hosts`` (https://github.com/ansible/ansible/issues/84469).
- display - replace few words with more inclusive word list such as denylist, FilterDenyList (https://github.com/ansible/ansible/pull/86304).
- dnf - Separate module into module and utility script
- executor - remove unused RETURN_VARS
- file - return disk_usage_bytes fact (https://github.com/ansible/ansible/issues/70834).
- filter - Use datetime.strftime instead of time.strftime in strftime (https://github.com/ansible/ansible/issues/86260).
- find - add locale encoding in err msg when none is given
- generator - add support for extra vars (https://github.com/ansible/ansible/issues/83270).
- group - Add warning message when invalid priority values are provided to Group.set_priority() method (https://github.com/ansible/ansible/pull/85468).
- ignore_errors - Invalid values for ``ignore_errors`` will always be treated as ``False``
- ignore_errors - Templated values for the ``ignore_errors`` keyword behave more consistently in looped tasks. If ``ignore_errors`` resolves ``True`` for any loop item, errors will be ignored for the entire task.
- ignore_unreachable - Templated values for the ``ignore_unreachable`` keyword behave more consistently in looped tasks. If ``ignore_unreachable`` resolves ``True`` for any loop item, unreachable hosts will be ignored for the entire task.
- include_role has new option `rescuable` to allow it to toggle between task failure and syntax errors.
- loops - The ``break_when`` keyword is now validated when the value is falsey.
- loops - The registered result of a loop task no longer contains the ``skipped`` key when it would be ``False``.
- module/action results - A ``results`` key returned from an action or module is always preserved. Previously the ``results`` key was sometimes removed, depending on the type of its value.
- package_facts - Switch from rpm python to rpm CLI to list packages
- package_facts - use apk query instead of apk info for gathering package facts in Alpine (https://github.com/ansible/ansible/issues/86579).
- password hashing - Add support back for using the ``crypt`` implementation from the C library used to build Python, or with expanded functionality using ``libxcrypt``
- psrp - Added the ``certificate_key_password`` option through the variable ``ansible_psrp_certificate_key_password`` that can be used to decrypt the key specified by ``certificate_key_pem``. This option requires ``pypsrp>=0.9.0`` to be installed in the Ansible environment.
- psrp - Added the ``no_profile`` option through the variable ``ansible_psrp_no_profile`` that can stop the remote Windows host from loading the user profile on the Ansible tasks. This option requires ``pypsrp>=0.9.0`` to be installed in the Ansible environment.
- script - remove the currently unsupported ``decrypt`` argument from the module documentation (https://github.com/ansible/ansible/issues/86067).
- service - add support for GNU Hurd systems, which use SysV init scripts (https://github.com/ansible/ansible/pull/86622).
- slurp module gets new C(armor) option to allow user to disable base64 encoding.
- stat - return disk_usage_bytes fact (https://github.com/ansible/ansible/issues/70834).
- to_yaml / to_nice_yaml filters - Add optional ``vault_behavior`` argument to configure how vaulted values are rendered.

amazon.aws
~~~~~~~~~~

- Add support for the io2 storage type for RDS (https://github.com/ansible-collections/amazon.aws/pull/2748).
- autoscaling_group - Added a boolean parameter ``protected_from_scale_in`` to toggle protection from scale-in. This allows users to enable or disable scale-in protection for instances in an autoscaling group. (https://github.com/ansible-collections/amazon.aws/pull/2207)
- aws_cloudtrail - Ported the event source plugin from ``ansible.eda`` to ``amazon.aws`` (https://github.com/ansible-collections/amazon.aws/pull/2816).
- aws_cloudtrail - replace deprecated ``datetime.utcnow()`` with timezone-aware ``datetime.now(tz=timezone.utc)`` (https://github.com/ansible-collections/amazon.aws/pull/2858).
- aws_ec2 - added "ec2_tags" host variable (https://github.com/ansible-collections/amazon.aws/pull/2847).
- aws_ec2 - remove explicit ``disable_lookups=False`` parameter from template calls as it is deprecated and False is the default value (https://github.com/ansible-collections/amazon.aws/pull/2864).
- aws_inventory_base - remove explicit ``disable_lookups=False`` parameter from template calls as it is deprecated and False is the default value (https://github.com/ansible-collections/amazon.aws/pull/2864).
- aws_rds - added "rds_tags" host variable (https://github.com/ansible-collections/amazon.aws/pull/2847).
- aws_resource_actions - remove redundant ``list()`` call when using ``sorted()``, improving efficiency by allowing sorted() to consume the generator expression directly (https://github.com/ansible-collections/amazon.aws/pull/2882).
- aws_sqs_queue - Ported the event source plugin from ``ansible.eda`` to ``amazon.aws`` (https://github.com/ansible-collections/amazon.aws/pull/2816).
- ec2_launch_template - increase GP3 volume ``throughput`` limits in line with updated AWS limits (https://github.com/ansible-collections/amazon.aws/pull/2749).
- ec2_vol - added ``volume_initialization_rate`` optional parameter to support Provisioned Initialization Rate when creating a volume from snapshots. (https://github.com/ansible-collections/amazon.aws/issues/2665)
- ec2_vol - increase ``throughput`` and ``iops`` limits for GP3 volumes in line with updated AWS limits (https://github.com/ansible-collections/amazon.aws/pull/2749).
- ec2_vpc_endpoint - replace deprecated ``datetime.utcnow()`` with timezone-aware ``datetime.now(datetime.timezone.utc)`` (https://github.com/ansible-collections/amazon.aws/pull/2866).
- ec2_vpc_nat_gateway - replace deprecated ``datetime.utcnow()`` with timezone-aware ``datetime.now(datetime.timezone.utc)`` (https://github.com/ansible-collections/amazon.aws/pull/2866).
- indirect node count - Add support for querying RDS database resources (https://github.com/ansible-collections/amazon.aws/pull/2825).
- indirect node count - Create query for networking load balancer resources (https://github.com/ansible-collections/amazon.aws/pull/2818).
- indirect node count - create query for ec2 (https://github.com/ansible-collections/amazon.aws/pull/2807).
- indirect node count - create query for networking resources vpc, subnet, nat gateway, internet gateway, virtual gateway, route table, vpn, vpc peering (https://github.com/ansible-collections/amazon.aws/pull/2811).
- indirect node count - create query for storage resources S3 bucket and Object (https://github.com/ansible-collections/amazon.aws/pull/2811).
- module_utils.s3 - added "501" to the list of error codes thrown by S3 replacements (https://github.com/ansible-collections/amazon.aws/issues/2447).
- module_utils/_s3/common - use ``is_boto3_error_httpstatus`` to handle HTTP 403 and 501 status codes from S3-compatible services (https://github.com/ansible-collections/amazon.aws/pull/2776).
- module_utils/botocore - add ``is_boto3_error_httpstatus`` helper function to catch boto3 exceptions based on HTTP status codes (https://github.com/ansible-collections/amazon.aws/pull/2776).
- module_utils/s3 - refactored S3 module utilities to consolidate duplicate code, add comprehensive type hints and docstrings, and improve maintainability (https://github.com/ansible-collections/amazon.aws/pull/2782).
- plugin_utils/inventory - add error handling for ClientError and BotoCoreError in _freeze_iam_role method (https://github.com/ansible-collections/amazon.aws/pull/2902).
- plugin_utils/inventory - extract role session name generation into separate method to improve code organisation (https://github.com/ansible-collections/amazon.aws/pull/2902).
- requirements.txt - Added ``aiobotocore`` as a dependency for the event source plugins only (https://github.com/ansible-collections/amazon.aws/pull/2816).
- route53 - added ``record_values`` key to ``resource_record_sets`` return value that can be accessed using Jinja2 dot notation (https://github.com/ansible-collections/amazon.aws/pull/2772).
- route53 - added ``routing_region`` parameter to explicitly specify the region for latency-based resource record sets (https://github.com/ansible-collections/amazon.aws/issues/2893).
- route53 - added temporary ``aws_region`` parameter to allow specifying the AWS region for API requests while the ``region`` parameter is being transitioned (https://github.com/ansible-collections/amazon.aws/issues/2893).
- route53 - refactored module utility to use decorator-based error handling. (https://github.com/ansible-collections/amazon.aws/pull/2892)
- route53_health_check - refactored module to improve testability and type safety. (https://github.com/ansible-collections/amazon.aws/pull/2892)
- s3_bucket - refactored to use centralized S3 wrapper functions from module_utils and consistently use S3ErrorHandler (https://github.com/ansible-collections/amazon.aws/pull/2782).
- s3_bucket_info - refactored to use centralized S3 wrapper functions from module_utils and consistently use S3ErrorHandler (https://github.com/ansible-collections/amazon.aws/pull/2782).
- s3_object - refactored to use centralized S3 wrapper functions from module_utils and consistently use S3ErrorHandler (https://github.com/ansible-collections/amazon.aws/pull/2782).
- s3_object_info - refactored to use centralized S3 wrapper functions from module_utils and consistently use S3ErrorHandler (https://github.com/ansible-collections/amazon.aws/pull/2782).
- sts_assume_role - improve error handling for ``MalformedPolicyDocument`` errors by providing a clearer error message when an invalid policy document is provided (https://github.com/ansible-collections/amazon.aws/pull/2778).

ansible.netcommon
~~~~~~~~~~~~~~~~~

- Exposes new libssh option to configure key_exchange_algorithms. This requires ansible-pylibssh v1.3.0 or higher.
- Option to use libssh as transport while using netconf, is added.
- The ssh-python module is needed, which will ensure libssh as transport for netconf operations. When use_libssh is enabled.

ansible.windows
~~~~~~~~~~~~~~~

- Add official support for Ansible 2.20
- PowerShell 7 - Add initial support for running modules against PowerShell 7 interpreters. Support for PowerShell 7 varies across each module, see module documentation for more information.
- ansible.windows.win_package - Add optional Authenticode signature validation for installer files via the new ``verify_signature`` parameter.
- win_environment - Add the return value ``env_values`` which is a copy of the existing ``values`` return value. The documentation for ``values`` has been removed to discourage use of that version due to the inability to use ``values`` with dot notation in a Jinja2 template due to the conflict with the Python ``values`` attribute.
- win_file - is aligned with ``ansible.builtin.file`` and now supports options ``access_time``, ``access_time_format``, ``modification_time``, and ``modification_time_format``. (https://github.com/ansible-collections/ansible.windows/issues/798)
- win_shell - Add ``cmd`` module option that can be used instead of the free form input. This aligns the options to the POSIX ``shell`` module.
- win_shell - Support using ``pwsh.exe`` as the executable in a mode similar to how ``powershell.exe`` is run.

cisco.aci
~~~~~~~~~

- Add contract_type option to aci_contract_subject_to_filter and aci_contract_subject.
- Add l3out, l3out_tenant, external_epg and redistribute options to aci_l4l7_device_selection_interface_context.
- Add normalize_payload_values option to aci_rest for Ansible Core 2.19 support.
- Add set_communities, set_as_path and set_policy_tag options to aci_tenant_action_rule_profile.

cisco.ios
~~~~~~~~~

- Adds a new Resource Module `ios_bfd_interfaces` to configure BFD on interfaces.
- Adds a new Resource Module `ios_bfd_templates` to configure BFD  using templates.
- ios_l2_interfaces - Added xconnect and encapsulation attributes for L2VPN pseudowire and MPLS services configuration.
- ios_l3_interfaces - Add support for 'redirects' and 'unreachables' attributes to configure ICMP redirect and unreachable messages.

cisco.meraki
~~~~~~~~~~~~

- Added new modules and action plugins for Cisco Umbrella account connect/disconnect, Wireless AutoRF (RRM) settings, third-party VPN peers, organization integrations, inventory EoX overview, network moves, SASE eligible networks, and wireless device provisioning deployments.
- Updated with v1.66.0 dashboard API, adding new plugins and fixing bugs.
- networks_wireless_settings: added multicast-to-unicast conversion support.
- organizations_inventory_devices_info: added eoxStatuses filtering and included EoX fields in returned inventory device data.

cisco.mso
~~~~~~~~~

- Add parent_type, node_id, path, port_channel, virtual_port_channel, encapsulation_type and encapsulation_value options to ndo_l3out_bgp_peer.
- Add ptp option to ndo_l3out_routed_interface and ndo_l3out_routed_sub_interface.
- Add support to deploy and undeploy non-schema templates in ndo_template_deploy (formerly ndo_schema_template_deploy).

cisco.nxos
~~~~~~~~~~

- Added alias for mode option as switchport_mode for nxos_l2_interfaces

cloudscale_ch.cloud
~~~~~~~~~~~~~~~~~~~

- Added missing param when creating a health monitor

community.aws
~~~~~~~~~~~~~

- cloudfront_distribution - Added ``elements`` key to ``active_trusted_signers`` (https://github.com/ansible-collections/community.aws/pull/2354).
- cloudfront_distribution - Added ``elements`` key to ``aliases`` (https://github.com/ansible-collections/community.aws/pull/2354).
- cloudfront_distribution - Added ``elements`` key to ``cache_behaviors.items.allowed_methods.cached_methods`` (https://github.com/ansible-collections/community.aws/pull/2354).
- cloudfront_distribution - Added ``elements`` key to ``cache_behaviors.items.allowed_methods`` (https://github.com/ansible-collections/community.aws/pull/2354).
- cloudfront_distribution - Added ``elements`` key to ``cache_behaviors.items.forwarded_values.cookies.whitelisted_names`` (https://github.com/ansible-collections/community.aws/pull/2354).
- cloudfront_distribution - Added ``elements`` key to ``cache_behaviors.items.forwarded_values.headers`` (https://github.com/ansible-collections/community.aws/pull/2354).
- cloudfront_distribution - Added ``elements`` key to ``cache_behaviors.items.forwarded_values.query_string_cache_keys`` (https://github.com/ansible-collections/community.aws/pull/2354).
- cloudfront_distribution - Added ``elements`` key to ``cache_behaviors.items.lambda_function_associations`` (https://github.com/ansible-collections/community.aws/pull/2354).
- cloudfront_distribution - Added ``elements`` key to ``cache_behaviors`` (https://github.com/ansible-collections/community.aws/pull/2354).
- cloudfront_distribution - Added ``elements`` key to ``custom_error_responses`` (https://github.com/ansible-collections/community.aws/pull/2354).
- cloudfront_distribution - Added ``elements`` key to ``default_cache_behavior.allowed_methods.cached_methods`` (https://github.com/ansible-collections/community.aws/pull/2354).
- cloudfront_distribution - Added ``elements`` key to ``default_cache_behavior.allowed_methods`` (https://github.com/ansible-collections/community.aws/pull/2354).
- cloudfront_distribution - Added ``elements`` key to ``default_cache_behavior.forwarded_values.cookies.whitelisted_names`` (https://github.com/ansible-collections/community.aws/pull/2354).
- cloudfront_distribution - Added ``elements`` key to ``default_cache_behavior.forwarded_values.headers`` (https://github.com/ansible-collections/community.aws/pull/2354).
- cloudfront_distribution - Added ``elements`` key to ``default_cache_behavior.forwarded_values.query_string_cache_keys`` (https://github.com/ansible-collections/community.aws/pull/2354).
- cloudfront_distribution - Added ``elements`` key to ``default_cache_behavior.lambda_function_associations`` (https://github.com/ansible-collections/community.aws/pull/2354).
- cloudfront_distribution - Added ``elements`` key to ``origins.items.custom_origin_config.origin_ssl_protocols`` (https://github.com/ansible-collections/community.aws/pull/2354).
- cloudfront_distribution - Added ``elements`` key to ``origins`` (https://github.com/ansible-collections/community.aws/pull/2354).
- cloudfront_distribution - Added ``elements`` key to ``restrictions.geo_restriction`` (https://github.com/ansible-collections/community.aws/pull/2354).
- cloudfront_distribution - move misplaced options out of ``forwarded_values`` ``suboptions``. (https://github.com/ansible-collections/community.aws/pull/2342).
- cloudfront_invalidation - Added ``elements`` key to ``invalidation.invalidation_batch.paths`` (https://github.com/ansible-collections/community.aws/pull/2354).

community.crypto
~~~~~~~~~~~~~~~~

- luks_device - add support for TPM2 enrollment using ``systemd-cryptsetup`` (https://github.com/ansible-collections/community.crypto/issues/850, https://github.com/ansible-collections/community.crypto/pull/972).
- luks_device - add support for keyslot priority (https://github.com/ansible-collections/community.crypto/issues/850, https://github.com/ansible-collections/community.crypto/pull/972).

community.dns
~~~~~~~~~~~~~

- Hetzner DNS modules and plugins - support the `new Hetzner DNS API <https://docs.hetzner.com/networking/dns/faq/beta/>`__ (https://github.com/ansible-collections/community.dns/pull/301).

community.docker
~~~~~~~~~~~~~~~~

- docker_compose_v2_pull - adds ``ignore_pull_failures`` parameter that passes ``--ignore-pull-failures`` to the ``docker compose pull`` call when set to ``true`` (https://github.com/ansible-collections/community.docker/pull/1248).

community.general
~~~~~~~~~~~~~~~~~

- ModuleHelper module utils - allow to ignore specific exceptions in ``module_fails_on_exception`` decorator (https://github.com/ansible-collections/community.general/pull/11488).
- The last code included in the collection that was licensed under the PSF 2.0 license was removed form the collection. This means that now all code is either GPLv3+ licensed, MIT licensed, or BSD-2-clause licensed (https://github.com/ansible-collections/community.general/pull/11232).
- _mount module utils - simplify return of boolean values in functions (https://github.com/ansible-collections/community.general/pull/11119).
- _stormssh module utils - fix cases of unused variables in loops (https://github.com/ansible-collections/community.general/pull/11115).
- a_module test plugin - add proper parameter checking and type hints (https://github.com/ansible-collections/community.general/pull/11167).
- aerospike_migrations - simplify return of boolean values in functions (https://github.com/ansible-collections/community.general/pull/11119).
- aix_filesystem - improve code by using native Python construct (https://github.com/ansible-collections/community.general/pull/11215).
- ali_instance - fix cases of unused variables in loops (https://github.com/ansible-collections/community.general/pull/11115).
- alicloud_ecs module utils - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11341).
- android_sdk - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11343).
- ansible_galaxy_install - add parameter ``executable`` (https://github.com/ansible-collections/community.general/issues/7261, https://github.com/ansible-collections/community.general/pull/11646).
- ansible_type plugin utils - add type hints (https://github.com/ansible-collections/community.general/pull/11167).
- ansible_type test plugin - add type hints (https://github.com/ansible-collections/community.general/pull/11167).
- api module utils - use Python-defined constants for HTTP return codes (https://github.com/ansible-collections/community.general/pull/11561).
- apk - simplify return of boolean values in functions (https://github.com/ansible-collections/community.general/pull/11119).
- apt_rpm - fix cases of unused variables in loops (https://github.com/ansible-collections/community.general/pull/11115).
- apt_rpm - simplify return of boolean values in functions (https://github.com/ansible-collections/community.general/pull/11119).
- archive - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11343).
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
- bitbucket module utils - use Python-defined constants for HTTP return codes (https://github.com/ansible-collections/community.general/pull/11561).
- bitbucket_access_key modules - replace ``%`` templating with f-strings or ``format()`` (https://github.com/ansible-collections/community.general/pull/11223).
- bitbucket_pipeline_key_pair modules - replace ``%`` templating with f-strings or ``format()`` (https://github.com/ansible-collections/community.general/pull/11223).
- bitbucket_pipeline_known_host - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11343).
- bitbucket_pipeline_known_host modules - replace ``%`` templating with f-strings or ``format()`` (https://github.com/ansible-collections/community.general/pull/11223).
- bitbucket_pipeline_variable modules - replace ``%`` templating with f-strings or ``format()`` (https://github.com/ansible-collections/community.general/pull/11223).
- btrfs module utils - make execution of external commands safer by passing arguments as list (https://github.com/ansible-collections/community.general/pull/11240).
- chef_databag lookup plugin - use ``raise ... from ...`` when passing on exceptions (https://github.com/ansible-collections/community.general/pull/11095).
- chroot connection plugin - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11341).
- chroot connection plugin - use ``raise ... from ...`` when passing on exceptions (https://github.com/ansible-collections/community.general/pull/11095).
- circonus_annotation - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11102).
- cloudflare_dns - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/1114).
- cmd_runner module utils - use ``raise ... from ...`` when passing on exceptions (https://github.com/ansible-collections/community.general/pull/11097).
- cobbler inventory plugin - fix cases of unused variables in loops (https://github.com/ansible-collections/community.general/pull/11115).
- cobbler inventory plugin - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11341).
- cobbler_sync - remove conditional code handling SSL for unsupported versions of Python (https://github.com/ansible-collections/community.general/pull/11078).
- cobbler_sync - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11105).
- cobbler_system - remove conditional code handling SSL for unsupported versions of Python (https://github.com/ansible-collections/community.general/pull/11078).
- cobbler_system - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11105).
- collection_version lookup plugin - use ``raise ... from ...`` when passing on exceptions (https://github.com/ansible-collections/community.general/pull/11095).
- composer - improve code by using native Python construct (https://github.com/ansible-collections/community.general/pull/11215).
- consul module utils - use Python-defined constants for HTTP return codes (https://github.com/ansible-collections/community.general/pull/11561, https://github.com/ansible-collections/community.general/pull/11573).
- consul_kv lookup plugin - use ``raise ... from ...`` when passing on exceptions (https://github.com/ansible-collections/community.general/pull/11095).
- copr - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11343).
- counter filter plugin - use ``raise ... from ...`` when passing on exceptions (https://github.com/ansible-collections/community.general/pull/11095).
- credstash lookup plugin - use ``raise ... from ...`` when passing on exceptions (https://github.com/ansible-collections/community.general/pull/11095).
- cronvar - simplify handling unknown exceptions (https://github.com/ansible-collections/community.general/pull/11340).
- cronvar - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11343).
- cronvar - use ``raise ... from ...`` when passing on exceptions (https://github.com/ansible-collections/community.general/pull/11097).
- crypttab - simplify return of boolean values in functions (https://github.com/ansible-collections/community.general/pull/11119).
- crypttab - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11343).
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
- deps module utils - change the internal representaion of dependency state (https://github.com/ansible-collections/community.general/pull/11242).
- deps module utils - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11112).
- dig lookup plugin - use ``raise ... from ...`` when passing on exceptions (https://github.com/ansible-collections/community.general/pull/11095).
- dimensiondata_network - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11102).
- dimensiondata_network modules - replace ``%`` templating with f-strings or ``format()`` (https://github.com/ansible-collections/community.general/pull/11223).
- dnf_config_manager - fix cases of unused variables in loops (https://github.com/ansible-collections/community.general/pull/11115).
- dnstxt lookup plugin - use ``raise ... from ...`` when passing on exceptions (https://github.com/ansible-collections/community.general/pull/11095).
- doas become plugin - add new option ``allow_pipelining`` to explicitly allow the use of pipelining with this plugin. This should only be set to ``true`` with ansible-core 2.19+ when ``doas`` does not require a password (https://github.com/ansible-collections/community.general/issues/11411, https://github.com/ansible-collections/community.general/pull/11481).
- dsv lookup plugin - use ``raise ... from ...`` when passing on exceptions (https://github.com/ansible-collections/community.general/pull/11095).
- elastic callback plugin - fix cases of unused variables in loops (https://github.com/ansible-collections/community.general/pull/11115).
- elasticsearch_plugin - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11343).
- etcd3 lookup plugin - use ``raise ... from ...`` when passing on exceptions (https://github.com/ansible-collections/community.general/pull/11095).
- exceptions module utils - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11112).
- filesize - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11104).
- filesize - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11106).
- flatpak - improve code by using native Python construct (https://github.com/ansible-collections/community.general/pull/11215).
- flatpak_remote - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11106).
- fqdn_valid test plugin - add proper parameter checking, and add type hints (https://github.com/ansible-collections/community.general/pull/11167).
- from_csv filter plugin - use ``raise ... from ...`` when passing on exceptions (https://github.com/ansible-collections/community.general/pull/11095).
- from_ini filter plugin - add ``delimiters`` parameter to allow correctly parsing more INI documents (https://github.com/ansible-collections/community.general/issues/11506, https://github.com/ansible-collections/community.general/pull/11512).
- from_ini filter plugin - use ``raise ... from ...`` when passing on exceptions (https://github.com/ansible-collections/community.general/pull/11095).
- gandi_livedns_api module utils - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11112).
- gandi_livedns_api module utils - use Python-defined constants for HTTP return codes (https://github.com/ansible-collections/community.general/pull/11561).
- github_app_access_token lookup plugin - use Python-defined constants for HTTP return codes (https://github.com/ansible-collections/community.general/pull/11561).
- github_app_access_token lookup plugin - use ``raise ... from ...`` when passing on exceptions (https://github.com/ansible-collections/community.general/pull/11095).
- gitlab_group - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11343).
- gitlab_group_access_token - simplify return of boolean values in functions (https://github.com/ansible-collections/community.general/pull/11119).
- gitlab_group_members - improve code by using native Python construct (https://github.com/ansible-collections/community.general/pull/11215).
- gitlab_issue - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11343).
- gitlab_merge_request - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11343).
- gitlab_project - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11343).
- gitlab_project_access_token - simplify return of boolean values in functions (https://github.com/ansible-collections/community.general/pull/11119).
- gitlab_project_members - improve code by using native Python construct (https://github.com/ansible-collections/community.general/pull/11215).
- gitlab_runner - allow maximum timeout to be disabled by passing ``0`` to ``maximum_timeout``  (https://github.com/ansible-collections/community.general/pull/11174).
- gitlab_runners inventory plugin - use ``raise ... from ...`` when passing on exceptions (https://github.com/ansible-collections/community.general/pull/11095).
- gunicorn - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11343).
- haproxy - fix cases of unused variables in loops (https://github.com/ansible-collections/community.general/pull/11115).
- hashids filter - replace ``%`` templating with f-strings or ``format()`` (https://github.com/ansible-collections/community.general/pull/11223).
- hashids filter plugin - use ``raise ... from ...`` when passing on exceptions (https://github.com/ansible-collections/community.general/pull/11095).
- hg - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11106).
- hg - simplify return of boolean values in functions (https://github.com/ansible-collections/community.general/pull/11119).
- hpilo_info - fix cases of unused variables in loops (https://github.com/ansible-collections/community.general/pull/11115).
- hpilo_info - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11098).
- htpasswd - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11098).
- htpasswd - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11343).
- hwc_ecs_instance - fix cases of unused variables in loops (https://github.com/ansible-collections/community.general/pull/11115).
- hwc_utils module utils - improve code by using native Python construct (https://github.com/ansible-collections/community.general/pull/11215).
- hwc_utils module utils - use Python-defined constants for HTTP return codes (https://github.com/ansible-collections/community.general/pull/11561, https://github.com/ansible-collections/community.general/pull/11573).
- hwc_utils module utils - use ``raise ... from ...`` when passing on exceptions (https://github.com/ansible-collections/community.general/pull/11097).
- hwc_vpc_port - fix cases of unused variables in loops (https://github.com/ansible-collections/community.general/pull/11115).
- ibm_sa_utils module utils - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11112).
- icinga2 inventory plugin - use Python-defined constants for HTTP return codes (https://github.com/ansible-collections/community.general/pull/11561, https://github.com/ansible-collections/community.general/pull/11573).
- icinga2 inventory plugin - use ``raise ... from ...`` when passing on exceptions (https://github.com/ansible-collections/community.general/pull/11095).
- icinga2_host - simplify return of boolean values in functions (https://github.com/ansible-collections/community.general/pull/11119).
- identity.keycloak.keycloak module utils - use ``raise ... from ...`` when passing on exceptions (https://github.com/ansible-collections/community.general/pull/11097).
- idrac_redfish_command - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11110).
- idrac_redfish_command - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/1114).
- idrac_redfish_config - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11098).
- idrac_redfish_config - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11102).
- idrac_redfish_config - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11110).
- idrac_redfish_config - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/1114).
- idrac_redfish_info - add multiple manager support to ``GetManagerAttributes`` command (https://github.com/ansible-collections/community.general/pull/11294).
- idrac_redfish_info - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11110).
- idrac_redfish_info - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/1114).
- ilo_redfish_command - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11110).
- ilo_redfish_command - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/1114).
- ilo_redfish_config - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11110).
- ilo_redfish_config - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/1114).
- imc_rest - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11343).
- imc_rest modules - replace ``%`` templating with f-strings or ``format()`` (https://github.com/ansible-collections/community.general/pull/11223).
- incus connection plugin - add support for Windows virtual machines (https://github.com/ansible-collections/community.general/pull/11199).
- incus connection plugin - improve code readability (https://github.com/ansible-collections/community.general/pull/11346).
- incus connection plugin - simplify regular expression matching commands (https://github.com/ansible-collections/community.general/pull/11347).
- incus inventory plugin - add support for constructing project-independent FQDNs (https://github.com/ansible-collections/community.general/pull/11555).
- influxdb_query - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11098).
- influxdb_user - fix cases of unused variables in loops (https://github.com/ansible-collections/community.general/pull/11115).
- influxdb_user - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11098).
- influxdb_write - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11098).
- ini_file - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11343).
- interfaces_file - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11343).
- iocage inventory plugin - fix cases of unused variables in loops (https://github.com/ansible-collections/community.general/pull/11115).
- ip_netns - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11104).
- ip_netns - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11105).
- ip_netns - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11106).
- ipa module utils - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11112).
- ipa module utils - use Python-defined constants for HTTP return codes (https://github.com/ansible-collections/community.general/pull/11561).
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
- iptables_state - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11343).
- iptables_state action plugin - add type hints (https://github.com/ansible-collections/community.general/pull/11167).
- iso_customize - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11106).
- jail connection plugin - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11341).
- jail connection plugin - use ``raise ... from ...`` when passing on exceptions (https://github.com/ansible-collections/community.general/pull/11095).
- jc filter plugin - use ``raise ... from ...`` when passing on exceptions (https://github.com/ansible-collections/community.general/pull/11095).
- jenkins_credential - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11343).
- jenkins_job - simplify return of boolean values in functions (https://github.com/ansible-collections/community.general/pull/11119).
- jenkins_job_info - remove conditional code handling SSL for unsupported versions of Python (https://github.com/ansible-collections/community.general/pull/11078).
- jenkins_plugin - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11102).
- jenkins_plugin - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/1114).
- jenkins_plugin - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11343).
- jenkins_plugin - use ``raise ... from ...`` when passing on exceptions (https://github.com/ansible-collections/community.general/pull/11097).
- jenkins_plugin modules - replace ``%`` templating with f-strings or ``format()`` (https://github.com/ansible-collections/community.general/pull/11223).
- jenkins_script - move ``import`` statemetns to the top of the file (https://github.com/ansible-collections/community.general/pull/11396).
- jenkins_script - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/1114).
- jira - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11104).
- jira - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/1114).
- jira - use ``raise ... from ...`` when passing on exceptions (https://github.com/ansible-collections/community.general/pull/11097).
- json_query filter plugin - use ``raise ... from ...`` when passing on exceptions (https://github.com/ansible-collections/community.general/pull/11095).
- kdeconfig - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11343).
- keycloak module utils - fix cases of unused variables in loops (https://github.com/ansible-collections/community.general/pull/11115).
- keycloak module utils - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11112).
- keycloak module utils - use Python-defined constants for HTTP return codes (https://github.com/ansible-collections/community.general/pull/11561).
- keycloak module_utils - replace ``%`` templating with f-strings or ``format()`` (https://github.com/ansible-collections/community.general/pull/11223).
- keycloak_authentication - fix cases of unused variables in loops (https://github.com/ansible-collections/community.general/pull/11115).
- keycloak_client - add ``valid_post_logout_redirect_uris`` option to configure post logout redirect URIs for a client, and ``backchannel_logout_url`` option to configure the backchannel logout URL for a client (https://github.com/ansible-collections/community.general/issues/6812, https://github.com/ansible-collections/community.general/issues/4892, https://github.com/ansible-collections/community.general/pull/11473).
- keycloak_client_rolemapping - fix cases of unused variables in loops (https://github.com/ansible-collections/community.general/pull/11115).
- keycloak_client_rolemapping, keycloak_realm_rolemapping, keycloak_group - optimize retrieval of groups by name to use Keycloak search API with exact matching instead of fetching all groups (https://github.com/ansible-collections/community.general/pull/11503).
- keycloak_component - fix cases of unused variables in loops (https://github.com/ansible-collections/community.general/pull/11115).
- keycloak_realm - add ``first_broker_login_flow`` parameter (https://github.com/ansible-collections/community.general/pull/11622).
- keycloak_realm - add ``webAuthnPolicyPasswordlessPasskeysEnabled`` parameter (https://github.com/ansible-collections/community.general/pull/11197).
- keycloak_realm - add support for ``localizationTexts`` option in Keycloak realms (https://github.com/ansible-collections/community.general/pull/11513).
- keycloak_realm_key - add support for auto-generated key providers (``rsa-generated``, ``rsa-enc-generated``, ``hmac-generated``, ``aes-generated``, ``ecdsa-generated``, ``ecdh-generated``, ``eddsa-generated``), ``java-keystore`` provider, additional algorithms (HMAC, ECDSA, ECDH, EdDSA, AES), and new config options (``secret_size``, ``key_size``, ``elliptic_curve``, ``keystore``, ``keystore_password``, ``key_alias``, ``key_password``). Also makes ``config.private_key`` and ``config.certificate`` optional as they are only required for imported key providers (https://github.com/ansible-collections/community.general/pull/11468).
- keycloak_realm_key - fix cases of unused variables in loops (https://github.com/ansible-collections/community.general/pull/11115).
- keycloak_realm_rolemapping - fix cases of unused variables in loops (https://github.com/ansible-collections/community.general/pull/11115).
- keycloak_user_rolemapping - fix cases of unused variables in loops (https://github.com/ansible-collections/community.general/pull/11115).
- keycloak_userprofile - add support for ``selector`` option (https://github.com/ansible-collections/community.general/pull/11309).
- keycloak_userprofile - add support for additional user profile attribute-validations available in Keycloak (https://github.com/ansible-collections/community.general/issues/9048, https://github.com/ansible-collections/community.general/pull/11285).
- keycloak_userprofile - fix cases of unused variables in loops (https://github.com/ansible-collections/community.general/pull/11115).
- keys_filter plugin_utils plugin - use ``raise ... from ...`` when passing on exceptions (https://github.com/ansible-collections/community.general/pull/11095).
- keys_filter.py plugin utils - add type hints (https://github.com/ansible-collections/community.general/pull/11167).
- known_hosts module utils - improve code by using native Python construct (https://github.com/ansible-collections/community.general/pull/11215).
- known_hosts module utils - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11341).
- layman - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11343).
- layman - use ``raise ... from ...`` when passing on exceptions (https://github.com/ansible-collections/community.general/pull/11097).
- ldap module utils - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11112).
- ldap_attrs - add ``binary_attributes`` and ``honor_binary`` parameters to handle binary attribute values (https://github.com/ansible-collections/community.general/pull/11558).
- ldap_attrs - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11102).
- ldap_entry - add ``binary_attributes`` and ``honor_binary`` parameters to handle creating objects with attributes set to binary values (https://github.com/ansible-collections/community.general/pull/11558).
- ldap_entry - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11102).
- ldap_inc - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11102).
- ldap_search - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11104).
- ldap_search - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11106).
- linode - move ``import`` statemetns to the top of the file (https://github.com/ansible-collections/community.general/pull/11396).
- linode inventory plugin - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11341).
- linode inventory plugin - use ``raise ... from ...`` when passing on exceptions (https://github.com/ansible-collections/community.general/pull/11095).
- listen_ports_facts - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11098).
- listen_ports_facts - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11343).
- listen_ports_facts - use ``raise ... from ...`` when passing on exceptions (https://github.com/ansible-collections/community.general/pull/11097).
- lmdb_kv lookup plugin - use ``raise ... from ...`` when passing on exceptions (https://github.com/ansible-collections/community.general/pull/11095).
- locale_gen - extend the search for available locales to include ``/usr/local/share/i18n/SUPPORTED`` in Debian and Ubuntu systems (https://github.com/ansible-collections/community.general/issues/10964, https://github.com/ansible-collections/community.general/pull/11046).
- locale_gen - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11343).
- logentries - simplify return of boolean values in functions (https://github.com/ansible-collections/community.general/pull/11119).
- logentries callback plugin - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11341).
- lookup plugin passwordstore - modernize internal ``check_output2()`` helper using ``subprocess.run()`` and rename it to ``run_backend_cmd()`` (https://github.com/ansible-collections/community.general/pull/11655).
- lvm_pv - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11343).
- lxc connection plugin - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11341).
- lxc connection plugin - use ``raise ... from ...`` when passing on exceptions (https://github.com/ansible-collections/community.general/pull/11095).
- lxc_container - refactor function ``create_script``, using ``subprocess.Popen()``, to a new module_utils ``_lxc`` (https://github.com/ansible-collections/community.general/pull/11204).
- lxc_container - use ``tempfile.TemporaryDirectory()`` instead of ``mkdtemp()`` (https://github.com/ansible-collections/community.general/pull/11323).
- lxd connection plugin - use ``raise ... from ...`` when passing on exceptions (https://github.com/ansible-collections/community.general/pull/11095).
- lxd inventory plugin - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11341).
- lxd inventory plugin - use ``raise ... from ...`` when passing on exceptions (https://github.com/ansible-collections/community.general/pull/11095).
- lxd module utils - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11112).
- lxd module utils - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11341).
- lxd module utils - use ``raise ... from ...`` when passing on exceptions (https://github.com/ansible-collections/community.general/pull/11097).
- lxd_container - improve code by using native Python construct (https://github.com/ansible-collections/community.general/pull/11215).
- macports - simplify return of boolean values in functions (https://github.com/ansible-collections/community.general/pull/11119).
- mail - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/1114).
- manageiq module utils - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11341).
- manageiq_alert_profiles - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11344).
- maven_artifact - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/1114).
- memset module utils - use Python-defined constants for HTTP return codes (https://github.com/ansible-collections/community.general/pull/11561).
- merge_variables - extend type detection failure message to allow users for easier failure debugging (https://github.com/ansible-collections/community.general/pull/11107).
- merge_variables lookup plugin - extended merging capabilities added (https://github.com/ansible-collections/community.general/pull/11536).
- merge_variables lookup plugin - simplify return of boolean values in functions (https://github.com/ansible-collections/community.general/pull/11119).
- modprobe - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11098).
- modprobe - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11344).
- monit - add ``monit_version`` return value also when the module has succeeded (https://github.com/ansible-collections/community.general/pull/11255).
- monit - use ``Enum`` to represent the possible states (https://github.com/ansible-collections/community.general/pull/11245).
- mssql_db - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11344).
- nagios - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11344).
- net_tools.pritunl.api module utils - use ``raise ... from ...`` when passing on exceptions (https://github.com/ansible-collections/community.general/pull/11097).
- netcup_dns - support diff mode (https://github.com/ansible-collections/community.general/pull/11376).
- nmap inventory plugin - use ``raise ... from ...`` when passing on exceptions (https://github.com/ansible-collections/community.general/pull/11095).
- nmcli - add idempotency check (https://github.com/ansible-collections/community.general/pull/11114).
- nmcli - add support for IPv6 routing rules (https://github.com/ansible-collections/community.general/issues/7094, https://github.com/ansible-collections/community.general/pull/11413).
- nmcli - fix cases of unused variables in loops (https://github.com/ansible-collections/community.general/pull/11115).
- nmcli - fix comparison of type (https://github.com/ansible-collections/community.general/pull/11121).
- nmcli - fix idempotency for MAC VLAN interfaces when using ``macvlan.tap`` (https://github.com/ansible-collections/community.general/pull/11551).
- nmcli module - add ``vxlan_parent`` option required for multicast ``vxlan_remote`` addresses; add ``vxlan`` to list of bridgeable devices (https://github.com/ansible-collections/community.general/pull/11182).
- nmcli modules - replace ``%`` templating with f-strings or ``format()`` (https://github.com/ansible-collections/community.general/pull/11223).
- nomad_job - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11098).
- nomad_job - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11106).
- nomad_job_info - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11098).
- nomad_token - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11098).
- nosh - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11106).
- nosh - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11344).
- nsupdate - add support for server FQDN and the GSS-TSIG key algorithm (https://github.com/ansible-collections/community.general/issues/5730, https://github.com/ansible-collections/community.general/pull/11425).
- nsupdate - replace ``list(map(...))`` constructs with Python comprehensions (https://github.com/ansible-collections/community.general/pull/11590).
- nsupdate modules plugin - replace aliased errors with proper Python error (https://github.com/ansible-collections/community.general/pull/11391).
- ocapi_command - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11106).
- ocapi_command - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11110).
- ocapi_info - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11106).
- ocapi_utils module utils - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11112).
- ocapi_utils module utils - use Python-defined constants for HTTP return codes (https://github.com/ansible-collections/community.general/pull/11561).
- oci_utils module utils - improve code by using native Python construct (https://github.com/ansible-collections/community.general/pull/11215).
- oci_utils module utils - improve templating of strings (https://github.com/ansible-collections/community.general/pull/11189).
- oci_utils module utils - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11341).
- oci_utils module utils - use Python-defined constants for HTTP return codes (https://github.com/ansible-collections/community.general/pull/11561).
- omapi_host - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11344).
- one_image - move ``import`` statemetns to the top of the file (https://github.com/ansible-collections/community.general/pull/11396).
- one_image_info - move ``import`` statemetns to the top of the file (https://github.com/ansible-collections/community.general/pull/11396).
- one_service - move ``import`` statemetns to the top of the file (https://github.com/ansible-collections/community.general/pull/11396).
- one_vm - move ``import`` statemetns to the top of the file (https://github.com/ansible-collections/community.general/pull/11396).
- one_vm - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11344).
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
- online module utils - use Python-defined constants for HTTP return codes (https://github.com/ansible-collections/community.general/pull/11561).
- opennebula inventory plugin - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11341).
- opennebula inventory plugin - use ``raise ... from ...`` when passing on exceptions (https://github.com/ansible-collections/community.general/pull/11095).
- opentelemetry callback plugin - fix cases of unused variables in loops (https://github.com/ansible-collections/community.general/pull/11115).
- osx_defaults - add support for ``dict`` type values, including ``dict_mode`` option to merge keys into an existing dictionary (https://github.com/ansible-collections/community.general/issues/238, https://github.com/ansible-collections/community.general/pull/11659).
- osx_defaults - use ``raise ... from ...`` when passing on exceptions (https://github.com/ansible-collections/community.general/pull/11097).
- packet_device - replace ``%`` templating with f-strings or ``format()`` (https://github.com/ansible-collections/community.general/pull/11231).
- packet_device modules - mark ``%`` templating as ``noqa`` (https://github.com/ansible-collections/community.general/pull/11223).
- packet_ip_subnet - use ``raise ... from ...`` when passing on exceptions (https://github.com/ansible-collections/community.general/pull/11097).
- packet_project - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11106).
- packet_sshkey - use ``raise ... from ...`` when passing on exceptions (https://github.com/ansible-collections/community.general/pull/11097).
- packet_volume - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11106).
- packet_volume - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/1114).
- pam_limits - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11344).
- pamd - simplify return of boolean values in functions (https://github.com/ansible-collections/community.general/pull/11119).
- pamd - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11344).
- parted - simplify return of boolean values in functions (https://github.com/ansible-collections/community.general/pull/11119).
- parted - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11344).
- passwordstore lookup plugin - use ``raise ... from ...`` when passing on exceptions (https://github.com/ansible-collections/community.general/pull/11095).
- pear - fix cases of unused variables in loops (https://github.com/ansible-collections/community.general/pull/11115).
- pids - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11098).
- pids - use ``raise ... from ...`` when passing on exceptions (https://github.com/ansible-collections/community.general/pull/11097).
- pmem - simplify text tests without using regular expression (https://github.com/ansible-collections/community.general/pull/11388).
- portage - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11106).
- pritunl_org - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11098).
- pritunl_org_info - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11098).
- pritunl_user - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11098).
- pritunl_user_info - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11098).
- pubnub_blocks - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11344).
- pulp_repo - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11344).
- pushbullet modules - replace ``%`` templating with f-strings or ``format()`` (https://github.com/ansible-collections/community.general/pull/11223).
- read_csv - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11098).
- read_csv - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11344).
- redfish_command - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11110).
- redfish_command - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/1114).
- redfish_config - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11110).
- redfish_config - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/1114).
- redfish_info - add Redfish Root data to results of successful ``CheckAvailability`` command (https://github.com/ansible-collections/community.general/pull/11504).
- redfish_utils module utils - adds support of ``@Redfish.Settings`` in ``ComputerSystem`` attributes for ``set_boot_override`` function (https://github.com/ansible-collections/community.general/issues/11297, https://github.com/ansible-collections/community.general/pull/11322).
- redfish_utils module utils - fix cases of unused variables in loops (https://github.com/ansible-collections/community.general/pull/11115).
- redfish_utils module utils - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11112).
- redfish_utils module utils - use Python-defined constants for HTTP return codes (https://github.com/ansible-collections/community.general/pull/11561, https://github.com/ansible-collections/community.general/pull/11573).
- redhat_subscription - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11106).
- redhat_subscription - simplify return of boolean values in functions (https://github.com/ansible-collections/community.general/pull/11119).
- redhat_subscription - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11344).
- redis cache plugin - use ``raise ... from ...`` when passing on exceptions (https://github.com/ansible-collections/community.general/pull/11095).
- redis lookup plugin - use ``raise ... from ...`` when passing on exceptions (https://github.com/ansible-collections/community.general/pull/11095).
- revbitspss lookup plugin - use ``raise ... from ...`` when passing on exceptions (https://github.com/ansible-collections/community.general/pull/11095).
- rhevm - use ``raise ... from ...`` when passing on exceptions (https://github.com/ansible-collections/community.general/pull/11097).
- rhsm_repository - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11344).
- riak - simplify return of boolean values in functions (https://github.com/ansible-collections/community.general/pull/11119).
- rundeck module utils - improve handling the return value ``exception``. It now contains the full stack trace of the exception, while the message is included in ``msg`` (https://github.com/ansible-collections/community.general/pull/11149).
- rundeck module utils - use Python-defined constants for HTTP return codes (https://github.com/ansible-collections/community.general/pull/11561, https://github.com/ansible-collections/community.general/pull/11573).
- runit - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11344).
- scaleway inventory plugin - added support for ``SCW_PROFILE`` environment variable for the ``scw_profile`` option (https://github.com/ansible-collections/community.general/issues/11310, https://github.com/ansible-collections/community.general/pull/11311).
- scaleway inventory plugin - use ``raise ... from ...`` when passing on exceptions (https://github.com/ansible-collections/community.general/pull/11095).
- scaleway module utils - added ``scw_profile`` parameter with ``SCW_PROFILE`` environment variable support (https://github.com/ansible-collections/community.general/issues/11313, https://github.com/ansible-collections/community.general/pull/11314).
- scaleway module utils - use Python-defined constants for HTTP return codes (https://github.com/ansible-collections/community.general/pull/11561).
- scaleway_ip - added ``project`` parameter (https://github.com/ansible-collections/community.general/issues/11367, https://github.com/ansible-collections/community.general/pull/11368).
- scaleway_security_group - added ``project`` parameter (https://github.com/ansible-collections/community.general/issues/11364, https://github.com/ansible-collections/community.general/pull/11366).
- scaleway_user_data modules - replace ``%`` templating with f-strings or ``format()`` (https://github.com/ansible-collections/community.general/pull/11223).
- selinux_permissive - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11098).
- sensu_check - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11098).
- sensu_check - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11344).
- sensu_client - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11344).
- sensu_handler - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11344).
- sensu_silence - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/1114).
- sensu_silence modules - replace ``%`` templating with f-strings or ``format()`` (https://github.com/ansible-collections/community.general/pull/11223).
- sensu_subscription - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11098).
- sensu_subscription - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11102).
- sensu_subscription - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11344).
- seport - adds support for DCCP and SCTP protocols (https://github.com/ansible-collections/community.general/pull/11486).
- seport - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11344).
- serverless - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11344).
- shelvefile lookup plugin - use ``raise ... from ...`` when passing on exceptions (https://github.com/ansible-collections/community.general/pull/11095).
- shutdown action plugin - add type hints (https://github.com/ansible-collections/community.general/pull/11167).
- shutdown action plugin - use ``raise ... from ...`` when passing on exceptions (https://github.com/ansible-collections/community.general/pull/11095).
- slack - simplify return of boolean values in functions (https://github.com/ansible-collections/community.general/pull/11119).
- slackpkg - refactor function ``query_packages()`` (https://github.com/ansible-collections/community.general/pull/11390).
- slackpkg - simplify return of boolean values in functions (https://github.com/ansible-collections/community.general/pull/11119).
- snap - improve templating of strings (https://github.com/ansible-collections/community.general/pull/11189).
- snmp_facts - simplify and improve code using standard Ansible validations (https://github.com/ansible-collections/community.general/pull/11148).
- solaris_zone - execute external commands using Ansible construct (https://github.com/ansible-collections/community.general/pull/11192).
- solaris_zone - simplify return of boolean values in functions (https://github.com/ansible-collections/community.general/pull/11119).
- solaris_zone - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11344).
- sorcery - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11344).
- spectrum_model_attrs - convert ``%`` templating to f-string (https://github.com/ansible-collections/community.general/pull/11229).
- spotinst_aws_elastigroup - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11344).
- statusio_maintenance - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11102).
- sudoers - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11098).
- sudoers - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11344).
- supervisorctl - added an additional condition for generating the error 'no such process' (https://github.com/ansible-collections/community.general/issues/11621, https://github.com/ansible-collections/community.general/pull/11632).
- svc - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/1114).
- svc - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11344).
- svr4pkg - simplify return of boolean values in functions (https://github.com/ansible-collections/community.general/pull/11119).
- swupd - simplify return of boolean values in functions (https://github.com/ansible-collections/community.general/pull/11119).
- timestamp callback plugin - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11341).
- timezone - replace ``list(map(...))`` constructs with Python comprehensions (https://github.com/ansible-collections/community.general/pull/11590).
- timezone - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11344).
- to_ini filter plugin - use ``raise ... from ...`` when passing on exceptions (https://github.com/ansible-collections/community.general/pull/11095).
- tss lookup plugin - use ``raise ... from ...`` when passing on exceptions (https://github.com/ansible-collections/community.general/pull/11095).
- univention_umc module utils - update code to Python 3 (https://github.com/ansible-collections/community.general/pull/11122).
- univention_umc module utils - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11341).
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
- utm_utils module utils - use Python-defined constants for HTTP return codes (https://github.com/ansible-collections/community.general/pull/11561, https://github.com/ansible-collections/community.general/pull/11573).
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
- wakeonlan - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11344).
- wdc_redfish_command - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11110).
- wdc_redfish_command - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/1114).
- wdc_redfish_info - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11110).
- wdc_redfish_info - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/1114).
- wsl connection plugin - add option ``wsl_remote_ssh_shell_type``. Support PowerShell in addition to cmd as the Windows shell (https://github.com/ansible-collections/community.general/issues/11307, https://github.com/ansible-collections/community.general/pull/11308).
- wsl connection plugin - adjust variable name for integration tests (https://github.com/ansible-collections/community.general/pull/11190).
- wsl connection plugin - fix cases of unused variables in loops (https://github.com/ansible-collections/community.general/pull/11115).
- wsl connection plugin - replace aliased errors with proper Python error (https://github.com/ansible-collections/community.general/pull/11391).
- wsl connection plugin - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11341).
- wsl connection plugin - use ``raise ... from ...`` when passing on exceptions (https://github.com/ansible-collections/community.general/pull/11095).
- xbps - fix cases of unused variables in loops (https://github.com/ansible-collections/community.general/pull/11115).
- xbps - simplify return of boolean values in functions (https://github.com/ansible-collections/community.general/pull/11119).
- xcc_redfish_command - fix cases of unused variables in loops (https://github.com/ansible-collections/community.general/pull/11115).
- xcc_redfish_command - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11110).
- xcc_redfish_command - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/1114).
- xenserver module utils - improve code by using native Python construct (https://github.com/ansible-collections/community.general/pull/11215).
- xenserver module utils - simplify return of boolean values in functions (https://github.com/ansible-collections/community.general/pull/11119).
- xenserver_guest modules - replace ``%`` templating with f-strings or ``format()`` (https://github.com/ansible-collections/community.general/pull/11223).
- xfs_quota - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11344).
- xml - remove redundant conversions to unicode (https://github.com/ansible-collections/community.general/pull/11106).
- xml - simplify return of boolean values in functions (https://github.com/ansible-collections/community.general/pull/11119).
- yaml cache plugin - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11341).
- yum_versionlock - remove redundant conversion to unicode in command output (https://github.com/ansible-collections/community.general/pull/11093).
- zfs - simplify return of boolean values in functions (https://github.com/ansible-collections/community.general/pull/11119).
- zone connection plugin - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11341).
- zone connection plugin - use ``raise ... from ...`` when passing on exceptions (https://github.com/ansible-collections/community.general/pull/11095).
- zypper - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11344).
- zypper_repository - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11344).

community.libvirt
~~~~~~~~~~~~~~~~~

- virt_cloud_instance - added commands return field to provide visibility into executed commands during VM provisioning.
- virt_install - added commands return field to provide visibility into executed commands during VM provisioning.
- virt_install - added support for memoryBacking source type configuration, including memfd for shared memory (https://github.com/ansible-collections/community.libvirt/issues/228).
- virt_install - added support for primary value attribute (_value or value) in dynamic dict options that require a primary value alongside additional attributes.
- virt_install - enhanced cloud_init configuration handling for sub-options (meta-data, user-data, and network-config) to support both string and dictionary inputs.
- virt_install - refactored common virt-install functionality into module_utils and doc_fragments to enable code reuse between modules.
- virt_volume - New return key/value pairs 'Type', 'Capacity' and 'Allocation' were added to command 'list_volumes' (https://github.com/ansible-collections/community.libvirt/issues/187)
- virt_volume - added ability to resize volumes if defined capacity is different. If volume already exists and defined capacity in XML differs a resize is attempted.

community.mysql
~~~~~~~~~~~~~~~

- Update imports from ansible.module_utils._text to use ansible.module_utils.common.text.converters
- mysql_role - add ``sql_log_bin`` option to disable binary logging for the connection (https://github.com/ansible-collections/community.mysql/issues/742).

community.postgresql
~~~~~~~~~~~~~~~~~~~~

- postgresql_privs - support MAINTAIN privilege on tables (added in PostgreSQL 17) (https://github.com/ansible-collections/community.postgresql/pull/888).

community.proxmox
~~~~~~~~~~~~~~~~~

- inventory plugin - add want_post_filtering_facts to delay fact gathering until filtering has completed (https://github.com/ansible-collections/community.proxmox/pull/261).
- inventory plugin, plugin_utils - replace deprecated ``ansible.module_utils.common._collections_compat`` imports with ``collections.abc`` from the Python standard library (https://github.com/ansible-collections/community.proxmox/issues/241).
- proxmox - Add api_timeout option for all modules (https://github.com/ansible-collections/community.proxmox/pull/253).
- proxmox - add ``totp`` authentification support (https://github.com/ansible-collections/community.proxmox/pull/265).
- proxmox - add a new helper `create_proxmox_module()` which adds generic auth args and constraints, and merges in the module-specific args and options (https://github.com/ansible-collections/community.proxmox/pull/289).
- proxmox - change disk size units to GiB (https://github.com/ansible-collections/community.proxmox/pull/236).
- proxmox - set ``state`` as not ``required`` and set default value ``present`` (https://github.com/ansible-collections/community.proxmox/pull/292).
- proxmox - update ``proxmoxer`` required dependencies to ``>=2.3`` (https://github.com/ansible-collections/community.proxmox/pull/265).
- proxmox_disk - change disk size units to GiB (https://github.com/ansible-collections/community.proxmox/pull/236).
- proxmox_kvm - add option to migrate local disks as well (https://github.com/ansible-collections/community.proxmox/pull/240).
- proxmox_kvm - add qemu parameter ``spice_enhancements`` (https://github.com/ansible-collections/community.proxmox/pull/324).
- proxmox_kvm - add qemu parameter ``virtiofs`` (https://github.com/ansible-collections/community.proxmox/pull/336).
- proxmox_kvm - change disk size units to GiB (https://github.com/ansible-collections/community.proxmox/pull/236).
- proxmox_node - add alias ``certificate_file_path`` for ``cert`` (https://github.com/ansible-collections/community.proxmox/pull/331).
- proxmox_node - add alias ``node`` for ``node_name`` (https://github.com/ansible-collections/community.proxmox/pull/331).
- proxmox_node - add alias ``private_key_file_path`` for ``key`` (https://github.com/ansible-collections/community.proxmox/pull/331).
- proxmox_node - add new parameter ``certificate`` to pass raw PEM encoded certificate (https://github.com/ansible-collections/community.proxmox/pull/331).
- proxmox_node - add new parameter ``private_key`` to pass raw PEM encoded private key (https://github.com/ansible-collections/community.proxmox/pull/331).
- proxmox_node_info - add information on node network interfaces to node information output (https://github.com/ansible-collections/community.proxmox/pull/220).
- proxmox_node_info - add information on node's PVE version (https://github.com/ansible-collections/community.proxmox/pull/225).
- proxmox_role - add role's privs on the return data (https://github.com/ansible-collections/community.proxmox/pull/283).
- proxmox_snap_info - Adds a new module to list snapshots or a specific snapshot for VM or container (https://github.com/ansible-collections/community.proxmox/issues/229).
- proxmox_storage - Add support for RBD (RADOS Block Device) storage (https://github.com/ansible-collections/community.proxmox/issues/329).
- proxmox_storage - Add support for ZFS thin-provisioning (https://github.com/ansible-collections/community.proxmox/pull/265).
- proxmox_storage - Add the option namespace for PBS storage (https://github.com/ansible-collections/community.proxmox/pull/282)
- proxmox_storage - add feature of subdirectory in CIFS share. (https://github.com/ansible-collections/community.proxmox/pull/214).
- proxmox_storage - enhanced error handling and parameters validation (https://github.com/ansible-collections/community.proxmox/pull/305).
- proxmox_storage - fix passing nfs_options to API payload (https://github.com/ansible-collections/community.proxmox/issues/203, https://github.com/ansible-collections/community.proxmox/pull/221).
- proxmox_storage - fixed CIFS authentication by sending username and password parameters to proxmoxer (https://github.com/ansible-collections/community.proxmox/pull/214).
- proxmox_storage - refactor the validation of storage options (https://github.com/ansible-collections/community.proxmox/pull/266).
- proxmox_storage - the parameter ``state`` now has a default value of ``present`` (https://github.com/ansible-collections/community.proxmox/pull/305).
- proxmox_storage - when ``state=present`` parameters ``content`` and ``nodes`` are now not required (https://github.com/ansible-collections/community.proxmox/pull/315).
- proxmox_storage_contents_info - Add support for content type ``import`` (https://github.com/ansible-collections/community.proxmox/pull/260).
- proxmox_zone, proxmox_vnet, proxmox_subnet - make sdn modules compatible with pve8 (https://github.com/ansible-collections/community.proxmox/pull/254).

community.routeros
~~~~~~~~~~~~~~~~~~

- api_info - adds support for the ``app`` path for RouterOS >= 7.21 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info - adds support for the ``caps-man actual-interface-configuration`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info - adds support for the ``disk btrfs filesystem`` path for RouterOS >=7.18 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info - adds support for the ``dude ros health`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info - adds support for the ``dude ros interface`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info - adds support for the ``dude ros neighbor`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info - adds support for the ``dude ros resource`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info - adds support for the ``dude ros routerboard`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info - adds support for the ``interface bridge port-controller port`` path for RouterOS >= 7.15, < 7.18 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info - adds support for the ``interface ethernet switch qos port`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/issues/319, https://github.com/ansible-collections/community.routeros/pull/433).
- api_info - adds support for the ``interface ethernet switch qos tx-manager queue`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/issues/319, https://github.com/ansible-collections/community.routeros/pull/433).
- api_info - adds support for the ``interface lte`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/issues/282, https://github.com/ansible-collections/community.routeros/pull/433).
- api_info - adds support for the ``interface wifi steering neighbor-group`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info - adds support for the ``interface wireless manual-tx-power-table`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info - adds support for the ``interface wireless nstreme`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info - adds support for the ``interface`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info - adds support for the ``iot bluetooth advertisers`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info - adds support for the ``iot bluetooth peripheral-devices`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info - adds support for the ``iot bluetooth scanners`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info - adds support for the ``iot bluetooth`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info - adds support for the ``iot lora channels`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info - adds support for the ``iot lora radios`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info - adds support for the ``iot lora`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info - adds support for the ``ip ipsec key`` path for RouterOS >= 7.15, < 7.20 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info - adds support for the ``ip pool used`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info - adds support for the ``ip proxy connections`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info - adds support for the ``ip socks connections`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info - adds support for the ``lcd screen`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info - adds support for the ``lora channels`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info - adds support for the ``lora radios`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info - adds support for the ``lora`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info - adds support for the ``partitions`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info - adds support for the ``port`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info - adds support for the ``routing isis interface`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/issues/356, https://github.com/ansible-collections/community.routeros/pull/433).
- api_info - adds support for the ``routing isis lsp`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/issues/356, https://github.com/ansible-collections/community.routeros/pull/433).
- api_info - adds support for the ``routing isis neighbor`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/issues/356, https://github.com/ansible-collections/community.routeros/pull/433).
- api_info - adds support for the ``routing ospf neighbor`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info - adds support for the ``routing pimsm igmp-interface-template`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info - adds support for the ``routing route rule`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info - adds support for the ``routing route`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info - adds support for the ``system package local-update`` path for RouterOS >= 7.17 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info - adds support for the ``system routerboard usb`` path for RouterOS >= 7.15, < 7.20 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info - adds support for the ``system script environment`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info - adds support for the ``system script job`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info - adds support for the ``system upgrade`` path for RouterOS >= 7.15, < 7.17 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - add ``2g-probe-delay`` field to path ``interface wifi steering`` (https://github.com/ansible-collections/community.routeros/pull/428).
- api_info, api_modify - add ``aaa.*``, ``channel.*``, ``datapath.*``, ``interworking.*``, ``security.*``, ``steering.*`` sub-fields to path ``interface wifi configuration`` (https://github.com/ansible-collections/community.routeros/pull/428).
- api_info, api_modify - add ``deprioritize-unii-3-4``, ``reselect-interval``, ``reselect-time`` fields to path ``interface wifi channel`` (https://github.com/ansible-collections/community.routeros/pull/428).
- api_info, api_modify - add ``multi-passphrase-group`` field to path ``interface wifi security`` (https://github.com/ansible-collections/community.routeros/pull/428).
- api_info, api_modify - add ``prefix-pool`` field to and fix default of ``address-pool`` for ``ipv6 dhcp-server`` path (https://github.com/ansible-collections/community.routeros/pull/430).
- api_info, api_modify - add ``send-email-from``, ``send-email-to`` and ``send-smtp-server`` to ``system watchdog`` (https://github.com/ansible-collections/community.routeros/pull/429).
- api_info, api_modify - add ``traffic-processing`` field to path ``interface wifi datapath`` and ``interface wifi configuration`` (https://github.com/ansible-collections/community.routeros/pull/424).
- api_info, api_modify - add ``use-bfd`` to ``routing ospf interface-template`` path (https://github.com/ansible-collections/community.routeros/pull/425).
- api_info, api_modify - add ``vrf`` to ``ip service`` (https://github.com/ansible-collections/community.routeros/pull/426).
- api_info, api_modify - add default values for fields ``ciphers`` in ``ip ssh``, ``mvrp`` in  ``interface vlan``, and ``mvrp-forbidden`` in ``interface bridge vlan`` (https://github.com/ansible-collections/community.routeros/pull/439/).
- api_info, api_modify - add missing attribute ``radsec-timeout`` for the ``radius`` path which exists since RouterOS version 7.19.6 (https://github.com/ansible-collections/community.routeros/pull/412).
- api_info, api_modify - add missing parameters to path ``interface bridge`` and ``interface bridge port`` (https://github.com/ansible-collections/community.routeros/pull/423).
- api_info, api_modify - add support for path ``disk settings`` (https://github.com/ansible-collections/community.routeros/pull/422).
- api_info, api_modify - add support for path ``interface dot1x client`` (https://github.com/ansible-collections/community.routeros/pull/414).
- api_info, api_modify - add support for path ``interface dot1x server`` (https://github.com/ansible-collections/community.routeros/pull/413).
- api_info, api_modify - add support for path ``ip socks access`` (https://github.com/ansible-collections/community.routeros/pull/431).
- api_info, api_modify - add support for paths ``ip hotspot``, ``ip hotspot profile``, ``ip hotspot user``, ``ip hotspot user profile``, ``ip hotspot walled-garden``, and ``ip hotspot walled-garden ip`` (https://github.com/ansible-collections/community.routeros/pull/418).
- api_info, api_modify - adds default value and removes required being true for parameter ``address-pool`` in the ``ipv6 dhcp-server`` path (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the  ``lacp-mode`` (>= 7.19), ``lacp-system-id`` (>= 7.21) and ``lacp-system-priority`` (>= 7.21) parameters in the ``interface bonding`` path (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``3gpp-info-raw`` (>= 7.21), and ``realms-raw`` (>= 7.21) parameters in the ``interface wifi interworking`` path (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``accept-prefix-without-address`` (>= 7.20), ``allow-reconfigure`` (>= 7.17), ``check-gateway`` (>= 7.19), ``custom-iana-id`` (>= 7.20), ``custom-iapd-id`` (>= 7.20), ``default-route-tables`` (>= 7.19), ``prefix-address-lists`` (>= 7.17) and ``rapid-commit`` (>= 7.17) parameters in the ``ipv6 dhcp-client`` path (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``accept-proto-version``, ``accept-pseudowire-type``, ``l2tpv3-circuit-id``, ``l2tpv3-cookie-length``, ``l2tpv3-digest-hash`` and ``l2tpv3-ether-interface-list`` parameters in the ``interface l2tp-server server`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``accept-router-advertisements-on`` parameters in the ``ipv6 settings`` path for RouterOS >= 7.21 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``accept-untagged`` (>= 7.20), and ``pppoe-over-vlan-range`` (>= 7.17) parameters in the ``interface pppoe-server server`` path (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``add-arp`` (>= 7.15), ``address-lists`` (>= 7.17) and ``use-reconfigure`` (>= 7.19) parameters in the ``ip dhcp-server`` path (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``address-list-extra-time`` and ``vrf`` parameters in the ``ip dns`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``address-lists`` (>= 7.17), ``ignore-ia-na-bindings`` (>= 7.20), ``prefix-pool`` (>= 7.17) and ``use-reconfigure`` (>= 7.17) parameters in the ``ipv6 dhcp-server`` path (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``agent-circuit-id`` and ``agent-remote-id`` parameters in the ``ip dhcp-server lease`` path for RouterOS >= 7.21 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``allow-dual-stack-queue``, ``block-access``, ``dhcp-option-set``, ``lease-time``, ``parent-queue``, ``queue-type``, ``rate-limit``, ``routes`` and ``use-src-mac`` parameters in the ``ip dhcp-server lease`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``allow-reconfigure`` (>= 7.19), ``check-gateway`` (>= 7.19), ``default-route-tables`` (>= 7.18), ``dscp`` (>= 7.20), ``use-broadcast`` (>= 7.20) and ``vlan-priority`` (>= 7.20) parameters in the ``ip dhcp-client`` path (https://github.com/ansible-collections/community.routeros/issues/407, https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``allowed-addresses4`` and ``allowed-addresses6`` parameters in the ``tool bandwidth-server`` path for RouterOS >= 7.18 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``app settings`` path for RouterOS >= 7.21 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``authentication``, ``comment``, ``ip-type``, ``ipv6-interface``, ``passthrough-interface``, ``passthrough-mac``, ``passthrough-subnet-size``, ``password``, ``use-network-apn`` and ``user`` parameters in the ``interface lte apn`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/issues/282, https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``auto-link-local`` parameter in the ``ipv6 address`` path for RouterOS >= 7.18 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``back-to-home-vpn`` and ``vpn-prefer-relay-code`` parameters in the ``ip cloud`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``beacon-protection`` parameter in the ``interface wifi security`` path for RouterOS >= 7.21 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``boot-os``, ``cpu-mode``, ``disable-pci``, ``etherboot-port``, ``gpio-function``, ``init-delay`` and ``regulatory-domain-ce`` parameters in the ``system routerboard settings`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``bridge-port-trusted`` (>= 7.17), ``bridge-port-vid`` (>= 7.217), ``comment`` (>= 7.15), ``dhcpv6-lease-time`` (>= 7.20), ``dhcpv6-pd-pool (>= 7.15)``, ``dhcpv6-use-radius`` (>= 7.20), ``remote-ipv6-prefix-pool`` (>= 7.15) and ``remote-ipv6-prefix-reuse`` (>= 7.20) parameters in the ``ppp profile`` path (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``broadcast`` and ``netmask`` parameters in the ``ip address`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``builtin-trust-anchors`` (>= 7.19) and ``builtin-trust-store`` (>= 7.21) parameters in the ``certificate settings`` path (https://github.com/ansible-collections/community.routeros/issues/379, https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``burst-time``, ``prism-cardtype``, ``vht-basic-mcs`` and ``vht-supported-mcs`` parameters in the ``interface wireless`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``cable-settings`` (>= 7.15.3), ``disable-running-check`` (>= 7.15.3), ``numbers`` (>= 7.15), ``sfp-ignore-rx-los`` (>= 7.15) parameters in the ``interface ethernet`` path (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``caps-man interface`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``caps-man rates`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``certificate crl`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``certificate scep-server ra`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``certificate scep-server`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``certificate-verification`` parameters in the ``tool e-mail`` path for RouterOS >= 7.21 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``certificate`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``certificate``, ``enable-tun-ipv6``, ``ipv6-prefix-len``, ``push-routes``, ``redirect-gateway``, ``reneg-sec``, ``tls-version`` and ``certtun-server-ipv6ificate`` parameters in the ``interface ovpn-server server`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``channel.deprioritize-unii-3-4`` (>= 7.20), ``channel.reselect-interval`` (>= 7.15), ``channel.reselect-time`` (>= 7.19), ``configuration.distance`` (>= 7.15), ``configuration.installation`` (>= 7.17), ``configuration.max-clients`` (>=7.18), ``configuration.station-roaming`` (>= 7.17), ``configuration.tx-chains`` (>= 7.15), ``datapath.openflow-switch`` (>= 7.20), ``security.multi-passphrase-group`` (>= 7.17) and ``steering.2g-probe-delay`` (>=7.18) parameters in the ``interface wifi`` path (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``ciphers`` parameter in the ``ip ssh`` path for RouterOS >= 7.17 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``ciphers`` parameters in the ``interface sstp-server server`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``client-address``, ``client-dns``, ``client-endpoint``, ``client-keepalive``, ``client-listen-port``, and ``private-key`` parameters in the ``interface wireguard peers`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``client-allowed-address`` parameter in the ``interface wireguard peers`` path for RouterOS >= 7.21 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``comment`` and ``pref64`` parameters in the ``ipv6 nd`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``comment`` parameter in the ``interface wireless security-profiles`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/issues/388, https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``comment`` parameter in the ``ip dhcp-client option`` path for RouterOS >= 7.16 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``comment`` parameter in the ``ip ipsec policy group`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``comment`` parameter in the ``ip ipsec proposal`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``comment`` parameter in the ``ip smb users`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``comment`` parameter in the ``ipv6 dhcp-server option`` path for RouterOS >= 7.16 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``comment`` parameter in the ``port remote-access`` path for RouterOS >= 7.21 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``comment`` parameter in the ``ppp secret`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``comment`` parameter in the ``tool romon port`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``configuration.hw-protection-mode``, ``interworking.3gpp-info-raw``, ``interworking.realms-raw``, ``security.beacon-protection``, ``steering.transition-request-count``, ``steering.transition-request-period``, ``steering.transition-threshold``, ``steering.transition-threshold-time`` and ``steering.transition-time`` parameters in the ``interface wifi`` path for RouterOS >= 7.21 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``connection-mark`` and ``use-responder-dns`` parameters in the ``ip ipsec mode-config`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``connection-nat-state`` parameter in the ``ipv6 firewall mangle`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``connection-nat-state``, ``routing-mark`` and ``tls-host`` parameters in the ``ipv6 firewall filter`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``connection-tracking-mode`` (>= 7.20), ``connection-tracking-port`` (>= 7.20), and ``group-authority`` (>= 7.15) parameters in the ``interface vrrp`` path (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``console settings`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``container config`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``container envs`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``container mounts`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``container`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``datapath.openflow-switch`` (>= 7.20), ``distance`` (>= 7.15), ``installation`` (>= 7.17), ``interworking.wan-symmetric`` (>= 7.15), ``max-clients`` (>=7.18) and ``station-roaming`` (>= 7.17) parameters in the ``interface wifi configuration`` path (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``days`` (>= 7.21) and  ``multi-passphrase-group`` (>= 7.17) parameters in the ``interface wifi access-list`` path (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``dhcp-server-vrf`` (>= 7.15) and ``local-address-as-src-ip`` (>= 7.17) parameters in the ``ip dhcp-relay`` path (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``disable-security-rules`` parameter in the ``iot modbus`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``disk btrfs subvolume`` path for RouterOS >=7.18 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``disk btrfs transfer`` path for RouterOS >=7.18 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``disk`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``dns-server`` (>= 7.16), ``early-failure-detection`` (>= 7.20), ``early-success-detection`` (>= 7.205), ``ignore-initial-down`` (>= 7.17), ``ignore-initial-up`` (>= 7.17) and ``record-type`` (>= 7.16) parameters in the ``tool netwatch`` path (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``dont-fragment`` parameter in the ``interface gre6`` path for RouterOS >= 7.21 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``dude agent`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``dude device-type`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``dude device`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``dude notification`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``dude probe`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``dude ros address`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``dude ros arp`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``dude ros lease`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``dude ros queue`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``dude ros route`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``dude service`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``dude`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``dynamic-lease-identifiers`` and ``support-broadband-tr101`` parameters in the ``ip dhcp-server`` path for RouterOS >= 7.21 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``dynamic`` and ``timeout`` parameters in the ``ip firewall address-list`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``dynamic`` and ``timeout`` parameters in the ``ipv6 firewall address-list`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``egress-rate``, ``ingress-rate``, ``l3-hw-offloading``, ``limit-broadcasts``, ``limit-unknown-multicasts``, ``limit-unknown-unicasts``, ``mirror-egress``, ``mirror-ingress``, ``mirror-ingress-target``, ``numbers`` and ``storm-rate`` parameters in the ``interface ethernet switch port`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``enable-ipv6-accounting`` parameter in the ``port aaa`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``file rsync-daemon`` path for RouterOS >= 7.16 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``file sync`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``file`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``filter-dst-ip-address`` (>= 7.15), ``filter-dst-ipv6-address`` (>= 7.15), ``filter-dst-mac-address`` (>= 7.15), ``filter-dst-port`` (>= 7.15), ``filter-src-ip-address`` (>= 7.15), ``filter-src-ipv6-address`` (>= 7.15), ``filter-src-mac-address`` (>= 7.15), ``filter-src-port`` (>= 7.15), ``filter-vlan`` (>= 7.15), ``max-packet-size`` (>= 7.19), ``quick-rows`` (>= 7.15) and ``quick-show-frame`` (>= 7.15) parameters in the ``tool sniffer`` path (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``headers``, ``hop-limit``, ``nth`` and ``to-address`` parameters in the ``ipv6 firewall nat`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``heartbeat`` (>= 7.18) and ``priority`` (>= 7.17) parameters in the ``interface bridge mlag`` path (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``hw-protection-mode``, ``distance``, ``interworking.3gpp-info-raw``, ``interworking.realms-raw``, ``security.beacon-protection``, ``steering.transition-request-coun``, ``steering.transition-request-period``, ``steering.transition-threshold``, ``steering.transition-threshold-time`` and ``steering.transition-time`` parameters in the ``interface wifi configuration`` path for RouterOS >= 7.21 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``icmp-errors-use-inbound-interface-address`` and ``tcp-timestamps`` parameters in the ``ip settings`` path for RouterOS >= 7.17 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``inactivity-policy`` (>= 7.16) and ``inactivity-timeout`` (>= 7.16) parameters in the ``user`` path (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``input.attr-error-handling`` (>= 7.21.2), ``input.filter-communities`` (>= 7.19), ``input.filter-ext-communities`` (>= 7.19), ``input.filter-large-communities`` (>= 7.19), ``input.filter-nlri`` (>= 7.20), ``input.filter-unknown`` (>= 7.19), ``output.as-override`` (>= 7.15), ``output.default-prepend`` (>= 7.15) and ``output.network-blackhole`` (>= 7.20.1) parameters in the ``routing bgp template`` path (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``input.attr-error-handling`` parameter in the ``routing bgp connection`` path for RouterOS >= 7.21.2 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``input`` parameter in the ``mpls interface`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``interface amt`` for RotuerOS 7.18 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``interface bridge calea`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``interface bridge filter`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``interface bridge host`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``interface bridge mdb`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``interface bridge msti`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``interface bridge nat`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``interface bridge port mst-override`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``interface bridge port-controller device`` path for RouterOS >= 7.15, < 7.18 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``interface eoipv6`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``interface ethernet switch host`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``interface ethernet switch l3hw-settings advanced`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``interface ethernet switch l3hw-settings`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``interface ethernet switch qos map ip`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/issues/319, https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``interface ethernet switch qos map vlan`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/issues/319, https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``interface ethernet switch qos map`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/issues/319, https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``interface ethernet switch qos priority-flow-control`` path for RouterOS >= 7.15, < 7.16 (https://github.com/ansible-collections/community.routeros/issues/319, https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``interface ethernet switch qos profile`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/issues/319, https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``interface ethernet switch qos settings`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/issues/319, https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``interface ethernet switch qos tx-manager`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/issues/319, https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``interface ethernet switch rule`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/issues/319, https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``interface ethernet switch vlan`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``interface ipip`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/issues/365, https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``interface ipipv6`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``interface l2tp-ether`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``interface l2tp-server`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``interface lte settings`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/issues/282, https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``interface macsec profile`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``interface macsec`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``interface macvlan`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``interface mesh port`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``interface mesh`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``interface ovpn-server`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``interface ppp-server`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``interface pppoe-server`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``interface pptp-client`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``interface pptp-server`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``interface sstp-client`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``interface sstp-server`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``interface veth`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``interface vpls`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``interface vxlan vteps`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``interface vxlan`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``interface wifi radio settings`` path for RouterOS >= 7.17 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``interface wifi security multi-passphrase`` path for RouterOS >= 7.17 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``interface wireless channels`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``interface wireless interworking-profiles`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``interface wireless nstreme-dual`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``interface wireless wds`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``invalid-users``,``read-only``,``require-encryption`` and ``valid-users`` parameters in the ``ip smb shares`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``iot bluetooth advertisers ad-structures`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``iot bluetooth whitelist`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``iot lora joineui`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``iot lora netid`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``iot lora servers`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``iot lora traffic options`` path for RouterOS >= 7.17 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``iot modbus security-rules`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``iot mqtt brokers`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``iot mqtt subscriptions`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``ip cloud back-to-home-file settings`` path for RouterOS >= 7.18 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``ip cloud back-to-home-file`` path for RouterOS >= 7.18 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``ip cloud back-to-home-user`` path for RouterOS >= 7.18 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``ip cloud back-to-home-users`` path for RouterOS >= 7.15, < 7.18 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``ip dhcp-server alert`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``ip firewall calea`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``ip hotspot ip-binding`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``ip ipsec key psk`` path for RouterOS >= 7.21 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``ip ipsec key qkd`` path for RouterOS >= 7.21 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``ip ipsec key rsa`` path for RouterOS >= 7.20 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``ip kid-control device`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``ip kid-control`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``ip media settings`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``ip media`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``ip nat-pmp interfaces`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``ip nat-pmp`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``ip packing`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``ip proxy access`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``ip proxy cache`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``ip proxy direct`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``ip service webserver`` path for RouterOS >= 7.21 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``ip socks users`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``ip socksify`` path for RouterOS >= 7.20 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``ip tftp`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``ipv6 dhcp-client option`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``ipv6 dhcp-relay option`` path for RouterOS >= 7.21 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``ipv6 dhcp-relay`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``ipv6 dhcp-server binding`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``ipv6 dhcp-server option sets`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``ipv6 nd proxy`` path for RouterOS >= 7.20 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``ipv6 neighbor`` path for RouterOS >= 7.18 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``ipv6 pool`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``l2tpv3-circuit-id`` (>= 7.15) and ``random-source-port`` (>=7.18) parameters in the ``interface gre6`` path (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``l3-hw-offloading``, ``mirror-egress-target``, ``numbers``, ``qos-hw-offloading``, ``rspan``, ``rspan-egress-vlan-id``, ``rspan-ingress-vlan-id`` and ``switch-all-ports`` parameters in the ``interface ethernet switch`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``lcd interface pages`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``lcd interface`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``lcd pin`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``lcd`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``liberal-tcp-tracking`` parameters in the ``ip firewall connection tracking`` path for RouterOS >= 7.20 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``lldp-dcbx`` (>= 7.17), ``lldp-max-frame-size`` (>= 7.15) and ``lldp-poe-power`` (>= 7.15) parameters in the ``ip neighbor discovery-settings`` (https://github.com/ansible-collections/community.routeros/issues/363, https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``local-address`` parameter in the ``port remote-access`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``lora joineui`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``lora netid`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``lora servers`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``lora traffic options`` path for RouterOS >= 7.17 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``mpls ldp local-mapping`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``mpls ldp neighbor`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``mpls ldp remote-mapping`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``mpls mangle`` path for RouterOS >= 7.17 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``mpls settings`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``mpls traffic-eng interface`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``mpls traffic-eng path`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``mpls traffic-eng tunnel`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``mvrp-forbidden`` parameter in the ``interface bridge vlan`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``mvrp`` (>= 7.15) and ``l3-hw-offloading`` (>= 7.21) parameters in the ``interface vlan`` path (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``network-mode`` (>= 7.20) and ``remote-address`` (>= 7.15) parameters in the ``interface ppp-client`` path (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``ntp-none`` parameter in the ``ip dhcp-server network`` path for RouterOS >= 7.20 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``numbers`` parameters in the ``interface ethernet poe`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``numbers`` parameters in the ``interface ethernet switch port-isolation`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``numbers`` parameters in the ``ip firewall service-port`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``numbers`` parameters in the ``ip hotspot service-port`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``numbers`` parameters in the ``ip service`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``numbers`` parameters in the ``queue interface`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``numbers`` parameters in the ``system resource irq rps`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``on-login`` and ``on-logout`` parameters in the ``ip hotspot user profile`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``openflow port`` path for RouterOS >= 7.20 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``openflow-switch`` parameter in the ``interface wifi datapath`` for RouterOS >= 7.20 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``openflow`` path for RouterOS >= 7.20 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``password-authentication`` and ``publickey-authentication-options`` parameters in the ``ip ssh`` path for RouterOS >= 7.21 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``password`` parameter in the ``interface dot1x client`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``polling`` (>= 7.16), ``remove-sent-sms-after-send`` (>= 7.20) and ``sms-storage`` (>= 7.15) parameters in the ``tool sms`` path (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``ppk-secret`` parameter in the ``ip ipsec peer`` path for RouterOS >= 7.21 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``ppk`` parameter in the ``ip ipsec profile`` path for RouterOS >= 7.21 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``ppp l2tp-secret`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``pref-src`` (>= 7.20), ``suppress-hw-offload`` (>= 7.15) parameters in the ``ipv6 route`` path (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``push-routes-ipv6`` parameter in the ``interface ovpn-server server`` path for RouterOS >= 7.21 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``radius-password`` parameters in the ``ip dhcp-server config`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``regex`` (>= 7.17) parameter in the ``system logging`` path (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``routing bgp evpn`` path for RouterOS >= 7.20 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``routing bgp instance`` path for RouterOS >= 7.20 (https://github.com/ansible-collections/community.routeros/issues/437, https://github.com/ansible-collections/community.routeros/pull/438).
- api_info, api_modify - adds support for the ``routing bgp vpls`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``routing bgp vpn`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``routing fantasy`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``routing filter community-ext-list`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``routing filter community-large-list`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``routing gmp`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``routing igmp-proxy mfc`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``routing isis instance`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/issues/356, https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``routing isis interface-template`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/issues/356, https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``routing pimsm bsr candidate`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``routing pimsm bsr rp-candidate`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``routing pimsm static-rp`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``routing rip instance`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``routing rip interface-template`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``routing rip keys`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``routing rip static-neighbor`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``routing rpki`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``routing settings`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``rsync-daemon`` path for RouterOS >= 7.15, < 7.16 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``rx-switch-offset`` parameter in the ``iot modbus`` path for RouterOS >= 7.21 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``sa-dst-address``, ``sa-src-address`` parameters in the ``ip ipsec policy`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``slave-name-format`` parameter in the ``interface wifi interworking`` path for RouterOS >= 7.16 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``socks5-port`` (>= 7.20), ``socks5-server`` (>= 7.20) and ``socksify-service`` (>= 7.20) parameters in the ``ip firewall nat`` path (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``special-login`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``src-port`` parameter in the ``ip socks access`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``stale-neighbor-detect-interval`` parameters in the ``ipv6 settings`` path for RouterOS >= 7.17 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``system console screen`` path for RouterOS >= 7.15, < 7.16.1 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``system console`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``system gps`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``system hardware`` path for RouterOS >= 7.15, < 7.16.1 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``system health`` path for RouterOS >= 7.15.3, < 7.16.1 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``system leds`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``system ntp key`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``system package local-update mirror`` path for RouterOS >= 7.17 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``system package local-update update-package-source`` path for RouterOS >= 7.17 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``system resource hardware usb-settings`` path for RouterOS >= 7.20 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``system resource usb settings`` path for RouterOS >= 7.15, < 7.20 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``system resource usb`` path for RouterOS >= 7.15, < 7.20 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``system routerboard mode-button`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``system routerboard reset-button`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``system routerboard wps-button`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``system swos`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``system upgrade upgrade-package-source`` path for RouterOS >= 7.15, < 7.17 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``task`` path for RouterOS >= 7.15, < 7.17 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``tool calea`` path for RouterOS >= 7.15, < 7.17 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``tool graphing queue`` path for RouterOS >= 7.15, < 7.17 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``tool mac-server sessions`` path for RouterOS >= 7.15, < 7.17 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``tool traffic-generator packet-template`` path for RouterOS >= 7.15, < 7.17 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``tool traffic-generator port`` path for RouterOS >= 7.15, < 7.17 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``tool traffic-generator raw-packet-template`` path for RouterOS >= 7.15, < 7.17 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``tool traffic-generator stream`` path for RouterOS >= 7.15, < 7.17 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``tool traffic-monitor`` path for RouterOS >= 7.15, < 7.17 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``tos`` parameter in the ``ip firewall filter`` path for RouterOS >= 7.21 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``tos`` parameter in the ``ip firewall mangle`` path for RouterOS >= 7.21 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``tos`` parameter in the ``ip firewall nat`` path for RouterOS >= 7.21 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``tos`` parameter in the ``ip firewall raw`` path for RouterOS >= 7.21 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``tos`` parameter in the ``ipv6 firewall filter`` path for RouterOS >= 7.21 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``tos`` parameter in the ``ipv6 firewall mangle`` path for RouterOS >= 7.21 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``tos`` parameter in the ``ipv6 firewall nat`` path for RouterOS >= 7.21 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``tos`` parameter in the ``ipv6 firewall raw`` path for RouterOS >= 7.21 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``total-bucket-size``, ``total-burst-limit``, ``total-burst-threshold``, ``total-burst-time``, ``total-limit-at``, ``total-max-limit``, ``total-priority`` and ``total-queue`` parameters in the ``queue simple`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``totp-secret`` parameter in the ``ip hotspot user`` path for RouterOS >= 7.21 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``tr069-client`` path for RouterOS >= 7.15, < 7.17 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``transition-request-count``, ``transition-request-period``, ``transition-threshold``, ``transition-threshold-time`` and ``transition-time`` parameters in the ``interface wifi steering`` path for RouterOS >= 7.21 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``user ssh-keys`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``user-manager advanced`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``user-manager attribute`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``user-manager database`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``user-manager limitation`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``user-manager payment`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``user-manager profile-limitation`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``user-manager profile`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``user-manager router`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``user-manager user group`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``user-manager user-profile`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``user-manager user`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``user-manager`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``vrf`` parameter in the ``interface wireguard`` path for RouterOS >= 7.21 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``vrf`` parameters in the ``ip socks`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``vrf`` parameters in the ``radius incoming`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``vrf`` parameters in the ``tool e-mail`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``zerotier controller member`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``zerotier controller`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``zerotier interface`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - adds support for the ``zerotier`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - allow multiple parameters to be disabled in the ``interface wifi configuration`` path (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - allow the ``fib`` parameter to be disabled for the ``routing table`` path (https://github.com/ansible-collections/community.routeros/issues/368, https://github.com/ansible-collections/community.routeros/pull/417).
- api_info, api_modify - allow the parameter ``forwarding-override`` to be disabled in the ``interface ethernet switch port-isolation`` path (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - allow the parameter ``mac-cookie-timeout`` to be disabled for the ``ip hotspot user profile`` path (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - allow the parameter ``mpls-mtu`` to be disabled for the ``mpls interface`` path (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - allow the parameter ``multi-passphrase-group`` to be disabled for the ``interface wifi security`` path (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - allow the parameter ``relay-info-remote-id`` to be disabled for the ``ip dhcp-relay`` path (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - allow the parameter ``sfp-shutdown-temperature`` to be disabled in the ``interface ethernet`` path (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - allow the parameter ``time`` to be disabled for the ``interface wireless access-list`` path (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - allow the parameter ``traffic-processing`` to be disabled for the ``interface wifi datapath`` path (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - allow the parameter ``use-bfd`` to be disabled for the ``routing ospf interface-template`` path (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - allow the parameters ``action`` to be disabled for the ``interface wifi access-list`` path (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - allow the parameters ``ca-certificate``, ``certificate`` and ``interfaces`` to be disabled for the ``interface wifi capsman`` path (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - allow the parameters ``caps-man-addresses``, ``caps-man-certificate-common-names``, ``caps-man-names``, ``certificate``, ``discovery-interfaces``, ``lock-to-caps-man``, ``slaves-datapath`` and ``slaves-static`` to be disabled for the ``interface wifi cap`` path (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - allow the parameters ``certificate``, ``down-script``, ``http-codes``, ``interval``, ``packet-interval``, ``port``, ``src-address``, ``start-delay``, ``startup-delay``, ``test-script``, ``thr-avg``, ``thr-http-time``, ``thr-jitter``, ``thr-loss-count``, ``thr-loss-percent``, ``thr-max``, ``thr-stdev``, ``thr-tcp-conn-time``, ``timeout`` and ``up-script`` to be disabled in the ``tool netwatch`` path (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - allow the parameters ``datapath.traffic-processing``, ``l2mtu``, ``master-interface``, ``mtu`` and ``radio-mac`` to be disabled for the ``interface wifi`` path (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - allow the parameters ``deprioritize-unii-3-4``, ``reselect-interval`` and ``reselect-time`` to be disabled for the ``interface wifi channel`` path (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - allow the parameters ``internal-path-cost`` and ``path-cost`` to be disabled in the ``interface bridge port`` path for RouterOS >= 7.13 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - changed support for the parameter ``group-master`` in the ``interface vrrp`` path to write-only for RouterOS >= 7.11 (deprecated and replaced by ``group-authority``) (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - fix default value for field ``mvrp-forbidden`` in ``interface bridge vlan`` (https://github.com/ansible-collections/community.routeros/issues/440, https://github.com/ansible-collections/community.routeros/pull/441/).
- api_info, api_modify - parameters ``copy-from`` and ``place-before`` are now write-only for the ``routing bfd configuration`` path (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - remove primary key constraint on 'peer' for path ``ip ipsec identity`` (https://github.com/ansible-collections/community.routeros/pull/421).
- api_info, api_modify - removed default value for parameters ``internal-path-cost`` and ``path-cost`` in the ``interface bridge port`` path for RouterOS >= 7.13 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - removed support for the ``interface bridge port port-controller`` path for RouterOS >= 7.18 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - removed support for the ``interface bridge port-extender`` path for RouterOS >= 7.18 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - removed support for the ``ip accounting web-access`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - removed support for the ``ip accounting`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - removed support for the ``mpls`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - removed support for the ``port firmware`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - removed support for the ``routing bgp aggregate`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - removed support for the ``routing bgp instance`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - removed support for the ``routing bgp network`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - removed support for the ``routing bgp peer`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - removed support for the ``routing mme`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - removed support for the ``routing rip`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - removed support for the ``system upgrade mirror`` path for RouterOS >= 7.17 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - removed support for the parameter ``address`` in the ``ip traffic-flow target`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - removed support for the parameter ``allow-guests`` in the ``ip smb`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - removed support for the parameter ``allow-none-crypto`` in the ``ip ssh`` path for RouterOS >= 7.17 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - removed support for the parameter ``always-allow-password-login`` in the ``ip ssh`` path for RouterOS >= 7.21 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - removed support for the parameter ``auto-erase`` in the ``tool sms`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - removed support for the parameter ``bsd-syslog`` in the ``system logging action`` path for RouterOS >= 7.18 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - removed support for the parameter ``comment`` in the ``ip ipsec mode-config`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - removed support for the parameter ``default-mount-point-template`` in the ``disk settings`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - removed support for the parameter ``default`` in the ``caps-man manager interface`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - removed support for the parameter ``default`` in the ``interface lte apn`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - removed support for the parameter ``default`` in the ``ip ipsec policy group`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - removed support for the parameter ``default`` in the ``ip smb users`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - removed support for the parameter ``default`` in the ``snmp community`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - removed support for the parameter ``disabled`` in the ``interface wireless security-profiles`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - removed support for the parameter ``force-aes`` in the ``interface sstp-server server`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - removed support for the parameter ``full-duplex`` in the ``interface ethernet`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - removed support for the parameter ``gmt-offset`` in the ``system clock`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - removed support for the parameter ``info`` in the ``mpls interface`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - removed support for the parameter ``input.accept-unknown`` in the ``routing bgp connection`` path for RouterOS >= 7.19 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - removed support for the parameter ``input.accept-unknown`` in the ``routing bgp template`` path for RouterOS >= 7.19 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - removed support for the parameter ``memory-frequency`` in the ``system routerboard settings`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - removed support for the parameter ``mtu`` in the ``interface vrrp`` path for RouterOS >= 7.20 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - removed support for the parameter ``route-cache`` in the ``ip settings`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - removed support for the parameter ``routing-table`` in the ``ip firewall filter`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - removed support for the parameter ``routing-table`` in the ``ip firewall mangle`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - removed support for the parameter ``tls-host`` in the ``ip firewall nat`` path for RouterOS >= 7.16 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - removed support for the parameter ``tls-host`` in the ``ipv6 firewall nat`` path for RouterOS >= 7.16 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - removed support for the parameters ``as-override``, ``input.limit-nlri-diversity`` and ``output.default-prepent`` in the ``routing bgp template`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - removed support for the parameters ``cluster-id`` and ``input.ignore-as-path-len`` in the ``routing bgp connection`` path for RouterOS >= 7.20 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - removed support for the parameters ``cluster-id`` and ``input.ignore-as-path-len`` in the ``routing bgp template`` path for RouterOS >= 7.20 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - removed support for the parameters ``default`` and ``max-sessions`` in the ``ip smb shares`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - removed support for the parameters ``installed-version``, ``latest-version`` and ``status`` in the ``system package update`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - removed support for the parameters ``layer7-protocol`` and ``to-addresses`` in the ``ipv6 firewall nat`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - removed support for the parameters ``primary-ntp``, ``secondary-ntp`` and ``server-dns-names`` in the ``system ntp client`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - removed support for the parameters ``route-tag``, ``routing-mark`` and ``type`` in the ``ip route`` path for RouterOS >= 7.15 (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - treat parameters ``list`` and ``key`` as primary keys for the ``container envs`` path on RouterOS versions >= 7.20 (https://github.com/ansible-collections/community.routeros/issues/449, https://github.com/ansible-collections/community.routeros/pull/451).
- api_modify - defined ``name`` as primary key, added default for ``container-mac-address``, allowed ``comment`` to be disabled for RouterOS path ``interface veth`` (https://github.com/ansible-collections/community.routeros/issues/454, https://github.com/ansible-collections/community.routeros/pull/455).
- api_modify - make ``name`` a primary key (and thus required) for the ``container`` path for RouterOS >=7.19 (https://github.com/ansible-collections/community.routeros/issues/443, https://github.com/ansible-collections/community.routeros/pull/445).

community.sap_libs
~~~~~~~~~~~~~~~~~~

- collection - Update all license headers (https://github.com/sap-linuxlab/community.sap_libs/pull/82)
- sap_control_exec - Add local socket support (https://github.com/sap-linuxlab/community.sap_libs/pull/66)
- sap_control_exec, sap_hostctrl_exec - QoL and Error handling (https://github.com/sap-linuxlab/community.sap_libs/pull/81)
- sap_control_exec, sap_hostctrl_exec - Refactor to use shared utilities (https://github.com/sap-linuxlab/community.sap_libs/pull/78)
- sap_hdbsql - Add error handling and secure flags for hdbsql (https://github.com/sap-linuxlab/community.sap_libs/pull/75)
- sap_hdbsql - Add new parameter named properties (https://github.com/sap-linuxlab/community.sap_libs/pull/79)
- sap_hostctrl_exec - Add new module and tests (https://github.com/sap-linuxlab/community.sap_libs/pull/67)
- sap_system_facts - Add SID and permission check to facts module (https://github.com/sap-linuxlab/community.sap_libs/pull/73)
- sapcar_extract - Add overwrite mode and improve exist validation (https://github.com/sap-linuxlab/community.sap_libs/pull/77)

community.sops
~~~~~~~~~~~~~~

- load_vars - now supports ansible-core 2.21's way of actually loading variables, instead of returning ``ansible_facts``. The behavior for this can be controlled through the new ``return_method`` option, which is by default set to ``auto``. On ansible-core 2.21+, ``auto`` behaves the same as ``vars-only`` (return proper variables), and for ansible-core before 2.21 the same as ``facts-only`` (return ``ansible_facts``) (https://github.com/ansible-collections/community.sops/pull/283).

community.windows
~~~~~~~~~~~~~~~~~

- Add official support for Ansible 2.20

containers.podman
~~~~~~~~~~~~~~~~~

- Add configuration for new Ansible release
- Fix CI of Podman Search modul
- Fix tests for new Podman
- add passthrough and none log driver options

dellemc.enterprise_sonic
~~~~~~~~~~~~~~~~~~~~~~~~

- plugins - Change all instances of 'after(generated)' to 'after_generated' to address sanity errors (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/609).
- sonic_aaa - Add support for accounting options (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/559).
- sonic_interfaces - Support for BAM/MSA configuration (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/567).
- sonic_lag_interfaces - Add support for 'speed' and 'adv_speed' (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/572).
- sonic_radius_server - Add support for RADIUS TLS security profile (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/615).
- sonic_system - Add support for banner and login exec-timeout options (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/614).
- sonic_vrrp - Add support for vrrp 'preempt_delay' option (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/571).
- sonic_vxlans - Add support for QoS mode (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/611).

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- Added support for OpenManage Enterprise version 4.4 and 4.5.
- The OpenManage Enterprise, OpenManage Enterprise Modular and OpenManage Enterprise Integration for VMware vCenter modules are now compatible with Ansible Core version 2.20.

fortinet.fortimanager
~~~~~~~~~~~~~~~~~~~~~

- Supported new environment variable "ANSIBLE_FORTIMANAGER_ENABLE_LOG" to enable/disable logging for FortiManager Ansible Collection.
- Supported new environment variable "ANSIBLE_FORTIMANAGER_VERSION_CHECK" to enable/disable version checking performed by the FortiManager Ansible Collection.
- Supported new modules to configure FortiProxy.
- Supported new schemas in FortiManager 7.0.15, 7.4.8, 7.6.4.
- Supported new schemas in FortiManager 7.0.16, 7.2.12, 7.4.9, 7.4.10, 7.6.5, 7.6.6

google.cloud
~~~~~~~~~~~~

- gcp_alloydb_* - added gcp_alloydb_cluster, gcp_alloydb_instance, gcp_alloydb_backup, and gcp_alloydb_user modules (https://github.com/ansible-collections/google.cloud/pull/722)
- gcp_cloudbuildv2_* - added gcp_cloudbuildv2_connection and gcp_cloudbuildv2_repository modules (https://github.com/ansible-collections/google.cloud/pull/729).
- gcp_colab_* - added four new modules (gcp_colab_notebook_execution, gcp_colab_runtime, gcp_colab_runtime_template, and gcp_colab_schedule) (https://github.com/ansible-collections/google.cloud/pull/747).
- gcp_compute_instance_* - renamed the `tags.items` field to `tags.tag_values`. The old naming is still available but will be removed in a future release. (https://github.com/ansible-collections/google.cloud/pull/750).
- gcp_sql_instance - add `allocated_ip_range` to `settings.ip_configuration` for private IP Cloud SQL instances (name of the allocated IP range in the VPC) (https://github.com/ansible-collections/google.cloud/pull/744).
- gcp_vertexai_* - added 18 Vertex AI modules (gcp_vertexai_dataset, gcp_vertexai_deployment_resource_pool, gcp_vertexai_endpoint, gcp_vertexai_endpoint_with_model_garden_deployment, gcp_vertexai_feature_group, gcp_vertexai_feature_group_feature, gcp_vertexai_feature_online_store, gcp_vertexai_feature_online_store_featureview, gcp_vertexai_featurestore, gcp_vertexai_featurestore_entitytype, gcp_vertexai_featurestore_entitytype_feature, gcp_vertexai_index, gcp_vertexai_index_endpoint, gcp_vertexai_index_endpoint_deployed_index, gcp_vertexai_metadata_store, gcp_vertexai_rag_engine_config, gcp_vertexai_reasoning_engine, gcp_vertexai_tensorboard) (https://github.com/ansible-collections/google.cloud/pull/743).

hetzner.hcloud
~~~~~~~~~~~~~~

- All ``module_utils`` are now marked as **private**. None of the modules were intended for public use.
- DNS support is now generally available.
- floating_ip - Unassign Floating IP before deleting it.
- load_balancer_network - Add ``ip_range`` argument to attach a load balancer to a specific subnet.
- primary_ip - Added the Primary IP ``location`` name to the return values (``hcloud_primary_ip.location``).
- primary_ip - Added the ``location`` argument to create a Primary IP in a specific location.
- primary_ip - Assign to new server if ``server`` is changed.
- primary_ip - Unassign Primary IP before deleting it.
- primary_ip - Unassign primary_ip if ``server`` is null.
- primary_ip_info - Added the Primary IPs ``location`` name to the return values (``hcloud_primary_ip_info[].location``).
- server - Rebuilding a Server now supports the ``user_data`` argument.
- server_network - Add ``ip_range`` argument to attach a load balancer to a specific subnet.
- storage_box - New module to create and manage Storage Boxes in Hetzner.
- storage_box - The module is no longer marked as experimental.
- storage_box_info - New module to gather infos about Hetzner Storage Boxes.
- storage_box_info - The module is no longer marked as experimental.
- storage_box_snapshot - New module to create and manage Storage Box Snapshots in Hetzner.
- storage_box_snapshot - The module is no longer marked as experimental.
- storage_box_snapshot_info - New module to gather infos about Hetzner Storage Box Snapshots.
- storage_box_snapshot_info - The module is no longer marked as experimental.
- storage_box_subaccount - New module to create and manage Storage Box Subaccounts in Hetzner.
- storage_box_subaccount - Replace the label based name workaround, with the new Storage Box Subaccount name property in the API.
- storage_box_subaccount - The module is no longer marked as experimental.
- storage_box_subaccount_info - New module to gather infos about Hetzner Storage Box Subaccounts.
- storage_box_subaccount_info - Replace the label based name workaround, with the new Storage Box Subaccount name property in the API.
- storage_box_subaccount_info - The module is no longer marked as experimental.
- storage_box_type_info - New module to gather infos about Hetzner Storage Box Types.
- storage_box_type_info - The module is no longer marked as experimental.
- txt_record - Add new txt_record filter to help format TXT , e.g. ``"{{ 'v=spf1 include:_spf.example.net ~all' | hetzner.hcloud.txt_record }}"``.

hitachivantara.vspone_block
~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Added "playbooks/vsp_direct/vsp_storage_connection_session_example.yml" as a sample playbook demonstrating session-based storage operations.
- Added a new "hv_pav_alias" module to manage PAV (Parallel Access Volume) alias assignments for Mainframe based VSP block storage systems.
- Added a new "hv_pav_alias_facts" module to gather facts about PAV aliases from Mainframe based VSP block storage systems.
- Added a new "hv_sds_block_audit_log_setting" module to support configuration of audit log settings on VSP One SDS Block and Cloud systems.
- Added a new "hv_sds_block_audit_log_setting_facts" module to retrieve audit log setting from VSP One SDS Block and Cloud systems.
- Added a new "hv_sds_block_dump_log_file" module to retrieve and dump log information from VSP One SDS Block and Cloud systems.
- Added a new "hv_sds_block_dump_log_status_facts" module to retrieve and dump log status information from VSP One SDS Block and Cloud systems.
- Added a new "hv_sds_block_encryption_environment_setting_facts" module to retrieve encryption environment configuration settings from VSP One SDS Block and Cloud systems.
- Added a new "hv_sds_block_encryption_environment_settings" module to enable or disable encryption functionality on VSP One SDS Block and Cloud systems.
- Added a new "hv_sds_block_encryption_key" module to create and delete encryption keys on VSP One SDS Block and Cloud systems.
- Added a new "hv_sds_block_encryption_key_count_facts" module to retrieve information about the number of encryption keys from VSP One SDS Block and Cloud systems.
- Added a new "hv_sds_block_encryption_key_facts" module to retrieve detailed information about encryption keys from VSP One SDS Block and Cloud systems.
- Added a new "hv_sds_block_event_log_setting_facts" module to retrieve event log setting from VSP One SDS Block and Cloud systems.
- Added a new "hv_sds_block_event_logs_facts" module to retrieve event logs with various filtering options from VSP One SDS Block and Cloud systems.
- Added a new "hv_sds_block_journal" module to create and update journals on VSP One SDS Block and Cloud systems.
- Added a new "hv_sds_block_journal_facts" module to retrieve journal details from VSP One SDS Block and Cloud systems.
- Added a new "hv_sds_block_license" module to manage license on VSP One SDS Block and Cloud systems.
- Added a new "hv_sds_block_license_facts" module to retrieve license from VSP One SDS Block and Cloud systems.
- Added a new "hv_sds_block_license_setting" module to modify license warning threshold settings for VSP One SDS Block and Cloud systems.
- Added a new "hv_sds_block_license_setting_facts" module to retrieve license setting from VSP One SDS Block and Cloud systems.
- Added a new "hv_sds_block_login_message" module to update the message configured to be displayed on the GUI login window and CLI warning banner of the VSP One SDS Block and Cloud systems.
- Added a new "hv_sds_block_login_message_facts" module to retrieve the message configured to be displayed on the GUI login window and CLI warning banner of the VSP One SDS Block and Cloud systems.
- Added a new "hv_sds_block_protection_domain" module to manage protection domains including creation, modification, and data relocation operations on VSP One SDS Block and Cloud systems.
- Added a new "hv_sds_block_remote_path_group" module to create remote path group, add remote path to a remote path group, remove remote path from remote path group, and delete remote path group on VSP One SDS Block systems.
- Added a new "hv_sds_block_remote_path_group_facts" module to retrieve information about remote path groups from VSP One SDS Block systems.
- Added a new "hv_sds_block_session" module to generate and discard session on VSP One SDS Block and Cloud systems.
- Added a new "hv_sds_block_session_facts" module to retrieve information about sessions on VSP One SDS Block and Cloud systems.
- Added a new "hv_sds_block_snmp_settings" module to manage SNMP settings including agent enablement, version configuration, trap settings, authentication settings, and system group information on VSP One SDS Block and Cloud systems.
- Added a new "hv_sds_block_snmp_settings_facts" module to retrieve SNMP settings including agent status, version configuration, trap settings, authentication settings, and system group information from VSP One SDS Block and Cloud systems.
- Added a new "hv_sds_block_spare_node" module to manage spare node configuration including node identification, fault domain assignment, network configuration, and BMC settings on VSP One SDS Block and Cloud systems.
- Added a new "hv_sds_block_spare_node_facts" module to retrieves spare node information and configuration details from VSP One SDS Block and Cloud systems.
- Added a new "hv_sds_block_storage_external_auth_server_setting" module to configure external authentication server settings on VSP One SDS Block and Cloud systems.
- Added a new "hv_sds_block_storage_external_auth_server_setting_facts" module to retrieve external authentication server settings from the VSP One SDS Block and Cloud systems.
- Added a new "hv_sds_block_storage_system" module to manage storage system configuration including certificate management, cache settings, and other system-level configurations on VSP One SDS Block and Cloud systems.
- Added a new "hv_sds_block_storage_user_auth_setting" module to configure external authentication server settings on VSP One SDS Block and Cloud systems.
- Added a new "hv_sds_block_storage_user_auth_setting_facts" module to retrieve user authentication settings from VSP One SDS Block and Cloud systems.
- Added a new "hv_sds_block_user_group" module to Create and update user groups on VSP One SDS Block and Cloud systems.
- Added a new "hv_sds_block_user_group_facts" module to retrieve user groups from VSP One SDS Block and Cloud systems.
- Added a new "hv_sds_block_web_server" module to manages the web server access setting for VSP One SDS Block and Cloud systems.
- Added a new "hv_sds_block_web_server_facts" module to retrieve the web server access setting from VSP One SDS Block and Cloud systems.
- Added a new "hv_session" module to generate and discard session on VSP block storage systems.
- Added a new "hv_session_facts" module to retrieve information about sessions on VSP block storage systems.
- Added a new "hv_snapshot_family_facts" module to retrieve information about snapshot family of the provided LDEV ID from VSP block storage systems.
- Added a new "hv_supported_host_mode_facts" module to retrieve detailed information about supported host mode options available in a given VSP block storage system.
- Added a new "hv_vclone_parent_volume_facts" module to retrieve information about virtual clone parent volume from VSP block storage systems.
- Added notes to module documentation indicating that a few modules are not supported for BHE and higher models.
- Added support for Mainframe z16.
- Added support for SVOS 10.5.1.
- Added support for latest software version 01.18.02 for VSP One SDS Block and Cloud systems.
- Added support to "Add user to user groups" to hv_sds_block_user module.
- Added support to "Delete a user" to hv_sds_block_user module.
- Added support to "Disable encryption for storage pool using ID" to hv_sds_block_storage_pool module.
- Added support to "Disable encryption for storage pool" to hv_sds_block_storage_pool module.
- Added support to "Enable encryption for storage pool by ID" to hv_sds_block_storage_pool module.
- Added support to "Enable encryption for storage pool by name" to hv_sds_block_storage_pool module.
- Added support to "Remove user from user groups" to hv_sds_block_user module.
- Added support to "Update user settings" to hv_sds_block_user module.
- Added support to "hv_ddp_pool" module for DDP pool creation with RAID6.
- Added support to "hv_hg" module for present/unpresent multiple LDEVs to/from hostgroups across multiple ports.
- Added support to "hv_hg" module to support host group's lun paths.
- Added support to "hv_ldev" module to create DRS LDEV without deduplication and compression.
- Added support to "hv_ldev" module to create ESE Mainframe LDEV with cylinder and emulation type.
- Added support to "hv_ldev" module to create Mainframe LDEV with cylinder and emulation type in a parity group.
- Added support to "hv_ldev" module to create Mainframe LDEV with cylinder and emulation type.
- Added support to "hv_ldev" module to create TSE Mainframe LDEV with cylinder and emulation type.
- Added support to "hv_ldev" module to stop the normal format for all volumes.
- Added support to "hv_ldev_facts" module output to include Mainframe, vClone and other new properties.
- Added support to "hv_ldev_facts" module to get information about multiple LDEVs by their IDs.
- Added support to "hv_paritygroup_facts" module output to include Mainframe and other new properties.
- Added support to "hv_resource_group_facts" module to get basic information about all resource groups including meta resource group information.
- Added support to "hv_sds_block_cluster" module to stop the storage cluster.
- Added support to "hv_snapshot" module to create or convert a snapshot pair to vClone depending on the snapshot pair status.
- Added support to "hv_snapshot" module to optionally delete secondary volume using should_delete_svol parameter.
- Added support to "hv_snapshot" module to restore a snapshot pair from vClone.
- Added support to "hv_snapshot_facts" module output to include vClone-related properties.
- Added support to "hv_snapshot_group" module to create or convert a snapshot pair to vClone by snapshot group name.
- Added support to "hv_snapshot_group" module to restore snapshot group from vClone.
- Added support to "hv_snapshot_group" module to restore the snapshot pairs using group name and wait for the final state of all snapshots.
- Added support to "hv_snapshot_group_facts" module output to include vClone-related properties.
- Added support to "hv_storage_port_facts" module output to include Mainframe and other new properties.
- Added support to "hv_storagepool" module output to include pool volumes information.
- Added support to "hv_storagepool" module to create a mainframe HDP storage pool using parity group and cylinder.
- Added support to "hv_storagepool" module to shrink a storage pool using list of pool volume IDs and delete pool volumes.
- Added support to "hv_storagepool" module to shrink a storage pool using list of pool volume IDs.
- Added support to "hv_storagepool" module to shrink a storage pool using start and end pool volume IDs.
- Added support to "hv_storagepool" module to stop the shrink operation of a storage pool.
- Added support to "hv_storagepool_facts" module output to include pool volumes information.
- Added support to "hv_storagepool_facts" module to get all mainframe storage pools with cache info for VSP 5XXX series storage.
- Added support to "hv_storagepool_facts" module to get all mainframe storage pools with extended info.
- Added support to "hv_storagepool_facts" module to get all mainframe storage pools.
- Added support to "hv_storagesystem_facts" module output to include "is_compression_acceleration_available" status.
- Added support to "hv_vsp_one_volume" module to create DRS volume without deduplication and compression.
- Added support to "hv_vsp_one_volume_facts" module output to include Mainframe, vClone and other new properties.
- Enhanced the performance of the "hv_gad_facts" module's task by implementing thread pool and batch processing.
- Enhanced the performance of the "hv_hg_facts" module's task by implementing parallel calls.
- Enhanced the performance of the "hv_ldev_facts" module's task by implementing thread pool and batch processing.
- Other minor bug fixes.

hitachivantara.vspone_object
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Enhanced `hv_storage_component` module to support storage components of type ARRAY for VSP One B20 series storage systems.

ibm.storage_virtualize
~~~~~~~~~~~~~~~~~~~~~~

- ibm_sv_manage_replication_policy - Enabled support for logging in via partition ip
- ibm_svc_initial_setup - Added support for managing anomaly settings
- ibm_svc_manage_volume - Added support for addressing volume via UID
- ibm_svc_manage_volume - Added support for autoexpand, preferrednode and cache parameters

infoblox.nios_modules
~~~~~~~~~~~~~~~~~~~~~

- CI/CD - Added PyGObject support and improved dependency handling
- nios_dtc_lbdn - Added support for auth_zones with enhanced change detection for string and object formats, including proper handling when entries are removed

kaytus.ksmanage
~~~~~~~~~~~~~~~

- Modify the contact email in the README.md file. (https://github.com/KSManageOSS/kaytus.ksmanage/pull/39).

kubernetes.core
~~~~~~~~~~~~~~~

- Remove deprecated import from ``ansible.module_utils._text`` (https://github.com/ansible-collections/kubernetes.core/pull/1053).
- helm - add ``release_values`` key to ``status`` return value that can be accessed using Jinja2 dot notation (https://github.com/ansible-collections/kubernetes.core/pull/1056).
- helm_info - add ``release_values`` key to ``status`` return value that can be accessed using Jinja2 dot notation (https://github.com/ansible-collections/kubernetes.core/pull/1056).

microsoft.ad
~~~~~~~~~~~~

- Add official support for Ansible 2.20

microsoft.iis
~~~~~~~~~~~~~

- Add official support for Ansible 2.20

netapp.ontap
~~~~~~~~~~~~

- na_ontap_ems_filter - new option `parameter_criteria` added in REST, requires ONTAP 9.13.1 or later.
- na_ontap_lun - updated documentation for unsupported REST parameters.
- na_ontap_net_ifgrp - Update `mode` parameter to specify allowed values.
- na_ontap_nfs - new option `credential_cache` added in REST.
- na_ontap_snapmirror - new options `time_out`, `wait_for_completion` added in REST.
- na_ontap_snapmirror - updated documentation for `identity_preserve` and `max_transfer_rate`.
- na_ontap_volume_efficiency- AWS Lambda support added to the module.
- na_ontap_volume_efficiency- Added `wait_for_completion` and `time_out` parameters to fix time out errors for long running operations.

netapp.storagegrid
~~~~~~~~~~~~~~~~~~

- all modules - add support for failure responses to include additional error details for easier troubleshooting.
- na_sg_grid_alert_receiver - new option `smtp_username` and `smtp_password` added in place of `username` and `password`.
- na_sg_grid_audit_destination - new option `access_logs_send`, `access_logs_facility`, and `access_logs_severity` added to manage access log settings for syslog server.
- na_sg_grid_gateway - new option `closed_on_untrusted_client_network`. Requires StorageGRID 11.8 or later.
- na_sg_grid_gateway - parameter `default_service_type` allows option for `management`. Requires StorageGRID 11.8 or later.
- na_sg_grid_group - new option `manage_alerts` and `storage_admin` added to management policy.
- na_sg_grid_info - Added new endpoints for the grid info.
- na_sg_org_bucket - user input for `capacity_limit` option changed from bytes to GB.
- na_sg_org_container - Enhanced the bucket policy.
- na_sg_org_container - user input for `capacity_limit` option changed from bytes to GB.
- na_sg_org_group - new options `s3_console` to control S3 console access and `view_all_containers` to view settings for all buckets added, requires StorageGRID version 11.8 or later.
- na_sg_org_info - Added new endpoints for the org info.

netbox.netbox
~~~~~~~~~~~~~

- Add integration tests for contact groups
- Add support for custom headers for all modules
- Change `netbox_contact.contact_group` to `contact_groups`
- Fix ansible-bad-import-from pylint errors
- Fix broken code path when using old api path on old netbox systems
- Make the unit-test data structures more flexible.
- Remove abandoned unit-test data.
- add workaround to _build_query_params for services and Netbox 4.3.0 - 4.4.3 (wrong parent_object_type data type)
- add yamllint to project pipeline.
- improve version_check_greater to be more universal
- netbox_circuit_termination - Add parameters termination_id and termination_type for NetBox 4.2+
- netbox_tag - Add support for object_types on tags
- rename variable full_version to netbox_version.
- rename variable version to api_version.
- sanitize netbox versions received from api
- test suite expanded to run on Python 3.11, 3.12, and 3.13.
- user.groups, user.permissions, user_group.permissions, permission.actions, and permission.object_types are now treated as unordered sets for update comparison purposes.

ovirt.ovirt
~~~~~~~~~~~

- Fix linting issues `(can only concatenate list (not "UndefinedMarker") to list)` (https://github.com/oVirt/ovirt-ansible-collection/pull/771)
- Remove product type in engine_setup role as Red Hat Virtualization is no longer supported (https://github.com/oVirt/ovirt-ansible-collection/pull/779)
- Rework hosted_engine_setup to support new ovirt-engine-appliance(s) built with kiwi  (https://github.com/oVirt/ovirt-ansible-collection/pull/778)

purestorage.flasharray
~~~~~~~~~~~~~~~~~~~~~~

- purefa_connection - Add new parameters for key refresh and connection refresh, as well as ability to update existing connection
- purefa_info - Added more data to hostgroup volume information to support NVMe connections
- purefa_info - Added tags info to entities that support them
- purefa_network - Addressed issues found in update_interface
- purefa_phonehome - Added ``excludes`` parameter, supported from Purity//FA 6.10.0
- purefa_pod - Fixed pydantic issue from lastest SDK version
- purefa_policy - Added Continuous Availability support for SMB policies

purestorage.flashblade
~~~~~~~~~~~~~~~~~~~~~~

- purefa_ad - Added support for local servers using the ``server`` parameter.
- purefb_ad - Added test and rotate states
- purefb_ad - Remove doc references to FQDNs as SPNs are the required method.
- purefb_ad - Updated encryption algorithms to use correct values
- purefb_ds - Allow directory services to be modified for internal NFS servers
- purefb_ds - Update test state to allow specific tests to be run
- purefb_info - Added MAC address information for LAGs

splunk.es
~~~~~~~~~

- Added ``limit`` parameter to splunk_finding_info, splunk_investigation_info, and splunk_response_plan_info modules to control the maximum number of results returned.
- Added splunk_finding module to manage (create/update) Splunk Enterprise Security findings.
- Added splunk_finding_info module to query information about Splunk Enterprise Security findings.
- Added splunk_investigation module to manage (create/update) Splunk Enterprise Security investigations.
- Added splunk_investigation_info module to query information about Splunk Enterprise Security investigations.
- Added splunk_investigation_type module to manage (create/update) Splunk Enterprise Security investigation types (incident types).
- Added splunk_investigation_type_info module to query information about Splunk Enterprise Security investigation types.
- Added splunk_response_plan module to manage (create/update/delete) Splunk Enterprise Security response plans.
- Added splunk_response_plan_execution module to apply/remove response plans to investigations and manage task statuses.
- Added splunk_response_plan_execution_info module to query applied response plans and task statuses on investigations.
- Added splunk_response_plan_info module to query information about Splunk Enterprise Security response plans.
- Modernized Python code across the collection by removing Python 2 compatibility patterns (``from __future__ import`` and ``__metaclass__ = type``), updating to modern ``super()`` syntax, converting ``.format()`` calls to f-strings, and consolidating duplicated ``_check_argspec()`` methods into the shared ``check_argspec()`` helper.
- Removed legacy module support code from module_utils/splunk.py as all modules now use the modern action plugin architecture.
- Removed parse_splunk_args function that was only used by deprecated legacy modules.
- Simplified SplunkRequest class initialization by removing unused parameters (module, headers, override).
- Updated SplunkRequest to require action_module and connection parameters, improving code clarity and maintainability.
- splunk_notes - new module to manage notes for findings, investigations, and response plan tasks.
- splunk_notes_info - new module to query notes from findings, investigations, and response plan tasks.

telekom_mms.icinga_director
~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Feat: add some parameters to the icinga service module (https://github.com/telekom-mms/ansible-collection-icinga-director/pull/289)

theforeman.foreman
~~~~~~~~~~~~~~~~~~

- activation_key - add ``content_view_environments`` parameter to support multi CV (https://github.com/theforeman/foreman-ansible-modules/pull/1935)
- content_view - add support for lifecycle environments in rolling content views
- convert2rhel role - removed subscription support as it's been unused since Katello 4.12 (05/2024)
- job_invocation - add ``feature`` parameter (https://github.com/theforeman/foreman-ansible-modules/pull/1923)
- locations role - Added ``state`` parameter to manage resource presence.

vmware.vmware
~~~~~~~~~~~~~

- Add module vm_snapshot_revert to revert a virtual machine to a snapshot. Fixes https://github.com/ansible-collections/vmware.vmware/issues/281
- cluster_ha - Add value to allow disabling admission control policy Fixes https://github.com/ansible-collections/vmware.vmware/issues/227
- content_library_item_info - Add item storage information to item result
- esxi_hosts - Added option to rename reserved variables to avoid potential conflicts with ansible-core and resolve warnings. fixes https://github.com/ansible-collections/vmware.vmware/issues/273
- module_deploy_vm_base - Removed redundant code by using new vm placement service methods in deploy modules
- vm - Add module to manage virtual machines
- vm - Add the ability to set the annotation of a VM. Fixes https://github.com/ansible-collections/vmware.vmware/issues/310
- vm_apply_customization - Added module to apply different customization specs to a VM
- vm_list_group_by_clusters_info - Add the ability to use the absolute path for the group name. This can be used to avoid group name collisions. Fixes https://github.com/ansible-collections/vmware.vmware/issues/297
- vms - Add setting to disable population of ansible_host to the inventory Fixes https://github.com/ansible-collections/vmware.vmware/pull/317
- vms - Added option to rename reserved variables to avoid potential conflicts with ansible-core and resolve warnings. fixes https://github.com/ansible-collections/vmware.vmware/issues/273

vmware.vmware_rest
~~~~~~~~~~~~~~~~~~

- Disable check mode for all non-info modules in this collection. Check mode was never supported for these modules. Fixes https://github.com/ansible-collections/vmware.vmware_rest/issues/363

vultr.cloud
~~~~~~~~~~~

- Added pagination support by adding ``api_results_per_page`` to the common attributes.
- bare_metal - Added support for multi-disk operation mode by adding ``mdisk_mode`` to the attributes (https://github.com/vultr/ansible-collection-vultr/issues/165).
- object_storage - Object storage subscriptions require specifying a tier upon creation, added ``tier`` to the attributes (https://github.com/vultr/ansible-collection-vultr/issues/135).
- snapshot - Added UEFI support adding ``uefi`` to the attributes (https://github.com/vultr/ansible-collection-vultr/pull/160).

Breaking Changes / Porting Guide
--------------------------------

Ansible-core
~~~~~~~~~~~~

- psrp - Changed the default of ``negotiate_service`` used to build the Kerberos Service Principal Name from ``WSMAN`` to ``host``. This aligns the defaults to how the native PowerShell PSRemoting client works on Windows and ensures that Kerberos can be used by more Windows targets by default. No deprecation period is used for this change as ``host`` is a builtin SPN to Windows and should improve compatibility out of the box. To go back to the old behaviour for any reason, set ``ansible_psrp_negotiate_service=WSMAN`` in the host vars.

community.aws
~~~~~~~~~~~~~

- community.aws collection - Due to the AWS SDKs announcing the end of support for Python less than 3.8 (https://aws.amazon.com/blogs/developer/python-support-policy-updates-for-aws-sdks-and-tools/), support for Python less than 3.8 by this collection has been deprecated and will be removed in release 10.0.0. (https://github.com/ansible-collections/community.aws/pull/2304).

community.mysql
~~~~~~~~~~~~~~~

- Update imports from ansible.module_utils.six to use their python3 equivalent. This change will make this collection incompatible for managed hosts on python2.7.

dellemc.enterprise_sonic
~~~~~~~~~~~~~~~~~~~~~~~~

- sonic_qos_wred - Add support for yellow and red colors (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/574).

splunk.es
~~~~~~~~~

- Removed deprecated modules that were scheduled for removal on 2024-09-01
- adaptive_response_notable_event - Use splunk.es.splunk_adaptive_response_notable_events instead
- correlation_search - Use splunk.es.splunk_correlation_searches instead
- data_input_monitor - Use splunk.es.splunk_data_inputs_monitor instead
- data_input_network - Use splunk.es.splunk_data_inputs_network instead

Deprecated Features
-------------------

- The ``netapp.cloudmanager`` collection is considered unmaintained and will be removed from Ansible 15 if no one starts maintaining it again before Ansible 15.
  See `Collections Removal Process for unmaintained collections <https://docs.ansible.com/projects/ansible/devel/community/collection_contributors/collection_package_removal.html#unmaintained-collections>`__ for more details, including for how this can be cancelled (`https://forum.ansible.com/t/44891 <https://forum.ansible.com/t/44891>`__).
  After removal, users can still install this collection with ``ansible-galaxy collection install netapp.cloudmanager``.

Ansible-core
~~~~~~~~~~~~

- The ``get_all_subclasses()`` function from ``ansible.module_utils.basic`` is deprecated and will be removed in ansible-core 2.24. Use ``get_all_subclasses()`` from ``ansible.module_utils.common._utils`` instead.
- The ``get_platfrom()`` function from ``ansible.module_utils.basic`` is deprecated and will be removed in ansible-core 2.24. Use ``platform.system()`` from the Python standard library instead.
- The ``load_platform_subclass()`` function from ``ansible.module_utils.basic`` is deprecated and will be removed in ansible-core 2.24. Use ``get_platform_subclass()`` from ``ansible.module_utils.common.sys_info`` instead.
- ``PluginLoader`` - Deprecate unused ``aliases`` attribute. Plugins in a collection should define aliases in the ``meta/runtime.yml`` file using the ``redirect`` field instead.
- ``ansible.module_utils.six`` - The ``six`` compatibility library provided at ``ansible.module_utils.six`` is deprecated, and planned for removal in ansible-core 2.24
- apt_key - deprecate in favor of deb822_repository.
- apt_repository - deprecate in favor of deb822_repository.
- connection plugins - Added a soft deprecation on the connection attributes ``has_native_async`` and ``always_pipeline_modules``. Connection plugins that wish to apply custom behaviour around pipelining should instead override the method ``is_pipelining_enabled(self, wrap_async=False)`` added in Ansible 2.19. For backwards compatibility no runtime deprecation warning is emitted but will be in the future.

amazon.aws
~~~~~~~~~~

- aws_ec2 - the ``tags`` host variable has been deprecated to avoid conflicts with Ansible reserved variable names and will be removed in a release after 2026-12-01. Use ``ec2_tags`` instead (https://github.com/ansible-collections/amazon.aws/pull/2847).
- aws_ec2 - the ``use_contrib_script_compatible_ec2_tag_keys`` option has been deprecated and will be removed in a release after 2026-12-01. Use the ``ec2_tags`` structure instead. (https://github.com/ansible-collections/amazon.aws/pull/2854)
- aws_ec2 - the ``use_contrib_script_compatible_sanitization`` option has been deprecated and will be removed in a release after 2026-12-01. Use Ansible's default group name sanitization instead. (https://github.com/ansible-collections/amazon.aws/pull/2854)
- aws_rds - the ``tags`` host variable has been deprecated to avoid conflicts with Ansible reserved variable names and will be removed in a release after 2026-12-01. Use ``rds_tags`` instead (https://github.com/ansible-collections/amazon.aws/pull/2847).
- ec2_vpc_dhcp_option - the ``dhcp_config`` return value has been deprecated and will be removed in a release after 2026-12-01. Use ``dhcp_options`` instead (https://github.com/ansible-collections/amazon.aws/pull/2772).
- ec2_vpc_dhcp_option_info - the ``dhcp_config`` return value has been deprecated and will be removed in a release after 2026-12-01. Use ``dhcp_options`` instead (https://github.com/ansible-collections/amazon.aws/pull/2772).
- route53 - the ``region`` parameter for latency-based routing has been deprecated and will be removed in a release after 2027-06-01. The ``routing_region`` parameter behaves exactly as ``region`` behaves today and should be used instead (https://github.com/ansible-collections/amazon.aws/issues/2893).
- route53 - the ``values`` key in the ``resource_record_sets`` return value has been deprecated in favor of ``record_values`` for Jinja2 compatibility. The ``values`` key will be removed in a release after 2026-12-01 (https://github.com/ansible-collections/amazon.aws/pull/2772).

community.aws
~~~~~~~~~~~~~

- The alias ``aws_acm_info`` for the ``acm_certificate_info`` module has been deprecated. Please use ``community.aws.acm_certificate_info`` instead (https://github.com/ansible-collections/community.aws/pull/2387).
- The alias ``aws_acm`` for the ``acm_certificate`` module has been deprecated. Please use ``community.aws.acm_certificate`` instead (https://github.com/ansible-collections/community.aws/pull/2387).
- The alias ``aws_api_gateway_domain`` for the ``api_gateway_domain`` module has been deprecated. Please use ``community.aws.api_gateway_domain`` instead (https://github.com/ansible-collections/community.aws/pull/2387).
- The alias ``aws_api_gateway`` for the ``api_gateway`` module has been deprecated. Please use ``community.aws.api_gateway`` instead (https://github.com/ansible-collections/community.aws/pull/2387).
- The alias ``aws_application_scaling_policy`` for the ``application_autoscaling_policy`` module has been deprecated. Please use ``community.aws.application_autoscaling_policy`` instead (https://github.com/ansible-collections/community.aws/pull/2387).
- The alias ``aws_batch_compute_environment`` for the ``batch_compute_environment`` module has been deprecated. Please use ``community.aws.batch_compute_environment`` instead (https://github.com/ansible-collections/community.aws/pull/2387).
- The alias ``aws_batch_job_definition`` for the ``batch_job_definition`` module has been deprecated. Please use ``community.aws.batch_job_definition`` instead (https://github.com/ansible-collections/community.aws/pull/2387).
- The alias ``aws_batch_job_queue`` for the ``batch_job_queue`` module has been deprecated. Please use ``community.aws.batch_job_queue`` instead (https://github.com/ansible-collections/community.aws/pull/2387).
- The alias ``aws_codebuild`` for the ``codebuild_project`` module has been deprecated. Please use ``community.aws.codebuild_project`` instead (https://github.com/ansible-collections/community.aws/pull/2387).
- The alias ``aws_codecommit`` for the ``codecommit_repository`` module has been deprecated. Please use ``community.aws.codecommit_repository`` instead (https://github.com/ansible-collections/community.aws/pull/2387).
- The alias ``aws_codepipeline`` for the ``codepipeline`` module has been deprecated. Please use ``community.aws.codepipeline`` instead (https://github.com/ansible-collections/community.aws/pull/2387).
- The alias ``aws_config_aggregation_authorization`` for the ``config_aggregation_authorization`` module has been deprecated. Please use ``community.aws.config_aggregation_authorization`` instead (https://github.com/ansible-collections/community.aws/pull/2387).
- The alias ``aws_config_aggregator`` for the ``config_aggregator`` module has been deprecated. Please use ``community.aws.config_aggregator`` instead (https://github.com/ansible-collections/community.aws/pull/2387).
- The alias ``aws_config_delivery_channel`` for the ``config_delivery_channel`` module has been deprecated. Please use ``community.aws.config_delivery_channel`` instead (https://github.com/ansible-collections/community.aws/pull/2387).
- The alias ``aws_config_recorder`` for the ``config_recorder`` module has been deprecated. Please use ``community.aws.config_recorder`` instead (https://github.com/ansible-collections/community.aws/pull/2387).
- The alias ``aws_config_rule`` for the ``config_rule`` module has been deprecated. Please use ``community.aws.config_rule`` instead (https://github.com/ansible-collections/community.aws/pull/2387).
- The alias ``aws_direct_connect_confirm_connection`` for the ``directconnect_confirm_connection`` module has been deprecated. Please use ``community.aws.directconnect_confirm_connection`` instead (https://github.com/ansible-collections/community.aws/pull/2387).
- The alias ``aws_direct_connect_connection`` for the ``directconnect_connection`` module has been deprecated. Please use ``community.aws.directconnect_connection`` instead (https://github.com/ansible-collections/community.aws/pull/2387).
- The alias ``aws_direct_connect_gateway`` for the ``directconnect_gateway`` module has been deprecated. Please use ``community.aws.directconnect_gateway`` instead (https://github.com/ansible-collections/community.aws/pull/2387).
- The alias ``aws_direct_connect_link_aggregation_group`` for the ``directconnect_link_aggregation_group`` module has been deprecated. Please use ``community.aws.directconnect_link_aggregation_group`` instead (https://github.com/ansible-collections/community.aws/pull/2387).
- The alias ``aws_direct_connect_virtual_interface`` for the ``directconnect_virtual_interface`` module has been deprecated. Please use ``community.aws.directconnect_virtual_interface`` instead (https://github.com/ansible-collections/community.aws/pull/2387).
- The alias ``aws_eks_cluster`` for the ``eks_cluster`` module has been deprecated. Please use ``community.aws.eks_cluster`` instead (https://github.com/ansible-collections/community.aws/pull/2387).
- The alias ``aws_elasticbeanstalk_app`` for the ``elasticbeanstalk_app`` module has been deprecated. Please use ``community.aws.elasticbeanstalk_app`` instead (https://github.com/ansible-collections/community.aws/pull/2387).
- The alias ``aws_glue_connection`` for the ``glue_connection`` module has been deprecated. Please use ``community.aws.glue_connection`` instead (https://github.com/ansible-collections/community.aws/pull/2387).
- The alias ``aws_glue_crawler`` for the ``glue_crawler`` module has been deprecated. Please use ``community.aws.glue_crawler`` instead (https://github.com/ansible-collections/community.aws/pull/2387).
- The alias ``aws_glue_job`` for the ``glue_job`` module has been deprecated. Please use ``community.aws.glue_job`` instead (https://github.com/ansible-collections/community.aws/pull/2387).
- The alias ``aws_inspector_target`` for the ``inspector_target`` module has been deprecated. Please use ``community.aws.inspector_target`` instead (https://github.com/ansible-collections/community.aws/pull/2387).
- The alias ``aws_kms_info`` for the ``kms_key_info`` module has been deprecated. Please use ``amazon.aws.kms_key_info`` instead (https://github.com/ansible-collections/community.aws/pull/2387).
- The alias ``aws_kms`` for the ``kms_key`` module has been deprecated. Please use ``amazon.aws.kms_key`` instead (https://github.com/ansible-collections/community.aws/pull/2387).
- The alias ``aws_msk_cluster`` for the ``msk_cluster`` module has been deprecated. Please use ``community.aws.msk_cluster`` instead (https://github.com/ansible-collections/community.aws/pull/2387).
- The alias ``aws_msk_config`` for the ``msk_config`` module has been deprecated. Please use ``community.aws.msk_config`` instead (https://github.com/ansible-collections/community.aws/pull/2387).
- The alias ``aws_s3_bucket_info`` for the ``s3_bucket_info`` module has been deprecated. Please use ``amazon.aws.s3_bucket_info`` instead (https://github.com/ansible-collections/community.aws/pull/2387).
- The alias ``aws_s3_cors`` for the ``s3_cors`` module has been deprecated. Please use ``community.aws.s3_cors`` instead (https://github.com/ansible-collections/community.aws/pull/2387).
- The alias ``aws_secret`` for the ``secretsmanager_secret`` module has been deprecated. Please use ``community.aws.secretsmanager_secret`` instead (https://github.com/ansible-collections/community.aws/pull/2387).
- The alias ``aws_ses_identity_policy`` for the ``ses_identity_policy`` module has been deprecated. Please use ``community.aws.ses_identity_policy`` instead (https://github.com/ansible-collections/community.aws/pull/2387).
- The alias ``aws_ses_identity`` for the ``ses_identity`` module has been deprecated. Please use ``community.aws.ses_identity`` instead (https://github.com/ansible-collections/community.aws/pull/2387).
- The alias ``aws_ses_rule_set`` for the ``ses_rule_set`` module has been deprecated. Please use ``community.aws.ses_rule_set`` instead (https://github.com/ansible-collections/community.aws/pull/2387).
- The alias ``aws_sgw_info`` for the ``storagegateway_info`` module has been deprecated. Please use ``community.aws.storagegateway_info`` instead (https://github.com/ansible-collections/community.aws/pull/2387).
- The alias ``aws_ssm_parameter_store`` for the ``ssm_parameter`` module has been deprecated. Please use ``community.aws.ssm_parameter`` instead (https://github.com/ansible-collections/community.aws/pull/2387).
- The alias ``aws_step_functions_state_machine_execution`` for the ``stepfunctions_state_machine_execution`` module has been deprecated. Please use ``community.aws.stepfunctions_state_machine_execution`` instead (https://github.com/ansible-collections/community.aws/pull/2387).
- The alias ``aws_step_functions_state_machine`` for the ``stepfunctions_state_machine`` module has been deprecated. Please use ``community.aws.stepfunctions_state_machine`` instead (https://github.com/ansible-collections/community.aws/pull/2387).
- The alias ``aws_waf_condition`` for the ``waf_condition`` module has been deprecated. Please use ``community.aws.waf_condition`` instead (https://github.com/ansible-collections/community.aws/pull/2387).
- The alias ``aws_waf_info`` for the ``waf_info`` module has been deprecated. Please use ``community.aws.waf_info`` instead (https://github.com/ansible-collections/community.aws/pull/2387).
- The alias ``aws_waf_rule`` for the ``waf_rule`` module has been deprecated. Please use ``community.aws.waf_rule`` instead (https://github.com/ansible-collections/community.aws/pull/2387).
- The alias ``aws_waf_web_acl`` for the ``waf_web_acl`` module has been deprecated. Please use ``community.aws.waf_web_acl`` instead (https://github.com/ansible-collections/community.aws/pull/2387).
- The alias ``cloudfront_info`` for the ``cloudfront_distribution_info`` module has been deprecated. Please use ``community.aws.cloudfront_distribution_info`` instead (https://github.com/ansible-collections/community.aws/pull/2387).
- The alias ``cloudtrail`` for the ``cloudtrail`` module has been deprecated. Please use ``amazon.aws.cloudtrail`` instead (https://github.com/ansible-collections/community.aws/pull/2387).
- The alias ``ec2_asg_info`` for the ``autoscaling_group_info`` module has been deprecated. Please use ``amazon.aws.autoscaling_group_info`` instead (https://github.com/ansible-collections/community.aws/pull/2387).
- The alias ``ec2_asg_instance_refresh_info`` for the ``autoscaling_instance_refresh_info`` module has been deprecated. Please use ``amazon.aws.autoscaling_instance_refresh_info`` instead (https://github.com/ansible-collections/community.aws/pull/2387).
- The alias ``ec2_asg_instance_refresh`` for the ``autoscaling_instance_refresh`` module has been deprecated. Please use ``amazon.aws.autoscaling_instance_refresh`` instead (https://github.com/ansible-collections/community.aws/pull/2387).
- The alias ``ec2_asg_lifecycle_hook`` for the ``autoscaling_lifecycle_hook`` module has been deprecated. Please use ``community.aws.autoscaling_lifecycle_hook`` instead (https://github.com/ansible-collections/community.aws/pull/2387).
- The alias ``ec2_asg_scheduled_action`` for the ``autoscaling_scheduled_action`` module has been deprecated. Please use ``community.aws.autoscaling_scheduled_action`` instead (https://github.com/ansible-collections/community.aws/pull/2387).
- The alias ``ec2_asg`` for the ``autoscaling_group`` module has been deprecated. Please use ``amazon.aws.autoscaling_group`` instead (https://github.com/ansible-collections/community.aws/pull/2387).
- The alias ``ec2_lc_find`` for the ``autoscaling_launch_config_find`` module has been deprecated. Please use ``community.aws.autoscaling_launch_config_find`` instead (https://github.com/ansible-collections/community.aws/pull/2387).
- The alias ``ec2_lc_info`` for the ``autoscaling_launch_config_info`` module has been deprecated. Please use ``community.aws.autoscaling_launch_config_info`` instead (https://github.com/ansible-collections/community.aws/pull/2387).
- The alias ``ec2_lc`` for the ``autoscaling_launch_config`` module has been deprecated. Please use ``community.aws.autoscaling_launch_config`` instead (https://github.com/ansible-collections/community.aws/pull/2387).
- The alias ``ec2_metric_alarm`` for the ``cloudwatch_metric_alarm`` module has been deprecated. Please use ``amazon.aws.cloudwatch_metric_alarm`` instead (https://github.com/ansible-collections/community.aws/pull/2387).
- The alias ``ec2_scaling_policy`` for the ``autoscaling_policy`` module has been deprecated. Please use ``community.aws.autoscaling_policy`` instead (https://github.com/ansible-collections/community.aws/pull/2387).
- The alias ``execute_lambda`` for the ``lambda_execute`` module has been deprecated. Please use ``amazon.aws.lambda_execute`` instead (https://github.com/ansible-collections/community.aws/pull/2387).
- cloudfront_distribution - The ``items`` return value in ``active_trusted_signers`` has been deprecated and will be removed in a release after 2026-12-15. Use ``elements`` instead (https://github.com/ansible-collections/community.aws/pull/2354).
- cloudfront_distribution - The ``items`` return value in ``aliases`` has been deprecated and will be removed in a release after 2026-12-15. Use ``elements`` instead (https://github.com/ansible-collections/community.aws/pull/2354).
- cloudfront_distribution - The ``items`` return value in ``cache_behaviors.items.allowed_methods.cached_methods`` has been deprecated and will be removed in a release after 2026-12-15. Use ``elements`` instead (https://github.com/ansible-collections/community.aws/pull/2354).
- cloudfront_distribution - The ``items`` return value in ``cache_behaviors.items.allowed_methods`` has been deprecated and will be remove in a release after 2026-12-15. Use ``elements`` instead (https://github.com/ansible-collections/community.aws/pull/2354).
- cloudfront_distribution - The ``items`` return value in ``cache_behaviors.items.forwarded_values.cookies.whitelisted_names`` has been deprecated and will be remove in a release after 2026-12-15. Use ``elements`` instead (https://github.com/ansible-collections/community.aws/pull/2354).
- cloudfront_distribution - The ``items`` return value in ``cache_behaviors.items.forwarded_values.headers`` has been deprecated and will be remove in a release after 2026-12-15. Use ``elements`` instead (https://github.com/ansible-collections/community.aws/pull/2354).
- cloudfront_distribution - The ``items`` return value in ``cache_behaviors.items.forwarded_values.query_string_cache_keys`` has been deprecated and will be remove in a release after 2026-12-15. Use ``elements`` instead (https://github.com/ansible-collections/community.aws/pull/2354).
- cloudfront_distribution - The ``items`` return value in ``cache_behaviors.items.lambda_function_associations`` has been deprecated and will be remove in a release after 2026-12-15. Use ``elements`` instead (https://github.com/ansible-collections/community.aws/pull/2354).
- cloudfront_distribution - The ``items`` return value in ``cache_behaviors`` has been deprecated and will be remove in a release after 2026-12-15. Use ``elements`` instead (https://github.com/ansible-collections/community.aws/pull/2354).
- cloudfront_distribution - The ``items`` return value in ``custom_error_responses`` has been deprecated and will be remove in a release after 2026-12-15. Use ``elements`` instead (https://github.com/ansible-collections/community.aws/pull/2354).
- cloudfront_distribution - The ``items`` return value in ``default_cache_behavior.allowed_methods.cached_methods`` has been deprecated and will be remove in a release after 2026-12-15. Use ``elements`` instead (https://github.com/ansible-collections/community.aws/pull/2354).
- cloudfront_distribution - The ``items`` return value in ``default_cache_behavior.allowed_methods`` has been deprecated and will be remove in a release after 2026-12-15. Use ``elements`` instead (https://github.com/ansible-collections/community.aws/pull/2354).
- cloudfront_distribution - The ``items`` return value in ``default_cache_behavior.forwarded_values.cookies.whitelisted_names`` has been deprecated and will be remove in a release after 2026-12-15. Use ``elements`` instead (https://github.com/ansible-collections/community.aws/pull/2354).
- cloudfront_distribution - The ``items`` return value in ``default_cache_behavior.forwarded_values.headers`` has been deprecated and will be remove in a release after 2026-12-15. Use ``elements`` instead (https://github.com/ansible-collections/community.aws/pull/2354).
- cloudfront_distribution - The ``items`` return value in ``default_cache_behavior.forwarded_values.query_string_cache_keys`` has been deprecated and will be remove in a release after 2026-12-15. Use ``elements`` instead (https://github.com/ansible-collections/community.aws/pull/2354).
- cloudfront_distribution - The ``items`` return value in ``default_cache_behavior.lambda_function_associations`` has been deprecated and will be remove in a release after 2026-12-15. Use ``elements`` instead (https://github.com/ansible-collections/community.aws/pull/2354).
- cloudfront_distribution - The ``items`` return value in ``origins.items.custom_origin_config.origin_ssl_protocols`` has been deprecated and will be remove in a release after 2026-12-15. Use ``elements`` instead (https://github.com/ansible-collections/community.aws/pull/2354).
- cloudfront_distribution - The ``items`` return value in ``origins`` has been deprecated and will be remove in a release after 2026-12-15. Use ``elements`` instead (https://github.com/ansible-collections/community.aws/pull/2354).
- cloudfront_distribution - The ``items`` return value in ``restrictions.geo_restriction`` has been deprecated and will be remove in a release after 2026-12-15. Use ``elements`` instead (https://github.com/ansible-collections/community.aws/pull/2354).
- cloudfront_invalidation - The ``items`` return value in ``invalidation.invalidation_batch.paths`` has been deprecated and will be remove in a release after 2026-12-15. Use ``elements`` instead (https://github.com/ansible-collections/community.aws/pull/2354).
- cloudfront_invalidation - The ``items`` return value in ``invalidation.invalidation_batch.paths`` has been deprecated and will be removed in a release after 2026-12-15. Use ``elements`` instead (https://github.com/ansible-collections/community.aws/pull/2354).
- waf_condition - The module has been deprecated as Amazon has retired the ``WAF Classic`` service. Please use the ``AWS WAF (WAFv2)`` service and modules instead. The module will be removed in version 12.0.0 (https://github.com/ansible-collections/community.aws/pull/2389).
- waf_info - The module has been deprecated as Amazon has retired the ``WAF Classic`` service. Please use the ``AWS WAF (WAFv2)`` service and modules instead. The module will be removed in version 12.0.0 (https://github.com/ansible-collections/community.aws/pull/2389).
- waf_rule - The module has been deprecated as Amazon has retired the ``WAF Classic`` service. Please use the ``AWS WAF (WAFv2)`` service and modules instead. The module will be removed in version 12.0.0 (https://github.com/ansible-collections/community.aws/pull/2389).
- waf_web_acl - The module has been deprecated as Amazon has retired the ``WAF Classic`` service. Please use the ``AWS WAF (WAFv2)`` service and modules instead. The module will be removed in version 12.0.0 (https://github.com/ansible-collections/community.aws/pull/2389).

community.general
~~~~~~~~~~~~~~~~~

- All module utils, plugin utils, and doc fragments will be made **private** in community.general 13.0.0. This means that they will no longer be part of the public API of the collection, and can have breaking changes even in bugfix releases. If you depend on importing code from the module or plugin utils, or use one of the doc fragments, please `comment in the issue to discuss this <https://github.com/ansible-collections/community.general/issues/11312>`__. Note that this does not affect any use of community.general in task files, roles, or playbooks (https://github.com/ansible-collections/community.general/issues/11312, https://github.com/ansible-collections/community.general/pull/11320).
- aix_devices - module is superseded by equivalent in ``ibm.power_aix`` collection. It will be removed from community.general 15.0.0 (https://github.com/ansible-collections/community.general/issues/11290, https://github.com/ansible-collections/community.general/pull/11540).
- aix_filesystem - module is superseded by equivalent in ``ibm.power_aix`` collection. It will be removed from community.general 15.0.0 (https://github.com/ansible-collections/community.general/issues/11290, https://github.com/ansible-collections/community.general/pull/11540).
- aix_inittab - module is superseded by equivalent in ``ibm.power_aix`` collection. It will be removed from community.general 15.0.0 (https://github.com/ansible-collections/community.general/issues/11290, https://github.com/ansible-collections/community.general/pull/11540).
- aix_lvg - module is superseded by equivalent in ``ibm.power_aix`` collection. It will be removed from community.general 15.0.0 (https://github.com/ansible-collections/community.general/issues/11290, https://github.com/ansible-collections/community.general/pull/11540).
- aix_lvol - module is superseded by equivalent in ``ibm.power_aix`` collection. It will be removed from community.general 15.0.0 (https://github.com/ansible-collections/community.general/issues/11290, https://github.com/ansible-collections/community.general/pull/11540).
- cloud module utils - this module utils is not used by community.general and will thus be removed from community.general 13.0.0. If you are using it from another collection, please copy it over (https://github.com/ansible-collections/community.general/pull/11205).
- database module utils - this module utils is not used by community.general and will thus be removed from community.general 13.0.0. If you are using it from another collection, please copy it over (https://github.com/ansible-collections/community.general/pull/11205).
- dconf - deprecate fallback mechanism when ``gi.repository`` is not available; fallback will be removed in community.general 15.0.0 (https://github.com/ansible-collections/community.general/pull/11088).
- known_hosts module utils - this module utils is not used by community.general and will thus be removed from community.general 13.0.0. If you are using it from another collection, please copy it over (https://github.com/ansible-collections/community.general/pull/11205).
- layman - ClearLinux was made EOL in July 2025.; the module will be removed from community.general 15.0.0 (https://github.com/ansible-collections/community.general/pull/11087).
- layman - Gentoo deprecated ``layman`` in mid-2023; the module will be removed from community.general 14.0.0 (https://github.com/ansible-collections/community.general/pull/11070).
- monit - support for Monit version 5.18 or older is deprecated and will be removed in community.general 14.0.0 (https://github.com/ansible-collections/community.general/pull/11254).
- puppet - the ``timeout`` parameter is deprecated and will be removed in community.general 14.0.0. (https://github.com/ansible-collections/community.general/pull/11658).
- pushbullet - module relies on Python package supporting Python 3.2 only; the module will be removed from community.general 13.0.0 (https://github.com/ansible-collections/community.general/pull/11224).
- saslprep module utils - this module utils is not used by community.general and will thus be removed from community.general 13.0.0. If you are using it from another collection, please copy it over (https://github.com/ansible-collections/community.general/pull/11205).
- spotinst_aws_elastigroup - module relies on Python package supporting Python 2.7 only; the module will be removed from community.general 13.0.0 (https://github.com/ansible-collections/community.general/pull/11069).

community.proxmox
~~~~~~~~~~~~~~~~~

- proxmox - Certificate verification default changes from ``false`` to ``true`` with version 2.0.0 (https://github.com/ansible-collections/community.proxmox/pull/256).

community.routeros
~~~~~~~~~~~~~~~~~~

- api_find_and_modify - the current defaults for ``ignore_dynamic`` and ``ignore_builtin`` (both ``false``) have been deprecated and will change to ``true`` in community.routeros 4.0.0. To avoid deprecation messages, please set the value explicitly to ``true`` or ``false``, if you have not already done so. We recommend to set them to ``true``, unless you have a good reason to set them to ``false`` (https://github.com/ansible-collections/community.routeros/pull/399).

hetzner.hcloud
~~~~~~~~~~~~~~

- hcloud inventory - The ``hcloud_datacenter`` host variable is deprecated and will be removed after 1 July 2026. Please use the ``hcloud_location`` host variable instead.
- network_info - The ``hcloud_network_info[].servers[].datacenter`` return value is deprecated and will be removed after 1 July 2026. Please use the ``hcloud_network_info[].servers[].location`` return value instead.
- primary_ip - The ``datacenter`` argument is deprecated and will be removed after 1 July 2026. Please use the ``location`` argument instead.
- primary_ip - The ``hcloud_primary_ip.datacenter`` return value is deprecated and will be removed after 1 July 2026. Please use the ``hcloud_primary_ip.location`` return value instead.
- primary_ip_info - The ``hcloud_primary_ip_info[].datacenter`` return value is deprecated and will be removed after 1 July 2026. Please use the ``hcloud_primary_ip_info[].location`` return value instead.
- server - The ``datacenter`` argument is deprecated and will be removed after 1 July 2026. Please use the ``location`` argument instead.
- server - The ``hcloud_server.datacenter`` return value is deprecated and will be removed after 1 July 2026. Please use the ``hcloud_server.location`` return value instead.
- server_info - The ``hcloud_server_info[].datacenter`` return value is deprecated and will be removed after 1 July 2026. Please use the ``hcloud_server_info[].location`` return value instead.

kubernetes.core
~~~~~~~~~~~~~~~

- helm - the ``status.values`` return value has been deprecated and will be removed in a release after 2027-01-08. Use ``status.release_values`` instead (https://github.com/ansible-collections/kubernetes.core/pull/1056).
- helm_info - the ``status.values`` return value has been deprecated and will be removed in a release after 2027-01-08. Use ``status.release_values`` instead (https://github.com/ansible-collections/kubernetes.core/pull/1056).

vmware.vmware_rest
~~~~~~~~~~~~~~~~~~

- Deprecate modules that have been moved to the new vmware.vmware collection. Includes vcenter_vm_guest_customization, vcenter_vm_hardware_adapter_sata, vcenter_vm_hardware_adapter_scsi, vcenter_vm_hardware_cdrom, vcenter_vm_hardware_cpu, vcenter_vm_hardware_disk, vcenter_vm_hardware_ethernet, vcenter_vm_hardware_memory, vcenter_vm

Removed Features (previously deprecated)
----------------------------------------

- The awx.awx collection has been removed from Ansible 14.
  The collection is undergoing a heavy \ `refactoring <https://forum.ansible.com/t/7404>`__ and currently does not align with the standards for the community package.
  See `the removal discussion <https://forum.ansible.com/t/44706>`__ for details.
  Users can still install this collection with ``ansible-galaxy collection install awx.awx``.
- The deprecated ``cisco.dnac`` collection has been removed (`https://forum.ansible.com/t/45609 <https://forum.ansible.com/t/45609>`__).
- The deprecated ``junipernetworks.junos`` collection has been removed (`https://forum.ansible.com/t/44869 <https://forum.ansible.com/t/44869>`__).

Ansible-core
~~~~~~~~~~~~

- Removed 'required' option from get_bin_path API (https://github.com/ansible/ansible/issues/85998).
- Removed deprecated ``ansible.builtin.paramiko`` connection plugin (https://github.com/ansible/ansible/issues/86002). Setting the ``connection`` keyword to ``persistent`` or ``smart`` no longer attempts to use ``paramiko``.
- Removed deprecated ``ansible.module_utils.compat.paramiko`` (https://github.com/ansible/ansible/issues/86001).
- Removed deprecated ``handle_stats_and_callbacks`` parameter of the ``StrategyBase._load_included_file`` method. (https://github.com/ansible/ansible/issues/86003)
- Removed deprecated ability to import ``datetime``, ``signal``, ``types``, ``chain``, ``repeat``, ``map`` and ``shlex_quote`` from ``ansible.module_utils.basic``.
- compat.datetime - removed deprecated datetime compat APIs (https://github.com/ansible/ansible/issues/86000).
- git - removed deprecated alias gpg_whitelist (https://github.com/ansible/ansible/issues/86004).
- interpreter_discovery - removed auto_legacy and auto_legacy_slient options (https://github.com/ansible/ansible/issues/85995).
- module_utils - Remove previously deprecated ``safe_eval`` function (#85996) (#85999)

splunk.es
~~~~~~~~~

- adaptive_response_notable_event module has been removed. Use splunk.es.splunk_adaptive_response_notable_events resource module instead.
- correlation_search module has been removed. Use splunk.es.splunk_correlation_searches resource module instead.
- correlation_search_info module has been removed. Use splunk.es.splunk_correlation_search_info instead.
- data_input_monitor module has been removed. Use splunk.es.splunk_data_inputs_monitor resource module instead.
- data_input_network module has been removed. Use splunk.es.splunk_data_inputs_network resource module instead.

Security Fixes
--------------

amazon.aws
~~~~~~~~~~

- arn - fix potential ReDoS vulnerability in ARN parsing regex by using negated character class instead of non-greedy quantifier (https://github.com/ansible-collections/amazon.aws/pull/2884).
- ec2_security_group - fix potential ReDoS vulnerability in security group ID parsing regex by using negated character classes and adding end anchor (https://github.com/ansible-collections/amazon.aws/pull/2884).

ansible.windows
~~~~~~~~~~~~~~~

- win_dns_record - Fixed a security risk where ``AllowUpdateAny`` was hardcoded for non-SRV records, allowing any authenticated user to update DNS records. Added a new parameter ``allow_update_any`` which defaults to ``false`` (https://issues.redhat.com/browse/ACA-5193).

kubernetes.core
~~~~~~~~~~~~~~~

- Selectively redact sensitive info from kubeconfig instead of applying blanket ``no_log=True`` (https://github.com/ansible-collections/kubernetes.core/pull/1014).

Bugfixes
--------

Ansible-core
~~~~~~~~~~~~

- Fix Windows LIB env var corruption (https://github.com/ansible-collections/ansible.windows/issues/297).
- Fix ``AnsibleModule.human_to_bytes()``, which was never adjusted after the standalone ``human_to_bytes()`` got a new parameter ``default_unit`` (https://github.com/ansible/ansible/pull/85259).
- Fix interpreter discovery on delegated ``async`` tasks (https://github.com/ansible/ansible/issues/86491)
- Fix source metadata validation (https://github.com/ansible/ansible/pull/86320).
- Fix up ``powershell`` shell commands when using a connection plugin that does not support stdin/pipeline input - https://github.com/ansible/ansible/issues/86397
- Fix up the Action plugin ``_make_tmp_path`` error to only include the command run rather than the shell's dataclass repr from ``mkdtemp``.
- Variable loading now uses file source instead of variables when invalidly formmated vars file is loaded.
- Windows - ignore temporary file cleanup warning when using AnsibleModule to compile C# utils. This should reduce the number of warnings that can safely be ignored when running PowerShell modules - https://github.com/ansible/ansible/issues/85976
- ``ansible-galaxy collection list`` - issue a warning when a collection's namespace and name do not match its filepath. (https://github.com/ansible/ansible/issues/69813)
- ``ansible-galaxy collection list|install`` - list collections based on reference (the fqcn used to refer to them in a playbook), not based on their documented name. (https://github.com/ansible/ansible/issues/69813)
- ``ansible-galaxy collection verify`` - fail collection verification when a collection's namespace and name  do not match its filepath. (https://github.com/ansible/ansible/issues/69813)
- ``ansible-galaxy install``/``ansible-galaxy collection download`` - collections from git repositories with a tag or sha version no longer emit detached head warning messages (https://github.com/ansible/ansible/issues/86169).
- ``ansible.builtin.pip`` - Running the built-in pip module with ``check_mode`` and packages coming from VCS URLs, archives, or local filepaths now correctly outputs the ``changed`` status of the task. Previously, it was always reported as changed due to improper package name resolution.  (https://github.com/ansible/ansible/pull/85623)
- ``ansible``, ``ansible-console`` - fix executing ``- meta: end_play`` tasks.
- ansible-connection - Prevent unpickling failures in module contexts by ensuring that AnsibleTaggedObjects in pickled responses are converted to plain types in ``JsonRpcServer``.
- ansible-galaxy - raise an error when wrong regex value specified in collection_skeleton_ignore.
- ansible-galaxy - warn instead of raising an error when no valid role or collections paths exist (https://github.com/ansible/ansible/pull/86341)
- ansible-galaxy collection - Fix using the server configuration for ``validate_certs`` when downloading collections. (https://github.com/ansible/ansible/issues/86694)
- ansible-test - Add missing bootstrapping for a target Python version in a controller container.
- ansible-test - Fix docker hostname parsing
- ansible-test - Fix traceback when requesting windows integration tests for multiple managed hosts.
- ansible-test - Missing git submodules in the source tree now result in a warning instead of an error.
- ansible-test - Restore code coverage reporting for Python code residing in integration tests.
- ansible-test - The runtime-metadata sanity test now ignores pre-release and build identifiers in collection versions. This prevents errors if a tombstone version is ``X.0.0``, while the collection's version is ``X.0.0-prerelease`` (https://github.com/ansible/ansible/issues/85193)."
- ansible-test - Upgrade ``expat`` during provisioning of Fedora 42 remote instances.
- ansible-test - When using the ``env --list-files`` option, non-filename output is now sent to stderr.
- ansible_facts[os_*] - Contained wrong information, if ClearLinux parsing was tried before falling back to general os-release parsing
- ansible_local will no longer trigger variable injection default value deprecation.
- ansible_virtualization_role and ansible_virtualization_type facts - fix the detection of vms running inside FreeBSD Bhyve hypervisor and detection of jails  (https://github.com/ansible/ansible/pull/85767)
- apt - Stop the >= operator from being ignored for packages that are not already installed (https://github.com/ansible/ansible/pull/85254)
- apt - handle comma separated packages from recommends while installing local deb package (https://github.com/ansible/ansible/issues/86609).
- apt - recreate the APT lists directory (/var/lib/apt/lists by default) if missing (https://github.com/ansible/ansible/issues/61176).
- basic - fail in controlled manner when ``run_command()`` attempts to parse a command with broken syntax passed in as a string (https://github.com/ansible/ansible/issues/85719).
- cache plugins based on the BaseFileCache class will now sanitize keys to avoid names that could cause issues with the storage path
- callbacks - The value of ``TaskResult.task.connection`` properly reflects the loaded connection name used. Previously, incorrect values were reported in some cases.
- config lookup now properly factors in variables and show_origin when checking entries from the global configuration.
- config lookup now uses preexisting constants for templating when needed.
- copy - honor directory_mode when copying directories with remote_src=True (https://github.com/ansible/ansible/issues/81292).
- copy - when a single-file local directory was specified as the source, ``changed`` used to be ``false`` even when the source was actually copied. It now makes sure ``changed`` is ``true`` in this case. (https://github.com/ansible/ansible/issues/85833)
- deb822_repository - Remove ``Install-Python-Debian`` from files outputted by the ``deb822_repository`` module (https://github.com/ansible/ansible/issues/86395)
- deb822_repository no longer over-normalizes repository names when generating sources list filenames, preventing collisions for names that differ by case, underscores, or dots (https://github.com/ansible/ansible/issues/86243)
- display - Fix ``getuser`` fallback error handling on Python 3.13 and later. (https://github.com/ansible/ansible/issues/86142)
- dnf - When installing a dnf module, install and enable when missing, upgrade when present (https://github.com/ansible/ansible/issues/73457)
- dnf - fix package installation when specifying architecture without version (e.g., ``libgcc.i686``) where a different architecture of the same package is already installed (https://github.com/ansible/ansible/issues/86156).
- dnf5 - return failure message which occurred while running RPM scriptlet (https://github.com/ansible/ansible/issues/86117).
- file module - issue warning when attempting to access files/directories the user lacks permissions on instead of silently treating them as absent (https://github.com/ansible/ansible/issues/57573)
- first_found - Correct the "Include tasks only if one of the files exists, otherwise skip" example.
- first_found - ensure file lookup under ``files`` directory when the task action cannot be resolved (https://github.com/ansible/ansible/issues/85655).
- first_found - use the task action to determine the directory (templates/vars/files) containing the file when the lookup is not used as task loop.
- galaxy - previously, some corrupted cache files could cause Ansible Galaxy to fail with a traceback. This has been corrected to display a clear error message explaining how to resolve the problem. (https://github.com/ansible/ansible/issues/85918)
- get_url - fix regex for GNU Digest line which is used in comparing checksums (https://github.com/ansible/ansible/issues/86132).
- getent - handle non-empty string for split parameter value (https://github.com/ansible/ansible/issues/85720).
- git - Correct the output of git checkmode to a failure when the ``version`` supplied is an invalid ref (https://github.com/ansible/ansible/issues/51580)
- include_role would emit a syntax error on X_from options errors, but a task failure when missing a role to make it consistent now it also emits a task failure on missing tasks_from, which makes it subject to error handling in the play.
- include_role, would ignore missing X_from files if the subdir (tasks/vars/handlers/defaults) did not exist, now it is a proper error.
- iptables - The module can now detect when a extensions added with the module ``match`` argument have  been automatically imported by other module arguments such as ``uid_owner`` and prevents duplicate extension imports which previously caused an error (https://github.com/ansible/ansible/issues/84387). 
- local connection - Fix ``getuser`` fallback error handling on Python 3.13 and later.
- local connection - Pass correct type to become plugins when checking password (https://github.com/ansible/ansible/issues/86458)
- modules - fix AnsiballZ wrapper code escaping of sitecustomize
- option argument deprecations now have a proper alternative help text.
- package, service, gather_facts - fix templating module_defaults for modules executed by these action plugins. (https://github.com/ansible/ansible/issues/85848)
- package_facts - typecast bytes to string while returning facts (https://github.com/ansible/ansible/issues/85937).
- password lookup plugin - replace random.SystemRandom() with secrets.SystemRandom() when generating passwords (https://github.com/ansible/ansible/issues/85956, https://github.com/ansible/ansible/pull/85971).
- pip - Prevent passing ``-e`` to ``pip`` when the ``editable`` and ``requirements`` parameters are both used.
- pip - When installing multiple packages with ``editable=True``, ensure each package is editable (https://github.com/ansible/ansible/issues/77755).
- pluginloader - Fixed non-collection load path for builtin non-Jinja plugins to consult deprecation metadata.
- psrp - ReadTimeout exceptions now mark host as unreachable instead of fatal (https://github.com/ansible/ansible/issues/85966)
- rpm_key - Use librpm library API instead of gpg utility to support version 6 PGP keys (https://github.com/ansible/ansible/issues/86157).
- ssh connection plugin - fix resource leaks when using sshpass
- task conditionals - An error in any task conditional (e.g., ``when``, ``until``, ``failed_when``) always causes the task to report a descriptive failure while preserving the task result. The resulting task failure is always recoverable via ``ignore_errors``. Previous inconsistent error handling in task conditionals could result in warnings, loss of completed task results, recoverable task errors, unrecoverable task errors, or failure of the Ansible controller process.
- template module - Report the line number for Jinja syntax errors in template files.
- templating - Fix traceback when using ``deepcopy`` on an imported template (https://github.com/ansible/ansible/issues/86723).
- to_yaml / to_nice_yaml filters - Restore pre-2.19 decryption behavior for vaulted values (https://github.com/ansible/ansible/issues/85722). A regression in 2.19.0 previously caused vaulted values to be dumped as ``!vault``-tagged ciphertext.
- unarchive - make timezone aware timestamp for comparison (https://github.com/ansible/ansible/issues/85779).
- user - ``user`` module integration tests can now run multiple times on the same freebsd host (https://github.com/ansible/ansible/issues/86541).
- user - create accounts in an unlocked state by default on BusyBox (https://github.com/ansible/ansible/issues/68676)
- user - emit a warning when the ``seuser`` parameter is set on a system where SELinux is not enabled, instead of silently ignoring it (https://github.com/ansible/ansible/issues/85542).
- user - fix ``FreeBsdUser`` to not create ``/nonexistent`` directory when modifying user to add them to a group on FreeBSD (https://github.com/ansible/ansible/issues/86368)
- user - fix modifying users on BusyBox (https://github.com/ansible/ansible/issues/66679)
- user - make option group required_by option append.
- user - preserve existing password when modifying accounts on BusyBox systems (https://github.com/ansible/ansible/pull/86530)
- user - raise an error if force=true is used while deleting the group on BusyBox based distros (https://github.com/ansible/ansible/issues/85565).
- user - return the actual system groups the user belongs to instead of only the groups specified in the module input (https://github.com/ansible/ansible/issues/80669).
- winrm - Provide a better error message if a domain user is specified using a User Principal Name (``UPN``) but the ``pykerberos`` library is not installed so Kerberos is unavailable.
- yaml loading - Fix traceback when parsing YAML strings (not files) when using the pure Python implementation of PyYAML.

amazon.aws
~~~~~~~~~~

- aws_ssm - Fixed connection being re-established on every loop iteration. The plugin now properly establishes a single connection for a loop (https://github.com/ansible-collections/amazon.aws/pull/2869).
- connection/aws_ssm - fixed ReferenceError in aws_ssm connection plugin destructor during interpreter shutdown (https://github.com/ansible-collections/amazon.aws/issues/2728).
- elb_application_lb - fixed comparison of multi-rule default actions to properly handle the ``Order`` field when determining if listener modifications are needed (https://github.com/ansible-collections/amazon.aws/issues/2537).
- elb_application_lb - fixed error where creating a new application load balancer with listener rules would fail with ``Parameter validation failed: Invalid type for parameter ListenerArn, value: None`` (https://github.com/ansible-collections/amazon.aws/issues/2400).
- lambda_info - fixed invalid return value documentation that used dot notation (``function.TheName``) which cannot be used in Jinja2 templates (https://github.com/ansible-collections/amazon.aws/pull/2772).
- s3_bucket - fix error when configuring AES256 bucket encryption with ``bucket_key_enabled`` explicitly set to ``false`` (https://github.com/ansible-collections/amazon.aws/issues/2734).
- s3_object - fixed error when using PUT with an empty ``content`` string (https://github.com/ansible-collections/amazon.aws/pull/2810)

ansible.netcommon
~~~~~~~~~~~~~~~~~

- Added support for private key passphrase in libssh connection plugin, when using encrypted private keys specified by the C(ansible_private_key_file) attribute.
- Adds backward compatibility of handling src attributes, functional consistency with ansible-core >= 2.19
- Adds deprecation warning for the jinja2 processing functionality for src attributes, src attributes in collections would still support considering file path but they would not process template files directly once the functionality is deprecated.
- Avoid legacy imports deprecated in ansible-core 2.20 (https://github.com/ansible-collections/ansible.netcommon/pull/720).
- Avoid merging module_defaults for all ansible.netcommon.grpc_* modules.
- It is suggested to use ansible.builtin.template module to process templates and use the processed template path in src attributes.
- Set libssh logging level to DEBUG when Ansible verbosity is greater than 3, to aid in troubleshooting connection issues.

ansible.utils
~~~~~~~~~~~~~

- Add a cleanup step that removes empty {} and [] values from lists in keep_keys_from_dict_n_list()

ansible.windows
~~~~~~~~~~~~~~~

- Stop using the deprecated text module_utils in Ansible that will be removed in Ansible ``2.24``.
- Update various action plugin calls to avoid some deprecated or old methods.
- win_dhcp_lease - when creating a reservation, the dns_name will be used as reservation_name in case that is not provided; will be discarded otherwise as the parameter HostName is not supported by Add-DhcpServerv4Reservation (https://github.com/ansible-collections/ansible.windows/issues/813)
- win_file - Fix idempotency issues when using ``state: touch`` (https://github.com/ansible-collections/ansible.windows/issues/798)
- win_get_url - Fix force=no not doing HEAD request if checksum is not set
- win_hotfix - Fix a bug in Get-HotfixMetadataFromKB fallback logic where it would fail to return metadata even if the hotfix was found.
- win_hotfix - Fix idempotency issue where some multi-package MSUs (e.g. SSU + CU) were incorrectly reported as installed by DISM even if the CU was missing. Added a secondary check using Get-Hotfix to verify installation.
- win_powershell - Fix up async support for Ansible 2.19 when running ``win_powershell`` - https://github.com/ansible-collections/ansible.windows/issues/828
- win_products_facts - return string for all the license related facts (https://github.com/ansible-collections/community.windows/issues/661).
- win_reboot - Use full path to ``shutdown.exe`` to avoid relying on ``PATH`` lookups to find - https://github.com/ansible-collections/ansible.windows/issues/826
- win_reboot - fix unhandled error when ``.exe`` not present in ``PATHEXT`` environment variable
- win_shell - Ensure the default ``executable`` uses the absolute path to ``powershell.exe`` rather than looking it up in the ``PATH`` environment.

arista.eos
~~~~~~~~~~

- Fix eos_vrf module to properly check existing interface configuration before making changes (https://github.com/ansible-collections/arista.eos/issues/546)

cisco.aci
~~~~~~~~~

- Fix allowed ranges of interface option in aci_interface_config module.
- Fix descriptions of options in aci_maintenance_policy.
- Fix querying description in aci_l4l7_service_graph_template.

cisco.ios
~~~~~~~~~

- Fixed delete and purged state function for ios_bfd_templates
- cisco.ios.ios_acls - Added support for converting numeric protocol values to real protocol options when gathered from the device.
- cisco.ios.ios_acls - Gathered state showing incomplete configuration.
- cisco.ios.ios_hsrp_intefaces - Considers version 1 as default if configuration does not specify version.
- cisco.ios.ios_hsrp_intefaces - Corrects idempotency issue when version is not specified in configuration.
- cisco.ios.ios_l2_interfaces - Moved mode parser to below the trunk parsers.

cisco.iosxr
~~~~~~~~~~~

- iosxr_bgp_address_family - Fixed label generation command handling under `address_family` configuration.

cisco.meraki
~~~~~~~~~~~~

- Fix parameter naming in organizations_inventory_claim.py to use camelCase for consistency with existing code.
- Fixing problem of naming in organizations_appliance_vpn_third_party_vpnpeers_info.
- Restructuring README.md file.
- administered_licensing_subscription_subscriptions_bind - Fixed parameter naming from 'subscription_id' to 'subscriptionId' for proper API compatibility
- meraki.py plugin utils - Added type checking in has_diff_elem2 function to prevent errors when comparing lists of non-dictionary elements
- networks_appliance_content_filtering - Enhanced idempotency by extracting category IDs from blockedUrlCategories before comparison

cisco.mso
~~~~~~~~~

- Fix updates of multicast_route_map_policy in mso_schema_template_vrf_rp.
- Fix updates of multicast_route_map_source_filter and multicast_route_map_destination_filter in mso_schema_template_bd.

cisco.nxos
~~~~~~~~~~

- Fixed nxos_facts module so it can handle VLAN interface facts without any issue even if addr is not defined
- Fixed nxos_static_routes module so to handle replaced and overridden state with vrf configuration.
- cisco.nxos.nxos_facts - Fix AttributeError when interface has multiple IPv6 addrs and handle ROW_addr as list.
- cisco.nxos.nxos_facts - Fix handling of facts for httapi type connection.
- cisco.nxos.nxos_hsrp_intefaces - Considers version 1 as default if configuration does not specify version.
- cisco.nxos.nxos_hsrp_intefaces - Corrects idempotency issue when version is not specified in configuration.
- cisco.nxos.nxos_hsrp_interfaces - Fix parsers for preempt and priority
- cisco.nxos.nxos_l2_interfaces - Fix cdp_enable config parsing.
- cisco.nxos.nxos_l3_interfaces - Improved the code logic for handling redirects.
- cisco.nxos.nxos_snmp_server - fixed communities parsing issue
- cisco.nxos.nxos_static_routes - Fix facts parser to filter inline VRF routes from global route collection preventing incorrect VRF route deletion.

community.aws
~~~~~~~~~~~~~

- Remove ``ansible.module_utils.six`` imports to avoid warnings (https://github.com/ansible-collections/community.aws/pull/2338).
- ec2_customer_gateway - Fix documentation for the return block (https://github.com/ansible-collections/community.aws/pull/2354).

community.crypto
~~~~~~~~~~~~~~~~

- crypto_info, openssl_privatekey, openssl_privatekey_pipe - fix detection of EC support for cryptography 46.0.5+ (https://github.com/ansible-collections/community.crypto/pull/981).

community.dns
~~~~~~~~~~~~~

- Update Public Suffix List.
- converter module utils - add ``stacklevel=2`` to Python warnings. This affects third-party users of the module utils outside this collection (https://github.com/ansible-collections/community.dns/pull/310).
- hetzner_* modules and hetzner_dns_records inventory plugin - retry on network problems and certain HTTP codes (502, 503, 504) (https://github.com/ansible-collections/community.dns/pull/313).
- hetzner_dns_record_set, hosttech_dns_record_set - fix ``on_existing != 'replace'`` mis-triggering when ``state=absent`` and the values to delete do not show up in the list of records (https://github.com/ansible-collections/community.dns/pull/301).
- hetzner_dns_record_sets - when doing batch updates, do not request status updates for too many actions at once (https://github.com/ansible-collections/community.dns/issues/312, https://github.com/ansible-collections/community.dns/pull/313).
- hosttech_* modules and hosttech_dns_records inventory plugin - when using the JSON API, retry on network problems and certain HTTP codes (502, 503, 504) (https://github.com/ansible-collections/community.dns/pull/313).
- hosttech_record_sets, hetzner_record_sets - ensure stable order also with Python < 3.6 (https://github.com/ansible-collections/community.dns/pull/301).
- lookup_rfc8427 lookup plugin - remove unused code (https://github.com/ansible-collections/community.dns/pull/308).
- remove_public_suffix filter plugin - fix plugin name in error message (https://github.com/ansible-collections/community.dns/pull/308).
- remove_registrable_domain filter plugin - fix plugin name in error message (https://github.com/ansible-collections/community.dns/pull/308).

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
- docker_image_pull, docker_container - fix pulled image change detection for Docker 29.2+ (https://github.com/ansible-collections/community.docker/pull/1242).
- docker_network - fix idempotency for IPv6 addresses and networks with Docker 29.0.0 (https://github.com/ansible-collections/community.docker/pull/1201).
- modules and plugins using the Docker SDK for Python - do not automatically set ``tls_hostname`` when ``validate_certs=true`` for Docker SDK for Python 7.0.0+ (https://github.com/ansible-collections/community.docker/issues/1225, https://github.com/ansible-collections/community.docker/pull/1226).

community.general
~~~~~~~~~~~~~~~~~

- _filelock module utils - add type hints. Fix bug if ``set_lock()`` is called with ``lock_timeout=None`` (https://github.com/ansible-collections/community.general/pull/11222).
- aix_filesystem - remove compatibility code for ancient Python versions (https://github.com/ansible-collections/community.general/pull/11232).
- ansible_type plugin utils - avoid potential concatenation of non-strings when ``alias`` has non-string values (https://github.com/ansible-collections/community.general/pull/11167).
- ansible_type test plugin - fix parameter checking (https://github.com/ansible-collections/community.general/pull/11167).
- apk - fix ``packages`` return value for apk-tools >= 3 (Alpine 3.23) (https://github.com/ansible-collections/community.general/issues/11264).
- cloudflare_dns - also allow ``flag=128`` for CAA records (https://github.com/ansible-collections/community.general/issues/11355, https://github.com/ansible-collections/community.general/pull/11377).
- cobbler_system - compare the version as a float which is the type returned by the Cobbler API (https://github.com/ansible-collections/community.general/issues/11044).
- counter_enabled callback plugin - fix plugin not observing ``display_ok_hosts`` option (https://github.com/ansible-collections/community.general/issues/3978, https://github.com/ansible-collections/community.general/pull/11656).
- datetime module utils - fix bug in ``fromtimestamp()`` that caused the function to crash. This function is not used in community.general (https://github.com/ansible-collections/community.general/pull/11206).
- gem - add compatibility with Ruby 4 rubygems (https://github.com/ansible-collections/community.general/issues/11397, https://github.com/ansible-collections/community.general/pull/11442).
- gitlab module utils - add type hints. Pass API version to python-gitlab as string and not as integer (https://github.com/ansible-collections/community.general/pull/11222).
- homebrew_service - slightly refactor code (https://github.com/ansible-collections/community.general/pull/11168).
- incus connection plugin - fix parsing of commands for Windows, enforcing a ``\`` after the drive letter and colon symbol (https://github.com/ansible-collections/community.general/pull/11347).
- ipa_dnsrecord - fix idempotency bug when using ``dnsttl`` due to wrong Python types (https://github.com/ansible-collections/community.general/pull/11559).
- ipinfoio_facts - fix handling of HTTP errors consulting the service (https://github.com/ansible-collections/community.general/pull/11145).
- iptables_state - refactor code to avoid writing unnecessary temporary files (https://github.com/ansible-collections/community.general/pull/11258).
- keycloak module utils - fix ``TypeError`` crash when managing users whose username or email contains special characters such as ``+`` (https://github.com/ansible-collections/community.general/issues/10305, https://github.com/ansible-collections/community.general/pull/11472).
- keycloak module utils - use proper URL encoding (``urllib.parse.quote``) for query parameters in authorization permission name searches, replacing fragile manual space replacement (https://github.com/ansible-collections/community.general/pull/11472).
- keycloak_authentication - fix ``TypeError`` crash when a flow is defined without ``authenticationExecutions`` (https://github.com/ansible-collections/community.general/issues/11547, https://github.com/ansible-collections/community.general/pull/11548).
- keycloak_client - fix idempotency bug caused by ``null`` client attribute value differences for non-existing client attributes (https://github.com/ansible-collections/community.general/issues/11443, https://github.com/ansible-collections/community.general/pull/11444).
- keycloak_client - fix idempotency bug caused by ``null`` flow overrides value differences for non-existing flow overrides (https://github.com/ansible-collections/community.general/issues/11430, https://github.com/ansible-collections/community.general/pull/11455).
- keycloak_client - remove IDs as change from diff result for protocol mappers (https://github.com/ansible-collections/community.general/issues/11453, https://github.com/ansible-collections/community.general/pull/11454).
- keycloak_realm - fixed crash in ``sanitize_cr()`` when ``realmrep`` was ``None`` (https://github.com/ansible-collections/community.general/pull/11260).
- keycloak_realm_key - fix ``KeyError`` crash when managing realm keys where Keycloak does not return ``active``, ``enabled``, or ``algorithm`` fields in the config response (https://github.com/ansible-collections/community.general/issues/11459, https://github.com/ansible-collections/community.general/pull/11470).
- keycloak_user_federation - mapper config item can be an array (https://github.com/ansible-collections/community.general/issues/11502, https://github.com/ansible-collections/community.general/pull/11515).
- keycloak_user_rolemapping - fix ``TypeError`` crash when adding a client role to a user who has no existing roles for that client (https://github.com/ansible-collections/community.general/issues/10960, https://github.com/ansible-collections/community.general/pull/11471).
- keycloak_user_rolemapping module - fixed crash when assigning roles to users without an existing role (https://github.com/ansible-collections/community.general/issues/10960, https://github.com/ansible-collections/community.general/pull/11256).
- keys_filter.py plugin utils - fixed requirements check so that other sequences than lists and strings are checked, and corrected broken formatting during error reporting (https://github.com/ansible-collections/community.general/pull/11167).
- listen_ports_facts - fix handling of empty PID lists when ``command=ss`` (https://github.com/ansible-collections/community.general/pull/11332).
- logstash_plugin - fix argument order when using ``version`` parameter. The plugin name must come after options like ``--version`` for the ``logstash-plugin`` CLI to work correctly (https://github.com/ansible-collections/community.general/issues/10745, https://github.com/ansible-collections/community.general/pull/11440).
- mas - parse CLI output correctly when listing installed apps with mas 3.0.0+ (https://github.com/ansible-collections/community.general/pull/11179).
- maven_artifact - fix SNAPSHOT version resolution to pick the newest matching ``<snapshotVersion>`` entry by ``<updated>`` timestamp instead of the first. Repositories like GitHub Packages keep all historical entries in ``<snapshotVersions>`` (oldest first), causing the module to resolve to the oldest snapshot instead of the latest (https://github.com/ansible-collections/community.general/issues/5117, https://github.com/ansible-collections/community.general/issues/11489, https://github.com/ansible-collections/community.general/pull/11501).
- monit - add delay of 0.5 seconds after state change and check for status (https://github.com/ansible-collections/community.general/pull/11255).
- monit - internal state was not reflecting when operation is "pending" in ``monit`` (https://github.com/ansible-collections/community.general/pull/11245).
- nictagadm - add a condition to the if statement so that ``is_valid_mac()`` does not get called if ``etherstub`` is false (https://github.com/ansible-collections/community.general/pull/11589).
- nmcli - add missing ``ipv6.routing-rules`` to ``settings_type()`` list type, preventing ``routing_rules6`` list from being corrupted (https://github.com/ansible-collections/community.general/issues/11630, https://github.com/ansible-collections/community.general/pull/11635).
- nsupdate - fix ``AttributeError`` when using the module without TSIG authentication (https://github.com/ansible-collections/community.general/issues/11460, https://github.com/ansible-collections/community.general/pull/11461).
- open_iscsi - fix IPv6 portal address formatting; iscsiadm requires bracket notation for IPv6 addresses but the module was producing an incorrect format (https://github.com/ansible-collections/community.general/issues/4467, https://github.com/ansible-collections/community.general/pull/11657).
- pam_limits - remove ``%`` templating no longer used in f-string (https://github.com/ansible-collections/community.general/pull/11229).
- pmem - fix test for invalid data input (https://github.com/ansible-collections/community.general/pull/11388).
- python_requirements_info - use ``importlib.metadata`` if ``pkg_resources`` from ``setuptools`` cannot be imported. That module has been removed from setuptools 82.0.0 (https://github.com/ansible-collections/community.general/issues/11491, https://github.com/ansible-collections/community.general/pull/11492).
- splunk callback plugin - replace deprecated callback function (https://github.com/ansible-collections/community.general/pull/11485).
- xcc_redfish_command - fix templating of dictionary keys as list (https://github.com/ansible-collections/community.general/pull/11144).
- xfconf - representation of boolean properties was not consistent between Python and ``xfconf-query``, leading to broken idempotency (https://github.com/ansible-collections/community.general/pull/11645).
- zfs - mark change correctly when updating properties whose current value differs, even if they already have a non-default value (https://github.com/ansible-collections/community.general/issues/11019, https://github.com/ansible-collections/community.general/pull/11172).

community.hrobot
~~~~~~~~~~~~~~~~

- Remove unnecessary Python 2 compatibilty code (https://github.com/ansible-collections/community.hrobot/pull/187).

community.libvirt
~~~~~~~~~~~~~~~~~

- libvirt_qemu - Vendor ``_parse_clixml`` locally to fix ``ImportError`` on ansible-core devel (2.21+).
- virt_install - fixed cloud_init configuration handling for meta-data, user-data, and network-config.
- virt_install - fixed the dict-based options handling for events, resource, and sysinfo options.

community.mysql
~~~~~~~~~~~~~~~

- mysql_user - When creating a new user, and specifying parsec as plugin it wil generate the wrong SQL query. It should be added to the same plugin check as ed25519 so that it generates a query using USING PASSWORDS(%s) instead of BY %s (https://github.com/ansible-collections/community.mysql/pull/779).

community.postgresql
~~~~~~~~~~~~~~~~~~~~

- postgresql_db - Fix connection limit not being set when value is "0" (https://github.com/ansible-collections/community.postgresql/issues/879).
- postgresql_db - fixed ``session_role`` parameter that was being ignored for raw connections (https://github.com/ansible-collections/community.postgresql/pull/865)
- postgresql_db - restoring from ``.sql`` files would execute the file twice. The module now avoids using both ``--file`` and stdin redirection simultaneously (https://github.com/ansible-collections/community.postgresql/issues/882).

community.proxmox
~~~~~~~~~~~~~~~~~

- proxmox all - add missing timeout parameter to proxmoxer object creation (https://github.com/ansible-collections/community.proxmox/pull/218).
- proxmox_cluster - make cluster join idempotent (https://github.com/ansible-collections/community.proxmox/pull/244).
- proxmox_cluster_firewall - error message for invalid log_ratelimit.rate parameter (https://github.com/ansible-collections/community.proxmox/pull/340).
- proxmox_disk - add support for efidisk and tpmstate disk bus types which previously caused module failure with "Unsupported disk bus" error (https://github.com/ansible-collections/community.proxmox/pull/319).
- proxmox_disk - make none iso disk idempotent (https://github.com/ansible-collections/community.proxmox/pull/288).
- proxmox_firewall - Enable ipsets on vm level and fix bugs regarding the cidr notation the proxmox api expects (https://github.com/ansible-collections/community.proxmox/pull/248).
- proxmox_ipam_info - fix bug where selecting by vmid did not work (https://github.com/ansible-collections/community.proxmox/pull/211).
- proxmox_pool - support nested pool (https://github.com/ansible-collections/community.proxmox/pull/316).
- proxmox_role - when privs is omitted, keep existing role privileges unchanged instead of treating it as no privileges (https://github.com/ansible-collections/community.proxmox/pull/284).
- proxmox_snap - fail the task when a given snapname does not exist instead of exiting (https://github.com/ansible-collections/community.proxmox/pull/365).
- proxmox_storage - backend ``cephfs``, ``dir`` and ``zfspool`` doesn't requires ``content`` parameter (https://github.com/ansible-collections/community.proxmox/pull/315).
- proxmox_storage - the parameter ``client_keyring`` was ignored (https://github.com/ansible-collections/community.proxmox/pull/305).
- proxmox_storage - the parameter ``fs_name`` was ignored (https://github.com/ansible-collections/community.proxmox/pull/305).
- proxmox_storage - the parameter ``state`` was optional and without default value (https://github.com/ansible-collections/community.proxmox/pull/305).
- proxmox_zone - fix validation logic for VXLAN zones to accept either ``fabric`` or ``peers`` parameter. Previously, only ``fabric`` was accepted, but Proxmox VE also supports creating VXLAN zones with a peer address list (https://github.com/ansible-collections/community.proxmox/issues/216).
- remove wrong api endpoints and error messages from proxmod_node certificate management(https://github.com/ansible-collections/community.proxmox/pull/232).

community.routeros
~~~~~~~~~~~~~~~~~~

- api_info, api_modify - removed support for several parameters (``shared-buffers-color``, ``shared-pool0``-``shared-pool7``, ``treat-yellow-as``, ``wred-shared-threshold``, ``wred-threshold``) in the ``interface ethernet switch qos settings`` path for RouterOS <7.16 (https://github.com/ansible-collections/community.routeros/pull/450).
- api_info, api_modify - removed support for the parameter ``color`` in the ``interface ethernet switch qos profile`` path for RouterOS <7.16 (https://github.com/ansible-collections/community.routeros/pull/450).
- api_info, api_modify - removed support for the parameter ``ecn`` in the ``interface ethernet switch qos tx-manager`` path for RouterOS <7.16 (https://github.com/ansible-collections/community.routeros/pull/450).
- api_info, api_modify - removed support for the parameter ``enabled`` in the ``interface ovpn-server server`` path for RouterOS >=7.17 (https://github.com/ansible-collections/community.routeros/pull/450).
- api_info, api_modify - removed support for the parameter ``envlist`` (replaced by ``envlists``) in the ``container`` path for RouterOS <7.20 (https://github.com/ansible-collections/community.routeros/pull/450).
- api_info, api_modify - removed support for the parameter ``fasttrack-hw`` in the ``interface ethernet switch l3hw-settings`` path for RouterOS <7.16 (https://github.com/ansible-collections/community.routeros/pull/450).
- api_info, api_modify - removed support for the parameter ``import.router-id`` in the ``routing bgp vpn`` path for RouterOS <7.20 (https://github.com/ansible-collections/community.routeros/pull/450).
- api_info, api_modify - removed support for the parameter ``min-echo-rx`` in the ``routing bfd configuration`` path for RouterOS <7.15 (https://github.com/ansible-collections/community.routeros/pull/450).
- api_info, api_modify - removed support for the parameter ``mounts`` (replaced by ``mount``) in the ``container`` path for RouterOS <7.21 (https://github.com/ansible-collections/community.routeros/pull/450).
- api_info, api_modify - removed support for the parameter ``name`` in the ``container envs`` path for RouterOS <7.20 (https://github.com/ansible-collections/community.routeros/pull/450).
- api_info, api_modify - removed support for the parameter ``name`` in the ``container mounts`` path for RouterOS <7.21 (https://github.com/ansible-collections/community.routeros/pull/450).
- api_info, api_modify - removed support for the parameter ``nvme-tcp-name`` in the ``disk`` path for RouterOS <7.21 (https://github.com/ansible-collections/community.routeros/pull/450).
- api_info, api_modify - removed support for the parameter ``partial-offload-chunk`` in the ``interface ethernet switch l3hw-settings advanced`` path for RouterOS <7.18 (https://github.com/ansible-collections/community.routeros/pull/450).
- api_info, api_modify - removed support for the parameter ``pfc`` in the ``interface ethernet switch qos port`` path for RouterOS <7.16 (https://github.com/ansible-collections/community.routeros/pull/450).
- api_info, api_modify - removed support for the parameter ``port`` in the ``interface vxlan vteps`` path for RouterOS <7.18 (https://github.com/ansible-collections/community.routeros/pull/450).
- api_info, api_modify - removed support for the parameter ``ports`` in the ``interface bridge mdb`` path for RouterOS <7.19 (https://github.com/ansible-collections/community.routeros/pull/450).
- api_info, api_modify - removed support for the parameter ``ram-high`` in the ``container config`` path for RouterOS <7.20 (https://github.com/ansible-collections/community.routeros/pull/450).
- api_info, api_modify - removed support for the parameter ``remote-addrs`` (replaced by ``remote-address``) and ``status`` in the ``file sync`` path for RouterOS <7.16 (https://github.com/ansible-collections/community.routeros/pull/450).
- api_info, api_modify - removed support for the parameter ``src-address`` in the ``iot lora`` and ``lora`` paths for RouterOS <7.19 (https://github.com/ansible-collections/community.routeros/pull/450).
- api_info, api_modify - removed support for the parameter ``start-tls`` (default ``False``) in the ``tool e-mail`` path for RouterOS <7.15 (https://github.com/ansible-collections/community.routeros/pull/450).
- api_info, api_modify - removed support for the parameter ``vrf`` in the ``interface vxlan`` path for RouterOS <7.20 (https://github.com/ansible-collections/community.routeros/pull/450).
- api_info, api_modify - removed support for the parameters ``rssi-off`` and ``tx-enabled`` in the ``iot lora radios`` and ``lora radios`` paths for RouterOS <7.17 (https://github.com/ansible-collections/community.routeros/pull/450).
- api_info, api_modify - removed support for the parameters ``shared-pool-index`` and ``wred`` in the ``interface ethernet switch qos tx-manager queue`` path for RouterOS <7.16 (https://github.com/ansible-collections/community.routeros/pull/450).
- api_modify - fix idempotency for ``container mounts`` path on RouterOS 7.22+ where for ``dst`` and ``src``, values without a leading ``/`` (e.g. ``TEST``) were not recognised as matching the normalised value returned by RouterOS (``/TEST``), causing spurious updates on every run (https://github.com/ansible-collections/community.routeros/issues/449, https://github.com/ansible-collections/community.routeros/pull/452).
- api_modify, api_info - in the ``routing bgp connection`` and ``bgp templates`` paths, fix spelling of the ``output.remove-private-as`` parameter (https://github.com/ansible-collections/community.routeros/issues/415, https://github.com/ansible-collections/community.routeros/pull/416).
- api_modify, api_info - in the ``routing bgp instance`` path, fix 'Cannot add new entry to this path' error (https://github.com/ansible-collections/community.routeros/issues/409, https://github.com/ansible-collections/community.routeros/pull/420).
- api_modify, api_info - in the ``routing bgp templates`` path, remove ``address-families`` for RouterOS 7.19+ (https://github.com/ansible-collections/community.routeros/issues/415, https://github.com/ansible-collections/community.routeros/pull/416).
- api_modify, api_info - in the ``routing bgp templates`` path, remove ``router-id`` for RouterOS 7.20+ (https://github.com/ansible-collections/community.routeros/issues/415, https://github.com/ansible-collections/community.routeros/pull/416).
- api_modify, api_info - in the ``routing bgp templates`` path, support ``afi`` (RouterOS 7.19+) (RouterOS 7.19 and before) (https://github.com/ansible-collections/community.routeros/issues/415, https://github.com/ansible-collections/community.routeros/pull/416).

community.vmware
~~~~~~~~~~~~~~~~

- vmware_guest_storage_policy - Fix storage policy search to return None if no policies are found, instead of causing an exception. fixes https://github.com/ansible-collections/community.vmware/issues/2527

community.windows
~~~~~~~~~~~~~~~~~

- Unify the TLS protocol handling logic for the modules that need it to ensure they use the configured OS policies.
- win_disk_facts - fixed an issue when a disk may not have a number (https://github.com/ansible-collections/community.windows/pull/652).
- win_initialize_disk - disks that are formatted but offline cannot be brought online without erasing them (https://github.com/ansible-collections/community.windows/issues/149).
- win_psmodule - Improve error message, if a module exists in multiple repositories - https://github.com/ansible-collections/community.windows/issues/641
- win_psrepository_copy - Fix idempotence check to not rely on .NET runtime implementation details. This should avoid any false positive changed indicators

containers.podman
~~~~~~~~~~~~~~~~~

- Fix Ansible warning about test utils
- Fix idempotency for tagging local images
- Fix image idempotency in pull
- Fix issue with --rm and service in Quadlet
- fix(podman_prune) set top-level changed status

dellemc.enterprise_sonic
~~~~~~~~~~~~~~~~~~~~~~~~

- ansible-core_219_compatibility - Modify the required Netcommon version and UT module param setting method for ansible-core 2.19 compatibility (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/600).
- sonic_bgp_af - Fix check mode behavior (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/613).
- sonic_lag_interfaces - Fix graceful_shutdown not disabled for existing lag interfaces (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/617).
- sonic_qos_buffer - Fix check mode and refactor module code (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/602).
- sonic_qos_interfaces - Fix check mode and refactor module code (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/603).
- sonic_qos_maps - Fix check mode and refactor module code (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/602).
- sonic_qos_scheduler - Fix check mode and refactor module code (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/602).
- sonic_qos_wred - Fix check mode and refactor module code (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/602).
- sonic_roce - Fix check mode and refactor module code (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/602).
- sonic_vxlans - Fix VXLAN config/facts handling; moving deprecated uri EVPN_NVO to current one VXLAN_EVPN_NVO (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/598).
- sonic_vxlans - Fix check mode handling (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/611).

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- idrac_job_queue - (Issue 1067) - Fails to find the file in role due to incorrect name (https://github.com/dell/dellemc-openmanage-ansible-modules/issues/1067)
- idrac_system_info - (Issue 1044) - FC section is missing (https://github.com/dell/dellemc-openmanage-ansible-modules/issues/1044)
- idrac_system_info - powersupply.get_red_type_set fails with TypeError due to unhandled None values when joining mapped redundancy types
- idrac_user - (Issue 1059) - Bad User Privileges when creating idrac user using "custom_privilege" (https://github.com/dell/dellemc-openmanage-ansible-modules/issues/1059)

fortinet.fortimanager
~~~~~~~~~~~~~~~~~~~~~

- Improved the request sending logic in httpapi plugin.

fortinet.fortios
~~~~~~~~~~~~~~~~

- Fixed an issue where users were required to specify a password confirmation when using the system_admin and system_api_user modules in FortiOS 7.6.5 and later.
- Fixed the issue that getting an error "BadGzipFile" when using token for authentication in new versions of FortiOS.

google.cloud
~~~~~~~~~~~~

- Fix runtime.yml to correctly note Ansible 2.17 minimum version (https://github.com/ansible-collections/google.cloud/pull/730)
- Revert removal of Ansible 2.16 support (https://github.com/ansible-collections/google.cloud/pull/734)
- connection plugin - fix attribute error when using reset_connection (https://github.com/ansible-collections/google.cloud/issues/737).
- connection plugin - fix ssh error in tasks with loops (https://github.com/ansible-collections/google.cloud/issues/738).
- gcp_secret_manager - return the secret value as type `str` rather than `bytes` (https://github.com/ansible-collections/google.cloud/pull/721)

hetzner.hcloud
~~~~~~~~~~~~~~

- Invalid redirects for Storage Box modules are now fixed by using fully qualified module names.
- firewall - Ensure idempotency when using non canonical ipv6 representation in Firewall rules.
- zone_rrset - Records order is not guaranteed, the module will not generate a diff if the order of records changes.
- zone_rrset - Records without comments will not generate a diff anymore.

hitachivantara.vspone_block
~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Resolved issue during GAD pair creation when resource lock is enabled.
- Resolved issue with quorum disk creation on VSP One Block 85 storage systems.
- Resolved issue with remote connection creation on VSP One Block 85 storage systems.
- Resolved issue with storage system facts retrieval module for VSP One Block 85 storage systems.
- Resolved resource group creation with VSP 5XXX series storage systems.
- Various additional bug fixes and enhancements for VSP One Block 85 storage systems.
- Various additional bug fixes and enhancements for VSP One storage systems and VSP One SDS Block storage systems.
- Various playbook fixes and improvements.

ibm.storage_virtualize
~~~~~~~~~~~~~~~~~~~~~~

- ibm_svc_manage_ip - Fixed issue related to VLAN while updating

infoblox.nios_modules
~~~~~~~~~~~~~~~~~~~~~

- Fixed sanity and unit test execution in CI pipeline
- Fixed transform functions to handle ``None`` parameters and apply default values correctly

inspur.ispim
~~~~~~~~~~~~

- Edit ansible devel version tests to our CI test scripts  (https://github.com/ispim/inspur.ispim/pull/39).
- Modify the automated tests and add support for version 2.18. (https://github.com/ispim/inspur.ispim/pull/40).
- Modify the automated tests and add support for version 2.18. (https://github.com/ispim/inspur.ispim/pull/45).
- Modify the ism.py file in the module_utils directory, and change the reference path of iteritems to be a reference from within Python. (https://github.com/ispim/inspur.ispim/pull/46).

kaytus.ksmanage
~~~~~~~~~~~~~~~

- Modify the automated tests and add support for version 2.18. (https://github.com/ieisystem/kaytus.ksmanage/pull/31).
- Modify the failure details returned in module_utils (https://github.com/ieisystem/kaytus.ksmanage/pull/29).
- Modify the ksmanage.py file in the module_utils directory, and change the reference path of iteritems to be a reference from within Python. (https://github.com/ieisystem/kaytus.ksmanage/pull/32).

kubernetes.core
~~~~~~~~~~~~~~~

- Add idempotency for ``helm_pull`` module (https://github.com/ansible-collections/kubernetes.core/pull/1055).
- Fixed a bug where setting ``K8S_AUTH_VERIFY_SSL=true`` (or any string value) caused the value to be treated as a separate ``kubectl`` command argument. (https://github.com/ansible-collections/kubernetes.core/pull/1049).
- Limit supported versions of Helm to <4.0.0 (https://github.com/ansible-collections/kubernetes.core/pull/1039).
- Replace passing ``warnings`` to ``exit_json`` with ``AnsibleModule.warn`` in the ``k8s_drain``, ``k8s_rollback.py`` and ``k8s_scale.py`` modules as it deprecated in ``ansible-core>=2.19.0`` and will be removed in ``ansible-core>=2.23.0`` (https://github.com/ansible-collections/kubernetes.core/pull/1033).
- k8s - Fix return block from the module documentation (https://github.com/ansible-collections/kubernetes.core/pull/1056).
- meta - Add ``k8s_cluster_info``, ``k8s_json_patch`` and ``k8s_rollback`` to k8s action group (https://github.com/ansible-collections/kubernetes.core/pull/992).

microsoft.ad
~~~~~~~~~~~~

- microsoft.ad.domain_child - Fix return document key so it displays when using the standard Ansible documentation tools.
- microsoft.ad.ldap - Fix issue where auth_protocol config option was never used when creating the spnego client.
- microsoft.ad.service_account - Fix return document key so it displays when using the standard Ansible documentation tools.

microsoft.iis
~~~~~~~~~~~~~

- website_info - Fix error when retrieving website information but none exist - https://github.com/ansible-collections/microsoft.iis/issues/44

netapp.ontap
~~~~~~~~~~~~

- na_ontap_aggregate - fixed issue with disabling software encryption in REST.
- na_ontap_cg_snapshot - fixed issue with ZAPI by removing default value for `consistency_type`.
- na_ontap_cifs_local_group - fixed issue with idempotency.
- na_ontap_export_policy_rule - Fixed issue where rule_index was not being applied to create body, and added logic to detect when a create action is actually a re-index of an existing rule.
- na_ontap_firmware_upgrade - Updated documentation for `node` parameter and added examples.
- na_ontap_job_schedule - Fix documentation formatting issue.
- na_ontap_lun - Updated module with alias `volume_name` for `flexvol_name`.
- na_ontap_net_vlan - Fixed state detection when VLAN exists but is not in broadcast domain.
- na_ontap_qtree - Updated documentation for 'unix_permissions' parameter to clarify its usage.
- na_ontap_qtree - Updated module with alias `volume_name` for `flexvol_name`.
- na_ontap_service_processor_network - fixed issue with interface state not being applied correctly, resolved ipv6 comparison issue and idempotency issue with ZAPI abd REST.
- na_ontap_snapmirror_policy - updated examples for creating and modifying snapmirror policy.
- na_ontap_user_role - Removed special handling of `DEFAULT` path and normalized empty query in privileges to None for consistency.
- na_ontap_volume - Fixed issue with volume rename.
- na_ontap_vserver_audit - updated documentation for `log`.

netapp.storagegrid
~~~~~~~~~~~~~~~~~~

- na_sg_grid_alert_receiver - correct example section in the module for better understanding.
- na_sg_grid_autosupport - add support to handle error response from the API.
- na_sg_grid_autosupport - fix issue with setting up `destinations` option in the module.
- na_sg_grid_domain_name - fixed issue where additional domain names was not detected as changed.
- na_sg_grid_group - fix issue where `activate_features` parameter was deprecated but still present in code.
- na_sg_grid_group - fix typo in parameter mapping for `alarm_acknowledgement` option.
- na_sg_grid_ha_group - correct documentation section in the module for better understanding.
- na_sg_grid_identity_federation - fix issue with check mode response.
- na_sg_grid_info - Fix issue where the module incorrectly reported tasks as changed.
- na_sg_grid_regions - correct documentation section in the module for better understanding.
- na_sg_org_identity_federation - fix issue with check mode response.
- na_sg_org_info - Fix issue where the module incorrectly reported tasks as changed.
- na_sg_org_user_s3_key - unique_user_name is fixed as in the documents

netbox.netbox
~~~~~~~~~~~~~

- Add netbox version check to support service creation for netbox version prior of 4.3
- Fix integration test for circuit termination, missing assignment
- Fix integration test for service
- Fix task duplicate task name in documentation that cause ansible-lint error
- Fix typos in tag integration tests.
- Support for related_object_filter when related_object_type is "object"
- Use dedicated function to check netbox version istead of self.full_version for rack.
- add parent_object_type and parent_object_id to services ALLOWED_QUERY_PARAMS
- nb_device_interface: Fix specifying primary_mac_address objects by id for disambiguation
- nb_inventory - Fix service collection for version greater than 4.3
- nb_inventory - Fixed empty inventory results when netbox server URL is a non-root path
- netbox_service - Fix issue 1426 - broken netbox_service module

ovirt.ovirt
~~~~~~~~~~~

- Fix missing cluster name when starting VM (https://github.com/oVirt/ovirt-ansible-collection/pull/780)

purestorage.flasharray
~~~~~~~~~~~~~~~~~~~~~~

- purefa_certs - Fix the syntax to generate a CSR
- purefa_connect - Fixed issue where incorrect transport type was passed.
- purefa_default_protection - Fixed issue adding new default protection group to the array scope
- purefa_dsrole_old - Fixed incorrect parameter name for old version of functions
- purefa_host - Fixed AttributeError when deleting WWNs from a host
- purefa_info - Added version check to ensure tags are only used in appropriate Purity versions
- purefa_info - Fixed AttributeError when directory service role has no name
- purefa_info - Fixed AttributeError when subnet has no VLAN
- purefa_info - Fixed error with Resalms-based API clients
- purefa_info - Fixed issue with shelf controllers not supporting uptime
- purefa_info - Resolved AttributeErrors in ``default`` info section
- purefa_info - Resolves issue with hosthgroup info when NVMe connected volumes are in a hostgroup
- purefa_network - Fixes issue caused by None meaning change in SDK
- purefa_pgsched - Fixed schedule deletion idempotency
- purefa_policy - Fixed AttributeError when modifying a password policy
- purefa_policy - Multiple syntax errors fixed in the password policy update section

purestorage.flashblade
~~~~~~~~~~~~~~~~~~~~~~

- purefb_ad - Ensure encryption algorithms used match the GUI values
- purefb_alert - Fixed issue with syntax error in update function
- purefb_bucket_replica - Fixed IndexError crash in check loop
- purefb_bucket_replica - Fixed issue with ItemIterator error
- purefb_certs - Fix the syntax to generate a CSR
- purefb_ds - Fixed issue when creating pre-enabled management directory service
- purefb_pingtrace - Fiexed issue with XFM module when state is ping

splunk.es
~~~~~~~~~

- Added sanity test ignore file for Ansible 2.20 to handle pylint errors in deprecated modules.
- Fixed ansible-lint errors by adding missing task names in integration tests.
- Fixed deprecated module alternatives to use fully qualified collection names (FQCN).
- Implement check mode support in action plugins. Previously, check mode was declared as supported but API calls were still being made. Now all state-changing operations (merged, replaced, deleted) properly skip API calls when running in check mode.
- splunk_correlation_searches - Fixed duplicate entries in gathered state caused by redundant loop in action plugin.

telekom_mms.icinga_director
~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Fix diff in check mode by normalising the boolean values (https://github.com/telekom-mms/ansible-collection-icinga-director/pull/295)
- Fix doc generation and remove need for iteritems (https://github.com/telekom-mms/ansible-collection-icinga-director/pull/296)
- Fix: remove default for states parameter in icinga_dependency_apply (https://github.com/telekom-mms/ansible-collection-icinga-director/pull/290)

theforeman.foreman
~~~~~~~~~~~~~~~~~~

- content_view_filter_rule - fix content_filter_rule_deb_spec to take into account desired versions

vmware.vmware
~~~~~~~~~~~~~

- Fix issue where modules that used the proxy_host and proxy_port arguments were ignoring these arguments when initializing clients. (https://github.com/ansible-collections/vmware.vmware/issues/259)
- Updated common VM deployment module docs to mention that name or MOID can be used for the resource pool, cluster, datastore, and datastore cluster parameters. This allows users to work around issues where the name is not unique. Fixes https://github.com/ansible-collections/vmware.vmware/issues/239
- cluster_info - When a user does not specify a cluster name, the module will now search recursively for clusters in the datacenter. Fixes https://github.com/ansible-collections/vmware.vmware/issues/303
- cluster_info - When a user specifies a datacenter name, the module will now fail if that datacenter is not found instead of silently continuing. Fixes https://github.com/ansible-collections/vmware.vmware/issues/303
- deploy_content_library_ovf - Remove invalid storage provisioning option 'eagerzeroedthick' from module's argument spec. (Fixes https://github.com/ansible-collections/vmware.vmware/issues/278)
- deploy_folder_template - Fixed issue where the vm folder was being cached in the placement service, causing the module to skip the template folder lookup and fail. Fixes https://github.com/ansible-collections/vmware.vmware/issues/292
- import_content_library_ovf - Fixed issue where OVFs with .nvram files failed to import Fixes https://github.com/ansible-collections/vmware.vmware/issues/257
- inventory plugins - fix handling of encrypted strings in inventory plugin username and password options for ansible-core<=2.19 fixes https://github.com/ansible-collections/vmware.vmware/issues/304
- vm - Fixed issue where error handling failed when state is absent
- vm - Remove check that prevents memory from being decreased regardless of power state. Fixes https://github.com/ansible-collections/vmware.vmware/issues/298
- vm_apply_customization - Fixed issue where the product ID, user name, and user org name were required by the API but not by the module

vultr.cloud
~~~~~~~~~~~

- dns_domain - Removed requirement for the ``ip`` argument when creating a new domain (https://github.com/vultr/ansible-collection-vultr/issues/140).
- instance, bare_metal - Fixed an issue where the ``user_data`` response returned a JSON serialization error (https://github.com/vultr/ansible-collection-vultr/issues/156).
- startup_script - Fixed an issue where the ``script`` response returned a JSON serialization error (https://github.com/vultr/ansible-collection-vultr/pull/162).

Known Issues
------------

community.docker
~~~~~~~~~~~~~~~~

- docker_image, docker_image_export - idempotency for archiving images depends on whether the image IDs used by the image storage backend correspond to the IDs used in the tarball's ``manifest.json`` files. The new default backend in Docker 29 apparently uses image IDs that no longer correspond, whence idempotency no longer works (https://github.com/ansible-collections/community.docker/pull/1199).

community.routeros
~~~~~~~~~~~~~~~~~~

- api_modify - to create or modify entries in the ``container`` path, you need librouteros 4.0.0 or newer due to a bug preventing older versions from setting or modifying properties named ``cmd`` (https://github.com/ansible-collections/community.routeros/issues/442).

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- Formal qualification of module ome_smart_fabric_info for Ansible Core version 2.19 is still pending.
- idrac_diagnostics - This module does not support export of diagnostics file to HTTP and HTTPS share via SOCKS proxy.
- idrac_license - Due to API limitation, proxy parameters are ignored during the import operation.
- idrac_license - The module will give different error messages for iDRAC9 and iDRAC10 when user imports license with invalid share name.
- idrac_os_deployment - The module continues to return a 200 response and marks the job as completed, even when an outdated date is supplied in the Expose duration.
- idrac_redfish_storage_controller - PatrolReadRatePercent attribute cannot be set in iDRAC10.
- idrac_server_config_profile - When attempting to revert iDRAC settings using a previously exported SCP file, the import operation will complete with errors if a new user was created after the export (Instead of restoring the system to its previous state, including the removal of newly added users).
- ome_smart_fabric_uplink - The module supported by OpenManage Enterprise Modular, however it does not allow the creation of multiple uplinks of the same name. If an uplink is created using the same name as an existing uplink, then the existing uplink is modified.
- redfish_storage_volume - Encryption type and block_io_size bytes will be read only property in iDRAC9 and iDRAC10 and hence the module ignores these parameters.

New Plugins
-----------

Callback
~~~~~~~~

- community.general.loganalytics_ingestion - Posts task results to an Azure Log Analytics workspace using the new Logs Ingestion API.

Filter
~~~~~~

- community.general.to_toml - Convert variable to TOML string.

New Modules
-----------

amazon.aws
~~~~~~~~~~

- amazon.aws.ec2_instance_type_info - Retrieve information about EC2 instance types

ansible.windows
~~~~~~~~~~~~~~~

- ansible.windows.dsc3 - Sets or checks DSC v3 configuration state

cisco.aci
~~~~~~~~~

- cisco.aci.aci_fabric_node_decommission - Manage the Commissioning and Decommissioning of the Fabric Node (fabric:RsDecommissionNode)
- cisco.aci.aci_management_network_instance_profile - Manage external management network instance profiles (mgmt:InstP).
- cisco.aci.aci_management_network_instance_profile_to_contract - Bind Consumed Contract to External Management Network Instance Profiles (mgmt:RsOoBCons)
- cisco.aci.aci_switch_access_config - Manage Switch Access Policy Configuration of Leaf and Spine nodes (infra:NodeConfig).
- cisco.aci.aci_switch_fabric_config - Manage Switch Fabric Policy Configuration of Leaf and Spine nodes (fabric:NodeConfig).

cisco.ios
~~~~~~~~~

- cisco.ios.ios_bfd_interfaces - Resource module to configure bfd in interfaces.
- cisco.ios.ios_bfd_templates - Bidirectional Forwarding Detection (BFD) templates configurations

cisco.mso
~~~~~~~~~

- cisco.mso.ndo_endpoint_ip_tag_policy - Manage Endpoint IP Tag Policies on Cisco Nexus Dashboard Orchestrator (NDO).
- cisco.mso.ndo_endpoint_mac_tag_policy - Manage Endpoint MAC Tag Policies on Cisco Nexus Dashboard Orchestrator (NDO).
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
- cisco.mso.ndo_template_deploy - Deploy templates to sites on Cisco Nexus Dashboard Orchestrator (NDO).
- cisco.mso.ndo_tenant_netflow_record - Manage NetFlow Record on Cisco Nexus Dashboard Orchestrator (NDO).

community.general
~~~~~~~~~~~~~~~~~

- community.general.file_remove - Remove files matching a pattern from a directory.
- community.general.github_secrets - Manage GitHub repository or organization secrets.
- community.general.github_secrets_info - List GitHub repository or organization secrets.
- community.general.icinga2_downtime - Manages Icinga 2 downtimes.
- community.general.ip2location_info - Retrieve IP geolocation information of a host's IP address.
- community.general.keycloak_authentication_v2 - Configure authentication flows in Keycloak in an idempotent and safe manner.
- community.general.keycloak_realm_localization - Allows management of Keycloak realm localization overrides via the Keycloak API.
- community.general.logrotate - Manage logrotate configurations.
- community.general.lxd_storage_pool_info - Retrieve information about LXD storage pools.
- community.general.lxd_storage_volume_info - Retrieve information about LXD storage volumes.
- community.general.sssd_info - Check SSSD domain status using D-Bus.

community.libvirt
~~~~~~~~~~~~~~~~~

- community.libvirt.virt_cloud_instance - Provision new virtual machines from cloud images via libvirt

community.proxmox
~~~~~~~~~~~~~~~~~

- community.proxmox.proxmox_ceph_mds - Add or delete Ceph Mds.
- community.proxmox.proxmox_ceph_mgr - Add or delete Ceph Manager.
- community.proxmox.proxmox_ceph_mon - Add or delete Ceph Monitor.
- community.proxmox.proxmox_cluster_firewall - Cluster-level firewall options management for Proxmox VE cluster.
- community.proxmox.proxmox_cluster_ha_rules_info - Retrieve Proxmox VE HA rules.
- community.proxmox.proxmox_domain - Manage authentication realms.
- community.proxmox.proxmox_domain_sync - Sync realms.
- community.proxmox.proxmox_role - Role management for Proxmox VE cluster.
- community.proxmox.proxmox_sendkey - Send key presses to a Proxmox VM console.

containers.podman
~~~~~~~~~~~~~~~~~

- containers.podman.podman_quadlet - Install or remove Podman Quadlets
- containers.podman.podman_quadlet_info - Gather information about Podman Quadlets

dellemc.enterprise_sonic
~~~~~~~~~~~~~~~~~~~~~~~~

- dellemc.enterprise_sonic.sonic_fbs_interfaces - Manage flow based services (FBS) interfaces configuration on SONiC.
- dellemc.enterprise_sonic.sonic_mfa - Manage Multi-factor authentication (MFA) configurations on SONiC.

fortinet.fortimanager
~~~~~~~~~~~~~~~~~~~~~

- fortinet.fortimanager.fmgr_devprof_log_syslogd_setting_logtemplates - System template log syslogd setting log templates
- fortinet.fortimanager.fmgr_devprof_system_template_interface - System template system template interface
- fortinet.fortimanager.fmgr_devprof_system_template_interface_iprange - System template system template interface ip range
- fortinet.fortimanager.fmgr_dynamic_log_npuserver_servergroup_dynamicmapping - Dynamic log npu server server group dynamic mapping
- fortinet.fortimanager.fmgr_firewall_pfcp - Configure PFCP.
- fortinet.fortimanager.fmgr_firewall_profileprotocoloptions_proxyredirect - Firewall profile protocol options proxy redirect
- fortinet.fortimanager.fmgr_firewall_profileprotocoloptions_rtmp - RTMP.
- fortinet.fortimanager.fmgr_firewall_proxyaddress6 - Firewall proxy address6
- fortinet.fortimanager.fmgr_firewall_proxyaddress6_headergroup - Firewall proxy address6 header group
- fortinet.fortimanager.fmgr_firewall_proxyaddress6_tagging - Firewall proxy address6 tagging
- fortinet.fortimanager.fmgr_firewall_proxyaddrgrp6 - Firewall proxy addrgrp6
- fortinet.fortimanager.fmgr_firewall_proxyaddrgrp6_tagging - Firewall proxy addrgrp6 tagging
- fortinet.fortimanager.fmgr_firewall_shapingprofile_classes - Firewall shaping profile classes
- fortinet.fortimanager.fmgr_firewall_sslsshprofile_sslclientcertificate - Firewall ssl ssh profile ssl client certificate
- fortinet.fortimanager.fmgr_fmg_script - Fmg script
- fortinet.fortimanager.fmgr_fmg_script_schedule - Fmg script schedule
- fortinet.fortimanager.fmgr_icap_remoteservergroup - Icap remote server group
- fortinet.fortimanager.fmgr_icap_remoteservergroup_serverlist - Icap remote server group server list
- fortinet.fortimanager.fmgr_isolator_profile - Isolator profile
- fortinet.fortimanager.fmgr_isolator_profile_entries - Isolator profile entries
- fortinet.fortimanager.fmgr_pkg_firewall_responseshapingpolicy - Policy package firewall response shaping policy
- fortinet.fortimanager.fmgr_securityconsole_template_validate - Securityconsole template validate
- fortinet.fortimanager.fmgr_switchcontroller_managedswitch_routerstatic - Configure static routes.
- fortinet.fortimanager.fmgr_switchcontroller_managedswitch_routervrf - Configure VRF.
- fortinet.fortimanager.fmgr_switchcontroller_managedswitch_systemdhcpserver - Configure DHCP servers.
- fortinet.fortimanager.fmgr_switchcontroller_managedswitch_systemdhcpserver_options - DHCP options.
- fortinet.fortimanager.fmgr_switchcontroller_managedswitch_systeminterface - Configure system interface on FortiSwitch.
- fortinet.fortimanager.fmgr_switchcontroller_securitypolicy_localaccess - Configure allowaccess list for mgmt and internal interfaces on managed FortiSwitch units.
- fortinet.fortimanager.fmgr_switchcontroller_switchprofile - Configure FortiSwitch switch profile.
- fortinet.fortimanager.fmgr_system_dnsdatabase - Configure DNS databases.
- fortinet.fortimanager.fmgr_system_dnsdatabase_dnsentry - DNS entry.
- fortinet.fortimanager.fmgr_system_localinpolicy6_dport - Cli system local in policy6 dport
- fortinet.fortimanager.fmgr_system_localinpolicy6_dst - Cli system local in policy6 dst
- fortinet.fortimanager.fmgr_system_localinpolicy6_intf - Cli system local in policy6 intf
- fortinet.fortimanager.fmgr_system_localinpolicy6_src - Cli system local in policy6 src
- fortinet.fortimanager.fmgr_system_localinpolicy_dport - Cli system local in policy dport
- fortinet.fortimanager.fmgr_system_localinpolicy_dst - Cli system local in policy dst
- fortinet.fortimanager.fmgr_system_localinpolicy_intf - Cli system local in policy intf
- fortinet.fortimanager.fmgr_system_localinpolicy_src - Cli system local in policy src
- fortinet.fortimanager.fmgr_system_locallog_tacacsaccounting_filter - Cli system locallog tacacs+accounting filter
- fortinet.fortimanager.fmgr_system_locallog_tacacsaccounting_setting - Cli system locallog tacacs+accounting setting
- fortinet.fortimanager.fmgr_system_log_apiratelimit - Cli system log api ratelimit
- fortinet.fortimanager.fmgr_system_log_settings_clientcertauth - Cli system log settings client cert auth
- fortinet.fortimanager.fmgr_telemetrycontroller_agent - Configure FortiTelemetry agents managed by a FortiGate unit.
- fortinet.fortimanager.fmgr_user_oidc - User oidc
- fortinet.fortimanager.fmgr_vpn_certificate_hsmlocal - Local certificates whose keys are stored on HSM.
- fortinet.fortimanager.fmgr_vpn_ipsec_manualkey - Configure IPsec manual keys.
- fortinet.fortimanager.fmgr_vpn_ipsec_phase1 - Configure VPN remote gateway.
- fortinet.fortimanager.fmgr_vpn_ipsec_phase1_ipv4excluderange - Configuration Method IPv4 exclude ranges.
- fortinet.fortimanager.fmgr_vpn_ipsec_phase1_ipv6excluderange - Configuration method IPv6 exclude ranges.
- fortinet.fortimanager.fmgr_vpn_kmipserver - KMIP server entry configuration.
- fortinet.fortimanager.fmgr_vpn_kmipserver_serverlist - KMIP server list.
- fortinet.fortimanager.fmgr_webfilter_domainlist - Webfilter domain list
- fortinet.fortimanager.fmgr_webfilter_domainlist_entries - Webfilter domain list entries
- fortinet.fortimanager.fmgr_webfilter_ftgdrisklevel - Configure FortiGuard Web Filter risk level.
- fortinet.fortimanager.fmgr_webfilter_urllist - Webfilter url list
- fortinet.fortimanager.fmgr_webfilter_urllist_entries - Webfilter url list entries
- fortinet.fortimanager.fmgr_webproxy_explicitproxy - Web proxy explicit proxy
- fortinet.fortimanager.fmgr_webproxy_redirectprofile - Web proxy redirect profile
- fortinet.fortimanager.fmgr_webproxy_redirectprofile_entries - Web proxy redirect profile entries
- fortinet.fortimanager.fmgr_ztna_serviceconnector - Ztna service connector
- fortinet.fortimanager.fmgr_ztna_trafficforwardproxy - Configure ZTNA traffic forward proxy.
- fortinet.fortimanager.fmgr_ztna_trafficforwardproxy_sslserverciphersuites - Ztna traffic forward proxy ssl server cipher suites
- fortinet.fortimanager.fmgr_ztna_trafficforwardproxy_urlroute - Ztna traffic forward proxy url route
- fortinet.fortimanager.fmgr_ztna_webportal - Configure ztna web-portal.
- fortinet.fortimanager.fmgr_ztna_webportalbookmark - Configure ztna web-portal bookmark.
- fortinet.fortimanager.fmgr_ztna_webportalbookmark_bookmarks - Bookmark table.
- fortinet.fortimanager.fmgr_ztna_webproxy - Configure ZTNA web-proxy.
- fortinet.fortimanager.fmgr_ztna_webproxy_apigateway - Set IPv4 API Gateway.
- fortinet.fortimanager.fmgr_ztna_webproxy_apigateway6 - Set IPv6 API Gateway.
- fortinet.fortimanager.fmgr_ztna_webproxy_apigateway6_realservers - Select the real servers that this Access Proxy will distribute traffic to.
- fortinet.fortimanager.fmgr_ztna_webproxy_apigateway6_sslciphersuites - SSL/TLS cipher suites to offer to a server, ordered by priority.
- fortinet.fortimanager.fmgr_ztna_webproxy_apigateway_realservers - Select the real servers that this Access Proxy will distribute traffic to.

hitachivantara.vspone_block
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Sds Block
^^^^^^^^^

- hitachivantara.vspone_block.hv_sds_block_audit_log_setting - Manages Hitachi SDS block storage system audit log settings.
- hitachivantara.vspone_block.hv_sds_block_audit_log_setting_facts - Get audit log setting from SDS Block storage system.
- hitachivantara.vspone_block.hv_sds_block_dump_log_file - Dumps log information from SDS Block storage system.
- hitachivantara.vspone_block.hv_sds_block_dump_log_status_facts - Dumps log status information from SDS Block storage system.
- hitachivantara.vspone_block.hv_sds_block_encryption_environment_setting_facts - Retrieves encryption environment settings from VSP One SDS Block and Cloud systems.
- hitachivantara.vspone_block.hv_sds_block_encryption_environment_settings - Manages encryption environment settings on VSP One SDS Block and Cloud systems.
- hitachivantara.vspone_block.hv_sds_block_encryption_key - Manage encryption keys on VSP One SDS Block and Cloud systems.
- hitachivantara.vspone_block.hv_sds_block_encryption_key_count_facts - Get encryption key count information from VSP One SDS Block and Cloud systems.
- hitachivantara.vspone_block.hv_sds_block_encryption_key_facts - Retrieves encryption key information from VSP One SDS Block and Cloud systems.
- hitachivantara.vspone_block.hv_sds_block_event_log_setting - Manages Hitachi SDS block storage system event log settings.
- hitachivantara.vspone_block.hv_sds_block_event_log_setting_facts - Get event log setting from SDS Block storage system.
- hitachivantara.vspone_block.hv_sds_block_journal - Create and update Journals from storage system.
- hitachivantara.vspone_block.hv_sds_block_journal_facts - Retrieve journal information from storage SDS Block storage system.
- hitachivantara.vspone_block.hv_sds_block_license - Manage licenses on SDS Block storage system.
- hitachivantara.vspone_block.hv_sds_block_license_facts - Get license(s) from SDS Block storage system.
- hitachivantara.vspone_block.hv_sds_block_license_setting - Manage license settings for SDS Block storage system.
- hitachivantara.vspone_block.hv_sds_block_license_setting_facts - Get license setting from SDS Block storage system.
- hitachivantara.vspone_block.hv_sds_block_login_message - Update the login message displayed in the GUI login window and CLI warning banner.
- hitachivantara.vspone_block.hv_sds_block_login_message_facts - Get the login message displayed in the GUI login window and CLI warning banner.
- hitachivantara.vspone_block.hv_sds_block_remote_path_group - Manages remote path groups on VSP One SDS Block and Cloud systems.
- hitachivantara.vspone_block.hv_sds_block_remote_path_group_facts - Get information about remote path groups from VSP One SDS Block and Cloud systems.
- hitachivantara.vspone_block.hv_sds_block_session - Manages sessions on VSP One SDS Block and Cloud systems.
- hitachivantara.vspone_block.hv_sds_block_session_facts - Retrieves information about sessions on VSP One SDS Block and Cloud systems.
- hitachivantara.vspone_block.hv_sds_block_storage_external_auth_server_setting - Manages external authentication server settings on VSP One SDS Block and Cloud systems.
- hitachivantara.vspone_block.hv_sds_block_storage_external_auth_server_setting_facts - Get external authentication server settings from the storage system.
- hitachivantara.vspone_block.hv_sds_block_storage_user_auth_setting - Manages external authentication server settings on VSP One SDS Block and Cloud systems.
- hitachivantara.vspone_block.hv_sds_block_storage_user_auth_setting_facts - Get user authentication settings from the storage system.
- hitachivantara.vspone_block.hv_sds_block_user_group - Create and update user groups on the storage system.
- hitachivantara.vspone_block.hv_sds_block_web_server - Manages the web server access setting for VSP One SDS Block and Cloud systems.
- hitachivantara.vspone_block.hv_sds_block_web_server_facts - Get the web server access setting from VSP One SDS Block and Cloud systems.

Vsp
^^^

- hitachivantara.vspone_block.hv_pav_alias - Manages PAV (Parallel Access Volume) alias assignments for VSP block storage systems.
- hitachivantara.vspone_block.hv_pav_alias_facts - retrieves information about PAV aliases from VSP block storage systems.
- hitachivantara.vspone_block.hv_session - Manages sessions on VSP block storage systems.
- hitachivantara.vspone_block.hv_session_facts - Retrieves information about sessions on VSP block storage systems.
- hitachivantara.vspone_block.hv_snapshot_family_facts - Retrieves snapshot family information of the provided LDEV ID from VSP block storage systems.
- hitachivantara.vspone_block.hv_supported_host_mode_facts - Retrieves supported host mode options information from a specified VSP block storage system.
- hitachivantara.vspone_block.hv_vclone_parent_volume_facts - Retrieves virtual clone parent volume information from VSP block storage systems.

ibm.storage_virtualize
~~~~~~~~~~~~~~~~~~~~~~

- ibm.storage_virtualize.ibm_sv_manage_clone - This module manages clone and thinclone of volume and volumegroup.

kaytus.ksmanage
~~~~~~~~~~~~~~~

- kaytus.ksmanage.generate_ssl - Generate SSL certificate
- kaytus.ksmanage.ssl_info - Get SSL certificate information
- kaytus.ksmanage.upload_ssl - Upload SSL certificate

netapp.ontap
~~~~~~~~~~~~

- netapp.ontap.na_ontap_autoupdate_config - NetApp ONTAP module to manage configurations for automatic updates.
- netapp.ontap.na_ontap_cg - NetApp ONTAP module to manage operations related to consistency groups.

netapp.storagegrid
~~~~~~~~~~~~~~~~~~

- netapp.storagegrid.na_sg_grid_firewall - NetApp StorageGRID manage node firewall.
- netapp.storagegrid.na_sg_grid_login - Login to StorageGRID grid/tenant.
- netapp.storagegrid.na_sg_grid_metrics - NetApp StorageGRID grab metrics.
- netapp.storagegrid.na_sg_grid_recovery_package - Retrieve the recovery package from StorageGRID
- netapp.storagegrid.na_sg_grid_ssh_security - Configure ssh security on StorageGRID.
- netapp.storagegrid.na_sg_grid_untrusted_client_network - Configure untrusted Client Network on StorageGRID.
- netapp.storagegrid.na_sg_org_cloud_mirror_replication - Manage Cloud Mirror Replication on StorageGRID.
- netapp.storagegrid.na_sg_pge_info - NetApp StorageGRID node PGE information gatherer.

netbox.netbox
~~~~~~~~~~~~~

- netbox.netbox.netbox_contact_assignment - Manage contact assignments in NetBox
- netbox.netbox.netbox_data_source - Manage data sources in NetBox

splunk.es
~~~~~~~~~

- splunk.es.splunk_finding - Manage Splunk Enterprise Security findings
- splunk.es.splunk_finding_info - Gather information about Splunk Enterprise Security Findings
- splunk.es.splunk_investigation - Manage Splunk Enterprise Security investigations
- splunk.es.splunk_investigation_info - Gather information about Splunk Enterprise Security Investigations
- splunk.es.splunk_investigation_type - Manage Splunk Enterprise Security investigation types
- splunk.es.splunk_investigation_type_info - Gather information about Splunk Enterprise Security investigation types
- splunk.es.splunk_notes - Manage notes for findings, investigations, and response plan tasks
- splunk.es.splunk_notes_info - Gather information about notes in Splunk Enterprise Security
- splunk.es.splunk_response_plan - Manage Splunk Enterprise Security response plans
- splunk.es.splunk_response_plan_execution - Apply response plans to investigations and manage tasks
- splunk.es.splunk_response_plan_execution_info - Gather information about applied response plans on an investigation
- splunk.es.splunk_response_plan_info - Gather information about Splunk Enterprise Security response plans

theforeman.foreman
~~~~~~~~~~~~~~~~~~

- theforeman.foreman.smart_proxy_refresh - Refresh Smart Proxy features

vultr.cloud
~~~~~~~~~~~

- vultr.cloud.load_balancer - Manages load balancers on Vultr
- vultr.cloud.load_balancer_info - Get information about Vultr load balancers
- vultr.cloud.object_storage_cluster_info - Get information about the Vultr object storage clusters
- vultr.cloud.object_storage_info - Get information about the Vultr object stores

Unchanged Collections
---------------------

- ansible.posix (still version 2.1.0)
- cisco.ucs (still version 1.16.0)
- community.ciscosmb (still version 1.0.11)
- community.grafana (still version 2.3.0)
- community.hashi_vault (still version 7.1.0)
- community.library_inventory_filtering_v1 (still version 1.1.5)
- community.okd (still version 5.0.0)
- community.proxysql (still version 1.7.0)
- community.rabbitmq (still version 1.6.0)
- community.zabbix (still version 4.1.1)
- dellemc.powerflex (still version 3.0.0)
- dellemc.unity (still version 2.1.0)
- f5networks.f5_modules (still version 1.39.0)
- grafana.grafana (still version 6.0.6)
- ieisystem.inmanage (still version 4.0.0)
- infinidat.infinibox (still version 1.6.3)
- lowlydba.sqlserver (still version 2.7.0)
- netapp.cloudmanager (still version 21.24.0)
- ngine_io.cloudstack (still version 3.0.0)
- openstack.cloud (still version 2.5.0)
- ravendb.ravendb (still version 1.0.4)
- vyos.vyos (still version 6.0.0)
