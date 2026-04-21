========================
Ansible 13 Release Notes
========================

This changelog describes changes since Ansible 12.0.0.

.. contents::
  :depth: 2

v13.6.0
=======

.. contents::
  :local:
  :depth: 2

Release Summary
---------------

Release Date: 2026-04-21

`Porting Guide <https://docs.ansible.com/projects/ansible/devel/porting_guides.html>`_

Ansible-core
------------

Ansible 13.6.0 contains ansible-core version 2.20.5.
This is a newer version than version 2.20.4 contained in the previous Ansible release.

The changes are reported in the combined changelog below.

Changed Collections
-------------------

If not mentioned explicitly, the changes are reported in the combined changelog below.

+------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| Collection             | Ansible 13.5.0 | Ansible 13.6.0 | Notes                                                                                                                        |
+========================+================+================+==============================================================================================================================+
| ansible.netcommon      | 8.4.0          | 8.5.0          |                                                                                                                              |
+------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| ansible.utils          | 6.0.1          | 6.0.2          |                                                                                                                              |
+------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| chocolatey.chocolatey  | 1.5.3          | 1.6.0          |                                                                                                                              |
+------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.intersight       | 2.16.0         | 2.18.0         | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.iosxr            | 12.1.1         | 12.2.1         |                                                                                                                              |
+------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.meraki           | 2.23.1         | 2.23.2         |                                                                                                                              |
+------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.crypto       | 3.1.1          | 3.2.0          |                                                                                                                              |
+------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.dns          | 3.5.3          | 3.5.4          |                                                                                                                              |
+------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.docker       | 5.1.0          | 5.2.0          |                                                                                                                              |
+------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.general      | 12.5.0         | 12.6.0         |                                                                                                                              |
+------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.libvirt      | 2.1.0          | 2.2.0          |                                                                                                                              |
+------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.routeros     | 3.18.0         | 3.20.0         |                                                                                                                              |
+------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.sops         | 2.2.7          | 2.3.0          |                                                                                                                              |
+------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.zabbix       | 4.1.1          | 4.2.0          |                                                                                                                              |
+------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| containers.podman      | 1.19.0         | 1.19.2         |                                                                                                                              |
+------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| dellemc.openmanage     | 10.0.1         | 10.0.2         |                                                                                                                              |
+------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| fortinet.fortios       | 2.5.0          | 2.5.1          |                                                                                                                              |
+------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| google.cloud           | 1.12.0         | 1.13.0         |                                                                                                                              |
+------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| graphiant.naas         | 26.2.4         | 26.3.0         |                                                                                                                              |
+------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| ibm.storage_virtualize | 3.2.0          | 3.3.0          |                                                                                                                              |
+------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| lowlydba.sqlserver     | 2.7.0          | 2.8.1          |                                                                                                                              |
+------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| theforeman.foreman     | 5.10.0         | 5.11.0         |                                                                                                                              |
+------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+

Major Changes
-------------

chocolatey.chocolatey
~~~~~~~~~~~~~~~~~~~~~

- win_chocolatey - add option to ignore pinned status of pinned packages

fortinet.fortios
~~~~~~~~~~~~~~~~

- Added a generic `headers` parameter to `fortios_json_generic` to support admin-password confirmation headers and future custom request headers.
- Updated FAQ to illustrate the use of `headers` in `fortios_json_generic` module.
- Updated deprecated import of to_text from ansible.module_utils._text to the supported implementation.

Minor Changes
-------------

Ansible-core
~~~~~~~~~~~~

- ansible-test - Generate ``dist_info`` when running tests.
- ansible-test - Replace the ``parallels`` managed macOS provider with a new ``mac`` provider.
- ansible-test - Switch managed macOS remotes from x86_64 to aarch64.

ansible.netcommon
~~~~~~~~~~~~~~~~~

- The dependency on ansible-pylibssh (for ssh_type=libssh / network_cli) is now ansible-pylibssh>=1.4.0 in requirements.txt, raised from the previous >=0.2.0 requirement. Installations still on ansible-pylibssh 0.x or 1.x below 1.4.0 must upgrade to use the libssh connection path with this collection release.
- libssh connection - When log_path is set (e.g. via ANSIBLE_LOG_PATH or log_path in ansible.cfg), the plugin now routes ansible-pylibssh (libssh) logs into the same Ansible log file. Log level is derived from display.verbosity using Python standard logging: verbosity 0 -> WARNING, 1-2 -> INFO, 3+ -> DEBUG. This allows SSH/libssh debug and trace output to appear in the configured log file for troubleshooting without changing ansible-pylibssh configuration manually.
- network_cli - The in-collection paramiko path supports the same host key policy behavior (including host_key_auto_add and known_hosts handling) and persistent connection caching as the previous ansible-core paramiko integration.
- network_cli - When ssh_type is set to paramiko, the connection plugin now uses an in-collection paramiko implementation instead of loading ansible-core's paramiko connection plugin. This allows network_cli to work with versions of ansible-core, where the paramiko connection plugin was removed.

cisco.iosxr
~~~~~~~~~~~

- iosxr_l3_interfaces - Added support for `flow.ipv4.direction` and `flow.ipv6.direction` value `bidirectional`. The module now expands bidirectional flow configuration into both ingress and egress IOS-XR flow monitor commands.

community.crypto
~~~~~~~~~~~~~~~~

