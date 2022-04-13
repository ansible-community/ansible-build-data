=======================
Ansible 6 Release Notes
=======================

This changelog describes changes since Ansible 5.0.0.

.. contents::
  :local:
  :depth: 2

v6.0.0a1
========

.. contents::
  :local:
  :depth: 2

Release Summary
---------------

Release Date: 2022-04-12

`Porting Guide <https://docs.ansible.com/ansible/devel/porting_guides.html>`_

Added Collections
-----------------

- community.sap (version 1.0.0)

Ansible-core
------------

Ansible 6.0.0a1 contains Ansible-core version 2.13.0b0.
This is a newer version than version 2.12.0 contained in the previous Ansible release.

The changes are reported in the combined changelog below.

Included Collections
--------------------

If not mentioned explicitly, the changes are reported in the combined changelog below.

+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| Collection                    | Ansible 5.0.0 | Ansible 6.0.0a1 | Notes                                                                                                                        |
+===============================+===============+=================+==============================================================================================================================+
| amazon.aws                    | 2.1.0         | 3.2.0           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| ansible.netcommon             | 2.4.0         | 2.6.1           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| ansible.utils                 | 2.4.2         | 2.6.0           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| ansible.windows               | 1.8.0         | 1.9.0           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| arista.eos                    | 3.1.0         | 4.1.2           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| awx.awx                       | 19.4.0        | 20.1.0          | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| azure.azcollection            | 1.10.0        | 1.12.0          | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| check_point.mgmt              | 2.1.1         | 2.3.0           | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| chocolatey.chocolatey         | 1.1.0         | 1.2.0           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.aci                     | 2.1.0         | 2.2.0           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.intersight              | 1.0.17        | 1.0.18          | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.ios                     | 2.5.0         | 2.8.1           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.iosxr                   | 2.5.0         | 2.9.0           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.ise                     | 1.2.1         | 2.3.0           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.meraki                  | 2.5.0         | 2.6.1           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.mso                     | 1.2.0         | 2.0.0           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.nxos                    | 2.7.1         | 2.9.1           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.ucs                     | 1.6.0         | 1.8.0           | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| cloud.common                  | 2.1.0         | 2.1.1           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| cloudscale_ch.cloud           | 2.2.0         | 2.2.1           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.aws                 | 2.1.0         | 3.2.0           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.crypto              | 2.0.1         | 2.2.4           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.digitalocean        | 1.12.0        | 1.16.0          |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.dns                 | 2.0.3         | 2.0.9           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.docker              | 2.0.1         | 2.3.0           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.general             | 4.0.2         | 4.7.0           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.grafana             | 1.2.3         | 1.3.3           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.hashi_vault         | 2.0.0         | 2.4.0           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.hrobot              | 1.2.1         | 1.2.3           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.mongodb             | 1.3.2         | 1.3.3           | There are no changes recorded in the changelog.                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.mysql               | 2.3.1         | 3.1.2           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.network             | 3.0.0         | 3.1.0           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.postgresql          | 1.5.0         | 2.1.3           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.proxysql            | 1.3.0         | 1.3.1           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.sap                 |               | 1.0.0           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.sops                | 1.2.0         | 1.2.1           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.vmware              | 1.16.0        | 2.2.0           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.windows             | 1.8.0         | 1.9.0           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.zabbix              | 1.5.0         | 1.5.1           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| containers.podman             | 1.8.2         | 1.9.3           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| dellemc.openmanage            | 4.2.0         | 5.2.0           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| f5networks.f5_modules         | 1.12.0        | 1.15.0          |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| fortinet.fortimanager         | 2.1.4         | 2.1.5           | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| fortinet.fortios              | 2.1.3         | 2.1.4           | There are no changes recorded in the changelog.                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| hpe.nimble                    | 1.1.3         | 1.1.4           | The collection did not have a changelog in this version.                                                                     |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| infinidat.infinibox           | 1.3.0         | 1.3.3           | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| infoblox.nios_modules         | 1.1.2         | 1.2.1           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| inspur.sm                     | 1.3.0         | 2.0.0           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| junipernetworks.junos         | 2.6.0         | 2.10.0          |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| kubernetes.core               | 2.2.1         | 2.3.0           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| netapp.cloudmanager           | 21.12.0       | 21.16.0         |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| netapp.ontap                  | 21.13.1       | 21.18.0         |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| netapp.storagegrid            | 21.7.0        | 21.10.0         |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| netapp_eseries.santricity     | 1.2.13        | 1.3.0           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| netbox.netbox                 | 3.3.0         | 3.6.0           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| ngine_io.cloudstack           | 2.2.2         | 2.2.3           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| ngine_io.vultr                | 1.1.0         | 1.1.1           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| openstack.cloud               | 1.5.3         | 1.8.0           | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| openvswitch.openvswitch       | 2.0.2         | 2.1.0           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| ovirt.ovirt                   | 1.6.5         | 2.0.2           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| purestorage.flasharray        | 1.11.0        | 1.12.1          |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| purestorage.flashblade        | 1.8.1         | 1.9.0           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| sensu.sensu_go                | 1.12.0        | 1.13.0          |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| t_systems_mms.icinga_director | 1.24.0        | 1.28.0          |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| theforeman.foreman            | 2.2.0         | 3.3.0           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| vyos.vyos                     | 2.6.0         | 2.8.0           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+

Major Changes
-------------

Ansible-core
~~~~~~~~~~~~

