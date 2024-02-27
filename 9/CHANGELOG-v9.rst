=======================
Ansible 9 Release Notes
=======================

This changelog describes changes since Ansible 8.0.0.

.. contents::
  :depth: 2

v9.3.0
======

.. contents::
  :local:
  :depth: 2

Release Summary
---------------

Release Date: 2024-02-27

`Porting Guide <https://docs.ansible.com/ansible/devel/porting_guides.html>`_

Ansible-core
------------

Ansible 9.3.0 contains ansible-core version 2.16.4.
This is a newer version than version 2.16.3 contained in the previous Ansible release.

The changes are reported in the combined changelog below.

Changed Collections
-------------------

If not mentioned explicitly, the changes are reported in the combined changelog below.

+-----------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| Collection            | Ansible 9.2.0 | Ansible 9.3.0 | Notes                                                                                                                        |
+=======================+===============+===============+==============================================================================================================================+
| amazon.aws            | 7.2.0         | 7.3.0         |                                                                                                                              |
+-----------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| awx.awx               | 23.6.0        | 23.8.1        | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+-----------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.dnac            | 6.10.2        | 6.11.0        | The collection did not have a changelog in this version.                                                                     |
+-----------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.crypto      | 2.17.1        | 2.18.0        |                                                                                                                              |
+-----------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.dns         | 2.8.0         | 2.8.1         |                                                                                                                              |
+-----------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.docker      | 3.7.0         | 3.8.0         |                                                                                                                              |
+-----------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.general     | 8.3.0         | 8.4.0         |                                                                                                                              |
+-----------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.grafana     | 1.7.0         | 1.8.0         |                                                                                                                              |
+-----------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.mongodb     | 1.6.3         | 1.7.1         | There are no changes recorded in the changelog.                                                                              |
+-----------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.mysql       | 3.8.0         | 3.9.0         |                                                                                                                              |
+-----------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.postgresql  | 3.3.0         | 3.4.0         |                                                                                                                              |
+-----------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.routeros    | 2.12.0        | 2.13.0        |                                                                                                                              |
+-----------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.vmware      | 4.1.0         | 4.2.0         |                                                                                                                              |
+-----------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| containers.podman     | 1.11.0        | 1.12.0        |                                                                                                                              |
+-----------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| f5networks.f5_modules | 1.27.1        | 1.28.0        |                                                                                                                              |
+-----------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| fortinet.fortimanager | 2.3.1         | 2.4.0         |                                                                                                                              |
+-----------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| fortinet.fortios      | 2.3.4         | 2.3.5         |                                                                                                                              |
+-----------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| grafana.grafana       | 2.2.4         | 2.2.5         |                                                                                                                              |
+-----------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| hetzner.hcloud        | 2.4.1         | 2.5.0         |                                                                                                                              |
+-----------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| infinidat.infinibox   | 1.3.12        | 1.4.3         | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+-----------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| kubernetes.core       | 2.4.0         | 2.4.1         |                                                                                                                              |
+-----------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| lowlydba.sqlserver    | 2.2.2         | 2.3.1         |                                                                                                                              |
+-----------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| netapp.ontap          | 22.9.0        | 22.10.0       |                                                                                                                              |
+-----------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| netapp.storagegrid    | 21.11.1       | 21.12.0       |                                                                                                                              |
+-----------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| netbox.netbox         | 3.16.0        | 3.17.0        |                                                                                                                              |
+-----------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| purestorage.fusion    | 1.6.0         | 1.6.1         |                                                                                                                              |
+-----------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+

Major Changes
-------------

community.mysql
~~~~~~~~~~~~~~~

- Collection version 2.*.* is EOL, no more bugfixes will be backported. Please consider upgrading to the latest version.

fortinet.fortios
~~~~~~~~~~~~~~~~

- Update all the boolean values to true/false in the documents and examples.
- Update the document of log_fact.
- Update the mismatched version message with version ranges.
- Update the required ansible version to 2.14.
- Update the supported version ranges instead of concrete version numbers to reduce the collection size.

Minor Changes
-------------

amazon.aws
~~~~~~~~~~