- acme_* modules - experimentally support ``dns-account-01`` challenge type according to `acme-dns-account-label draft 02 <https://datatracker.ietf.org/doc/html/draft-ietf-acme-dns-account-label-02>`__. Note that breaking changes to this challenge type can also happen in minor releases until the acme-dns-account-label draft has been finalized as an RFC (https://github.com/ansible-collections/community.crypto/pull/996).
- acme_* modules - experimentally support ``dns-persist-01`` challenge type according to `acme-dns-persist draft 01 <https://www.ietf.org/archive/id/draft-ietf-acme-dns-persist-01.html>`__. Note that breaking changes to this challenge type can also happen in minor releases until the acme-dns-persist draft has been finalized as an RFC (https://github.com/ansible-collections/community.crypto/pull/997).

community.docker
~~~~~~~~~~~~~~~~

- docker_image_export - adds ``platform`` parameter to allow exporting a specific platform variant from a multi-arch image (https://github.com/ansible-collections/community.docker/issues/1064, https://github.com/ansible-collections/community.docker/pull/1251).

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

community.libvirt
~~~~~~~~~~~~~~~~~

- virt_cloud_instance - added commands return field to provide visibility into executed commands during VM provisioning.
- virt_install - added commands return field to provide visibility into executed commands during VM provisioning.

community.routeros
~~~~~~~~~~~~~~~~~~

- api_info - add missing ``numbers`` parameter across numerous existing paths for RouterOS >= 7.15.2 (https://github.com/ansible-collections/community.routeros/pull/458).
- api_info - add support for the ``interface dot1x server active``, ``ip hotspot active``, ``ip ipsec active-peers``, ``ip proxy cache-contents``, ``ip socks connections``, ``user active``, and ``user-manager session`` paths as info-only (read-only) paths (https://github.com/ansible-collections/community.routeros/pull/458).
- api_info - adds support for additional read-only parameters in the ``app`` path for RouterOS >= 7.22 (https://github.com/ansible-collections/community.routeros/pull/457).
- api_info, api_modify - add 46 new parameters to the ``interface ethernet switch port`` path for RouterOS >= 7.15 (CRS1xx/2xx variant) including QoS, mirroring, VLAN, and learning control parameters (https://github.com/ansible-collections/community.routeros/pull/463).
- api_info, api_modify - add ``color`` parameter to the ``zerotier interface`` path for RouterOS >= 7.22.1 (https://github.com/ansible-collections/community.routeros/pull/459).
- api_info, api_modify - add ``comment``, ``disabled``, ``independent-learning``, ``qos-group``, ``svl``, and ``switch`` parameters to the ``interface ethernet switch vlan`` path for RouterOS >= 7.15 (CRS1xx/2xx variant) (https://github.com/ansible-collections/community.routeros/pull/463).
- api_info, api_modify - add ``current-defaults`` parameter to the ``ip dns`` path for RouterOS >= 7.22.1 (https://github.com/ansible-collections/community.routeros/pull/459).
- api_info, api_modify - add ``mld-datapath`` parameter to the ``interface wifi cap`` path for RouterOS >= 7.22.1 (https://github.com/ansible-collections/community.routeros/pull/459).
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

community.sops
~~~~~~~~~~~~~~

- all modules and plugins - allow retrieving private age keys and private SSH keys through commands with the new ``age_key_cmd`` and ``age_ssh_private_key_cmd`` options (https://github.com/ansible-collections/community.sops/issues/282, https://github.com/ansible-collections/community.sops/pull/286).
- all modules and plugins - allow to configure GCP access with the ``gcp_oauth_access_token`` and ``gcp_kms_client_type`` options (https://github.com/ansible-collections/community.sops/issues/282, https://github.com/ansible-collections/community.sops/pull/286).
- load_vars - now supports ansible-core 2.21's way of actually loading variables, instead of returning ``ansible_facts``. The behavior for this can be controlled through the new ``return_method`` option, which is by default set to ``auto``. On ansible-core 2.21+, ``auto`` behaves the same as ``vars-only`` (return proper variables), and for ansible-core before 2.21 the same as ``facts-only`` (return ``ansible_facts``) (https://github.com/ansible-collections/community.sops/pull/283).
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

containers.podman
~~~~~~~~~~~~~~~~~

- Add --platform option to podman_image

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- Added support for OpenManage Enterprise version 4.4 and 4.5.
- The OpenManage Enterprise, OpenManage Enterprise Modular and OpenManage Enterprise Integration for VMware vCenter modules are now compatible with Ansible Core version 2.20.

google.cloud
~~~~~~~~~~~~

- gcp_colab_* - added four new modules (gcp_colab_notebook_execution, gcp_colab_runtime, gcp_colab_runtime_template, and gcp_colab_schedule) (https://github.com/ansible-collections/google.cloud/pull/747).
- gcp_compute_instance_* - renamed the `tags.items` field to `tags.tag_values`. The old naming is still available but will be removed in a future release. (https://github.com/ansible-collections/google.cloud/pull/750).

graphiant.naas
~~~~~~~~~~~~~~

- Minimum ``graphiant-sdk`` raised to ``>= 26.3.0`` (see ``_version.py`` ``DEPENDENCIES``)
- Portal authentication: optional ``access_token`` module option and ``GRAPHIANT_ACCESS_TOKEN`` environment variable (e.g. after ``graphiant login``); invalid or missing token falls back to username/password when provided

ibm.storage_virtualize
~~~~~~~~~~~~~~~~~~~~~~

- ibm_svc_initial_setup - Added support for managing anomaly settings
- ibm_svc_manage_volume - Added support for addressing volume via UID

lowlydba.sqlserver
~~~~~~~~~~~~~~~~~~

- user_role - Added ``roles`` parameter with ``add``/``remove``/``set`` pattern to manage multiple roles. The existing ``role`` parameter is deprecated and will be removed in 3.0.0. (#352)

theforeman.foreman
~~~~~~~~~~~~~~~~~~

- Support OAuth1 authentication by passing ``oauth1_consumer_key`` and ``oauth1_consumer_secret`` instead of ``username`` and ``password``.
- registration_command - add support for the setup_container_registry_certs parameter (https://github.com/theforeman/foreman-ansible-modules/pull/1966)

Deprecated Features
-------------------

- The ``cisco.dnac`` collection has been deprecated.
  It will be removed from Ansible 14 if no one starts maintaining it again before Ansible 14.
  See `Collections Removal Process for unmaintained collections <https://docs.ansible.com/projects/ansible/devel/community/collection_contributors/collection_package_removal.html#unmaintained-collections>`__ for more details (`https://forum.ansible.com/t/45609 <https://forum.ansible.com/t/45609>`__).

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
- ansible-galaxy collection - Fix using the server configuration for ``validate_certs`` when downloading collections. (https://github.com/ansible/ansible/issues/86694)
- ansible_facts[os_*] - Contained wrong information, if ClearLinux parsing was tried before falling back to general os-release parsing
- templating - Fix traceback when using ``deepcopy`` on an imported template (https://github.com/ansible/ansible/issues/86723).

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

cisco.iosxr
~~~~~~~~~~~

- Fixed iosxr_user module to correctly handle MD5 hashed passwords when updating user credentials.

cisco.meraki
~~~~~~~~~~~~

- devices_switch_ports - Fixed AttributeError crash in ``update()`` caused by ``get_object_by_name`` returning the full port list instead of ``None`` when no port matched by name. Added ``isinstance(prev_obj_name, dict)`` guard to prevent calling ``.get()`` on a list.
- devices_switch_ports - Fixed idempotency regression where the module always reported ``changed`` due to ``serial`` (a path parameter absent from the API response) and ``portId`` (int/string type mismatch) being incorrectly included in the ``requires_update`` comparison.

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

community.libvirt
~~~~~~~~~~~~~~~~~

- libvirt_qemu - Vendor ``_parse_clixml`` locally to fix ``ImportError`` on ansible-core devel (2.21+).

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

containers.podman
~~~~~~~~~~~~~~~~~

- podman_container - Fix quadlet_options placement when restart_policy is set
- podman_network - Add diff and idempotency to ip_ranges in net_config

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- idrac_job_queue - (Issue 1067) - Fails to find the file in role due to incorrect name (https://github.com/dell/dellemc-openmanage-ansible-modules/issues/1067)
- idrac_system_info - (Issue 1044) - FC section is missing (https://github.com/dell/dellemc-openmanage-ansible-modules/issues/1044)
- idrac_system_info - powersupply.get_red_type_set fails with TypeError due to unhandled None values when joining mapped redundancy types
- idrac_user - (Issue 1059) - Bad User Privileges when creating idrac user using "custom_privilege" (https://github.com/dell/dellemc-openmanage-ansible-modules/issues/1059)

fortinet.fortios
~~~~~~~~~~~~~~~~

- Fixed an issue where parameters ending with _dict always returned changed, even in check mode or when no changes were made.
- Fixed an issue where some modules could not be configured globally.
- Fixed an issue where the generate-key.system.api-user selector in the fortios_monitor module required an admin password to function.

ibm.storage_virtualize
~~~~~~~~~~~~~~~~~~~~~~

- ibm_svc_manage_ip - Fixed issue related to VLAN while updating

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
- ome_smart_fabric_uplink - The module supported by OpenManage Enterprise Modular, however it does not allow the creation of multiple uplinks of the same name. If an uplink is created using the same name as an existing uplink, then the existing uplink is modified.
- redfish_storage_volume - Encryption type and block_io_size bytes will be read only property in iDRAC9 and iDRAC10 and hence the module ignores these parameters.

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

Unchanged Collections
---------------------

- amazon.aws (still version 10.3.0)
- ansible.posix (still version 2.1.0)
- ansible.windows (still version 3.5.0)
- arista.eos (still version 12.0.1)
- awx.awx (still version 24.6.1)
- azure.azcollection (still version 3.16.0)
- check_point.mgmt (still version 6.9.0)
- cisco.aci (still version 2.13.0)
- cisco.dnac (still version 6.48.0)
- cisco.ios (still version 11.3.0)
- cisco.mso (still version 2.13.0)
- cisco.nxos (still version 11.1.3)
- cisco.ucs (still version 1.16.0)
- cloudscale_ch.cloud (still version 2.5.3)
- community.aws (still version 10.1.0)
- community.ciscosmb (still version 1.0.11)
- community.clickhouse (still version 2.1.0)
- community.grafana (still version 2.3.0)
- community.hashi_vault (still version 7.1.0)
- community.hrobot (still version 2.7.1)
- community.library_inventory_filtering_v1 (still version 1.1.5)
- community.mongodb (still version 1.7.12)
- community.mysql (still version 4.2.0)
- community.okd (still version 5.0.0)
- community.postgresql (still version 4.2.0)
- community.proxmox (still version 1.6.0)
- community.proxysql (still version 1.7.0)
- community.rabbitmq (still version 1.6.0)
- community.sap_libs (still version 1.7.0)
- community.vmware (still version 6.2.0)
- community.windows (still version 3.1.0)
- cyberark.conjur (still version 1.3.9)
- cyberark.pas (still version 1.0.39)
- dellemc.enterprise_sonic (still version 3.2.0)
- dellemc.powerflex (still version 3.0.0)
- dellemc.unity (still version 2.1.0)
- f5networks.f5_modules (still version 1.39.0)
- fortinet.fortimanager (still version 2.13.0)
- grafana.grafana (still version 6.0.6)
- hetzner.hcloud (still version 6.8.0)
- hitachivantara.vspone_block (still version 4.6.1)
- hitachivantara.vspone_object (still version 1.1.1)
- ieisystem.inmanage (still version 4.0.0)
- infinidat.infinibox (still version 1.6.3)
- infoblox.nios_modules (still version 1.9.0)
- inspur.ispim (still version 2.2.4)
- junipernetworks.junos (still version 11.0.0)
- kaytus.ksmanage (still version 2.0.0)
- kubernetes.core (still version 6.3.0)
- kubevirt.core (still version 2.2.4)
- microsoft.ad (still version 1.10.0)
- microsoft.iis (still version 1.1.0)
- netapp.cloudmanager (still version 21.24.0)
- netapp.ontap (still version 23.4.0)
- netapp.storagegrid (still version 21.16.0)
- netapp_eseries.santricity (still version 1.4.1)
- netbox.netbox (still version 3.22.0)
- ngine_io.cloudstack (still version 3.0.0)
- openstack.cloud (still version 2.5.0)
- ovirt.ovirt (still version 3.2.2)
- pcg.alpaca_operator (still version 2.2.0)
- purestorage.flasharray (still version 1.42.0)
- purestorage.flashblade (still version 1.24.0)
- ravendb.ravendb (still version 1.0.4)
- splunk.es (still version 4.0.0)
- telekom_mms.icinga_director (still version 2.5.1)
- vmware.vmware (still version 2.8.0)
- vmware.vmware_rest (still version 4.10.0)
- vultr.cloud (still version 1.14.0)
- vyos.vyos (still version 6.0.0)
- wti.remote (still version 1.0.11)

v13.5.0
=======

.. contents::
  :local:
  :depth: 2

Release Summary
---------------

Release Date: 2026-03-25

`Porting Guide <https://docs.ansible.com/projects/ansible/devel/porting_guides.html>`_

Added Collections
-----------------

- graphiant.naas (version 26.2.4)

Ansible-core
------------

Ansible 13.5.0 contains ansible-core version 2.20.4.
This is a newer version than version 2.20.3 contained in the previous Ansible release.

The changes are reported in the combined changelog below.

Changed Collections
-------------------

If not mentioned explicitly, the changes are reported in the combined changelog below.

+-----------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| Collection            | Ansible 13.4.0 | Ansible 13.5.0 | Notes                                                                                                                        |
+=======================+================+================+==============================================================================================================================+
| amazon.aws            | 10.2.0         | 10.3.0         |                                                                                                                              |
+-----------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| ansible.windows       | 3.3.0          | 3.5.0          |                                                                                                                              |
+-----------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| azure.azcollection    | 3.14.0         | 3.16.0         | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+-----------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| check_point.mgmt      | 6.8.0          | 6.9.0          | The collection did not have a changelog in this version.                                                                     |
+-----------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.intersight      | 2.12.0         | 2.16.0         | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+-----------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.meraki          | 2.22.1         | 2.23.1         |                                                                                                                              |
+-----------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.mso             | 2.12.0         | 2.13.0         |                                                                                                                              |
+-----------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.clickhouse  | 2.0.0          | 2.1.0          |                                                                                                                              |
+-----------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.dns         | 3.5.2          | 3.5.3          |                                                                                                                              |
+-----------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.docker      | 5.0.6          | 5.1.0          |                                                                                                                              |
+-----------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.general     | 12.4.0         | 12.5.0         |                                                                                                                              |
+-----------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.hrobot      | 2.7.0          | 2.7.1          |                                                                                                                              |
+-----------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.mysql       | 4.1.0          | 4.2.0          |                                                                                                                              |
+-----------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.proxmox     | 1.5.0          | 1.6.0          |                                                                                                                              |
+-----------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.routeros    | 3.16.0         | 3.18.0         |                                                                                                                              |
+-----------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.sap_libs    | 1.6.0          | 1.7.0          |                                                                                                                              |
+-----------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| cyberark.pas          | 1.0.36         | 1.0.39         | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+-----------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| fortinet.fortimanager | 2.12.0         | 2.13.0         |                                                                                                                              |
+-----------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| fortinet.fortios      | 2.4.2          | 2.5.0          |                                                                                                                              |
+-----------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| google.cloud          | 1.11.0         | 1.12.0         |                                                                                                                              |
+-----------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| graphiant.naas        |                | 26.2.4         | The collection was added to Ansible                                                                                          |
+-----------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| hetzner.hcloud        | 6.7.0          | 6.8.0          |                                                                                                                              |
+-----------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| kubevirt.core         | 2.2.3          | 2.2.4          | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+-----------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| netapp.ontap          | 23.3.0         | 23.4.0         |                                                                                                                              |
+-----------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| theforeman.foreman    | 5.8.0          | 5.10.0         |                                                                                                                              |
+-----------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| vmware.vmware         | 2.7.0          | 2.8.0          |                                                                                                                              |
+-----------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| vultr.cloud           | 1.13.0         | 1.14.0         |                                                                                                                              |
+-----------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| wti.remote            | 1.0.10         | 1.0.11         | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+-----------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+

Major Changes
-------------

community.proxmox
~~~~~~~~~~~~~~~~~

- proxmox - Add ca_path option to specify a ca-certificate for tls validation (https://github.com/ansible-collections/community.proxmox/pull/256).

community.routeros
~~~~~~~~~~~~~~~~~~

- api_info, api_modify - multiple parameters can no longer be disabled for the``tool netwatch`` path (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - parameter ``name-format`` can no longer be disabled for the ``interface wifi provisioning`` path (https://github.com/ansible-collections/community.routeros/pull/433).
- api_info, api_modify - parameter ``script`` can no longer be disabled for the ``ip dhcp-client`` path (https://github.com/ansible-collections/community.routeros/pull/433).

fortinet.fortios
~~~~~~~~~~~~~~~~

- Supported new versions 7.6.5 and 7.6.6.
- Updated the Q&A for using the default_group feature in modules.

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
- na_ontap_lun_copy - AWS Lambda support added to the module.
- na_ontap_lun_map - AWS Lambda support added to the module.
- na_ontap_lun_map_reporting_nodes - AWS Lambda support added to the module.
- na_ontap_s3_buckets - AWS Lambda support added to the module.
- na_ontap_s3_groups - AWS Lambda support added to the module.
- na_ontap_s3_policies - AWS Lambda support added to the module.
- na_ontap_s3_services - AWS Lambda support added to the module.
- na_ontap_s3_users - AWS Lambda support added to the module.
- na_ontap_snapmirror - AWS Lambda support added to the module.
- na_ontap_volume_autosize - AWS Lambda support added to the module.
- na_ontap_volume_clone - AWS Lambda support added to the module.
- na_ontap_vserver_peer - AWS Lambda support added to the module.

Minor Changes
-------------

Ansible-core
~~~~~~~~~~~~

- ansible-test - Add container/remote aliases for more loosely specifying managed test environments.
- ansible-test - Add support for using the Ansible Core CI service from GitHub Actions.

amazon.aws
~~~~~~~~~~

- meta/runtime.yml - Lowered the ``ansible-core`` minimum version to ``2.16``. This expands compatibility and does not change or remove existing functionality.

ansible.windows
~~~~~~~~~~~~~~~

- PowerShell 7 - Add initial support for running modules against PowerShell 7 interpreters. Support for PowerShell 7 varies across each module, see module documentation for more information.
- ansible.windows.win_package - Add optional Authenticode signature validation for installer files via the new ``verify_signature`` parameter.
- win_file - is aligned with ``ansible.builtin.file`` and now supports options ``access_time``, ``access_time_format``, ``modification_time``, and ``modification_time_format``. (https://github.com/ansible-collections/ansible.windows/issues/798)
- win_shell - Add ``cmd`` module option that can be used instead of the free form input. This aligns the options to the POSIX ``shell`` module.
- win_shell - Support using ``pwsh.exe`` as the executable in a mode similar to how ``powershell.exe`` is run.

cisco.meraki
~~~~~~~~~~~~

- Added new modules and action plugins for Cisco Umbrella account connect/disconnect, Wireless AutoRF (RRM) settings, third-party VPN peers, organization integrations, inventory EoX overview, network moves, SASE eligible networks, and wireless device provisioning deployments.
- networks_wireless_settings: added multicast-to-unicast conversion support.
- organizations_inventory_devices_info: added eoxStatuses filtering and included EoX fields in returned inventory device data.

cisco.mso
~~~~~~~~~

- Add support to deploy and undeploy non-schema templates in ndo_template_deploy (formerly ndo_schema_template_deploy).

community.clickhouse
~~~~~~~~~~~~~~~~~~~~

- clickhouse_user - added new ``authentication`` dict parameter supporting LDAP, hashed, and plain-text password authentication for created users. Cannot be used together with the existing ``type_password`` and ``password`` parameters (https://github.com/ansible-collections/community.clickhouse/issues/142).

community.docker
~~~~~~~~~~~~~~~~

- docker_compose_v2_pull - adds ``ignore_pull_failures`` parameter that passes ``--ignore-pull-failures`` to the ``docker compose pull`` call when set to ``true`` (https://github.com/ansible-collections/community.docker/pull/1248).

community.general
~~~~~~~~~~~~~~~~~

- ansible_galaxy_install - add parameter ``executable`` (https://github.com/ansible-collections/community.general/issues/7261, https://github.com/ansible-collections/community.general/pull/11646).
- api module utils - use Python-defined constants for HTTP return codes (https://github.com/ansible-collections/community.general/pull/11561).
- bitbucket module utils - use Python-defined constants for HTTP return codes (https://github.com/ansible-collections/community.general/pull/11561).
- consul module utils - use Python-defined constants for HTTP return codes (https://github.com/ansible-collections/community.general/pull/11561, https://github.com/ansible-collections/community.general/pull/11573).
- doas become plugin - add new option ``allow_pipelining`` to explicitly allow the use of pipelining with this plugin. This should only be set to ``true`` with ansible-core 2.19+ when ``doas`` does not require a password (https://github.com/ansible-collections/community.general/issues/11411, https://github.com/ansible-collections/community.general/pull/11481).
- gandi_livedns_api module utils - use Python-defined constants for HTTP return codes (https://github.com/ansible-collections/community.general/pull/11561).
- github_app_access_token lookup plugin - use Python-defined constants for HTTP return codes (https://github.com/ansible-collections/community.general/pull/11561).
- hwc_utils module utils - use Python-defined constants for HTTP return codes (https://github.com/ansible-collections/community.general/pull/11561, https://github.com/ansible-collections/community.general/pull/11573).
- icinga2 inventory plugin - use Python-defined constants for HTTP return codes (https://github.com/ansible-collections/community.general/pull/11561, https://github.com/ansible-collections/community.general/pull/11573).
- incus inventory plugin - add support for constructing project-independent FQDNs (https://github.com/ansible-collections/community.general/pull/11555).
- ipa module utils - use Python-defined constants for HTTP return codes (https://github.com/ansible-collections/community.general/pull/11561).
- keycloak module utils - use Python-defined constants for HTTP return codes (https://github.com/ansible-collections/community.general/pull/11561).
- keycloak_realm - add ``first_broker_login_flow`` parameter (https://github.com/ansible-collections/community.general/pull/11622).
- ldap_attrs - add ``binary_attributes`` and ``honor_binary`` parameters to handle binary attribute values (https://github.com/ansible-collections/community.general/pull/11558).
- ldap_entry - add ``binary_attributes`` and ``honor_binary`` parameters to handle creating objects with attributes set to binary values (https://github.com/ansible-collections/community.general/pull/11558).
- lookup plugin passwordstore - modernize internal ``check_output2()`` helper using ``subprocess.run()`` and rename it to ``run_backend_cmd()`` (https://github.com/ansible-collections/community.general/pull/11655).
- memset module utils - use Python-defined constants for HTTP return codes (https://github.com/ansible-collections/community.general/pull/11561).
- merge_variables lookup plugin - extended merging capabilities added (https://github.com/ansible-collections/community.general/pull/11536).
- nmcli - fix idempotency for MAC VLAN interfaces when using ``macvlan.tap`` (https://github.com/ansible-collections/community.general/pull/11551).
- nsupdate - replace ``list(map(...))`` constructs with Python comprehensions (https://github.com/ansible-collections/community.general/pull/11590).
- ocapi_utils module utils - use Python-defined constants for HTTP return codes (https://github.com/ansible-collections/community.general/pull/11561).
- oci_utils module utils - use Python-defined constants for HTTP return codes (https://github.com/ansible-collections/community.general/pull/11561).
- online module utils - use Python-defined constants for HTTP return codes (https://github.com/ansible-collections/community.general/pull/11561).
- osx_defaults - add support for ``dict`` type values, including ``dict_mode`` option to merge keys into an existing dictionary (https://github.com/ansible-collections/community.general/issues/238, https://github.com/ansible-collections/community.general/pull/11659).
- redfish_utils module utils - use Python-defined constants for HTTP return codes (https://github.com/ansible-collections/community.general/pull/11561, https://github.com/ansible-collections/community.general/pull/11573).
- rundeck module utils - use Python-defined constants for HTTP return codes (https://github.com/ansible-collections/community.general/pull/11561, https://github.com/ansible-collections/community.general/pull/11573).
- scaleway module utils - use Python-defined constants for HTTP return codes (https://github.com/ansible-collections/community.general/pull/11561).
- supervisorctl - added an additional condition for generating the error 'no such process' (https://github.com/ansible-collections/community.general/issues/11621, https://github.com/ansible-collections/community.general/pull/11632).
- timezone - replace ``list(map(...))`` constructs with Python comprehensions (https://github.com/ansible-collections/community.general/pull/11590).
- utm_utils module utils - use Python-defined constants for HTTP return codes (https://github.com/ansible-collections/community.general/pull/11561, https://github.com/ansible-collections/community.general/pull/11573).

community.mysql
~~~~~~~~~~~~~~~

- Update imports from ansible.module_utils._text to use ansible.module_utils.common.text.converters

community.proxmox
~~~~~~~~~~~~~~~~~

- inventory plugin - add want_post_filtering_facts to delay fact gathering until filtering has completed (https://github.com/ansible-collections/community.proxmox/pull/261).
- proxmox - Add api_timeout option for all modules (https://github.com/ansible-collections/community.proxmox/pull/253).
- proxmox_role - add role's privs on the return data (https://github.com/ansible-collections/community.proxmox/pull/283).
- proxmox_storage - Add support for ZFS thin-provisioning (https://github.com/ansible-collections/community.proxmox/pull/265).
- proxmox_storage - Add the option namespace for PBS storage (https://github.com/ansible-collections/community.proxmox/pull/282)
- proxmox_storage - refactor the validation of storage options (https://github.com/ansible-collections/community.proxmox/pull/266).
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
- api_info, api_modify - add default values for fields ``ciphers`` in ``ip ssh``, ``mvrp`` in  ``interface vlan``, and ``mvrp-forbidden`` in ``interface bridge vlan`` (https://github.com/ansible-collections/community.routeros/pull/439/).
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
- sap_control_exec, sap_hostctrl_exec - QoL and Error handling (https://github.com/sap-linuxlab/community.sap_libs/pull/81)
- sap_control_exec, sap_hostctrl_exec - Refactor to use shared utilities (https://github.com/sap-linuxlab/community.sap_libs/pull/78)
- sap_hdbsql - Add error handling and secure flags for hdbsql (https://github.com/sap-linuxlab/community.sap_libs/pull/75)
- sap_hdbsql - Add new parameter named properties (https://github.com/sap-linuxlab/community.sap_libs/pull/79)
- sap_system_facts - Add SID and permission check to facts module (https://github.com/sap-linuxlab/community.sap_libs/pull/73)
- sapcar_extract - Add overwrite mode and improve exist validation (https://github.com/sap-linuxlab/community.sap_libs/pull/77)

fortinet.fortimanager
~~~~~~~~~~~~~~~~~~~~~

- Supported new environment variable "ANSIBLE_FORTIMANAGER_ENABLE_LOG" to enable/disable logging for FortiManager Ansible Collection.
- Supported new environment variable "ANSIBLE_FORTIMANAGER_VERSION_CHECK" to enable/disable version checking performed by the FortiManager Ansible Collection.
- Supported new schemas in FortiManager 7.0.16, 7.2.12, 7.4.9, 7.4.10, 7.6.5, 7.6.6

google.cloud
~~~~~~~~~~~~

- gcp_sql_instance - add `allocated_ip_range` to `settings.ip_configuration` for private IP Cloud SQL instances (name of the allocated IP range in the VPC) (https://github.com/ansible-collections/google.cloud/pull/744).
- gcp_vertexai_* - added 18 Vertex AI modules (gcp_vertexai_dataset, gcp_vertexai_deployment_resource_pool, gcp_vertexai_endpoint, gcp_vertexai_endpoint_with_model_garden_deployment, gcp_vertexai_feature_group, gcp_vertexai_feature_group_feature, gcp_vertexai_feature_online_store, gcp_vertexai_feature_online_store_featureview, gcp_vertexai_featurestore, gcp_vertexai_featurestore_entitytype, gcp_vertexai_featurestore_entitytype_feature, gcp_vertexai_index, gcp_vertexai_index_endpoint, gcp_vertexai_index_endpoint_deployed_index, gcp_vertexai_metadata_store, gcp_vertexai_rag_engine_config, gcp_vertexai_reasoning_engine, gcp_vertexai_tensorboard) (https://github.com/ansible-collections/google.cloud/pull/743).

hetzner.hcloud
~~~~~~~~~~~~~~

- primary_ip - Assign to new server if ``server`` is changed.
- primary_ip - Unassign primary_ip if ``server`` is null.

netapp.ontap
~~~~~~~~~~~~

- na_ontap_lun - updated documentation for unsupported REST parameters.
- na_ontap_nfs - new option `credential_cache` added in REST.
- na_ontap_snapmirror - new options `time_out`, `wait_for_completion` added in REST.
- na_ontap_snapmirror - updated documentation for `identity_preserve` and `max_transfer_rate`.
- na_ontap_volume_efficiency- AWS Lambda support added to the module.
- na_ontap_volume_efficiency- Added `wait_for_completion` and `time_out` parameters to fix time out errors for long running operations.

theforeman.foreman
~~~~~~~~~~~~~~~~~~

- content_view - add support for lifecycle environments in rolling content views
- convert2rhel role - removed subscription support as it's been unused since Katello 4.12 (05/2024)
- locations role - Added ``state`` parameter to manage resource presence.

vmware.vmware
~~~~~~~~~~~~~

- cluster_ha - Add value to allow disabling admission control policy Fixes https://github.com/ansible-collections/vmware.vmware/issues/227
- vm - Add the ability to set the annotation of a VM. Fixes https://github.com/ansible-collections/vmware.vmware/issues/310
- vm_list_group_by_clusters_info - Add the ability to use the absolute path for the group name. This can be used to avoid group name collisions. Fixes https://github.com/ansible-collections/vmware.vmware/issues/297
- vms - Add setting to disable population of ansible_host to the inventory Fixes https://github.com/ansible-collections/vmware.vmware/pull/317

vultr.cloud
~~~~~~~~~~~

- Added pagination support by adding ``api_results_per_page`` to the common attributes.
- bare_metal - Added support for multi-disk operation mode by adding ``mdisk_mode`` to the attributes (https://github.com/vultr/ansible-collection-vultr/issues/165).
- object_storage - Object storage subscriptions require specifying a tier upon creation, added ``tier`` to the attributes (https://github.com/vultr/ansible-collection-vultr/issues/135).
- snapshot - Added UEFI support adding ``uefi`` to the attributes (https://github.com/vultr/ansible-collection-vultr/pull/160).

Breaking Changes / Porting Guide
--------------------------------

community.mysql
~~~~~~~~~~~~~~~

- Update imports from ansible.module_utils.six to use their python3 equivalent. This change will make this collection incompatible for managed hosts on python2.7.

community.proxmox
~~~~~~~~~~~~~~~~~

- proxmox - set ``state`` as not ``optional`` and assign default value ``present`` (https://github.com/ansible-collections/community.proxmox/pull/292).

Deprecated Features
-------------------

community.general
~~~~~~~~~~~~~~~~~

- aix_devices - module is superseded by equivalent in ``ibm.power_aix`` collection. It will be removed from community.general 15.0.0 (https://github.com/ansible-collections/community.general/issues/11290, https://github.com/ansible-collections/community.general/pull/11540).
- aix_filesystem - module is superseded by equivalent in ``ibm.power_aix`` collection. It will be removed from community.general 15.0.0 (https://github.com/ansible-collections/community.general/issues/11290, https://github.com/ansible-collections/community.general/pull/11540).
- aix_inittab - module is superseded by equivalent in ``ibm.power_aix`` collection. It will be removed from community.general 15.0.0 (https://github.com/ansible-collections/community.general/issues/11290, https://github.com/ansible-collections/community.general/pull/11540).
- aix_lvg - module is superseded by equivalent in ``ibm.power_aix`` collection. It will be removed from community.general 15.0.0 (https://github.com/ansible-collections/community.general/issues/11290, https://github.com/ansible-collections/community.general/pull/11540).
- aix_lvol - module is superseded by equivalent in ``ibm.power_aix`` collection. It will be removed from community.general 15.0.0 (https://github.com/ansible-collections/community.general/issues/11290, https://github.com/ansible-collections/community.general/pull/11540).
- monit - support for Monit version 5.18 or older is deprecated and will be removed in community.general 14.0.0 (https://github.com/ansible-collections/community.general/pull/11254).
- puppet - the ``timeout`` parameter is deprecated and will be removed in community.general 14.0.0. (https://github.com/ansible-collections/community.general/pull/11658).

community.proxmox
~~~~~~~~~~~~~~~~~

- proxmox - Certificate verification default changes from ``false`` to ``true`` with version 2.0.0 (https://github.com/ansible-collections/community.proxmox/pull/256).

Security Fixes
--------------

amazon.aws
~~~~~~~~~~

- arn - fix potential ReDoS vulnerability in ARN parsing regex by using negated character class instead of non-greedy quantifier (https://github.com/ansible-collections/amazon.aws/pull/2884).
- ec2_security_group - fix potential ReDoS vulnerability in security group ID parsing regex by using negated character classes and adding end anchor (https://github.com/ansible-collections/amazon.aws/pull/2884).

ansible.windows
~~~~~~~~~~~~~~~

- win_dns_record - Fixed a security risk where ``AllowUpdateAny`` was hardcoded for non-SRV records, allowing any authenticated user to update DNS records. Added a new parameter ``allow_update_any`` which defaults to ``false`` (https://issues.redhat.com/browse/ACA-5193).

Bugfixes
--------

Ansible-core
~~~~~~~~~~~~

- Fix up ``powershell`` shell commands when using a connection plugin that does not support stdin/pipeline input - https://github.com/ansible/ansible/issues/86397
- ansible-connection - Prevent unpickling failures in module contexts by ensuring that AnsibleTaggedObjects in pickled responses are converted to plain types in ``JsonRpcServer``.
- config lookup now uses preexisting constants for templating when needed.
- rpm_key - Use librpm library API instead of gpg utility to support version 6 PGP keys (https://github.com/ansible/ansible/issues/86157).
- yaml loading - Fix traceback when parsing YAML strings (not files) when using the pure Python implementation of PyYAML.

amazon.aws
~~~~~~~~~~

- aws_ssm - Fixed connection being re-established on every loop iteration. The plugin now properly establishes a single connection for a loop (https://github.com/ansible-collections/amazon.aws/pull/2869).
- elb_application_lb - fixed comparison of multi-rule default actions to properly handle the ``Order`` field when determining if listener modifications are needed (https://github.com/ansible-collections/amazon.aws/issues/2537).
- elb_application_lb - fixed error where creating a new application load balancer with listener rules would fail with ``Parameter validation failed: Invalid type for parameter ListenerArn, value: None`` (https://github.com/ansible-collections/amazon.aws/issues/2400).
- s3_object - fixed error when using PUT with an empty ``content`` string (https://github.com/ansible-collections/amazon.aws/pull/2810)

ansible.windows
~~~~~~~~~~~~~~~

- Stop using the deprecated text module_utils in Ansible that will be removed in Ansible ``2.24``.
- win_dhcp_lease - when creating a reservation, the dns_name will be used as reservation_name in case that is not provided; will be discarded otherwise as the parameter HostName is not supported by Add-DhcpServerv4Reservation (https://github.com/ansible-collections/ansible.windows/issues/813)
- win_file - Fix idempotency issues when using ``state: touch`` (https://github.com/ansible-collections/ansible.windows/issues/798)
- win_hotfix - Fix a bug in Get-HotfixMetadataFromKB fallback logic where it would fail to return metadata even if the hotfix was found.
- win_hotfix - Fix idempotency issue where some multi-package MSUs (e.g. SSU + CU) were incorrectly reported as installed by DISM even if the CU was missing. Added a secondary check using Get-Hotfix to verify installation.
- win_products_facts - return string for all the license related facts (https://github.com/ansible-collections/community.windows/issues/661).
- win_reboot - fix unhandled error when ``.exe`` not present in ``PATHEXT`` environment variable
- win_shell - Ensure the default ``executable`` uses the absolute path to ``powershell.exe`` rather than looking it up in the ``PATH`` environment.

cisco.meraki
~~~~~~~~~~~~

- Fixing problem of naming in organizations_appliance_vpn_third_party_vpnpeers_info.
- Restructuring README.md file.

community.dns
~~~~~~~~~~~~~

- Update Public Suffix List.
- hetzner_* modules and hetzner_dns_records inventory plugin - retry on network problems and certain HTTP codes (502, 503, 504) (https://github.com/ansible-collections/community.dns/pull/313).
- hetzner_dns_record_sets - when doing batch updates, do not request status updates for too many actions at once (https://github.com/ansible-collections/community.dns/issues/312, https://github.com/ansible-collections/community.dns/pull/313).
- hosttech_* modules and hosttech_dns_records inventory plugin - when using the JSON API, retry on network problems and certain HTTP codes (502, 503, 504) (https://github.com/ansible-collections/community.dns/pull/313).

community.general
~~~~~~~~~~~~~~~~~

- counter_enabled callback plugin - fix plugin not observing ``display_ok_hosts`` option (https://github.com/ansible-collections/community.general/issues/3978, https://github.com/ansible-collections/community.general/pull/11656).
- ipa_dnsrecord - fix idempotency bug when using ``dnsttl`` due to wrong Python types (https://github.com/ansible-collections/community.general/pull/11559).
- keycloak_authentication - fix ``TypeError`` crash when a flow is defined without ``authenticationExecutions`` (https://github.com/ansible-collections/community.general/issues/11547, https://github.com/ansible-collections/community.general/pull/11548).
- nictagadm - add a condition to the if statement so that ``is_valid_mac()`` does not get called if ``etherstub`` is false (https://github.com/ansible-collections/community.general/pull/11589).
- nmcli - add missing ``ipv6.routing-rules`` to ``settings_type()`` list type, preventing ``routing_rules6`` list from being corrupted (https://github.com/ansible-collections/community.general/issues/11630, https://github.com/ansible-collections/community.general/pull/11635).
- open_iscsi - fix IPv6 portal address formatting; iscsiadm requires bracket notation for IPv6 addresses but the module was producing an incorrect format (https://github.com/ansible-collections/community.general/issues/4467, https://github.com/ansible-collections/community.general/pull/11657).
- xfconf - representation of boolean properties was not consistent between Python and ``xfconf-query``, leading to broken idempotency (https://github.com/ansible-collections/community.general/pull/11645).

community.hrobot
~~~~~~~~~~~~~~~~

- Remove unnecessary Python 2 compatibilty code (https://github.com/ansible-collections/community.hrobot/pull/187).

community.mysql
~~~~~~~~~~~~~~~

- mysql_user - When creating a new user, and specifying parsec as plugin it wil generate the wrong SQL query. It should be added to the same plugin check as ed25519 so that it generates a query using USING PASSWORDS(%s) instead of BY %s (https://github.com/ansible-collections/community.mysql/pull/779).

community.proxmox
~~~~~~~~~~~~~~~~~

- proxmox_cluster - make cluster join idempotent (https://github.com/ansible-collections/community.proxmox/pull/244).
- proxmox_disk - make none iso disk idempotent (https://github.com/ansible-collections/community.proxmox/pull/288).
- proxmox_firewall - Enable ipsets on vm level and fix bugs regarding the cidr notation the proxmox api expects (https://github.com/ansible-collections/community.proxmox/pull/248).
- proxmox_role - when privs is omitted, keep existing role privileges unchanged instead of treating it as no privileges (https://github.com/ansible-collections/community.proxmox/pull/284).

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

fortinet.fortios
~~~~~~~~~~~~~~~~

- Fixed an issue where users were required to specify a password confirmation when using the system_admin and system_api_user modules in FortiOS 7.6.5 and later.
- Fixed the issue that getting an error "BadGzipFile" when using token for authentication in new versions of FortiOS.

netapp.ontap
~~~~~~~~~~~~

- na_ontap_export_policy_rule - Fixed issue where rule_index was not being applied to create body, and added logic to detect when a create action is actually a re-index of an existing rule.
- na_ontap_lun - Updated module with alias `volume_name` for `flexvol_name`.
- na_ontap_qtree - Updated module with alias `volume_name` for `flexvol_name`.
- na_ontap_service_processor_network - fixed issue with interface state not being applied correctly, resolved ipv6 comparison issue and idempotency issue with ZAPI abd REST.
- na_ontap_snapmirror_policy - updated examples for creating and modifying snapmirror policy.
- na_ontap_user_role - Removed special handling of `DEFAULT` path and normalized empty query in privileges to None for consistency.
- na_ontap_volume - Fixed issue with volume rename.
- na_ontap_vserver_audit - updated documentation for `log`.

theforeman.foreman
~~~~~~~~~~~~~~~~~~

- content_view_filter_rule - fix content_filter_rule_deb_spec to take into account desired versions

vmware.vmware
~~~~~~~~~~~~~

- cluster_info - When a user does not specify a cluster name, the module will now search recursively for clusters in the datacenter. Fixes https://github.com/ansible-collections/vmware.vmware/issues/303
- cluster_info - When a user specifies a datacenter name, the module will now fail if that datacenter is not found instead of silently continuing. Fixes https://github.com/ansible-collections/vmware.vmware/issues/303
- inventory plugins - fix handling of encrypted strings in inventory plugin username and password options for ansible-core<=2.19 fixes https://github.com/ansible-collections/vmware.vmware/issues/304

vultr.cloud
~~~~~~~~~~~

- dns_domain - Removed requirement for the ``ip`` argument when creating a new domain (https://github.com/vultr/ansible-collection-vultr/issues/140).
- instance, bare_metal - Fixed an issue where the ``user_data`` response returned a JSON serialization error (https://github.com/vultr/ansible-collection-vultr/issues/156).
- startup_script - Fixed an issue where the ``script`` response returned a JSON serialization error (https://github.com/vultr/ansible-collection-vultr/pull/162).

Known Issues
------------

community.routeros
~~~~~~~~~~~~~~~~~~

- api_modify - to create or modify entries in the ``container`` path, you need librouteros 4.0.0 or newer due to a bug preventing older versions from setting or modifying properties named ``cmd`` (https://github.com/ansible-collections/community.routeros/issues/442).

New Modules
-----------

ansible.windows
~~~~~~~~~~~~~~~

- ansible.windows.dsc3 - Sets or checks DSC v3 configuration state

cisco.mso
~~~~~~~~~

- cisco.mso.ndo_endpoint_ip_tag_policy - Manage Endpoint IP Tag Policies on Cisco Nexus Dashboard Orchestrator (NDO).
- cisco.mso.ndo_endpoint_mac_tag_policy - Manage Endpoint MAC Tag Policies on Cisco Nexus Dashboard Orchestrator (NDO).
- cisco.mso.ndo_template_deploy - Deploy templates to sites on Cisco Nexus Dashboard Orchestrator (NDO).
- cisco.mso.ndo_tenant_netflow_record - Manage NetFlow Record on Cisco Nexus Dashboard Orchestrator (NDO).

community.general
~~~~~~~~~~~~~~~~~

- community.general.github_secrets - Manage GitHub repository or organization secrets.
- community.general.github_secrets_info - List GitHub repository or organization secrets.
- community.general.keycloak_authentication_v2 - Configure authentication flows in Keycloak in an idempotent and safe manner.
- community.general.logrotate - Manage logrotate configurations.

community.proxmox
~~~~~~~~~~~~~~~~~

- community.proxmox.proxmox_role - Role management for Proxmox VE cluster.

fortinet.fortimanager
~~~~~~~~~~~~~~~~~~~~~

- fortinet.fortimanager.fmgr_devprof_system_template_interface - System template system template interface
- fortinet.fortimanager.fmgr_devprof_system_template_interface_iprange - System template system template interface ip range
- fortinet.fortimanager.fmgr_fmg_script - Fmg script
- fortinet.fortimanager.fmgr_fmg_script_schedule - Fmg script schedule
- fortinet.fortimanager.fmgr_securityconsole_template_validate - Securityconsole template validate
- fortinet.fortimanager.fmgr_system_locallog_tacacsaccounting_filter - Cli system locallog tacacs+accounting filter
- fortinet.fortimanager.fmgr_system_locallog_tacacsaccounting_setting - Cli system locallog tacacs+accounting setting
- fortinet.fortimanager.fmgr_system_log_apiratelimit - Cli system log api ratelimit
- fortinet.fortimanager.fmgr_system_log_settings_clientcertauth - Cli system log settings client cert auth

netapp.ontap
~~~~~~~~~~~~

- netapp.ontap.na_ontap_autoupdate_config - NetApp ONTAP module to manage configurations for automatic updates.
- netapp.ontap.na_ontap_cg - NetApp ONTAP module to manage operations related to consistency groups.

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

- ansible.netcommon (still version 8.4.0)
- ansible.posix (still version 2.1.0)
- ansible.utils (still version 6.0.1)
- arista.eos (still version 12.0.1)
- awx.awx (still version 24.6.1)
- chocolatey.chocolatey (still version 1.5.3)
- cisco.aci (still version 2.13.0)
- cisco.dnac (still version 6.48.0)
- cisco.ios (still version 11.3.0)
- cisco.iosxr (still version 12.1.1)
- cisco.nxos (still version 11.1.3)
- cisco.ucs (still version 1.16.0)
- cloudscale_ch.cloud (still version 2.5.3)
- community.aws (still version 10.1.0)
- community.ciscosmb (still version 1.0.11)
- community.crypto (still version 3.1.1)
- community.grafana (still version 2.3.0)
- community.hashi_vault (still version 7.1.0)
- community.library_inventory_filtering_v1 (still version 1.1.5)
- community.libvirt (still version 2.1.0)
- community.mongodb (still version 1.7.12)
- community.okd (still version 5.0.0)
- community.postgresql (still version 4.2.0)
- community.proxysql (still version 1.7.0)
- community.rabbitmq (still version 1.6.0)
- community.sops (still version 2.2.7)
- community.vmware (still version 6.2.0)
- community.windows (still version 3.1.0)
- community.zabbix (still version 4.1.1)
- containers.podman (still version 1.19.0)
- cyberark.conjur (still version 1.3.9)
- dellemc.enterprise_sonic (still version 3.2.0)
- dellemc.openmanage (still version 10.0.1)
- dellemc.powerflex (still version 3.0.0)
- dellemc.unity (still version 2.1.0)
- f5networks.f5_modules (still version 1.39.0)
- grafana.grafana (still version 6.0.6)
- hitachivantara.vspone_block (still version 4.6.1)
- hitachivantara.vspone_object (still version 1.1.1)
- ibm.storage_virtualize (still version 3.2.0)
- ieisystem.inmanage (still version 4.0.0)
- infinidat.infinibox (still version 1.6.3)
- infoblox.nios_modules (still version 1.9.0)
- inspur.ispim (still version 2.2.4)
- junipernetworks.junos (still version 11.0.0)
- kaytus.ksmanage (still version 2.0.0)
- kubernetes.core (still version 6.3.0)
- lowlydba.sqlserver (still version 2.7.0)
- microsoft.ad (still version 1.10.0)
- microsoft.iis (still version 1.1.0)
- netapp.cloudmanager (still version 21.24.0)
- netapp.storagegrid (still version 21.16.0)
- netapp_eseries.santricity (still version 1.4.1)
- netbox.netbox (still version 3.22.0)
- ngine_io.cloudstack (still version 3.0.0)
- openstack.cloud (still version 2.5.0)
- ovirt.ovirt (still version 3.2.2)
- pcg.alpaca_operator (still version 2.2.0)
- purestorage.flasharray (still version 1.42.0)
- purestorage.flashblade (still version 1.24.0)
- ravendb.ravendb (still version 1.0.4)
- splunk.es (still version 4.0.0)
- telekom_mms.icinga_director (still version 2.5.1)
- vmware.vmware_rest (still version 4.10.0)
- vyos.vyos (still version 6.0.0)

v13.4.0
=======

.. contents::
  :local:
  :depth: 2

Release Summary
---------------

Release Date: 2026-02-24

`Porting Guide <https://docs.ansible.com/projects/ansible/devel/porting_guides.html>`_

Ansible-core
------------

Ansible 13.4.0 contains ansible-core version 2.20.3.
This is a newer version than version 2.20.2 contained in the previous Ansible release.

The changes are reported in the combined changelog below.

Changed Collections
-------------------

If not mentioned explicitly, the changes are reported in the combined changelog below.

+-----------------------------+----------------+----------------+----------------------------------------------------------+
| Collection                  | Ansible 13.3.0 | Ansible 13.4.0 | Notes                                                    |
+=============================+================+================+==========================================================+
| ansible.netcommon           | 8.2.1          | 8.4.0          |                                                          |
+-----------------------------+----------------+----------------+----------------------------------------------------------+
| arista.eos                  | 12.0.0         | 12.0.1         |                                                          |
+-----------------------------+----------------+----------------+----------------------------------------------------------+
| cisco.dnac                  | 6.44.0         | 6.48.0         |                                                          |
+-----------------------------+----------------+----------------+----------------------------------------------------------+
| cisco.ios                   | 11.2.0         | 11.3.0         |                                                          |
+-----------------------------+----------------+----------------+----------------------------------------------------------+
| cisco.meraki                | 2.22.0         | 2.22.1         |                                                          |
+-----------------------------+----------------+----------------+----------------------------------------------------------+
| community.aws               | 10.0.0         | 10.1.0         |                                                          |
+-----------------------------+----------------+----------------+----------------------------------------------------------+
| community.crypto            | 3.1.0          | 3.1.1          |                                                          |
+-----------------------------+----------------+----------------+----------------------------------------------------------+
| community.dns               | 3.5.1          | 3.5.2          |                                                          |
+-----------------------------+----------------+----------------+----------------------------------------------------------+
| community.docker            | 5.0.5          | 5.0.6          |                                                          |
+-----------------------------+----------------+----------------+----------------------------------------------------------+
| community.general           | 12.3.0         | 12.4.0         |                                                          |
+-----------------------------+----------------+----------------+----------------------------------------------------------+
| community.libvirt           | 2.0.0          | 2.1.0          |                                                          |
+-----------------------------+----------------+----------------+----------------------------------------------------------+
| community.mongodb           | 1.7.11         | 1.7.12         | There are no changes recorded in the changelog.          |
+-----------------------------+----------------+----------------+----------------------------------------------------------+
| community.mysql             | 4.0.1          | 4.1.0          |                                                          |
+-----------------------------+----------------+----------------+----------------------------------------------------------+
| containers.podman           | 1.18.1         | 1.19.0         |                                                          |
+-----------------------------+----------------+----------------+----------------------------------------------------------+
| hitachivantara.vspone_block | 4.5.1          | 4.6.1          |                                                          |
+-----------------------------+----------------+----------------+----------------------------------------------------------+
| kubernetes.core             | 6.2.0          | 6.3.0          |                                                          |
+-----------------------------+----------------+----------------+----------------------------------------------------------+
| pcg.alpaca_operator         | 2.1.1          | 2.2.0          | The collection did not have a changelog in this version. |
+-----------------------------+----------------+----------------+----------------------------------------------------------+
| purestorage.flasharray      | 1.41.0         | 1.42.0         |                                                          |
+-----------------------------+----------------+----------------+----------------------------------------------------------+
| vmware.vmware_rest          | 4.9.0          | 4.10.0         |                                                          |
+-----------------------------+----------------+----------------+----------------------------------------------------------+

Major Changes
-------------

containers.podman
~~~~~~~~~~~~~~~~~

- Add podman Quadlet modules

Minor Changes
-------------

Ansible-core
~~~~~~~~~~~~

- ansible-test - Update URL used to download FreeBSD wheels for managed remotes.
- ansible-test - Use the new API endpoint for the Ansible Core CI service.

ansible.netcommon
~~~~~~~~~~~~~~~~~

- Option to use libssh as transport while using netconf, is added.
- The ssh-python module is needed, which will ensure libssh as transport for netconf operations. When use_libssh is enabled.

cisco.dnac
~~~~~~~~~~

- Added '802_11_be_profiles'  attribute in wireless_design_workflow_manager module
- Added build_ignore configuration to optimize Ansible Galaxy collection packaging.
- Changes in accesspoint_workflow_manager module
- Changes in device_configs_backup_workflow_manager module
- Changes in inventory_workflow_manager module
- Changes in lan_automation_workflow_manager module
- Changes in network_profile_wireless_workflow_manager module
- Changes in pnp_workflow_manager module
- Changes in provision_workflow_manager module
- Changes in sda_fabric_devices_workflow_manager module
- Changes in sda_host_port_onboarding_workflow_manager module
- Changes in swim_workflow_manager module
- Changes in template_workflow_manager module
- Changes in wireless_design_workflow_manager module
- Code formatting and ansible-lint compliance updates for Red Hat standards
- Standardized README format and content to match Catalyst Center Ansible collection documentation practices.
- access_groups - new module to manage access groups
- access_groups_count_info - new module to retrieve access groups count
- access_groups_info - new module to retrieve access groups information
- cisco.dnac collection - New service system_software_upgrade added for Catalyst Center 3.1.6.0
- cisco.dnac collection - SDK updated to dnacentersdk 2.11.0 with support for Cisco Catalyst Center 3.1.6.0
- client_enrichment_details_v2_info - new module to retrieve client enrichment details (v2)
- compliance_network_devices_detail_policys_info - new module to retrieve compliance policies for network devices
- compliance_network_devices_detail_policys_violations_info - new module to retrieve compliance policy violations for network devices
- compliance_policys - new module to manage compliance policies
- compliance_policys_count_info - new module to retrieve compliance policies count
- compliance_policys_info - new module to retrieve compliance policies information
- compliance_policys_rules - new module to manage compliance policy rules
- compliance_policys_rules_conditions - new module to manage compliance policy rule conditions
- compliance_policys_rules_conditions_count_info - new module to retrieve compliance policy rule conditions count
- compliance_policys_rules_conditions_info - new module to retrieve compliance policy rule conditions information
- compliance_policys_rules_count_info - new module to retrieve compliance policy rules count
- compliance_policys_rules_info - new module to retrieve compliance policy rules information
- compliance_policys_rules_variables - new module to manage compliance policy rule variables
- compliance_policys_rules_variables_count_info - new module to retrieve compliance policy rule variables count
- compliance_policys_rules_variables_info - new module to retrieve compliance policy rule variables information
- compliance_policys_site_assignments - new module to manage compliance policy site assignments
- compliance_policys_site_assignments_info - new module to retrieve compliance policy site assignments information
- compliance_policys_sites_rules_variables - new module to manage compliance policy site rule variables
- compliance_policys_sites_rules_variables_info - new module to retrieve compliance policy site rule variables information
- device_enrichment_details_v2_info - new module to retrieve device enrichment details (v2)
- discoverys - new module to manage device discoveries
- discoverys_count_info - new module to retrieve device discoveries count
- discoverys_info - new module to retrieve device discoveries information
- discoverys_jobs - new module to manage discovery jobs
- discoverys_jobs_count_info - new module to retrieve discovery jobs count
- discoverys_jobs_discovered_network_devices_count_info - new module to retrieve discovered network devices count
- discoverys_jobs_discovered_network_devices_info - new module to retrieve discovered network devices from discovery jobs
- discoverys_jobs_info - new module to retrieve discovery jobs information
- discoverys_jobs_stop_create - new module to stop discovery jobs
- discoverys_jobs_summarys_info - new module to retrieve discovery jobs summaries
- download_software_release_create - new module to download software releases
- download_software_release_delete - new module to delete software release downloads
- download_software_release_update - new module to update software release downloads
- filter_group_aassociations_delete - new module to delete filter group associations
- filter_group_associations - new module to manage filter group associations
- filter_group_associations_info - new module to retrieve filter group associations information
- filter_groups - new module to manage filter groups
- filter_groups_info - new module to retrieve filter groups information
- global_credentials - new module to manage global credentials
- global_credentials_count_info - new module to retrieve global credentials count
- global_credentials_info - new module to retrieve global credentials information
- images_delete - new module to delete software images
- install_optional_packages_create - new module to install optional packages
- installed_release_info - new module to retrieve installed release information
- iot_fabric_rep_rings_delete - new module to delete IoT fabric REP rings
- iot_non_fabric_rep_rings_delete - new module to delete IoT non-fabric REP rings
- issue_enrichment_details_info - new module to retrieve issue enrichment details
- network_devices_create - new module to create network devices
- network_devices_export_credentials_create - new module to export network device credentials
- network_devices_update - new module to update network devices
- network_devices_update_create - new module to trigger network device updates
- network_devices_validate_device_create - new module to validate network devices
- product_series_count_info - new module to retrieve product series count
- releases_info - new module to retrieve available releases information
- releases_release_summary_info - new module to retrieve release summary
- roles_permissions_info - new module to retrieve roles permissions
- roles_v2 - new module to manage roles (v2)
- roles_v2_info - new module to retrieve roles information (v2)
- sda_layer3_virtual_networks_delete - new module to delete SDA layer 3 virtual networks
- sda_transit_networks_delete - new module to delete SDA transit networks
- site_delete - new module to delete sites
- site_update - new module to update sites
- software_management_executions_info - new module to retrieve software management execution details
- uninstall_optional_packages_create - new module to uninstall optional packages
- upgrade_software_release_create - new module to upgrade software releases
- user_enrichment_details_v2_info - new module to retrieve user enrichment details (v2)
- wireless_controllers_certificate_renewal_create - new module to trigger wireless controller certificate renewal
- wireless_controllers_site_tags_info - new module to retrieve wireless controller site tags
- wireless_profiles_policy_tags_info - new module to retrieve wireless profile policy tags
- wireless_settings_certificate_renewal_profiles - new module to manage wireless certificate renewal profiles
- wireless_settings_certificate_renewal_profiles_count_info - new module to retrieve wireless certificate renewal profiles count
- wireless_settings_certificate_renewal_profiles_info - new module to retrieve wireless certificate renewal profiles information

cisco.ios
~~~~~~~~~

- Adds a new Resource Module `ios_bfd_interfaces` to configure BFD on interfaces.
- Adds a new Resource Module `ios_bfd_templates` to configure BFD  using templates.
- ios_l3_interfaces - Add support for 'redirects' and 'unreachables' attributes to configure ICMP redirect and unreachable messages.

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

community.general
~~~~~~~~~~~~~~~~~

- ModuleHelper module utils - allow to ignore specific exceptions in ``module_fails_on_exception`` decorator (https://github.com/ansible-collections/community.general/pull/11488).
- from_ini filter plugin - add ``delimiters`` parameter to allow correctly parsing more INI documents (https://github.com/ansible-collections/community.general/issues/11506, https://github.com/ansible-collections/community.general/pull/11512).
- keycloak_client - add ``valid_post_logout_redirect_uris`` option to configure post logout redirect URIs for a client, and ``backchannel_logout_url`` option to configure the backchannel logout URL for a client (https://github.com/ansible-collections/community.general/issues/6812, https://github.com/ansible-collections/community.general/issues/4892, https://github.com/ansible-collections/community.general/pull/11473).
- keycloak_client_rolemapping, keycloak_realm_rolemapping, keycloak_group - optimize retrieval of groups by name to use Keycloak search API with exact matching instead of fetching all groups (https://github.com/ansible-collections/community.general/pull/11503).
- keycloak_realm - add support for ``localizationTexts`` option in Keycloak realms (https://github.com/ansible-collections/community.general/pull/11513).
- keycloak_realm_key - add support for auto-generated key providers (``rsa-generated``, ``rsa-enc-generated``, ``hmac-generated``, ``aes-generated``, ``ecdsa-generated``, ``ecdh-generated``, ``eddsa-generated``), ``java-keystore`` provider, additional algorithms (HMAC, ECDSA, ECDH, EdDSA, AES), and new config options (``secret_size``, ``key_size``, ``elliptic_curve``, ``keystore``, ``keystore_password``, ``key_alias``, ``key_password``). Also makes ``config.private_key`` and ``config.certificate`` optional as they are only required for imported key providers (https://github.com/ansible-collections/community.general/pull/11468).
- redfish_info - add Redfish Root data to results of successful ``CheckAvailability`` command (https://github.com/ansible-collections/community.general/pull/11504).
- seport - adds support for DCCP and SCTP protocols (https://github.com/ansible-collections/community.general/pull/11486).

community.libvirt
~~~~~~~~~~~~~~~~~

- virt_install - added support for memoryBacking source type configuration, including memfd for shared memory (https://github.com/ansible-collections/community.libvirt/issues/228).
- virt_install - added support for primary value attribute (_value or value) in dynamic dict options that require a primary value alongside additional attributes.
- virt_install - enhanced cloud_init configuration handling for sub-options (meta-data, user-data, and network-config) to support both string and dictionary inputs.
- virt_install - refactored common virt-install functionality into module_utils and doc_fragments to enable code reuse between modules.
- virt_volume - New return key/value pairs 'Type', 'Capacity' and 'Allocation' were added to command 'list_volumes' (https://github.com/ansible-collections/community.libvirt/issues/187)
- virt_volume - added ability to resize volumes if defined capacity is different. If volume already exists and defined capacity in XML differs a resize is attempted.

community.mysql
~~~~~~~~~~~~~~~

- mysql_role - add ``sql_log_bin`` option to disable binary logging for the connection (https://github.com/ansible-collections/community.mysql/issues/742).

containers.podman
~~~~~~~~~~~~~~~~~

- Fix tests for new Podman

hitachivantara.vspone_block
~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Added "playbooks/vsp_direct/vsp_storage_connection_session_example.yml" as a sample playbook demonstrating session-based storage operations.
- Added a new "hv_pav_alias" module to manage PAV (Parallel Access Volume) alias assignments for Mainframe based VSP block storage systems.
- Added a new "hv_pav_alias_facts" module to gather facts about PAV aliases from Mainframe based VSP block storage systems.
- Added a new "hv_sds_block_audit_log_setting" module to support configuration of audit log settings on VSP One SDS Block and Cloud systems.
- Added a new "hv_sds_block_audit_log_setting_facts" module to retrieve audit log setting from VSP One SDS Block and Cloud systems.
- Added a new "hv_sds_block_dump_log_file" module to retrieve and dump log information from VSP One SDS Block and Cloud systems.
- Added a new "hv_sds_block_dump_log_status_facts" module to retrieve and dump log status information from VSP One SDS Block and Cloud systems.
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
- Added a new "hv_sds_block_storage_external_auth_server_setting" module to configure external authentication server settings on VSP One SDS Block and Cloud systems.
- Added a new "hv_sds_block_storage_external_auth_server_setting_facts" module to retrieve external authentication server settings from the VSP One SDS Block and Cloud systems.
- Added a new "hv_sds_block_storage_user_auth_setting" module to configure external authentication server settings on VSP One SDS Block and Cloud systems.
- Added a new "hv_sds_block_storage_user_auth_setting_facts" module to retrieve user authentication settings from VSP One SDS Block and Cloud systems.
- Added a new "hv_session" module to generate and discard session on VSP block storage systems.
- Added a new "hv_session_facts" module to retrieve information about sessions on VSP block storage systems.
- Added a new "hv_snapshot_family_facts" module to retrieve information about snapshot family of the provided LDEV ID from VSP block storage systems.
- Added a new "hv_supported_host_mode_facts" module to retrieve detailed information about supported host mode options available in a given VSP block storage system.
- Added a new "hv_vclone_parent_volume_facts" module to retrieve information about virtual clone parent volume from VSP block storage systems.
- Added notes to module documentation indicating that a few modules are not supported for BHE and higher models.
- Added support for Mainframe z16.
- Added support for SVOS 10.5.1.
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

kubernetes.core
~~~~~~~~~~~~~~~

- Remove deprecated import from ``ansible.module_utils._text`` (https://github.com/ansible-collections/kubernetes.core/pull/1053).
- helm - add ``release_values`` key to ``status`` return value that can be accessed using Jinja2 dot notation (https://github.com/ansible-collections/kubernetes.core/pull/1056).
- helm_info - add ``release_values`` key to ``status`` return value that can be accessed using Jinja2 dot notation (https://github.com/ansible-collections/kubernetes.core/pull/1056).

vmware.vmware_rest
~~~~~~~~~~~~~~~~~~

- Disable check mode for all non-info modules in this collection. Check mode was never supported for these modules. Fixes https://github.com/ansible-collections/vmware.vmware_rest/issues/363

Deprecated Features
-------------------

- The awx.awx collection will be removed from Ansible 14.
  The collection is undergoing a heavy \ `refactoring <https://forum.ansible.com/t/7404>`__ and currently does not align with the standards for the community package.
  See `the removal discussion for details <https://forum.ansible.com/t/44706>`__.
  After removal, users can still install this collection with ``ansible-galaxy collection install awx.awx``.

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

kubernetes.core
~~~~~~~~~~~~~~~

- helm - the ``status.values`` return value has been deprecated and will be removed in a release after 2027-01-08. Use ``status.release_values`` instead (https://github.com/ansible-collections/kubernetes.core/pull/1056).
- helm_info - the ``status.values`` return value has been deprecated and will be removed in a release after 2027-01-08. Use ``status.release_values`` instead (https://github.com/ansible-collections/kubernetes.core/pull/1056).

vmware.vmware_rest
~~~~~~~~~~~~~~~~~~

- Deprecate modules that have been moved to the new vmware.vmware collection. Includes vcenter_vm_guest_customization, vcenter_vm_hardware_adapter_sata, vcenter_vm_hardware_adapter_scsi, vcenter_vm_hardware_cdrom, vcenter_vm_hardware_cpu, vcenter_vm_hardware_disk, vcenter_vm_hardware_ethernet, vcenter_vm_hardware_memory, vcenter_vm

Security Fixes
--------------

kubernetes.core
~~~~~~~~~~~~~~~

- Selectively redact sensitive info from kubeconfig instead of applying blanket ``no_log=True`` (https://github.com/ansible-collections/kubernetes.core/pull/1014).

Bugfixes
--------

Ansible-core
~~~~~~~~~~~~

- Fix interpreter discovery on delegated ``async`` tasks (https://github.com/ansible/ansible/issues/86491)
- Fix up the Action plugin ``_make_tmp_path`` error to only include the command run rather than the shell's dataclass repr from ``mkdtemp``.
- local connection - Pass correct type to become plugins when checking password (https://github.com/ansible/ansible/issues/86458)

arista.eos
~~~~~~~~~~

- Fix eos_vrf module to properly check existing interface configuration before making changes (https://github.com/ansible-collections/arista.eos/issues/546)

cisco.ios
~~~~~~~~~

- Fixed delete and purged state function for ios_bfd_templates

cisco.meraki
~~~~~~~~~~~~

- Fix parameter naming in organizations_inventory_claim.py to use camelCase for consistency with existing code.

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

community.docker
~~~~~~~~~~~~~~~~

- docker_image_pull, docker_container - fix pulled image change detection for Docker 29.2+ (https://github.com/ansible-collections/community.docker/pull/1242).

community.general
~~~~~~~~~~~~~~~~~

- keycloak module utils - fix ``TypeError`` crash when managing users whose username or email contains special characters such as ``+`` (https://github.com/ansible-collections/community.general/issues/10305, https://github.com/ansible-collections/community.general/pull/11472).
- keycloak module utils - use proper URL encoding (``urllib.parse.quote``) for query parameters in authorization permission name searches, replacing fragile manual space replacement (https://github.com/ansible-collections/community.general/pull/11472).
- keycloak_client - fix idempotency bug caused by ``null`` flow overrides value differences for non-existing flow overrides (https://github.com/ansible-collections/community.general/issues/11430, https://github.com/ansible-collections/community.general/pull/11455).
- keycloak_client - remove IDs as change from diff result for protocol mappers (https://github.com/ansible-collections/community.general/issues/11453, https://github.com/ansible-collections/community.general/pull/11454).
- keycloak_realm_key - fix ``KeyError`` crash when managing realm keys where Keycloak does not return ``active``, ``enabled``, or ``algorithm`` fields in the config response (https://github.com/ansible-collections/community.general/issues/11459, https://github.com/ansible-collections/community.general/pull/11470).
- keycloak_user_federation - mapper config item can be an array (https://github.com/ansible-collections/community.general/issues/11502, https://github.com/ansible-collections/community.general/pull/11515).
- keycloak_user_rolemapping - fix ``TypeError`` crash when adding a client role to a user who has no existing roles for that client (https://github.com/ansible-collections/community.general/issues/10960, https://github.com/ansible-collections/community.general/pull/11471).
- maven_artifact - fix SNAPSHOT version resolution to pick the newest matching ``<snapshotVersion>`` entry by ``<updated>`` timestamp instead of the first. Repositories like GitHub Packages keep all historical entries in ``<snapshotVersions>`` (oldest first), causing the module to resolve to the oldest snapshot instead of the latest (https://github.com/ansible-collections/community.general/issues/5117, https://github.com/ansible-collections/community.general/issues/11489, https://github.com/ansible-collections/community.general/pull/11501).
- nsupdate - fix ``AttributeError`` when using the module without TSIG authentication (https://github.com/ansible-collections/community.general/issues/11460, https://github.com/ansible-collections/community.general/pull/11461).
- python_requirements_info - use ``importlib.metadata`` if ``pkg_resources`` from ``setuptools`` cannot be imported. That module has been removed from setuptools 82.0.0 (https://github.com/ansible-collections/community.general/issues/11491, https://github.com/ansible-collections/community.general/pull/11492).
- splunk callback plugin - replace deprecated callback function (https://github.com/ansible-collections/community.general/pull/11485).

community.libvirt
~~~~~~~~~~~~~~~~~

- virt_install - fixed cloud_init configuration handling for meta-data, user-data, and network-config.
- virt_install - fixed the dict-based options handling for events, resource, and sysinfo options.

containers.podman
~~~~~~~~~~~~~~~~~

- Fix Ansible warning about test utils

kubernetes.core
~~~~~~~~~~~~~~~

- Add idempotency for ``helm_pull`` module (https://github.com/ansible-collections/kubernetes.core/pull/1055).
- Fixed a bug where setting ``K8S_AUTH_VERIFY_SSL=true`` (or any string value) caused the value to be treated as a separate ``kubectl`` command argument. (https://github.com/ansible-collections/kubernetes.core/pull/1049).
- Limit supported versions of Helm to <4.0.0 (https://github.com/ansible-collections/kubernetes.core/pull/1039).
- Replace passing ``warnings`` to ``exit_json`` with ``AnsibleModule.warn`` in the ``k8s_drain``, ``k8s_rollback.py`` and ``k8s_scale.py`` modules as it deprecated in ``ansible-core>=2.19.0`` and will be removed in ``ansible-core>=2.23.0`` (https://github.com/ansible-collections/kubernetes.core/pull/1033).
- k8s - Fix return block from the module documentation (https://github.com/ansible-collections/kubernetes.core/pull/1056).
- meta - Add ``k8s_cluster_info``, ``k8s_json_patch`` and ``k8s_rollback`` to k8s action group (https://github.com/ansible-collections/kubernetes.core/pull/992).

purestorage.flasharray
~~~~~~~~~~~~~~~~~~~~~~

- purefa_certs - Fix the syntax to generate a CSR
- purefa_connect - Fixed issue where incorrect transport type was passed.
- purefa_default_protection - Fixed issue adding new default protection group to the array scope
- purefa_dsrole_old - Fixed incorrect parameter name for old version of functions
- purefa_host - Fixed AttributeError when deleting WWNs from a host
- purefa_info - Fixed AttributeError when subnet has no VLAN
- purefa_info - Fixed error with Resalms-based API clients
- purefa_info - Fixed issue with shelf controllers not supporting uptime
- purefa_info - Resolved AttributeErrors in ``default`` info section
- purefa_network - Fixes issue caused by None meaning change in SDK
- purefa_pgsched - Fixed schedule deletion idempotency
- purefa_policy - Fixed AttributeError when modifying a password policy

New Plugins
-----------

Callback
~~~~~~~~

- community.general.loganalytics_ingestion - Posts task results to an Azure Log Analytics workspace using the new Logs Ingestion API.

New Modules
-----------

cisco.ios
~~~~~~~~~

- cisco.ios.ios_bfd_interfaces - Resource module to configure bfd in interfaces.
- cisco.ios.ios_bfd_templates - Bidirectional Forwarding Detection (BFD) templates configurations

community.general
~~~~~~~~~~~~~~~~~

- community.general.icinga2_downtime - Manages Icinga 2 downtimes.
- community.general.keycloak_realm_localization - Allows management of Keycloak realm localization overrides via the Keycloak API.

community.libvirt
~~~~~~~~~~~~~~~~~

- community.libvirt.virt_cloud_instance - Provision new virtual machines from cloud images via libvirt

containers.podman
~~~~~~~~~~~~~~~~~

- containers.podman.podman_quadlet - Install or remove Podman Quadlets
- containers.podman.podman_quadlet_info - Gather information about Podman Quadlets

hitachivantara.vspone_block
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Sds Block
^^^^^^^^^

- hitachivantara.vspone_block.hv_sds_block_audit_log_setting - Manages Hitachi SDS block storage system audit log settings.
- hitachivantara.vspone_block.hv_sds_block_audit_log_setting_facts - Get audit log setting from SDS Block storage system.
- hitachivantara.vspone_block.hv_sds_block_dump_log_file - Dumps log information from SDS Block storage system.
- hitachivantara.vspone_block.hv_sds_block_dump_log_status_facts - Dumps log status information from SDS Block storage system.
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
- hitachivantara.vspone_block.hv_sds_block_storage_external_auth_server_setting - Manages external authentication server settings on VSP One SDS Block and Cloud systems.
- hitachivantara.vspone_block.hv_sds_block_storage_external_auth_server_setting_facts - Get external authentication server settings from the storage system.
- hitachivantara.vspone_block.hv_sds_block_storage_user_auth_setting - Manages external authentication server settings on VSP One SDS Block and Cloud systems.
- hitachivantara.vspone_block.hv_sds_block_storage_user_auth_setting_facts - Get user authentication settings from the storage system.

Vsp
^^^

- hitachivantara.vspone_block.hv_pav_alias - Manages PAV (Parallel Access Volume) alias assignments for VSP block storage systems.
- hitachivantara.vspone_block.hv_pav_alias_facts - retrieves information about PAV aliases from VSP block storage systems.
- hitachivantara.vspone_block.hv_session - Manages sessions on VSP block storage systems.
- hitachivantara.vspone_block.hv_session_facts - Retrieves information about sessions on VSP block storage systems.
- hitachivantara.vspone_block.hv_snapshot_family_facts - Retrieves snapshot family information of the provided LDEV ID from VSP block storage systems.
- hitachivantara.vspone_block.hv_supported_host_mode_facts - Retrieves supported host mode options information from a specified VSP block storage system.
- hitachivantara.vspone_block.hv_vclone_parent_volume_facts - Retrieves virtual clone parent volume information from VSP block storage systems.

Unchanged Collections
---------------------

- amazon.aws (still version 10.2.0)
- ansible.posix (still version 2.1.0)
- ansible.utils (still version 6.0.1)
- ansible.windows (still version 3.3.0)
- awx.awx (still version 24.6.1)
- azure.azcollection (still version 3.14.0)
- check_point.mgmt (still version 6.8.0)
- chocolatey.chocolatey (still version 1.5.3)
- cisco.aci (still version 2.13.0)
- cisco.intersight (still version 2.12.0)
- cisco.iosxr (still version 12.1.1)
- cisco.mso (still version 2.12.0)
- cisco.nxos (still version 11.1.3)
- cisco.ucs (still version 1.16.0)
- cloudscale_ch.cloud (still version 2.5.3)
- community.ciscosmb (still version 1.0.11)
- community.clickhouse (still version 2.0.0)
- community.grafana (still version 2.3.0)
- community.hashi_vault (still version 7.1.0)
- community.hrobot (still version 2.7.0)
- community.library_inventory_filtering_v1 (still version 1.1.5)
- community.okd (still version 5.0.0)
- community.postgresql (still version 4.2.0)
- community.proxmox (still version 1.5.0)
- community.proxysql (still version 1.7.0)
- community.rabbitmq (still version 1.6.0)
- community.routeros (still version 3.16.0)
- community.sap_libs (still version 1.6.0)
- community.sops (still version 2.2.7)
- community.vmware (still version 6.2.0)
- community.windows (still version 3.1.0)
- community.zabbix (still version 4.1.1)
- cyberark.conjur (still version 1.3.9)
- cyberark.pas (still version 1.0.36)
- dellemc.enterprise_sonic (still version 3.2.0)
- dellemc.openmanage (still version 10.0.1)
- dellemc.powerflex (still version 3.0.0)
- dellemc.unity (still version 2.1.0)
- f5networks.f5_modules (still version 1.39.0)
- fortinet.fortimanager (still version 2.12.0)
- fortinet.fortios (still version 2.4.2)
- google.cloud (still version 1.11.0)
- grafana.grafana (still version 6.0.6)
- hetzner.hcloud (still version 6.7.0)
- hitachivantara.vspone_object (still version 1.1.1)
- ibm.storage_virtualize (still version 3.2.0)
- ieisystem.inmanage (still version 4.0.0)
- infinidat.infinibox (still version 1.6.3)
- infoblox.nios_modules (still version 1.9.0)
- inspur.ispim (still version 2.2.4)
- junipernetworks.junos (still version 11.0.0)
- kaytus.ksmanage (still version 2.0.0)
- kubevirt.core (still version 2.2.3)
- lowlydba.sqlserver (still version 2.7.0)
- microsoft.ad (still version 1.10.0)
- microsoft.iis (still version 1.1.0)
- netapp.cloudmanager (still version 21.24.0)
- netapp.ontap (still version 23.3.0)
- netapp.storagegrid (still version 21.16.0)
- netapp_eseries.santricity (still version 1.4.1)
- netbox.netbox (still version 3.22.0)
- ngine_io.cloudstack (still version 3.0.0)
- openstack.cloud (still version 2.5.0)
- ovirt.ovirt (still version 3.2.2)
- purestorage.flashblade (still version 1.24.0)
- ravendb.ravendb (still version 1.0.4)
- splunk.es (still version 4.0.0)
- telekom_mms.icinga_director (still version 2.5.1)
- theforeman.foreman (still version 5.8.0)
- vmware.vmware (still version 2.7.0)
- vultr.cloud (still version 1.13.0)
- vyos.vyos (still version 6.0.0)
- wti.remote (still version 1.0.10)

v13.3.0
=======

.. contents::
  :local:
  :depth: 2

Release Summary
---------------

Release Date: 2026-01-29

`Porting Guide <https://docs.ansible.com/projects/ansible/devel/porting_guides.html>`_

Added Collections
-----------------

- community.clickhouse (version 2.0.0)
- pcg.alpaca_operator (version 2.1.1)

Ansible-core
------------

Ansible 13.3.0 contains ansible-core version 2.20.2.
This is a newer version than version 2.20.1 contained in the previous Ansible release.

The changes are reported in the combined changelog below.

Changed Collections
-------------------

If not mentioned explicitly, the changes are reported in the combined changelog below.

+-----------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| Collection                  | Ansible 13.2.0 | Ansible 13.3.0 | Notes                                                                                                                        |
+=============================+================+================+==============================================================================================================================+
| amazon.aws                  | 10.1.2         | 10.2.0         |                                                                                                                              |
+-----------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| ansible.netcommon           | 8.2.0          | 8.2.1          |                                                                                                                              |
+-----------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| ansible.utils               | 6.0.0          | 6.0.1          |                                                                                                                              |
+-----------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| azure.azcollection          | 3.12.0         | 3.14.0         | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+-----------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.dnac                  | 6.43.0         | 6.44.0         |                                                                                                                              |
+-----------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.meraki                | 2.21.9         | 2.22.0         |                                                                                                                              |
+-----------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.nxos                  | 11.1.1         | 11.1.3         |                                                                                                                              |
+-----------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| cloudscale_ch.cloud         | 2.5.2          | 2.5.3          |                                                                                                                              |
+-----------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.clickhouse        |                | 2.0.0          | The collection was added to Ansible                                                                                          |
+-----------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.dns               | 3.4.2          | 3.5.1          |                                                                                                                              |
+-----------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.docker            | 5.0.4          | 5.0.5          |                                                                                                                              |
+-----------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.general           | 12.2.0         | 12.3.0         |                                                                                                                              |
+-----------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.mongodb           | 1.7.10         | 1.7.11         | There are no changes recorded in the changelog.                                                                              |
+-----------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.routeros          | 3.15.0         | 3.16.0         |                                                                                                                              |
+-----------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.vmware            | 6.1.0          | 6.2.0          |                                                                                                                              |
+-----------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| containers.podman           | 1.18.0         | 1.18.1         |                                                                                                                              |
+-----------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| google.cloud                | 1.10.2         | 1.11.0         |                                                                                                                              |
+-----------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| hetzner.hcloud              | 6.3.0          | 6.7.0          |                                                                                                                              |
+-----------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| ibm.storage_virtualize      | 3.1.0          | 3.2.0          |                                                                                                                              |
+-----------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| infoblox.nios_modules       | 1.8.0          | 1.9.0          |                                                                                                                              |
+-----------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| netbox.netbox               | 3.21.0         | 3.22.0         |                                                                                                                              |
+-----------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| ovirt.ovirt                 | 3.2.1          | 3.2.2          |                                                                                                                              |
+-----------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| pcg.alpaca_operator         |                | 2.1.1          | The collection was added to Ansible                                                                                          |
+-----------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| purestorage.flashblade      | 1.23.1         | 1.24.0         |                                                                                                                              |
+-----------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| telekom_mms.icinga_director | 2.5.0          | 2.5.1          |                                                                                                                              |
+-----------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| theforeman.foreman          | 5.7.0          | 5.8.0          |                                                                                                                              |
+-----------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+
| vmware.vmware               | 2.6.0          | 2.7.0          |                                                                                                                              |
+-----------------------------+----------------+----------------+------------------------------------------------------------------------------------------------------------------------------+

Major Changes
-------------

community.vmware
~~~~~~~~~~~~~~~~

- Bump required ``vmware.vmware`` collection version to 2.5.0 (https://github.com/ansible-collections/community.vmware/pull/2503).

containers.podman
~~~~~~~~~~~~~~~~~

- Rewrite podman and buildah connections

Minor Changes
-------------

Ansible-core
~~~~~~~~~~~~

- ansible-test - Replace RHEL 10.0 remote with 10.1.
- ansible-test - Replace RHEL 9.6 remote with 9.7.

amazon.aws
~~~~~~~~~~

- Add support for the io2 storage type for RDS (https://github.com/ansible-collections/amazon.aws/pull/2748).
- ec2_launch_template - increase GP3 volume ``throughput`` limits in line with updated AWS limits (https://github.com/ansible-collections/amazon.aws/pull/2749).
- ec2_vol - increase ``throughput`` and ``iops`` limits for GP3 volumes in line with updated AWS limits (https://github.com/ansible-collections/amazon.aws/pull/2749).
- module_utils.s3 - added "501" to the list of error codes thrown by S3 replacements (https://github.com/ansible-collections/amazon.aws/issues/2447).
- module_utils/_s3/common - use ``is_boto3_error_httpstatus`` to handle HTTP 403 and 501 status codes from S3-compatible services (https://github.com/ansible-collections/amazon.aws/pull/2776).
- module_utils/botocore - add ``is_boto3_error_httpstatus`` helper function to catch boto3 exceptions based on HTTP status codes (https://github.com/ansible-collections/amazon.aws/pull/2776).
- route53 - added ``record_values`` key to ``resource_record_sets`` return value that can be accessed using Jinja2 dot notation (https://github.com/ansible-collections/amazon.aws/pull/2772).
- sts_assume_role - improve error handling for ``MalformedPolicyDocument`` errors by providing a clearer error message when an invalid policy document is provided (https://github.com/ansible-collections/amazon.aws/pull/2778).

cisco.dnac
~~~~~~~~~~

- Added 'template_content_file_path'  attribute in template_workflow_manager module
- Changes in accesspoint_location_workflow_manager module
- Changes in accesspoint_workflow_manager module
- Changes in application_policy_workflow_manager module
- Changes in assurance_device_health_score_settings_workflow_manager module
- Changes in assurance_icap_settings_workflow_manager module
- Changes in device_conigs_backup_workflow_manager module
- Changes in inventory_workflow_manager module
- Changes in network_settings_workflow_manager module
- Changes in provision_workflow_manager module
- Changes in reports_workflow_manager module
- Changes in sda_fabric_mulitcast_workflow_manager module
- Changes in sda_fabric_sites_zones_workflow_manager module
- Changes in site_workflow_manager module
- Changes in swim_workflow_manager module
- Changes in template_workflow_manager module
- Changes in user_role_workflow_manager module
- Changes in wireless_design_workflow_manager module

cisco.meraki
~~~~~~~~~~~~

- Updated with v1.66.0 dashboard API, adding new plugins and fixing bugs.

cloudscale_ch.cloud
~~~~~~~~~~~~~~~~~~~

- Added missing param when creating a health monitor

community.dns
~~~~~~~~~~~~~

- Hetzner DNS modules and plugins - support the `new Hetzner DNS API <https://docs.hetzner.com/networking/dns/faq/beta/>`__ (https://github.com/ansible-collections/community.dns/pull/301).

community.general
~~~~~~~~~~~~~~~~~

- alicloud_ecs module utils - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11341).
- android_sdk - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11343).
- archive - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11343).
- bitbucket_pipeline_known_host - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11343).
- chroot connection plugin - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11341).
- cobbler inventory plugin - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11341).
- copr - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11343).
- cronvar - simplify handling unknown exceptions (https://github.com/ansible-collections/community.general/pull/11340).
- cronvar - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11343).
- crypttab - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11343).
- elasticsearch_plugin - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11343).
- gitlab_group - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11343).
- gitlab_issue - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11343).
- gitlab_merge_request - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11343).
- gitlab_project - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11343).
- gunicorn - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11343).
- htpasswd - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11343).
- idrac_redfish_info - add multiple manager support to ``GetManagerAttributes`` command (https://github.com/ansible-collections/community.general/pull/11294).
- imc_rest - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11343).
- incus connection plugin - improve code readability (https://github.com/ansible-collections/community.general/pull/11346).
- incus connection plugin - simplify regular expression matching commands (https://github.com/ansible-collections/community.general/pull/11347).
- ini_file - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11343).
- interfaces_file - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11343).
- iptables_state - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11343).
- jail connection plugin - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11341).
- jenkins_credential - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11343).
- jenkins_plugin - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11343).
- jenkins_script - move ``import`` statemetns to the top of the file (https://github.com/ansible-collections/community.general/pull/11396).
- kdeconfig - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11343).
- known_hosts module utils - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11341).
- layman - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11343).
- linode - move ``import`` statemetns to the top of the file (https://github.com/ansible-collections/community.general/pull/11396).
- linode inventory plugin - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11341).
- listen_ports_facts - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11343).
- locale_gen - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11343).
- logentries callback plugin - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11341).
- lvm_pv - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11343).
- lxc connection plugin - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11341).
- lxd inventory plugin - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11341).
- lxd module utils - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11341).
- manageiq module utils - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11341).
- manageiq_alert_profiles - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11344).
- modprobe - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11344).
- mssql_db - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11344).
- nagios - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11344).
- netcup_dns - support diff mode (https://github.com/ansible-collections/community.general/pull/11376).
- nmcli - add idempotency check (https://github.com/ansible-collections/community.general/pull/11114).
- nmcli - add support for IPv6 routing rules (https://github.com/ansible-collections/community.general/issues/7094, https://github.com/ansible-collections/community.general/pull/11413).
- nosh - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11344).
- nsupdate - add support for server FQDN and the GSS-TSIG key algorithm (https://github.com/ansible-collections/community.general/issues/5730, https://github.com/ansible-collections/community.general/pull/11425).
- nsupdate modules plugin - replace aliased errors with proper Python error (https://github.com/ansible-collections/community.general/pull/11391).
- oci_utils module utils - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11341).
- omapi_host - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11344).
- one_image - move ``import`` statemetns to the top of the file (https://github.com/ansible-collections/community.general/pull/11396).
- one_image_info - move ``import`` statemetns to the top of the file (https://github.com/ansible-collections/community.general/pull/11396).
- one_service - move ``import`` statemetns to the top of the file (https://github.com/ansible-collections/community.general/pull/11396).
- one_vm - move ``import`` statemetns to the top of the file (https://github.com/ansible-collections/community.general/pull/11396).
- one_vm - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11344).
- opennebula inventory plugin - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11341).
- pam_limits - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11344).
- pamd - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11344).
- parted - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11344).
- pmem - simplify text tests without using regular expression (https://github.com/ansible-collections/community.general/pull/11388).
- pubnub_blocks - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11344).
- pulp_repo - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11344).
- read_csv - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11344).
- redfish_utils module utils - adds support of ``@Redfish.Settings`` in ``ComputerSystem`` attributes for ``set_boot_override`` function (https://github.com/ansible-collections/community.general/issues/11297, https://github.com/ansible-collections/community.general/pull/11322).
- redhat_subscription - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11344).
- rhsm_repository - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11344).
- runit - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11344).
- scaleway_ip - added ``project`` parameter (https://github.com/ansible-collections/community.general/issues/11367, https://github.com/ansible-collections/community.general/pull/11368).
- scaleway_security_group - added ``project`` parameter (https://github.com/ansible-collections/community.general/issues/11364, https://github.com/ansible-collections/community.general/pull/11366).
- sensu_check - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11344).
- sensu_client - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11344).
- sensu_handler - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11344).
- sensu_subscription - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11344).
- seport - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11344).
- serverless - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11344).
- slackpkg - refactor function ``query_packages()`` (https://github.com/ansible-collections/community.general/pull/11390).
- solaris_zone - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11344).
- sorcery - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11344).
- spotinst_aws_elastigroup - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11344).
- sudoers - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11344).
- svc - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11344).
- timestamp callback plugin - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11341).
- timezone - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11344).
- univention_umc module utils - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11341).
- wakeonlan - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11344).
- wsl connection plugin - add option ``wsl_remote_ssh_shell_type``. Support PowerShell in addition to cmd as the Windows shell (https://github.com/ansible-collections/community.general/issues/11307, https://github.com/ansible-collections/community.general/pull/11308).
- wsl connection plugin - replace aliased errors with proper Python error (https://github.com/ansible-collections/community.general/pull/11391).
- wsl connection plugin - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11341).
- xfs_quota - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11344).
- yaml cache plugin - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11341).
- zone connection plugin - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11341).
- zypper - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11344).
- zypper_repository - update to Python 3.7 idioms (https://github.com/ansible-collections/community.general/pull/11344).

community.routeros
~~~~~~~~~~~~~~~~~~

- api_info, api_modify - add ``prefix-pool`` field to and fix default of ``address-pool`` for ``ipv6 dhcp-server`` path (https://github.com/ansible-collections/community.routeros/pull/430).
- api_info, api_modify - add support for path ``ip socks access`` (https://github.com/ansible-collections/community.routeros/pull/431).

containers.podman
~~~~~~~~~~~~~~~~~

- Add configuration for new Ansible release
- Fix CI of Podman Search modul
- add passthrough and none log driver options

google.cloud
~~~~~~~~~~~~

- gcp_cloudbuildv2_* - added gcp_cloudbuildv2_connection and gcp_cloudbuildv2_repository modules (https://github.com/ansible-collections/google.cloud/pull/729).

hetzner.hcloud
~~~~~~~~~~~~~~

- All ``module_utils`` are now marked as **private**. None of the modules were intended for public use.
- floating_ip - Unassign Floating IP before deleting it.
- primary_ip - Added the Primary IP ``location`` name to the return values (``hcloud_primary_ip.location``).
- primary_ip - Added the ``location`` argument to create a Primary IP in a specific location.
- primary_ip - Unassign Primary IP before deleting it.
- primary_ip_info - Added the Primary IPs ``location`` name to the return values (``hcloud_primary_ip_info[].location``).
- server - Rebuilding a Server now supports the ``user_data`` argument.
- storage_box - The module is no longer marked as experimental.
- storage_box_info - The module is no longer marked as experimental.
- storage_box_snapshot - The module is no longer marked as experimental.
- storage_box_snapshot_info - The module is no longer marked as experimental.
- storage_box_subaccount - Replace the label based name workaround, with the new Storage Box Subaccount name property in the API.
- storage_box_subaccount - The module is no longer marked as experimental.
- storage_box_subaccount_info - Replace the label based name workaround, with the new Storage Box Subaccount name property in the API.
- storage_box_subaccount_info - The module is no longer marked as experimental.
- storage_box_type_info - The module is no longer marked as experimental.

ibm.storage_virtualize
~~~~~~~~~~~~~~~~~~~~~~

- ibm_sv_manage_replication_policy - Enabled support for logging in via partition ip
- ibm_svc_manage_volume - Added support for autoexpand, preferrednode and cache parameters

infoblox.nios_modules
~~~~~~~~~~~~~~~~~~~~~

- CI/CD - Added PyGObject support and improved dependency handling
- nios_dtc_lbdn - Added support for auth_zones with enhanced change detection for string and object formats, including proper handling when entries are removed

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

theforeman.foreman
~~~~~~~~~~~~~~~~~~

- activation_key - add ``content_view_environments`` parameter to support multi CV (https://github.com/theforeman/foreman-ansible-modules/pull/1935)
- job_invocation - add ``feature`` parameter (https://github.com/theforeman/foreman-ansible-modules/pull/1923)

vmware.vmware
~~~~~~~~~~~~~

- Add module vm_snapshot_revert to revert a virtual machine to a snapshot. Fixes https://github.com/ansible-collections/vmware.vmware/issues/281

Deprecated Features
-------------------

- The ``netapp.cloudmanager`` collection is considered unmaintained and will be removed from Ansible 15 if no one starts maintaining it again before Ansible 15.
  See `Collections Removal Process for unmaintained collections <https://docs.ansible.com/projects/ansible/devel/community/collection_contributors/collection_package_removal.html#unmaintained-collections>`__ for more details, including for how this can be cancelled (`https://forum.ansible.com/t/44891 <https://forum.ansible.com/t/44891>`__).
  After removal, users can still install this collection with ``ansible-galaxy collection install netapp.cloudmanager``.

amazon.aws
~~~~~~~~~~

- ec2_vpc_dhcp_option - the ``dhcp_config`` return value has been deprecated and will be removed in a release after 2026-12-01. Use ``dhcp_options`` instead (https://github.com/ansible-collections/amazon.aws/pull/2772).
- ec2_vpc_dhcp_option_info - the ``dhcp_config`` return value has been deprecated and will be removed in a release after 2026-12-01. Use ``dhcp_options`` instead (https://github.com/ansible-collections/amazon.aws/pull/2772).
- route53 - the ``values`` key in the ``resource_record_sets`` return value has been deprecated in favor of ``record_values`` for Jinja2 compatibility. The ``values`` key will be removed in a release after 2026-12-01 (https://github.com/ansible-collections/amazon.aws/pull/2772).

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

Bugfixes
--------

Ansible-core
~~~~~~~~~~~~

- Fix Windows LIB env var corruption (https://github.com/ansible-collections/ansible.windows/issues/297).
- ``ansible``, ``ansible-console`` - fix executing ``- meta: end_play`` tasks.
- ansible-test - Upgrade ``expat`` during provisioning of Fedora 42 remote instances.
- ansible_local will no longer trigger variable injection default value deprecation.
- copy - when a single-file local directory was specified as the source, ``changed`` used to be ``false`` even when the source was actually copied. It now makes sure ``changed`` is ``true`` in this case. (https://github.com/ansible/ansible/issues/85833)
- deb822_repository - Remove ``Install-Python-Debian`` from files outputed by the ``deb822_repository`` module (https://github.com/ansible/ansible/issues/86395)
- dnf - When installing a dnf module, install and enable when missing, upgrade when present (https://github.com/ansible/ansible/issues/73457)
- dnf - fix package installation when specifying architecture without version (e.g., ``libgcc.i686``) where a different architecture of the same package is already installed (https://github.com/ansible/ansible/issues/86156).
- package, service, gather_facts - fix templating module_defaults for modules executed by these action plugins. (https://github.com/ansible/ansible/issues/85848)
- winrm - Provide a better error message if a domain user is specified using a User Principal Name (``UPN``) but the ``pykerberos`` library is not installed so Kerberos is unavailable.

amazon.aws
~~~~~~~~~~

- connection/aws_ssm - fixed ReferenceError in aws_ssm connection plugin destructor during interpreter shutdown (https://github.com/ansible-collections/amazon.aws/issues/2728).
- lambda_info - fixed invalid return value documentation that used dot notation (``function.TheName``) which cannot be used in Jinja2 templates (https://github.com/ansible-collections/amazon.aws/pull/2772).
- s3_bucket - fix error when configuring AES256 bucket encryption with ``bucket_key_enabled`` explicitly set to ``false`` (https://github.com/ansible-collections/amazon.aws/issues/2734).

ansible.netcommon
~~~~~~~~~~~~~~~~~

- Adds backward compatibility of handling src attributes, functional consistency with ansible-core >= 2.19
- Adds deprecation warning for the jinja2 processing functionality for src attributes, src attributes in collections would still support considering file path but they would not process template files directly once the functionality is deprecated.
- It is suggested to use ansible.builtin.template module to process templates and use the processed template path in src attributes.

ansible.utils
~~~~~~~~~~~~~

- Add a cleanup step that removes empty {} and [] values from lists in keep_keys_from_dict_n_list()

cisco.nxos
~~~~~~~~~~

- Fixed nxos_facts module so it can handle VLAN interface facts without any issue even if addr is not defined
- Fixed nxos_static_routes module so to handle replaced and overridden state with vrf configuration.
- cisco.nxos.nxos_facts - Fix AttributeError when interface has multiple IPv6 addrs and handle ROW_addr as list.

community.dns
~~~~~~~~~~~~~

- Update Public Suffix List.
- converter module utils - add ``stacklevel=2`` to Python warnings. This affects third-party users of the module utils outside this collection (https://github.com/ansible-collections/community.dns/pull/310).
- hetzner_dns_record_set, hosttech_dns_record_set - fix ``on_existing != 'replace'`` mis-triggering when ``state=absent`` and the values to delete do not show up in the list of records (https://github.com/ansible-collections/community.dns/pull/301).
- hosttech_record_sets, hetzner_record_sets - ensure stable order also with Python < 3.6 (https://github.com/ansible-collections/community.dns/pull/301).
- lookup_rfc8427 lookup plugin - remove unused code (https://github.com/ansible-collections/community.dns/pull/308).
- remove_public_suffix filter plugin - fix plugin name in error message (https://github.com/ansible-collections/community.dns/pull/308).
- remove_registrable_domain filter plugin - fix plugin name in error message (https://github.com/ansible-collections/community.dns/pull/308).

community.docker
~~~~~~~~~~~~~~~~

- modules and plugins using the Docker SDK for Python - do not automatically set ``tls_hostname`` when ``validate_certs=true`` for Docker SDK for Python 7.0.0+ (https://github.com/ansible-collections/community.docker/issues/1225, https://github.com/ansible-collections/community.docker/pull/1226).

community.general
~~~~~~~~~~~~~~~~~

- cloudflare_dns - also allow ``flag=128`` for CAA records (https://github.com/ansible-collections/community.general/issues/11355, https://github.com/ansible-collections/community.general/pull/11377).
- gem - add compatibility with Ruby 4 rubygems (https://github.com/ansible-collections/community.general/issues/11397, https://github.com/ansible-collections/community.general/pull/11442).
- incus connection plugin - fix parsing of commands for Windows, enforcing a ``\`` after the drive letter and colon symbol (https://github.com/ansible-collections/community.general/pull/11347).
- keycloak_client - fix idempotency bug caused by ``null`` client attribute value differences for non-existing client attributes (https://github.com/ansible-collections/community.general/issues/11443, https://github.com/ansible-collections/community.general/pull/11444).
- logstash_plugin - fix argument order when using ``version`` parameter. The plugin name must come after options like ``--version`` for the ``logstash-plugin`` CLI to work correctly (https://github.com/ansible-collections/community.general/issues/10745, https://github.com/ansible-collections/community.general/pull/11440).
- pmem - fix test for invalid data input (https://github.com/ansible-collections/community.general/pull/11388).

community.vmware
~~~~~~~~~~~~~~~~

- vmware_guest_storage_policy - Fix storage policy search to return None if no policies are found, instead of causing an exception. fixes https://github.com/ansible-collections/community.vmware/issues/2527

containers.podman
~~~~~~~~~~~~~~~~~

- Fix idempotency for tagging local images
- Fix image idempotency in pull
- Fix issue with --rm and service in Quadlet
- fix(podman_prune) set top-level changed status

google.cloud
~~~~~~~~~~~~

- connection plugin - fix attribute error when using reset_connection (https://github.com/ansible-collections/google.cloud/issues/737).
- connection plugin - fix ssh error in tasks with loops (https://github.com/ansible-collections/google.cloud/issues/738).

hetzner.hcloud
~~~~~~~~~~~~~~

- Invalid redirects for Storage Box modules are now fixed by using fully qualified module names.

infoblox.nios_modules
~~~~~~~~~~~~~~~~~~~~~

- Fixed sanity and unit test execution in CI pipeline
- Fixed transform functions to handle ``None`` parameters and apply default values correctly

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

purestorage.flashblade
~~~~~~~~~~~~~~~~~~~~~~

- purefb_ad - Ensure encryption algorithms used match the GUI values
- purefb_certs - Fix the syntax to generate a CSR
- purefb_ds - Fixed issue when creating pre-enabled management directory service

vmware.vmware
~~~~~~~~~~~~~

- deploy_folder_template - Fixed issue where the vm folder was being cached in the placement service, causing the module to skip the template folder lookup and fail. Fixes https://github.com/ansible-collections/vmware.vmware/issues/292
- import_content_library_ovf - Fixed issue where OVFs with .nvram files failed to import Fixes https://github.com/ansible-collections/vmware.vmware/issues/257
- vm - Fixed issue where error handling failed when state is absent
- vm - Remove check that prevents memory from being decreased regardless of power state. Fixes https://github.com/ansible-collections/vmware.vmware/issues/298
- vm_apply_customization - Fixed issue where the product ID, user name, and user org name were required by the API but not by the module

New Plugins
-----------

Filter
~~~~~~

- community.general.to_toml - Convert variable to TOML string.

New Modules
-----------

ibm.storage_virtualize
~~~~~~~~~~~~~~~~~~~~~~

- ibm.storage_virtualize.ibm_sv_manage_clone - This module manages clone and thinclone of volume and volumegroup.

netbox.netbox
~~~~~~~~~~~~~

- netbox.netbox.netbox_contact_assignment - Manage contact assignments in NetBox
- netbox.netbox.netbox_data_source - Manage data sources in NetBox

Unchanged Collections
---------------------

- ansible.posix (still version 2.1.0)
- ansible.windows (still version 3.3.0)
- arista.eos (still version 12.0.0)
- awx.awx (still version 24.6.1)
- check_point.mgmt (still version 6.8.0)
- chocolatey.chocolatey (still version 1.5.3)
- cisco.aci (still version 2.13.0)
- cisco.intersight (still version 2.12.0)
- cisco.ios (still version 11.2.0)
- cisco.iosxr (still version 12.1.1)
- cisco.mso (still version 2.12.0)
- cisco.ucs (still version 1.16.0)
- community.aws (still version 10.0.0)
- community.ciscosmb (still version 1.0.11)
- community.crypto (still version 3.1.0)
- community.grafana (still version 2.3.0)
- community.hashi_vault (still version 7.1.0)
- community.hrobot (still version 2.7.0)
- community.library_inventory_filtering_v1 (still version 1.1.5)
- community.libvirt (still version 2.0.0)
- community.mysql (still version 4.0.1)
- community.okd (still version 5.0.0)
- community.postgresql (still version 4.2.0)
- community.proxmox (still version 1.5.0)
- community.proxysql (still version 1.7.0)
- community.rabbitmq (still version 1.6.0)
- community.sap_libs (still version 1.6.0)
- community.sops (still version 2.2.7)
- community.windows (still version 3.1.0)
- community.zabbix (still version 4.1.1)
- cyberark.conjur (still version 1.3.9)
- cyberark.pas (still version 1.0.36)
- dellemc.enterprise_sonic (still version 3.2.0)
- dellemc.openmanage (still version 10.0.1)
- dellemc.powerflex (still version 3.0.0)
- dellemc.unity (still version 2.1.0)
- f5networks.f5_modules (still version 1.39.0)
- fortinet.fortimanager (still version 2.12.0)
- fortinet.fortios (still version 2.4.2)
- grafana.grafana (still version 6.0.6)
- hitachivantara.vspone_block (still version 4.5.1)
- hitachivantara.vspone_object (still version 1.1.1)
- ieisystem.inmanage (still version 4.0.0)
- infinidat.infinibox (still version 1.6.3)
- inspur.ispim (still version 2.2.4)
- junipernetworks.junos (still version 11.0.0)
- kaytus.ksmanage (still version 2.0.0)
- kubernetes.core (still version 6.2.0)
- kubevirt.core (still version 2.2.3)
- lowlydba.sqlserver (still version 2.7.0)
- microsoft.ad (still version 1.10.0)
- microsoft.iis (still version 1.1.0)
- netapp.cloudmanager (still version 21.24.0)
- netapp.ontap (still version 23.3.0)
- netapp.storagegrid (still version 21.16.0)
- netapp_eseries.santricity (still version 1.4.1)
- ngine_io.cloudstack (still version 3.0.0)
- openstack.cloud (still version 2.5.0)
- purestorage.flasharray (still version 1.41.0)
- ravendb.ravendb (still version 1.0.4)
- splunk.es (still version 4.0.0)
- vmware.vmware_rest (still version 4.9.0)
- vultr.cloud (still version 1.13.0)
- vyos.vyos (still version 6.0.0)
- wti.remote (still version 1.0.10)

v13.2.0
=======

.. contents::
  :local:
  :depth: 2

Release Summary
---------------

Release Date: 2025-12-30

`Porting Guide <https://docs.ansible.com/projects/ansible/devel/porting_guides.html>`_

Ansible-core
------------

Ansible 13.2.0 contains ansible-core version 2.20.1.
This is the same version of ansible-core as in the previous Ansible release.

Changed Collections
-------------------

If not mentioned explicitly, the changes are reported in the combined changelog below.

+-----------------------------+----------------+----------------+----------------------------------------------------------+
| Collection                  | Ansible 13.1.0 | Ansible 13.2.0 | Notes                                                    |
+=============================+================+================+==========================================================+
| check_point.mgmt            | 6.7.0          | 6.8.0          | The collection did not have a changelog in this version. |
+-----------------------------+----------------+----------------+----------------------------------------------------------+
| cisco.ios                   | 11.1.1         | 11.2.0         |                                                          |
+-----------------------------+----------------+----------------+----------------------------------------------------------+
| cisco.iosxr                 | 12.1.0         | 12.1.1         |                                                          |
+-----------------------------+----------------+----------------+----------------------------------------------------------+
| cisco.nxos                  | 11.1.0         | 11.1.1         |                                                          |
+-----------------------------+----------------+----------------+----------------------------------------------------------+
| community.crypto            | 3.0.5          | 3.1.0          |                                                          |
+-----------------------------+----------------+----------------+----------------------------------------------------------+
| community.dns               | 3.4.1          | 3.4.2          |                                                          |
+-----------------------------+----------------+----------------+----------------------------------------------------------+
| community.general           | 12.1.0         | 12.2.0         |                                                          |
+-----------------------------+----------------+----------------+----------------------------------------------------------+
| community.proxmox           | 1.4.0          | 1.5.0          |                                                          |
+-----------------------------+----------------+----------------+----------------------------------------------------------+
| community.routeros          | 3.14.0         | 3.15.0         |                                                          |
+-----------------------------+----------------+----------------+----------------------------------------------------------+
| community.sap_libs          | 1.5.0          | 1.6.0          |                                                          |
+-----------------------------+----------------+----------------+----------------------------------------------------------+
| fortinet.fortimanager       | 2.11.0         | 2.12.0         |                                                          |
+-----------------------------+----------------+----------------+----------------------------------------------------------+
| hetzner.hcloud              | 6.2.1          | 6.3.0          |                                                          |
+-----------------------------+----------------+----------------+----------------------------------------------------------+
| hitachivantara.vspone_block | 4.5.0          | 4.5.1          |                                                          |
+-----------------------------+----------------+----------------+----------------------------------------------------------+
| netapp.ontap                | 23.2.0         | 23.3.0         |                                                          |
+-----------------------------+----------------+----------------+----------------------------------------------------------+
| netapp.storagegrid          | 21.15.0        | 21.16.0        |                                                          |
+-----------------------------+----------------+----------------+----------------------------------------------------------+
| purestorage.flasharray      | 1.40.0         | 1.41.0         |                                                          |
+-----------------------------+----------------+----------------+----------------------------------------------------------+
| purestorage.flashblade      | 1.22.0         | 1.23.1         |                                                          |
+-----------------------------+----------------+----------------+----------------------------------------------------------+

Major Changes
-------------

netapp.ontap
~~~~~~~~~~~~

- na_ontap_interface - AWS Lambda support added to the module.
- na_ontap_lun - AWS Lambda support added to the module.
- na_ontap_snapshot - AWS Lambda support added to the module.
- na_ontap_svm - AWS Lambda support added to the module.

Minor Changes
-------------

cisco.ios
~~~~~~~~~

- ios_l2_interfaces - Added xconnect and encapsulation attributes for L2VPN pseudowire and MPLS services configuration.

community.crypto
~~~~~~~~~~~~~~~~

- luks_device - add support for TPM2 enrollment using ``systemd-cryptsetup`` (https://github.com/ansible-collections/community.crypto/issues/850, https://github.com/ansible-collections/community.crypto/pull/972).
- luks_device - add support for keyslot priority (https://github.com/ansible-collections/community.crypto/issues/850, https://github.com/ansible-collections/community.crypto/pull/972).

community.general
~~~~~~~~~~~~~~~~~

- btrfs module utils - make execution of external commands safer by passing arguments as list (https://github.com/ansible-collections/community.general/pull/11240).
- deps module utils - change the internal representaion of dependency state (https://github.com/ansible-collections/community.general/pull/11242).
- keycloak_userprofile - add support for ``selector`` option (https://github.com/ansible-collections/community.general/pull/11309).
- keycloak_userprofile - add support for additional user profile attribute-validations available in Keycloak (https://github.com/ansible-collections/community.general/issues/9048, https://github.com/ansible-collections/community.general/pull/11285).
- lxc_container - refactor function ``create_script``, using ``subprocess.Popen()``, to a new module_utils ``_lxc`` (https://github.com/ansible-collections/community.general/pull/11204).
- lxc_container - use ``tempfile.TemporaryDirectory()`` instead of ``mkdtemp()`` (https://github.com/ansible-collections/community.general/pull/11323).
- monit - add ``monit_version`` return value also when the module has succeeded (https://github.com/ansible-collections/community.general/pull/11255).
- monit - use ``Enum`` to represent the possible states (https://github.com/ansible-collections/community.general/pull/11245).
- nmcli module - add ``vxlan_parent`` option required for multicast ``vxlan_remote`` addresses; add ``vxlan`` to list of bridgeable devices (https://github.com/ansible-collections/community.general/pull/11182).
- scaleway inventory plugin - added support for ``SCW_PROFILE`` environment variable for the ``scw_profile`` option (https://github.com/ansible-collections/community.general/issues/11310, https://github.com/ansible-collections/community.general/pull/11311).
- scaleway module utils - added ``scw_profile`` parameter with ``SCW_PROFILE`` environment variable support (https://github.com/ansible-collections/community.general/issues/11313, https://github.com/ansible-collections/community.general/pull/11314).

community.proxmox
~~~~~~~~~~~~~~~~~

- inventory plugin, plugin_utils - replace deprecated ``ansible.module_utils.common._collections_compat`` imports with ``collections.abc`` from the Python standard library (https://github.com/ansible-collections/community.proxmox/issues/241).
- proxmox - change disk size units to GiB (https://github.com/ansible-collections/community.proxmox/pull/236).
- proxmox_disk - change disk size units to GiB (https://github.com/ansible-collections/community.proxmox/pull/236).
- proxmox_kvm - add option to migrate local disks as well (https://github.com/ansible-collections/community.proxmox/pull/240).
- proxmox_kvm - change disk size units to GiB (https://github.com/ansible-collections/community.proxmox/pull/236).
- proxmox_node_info - add information on node network interfaces to node information output (https://github.com/ansible-collections/community.proxmox/pull/220).
- proxmox_node_info - add information on node's PVE version (https://github.com/ansible-collections/community.proxmox/pull/225).
- proxmox_snap_info - Adds a new module to list snapshots or a specific snapshot for VM or container (https://github.com/ansible-collections/community.proxmox/issues/229).
- proxmox_storage - add feature of subdirectory in CIFS share. (https://github.com/ansible-collections/community.proxmox/pull/214).
- proxmox_storage - fix passing nfs_options to API payload (https://github.com/ansible-collections/community.proxmox/issues/203, https://github.com/ansible-collections/community.proxmox/pull/221).
- proxmox_storage - fixed CIFS authentication by sending username and password parameters to proxmoxer (https://github.com/ansible-collections/community.proxmox/pull/214).

community.routeros
~~~~~~~~~~~~~~~~~~

- api_info, api_modify - add ``2g-probe-delay`` field to path ``interface wifi steering`` (https://github.com/ansible-collections/community.routeros/pull/428).
- api_info, api_modify - add ``aaa.*``, ``channel.*``, ``datapath.*``, ``interworking.*``, ``security.*``, ``steering.*`` sub-fields to path ``interface wifi configuration`` (https://github.com/ansible-collections/community.routeros/pull/428).
- api_info, api_modify - add ``deprioritize-unii-3-4``, ``reselect-interval``, ``reselect-time`` fields to path ``interface wifi channel`` (https://github.com/ansible-collections/community.routeros/pull/428).
- api_info, api_modify - add ``multi-passphrase-group`` field to path ``interface wifi security`` (https://github.com/ansible-collections/community.routeros/pull/428).
- api_info, api_modify - add ``send-email-from``, ``send-email-to`` and ``send-smtp-server`` to ``system watchdog`` (https://github.com/ansible-collections/community.routeros/pull/429).
- api_info, api_modify - add ``traffic-processing`` field to path ``interface wifi datapath`` and ``interface wifi configuration`` (https://github.com/ansible-collections/community.routeros/pull/424).
- api_info, api_modify - add ``use-bfd`` to ``routing ospf interface-template`` path (https://github.com/ansible-collections/community.routeros/pull/425).
- api_info, api_modify - add ``vrf`` to ``ip service`` (https://github.com/ansible-collections/community.routeros/pull/426).
- api_info, api_modify - add missing parameters to path ``interface bridge`` and ``interface bridge port`` (https://github.com/ansible-collections/community.routeros/pull/423).
- api_info, api_modify - add support for path ``disk settings`` (https://github.com/ansible-collections/community.routeros/pull/422).

community.sap_libs
~~~~~~~~~~~~~~~~~~

- sap_control_exec - Add local socket support (https://github.com/sap-linuxlab/community.sap_libs/pull/66)
- sap_hostctrl_exec - Add new module and tests (https://github.com/sap-linuxlab/community.sap_libs/pull/67)

fortinet.fortimanager
~~~~~~~~~~~~~~~~~~~~~

- Supported new modules to configure FortiProxy.
- Supported new schemas in FortiManager 7.0.15, 7.4.8, 7.6.4.

hetzner.hcloud
~~~~~~~~~~~~~~

- storage_box - New module to create and manage Storage Boxes in Hetzner.
- storage_box_info - New module to gather infos about Hetzner Storage Boxes.
- storage_box_snapshot - New module to create and manage Storage Box Snapshots in Hetzner.
- storage_box_snapshot_info - New module to gather infos about Hetzner Storage Box Snapshots.
- storage_box_subaccount - New module to create and manage Storage Box Subaccounts in Hetzner.
- storage_box_subaccount_info - New module to gather infos about Hetzner Storage Box Subaccounts.
- storage_box_type_info - New module to gather infos about Hetzner Storage Box Types.

netapp.ontap
~~~~~~~~~~~~

- na_ontap_ems_filter - new option `parameter_criteria` added in REST, requires ONTAP 9.13.1 or later.
- na_ontap_net_ifgrp - Update `mode` parameter to specify allowed values.

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

purestorage.flashblade
~~~~~~~~~~~~~~~~~~~~~~

- purefa_ad - Added support for local servers using the ``server`` parameter.
- purefb_ad - Added test and rotate states
- purefb_ad - Remove doc references to FQDNs as SPNs are the required method.
- purefb_ad - Updated encryption algorithms to use correct values
- purefb_ds - Allow directory services to be modified for internal NFS servers
- purefb_ds - Update test state to allow specific tests to be run
- purefb_info - Added MAC address information for LAGs

Deprecated Features
-------------------

community.general
~~~~~~~~~~~~~~~~~

- All module utils, plugin utils, and doc fragments will be made **private** in community.general 13.0.0. This means that they will no longer be part of the public API of the collection, and can have breaking changes even in bugfix releases. If you depend on importing code from the module or plugin utils, or use one of the doc fragments, please `comment in the issue to discuss this <https://github.com/ansible-collections/community.general/issues/11312>`__. Note that this does not affect any use of community.general in task files, roles, or playbooks (https://github.com/ansible-collections/community.general/issues/11312, https://github.com/ansible-collections/community.general/pull/11320).

community.routeros
~~~~~~~~~~~~~~~~~~

- api_find_and_modify - the current defaults for ``ignore_dynamic`` and ``ignore_builtin`` (both ``false``) have been deprecated and will change to ``true`` in community.routeros 4.0.0. To avoid deprecation messages, please set the value explicitly to ``true`` or ``false``, if you have not already done so. We recommend to set them to ``true``, unless you have a good reason to set them to ``false`` (https://github.com/ansible-collections/community.routeros/pull/399).

Bugfixes
--------

cisco.ios
~~~~~~~~~

- cisco.ios.ios_acls - Added support for converting numeric protocol values to real protocol options when gathered from the device.
- cisco.ios.ios_acls - Gathered state showing incomplete configuration.
- cisco.ios.ios_hsrp_intefaces - Considers version 1 as default if configuration does not specify version.
- cisco.ios.ios_hsrp_intefaces - Corrects idempotency issue when version is not specified in configuration.
- cisco.ios.ios_l2_interfaces - Moved mode parser to below the trunk parsers.

cisco.iosxr
~~~~~~~~~~~

- iosxr_bgp_address_family - Fixed label generation command handling under `address_family` configuration.

cisco.nxos
~~~~~~~~~~

- cisco.nxos.nxos_hsrp_intefaces - Considers version 1 as default if configuration does not specify version.
- cisco.nxos.nxos_hsrp_intefaces - Corrects idempotency issue when version is not specified in configuration.

community.dns
~~~~~~~~~~~~~

- Update Public Suffix List.

community.general
~~~~~~~~~~~~~~~~~

- apk - fix ``packages`` return value for apk-tools >= 3 (Alpine 3.23) (https://github.com/ansible-collections/community.general/issues/11264).
- iptables_state - refactor code to avoid writing unnecessary temporary files (https://github.com/ansible-collections/community.general/pull/11258).
- keycloak_realm - fixed crash in ``sanitize_cr()`` when ``realmrep`` was ``None`` (https://github.com/ansible-collections/community.general/pull/11260).
- keycloak_user_rolemapping module - fixed crash when assigning roles to users without an existing role (https://github.com/ansible-collections/community.general/issues/10960, https://github.com/ansible-collections/community.general/pull/11256).
- listen_ports_facts - fix handling of empty PID lists when ``command=ss`` (https://github.com/ansible-collections/community.general/pull/11332).
- monit - add delay of 0.5 seconds after state change and check for status (https://github.com/ansible-collections/community.general/pull/11255).
- monit - internal state was not reflecting when operation is "pending" in ``monit`` (https://github.com/ansible-collections/community.general/pull/11245).

community.proxmox
~~~~~~~~~~~~~~~~~

- proxmox all - add missing timeout parameter to proxmoxer object creation (https://github.com/ansible-collections/community.proxmox/pull/218).
- proxmox_ipam_info - fix bug where selecting by vmid did not work (https://github.com/ansible-collections/community.proxmox/pull/211).
- proxmox_zone - fix validation logic for VXLAN zones to accept either ``fabric`` or ``peers`` parameter. Previously, only ``fabric`` was accepted, but Proxmox VE also supports creating VXLAN zones with a peer address list (https://github.com/ansible-collections/community.proxmox/issues/216).
- remove wrong api endpoints and error messages from proxmod_node certificate management(https://github.com/ansible-collections/community.proxmox/pull/232).

fortinet.fortimanager
~~~~~~~~~~~~~~~~~~~~~

- Improved the request sending logic in httpapi plugin.

hitachivantara.vspone_block
~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Resolved resource group creation with VSP 5XXX series storage systems.
- Various playbook fixes and improvements.

netapp.ontap
~~~~~~~~~~~~

- na_ontap_aggregate - fixed issue with disabling software encryption in REST.
- na_ontap_cg_snapshot - fixed issue with ZAPI by removing default value for `consistency_type`.
- na_ontap_cifs_local_group - fixed issue with idempotency.
- na_ontap_firmware_upgrade - Updated documentation for `node` parameter and added examples.
- na_ontap_job_schedule - Fix documentation formatting issue.
- na_ontap_net_vlan - Fixed state detection when VLAN exists but is not in broadcast domain.
- na_ontap_qtree - Updated documentation for 'unix_permissions' parameter to clarify its usage.

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

purestorage.flasharray
~~~~~~~~~~~~~~~~~~~~~~

- purefa_info - Added version check to ensure tags are only used in appropriate Purity versions
- purefa_info - Fixed AttributeError when directory service role has no name
- purefa_policy - Multiple syntax errors fixed in the password policy update section

purestorage.flashblade
~~~~~~~~~~~~~~~~~~~~~~

- purefb_alert - Fixed issue with syntax error in update function
- purefb_bucket_replica - Fixed IndexError crash in check loop
- purefb_bucket_replica - Fixed issue with ItemIterator error
- purefb_pingtrace - Fiexed issue with XFM module when state is ping

New Modules
-----------

community.general
~~~~~~~~~~~~~~~~~

- community.general.ip2location_info - Retrieve IP geolocation information of a host's IP address.
- community.general.sssd_info - Check SSSD domain status using D-Bus.

community.proxmox
~~~~~~~~~~~~~~~~~

- community.proxmox.proxmox_ceph_mds - Add or delete Ceph Mds.
- community.proxmox.proxmox_ceph_mgr - Add or delete Ceph Manager.
- community.proxmox.proxmox_ceph_mon - Add or delete Ceph Monitor.
- community.proxmox.proxmox_sendkey - Send key presses to a Proxmox VM console.

fortinet.fortimanager
~~~~~~~~~~~~~~~~~~~~~

- fortinet.fortimanager.fmgr_devprof_log_syslogd_setting_logtemplates - System template log syslogd setting log templates
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
- fortinet.fortimanager.fmgr_icap_remoteservergroup - Icap remote server group
- fortinet.fortimanager.fmgr_icap_remoteservergroup_serverlist - Icap remote server group server list
- fortinet.fortimanager.fmgr_isolator_profile - Isolator profile
- fortinet.fortimanager.fmgr_isolator_profile_entries - Isolator profile entries
- fortinet.fortimanager.fmgr_pkg_firewall_responseshapingpolicy - Policy package firewall response shaping policy
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

Unchanged Collections
---------------------

- amazon.aws (still version 10.1.2)
- ansible.netcommon (still version 8.2.0)
- ansible.posix (still version 2.1.0)
- ansible.utils (still version 6.0.0)
- ansible.windows (still version 3.3.0)
- arista.eos (still version 12.0.0)
- awx.awx (still version 24.6.1)
- azure.azcollection (still version 3.12.0)
- chocolatey.chocolatey (still version 1.5.3)
- cisco.aci (still version 2.13.0)
- cisco.dnac (still version 6.43.0)
- cisco.intersight (still version 2.12.0)
- cisco.meraki (still version 2.21.9)
- cisco.mso (still version 2.12.0)
- cisco.ucs (still version 1.16.0)
- cloudscale_ch.cloud (still version 2.5.2)
- community.aws (still version 10.0.0)
- community.ciscosmb (still version 1.0.11)
- community.docker (still version 5.0.4)
- community.grafana (still version 2.3.0)
- community.hashi_vault (still version 7.1.0)
- community.hrobot (still version 2.7.0)
- community.library_inventory_filtering_v1 (still version 1.1.5)
- community.libvirt (still version 2.0.0)
- community.mongodb (still version 1.7.10)
- community.mysql (still version 4.0.1)
- community.okd (still version 5.0.0)
- community.postgresql (still version 4.2.0)
- community.proxysql (still version 1.7.0)
- community.rabbitmq (still version 1.6.0)
- community.sops (still version 2.2.7)
- community.vmware (still version 6.1.0)
- community.windows (still version 3.1.0)
- community.zabbix (still version 4.1.1)
- containers.podman (still version 1.18.0)
- cyberark.conjur (still version 1.3.9)
- cyberark.pas (still version 1.0.36)
- dellemc.enterprise_sonic (still version 3.2.0)
- dellemc.openmanage (still version 10.0.1)
- dellemc.powerflex (still version 3.0.0)
- dellemc.unity (still version 2.1.0)
- f5networks.f5_modules (still version 1.39.0)
- fortinet.fortios (still version 2.4.2)
- google.cloud (still version 1.10.2)
- grafana.grafana (still version 6.0.6)
- hitachivantara.vspone_object (still version 1.1.1)
- ibm.storage_virtualize (still version 3.1.0)
- ieisystem.inmanage (still version 4.0.0)
- infinidat.infinibox (still version 1.6.3)
- infoblox.nios_modules (still version 1.8.0)
- inspur.ispim (still version 2.2.4)
- junipernetworks.junos (still version 11.0.0)
- kaytus.ksmanage (still version 2.0.0)
- kubernetes.core (still version 6.2.0)
- kubevirt.core (still version 2.2.3)
- lowlydba.sqlserver (still version 2.7.0)
- microsoft.ad (still version 1.10.0)
- microsoft.iis (still version 1.1.0)
- netapp.cloudmanager (still version 21.24.0)
- netapp_eseries.santricity (still version 1.4.1)
- netbox.netbox (still version 3.21.0)
- ngine_io.cloudstack (still version 3.0.0)
- openstack.cloud (still version 2.5.0)
- ovirt.ovirt (still version 3.2.1)
- ravendb.ravendb (still version 1.0.4)
- splunk.es (still version 4.0.0)
- telekom_mms.icinga_director (still version 2.5.0)
- theforeman.foreman (still version 5.7.0)
- vmware.vmware (still version 2.6.0)
- vmware.vmware_rest (still version 4.9.0)
- vultr.cloud (still version 1.13.0)
- vyos.vyos (still version 6.0.0)
- wti.remote (still version 1.0.10)

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

fortinet.fortios
~~~~~~~~~~~~~~~~

- Supported default_group feature for all of the modules.

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