- Jinja2 Controller Requirement - Jinja2 3.0.0 or newer is required for the control node (the machine that runs Ansible) (https://github.com/ansible/ansible/pull/75881)
- Templating - remove ``safe_eval`` in favor of using ``NativeEnvironment`` but utilizing ``literal_eval`` only in cases when ``safe_eval`` was used (https://github.com/ansible/ansible/pull/75587)

amazon.aws
~~~~~~~~~~

- amazon.aws collection - The amazon.aws collection has dropped support for ``botocore<1.19.0`` and ``boto3<1.16.0``. Most modules will continue to work with older versions of the AWS SDK, however compatability with older versions of the SDK is not guaranteed and will not be tested. When using older versions of the SDK a warning will be emitted by Ansible (https://github.com/ansible-collections/amazon.aws/pull/574).

chocolatey.chocolatey
~~~~~~~~~~~~~~~~~~~~~

- win_chocolatey - Added choco_args option to pass additional arguments directly to Chocolatey.

cisco.ise
~~~~~~~~~

- Update ciscoisesdk requirement to 1.2.0
- anc_endpoint_bulk_monitor_status_info - change return value, it returns BulkStatus content.
- anc_policy_bulk_monitor_status_info - change return value, it returns BulkStatus content.
- backup_last_status_info - change return value, it returns response content.
- device_administration_authentication_rules - deletes parameter identitySourceId.
- device_administration_authentication_rules_info - change return value, it returns response content.
- device_administration_authorization_rules_info - change return value, it returns response content.
- device_administration_conditions - deletes parameter attributeId.
- device_administration_conditions_for_authentication_rule_info - change return value, it returns response content.
- device_administration_conditions_for_authorization_rule_info - change return value, it returns response content.
- device_administration_conditions_for_policy_set_info - change return value, it returns response content.
- device_administration_conditions_info - change return value, it returns response content.
- device_administration_dictionary_attributes_authentication_info - change return value, it returns response content.
- device_administration_dictionary_attributes_authorization_info - change return value, it returns response content.
- device_administration_dictionary_attributes_policy_set_info - change return value, it returns response content.
- device_administration_global_exception_rules_info - change return value, it returns response content.
- device_administration_network_conditions_info - change return value, it returns response content.
- device_administration_time_date_conditions - deletes parameter attributeId.
- device_administration_time_date_conditions_info - change return value, it returns response content.
- egress_matrix_cell_bulk_monitor_status_info - change return value, it returns BulkStatus content.
- network_access_authentication_rules - deletes parameter identitySourceId.
- network_access_conditions - deletes parameter attributeId.
- network_access_time_date_conditions - deletes parameter attributeId.
- node_deployment - update parameters.
- node_deployment_info - add filter and filterType parameters.
- node_group - fixes response recollection.
- node_group_info - fixes response recollection.
- repository_files_info - change return value, it returns response content.
- repository_info - change return value, it returns response content.
- sg_acl_bulk_monitor_status_info - change return value, it returns BulkStatus content.
- sg_mapping_bulk_monitor_status_info - change return value, it returns BulkStatus content.
- sg_mapping_group_bulk_monitor_status_info - change return value, it returns BulkStatus content.
- sg_mapping_group_info - change return value, it returns BulkStatus content.
- sg_to_vn_to_vlan_bulk_monitor_status_info - change return value, it returns BulkStatus content.
- sgt - change generationId type from int to str.
- sgt_bulk_monitor_status_info - change return value, it returns BulkStatus content.
- sxp_connections_bulk_monitor_status_info - change return value, it returns BulkStatus content.
- sxp_local_bindings_bulk_monitor_status_info - change return value, it returns BulkStatus content.
- sxp_vpns_bulk_monitor_status_info - change return value, it returns BulkStatus content.
- system_certificate - new parameters portalTagTransferForSameSubject and roleTransferForSameSubject.
- system_certificate - portalTagTransferForSameSubject parameter renamed to allowPortalTagTransferForSameSubject.
- system_certificate - roleTransferForSameSubject parameter renamed to allowRoleTransferForSameSubject.
- system_certificate_import - new parameters portalTagTransferForSameSubject and roleTransferForSameSubject.
- system_certificate_import - portalTagTransferForSameSubject parameter renamed to allowPortalTagTransferForSameSubject.
- system_certificate_import - roleTransferForSameSubject parameter renamed to allowRoleTransferForSameSubject.
- trustsec_nbar_app_info - change type from str to list.
- trustsec_vn_info - change type from str to list.

cisco.meraki
~~~~~~~~~~~~

- meraki_mr_radio - New module

community.aws
~~~~~~~~~~~~~

- community.aws collection - The community.aws collection has dropped support for ``botocore<1.19.0`` and ``boto3<1.16.0``. Most modules will continue to work with older versions of the AWS SDK, however compatability with older versions of the SDK is not guaranteed and will not be tested. When using older versions of the SDK a warning will be emitted by Ansible (https://github.com/ansible-collections/community.aws/pull/809).
- s3_bucket_notifications - refactor module to support SNS / SQS targets as well as the existing support for Lambda functions (https://github.com/ansible-collections/community.aws/issues/140).

community.postgresql
~~~~~~~~~~~~~~~~~~~~

- postgresql_privs - the ``usage_on_types`` feature have been deprecated and will be removed in ``community.postgresql 3.0.0``. Please use the ``type`` option with the ``type`` value to explicitly grant/revoke privileges on types (https://github.com/ansible-collections/community.postgresql/issues/207).
- postgresql_query - the ``path_to_script`` and ``as_single_query`` options as well as the ``query_list`` and ``query_all_results`` return values have been deprecated and will be removed in ``community.postgresql 3.0.0``. Please use the ``community.postgresql.postgresql_script`` module to execute statements from scripts (https://github.com/ansible-collections/community.postgresql/issues/189).
- postgresql_query - the default value of the ``as_single_query`` option changes to ``yes``. If the related behavior of your tasks where the module is involved changes, please adjust the parameter's value correspondingly (https://github.com/ansible-collections/community.postgresql/issues/85).
- postgresql_user - the ``priv`` argument has been deprecated and will be removed in ``community.postgresql 3.0.0``. Please use the ``postgresql_privs`` module to grant/revoke privileges instead (https://github.com/ansible-collections/community.postgresql/issues/212).

containers.podman
~~~~~~~~~~~~~~~~~

- Add podman_tag module
- Add secrets driver and driver opts support

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- All modules can read custom or organizational CA signed certificate from the environment variables. Please refer to `SSL Certificate Validation <https://github.com/dell/dellemc-openmanage-ansible-modules#ssl-certificate-validation>`_ section in the `README.md <https://github.com/dell/dellemc-openmanage-ansible-modules/blob/collections/README.md#SSL-Certificate-Validation>`_ for modification to existing playbooks or setting environment variable.
- All modules now support SSL over HTTPS and socket level timeout.

f5networks.f5_modules
~~~~~~~~~~~~~~~~~~~~~

- bigip_device_info - pagination logic has also been added to help with api stability.
- bigip_device_info - the module no longer gathers information from all partitions on device. This change will stabalize the module by gathering resources only from the given partition and prevent the module from gathering way too much information that might result in crashing.

ovirt.ovirt
~~~~~~~~~~~

- manageiq - role removed (https://github.com/oVirt/ovirt-ansible-collection/pull/375).

vyos.vyos
~~~~~~~~~

- Add 'pool' as value to server key in ntp_global.

Minor Changes
-------------

Ansible-core
~~~~~~~~~~~~

- Action Plugins - Add helper method for argument spec validation, and extend to pause and async_wrapper
- Added AIX root CA certs folders - enhance the TLS support in ``uri`` task on AIX
- Added ``module_utils.compat.typing`` to facilitate type-hinting on all supported Python versions.
- Ansible.Basic - small changes to allow use in PowerShell modules running on non-Windows platforms (https://github.com/ansible/ansible/pull/76924).
- AnsibleModule.run_command() now has a toggle to allow caller to decide to handle exceptions from executing the command itself
- Attach concat function to an environment class (https://github.com/ansible/ansible/pull/76282)
- Clarify in a comment that unrolling an iterator in ``Templar._finalize`` is actually necessary. Also switch to using the ``_unroll_iterator`` decorator directly to deduplicate code in ``Templar._finalize``. (https://github.com/ansible/ansible/pull/76436)
- Installation - modernize our python installation, to reduce dynamic code in setup.py, and migrate what is feasible to setup.cfg. This will enable shipping wheels in the future.
- PlayIterator - introduce public methods to access ``PlayIterator._host_states`` (https://github.com/ansible/ansible/pull/74416)
- PlayIterator - use enums for Iterating and Failed states (https://github.com/ansible/ansible/pull/74511)
- Reduce number of iterations through PlayIterator (https://github.com/ansible/ansible/pull/74175)
- Remove more Python 2.x compatibility code from controller (https://github.com/ansible/ansible/pull/77320).
- Start of moving away from using Six, Python 2 and 3 compatibility library (https://github.com/ansible/ansible/pull/75863)
- The collection loader now reports a Python warning if an attempt is made to install the Ansible collection loader a second time. Previously this condition was reported using an Ansible warning.
- ``ansible-galaxy collection [install|verify]`` - allow user-provided signature sources in addition to those from the Galaxy server. Each collection entry in a requirements file can specify a ``signatures`` key followed by a list of sources. Collection name(s) provided on the CLI can specify additional signature sources by using the ``--signatures`` CLI option. Signature sources should be URIs that can be opened with ``urllib.request.urlopen()``, such as "https://example.com/path/to/detached_signature.asc" or "file:///path/to/detached_signature.asc". The ``--keyring`` option must be specified if signature sources are provided.
- ``ansible-galaxy collection [install|verify]`` - use gpg to verify the authenticity of the signed ``MANIFEST.json`` with ASCII armored detached signatures provided by the Galaxy server. The keyring (which is not managed by ``ansible-galaxy``) must be provided with the ``--keyring`` option to use signature verification. If no ``--keyring`` is specified and the collection to ``install|verify`` has associated detached signatures on the Galaxy server, a warning is provided.
- ``ansible-galaxy collection install`` - Add a global configuration to modify the required number of signatures that must verify the authenticity of the collection. By default, the number of required successful signatures is 1. Set this option to ``all`` to require all signatures verify the collection. To ensure signature verification fails if there are no valid signatures, prepend the value with '+', such as ``+all`` or ``+1``.
- ``ansible-galaxy collection install`` - Add a global ignore list for gpg signature errors. This can be used to ignore certain signatures when the number of required successful signatures is all. When the required number of successful signatures is a positive integer, the only effect this has is to display fewer errors to the user on failure (success is determined by having the minimum number of successful signatures, in which case all errors are disregarded).
- ``ansible-galaxy collection install`` - Add a global toggle to turn off GPG signature verification.
- ``ansible-galaxy collection install`` - Store Galaxy server metadata alongside installed collections for provenance. Signatures obtained from the Galaxy server can be used for offline verification with ``ansible-galaxy collection verify --offline``.
- ansible-console - Provide a  way to customize the stdout callback
- ansible-core modules - Remove unused Python shebangs from built-in modules.
- ansible-doc metadata dump - add option ``--no-fail-on-errors`` which allows to not fail the ansible-doc invocation when errors happen during docs parsing or processing. Instead they are reported in the JSON result in an ``error`` key for the affected plugins (https://github.com/ansible/ansible/pull/77035).
- ansible-galaxy - the option to skip certificate verification now also applies when cloning via SCM (git/hg) (https://github.com/ansible/ansible/issues/41077)
- ansible-test - Accept new-style Python modules without a shebang.
- ansible-test - Add ``--version`` support to show the ansible-core version.
- ansible-test - Add support for ``rhel/8.5`` remote instances.
- ansible-test - Add support for remote testing of FreeBSD 12.3.
- ansible-test - Add support for running container tests with ``podman remote`` (https://github.com/ansible/ansible/pull/75753)
- ansible-test - Added the ``fedora35`` test container.
- ansible-test - Change the maximum number of open files in a test container from the default to ``10240``.
- ansible-test - Declare public dependencies of ansible-core and use to limit unguarded imports in plugins.
- ansible-test - Importing ``distutils`` now results in an error.
- ansible-test - Installation of ``cryptography`` is no longer version constrained when ``openssl`` 1.1.0 or later is installed.
- ansible-test - Miscellaneous code cleanup and type hint fixes.
- ansible-test - PowerShell in the ``base`` and ``default`` containers has been upgraded to version 7.1.4.
- ansible-test - Remove RHEL 8.4 remote (``rhel/8.4``) support.
- ansible-test - Remove ``idna`` constraint.
- ansible-test - Remove obsolete ``MAXFD`` display.
- ansible-test - Remove obsolete constraints for Python 2.6.
- ansible-test - Remove support for FreeBSD 12.2 remote provisioning.
- ansible-test - Remove support for macOS 11.1 remote provisioning.
- ansible-test - Remove support for provisioning remote AIX instances.
- ansible-test - Remove the ``centos8`` test container since CentOS 8 will reach end-of-life soon.
- ansible-test - Remove the ``fedora33`` test container since Fedora 33 will reach end-of-life soon.
- ansible-test - Remove unused Python 2.x compatibility code.
- ansible-test - Removed support for Sherlock from the Azure provisioning plugin.
- ansible-test - Removed used ``MarkupSafe`` constraint for Python 3.5 and earlier.
- ansible-test - Requirements for the plugin import test are now frozen.
- ansible-test - Shellcheck in the ``base`` and ``default`` containers has been upgraded to version 0.7.0.
- ansible-test - Stop early with an error if the current working directory contains an invalid collection namespace or name.
- ansible-test - The ``--help`` option is now available when an unsupported cwd is in use.
- ansible-test - The ``--help`` output now shows the same instructions about cwd as would be shown in error messages if the cwd is unsupported.
- ansible-test - The ``pip`` and ``wheel`` packages are removed from all sanity test virtual environments after installation completes to reduce their size. Previously they were only removed from the environments used for the ``import`` sanity test.
- ansible-test - The explanation about cwd usage has been improved to explain more clearly what is required.
- ansible-test - The hash for all managed sanity test virtual environments has changed. Containers that include ``ansible-test sanity --prime-venvs`` will need to be rebuilt to continue using primed virtual environments.
- ansible-test - Update ``base`` container to version 2.1.0.
- ansible-test - Update ``base`` container to version 2.2.0.
- ansible-test - Update ``default`` containers to version 5.2.0.
- ansible-test - Update ``default`` containers to version 5.4.0.
- ansible-test - Update ``default`` containers to version 5.5.0.
- ansible-test - Update ``default`` containers to version 5.6.2.
- ansible-test - Update ``default`` containers to version 5.7.0.
- ansible-test - Update ``default`` containers to version 5.8.0.
- ansible-test - Update ``pip`` used to bootstrap remote FreeBSD instances from version 20.3.4 to 21.3.1.
- ansible-test - Update sanity test requirements.
- ansible-test - Update the NIOS test plugin container to version 1.4.0.
- ansible-test - Update the ``alpine`` container to version 3.3.0. This updates the base image from 3.14.2 to 3.15.0, which includes support for installing binary wheels using pip.
- ansible-test - Update the ``base`` and ``default`` containers from Python 3.10.0rc2 to 3.10.0.
- ansible-test - Update the ``base`` and ``default`` containers from a Ubuntu 18.04 to Ubuntu 20.04 base image.
- ansible-test - Update the ``default`` containers to version 5.1.0.
- ansible-test - Update the ``galaxy`` test plugin to get its container from a copy on quay.io.
- ansible-test - Update the ``openshift`` test plugin to get its container from a copy on quay.io.
- ansible-test - Use Python 3.10 as the default Python version for the ``base`` and ``default`` containers.
- ansible-test - add macOS 12.0 as a remote target (https://github.com/ansible/ansible/pull/76328)
- ansible-test - handle JSON decode error gracefully in podman environment.
- ansible-test pslint - Added the `AvoidLongLines <https://github.com/PowerShell/PSScriptAnalyzer/blob/master/docs/Rules/AvoidLongLines.md>`_ rule set to a length of 160.
- ansible-test pslint - Added the `PlaceCloseBrace <https://github.com/PowerShell/PSScriptAnalyzer/blob/master/docs/Rules/PlaceCloseBrace.md>`_ rule set to enforce close braces on a newline.
- ansible-test pslint - Added the `PlaceOpenBrace <https://github.com/PowerShell/PSScriptAnalyzer/blob/master/docs/Rules/PlaceOpenBrace.md>`_ rule set to enforce open braces on the same line and a subsequent newline.
- ansible-test pslint - Added the `UseConsistentIndentation <https://github.com/PowerShell/PSScriptAnalyzer/blob/master/docs/Rules/UseConsistentIndentation.md>`_ rule to enforce indentation is done with 4 spaces.
- ansible-test pslint - Added the `UseConsistentWhitespace <https://github.com/PowerShell/PSScriptAnalyzer/blob/master/docs/Rules/UseConsistentWhitespace.md>`_ rule to enforce whitespace consistency in PowerShell.
- ansible-test pslint - Updated ``PowerShellScriptAnalyzer`` to 1.20.0
- ansible-test sanity validate-modules - the validate-modules sanity test now also checks the documentation of documentable plugin types (https://github.com/ansible/ansible/pull/71734).
- ansible-test validate-modules sanity test - add more schema checks to improve quality of plugin documentation (https://github.com/ansible/ansible/pull/77268).
- ansible-test validate_modules - allow ``choices`` for return values (https://github.com/ansible/ansible/pull/76009).
- apt - Add support for using ">=" in package version number matching.
- apt - Adds APT option ``--allow-change-held-packages`` as module parameter ``allow_change_held_packages`` to allow APT up- or downgrading a package which is on APTs hold list (https://github.com/ansible/ansible/issues/65325)
- auto inventory plugin will now give plugin loading information on verbose output
- callbacks - Add result serialization format options to ``_dump_results`` allowing plugins such as the ``default`` callback to emit ``YAML`` serialized task results in addition to ``JSON``
- dnf - add more specific error message for GPG validation (https://github.com/ansible/ansible/issues/76192)
- env lookup, add default option
- facts - report prefix length for IPv4 addresses in Linux network facts.
- get_parsable_locale now logs result when in debug mode.
- git - display the destination directory path in error msg when local_mods detects local modifications conflict so that users see the exact location
- iptables - add the ``chain_management`` parameter that controls iptables chain creation and deletion
- jinja2_native - keep same behavior on Python 3.10.
- junit callback - Add support for replacing the directory portion of out-of-tree relative task paths with a placeholder.
- k8s - scenario guides for kubernetes migrated to ``kubernetes.core`` collection.
- module_utils.distro - Add missing ``typing`` import from original code.
- package_facts - add pkg_info support for OpenBSD and NetBSD (https://github.com/ansible/ansible/pull/76580)
- services_facts - Add support for openrc (https://github.com/ansible/ansible/pull/76373).
- setting DEFAULT_FACT_PATH is being deprecated in favor of the generic module_defaults keyword
- uri - Avoid reading the response body when not needed
- uri - Eliminate multiple requests to determine the final URL for file naming with ``dest``
- validate-modules - do some basic validation on the ``M(...)``, ``U(...)``, ``L(..., ...)`` and ``R(..., ...)`` documentation markups (https://github.com/ansible/ansible/pull/76262).
- vmware - migrated vmware scenario guides to `community.vmware` repo.
- yum, dnf - add sslverify option to temporarily disable certificate validation for a repository

amazon.aws
~~~~~~~~~~

- add new parameters hostvars_prefix and hostvars_suffix for inventory plugins aws_ec2 and aws_rds (https://github.com/ansible-collections/amazon.aws/issues/535).
- aws_s3 - Add ``validate_bucket_name`` option, to control bucket name validation (https://github.com/ansible-collections/amazon.aws/pull/615).
- aws_s3 - add latest choice on ``overwrite`` parameter to get latest object on S3 (https://github.com/ansible-collections/amazon.aws/pull/595).
- aws_secret - add pagination for ``bypath`` functionality (https://github.com/ansible-collections/amazon.aws/pull/591).
- bump the release version of the amazon.aws collection from 3.1.0 to 3.1.1 because of a bug that occurred while uploading to Galaxy.
- ec2_instance - Fix scope of deprecation warning to not show warning when ``state`` in ``absent`` (https://github.com/ansible-collections/amazon.aws/pull/719).
- ec2_instance - add count parameter support (https://github.com/ansible-collections/amazon.aws/pull/539).
- ec2_vol - add support for OutpostArn param (https://github.com/ansible-collections/amazon.aws/pull/597).
- ec2_vol - tag volume on creation (https://github.com/ansible-collections/amazon.aws/pull/603).
- ec2_vpc_route_table - add support for IPv6 in creating route tables (https://github.com/ansible-collections/amazon.aws/pull/601).
- ec2_vpc_route_table - support associating internet gateways (https://github.com/ansible-collections/amazon.aws/pull/690).
- module_utils.elbv2 - Add support for alb specific attributes and compare_elb_attributes method to support check_mode in module_utils.elbv2 (https://github.com/ansible-collections/amazon.aws/pull/696).
- s3_bucket - Add ``validate_bucket_name`` option, to control bucket name validation (https://github.com/ansible-collections/amazon.aws/pull/615).
- s3_bucket - Add support for enforced bucket owner object ownership (https://github.com/ansible-collections/amazon.aws/pull/694).

ansible.netcommon
~~~~~~~~~~~~~~~~~

- Copied the cliconf, httpapi, netconf, and terminal base plugins and NetworkConnectionBase into netcommon. These base plugins may now be imported from netcommmon instead of ansible if a collection depends on netcommon versions newer than this version, allowing features and bugfixes to flow to those collections without upgrading ansible.
- Make ansible_network_os as optional param for httpapi connection plugin.
- Redirected ipaddr filters to ansible.utils (https://github.com/ansible-collections/ansible.netcommon/pull/359).
- Support removal of non-config lines from running config while taking backup.
- `network_cli` - added new option 'become_errors' to determine how privilege escalation failures are handled.
- httpapi - new parameter retries in send() method limits the number of times a request is retried when a HTTP error that can be worked around is encountered. The default is to retry indefinitely to maintain old behavior, but this default may change in a later breaking release.

ansible.utils
~~~~~~~~~~~~~

- 'consolidate' filter plugin added.
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

ansible.windows
~~~~~~~~~~~~~~~

- win_dsc - deduplicated error writing code with a new function. No actual error text was changed.
- win_powershell - Added ``$Ansible.Verbosity`` for scripts to adjust code based on the verbosity Ansible is running as

arista.eos
~~~~~~~~~~

- Add eos_hostname resource module.
- Add eos_snmp_server resource module.
- eos_acls - Fix examples typos

chocolatey.chocolatey
~~~~~~~~~~~~~~~~~~~~~

- All modules - Ported away from the Ansible.Legacy format, using Ansible.Basic.Module instead.
- win_chocolatey - Added state: upgrade as an alias for state: latest.
- win_chocolatey - Improved automatic URL handling for getting the install.ps1 script from a custom source URL.
- win_chocolatey - Improved handling of Chocolatey bootstrapping installation script.
- win_chocolatey - Removed warning for installing Chocolatey if when specifically installing it with `name: chocolatey`.

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

cisco.ios
~~~~~~~~~

- `ios_acls` - Added enable_fragment attribute to enable fragments under ace.
- `ios_acls` - feature: Remarks can be configured for ACLs.
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
- `ios_hostname` - New Resource module added.
- `ios_snmp_server` - Enables configuration of v3 auth and encryption password for each user.
- `ios_snmp_server` - New Resource module added.

cisco.iosxr
~~~~~~~~~~~

- Add commit_confirmed functionality in IOSXR.
- Add disable_default_comment option to disable default comment in iosxr_config module.
- Add iosxr_snmp_server resource module.
- Added support for keys net_group, port_group to resolve issue with fact gathering against IOS-XR 6.6.3.
- IOSXR - Fix sanity for missing elements tag under list type attribute.
- `iosxr_hostname` - New Resource module added.

cisco.ise
~~~~~~~~~

- Add ise_uses_csrf_token parameter to modules
- Update requirements to use ciscoisesdk >= 1.4.0.
- aci_bindings_info - change default response to [].
- active_directory_info - change default response to [].
- admin_user_info - change default response to [].
- allowed_protocols_info - change default response to [].
- anc_endpoint_info - change default response to [].
- anc_policy_info - change default response to [].
- authorization_profile_info - change default response to [].
- backup_schedule_config_update - new module.
- byod_portal_info - change default response to [].
- certificate_profile_info - change default response to [].
- certificate_template_info - change default response to [].
- csr_export_info - Instead of returning the data string, it now returns a dictionary. The dictionary has property data with the previous string value.
- csr_export_info - add parameter filename.
- csr_info - change default response to [].
- downloadable_acl_info - change default response to [].
- egress_matrix_cell_info - change default response to [].
- endpoint_bulk_monitor_status_info - change default response to [].
- endpoint_certificate - Instead of returning the data string, it now returns a dictionary. The dictionary has property data with the previous string value.
- endpoint_certificate - add parameter filename.
- hotpatch_info - new module.
- hotpatch_install - new module.
- hotpatch_rollback - new module.
- licensing_connection_type_info - new module.
- licensing_eval_license_info - new module.
- licensing_feature_to_tier_mapping_info - new module.
- licensing_registration_create - new module.
- licensing_registration_info - new module.
- licensing_smart_state_create - new module.
- licensing_smart_state_info - new module.
- licensing_tier_state_create - fix function call.
- licensing_tier_state_create - new module.
- licensing_tier_state_info - new module.
- node_deployment_sync - new module.
- node_group_node_create - new module.
- node_group_node_delete - new module.
- node_group_node_info - new module.
- node_primary_to_standalone - new module.
- node_secondary_to_primary - new module.
- node_services_interfaces_info - new module.
- node_services_profiler_probe_config - new module.
- node_services_profiler_probe_config_info - new module.
- node_services_sxp_interfaces - new module.
- node_services_sxp_interfaces_info - new module.
- node_standalone_to_primary - new module.
- pan_ha_update - new module.
- patch_info - new module.
- patch_install - new module.
- patch_rollback - new module.
- proxy_connection_settings - new module.
- proxy_connection_settings_info - new module.
- radius_server_sequence_info - change default response to [].
- rest_id_store_info - change default response to [].
- self_registered_portal_info - change default response to [].
- selfsigned_certificate_generate - new module.
- sg_acl_info - change default response to [].
- sg_to_vn_to_vlan_info - change default response to [].
- sgt_info - change default response to [].
- sponsor_group_info - change default response to [].
- sponsor_portal_info - change default response to [].
- sponsored_guest_portal_info - change default response to [].
- support_bundle_download - Instead of returning the data string, it now returns a dictionary. The dictionary has property data with the previous string value.
- support_bundle_download - add parameter filename.
- support_bundle_status_info - change default response to [].
- sxp_connections_info - change default response to [].
- sxp_local_bindings_info - change default response to [].
- sxp_vpns_info - change default response to [].
- system_certificate_export_info - Instead of returning the data string, it now returns a dictionary. The dictionary has property data with the previous string value.
- system_certificate_export_info - add parameter filename.
- tacacs_command_sets_info - change default response to [].
- tacacs_external_servers_info - change default response to [].
- tacacs_profile_info - change default response to [].
- tacacs_server_sequence_info - change default response to [].
- telemetry_info - change default response to [].
- transport_gateway_settings - new module.
- transport_gateway_settings_info - new module.
- trusted_certificate - change default response to [].
- trusted_certificate_export_info - Instead of returning the data string, it now returns a dictionary. The dictionary has property data with the previous string value.
- trusted_certificate_export_info - add parameter filename.
- trustsec_nbar_app - new module.
- trustsec_nbar_app_info - new module.
- trustsec_nbarapp - new playbook.
- trustsec_sg_vn_mapping - new module.
- trustsec_sg_vn_mapping - new playbook.
- trustsec_sg_vn_mapping_bulk_create - new module.
- trustsec_sg_vn_mapping_bulk_delete - new module.
- trustsec_sg_vn_mapping_bulk_update - new module.
- trustsec_sg_vn_mapping_info - new module.
- trustsec_vn - new module.
- trustsec_vn - new playbook.
- trustsec_vn_bulk_create - new module.
- trustsec_vn_bulk_delete - new module.
- trustsec_vn_bulk_update - new module.
- trustsec_vn_info - new module.
- trustsec_vn_vlan_mapping - new module.
- trustsec_vn_vlan_mapping - new playbook.
- trustsec_vn_vlan_mapping_bulk_create - new module.
- trustsec_vn_vlan_mapping_bulk_delete - new module.
- trustsec_vn_vlan_mapping_bulk_update - new module.
- trustsec_vn_vlan_mapping_info - new module.

cisco.meraki
~~~~~~~~~~~~

- meraki_mx_l7_firewall - Allow passing an empty ruleset to delete all rules
- meraki_ssid - Add support for enterprise_admin_access and splash_guest_sponsor_domains with the latter required for creating a sponsor portal.
- meraki_utils - Add debugging output for failed socket connections

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

- Add nxos_hostname resource module.
- Add nxos_snmp_server resource module.

cloud.common
~~~~~~~~~~~~

- Move the content of README_ansible_turbo.module.rst in the main README.md to get visibility on Ansible Galaxy.

cloudscale_ch.cloud
~~~~~~~~~~~~~~~~~~~

- Updated documentation: ``ssh_keys`` is a YAML list, not a string.

community.aws
~~~~~~~~~~~~~

- Added suport for retries (AWSRetry.jittered_backoff) for cloudfront_distribution (https://github.com/ansible-collections/community.aws/issues/296)
- aws_acm - Add ``tags`` and ``purge_tags`` parameters to tag certificates in ACM (https://github.com/ansible-collections/community.aws/pull/870).
- aws_glue_job - Added ``command_python_version`` parameter (https://github.com/ansible-collections/community.aws/pull/480).
- aws_glue_job - Added ``glue_version`` parameter (https://github.com/ansible-collections/community.aws/pull/480).
- aws_glue_job - Added support for check mode (https://github.com/ansible-collections/community.aws/pull/480).
- aws_glue_job - Added support for tags (https://github.com/ansible-collections/community.aws/pull/480).
- aws_msk_config - remove duplicated and unspecific requirements (https://github.com/ansible-collections/community.aws/pull/863).
- aws_secret - Add ``resource_policy`` parameter (https://github.com/ansible-collections/community.aws/pull/843).
- aws_ssm connection plugin - add parameters to explicitly specify SSE mode and KMS key id for uploads on the file transfer bucket. (https://github.com/ansible-collections/community.aws/pull/763)
- cloudfront_distribution - Added support for retries (AWSRetry.jittered_backoff) (https://github.com/ansible-collections/community.aws/issues/296)
- dynamodb_table - the ``table_class`` parameter has been added (https://github.com/ansible-collections/community.aws/pull/880).
- ec2_asg - Added functionality to detach specific instances and/or decrement desired capacity from ASG without terminating instances (https://github.com/ansible-collections/community.aws/pull/933).
- ec2_asg - Restructure integration tests to run in parallel and reduce runtime (https://github.com/ansible-collections/community.aws/pull/1036).
- ec2_asg - add support for ``purge_tags`` to ec2_asg (https://github.com/ansible-collections/community.aws/pull/960).
- ec2_eip - refactor module by fixing check_mode and more clear return obj. added integration tests (https://github.com/ansible-collections/community.aws/pull/936)
- ec2_launch_template - Add metadata options parameter ``http_protocol_ipv6`` and ``instance_metadata_tags`` (https://github.com/ansible-collections/community.aws/pull/917).
- ec2_lc - add support for throughput parameter (https://github.com/ansible-collections/community.aws/pull/790).
- ec2_placement_group - add support for partition strategy and partition count (https://github.com/ansible-collections/community.aws/pull/872).
- ecs_taskdefinition - remove duplicated and unspecific requirements (https://github.com/ansible-collections/community.aws/pull/863).
- elb_application_lb - Add support for alb specific attributes and check_mode support for modifying them (https://github.com/ansible-collections/community.aws/pull/963).
- elb_application_lb - add check_mode support and refactor integration tests (https://github.com/ansible-collections/community.aws/pull/894)
- elb_application_lb_info - update documentation and refactor integration tests (https://github.com/ansible-collections/community.aws/pull/894)
- elb_instance - `wait` parameter is no longer ignored (https://github.com/ansible-collections/community.aws/pull/826)
- elb_target_group - add support for alb target_type and update documentation (https://github.com/ansible-collections/community.aws/pull/966).
- elb_target_group - add support for parameter ``deregistration_connection_termination`` (https://github.com/ansible-collections/community.aws/pull/913).
- elb_target_group - add support for setting load_balancing_algorithm_type (https://github.com/ansible-collections/community.aws/pull/1016).
- iam_managed_policy - refactor module adding ``check_mode`` and better AWSRetry backoff logic (https://github.com/ansible-collections/community.aws/pull/893).
- iam_user - add boto3 waiter for iam user creation (https://github.com/ansible-collections/community.aws/pull/822).
- iam_user - add parameter ``password_reset_required`` (https://github.com/ansible-collections/community.aws/pull/860).
- iam_user - add password management support bringing parity with `iam` module (https://github.com/ansible-collections/community.aws/pull/822).
- rds_instance - add `choices` for valid engine value (https://github.com/ansible-collections/community.aws/pull/1034).
- rds_subnet_group - add ``check_mode`` (https://github.com/ansible-collections/community.aws/pull/562).
- rds_subnet_group - add ``tags`` feature (https://github.com/ansible-collections/community.aws/pull/562).
- route53 - ``ttl``  and ``value`` are not required for deleting records (https://github.com/ansible-collections/community.aws/pull/801).
- route53_info - `max_items` and `type` are no longer ignored fixing a regression (https://github.com/ansible-collections/community.aws/pull/813).
- s3_lifecycle - Add ``abort_incomplete_multipart_upload_days`` and ``expire_object_delete_marker`` parameters (https://github.com/ansible-collections/community.aws/pull/794).
- wafv2_web_acl - Documentation updates wafv2_web_acl and aws_waf_web_acl (https://github.com/ansible-collections/community.aws/pull/721).
- wafv2_web_acl - Extended the wafv2_web_acl module to also take the ``custom_response_bodies`` argument (https://github.com/ansible-collections/community.aws/pull/721).

community.crypto
~~~~~~~~~~~~~~~~

- Adjust error messages that indicate ``cryptography`` is not installed from ``Can't`` to ``Cannot`` (https://github.com/ansible-collections/community.crypto/pull/374).
- openssh_cert - added ``ignore_timestamps`` parameter so it can be used semi-idempotent with relative timestamps in ``valid_to``/``valid_from`` (https://github.com/ansible-collections/community.crypto/issues/379).

community.digitalocean
~~~~~~~~~~~~~~~~~~~~~~

- Set Python 3.9 as the C(python-version) and C(target-python-version) in the integration, sanity, and unit tests for Ansible > 2.9 (3.8 otherwise).
- Updates DigitalOcean API documentation links to current domain with working URL anchors (https://github.com/ansible-collections/community.digitalocean/issues/223).
- black test - added a 15 minute timeout (https://github.com/ansible-collections/community.digitalocean/issues/228).
- digital_ocean_domain - add support for IPv6 apex domain records (https://github.com/ansible-collections/community.digitalocean/issues/226).
- digital_ocean_droplet - allow the user to override the Droplet action and status polling interval (https://github.com/ansible-collections/community.digitalocean/issues/194).
- digital_ocean_kubernetes - adding support for HA control plane (https://github.com/ansible-collections/community.digitalocean/issues/190).
- digital_ocean_kubernetes_info - switching C(changed=True) to C(changed=False) since getting information is read-only in nature (https://github.com/ansible-collections/community.digitalocean/issues/204).
- integration tests - added a 120 minute timeout (https://github.com/ansible-collections/community.digitalocean/issues/228).
- sanity and unit tests - added a 30 minute timeout (https://github.com/ansible-collections/community.digitalocean/issues/228).

community.docker
~~~~~~~~~~~~~~~~

- docker connection plugin - implement connection reset by clearing internal container user cache (https://github.com/ansible-collections/community.docker/pull/312).
- docker connection plugin - simplify ``actual_user`` handling code (https://github.com/ansible-collections/community.docker/pull/311).
- docker connection plugin - the plugin supports new ways to define the timeout. These are the ``ANSIBLE_DOCKER_TIMEOUT`` environment variable, the ``timeout`` setting in the ``docker_connection`` section of ``ansible.cfg``, and the ``ansible_docker_timeout`` variable (https://github.com/ansible-collections/community.docker/pull/297).
- docker_api connection plugin - implement connection reset by clearing internal container user/group ID cache (https://github.com/ansible-collections/community.docker/pull/312).
- docker_api connection plugin - the plugin supports new ways to define the timeout. These are the ``ANSIBLE_DOCKER_TIMEOUT`` environment variable, the ``timeout`` setting in the ``docker_connection`` section of ``ansible.cfg``, and the ``ansible_docker_timeout`` variable (https://github.com/ansible-collections/community.docker/pull/308).
- docker_config - add support for rolling update, set ``rolling_versions`` to ``true`` to enable (https://github.com/ansible-collections/community.docker/pull/295, https://github.com/ansible-collections/community.docker/issues/109).
- docker_container_exec - add ``detach`` parameter (https://github.com/ansible-collections/community.docker/issues/250, https://github.com/ansible-collections/community.docker/pull/255).
- docker_container_exec - add ``env`` option (https://github.com/ansible-collections/community.docker/issues/248, https://github.com/ansible-collections/community.docker/pull/254).
- docker_secret - add support for rolling update, set ``rolling_versions`` to ``true`` to enable (https://github.com/ansible-collections/community.docker/pull/293, https://github.com/ansible-collections/community.docker/issues/21).
- docker_swarm_service - add support for setting capabilities with the ``cap_add`` and ``cap_drop`` parameters. Usage is the same as with the ``capabilities`` and ``cap_drop`` parameters for ``docker_container`` (https://github.com/ansible-collections/community.docker/pull/294).

community.general
~~~~~~~~~~~~~~~~~

- Avoid internal ansible-core module_utils in favor of equivalent public API available since at least Ansible 2.9. This fixes some instances added since the last time this was fixed (https://github.com/ansible-collections/community.general/pull/4232).
- aix_filesystem - calling ``run_command`` with arguments as ``list`` instead of ``str`` (https://github.com/ansible-collections/community.general/pull/3833).
- aix_lvg - calling ``run_command`` with arguments as ``list`` instead of ``str`` (https://github.com/ansible-collections/community.general/pull/3834).
- ansible_galaxy_install - added option ``no_deps`` to the module (https://github.com/ansible-collections/community.general/issues/4174).
- cobbler inventory plugin - add ``include_profiles`` option (https://github.com/ansible-collections/community.general/pull/4068).
- gitlab - add more token authentication support with the new options ``api_oauth_token`` and ``api_job_token`` (https://github.com/ansible-collections/community.general/issues/705).
- gitlab - clean up modules and utils (https://github.com/ansible-collections/community.general/pull/3694).
- gitlab_group, gitlab_project - add new option ``avatar_path`` (https://github.com/ansible-collections/community.general/pull/3792).
- gitlab_group_variable - new ``variables`` parameter (https://github.com/ansible-collections/community.general/pull/4038 and https://github.com/ansible-collections/community.general/issues/4074).
- gitlab_project - add new option ``default_branch`` to gitlab_project (if ``readme = true``) (https://github.com/ansible-collections/community.general/pull/3792).
- gitlab_project_variable - new ``variables`` parameter (https://github.com/ansible-collections/community.general/issues/4038).
- hponcfg - revamped module using ModuleHelper (https://github.com/ansible-collections/community.general/pull/3840).
- icinga2 inventory plugin - added the ``display_name`` field to variables (https://github.com/ansible-collections/community.general/issues/3875, https://github.com/ansible-collections/community.general/pull/3906).
- icinga2 inventory plugin - implemented constructed interface (https://github.com/ansible-collections/community.general/pull/4088).
- icinga2 inventory plugin - inventory object names are changable using ``inventory_attr`` in your config file to the host object name, address, or display_name fields (https://github.com/ansible-collections/community.general/issues/3875, https://github.com/ansible-collections/community.general/pull/3906).
- ip_netns - calling ``run_command`` with arguments as ``list`` instead of ``str`` (https://github.com/ansible-collections/community.general/pull/3822).
- ipa_dnszone - ``dynamicupdate`` is now a boolean parameter, instead of a string parameter accepting ``"true"`` and ``"false"``. Also the module is now idempotent with respect to ``dynamicupdate`` (https://github.com/ansible-collections/community.general/pull/3374).
- ipa_dnszone - add DNS zone synchronization support (https://github.com/ansible-collections/community.general/pull/3374).
- ipa_service - add ``skip_host_check`` parameter. (https://github.com/ansible-collections/community.general/pull/4417).
- ipmi_boot - add support for user-specified IPMI encryption key (https://github.com/ansible-collections/community.general/issues/3698).
- ipmi_power - add ``machine`` option to ensure the power state via the remote target address (https://github.com/ansible-collections/community.general/pull/3968).
- ipmi_power - add support for user-specified IPMI encryption key (https://github.com/ansible-collections/community.general/issues/3698).
- iso_extract - calling ``run_command`` with arguments as ``list`` instead of ``str`` (https://github.com/ansible-collections/community.general/pull/3805).
- java_cert - calling ``run_command`` with arguments as ``list`` instead of ``str`` (https://github.com/ansible-collections/community.general/pull/3835).
- jira - add support for Bearer token auth (https://github.com/ansible-collections/community.general/pull/3838).
- jira - when creating a comment, ``fields`` now is used for additional data (https://github.com/ansible-collections/community.general/pull/4304).
- keycloak_* modules - added connection timeout parameter when calling server (https://github.com/ansible-collections/community.general/pull/4168).
- keycloak_client - add ``always_display_in_console`` parameter (https://github.com/ansible-collections/community.general/issues/4390).
- keycloak_client - add ``default_client_scopes`` and ``optional_client_scopes`` parameters. (https://github.com/ansible-collections/community.general/pull/4385).
- keycloak_user_federation - add sssd user federation support (https://github.com/ansible-collections/community.general/issues/3767).
- ldap_entry - add support for recursive deletion (https://github.com/ansible-collections/community.general/issues/3613).
- linode inventory plugin - add support for caching inventory results (https://github.com/ansible-collections/community.general/pull/4179).
- linode inventory plugin - allow templating of ``access_token`` variable in Linode inventory plugin (https://github.com/ansible-collections/community.general/pull/4040).
- listen_ports_facts - add support for ``ss`` command besides ``netstat`` (https://github.com/ansible-collections/community.general/pull/3708).
- lists_mergeby filter plugin - add parameters ``list_merge`` and ``recursive``. These are only supported when used with ansible-base 2.10 or ansible-core, but not with Ansible 2.9 (https://github.com/ansible-collections/community.general/pull/4058).
- logentries - calling ``run_command`` with arguments as ``list`` instead of ``str`` (https://github.com/ansible-collections/community.general/pull/3807).
- logstash_plugin - calling ``run_command`` with arguments as ``list`` instead of ``str`` (https://github.com/ansible-collections/community.general/pull/3808).
- lxc_container - added ``wait_for_container`` parameter. If ``true`` the module will wait until the running task reports success as the status (https://github.com/ansible-collections/community.general/pull/4039).
- lxc_container - calling ``run_command`` with arguments as ``list`` instead of ``str`` (https://github.com/ansible-collections/community.general/pull/3851).
- lxd connection plugin - make sure that ``ansible_lxd_host``, ``ansible_executable``, and ``ansible_lxd_executable`` work (https://github.com/ansible-collections/community.general/pull/3798).
- lxd inventory plugin - support virtual machines (https://github.com/ansible-collections/community.general/pull/3519).
- lxd_container - adds ``type`` option which also allows to operate on virtual machines and not just containers (https://github.com/ansible-collections/community.general/pull/3661).
- mail callback plugin - add ``Message-ID`` and ``Date`` headers (https://github.com/ansible-collections/community.general/issues/4055, https://github.com/ansible-collections/community.general/pull/4056).
- mail callback plugin - properly use Ansible's option handling to split lists (https://github.com/ansible-collections/community.general/pull/4140).
- mattermost - add the possibility to send attachments instead of text messages (https://github.com/ansible-collections/community.general/pull/3946).
- mksysb - revamped the module using ``ModuleHelper`` (https://github.com/ansible-collections/community.general/pull/3295).
- module_helper module utils - added decorators ``check_mode_skip`` and ``check_mode_skip_returns`` for skipping methods when ``check_mode=True`` (https://github.com/ansible-collections/community.general/pull/3849).
- monit - calling ``run_command`` with arguments as ``list`` instead of ``str`` (https://github.com/ansible-collections/community.general/pull/3821).
- nmcli - add ``wireguard`` connection type (https://github.com/ansible-collections/community.general/pull/3985).
- nmcli - add missing connection aliases ``802-3-ethernet`` and ``802-11-wireless`` (https://github.com/ansible-collections/community.general/pull/4108).
- nmcli - add multiple addresses support for ``ip4`` parameter (https://github.com/ansible-collections/community.general/issues/1088, https://github.com/ansible-collections/community.general/pull/3738).
- nmcli - add multiple addresses support for ``ip6`` parameter (https://github.com/ansible-collections/community.general/issues/1088).
- nmcli - add support for ``eui64`` and ``ipv6privacy`` parameters (https://github.com/ansible-collections/community.general/issues/3357).
- nmcli - adds ``routes6`` and ``route_metric6`` parameters for supporting IPv6 routes (https://github.com/ansible-collections/community.general/issues/4059).
- nmcli - remove nmcli modify dependency on ``type`` parameter (https://github.com/ansible-collections/community.general/issues/2858).
- npm - add ability to use ``production`` flag when ``ci`` is set (https://github.com/ansible-collections/community.general/pull/4299).
- open_iscsi - extended module to allow rescanning of established session for one or all targets (https://github.com/ansible-collections/community.general/issues/3763).
- opennebula - add the release action for VMs in the ``HOLD`` state (https://github.com/ansible-collections/community.general/pull/4036).
- opentelemetry_plugin - enrich service when using the ``docker_login`` (https://github.com/ansible-collections/community.general/pull/4104).
- opentelemetry_plugin - enrich service when using the ``jenkins``, ``hetzner`` or ``jira`` modules (https://github.com/ansible-collections/community.general/pull/4105).
- pacman - add ``remove_nosave`` parameter to avoid saving modified configuration files as ``.pacsave`` files. (https://github.com/ansible-collections/community.general/pull/4316, https://github.com/ansible-collections/community.general/issues/4315).
- pacman - add ``stdout`` and ``stderr`` as return values (https://github.com/ansible-collections/community.general/pull/3758).
- pacman - now implements proper change detection for ``update_cache=true``. Adds ``cache_updated`` return value to when ``update_cache=true`` to report this result independently of the module's overall changed return value (https://github.com/ansible-collections/community.general/pull/4337).
- pacman - the module has been rewritten and is now much faster when using ``state=latest``. Operations are now done all packages at once instead of package per package and the configured output format of ``pacman`` no longer affect the module's operation. (https://github.com/ansible-collections/community.general/pull/3907, https://github.com/ansible-collections/community.general/issues/3783, https://github.com/ansible-collections/community.general/issues/4079)
- passwordstore lookup plugin - add configurable ``lock`` and ``locktimeout`` options to avoid race conditions in itself and in the ``pass`` utility it calls. By default, the plugin now locks on write operations (https://github.com/ansible-collections/community.general/pull/4194).
- pipx - added options ``editable`` and ``pip_args`` (https://github.com/ansible-collections/community.general/issues/4300).
- proxmox - add ``clone`` parameter (https://github.com/ansible-collections/community.general/pull/3930).
- proxmox inventory plugin - add support for client-side jinja filters (https://github.com/ansible-collections/community.general/issues/3553).
- proxmox inventory plugin - add support for templating the ``url``, ``user``, and ``password`` options (https://github.com/ansible-collections/community.general/pull/4418).
- proxmox modules - move ``HAS_PROXMOXER`` check into ``module_utils`` (https://github.com/ansible-collections/community.general/pull/4030).
- proxmox modules - move common code into ``module_utils`` (https://github.com/ansible-collections/community.general/pull/4029).
- proxmox_kvm - added EFI disk support when creating VM with OVMF UEFI BIOS with new ``efidisk0`` option (https://github.com/ansible-collections/community.general/pull/4106, https://github.com/ansible-collections/community.general/issues/1638).
- proxmox_kwm - add ``win11`` to ``ostype`` parameter for Windows 11 and Windows Server 2022 support (https://github.com/ansible-collections/community.general/issues/4023, https://github.com/ansible-collections/community.general/pull/4191).
- puppet - remove deprecation for ``show_diff`` parameter. Its alias ``show-diff`` is still deprecated and will be removed in community.general 7.0.0 (https://github.com/ansible-collections/community.general/pull/3980).
- python_requirements_info - returns python version broken down into its components, and some minor refactoring (https://github.com/ansible-collections/community.general/pull/3797).
- redfish_command - add ``GetHostInterfaces`` command to enable reporting Redfish Host Interface information (https://github.com/ansible-collections/community.general/issues/3693).
- redfish_command - add ``SetHostInterface`` command to enable configuring the Redfish Host Interface (https://github.com/ansible-collections/community.general/issues/3632).
- redis - add authentication parameters ``login_user``, ``tls``, ``validate_certs``, and ``ca_certs`` (https://github.com/ansible-collections/community.general/pull/4207).
- scaleway inventory plugin - add profile parameter ``scw_profile`` (https://github.com/ansible-collections/community.general/pull/4049).
- scaleway_compute - add possibility to use project identifier (new ``project`` option) instead of deprecated organization identifier (https://github.com/ansible-collections/community.general/pull/3951).
- scaleway_volume - all volumes are systematically created on par1 (https://github.com/ansible-collections/community.general/pull/3964).
- snap - add option ``options`` permitting to set options using the ``snap set`` command (https://github.com/ansible-collections/community.general/pull/3943).
- sudoers - add support for ``runas`` parameter (https://github.com/ansible-collections/community.general/issues/4379).
- svc - calling ``run_command`` with arguments as ``list`` instead of ``str`` (https://github.com/ansible-collections/community.general/pull/3829).
- syslog_json - add option to skip logging of ``gather_facts`` playbook tasks; use v2 callback API (https://github.com/ansible-collections/community.general/pull/4223).
- xattr - calling ``run_command`` with arguments as ``list`` instead of ``str`` (https://github.com/ansible-collections/community.general/pull/3806).
- xfconf - minor refactor on the base class for the module (https://github.com/ansible-collections/community.general/pull/3919).
- zypper - add support for ``--clean-deps`` option to remove packages that depend on a package being removed (https://github.com/ansible-collections/community.general/pull/4195).

community.grafana
~~~~~~~~~~~~~~~~~

- community.grafana.grafana_datasource supports aws_auth_type of default.

community.hashi_vault
~~~~~~~~~~~~~~~~~~~~~

- The Filter guide has been added to the collection's docsite.

community.mysql
~~~~~~~~~~~~~~~

- Added explicit description of the supported versions of databases and connectors. Changes to the collection are **NOT** tested against database versions older than `mysql 5.7.31` and `mariadb 10.2.37` or connector versions older than `pymysql 0.7.10` and `mysqlclient 2.0.1`. (https://github.com/ansible-collections/community.mysql/discussions/141)
- mysql_user - added the ``force_context`` boolean option to set the default database context for the queries to be the ``mysql`` database. This way replication/binlog filters can catch the statements (https://github.com/ansible-collections/community.mysql/issues/265).

community.network
~~~~~~~~~~~~~~~~~

- community.network.ce_switchport - add support of decode a few stdout values from bitmap to human readable format(https://github.com/ansible-collections/community.network/issues/315)
- community.network.edgeos_config - append save command into result (https://github.com/ansible-collections/community.network/pull/189)

community.proxysql
~~~~~~~~~~~~~~~~~~

- module_utils - Refactor save_config_to_disk and load_config_to_runtime (https://github.com/ansible-collections/community.proxysql/pull/78).
- proxysql_mysql_users - Add missing ``no_log`` option to ``encrypt_password`` parameter (https://github.com/ansible-collections/community.proxysql/pull/86).

community.sap
~~~~~~~~~~~~~

- sapcar_extract.py - more strict logic for filenames

community.vmware
~~~~~~~~~~~~~~~~

- Remove `version_added` documentation that pre-dates the collection, that is refers to Ansible < 2.10 (https://github.com/ansible-collections/community.vmware/pull/1215).
- vmware_datastore_info - added show_tag parameters to allow datastore tags to be read in a uniform way across _info modules  (https://github.com/ansible-collections/community.vmware/pull/1085).
- vmware_export_ovf - Add a new parameter 'export_with_extraconfig' to support export extra config options in ovf (https://github.com/ansible-collections/community.vmware/pull/1161).
- vmware_guest_disk - Added a new key 'cluster_disk' which allows you to use a filename originating from a VM with an RDM.
- vmware_guest_disk - Added bus_sharing as an option for SCSI devices.
- vmware_guest_disk - Enabled the use of up to 64 disks on a paravirtual SCSI controller when the hardware is version 14 or higher.
- vmware_guest_sendkey - added additional USB scan codes for HOME and END.
- vmware_guest_storage_policy - New parameter `controller_number` to support multiple SCSI controllers (https://github.com/ansible-collections/community.vmware/issues/1203).
- vmware_host_scanhba - add rescan_vmfs parameter to allow rescaning for new VMFS volumes. Also add rescan_hba parameter with default true to allow for not rescaning HBAs as this might be very slow. (https://github.com/ansible-collections/community.vmware/issues/479)
- vmware_host_snmp - implement setting syscontact and syslocation (https://github.com/ansible-collections/community.vmware/issues/1044).
- vmware_object_role_permission - added VMware DV portgroup object_type for setting permissions (https://github.com/ansible-collections/community.vmware/pull/1176)
- vmware_rest_client module_util - added function get_tags_for_datastore for convenient tag collection (https://github.com/ansible-collections/community.vmware/pull/1085).
- vmware_vm_config_option - Fix the parameter not correct issue when hostname is set to ESXi host(https://github.com/ansible-collections/community.vmware/pull/1171).
- vmware_vm_info - Add the posibility to get the configuration informations of only one vm by name. (https://github.com/ansible-collections/community.vmware/pull/1241)
- vmware_vm_info - adding fact about ``datastore_url`` to output (https://github.com/ansible-collections/community.vmware/pull/1143).

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
- Add new options for pod module
- Add requires option to podman_container module
- Fix sanity issues with a new Ansible version
- Use yaml syntax highlighting where appropriate

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- idrac_redfish_storage_controller - This module is enhanced to support the following settings with check mode and idempotency - UnassignSpare, EnableControllerEncryption, BlinkTarget, UnBlinkTarget,  ConvertToRAID, ConvertToNonRAID, ChangePDStateToOnline, ChangePDStateToOffline.
- ome_application_network_address - The module is enhanced to support check mode and idempotency.
- ome_device_info - The module is enhanced to return a blank list when devices or baselines are not present in the system.
- ome_diagnostics - The module is enhanced to support check mode and idempotency. (https://github.com/dell/dellemc-openmanage-ansible-modules/issues/345)
- ome_diagnostics - This module is enhanced to extract log from lead chassis. (https://github.com/dell/dellemc-openmanage-ansible-modules/issues/310)
- ome_firmware - The module is enhanced to support check mode and idempotency (https://github.com/dell/dellemc-openmanage-ansible-modules/issues/274)
- ome_firmware_baseline_compliance_info - The module is enhanced to return a blank list when devices or baselines are not present in the system.
- ome_firmware_baseline_info - The module is enhanced to return a blank list when devices or baselines are not present in the system.
- ome_identity_pool - The iSCSI Initiator and Initiator IP Pool attributes are not mandatory to create an identity pool. (https://github.com/dell/dellemc-openmanage-ansible-modules/issues/329)
- ome_identity_pool - The module is enhanced to support check mode and idempotency. (https://github.com/dell/dellemc-openmanage-ansible-modules/issues/328)
- ome_profile - The module is enhanced to support check mode and idempotency.
- ome_profile - The module is enhanced to support modifying a profile based on the attribute names instead of the ID.
- ome_template - An example task is added to create a compliance template from reference device (https://github.com/dell/dellemc-openmanage-ansible-modules/issues/339)
- ome_template - The module is enhanced to support check mode and idempotency. (https://github.com/dell/dellemc-openmanage-ansible-modules/issues/255)
- ome_template - The module is enhanced to support modifying a template based on the attribute names instead of the ID. (https://github.com/dell/dellemc-openmanage-ansible-modules/issues/358)
- ome_template_identity_pool - The module is enhanced to support check mode and idempotency.
- redfish_event_subscription - The module is enhanced to support check mode and idempotency.

f5networks.f5_modules
~~~~~~~~~~~~~~~~~~~~~

- Added no_log=True to content parameters in bigip_ssl_key and bigip_ssl_key_cert module to stop key and cert content fomr being logged.
- bigip_device_info - Added a new meta choice, packages, which groups information about as3, do, cfe and ts. This change was done to ensure users with non admin access can use this module to get information that does not require admin access.
- bigip_device_info - added stats parameter for each virtual_server resource attached to a gtm_server
- bigip_device_info - this module can gather information about ucs backup files.
- bigip_pool_member - add checkmode bypass so that existence checks for pool is always returns true when using check mode
- bigip_profile_http_compression - Add content_type_include parameter to bigip_profile_fastl4 module

infoblox.nios_modules
~~~~~~~~~~~~~~~~~~~~~

- Added tags 'cloud' and 'networking' in 'galaxy.yaml'
- Following options are made required in the modules | Record | Option made required | | ------ | -------------------- | | A | ipv4addr | | AAAA | ipv6addr | | CNAME | canonical | | MX | mail_exchanger, preference | | PTR | ptrdname |
- Updated 'required' field in modules `#99 <https://github.com/infobloxopen/infoblox-ansible/pull/99>`_

inspur.sm
~~~~~~~~~

- Add the onboard_disk_info module.
- Modified logical disk Settings, added logical disk Settings for M6 PMC card.
- Modify the edit_pdisk function to add new parameters.
- The user module adds the mailbox field.

junipernetworks.junos
~~~~~~~~~~~~~~~~~~~~~

- Add junos_hostname resource module.
- Add junos_routing_options resource module.
- Add junos_snmp_server resource module.
- Added junos_security_policies module.
- Added junos_security_policies_global module.
- Added junos_security_zones module.
- Allow interfaces resource module to configure and gather logical interface description.

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

netapp.cloudmanager
~~~~~~~~~~~~~~~~~~~

- Add ``update_svm_password`` for ``svm_password`` update on AWS, AZURE and GCP CVOs. Update ``svm_password`` if ``update_svm_password`` is true.
- Add ontap image upgrade on AWS, AZURE and GCP CVOs if ``upgrade_ontap_version`` is true and ``ontap_version`` is provided with a specific version. ``use_latest_version`` has to be false.
- Add the description of client_id based on the cloudmanager UI.
- Set license_type default value 'capacity-paygo' for single node 'ha-capacity-paygo' for HA and 'capacity_package_name' value 'Essential'
- na_cloudmanager_connector_aws - automatically fetch client_id and instance_id for delete.
- na_cloudmanager_connector_aws - make the module idempotent for create and delete.
- na_cloudmanager_connector_aws - report client_id and instance_id if connector already exists.
- na_cloudmanager_connector_gcp - when using the user application default credential authentication by running the command gcloud auth application-default login, ``gcp_service_account_path`` is not needed.
- na_cloudmanager_cvo_aws - Support instance_type update
- na_cloudmanager_cvo_azure - Support instance_type update
- na_cloudmanager_cvo_gcp - Support instance_type update
- na_cloudmanager_info - new subsets - account_info, agents_info, active_agents_info
- na_cloudmanager_snapmirror - Add FSX to snapmirror.
- na_cloudmanager_volume - Report error if the volume properties cannot be modified. Add support ``tiering_policy`` and ``snapshot_policy_name`` modification.

netapp.ontap
~~~~~~~~~~~~

- all modules that only support ZAPI - warn when ``use_rest`` with a value of ``always`` is ignored.
- na_ontap_aggregate - Added REST support.
- na_ontap_aggregate - Added ``disk_class`` option for REST and ZAPI.
- na_ontap_aggregate - Extended accepted ``disk_type`` values for ZAPI.
- na_ontap_aggregate - new option ``encryption`` to enable encryption with ZAPI.
- na_ontap_broadcast_domain - Added REST support to the broadcast domain module.
- na_ontap_broadcast_domain - new REST only option ``from_ipspace`` added.
- na_ontap_broadcast_domain_ports - warn about deprecation, fall back to ZAPI or fail when REST is desired.
- na_ontap_cifs_acl - Added REST support to the cifs share access control module.
- na_ontap_cifs_acl - new option ``type`` for user-group-type.
- na_ontap_cifs_server - Added REST support to the cifs server module.
- na_ontap_cifs_share - Added REST support to the cifs share module.
- na_ontap_cluster_config role - use na_ontap_login_messages as na_ontap_motd is deprecated.
- na_ontap_cluster_peer - Added REST support to the cluster_peer module.
- na_ontap_debug - report ansible version and ONTAP collection version.
- na_ontap_efficiency_policy - Added REST support.
- na_ontap_export_policy_rule - new option ``ntfs_unix_security`` for NTFS export UNIX security options added.
- na_ontap_export_policy_rule -- Added Rest support for Export Policy Rules
- na_ontap_fcp -- Added REST support for FCP
- na_ontap_firmware_upgrade - REST support to download firmware and reboot SP.
- na_ontap_license - Added REST support to the license module.
- na_ontap_lun - Added REST support.
- na_ontap_lun_map - Added REST support.
- na_ontap_net_ifgrp - Added REST support to the net ifgrp module.
- na_ontap_net_ifgrp - new REST only options ``from_lag_ports``, ``broadcast_domain`` and ``ipspace`` added.
- na_ontap_net_port - Added REST support to the net port module
- na_ontap_nfs - Added Rest Support
- na_ontap_ports - Added REST support to the ports module.
- na_ontap_rest_info - update documention for `fields` to clarify the list of fields that are return by default.
- na_ontap_restit - new option ``wait_for_completion`` to support asynchronous operations and wait for job completion.
- na_ontap_snapmirror - Added REST support to the na_ontap_snapmirror module
- na_ontap_snapmirror -- Added more descriptive error messages for REST
- na_ontap_snapshot_policy - Added REST support to the na_ontap_snapshot_policy module.
- na_ontap_svm - add support for web services (ssl modify) - REST only with 9.8 or later.
- na_ontap_svm - new REST options of svm admin_state ``stopped`` and ``running`` added.
- na_ontap_volume - Added REST support to the volume module
- na_ontap_volume - ``logical_space_enforcement`` to specifies whether to perform logical space accounting on the volume.
- na_ontap_volume - ``logical_space_reporting`` to specifies whether to report space logically on the volume.
- na_ontap_volume - ``tiering_minimum_cooling_days`` to specify how many days must pass before inactive data in a volume using the Auto or Snapshot-Only policy is considered cold and eligible for tiering.
- na_ontap_volume - add support for SnapLock - only for REST.
- na_ontap_volume - allow to modify volume after rename.
- na_ontap_volume - new option ``max_files`` to increase the inode count value.
- na_ontap_volume_clone - Added REST support.
- na_ontap_volume_efficiency - new option ``storage_efficiency_mode`` for AFF only with 9.10.1 or later.
- na_ontap_vserver_create role - support max_volumes option.
- na_ontap_vserver_delete role - added set_fact to accept ``netapp_{hostname|username|password}`` or ``hostname,username and password`` variables.
- na_ontap_vserver_delete role - do not report an error if the vserver does not exist.
- na_ontap_vserver_peer - Added REST support to the vserver_peer module

netapp.storagegrid
~~~~~~~~~~~~~~~~~~

- PR2 - allow usage of Ansible module group defaults - for Ansible 2.12+.
- na_sg_grid_gateway - supports load balancer endpoint binding available in StorageGRID 11.5+.
- na_sg_grid_gateway - supports specifying HA Groups by name or UUID.
- na_sg_org_container - supports creation of S3 Object Lock buckets available in StorageGRID 11.5+.

netapp_eseries.santricity
~~~~~~~~~~~~~~~~~~~~~~~~~

- na_santricity_global - Add controller_shelf_id argument to set controller shelf identifier.
- na_santricity_volume - Add flag to control whether volume expansion operations are allowed.
- na_santricity_volume - Add volume write cache mirroring option.
- nar_santricity_host - Add volume write cache mirroring options.

netbox.netbox
~~~~~~~~~~~~~

- Add custom fields to modules missing it [#723](https://github.com/netbox-community/ansible_modules/pull/723)
- Add tags to modules missing it [#725](https://github.com/netbox-community/ansible_modules/pull/725)
- nb_inventory - Add a racks option [#701](https://github.com/netbox-community/ansible_modules/pull/701)
- nb_inventory - Add documentation for use of inventory plugin in Tower/AWX [#648](https://github.com/netbox-community/ansible_modules/pull/648)
- nb_inventory - Cache OpenAPI locally to speed up inventory [#617](https://github.com/netbox-community/ansible_modules/pull/617)
- nb_inventory - Pull extended inventory data for prefixes and site [#646](https://github.com/netbox-community/ansible_modules/pull/646)
- nb_lookup - Add endpoints for wireless (new in NetBox 3.1) [#673](https://github.com/netbox-community/ansible_modules/pull/673)
- nb_lookup - Add missing endpoints to nb_lookup [#655](https://github.com/netbox-community/ansible_modules/pull/655)
- netbox_cable - Improve lookup speed on NetBox versions earlier than 3.0.6 [#645](https://github.com/netbox-community/ansible_modules/pull/645)
- netbox_circuit_termination - Add mark_connected field to module [#686](https://github.com/netbox-community/ansible_modules/pull/686)
- netbox_contact, netbox_contact_group, netbox_contact_role - Add modules [#671](https://github.com/netbox-community/ansible_modules/pull/671)
- netbox_custom_field - Add module [#719](https://github.com/netbox-community/ansible_modules/pull/719)
- netbox_custom_link - Add module [#722](https://github.com/netbox-community/ansible_modules/pull/722)
- netbox_device_interface, netbox_vm_interface - Add bridge to netbox_device_interface and netbox_vm_interface [#713](https://github.com/netbox-community/ansible_modules/pull/713)
- netbox_export_template - Add module [#727](https://github.com/netbox-community/ansible_modules/pull/727)
- netbox_inventory_item - Add label and custom fields to module [#632](https://github.com/netbox-community/ansible_modules/pull/632)
- netbox_inventory_item - Add parent field to module [#682](https://github.com/netbox-community/ansible_modules/pull/682)
- netbox_provider_network - Add module for handling provider networks [#653](https://github.com/netbox-community/ansible_modules/pull/653)
- netbox_region - Add description, tags, custom_fields to module [#689](https://github.com/netbox-community/ansible_modules/pull/689)
- netbox_service - Add virtual_machine as an allowed query parameter for ipaddresses [#718](https://github.com/netbox-community/ansible_modules/pull/718)
- netbox_virtual_chassis - Add custom_fields to netbox_virtual_chassis [#657](https://github.com/netbox-community/ansible_modules/pull/657)
- netbox_vm_interface - Add custom fields to module [#637](https://github.com/netbox-community/ansible_modules/pull/637)
- netbox_webhook - Add module [#738](https://github.com/netbox-community/ansible_modules/pull/738)
- netbox_wireless_lan, netbox_wireless_lan_group, netbox_wireless_link - Add modules [#678](https://github.com/netbox-community/ansible_modules/pull/678)

openvswitch.openvswitch
~~~~~~~~~~~~~~~~~~~~~~~

- Allows read operation in openvswitch_db module(https://github.com/ansible-collections/openvswitch.openvswitch/pull/88)
- openvswitch modules got support for database socket parameter.

ovirt.ovirt
~~~~~~~~~~~

- Add json_query filter (https://github.com/oVirt/ovirt-ansible-collection/pull/436).
- cluster_upgrade - Add progress tracking via event logs to the role (https://github.com/oVirt/ovirt-ansible-collection/pull/415)
- cluster_upgrade - Directly log progress to the cluster (https://github.com/oVirt/ovirt-ansible-collection/pull/449)
- engine_setup - Honor ovirt_engine_setup_offline variable (https://github.com/oVirt/ovirt-ansible-collection/pull/381).
- engine_setup - Prepare answer files and default values for 4.5 release (https://github.com/oVirt/ovirt-ansible-collection/pull/414).
- gluster_heal_info - Replacing gluster module to CLI to support RHV automation hub (https://github.com/oVirt/ovirt-ansible-collection/pull/340).
- hosted_engine - Replace virt_net and xml with commands (https://github.com/oVirt/ovirt-ansible-collection/pull/359).
- hosted_engine_setup - Fix default gateway variable name (https://github.com/oVirt/ovirt-ansible-collection/pull/423).
- hosted_engine_setup - Fix permissions on copied engine logs, needed for OpenSCAP (https://github.com/oVirt/ovirt-ansible-collection/pull/404).
- hosted_engine_setup - Honor he_offline_deployment variable (https://github.com/oVirt/ovirt-ansible-collection/pull/380).
- hosted_engine_setup - Replace calls to psql as postgres with engine_psql.sh (https://github.com/oVirt/ovirt-ansible-collection/pull/453).
- hosted_engine_setup - configured abrt initial files only when needed (https://github.com/oVirt/ovirt-ansible-collection/pull/397).
- info - Rename follows to follow parameter and add alias (https://github.com/oVirt/ovirt-ansible-collection/pull/367).
- info - bump deprecate version for fetch_nested and nested_attributes (https://github.com/oVirt/ovirt-ansible-collection/pull/378).
- info modules - Add follow link url to api model links_summary
- info modules - Enable follow parameter (https://github.com/oVirt/ovirt-ansible-collection/pull/355).
- manageiq - add deprecation info (https://github.com/oVirt/ovirt-ansible-collection/pull/384).
- ovirt_disk - Add warning for disk attachments (https://github.com/oVirt/ovirt-ansible-collection/pull/347).
- ovirt_disk - Use imageio client (https://github.com/oVirt/ovirt-ansible-collection/pull/358).
- ovirt_event - enable correlation_id on events (https://github.com/oVirt/ovirt-ansible-collection/pull/368).
- ovirt_host - Add enroll_certificate (https://github.com/oVirt/ovirt-ansible-collection/pull/439).
- ovirt_permission - add mac pool (https://github.com/oVirt/ovirt-ansible-collection/pull/353).
- ovirt_remove_stale_lun - Allow user to remove multiple LUNs (https://github.com/oVirt/ovirt-ansible-collection/pull/357).
- ovirt_remove_stale_lun - Retry "multipath -f" while removing the LUNs (https://github.com/oVirt/ovirt-ansible-collection/pull/382).
- ovirt_remove_stale_lun - Use add_host instead of delegate_to (https://github.com/oVirt/ovirt-ansible-collection/pull/390).
- ovirt_storage_template_info - fix docs (https://github.com/oVirt/ovirt-ansible-collection/pull/356).
- ovirt_storage_vm_info - fix docs (https://github.com/oVirt/ovirt-ansible-collection/pull/356).
- ovirt_template - Add ova import of template (https://github.com/oVirt/ovirt-ansible-collection/pull/304).
- ovirt_template - add boot_menu and bios_type https://github.com/oVirt/ovirt-ansible-collection/pull/465).
- ovirt_vm - Add display file_transfer_enabled and copy_paste_enabled (https://github.com/oVirt/ovirt-ansible-collection/pull/339).
- ovirt_vm - Add virtio_scsi_enabled and multi_queues_enabled (https://github.com/oVirt/ovirt-ansible-collection/pull/348).
- ovirt_vm - Add virtio_scsi_multi_queues (https://github.com/oVirt/ovirt-ansible-collection/pull/373).
- plugins - Remove unused imports (https://github.com/oVirt/ovirt-ansible-collection/pull/444).
- repositories - Add to the documentation variable priority (https://github.com/oVirt/ovirt-ansible-collection/pull/440).
- repositories - Replace redhat_subscription and rhsm_repository with command (https://github.com/oVirt/ovirt-ansible-collection/pull/346).
- repositories - Update host and engine repositories to 4.4.9 (https://github.com/oVirt/ovirt-ansible-collection/pull/363).
- repositories - add no_log to register (https://github.com/oVirt/ovirt-ansible-collection/pull/350).
- repositories - add satelite support (https://github.com/oVirt/ovirt-ansible-collection/pull/431).
- vm_infra - Add no_log to Manage VMs state task (https://github.com/oVirt/ovirt-ansible-collection/pull/417).

purestorage.flasharray
~~~~~~~~~~~~~~~~~~~~~~

- All modules - Change examples to use FQCN for module
- purefa_admin - New module to set global admin settings, inclusing SSO
- purefa_dirsnap - Add support to rename directory snapshots not managed by a snapshot policy
- purefa_info - Add SAML2SSO configutration information
- purefa_info - Add Safe Mode status
- purefa_info - Fix Active Directory configuration details
- purefa_network - Resolve bug stopping management IP address being changed correctly
- purefa_offload - Add support for multiple, homogeneous, offload targets
- purefa_saml - Add support for SAML2 SSO IdPs
- purefa_volume - Provide volume facts in all cases, including when no change has occured.

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
- Added argument remote_on inside bonsai_asset module

t_systems_mms.icinga_director
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Add Icinga scheduled downtime module (https://github.com/T-Systems-MMS/ansible-collection-icinga-director/pull/146)
- Add possibility to use Compose and keyed groups in inventory-module (https://github.com/T-Systems-MMS/ansible-collection-icinga-director/pull/155)
- Added missing fields to 'icinga_host' and 'icinga_host_template' (https://github.com/T-Systems-MMS/ansible-collection-icinga-director/pull/158)
- add option to append arguments to all modules (https://github.com/T-Systems-MMS/ansible-collection-icinga-director/pull/153)

theforeman.foreman
~~~~~~~~~~~~~~~~~~

- Add a role `convert2rhel` to perform setup for converting systems to RHEL
- Warn if the user tries to use a plain HTTP server URL and fail if the URL is neither HTTPS nor HTTP.
- content_upload - add support for OSTree content uploads (https://github.com/theforeman/foreman-ansible-modules/issues/628, https://projects.theforeman.org/issues/33299)
- inventory plugin - enable certificate validation by default
- new ``auth_sources_ldap`` role to manage LDAP authentication sources
- new ``compute_profiles`` role to manage compute profiles
- new ``compute_resources`` role to manage compute resources
- new ``content_view_publish`` role to publish a list of content views (https://github.com/theforeman/foreman-ansible-modules/issues/1209)
- new ``domains`` role to manage domains
- new ``operatingsystems`` role to manage operating systems
- new ``provisioning_templates`` role to manage provisioning templates
- new ``settings`` role to manage settings
- new ``subnets`` role to manage subnets
- os_default_template, provisioning_template - add ``host_init_config`` to list of possible template types
- repository - add ``arch`` parameter to limit architectures of the repository (https://github.com/theforeman/foreman-ansible-modules/issues/1265)
- repository - new ``download_concurrency`` parameter (https://github.com/theforeman/foreman-ansible-modules/issues/1273)

vyos.vyos
~~~~~~~~~

- Add vyos_hostname resource module.
- Add vyos_snmp_server resource module.
- Rename V4-EGRESS/V6-EGRESS to EGRESS in the tests to test the same-name situation
- Update vyos_facts to support IPv4 and IPv6 rule sets having the same name
- Update vyos_firewall_rules to support IPv4 and IPv6 rule sets having the same name
- vyos_firewall_rules - Add support for log enable on individual rules
- vyos_firewall_rules - fixed incorrect option 'disabled' passed to the rules.

Breaking Changes / Porting Guide
--------------------------------

Ansible-core
~~~~~~~~~~~~

- Module Python Dependency - Drop support for Python 2.6 in module execution.
- Templating - it is no longer allowed to perform arithmetic and concatenation operations outside of the jinja template (https://github.com/ansible/ansible/pull/75587)
- The ``finalize`` method is no longer exposed in the globals for use in templating.

amazon.aws
~~~~~~~~~~

- aws_caller_facts - Remove deprecated ``aws_caller_facts`` alias.  Please use ``aws_caller_info`` instead.
- cloudformation_facts - Remove deprecated ``cloudformation_facts`` alias.  Please use ``cloudformation_info`` instead.
- ec2_ami_facts - Remove deprecated ``ec2_ami_facts`` alias.  Please use ``ec2_ami_info`` instead.
- ec2_eni_facts - Remove deprecated ``ec2_eni_facts`` alias.  Please use ``ec2_eni_info`` instead.
- ec2_group_facts - Remove deprecated ``ec2_group_facts`` alias.  Please use ``ec2_group_info`` instead.
- ec2_instance_facts - Remove deprecated ``ec2_instance_facts`` alias.  Please use ``ec2_instance_info`` instead.
- ec2_snapshot_facts - Remove deprecated ``ec2_snapshot_facts`` alias.  Please use ``ec2_snapshot_info`` instead.
- ec2_vol_facts - Remove deprecated ``ec2_vol_facts`` alias.  Please use ``ec2_vol_info`` instead.
- ec2_vpc_dhcp_option_facts - Remove deprecated ``ec2_vpc_dhcp_option_facts`` alias.  Please use ``ec2_vpc_dhcp_option_info`` instead.
- ec2_vpc_endpoint_facts - Remove deprecated ``ec2_vpc_endpoint_facts`` alias.  Please use ``ec2_vpc_endpoint_info`` instead.
- ec2_vpc_igw_facts - Remove deprecated ``ec2_vpc_igw_facts`` alias.  Please use ``ec2_vpc_igw_info`` instead.
- ec2_vpc_nat_gateway_facts - Remove deprecated ``ec2_vpc_nat_gateway_facts`` alias.  Please use ``ec2_vpc_nat_gateway_info`` instead.
- ec2_vpc_net_facts - Remove deprecated ``ec2_vpc_net_facts`` alias.  Please use ``ec2_vpc_net_info`` instead.
- ec2_vpc_route_table_facts - Remove deprecated ``ec2_vpc_route_table_facts`` alias.  Please use ``ec2_vpc_route_table_info`` instead.
- ec2_vpc_subnet_facts - Remove deprecated ``ec2_vpc_subnet_facts`` alias.  Please use ``ec2_vpc_subnet_info`` instead.

arista.eos
~~~~~~~~~~

- eos_command - new suboption ``version`` of parameter ``command``, which controls the JSON response version. Previously the value was assumed to be "latest" for network_cli and "1" for httpapi, but the default will now be "latest" for both connections. This option is also available for use in modules making their own device requests with ``plugins.module_utils.network.eos.eos.run_commands()`` with the same new default behavior. (https://github.com/ansible-collections/arista.eos/pull/258).

community.aws
~~~~~~~~~~~~~

- aws_acm_facts -  Remove deprecated alias ``aws_acm_facts``.  Please use ``aws_acm_info`` instead.
- aws_kms_facts -  Remove deprecated alias ``aws_kms_facts``.  Please use ``aws_kms_info`` instead.
- aws_kms_info - Deprecated ``keys_attr`` field is now ignored (https://github.com/ansible-collections/community.aws/pull/838).
- aws_region_facts -  Remove deprecated alias ``aws_region_facts``.  Please use ``aws_region_info`` instead.
- aws_s3_bucket_facts -  Remove deprecated alias ``aws_s3_bucket_facts``.  Please use ``aws_s3_bucket_info`` instead.
- aws_sgw_facts -  Remove deprecated alias ``aws_sgw_facts``.  Please use ``aws_sgw_info`` instead.
- aws_waf_facts -  Remove deprecated alias ``aws_waf_facts``.  Please use ``aws_waf_info`` instead.
- cloudfront_facts -  Remove deprecated alias ``cloudfront_facts``.  Please use ``cloudfront_info`` instead.
- cloudwatchlogs_log_group_facts -  Remove deprecated alias ``cloudwatchlogs_log_group_facts``.  Please use ``cloudwatchlogs_log_group_info`` instead.
- dynamodb_table - deprecated updates currently ignored for primary keys and global_all indexes will now result in a failure. (https://github.com/ansible-collections/community.aws/pull/837).
- ec2_asg_facts -  Remove deprecated alias ``ec2_asg_facts``.  Please use ``ec2_asg_info`` instead.
- ec2_customer_gateway_facts -  Remove deprecated alias ``ec2_customer_gateway_facts``.  Please use ``ec2_customer_gateway_info`` instead.
- ec2_eip_facts -  Remove deprecated alias ``ec2_eip_facts``.  Please use ``ec2_eip_info`` instead.
- ec2_elb_facts -  Remove deprecated alias ``ec2_elb_facts``.  Please use ``ec2_elb_info`` instead.
- ec2_elb_info -  The ``ec2_elb_info`` module has been removed.  Please use ``the ``elb_classic_lb_info`` module.
- ec2_lc_facts -  Remove deprecated alias ``ec2_lc_facts``.  Please use ``ec2_lc_info`` instead.
- ec2_placement_group_facts -  Remove deprecated alias ``ec2_placement_group_facts``.  Please use ``ec2_placement_group_info`` instead.
- ec2_vpc_nacl_facts -  Remove deprecated alias ``ec2_vpc_nacl_facts``.  Please use ``ec2_vpc_nacl_info`` instead.
- ec2_vpc_peering_facts -  Remove deprecated alias ``ec2_vpc_peering_facts``.  Please use ``ec2_vpc_peering_info`` instead.
- ec2_vpc_route_table_facts -  Remove deprecated alias ``ec2_vpc_route_table_facts``.  Please use ``ec2_vpc_route_table_info`` instead.
- ec2_vpc_vgw_facts -  Remove deprecated alias ``ec2_vpc_vgw_facts``.  Please use ``ec2_vpc_vgw_info`` instead.
- ec2_vpc_vpn_facts -  Remove deprecated alias ``ec2_vpc_vpn_facts``.  Please use ``ec2_vpc_vpn_info`` instead.
- ecs_service_facts -  Remove deprecated alias ``ecs_service_facts``.  Please use ``ecs_service_info`` instead.
- ecs_taskdefinition_facts -  Remove deprecated alias ``ecs_taskdefinition_facts``.  Please use ``ecs_taskdefinition_info`` instead.
- efs_facts -  Remove deprecated alias ``efs_facts``.  Please use ``efs_info`` instead.
- elasticache_facts -  Remove deprecated alias ``elasticache_facts``.  Please use ``elasticache_info`` instead.
- elb_application_lb_facts -  Remove deprecated alias ``elb_application_lb_facts``.  Please use ``elb_application_lb_info`` instead.
- elb_classic_lb_facts -  Remove deprecated alias ``elb_classic_lb_facts``.  Please use ``elb_classic_lb_info`` instead.
- elb_target_facts -  Remove deprecated alias ``elb_target_facts``.  Please use ``elb_target_info`` instead.
- elb_target_group_facts -  Remove deprecated alias ``elb_target_group_facts``.  Please use ``elb_target_group_info`` instead.
- iam - Removed deprecated ``community.aws.iam`` module. Please use ``community.aws.iam_user``, ``community.aws.iam_access_key`` or ``community.aws.iam_group`` (https://github.com/ansible-collections/community.aws/pull/839).
- iam_cert_facts -  Remove deprecated alias ``iam_cert_facts``.  Please use ``iam_cert_info`` instead.
- iam_mfa_device_facts -  Remove deprecated alias ``iam_mfa_device_facts``.  Please use ``iam_mfa_device_info`` instead.
- iam_role_facts -  Remove deprecated alias ``iam_role_facts``.  Please use ``iam_role_info`` instead.
- iam_server_certificate_facts -  Remove deprecated alias ``iam_server_certificate_facts``.  Please use ``iam_server_certificate_info`` instead.
- lambda_facts -  Remove deprecated module lambda_facts``.  Please use ``lambda_info`` instead.
- rds - Removed deprecated ``community.aws.rds`` module. Please use ``community.aws.rds_instance`` (https://github.com/ansible-collections/community.aws/pull/839).
- rds_instance_facts -  Remove deprecated alias ``rds_instance_facts``.  Please use ``rds_instance_info`` instead.
- rds_snapshot_facts -  Remove deprecated alias ``rds_snapshot_facts``.  Please use ``rds_snapshot_info`` instead.
- redshift_facts -  Remove deprecated alias ``redshift_facts``.  Please use ``redshift_info`` instead.
- route53_facts -  Remove deprecated alias ``route53_facts``.  Please use ``route53_info`` instead.

community.mysql
~~~~~~~~~~~~~~~

- mysql_replication - remove ``Is_Slave`` and ``Is_Master`` return values (were replaced with ``Is_Primary`` and ``Is_Replica`` (https://github.com/ansible-collections    /community.mysql/issues/145).
- mysql_replication - remove the mode options values containing ``master``/``slave`` and the master_use_gtid option ``slave_pos`` (were replaced with corresponding ``primary``/``replica`` values) (https://github.com/ansible-collections/community.mysql/issues/145).
- mysql_user - remove support for the `REQUIRESSL` special privilege as it has ben superseded by the `tls_requires` option (https://github.com/ansible-collections/community.mysql/discussions/121).
- mysql_user - validate privileges using database engine directly (https://github.com/ansible-collections/community.mysql/issues/234 https://github.com/ansible-collections/community.mysql/pull/243). Do not validate privileges in this module anymore.

community.vmware
~~~~~~~~~~~~~~~~

- The collection now requires at least ansible-core 2.11.0. Ansible 3 and before, and ansible-base versions are no longer supported.
- vmware_cluster_drs - The default for ``enable`` has been changed from ``false`` to ``true``.
- vmware_cluster_drs - The parameter alias ``enable_drs`` has been removed, use ``enable`` instead.
- vmware_cluster_ha - The default for ``enable`` has been changed from ``false`` to ``true``.
- vmware_cluster_ha - The parameter alias ``enable_ha`` has been removed, use ``enable`` instead.
- vmware_cluster_vsan - The default for ``enable`` has been changed from ``false`` to ``true``.
- vmware_cluster_vsan - The parameter alias ``enable_vsan`` has been removed, use ``enable`` instead.
- vmware_guest - Virtualization Based Security has some requirements (``nested_virt``, ``secure_boot`` and ``iommu``) that the module silently enabled. They have to be enabled explicitly now.

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- HTTPS SSL certificate validation is a **breaking change** and will require modification in the existing playbooks. Please refer to `SSL Certificate Validation <https://github.com/dell/dellemc-openmanage-ansible-modules#ssl-certificate-validation>`_ section in the `README.md <https://github.com/dell/dellemc-openmanage-ansible-modules/blob/collections/README.md#SSL-Certificate-Validation>`_ for modification to existing playbooks.

theforeman.foreman
~~~~~~~~~~~~~~~~~~

- Set use_reports_api default value to true for the inventory plugin
- Support for Ansible 2.8 is removed

Deprecated Features
-------------------

Ansible-core
~~~~~~~~~~~~

- ansible-core - Remove support for Python 2.6.
- ansible-test - Remove support for Python 2.6.
- ssh connection plugin option scp_if_ssh in favor of ssh_transfer_method.

amazon.aws
~~~~~~~~~~

- ec2_instance - The default value for ```instance_type``` has been deprecated, in the future release you must set an instance_type or a launch_template (https://github.com/ansible-collections/amazon.aws/pull/587).
- module_utils - support for the original AWS SDK `boto` has been deprecated in favour of the `boto3`/`botocore` SDK. All `boto` based modules have either been deprecated or migrated to `botocore`, and the remaining support code in module_utils will be removed in release 4.0.0 of the amazon.aws collection. Any modules outside of the amazon.aws and community.aws collections based on the `boto` library will need to be migrated to the `boto3`/`botocore` libraries (https://github.com/ansible-collections/amazon.aws/pull/575).

cisco.ios
~~~~~~~~~

- Deprecates lldp module.
- `ios_acls` - Deprecated fragment attribute added boolean alternate as enable_fragment.

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

- mail callback plugin - not specifying ``sender`` is deprecated and will be disallowed in community.general 6.0.0 (https://github.com/ansible-collections/community.general/pull/4140).
- module_helper module utils - deprecated the attribute ``ModuleHelper.VarDict`` (https://github.com/ansible-collections/community.general/pull/3801).
- pacman - from community.general 5.0.0 on, the ``changed`` status of ``update_cache`` will no longer be ignored if ``name`` or ``upgrade`` is specified. To keep the old behavior, add something like ``register: result`` and ``changed_when: result.packages | length > 0`` to your task (https://github.com/ansible-collections/community.general/pull/4329).

community.hashi_vault
~~~~~~~~~~~~~~~~~~~~~

- Support for Ansible 2.9 and ansible-base 2.10 is deprecated, and will be removed in the next major release (community.hashi_vault 3.0.0) next spring (https://github.com/ansible-community/community-topics/issues/50, https://github.com/ansible-collections/community.hashi_vault/issues/189).
- aws_iam_login auth method - the ``aws_iam_login`` method has been renamed to ``aws_iam``. The old name will be removed in collection version ``3.0.0``. Until then both names will work, and a warning will be displayed when using the old name (https://github.com/ansible-collections/community.hashi_vault/pull/193).

junipernetworks.junos
~~~~~~~~~~~~~~~~~~~~~

- 'router_id' options is deprecated from junos_ospf_interfaces, junos_ospfv2 and junos_ospfv3 resuorce module.

purestorage.flasharray
~~~~~~~~~~~~~~~~~~~~~~

- purefa_sso - Deprecated in favor of M(purefa_admin). Will be removed in Collection 2.0

Removed Features (previously deprecated)
----------------------------------------

Ansible-core
~~~~~~~~~~~~

- Remove deprecated ``Templar.set_available_variables()`` method (https://github.com/ansible/ansible/issues/75828)
- cli - remove deprecated ability to set verbosity before the sub-command (https://github.com/ansible/ansible/issues/75823)
- copy - remove deprecated ``thirsty`` alias (https://github.com/ansible/ansible/issues/75824)
- psrp - Removed fallback on ``put_file`` with older ``pypsrp`` versions. Users must have at least ``pypsrp>=0.4.0``.
- url_argument_spec - remove deprecated ``thirsty`` alias for ``get_url`` and ``uri`` modules (https://github.com/ansible/ansible/issues/75825, https://github.com/ansible/ansible/issues/75826)

community.hashi_vault
~~~~~~~~~~~~~~~~~~~~~

- the "legacy" integration test setup has been removed; this does not affect end users and is only relevant to contributors (https://github.com/ansible-collections/community.hashi_vault/pull/191).

community.vmware
~~~~~~~~~~~~~~~~

- vcenter_extension_facts - The deprecated module ``vcenter_extension_facts`` has been removed, use ``vcenter_extension_info`` instead.
- vmware_about_facts - The deprecated module ``vmware_about_facts`` has been removed, use ``vmware_about_info`` instead.
- vmware_category_facts - The deprecated module ``vmware_category_facts`` has been removed, use ``vmware_category_info`` instead.
- vmware_cluster - Remove DRS configuration in favour of module ``vmware_cluster_drs``.
- vmware_cluster - Remove HA configuration in favour of module ``vmware_cluster_ha``.
- vmware_cluster - Remove VSAN configuration in favour of module ``vmware_cluster_vsan``.
- vmware_cluster_facts - The deprecated module ``vmware_cluster_facts`` has been removed, use ``vmware_cluster_info`` instead.
- vmware_datastore_facts - The deprecated module ``vmware_datastore_facts`` has been removed, use ``vmware_datastore_info`` instead.
- vmware_drs_group_facts - The deprecated module ``vmware_drs_group_facts`` has been removed, use ``vmware_drs_group_info`` instead.
- vmware_drs_rule_facts - The deprecated module ``vmware_drs_rule_facts`` has been removed, use ``vmware_drs_rule_info`` instead.
- vmware_dvs_portgroup - The deprecated parameter ``portgroup_type`` has been removed, use ``port_binding`` instead.
- vmware_dvs_portgroup_facts - The deprecated module ``vmware_dvs_portgroup_facts`` has been removed, use ``vmware_dvs_portgroup_info`` instead.
- vmware_guest_boot_facts - The deprecated module ``vmware_guest_boot_facts`` has been removed, use ``vmware_guest_boot_info`` instead.
- vmware_guest_customization_facts - The deprecated module ``vmware_guest_customization_facts`` has been removed, use ``vmware_guest_customization_info`` instead.
- vmware_guest_disk_facts - The deprecated module ``vmware_guest_disk_facts`` has been removed, use ``vmware_guest_disk_info`` instead.
- vmware_guest_facts - The deprecated module ``vmware_guest_facts`` has been removed, use ``vmware_guest_info`` instead.
- vmware_guest_snapshot_facts - The deprecated module ``vmware_guest_snapshot_facts`` has been removed, use ``vmware_guest_snapshot_info`` instead.
- vmware_host_capability_facts - The deprecated module ``vmware_host_capability_facts`` has been removed, use ``vmware_host_capability_info`` instead.
- vmware_host_config_facts - The deprecated module ``vmware_host_config_facts`` has been removed, use ``vmware_host_config_info`` instead.
- vmware_host_dns_facts - The deprecated module ``vmware_host_dns_facts`` has been removed, use ``vmware_host_dns_info`` instead.
- vmware_host_feature_facts - The deprecated module ``vmware_host_feature_facts`` has been removed, use ``vmware_host_feature_info`` instead.
- vmware_host_firewall_facts - The deprecated module ``vmware_host_firewall_facts`` has been removed, use ``vmware_host_firewall_info`` instead.
- vmware_host_ntp_facts - The deprecated module ``vmware_host_ntp_facts`` has been removed, use ``vmware_host_ntp_info`` instead.
- vmware_host_package_facts - The deprecated module ``vmware_host_package_facts`` has been removed, use ``vmware_host_package_info`` instead.
- vmware_host_service_facts - The deprecated module ``vmware_host_service_facts`` has been removed, use ``vmware_host_service_info`` instead.
- vmware_host_ssl_facts - The deprecated module ``vmware_host_ssl_facts`` has been removed, use ``vmware_host_ssl_info`` instead.
- vmware_host_vmhba_facts - The deprecated module ``vmware_host_vmhba_facts`` has been removed, use ``vmware_host_vmhba_info`` instead.
- vmware_host_vmnic_facts - The deprecated module ``vmware_host_vmnic_facts`` has been removed, use ``vmware_host_vmnic_info`` instead.
- vmware_local_role_facts - The deprecated module ``vmware_local_role_facts`` has been removed, use ``vmware_local_role_info`` instead.
- vmware_local_user_facts - The deprecated module ``vmware_local_user_facts`` has been removed, use ``vmware_local_user_info`` instead.
- vmware_portgroup_facts - The deprecated module ``vmware_portgroup_facts`` has been removed, use ``vmware_portgroup_info`` instead.
- vmware_resource_pool_facts - The deprecated module ``vmware_resource_pool_facts`` has been removed, use ``vmware_resource_pool_info`` instead.
- vmware_tag_facts - The deprecated module ``vmware_tag_facts`` has been removed, use ``vmware_tag_info`` instead.
- vmware_target_canonical_facts - The deprecated module ``vmware_target_canonical_facts`` has been removed, use ``vmware_target_canonical_info`` instead.
- vmware_vm_facts - The deprecated module ``vmware_vm_facts`` has been removed, use ``vmware_vm_info`` instead.
- vmware_vmkernel_facts - The deprecated module ``vmware_vmkernel_facts`` has been removed, use ``vmware_vmkernel_info`` instead.
- vmware_vmkernel_ip_config - The deprecated module ``vmware_vmkernel_ip_config`` has been removed, use ``vmware_vmkernel`` instead.
- vmware_vswitch_facts - The deprecated module ``vmware_vswitch_facts`` has been removed, use ``vmware_vswitch_info`` instead.

Security Fixes
--------------

Ansible-core
~~~~~~~~~~~~

- Do not include params in exception when a call to ``set_options`` fails. Additionally, block the exception that is returned from being displayed to stdout. (CVE-2021-3620)

Bugfixes
--------

Ansible-core
~~~~~~~~~~~~

- Add a YAML representer for ``NativeJinjaText``
- Add a YAML representer for ``NativeJinjaUnsafeText``
- AnsiballZ - Ensure we use the full python package in the module cache filename to avoid a case where ``collections:`` is used to execute a module via short name, where the short name duplicates another module from ``ansible.builtin`` or another collection that was executed previously.
- Ansible.ModuleUtils.LinkUtil - Ignore the ``LIB`` environment variable when loading the ``LinkUtil`` code
- Ansible.ModuleUtils.SID - Use user principal name as is for lookup in the ``Convert-ToSID`` function - https://github.com/ansible/ansible/issues/77316
- Detect package manager for Amazon Linux 2022 (AL2022) as dnf
- Ensure the correct ``environment_class`` is set on ``AnsibleJ2Template``
- Fix ``AttributeError`` when providing password file via ``--connection-password-file`` (https://github.com/ansible/ansible/issues/76530)
- Fix ``end_play`` to end the current play only (https://github.com/ansible/ansible/issues/76672)
- Fix collection filter/test plugin redirects (https://github.com/ansible/ansible/issues/77192).
- Fix executing includes in the always section in the free strategy (https://github.com/ansible/ansible/issues/75642)
- Fix for when templating empty template file resulted in file with string 'None' (https://github.com/ansible/ansible/issues/76610)
- Fix help message for the 'ansible-galaxy collection verify' positional argument. The positional argument must be a collection name (https://github.com/ansible/ansible/issues/76087).
- Fix module logging issue when using custom module on WSL2 (https://github.com/ansible/ansible/issues/76320)
- Fix task debugger to work with ``run_once`` using ``linear`` strategy (https://github.com/ansible/ansible/issues/76049)
- Fix traceback when installing a collection from a git repository and git is not installed (https://github.com/ansible/ansible/issues/77479).
- Interpreter Discovery - Fallback to OS family if the distro is not found in ``INTERPRETER_PYTHON_DISTRO_MAP`` (https://github.com/ansible/ansible/issues/75560)
- Interpreter discovery - Add ``RHEL`` to ``OS_FAMILY_MAP`` for correct family fallback for interpreter discovery (https://github.com/ansible/ansible/issues/77368)
- Make include_role/include_tasks work with any_errors_fatal (https://github.com/ansible/ansible/issues/50897)
- Parser errors from within includes should not be rescueable (https://github.com/ansible/ansible/issues/73657)
- Templating - Ensure we catch exceptions when getting ``.filters`` and ``.tests`` attributes on their respective plugins and properly error, instead of aborting which results in no filters being added to the jinja2 environment
- Trigger an undefined error when an undefined variable is detected within a dictionary and/or list (https://github.com/ansible/ansible/pull/75587)
- _run_loop - Add the task name to the warning (https://github.com/ansible/ansible/issues/76011)
- ``Templar.copy_with_new_env`` - set the ``finalize`` method of the new ``Templar`` object for the new environment (https://github.com/ansible/ansible/issues/76379)
- add_host/group_by: fix using changed_when in a loop (https://github.com/ansible/ansible/issues/71627)
- ansible-config avoid showing _terms and _input when --only-changed.
- ansible-doc - Fix ansible-doc -l ansible.builtin / ansible.legacy not returning anything
- ansible-doc - ignore plugin deprecation warnings (https://github.com/ansible/ansible/issues/75671)
- ansible-galaxy - Add galaxy_collection_skeleton/galaxy_collection_skeleton_ignore configuration options
- ansible-galaxy - Fix using the '--ignore-certs' option when there is no server-specific configuration for the Galaxy server.
- ansible-galaxy - installing/downloading collections with invalid versions in git repositories and directories now gives a formatted error message (https://github.com/ansible/ansible/issues/76425, https://github.com/ansible/ansible/issues/75404).
- ansible-galaxy - when installing a role properly raise an error when inaccessible path is specified multiple times in roles_path (e.g. via environment variable and command line option) (https://github.com/ansible/ansible/issues/76316)
- ansible-galaxy collection build - Ignore any existing ``MANIFEST.json`` and ``FILES.json`` in the root directory when building a collection.
- ansible-galaxy collection verify - display files/directories not included in the FILES.json as modified content.
- ansible-galaxy publish - Fix warning and error detection in import messages to properly display them in Ansible
- ansible-pull handle case where hostname and nodename are empty
- ansible-test - Add default entry for Windows remotes to be used with unknown versions.
- ansible-test - All virtual environments managed by ansible-test are marked as usable after being bootstrapped, to avoid errors caused by use of incomplete environments. Previously this was only done for sanity tests. Existing environments from previous versions of ansible-test will be recreated on demand due to lacking the new marker.
- ansible-test - Automatic target requirements installation is now based on the target environment instead of the controller environment.
- ansible-test - Correctly detect when running as the ``root`` user (UID 0) on the origin host. The result of the detection was incorrectly being inverted.
- ansible-test - Don't fail if network cannot be disconnected (https://github.com/ansible/ansible/pull/77472)
- ansible-test - Fix Python real prefix detection when running in a ``venv`` virtual environment.
- ansible-test - Fix ``windows-integration`` and ``network-integration`` when used with the ``--docker`` option and user-provided inventory.
- ansible-test - Fix installation and usage of ``pyyaml`` requirement for the ``import`` sanity test for collections.
- ansible-test - Fix path to inventory file for ``windows-integration`` and ``network-integration`` commands for collections.
- ansible-test - Fix plugin loading.
- ansible-test - Fix skipping of tests marked ``needs/python`` on the origin host.
- ansible-test - Fix skipping of tests marked ``needs/root`` on the origin host.
- ansible-test - Fix the ``import`` sanity test to work properly when Ansible's built-in vendoring support is in use.
- ansible-test - Fix the ``validate-modules`` sanity test to avoid double-loading the collection loader and possibly failing on import of the ``packaging`` module.
- ansible-test - Fix traceback in ``import`` sanity test on Python 2.7 when ``pip`` is not available.
- ansible-test - Fix traceback in the ``validate-modules`` sanity test when testing an Ansible module without any callables.
- ansible-test - Fix traceback when running from an install and delegating execution to a different Python interpreter.
- ansible-test - Fix traceback when using the ``--all`` option with PowerShell code coverage.
- ansible-test - Fix type hints.
- ansible-test - Import ``yaml.cyaml.CParser`` instead of ``_yaml.CParser`` in the ``yamllint`` sanity test.
- ansible-test - Limit ``paramiko`` installation to versions before 2.9.0. This is required to maintain support for systems which do not support RSA SHA-2 algorithms.
- ansible-test - Pylint Deprecated Plugin - Use correct message symbols when date or version is not a float or str (https://github.com/ansible/ansible/issues/77085)
- ansible-test - Relocate constants to eliminate symlink.
- ansible-test - Replace the directory portion of out-of-tree paths in JUnit files from integration tests with the ``out-of-tree:`` prefix.
- ansible-test - Sanity tests run with the ``--requirements` option for Python 2.x now install ``virtualenv`` when it is missing or too old. Previously it was only installed if missing. Version 16.7.12 is now installed instead of the latest version.
- ansible-test - Set the ``pytest`` option ``--rootdir`` instead of letting it be auto-detected.
- ansible-test - Show an error message instead of a traceback when running outside of a supported directory.
- ansible-test - Target integration test requirements are now correctly installed for target environments running on the controller.
- ansible-test - The ``import`` sanity test no longer reports errors about ``packaging`` being missing when testing collections.
- ansible-test - Update distribution test containers to version 3.1.0.
- ansible-test - Update help links to reference ``ansible-core`` instead of ``ansible``.
- ansible-test - Update unit tests to use the ``--forked`` option instead of the deprecated ``--boxed`` option.
- ansible-test - Use https://ci-files.testing.ansible.com/ for instance bootstrapping instead of an S3 endpoint.
- ansible-test - Use relative paths in JUnit files generated during integration test runs.
- ansible-test - Use the correct variable to reference the client's SSH key when generating inventory.
- ansible-test - Use the legacy collection loader for ``import`` sanity tests on target-only Python versions.
- ansible-test - Virtual environments managed by ansible-test now use consistent versions of ``pip``, ``setuptools`` and ``wheel``. This avoids issues with virtual environments containing outdated or dysfunctional versions of these tools. The initial bootstrapping of ``pip`` is done by ansible-test from an HTTPS endpoint instead of creating the virtual environment with it already present.
- ansible-test - fix a typo in validate-modules.
- ansible-test - fixed support container failures (eg http-test-container) under podman
- ansible-test compile sanity test - do not crash if a column could not be determined for an error (https://github.com/ansible/ansible/pull/77465).
- ansible-test pslint - Fix error when encountering validation results that are highly nested - https://github.com/ansible/ansible/issues/74151
- ansible-vault encrypt_string - fix ``--output`` option to correctly write encrypted string into given file (https://github.com/ansible/ansible/issues/75101)
- ansible.builtin.file modification_time supports check_mode
- ansible_facts.devices - Fix parsing of device serial number detected via sg_inq for rhel8 (https://github.com/ansible/ansible/issues/75420)
- apt - fails to deploy deb file to old debian systems using python-apt < 0.8.9 (https://github.com/ansible/ansible/issues/47277)
- async - Improve performance of sending async callback events by never sending the full task through the queue (https://github.com/ansible/ansible/issues/76729)
- catch the case that cowsay is broken which would lead to missing output
- cleaning facts will now only warn about the variable name and not post the content, which can be undesireable to disclose
- collection_loader - Implement 'find_spec' and 'exec_module' to override deprecated importlib methods 'find_module' and 'load_module' when applicable (https://github.com/ansible/ansible/issues/74660).
- correctly inherit vars from parent in block (https://github.com/ansible/ansible/issues/75286).
- default callback - Ensure we compare FQCN also in lockstep logic, to ensure using the FQCN of a strategy plugin triggers the correct behavior in the default callback plugin. (https://github.com/ansible/ansible/issues/76782)
- distribution - add EuroLinux to fact gathering (https://github.com/ansible/ansible/pull/76624).
- distribution - detect tencentos and gather correct facts on the distro.
- dnf - ensure releasever is passed into libdnf as string (https://github.com/ansible/ansible/issues/77010)
- extend timeout for ansible-galaxy when communicating with the galaxy server api, and apply it to all interactions with the api
- facts - add support for deepin distro information detection (https://github.com/ansible/ansible/issues/77286).
- first_found - fix to allow for spaces in file names (https://github.com/ansible/ansible/issues/77136)
- gather_facts - Fact gathering now continues even if it fails to read a file
- gather_facts action now handles the move of base connection plugin types into collections to add/prevent subset argument correctly
- gather_facts/setup will not fail anymore if capsh is present but not executable
- git module is more consistent and clearer about which ssh options are added to git calls.
- git module no longer uses wrapper script for ssh options.
- hacking - fix incorrect usage of deprecated fish-shell redirection operators that failed to honor ``--quiet`` flag when sourced (https://github.com/ansible/ansible/pull/77180).
- hostname - Do not require SystemdStrategy subclasses for every distro (https://github.com/ansible/ansible/issues/76792)
- hostname - Fix Debian strategy KeyError, use `SystemdStrategy` (https://github.com/ansible/ansible/issues/76124)
- hostname - Update the systemd strategy in the ``hostname`` module to not interfere with NetworkManager (https://github.com/ansible/ansible/issues/76958)
- hostname - add hostname support for openEuler distro (https://github.com/ansible/ansible/pull/76619).
- hostname - use ``file_get_content()`` to read the file containing the host name in the ``FileStrategy.get_permanent_hostname()`` method. This prevents a ``TypeError`` from being raised when the strategy is used (https://github.com/ansible/ansible/issues/77025).
- include_vars, properly initialize variable as there is corner case in which it can end up referenced and not defined
- inventory - parameterize ``disable_lookups`` in ``Constructable`` (https://github.com/ansible/ansible/issues/76769).
- inventory manager now respects --flush-cache
- junit callback - Fix traceback during automatic fact gathering when using relative paths.
- junit callback - Fix unicode error when handling non-ASCII task paths.
- module_utils.common.yaml - The ``SafeLoader``, ``SafeDumper`` and ``Parser`` classes now fallback to ``object`` when ``yaml`` is not available. This fixes tracebacks when inheriting from these classes without requiring a ``HAS_YAML`` guard around class definitions.
- parameters - handle blank values when argument is a list (https://github.com/ansible/ansible/issues/77108).
- play_context now compensates for when a conneciton sets the default to inventory_hostname but skips adding it to the vars.
- playbook/strategy have more informative 'attribute' based errors for playbook objects and handlers.
- python modules (new type) will now again prefer the specific python stated in the module's shebang instead of hardcoding to /usr/bin/python.
- replace - Always return ``rc`` to ensure return values are consistent - https://github.com/ansible/ansible/pull/71963
- script - skip in check mode if the plugin cannot determine if a change will occur (i.e. neither `creates` or `removes` are provided).
- service - Fixed handling of sleep arguments during service restarts on AIX. (https://github.com/ansible/ansible/issues/76877)
- service - Fixed service restarts with arguments on AIX. (https://github.com/ansible/ansible/issues/76840)
- service_facts module will now give more meaningful warnings when it fails to gather data.
- set_fact/include_vars correctly handle delegation assignments within loops
- setup - detect docker container with check for ./dockerenv or ./dockinit (https://github.com/ansible/ansible/pull/74349).
- shell/command - only return changed as True if the task has not been skipped.
- shell/command - only skip in check mode if the options `creates` and `removes` are both None.
- ssh connection - properly quote controlpersist path given by user to avoid issues with spaces and other characters
- ssh connection avoid parsing ssh cli debug lines as they can match expected output at high verbosities.
- ssh connection now uses more correct host source as play_context can ignore loop/delegation variations.
- sudo become plugin, fix handling of non interactive flags, previous substitution was too naive
- systemd - check if service is alias so it gets enabled (https://github.com/ansible/ansible/issues/75538).
- systemd - check if service is indirect so it gets enabled (https://github.com/ansible/ansible/issues/76453).
- task_executor reverts the change to push facts into delegated vars on loop finalization as result managing code already handles this and was duplicating effort to wrong result.
- template lookup - restore inadvertently deleted default for ``convert_data`` (https://github.com/ansible/ansible/issues/77004)
- to_json/to_nice_json filters defaults back to unvaulting/no unsafe packing.
- unarchive - Fix zip archive file listing that caused issues with content postprocessing (https://github.com/ansible/ansible/issues/76067).
- unarchive - Make extraction work when the LANGUAGE environment variable is set to a non-English locale.
- unarchive - apply ``owner`` and ``group`` permissions to top folder (https://github.com/ansible/ansible/issues/35426)
- unarchive - include the original error when a handler cannot manage the archive (https://github.com/ansible/ansible/issues/28977).
- unarchive - the ``io_buffer_size`` option added in 2.12 was not accepted by the module (https://github.com/ansible/ansible/pull/77271).
- urls - Allow ``ca_path`` to point to a bundle containing multiple PEM certs (https://github.com/ansible/ansible/issues/75015)
- urls/uri - Address case where ``HTTPError`` isn't fully initialized due to the error, and is missing certain methods and attributes (https://github.com/ansible/ansible/issues/76386)
- user - allow ``password_expiry_min`` and ``password_expiry_min`` to be set to ``0`` (https://github.com/ansible/ansible/issues/75017)
- user - allow password min and max to be set at the same time (https://github.com/ansible/ansible/issues/75017)
- user - update logic to check if user exists or not in MacOS.
- validate_argument_spec - Skip suboption validation if the top level option is an invalid type (https://github.com/ansible/ansible/issues/75612).
- vault - Warn instead of fail for missing vault IDs if at least one valid vault secret is found.
- winrm - Ensure ``kinit`` is run with the same ``PATH`` env var as the Ansible process
- yum - prevent storing unnecessary cache data by running `yum makecache fast` (https://github.com/ansible/ansible/issues/76336)

amazon.aws
~~~~~~~~~~

- Various modules and plugins - use vendored version of ``distutils.version`` instead of the deprecated Python standard library ``distutils`` (https://github.com/ansible-collections/amazon.aws/pull/599).
- aws_acm - No longer raising ResourceNotFound exception while retrieving ACM certificates.
- aws_ec2 inventory - use the iam_role_arn configuration parameter to assume the role before trying to call DescribeRegions if the regions configuration is not set and AWS credentials provided without enough privilege to perform the DescribeRegions action. (https://github.com/ansible-collections/amazon.aws/issues/566).
- aws_s3 - fix exception raised when using module to copy from source to destination and key is missing from source (https://github.com/ansible-collections/amazon.aws/issues/602).
- ec2_instance - Add a condition to handle default ```instance_type``` value for fix breaking on instance creation with launch template (https://github.com/ansible-collections/amazon.aws/pull/587).
- ec2_key - add support for ED25519 key type (https://github.com/ansible-collections/amazon.aws/issues/572).
- ec2_vol - Sets the Iops value in req_obj even if the iops value has not changed, to allow modifying volume types that require passing an iops value to boto. (https://github.com/ansible-collections/amazon.aws/pull/606)
- ec2_vol - changing a volume from a type that does not support IOPS (like ``standard``) to a type that does (like ``gp3``) fails (https://github.com/ansible-collections/amazon.aws/issues/626).
- ec2_vpc_igw - fix 'NoneType' object is not subscriptable error (https://github.com/ansible-collections/amazon.aws/pull/691).
- ec2_vpc_igw - use paginator for describe internet gateways and add retry to fix NoneType object is not subscriptable error (https://github.com/ansible-collections/amazon.aws/pull/695).
- ec2_vpc_net - In check mode, ensure the module does not change the configuration. Handle case when Amazon-provided ipv6 block is enabled, then disabled, then enabled again. Do not disable IPv6 CIDR association (using Amazon pool) if ipv6_cidr property is not present in the task. If the VPC already exists and ipv6_cidr property, retain the current config (https://github.com/ansible-collections/amazon.aws/pull/631).
- elb_classic_lb - handle security_group_ids when providing security_group_names and fix broken tasks in integration test (https://github.com/ansible-collections/amazon.aws/pull/592).
- s3_bucket - Enable the management of bucket-level ACLs (https://github.com/ansible-collections/amazon.aws/issues/573).

ansible.netcommon
~~~~~~~~~~~~~~~~~

- Fix issue with cli_parse native_parser plugin when input is empty (https://github.com/ansible-collections/ansible.netcommon/issues/347).
- Fix validate-module sanity test.
- Fixed plugins inheriting from netcommon's base plugins (for example httpapi/restconf or netconf/default) so that they can be properly loaded (https://github.com/ansible-collections/ansible.netcommon/issues/356).
- No activity on the transport's channel was triggering a socket.timeout() after 30 secs, even if persistent_command_timeout is set to a higher value. This patch fixes it.
- network_cli - Provide clearer error message when a prompt regex fails to compile
- network_cli - fix issue when multiple terminal_initial_(prompt|answer) values are given (https://github.com/ansible-collections/ansible.netcommon/issues/331).

ansible.utils
~~~~~~~~~~~~~

- Fix issue in ipaddr,ipv4,ipv6,ipwrap filters.(https://github.com/ansible-collections/ansible.utils/issues/148).
- ipaddr - Add valid network for link-local (https://github.com/ansible-collections/ansible.netcommon/issues/350).
- ipaddr - Fix issue of breaking ipaddr filter with netcommon 2.6.0(https://github.com/ansible-collections/ansible.netcommon/issues/375).

ansible.windows
~~~~~~~~~~~~~~~

- win_command - Use the 24 hour format for the hours of ``start`` and ``end`` - https://github.com/ansible-collections/ansible.windows/issues/303
- win_copy - improve dest folder size detection to handle broken and recursive symlinks as well as inaccesible folders - https://github.com/ansible-collections/ansible.windows/issues/298
- win_dsc - Provide better error message when trying to invoke a composite DSC resource
- win_shell - Use the 24 hour format for the hours of ``start`` and ``end`` - https://github.com/ansible-collections/ansible.windows/issues/303
- win_updates - Fix return value for ``updates`` and ``filtered_updates`` to match original stucture - https://github.com/ansible-collections/ansible.windows/issues/307
- win_updates - Fixed issue when attempting to run ``task.ps1`` with a host that has a restrictive execution policy set through GPO
- win_updates - prevent the host from going to sleep if a low sleep timeout is set - https://github.com/ansible-collections/ansible.windows/issues/310

arista.eos
~~~~~~~~~~

- Add check mode support to bgp_global and bgp_address_family
- Add logic to skip unwanted configs from running-config, to collect bgp af facts.
- Add symlink of modules under plugins/action.
- Fixed an invalid parameter used in example for eos_l2_interfaces
- eos_acls - fixes state replaced where new ACEs are not all added
- eos_bgp_global - Add alias for peer -  neighbor_address

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

- 'ios_acls'- filters out dynamically generated reflexive type acls.
- 'ios_banner' - Bugfix for presence of multiple delimitation chars in the banner's declaration and idempotence improvement.
- Add symlink of modules under plugins/action.
- Fix ntp_global - remove no_log for key_id under peer and server attributes.
- Fix ntp_global - to handle when attribute value is false.
- `ios_acls` - Fix commands sequencing for replaced state.
- `ios_acls` - Fix remarks breaking idempotent behavior.
- `ios_acls` - Fixes protocol_options not rendering command properly when range is specified.
- `ios_acls` - Fixes standard acls getting wrongly parsed in v2.6.0
- `ios_acls` - bugfixes and optimization for ACLs.
- `ios_bgp_address_family` - Fix multiple bgp_address_family issues. Add `set` option in `send_community` to allow backwards compatibility with older configs. Add `set` option in `redistribute.connected` to allow ospf redistribution. Fix issue with ipv6 and peer-group neighbor identification. Add ability to pull `redistribute` information for address families to conform to argspec. Fix issue with not pulling `local_as` when defined for neighbors.
- `ios_bgp_global` - Added bmp.server_options.
- `ios_bgp_global` - Added capability of configure network options.
- `ios_bgp_global` - Added community and local_preference for route_reflector_client.
- `ios_bgp_global` - Added update_source for neighbors.
- `ios_bgp_global` - Correct misspelled attributes with alternates/alias.
- `ios_bgp_global` - Facts and config code optimized for using rm_templates.
- `ios_bgp_global` - Parsers added for non-implemented attributes.
- `ios_bgp_global` - client_to_client.cluster_id corrected to take string input.
- `ios_bgp_global` - neighbors.path_attribute to support float format.
- `ios_facts` - Fix Line protocol parser for legacy facts where state information per interface is present.
- `ios_l2_interfaces` - fix unable to identify FiveGigabitEthernet names on facts gathering.
- `ios_l2_interfaces` - fix unable to set switchport mode properly.
- `ios_logging_global` - fix host ipv6 commands not parsed correctly.
- `ios_logging_global` - fix wrong ordering of commands fired on replaced state.
- `ios_route_maps` - Fix parsers for correct rendering of as_number as list.
- `ios_snmp_server` - Change key from `users` to `views` in rm template to fix failure when collecting snmp server facts from devices that have a view defined in the configuration (https://github.com/ansible-collections/cisco.ios/issues/491).
- `ios_snmp_server` - Fix parsers for views facts collection.
- `ios_static_routes` - Consider only config containing routes to render facts.
- `ios_static_routes` - Fixes static routes unable to identify interface names when supplied with destination attribute.
- `ios_vlans` - fix parsing of VLAN names with spaces.
- `ios_vlans` - fix parsing of VLAN ranges under remote span.

cisco.iosxr
~~~~~~~~~~~

- Add symlink of modules under plugins/action.
- `iosxr_acls` - fix acl for parsing wrong command on ( num matches ) data
- `iosxr_snmp_server` - Add aliases for access-lists in snmp-server(https://github.com/ansible-collections/cisco.iosxr/pull/225).
- fix issue of local variable 'start_index' referenced before assignment with cisco.iosxr.iosxr_config.
- iosxr_bgp_global - Add alias for neighbor_address (https://github.com/ansible-collections/cisco.iosxr/issues/216)
- iosxr_snmp_server - Fix gather_facts issue in snmp_servers (https://github.com/ansible-collections/cisco.iosxr/issues/215)
- iosxr_user - replaced custom paramiko sftp and ssh usage with native "copy_file" and "send_command" functions. Fixed issue when ssh key copying doesn't work with network_cli or netconf plugin by deleting "provider" usage. Fixed improper handling of "No such configuration item" when getting data for username section, without that ansible always tried to delete user "No" when purging if there is no any user in config. Fixed one-line admin mode commands not work anymore for ssh key management on IOS XR Software, Version 7.1.3, and add support of "admin" module property (https://github.com/ansible-collections/cisco.iosxr/pull/15)

cisco.ise
~~~~~~~~~

- Update ISE version to 3.1.0 on vars example
- Update README recommended SDK version in compatibility matrix
- Update README, add ISE 3.1 + Patch 1 and ISE API Versioning notes
- Update README, update Compatibility matrix.
- Update documentation of the modules.
- Update recommended SDK version in modules from 1.4.0 to 1.5.0
- node_group_node_create - fix family execution call from Node Deployment to Node Group.
- node_group_node_delete - fix family execution call from Node Deployment to Node Group.
- node_group_node_info - fix family execution call from Node Deployment to Node Group.
- node_services_profiler_probe_config - fixes params used for module.
- node_services_sxp_interfaces - fixes params used for module.
- plugin/modules - update documentation block.
- repository - fixes params used for modules. Fix for issue 19.
- repository_files_info - fixes params used for module.
- trustsec_sg_vn_mapping - fix version_added to 2.0.0
- trustsec_sg_vn_mapping_bulk_create - fix version_added to 2.0.0
- trustsec_sg_vn_mapping_bulk_create - update EXAMPLES block of module documentation
- trustsec_sg_vn_mapping_bulk_delete - fix version_added to 2.0.0
- trustsec_sg_vn_mapping_bulk_delete - update EXAMPLES block of module documentation
- trustsec_sg_vn_mapping_bulk_update - fix version_added to 2.0.0
- trustsec_sg_vn_mapping_bulk_update - update EXAMPLES block of module documentation
- trustsec_sg_vn_mapping_info - change filter param type from str to list
- trustsec_sg_vn_mapping_info - fix version_added to 2.0.0
- trustsec_vn_bulk_create - update EXAMPLES block of module documentation
- trustsec_vn_bulk_delete - update EXAMPLES block of module documentation
- trustsec_vn_bulk_update - update EXAMPLES block of module documentation
- trustsec_vn_vlan_mapping - fix version_added to 2.0.0
- trustsec_vn_vlan_mapping_bulk_create - fix version_added to 2.0.0
- trustsec_vn_vlan_mapping_bulk_create - update EXAMPLES block of module documentation
- trustsec_vn_vlan_mapping_bulk_delete - fix version_added to 2.0.0
- trustsec_vn_vlan_mapping_bulk_delete - update EXAMPLES block of module documentation
- trustsec_vn_vlan_mapping_bulk_update - fix version_added to 2.0.0
- trustsec_vn_vlan_mapping_bulk_update - update EXAMPLES block of module documentation
- trustsec_vn_vlan_mapping_info - change filter param type from str to list
- trustsec_vn_vlan_mapping_info - fix version_added to 2.0.0
- update README links in galaxy from relative to absolute links.
- update README.

cisco.meraki
~~~~~~~~~~~~

- meraki_mr_rf_profile - Fix issue with idempotency and creation of RF Profiles by name only
- meraki_mr_ssid - Fix issue with SSID removal idempotency when ID doesn't exist
- meraki_syslog - Improve reliability for multiple roles or capitalization.

cisco.mso
~~~~~~~~~

- Add no_log to aws_access_key and secret_key in mso_tenant_site
- Fix MSO HTTP API to work without host, user and password module attribute
- Fix issue with unicast_routing idemptotency in mso_schema_template_bd
- Fix mso_schema_site_anp and mso_schema_site_anp_epg idempotency issue
- Remove sanity ignore files and fix sanity issues that were previously ignored

cisco.nxos
~~~~~~~~~~

- Fix action plugin redirection to make module defaults work properly.
- Fix for nxos_vlans issue (https://github.com/ansible-collections/cisco.nxos/issues/425).
- `nxos_bgp_address_family` -  Add hmm as valid option for redistribute protocol (https://github.com/ansible-collections/cisco.nxos/issues/385).
- `nxos_ntp_global` - Aliased `vrf` to `use_vrf` wherever applicable to maintain consistency with models for other platforms.
- `nxos_ntp_global` - In some cases, there is an extra whitespace in the source-interface line. This patch accounts for this behaviour in config (https://github.com/ansible-collections/cisco.nxos/issues/399).
- `nxos_snmp_server` - Fix rendering context command (https://github.com/ansible-collections/cisco.nxos/issues/406).
- nxos_acls - Fix incorrect parsing of remarks if it has 'ip/ipv6 access-list' in it.
- nxos_snmp_server - Add alias for community (https://github.com/ansible-collections/cisco.nxos/issues/433)

cloud.common
~~~~~~~~~~~~

- fix parameters with aliases not being passed through (https://github.com/ansible-collections/cloud.common/issues/91).
- fix turbo mode loading incorrect module (https://github.com/ansible-collections/cloud.common/pull/102).
- turbo - Ensure we don't call the module with duplicated aliased parameters.

community.aws
~~~~~~~~~~~~~

- Add backoff retry logic to elb_application_lb_info (https://github.com/ansible-collections/community.aws/pull/977)
- Add backoff retry logic to route53_info (https://github.com/ansible-collections/community.aws/pull/865).
- Add backoff retry logic to route53_zone (https://github.com/ansible-collections/community.aws/pull/865).
- aws_eks - Fix EKS cluster creation with short names (https://github.com/ansible-collections/community.aws/pull/818).
- cloudfront_distribution - Dont pass ``s3_origin_access_identity_enabled`` to API request (https://github.com/ansible-collections/community.aws/pull/881).
- ecs_taskdefinition - include launch_type comparison when comparing task definitions (https://github.com/ansible-collections/community.aws/pull/840)
- elb_application_lb - Fix empty security groups list behaves inconsistently on create/update by treating empty security group as VPC's defaault (https://github.com/ansible-collections/community.aws/pull/971).
- elb_application_lb_info - Add backoff retry logic (https://github.com/ansible-collections/community.aws/pull/977)
- elb_target_group_info - Add backoff retry logic (https://github.com/ansible-collections/community.aws/pull/1001)
- execute_lambda - Wait for Lambda function State = Active before executing (https://github.com/ansible-collections/community.aws/pull/857)
- iam_role - Removes unnecessary removal of permission boundary from a role when deleting a role. Unlike inline policies, permission boundaries do not need to be removed from an IAM role before deleting the IAM role. This behavior causes issues when a permission boundary is inherited that prevents removal of the permission boundary. (https://github.com/ansible-collections/community.aws/pull/961)
- lambda - Wait for Lambda function State = Active & LastUpdateStatus = Successful before updating (https://github.com/ansible-collections/community.aws/pull/857)
- rds_instance - Fix updates of ``iops`` or ``allocated_storage`` for ``io1`` DB instances when only one value is changing (https://github.com/ansible-collections/community.aws/pull/878).
- redshift_info - fix invalid import path for botocore exceptions (https://github.com/ansible-collections/community.aws/issues/968).
- wafv2_web_acl - fix exception when a rule contains lists values (https://github.com/ansible-collections/community.aws/pull/962).

community.crypto
~~~~~~~~~~~~~~~~

- Various modules and plugins - use vendored version of ``distutils.version`` instead of the deprecated Python standard library ``distutils`` (https://github.com/ansible-collections/community.crypto/pull/353).
- certificate_complete_chain - allow multiple potential intermediate certificates to have the same subject (https://github.com/ansible-collections/community.crypto/issues/399, https://github.com/ansible-collections/community.crypto/pull/403).
- certificate_complete_chain - do not append root twice if the chain already ends with a root certificate (https://github.com/ansible-collections/community.crypto/pull/360).
- certificate_complete_chain - do not hang when infinite loop is found (https://github.com/ansible-collections/community.crypto/issues/355, https://github.com/ansible-collections/community.crypto/pull/360).
- luks_device - fix parsing of ``lsblk`` output when device name ends with ``crypt`` (https://github.com/ansible-collections/community.crypto/issues/409, https://github.com/ansible-collections/community.crypto/pull/410).
- luks_devices - set ``LANG`` and similar environment variables to avoid translated output, which can break some of the module's functionality like key management (https://github.com/ansible-collections/community.crypto/pull/388, https://github.com/ansible-collections/community.crypto/issues/385).
- openssh_* modules - fix exception handling to report traceback to users for enhanced traceability (https://github.com/ansible-collections/community.crypto/pull/417).
- openssh_cert - fixed false ``changed`` status for ``host`` certificates when using ``full_idempotence`` (https://github.com/ansible-collections/community.crypto/issues/395, https://github.com/ansible-collections/community.crypto/pull/396).
- x509_certificate - for the ``ownca`` provider, check whether the CA private key actually belongs to the CA certificate (https://github.com/ansible-collections/community.crypto/pull/407).
- x509_certificate - regenerate certificate when the CA's public key changes for ``provider=ownca`` (https://github.com/ansible-collections/community.crypto/pull/407).
- x509_certificate - regenerate certificate when the CA's subject changes for ``provider=ownca`` (https://github.com/ansible-collections/community.crypto/issues/400, https://github.com/ansible-collections/community.crypto/pull/402).
- x509_certificate - regenerate certificate when the private key changes for ``provider=selfsigned`` (https://github.com/ansible-collections/community.crypto/pull/407).

community.digitalocean
~~~~~~~~~~~~~~~~~~~~~~

- Update README.md with updated Droplet examples (https://github.com/ansible-collections/community.digitalocean/issues/199).
- digital_ocean_cdn_endpoints - defaulting optional string parameters as strings (https://github.com/ansible-collections/community.digitalocean/issues/205).
- digital_ocean_cdn_endpoints - updating Spaces endpoint for the integration test (https://github.com/ansible-collections/community.digitalocean/issues/205).
- digital_ocean_droplet - ensure that Droplet creation is successful (https://github.com/ansible-collections/community.digitalocean/issues/197).
- digital_ocean_droplet - fix reporting of changed state when ``firewall`` argument is present (https://github.com/ansible-collections/community.digitalocean/pull/219).
- digital_ocean_droplet - fixing project assignment for the C(unique_name=False) case (https://github.com/ansible-collections/community.digitalocean/issues/201).
- digital_ocean_droplet - move Droplet data under "droplet" key in returned payload (https://github.com/ansible-collections/community.digitalocean/issues/211).
- digital_ocean_droplet - update Droplet examples (https://github.com/ansible-collections/community.digitalocean/issues/199).
- digital_ocean_kubernetes - add missing elements type to C(node_pools.tags) and C(node_pools.taints) options (https://github.com/ansible-collections/community.digitalocean/issues/232).

community.dns
~~~~~~~~~~~~~

- Update Public Suffix List.
- wait_for_txt - do not fail if ``NXDOMAIN`` result is returned. Also do not succeed if no nameserver can be found (https://github.com/ansible-collections/community.dns/issues/81, https://github.com/ansible-collections/community.dns/pull/82).

community.docker
~~~~~~~~~~~~~~~~

- Fix unintended breaking change caused by `an earlier fix <https://github.com/ansible-collections/community.docker/pull/258>`_ by vendoring the deprecated Python standard library ``distutils.version`` until this collection stops supporting Ansible 2.9 and ansible-base 2.10 (https://github.com/ansible-collections/community.docker/issues/267, https://github.com/ansible-collections/community.docker/pull/269).
- Various modules and plugins - use vendored version of ``distutils.version`` included in ansible-core 2.12 if available. This avoids breakage when ``distutils`` is removed from the standard library of Python 3.12. Note that ansible-core 2.11, ansible-base 2.10 and Ansible 2.9 are right now not compatible with Python 3.12, hence this fix does not target these ansible-core/-base/2.9 versions (https://github.com/ansible-collections/community.docker/pull/258).
- docker connection plugin - fix option handling to be compatible with ansible-core 2.13 (https://github.com/ansible-collections/community.docker/pull/297, https://github.com/ansible-collections/community.docker/issues/307).
- docker connection plugin - replace deprecated ``distutils.spawn.find_executable`` with Ansible's ``get_bin_path`` to find the ``docker`` executable (https://github.com/ansible-collections/community.docker/pull/257).
- docker_api connection plugin - avoid passing an unnecessary argument to a Docker SDK for Python call that is only supported by version 3.0.0 or later (https://github.com/ansible-collections/community.docker/pull/243).
- docker_api connection plugin - fix option handling to be compatible with ansible-core 2.13 (https://github.com/ansible-collections/community.docker/pull/308).
- docker_compose - fix Python 3 type error when extracting warnings or errors from docker-compose's output (https://github.com/ansible-collections/community.docker/pull/305).
- docker_container, docker_image - adjust image finding code to pecularities of ``podman-docker``'s API emulation when Docker short names like ``redis`` are used (https://github.com/ansible-collections/community.docker/issues/292).
- docker_container_exec - ``chdir`` is only supported since Docker SDK for Python 3.0.0. Make sure that this option can only use when 3.0.0 or later is installed, and prevent passing this parameter on when ``chdir`` is not provided to this module (https://github.com/ansible-collections/community.docker/pull/243, https://github.com/ansible-collections/community.docker/issues/242).
- docker_container_exec - disallow using the ``chdir`` option for Docker API before 1.35 (https://github.com/ansible-collections/community.docker/pull/253).
- nsenter connection plugin - ensure the ``nsenter_pid`` option is retrieved in ``_connect`` instead of ``__init__`` to prevent a crasher due to bad initialization order (https://github.com/ansible-collections/community.docker/pull/249).
- nsenter connection plugin - replace the use of ``--all-namespaces`` with specific namespaces to support compatibility with Busybox nsenter (used on, for example, Alpine containers) (https://github.com/ansible-collections/community.docker/pull/249).

community.general
~~~~~~~~~~~~~~~~~

- Various modules and plugins - use vendored version of ``distutils.version`` instead of the deprecated Python standard library ``distutils`` (https://github.com/ansible-collections/community.general/pull/3936).
- alternatives - fix output parsing for alternatives groups (https://github.com/ansible-collections/community.general/pull/3976).
- cargo - fix detection of outdated packages when ``state=latest`` (https://github.com/ansible-collections/community.general/pull/4052).
- cargo - fix incorrectly reported changed status for packages with a name containing a hyphen (https://github.com/ansible-collections/community.general/issues/4044, https://github.com/ansible-collections/community.general/pull/4052).
- dconf - skip processes that disappeared while we inspected them (https://github.com/ansible-collections/community.general/issues/4151).
- dsv lookup plugin - raise an Ansible error if the wrong ``python-dsv-sdk`` version is installed (https://github.com/ansible-collections/community.general/pull/4422).
- filesize - add support for busybox dd implementation, that is used by default on Alpine linux (https://github.com/ansible-collections/community.general/pull/4288, https://github.com/ansible-collections/community.general/issues/4259).
- github_repo - ``private`` and ``description`` attributes should not be set to default values when the repo already exists (https://github.com/ansible-collections/community.general/pull/2386).
- gitlab_group_variable - add missing documentation about GitLab versions that support ``environment_scope`` and ``variable_type`` (https://github.com/ansible-collections/community.general/pull/4038).
- gitlab_group_variable - allow to set same variable name under different environment scopes. Due this change, the return value ``group_variable`` differs from previous version in check mode. It was counting ``updated`` values, because it was accidentally overwriting environment scopes (https://github.com/ansible-collections/community.general/pull/4038).
- gitlab_group_variable - fix idempotent change behaviour for float and integer variables (https://github.com/ansible-collections/community.general/pull/4038).
- gitlab_project_variable - ``value`` is not necessary when deleting variables (https://github.com/ansible-collections/community.general/pull/4150).
- gitlab_project_variable - add missing documentation about GitLab versions that support ``environment_scope`` and ``variable_type`` (https://github.com/ansible-collections/community.general/issues/4038).
- gitlab_project_variable - allow to set same variable name under different environment scopes. Due this change, the return value ``project_variable`` differs from previous version in check mode. It was counting ``updated`` values, because it was accidentally overwriting environment scopes (https://github.com/ansible-collections/community.general/issues/4038).
- gitlab_project_variable - fix idempotent change behaviour for float and integer variables (https://github.com/ansible-collections/community.general/issues/4038).
- gitlab_runner - make ``project`` and ``owned`` mutually exclusive (https://github.com/ansible-collections/community.general/pull/4136).
- gitlab_runner - use correct API endpoint to create and retrieve project level runners when using ``project`` (https://github.com/ansible-collections/community.general/pull/3965).
- homebrew_cask - fix force install operation (https://github.com/ansible-collections/community.general/issues/3703).
- icinga2 inventory plugin - handle 404 error when filter produces no results (https://github.com/ansible-collections/community.general/issues/3875, https://github.com/ansible-collections/community.general/pull/3906).
- imc_rest - fixes the module failure due to the usage of ``itertools.izip_longest`` which is not available in Python 3 (https://github.com/ansible-collections/community.general/issues/4206).
- ini_file - when removing nothing do not report changed (https://github.com/ansible-collections/community.general/issues/4154).
- interfaces_file - fixed the check for existing option in interface (https://github.com/ansible-collections/community.general/issues/3841).
- jail connection plugin - replace deprecated ``distutils.spawn.find_executable`` with Ansible's ``get_bin_path`` to find the executable (https://github.com/ansible-collections/community.general/pull/3934).
- jira - fixed bug where module returns error related to dictionary key ``body`` (https://github.com/ansible-collections/community.general/issues/3419).
- keycloak_* - the documented ``validate_certs`` parameter was not taken into account when calling the ``open_url`` function in some cases, thus enforcing certificate validation even when ``validate_certs`` was set to ``false``. (https://github.com/ansible-collections/community.general/pull/4382)
- keycloak_user_federation - creating a user federation while specifying an ID (that does not exist yet) no longer fail with a 404 Not Found (https://github.com/ansible-collections/community.general/pull/4212).
- keycloak_user_federation - mappers auto-created by keycloak are matched and merged by their name and no longer create duplicated entries (https://github.com/ansible-collections/community.general/pull/4212).
- linode inventory plugin - fix configuration handling relating to inventory filtering (https://github.com/ansible-collections/community.general/pull/4336).
- listen_ports_facts - local port regex was not handling well IPv6 only binding. Fixes the regex for ``ss`` (https://github.com/ansible-collections/community.general/pull/4092).
- lxd connection plugin - replace deprecated ``distutils.spawn.find_executable`` with Ansible's ``get_bin_path`` to find the ``lxc`` executable (https://github.com/ansible-collections/community.general/pull/3934).
- lxd inventory plugin - do not crash if OS and release metadata are not present
  (https://github.com/ansible-collections/community.general/pull/4351).
- mail callback plugin - fix crash on Python 3 (https://github.com/ansible-collections/community.general/issues/4025, https://github.com/ansible-collections/community.general/pull/4026).
- mail callback plugin - fix encoding of the name of sender and recipient (https://github.com/ansible-collections/community.general/issues/4060, https://github.com/ansible-collections/community.general/pull/4061).
- mksysb - fixed bug for parameter ``backup_dmapi_fs`` was passing the wrong CLI argument (https://github.com/ansible-collections/community.general/pull/3295).
- nmcli - fix returning "changed" when no mask set for IPv4 or IPv6 addresses on task rerun (https://github.com/ansible-collections/community.general/issues/3768).
- nmcli - fix returning "changed" when routes parameters set, also suggest new routes4 and routes6 format (https://github.com/ansible-collections/community.general/issues/4131).
- nmcli - pass ``flags``, ``ingress``, ``egress`` params to ``nmcli`` (https://github.com/ansible-collections/community.general/issues/1086).
- nrdp callback plugin - fix error ``string arguments without an encoding`` (https://github.com/ansible-collections/community.general/issues/3903).
- opentelemetry - fix generating a trace with a task containing ``no_log: true`` (https://github.com/ansible-collections/community.general/pull/4043).
- opentelemetry_plugin - honour ``ignore_errors`` when a task has failed instead of reporting an error (https://github.com/ansible-collections/community.general/pull/3837).
- pacman - Use ``--groups`` instead of ``--group`` (https://github.com/ansible-collections/community.general/pull/4312).
- pacman - fix URL based package installation (https://github.com/ansible-collections/community.general/pull/4286, https://github.com/ansible-collections/community.general/issues/4285).
- pacman - fix ``upgrade=yes`` (https://github.com/ansible-collections/community.general/pull/4275, https://github.com/ansible-collections/community.general/issues/4274).
- pacman - make sure that ``packages`` is always returned when ``name`` or ``upgrade`` is specified, also if nothing is done (https://github.com/ansible-collections/community.general/pull/4329).
- pacman - when the ``update_cache`` option is combined with another option such as ``upgrade``, report ``changed`` based on the actions performed by the latter option. This was the behavior in community.general 4.4.0 and before. In community.general 4.5.0, a task combining these options would always report ``changed`` (https://github.com/ansible-collections/community.general/pull/4318).
- passwordstore lookup plugin - fix error detection for non-English locales (https://github.com/ansible-collections/community.general/pull/4219).
- passwordstore lookup plugin - prevent returning path names as passwords by accident (https://github.com/ansible-collections/community.general/issues/4185, https://github.com/ansible-collections/community.general/pull/4192).
- passwordstore lookup plugin - replace deprecated ``distutils.util.strtobool`` with Ansible's ``convert_bool.boolean`` to interpret values for the ``create``, ``returnall``, ``overwrite``, 'backup``, and ``nosymbols`` options (https://github.com/ansible-collections/community.general/pull/3934).
- pipx - passes the correct command line option ``--include-apps`` (https://github.com/ansible-collections/community.general/issues/3791).
- proxmox - fixed ``onboot`` parameter causing module failures when undefined (https://github.com/ansible-collections/community.general/issues/3844).
- proxmox inventory plugin - always convert strings that follow the ``key=value[,key=value[...]]`` form into dictionaries (https://github.com/ansible-collections/community.general/pull/4349).
- proxmox inventory plugin - fixed the ``description`` field being ignored if it contained a comma (https://github.com/ansible-collections/community.general/issues/4348).
- proxmox inventory plugin - fixed the ``tags_parsed`` field when Proxmox returns a single space for the ``tags`` entry (https://github.com/ansible-collections/community.general/pull/4378).
- proxmox_kvm - fix error in check when creating or cloning (https://github.com/ansible-collections/community.general/pull/4306).
- proxmox_kvm - fix error when checking whether Proxmox VM exists (https://github.com/ansible-collections/community.general/pull/4287).
- python_requirements_info - fails if version operator used without version (https://github.com/ansible-collections/community.general/pull/3785).
- python_requirements_info - store ``mismatched`` return values per package as documented in the module (https://github.com/ansible-collections/community.general/pull/4078).
- say callback plugin - replace deprecated ``distutils.spawn.find_executable`` with Ansible's ``get_bin_path`` to find the ``say`` resp. ``espeak`` executables (https://github.com/ansible-collections/community.general/pull/3934).
- scaleway_user_data - fix double-quote added where no double-quote is needed to user data in scaleway's server (``Content-type`` -> ``Content-Type``) (https://github.com/ansible-collections/community.general/pull/3940).
- slack - add ``charset`` to HTTP headers to avoid Slack API warning (https://github.com/ansible-collections/community.general/issues/3932).
- terraform - fix ``variable`` handling to allow complex values (https://github.com/ansible-collections/community.general/pull/4281).
- terraform - fix command options being ignored during planned/plan in function ``build_plan`` such as ``lock`` or ``lock_timeout`` (https://github.com/ansible-collections/community.general/issues/3707, https://github.com/ansible-collections/community.general/pull/3726).
- terraform - revert bugfix https://github.com/ansible-collections/community.general/pull/4281 that tried to fix ``variable`` handling to allow complex values. It turned out that this was breaking several valid use-cases (https://github.com/ansible-collections/community.general/issues/4367, https://github.com/ansible-collections/community.general/pull/4370).
- vdo - fix options error (https://github.com/ansible-collections/community.general/pull/4163).
- yarn - fix incorrect handling of ``yarn list`` and ``yarn global list`` output that could result in fatal error (https://github.com/ansible-collections/community.general/pull/4050).
- yarn - fix incorrectly reported status when installing a package globally (https://github.com/ansible-collections/community.general/issues/4045, https://github.com/ansible-collections/community.general/pull/4050).
- yarn - fix missing ``~`` expansion in yarn global install folder which resulted in incorrect task status (https://github.com/ansible-collections/community.general/issues/4045, https://github.com/ansible-collections/community.general/pull/4048).
- yum_versionlock - fix matching of existing entries with names passed to the module. Match yum and dnf lock format (https://github.com/ansible-collections/community.general/pull/4183).
- zone connection plugin - replace deprecated ``distutils.spawn.find_executable`` with Ansible's ``get_bin_path`` to find the executable (https://github.com/ansible-collections/community.general/pull/3934).
- zypper - fixed bug that caused zypper to always report [ok] and do nothing on ``state=present`` when all packages in ``name`` had a version specification (https://github.com/ansible-collections/community.general/issues/4371, https://github.com/ansible-collections/community.general/pull/4421).

community.grafana
~~~~~~~~~~~~~~~~~

- Fix an issue with grafana_datasource for Prometheus with basic auth credential management. (#204)
- Fix an issue with threema notification channel that was not creating gateway, recipient and api_secret in Grafana. (#208)
- Fix issue with datasource names that could not contain slashes (#125)

community.hrobot
~~~~~~~~~~~~~~~~

- boot - fix incorrect handling of SSH authorized keys (https://github.com/ansible-collections/community.hrobot/issues/32, https://github.com/ansible-collections/community.hrobot/pull/33).

community.mysql
~~~~~~~~~~~~~~~

- Collection core functions - fixes related to the mysqlclient Python connector (https://github.com/ansible-collections/community.mysql/issues/292).
- Collection core functions - use vendored version of ``distutils.version`` instead of the deprecated Python standard library ``distutils`` (https://github.com/ansible-collections/community.mysql/pull/269).
- mysql_role - make the ``set_default_role_all`` parameter actually working (https://github.com/ansible-collections/community.mysql/pull/282).

community.network
~~~~~~~~~~~~~~~~~

- ce - Modify the bug in the query configuration method (https://github.com/ansible-collections/community.network/pull/56).
- community.network.ce_switchport - fix error causing by ``KeyError:`` ``host`` due to properties aren't used anywhere (https://github.com/ansible-collections/community.network/issues/313)
- exos_config - fix a hang due to an unexpected prompt during save_when (https://github.com/ansible-collections/community.network/pull/110).
- weos4 cliconf plugin - fix linting errors in documentation data (https://github.com/ansible-collections/community.network/pull/368).

community.postgresql
~~~~~~~~~~~~~~~~~~~~

- Collection core functions - use vendored version of ``distutils.version`` instead of the deprecated Python standard library ``distutils`` (https://github.com/ansible-collections/community.postgresql/pull/179).
- module core functions - get rid of the deprecated psycopg2 connection alias ``database`` in favor of ``dbname`` when psycopg2 is 2.7+ (https://github.com/ansible-collections/community.postgresql/pull/196).
- postgres_info - It now works on AWS RDS Postgres.
- postgres_info - Specific info (namespaces, extensions, languages) of each database was not being shown properly. Instead, the info from the DB that was connected was always being shown (https://github.com/ansible-collections/community.postgresql/issues/172).
- postgresql_db - get rid of the deprecated psycopg2 connection alias ``database`` in favor of ``dbname`` when psycopg2 is 2.7+ is used (https://github.com/ansible-collections/community.postgresql/issues/194, https://github.com/ansible-collections/community.postgresql/pull/196).
- postgresql_ext - Handle postgresql extension updates through path validation instead of version comparison (https://github.com/ansible-collections/community.postgresql/issues/129).
- postgresql_query - cannot handle .sql file with \\n at end of file (https://github.com/ansible-collections/community.postgresql/issues/180).

community.vmware
~~~~~~~~~~~~~~~~

- Various modules and plugins - use vendored version of ``distutils.version`` included in ansible-core 2.12 if available. This avoids breakage when ``distutils`` is removed from the standard library of Python 3.12. Note that ansible-core 2.11, ansible-base 2.10 and Ansible 2.9 are right now not compatible with Python 3.12, hence this fix does not target these ansible-core/-base/2.9 versions.
- create_nic - add advanced SR-IOV options from the VMware API (PCI dev PF/VF backing and guest OS MTU change)
- vcenter_folder - fixed folders search collision issue (https://github.com/ansible-collections/community.vmware/issues/1112).
- vmware_dvs_host - match the list of the host nics in the correct order based on the uplink port name in vCenter (https://github.com/ansible-collections/community.vmware/issues/1242).
- vmware_guest - when ``customization.password`` is not defined, the Administrator password is made empty instead of setting it to string 'None' (https://github.com/ansible-collections/community.vmware/issues/1017).
- vmware_guest_network - fix a bug that can crash the module due to an uncaught exception (https://github.com/ansible-collections/community.vmware/issues/25).
- vmware_guest_powerstate - `shutdownguest` power state is not idempotent (https://github.com/ansible-collections/community.vmware/pull/1227).

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
- Add slirp4netns idempotency for pods
- Don't include shared 'net' if network is host in pods
- Fix MAC address detection in created container
- Fix check for read-only change of root image in podman_container module
- Fix error with exitcommand for Podman v4
- Fix issue when missing plugins entry in podman_network module
- Fix new requirements for plugins documentation
- Fix podman collection for Podman version 4
- Fix podman_pod_lib behavior for ports published to multiple IPs
- Fix tests for podman_container module
- Handle tlsverify correctly in podman_login
- Hardcode RT signal numbers
- Remove default value of log-driver
- Remove idempotency for log level
- Strip slashes from volumes
- Support --new in generate_systemd
- Update secrets description and add test with secret opts

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- All playbooks require modification because the validate_certs argument is set to True by default (https://github.com/dell/dellemc-openmanage-ansible-modules/issues/357)
- The ome_application_network_time and ome_application_network_proxy modules are breaking due to the changes introduced for SSL validation.(https://github.com/dell/dellemc-openmanage-ansible-modules/issues/360)
- idrac_bios - The issue while configuring boot sources is fixed (https://github.com/dell/dellemc-openmanage-ansible-modules/issues/347)
- idrac_firmware - Issue (220130) The socket.timout issue that occurs during the wait_for_job_completion() job is fixed.
- ome_device_location - The issue that applies values of the location settings only in lowercase is fixed (https://github.com/dell/dellemc-openmanage-ansible-modules/issues/341)

f5networks.f5_modules
~~~~~~~~~~~~~~~~~~~~~

- Add auto_last_hop parameter to bigip_virtual_server module
- Fix an issue in bigip_virtual_server module that wrongly sets the partition name for profile.
- Fix issue with teem data collection where device was not ready and was returning 404 error when queried for tmos version
- asm_policy_* - fixed partition filter in asm modules.
- bigip_device_info - changes cipher and cipher_group parameters to register when the actual value is 'none'.
- bigip_device_info - fixed bug regarding handling of negated meta options.
- bigip_device_license - fixed issue that resulted in only first of the multiple add-on keys getting added to the device.
- bigip_device_syslog - this change is done so that only unescaped " is replaced with ' in the value of include parameter.
- bigip_firewall_address_list - fixed issue where addresses that contained RD would cause an error.
- bigip_gtm_wide_ip - fixed a bug that prevented creation of gtm wide ips in disabled state.
- bigip_monitor_ldap - fixed idempotency issue with security parameter in module.
- fix for displaying src, checksum and other parameters when running ucs_fetch module
- fix for source capability for bigip_device_auth_ldap module
- multiple modules - Add no_log=False setting to update_password parameter in respective modules avoid false positive security warnings.

infoblox.nios_modules
~~~~~~~~~~~~~~~~~~~~~

- Ansible playbook fails to update canonical name of CName Record `#97 <https://github.com/infobloxopen/infoblox-ansible/pull/97>`_
- nios_a_record module - KeyError 'old_ipv4addr' `#79 <https://github.com/infobloxopen/infoblox-ansible/issues/79>`_

junipernetworks.junos
~~~~~~~~~~~~~~~~~~~~~

- Fix junos_command output when empty config response is received for show commands (https://github.com/ansible-collections/junipernetworks.junos/issues/249).
- Fix ospf router_id overlap issue.

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

netapp.cloudmanager
~~~~~~~~~~~~~~~~~~~

- Add check when volume is capacity tiered.
- CVO working environment clusterProperties is deprecated. Make changes accordingly. Add CVO update status check on ``instance_type`` change.
- na_cloudmanager_connector_aws - Fix default ami not based on the region in resource file
- na_cloudmanager_connector_azure - Fix string formatting error when deleting the connector.
- na_cloudmanager_cvo_gcp - handle extra two auto-gen GCP labels to prevent update ``gcp_labels`` failure.
- na_cloudmanager_snapmirror - report actual error rather than None with "Error getting destination info".

netapp.ontap
~~~~~~~~~~~~

- Fixed ONTAP minor version ignored in checking minimum ONTAP version.
- fix error where module will fail for ONTAP 9.6 if use_rest was set to auto
- four modules (mediator, metrocluster, security_certificates, wwpn_alias) would report a None error when REST is not available.
- module_utils - fixed KeyError on Allow when using OPTIONS method and the API failed.
- na_ontap_active_directory - Fixed idempotency and traceback issues.
- na_ontap_aggregate - Fixed KeyError on unmount_volumes when offlining a volume if option is not set.
- na_ontap_aggregate - Fixed UUID issue when attempting to attach object store as part of creating the aggregate with REST.
- na_ontap_aggregate - Fixed error in delete aggregate if the ``disk_count`` is less than current disk count.
- na_ontap_aggregate - Report an error when attempting to change snaplock_type.
- na_ontap_autosupport - Fixed `partner_address` not working in REST.
- na_ontap_broadcast_domain - fix idempotency issue when ``ports`` has identical values.
- na_ontap_cifs_local_user_modify - KeyError on ``description`` or ``full_name`` with REST.
- na_ontap_cifs_local_user_modify - unexpected argument ``name`` error with REST.
- na_ontap_cifs_server -  error out if ZAPI only options ``force`` or ``workgroup`` are used with REST.
- na_ontap_cluster_peer - Fixed KeyError if both ``source_intercluster_lifs`` and ``dest_intercluster_lifs`` not present in cluster create.
- na_ontap_command - document that a READONLY user is not supported, even for show commands.
- na_ontap_disk_options - ONTAP 9.10.1 returns on/off rather than True/False.
- na_ontap_export_policy - fix error if more than 1 verser matched search name, the wrong uuid could be given
- na_ontap_export_policy_rule - Fixed bug that prevent ZAPI and REST calls from working correctly
- na_ontap_igroup - ``force_remove_initiator`` option was ignored when removing initiators from existing igroup.
- na_ontap_info - Add active_directory_account_info.
- na_ontap_info - Fixes issue with na_ontap_info failing in 9.1 because of ``job-schedule-cluster``.
- na_ontap_info - fix KeyError on node for aggr_efficiency_info option against a metrocluster system.
- na_ontap_iscsi - Fixed issue with ``start_state`` always being set to stopped when creating an ISCSI.
- na_ontap_lun_map - Fixed bug when deleting lun map using REST.
- na_ontap_lun_map - TypeError - '>' not supported between instances of 'int' and 'str '.
- na_ontap_lun_map - fixed bugs resulting in REST support to not work.
- na_ontap_net_ifgrp - fix error in modify ports with zapi.
- na_ontap_net_routes - metric was not always modified with ZAPI.
- na_ontap_net_routes - support cluster-scoped routes with REST.
- na_ontap_qtree - Fixed issue with ``oplocks`` not being changed during a modify in Zapi.
- na_ontap_qtree - Fixed issue with ``oplocks`` not warning user about not being supported in REST
- na_ontap_rest_info - Fixed an issues with adding field to specific info that didn't have a direct REST equivalent.
- na_ontap_rest_info - Fixed example with wrong indentation for ``use_python_keys``.
- na_ontap_security_certificates - ``intermediate_certificates`` option was ignored.
- na_ontap_snapmirror - Added use_rest condition for the REST support to work when use_rest `always`.
- na_ontap_snapshot - add error message if volume is not found with REST.
- na_ontap_snapshot - fix key error on volume when using REST.
- na_ontap_svm - fixed KeyError issue on protocols when vserver is stopped.
- na_ontap_user - Fixed TypeError 'tuple' object does not support item assignment.
- na_ontap_user - Fixed issue when attempting to change pasword for absent user when set_password is set.
- na_ontap_user - Fixed lock state is not set if password is not changed.
- na_ontap_volume - Fixed error when creating a flexGroup when ``aggregate_name`` and ``aggr_list_multiplier`` are not set in rest.
- na_ontap_volume - Fixed error with unmounting junction_path in rest.
- na_ontap_volume - Fixed issue that would fail the module in REST when changing `is_online` if two vserver volume had the same name.
- na_ontap_volume - If using REST and ONTAP 9.6 and `efficiency_policy` module will fail as `efficiency_policy` is not supported in ONTAP 9.6.
- na_ontap_volume - do not attempt to mount volume if current state is offline.
- na_ontap_volume - fix idempotency issue with compression settings when using REST.
- na_ontap_volume - report error when attempting to change the nas_application tiering control from disalllowed to required, or reciprocally.
- na_ontap_volume_efficiency - Removed restriction on policy name.
- na_ontap_vserver_delete role - report error if ONTAP version is 9.6 or older.
- na_ontap_vserver_peer - Added cluster peer accept code in REST.
- na_ontap_vserver_peer - Fixed AttributeError if ``dest_hostname`` or ``peer_options`` not present.
- na_ontap_vserver_peer - Fixed ``local_name_for_peer`` and ``local_name_for_source`` options silently ignored in REST.
- na_ontap_vserver_peer - Get peer cluster name if remote peer exist else use local cluster name.
- na_ontap_vserver_peer - ignore job entry doesn't exist error with REST to bypass ONTAP issue with FSx.
- na_ontap_vserver_peer - report error if SVM peer does not see a peering relationship after create.

netapp.storagegrid
~~~~~~~~~~~~~~~~~~

- na_sg_grid_account - minor documentation fix.
- na_sg_grid_gateway - existing endpoints matched by ``name`` and ``port``.
- na_sg_org_group - fixed behaviour where update to ``s3_policy`` is ignored if ``management_policy`` is set.

netapp_eseries.santricity
~~~~~~~~~~~~~~~~~~~~~~~~~

- santricity_host - Ensure a list of volumes are provided to prevent netapp_eseries.santricity.santricity_host (lookup) index is string not integer exception.

netbox.netbox
~~~~~~~~~~~~~

- Config Context is now able to be added to cluster [#715](https://github.com/netbox-community/ansible_modules/pull/715)
- Ensure proper filtering for VLAN group [#741](https://github.com/netbox-community/ansible_modules/pull/741)
- Fix prefix_count error on older NetBox versions in nb_inventory [#696](https://github.com/netbox-community/ansible_modules/pull/696)
- Fix prefixes option in nb_inventory to ensure all prefixes are returned [#742](https://github.com/netbox-community/ansible_modules/pull/742)
- Make sure API calls on versions without the /api/status endpoint [#707](https://github.com/netbox-community/ansible_modules/pull/707)
- Use individual list items when looking for objects  [#570](https://github.com/netbox-community/ansible_modules/pull/570)
- nb_lookup - Fix documentation of validate_cert [#629](https://github.com/netbox-community/ansible_modules/pull/629)
- netbox_site - Ensure idempotency between NetBox version 2.11 and 3.00 [#631](https://github.com/netbox-community/ansible_modules/pull/631)
- netbox_virtual_chassis - Fix issue with virtual chassis creation [#657](https://github.com/netbox-community/ansible_modules/pull/657)
- netbox_virtual_machine - Ensure idempotency between NetBox version 2.11 and 3.00 [#633](https://github.com/netbox-community/ansible_modules/pull/633)

ngine_io.cloudstack
~~~~~~~~~~~~~~~~~~~

- cs_instance - Fixed regression project ID KeyError if no project is used (https://github.com/ngine-io/ansible-collection-cloudstack/pull/94).

ngine_io.vultr
~~~~~~~~~~~~~~

- vultr_server - Fix user data not handled correctly (https://github.com/ngine-io/ansible-collection-vultr/pull/26).

ovirt.ovirt
~~~~~~~~~~~

- Fix progress logging via REST (https://github.com/oVirt/ovirt-ansible-collection/pull/474).
- Make storage_format optional - do not fail if missing (https://github.com/oVirt/ovirt-ansible-collection/pull/471).
- hosted_engine_setup - Add OpenSCAP security profile name parameter (https://github.com/oVirt/ovirt-ansible-collection/pull/411).
- hosted_engine_setup - Add an option to set the storage format when createing a storage domain and use it (https://github.com/oVirt/ovirt-ansible-collection/pull/463).
- hosted_engine_setup - Adjust files permissions (https://github.com/oVirt/ovirt-ansible-collection/pull/409).
- hosted_engine_setup - Fix call to engine-psql for vds_spm_id (https://github.com/oVirt/ovirt-ansible-collection/pull/459).
- hosted_engine_setup - Fix cloud-init package removal in airgapped environment (https://github.com/oVirt/ovirt-ansible-collection/pull/442)
- hosted_engine_setup - Remove SPICE graphic protocol (https://github.com/oVirt/ovirt-ansible-collection/pull/394).
- hosted_engine_setup - Replace xml community module (https://github.com/oVirt/ovirt-ansible-collection/pull/438).
- hosted_engine_setup - Support disa stig profile (https://github.com/oVirt/ovirt-ansible-collection/pull/426).
- hosted_engine_setup - Use cat command (https://github.com/oVirt/ovirt-ansible-collection/pull/443).
- hosted_engine_setup - Use tpgt in iscsi login (https://github.com/oVirt/ovirt-ansible-collection/pull/338)
- image_template - Remove static no - unsupported in ansible 2.12 (https://github.com/oVirt/ovirt-ansible-collection/pull/341).
- ovirt_host - Fix failed_state_after_reinstall condition (https://github.com/oVirt/ovirt-ansible-collection/pull/371).
- ovirt_template - Fix creating templates where the base template version number is not 1 (https://github.com/oVirt/ovirt-ansible-collection/pull/370).
- repositories - Fix dnf module variable (https://github.com/oVirt/ovirt-ansible-collection/pull/454).
- repositories - fix force flag on subscription-manager (https://github.com/oVirt/ovirt-ansible-collection/pull/430).

purestorage.flasharray
~~~~~~~~~~~~~~~~~~~~~~

- purefa_certs - Allow a certificate to be imported over an existing SSL certificate
- purefa_eula - Reolve EULA signing issue
- purefa_info - Fix space reporting issue
- purefa_network - Fix bug introduced with management of FC ports
- purefa_policy - Fix issue with SMB Policy creation
- purefa_subnet - Fix subnet update checks when no gateway in existing subnet configuration

t_systems_mms.icinga_director
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- added a fix for the new scheduled_downtime module (https://github.com/T-Systems-MMS/ansible-collection-icinga-director/pull/150)
- role: add check_command to icinga_service_apply (https://github.com/T-Systems-MMS/ansible-collection-icinga-director/pull/161)

theforeman.foreman
~~~~~~~~~~~~~~~~~~

- callback plugin - include timezone information in the callback reported data (https://github.com/theforeman/foreman-ansible-modules/issues/1171)
- content_upload - clarify that ``src`` refers to a remote file (https://bugzilla.redhat.com/show_bug.cgi?id=2055416)
- host, hostgroup - fix updating puppetclasses while also updating description (or other string-like attributes) (https://github.com/theforeman/foreman-ansible-modules/issues/1231)
- hostgroup, location - don't fail when trying to delete a Hostgroup or Location where the parent is already absent
- inventory plugin - fetch *all* facts, not only the first 250, when using the old Hosts API

Known Issues
------------

Ansible-core
~~~~~~~~~~~~

- get_url - document ``check_mode`` correctly with unreliable changed status (https://github.com/ansible/ansible/issues/65687).

community.general
~~~~~~~~~~~~~~~~~

- pacman - ``update_cache`` cannot differentiate between up to date and outdated package lists and will report ``changed`` in both situations (https://github.com/ansible-collections/community.general/pull/4318).
- pacman - binaries specified in the ``executable`` parameter must support ``--print-format`` in order to be used by this module. In particular, AUR helper ``yay`` is known not to currently support it (https://github.com/ansible-collections/community.general/pull/4312).

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- idrac_user - Issue(192043) The module may error out with the message ``unable to perform the import or export operation because there are pending attribute changes or a configuration job is in progress``. Wait for the job to complete and run the task again.
- ome_application_alerts_smtp - Issue(212310) - The module does not provide a proper error message if the destination_address is more than 255 characters.
- ome_application_alerts_syslog - Issue(215374) - The module does not provide a proper error message if the destination_address is more than 255 characters.
- ome_application_console_preferences - Issue(224690) - The module does not display a proper error message when an unsupported value is provided for the parameters report_row_limit, email_sender_settings, and metric_collection_settings, and the value is applied on OpenManage Enterprise.
- ome_device_local_access_configuration - Issue(215035) - The module reports ``Successfully updated the local access setting`` if an unsupported value is provided for the parameter timeout_limit. However, this value is not actually applied on OpenManage Enterprise Modular.
- ome_device_local_access_configuration - Issue(217865) - The module does not display a proper error message if an unsupported value is provided for the user_defined and lcd_language parameters.
- ome_device_network_services - Issue(212681) - The module does not provide a proper error message if unsupported values are provided for the parameters- port_number, community_name, max_sessions, max_auth_retries, and idle_timeout.
- ome_device_power_settings - Issue(212679) - The module displays the following message if the value provided for the parameter ``power_cap`` is not within the supported range of 0 to 32767, ``Unable to complete the request because PowerCap does not exist or is not applicable for the resource URI.``
- ome_device_power_settings - Issue(212679) - The module errors out with the following message if the value provided for the parameter ``power_cap`` is not within the supported range of 0 to 32767, ``Unable to complete the request because PowerCap does not  exist or is not applicable for the resource URI.``
- ome_device_power_settings - Issue(212679) - The module errors out with the following message if the value provided for the parameter ``power_cap`` is not within the supported range of 0 to 32767, ``Unable to complete the request because PowerCap does not exist or is not applicable for the resource URI.``
- ome_device_quick_deploy - Issue(216352) - The module does not display a proper error message if an unsupported value is provided for the ipv6_prefix_length and vlan_id parameters.
- ome_smart_fabric_uplink - Issue(186024) - The module does not allow the creation of multiple uplinks of the same name even though it is supported by OpenManage Enterprise Modular. If an uplink is created using the same name as an existing uplink, the existing uplink is modified.

purestorage.flasharray
~~~~~~~~~~~~~~~~~~~~~~

- purefa_admin - Once `max_login` and `lockout` have been set there is currently no way to rest these to zero except through the FlashArray GUI

New Plugins
-----------

Callback
~~~~~~~~

- ovirt.ovirt.stdout - Output the log of ansible

Filter
~~~~~~

- community.general.counter - Counts hashable elements in a sequence
- community.hashi_vault.vault_login_token - Extracts the client token from a Vault login response

Inventory
~~~~~~~~~

- community.general.xen_orchestra - Xen Orchestra inventory source

Lookup
~~~~~~

- community.general.revbitspss - Get secrets from RevBits PAM server
- community.hashi_vault.vault_login - Perform a login operation against HashiCorp Vault
- community.hashi_vault.vault_token_create - Create a HashiCorp Vault token
- community.hashi_vault.vault_write - Perform a write operation against HashiCorp Vault

New Modules
-----------

arista.eos
~~~~~~~~~~

- arista.eos.eos_hostname - Manages hostname resource module
- arista.eos.eos_snmp_server - Manages snmp server resource module

cisco.ios
~~~~~~~~~

- cisco.ios.ios_hostname - hostname resource module
- cisco.ios.ios_snmp_server - snmp_server resource module

cisco.iosxr
~~~~~~~~~~~

- cisco.iosxr.iosxr_hostname - Manages hostname resource module
- cisco.iosxr.iosxr_snmp_server - Manages snmp-server resource module

cisco.nxos
~~~~~~~~~~

- cisco.nxos.nxos_hostname - Hostname resource module.
- cisco.nxos.nxos_snmp_server - SNMP Server resource module.

community.aws
~~~~~~~~~~~~~

- community.aws.cloudfront_response_headers_policy - Create, update and delete response headers policies to be used in a Cloudfront distribution
- community.aws.ec2_asg_instance_refresh - Start or cancel an EC2 Auto Scaling Group (ASG) instance refresh in AWS
- community.aws.ec2_asg_instance_refresh_info - Gather information about ec2 Auto Scaling Group (ASG) Instance Refreshes in AWS
- community.aws.ec2_asg_scheduled_action - Create, modify and delete ASG scheduled scaling actions.
- community.aws.rds_cluster - rds_cluster module
- community.aws.rds_cluster_info - Obtain information about one or more RDS clusters
- community.aws.sns_topic_info - sns_topic_info module

community.crypto
~~~~~~~~~~~~~~~~

- community.crypto.crypto_info - Retrieve cryptographic capabilities
- community.crypto.openssl_privatekey_convert - Convert OpenSSL private keys

community.digitalocean
~~~~~~~~~~~~~~~~~~~~~~

- community.digitalocean.digital_ocean_domain_record_info - Gather information about DigitalOcean domain records
- community.digitalocean.digital_ocean_spaces - Create and remove DigitalOcean Spaces.
- community.digitalocean.digital_ocean_spaces_info - List DigitalOcean Spaces.

community.general
~~~~~~~~~~~~~~~~~

Cloud
^^^^^

Scaleway
........

- community.general.scaleway_private_network - Scaleway private network management

Identity
^^^^^^^^

Keycloak
........

- community.general.keycloak_realm_info - Allows obtaining Keycloak realm public information via Keycloak API

Net Tools
^^^^^^^^^

- community.general.dnsimple_info - Pull basic info from DNSimple API

Packaging
^^^^^^^^^

Language
........

- community.general.cargo - Manage Rust packages with cargo

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

Storage
^^^^^^^

Pmem
....

- community.general.pmem - Configure Intel Optane Persistent Memory modules

System
^^^^^^

- community.general.homectl - Manage user accounts with systemd-homed
- community.general.sudoers - Manage sudoers files

community.grafana
~~~~~~~~~~~~~~~~~

- community.grafana.grafana_organization - Manage Grafana Organization

community.hashi_vault
~~~~~~~~~~~~~~~~~~~~~

- community.hashi_vault.vault_login - Perform a login operation against HashiCorp Vault
- community.hashi_vault.vault_pki_generate_certificate - Generates a new set of credentials (private key and certificate) using HashiCorp Vault PKI
- community.hashi_vault.vault_token_create - Create a HashiCorp Vault token
- community.hashi_vault.vault_write - Perform a write operation against HashiCorp Vault

community.postgresql
~~~~~~~~~~~~~~~~~~~~

- community.postgresql.postgresql_script - Run PostgreSQL statements from a file

community.sap
~~~~~~~~~~~~~

Database
^^^^^^^^

Saphana
.......

- community.sap.hana_query - Execute SQL on HANA

Files
^^^^^

- community.sap.sapcar_extract - Manages SAP SAPCAR archives

Identity
^^^^^^^^

- community.sap.sap_company - This module will manage a company entities in a SAP S4HANA environment
- community.sap.sap_user - This module will manage a user entities in a SAP S4/HANA environment

System
^^^^^^

- community.sap.sap_snote - This module will upload and (de)implements C(SNOTES) in a SAP S4HANA environment.
- community.sap.sap_system_facts - Gathers SAP facts in a host
- community.sap.sap_task_list_execute - Perform SAP Task list execution

community.vmware
~~~~~~~~~~~~~~~~

- community.vmware.vmware_host_user_manager - Manage users of ESXi

containers.podman
~~~~~~~~~~~~~~~~~

- containers.podman.podman_tag - Add an additional name to a local image

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- dellemc.openmanage.ome_application_alerts_smtp - This module allows to configure SMTP or email configurations
- dellemc.openmanage.ome_application_alerts_syslog - Configure syslog forwarding settings on OpenManage Enterprise and OpenManage Enterprise Modular
- dellemc.openmanage.ome_application_console_preferences - Configures console preferences on OpenManage Enterprise.
- dellemc.openmanage.ome_application_network_settings - This module allows you to configure the session inactivity timeout settings
- dellemc.openmanage.ome_application_security_settings - Configure the login security properties
- dellemc.openmanage.ome_device_local_access_configuration - Configure local access settings on OpenManage Enterprise Modular
- dellemc.openmanage.ome_device_network_services - Configure chassis network services settings on OpenManage Enterprise Modular
- dellemc.openmanage.ome_device_quick_deploy - Configure Quick Deploy settings on OpenManage Enterprise Modular
- dellemc.openmanage.ome_server_interface_profile_info - Retrieves the information of server interface profile on OpenManage Enterprise Modular.
- dellemc.openmanage.ome_server_interface_profiles - Configures server interface profiles on OpenManage Enterprise Modular.

inspur.sm
~~~~~~~~~

- inspur.sm.onboard_disk_info - Get onboard disks information.

junipernetworks.junos
~~~~~~~~~~~~~~~~~~~~~

- junipernetworks.junos.junos_hostname - Manage Hostname server configuration on Junos devices.
- junipernetworks.junos.junos_routing_options - Manage routing-options configuration on Junos devices.
- junipernetworks.junos.junos_security_policies - Manage security policies on Junos devices.
- junipernetworks.junos.junos_security_policies_global - Manage global security policy parameters on Junos devices.
- junipernetworks.junos.junos_security_zones - Manage security zones on Junos devices.
- junipernetworks.junos.junos_snmp_server - Manage SNMP server configuration on Junos devices.

kubernetes.core
~~~~~~~~~~~~~~~

- kubernetes.core.k8s_taint - Taint a node in a Kubernetes/OpenShift cluster

netapp.cloudmanager
~~~~~~~~~~~~~~~~~~~

- netapp.cloudmanager.na_cloudmanager_aws_fsx - Cloud ONTAP file system(FSX) in AWS

netapp.storagegrid
~~~~~~~~~~~~~~~~~~

- netapp.storagegrid.na_sg_grid_ha_group - Manage high availability (HA) group configuration on StorageGRID.
- netapp.storagegrid.na_sg_grid_traffic_classes - Manage Traffic Classification Policy configuration on StorageGRID.

netbox.netbox
~~~~~~~~~~~~~

- netbox.netbox.netbox_contact - Create, update or delete Contact objects in NetBox
- netbox.netbox.netbox_contact_group - Create, update or delete Contact Group objects in NetBox
- netbox.netbox.netbox_custom_field - Create, update or delete Custom fields in NetBox
- netbox.netbox.netbox_custom_link - Create, update or delete Custom links in NetBox
- netbox.netbox.netbox_export_template - Create, update or delete Export templates in NetBox
- netbox.netbox.netbox_provider_network - Create, update or delete Provider Network in NetBox
- netbox.netbox.netbox_webhook - Create, update or delete Webhooks in NetBox
- netbox.netbox.netbox_wireless_lan - Create, update or delete Wireless LAN objects in NetBox
- netbox.netbox.netbox_wireless_lan_group - Create, update or delete Wireless LAN Group objects in NetBox
- netbox.netbox.netbox_wireless_link - Create, update or delete Wireless Link objects in NetBox

purestorage.flasharray
~~~~~~~~~~~~~~~~~~~~~~

- purestorage.flasharray.purefa_admin - Configure Pure Storage FlashArray Global Admin settings
- purestorage.flasharray.purefa_saml - Manage FlashArray SAML2 service and identity providers

vyos.vyos
~~~~~~~~~

- vyos.vyos.vyos_hostname - Manages hostname resource module
- vyos.vyos.vyos_snmp_server - Manages snmp_server resource module

Unchanged Collections
---------------------

- ansible.posix (still version 1.3.0)
- cisco.asa (still version 2.1.0)
- cisco.nso (still version 1.0.3)
- community.azure (still version 1.1.0)
- community.ciscosmb (still version 1.0.4)
- community.fortios (still version 1.0.0)
- community.google (still version 1.0.0)
- community.kubernetes (still version 2.0.1)
- community.kubevirt (still version 1.0.0)
- community.libvirt (still version 1.0.2)
- community.okd (still version 2.1.0)
- community.rabbitmq (still version 1.1.0)
- community.routeros (still version 2.0.0)
- community.skydive (still version 1.0.0)
- cyberark.conjur (still version 1.1.0)
- cyberark.pas (still version 1.0.13)
- dellemc.enterprise_sonic (still version 1.1.0)
- dellemc.os10 (still version 1.1.1)
- dellemc.os6 (still version 1.0.7)
- dellemc.os9 (still version 1.0.4)
- frr.frr (still version 1.0.3)
- gluster.gluster (still version 1.0.2)
- google.cloud (still version 1.0.2)
- hetzner.hcloud (still version 1.6.0)
- ibm.qradar (still version 1.0.3)
- mellanox.onyx (still version 1.0.0)
- netapp.aws (still version 21.7.0)
- netapp.azure (still version 21.10.0)
- netapp.elementsw (still version 21.7.0)
- netapp.um_info (still version 21.8.0)
- ngine_io.exoscale (still version 1.0.0)
- servicenow.servicenow (still version 1.0.6)
- splunk.es (still version 1.0.2)
- wti.remote (still version 1.0.3)