- backup_plan - Let user to set ``schedule_expression_timezone`` for backup plan rules when when using botocore >= 1.31.36 (https://github.com/ansible-collections/amazon.aws/issues/1952).
- iam_user - refactored error handling to use a decorator (https://github.com/ansible-collections/amazon.aws/pull/1951).
- lambda - added support for using ECR images for the function (https://github.com/ansible-collections/amazon.aws/pull/1939).
- module_utils.errors - added a basic error handler decorator (https://github.com/ansible-collections/amazon.aws/pull/1951).
- rds_cluster - Add support for ServerlessV2ScalingConfiguration to create and modify cluster operations (https://github.com/ansible-collections/amazon.aws/pull/1839).
- s3_bucket_info - add parameter ``bucket_versioning`` to return the versioning state of a bucket (https://github.com/ansible-collections/amazon.aws/pull/1919).
- s3_object_info - fix exception raised when listing objects from empty bucket (https://github.com/ansible-collections/amazon.aws/pull/1919).

community.crypto
~~~~~~~~~~~~~~~~

- x509_crl - the new option ``serial_numbers`` allow to configure in which format serial numbers can be provided to ``revoked_certificates[].serial_number``. The default is as integers (``serial_numbers=integer``) for backwards compatibility; setting ``serial_numbers=hex-octets`` allows to specify colon-separated hex octet strings like ``00:11:22:FF`` (https://github.com/ansible-collections/community.crypto/issues/687, https://github.com/ansible-collections/community.crypto/pull/715).

community.docker
~~~~~~~~~~~~~~~~

- docker_compose_v2 - allow to wait until containers are running/health when running ``docker compose up`` with the new ``wait`` option (https://github.com/ansible-collections/community.docker/issues/794, https://github.com/ansible-collections/community.docker/pull/796).
- docker_container - the ``pull_check_mode_behavior`` option now allows to control the module's behavior in check mode when ``pull=always`` (https://github.com/ansible-collections/community.docker/issues/792, https://github.com/ansible-collections/community.docker/pull/797).
- docker_container - the ``pull`` option now accepts the three values ``never``, ``missing_image`` (default), and ``never``, next to the previously valid values ``true`` (equivalent to ``always``) and ``false`` (equivalent to ``missing_image``). This allows the equivalent to ``--pull=never`` from the Docker command line (https://github.com/ansible-collections/community.docker/issues/783, https://github.com/ansible-collections/community.docker/pull/797).

community.general
~~~~~~~~~~~~~~~~~

- bitwarden lookup plugin - add ``bw_session`` option, to pass session key instead of reading from env (https://github.com/ansible-collections/community.general/pull/7994).
- gitlab_deploy_key, gitlab_group_members, gitlab_group_variable, gitlab_hook, gitlab_instance_variable, gitlab_project_badge, gitlab_project_variable, gitlab_user - improve API pagination and compatibility with different versions of ``python-gitlab`` (https://github.com/ansible-collections/community.general/pull/7790).
- gitlab_hook - adds ``releases_events`` parameter for supporting Releases events triggers on GitLab hooks (https://github.com/ansible-collections/community.general/pull/7956).
- icinga2 inventory plugin - add Jinja2 templating support to ``url``, ``user``, and ``password`` paramenters (https://github.com/ansible-collections/community.general/issues/7074, https://github.com/ansible-collections/community.general/pull/7996).
- mssql_script - adds transactional (rollback/commit) support via optional boolean param ``transaction`` (https://github.com/ansible-collections/community.general/pull/7976).
- proxmox_kvm - add parameter ``update_unsafe`` to avoid limitations when updating dangerous values (https://github.com/ansible-collections/community.general/pull/7843).
- redfish_config - add command ``SetServiceIdentification`` to set service identification (https://github.com/ansible-collections/community.general/issues/7916).
- sudoers - add support for the ``NOEXEC`` tag in sudoers rules (https://github.com/ansible-collections/community.general/pull/7983).
- terraform - fix ``diff_mode`` in state ``absent`` and when terraform ``resource_changes`` does not exist (https://github.com/ansible-collections/community.general/pull/7963).

community.grafana
~~~~~~~~~~~~~~~~~

- Manage `grafana_folder` for organizations
- Merged ansible role telekom-mms/ansible-role-grafana into ansible-collections/community.grafana
- added `community.grafana.notification_channel` to role
- grafana_dashboard - add check_mode support

community.mysql
~~~~~~~~~~~~~~~

- mysql_user - add the ``password_expire`` and ``password_expire_interval`` arguments to implement the password expiration management for mysql user (https://github.com/ansible-collections/community.mysql/pull/598).
- mysql_user - add user attribute support via the ``attributes`` parameter and return value (https://github.com/ansible-collections/community.mysql/pull/604).

community.postgresql
~~~~~~~~~~~~~~~~~~~~

- postgresql_db - add the ``icu_locale`` argument (https://github.com/ansible-collections/community.postgresql/issues/666).
- postgresql_db - add the ``locale_provider`` argument (https://github.com/ansible-collections/community.postgresql/issues/666).

community.routeros
~~~~~~~~~~~~~~~~~~

- api_info, api_modify - make path ``user group`` modifiable and add ``comment`` attribute (https://github.com/ansible-collections/community.routeros/issues/256, https://github.com/ansible-collections/community.routeros/pull/257).
- api_modify, api_info - add support for the ``ip vrf`` path in RouterOS 7  (https://github.com/ansible-collections/community.routeros/pull/259)

community.vmware
~~~~~~~~~~~~~~~~

- Add standard function vmware_argument_spec() from module_utils for using default env fallback function. https://github.com/ansible-collections/community.vmware/issues/1977
- vmware_first_class_disk_info - Add a module to gather informations about first class disks. (https://github.com/ansible-collections/community.vmware/pull/1996). (https://github.com/ansible-collections/community.vmware/issues/1988).
- vmware_host_facts - Add the possibility to get the related datacenter. (https://github.com/ansible-collections/community.vmware/pull/1994).
- vmware_vm_inventory - Add parameter `subproperties` (https://github.com/ansible-collections/community.vmware/pull/1972).
- vmware_vmkernel - Add the function to set the enable_backup_nfc setting (https://github.com/ansible-collections/community.vmware/pull/1978)
- vsphere_copy - Add parameter to tell vsphere_copy which diskformat is being uploaded (https://github.com/ansible-collections/community.vmware/pull/1995).

containers.podman
~~~~~~~~~~~~~~~~~

- Add log_opt and annotaion options to podman_play module
- Add option to parse CreateCommand easily for diff calc
- Add support for setting underlying interface in podman_network
- Alias generate systemd options stop_timeout and time
- Fix CI rootfs for podman_container
- Fix broken conmon version in CI install
- Improve security_opt comparison between existing container
- podman_container - Add new arguments to podman status commands
- podman_container - Update env_file to accept a list of files instead of a single file
- podman_secret_info - Add secrets info module

fortinet.fortimanager
~~~~~~~~~~~~~~~~~~~~~

- Added deprecated warning to invalid argument name, please change the invalid argument name such as "var-name", "var name" to "var_name".
- Supported fortimanager 7.4.2, 21 new modules.

grafana.grafana
~~~~~~~~~~~~~~~

- Add 'run_once' to download&unzip tasks by @v-zhuravlev in https://github.com/grafana/grafana-ansible-collection/pull/136
- Adding `oauth_allow_insecure_email_lookup` to fix oauth user sync error by @hypery2k in https://github.com/grafana/grafana-ansible-collection/pull/132
- Bump ansible-core from 2.15.4 to 2.15.8 by @dependabot in https://github.com/grafana/grafana-ansible-collection/pull/137
- Bump ansible-lint from 6.13.1 to 6.14.3 by @dependabot in https://github.com/grafana/grafana-ansible-collection/pull/139
- Bump ansible-lint from 6.14.3 to 6.22.2 by @dependabot in https://github.com/grafana/grafana-ansible-collection/pull/142
- Bump ansible-lint from 6.22.2 to 24.2.0 by @dependabot in https://github.com/grafana/grafana-ansible-collection/pull/150
- Bump jinja2 from 3.1.2 to 3.1.3 by @dependabot in https://github.com/grafana/grafana-ansible-collection/pull/129
- Bump pylint from 2.16.2 to 3.0.3 by @dependabot in https://github.com/grafana/grafana-ansible-collection/pull/141
- Bump yamllint from 1.29.0 to 1.33.0 by @dependabot in https://github.com/grafana/grafana-ansible-collection/pull/140
- Bump yamllint from 1.29.0 to 1.33.0 by @dependabot in https://github.com/grafana/grafana-ansible-collection/pull/143
- Bump yamllint from 1.33.0 to 1.34.0 by @dependabot in https://github.com/grafana/grafana-ansible-collection/pull/151
- Change handler to systemd by @v-zhuravlev in https://github.com/grafana/grafana-ansible-collection/pull/135
- Fix links in grafana_agent/defaults/main.yaml by @PabloCastellano in https://github.com/grafana/grafana-ansible-collection/pull/134
- Topic/grafana agent idempotency by @ohdearaugustin in https://github.com/grafana/grafana-ansible-collection/pull/147

hetzner.hcloud
~~~~~~~~~~~~~~

- Replace deprecated `ansible.netcommon` ip utils with python `ipaddress` module. The `ansible.netcommon` collection is no longer required by the collections.
- firewall - Allow forcing the deletion of firewalls that are still in use.
- firewall - Do not silence 'firewall still in use' delete failures.
- firewall - Return resources the firewall is `applied_to`.
- firewall_info - Add new `firewall_info` module to gather firewalls info.
- firewall_resource - Add new `firewall_resource` module to manage firewalls resources.
- inventory - Add `hostvars_prefix` and hostvars_suffix` options to customize the inventory host variables keys.

lowlydba.sqlserver
~~~~~~~~~~~~~~~~~~

- Add ability to prevent changing login's password, even if password supplied.
- Add new input strings to be compatible with dbops v0.9.x (https://github.com/lowlydba/lowlydba.sqlserver/pull/231)

netapp.ontap
~~~~~~~~~~~~

- na_ontap_cifs_server - new option `is_multichannel_enabled` added in REST, requires ONTAP 9.10 or later.
- na_ontap_export_policy_rule - added `actions` and `modify` in module output.
- na_ontap_file_security_permissions_acl - added `actions` and `modify` in module output.
- na_ontap_igroup_initiator - added `actions` in module output.
- na_ontap_lun_map - added `actions` in module output.
- na_ontap_lun_map_reporting_nodes - added `actions` in module output.
- na_ontap_name_mappings - added `actions` and `modify` in module output.
- na_ontap_node - added `modify` in module output.
- na_ontap_rest_info - added warning message if given subset doesn't support option `owning_resource`.
- na_ontap_storage_auto_giveback - added information on modified attributes in module output.
- na_ontap_vscan_scanner_pool - added REST support to Vscan Scanner Pools Configuration module, requires ONTAP 9.6 or later.

netapp.storagegrid
~~~~~~~~~~~~~~~~~~

- na_sg_grid_account - New option ``allow_select_object_content`` for enabling use of the S3 SelectObjectContent API.
- na_sg_grid_account - New option ``description`` for setting additional identifying information for the tenant account.

netbox.netbox
~~~~~~~~~~~~~

- CI - CI adjustments [#1154](https://github.com/netbox-community/ansible_modules/pull/1154) [#1155](https://github.com/netbox-community/ansible_modules/pull/1155) [#1157](https://github.com/netbox-community/ansible_modules/pull/1157)
- nb_lookup - Add new VPN endpoints for NetBox 3.7 support [#1162](https://github.com/netbox-community/ansible_modules/pull/1162)
- netbox_rack_role - Add description option [#1143](https://github.com/netbox-community/ansible_modules/pull/1143)
- netbox_virtual_disk - New module [#1153](https://github.com/netbox-community/ansible_modules/pull/1153)
- netbox_virtual_machine and netbox_device - Add option config_template [#1171](https://github.com/netbox-community/ansible_modules/pull/1171)

purestorage.fusion
~~~~~~~~~~~~~~~~~~

- fusion_volume - Allow creating a new volume from already existing volume or volume snapshot

Deprecated Features
-------------------

- The ``inspur.sm`` collection is considered unmaintained and will be removed from Ansible 11 if no one starts maintaining it again before Ansible 11. See `the removal process for details on how this works <https://github.com/ansible-collections/overview/blob/main/removal_from_ansible.rst#cancelling-removal-of-an-unmaintained-collection>`__ (https://forum.ansible.com/t/2854).
- The ``netapp.storagegrid`` collection is considered unmaintained and will be removed from Ansible 11 if no one starts maintaining it again before Ansible 11. See `the removal process for details on how this works <https://github.com/ansible-collections/overview/blob/main/removal_from_ansible.rst#cancelling-removal-of-an-unmaintained-collection>`__ (https://forum.ansible.com/t/2811).
- The ``purestorage.fusion`` collection is officially unmaintained and has been archived. Therefore, it will be removed from Ansible 10 (https://forum.ansible.com/t/3712).

community.crypto
~~~~~~~~~~~~~~~~

- openssl_csr_pipe, openssl_privatekey_pipe, x509_certificate_pipe - the current behavior of check mode is deprecated and will change in community.crypto 3.0.0. The current behavior is similar to the modules without ``_pipe``: if the object needs to be (re-)generated, only the ``changed`` status is set, but the object is not updated. From community.crypto 3.0.0 on, the modules will ignore check mode and always act as if check mode is not active. This behavior can already achieved now by adding ``check_mode: false`` to the task. If you think this breaks your use-case of this module, please `create an issue in the community.crypto repository <https://github.com/ansible-collections/community.crypto/issues/new/choose>`__ (https://github.com/ansible-collections/community.crypto/issues/712, https://github.com/ansible-collections/community.crypto/pull/714).

Bugfixes
--------

Ansible-core
~~~~~~~~~~~~

- Fix loading vars_plugins in roles (https://github.com/ansible/ansible/issues/82239).
- expect - fix argument spec error using timeout=null (https://github.com/ansible/ansible/issues/80982).
- include_vars - fix calculating ``depth`` relative to the root and ensure all files are included (https://github.com/ansible/ansible/issues/80987).
- templating - ensure syntax errors originating from a template being compiled into Python code object result in a failure (https://github.com/ansible/ansible/issues/82606)

amazon.aws
~~~~~~~~~~

- backup_plan - Fix idempotency issue when using botocore >= 1.31.36 (https://github.com/ansible-collections/amazon.aws/issues/1952).
- plugins/inventory/aws_ec2 - Fix failure when retrieving information for more than 40 instances with use_ssm_inventory (https://github.com/ansible-collections/amazon.aws/issues/1713).

community.crypto
~~~~~~~~~~~~~~~~

- luks_device - fixed module a bug that prevented using ``remove_keyslot`` with the value ``0`` (https://github.com/ansible-collections/community.crypto/pull/710).
- luks_device - fixed module falsely outputting ``changed=false`` when trying to add a new slot with a key that is already present in another slot. The module now rejects adding keys that are already present in another slot (https://github.com/ansible-collections/community.crypto/pull/710).
- luks_device - fixed testing of LUKS passphrases in when specifying a keyslot for cryptsetup version 2.0.3. The output of this cryptsetup version slightly differs from later versions (https://github.com/ansible-collections/community.crypto/pull/710).

community.dns
~~~~~~~~~~~~~

- Update Public Suffix List.

community.docker
~~~~~~~~~~~~~~~~

- docker_compose_v2 - do not consider a ``Waiting`` event as an action/change (https://github.com/ansible-collections/community.docker/pull/804).
- docker_compose_v2 - do not treat service-level pull events as changes to avoid incorrect ``changed=true`` return value of ``pull=always`` (https://github.com/ansible-collections/community.docker/issues/802, https://github.com/ansible-collections/community.docker/pull/803).
- docker_compose_v2, docker_compose_v2_pull - fix parsing of pull messages for Docker Compose 2.20.0 (https://github.com/ansible-collections/community.docker/issues/785, https://github.com/ansible-collections/community.docker/pull/786).

community.general
~~~~~~~~~~~~~~~~~

- cargo - fix idempotency issues when using a custom installation path for packages (using the ``--path`` parameter). The initial installation runs fine, but subsequent runs use the ``get_installed()`` function which did not check the given installation location, before running ``cargo install``. This resulted in a false ``changed`` state. Also the removal of packeges using ``state: absent`` failed, as the installation check did not use the given parameter (https://github.com/ansible-collections/community.general/pull/7970).
- gitlab_issue - fix behavior to search GitLab issue, using ``search`` keyword instead of ``title`` (https://github.com/ansible-collections/community.general/issues/7846).
- gitlab_runner - fix pagination when checking for existing runners (https://github.com/ansible-collections/community.general/pull/7790).
- keycloak_client - fixes issue when metadata is provided in desired state when task is in check mode (https://github.com/ansible-collections/community.general/issues/1226, https://github.com/ansible-collections/community.general/pull/7881).
- modprobe - listing modules files or modprobe files could trigger a FileNotFoundError if ``/etc/modprobe.d`` or ``/etc/modules-load.d`` did not exist. Relevant functions now return empty lists if the directories do not exist to avoid crashing the module (https://github.com/ansible-collections/community.general/issues/7717).
- onepassword lookup plugin - failed for fields that were in sections and had uppercase letters in the label/ID. Field lookups are now case insensitive in all cases (https://github.com/ansible-collections/community.general/pull/7919).
- pkgin - pkgin (pkgsrc package manager used by SmartOS) raises erratic exceptions and spurious ``changed=true`` (https://github.com/ansible-collections/community.general/pull/7971).
- redfish_info - allow for a GET operation invoked by ``GetUpdateStatus`` to allow for an empty response body for cases where a service returns 204 No Content (https://github.com/ansible-collections/community.general/issues/8003).
- redfish_info - correct uncaught exception when attempting to retrieve ``Chassis`` information (https://github.com/ansible-collections/community.general/pull/7952).

community.grafana
~~~~~~~~~~~~~~~~~

- test: replace deprecated `TestCase.assertEquals` to support Python 3.12

community.mysql
~~~~~~~~~~~~~~~

- mysql_info - the ``slave_status`` filter was returning an empty list on MariaDB with multiple replication channels. It now returns all channels by running ``SHOW ALL SLAVES STATUS`` for MariaDB servers (https://github.com/ansible-collections/community.mysql/issues/603).

community.postgresql
~~~~~~~~~~~~~~~~~~~~

- postgresql_privs - fix a failure when altering privileges with ``grant_option: true`` (https://github.com/ansible-collections/community.postgresql/issues/668).

community.routeros
~~~~~~~~~~~~~~~~~~

- facts - fix date not getting removed for idempotent config export (https://github.com/ansible-collections/community.routeros/pull/262).

containers.podman
~~~~~~~~~~~~~~~~~

- Add idempotency for podman_secret module
- Catch exceptions when no JSON output in podman_image
- Fail if systemd generation failed and it's explicitly set
- Fix example name
- Fix idempotency for podman_network
- Fix idempotency when using 0.0.0.0 in ports
- Fix multi-image support for podman_save
- Fix volume inspection by name in podman_volume
- Recreate stopped containers if recreate flag is enabled

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

- Changed revision to v_range to reduce the size of the code.
- Fixed the behavior of module fmgr_firewall_internetservicecustom.
- Fixed the behavior of some modules that contain the argument policyid.
- Improved example ansible playbooks.
- Improved the logic of fmgr_fact, fmgr_clone, fmgr_rename, fmgr_move. Usage remains unchanged.
- Reduced the size of module_arg_spec in each module.
- Removed most of the sanity test ignores.

fortinet.fortios
~~~~~~~~~~~~~~~~

- Github issue

lowlydba.sqlserver
~~~~~~~~~~~~~~~~~~

- Add ActiveStartDate to the compare properties so this item is marked accurately as changed.
- Fixed the formatting of the SPN by updating the backslash to a forward-slash for the $spn var (lowlydba.sqlserver.spn)

netapp.ontap
~~~~~~~~~~~~

- na_ontap_igroup_initiator - fixed issue with idempotency.

netapp.storagegrid
~~~~~~~~~~~~~~~~~~

- Removed fetch limit in API request and implemented pagination.

netbox.netbox
~~~~~~~~~~~~~

- netbox_vlan - Fix documentation of vlan_group [#1138](https://github.com/netbox-community/ansible_modules/pull/1138)

New Plugins
-----------

Callback
~~~~~~~~

- community.general.default_without_diff - The default ansible callback without diff output

Filter
~~~~~~

- community.crypto.parse_serial - Convert a serial number as a colon-separated list of hex numbers to an integer
- community.crypto.to_serial - Convert an integer to a colon-separated list of hex numbers
- community.general.lists_difference - Difference of lists with a predictive order
- community.general.lists_intersect - Intersection of lists with a predictive order
- community.general.lists_symmetric_difference - Symmetric Difference of lists with a predictive order
- community.general.lists_union - Union of lists with a predictive order

New Modules
-----------

community.general
~~~~~~~~~~~~~~~~~

- community.general.gitlab_group_access_token - Manages GitLab group access tokens
- community.general.gitlab_project_access_token - Manages GitLab project access tokens

containers.podman
~~~~~~~~~~~~~~~~~

- containers.podman.podman_secret_info - Secrets info module

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

netbox.netbox
~~~~~~~~~~~~~

- netbox.netbox.netbox_virtual_disk - Create, updates, or removes a disk from a Virtual Machine

Unchanged Collections
---------------------

- ansible.netcommon (still version 5.3.0)
- ansible.posix (still version 1.5.4)
- ansible.utils (still version 2.12.0)
- ansible.windows (still version 2.2.0)
- arista.eos (still version 6.2.2)
- azure.azcollection (still version 1.19.0)
- check_point.mgmt (still version 5.2.2)
- chocolatey.chocolatey (still version 1.5.1)
- cisco.aci (still version 2.8.0)
- cisco.asa (still version 4.0.3)
- cisco.intersight (still version 2.0.7)
- cisco.ios (still version 5.3.0)
- cisco.iosxr (still version 6.1.1)
- cisco.ise (still version 2.7.0)
- cisco.meraki (still version 2.17.2)
- cisco.mso (still version 2.5.0)
- cisco.nxos (still version 5.3.0)
- cisco.ucs (still version 1.10.0)
- cloud.common (still version 2.1.4)
- cloudscale_ch.cloud (still version 2.3.1)
- community.aws (still version 7.1.0)
- community.azure (still version 2.0.0)
- community.ciscosmb (still version 1.0.7)
- community.digitalocean (still version 1.26.0)
- community.hashi_vault (still version 6.1.0)
- community.hrobot (still version 1.9.0)
- community.library_inventory_filtering_v1 (still version 1.0.0)
- community.libvirt (still version 1.3.0)
- community.network (still version 5.0.2)
- community.okd (still version 2.3.0)
- community.proxysql (still version 1.5.1)
- community.rabbitmq (still version 1.2.3)
- community.sap (still version 2.0.0)
- community.sap_libs (still version 1.4.2)
- community.sops (still version 1.6.7)
- community.windows (still version 2.1.0)
- community.zabbix (still version 2.3.1)
- cyberark.conjur (still version 1.2.2)
- cyberark.pas (still version 1.0.25)
- dellemc.enterprise_sonic (still version 2.4.0)
- dellemc.openmanage (still version 8.7.0)
- dellemc.powerflex (still version 2.1.0)
- dellemc.unity (still version 1.7.1)
- frr.frr (still version 2.0.2)
- gluster.gluster (still version 1.0.2)
- google.cloud (still version 1.3.0)
- hpe.nimble (still version 1.1.4)
- ibm.qradar (still version 2.1.0)
- ibm.spectrum_virtualize (still version 2.0.0)
- ibm.storage_virtualize (still version 2.2.0)
- infoblox.nios_modules (still version 1.6.1)
- inspur.ispim (still version 2.2.0)
- inspur.sm (still version 2.3.0)
- junipernetworks.junos (still version 5.3.1)
- microsoft.ad (still version 1.4.1)
- netapp.aws (still version 21.7.1)
- netapp.azure (still version 21.10.1)
- netapp.cloudmanager (still version 21.22.1)
- netapp.elementsw (still version 21.7.0)
- netapp.um_info (still version 21.8.1)
- netapp_eseries.santricity (still version 1.4.0)
- ngine_io.cloudstack (still version 2.3.0)
- ngine_io.exoscale (still version 1.1.0)
- openstack.cloud (still version 2.2.0)
- openvswitch.openvswitch (still version 2.1.1)
- ovirt.ovirt (still version 3.2.0)
- purestorage.flasharray (still version 1.26.0)
- purestorage.flashblade (still version 1.15.0)
- sensu.sensu_go (still version 1.14.0)
- splunk.es (still version 2.1.2)
- t_systems_mms.icinga_director (still version 2.0.1)
- telekom_mms.icinga_director (still version 1.35.0)
- theforeman.foreman (still version 3.15.0)
- vmware.vmware_rest (still version 2.3.1)
- vultr.cloud (still version 1.12.1)
- vyos.vyos (still version 4.1.0)
- wti.remote (still version 1.0.5)

v9.2.0
======

.. contents::
  :local:
  :depth: 2

Release Summary
---------------

Release Date: 2024-01-30

`Porting Guide <https://docs.ansible.com/ansible/devel/porting_guides.html>`_

Added Collections
-----------------

- community.library_inventory_filtering_v1 (version 1.0.0)

Ansible-core
------------

Ansible 9.2.0 contains ansible-core version 2.16.3.
This is a newer version than version 2.16.1 contained in the previous Ansible release.

The changes are reported in the combined changelog below.

Changed Collections
-------------------

If not mentioned explicitly, the changes are reported in the combined changelog below.

+------------------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| Collection                               | Ansible 9.1.0 | Ansible 9.2.0 | Notes                                                                                                                        |
+==========================================+===============+===============+==============================================================================================================================+
| amazon.aws                               | 7.0.0         | 7.2.0         |                                                                                                                              |
+------------------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| awx.awx                                  | 23.5.0        | 23.6.0        | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+------------------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| check_point.mgmt                         | 5.1.1         | 5.2.2         |                                                                                                                              |
+------------------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.dnac                               | 6.8.1         | 6.10.2        | The collection did not have a changelog in this version.                                                                     |
+------------------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.intersight                         | 2.0.3         | 2.0.7         | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+------------------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.ise                                | 2.6.2         | 2.7.0         |                                                                                                                              |
+------------------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.meraki                             | 2.16.16       | 2.17.2        |                                                                                                                              |
+------------------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.aws                            | 7.0.0         | 7.1.0         |                                                                                                                              |
+------------------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.crypto                         | 2.16.1        | 2.17.1        |                                                                                                                              |
+------------------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.digitalocean                   | 1.24.0        | 1.26.0        |                                                                                                                              |
+------------------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.dns                            | 2.6.4         | 2.8.0         |                                                                                                                              |
+------------------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.docker                         | 3.4.11        | 3.7.0         |                                                                                                                              |
+------------------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.general                        | 8.1.0         | 8.3.0         |                                                                                                                              |
+------------------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.grafana                        | 1.6.1         | 1.7.0         |                                                                                                                              |
+------------------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.hashi_vault                    | 6.0.0         | 6.1.0         |                                                                                                                              |
+------------------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.hrobot                         | 1.8.2         | 1.9.0         |                                                                                                                              |
+------------------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.library_inventory_filtering_v1 |               | 1.0.0         | The collection was added to Ansible                                                                                          |
+------------------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.postgresql                     | 3.2.0         | 3.3.0         |                                                                                                                              |
+------------------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.routeros                       | 2.11.0        | 2.12.0        |                                                                                                                              |
+------------------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.sap_libs                       | 1.4.1         | 1.4.2         |                                                                                                                              |
+------------------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.vmware                         | 4.0.1         | 4.1.0         |                                                                                                                              |
+------------------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.zabbix                         | 2.2.0         | 2.3.1         |                                                                                                                              |
+------------------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cyberark.pas                             | 1.0.23        | 1.0.25        | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+------------------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| dellemc.enterprise_sonic                 | 2.2.0         | 2.4.0         |                                                                                                                              |
+------------------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| dellemc.openmanage                       | 8.5.0         | 8.7.0         |                                                                                                                              |
+------------------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| fortinet.fortimanager                    | 2.3.0         | 2.3.1         |                                                                                                                              |
+------------------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| grafana.grafana                          | 2.2.3         | 2.2.4         |                                                                                                                              |
+------------------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| ibm.storage_virtualize                   | 2.1.0         | 2.2.0         |                                                                                                                              |
+------------------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| infoblox.nios_modules                    | 1.5.0         | 1.6.1         |                                                                                                                              |
+------------------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| netapp.ontap                             | 22.8.3        | 22.9.0        |                                                                                                                              |
+------------------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| netbox.netbox                            | 3.15.0        | 3.16.0        |                                                                                                                              |
+------------------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| purestorage.flasharray                   | 1.24.0        | 1.26.0        |                                                                                                                              |
+------------------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| purestorage.flashblade                   | 1.14.0        | 1.15.0        |                                                                                                                              |
+------------------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| vultr.cloud                              | 1.10.1        | 1.12.1        |                                                                                                                              |
+------------------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+

Major Changes
-------------

community.docker
~~~~~~~~~~~~~~~~

- The ``community.docker`` collection now depends on the ``community.library_inventory_filtering_v1`` collection. This utility collection provides host filtering functionality for inventory plugins. If you use the Ansible community package, both collections are included and you do not have to do anything special. If you install the collection with ``ansible-galaxy collection install``, it will be installed automatically. If you install the collection by copying the files of the collection to a place where ansible-core can find it, for example by cloning the git repository, you need to make sure that you also have to install the dependency if you are using the inventory plugins (https://github.com/ansible-collections/community.docker/pull/698).

community.hashi_vault
~~~~~~~~~~~~~~~~~~~~~

- requirements - the ``requests`` package which is required by ``hvac`` now has a more restrictive range for this collection in certain use cases due to breaking security changes in ``ansible-core`` that were backported (https://github.com/ansible-collections/community.hashi_vault/pull/416).

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- All OME modules are enhanced to support the environment variables `OME_USERNAME` and `OME_PASSWORD` as fallback for credentials.
- All iDRAC and Redfish modules are enhanced to support the environment variables `IDRAC_USERNAME` and `IDRAC_PASSWORD` as fallback for credentials.
- idrac_certificates - The module is enhanced to support the import and export of `CUSTOMCERTIFICATE`.
- idrac_gather_facts - This role is enhanced to support secure boot.
- idrac_license - The module is introduced to configure iDRAC licenses.

infoblox.nios_modules
~~~~~~~~~~~~~~~~~~~~~

- Upgrade Ansible version support from 2.13 to 2.16.
- Upgrade Python version support from 3.8 to 3.10.

Minor Changes
-------------

amazon.aws
~~~~~~~~~~

- autoscaling_group - minor PEP8 whitespace sanity fixes (https://github.com/ansible-collections/amazon.aws/pull/1846).
- ec2_ami_info - simplify parameters to ``get_image_attribute`` to only pass ID of image (https://github.com/ansible-collections/amazon.aws/pull/1846).
- ec2_eip - use ``ResourceTags`` to set initial tags upon creation (https://github.com/ansible-collections/amazon.aws/issues/1843)
- ec2_instance - Add support for modifying metadata options of an existing instance (https://github.com/ansible-collections/amazon.aws/pull/1918).
- ec2_instance - add support for AdditionalInfo option when creating an instance (https://github.com/ansible-collections/amazon.aws/pull/1828).
- ec2_security_group - use ``ResourceTags`` to set initial tags upon creation (https://github.com/ansible-collections/amazon.aws/pull/1844)
- ec2_vpc_igw - use ``ResourceTags`` to set initial tags upon creation (https://github.com/ansible-collections/amazon.aws/issues/1843)
- ec2_vpc_route_table - use ``ResourceTags`` to set initial tags upon creation (https://github.com/ansible-collections/amazon.aws/issues/1843)
- ec2_vpc_subnet - the default value for ``tags`` has been changed from ``{}`` to ``None``, to remove tags from a subnet an empty map must be explicitly passed to the module (https://github.com/ansible-collections/amazon.aws/pull/1876).
- ec2_vpc_subnet - use ``ResourceTags`` to set initial tags upon creation (https://github.com/ansible-collections/amazon.aws/issues/1843)
- ec2_vpc_subnet - use ``wait_timeout`` to also control maximum time to wait for initial creation of subnets (https://github.com/ansible-collections/amazon.aws/pull/1848).
- iam_group - Basic testing of ``name`` and ``path`` has been added to improve error messages (https://github.com/ansible-collections/amazon.aws/pull/1933).
- iam_group - ``group_name`` has been added as an alias to ``name`` for consistency with other IAM modules (https://github.com/ansible-collections/amazon.aws/pull/1933).
- iam_group - add support for setting group path (https://github.com/ansible-collections/amazon.aws/pull/1892).
- iam_group - adds attached_policies return value (https://github.com/ansible-collections/amazon.aws/pull/1892).
- iam_group - code refactored to avoid single long function (https://github.com/ansible-collections/amazon.aws/pull/1892).
- iam_instance_profile - Basic testing of ``name`` and ``path`` has been added to improve error messages (https://github.com/ansible-collections/amazon.aws/pull/1933).
- iam_instance_profile - attempting to change the ``path`` for an existing profile will now generate a warning, previously this was silently ignored (https://github.com/ansible-collections/amazon.aws/pull/1933).
- iam_instance_profile - the ``prefix`` parameter has been renamed ``path`` for consistency with other IAM modules, ``prefix`` remains as an alias. No change to playbooks is required (https://github.com/ansible-collections/amazon.aws/pull/1933).
- iam_instance_profile - the default value for ``path`` has been removed.  New instances will still be created with a default path of ``/``. No change to playbooks is required (https://github.com/ansible-collections/amazon.aws/pull/1933).
- iam_managed_policy - Basic testing of ``name`` and ``path`` has been added to improve error messages (https://github.com/ansible-collections/amazon.aws/pull/1933).
- iam_managed_policy - ``description`` attempting to update the description now results in a warning, previously it was simply ignored (https://github.com/ansible-collections/amazon.aws/pull/1936).
- iam_managed_policy - ``policy`` is no longer a required parameter (https://github.com/ansible-collections/amazon.aws/pull/1936).
- iam_managed_policy - added support for tagging managed policies (https://github.com/ansible-collections/amazon.aws/pull/1936).
- iam_managed_policy - more consistently perform retries on rate limiting errors (https://github.com/ansible-collections/amazon.aws/pull/1936).
- iam_managed_policy - support for setting ``path`` (https://github.com/ansible-collections/amazon.aws/pull/1936).
- iam_managed_policy - the ``policy_description`` parameter has been renamed ``description`` for consistency with other IAM modules, ``policy_description`` remains as an alias. No change to playbooks is required (https://github.com/ansible-collections/amazon.aws/pull/1933).
- iam_managed_policy - the ``policy_name`` parameter has been renamed ``name`` for consistency with other IAM modules, ``policy_name`` remains as an alias. No change to playbooks is required (https://github.com/ansible-collections/amazon.aws/pull/1933).
- iam_role - Basic testing of ``name`` and ``path`` has been added to improve error messages (https://github.com/ansible-collections/amazon.aws/pull/1933).
- iam_role - ``prefix`` and ``path_prefix`` have been added as aliases to ``path`` for consistency with other IAM modules (https://github.com/ansible-collections/amazon.aws/pull/1933).
- iam_role - ``role_name`` has been added as an alias to ``name`` for consistency with other IAM modules (https://github.com/ansible-collections/amazon.aws/pull/1933).
- iam_role - attempting to change the ``path`` for an existing profile will now generate a warning, previously this was silently ignored (https://github.com/ansible-collections/amazon.aws/pull/1933).
- iam_role - the default value for ``path`` has been removed.  New roles will still be created with a default path of ``/``. No change to playbooks is required (https://github.com/ansible-collections/amazon.aws/pull/1933).
- iam_role_info - ``path`` and ``prefix`` have been added as aliases to ``path_prefix`` for consistency with other IAM modules (https://github.com/ansible-collections/amazon.aws/pull/1933).
- iam_user - Basic testing of ``name`` and ``path`` has been added to improve error messages (https://github.com/ansible-collections/amazon.aws/pull/1933).
- iam_user - ``user_name`` has been added as an alias to ``name`` for consistency with other IAM modules (https://github.com/ansible-collections/amazon.aws/pull/1933).
- iam_user - add ``boundary`` parameter to support managing boundary policy on users (https://github.com/ansible-collections/amazon.aws/pull/1912).
- iam_user - add ``path`` parameter to support managing user path (https://github.com/ansible-collections/amazon.aws/pull/1912).
- iam_user - added ``attached_policies`` to return value (https://github.com/ansible-collections/amazon.aws/pull/1912).
- iam_user - refactored code to reduce complexity (https://github.com/ansible-collections/amazon.aws/pull/1912).
- iam_user_info - ``prefix`` has been added as an alias to ``path_prefix`` for consistency with other IAM modules (https://github.com/ansible-collections/amazon.aws/pull/1933).
- iam_user_info - the ``path`` parameter has been renamed ``path_prefix`` for consistency with other IAM modules, ``path`` remains as an alias. No change to playbooks is required (https://github.com/ansible-collections/amazon.aws/pull/1933).
- rds_instance_snapshot - minor PEP8 whitespace sanity fixes (https://github.com/ansible-collections/amazon.aws/pull/1846).

check_point.mgmt
~~~~~~~~~~~~~~~~

- New resource modules for R81.20 JHF Take 43
- meta/runtime.yml - update minimum Ansible version required to 2.14.0.

cisco.ise
~~~~~~~~~

- cisco.ise collection now supports ansible.utils v3

cisco.meraki
~~~~~~~~~~~~

- Adding support to ansible.utils ">=2.0.0, <4.00".

community.aws
~~~~~~~~~~~~~

- aws_ssm - Updated the documentation to explicitly state that an S3 bucket is required, the behavior of the files in that bucket, and requirements around that. (https://github.com/ansible-collections/community.aws/issues/1775).
- cloudfront_distribution - added support for ``cache_policy_id`` and ``origin_request_policy_id`` for behaviors (https://github.com/ansible-collections/community.aws/pull/1589)
- mq_broker - add support to wait for broker state via ``wait`` and ``wait_timeout`` parameter values (https://github.com/ansible-collections/community.aws/pull/1879).

community.crypto
~~~~~~~~~~~~~~~~

- luks_device - add allow discards option (https://github.com/ansible-collections/community.crypto/pull/693).

community.digitalocean
~~~~~~~~~~~~~~~~~~~~~~

- digital_ocean_kubernetes - add project_name parameter (https://github.com/ansible-collections/community.digitalocean/issues/264).
- fix sanity tests (https://github.com/ansible-collections/community.digitalocean/issues/323).

community.dns
~~~~~~~~~~~~~

- hetzner_dns_records and hosttech_dns_records inventory plugins - the ``filters`` option has been renamed to ``simple_filters``. The old name still works until community.hrobot 2.0.0. Then it will change to allow more complex filtering with the ``community.library_inventory_filtering_v1`` collection's functionality (https://github.com/ansible-collections/community.dns/pull/181).
- nameserver_info and nameserver_record_info - add ``server`` parameter to specify custom DNS servers (https://github.com/ansible-collections/community.dns/pull/168, https://github.com/ansible-collections/community.dns/pull/178).
- wait_for_txt - add ``server`` parameter to specify custom DNS servers (https://github.com/ansible-collections/community.dns/pull/178).

community.docker
~~~~~~~~~~~~~~~~

- The ``ca_cert`` option available to almost all modules and plugins has been renamed to ``ca_path``. The name ``ca_path`` is also used for similar options in ansible-core and other collections. The old name has been added as an alias and can still be used (https://github.com/ansible-collections/community.docker/pull/744).
- The ``docker_stack*`` modules now use the common CLI-based module code added for the ``docker_image_build`` and ``docker_compose_v2`` modules. This means that the modules now have various more configuration options with respect to talking to the Docker Daemon, and now also are part of the ``community.docker.docker`` and ``docker`` module default groups (https://github.com/ansible-collections/community.docker/pull/745).
- docker_compose_v2 - add ``scale`` option to allow to explicitly scale services (https://github.com/ansible-collections/community.docker/pull/776).
- docker_compose_v2, docker_compose_v2_pull - support ``files`` parameter to specify multiple Compose files (https://github.com/ansible-collections/community.docker/issues/772, https://github.com/ansible-collections/community.docker/pull/775).
- docker_container - add ``networks[].mac_address`` option for Docker API 1.44+. Note that Docker API 1.44 no longer uses the global ``mac_address`` option, this new option is the only way to set the MAC address for a container (https://github.com/ansible-collections/community.docker/pull/763).
- docker_container - implement better ``platform`` string comparisons to improve idempotency (https://github.com/ansible-collections/community.docker/issues/654, https://github.com/ansible-collections/community.docker/pull/705).
- docker_container - internal refactorings which allow comparisons to use more information like details of the current image or the Docker host config (https://github.com/ansible-collections/community.docker/pull/713).
- docker_image - allow to specify labels and ``/dev/shm`` size when building images (https://github.com/ansible-collections/community.docker/issues/726, https://github.com/ansible-collections/community.docker/pull/727).
- docker_image - allow to specify memory size and swap memory size in other units than bytes (https://github.com/ansible-collections/community.docker/pull/727).
- inventory plugins - add ``filter`` option which allows to include and exclude hosts based on Jinja2 conditions (https://github.com/ansible-collections/community.docker/pull/698, https://github.com/ansible-collections/community.docker/issues/610).

community.general
~~~~~~~~~~~~~~~~~

- consul_auth_method, consul_binding_rule, consul_policy, consul_role, consul_session, consul_token - added action group ``community.general.consul`` (https://github.com/ansible-collections/community.general/pull/7897).
- consul_policy - added support for diff and check mode (https://github.com/ansible-collections/community.general/pull/7878).
- consul_policy, consul_role, consul_session - removed dependency on ``requests`` and factored out common parts (https://github.com/ansible-collections/community.general/pull/7826, https://github.com/ansible-collections/community.general/pull/7878).
- consul_role - ``node_identities`` now expects a ``node_name`` option to match the Consul API, the old ``name`` is still supported as alias (https://github.com/ansible-collections/community.general/pull/7878).
- consul_role - ``service_identities`` now expects a ``service_name`` option to match the Consul API, the old ``name`` is still supported as alias (https://github.com/ansible-collections/community.general/pull/7878).
- consul_role - added support for diff mode (https://github.com/ansible-collections/community.general/pull/7878).
- consul_role - added support for templated policies (https://github.com/ansible-collections/community.general/pull/7878).
- ipa_dnsrecord - adds ability to manage NS record types (https://github.com/ansible-collections/community.general/pull/7737).
- ipa_pwpolicy - refactor module and exchange a sequence ``if`` statements with a ``for`` loop (https://github.com/ansible-collections/community.general/pull/7723).
- ipa_pwpolicy - update module to support ``maxrepeat``, ``maxsequence``, ``dictcheck``, ``usercheck``, ``gracelimit`` parameters in FreeIPA password policies (https://github.com/ansible-collections/community.general/pull/7723).
- keycloak_realm_key - the ``config.algorithm`` option now supports 8 additional key algorithms (https://github.com/ansible-collections/community.general/pull/7698).
- keycloak_realm_key - the ``config.certificate`` option value is no longer defined with ``no_log=True`` (https://github.com/ansible-collections/community.general/pull/7698).
- keycloak_realm_key - the ``provider_id`` option now supports RSA encryption key usage (value ``rsa-enc``) (https://github.com/ansible-collections/community.general/pull/7698).
- keycloak_user_federation - allow custom user storage providers to be set through ``provider_id`` (https://github.com/ansible-collections/community.general/pull/7789).
- mail - add ``Message-ID`` header; which is required by some mail servers (https://github.com/ansible-collections/community.general/pull/7740).
- mail module, mail callback plugin - allow to configure the domain name of the Message-ID header with a new ``message_id_domain`` option (https://github.com/ansible-collections/community.general/pull/7765).
- redfish_info - add command ``GetServiceIdentification`` to get service identification (https://github.com/ansible-collections/community.general/issues/7882).
- ssh_config - new feature to set ``AddKeysToAgent`` option to ``yes`` or ``no`` (https://github.com/ansible-collections/community.general/pull/7703).
- ssh_config - new feature to set ``IdentitiesOnly`` option to ``yes`` or ``no`` (https://github.com/ansible-collections/community.general/pull/7704).
- terraform - add support for ``diff_mode`` for terraform resource_changes (https://github.com/ansible-collections/community.general/pull/7896).
- xcc_redfish_command - added support for raw POSTs (``command=PostResource`` in ``category=Raw``) without a specific action info (https://github.com/ansible-collections/community.general/pull/7746).

community.grafana
~~~~~~~~~~~~~~~~~

- Add Quickwit search engine datasource (https://quickwit.io).
- Add parameter `org_name` to `grafana_dashboard`
- Add parameter `org_name` to `grafana_datasource`
- Add parameter `org_name` to `grafana_organization_user`
- Add support for Grafana Tempo datasource type (https://grafana.com/docs/grafana/latest/datasources/tempo/)
- default to true/false in docs and code

community.hrobot
~~~~~~~~~~~~~~~~

- robot inventory plugin - the ``filters`` option has been renamed to ``simple_filters``. The old name still works until community.hrobot 2.0.0. Then it will change to allow more complex filtering with the ``community.library_inventory_filtering_v1`` collection's functionality (https://github.com/ansible-collections/community.hrobot/pull/94).

community.postgresql
~~~~~~~~~~~~~~~~~~~~

- postgresql_db - add the ``comment`` argument (https://github.com/ansible-collections/community.postgresql/issues/614).
- postgresql_ext - add the ``comment`` argument (https://github.com/ansible-collections/community.postgresql/issues/354).
- postgresql_publication - add the ``comment`` argument (https://github.com/ansible-collections/community.postgresql/issues/354).
- postgresql_schema - add the ``comment`` argument (https://github.com/ansible-collections/community.postgresql/issues/354).
- postgresql_subscription - add the ``comment`` argument (https://github.com/ansible-collections/community.postgresql/issues/354).
- postgresql_tablespace - add the ``comment`` argument (https://github.com/ansible-collections/community.postgresql/issues/354).

community.routeros
~~~~~~~~~~~~~~~~~~

- api_info, api_modify - add ``interface ovpn-client`` path (https://github.com/ansible-collections/community.routeros/issues/242, https://github.com/ansible-collections/community.routeros/pull/244).
- api_info, api_modify - add ``radius`` path (https://github.com/ansible-collections/community.routeros/issues/241, https://github.com/ansible-collections/community.routeros/pull/245).
- api_info, api_modify - add ``routing rule`` path (https://github.com/ansible-collections/community.routeros/issues/162, https://github.com/ansible-collections/community.routeros/pull/246).
- api_info, api_modify - add missing path ``routing bgp template`` (https://github.com/ansible-collections/community.routeros/pull/243).
- api_info, api_modify - add support for the ``tx-power`` attribute in ``interface wireless`` (https://github.com/ansible-collections/community.routeros/pull/239).
- api_info, api_modify - removed ``host`` primary key in ``tool netwatch`` path (https://github.com/ansible-collections/community.routeros/pull/248).
- api_modify, api_info - added support for ``interface wifiwave2`` (https://github.com/ansible-collections/community.routeros/pull/226).

community.vmware
~~~~~~~~~~~~~~~~

- vmware_guest - Add IPv6 support for VM network interfaces (https://github.com/ansible-collections/community.vmware/pull/1937).
- vmware_guest_sendkey - Add Windows key (https://github.com/ansible-collections/community.vmware/issues/1959).
- vmware_guest_tools_upgrade - Add parameter `installer_options` to pass command line options to the installer to modify the installation procedure for tools (https://github.com/ansible-collections/community.vmware/pull/1059).

community.zabbix
~~~~~~~~~~~~~~~~

- api_requests - Handled error from depricated CertificateError class
- multiple roles - Removed unneeded Apt Clean commands.
- proxy role - Updated MariaDB version for Centos 7 to 10.11
- zabbix web - Allowed the independent configuration of php-fpm without creating vhost.
- zabbix_host_info - added ability to get all the hosts configured in Zabbix
- zabbix_proxy role - Add variable zabbix_proxy_dbpassword_hash_method to control whether you want postgresql user password to be hashed with md5 or want to use db default. When zabbix_proxy_dbpassword_hash_method is set to anything other than md5 then do not hash the password with md5 so you could use postgresql scram-sha-256 hashing method.
- zabbix_server role - Add variable zabbix_server_dbpassword_hash_method to control whether you want postgresql user password to be hashed with md5 or want to use db default. When zabbix_server_dbpassword_hash_method is set to anything other than md5 then do not hash the password with md5 so you could use postgresql scram-sha-256 hashing method.
- zabbix_templategroup module added

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

- For idrac_certificate role, added support for import operation of `HTTPS` certificate with the SSL key.
- For idrac_certificates module, below enhancements are made: Added support for import operation of `HTTPS` certificate with the SSL key. The `email_address` has been made as an optional parameter.
- For idrac_gather_facts role, added storage controller details in the role output.

grafana.grafana
~~~~~~~~~~~~~~~

- Bump cryptography from 41.0.4 to 41.0.6 by @dependabot in https://github.com/grafana/grafana-ansible-collection/pull/126
- Drop curl check by @v-zhuravlev in https://github.com/grafana/grafana-ansible-collection/pull/120
- Fix check mode for grafana role by @Boschung-Mecatronic-AG-Infrastructure in https://github.com/grafana/grafana-ansible-collection/pull/125
- Fix check mode in Grafana Agent by @AmandaCameron in https://github.com/grafana/grafana-ansible-collection/pull/124
- Update tags in README by @ishanjainn in https://github.com/grafana/grafana-ansible-collection/pull/121

ibm.storage_virtualize
~~~~~~~~~~~~~~~~~~~~~~

- ibm_sv_manage_replication_policy - Added support to configure a 2-site-ha policy.
- ibm_sv_manage_snapshot - Added support to restore entire volumegroup from a snapshot of that volumegroup.
- ibm_svc_host - Added support to create nvmetcp host.
- ibm_svc_info - Added support to display information about thinclone/clone volumes and volumegroups.
- ibm_svc_manage_volumgroup - Added support to delete volumegroups keeping volumes via 'evictvolumes'.

netapp.ontap
~~~~~~~~~~~~

- na_ontap_cifs_server - new option `lm_compatibility_level` added in REST, requires ONTAP 9.8 or later.
- na_ontap_cluster - new option `certificate.uuid` added in REST, requires ONTAP 9.10 or later.
- na_ontap_cluster_peer - added REST only support for modifying remote intercluster addresses in cluster peer relation.
- na_ontap_ems_destination - new options `syslog`, `port`, `transport`, `message_format`, `timestamp_format_override` and `hostname_format_override` added in REST, requires ONTAP 9.12.1 or later.
- na_ontap_s3_services - create, modify S3 service returns `s3_service_info` in module output.
- na_ontap_snapmirror - updated resync and resume operation for synchronous snapmirror relationship in REST.

netbox.netbox
~~~~~~~~~~~~~

- nb_inventory - Add facility group_by option [#1059](https://github.com/netbox-community/ansible_modules/pull/1059)
- nb_inventory - Enable ansible-vault strings in config-context data [#1114](https://github.com/netbox-community/ansible_modules/pull/1114)
- netbox_platform - Add config_template option to netbox_platform [#1119](https://github.com/netbox-community/ansible_modules/pull/1119)
- netbox_power_port_template - Add option module_type to netbox_power_port_template [#1105](https://github.com/netbox-community/ansible_modules/pull/1105)

purestorage.flasharray
~~~~~~~~~~~~~~~~~~~~~~

- all - ``distro`` package added as a pre-requisite
- multiple - Remove packaging pre-requisite.
- multiple - Where only REST 2.x endpoints are used, convert to REST 2.x methodology.
- purefa_info - Expose NFS security flavor for policies
- purefa_info - Expose cloud capacity details if array is a Cloud Block Store.
- purefa_policy - Add SMB user based enumeration parameter
- purefa_policy - Added NFS security flavors for accessing files in the mount point.
- purefa_policy - Remove default setting for nfs_version to allow for change of version at policy level

purestorage.flashblade
~~~~~~~~~~~~~~~~~~~~~~

- purefb_bucket - Add support for public buckets
- purefb_bucket - From REST 2.12 the `mode` parameter default changes to `multi-site-writable`.
- purefb_fs - Added SMB Continuous Availability parameter. Requires REST 2.12 or higher.
- purefb_info - Added enhanced information for buckets, filesystems and snapshots, based on new features in REST 2.12
- purefb_s3acc - Add support for public buckets
- purefb_s3acc - Remove default requirements for ``hard_limit`` and ``default_hard_limit``

vultr.cloud
~~~~~~~~~~~

- Added retry on HTTP 504 returned by the API (https://github.com/vultr/ansible-collection-vultr/pull/104).
- Implemented a feature to distinguish resources by region if available. This allows to have identical name per region e.g. a VPC named ``default`` in each region. (https://github.com/vultr/ansible-collection-vultr/pull/98).
- instance - Added a new param ``user_scheme`` to change user scheme to non-root on Linux while creating the instance (https://github.com/vultr/ansible-collection-vultr/issues/96).

Deprecated Features
-------------------

community.dns
~~~~~~~~~~~~~

- hetzner_dns_records and hosttech_dns_records inventory plugins - the ``filters`` option has been renamed to ``simple_filters``. The old name will stop working in community.hrobot 2.0.0 (https://github.com/ansible-collections/community.dns/pull/181).

community.docker
~~~~~~~~~~~~~~~~

- docker_container - the default ``ignore`` for the ``image_name_mismatch`` parameter has been deprecated and will switch to ``recreate`` in community.docker 4.0.0. A deprecation warning will be printed in situations where the default value is used and where a behavior would change once the default changes (https://github.com/ansible-collections/community.docker/pull/703).

community.general
~~~~~~~~~~~~~~~~~

- consul_acl - the module has been deprecated and will be removed in community.general 10.0.0. ``consul_token`` and ``consul_policy`` can be used instead (https://github.com/ansible-collections/community.general/pull/7901).

community.hrobot
~~~~~~~~~~~~~~~~

- robot inventory plugin - the ``filters`` option has been renamed to ``simple_filters``. The old name will stop working in community.hrobot 2.0.0 (https://github.com/ansible-collections/community.hrobot/pull/94).

Security Fixes
--------------

Ansible-core
~~~~~~~~~~~~

- ANSIBLE_NO_LOG - Address issue where ANSIBLE_NO_LOG was ignored (CVE-2024-0690)

Bugfixes
--------

Ansible-core
~~~~~~~~~~~~

- Run all handlers with the same ``listen`` topic, even when notified from another handler (https://github.com/ansible/ansible/issues/82363).
- ``ansible-galaxy role import`` - fix using the ``role_name`` in a standalone role's ``galaxy_info`` metadata by disabling automatic removal of the ``ansible-role-`` prefix. This matches the behavior of the Galaxy UI which also no longer implicitly removes the ``ansible-role-`` prefix. Use the ``--role-name`` option or add a ``role_name`` to the ``galaxy_info`` dictionary in the role's ``meta/main.yml`` to use an alternate role name.
- ``ansible-test sanity --test runtime-metadata`` - add ``action_plugin`` as a valid field for modules in the schema (https://github.com/ansible/ansible/pull/82562).
- ansible-config init will now dedupe ini entries from plugins.
- ansible-galaxy role import - exit with 1 when the import fails (https://github.com/ansible/ansible/issues/82175).
- ansible-galaxy role install - normalize tarfile paths and symlinks using ``ansible.utils.path.unfrackpath`` and consider them valid as long as the realpath is in the tarfile's role directory (https://github.com/ansible/ansible/issues/81965).
- delegate_to when set to an empty or undefined variable will now give a proper error.
- dwim functions for lookups should be better at detectging role context even in abscense of tasks/main.
- roles, code cleanup and performance optimization of dependencies, now cached,  and ``public`` setting is now determined once, at role instantiation.
- roles, the ``static`` property is now correctly set, this will fix issues with ``public`` and ``DEFAULT_PRIVATE_ROLE_VARS`` controls on exporting vars.
- unsafe data - Address an incompatibility when iterating or getting a single index from ``AnsibleUnsafeBytes``
- unsafe data - Address an incompatibility with ``AnsibleUnsafeText`` and ``AnsibleUnsafeBytes`` when pickling with ``protocol=0``
- unsafe data - Enable directly using ``AnsibleUnsafeText`` with Python ``pathlib`` (https://github.com/ansible/ansible/issues/82414)

amazon.aws
~~~~~~~~~~

- ec2_vpc_subnet - cleanly handle failure when subnet isn't created in time (https://github.com/ansible-collections/amazon.aws/pull/1848).
- iam_managed_policy - fixed an issue where only partial results were returned (https://github.com/ansible-collections/amazon.aws/pull/1936).
- s3_object - Fix typo that caused false deprecation warning when setting ``overwrite=latest`` (https://github.com/ansible-collections/amazon.aws/pull/1847).
- s3_object - when doing a put and specifying ``Content-Type`` in metadata, this module (since 6.0.0) erroneously set the ``Content-Type`` to ``None`` causing the put to fail. Fix now correctly honours the specified ``Content-Type`` (https://github.com/ansible-collections/amazon.aws/issues/1881).

check_point.mgmt
~~~~~~~~~~~~~~~~

- httpapi/checkpoint.py - Raise a fatal error if login wasn't successful.

cisco.meraki
~~~~~~~~~~~~

- Adding `smartquotes = False` to `conf.py` and romoving `'` from rst files.
- Adding build_ignore property to galaxy file.
- Adding support to ansible.utils >=3.0

community.aws
~~~~~~~~~~~~~

- aws_ssm - disable `enable-bracketed-paste` to fix issue with amazon linux 2023 and other OSes (https://github.com/ansible-collections/community.aws/issues/1756)

community.crypto
~~~~~~~~~~~~~~~~

- acme_* modules - directly react on bad return data for account creation/retrieval/updating requests (https://github.com/ansible-collections/community.crypto/pull/682).
- acme_* modules - fix improved error reporting in case of socket errors, bad status lines, and unknown connection errors (https://github.com/ansible-collections/community.crypto/pull/684).
- acme_* modules - increase number of retries from 5 to 10 to increase stability with unstable ACME endpoints (https://github.com/ansible-collections/community.crypto/pull/685).
- acme_* modules - make account registration handling more flexible to accept 404 instead of 400 send by DigiCert's ACME endpoint when an account does not exist (https://github.com/ansible-collections/community.crypto/pull/681).
- openssl_dhparam - was using an internal function instead of the public API to load DH param files when using the ``cryptography`` backend. The internal function was removed in cryptography 42.0.0. The module now uses the public API, which has been available since support for DH params was added to cryptography (https://github.com/ansible-collections/community.crypto/pull/698).
- openssl_privatekey_info - ``check_consistency=true`` no longer works for RSA keys with cryptography 42.0.0+ (https://github.com/ansible-collections/community.crypto/pull/701).
- openssl_privatekey_info - ``check_consistency=true`` now reports a warning if it cannot determine consistency (https://github.com/ansible-collections/community.crypto/pull/705).

community.digitalocean
~~~~~~~~~~~~~~~~~~~~~~

- The C(project_name) parameter for many modules was used by alias C(project) internally in the codebase, but to work properly C(project_name) must be used in the code. Replace self.module.params.get("project") with self.module.params.get("project_name") (https://github.com/ansible-collections/community.digitalocean/issues/326).
- digital_ocean_kubernetes - module didn't return kubeconfig properly, return documentation was invalid. Fixed version returns data with the same structure all the time, also it is aligned with M(community.digitalocean.digital_ocean_kubernetes_info) documentation return data now. (https://github.com/ansible-collections/community.digitalocean/issues/322).
- inventory plugin - restore reading auth token from env variables (https://github.com/ansible-collections/community.digitalocean/pull/315).

community.dns
~~~~~~~~~~~~~

- Update Public Suffix List.
- wait_for_txt, nameserver_info, nameserver_record_info - when looking up nameservers for a domain, do not treat ``NXDOMAIN`` as a fatal error (https://github.com/ansible-collections/community.dns/pull/177).

community.docker
~~~~~~~~~~~~~~~~

- Use ``unix:///var/run/docker.sock`` instead of the legacy ``unix://var/run/docker.sock`` as default for ``docker_host`` (https://github.com/ansible-collections/community.docker/pull/736).
- docker_compose_v2 - properly parse dry-run build events from ``stderr`` (https://github.com/ansible-collections/community.docker/issues/778, https://github.com/ansible-collections/community.docker/pull/779).
- docker_compose_v2_pull - the module was documented as part of the ``community.docker.docker`` action group, but was not actually part of it. That has now been fixed (https://github.com/ansible-collections/community.docker/pull/773).
- docker_image - fix archiving idempotency with Docker API 1.44 or later (https://github.com/ansible-collections/community.docker/pull/765).
- modules and plugins using the Docker SDK for Python - remove ``ssl_version`` from the parameters passed to Docker SDK for Python 7.0.0+. Explicitly fail with a nicer error message if it was explicitly set in this case (https://github.com/ansible-collections/community.docker/pull/715).
- modules and plugins using the Docker SDK for Python - remove ``tls_hostname`` from the parameters passed to Docker SDK for Python 7.0.0+. Explicitly fail with a nicer error message if it was explicitly set in this case (https://github.com/ansible-collections/community.docker/pull/721).
- vendored Docker SDK for Python - avoid passing on ``ssl_version`` and ``tls_hostname`` if they were not provided by the user. Remove dead code. (https://github.com/ansible-collections/community.docker/pull/722).

community.general
~~~~~~~~~~~~~~~~~

- homebrew - detect already installed formulae and casks using JSON output from ``brew info`` (https://github.com/ansible-collections/community.general/issues/864).
- incus connection plugin - treats ``inventory_hostname`` as a variable instead of a literal in remote connections (https://github.com/ansible-collections/community.general/issues/7874).
- ipa_otptoken - the module expect ``ipatokendisabled`` as string but the ``ipatokendisabled`` value is returned as a boolean (https://github.com/ansible-collections/community.general/pull/7795).
- keycloak_identity_provider - ``mappers`` processing was not idempotent if the mappers configuration list had not been sorted by name (in ascending order). Fix resolves the issue by sorting mappers in the desired state using the same key which is used for obtaining existing state (https://github.com/ansible-collections/community.general/pull/7418).
- keycloak_identity_provider - it was not possible to reconfigure (add, remove) ``mappers`` once they were created initially. Removal was ignored, adding new ones resulted in dropping the pre-existing unmodified mappers. Fix resolves the issue by supplying correct input to the internal update call (https://github.com/ansible-collections/community.general/pull/7418).
- keycloak_user - when ``force`` is set, but user does not exist, do not try to delete it (https://github.com/ansible-collections/community.general/pull/7696).
- ldap - previously the order number (if present) was expected to follow an equals sign in the DN. This makes it so the order number string is identified correctly anywhere within the DN (https://github.com/ansible-collections/community.general/issues/7646).
- mssql_script - make the module work with Python 2 (https://github.com/ansible-collections/community.general/issues/7818, https://github.com/ansible-collections/community.general/pull/7821).
- nmcli - fix ``connection.slave-type`` wired to ``bond`` and not with parameter ``slave_type`` in case of connection type ``wifi`` (https://github.com/ansible-collections/community.general/issues/7389).
- proxmox - fix updating a container config if the setting does not already exist (https://github.com/ansible-collections/community.general/pull/7872).
- proxmox_kvm - running ``state=template`` will first check whether VM is already a template (https://github.com/ansible-collections/community.general/pull/7792).
- statusio_maintenance - fix error caused by incorrectly formed API data payload. Was raising "Failed to create maintenance HTTP Error 400 Bad Request" caused by bad data type for date/time and deprecated dict keys (https://github.com/ansible-collections/community.general/pull/7754).

community.grafana
~~~~~~~~~~~~~~~~~

- Add `grafana_organiazion_user` to `action_groups.grafana`
- Fixed orgId handling in diff comparison for `grafana_datasource` if using org_name

community.postgresql
~~~~~~~~~~~~~~~~~~~~

- postgresql_query - now reports not changed for queries starting with "SHOW" (https://github.com/ansible-collections/community.postgresql/pull/592).
- postgresql_user - module failed when running against an SQL_ASCII encoded database as the user's current password was returned as bytes as opposed to a str. Fix now checks for this case and decodes the bytes as an ascii encoded string. (https://github.com/ansible-collections/community.postgresql/issues/584).

community.sap_libs
~~~~~~~~~~~~~~~~~~

- fixes failures in sanity test for all modules

community.vmware
~~~~~~~~~~~~~~~~

- Fix InsecureRequestWarning for modules based on the VmwareRestClient module util when setting ``validate_certs`` to ``False`` (https://github.com/ansible-collections/community.vmware/pull/1969).
- module_utils/vmware.py - remove ssl.wrap_socet() function. Replaced for code based on ssl.get_server_certificate (https://github.com/ansible-collections/community.vmware/issues/1930).
- vmware_guest - Fix failure of vm reconfiguration with enabled virt_based_security (https://github.com/ansible-collections/community.vmware/pull/1848).

community.zabbix
~~~~~~~~~~~~~~~~

- Avoid to update user-directory configuration in dry run.
- api module - Fixed certificiate errors
- proxy and server roles - Defaulted location of fping and fping6 based on OS.
- proxy role - Removed requirement for mysql group definition.
- server role - typo in configuration var StasAllowedIP to StatsAllowedIP
- zabbix-{agent, javagateway, proxy, server, web} - support raspberry pi without repository url specification

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

- Fixed the issue for ignoring the environment variable `NO_PROXY` earlier. (https://github.com/dell/dellemc-openmanage-ansible-modules/issues/554)
- For idrac_certificates module, the `email_address` has been made as an optional parameter. (https://github.com/dell/dellemc-openmanage-ansible-modules/issues/582).
- Issue is fixed for deploying a new configuration on quick deploy slot when IPv6 is disabled.(https://github.com/dell/dellemc-openmanage-ansible-modules/issues/533)

fortinet.fortimanager
~~~~~~~~~~~~~~~~~~~~~

- Added missing enum values for some arguments.
- Change minimum required ansible-core version to 2.14.0
- Fixed a bug where ansible may skip update incorrectly.
- Support FortiManager 7.0.10

infoblox.nios_modules
~~~~~~~~~~~~~~~~~~~~~

- Fixes environment variable max_results using INFOBLOX_MAX_RESULTS `#209 <https://github.com/infobloxopen/infoblox-ansible/pull/209>`_
- Fixes index error for transform fields in DTC LBDN (auth_zone and Pool) and DTC POOL (servers and monitors) `#209 <https://github.com/infobloxopen/infoblox-ansible/pull/209>`_
- Fixes typo for environment variable INFOBLOX_WAPI_VERSION `#209 <https://github.com/infobloxopen/infoblox-ansible/pull/209>`_

netapp.ontap
~~~~~~~~~~~~

- na_ontap_nfs - fix error with `windows` in REST for ONTAP 9.10 or earlier.
- na_ontap_security_certificates - fix error with ontap_info returned in module output in REST.
- na_ontap_snapshot_policy - fix issue with modifying snapshot policy in REST.
- na_ontap_volume - modified `type` to be case insensitive in REST.

netbox.netbox
~~~~~~~~~~~~~

- Improve error reporting for missing module [#1126](https://github.com/netbox-community/ansible_modules/pull/1126)
- nb_inventory - Fix API cache failure [#1111](https://github.com/netbox-community/ansible_modules/pull/1111)
- nb_lookup - Allow multiple IDs in nb_lookup [#1042](https://github.com/netbox-community/ansible_modules/pull/1042)

purestorage.flasharray
~~~~~~~~~~~~~~~~~~~~~~

- purefa_ds - Fix issue with SDK returning empty data for data directory services even when it does exist
- purefa_policy - Fix incorrect call of psot instead of patch for NFS policies

purestorage.flashblade
~~~~~~~~~~~~~~~~~~~~~~

- purefb_info - Added missing object lock retention details if enabledd

vultr.cloud
~~~~~~~~~~~

- Fixed an error while waiting for a specific state and the API returns an empty response. (https://github.com/vultr/ansible-collection-vultr/issues/108).
- Fixed an issue with waiting for state (https://github.com/vultr/ansible-collection-vultr/pull/102).
- instance_info - Fixed the alias ``name`` being was used on the wrong argument. (https://github.com/vultr/ansible-collection-vultr/issues/105).
- reserved_ip - Fixed an issue which caused the module to fail, also enabled integration tests (https://github.com/vultr/ansible-collection-vultr/issues/92).

Known Issues
------------

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- idrac_firmware - Issue(279282) - This module does not support firmware update using HTTP, HTTPS, and FTP shares with authentication on iDRAC8.
- idrac_network_attributes - Issue(279049) -  If unsupported values are provided for the parameter ``ome_network_attributes``, then this module does not provide a correct error message.
- ome_device_network_services - Issue(212681) - The module does not provide a proper error message if unsupported values are provided for the following parameters- port_number, community_name, max_sessions, max_auth_retries, and idle_timeout.
- ome_device_power_settings - Issue(212679) - The module displays the following message if the value provided for the parameter ``power_cap`` is not within the supported range of 0 to 32767, ``Unable to complete the request because PowerCap does not exist or is not applicable for the resource URI.``
- ome_device_quick_deploy - Issue(275231) - This module does not deploy a new configuration to a slot that has disabled IPv6.
- ome_diagnostics - Issue(279193) - Export of SupportAssist collection logs to the share location fails on OME version 4.0.0.
- ome_smart_fabric_uplink - Issue(186024) - The module supported by OpenManage Enterprise Modular, however it does not allow the creation of multiple uplinks of the same name. If an uplink is created using the same name as an existing uplink, then the existing uplink is modified.

New Plugins
-----------

Connection
~~~~~~~~~~

- community.general.incus - Run tasks in Incus instances via the Incus CLI.

Filter
~~~~~~

- community.general.from_ini - Converts INI text input into a dictionary
- community.general.to_ini - Converts a dictionary to the INI file format

Lookup
~~~~~~

- community.general.github_app_access_token - Obtain short-lived Github App Access tokens

New Modules
-----------

check_point.mgmt
~~~~~~~~~~~~~~~~

- check_point.mgmt.cp_mgmt_add_central_license - Add central license.
- check_point.mgmt.cp_mgmt_central_license_facts - Get central-license objects facts on Checkpoint over Web Services API.
- check_point.mgmt.cp_mgmt_delete_central_license - Delete central license.
- check_point.mgmt.cp_mgmt_distribute_cloud_licenses - Distribute licenses to target CloudGuard gateways.
- check_point.mgmt.cp_mgmt_show_cloud_licenses_usage - Show attached licenses usage.
- check_point.mgmt.cp_mgmt_show_ha_status - Retrieve domain high availability status.

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

- community.general.consul_acl_bootstrap - Bootstrap ACLs in Consul
- community.general.consul_auth_method - Manipulate Consul auth methods
- community.general.consul_binding_rule - Manipulate Consul binding rules
- community.general.consul_token - Manipulate Consul tokens
- community.general.dnf_config_manager - Enable or disable dnf repositories using config-manager
- community.general.gitlab_label - Creates/updates/deletes GitLab Labels belonging to project or group.
- community.general.gitlab_milestone - Creates/updates/deletes GitLab Milestones belonging to project or group
- community.general.keycloak_component_info - Retrive component info in Keycloak
- community.general.keycloak_realm_rolemapping - Allows administration of Keycloak realm role mappings into groups with the Keycloak API
- community.general.proxmox_node_info - Retrieve information about one or more Proxmox VE nodes
- community.general.proxmox_storage_contents_info - List content from a Proxmox VE storage

dellemc.enterprise_sonic
~~~~~~~~~~~~~~~~~~~~~~~~

- dellemc.enterprise_sonic.sonic_dhcp_snooping - Manage DHCP Snooping on SONiC
- dellemc.enterprise_sonic.sonic_pki - Manages PKI attributes of Enterprise Sonic
- dellemc.enterprise_sonic.sonic_stp - Manage STP configuration on SONiC

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- dellemc.openmanage.idrac_license - This module allows to import, export, and delete licenses on iDRAC.

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

purestorage.flashblade
~~~~~~~~~~~~~~~~~~~~~~

- purestorage.flashblade.purefb_hardware - Manage FlashBlade Hardware

vultr.cloud
~~~~~~~~~~~

- vultr.cloud.object_storage - Manages object storages on Vultr

Unchanged Collections
---------------------

- ansible.netcommon (still version 5.3.0)
- ansible.posix (still version 1.5.4)
- ansible.utils (still version 2.12.0)
- ansible.windows (still version 2.2.0)
- arista.eos (still version 6.2.2)
- azure.azcollection (still version 1.19.0)
- chocolatey.chocolatey (still version 1.5.1)
- cisco.aci (still version 2.8.0)
- cisco.asa (still version 4.0.3)
- cisco.ios (still version 5.3.0)
- cisco.iosxr (still version 6.1.1)
- cisco.mso (still version 2.5.0)
- cisco.nxos (still version 5.3.0)
- cisco.ucs (still version 1.10.0)
- cloud.common (still version 2.1.4)
- cloudscale_ch.cloud (still version 2.3.1)
- community.azure (still version 2.0.0)
- community.ciscosmb (still version 1.0.7)
- community.libvirt (still version 1.3.0)
- community.mongodb (still version 1.6.3)
- community.mysql (still version 3.8.0)
- community.network (still version 5.0.2)
- community.okd (still version 2.3.0)
- community.proxysql (still version 1.5.1)
- community.rabbitmq (still version 1.2.3)
- community.sap (still version 2.0.0)
- community.sops (still version 1.6.7)
- community.windows (still version 2.1.0)
- containers.podman (still version 1.11.0)
- cyberark.conjur (still version 1.2.2)
- dellemc.powerflex (still version 2.1.0)
- dellemc.unity (still version 1.7.1)
- f5networks.f5_modules (still version 1.27.1)
- fortinet.fortios (still version 2.3.4)
- frr.frr (still version 2.0.2)
- gluster.gluster (still version 1.0.2)
- google.cloud (still version 1.3.0)
- hetzner.hcloud (still version 2.4.1)
- hpe.nimble (still version 1.1.4)
- ibm.qradar (still version 2.1.0)
- ibm.spectrum_virtualize (still version 2.0.0)
- infinidat.infinibox (still version 1.3.12)
- inspur.ispim (still version 2.2.0)
- inspur.sm (still version 2.3.0)
- junipernetworks.junos (still version 5.3.1)
- kubernetes.core (still version 2.4.0)
- lowlydba.sqlserver (still version 2.2.2)
- microsoft.ad (still version 1.4.1)
- netapp.aws (still version 21.7.1)
- netapp.azure (still version 21.10.1)
- netapp.cloudmanager (still version 21.22.1)
- netapp.elementsw (still version 21.7.0)
- netapp.storagegrid (still version 21.11.1)
- netapp.um_info (still version 21.8.1)
- netapp_eseries.santricity (still version 1.4.0)
- ngine_io.cloudstack (still version 2.3.0)
- ngine_io.exoscale (still version 1.1.0)
- openstack.cloud (still version 2.2.0)
- openvswitch.openvswitch (still version 2.1.1)
- ovirt.ovirt (still version 3.2.0)
- purestorage.fusion (still version 1.6.0)
- sensu.sensu_go (still version 1.14.0)
- splunk.es (still version 2.1.2)
- t_systems_mms.icinga_director (still version 2.0.1)
- telekom_mms.icinga_director (still version 1.35.0)
- theforeman.foreman (still version 3.15.0)
- vmware.vmware_rest (still version 2.3.1)
- vyos.vyos (still version 4.1.0)
- wti.remote (still version 1.0.5)

v9.1.0
======

.. contents::
  :local:
  :depth: 2

Release Summary
---------------

Release Date: 2023-12-05

`Porting Guide <https://docs.ansible.com/ansible/devel/porting_guides.html>`_

Ansible-core
------------

Ansible 9.1.0 contains ansible-core version 2.16.1.
This is a newer version than version 2.16.0 contained in the previous Ansible release.

The changes are reported in the combined changelog below.

Changed Collections
-------------------

If not mentioned explicitly, the changes are reported in the combined changelog below.

+-----------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| Collection                  | Ansible 9.0.1 | Ansible 9.1.0 | Notes                                                                                                                        |
+=============================+===============+===============+==============================================================================================================================+
| ansible.utils               | 2.11.0        | 2.12.0        |                                                                                                                              |
+-----------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| ansible.windows             | 2.1.0         | 2.2.0         |                                                                                                                              |
+-----------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| arista.eos                  | 6.2.1         | 6.2.2         |                                                                                                                              |
+-----------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| awx.awx                     | 23.3.1        | 23.5.0        | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+-----------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.dnac                  | 6.7.6         | 6.8.1         | The collection did not have a changelog in this version.                                                                     |
+-----------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.ios                   | 5.2.0         | 5.3.0         |                                                                                                                              |
+-----------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.iosxr                 | 6.1.0         | 6.1.1         |                                                                                                                              |
+-----------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.ise                   | 2.5.16        | 2.6.2         |                                                                                                                              |
+-----------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.meraki                | 2.16.14       | 2.16.16       |                                                                                                                              |
+-----------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.nxos                  | 5.2.1         | 5.3.0         |                                                                                                                              |
+-----------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.crypto            | 2.16.0        | 2.16.1        |                                                                                                                              |
+-----------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.dns               | 2.6.3         | 2.6.4         |                                                                                                                              |
+-----------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.general           | 8.0.2         | 8.1.0         |                                                                                                                              |
+-----------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.routeros          | 2.10.0        | 2.11.0        |                                                                                                                              |
+-----------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.vmware            | 4.0.0         | 4.0.1         |                                                                                                                              |
+-----------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.windows           | 2.0.0         | 2.1.0         |                                                                                                                              |
+-----------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.zabbix            | 2.1.0         | 2.2.0         |                                                                                                                              |
+-----------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| dellemc.openmanage          | 8.4.0         | 8.5.0         |                                                                                                                              |
+-----------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| dellemc.powerflex           | 2.0.1         | 2.1.0         |                                                                                                                              |
+-----------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| f5networks.f5_modules       | 1.27.0        | 1.27.1        |                                                                                                                              |
+-----------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| google.cloud                | 1.2.0         | 1.3.0         |                                                                                                                              |
+-----------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| hetzner.hcloud              | 2.3.0         | 2.4.1         |                                                                                                                              |
+-----------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| inspur.ispim                | 2.1.0         | 2.2.0         |                                                                                                                              |
+-----------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| junipernetworks.junos       | 5.3.0         | 5.3.1         |                                                                                                                              |
+-----------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| microsoft.ad                | 1.3.0         | 1.4.1         |                                                                                                                              |
+-----------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| netapp.ontap                | 22.8.2        | 22.8.3        |                                                                                                                              |
+-----------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| openstack.cloud             | 2.1.0         | 2.2.0         | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+-----------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| purestorage.flasharray      | 1.22.0        | 1.24.0        |                                                                                                                              |
+-----------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| splunk.es                   | 2.1.0         | 2.1.2         |                                                                                                                              |
+-----------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| telekom_mms.icinga_director | 1.34.1        | 1.35.0        |                                                                                                                              |
+-----------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| theforeman.foreman          | 3.14.0        | 3.15.0        |                                                                                                                              |
+-----------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| vultr.cloud                 | 1.10.0        | 1.10.1        |                                                                                                                              |
+-----------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+

Minor Changes
-------------

ansible.utils
~~~~~~~~~~~~~

- Fact_diff filter plugin - Add fact_diff filter plugin. (https://github.com/ansible-collections/ansible.utils/issues/78).

ansible.windows
~~~~~~~~~~~~~~~

- Set minimum supported Ansible version to 2.14 to align with the versions still supported by Ansible.
- win_share - Added a new param called ``scope_name`` that allows file shares to be scoped for Windows Server failover cluster roles.

cisco.ios
~~~~~~~~~

- Added ios_evpn_evi resource module.
- Added ios_evpn_global resource module.
- Added ios_vxlan_vtep resource module.
- Fixed ios_evpn_evi resource module integration test failure - code to remove VLAN config.
- ios_bgp_address_family - Fixed an issue with inherit peer-policy CLI
- ios_bgp_address_family - added 'advertise' key
- ios_vlans - added vlan config CLI feature.
- ios_vrf - added MDT related keys

cisco.ise
~~~~~~~~~

- Services included configuration, edda, dataconnect_services, subscriber.

cisco.nxos
~~~~~~~~~~

- nxos_config - Relax restrictions on I(src) parameter so it can be used more like I(lines). (https://github.com/ansible-collections/cisco.nxos/issues/89).

community.general
~~~~~~~~~~~~~~~~~

- bitwarden lookup plugin - when looking for items using an item ID, the item is now accessed directly with ``bw get item`` instead of searching through all items. This doubles the lookup speed (https://github.com/ansible-collections/community.general/pull/7468).
- elastic callback plugin - close elastic client to not leak resources (https://github.com/ansible-collections/community.general/pull/7517).
- git_config - allow multiple git configs for the same name with the new ``add_mode`` option (https://github.com/ansible-collections/community.general/pull/7260).
- git_config - the ``after`` and ``before`` fields in the ``diff`` of the return value can be a list instead of a string in case more configs with the same key are affected (https://github.com/ansible-collections/community.general/pull/7260).
- git_config - when a value is unset, all configs with the same key are unset (https://github.com/ansible-collections/community.general/pull/7260).
- gitlab modules - add ``ca_path`` option (https://github.com/ansible-collections/community.general/pull/7472).
- gitlab modules - remove duplicate ``gitlab`` package check (https://github.com/ansible-collections/community.general/pull/7486).
- gitlab_runner - add support for new runner creation workflow (https://github.com/ansible-collections/community.general/pull/7199).
- ipa_config - adds ``passkey`` choice to ``ipauserauthtype`` parameter's choices (https://github.com/ansible-collections/community.general/pull/7588).
- ipa_sudorule - adds options to include denied commands or command groups (https://github.com/ansible-collections/community.general/pull/7415).
- ipa_user - adds ``idp`` and ``passkey`` choice to ``ipauserauthtype`` parameter's choices (https://github.com/ansible-collections/community.general/pull/7589).
- irc - add ``validate_certs`` option, and rename ``use_ssl`` to ``use_tls``, while keeping ``use_ssl`` as an alias. The default value for ``validate_certs`` is ``false`` for backwards compatibility. We recommend to every user of this module to explicitly set ``use_tls=true`` and `validate_certs=true`` whenever possible, especially when communicating to IRC servers over the internet (https://github.com/ansible-collections/community.general/pull/7550).
- keycloak module utils - expose error message from Keycloak server for HTTP errors in some specific situations (https://github.com/ansible-collections/community.general/pull/7645).
- keycloak_user_federation - add option for ``krbPrincipalAttribute`` (https://github.com/ansible-collections/community.general/pull/7538).
- lvol - change ``pvs`` argument type to list of strings (https://github.com/ansible-collections/community.general/pull/7676, https://github.com/ansible-collections/community.general/issues/7504).
- lxd connection plugin - tighten the detection logic for lxd ``Instance not found`` errors, to avoid false detection on unrelated errors such as ``/usr/bin/python3: not found`` (https://github.com/ansible-collections/community.general/pull/7521).
- netcup_dns - adds support for record types ``OPENPGPKEY``, ``SMIMEA``, and ``SSHFP`` (https://github.com/ansible-collections/community.general/pull/7489).
- nmcli - add support for new connection type ``loopback`` (https://github.com/ansible-collections/community.general/issues/6572).
- nmcli - allow for ``infiniband`` slaves of ``bond`` interface types (https://github.com/ansible-collections/community.general/pull/7569).
- nmcli - allow for the setting of ``MTU`` for ``infiniband`` and ``bond`` interface types (https://github.com/ansible-collections/community.general/pull/7499).
- onepassword lookup plugin - support 1Password Connect with the opv2 client by setting the connect_host and connect_token parameters (https://github.com/ansible-collections/community.general/pull/7116).
- onepassword_raw lookup plugin - support 1Password Connect with the opv2 client by setting the connect_host and connect_token parameters (https://github.com/ansible-collections/community.general/pull/7116)
- passwordstore - adds ``timestamp`` and ``preserve`` parameters to modify the stored password format (https://github.com/ansible-collections/community.general/pull/7426).
- proxmox - adds ``template`` value to the ``state`` parameter, allowing conversion of container to a template (https://github.com/ansible-collections/community.general/pull/7143).
- proxmox - adds ``update`` parameter, allowing update of an already existing containers configuration (https://github.com/ansible-collections/community.general/pull/7540).
- proxmox inventory plugin - adds an option to exclude nodes from the dynamic inventory generation. The new setting is optional, not using this option will behave as usual (https://github.com/ansible-collections/community.general/issues/6714, https://github.com/ansible-collections/community.general/pull/7461).
- proxmox_disk - add ability to manipulate CD-ROM drive (https://github.com/ansible-collections/community.general/pull/7495).
- proxmox_kvm - adds ``template`` value to the ``state`` parameter, allowing conversion of a VM to a template (https://github.com/ansible-collections/community.general/pull/7143).
- proxmox_kvm - support the ``hookscript`` parameter (https://github.com/ansible-collections/community.general/issues/7600).
- proxmox_ostype - it is now possible to specify the ``ostype`` when creating an LXC container (https://github.com/ansible-collections/community.general/pull/7462).
- proxmox_vm_info - add ability to retrieve configuration info (https://github.com/ansible-collections/community.general/pull/7485).
- redfish_info - adding the ``BootProgress`` property when getting ``Systems`` info (https://github.com/ansible-collections/community.general/pull/7626).
- ssh_config - adds ``controlmaster``, ``controlpath`` and ``controlpersist`` parameters (https://github.com/ansible-collections/community.general/pull/7456).

community.routeros
~~~~~~~~~~~~~~~~~~

- api_info, api_modify - add missing DoH parameters ``doh-max-concurrent-queries``, ``doh-max-server-connections``, and ``doh-timeout`` to the ``ip dns`` path (https://github.com/ansible-collections/community.routeros/issues/230, https://github.com/ansible-collections/community.routeros/pull/235)
- api_info, api_modify - add missing parameters ``address-list``, ``address-list-timeout``, ``randomise-ports``, and ``realm`` to subpaths of the ``ip firewall`` path (https://github.com/ansible-collections/community.routeros/issues/236, https://github.com/ansible-collections/community.routeros/pull/237).
- api_info, api_modify - mark the ``interface wireless`` parameter ``running`` as read-only (https://github.com/ansible-collections/community.routeros/pull/233).
- api_info, api_modify - set the default value to ``false`` for the  ``disabled`` parameter in some more paths where it can be seen in the documentation (https://github.com/ansible-collections/community.routeros/pull/237).
- api_modify - add missing ``comment`` attribute to ``/routing id`` (https://github.com/ansible-collections/community.routeros/pull/234).
- api_modify - add missing attributes to the ``routing bgp connection`` path (https://github.com/ansible-collections/community.routeros/pull/234).
- api_modify - add versioning to the ``/tool e-mail`` path (RouterOS 7.12 release) (https://github.com/ansible-collections/community.routeros/pull/234).
- api_modify - make ``/ip traffic-flow target`` a multiple value attribute (https://github.com/ansible-collections/community.routeros/pull/234).

community.windows
~~~~~~~~~~~~~~~~~

- Set minimum supported Ansible version to 2.14 to align with the versions still supported by Ansible.

community.zabbix
~~~~~~~~~~~~~~~~

- Added zabbix_group_events_info module
- action module - Added notify_if_canceled property
- agent and proxy roles - Set default `zabbix_api_server_port` to 80 or 443 based on `zabbix_api_use_ssl`
- agent role - Removed duplicative Windows agent task
- agent role - Standardized default yum priority to 99
- all roles - Re-added ability to override Debian repo source
- all roles - Updated Debian repository format to 822 standard
- various - updated testing modules
- various - updated to fully qualified module names
- zabbix agent - Added capability to add additional configuration includes
- zabbix_api_info module added
- zabbix_user module - add current_passwd optional parameter to enable password updating of the currently logged in user (https://www.zabbix.com/documentation/6.4/en/manual/api/reference/user/update)

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- Ansible lint issues are fixed for the collections.
- Module ``redfish_storage_volume`` is enhanced to support reboot options and job tracking operation.

dellemc.powerflex
~~~~~~~~~~~~~~~~~

- Added support for PowerFlex Denver version(4.5.x) to TB and Config role.

f5networks.f5_modules
~~~~~~~~~~~~~~~~~~~~~

- bigiq_device_discovery - Changes in documentation related to Provider block

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

hetzner.hcloud
~~~~~~~~~~~~~~

- Add the `hetzner.hcloud.all` group to configure all the modules using `module_defaults`.
- Allow to set the `api_endpoint` module argument using the `HCLOUD_ENDPOINT` environment variable.
- Removed the `hcloud_` prefix from all modules names, e.g. `hetzner.hcloud.hcloud_firewall` was renamed to `hetzner.hcloud.firewall`. Old module names will continue working.
- Renamed the `endpoint` module argument to `api_endpoint`, backward compatibility is maintained using an alias.
- hcloud inventory - Add the `api_endpoint` option.
- hcloud inventory - Deprecate the `api_token_env` option, suggest using a lookup plugin (`{{ lookup('ansible.builtin.env', 'YOUR_ENV_VAR') }}`) or use the well-known `HCLOUD_TOKEN` environment variable name.
- hcloud inventory - Rename the `token_env` option to `api_token_env`, use aliases for backward compatibility.
- hcloud inventory - Rename the `token` option to `api_token`, use aliases for backward compatibility.

inspur.ispim
~~~~~~~~~~~~

- Modify edit_smtp_com and add description information.

microsoft.ad
~~~~~~~~~~~~

- Make ``name`` an optional parameter for the AD modules. Either ``name`` or ``identity`` needs to be set with their respective behaviours. If creating a new AD user and only ``identity`` is set, that will be the value used for the name of the object.
- Set minimum supported Ansible version to 2.14 to align with the versions still supported by Ansible.
- object_info - Add ActiveDirectory module import

purestorage.flasharray
~~~~~~~~~~~~~~~~~~~~~~

- purefa_dns - Added facility to add a CA certifcate to management DNS and check peer.
- purefa_info - Add NSID value for NVMe namespace in `hosts` response
- purefa_info - Subset `pgroups` now also provides a new dict called `deleted_pgroups`
- purefa_offload - Remove `nfs` as an option when Purity//FA 6.6.0 or higher is detected
- purefa_snap - Add support for suffix on remote offload snapshots

telekom_mms.icinga_director
~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Extended docs and examples for multiple assign_filter conditions (https://github.com/telekom-mms/ansible-collection-icinga-director/pull/227)

theforeman.foreman
~~~~~~~~~~~~~~~~~~

- content_view_publish role - allow passing ``async`` and ``poll`` to the module (https://github.com/theforeman/foreman-ansible-modules/pull/1676)
- convert2rhel role - install ``convert2rhel`` from ``cdn-public.redhat.com``, dropping the requirement of a custom CA cert

Breaking Changes / Porting Guide
--------------------------------

Ansible-core
~~~~~~~~~~~~

- assert - Nested templating may result in an inability for the conditional to be evaluated. See the porting guide for more information.

Security Fixes
--------------

Ansible-core
~~~~~~~~~~~~

- templating - Address issues where internal templating can cause unsafe variables to lose their unsafe designation (CVE-2023-5764)

Bugfixes
--------

Ansible-core
~~~~~~~~~~~~

- Fix issue where an ``include_tasks`` handler in a role was not able to locate a file in ``tasks/`` when ``tasks_from`` was used as a role entry point and ``main.yml`` was not present (https://github.com/ansible/ansible/issues/82241)
- Plugin loader does not dedupe nor cache filter/test plugins by file basename, but full path name.
- Restoring the ability of filters/tests can have same file base name but different tests/filters defined inside.
- ansible-pull now will expand relative paths for the ``-d|--directory`` option is now expanded before use.
- ansible-pull will now correctly handle become and connection password file options for ansible-playbook.
- flush_handlers - properly handle a handler failure in a nested block when ``force_handlers`` is set (http://github.com/ansible/ansible/issues/81532)
- module no_log will no longer affect top level booleans, for example ``no_log_module_parameter='a'`` will no longer hide ``changed=False`` as a 'no log value' (matches 'a').
- role params now have higher precedence than host facts again, matching documentation, this had unintentionally changed in 2.15.
- wait_for should not handle 'non mmapable files' again.

ansible.windows
~~~~~~~~~~~~~~~

- Process.cs - Fix up the ``ProcessCreationFlags.CreateProtectedProcess`` typo in the enum name
- setup - Fix up typo ``collection -> collect`` when a timeout occurred during a fact subset
- win_acl - Fix broken path in case of volume junction
- win_service_info - Warn and not fail if ERROR_FILE_NOT_FOUND when trying to query a service - https://github.com/ansible-collections/ansible.windows/issues/556
- win_updates - Fix up typo for Download progress event messages - https://github.com/ansible-collections/ansible.windows/issues/554

arista.eos
~~~~~~~~~~

- correct the reference of string attribute 'reference_bandwith'.

cisco.ios
~~~~~~~~~

- Updated the ios_ping ping module to support size param.
- ios_acls - make sequence optional for rendering of standard acls.
- ios_bgp_global - Explicitly add neighbor address to every parser.
- ios_bgp_global - remote_as not mendatory for neighbors.
- ios_vrf - added MDT related keys

cisco.iosxr
~~~~~~~~~~~

- Fix issue in gathered state of interfaces and l3_interfaces RMs(https://github.com/ansible-collections/cisco.iosxr/issues/452, https://github.com/ansible-collections/cisco.iosxr/issues/451)

cisco.ise
~~~~~~~~~

- Added missing import re in endpoint module
- Updated to use ciscoisesdk v2.1.1 or newer fixing ciscoisesdk problem.

cisco.meraki
~~~~~~~~~~~~

- Adding `network_clients_info` and `network_client_info`.
- Adding `platform_meraki.rst` to docs.
- Adding `product_types` for update request on networks.
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

community.crypto
~~~~~~~~~~~~~~~~

- acme_* modules - also retry requests in case of socket errors, bad status lines, and unknown connection errors; improve error messages in these cases (https://github.com/ansible-collections/community.crypto/issues/680).

community.dns
~~~~~~~~~~~~~

- Update Public Suffix List.
- nameserver_record_info - fix crash when more than one record is retrieved (https://github.com/ansible-collections/community.dns/pull/172).

community.general
~~~~~~~~~~~~~~~~~

- apt-rpm - the module did not upgrade packages if a newer version exists. Now the package will be reinstalled if the candidate is newer than the installed version (https://github.com/ansible-collections/community.general/issues/7414).
- cloudflare_dns - fix Cloudflare lookup of SHFP records (https://github.com/ansible-collections/community.general/issues/7652).
- interface_files - also consider ``address_family`` when changing ``option=method`` (https://github.com/ansible-collections/community.general/issues/7610, https://github.com/ansible-collections/community.general/pull/7612).
- irc - replace ``ssl.wrap_socket`` that was removed from Python 3.12 with code for creating a proper SSL context (https://github.com/ansible-collections/community.general/pull/7542).
- keycloak_* - fix Keycloak API client to quote ``/`` properly (https://github.com/ansible-collections/community.general/pull/7641).
- keycloak_authz_permission - resource payload variable for scope-based permission was constructed as a string, when it needs to be a list, even for a single item (https://github.com/ansible-collections/community.general/issues/7151).
- log_entries callback plugin - replace ``ssl.wrap_socket`` that was removed from Python 3.12 with code for creating a proper SSL context (https://github.com/ansible-collections/community.general/pull/7542).
- lvol - test for output messages in both ``stdout`` and ``stderr`` (https://github.com/ansible-collections/community.general/pull/7601, https://github.com/ansible-collections/community.general/issues/7182).
- onepassword lookup plugin - field and section titles are now case insensitive when using op CLI version two or later. This matches the behavior of version one (https://github.com/ansible-collections/community.general/pull/7564).
- redhat_subscription - use the D-Bus registration on RHEL 7 only on 7.4 and
  greater; older versions of RHEL 7 do not have it
  (https://github.com/ansible-collections/community.general/issues/7622,
  https://github.com/ansible-collections/community.general/pull/7624).
- terraform - fix multiline string handling in complex variables (https://github.com/ansible-collections/community.general/pull/7535).

community.vmware
~~~~~~~~~~~~~~~~

- vmware_vm_info - Fix an AttributeError when gathering network information (https://github.com/ansible-collections/community.vmware/pull/1919).

community.windows
~~~~~~~~~~~~~~~~~

- Remove some code which is no longer valid for dotnet 5+
- community.windows.win_psmodule_info - exception thrown when host has no Installed Module. Fix now checks that variable $installedModules is not null before calling the .Contains(..) function on it.
- win_rabbitmq_plugin - Avoid using ``Invoke-Expression`` when running external commands
- win_rds_rap - The module crashed when creating a RAP with Gateway Managed Computer Group (https://github.com/ansible-collections/community.windows/issues/184).

community.zabbix
~~~~~~~~~~~~~~~~

- zabbix_inventory - fixed handeling of add_zabbix_groups option
- zabbix_template - fix template export when template's content has "error" word
- zabbix_web role - fix variable naming issues (undefined) to zabbix_web_version and zabbix_web_apt_repository

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- ome_inventory - The plugin returns 50 results when a group is specified. No results are shown when a group is not specified. (https://github.com/dell/dellemc-openmanage-ansible-modules/issues/575).

hetzner.hcloud
~~~~~~~~~~~~~~

- hcloud inventory - Ensure the API client use a new cache for every *cached session*.

junipernetworks.junos
~~~~~~~~~~~~~~~~~~~~~

- fix to gather l2_interfaces facts with default port-mode access.

microsoft.ad
~~~~~~~~~~~~

- debug_ldap_client - handle failures when attempting to get the krb5 context and default CCache rather than fail with a traceback

netapp.ontap
~~~~~~~~~~~~

- na_ontap_ems_destination - fix field error with `certificate.name` for ONTAP 9.11.1 or later in REST.
- na_ontap_vserver_peer - fix issue with peering multiple clusters with same vserver name in REST.

purestorage.flasharray
~~~~~~~~~~~~~~~~~~~~~~

- purefa_cert - Fixed issue where parts of the subject where not included in the CSR if they did not exist in the currently used cert.
- purefa_dns - Fixed attribute error on deletion of management DNS
- purefa_pg - Allows a protection group to be correctly created when `target` is specified as well as other objects, such as `volumes` or `hosts`
- purefa_pgsched - Fixed issue with disabling schedules
- purefa_pgsnap - Fixed incorrect parameter name

splunk.es
~~~~~~~~~

- Fixed argspec validation for plugins with empty task attributes when run with Ansible 2.9.

theforeman.foreman
~~~~~~~~~~~~~~~~~~

- content_view_filter_rule - handle multiple rules for the same package but different architectures and versions correctly (https://bugzilla.redhat.com/show_bug.cgi?id=2189687)

vultr.cloud
~~~~~~~~~~~

- instance - Fixed an issue detecting the instance state returned by the API (https://github.com/vultr/ansible-collection-vultr/pull/89).

Known Issues
------------

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- idrac_firmware - Issue(279282) - This module does not support firmware update using HTTP, HTTPS, and FTP shares with authentication on iDRAC8.
- idrac_network_attributes - Issue(279049) -  If unsupported values are provided for the parameter ``ome_network_attributes``, then this module does not provide a correct error message.
- ome_device_network_services - Issue(212681) - The module does not provide a proper error message if unsupported values are provided for the following parameters- port_number, community_name, max_sessions, max_auth_retries, and idle_timeout.
- ome_device_power_settings - Issue(212679) - The module displays the following message if the value provided for the parameter ``power_cap`` is not within the supported range of 0 to 32767, ``Unable to complete the request because PowerCap does not exist or is not applicable for the resource URI.``
- ome_device_quick_deploy - Issue(275231) - This module does not deploy a new configuration to a slot that has disabled IPv6.
- ome_diagnostics - Issue(279193) - Export of SupportAssist collection logs to the share location fails on OME version 4.0.0.
- ome_smart_fabric_uplink - Issue(186024) - The module supported by OpenManage Enterprise Modular, however it does not allow the creation of multiple uplinks of the same name. If an uplink is created using the same name as an existing uplink, then the existing uplink is modified.

New Plugins
-----------

Filter
~~~~~~

- ansible.utils.fact_diff - Find the difference between currently set facts

Lookup
~~~~~~

- community.general.onepassword_doc - Fetch documents stored in 1Password

Test
~~~~

- community.general.fqdn_valid - Validates fully-qualified domain names against RFC 1123

New Modules
-----------

cisco.ios
~~~~~~~~~

- cisco.ios.ios_evpn_evi - Resource module to configure L2VPN EVPN EVI.
- cisco.ios.ios_evpn_global - Resource module to configure L2VPN EVPN.
- cisco.ios.ios_vxlan_vtep - Resource module to configure VXLAN VTEP interface.

community.general
~~~~~~~~~~~~~~~~~

- community.general.git_config_info - Read git configuration
- community.general.gitlab_issue - Create, update, or delete GitLab issues
- community.general.nomad_token - Manage Nomad ACL tokens

purestorage.flasharray
~~~~~~~~~~~~~~~~~~~~~~

- purestorage.flasharray.purefa_hardware - Manage FlashArray Hardware Identification

Unchanged Collections
---------------------

- amazon.aws (still version 7.0.0)
- ansible.netcommon (still version 5.3.0)
- ansible.posix (still version 1.5.4)
- azure.azcollection (still version 1.19.0)
- check_point.mgmt (still version 5.1.1)
- chocolatey.chocolatey (still version 1.5.1)
- cisco.aci (still version 2.8.0)
- cisco.asa (still version 4.0.3)
- cisco.intersight (still version 2.0.3)
- cisco.mso (still version 2.5.0)
- cisco.ucs (still version 1.10.0)
- cloud.common (still version 2.1.4)
- cloudscale_ch.cloud (still version 2.3.1)
- community.aws (still version 7.0.0)
- community.azure (still version 2.0.0)
- community.ciscosmb (still version 1.0.7)
- community.digitalocean (still version 1.24.0)
- community.docker (still version 3.4.11)
- community.grafana (still version 1.6.1)
- community.hashi_vault (still version 6.0.0)
- community.hrobot (still version 1.8.2)
- community.libvirt (still version 1.3.0)
- community.mongodb (still version 1.6.3)
- community.mysql (still version 3.8.0)
- community.network (still version 5.0.2)
- community.okd (still version 2.3.0)
- community.postgresql (still version 3.2.0)
- community.proxysql (still version 1.5.1)
- community.rabbitmq (still version 1.2.3)
- community.sap (still version 2.0.0)
- community.sap_libs (still version 1.4.1)
- community.sops (still version 1.6.7)
- containers.podman (still version 1.11.0)
- cyberark.conjur (still version 1.2.2)
- cyberark.pas (still version 1.0.23)
- dellemc.enterprise_sonic (still version 2.2.0)
- dellemc.unity (still version 1.7.1)
- fortinet.fortimanager (still version 2.3.0)
- fortinet.fortios (still version 2.3.4)
- frr.frr (still version 2.0.2)
- gluster.gluster (still version 1.0.2)
- grafana.grafana (still version 2.2.3)
- hpe.nimble (still version 1.1.4)
- ibm.qradar (still version 2.1.0)
- ibm.spectrum_virtualize (still version 2.0.0)
- ibm.storage_virtualize (still version 2.1.0)
- infinidat.infinibox (still version 1.3.12)
- infoblox.nios_modules (still version 1.5.0)
- inspur.sm (still version 2.3.0)
- kubernetes.core (still version 2.4.0)
- lowlydba.sqlserver (still version 2.2.2)
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
- openvswitch.openvswitch (still version 2.1.1)
- ovirt.ovirt (still version 3.2.0)
- purestorage.flashblade (still version 1.14.0)
- purestorage.fusion (still version 1.6.0)
- sensu.sensu_go (still version 1.14.0)
- t_systems_mms.icinga_director (still version 2.0.1)
- vmware.vmware_rest (still version 2.3.1)
- vyos.vyos (still version 4.1.0)
- wti.remote (still version 1.0.5)

v9.0.1
======

.. contents::
  :local:
  :depth: 2

Release Summary
---------------

Release Date: 2023-11-21

`Porting Guide <https://docs.ansible.com/ansible/devel/porting_guides.html>`_

Ansible-core
------------

Ansible 9.0.1 contains ansible-core version 2.16.0.
This is the same version of ansible-core as in the previous Ansible release.

Bugfixes
--------

- Fix the Python package metadata in ``setup.cfg`` to require Python ``>=3.10`` to ensure that pip can properly install ``ansible`` on older Python versions.

Unchanged Collections
---------------------

- amazon.aws (still version 7.0.0)
- ansible.netcommon (still version 5.3.0)
- ansible.posix (still version 1.5.4)
- ansible.utils (still version 2.11.0)
- ansible.windows (still version 2.1.0)
- arista.eos (still version 6.2.1)
- awx.awx (still version 23.3.1)
- azure.azcollection (still version 1.19.0)
- check_point.mgmt (still version 5.1.1)
- chocolatey.chocolatey (still version 1.5.1)
- cisco.aci (still version 2.8.0)
- cisco.asa (still version 4.0.3)
- cisco.dnac (still version 6.7.6)
- cisco.intersight (still version 2.0.3)
- cisco.ios (still version 5.2.0)
- cisco.iosxr (still version 6.1.0)
- cisco.ise (still version 2.5.16)
- cisco.meraki (still version 2.16.14)
- cisco.mso (still version 2.5.0)
- cisco.nxos (still version 5.2.1)
- cisco.ucs (still version 1.10.0)
- cloud.common (still version 2.1.4)
- cloudscale_ch.cloud (still version 2.3.1)
- community.aws (still version 7.0.0)
- community.azure (still version 2.0.0)
- community.ciscosmb (still version 1.0.7)
- community.crypto (still version 2.16.0)
- community.digitalocean (still version 1.24.0)
- community.dns (still version 2.6.3)
- community.docker (still version 3.4.11)
- community.general (still version 8.0.2)
- community.grafana (still version 1.6.1)
- community.hashi_vault (still version 6.0.0)
- community.hrobot (still version 1.8.2)
- community.libvirt (still version 1.3.0)
- community.mongodb (still version 1.6.3)
- community.mysql (still version 3.8.0)
- community.network (still version 5.0.2)
- community.okd (still version 2.3.0)
- community.postgresql (still version 3.2.0)
- community.proxysql (still version 1.5.1)
- community.rabbitmq (still version 1.2.3)
- community.routeros (still version 2.10.0)
- community.sap (still version 2.0.0)
- community.sap_libs (still version 1.4.1)
- community.sops (still version 1.6.7)
- community.vmware (still version 4.0.0)
- community.windows (still version 2.0.0)
- community.zabbix (still version 2.1.0)
- containers.podman (still version 1.11.0)
- cyberark.conjur (still version 1.2.2)
- cyberark.pas (still version 1.0.23)
- dellemc.enterprise_sonic (still version 2.2.0)
- dellemc.openmanage (still version 8.4.0)
- dellemc.powerflex (still version 2.0.1)
- dellemc.unity (still version 1.7.1)
- f5networks.f5_modules (still version 1.27.0)
- fortinet.fortimanager (still version 2.3.0)
- fortinet.fortios (still version 2.3.4)
- frr.frr (still version 2.0.2)
- gluster.gluster (still version 1.0.2)
- google.cloud (still version 1.2.0)
- grafana.grafana (still version 2.2.3)
- hetzner.hcloud (still version 2.3.0)
- hpe.nimble (still version 1.1.4)
- ibm.qradar (still version 2.1.0)
- ibm.spectrum_virtualize (still version 2.0.0)
- ibm.storage_virtualize (still version 2.1.0)
- infinidat.infinibox (still version 1.3.12)
- infoblox.nios_modules (still version 1.5.0)
- inspur.ispim (still version 2.1.0)
- inspur.sm (still version 2.3.0)
- junipernetworks.junos (still version 5.3.0)
- kubernetes.core (still version 2.4.0)
- lowlydba.sqlserver (still version 2.2.2)
- microsoft.ad (still version 1.3.0)
- netapp.aws (still version 21.7.1)
- netapp.azure (still version 21.10.1)
- netapp.cloudmanager (still version 21.22.1)
- netapp.elementsw (still version 21.7.0)
- netapp.ontap (still version 22.8.2)
- netapp.storagegrid (still version 21.11.1)
- netapp.um_info (still version 21.8.1)
- netapp_eseries.santricity (still version 1.4.0)
- netbox.netbox (still version 3.15.0)
- ngine_io.cloudstack (still version 2.3.0)
- ngine_io.exoscale (still version 1.1.0)
- openstack.cloud (still version 2.1.0)
- openvswitch.openvswitch (still version 2.1.1)
- ovirt.ovirt (still version 3.2.0)
- purestorage.flasharray (still version 1.22.0)
- purestorage.flashblade (still version 1.14.0)
- purestorage.fusion (still version 1.6.0)
- sensu.sensu_go (still version 1.14.0)
- splunk.es (still version 2.1.0)
- t_systems_mms.icinga_director (still version 2.0.1)
- telekom_mms.icinga_director (still version 1.34.1)
- theforeman.foreman (still version 3.14.0)
- vmware.vmware_rest (still version 2.3.1)
- vultr.cloud (still version 1.10.0)
- vyos.vyos (still version 4.1.0)
- wti.remote (still version 1.0.5)

v9.0.0
======

.. contents::
  :local:
  :depth: 2

Release Summary
---------------

[YANKED] Release Date: 2023-11-21 `Porting Guide <https://docs.ansible.com/ansible/devel/porting_guides.html>`_

Removed Collections
-------------------

- cisco.nso (previously included version: 1.0.3)
- community.fortios (previously included version: 1.0.0)
- community.google (previously included version: 1.0.0)
- community.skydive (previously included version: 1.0.0)
- ngine_io.vultr (previously included version: 1.1.3)
- servicenow.servicenow (previously included version: 1.0.6)

Added Collections
-----------------

- ibm.storage_virtualize (version 2.1.0)
- telekom_mms.icinga_director (version 1.34.1)

Ansible-core
------------

Ansible 9.0.0 contains ansible-core version 2.16.0.
This is a newer version than version 2.15.0 contained in the previous Ansible release.

The changes are reported in the combined changelog below.

Included Collections
--------------------

If not mentioned explicitly, the changes are reported in the combined changelog below.

+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Collection                    | Ansible 8.0.0 | Ansible 9.0.0 | Notes                                                                                                                                                                                                          |
+===============================+===============+===============+================================================================================================================================================================================================================+
| amazon.aws                    | 6.0.1         | 7.0.0         |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ansible.netcommon             | 5.1.1         | 5.3.0         |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ansible.utils                 | 2.10.3        | 2.11.0        |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ansible.windows               | 1.14.0        | 2.1.0         |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| arista.eos                    | 6.0.1         | 6.2.1         |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| awx.awx                       | 22.2.0        | 23.3.1        | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.                                                                                   |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| azure.azcollection            | 1.15.0        | 1.19.0        | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.                                                                                   |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| check_point.mgmt              | 5.0.0         | 5.1.1         |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| chocolatey.chocolatey         | 1.4.0         | 1.5.1         |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cisco.aci                     | 2.6.0         | 2.8.0         |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cisco.asa                     | 4.0.0         | 4.0.3         |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cisco.dnac                    | 6.7.2         | 6.7.6         | The collection did not have a changelog in this version.                                                                                                                                                       |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cisco.intersight              | 1.0.27        | 2.0.3         | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.                                                                                   |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cisco.ios                     | 4.5.0         | 5.2.0         |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cisco.iosxr                   | 5.0.2         | 6.1.0         |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cisco.ise                     | 2.5.12        | 2.5.16        |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cisco.meraki                  | 2.15.1        | 2.16.14       |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cisco.mso                     | 2.4.0         | 2.5.0         |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cisco.nxos                    | 4.3.0         | 5.2.1         |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cisco.ucs                     | 1.8.0         | 1.10.0        | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.                                                                                   |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cloud.common                  | 2.1.3         | 2.1.4         |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cloudscale_ch.cloud           | 2.2.4         | 2.3.1         |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.aws                 | 6.0.0         | 7.0.0         |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.ciscosmb            | 1.0.5         | 1.0.7         |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.crypto              | 2.13.1        | 2.16.0        |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.digitalocean        | 1.23.0        | 1.24.0        |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.dns                 | 2.5.4         | 2.6.3         |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.docker              | 3.4.6         | 3.4.11        |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.general             | 7.0.1         | 8.0.2         |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.grafana             | 1.5.4         | 1.6.1         |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.hashi_vault         | 5.0.0         | 6.0.0         |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.hrobot              | 1.8.0         | 1.8.2         |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.libvirt             | 1.2.0         | 1.3.0         |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.mongodb             | 1.5.2         | 1.6.3         | There are no changes recorded in the changelog.                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.mysql               | 3.7.1         | 3.8.0         |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.network             | 5.0.0         | 5.0.2         |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.postgresql          | 2.4.1         | 3.2.0         |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.routeros            | 2.8.0         | 2.10.0        |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.sap                 | 1.0.0         | 2.0.0         |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.sops                | 1.6.1         | 1.6.7         |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.vmware              | 3.6.0         | 4.0.0         |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.windows             | 1.13.0        | 2.0.0         |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.zabbix              | 2.0.0         | 2.1.0         |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| containers.podman             | 1.10.1        | 1.11.0        |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cyberark.conjur               | 1.2.0         | 1.2.2         | You can find the collection's changelog at `https://github.com/cyberark/ansible-conjur-collection/blob/master/CHANGELOG.md <https://github.com/cyberark/ansible-conjur-collection/blob/master/CHANGELOG.md>`_. |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cyberark.pas                  | 1.0.19        | 1.0.23        | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.                                                                                   |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| dellemc.enterprise_sonic      | 2.0.0         | 2.2.0         |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| dellemc.openmanage            | 7.5.0         | 8.4.0         |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| dellemc.powerflex             | 1.6.0         | 2.0.1         |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| dellemc.unity                 | 1.6.0         | 1.7.1         |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| f5networks.f5_modules         | 1.24.0        | 1.27.0        |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| fortinet.fortimanager         | 2.1.7         | 2.3.0         |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| fortinet.fortios              | 2.2.3         | 2.3.4         |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| google.cloud                  | 1.1.3         | 1.2.0         |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| grafana.grafana               | 2.0.0         | 2.2.3         |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| hetzner.hcloud                | 1.11.0        | 2.3.0         |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ibm.spectrum_virtualize       | 1.12.0        | 2.0.0         |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ibm.storage_virtualize        |               | 2.1.0         | The collection was added to Ansible                                                                                                                                                                            |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| inspur.ispim                  | 1.3.0         | 2.1.0         |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| junipernetworks.junos         | 5.1.0         | 5.3.0         |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| lowlydba.sqlserver            | 2.0.0         | 2.2.2         |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| microsoft.ad                  | 1.1.0         | 1.3.0         |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| netapp.aws                    | 21.7.0        | 21.7.1        | The collection did not have a changelog in this version.                                                                                                                                                       |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| netapp.azure                  | 21.10.0       | 21.10.1       | The collection did not have a changelog in this version.                                                                                                                                                       |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| netapp.cloudmanager           | 21.22.0       | 21.22.1       | The collection did not have a changelog in this version.                                                                                                                                                       |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| netapp.ontap                  | 22.6.0        | 22.8.2        |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| netapp.um_info                | 21.8.0        | 21.8.1        | The collection did not have a changelog in this version.                                                                                                                                                       |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| netbox.netbox                 | 3.13.0        | 3.15.0        |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ngine_io.exoscale             | 1.0.0         | 1.1.0         |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ovirt.ovirt                   | 3.1.2         | 3.2.0         |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| purestorage.flasharray        | 1.18.0        | 1.22.0        |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| purestorage.flashblade        | 1.11.0        | 1.14.0        |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| purestorage.fusion            | 1.4.2         | 1.6.0         |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| sensu.sensu_go                | 1.13.2        | 1.14.0        |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| t_systems_mms.icinga_director | 1.32.2        | 2.0.1         |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| telekom_mms.icinga_director   |               | 1.34.1        | The collection was added to Ansible                                                                                                                                                                            |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| theforeman.foreman            | 3.10.0        | 3.14.0        |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| vultr.cloud                   | 1.7.1         | 1.10.0        |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| vyos.vyos                     | 4.0.2         | 4.1.0         |                                                                                                                                                                                                                |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| wti.remote                    | 1.0.4         | 1.0.5         | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.                                                                                   |
+-------------------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Major Changes
-------------

amazon.aws
~~~~~~~~~~

- aws_region_info - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.aws_region_info``.
- aws_s3_bucket_info - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.aws_s3_bucket_info``.
- iam_access_key - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.iam_access_key``.
- iam_access_key_info - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.iam_access_key_info``.
- iam_group - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.iam_group`` (https://github.com/ansible-collections/amazon.aws/pull/1755).
- iam_managed_policy - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.iam_managed_policy`` (https://github.com/ansible-collections/amazon.aws/pull/1762).
- iam_mfa_device_info - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.iam_mfa_device_info`` (https://github.com/ansible-collections/amazon.aws/pull/1761).
- iam_password_policy - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.iam_password_policy``.
- iam_role - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.iam_role`` (https://github.com/ansible-collections/amazon.aws/pull/1760).
- iam_role_info - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.iam_role_info`` (https://github.com/ansible-collections/amazon.aws/pull/1760).
- s3_bucket_info - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.s3_bucket_info``.
- sts_assume_role - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.sts_assume_role``.

chocolatey.chocolatey
~~~~~~~~~~~~~~~~~~~~~

- win_chocolatey - add options for specifying checksums
- win_chocolatey_facts - add filter / gather_subset option

cisco.ios
~~~~~~~~~

- This release removes a previously deprecated modules, and a few attributes from this collection. Refer to **Removed Features** section for details.

cisco.nxos
~~~~~~~~~~

- Refer to **Removed Features** section for details.
- This release removes four of the previously deprecated modules from this collection.

cloudscale_ch.cloud
~~~~~~~~~~~~~~~~~~~

- Bump minimum required Ansible version to 2.13.0

community.mysql
~~~~~~~~~~~~~~~

- The community.mysql collection no longer supports ``ansible-core 2.12`` and ``ansible-core 2.13``. While we take no active measures to prevent usage and there are no plans to introduce incompatible code to the modules, we will stop testing those versions. Both are or will soon be End of Life and if you are still using them, you should consider upgrading to the ``latest Ansible / ansible-core 2.15 or later`` as soon as possible (https://github.com/ansible-collections/community.mysql/pull/574).
- mysql_role - the ``column_case_sensitive`` argument's default value will be changed to ``true`` in community.mysql 4.0.0. If your playbook expected the column to be automatically uppercased for your roles privileges, you should set this to false explicitly (https://github.com/ansible-collections/community.mysql/issues/578).
- mysql_user - the ``column_case_sensitive`` argument's default value will be changed to ``true`` in community.mysql 4.0.0. If your playbook expected the column to be automatically uppercased for your users privileges, you should set this to false explicitly (https://github.com/ansible-collections/community.mysql/issues/577).

community.postgresql
~~~~~~~~~~~~~~~~~~~~

- postgres modules - the minimum version of psycopg2 library the collection supports is 2.5.1 (https://github.com/ansible-collections/community.postgresql/pull/556).
- postgresql_pg_hba - remove the deprecated ``order`` argument. The sortorder ``sdu`` is hardcoded (https://github.com/ansible-collections/community.postgresql/pull/496).
- postgresql_privs - remove the deprecated ``usage_on_types`` argument. Use the ``type`` option of the ``type`` argument to explicitly manipulate privileges on PG types (https://github.com/ansible-collections/community.postgresql/issues/208).
- postgresql_query - remove the deprecated ``path_to_script`` and ``as_single_query`` arguments. Use the ``postgresql_script`` module to run queries from scripts (https://github.com/ansible-collections/community.postgresql/issues/189).
- postgresql_user - move the deprecated ``privs`` argument removal to community.postgresql 4.0.0 (https://github.com/ansible-collections/community.postgresql/issues/493).
- postgresql_user - remove the deprecated ``groups`` argument. Use the ``postgresql_membership`` module instead (https://github.com/ansible-collections/community.postgresql/issues/300).

community.sap
~~~~~~~~~~~~~

- all modules - everything is now a redirect to the new collection community.sap_libs

community.vmware
~~~~~~~~~~~~~~~~

- vmware_vasa - added a new module to register/unregister a VASA provider
- vmware_vasa_info - added a new module to gather the information about existing VASA provider(s)

fortinet.fortimanager
~~~~~~~~~~~~~~~~~~~~~

- Support all FortiManager versions in 6.2, 6.4, 7.0, 7.2 and 7.4. 139 new modules.
- Support token based authentication.

fortinet.fortios
~~~~~~~~~~~~~~~~

- Add new fortios version 7.4.1.
- Add readthedocs.yaml file.
- Format the contents in the changelog.yml file.
- Improve the `no_log` feature in some modules;
- Improve the document for adding notes and examples in Q&A for modules using Integer number as the mkey.
- Improve the documentation and example for `seq_num` in `fortios_router_static`;
- Improve the documentation for `member_path` in all the modules;
- Support new FOS versions.
- Update Ansible version from 2.9 to 2.14.
- Update Q&A regarding setting up FortiToken multi-factor authentication;
- Update Q&A with a resolution for Ansible Always Sending GET/PUT Requests as POST Requests.
- Update the requirement.txt file to specify the sphinx_rtd_theme==1.3.0
- update the required Ansible version to 2.14.0 in the runtime.yml file.

grafana.grafana
~~~~~~~~~~~~~~~

- Addition of Grafana Server role by @gardar
- Configurable agent user groups by @NormanJS
- Grafana Plugins support on-prem Grafana installation by @ishanjainn
- Updated Service for flow mode by @bentonam

Minor Changes
-------------

- Move setuptools configuration into the declarative ``setup.cfg`` format. ``ansible`` sdists still contain a stub ``setup.py`` file, but we recommend that users move to tools like pip and build and the PEP 517 interface instead of setuptools' deprecated ``setup.py`` interface (https://github.com/ansible-community/antsibull/pull/530).

Ansible-core
~~~~~~~~~~~~

- Add Python type hints to the Display class (https://github.com/ansible/ansible/issues/80841)
- Add ``GALAXY_COLLECTIONS_PATH_WARNING`` option to disable the warning given by ``ansible-galaxy collection install`` when installing a collection to a path that isn't in the configured collection paths.
- Add ``python3.12`` to the default ``INTERPRETER_PYTHON_FALLBACK`` list.
- Add ``utcfromtimestamp`` and ``utcnow`` to ``ansible.module_utils.compat.datetime`` to return fixed offset datetime objects.
- Add a general ``GALAXY_SERVER_TIMEOUT`` config option for distribution servers (https://github.com/ansible/ansible/issues/79833).
- Added Python type annotation to connection plugins
- CLI argument parsing - Automatically prepend to the help of CLI arguments that support being specified multiple times. (https://github.com/ansible/ansible/issues/22396)
- DEFAULT_TRANSPORT now defaults to 'ssh', the old 'smart' option is being deprecated as versions of OpenSSH without control persist are basically not present anymore.
- Documentation for set filters ``intersect``, ``difference``, ``symmetric_difference`` and ``union`` now states that the returned list items are in arbitrary order.
- Record ``removal_date`` in runtime metadata as a string instead of a date.
- Remove the ``CleansingNodeVisitor`` class and its usage due to the templating changes that made it superfluous. Also simplify the ``Conditional`` class.
- Removed ``exclude`` and ``recursive-exclude`` commands for generated files from the ``MANIFEST.in`` file. These excludes were unnecessary since releases are expected to be built with a clean worktree.
- Removed ``exclude`` commands for sanity test files from the ``MANIFEST.in`` file. These tests were previously excluded because they did not pass when run from an sdist. However, sanity tests are not expected to pass from an sdist, so excluding some (but not all) of the failing tests makes little sense.
- Removed redundant ``include`` commands from the ``MANIFEST.in`` file. These includes either duplicated default behavior or another command.
- The ``ansible-core`` sdist no longer contains pre-generated man pages. Instead, a ``packaging/cli-doc/build.py`` script is included in the sdist. This script can generate man pages and standalone RST documentation for ``ansible-core`` CLI programs.
- The ``docs`` and ``examples`` directories are no longer included in the ``ansible-core`` sdist. These directories have been moved to the https://github.com/ansible/ansible-documentation repository.
- The minimum required ``setuptools`` version is now 66.1.0, as it is the oldest version to support Python 3.12.
- Update ``ansible_service_mgr`` fact to include init system for SMGL OS family
- Use ``ansible.module_utils.common.text.converters`` instead of ``ansible.module_utils._text``.
- Use ``importlib.resources.abc.TraversableResources`` instead of deprecated ``importlib.abc.TraversableResources`` where available (https:/github.com/ansible/ansible/pull/81082).
- Use ``include`` where ``recursive-include`` is unnecessary in the ``MANIFEST.in`` file.
- Use ``package_data`` instead of ``include_package_data`` for ``setup.cfg`` to avoid ``setuptools`` warnings.
- Utilize gpg check provided internally by the ``transaction.run`` method as oppose to calling it manually.
- ``Templar`` - do not add the ``dict`` constructor to ``globals`` as all required Jinja2 versions already do so
- ansible-doc - allow to filter listing of collections and metadata dump by more than one collection (https://github.com/ansible/ansible/pull/81450).
- ansible-galaxy - Add a plural option to improve ignoring multiple signature error status codes when installing or verifying collections. A space-separated list of error codes can follow --ignore-signature-status-codes in addition to specifying --ignore-signature-status-code multiple times (for example, ``--ignore-signature-status-codes NO_PUBKEY UNEXPECTED``).
- ansible-galaxy - Remove internal configuration argument ``v3`` (https://github.com/ansible/ansible/pull/80721)
- ansible-galaxy - add note to the collection dependency resolver error message about pre-releases if ``--pre`` was not provided (https://github.com/ansible/ansible/issues/80048).
- ansible-galaxy - used to crash out with a "Errno 20 Not a directory" error when extracting files from a role when hitting a file with an illegal name (https://github.com/ansible/ansible/pull/81553). Now it gives a warning identifying the culprit file and the rule violation (e.g., ``my$class.jar`` has a ``$`` in the name) before crashing out, giving the user a chance to remove the invalid file and try again. (https://github.com/ansible/ansible/pull/81555).
- ansible-test - Add Alpine 3.18 to remotes
- ansible-test - Add Fedora 38 container.
- ansible-test - Add Fedora 38 remote.
- ansible-test - Add FreeBSD 13.2 remote.
- ansible-test - Add new pylint checker for new ``# deprecated:`` comments within code to trigger errors when time to remove code that has no user facing deprecation message. Only supported in ansible-core, not collections.
- ansible-test - Add support for RHEL 8.8 remotes.
- ansible-test - Add support for RHEL 9.2 remotes.
- ansible-test - Add support for testing with Python 3.12.
- ansible-test - Allow float values for the ``--timeout`` option to the ``env`` command. This simplifies testing.
- ansible-test - Enable ``thread`` code coverage in addition to the existing ``multiprocessing`` coverage.
- ansible-test - Make Python 3.12 the default version used in the ``base`` and ``default`` containers.
- ansible-test - RHEL 8.8 provisioning can now be used with the ``--python 3.11`` option.
- ansible-test - RHEL 9.2 provisioning can now be used with the ``--python 3.11`` option.
- ansible-test - Refactored ``env`` command logic and timeout handling.
- ansible-test - Remove Fedora 37 remote support.
- ansible-test - Remove Fedora 37 test container.
- ansible-test - Remove Python 3.8 and 3.9 from RHEL 8.8.
- ansible-test - Remove obsolete embedded script for configuring WinRM on Windows remotes.
- ansible-test - Removed Ubuntu 20.04 LTS image from the `--remote` option.
- ansible-test - Removed `freebsd/12.4` remote.
- ansible-test - Removed `freebsd/13.1` remote.
- ansible-test - Removed test remotes: rhel/8.7, rhel/9.1
- ansible-test - Removed the deprecated ``--docker-no-pull`` option.
- ansible-test - Removed the deprecated ``--no-pip-check`` option.
- ansible-test - Removed the deprecated ``foreman`` test plugin.
- ansible-test - Removed the deprecated ``govcsim`` support from the ``vcenter`` test plugin.
- ansible-test - Replace the ``pytest-forked`` pytest plugin with a custom plugin.
- ansible-test - The ``no-get-exception`` sanity test is now limited to plugins in collections. Previously any Python file in a collection was checked for ``get_exception`` usage.
- ansible-test - The ``replace-urlopen`` sanity test is now limited to plugins in collections. Previously any Python file in a collection was checked for ``urlopen`` usage.
- ansible-test - The ``use-compat-six`` sanity test is now limited to plugins in collections. Previously any Python file in a collection was checked for ``six`` usage.
- ansible-test - The openSUSE test container has been updated to openSUSE Leap 15.5.
- ansible-test - Update pip to ``23.1.2`` and setuptools to ``67.7.2``.
- ansible-test - Update the ``default`` containers.
- ansible-test - Update the ``nios-test-container`` to version 2.0.0, which supports API version 2.9.
- ansible-test - Update the logic used to detect when ``ansible-test`` is running from source.
- ansible-test - Updated the CloudStack test container to version 1.6.1.
- ansible-test - Updated the distro test containers to version 6.3.0 to include coverage 7.3.2 for Python 3.8+. The alpine3 container is now based on 3.18 instead of 3.17 and includes Python 3.11 instead of Python 3.10.
- ansible-test - Use ``datetime.datetime.now`` with ``tz`` specified instead of ``datetime.datetime.utcnow``.
- ansible-test - Use a context manager to perform cleanup at exit instead of using the built-in ``atexit`` module.
- ansible-test - When invoking ``sleep`` in containers during container setup, the ``env`` command is used to avoid invoking the shell builtin, if present.
- ansible-test - remove Alpine 3.17 from remotes
- ansible-test — Python 3.8–3.12 will use ``coverage`` v7.3.2.
- ansible-test — ``coverage`` v6.5.0 is to be used only under Python 3.7.
- ansible-vault create: Now raises an error when opening the editor without tty. The flag --skip-tty-check restores previous behaviour.
- ansible_user_module - tweaked macos user defaults to reflect expected defaults (https://github.com/ansible/ansible/issues/44316)
- apt - return calculated diff while running apt clean operation.
- blockinfile - add append_newline and prepend_newline options (https://github.com/ansible/ansible/issues/80835).
- cli - Added short option '-J' for asking for vault password (https://github.com/ansible/ansible/issues/80523).
- command - Add option ``expand_argument_vars`` to disable argument expansion and use literal values - https://github.com/ansible/ansible/issues/54162
- config lookup new option show_origin to also return the origin of a configuration value.
- display methods for warning and deprecation are now proxied to main process when issued from a fork. This allows for the deduplication of warnings and deprecations to work globally.
- dnf5 - enable environment groups installation testing in CI as its support was added.
- dnf5 - enable now implemented ``cacheonly`` functionality
- executor now skips persistent connection when it detects an action that does not require a connection.
- find module - Add ability to filter based on modes
- gather_facts now will use gather_timeout setting to limit parallel execution of modules that do not themselves use gather_timeout.
- group - remove extraneous warning shown when user does not exist (https://github.com/ansible/ansible/issues/77049).
- include_vars - os.walk now follows symbolic links when traversing directories (https://github.com/ansible/ansible/pull/80460)
- module compression is now sourced directly via config, bypassing play_context possibly stale values.
- reboot - show last error message in verbose logs (https://github.com/ansible/ansible/issues/81574).
- service_facts now returns more info for rcctl managed systesm (OpenBSD).
- tasks - the ``retries`` keyword can be specified without ``until`` in which case the task is retried until it succeeds but at most ``retries`` times (https://github.com/ansible/ansible/issues/20802)
- user - add new option ``password_expire_warn`` (supported on Linux only) to set the number of days of warning before a password change is required (https://github.com/ansible/ansible/issues/79882).
- yum_repository - Align module documentation with parameters

amazon.aws
~~~~~~~~~~

- amazon.aws collection - apply isort code formatting to ensure consistent formatting of code (https://github.com/ansible-collections/amazon.aws/pull/1771).
- backup_selection - add validation and documentation for all conditions suboptions (https://github.com/ansible-collections/amazon.aws/pull/1633).
- cloudformation - Add support for ``disable_rollback`` to update stack operation (https://github.com/ansible-collections/amazon.aws/issues/1681).
- ec2_ami - add support for ``org_arns`` and ``org_unit_arns`` in launch_permissions (https://github.com/ansible-collections/amazon.aws/pull/1690).
- ec2_instance - add support for additional ``placement`` options and ``license_specifications`` in run instance spec (https://github.com/ansible-collections/amazon.aws/issues/1824).
- ec2_instance - refactored ARN validation handling (https://github.com/ansible-collections/amazon.aws/pull/1619).
- ec2_instance_info - add new parameter ``include_attributes`` to describe instance attributes (https://github.com/ansible-collections/amazon.aws/pull/1577).
- ec2_key - add support for new parameter ``file_name`` to save private key in when new key is created by AWS. When this option is provided the generated private key will be removed from the module return (https://github.com/ansible-collections/amazon.aws/pull/1704).
- ec2_metadata_facts - use fstrings where appropriate (https://github.com/ansible-collections/amazon.aws/pull/1802).
- ec2_snapshot - Add support for modifying createVolumePermission (https://github.com/ansible-collections/amazon.aws/pull/1464).
- ec2_snapshot_info - Add createVolumePermission to output result (https://github.com/ansible-collections/amazon.aws/pull/1464).
- ec2_vpc_igw - Add ability to attach/detach VPC to/from internet gateway (https://github.com/ansible-collections/amazon.aws/pull/1786).
- ec2_vpc_igw - Add ability to change VPC attached to internet gateway (https://github.com/ansible-collections/amazon.aws/pull/1786).
- ec2_vpc_igw - Add ability to create an internet gateway without attaching a VPC (https://github.com/ansible-collections/amazon.aws/pull/1786).
- ec2_vpc_igw - Add ability to delete a vpc internet gateway using the id of the gateway (https://github.com/ansible-collections/amazon.aws/pull/1786).
- elb_application_lb_info - add new parameters ``include_attributes``, ``include_listeners`` and  ``include_listener_rules`` to optionally speed up module by fetching less information (https://github.com/ansible-collections/amazon.aws/pull/1778).
- elb_application_lb_info - drop redundant ``describe_load_balancers`` call fetching ``ip_address_type`` (https://github.com/ansible-collections/amazon.aws/pull/1768).
- iam_user - refactored ARN validation handling (https://github.com/ansible-collections/amazon.aws/pull/1619).
- module_utils.arn - add ``resource_id`` and ``resource_type`` to ``parse_aws_arn`` return values (https://github.com/ansible-collections/amazon.aws/pull/1619).
- module_utils.arn - added ``validate_aws_arn`` function to handle common pattern matching for ARNs (https://github.com/ansible-collections/amazon.aws/pull/1619).
- module_utils.botocore - migrate from vendored copy of LooseVersion to packaging.version.Version (https://github.com/ansible-collections/amazon.aws/pull/1587).
- rds_cluster - Add support for removing cluster from global db (https://github.com/ansible-collections/amazon.aws/pull/1705).
- rds_cluster - add support for another ``state`` choice called ``started``. This starts the rds cluster (https://github.com/ansible-collections/amazon.aws/pull/1647/files).
- rds_cluster - add support for another ``state`` choice called ``stopped``. This stops the rds cluster (https://github.com/ansible-collections/amazon.aws/pull/1647/files).
- route53 - add a ``wait_id`` return value when a change is done (https://github.com/ansible-collections/amazon.aws/pull/1683).
- route53_health_check - add support for a string list parameter called ``child_health_checks`` to specify health checks that must be healthy for the calculated health check (https://github.com/ansible-collections/amazon.aws/pull/1631).
- route53_health_check - add support for an integer parameter called ``health_threshold`` to specify the minimum number of healthy child health checks that must be healthy for the calculated health check (https://github.com/ansible-collections/amazon.aws/pull/1631).
- route53_health_check - add support for another ``type`` choice called ``CALCULATED`` (https://github.com/ansible-collections/amazon.aws/pull/1631).
- s3_object - Allow recursive copy of objects in S3 bucket (https://github.com/ansible-collections/amazon.aws/issues/1379).
- s3_object - use fstrings where appropriate (https://github.com/ansible-collections/amazon.aws/pull/1802).

ansible.netcommon
~~~~~~~~~~~~~~~~~

- Add a new cliconf plugin ``default`` that can be used when no cliconf plugin is found for a given network_os. This plugin only supports ``get()``. (https://github.com/ansible-collections/ansible.netcommon/pull/569)
- Add new module cli_backup that exclusively handles configuration backup.
- httpapi - Add additional option ``ca_path``, ``client_cert``, ``client_key``, and ``http_agent`` that are available in open_url but not to httpapi. (https://github.com/ansible-collections/ansible.netcommon/issues/528)
- telnet - add crlf option to send CRLF instead of just LF (https://github.com/ansible-collections/ansible.netcommon/pull/440).

ansible.utils
~~~~~~~~~~~~~

- Add ipcut filter plugin.(https://github.com/ansible-collections/ansible.utils/issues/251)
- Add ipv6form filter plugin.(https://github.com/ansible-collections/ansible.utils/issues/230)

ansible.windows
~~~~~~~~~~~~~~~

- win_certificate_store - the private key check, when exporting to pkcs12, has been modified to handle the case where the ``PrivateKey`` property is null despite it being there
- win_find - Added ``depth`` option to control how deep to go when scanning into the target path - https://github.com/ansible-collections/ansible.windows/issues/335
- win_updates - Avoid using a scheduled task to spawn the updates background job when running as become. This provides an alternative method available to users in case the task scheduler does not work on their system - https://github.com/ansible-collections/ansible.windows/issues/543

arista.eos
~~~~~~~~~~

- Add support for overridden operation in bgp_global resource module.
- arista_config - Relax restrictions on I(src) parameter so it can be used more like I(lines).

check_point.mgmt
~~~~~~~~~~~~~~~~

- cp_mgmt_vpn_community_star - new fields added.
- show command modules  - no longer return result of changed=True.

chocolatey.chocolatey
~~~~~~~~~~~~~~~~~~~~~

- All modules - Ensure modules are compatible with both Chocolatey CLI v2.x and v1.x
- win_chocolatey - Improve error messages when installation of Chocolatey CLI v2.x fails due to unmet .NET Framework 4.8 dependency on client

cisco.aci
~~~~~~~~~

- Add 8.0 option for dvs_version attribute in aci_vmm_controller
- Add ACI HTTPAPI plugin with multi host support (#114)
- Add Match Rules for aci_route_control_profile modules
- Add OSPF parameters to aci_l3out module and create the associated test case.
- Add aci_access_span_src_group modules for access span source group support
- Add aci_access_span_src_group_src module for access span source support
- Add aci_access_span_src_group_src_path module for access span source path support
- Add aci_bgp_timers_policy and aci_bgp_best_path_policy modules
- Add aci_epg_subnet module (#424)
- Add aci_fabric_interface_policy_group module
- Add aci_fabric_span_dst_group module for fabric span destination group support
- Add aci_fabric_span_src_group module for fabric span source group support
- Add aci_fabric_span_src_group_src module for fabric span source support
- Add aci_fabric_span_src_group_src_node module for fabric span source node support
- Add aci_fabric_span_src_group_src_path module for fabric span source path support
- Add aci_file_remote_path module (#379)
- Add aci_interface_policy_leaf_fc_policy_group and aci_interface_policy_spine_policy_group module
- Add aci_l3out_bgp_protocol_profile module
- Add aci_match_community_factor module.
- Add aci_route_control_context and aci_match_rule modules
- Add aci_route_control_profile module
- Add aci_vrf_leak_internal_subnet module (#449)
- Add description parameter for aci_l3out_logical_interface_profile
- Add hmac-sha2-224, hmac-sha2-256, hmac-sha2-384, hmac-sha2-512 authentication types and description to aci_snmp_user module
- Add ip_data_plane_learning attribute to aci_bd_subnet and aci_vrf modules (#413)
- Add local_as_number_config and local_as_number attributes to support bgpLocalAsnP child object in aci_l3out_bgp_peer module (#416)
- Add loopback interface profile as a child class for aci_l3out_logical_node.
- Add missing attributes in aci_interface_policy_leaf_policy_group
- Add missing attributes to aci_l3out_extepg module
- Add missing test cases, fix found issues and add missing attributes for aci_fabric_scheduler, aci_firmware_group, aci_firmware_group_node, aci_firmware_policy, aci_interface_policy_fc, aci_interface_policy_lldp, aci_interface_policy_mcp, aci_interface_policy_ospf, aci_interface_policy_port_channel, aci_maintenance_group, aci_maintenance_group_node, aci_maintenance_policy and aci_tenant_ep_retention_policy modules (#453)
- Add node_type and remote_leaf_pool_id attributes to aci_fabric_node
- Add source_port, source_port_start, source_port_end, tcp_flags and match_only_fragments attributes to aci_filter_entry module (#426)
- Add support for checkmode in aci_rest module
- Add support for configuration of fabric node control with aci_fabric_node_control module
- Add support for configuration of fabric pod selectors with aci_fabric_pod_selector module
- Add support for configuration of system banner and alias with aci_system_banner module
- Add support for configuration of system endpoint controls, ip aging, ep loop protection and roque endpoint control with aci_system_endpoint_controls module
- Add support for configuration of system fabric wide settings with aci_fabric_wide_settings module
- Add support for configuration of system global aes passphrase encryption with aci_system_global_aes_passphrase_encryption module
- Add support for global infra dhcp relay policy configuration in aci_dhcp_relay
- Add support for global infra dhcp relay policy configuration in aci_dhcp_relay_provider

cisco.ios
~~~~~~~~~

- Fixe an issue with some files that doesn't pass the PEP8 sanity check because `type(<obj>) == <type>` is not allowed. We need to use `isinstance(<obj>,<type>)` function in place
- ios_acls - make remarks ordered and to be applied per ace basis.
- ios_acls - remarks in replaced and overridden state to be negated once per ace.
- ios_config - Relax restrictions on I(src) parameter so it can be used more like I(lines).
- ios_facts - Add CPU utilization. (https://github.com/ansible-collections/cisco.ios/issues/779)
- ios_interfaces - Add template attribute to provide support for cisco ios templates.
- ios_service - Create module to manage service configuration on IOS switches
- ios_snmp_server - Fix an issue with cbgp2 to take in count correctly the bgp traps
- ios_snmp_server - Update the module to manage correctly a lot of traps not take in count
- ios_snmp_user - update the user part to compare correctly the auth and privacy parts.
- ospfv2 - added more tests to improve coverage for the rm_template
- ospfv2 - aliased passive_interface to passive_interfaces that supports a list of interfaces
- ospfv2 - fix area ranges rendering
- ospfv2 - fix passive interfaces rendering
- ospfv2 - optimized all the regex to perform better
- ospfv2 - optimized the config side code for quicker comparison and execution

cisco.iosxr
~~~~~~~~~~~

- Add iosxr_bgp_templates module (https://github.com/ansible-collections/cisco.iosxr/issues/341).
- iosxr_config - Relax restrictions on I(src) parameter so it can be used more like I(lines). (https://github.com/ansible-collections/cisco.iosxr/issues/343).
- iosxr_config Add updates option in return value(https://github.com/ansible-collections/cisco.iosxr/issues/438).
- iosxr_facts - Add CPU utilization.
- iosxr_l2_interfaces - fix issue in supporting multiple iosxr version. (https://github.com/ansible-collections/cisco.iosxr/issues/379).

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
- meraki_mx_site_to_site_firewall - Fix updating VPN rules per issue 302.
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

cisco.mso
~~~~~~~~~

- Add login domain attribute to mso httpapi connection plugin with restructure of connection parameter handling
- Add mso_schema_template_anp_epg_useg_attribute and mso_schema_site_anp_epg_useg_attribute modules to manage EPG uSeg attributes (#370)

cisco.nxos
~~~~~~~~~~

- Add nxos_bgp_templates module.
- Added new module fc_interfaces
- bgp_global - support remote-as as a route-map (https://github.com/ansible-collections/cisco.nxos/issues/741).
- bgp_neighbor_address_family - support rewrite-rt-asn for ipv4 mvpn (https://github.com/ansible-collections/cisco.nxos/issues/741).
- bgp_templates - Add support for safi evpn (https://github.com/ansible-collections/cisco.nxos/issues/739).
- bgp_templates - Add support for send_community (https://github.com/ansible-collections/cisco.nxos/issues/740).
- nxos_facts - add cpu utilization data to facts.
- nxos_user - Add support for hashed passwords. (https://github.com/ansible-collections/cisco.nxos/issues/370).
- nxos_user - Added dev-ops role to BUILTINS (https://github.com/ansible-collections/cisco.nxos/issues/690)
- route_maps - support extcommunity rt option (https://github.com/ansible-collections/cisco.nxos/issues/743).

community.aws
~~~~~~~~~~~~~

- api_gateway - add support for parameters ``name``, ``lookup``, ``tags`` and ``purge_tags`` (https://github.com/ansible-collections/community.aws/pull/1845).
- api_gateway - use fstrings where appropriate (https://github.com/ansible-collections/amazon.aws/pull/1962).
- api_gateway_info - use fstrings where appropriate (https://github.com/ansible-collections/amazon.aws/pull/1962).
- community.aws collection - apply isort code formatting to ensure consistent formatting of code (https://github.com/ansible-collections/community.aws/pull/1962)
- dynamodb_table - added waiter when updating indexes to avoid concurrency issues (https://github.com/ansible-collections/community.aws/pull/1866).
- dynamodb_table - increased default timeout based on time to update indexes in CI (https://github.com/ansible-collections/community.aws/pull/1866).
- ec2_vpc_vpn - add support for connecting VPNs to a transit gateway (https://github.com/ansible-collections/community.aws/pull/1877).
- ecs_taskdefinition - Add parameter ``runtime_platform`` (https://github.com/ansible-collections/community.aws/issues/1891).
- eks_nodegroup - ensure wait also waits for deletion to complete when ``wait==True`` (https://github.com/ansible-collections/community.aws/pull/1994).
- iam_group - refactored ARN validation handling (https://github.com/ansible-collections/community.aws/pull/1848).
- iam_role - refactored ARN validation handling (https://github.com/ansible-collections/community.aws/pull/1848).
- sns_topic - refactored ARN validation handling (https://github.com/ansible-collections/community.aws/pull/1848).

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
- luks_devices - add new options ``keyslot``, ``new_keyslot``, and ``remove_keyslot`` to allow adding/removing keys to/from specific keyslots (https://github.com/ansible-collections/community.crypto/pull/664).
- openssh_keypair - fail when comment cannot be updated (https://github.com/ansible-collections/community.crypto/pull/646).
- x509_certificate_info - added support for certificates in DER format when using ``path`` parameter (https://github.com/ansible-collections/community.crypto/issues/603).

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

- The collection will start using semantic markup (https://github.com/ansible-collections/community.general/pull/6539).
- VarDict module utils - add method ``VarDict.as_dict()`` to convert to a plain ``dict`` object (https://github.com/ansible-collections/community.general/pull/6602).
- apt_rpm - extract package name from local ``.rpm`` path when verifying
  installation success. Allows installing packages from local ``.rpm`` files
  (https://github.com/ansible-collections/community.general/pull/7396).
- cargo - add option ``executable``, which allows user to specify path to the cargo binary (https://github.com/ansible-collections/community.general/pull/7352).
- cargo - add option ``locked`` which allows user to specify install the locked version of dependency instead of latest compatible version (https://github.com/ansible-collections/community.general/pull/6134).
- chroot connection plugin - add ``disable_root_check`` option (https://github.com/ansible-collections/community.general/pull/7099).
- cloudflare_dns - add CAA record support (https://github.com/ansible-collections/community.general/pull/7399).
- cobbler inventory plugin - add ``exclude_mgmt_classes`` and ``include_mgmt_classes`` options to exclude or include hosts based on management classes (https://github.com/ansible-collections/community.general/pull/7184).
- cobbler inventory plugin - add ``inventory_hostname`` option to allow using the system name for the inventory hostname (https://github.com/ansible-collections/community.general/pull/6502).
- cobbler inventory plugin - add ``want_ip_addresses`` option to collect all interface DNS name to IP address mapping (https://github.com/ansible-collections/community.general/pull/6711).
- cobbler inventory plugin - add primary IP addess to ``cobbler_ipv4_address`` and IPv6 address to ``cobbler_ipv6_address`` host variable (https://github.com/ansible-collections/community.general/pull/6711).
- cobbler inventory plugin - add warning for systems with empty profiles (https://github.com/ansible-collections/community.general/pull/6502).
- cobbler inventory plugin - convert Ansible unicode strings to native Python unicode strings before passing user/password to XMLRPC client (https://github.com/ansible-collections/community.general/pull/6923).
- consul_session - drops requirement for the ``python-consul`` library to communicate with the Consul API, instead relying on the existing ``requests`` library requirement (https://github.com/ansible-collections/community.general/pull/6755).
- copr - respawn module to use the system python interpreter when the ``dnf`` python module is not available in ``ansible_python_interpreter`` (https://github.com/ansible-collections/community.general/pull/6522).
- cpanm - minor refactor when creating the ``CmdRunner`` object (https://github.com/ansible-collections/community.general/pull/7231).
- datadog_monitor - adds ``notification_preset_name``, ``renotify_occurrences`` and ``renotify_statuses`` parameters (https://github.com/ansible-collections/community.general/issues/6521,https://github.com/ansible-collections/community.general/issues/5823).
- dig lookup plugin - add TCP option to enable the use of TCP connection during DNS lookup (https://github.com/ansible-collections/community.general/pull/7343).
- ejabberd_user - module now using ``CmdRunner`` to execute external command (https://github.com/ansible-collections/community.general/pull/7075).
- filesystem - add ``uuid`` parameter for UUID change feature (https://github.com/ansible-collections/community.general/pull/6680).
- gitlab_group - add option ``force_delete`` (default: false) which allows delete group even if projects exists in it (https://github.com/ansible-collections/community.general/pull/7364).
- gitlab_group_variable - add support for ``raw`` variables suboption (https://github.com/ansible-collections/community.general/pull/7132).
- gitlab_project_variable - add support for ``raw`` variables suboption (https://github.com/ansible-collections/community.general/pull/7132).
- gitlab_project_variable - minor refactor removing unnecessary code statements (https://github.com/ansible-collections/community.general/pull/6928).
- gitlab_runner - minor refactor removing unnecessary code statements (https://github.com/ansible-collections/community.general/pull/6927).
- htpasswd - minor code improvements in the module (https://github.com/ansible-collections/community.general/pull/6901).
- htpasswd - the parameter ``crypt_scheme`` is being renamed as ``hash_scheme`` and added as an alias to it (https://github.com/ansible-collections/community.general/pull/6841).
- icinga2_host - the ``ip`` option is no longer required, since Icinga 2 allows for an empty address attribute (https://github.com/ansible-collections/community.general/pull/7452).
- ini_file - add ``ignore_spaces`` option (https://github.com/ansible-collections/community.general/pull/7273).
- ini_file - add ``modify_inactive_option`` option (https://github.com/ansible-collections/community.general/pull/7401).
- ipa_config - add module parameters to manage FreeIPA user and group objectclasses (https://github.com/ansible-collections/community.general/pull/7019).
- ipa_config - adds ``idp`` choice to ``ipauserauthtype`` parameter's choices (https://github.com/ansible-collections/community.general/pull/7051).
- jenkins_build - add new ``detach`` option, which allows the module to exit successfully as long as the build is created (default functionality is still waiting for the build to end before exiting) (https://github.com/ansible-collections/community.general/pull/7204).
- jenkins_build - add new ``time_between_checks`` option, which allows to configure the wait time between requests to the Jenkins server (https://github.com/ansible-collections/community.general/pull/7204).
- keycloak_authentication - added provider ID choices, since Keycloak supports only those two specific ones (https://github.com/ansible-collections/community.general/pull/6763).
- keycloak_client_rolemapping - adds support for subgroups with additional parameter ``parents`` (https://github.com/ansible-collections/community.general/pull/6687).
- keycloak_role - add composite roles support for realm and client roles (https://github.com/ansible-collections/community.general/pull/6469).
- keyring - minor refactor removing unnecessary code statements (https://github.com/ansible-collections/community.general/pull/6927).
- ldap_* - add new arguments ``client_cert`` and ``client_key`` to the LDAP modules in order to allow certificate authentication (https://github.com/ansible-collections/community.general/pull/6668).
- ldap_search - add a new ``page_size`` option to enable paged searches (https://github.com/ansible-collections/community.general/pull/6648).
- locale_gen - module has been refactored to use ``ModuleHelper`` and ``CmdRunner`` (https://github.com/ansible-collections/community.general/pull/6903).
- locale_gen - module now using ``CmdRunner`` to execute external commands (https://github.com/ansible-collections/community.general/pull/6820).
- lvg - add ``active`` and ``inactive`` values to the ``state`` option for active state management feature (https://github.com/ansible-collections/community.general/pull/6682).
- lvg - add ``reset_vg_uuid``, ``reset_pv_uuid`` options for UUID reset feature (https://github.com/ansible-collections/community.general/pull/6682).
- lxc connection plugin - properly handle a change of the ``remote_addr`` option (https://github.com/ansible-collections/community.general/pull/7373).
- lxd connection plugin - automatically translate ``remote_addr`` from FQDN to (short) hostname (https://github.com/ansible-collections/community.general/pull/7360).
- lxd connection plugin - update error parsing to work with newer messages mentioning instances (https://github.com/ansible-collections/community.general/pull/7360).
- lxd inventory plugin - add ``server_cert`` option for trust anchor to use for TLS verification of server certificates (https://github.com/ansible-collections/community.general/pull/7392).
- lxd inventory plugin - add ``server_check_hostname`` option to disable hostname verification of server certificates (https://github.com/ansible-collections/community.general/pull/7392).
- make - add new ``targets`` parameter allowing multiple targets to be used with ``make`` (https://github.com/ansible-collections/community.general/pull/6882, https://github.com/ansible-collections/community.general/issues/4919).
- make - allows ``params`` to be used without value (https://github.com/ansible-collections/community.general/pull/7180).
- mas - disable sign-in check for macOS 12+ as ``mas account`` is non-functional (https://github.com/ansible-collections/community.general/pull/6520).
- newrelic_deployment - add option ``app_name_exact_match``, which filters results for the exact app_name provided (https://github.com/ansible-collections/community.general/pull/7355).
- nmap inventory plugin - now has a ``use_arp_ping`` option to allow the user to disable the default ARP ping query for a more reliable form (https://github.com/ansible-collections/community.general/pull/7119).
- nmcli - add support for ``ipv4.dns-options`` and ``ipv6.dns-options`` (https://github.com/ansible-collections/community.general/pull/6902).
- nomad_job, nomad_job_info - add ``port`` parameter (https://github.com/ansible-collections/community.general/pull/7412).
- npm - minor improvement on parameter validation (https://github.com/ansible-collections/community.general/pull/6848).
- npm - module now using ``CmdRunner`` to execute external commands (https://github.com/ansible-collections/community.general/pull/6989).
- onepassword lookup plugin - add service account support (https://github.com/ansible-collections/community.general/issues/6635, https://github.com/ansible-collections/community.general/pull/6660).
- onepassword lookup plugin - introduce ``account_id`` option which allows specifying which account to use (https://github.com/ansible-collections/community.general/pull/7308).
- onepassword_raw lookup plugin - add service account support (https://github.com/ansible-collections/community.general/issues/6635, https://github.com/ansible-collections/community.general/pull/6660).
- onepassword_raw lookup plugin - introduce ``account_id`` option which allows specifying which account to use (https://github.com/ansible-collections/community.general/pull/7308).
- opentelemetry callback plugin - add span attributes in the span event (https://github.com/ansible-collections/community.general/pull/6531).
- opkg - add ``executable`` parameter allowing to specify the path of the ``opkg`` command (https://github.com/ansible-collections/community.general/pull/6862).
- opkg - remove default value ``""`` for parameter ``force`` as it causes the same behaviour of not having that parameter (https://github.com/ansible-collections/community.general/pull/6513).
- pagerduty - adds in option to use v2 API for creating pagerduty incidents (https://github.com/ansible-collections/community.general/issues/6151)
- parted - on resize, use ``--fix`` option if available (https://github.com/ansible-collections/community.general/pull/7304).
- pnpm - set correct version when state is latest or version is not mentioned. Resolves previous idempotency problem (https://github.com/ansible-collections/community.general/pull/7339).
- pritunl module utils - ensure ``validate_certs`` parameter is honoured in all methods (https://github.com/ansible-collections/community.general/pull/7156).
- proxmox - add ``vmid`` (and ``taskid`` when possible) to return values (https://github.com/ansible-collections/community.general/pull/7263).
- proxmox - support ``timezone`` parameter at container creation (https://github.com/ansible-collections/community.general/pull/6510).
- proxmox inventory plugin - add composite variables support for Proxmox nodes (https://github.com/ansible-collections/community.general/issues/6640).
- proxmox_kvm - added support for ``tpmstate0`` parameter to configure TPM (Trusted Platform Module) disk. TPM is required for Windows 11 installations (https://github.com/ansible-collections/community.general/pull/6533).
- proxmox_kvm - enabled force restart of VM, bringing the ``force`` parameter functionality in line with what is described in the docs (https://github.com/ansible-collections/community.general/pull/6914).
- proxmox_kvm - re-use ``timeout`` module param to forcefully shutdown a virtual machine when ``state`` is ``stopped`` (https://github.com/ansible-collections/community.general/issues/6257).
- proxmox_snap - add ``retention`` parameter to delete old snapshots (https://github.com/ansible-collections/community.general/pull/6576).
- proxmox_vm_info - ``node`` parameter is no longer required. Information can be obtained for the whole cluster (https://github.com/ansible-collections/community.general/pull/6976).
- proxmox_vm_info - non-existing provided by name/vmid VM would return empty results instead of failing (https://github.com/ansible-collections/community.general/pull/7049).
- pubnub_blocks - minor refactor removing unnecessary code statements (https://github.com/ansible-collections/community.general/pull/6928).
- random_string - added new ``ignore_similar_chars`` and ``similar_chars`` option to ignore certain chars (https://github.com/ansible-collections/community.general/pull/7242).
- redfish_command - add ``MultipartHTTPPushUpdate`` command (https://github.com/ansible-collections/community.general/issues/6471, https://github.com/ansible-collections/community.general/pull/6612).
- redfish_command - add ``account_types`` and ``oem_account_types`` as optional inputs to ``AddUser`` (https://github.com/ansible-collections/community.general/issues/6823, https://github.com/ansible-collections/community.general/pull/6871).
- redfish_command - add new option ``update_oem_params`` for the ``MultipartHTTPPushUpdate`` command (https://github.com/ansible-collections/community.general/issues/7331).
- redfish_config - add ``CreateVolume`` command to allow creation of volumes on servers (https://github.com/ansible-collections/community.general/pull/6813).
- redfish_config - add ``DeleteAllVolumes`` command to allow deletion of all volumes on servers (https://github.com/ansible-collections/community.general/pull/6814).
- redfish_config - adding ``SetSecureBoot`` command (https://github.com/ansible-collections/community.general/pull/7129).
- redfish_info - add ``AccountTypes`` and ``OEMAccountTypes`` to the output of ``ListUsers`` (https://github.com/ansible-collections/community.general/issues/6823, https://github.com/ansible-collections/community.general/pull/6871).
- redfish_info - add support for ``GetBiosRegistries`` command (https://github.com/ansible-collections/community.general/pull/7144).
- redfish_info - adds ``LinkStatus`` to NIC inventory (https://github.com/ansible-collections/community.general/pull/7318).
- redfish_info - adds ``ProcessorArchitecture`` to CPU inventory (https://github.com/ansible-collections/community.general/pull/6864).
- redfish_info - fix for ``GetVolumeInventory``, Controller name was getting populated incorrectly and duplicates were seen in the volumes retrieved (https://github.com/ansible-collections/community.general/pull/6719).
- redfish_info - report ``Id`` in the output of ``GetManagerInventory`` (https://github.com/ansible-collections/community.general/pull/7140).
- redfish_utils - use ``Controllers`` key in redfish data to obtain Storage controllers properties (https://github.com/ansible-collections/community.general/pull/7081).
- redfish_utils module utils - add support for ``PowerCycle`` reset type for ``redfish_command`` responses feature (https://github.com/ansible-collections/community.general/issues/7083).
- redfish_utils module utils - add support for following ``@odata.nextLink`` pagination in ``software_inventory`` responses feature (https://github.com/ansible-collections/community.general/pull/7020).
- redfish_utils module utils - support ``Volumes`` in response for ``GetDiskInventory`` (https://github.com/ansible-collections/community.general/pull/6819).
- redhat_subscription - the internal ``RegistrationBase`` class was folded
  into the other internal ``Rhsm`` class, as the separation had no purpose
  anymore
  (https://github.com/ansible-collections/community.general/pull/6658).
- redis_info - refactor the redis_info module to use the redis module_utils enabling to pass TLS parameters to the Redis client (https://github.com/ansible-collections/community.general/pull/7267).
- rhsm_release - improve/harden the way ``subscription-manager`` is run;
  no behaviour change is expected
  (https://github.com/ansible-collections/community.general/pull/6669).
- rhsm_repository - the interaction with ``subscription-manager`` was
  refactored by grouping things together, removing unused bits, and hardening
  the way it is run; also, the parsing of ``subscription-manager repos --list``
  was improved and made slightly faster; no behaviour change is expected
  (https://github.com/ansible-collections/community.general/pull/6783,
  https://github.com/ansible-collections/community.general/pull/6837).
- scaleway_security_group_rule - minor refactor removing unnecessary code statements (https://github.com/ansible-collections/community.general/pull/6928).
- shutdown - use ``shutdown -p ...`` with FreeBSD to halt and power off machine (https://github.com/ansible-collections/community.general/pull/7102).
- snap - add option ``dangerous`` to the module, that will map into the command line argument ``--dangerous``, allowing unsigned snap files to be installed (https://github.com/ansible-collections/community.general/pull/6908, https://github.com/ansible-collections/community.general/issues/5715).
- snap - module is now aware of channel when deciding whether to install or refresh the snap (https://github.com/ansible-collections/community.general/pull/6435, https://github.com/ansible-collections/community.general/issues/1606).
- sorcery - add grimoire (repository) management support (https://github.com/ansible-collections/community.general/pull/7012).
- sorcery - minor refactor (https://github.com/ansible-collections/community.general/pull/6525).
- supervisorctl - allow to stop matching running processes before removing them with ``stop_before_removing=true`` (https://github.com/ansible-collections/community.general/pull/7284).
- tss lookup plugin - allow to fetch secret IDs which are in a folder based on folder ID. Previously, we could not fetch secrets based on folder ID but now use ``fetch_secret_ids_from_folder`` option to indicate to fetch secret IDs based on folder ID (https://github.com/ansible-collections/community.general/issues/6223).
- tss lookup plugin - allow to fetch secret by path. Previously, we could not fetch secret by path but now use ``secret_path`` option to indicate to fetch secret by secret path (https://github.com/ansible-collections/community.general/pull/6881).
- unixy callback plugin - add support for ``check_mode_markers`` option (https://github.com/ansible-collections/community.general/pull/7179).
- vardict module utils - added convenience methods to ``VarDict`` (https://github.com/ansible-collections/community.general/pull/6647).
- xenserver_guest_info - minor refactor removing unnecessary code statements (https://github.com/ansible-collections/community.general/pull/6928).
- xenserver_guest_powerstate - minor refactor removing unnecessary code statements (https://github.com/ansible-collections/community.general/pull/6928).
- yum_versionlock - add support to pin specific package versions instead of only the package itself (https://github.com/ansible-collections/community.general/pull/6861, https://github.com/ansible-collections/community.general/issues/4470).

community.grafana
~~~~~~~~~~~~~~~~~

- Add `grafana_organization_user` module
- Bump version of Python used in tests to 3.10
- Enable datasource option `time_interval` for prometheus
- Fix documentation url for Ansible doc website
- Now testing against Grafana 9.5.13, 8.5.27, 10.2.0

community.libvirt
~~~~~~~~~~~~~~~~~

- virt - add `mutate_flags` parameter to enable XML mutation (add UUID, MAC addresses from existing domain) (https://github.com/ansible-collections/community.libvirt/pull/142/).
- virt - support ``--diff`` for ``define`` command (https://github.com/ansible-collections/community.libvirt/pull/142/).

community.mysql
~~~~~~~~~~~~~~~

- mysql_info - add filter ``users_info`` (https://github.com/ansible-collections/community.mysql/pull/580).
- mysql_role - add ``column_case_sensitive`` option to prevent field names from being uppercased (https://github.com/ansible-collections/community.mysql/pull/569).
- mysql_user - add ``column_case_sensitive`` option to prevent field names from being uppercased (https://github.com/ansible-collections/community.mysql/pull/569).

community.postgresql
~~~~~~~~~~~~~~~~~~~~

- Collection core functions - use ``get_server_version`` in all modules (https://github.com/ansible-collections/community.postgresql/pull/518)."
- Collection core functions - use common cursor arguments in all modules (https://github.com/ansible-collections/community.postgresql/pull/522)."
- postgres modules - added support for Psycopg 3 library (https://github.com/ansible-collections/community.postgresql/pull/517).
- postgresql_ext - added idempotence always both in standard and in check mode (https://github.com/ansible-collections/community.postgresql/pull/545).
- postgresql_ext - added idempotence when version=latest (https://github.com/ansible-collections/community.postgresql/pull/504).
- postgresql_ext - added prev_version and version return values (https://github.com/ansible-collections/community.postgresql/pull/545).
- postgresql_ext - added queries in module output also in check mode (https://github.com/ansible-collections/community.postgresql/pull/545).
- postgresql_ext - improved error messages (https://github.com/ansible-collections/community.postgresql/pull/545).
- postgresql_owner - added support at new object types (https://github.com/ansible-collections/community.postgresql/pull/555).
- postgresql_privs - added idempotence when roles=PUBLIC (https://github.com/ansible-collections/community.postgresql/pull/502).
- postgresql_privs - added parameters privileges support for PostgreSQL 15 or higher (https://github.com/ansible-collections/community.postgresql/issues/481).
- postgresql_privs - added support for implicit roles CURRENT_ROLE, CURRENT_USER, and SESSION_USER (https://github.com/ansible-collections/community.postgresql/pull/502).
- postgresql_tablespace - added idempotence when dropping a non-existing tablespace (https://github.com/ansible-collections/community.postgresql/pull/554).

community.routeros
~~~~~~~~~~~~~~~~~~

- api_info - add new ``include_read_only`` option to select behavior for read-only values. By default these are not returned (https://github.com/ansible-collections/community.routeros/pull/213).
- api_info, api_modify - add path ``caps-man channel`` and enable path ``caps-man manager interface`` (https://github.com/ansible-collections/community.routeros/issues/193, https://github.com/ansible-collections/community.routeros/pull/194).
- api_info, api_modify - add path ``ip traffic-flow target`` (https://github.com/ansible-collections/community.routeros/issues/191, https://github.com/ansible-collections/community.routeros/pull/192).
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

- Removed module / plugin documentation RST files from the repository (https://github.com/ansible-collections/community.vmware/pull/1897).
- Using semantic markup in documentation (https://github.com/ansible-collections/community.vmware/issues/1771).
- add moid property in the return value for the module(https://github.com/ansible-collections/community.vmware/pull/1855).
- add new snapshot_id option to the vmware_guest_snapshot module(https://github.com/ansible-collections/community.vmware/pull/1847).
- autoselect_datastore - add support to also look at NFS mounted filesystems (previously was just VMFS)
- vmware_cluster_drs_recommendations - Add the Module to apply the drs recommendations (https://github.com/ansible-collections/community.vmware/pull/1736)
- vmware_deploy_ovf - New parameter enable_hidden_properties to force OVF properties marked as `ovf:userConfigurable=false` to become user configurable (https://github.com/ansible-collections/community.vmware/issues/802).
- vmware_dvs_portgroup_info - add moid property in the return value for the module (https://github.com/ansible-collections/community.vmware/issues/1849).
- vmware_guest - add support for configuring vMotion and FT encryption (https://github.com/ansible-collections/community.vmware/issues/1069)
- vmware_guest_serial_port - add support for proxyURI parameter to enable use of a virtual serial port concentrator (https://github.com/ansible-collections/community.vmware/issues/1742)
- vmware_guest_snapshot - add new snapshot_id option (https://github.com/ansible-collections/community.vmware/pull/1847).
- vmware_host_datastore - added new datastore type 'vvol' for enabling creation/deletion of vVols datastores
- vmware_host_datastore - added new parameter resignature for supporting resignaturing an existing VMFS datastore on an imported/cloned LUN.
- vmware_host_snmp module now can configure SNMP agent on set of hosts (list in esxi_hostname parameter or as cluster in cluster_name parameter). The ability to configure the host directly remains (https://github.com/ansible-collections/community.vmware/issues/1799).
- vmware_vm_info -  Add `instance_uuid` to the result (https://github.com/ansible-collections/community.vmware/issues/1805)

community.windows
~~~~~~~~~~~~~~~~~

- win_dns_record - Added ``zone_scope`` option to manage a record in a specific zone scope

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

containers.podman
~~~~~~~~~~~~~~~~~

- Update docs
- podman_container - Add support for health-on-failure action
- podman_image -Add target support for podman build image
- podman_play - Add build and context_dir option to podman_play
- podman_pod - Add options for resource limits to podman_pod

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

- All the module documentation and examples are updated to use true or false for Boolean values.
- Module ``idrac_user`` is enhanced to configure custom privileges for an user.
- Module ``ome_application_certificate`` is enhanced to support subject alternative names.
- Module ``ome_diagnostics`` is enhanced to update changed flag status in response.
- Module ``ome_discovery`` is enhanced to add detailed job information of each IP discovered.
- Module ``ome_firmware_baseline`` is enhanced to support the option to select only components with no reboot required.
- Module ``ome_firmware_catalog`` is enhanced to support IPv6 address.
- Module ``ome_firmware`` is enhanced to support reboot type options.
- Module ``ome_job_info`` is enhanced to return last execution details and execution histories.
- Module ``redfish_firmware`` is enhanced to support IPv6 address.
- Module ``redfish_storage_volume`` is enhanced to support RAID6 and RAID60.
- Role ``idrac_os_deployment`` is enhanced to remove the auto installation of required libraries and to support custom ISO and kickstart file as input.
- Updated the idrac_gather_facts role to use jinja template filters.

dellemc.powerflex
~~~~~~~~~~~~~~~~~

- Added Ansible role to support creation and deletion of protection domain, storage pool and fault set.
- Added Ansible role to support installation and uninstallation of Active MQ.
- Added Ansible role to support installation and uninstallation of Gateway.
- Added Ansible role to support installation and uninstallation of LIA.
- Added Ansible role to support installation and uninstallation of MDM.
- Added Ansible role to support installation and uninstallation of SDC.
- Added Ansible role to support installation and uninstallation of SDR.
- Added Ansible role to support installation and uninstallation of SDS.
- Added Ansible role to support installation and uninstallation of TB.
- Added Ansible role to support installation and uninstallation of Web UI.
- Added sample playbooks for the modules.
- Added support for PowerFlex Denver version(4.5.x)
- Added support for SDC installation on ESXi, Rocky Linux and Windows OS.
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
- Patch update to fix import errors in utils file.

f5networks.f5_modules
~~~~~~~~~~~~~~~~~~~~~

- bigip_command - Added note to give appropriate timeout value for long running commands
- bigip_policy_rule - added six more options for ssl_extension condition

fortinet.fortimanager
~~~~~~~~~~~~~~~~~~~~~

- Corrected the behavior of module fmgr_pkg_firewall_consolidated_policy_sectionvalue and fmgr_pkg_firewall_securitypolicy_sectionvalue.
- Improve documentation.
- Some arguments can support both list or string format input now.
- Support newest versions for FortiManager v6.2 ~ v7.4

google.cloud
~~~~~~~~~~~~

- Add DataPlane V2 Support.
- Add auth support for GCP access tokens (#574).
- Add support for ip_allocation_policy->stack_type.

grafana.grafana
~~~~~~~~~~~~~~~

- Ability to configure date format in grafana server role by @RomainMou
- Add Grafana Agent Version and CPU Arch to Downloaded ZIP in Grafana Agent Role
- Add check for Curl and failure step if Agent Version is not retrieved
- Add overrides.conf with CAP_NET_BIND_SERVICE for grafana-server unit
- Allow alert resource provisioning in Grafana Role
- Avoid using shell for fetching latest version in Grafana Agent Role by @gardar
- Bump cryptography from 39.0.2 to 41.0.3
- Bump cryptography from 41.0.3 to 41.0.4
- Bump semver from 5.7.1 to 5.7.2
- Bump word-wrap from 1.2.3 to 1.2.5
- Create local dashboard directory in check mode
- Create missing notification directory in Grafana Role
- Datasource test updates and minor fixes
- Fix Deleting datasources
- Fix Grafana Dashboard Import for Grafana Role
- Fix alert_notification_policy failing on fresh instance
- Fix for invalid yaml with datasources list enclosed in quotes by @elkozmon
- Fix grafana dashboard import in Grafana Role
- Make grafana_agent Idempotent
- Making Deleting folders idempotent
- Move _grafana_agent_base_download_url from /vars to /defaults in Grafana Agent Role
- Provisioning errors in YAML
- Remove agent installation custom check by @VLZZZ
- Remove check_mode from create local directory task in Grafana Role
- Remove dependency on local-fs.target from Grafana Agent role
- Remove explicit user creation check by @v-zhuravlev
- Remove trailing slash automatically from grafana_url
- Update CI Testing
- Update Cloud Stack Module failures
- Update Download tasks in Grafana Agent Role
- Use 'ansible_system' env variable to detect os typ in Grafana Agent Role
- Use new standard to configure Grafana APT source for Grafana Role
- YAML Fixes
- hange grafana Agent Wal and Positions Directory in Grafana Agent Role
- indentation and Lint fixes to modules

hetzner.hcloud
~~~~~~~~~~~~~~

- Bundle hcloud python dependency inside the collection.
- Use the collection version in the hcloud user-agent instead of the ansible-core version.
- hcloud_datacenter_info - Add `server_types` field
- hcloud_floating_ip_info - Allow querying floating ip by name.
- hcloud_iso_info - Add deprecation field
- hcloud_iso_info Create hcloud_iso_info module
- hcloud_load_balancer_info - Add targets health status field.
- hcloud_load_balancer_network - Allow selecting a `load_balancer` or `network` using its ID.
- hcloud_load_balancer_service - Allow selecting a `load_balancer` using its ID.
- hcloud_load_balancer_target - Allow selecting a `load_balancer` or `server` using its ID.
- hcloud_network Add expose_routes_to_vswitch field.
- hcloud_network_info Return expose_routes_to_vswitch for network.
- hcloud_primary_ip_info Create hcloud_primary_ip_info module
- hcloud_rdns - Allow selecting a `server`, `floating_ip`, `primary_ip` or `load_balancer` using its ID.
- hcloud_route - Allow selecting a `network` using its ID.
- hcloud_server - Add `created` field
- hcloud_server Show warning if used server_type is deprecated.
- hcloud_server_info - Add `created` field
- hcloud_server_network - Allow selecting a `network` or `server` using its ID.
- hcloud_server_type_info - Add field included_traffic to returned server types
- hcloud_server_type_info Return deprecation info for server types.
- hcloud_subnetwork - Allow selecting to a `network` using its ID.
- inventory - Allow caching the hcloud inventory.
- python-dateutil >= 2.7.5 is now required by the collection. If you already have the hcloud package installed, this dependency should also be installed.
- requests >= 2.20 is now required by the collection. If you already have the hcloud package installed, this dependency should also be installed.

inspur.ispim
~~~~~~~~~~~~

- Change the ansible-test.yml application file version.
- Modify logical disk creation, add MV raid card compatible.
- The edit_bios module adds the list field.

junipernetworks.junos
~~~~~~~~~~~~~~~~~~~~~

- `junos_ospfv2` - Fix the authentication config when password is configured
- `junos_ospfv2` - Rename key ospf to ospfv2 in facts.
- `junos_ospfv2` - add area_ranges attribute which supports list of dict attributes.
- `junos_ospfv2` - add attributes `allow_route_leaking`, `stub_network` and `as-external` to overload dict.
- `junos_ospfv2` - add attributes `no_ignore_out_externals` to spf_options dict.
- `junos_ospfv2` - fix to gather reference_bandwidth and rfc1583compatibility.
- add acl_interfaces key for junos_facts output.
- add overridden state opperation support.

lowlydba.sqlserver
~~~~~~~~~~~~~~~~~~

- Add refresh workaround for agent schedule bug where properties returned are stale. (https://github.com/lowlydba/lowlydba.sqlserver/pull/185)
- Added SID as an optional parameter to the login module (https://github.com/lowlydba/lowlydba.sqlserver/pull/189)
- Added only_accessible as an optional parameter to the database module (https://github.com/lowlydba/lowlydba.sqlserver/pull/198)
- Fixes error handling for Remove-DbaDatabase when joined to AvailabilityGroup, exception was not being thrown so we have to parse Status

microsoft.ad
~~~~~~~~~~~~

- AD objects will no longer be moved to the default AD path for their type if no ``path`` was specified. Use the value ``microsoft.ad.default_path`` to explicitly set the path to the default path if that behaviour is desired.
- microsoft.ad.debug_ldap_client - Add ``dpapi_ng`` to list of packages checked
- microsoft.ad.ldap - Add support for decrypting LAPS encrypted password
- microsoft.ad.ldap - Added the option ``filter_without_computer`` to not add the AND clause ``objectClass=computer`` to the final filter used - https://github.com/ansible-collections/microsoft.ad/issues/55
- microsoft.ad.ldap - Allow setting LDAP connection and authentication options through environment variables - https://github.com/ansible-collections/microsoft.ad/issues/34

netapp.ontap
~~~~~~~~~~~~

- na_ontap_broadcast_domain - changed documentation for ipspace as it is required while using REST.
- na_ontap_cg_snapshot - added REST support to the cg snapshot module, requires ONTAP 9.10.1 or later.
- na_ontap_cifs_server - new option `default_site` added in REST, requires ONTAP 9.13.1 or later.
- na_ontap_ems_destination - new option ``certificate``, ``ca`` added.
- na_ontap_kerberos_realm - add REST support for `admin_server_ip`, `admin_server_port`, `pw_server_ip`, `pw_server_port` and `clock_skew` from ONTAP 9.13.1 or later
- na_ontap_lun - new option `qtree_name` added in REST.
- na_ontap_name_mappings - added choices ``s3_win`` and ``s3_unix`` to ``direction``, requires ONTAP 9.12.1 or later.
- na_ontap_net_ifgrp - return `name` and other details of a newly created interface group in module output in REST.
- na_ontap_qos_policy_group - added new REST only options `expected_iops_allocation` and `peak_iops_allocation`, requires ONTAP 9.10.1 or later.
- na_ontap_rest_info - new option `hal_linking` added to enable or disable HAL links.
- na_ontap_restit - returns changed as False for GET method.
- na_ontap_s3_buckets - new option ``nas_path`` added, requires ONTAP 9.12.1 or later.
- na_ontap_snmp - added REST support for snmpv3 user.
- na_ontap_user - Added warning message when password is not changed.
- na_ontap_volume - added REST support for `atime_update` requires ONTAP 9.8 or later, `snapdir_access` and `snapshot_auto_delete` requires ONTAP 9.13.1 or later.
- na_ontap_volume - added new REST only options `vol_nearly_full_threshold_percent` and `vol_full_threshold_percent`, requires ONTAP 9.9 or later.

netbox.netbox
~~~~~~~~~~~~~

- API - Add possibility to use Bearer token [#1023](https://github.com/netbox-community/ansible_modules/pull/1023)
- custom fields - Add datetime as an custom field option [#1019](https://github.com/netbox-community/ansible_modules/pull/1019)
- netbox_cable - Add tenant [#1027](https://github.com/netbox-community/ansible_modules/pull/1027)
- netbox_circuit_type, netbox_device_interface - Add missing options [#1025](https://github.com/netbox-community/ansible_modules/pull/1025)
- netbox_config_template - New module [#1090](https://github.com/netbox-community/ansible_modules/pull/1090)
- netbox_custom_field - Add hidden-ifunset option [#1048](https://github.com/netbox-community/ansible_modules/pull/1048)
- netbox_device - Add oob_ip to device [#1085](https://github.com/netbox-community/ansible_modules/pull/1085)
- netbox_device_type - Add default_platform [#1092](https://github.com/netbox-community/ansible_modules/pull/1092)
- netbox_inventory_item - Add role to module [#1050](https://github.com/netbox-community/ansible_modules/pull/1050)
- netbox_power_port - Add missing power port option [#1049](https://github.com/netbox-community/ansible_modules/pull/1049)

ovirt.ovirt
~~~~~~~~~~~

- ovirt_vm - Add tpm_enabled (https://github.com/oVirt/ovirt-ansible-collection/pull/722).
- storage_error_resume_behaviour - Support VM storage error resume behaviour "auto_resume", "kill", "leave_paused". (https://github.com/oVirt/ovirt-ansible-collection/pull/721)
- vm_infra - Support boot disk renaming and resizing. (https://github.com/oVirt/ovirt-ansible-collection/pull/705)

purestorage.flasharray
~~~~~~~~~~~~~~~~~~~~~~

- purefa_eradication - Added support for disabled and enabled timers from Purity//FA 6.4.10
- purefa_info - Add `port_connectivity` information for hosts
- purefa_info - Add array subscription data
- purefa_info - Add promotion status information for volumes
- purefa_info - Added `nfs_version` to policies and rules from Purity//FA 6.4.10
- purefa_info - Added `total_used` to multiple sections from Purity//FA 6.4.10
- purefa_info - Added support for autodir policies
- purefa_info - Prive array timezone from Purity//FA 6.4.10
- purefa_info - Report NTP Symmetric key presence from Purity//FA 6.4.10
- purefa_network - Add support for creating/modifying VIF and LACP_BOND interfaces
- purefa_network - `enabled` option added. This must now be used instead of state=absent to disable a physical interface as state=absent can now fully delete a non-physical interface
- purefa_ntp - Added support for NTP Symmetric Key from Purity//FA 6.4.10s
- purefa_offload - Added a new profile parameter.
- purefa_pgsched - Change `snap_at` and `replicate_at` to be AM or PM hourly
- purefa_pgsnap - Add protection group snapshot rename functionality
- purefa_pgsnap - Added new parameter to support snapshot throttling
- purefa_policy - Added support for autodir policies
- purefa_policy - Added support for multiple NFS versions from Purity//FA 6.4.10
- purefa_proxy - Add new protocol parameter, defaults to https
- purefa_snap - Added new parameter to support snapshot throttling
- purefa_vg - Add rename parameter

purestorage.flashblade
~~~~~~~~~~~~~~~~~~~~~~

- purefb_bucket_replica - Added support for cascading replica links
- purefb_fs - Added support for SMB client and share policies
- purefb_fs_replica - Added support to delete filesystem replica links from REST 2.10
- purefb_info - Add drive type in drives subset for //S and //E platforms. Only available from REST 2.9.
- purefb_info - Added support for SMB client and share policies
- purefb_info - New fields to display free space (remaining quota) for Accounts and Buckets. Space used by destroyed buckets is split out from virtual field to new destroyed_virtual field
- purefb_info - Report encryption state in SMB client policy rules
- purefb_info - Report more detailed space data from Purity//FB 4.3.0
- purefb_policy - Add deny effect for object store policy rules. Requires Purity//FB 4.3.0+
- purefb_policy - Add new and updated policy access rights
- purefb_policy - Added parameter to define object store policy description
- purefb_policy - Added support for SMB client and share policies
- purefb_s3acc - Allow human readable quota sizes; eg. 1T, 230K, etc
- purefb_s3user - Add new boolean parameter I(multiple_keys) to limit access keys for a user to a single key.

purestorage.fusion
~~~~~~~~~~~~~~~~~~

- FUSION_API_HOST && FUSION_HOST - changed logic, now this variables require host name without path
- Fusion authentication - add 'access_token' module's parameter and 'FUSION_ACCESS_TOKEN' environment variable, as an alternative way of the authentication.
- all modules - return resource's id parameter on update and create.
- fusion - added private key password, which is used to decrypt private key files
- fusion_array - added `apartment_id` argument, which can be used when creating an array.
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
- fusion_pg - introduced `destroy_snapshots_on_delete` which, if set to true, ensures that before deleting placement group, snapshots within the placement group will be deleted.
- fusion_pp - 'local_rpo' duration parsing documented, 'local_retention' minimum value fixed
- fusion_pp - Allow leading zeros in duration strings
- fusion_pp - Change the minimum value of the protection policy local retention from 1 to 10
- fusion_pp - duration parsing improved. Supports combination of time units (E.g 5H5M)
- fusion_pp - introduced `destroy_snapshots_on_delete` which, if set to true, ensures that before deleting protection policy, snapshots within the protection policy will be deleted.
- fusion_ra - added `api_client_key` argument, which can be used instead of `user` and `principal` argument
- fusion_ra - added `principal` argument, which is an ID of either API client or User and can be used instead of `user` argument
- fusion_se - add support for CBS Storage Endpoint
- fusion_volume - Allow creating a new volume from already existing volume or volume snapshot

sensu.sensu_go
~~~~~~~~~~~~~~

- Added Docker file configurations for Ubuntu 20.04 and 22.04
- Added aditional parameters for Postgres resource to datastore module
- Added bcrypt check to user module
- Added docs for backends and package_name filter
- Added symlink for AlmaLinux.yml for alma linux 9 support

t_systems_mms.icinga_director
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Add Icinga Deploy handler and module (https://github.com/T-Systems-MMS/ansible-collection-icinga-director/pull/205)

theforeman.foreman
~~~~~~~~~~~~~~~~~~

- compute_resource - add support for OpenStack
- content_view_filter - add deb filter type
- content_view_filter_rule - add spec for deb filter rules
- content_view_promote role - also accept all parameters of the `content_view_version` module (https://github.com/theforeman/foreman-ansible-modules/issues/1591)
- content_view_version - include information about the published version in the return value of the module
- job-invocation - add ``recurrence purpose`` and ``description_format`` parameters
- locations role - New role to manage locations
- organizations role - accept ``parameters`` and ``ignore_types`` like the module does
- repositories role - allow disabling/removing of repositories by setting the ``state`` parameter

vultr.cloud
~~~~~~~~~~~

- instance - Implemented a new ``state`` equal ``reinstalled`` to reinstall an existing instance (https://github.com/vultr/ansible-collection-vultr/pull/66).
- inventory - Added VPC/VPC 2.0 support by adding ``internal_ip`` to the attributes (https://github.com/vultr/ansible-collection-vultr/issues/86).
- inventory - Bare metal support has been implemented (https://github.com/vultr/ansible-collection-vultr/pull/63).

vyos.vyos
~~~~~~~~~

- vyos-l3_interface_support - Add support for Tunnel, Bridge and Dummy interfaces. (https://github.com/ansible-collections/vyos.vyos/issues/265)

Breaking Changes / Porting Guide
--------------------------------

Ansible-core
~~~~~~~~~~~~

- Any plugin using the config system and the `cli` entry to use the `timeout` from the command line, will see the value change if the use had configured it in any of the lower precedence methods. If relying on this behaviour to consume the global/generic timeout from the DEFAULT_TIMEOUT constant, please consult the documentation on plugin configuration to add the overlaping entries.
- ansible-test - Test plugins that rely on containers no longer support reusing running containers. The previous behavior was an undocumented, untested feature.
- service module will not permanently configure variables/flags for openbsd when doing enable/disable operation anymore, this module was never meant to do this type of work, just to manage the service state itself. A rcctl_config or similar module should be created and used instead.

amazon.aws
~~~~~~~~~~

- The amazon.aws collection has dropped support for ``botocore<1.29.0`` and ``boto3<1.26.0``. Most modules will continue to work with older versions of the AWS SDK, however compatability with older versions of the SDK is not guaranteed and will not be tested. When using older versions of the SDK a warning will be emitted by Ansible (https://github.com/ansible-collections/amazon.aws/pull/1763).
- amazon.aws collection - due to the AWS SDKs announcing the end of support for Python less than 3.7 (https://aws.amazon.com/blogs/developer/python-support-policy-updates-for-aws-sdks-and-tools/) support for Python less than 3.7 by this collection wss been deprecated in release 6.0.0 and removed in release 7.0.0. (https://github.com/ansible-collections/amazon.aws/pull/1763).
- module_utils - ``module_utils.urls`` was previously deprecated and has been removed (https://github.com/ansible-collections/amazon.aws/pull/1540).
- module_utils._version - vendored copy of distutils.version has been dropped (https://github.com/ansible-collections/amazon.aws/pull/1587).

community.aws
~~~~~~~~~~~~~

- The community.aws collection has dropped support for ``botocore<1.29.0`` and ``boto3<1.26.0``. Most modules will continue to work with older versions of the AWS SDK, however compatability with older versions of the SDK is not guaranteed and will not be tested. When using older versions of the SDK a warning will be emitted by Ansible (https://github.com/ansible-collections/amazon.aws/pull/1763).
- aws_region_info - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.aws_region_info``.
- aws_s3_bucket_info - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.aws_s3_bucket_info``.
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

community.general
~~~~~~~~~~~~~~~~~

- collection_version lookup plugin - remove compatibility code for ansible-base 2.10 and ansible-core 2.11 (https://github.com/ansible-collections/community.general/pull/7269).
- gitlab_project - add ``default_branch`` support for project update. If you used the module so far with ``default_branch`` to update a project, the value of ``default_branch`` was ignored. Make sure that you either do not pass a value if you are not sure whether it is the one you want to have to avoid unexpected breaking changes (https://github.com/ansible-collections/community.general/pull/7158).
- selective callback plugin - remove compatibility code for Ansible 2.9 and ansible-core 2.10 (https://github.com/ansible-collections/community.general/pull/7269).
- vardict module utils - ``VarDict`` will no longer accept variables named ``_var``, ``get_meta``, and ``as_dict`` (https://github.com/ansible-collections/community.general/pull/6647).
- version module util - remove fallback for ansible-core 2.11. All modules and plugins that do version collections no longer work with ansible-core 2.11 (https://github.com/ansible-collections/community.general/pull/7269).

community.hashi_vault
~~~~~~~~~~~~~~~~~~~~~

- The minimum required version of ``hvac`` is now ``1.2.1`` (https://docs.ansible.com/ansible/devel/collections/community/hashi_vault/docsite/user_guide.html#hvac-version-specifics).

community.vmware
~~~~~~~~~~~~~~~~

- Removed support for ansible-core version < 2.15.0.
- vmware_dvs_host - removed defaults for `vmnics` and `lag_uplinks` (https://github.com/ansible-collections/community.vmware/issues/1516).
- vmware_host_acceptance - removed `acceptance_level` and used its options in `state`. This also means there will be no state `list` anymore. In order to get information about the current acceptance level, use the new module `vmware_host_acceptance_info` (https://github.com/ansible-collections/community.vmware/issues/1872).
- vmware_vm_info - added prefix length to IP addresses in vm_network, so they now show up as for example 10.76.33.228/24 instead of just 10.76.33.228 (https://github.com/ansible-collections/community.vmware/issues/1761).

dellemc.enterprise_sonic
~~~~~~~~~~~~~~~~~~~~~~~~

- sonic_aaa - Add default_auth attribute to the argspec to replace the deleted group and local attributes. This change allows for ordered login authentication. (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/195).

hetzner.hcloud
~~~~~~~~~~~~~~

- Drop support for ansible-core 2.12
- Drop support for python 3.7
- hcloud-python 1.20.0 is now required for full compatibility
- inventory plugin - Don't set the server image variables (`image_id`, `image_os_flavor` and `image_name`) when the server image is not defined.

Deprecated Features
-------------------

- The ``community.azure`` collection is officially unmaintained and has been archived. Therefore, it will be removed from Ansible 10. There is already a successor collection ``azure.azcollection`` in the community package which should cover the same functionality (https://github.com/ansible-community/community-topics/issues/263).
- The ``hpe.nimble`` collection is considered unmaintained and will be removed from Ansible 10 if no one starts maintaining it again before Ansible 10. See `the removal process for details on how this works <https://github.com/ansible-collections/overview/blob/main/removal_from_ansible.rst#cancelling-removal-of-an-unmaintained-collection>`__ (https://github.com/ansible-community/community-topics/issues/254).
- The collection ``community.sap`` has been renamed to ``community.sap_libs``. For now both collections are included in Ansible. The content in ``community.sap`` has deprecated redirects to the new collection in Ansible 9.0.0, and the collection will be removed from Ansible 10 completely. Please update your FQCNs for ``community.sap``.
- The collection ``ibm.spectrum_virtualize`` has been renamed to ``ibm.storage_virtualize``. For now, both collections are included in Ansible. The content in ``ibm.spectrum_virtualize`` will be replaced with deprecated redirects to the new collection in Ansible 10.0.0, and these redirects will eventually be removed from Ansible. Please update your FQCNs for ``ibm.spectrum_virtualize``.
- The collection ``t_systems_mms.icinga_director`` has been renamed to ``telekom_mms.icinga_director``. For now both collections are included in Ansible. The content in ``t_systems_mms.icinga_director`` has been replaced with deprecated redirects to the new collection in Ansible 9.0.0, and these redirects will be removed from Ansible 11. Please update your FQCNs for ``t_systems_mms.icinga_director``.
- The netapp.azure collection is considered unmaintained and will be removed from Ansible 10 if no one starts maintaining it again before Ansible 10. See `the removal process for details on how this works <https://github.com/ansible-collections/overview/blob/main/removal_from_ansible.rst#cancelling-removal-of-an-unmaintained-collection>`__ (https://github.com/ansible-community/community-topics/issues/234).
- The netapp.elementsw collection is considered unmaintained and will be removed from Ansible 10 if no one starts maintaining it again before Ansible 10. See `the removal process for details on how this works <https://github.com/ansible-collections/overview/blob/main/removal_from_ansible.rst#cancelling-removal-of-an-unmaintained-collection>`__ (https://github.com/ansible-community/community-topics/issues/235).
- The netapp.um_info collection is considered unmaintained and will be removed from Ansible 10 if no one starts maintaining it again before Ansible 10. See `the removal process for details on how this works <https://github.com/ansible-collections/overview/blob/main/removal_from_ansible.rst#cancelling-removal-of-an-unmaintained-collection>`__ (https://github.com/ansible-community/community-topics/issues/244).

Ansible-core
~~~~~~~~~~~~

- Deprecated ini config option ``collections_paths``, use the singular form ``collections_path`` instead
- Deprecated the env var ``ANSIBLE_COLLECTIONS_PATHS``, use the singular form ``ANSIBLE_COLLECTIONS_PATH`` instead
- Old style vars plugins which use the entrypoints `get_host_vars` or `get_group_vars` are deprecated. The plugin should be updated to inherit from `BaseVarsPlugin` and define a `get_vars` method as the entrypoint.
- Support for Windows Server 2012 and 2012 R2 has been removed as the support end of life from Microsoft is October 10th 2023. These versions of Windows will no longer be tested in this Ansible release and it cannot be guaranteed that they will continue to work going forward.
- ``STRING_CONVERSION_ACTION`` config option is deprecated as it is no longer used in the Ansible Core code base.
- the 'smart' option for setting a connection plugin is being removed as its main purpose (choosing between ssh and paramiko) is now irrelevant.
- vault and unfault filters - the undocumented ``vaultid`` parameter is deprecated and will be removed in ansible-core 2.20. Use ``vault_id`` instead.
- yum_repository - deprecated parameter 'keepcache' (https://github.com/ansible/ansible/issues/78693).

amazon.aws
~~~~~~~~~~

- ec2_instance - deprecation of ``tenancy`` and ``placement_group`` in favor of ``placement`` attribute  (https://github.com/ansible-collections/amazon.aws/pull/1825).
- s3_object - support for passing object keys with a leading ``/`` has been deprecated and will be removed in a release after 2025-12-01 (https://github.com/ansible-collections/amazon.aws/pull/1549).

ansible.netcommon
~~~~~~~~~~~~~~~~~

- libssh - the ssh_*_args options are now marked that they will be removed after 2026-01-01.

ansible.windows
~~~~~~~~~~~~~~~

- Add warning when using Server 2012 or 2012 R2 with the ``setup`` module. These OS' are nearing the End of Life and will not be tested in CI when that time is reached.
- win_domain - Module is deprecated in favour of the ``microsoft.ad.domain`` module, the ``ansible.windows.win_domain`` module will be removed in the ``3.0.0`` release of this collection.
- win_domain_controller - Module is deprecated in favour of the ``microsoft.ad.domain_controller`` module, the ``ansible.windows.win_domain_controller`` module will be removed in the ``3.0.0`` release of this collection.
- win_domain_membership - Module is deprecated in favour of the ``microsoft.ad.membership`` module, the ``ansible.windows.win_domain_membership`` module will be removed in the ``3.0.0`` release of this collection.

cisco.ios
~~~~~~~~~

- ios_snmp_server - deprecate traps.envmon.fan with traps.envmon.fan_enable
- ios_snmp_server - deprecate traps.mpls_vpn with traps.mpls
- ospfv2 - removed passive_interface to passive_interfaces that supports a list of interfaces

cisco.iosxr
~~~~~~~~~~~

- Deprecated iosxr_bgp module in favor of iosxr_bgp_global,iosxr_bgp_neighbor_address_family and iosxr_bgp_address_family.
- iosxr_l2_interfaces - deprecate q_vlan with qvlan which allows vlans in str format e.g "any"

community.ciscosmb
~~~~~~~~~~~~~~~~~~

- support for Python 2.6 nad 2.7
- support for ansible 2.9

community.crypto
~~~~~~~~~~~~~~~~

- get_certificate - the default ``false`` of the ``asn1_base64`` option is deprecated and will change to ``true`` in community.crypto 3.0.0 (https://github.com/ansible-collections/community.crypto/pull/600).

community.general
~~~~~~~~~~~~~~~~~

- CmdRunner module utils - deprecate ``cmd_runner_fmt.as_default_type()`` formatter (https://github.com/ansible-collections/community.general/pull/6601).
- MH VarsMixin module utils - deprecates ``VarsMixin`` and supporting classes in favor of plain ``vardict`` module util (https://github.com/ansible-collections/community.general/pull/6649).
- The next major release, community.general 8.0.0, will drop support for ansible-core 2.11 and 2.12, which have been End of Life for some time now. This means that this collection no longer supports Python 2.6 on the target. Individual content might still work with unsupported ansible-core versions, but that can change at any time. Also please note that from now on, for every new major community.general release, we will drop support for all ansible-core versions that have been End of Life for more than a few weeks on the date of the major release (https://github.com/ansible-community/community-topics/discussions/271, https://github.com/ansible-collections/community.general/pull/7259).
- ansible_galaxy_install - the ``ack_ansible29`` and ``ack_min_ansiblecore211`` options have been deprecated and will be removed in community.general 9.0.0 (https://github.com/ansible-collections/community.general/pull/7358).
- consul - the ``ack_params_state_absent`` option has been deprecated and will be removed in community.general 10.0.0 (https://github.com/ansible-collections/community.general/pull/7358).
- cpanm - value ``compatibility`` is deprecated as default for parameter ``mode`` (https://github.com/ansible-collections/community.general/pull/6512).
- ejabberd_user - deprecate the parameter ``logging`` in favour of producing more detailed information in the module output (https://github.com/ansible-collections/community.general/pull/7043).
- flowdock - module relies entirely on no longer responsive API endpoints, and it will be removed in community.general 9.0.0 (https://github.com/ansible-collections/community.general/pull/6930).
- proxmox - old feature flag ``proxmox_default_behavior`` will be removed in community.general 10.0.0 (https://github.com/ansible-collections/community.general/pull/6836).
- proxmox_kvm - deprecate the option ``proxmox_default_behavior`` (https://github.com/ansible-collections/community.general/pull/7377).
- redfish_info, redfish_config, redfish_command - the default value ``10`` for the ``timeout`` option is deprecated and will change to ``60`` in community.general 9.0.0 (https://github.com/ansible-collections/community.general/pull/7295).
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
- stackdriver - module relies entirely on no longer existent API endpoints, and it will be removed in community.general 9.0.0 (https://github.com/ansible-collections/community.general/pull/6887).
- webfaction_app - module relies entirely on no longer existent API endpoints, and it will be removed in community.general 9.0.0 (https://github.com/ansible-collections/community.general/pull/6909).
- webfaction_db - module relies entirely on no longer existent API endpoints, and it will be removed in community.general 9.0.0 (https://github.com/ansible-collections/community.general/pull/6909).
- webfaction_domain - module relies entirely on no longer existent API endpoints, and it will be removed in community.general 9.0.0 (https://github.com/ansible-collections/community.general/pull/6909).
- webfaction_mailbox - module relies entirely on no longer existent API endpoints, and it will be removed in community.general 9.0.0 (https://github.com/ansible-collections/community.general/pull/6909).
- webfaction_site - module relies entirely on no longer existent API endpoints, and it will be removed in community.general 9.0.0 (https://github.com/ansible-collections/community.general/pull/6909).

community.postgresql
~~~~~~~~~~~~~~~~~~~~

- postgresql_lang - the module has been deprecated and will be removed in ``community.postgresql 4.0.0``. Please use the ``postgresql_ext`` module instead (https://github.com/ansible-collections/community.postgresql/issues/559).

community.sap
~~~~~~~~~~~~~

- community.sap.hana_query - is deprecated in favor of community.sap_libs.sap_hdbsql
- community.sap.sap_company - is deprecated in favor of community.sap_libs.sap_company
- community.sap.sap_snote - is deprecated in favor of community.sap_libs.sap_snote
- community.sap.sap_task_list_execute - is deprecated in favor of community.sap_libs.sap_task_list_execute
- community.sap.sap_user - is deprecated in favor of community.sap_libs.sap_user
- community.sap.sapcar_extract - is deprecated in favor of community.sap_libs.sapcar_extract

community.windows
~~~~~~~~~~~~~~~~~

- win_domain_computer - Module is deprecated in favour of the ``microsoft.ad.computer`` module, the ``community.windows.win_domain_computer`` module will be removed in the ``3.0.0`` release of this collection.
- win_domain_group - Module is deprecated in favour of the ``microsoft.ad.group`` module, the ``community.windows.win_domain_group`` module will be removed in the ``3.0.0`` release of this collection.
- win_domain_group_membership - Module is deprecated in favour of the ``microsoft.ad.group`` module, the ``community.windows.win_domain_group_membership`` module will be removed in the ``3.0.0`` release of this collection.
- win_domain_object_info - Module is deprecated in favour of the ``microsoft.ad.object_info`` module, the ``community.windows.win_domain_object_info`` module will be removed in the ``3.0.0`` release of this collection.
- win_domain_ou - Module is deprecated in favour of the ``microsoft.ad.ou`` module, the ``community.windows.win_domain_ou`` module will be removed in the ``3.0.0`` release of this collection.
- win_domain_user - Module is deprecated in favour of the ``microsoft.ad.user`` module, the ``community.windows.win_domain_user`` module will be removed in the ``3.0.0`` release of this collection.

junipernetworks.junos
~~~~~~~~~~~~~~~~~~~~~

- `junos_ospfv2` - add deprecate warning for area_range.
- add deprecate warning for junos_acl_interfaces key for junos facts results.

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

t_systems_mms.icinga_director
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- All modules and plugins are moved to the new namespace telekom_mms. Please update your code accordingly.

Removed Features (previously deprecated)
----------------------------------------

- The deprecated servicenow.servicenow collection has been removed from Ansible 7, but accidentally re-added to Ansible 8. It has been removed again from Ansible 9 (https://github.com/ansible-community/community-topics/issues/246).
- The ngine_io.vultr collection has been removed from Ansible 9, because it is officially unmaintained and has been archived. The successor collection ``vultr.cloud`` (using the recent v2 Vultr API) covers the same functionality but might not have compatible syntax (https://github.com/ansible-community/community-topics/issues/257).
- ``cisco.nso`` was considered unmaintained and removed from Ansible 9 as per the `removal from Ansible process <https://github.com/ansible-collections/overview/blob/main/removal_from_ansible.rst#unmaintained-collections>`_. Users can still install this collection with ``ansible-galaxy collection install cisco.nso``.
- ``community.fortios`` was considered unmaintained and removed from Ansible 9 as per the `removal from Ansible process <https://github.com/ansible-collections/overview/blob/main/removal_from_ansible.rst#unmaintained-collections>`_. Users can still install this collection with ``ansible-galaxy collection install community.fortios``.
- ``community.google`` was considered unmaintained and removed from Ansible 9 as per the `removal from Ansible process <https://github.com/ansible-collections/overview/blob/main/removal_from_ansible.rst#unmaintained-collections>`_. Users can still install this collection with ``ansible-galaxy collection install community.google``.
- ``community.skydive`` was considered unmaintained and removed from Ansible 9 as per the `removal from Ansible process <https://github.com/ansible-collections/overview/blob/main/removal_from_ansible.rst#unmaintained-collections>`_. Users can still install this collection with ``ansible-galaxy collection install community.skydive``.

Ansible-core
~~~~~~~~~~~~

- ActionBase - remove deprecated ``_remote_checksum`` method
- PlayIterator - remove deprecated ``cache_block_tasks`` and ``get_original_task`` methods
- Remove deprecated ``FileLock`` class
- Removed Python 3.9 as a supported version on the controller. Python 3.10 or newer is required.
- Removed ``include`` which has been deprecated in Ansible 2.12. Use ``include_tasks`` or ``import_tasks`` instead.
- ``Templar`` - remove deprecated ``shared_loader_obj`` parameter of ``__init__``
- ``fetch_url`` - remove auto disabling ``decompress`` when gzip is not available
- ``get_action_args_with_defaults`` - remove deprecated ``redirected_names`` method parameter
- ansible-test - Removed support for the remote Windows targets 2012 and 2012-R2
- inventory_cache - remove deprecated ``default.fact_caching_prefix`` ini configuration option, use ``defaults.fact_caching_prefix`` instead.
- module_utils/basic.py - Removed Python 3.5 as a supported remote version. Python 2.7 or Python 3.6+ is now required.
- stat - removed unused `get_md5` parameter.

ansible.windows
~~~~~~~~~~~~~~~

- win_get_url - Removed the deprecated option alias ``passwordd``, use ``url_password`` instead.
- win_get_url - Removed the deprecated option alias ``user`` and ``username``, use ``url_username`` instead.
- win_package - Removed deprecated module option ``ensure``, use ``state`` instead.
- win_package - Removed deprecated module option ``productid``, use ``product_id`` instead.
- win_package - Removed deprecated module option ``username``, ``user_name``, ``password``, and ``user_password``. Use ``become`` with ``become_flags: logon_type=new_credentials logon_flags=netcredentials_only`` on the task instead to replicate the same functionality instead.
- win_reboot - Removed backwards compatibility check where ``ignore_errors: true`` will be treated like ``ignore_unreachable: true``. Going forward ``ignore_errors: true`` will only ignore errors the plugin encountered and not an unreachable host. Use ``ignore_unreachable: true`` to ignore that error like any other module.
- win_regedit - Removed support for using a ``path`` with forward slashes as a key separator. Using a forward slash has been deprecated since Ansible 2.9. If using forward slashes in the ``win_regedit`` ``path`` value, make sure to change the forward slash ``/`` to a backslash ``\``. If enclosed in double quotes the backslash will have to be doubled up.
- win_updates - Removed deprecated alias ``blacklist``, use ``reject_list`` instead.
- win_updates - Removed deprecated alias ``whitelist``, use ``accept_list`` instead.
- win_updates - Removed deprecated module option ``use_scheduled_task``. This option did not change any functionality in the module and can be safely removed from the task entry.
- win_uri - Removed the deprecated option alias ``password``, use ``url_password`` instead.
- win_uri - Removed the deprecated option alias ``user`` and ``username``, use ``url_username`` instead.

cisco.ios
~~~~~~~~~

- Deprecated ios_logging module in favor of ios_logging_global.
- Deprecated next_hop_self attribute for bgp_address_family with nexthop_self.

cisco.nxos
~~~~~~~~~~

- The nxos_bgp module has been removed with this release.
- The nxos_bgp_af module has been removed with this release.
- The nxos_bgp_neighbor module has been removed with this release.
- The nxos_bgp_neighbor_af module has been removed with this release.

community.ciscosmb
~~~~~~~~~~~~~~~~~~

- remove testing for Python 2.6 nad 2.7
- remove testing for ansible 2.9

community.general
~~~~~~~~~~~~~~~~~

- The collection no longer supports ansible-core 2.11 and ansible-core 2.12. Parts of the collection might still work on these ansible-core versions, but others might not (https://github.com/ansible-collections/community.general/pull/7269).
- ansible_galaxy_install - support for Ansible 2.9 and ansible-base 2.10 has been removed (https://github.com/ansible-collections/community.general/pull/7358).
- consul - when ``state=absent``, the options ``script``, ``ttl``, ``tcp``, ``http``, and ``interval`` can no longer be specified (https://github.com/ansible-collections/community.general/pull/7358).
- gconftool2 - ``state=get`` has been removed. Use the module ``community.general.gconftool2_info`` instead (https://github.com/ansible-collections/community.general/pull/7358).
- gitlab_runner - remove the default value for the ``access_level`` option. To restore the previous behavior, explicitly set it to ``ref_protected`` (https://github.com/ansible-collections/community.general/pull/7358).
- htpasswd - removed code for passlib <1.6 (https://github.com/ansible-collections/community.general/pull/6901).
- manageiq_polices - ``state=list`` has been removed. Use the module ``community.general.manageiq_policies_info`` instead (https://github.com/ansible-collections/community.general/pull/7358).
- manageiq_tags - ``state=list`` has been removed. Use the module ``community.general.manageiq_tags_info`` instead (https://github.com/ansible-collections/community.general/pull/7358).
- mh.mixins.cmd module utils - the ``ArgFormat`` class has been removed (https://github.com/ansible-collections/community.general/pull/7358).
- mh.mixins.cmd module utils - the ``CmdMixin`` mixin has been removed. Use ``community.general.plugins.module_utils.cmd_runner.CmdRunner`` instead (https://github.com/ansible-collections/community.general/pull/7358).
- mh.mixins.cmd module utils - the mh.mixins.cmd module utils has been removed after all its contents were removed (https://github.com/ansible-collections/community.general/pull/7358).
- mh.module_helper module utils - the ``CmdModuleHelper`` and ``CmdStateModuleHelper`` classes have been removed. Use ``community.general.plugins.module_utils.cmd_runner.CmdRunner`` instead (https://github.com/ansible-collections/community.general/pull/7358).
- proxmox module utils - removed unused imports (https://github.com/ansible-collections/community.general/pull/6873).
- xfconf - the deprecated ``disable_facts`` option was removed (https://github.com/ansible-collections/community.general/pull/7358).

community.hashi_vault
~~~~~~~~~~~~~~~~~~~~~

- The minimum supported version of ``ansible-core`` is now ``2.14``, support for ``2.13`` has been dropped (https://github.com/ansible-collections/community.hashi_vault/pull/403).

community.vmware
~~~~~~~~~~~~~~~~

- Removed module util `version` (https://github.com/ansible-collections/community.vmware/issues/1639).
- vmware_guest - removed specifying CDROM configuration as a dict, instead use a list (https://github.com/ansible-collections/community.vmware/issues/1472).
- vmware_host_lockdown - removed deprecated states `absent` and `present` (https://github.com/ansible-collections/community.vmware/issues/1517).
- vmware_rest_client - removed deprecated method `get_tag_by_category()` (https://github.com/ansible-collections/community.vmware/issues/1898).

community.windows
~~~~~~~~~~~~~~~~~

- Removed testing for Server 2012 and Server 2012 R2 as they are reaching End of Life status from Microsoft. These OS versions may continue to work but will not be tested in CI.
- win_nssm - Removed the deprecated module option ``app_parameters``, use ``arguments`` instead.
- win_psmodule - Removed the deprecated module option ``url``, use ``community.windows.win_psrepository`` to manage repositories instead
- win_psmodule - Will no longer remove the ``repository`` specified when ``state: absent``, use ``community.windows.win_psrepository`` to manage repositories instead
- win_scheduled_tasks - Removed support for a trigger ``repetition`` to be defined as a list of dictionary entries. Specify the ``repetition`` as a dictionary value rather than a list of dictionaries.

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- The ``dellemc_get_firmware_inventory`` module is removed and replaced with the module ``idrac_firmware_info``.
- The ``dellemc_get_system_inventory`` module is removed and replaced with the module ``idrac_system_info``.

hetzner.hcloud
~~~~~~~~~~~~~~

- hcloud_datacenter_facts Removed deprecated facts module
- hcloud_floating_ip_facts Removed deprecated facts module
- hcloud_image_facts Removed deprecated facts module
- hcloud_location_facts Removed deprecated facts module
- hcloud_server_facts Removed deprecated facts module
- hcloud_server_type_facts Removed deprecated facts module
- hcloud_ssh_key_facts Removed deprecated facts module
- hcloud_volume_facts Removed deprecated facts module

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
- AnsibleModule.run_command - Only use selectors when needed, and rely on Python stdlib subprocess for the simple task of collecting stdout/stderr when prompt matching is not required.
- Cache host_group_vars after instantiating it once and limit the amount of repetitive work it needs to do every time it runs.
- Call PluginLoader.all() once for vars plugins, and load vars plugins that run automatically or are enabled specifically by name subsequently.
- Display - Defensively configure writing to stdout and stderr with a custom encoding error handler that will replace invalid characters while providing a deprecation warning that non-utf8 text will result in an error in a future version.
- Exclude internal options from man pages and docs.
- Fix ``ansible-config init`` man page option indentation.
- Fix ``ast`` deprecation warnings for ``Str`` and ``value.s`` when using Python 3.12.
- Fix ``run_once`` being incorrectly interpreted on handlers (https://github.com/ansible/ansible/issues/81666)
- Fix exceptions caused by various inputs when performing arg splitting or parsing key/value pairs. Resolves issue https://github.com/ansible/ansible/issues/46379 and issue https://github.com/ansible/ansible/issues/61497
- Fix incorrect parsing of multi-line Jinja2 blocks when performing arg splitting or parsing key/value pairs.
- Fix post-validating looped task fields so the strategy uses the correct values after task execution.
- Fixed `pip` module failure in case of usage quotes for `virtualenv_command` option for the venv command. (https://github.com/ansible/ansible/issues/76372)
- From issue https://github.com/ansible/ansible/issues/80880, when notifying a handler from another handler, handler notifications must be registered immediately as the flush_handler call is not recursive.
- Import ``FILE_ATTRIBUTES`` from ``ansible.module_utils.common.file`` in ``ansible.module_utils.basic`` instead of defining it twice.
- Inventory scripts parser not treat exception when getting hostsvar (https://github.com/ansible/ansible/issues/81103)
- On Python 3 use datetime methods ``fromtimestamp`` and ``now`` with UTC timezone instead of ``utcfromtimestamp`` and ``utcnow``, which are deprecated in Python 3.12.
- PluginLoader - fix Jinja plugin performance issues (https://github.com/ansible/ansible/issues/79652)
- PowerShell - Remove some code which is no longer valid for dotnet 5+
- Prevent running same handler multiple times when included via ``include_role`` (https://github.com/ansible/ansible/issues/73643)
- Prompting - add a short sleep between polling for user input to reduce CPU consumption (https://github.com/ansible/ansible/issues/81516).
- Properly disable ``jinja2_native`` in the template module when jinja2 override is used in the template (https://github.com/ansible/ansible/issues/80605)
- Properly template tags in parent blocks (https://github.com/ansible/ansible/issues/81053)
- Remove unreachable parser error for removed ``static`` parameter of ``include_role``
- Replace uses of ``configparser.ConfigParser.readfp()`` which was removed in Python 3.12 with ``configparser.ConfigParser.read_file()`` (https://github.com/ansible/ansible/issues/81656)
- Set filters ``intersect``, ``difference``, ``symmetric_difference`` and ``union`` now always return a ``list``, never a ``set``. Previously, a ``set`` would be returned if the inputs were a hashable type such as ``str``, instead of a collection, such as a ``list`` or ``tuple``.
- Set filters ``intersect``, ``difference``, ``symmetric_difference`` and ``union`` now use set operations when the given items are hashable. Previously, list operations were performed unless the inputs were a hashable type such as ``str``, instead of a collection, such as a ``list`` or ``tuple``.
- Switch result queue from a ``multiprocessing.queues.Queue` to ``multiprocessing.queues.SimpleQueue``, primarily to allow properly handling pickling errors, to prevent an infinite hang waiting for task results
- The ``ansible-config init`` command now has a documentation description.
- The ``ansible-galaxy collection download`` command now has a documentation description.
- The ``ansible-galaxy collection install`` command documentation is now visible (previously hidden by a decorator).
- The ``ansible-galaxy collection verify`` command now has a documentation description.
- The ``ansible-galaxy role install`` command documentation is now visible (previously hidden by a decorator).
- The ``ansible-inventory`` command command now has a documentation description (previously used as the epilog).
- The ``hostname`` module now also updates both current and permanent hostname on OpenBSD. Before it only updated the permanent hostname (https://github.com/ansible/ansible/issues/80520).
- Update module_utils.urls unit test to work with cryptography >= 41.0.0.
- When generating man pages, use ``func`` to find the command function instead of looking it up by the command name.
- ``StrategyBase._process_pending_results`` - create a ``Templar`` on demand for templating ``changed_when``/``failed_when``.
- ``ansible-galaxy`` now considers all collection paths when identifying which collection requirements are already installed. Use the ``COLLECTIONS_PATHS`` and ``COLLECTIONS_SCAN_SYS_PATHS`` config options to modify these. Previously only the install path was considered when resolving the candidates. The install path will remain the only one potentially modified. (https://github.com/ansible/ansible/issues/79767, https://github.com/ansible/ansible/issues/81163)
- ``ansible.module_utils.service`` - ensure binary data transmission in ``daemonize()``
- ``ansible.module_utils.service`` - fix inter-process communication in ``daemonize()``
- ``import_role`` reverts to previous behavior of exporting vars at compile time.
- ``pkg_mgr`` - fix the default dnf version detection
- ansiballz - Prevent issue where the time on the control host could change part way through building the ansiballz file, potentially causing a pre-1980 date to be used during ansiballz unpacking leading to a zip file error (https://github.com/ansible/ansible/issues/80089)
- ansible terminal color settings were incorrectly limited to 16 options via 'choices', removing so all 256 can be accessed.
- ansible-console - fix filtering by collection names when a collection search path was set (https://github.com/ansible/ansible/pull/81450).
- ansible-galaxy - Enabled the ``data`` tarfile filter during role installation for Python versions that support it. A probing mechanism is used to avoid Python versions with a broken implementation.
- ansible-galaxy - Fix issue installing collections containing directories with more than 100 characters on python versions before 3.10.6
- ansible-galaxy - Fix variable type error when installing subdir collections (https://github.com/ansible/ansible/issues/80943)
- ansible-galaxy - Provide a better error message when using a requirements file with an invalid format - https://github.com/ansible/ansible/issues/81901
- ansible-galaxy - fix installing collections from directories that have a trailing path separator (https://github.com/ansible/ansible/issues/77803).
- ansible-galaxy - fix installing signed collections (https://github.com/ansible/ansible/issues/80648).
- ansible-galaxy - reduce API calls to servers by fetching signatures only for final candidates.
- ansible-galaxy - started allowing the use of pre-releases for collections that do not have any stable versions published. (https://github.com/ansible/ansible/pull/81606)
- ansible-galaxy - started allowing the use of pre-releases for dependencies on any level of the dependency tree that specifically demand exact pre-release versions of collections and not version ranges. (https://github.com/ansible/ansible/pull/81606)
- ansible-galaxy collection verify - fix verifying signed collections when the keyring is not configured.
- ansible-galaxy info - fix reporting no role found when lookup_role_by_name returns None.
- ansible-inventory - index available_hosts for major performance boost when dumping large inventories
- ansible-test - Add a ``pylint`` plugin to work around a known issue on Python 3.12.
- ansible-test - Add support for ``argcomplete`` version 3.
- ansible-test - All containers created by ansible-test now include the current test session ID in their name. This avoids conflicts between concurrent ansible-test invocations using the same container host.
- ansible-test - Always use ansible-test managed entry points for ansible-core CLI tools when not running from source. This fixes issues where CLI entry points created during install are not compatible with ansible-test.
- ansible-test - Fix a traceback that occurs when attempting to test Ansible source using a different ansible-test. A clear error message is now given when this scenario occurs.
- ansible-test - Fix handling of timeouts exceeding one day.
- ansible-test - Fix parsing of cgroup entries which contain a ``:`` in the path (https://github.com/ansible/ansible/issues/81977).
- ansible-test - Fix several possible tracebacks when using the ``-e`` option with sanity tests.
- ansible-test - Fix various cases where the test timeout could expire without terminating the tests.
- ansible-test - Include missing ``pylint`` requirements for Python 3.10.
- ansible-test - Pre-build a PyYAML wheel before installing requirements to avoid a potential Cython build failure.
- ansible-test - Remove redundant warning about missing programs before attempting to execute them.
- ansible-test - The ``import`` sanity test now checks the collection loader for remote-only Python support when testing ansible-core.
- ansible-test - Unit tests now report warnings generated during test runs. Previously only warnings generated during test collection were reported.
- ansible-test - Update ``pylint`` to 2.17.2 to resolve several possible false positives.
- ansible-test - Update ``pylint`` to 2.17.3 to resolve several possible false positives.
- ansible-test - Update ``pylint`` to version 3.0.1.
- ansible-test - Use ``raise ... from ...`` when raising exceptions from within an exception handler.
- ansible-test - When bootstrapping remote FreeBSD instances, use the OS packaged ``setuptools`` instead of installing the latest version from PyPI.
- ansible-test local change detection - use ``git merge-base <branch> HEAD`` instead of ``git merge-base --fork-point <branch>`` (https://github.com/ansible/ansible/pull/79734).
- ansible-vault - fail when the destination file location is not writable before performing encryption (https://github.com/ansible/ansible/issues/81455).
- apt - ignore fail_on_autoremove and allow_downgrade parameters when using aptitude (https://github.com/ansible/ansible/issues/77868).
- blockinfile - avoid crash with Python 3 if creating the directory fails when ``create=true`` (https://github.com/ansible/ansible/pull/81662).
- connection timeouts defined in ansible.cfg will now be properly used, the --timeout cli option was obscuring them by always being set.
- copy - print correct destination filename when using `content` and `--diff` (https://github.com/ansible/ansible/issues/79749).
- copy unit tests - Fixing "dir all perms" documentation and formatting for easier reading.
- core will now also look at the connection plugin to force 'local' interpreter for networking path compatibility as just ansible_network_os could be misleading.
- deb822_repository - use http-agent for receiving content (https://github.com/ansible/ansible/issues/80809).
- debconf - idempotency in questions with type 'password' (https://github.com/ansible/ansible/issues/47676).
- distribution facts - fix Source Mage family mapping
- dnf - fix a failure when a package from URI was specified and ``update_only`` was set (https://github.com/ansible/ansible/issues/81376).
- dnf5 - Update dnf5 module to handle API change for setting the download directory (https://github.com/ansible/ansible/issues/80887)
- dnf5 - Use ``transaction.check_gpg_signatures`` API call to check package signatures AND possibly to recover from when keys are missing.
- dnf5 - fix module and package names in the message following failed module respawn attempt
- dnf5 - use the logs API to determine transaction problems
- dpkg_selections - check if the package exists before performing the selection operation (https://github.com/ansible/ansible/issues/81404).
- encrypt - deprecate passlib_or_crypt API (https://github.com/ansible/ansible/issues/55839).
- fetch - Handle unreachable errors properly (https://github.com/ansible/ansible/issues/27816)
- file modules - Make symbolic modes with X use the computed permission, not original file (https://github.com/ansible/ansible/issues/80128)
- file modules - fix validating invalid symbolic modes.
- first found lookup has been updated to use the normalized argument parsing (pythonic) matching the documented examples.
- first found lookup, fixed an issue with subsequent items clobbering information from previous ones.
- first_found lookup now gets 'untemplated' loop entries and handles templating itself as task_executor was removing even 'templatable' entries and breaking functionality. https://github.com/ansible/ansible/issues/70772
- galaxy - check if the target for symlink exists (https://github.com/ansible/ansible/pull/81586).
- galaxy - cross check the collection type and collection source (https://github.com/ansible/ansible/issues/79463).
- gather_facts parallel option was doing the reverse of what was stated, now it does run modules in parallel when True and serially when False.
- handlers - fix ``v2_playbook_on_notify`` callback not being called when notifying handlers
- handlers - the ``listen`` keyword can affect only one handler with the same name, the last one defined as it is a case with the ``notify`` keyword (https://github.com/ansible/ansible/issues/81013)
- include_role - expose variables from parent roles to role's handlers (https://github.com/ansible/ansible/issues/80459)
- inventory_ini - handle SyntaxWarning while parsing ini file in inventory (https://github.com/ansible/ansible/issues/81457).
- iptables - remove default rule creation when creating iptables chain to be more similar to the command line utility (https://github.com/ansible/ansible/issues/80256).
- lib/ansible/utils/encrypt.py - remove unused private ``_LOCK`` (https://github.com/ansible/ansible/issues/81613)
- lookup/url.py - Fix incorrect var/env/ini entry for `force_basic_auth`
- man page build - Remove the dependency on the ``docs`` directory for building man pages.
- man page build - Sub commands of ``ansible-galaxy role`` and ``ansible-galaxy collection`` are now documented.
- module responses - Ensure that module responses are utf-8 adhereing to JSON RFC and expectations of the core code.
- module/role argument spec - validate the type for options that are None when the option is required or has a non-None default (https://github.com/ansible/ansible/issues/79656).
- modules/user.py - Add check for valid directory when creating new user homedir (allows /dev/null as skeleton) (https://github.com/ansible/ansible/issues/75063)
- paramiko_ssh, psrp, and ssh connection plugins - ensure that all values for options that should be strings are actually converted to strings (https://github.com/ansible/ansible/pull/81029).
- password_hash - fix salt format for ``crypt``  (only used if ``passlib`` is not installed) for the ``bcrypt`` algorithm.
- pep517 build backend - Copy symlinks when copying the source tree. This avoids tracebacks in various scenarios, such as when a venv is present in the source tree.
- pep517 build backend - Use the documented ``import_module`` import from ``importlib``.
- pip module - Update module to prefer use of the python ``packaging`` and ``importlib.metadata`` modules due to ``pkg_resources`` being deprecated (https://github.com/ansible/ansible/issues/80488)
- pkg_mgr.py - Fix `ansible_pkg_mgr` incorrect in TencentOS Server Linux
- pkg_mgr.py - Fix `ansible_pkg_mgr` is unknown in Kylin Linux (https://github.com/ansible/ansible/issues/81332)
- powershell modules - Only set an rc of 1 if the PowerShell pipeline signaled an error occurred AND there are error records present. Previously it would do so only if the error signal was present without checking the error count.
- replace - handle exception when bad escape character is provided in replace (https://github.com/ansible/ansible/issues/79364).
- role deduplication - don't deduplicate before a role has had a task run for that particular host (https://github.com/ansible/ansible/issues/81486).
- service module, does not permanently configure flags flags on Openbsd when enabling/disabling a service.
- service module, enable/disable is not a exclusive action in checkmode anymore.
- setup gather_timeout - Fix timeout in get_mounts_facts for linux.
- setup module (fact gathering) will now try to be smarter about different versions of facter emitting error when --puppet flag is used w/o puppet.
- syntax check - Limit ``--syntax-check`` to ``ansible-playbook`` only, as that is the only CLI affected by this argument (https://github.com/ansible/ansible/issues/80506)
- tarfile - handle data filter deprecation warning message for extract and extractall (https://github.com/ansible/ansible/issues/80832).
- template - Fix for formatting issues when a template path contains valid jinja/strftime pattern (especially line break one) and using the template path in ansible_managed (https://github.com/ansible/ansible/pull/79129)
- templating - In the template action and lookup, use local jinja2 environment overlay overrides instead of mutating the templars environment
- templating - prevent setting arbitrary attributes on Jinja2 environments via Jinja2 overrides in templates
- templating escape and single var optimization now use correct delimiters when custom ones are provided either via task or template header.
- unarchive - fix unarchiving sources that are copied to the remote node using a relative temporory directory path (https://github.com/ansible/ansible/issues/80710).
- uri - fix search for JSON type to include complex strings containing '+'
- uri/urls - Add compat function to handle the ability to parse the filename from a Content-Disposition header (https://github.com/ansible/ansible/issues/81806)
- urls.py - fixed cert_file and key_file parameters when running on Python 3.12 - https://github.com/ansible/ansible/issues/80490
- user - set expiration value correctly when unable to retrieve the current value from the system (https://github.com/ansible/ansible/issues/71916)
- validate-modules sanity test - replace semantic markup parsing and validating code with the code from `antsibull-docs-parser 0.2.0 <https://github.com/ansible-community/antsibull-docs-parser/releases/tag/0.2.0>`__ (https://github.com/ansible/ansible/pull/80406).
- vars_prompt - internally convert the ``unsafe`` value to ``bool``
- vault and unvault filters now properly take ``vault_id`` parameter.
- win_fetch - Add support for using file with wildcards in file name. (https://github.com/ansible/ansible/issues/73128)
- winrm - Better handle send input failures when communicating with hosts under load

amazon.aws
~~~~~~~~~~

- autoscaling_group - fix ValidationError when describing an autoscaling group that has more than 20 target groups attached to it by breaking the request into chunks (https://github.com/ansible-collections/amazon.aws/pull/1593).
- autoscaling_group_info - fix ValidationError when describing an autoscaling group that has more than 20 target groups attached to it by breaking the request into chunks (https://github.com/ansible-collections/amazon.aws/pull/1593).
- aws_ec2 inventory plugin - fix ``NoRegionError`` when no regions are provided and region isn't specified (https://github.com/ansible-collections/amazon.aws/issues/1551).
- backup_plan - Use existing ``scrub_none_values`` function from module_utils to remove None values from nested dicts in supplied params. Nested None values were being retained and causing an error when sent through to the boto3 client operation (https://github.com/ansible-collections/amazon.aws/pull/1611).
- backup_selection - ensures that updating an existing selection will add new ``Conditions`` if there previously were not any (https://github.com/ansible-collections/amazon.aws/pull/1701).
- backup_vault - fix error when updating tags on a backup vault by using the correct boto3 client methods for tagging and untagging backup resources (https://github.com/ansible-collections/amazon.aws/pull/1610).
- cloudwatchevent_rule - Fixes changed status to report False when no change has been made. The module had incorrectly always reported a change. (https://github.com/ansible-collections/amazon.aws/pull/1589)
- ec2_instance - fix check_mode issue when adding network interfaces (https://github.com/ansible-collections/amazon.aws/issues/1403).
- ec2_instance - retry API call if we get ``InvalidInstanceID.NotFound`` error (https://github.com/ansible-collections/amazon.aws/pull/1650).
- ec2_metadata_facts - Handle decompression when EC2 instance user-data is gzip compressed. The fetch_url method from ansible.module_utils.urls does not decompress the user-data unless the header explicitly contains ``Content-Encoding: gzip`` (https://github.com/ansible-collections/amazon.aws/pull/1575).
- ec2_vpc_nat_gateway - adding a boolean parameter called ``default_create`` to allow users to have the option to choose whether they want to display an error message or create a NAT gateway when an EIP address is not found. The module (ec2_vpc_nat_gateway) had incorrectly failed silently if EIP didn't exist (https://github.com/ansible-collections/amazon.aws/issues/1295).
- ec2_vpc_nat_gateway - fixes to nat gateway so that when the user creates a private NAT gateway, an Elastic IP address should not be allocated. The module had inncorrectly always allocate elastic IP address when creating private nat gateway (https://github.com/ansible-collections/amazon.aws/pull/1632).
- ec2_vpc_route_table_info - default filters to empty dictionary (https://github.com/ansible-collections/amazon.aws/issues/1668).
- elb_application_lb - fix missing attributes on creation of ALB. The ``create_or_update_alb()`` was including ALB-specific attributes when updating an existing ALB but not when creating a new ALB (https://github.com/ansible-collections/amazon.aws/issues/1510).
- elb_application_lb_info - ensure all API queries use the retry decorator (https://github.com/ansible-collections/amazon.aws/issues/1767).
- lambda_execute - Fixes to the stack trace output, where it does not contain spaces between each character. The module had incorrectly always outputted extra spaces between each character. (https://github.com/ansible-collections/amazon.aws/pull/1615)
- module_utils.acm - fixes list_certificates returning only RSA_2048 certificates (https://github.com/ansible-collections/amazon.aws/issues/1567).
- module_utils.backup - get_selection_details fix empty list returned when multiple backup selections exist (https://github.com/ansible-collections/amazon.aws/pull/1633).
- rds_cluster - Add ``AllocatedStorage``, ``DBClusterInstanceClass``, ``StorageType``, ``Iops``, and ``EngineMode`` to the list of parameters that can be passed when creating or modifying a Multi-AZ RDS cluster (https://github.com/ansible-collections/amazon.aws/pull/1657).
- rds_cluster - Allow to pass GlobalClusterIdentifier to rds cluster on creation (https://github.com/ansible-collections/amazon.aws/pull/1663).
- rds_instance - add support for CACertificateIdentifier to create/update rds instance (https://github.com/ansible-collections/amazon.aws/pull/1459).
- s3_bucket - fixes issue when deleting a bucket with unversioned objects (https://github.com/ansible-collections/amazon.aws/issues/1533).
- s3_object - fixed ``NoSuchTagSet`` error when S3 endpoint doesn't support tags (https://github.com/ansible-collections/amazon.aws/issues/1607).
- s3_object - fixes regression related to objects with a leading ``/`` (https://github.com/ansible-collections/amazon.aws/issues/1548).

ansible.netcommon
~~~~~~~~~~~~~~~~~

- Ensure that all connection plugin options that should be strings are actually strings (https://github.com/ansible-collections/ansible.netcommon/pull/549).
- Fix attribute types from string to str in filter plugins.
- Vendor telnetlib from cpython (https://github.com/ansible-collections/ansible.netcommon/pull/546)

ansible.utils
~~~~~~~~~~~~~

- Validate input for ipv4_hex(https://github.com/ansible-collections/ansible.utils/issues/281)

ansible.windows
~~~~~~~~~~~~~~~

- Remove some code which is no longer valid for dotnet 5+
- win_async - Set maximum data size allowed when deserializing async output - https://github.com/ansible-collections/ansible.windows/pull/520
- win_group_membership - Return accurate results when using check_mode - https://github.com/ansible-collections/ansible.windows/issues/532
- win_updates - Add retry mechanism when polling output in case file is locked by another process like an Anti Virus - https://github.com/ansible-collections/ansible.windows/issues/490
- win_updates - Add special handling for KB2267602 in case it fails - https://github.com/ansible-collections/ansible.windows/issues/530
- win_updates - Fix up endless retries when an update failed to install more than once - https://github.com/ansible-collections/ansible.windows/issues/343

arista.eos
~~~~~~~~~~

- Fix command generated for local-interface with in ntp server attribute.
- Fix command generation for source_interface attribute.
- Fix secondary ip address parsing.
- Skip compile testing for python <3.6.
- fix line attribute fact generation and placement in ACE, when ACE is not fully parsed.
- fix sanity issues w.r.t python27

check_point.mgmt
~~~~~~~~~~~~~~~~

- cp_mgmt_access_rules - split vpn param that can accept either a String or list of objects to two
- module_utils/checkpoint.py - fixed compile issue (Syntax Error) on python 2.7

chocolatey.chocolatey
~~~~~~~~~~~~~~~~~~~~~

- win-chocolatey - unable to install packages if a license is already installed and chocolatey.extension is not installed

cisco.aci
~~~~~~~~~

- Change input of prefix_suppression to type string to allow enable, disable and inherit options for aci_interface_policy_ospf
- Fixed issue with default values for ssl, proxy, timeout in aci.py and the display of host in the url when the plugin httpapi is used
- Modified  aci_rest  and  aci_config_snapshot  modules to display the correct URL output string (#487)

cisco.ios
~~~~~~~~~

- Fix invalid password length not being recognized by the error parser.
- The regex looking for errors in the terminal output was matching anything with '\S+ Error:'. Caused issues with 'show runnning-config' if this string appeared in the output. Updated the regex to require the % anchor.
- bgp_address_family - fix deleted string with int concat issue in bgp_address_family.
- ios_acls - Fix protocol_options rendering corrects processing of overridden/ replaced state.
- ios_acls - Fix standard acls rendering.
- ios_bgp_address_family - fix rendering of remote_as configuration with period.
- ios_facts - Fix facts gathering when memory statistics head is not hexadecimal. (https://github.com/ansible-collections/cisco.ios/issues/776)
- ios_facts - fix calculation of memory from bytes to megabytes; grab correct output element for free memory (https://github.com/ansible-collections/cisco.ios/issues/763)
- ios_l3_interfaces - account for secondary/primary when comparing ipv4 addresses. (https://github.com/ansible-collections/cisco.ios/issues/826)
- ios_lag_interfaces - Fix empty facts to be a list.
- ios_logging_global - fix configuration order to configure discriminator before buffer.
- ios_ospf_interface - Fix configuration rendering for ipv4 and ipv6 configurations.
- ios_ospf_interface - Fix replaced and overridden state, action to negate superfluous configuration.
- ios_prefix_lists - fix deleted state to remove exisiting prefix lists from configuration.
- ios_service - Put condition to add `private_config_encryption` in default services
- ios_snmp_server - Add default versions to version 3 users.
- ios_snmp_server - Fixes error handling for snmp user when snmp agent is not enabled
- ios_static_routes - Fix non vlan entries to have unique group identifier.
- ios_static_routes - Fix parsers to parse interface attribute correctly.
- ospfv2 - Fixed rendering of capability command with vrf_lite.
- ospfv3 - Fixed rendering of capability command with vrf_lite.
- snmp_server - update module to get snmp_server user configuration.

cisco.iosxr
~~~~~~~~~~~

- Add support to delete specific static route entry.(https://github.com/ansible-collections/cisco.iosxr/issues/375)
- Fix issue in deletion of ospf.(https://github.com/ansible-collections/cisco.iosxr/issues/425)
- Fix issue in facts gathering for Interfaces RM.(https://github.com/ansible-collections/cisco.iosxr/issues/417)
- Fix issue in lacp and lldp_global of local variable commands.
- Fixing Bundle-Ether/-POS recognition for resource modules. (https://github.com/ansible-collections/cisco.iosxr/issues/369)
- Support overridden state in bgp_global,lacp and lldp_global module.(https://github.com/ansible-collections/cisco.iosxr/issues/386)
- acls - Fix issue in ``replaced`` state of not replacing ace entries with remark action. (https://github.com/ansible-collections/cisco.iosxr/issues/332)
- l2_interfaces Fix issue in qvlan parsing.(https://github.com/ansible-collections/cisco.iosxr/issues/403)
- l3_interfaces - Fix issue in ``gather`` state of not gathering management interface. (https://github.com/ansible-collections/cisco.iosxr/issues/381)

cisco.ise
~~~~~~~~~

- Cannot get cisco.ise.active_directory_groups_by_domain_info to work.
- Cannot get cisco.ise.rest_id_store to work fixed.
- System Certificate Update does not work but always reports Object already present temporary solution.
- cisco.ise.mnt_session_active_count_info ise_reponse is null fixed.
- node_deployment tasks fail because of timeout, adding new collection param.
- system_certificate - added support for none value in the used_by param.
- system_certificate - fixed get_object_by_id response.

cisco.meraki
~~~~~~~~~~~~

- Adding condition to avoid error on exists on devices.
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
- Removing ignores.
- Resolved the issue with link negotation at meraki_ms_switchport
- Returning requires_ansible to 2.9.10
- Returning requires_ansible to >=2.14.0
- Sanity fixes.
- Updating collection docs link.
- Updating documentation, yml fixes - Documentation Broken.
- cisco.meraki.networks_devices_claim - got an unexpected keyword argument 'network_id', bug with parameter naming.
- cisco.meraki.organizations_login_security module will not update org api authentication - fixing for look at organizations_login_security.
- meraki_devices - Fix endpoints due to breaking change in Meraki API v1.33
- runtime updated requires_ansible from 2.9.10 to '>=2.14.0'.

cisco.mso
~~~~~~~~~

- Fix mso_tenant_site "site not found" issue on absent (#368)

cisco.nxos
~~~~~~~~~~

- acls - Fix parsing error when ACE has a source port range (https://github.com/ansible-collections/cisco.nxos/issues/713).
- interfaces - Re-apply existing non-default MTU when changing mode to L2 (https://github.com/ansible-collections/cisco.nxos/issues/730).
- l3_interfaces - Append tag when updating IP address with state replaced (https://github.com/ansible-collections/cisco.nxos/issues/678).
- lag_interfaces - Allow force option to be idempotent (https://github.com/ansible-collections/cisco.nxos/issues/742).
- ntp_global - Fix incorrect handling of prefer option (https://github.com/ansible-collections/cisco.nxos/issues/670).
- nxos_acls - fix parsing of ACE with named source/dest port range (https://github.com/ansible-collections/cisco.nxos/issues/763).
- nxos_banner - Add support for a custom multiline delimiter
- nxos_facts - Fix missing SVI facts (https://github.com/ansible-collections/cisco.nxos/issues/440).
- nxos_static_routes - Prevent action states to generate terminal configuration command.
- nxos_static_routes - Update the delete operation of static routes to be similar to other platforms. (https://github.com/ansible-collections/cisco.nxos/issues/666)
- snmp_server - fix host delete when authentication options are present (https://github.com/ansible-collections/cisco.nxos/issues/439).
- terminal - attempt privilege escalation only when prompt does not end with #
- vtp_version - allow VTP version 3 to be configured (https://github.com/ansible-collections/cisco.nxos/issues/704).

cloud.common
~~~~~~~~~~~~

- Ensure result is always defined in lookup plugins (https://github.com/ansible-collections/cloud.common/pull/116/files).
- Fix lookup modules failing on Ansible 2.15 (https://github.com/ansible-collections/cloud.common/pull/130).

cloudscale_ch.cloud
~~~~~~~~~~~~~~~~~~~

- Add missing modules to the "cloudscale_ch.cloud.cloudscale" action group.
- Remove outdated Ansible version requirement from the README.

community.aws
~~~~~~~~~~~~~

- Remove ``apigateway`` and ``apigateway_deployment`` from meta/runtime.yml (https://github.com/ansible-collections/community.aws/pull/1905).
- batch_compute_environment - fixed incorrect handling of Gov Cloud ARNs in ``compute_environment_name`` parameter (https://github.com/ansible-collections/community.aws/issues/1846).
- cloudfront_distribution - The origins  recognises the s3 domains with region part now (https://github.com/ansible-collections/community.aws/issues/1819).
- cloudfront_distribution - no longer crashes when waiting for completion of creation (https://github.com/ansible-collections/community.aws/issues/255).
- cloudfront_distribution - now honours the ``enabled`` setting (https://github.com/ansible-collections/community.aws/issues/1823).
- dynamodb_table - secondary indexes are now created (https://github.com/ansible-collections/community.aws/issues/1825).
- ec2_launch_template - fixed incorrect handling of Gov Cloud ARNs in ``compute_environment_name`` parameter (https://github.com/ansible-collections/community.aws/issues/1846).
- elasticache_info - remove hard coded use of ``aws`` partition (https://github.com/ansible-collections/community.aws/issues/1846).
- iam_role - fixed incorrect rejection of Gov Cloud ARNs in ``boundary`` parameter (https://github.com/ansible-collections/community.aws/issues/1846).
- mq_broker - ensure broker is created with ``tags`` when passed (https://github.com/ansible-collections/community.aws/issues/1832).
- msk_cluster - remove hard coded use of ``aws`` partition (https://github.com/ansible-collections/community.aws/issues/1846).
- opensearch - Don't try to read a non existing key from the domain config (https://github.com/ansible-collections/community.aws/pull/1910).
- redshift - fixed hard coded use of ``aws`` partition (https://github.com/ansible-collections/community.aws/issues/1846).

community.ciscosmb
~~~~~~~~~~~~~~~~~~

- added Cisco device config guide to address issue
- added extra "\n" to sending commands to address issue

community.crypto
~~~~~~~~~~~~~~~~

- Fix PEM detection/identification to also accept random other lines before the line starting with ``-----BEGIN`` (https://github.com/ansible-collections/community.crypto/issues/627, https://github.com/ansible-collections/community.crypto/pull/628).
- acme_* modules - correctly handle error documents without ``type`` (https://github.com/ansible-collections/community.crypto/issues/651, https://github.com/ansible-collections/community.crypto/pull/652).
- openssh_cert, openssh_keypair - the modules ignored return codes of ``ssh`` and ``ssh-keygen`` in some cases (https://github.com/ansible-collections/community.crypto/issues/645, https://github.com/ansible-collections/community.crypto/pull/646).
- openssh_keypair - fix comment updating for OpenSSH before 6.5 (https://github.com/ansible-collections/community.crypto/pull/646).
- openssl_pkcs12 - modify autodetect to not detect pyOpenSSL >= 23.3.0, which removed PKCS#12 support (https://github.com/ansible-collections/community.crypto/pull/666).

community.digitalocean
~~~~~~~~~~~~~~~~~~~~~~

- digital_ocean_domain - fix ``all_domains`` by using ``get_paginated_data`` to retrieve all of the domains in the account from the paginated domains api endpoint (https://github.com/ansible-collections/community.digitalocean/pull/307).

community.dns
~~~~~~~~~~~~~

- HTTP module utils - make compatible with ansible-core 2.17 (https://github.com/ansible-collections/community.dns/pull/165).
- Update Public Suffix List.
- wait_for_txt, resolver module utils - improve error handling (https://github.com/ansible-collections/community.dns/pull/158).

community.docker
~~~~~~~~~~~~~~~~

- docker_swarm - make init and join operations work again with Docker SDK for Python before 4.0.0 (https://github.com/ansible-collections/community.docker/issues/695, https://github.com/ansible-collections/community.docker/pull/696).
- docker_swarm_info - if ``service=true`` is used, do not crash when a service without an endpoint spec is encountered (https://github.com/ansible-collections/community.docker/issues/636, https://github.com/ansible-collections/community.docker/pull/637).
- docker_volume - fix crash caused by accessing an empty dictionary. The ``has_different_config()`` was raising an ``AttributeError`` because the ``self.existing_volume["Labels"]`` dictionary was ``None`` (https://github.com/ansible-collections/community.docker/pull/702).
- vendored Docker SDK for Python code - cherry-pick changes from the Docker SDK for Python code to align code. These changes should not affect the parts used by the collection's code (https://github.com/ansible-collections/community.docker/pull/694).

community.general
~~~~~~~~~~~~~~~~~

- CmdRunner module utils - does not attempt to resolve path if executable is a relative or absolute path (https://github.com/ansible-collections/community.general/pull/7200).
- MH DependencyMixin module utils - deprecation notice was popping up for modules not using dependencies (https://github.com/ansible-collections/community.general/pull/6644, https://github.com/ansible-collections/community.general/issues/6639).
- bitwarden lookup plugin - the plugin made assumptions about the structure of a Bitwarden JSON object which may have been broken by an update in the Bitwarden API. Remove assumptions, and allow queries for general fields such as ``notes`` (https://github.com/ansible-collections/community.general/pull/7061).
- cmd_runner module utils - when a parameter in ``argument_spec`` has no type, meaning it is implicitly a ``str``, ``CmdRunner`` would fail trying to find the ``type`` key in that dictionary (https://github.com/ansible-collections/community.general/pull/6968).
- cobbler inventory plugin - fix calculation of cobbler_ipv4/6_address (https://github.com/ansible-collections/community.general/pull/6925).
- composer - fix impossible to run ``working_dir`` dependent commands. The module was throwing an error when trying to run a ``working_dir`` dependent command, because it tried to get the command help without passing the ``working_dir`` (https://github.com/ansible-collections/community.general/issues/3787).
- csv module utils - detects and remove unicode BOM markers from incoming CSV content (https://github.com/ansible-collections/community.general/pull/6662).
- datadog_downtime - presence of ``rrule`` param lead to the Datadog API returning Bad Request due to a missing recurrence type (https://github.com/ansible-collections/community.general/pull/6811).
- ejabberd_user - module was failing to detect whether user was already created and/or password was changed (https://github.com/ansible-collections/community.general/pull/7033).
- ejabberd_user - provide meaningful error message when the ``ejabberdctl`` command is not found (https://github.com/ansible-collections/community.general/pull/7028, https://github.com/ansible-collections/community.general/issues/6949).
- github_deploy_key - fix pagination behaviour causing a crash when only a single page of deploy keys exist (https://github.com/ansible-collections/community.general/pull/7375).
- gitlab_group - the module passed parameters to the API call even when not set. The module is now filtering out ``None`` values to remediate this (https://github.com/ansible-collections/community.general/pull/6712).
- gitlab_group_members - fix gitlab constants call in ``gitlab_group_members`` module (https://github.com/ansible-collections/community.general/issues/7467).
- gitlab_group_variable - deleted all variables when used with ``purge=true`` due to missing ``raw`` property in KNOWN attributes (https://github.com/ansible-collections/community.general/issues/7250).
- gitlab_project_members - fix gitlab constants call in ``gitlab_project_members`` module (https://github.com/ansible-collections/community.general/issues/7467).
- gitlab_project_variable - deleted all variables when used with ``purge=true`` due to missing ``raw`` property in KNOWN attributes (https://github.com/ansible-collections/community.general/issues/7250).
- gitlab_protected_branches - fix gitlab constants call in ``gitlab_protected_branches`` module (https://github.com/ansible-collections/community.general/issues/7467).
- gitlab_user - fix gitlab constants call in ``gitlab_user`` module (https://github.com/ansible-collections/community.general/issues/7467).
- icinga2_host - fix a key error when updating an existing host (https://github.com/ansible-collections/community.general/pull/6748).
- ini_file - add the ``follow`` paramter to follow the symlinks instead of replacing them (https://github.com/ansible-collections/community.general/pull/6546).
- ini_file - fix a bug where the inactive options were not used when possible (https://github.com/ansible-collections/community.general/pull/6575).
- ipa_dnszone - fix 'idnsallowsyncptr' key error for reverse zone (https://github.com/ansible-collections/community.general/pull/6906, https://github.com/ansible-collections/community.general/issues/6905).
- kernel_blacklist - simplified the mechanism to update the file, fixing the error (https://github.com/ansible-collections/community.general/pull/7382, https://github.com/ansible-collections/community.general/issues/7362).
- keycloak module util - fix missing ``http_agent``, ``timeout``, and ``validate_certs`` ``open_url()`` parameters (https://github.com/ansible-collections/community.general/pull/7067).
- keycloak module utils - fix ``is_struct_included`` handling of lists of lists/dictionaries (https://github.com/ansible-collections/community.general/pull/6688).
- keycloak module utils - the function ``get_user_by_username`` now return the user representation or ``None`` as stated in the documentation (https://github.com/ansible-collections/community.general/pull/6758).
- keycloak_authentication - fix Keycloak authentication flow (step or sub-flow) indexing during update, if not specified by the user (https://github.com/ansible-collections/community.general/pull/6734).
- keycloak_client inventory plugin - fix missing client secret (https://github.com/ansible-collections/community.general/pull/6931).
- ldap_search - fix string normalization and the ``base64_attributes`` option on Python 3 (https://github.com/ansible-collections/community.general/issues/5704, https://github.com/ansible-collections/community.general/pull/7264).
- locale_gen - now works for locales without the underscore character such as ``C.UTF-8`` (https://github.com/ansible-collections/community.general/pull/6774, https://github.com/ansible-collections/community.general/issues/5142, https://github.com/ansible-collections/community.general/issues/4305).
- lvol - add support for percentage of origin size specification when creating snapshot volumes (https://github.com/ansible-collections/community.general/issues/1630, https://github.com/ansible-collections/community.general/pull/7053).
- lxc connection plugin - now handles ``remote_addr`` defaulting to ``inventory_hostname`` correctly (https://github.com/ansible-collections/community.general/pull/7104).
- lxc connection plugin - properly evaluate options (https://github.com/ansible-collections/community.general/pull/7369).
- machinectl become plugin - mark plugin as ``require_tty`` to automatically disable pipelining, with which this plugin is not compatible (https://github.com/ansible-collections/community.general/issues/6932, https://github.com/ansible-collections/community.general/pull/6935).
- mail - skip headers containing equals characters due to missing ``maxsplit`` on header key/value parsing (https://github.com/ansible-collections/community.general/pull/7303).
- memset module utils - make compatible with ansible-core 2.17 (https://github.com/ansible-collections/community.general/pull/7379).
- nmap inventory plugin - fix ``get_option`` calls (https://github.com/ansible-collections/community.general/pull/7323).
- nmap inventory plugin - now uses ``get_option`` in all cases to get its configuration information (https://github.com/ansible-collections/community.general/pull/7119).
- nmcli - fix bond option ``xmit_hash_policy`` (https://github.com/ansible-collections/community.general/pull/6527).
- nmcli - fix support for empty list (in compare and scrape) (https://github.com/ansible-collections/community.general/pull/6769).
- nsupdate - fix a possible ``list index out of range`` exception (https://github.com/ansible-collections/community.general/issues/836).
- ocapi_utils, oci_utils, redfish_utils module utils - replace ``type()`` calls with ``isinstance()`` calls (https://github.com/ansible-collections/community.general/pull/7501).
- oci_utils module util - fix inappropriate logical comparison expressions and makes them simpler. The previous checks had logical short circuits (https://github.com/ansible-collections/community.general/pull/7125).
- oci_utils module utils - avoid direct type comparisons (https://github.com/ansible-collections/community.general/pull/7085).
- onepassword - fix KeyError exception when trying to access value of a field that is not filled out in OnePassword item (https://github.com/ansible-collections/community.general/pull/7241).
- openbsd_pkg - the pkg_info(1) behavior has changed in OpenBSD >7.3. The error message ``Can't find`` should not lead to an error case (https://github.com/ansible-collections/community.general/pull/6785).
- pacman - module recognizes the output of ``yay`` running as ``root`` (https://github.com/ansible-collections/community.general/pull/6713).
- pipx module utils - change the CLI argument formatter for the ``pip_args`` parameter (https://github.com/ansible-collections/community.general/issues/7497, https://github.com/ansible-collections/community.general/pull/7506).
- portage - fix ``changed_use`` and ``newuse`` not triggering rebuilds (https://github.com/ansible-collections/community.general/issues/6008, https://github.com/ansible-collections/community.general/pull/6548).
- pritunl module utils - fix incorrect URL parameter for orgnization add method (https://github.com/ansible-collections/community.general/pull/7161).
- proxmox - fix error when a configuration had no ``template`` field (https://github.com/ansible-collections/community.general/pull/6838, https://github.com/ansible-collections/community.general/issues/5372).
- proxmox module utils - add logic to detect whether an old Promoxer complains about the ``token_name`` and ``token_value`` parameters and provide a better error message when that happens (https://github.com/ansible-collections/community.general/pull/6839, https://github.com/ansible-collections/community.general/issues/5371).
- proxmox module utils - fix proxmoxer library version check (https://github.com/ansible-collections/community.general/issues/6974, https://github.com/ansible-collections/community.general/issues/6975, https://github.com/ansible-collections/community.general/pull/6980).
- proxmox_disk - fix unable to create ``cdrom`` media due to ``size`` always being appended (https://github.com/ansible-collections/community.general/pull/6770).
- proxmox_kvm - ``absent`` state with ``force`` specified failed to stop the VM due to the ``timeout`` value not being passed to ``stop_vm`` (https://github.com/ansible-collections/community.general/pull/6827).
- proxmox_kvm - ``restarted`` state did not actually restart a VM in some VM configurations. The state now uses the Proxmox reboot endpoint instead of calling the ``stop_vm`` and ``start_vm`` functions (https://github.com/ansible-collections/community.general/pull/6773).
- proxmox_kvm - allow creation of VM with existing name but new vmid (https://github.com/ansible-collections/community.general/issues/6155, https://github.com/ansible-collections/community.general/pull/6709).
- proxmox_kvm - when ``name`` option is provided without ``vmid`` and VM with that name already exists then no new VM will be created (https://github.com/ansible-collections/community.general/issues/6911, https://github.com/ansible-collections/community.general/pull/6981).
- proxmox_pool_member - absent state for type VM did not delete VMs from the pools (https://github.com/ansible-collections/community.general/pull/7464).
- proxmox_tasks_info - remove ``api_user`` + ``api_password`` constraint from ``required_together`` as it causes to require ``api_password`` even when API token param is used (https://github.com/ansible-collections/community.general/issues/6201).
- proxmox_template - require ``requests_toolbelt`` module to fix issue with uploading large templates (https://github.com/ansible-collections/community.general/issues/5579, https://github.com/ansible-collections/community.general/pull/6757).
- proxmox_user_info - avoid direct type comparisons (https://github.com/ansible-collections/community.general/pull/7085).
- redfish_command - fix usage of message parsing in ``SimpleUpdate`` and ``MultipartHTTPPushUpdate`` commands to treat the lack of a ``MessageId`` as no message (https://github.com/ansible-collections/community.general/issues/7465, https://github.com/ansible-collections/community.general/pull/7471).
- redfish_info - fix ``ListUsers`` to not show empty account slots (https://github.com/ansible-collections/community.general/issues/6771, https://github.com/ansible-collections/community.general/pull/6772).
- redhat_subscription - use the right D-Bus options for the consumer type when
  registering a RHEL system older than 9 or a RHEL 9 system older than 9.2
  and using ``consumer_type``
  (https://github.com/ansible-collections/community.general/pull/7378).
- refish_utils module utils - changing variable names to avoid issues occuring when fetching Volumes data (https://github.com/ansible-collections/community.general/pull/6883).
- rhsm_repository - when using the ``purge`` option, the ``repositories``
  dictionary element in the returned JSON is now properly updated according
  to the pruning operation
  (https://github.com/ansible-collections/community.general/pull/6676).
- rundeck - fix ``TypeError`` on 404 API response (https://github.com/ansible-collections/community.general/pull/6983).
- selective callback plugin - fix length of task name lines in output always being 3 characters longer than desired (https://github.com/ansible-collections/community.general/pull/7374).
- snap - an exception was being raised when snap list was empty (https://github.com/ansible-collections/community.general/pull/7124, https://github.com/ansible-collections/community.general/issues/7120).
- snap - assume default track ``latest`` in parameter ``channel`` when not specified (https://github.com/ansible-collections/community.general/pull/6835, https://github.com/ansible-collections/community.general/issues/6821).
- snap - change the change detection mechanism from "parsing installation" to "comparing end state with initial state" (https://github.com/ansible-collections/community.general/pull/7340, https://github.com/ansible-collections/community.general/issues/7265).
- snap - fix crash when multiple snaps are specified and one has ``---`` in its description (https://github.com/ansible-collections/community.general/pull/7046).
- snap - fix the processing of the commands' output, stripping spaces and newlines from it (https://github.com/ansible-collections/community.general/pull/6826, https://github.com/ansible-collections/community.general/issues/6803).
- sorcery - fix interruption of the multi-stage process (https://github.com/ansible-collections/community.general/pull/7012).
- sorcery - fix queue generation before the whole system rebuild (https://github.com/ansible-collections/community.general/pull/7012).
- sorcery - latest state no longer triggers update_cache (https://github.com/ansible-collections/community.general/pull/7012).
- terraform - prevents ``-backend-config`` option double encapsulating with ``shlex_quote`` function. (https://github.com/ansible-collections/community.general/pull/7301).
- tss lookup plugin - fix multiple issues when using ``fetch_attachments=true`` (https://github.com/ansible-collections/community.general/pull/6720).
- zypper - added handling of zypper exitcode 102. Changed state is set correctly now and rc 102 is still preserved to be evaluated by the playbook (https://github.com/ansible-collections/community.general/pull/6534).

community.grafana
~~~~~~~~~~~~~~~~~

- Fix error with datasources configured without basicAuth
- grafana_folder, fix an issue during delete (starting Grafana 9.3)

community.hashi_vault
~~~~~~~~~~~~~~~~~~~~~

- vault_write - the ``vault_write`` lookup and module were not able to write data containing keys named ``path`` or ``wrap_ttl`` due to a bug in the ``hvac`` library. These plugins have now been updated to take advantage of fixes in ``hvac>=1.2`` to address this (https://github.com/ansible-collections/community.hashi_vault/issues/389).

community.hrobot
~~~~~~~~~~~~~~~~

- Show more information (if available) from error messages (https://github.com/ansible-collections/community.hrobot/pull/89).

community.libvirt
~~~~~~~~~~~~~~~~~

- libvirt_qemu - connection plugin threw a warning about an improperly configured remote target. Fix adds `inventory_hostname` to `options.remote_addr.vars` (https://github.com/ansible-collections/community.libvirt/pull/147).
- libvirt_qemu - fix encoding errors on Windows guests for non-ASCII return values (https://github.com/ansible-collections/community.libvirt/pull/157)
- virt - fix virt module to undefine a domain with nvram, managed_save, snapshot_metadata or checkpoints_metadata (https://github.com/ansible-collections/community.libvirt/issues/40).
- virt_pool - replace discouraged function ``listAllVolumes`` with ``listAllVolumes`` to fix potential race conditions (https://github.com/ansible-collections/community.libvirt/pull/135).
- virt_pool - replace discouraged functions ``listStoragePools`` and ``listDefinedStoragePools`` with ``listAllStoragePools`` to fix potential race conditions (https://github.com/ansible-collections/community.libvirt/pull/134).

community.mysql
~~~~~~~~~~~~~~~

- mysql module utils - use the connection arguments ``db`` instead of ``database`` and ``passwd`` instead of ``password`` when running with MySQLdb < 2.0.0 (https://github.com/ansible-collections/community.mysql/pull/553).

community.network
~~~~~~~~~~~~~~~~~

- cnos_l3_interface - fix import errors (https://github.com/ansible-collections/community.network/pull/531).
- exos_config - missing whitespace in command with ``defaults: True``. It happened because the command is ``show configurationdetail`` instead of ``show configuration detail`` (https://github.com/ansible-collections/community.network/pull/516).
- exos_facts - returns timeout error when we use connection type ``network_cli``. It happened because we send command without ``no-refresh`` and script ``cli2json.py`` stuck in loop while reading console output (https://github.com/ansible-collections/community.network/pull/517).
- icx_l3_interface - fix import errors (https://github.com/ansible-collections/community.network/pull/531).
- slxos_l3_interface - fix import errors (https://github.com/ansible-collections/community.network/pull/531).

community.postgresql
~~~~~~~~~~~~~~~~~~~~

- postgresql_db - when the task is completed successfully, close the database connection (https://github.com/ansible-collections/community.postgresql/issues/465).
- postgresql_ext - fixed queries return value name in documentation (https://github.com/ansible-collections/community.postgresql/pull/545).
- postgresql_info - fix SQL syntax issue (https://github.com/ansible-collections/community.postgresql/issues/570).
- postgresql_info - when the task is completed successfully, close the database connection (https://github.com/ansible-collections/community.postgresql/issues/465).
- postgresql_ping - when the task is completed successfully, close the database connection (https://github.com/ansible-collections/community.postgresql/issues/465).
- postgresql_privs - fixed error message and documentation (https://github.com/ansible-collections/community.postgresql/pull/510).
- postgresql_privs - when the task is completed successfully, close the database connection (https://github.com/ansible-collections/community.postgresql/issues/465).
- postgresql_set - fixed GUC_LIST_QUOTE parameters (https://github.com/ansible-collections/community.postgresql/pull/521).
- postgresql_set - fixed error message in param_set function (https://github.com/ansible-collections/community.postgresql/pull/505).

community.routeros
~~~~~~~~~~~~~~~~~~

- api_info, api_modify - in the ``snmp`` path, ensure that ``engine-id-suffix`` is only available on RouterOS 7.10+, and that ``engine-id`` is read-only on RouterOS 7.10+ (https://github.com/ansible-collections/community.routeros/issues/208, https://github.com/ansible-collections/community.routeros/pull/218).
- api_modify, api_info - add missing parameter ``engine-id-suffix`` for the ``snmp`` path (https://github.com/ansible-collections/community.routeros/issues/189, https://github.com/ansible-collections/community.routeros/pull/190).
- api_modify, api_info - add missing parameter ``tls`` for the ``tool e-mail`` path (https://github.com/ansible-collections/community.routeros/issues/179, https://github.com/ansible-collections/community.routeros/pull/180).
- facts - do not crash in CLI output preprocessing in unexpected situations during line unwrapping (https://github.com/ansible-collections/community.routeros/issues/170, https://github.com/ansible-collections/community.routeros/pull/177).

community.sops
~~~~~~~~~~~~~~

- Avoid pre-releases when picking the latest version when using the GitHub API method (https://github.com/ansible-collections/community.sops/pull/159).
- Fix RPM URL for the 3.8.0 release (https://github.com/ansible-collections/community.sops/pull/161).
- Fix changed DEB and RPM URLs for 3.8.0 and its prerelease(s) (https://github.com/ansible-collections/community.sops/pull/159).
- install role - fix ``sops_github_latest_detection=latest-release``, which broke due to sops moving to another GitHub organization (https://github.com/ansible-collections/community.sops/pull/151).
- install role - make sure that the ``pkg_mgr`` fact is definitely available when installing on ``localhost``. This can improve error messages in some cases (https://github.com/ansible-collections/community.sops/issues/145, https://github.com/ansible-collections/community.sops/pull/146).
- sops_encrypt - ensure that output-type is set to ``yaml`` when the file extension ``.yml`` is used. Now both ``.yaml`` and ``.yml`` files use the SOPS ``--output-type=yaml`` formatting (https://github.com/ansible-collections/community.sops/issues/164).

community.vmware
~~~~~~~~~~~~~~~~

- Add missing modules to runtime.yml (https://github.com/ansible-collections/community.vmware/pull/1764).
- fix problem when module try apply non global or non VM type custom attribute to VM object (https://github.com/ansible-collections/community.vmware/issues/1772)
- vmware_deploy_ovf - Fix an issue with networks that are available on more than one cluster (https://github.com/ansible-collections/community.vmware/issues/1590).
- vmware_deploy_ovf - fix error in finding networks part of code (https://github.com/ansible-collections/community.vmware/issues/1853).
- vmware_deploy_ovf: fix error in finding networks part of code https://github.com/ansible-collections/community.vmware/issues/1853
- vmware_guest_custom_attributes - fix problem when module try apply non global or non VM type custom attribute to VM object (https://github.com/ansible-collections/community.vmware/issues/1772).
- vmware_guest_disk - Fix idempotency for `absent` disks (https://github.com/ansible-collections/community.vmware/issues/1765).
- vmware_vm_info - Add missing show_folder parameter (https://github.com/ansible-collections/community.vmware/issues/1709).

community.windows
~~~~~~~~~~~~~~~~~

- win_psmodule - fix requireLicenseAcceptance test so that it is no longer always true

community.zabbix
~~~~~~~~~~~~~~~~

- Proxy and Agent Roles - Added `zabbix_api_use_ssl` variable to allow secure API connections
- Web Role - Added defaults and documentation for `zabbix_apache_custom_includes`
- agent - Handled undefined variable error for Windows default versions
- agent role - Added missing become statement to allow run to role as nonroot
- all roles - Added option to selectively disable a repo on Redhat installs
- zabbix_host module - fix updating hosts that were discovered via LLD
- zabbix_proxy role - failed at version validation. Fix adds cast of zabbix_proxy_version to float, similarly to the other roles.
- zabbix_proxy role - undefined vars at updating proxy definition. Fix adds null defaults for zabbix_proxy_tlsaccept and zabbix_proxy_tlsconnect.
- zabbix_web role - removed 'ssl on;' nginx configuration, which is no longer supported since nginx version 1.25.1.

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
- Fix common file for Python 2.7
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
- podman_network - Do not force network removal by default
- podman_network - Fix network DNS enable idempotency issue
- podman_pod - Fix idempotency when running inside Podman container
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

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- Job tracking is fixed for iDRAC SCP import (https://github.com/dell/dellemc-openmanage-ansible-modules/pull/504).
- OMSDK is handled for import error ``SNIMissingWarning`` that is undefined (https://github.com/dell/omsdk/issues/33).
- The Chassis Power PIN value must be of six numerical digits input from the module. (https://github.com/dell/dellemc-openmanage-ansible-modules/issues/492).
- Update document on how to use with ansible. (https://github.com/dell/dellemc-openmanage-ansible-modules/issues/393).
- idrac_attributes module can now support modification of IPv6 attributes on iDRAC 8. (https://github.com/dell/dellemc-openmanage-ansible-modules/issues/488).
- idrac_firmware - Issue(276335) - This module fails on the Python 3.11.x version with NFS share. Use a different Python version or Share type.
- idrac_server_config_profile - The import for Server Configuration Profile (SCP) operation fails to handle the absence of a file and incorrectly reports success instead of the expected failure. (https://github.com/dell/dellemc-openmanage-ansible-modules/issues/544).
- ome_device_info is limited to 50 responses with a query filter. (https://github.com/dell/dellemc-openmanage-ansible-modules/issues/499).
- ome_device_quick_deploy - If the blade is not present, then the module can assign a static IP to the slot (https://github.com/dell/dellemc-openmanage-ansible-modules/issues/532).

f5networks.f5_modules
~~~~~~~~~~~~~~~~~~~~~

- bigip_device_certificate - error-handling for connection error while running exec command function to fetch certificate details
- bigip_pool - Resolved a bug in the code to allow the module to remove monitors from the pool
- bigip_provision_async - created module to address scenarios where infinite loops or timeouts happen
- bigip_ssl_key_cert - fixed flaw in code to make module work with same key and cert name when true_names set to true
- bigip_virtual_server - fixed an idempotency bug where the module send asm policy profile for update even when not specified explicitly by the user

fortinet.fortimanager
~~~~~~~~~~~~~~~~~~~~~

- Add 'access_token' in 'fmgr_generic'.
- Add param 'platform' in 'fmgr_wtpprofile' and param 'interface' in 'fmgr_fsp_vlan'.
- Corrected description of parameters in documentation.
- Fix a bug that collection may update the resource when it does not need to.
- Fix a bug where the user may not be able to use workspace_locking_adom if the workspace mode is per-adom.
- Fix some modules missing revision (used for version warning).
- Fixed Many sanity test warnings and errors.
- Fixed a bug where users might not be able to login.
- Fixed the bug that would report an error when providing access_token and username/password at the same time.
- Fixed version_added in the document. The value of this parameter is the version each module first supported in the FortiManager Ansible Collection.
- Improve document.
- Improve fmgr_fact. 'changed' will not be true anymore if you get the result.
- Improve login logic in httpapi plugin.
- Improve sanity tests.
- When the JSON data sent by FortiManager is not in the right format, the collection can still execute correctly.

fortinet.fortios
~~~~~~~~~~~~~~~~

- Fix the error of pure number password.
- Fix the hyperlink issue for the supported FOS versions in USER's GUIDE.
- Fix the issue of one session remaining open after the task is finished.
- Fix the issue while comparing the changes in before and after data in check_mode;
- Fix the issues that some parameters are not in a specific fos vm versions.
- Fix the request error when updating global object;
- Fix the sanity test error;
- Fix the wrong credential error when using username/password in fos verion 6;
- To optimize the json_generic module and reduce the time spent while sending GET requests.

google.cloud
~~~~~~~~~~~~

- Use default service account if `service_account_email` is unset.

hetzner.hcloud
~~~~~~~~~~~~~~

- `*_info` - Consistently fail on invalid ID in `*_info` modules.
- hcloud_firewall - The port argument is required when the firewall rule protocol is `udp` or `tcp`.
- hcloud_image_info Fix facts modules deprecated result key
- hcloud_load_balancer_service - In the returned data, the invalid `health_check.http.certificates` field was renamed to `health_check.http.status_codes`.
- hcloud_location_info Fix facts modules deprecation warnings
- hcloud_server - Fix string formatting error on deprecated server type warning
- hcloud_server - TypeError when trying to use deprecated image with allow_deprecated_image
- hcloud_server_type_info Fix facts modules deprecated result dict
- hcloud_server_type_info Fix facts modules deprecation warnings

junipernetworks.junos
~~~~~~~~~~~~~~~~~~~~~

- fix `no_advertise_adjacency_segment` config implementation.
- fix `no_eligible_backup` config implementation.
- fix `no_eligible_remote_backup` config implementation.
- fix `no_interface_state_traps` config implementation.
- fix `no_neighbor_down_notification` config implementation.
- fix `node_link_protection` implementation.
- fix md5 authentication which allows list of keys to be configured.

microsoft.ad
~~~~~~~~~~~~

- Added the missing dependency ``dpapi-ng`` to Ansible Execution Environments requirements file for LAPS decryption support
- Ensure renaming and moving an object will be done with the ``domain_server`` and ``domain_username`` credentials specified - https://github.com/ansible-collections/microsoft.ad/issues/54
- Fix up ``protect_from_deletion`` when creating new AD objects - https://github.com/ansible-collections/microsoft.ad/issues/47
- Fix up date_time attribute comparisons to be idempotent - https://github.com/ansible-collections/microsoft.ad/issues/57
- group - Fix idempotency check when ``scope: domainlocal`` is set - https://github.com/ansible-collections/microsoft.ad/issues/31
- microsoft.ad.group - ensure the ``scope`` and ``category`` values are checked as case insensitive to avoid changes when not needed - https://github.com/ansible-collections/microsoft.ad/issues/31
- microsoft.ad.user - Ensure the ``spn`` diff after key is ``spn`` and not ``kerberos_encryption_types``
- microsoft.ad.user - treat an expired account as a password that needs to be changed

netapp.ontap
~~~~~~~~~~~~

- na_ontap_dns - fix DNS not working with Cluster mode.
- na_ontap_dns - fix keyerror for uuid when DNS is set to vserver in REST.
- na_ontap_ems_filter - fix delete operation not idempotent for filter.
- na_ontap_ems_filter - fix modify operation to add rule in existing filter.
- na_ontap_login_messages - fix ``banner`` and ``motd_message`` not idempotent when trailing '\n' is present.
- na_ontap_login_messages - fix idempotency issue in Cluster scope in REST.
- na_ontap_login_messages - fix idempotent issue on ``show_cluster_motd`` option when try to set banner or motd_message for the first time in REST.
- na_ontap_nfs - fix `default_user` under `windows` not getting modified if not set previously in REST.
- na_ontap_svm - fix REST version warning for `ndmp` under `services`.
- na_ontap_volume - fix invalid field error with 'space.snapshot.autodelete' in REST.

netbox.netbox
~~~~~~~~~~~~~

- Fix schema caching [#1053](https://github.com/netbox-community/ansible_modules/pull/1053)
- netbox_ device - Adjust device_role to role for NetBox 3.6 [#1066](https://github.com/netbox-community/ansible_modules/pull/1066)

ovirt.ovirt
~~~~~~~~~~~

- HE - add back dependency on python3-jmespath (https://github.com/oVirt/ovirt-ansible-collection/pull/701)
- HE - drop remaining filters using netaddr (https://github.com/oVirt/ovirt-ansible-collection/pull/702)
- HE - drop usage of ipaddr filters and remove dependency on python-netaddr (https://github.com/oVirt/ovirt-ansible-collection/pull/696)
- HE - fix ipv4 and ipv6 check after dropping netaddr (https://github.com/oVirt/ovirt-ansible-collection/pull/704)
- hosted_engine_setup -  Update README (https://github.com/oVirt/ovirt-ansible-collection/pull/706)
- ovirt_disk -  Fix issue in detaching the direct LUN (https://github.com/oVirt/ovirt-ansible-collection/pull/700)
- ovirt_quota - Convert storage size to integer (https://github.com/oVirt/ovirt-ansible-collection/pull/712)
- ovirt_role - Fix administrative option when set to False (https://github.com/oVirt/ovirt-ansible-collection/pull/723).

purestorage.flasharray
~~~~~~~~~~~~~~~~~~~~~~

- purefa_certs - Resolved CSR issue and require export_file for state sign.
- purefa_ds - Fixes error when enabling directory services while a bind_user is set on the array and a bind_password is not.
- purefa_ds - Fixes issue with creating a new ds configuration while setting force_bind_password as "false".
- purefa_host - Fix incorrect calling of "module.params".
- purefa_info - Added missing alerts subset name
- purefa_info - Fix serial number generation issue for vVols
- purefa_info - Fixed attribute errors after EUC changes
- purefa_info - Fixed issue with replica links in unknown state
- purefa_info - Fixed missing arguments for google_offload and pods
- purefa_info - Fixed parameter error when enabled and disabled timers are different values on purity 6.4.10+ arrays.
- purefa_info - Fixed py39 specific bug with multiple DNS entries
- purefa_network - Allow `gateway` to be set as `0.0.0.0` to remove an existing gateway address
- purefa_network - Fixed IPv6 support issues
- purefa_network - Fixed idempotency issue when gateway not modified
- purefa_pgsched - Fixed bug with an unnecessary substitution
- purefa_pgsched - Resolved idempotency issue with snap and replication enabled flags
- purefa_pgsnap - Enabled to eradicate destroyed snapshots.
- purefa_pgsnap - Ensure that `now` and `remote` are mutually exclusive.
- purefa_pgsnap - Fixed issue with eradicating deleted pgsnapshot
- purefa_pgsnap - Update the accepted suffixes to include also numbers only. Fixed the logic to retrieve the latest completed snapshot
- purefa_policy - Set user_mapping parameter default to True
- purefa_snap - Fixed incorrect calling logic causing failure on remote snapshot creation
- purefa_snap - Fixed issue with remote snapshot retrieve. Mainly a workaround to an issue with Purity REST 1.x when remote snapshots are searched.
- purefa_subnet - Fixed IPv4 gateway removal issue.
- purefa_subnet - Fixed IPv6 support issues.
- purefa_volume - Fixed bug with NULL suffix for multiple volume creation.

purestorage.flashblade
~~~~~~~~~~~~~~~~~~~~~~

- purefb_bucket - Fixed bucket type mode name typo
- purefb_fs - Fixed issue with incorrect promotion state setting
- purefb_info - Fixed missing atributes for SMB client policy rules
- purefb_userpolicy - Fixed `show` state for all user policies

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
- content_view_publish role - correctly pass ``version`` not ``description`` to the module (https://bugzilla.redhat.com/show_bug.cgi?id=2234444)
- convert2rhel role - Sync repos before CV publish (https://bugzilla.redhat.com/show_bug.cgi?id=2216907)
- repositories role - don't log repository information when creating products (https://bugzilla.redhat.com/show_bug.cgi?id=2183357)
- repository - don't fail when removing a content credential from a repository (https://bugzilla.redhat.com/show_bug.cgi?id=2224122)
- smart_class_parameter - correctly allow setting ``override`` to ``false`` (https://github.com/theforeman/foreman-ansible-modules/issues/1644)

vultr.cloud
~~~~~~~~~~~

- firewall_rule - Fixed an idempotency issue if parameter ``port`` is set on protocols other than TCP/UDP (https://github.com/vultr/ansible-collection-vultr/issues/76).

vyos.vyos
~~~~~~~~~

- vyos-l3_interface_facts - fixed error when using no-default-link-local option. (https://github.com/ansible-collections/vyos.vyos/issues/295)

Known Issues
------------

Ansible-core
~~~~~~~~~~~~

- ansible-galaxy - dies in the middle of installing a role when that role contains Java inner classes (files with $ in the file name).  This is by design, to exclude temporary or backup files. (https://github.com/ansible/ansible/pull/81553).
- ansible-test - The ``pep8`` sanity test is unable to detect f-string spacing issues (E201, E202) on Python 3.10 and 3.11. They are correctly detected under Python 3.12. See (https://github.com/PyCQA/pycodestyle/issues/1190).

community.crypto
~~~~~~~~~~~~~~~~

- Ansible markup will show up in raw form on ansible-doc text output for ansible-core before 2.15. If you have trouble deciphering the documentation markup, please upgrade to ansible-core 2.15 (or newer), or read the HTML documentation on https://docs.ansible.com/ansible/devel/collections/community/crypto/.

community.dns
~~~~~~~~~~~~~

- Ansible markup will show up in raw form on ansible-doc text output for ansible-core before 2.15. If you have trouble deciphering the documentation markup, please upgrade to ansible-core 2.15 (or newer), or read the HTML documentation on https://docs.ansible.com/ansible/devel/collections/community/dns/.

community.docker
~~~~~~~~~~~~~~~~

- Ansible markup will show up in raw form on ansible-doc text output for ansible-core before 2.15. If you have trouble deciphering the documentation markup, please upgrade to ansible-core 2.15 (or newer), or read the HTML documentation on https://docs.ansible.com/ansible/devel/collections/community/docker/.

community.general
~~~~~~~~~~~~~~~~~

- Ansible markup will show up in raw form on ansible-doc text output for ansible-core before 2.15. If you have trouble deciphering the documentation markup, please upgrade to ansible-core 2.15 (or newer), or read the HTML documentation on https://docs.ansible.com/ansible/devel/collections/community/general/ (https://github.com/ansible-collections/community.general/pull/6539).

community.hrobot
~~~~~~~~~~~~~~~~

- Ansible markup will show up in raw form on ansible-doc text output for ansible-core before 2.15. If you have trouble deciphering the documentation markup, please upgrade to ansible-core 2.15 (or newer), or read the HTML documentation on https://docs.ansible.com/ansible/devel/collections/community/hrobot/.

community.routeros
~~~~~~~~~~~~~~~~~~

- Ansible markup will show up in raw form on ansible-doc text output for ansible-core before 2.15. If you have trouble deciphering the documentation markup, please upgrade to ansible-core 2.15 (or newer), or read the HTML documentation on https://docs.ansible.com/ansible/devel/collections/community/routeros/.

community.sops
~~~~~~~~~~~~~~

- Ansible markup will show up in raw form on ansible-doc text output for ansible-core before 2.15. If you have trouble deciphering the documentation markup, please upgrade to ansible-core 2.15 (or newer), or read the HTML documentation on https://docs.ansible.com/ansible/devel/collections/community/sops/.

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- ca_path missing - Issue(275740) - The roles idrac_attributes, redfish_storage_volume, and idrac_server_powerstate have a missing parameter ca_path.
- idrac_firmware - Issue(276335) - This module fails on the Python 3.11.x version with NFS shares. Use a different Python version or Share type.
- idrac_firmware - Issue(279282) - This module does not support firmware update using HTTP, HTTPS, and FTP shares with authentication on iDRAC8.
- idrac_network_attributes - Issue(279049) -  If unsupported values are provided for the parameter ``ome_network_attributes``, then this module does not provide a correct error message.
- idrac_redfish_storage_controller - Issue(256164) - If incorrect value is provided for one of the attributes in the provided attribute list for controller configuration, then this module does not exit with error.
- ome_device_network_services - Issue(212681) - The module does not provide a proper error message if unsupported values are provided for the following parameters- port_number, community_name, max_sessions, max_auth_retries, and idle_timeout.
- ome_device_power_settings - Issue(212679) - The module displays the following message if the value provided for the parameter ``power_cap`` is not within the supported range of 0 to 32767, ``Unable to complete the request because PowerCap does not exist or is not applicable for the resource URI.``
- ome_device_quick_deploy - Issue(275231) - This module does not deploy a new configuration to a slot that has disabled IPv6.
- ome_smart_fabric_uplink - Issue(186024) - Despite the module supported by OpenManage Enterprise Modular, it does not allow the creation of multiple uplinks of the same name. If an uplink is created using the same name as an existing uplink, the existing uplink is modified.

New Plugins
-----------

Cliconf
~~~~~~~

- ansible.netcommon.default - General purpose cliconf plugin for new platforms

Filter
~~~~~~

- ansible.utils.ipcut - This filter is designed to get 1st or last few bits of IP address.
- ansible.utils.ipv6form - This filter is designed to convert ipv6 address in different formats. For example expand, compressetc.
- community.crypto.gpg_fingerprint - Retrieve a GPG fingerprint from a GPG public or private key

Inventory
~~~~~~~~~

- community.aws.aws_mq - MQ broker inventory source

Lookup
~~~~~~

- community.crypto.gpg_fingerprint - Retrieve a GPG fingerprint from a GPG public or private key file
- community.dns.lookup - Look up DNS records
- community.dns.lookup_as_dict - Look up DNS records as dictionaries
- community.general.bitwarden_secrets_manager - Retrieve secrets from Bitwarden Secrets Manager

New Modules
-----------

amazon.aws
~~~~~~~~~~

- amazon.aws.ec2_import_image - Manage AWS EC2 import image tasks
- amazon.aws.ec2_import_image_info - Gather information about import virtual machine tasks
- amazon.aws.ec2_key_info - Gather information about EC2 key pairs in AWS
- amazon.aws.iam_instance_profile - manage IAM instance profiles
- amazon.aws.iam_instance_profile_info - gather information on IAM instance profiles
- amazon.aws.rds_global_cluster_info - Obtain information about Aurora global database clusters

cisco.ios
~~~~~~~~~

- cisco.ios.ios_service - Resource module to configure service.

cisco.iosxr
~~~~~~~~~~~

- cisco.iosxr.iosxr_bgp_templates - Manages BGP templates resource module.

cisco.nxos
~~~~~~~~~~

- cisco.nxos.nxos_fc_interfaces - Fc Interfaces resource module

cloudscale_ch.cloud
~~~~~~~~~~~~~~~~~~~

- cloudscale_ch.cloud.load_balancer - Manages load balancers on the cloudscale.ch IaaS service
- cloudscale_ch.cloud.load_balancer_health_monitor - Manages load balancers on the cloudscale.ch IaaS service
- cloudscale_ch.cloud.load_balancer_listener - Manages load balancer listeners on the cloudscale.ch IaaS service
- cloudscale_ch.cloud.load_balancer_pool - Manages load balancer pools on the cloudscale.ch IaaS service
- cloudscale_ch.cloud.load_balancer_pool_member - Manages load balancer pool members on the cloudscale.ch IaaS service

community.aws
~~~~~~~~~~~~~

- community.aws.route53_wait - wait for changes in Amazons Route 53 DNS service to propagate

community.dns
~~~~~~~~~~~~~

- community.dns.nameserver_info - Look up nameservers for a DNS name
- community.dns.nameserver_record_info - Look up all records of a type from all nameservers for a DNS name

community.general
~~~~~~~~~~~~~~~~~

- community.general.consul_policy - Manipulate Consul policies
- community.general.consul_role - Manipulate Consul roles
- community.general.facter_facts - Runs the discovery program C(facter) on the remote system and return Ansible facts
- community.general.gio_mime - Set default handler for MIME type, for applications using Gnome GIO
- community.general.gitlab_instance_variable - Creates, updates, or deletes GitLab instance variables
- community.general.gitlab_merge_request - Create, update, or delete GitLab merge requests
- community.general.jenkins_build_info - Get information about Jenkins builds
- community.general.keycloak_authentication_required_actions - Allows administration of Keycloak authentication required actions
- community.general.keycloak_authz_custom_policy - Allows administration of Keycloak client custom Javascript policies via Keycloak API
- community.general.keycloak_authz_permission - Allows administration of Keycloak client authorization permissions via Keycloak API
- community.general.keycloak_authz_permission_info - Query Keycloak client authorization permissions information
- community.general.keycloak_realm_key - Allows administration of Keycloak realm keys via Keycloak API
- community.general.keycloak_user - Create and configure a user in Keycloak
- community.general.lvg_rename - Renames LVM volume groups
- community.general.pnpm - Manage node.js packages with pnpm
- community.general.proxmox_pool - Pool management for Proxmox VE cluster
- community.general.proxmox_pool_member - Add or delete members from Proxmox VE cluster pools
- community.general.proxmox_vm_info - Retrieve information about one or more Proxmox VE virtual machines
- community.general.simpleinit_msb - Manage services on Source Mage GNU/Linux

community.grafana
~~~~~~~~~~~~~~~~~

- community.grafana.grafana_organization_user - Manage Grafana Organization Users.

community.vmware
~~~~~~~~~~~~~~~~

- community.vmware.vcenter_root_password_expiration - root password expiration of vCSA
- community.vmware.vmware_cluster_drs_recommendations - Apply DRS Recommendations
- community.vmware.vmware_host_graphics - Manage Host Graphic Settings
- community.vmware.vmware_vasa - Manage VMware Virtual Volumes storage provider
- community.vmware.vmware_vasa_info - Gather information about vSphere VASA providers.
- community.vmware.vmware_vsan_release_catalog - Uploads the vSAN Release Catalog

community.zabbix
~~~~~~~~~~~~~~~~

- community.zabbix.zabbix_regexp - Create/update/delete Zabbix regular expression
- community.zabbix.zabbix_settings - Update Zabbix global settings.
- community.zabbix.zabbix_token - Create/Update/Generate/Delete Zabbix token.

containers.podman
~~~~~~~~~~~~~~~~~

- containers.podman.podman_container_exec - Executes a command in a running container
- containers.podman.podman_runlabel - Run given label from given image

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

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- dellemc.openmanage.idrac_network_attributes - This module allows you to configure the port and partition network attributes on the network interface cards.
- dellemc.openmanage.ome_alert_policies - Manage OME alert policies.
- dellemc.openmanage.ome_alert_policies_action_info - Get information on actions of alert policies.
- dellemc.openmanage.ome_alert_policies_category_info - Retrieves information of all OME alert policy categories.
- dellemc.openmanage.ome_alert_policies_info - Retrieves information of one or more OME alert policies.
- dellemc.openmanage.ome_alert_policies_message_id_info - Get message ID information of alert policies.
- dellemc.openmanage.redfish_firmware_rollback - To perform a component firmware rollback using component name.

dellemc.powerflex
~~~~~~~~~~~~~~~~~

- dellemc.powerflex.snapshot_policy - Manage snapshot policies on Dell PowerFlex

dellemc.unity
~~~~~~~~~~~~~

- dellemc.unity.replication_session - Manage replication session on the Unity storage system

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
- fortinet.fortimanager.fmgr_dvmdb_upgrade - no description
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
- fortinet.fortimanager.fmgr_firewall_accessproxy6_apigateway6_quic - QUIC setting.
- fortinet.fortimanager.fmgr_firewall_accessproxy6_apigateway6_realservers - Select the real servers that this Access Proxy will distribute traffic to.
- fortinet.fortimanager.fmgr_firewall_accessproxy6_apigateway6_sslciphersuites - SSL/TLS cipher suites to offer to a server, ordered by priority.
- fortinet.fortimanager.fmgr_firewall_accessproxy6_apigateway_quic - QUIC setting.
- fortinet.fortimanager.fmgr_firewall_accessproxy6_apigateway_realservers - Select the real servers that this Access Proxy will distribute traffic to.
- fortinet.fortimanager.fmgr_firewall_accessproxy6_apigateway_sslciphersuites - SSL/TLS cipher suites to offer to a server, ordered by priority.
- fortinet.fortimanager.fmgr_firewall_accessproxy_apigateway6_quic - QUIC setting.
- fortinet.fortimanager.fmgr_firewall_accessproxy_apigateway_quic - QUIC setting.
- fortinet.fortimanager.fmgr_firewall_address6_profilelist - List of NSX service profiles that use this address.
- fortinet.fortimanager.fmgr_firewall_address_profilelist - List of NSX service profiles that use this address.
- fortinet.fortimanager.fmgr_firewall_casbprofile - no description
- fortinet.fortimanager.fmgr_firewall_casbprofile_saasapplication - no description
- fortinet.fortimanager.fmgr_firewall_casbprofile_saasapplication_accessrule - no description
- fortinet.fortimanager.fmgr_firewall_casbprofile_saasapplication_customcontrol - no description
- fortinet.fortimanager.fmgr_firewall_casbprofile_saasapplication_customcontrol_option - no description
- fortinet.fortimanager.fmgr_firewall_explicitproxyaddress - Explicit web proxy address configuration.
- fortinet.fortimanager.fmgr_firewall_explicitproxyaddress_headergroup - HTTP header group.
- fortinet.fortimanager.fmgr_firewall_explicitproxyaddrgrp - Explicit web proxy address group configuration.
- fortinet.fortimanager.fmgr_firewall_gtp_messagefilter - Message filter.
- fortinet.fortimanager.fmgr_firewall_ippoolgrp - Configure IPv4 pool groups.
- fortinet.fortimanager.fmgr_firewall_networkservicedynamic - Configure Dynamic Network Services.
- fortinet.fortimanager.fmgr_firewall_vendormac - Show vendor and the MAC address they have.
- fortinet.fortimanager.fmgr_firewall_vip_quic - QUIC setting.
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
- fortinet.fortimanager.fmgr_pm_config_meta_reference - no description
- fortinet.fortimanager.fmgr_pm_config_pblock_firewall_consolidated_policy - Configure consolidated IPv4/IPv6 policies.
- fortinet.fortimanager.fmgr_pm_config_pblock_firewall_consolidated_policy_sectionvalue - Configure consolidated IPv4/IPv6 policies.
- fortinet.fortimanager.fmgr_pm_config_pblock_firewall_policy6 - Configure IPv6 policies.
- fortinet.fortimanager.fmgr_pm_config_pblock_firewall_policy6_sectionvalue - Configure IPv6 policies.
- fortinet.fortimanager.fmgr_pm_devprof_scopemember - no description
- fortinet.fortimanager.fmgr_pm_pkg_scopemember - Policy package or folder.
- fortinet.fortimanager.fmgr_pm_wanprof_scopemember - no description
- fortinet.fortimanager.fmgr_securityconsole_install_objects_v2 - no description
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
- fortinet.fortimanager.fmgr_switchcontroller_managedswitch_routeoffloadrouter - Configure route offload MCLAG IP address.
- fortinet.fortimanager.fmgr_switchcontroller_managedswitch_staticmac - Configuration method to edit FortiSwitch Static and Sticky MAC.
- fortinet.fortimanager.fmgr_switchcontroller_managedswitch_stpinstance - Configuration method to edit Spanning Tree Protocol
- fortinet.fortimanager.fmgr_switchcontroller_ptp_profile - Global PTP profile.
- fortinet.fortimanager.fmgr_switchcontroller_switchinterfacetag - Configure switch object tags.
- fortinet.fortimanager.fmgr_switchcontroller_trafficpolicy - Configure FortiSwitch traffic policy.
- fortinet.fortimanager.fmgr_switchcontroller_vlanpolicy - Configure VLAN policy to be applied on the managed FortiSwitch ports through dynamic-port-policy.
- fortinet.fortimanager.fmgr_sys_cloud_orchest - no description
- fortinet.fortimanager.fmgr_system_csf - Add this device to a Security Fabric or set up a new Security Fabric on this device.
- fortinet.fortimanager.fmgr_system_csf_fabricconnector - Fabric connector configuration.
- fortinet.fortimanager.fmgr_system_csf_trustedlist - Pre-authorized and blocked security fabric nodes.
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
- fortinet.fortimanager.fmgr_system_sdnproxy - Configure SDN proxy.
- fortinet.fortimanager.fmgr_system_socfabric_trustedlist - Pre-authorized security fabric nodes
- fortinet.fortimanager.fmgr_um_image_upgrade - The older API for updating the firmware of specific device.
- fortinet.fortimanager.fmgr_um_image_upgrade_ext - Update the firmware of specific device.
- fortinet.fortimanager.fmgr_user_certificate - Configure certificate users.
- fortinet.fortimanager.fmgr_user_deviceaccesslist - Configure device access control lists.
- fortinet.fortimanager.fmgr_user_deviceaccesslist_devicelist - Device list.
- fortinet.fortimanager.fmgr_user_flexvm - no description
- fortinet.fortimanager.fmgr_user_json - no description
- fortinet.fortimanager.fmgr_user_saml_dynamicmapping - SAML server entry configuration.
- fortinet.fortimanager.fmgr_virtualpatch_profile - Configure virtual-patch profile.
- fortinet.fortimanager.fmgr_virtualpatch_profile_exemption - Exempt devices or rules.
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

inspur.ispim
~~~~~~~~~~~~

- inspur.ispim.hba_info - Get CPU information
- inspur.ispim.update_psu - Update PSU

netapp.ontap
~~~~~~~~~~~~

- netapp.ontap.na_ontap_active_directory_domain_controllers - NetApp ONTAP configure active directory preferred domain controllers
- netapp.ontap.na_ontap_ems_config - NetApp ONTAP module to modify EMS configuration.

netbox.netbox
~~~~~~~~~~~~~

- netbox.netbox.netbox_config_template - Creates, updates, or removed a config template from NetBox

ngine_io.exoscale
~~~~~~~~~~~~~~~~~

- ngine_io.exoscale.instance_rdns_record - Manages reverse DNS records for Exoscale compute instances.

purestorage.flasharray
~~~~~~~~~~~~~~~~~~~~~~

- purestorage.flasharray.purefa_file - Manage FlashArray File Copies
- purestorage.flasharray.purefa_logging - Manage Pure Storage FlashArray Audit and Session logs

sensu.sensu_go
~~~~~~~~~~~~~~

- sensu.sensu_go.pipeline - Manage Sensu pipelines.
- sensu.sensu_go.pipeline_info - List Sensu pipelines.

t_systems_mms.icinga_director
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- t_systems_mms.icinga_director.icinga_deploy - Trigger deployment in Icinga2
- t_systems_mms.icinga_director.icinga_deploy_info - Get deployment information through the director API

theforeman.foreman
~~~~~~~~~~~~~~~~~~

- theforeman.foreman.smart_class_parameter_override_value - Manage Smart Class Parameter Override Values
- theforeman.foreman.wait_for_task - Wait for a task

vultr.cloud
~~~~~~~~~~~

- vultr.cloud.bare_metal - Manages bare metal machines on Vultr.
- vultr.cloud.vpc2 - Manages VPCs 2.0 on Vultr
- vultr.cloud.vpc2_info - Gather information about the Vultr VPCs 2.0

New Roles
---------

- dellemc.openmanage.idrac_attributes - Role to configure iDRAC attributes.
- dellemc.openmanage.idrac_bios - Role to modify BIOS attributes, clear pending BIOS attributes, and reset the BIOS to default settings.
- dellemc.openmanage.idrac_boot - Configure the boot order settings
- dellemc.openmanage.idrac_job_queue - Role to manage the iDRAC lifecycle controller job queue.
- dellemc.openmanage.idrac_reset - Role to reset and restart iDRAC (iDRAC8 and iDRAC9 only) for Dell PowerEdge servers.
- dellemc.openmanage.idrac_storage_controller - Role to configure the physical disk, virtual disk, and storage controller settings on iDRAC9 based PowerEdge servers.

Unchanged Collections
---------------------

- ansible.posix (still version 1.5.4)
- community.azure (still version 2.0.0)
- community.okd (still version 2.3.0)
- community.proxysql (still version 1.5.1)
- community.rabbitmq (still version 1.2.3)
- community.sap_libs (still version 1.4.1)
- frr.frr (still version 2.0.2)
- gluster.gluster (still version 1.0.2)
- hpe.nimble (still version 1.1.4)
- ibm.qradar (still version 2.1.0)
- infinidat.infinibox (still version 1.3.12)
- infoblox.nios_modules (still version 1.5.0)
- inspur.sm (still version 2.3.0)
- kubernetes.core (still version 2.4.0)
- netapp.elementsw (still version 21.7.0)
- netapp.storagegrid (still version 21.11.1)
- netapp_eseries.santricity (still version 1.4.0)
- ngine_io.cloudstack (still version 2.3.0)
- openstack.cloud (still version 2.1.0)
- openvswitch.openvswitch (still version 2.1.1)
- splunk.es (still version 2.1.0)
- vmware.vmware_rest (still version 2.3.1)
