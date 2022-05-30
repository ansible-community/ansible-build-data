=======================
Ansible 5 Release Notes
=======================

This changelog describes changes since Ansible 4.0.0.

.. contents::
  :local:
  :depth: 2

v5.8.0
======

.. contents::
  :local:
  :depth: 2

Release Summary
---------------

Release Date: 2022-05-18

`Porting Guide <https://docs.ansible.com/ansible/devel/porting_guides.html>`_

Added Collections
-----------------

- vmware.vmware_rest (version 2.1.5)

Ansible-core
------------

Ansible 5.8.0 contains Ansible-core version 2.12.5.
This is the same version of Ansible-core as in the previous Ansible release.


Changed Collections
-------------------

If not mentioned explicitly, the changes are reported in the combined changelog below.

+------------------------+---------------+---------------+-------------------------------------------------+
| Collection             | Ansible 5.7.1 | Ansible 5.8.0 | Notes                                           |
+========================+===============+===============+=================================================+
| ansible.utils          | 2.6.0         | 2.6.1         |                                                 |
+------------------------+---------------+---------------+-------------------------------------------------+
| ansible.windows        | 1.9.0         | 1.10.0        |                                                 |
+------------------------+---------------+---------------+-------------------------------------------------+
| cisco.meraki           | 2.6.1         | 2.6.2         |                                                 |
+------------------------+---------------+---------------+-------------------------------------------------+
| community.ciscosmb     | 1.0.4         | 1.0.5         |                                                 |
+------------------------+---------------+---------------+-------------------------------------------------+
| community.crypto       | 2.2.4         | 2.3.1         |                                                 |
+------------------------+---------------+---------------+-------------------------------------------------+
| community.digitalocean | 1.16.0        | 1.19.0        |                                                 |
+------------------------+---------------+---------------+-------------------------------------------------+
| community.dns          | 2.1.0         | 2.1.1         |                                                 |
+------------------------+---------------+---------------+-------------------------------------------------+
| community.docker       | 2.4.0         | 2.5.1         |                                                 |
+------------------------+---------------+---------------+-------------------------------------------------+
| community.general      | 4.8.0         | 4.8.1         |                                                 |
+------------------------+---------------+---------------+-------------------------------------------------+
| community.hashi_vault  | 2.4.0         | 2.5.0         |                                                 |
+------------------------+---------------+---------------+-------------------------------------------------+
| community.libvirt      | 1.0.2         | 1.1.0         |                                                 |
+------------------------+---------------+---------------+-------------------------------------------------+
| community.mongodb      | 1.3.3         | 1.4.0         | There are no changes recorded in the changelog. |
+------------------------+---------------+---------------+-------------------------------------------------+
| community.mysql        | 2.3.5         | 2.3.7         |                                                 |
+------------------------+---------------+---------------+-------------------------------------------------+
| community.network      | 3.1.0         | 3.3.0         |                                                 |
+------------------------+---------------+---------------+-------------------------------------------------+
| community.okd          | 2.1.0         | 2.2.0         |                                                 |
+------------------------+---------------+---------------+-------------------------------------------------+
| community.postgresql   | 1.7.2         | 1.7.4         |                                                 |
+------------------------+---------------+---------------+-------------------------------------------------+
| community.rabbitmq     | 1.1.0         | 1.2.1         |                                                 |
+------------------------+---------------+---------------+-------------------------------------------------+
| community.windows      | 1.9.0         | 1.10.0        |                                                 |
+------------------------+---------------+---------------+-------------------------------------------------+
| frr.frr                | 1.0.3         | 1.0.4         |                                                 |
+------------------------+---------------+---------------+-------------------------------------------------+
| kubernetes.core        | 2.3.0         | 2.3.1         |                                                 |
+------------------------+---------------+---------------+-------------------------------------------------+
| netapp.cloudmanager    | 21.16.0       | 21.17.0       |                                                 |
+------------------------+---------------+---------------+-------------------------------------------------+
| netapp.ontap           | 21.18.1       | 21.19.1       |                                                 |
+------------------------+---------------+---------------+-------------------------------------------------+
| netbox.netbox          | 3.7.0         | 3.7.1         |                                                 |
+------------------------+---------------+---------------+-------------------------------------------------+
| purestorage.flasharray | 1.12.1        | 1.13.0        |                                                 |
+------------------------+---------------+---------------+-------------------------------------------------+
| vmware.vmware_rest     |               | 2.1.5         | The collection was added to Ansible             |
+------------------------+---------------+---------------+-------------------------------------------------+

Major Changes
-------------

community.mysql
~~~~~~~~~~~~~~~

- The community.mysql collection no longer supports ``Ansible 2.9`` and ``ansible-base 2.10``. While we take no active measures to prevent usage and there are no plans to introduce incompatible code to the modules, we will stop testing against ``Ansible 2.9`` and ``ansible-base 2.10``. Both will very soon be End of Life and if you are still using them, you should consider upgrading to the ``latest Ansible / ansible-core 2.11 or later`` as soon as possible (https://github.com/ansible-collections/community.mysql/pull/343).

community.postgresql
~~~~~~~~~~~~~~~~~~~~

- The community.postgresql collection no longer supports ``Ansible 2.9`` and ``ansible-base 2.10``. While we take no active measures to prevent usage and there are no plans to introduce incompatible code to the modules, we will stop testing against ``Ansible 2.9`` and ``ansible-base 2.10``. Both will very soon be End of Life and if you are still using them, you should consider upgrading to the ``latest Ansible / ansible-core 2.11 or later`` as soon as possible (https://github.com/ansible-collections/community.postgresql/pull/245).

Minor Changes
-------------

ansible.windows
~~~~~~~~~~~~~~~

- setup - Added ipv4, ipv6, mtu and speed data to ansible_interfaces
- win_environment - Trigger ``WM_SETTINGCHANGE`` on a change to notify other host processes of an environment change
- win_path - Migrate to newer style module parser that adds features like module invocation under ``-vvv``
- win_path - Trigger ``WM_SETTINGCHANGE`` on a change to notify other host processes of an environment change

cisco.meraki
~~~~~~~~~~~~

- Add execution-environment.yml in meta as the base to a Meraki ee
- meraki_network - Add Products to net_type list

community.ciscosmb
~~~~~~~~~~~~~~~~~~

- CI  change <plugin_type> <name> to name <name> for validate-module
- CI - add ansible 2.13 to test matrix

community.crypto
~~~~~~~~~~~~~~~~

- Prepare collection for inclusion in an Execution Environment by declaring its dependencies. Please note that system packages are used for cryptography and PyOpenSSL, which can be rather limited. If you need features from newer cryptography versions, you will have to manually force a newer version to be installed by pip by specifying something like ``cryptography >= 37.0.0`` in your Execution Environment's Python dependencies file (https://github.com/ansible-collections/community.crypto/pull/440).
- Support automatic conversion for Internalionalized Domain Names (IDNs). When passing general names, for example Subject Altenative Names to ``community.crypto.openssl_csr``, these will automatically be converted to IDNA. Conversion will be done per label to IDNA2008 if possible, and IDNA2003 if IDNA2008 conversion fails for that label. Note that IDNA conversion requires `the Python idna library <https://pypi.org/project/idna/>`_ to be installed. Please note that depending on which versions of the cryptography library are used, it could try to process the converted IDNA another time with the Python ``idna`` library and reject IDNA2003 encoded values. Using a new enough ``cryptography`` version avoids this (https://github.com/ansible-collections/community.crypto/issues/426, https://github.com/ansible-collections/community.crypto/pull/436).
- acme_* modules - add parameter ``request_timeout`` to manage HTTP(S) request timeout (https://github.com/ansible-collections/community.crypto/issues/447, https://github.com/ansible-collections/community.crypto/pull/448).
- luks_devices - added ``perf_same_cpu_crypt``, ``perf_submit_from_crypt_cpus``, ``perf_no_read_workqueue``, ``perf_no_write_workqueue`` for performance tuning when opening LUKS2 containers (https://github.com/ansible-collections/community.crypto/issues/427).
- luks_devices - added ``persistent`` option when opening LUKS2 containers (https://github.com/ansible-collections/community.crypto/pull/434).
- openssl_csr_info - add ``name_encoding`` option to control the encoding (IDNA, Unicode) used to return domain names in general names (https://github.com/ansible-collections/community.crypto/pull/436).
- openssl_pkcs12 - allow to provide the private key as text instead of having to read it from a file. This allows to store the private key in an encrypted form, for example in Ansible Vault (https://github.com/ansible-collections/community.crypto/pull/452).
- x509_certificate_info - add ``name_encoding`` option to control the encoding (IDNA, Unicode) used to return domain names in general names (https://github.com/ansible-collections/community.crypto/pull/436).
- x509_crl - add ``name_encoding`` option to control the encoding (IDNA, Unicode) used to return domain names in general names (https://github.com/ansible-collections/community.crypto/pull/436).
- x509_crl_info - add ``name_encoding`` option to control the encoding (IDNA, Unicode) used to return domain names in general names (https://github.com/ansible-collections/community.crypto/pull/436).

community.digitalocean
~~~~~~~~~~~~~~~~~~~~~~

- ci - adding stable-2.13 to sanity and unit testing (https://github.com/ansible-collections/community.digitalocean/issues/239).
- digital_ocean - parameterize the DigitalOcean API base url (https://github.com/ansible-collections/community.digitalocean/issues/237).
- digital_ocean - reference C(DO_API_TOKEN) consistently in module documentation and examples (https://github.com/ansible-collections/community.digitalocean/issues/248).
- digital_ocean_spaces - set C(no_log=True) for C(aws_access_key_id) parameter (https://github.com/ansible-collections/community.digitalocean/issues/243).
- digital_ocean_spaces_info - set C(no_log=True) for C(aws_access_key_id) parameter (https://github.com/ansible-collections/community.digitalocean/issues/243).

community.docker
~~~~~~~~~~~~~~~~

- docker_config - add support for ``template_driver`` with one option ``golang`` (https://github.com/ansible-collections/community.docker/issues/332, https://github.com/ansible-collections/community.docker/pull/345).
- docker_swarm - adds ``data_path_addr`` parameter during swarm initialization or when joining (https://github.com/ansible-collections/community.docker/issues/339).

community.hashi_vault
~~~~~~~~~~~~~~~~~~~~~

- vault_login module & lookup - no friendly error message was given when ``hvac`` was missing (https://github.com/ansible-collections/community.hashi_vault/issues/257).
- vault_pki_certificate - add ``vault_pki_certificate`` to the ``community.hashi_vault.vault`` action group (https://github.com/ansible-collections/community.hashi_vault/issues/251).
- vault_read module & lookup - no friendly error message was given when ``hvac`` was missing (https://github.com/ansible-collections/community.hashi_vault/issues/257).
- vault_token_create - add ``vault_token_create`` to the ``community.hashi_vault.vault`` action group (https://github.com/ansible-collections/community.hashi_vault/issues/251).
- vault_token_create module & lookup - no friendly error message was given when ``hvac`` was missing (https://github.com/ansible-collections/community.hashi_vault/issues/257).
- vault_write - add ``vault_write`` to the ``community.hashi_vault.vault`` action group (https://github.com/ansible-collections/community.hashi_vault/issues/251).

community.okd
~~~~~~~~~~~~~

- add action groups to runtime.yml (https://github.com/openshift/community.okd/issues/41).

community.rabbitmq
~~~~~~~~~~~~~~~~~~

- rabbitmq_user - add support for `topic authorization <https://www.rabbitmq.com/access-control.html#topic-authorisation>`_ (featured in RabbitMQ 3.7.0) (https://github.com/ansible-collections/community.rabbitmq/pull/73).

community.windows
~~~~~~~~~~~~~~~~~

- win_domain_user - Add support for managing service prinicpal names via the ``spn`` param and principals allowed to delegate via the ``delegates`` param (https://github.com/ansible-collections/community.windows/pull/365)
- win_domain_user - Added the ``groups_missing_behaviour`` option that controls the behaviour when a group specified does not exist - https://github.com/ansible-collections/community.windows/pull/375
- win_hotfix - Added the ``identifiers`` and ``kbs`` return value that is always a list of identifiers and kbs inside a hotfix
- win_psmodule - Add credential support for through the ``username`` and ``password`` options
- win_psrepository - Add credential support for through the ``username`` and ``password`` options

netapp.cloudmanager
~~~~~~~~~~~~~~~~~~~

- na_cloudmanager_aws_fsx - Import AWS FSX to CloudManager by adding new parameters ``import_file_system`` and ``file_system_id``.
- na_cloudmanager_connector_azure - Support user defined ``storage_account`` name. The ``storage_account`` can be created automatically. When ``storage_account`` is not set, the name is constructed by appending 'sa' to the connector ``name``.
- na_cloudmanager_cvo_aws - Support license_type update
- na_cloudmanager_cvo_azure - Support license_type update
- na_cloudmanager_cvo_gcp - Support license_type update

netapp.ontap
~~~~~~~~~~~~

- na_ontap_cifs - Added ``unix_symlink`` option in REST.
- na_ontap_cifs_server - Added ``force`` option for create, delete and rename cifs server when using REST.
- na_ontap_cifs_server - Added ``from_name`` option to rename cifs server when using REST.
- na_ontap_igroup_initiator - Added REST support.
- na_ontap_interface - use REST when ``use_rest`` is set to ``auto``.
- na_ontap_iscsi - Added REST support.
- na_ontap_nvme - Added REST support.
- na_ontap_qos_adaptive_policy_group - warn about deprecation, fall back to ZAPI or fail when REST is desired.
- na_ontap_qos_policy_group - Added REST only supported option ``adaptive_qos_options`` for configuring adaptive policy.
- na_ontap_qos_policy_group - Added REST only supported option ``fixed_qos_options`` for configuring max/min throughput policy.
- na_ontap_qos_policy_group - Added REST support.
- na_ontap_quotas - support TB as a unit, update doc with size format description.
- na_ontap_rest_info - new option ``owning_resource`` for REST info that requires an owning resource. For instance volume for a snapshot
- na_ontap_rest_info - support added for protocols/nfs/export-policies/rules (Requires owning_resource to be set)
- na_ontap_rest_info - support added for storage/volumes/snapshots (Requires owning_resource to be set)
- na_ontap_rest_info REST API's with hyphens in the name will now be converted to underscores when ``use_python_keys`` is set to ``True`` so that YAML parsing works correctly.
- na_ontap_rest_info support added for application/consistency-groups
- na_ontap_rest_info support added for cluster/fireware/history
- na_ontap_rest_info support added for cluster/mediators
- na_ontap_rest_info support added for cluster/metrocluster/dr-groups
- na_ontap_rest_info support added for cluster/metrocluster/interconnects
- na_ontap_rest_info support added for cluster/metrocluster/operations
- na_ontap_rest_info support added for cluster/ntp/keys
- na_ontap_rest_info support added for cluster/web
- na_ontap_rest_info support added for name-services/local-hosts
- na_ontap_rest_info support added for name-services/unix-groups
- na_ontap_rest_info support added for name-services/unix-users
- na_ontap_rest_info support added for network/ethernet/switch/ports
- na_ontap_rest_info support added for network/fc/ports
- na_ontap_rest_info support added for network/http-proxy
- na_ontap_rest_info support added for network/ip/bgp/peer-groups
- na_ontap_rest_info support added for protocols/audit
- na_ontap_rest_info support added for protocols/cifs/domains
- na_ontap_rest_info support added for protocols/cifs/local-groups
- na_ontap_rest_info support added for protocols/cifs/local-users
- na_ontap_rest_info support added for protocols/cifs/sessions
- na_ontap_rest_info support added for protocols/cifs/unix-symlink-mapping
- na_ontap_rest_info support added for protocols/cifs/users-and-groups/privilege
- na_ontap_rest_info support added for protocols/file-access-tracing/events
- na_ontap_rest_info support added for protocols/file-access-tracing/filters
- na_ontap_rest_info support added for protocols/fpolicy
- na_ontap_rest_info support added for protocols/locks
- na_ontap_rest_info support added for protocols/ndmp
- na_ontap_rest_info support added for protocols/ndmp/nodes
- na_ontap_rest_info support added for protocols/ndmp/sessions
- na_ontap_rest_info support added for protocols/ndmp/svms
- na_ontap_rest_info support added for protocols/nfs/connected-clients
- na_ontap_rest_info support added for protocols/nfs/kerberos/interfaces
- na_ontap_rest_info support added for protocols/nvme/subsystem-controllers
- na_ontap_rest_info support added for protocols/nvme/subsystem-maps
- na_ontap_rest_info support added for protocols/s3/buckets
- na_ontap_rest_info support added for protocols/s3/services
- na_ontap_rest_info support added for protocols/san/iscsi/sessions
- na_ontap_rest_info support added for protocols/san/portsets
- na_ontap_rest_info support added for protocols/san/vvol-bindings
- na_ontap_rest_info support added for security/anti-ransomware/suspects
- na_ontap_rest_info support added for security/audit
- na_ontap_rest_info support added for security/audit/messages
- na_ontap_rest_info support added for security/authentication/cluster/ad-proxy
- na_ontap_rest_info support added for security/authentication/cluster/ldap
- na_ontap_rest_info support added for security/authentication/cluster/nis
- na_ontap_rest_info support added for security/authentication/cluster/saml-sp
- na_ontap_rest_info support added for security/authentication/publickeys
- na_ontap_rest_info support added for security/azure-key-vaults
- na_ontap_rest_info support added for security/certificates
- na_ontap_rest_info support added for security/gcp-kms
- na_ontap_rest_info support added for security/ipsec
- na_ontap_rest_info support added for security/ipsec/ca-certificates
- na_ontap_rest_info support added for security/ipsec/policies
- na_ontap_rest_info support added for security/ipsec/security-associations
- na_ontap_rest_info support added for security/key-manager-configs
- na_ontap_rest_info support added for security/key-managers
- na_ontap_rest_info support added for security/key-stores
- na_ontap_rest_info support added for security/login/messages
- na_ontap_rest_info support added for security/ssh
- na_ontap_rest_info support added for security/ssh/svms
- na_ontap_rest_info support added for storage/cluster
- na_ontap_rest_info support added for storage/file/clone/split-loads
- na_ontap_rest_info support added for storage/file/clone/split-status
- na_ontap_rest_info support added for storage/file/clone/tokens
- na_ontap_rest_info support added for storage/monitored-files
- na_ontap_rest_info support added for storage/qos/workloads
- na_ontap_rest_info support added for storage/snaplock/audit-logs
- na_ontap_rest_info support added for storage/snaplock/compliance-clocks
- na_ontap_rest_info support added for storage/snaplock/event-retention/operations
- na_ontap_rest_info support added for storage/snaplock/event-retention/policies
- na_ontap_rest_info support added for storage/snaplock/file-fingerprints
- na_ontap_rest_info support added for storage/snaplock/litigations
- na_ontap_rest_info support added for storage/switches
- na_ontap_rest_info support added for storage/tape-devices
- na_ontap_rest_info support added for support/auto-update
- na_ontap_rest_info support added for support/auto-update/configurations
- na_ontap_rest_info support added for support/auto-update/updates
- na_ontap_rest_info support added for support/configuration-backup
- na_ontap_rest_info support added for support/configuration-backup/backups
- na_ontap_rest_info support added for support/coredump/coredumps
- na_ontap_rest_info support added for support/ems/messages
- na_ontap_rest_info support added for support/snmp
- na_ontap_rest_info support added for support/snmp/users
- na_ontap_rest_info support added for svm/migrations
- na_ontap_volume_autosize - improve error reporting.

purestorage.flasharray
~~~~~~~~~~~~~~~~~~~~~~

- purefa_fs - Add support for replicated file systems
- purefa_info - Add QoS information for volume groups
- purefa_info - Add info for protection group safe mode setting (Requires Purity//FA 6.3.0 or higher)
- purefa_info - Add info for protection group snapshots
- purefa_info - Add priority adjustment information for volumes and volume groups
- purefa_info - Split volume groups into live and deleted dicts
- purefa_pg - Add support for protection group SafeMode. Requires Purity//FA 6.3.0 or higher
- purefa_policy - Allow directories in snapshot policies to be managed
- purefa_vg - Add DMM Priority Adjustment support
- purefa_volume - Add support for DMM Priority Adjustment
- purefa_volume - Provide volume facts for volume after recovery

Deprecated Features
-------------------

community.hashi_vault
~~~~~~~~~~~~~~~~~~~~~

- token_validate options - the shared auth option ``token_validate`` will change its default from ``True`` to ``False`` in community.hashi_vault version 4.0.0. The ``vault_login`` lookup and module will keep the default value of ``True`` (https://github.com/ansible-collections/community.hashi_vault/issues/248).

community.network
~~~~~~~~~~~~~~~~~

- Support for Ansible 2.9 and ansible-base 2.10 is deprecated, and will be removed in the next major release (community.network 4.0.0) this spring. While most content will probably still work with ansible-base 2.10, we will remove symbolic links for modules and action plugins, which will make it impossible to use them with Ansible 2.9 anymore. Please use community.network 3.x.y with Ansible 2.9 and ansible-base 2.10, as these releases will continue to support Ansible 2.9 and ansible-base 2.10 even after they are End of Life (https://github.com/ansible-community/community-topics/issues/50, https://github.com/ansible-collections/community.network/pull/382).

Bugfixes
--------

ansible.windows
~~~~~~~~~~~~~~~

- win_reboot - Always set a minimum of 2 seconds for ``pre_reboot_delay`` to ensure the plugin can read the result

cisco.meraki
~~~~~~~~~~~~

- meraki_alert - Updates now properly set default destination webhook
- meraki_syslog -  Fix crash due to incorrect dictionary reference

community.crypto
~~~~~~~~~~~~~~~~

- Include ``PSF-license.txt`` file for ``plugins/module_utils/_version.py``.
- Make collection more robust when PyOpenSSL is used with an incompatible cryptography version (https://github.com/ansible-collections/community.crypto/pull/445).
- x509_crl - fix crash when ``issuer`` for a revoked certificate is specified (https://github.com/ansible-collections/community.crypto/pull/441).

community.digitalocean
~~~~~~~~~~~~~~~~~~~~~~

- digital_ocean_cdn_endpoints - remove non-API parameters before posting to the API (https://github.com/ansible-collections/community.digitalocean/issues/252).
- digital_ocean_cdn_endpoints - use the correct module name in the C(EXAMPLES) (https://github.com/ansible-collections/community.digitalocean/issues/251).

community.dns
~~~~~~~~~~~~~

- Update Public Suffix List.

community.docker
~~~~~~~~~~~~~~~~

- Include ``PSF-license.txt`` file for ``plugins/module_utils/_version.py``.

community.general
~~~~~~~~~~~~~~~~~

- Include ``PSF-license.txt`` file for ``plugins/module_utils/_version.py``.
- consul - fixed bug where class ``ConsulService`` was overwriting the field ``checks``, preventing the addition of checks to a service (https://github.com/ansible-collections/community.general/pull/4590).
- gconftool2 - properly escape values when passing them to ``gconftool-2`` (https://github.com/ansible-collections/community.general/pull/4647).
- onepassword - search all valid configuration locations and use the first found (https://github.com/ansible-collections/community.general/pull/4640).
- opentelemetry callback plugin - fix task message attribute that is reported failed regardless of the task result (https://github.com/ansible-collections/community.general/pull/4624).
- opentelemetry callback plugin - fix warning for the include_tasks (https://github.com/ansible-collections/community.general/pull/4623).
- terraform - fix list initialization to support both Python 2 and Python 3 (https://github.com/ansible-collections/community.general/issues/4531).

community.libvirt
~~~~~~~~~~~~~~~~~

- replace deprecated ``distutils.spawn.find_executable`` with Ansible's ``get_bin_path`` in ``_search_executable`` function.

community.mysql
~~~~~~~~~~~~~~~

- Include ``PSF-license.txt`` file for ``plugins/module_utils/_version.py``.
- mysql_role - remove redundant connection closing (https://github.com/ansible-collections/community.mysql/pull/330).
- mysql_user - fix missing dynamic privileges after revoke and grant privileges to user (https://github.com/ansible-collections/community.mysql/issues/120).
- mysql_user - fix parsing privs when a user has roles assigned (https://github.com/ansible-collections/community.mysql/issues/231).
- mysql_user - fix the possibility for a race condition that breaks certain (circular) replication configurations when ``DROP USER`` is executed on multiple nodes in the replica set. Adding ``IF EXISTS`` avoids the need to use ``sql_log_bin: no`` making the statement always replication safe (https://github.com/ansible-collections/community.mysql/pull/287).

community.network
~~~~~~~~~~~~~~~~~

- Collection core functions - use vendored version of ``distutils.version`` instead of the deprecated Python standard library ``distutils``.
- Include ``PSF-license.txt`` file for ``plugins/module_utils/_version.py``.

community.okd
~~~~~~~~~~~~~

- fix ocp auth failing against cluster api url with trailing slash (https://github.com/openshift/community.okd/issues/139)

community.postgresql
~~~~~~~~~~~~~~~~~~~~

- Include ``PSF-license.txt`` file for ``plugins/module_utils/_version.py``.

community.rabbitmq
~~~~~~~~~~~~~~~~~~

- Collection core functions - use vendored version of ``distutils.version`` instead of the deprecated Python standard library ``distutils``.
- Include ``PSF-license.txt`` file for ``plugins/module_utils/_version.py``.

community.windows
~~~~~~~~~~~~~~~~~

- win_hotfix - Supports hotfixes that contain multiple updates inside the supplied update msu - https://github.com/ansible-collections/community.windows/issues/284
- win_iis_webapplication - Fix physical path check for broken configurations - https://github.com/ansible-collections/community.windows/pull/385
- win_rds_cap - Fix SID lookup with any account ending with the ``@builtin`` UPN suffix
- win_rds_rap - Fix SID lookup with any account ending with the ``@builtin`` UPN suffix
- win_region - Fix junk output when copying settings across users
- win_scoop - Fix bootstrapping process to properly work when running as admin
- win_scoop_bucket - Fix handling of output and errors from each scoop command

kubernetes.core
~~~~~~~~~~~~~~~

- Catch expectation raised when the process is waiting for resources (https://github.com/ansible-collections/kubernetes.core/issues/407).
- Remove `omit` placeholder when defining resource using template parameter (https://github.com/ansible-collections/kubernetes.core/issues/431).
- k8s - fix the issue when trying to delete resources using label_selectors options (https://github.com/ansible-collections/kubernetes.core/issues/433).
- k8s_cp - fix issue when using parameter local_path with file on managed node. (https://github.com/ansible-collections/kubernetes.core/issues/421).
- k8s_drain - fix error occurring when trying to drain node with disable_eviction set to yes (https://github.com/ansible-collections/kubernetes.core/issues/416).

netapp.ontap
~~~~~~~~~~~~

- na_ontap_cifs - fixed `symlink_properties` option silently ignored for cifs share creation when using REST.
- na_ontap_cifs - fixed error in modifying comment if it is not set while creating CIFS share in REST.
- na_ontap_command - fix typo in example.
- na_ontap_interface - rename fails with 'inconsistency in rename action' for cluster interface with REST.
- na_ontap_login_messages - fix typo in examples for username.
- na_ontap_nfs - fix TypeError on NoneType as ``tcp_max_xfer_size`` is not supported in earlier ONTAP versions.
- na_ontap_nfs - fix ``Extra input`` error with ZAPI for ``is-nfsv4-enabled``.
- na_ontap_quotas - fix idempotency issue on ``disk_limit`` and ``soft_disk_limit``.
- na_ontap_service_policy - fix examples in documentation.
- na_ontap_volume - QOS policy was not set when using NAS application.
- na_ontap_volume - correctly warn when attempting to modify NAS application.
- na_ontap_volume - do not set encrypt on modify, as it is already handled with specialized ZAPI calls.
- na_ontap_volume - use ``time_out`` value when creating/modifying/deleting volumes with REST rathar than hardcoded value.

netbox.netbox
~~~~~~~~~~~~~

- nb_inventory - Ensure inventory works on NetBox versions without the site group model [#781](https://github.com/netbox-community/ansible_modules/pull/781)
- nb_inventory - Fix netbox_inventory site_group group_by @ryanmerolle in [#780](https://github.com/netbox-community/ansible_modules/pull/780)

purestorage.flasharray
~~~~~~~~~~~~~~~~~~~~~~

- purefa_host - Allow multi-host creation without requiring a suffix string
- purefa_info - Fix issue where remote arrays are not in a valid connected state
- purefa_policy - Fix idempotency issue with quota policy rules
- purefa_policy - Fix issue when creating multiple rules in an NFS policy

New Plugins
-----------

Lookup
~~~~~~

- community.hashi_vault.vault_ansible_settings - Returns plugin settings (options)
- community.hashi_vault.vault_kv1_get - Get a secret from HashiCorp Vault's KV version 1 secret store
- community.hashi_vault.vault_kv2_get - Get a secret from HashiCorp Vault's KV version 2 secret store

New Modules
-----------

community.hashi_vault
~~~~~~~~~~~~~~~~~~~~~

- community.hashi_vault.vault_kv1_get - Get a secret from HashiCorp Vault's KV version 1 secret store
- community.hashi_vault.vault_kv2_get - Get a secret from HashiCorp Vault's KV version 2 secret store

community.okd
~~~~~~~~~~~~~

- community.okd.openshift_adm_migrate_template_instances - Update TemplateInstances to point to the latest group-version-kinds
- community.okd.openshift_adm_prune_auth - Removes references to the specified roles, clusterroles, users, and groups
- community.okd.openshift_adm_prune_deployments - Remove old completed and failed deployment configs
- community.okd.openshift_adm_prune_images - Remove unreferenced images
- community.okd.openshift_import_image - Import the latest image information from a tag in a container image registry.
- community.okd.openshift_registry_info - Display information about the integrated registry.

community.windows
~~~~~~~~~~~~~~~~~

- community.windows.win_listen_ports_facts - Recopilates the facts of the listening ports of the machine

netapp.ontap
~~~~~~~~~~~~

- netapp.ontap.na_ontap_s3_buckets - NetApp ONTAP S3 Buckets

Unchanged Collections
---------------------

- amazon.aws (still version 2.2.0)
- ansible.netcommon (still version 2.6.1)
- ansible.posix (still version 1.3.0)
- arista.eos (still version 3.1.0)
- awx.awx (still version 19.4.0)
- azure.azcollection (still version 1.12.0)
- check_point.mgmt (still version 2.3.0)
- chocolatey.chocolatey (still version 1.2.0)
- cisco.aci (still version 2.2.0)
- cisco.asa (still version 2.1.0)
- cisco.intersight (still version 1.0.18)
- cisco.ios (still version 2.8.1)
- cisco.iosxr (still version 2.9.0)
- cisco.ise (still version 1.2.1)
- cisco.mso (still version 1.4.0)
- cisco.nso (still version 1.0.3)
- cisco.nxos (still version 2.9.1)
- cisco.ucs (still version 1.8.0)
- cloud.common (still version 2.1.1)
- cloudscale_ch.cloud (still version 2.2.1)
- community.aws (still version 2.4.0)
- community.azure (still version 1.1.0)
- community.fortios (still version 1.0.0)
- community.google (still version 1.0.0)
- community.grafana (still version 1.4.0)
- community.hrobot (still version 1.3.0)
- community.kubernetes (still version 2.0.1)
- community.kubevirt (still version 1.0.0)
- community.proxysql (still version 1.3.2)
- community.routeros (still version 2.0.0)
- community.sap (still version 1.0.0)
- community.skydive (still version 1.0.0)
- community.sops (still version 1.2.1)
- community.vmware (still version 1.18.0)
- community.zabbix (still version 1.6.0)
- containers.podman (still version 1.9.3)
- cyberark.conjur (still version 1.1.0)
- cyberark.pas (still version 1.0.13)
- dellemc.enterprise_sonic (still version 1.1.0)
- dellemc.openmanage (still version 4.4.0)
- dellemc.os10 (still version 1.1.1)
- dellemc.os6 (still version 1.0.7)
- dellemc.os9 (still version 1.0.4)
- f5networks.f5_modules (still version 1.16.0)
- fortinet.fortimanager (still version 2.1.5)
- fortinet.fortios (still version 2.1.4)
- gluster.gluster (still version 1.0.2)
- google.cloud (still version 1.0.2)
- hetzner.hcloud (still version 1.6.0)
- hpe.nimble (still version 1.1.4)
- ibm.qradar (still version 1.0.3)
- infinidat.infinibox (still version 1.3.3)
- infoblox.nios_modules (still version 1.2.1)
- inspur.sm (still version 1.3.0)
- junipernetworks.junos (still version 2.10.0)
- mellanox.onyx (still version 1.0.0)
- netapp.aws (still version 21.7.0)
- netapp.azure (still version 21.10.0)
- netapp.elementsw (still version 21.7.0)
- netapp.storagegrid (still version 21.10.0)
- netapp.um_info (still version 21.8.0)
- netapp_eseries.santricity (still version 1.3.0)
- ngine_io.cloudstack (still version 2.2.3)
- ngine_io.exoscale (still version 1.0.0)
- ngine_io.vultr (still version 1.1.1)
- openstack.cloud (still version 1.8.0)
- openvswitch.openvswitch (still version 2.1.0)
- ovirt.ovirt (still version 1.6.6)
- purestorage.flashblade (still version 1.9.0)
- sensu.sensu_go (still version 1.13.1)
- servicenow.servicenow (still version 1.0.6)
- splunk.es (still version 1.0.2)
- t_systems_mms.icinga_director (still version 1.29.0)
- theforeman.foreman (still version 2.2.0)
- vyos.vyos (still version 2.8.0)
- wti.remote (still version 1.0.3)

v5.7.1
======

.. contents::
  :local:
  :depth: 2

Release Summary
---------------

Release Date: 2022-05-04

`Porting Guide <https://docs.ansible.com/ansible/devel/porting_guides.html>`_

Ansible-core
------------

Ansible 5.7.1 contains Ansible-core version 2.12.5.
This is the same version of Ansible-core as in the previous Ansible release.


Changed Collections
-------------------

If not mentioned explicitly, the changes are reported in the combined changelog below.

+------------------+---------------+---------------+----------------------------------------------------------+
| Collection       | Ansible 5.7.0 | Ansible 5.7.1 | Notes                                                    |
+==================+===============+===============+==========================================================+
| fortinet.fortios | 2.1.5         | 2.1.4         | The collection did not have a changelog in this version. |
+------------------+---------------+---------------+----------------------------------------------------------+

Minor Changes
-------------

- The version of fortinet.fortios has been rolled back to 2.1.4 (from 2.1.5) to address a syntax error pending a new release of the collection (https://github.com/fortinet-ansible-dev/ansible-galaxy-fortios-collection/pull/177)

Unchanged Collections
---------------------

- amazon.aws (still version 2.2.0)
- ansible.netcommon (still version 2.6.1)
- ansible.posix (still version 1.3.0)
- ansible.utils (still version 2.6.0)
- ansible.windows (still version 1.9.0)
- arista.eos (still version 3.1.0)
- awx.awx (still version 19.4.0)
- azure.azcollection (still version 1.12.0)
- check_point.mgmt (still version 2.3.0)
- chocolatey.chocolatey (still version 1.2.0)
- cisco.aci (still version 2.2.0)
- cisco.asa (still version 2.1.0)
- cisco.intersight (still version 1.0.18)
- cisco.ios (still version 2.8.1)
- cisco.iosxr (still version 2.9.0)
- cisco.ise (still version 1.2.1)
- cisco.meraki (still version 2.6.1)
- cisco.mso (still version 1.4.0)
- cisco.nso (still version 1.0.3)
- cisco.nxos (still version 2.9.1)
- cisco.ucs (still version 1.8.0)
- cloud.common (still version 2.1.1)
- cloudscale_ch.cloud (still version 2.2.1)
- community.aws (still version 2.4.0)
- community.azure (still version 1.1.0)
- community.ciscosmb (still version 1.0.4)
- community.crypto (still version 2.2.4)
- community.digitalocean (still version 1.16.0)
- community.dns (still version 2.1.0)
- community.docker (still version 2.4.0)
- community.fortios (still version 1.0.0)
- community.general (still version 4.8.0)
- community.google (still version 1.0.0)
- community.grafana (still version 1.4.0)
- community.hashi_vault (still version 2.4.0)
- community.hrobot (still version 1.3.0)
- community.kubernetes (still version 2.0.1)
- community.kubevirt (still version 1.0.0)
- community.libvirt (still version 1.0.2)
- community.mongodb (still version 1.3.3)
- community.mysql (still version 2.3.5)
- community.network (still version 3.1.0)
- community.okd (still version 2.1.0)
- community.postgresql (still version 1.7.2)
- community.proxysql (still version 1.3.2)
- community.rabbitmq (still version 1.1.0)
- community.routeros (still version 2.0.0)
- community.sap (still version 1.0.0)
- community.skydive (still version 1.0.0)
- community.sops (still version 1.2.1)
- community.vmware (still version 1.18.0)
- community.windows (still version 1.9.0)
- community.zabbix (still version 1.6.0)
- containers.podman (still version 1.9.3)
- cyberark.conjur (still version 1.1.0)
- cyberark.pas (still version 1.0.13)
- dellemc.enterprise_sonic (still version 1.1.0)
- dellemc.openmanage (still version 4.4.0)
- dellemc.os10 (still version 1.1.1)
- dellemc.os6 (still version 1.0.7)
- dellemc.os9 (still version 1.0.4)
- f5networks.f5_modules (still version 1.16.0)
- fortinet.fortimanager (still version 2.1.5)
- frr.frr (still version 1.0.3)
- gluster.gluster (still version 1.0.2)
- google.cloud (still version 1.0.2)
- hetzner.hcloud (still version 1.6.0)
- hpe.nimble (still version 1.1.4)
- ibm.qradar (still version 1.0.3)
- infinidat.infinibox (still version 1.3.3)
- infoblox.nios_modules (still version 1.2.1)
- inspur.sm (still version 1.3.0)
- junipernetworks.junos (still version 2.10.0)
- kubernetes.core (still version 2.3.0)
- mellanox.onyx (still version 1.0.0)
- netapp.aws (still version 21.7.0)
- netapp.azure (still version 21.10.0)
- netapp.cloudmanager (still version 21.16.0)
- netapp.elementsw (still version 21.7.0)
- netapp.ontap (still version 21.18.1)
- netapp.storagegrid (still version 21.10.0)
- netapp.um_info (still version 21.8.0)
- netapp_eseries.santricity (still version 1.3.0)
- netbox.netbox (still version 3.7.0)
- ngine_io.cloudstack (still version 2.2.3)
- ngine_io.exoscale (still version 1.0.0)
- ngine_io.vultr (still version 1.1.1)
- openstack.cloud (still version 1.8.0)
- openvswitch.openvswitch (still version 2.1.0)
- ovirt.ovirt (still version 1.6.6)
- purestorage.flasharray (still version 1.12.1)
- purestorage.flashblade (still version 1.9.0)
- sensu.sensu_go (still version 1.13.1)
- servicenow.servicenow (still version 1.0.6)
- splunk.es (still version 1.0.2)
- t_systems_mms.icinga_director (still version 1.29.0)
- theforeman.foreman (still version 2.2.0)
- vyos.vyos (still version 2.8.0)
- wti.remote (still version 1.0.3)

v5.7.0
======

.. contents::
  :local:
  :depth: 2

Release Summary
---------------

Release Date: 2022-04-26

`Porting Guide <https://docs.ansible.com/ansible/devel/porting_guides.html>`_

Ansible-core
------------

Ansible 5.7.0 contains Ansible-core version 2.12.5.
This is a newer version than version 2.12.4 contained in the previous Ansible release.

The changes are reported in the combined changelog below.

Changed Collections
-------------------

If not mentioned explicitly, the changes are reported in the combined changelog below.

+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| Collection                    | Ansible 5.6.0 | Ansible 5.7.0 | Notes                                                                                                                        |
+===============================+===============+===============+==============================================================================================================================+
| ansible.utils                 | 2.5.2         | 2.6.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cloud.common                  | 2.1.0         | 2.1.1         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.dns                 | 2.0.9         | 2.1.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.docker              | 2.3.0         | 2.4.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.general             | 4.7.0         | 4.8.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.grafana             | 1.3.3         | 1.4.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.hrobot              | 1.2.3         | 1.3.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.postgresql          | 1.7.1         | 1.7.2         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.proxysql            | 1.3.1         | 1.3.2         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.zabbix              | 1.5.1         | 1.6.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| f5networks.f5_modules         | 1.15.0        | 1.16.0        |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| fortinet.fortimanager         | 2.1.4         | 2.1.5         | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| fortinet.fortios              | 2.1.4         | 2.1.5         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| netapp.cloudmanager           | 21.15.0       | 21.16.0       |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| netapp.ontap                  | 21.17.3       | 21.18.1       |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| netbox.netbox                 | 3.6.0         | 3.7.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| openstack.cloud               | 1.7.2         | 1.8.0         | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| sensu.sensu_go                | 1.13.0        | 1.13.1        |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| t_systems_mms.icinga_director | 1.28.0        | 1.29.0        |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+

Major Changes
-------------

community.postgresql
~~~~~~~~~~~~~~~~~~~~

- postgresql_user - the ``priv`` argument has been deprecated and will be removed in ``community.postgresql 3.0.0``. Please use the ``postgresql_privs`` module to grant/revoke privileges instead (https://github.com/ansible-collections/community.postgresql/issues/212).

fortinet.fortios
~~~~~~~~~~~~~~~~

- Support FortiOS 7.0.2, 7.0.3, 7.0.4, 7.0.5.

Minor Changes
-------------

ansible.utils
~~~~~~~~~~~~~

- 'consolidate' filter plugin added.

cloud.common
~~~~~~~~~~~~

- Move the content of README_ansible_turbo.module.rst in the main README.md to get visibility on Ansible Galaxy.

community.dns
~~~~~~~~~~~~~

- Prepare collection for inclusion in an Execution Environment by declaring its dependencies (https://github.com/ansible-collections/community.dns/pull/93).

community.docker
~~~~~~~~~~~~~~~~

- Prepare collection for inclusion in an Execution Environment by declaring its dependencies. The ``docker_stack*`` modules are not supported (https://github.com/ansible-collections/community.docker/pull/336).
- current_container_facts - add detection for GitHub Actions (https://github.com/ansible-collections/community.docker/pull/336).
- docker_container - support returning Docker container log output when using Docker's ``local`` logging driver, an optimized local logging driver introduced in Docker 18.09 (https://github.com/ansible-collections/community.docker/pull/337).

community.general
~~~~~~~~~~~~~~~~~

- alternatives - add ``state`` parameter, which provides control over whether the alternative should be set as the active selection for its alternatives group (https://github.com/ansible-collections/community.general/issues/4543, https://github.com/ansible-collections/community.general/pull/4557).
- atomic_container - minor refactoring (https://github.com/ansible-collections/community.general/pull/4567).
- clc_alert_policy - minor refactoring (https://github.com/ansible-collections/community.general/pull/4556).
- clc_group - minor refactoring (https://github.com/ansible-collections/community.general/pull/4556).
- clc_loadbalancer - minor refactoring (https://github.com/ansible-collections/community.general/pull/4556).
- clc_server - minor refactoring (https://github.com/ansible-collections/community.general/pull/4556).
- cmd_runner module util - reusable command runner with consistent argument formatting and sensible defaults (https://github.com/ansible-collections/community.general/pull/4476).
- datadog_monitor - support new datadog event monitor of type `event-v2 alert` (https://github.com/ansible-collections/community.general/pull/4457)
- filesystem - add support for resizing btrfs (https://github.com/ansible-collections/community.general/issues/4465).
- lxd_container - adds ``project`` option to allow selecting project for LXD instance (https://github.com/ansible-collections/community.general/pull/4479).
- lxd_profile - adds ``project`` option to allow selecting project for LXD profile (https://github.com/ansible-collections/community.general/pull/4479).
- nmap inventory plugin - add ``sudo`` option in plugin in order to execute ``sudo nmap`` so that ``nmap`` runs with elevated privileges (https://github.com/ansible-collections/community.general/pull/4506).
- nomad_job - minor refactoring (https://github.com/ansible-collections/community.general/pull/4567).
- nomad_job_info - minor refactoring (https://github.com/ansible-collections/community.general/pull/4567).
- packet_device - minor refactoring (https://github.com/ansible-collections/community.general/pull/4567).
- packet_sshkey - minor refactoring (https://github.com/ansible-collections/community.general/pull/4567).
- packet_volume - minor refactoring (https://github.com/ansible-collections/community.general/pull/4567).
- profitbricks - minor refactoring (https://github.com/ansible-collections/community.general/pull/4567).
- proxmox - minor refactoring (https://github.com/ansible-collections/community.general/pull/4567).
- proxmox inventory plugin - add token authentication as an alternative to username/password (https://github.com/ansible-collections/community.general/pull/4540).
- proxmox inventory plugin - parse LXC configs returned by the proxmox API (https://github.com/ansible-collections/community.general/pull/4472).
- proxmox_snap - add restore snapshot option (https://github.com/ansible-collections/community.general/pull/4377).
- proxmox_snap - fixed timeout value to correctly reflect time in seconds. The timeout was off by one second (https://github.com/ansible-collections/community.general/pull/4377).
- redfish_command - add ``IndicatorLedOn``, ``IndicatorLedOff``, and ``IndicatorLedBlink`` commands to the Systems category for controling system LEDs (https://github.com/ansible-collections/community.general/issues/4084).
- seport - minor refactoring (https://github.com/ansible-collections/community.general/pull/4471).
- smartos_image_info - minor refactoring (https://github.com/ansible-collections/community.general/pull/4567).
- terraform - adds ``terraform_upgrade`` parameter which allows ``terraform init`` to satisfy new provider constraints in an existing Terraform project (https://github.com/ansible-collections/community.general/issues/4333).
- udm_group - minor refactoring (https://github.com/ansible-collections/community.general/pull/4556).
- udm_share - minor refactoring (https://github.com/ansible-collections/community.general/pull/4556).
- vmadm - minor refactoring (https://github.com/ansible-collections/community.general/pull/4567).
- webfaction_app - minor refactoring (https://github.com/ansible-collections/community.general/pull/4567).
- webfaction_db - minor refactoring (https://github.com/ansible-collections/community.general/pull/4567).
- xfconf - added missing value types ``char``, ``uchar``, ``int64`` and ``uint64`` (https://github.com/ansible-collections/community.general/pull/4534).

community.grafana
~~~~~~~~~~~~~~~~~

- Remove requirement for `ds_type` and `ds_url` parameters when deleting a datasource
- add `grafana` action group in `meta/runtime.yml` to support for module group defaults
- refactor grafana_notification_channel module

community.hrobot
~~~~~~~~~~~~~~~~

- Prepare collection for inclusion in an Execution Environment by declaring its dependencies (https://github.com/ansible-collections/community.hrobot/pull/45).

community.zabbix
~~~~~~~~~~~~~~~~

- all modules - prepare for deprecation of distutils LooseVersion.
- collection - Add dependencies to other collections. This helps Ansible Galaxy automatically downloading collections that this collection relies on to run.
- connection.httpapi (plugin) - add initial httpapi connection plugin.
- httpapi.jsonrpc (plugin) - add initial httpapi for future handling of json-rpc.
- new module zabbix authentication for configuring global authentication settings in Zabbix Server's Settings section of GUI.
- new module zabbix_autoregister for configuring global autoregistration settings in Zabbix Server's Settings section of GUI.
- new module zabbix_housekeeping for configuring global housekeeping settings in Zabbix Server's Settings section of GUI.
- test_zabbix_host_info - fix Template/Group names for 5.4
- test_zabbix_screen - disable testing for screen in 5.4 (deprecated)
- zabbix_action - additional fixes to make module work with Zabbix 6.0 (https://github.com/ansible-collections/community.zabbix/pull/664)
- zabbix_action - module ported to work with Zabbix 6.0 (https://github.com/ansible-collections/community.zabbix/pull/648, https://github.com/ansible-collections/community.zabbix/pull/653)
- zabbix_agent - Check if 'firewalld' exist and is running when handler is executed.
- zabbix_agent - Install the correct Python libxml2 package on SLES15
- zabbix_agent - Move inclusion of the apache.yml tasks to later stage during execution of role.
- zabbix_agent - Prepare for Zabbix 6.0.
- zabbix_agent - Specify a minor version with zabbix_agent_version_minor for RH systems.
- zabbix_agent - There was no way to configure a specific type for the macro.
- zabbix_agent - Use multiple aliases in the configuration file with ``zabbix_agent_zabbix_alias`` or ``zabbix_agent2_zabbix_alias``.
- zabbix_maintenance - added new module parameter `tags`, which allows configuring Problem Tags on maintenances.
- zabbix_proxy - Prepare for Zabbix 6.0.
- zabbix_proxy - Specify a minor version with zabbix_proxy_version_minor for RH systems.
- zabbix_proxy - Support for Sangoma and treat it like a RHEL system.
- zabbix_server - Check the 'zabbix_server_install_database_client' variable in RedHat tasks.
- zabbix_server - Prepare for Zabbix 6.0.
- zabbix_server - Specify a minor version with zabbix_server_version_minor for RH systems.
- zabbix_user - change alias property to username (changed in 5.4) (alias is now an alias for username)
- zabbix_user_info - change alias property to username (changed in 5.4) (alias is now an alias for username)
- zabbix_web - Change format ENCRYPTION, VERIFY_HOST from string to boolean.
- zabbix_web - Specify a minor version with zabbix_web_version_minor for RH systems.

f5networks.f5_modules
~~~~~~~~~~~~~~~~~~~~~

- bigip_device_info - add UCS creation date to the data gathered
- bigip_virtual_server - add service_down_immediate_action parameter
- bigiq_regkey_license - add addon_keys parameter to the module

netapp.cloudmanager
~~~~~~~~~~~~~~~~~~~

- na_cloudmanager_connector_gcp - when using the user application default credential authentication by running the command gcloud auth application-default login, ``gcp_service_account_path`` is not needed.

netapp.ontap
~~~~~~~~~~~~

- na_ontap_cluster_config role - use na_ontap_login_messages as na_ontap_motd is deprecated.
- na_ontap_debug - report ansible version and ONTAP collection version.
- na_ontap_efficiency_policy - Added REST support.
- na_ontap_export_policy_rule - new option ``ntfs_unix_security`` for NTFS export UNIX security options added.
- na_ontap_lun - Added REST support.
- na_ontap_snapmirror -- Added more descriptive error messages for REST
- na_ontap_snapshot_policy - Added REST support to the na_ontap_snapshot_policy module.
- na_ontap_svm - add support for web services (ssl modify) - REST only with 9.8 or later.
- na_ontap_volume - add support for SnapLock - only for REST.
- na_ontap_volume - allow to modify volume after rename.
- na_ontap_volume - new option ``max_files`` to increase the inode count value.
- na_ontap_vserver_create role - support max_volumes option.

netbox.netbox
~~~~~~~~~~~~~

- Add meta information for use in Execution Environments [#753](https://github.com/netbox-community/ansible_modules/pull/753)
- Multiple modules - add new parameters added in NetBox 3.2 [#768](https://github.com/netbox-community/ansible_modules/pull/768)
- nb_inventory - Add site_group as an option [#755](https://github.com/netbox-community/ansible_modules/pull/755)
- netbox_front_port and netbox_rear_port - Add label as parameter [#766](https://github.com/netbox-community/ansible_modules/pull/766)

sensu.sensu_go
~~~~~~~~~~~~~~

- Added support for ansible 2.13
- Removed support for CentOS 8

t_systems_mms.icinga_director
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Add icinga_serviceset module (https://github.com/T-Systems-MMS/ansible-collection-icinga-director/pull/163)
- Test more ansible versions (https://github.com/T-Systems-MMS/ansible-collection-icinga-director/pull/162)

Deprecated Features
-------------------

community.general
~~~~~~~~~~~~~~~~~

- nmcli - deprecate default hairpin mode for a bridge. This so we can change it to ``false`` in community.general 7.0.0, as this is also the default in ``nmcli`` (https://github.com/ansible-collections/community.general/pull/4334).
- proxmox inventory plugin - the current default ``true`` of the ``want_proxmox_nodes_ansible_host`` option has been deprecated. The default will change to ``false`` in community.general 6.0.0. To keep the current behavior, explicitly set ``want_proxmox_nodes_ansible_host`` to ``true`` in your inventory configuration. We suggest to already switch to the new behavior by explicitly setting it to ``false``, and by using ``compose:`` to set ``ansible_host`` to the correct value. See the examples in the plugin documentation for details (https://github.com/ansible-collections/community.general/pull/4466).

Bugfixes
--------

Ansible-core
~~~~~~~~~~~~

- Ansible.ModuleUtils.SID - Use user principal name as is for lookup in the ``Convert-ToSID`` function - https://github.com/ansible/ansible/issues/77316
- Fix traceback when installing a collection from a git repository and git is not installed (https://github.com/ansible/ansible/issues/77479).
- ansible-test - Correctly detect when running as the ``root`` user (UID 0) on the origin host. The result of the detection was incorrectly being inverted.
- ansible-test - Fix skipping of tests marked ``needs/python`` on the origin host.
- ansible-test - Fix skipping of tests marked ``needs/root`` on the origin host.
- ansible-test compile sanity test - do not crash if a column could not be determined for an error (https://github.com/ansible/ansible/pull/77465).
- hostname - use ``file_get_content()`` to read the file containing the host name in the ``FileStrategy.get_permanent_hostname()`` method. This prevents a ``TypeError`` from being raised when the strategy is used (https://github.com/ansible/ansible/issues/77025).
- script - skip in check mode since the plugin cannot determine if a change will occur.
- shell/command - only skip in check mode if the options `creates` and `removes` are both None.
- winrm - Ensure ``kinit`` is run with the same ``PATH`` env var as the Ansible process

cloud.common
~~~~~~~~~~~~

- fix parameters with aliases not being passed through (https://github.com/ansible-collections/cloud.common/issues/91).
- fix turbo mode loading incorrect module (https://github.com/ansible-collections/cloud.common/pull/102).
- turbo - Ensure we don't call the module with duplicated aliased parameters.

community.dns
~~~~~~~~~~~~~

- Update Public Suffix List.

community.docker
~~~~~~~~~~~~~~~~

- docker connection plugin - make sure that ``docker_extra_args`` is used for querying the Docker version. Also ensures that the Docker version is only queried when needed. This is currently the case if a remote user is specified (https://github.com/ansible-collections/community.docker/issues/325, https://github.com/ansible-collections/community.docker/pull/327).

community.general
~~~~~~~~~~~~~~~~~

- dnsmadeeasy - fix failure on deleting DNS entries when API response does not contain monitor value (https://github.com/ansible-collections/community.general/issues/3620).
- git_branch - remove deprecated and unnecessary branch ``unprotect`` method (https://github.com/ansible-collections/community.general/pull/4496).
- gitlab_group - improve searching for projects inside group on deletion (https://github.com/ansible-collections/community.general/pull/4491).
- gitlab_group_members - handle more than 20 groups when finding a group (https://github.com/ansible-collections/community.general/pull/4491, https://github.com/ansible-collections/community.general/issues/4460, https://github.com/ansible-collections/community.general/issues/3729).
- gitlab_hook - handle more than 20 hooks when finding a hook (https://github.com/ansible-collections/community.general/pull/4491).
- gitlab_project - handle more than 20 namespaces when finding a namespace (https://github.com/ansible-collections/community.general/pull/4491).
- gitlab_project_members - handle more than 20 projects and users when finding a project resp. user (https://github.com/ansible-collections/community.general/pull/4491).
- gitlab_user - handle more than 20 users and SSH keys when finding a user resp. SSH key (https://github.com/ansible-collections/community.general/pull/4491).
- keycloak - fix parameters types for ``defaultDefaultClientScopes`` and ``defaultOptionalClientScopes`` from list of dictionaries to list of strings (https://github.com/ansible-collections/community.general/pull/4526).
- opennebula inventory plugin - complete the implementation of ``constructable`` for opennebula inventory plugin. Now ``keyed_groups``, ``compose``, ``groups`` actually work (https://github.com/ansible-collections/community.general/issues/4497).
- pacman - fixed bug where ``absent`` state did not work for locally installed packages (https://github.com/ansible-collections/community.general/pull/4464).
- pritunl - fixed bug where pritunl plugin api add unneeded data in ``auth_string`` parameter (https://github.com/ansible-collections/community.general/issues/4527).
- proxmox inventory plugin - fix error when parsing container with LXC configs (https://github.com/ansible-collections/community.general/issues/4472, https://github.com/ansible-collections/community.general/pull/4472).
- proxmox_kvm - fix a bug when getting a state of VM without name will fail (https://github.com/ansible-collections/community.general/pull/4508).
- xbps - fix error message that is reported when installing packages fails (https://github.com/ansible-collections/community.general/pull/4438).

community.hrobot
~~~~~~~~~~~~~~~~

- robot inventory plugin - do not crash if a server neither has name or primary IP set. Instead, fall back to using the server's number as the name. This can happen if unnamed rack reservations show up in your server list (https://github.com/ansible-collections/community.hrobot/issues/40, https://github.com/ansible-collections/community.hrobot/pull/47).

community.postgresql
~~~~~~~~~~~~~~~~~~~~

- postgresql_db - get rid of the deprecated psycopg2 connection alias ``database`` in favor of ``dbname`` when psycopg2 is 2.7+ is used (https://github.com/ansible-collections/community.postgresql/issues/194, https://github.com/ansible-collections/community.postgresql/pull/196).

community.proxysql
~~~~~~~~~~~~~~~~~~

- module_utils/mysql.py - Proxysql version suffix may not be an integer (https://github.com/ansible-collections/community.proxysql/pull/96).

community.zabbix
~~~~~~~~~~~~~~~~

- Various modules and plugins - use vendored version of ``distutils.version`` instead of the deprecated Python standard library ``distutils`` (https://github.com/ansible-collections/community.zabbix/pull/603). This superseedes #597.
- ZapiWrapper (module_utils) - fix only partial zabbix version is returned.
- zabbix_agent - Install Zabbix packages when zabbix_repo == other is used with yum.
- zabbix_agent - Install the Agent for MacOSX sooner than its configuration.
- zabbix_agent - The ``Install gpg key`` task for Debian did not work when a http proxy is configured.
- zabbix_agent - Use the correct URL with correct version.
- zabbix_agent - Use the correct path to determine Zabbix Agent 2 installation on Windows.
- zabbix_agent - Using the correct hostgroup as default now.
- zabbix_agent - fix for the autopsk, incl. tests with Molecule.
- zabbix_host - Added small notification that an user should have read access to get hostgroups overview.
- zabbix_host - adapter changed properties for interface comparisson
- zabbix_maintenance - should now work when creating maintenace on Zabbix 6.0 server
- zabbix_proxy - 'zcat' the zipped sql files to /tmp before executing it.
- zabbix_proxy - Check MySQL version before settings mysql_innodb_default_row_format value.
- zabbix_proxy - Install Zabbix packages when zabbix_repo == other is used with yum.
- zabbix_server - 'zcat' the zipped sql files to /tmp before executing it.
- zabbix_server - Check MySQL version before settings mysql_innodb_default_row_format value.
- zabbix_server - Install Zabbix packages when zabbix_repo == other is used with yum.
- zabbix_template - setting correct null values to fix unintentional changes
- zabbix_web - Added some default variables if the geerlingguys apache role is not used.
- zabbix_web - Specified the correct versions for php.

f5networks.f5_modules
~~~~~~~~~~~~~~~~~~~~~

- bigip_command - fixed a bug that interpreted a pipe symbol inside an input string as pipe used to combine commands
- bigip_device_certificate - adds missing space to tmsh command
- bigip_gtm_wide_ip - fixed inability to change persistence setting on existing wide ip objects

fortinet.fortios
~~~~~~~~~~~~~~~~

- Fix issues in version mismatch logic.
- Fix status issue in fortios_json_generic().
- Fix the issue of inconsistent data types in different schemas.

netapp.cloudmanager
~~~~~~~~~~~~~~~~~~~

- Add check when volume is capacity tiered.
- na_cloudmanager_connector_azure - Fix string formatting error when deleting the connector.

netapp.ontap
~~~~~~~~~~~~

- Fixed ONTAP minor version ignored in checking minimum ONTAP version.
- na_ontap_aggregate - Fixed error in delete aggregate if the ``disk_count`` is less than current disk count.
- na_ontap_autosupport - Fixed `partner_address` not working in REST.
- na_ontap_command - document that a READONLY user is not supported, even for show commands.
- na_ontap_disk_options - ONTAP 9.10.1 returns on/off rather than True/False.
- na_ontap_info - Fixes issue with na_ontap_info failing in 9.1 because of ``job-schedule-cluster``.
- na_ontap_iscsi - Fixed issue with ``start_state`` always being set to stopped when creating an ISCSI.
- na_ontap_iscsi - fixed error starting iscsi service on vserver where Service, adapter, or operation already started.
- na_ontap_lun - Fixed KeyError on options ``force_resize``, ``force_remove`` and ``force_remove_fenced`` in Zapi.
- na_ontap_lun - Fixed ``force_remove`` option silently ignored in REST.
- na_ontap_lun_map - TypeError - '>' not supported between instances of 'int' and 'str '.
- na_ontap_qtree - Fixed issue with ``oplocks`` not being changed during a modify in Zapi.
- na_ontap_qtree - Fixed issue with ``oplocks`` not warning user about not being supported in REST
- na_ontap_snapmirror - Added use_rest condition for the REST support to work when use_rest `always`.
- na_ontap_snapshot - add error message if volume is not found with REST.
- na_ontap_snapshot - fix key error on volume when using REST.
- na_ontap_snapshot_policy - Do not validate parameter when state is ``absent`` and fix KeyError on ``comment``.
- na_ontap_svm - fixed KeyError issue on protocols when vserver is stopped.
- na_ontap_volume - do not attempt to mount volume if current state is offline.
- na_ontap_volume - fix idempotency issue with compression settings when using REST.
- na_ontap_vserver_peer - Added cluster peer accept code in REST.
- na_ontap_vserver_peer - Fixed AttributeError if ``dest_hostname`` or ``peer_options`` not present.
- na_ontap_vserver_peer - Fixed ``local_name_for_peer`` and ``local_name_for_source`` options silently ignored in REST.
- na_ontap_vserver_peer - Get peer cluster name if remote peer exist else use local cluster name.
- na_ontap_vserver_peer - ignore job entry doesn't exist error with REST to bypass ONTAP issue with FSx.
- na_ontap_vserver_peer - report error if SVM peer does not see a peering relationship after create.

netbox.netbox
~~~~~~~~~~~~~

- netbox_contact_group - Fix field description [#762](https://github.com/netbox-community/ansible_modules/pull/762)
- netbox_rack - Add location as a query parameter for uniqueness check [#751](https://github.com/netbox-community/ansible_modules/pull/751)

New Plugins
-----------

Connection
~~~~~~~~~~

- community.zabbix.httpapi - Use httpapi to run command on network appliances

Httpapi
~~~~~~~

- community.zabbix.jsonrpc - HttpApi Plugin for Zabbix

New Modules
-----------

community.general
~~~~~~~~~~~~~~~~~

Cloud
^^^^^

Lxd
...

- community.general.lxd_project - Manage LXD projects

Monitoring
^^^^^^^^^^

- community.general.alerta_customer - Manage customers in Alerta

community.zabbix
~~~~~~~~~~~~~~~~

- community.zabbix.zabbix_authentication - Update Zabbix authentication
- community.zabbix.zabbix_autoregister - Update Zabbix autoregistration
- community.zabbix.zabbix_housekeeping - Update Zabbix housekeeping

f5networks.f5_modules
~~~~~~~~~~~~~~~~~~~~~

- f5networks.f5_modules.bigip_ltm_global - Manages global LTM settings

t_systems_mms.icinga_director
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- t_systems_mms.icinga_director.icinga_serviceset - Manage servicesets in Icinga2

Unchanged Collections
---------------------

- amazon.aws (still version 2.2.0)
- ansible.netcommon (still version 2.6.1)
- ansible.posix (still version 1.3.0)
- ansible.windows (still version 1.9.0)
- arista.eos (still version 3.1.0)
- awx.awx (still version 19.4.0)
- azure.azcollection (still version 1.12.0)
- check_point.mgmt (still version 2.3.0)
- chocolatey.chocolatey (still version 1.2.0)
- cisco.aci (still version 2.2.0)
- cisco.asa (still version 2.1.0)
- cisco.intersight (still version 1.0.18)
- cisco.ios (still version 2.8.1)
- cisco.iosxr (still version 2.9.0)
- cisco.ise (still version 1.2.1)
- cisco.meraki (still version 2.6.1)
- cisco.mso (still version 1.4.0)
- cisco.nso (still version 1.0.3)
- cisco.nxos (still version 2.9.1)
- cisco.ucs (still version 1.8.0)
- cloudscale_ch.cloud (still version 2.2.1)
- community.aws (still version 2.4.0)
- community.azure (still version 1.1.0)
- community.ciscosmb (still version 1.0.4)
- community.crypto (still version 2.2.4)
- community.digitalocean (still version 1.16.0)
- community.fortios (still version 1.0.0)
- community.google (still version 1.0.0)
- community.hashi_vault (still version 2.4.0)
- community.kubernetes (still version 2.0.1)
- community.kubevirt (still version 1.0.0)
- community.libvirt (still version 1.0.2)
- community.mongodb (still version 1.3.3)
- community.mysql (still version 2.3.5)
- community.network (still version 3.1.0)
- community.okd (still version 2.1.0)
- community.rabbitmq (still version 1.1.0)
- community.routeros (still version 2.0.0)
- community.sap (still version 1.0.0)
- community.skydive (still version 1.0.0)
- community.sops (still version 1.2.1)
- community.vmware (still version 1.18.0)
- community.windows (still version 1.9.0)
- containers.podman (still version 1.9.3)
- cyberark.conjur (still version 1.1.0)
- cyberark.pas (still version 1.0.13)
- dellemc.enterprise_sonic (still version 1.1.0)
- dellemc.openmanage (still version 4.4.0)
- dellemc.os10 (still version 1.1.1)
- dellemc.os6 (still version 1.0.7)
- dellemc.os9 (still version 1.0.4)
- frr.frr (still version 1.0.3)
- gluster.gluster (still version 1.0.2)
- google.cloud (still version 1.0.2)
- hetzner.hcloud (still version 1.6.0)
- hpe.nimble (still version 1.1.4)
- ibm.qradar (still version 1.0.3)
- infinidat.infinibox (still version 1.3.3)
- infoblox.nios_modules (still version 1.2.1)
- inspur.sm (still version 1.3.0)
- junipernetworks.junos (still version 2.10.0)
- kubernetes.core (still version 2.3.0)
- mellanox.onyx (still version 1.0.0)
- netapp.aws (still version 21.7.0)
- netapp.azure (still version 21.10.0)
- netapp.elementsw (still version 21.7.0)
- netapp.storagegrid (still version 21.10.0)
- netapp.um_info (still version 21.8.0)
- netapp_eseries.santricity (still version 1.3.0)
- ngine_io.cloudstack (still version 2.2.3)
- ngine_io.exoscale (still version 1.0.0)
- ngine_io.vultr (still version 1.1.1)
- openvswitch.openvswitch (still version 2.1.0)
- ovirt.ovirt (still version 1.6.6)
- purestorage.flasharray (still version 1.12.1)
- purestorage.flashblade (still version 1.9.0)
- servicenow.servicenow (still version 1.0.6)
- splunk.es (still version 1.0.2)
- theforeman.foreman (still version 2.2.0)
- vyos.vyos (still version 2.8.0)
- wti.remote (still version 1.0.3)

v5.6.0
======

.. contents::
  :local:
  :depth: 2

Release Summary
---------------

Release Date: 2022-04-05

`Porting Guide <https://docs.ansible.com/ansible/devel/porting_guides.html>`_

Added Collections
-----------------

- community.sap (version 1.0.0)

Ansible-core
------------

Ansible 5.6.0 contains Ansible-core version 2.12.4.
This is a newer version than version 2.12.3 contained in the previous Ansible release.

The changes are reported in the combined changelog below.

Changed Collections
-------------------

If not mentioned explicitly, the changes are reported in the combined changelog below.

+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| Collection                    | Ansible 5.5.0 | Ansible 5.6.0 | Notes                                                                                                                        |
+===============================+===============+===============+==============================================================================================================================+
| amazon.aws                    | 2.1.0         | 2.2.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| ansible.netcommon             | 2.5.1         | 2.6.1         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| azure.azcollection            | 1.11.0        | 1.12.0        | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.aci                     | 2.1.0         | 2.2.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.ios                     | 2.8.0         | 2.8.1         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.iosxr                   | 2.8.1         | 2.9.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.meraki                  | 2.6.0         | 2.6.1         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.mso                     | 1.3.0         | 1.4.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.nxos                    | 2.9.0         | 2.9.1         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.ucs                     | 1.7.0         | 1.8.0         | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cloudscale_ch.cloud           | 2.2.0         | 2.2.1         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.aws                 | 2.3.0         | 2.4.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.crypto              | 2.2.3         | 2.2.4         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.digitalocean        | 1.15.1        | 1.16.0        |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.dns                 | 2.0.8         | 2.0.9         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.docker              | 2.2.1         | 2.3.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.general             | 4.6.0         | 4.7.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.hashi_vault         | 2.3.0         | 2.4.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.hrobot              | 1.2.2         | 1.2.3         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.mongodb             | 1.3.2         | 1.3.3         | There are no changes recorded in the changelog.                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.sap                 |               | 1.0.0         | The collection was added to Ansible                                                                                          |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.sops                | 1.2.0         | 1.2.1         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.vmware              | 1.17.1        | 1.18.0        |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| containers.podman             | 1.9.1         | 1.9.3         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| junipernetworks.junos         | 2.9.0         | 2.10.0        |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| kubernetes.core               | 2.2.3         | 2.3.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| netapp.storagegrid            | 21.9.0        | 21.10.0       |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| netapp_eseries.santricity     | 1.2.13        | 1.3.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| ngine_io.vultr                | 1.1.0         | 1.1.1         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| t_systems_mms.icinga_director | 1.27.1        | 1.28.0        |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+

Minor Changes
-------------

amazon.aws
~~~~~~~~~~

- ec2_instance - add count parameter support (https://github.com/ansible-collections/amazon.aws/pull/539).

ansible.netcommon
~~~~~~~~~~~~~~~~~

- Redirected ipaddr filters to ansible.utils (https://github.com/ansible-collections/ansible.netcommon/pull/359).
- httpapi - new parameter retries in send() method limits the number of times a request is retried when a HTTP error that can be worked around is encountered. The default is to retry indefinitely to maintain old behavior, but this default may change in a later breaking release.

cisco.aci
~~~~~~~~~

- Add access_mode and enable_vm_folder attributes to aci_domain
- Add aci_bgp_rr_asn and aci_bgp_rr_node module and tests
- Add aci_dhcp_relay and aci_dhcp_relay_provider modules and test files (#211)
- Add aci_dns_profile, aci_dns_domain and aci_dns_provider modules and test files (#221)
- Add aci_epg_to_contract_interface module and test file
- Add aci_esg, aci_esg_contract_master, aci_esg_epg_selector, aci_esg_ip_subnet_selector and aci_esg_tag_selector modules (#212)
- Add aci_fabric_leaf_profile and aci_fabric_leaf_switch_assoc modules and test files
- Add aci_fabric_switch_policy_group module and test file
- Add aci_l3out_interface_secondary_ip module and test file
- Add description to aci_fabric_spine_switch_assoc module
- Add destination_epg, source_ip, destination_ip, span_version, flow_id, ttl, mtu, dscp, and version_enforced attributes to aci_tenant_span_dst_group module
- Add mtu and ipv6_dad attributes to aci_l3out_interface
- Add new aci_vmm_uplink and aci_vmm_uplink_container modules and test files  (#189)
- Add new priorities in the aci_epg_to_contract priority module attribute
- Add support for contract_label and subject_label into aci_epg_to_contract module
- Add support for tagging with new module aci_tag (#210)
- Add useg attribute to aci_epg module

cisco.iosxr
~~~~~~~~~~~

- IOSXR - Fix sanity for missing elements tag under list type attribute.

cisco.meraki
~~~~~~~~~~~~

- meraki_ssid - Add support for enterprise_admin_access and splash_guest_sponsor_domains with the latter required for creating a sponsor portal.

cisco.mso
~~~~~~~~~

- Update mso_schema_template_clone to use new method from NDO and unrestrict it to earlier version

cloudscale_ch.cloud
~~~~~~~~~~~~~~~~~~~

- Updated documentation: ``ssh_keys`` is a YAML list, not a string.

community.aws
~~~~~~~~~~~~~

- Added suport for retries (AWSRetry.jittered_backoff) for cloudfront_distribution (https://github.com/ansible-collections/community.aws/issues/296)

community.digitalocean
~~~~~~~~~~~~~~~~~~~~~~

- black test - added a 15 minute timeout (https://github.com/ansible-collections/community.digitalocean/issues/228).
- digital_ocean_domain - add support for IPv6 apex domain records (https://github.com/ansible-collections/community.digitalocean/issues/226).
- integration tests - added a 120 minute timeout (https://github.com/ansible-collections/community.digitalocean/issues/228).
- sanity and unit tests - added a 30 minute timeout (https://github.com/ansible-collections/community.digitalocean/issues/228).

community.docker
~~~~~~~~~~~~~~~~

- docker connection plugin - implement connection reset by clearing internal container user cache (https://github.com/ansible-collections/community.docker/pull/312).
- docker connection plugin - simplify ``actual_user`` handling code (https://github.com/ansible-collections/community.docker/pull/311).
- docker connection plugin - the plugin supports new ways to define the timeout. These are the ``ANSIBLE_DOCKER_TIMEOUT`` environment variable, the ``timeout`` setting in the ``docker_connection`` section of ``ansible.cfg``, and the ``ansible_docker_timeout`` variable (https://github.com/ansible-collections/community.docker/pull/297).
- docker_api connection plugin - implement connection reset by clearing internal container user/group ID cache (https://github.com/ansible-collections/community.docker/pull/312).
- docker_api connection plugin - the plugin supports new ways to define the timeout. These are the ``ANSIBLE_DOCKER_TIMEOUT`` environment variable, the ``timeout`` setting in the ``docker_connection`` section of ``ansible.cfg``, and the ``ansible_docker_timeout`` variable (https://github.com/ansible-collections/community.docker/pull/308).

community.general
~~~~~~~~~~~~~~~~~

- ipa_service - add ``skip_host_check`` parameter. (https://github.com/ansible-collections/community.general/pull/4417).
- keycloak_client - add ``always_display_in_console`` parameter (https://github.com/ansible-collections/community.general/issues/4390).
- keycloak_client - add ``default_client_scopes`` and ``optional_client_scopes`` parameters. (https://github.com/ansible-collections/community.general/pull/4385).
- proxmox inventory plugin - add support for templating the ``url``, ``user``, and ``password`` options (https://github.com/ansible-collections/community.general/pull/4418).
- sudoers - add support for ``runas`` parameter (https://github.com/ansible-collections/community.general/issues/4379).

community.vmware
~~~~~~~~~~~~~~~~

- Remove `version_added` documentation that pre-dates the collection, that is refers to Ansible < 2.10 (https://github.com/ansible-collections/community.vmware/pull/1215).
- vmware_object_role_permission - added VMware DV portgroup object_type for setting permissions (https://github.com/ansible-collections/community.vmware/pull/1176)
- vmware_vm_config_option - Fix the parameter not correct issue when hostname is set to ESXi host(https://github.com/ansible-collections/community.vmware/pull/1171).
- vmware_vm_info - adding fact about ``datastore_url`` to output (https://github.com/ansible-collections/community.vmware/pull/1143).

containers.podman
~~~~~~~~~~~~~~~~~

- Add requires option to podman_container module
- Fix sanity issues with a new Ansible version

junipernetworks.junos
~~~~~~~~~~~~~~~~~~~~~

- Added junos_security_policies module.
- Added junos_security_policies_global module.
- Added junos_security_zones module.

kubernetes.core
~~~~~~~~~~~~~~~

- add support for dry run with kubernetes client version >=18.20 (https://github.com/ansible-collections/kubernetes.core/pull/245).
- fixed module_defaults by removing routing hacks from runtime.yml (https://github.com/ansible-collections/kubernetes.core/pull/347).
- helm - add support for timeout cli parameter to allow setting Helm timeout independent of wait (https://github.com/ansible-collections/kubernetes.core/issues/67).
- helm - add support for wait parameter for helm uninstall command. (https://github.com/ansible-collections/kubernetes/core/issues/33).
- helm - support repo location for helm diff (https://github.com/ansible-collections/kubernetes.core/issues/174).
- helm - when ansible is executed in check mode, return the diff between what's deployed and what will be deployed.
- helm_info - add release state as a module argument (https://github.com/ansible-collections/kubernetes.core/issues/377).
- helm_plugin - Add plugin_version parameter to the helm_plugin module (https://github.com/ansible-collections/kubernetes.core/issues/157).
- helm_plugin - Add support for helm plugin update using state=update.
- helm_repository - add support for pass-credentials cli parameter (https://github.com/ansible-collections/kubernetes.core/pull/282).
- helm_repository - added support for ``host``, ``api_key``, ``validate_certs``, and ``ca_cert``.
- helm_template - add show_only and release_namespace as module arguments (https://github.com/ansible-collections/kubernetes.core/issues/313).
- k8s - add no_proxy support to k8s* (https://github.com/ansible-collections/kubernetes.core/pull/272).
- k8s - add support for server_side_apply. (https://github.com/ansible-collections/kubernetes.core/issues/87).
- k8s - add support for user impersonation. (https://github.com/ansible-collections/kubernetes/core/issues/40).
- k8s - allow resource definition using metadata.generateName (https://github.com/ansible-collections/kubernetes.core/issues/35).
- k8s lookup plugin - Enable turbo mode via environment variable  (https://github.com/ansible-collections/kubernetes.core/issues/291).
- k8s_drain - Adds ``delete_emptydir_data`` option to ``k8s_drain.delete_options`` to evict pods with an ``emptyDir`` volume attached (https://github.com/ansible-collections/kubernetes.core/pull/322).
- k8s_exec - select first container from the pod if none specified (https://github.com/ansible-collections/kubernetes.core/issues/358).
- k8s_rollback - add support for check_mode. (https://github.com/ansible-collections/kubernetes/core/issues/243).
- k8s_scale - add support for check_mode. (https://github.com/ansible-collections/kubernetes/core/issues/244).
- kubectl - wait for dd command to complete before proceeding (https://github.com/ansible-collections/kubernetes.core/pull/321).

netapp.storagegrid
~~~~~~~~~~~~~~~~~~

- na_sg_grid_gateway - supports specifying HA Groups by name or UUID.

netapp_eseries.santricity
~~~~~~~~~~~~~~~~~~~~~~~~~

- na_santricity_global - Add controller_shelf_id argument to set controller shelf identifier.
- na_santricity_volume - Add flag to control whether volume expansion operations are allowed.
- na_santricity_volume - Add volume write cache mirroring option.
- nar_santricity_host - Add volume write cache mirroring options.

t_systems_mms.icinga_director
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Added missing fields to 'icinga_host' and 'icinga_host_template' (https://github.com/T-Systems-MMS/ansible-collection-icinga-director/pull/158)

Deprecated Features
-------------------

cisco.ios
~~~~~~~~~

- Deprecates lldp module.

Bugfixes
--------

Ansible-core
~~~~~~~~~~~~

- Add a YAML representer for ``NativeJinjaText``
- Add a YAML representer for ``NativeJinjaUnsafeText``
- AnsiballZ - Ensure we use the full python package in the module cache filename to avoid a case where ``collections:`` is used to execute a module via short name, where the short name duplicates another module from ``ansible.builtin`` or another collection that was executed previously.
- Fix collection filter/test plugin redirects (https://github.com/ansible/ansible/issues/77192).
- ansible-galaxy collection verify - display files/directories not included in the FILES.json as modified content.
- ansible-test - Fix ``windows-integration`` and ``network-integration`` when used with the ``--docker`` option and user-provided inventory.
- extend timeout for ansible-galaxy when communicating with the galaxy server api, and apply it to all interactions with the api
- first_found - fix to allow for spaces in file names (https://github.com/ansible/ansible/issues/77136)
- unarchive - the ``io_buffer_size`` option added in 2.12 was not accepted by the module (https://github.com/ansible/ansible/pull/77271).

amazon.aws
~~~~~~~~~~

- aws_ec2 inventory - use the iam_role_arn configuration parameter to assume the role before trying to call DescribeRegions if the regions configuration is not set and AWS credentials provided without enough privilege to perform the DescribeRegions action. (https://github.com/ansible-collections/amazon.aws/issues/566).
- ec2_vol - Sets the Iops value in req_obj even if the iops value has not changed, to allow modifying volume types that require passing an iops value to boto. (https://github.com/ansible-collections/amazon.aws/pull/606)
- ec2_vol - changing a volume from a type that does not support IOPS (like ``standard``) to a type that does (like ``gp3``) fails (https://github.com/ansible-collections/amazon.aws/issues/626).
- ec2_vpc_igw - fix 'NoneType' object is not subscriptable error (https://github.com/ansible-collections/amazon.aws/pull/691).
- ec2_vpc_igw - use paginator for describe internet gateways and add retry to fix NoneType object is not subscriptable error (https://github.com/ansible-collections/amazon.aws/pull/695).
- elb_classic_lb - handle security_group_ids when providing security_group_names and fix broken tasks in integration test (https://github.com/ansible-collections/amazon.aws/pull/592).

ansible.netcommon
~~~~~~~~~~~~~~~~~

- Fix issue with cli_parse native_parser plugin when input is empty (https://github.com/ansible-collections/ansible.netcommon/issues/347).
- Fix validate-module sanity test.
- No activity on the transport's channel was triggering a socket.timeout() after 30 secs, even if persistent_command_timeout is set to a higher value. This patch fixes it.

cisco.aci
~~~~~~~~~

- Add pool_allocation_mode to the required parameter list in aci_vlan_pool_encap_block module
- Fix bfd issues in aci_l3out_static_routes module on pre-4.2 APICs
- Fix output_path to support multiple APIC runs in parallel
- Fix small sanity issue in aci_epg_to_contract
- Remove owner_key, owner_tag and annotation from module that do not support them
- Removed block_name from the required parameter list in aci_vlan_pool_encap_block module

cisco.ios
~~~~~~~~~

- Add symlink of modules under plugins/action.
- `ios_acls` - Fix commands sequencing for replaced state.
- `ios_acls` - Fix remarks breaking idempotent behavior.
- `ios_bgp_address_family` - Fix multiple bgp_address_family issues. Add `set` option in `send_community` to allow backwards compatibility with older configs. Add `set` option in `redistribute.connected` to allow ospf redistribution. Fix issue with ipv6 and peer-group neighbor identification. Add ability to pull `redistribute` information for address families to conform to argspec. Fix issue with not pulling `local_as` when defined for neighbors.
- `ios_facts` - Fix Line protocol parser for legacy facts where state information per interface is present.
- `ios_route_maps` - Fix parsers for correct rendering of as_number as list.
- `ios_snmp_server` - Fix parsers for views facts collection.

cisco.iosxr
~~~~~~~~~~~

- Add symlink of modules under plugins/action.
- `iosxr_snmp_server` - Add aliases for access-lists in snmp-server(https://github.com/ansible-collections/cisco.iosxr/pull/225).
- iosxr_bgp_global - Add alias for neighbor_address (https://github.com/ansible-collections/cisco.iosxr/issues/216)
- iosxr_snmp_server - Fix gather_facts issue in snmp_servers (https://github.com/ansible-collections/cisco.iosxr/issues/215)

cisco.meraki
~~~~~~~~~~~~

- meraki_mr_rf_profile - Fix issue with idempotency and creation of RF Profiles by name only
- meraki_syslog - Improve reliability for multiple roles or capitalization.

cisco.mso
~~~~~~~~~

- Fix arp_entry value issue in mso_schema_template_filter_entry
- Fix mso_schema_site_anp idempotency when children exists
- Fix use_ssl documentation to explain usage when used with HTTPAPI connection plugin

cisco.nxos
~~~~~~~~~~

- Fix action plugin redirection to make module defaults work properly.
- Fix for nxos_vlans issue (https://github.com/ansible-collections/cisco.nxos/issues/425).
- `nxos_ntp_global` - Aliased `vrf` to `use_vrf` wherever applicable to maintain consistency with models for other platforms.
- nxos_snmp_server - Add alias for community (https://github.com/ansible-collections/cisco.nxos/issues/433)

community.aws
~~~~~~~~~~~~~

- Add backoff retry logic to elb_application_lb_info (https://github.com/ansible-collections/community.aws/pull/977)
- ecs_taskdefinition - include launch_type comparison when comparing task definitions (https://github.com/ansible-collections/community.aws/pull/840)
- elb_target_group_info - Add backoff retry logic (https://github.com/ansible-collections/community.aws/pull/1001)
- iam_role - Removes unnecessary removal of permission boundary from a role when deleting a role. Unlike inline policies, permission boundaries do not need to be removed from an IAM role before deleting the IAM role. This behavior causes issues when a permission boundary is inherited that prevents removal of the permission boundary. (https://github.com/ansible-collections/community.aws/pull/961)
- redshift_info - fix invalid import path for botocore exceptions (https://github.com/ansible-collections/community.aws/issues/968).
- wafv2_web_acl - fix exception when a rule contains lists values (https://github.com/ansible-collections/community.aws/pull/962).

community.crypto
~~~~~~~~~~~~~~~~

- openssh_* modules - fix exception handling to report traceback to users for enhanced traceability (https://github.com/ansible-collections/community.crypto/pull/417).

community.digitalocean
~~~~~~~~~~~~~~~~~~~~~~

- digital_ocean_kubernetes - add missing elements type to C(node_pools.tags) and C(node_pools.taints) options (https://github.com/ansible-collections/community.digitalocean/issues/232).

community.dns
~~~~~~~~~~~~~

- Update Public Suffix List.

community.docker
~~~~~~~~~~~~~~~~

- docker connection plugin - fix option handling to be compatible with ansible-core 2.13 (https://github.com/ansible-collections/community.docker/pull/297, https://github.com/ansible-collections/community.docker/issues/307).
- docker_api connection plugin - fix option handling to be compatible with ansible-core 2.13 (https://github.com/ansible-collections/community.docker/pull/308).

community.general
~~~~~~~~~~~~~~~~~

- dsv lookup plugin - raise an Ansible error if the wrong ``python-dsv-sdk`` version is installed (https://github.com/ansible-collections/community.general/pull/4422).
- keycloak_* - the documented ``validate_certs`` parameter was not taken into account when calling the ``open_url`` function in some cases, thus enforcing certificate validation even when ``validate_certs`` was set to ``false``. (https://github.com/ansible-collections/community.general/pull/4382)
- lxd inventory plugin - do not crash if OS and release metadata are not present
  (https://github.com/ansible-collections/community.general/pull/4351).
- nmcli - fix returning "changed" when routes parameters set, also suggest new routes4 and routes6 format (https://github.com/ansible-collections/community.general/issues/4131).
- proxmox inventory plugin - fixed the ``tags_parsed`` field when Proxmox returns a single space for the ``tags`` entry (https://github.com/ansible-collections/community.general/pull/4378).
- terraform - revert bugfix https://github.com/ansible-collections/community.general/pull/4281 that tried to fix ``variable`` handling to allow complex values. It turned out that this was breaking several valid use-cases (https://github.com/ansible-collections/community.general/issues/4367, https://github.com/ansible-collections/community.general/pull/4370).
- zypper - fixed bug that caused zypper to always report [ok] and do nothing on ``state=present`` when all packages in ``name`` had a version specification (https://github.com/ansible-collections/community.general/issues/4371, https://github.com/ansible-collections/community.general/pull/4421).

community.vmware
~~~~~~~~~~~~~~~~

- vmware_dvs_host - match the list of the host nics in the correct order based on the uplink port name in vCenter (https://github.com/ansible-collections/community.vmware/issues/1242).

containers.podman
~~~~~~~~~~~~~~~~~

- Add slirp4netns idempotency for pods
- Fix MAC address detection in created container
- Fix check for read-only change of root image in podman_container module
- Fix error with exitcommand for Podman v4
- Fix issue when missing plugins entry in podman_network module
- Fix new requirements for plugins documentation
- Fix podman collection for Podman version 4
- Fix tests for podman_container module
- Remove idempotency for log level
- Strip slashes from volumes

kubernetes.core
~~~~~~~~~~~~~~~

- Various modules and plugins - use vendored version of ``distutils.version`` instead of the deprecated Python standard library ``distutils`` (https://github.com/ansible-collections/kubernetes.core/pull/314).
- common - Ensure the label_selectors parameter of _wait_for method is optional.
- helm_template - evaluate release_values after values_files, insuring highest precedence (now same behavior as in helm module). (https://github.com/ansible-collections/kubernetes.core/pull/348)
- import exception from ``kubernetes.client.rest``.
- k8s_drain - fix error caused by accessing an undefined variable when pods have local storage (https://github.com/ansible-collections/kubernetes.core/issues/292).
- k8s_info - don't wait on empty List resources (https://github.com/ansible-collections/kubernetes.core/pull/253).
- k8s_scale - fix waiting on statefulset when scaled down to 0 replicas (https://github.com/ansible-collections/kubernetes.core/issues/203).
- module_utils.common - change default opening mode to read-bytes to avoid bad interpretation of non ascii characters and strings, often present in 3rd party manifests.
- remove binary file from k8s_cp test suite (https://github.com/ansible-collections/kubernetes.core/pull/298).
- use resource prefix when finding resource and apiVersion is v1 (https://github.com/ansible-collections/kubernetes.core/issues/351).

netapp.storagegrid
~~~~~~~~~~~~~~~~~~

- na_sg_org_group - fixed behaviour where update to ``s3_policy`` is ignored if ``management_policy`` is set.

netapp_eseries.santricity
~~~~~~~~~~~~~~~~~~~~~~~~~

- santricity_host - Ensure a list of volumes are provided to prevent netapp_eseries.santricity.santricity_host (lookup) index is string not integer exception.

ngine_io.vultr
~~~~~~~~~~~~~~

- vultr_server - Fix user data not handled correctly (https://github.com/ngine-io/ansible-collection-vultr/pull/26).

t_systems_mms.icinga_director
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- role: add check_command to icinga_service_apply (https://github.com/T-Systems-MMS/ansible-collection-icinga-director/pull/161)

New Plugins
-----------

Lookup
~~~~~~

- community.hashi_vault.vault_write - Perform a write operation against HashiCorp Vault

New Modules
-----------

community.digitalocean
~~~~~~~~~~~~~~~~~~~~~~

- community.digitalocean.digital_ocean_domain_record_info - Gather information about DigitalOcean domain records

community.hashi_vault
~~~~~~~~~~~~~~~~~~~~~

- community.hashi_vault.vault_write - Perform a write operation against HashiCorp Vault

junipernetworks.junos
~~~~~~~~~~~~~~~~~~~~~

- junipernetworks.junos.junos_security_policies - Manage security policies on Junos devices.
- junipernetworks.junos.junos_security_policies_global - Manage global security policy parameters on Junos devices.
- junipernetworks.junos.junos_security_zones - Manage security zones on Junos devices.

kubernetes.core
~~~~~~~~~~~~~~~

- kubernetes.core.k8s_taint - Taint a node in a Kubernetes/OpenShift cluster

netapp.storagegrid
~~~~~~~~~~~~~~~~~~

- netapp.storagegrid.na_sg_grid_ha_group - Manage high availability (HA) group configuration on StorageGRID.
- netapp.storagegrid.na_sg_grid_traffic_classes - Manage Traffic Classification Policy configuration on StorageGRID.

Unchanged Collections
---------------------

- ansible.posix (still version 1.3.0)
- ansible.utils (still version 2.5.2)
- ansible.windows (still version 1.9.0)
- arista.eos (still version 3.1.0)
- awx.awx (still version 19.4.0)
- check_point.mgmt (still version 2.3.0)
- chocolatey.chocolatey (still version 1.2.0)
- cisco.asa (still version 2.1.0)
- cisco.intersight (still version 1.0.18)
- cisco.ise (still version 1.2.1)
- cisco.nso (still version 1.0.3)
- cloud.common (still version 2.1.0)
- community.azure (still version 1.1.0)
- community.ciscosmb (still version 1.0.4)
- community.fortios (still version 1.0.0)
- community.google (still version 1.0.0)
- community.grafana (still version 1.3.3)
- community.kubernetes (still version 2.0.1)
- community.kubevirt (still version 1.0.0)
- community.libvirt (still version 1.0.2)
- community.mysql (still version 2.3.5)
- community.network (still version 3.1.0)
- community.okd (still version 2.1.0)
- community.postgresql (still version 1.7.1)
- community.proxysql (still version 1.3.1)
- community.rabbitmq (still version 1.1.0)
- community.routeros (still version 2.0.0)
- community.skydive (still version 1.0.0)
- community.windows (still version 1.9.0)
- community.zabbix (still version 1.5.1)
- cyberark.conjur (still version 1.1.0)
- cyberark.pas (still version 1.0.13)
- dellemc.enterprise_sonic (still version 1.1.0)
- dellemc.openmanage (still version 4.4.0)
- dellemc.os10 (still version 1.1.1)
- dellemc.os6 (still version 1.0.7)
- dellemc.os9 (still version 1.0.4)
- f5networks.f5_modules (still version 1.15.0)
- fortinet.fortimanager (still version 2.1.4)
- fortinet.fortios (still version 2.1.4)
- frr.frr (still version 1.0.3)
- gluster.gluster (still version 1.0.2)
- google.cloud (still version 1.0.2)
- hetzner.hcloud (still version 1.6.0)
- hpe.nimble (still version 1.1.4)
- ibm.qradar (still version 1.0.3)
- infinidat.infinibox (still version 1.3.3)
- infoblox.nios_modules (still version 1.2.1)
- inspur.sm (still version 1.3.0)
- mellanox.onyx (still version 1.0.0)
- netapp.aws (still version 21.7.0)
- netapp.azure (still version 21.10.0)
- netapp.cloudmanager (still version 21.15.0)
- netapp.elementsw (still version 21.7.0)
- netapp.ontap (still version 21.17.3)
- netapp.um_info (still version 21.8.0)
- netbox.netbox (still version 3.6.0)
- ngine_io.cloudstack (still version 2.2.3)
- ngine_io.exoscale (still version 1.0.0)
- openstack.cloud (still version 1.7.2)
- openvswitch.openvswitch (still version 2.1.0)
- ovirt.ovirt (still version 1.6.6)
- purestorage.flasharray (still version 1.12.1)
- purestorage.flashblade (still version 1.9.0)
- sensu.sensu_go (still version 1.13.0)
- servicenow.servicenow (still version 1.0.6)
- splunk.es (still version 1.0.2)
- theforeman.foreman (still version 2.2.0)
- vyos.vyos (still version 2.8.0)
- wti.remote (still version 1.0.3)

v5.5.0
======

.. contents::
  :local:
  :depth: 2

Release Summary
---------------

Release Date: 2022-03-15

`Porting Guide <https://docs.ansible.com/ansible/devel/porting_guides.html>`_

Ansible-core
------------

Ansible 5.5.0 contains Ansible-core version 2.12.3.
This is a newer version than version 2.12.2 contained in the previous Ansible release.

The changes are reported in the combined changelog below.

Changed Collections
-------------------

If not mentioned explicitly, the changes are reported in the combined changelog below.

+-----------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| Collection            | Ansible 5.4.0 | Ansible 5.5.0 | Notes                                                                                                                        |
+=======================+===============+===============+==============================================================================================================================+
| ansible.utils         | 2.5.0         | 2.5.2         |                                                                                                                              |
+-----------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| check_point.mgmt      | 2.2.2         | 2.3.0         | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+-----------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.ios             | 2.7.1         | 2.8.0         |                                                                                                                              |
+-----------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.iosxr           | 2.7.0         | 2.8.1         |                                                                                                                              |
+-----------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.ucs             | 1.6.0         | 1.7.0         | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+-----------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.crypto      | 2.2.2         | 2.2.3         |                                                                                                                              |
+-----------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.dns         | 2.0.7         | 2.0.8         |                                                                                                                              |
+-----------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.docker      | 2.2.0         | 2.2.1         |                                                                                                                              |
+-----------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.general     | 4.5.0         | 4.6.0         |                                                                                                                              |
+-----------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.grafana     | 1.3.2         | 1.3.3         |                                                                                                                              |
+-----------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.mysql       | 2.3.4         | 2.3.5         |                                                                                                                              |
+-----------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.network     | 3.0.0         | 3.1.0         |                                                                                                                              |
+-----------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.postgresql  | 1.7.0         | 1.7.1         |                                                                                                                              |
+-----------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| f5networks.f5_modules | 1.14.0        | 1.15.0        |                                                                                                                              |
+-----------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| netapp.cloudmanager   | 21.14.0       | 21.15.0       |                                                                                                                              |
+-----------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| netapp.ontap          | 21.16.0       | 21.17.3       |                                                                                                                              |
+-----------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| netbox.netbox         | 3.5.1         | 3.6.0         |                                                                                                                              |
+-----------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| openstack.cloud       | 1.7.0         | 1.7.2         | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+-----------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| vyos.vyos             | 2.7.0         | 2.8.0         |                                                                                                                              |
+-----------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+

Minor Changes
-------------

Ansible-core
~~~~~~~~~~~~

- The collection loader now reports a Python warning if an attempt is made to install the Ansible collection loader a second time. Previously this condition was reported using an Ansible warning.
- ansible-test - Installation of ``cryptography`` is no longer version constrained when ``openssl`` 1.1.0 or later is installed.
- ansible-test - Requirements for the plugin import test are now frozen.
- ansible-test - The ``pip`` and ``wheel`` packages are removed from all sanity test virtual environments after installation completes to reduce their size. Previously they were only removed from the environments used for the ``import`` sanity test.
- ansible-test - The hash for all managed sanity test virtual environments has changed. Containers that include ``ansible-test sanity --prime-venvs`` will need to be rebuilt to continue using primed virtual environments.
- ansible-test - Update ``pip`` used to bootstrap remote FreeBSD instances from version 20.3.4 to 21.3.1.
- ansible-test - Update the ``alpine`` container to version 3.3.0. This updates the base image from 3.14.2 to 3.15.0, which includes support for installing binary wheels using pip.
- ansible-test - Update the ``galaxy`` test plugin to get its container from a copy on quay.io.
- ansible-test - Update the ``openshift`` test plugin to get its container from a copy on quay.io.
- junit callback - Add support for replacing the directory portion of out-of-tree relative task paths with a placeholder.

cisco.ios
~~~~~~~~~

- `ios_bgp_global` - Deprecate aggregate_address with aggregate_address which supports list of dict attributes.
- `ios_bgp_global` - Deprecate bestpath with bestpath_options which supports a dict attribute.
- `ios_bgp_global` - Deprecate distribute_list with distributes which supports list of dict attributes.
- `ios_bgp_global` - Deprecate inject_map with inject_maps which supports list of dict attributes.
- `ios_bgp_global` - Deprecate listen.ipv4_with_subnet/ipv6_with_subnet with host_with_subnet which enables common attribute for facts rendering.
- `ios_bgp_global` - Deprecate neighbors.address/tag/ipv6_adddress with neighbor_address which enables common attribute for facts rendering.
- `ios_bgp_global` - Deprecate neighbors.password with password_options which allows encryption and password.
- `ios_bgp_global` - Deprecate neighbors.route_map with route_maps which supports list of dict attributes.
- `ios_bgp_global` - Deprecate nopeerup_delay with nopeerup_delay_options which supports a dict attribute.
- `ios_bgp_global` - Deprecates route_server_context, scope, template as they were not implemented with the scope of the module.

cisco.iosxr
~~~~~~~~~~~

- Add commit_confirmed functionality in IOSXR.
- Add disable_default_comment option to disable default comment in iosxr_config module.

community.general
~~~~~~~~~~~~~~~~~

- jira - when creating a comment, ``fields`` now is used for additional data (https://github.com/ansible-collections/community.general/pull/4304).
- ldap_entry - add support for recursive deletion (https://github.com/ansible-collections/community.general/issues/3613).
- mksysb - revamped the module using ``ModuleHelper`` (https://github.com/ansible-collections/community.general/pull/3295).
- nmcli - add missing connection aliases ``802-3-ethernet`` and ``802-11-wireless`` (https://github.com/ansible-collections/community.general/pull/4108).
- nmcli - remove nmcli modify dependency on ``type`` parameter (https://github.com/ansible-collections/community.general/issues/2858).
- npm - add ability to use ``production`` flag when ``ci`` is set (https://github.com/ansible-collections/community.general/pull/4299).
- pacman - add ``remove_nosave`` parameter to avoid saving modified configuration files as ``.pacsave`` files. (https://github.com/ansible-collections/community.general/pull/4316, https://github.com/ansible-collections/community.general/issues/4315).
- pacman - now implements proper change detection for ``update_cache=true``. Adds ``cache_updated`` return value to when ``update_cache=true`` to report this result independently of the module's overall changed return value (https://github.com/ansible-collections/community.general/pull/4337).
- pipx - added options ``editable`` and ``pip_args`` (https://github.com/ansible-collections/community.general/issues/4300).
- proxmox inventory plugin - add support for client-side jinja filters (https://github.com/ansible-collections/community.general/issues/3553).
- redis - add authentication parameters ``login_user``, ``tls``, ``validate_certs``, and ``ca_certs`` (https://github.com/ansible-collections/community.general/pull/4207).
- syslog_json - add option to skip logging of ``gather_facts`` playbook tasks; use v2 callback API (https://github.com/ansible-collections/community.general/pull/4223).
- zypper - add support for ``--clean-deps`` option to remove packages that depend on a package being removed (https://github.com/ansible-collections/community.general/pull/4195).

community.network
~~~~~~~~~~~~~~~~~

- community.network.ce_switchport - add support of decode a few stdout values from bitmap to human readable format(https://github.com/ansible-collections/community.network/issues/315)
- community.network.edgeos_config - append save command into result (https://github.com/ansible-collections/community.network/pull/189)

f5networks.f5_modules
~~~~~~~~~~~~~~~~~~~~~

- bigip_device_info - Added a new meta choice, packages, which groups information about as3, do, cfe and ts. This change was done to ensure users with non admin access can use this module to get information that does not require admin access.
- bigip_device_info - this module can gather information about ucs backup files.
- bigip_pool_member - add checkmode bypass so that existence checks for pool is always returns true when using check mode
- bigip_profile_http_compression - Add content_type_include parameter to bigip_profile_fastl4 module

netapp.cloudmanager
~~~~~~~~~~~~~~~~~~~

- Add the description of client_id based on the cloudmanager UI.
- Set license_type default value 'capacity-paygo' for single node 'ha-capacity-paygo' for HA and 'capacity_package_name' value 'Essential'

netapp.ontap
~~~~~~~~~~~~

- all modules that only support ZAPI - warn when ``use_rest`` with a value of ``always`` is ignored.
- na_ontap_cifs_acl - Added REST support to the cifs share access control module.
- na_ontap_cifs_acl - new option ``type`` for user-group-type.
- na_ontap_cifs_share - Added REST support to the cifs share module.
- na_ontap_cluster_peer - Added REST support to the cluster_peer module.
- na_ontap_lun_map - Added REST support.
- na_ontap_nfs - Added Rest Support
- na_ontap_volume_clone - Added REST support.

netbox.netbox
~~~~~~~~~~~~~

- Add custom fields to modules missing it [#723](https://github.com/netbox-community/ansible_modules/pull/723)
- Add tags to modules missing it [#725](https://github.com/netbox-community/ansible_modules/pull/725)
- nb_inventory - Add a racks option [#701](https://github.com/netbox-community/ansible_modules/pull/701)
- netbox_custom_field - Add module [#719](https://github.com/netbox-community/ansible_modules/pull/719)
- netbox_custom_link - Add module [#722](https://github.com/netbox-community/ansible_modules/pull/722)
- netbox_device_interface, netbox_vm_interface - Add bridge to netbox_device_interface and netbox_vm_interface [#713](https://github.com/netbox-community/ansible_modules/pull/713)
- netbox_export_template - Add module [#727](https://github.com/netbox-community/ansible_modules/pull/727)
- netbox_service - Add virtual_machine as an allowed query parameter for ipaddresses [#718](https://github.com/netbox-community/ansible_modules/pull/718)
- netbox_webhook - Add module [#738](https://github.com/netbox-community/ansible_modules/pull/738)

vyos.vyos
~~~~~~~~~

- Add vyos_hostname resource module.
- Rename V4-EGRESS/V6-EGRESS to EGRESS in the tests to test the same-name situation
- Update vyos_facts to support IPv4 and IPv6 rule sets having the same name
- Update vyos_firewall_rules to support IPv4 and IPv6 rule sets having the same name
- vyos_firewall_rules - Add support for log enable on individual rules
- vyos_firewall_rules - fixed incorrect option 'disabled' passed to the rules.

Deprecated Features
-------------------

community.general
~~~~~~~~~~~~~~~~~

- pacman - from community.general 5.0.0 on, the ``changed`` status of ``update_cache`` will no longer be ignored if ``name`` or ``upgrade`` is specified. To keep the old behavior, add something like ``register: result`` and ``changed_when: result.packages | length > 0`` to your task (https://github.com/ansible-collections/community.general/pull/4329).

Bugfixes
--------

Ansible-core
~~~~~~~~~~~~

- ansible-test - All virtual environments managed by ansible-test are marked as usable after being bootstrapped, to avoid errors caused by use of incomplete environments. Previously this was only done for sanity tests. Existing environments from previous versions of ansible-test will be recreated on demand due to lacking the new marker.
- ansible-test - Fix the ``validate-modules`` sanity test to avoid double-loading the collection loader and possibly failing on import of the ``packaging`` module.
- ansible-test - Import ``yaml.cyaml.CParser`` instead of ``_yaml.CParser`` in the ``yamllint`` sanity test.
- ansible-test - Replace the directory portion of out-of-tree paths in JUnit files from integration tests with the ``out-of-tree:`` prefix.
- ansible-test - Sanity tests run with the ``--requirements` option for Python 2.x now install ``virtualenv`` when it is missing or too old. Previously it was only installed if missing. Version 16.7.12 is now installed instead of the latest version on Python 2.7.
- ansible-test - The ``import`` sanity test no longer reports errors about ``packaging`` being missing when testing collections.
- ansible-test - Update the ``default`` containers to version 4.2.0.
- ansible-test - Use https://ci-files.testing.ansible.com/ for instance bootstrapping instead of an S3 endpoint.
- ansible-test - Use relative paths in JUnit files generated during integration test runs.
- ansible-test - Virtual environments managed by ansible-test now use consistent versions of ``pip``, ``setuptools`` and ``wheel``. This avoids issues with virtual environments containing outdated or dysfunctional versions of these tools. The initial bootstrapping of ``pip`` is done by ansible-test from an HTTPS endpoint instead of creating the virtual environment with it already present.
- cleaning facts will now only warn about the variable name and not post the content, which can be undesireable to disclose
- correctly inherit vars from parent in block (https://github.com/ansible/ansible/issues/75286).
- gather_facts action now handles the move of base connection plugin types into collections to add/prevent subset argument correctly
- junit callback - Fix traceback during automatic fact gathering when using relative paths.
- junit callback - Fix unicode error when handling non-ASCII task paths.
- ssh connection now uses more correct host source as play_context can ignore loop/delegation variations.
- task_executor reverts the change to push facts into delegated vars on loop finalization as result managing code already handles this and was duplicating effort to wrong result.
- template lookup - restore inadvertently deleted default for ``convert_data`` (https://github.com/ansible/ansible/issues/77004)
- unarchive - Make extraction work when the LANGUAGE environment variable is set to a non-English locale.

ansible.utils
~~~~~~~~~~~~~

- Fix issue in ipaddr,ipv4,ipv6,ipwrap filters.(https://github.com/ansible-collections/ansible.utils/issues/148).
- ipaddr - Add valid network for link-local (https://github.com/ansible-collections/ansible.netcommon/issues/350).
- ipaddr - Fix issue of breaking ipaddr filter with netcommon 2.6.0(https://github.com/ansible-collections/ansible.netcommon/issues/375).

cisco.ios
~~~~~~~~~

- 'ios_acls'- filters out dynamically generated reflexive type acls.
- `ios_bgp_global` - Added bmp.server_options.
- `ios_bgp_global` - Added capability of configure network options.
- `ios_bgp_global` - Added community and local_preference for route_reflector_client.
- `ios_bgp_global` - Added update_source for neighbors.
- `ios_bgp_global` - Correct misspelled attributes with alternates/alias.
- `ios_bgp_global` - Facts and config code optimized for using rm_templates.
- `ios_bgp_global` - Parsers added for non-implemented attributes.
- `ios_bgp_global` - client_to_client.cluster_id corrected to take string input.
- `ios_bgp_global` - neighbors.path_attribute to support float format.
- `ios_static_routes` - Consider only config containing routes to render facts.

cisco.iosxr
~~~~~~~~~~~

- `iosxr_acls` - fix acl for parsing wrong command on ( num matches ) data

community.crypto
~~~~~~~~~~~~~~~~

- luks_device - fix parsing of ``lsblk`` output when device name ends with ``crypt`` (https://github.com/ansible-collections/community.crypto/issues/409, https://github.com/ansible-collections/community.crypto/pull/410).

community.dns
~~~~~~~~~~~~~

- Update Public Suffix List.

community.docker
~~~~~~~~~~~~~~~~

- docker_compose - fix Python 3 type error when extracting warnings or errors from docker-compose's output (https://github.com/ansible-collections/community.docker/pull/305).

community.general
~~~~~~~~~~~~~~~~~

- filesize - add support for busybox dd implementation, that is used by default on Alpine linux (https://github.com/ansible-collections/community.general/pull/4288, https://github.com/ansible-collections/community.general/issues/4259).
- linode inventory plugin - fix configuration handling relating to inventory filtering (https://github.com/ansible-collections/community.general/pull/4336).
- mksysb - fixed bug for parameter ``backup_dmapi_fs`` was passing the wrong CLI argument (https://github.com/ansible-collections/community.general/pull/3295).
- pacman - Use ``--groups`` instead of ``--group`` (https://github.com/ansible-collections/community.general/pull/4312).
- pacman - fix URL based package installation (https://github.com/ansible-collections/community.general/pull/4286, https://github.com/ansible-collections/community.general/issues/4285).
- pacman - fix ``upgrade=yes`` (https://github.com/ansible-collections/community.general/pull/4275, https://github.com/ansible-collections/community.general/issues/4274).
- pacman - make sure that ``packages`` is always returned when ``name`` or ``upgrade`` is specified, also if nothing is done (https://github.com/ansible-collections/community.general/pull/4329).
- pacman - when the ``update_cache`` option is combined with another option such as ``upgrade``, report ``changed`` based on the actions performed by the latter option. This was the behavior in community.general 4.4.0 and before. In community.general 4.5.0, a task combining these options would always report ``changed`` (https://github.com/ansible-collections/community.general/pull/4318).
- proxmox inventory plugin - always convert strings that follow the ``key=value[,key=value[...]]`` form into dictionaries (https://github.com/ansible-collections/community.general/pull/4349).
- proxmox inventory plugin - fixed the ``description`` field being ignored if it contained a comma (https://github.com/ansible-collections/community.general/issues/4348).
- proxmox_kvm - fix error in check when creating or cloning (https://github.com/ansible-collections/community.general/pull/4306).
- proxmox_kvm - fix error when checking whether Proxmox VM exists (https://github.com/ansible-collections/community.general/pull/4287).
- terraform - fix ``variable`` handling to allow complex values (https://github.com/ansible-collections/community.general/pull/4281).

community.grafana
~~~~~~~~~~~~~~~~~

- Fix an issue with grafana_datasource for Prometheus with basic auth credential management. (#204)

community.mysql
~~~~~~~~~~~~~~~

- Collection core functions - fixes related to the mysqlclient Python connector (https://github.com/ansible-collections/community.mysql/issues/292).

community.network
~~~~~~~~~~~~~~~~~

- ce - Modify the bug in the query configuration method (https://github.com/ansible-collections/community.network/pull/56).
- community.network.ce_switchport - fix error causing by ``KeyError:`` ``host`` due to properties aren't used anywhere (https://github.com/ansible-collections/community.network/issues/313)
- exos_config - fix a hang due to an unexpected prompt during save_when (https://github.com/ansible-collections/community.network/pull/110).
- weos4 cliconf plugin - fix linting errors in documentation data (https://github.com/ansible-collections/community.network/pull/368).

community.postgresql
~~~~~~~~~~~~~~~~~~~~

- module core functions - get rid of the deprecated psycopg2 connection alias ``database`` in favor of ``dbname`` when psycopg2 is 2.7+ (https://github.com/ansible-collections/community.postgresql/pull/196).
- postgresql_query - cannot handle .sql file with \\n at end of file (https://github.com/ansible-collections/community.postgresql/issues/180).

f5networks.f5_modules
~~~~~~~~~~~~~~~~~~~~~

- bigip_device_info - fixed bug regarding handling of negated meta options.
- bigip_device_license - fixed issue that resulted in only first of the multiple add-on keys getting added to the device.
- bigip_firewall_address_list - fixed issue where addresses that contained RD would cause an error.
- bigip_gtm_wide_ip - fixed a bug that prevented creation of gtm wide ips in disabled state.

netapp.ontap
~~~~~~~~~~~~

- na_ontap_aggregate - Fixed UUID issue when attempting to attach object store as part of creating the aggregate with REST.
- na_ontap_cifs_server -  error out if ZAPI only options ``force`` or ``workgroup`` are used with REST.
- na_ontap_cluster_peer - Fixed KeyError if both ``source_intercluster_lifs`` and ``dest_intercluster_lifs`` not present in cluster create.
- na_ontap_lun_map - Fixed bug when deleting lun map using REST.
- na_ontap_lun_map - fixed bugs resulting in REST support to not work.
- na_ontap_rest_info - Fixed an issues with adding field to specific info that didn't have a direct REST equivalent.
- na_ontap_rest_info - Fixed example with wrong indentation for ``use_python_keys``.

netbox.netbox
~~~~~~~~~~~~~

- Config Context is now able to be added to cluster [#715](https://github.com/netbox-community/ansible_modules/pull/715)
- Ensure proper filtering for VLAN group [#741](https://github.com/netbox-community/ansible_modules/pull/741)
- Fix prefixes option in nb_inventory to ensure all prefixes are returned [#742](https://github.com/netbox-community/ansible_modules/pull/742)
- Make sure API calls on versions without the /api/status endpoint [#707](https://github.com/netbox-community/ansible_modules/pull/707)

Known Issues
------------

community.general
~~~~~~~~~~~~~~~~~

- pacman - ``update_cache`` cannot differentiate between up to date and outdated package lists and will report ``changed`` in both situations (https://github.com/ansible-collections/community.general/pull/4318).
- pacman - binaries specified in the ``executable`` parameter must support ``--print-format`` in order to be used by this module. In particular, AUR helper ``yay`` is known not to currently support it (https://github.com/ansible-collections/community.general/pull/4312).

New Modules
-----------

netbox.netbox
~~~~~~~~~~~~~

- netbox.netbox.netbox_custom_field - Create, update or delete Custom fields in NetBox
- netbox.netbox.netbox_custom_link - Create, update or delete Custom links in NetBox
- netbox.netbox.netbox_export_template - Create, update or delete Export templates in NetBox
- netbox.netbox.netbox_webhook - Create, update or delete Webhooks in NetBox

vyos.vyos
~~~~~~~~~

- vyos.vyos.vyos_hostname - Manages hostname resource module

Unchanged Collections
---------------------

- amazon.aws (still version 2.1.0)
- ansible.netcommon (still version 2.5.1)
- ansible.posix (still version 1.3.0)
- ansible.windows (still version 1.9.0)
- arista.eos (still version 3.1.0)
- awx.awx (still version 19.4.0)
- azure.azcollection (still version 1.11.0)
- chocolatey.chocolatey (still version 1.2.0)
- cisco.aci (still version 2.1.0)
- cisco.asa (still version 2.1.0)
- cisco.intersight (still version 1.0.18)
- cisco.ise (still version 1.2.1)
- cisco.meraki (still version 2.6.0)
- cisco.mso (still version 1.3.0)
- cisco.nso (still version 1.0.3)
- cisco.nxos (still version 2.9.0)
- cloud.common (still version 2.1.0)
- cloudscale_ch.cloud (still version 2.2.0)
- community.aws (still version 2.3.0)
- community.azure (still version 1.1.0)
- community.ciscosmb (still version 1.0.4)
- community.digitalocean (still version 1.15.1)
- community.fortios (still version 1.0.0)
- community.google (still version 1.0.0)
- community.hashi_vault (still version 2.3.0)
- community.hrobot (still version 1.2.2)
- community.kubernetes (still version 2.0.1)
- community.kubevirt (still version 1.0.0)
- community.libvirt (still version 1.0.2)
- community.mongodb (still version 1.3.2)
- community.okd (still version 2.1.0)
- community.proxysql (still version 1.3.1)
- community.rabbitmq (still version 1.1.0)
- community.routeros (still version 2.0.0)
- community.skydive (still version 1.0.0)
- community.sops (still version 1.2.0)
- community.vmware (still version 1.17.1)
- community.windows (still version 1.9.0)
- community.zabbix (still version 1.5.1)
- containers.podman (still version 1.9.1)
- cyberark.conjur (still version 1.1.0)
- cyberark.pas (still version 1.0.13)
- dellemc.enterprise_sonic (still version 1.1.0)
- dellemc.openmanage (still version 4.4.0)
- dellemc.os10 (still version 1.1.1)
- dellemc.os6 (still version 1.0.7)
- dellemc.os9 (still version 1.0.4)
- fortinet.fortimanager (still version 2.1.4)
- fortinet.fortios (still version 2.1.4)
- frr.frr (still version 1.0.3)
- gluster.gluster (still version 1.0.2)
- google.cloud (still version 1.0.2)
- hetzner.hcloud (still version 1.6.0)
- hpe.nimble (still version 1.1.4)
- ibm.qradar (still version 1.0.3)
- infinidat.infinibox (still version 1.3.3)
- infoblox.nios_modules (still version 1.2.1)
- inspur.sm (still version 1.3.0)
- junipernetworks.junos (still version 2.9.0)
- kubernetes.core (still version 2.2.3)
- mellanox.onyx (still version 1.0.0)
- netapp.aws (still version 21.7.0)
- netapp.azure (still version 21.10.0)
- netapp.elementsw (still version 21.7.0)
- netapp.storagegrid (still version 21.9.0)
- netapp.um_info (still version 21.8.0)
- netapp_eseries.santricity (still version 1.2.13)
- ngine_io.cloudstack (still version 2.2.3)
- ngine_io.exoscale (still version 1.0.0)
- ngine_io.vultr (still version 1.1.0)
- openvswitch.openvswitch (still version 2.1.0)
- ovirt.ovirt (still version 1.6.6)
- purestorage.flasharray (still version 1.12.1)
- purestorage.flashblade (still version 1.9.0)
- sensu.sensu_go (still version 1.13.0)
- servicenow.servicenow (still version 1.0.6)
- splunk.es (still version 1.0.2)
- t_systems_mms.icinga_director (still version 1.27.1)
- theforeman.foreman (still version 2.2.0)
- wti.remote (still version 1.0.3)

v5.4.0
======

.. contents::
  :local:
  :depth: 2

Release Summary
---------------

Release Date: 2022-02-22

`Porting Guide <https://docs.ansible.com/ansible/devel/porting_guides.html>`_

Ansible-core
------------

Ansible 5.4.0 contains Ansible-core version 2.12.2.
This is the same version of Ansible-core as in the previous Ansible release.


Changed Collections
-------------------

If not mentioned explicitly, the changes are reported in the combined changelog below.

+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| Collection                    | Ansible 5.3.0 | Ansible 5.4.0 | Notes                                                                                                                        |
+===============================+===============+===============+==============================================================================================================================+
| ansible.netcommon             | 2.5.0         | 2.5.1         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| ansible.utils                 | 2.4.3         | 2.5.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| chocolatey.chocolatey         | 1.1.0         | 1.2.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.ios                     | 2.6.0         | 2.7.1         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.iosxr                   | 2.6.0         | 2.7.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.nxos                    | 2.8.2         | 2.9.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.aws                 | 2.2.0         | 2.3.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.crypto              | 2.2.0         | 2.2.2         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.digitalocean        | 1.15.0        | 1.15.1        |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.dns                 | 2.0.6         | 2.0.7         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.docker              | 2.1.1         | 2.2.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.general             | 4.4.0         | 4.5.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.grafana             | 1.3.0         | 1.3.2         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.hashi_vault         | 2.2.0         | 2.3.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.mysql               | 2.3.3         | 2.3.4         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.postgresql          | 1.6.1         | 1.7.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| fortinet.fortios              | 2.1.3         | 2.1.4         | There are no changes recorded in the changelog.                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| junipernetworks.junos         | 2.8.0         | 2.9.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| netapp.cloudmanager           | 21.13.0       | 21.14.0       |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| netapp.ontap                  | 21.15.1       | 21.16.0       |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| ngine_io.cloudstack           | 2.2.2         | 2.2.3         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| openstack.cloud               | 1.6.0         | 1.7.0         | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| t_systems_mms.icinga_director | 1.27.0        | 1.27.1        |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| vyos.vyos                     | 2.6.0         | 2.7.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+

Major Changes
-------------

chocolatey.chocolatey
~~~~~~~~~~~~~~~~~~~~~

- win_chocolatey - Added choco_args option to pass additional arguments directly to Chocolatey.

vyos.vyos
~~~~~~~~~

- Add 'pool' as value to server key in ntp_global.

Minor Changes
-------------

ansible.utils
~~~~~~~~~~~~~

- 'keep_keys' filter plugin added.
- 'remove_keys' filter plugin added.
- 'replace_keys' filter plugin added.
- Add cli_merge ipaddr filter plugin.
- Add ip4_hex filter plugin.
- Add ipaddr filter plugin.
- Add ipmath filter plugin.
- Add ipsubnet filter plugin.
- Add ipv4 filter plugin.
- Add ipv6 filter plugin.
- Add ipwrap filter plugin.
- Add network_in_network filter plugin.
- Add network_in_usable filter plugin.
- Add next_nth_usable filter plugin.
- Add nthhost filter plugin.
- Add previous_nth_usable filter plugin.
- Add reduce_on_network filter plugin.
- Add slaac,hwaddr,mac filter plugin.
- New validate sub-plugin "config" to validate device configuration against user-defined rules (https://github.com/ansible-collections/ansible.network/issues/15).

chocolatey.chocolatey
~~~~~~~~~~~~~~~~~~~~~

- All modules - Ported away from the Ansible.Legacy format, using Ansible.Basic.Module instead.
- win_chocolatey - Added state: upgrade as an alias for state: latest.
- win_chocolatey - Improved automatic URL handling for getting the install.ps1 script from a custom source URL.
- win_chocolatey - Improved handling of Chocolatey bootstrapping installation script.
- win_chocolatey - Removed warning for installing Chocolatey if when specifically installing it with `name: chocolatey`.

cisco.ios
~~~~~~~~~

- `ios_acls` - Added enable_fragment attribute to enable fragments under ace.
- `ios_hostname` - New Resource module added.
- `ios_snmp_server` - Enables configuration of v3 auth and encryption password for each user.

cisco.iosxr
~~~~~~~~~~~

- `iosxr_hostname` - New Resource module added.

cisco.nxos
~~~~~~~~~~

- Add nxos_hostname resource module.

community.aws
~~~~~~~~~~~~~

- elb_instance - `wait` parameter is no longer ignored (https://github.com/ansible-collections/community.aws/pull/826)

community.digitalocean
~~~~~~~~~~~~~~~~~~~~~~

- Updates DigitalOcean API documentation links to current domain with working URL anchors (https://github.com/ansible-collections/community.digitalocean/issues/223).

community.docker
~~~~~~~~~~~~~~~~

- docker_config - add support for rolling update, set ``rolling_versions`` to ``true`` to enable (https://github.com/ansible-collections/community.docker/pull/295, https://github.com/ansible-collections/community.docker/issues/109).
- docker_secret - add support for rolling update, set ``rolling_versions`` to ``true`` to enable (https://github.com/ansible-collections/community.docker/pull/293, https://github.com/ansible-collections/community.docker/issues/21).
- docker_swarm_service - add support for setting capabilities with the ``cap_add`` and ``cap_drop`` parameters. Usage is the same as with the ``capabilities`` and ``cap_drop`` parameters for ``docker_container`` (https://github.com/ansible-collections/community.docker/pull/294).

community.general
~~~~~~~~~~~~~~~~~

- Avoid internal ansible-core module_utils in favor of equivalent public API available since at least Ansible 2.9. This fixes some instances added since the last time this was fixed (https://github.com/ansible-collections/community.general/pull/4232).
- ansible_galaxy_install - added option ``no_deps`` to the module (https://github.com/ansible-collections/community.general/issues/4174).
- gitlab_group_variable - new ``variables`` parameter (https://github.com/ansible-collections/community.general/pull/4038 and https://github.com/ansible-collections/community.general/issues/4074).
- keycloak_* modules - added connection timeout parameter when calling server (https://github.com/ansible-collections/community.general/pull/4168).
- linode inventory plugin - add support for caching inventory results (https://github.com/ansible-collections/community.general/pull/4179).
- opentelemetry_plugin - enrich service when using the ``jenkins``, ``hetzner`` or ``jira`` modules (https://github.com/ansible-collections/community.general/pull/4105).
- pacman - the module has been rewritten and is now much faster when using ``state=latest``. Operations are now done all packages at once instead of package per package and the configured output format of ``pacman`` no longer affect the module's operation. (https://github.com/ansible-collections/community.general/pull/3907, https://github.com/ansible-collections/community.general/issues/3783, https://github.com/ansible-collections/community.general/issues/4079)
- passwordstore lookup plugin - add configurable ``lock`` and ``locktimeout`` options to avoid race conditions in itself and in the ``pass`` utility it calls. By default, the plugin now locks on write operations (https://github.com/ansible-collections/community.general/pull/4194).
- proxmox modules - move common code into ``module_utils`` (https://github.com/ansible-collections/community.general/pull/4029).
- proxmox_kvm - added EFI disk support when creating VM with OVMF UEFI BIOS with new ``efidisk0`` option (https://github.com/ansible-collections/community.general/pull/4106, https://github.com/ansible-collections/community.general/issues/1638).
- proxmox_kwm - add ``win11`` to ``ostype`` parameter for Windows 11 and Windows Server 2022 support (https://github.com/ansible-collections/community.general/issues/4023, https://github.com/ansible-collections/community.general/pull/4191).

community.grafana
~~~~~~~~~~~~~~~~~

- community.grafana.grafana_datasource supports aws_auth_type of default.

community.postgresql
~~~~~~~~~~~~~~~~~~~~

- postgresql_ping - add the ``conn_err_msg`` return value (https://github.com/ansible-collections/community.postgresql/pull/177).

junipernetworks.junos
~~~~~~~~~~~~~~~~~~~~~

- Add junos_hostname resource module.
- Allow interfaces resource module to configure and gather logical interface description.

netapp.cloudmanager
~~~~~~~~~~~~~~~~~~~

- na_cloudmanager_snapmirror - Add FSX to snapmirror.

netapp.ontap
~~~~~~~~~~~~

- na_ontap_aggregate - Added REST support.
- na_ontap_aggregate - Added ``disk_class`` option for REST and ZAPI.
- na_ontap_aggregate - Extended accepted ``disk_type`` values for ZAPI.
- na_ontap_cifs_server - Added REST support to the cifs server module.
- na_ontap_ports - Added REST support to the ports module.
- na_ontap_snapmirror - Added REST support to the na_ontap_snapmirror module
- na_ontap_volume - ``logical_space_enforcement`` to specifies whether to perform logical space accounting on the volume.
- na_ontap_volume - ``logical_space_reporting`` to specifies whether to report space logically on the volume.
- na_ontap_volume - ``tiering_minimum_cooling_days`` to specify how many days must pass before inactive data in a volume using the Auto or Snapshot-Only policy is considered cold and eligible for tiering.
- na_ontap_volume_clone - Added REST support.

vyos.vyos
~~~~~~~~~

- Add vyos_snmp_server resource module.

Deprecated Features
-------------------

cisco.ios
~~~~~~~~~

- `ios_acls` - Deprecated fragment attribute added boolean alternate as enable_fragment.

Bugfixes
--------

ansible.netcommon
~~~~~~~~~~~~~~~~~

- Fixed plugins inheriting from netcommon's base plugins (for example httpapi/restconf or netconf/default) so that they can be properly loaded (https://github.com/ansible-collections/ansible.netcommon/issues/356).

cisco.ios
~~~~~~~~~

- `ios_acls` - Fixes protocol_options not rendering command properly when range is specified.
- `ios_acls` - Fixes standard acls getting wrongly parsed in v2.6.0
- `ios_l2_interfaces` - fix unable to identify FiveGigabitEthernet names on facts gathering.
- `ios_snmp_server` - Change key from `users` to `views` in rm template to fix failure when collecting snmp server facts from devices that have a view defined in the configuration (https://github.com/ansible-collections/cisco.ios/issues/491).
- `ios_static_routes` - Fixes static routes unable to identify interface names when supplied with destination attribute.
- `ios_vlans` - fix parsing of VLAN names with spaces.
- `ios_vlans` - fix parsing of VLAN ranges under remote span.

cisco.nxos
~~~~~~~~~~

- `nxos_bgp_address_family` -  Add hmm as valid option for redistribute protocol (https://github.com/ansible-collections/cisco.nxos/issues/385).
- `nxos_snmp_server` - Fix rendering context command (https://github.com/ansible-collections/cisco.nxos/issues/406).

community.aws
~~~~~~~~~~~~~

- cloudfront_distribution - Dont pass ``s3_origin_access_identity_enabled`` to API request (https://github.com/ansible-collections/community.aws/pull/881).
- execute_lambda - Wait for Lambda function State = Active before executing (https://github.com/ansible-collections/community.aws/pull/857)
- lambda - Wait for Lambda function State = Active & LastUpdateStatus = Successful before updating (https://github.com/ansible-collections/community.aws/pull/857)

community.crypto
~~~~~~~~~~~~~~~~

- certificate_complete_chain - allow multiple potential intermediate certificates to have the same subject (https://github.com/ansible-collections/community.crypto/issues/399, https://github.com/ansible-collections/community.crypto/pull/403).
- openssh_cert - fixed false ``changed`` status for ``host`` certificates when using ``full_idempotence`` (https://github.com/ansible-collections/community.crypto/issues/395, https://github.com/ansible-collections/community.crypto/pull/396).
- x509_certificate - for the ``ownca`` provider, check whether the CA private key actually belongs to the CA certificate (https://github.com/ansible-collections/community.crypto/pull/407).
- x509_certificate - regenerate certificate when the CA's public key changes for ``provider=ownca`` (https://github.com/ansible-collections/community.crypto/pull/407).
- x509_certificate - regenerate certificate when the CA's subject changes for ``provider=ownca`` (https://github.com/ansible-collections/community.crypto/issues/400, https://github.com/ansible-collections/community.crypto/pull/402).
- x509_certificate - regenerate certificate when the private key changes for ``provider=selfsigned`` (https://github.com/ansible-collections/community.crypto/pull/407).

community.digitalocean
~~~~~~~~~~~~~~~~~~~~~~

- digital_ocean_droplet - fix reporting of changed state when ``firewall`` argument is present (https://github.com/ansible-collections/community.digitalocean/pull/219).

community.dns
~~~~~~~~~~~~~

- Update Public Suffix List.

community.docker
~~~~~~~~~~~~~~~~

- docker_container, docker_image - adjust image finding code to pecularities of ``podman-docker``'s API emulation when Docker short names like ``redis`` are used (https://github.com/ansible-collections/community.docker/issues/292).

community.general
~~~~~~~~~~~~~~~~~

- dconf - skip processes that disappeared while we inspected them (https://github.com/ansible-collections/community.general/issues/4151).
- gitlab_group_variable - add missing documentation about GitLab versions that support ``environment_scope`` and ``variable_type`` (https://github.com/ansible-collections/community.general/pull/4038).
- gitlab_group_variable - allow to set same variable name under different environment scopes. Due this change, the return value ``group_variable`` differs from previous version in check mode. It was counting ``updated`` values, because it was accidentally overwriting environment scopes (https://github.com/ansible-collections/community.general/pull/4038).
- gitlab_group_variable - fix idempotent change behaviour for float and integer variables (https://github.com/ansible-collections/community.general/pull/4038).
- gitlab_project_variable - ``value`` is not necessary when deleting variables (https://github.com/ansible-collections/community.general/pull/4150).
- gitlab_runner - make ``project`` and ``owned`` mutually exclusive (https://github.com/ansible-collections/community.general/pull/4136).
- homebrew_cask - fix force install operation (https://github.com/ansible-collections/community.general/issues/3703).
- imc_rest - fixes the module failure due to the usage of ``itertools.izip_longest`` which is not available in Python 3 (https://github.com/ansible-collections/community.general/issues/4206).
- ini_file - when removing nothing do not report changed (https://github.com/ansible-collections/community.general/issues/4154).
- keycloak_user_federation - creating a user federation while specifying an ID (that does not exist yet) no longer fail with a 404 Not Found (https://github.com/ansible-collections/community.general/pull/4212).
- keycloak_user_federation - mappers auto-created by keycloak are matched and merged by their name and no longer create duplicated entries (https://github.com/ansible-collections/community.general/pull/4212).
- mail callback plugin - fix encoding of the name of sender and recipient (https://github.com/ansible-collections/community.general/issues/4060, https://github.com/ansible-collections/community.general/pull/4061).
- passwordstore lookup plugin - fix error detection for non-English locales (https://github.com/ansible-collections/community.general/pull/4219).
- passwordstore lookup plugin - prevent returning path names as passwords by accident (https://github.com/ansible-collections/community.general/issues/4185, https://github.com/ansible-collections/community.general/pull/4192).
- vdo - fix options error (https://github.com/ansible-collections/community.general/pull/4163).
- yum_versionlock - fix matching of existing entries with names passed to the module. Match yum and dnf lock format (https://github.com/ansible-collections/community.general/pull/4183).

community.grafana
~~~~~~~~~~~~~~~~~

- Fix an issue with threema notification channel that was not creating gateway, recipient and api_secret in Grafana. (#208)

community.mysql
~~~~~~~~~~~~~~~

- mysql_role - make the ``set_default_role_all`` parameter actually working (https://github.com/ansible-collections/community.mysql/pull/282).

junipernetworks.junos
~~~~~~~~~~~~~~~~~~~~~

- Fix junos_command output when empty config response is received for show commands (https://github.com/ansible-collections/junipernetworks.junos/issues/249).

netapp.cloudmanager
~~~~~~~~~~~~~~~~~~~

- CVO working environment clusterProperties is deprecated. Make changes accordingly. Add CVO update status check on ``instance_type`` change.

netapp.ontap
~~~~~~~~~~~~

- four modules (mediator, metrocluster, security_certificates, wwpn_alias) would report a None error when REST is not available.
- module_utils - fixed KeyError on Allow when using OPTIONS method and the API failed.
- na_ontap_active_directory - Fixed idempotency and traceback issues.
- na_ontap_aggregate - Fixed KeyError on unmount_volumes when offlining a volume if option is not set.
- na_ontap_aggregate - Report an error when attempting to change snaplock_type.
- na_ontap_igroup - ``force_remove_initiator`` option was ignored when removing initiators from existing igroup.
- na_ontap_info - Add active_directory_account_info.
- na_ontap_security_certificates - ``intermediate_certificates`` option was ignored.
- na_ontap_user - Fixed TypeError 'tuple' object does not support item assignment.
- na_ontap_user - Fixed issue when attempting to change pasword for absent user when set_password is set.
- na_ontap_user - Fixed lock state is not set if password is not changed.
- na_ontap_volume - Fixed error when creating a flexGroup when ``aggregate_name`` and ``aggr_list_multiplier`` are not set in rest.
- na_ontap_volume - Fixed error with unmounting junction_path in rest.
- na_ontap_volume - report error when attempting to change the nas_application tiering control from disalllowed to required, or reciprocally.

ngine_io.cloudstack
~~~~~~~~~~~~~~~~~~~

- cs_instance - Fixed regression project ID KeyError if no project is used (https://github.com/ngine-io/ansible-collection-cloudstack/pull/94).

New Plugins
-----------

Lookup
~~~~~~

- community.hashi_vault.vault_token_create - Create a HashiCorp Vault token

New Modules
-----------

cisco.ios
~~~~~~~~~

- cisco.ios.ios_hostname - hostname resource module

cisco.iosxr
~~~~~~~~~~~

- cisco.iosxr.iosxr_hostname - Manages hostname resource module

cisco.nxos
~~~~~~~~~~

- cisco.nxos.nxos_hostname - Hostname resource module.

community.general
~~~~~~~~~~~~~~~~~

Cloud
^^^^^

Scaleway
........

- community.general.scaleway_private_network - Scaleway private network management

Storage
^^^^^^^

Pmem
....

- community.general.pmem - Configure Intel Optane Persistent Memory modules

community.hashi_vault
~~~~~~~~~~~~~~~~~~~~~

- community.hashi_vault.vault_pki_generate_certificate - Generates a new set of credentials (private key and certificate) using HashiCorp Vault PKI
- community.hashi_vault.vault_token_create - Create a HashiCorp Vault token

junipernetworks.junos
~~~~~~~~~~~~~~~~~~~~~

- junipernetworks.junos.junos_hostname - Manage Hostname server configuration on Junos devices.
- junipernetworks.junos.junos_snmp_server - Manage SNMP server configuration on Junos devices.

vyos.vyos
~~~~~~~~~

- vyos.vyos.vyos_snmp_server - Manages snmp_server resource module

Unchanged Collections
---------------------

- amazon.aws (still version 2.1.0)
- ansible.posix (still version 1.3.0)
- ansible.windows (still version 1.9.0)
- arista.eos (still version 3.1.0)
- awx.awx (still version 19.4.0)
- azure.azcollection (still version 1.11.0)
- check_point.mgmt (still version 2.2.2)
- cisco.aci (still version 2.1.0)
- cisco.asa (still version 2.1.0)
- cisco.intersight (still version 1.0.18)
- cisco.ise (still version 1.2.1)
- cisco.meraki (still version 2.6.0)
- cisco.mso (still version 1.3.0)
- cisco.nso (still version 1.0.3)
- cisco.ucs (still version 1.6.0)
- cloud.common (still version 2.1.0)
- cloudscale_ch.cloud (still version 2.2.0)
- community.azure (still version 1.1.0)
- community.ciscosmb (still version 1.0.4)
- community.fortios (still version 1.0.0)
- community.google (still version 1.0.0)
- community.hrobot (still version 1.2.2)
- community.kubernetes (still version 2.0.1)
- community.kubevirt (still version 1.0.0)
- community.libvirt (still version 1.0.2)
- community.mongodb (still version 1.3.2)
- community.network (still version 3.0.0)
- community.okd (still version 2.1.0)
- community.proxysql (still version 1.3.1)
- community.rabbitmq (still version 1.1.0)
- community.routeros (still version 2.0.0)
- community.skydive (still version 1.0.0)
- community.sops (still version 1.2.0)
- community.vmware (still version 1.17.1)
- community.windows (still version 1.9.0)
- community.zabbix (still version 1.5.1)
- containers.podman (still version 1.9.1)
- cyberark.conjur (still version 1.1.0)
- cyberark.pas (still version 1.0.13)
- dellemc.enterprise_sonic (still version 1.1.0)
- dellemc.openmanage (still version 4.4.0)
- dellemc.os10 (still version 1.1.1)
- dellemc.os6 (still version 1.0.7)
- dellemc.os9 (still version 1.0.4)
- f5networks.f5_modules (still version 1.14.0)
- fortinet.fortimanager (still version 2.1.4)
- frr.frr (still version 1.0.3)
- gluster.gluster (still version 1.0.2)
- google.cloud (still version 1.0.2)
- hetzner.hcloud (still version 1.6.0)
- hpe.nimble (still version 1.1.4)
- ibm.qradar (still version 1.0.3)
- infinidat.infinibox (still version 1.3.3)
- infoblox.nios_modules (still version 1.2.1)
- inspur.sm (still version 1.3.0)
- kubernetes.core (still version 2.2.3)
- mellanox.onyx (still version 1.0.0)
- netapp.aws (still version 21.7.0)
- netapp.azure (still version 21.10.0)
- netapp.elementsw (still version 21.7.0)
- netapp.storagegrid (still version 21.9.0)
- netapp.um_info (still version 21.8.0)
- netapp_eseries.santricity (still version 1.2.13)
- netbox.netbox (still version 3.5.1)
- ngine_io.exoscale (still version 1.0.0)
- ngine_io.vultr (still version 1.1.0)
- openvswitch.openvswitch (still version 2.1.0)
- ovirt.ovirt (still version 1.6.6)
- purestorage.flasharray (still version 1.12.1)
- purestorage.flashblade (still version 1.9.0)
- sensu.sensu_go (still version 1.13.0)
- servicenow.servicenow (still version 1.0.6)
- splunk.es (still version 1.0.2)
- theforeman.foreman (still version 2.2.0)
- wti.remote (still version 1.0.3)

v5.3.0
======

.. contents::
  :local:
  :depth: 2

Release Summary
---------------

Release Date: 2022-02-01

`Porting Guide <https://docs.ansible.com/ansible/devel/porting_guides.html>`_

Ansible-core
------------

Ansible 5.3.0 contains Ansible-core version 2.12.2.
This is a newer version than version 2.12.1 contained in the previous Ansible release.

The changes are reported in the combined changelog below.

Changed Collections
-------------------

If not mentioned explicitly, the changes are reported in the combined changelog below.

+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| Collection             | Ansible 5.2.0 | Ansible 5.3.0 | Notes                                                                                                                        |
+========================+===============+===============+==============================================================================================================================+
| azure.azcollection     | 1.10.0        | 1.11.0        | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| check_point.mgmt       | 2.2.0         | 2.2.2         | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.aws          | 2.1.0         | 2.2.0         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.crypto       | 2.1.0         | 2.2.0         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.digitalocean | 1.14.0        | 1.15.0        |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.dns          | 2.0.4         | 2.0.6         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.general      | 4.3.0         | 4.4.0         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.mysql        | 2.3.2         | 2.3.3         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.postgresql   | 1.6.0         | 1.6.1         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.vmware       | 1.17.0        | 1.17.1        |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| containers.podman      | 1.9.0         | 1.9.1         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| f5networks.f5_modules  | 1.13.0        | 1.14.0        |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| kubernetes.core        | 2.2.2         | 2.2.3         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| netapp.cloudmanager    | 21.12.1       | 21.13.0       |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| netapp.ontap           | 21.14.1       | 21.15.1       |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| netbox.netbox          | 3.5.0         | 3.5.1         |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| openstack.cloud        | 1.5.3         | 1.6.0         | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| purestorage.flasharray | 1.12.0        | 1.12.1        |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| sensu.sensu_go         | 1.12.1        | 1.13.0        |                                                                                                                              |
+------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+

Major Changes
-------------

f5networks.f5_modules
~~~~~~~~~~~~~~~~~~~~~

- bigip_device_info - pagination logic has also been added to help with api stability.
- bigip_device_info - the module no longer gathers information from all partitions on device. This change will stabalize the module by gathering resources only from the given partition and prevent the module from gathering way too much information that might result in crashing.

Minor Changes
-------------

community.aws
~~~~~~~~~~~~~

- aws_msk_config - remove duplicated and unspecific requirements (https://github.com/ansible-collections/community.aws/pull/863).
- aws_ssm connection plugin - add parameters to explicitly specify SSE mode and KMS key id for uploads on the file transfer bucket. (https://github.com/ansible-collections/community.aws/pull/763)
- ecs_taskdefinition - remove duplicated and unspecific requirements (https://github.com/ansible-collections/community.aws/pull/863).
- iam_user - add boto3 waiter for iam user creation (https://github.com/ansible-collections/community.aws/pull/822).
- iam_user - add password management support bringing parity with `iam` module (https://github.com/ansible-collections/community.aws/pull/822).
- s3_lifecycle - Add ``abort_incomplete_multipart_upload_days`` and ``expire_object_delete_marker`` parameters (https://github.com/ansible-collections/community.aws/pull/794).

community.crypto
~~~~~~~~~~~~~~~~

- openssh_cert - added ``ignore_timestamps`` parameter so it can be used semi-idempotent with relative timestamps in ``valid_to``/``valid_from`` (https://github.com/ansible-collections/community.crypto/issues/379).

community.general
~~~~~~~~~~~~~~~~~

- cobbler inventory plugin - add ``include_profiles`` option (https://github.com/ansible-collections/community.general/pull/4068).
- gitlab_project_variable - new ``variables`` parameter (https://github.com/ansible-collections/community.general/issues/4038).
- icinga2 inventory plugin - implemented constructed interface (https://github.com/ansible-collections/community.general/pull/4088).
- linode inventory plugin - allow templating of ``access_token`` variable in Linode inventory plugin (https://github.com/ansible-collections/community.general/pull/4040).
- lists_mergeby filter plugin - add parameters ``list_merge`` and ``recursive``. These are only supported when used with ansible-base 2.10 or ansible-core, but not with Ansible 2.9 (https://github.com/ansible-collections/community.general/pull/4058).
- lxc_container - added ``wait_for_container`` parameter. If ``true`` the module will wait until the running task reports success as the status (https://github.com/ansible-collections/community.general/pull/4039).
- mail callback plugin - add ``Message-ID`` and ``Date`` headers (https://github.com/ansible-collections/community.general/issues/4055, https://github.com/ansible-collections/community.general/pull/4056).
- mail callback plugin - properly use Ansible's option handling to split lists (https://github.com/ansible-collections/community.general/pull/4140).
- nmcli - adds ``routes6`` and ``route_metric6`` parameters for supporting IPv6 routes (https://github.com/ansible-collections/community.general/issues/4059).
- opennebula - add the release action for VMs in the ``HOLD`` state (https://github.com/ansible-collections/community.general/pull/4036).
- opentelemetry_plugin - enrich service when using the ``docker_login`` (https://github.com/ansible-collections/community.general/pull/4104).
- proxmox modules - move ``HAS_PROXMOXER`` check into ``module_utils`` (https://github.com/ansible-collections/community.general/pull/4030).
- scaleway inventory plugin - add profile parameter ``scw_profile`` (https://github.com/ansible-collections/community.general/pull/4049).
- snap - add option ``options`` permitting to set options using the ``snap set`` command (https://github.com/ansible-collections/community.general/pull/3943).

containers.podman
~~~~~~~~~~~~~~~~~

- Add new options for pod module
- Use yaml syntax highlighting where appropriate

f5networks.f5_modules
~~~~~~~~~~~~~~~~~~~~~

- Added no_log=True to content parameters in bigip_ssl_key and bigip_ssl_key_cert module to stop key and cert content fomr being logged.
- bigip_device_info - added stats parameter for each virtual_server resource attached to a gtm_server

kubernetes.core
~~~~~~~~~~~~~~~

- Add integration test to check handling of module_defaults (https://github.com/ansible-collections/kubernetes.core/pull/296).

netapp.cloudmanager
~~~~~~~~~~~~~~~~~~~

- Add ``update_svm_password`` for ``svm_password`` update on AWS, AZURE and GCP CVOs. Update ``svm_password`` if ``update_svm_password`` is true.
- Add ontap image upgrade on AWS, AZURE and GCP CVOs if ``upgrade_ontap_version`` is true and ``ontap_version`` is provided with a specific version. ``use_latest_version`` has to be false.
- na_cloudmanager_connector_aws - automatically fetch client_id and instance_id for delete.
- na_cloudmanager_connector_aws - make the module idempotent for create and delete.
- na_cloudmanager_connector_aws - report client_id and instance_id if connector already exists.
- na_cloudmanager_cvo_aws - Support instance_type update
- na_cloudmanager_cvo_azure - Support instance_type update
- na_cloudmanager_cvo_gcp - Support instance_type update
- na_cloudmanager_info - new subsets - account_info, agents_info, active_agents_info
- na_cloudmanager_volume - Report error if the volume properties cannot be modified. Add support ``tiering_policy`` and ``snapshot_policy_name`` modification.

netapp.ontap
~~~~~~~~~~~~

- na_ontap_broadcast_domain - Added REST support to the broadcast domain module.
- na_ontap_broadcast_domain - new REST only option ``from_ipspace`` added.
- na_ontap_broadcast_domain_ports - warn about deprecation, fall back to ZAPI or fail when REST is desired.
- na_ontap_export_policy_rule -- Added Rest support for Export Policy Rules
- na_ontap_firmware_upgrade - REST support to download firmware and reboot SP.
- na_ontap_license - Added REST support to the license module.
- na_ontap_rest_info - update documention for `fields` to clarify the list of fields that are return by default.
- na_ontap_svm - new REST options of svm admin_state ``stopped`` and ``running`` added.

purestorage.flasharray
~~~~~~~~~~~~~~~~~~~~~~

- All modules - Change examples to use FQCN for module

sensu.sensu_go
~~~~~~~~~~~~~~

- Added argument remote_on inside bonsai_asset module

Deprecated Features
-------------------

community.general
~~~~~~~~~~~~~~~~~

- mail callback plugin - not specifying ``sender`` is deprecated and will be disallowed in community.general 6.0.0 (https://github.com/ansible-collections/community.general/pull/4140).

Bugfixes
--------

Ansible-core
~~~~~~~~~~~~

- Fix ``AttributeError`` when providing password file via ``--connection-password-file`` (https://github.com/ansible/ansible/issues/76530)
- Fix ``end_play`` to end the current play only (https://github.com/ansible/ansible/issues/76672)
- Templating - Ensure we catch exceptions when getting ``.filters`` and ``.tests`` attributes on their respective plugins and properly error, instead of aborting which results in no filters being added to the jinja2 environment
- ``Templar.copy_with_new_env`` - set the ``finalize`` method of the new ``Templar`` object for the new environment (https://github.com/ansible/ansible/issues/76379)
- ansible-config avoid showing _terms and _input when --only-changed.
- ansible-galaxy - Fix using the '--ignore-certs' option when there is no server-specific configuration for the Galaxy server.
- ansible-galaxy collection build - Ignore any existing ``MANIFEST.json`` and ``FILES.json`` in the root directory when building a collection.
- ansible-test - Fix the ``import`` sanity test to work properly when Ansible's built-in vendoring support is in use.
- ansible-test - Fix traceback in the ``validate-modules`` sanity test when testing an Ansible module without any callables.
- ansible-test - Fix traceback when running from an install and delegating execution to a different Python interpreter.
- ansible-test - Show an error message instead of a traceback when running outside of a supported directory.
- ansible-test - Update help links to reference ``ansible-core`` instead of ``ansible``.
- ansible-test - Update unit tests to use the ``--forked`` option instead of the deprecated ``--boxed`` option.
- async - Improve performance of sending async callback events by never sending the full task through the queue (https://github.com/ansible/ansible/issues/76729)
- default callback - Ensure we compare FQCN also in lockstep logic, to ensure using the FQCN of a strategy plugin triggers the correct behavior in the default callback plugin. (https://github.com/ansible/ansible/issues/76782)
- hostname - Do not require SystemdStrategy subclasses for every distro (https://github.com/ansible/ansible/issues/76792)
- include_vars, properly initialize variable as there is corner case in which it can end up referenced and not defined
- ssh connection - properly quote controlpersist path given by user to avoid issues with spaces and other characters
- ssh connection avoid parsing ssh cli debug lines as they can match expected output at high verbosities.
- sudo become plugin, fix handling of non interactive flags, previous substitution was too naive
- unarchive - Fix zip archive file listing that caused issues with content postprocessing (https://github.com/ansible/ansible/issues/76067).
- yum - prevent storing unnecessary cache data by running `yum makecache fast` (https://github.com/ansible/ansible/issues/76336)

community.aws
~~~~~~~~~~~~~

- aws_eks - Fix EKS cluster creation with short names (https://github.com/ansible-collections/community.aws/pull/818).

community.crypto
~~~~~~~~~~~~~~~~

- luks_devices - set ``LANG`` and similar environment variables to avoid translated output, which can break some of the module's functionality like key management (https://github.com/ansible-collections/community.crypto/pull/388, https://github.com/ansible-collections/community.crypto/issues/385).

community.digitalocean
~~~~~~~~~~~~~~~~~~~~~~

- digital_ocean_droplet - move Droplet data under "droplet" key in returned payload (https://github.com/ansible-collections/community.digitalocean/issues/211).

community.dns
~~~~~~~~~~~~~

- Update Public Suffix List.
- wait_for_txt - do not fail if ``NXDOMAIN`` result is returned. Also do not succeed if no nameserver can be found (https://github.com/ansible-collections/community.dns/issues/81, https://github.com/ansible-collections/community.dns/pull/82).

community.general
~~~~~~~~~~~~~~~~~

- cargo - fix detection of outdated packages when ``state=latest`` (https://github.com/ansible-collections/community.general/pull/4052).
- cargo - fix incorrectly reported changed status for packages with a name containing a hyphen (https://github.com/ansible-collections/community.general/issues/4044, https://github.com/ansible-collections/community.general/pull/4052).
- gitlab_project_variable - add missing documentation about GitLab versions that support ``environment_scope`` and ``variable_type`` (https://github.com/ansible-collections/community.general/issues/4038).
- gitlab_project_variable - allow to set same variable name under different environment scopes. Due this change, the return value ``project_variable`` differs from previous version in check mode. It was counting ``updated`` values, because it was accidentally overwriting environment scopes (https://github.com/ansible-collections/community.general/issues/4038).
- gitlab_project_variable - fix idempotent change behaviour for float and integer variables (https://github.com/ansible-collections/community.general/issues/4038).
- gitlab_runner - use correct API endpoint to create and retrieve project level runners when using ``project`` (https://github.com/ansible-collections/community.general/pull/3965).
- listen_ports_facts - local port regex was not handling well IPv6 only binding. Fixes the regex for ``ss`` (https://github.com/ansible-collections/community.general/pull/4092).
- mail callback plugin - fix crash on Python 3 (https://github.com/ansible-collections/community.general/issues/4025, https://github.com/ansible-collections/community.general/pull/4026).
- opentelemetry - fix generating a trace with a task containing ``no_log: true`` (https://github.com/ansible-collections/community.general/pull/4043).
- python_requirements_info - store ``mismatched`` return values per package as documented in the module (https://github.com/ansible-collections/community.general/pull/4078).
- yarn - fix incorrect handling of ``yarn list`` and ``yarn global list`` output that could result in fatal error (https://github.com/ansible-collections/community.general/pull/4050).
- yarn - fix incorrectly reported status when installing a package globally (https://github.com/ansible-collections/community.general/issues/4045, https://github.com/ansible-collections/community.general/pull/4050).
- yarn - fix missing ``~`` expansion in yarn global install folder which resulted in incorrect task status (https://github.com/ansible-collections/community.general/issues/4045, https://github.com/ansible-collections/community.general/pull/4048).

community.mysql
~~~~~~~~~~~~~~~

- Collection core functions - use vendored version of ``distutils.version`` instead of the deprecated Python standard library ``distutils`` (https://github.com/ansible-collections/community.mysql/pull/269).

community.postgresql
~~~~~~~~~~~~~~~~~~~~

- Collection core functions - use vendored version of ``distutils.version`` instead of the deprecated Python standard library ``distutils`` (https://github.com/ansible-collections/community.postgresql/pull/179).
- postgres_info - It now works on AWS RDS Postgres.
- postgres_info - Specific info (namespaces, extensions, languages) of each database was not being shown properly. Instead, the info from the DB that was connected was always being shown (https://github.com/ansible-collections/community.postgresql/issues/172).

community.vmware
~~~~~~~~~~~~~~~~

- vmware_guest_network - fix a bug that can crash the module due to an uncaught exception (https://github.com/ansible-collections/community.vmware/issues/25).

containers.podman
~~~~~~~~~~~~~~~~~

- Fix podman_pod_lib behavior for ports published to multiple IPs
- Handle tlsverify correctly in podman_login
- Update secrets description and add test with secret opts

f5networks.f5_modules
~~~~~~~~~~~~~~~~~~~~~

- asm_policy_* - fixed partition filter in asm modules.
- bigip_device_info - changes cipher and cipher_group parameters to register when the actual value is 'none'.
- bigip_device_syslog - this change is done so that only unescaped " is replaced with ' in the value of include parameter.
- bigip_monitor_ldap - fixed idempotency issue with security parameter in module.
- multiple modules - Add no_log=False setting to update_password parameter in respective modules avoid false positive security warnings.

kubernetes.core
~~~~~~~~~~~~~~~

- k8s_drain - fix error caused by accessing an undefined variable when pods have local storage (https://github.com/ansible-collections/kubernetes.core/issues/292).
- k8s_info - don't wait on empty List resources (https://github.com/ansible-collections/kubernetes.core/pull/253).
- module_utils.common - change default opening mode to read-bytes to avoid bad interpretation of non ascii characters and strings, often present in 3rd party manifests.

netapp.cloudmanager
~~~~~~~~~~~~~~~~~~~

- na_cloudmanager_cvo_gcp - handle extra two auto-gen GCP labels to prevent update ``gcp_labels`` failure.

netapp.ontap
~~~~~~~~~~~~

- na_ontap_broadcast_domain - fix idempotency issue when ``ports`` has identical values.
- na_ontap_export_policy_rule - Fixed bug that prevent ZAPI and REST calls from working correctly
- na_ontap_info - fix KeyError on node for aggr_efficiency_info option against a metrocluster system.
- na_ontap_volume - Fixed issue that would fail the module in REST when changing `is_online` if two vserver volume had the same name.
- na_ontap_volume - If using REST and ONTAP 9.6 and `efficiency_policy` module will fail as `efficiency_policy` is not supported in ONTAP 9.6.
- na_ontap_volume_efficiency - Removed restriction on policy name.

netbox.netbox
~~~~~~~~~~~~~

- Fix prefix_count error on older NetBox versions in nb_inventory [#696](https://github.com/netbox-community/ansible_modules/pull/696)

purestorage.flasharray
~~~~~~~~~~~~~~~~~~~~~~

- purefa_info - Fix space reporting issue
- purefa_subnet - Fix subnet update checks when no gateway in existing subnet configuration

New Modules
-----------

community.aws
~~~~~~~~~~~~~

- community.aws.ec2_asg_scheduled_action - Create, modify and delete ASG scheduled scaling actions.

community.digitalocean
~~~~~~~~~~~~~~~~~~~~~~

- community.digitalocean.digital_ocean_spaces - Create and remove DigitalOcean Spaces.
- community.digitalocean.digital_ocean_spaces_info - List DigitalOcean Spaces.

community.general
~~~~~~~~~~~~~~~~~

System
^^^^^^

- community.general.homectl - Manage user accounts with systemd-homed

netapp.cloudmanager
~~~~~~~~~~~~~~~~~~~

- netapp.cloudmanager.na_cloudmanager_aws_fsx - Cloud ONTAP file system(FSX) in AWS

Unchanged Collections
---------------------

- amazon.aws (still version 2.1.0)
- ansible.netcommon (still version 2.5.0)
- ansible.posix (still version 1.3.0)
- ansible.utils (still version 2.4.3)
- ansible.windows (still version 1.9.0)
- arista.eos (still version 3.1.0)
- awx.awx (still version 19.4.0)
- chocolatey.chocolatey (still version 1.1.0)
- cisco.aci (still version 2.1.0)
- cisco.asa (still version 2.1.0)
- cisco.intersight (still version 1.0.18)
- cisco.ios (still version 2.6.0)
- cisco.iosxr (still version 2.6.0)
- cisco.ise (still version 1.2.1)
- cisco.meraki (still version 2.6.0)
- cisco.mso (still version 1.3.0)
- cisco.nso (still version 1.0.3)
- cisco.nxos (still version 2.8.2)
- cisco.ucs (still version 1.6.0)
- cloud.common (still version 2.1.0)
- cloudscale_ch.cloud (still version 2.2.0)
- community.azure (still version 1.1.0)
- community.ciscosmb (still version 1.0.4)
- community.docker (still version 2.1.1)
- community.fortios (still version 1.0.0)
- community.google (still version 1.0.0)
- community.grafana (still version 1.3.0)
- community.hashi_vault (still version 2.2.0)
- community.hrobot (still version 1.2.2)
- community.kubernetes (still version 2.0.1)
- community.kubevirt (still version 1.0.0)
- community.libvirt (still version 1.0.2)
- community.mongodb (still version 1.3.2)
- community.network (still version 3.0.0)
- community.okd (still version 2.1.0)
- community.proxysql (still version 1.3.1)
- community.rabbitmq (still version 1.1.0)
- community.routeros (still version 2.0.0)
- community.skydive (still version 1.0.0)
- community.sops (still version 1.2.0)
- community.windows (still version 1.9.0)
- community.zabbix (still version 1.5.1)
- cyberark.conjur (still version 1.1.0)
- cyberark.pas (still version 1.0.13)
- dellemc.enterprise_sonic (still version 1.1.0)
- dellemc.openmanage (still version 4.4.0)
- dellemc.os10 (still version 1.1.1)
- dellemc.os6 (still version 1.0.7)
- dellemc.os9 (still version 1.0.4)
- fortinet.fortimanager (still version 2.1.4)
- fortinet.fortios (still version 2.1.3)
- frr.frr (still version 1.0.3)
- gluster.gluster (still version 1.0.2)
- google.cloud (still version 1.0.2)
- hetzner.hcloud (still version 1.6.0)
- hpe.nimble (still version 1.1.4)
- ibm.qradar (still version 1.0.3)
- infinidat.infinibox (still version 1.3.3)
- infoblox.nios_modules (still version 1.2.1)
- inspur.sm (still version 1.3.0)
- junipernetworks.junos (still version 2.8.0)
- mellanox.onyx (still version 1.0.0)
- netapp.aws (still version 21.7.0)
- netapp.azure (still version 21.10.0)
- netapp.elementsw (still version 21.7.0)
- netapp.storagegrid (still version 21.9.0)
- netapp.um_info (still version 21.8.0)
- netapp_eseries.santricity (still version 1.2.13)
- ngine_io.cloudstack (still version 2.2.2)
- ngine_io.exoscale (still version 1.0.0)
- ngine_io.vultr (still version 1.1.0)
- openvswitch.openvswitch (still version 2.1.0)
- ovirt.ovirt (still version 1.6.6)
- purestorage.flashblade (still version 1.9.0)
- servicenow.servicenow (still version 1.0.6)
- splunk.es (still version 1.0.2)
- t_systems_mms.icinga_director (still version 1.27.0)
- theforeman.foreman (still version 2.2.0)
- vyos.vyos (still version 2.6.0)
- wti.remote (still version 1.0.3)

v5.2.0
======

.. contents::
  :local:
  :depth: 2

Release Summary
---------------

Release Date: 2022-01-12

`Porting Guide <https://docs.ansible.com/ansible/devel/porting_guides.html>`_

Ansible-core
------------

Ansible 5.2.0 contains Ansible-core version 2.12.1.
This is the same version of Ansible-core as in the previous Ansible release.


Changed Collections
-------------------

If not mentioned explicitly, the changes are reported in the combined changelog below.

+-------------------------------+---------------+---------------+-------+
| Collection                    | Ansible 5.1.0 | Ansible 5.2.0 | Notes |
+===============================+===============+===============+=======+
| cisco.meraki                  | 2.5.0         | 2.6.0         |       |
+-------------------------------+---------------+---------------+-------+
| community.crypto              | 2.0.2         | 2.1.0         |       |
+-------------------------------+---------------+---------------+-------+
| community.dns                 | 2.0.3         | 2.0.4         |       |
+-------------------------------+---------------+---------------+-------+
| community.docker              | 2.0.2         | 2.1.1         |       |
+-------------------------------+---------------+---------------+-------+
| community.general             | 4.2.0         | 4.3.0         |       |
+-------------------------------+---------------+---------------+-------+
| community.hashi_vault         | 2.1.0         | 2.2.0         |       |
+-------------------------------+---------------+---------------+-------+
| community.hrobot              | 1.2.1         | 1.2.2         |       |
+-------------------------------+---------------+---------------+-------+
| community.proxysql            | 1.3.0         | 1.3.1         |       |
+-------------------------------+---------------+---------------+-------+
| dellemc.openmanage            | 4.3.0         | 4.4.0         |       |
+-------------------------------+---------------+---------------+-------+
| netbox.netbox                 | 3.4.0         | 3.5.0         |       |
+-------------------------------+---------------+---------------+-------+
| purestorage.flasharray        | 1.11.0        | 1.12.0        |       |
+-------------------------------+---------------+---------------+-------+
| t_systems_mms.icinga_director | 1.26.0        | 1.27.0        |       |
+-------------------------------+---------------+---------------+-------+

Major Changes
-------------

cisco.meraki
~~~~~~~~~~~~

- meraki_mr_radio - New module

Minor Changes
-------------

cisco.meraki
~~~~~~~~~~~~

- meraki_mx_l7_firewall - Allow passing an empty ruleset to delete all rules
- meraki_utils - Add debugging output for failed socket connections

community.crypto
~~~~~~~~~~~~~~~~

- Adjust error messages that indicate ``cryptography`` is not installed from ``Can't`` to ``Cannot`` (https://github.com/ansible-collections/community.crypto/pull/374).

community.docker
~~~~~~~~~~~~~~~~

- docker_container_exec - add ``detach`` parameter (https://github.com/ansible-collections/community.docker/issues/250, https://github.com/ansible-collections/community.docker/pull/255).
- docker_container_exec - add ``env`` option (https://github.com/ansible-collections/community.docker/issues/248, https://github.com/ansible-collections/community.docker/pull/254).

community.general
~~~~~~~~~~~~~~~~~

- ipa_dnszone - ``dynamicupdate`` is now a boolean parameter, instead of a string parameter accepting ``"true"`` and ``"false"``. Also the module is now idempotent with respect to ``dynamicupdate`` (https://github.com/ansible-collections/community.general/pull/3374).
- ipa_dnszone - add DNS zone synchronization support (https://github.com/ansible-collections/community.general/pull/3374).
- ipmi_power - add ``machine`` option to ensure the power state via the remote target address (https://github.com/ansible-collections/community.general/pull/3968).
- mattermost - add the possibility to send attachments instead of text messages (https://github.com/ansible-collections/community.general/pull/3946).
- nmcli - add ``wireguard`` connection type (https://github.com/ansible-collections/community.general/pull/3985).
- proxmox - add ``clone`` parameter (https://github.com/ansible-collections/community.general/pull/3930).
- puppet - remove deprecation for ``show_diff`` parameter. Its alias ``show-diff`` is still deprecated and will be removed in community.general 7.0.0 (https://github.com/ansible-collections/community.general/pull/3980).
- scaleway_compute - add possibility to use project identifier (new ``project`` option) instead of deprecated organization identifier (https://github.com/ansible-collections/community.general/pull/3951).
- scaleway_volume - all volumes are systematically created on par1 (https://github.com/ansible-collections/community.general/pull/3964).

community.hashi_vault
~~~~~~~~~~~~~~~~~~~~~

- The Filter guide has been added to the collection's docsite.

community.proxysql
~~~~~~~~~~~~~~~~~~

- module_utils - Refactor save_config_to_disk and load_config_to_runtime (https://github.com/ansible-collections/community.proxysql/pull/78).
- proxysql_mysql_users - Add missing ``no_log`` option to ``encrypt_password`` parameter (https://github.com/ansible-collections/community.proxysql/pull/86).

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- ome_firmware - The module is enhanced to support check mode and idempotency (https://github.com/dell/dellemc-openmanage-ansible-modules/issues/274)
- ome_template - An example task is added to create a compliance template from reference device (https://github.com/dell/dellemc-openmanage-ansible-modules/issues/339)

netbox.netbox
~~~~~~~~~~~~~

- nb_inventory - Pull extended inventory data for prefixes and site [#646](https://github.com/netbox-community/ansible_modules/pull/646)
- nb_lookup - Add endpoints for wireless (new in NetBox 3.1) [#673](https://github.com/netbox-community/ansible_modules/pull/673)
- netbox_circuit_termination - Add mark_connected field to module [#686](https://github.com/netbox-community/ansible_modules/pull/686)
- netbox_contact, netbox_contact_group, netbox_contact_role - Add modules [#671](https://github.com/netbox-community/ansible_modules/pull/671)
- netbox_inventory_item - Add parent field to module [#682](https://github.com/netbox-community/ansible_modules/pull/682)
- netbox_region - Add description, tags, custom_fields to module [#689](https://github.com/netbox-community/ansible_modules/pull/689)
- netbox_wireless_lan, netbox_wireless_lan_group, netbox_wireless_link - Add modules [#678](https://github.com/netbox-community/ansible_modules/pull/678)

purestorage.flasharray
~~~~~~~~~~~~~~~~~~~~~~

- purefa_admin - New module to set global admin settings, inclusing SSO
- purefa_dirsnap - Add support to rename directory snapshots not managed by a snapshot policy
- purefa_info - Add SAML2SSO configutration information
- purefa_info - Add Safe Mode status
- purefa_info - Fix Active Directory configuration details
- purefa_network - Resolve bug stopping management IP address being changed correctly
- purefa_offload - Add support for multiple, homogeneous, offload targets
- purefa_saml - Add support for SAML2 SSO IdPs
- purefa_volume - Provide volume facts in all cases, including when no change has occured.

t_systems_mms.icinga_director
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Add possibility to use Compose and keyed groups in inventory-module (https://github.com/T-Systems-MMS/ansible-collection-icinga-director/pull/155)

Deprecated Features
-------------------

purestorage.flasharray
~~~~~~~~~~~~~~~~~~~~~~

- purefa_sso - Deprecated in favor of M(purefa_admin). Will be removed in Collection 2.0

Bugfixes
--------

cisco.meraki
~~~~~~~~~~~~

- meraki_mr_ssid - Fix issue with SSID removal idempotency when ID doesn't exist

community.crypto
~~~~~~~~~~~~~~~~

- Various modules and plugins - use vendored version of ``distutils.version`` instead of the deprecated Python standard library ``distutils`` (https://github.com/ansible-collections/community.crypto/pull/353).
- certificate_complete_chain - do not append root twice if the chain already ends with a root certificate (https://github.com/ansible-collections/community.crypto/pull/360).
- certificate_complete_chain - do not hang when infinite loop is found (https://github.com/ansible-collections/community.crypto/issues/355, https://github.com/ansible-collections/community.crypto/pull/360).

community.dns
~~~~~~~~~~~~~

- Update Public Suffix List.

community.docker
~~~~~~~~~~~~~~~~

- Fix unintended breaking change caused by `an earlier fix <https://github.com/ansible-collections/community.docker/pull/258>`_ by vendoring the deprecated Python standard library ``distutils.version`` until this collection stops supporting Ansible 2.9 and ansible-base 2.10 (https://github.com/ansible-collections/community.docker/issues/267, https://github.com/ansible-collections/community.docker/pull/269).
- Various modules and plugins - use vendored version of ``distutils.version`` included in ansible-core 2.12 if available. This avoids breakage when ``distutils`` is removed from the standard library of Python 3.12. Note that ansible-core 2.11, ansible-base 2.10 and Ansible 2.9 are right now not compatible with Python 3.12, hence this fix does not target these ansible-core/-base/2.9 versions (https://github.com/ansible-collections/community.docker/pull/258).
- docker connection plugin - replace deprecated ``distutils.spawn.find_executable`` with Ansible's ``get_bin_path`` to find the ``docker`` executable (https://github.com/ansible-collections/community.docker/pull/257).
- docker_container_exec - disallow using the ``chdir`` option for Docker API before 1.35 (https://github.com/ansible-collections/community.docker/pull/253).

community.general
~~~~~~~~~~~~~~~~~

- Various modules and plugins - use vendored version of ``distutils.version`` instead of the deprecated Python standard library ``distutils`` (https://github.com/ansible-collections/community.general/pull/3936).
- alternatives - fix output parsing for alternatives groups (https://github.com/ansible-collections/community.general/pull/3976).
- jail connection plugin - replace deprecated ``distutils.spawn.find_executable`` with Ansible's ``get_bin_path`` to find the executable (https://github.com/ansible-collections/community.general/pull/3934).
- lxd connection plugin - replace deprecated ``distutils.spawn.find_executable`` with Ansible's ``get_bin_path`` to find the ``lxc`` executable (https://github.com/ansible-collections/community.general/pull/3934).
- passwordstore lookup plugin - replace deprecated ``distutils.util.strtobool`` with Ansible's ``convert_bool.boolean`` to interpret values for the ``create``, ``returnall``, ``overwrite``, 'backup``, and ``nosymbols`` options (https://github.com/ansible-collections/community.general/pull/3934).
- say callback plugin - replace deprecated ``distutils.spawn.find_executable`` with Ansible's ``get_bin_path`` to find the ``say`` resp. ``espeak`` executables (https://github.com/ansible-collections/community.general/pull/3934).
- scaleway_user_data - fix double-quote added where no double-quote is needed to user data in scaleway's server (``Content-type`` -> ``Content-Type``) (https://github.com/ansible-collections/community.general/pull/3940).
- slack - add ``charset`` to HTTP headers to avoid Slack API warning (https://github.com/ansible-collections/community.general/issues/3932).
- zone connection plugin - replace deprecated ``distutils.spawn.find_executable`` with Ansible's ``get_bin_path`` to find the executable (https://github.com/ansible-collections/community.general/pull/3934).

community.hrobot
~~~~~~~~~~~~~~~~

- boot - fix incorrect handling of SSH authorized keys (https://github.com/ansible-collections/community.hrobot/issues/32, https://github.com/ansible-collections/community.hrobot/pull/33).

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- ome_device_location - The issue that applies values of the location settings only in lowercase is fixed (https://github.com/dell/dellemc-openmanage-ansible-modules/issues/341)

netbox.netbox
~~~~~~~~~~~~~

- Use individual list items when looking for objects  [#570](https://github.com/netbox-community/ansible_modules/pull/570)

purestorage.flasharray
~~~~~~~~~~~~~~~~~~~~~~

- purefa_certs - Allow a certificate to be imported over an existing SSL certificate
- purefa_eula - Reolve EULA signing issue
- purefa_network - Fix bug introduced with management of FC ports
- purefa_policy - Fix issue with SMB Policy creation

Known Issues
------------

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- idrac_user - Issue(192043) The module may error out with the message ``unable to perform the import or export operation because there are pending attribute changes or a configuration job is in progress``. Wait for the job to complete and run the task again.
- ome_application_alerts_smtp - Issue(212310) - The module does not provide a proper error message if the destination_address is more than 255 characters.
- ome_application_alerts_syslog - Issue(215374) - The module does not provide a proper error message if the destination_address is more than 255 characters.
- ome_device_local_access_configuration - Issue(215035) - The module reports ``Successfully updated the local access setting`` if an unsupported value is provided for the parameter timeout_limit. However, this value is not actually applied on OpenManage Enterprise Modular.
- ome_device_local_access_configuration - Issue(217865) - The module does not display a proper error message if an unsupported value is provided for the user_defined and lcd_language parameters.
- ome_device_network_services - Issue(212681) - The module does not provide a proper error message if unsupported values are provided for the parameters- port_number, community_name, max_sessions, max_auth_retries, and idle_timeout.
- ome_device_power_settings - Issue(212679) - The module errors out with the following message if the value provided for the parameter ``power_cap`` is not within the supported range of 0 to 32767, ``Unable to complete the request because PowerCap does not  exist or is not applicable for the resource URI.``
- ome_smart_fabric_uplink - Issue(186024) - The module does not allow the creation of multiple uplinks of the same name even though it is supported by OpenManage Enterprise Modular. If an uplink is created using the same name as an existing uplink, the existing uplink is modified.

purestorage.flasharray
~~~~~~~~~~~~~~~~~~~~~~

- purefa_admin - Once `max_login` and `lockout` have been set there is currently no way to rest these to zero except through the FlashArray GUI

New Plugins
-----------

Filter
~~~~~~

- community.general.counter - Counts hashable elements in a sequence
- community.hashi_vault.vault_login_token - Extracts the client token from a Vault login response

Lookup
~~~~~~

- community.hashi_vault.vault_login - Perform a login operation against HashiCorp Vault

New Modules
-----------

community.crypto
~~~~~~~~~~~~~~~~

- community.crypto.crypto_info - Retrieve cryptographic capabilities
- community.crypto.openssl_privatekey_convert - Convert OpenSSL private keys

community.general
~~~~~~~~~~~~~~~~~

Identity
^^^^^^^^

Keycloak
........

- community.general.keycloak_realm_info - Allows obtaining Keycloak realm public information via Keycloak API

Packaging
^^^^^^^^^

Language
........

- community.general.cargo - Manage Rust packages with cargo

System
^^^^^^

- community.general.sudoers - Manage sudoers files

community.hashi_vault
~~~~~~~~~~~~~~~~~~~~~

- community.hashi_vault.vault_login - Perform a login operation against HashiCorp Vault

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- dellemc.openmanage.ome_application_network_settings - This module allows you to configure the session inactivity timeout settings
- dellemc.openmanage.ome_application_security_settings - Configure the login security properties
- dellemc.openmanage.ome_device_local_access_configuration - Configure local access settings on OpenManage Enterprise Modular

netbox.netbox
~~~~~~~~~~~~~

- netbox.netbox.netbox_contact - Create, update or delete Contact objects in NetBox
- netbox.netbox.netbox_contact_group - Create, update or delete Contact Group objects in NetBox
- netbox.netbox.netbox_wireless_lan - Create, update or delete Wireless LAN objects in NetBox
- netbox.netbox.netbox_wireless_lan_group - Create, update or delete Wireless LAN Group objects in NetBox
- netbox.netbox.netbox_wireless_link - Create, update or delete Wireless Link objects in NetBox

purestorage.flasharray
~~~~~~~~~~~~~~~~~~~~~~

- purestorage.flasharray.purefa_admin - Configure Pure Storage FlashArray Global Admin settings
- purestorage.flasharray.purefa_saml - Manage FlashArray SAML2 service and identity providers

Unchanged Collections
---------------------

- amazon.aws (still version 2.1.0)
- ansible.netcommon (still version 2.5.0)
- ansible.posix (still version 1.3.0)
- ansible.utils (still version 2.4.3)
- ansible.windows (still version 1.9.0)
- arista.eos (still version 3.1.0)
- awx.awx (still version 19.4.0)
- azure.azcollection (still version 1.10.0)
- check_point.mgmt (still version 2.2.0)
- chocolatey.chocolatey (still version 1.1.0)
- cisco.aci (still version 2.1.0)
- cisco.asa (still version 2.1.0)
- cisco.intersight (still version 1.0.18)
- cisco.ios (still version 2.6.0)
- cisco.iosxr (still version 2.6.0)
- cisco.ise (still version 1.2.1)
- cisco.mso (still version 1.3.0)
- cisco.nso (still version 1.0.3)
- cisco.nxos (still version 2.8.2)
- cisco.ucs (still version 1.6.0)
- cloud.common (still version 2.1.0)
- cloudscale_ch.cloud (still version 2.2.0)
- community.aws (still version 2.1.0)
- community.azure (still version 1.1.0)
- community.ciscosmb (still version 1.0.4)
- community.digitalocean (still version 1.14.0)
- community.fortios (still version 1.0.0)
- community.google (still version 1.0.0)
- community.grafana (still version 1.3.0)
- community.kubernetes (still version 2.0.1)
- community.kubevirt (still version 1.0.0)
- community.libvirt (still version 1.0.2)
- community.mongodb (still version 1.3.2)
- community.mysql (still version 2.3.2)
- community.network (still version 3.0.0)
- community.okd (still version 2.1.0)
- community.postgresql (still version 1.6.0)
- community.rabbitmq (still version 1.1.0)
- community.routeros (still version 2.0.0)
- community.skydive (still version 1.0.0)
- community.sops (still version 1.2.0)
- community.vmware (still version 1.17.0)
- community.windows (still version 1.9.0)
- community.zabbix (still version 1.5.1)
- containers.podman (still version 1.9.0)
- cyberark.conjur (still version 1.1.0)
- cyberark.pas (still version 1.0.13)
- dellemc.enterprise_sonic (still version 1.1.0)
- dellemc.os10 (still version 1.1.1)
- dellemc.os6 (still version 1.0.7)
- dellemc.os9 (still version 1.0.4)
- f5networks.f5_modules (still version 1.13.0)
- fortinet.fortimanager (still version 2.1.4)
- fortinet.fortios (still version 2.1.3)
- frr.frr (still version 1.0.3)
- gluster.gluster (still version 1.0.2)
- google.cloud (still version 1.0.2)
- hetzner.hcloud (still version 1.6.0)
- hpe.nimble (still version 1.1.4)
- ibm.qradar (still version 1.0.3)
- infinidat.infinibox (still version 1.3.3)
- infoblox.nios_modules (still version 1.2.1)
- inspur.sm (still version 1.3.0)
- junipernetworks.junos (still version 2.8.0)
- kubernetes.core (still version 2.2.2)
- mellanox.onyx (still version 1.0.0)
- netapp.aws (still version 21.7.0)
- netapp.azure (still version 21.10.0)
- netapp.cloudmanager (still version 21.12.1)
- netapp.elementsw (still version 21.7.0)
- netapp.ontap (still version 21.14.1)
- netapp.storagegrid (still version 21.9.0)
- netapp.um_info (still version 21.8.0)
- netapp_eseries.santricity (still version 1.2.13)
- ngine_io.cloudstack (still version 2.2.2)
- ngine_io.exoscale (still version 1.0.0)
- ngine_io.vultr (still version 1.1.0)
- openstack.cloud (still version 1.5.3)
- openvswitch.openvswitch (still version 2.1.0)
- ovirt.ovirt (still version 1.6.6)
- purestorage.flashblade (still version 1.9.0)
- sensu.sensu_go (still version 1.12.1)
- servicenow.servicenow (still version 1.0.6)
- splunk.es (still version 1.0.2)
- theforeman.foreman (still version 2.2.0)
- vyos.vyos (still version 2.6.0)
- wti.remote (still version 1.0.3)

v5.1.0
======

.. contents::
  :local:
  :depth: 2

Release Summary
---------------

Release Date: 2021-12-21

`Porting Guide <https://docs.ansible.com/ansible/devel/porting_guides.html>`_

Ansible-core
------------

Ansible 5.1.0 contains Ansible-core version 2.12.1.
This is a newer version than version 2.12.0 contained in the previous Ansible release.

The changes are reported in the combined changelog below.

Changed Collections
-------------------

If not mentioned explicitly, the changes are reported in the combined changelog below.

+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| Collection                    | Ansible 5.0.1 | Ansible 5.1.0 | Notes                                                                                                                        |
+===============================+===============+===============+==============================================================================================================================+
| ansible.netcommon             | 2.4.0         | 2.5.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| ansible.utils                 | 2.4.2         | 2.4.3         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| ansible.windows               | 1.8.0         | 1.9.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| check_point.mgmt              | 2.1.1         | 2.2.0         | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.intersight              | 1.0.17        | 1.0.18        | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.ios                     | 2.5.0         | 2.6.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.iosxr                   | 2.5.0         | 2.6.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.mso                     | 1.2.0         | 1.3.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.nxos                    | 2.7.1         | 2.8.2         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.crypto              | 2.0.1         | 2.0.2         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.digitalocean        | 1.12.0        | 1.14.0        |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.docker              | 2.0.1         | 2.0.2         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.general             | 4.0.2         | 4.2.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.grafana             | 1.2.3         | 1.3.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.hashi_vault         | 2.0.0         | 2.1.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.mysql               | 2.3.1         | 2.3.2         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.postgresql          | 1.5.0         | 1.6.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.vmware              | 1.16.0        | 1.17.0        |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.windows             | 1.8.0         | 1.9.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.zabbix              | 1.5.0         | 1.5.1         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| containers.podman             | 1.8.2         | 1.9.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| dellemc.openmanage            | 4.2.0         | 4.3.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| f5networks.f5_modules         | 1.12.0        | 1.13.0        |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| hpe.nimble                    | 1.1.3         | 1.1.4         | The collection did not have a changelog in this version.                                                                     |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| infinidat.infinibox           | 1.3.0         | 1.3.3         | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| infoblox.nios_modules         | 1.1.2         | 1.2.1         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| junipernetworks.junos         | 2.6.0         | 2.8.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| kubernetes.core               | 2.2.1         | 2.2.2         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| netapp.cloudmanager           | 21.12.0       | 21.12.1       |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| netapp.ontap                  | 21.13.1       | 21.14.1       |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| netapp.storagegrid            | 21.7.0        | 21.9.0        |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| netbox.netbox                 | 3.3.0         | 3.4.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| openvswitch.openvswitch       | 2.0.2         | 2.1.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| ovirt.ovirt                   | 1.6.5         | 1.6.6         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| purestorage.flashblade        | 1.8.1         | 1.9.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| sensu.sensu_go                | 1.12.0        | 1.12.1        |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| t_systems_mms.icinga_director | 1.24.0        | 1.26.0        |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+

Major Changes
-------------

containers.podman
~~~~~~~~~~~~~~~~~

- Add podman_tag module
- Add secrets driver and driver opts support

Minor Changes
-------------

Ansible-core
~~~~~~~~~~~~

- jinja2_native - keep same behavior on Python 3.10.

ansible.netcommon
~~~~~~~~~~~~~~~~~

- Copied the cliconf, httpapi, netconf, and terminal base plugins and NetworkConnectionBase into netcommon. These base plugins may now be imported from netcommmon instead of ansible if a collection depends on netcommon versions newer than this version, allowing features and bugfixes to flow to those collections without upgrading ansible.
- Make ansible_network_os as optional param for httpapi connection plugin.
- Support removal of non-config lines from running config while taking backup.
- `network_cli` - added new option 'become_errors' to determine how privilege escalation failures are handled.

ansible.windows
~~~~~~~~~~~~~~~

- win_dsc - deduplicated error writing code with a new function. No actual error text was changed.
- win_powershell - Added ``$Ansible.Verbosity`` for scripts to adjust code based on the verbosity Ansible is running as

cisco.ios
~~~~~~~~~

- `ios_acls` - feature: Remarks can be configured for ACLs.
- `ios_snmp_server` - New Resource module added.

cisco.iosxr
~~~~~~~~~~~

- Add iosxr_snmp_server resource module.
- Added support for keys net_group, port_group to resolve issue with fact gathering against IOS-XR 6.6.3.

cisco.mso
~~~~~~~~~

- Add container_overlay and underlay_context_profile support to mso_schema_site_vrf_region
- Add description support to various modules
- Add hosted_vrf support to mso_schema_site_vrf_region_cidr_subnet
- Add module mso_schema_validate to check schema validations
- Add private_link_label support to mso_schema_site_anp_epg and mso_schema_site_vrf_region_cidr_subnet
- Add qos_level and Service EPG support to mso_schema_template_anp_epg
- Add qos_level, action and priority support to mso_schema_template_contract_filter
- Add schema and template description support to mso_schema_template
- Add subnet as primary support to mso_schema_template_bd_subnet
- Add support for automatically creating anp structure at site level when using mso_schema_site_anp_epg
- Add support for encap-flood as multi_destination_flooding in mso_schema_template_bd
- Add test file for mso_schema_site_anp, mso_schema_site_anp_epg, mso_schema_template_external_epg_subnet mso_schema_template_filter_entry
- Improve scope attribute documentation in mso_schema_template_external_epg_subnet
- Update Ansible version used in automated testing to v2.9.27, v2.10.16 and addition of v2.11.7 and v2.12.1

cisco.nxos
~~~~~~~~~~

- Add nxos_snmp_server resource module.

community.digitalocean
~~~~~~~~~~~~~~~~~~~~~~

- Set Python 3.9 as the C(python-version) and C(target-python-version) in the integration, sanity, and unit tests for Ansible > 2.9 (3.8 otherwise).
- digital_ocean_droplet - allow the user to override the Droplet action and status polling interval (https://github.com/ansible-collections/community.digitalocean/issues/194).
- digital_ocean_kubernetes - adding support for HA control plane (https://github.com/ansible-collections/community.digitalocean/issues/190).
- digital_ocean_kubernetes_info - switching C(changed=True) to C(changed=False) since getting information is read-only in nature (https://github.com/ansible-collections/community.digitalocean/issues/204).

community.general
~~~~~~~~~~~~~~~~~

- aix_filesystem - calling ``run_command`` with arguments as ``list`` instead of ``str`` (https://github.com/ansible-collections/community.general/pull/3833).
- aix_lvg - calling ``run_command`` with arguments as ``list`` instead of ``str`` (https://github.com/ansible-collections/community.general/pull/3834).
- gitlab - add more token authentication support with the new options ``api_oauth_token`` and ``api_job_token`` (https://github.com/ansible-collections/community.general/issues/705).
- gitlab - clean up modules and utils (https://github.com/ansible-collections/community.general/pull/3694).
- gitlab_group, gitlab_project - add new option ``avatar_path`` (https://github.com/ansible-collections/community.general/pull/3792).
- gitlab_project - add new option ``default_branch`` to gitlab_project (if ``readme = true``) (https://github.com/ansible-collections/community.general/pull/3792).
- hponcfg - revamped module using ModuleHelper (https://github.com/ansible-collections/community.general/pull/3840).
- icinga2 inventory plugin - added the ``display_name`` field to variables (https://github.com/ansible-collections/community.general/issues/3875, https://github.com/ansible-collections/community.general/pull/3906).
- icinga2 inventory plugin - inventory object names are changable using ``inventory_attr`` in your config file to the host object name, address, or display_name fields (https://github.com/ansible-collections/community.general/issues/3875, https://github.com/ansible-collections/community.general/pull/3906).
- ip_netns - calling ``run_command`` with arguments as ``list`` instead of ``str`` (https://github.com/ansible-collections/community.general/pull/3822).
- ipmi_boot - add support for user-specified IPMI encryption key (https://github.com/ansible-collections/community.general/issues/3698).
- ipmi_power - add support for user-specified IPMI encryption key (https://github.com/ansible-collections/community.general/issues/3698).
- iso_extract - calling ``run_command`` with arguments as ``list`` instead of ``str`` (https://github.com/ansible-collections/community.general/pull/3805).
- java_cert - calling ``run_command`` with arguments as ``list`` instead of ``str`` (https://github.com/ansible-collections/community.general/pull/3835).
- jira - add support for Bearer token auth (https://github.com/ansible-collections/community.general/pull/3838).
- keycloak_user_federation - add sssd user federation support (https://github.com/ansible-collections/community.general/issues/3767).
- listen_ports_facts - add support for ``ss`` command besides ``netstat`` (https://github.com/ansible-collections/community.general/pull/3708).
- logentries - calling ``run_command`` with arguments as ``list`` instead of ``str`` (https://github.com/ansible-collections/community.general/pull/3807).
- logstash_plugin - calling ``run_command`` with arguments as ``list`` instead of ``str`` (https://github.com/ansible-collections/community.general/pull/3808).
- lxc_container - calling ``run_command`` with arguments as ``list`` instead of ``str`` (https://github.com/ansible-collections/community.general/pull/3851).
- lxd connection plugin - make sure that ``ansible_lxd_host``, ``ansible_executable``, and ``ansible_lxd_executable`` work (https://github.com/ansible-collections/community.general/pull/3798).
- lxd inventory plugin - support virtual machines (https://github.com/ansible-collections/community.general/pull/3519).
- lxd_container - adds ``type`` option which also allows to operate on virtual machines and not just containers (https://github.com/ansible-collections/community.general/pull/3661).
- module_helper module utils - added decorators ``check_mode_skip`` and ``check_mode_skip_returns`` for skipping methods when ``check_mode=True`` (https://github.com/ansible-collections/community.general/pull/3849).
- monit - calling ``run_command`` with arguments as ``list`` instead of ``str`` (https://github.com/ansible-collections/community.general/pull/3821).
- nmcli - add multiple addresses support for ``ip4`` parameter (https://github.com/ansible-collections/community.general/issues/1088, https://github.com/ansible-collections/community.general/pull/3738).
- nmcli - add multiple addresses support for ``ip6`` parameter (https://github.com/ansible-collections/community.general/issues/1088).
- nmcli - add support for ``eui64`` and ``ipv6privacy`` parameters (https://github.com/ansible-collections/community.general/issues/3357).
- open_iscsi - extended module to allow rescanning of established session for one or all targets (https://github.com/ansible-collections/community.general/issues/3763).
- pacman - add ``stdout`` and ``stderr`` as return values (https://github.com/ansible-collections/community.general/pull/3758).
- python_requirements_info - returns python version broken down into its components, and some minor refactoring (https://github.com/ansible-collections/community.general/pull/3797).
- redfish_command - add ``GetHostInterfaces`` command to enable reporting Redfish Host Interface information (https://github.com/ansible-collections/community.general/issues/3693).
- redfish_command - add ``SetHostInterface`` command to enable configuring the Redfish Host Interface (https://github.com/ansible-collections/community.general/issues/3632).
- svc - calling ``run_command`` with arguments as ``list`` instead of ``str`` (https://github.com/ansible-collections/community.general/pull/3829).
- xattr - calling ``run_command`` with arguments as ``list`` instead of ``str`` (https://github.com/ansible-collections/community.general/pull/3806).
- xfconf - minor refactor on the base class for the module (https://github.com/ansible-collections/community.general/pull/3919).

community.vmware
~~~~~~~~~~~~~~~~

- vmware_datastore_info - added show_tag parameters to allow datastore tags to be read in a uniform way across _info modules  (https://github.com/ansible-collections/community.vmware/pull/1085).
- vmware_guest_disk - Added a new key 'cluster_disk' which allows you to use a filename originating from a VM with an RDM.
- vmware_guest_disk - Added bus_sharing as an option for SCSI devices.
- vmware_guest_disk - Enabled the use of up to 64 disks on a paravirtual SCSI controller when the hardware is version 14 or higher.
- vmware_guest_sendkey - added additional USB scan codes for HOME and END.
- vmware_host_scanhba - add rescan_vmfs parameter to allow rescaning for new VMFS volumes. Also add rescan_hba parameter with default true to allow for not rescaning HBAs as this might be very slow. (https://github.com/ansible-collections/community.vmware/issues/479)
- vmware_host_snmp - implement setting syscontact and syslocation (https://github.com/ansible-collections/community.vmware/issues/1044).
- vmware_rest_client module_util - added function get_tags_for_datastore for convenient tag collection (https://github.com/ansible-collections/community.vmware/pull/1085).

community.windows
~~~~~~~~~~~~~~~~~

- win_disk_facts - Added ``filter`` option to filter returned facts by type of disk information - https://github.com/ansible-collections/community.windows/issues/33
- win_disk_facts - Converted from ``#Requires -Module Ansible.ModuleUtils.Legacy`` to ``#AnsibleRequires -CSharpUtil Ansible.Basic``
- win_iis_virtualdirectory - Added the ``connect_as``, ``username``, and ``password`` options to control the virtual directory authentication - https://github.com/ansible-collections/community.windows/issues/346
- win_power_plan - Added ``guid`` option to specify plan by a unique identifier - https://github.com/ansible-collections/community.windows/issues/310

community.zabbix
~~~~~~~~~~~~~~~~

- Enabled usage of environment variables for modules by adding a fallback lookup in the module_utils/helpers.py - zabbix_common_argument_spec

containers.podman
~~~~~~~~~~~~~~~~~

- Add a second example to podman_pod_module.html

infoblox.nios_modules
~~~~~~~~~~~~~~~~~~~~~

- Added tags 'cloud' and 'networking' in 'galaxy.yaml'
- Following options are made required in the modules | Record | Option made required | | ------ | -------------------- | | A | ipv4addr | | AAAA | ipv6addr | | CNAME | canonical | | MX | mail_exchanger, preference | | PTR | ptrdname |
- Updated 'required' field in modules `#99 <https://github.com/infobloxopen/infoblox-ansible/pull/99>`_

junipernetworks.junos
~~~~~~~~~~~~~~~~~~~~~

- Add junos_routing_options resource module.
- Add junos_snmp_server resource module.

netapp.ontap
~~~~~~~~~~~~

- na_ontap_aggregate - new option ``encryption`` to enable encryption with ZAPI.
- na_ontap_fcp -- Added REST support for FCP
- na_ontap_net_ifgrp - Added REST support to the net ifgrp module.
- na_ontap_net_ifgrp - new REST only options ``from_lag_ports``, ``broadcast_domain`` and ``ipspace`` added.
- na_ontap_net_port - Added REST support to the net port module
- na_ontap_restit - new option ``wait_for_completion`` to support asynchronous operations and wait for job completion.
- na_ontap_volume - Added REST support to the volume module
- na_ontap_volume_efficiency - new option ``storage_efficiency_mode`` for AFF only with 9.10.1 or later.
- na_ontap_vserver_delete role - added set_fact to accept ``netapp_{hostname|username|password}`` or ``hostname,username and password`` variables.
- na_ontap_vserver_delete role - do not report an error if the vserver does not exist.
- na_ontap_vserver_peer - Added REST support to the vserver_peer module

netapp.storagegrid
~~~~~~~~~~~~~~~~~~

- PR2 - allow usage of Ansible module group defaults - for Ansible 2.12+.
- na_sg_grid_gateway - supports load balancer endpoint binding available in StorageGRID 11.5+.
- na_sg_org_container - supports creation of S3 Object Lock buckets available in StorageGRID 11.5+.

netbox.netbox
~~~~~~~~~~~~~

- nb_inventory - Add documentation for use of inventory plugin in Tower/AWX [#648](https://github.com/netbox-community/ansible_modules/pull/648)
- nb_inventory - Cache OpenAPI locally to speed up inventory [#617](https://github.com/netbox-community/ansible_modules/pull/617)
- nb_lookup - Add missing endpoints to nb_lookup [#655](https://github.com/netbox-community/ansible_modules/pull/655)
- netbox_cable - Improve lookup speed on NetBox versions earlier than 3.0.6 [#645](https://github.com/netbox-community/ansible_modules/pull/645)
- netbox_inventory_item - Add label and custom fields to module [#632](https://github.com/netbox-community/ansible_modules/pull/632)
- netbox_provider_network - Add module for handling provider networks [#653](https://github.com/netbox-community/ansible_modules/pull/653)
- netbox_virtual_chassis - Add custom_fields to netbox_virtual_chassis [#657](https://github.com/netbox-community/ansible_modules/pull/657)
- netbox_vm_interface - Add custom fields to module [#637](https://github.com/netbox-community/ansible_modules/pull/637)

openvswitch.openvswitch
~~~~~~~~~~~~~~~~~~~~~~~

- Allows read operation in openvswitch_db module(https://github.com/ansible-collections/openvswitch.openvswitch/pull/88)
- openvswitch modules got support for database socket parameter.

ovirt.ovirt
~~~~~~~~~~~

- info - Enable follow parameter (https://github.com/oVirt/ovirt-ansible-collection/pull/355).
- info - Rename follows to follow parameter and add alias (https://github.com/oVirt/ovirt-ansible-collection/pull/367).
- info - bump deprecate version for fetch_nested and nested_attributes (https://github.com/oVirt/ovirt-ansible-collection/pull/378).
- manageiq - add deprecation info (https://github.com/oVirt/ovirt-ansible-collection/pull/384).
- ovirt_remove_stale_lun - Allow user to remove multiple LUNs (https://github.com/oVirt/ovirt-ansible-collection/pull/357).
- ovirt_remove_stale_lun - Retry "multipath -f" while removing the LUNs (https://github.com/oVirt/ovirt-ansible-collection/pull/382).

purestorage.flashblade
~~~~~~~~~~~~~~~~~~~~~~

- purefb_admin - New module to manage global admin settings
- purefb_connect - Add support for array connections to have bandwidth throttling defined
- purefb_fs - Add support for NFS export policies
- purefb_info - Add NFS export policies and rules
- purefb_info - Show array connections bandwidth throttle information
- purefb_policy - Add NFS export policies, with rules, as a new policy type
- purefb_policy - Add support for Object Store Access Policies, associated rules and user grants
- purefb_policy - New parameter `policy_type` added. For backwards compatability, default to `snapshot` if not provided.

sensu.sensu_go
~~~~~~~~~~~~~~

- Add Sensu Go 6.5.5 Windows metadata
- Add sensu Go 6.6.2 Windows metadata

t_systems_mms.icinga_director
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Add Icinga scheduled downtime module (https://github.com/T-Systems-MMS/ansible-collection-icinga-director/pull/146)
- add option to append arguments to all modules (https://github.com/T-Systems-MMS/ansible-collection-icinga-director/pull/153)

Deprecated Features
-------------------

cisco.nxos
~~~~~~~~~~

- Deprecated nxos_snmp_community module.
- Deprecated nxos_snmp_contact module.
- Deprecated nxos_snmp_host module.
- Deprecated nxos_snmp_location module.
- Deprecated nxos_snmp_traps module.
- Deprecated nxos_snmp_user module.

community.general
~~~~~~~~~~~~~~~~~

- module_helper module utils - deprecated the attribute ``ModuleHelper.VarDict`` (https://github.com/ansible-collections/community.general/pull/3801).

community.hashi_vault
~~~~~~~~~~~~~~~~~~~~~

- Support for Ansible 2.9 and ansible-base 2.10 is deprecated, and will be removed in the next major release (community.hashi_vault 3.0.0) next spring (https://github.com/ansible-community/community-topics/issues/50, https://github.com/ansible-collections/community.hashi_vault/issues/189).
- aws_iam_login auth method - the ``aws_iam_login`` method has been renamed to ``aws_iam``. The old name will be removed in collection version ``3.0.0``. Until then both names will work, and a warning will be displayed when using the old name (https://github.com/ansible-collections/community.hashi_vault/pull/193).

junipernetworks.junos
~~~~~~~~~~~~~~~~~~~~~

- 'router_id' options is deprecated from junos_ospf_interfaces, junos_ospfv2 and junos_ospfv3 resuorce module.

Removed Features (previously deprecated)
----------------------------------------

community.hashi_vault
~~~~~~~~~~~~~~~~~~~~~

- the "legacy" integration test setup has been removed; this does not affect end users and is only relevant to contributors (https://github.com/ansible-collections/community.hashi_vault/pull/191).

Bugfixes
--------

Ansible-core
~~~~~~~~~~~~

- Ansible.ModuleUtils.LinkUtil - Ignore the ``LIB`` environment variable when loading the ``LinkUtil`` code
- ansible-test - Automatic target requirements installation is now based on the target environment instead of the controller environment.
- ansible-test - Fix Python real prefix detection when running in a ``venv`` virtual environment.
- ansible-test - Fix installation and usage of ``pyyaml`` requirement for the ``import`` sanity test for collections.
- ansible-test - Fix traceback in ``import`` sanity test on Python 2.7 when ``pip`` is not available.
- ansible-test - Relocate constants to eliminate symlink.
- ansible-test - Target integration test requirements are now correctly installed for target environments running on the controller.
- ansible-test - Update the ``default`` containers to version 4.1.1, which includes the updated ``import`` sanity test requirements.
- ansible-test - Use the legacy collection loader for ``import`` sanity tests on target-only Python versions.
- set_fact/include_vars correctly handle delegation assignments within loops
- setup - detect docker container with check for ./dockerenv or ./dockinit (https://github.com/ansible/ansible/pull/74349).
- validate_argument_spec - Skip suboption validation if the top level option is an invalid type (https://github.com/ansible/ansible/issues/75612).

ansible.netcommon
~~~~~~~~~~~~~~~~~

- network_cli - Provide clearer error message when a prompt regex fails to compile
- network_cli - fix issue when multiple terminal_initial_(prompt|answer) values are given (https://github.com/ansible-collections/ansible.netcommon/issues/331).

ansible.windows
~~~~~~~~~~~~~~~

- win_command - Use the 24 hour format for the hours of ``start`` and ``end`` - https://github.com/ansible-collections/ansible.windows/issues/303
- win_copy - improve dest folder size detection to handle broken and recursive symlinks as well as inaccesible folders - https://github.com/ansible-collections/ansible.windows/issues/298
- win_dsc - Provide better error message when trying to invoke a composite DSC resource
- win_shell - Use the 24 hour format for the hours of ``start`` and ``end`` - https://github.com/ansible-collections/ansible.windows/issues/303
- win_updates - Fix return value for ``updates`` and ``filtered_updates`` to match original stucture - https://github.com/ansible-collections/ansible.windows/issues/307
- win_updates - Fixed issue when attempting to run ``task.ps1`` with a host that has a restrictive execution policy set through GPO
- win_updates - prevent the host from going to sleep if a low sleep timeout is set - https://github.com/ansible-collections/ansible.windows/issues/310

cisco.ios
~~~~~~~~~

- 'ios_banner' - Bugfix for presence of multiple delimitation chars in the banner's declaration and idempotence improvement.
- Fix ntp_global - remove no_log for key_id under peer and server attributes.
- Fix ntp_global - to handle when attribute value is false.
- `ios_acls` - bugfixes and optimization for ACLs.
- `ios_l2_interfaces` - fix unable to set switchport mode properly.
- `ios_logging_global` - fix host ipv6 commands not parsed correctly.
- `ios_logging_global` - fix wrong ordering of commands fired on replaced state.

cisco.iosxr
~~~~~~~~~~~

- fix issue of local variable 'start_index' referenced before assignment with cisco.iosxr.iosxr_config.
- iosxr_user - replaced custom paramiko sftp and ssh usage with native "copy_file" and "send_command" functions. Fixed issue when ssh key copying doesn't work with network_cli or netconf plugin by deleting "provider" usage. Fixed improper handling of "No such configuration item" when getting data for username section, without that ansible always tried to delete user "No" when purging if there is no any user in config. Fixed one-line admin mode commands not work anymore for ssh key management on IOS XR Software, Version 7.1.3, and add support of "admin" module property (https://github.com/ansible-collections/cisco.iosxr/pull/15)

cisco.mso
~~~~~~~~~

- Add no_log to aws_access_key and secret_key in mso_tenant_site
- Fix MSO HTTP API to work without host, user and password module attribute
- Fix issue with unicast_routing idemptotency in mso_schema_template_bd
- Fix mso_schema_site_anp and mso_schema_site_anp_epg idempotency issue
- Remove sanity ignore files and fix sanity issues that were previously ignored

cisco.nxos
~~~~~~~~~~

- `nxos_ntp_global` - In some cases, there is an extra whitespace in the source-interface line. This patch accounts for this behaviour in config (https://github.com/ansible-collections/cisco.nxos/issues/399).
- nxos_acls - Fix incorrect parsing of remarks if it has 'ip/ipv6 access-list' in it.

community.digitalocean
~~~~~~~~~~~~~~~~~~~~~~

- Update README.md with updated Droplet examples (https://github.com/ansible-collections/community.digitalocean/issues/199).
- digital_ocean_cdn_endpoints - defaulting optional string parameters as strings (https://github.com/ansible-collections/community.digitalocean/issues/205).
- digital_ocean_cdn_endpoints - updating Spaces endpoint for the integration test (https://github.com/ansible-collections/community.digitalocean/issues/205).
- digital_ocean_droplet - ensure that Droplet creation is successful (https://github.com/ansible-collections/community.digitalocean/issues/197).
- digital_ocean_droplet - fixing project assignment for the C(unique_name=False) case (https://github.com/ansible-collections/community.digitalocean/issues/201).
- digital_ocean_droplet - update Droplet examples (https://github.com/ansible-collections/community.digitalocean/issues/199).

community.docker
~~~~~~~~~~~~~~~~

- docker_api connection plugin - avoid passing an unnecessary argument to a Docker SDK for Python call that is only supported by version 3.0.0 or later (https://github.com/ansible-collections/community.docker/pull/243).
- docker_container_exec - ``chdir`` is only supported since Docker SDK for Python 3.0.0. Make sure that this option can only use when 3.0.0 or later is installed, and prevent passing this parameter on when ``chdir`` is not provided to this module (https://github.com/ansible-collections/community.docker/pull/243, https://github.com/ansible-collections/community.docker/issues/242).
- nsenter connection plugin - ensure the ``nsenter_pid`` option is retrieved in ``_connect`` instead of ``__init__`` to prevent a crasher due to bad initialization order (https://github.com/ansible-collections/community.docker/pull/249).
- nsenter connection plugin - replace the use of ``--all-namespaces`` with specific namespaces to support compatibility with Busybox nsenter (used on, for example, Alpine containers) (https://github.com/ansible-collections/community.docker/pull/249).

community.general
~~~~~~~~~~~~~~~~~

- github_repo - ``private`` and ``description`` attributes should not be set to default values when the repo already exists (https://github.com/ansible-collections/community.general/pull/2386).
- icinga2 inventory plugin - handle 404 error when filter produces no results (https://github.com/ansible-collections/community.general/issues/3875, https://github.com/ansible-collections/community.general/pull/3906).
- interfaces_file - fixed the check for existing option in interface (https://github.com/ansible-collections/community.general/issues/3841).
- jira - fixed bug where module returns error related to dictionary key ``body`` (https://github.com/ansible-collections/community.general/issues/3419).
- nmcli - fix returning "changed" when no mask set for IPv4 or IPv6 addresses on task rerun (https://github.com/ansible-collections/community.general/issues/3768).
- nmcli - pass ``flags``, ``ingress``, ``egress`` params to ``nmcli`` (https://github.com/ansible-collections/community.general/issues/1086).
- nrdp callback plugin - fix error ``string arguments without an encoding`` (https://github.com/ansible-collections/community.general/issues/3903).
- opentelemetry_plugin - honour ``ignore_errors`` when a task has failed instead of reporting an error (https://github.com/ansible-collections/community.general/pull/3837).
- pipx - passes the correct command line option ``--include-apps`` (https://github.com/ansible-collections/community.general/issues/3791).
- proxmox - fixed ``onboot`` parameter causing module failures when undefined (https://github.com/ansible-collections/community.general/issues/3844).
- python_requirements_info - fails if version operator used without version (https://github.com/ansible-collections/community.general/pull/3785).
- terraform - fix command options being ignored during planned/plan in function ``build_plan`` such as ``lock`` or ``lock_timeout`` (https://github.com/ansible-collections/community.general/issues/3707, https://github.com/ansible-collections/community.general/pull/3726).

community.grafana
~~~~~~~~~~~~~~~~~

- Fix issue with datasource names that could not contain slashes (#125)

community.mysql
~~~~~~~~~~~~~~~

- mysql_db - Fix mismatch when database name contains a ``%`` character (https://github.com/ansible-collections/community.mysql/pull/227).

community.postgresql
~~~~~~~~~~~~~~~~~~~~

- postgresql_ext - Handle postgresql extension updates through path validation instead of version comparison (https://github.com/ansible-collections/community.postgresql/issues/129).

community.vmware
~~~~~~~~~~~~~~~~

- vmware_guest - when ``customization.password`` is not defined, the Administrator password is made empty instead of setting it to string 'None' (https://github.com/ansible-collections/community.vmware/issues/1017).

community.windows
~~~~~~~~~~~~~~~~~

- win_domain_user - Module now properly captures and reports bad password - https://github.com/ansible-collections/community.windows/issues/316
- win_domain_user - Module now reports user created and changed properly - https://github.com/ansible-collections/community.windows/issues/316
- win_domain_user - The AD user's existing identity is searched using their sAMAccountName name preferentially and falls back to the provided name property instead - https://github.com/ansible-collections/community.windows/issues/344
- win_iis_virtualdirectory - Fixed an issue where virtual directory information could not be obtained correctly when the parameter ``application`` was set

community.zabbix
~~~~~~~~~~~~~~~~

- template - use templateid property when linking templates for ``template.create`` and ``template.update`` API calls.
- zabbix inventory - Moved ZABBIX_VALIDATE_CERTS to correct option, validate_certs.
- zabbix_agent - Create the actual configuration file for Windows setups.
- zabbix_agent - Fix typo for correct using the zabbix_windows_service.exists
- zabbix_agent - tlspsk_auto to support become on Linux and ignore on windows
- zabbix_user - fix zabbix_user require password only on internal.

containers.podman
~~~~~~~~~~~~~~~~~

- Add documentations for generate_systemd
- Don't include shared 'net' if network is host in pods
- Hardcode RT signal numbers
- Remove default value of log-driver
- Support --new in generate_systemd

f5networks.f5_modules
~~~~~~~~~~~~~~~~~~~~~

- Add auto_last_hop parameter to bigip_virtual_server module
- Fix an issue in bigip_virtual_server module that wrongly sets the partition name for profile.
- Fix issue with teem data collection where device was not ready and was returning 404 error when queried for tmos version
- fix for displaying src, checksum and other parameters when running ucs_fetch module
- fix for source capability for bigip_device_auth_ldap module

infoblox.nios_modules
~~~~~~~~~~~~~~~~~~~~~

- Ansible playbook fails to update canonical name of CName Record `#97 <https://github.com/infobloxopen/infoblox-ansible/pull/97>`_
- nios_a_record module - KeyError 'old_ipv4addr' `#79 <https://github.com/infobloxopen/infoblox-ansible/issues/79>`_

junipernetworks.junos
~~~~~~~~~~~~~~~~~~~~~

- Fix ospf router_id overlap issue.

kubernetes.core
~~~~~~~~~~~~~~~

- remove binary file from k8s_cp test suite (https://github.com/ansible-collections/kubernetes.core/pull/298).

netapp.cloudmanager
~~~~~~~~~~~~~~~~~~~

- na_cloudmanager_connector_aws - Fix default ami not based on the region in resource file
- na_cloudmanager_snapmirror - report actual error rather than None with "Error getting destination info".

netapp.ontap
~~~~~~~~~~~~

- fix error where module will fail for ONTAP 9.6 if use_rest was set to auto
- na_ontap_cifs_local_user_modify - KeyError on ``description`` or ``full_name`` with REST.
- na_ontap_cifs_local_user_modify - unexpected argument ``name`` error with REST.
- na_ontap_export_policy - fix error if more than 1 verser matched search name, the wrong uuid could be given
- na_ontap_net_ifgrp - fix error in modify ports with zapi.
- na_ontap_net_routes - metric was not always modified with ZAPI.
- na_ontap_net_routes - support cluster-scoped routes with REST.
- na_ontap_vserver_delete role - report error if ONTAP version is 9.6 or older.

netapp.storagegrid
~~~~~~~~~~~~~~~~~~

- na_sg_grid_account - minor documentation fix.
- na_sg_grid_gateway - existing endpoints matched by ``name`` and ``port``.

netbox.netbox
~~~~~~~~~~~~~

- nb_lookup - Fix documentation of validate_cert [#629](https://github.com/netbox-community/ansible_modules/pull/629)
- netbox_site - Ensure idempotency between NetBox version 2.11 and 3.00 [#631](https://github.com/netbox-community/ansible_modules/pull/631)
- netbox_virtual_chassis - Fix issue with virtual chassis creation [#657](https://github.com/netbox-community/ansible_modules/pull/657)
- netbox_virtual_machine - Ensure idempotency between NetBox version 2.11 and 3.00 [#633](https://github.com/netbox-community/ansible_modules/pull/633)

t_systems_mms.icinga_director
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- added a fix for the new scheduled_downtime module (https://github.com/T-Systems-MMS/ansible-collection-icinga-director/pull/150)

Known Issues
------------

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- idrac_user - Issue(192043) The module may error out with the message ``unable to perform the import or export operation because there are pending attribute changes or a configuration job is in progress``. Wait for the job to complete and run the task again.
- ome_application_alerts_smtp - Issue(212310) - The module does not provide a proper error message if the destination_address is more than 255 characters.
- ome_application_alerts_syslog - Issue(215374) - The module does not provide a proper error message if the destination_address is more than 255 characters.
- ome_device_network_services - Issue(212681) - The module does not provide a proper error message if unsupported values are provided for the parameters- port_number, community_name, max_sessions, max_auth_retries, and idle_timeout.
- ome_device_power_settings - Issue(212679) - The module errors out with the following message if the value provided for the parameter ``power_cap`` is not within the supported range of 0 to 32767, ``Unable to complete the request because PowerCap does not  exist or is not applicable for the resource URI.``
- ome_smart_fabric_uplink - Issue(186024) - The module does not allow the creation of multiple uplinks of the same name even though it is supported by OpenManage Enterprise Modular. If an uplink is created using the same name as an existing uplink, the existing uplink is modified.

New Plugins
-----------

Inventory
~~~~~~~~~

- community.general.xen_orchestra - Xen Orchestra inventory source

Lookup
~~~~~~

- community.general.revbitspss - Get secrets from RevBits PAM server

New Modules
-----------

cisco.ios
~~~~~~~~~

- cisco.ios.ios_snmp_server - snmp_server resource module

cisco.iosxr
~~~~~~~~~~~

- cisco.iosxr.iosxr_snmp_server - Manages snmp-server resource module

cisco.nxos
~~~~~~~~~~

- cisco.nxos.nxos_snmp_server - SNMP Server resource module.

community.general
~~~~~~~~~~~~~~~~~

Net Tools
^^^^^^^^^

- community.general.dnsimple_info - Pull basic info from DNSimple API

Remote Management
^^^^^^^^^^^^^^^^^

Redfish
.......

- community.general.ilo_redfish_config - Sets or updates configuration attributes on HPE iLO with Redfish OEM extensions
- community.general.ilo_redfish_info - Gathers server information through iLO using Redfish APIs

Source Control
^^^^^^^^^^^^^^

Gitlab
......

- community.general.gitlab_branch - Create or delete a branch

community.grafana
~~~~~~~~~~~~~~~~~

- community.grafana.grafana_organization - Manage Grafana Organization

containers.podman
~~~~~~~~~~~~~~~~~

- containers.podman.podman_tag - Add an additional name to a local image

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- dellemc.openmanage.ome_application_alerts_smtp - This module allows to configure SMTP or email configurations
- dellemc.openmanage.ome_application_alerts_syslog - Configure syslog forwarding settings on OpenManage Enterprise and OpenManage Enterprise Modular
- dellemc.openmanage.ome_device_network_services - Configure chassis network services settings on OpenManage Enterprise Modular

junipernetworks.junos
~~~~~~~~~~~~~~~~~~~~~

- junipernetworks.junos.junos_routing_options - Manage routing-options configuration on Junos devices.

netbox.netbox
~~~~~~~~~~~~~

- netbox.netbox.netbox_provider_network - Create, update or delete Provider Network in NetBox

Unchanged Collections
---------------------

- amazon.aws (still version 2.1.0)
- ansible.posix (still version 1.3.0)
- arista.eos (still version 3.1.0)
- awx.awx (still version 19.4.0)
- azure.azcollection (still version 1.10.0)
- chocolatey.chocolatey (still version 1.1.0)
- cisco.aci (still version 2.1.0)
- cisco.asa (still version 2.1.0)
- cisco.ise (still version 1.2.1)
- cisco.meraki (still version 2.5.0)
- cisco.nso (still version 1.0.3)
- cisco.ucs (still version 1.6.0)
- cloud.common (still version 2.1.0)
- cloudscale_ch.cloud (still version 2.2.0)
- community.aws (still version 2.1.0)
- community.azure (still version 1.1.0)
- community.ciscosmb (still version 1.0.4)
- community.dns (still version 2.0.3)
- community.fortios (still version 1.0.0)
- community.google (still version 1.0.0)
- community.hrobot (still version 1.2.1)
- community.kubernetes (still version 2.0.1)
- community.kubevirt (still version 1.0.0)
- community.libvirt (still version 1.0.2)
- community.mongodb (still version 1.3.2)
- community.network (still version 3.0.0)
- community.okd (still version 2.1.0)
- community.proxysql (still version 1.3.0)
- community.rabbitmq (still version 1.1.0)
- community.routeros (still version 2.0.0)
- community.skydive (still version 1.0.0)
- community.sops (still version 1.2.0)
- cyberark.conjur (still version 1.1.0)
- cyberark.pas (still version 1.0.13)
- dellemc.enterprise_sonic (still version 1.1.0)
- dellemc.os10 (still version 1.1.1)
- dellemc.os6 (still version 1.0.7)
- dellemc.os9 (still version 1.0.4)
- fortinet.fortimanager (still version 2.1.4)
- fortinet.fortios (still version 2.1.3)
- frr.frr (still version 1.0.3)
- gluster.gluster (still version 1.0.2)
- google.cloud (still version 1.0.2)
- hetzner.hcloud (still version 1.6.0)
- ibm.qradar (still version 1.0.3)
- inspur.sm (still version 1.3.0)
- mellanox.onyx (still version 1.0.0)
- netapp.aws (still version 21.7.0)
- netapp.azure (still version 21.10.0)
- netapp.elementsw (still version 21.7.0)
- netapp.um_info (still version 21.8.0)
- netapp_eseries.santricity (still version 1.2.13)
- ngine_io.cloudstack (still version 2.2.2)
- ngine_io.exoscale (still version 1.0.0)
- ngine_io.vultr (still version 1.1.0)
- openstack.cloud (still version 1.5.3)
- purestorage.flasharray (still version 1.11.0)
- servicenow.servicenow (still version 1.0.6)
- splunk.es (still version 1.0.2)
- theforeman.foreman (still version 2.2.0)
- vyos.vyos (still version 2.6.0)
- wti.remote (still version 1.0.3)

v5.0.1
======

.. contents::
  :local:
  :depth: 2

Release Summary
---------------

Release Date: 2021-12-02

`Porting Guide <https://docs.ansible.com/ansible/devel/porting_guides.html>`_

Ansible-core
------------

Ansible 5.0.1 contains Ansible-core version 2.12.0.
This is the same version of Ansible-core as in the previous Ansible release.


Major Changes
-------------

- Raised python requirement of the ansible package from >=2.7 to >=3.8 to match ansible-core

Minor Changes
-------------

- A galaxy-requirements.yaml file has been added to `ansible-build-data <https://github.com/ansible-community/ansible-build-data/blob/main/5/galaxy-requirements.yaml>`_. This file can be downloaded and used to install the Ansible collections that are otherwise included in the Ansible package with ``ansible-galaxy collection install -r galaxy-requirements.yaml``.

Unchanged Collections
---------------------

- amazon.aws (still version 2.1.0)
- ansible.netcommon (still version 2.4.0)
- ansible.posix (still version 1.3.0)
- ansible.utils (still version 2.4.2)
- ansible.windows (still version 1.8.0)
- arista.eos (still version 3.1.0)
- awx.awx (still version 19.4.0)
- azure.azcollection (still version 1.10.0)
- check_point.mgmt (still version 2.1.1)
- chocolatey.chocolatey (still version 1.1.0)
- cisco.aci (still version 2.1.0)
- cisco.asa (still version 2.1.0)
- cisco.intersight (still version 1.0.17)
- cisco.ios (still version 2.5.0)
- cisco.iosxr (still version 2.5.0)
- cisco.ise (still version 1.2.1)
- cisco.meraki (still version 2.5.0)
- cisco.mso (still version 1.2.0)
- cisco.nso (still version 1.0.3)
- cisco.nxos (still version 2.7.1)
- cisco.ucs (still version 1.6.0)
- cloud.common (still version 2.1.0)
- cloudscale_ch.cloud (still version 2.2.0)
- community.aws (still version 2.1.0)
- community.azure (still version 1.1.0)
- community.ciscosmb (still version 1.0.4)
- community.crypto (still version 2.0.1)
- community.digitalocean (still version 1.12.0)
- community.dns (still version 2.0.3)
- community.docker (still version 2.0.1)
- community.fortios (still version 1.0.0)
- community.general (still version 4.0.2)
- community.google (still version 1.0.0)
- community.grafana (still version 1.2.3)
- community.hashi_vault (still version 2.0.0)
- community.hrobot (still version 1.2.1)
- community.kubernetes (still version 2.0.1)
- community.kubevirt (still version 1.0.0)
- community.libvirt (still version 1.0.2)
- community.mongodb (still version 1.3.2)
- community.mysql (still version 2.3.1)
- community.network (still version 3.0.0)
- community.okd (still version 2.1.0)
- community.postgresql (still version 1.5.0)
- community.proxysql (still version 1.3.0)
- community.rabbitmq (still version 1.1.0)
- community.routeros (still version 2.0.0)
- community.skydive (still version 1.0.0)
- community.sops (still version 1.2.0)
- community.vmware (still version 1.16.0)
- community.windows (still version 1.8.0)
- community.zabbix (still version 1.5.0)
- containers.podman (still version 1.8.2)
- cyberark.conjur (still version 1.1.0)
- cyberark.pas (still version 1.0.13)
- dellemc.enterprise_sonic (still version 1.1.0)
- dellemc.openmanage (still version 4.2.0)
- dellemc.os10 (still version 1.1.1)
- dellemc.os6 (still version 1.0.7)
- dellemc.os9 (still version 1.0.4)
- f5networks.f5_modules (still version 1.12.0)
- fortinet.fortimanager (still version 2.1.4)
- fortinet.fortios (still version 2.1.3)
- frr.frr (still version 1.0.3)
- gluster.gluster (still version 1.0.2)
- google.cloud (still version 1.0.2)
- hetzner.hcloud (still version 1.6.0)
- hpe.nimble (still version 1.1.3)
- ibm.qradar (still version 1.0.3)
- infinidat.infinibox (still version 1.3.0)
- infoblox.nios_modules (still version 1.1.2)
- inspur.sm (still version 1.3.0)
- junipernetworks.junos (still version 2.6.0)
- kubernetes.core (still version 2.2.1)
- mellanox.onyx (still version 1.0.0)
- netapp.aws (still version 21.7.0)
- netapp.azure (still version 21.10.0)
- netapp.cloudmanager (still version 21.12.0)
- netapp.elementsw (still version 21.7.0)
- netapp.ontap (still version 21.13.1)
- netapp.storagegrid (still version 21.7.0)
- netapp.um_info (still version 21.8.0)
- netapp_eseries.santricity (still version 1.2.13)
- netbox.netbox (still version 3.3.0)
- ngine_io.cloudstack (still version 2.2.2)
- ngine_io.exoscale (still version 1.0.0)
- ngine_io.vultr (still version 1.1.0)
- openstack.cloud (still version 1.5.3)
- openvswitch.openvswitch (still version 2.0.2)
- ovirt.ovirt (still version 1.6.5)
- purestorage.flasharray (still version 1.11.0)
- purestorage.flashblade (still version 1.8.1)
- sensu.sensu_go (still version 1.12.0)
- servicenow.servicenow (still version 1.0.6)
- splunk.es (still version 1.0.2)
- t_systems_mms.icinga_director (still version 1.24.0)
- theforeman.foreman (still version 2.2.0)
- vyos.vyos (still version 2.6.0)
- wti.remote (still version 1.0.3)

v5.0.0
======

.. contents::
  :local:
  :depth: 2

Release Summary
---------------

Release Date: 2021-11-30

`Porting Guide <https://docs.ansible.com/ansible/devel/porting_guides.html>`_

Added Collections
-----------------

- cisco.ise (version 1.2.1)
- cloud.common (version 2.1.0)
- community.ciscosmb (version 1.0.4)
- community.dns (version 2.0.3)
- infoblox.nios_modules (version 1.1.2)
- netapp.storagegrid (version 21.7.0)

Ansible-core
------------

Ansible 5.0.0 contains Ansible-core version 2.12.0.
This is a newer version than version 2.11.0 contained in the previous Ansible release.

The changes are reported in the combined changelog below.

Included Collections
--------------------

If not mentioned explicitly, the changes are reported in the combined changelog below.

+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| Collection                    | Ansible 4.0.0 | Ansible 5.0.0 | Notes                                                                                                                        |
+===============================+===============+===============+==============================================================================================================================+
| amazon.aws                    | 1.5.0         | 2.1.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| ansible.netcommon             | 2.0.2         | 2.4.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| ansible.posix                 | 1.2.0         | 1.3.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| ansible.utils                 | 2.1.0         | 2.4.2         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| ansible.windows               | 1.5.0         | 1.8.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| arista.eos                    | 2.1.1         | 3.1.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| awx.awx                       | 19.0.0        | 19.4.0        | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| azure.azcollection            | 1.5.0         | 1.10.0        | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| check_point.mgmt              | 2.0.0         | 2.1.1         | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.aci                     | 2.0.0         | 2.1.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.asa                     | 2.0.1         | 2.1.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.intersight              | 1.0.15        | 1.0.17        | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.ios                     | 2.0.1         | 2.5.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.iosxr                   | 2.1.0         | 2.5.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.ise                     |               | 1.2.1         | The collection was added to Ansible                                                                                          |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.meraki                  | 2.2.1         | 2.5.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.mso                     | 1.1.0         | 1.2.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.nxos                    | 2.2.0         | 2.7.1         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cloud.common                  |               | 2.1.0         | The collection was added to Ansible                                                                                          |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cloudscale_ch.cloud           | 2.1.0         | 2.2.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.aws                 | 1.5.0         | 2.1.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.azure               | 1.0.0         | 1.1.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.ciscosmb            |               | 1.0.4         | The collection was added to Ansible                                                                                          |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.crypto              | 1.6.2         | 2.0.1         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.digitalocean        | 1.1.1         | 1.12.0        |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.dns                 |               | 2.0.3         | The collection was added to Ansible                                                                                          |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.docker              | 1.5.0         | 2.0.1         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.general             | 3.0.2         | 4.0.2         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.grafana             | 1.2.1         | 1.2.3         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.hashi_vault         | 1.1.3         | 2.0.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.hrobot              | 1.1.1         | 1.2.1         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.kubernetes          | 1.2.1         | 2.0.1         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.libvirt             | 1.0.1         | 1.0.2         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.mongodb             | 1.2.1         | 1.3.2         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.mysql               | 2.1.0         | 2.3.1         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.okd                 | 1.1.2         | 2.1.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.postgresql          | 1.2.0         | 1.5.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.proxysql            | 1.0.0         | 1.3.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.rabbitmq            | 1.0.3         | 1.1.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.routeros            | 1.1.0         | 2.0.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.sops                | 1.0.6         | 1.2.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.vmware              | 1.9.0         | 1.16.0        |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.windows             | 1.3.0         | 1.8.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.zabbix              | 1.3.0         | 1.5.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| containers.podman             | 1.5.0         | 1.8.2         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cyberark.pas                  | 1.0.6         | 1.0.13        | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| dellemc.enterprise_sonic      | 1.0.3         | 1.1.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| dellemc.openmanage            | 3.3.0         | 4.2.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| f5networks.f5_modules         | 1.9.0         | 1.12.0        |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| fortinet.fortimanager         | 2.0.2         | 2.1.4         | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| fortinet.fortios              | 2.0.1         | 2.1.3         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| gluster.gluster               | 1.0.1         | 1.0.2         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| hetzner.hcloud                | 1.4.3         | 1.6.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| infinidat.infinibox           | 1.2.4         | 1.3.0         | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| infoblox.nios_modules         |               | 1.1.2         | The collection was added to Ansible                                                                                          |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| inspur.sm                     | 1.1.4         | 1.3.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| junipernetworks.junos         | 2.1.0         | 2.6.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| kubernetes.core               | 1.2.1         | 2.2.1         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| netapp.aws                    | 21.2.0        | 21.7.0        |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| netapp.azure                  | 21.5.0        | 21.10.0       |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| netapp.cloudmanager           | 21.5.1        | 21.12.0       |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| netapp.elementsw              | 21.3.0        | 21.7.0        |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| netapp.ontap                  | 21.5.0        | 21.13.1       |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| netapp.storagegrid            |               | 21.7.0        | The collection was added to Ansible                                                                                          |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| netapp.um_info                | 21.5.0        | 21.8.0        |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| netapp_eseries.santricity     | 1.2.7         | 1.2.13        |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| netbox.netbox                 | 3.0.0         | 3.3.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| ngine_io.cloudstack           | 2.1.0         | 2.2.2         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| openstack.cloud               | 1.4.0         | 1.5.3         | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| openvswitch.openvswitch       | 2.0.0         | 2.0.2         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| ovirt.ovirt                   | 1.4.2         | 1.6.5         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| purestorage.flasharray        | 1.8.0         | 1.11.0        |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| purestorage.flashblade        | 1.6.0         | 1.8.1         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| sensu.sensu_go                | 1.9.4         | 1.12.0        |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| servicenow.servicenow         | 1.0.5         | 1.0.6         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| t_systems_mms.icinga_director | 1.16.0        | 1.24.0        |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| theforeman.foreman            | 2.0.1         | 2.2.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| vyos.vyos                     | 2.2.0         | 2.6.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| wti.remote                    | 1.0.1         | 1.0.3         | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+

Major Changes
-------------

Ansible-core
~~~~~~~~~~~~

- Python Controller Requirement - Python 3.8 or newer is required for the control node (the machine that runs Ansible) (https://github.com/ansible/ansible/pull/74013)
- ansible-test - All "cloud" plugins which use containers can now be used with all POSIX and Windows hosts. Previously the plugins did not work with Windows at all, and support for hosts created with the ``--remote`` option was inconsistent.
- ansible-test - Collections can now specify controller and target specific integration test requirements and constraints. If provided, they take precedence over the previously available requirements and constraints files.
- ansible-test - Integration tests run with the ``integration`` command can now be executed on two separate hosts instead of always running on the controller. The target host can be one provided by ``ansible-test`` or by the user, as long as it is accessible using SSH.
- ansible-test - Most container features are now supported under Podman. Previously a symbolic link for ``docker`` pointing to ``podman`` was required.
- ansible-test - New ``--controller`` and ``--target`` / ``--target-python`` options have been added to allow more control over test environments.
- ansible-test - Python 3.8 - 3.10 are now required to run ``ansible-test``, thus matching the Ansible controller Python requirements. Older Python versions (2.6 - 2.7 and 3.5 - 3.10) can still be the target for relevant tests.
- ansible-test - SSH port forwarding and redirection is now used exclusively to make container ports available on non-container hosts. When testing on POSIX systems this requires SSH login as root. Previously SSH port forwarding was combined with firewall rules or other port redirection methods, with some platforms being unsupported.
- ansible-test - Sanity tests always run in isolated Python virtual environments specific to the requirements of each test. The environments are cached.
- ansible-test - Sanity tests are now separated into two categories, controller and target. All tests except ``import`` and ``compile`` are controller tests. The controller tests always run using the same Python version used to run ``ansible-test``. The target tests use the Python version(s) specified by the user, or all available Python versions.
- ansible-test - Sanity tests now use fully pinned requirements that are independent of each other and other test types.
- ansible-test - Tests run with the ``centos6`` and ``default`` test containers now use a PyPI proxy container to access PyPI when Python 2.6 is used. This allows tests running under Python 2.6 to continue functioning even though PyPI is discontinuing support for non-SNI capable clients.
- ansible-test - The ``future-import-boilerplate`` and ``metaclass-boilerplate`` sanity tests are limited to remote-only code. Additionally, they are skipped for collections which declare no support for Python 2.x.
- ansible-test - The ``import`` and ``compile`` sanity tests limit remote-only Python version checks to remote-only code.
- ansible-test - Unit tests for controller-only code now require Python 3.8 or later.
- ansible-test - Version neutral sanity tests now require Python 3.8 or later.
- junit callback - The ``junit_xml`` and ``ordereddict`` Python modules are no longer required to use the ``junit`` callback plugin.

amazon.aws
~~~~~~~~~~

- amazon.aws collection - Due to the AWS SDKs announcing the end of support for Python less than 3.6 (https://boto3.amazonaws.com/v1/documentation/api/1.17.64/guide/migrationpy3.html) this collection now requires Python 3.6+ (https://github.com/ansible-collections/amazon.aws/pull/298).
- amazon.aws collection - The amazon.aws collection has dropped support for ``botocore<1.18.0`` and ``boto3<1.15.0``. Most modules will continue to work with older versions of the AWS SDK, however compatability with older versions of the SDK is not guaranteed and will not be tested. When using older versions of the SDK a warning will be emitted by Ansible (https://github.com/ansible-collections/amazon.aws/pull/502).
- ec2_instance - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.ec2_instance``.
- ec2_instance_info - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.ec2_instance_info``.
- ec2_vpc_endpoint - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.ec2_vpc_endpoint``.
- ec2_vpc_endpoint_facts - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.ec2_vpc_endpoint_info``.
- ec2_vpc_endpoint_info - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.ec2_vpc_endpoint_info``.
- ec2_vpc_endpoint_service_info - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.ec2_vpc_endpoint_service_info``.
- ec2_vpc_igw - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.ec2_vpc_igw``.
- ec2_vpc_igw_facts - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.ec2_vpc_igw_facts``.
- ec2_vpc_igw_info - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.ec2_vpc_igw_info``.
- ec2_vpc_nat_gateway - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.ec2_vpc_nat_gateway``.
- ec2_vpc_nat_gateway_facts - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.ec2_vpc_nat_gateway_info``.
- ec2_vpc_nat_gateway_info - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.ec2_vpc_nat_gateway_info``.
- ec2_vpc_route_table - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.ec2_vpc_route_table``.
- ec2_vpc_route_table_facts - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.ec2_vpc_route_table_facts``.
- ec2_vpc_route_table_info - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.ec2_vpc_route_table_info``.

cloudscale_ch.cloud
~~~~~~~~~~~~~~~~~~~

- Add custom_image module

community.aws
~~~~~~~~~~~~~

- community.aws collection - The community.aws collection has dropped support for ``botocore<1.18.0`` and ``boto3<1.15.0`` (https://github.com/ansible-collections/community.aws/pull/711). Most modules will continue to work with older versions of the AWS SDK, however compatability with older versions of the SDK is not guaranteed and will not be tested. When using older versions of the SDK a warning will be emitted by Ansible (https://github.com/ansible-collections/amazon.aws/pull/442).

community.general
~~~~~~~~~~~~~~~~~

- bitbucket_* modules - ``client_id`` is no longer marked as ``no_log=true``. If you relied on its value not showing up in logs and output, please mark the whole tasks with ``no_log: true`` (https://github.com/ansible-collections/community.general/pull/2045).

community.kubernetes
~~~~~~~~~~~~~~~~~~~~

- redirect everything from ``community.kubernetes`` to ``kubernetes.core`` (https://github.com/ansible-collections/community.kubernetes/pull/425).

community.okd
~~~~~~~~~~~~~

- update to use kubernetes.core 2.0 (https://github.com/openshift/community.okd/pull/93).

community.postgresql
~~~~~~~~~~~~~~~~~~~~

- postgresql_query - the default value of the ``as_single_query`` option will be changed to ``yes`` in community.postgresql 2.0.0 (https://github.com/ansible-collections/community.postgresql/issues/85).

community.vmware
~~~~~~~~~~~~~~~~

- vmware_object_custom_attributes_info - added a new module to gather custom attributes of an object (https://github.com/ansible-collections/community.vmware/pull/851).

containers.podman
~~~~~~~~~~~~~~~~~

- Add systemd generation for pods
- Generate systemd service files for containers

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- idrac_server_config_profile - Added support for exporting and importing Server Configuration Profile through HTTP/HTTPS share.
- ome_device_group - Added support for adding devices to a group using the IP addresses of the devices and group ID.
- ome_firmware - Added option to stage the firmware update and support for selecting components and devices for baseline-based firmware update.
- ome_firmware_baseline - Module supports check mode, and allows the modification and deletion of firmware baselines.
- ome_firmware_catalog - Module supports check mode, and allows the modification and deletion of firmware catalogs.

fortinet.fortios
~~~~~~~~~~~~~~~~

- Add real-world use cases in the example section for some configuration modules.
- Collect the current configurations of the modules and convert them into playbooks.
- Improve ``fortios_configuration_fact`` to use multiple selectors concurrently.
- New module fortios_monitor_fact.
- Support FortiOS 7.0.1.
- Support Fortios 7.0.
- Support Log APIs.
- Support ``check_mode`` in all cofigurationAPI-based modules.
- Support filtering for fact gathering modules ``fortios_configuration_fact`` and ``fortios_monitor_fact``.
- Support member operation (delete/add extra members) on an object that has a list of members in it.
- Support moving policy in ``firewall_central_snat_map``.
- Support selectors feature in ``fortios_monitor_fact`` and ``fortios_log_fact``.
- Unify schemas for monitor API.

gluster.gluster
~~~~~~~~~~~~~~~

- enable client.ssl,server.ssl before starting the gluster volume (https://github.com/gluster/gluster-ansible-collection/pull/19)

hetzner.hcloud
~~~~~~~~~~~~~~

- Introduction of placement groups

kubernetes.core
~~~~~~~~~~~~~~~

- k8s - deprecate merge_type=json. The JSON patch functionality has never worked (https://github.com/ansible-collections/kubernetes.core/pull/99).
- k8s_json_patch - split JSON patch functionality out into a separate module (https://github.com/ansible-collections/kubernetes.core/pull/99).
- replaces the openshift client with the official kubernetes client (https://github.com/ansible-collections/kubernetes.core/issues/34).

netapp.cloudmanager
~~~~~~~~~~~~~~~~~~~

- Adding stage environment to all modules in cloudmanager

netbox.netbox
~~~~~~~~~~~~~

- packages is now a required Python package and gets installed via Ansible 2.10+.

openvswitch.openvswitch
~~~~~~~~~~~~~~~~~~~~~~~

- By mistake we tagged the repo to 2.0.0 and as it wasn't intended and cannot be reverted we're releasing 2.0.1 to make the community aware of the major version update.

ovirt.ovirt
~~~~~~~~~~~

- remove_stale_lun - Add role for removing stale LUN (https://bugzilla.redhat.com/1966873).

Minor Changes
-------------

Ansible-core
~~~~~~~~~~~~

- Add ``end_batch`` meta task.
- Allow connection and become passwords to be set by file/executable script. Also document this was already the case for vault.
- CLI - Remove ``__requires__`` attribute for ``pkg_resources``
- Collections can define action_groups in ``meta/runtime.yml``.
- Introduce a config option to enable/disable emitting warning about Jinja2 version being old for ``jinja2_native``. The option is on by default, only in CI it is off.
- Make the code structure of ansible-doc's generic snippet feature more maintainable.
- On RHEL 9, CentOS Stream 9 etc., use /usr/bin/python3 as the default interpreter; /usr/libexec/platform-python is just a backwards-compatibility symbolic link there.
- PowerShell - Added support for optional module_util imports by scanning for ``-Optional`` at the end of the import declaration
- Python 2.6 Target Support - Deprecate Python 2.6 for targets, requiring Python 2.7 or newer. ``ansible-core==2.13`` will drop support for Python 2.6. (https://github.com/ansible/ansible/pull/74165)
- Task - Add a resolved_action attribute for Task objects to get the final resolved plugin.
- Templar - remove ``_fail_on_lookup_errors`` and ``_fail_on_filter_errors`` instance variables that were never used. (https://github.com/ansible/ansible/pull/73785)
- The AnsiballZ Python wrapper now changes the working directory to ``~`` or ``/`` if the current one is not accessible. This allows become to drop privileges on macOS when using pipelining.
- Update test container ansible-core-test-container to version 3.6.0
- Update test container ansible-core-test-container to version 3.7.0
- Update test container default-test-container to version 3.6.0
- Update test container default-test-container to version 3.7.0
- Update vendored copy of ``six`` to 1.16.0 to eliminate warnings for deprecated python loader methods in Python 3.10+ (https://github.com/ansible/ansible/issues/74659)
- Update vendored copy of distro to 1.6.0
- Vendor ``distutils.version`` due to it's deprecation in Python 3.10 and impending removal in Python 3.12 (https://github.com/ansible/ansible/issues/74599)
- YAML parsing - Create common utils for loading and dumping YAML that prefer the C extensions if available
- ``include_role`` - Allow use of ``omit`` in the ``from_*`` arguments (https://github.com/ansible/ansible/issues/66349)
- ``uri``/``get_url`` - Expose ``unredirected_headers`` to modules to allow user control
- `ansible.plugins.callback.CallbackBase.host_label()` has been factored out as a static method (https://github.com/ansible/ansible/pull/73814).
- action_groups can include actions from other groups by using the special ``metadata`` dictionary field.
- add a quick short circuit when checking if a string is a template to improve performance on large strings (https://github.com/ansible/ansible/issues/74336)
- add host label to retry print statements
- added new function to module utils to choose best possible locale.
- adds the ``undef`` keyword to the templating environment. This allows for directly creating Undefined values in templates. It is most useful for providing a hint for variables which must be overridden.
- ansbile-doc now also shows snippets for inventory and lookup, adding to existing modules.
- ansible adhoc, clarified the help to some options, also added some comments to code.
- ansible-cli - remove unnecessary trailing space in ``ansible --version`` (https://github.com/ansible/ansible/issues/74875).
- ansible-config can now list and dump for specific documentable plugins by specifying them in the command line
- ansible-config has new 'init' option to create, highly commented, example configurations as ini (ansible.cfg), environment variables (shell) or Ansible variable files (YAML)
- ansible-config now supports displaying plugin configuration info.
- ansible-doc - ``version_added`` in ``attributes`` now comes with ``version_added_collection`` (https://github.com/ansible/ansible/pull/74602).
- ansible-doc - show ``version_added`` for the plugin/module itself in text output, and improve ``version_added`` formatting (https://github.com/ansible/ansible/pull/73602).
- ansible-doc now supports 'attributes' for plugins as per proposal.
- ansible-doc pretty cli options output.
- ansible-doc, improve handling of rstisms, try to make the display more meaningfull for the terminal users.
- ansible-galaxy - Allow specification of client_id override value for Keycloak Token (https://github.com/ansible/ansible/issues/75593).
- ansible-galaxy - Allow validate_certs to be configured for individual Galaxy servers (https://github.com/ansible/ansible/issues/75677).
- ansible-galaxy - Installing a collection from a git repository without specifying a version (or using the version ``HEAD``) will clone the repository using --depth=1.
- ansible-galaxy - Non-HTTP exceptions from Galaxy servers are now a warning and only fatal if the collection to download|install|verify is not available from any of the servers (https://github.com/ansible/ansible/issues/75443).
- ansible-test - A new ``base`` test container is available. It is similar to the ``default`` test container, but contains no pre-installed Python packages other than ``pip`` and its dependencies.
- ansible-test - Add RHEL 8.4 as a remote.
- ansible-test - Add ``--prime-venvs`` option to create virtual environments without running tests.
- ansible-test - Add constraint for ``decorator`` for Python versions prior to 3.5.
- ansible-test - Add support for Windows Server 2022.
- ansible-test - Add support for an ansible-test configuration file in collections under ``tests/config.yml``.
- ansible-test - Add support for testing with Python 3.10.
- ansible-test - Added a ``--prime-containers`` option to support downloading containers without running tests.
- ansible-test - Adding DigitalOcean cloud support to ansible-test (https://github.com/ansible/ansible/pull/74222).
- ansible-test - All "cloud" plugins have been refactored for more consistency. For those that use docker containers, management of the containers has been standardized.
- ansible-test - All "cloud" plugins now use fixed hostnames and ports in tests. Previously some tests used IP addresses and/or randomly assigned ports.
- ansible-test - Changes made to the ``hosts`` file on test systems are now done using an Ansible playbook for both POSIX and Windows systems. Changes are applied before a test target runs and are reverted after the test target finishes.
- ansible-test - Clean up code in the cloud plugins.
- ansible-test - Collections can declare their remote-only code (modules/module_utils and related tests) as controller-only.
- ansible-test - Collections can limit the Python versions used for testing their remote-only code (modules/module_utils and related tests).
- ansible-test - Command line help has been updated to hide the ``--remote`` option (and related options) when the user lacks an API key to use the feature.
- ansible-test - Constraints provided by ``ansible-test`` for Python package installs have been reduced.
- ansible-test - Default settings are now applied to unknown versions of known ``--remote`` platforms.
- ansible-test - Distribution specific test containers have been updated to version 3.0.0.
- ansible-test - Environment checking (``pip``, ``python``, ``~/.ssh/known_hosts``, etc.) is no longer performed when running integration tests.
- ansible-test - Environment variables exposed by "cloud" plugins are now available to the controller for role based tests. Previously only script based tests had access to the exposed environment variables.
- ansible-test - Fedora 32 and 33 (``fedora32`` and ``fedora33``) containers have been updated and now allow for ssh in more container environments.
- ansible-test - Fedora 34 (``fedora34``) container has been added.
- ansible-test - Installation of ``cryptography`` no longer occurs when it is already installed. This avoids downgrading existing OS packages.
- ansible-test - Minor code cleanup.
- ansible-test - More efficient string splitting.
- ansible-test - Most scripts used internally by ``ansible-test`` no longer have a shebang or the executable bit set.
- ansible-test - Move code from ``_data`` directory to ``_util`` directory.
- ansible-test - Relocate change classification code.
- ansible-test - Remove CI provider support for Shippable, now that the service has been discontinued.
- ansible-test - Remove check for legacy ``core`` and ``extras`` directories.
- ansible-test - Remove deprecated container ``fedora32``.
- ansible-test - Remove deprecated remote platforms ``freebsd/11.4`` and ``rhel/8.3```.
- ansible-test - Removed the warning filter for ``PyYAML`` in the ``import`` sanity test.
- ansible-test - Removed unused pip constraints. Collections may need to add their own constraints if they depended on any which were removed.
- ansible-test - Reorganize code for individual commands.
- ansible-test - Reorganize integration test implementation by command.
- ansible-test - Rewrite the ``compile`` sanity test to improve error handling and support Python 3.10.
- ansible-test - Sanity test warnings relating to Python version support have been improved.
- ansible-test - Set minimum version constraints for ``pytest``.
- ansible-test - Split out shell command implementation.
- ansible-test - The "injector" scripts are now generated at runtime to avoid issues with symlinks and shebangs.
- ansible-test - The HTTP Tester can now be used without the ``--docker`` or `--remote`` options. It still requires use of the ``docker`` command to run the container.
- ansible-test - The HTTP Tester has been converted to a "cloud" plugin and can now be requested using the ``cloud/httptester`` alias. The original ``needs/httptester`` alias is still supported for backwards compatibility.
- ansible-test - The ``--docker-keep-git`` option (used only for testing ansible-core) has been renamed to ``--keep-git``.
- ansible-test - The ``--python`` option can be used without another delegation option such as the ``--venv`` or ``--docker`` options.
- ansible-test - The ``ansible-test coverage`` commands ``combine``, ``report``, ``html`` and ``xml`` now support delegation.
- ansible-test - The ``default`` test container has been updated to version 3.4.0 and now uses Python 3.9 by default instead of Python 3.6.
- ansible-test - The ``docker run`` option ``--link`` is no longer used to connect test containers. As a result, changes are made to the ``/etc/hosts`` file as needed on all test containers. Previously containers which were used with the ``--link`` option did not require changes to the ``/etc/hosts`` file.
- ansible-test - The ``import`` sanity test now requires that Ansible modules guard instantiation of ``AnsibleModule`` with a ``if __name__ == '__main__'`` conditional, or equivalent logic.
- ansible-test - The ``import`` sanity test now requires that non-modules do not instantiate ``AnsibleModule`` on import.
- ansible-test - The ``validate-modules`` sanity test codes ``ansible-deprecated-module`` and ``collection-deprecated-module`` have been added.
- ansible-test - The ``validate-modules`` sanity test codes ``last-line-main-call``, ``missing-if-name-main`` and ``missing-main-call`` have been removed.
- ansible-test - The ``validate-modules`` sanity test no longer enforces the ``missing-if-name-main``, ``last-line-main-call`` or ``missing-main-call`` checks on non-deleted Ansible modules. Modules are still required to instantiate ``AnsibleModule`` when ``__name__ == '__main__'``.
- ansible-test - Unit tests are now run in separate contexts (``controller``, ``modules``, ``module_utils``), each using separate invocations of ``pytest``.
- ansible-test - Unit tests other than ``modules`` and ``module_utils`` are now run only on Python versions supported by the controller (Python 3.8+).
- ansible-test - Update ``typed-ast`` constraint to version 1.4.3 for compatibility with Python 3.10.
- ansible-test - Update distribution test containers from version 2.0.1 to 2.0.2.
- ansible-test - Update the Ansible Core and Ansible Collection default test containers to 3.2.0 and 3.2.2 respectively.
- ansible-test - Update the ``base`` and ``default`` containers from Python 3.10.0rc2 to 3.10.0.
- ansible-test - Update the ``import`` sanity test to avoid a new warning in Python 3.10.
- ansible-test - Update the ``runtime-metadata`` sanity test to handle a new warning on Python 3.10.
- ansible-test - Updated the ``default`` containers to version 4.0.1.
- ansible-test - Updated the help message for failed tests in the ``azure`` test plugin.
- ansible-test - Upgrade ``pylint`` to version 2.9.3 and update its dependencies to the latest versions as well.
- ansible-test - Using an unknown ``--docker`` or ``--remote`` environment now requires specifying a Python version.
- ansible-test - add freebsd/13.0 as a remote option.
- ansible-test - aws creates and exposes a new tiny_prefix variable to provide a shorter prefix for the AWS tests.
- ansible-test - display recent ``ssh`` debug logs after connection failures (https://github.com/ansible/ansible/pull/75374)
- ansible-test - validate-modules now properly checks ``attributes`` for plugins (https://github.com/ansible/ansible/pull/74602).
- ansible-test - virtualenv-isolated.sh is no longer provided. Prefer virtualenv.sh in its place.
- ansible-test validate-modules - enforce that ``_info`` and ``_facts`` modules set ``supports_check_mode=True`` (https://github.com/ansible/ansible/pull/75324).
- ansible-vault - remove support for ``PyCrypto`` (https://github.com/ansible/ansible/issues/72646)
- apt - added an ``allow_downgrade`` option to enable safe downgrade of packages without using ``force`` which doesn't verify signatures (https://github.com/ansible/ansible/issues/29451, https://github.com/ansible/ansible/pull/74852).
- apt, added a 'lock_timeout' to be more resilient when encountering the apt db already locked and handle it w/o haveing to rerun task.
- async tasks - the use of the task-level ``ANSIBLE_ASYNC_DIR`` variable within ``environment:`` is no longer valid. Use the shell configuration variable ``async_dir`` instead.
- async_wrapper, better reporting on timeout, slight refactor on reporting itself.
- basic module_util - Clean up ``selinux`` compat import.
- blockinfile - Remove unused code for Ansible 1.x.
- cache base - More efficient string splitting.
- callback API - implemented ``v2_runner_on_async_ok`` and ``v2_runner_on_async_failed`` callbacks (https://github.com/ansible/ansible/pull/74953).
- cli scripts - remove trailing blank space in help after newline when outputting.
- collection - match skip message as per role installation.
- command - update the user warning message to point out command name (https://github.com/ansible/ansible/pull/74475).
- config lookup now can handle plugin settings.
- config, default site for ansible-core is now under /ansbile-core/.
- connection base - Avoid using deprecated ``@abstractproperty`` decorator.
- constructed - a new options ``trailing_separator`` and ``default_value`` to deal with key's value empty on keyed group.
- cron - ``name`` is now a required parameter always
- cron - ``reboot`` parameter has been dropped in favor of ``special_time: reboot``
- cron, removed previously deprecated 'reboot' and now requires either 'name' as unique identifier.
- default callback plugin - displays output for ``v2_runner_on_async_ok`` and ``v2_runner_on_async_failed`` callbacks.
- deprecate ``_remote_checksum()`` and remove all internal uses (https://github.com/ansible/ansible/pull/74848)
- dnf - Add ``cacheonly`` option (https://github.com/ansible/ansible/issues/69397).
- dnf - allow for ``download_only`` to be run without root privileges (https://github.com/ansible/ansible/issues/75530)
- encrypt - add new parameter ``ident`` to specify version of BCrypt algorithm to be used (https://github.com/ansible/ansible/issues/74571).
- fact cache - Remove deprecated backwards compatibility shim for the FactCache `update` method to accept multiple arguments.
- fact cache - Remove the deprecated location for FactCache. Import FactCache from `ansible.vars.fact_cache` instead.
- facts - add fiber channel facts for HP-UX (https://github.com/ansible/ansible/pull/57406)
- galaxy - support role artifact download from API response ``download_url`` location (https://github.com/ansible/ansible/issues/73103).
- get_distribution - ``lib.ansible.module_utils.common.sys_info.get_distribution`` now returns distribution information for all platforms not just Linux (https://github.com/ansible/ansible/issues/17587)
- get_distribution_version - ``lib.ansible.module_utils.common.sys_info.get_distribution_version`` now returns the version for all platfroms not just Linux (https://github.com/ansible/ansible/issues/17587)
- git - Add ``accept_newhostkey`` option (https://github.com/ansible/ansible/issues/69846).
- hostname - add support RedOS (https://github.com/ansible/ansible/issues/74779).
- import_role - Template tasks_from, vars_from, defaults_from, and handlers_from with --extra-vars (https://github.com/ansible/ansible/issues/69097).
- include_vars - add ``hash_behaviour`` option (https://github.com/ansible/ansible/pull/72944).
- ini - added new parameter ``allow_no_value`` to ini lookup plugin (https://github.com/ansible/ansible/issues/50594).
- ini lookup - add case sensitive option (https://github.com/ansible/ansible/issues/74601)
- interpreter discovery - allow the default list of ``INTERPRETER_PYTHON_FALLBACK`` to be changed using a variable
- interpreter discovery - prefer Python 3 over Python 2
- inventory plugins - Remove the deprecated cache interface. Set top level keys in the inventory plugin's `_cache` attribute (a dictionary) instead.
- jinja2_native - short-circuit ``ast.literal_eval`` for non-string values
- module_utils distro - when a 'distro' package/module is in PYTHONPATH but isn't the real 'distro' package/module that we expect, gracefully fall back to our own bundled distro.
- modules - add Anolis distro in hostname.py. project website https://openanolis.org/
- move all builtin modules to use the best possible locale function instead of hardcoding 'C'.
- password - add new parameter ``ident`` to specify version of BCrypt algorithm to be used (https://github.com/ansible/ansible/issues/74571).
- password - add new parameter ``seed`` in lookup plugin (https://github.com/ansible/ansible/pull/69775).
- password_hash uses passlib default if option isn't set
- playbook - Error if a playbook is an empty list instead of just skipping
- playbook - Error if using ``include`` instead of ``import_playbook``
- replaced examples/ansible.cfg with instructions on how to generate an up to date copy.
- service - add description how service module works internally (https://github.com/ansible/ansible/issues/74507).
- service_facts now handles more states/statuses from systemd and in a more reliable way (failed, not-found, masked).
- setup - add ``epoch_int`` option to date_time facts (https://github.com/ansible/ansible/pull/73822).
- ssh - added pkcs11 support by adding the pkcs11_provider option in the ssh connection module. (https://www.github.com/ansible/ansible/pull/32829)
- ssh connection, can not configure ssh_transfer_method with a variable.
- ssh connection, ssh_transfer_method is now configurable via variable.
- subelements lookup - Use generator in instance type check.
- tempfile - Remove unnecessary conditional for creating a temporary directory.
- template - Add comment attributes (``comment_start_string`` and ``comment_end_string``)
- unicode utils - Fix ``__all__`` which was incorrectly declared as a string instead of a tuple.
- user - Add ``umask`` option (https://github.com/ansible/ansible/issues/40359).
- user module - Remove unused code.
- validation testcases for check_* APIs (https://github.com/ansible/ansible/issues/55994).
- winrm - Allow explicit environment variables to be passed through to the ``kinit`` call for Kerberos authentication
- yaml dumper - YAML representer for AnsibleUndefined (https://github.com/ansible/ansible/issues/75072).
- yum - Add ``cacheonly`` option (https://github.com/ansible/ansible/issues/69397).

amazon.aws
~~~~~~~~~~

- aws_ec2 - use a generator rather than list comprehension (https://github.com/ansible-collections/amazon.aws/pull/465).
- aws_s3 - Tests for compatability with older versions of the AWS SDKs have been removed (https://github.com/ansible-collections/amazon.aws/pull/442).
- aws_s3 - add ``tags`` and ``purge_tags`` features for an S3 object (https://github.com/ansible-collections/amazon.aws/pull/335)
- aws_s3 - new mode to copy existing on another bucket (https://github.com/ansible-collections/amazon.aws/pull/359).
- aws_secret - added support for gracefully handling deleted secrets (https://github.com/ansible-collections/amazon.aws/pull/455).
- aws_service_ip_ranges - add new option ``ipv6_prefixes`` to get only IPV6 addresses and prefixes for Amazon services (https://github.com/ansible-collections/amazon.aws/pull/430)
- aws_ssm - add "on_missing" and "on_denied" option (https://github.com/ansible-collections/amazon.aws/pull/370).
- cloudformation - Tests for compatability with older versions of the AWS SDKs have been removed (https://github.com/ansible-collections/amazon.aws/pull/442).
- cloudformation - fix detection when there are no changes. Sometimes when there are no changes, the change set will have a status FAILED with StatusReason No updates are to be performed (https://github.com/ansible-collections/amazon.aws/pull/507).
- ec2_ami - add check_mode support (https://github.com/ansible-collections/amazon.aws/pull/516).
- ec2_ami - ensure tags are propagated to the snapshot(s) when creating an AMI (https://github.com/ansible-collections/amazon.aws/pull/437).
- ec2_ami - use module_util helper for tagging AMIs (https://github.com/ansible-collections/amazon.aws/pull/520).
- ec2_ami - when creating an AMI from an instance pass the tagging options at creation time (https://github.com/ansible-collections/amazon.aws/pull/551).
- ec2_elb_lb - module renamed to ``elb_classic_lb`` (https://github.com/ansible-collections/amazon.aws/pull/377).
- ec2_eni - add check mode support (https://github.com/ansible-collections/amazon.aws/pull/534).
- ec2_eni - fix idempotency when ``security_groups`` attribute is specified (https://github.com/ansible-collections/amazon.aws/pull/337).
- ec2_eni - timeout increased when waiting for ENIs to finish detaching (https://github.com/ansible-collections/amazon.aws/pull/501).
- ec2_eni - use module_util helper for tagging ENIs (https://github.com/ansible-collections/amazon.aws/pull/522).
- ec2_group - Tests for compatability with older versions of the AWS SDKs have been removed (https://github.com/ansible-collections/amazon.aws/pull/442).
- ec2_group - use a generator rather than list comprehension (https://github.com/ansible-collections/amazon.aws/pull/465).
- ec2_group - use system ipaddress module, available with Python >= 3.3, instead of vendored copy (https://github.com/ansible-collections/amazon.aws/pull/461).
- ec2_instance - Tests for compatability with older versions of the AWS SDKs have been removed (https://github.com/ansible-collections/amazon.aws/pull/442).
- ec2_instance - add ``throughput`` parameter for gp3 volume types (https://github.com/ansible-collections/amazon.aws/pull/433).
- ec2_instance - add support for controlling metadata options (https://github.com/ansible-collections/amazon.aws/pull/414).
- ec2_instance - remove unnecessary raise when exiting with a failure (https://github.com/ansible-collections/amazon.aws/pull/460).
- ec2_instance - use module_util helpers for tagging (https://github.com/ansible-collections/amazon.aws/pull/527).
- ec2_instance_info - Tests for compatability with older versions of the AWS SDKs have been removed (https://github.com/ansible-collections/amazon.aws/pull/442).
- ec2_key - add support for tagging key pairs (https://github.com/ansible-collections/amazon.aws/pull/548).
- ec2_snapshot - add check_mode support (https://github.com/ansible-collections/amazon.aws/pull/512).
- ec2_snapshot - migrated to use the boto3 python library (https://github.com/ansible-collections/amazon.aws/pull/356).
- ec2_spot_instance_info - Added a new module that describes the specified Spot Instance requests (https://github.com/ansible-collections/amazon.aws/pull/487).
- ec2_vol - add check_mode support (https://github.com/ansible-collections/amazon.aws/pull/509).
- ec2_vol - add parameter ``multi_attach`` to support Multi-Attach on volume creation/update (https://github.com/ansible-collections/amazon.aws/pull/362).
- ec2_vol - relax the boto3/botocore requirements and only require botocore 1.19.27 for modifying the ``throughput`` parameter (https://github.com/ansible-collections/amazon.aws/pull/346).
- ec2_vpc_dhcp_option - Now also returns a boto3-style resource description in the ``dhcp_options`` result key.  This includes any tags for the ``dhcp_options_id`` and has the same format as the current return value of ``ec2_vpc_dhcp_option_info``. (https://github.com/ansible-collections/amazon.aws/pull/252)
- ec2_vpc_dhcp_option - use module_util helpers for tagging (https://github.com/ansible-collections/amazon.aws/pull/531).
- ec2_vpc_dhcp_option_info - Now also returns a user-friendly ``dhcp_config`` key that matches the historical ``new_config`` key from ec2_vpc_dhcp_option, and alleviates the need to use ``items2dict(key_name='key', value_name='values')`` when parsing the output of the module. (https://github.com/ansible-collections/amazon.aws/pull/252)
- ec2_vpc_endpoint - added ``vpc_endpoint_security_groups`` parameter to support defining the security group attached to an interface endpoint (https://github.com/ansible-collections/amazon.aws/pull/544).
- ec2_vpc_endpoint - added ``vpc_endpoint_subnets`` parameter to support defining the subnet attached to an interface or gateway endpoint (https://github.com/ansible-collections/amazon.aws/pull/544).
- ec2_vpc_endpoint - use module_util helper for tagging (https://github.com/ansible-collections/amazon.aws/pull/525).
- ec2_vpc_endpoint - use module_util helpers for tagging (https://github.com/ansible-collections/amazon.aws/pull/531).
- ec2_vpc_igw - use module_util helper for tagging (https://github.com/ansible-collections/amazon.aws/pull/523).
- ec2_vpc_igw - use module_util helpers for tagging (https://github.com/ansible-collections/amazon.aws/pull/531).
- ec2_vpc_nat_gateway - use module_util helper for tagging (https://github.com/ansible-collections/amazon.aws/pull/524).
- ec2_vpc_nat_gateway - use module_util helpers for tagging (https://github.com/ansible-collections/amazon.aws/pull/531).
- ec2_vpc_subnet - Tests for compatability with older versions of the AWS SDKs have been removed (https://github.com/ansible-collections/amazon.aws/pull/442).
- elb_classic_lb - added retries on common AWS temporary API failures (https://github.com/ansible-collections/amazon.aws/pull/377).
- elb_classic_lb - added support for check_mode (https://github.com/ansible-collections/amazon.aws/pull/377).
- elb_classic_lb - added support for wait during creation (https://github.com/ansible-collections/amazon.aws/pull/377).
- elb_classic_lb - added support for wait during instance addition and removal (https://github.com/ansible-collections/amazon.aws/pull/377).
- elb_classic_lb - migrated to boto3 SDK (https://github.com/ansible-collections/amazon.aws/pull/377).
- elb_classic_lb - various error messages changed due to refactor (https://github.com/ansible-collections/amazon.aws/pull/377).
- integration tests - remove dependency with collection ``community.general`` (https://github.com/ansible-collections/amazon.aws/pull/361).
- module_utils.ec2 - moved generic tagging helpers into module_utils.tagging (https://github.com/ansible-collections/amazon.aws/pull/527).
- module_utils.tagging - add new helper to generate TagSpecification lists (https://github.com/ansible-collections/amazon.aws/pull/527).
- module_utils/waiter - add RDS cluster ``cluster_available`` waiter (https://github.com/ansible-collections/amazon.aws/pull/464).
- module_utils/waiter - add RDS cluster ``cluster_deleted`` waiter (https://github.com/ansible-collections/amazon.aws/pull/464).
- module_utils/waiter - add Route53 ``resource_record_sets_changed`` waiter (https://github.com/ansible-collections/amazon.aws/pull/350).
- s3_bucket - Tests for compatability with older versions of the AWS SDKs have been removed (https://github.com/ansible-collections/amazon.aws/pull/442).
- s3_bucket - add new option ``object_ownership`` to configure object ownership (https://github.com/ansible-collections/amazon.aws/pull/311)
- s3_bucket - updated to use HeadBucket instead of ListBucket when testing for bucket existence (https://github.com/ansible-collections/amazon.aws/pull/357).

ansible.netcommon
~~~~~~~~~~~~~~~~~

- Add network_resource plugin to manage and provide single entry point for all resource modules for higher oder roles.
- Add support for ProxyCommand with netconf connection.
- Add variable to control ProxyCommand with libssh connection.
- Add vlan_expander filter
- NetworkTemplate and ResouceModule base classes have been moved under module_utils.network.common.rm_base. Stubs have been kept for backwards compatibility. These will be removed after 2023-01-01. Please update imports for existing modules that subclass them. The `cli_rm_builder <https://github.com/ansible-network/cli_rm_builder>`_ has been updated to use the new imports.
- Persistent connection options (persistent_command_timeout, persistent_log_messages, etc.) have been unified across all persistent connections. New persistent connections may also now get these options by extending the connection_persistent documentation fragment.

ansible.posix
~~~~~~~~~~~~~

- acl - add new alias ``recurse`` for ``recursive`` parameter (https://github.com/ansible-collections/ansible.posix/issues/124).
- added 2.11 branch to test matrix, added ignore-2.12.txt.
- authorized_key - add ``no_log=False`` in ``argument_spec`` to clear false-positives of ``no-log-needed`` (https://github.com/ansible-collections/ansible.posix/pull/156).
- authorized_key - add a list of valid key types (https://github.com/ansible-collections/ansible.posix/issues/134).
- mount - Change behavior of ``boot`` option to set ``noauto`` on BSD nodes (https://github.com/ansible-collections/ansible.posix/issues/28).
- mount - Change behavior of ``boot`` option to set ``noauto`` on Linux nodes (https://github.com/ansible-collections/ansible.posix/issues/28).
- mount - add ``no_log=False`` in ``argument_spec`` to clear false-positives of ``no-log-needed`` (https://github.com/ansible-collections/ansible.posix/pull/156).
- mount - returns ``backup_file`` value when a backup fstab is created.
- synchronize - add ``delay_updates`` option (https://github.com/ansible-collections/ansible.posix/issues/157).
- synchronize - fix typo (https://github.com/ansible-collections/ansible.posix/pull/198).

ansible.utils
~~~~~~~~~~~~~

- Add in_any_network, in_network, in_one_network test plugins
- Add ip, ip_address test plugins
- Add ipv4, ipv4_address, ipv4_hostmask, ipv4_netmask test plugins
- Add ipv6, ipv6_address, ipv6_ipv4_mapped, ipv6_sixtofour, ipv6_teredo test plugins
- Add loopback, mac, multicast test plugins
- Add new plugin param_list_compare that generates the final param list after comparing base and provided/target param list.
- Add private, public, reserved test plugins
- Add resolvable test plugins
- Add subnet_of, supernet_of, unspecified test plugins
- Add usable_range test plugin

ansible.windows
~~~~~~~~~~~~~~~

- win_reboot - Change the default ``test_command`` run after a reboot to wait for more services to start up before the plugin finished. This should better handle waiting until the logon screen appears rather than just when WinRM is first online.
- win_updates - Added ``accept_list`` and ``reject_list`` to replace ``whitelist`` and ``blacklist``
- win_updates - Added ``failure_msg`` result to the return value of each update that gives a human readable error message if the update failed to download or install
- win_updates - Added ``filtered_reasons`` that list all the reasons why the update has been filtered - https://github.com/ansible-collections/ansible.windows/issues/226
- win_updates - Added progress logs to display on higher verbosities the download and install progress for each host
- win_updates - Added the ``downloaded`` result to the return value of each update to indicate if an update was downloaded or not
- win_updates - Added the ``skip_optional`` module option to skip optional updates
- win_updates - Added the category ``*`` that matches all categories
- win_updates - Improve Windows Update HRESULT error messages
- win_updates - Improve the details present in the ``log_path`` log entries for better monitoring

arista.eos
~~~~~~~~~~

- Add eos_logging_global resource module.
- Add eos_ntp_global module.
- Add eos_prefix_lists resource module.
- Add new keys to vrf->route_target in bgp modules.
- Change cli 'bgp listen limit' to 'dynamic peer max' ( cli changes in eos 4.23 ).
- Fix ospf3 to be ospfv3 in bgp config.
- Update BGP neighbor peer group syntax.

cisco.aci
~~~~~~~~~

- Add APIC 5.x to inventory for Integration tests
- Add a requirements file
- Add ability to change custom epg name
- Add aci_cloud_ap module and test file
- Add aci_cloud_aws_provider module and its test file (#181)
- Add aci_cloud_bgp_asn module and test file (#180)
- Add aci_cloud_epg_selector module and test file (#182)
- Add aci_fabric_spine_profile, aci_fabric_spine_switch_assoc and aci_fabric_switch_block modules and integration tests (#187)
- Add aci_info
- Add aci_interface_description module and test file (#167)
- Add aci_l3out_bgp_peer and aci_l3out_interface modules and test files (#177)
- Add aci_snmp_client, aci_snmp_client_group, aci_snmp_community_policy, aci_snmp_policy and aci_snmp_user modules and test files (#176)
- Add aci_syslog_group module and test file (#170)
- Add aci_syslog_source and aci_syslog_remote_dest modules and test files (#174)
- Add aci_vmm_controller module and test file
- Add aci_vmm_vswitch module and test file (#142)
- Add check for enhanced lag policy
- Add cloud_external_epg and cloud_external_epg_selector modules and test files (#185)
- Add directory and aliases file for l3out node profile tests
- Add ethertype for IPv6
- Add ethertype ipv4
- Add functionality to support cryptography for signing
- Add galaxy-importer check (#115)
- Add ipv6_l3_unknown_multicast parameter support for aci_bd
- Add issue templates
- Add module aci_cloud_epg & test file (#175)
- Add module aci_l3out_logical_node_profile to manage l3out node profiles
- Add module and test for aci_contract_subject_to_service_graph
- Add new module aci_l2out_extepg_to_contract and test file based on aci_l3out_extepg_to_contract
- Add new modules for L2out - aci_l2out_logical_*
- Add primary_encap in module tests
- Add route_profile, route_profile_l3_out to aci_bd
- Add support and tests for custom_qos_policy parameter in aci_epg
- Add support for ANSIBLE_NET_SSH_KEYFILE
- Add support for vmm domain infra port group and tag collection in aci_domain module (#141)
- Add task to create requirement for enhanced lag policy
- Add test case for custom epg name
- Add test file for aci_bd
- Add tests for ipv6_l3_unknown_multicast parameter support in aci_bd
- Add tests for l3out node profile module
- Add tests to create multiple node profiles and query all node profiles in an L3out
- Add variable references and fix naming in l3out_node_profile tests
- Add version check for changing custom epg name
- Added Enhanced Lag Policy for VMware VMM Domain Profile in module aci_epg_to_domain
- Change CI to latest version of ansible and python 3.8
- Change child_configs & child_classes
- Change dscp to target_dscp in aci_l3out_logical_node_profile module to avoid future var conflicts
- Change naming of lagpolicy
- Change primary_encap --> primaryEncap
- Change test case for enhanced_lag_policy
- Changes made to execute aci_epg_to_domain and aci_cloud_cidr modules, also generalised the cloud variables
- Check WARNINGs and ERRORs in galaxy-importer check (#118)
- Correcting sanity in aci_static_binding_to_epg.py module
- Fix broken test parameters for aci_l3out_logical_interface_profile
- Fix documentation and add example to query all node profiles for L3out
- Fix feedback
- Fix indentation causing linting error
- Fix lag_plicy tDn
- Fix missed separators '/' in path attribute of ACIModule class
- Fix module reference and remove unused aliases in aci_l3out_logical_node_profile tests
- Fixed default values in docs and specs
- Fixed the behavior when output is specified in aci_rest. (#169)
- Initial changes to aci_cloud_ctx_profile module to execute only cloud sites from inventory
- Interface types added for Po's and vPC's using fex-ports and test files
- L3Out Enhancements
- L3Out Interface Profile (#134)
- Made changes in collection version segment
- Made changes in mso.py to generalize construct_url
- Made changes to support aci non cloud host >=3.2
- Made changes with respect to galaxy importer similar to MSO
- Modified 12 files affected from inventory file changes, by differentiating tasks into cloud and non-cloud specific hosts
- Move custom_qos_policy to conditional and remove unnecessary custom_qos_policy from monitoring policy in test
- Move ipv6_l3_unknown_multicast to condition and check version in test
- Remove uneccessary delegate_to variable for l3out_node_profile cleanup task
- Separated assert statements for cloud and non-cloud sites and added additional condition statement required for execution of version<=4.1
- Supports primaryEncap value as unknown (#157)
- Update aci_l3out_extepg_to_contract.py
- W291 + boolean correction
- contract_enhancements (#135)
- doc-required-mismatch fix
- interface blacklist test fix
- interface disable/enable fabricRsOosPath
- interface disable/enable fex support

cisco.asa
~~~~~~~~~

- Fixes asa_ogs service object where complete params were not supported and added with the PR ((https://github.com/ansible-collections/cisco.asa/issues/100).

cisco.ios
~~~~~~~~~

- Add ios_logging_global module.
- Add ios_route_maps Resource Module (https://github.com/ansible-collections/cisco.ios/pull/297).
- Add support for VRF configuration under NTP server.
- Add support for ansible_network_resources key allows to fetch the available resources for a platform (https://github.com/ansible-collections/cisco.ios/pull/292).
- Added ios_ntp_global resource module.
- Deprecated next_hop_self type bool and introduced nexthop_self as dict under bgp_address_family.
- IOS Prefix list resource module.
- Move ios_config idempotent warning message with the task response under `warnings` key if `changed` is `True`
- PR adds the implementation of object group param to acls source and destination parameters (https://github.com/ansible-collections/cisco.ios/issues/339).
- PR to fix the bgp global activate rendering and fix bgp address family round trip failure (https://github.com/ansible-collections/cisco.ios/issues/353).
- Terminal plugin to support IOS device running in SD-WAN mode.
- To add ospfv2 passive_interfaces param with added functionality (https://github.com/ansible-collections/cisco.ios/issues/336).
- To add updated prefix lists and route maps params to Bgp AF RM (https://github.com/ansible-collections/cisco.ios/issues/267).
- To update prefix list and acls merge behaviour and update prefix list description position in model (https://github.com/ansible-collections/cisco.ios/issues/345).

cisco.iosxr
~~~~~~~~~~~

- Add `iosxr_prefix_lists` resource module.
- Add iosxr_logging_global resource module.
- Add new keys for iosxr_l2_interface, iosxr_logging.
- Added iosxr ntp_global resource module.
- Fix integration tests for iosxr_config, iosxr_smoke,iosxr_facts,iosxr_l2_interfaces,iosxr_lag_interfaces, iosxr_logging,iosxr_user.

cisco.meraki
~~~~~~~~~~~~

- meraki_mr_l3_firewall - Return each MR L3 firewall rule's values in lowercase.
- meraki_mr_ssid - Add support for radius_proxy_enabled SSID setting.
- meraki_ms_switchport - Adding additional functionality to support the access_policy_types "MAC allow list" and "Sticky MAC allow list" port security configuration options. (https://github.com/CiscoDevNet/ansible-meraki/issues/227).
- meraki_mx_intrusion_prevention - Rename message to rule_message to avoid conflicts with internal Ansible variables.
- meraki_mx_l3_firewall - Return each MX L3 firewall rule's values in lowercase.
- meraki_mx_switchport - Improve documentation for response
- meraki_mx_vlan - Fix dhcp_boot_options_enabled parameter

cisco.mso
~~~~~~~~~

- Add Ansible common HTTPAPI dependancy in galaxy.yml
- Add HTTPAPI connection plugin support and HTTPAPI MSO connection plugin
- Add primary and unicast_routing attributes to mso_schema_template_bd
- Add requirements.txt for Ansible Environment support
- Add schema and template cloning modules mso_schema_clone and mso_schema_template_clone
- Add support cisco.nd.nd connection plugin
- Add support for multiple DCHP policies in a BD and new module mso_schema_template_bd_dhcp_policy
- Upgrade CI to latest Ansible version and Python 3.8

cisco.nxos
~~~~~~~~~~

- Add `advertise_l2vpn_evpn` option in `nxos_bgp_address_family` module (https://github.com/ansible-collections/cisco.nxos/issues/302).
- Add `default_passive_interface` option in `nxos_ospf_interfaces`.
- Add `nxos_prefix_lists` resource module.
- Add a netconf subplugin to make netconf_* modules work with older NX-OS versions (https://github.com/ansible-collections/ansible.netcommon/issues/252).
- Add nxos_logging_global resource module.
- Add nxos_ntp_global module.
- `nxos_telemetry` - Add support for state gathered

cloudscale_ch.cloud
~~~~~~~~~~~~~~~~~~~

- Increase api_timeout to 45
- Read CLOUDSCALE_API_TIMEOUT environment variable

community.aws
~~~~~~~~~~~~~

- aws_config_delivery_channel - replaced use of deprecated backoff decorator (https://github.com/ansible-collections/community.aws/pull/764).
- aws_direct_connect_confirm_connection - replaced use of deprecated backoff decorator (https://github.com/ansible-collections/community.aws/pull/764).
- aws_direct_connect_connection - replaced use of deprecated backoff decorator (https://github.com/ansible-collections/community.aws/pull/764).
- aws_direct_connect_link_aggregation_group - replaced use of deprecated backoff decorator (https://github.com/ansible-collections/community.aws/pull/764).
- aws_direct_connect_virtual_interface - replaced use of deprecated backoff decorator (https://github.com/ansible-collections/community.aws/pull/764).
- aws_eks_cluster - Tests for compatability with older versions of the AWS SDKs have been removed (https://github.com/ansible-collections/community.aws/pull/675).
- aws_inspector_target - replaced use of deprecated backoff decorator (https://github.com/ansible-collections/community.aws/pull/764).
- aws_kms - add support for ``kms_spec`` and ``kms_usage`` parameter (https://github.com/ansible-collections/community.aws/pull/774).
- aws_kms - replaced use of deprecated backoff decorator (https://github.com/ansible-collections/community.aws/pull/764).
- aws_kms_info - replaced use of deprecated backoff decorator (https://github.com/ansible-collections/community.aws/pull/764).
- aws_kms_info - use a generator rather than list comprehension (https://github.com/ansible-collections/community.aws/pull/688).
- aws_s3_bucket_info - added test for botocore>=1.18.11 when attempting to fetch bucket ownership controls (https://github.com/ansible-collections/community.aws/pull/682)
- aws_ses_rule_set - use a generator rather than list comprehension (https://github.com/ansible-collections/community.aws/pull/688).
- aws_sgw_info - ensure module runs in check_mode (https://github.com/ansible-collections/community.aws/issues/659).
- cloudformation_exports_info - ensure module runs in check_mode (https://github.com/ansible-collections/community.aws/issues/659).
- cloudformation_stack_set - Tests for compatability with older versions of the AWS SDKs have been removed (https://github.com/ansible-collections/community.aws/pull/675).
- cloudformation_stack_set - replaced use of deprecated backoff decorator (https://github.com/ansible-collections/community.aws/pull/764).
- cloudfront_distribution - add ``TLSv1.2_2021`` security policy for viewer connections (https://github.com/ansible-collections/community.aws/pull/707).
- cloudfront_info - ensure module runs in check_mode (https://github.com/ansible-collections/community.aws/issues/659).
- cloudwatchevent_rule - use a generator rather than list comprehension (https://github.com/ansible-collections/community.aws/pull/688).
- dms_endpoint - replaced use of deprecated backoff decorator (https://github.com/ansible-collections/community.aws/pull/764).
- dms_replication_subnet_group - replaced use of deprecated backoff decorator (https://github.com/ansible-collections/community.aws/pull/764).
- dynamodb_table - Tests for compatability with older versions of the AWS SDKs have been removed (https://github.com/ansible-collections/community.aws/pull/675).
- dynamodb_table - add support for setting the `billing_mode` option (https://github.com/ansible-collections/community.aws/pull/753).
- dynamodb_table - the module has been updated to use the boto3 AWS SDK (https://github.com/ansible-collections/community.aws/pull/726).
- dynamodb_ttl - Tests for compatability with older versions of the AWS SDKs have been removed (https://github.com/ansible-collections/community.aws/pull/675).
- ec2_ami_copy - Tests for compatability with older versions of the AWS SDKs have been removed (https://github.com/ansible-collections/community.aws/pull/675).
- ec2_asg - Tests for compatability with older versions of the AWS SDKs have been removed (https://github.com/ansible-collections/community.aws/pull/675).
- ec2_asg - replaced use of deprecated backoff decorator (https://github.com/ansible-collections/community.aws/pull/764).
- ec2_asg_info - ensure module runs in check_mode (https://github.com/ansible-collections/community.aws/issues/659).
- ec2_eip - added support for tagging EIPs (https://github.com/ansible-collections/community.aws/pull/332).
- ec2_eip_info - added automatic retries for common temporary API failures (https://github.com/ansible-collections/community.aws/pull/332).
- ec2_eip_info - added support for tagging EIPs (https://github.com/ansible-collections/community.aws/pull/332).
- ec2_elb_info - replaced use of deprecated backoff decorator (https://github.com/ansible-collections/community.aws/pull/764).
- ec2_launch_template - Tests for compatability with older versions of the AWS SDKs have been removed (https://github.com/ansible-collections/community.aws/pull/675).
- ec2_lc_info - ensure module runs in check_mode (https://github.com/ansible-collections/community.aws/issues/659).
- ec2_transit_gateway - Tests for compatability with older versions of the AWS SDKs have been removed (https://github.com/ansible-collections/community.aws/pull/675).
- ec2_transit_gateway_info - Tests for compatability with older versions of the AWS SDKs have been removed (https://github.com/ansible-collections/community.aws/pull/675).
- ec2_vpc_peer - Tests for compatability with older versions of the AWS SDKs have been removed (https://github.com/ansible-collections/community.aws/pull/675).
- ec2_vpc_peer - use shared code for tagging peering connections (https://github.com/ansible-collections/community.aws/pull/614).
- ec2_vpc_route_table - use shared code for tagging route tables (https://github.com/ansible-collections/community.aws/pull/616).
- ec2_vpc_vgw - fix arguments-renamed pylint issue (https://github.com/ansible-collections/community.aws/pull/686).
- ec2_vpc_vpn - fix arguments-renamed pylint issue (https://github.com/ansible-collections/community.aws/pull/686).
- ec2_win_password - module updated to use the boto3 AWS SDK (https://github.com/ansible-collections/community.aws/pull/759).
- ecs_ecr - Tests for compatability with older versions of the AWS SDKs have been removed (https://github.com/ansible-collections/community.aws/pull/675).
- ecs_service - Tests for compatability with older versions of the AWS SDKs have been removed (https://github.com/ansible-collections/community.aws/pull/675).
- ecs_service - added support for forcing deletion of a service (https://github.com/ansible-collections/community.aws/pull/228).
- ecs_service_info - replaced use of deprecated backoff decorator (https://github.com/ansible-collections/community.aws/pull/764).
- ecs_task - Tests for compatability with older versions of the AWS SDKs have been removed (https://github.com/ansible-collections/community.aws/pull/675).
- ecs_task - remove unused import (https://github.com/ansible-collections/community.aws/pull/686).
- ecs_taskdefinition - Tests for compatability with older versions of the AWS SDKs have been removed (https://github.com/ansible-collections/community.aws/pull/675).
- ecs_taskdefinition - add ``placement_constraints`` option (https://github.com/ansible-collections/community.aws/pull/741).
- efs - Tests for compatability with older versions of the AWS SDKs have been removed (https://github.com/ansible-collections/community.aws/pull/675).
- efs - add ``transition_to_ia`` parameter to support specifying the number of days before transitioning data to inactive storage (https://github.com/ansible-collections/community.aws/pull/522).
- efs_info - Tests for compatability with older versions of the AWS SDKs have been removed (https://github.com/ansible-collections/community.aws/pull/675).
- elasticache_subnet_group - add return values (https://github.com/ansible-collections/community.aws/pull/723).
- elasticache_subnet_group - add support for check_mode (https://github.com/ansible-collections/community.aws/pull/723).
- elasticache_subnet_group - module migrated to boto3 AWS SDK (https://github.com/ansible-collections/community.aws/pull/723).
- elb_application_lb - added ``ip_address_type`` parameter to support changing application load balancer configuration (https://github.com/ansible-collections/community.aws/pull/499).
- elb_application_lb_info - added ``ip_address_type`` in output when gathering application load balancer parameters (https://github.com/ansible-collections/community.aws/pull/499).
- elb_instance - added new ``updated_elbs`` return value (https://github.com/ansible-collections/community.aws/pull/773).
- elb_instance - make elb_instance idempotent when deregistering instances.  Merged from ec2_elb U(https://github.com/ansible/ansible/pull/31660).
- elb_instance - the module has been migrated to the boto3 AWS SDK (https://github.com/ansible-collections/community.aws/pull/773).
- elb_network_lb - added ``ip_address_type`` parameter to support changing network load balancer configuration (https://github.com/ansible-collections/community.aws/pull/499).
- elb_target_group - Tests for compatability with older versions of the AWS SDKs have been removed (https://github.com/ansible-collections/community.aws/pull/675).
- elb_target_group - add ``preserve_client_ip_enabled`` option (https://github.com/ansible-collections/community.aws/pull/670).
- elb_target_group - add ``proxy_protocol_v2_enabled`` option (https://github.com/ansible-collections/community.aws/pull/670).
- elb_target_group - use a generator rather than list comprehension (https://github.com/ansible-collections/community.aws/pull/688).
- iam - use a generator rather than list comprehension (https://github.com/ansible-collections/community.aws/pull/688).
- iam_group - use a generator rather than list comprehension (https://github.com/ansible-collections/community.aws/pull/688).
- iam_managed_policy - replaced use of deprecated backoff decorator (https://github.com/ansible-collections/community.aws/pull/764).
- iam_mfa_device_info - ensure module runs in check_mode (https://github.com/ansible-collections/community.aws/issues/659).
- iam_role - Added `wait` option for IAM role creation / updates (https://github.com/ansible-collections/community.aws/pull/767).
- iam_role - Tests for compatability with older versions of the AWS SDKs have been removed (https://github.com/ansible-collections/community.aws/pull/675).
- iam_role - use a generator rather than list comprehension (https://github.com/ansible-collections/community.aws/pull/688).
- iam_saml_federation - replaced use of deprecated backoff decorator (https://github.com/ansible-collections/community.aws/pull/764).
- iam_server_certificate - add support for check_mode (https://github.com/ansible-collections/community.aws/pull/737).
- iam_server_certificate - migrate module to using the boto3 SDK (https://github.com/ansible-collections/community.aws/pull/737).
- iam_server_certificate_info - ensure module runs in check_mode (https://github.com/ansible-collections/community.aws/issues/659).
- iam_user - use a generator rather than list comprehension (https://github.com/ansible-collections/community.aws/pull/688).
- kms_info - added a new ``keys_attr`` parameter to continue returning the key details in the ``keys`` attribute as well as the ``kms_keys`` attribute (https://github.com/ansible-collections/community.aws/pull/648).
- lambda - Tests for compatability with older versions of the AWS SDKs have been removed (https://github.com/ansible-collections/community.aws/pull/675).
- lambda_info - add automatic retries for recoverable errors (https://github.com/ansible-collections/community.aws/pull/777).
- lambda_info - add support for tags (https://github.com/ansible-collections/community.aws/pull/375).
- lambda_info - use paginator for list queries (https://github.com/ansible-collections/community.aws/pull/777).
- rds - replaced use of deprecated backoff decorator (https://github.com/ansible-collections/community.aws/pull/764).
- rds_instance - Tests for compatability with older versions of the AWS SDKs have been removed (https://github.com/ansible-collections/community.aws/pull/675).
- rds_instance - convert ``preferred_maintenance_window`` days into lowercase so changed returns properly (https://github.com/ansible-collections/community.aws/pull/516).
- rds_instance - use a generator rather than list comprehension (https://github.com/ansible-collections/community.aws/pull/688).
- redshift_subnet_group - added support for check_mode (https://github.com/ansible-collections/community.aws/pull/724).
- redshift_subnet_group - the ``group_description`` option has been renamed to ``description`` and is now optional. The old parameter name will continue to work (https://github.com/ansible-collections/community.aws/pull/724).
- redshift_subnet_group - the ``group_subnets`` option has been renamed to ``subnets`` and is now only required when creating a new group. The old parameter name will continue to work (https://github.com/ansible-collections/community.aws/pull/724).
- redshift_subnet_group - the module has been migrated to the boto3 AWS SDK (https://github.com/ansible-collections/community.aws/pull/724).
- route53 - add rate-limiting retries while waiting for changes to propagate (https://github.com/ansible-collections/community.aws/pull/564).
- route53 - add retries on ``PriorRequestNotComplete`` errors (https://github.com/ansible-collections/community.aws/pull/564).
- route53 - update retry ``max_delay`` setting so that it can be set above 60 seconds (https://github.com/ansible-collections/community.aws/pull/564).
- route53_health_check - add support for tagging health checks (https://github.com/ansible-collections/community.aws/pull/765).
- route53_health_check - added support for check_mode (https://github.com/ansible-collections/community.aws/pull/734).
- route53_health_check - added support for disabling health checks (https://github.com/ansible-collections/community.aws/pull/756).
- route53_health_check - migrated to boto3 SDK (https://github.com/ansible-collections/community.aws/pull/734).
- route53_zone - add support for tagging Route 53 zones (https://github.com/ansible-collections/community.aws/pull/565).
- sns_topic - Added ``topic_type`` parameter to select type of SNS topic (either FIFO or Standard) (https://github.com/ansible-collections/community.aws/pull/599).
- sqs_queue - Providing a kms_master_key_id will now enable SSE properly (https://github.com/ansible-collections/community.aws/pull/762)
- sqs_queue - Tests for compatability with older versions of the AWS SDKs have been removed (https://github.com/ansible-collections/community.aws/pull/675).
- various community.aws modules - remove unused imports (https://github.com/ansible-collections/community.aws/pull/629)
- wafv2_resources_info - ensure module runs in check_mode (https://github.com/ansible-collections/community.aws/issues/659).
- wafv2_web_acl_info - ensure module runs in check_mode (https://github.com/ansible-collections/community.aws/issues/659).

community.crypto
~~~~~~~~~~~~~~~~

- Avoid internal ansible-core module_utils in favor of equivalent public API available since at least Ansible 2.9 (https://github.com/ansible-collections/community.crypto/pull/253).
- acme_* modules - fix usage of ``fetch_url`` with changes in latest ansible-core ``devel`` branch (https://github.com/ansible-collections/community.crypto/pull/339).
- acme_certificate - the ``subject`` and ``issuer`` fields in in the ``select_chain`` entries are now more strictly validated (https://github.com/ansible-collections/community.crypto/pull/316).
- cryptography_openssh module utils - new module_utils for managing asymmetric keypairs and OpenSSH formatted/encoded asymmetric keypairs (https://github.com/ansible-collections/community.crypto/pull/213).
- get_certificate - added ``starttls`` option to retrieve certificates from servers which require clients to request an encrypted connection (https://github.com/ansible-collections/community.crypto/pull/264).
- openssh certificate module utils - new module_utils for parsing OpenSSH certificates (https://github.com/ansible-collections/community.crypto/pull/246).
- openssh_cert - added ``regenerate`` option to validate additional certificate parameters which trigger regeneration of an existing certificate (https://github.com/ansible-collections/community.crypto/pull/256).
- openssh_cert - adding ``diff`` support (https://github.com/ansible-collections/community.crypto/pull/255).
- openssh_keypair - added ``backend`` parameter for selecting between the cryptography library or the OpenSSH binary for the execution of actions performed by ``openssh_keypair`` (https://github.com/ansible-collections/community.crypto/pull/236).
- openssh_keypair - added ``diff`` support (https://github.com/ansible-collections/community.crypto/pull/260).
- openssh_keypair - added ``passphrase`` parameter for encrypting/decrypting OpenSSH private keys (https://github.com/ansible-collections/community.crypto/pull/225).
- openssl_csr - add diff mode (https://github.com/ansible-collections/community.crypto/issues/38, https://github.com/ansible-collections/community.crypto/pull/150).
- openssl_csr, openssl_csr_pipe - provide a new ``subject_ordered`` option if the order of the components in the subject is of importance (https://github.com/ansible-collections/community.crypto/issues/291, https://github.com/ansible-collections/community.crypto/pull/316).
- openssl_csr, openssl_csr_pipe - there is now stricter validation of the values of the ``subject`` option (https://github.com/ansible-collections/community.crypto/pull/316).
- openssl_csr_info - now returns ``public_key_type`` and ``public_key_data`` (https://github.com/ansible-collections/community.crypto/pull/233).
- openssl_csr_info - refactor module to allow code re-use for diff mode (https://github.com/ansible-collections/community.crypto/pull/204).
- openssl_csr_pipe - add diff mode (https://github.com/ansible-collections/community.crypto/issues/38, https://github.com/ansible-collections/community.crypto/pull/150).
- openssl_pkcs12 - added option ``select_crypto_backend`` and a ``cryptography`` backend. This requires cryptography 3.0 or newer, and does not support the ``iter_size`` and ``maciter_size`` options (https://github.com/ansible-collections/community.crypto/pull/234).
- openssl_privatekey - add diff mode (https://github.com/ansible-collections/community.crypto/issues/38, https://github.com/ansible-collections/community.crypto/pull/150).
- openssl_privatekey_info - add ``check_consistency`` option to request private key consistency checks to be done (https://github.com/ansible-collections/community.crypto/pull/309).
- openssl_privatekey_info - refactor module to allow code re-use for diff mode (https://github.com/ansible-collections/community.crypto/pull/205).
- openssl_privatekey_pipe - add diff mode (https://github.com/ansible-collections/community.crypto/issues/38, https://github.com/ansible-collections/community.crypto/pull/150).
- openssl_publickey - add diff mode (https://github.com/ansible-collections/community.crypto/issues/38, https://github.com/ansible-collections/community.crypto/pull/150).
- x509_certificate - add diff mode (https://github.com/ansible-collections/community.crypto/issues/38, https://github.com/ansible-collections/community.crypto/pull/150).
- x509_certificate, x509_certificate_pipe - add ``ignore_timestamps`` option which allows to enable idempotency for 'not before' and 'not after' options (https://github.com/ansible-collections/community.crypto/issues/295, https://github.com/ansible-collections/community.crypto/pull/317).
- x509_certificate_info - now returns ``public_key_type`` and ``public_key_data`` (https://github.com/ansible-collections/community.crypto/pull/233).
- x509_certificate_info - refactor module to allow code re-use for diff mode (https://github.com/ansible-collections/community.crypto/pull/206).
- x509_certificate_pipe - add diff mode (https://github.com/ansible-collections/community.crypto/issues/38, https://github.com/ansible-collections/community.crypto/pull/150).
- x509_crl - add diff mode (https://github.com/ansible-collections/community.crypto/issues/38, https://github.com/ansible-collections/community.crypto/pull/150).
- x509_crl - provide a new ``issuer_ordered`` option if the order of the components in the issuer is of importance (https://github.com/ansible-collections/community.crypto/issues/291, https://github.com/ansible-collections/community.crypto/pull/316).
- x509_crl - there is now stricter validation of the values of the ``issuer`` option (https://github.com/ansible-collections/community.crypto/pull/316).
- x509_crl_info - add ``list_revoked_certificates`` option to avoid enumerating all revoked certificates (https://github.com/ansible-collections/community.crypto/pull/232).
- x509_crl_info - refactor module to allow code re-use for diff mode (https://github.com/ansible-collections/community.crypto/pull/203).

community.digitalocean
~~~~~~~~~~~~~~~~~~~~~~

- digital_ocean - ``ssh_key_ids`` list entries are now validated to be strings (https://github.com/ansible-collections/community.digitalocean/issues/13).
- digital_ocean - running and enforcing psf/black in the codebase (https://github.com/ansible-collections/community.digitalocean/issues/136).
- digital_ocean_block_storage - adding Project support (https://github.com/ansible-collections/community.digitalocean/issues/171).
- digital_ocean_database - add support for MongoDB (https://github.com/ansible-collections/community.digitalocean/issues/124).
- digital_ocean_database - adding Project support (https://github.com/ansible-collections/community.digitalocean/issues/171).
- digital_ocean_domain - adding Project support (https://github.com/ansible-collections/community.digitalocean/issues/171).
- digital_ocean_droplet - ``ssh_keys``, ``tags``, and ``volumes`` list entries are now validated to be strings (https://github.com/ansible-collections/community.digitalocean/issues/13).
- digital_ocean_droplet - adding Project support (https://github.com/ansible-collections/community.digitalocean/issues/171).
- digital_ocean_droplet - adding ``active`` and ``inactive`` states (https://github.com/ansible-collections/community.digitalocean/issues/23).
- digital_ocean_droplet - adding ability to apply and remove firewall by using droplet module (https://github.com/ansible-collections/community.digitalocean/issues/159).
- digital_ocean_droplet - adds Droplet resize functionality (https://github.com/ansible-collections/community.digitalocean/issues/4).
- digital_ocean_droplet - require unique_name for state=absent to avoid unintentional droplet deletions.
- digital_ocean_firewall - inbound_rules and outbound_rules are no longer required for firewall removal (https://github.com/ansible-collections/community.digitalocean/issues/181).
- digital_ocean_floating_ip - adding Project support (https://github.com/ansible-collections/community.digitalocean/issues/171).
- digital_ocean_floating_ip - adding attach and detach states to floating ip module (https://github.com/ansible-collections/community.digitalocean/issues/170).
- digital_ocean_floating_ip_info - new integration test for the `digital_ocean_floating_ip_info` module (https://github.com/ansible-collections/community.digitalocean/issues/130).
- digital_ocean_kubernetes - adding the C(taints), C(auto_scale), C(min_nodes) and C(max_nodes) parameters to the C(node_pools) definition (https://github.com/ansible-collections/community.digitalocean/issues/157).
- digital_ocean_kubernetes - set "latest" as the default version for new clusters (https://github.com/ansible-collections/community.digitalocean/issues/114).
- digital_ocean_load_balancer - adding Project support (https://github.com/ansible-collections/community.digitalocean/issues/171).
- digitalocean - Filter droplets in dynamic inventory plugin using arbitrary. jinja2 expressions (https://github.com/ansible-collections/community.digitalocean/pull/96).
- digitalocean - Support templates in API tokens when using the dynamic inventory plugin (https://github.com/ansible-collections/community.digitalocean/pull/98).
- digitalocean integration tests - adding integration tests for CDN Endpoints (https://github.com/ansible-collections/community.digitalocean/issues/179).
- digitalocean inventory script - add support for Droplet tag filtering (https://github.com/ansible-collections/community.digitalocean/issues/7).

community.docker
~~~~~~~~~~~~~~~~

- Add the modules docker_container_exec, docker_image_load and docker_plugin to the ``docker`` module defaults group (https://github.com/ansible-collections/community.docker/pull/209).
- Avoid internal ansible-core module_utils in favor of equivalent public API available since at least Ansible 2.9 (https://github.com/ansible-collections/community.docker/pull/164).
- common module utils - correct error messages for guiding to install proper Docker SDK for Python module (https://github.com/ansible-collections/community.docker/pull/125).
- docker_* modules - include ``ImportError`` traceback when reporting that Docker SDK for Python could not be found (https://github.com/ansible-collections/community.docker/pull/188).
- docker_compose - added ``env_file`` option for specifying custom environment files (https://github.com/ansible-collections/community.docker/pull/174).
- docker_compose - added ``profiles`` option to specify service profiles when starting services (https://github.com/ansible-collections/community.docker/pull/167).
- docker_config - add option ``data_src`` to read configuration data from target (https://github.com/ansible-collections/community.docker/issues/64, https://github.com/ansible-collections/community.docker/pull/203).
- docker_container - added ``publish_all_ports`` option to publish all exposed ports to random ports except those explicitly bound with ``published_ports`` (this was already added in community.docker 1.8.0) (https://github.com/ansible-collections/community.docker/pull/162).
- docker_container - added new ``command_handling`` option with current deprecated default value ``compatibility`` which allows to control how the module handles shell quoting when interpreting lists, and how the module handles empty lists/strings. The default will switch to ``correct`` in community.docker 3.0.0 (https://github.com/ansible-collections/community.docker/pull/186).
- docker_container - allow ``memory_swap: -1`` to set memory swap limit to unlimited. This is useful when the user cannot set memory swap limits due to cgroup limitations or other reasons, as by default Docker will try to set swap usage to two times the value of ``memory`` (https://github.com/ansible-collections/community.docker/pull/138).
- docker_container - lifted restriction preventing the creation of anonymous volumes with the ``mounts`` option (https://github.com/ansible-collections/community.docker/pull/181).
- docker_containers inventory plugin - when ``connection_type=docker-api``, now pass Docker daemon connection options from inventory plugin to connection plugin. This can be disabled by setting ``configure_docker_daemon=false`` (https://github.com/ansible-collections/community.docker/pull/157).
- docker_host_info - allow values for keys in ``containers_filters``, ``images_filters``, ``networks_filters``, and ``volumes_filters`` to be passed as YAML lists (https://github.com/ansible-collections/community.docker/pull/160).
- docker_image - allow to tag images by ID (https://github.com/ansible-collections/community.docker/pull/149).
- docker_plugin - added ``alias`` option to specify local names for docker plugins (https://github.com/ansible-collections/community.docker/pull/161).
- docker_secret - add option ``data_src`` to read secret data from target (https://github.com/ansible-collections/community.docker/issues/64, https://github.com/ansible-collections/community.docker/pull/203).

community.general
~~~~~~~~~~~~~~~~~

- Avoid internal ansible-core module_utils in favor of equivalent public API available since at least Ansible 2.9 (https://github.com/ansible-collections/community.general/pull/2877).
- ModuleHelper module utils - improved mechanism for customizing the calculation of ``changed`` (https://github.com/ansible-collections/community.general/pull/2514).
- Remove unnecessary ``__init__.py`` files from ``plugins/`` (https://github.com/ansible-collections/community.general/pull/2632).
- apache2_module - minor refactoring improving code quality, readability and speed (https://github.com/ansible-collections/community.general/pull/3106).
- archive - added ``dest_state`` return value to describe final state of ``dest`` after successful task execution (https://github.com/ansible-collections/community.general/pull/2913).
- archive - added ``exclusion_patterns`` option to exclude files or subdirectories from archives (https://github.com/ansible-collections/community.general/pull/2616).
- archive - refactoring prior to fix for idempotency checks. The fix will be a breaking change and only appear in community.general 4.0.0 (https://github.com/ansible-collections/community.general/pull/2987).
- bitbucket_* modules - add ``user`` and ``password`` options for Basic authentication (https://github.com/ansible-collections/community.general/pull/2045).
- chroot connection - minor refactor to make lints and IDEs happy (https://github.com/ansible-collections/community.general/pull/2520).
- cloud_init_data_facts - minor refactor (https://github.com/ansible-collections/community.general/pull/2557).
- cmd (Module Helper) module utils - ``CmdMixin`` now pulls the value for ``run_command()`` params from ``self.vars``, as opposed to previously retrieving those from ``self.module.params`` (https://github.com/ansible-collections/community.general/pull/2517).
- composer - add ``composer_executable`` option (https://github.com/ansible-collections/community.general/issues/2649).
- datadog_event - adding parameter ``api_host`` to allow selecting a datadog API endpoint instead of using the default one (https://github.com/ansible-collections/community.general/issues/2774, https://github.com/ansible-collections/community.general/pull/2775).
- datadog_monitor - allow creation of composite datadog monitors (https://github.com/ansible-collections/community.general/issues/2956).
- dig lookup plugin - add ``retry_servfail`` option (https://github.com/ansible-collections/community.general/pull/3247).
- dnsimple - module rewrite to include support for python-dnsimple>=2.0.0; also add ``sandbox`` parameter (https://github.com/ansible-collections/community.general/pull/2946).
- elastic callback plugin - enriched the stacktrace information with the ``message``, ``exception`` and ``stderr`` fields from the failed task (https://github.com/ansible-collections/community.general/pull/3556).
- filesystem - cleanup and revamp module, tests and doc. Pass all commands to ``module.run_command()`` as lists. Move the device-vs-mountpoint logic to ``grow()`` method. Give to all ``get_fs_size()`` the same logic and error handling. (https://github.com/ansible-collections/community.general/pull/2472).
- filesystem - extend support for FreeBSD. Avoid potential data loss by checking existence of a filesystem with ``fstyp`` (native command) if ``blkid`` (foreign command) doesn't find one. Add support for character devices and ``ufs`` filesystem type (https://github.com/ansible-collections/community.general/pull/2902).
- flatpak - add ``no_dependencies`` parameter (https://github.com/ansible/ansible/pull/55452, https://github.com/ansible-collections/community.general/pull/2751).
- flatpak - allows installing or uninstalling a list of packages (https://github.com/ansible-collections/community.general/pull/2521).
- funcd connection - minor refactor to make lints and IDEs happy (https://github.com/ansible-collections/community.general/pull/2520).
- gem - add ``bindir`` option to specify an installation path for executables such as ``/home/user/bin`` or ``/home/user/.local/bin`` (https://github.com/ansible-collections/community.general/pull/2837).
- gem - add ``norc`` option to avoid loading any ``.gemrc`` file (https://github.com/ansible-collections/community.general/pull/2837).
- github_repo - add new option ``api_url``  to allow working with on premises installations (https://github.com/ansible-collections/community.general/pull/3038).
- gitlab_group - add new options ``project_creation_level``, ``auto_devops_enabled``, ``subgroup_creation_level`` (https://github.com/ansible-collections/community.general/pull/3248).
- gitlab_group - add new property ``require_two_factor_authentication`` (https://github.com/ansible-collections/community.general/pull/3367).
- gitlab_group_members - ``gitlab_user`` can now also be a list of users (https://github.com/ansible-collections/community.general/pull/3047).
- gitlab_group_members - added functionality to set all members exactly as given (https://github.com/ansible-collections/community.general/pull/3047).
- gitlab_project - add new options ``allow_merge_on_skipped_pipeline``, ``only_allow_merge_if_all_discussions_are_resolved``, ``only_allow_merge_if_pipeline_succeeds``, ``packages_enabled``, ``remove_source_branch_after_merge``, ``squash_option`` (https://github.com/ansible-collections/community.general/pull/3002).
- gitlab_project - add new properties ``ci_config_path`` and ``shared_runners_enabled`` (https://github.com/ansible-collections/community.general/pull/3379).
- gitlab_project - projects can be created under other user's namespaces with the new ``username`` option (https://github.com/ansible-collections/community.general/pull/2824).
- gitlab_project_members - ``gitlab_user`` can now also be a list of users (https://github.com/ansible-collections/community.general/pull/3319).
- gitlab_project_members - added functionality to set all members exactly as given (https://github.com/ansible-collections/community.general/pull/3319).
- gitlab_runner - support project-scoped gitlab.com runners registration (https://github.com/ansible-collections/community.general/pull/634).
- gitlab_user - add ``expires_at`` option (https://github.com/ansible-collections/community.general/issues/2325).
- gitlab_user - add functionality for adding external identity providers to a GitLab user (https://github.com/ansible-collections/community.general/pull/2691).
- gitlab_user - allow to reset an existing password with the new ``reset_password`` option (https://github.com/ansible-collections/community.general/pull/2691).
- gitlab_user - specifying a password is no longer necessary (https://github.com/ansible-collections/community.general/pull/2691).
- gunicorn - search for ``gunicorn`` binary in more paths (https://github.com/ansible-collections/community.general/pull/3092).
- hana_query - added the abillity to use hdbuserstore (https://github.com/ansible-collections/community.general/pull/3125).
- hpilo_info - added ``host_power_status`` return value to report power state of machine with ``OFF``, ``ON`` or ``UNKNOWN`` (https://github.com/ansible-collections/community.general/pull/3079).
- idrac_redfish_config - modified set_manager_attributes function to skip invalid attribute instead of returning. Added skipped attributes to output. Modified module exit to add warning variable (https://github.com/ansible-collections/community.general/issues/1995).
- influxdb_retention_policy - add ``state`` parameter with allowed values ``present`` and ``absent`` to support deletion of existing retention policies (https://github.com/ansible-collections/community.general/issues/2383).
- influxdb_retention_policy - simplify duration logic parsing (https://github.com/ansible-collections/community.general/pull/2385).
- ini_file - add abbility to define multiple options with the same name but different values (https://github.com/ansible-collections/community.general/issues/273, https://github.com/ansible-collections/community.general/issues/1204).
- ini_file - add module option ``exclusive`` (boolean) for the ability to add/remove single ``option=value`` entries without overwriting existing options with the same name but different values (https://github.com/ansible-collections/community.general/pull/3033).
- ini_file - opening file with encoding ``utf-8-sig`` (https://github.com/ansible-collections/community.general/issues/2189).
- interfaces_file - minor refactor (https://github.com/ansible-collections/community.general/pull/3328).
- iocage connection - minor refactor to make lints and IDEs happy (https://github.com/ansible-collections/community.general/pull/2520).
- ipa_config - add ``ipaselinuxusermaporder`` option to set the SELinux user map order (https://github.com/ansible-collections/community.general/pull/3178).
- ipa_group - add ``append`` option for adding group and users members, instead of replacing the respective lists (https://github.com/ansible-collections/community.general/pull/3545).
- jail connection - minor refactor to make lints and IDEs happy (https://github.com/ansible-collections/community.general/pull/2520).
- java_keystore - added ``ssl_backend`` parameter for using the cryptography library instead of the OpenSSL binary (https://github.com/ansible-collections/community.general/pull/2485).
- java_keystore - replace envvar by stdin to pass secret to ``keytool`` (https://github.com/ansible-collections/community.general/pull/2526).
- jenkins_build - support stopping a running jenkins build (https://github.com/ansible-collections/community.general/pull/2850).
- jenkins_job_info - the ``password`` and ``token`` parameters can also be omitted to retrieve only public information (https://github.com/ansible-collections/community.general/pull/2948).
- jenkins_plugin - add fallback url(s) for failure of plugin installation/download (https://github.com/ansible-collections/community.general/pull/1334).
- jira - add comment visibility parameter for comment operation (https://github.com/ansible-collections/community.general/pull/2556).
- kernel_blacklist - revamped the module using ``ModuleHelper`` (https://github.com/ansible-collections/community.general/pull/3329).
- keycloak_* modules - refactor many of the ``keycloak_*`` modules to have similar structures, comments, and documentation (https://github.com/ansible-collections/community.general/pull/3280).
- keycloak_authentication - enhanced diff mode to also return before and after state when the authentication flow is updated (https://github.com/ansible-collections/community.general/pull/2963).
- keycloak_client - add ``authentication_flow_binding_overrides`` option (https://github.com/ansible-collections/community.general/pull/2949).
- keycloak_realm - add ``events_enabled`` parameter to allow activation or deactivation of login events (https://github.com/ansible-collections/community.general/pull/3231).
- linode - added proper traceback when failing due to exceptions (https://github.com/ansible-collections/community.general/pull/2410).
- linode - parameter ``additional_disks`` is now validated as a list of dictionaries (https://github.com/ansible-collections/community.general/pull/2410).
- linode inventory plugin - adds the ``ip_style`` configuration key. Set to ``api`` to get more detailed network details back from the remote Linode host (https://github.com/ansible-collections/community.general/pull/3203).
- lxc connection - minor refactor to make lints and IDEs happy (https://github.com/ansible-collections/community.general/pull/2520).
- lxd_container - add ``ignore_volatile_options`` option which allows to disable the behavior that the module ignores options starting with ``volatile.`` (https://github.com/ansible-collections/community.general/pull/3331).
- mail - added the ``ehlohost`` parameter which allows for manual override of the host used in SMTP EHLO (https://github.com/ansible-collections/community.general/pull/3425).
- maven_artifact - added ``checksum_alg`` option to support SHA1 checksums in order to support FIPS systems (https://github.com/ansible-collections/community.general/pull/2662).
- module_helper cmd module utils - added the ``ArgFormat`` style ``BOOLEAN_NOT``, to add CLI parameters when the module argument is false-ish (https://github.com/ansible-collections/community.general/pull/3290).
- module_helper module utils - added feature flag parameter to ``CmdMixin`` to control whether ``cmd_args`` is automatically added to the module output (https://github.com/ansible-collections/community.general/pull/3648).
- module_helper module utils - added feature flag parameters to ``CmdMixin`` to control whether ``rc``, ``out`` and ``err`` are automatically added to the module output (https://github.com/ansible-collections/community.general/pull/2922).
- module_helper module utils - break down of the long file into smaller pieces (https://github.com/ansible-collections/community.general/pull/2393).
- module_helper module utils - method ``CmdMixin.run_command()`` now accepts ``process_output`` specifying a function to process the outcome of the underlying ``module.run_command()`` (https://github.com/ansible-collections/community.general/pull/2564).
- module_helper module_utils - added classmethod to trigger the execution of MH modules (https://github.com/ansible-collections/community.general/pull/3206).
- nmcli - add ``disabled`` value to ``method6`` option (https://github.com/ansible-collections/community.general/issues/2730).
- nmcli - add ``dummy`` interface support (https://github.com/ansible-collections/community.general/issues/724).
- nmcli - add ``gre`` tunnel support (https://github.com/ansible-collections/community.general/issues/3105, https://github.com/ansible-collections/community.general/pull/3262).
- nmcli - add ``gsm`` support (https://github.com/ansible-collections/community.general/pull/3313).
- nmcli - add ``routing_rules4`` and ``may_fail4`` options (https://github.com/ansible-collections/community.general/issues/2730).
- nmcli - add ``runner`` and ``runner_hwaddr_policy`` options (https://github.com/ansible-collections/community.general/issues/2901).
- nmcli - add ``wifi-sec`` option change detection to support managing secure Wi-Fi connections (https://github.com/ansible-collections/community.general/pull/3136).
- nmcli - add ``wifi`` option to support managing Wi-Fi settings such as ``hidden`` or ``mode`` (https://github.com/ansible-collections/community.general/pull/3081).
- nmcli - add new options to ignore automatic DNS servers and gateways (https://github.com/ansible-collections/community.general/issues/1087).
- nmcli - query ``nmcli`` directly to determine available WiFi options (https://github.com/ansible-collections/community.general/pull/3141).
- nmcli - remove dead code, ``options`` never contains keys from ``param_alias`` (https://github.com/ansible-collections/community.general/pull/2417).
- nmcli - the option ``routing_rules4`` can now be specified as a list of strings, instead of as a single string (https://github.com/ansible-collections/community.general/issues/3401).
- nrdp callback plugin - parameters are now converted to strings, except ``validate_certs`` which is converted to boolean (https://github.com/ansible-collections/community.general/pull/2878).
- onepassword lookup plugin - add ``domain`` option (https://github.com/ansible-collections/community.general/issues/2734).
- open-iscsi - adding support for mutual authentication between target and initiator (https://github.com/ansible-collections/community.general/pull/3422).
- open_iscsi - add ``auto_portal_startup`` parameter to allow ``node.startup`` setting per portal (https://github.com/ansible-collections/community.general/issues/2685).
- open_iscsi - also consider ``portal`` and ``port`` to check if already logged in or not (https://github.com/ansible-collections/community.general/issues/2683).
- open_iscsi - minor refactoring (https://github.com/ansible-collections/community.general/pull/3286).
- opentelemetry callback plugin - added option ``enable_from_environment`` to support enabling the plugin only if the given environment variable exists and it is set to true (https://github.com/ansible-collections/community.general/pull/3498).
- opentelemetry callback plugin - enriched the span attributes with HTTP metadata for those Ansible tasks that interact with third party systems (https://github.com/ansible-collections/community.general/pull/3448).
- opentelemetry callback plugin - enriched the stacktrace information for loops with the ``message``, ``exception`` and ``stderr`` fields from the failed item in the tasks in addition to the name of the task and failed item (https://github.com/ansible-collections/community.general/pull/3599).
- opentelemetry callback plugin - enriched the stacktrace information with the ``message``, ``exception`` and ``stderr`` fields from the failed task (https://github.com/ansible-collections/community.general/pull/3496).
- opentelemetry callback plugin - transformed args in a list of span attributes in addition it redacted username and password from any URLs (https://github.com/ansible-collections/community.general/pull/3564).
- openwrt_init - minor refactoring (https://github.com/ansible-collections/community.general/pull/3284).
- opkg - allow ``name`` to be a YAML list of strings (https://github.com/ansible-collections/community.general/issues/572, https://github.com/ansible-collections/community.general/pull/3554).
- pacman - add ``executable`` option to use an alternative pacman binary (https://github.com/ansible-collections/community.general/issues/2524).
- pacman - speed up checking if the package is installed, when the latest version check is not needed (https://github.com/ansible-collections/community.general/pull/3606).
- pamd - minor refactorings (https://github.com/ansible-collections/community.general/pull/3285).
- passwordstore lookup - add option ``missing`` to choose what to do if the password file is missing (https://github.com/ansible-collections/community.general/pull/2500).
- pids - refactor to add support for older ``psutil`` versions to the ``pattern`` option (https://github.com/ansible-collections/community.general/pull/3315).
- pipx - minor refactor on the ``changed`` logic (https://github.com/ansible-collections/community.general/pull/3647).
- pkgin - in case of ``pkgin`` tool failue, display returned standard output ``stdout`` and standard error ``stderr`` to ease debugging (https://github.com/ansible-collections/community.general/issues/3146).
- pkgng - ``annotation`` can now also be a YAML list (https://github.com/ansible-collections/community.general/pull/3526).
- pkgng - packages being installed (or upgraded) are acted on in one command (per action) (https://github.com/ansible-collections/community.general/issues/2265).
- pkgng - status message specifies number of packages installed and/or upgraded separately. Previously, all changes were reported as one count of packages "added" (https://github.com/ansible-collections/community.general/pull/3393).
- proxmox inventory plugin - added snapshots to host facts (https://github.com/ansible-collections/community.general/pull/3044).
- proxmox_group_info - minor refactor (https://github.com/ansible-collections/community.general/pull/2557).
- proxmox_kvm - minor refactor (https://github.com/ansible-collections/community.general/pull/2557).
- qubes connection - minor refactor to make lints and IDEs happy (https://github.com/ansible-collections/community.general/pull/2520).
- rax_mon_notification_plan - fixed validation checks by specifying type ``str`` as the ``elements`` of parameters ``ok_state``, ``warning_state`` and ``critical_state`` (https://github.com/ansible-collections/community.general/pull/2955).
- redfish_command - add ``boot_override_mode`` argument to BootSourceOverride commands (https://github.com/ansible-collections/community.general/issues/3134).
- redfish_command and redfish_config and redfish_utils module utils - add parameter to strip etag of quotes before patch, since some vendors do not properly ``If-Match`` etag with quotes (https://github.com/ansible-collections/community.general/pull/3296).
- redfish_config - modified module exit to add warning variable (https://github.com/ansible-collections/community.general/issues/1995).
- redfish_info - include ``Status`` property for Thermal objects when querying Thermal properties via ``GetChassisThermals`` command (https://github.com/ansible-collections/community.general/issues/3232).
- redfish_utils module utils - modified set_bios_attributes function to skip invalid attribute instead of returning. Added skipped attributes to output (https://github.com/ansible-collections/community.general/issues/1995).
- redhat_subscription - add ``server_prefix`` and ``server_port`` parameters (https://github.com/ansible-collections/community.general/pull/2779).
- redis - allow to use the term ``replica`` instead of ``slave``, which has been the official Redis terminology since 2018 (https://github.com/ansible-collections/community.general/pull/2867).
- rhevm - minor refactor (https://github.com/ansible-collections/community.general/pull/2557).
- saltstack connection - minor refactor to make lints and IDEs happy (https://github.com/ansible-collections/community.general/pull/2520).
- scaleway plugin inventory - parse scw-cli config file for ``oauth_token`` (https://github.com/ansible-collections/community.general/pull/3250).
- serverless - minor refactor (https://github.com/ansible-collections/community.general/pull/2557).
- slack - minor refactoring (https://github.com/ansible-collections/community.general/pull/3205).
- snap - added ``enabled`` and ``disabled`` states (https://github.com/ansible-collections/community.general/issues/1990).
- snap - improved module error handling, especially for the case when snap server is down (https://github.com/ansible-collections/community.general/issues/2970).
- splunk callback plugin - add ``batch`` option for user-configurable correlation ID's (https://github.com/ansible-collections/community.general/issues/2790).
- spotinst_aws_elastigroup - elements of list parameters are now validated (https://github.com/ansible-collections/community.general/pull/2355).
- ssh_config - new feature to set ``ForwardAgent`` option to ``yes`` or ``no`` (https://github.com/ansible-collections/community.general/issues/2473).
- stacki_host - minor refactoring (https://github.com/ansible-collections/community.general/pull/2681).
- supervisorctl - add the possibility to restart all programs and program groups (https://github.com/ansible-collections/community.general/issues/3551).
- supervisorctl - using standard Ansible mechanism to validate ``signalled`` state required parameter (https://github.com/ansible-collections/community.general/pull/3068).
- terraform - add ``check_destroy`` optional parameter to check for deletion of resources before it is applied (https://github.com/ansible-collections/community.general/pull/2874).
- terraform - add ``parallelism`` parameter (https://github.com/ansible-collections/community.general/pull/3540).
- terraform - add option ``overwrite_init`` to skip init if exists (https://github.com/ansible-collections/community.general/pull/2573).
- terraform - minor refactor (https://github.com/ansible-collections/community.general/pull/2557).
- timezone - print error message to debug instead of warning when timedatectl fails (https://github.com/ansible-collections/community.general/issues/1942).
- tss lookup plugin - added ``token`` parameter for token authorization; ``username`` and ``password`` are optional when ``token`` is provided (https://github.com/ansible-collections/community.general/pull/3327).
- tss lookup plugin - added new parameter for domain authorization (https://github.com/ansible-collections/community.general/pull/3228).
- tss lookup plugin - refactored to decouple the supporting third-party library (``python-tss-sdk``) (https://github.com/ansible-collections/community.general/pull/3252).
- ufw - if ``delete=true`` and ``insert`` option is present, then ``insert`` is now ignored rather than failing with a syntax error (https://github.com/ansible-collections/community.general/pull/3514).
- vdo - minor refactoring of the code (https://github.com/ansible-collections/community.general/pull/3191).
- zfs - added diff mode support (https://github.com/ansible-collections/community.general/pull/502).
- zfs_delegate_admin - drop choices from permissions, allowing any permission supported by the underlying zfs commands (https://github.com/ansible-collections/community.general/pull/2540).
- zone connection - minor refactor to make lints and IDEs happy (https://github.com/ansible-collections/community.general/pull/2520).
- zpool_facts - minor refactoring (https://github.com/ansible-collections/community.general/pull/3332).
- zypper - prefix zypper commands with ``/sbin/transactional-update --continue --drop-if-no-change --quiet run`` if transactional updates are detected (https://github.com/ansible-collections/community.general/issues/3159).

community.hashi_vault
~~~~~~~~~~~~~~~~~~~~~

- add the ``community.hashi_vault.vault`` action group (https://github.com/ansible-collections/community.hashi_vault/pull/172).
- auth methods - Add support for configuring the ``mount_point`` auth method option in plugins via the ``ANSIBLE_HASHI_VAULT_MOUNT_POINT`` environment variable, ``ansible_hashi_vault_mount_point`` ansible variable, or ``mount_point`` INI section (https://github.com/ansible-collections/community.hashi_vault/pull/171).
- community.hashi_vault collection - add cert auth method (https://github.com/ansible-collections/community.hashi_vault/pull/159).
- hashi_vault collection - add ``execution-environment.yml`` and a python requirements file to better support ``ansible-builder`` (https://github.com/ansible-collections/community.hashi_vault/pull/105).
- hashi_vault lookup - add ``ANSIBLE_HASHI_VAULT_CA_CERT`` env var (with ``VAULT_CACERT`` low-precedence fallback) for ``ca_cert`` option (https://github.com/ansible-collections/community.hashi_vault/pull/97).
- hashi_vault lookup - add ``ANSIBLE_HASHI_VAULT_PASSWORD`` env var and ``ansible_hashi_vault_password`` ansible var for ``password`` option (https://github.com/ansible-collections/community.hashi_vault/pull/96).
- hashi_vault lookup - add ``ANSIBLE_HASHI_VAULT_USERNAME`` env var and ``ansible_hashi_vault_username`` ansible var for ``username`` option (https://github.com/ansible-collections/community.hashi_vault/pull/96).
- hashi_vault lookup - add ``ansible_hashi_vault_auth_method`` Ansible vars entry to the ``proxies`` option (https://github.com/ansible-collections/community.hashi_vault/pull/86).
- hashi_vault lookup - add ``ansible_hashi_vault_ca_cert`` ansible var for ``ca_cert`` option (https://github.com/ansible-collections/community.hashi_vault/pull/97).
- hashi_vault lookup - add ``ansible_hashi_vault_namespace`` Ansible vars entry to the ``namespace`` option (https://github.com/ansible-collections/community.hashi_vault/pull/86).
- hashi_vault lookup - add ``ansible_hashi_vault_proxies`` Ansible vars entry to the ``proxies`` option (https://github.com/ansible-collections/community.hashi_vault/pull/86).
- hashi_vault lookup - add ``ansible_hashi_vault_role_id`` Ansible vars entry to the ``proxies`` option (https://github.com/ansible-collections/community.hashi_vault/pull/86).
- hashi_vault lookup - add ``ansible_hashi_vault_secret_id`` Ansible vars entry to the ``proxies`` option (https://github.com/ansible-collections/community.hashi_vault/pull/86).
- hashi_vault lookup - add ``ansible_hashi_vault_token_file`` Ansible vars entry to the ``token_file`` option (https://github.com/ansible-collections/community.hashi_vault/pull/95).
- hashi_vault lookup - add ``ansible_hashi_vault_token_path`` Ansible vars entry to the ``token_path`` option (https://github.com/ansible-collections/community.hashi_vault/pull/95).
- hashi_vault lookup - add ``ansible_hashi_vault_token_validate`` Ansible vars entry to the ``proxies`` option (https://github.com/ansible-collections/community.hashi_vault/pull/86).
- hashi_vault lookup - add ``ansible_hashi_vault_token`` Ansible vars entry to the ``proxies`` option (https://github.com/ansible-collections/community.hashi_vault/pull/86).
- hashi_vault lookup - add ``ansible_hashi_vault_url`` and ``ansible_hashi_vault_addr`` Ansible vars entries to the ``url`` option (https://github.com/ansible-collections/community.hashi_vault/pull/86).
- hashi_vault lookup - add ``ansible_hashi_vault_validate_certs`` Ansible vars entry to the ``validate_certs`` option (https://github.com/ansible-collections/community.hashi_vault/pull/95).
- hashi_vault lookup - add ``ca_cert`` INI config file key ``ca_cert`` option (https://github.com/ansible-collections/community.hashi_vault/pull/97).
- hashi_vault lookup - add ``none`` auth type which allows for passive auth via a Vault agent (https://github.com/ansible-collections/community.hashi_vault/pull/80).
- hashi_vault lookup - add ``retries`` and ``retry_action`` to enable built-in retry on failure (https://github.com/ansible-collections/community.hashi_vault/pull/71).
- hashi_vault lookup - add ``timeout`` option to control connection timeouts (https://github.com/ansible-collections/community.hashi_vault/pull/100).

community.hrobot
~~~~~~~~~~~~~~~~

- Avoid internal ansible-core module_utils in favor of equivalent public API available since at least Ansible 2.9 (https://github.com/ansible-collections/community.hrobot/pull/18).
- Generic module HTTP support code - fix usage of ``fetch_url`` with changes in latest ansible-core ``devel`` branch (https://github.com/ansible-collections/community.hrobot/pull/30).
- firewall - rename option ``whitelist_hos`` to ``allowlist_hos``, keep old name as alias (https://github.com/ansible-collections/community.hrobot/pull/15).
- firewall, firewall_info - add return value ``allowlist_hos``, which contains the same value as ``whitelist_hos``. The old name ``whitelist_hos`` will be removed eventually (https://github.com/ansible-collections/community.hrobot/pull/15).
- robot module utils - add ``allow_empty_result`` parameter to ``plugin_open_url_json`` and ``fetch_url_json`` (https://github.com/ansible-collections/community.hrobot/pull/16).

community.mongodb
~~~~~~~~~~~~~~~~~

- 338 - role monogdb_repository - Variablize repository details.
- 345 - roles mongodb_config, mongodb_mongod, mongodb_mongos - Make security.keyFile configurable.
- 346 - roles mongodb_config, mongodb_mongod, mongodb_mongos - Allow using net.bindIpAll instead of net.bindIp.
- 347 - roles mongodb_config, mongodb_mongod, mongodb_mongos - Allow overriding net.compression.compressors in mongo*.conf

community.mysql
~~~~~~~~~~~~~~~

- mysql_query - correctly reflect changed status in replace statements (https://github.com/ansible-collections/community.mysql/pull/193).
- mysql_user - replace VALID_PRIVS constant by get_valid_privs() function (https://github.com/ansible-collections/community.mysql/pull/217).

community.okd
~~~~~~~~~~~~~

- Added documentation for the ``community.okd`` collection.
- add support for turbo mode (https://github.com/openshift/community.okd/pull/102).
- increase kubernetes.core dependency version (https://github.com/openshift/community.okd/pull/97).
- openshift - inventory plugin supports FQCN ``redhat.openshift``.
- openshift_route - Add support for Route annotations (https://github.com/ansible-collections/community.okd/pull/99).

community.postgresql
~~~~~~~~~~~~~~~~~~~~

- postgresql_db - Add the ``force`` boolean option to drop active connections first and then remove the database (https://github.com/ansible-collections/community.postgresql/issues/109).
- postgresql_db - add support for the ``directory`` format when the ``state`` option is ``dump`` or ``restore`` (https://github.com/ansible-collections/community.postgresql/pull/108).
- postgresql_db - add the ``rename`` value to the ``state`` option (https://github.com/ansible-collections/community.postgresql/pull/107).
- postgresql_info - Add the ``raw`` return value for extension version (https://github.com/ansible-collections/community.postgresql/pull/138).
- postgresql_pg_hba - Add the parameters ``keep_comments_at_rules`` and ``comment`` (https://github.com/ansible-collections/community.postgresql/issues/134).

community.proxysql
~~~~~~~~~~~~~~~~~~

- Refactoring of connector presence checking (https://github.com/ansible-collections/community.proxysql/pull/50).
- Replace MySQL-Python with mysqlclient in the import error message (https://github.com/ansible-collections/community.proxysql/pull/50).
- proxysql_query_rules - add ``next_query_flagIN`` argument (https://github.com/ansible-collections/community.proxysql/pull/74).
- proxysql_query_rules - added new parameters ``cache_empty_result``, ``multiplex``, ``OK_msg`` (https://github.com/ansible-collections/community.proxysql/issues/24).
- proxysql_replication_hostgroups - implement ``check_type`` parameter (https://github.com/ansible-collections/community.proxysql/pull/69).
- refactor ``perform_checks`` function and move ``login_port`` check to ``module_utils/mysql.py`` (https://github.com/ansible-collections/community.proxysql/pull/63).

community.routeros
~~~~~~~~~~~~~~~~~~

- Avoid internal ansible-core module_utils in favor of equivalent public API available since at least Ansible 2.9 (https://github.com/ansible-collections/community.routeros/pull/38).
- api - add options ``validate_certs`` (default value ``true``), ``validate_cert_hostname`` (default value ``false``), and ``ca_path`` to control certificate validation (https://github.com/ansible-collections/community.routeros/pull/37).
- api - make validation of ``WHERE`` for ``query`` more strict (https://github.com/ansible-collections/community.routeros/pull/53).
- api - rename option ``ssl`` to ``tls``, and keep the old name as an alias (https://github.com/ansible-collections/community.routeros/pull/37).
- command - the ``commands`` and ``wait_for`` options now convert the list elements to strings (https://github.com/ansible-collections/community.routeros/pull/55).
- fact - add fact ``ansible_net_config_nonverbose`` to get idempotent config (no date, no verbose) (https://github.com/ansible-collections/community.routeros/pull/23).
- facts - the ``gather_subset`` option now converts the list elements to strings (https://github.com/ansible-collections/community.routeros/pull/55).

community.sops
~~~~~~~~~~~~~~

- Avoid internal ansible-core module_utils in favor of equivalent public API available since at least Ansible 2.9 (https://github.com/ansible-collections/community.sops/pull/73).
- sops lookup and vars plugin - allow to configure almost all generic options by ansible.cfg entries and environment variables (https://github.com/ansible-collections/community.sops/pull/81).

community.vmware
~~~~~~~~~~~~~~~~

- vm_device_helper - Add new functions for create, remove or reconfigure virutal NVDIMM device (https://github.com/ansible-collections/community.vmware/issues/853).
- vm_device_helper - move NIC device types from vmware_guest module to vm_device_helper (https://github.com/ansible-collections/community.vmware/pull/998).
- vmware - add processing to answer if the answer question is occurred in starting the vm (https://github.com/ansible-collections/community.vmware/pull/821).
- vmware - add vTPM information to default gather information (https://github.com/ansible-collections/community.vmware/pull/1082).
- vmware - added a new method to search Managed Object based on moid and object type (https://github.com/ansible-collections/community.vmware/pull/879).
- vmware - find_folder_by_fqpn added to support specifying folders by their fully qualified path name, defined as I(datacenter)/I(folder_type)/subfolder1/subfolder2/.
- vmware - folder field default changed from None to vm.
- vmware - the scenario guides from Ansible repo migrated to collection repo.
- vmware_cluster_drs - Make enable_drs an alias of enable and add a warning that the default will change from false to true in a future version (https://github.com/ansible-collections/community.vmware/pull/766)
- vmware_cluster_ha - Make enable_ha an alias of enable and add a warning that the default will change from false to true in a future version (https://github.com/ansible-collections/community.vmware/pull/766)
- vmware_cluster_vsan - Make enable_vsan an alias of enable and add a warning that the default will change from false to true in a future version (https://github.com/ansible-collections/community.vmware/pull/766)
- vmware_content_deploy_ovf_template - storage_provisioning default changed from None to thin, in keeping with VMware best practices for flash storage.
- vmware_dvs_host - implement adding pNICs to LAGs (https://github.com/ansible-collections/community.vmware/issues/112).
- vmware_dvs_portgroup - Implement 'elastic' port group configuration (https://github.com/ansible-collections/community.vmware/issues/410).
- vmware_dvs_portgroup - Implement MAC learning configuration (https://github.com/ansible-collections/community.vmware/issues/644).
- vmware_dvs_portgroup - Implement configuration of active and standby uplinks (https://github.com/ansible-collections/community.vmware/issues/709).
- vmware_dvs_portgroup - Remove default for teaming_policy.inbound_policy (https://github.com/ansible-collections/community.vmware/pull/743).
- vmware_dvs_portgroup_info - Return information about MAC learning configuration (https://github.com/ansible-collections/community.vmware/issues/644).
- vmware_dvs_portgroup_info - Return information about uplinks (https://github.com/ansible-collections/community.vmware/issues/709).
- vmware_dvswitch - Dynamically check the DVS versions vCenter supports (https://github.com/ansible-collections/community.vmware/issues/839).
- vmware_dvswitch - Implement network_policy parameter with suboptions promiscuous, forged_transmits and mac_changes (https://github.com/ansible-collections/community.vmware/issues/833).
- vmware_guest - Add new parameter 'nvdimm' for add, remove or reconfigure virutal NVDIMM device of virtual machine (https://github.com/ansible-collections/community.vmware/issues/853).
- vmware_guest - Make the requirements for Virtualization Based Security explicit (https://github.com/ansible-collections/community.vmware/pull/816).
- vmware_guest - New parameter ``secure_boot`` to manage (U)EFI secure boot on VMs (https://github.com/ansible-collections/community.vmware/pull/816).
- vmware_guest - New parameter ``vvtd`` to manage Intel Virtualization Technology for Directed I/O on VMs (https://github.com/ansible-collections/community.vmware/pull/816).
- vmware_guest - add more documentation about ``is_template`` (https://github.com/ansible-collections/community.vmware/pull/794).
- vmware_guest_controller - added bus_sharing property to scsi controllers (https://github.com/ansible-collections/community.vmware/pull/878).
- vmware_guest_cross_vc_clone - Added the is_template option to mark a cloned vm/template as a template (https://github.com/ansible-collections/community.vmware/pull/996).
- vmware_guest_disk - add the capability to create and remove RDM disks from Virtual Machines.
- vmware_guest_instant_clone - added a new option to wait until the vmware tools start (https://github.com/ansible-collections/community.vmware/pull/904).
- vmware_guest_instant_clone - added a reboot processing to reflect the customization parameters to an instant clone vm (https://github.com/ansible-collections/community.vmware/pull/904).
- vmware_guest_instant_clone - added the the guestinfo_vars parameter to provide GuestOS Customization functionality in instant cloned VM (https://github.com/ansible-collections/community.vmware/pull/796).
- vmware_guest_powerstate - Add an option that answers whether it was copied or moved the vm if the vm is blocked (https://github.com/ansible-collections/community.vmware/pull/821).
- vmware_guest_snapshot_info - add quiesced status in VM snapshot info (https://github.com/ansible-collections/community.vmware/pull/978)
- vmware_host_custom_attributes - new module (https://github.com/ansible-collections/community.vmware/pull/838).
- vmware_host_datastore - added a new parameter to expand a datastore capacity (https://github.com/ansible-collections/community.vmware/pull/915).
- vmware_host_inventory - added ability for username to be a vault encrypted variable, and updated documentation to reflect ability for username and password to be vaulted. (https://github.com/ansible-collections/community.vmware/issues/854).
- vmware_host_inventory - filter hosts before templating hostnames (https://github.com/ansible-collections/community.vmware/issues/850).
- vmware_host_inventory - support api access via proxy (https://github.com/ansible-collections/community.vmware/pull/817).
- vmware_host_iscsi_info - added a list(detected_iscsi_drives) of detected iscsi drives to the return value after set an iscsi config (https://github.com/ansible-collections/community.vmware/pull/729).
- vmware_host_passthrough - added a new module to enable or disable passthrough of PCI devices with ESXi host has (https://github.com/ansible-collections/community.vmware/pull/872).
- vmware_host_service_manager - Introducing a new state "unchanged" to allow defining startup policy without defining service state or automatically starting it (https://github.com/ansible-collections/community.vmware/issues/916).
- vmware_host_tcpip_stacks - added ipv6_gateway parameter and nsx_overlay as an alias of vxlan (https://github.com/ansible-collections/community.vmware/pull/834).
- vmware_host_vmnic_info - add LLDP information to output when applicable (https://github.com/ansible-collections/community.vmware/pull/828).
- vmware_object_custom_attributes_info - added a new parameter to support moid (https://github.com/ansible-collections/community.vmware/pull/879).
- vmware_object_role_permission_info - added principal to provide list of individual permissions on specified entity (https://github.com/ansible-collections/community.vmware/issues/868).
- vmware_portgroup - Disable traffic shaping without defining ``traffic_shaping.average_bandwidth``, ``traffic_shaping.burst_size`` and ``traffic_shaping.peak_bandwidth`` (https://github.com/ansible-collections/community.vmware/issues/955).
- vmware_rest_client - support proxy feature for module using this API (https://github.com/ansible-collections/community.vmware/pull/848).
- vmware_spbm - Add a new function 'find_storage_profile_by_name' (https://github.com/ansible-collections/community.vmware/issues/853).
- vmware_tag - modified the category_id parameter to required (https://github.com/ansible-collections/community.vmware/pull/790).
- vmware_vcenter_settings.py - Add advanced_settings parameter (https://github.com/ansible-collections/community.vmware/pull/819).
- vmware_vm_inventory - added ability for username to be a vault encrypted variable, and updated documentation to reflect ability for username and password to be vaulted. (https://github.com/ansible-collections/community.vmware/issues/854).
- vmware_vm_inventory - filter guests before templating hostnames (https://github.com/ansible-collections/community.vmware/issues/850).
- vmware_vm_inventory - set default to ``True`` for ``with_nested_properties`` (https://github.com/ansible-collections/community.vmware/issues/712).
- vmware_vm_inventory - support api access via proxy (https://github.com/ansible-collections/community.vmware/pull/817).

community.windows
~~~~~~~~~~~~~~~~~

- win_dns_record - Added txt Support
- win_domain_user - Added ``sam_account_name`` to explicitly set the ``sAMAccountName`` property of an object - https://github.com/ansible-collections/community.windows/issues/281
- win_nssm - Added ``username`` as an alias for ``user``
- win_nssm - Remove deprecation for ``state``, ``dependencies``, ``user``, ``password``, ``start_mode``
- win_nssm - Support gMSA accounts for ``user``
- win_scheduled_task - Added support for setting a ``session_state_change`` trigger by documenting the human friendly values for ``state_change``
- win_scheduled_task_state - Added ``state_change_str`` to the trigger output to give a human readable description of the value

community.zabbix
~~~~~~~~~~~~~~~~

- Added requirements.txt to collection root to be used with Ansible Builder. See https://ansible-builder.readthedocs.io/en/latest/collection_metadata.html
- all roles were updated to support Zabbix 5.4 release (https://github.com/ansible-collections/community.zabbix/pull/405)
- new inventory plugin zabbix_inventory (https://github.com/ansible-collections/community.zabbix/pull/373)
- new module plugin zabbix_globalmacro (https://github.com/ansible-collections/community.zabbix/pull/377)
- some roles are now using new naming for API connection parameters (https://github.com/ansible-collections/community.zabbix/pull/492 and https://github.com/ansible-collections/community.zabbix/pull/495).
- some roles can now utilize an option `zabbix_repo_yum_gpgcheck` to enable/disable GPG check for YUM repository (https://github.com/ansible-collections/community.zabbix/pull/438).
- zabbix inventory - Enabled the usage of environment variables in zabbix inventory plugin.
- zabbix inventory plugin - can now use environment variables ZABBIX_SERVER, ZABBIX_USERNAME and ZABBIX_PASSWORD for connection purposes to the Zabbix API.
- zabbix_agent - `zabbix_agent_loadmodule` can also be configured with a list.
- zabbix_agent - `zabbix_agent_src_reinstall` now defaults to `False` (https://github.com/ansible-collections/community.zabbix/pull/403)
- zabbix_agent - new `zabbix_api_timeout` option.
- zabbix_agent - now supports DenyKeys configuration.
- zabbix_agent - now supports setting AllowKey (https://github.com/ansible-collections/community.zabbix/pull/358)
- zabbix_globalmacros - it is now possible to create global macros using this module (https://github.com/ansible-collections/community.zabbix/pull/377).
- zabbix_hostmacro - now supports creating macros of type secret and vault.
- zabbix_inventory - Created Ansible - Zabbix inventory plugin to create dynamic inventory from Zabbix.
- zabbix_maintenance - it is now possible to target hosts by their technical name if it differs from the visible name
- zabbix_proxy (role) - new `zabbix_api_timeout` option.
- zabbix_proxy - Add MySQL Python 3 package installation.
- zabbix_proxy_info - new module that allows to retrieve information about configured Zabbix Proxies.
- zabbix_server - Add MySQL Python 3 package installation.
- zabbix_server - added support for TimescaleDB (https://github.com/ansible-collections/community.zabbix/pull/428).
- zabbix_server - now supports setting StartLLDProcessors (https://github.com/ansible-collections/community.zabbix/pull/361)
- zabbix_user - now supports parameter `username` as an alternative to `alias` (https://github.com/ansible-collections/community.zabbix/pull/406)
- zabbix_user - removed some of the default values because a configuration should be changed only if specified as a parameter (https://github.com/ansible-collections/community.zabbix/pull/382).
- zabbix_web - now supports setting SAML certificates (https://github.com/ansible-collections/community.zabbix/pull/408)

containers.podman
~~~~~~~~~~~~~~~~~

- Add Ansible 2.11 to all tests and use Ubuntu 20.04
- Add Ansible 2.11 to testing
- Add RPM building scripts
- Add support for timezones in containers
- Podman secret module

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- ome_firmware_catalog - Added support for repositories available on the Dell support site.
- ome_template_network_vlan - Added the input option which allows to apply the modified VLAN settings immediately on the associated modular-system servers.
- ome_template_network_vlan - Enabled check_mode support.

f5networks.f5_modules
~~~~~~~~~~~~~~~~~~~~~

- Add ENV variable with better name, it should make it easier to understand when disabling F5 TEEM telemetry
- Add address_matches_with_external_datagroup condition to bigip_policy_rule module
- Add cipher_groups option to bigip_server_ssl module
- Add new choices to request/response chunking parameter to accomodate TMOS v15 and above
- Add only_create_file option to bigip_ucs_fetch module
- Add option to overwrite existing conditons with the ones provided by user in bigip_policy_rule
- Add persistence target for disable action to bigip_policy_rule module
- Add reverse flag support to bigip_monitor_https
- Add rule_order parameter to bigip_policy_rule module

hetzner.hcloud
~~~~~~~~~~~~~~

- hcloud_firewall Add description field to firewall rules
- hcloud_rdns Add support for load balancer

inspur.sm
~~~~~~~~~

- Compatible with M6 models, add M6 specific fields.
- The user module adds the mailbox field.

junipernetworks.junos
~~~~~~~~~~~~~~~~~~~~~

- Add junos_logging_global Resource Module.
- Add junos_ntp_global resource module.
- Add junos_prefix_lists Resource Module.
- Add support for backup_format option in junos_config
- Change src element from str to path for junos_scp.
- Improve junos ospfv2 integration and unit tests coverage and router id assignment check implemented.
- Improve junos vlans integration and unit tests coverage and facts gathering logic modification.
- Improve junos_bgp_address_family unit test coverage.
- support l3_interface in junos vlans

kubernetes.core
~~~~~~~~~~~~~~~

- Add cache_file when DynamicClient is created (https://github.com/ansible-collections/kubernetes.core/pull/46).
- Add configmap and secret hash functionality (https://github.com/ansible-collections/kubernetes.core/pull/48).
- Add logic for cache file name generation (https://github.com/ansible-collections/kubernetes.core/pull/46).
- Replicate apply method in the DynamicClient (https://github.com/ansible-collections/kubernetes.core/pull/45).
- add ``proxy_headers`` option for authentication on k8s_xxx modules (https://github.com/ansible-collections/kubernetes.core/pull/58).
- add support for in-memory kubeconfig in addition to file for k8s modules. (https://github.com/ansible-collections/kubernetes.core/pull/212).
- add support for using tags when running molecule test suite (https://github.com/ansible-collections/kubernetes.core/pull/62).
- added documentation for ``kubernetes.core`` collection (https://github.com/ansible-collections/kubernetes.core/pull/50).
- common - removed ``KubernetesAnsibleModule``, use ``K8sAnsibleMixin`` instead (https://github.com/ansible-collections/kubernetes.core/pull/70).
- helm - add example for complex values in ``helm`` module (https://github.com/ansible-collections/kubernetes.core/issues/109).
- helm - add support for history_max cli parameter (https://github.com/ansible-collections/kubernetes.core/pull/164).
- k8s - Handle list of definition for option `template` (https://github.com/ansible-collections/kubernetes.core/pull/49).
- k8s - `continue_on_error` option added (whether to continue on creation/deletion errors) (https://github.com/ansible-collections/kubernetes.core/pull/49).
- k8s - add support for label_selectors options (https://github.com/ansible-collections/kubernetes.core/issues/43).
- k8s - add support for waiting on statefulsets (https://github.com/ansible-collections/kubernetes.core/pull/195).
- k8s - support ``patched`` value for ``state`` option. patched state is an existing resource that has a given patch applied (https://github.com/ansible-collections/kubernetes.core/pull/90).
- k8s - wait for all pods to update when rolling out daemonset changes (https://github.com/ansible-collections/kubernetes.core/pull/102).
- k8s_log - Add since-seconds parameter to the k8s_log module (https://github.com/ansible-collections/kubernetes.core/pull/142).
- k8s_scale - ability to scale multiple resource using ``label_selectors`` (https://github.com/ansible-collections/kubernetes.core/pull/114).
- k8s_scale - new parameter to determine whether to continue or not on error when scaling multiple resources (https://github.com/ansible-collections/kubernetes.core/pull/114).
- kubeconfig - update ``kubeconfig`` file location in the documentation (https://github.com/ansible-collections/kubernetes.core/issues/53).
- new lookup plugin to support kubernetes kustomize feature. (https://github.com/ansible-collections/kubernetes.core/issues/39).
- re-enable turbo mode for collection. The default is initially set to off (https://github.com/ansible-collections/kubernetes.core/pull/169).
- remove cloud.common as default dependency (https://github.com/ansible-collections/kubernetes.core/pull/148).
- remove old change log fragment files.
- remove the deprecated ``KubernetesRawModule`` class (https://github.com/ansible-collections/community.kubernetes/issues/232).
- replicate base resource for lists functionality (https://github.com/ansible-collections/kubernetes.core/pull/89).
- temporarily disable turbo mode (https://github.com/ansible-collections/kubernetes.core/pull/149).

netapp.aws
~~~~~~~~~~

- PR1 - allow usage of Ansible module group defaults - for Ansible 2.12+.
- all modules - ability to trace API calls and responses.

netapp.azure
~~~~~~~~~~~~

- PR1 - allow usage of Ansible module group defaults - for Ansible 2.12+.
- azure_rm_netapp_account - support additional authentication schemes provided by AzureRMModuleBase.
- azure_rm_netapp_capacity_pool - support additional authentication schemes provided by AzureRMModuleBase, and tags.
- azure_rm_netapp_capacity_pool - wait for completion when creating, modifying, or deleting a pool.
- azure_rm_netapp_snapshot - support additional authentication schemes provided by AzureRMModuleBase.
- azure_rm_netapp_snapshot - wait for completion when creating, modifying, or deleting a pool.
- azure_rm_netapp_volume - new option ``feature_flags`` to selectively enable/disable a feature.
- azure_rm_netapp_volume - support additional authentication schemes provided by AzureRMModuleBase, and tags.

netapp.cloudmanager
~~~~~~~~~~~~~~~~~~~

- Add CVO modification unit tests
- Adding new parameter ``capacity_package_name`` for all CVOs creation with capacity based ``license_type`` capacity-paygo or ha-capacity-paygo for HA.
- Only these parameters will be modified on the existing CVOs. svm_passowrd will be updated on each run.
- PR1 - allow usage of Ansible module group defaults - for Ansible 2.12+.
- all modules - better error reporting if refresh_token is not valid.
- na_cloudmanager - Support pd-balanced in ``gcp_volume_type`` for CVO GCP, ``provider_volume_type`` in na_cloudmanager_snapmirror and na_cloudmanager_volume.
- na_cloudmanager - Support service account with new options ``sa_client_id`` and ``sa_secret_key`` to use for API operations.
- na_cloudmanager_aggregate - Add provider_volume_type gp3 support.
- na_cloudmanager_connector_azure - Change default value of ``virtual_machine_size`` to Standard_DS3_v2.
- na_cloudmanager_connector_gcp - automatically fetch client_id for delete.
- na_cloudmanager_connector_gcp - make the module idempotent for create and delete.
- na_cloudmanager_connector_gcp - rename option ``service_account_email`` and ``service_account_path`` to ``gcp_service_account_email`` and ``gcp_service_account_path`` respectively.
- na_cloudmanager_connector_gcp - report client_id if connector already exists.
- na_cloudmanager_cvo_aws - Add ebs_volume_type gp3 support.
- na_cloudmanager_cvo_aws - Add unit tests for capacity based license support.
- na_cloudmanager_cvo_aws - Support update on svm_password, tier_level, and aws_tag.
- na_cloudmanager_cvo_aws - add new parameter ``kms_key_id`` and ``kms_key_arn`` as AWS encryption parameters to support AWS CVO encryption
- na_cloudmanager_cvo_azure - Add extra tag handling on azure_tag maintenance
- na_cloudmanager_cvo_azure - Add new parameter ``ha_enable_https`` for HA CVO to enable the HTTPS connection from CVO to storage accounts. This can impact write performance. The default is false.
- na_cloudmanager_cvo_azure - Add unit tests for capacity based license support.
- na_cloudmanager_cvo_azure - Support update on svm_password, tier_level, and azure_tag.
- na_cloudmanager_cvo_azure - add new parameter ``azure_encryption_parameters`` to support AZURE CVO encryption
- na_cloudmanager_cvo_gcp - Add extra label hendling for HA and only allow add new labels on gcp_labels
- na_cloudmanager_cvo_gcp - Add selflink support on subnet_id, vpc0_node_and_data_connectivity, vpc1_cluster_connectivity, vpc2_ha_connectivity, vpc3_data_replication, subnet0_node_and_data_connectivity, subnet1_cluster_connectivity, subnet2_ha_connectivity, and subnet3_data_replication.
- na_cloudmanager_cvo_gcp - Add unit tests for capacity based license support and delete cvo.
- na_cloudmanager_cvo_gcp - Support update on svm_password, tier_level, and gcp_labels.
- na_cloudmanager_cvo_gcp - add new parameter ``gcp_encryption_parameters`` to support GCP CVO encryption
- na_cloudmanager_snapmirror - Add provider_volume_type gp3 support.
- na_cloudmanager_snapmirror - working environment get information api not working for onprem is fixed
- na_cloudmanager_volume - Add aggregate_name support on volume creation.
- na_cloudmanager_volume - Add provider_volume_type gp3 support.
- netapp.py - improve error handling with error content.

netapp.elementsw
~~~~~~~~~~~~~~~~

- PR1 - allow usage of Ansible module group defaults - for Ansible 2.12+.

netapp.ontap
~~~~~~~~~~~~

- License displayed correctly in Github
- PR15 - allow usage of Ansible module group defaults - for Ansible 2.12+.
- na_ontap_cifs - new option ``comment`` to associate a description to a CIFS share.
- na_ontap_cifs_server - ``force`` option is supported when state is absent to ignore communication errors.
- na_ontap_cluster - Added REST support to the cluster module.
- na_ontap_cluster - add ``force`` option when deleting a node.
- na_ontap_cluster_peer - new option ``peer_options`` to use different credentials on peer.
- na_ontap_debug - additional checks when REST is available to help debug vserver connectivity issues.
- na_ontap_disks - added REST support for the module.
- na_ontap_disks - added functionality to reassign spare disks from a partner node to the desired node.
- na_ontap_disks - new option min_spares.
- na_ontap_firewall_policy - added ``none`` as a choice for ``service`` which is supported from 9.8 ONTAP onwards.
- na_ontap_flexcache - corrected module name in documentation Examples
- na_ontap_interface - Added REST support to the interface module (for IP and FC interfaces).
- na_ontap_interface - new option ``from_name`` to rename an interface.
- na_ontap_job_schedule - new option ``month_offset`` to explictly select 0 or 1 for January.
- na_ontap_lun - new suboption ``exclude_aggregates`` for SAN application.
- na_ontap_net_port - change option types to bool and int respectively for ``autonegotiate_admin`` and ``mtu``.
- na_ontap_net_port - new option ``up_admin`` to set administrative state.
- na_ontap_net_vlan - Added REST support to the net vlan module.
- na_ontap_net_vlan - new REST options ``broadcast_domain``, ``ipspace`` and ``enabled`` added.
- na_ontap_ntp - Added REST support to the ntp module
- na_ontap_object_store - new REST options ``owner`` and ``change_password``.
- na_ontap_object_store - new option ``port``, ``certificate_validation_enabled``, ``ssl_enabled`` for target server.
- na_ontap_object_store - support modifying an object store config with REST.
- na_ontap_rest_info - Added "autosupport_check_info"/"support/autosupport/check" to the attributes that will be collected when gathering info using the module.
- na_ontap_rest_info - All Info that exist in ``na_ontap_info`` that has REST equivalents have been implemented. Note that the returned structure for REST and the variable names in the structure is different from the ZAPI based ``na_ontap_info``. Some default variables in ZAPI are no longer returned by default in REST and will need to be specified using the ``field`` option.
- na_ontap_rest_info - The Default for ``gather_subset`` has been changed to demo which returns ``cluster/software``, ``svm/svms``, ``cluster/nodes``. To return all Info must specificly list ``all`` in your playbook. Do note ``all`` is a very resource-intensive action and it is highly recommended to call just the info/APIs you need.
- na_ontap_rest_info - The following info subsets have been added ``system_node_info``, ``net_interface_info``, ``net_port_info``, ``security_login_account_info``, ``vserver_peer_info``, ``cluster_image_info``, ``cluster_log_forwarding_info``, ``metrocluster_info``, ``metrocluster_node_info``, ``net_dns_info``, ``net_interface_service_policy_info``, ``vserver_nfs_info``, ``clock_info``, ``igroup_info``, ``vscan_status_info``, ``vscan_connection_status_all_info``, ``storage_bridge_info``, ``nvme_info``, ``nvme_interface_info``, ``nvme_subsystem_info``, ``cluster_switch_info``, ``export_policy_info``, ``kerberos_realm_info``,``sis_info``, ``sis_policy_info``, ``snapmirror_info``, ``snapmirror_destination_info``, ``snapmirror_policy_info``, ``sys_cluster_alerts``, ``cifs_vserver_security_info``
- na_ontap_rest_info - add examples for ``parameters`` option.
- na_ontap_rest_info - added file_directory_security to return the effective permissions of the directory. When using file_directory_security it must be called with gather_subsets and path and vserver must be specified in parameters.
- na_ontap_rest_info - new option ``use_python_keys`` to replace ``svm/svms`` with ``svm_svms`` to simplify post processing.
- na_ontap_snapshot - add REST support to create, modify, rename, and delete snapshot.
- na_ontap_snapshot - new option ``expiry_time``.
- na_ontap_snmp - Added REST support to the SNMP module
- na_ontap_software_update - new option ``validate_after_download`` to run ONTAP software update validation checks.
- na_ontap_software_update - remove ``absent`` as a choice for ``state`` as it has no use.
- na_ontap_svm - ignore ``aggr_list`` with ``'*'`` when using REST.
- na_ontap_svm - new option ``ignore_rest_unsupported_options`` to ignore older ZAPI options not available in REST.
- na_ontap_svm - new option ``max_volumes``.
- na_ontap_svm - new option ``services`` to allow and/or enable protocol services.
- na_ontap_svm - support ``allowed protocols`` with REST for ONTAP 9.6 and later.
- na_ontap_users - new option ``application_dicts`` to associate multiple authentication methods to an application.
- na_ontap_users - new option ``application_strs`` to disambiguate ``applications``.
- na_ontap_users - new option ``replace_existing_apps_and_methods``.
- na_ontap_users - new suboption ``second_authentication_method`` with ``application_dicts`` option.
- na_ontap_volume - new suboption ``exclude_aggregates`` for NAS application.
- na_ontap_volume - show warning when resize is ignored because threshold is not reached.
- na_ontap_vserver_create role - add ``nfsv3``, ``nfsv4``, ``nfsv41`` options.
- na_ontap_vserver_peer - new option ``peer_options`` to use different credentials on peer.
- na_ontap_vserver_peer - new options ``local_name_for_source`` and ``local_name_for_peer`` added.

netapp.um_info
~~~~~~~~~~~~~~

- PR1 - allow usage of Ansible module group defaults - for Ansible 2.12+.
- all modules - ability to trace API calls and responses.
- all modules - new ``max_records`` option to limit the amount of data in a single GET response.
- na_um_list_aggregates has been renamed na_um_aggregates_info.
- na_um_list_clusters has been renamed na_um_clusters_info.
- na_um_list_nodes has been renamed na_um_nodes_info.
- na_um_list_svms has been renamed na_um_svms_info.
- na_um_list_volumes has been renamed na_um_volumes_info.

netapp_eseries.santricity
~~~~~~~~~~~~~~~~~~~~~~~~~

- Add eseries_system_old_password variable to faciliate changing the storage system's admin password.
- Add login banner message to na_santricity_global module and nar_santricity_management role.
- Add remove_unspecified_user_certificates variable to the client certificates module.
- Add usable drive option for na_santricity_storagepool module and nar_santricity_host role which can be used to choose selected drives for storage pool/volumes or define a pattern drive selection.

netbox.netbox
~~~~~~~~~~~~~

- Add ansible-core support - Quick fix to support ansible-core 2.11 [#558](https://github.com/netbox-community/ansible_modules/pull/558)
- Add connected-devices to nb_lookup [#540](https://github.com/netbox-community/ansible_modules/pull/540)
- Add location and power panel as lookup keys to nb_lookup [#599](https://github.com/netbox-community/ansible_modules/pull/599)
- Add private_key option to nb_lookup for secret decryption [#532](https://github.com/netbox-community/ansible_modules/pull/532)
- Added custom certificate support [#534](https://github.com/netbox-community/ansible_modules/pull/534)
- CI testing & integration tests now leverage ansible-core 2.11 - Fixes #583: Move to Ansible-core for CI tests  [#591](https://github.com/netbox-community/ansible_modules/pull/591)
- Correct Invalid NetBox readthedocs URL in nb_inventory docs [#568](https://github.com/netbox-community/ansible_modules/pull/568)
- Fixes to CI due to not pinning NetBox & NetBox-Docker version CI among other minor CI corrections - General CI Fix [573](https://github.com/netbox-community/ansible_modules/pull/573)
- Improve speed of netbox_cable module on NetBox version 3.0.6 or later [#624](https://github.com/netbox-community/ansible_modules/pull/624)
- README: Slack link and tidyup [#584](https://github.com/netbox-community/ansible_modules/pull/584)
- Release v3.1.2 [#594](https://github.com/netbox-community/ansible_modules/pull/594)
- Update netbox_region documentation - Documentation: netbox_region - Correct examples [#548](https://github.com/netbox-community/ansible_modules/pull/548)
- netbox_config_context - add module for handling Config Context [#610](https://github.com/netbox-community/ansible_modules/pull/610)
- netbox_device_interface - Add custom_fields [#514](https://github.com/netbox-community/ansible_modules/pull/514)
- netbox_device_interface - Add label option.
- netbox_device_interface - Add mark_connected option.
- netbox_device_interface and netbox_vm_interface - Add parent interface to modules [#604](https://github.com/netbox-community/ansible_modules/pull/604)
- netbox_location - add module for handling Location [#543](https://github.com/netbox-community/ansible_modules/pull/543)
- netbox_power_panel - Add location option.
- netbox_rack - Add location option.
- netbox_site_group - add module for handling Site Group [#547](https://github.com/netbox-community/ansible_modules/pull/547)
- netbox_virtual_machine - Change vCPU to float from int (to reflect NetBox 3.0) [#605](https://github.com/netbox-community/ansible_modules/pull/605)
- netbox_vlan_group - Add custom_fields option.
- netbox_vlan_group - Add description option.
- netbox_vlan_group - Add scope option.
- netbox_vlan_group - Add scope_type option.

ngine_io.cloudstack
~~~~~~~~~~~~~~~~~~~

- cs_instance - add support for MAC address and IPv6 in ``ip_to_networks`` (https://github.com/ngine-io/ansible-collection-cloudstack/issues/78).
- cs_instance_info - implemented support for ``host`` filter (https://github.com/ngine-io/ansible-collection-cloudstack/pull/83).
- cs_network_offering - implemented support for ``tags``, ``zones`` and ``domains`` (https://github.com/ngine-io/ansible-collection-cloudstack/pull/82).

ovirt.ovirt
~~~~~~~~~~~

- Don't rely on safe_eval being able to do math/concat (https://github.com/oVirt/ovirt-ansible-collection/pull/307)
- disaster_recovery - Change conf paths (https://github.com/oVirt/ovirt-ansible-collection/pull/286).
- engine_setup - Wait for webserver up after engine-config reboot (https://github.com/oVirt/ovirt-ansible-collection/pull/324).
- gluster_heal_info - Replacing gluster module to CLI to support RHV automation hub (https://github.com/oVirt/ovirt-ansible-collection/pull/340).
- hosted_engine_setup - Add-pause-option-before-engine-setup (https://github.com/oVirt/ovirt-ansible-collection/pull/273).
- hosted_engine_setup - Allow FIPS on HE VM (https://github.com/oVirt/ovirt-ansible-collection/pull/313)
- hosted_engine_setup - Do not try to sync at end of full_execution (https://github.com/oVirt/ovirt-ansible-collection/pull/305)
- hosted_engine_setup - Fix engine vm add_host for the target machine (https://github.com/oVirt/ovirt-ansible-collection/pull/311)
- hosted_engine_setup - Minor doc update (https://github.com/oVirt/ovirt-ansible-collection/pull/310)
- hosted_engine_setup - Pause deployment on failure of `engine-backup --mode=restore` (https://github.com/oVirt/ovirt-ansible-collection/pull/327).
- hosted_engine_setup - Remove leftover code and omit parameters (https://github.com/oVirt/ovirt-ansible-collection/pull/281).
- hosted_engine_setup - Text change - Consistently use 'bootstrap engine VM' (https://github.com/oVirt/ovirt-ansible-collection/pull/328).
- hosted_engine_setup - Update Ansible requirements in README (https://github.com/oVirt/ovirt-ansible-collection/pull/321)
- hosted_engine_setup - use-ansible-host (https://github.com/oVirt/ovirt-ansible-collection/pull/277).
- infra - Storage fix parameters typo (https://github.com/oVirt/ovirt-ansible-collection/pull/282).
- infra role - Add external_provider parameter on networks role of infra role (https://github.com/oVirt/ovirt-ansible-collection/pull/297)
- ovirt_host - Update iscsi target struct (https://github.com/oVirt/ovirt-ansible-collection/pull/274).
- ovirt_vm - Add default return value to check_placement_policy (https://github.com/oVirt/ovirt-ansible-collection/pull/301).
- ovirt_vm - Add placement_policy_hosts (https://github.com/oVirt/ovirt-ansible-collection/pull/294).
- readme - Update Ansible requirement (https://github.com/oVirt/ovirt-ansible-collection/pull/326).
- remove_stale_lun - Fix example for `remote_stale_lun` role to be able to run it from engine (https://github.com/oVirt/ovirt-ansible-collection/pull/334).
- repositories - Replace redhat_subscription and rhsm_repository with command (https://github.com/oVirt/ovirt-ansible-collection/pull/346).
- repositories - Update host and engine repositories to 4.4.9 (https://github.com/oVirt/ovirt-ansible-collection/pull/363).
- repositories - add no_log to register (https://github.com/oVirt/ovirt-ansible-collection/pull/350).

purestorage.flasharray
~~~~~~~~~~~~~~~~~~~~~~

- purefa_ad - Increase number of kerberos and directory servers to be 3 for each.
- purefa_ad - New module to manage Active Directory accounts
- purefa_dirsnap - New modules to manage FA-Files directory snapshots
- purefa_ds - Add ``join_ou`` parameter for AD account creation
- purefa_eradication - New module to set deleted items eradication timer
- purefa_host - Deprecate ``protocol`` parameter. No longer required.
- purefa_info - Add NVMe NGUID value for volumes
- purefa_info - Add array, volume and snapshot detailed capacity information
- purefa_info - Add data-at-rest and eradication timer information to default dict
- purefa_info - Add deleted members to volume protection group info
- purefa_info - Add high-level count for directory quotas and details for all FA-Files policies
- purefa_info - Add snapshot policy rules suffix support
- purefa_info - Add volume Page 83 NAA information for volume details
- purefa_info - Remove directory_services field. Deprecated in Collections 1.6
- purefa_kmip - Add support for KMIP server management
- purefa_network - Add support for enable/diable FC ports
- purefa_policy - Add snapshot policy rules suffix support
- purefa_policy - Add support for FA-files Directory Quotas and associated rules and members
- purefa_sso - Add support for setting FlashArray Single Sign-On from Pure1 Manage
- purefa_syslog_settings - Add support to manage global syslog server settings
- purefa_volume - Add NVMe NGUID to response dict
- purefa_volume - Add volume Page 83 NAA information to response dict

purestorage.flashblade
~~~~~~~~~~~~~~~~~~~~~~

- purefb.py - Add check to ensure FlashBlade uses the latest REST version possible for Purity version installed
- purefb.py - Use latest `pypureclient` SDK with fix for "best fit". No longer requires double login to negotiate best API version.
- purefb_groupquota - New module for manage individual filesystem group quotas
- purefb_info - Add object lifecycles rules to bucket subset
- purefb_lag - Add support for LAG management
- purefb_lifecycle - Add support for updated object lifecycle rules. See documentation for details of new parameters.
- purefb_lifecycle - Change `keep_for` parameter to be `keep_previous_for`. `keep_for` is deprecated and will be removed in a later version.
- purefb_snap - Add support for immeadiate snapshot to remote connected FlashBlade
- purefb_subnet - Add support for multiple LAGs.
- purefb_user - Add support for managing user public key and user unlock
- purefb_userquota - New module for manage individual filesystem user quotas

sensu.sensu_go
~~~~~~~~~~~~~~

- Add Sensu Go 6.4.0 Windows metadata.
- Add Sensu Go 6.4.1 Windows metadata.
- Add argument specification to the agent role.
- Add argument specification to the backend role.
- Add argument specification to the install role.
- Add modules for managing Sensu Go authentication providers.
- Add support for OracleLinux.
- Update list of available Sensu Go agent packages for Windows installations (added 6.3.0).

t_systems_mms.icinga_director
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Add event_command parameter to icinga_service_apply module (https://github.com/T-Systems-MMS/ansible-collection-icinga-director/pull/132)
- Add event_command parameter to service apply playbook to enable usage (https://github.com/T-Systems-MMS/ansible-collection-icinga-director/pull/133)
- Add some more documentation on command template (https://github.com/T-Systems-MMS/ansible-collection-icinga-director/pull/128)
- Add support for retry_interval and max_check_attempts to host template (https://github.com/T-Systems-MMS/ansible-collection-icinga-director/pull/140)
- add "vars" variable to icinga_notification in the role (https://github.com/T-Systems-MMS/ansible-collection-icinga-director/pull/129)
- add notification_template to role (https://github.com/T-Systems-MMS/ansible-collection-icinga-director/pull/125)
- add resolve option to inventory-plugin (https://github.com/T-Systems-MMS/ansible-collection-icinga-director/pull/147)

theforeman.foreman
~~~~~~~~~~~~~~~~~~

- Add a domain_info module
- Add a hostgroups role (https://github.com/theforeman/foreman-ansible-modules/issues/1116)
- Add a role `content_rhel` to perform basic setup for registering and syncing RHEL content hosts
- Add content credentials role
- callback plugin - collect facts during the run, merge them correctly and upload them once at the end
- compute_resource - add ``cloud`` param for the AzureRm provider, to select which Azure cloud to use
- compute_resource - add ``sub_id`` parameter for handling the Azure Subscription ID instead of the ``user`` parameter
- host - Add ``Redfish`` to list of possible BMC providers of an interface
- host, compute_profile - look up the correct id for storage pods and domains given as part of ``volumes_attributes`` (https://bugzilla.redhat.com/show_bug.cgi?id=1885234)
- hostgroup - add a ``ansible_roles`` parameter (https://github.com/theforeman/foreman-ansible-modules/issues/1123)
- new ``content_views`` role to manage content views (https://github.com/theforeman/foreman-ansible-modules/issues/1111)
- new ``organizations`` role to manage organizations (https://github.com/theforeman/foreman-ansible-modules/issues/1109)
- repository - add support for filtering repositories by OS version based on API feature apidoc/v2/repositories/create.html
- subnet - add ``bmc_proxy`` parameter to configure BMC proxies for subnets

vyos.vyos
~~~~~~~~~

- Add vyos_ntp Resource Module
- Add vyos_prefix_lists Resource Module.
- Add vyos_route_maps resource module (https://github.com/ansible-collections/vyos.vyos/pull/156.).
- Adds support for specifying an `afi` for an `address_group` for `vyos.vyos.firewall_global`.  As a result, `address_group` now supports IPv6.
- Adds support for specifying an `afi` for an `network_group` for `vyos.vyos.firewall_global`.  As a result, `network_group` now supports IPv6.
- vyos_logging_global logging resource module.

Breaking Changes / Porting Guide
--------------------------------

Ansible-core
~~~~~~~~~~~~

- Action, module, and group names in module_defaults must be static values. Their values can still be templates.
- Fully qualified 'ansible.legacy' plugin names are not included implicitly in action_groups.
- Unresolvable groups, action plugins, and modules in module_defaults are an error.
- ansible-test - Automatic installation of requirements for "cloud" test plugins no longer occurs. The affected test plugins are ``aws``, ``azure``, ``cs``, ``hcloud``, ``nios``, ``opennebula``, ``openshift`` and ``vcenter``. Collections should instead use one of the supported integration test requirements files, such as the ``tests/integration/requirements.txt`` file.
- ansible-test - The HTTP Tester is no longer available with the ``ansible-test shell`` command. Only the ``integration`` and ``windows-integration`` commands provide HTTP Tester.
- ansible-test - The ``--disable-httptester`` option is no longer available. The HTTP Tester is no longer optional for tests that specify it.
- ansible-test - The ``--httptester`` option is no longer available. To override the container used for HTTP Tester tests, set the ``ANSIBLE_HTTP_TEST_CONTAINER`` environment variable instead.
- ansible-test - Unit tests for ``modules`` and ``module_utils`` are now limited to importing only ``ansible.module_utils`` from the ``ansible`` module.
- conditionals - ``when`` conditionals no longer automatically parse string booleans such as ``"true"`` and ``"false"`` into actual booleans. Any non-empty string is now considered true. The ``CONDITIONAL_BARE_VARS`` configuration variable no longer has any effect.
- hostname - Drops any remaining support for Python 2.4 by using ``with open()`` to simplify exception handling code which leaked file handles in several spots
- hostname - On FreeBSD, the string ``temporarystub`` no longer gets written to the hostname file in the get methods (and in check_mode). As a result, the default hostname will now appear as ``''`` (empty string) instead of ``temporarystub`` for consistency with other strategies. This means the ``before`` result will be different.
- hostname - On OpenRC systems and Solaris, the ``before`` value will now be ``''`` (empty string) if the permanent hostname file does not exist, for consistency with other strategies.
- intersect, difference, symmetric_difference, union filters - the default behavior is now to be case-sensitive (https://github.com/ansible/ansible/issues/74255)
- unique filter - the default behavior is now to fail if Jinja2's filter fails and explicit ``case_sensitive=False`` as the Ansible's fallback is case-sensitive (https://github.com/ansible/ansible/pull/74256)

amazon.aws
~~~~~~~~~~

- ec2_instance - instance wait for state behaviour has changed.  If plays require the old behavior of waiting for the instance monitoring status to become ``OK`` when launching a new instance, the action will need to specify ``state: started`` (https://github.com/ansible-collections/amazon.aws/pull/481).
- ec2_snapshot - support for waiting indefinitely has been dropped, new default is 10 minutes (https://github.com/ansible-collections/amazon.aws/pull/356).
- ec2_vol_info - return ``attachment_set`` is now a list of attachments with Multi-Attach support on disk. (https://github.com/ansible-collections/amazon.aws/pull/362).
- ec2_vpc_dhcp_option - The module has been refactored to use boto3. Keys and value types returned by the module are now consistent, which is a change from the previous behaviour. A ``purge_tags`` option has been added, which defaults to ``True``.  (https://github.com/ansible-collections/amazon.aws/pull/252)
- ec2_vpc_dhcp_option_info - Now preserves case for tag keys in return value. (https://github.com/ansible-collections/amazon.aws/pull/252)
- module_utils.core - The boto3 switch has been removed from the region parameter (https://github.com/ansible-collections/amazon.aws/pull/287).
- module_utils/compat - vendored copy of ipaddress removed (https://github.com/ansible-collections/amazon.aws/pull/461).
- module_utils/core - updated the ``scrub_none_parameters`` function so that ``descend_into_lists`` is set to ``True`` by default (https://github.com/ansible-collections/amazon.aws/pull/297).

arista.eos
~~~~~~~~~~

- Arista released train 4.23.X and newer and along with it replaced and deprecated lots of commands. This PR adds support for syntax changes in release train 4.23 and after. Going forward the eos modules will not support eos sw version < 4.23.

community.aws
~~~~~~~~~~~~~

- ec2_instance - The module has been migrated to the ``amazon.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.ec2_instance``.
- ec2_instance_info - The module has been migrated to the ``amazon.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.ec2_instance_info``.
- ec2_vpc_endpoint - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.ec2_vpc_endpoint``.
- ec2_vpc_endpoint_facts - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.ec2_vpc_endpoint_info``.
- ec2_vpc_endpoint_info - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.ec2_vpc_endpoint_info``.
- ec2_vpc_endpoint_service_info - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.ec2_vpc_endpoint_service_info``.
- ec2_vpc_igw - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.ec2_vpc_igw``.
- ec2_vpc_igw_facts - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.ec2_vpc_igw_info``.
- ec2_vpc_igw_info - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.ec2_vpc_igw_info``.
- ec2_vpc_nat_gateway - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.ec2_vpc_nat_gateway``.
- ec2_vpc_nat_gateway_facts - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.ec2_vpc_nat_gateway_info``.
- ec2_vpc_nat_gateway_info - The module has been migrated from the ``community.aws`` collection. Playbooks using the Fully Qualified Collection Name for this module should be updated to use ``amazon.aws.ec2_vpc_nat_gateway_info``.
- kms_info - key details are now returned in the ``kms_keys`` attribute rather than the ``keys`` attribute (https://github.com/ansible-collections/community.aws/pull/648).

community.crypto
~~~~~~~~~~~~~~~~

- Adjust ``dirName`` text parsing and to text converting code to conform to `Sections 2 and 3 of RFC 4514 <https://datatracker.ietf.org/doc/html/rfc4514.html>`_. This is similar to how `cryptography handles this <https://cryptography.io/en/latest/x509/reference/#cryptography.x509.Name.rfc4514_string>`_ (https://github.com/ansible-collections/community.crypto/pull/274).
- acme module utils - removing compatibility code (https://github.com/ansible-collections/community.crypto/pull/290).
- acme_* modules - removed vendored copy of the Python library ``ipaddress``. If you are using Python 2.x, please make sure to install the library (https://github.com/ansible-collections/community.crypto/pull/287).
- compatibility module_utils - removed vendored copy of the Python library ``ipaddress`` (https://github.com/ansible-collections/community.crypto/pull/287).
- crypto module utils - removing compatibility code (https://github.com/ansible-collections/community.crypto/pull/290).
- get_certificate, openssl_csr_info, x509_certificate_info - depending on the ``cryptography`` version used, the modules might not return the ASN.1 value for an extension as contained in the certificate respectively CSR, but a re-encoded version of it. This should usually be identical to the value contained in the source file, unless the value was malformed. For extensions not handled by C(cryptography) the value contained in the source file is always returned unaltered (https://github.com/ansible-collections/community.crypto/pull/318).
- module_utils - removed various PyOpenSSL support functions and default backend values that are not needed for the openssl_pkcs12 module (https://github.com/ansible-collections/community.crypto/pull/273).
- openssl_csr, openssl_csr_pipe, x509_crl - the ``subject`` respectively ``issuer`` fields no longer ignore empty values, but instead fail when encountering them (https://github.com/ansible-collections/community.crypto/pull/316).
- openssl_privatekey_info - by default consistency checks are not run; they need to be explicitly requested by passing ``check_consistency=true`` (https://github.com/ansible-collections/community.crypto/pull/309).
- x509_crl - for idempotency checks, the ``issuer`` order is ignored. If order is important, use the new ``issuer_ordered`` option (https://github.com/ansible-collections/community.crypto/pull/316).

community.docker
~~~~~~~~~~~~~~~~

- docker_compose - fixed ``timeout`` defaulting behavior so that ``stop_grace_period``, if defined in the compose file, will be used if `timeout`` is not specified (https://github.com/ansible-collections/community.docker/pull/163).

community.general
~~~~~~~~~~~~~~~~~

- archive - adding idempotency checks for changes to file names and content within the ``destination`` file (https://github.com/ansible-collections/community.general/pull/3075).
- lxd inventory plugin - when used with Python 2, the plugin now needs ``ipaddress`` installed `from pypi <https://pypi.org/project/ipaddress/>`_ (https://github.com/ansible-collections/community.general/pull/2441).
- scaleway_security_group_rule - when used with Python 2, the module now needs ``ipaddress`` installed `from pypi <https://pypi.org/project/ipaddress/>`_ (https://github.com/ansible-collections/community.general/pull/2441).

community.hashi_vault
~~~~~~~~~~~~~~~~~~~~~

- connection options - there is no longer a default value for the ``url`` option (the Vault address), so a value must be supplied (https://github.com/ansible-collections/community.hashi_vault/issues/83).

community.okd
~~~~~~~~~~~~~

- drop python 2 support (https://github.com/openshift/community.okd/pull/93).

community.routeros
~~~~~~~~~~~~~~~~~~

- api - due to a programming error, the module never failed on errors. This has now been fixed. If you are relying on the module not failing in case of idempotent commands (resulting in errors like ``failure: already have such address``), you need to adjust your roles/playbooks. We suggest to use ``failed_when`` to accept failure in specific circumstances, for example ``failed_when: "'failure: already have ' in result.msg[0]"`` (https://github.com/ansible-collections/community.routeros/pull/39).
- api - splitting commands no longer uses a naive split by whitespace, but a more RouterOS CLI compatible splitting algorithm (https://github.com/ansible-collections/community.routeros/pull/45).
- command - the module now always indicates that a change happens. If this is not correct, please use ``changed_when`` to determine the correct changed status for a task (https://github.com/ansible-collections/community.routeros/pull/50).

community.zabbix
~~~~~~~~~~~~~~~~

- all roles now reference other roles and modules via their fully qualified collection names, which makes Ansible 2.10 minimum supported version for roles (See https://github.com/ansible-collections/community.zabbix/pull/477).

kubernetes.core
~~~~~~~~~~~~~~~

- Drop python 2 support (https://github.com/ansible-collections/kubernetes.core/pull/86).
- helm_plugin - remove unused ``release_namespace`` parameter (https://github.com/ansible-collections/kubernetes.core/pull/85).
- helm_plugin_info - remove unused ``release_namespace`` parameter (https://github.com/ansible-collections/kubernetes.core/pull/85).
- k8s_cluster_info - returned apis as list to avoid being overwritten in case of multiple version (https://github.com/ansible-collections/kubernetes.core/pull/41).
- k8s_facts - remove the deprecated alias from k8s_facts to k8s_info (https://github.com/ansible-collections/kubernetes.core/pull/125).

Deprecated Features
-------------------

Ansible-core
~~~~~~~~~~~~

- ansible-test - The ``--docker-no-pull`` option is deprecated and has no effect.
- ansible-test - The ``--no-pip-check`` option is deprecated and has no effect.
- include action is deprecated in favor of include_tasks, import_tasks and import_playbook.
- module_utils' FileLock is scheduled to be removed, it is not used due to its unreliable nature.

amazon.aws
~~~~~~~~~~

- ec2 - the boto based ``ec2`` module has been deprecated in favour of the boto3 based ``ec2_instance`` module. The ``ec2`` module will be removed in release 4.0.0 (https://github.com/ansible-collections/amazon.aws/pull/424).
- ec2_classic_lb - setting of the ``ec2_elb`` fact has been deprecated and will be removed in release 4.0.0 of the collection. The module now returns ``elb`` which can be accessed using the register keyword (https://github.com/ansible-collections/amazon.aws/pull/552).
- ec2_vpc_dhcp_option - The ``new_config`` return key has been deprecated and will be removed in a future release.  It will be replaced by ``dhcp_config``.  Both values are returned in the interim. (https://github.com/ansible-collections/amazon.aws/pull/252)

ansible.netcommon
~~~~~~~~~~~~~~~~~

- network_cli - The paramiko_ssh setting ``look_for_keys`` was set automatically based on the values of the ``password`` and ``private_key_file`` options passed to network_cli. This option can now be set explicitly, and the automatic setting of ``look_for_keys`` will be removed after 2024-01-01  (https://github.com/ansible-collections/ansible.netcommon/pull/271).

ansible.windows
~~~~~~~~~~~~~~~

- win_reboot - Unreachable hosts can be ignored with ``ignore_errors: True``, this ability will be removed in a future version. Use ``ignore_unreachable: True`` to ignore unreachable hosts instead. - https://github.com/ansible-collections/ansible.windows/issues/62
- win_updates - Deprecated the ``filtered_reason`` return value for each filtered up in favour of ``filtered_reasons``. This has been done to show all the reasons why an update was filtered and not just the first reason.
- win_updates - Deprecated the ``use_scheduled_task`` option as it is no longer used.
- win_updates - Deprecated the ``whitelist`` and ``blacklist`` options in favour of ``accept_list`` and ``reject_list`` respectively to conform to the new standards used in Ansible for these types of options.

arista.eos
~~~~~~~~~~

- Remove testing with provider for ansible-test integration jobs. This helps prepare us to move to network-ee integration tests.

cisco.ios
~~~~~~~~~

- Deprecated ios_bgp in favor of ios_bgp_global and ios_bgp_address_family.
- Deprecated ios_ntp modules.
- Remove testing with provider for ansible-test integration jobs. This helps prepare us to move to network-ee integration tests.

cisco.iosxr
~~~~~~~~~~~

- The iosxr_logging module has been deprecated in favor of the new iosxr_logging_global resource module and will be removed in a release after '2023-08-01'.

cisco.nxos
~~~~~~~~~~

- Deprecated `nxos_ntp`, `nxos_ntp_options`, `nxos_ntp_auth` modules.
- The nxos_logging module has been deprecated in favor of the new nxos_logging_global resource module and will be removed in a release after '2023-08-01'.

community.aws
~~~~~~~~~~~~~

- dynamodb_table - DynamoDB does not support specifying non-key-attributes when creating an ``ALL`` index.  Passing ``includes`` for such indexes is currently ignored but will result in failures after version 3.0.0 (https://github.com/ansible-collections/community.aws/pull/726).
- dynamodb_table - DynamoDB does not support updating the primary indexes on a table.  Attempts to make such changes are currently ignored but will result in failures after version 3.0.0 (https://github.com/ansible-collections/community.aws/pull/726).
- ec2_elb - the ``ec2_elb`` module has been removed and redirected to the ``elb_instance`` module which functions identically. The original ``ec2_elb`` name is now deprecated and will be removed in release 3.0.0 (https://github.com/ansible-collections/community.aws/pull/586).
- ec2_elb_info - the boto based ``ec2_elb_info`` module has been deprecated in favour of the boto3 based ``elb_classic_lb_info`` module. The ``ec2_elb_info`` module will be removed in release 3.0.0 (https://github.com/ansible-collections/community.aws/pull/586).
- elb_classic_lb - the ``elb_classic_lb`` module has been removed and redirected to the ``amazon.aws.ec2_elb_lb`` module which functions identically.
- elb_instance - setting of the ``ec2_elb`` fact has been deprecated and will be removed in release 4.0.0 of the collection. See the module documentation for an alternative example using the register keyword (https://github.com/ansible-collections/community.aws/pull/773).
- iam - the boto based ``iam`` module has been deprecated in favour of the boto3 based ``iam_user``, ``iam_group`` and ``iam_role`` modules. The ``iam`` module will be removed in release 3.0.0 (https://github.com/ansible-collections/community.aws/pull/664).
- iam_cert - the iam_cert module has been renamed to iam_server_certificate for consistency with the companion iam_server_certificate_info module. The usage of the module has not changed.  The iam_cert alias will be removed in version 4.0.0 (https://github.com/ansible-collections/community.aws/pull/728).
- iam_server_certificate - Passing file names to the ``cert``, ``chain_cert`` and ``key`` parameters has been deprecated. We recommend using a lookup plugin to read the files instead, see the documentation for an example (https://github.com/ansible-collections/community.aws/pull/735).
- iam_server_certificate - the default value for the ``dup_ok`` parameter is currently ``false``, in version 4.0.0 this will be updated to ``true``.  To preserve the current behaviour explicitly set the ``dup_ok`` parameter to ``false`` (https://github.com/ansible-collections/community.aws/pull/737).
- rds - the boto based ``rds`` module has been deprecated in favour of the boto3 based ``rds_instance`` module. The ``rds`` module will be removed in release 3.0.0 (https://github.com/ansible-collections/community.aws/pull/663).
- rds_snapshot - the rds_snapshot module has been renamed to rds_instance_snapshot. The usage of the module has not changed. The rds_snapshot alias will be removed in version 4.0.0 (https://github.com/ansible-collections/community.aws/pull/783).
- script_inventory_ec2 - The ec2.py inventory script is being moved to a new repository. The script can now be downloaded from https://github.com/ansible-community/contrib-scripts/blob/main/inventory/ec2.py and will be removed from this collection in the 3.0 release. We recommend migrating from the script to the `amazon.aws.ec2` inventory plugin.

community.azure
~~~~~~~~~~~~~~~

- All community.azure.azure_rm_<resource>_facts modules are deprecated. Use azure.azcollection.azure_rm_<resource>_info modules instead (https://github.com/ansible-collections/community.azure/pull/24).
- All community.azure.azure_rm_<resource>_info modules are deprecated. Use azure.azcollection.azure_rm_<resource>_info modules instead (https://github.com/ansible-collections/community.azure/pull/24).
- community.azure.azure_rm_managed_disk and community.azure.azure_rm_manageddisk are deprecated. Use azure.azcollection.azure_rm_manageddisk instead (https://github.com/ansible-collections/community.azure/pull/24).
- community.azure.azure_rm_virtualmachine_extension and community.azure.azure_rm_virtualmachineextension are deprecated. Use azure.azcollection.azure_rm_virtualmachineextension instead (https://github.com/ansible-collections/community.azure/pull/24).
- community.azure.azure_rm_virtualmachine_scaleset and community.azure.azure_rm_virtualmachinescaleset are deprecated. Use azure.azcollection.azure_rm_virtualmachinescaleset instead (https://github.com/ansible-collections/community.azure/pull/24).

community.crypto
~~~~~~~~~~~~~~~~

- acme_* modules - ACME version 1 is now deprecated and support for it will be removed in community.crypto 2.0.0 (https://github.com/ansible-collections/community.crypto/pull/288).

community.docker
~~~~~~~~~~~~~~~~

- docker_* modules and plugins, except ``docker_swarm`` connection plugin and ``docker_compose`` and ``docker_stack*` modules - the current default ``localhost`` for ``tls_hostname`` is deprecated. In community.docker 2.0.0 it will be computed from ``docker_host`` instead (https://github.com/ansible-collections/community.docker/pull/134).
- docker_container - the new ``command_handling``'s default value, ``compatibility``, is deprecated and will change to ``correct`` in community.docker 3.0.0. A deprecation warning is emitted by the module in cases where the behavior will change. Please note that ansible-core will output a deprecation warning only once, so if it is shown for an earlier task, there could be more tasks with this warning where it is not shown (https://github.com/ansible-collections/community.docker/pull/186).
- docker_container - using the special value ``all`` in ``published_ports`` has been deprecated. Use ``publish_all_ports=true`` instead (https://github.com/ansible-collections/community.docker/pull/210).

community.general
~~~~~~~~~~~~~~~~~

- Support for Ansible 2.9 and ansible-base 2.10 is deprecated, and will be removed in the next major release (community.general 5.0.0) next spring. While most content will probably still work with ansible-base 2.10, we will remove symbolic links for modules and action plugins, which will make it impossible to use them with Ansible 2.9 anymore. Please use community.general 4.x.y with Ansible 2.9 and ansible-base 2.10, as these releases will continue to support Ansible 2.9 and ansible-base 2.10 even after they are End of Life (https://github.com/ansible-community/community-topics/issues/50, https://github.com/ansible-collections/community.general/pull/3723).
- ali_instance_info - marked removal version of deprecated parameters ``availability_zone`` and ``instance_names`` (https://github.com/ansible-collections/community.general/issues/2429).
- bitbucket_* modules - ``username`` options have been deprecated in favor of ``workspace`` and will be removed in community.general 6.0.0 (https://github.com/ansible-collections/community.general/pull/2045).
- dnsimple - python-dnsimple < 2.0.0 is deprecated and support for it will be removed in community.general 5.0.0 (https://github.com/ansible-collections/community.general/pull/2946#discussion_r667624693).
- gitlab_group_members - setting ``gitlab_group`` to ``name`` or ``path`` is deprecated. Use ``full_path`` instead (https://github.com/ansible-collections/community.general/pull/3451).
- keycloak_authentication - the return value ``flow`` is now deprecated and will be removed in community.general 6.0.0; use ``end_state`` instead (https://github.com/ansible-collections/community.general/pull/3280).
- keycloak_group - the return value ``group`` is now deprecated and will be removed in community.general 6.0.0; use ``end_state`` instead (https://github.com/ansible-collections/community.general/pull/3280).
- linode - parameter ``backupsenabled`` is deprecated and will be removed in community.general 5.0.0 (https://github.com/ansible-collections/community.general/pull/2410).
- lxd_container - the current default value ``true`` of ``ignore_volatile_options`` is deprecated and will change to ``false`` in community.general 6.0.0 (https://github.com/ansible-collections/community.general/pull/3429).
- serverless - deprecating parameter ``functions`` because it was not used in the code (https://github.com/ansible-collections/community.general/pull/2845).
- xfconf - deprecate the ``get`` state. The new module ``xfconf_info`` should be used instead (https://github.com/ansible-collections/community.general/pull/3049).

community.grafana
~~~~~~~~~~~~~~~~~

- grafana_dashboard lookup - Providing a mangled version of the API key is no longer preferred.

community.hashi_vault
~~~~~~~~~~~~~~~~~~~~~

- hashi_vault collection - support for Python 2 will be dropped in version ``2.0.0`` of ``community.hashi_vault`` (https://github.com/ansible-collections/community.hashi_vault/issues/81).
- hashi_vault collection - support for Python 3.5 will be dropped in version ``2.0.0`` of ``community.hashi_vault`` (https://github.com/ansible-collections/community.hashi_vault/issues/81).
- lookup hashi_vault - the ``[lookup_hashi_vault]`` section in the ``ansible.cfg`` file is deprecated and will be removed in collection version ``3.0.0``. Instead, the section ``[hashi_vault_collection]`` can be used, which will apply to all plugins in the collection going forward (https://github.com/ansible-collections/community.hashi_vault/pull/144).

community.kubernetes
~~~~~~~~~~~~~~~~~~~~

- The ``community.kubernetes`` collection is being renamed to ``kubernetes.core``. All content in the collection has been replaced by deprecated redirects to ``kubernetes.core``. If you are using FQCNs starting with ``community.kubernetes``, please update them to ``kubernetes.core`` (https://github.com/ansible-collections/community.kubernetes/pull/439).

community.vmware
~~~~~~~~~~~~~~~~

- vmware_guest_vnc -  Sphere 7.0 removed the built-in VNC server (https://docs.vmware.com/en/VMware-vSphere/7.0/rn/vsphere-esxi-vcenter-server-70-release-notes.html#productsupport).

inspur.sm
~~~~~~~~~

- add_ad_group - This feature will be removed in inspur.sm.add_ad_group 3.0.0. replaced with inspur.sm.ad_group.
- add_ldap_group - This feature will be removed in inspur.sm.add_ldap_group 3.0.0. replaced with inspur.sm.ldap_group.
- add_user - This feature will be removed in inspur.sm.add_user 3.0.0. replaced with inspur.sm.user.
- add_user_group - This feature will be removed in inspur.sm.add_user_group 3.0.0. replaced with inspur.sm.user_group.
- del_ad_group - This feature will be removed in inspur.sm.del_ad_group 3.0.0. replaced with inspur.sm.ad_group.
- del_ldap_group - This feature will be removed in inspur.sm.del_ldap_group 3.0.0. replaced with inspur.sm.ldap_group.
- del_user - This feature will be removed in inspur.sm.del_user 3.0.0. replaced with inspur.sm.user.
- del_user_group - This feature will be removed in inspur.sm.del_user_group 3.0.0. replaced with inspur.sm.user_group.
- edit_ad_group - This feature will be removed in inspur.sm.edit_ad_group 3.0.0. replaced with inspur.sm.ad_group.
- edit_ldap_group - This feature will be removed in inspur.sm.edit_ldap_group 3.0.0. replaced with inspur.sm.ldap_group.
- edit_user - This feature will be removed in inspur.sm.edit_user 3.0.0. replaced with inspur.sm.user.
- edit_user_group - This feature will be removed in inspur.sm.edit_user_group 3.0.0. replaced with inspur.sm.user_group.

junipernetworks.junos
~~~~~~~~~~~~~~~~~~~~~

- Deprecated router_id from ospfv2 resource module.
- Deprecated router_id from ospfv3 resource module.
- The junos_logging module has been deprecated in favor of the new junos_logging_global resource module and will be removed in a release after '2023-08-01'.

vyos.vyos
~~~~~~~~~

- The vyos_logging module has been deprecated in favor of the new vyos_logging_global resource module and will be removed in a release after "2023-08-01".

Removed Features (previously deprecated)
----------------------------------------

Ansible-core
~~~~~~~~~~~~

- The built-in module_util ``ansible.module_utils.common.removed`` was previously deprecated and has been removed.
- connections, removed password check stubs that had been moved to become plugins.
- task, inline parameters being auto coerced into variables has been removed.

ansible.windows
~~~~~~~~~~~~~~~

- win_reboot - Removed ``shutdown_timeout`` and ``shutdown_timeout_sec`` which has not done anything since Ansible 2.5.

community.crypto
~~~~~~~~~~~~~~~~

- acme_* modules - the ``acme_directory`` option is now required (https://github.com/ansible-collections/community.crypto/pull/290).
- acme_* modules - the ``acme_version`` option is now required (https://github.com/ansible-collections/community.crypto/pull/290).
- acme_account_facts - the deprecated redirect has been removed. Use community.crypto.acme_account_info instead (https://github.com/ansible-collections/community.crypto/pull/290).
- acme_account_info - ``retrieve_orders=url_list`` no longer returns the return value ``orders``. Use the ``order_uris`` return value instead (https://github.com/ansible-collections/community.crypto/pull/290).
- crypto.info module utils - the deprecated redirect has been removed. Use ``crypto.pem`` instead (https://github.com/ansible-collections/community.crypto/pull/290).
- get_certificate - removed the ``pyopenssl`` backend (https://github.com/ansible-collections/community.crypto/pull/273).
- openssl_certificate - the deprecated redirect has been removed. Use community.crypto.x509_certificate instead (https://github.com/ansible-collections/community.crypto/pull/290).
- openssl_certificate_info - the deprecated redirect has been removed. Use community.crypto.x509_certificate_info instead (https://github.com/ansible-collections/community.crypto/pull/290).
- openssl_csr - removed the ``pyopenssl`` backend (https://github.com/ansible-collections/community.crypto/pull/273).
- openssl_csr and openssl_csr_pipe - ``version`` now only accepts the (default) value 1 (https://github.com/ansible-collections/community.crypto/pull/290).
- openssl_csr_info - removed the ``pyopenssl`` backend (https://github.com/ansible-collections/community.crypto/pull/273).
- openssl_csr_pipe - removed the ``pyopenssl`` backend (https://github.com/ansible-collections/community.crypto/pull/273).
- openssl_privatekey - removed the ``pyopenssl`` backend (https://github.com/ansible-collections/community.crypto/pull/273).
- openssl_privatekey_info - removed the ``pyopenssl`` backend (https://github.com/ansible-collections/community.crypto/pull/273).
- openssl_privatekey_pipe - removed the ``pyopenssl`` backend (https://github.com/ansible-collections/community.crypto/pull/273).
- openssl_publickey - removed the ``pyopenssl`` backend (https://github.com/ansible-collections/community.crypto/pull/273).
- openssl_publickey_info - removed the ``pyopenssl`` backend (https://github.com/ansible-collections/community.crypto/pull/273).
- openssl_signature - removed the ``pyopenssl`` backend (https://github.com/ansible-collections/community.crypto/pull/273).
- openssl_signature_info - removed the ``pyopenssl`` backend (https://github.com/ansible-collections/community.crypto/pull/273).
- x509_certificate - remove ``assertonly`` provider (https://github.com/ansible-collections/community.crypto/pull/289).
- x509_certificate - removed the ``pyopenssl`` backend (https://github.com/ansible-collections/community.crypto/pull/273).
- x509_certificate_info - removed the ``pyopenssl`` backend (https://github.com/ansible-collections/community.crypto/pull/273).
- x509_certificate_pipe - removed the ``pyopenssl`` backend (https://github.com/ansible-collections/community.crypto/pull/273).

community.docker
~~~~~~~~~~~~~~~~

- docker_container - the default value of ``container_default_behavior`` changed to ``no_defaults`` (https://github.com/ansible-collections/community.docker/pull/210).
- docker_container - the default value of ``network_mode`` is now the name of the first network specified in ``networks`` if such are specified and ``networks_cli_compatible=true`` (https://github.com/ansible-collections/community.docker/pull/210).
- docker_container - the special value ``all`` can no longer be used in ``published_ports`` next to other values. Please use ``publish_all_ports=true`` instead (https://github.com/ansible-collections/community.docker/pull/210).
- docker_login - removed the ``email`` option (https://github.com/ansible-collections/community.docker/pull/210).

community.general
~~~~~~~~~~~~~~~~~

- All inventory and vault scripts contained in community.general were moved to the `contrib-scripts GitHub repository <https://github.com/ansible-community/contrib-scripts>`_ (https://github.com/ansible-collections/community.general/pull/2696).
- ModuleHelper module utils - remove fallback when value could not be determined for a parameter (https://github.com/ansible-collections/community.general/pull/3461).
- Removed deprecated netapp module utils and doc fragments (https://github.com/ansible-collections/community.general/pull/3197).
- The nios, nios_next_ip, nios_next_network lookup plugins, the nios documentation fragment, and the nios_host_record, nios_ptr_record, nios_mx_record, nios_fixed_address, nios_zone, nios_member, nios_a_record, nios_aaaa_record, nios_network, nios_dns_view, nios_txt_record, nios_naptr_record, nios_srv_record, nios_cname_record, nios_nsgroup, and nios_network_view module have been removed from community.general 4.0.0 and were replaced by redirects to the `infoblox.nios_modules <https://galaxy.ansible.com/infoblox/nios_modules>`_ collection. Please install the ``infoblox.nios_modules`` collection to continue using these plugins and modules, and update your FQCNs (https://github.com/ansible-collections/community.general/pull/3592).
- The vendored copy of ``ipaddress`` has been removed. Please use ``ipaddress`` from the Python 3 standard library, or `from pypi <https://pypi.org/project/ipaddress/>`_. (https://github.com/ansible-collections/community.general/pull/2441).
- cpanm - removed the deprecated ``system_lib`` option. Use Ansible's privilege escalation mechanism instead; the option basically used ``sudo`` (https://github.com/ansible-collections/community.general/pull/3461).
- grove - removed the deprecated alias ``message`` of the ``message_content`` option (https://github.com/ansible-collections/community.general/pull/3461).
- proxmox - default value of ``proxmox_default_behavior`` changed to ``no_defaults`` (https://github.com/ansible-collections/community.general/pull/3461).
- proxmox_kvm - default value of ``proxmox_default_behavior`` changed to ``no_defaults`` (https://github.com/ansible-collections/community.general/pull/3461).
- runit - removed the deprecated ``dist`` option which was not used by the module (https://github.com/ansible-collections/community.general/pull/3461).
- telegram - removed the deprecated ``msg``, ``msg_format`` and ``chat_id`` options (https://github.com/ansible-collections/community.general/pull/3461).
- xfconf - the default value of ``disable_facts`` changed to ``true``, and the value ``false`` is no longer allowed. Register the module results instead (https://github.com/ansible-collections/community.general/pull/3461).

community.hashi_vault
~~~~~~~~~~~~~~~~~~~~~

- drop support for Python 2 and Python 3.5 (https://github.com/ansible-collections/community.hashi_vault/issues/81).
- support for the following deprecated environment variables has been removed: ``VAULT_AUTH_METHOD``, ``VAULT_TOKEN_PATH``, ``VAULT_TOKEN_FILE``, ``VAULT_ROLE_ID``, ``VAULT_SECRET_ID`` (https://github.com/ansible-collections/community.hashi_vault/pull/173).

Security Fixes
--------------

Ansible-core
~~~~~~~~~~~~

- Do not include params in exception when a call to ``set_options`` fails. Additionally, block the exception that is returned from being displayed to stdout. (CVE-2021-3620)
- templating engine fix for not preserving usnafe status when trying to preserve newlines. CVE-2021-3583

cisco.ios
~~~~~~~~~

- To fix Cisco IOS no log issue and add ignore txt for 2.12 (https://github.com/ansible-collections/cisco.ios/pull/304).

community.general
~~~~~~~~~~~~~~~~~

- nmcli - do not pass WiFi secrets on the ``nmcli`` command line. Use ``nmcli con edit`` instead and pass secrets as ``stdin`` (https://github.com/ansible-collections/community.general/issues/3145).

community.mongodb
~~~~~~~~~~~~~~~~~

- 312 - Set no_log True for ssl_keyfile.

community.windows
~~~~~~~~~~~~~~~~~

- win_psexec - Ensure password is masked in ``psexec_command`` return result - https://github.com/ansible-collections/community.windows/issues/43

Bugfixes
--------

Ansible-core
~~~~~~~~~~~~

- Add RockyLinux to fact gathering (https://github.com/ansible/ansible/pull/74530).
- Add unicode support to ``ansible-inventory`` CLI (https://github.com/ansible/ansible/issues/57378)
- Add yaml representer for VarsWithSources (https://github.com/ansible/ansible/pull/68525).
- Added page describing terminal plugins to docsite
- AnsibleModule.set_mode_if_different - don't check file existence when check_mode is activated (https://github.com/ansible/ansible/issues/61185).
- Apply ``display_failed_stderr`` callback option on loop item results. (https://github.com/ansible/ansible/issues/74864)
- Binary GnuPG keys downloaded via URLs by the 'ansible.builtin.apt_key' module were corrupted so 'gpg' could not import them (https://github.com/ansible/ansible/issues/74424).
- Ensure end_play ends play, not batch (https://github.com/ansible/ansible/issues/73971)
- Ensure we get full path for extra vars into cliargs to avoid realpath issues after initial load.
- Fix ``keys()`` implementation of ``BaseFileCacheModule`` to strip the prefix from the key and only return keys that share the same prefix as the cache.
- Fix ``when`` evaluation on Native Jinja and Python 3.10.
- Fix templating task action with host-specific vars (https://github.com/ansible/ansible/issues/75568)
- Fully qualified 'ansible.legacy' and 'ansible.builtin' plugin names work in conjunction with module_defaults.
- Give a warning instead of an error if a handler name contains undefined variables and has no listen topics (https://github.com/ansible/ansible/issues/58841).
- Improve resilience of ``ansible-galaxy collection`` by increasing the page size to make fewer requests overall and retrying queries with a jittered exponential backoff when rate limiting HTTP codes (520 and 429) occur. (https://github.com/ansible/ansible/issues/74191)
- Jinja2 globals should be accessible even when importing a template without the context (https://github.com/ansible/ansible/issues/75371)
- PlayContext - Remove deprecated ``make_become_cmd`` (https://github.com/ansible/ansible/issues/74136)
- PowerShell - Ignore the ``LIB`` environment variable when compiling C# Ansible code
- Prevent ``ansible_failed_task`` from further templating (https://github.com/ansible/ansible/issues/74036)
- Remove 'default' from ssh plugin as we want to rely on default from ssh itself or ssh/config.
- Replace usage of private dnf.Base() attribute by future dnf API
- Save unreachable hosts between plays by adding them to the PlayIterator's _play._removed_hosts (https://github.com/ansible/ansible/issues/66945).
- Solaris - correct version check in svcadm_supports_sync (https://github.com/ansible/ansible/pull/73860).
- Task depth - Prevent exception when the task depth exceeds Pythons recursion depth (https://github.com/ansible/ansible/issues/73996)
- Templating - Ensure we catch exceptions when calling ``.filters()`` or ``.tests()`` on their respective plugins and properly error, instead of aborting which results in no filters being added to the jinja2 environment (https://github.com/ansible/ansible/pull/74127)
- The ``apt_key`` module did not properly handle GnuPG errors (https://github.com/ansible/ansible/issues/74477)
- The error message about the failure to import a ```gpg`` key by the ``apt_key`` module was incorrect (https://github.com/ansible/ansible/issues/74423).
- Update network user guide to explain use of cli_parse and validate plugins.
- Variable Manager - Only check if ``play.hosts`` is a template when the play hasn't been finalized (https://github.com/ansible/ansible/issues/73926)
- WorkerProcess - Python 3.5 fix for workaround for stdout deadlock in multiprocessing shutdown to avoid process hangs. (https://github.com/ansible/ansible/issues/74149)
- ``AnsibleModule.run_command`` - Address thread safety issues, concerning mutating the environment, current working directory, and umask. (https://github.com/ansible/ansible/issues/74783)
- ``failed_when``/``changed_when`` - Catch templating errors to prevent masking of module output (https://github.com/ansible/ansible/issues/37187)
- ``heuristic_log_sanitize`` - Return the full string if there is no password (https://github.com/ansible/ansible/issues/75542)
- ``pip`` now uses the ``pip`` Python module installed for the Ansible module's Python interpreter, if available, unless ``executable`` or ``virtualenv`` were specified.
- advanced_host_list inventory plugin - Fixed variable referenced before assignment when hostname/range could not be parsed.
- ansiballz - avoid treating path to site_packages as regex; escape it. This prevents a crash when ansible is installed to, or running from, an oddly named directory like ``ansi[ble``
- ansible-doc - in text output, do not show empty ``version_added_collection`` values (https://github.com/ansible/ansible/pull/74999).
- ansible-doc can now dump kewyords with --metadata-dump (still just for internal use)
- ansible-doc, fix output for internal metadata dump option
- ansible-doc, make inventory plugin selection for snippets generic and not a hardcoded list
- ansible-galaxy - Fix a bug with build_ignore when installing collections from source (https://github.com/ansible/ansible/issues/75528).
- ansible-galaxy - Fix handling HTTP exceptions from Galaxy servers. Continue to the next server in the list until the collection is found.
- ansible-galaxy - Improve error message from dependency resolution when a candidate has inconsistent requirements (https://github.com/ansible/ansible/issues/75139).
- ansible-inventory - handle an exception while parsing inventory in toml format (https://github.com/ansible/ansible/issues/74404).
- ansible-playbook, more robust handling of --list-hosts and undefined vars in hosts keyword.
- ansible-pull - update documentation for ``--directory`` option to clarify path must be absolute.
- ansible-pull, restore other options to use as repo other than git.
- ansible-test - Add constraint for ``pyspnego>=0.1.6`` for Python 3.10 - https://github.com/ansible/ansible/pull/74612
- ansible-test - Avoid publishing the port used by the ``pypi-test-container`` since it is only accessed by other containers. This avoids issues when trying to run tests in parallel on a single host.
- ansible-test - Failure to download test results from a remote host no longer hide test failures. If a download failure occurs after tests fail, a warning will be issued instead.
- ansible-test - Fix docker container IP address detection. The ``bridge`` network is no longer assumed to be the default.
- ansible-test - Fix path to inventory file for ``windows-integration`` and ``network-integration`` commands for collections.
- ansible-test - Fix traceback when generating coverage reports and no coverage directory exists.
- ansible-test - Random port selection is no longer handled by ``ansible-test``, avoiding possible port conflicts. Previously ``ansible-test`` would, under some circumstances, use one host's available ports to determine those of another host.
- ansible-test - Running tests in a single test run with multiple "cloud" plugins no longer results in port conflicts. Previously two or more containers with overlapping ports could not be used in the same test run.
- ansible-test - Tab completion after options like ``--docker`` which accept an optional argument will no longer provide incorrect completions.
- ansible-test - The ``--python`` and ``--venv`` options are no longer ignored by some commands, such as ``coverage``.
- ansible-test - The ``docker inspect`` command is now used to check for existing images instead of the ``docker images`` command. This resolves an issue where a ``docker pull`` would be unnecessarily executed for an image referenced by checksum.
- ansible-test - Update distribution test containers to version 3.1.0.
- ansible-test - Use ``--strict`` for ``pytest`` on Python 2.6 since ``--strict-markers`` is not available.
- ansible-test - Use documented API to retrieve build information from Azure Pipelines.
- ansible-test - Use pwsh to generate correct coverage line counts for stub files to get a more accurate coverage result
- ansible-test - Use the correct variable to reference the client's SSH key when generating inventory.
- ansible-test - add packaging python module to ``ansible-doc`` sanity test requirements.
- ansible-test - allow the same listening port on all container interfaces
- ansible-test - ensure the correct unit test target is given when the ``__init__.py`` file is modified inside the connection plugins directory
- ansible-test - make the ``a/`` and ``b/`` prefixes an optional match since these can be turned off with the ``diff.noprefix`` setting in ``git``
- ansible-test - restrict ``packaging`` to ``< 21.0`` for Python ``< 3.6`` (https://github.com/ansible/ansible/pull/75186).
- ansible-test pslint - Fix error when encountering validation results that are highly nested - https://github.com/ansible/ansible/issues/74151
- ansible-test validate-modules - EXAMPLES will no longer be marked as invalid YAML when it uses Ansible-specific YAML tags (https://github.com/ansible/ansible/pull/74384).
- ansible-test validate-modules - correctly validate positional parameters to ``AnsibleModules`` (https://github.com/ansible/ansible/pull/75332).
- ansible.builtin.cron - Keep non-empty crontabs, when removing cron jobs (https://github.com/ansible/ansible/pull/74497).
- ansible.utils.encrypt now handles missing or unusable 'crypt' library.
- ansible_test - add constraint for ``MarkupSafe`` (https://github.com/ansible/ansible/pull/74666)
- apt_key - set --recv argument as last one in apt-key command when using env var HTTP_PROXY (https://github.com/ansible/ansible/issues/74946)
- arg_spec - remove unused imports
- async_status, ensure we always get documented returns
- async_status, resurrected module to deprecate for those that were invoking it directly.
- basic - skip over module parameters which are used in ``journal.send`` API call (https://github.com/ansible/ansible/issues/71343).
- become - fix a regression on Solaris where chmod can return 5 which we interpret as auth failure and stop trying become tmpdir permission fallbacks
- become - work around setfacl not existing on modern Solaris (and possibly failing on some filesystems even when it does exist)
- callbacks, restore displaying delegation to host as host label.
- cli defaults for ssh args set to None as '' was bypassing normal default.
- command - remove unreachable code path when trying to convert the value for ``chdir`` to bytes (https://github.com/ansible/ansible/pull/75036)
- command module, clarify order of remove/creates checks.
- command module, correctly handles chdir to symlinks.
- command module, move to standarized messages in 'msg' vs abusing 'stdout'.
- command module, now all options work in ad-hoc execution.
- command module, now always returns what we documented as 'returns always'.
- config - use ``callbacks_enabled`` instead ``callback_enabled`` in a deprecated message (https://github.com/ansible/ansible/issues/70028).
- config lookup, can also handle collection plugins now
- config, ensure 'quoted' lists from ini or env do not take the quotes literally as part of the list item.
- connection ssh, no ssh_args cli option, so removed doc entry.
- constants, internal _deprecated function always requires version.
- correct doc links for become on warnings over world readable settings.
- correctly use world readable setting since old constant is not 'settable' anymore.
- dnf - align the return value of the list argument with the ``yum`` module (https://github.com/ansible/ansible/issues/75483)
- dnf - properly capture transaction error (https://github.com/ansible/ansible/issues/72651)
- dnf - refactor code to use `dnf whatprovides` API (https://github.com/ansible/ansible/issues/73503).
- dnf - support non-english environments (https://github.com/ansible/ansible/issues/75021)
- dnf module - Use all components of a package name to determine if it's installed (https://github.com/ansible/ansible/issues/75311).
- do not trigger interpreter discovery in the forced_local module path as they should use the ansible playbook python unless otherwise configured.
- facts - detect homebrew installed at /opt/homebrew/bin/brew
- facts, service_mgr, handle issues if ps command fails or returns empty.
- filter plugins - patch new versions of Jinja2 to prevent warnings/errors on renamed filter decorators (https://github.com/ansible/ansible/issues/74667)
- find - fix a bug where ``size`` argument was ignored for regular files with ``file_type`` of ``any``.
- find action, correctly convert path to text when warning about skiping.
- find does not ignore errors from os.walk anymore and issues warnings as expected.
- gather_facts, improved message on timeout.
- gather_facts, package, service - fix using module_defaults for the modules in addition to the action plugins. (https://github.com/ansible/ansible/issues/72918)
- get_bin_path, clarify with quotes what the missing required executable is.
- get_url - Fixed checksum validation for binary files (leading asterisk) in checksum files (https://github.com/ansible/ansible/pull/74502).
- getent, fix return data for when there are multiple results for the same key
- git - Fix git path used when .git file is present (https://github.com/ansible/ansible/issues/75608).
- host_group_vars vars plugin fixed ini entry, section and key were reversed.
- hostname - Add Rocky Linux support
- hostname - No longer modifies system files in get_* methods and therefore when consulted in check_mode (https://github.com/ansible/ansible/issues/66432)
- include - Remove deprecated ``static`` argument for ``include`` (https://github.com/ansible/ansible/issues/74135)
- includes - Remove the deprecated ability to specify ``tags`` as ``vars`` on includes (https://github.com/ansible/ansible/issues/74144)
- ini lookup - better error on mixed/bad parameters
- ini lookup - handle errors for duplicate keys and missing sections (https://github.com/ansible/ansible/issues/74601)
- interpreter discovery - Debian 8 and lower will avoid unsupported Python3 version in interpreter discovery
- interpreter discovery is now handling special (ansible_network_os) cases in less noisy ways.
- interpreter_discovery - hide warning 'No python interpreters...' when ANSIBLE_PYTHON_INTERPRETER=auto_silent (https://github.com/ansible/ansible/issues/74274).
- module_common - handle exception when multiple workers try to create the cache directory
- module_defaults - Fix action defaults for legacy actions/modules (https://github.com/ansible/ansible/issues/75279).
- module_utils - detect symlinked init systems, even if unable to read /proc/1/comm (https://github.com/ansible/ansible/issues/74866).
- netconf - catch and handle exception to prevent stack trace when running in FIPS mode
- network module_utils - fix bug where ``to_bits()`` returned the ``str`` type instead of a useful value.
- paramiko_ssh - mark connection as connected when ``_connect()`` is called (https://github.com/ansible/ansible/issues/74081)
- password - Handle passlib wrapped algos bsd_nthash, django_argon2, django_bcrypt, ldap_bcrypt, ldap_bsdi_crypt, ldap_des_crypt, ldap_hex_md5, ldap_hex_sha1, ldap_md5_crypt, ldap_pbkdf2_sha1, ldap_pbkdf2_sha256, ldap_pbkdf2_sha512, ldap_sha1_crypt, ldap_sha256_crypt, ldap_sha512_crypt, roundup_plaintext (https://github.com/ansible/ansible/pull/75527).
- pause - ensure control characters are always set to an appropriate value (https://github.com/ansible/ansible/issues/73264)
- pkg_mgr.py - Lower the priority of rpm-ostree detection to avoid false positives on systems not using it as the main package manager (https://github.com/ansible/ansible/issues/74578)
- play - validate the ``hosts`` entry in a play (https://github.com/ansible/ansible/issues/65386)
- playbook loaded from collection subdir now does not ignore subdirs.
- plugin config now allows list type options to have multiple valid choices (#74225).
- psrp - Always cleanup the last run pipeline if a second pipeline is invoked to avoid violating any resource limits.
- psrp - Fix error when resetting a connection that was initialised but not connected - (https://github.com/ansible/ansible/issues/74092).
- psrp - Try to clean up any server-side resources when resetting a connection.
- recursive_diff - handle condition when parameters are not dict (https://github.com/ansible/ansible/issues/56249).
- register - Ensure that ``register`` used on ``set_fact`` or ``include_vars`` does not automatically wrap the facts as unsafe. (https://github.com/ansible/ansible/issues/21088)
- rekey_on_member - handle undefined positional arguments better.
- remote tmpdir permissions - fix type error in macOS chmod ACL fallback (https://github.com/ansible/ansible/pull/74613).
- replace - better handling of file operation exceptions (https://github.com/ansible/ansible/pull/74686).
- roles - allow for role arg specs in new meta file (https://github.com/ansible/ansible/issues/74525).
- roles - fix unexpected ``AttributeError`` when an empty ``argument_specs.yml`` is present (https://github.com/ansible/ansible/pull/75604).
- roles - make sure argspec validation task is tagged with ``always`` (https://github.com/ansible/ansible/pull/74994).
- roles - make sure argspec validation task templates suboptions (https://github.com/ansible/ansible/issues/75070).
- schema validation now uses dynamic range of versions for valid deprecation entries vs hardcoded out of date list.
- script inventory plugin - Remove deprecated caching support (https://github.com/ansible/ansible/issues/74143)
- sequence - fix error message so that unrecognized options to the plugin display correctly as a list and normalize error messages.
- service - compare version without LooseVersion API (https://github.com/ansible/ansible/issues/74488).
- set ssh host_key_checking defaults to True, restoring original behaviour (https://github.com/ansible/ansible/issues/75168)
- setup module should now not truncate hpux interface names.
- setup module, fix filter to adjust for missing ``ansible_`` prefix on query.
- setup, while gathering linux hardware facts be more resilient to errors and try to return more info.
- slurp - Fix error messages for unreadable files and directories(https://github.com/ansible/ansible/issues/67340).
- slurp - handle error when ``path`` is a directory and not a file (https://github.com/ansible/ansible/pull/74930).
- slurp - improve the logic in the error handling and remove ``os.stat()`` call (https://github.com/ansible/ansible/pull/75038)
- ssh connection now correctly handle ssh_transfer_method and scp_if_ssh interactions.
- ssh connection, fix interaction between trasnfer settings options.
- ssh connection, use self.host which has the most up2date info instead of pc.remote_addr
- ssh_connection - rename ``retries`` to ``reconnection_retries`` to avoid conflicts with task vars (https://github.com/ansible/ansible/issues/75142).
- ssh_connection - set the default for ``reconnection_retries`` back to ``0`` (https://github.com/ansible/ansible/issues/75142).
- subversion - fix stack trace when getting information about the repository (https://github.com/ansible/ansible/issues/36498)
- system_service - use a context manager for file handling.
- task_executor, Actions using AnsibleActionFail/Skip will now propagate 'results' if given
- task_executor/ssh_connection - use the ``retries`` value from ``ssh_connection`` settings, not the default from the ``Task`` field attributes (https://github.com/ansible/ansible/issues/75142).
- template - ensure Jinja2 overrides from template header are used (https://github.com/ansible/ansible/issues/75275)
- unarchive - allow extracting archives that contain files which size exceeds free system memory (https://github.com/ansible/ansible/issues/73985).
- unarchive - fail when zipinfo binary is not found in executable paths (https://github.com/ansible/ansible/issues/39029).
- unarchive - move failure for missing binary to ``can_handle_archive()`` rather than ``__init__()``
- uri - Fix traceback and provide error message when trying to use non-string or mapping for ``form-multipart`` body - https://github.com/ansible/ansible/issues/74276
- urls - Fix logic in matching ``unredirected_headers`` to perform case insensitive matching
- validate_argument_spec, correct variable precedence and merge method and add missing examples
- variable manager, avoid sourcing delegated variables when no inventory hostname is present. This affects scenarios like syntax check and imports.
- version test - improve error message when an empty version is provided
- yum - Fixed typo in failure message (https://github.com/ansible/ansible/pull/72964).
- yum - When upgrading, every architecture of a package is now included in the module results, instead of just one (https://github.com/ansible/ansible/issues/73284).
- yum - fix ``yumstate`` return value when wildcards are used in the ``list`` argument (https://github.com/ansible/ansible/issues/74557)
- yum - fix parsing of multiple subsequent empty lines from ``yum check-update`` output (https://github.com/ansible/ansible/issues/70949)
- yum - yum action plugin changes to support 'use' as an alias of 'use_backend' (https://github.com/ansible/ansible/issues/70774).

amazon.aws
~~~~~~~~~~

- AWS action group - added missing ``ec2_instance_facts`` entry (https://github.com/ansible-collections/amazon.aws/issues/557)
- aws_s3 - Fix upload permission when an S3 bucket ACL policy requires a particular canned ACL (https://github.com/ansible-collections/amazon.aws/pull/318)
- ec2_ami - Fix ami issue when creating an ami with no_device parameter (https://github.com/ansible-collections/amazon.aws/pull/386)
- ec2_ami - fix problem when creating an AMI from an instance with ephemeral volumes (https://github.com/ansible-collections/amazon.aws/issues/511).
- ec2_instance - ``ec2_instance`` was waiting on EC2 instance monitoring status to be ``OK`` when launching a new instance. This could cause a play to wait multiple minutes for AWS's monitoring to complete status checks (https://github.com/ansible-collections/amazon.aws/pull/481).
- ec2_instance - ensure that ec2_instance falls back to the tag(Name) parameter when no filter and no name parameter is passed (https://github.com/ansible-collections/amazon.aws/issues/526).
- ec2_snapshot - Fix snapshot issue when capturing a snapshot of a volume without tags (https://github.com/ansible-collections/amazon.aws/pull/383)
- ec2_vol - Fixes ``changed`` status when ``modify_volume`` is used, but no new  disk is being attached.  The module incorrectly reported that no change had  occurred even when disks had been modified (iops, throughput, type, etc.). (https://github.com/ansible-collections/amazon.aws/issues/482).
- ec2_vol - fix iops setting and enforce iops/throughput parameters usage (https://github.com/ansible-collections/amazon.aws/pull/334)
- inventory - ``include_filters`` won't be ignored anymore if ``filters`` is not set (https://github.com/ansible-collections/amazon.aws/issues/457).
- s3_bucket - Fix error handling when attempting to set a feature that is not implemented (https://github.com/ansible-collections/amazon.aws/pull/391).
- s3_bucket - Gracefully handle ``NotImplemented`` exceptions when fetching encryption settings (https://github.com/ansible-collections/amazon.aws/issues/390).
- s3_bucket - update error handling to better support DigitalOcean Space (https://github.com/ansible-collections/amazon.aws/issues/508).

ansible.netcommon
~~~~~~~~~~~~~~~~~

- Variables in play_context will now be updated for netconf connections on each task run.
- fix SCP/SFTP when using network_cli with libssh
- libssh - Fix fromatting of authenticity error message when not prompting for input (https://github.com/ansible-collections/ansible.netcommon/issues/283)
- netconf - Fix connection with ncclient versions < 0.6.10
- network_cli - Add ability to set options inherited from paramiko/libssh in ansible >= 2.11 (https://github.com/ansible-collections/ansible.netcommon/pull/271).
- network_cli - Fix for execution failing when ansible_ssh_password is used to specify password (https://github.com/ansible-collections/ansible.netcommon/issues/288)

ansible.posix
~~~~~~~~~~~~~

- Synchronize module not recognizing remote ssh key (https://github.com/ansible-collections/ansible.posix/issues/24).
- Synchronize not using quotes around arguments like --out-format (https://github.com/ansible-collections/ansible.posix/issues/190).
- at - append line-separator to the end of the ``command`` (https://github.com/ansible-collections/ansible.posix/issues/169).
- csh - define ``ECHO`` and ``COMMAND_SEP`` (https://github.com/ansible-collections/ansible.posix/issues/204).
- firewalld - enable integration after migration (https://github.com/ansible-collections/ansible.posix/pull/239).
- firewalld - ensure idempotency with firewalld 0.9.3 (https://github.com/ansible-collections/ansible.posix/issues/179).
- firewalld - fix setting zone target to ``%%REJECT%%`` (https://github.com/ansible-collections/ansible.posix/pull/215).
- mount - Handle ``boot`` option on Solaris correctly (https://github.com/ansible-collections/ansible.posix/issues/184).
- synchronize - add ``community.podman.podman`` to the list of supported connection plugins (https://github.com/ansible-community/molecule-podman/issues/45).
- synchronize - complete podman support for synchronize module.
- synchronize - properly quote rsync CLI parameters (https://github.com/ansible-collections/ansible.posix/pull/241).
- synchronize - replace removed ``ansible_ssh_user`` by ``ansible_user`` everywhere; do the same for ``ansible_ssh_port`` and ``ansible_ssh_host`` (https://github.com/ansible-collections/ansible.posix/issues/60).
- synchronize - use SSH args from SSH connection plugin (https://github.com/ansible-collections/ansible.posix/issues/222).
- synchronize - use become_user when invoking rsync on remote with sudo (https://github.com/ansible-collections/ansible.posix/issues/186).
- sysctl - modifying conditional check for docker to fix tests being skipped (https://github.com/ansible-collections/ansible.posix/pull/226).

ansible.utils
~~~~~~~~~~~~~

- Add support for the validation of formats to the jsonschema validator.
- Also include empty lists and mappings into the output dictionary (https://github.com/ansible-collections/ansible.utils/pull/58).
- Improve test coverage
- Update validate to use 2.11 ArgumentSpecValidator if available.

ansible.windows
~~~~~~~~~~~~~~~

- win_certificate_store - Make sure `store_name: CertificateAuthority` refers to the `CA` store for backwards compatibility - https://github.com/ansible-collections/ansible.windows/pull/216
- win_copy - Fix remote dest size calculation logic
- win_dns_client - Fix method used to read IPv6 DNS settings given by DHCP - https://github.com/ansible-collections/ansible.windows/issues/283
- win_dsc - Fix import errors when running against host that wasn't installed with the ``en-US`` locale - https://github.com/ansible-collections/ansible.windows/issues/83
- win_file - Fix conflicts with existing ``LIB`` environment variable
- win_find - Fix conflicts with existing ``LIB`` environment variable
- win_group - fixed ``description`` setting for a group that doesn't exist when running in check_mode (https://github.com/ansible-collections/ansible.windows/pull/260).
- win_reboot - Ensure documented return values are always returned even on a failure
- win_reboot - Fix local variable referenced before assignment issue - https://github.com/ansible-collections/ansible.windows/issues/276
- win_reboot - Handle connection failures when getting the first boot time command
- win_reboot - Handle more connection failures during the reboot phases
- win_reboot - User defined commands are run wrapped as a PowerShell command so they work on all shells - https://github.com/ansible-collections/ansible.windows/issues/36
- win_stat - Fix conflicts with existing ``LIB`` environment variable
- win_state - Fixed the ``creationtime``, ``lastaccesstime``, and ``lastwritetime`` to report the time in UTC. This matches the ``stat`` module's behaviour and what many would expect for a epoch based timestamp - https://github.com/ansible-collections/ansible.windows/issues/240
- win_updates - Always return the ``failed_updates_count`` on a standard failure - https://github.com/ansible-collections/ansible.windows/issues/13
- win_updates - Always use a scheduled task which should be less prone to random token errors when trying to connect to Windows Update - https://github.com/ansible-collections/ansible.windows/issues/193
- win_updates - Attempt a reboot once when ``reboot=True`` is set and a failure occurred - https://github.com/ansible-collections/ansible.windows/issues/22
- win_updates - Bypass execution policy checks when polling or cancelling the update task - https://github.com/ansible-collections/ansible.windows/issues/272
- win_updates - Fix conflicts with existing ``LIB`` environment variable
- win_updates - Fixed ``win_updates`` output to not cast to an integer to preserve original behaviour and issues with non integer values - https://github.com/ansible-collections/ansible.windows/issues/247
- win_updates - Ignore named pipes with illegal filenames when checking for the task named pipe during bootstrapping - https://github.com/ansible-collections/ansible.windows/issues/291
- win_updates - Improve error handling when starting background update task
- win_updates - Improve the reboot detection behaviour when ``reboot=True`` is set - https://github.com/ansible-collections/ansible.windows/issues/25
- win_updates - Improve the reboot mechanism - https://github.com/ansible-collections/ansible.windows/issues/143
- win_updates - Reboot the host when ``reboot=True`` if the first search result indicates a reboot is required - https://github.com/ansible-collections/ansible.windows/issues/49
- win_updates - fallback to run as SYSTEM if current user does not have batch logon rights - https://github.com/ansible-collections/ansible.windows/issues/253
- win_user - Fix ``msg`` return value when setting ``state: query``
- win_user - Set validate user logic to always check local database
- win_whoami - Fix conflicts with existing ``LIB`` environment variable

arista.eos
~~~~~~~~~~

- Add alias to neighbor and network in bgp_global so that lists of objects are plural.
- Add support to accomodate change in username config cli in latest eos software version.
- Added fix to support multiple keys under ip and ipv6 dict in parser template.
- Changed access_group parameter to type list, to enable multiple access-groups configuration.
- Fix logic error while executing replaced and overridden operations on bgp neighbors.
- Fix regex for password prompt.
- Fix typo and logic errors in bgp_global, to skip other routing protocol configs from running-config.
- Fix typo in eos_bgp_address_family redirection.
- argspec key 'shut_down' changed to 'shutdown'.
- command template fixed supporting Jinja version for centos-8 EEs.
- fix issue in prefix_lists facts code when prefix_lists facts are empty.
- fix issue in route-maps facts code when route-maps facts are empty.

cisco.aci
~~~~~~~~~

- Fix blacklist bug
- Fix cleanup of MGMT EPGs
- Fix module reference for l3out_node_profile cleanup task
- Fix required variables for absent and present states for l3out_node_profile
- Fix sanity & importer check errors
- Fix test and assertion variables and module references for l3out_node_profile tests
- pylint fix for .format()

cisco.asa
~~~~~~~~~

- Fix TypeError argument of type 'NoneType' is not iterable in service-group when service-group does not exists.
- Fixes asa_acls to add the support for service object group under destination option ((https://github.com/ansible-collections/cisco.asa/issues/100).
- Fixes asa_ogs protocol object to except protocol number as input (https://github.com/ansible-collections/cisco.asa/issues/116).
- Fixes description for "passwords" parameter in documentation (https://github.com/ansible-collections/cisco.asa/issues/132).
- Implement the replace block mode that is described in the docs for asa_acl (https://github.com/ansible-collections/cisco.asa/issues/97).
- To fix Cisco ASA network_object object config which wasn't working as expected.
- To fix asa_acls port range implementation, (https://github.com/ansible-collections/cisco.asa/issues/120, https://github.com/ansible-collections/cisco.asa/issues/121, https://github.com/ansible-collections/cisco.asa/issues/122).
- To fix asa_acls where ipv6 with host wasn't getting rendered as expected and facts was skipping.
- To fix asa_ogs for empty object traceback failure, (https://github.com/ansible-collections/cisco.asa/issues/124).
- To fix asa_ogs for parsing network object with ipv6 host address as expected (https://github.com/ansible-collections/cisco.asa/issues/128).

cisco.ios
~~~~~~~~~

- Add support for autoconfig and dhcp keywords for IPv6 addresses in l3_interfaces (https://github.com/ansible-collections/cisco.ios/pull/269).
- Fix IOS bgp global RM tracback while there's no bestpath/nopeerup_delay configured.
- Fix logging commands for v12 versions (https://github.com/ansible-collections/cisco.ios/issues/207).
- Fixed bgp_address_family, for rendering multiple neighbors when available in config.
- Logging command template fixed supporting Jinja version for centos-8 EEs.
- Reordering names of interface for proper value assignment
- To fix IOS vlans RM where traceback was thrown if show vlan wasn't supported on the device and also fix replace and overridden state behaviour.
- To fix Spelling glitch.
- To fix ios acls overridden and replaced state of their inconsistent behaviour (https://github.com/ansible-collections/cisco.ios/issues/250).
- To fix ios_bgp_address_family neighbor next_hop_self param (https://github.com/ansible-collections/cisco.ios/issues/319).
- To fix the wrong arg being passed in acls template function (https://github.com/ansible-collections/cisco.ios/pull/305).
- Updated ios_command module doc example section with appropriate punctuation.
- Updated ios_l3_interface as the newer Resource Module implementation and added features.
- fixed become functionality on privilege level not 15.
- fixes Serial interface configuration for l3_interfaces module and Unit Test cases added.
- fixes banner module with new attribute introduced
- fixes soft_reconfiguration and prefix_list command formation.
- ios_facts - fix for devices which have no support for VLANs, such as L3 devices.
- ios_user fails to add password when configured in separate task with update_password.
- ios_vlans - for playbook execution module fails with an error when target device does not support VLANs, The offline states rendered and parsed will work as expected.

cisco.iosxr
~~~~~~~~~~~

- Add warning when comment is not supported by IOSXR.
- Fix issue of commit operation which was not failing for invalid inputs.
- To add updated route policy params to Bgp nbr AF RM
- fix backword compatibility issue for iosxr 6.x.
- fix intermittent issue on CI for iosxr_banner module.
- fix iosxr_config issue for prefix-set,route-policy config
- fix issue in prefix-lists facts code when prefix-lists facts are empty. (https://github.com/ansible-collections/cisco.iosxr/pull/161)
- fix static routes interface parsing issue.

cisco.meraki
~~~~~~~~~~~~

- Allow a state of absent in voice vlan to allow the value to be nulled out(https://github.com/CiscoDevNet/ansible-meraki/issues/238)
- Fix some flake8 sanity errors as reported by Ansible Galaxy. Should be no functional change.
- meraki_ms_switchport - access_policy_types choices are incorrect causing failures. (https://github.com/CiscoDevNet/ansible-meraki/issues/227).
- meraki_ms_switchport - link_negotiation choice for 100 Megabit Auto is incorrect causing failures. (https://github.com/CiscoDevNet/ansible-meraki/issues/235).

cisco.mso
~~~~~~~~~

- Add test case and small fixes to mso_schema_site_bd_l3out module
- Fix documentation issues accross modules
- Fix fail_json usage accross module_utils/mso.py
- Fix mso_rest to support HTTPAPI plugin and tests to support ND platform
- Fix mso_user to due to error in v1 API in MSO 3.2
- Fix path issue in mso_schema_template_migrate
- Fixes for site level external epgs and site level L3Outs
- Fixes to support MSO 3.3
- Remove query of all schemas to get schema ID and only query schema ID indentity list API

cisco.nxos
~~~~~~~~~~

- Convert vlan lists to ranges in nxos_l2_interfaces (https://github.com/ansible-collections/cisco.nxos/issues/95).
- Do not expand direction 'both' into 'import' and 'export' for Nexus 9000 platforms (https://github.com/ansible-collections/cisco.nxos/issues/303).
- Fix how `send_community` attribute is handled in `nxos_bgp_neighbor_address_family` (https://github.com/ansible-collections/cisco.nxos/issues/281).
- Make `passive_interface` work properly when set to False.
- Prevent traceback when parsing unexpected line in nxos_static_routes.
- Render neighbor peer_type command correctly (https://github.com/ansible-collections/cisco.nxos/issues/308).
- `nxos_acls` - Fix traceback with 'port_protocol' range (https://github.com/ansible-collections/cisco.nxos/issues/356)
- `nxos_acls` - Updating an existing ACE can only be done with states replaced or overridden. Using state merged will result in a failure.
- `nxos_facts` - Fix KeyError while gathering CDP neighbor facts (https://github.com/ansible-collections/cisco.nxos/issues/354).
- `nxos_facts` - Fix gathering CDP neighbor facts from certain N7Ks (https://github.com/ansible-collections/cisco.nxos/issues/329).
- `nxos_logging_global` - Fix vlan_mgr not being gathered in facts (https://github.com/ansible-collections/cisco.nxos/issues/380).
- `nxos_ospf_interfaces` - Correctly sort interface names before rendering.
- `nxos_vlans` - Fallback to json when json-pretty is not supported (https://github.com/ansible-collections/cisco.nxos/issues/377).
- `nxos_vlans` - switching to `| json-pretty` instead of `| json` as a workaround for the timeout issue with `libssh` (https://github.com/ansible/pylibssh/issues/208)
- `nxos_zone_zoneset` - zone member addition with smart zoning in an already existing zone should be a no-op (https://github.com/ansible-collections/cisco.nxos/issues/339).

community.aws
~~~~~~~~~~~~~

- AWS action group - added missing ``aws_direct_connect_confirm_connection`` and ``efs_tag`` entries (https://github.com/ansible-collections/amazon.aws/issues/557).
- aws_secret - fix deletion idempotency when not using instant deletion (https://github.com/ansible-collections/community.aws/pull/681).
- aws_ssm - rename ``retries`` to ``reconnection_retries`` to avoid conflict with task retries
- cloudfront_info - Switch to native boto3 paginators to fix reported bug when over 100 distributions exist (https://github.com/ansible-collections/community.aws/issues/769).
- ec2_eip - fix bug when allocating an EIP but not associating it to a VPC (https://github.com/ansible-collections/community.aws/pull/731).
- ec2_vpc_peer - automatically retry when attempting to tag freshly created peering connections (https://github.com/ansible-collections/community.aws/pull/614).
- ec2_vpc_route_table - automatically retry when attempting to modify freshly created route tables (https://github.com/ansible-collections/community.aws/pull/616).
- ecs_taskdefinition - ensure cast to integer (https://github.com/ansible-collections/community.aws/pull/574).
- ecs_taskdefinition - fix idempotency (https://github.com/ansible-collections/community.aws/pull/574).
- ecs_taskdefinition - fix typo in ecs task defination for env file validations (https://github.com/ansible-collections/community.aws/pull/600).
- elb_classic_lb_info - fix empty list returned when names not defined (https://github.com/ansible-collections/community.aws/pull/693).
- elb_instance - Python 3 compatability fix (https://github.com/ansible-collections/community.aws/issues/384).
- iam_role - Modified iam_role internal code to replace update_role_description with update_role (https://github.com/ansible-collections/community.aws/pull/697).
- iam_role_info - switch to jittered backoff to reduce rate limiting failures (https://github.com/ansible-collections/community.aws/pull/748).
- rds_instance - Fixed issue with enabling enhanced monitoring on a pre-existing RDS instance (https://github.com/ansible-collections/community.aws/pull/747).
- route53 - add missing set identifier in resource_record_set (https://github.com/ansible-collections/community.aws/pull/595).
- route53 - fix diff mode when deleting records (https://github.com/ansible-collections/community.aws/pull/802).
- route53 - fix typo in waiter configuration that prevented management of the delays (https://github.com/ansible-collections/community.aws/pull/564).
- route53 - return empty result for nonexistent records (https://github.com/ansible-collections/community.aws/pull/799).
- s3_sync - fix handling individual file path to upload a individual file to s3 bucket (https://github.com/ansible-collections/community.aws/pull/692).
- sns_topic - define suboptions for delivery_policy option (https://github.com/ansible-collections/community.aws/issues/713).
- sqs_queue - fix queue attribute comparison to make module idempotent (https://github.com/ansible-collections/community.aws/pull/592).

community.crypto
~~~~~~~~~~~~~~~~

- acme_* modules - fix commands composed for OpenSSL backend to retrieve information on CSRs and certificates from stdin to use ``/dev/stdin`` instead of ``-``. This is needed for OpenSSL 1.0.1 and 1.0.2, apparently (https://github.com/ansible-collections/community.crypto/pull/279).
- acme_certificate - avoid passing multiple certificates to ``cryptography``'s X.509 certificate loader when ``fullchain_dest`` is used (https://github.com/ansible-collections/community.crypto/pull/324).
- acme_challenge_cert_helper - only return exception when cryptography is not installed, not when a too old version of it is installed. This prevents Ansible's callback to crash (https://github.com/ansible-collections/community.crypto/pull/281).
- cryptography backend - improve Unicode handling for Python 2 (https://github.com/ansible-collections/community.crypto/pull/313).
- get_certificate - fix compatibility with the cryptography 35.0.0 release (https://github.com/ansible-collections/community.crypto/pull/294).
- get_certificate, openssl_csr_info, x509_certificate_info - add fallback code for extension parsing that works with cryptography 36.0.0 and newer. This code re-serializes de-serialized extensions and thus can return slightly different values if the extension in the original CSR resp. certificate was not canonicalized correctly. This code is currently used as a fallback if the existing code stops working, but we will switch it to be the main code in a future release (https://github.com/ansible-collections/community.crypto/pull/331).
- keypair_backend module utils - simplify code to pass sanity tests (https://github.com/ansible-collections/community.crypto/pull/263).
- luks_device - now also runs a built-in LUKS signature cleaner on ``state=absent`` to make sure that also the secondary LUKS2 header is wiped when older versions of wipefs are used (https://github.com/ansible-collections/community.crypto/issues/326, https://github.com/ansible-collections/community.crypto/pull/327).
- openssh_cert - fixed certificate generation to restore original certificate if an error is encountered (https://github.com/ansible-collections/community.crypto/pull/255).
- openssh_keypair - fix ``check_mode`` to populate return values for existing keypairs (https://github.com/ansible-collections/community.crypto/issues/113, https://github.com/ansible-collections/community.crypto/pull/230).
- openssh_keypair - fixed ``cryptography`` backend to preserve original file permissions when regenerating a keypair requires existing files to be overwritten (https://github.com/ansible-collections/community.crypto/pull/260).
- openssh_keypair - fixed a bug that prevented custom file attributes being applied to public keys (https://github.com/ansible-collections/community.crypto/pull/257).
- openssh_keypair - fixed error handling to restore original keypair if regeneration fails (https://github.com/ansible-collections/community.crypto/pull/260).
- openssl_csr and openssl_csr_pipe - make sure that Unicode strings are used to compare strings with the cryptography backend. This fixes idempotency problems with non-ASCII letters on Python 2 (https://github.com/ansible-collections/community.crypto/issues/270, https://github.com/ansible-collections/community.crypto/pull/271).
- openssl_csr_info - fix compatibility with the cryptography 35.0.0 release (https://github.com/ansible-collections/community.crypto/pull/294).
- openssl_csr_info - fix compatibility with the cryptography 35.0.0 release in PyOpenSSL backend (https://github.com/ansible-collections/community.crypto/pull/300).
- openssl_pkcs12 - fix compatibility with the cryptography 35.0.0 release (https://github.com/ansible-collections/community.crypto/pull/296).
- openssl_pkcs12 - fix crash when loading passphrase-protected PKCS#12 files with ``cryptography`` backend (https://github.com/ansible-collections/community.crypto/issues/247, https://github.com/ansible-collections/community.crypto/pull/248).
- openssl_pkcs12 - use new PKCS#12 deserialization infrastructure from cryptography 36.0.0 if available (https://github.com/ansible-collections/community.crypto/pull/302).
- various modules - prevent crashes when modules try to set attributes on not yet existing files in check mode. This will be fixed in ansible-core 2.12, but it is not backported to every Ansible version we support (https://github.com/ansible-collections/community.crypto/issue/242, https://github.com/ansible-collections/community.crypto/pull/243).
- x509_certificate - fix crash when ``assertonly`` provider is used and some error conditions should be reported (https://github.com/ansible-collections/community.crypto/issues/240, https://github.com/ansible-collections/community.crypto/pull/241).
- x509_certificate_info - fix compatibility with the cryptography 35.0.0 release (https://github.com/ansible-collections/community.crypto/pull/294).
- x509_certificate_info - fix compatibility with the cryptography 35.0.0 release in PyOpenSSL backend (https://github.com/ansible-collections/community.crypto/pull/300).
- x509_crl - restore inherited function signature to pass sanity tests (https://github.com/ansible-collections/community.crypto/pull/263).

community.digitalocean
~~~~~~~~~~~~~~~~~~~~~~

- Adding missing status badges for black and unit tests (https://github.com/ansible-collections/community.digitalocean/pull/164).
- Documentation URLs are fixed for the C(digital_ocean_domain_record) and C(digital_ocean_droplet_info) modules (https://github.com/ansible-collections/community.digitalocean/pull/163).
- Serializing the cloud integration tests (https://github.com/ansible-collections/community.digitalocean/pull/165).
- Update the tests so that they only run once (https://github.com/ansible-collections/community.digitalocean/issues/186).
- digital_ocean - integration tests need community.general and jmespath (https://github.com/ansible-collections/community.digitalocean/issues/121).
- digital_ocean inventory script - fail cleaner on invalid ``HOST`` argument to ``--host`` option (https://github.com/ansible-collections/community.digitalocean/pull/44).
- digital_ocean inventory script - implement unimplemented ``use_private_network`` option and register missing ``do_ip_address``, ``do_private_ip_address`` host vars (https://github.com/ansible-collections/community.digitalocean/pull/45/files).
- digital_ocean inventory script - return JSON consistent with specification with ``--host`` (https://github.com/ansible-collections/community.digitalocean/pull/44).
- digital_ocean_block_storage - fix block volumes detach idempotency (https://github.com/ansible-collections/community.digitalocean/issues/149).
- digital_ocean_certificate - fixing integration test (https://github.com/ansible-collections/community.digitalocean/issues/114).
- digital_ocean_certificate_info - ensure return type is a list (https://github.com/ansible-collections/community.digitalocean/issues/55).
- digital_ocean_database - Fixed DB attribute settings (https://github.com/ansible-collections/community.digitalocean/issues/94).
- digital_ocean_database - increase the database creation integration test timeout (https://github.com/ansible-collections/community.digitalocean).
- digital_ocean_database_info - Cleanup unused attribs (https://github.com/ansible-collections/community.digitalocean/pulls/100).
- digital_ocean_domain - return zone records when creating a new zone (https://github.com/ansible-collections/community.digitalocean/issues/46).
- digital_ocean_domain_info - ensure return type is a list (https://github.com/ansible-collections/community.digitalocean/issues/55).
- digital_ocean_droplet - Add integration tests for Droplet active and inactive states (https://github.com/ansible-collections/community.digitalocean/issues/66).
- digital_ocean_droplet - Fix Droplet inactive state (https://github.com/ansible-collections/community.digitalocean/issues/83).
- digital_ocean_droplet - Fixed Droplet inactive state (https://github.com/ansible-collections/community.digitalocean/pull/88).
- digital_ocean_droplet - add missing ``required=True`` on ``do_oauth_token`` in ``argument_spec`` (https://github.com/ansible-collections/community.digitalocean/issues/13).
- digital_ocean_droplet - ensure "active" state before issuing "power on" action (https://github.com/ansible-collections/community.digitalocean/issues/150)
- digital_ocean_droplet - fix resizing with C(state: active) does not actually turn Droplet on (https://github.com/ansible-collections/community.digitalocean/issues/140).
- digital_ocean_droplet - power on should poll/wait, resize should support "active" state (https://github.com/ansible-collections/community.digitalocean/pull/143).
- digital_ocean_droplet - state `present` with `wait` was not waiting (https://github.com/ansible-collections/community.digitalocean/issues/116).
- digital_ocean_droplet_info - Fix documentation link for `digital_ocean_droplet_info` (https://github.com/ansible-collections/community.digitalocean/pull/81).
- digital_ocean_firewall - fixed idempotence (https://github.com/ansible-collections/community.digitalocean/issues/122).
- digital_ocean_firewall - fixing integration test (https://github.com/ansible-collections/community.digitalocean/issues/114).
- digital_ocean_firewall_info - ensure return type is a list (https://github.com/ansible-collections/community.digitalocean/issues/55).
- digital_ocean_floating_ip - delete all Floating IPs initially during the integration test run (https://github.com/ansible-collections/community.digitalocean/issues/129).
- digital_ocean_floating_ip - fixes idempotence (https://github.com/ansible-collections/community.digitalocean/issues/5).
- digital_ocean_floating_ip - make floating ip return data idempotent (https://github.com/ansible-collections/community.digitalocean/pull/162).
- digital_ocean_kubernetes - fix return value consistency (https://github.com/ansible-collections/community.digitalocean/issues/174).
- digital_ocean_load_balancer - C(droplet_ids) are not required when C(state=absent) is chosen (https://github.com/ansible-collections/community.digitalocean/pull/147).
- digital_ocean_load_balancer - when C(state=absent) is chosen the API returns an empty response (https://github.com/ansible-collections/community.digitalocean/pull/147).
- digital_ocean_load_balancer_info - ensure return type is a list (https://github.com/ansible-collections/community.digitalocean/issues/55).
- digital_ocean_snapshot_info - Fix lookup of snapshot_info by_id (https://github.com/ansible-collections/community.digitalocean/issues/92).
- digital_ocean_sshkey - Fixed SSH Key Traceback Issue (https://github.com/ansible-collections/community.digitalocean/issues/68).
- digital_ocean_tag - Fix tag idempotency (https://github.com/ansible-collections/community.digitalocean/issues/61).
- digital_ocean_tag - fixing integration test (https://github.com/ansible-collections/community.digitalocean/issues/114).
- digital_ocean_tag_info - ensure return type is a list (https://github.com/ansible-collections/community.digitalocean/issues/55).
- digitalocean - Fix return docs for digital_ocean_sshkey_info (https://github.com/ansible-collections/community.digitalocean/issues/56).
- digitalocean - Update README.md for K8s and databases (https://github.com/ansible-collections/community.digitalocean/pull/80).
- digitalocean - update README.md with project_info and project module (https://github.com/ansible-collections/community.digitalocean/pull/112).
- digitalocean inventory - enforce the C(timeout) parameter (https://github.com/ansible-collections/community.digitalocean/issues/168).
- digitalocean inventory - respect the TRANSFORM_INVALID_GROUP_CHARS configuration setting (https://github.com/ansible-collections/community.digitalocean/pull/138).
- digitalocean inventory plugin - Wire up advertised caching functionality (https://github.com/ansible-collections/community.digitalocean/pull/97).
- digitalocean inventory plugin - attributes available to filters are limited to explicitly required attributes and are prefixed with ``var_prefix`` (https://github.com/ansible-collections/community.digitalocean/pull/102).
- info modules - adding missing check mode support (https://github.com/ansible-collections/community.digitalocean/issues/139).

community.docker
~~~~~~~~~~~~~~~~

- docker-compose - fix not pulling when ``state: present`` and ``stopped: true`` (https://github.com/ansible-collections/community.docker/issues/12, https://github.com/ansible-collections/community.docker/pull/119).
- docker_* modules and plugins, except ``docker_swarm`` connection plugin and ``docker_compose`` and ``docker_stack*` modules - only emit ``tls_hostname`` deprecation message if TLS is actually used (https://github.com/ansible-collections/community.docker/pull/143).
- docker_compose - fix idempotence bug when using ``stopped: true`` (https://github.com/ansible-collections/community.docker/issues/142, https://github.com/ansible-collections/community.docker/pull/159).
- docker_compose - fixed incorrect ``changed`` status for services with ``profiles`` defined, but none enabled (https://github.com/ansible-collections/community.docker/pull/192).
- docker_compose - fixes task failures when bringing up services while using ``docker-compose <1.17.0`` (https://github.com/ansible-collections/community.docker/issues/180).
- docker_container - make sure to also return ``container`` on ``detached=false`` when status code is non-zero (https://github.com/ansible-collections/community.docker/pull/178).
- docker_plugin - also configure plugin after installing (https://github.com/ansible-collections/community.docker/issues/118, https://github.com/ansible-collections/community.docker/pull/135).
- docker_stack_info - make sure that module isn't skipped in check mode (https://github.com/ansible-collections/community.docker/pull/183).
- docker_stack_task_info - make sure that module isn't skipped in check mode (https://github.com/ansible-collections/community.docker/pull/183).
- docker_swarm_services - avoid crash during idempotence check if ``published_port`` is not specified (https://github.com/ansible-collections/community.docker/issues/107, https://github.com/ansible-collections/community.docker/pull/136).

community.general
~~~~~~~~~~~~~~~~~

- _mount module utils - fixed the sanity checks (https://github.com/ansible-collections/community.general/pull/2883).
- a_module test plugin - fix crash when testing a module name that was tombstoned (https://github.com/ansible-collections/community.general/pull/3660).
- ali_instance_info - added support to check mode (https://github.com/ansible-collections/community.general/pull/3084).
- ansible_galaxy_install - the output value ``cmd_args`` was bringing the intermediate command used to gather the state, instead of the command that actually performed the state change (https://github.com/ansible-collections/community.general/pull/3655).
- apache2_module - fix ``a2enmod``/``a2dismod`` detection, and error message when not found (https://github.com/ansible-collections/community.general/issues/3253).
- archive - fixed ``exclude_path`` values causing incorrect archive root (https://github.com/ansible-collections/community.general/pull/2816).
- archive - fixed improper file names for single file zip archives (https://github.com/ansible-collections/community.general/issues/2818).
- archive - fixed incorrect ``state`` result value documentation (https://github.com/ansible-collections/community.general/pull/2816).
- archive - fixed task failure when using the ``remove`` option with a ``path`` containing nested files for ``format``s other than ``zip`` (https://github.com/ansible-collections/community.general/issues/2919).
- archive - fixing archive root determination when longest common root is ``/`` (https://github.com/ansible-collections/community.general/pull/3036).
- composer - use ``no-interaction`` option when discovering available options to avoid an issue where composer hangs (https://github.com/ansible-collections/community.general/pull/2348).
- consul_acl - update the hcl allowlist to include all supported options (https://github.com/ansible-collections/community.general/pull/2495).
- consul_kv lookup plugin - allow to set ``recurse``, ``index``, ``datacenter`` and ``token`` as keyword arguments (https://github.com/ansible-collections/community.general/issues/2124).
- copr - fix chroot naming issues, ``centos-stream`` changed naming to ``centos-stream-<number>`` (for exmaple ``centos-stream-8``) (https://github.com/ansible-collections/community.general/issues/2084, https://github.com/ansible-collections/community.general/pull/3237).
- counter_enabled callback plugin - fix output to correctly display host and task counters in serial mode (https://github.com/ansible-collections/community.general/pull/3709).
- cpanm - also use ``LC_ALL`` to enforce locale choice (https://github.com/ansible-collections/community.general/pull/2731).
- deploy_helper - improved parameter checking by using standard Ansible construct (https://github.com/ansible-collections/community.general/pull/3104).
- django_manage - argument ``command`` is being splitted again as it should (https://github.com/ansible-collections/community.general/issues/3215).
- django_manage - parameters ``apps`` and ``fixtures`` are now splitted instead of being used as a single argument (https://github.com/ansible-collections/community.general/issues/3333).
- django_manage - refactor to call ``run_command()`` passing command as a list instead of string (https://github.com/ansible-collections/community.general/pull/3098).
- ejabberd_user - replaced in-code check with ``required_if``, using ``get_bin_path()`` for the command, passing args to ``run_command()`` as list instead of string (https://github.com/ansible-collections/community.general/pull/3093).
- filesystem - repair ``reiserfs`` fstype support after adding it to integration tests (https://github.com/ansible-collections/community.general/pull/2472).
- gitlab_deploy_key - fix idempotency on projects with multiple deploy keys (https://github.com/ansible-collections/community.general/pull/3473).
- gitlab_deploy_key - fix the SSH Deploy Key being deleted accidentally while running task in check mode (https://github.com/ansible-collections/community.general/issues/3621, https://github.com/ansible-collections/community.general/pull/3622).
- gitlab_group - avoid passing wrong value for ``require_two_factor_authentication`` on creation when the option has not been specified (https://github.com/ansible-collections/community.general/pull/3453).
- gitlab_group_members - ``get_group_id`` return the group ID by matching ``full_path``, ``path`` or ``name`` (https://github.com/ansible-collections/community.general/pull/3400).
- gitlab_group_members - fixes issue when gitlab group has more then 20 members, pagination problem (https://github.com/ansible-collections/community.general/issues/3041).
- gitlab_project - user projects are created using namespace ID now, instead of user ID (https://github.com/ansible-collections/community.general/pull/2881).
- gitlab_project_members - ``get_project_id`` return the project id by matching ``full_path`` or ``name`` (https://github.com/ansible-collections/community.general/pull/3602).
- gitlab_project_members - fixes issue when gitlab group has more then 20 members, pagination problem (https://github.com/ansible-collections/community.general/issues/3041).
- idrac_redfish_info - added support to check mode (https://github.com/ansible-collections/community.general/pull/3084).
- influxdb_retention_policy - fix bug where ``INF`` duration values failed parsing (https://github.com/ansible-collections/community.general/pull/2385).
- influxdb_user - allow creation of admin users when InfluxDB authentication is enabled but no other user exists on the database. In this scenario, InfluxDB 1.x allows only ``CREATE USER`` queries and rejects any other query (https://github.com/ansible-collections/community.general/issues/2364).
- influxdb_user - fix bug where an influxdb user has no privileges for 2 or more databases (https://github.com/ansible-collections/community.general/pull/2499).
- influxdb_user - fix bug which removed current privileges instead of appending them to existing ones (https://github.com/ansible-collections/community.general/issues/2609, https://github.com/ansible-collections/community.general/pull/2614).
- ini_file - fix Unicode processing for Python 2 (https://github.com/ansible-collections/community.general/pull/2875).
- ini_file - fix inconsistency between empty value and no value (https://github.com/ansible-collections/community.general/issues/3031).
- interfaces_file - no longer reporting change when none happened (https://github.com/ansible-collections/community.general/pull/3328).
- inventory and vault scripts - change file permissions to make vendored inventory and vault scripts exectuable (https://github.com/ansible-collections/community.general/pull/2337).
- ipa_* modules - fix environment fallback for ``ipa_host`` option (https://github.com/ansible-collections/community.general/issues/3560).
- ipa_sudorule - call ``sudorule_add_allow_command`` method instead of  ``sudorule_add_allow_command_group`` (https://github.com/ansible-collections/community.general/issues/2442).
- iptables_state - call ``async_status`` action plugin rather than its module (https://github.com/ansible-collections/community.general/issues/2700).
- iptables_state - fix a 'FutureWarning' in a regex and do some basic code clean up (https://github.com/ansible-collections/community.general/pull/2525).
- iptables_state - fix a broken query of ``async_status`` result with current ansible-core development version (https://github.com/ansible-collections/community.general/issues/2627, https://github.com/ansible-collections/community.general/pull/2671).
- iptables_state - fix initialization of iptables from null state when adressing more than one table (https://github.com/ansible-collections/community.general/issues/2523).
- java_cert - fix issue with incorrect alias used on PKCS#12 certificate import (https://github.com/ansible-collections/community.general/pull/2560).
- java_cert - import private key as well as public certificate from PKCS#12 (https://github.com/ansible-collections/community.general/issues/2460).
- java_keystore - add parameter ``keystore_type`` to control output file format and override ``keytool``'s default, which depends on Java version (https://github.com/ansible-collections/community.general/issues/2515).
- jboss - fix the deployment file permission issue when Jboss server is running under non-root user. The deployment file is copied with file content only. The file permission is set to ``440`` and belongs to root user. When the JBoss ``WildFly`` server is running under non-root user, it is unable to read the deployment file (https://github.com/ansible-collections/community.general/pull/3426).
- jenkins_build - examine presence of ``build_number`` before deleting a jenkins build (https://github.com/ansible-collections/community.general/pull/2850).
- jenkins_plugin - use POST method for sending request to jenkins API when ``state`` option is one of ``enabled``, ``disabled``, ``pinned``, ``unpinned``, or ``absent`` (https://github.com/ansible-collections/community.general/issues/2510).
- json_query filter plugin - avoid 'unknown type' errors for more Ansible internal types (https://github.com/ansible-collections/community.general/pull/2607).
- keycloak_authentication - fix bug when two identical executions are in the same authentication flow (https://github.com/ansible-collections/community.general/pull/2904).
- keycloak_authentication - fix bug, the requirement was always on ``DISABLED`` when creating a new authentication flow (https://github.com/ansible-collections/community.general/pull/3330).
- keycloak_client - update the check mode to not show differences resulting from sorting and default values relating to the properties, ``redirectUris``, ``attributes``, and ``protocol_mappers`` (https://github.com/ansible-collections/community.general/pull/3610).
- keycloak_identity_provider - fix change detection when updating identity provider mappers (https://github.com/ansible-collections/community.general/pull/3538, https://github.com/ansible-collections/community.general/issues/3537).
- keycloak_realm - ``ssl_required`` changed from a boolean type to accept the strings ``none``, ``external`` or ``all``. This is not a breaking change since the module always failed when a boolean was supplied (https://github.com/ansible-collections/community.general/pull/2693).
- keycloak_realm - element type for ``events_listeners`` parameter should be ``string`` instead of ``dict`` (https://github.com/ansible-collections/community.general/pull/3231).
- keycloak_realm - remove warning that ``reset_password_allowed`` needs to be marked as ``no_log`` (https://github.com/ansible-collections/community.general/pull/2694).
- keycloak_role - quote role name when used in URL path to avoid errors when role names contain special characters (https://github.com/ansible-collections/community.general/issues/3535, https://github.com/ansible-collections/community.general/pull/3536).
- launchd - fixed sanity check in the module's code (https://github.com/ansible-collections/community.general/pull/2960).
- launchd - use private attribute to fix sanity errors (https://github.com/ansible-collections/community.general/pull/3194).
- ldap_search - allow it to be used even in check mode (https://github.com/ansible-collections/community.general/issues/3619).
- linode inventory plugin - fix default value of new option ``ip_style`` (https://github.com/ansible-collections/community.general/issues/3337).
- linode_v4 - changed the error message to point to the correct bugtracker URL (https://github.com/ansible-collections/community.general/pull/2430).
- logdns callback plugin - improve split call to fix sanity errors (https://github.com/ansible-collections/community.general/pull/3194).
- logstash callback plugin - replace ``_option`` with ``context.CLIARGS`` to fix the plugin on ansible-base and ansible-core (https://github.com/ansible-collections/community.general/issues/2692).
- lvol - allows logical volumes to be created with certain size arguments prefixed with ``+`` to preserve behavior of older versions of this module (https://github.com/ansible-collections/community.general/issues/3665).
- lvol - fixed rounding errors (https://github.com/ansible-collections/community.general/issues/2370).
- lvol - fixed size unit capitalization to match units used between different tools for comparison (https://github.com/ansible-collections/community.general/issues/2360).
- lvol - honor ``check_mode`` on thinpool (https://github.com/ansible-collections/community.general/issues/2934).
- macports - add ``stdout`` and ``stderr`` to return values (https://github.com/ansible-collections/community.general/issues/3499).
- maven_artifact - improve split call to fix sanity errors (https://github.com/ansible-collections/community.general/pull/3194).
- memcached cache plugin - change function argument names to fix sanity errors (https://github.com/ansible-collections/community.general/pull/3194).
- memset_memstore_info - added support to check mode (https://github.com/ansible-collections/community.general/pull/3084).
- memset_server_info - added support to check mode (https://github.com/ansible-collections/community.general/pull/3084).
- modprobe - added additional checks to ensure module load/unload is effective (https://github.com/ansible-collections/community.general/issues/1608).
- module_helper module utils - ``CmdMixin`` must also use ``LC_ALL`` to enforce locale choice (https://github.com/ansible-collections/community.general/pull/2731).
- module_helper module utils - avoid failing when non-zero ``rc`` is present on regular exit (https://github.com/ansible-collections/community.general/pull/2912).
- module_helper module utils - fixed change-tracking for dictionaries and lists (https://github.com/ansible-collections/community.general/pull/2951).
- netapp module utils - remove always-true conditional to fix sanity errors (https://github.com/ansible-collections/community.general/pull/3194).
- netcup_dns - use ``str(ex)`` instead of unreliable ``ex.message`` in exception handling to fix ``AttributeError`` in error cases (https://github.com/ansible-collections/community.general/pull/2590).
- nmap inventory plugin - fix local variable error when cache is disabled (https://github.com/ansible-collections/community.general/issues/2512).
- nmcli - added ip4/ip6 configuration arguments for ``sit`` and ``ipip`` tunnels (https://github.com/ansible-collections/community.general/issues/3238, https://github.com/ansible-collections/community.general/pull/3239).
- nmcli - compare MAC addresses case insensitively to fix idempotency issue (https://github.com/ansible-collections/community.general/issues/2409).
- nmcli - fixed ``dns6`` option handling so that it is treated as a list internally (https://github.com/ansible-collections/community.general/pull/3563).
- nmcli - fixed ``ipv4.route-metric`` being in properties of type list (https://github.com/ansible-collections/community.general/pull/3563).
- nmcli - fixed falsely reported changed status when ``mtu`` is omitted with ``dummy`` connections (https://github.com/ansible-collections/community.general/issues/3612, https://github.com/ansible-collections/community.general/pull/3625).
- nmcli - fixes team-slave configuration by adding connection.slave-type (https://github.com/ansible-collections/community.general/issues/766).
- nmcli - if type is ``bridge-slave`` add ``slave-type bridge`` to ``nmcli`` command (https://github.com/ansible-collections/community.general/issues/2408).
- npm - correctly handle cases where a dependency does not have a ``version`` property because it is either missing or invalid (https://github.com/ansible-collections/community.general/issues/2917).
- npm - when the ``version`` option is used the comparison of installed vs missing will use name@version instead of just name, allowing version specific updates (https://github.com/ansible-collections/community.general/issues/2021).
- one_image - fix error message when renaming an image (https://github.com/ansible-collections/community.general/pull/3626).
- one_template - change function argument name to fix sanity errors (https://github.com/ansible-collections/community.general/pull/3194).
- one_vm - Allow missing NIC keys (https://github.com/ansible-collections/community.general/pull/2435).
- oneview_datacenter_info - added support to check mode (https://github.com/ansible-collections/community.general/pull/3084).
- oneview_enclosure_info - added support to check mode (https://github.com/ansible-collections/community.general/pull/3084).
- oneview_ethernet_network_info - added support to check mode (https://github.com/ansible-collections/community.general/pull/3084).
- oneview_fc_network_info - added support to check mode (https://github.com/ansible-collections/community.general/pull/3084).
- oneview_fcoe_network_info - added support to check mode (https://github.com/ansible-collections/community.general/pull/3084).
- oneview_logical_interconnect_group_info - added support to check mode (https://github.com/ansible-collections/community.general/pull/3084).
- oneview_network_set_info - added support to check mode (https://github.com/ansible-collections/community.general/pull/3084).
- oneview_san_manager_info - added support to check mode (https://github.com/ansible-collections/community.general/pull/3084).
- online inventory plugin - improve split call to fix sanity errors (https://github.com/ansible-collections/community.general/pull/3194).
- online module utils - improve split call to fix sanity errors (https://github.com/ansible-collections/community.general/pull/3194).
- open_iscsi - calling ``run_command`` with arguments as ``list`` instead of ``str`` (https://github.com/ansible-collections/community.general/pull/3286).
- openbsd_pkg - fix crash from ``KeyError`` exception when package installs, but ``pkg_add`` returns with a non-zero exit code (https://github.com/ansible-collections/community.general/pull/3336).
- openbsd_pkg - fix regexp matching crash. This bug could trigger on package names with special characters, for example ``g++`` (https://github.com/ansible-collections/community.general/pull/3161).
- opentelemetry callback plugin - validated the task result exception without crashing. Also simplifying code a bit (https://github.com/ansible-collections/community.general/pull/3450, https://github.com/ansible/ansible/issues/75726).
- openwrt_init - calling ``run_command`` with arguments as ``list`` instead of ``str`` (https://github.com/ansible-collections/community.general/pull/3284).
- ovir4 inventory script - improve configparser creation to avoid crashes for options without values (https://github.com/ansible-collections/community.general/issues/674).
- packet_device - use generator to fix sanity errors (https://github.com/ansible-collections/community.general/pull/3194).
- packet_sshkey - use generator to fix sanity errors (https://github.com/ansible-collections/community.general/pull/3194).
- pacman - fix changed status when ignorepkg has been defined (https://github.com/ansible-collections/community.general/issues/1758).
- pamd - code for ``state=updated`` when dealing with the pam module arguments, made no distinction between ``None`` and an empty list (https://github.com/ansible-collections/community.general/issues/3260).
- pamd - fixed problem with files containing only one or two lines (https://github.com/ansible-collections/community.general/issues/2925).
- pids - avoid crashes for older ``psutil`` versions, like on RHEL6 and RHEL7 (https://github.com/ansible-collections/community.general/pull/2808).
- pipx - ``state=inject`` was failing to parse the list of injected packages (https://github.com/ansible-collections/community.general/pull/3611).
- pipx - set environment variable ``USE_EMOJI=0`` to prevent errors in platforms that do not support ``UTF-8`` (https://github.com/ansible-collections/community.general/pull/3611).
- pipx - the output value ``cmd_args`` was bringing the intermediate command used to gather the state, instead of the command that actually performed the state change (https://github.com/ansible-collections/community.general/pull/3655).
- pkgin - Fix exception encountered when all packages are already installed (https://github.com/ansible-collections/community.general/pull/3583).
- pkgng - ``name=* state=latest`` check for upgrades did not count "Number of packages to be reinstalled" as a `changed` action, giving incorrect results in both regular and check mode (https://github.com/ansible-collections/community.general/pull/3526).
- pkgng - an `earlier PR <https://github.com/ansible-collections/community.general/pull/3393>`_ broke check mode so that the module always reports `not changed`. This is now fixed so that the module reports number of upgrade or install actions that would be performed (https://github.com/ansible-collections/community.general/pull/3526).
- pkgng - the ``annotation`` functionality was broken and is now fixed, and now also works with check mode (https://github.com/ansible-collections/community.general/pull/3526).
- proxmox inventory plugin - fixed parsing failures when some cluster nodes are offline (https://github.com/ansible-collections/community.general/issues/2931).
- proxmox inventory plugin - fixed plugin failure when a ``qemu`` guest has no ``template`` key (https://github.com/ansible-collections/community.general/pull/3052).
- proxmox_group_info - fix module crash if a ``group`` parameter is used (https://github.com/ansible-collections/community.general/pull/3649).
- proxmox_kvm - clone operation should return the VMID of the target VM and not that of the source VM. This was failing when the target VM with the chosen name already existed (https://github.com/ansible-collections/community.general/pull/3266).
- proxmox_kvm - fix parsing of Proxmox VM information with device info not containing a comma, like disks backed by ZFS zvols (https://github.com/ansible-collections/community.general/issues/2840).
- proxmox_kvm - fix result of clone, now returns ``newid`` instead of ``vmid`` (https://github.com/ansible-collections/community.general/pull/3034).
- proxmox_kvm - fixed ``vmid`` return value when VM with ``name`` already exists (https://github.com/ansible-collections/community.general/issues/2648).
- puppet - replace ``console` with ``stdout`` in ``logdest`` option when ``all`` has been chosen (https://github.com/ansible-collections/community.general/issues/1190).
- rax_facts - added support to check mode (https://github.com/ansible-collections/community.general/pull/3084).
- redfish_command - fix extraneous error caused by missing ``bootdevice`` argument when using the ``DisableBootOverride`` sub-command (https://github.com/ansible-collections/community.general/issues/3005).
- redfish_info - added support to check mode (https://github.com/ansible-collections/community.general/pull/3084).
- redfish_utils module utils - do not attempt to change the boot source override mode if not specified by the user (https://github.com/ansible-collections/community.general/issues/3509/).
- redfish_utils module utils - if a manager network property is not specified in the service, attempt to change the requested settings (https://github.com/ansible-collections/community.general/issues/3404/).
- redfish_utils module utils - if given, add account ID of user that should be created to HTTP request (https://github.com/ansible-collections/community.general/pull/3343/).
- redis cache - improved connection string parsing (https://github.com/ansible-collections/community.general/issues/497).
- rhsm_release - fix the issue that module considers 8, 7Client and 7Workstation as invalid releases (https://github.com/ansible-collections/community.general/pull/2571).
- saltstack connection plugin - fix function signature (https://github.com/ansible-collections/community.general/pull/3194).
- scaleway module utils - improve split call to fix sanity errors (https://github.com/ansible-collections/community.general/pull/3194).
- scaleway plugin inventory - fix ``JSON object must be str, not 'bytes'`` with Python 3.5 (https://github.com/ansible-collections/community.general/issues/2769).
- smartos_image_info - added support to check mode (https://github.com/ansible-collections/community.general/pull/3084).
- snap - also use ``LC_ALL`` to enforce locale choice (https://github.com/ansible-collections/community.general/pull/2731).
- snap - fix formatting of ``--channel`` argument when the ``channel`` option is used (https://github.com/ansible-collections/community.general/pull/3028).
- snap - fix various bugs which prevented the module from working at all, and which resulted in ``state=absent`` fail on absent snaps (https://github.com/ansible-collections/community.general/issues/2835, https://github.com/ansible-collections/community.general/issues/2906, https://github.com/ansible-collections/community.general/pull/2912).
- snap - fixed the order of the ``--classic`` parameter in the command line invocation (https://github.com/ansible-collections/community.general/issues/2916).
- snap_alias - the output value ``cmd_args`` was bringing the intermediate command used to gather the state, instead of the command that actually performed the state change (https://github.com/ansible-collections/community.general/pull/3655).
- snmp_facts - added support to check mode (https://github.com/ansible-collections/community.general/pull/3084).
- ssh_config - reduce stormssh searches based on host (https://github.com/ansible-collections/community.general/pull/2568/).
- stacki_host - when adding a new server, ``rack`` and ``rank`` must be passed, and network parameters are optional (https://github.com/ansible-collections/community.general/pull/2681).
- stackpath_compute inventory script - fix broken validation checks for client ID and client secret (https://github.com/ansible-collections/community.general/pull/2448).
- supervisorctl - state ``signalled`` was not working (https://github.com/ansible-collections/community.general/pull/3068).
- svr4pkg - convert string to a bytes-like object to avoid ``TypeError`` with Python 3 (https://github.com/ansible-collections/community.general/issues/2373).
- taiga - some constructs in the module fixed to work also in Python 3 (https://github.com/ansible-collections/community.general/pull/3067).
- terraform - ensure the workspace is set back to its previous value when the apply fails (https://github.com/ansible-collections/community.general/pull/2634).
- tss lookup plugin - fixed backwards compatibility issue with ``python-tss-sdk`` version <=0.0.5 (https://github.com/ansible-collections/community.general/issues/3192, https://github.com/ansible-collections/community.general/pull/3199).
- tss lookup plugin - fixed incompatibility with ``python-tss-sdk`` version 1.0.0 (https://github.com/ansible-collections/community.general/issues/3057, https://github.com/ansible-collections/community.general/pull/3139).
- udm_dns_record - fixed managing of PTR records, which can never have worked before (https://github.com/ansible-collections/community.general/pull/3256).
- ufw - use generator to fix sanity errors (https://github.com/ansible-collections/community.general/pull/3194).
- utm_aaa_group_info - added support to check mode (https://github.com/ansible-collections/community.general/pull/3084).
- utm_ca_host_key_cert_info - added support to check mode (https://github.com/ansible-collections/community.general/pull/3084).
- utm_network_interface_address_info - added support to check mode (https://github.com/ansible-collections/community.general/pull/3084).
- utm_proxy_frontend_info - added support to check mode (https://github.com/ansible-collections/community.general/pull/3084).
- utm_proxy_location_info - added support to check mode (https://github.com/ansible-collections/community.general/pull/3084).
- vdo - boolean arguments now compared with proper ``true`` and ``false`` values instead of string representations like ``"yes"`` or ``"no"`` (https://github.com/ansible-collections/community.general/pull/3191).
- xattr - fix exception caused by ``_run_xattr()`` raising a ``ValueError`` due to a mishandling of base64-encoded value (https://github.com/ansible-collections/community.general/issues/3673).
- xenserver_facts - added support to check mode (https://github.com/ansible-collections/community.general/pull/3084).
- xfconf - also use ``LC_ALL`` to enforce locale choice (https://github.com/ansible-collections/community.general/issues/2715).
- xfconf_info - added support to check mode (https://github.com/ansible-collections/community.general/pull/3084).
- yaml callback plugin - avoid modifying PyYAML so that other plugins using it on the controller, like the ``to_yaml`` filter, do not produce different output (https://github.com/ansible-collections/community.general/issues/3471, https://github.com/ansible-collections/community.general/pull/3478).
- yum_versionlock - fix idempotency when using wildcard (asterisk) in ``name`` option (https://github.com/ansible-collections/community.general/issues/2761).
- zfs - certain ZFS properties, especially sizes, would lead to a task being falsely marked as "changed" even when no actual change was made (https://github.com/ansible-collections/community.general/issues/975, https://github.com/ansible-collections/community.general/pull/2454).
- zfs - treated received properties as local (https://github.com/ansible-collections/community.general/pull/502).
- zypper_repository - fix idempotency on adding repository with ``$releasever`` and ``$basearch`` variables (https://github.com/ansible-collections/community.general/issues/1985).
- zypper_repository - when an URL to a .repo file was provided in option ``repo=`` and ``state=present`` only the first run was successful, future runs failed due to missing checks prior starting zypper. Usage of ``state=absent`` in combination with a .repo file was not working either (https://github.com/ansible-collections/community.general/issues/1791, https://github.com/ansible-collections/community.general/issues/3466).

community.grafana
~~~~~~~~~~~~~~~~~

- Fix an issue with datasource uid now returned by the Grafana API (#176)
- Fix issue with trailing '/' in provided grafana_url. The modules now support values with trailing slashes.
- grafana_dashboard lookup - All valid API keys can be used, not just keys ending in '=='.
- grafana_dashboard now explicitely fails if the folder doesn't exist upon creation. It would previously silently pass but not create the dashboard. (https://github.com/ansible-collections/community.grafana/issues/153)
- grafana_team now able to handle spaces and other utf-8 chars in the name parameter. (https://github.com/ansible-collections/community.grafana/issues/164)

community.hashi_vault
~~~~~~~~~~~~~~~~~~~~~

- aws_iam_login auth - the ``aws_security_token`` option was not used, causing assumed role credentials to fail (https://github.com/ansible-collections/community.hashi_vault/issues/160).
- aws_iam_login auth method - fix incorrect use of ``boto3``/``botocore`` that prevented proper loading of AWS IAM role credentials (https://github.com/ansible-collections/community.hashi_vault/issues/167).
- hashi_vault collection - a fallback import supporting the ``retries`` option for ``urllib3`` via ``requests.packages.urllib3`` was not correctly formed (https://github.com/ansible-collections/community.hashi_vault/issues/116).
- hashi_vault collection - unhandled exception with ``token`` auth when ``token_file`` exists but is a directory (https://github.com/ansible-collections/community.hashi_vault/issues/152).

community.libvirt
~~~~~~~~~~~~~~~~~

- libvirt inventory plugin - Use FQCN for the inventory plugin name for compatibility with Ansible 2.10 and above (https://github.com/ansible-collections/community.libvirt/pull/73).

community.mongodb
~~~~~~~~~~~~~~~~~

- 315 - Fix exception handling for mongodb_stepdown module on python3.6
- 320 - Fix exception handling for modules mongodb_balancer, mongodb_shard, and mongodb_status.
- 352 - Add ansible.posix collection to dependencies list.

community.mysql
~~~~~~~~~~~~~~~

- mysql_info - fix TypeError failure when there are databases that do not contain tables (https://github.com/ansible-collections/community.mysql/issues/204).
- mysql_user - Fix crash reporting ``Invalid privileges specified`` when passing privileges that became aliases (https://github.com/ansible-collections/community.mysql/issues/232).

community.okd
~~~~~~~~~~~~~

- fix broken links in Automation Hub for redhat.openshift (https://github.com/openshift/community.okd/issues/100).
- fixes test suite to use correct versions of python and dependencies (https://github.com/ansible-collections/community.okd/pull/89).
- openshift_process - fix module execution when template does not include a message (https://github.com/ansible-collections/community.okd/pull/87).

community.postgresql
~~~~~~~~~~~~~~~~~~~~

- postgresql_ext - Fix extension version handling when it has 0 value (https://github.com/ansible-collections/community.postgresql/issues/136).
- postgresql_info - Fix extension version handling when it has 0 value (https://github.com/ansible-collections/community.postgresql/issues/137).
- postgresql_privs - fix ``fail_on_role`` check (https://github.com/ansible-collections/community.postgresql/pull/82).
- postgresql_set - Fix wrong numerical value conversion (https://github.com/ansible-collections/community.postgresql/issues/110).
- postgresql_slot - Correct the server_version check for PG 9.6 (https://github.com/ansible-collections/community.postgresql/issue/120)

community.proxysql
~~~~~~~~~~~~~~~~~~

- proxysql_query_rules - fix backwards compatibility. Proxysql > 2 does not support parameter ``cache_empty_result`` (https://github.com/ansible-collections/community.proxysql/pull/77).
- proxysql_replication_hostgroups - ability to change ``reader_hostgroup`` (https://github.com/ansible-collections/community.proxysql/pull/69).

community.rabbitmq
~~~~~~~~~~~~~~~~~~

- rabbitmq_policy - The ``_policy_check`` piece of the policy module (``policy_data``) is typically list based on a split of the variable ``policy``. However ``policy`` in some cases does not contain data. The fix allows ``tags`` to attempt to load as json first but in the case of failure, assign ``tags`` without using the json loader (https://github.com/ansible-collections/community.rabbitmq/pull/28).

community.routeros
~~~~~~~~~~~~~~~~~~

- api - improve splitting of ``WHERE`` queries (https://github.com/ansible-collections/community.routeros/pull/47).
- api - when converting result lists to dictionaries, no longer removes second ``=`` and text following that if present (https://github.com/ansible-collections/community.routeros/pull/47).
- api - when using TLS/SSL, remove explicit cipher configuration to insecure values, which also makes it impossible to connect to newer RouterOS versions (https://github.com/ansible-collections/community.routeros/pull/34).
- routeros cliconf plugin - adjust function signature that was modified in Ansible after creation of this plugin (https://github.com/ansible-collections/community.routeros/pull/43).

community.sops
~~~~~~~~~~~~~~

- Fix error handling in calls of the ``sops`` binary when negative errors are returned (https://github.com/ansible-collections/community.sops/issues/82, https://github.com/ansible-collections/community.sops/pull/83).

community.vmware
~~~~~~~~~~~~~~~~

- Fix a bug that prevented enabling VSAN on more than one vmk, risking splitting the whole cluster during interface migration scenarios (https://github.com/ansible-collections/community.vmware/issues/891)
- update_vswitch - add the possibility to remove nics from vswitch (https://github.com/ansible-collections/community.vmware/issues/536)
- vmware - changed to use from isinstance to type in the if condition of option_diff method (https://github.com/ansible-collections/community.vmware/pull/983).
- vmware - fix that the return value should be returned None if moId doesn't exist of a virtual machine (https://github.com/ansible-collections/community.vmware/pull/867).
- vmware - fixed a bug that the guest_guestion in the facts doesn't convert to the dictionary (https://github.com/ansible-collections/community.vmware/pull/825).
- vmware - handle exception raised in ``get_all_objs`` and ``find_object_by_name`` which occurs due to multiple parallel operations (https://github.com/ansible-collections/community.vmware/issues/791).
- vmware_category - fixed some issues that the errors have occurred in executing the module (https://github.com/ansible-collections/community.vmware/pull/990).
- vmware_cluster_info - Fix a bug that returned enabled_vsan and vsan_auto_claim_storage as lists instead of just true or false (https://github.com/ansible-collections/community.vmware/issues/805).
- vmware_content_deploy_ovf_template - no longer requires host, datastore, resource_pool.
- vmware_content_deploy_xxx - deploys to recommended datastore in specified datastore_cluster.
- vmware_content_deploy_xxx - honors folder specified by fully qualified path name.
- vmware_deploy_ovf - Fix deploy ovf issue when there are more than one datacenter in VC (https://github.com/ansible-collections/community.vmware/issues/164).
- vmware_deploy_ovf - fixed to display suitable the error when not exist an ovf file path (https://github.com/ansible-collections/community.vmware/pull/1065).
- vmware_evc_mode - fixed an issue that evc_mode is required when the state parameter set to absent (https://github.com/ansible-collections/community.vmware/pull/764).
- vmware_guest - Use hostname parameter in customization only if value is not None (https://github.com/ansible-collections/community.vmware/issues/655)
- vmware_guest - add message for `deploy_vm` method when it fails with timeout error while customizing the VM (https://github.com/ansible-collections/community.vmware/pull/933).
- vmware_guest - skip customvalues while deploying VM on a standalone ESXi (https://github.com/ansible-collections/community.vmware/issues/721).
- vmware_guest_instant_clone - fixed an issue that the module should be required the guestinfo_vars parameter when executing (https://github.com/ansible-collections/community.vmware/pull/962).
- vmware_guest_network - Fix adding more than one NIC to a VM before powering on (https://github.com/ansible-collections/community.vmware/issues/860).
- vmware_guest_powerstate - added the datacenter parameter to fix an issue that datacenter key error has been occurring (https://github.com/ansible-collections/community.vmware/pull/924).
- vmware_guest_powerstate - handle 'present' state as 'poweredon' (https://github.com/ansible-collections/community.vmware/pull/1033).
- vmware_guest_serial_port - handle correct serial backing type (https://github.com/ansible-collections/community.vmware/issues/1043).
- vmware_guest_tools_wait - add documentation about datacenter parameter (https://github.com/ansible-collections/community.vmware/pull/870).
- vmware_host_datastore - fixed an issue that the right error message isn't displayed (https://github.com/ansible-collections/community.vmware/pull/976).
- vmware_host_iscsi_info - fixed an issue that an error occurs gathering iSCSI information against an ESXi Host with iSCSI disabled (https://github.com/ansible-collections/community.vmware/pull/729).
- vmware_host_lockdown - Fix an issue when enabling or disabling lockdown mode failes (https://github.com/ansible-collections/community.vmware/issues/1083)
- vmware_object_rename - fixed an issue that an error has occurred when getting than 1,000 objects (https://github.com/ansible-collections/community.vmware/pull/1010).
- vmware_vcenter_settings_info - fix to return all VCSA settings when setting vsphere to the schema and not specifying the properties (https://github.com/ansible-collections/community.vmware/pull/1050).
- vmware_vm_info - handle vApp parent logic (https://github.com/ansible-collections/community.vmware/issues/777).
- vmware_vm_inventory - remove erroneous ``ansible_host`` condition (https://github.com/ansible-collections/community.vmware/issues/975).
- vmware_vm_shell - handle exception raised while performing the operation (https://github.com/ansible-collections/community.vmware/issues/732).
- vmware_vm_storage_policy_info - fixed an issue that the module can't get storage policy info when the policy has the tag base rules (https://github.com/ansible-collections/community.vmware/pull/788).
- vmware_vmotion - Provide an meaningful error message when providing a bad ESXi node as ``destination_host`` (https://github.com/ansible-collections/vmware/pull/804).
- vmware_vmotion - implement new parameter named destination_datacenter to fix failure to move storage when datastores are shared across datacenters (https://github.com/ansible-collections/community.vmware/issues/858)

community.windows
~~~~~~~~~~~~~~~~~

- win_audit_rule - Fix exception when trying to change a rule on a hidden or protected system file - https://github.com/ansible-collections/community.windows/issues/17
- win_dns_record - Fix issue when trying to use the ``computer_name`` option - https://github.com/ansible-collections/community.windows/issues/276
- win_dns_zone - Fix idempotency when using a DNS zone with forwarders - https://github.com/ansible-collections/community.windows/issues/259
- win_domain_group_member - Fix faulty logic when comparing existing group members - https://github.com/ansible-collections/community.windows/issues/256
- win_domain_group_membership - Handle timeouts when dealing with group with lots of members - https://github.com/ansible-collections/community.windows/pull/204
- win_domain_user - Fallback to NETBIOS username for password verification check if the UPN is not set - https://github.com/ansible-collections/community.windows/pull/289
- win_domain_user - Make sure a password is set to change when it is marked as password needs to be changed before logging in - https://github.com/ansible-collections/community.windows/issues/223
- win_domain_user - fix reporting on user when running in check mode - https://github.com/ansible-collections/community.windows/pull/248
- win_firewall - Fix GpoBoolean/Boolean comparation(windows versions compatibility increase)
- win_initialize_disk - Ensure ``online: False`` doesn't bring the disk online again - https://github.com/ansible-collections/community.windows/pull/268
- win_lineinfile - Avoid stripping the newline at the end of a file - https://github.com/ansible-collections/community.windows/pull/219
- win_lineinfile - Fix crash when using ``insertbefore`` and ``insertafter`` at the same time - https://github.com/ansible-collections/community.windows/issues/220
- win_lineinfile - Fix up diff output with ending newlines - https://github.com/ansible-collections/community.windows/pull/283
- win_nssm - Perform better user comparison checks for idempotency
- win_partition - Fix gtp_type setting in win_partition - https://github.com/ansible-collections/community.windows/issues/241
- win_product_facts - fixed an issue that the module doesn't correctly convert a product id (https://github.com/ansible-collections/community.windows/pull/251).
- win_psmodule - Makes sure ``-AllowClobber`` is used when updating pre-requisites if requested - https://github.com/ansible-collections/community.windows/issues/42
- win_pssession_configuration - the ``async_poll`` option was not actually used and polling mode was always used with the default poll delay; this change also formally disables ``async_poll=0`` (https://github.com/ansible-collections/community.windows/pull/212).
- win_pssession_configuration - the associated action plugin detects check mode using a method that isn't always accurate (https://github.com/ansible-collections/community.windows/pull/318).
- win_region - Fix ``copy_settings`` on a host that has disabled ``reg.exe`` access - https://github.com/ansible-collections/community.windows/issues/287
- win_region - Fix conflicts with existing ``LIB`` environment variable
- win_scheduled_task - Fix conflicts with existing ``LIB`` environment variable
- win_scheduled_task_stat - Fix conflicts with existing ``LIB`` environment variable
- win_scoop_bucket - Ensure no extra data is sent to the controller resulting in a junk output warning
- win_wait_for_process - Fix bug when specifying multiple ``process_name_exact`` values - https://github.com/ansible-collections/community.windows/issues/203
- win_xml - Do not show warnings for normal operations - https://github.com/ansible-collections/community.windows/issues/205
- win_xml - Fix removal operation when running with higher verbosities - https://github.com/ansible-collections/community.windows/issues/275

community.zabbix
~~~~~~~~~~~~~~~~

- all roles now support installing zabbix 4.0 version on Ubuntu 20.04.
- all roles now supports installations on Debian 11.
- zabbix inventory - Change default value for host_zapi_query from list "[]" to dict "{}".
- zabbix_action - should no longer fail with Zabbix version 5.4.
- zabbix_agent - StatusPort will be configured only when `zabbix_agent2_statusport` is defined (https://github.com/ansible-collections/community.zabbix/pull/378)
- zabbix_agent - `zabbix_win_install_dir` no longer ignored for zabbix_agentd.d and zabbix log directories.
- zabbix_agent - auto-recovery for Windows installation has been fixed (https://github.com/ansible-collections/community.zabbix/pull/470).
- zabbix_agent - deploying zabbix_agent2 under Windows should now be possible (Thanks to https://github.com/ansible-collections/community.zabbix/pull/433 and https://github.com/ansible-collections/community.zabbix/pull/453).
- zabbix_agent - fixed AutoPSK for Windows deployments (https://github.com/ansible-collections/community.zabbix/pull/450).
- zabbix_agent - fixed issue preventing installation of zabbix-agent 4.2 on Ubuntu Focal 20.04 (https://github.com/ansible-collections/community.zabbix/pull/390)
- zabbix_agent - role will now configure correct port for hostinterface in Zabbix Server if `zabbix_agent2_listenport` is defined (https://github.com/ansible-collections/community.zabbix/pull/400)
- zabbix_agent - should no longer be failing on Windows platform due to re-running all of the tasks for the 2nd time (https://github.com/ansible-collections/community.zabbix/pull/376)
- zabbix_agent - should no longer fail while cleaning up zabbix_agent installation if Zabbix Agent2 is being used (https://github.com/ansible-collections/community.zabbix/pull/409)
- zabbix_agent - will no longer install zabbix_get package on Debian systems when `zabbix_agent_install_agent_only` is defined (https://github.com/ansible-collections/community.zabbix/pull/363)
- zabbix_host - Fix error when updating hosts caused by Zabbix bug not returning the inventory_mode field for hosts(https://github.com/ansible-collections/community.zabbix/issues/385).
- zabbix_host - fixed issue where module was idempotent when multiple host interfaces of the same type were present (https://github.com/ansible-collections/community.zabbix/pull/391)
- zabbix_host - will not break when `tls_psk*` parameters are set with Zabbix version 5.4.
- zabbix_proxy (module) - now supports configuring `tls_psk*` parameters.
- zabbix_proxy (role) - TLS config should now properly configure certificates.
- zabbix_proxy (role) - should no longer fail on permission problems wren configured to use SQLite database and now installs correct package sqlite3 on Debian systems.
- zabbix_proxy (role) - will no longer fail on proxy creation in Zabbix Server when TLS parameters are used (https://github.com/ansible-collections/community.zabbix/pull/388)
- zabbix_server - Removed the removal everything from /tmp directory command as it removes things that it shouldnt do.
- zabbix_template - first time import of template now works with Zabbix 5.4 (https://github.com/ansible-collections/community.zabbix/pull/407), please note that rerunning the task will fail as there are breaking changes in Zabbix 5.4 API that module not yet covers.
- zabbix_user - now works with Zabbix 5.4 (https://github.com/ansible-collections/community.zabbix/pull/406)
- zabbix_web - `zabbix_nginx_vhost_*` parameters are no longer ignored.
- zabbix_web - executing role with `--tags` should now correctly include distribution specific variables (https://github.com/ansible-collections/community.zabbix/pull/448).
- zabbix_web - now correctly restarts php-fpm service (https://github.com/ansible-collections/community.zabbix/pull/427).
- zabbix_web - permissions for accesing php-fpm socket has been fixed (See https://github.com/ansible-collections/community.zabbix/pull/426).

containers.podman
~~~~~~~~~~~~~~~~~

- Add .service extension to systemd files
- Add aliases for image load/save
- Add meta/runtime.yml which is required for Galaxy now
- Add option for ansible-core in RPM spec file
- Add skip option for podman secret
- Add support for network-alias flag
- Add support for podman pod create --infra-name
- Allow to actually pass a list of string for "mounts"
- Avoid exposing pipelining support for podman connections
- Change present state to be as created state
- Change python version for ansible-core to 3.9
- Disable no-hosts idempotency
- Don't add newlines to secrets
- Fix ansible-test issues for CI
- Fix failure when listing containers
- Fix idempotency for environment
- Fix idempotency when containers have a common network
- Fix idempotency with systemd podman files
- Fix ipv6=false issue
- Fix issue with podman and exposed ports
- Fix multi-containers options
- Fix overlayfs issue in CI for buildah connection
- Fix signal diff for truncated and RT signal names
- Fix suboption key in podman_container/podman_pod for generate_systemd documentation
- Remove idempotency for volume UID/GID
- Remove idempotency leftovers of volumes GID,UID
- Support empty stings in prefixes
- Update error message when pull set to false

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- Handled invalid share and unused imports cleanup for iDRAC modules (https://github.com/dell/dellemc-openmanage-ansible-modules/issues/268)
- dellemc_idrac_storage_volume - Module fails if the BlockSize, FreeSize, or Size state of the physical disk is set to "Not Available".

f5networks.f5_modules
~~~~~~~~~~~~~~~~~~~~~

- Add fix to iapp service update module
- Add fix to ucs module to cover more scenarios of API instability
- Add negate as3,do,ts,cfe filter for bigip_device_info
- Add syn_cookie_enable parameter to bigip_profile_fastl4 module
- Disable cert validaton for Teem
- Fix API filters not returning correct results when policy names ending with numbers
- Fix a name/address comparison logic when using aggregates in bigip_pool_member
- Fix a regression introduced to aggregate component of bigip_pool_member
- Fix asm policy stats to return complete info in bigip_device_info module
- Fix bigip_device_info with correct attribute "insert_xforwarded_for"
- Fix bigip_gtm_wide_ip to support wildcard type a wide ips
- Fix bigiq non local provider backport from f5_bigip collection
- Fix detaching of attached AFM policy to created route domain
- Fix for Virtual server idempotency with non-common partition.
- Fix for adding sip profile to Virtual server
- Fix for bigip_data_group accepts address object without value
- Fix for bigip_firewall_rule not idempotent when using address_list as source or destination
- Fix for bigip_pool_member aggregate fails to member comparison
- Fix for bigip_software_install module with state activated
- Fix for inactive volume handling issue for bigip_software_install module
- Fix ignoring of partition parameter when creating external datagroups
- Fix imish config issue where last character is chopped off by adding extra space to commands
- Fix incorrect duplication of entries when creating new ACLs
- Fix index out of range error when comparing user and device's ACLs
- Fix issue in bigip_firewall_dos_policy where in TMOS v15 and above creating dos vector containers requires additional step in the API
- Fix issue in bigip_gtm_topology_region where parameter region_members being set to empty list returned an error
- Fix issue in bigip_pool_member with module idempotency when pool member status was fqdn-down
- Fix issue where bigip_firewall_port_list was failing when removing objects (#1988)
- Fix issue where empty irules property on device would throw exception during comparison
- Fix issue where viprion platrform interfaces interface naming scheme prevented the use of module
- Fix issue with new telemetry environment variable not populated in provider
- Fix issue with send_teem function ignoring environment variable
- Fix ltm policy conditions to return complete data in bigip_device_info module
- Fix query filters in bigip_asm_* modules to allow policy names subsets
- Fix snat pool issue in device info module
- Fix teem call when bigip_command and bigip_wait modules are using CLI as transport
- Fix teem version in constants.py
- Fix validation function for bigip_virtual_server module to include new api endpoints for checking SIP profiles
- Fix various minor regressions and improved functional testing in collection
- Include serialNumber for ssl-certs gather_subset
- Remove type str for datagroups as we are not supporting it.
- fix destination re in bigip_device_info misses shared partition.
- fix to allow tcp condition with asm_enable action

fortinet.fortios
~~~~~~~~~~~~~~~~

- Disable check_mode feature from all global objects of configuration modules due to 'state' issue.
- Fix Github issue
- Fix a bug in IP_PREFIX.match().
- Fix a regression bug caused by non-required attributes.
- Fix an intentional exception for listed options.
- Fix the KeyError caused by non-required multi-value attributes in an object.
- Fix the authorization fails at log in with username and password in FOS7.0.
- Fix the corner cases that response does not have status in it.
- Fix the filters error when fetching multiple facts with selectors for a configuration module (Github issue
- Fix the issue that the ``server_type`` is not updated in ``fortios_system_central_management``.
- Fix the unexpected warning caused by optinal params in ``fortios_monitor_fact`` and ``fortios_monitor``.
- Github Issue 103
- Github Issue 105

hetzner.hcloud
~~~~~~~~~~~~~~

- hcloud_rdns improve error message on not existing server/Floating IP
- hcloud_server Improve Error Message when attaching a not existing firewall to a server
- hcloud_server backups property defaults to None now instead of False
- hcloud_volume Force detaching of volumes on servers before deletion

junipernetworks.junos
~~~~~~~~~~~~~~~~~~~~~

- fix lacp force-up without port-priority in junos_lacp_interfaces
- fix netconf test-case for lacp revert
- junos_acls failed to parse acl when multiple addresses defined within a single term (https://github.com/ansible-collections/junipernetworks.junos/issues/190)

kubernetes.core
~~~~~~~~~~~~~~~

- Fix apply for k8s module when an array attribute from definition contains empty dict (https://github.com/ansible-collections/kubernetes.core/issues/113).
- check auth params for existence, not whether they are true (https://github.com/ansible-collections/kubernetes.core/pull/151).
- common - Ensure the label_selectors parameter of _wait_for method is optional.
- common - import k8sdynamicclient directly to workaround Ansible upstream bug (https://github.com/ansible-collections/kubernetes.core/issues/162).
- connection plugin - add arguments information into censored command (https://github.com/ansible-collections/kubernetes.core/pull/196).
- enable unit tests in CI (https://github.com/ansible-collections/community.kubernetes/pull/407).
- fix resource cache not being used (https://github.com/ansible-collections/kubernetes.core/pull/228).
- helm - Accept ``validate_certs`` with a ``context`` (https://github.com/ansible-collections/kubernetes.core/pull/74).
- helm - fix helm ignoring the kubeconfig context when passed through the ``context`` param or the ``K8S_AUTH_CONTEXT`` environment variable (https://github.com/ansible-collections/community.kubernetes/issues/385).
- helm - handle multiline output of ``helm plugin list`` command (https://github.com/ansible-collections/community.kubernetes/issues/399).
- inventory - add community.kubernetes to list of plugin choices in k8s inventory (https://github.com/ansible-collections/kubernetes.core/pull/128).
- k8s - Fixes a bug where diff was always returned when using apply or modifying an existing object, even when diff=no was specified. The module no longer returns diff unless requested and will now honor diff=no (https://github.com/ansible-collections/kubernetes.core/pull/146).
- k8s - fix merge_type option when set to json (https://github.com/ansible-collections/kubernetes.core/issues/54).
- k8s - lookup should return list even if single item is found (https://github.com/ansible-collections/kubernetes.core/issues/9).
- k8s inventory - remove extra trailing slashes from the hostname (https://github.com/ansible-collections/kubernetes.core/issues/52).
- k8s_cp - fix k8s_cp uploading when target container's WORKDIR is not '/' (https://github.com/ansible-collections/kubernetes.core/issues/222).
- k8s_exec - add missing deprecation notice to return_code for k8s_exec (https://github.com/ansible-collections/kubernetes.core/pull/233).
- k8s_exec - fix k8s_exec returning rc attribute,  to follow ansible's common return values (https://github.com/ansible-collections/kubernetes.core/pull/230).
- lookup - recommend query instead of lookup (https://github.com/ansible-collections/kubernetes.core/issues/147).
- rename the apply function to fix broken imports in Ansible 2.9 (https://github.com/ansible-collections/kubernetes.core/pull/135).
- support the ``template`` param in all collections depending on kubernetes.core (https://github.com/ansible-collections/kubernetes.core/pull/154).

netapp.aws
~~~~~~~~~~

- all modules - fix traceback TypeError 'NoneType' object is not subscriptable when URL points to a web server.

netapp.azure
~~~~~~~~~~~~

- Hub Automation cannot generate documentation (cannot use doc fragments from another collection).
- azure_rm_netapp_volume - 'Change Ownership' is not permitted when creating NFSv4.1 volume with latest azure-mgmt-netapp package (4.0.0).
- fix CI pipeline as azcollection does not support python 2.6.
- fix CI pipeline as ignores are not required with latest azcollection.
- fix CI pipeline to work with azcollection, and isolate UTs from azcollection.

netapp.cloudmanager
~~~~~~~~~~~~~~~~~~~

- Fix cannot find working environment if ``working_environment_name`` is provided
- na_cloudmanager_aggregate - Improve error message
- na_cloudmanager_aggregate - accept client_id end with or without 'clients'
- na_cloudmanager_cifs_server - Fix incorrect API call when is_workgroup is true
- na_cloudmanager_cifs_server - accept client_id end with or without 'clients'
- na_cloudmanager_connector_aws - accept client_id end with or without 'clients'
- na_cloudmanager_connector_azure - Add subnet_name as aliases of subnet_id, vnet_name as aliases of vnet_id.
- na_cloudmanager_connector_azure - Change client_id as optional
- na_cloudmanager_connector_azure - Fix KeyError client_id
- na_cloudmanager_connector_azure - Fix python error - msrest.exceptions.ValidationError. Parameter 'Deployment.properties' can not be None.
- na_cloudmanager_connector_azure - Fix wrong example on the document and update account_id is required field on deletion.
- na_cloudmanager_connector_azure - accept client_id end with or without 'clients'
- na_cloudmanager_connector_gcp - accept client_id end with or without 'clients'
- na_cloudmanager_connector_gcp - typeError when using proxy certificates.
- na_cloudmanager_cvo_aws - accept client_id end with or without 'clients'
- na_cloudmanager_cvo_azure - accept client_id end with or without 'clients'
- na_cloudmanager_cvo_gcp - Apply network_project_id check on vpc1_cluster_connectivity, vpc2_ha_connectivity, vpc3_data_replication, subnet1_cluster_connectivity, subnet2_ha_connectivity, subnet3_data_replication
- na_cloudmanager_cvo_gcp - Change vpc_id from optional to required.
- na_cloudmanager_cvo_gcp - accept client_id end with or without 'clients'
- na_cloudmanager_info - accept client_id end with or without 'clients'
- na_cloudmanager_nss_account - Improve error message
- na_cloudmanager_nss_account - accept client_id end with or without 'clients'
- na_cloudmanager_snapmirror - accept client_id end with or without 'clients'
- na_cloudmanager_snapmirror - key error CloudProviderName for ONPREM operation
- na_cloudmanager_volume - Improve error message
- na_cloudmanager_volume - accept client_id end with or without 'clients'

netapp.elementsw
~~~~~~~~~~~~~~~~

- requirements.txt - point to the correct python dependency

netapp.ontap
~~~~~~~~~~~~

- all REST modules - 9.4 and 9.5 were incorrectly detected as supporting REST.
- all modules - fix traceback TypeError 'NoneType' object is not subscriptable when hostname points to a web server.
- all modules - traceback on ONTAP 9.3 (and earlier) when trying to detect REST support.
- cluster scoped modules are failing on FSx with 'Vserver API missing vserver parameter' error.
- na_ontap_autosupport - KeyError - No element by given name validate-digital-certificate.
- na_ontap_autosupport - TypeError - '>' not supported between instances of 'str' and 'list'.
- na_ontap_cluster - ``single_node_cluster`` was silently ignored with REST.
- na_ontap_cluster - switch to ZAPI when DELETE is required with ONTAP 9.6.
- na_ontap_cluster_peer - KeyError on dest_cluster_name if destination is unreachable.
- na_ontap_cluster_peer - KeyError on username when using certicate.
- na_ontap_export_policy_rule - change ``anonymous_user_id`` type to str to accept user name and user id.   (A warning is now triggered when a number is not quoted.)
- na_ontap_flexcache - one occurrence of msg missing in call to fail_json.
- na_ontap_igroup - one occurrence of msg missing in call to fail_json.
- na_ontap_igroups - nested igroups are not supported on ONTAP 9.9.0 but are on 9.9.1.
- na_ontap_iscsi_security - IndexError list index out of range if vserver does not exist
- na_ontap_iscsi_security - cannot change authentication_type
- na_ontap_job_schedule - cannot modify options not present in create when using REST.
- na_ontap_job_schedule - fix documentation for REST ranges for months.
- na_ontap_job_schedule - fix idempotency issue with REST when job_minutes is set to -1.
- na_ontap_job_schedule - fix idempotency issue with ZAPI when job_minutes is set to -1.
- na_ontap_job_schedule - modify error if month is changed from some values to all (-1) when using REST.
- na_ontap_job_schedule - modify error if month is present but not changed with 0 offset when using REST.
- na_ontap_ldap_client - remove limitation on schema so that custom schemas can be used.
- na_ontap_lun - three occurrencse of msg missing in call to fail_json.
- na_ontap_lun_map_reporting_nodes - one occurrence of msg missing in call to fail_json.
- na_ontap_object_store - when using REST, wait for job status to correctly report errors.
- na_ontap_quotas - attempt to retry on ``13001:success`` ZAPI error.  Add debug data.
- na_ontap_quotas - fail to reinitialize on create if quota is already on.
- na_ontap_rest_cli - removed incorrect statement indicating that console access is required.
- na_ontap_snapmirror - ``source_path`` and ``source_hostname`` parameters are not mandatory to delete snapmirror relationship when source cluster is unknown, if specified it will delete snapmirror at destination and release the same at source side.  if not, it only deletes the snapmirror at destination and will not look for source to perform snapmirror release.
- na_ontap_snapmirror - improve error message when option is not supported with ZAPI.
- na_ontap_snapmirror - modify policy, schedule and other parameter failure are fixed.
- na_ontap_snapmirror - one occurrence of msg missing in call to fail_json.
- na_ontap_snapshot - ``expiry_time`` required REST api, will return error if set when using ZAPI.
- na_ontap_snapshot - ``snapmirror_label`` is supported with REST on ONTAP 9.7 or higher, report error if used on ONTAP 9.6.
- na_ontap_storage_failover - KeyError on 'ha' if the system is not configured as HA.
- na_ontap_svm - module will on init if a rest only and zapi only option are used at the same time.
- na_ontap_volume_clone - ``parent_vserver`` can not be given with ``junction_path``, ``uid``, or ``gid``
- na_ontap_vserver_delete role - delete iSCSI igroups and CIFS server before deleting vserver.
- na_ontap_vserver_delete role - fix typos for cifs.
- na_ontap_vserver_peer - KeyError on username when using certicate.

netapp.um_info
~~~~~~~~~~~~~~

- all modules - report error when connecting to a server that does not run AIQUM.
- all modules - return all records rather than the first 1000 records (mostly for volumes).
- rename na_um_list_volumes.p to na_um_list_volumes.py

netapp_eseries.santricity
~~~~~~~~~~~~~~~~~~~~~~~~~

- Fix PEM certificate/key imports in the na_santricity_server_certificate module.
- Fix availability of client certificate change.
- Fix host and host port names from being changed to lower case.
- Fix login banner message option bytes error in na_santricity_global.
- Fix missing proxy client and server certificate in management role.
- Fix missing proxy validate_certs and change current proxy password variables.
- Fix na_santricity_mgmt_interface IPv4 and IPv6 form validation.
- Fix pkcs8 private key passphrase issue.
- Fix server certificate module not forwarding certificate imports to the embedded web services.
- Fix storage system admin password change from web services proxy in na_santricity_auth module.

netbox.netbox
~~~~~~~~~~~~~

- Allow ``virtual_chassis`` to be found via name [#402](https://github.com/netbox-community/ansible_modules/issues/402)
- Copy interfaces before processing [#556](https://github.com/netbox-community/ansible_modules/pull/556)
- Fix mapping between power_outlet_template and power_port_template.
- Inventory - Update plugin to support location for NetBox 2.11+ [#510](https://github.com/netbox-community/ansible_modules/pull/510)
- Make attached_ips subscriptable. [#609](https://github.com/netbox-community/ansible_modules/pull/609)
- inventory - Fix rack-group -> location for NetBox 2.11 changes.
- inventory - Properly handle interface tags.
- netbox_tenant - Fix example to match argspec.

ngine_io.cloudstack
~~~~~~~~~~~~~~~~~~~

- cs_instance - Fixed attribute error in custom service offerings handling (https://github.com/ngine-io/ansible-collection-cloudstack/pull/87).
- cs_instance - Fixed custom service offerings usage (https://github.com/ngine-io/ansible-collection-cloudstack/issues/79).
- cs_instance - Fixed missing project ID to volume query when checking root disk size. (https://github.com/ngine-io/ansible-collection-cloudstack/pull/90).

openvswitch.openvswitch
~~~~~~~~~~~~~~~~~~~~~~~

- `openvswitch_bridge` - Fix idempotency for VLAN bridges

ovirt.ovirt
~~~~~~~~~~~

- hosted_engine_setup - Filter VLAN devices with bad names (https://github.com/oVirt/ovirt-ansible-collection/pull/238)
- hosted_engine_setup - Remove cloud-init configuration (https://github.com/oVirt/ovirt-ansible-collection/pull/295).
- hosted_engine_setup - Use default bridge for IPv6 advertisements (https://github.com/oVirt/ovirt-ansible-collection/pull/331)
- hosted_engine_setup - Use forward network during an IPv6 deployment (https://github.com/oVirt/ovirt-ansible-collection/pull/315)
- hosted_engine_setup - Use ovirt_host module to discover iscsi (https://github.com/oVirt/ovirt-ansible-collection/pull/275).
- hosted_engine_setup - align with ansible-lint 5.0.0 (https://github.com/oVirt/ovirt-ansible-collection/pull/271).
- hosted_engine_setup - remove duplicate tasks (https://github.com/oVirt/ovirt-ansible-collection/pull/314)
- image_template - Remove static no - unsupported in ansible 2.12 (https://github.com/oVirt/ovirt-ansible-collection/pull/341).
- ovirt inventory plugin - allow several valid values for the `plugin` key (https://github.com/oVirt/ovirt-ansible-collection/pull/293).
- ovirt_auth - Fix password and username requirements (https://github.com/oVirt/ovirt-ansible-collection/pull/325).
- ovirt_auth - Fix token no_log (https://github.com/oVirt/ovirt-ansible-collection/pull/332).
- ovirt_disk - Fix update_check with no VM (https://github.com/oVirt/ovirt-ansible-collection/pull/323).
- ovirt_permission - fix group search that has space in it's name (https://github.com/oVirt/ovirt-ansible-collection/pull/318)

purestorage.flasharray
~~~~~~~~~~~~~~~~~~~~~~

- purefa_host - Rollback host creation if initiators already used by another host
- purefa_policy - Fix incorrect protocol endpoint invocation
- purefa_ra - fix disable feature for remote assist, this didn't work due to error in check logic
- purefa_subnet - Add regex to check for correct dsubnet name
- purefa_user - Add regex to check for correct username
- purefa_vg - Correct issue when setting or changing Volume Group QoS
- purefa_volume - Fix incorrect API version check for ActiveDR support

purestorage.flashblade
~~~~~~~~~~~~~~~~~~~~~~

- purefb_fs - Fix bug where changing the state of both NFS v3 and v4.1 at the same time ignored one of these.
- purefb_s3acc - Ensure S3 Account Name is always lowercase
- purefb_s3user - Ensure S3 Account Name is always lowercase
- purefb_subnet - Allow subnet creation with no gateway

servicenow.servicenow
~~~~~~~~~~~~~~~~~~~~~

- makes auth backwards compatible by defaulting to OAuth if client_id is present without specifying auth
- order_by again working by locally sorting return list of records

t_systems_mms.icinga_director
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Changed place in the creation order of service object in ansible_icinga role (https://github.com/T-Systems-MMS/ansible-collection-icinga-director/pull/135)

theforeman.foreman
~~~~~~~~~~~~~~~~~~

- activation_key - submit organization_id when querying subs, required for Katello 4.1
- content_view_version_cleanup - sort content view versions before deleting (https://github.com/RedHatSatellite/satellite-ansible-collection/issues/30, https://bugzilla.redhat.com/show_bug.cgi?id=1980274)
- content_view_version_cleanup role - properly clean up when users set keep=0 (https://bugzilla.redhat.com/show_bug.cgi?id=1974314)
- external_usergroup - always lookup the ID of the usergroup, instead of passing the name to the API (https://bugzilla.redhat.com/show_bug.cgi?id=1967649)
- host - pass the right image id to the compute resource when creating a host (https://github.com/theforeman/foreman-ansible-modules/issues/1160, https://bugzilla.redhat.com/show_bug.cgi?id=1911670)
- host, compute_profile - when resolving cluster and other values in vm_attrs, compare them as strings (https://github.com/theforeman/foreman-ansible-modules/issues/1245)
- host, hostgroup - don't accidentally duplicate ``kt_activation_keys`` param (https://github.com/theforeman/foreman-ansible-modules/issues/1268)
- host, hostgroup - don't override already set parameters when passing an activation key only (and vice versa) (https://bugzilla.redhat.com/show_bug.cgi?id=1967904)
- subscription_info - mark ``organization`` parameter as required, to match Katello

vyos.vyos
~~~~~~~~~

- Fix KeyError 'source' - vyos_firewall_rules
- Fix vyos_firewall_rules with state replaced to only replace the specified rules.
- Updated docs resolving spelling typos
- change admin_distance to distance while generating static_routes nexthop command.
- change interface to next-hop-interface while generating static_routes nexthop command.
- firewall_global - port-groups were not added (https://github.com/ansible-collections/vyos.vyos/issues/107)
- fix issue in firewall rules facts code when IPV6 ICMP type name in vyos.vyos.vyos_firewall_rules is not idempotent
- fix issue in route-maps facts code when route-maps facts are empty.

Known Issues
------------

Ansible-core
~~~~~~~~~~~~

- ansible-test - Tab completion anywhere other than the end of the command with the new composite options will provide incorrect results. See https://github.com/kislyuk/argcomplete/issues/351 for additional details.

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- idrac_user - Issue(192043) Module may error out with the message ``unable to perform the import or export operation because there are pending attribute changes or a configuration job is in progress``. Wait for the job to complete and run the task again.
- ome_device_power_settings - Issue(212679) The ome_device_power_settings module errors out with the following message if the value provided for the parameter ``power_cap`` is not within the supported range of 0 to 32767, ``Unable to complete the request because PowerCap does not  exist or is not applicable for the resource URI.``
- ome_smart_fabric_uplink - Issue(186024) ome_smart_fabric_uplink module does not allow the creation of multiple uplinks of the same name even though it is supported by OpenManage Enterprise Modular. If an uplink is created using the same name as an existing uplink, the existing uplink is modified.
- ome_smart_fabric_uplink - Issue(186024) ome_smart_fabric_uplink module does not allow the creation of multiple uplinks of the same name even though this is supported by OpenManage Enterprise Modular. If an uplink is created using the same name as an existing uplink, the existing uplink is modified.

purestorage.flashblade
~~~~~~~~~~~~~~~~~~~~~~

- purefb_lag - The mac_address field in the response is not populated. This will be fixed in a future FlashBlade update.

New Plugins
-----------

Callback
~~~~~~~~

- community.general.elastic - Create distributed traces for each Ansible task in Elastic APM
- community.general.opentelemetry - Create distributed traces with OpenTelemetry

Connection
~~~~~~~~~~

- community.docker.nsenter - execute on host running controller container

Filter
~~~~~~

- community.general.groupby_as_dict - Transform a sequence of dictionaries to a dictionary where the dictionaries are indexed by an attribute
- community.general.unicode_normalize - Normalizes unicode strings to facilitate comparison of characters with normalized forms
- community.routeros.join - Join a list of arguments to a command
- community.routeros.list_to_dict - Convert a list of arguments to a list of dictionary
- community.routeros.quote_argument - Quote an argument
- community.routeros.quote_argument_value - Quote an argument value
- community.routeros.split - Split a command into arguments
- community.sops.decrypt - Decrypt sops-encrypted data

Httpapi
~~~~~~~

- cisco.mso.mso - MSO Ansible HTTPAPI Plugin.

Inventory
~~~~~~~~~

- community.general.icinga2 - Icinga2 inventory source
- community.general.opennebula - OpenNebula inventory source
- community.vmware.vmware_host_inventory - VMware ESXi hostsystem inventory source
- community.zabbix.zabbix_inventory - Zabbix Inventory Plugin

Lookup
~~~~~~

- community.general.collection_version - Retrieves the version of an installed collection
- community.general.dependent - Composes a list with nested elements of other lists or dicts which can depend on previous loop variables
- community.general.random_pet - Generates random pet names
- community.general.random_string - Generates random string
- community.general.random_words - Return a number of random words
- community.hashi_vault.vault_read - Perform a read operation against HashiCorp Vault
- kubernetes.core.kustomize - Build a set of kubernetes resources using a 'kustomization.yaml' file.

Netconf
~~~~~~~

- cisco.nxos.nxos - Use nxos netconf plugin to run netconf commands on Cisco NX-OS platform.

Test
~~~~

- community.general.a_module - Check whether the given string refers to an available module or action plugin

New Modules
-----------

amazon.aws
~~~~~~~~~~

- amazon.aws.ec2_spot_instance - request, stop, reboot or cancel spot instance
- amazon.aws.ec2_spot_instance_info - Gather information about ec2 spot instance requests

ansible.netcommon
~~~~~~~~~~~~~~~~~

- ansible.netcommon.network_resource - Manage resource modules

arista.eos
~~~~~~~~~~

- arista.eos.eos_logging_global - Manages logging resource module
- arista.eos.eos_ntp_global - Manages ntp resource module
- arista.eos.eos_prefix_lists - Manages Prefix lists resource module

cisco.ios
~~~~~~~~~

- cisco.ios.ios_logging_global - Logging resource module.
- cisco.ios.ios_ntp_global - ntp_global resource module
- cisco.ios.ios_prefix_lists - Prefix Lists resource module.
- cisco.ios.ios_route_maps - Route Maps resource module.

cisco.iosxr
~~~~~~~~~~~

- cisco.iosxr.iosxr_logging_global - Manages logging attributes of Cisco IOSXR network devices
- cisco.iosxr.iosxr_prefix_lists - Prefix-Lists resource module.

cisco.nxos
~~~~~~~~~~

- cisco.nxos.nxos_logging_global - Logging resource module.
- cisco.nxos.nxos_ntp_global - NTP Global resource module.
- cisco.nxos.nxos_prefix_lists - Prefix-Lists resource module.

cloudscale_ch.cloud
~~~~~~~~~~~~~~~~~~~

- cloudscale_ch.cloud.custom_image - Manage custom images on the cloudscale.ch IaaS service

community.aws
~~~~~~~~~~~~~

- community.aws.aws_msk_cluster - Manage Amazon MSK clusters.
- community.aws.aws_msk_config - Manage Amazon MSK cluster configurations.
- community.aws.efs_tag - create and remove tags on Amazon EFS resources
- community.aws.iam_access_key - Manage AWS IAM User access keys
- community.aws.iam_access_key_info - fetch information about AWS IAM User access keys
- community.aws.rds_option_group - rds_option_group module
- community.aws.rds_option_group_info - rds_option_group_info module

community.crypto
~~~~~~~~~~~~~~~~

- community.crypto.openssl_publickey_info - Provide information for OpenSSL public keys

community.digitalocean
~~~~~~~~~~~~~~~~~~~~~~

- community.digitalocean.digital_ocean_balance_info - Display DigitalOcean customer balance
- community.digitalocean.digital_ocean_cdn_endpoints - Create and delete DigitalOcean CDN Endpoints
- community.digitalocean.digital_ocean_cdn_endpoints_info - Gather information about DigitalOcean CDN Endpoints
- community.digitalocean.digital_ocean_database - Create and delete a DigitalOcean database
- community.digitalocean.digital_ocean_database_info - Gather information about DigitalOcean databases
- community.digitalocean.digital_ocean_droplet_info - Gather information about DigitalOcean Droplets
- community.digitalocean.digital_ocean_kubernetes - Create and delete a DigitalOcean Kubernetes cluster
- community.digitalocean.digital_ocean_kubernetes_info - Returns information about an existing DigitalOcean Kubernetes cluster
- community.digitalocean.digital_ocean_load_balancer - Manage DigitalOcean Load Balancers
- community.digitalocean.digital_ocean_monitoring_alerts - Create and delete DigitalOcean Monitoring alerts
- community.digitalocean.digital_ocean_monitoring_alerts_info - Gather information about DigitalOcean Monitoring alerts
- community.digitalocean.digital_ocean_project - Manage a DigitalOcean project
- community.digitalocean.digital_ocean_project_info - Gather information about DigitalOcean Projects
- community.digitalocean.digital_ocean_snapshot - Create and delete DigitalOcean snapshots
- community.digitalocean.digital_ocean_vpc - Create and delete DigitalOcean VPCs
- community.digitalocean.digital_ocean_vpc_info - Gather information about DigitalOcean VPCs

community.general
~~~~~~~~~~~~~~~~~

Cloud
^^^^^

Misc
....

- community.general.proxmox_nic - Management of a NIC of a Qemu(KVM) VM in a Proxmox VE cluster.
- community.general.proxmox_tasks_info - Retrieve information about one or more Proxmox VE tasks

Database
^^^^^^^^

Misc
....

- community.general.redis_data - Set key value pairs in Redis
- community.general.redis_data_incr - Increment keys in Redis
- community.general.redis_data_info - Get value of key in Redis database

Mssql
.....

- community.general.mssql_script - Execute SQL scripts on a MSSQL database

Saphana
.......

- community.general.hana_query - Execute SQL on HANA

Files
^^^^^

- community.general.sapcar_extract - Manages SAP SAPCAR archives

Identity
^^^^^^^^

Keycloak
........

- community.general.keycloak_authentication - Configure authentication in Keycloak
- community.general.keycloak_client_rolemapping - Allows administration of Keycloak client_rolemapping with the Keycloak API
- community.general.keycloak_clientscope - Allows administration of Keycloak client_scopes via Keycloak API
- community.general.keycloak_identity_provider - Allows administration of Keycloak identity providers via Keycloak API
- community.general.keycloak_role - Allows administration of Keycloak roles via Keycloak API
- community.general.keycloak_user_federation - Allows administration of Keycloak user federations via Keycloak API

Notification
^^^^^^^^^^^^

- community.general.discord - Send Discord messages

Packaging
^^^^^^^^^

Language
........

- community.general.ansible_galaxy_install - Install Ansible roles or collections using ansible-galaxy
- community.general.pipx - Manages applications installed with pipx

Os
..

- community.general.dnf_versionlock - Locks package versions in C(dnf) based systems
- community.general.pacman_key - Manage pacman's list of trusted keys
- community.general.snap_alias - Manages snap aliases

Source Control
^^^^^^^^^^^^^^

Gitlab
......

- community.general.gitlab_protected_branch - (un)Marking existing branches for protection

System
^^^^^^

- community.general.sap_task_list_execute - Perform SAP Task list execution
- community.general.xfconf_info - Retrieve XFCE4 configurations

Web Infrastructure
^^^^^^^^^^^^^^^^^^

- community.general.rundeck_job_executions_info - Query executions for a Rundeck job
- community.general.rundeck_job_run - Run a Rundeck job

community.hashi_vault
~~~~~~~~~~~~~~~~~~~~~

- community.hashi_vault.vault_read - Perform a read operation against HashiCorp Vault

community.hrobot
~~~~~~~~~~~~~~~~

- community.hrobot.boot - Set boot configuration
- community.hrobot.reset - Reset a dedicated server
- community.hrobot.reverse_dns - Set or remove reverse DNS entry for IP
- community.hrobot.server - Update server information
- community.hrobot.server_info - Query information on one or more servers
- community.hrobot.ssh_key - Add, remove or update SSH key
- community.hrobot.ssh_key_info - Query information on SSH keys

community.mongodb
~~~~~~~~~~~~~~~~~

- community.mongodb.mongodb_monitoring - Manages the free monitoring feature.
- community.mongodb.mongodb_schema - Manages MongoDB Document Schema Validators.
- community.mongodb.mongodb_shard_tag - Manage Shard Tags.
- community.mongodb.mongodb_shard_zone - Manage Shard Zones.

community.mysql
~~~~~~~~~~~~~~~

- community.mysql.mysql_role - Adds, removes, or updates a MySQL role

community.proxysql
~~~~~~~~~~~~~~~~~~

- community.proxysql.proxysql_info - Gathers information about proxysql server
- community.proxysql.proxysql_query_rules_fast_routing - Modifies query rules for fast routing policies using the proxysql admin interface

community.rabbitmq
~~~~~~~~~~~~~~~~~~

- community.rabbitmq.rabbitmq_feature_flag - Enables feature flag
- community.rabbitmq.rabbitmq_upgrade - Execute rabbitmq-upgrade commands
- community.rabbitmq.rabbitmq_user_limits - Manage RabbitMQ user limits

community.vmware
~~~~~~~~~~~~~~~~

- community.vmware.vmware_guest_tpm - Add or remove vTPM device for specified VM.
- community.vmware.vmware_host_custom_attributes - Manage custom attributes from VMware for the given ESXi host
- community.vmware.vmware_host_passthrough - Manage PCI device passthrough settings on host
- community.vmware.vmware_host_tcpip_stacks - Manage the TCP/IP Stacks configuration of ESXi host
- community.vmware.vmware_object_custom_attributes_info - Gather custom attributes of an object
- community.vmware.vmware_object_role_permission_info - Gather information about object's permissions
- community.vmware.vmware_recommended_datastore - Returns the recommended datastore from a SDRS-enabled datastore cluster
- community.vmware.vmware_vm_config_option - Return supported guest ID list and VM recommended config option for specific guest OS

community.windows
~~~~~~~~~~~~~~~~~

- community.windows.win_domain_ou - Manage Active Directory Organizational Units
- community.windows.win_feature_info - Gather information about Windows features

community.zabbix
~~~~~~~~~~~~~~~~

- community.zabbix.zabbix_globalmacro - Create/update/delete Zabbix Global macros
- community.zabbix.zabbix_proxy_info - Gather information about Zabbix proxy

containers.podman
~~~~~~~~~~~~~~~~~

- containers.podman.podman_export - Export a podman container to tar file
- containers.podman.podman_import - Import Podman container from a tar file
- containers.podman.podman_load - Load image from a tar file
- containers.podman.podman_play - Play Kubernetes YAML files with Podman
- containers.podman.podman_save - Saves podman image to tar file
- containers.podman.podman_secret - Manage podman secrets

dellemc.enterprise_sonic
~~~~~~~~~~~~~~~~~~~~~~~~

- dellemc.enterprise_sonic.sonic_aaa - AAA resource module.
- dellemc.enterprise_sonic.sonic_radius_server - RADIUS resource module.
- dellemc.enterprise_sonic.sonic_system - SYSTEM resource module.
- dellemc.enterprise_sonic.sonic_tacacs_server - TACACS Server resource module.

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- dellemc.openmanage.ome_active_directory - Configure Active Directory groups to be used with Directory Services on OpenManage Enterprise and OpenManage Enterprise Modular
- dellemc.openmanage.ome_chassis_slots - Rename sled slots on OpenManage Enterprise Modular
- dellemc.openmanage.ome_device_location - Configure device location settings on OpenManage Enterprise Modular
- dellemc.openmanage.ome_device_mgmt_network - Configure network settings of devices on OpenManage Enterprise Modular
- dellemc.openmanage.ome_device_power_settings - Configure chassis power settings on OpenManage Enterprise Modular
- dellemc.openmanage.ome_diagnostics - Export technical support logs(TSR) to network share location
- dellemc.openmanage.ome_domain_user_groups - Create, modify, or delete an Active Directory user group on OpenManage Enterprise and OpenManage Enterprise Modular
- dellemc.openmanage.ome_groups - Manages static device groups on OpenManage Enterprise
- dellemc.openmanage.redfish_event_subscription - Manage Redfish Subscriptions

junipernetworks.junos
~~~~~~~~~~~~~~~~~~~~~

- junipernetworks.junos.junos_logging_global - Manage logging configuration on Junos devices.
- junipernetworks.junos.junos_ntp_global - Manage NTP configuration on Junos devices.

kubernetes.core
~~~~~~~~~~~~~~~

- kubernetes.core.k8s_cp - Copy files and directories to and from pod.
- kubernetes.core.k8s_drain - Drain, Cordon, or Uncordon node in k8s cluster
- kubernetes.core.k8s_json_patch - Apply JSON patch operations to existing objects

netapp.cloudmanager
~~~~~~~~~~~~~~~~~~~

- netapp.cloudmanager.na_cloudmanager_snapmirror - NetApp Cloud Manager SnapMirror

netapp.ontap
~~~~~~~~~~~~

- netapp.ontap.na_ontap_cifs_local_user_set_password - NetApp ONTAP set local CIFS user password
- netapp.ontap.na_ontap_fdsd - NetApp ONTAP create or remove a File Directory security descriptor.
- netapp.ontap.na_ontap_fdsp - NetApp ONTAP create or delete a file directory security policy
- netapp.ontap.na_ontap_fdspt - NetApp ONTAP create, delete or modify File Directory security policy tasks
- netapp.ontap.na_ontap_fdss - NetApp ONTAP File Directory Security Set.
- netapp.ontap.na_ontap_partitions - NetApp ONTAP Assign partitions and disks to nodes.
- netapp.ontap.na_ontap_publickey - NetApp ONTAP publickey configuration
- netapp.ontap.na_ontap_service_policy - NetApp ONTAP service policy configuration

netbox.netbox
~~~~~~~~~~~~~

- netbox.netbox.netbox_config_context - Create, update or delete Config Context in NetBox
- netbox.netbox.netbox_location - Create, update or delete Location in NetBox
- netbox.netbox.netbox_site_group - Create, update or delete Site Group in NetBox

purestorage.flasharray
~~~~~~~~~~~~~~~~~~~~~~

- purestorage.flasharray.purefa_ad - Manage FlashArray Active Directory Account
- purestorage.flasharray.purefa_dirsnap - Manage FlashArray File System Directory Snapshots
- purestorage.flasharray.purefa_eradication - Configure Pure Storage FlashArray Eradication Timer
- purestorage.flasharray.purefa_kmip - Manage FlashArray KMIP server objects
- purestorage.flasharray.purefa_sso - Configure Pure Storage FlashArray Single Sign-On

purestorage.flashblade
~~~~~~~~~~~~~~~~~~~~~~

- purestorage.flashblade.purefb_groupquota - Manage filesystem group quotas
- purestorage.flashblade.purefb_lag - Manage FlashBlade Link Aggregation Groups
- purestorage.flashblade.purefb_userquota - Manage filesystem user quotas

sensu.sensu_go
~~~~~~~~~~~~~~

- sensu.sensu_go.ad_auth_provider - Manage Sensu AD authentication provider
- sensu.sensu_go.auth_provider_info - List Sensu authentication providers
- sensu.sensu_go.ldap_auth_provider - Manage Sensu LDAP authentication provider
- sensu.sensu_go.oidc_auth_provider - Manage Sensu OIDC authentication provider

theforeman.foreman
~~~~~~~~~~~~~~~~~~

- theforeman.foreman.content_view_info - Fetch information about Content Views
- theforeman.foreman.content_view_version_info - Fetch information about Content Views
- theforeman.foreman.domain_info - Fetch information about Domains
- theforeman.foreman.host_errata_info - Fetch information about Host Errata
- theforeman.foreman.repository_set_info - Fetch information about Red Hat Repositories
- theforeman.foreman.setting_info - Fetch information about Settings
- theforeman.foreman.subnet_info - Fetch information about Subnets
- theforeman.foreman.subscription_info - Fetch information about Subscriptions

vyos.vyos
~~~~~~~~~

- vyos.vyos.vyos_prefix_lists - Prefix-Lists resource module for VyOS
- vyos.vyos.vyos_route_maps - Route Map Resource Module.

Unchanged Collections
---------------------

- chocolatey.chocolatey (still version 1.1.0)
- cisco.nso (still version 1.0.3)
- cisco.ucs (still version 1.6.0)
- community.fortios (still version 1.0.0)
- community.google (still version 1.0.0)
- community.kubevirt (still version 1.0.0)
- community.network (still version 3.0.0)
- community.skydive (still version 1.0.0)
- cyberark.conjur (still version 1.1.0)
- dellemc.os10 (still version 1.1.1)
- dellemc.os6 (still version 1.0.7)
- dellemc.os9 (still version 1.0.4)
- frr.frr (still version 1.0.3)
- google.cloud (still version 1.0.2)
- hpe.nimble (still version 1.1.3)
- ibm.qradar (still version 1.0.3)
- mellanox.onyx (still version 1.0.0)
- ngine_io.exoscale (still version 1.0.0)
- ngine_io.vultr (still version 1.1.0)
- splunk.es (still version 1.0.2)
