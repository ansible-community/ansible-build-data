=======================
Ansible 5 Release Notes
=======================

This changelog describes changes since Ansible 4.0.0.

.. contents::
  :local:
  :depth: 2

v5.0.0a2
========

.. contents::
  :local:
  :depth: 2

Release Summary
---------------

Release Date: 2021-10-19

`Porting Guide <https://docs.ansible.com/ansible/devel/porting_guides.html>`_

Ansible-core
------------

Ansible 5.0.0a2 contains Ansible-core version 2.12.0rc1.
This is a newer version than version 2.12.0b1 contained in the previous Ansible release.

The changes are reported in the combined changelog below.

Changed Collections
-------------------

If not mentioned explicitly, the changes are reported in the combined changelog below.

+---------------------+-----------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| Collection          | Ansible 5.0.0a1 | Ansible 5.0.0a2 | Notes                                                                                                                        |
+=====================+=================+=================+==============================================================================================================================+
| ansible.utils       | 2.4.1           | 2.4.2           | There are no changes recorded in the changelog.                                                                              |
+---------------------+-----------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| check_point.mgmt    | 2.0.0           | 2.1.0           | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+---------------------+-----------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.aci           | 2.0.0           | 2.1.0           |                                                                                                                              |
+---------------------+-----------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.asa           | 2.0.3           | 2.1.0           |                                                                                                                              |
+---------------------+-----------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.meraki        | 2.4.2           | 2.5.0           | The collection did not have a changelog in this version.                                                                     |
+---------------------+-----------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.crypto    | 1.9.4           | 1.9.5           |                                                                                                                              |
+---------------------+-----------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.dns       | 2.0.0           | 2.0.1           |                                                                                                                              |
+---------------------+-----------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.general   | 3.7.0           | 3.8.0           |                                                                                                                              |
+---------------------+-----------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.mysql     | 2.3.0           | 2.3.1           |                                                                                                                              |
+---------------------+-----------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.routeros  | 2.0.0-a1        | 2.0.0-a2        |                                                                                                                              |
+---------------------+-----------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.vmware    | 1.14.0          | 1.15.0          |                                                                                                                              |
+---------------------+-----------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| netapp.cloudmanager | 21.10.0         | 21.11.0         |                                                                                                                              |
+---------------------+-----------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| netapp.ontap        | 21.11.0         | 21.12.0         |                                                                                                                              |
+---------------------+-----------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| netbox.netbox       | 3.1.2           | 3.2.0           |                                                                                                                              |
+---------------------+-----------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+

Minor Changes
-------------

Ansible-core
~~~~~~~~~~~~

- ansible-test - Update the ``base`` and ``default`` containers from Python 3.10.0rc2 to 3.10.0.

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

community.general
~~~~~~~~~~~~~~~~~

- mail - added the ``ehlohost`` parameter which allows for manual override of the host used in SMTP EHLO (https://github.com/ansible-collections/community.general/pull/3425).
- nmcli - the option ``routing_rules4`` can now be specified as a list of strings, instead of as a single string (https://github.com/ansible-collections/community.general/issues/3401).
- open-iscsi - adding support for mutual authentication between target and initiator (https://github.com/ansible-collections/community.general/pull/3422).
- opentelemetry callback plugin - added option ``enable_from_environment`` to support enabling the plugin only if the given environment variable exists and it is set to true (https://github.com/ansible-collections/community.general/pull/3498).
- opentelemetry callback plugin - enriched the stacktrace information with the ``message``, ``exception`` and ``stderr`` fields from the failed task (https://github.com/ansible-collections/community.general/pull/3496).
- pkgng - packages being installed (or upgraded) are acted on in one command (per action) (https://github.com/ansible-collections/community.general/issues/2265).
- pkgng - status message specifies number of packages installed and/or upgraded separately. Previously, all changes were reported as one count of packages "added" (https://github.com/ansible-collections/community.general/pull/3393).
- terraform - add ``parallelism`` parameter (https://github.com/ansible-collections/community.general/pull/3540).
- ufw - if ``delete=true`` and ``insert`` option is present, then ``insert`` is now ignored rather than failing with a syntax error (https://github.com/ansible-collections/community.general/pull/3514).

community.routeros
~~~~~~~~~~~~~~~~~~

- api - make validation of ``WHERE`` for ``query`` more strict (https://github.com/ansible-collections/community.routeros/pull/53).

community.vmware
~~~~~~~~~~~~~~~~

- vm_device_helper - move NIC device types from vmware_guest module to vm_device_helper (https://github.com/ansible-collections/community.vmware/pull/998).

netapp.cloudmanager
~~~~~~~~~~~~~~~~~~~

- Add CVO modification unit tests
- Adding new parameter ``capacity_package_name`` for all CVOs creation with capacity based ``license_type`` capacity-paygo or ha-capacity-paygo for HA.
- all modules - better error reporting if refresh_token is not valid.
- na_cloudmanager_connector_gcp - automatically fetch client_id for delete.
- na_cloudmanager_connector_gcp - make the module idempotent for create and delete.
- na_cloudmanager_connector_gcp - report client_id if connector already exists.
- na_cloudmanager_cvo_aws - Add unit tests for capacity based license support.
- na_cloudmanager_cvo_azure - Add unit tests for capacity based license support.
- na_cloudmanager_cvo_gcp - Add unit tests for capacity based license support and delete cvo.
- netapp.py - improve error handling with error content.

netapp.ontap
~~~~~~~~~~~~

- na_ontap_cluster - Added REST support to the cluster module.
- na_ontap_firewall_policy - added ``none`` as a choice for ``service`` which is supported from 9.8 ONTAP onwards.
- na_ontap_svm - new option ``max_volumes``.
- na_ontap_svm - support ``allowed protocols`` with REST for ONTAP 9.6 and later.

netbox.netbox
~~~~~~~~~~~~~

- Add connected-devices to nb_lookup [#540](https://github.com/netbox-community/ansible_modules/pull/540)
- Add location and power panel as lookup keys to nb_lookup [#599](https://github.com/netbox-community/ansible_modules/pull/599)
- netbox_device_interface and netbox_vm_interface - Add parent interface to modules [#604](https://github.com/netbox-community/ansible_modules/pull/604)
- netbox_virtual_machine - Change vCPU to float from int (to reflect NetBox 3.0) [#605](https://github.com/netbox-community/ansible_modules/pull/605)

Breaking Changes / Porting Guide
--------------------------------

community.routeros
~~~~~~~~~~~~~~~~~~

- api - splitting commands no longer uses a naive split by whitespace, but a more RouterOS CLI compatible splitting algorithm (https://github.com/ansible-collections/community.routeros/pull/45).
- command - the module now always indicates that a change happens. If this is not correct, please use ``changed_when`` to determine the correct changed status for a task (https://github.com/ansible-collections/community.routeros/pull/50).

Deprecated Features
-------------------

community.vmware
~~~~~~~~~~~~~~~~

- vmware_guest_vnc -  Sphere 7.0 removed the built-in VNC server (https://docs.vmware.com/en/VMware-vSphere/7.0/rn/vsphere-esxi-vcenter-server-70-release-notes.html#productsupport).

Security Fixes
--------------

Ansible-core
~~~~~~~~~~~~

- Do not include params in exception when a call to ``set_options`` fails. Additionally, block the exception that is returned from being displayed to stdout. (CVE-2021-3620)

Bugfixes
--------

Ansible-core
~~~~~~~~~~~~

- ansible-test - Fix path to inventory file for ``windows-integration`` and ``network-integration`` commands for collections.
- ansible-test - Update distribution test containers to version 3.1.0.
- ansible-test - Use the correct variable to reference the client's SSH key when generating inventory.
- ansible-test pslint - Fix error when encountering validation results that are highly nested - https://github.com/ansible/ansible/issues/74151

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

- Fixes asa_acls to add the support for service object group under destination option ((https://github.com/ansible-collections/cisco.asa/issues/100).

community.crypto
~~~~~~~~~~~~~~~~

- get_certificate - fix compatibility with the cryptography 35.0.0 release (https://github.com/ansible-collections/community.crypto/pull/294).
- openssl_csr_info - fix compatibility with the cryptography 35.0.0 release (https://github.com/ansible-collections/community.crypto/pull/294).
- openssl_csr_info - fix compatibility with the cryptography 35.0.0 release in PyOpenSSL backend (https://github.com/ansible-collections/community.crypto/pull/300).
- openssl_pkcs12 - fix compatibility with the cryptography 35.0.0 release (https://github.com/ansible-collections/community.crypto/pull/296).
- x509_certificate_info - fix compatibility with the cryptography 35.0.0 release (https://github.com/ansible-collections/community.crypto/pull/294).
- x509_certificate_info - fix compatibility with the cryptography 35.0.0 release in PyOpenSSL backend (https://github.com/ansible-collections/community.crypto/pull/300).

community.dns
~~~~~~~~~~~~~

- Update Public Suffix List.

community.general
~~~~~~~~~~~~~~~~~

- gitlab_deploy_key - fix idempotency on projects with multiple deploy keys (https://github.com/ansible-collections/community.general/pull/3473).
- gitlab_group - avoid passing wrong value for ``require_two_factor_authentication`` on creation when the option has not been specified (https://github.com/ansible-collections/community.general/pull/3453).
- gitlab_group_members - ``get_group_id`` return the group ID by matching ``full_path``, ``path`` or ``name`` (https://github.com/ansible-collections/community.general/pull/3400).
- jboss - fix the deployment file permission issue when Jboss server is running under non-root user. The deployment file is copied with file content only. The file permission is set to ``440`` and belongs to root user. When the JBoss ``WildFly`` server is running under non-root user, it is unable to read the deployment file (https://github.com/ansible-collections/community.general/pull/3426).
- keycloak_authentication - fix bug, the requirement was always on ``DISABLED`` when creating a new authentication flow (https://github.com/ansible-collections/community.general/pull/3330).
- keycloak_identity_provider - fix change detection when updating identity provider mappers (https://github.com/ansible-collections/community.general/pull/3538, https://github.com/ansible-collections/community.general/issues/3537).
- keycloak_role - quote role name when used in URL path to avoid errors when role names contain special characters (https://github.com/ansible-collections/community.general/issues/3535, https://github.com/ansible-collections/community.general/pull/3536).
- logstash callback plugin - replace ``_option`` with ``context.CLIARGS`` to fix the plugin on ansible-base and ansible-core (https://github.com/ansible-collections/community.general/issues/2692).
- macports - add ``stdout`` and ``stderr`` to return values (https://github.com/ansible-collections/community.general/issues/3499).
- opentelemetry callback plugin - validated the task result exception without crashing. Also simplifying code a bit (https://github.com/ansible-collections/community.general/pull/3450, https://github.com/ansible/ansible/issues/75726).
- yaml callback plugin - avoid modifying PyYAML so that other plugins using it on the controller, like the ``to_yaml`` filter, do not produce different output (https://github.com/ansible-collections/community.general/issues/3471, https://github.com/ansible-collections/community.general/pull/3478).
- zypper_repository - when an URL to a .repo file was provided in option ``repo=`` and ``state=present`` only the first run was successful, future runs failed due to missing checks prior starting zypper. Usage of ``state=absent`` in combination with a .repo file was not working either (https://github.com/ansible-collections/community.general/issues/1791, https://github.com/ansible-collections/community.general/issues/3466).

community.mysql
~~~~~~~~~~~~~~~

- mysql_user - Fix crash reporting ``Invalid privileges specified`` when passing privileges that became aliases (https://github.com/ansible-collections/community.mysql/issues/232).

community.routeros
~~~~~~~~~~~~~~~~~~

- api - improve splitting of ``WHERE`` queries (https://github.com/ansible-collections/community.routeros/pull/47).
- api - when converting result lists to dictionaries, no longer removes second ``=`` and text following that if present (https://github.com/ansible-collections/community.routeros/pull/47).
- routeros cliconf plugin - adjust function signature that was modified in Ansible after creation of this plugin (https://github.com/ansible-collections/community.routeros/pull/43).

community.vmware
~~~~~~~~~~~~~~~~

- Fix a bug that prevented enabling VSAN on more than one vmk, risking splitting the whole cluster during interface migration scenarios (https://github.com/ansible-collections/community.vmware/issues/891)
- vmware_deploy_ovf - Fix deploy ovf issue when there are more than one datacenter in VC (https://github.com/ansible-collections/community.vmware/issues/164).
- vmware_deploy_ovf - fixed to display suitable the error when not exist an ovf file path (https://github.com/ansible-collections/community.vmware/pull/1065).
- vmware_guest_powerstate - handle 'present' state as 'poweredon' (https://github.com/ansible-collections/community.vmware/pull/1033).
- vmware_guest_tools_wait - add documentation about datacenter parameter (https://github.com/ansible-collections/community.vmware/pull/870).
- vmware_object_rename - fixed an issue that an error has occurred when getting than 1,000 objects (https://github.com/ansible-collections/community.vmware/pull/1010).
- vmware_vcenter_settings_info - fix to return all VCSA settings when setting vsphere to the schema and not specifying the properties (https://github.com/ansible-collections/community.vmware/pull/1050).
- vmware_vm_inventory - remove erroneous ``ansible_host`` condition (https://github.com/ansible-collections/community.vmware/issues/975).

netapp.cloudmanager
~~~~~~~~~~~~~~~~~~~

- na_cloudmanager_connector_gcp - typeError when using proxy certificates.

netapp.ontap
~~~~~~~~~~~~

- na_ontap_job_schedule - cannot modify options not present in create when using REST.
- na_ontap_job_schedule - fix idempotency issue with ZAPI when job_minutes is set to -1.
- na_ontap_job_schedule - modify error if month is changed from some values to all (-1) when using REST.
- na_ontap_job_schedule - modify error if month is present but not changed with 0 offset when using REST.
- na_ontap_vserver_delete role - fix typos for cifs.

netbox.netbox
~~~~~~~~~~~~~

- Copy interfaces before processing [#556](https://github.com/netbox-community/ansible_modules/pull/556)
- Make attached_ips subscriptable. [#609](https://github.com/netbox-community/ansible_modules/pull/609)

New Plugins
-----------

Callback
~~~~~~~~

- community.general.elastic - Create distributed traces for each Ansible task in Elastic APM

Filter
~~~~~~

- community.routeros.join - Join a list of arguments to a command
- community.routeros.list_to_dict - Convert a list of arguments to a list of dictionary
- community.routeros.quote_argument - Quote an argument
- community.routeros.quote_argument_value - Quote an argument value
- community.routeros.split - Split a command into arguments

Inventory
~~~~~~~~~

- community.general.opennebula - OpenNebula inventory source

New Modules
-----------

community.general
~~~~~~~~~~~~~~~~~

Cloud
^^^^^

Misc
....

- community.general.proxmox_tasks_info - Retrieve information about one or more Proxmox VE tasks

Packaging
^^^^^^^^^

Language
........

- community.general.pipx - Manages applications installed with pipx

Web Infrastructure
^^^^^^^^^^^^^^^^^^

- community.general.rundeck_job_executions_info - Query executions for a Rundeck job
- community.general.rundeck_job_run - Run a Rundeck job

community.vmware
~~~~~~~~~~~~~~~~

- community.vmware.vmware_vm_config_option - Return supported guest ID list and VM recommended config option for specific guest OS

Unchanged Collections
---------------------

- amazon.aws (still version 2.0.0)
- ansible.netcommon (still version 2.4.0)
- ansible.posix (still version 1.3.0)
- ansible.windows (still version 1.7.3)
- arista.eos (still version 3.1.0)
- awx.awx (still version 19.4.0)
- azure.azcollection (still version 1.9.0)
- chocolatey.chocolatey (still version 1.1.0)
- cisco.intersight (still version 1.0.17)
- cisco.ios (still version 2.5.0)
- cisco.iosxr (still version 2.5.0)
- cisco.mso (still version 1.2.0)
- cisco.nso (still version 1.0.3)
- cisco.nxos (still version 2.7.0)
- cisco.ucs (still version 1.6.0)
- cloudscale_ch.cloud (still version 2.2.0)
- community.aws (still version 2.0.0)
- community.azure (still version 1.0.0)
- community.ciscosmb (still version 1.0.4)
- community.digitalocean (still version 1.10.0)
- community.docker (still version 1.10.0)
- community.fortios (still version 1.0.0)
- community.google (still version 1.0.0)
- community.grafana (still version 1.2.3)
- community.hashi_vault (still version 1.3.2)
- community.hrobot (still version 1.1.1)
- community.kubernetes (still version 2.0.0)
- community.kubevirt (still version 1.0.0)
- community.libvirt (still version 1.0.2)
- community.mongodb (still version 1.3.1)
- community.network (still version 3.0.0)
- community.okd (still version 2.0.1)
- community.postgresql (still version 1.5.0)
- community.proxysql (still version 1.3.0)
- community.rabbitmq (still version 1.1.0)
- community.skydive (still version 1.0.0)
- community.sops (still version 1.1.0)
- community.windows (still version 1.7.0)
- community.zabbix (still version 1.4.0)
- containers.podman (still version 1.8.1)
- cyberark.conjur (still version 1.1.0)
- cyberark.pas (still version 1.0.7)
- dellemc.enterprise_sonic (still version 1.1.0)
- dellemc.openmanage (still version 4.1.0)
- dellemc.os10 (still version 1.1.1)
- dellemc.os6 (still version 1.0.7)
- dellemc.os9 (still version 1.0.4)
- f5networks.f5_modules (still version 1.11.1)
- fortinet.fortimanager (still version 2.1.3)
- fortinet.fortios (still version 2.1.2)
- frr.frr (still version 1.0.3)
- gluster.gluster (still version 1.0.2)
- google.cloud (still version 1.0.2)
- hetzner.hcloud (still version 1.6.0)
- hpe.nimble (still version 1.1.3)
- ibm.qradar (still version 1.0.3)
- infinidat.infinibox (still version 1.2.4)
- inspur.sm (still version 1.3.0)
- junipernetworks.junos (still version 2.6.0)
- kubernetes.core (still version 2.2.0)
- mellanox.onyx (still version 1.0.0)
- netapp.aws (still version 21.6.0)
- netapp.azure (still version 21.9.0)
- netapp.elementsw (still version 21.6.1)
- netapp.um_info (still version 21.7.0)
- netapp_eseries.santricity (still version 1.2.13)
- ngine_io.cloudstack (still version 2.2.1)
- ngine_io.exoscale (still version 1.0.0)
- ngine_io.vultr (still version 1.1.0)
- openstack.cloud (still version 1.5.1)
- openvswitch.openvswitch (still version 2.0.2)
- ovirt.ovirt (still version 1.6.4)
- purestorage.flasharray (still version 1.11.0)
- purestorage.flashblade (still version 1.7.0)
- sensu.sensu_go (still version 1.12.0)
- servicenow.servicenow (still version 1.0.6)
- splunk.es (still version 1.0.2)
- t_systems_mms.icinga_director (still version 1.23.0)
- theforeman.foreman (still version 2.2.0)
- vyos.vyos (still version 2.6.0)
- wti.remote (still version 1.0.1)

v5.0.0a1
========

.. contents::
  :local:
  :depth: 2

Release Summary
---------------

Release Date: 2021-10-05

`Porting Guide <https://docs.ansible.com/ansible/devel/porting_guides.html>`_

Ansible-core
------------

Ansible 5.0.0a1 contains Ansible-core version 2.12.0b1.
This is a newer version than version 2.11.0 contained in the previous Ansible release.

The changes are reported in the combined changelog below.

Included Collections
--------------------

If not mentioned explicitly, the changes are reported in the combined changelog below.

+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| Collection                    | Ansible 4.0.0 | Ansible 5.0.0a1 | Notes                                                                                                                        |
+===============================+===============+=================+==============================================================================================================================+
| amazon.aws                    | 1.5.0         | 2.0.0           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| ansible.netcommon             | 2.0.2         | 2.4.0           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| ansible.posix                 | 1.2.0         | 1.3.0           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| ansible.utils                 | 2.1.0         | 2.4.1           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| ansible.windows               | 1.5.0         | 1.7.3           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| arista.eos                    | 2.1.1         | 3.1.0           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| awx.awx                       | 19.0.0        | 19.4.0          | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| azure.azcollection            | 1.5.0         | 1.9.0           | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.asa                     | 2.0.1         | 2.0.3           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.intersight              | 1.0.15        | 1.0.17          | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.ios                     | 2.0.1         | 2.5.0           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.iosxr                   | 2.1.0         | 2.5.0           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.meraki                  | 2.2.1         | 2.4.2           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.mso                     | 1.1.0         | 1.2.0           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.nxos                    | 2.2.0         | 2.7.0           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| cloudscale_ch.cloud           | 2.1.0         | 2.2.0           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.aws                 | 1.5.0         | 2.0.0           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.ciscosmb            |               | 1.0.4           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.crypto              | 1.6.2         | 1.9.4           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.digitalocean        | 1.1.1         | 1.10.0          |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.dns                 |               | 2.0.0           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.docker              | 1.5.0         | 1.10.0          |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.general             | 3.0.2         | 3.7.0           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.grafana             | 1.2.1         | 1.2.3           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.hashi_vault         | 1.1.3         | 1.3.2           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.kubernetes          | 1.2.1         | 2.0.0           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.libvirt             | 1.0.1         | 1.0.2           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.mongodb             | 1.2.1         | 1.3.1           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.mysql               | 2.1.0         | 2.3.0           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.okd                 | 1.1.2         | 2.0.1           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.postgresql          | 1.2.0         | 1.5.0           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.proxysql            | 1.0.0         | 1.3.0           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.rabbitmq            | 1.0.3         | 1.1.0           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.routeros            | 1.1.0         | 2.0.0-a1        |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.sops                | 1.0.6         | 1.1.0           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.vmware              | 1.9.0         | 1.14.0          |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.windows             | 1.3.0         | 1.7.0           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.zabbix              | 1.3.0         | 1.4.0           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| containers.podman             | 1.5.0         | 1.8.1           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| cyberark.pas                  | 1.0.6         | 1.0.7           | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| dellemc.enterprise_sonic      | 1.0.3         | 1.1.0           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| dellemc.openmanage            | 3.3.0         | 4.1.0           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| f5networks.f5_modules         | 1.9.0         | 1.11.1          |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| fortinet.fortimanager         | 2.0.2         | 2.1.3           | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| fortinet.fortios              | 2.0.1         | 2.1.2           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| gluster.gluster               | 1.0.1         | 1.0.2           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| hetzner.hcloud                | 1.4.3         | 1.6.0           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| inspur.sm                     | 1.1.4         | 1.3.0           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| junipernetworks.junos         | 2.1.0         | 2.6.0           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| kubernetes.core               | 1.2.1         | 2.2.0           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| netapp.aws                    | 21.2.0        | 21.6.0          |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| netapp.azure                  | 21.5.0        | 21.9.0          |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| netapp.cloudmanager           | 21.5.1        | 21.10.0         |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| netapp.elementsw              | 21.3.0        | 21.6.1          |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| netapp.ontap                  | 21.5.0        | 21.11.0         |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| netapp.um_info                | 21.5.0        | 21.7.0          |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| netapp_eseries.santricity     | 1.2.7         | 1.2.13          |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| netbox.netbox                 | 3.0.0         | 3.1.2           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| ngine_io.cloudstack           | 2.1.0         | 2.2.1           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| openstack.cloud               | 1.4.0         | 1.5.1           | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| openvswitch.openvswitch       | 2.0.0         | 2.0.2           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| ovirt.ovirt                   | 1.4.2         | 1.6.4           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| purestorage.flasharray        | 1.8.0         | 1.11.0          |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| purestorage.flashblade        | 1.6.0         | 1.7.0           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| sensu.sensu_go                | 1.9.4         | 1.12.0          |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| servicenow.servicenow         | 1.0.5         | 1.0.6           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| t_systems_mms.icinga_director | 1.16.0        | 1.23.0          |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| theforeman.foreman            | 2.0.1         | 2.2.0           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| vyos.vyos                     | 2.2.0         | 2.6.0           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+

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
- amazon.aws collection - The amazon.aws collection has dropped support for ``botocore<1.16.0`` and ``boto3<1.13.0``. Most modules will continue to work with older versions of the AWS SDK, however compatability with older versions of the SDK is not guaranteed and will not be tested. When using older versions of the SDK a warning will be emitted by Ansible (https://github.com/ansible-collections/amazon.aws/pull/442).
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

community.ciscosmb
~~~~~~~~~~~~~~~~~~

- Python 2.6, 2.7, 3.5 is required
- add CBS350 support
- add antsibull-changelog support
- add ciscosmb_command
- added facts subset "interfaces"
- ciscosmb_facts with default subset and unit tests
- interface name canonicalization
- transform collection qaxi.ciscosmb to community.ciscosmb
- transform community.ciscosmb.ciscosmb_command to community.ciscosmb.command
- transform community.ciscosmb.ciscosmb_facts to community.ciscosmb.facts
- unit tests for CBS350

community.dns
~~~~~~~~~~~~~

- hosttech_* modules - support the new JSON API at https://api.ns1.hosttech.eu/api/documentation/ (https://github.com/ansible-collections/community.dns/pull/4).

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

- Improve ``fortios_configuration_fact`` to use multiple selectors concurrently.
- New module fortios_monitor_fact.
- Support Fortios 7.0.
- Support Log APIs.
- Support ``check_mode`` in all cofigurationAPI-based modules.
- Support filtering for fact gathering modules ``fortios_configuration_fact`` and ``fortios_monitor_fact``.
- Support moving policy in ``firewall_central_snat_map``.
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
- aws_ssm - add "on_missing" and "on_denied" option (https://github.com/ansible-collections/amazon.aws/pull/370).
- cloudformation - Tests for compatability with older versions of the AWS SDKs have been removed (https://github.com/ansible-collections/amazon.aws/pull/442).
- ec2_ami - ensure tags are propagated to the snapshot(s) when creating an AMI (https://github.com/ansible-collections/amazon.aws/pull/437).
- ec2_eni - fix idempotency when ``security_groups`` attribute is specified (https://github.com/ansible-collections/amazon.aws/pull/337).
- ec2_eni - timeout increased when waiting for ENIs to finish detaching (https://github.com/ansible-collections/amazon.aws/pull/501).
- ec2_group - Tests for compatability with older versions of the AWS SDKs have been removed (https://github.com/ansible-collections/amazon.aws/pull/442).
- ec2_group - use a generator rather than list comprehension (https://github.com/ansible-collections/amazon.aws/pull/465).
- ec2_group - use system ipaddress module, available with Python >= 3.3, instead of vendored copy (https://github.com/ansible-collections/amazon.aws/pull/461).
- ec2_instance - Tests for compatability with older versions of the AWS SDKs have been removed (https://github.com/ansible-collections/amazon.aws/pull/442).
- ec2_instance - add ``throughput`` parameter for gp3 volume types (https://github.com/ansible-collections/amazon.aws/pull/433).
- ec2_instance - add support for controlling metadata options (https://github.com/ansible-collections/amazon.aws/pull/414).
- ec2_instance - remove unnecessary raise when exiting with a failure (https://github.com/ansible-collections/amazon.aws/pull/460).
- ec2_instance_info - Tests for compatability with older versions of the AWS SDKs have been removed (https://github.com/ansible-collections/amazon.aws/pull/442).
- ec2_snapshot - migrated to use the boto3 python library (https://github.com/ansible-collections/amazon.aws/pull/356).
- ec2_spot_instance_info - Added a new module that describes the specified Spot Instance requests (https://github.com/ansible-collections/amazon.aws/pull/487).
- ec2_vol - add parameter ``multi_attach`` to support Multi-Attach on volume creation/update (https://github.com/ansible-collections/amazon.aws/pull/362).
- ec2_vol - relax the boto3/botocore requirements and only require botocore 1.19.27 for modifying the ``throughput`` parameter (https://github.com/ansible-collections/amazon.aws/pull/346).
- ec2_vpc_dhcp_option - Now also returns a boto3-style resource description in the ``dhcp_options`` result key.  This includes any tags for the ``dhcp_options_id`` and has the same format as the current return value of ``ec2_vpc_dhcp_option_info``. (https://github.com/ansible-collections/amazon.aws/pull/252)
- ec2_vpc_dhcp_option_info - Now also returns a user-friendly ``dhcp_config`` key that matches the historical ``new_config`` key from ec2_vpc_dhcp_option, and alleviates the need to use ``items2dict(key_name='key', value_name='values')`` when parsing the output of the module. (https://github.com/ansible-collections/amazon.aws/pull/252)
- ec2_vpc_subnet - Tests for compatability with older versions of the AWS SDKs have been removed (https://github.com/ansible-collections/amazon.aws/pull/442).
- integration tests - remove dependency with collection ``community.general`` (https://github.com/ansible-collections/amazon.aws/pull/361).
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

- meraki_ms_switchport - Adding additional functionality to support the access_policy_types "MAC allow list" and "Sticky MAC allow list" port security configuration options. (https://github.com/CiscoDevNet/ansible-meraki/issues/227).
- meraki_mx_intrusion_prevention - Rename message to rule_message to avoid conflicts with internal Ansible variables.
- meraki_mx_switchport - Improve documentation for response

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

- aws_eks_cluster - Tests for compatability with older versions of the AWS SDKs have been removed (https://github.com/ansible-collections/community.aws/pull/675).
- aws_kms_info - use a generator rather than list comprehension (https://github.com/ansible-collections/community.aws/pull/688).
- aws_s3_bucket_info - added test for botocore>=1.18.11 when attempting to fetch bucket ownership controls (https://github.com/ansible-collections/community.aws/pull/682)
- aws_ses_rule_set - use a generator rather than list comprehension (https://github.com/ansible-collections/community.aws/pull/688).
- aws_sgw_info - ensure module runs in check_mode (https://github.com/ansible-collections/community.aws/issues/659).
- cloudformation_exports_info - ensure module runs in check_mode (https://github.com/ansible-collections/community.aws/issues/659).
- cloudformation_stack_set - Tests for compatability with older versions of the AWS SDKs have been removed (https://github.com/ansible-collections/community.aws/pull/675).
- cloudfront_info - ensure module runs in check_mode (https://github.com/ansible-collections/community.aws/issues/659).
- cloudwatchevent_rule - use a generator rather than list comprehension (https://github.com/ansible-collections/community.aws/pull/688).
- dynamodb_table - Tests for compatability with older versions of the AWS SDKs have been removed (https://github.com/ansible-collections/community.aws/pull/675).
- dynamodb_ttl - Tests for compatability with older versions of the AWS SDKs have been removed (https://github.com/ansible-collections/community.aws/pull/675).
- ec2_ami_copy - Tests for compatability with older versions of the AWS SDKs have been removed (https://github.com/ansible-collections/community.aws/pull/675).
- ec2_asg - Tests for compatability with older versions of the AWS SDKs have been removed (https://github.com/ansible-collections/community.aws/pull/675).
- ec2_asg_info - ensure module runs in check_mode (https://github.com/ansible-collections/community.aws/issues/659).
- ec2_launch_template - Tests for compatability with older versions of the AWS SDKs have been removed (https://github.com/ansible-collections/community.aws/pull/675).
- ec2_lc_info - ensure module runs in check_mode (https://github.com/ansible-collections/community.aws/issues/659).
- ec2_transit_gateway - Tests for compatability with older versions of the AWS SDKs have been removed (https://github.com/ansible-collections/community.aws/pull/675).
- ec2_transit_gateway_info - Tests for compatability with older versions of the AWS SDKs have been removed (https://github.com/ansible-collections/community.aws/pull/675).
- ec2_vpc_peer - Tests for compatability with older versions of the AWS SDKs have been removed (https://github.com/ansible-collections/community.aws/pull/675).
- ec2_vpc_peer - use shared code for tagging peering connections (https://github.com/ansible-collections/community.aws/pull/614).
- ec2_vpc_route_table - use shared code for tagging route tables (https://github.com/ansible-collections/community.aws/pull/616).
- ec2_vpc_vgw - fix arguments-renamed pylint issue (https://github.com/ansible-collections/community.aws/pull/686).
- ec2_vpc_vpn - fix arguments-renamed pylint issue (https://github.com/ansible-collections/community.aws/pull/686).
- ecs_ecr - Tests for compatability with older versions of the AWS SDKs have been removed (https://github.com/ansible-collections/community.aws/pull/675).
- ecs_service - Tests for compatability with older versions of the AWS SDKs have been removed (https://github.com/ansible-collections/community.aws/pull/675).
- ecs_task - Tests for compatability with older versions of the AWS SDKs have been removed (https://github.com/ansible-collections/community.aws/pull/675).
- ecs_task - remove unused import (https://github.com/ansible-collections/community.aws/pull/686).
- ecs_taskdefinition - Tests for compatability with older versions of the AWS SDKs have been removed (https://github.com/ansible-collections/community.aws/pull/675).
- efs - Tests for compatability with older versions of the AWS SDKs have been removed (https://github.com/ansible-collections/community.aws/pull/675).
- efs_info - Tests for compatability with older versions of the AWS SDKs have been removed (https://github.com/ansible-collections/community.aws/pull/675).
- elasticache_subnet_group - add return values (https://github.com/ansible-collections/community.aws/pull/723).
- elasticache_subnet_group - add support for check_mode (https://github.com/ansible-collections/community.aws/pull/723).
- elasticache_subnet_group - module migrated to boto3 AWS SDK (https://github.com/ansible-collections/community.aws/pull/723).
- elb_application_lb - added ``ip_address_type`` parameter to support changing application load balancer configuration (https://github.com/ansible-collections/community.aws/pull/499).
- elb_application_lb_info - added ``ip_address_type`` in output when gathering application load balancer parameters (https://github.com/ansible-collections/community.aws/pull/499).
- elb_instance - make elb_instance idempotent when deregistering instances.  Merged from ec2_elb U(https://github.com/ansible/ansible/pull/31660).
- elb_network_lb - added ``ip_address_type`` parameter to support changing network load balancer configuration (https://github.com/ansible-collections/community.aws/pull/499).
- elb_target_group - Tests for compatability with older versions of the AWS SDKs have been removed (https://github.com/ansible-collections/community.aws/pull/675).
- elb_target_group - use a generator rather than list comprehension (https://github.com/ansible-collections/community.aws/pull/688).
- iam - use a generator rather than list comprehension (https://github.com/ansible-collections/community.aws/pull/688).
- iam_group - use a generator rather than list comprehension (https://github.com/ansible-collections/community.aws/pull/688).
- iam_mfa_device_info - ensure module runs in check_mode (https://github.com/ansible-collections/community.aws/issues/659).
- iam_role - Tests for compatability with older versions of the AWS SDKs have been removed (https://github.com/ansible-collections/community.aws/pull/675).
- iam_role - use a generator rather than list comprehension (https://github.com/ansible-collections/community.aws/pull/688).
- iam_server_certificate_info - ensure module runs in check_mode (https://github.com/ansible-collections/community.aws/issues/659).
- iam_user - use a generator rather than list comprehension (https://github.com/ansible-collections/community.aws/pull/688).
- kms_info - added a new ``keys_attr`` parameter to continue returning the key details in the ``keys`` attribute as well as the ``kms_keys`` attribute (https://github.com/ansible-collections/community.aws/pull/648).
- lambda - Tests for compatability with older versions of the AWS SDKs have been removed (https://github.com/ansible-collections/community.aws/pull/675).
- rds_instance - Tests for compatability with older versions of the AWS SDKs have been removed (https://github.com/ansible-collections/community.aws/pull/675).
- rds_instance - convert ``preferred_maintenance_window`` days into lowercase so changed returns properly (https://github.com/ansible-collections/community.aws/pull/516).
- rds_instance - use a generator rather than list comprehension (https://github.com/ansible-collections/community.aws/pull/688).
- route53 - add rate-limiting retries while waiting for changes to propagate (https://github.com/ansible-collections/community.aws/pull/564).
- route53 - add retries on ``PriorRequestNotComplete`` errors (https://github.com/ansible-collections/community.aws/pull/564).
- route53 - update retry ``max_delay`` setting so that it can be set above 60 seconds (https://github.com/ansible-collections/community.aws/pull/564).
- sns_topic - Added ``topic_type`` parameter to select type of SNS topic (either FIFO or Standard) (https://github.com/ansible-collections/community.aws/pull/599).
- sqs_queue - Tests for compatability with older versions of the AWS SDKs have been removed (https://github.com/ansible-collections/community.aws/pull/675).
- various community.aws modules - remove unused imports (https://github.com/ansible-collections/community.aws/pull/629)
- wafv2_resources_info - ensure module runs in check_mode (https://github.com/ansible-collections/community.aws/issues/659).
- wafv2_web_acl_info - ensure module runs in check_mode (https://github.com/ansible-collections/community.aws/issues/659).

community.ciscosmb
~~~~~~~~~~~~~~~~~~

- Add Py 3.6 to supported python versions (https://github.com/ansible-collections/community.ciscosmb/pull/44)
- Added Releasing, CoC and Contributing to README.md
- Added author
- Added license header
- Fix link to issue tracker in galaxy.yml (https://github.com/ansible-collections/community.ciscosmb/pull/42)
- Misc doc fixes for collection inclusion (https://github.com/ansible-collections/community.ciscosmb/pull/41)
- Python 2.6, 2.7, 3.5 compatibility
- Release policy, versioning, deprecation
- Updated CoC, added email address
- add Code of conduct
- add Contribution
- add required files for community inclusion
- added ansible dev-guide manual test
- better tests requirements
- check tags and add tag switch
- cluter removed
- code cleaning
- correct version bumping
- doc update
- more descriptiove Release section on README.md
- remove mock warning
- remove unnecersary parameters on function re.sub()
- setup standard Ansible CI
- update my tests
- uptime in seconds

community.crypto
~~~~~~~~~~~~~~~~

- Avoid internal ansible-core module_utils in favor of equivalent public API available since at least Ansible 2.9 (https://github.com/ansible-collections/community.crypto/pull/253).
- cryptography_openssh module utils - new module_utils for managing asymmetric keypairs and OpenSSH formatted/encoded asymmetric keypairs (https://github.com/ansible-collections/community.crypto/pull/213).
- get_certificate - added ``starttls`` option to retrieve certificates from servers which require clients to request an encrypted connection (https://github.com/ansible-collections/community.crypto/pull/264).
- openssh certificate module utils - new module_utils for parsing OpenSSH certificates (https://github.com/ansible-collections/community.crypto/pull/246).
- openssh_cert - added ``regenerate`` option to validate additional certificate parameters which trigger regeneration of an existing certificate (https://github.com/ansible-collections/community.crypto/pull/256).
- openssh_cert - adding ``diff`` support (https://github.com/ansible-collections/community.crypto/pull/255).
- openssh_keypair - added ``backend`` parameter for selecting between the cryptography library or the OpenSSH binary for the execution of actions performed by ``openssh_keypair`` (https://github.com/ansible-collections/community.crypto/pull/236).
- openssh_keypair - added ``diff`` support (https://github.com/ansible-collections/community.crypto/pull/260).
- openssh_keypair - added ``passphrase`` parameter for encrypting/decrypting OpenSSH private keys (https://github.com/ansible-collections/community.crypto/pull/225).
- openssl_csr - add diff mode (https://github.com/ansible-collections/community.crypto/issues/38, https://github.com/ansible-collections/community.crypto/pull/150).
- openssl_csr_info - now returns ``public_key_type`` and ``public_key_data`` (https://github.com/ansible-collections/community.crypto/pull/233).
- openssl_csr_info - refactor module to allow code re-use for diff mode (https://github.com/ansible-collections/community.crypto/pull/204).
- openssl_csr_pipe - add diff mode (https://github.com/ansible-collections/community.crypto/issues/38, https://github.com/ansible-collections/community.crypto/pull/150).
- openssl_pkcs12 - added option ``select_crypto_backend`` and a ``cryptography`` backend. This requires cryptography 3.0 or newer, and does not support the ``iter_size`` and ``maciter_size`` options (https://github.com/ansible-collections/community.crypto/pull/234).
- openssl_privatekey - add diff mode (https://github.com/ansible-collections/community.crypto/issues/38, https://github.com/ansible-collections/community.crypto/pull/150).
- openssl_privatekey_info - refactor module to allow code re-use for diff mode (https://github.com/ansible-collections/community.crypto/pull/205).
- openssl_privatekey_pipe - add diff mode (https://github.com/ansible-collections/community.crypto/issues/38, https://github.com/ansible-collections/community.crypto/pull/150).
- openssl_publickey - add diff mode (https://github.com/ansible-collections/community.crypto/issues/38, https://github.com/ansible-collections/community.crypto/pull/150).
- x509_certificate - add diff mode (https://github.com/ansible-collections/community.crypto/issues/38, https://github.com/ansible-collections/community.crypto/pull/150).
- x509_certificate_info - now returns ``public_key_type`` and ``public_key_data`` (https://github.com/ansible-collections/community.crypto/pull/233).
- x509_certificate_info - refactor module to allow code re-use for diff mode (https://github.com/ansible-collections/community.crypto/pull/206).
- x509_certificate_pipe - add diff mode (https://github.com/ansible-collections/community.crypto/issues/38, https://github.com/ansible-collections/community.crypto/pull/150).
- x509_crl - add diff mode (https://github.com/ansible-collections/community.crypto/issues/38, https://github.com/ansible-collections/community.crypto/pull/150).
- x509_crl_info - add ``list_revoked_certificates`` option to avoid enumerating all revoked certificates (https://github.com/ansible-collections/community.crypto/pull/232).
- x509_crl_info - refactor module to allow code re-use for diff mode (https://github.com/ansible-collections/community.crypto/pull/203).

community.digitalocean
~~~~~~~~~~~~~~~~~~~~~~

- digital_ocean - ``ssh_key_ids`` list entries are now validated to be strings (https://github.com/ansible-collections/community.digitalocean/issues/13).
- digital_ocean - running and enforcing psf/black in the codebase (https://github.com/ansible-collections/community.digitalocean/issues/136).
- digital_ocean_database - add support for MongoDB (https://github.com/ansible-collections/community.digitalocean/issues/124).
- digital_ocean_droplet - ``ssh_keys``, ``tags``, and ``volumes`` list entries are now validated to be strings (https://github.com/ansible-collections/community.digitalocean/issues/13).
- digital_ocean_droplet - adding ``active`` and ``inactive`` states (https://github.com/ansible-collections/community.digitalocean/issues/23).
- digital_ocean_droplet - adds Droplet resize functionality (https://github.com/ansible-collections/community.digitalocean/issues/4).
- digital_ocean_floating_ip_info - new integration test for the `digital_ocean_floating_ip_info` module (https://github.com/ansible-collections/community.digitalocean/issues/130).
- digital_ocean_kubernetes - adding the C(taints), C(auto_scale), C(min_nodes) and C(max_nodes) parameters to the C(node_pools) definition (https://github.com/ansible-collections/community.digitalocean/issues/157).
- digital_ocean_kubernetes - set "latest" as the default version for new clusters (https://github.com/ansible-collections/community.digitalocean/issues/114).
- digitalocean - Filter droplets in dynamic inventory plugin using arbitrary. jinja2 expressions (https://github.com/ansible-collections/community.digitalocean/pull/96).
- digitalocean - Support templates in API tokens when using the dynamic inventory plugin (https://github.com/ansible-collections/community.digitalocean/pull/98).

community.dns
~~~~~~~~~~~~~

- Add support for Hetzner DNS (https://github.com/ansible-collections/community.dns/pull/27).
- Added a ``txt_transformation`` option to all modules and plugins working with DNS records (https://github.com/ansible-collections/community.dns/issues/48, https://github.com/ansible-collections/community.dns/pull/57, https://github.com/ansible-collections/community.dns/pull/60).
- Avoid internal ansible-core module_utils in favor of equivalent public API available since at least Ansible 2.9 (https://github.com/ansible-collections/community.dns/pull/24).
- The hosttech_dns_records module has been renamed to hosttech_dns_record_sets (https://github.com/ansible-collections/community.dns/pull/31).
- The internal API now supports bulk DNS record changes, if supported by the API (https://github.com/ansible-collections/community.dns/pull/39).
- The internal record API allows to manage extra data (https://github.com/ansible-collections/community.dns/pull/63).
- Use HTTP helper class to make API implementations work for both plugins and modules. Make WSDL API use ``fetch_url`` instead of ``open_url`` for modules (https://github.com/ansible-collections/community.dns/pull/36).
- hetzner_dns_record and hosttech_dns_record - when not using check mode, use actual return data for diff, instead of input data, so that extra data can be shown (https://github.com/ansible-collections/community.dns/pull/63).
- hetzner_dns_zone_info - the ``legacy_ns`` return value is now sorted, since its order is unstable (https://github.com/ansible-collections/community.dns/pull/46).
- hosttech modules - add ``api_token`` alias for ``hosttech_token`` (https://github.com/ansible-collections/community.dns/pull/26).
- hosttech_dns_* - handle ``419 Too Many Requests`` with proper rate limiting for JSON API (https://github.com/ansible-collections/community.dns/pull/14).
- hosttech_dns_* modules - rename ``zone`` parameter to ``zone_name``. The old name ``zone`` can still be used as an alias (https://github.com/ansible-collections/community.dns/pull/32).
- hosttech_dns_record - in ``diff`` mode, also return ``diff`` data structure when ``changed`` is ``false`` (https://github.com/ansible-collections/community.dns/pull/28).
- hosttech_dns_record* modules - allow to specify ``prefix`` instead of ``record`` (https://github.com/ansible-collections/community.dns/pull/8).
- hosttech_dns_record* modules - allow to specify zone by ID with the ``zone_id`` parameter, alternatively to the ``zone`` parameter (https://github.com/ansible-collections/community.dns/pull/7).
- hosttech_dns_record* modules - return ``zone_id`` on success (https://github.com/ansible-collections/community.dns/pull/7).
- hosttech_dns_record* modules - support IDN domain names and prefixes (https://github.com/ansible-collections/community.dns/pull/9).
- hosttech_dns_record_info - also return ``prefix`` for a record set (https://github.com/ansible-collections/community.dns/pull/8).
- hosttech_dns_record_set - ``value`` is no longer required when ``state=absent`` and ``overwrite=true`` (https://github.com/ansible-collections/community.dns/pull/31).
- hosttech_dns_record_sets - ``records`` has been renamed to ``record_sets``. The old name ``records`` can still be used as an alias (https://github.com/ansible-collections/community.dns/pull/31).
- hosttech_dns_zone_info - return extra information as ``zone_info`` (https://github.com/ansible-collections/community.dns/pull/38).
- hosttech_record - allow to delete records without querying their content first by specifying ``overwrite=true`` (https://github.com/ansible-collections/community.dns/pull/4).
- module utils - add default implementation for some zone/record API functions, and move common JSON API code to helper class (https://github.com/ansible-collections/community.dns/pull/26).

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
- chroot connection - minor refactor to make lints and IDEs happy (https://github.com/ansible-collections/community.general/pull/2520).
- cloud_init_data_facts - minor refactor (https://github.com/ansible-collections/community.general/pull/2557).
- cmd (Module Helper) module utils - ``CmdMixin`` now pulls the value for ``run_command()`` params from ``self.vars``, as opposed to previously retrieving those from ``self.module.params`` (https://github.com/ansible-collections/community.general/pull/2517).
- composer - add ``composer_executable`` option (https://github.com/ansible-collections/community.general/issues/2649).
- datadog_event - adding parameter ``api_host`` to allow selecting a datadog API endpoint instead of using the default one (https://github.com/ansible-collections/community.general/issues/2774, https://github.com/ansible-collections/community.general/pull/2775).
- datadog_monitor - allow creation of composite datadog monitors (https://github.com/ansible-collections/community.general/issues/2956).
- dig lookup plugin - add ``retry_servfail`` option (https://github.com/ansible-collections/community.general/pull/3247).
- dnsimple - module rewrite to include support for python-dnsimple>=2.0.0; also add ``sandbox`` parameter (https://github.com/ansible-collections/community.general/pull/2946).
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
- jail connection - minor refactor to make lints and IDEs happy (https://github.com/ansible-collections/community.general/pull/2520).
- java_keystore - added ``ssl_backend`` parameter for using the cryptography library instead of the OpenSSL binary (https://github.com/ansible-collections/community.general/pull/2485).
- java_keystore - replace envvar by stdin to pass secret to ``keytool`` (https://github.com/ansible-collections/community.general/pull/2526).
- jenkins_build - support stopping a running jenkins build (https://github.com/ansible-collections/community.general/pull/2850).
- jenkins_job_info - the ``password`` and ``token`` parameters can also be omitted to retrieve only public information (https://github.com/ansible-collections/community.general/pull/2948).
- jenkins_plugin - add fallback url(s) for failure of plugin installation/download (https://github.com/ansible-collections/community.general/pull/1334).
- jira - add comment visibility parameter for comment operation (https://github.com/ansible-collections/community.general/pull/2556).
- kernel_blacklist - revamped the module using ``ModuleHelper`` (https://github.com/ansible-collections/community.general/pull/3329).
- keycloak_authentication - enhanced diff mode to also return before and after state when the authentication flow is updated (https://github.com/ansible-collections/community.general/pull/2963).
- keycloak_client - add ``authentication_flow_binding_overrides`` option (https://github.com/ansible-collections/community.general/pull/2949).
- keycloak_realm - add ``events_enabled`` parameter to allow activation or deactivation of login events (https://github.com/ansible-collections/community.general/pull/3231).
- linode - added proper traceback when failing due to exceptions (https://github.com/ansible-collections/community.general/pull/2410).
- linode - parameter ``additional_disks`` is now validated as a list of dictionaries (https://github.com/ansible-collections/community.general/pull/2410).
- linode inventory plugin - adds the ``ip_style`` configuration key. Set to ``api`` to get more detailed network details back from the remote Linode host (https://github.com/ansible-collections/community.general/pull/3203).
- lxc connection - minor refactor to make lints and IDEs happy (https://github.com/ansible-collections/community.general/pull/2520).
- lxd_container - add ``ignore_volatile_options`` option which allows to disable the behavior that the module ignores options starting with ``volatile.`` (https://github.com/ansible-collections/community.general/pull/3331).
- maven_artifact - added ``checksum_alg`` option to support SHA1 checksums in order to support FIPS systems (https://github.com/ansible-collections/community.general/pull/2662).
- module_helper cmd module utils - added the ``ArgFormat`` style ``BOOLEAN_NOT``, to add CLI parameters when the module argument is false-ish (https://github.com/ansible-collections/community.general/pull/3290).
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
- nrdp callback plugin - parameters are now converted to strings, except ``validate_certs`` which is converted to boolean (https://github.com/ansible-collections/community.general/pull/2878).
- onepassword lookup plugin - add ``domain`` option (https://github.com/ansible-collections/community.general/issues/2734).
- open_iscsi - add ``auto_portal_startup`` parameter to allow ``node.startup`` setting per portal (https://github.com/ansible-collections/community.general/issues/2685).
- open_iscsi - also consider ``portal`` and ``port`` to check if already logged in or not (https://github.com/ansible-collections/community.general/issues/2683).
- open_iscsi - minor refactoring (https://github.com/ansible-collections/community.general/pull/3286).
- openwrt_init - minor refactoring (https://github.com/ansible-collections/community.general/pull/3284).
- pacman - add ``executable`` option to use an alternative pacman binary (https://github.com/ansible-collections/community.general/issues/2524).
- pamd - minor refactorings (https://github.com/ansible-collections/community.general/pull/3285).
- passwordstore lookup - add option ``missing`` to choose what to do if the password file is missing (https://github.com/ansible-collections/community.general/pull/2500).
- pids - refactor to add support for older ``psutil`` versions to the ``pattern`` option (https://github.com/ansible-collections/community.general/pull/3315).
- pkgin - in case of ``pkgin`` tool failue, display returned standard output ``stdout`` and standard error ``stderr`` to ease debugging (https://github.com/ansible-collections/community.general/issues/3146).
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
- stacki_host - minor refactoring (https://github.com/ansible-collections/community.general/pull/2681).
- supervisorctl - using standard Ansible mechanism to validate ``signalled`` state required parameter (https://github.com/ansible-collections/community.general/pull/3068).
- terraform - add ``check_destroy`` optional parameter to check for deletion of resources before it is applied (https://github.com/ansible-collections/community.general/pull/2874).
- terraform - add option ``overwrite_init`` to skip init if exists (https://github.com/ansible-collections/community.general/pull/2573).
- terraform - minor refactor (https://github.com/ansible-collections/community.general/pull/2557).
- timezone - print error message to debug instead of warning when timedatectl fails (https://github.com/ansible-collections/community.general/issues/1942).
- tss lookup plugin - added ``token`` parameter for token authorization; ``username`` and ``password`` are optional when ``token`` is provided (https://github.com/ansible-collections/community.general/pull/3327).
- tss lookup plugin - added new parameter for domain authorization (https://github.com/ansible-collections/community.general/pull/3228).
- tss lookup plugin - refactored to decouple the supporting third-party library (``python-tss-sdk``) (https://github.com/ansible-collections/community.general/pull/3252).
- vdo - minor refactoring of the code (https://github.com/ansible-collections/community.general/pull/3191).
- zfs - added diff mode support (https://github.com/ansible-collections/community.general/pull/502).
- zfs_delegate_admin - drop choices from permissions, allowing any permission supported by the underlying zfs commands (https://github.com/ansible-collections/community.general/pull/2540).
- zone connection - minor refactor to make lints and IDEs happy (https://github.com/ansible-collections/community.general/pull/2520).
- zpool_facts - minor refactoring (https://github.com/ansible-collections/community.general/pull/3332).
- zypper - prefix zypper commands with ``/sbin/transactional-update --continue --drop-if-no-change --quiet run`` if transactional updates are detected (https://github.com/ansible-collections/community.general/issues/3159).

community.hashi_vault
~~~~~~~~~~~~~~~~~~~~~

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
- increase kubernetes.core dependency version (https://github.com/openshift/community.okd/pull/97).
- openshift - inventory plugin supports FQCN ``redhat.openshift``.

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
- api - rename option ``ssl`` to ``tls``, and keep the old name as an alias (https://github.com/ansible-collections/community.routeros/pull/37).
- fact - add fact ``ansible_net_config_nonverbose`` to get idempotent config (no date, no verbose) (https://github.com/ansible-collections/community.routeros/pull/23).

community.sops
~~~~~~~~~~~~~~

- Avoid internal ansible-core module_utils in favor of equivalent public API available since at least Ansible 2.9 (https://github.com/ansible-collections/community.sops/pull/73).

community.vmware
~~~~~~~~~~~~~~~~

- vm_device_helper - Add new functions for create, remove or reconfigure virutal NVDIMM device (https://github.com/ansible-collections/community.vmware/issues/853).
- vmware - add processing to answer if the answer question is occurred in starting the vm (https://github.com/ansible-collections/community.vmware/pull/821).
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
- win_scheduled_task - Added support for setting a ``session_state_change`` trigger by documenting the human friendly values for ``state_change``
- win_scheduled_task_state - Added ``state_change_str`` to the trigger output to give a human readable description of the value

community.zabbix
~~~~~~~~~~~~~~~~

- all roles were updated to support Zabbix 5.4 release (https://github.com/ansible-collections/community.zabbix/pull/405)
- new inventory plugin zabbix_inventory (https://github.com/ansible-collections/community.zabbix/pull/373)
- new module plugin zabbix_globalmacro (https://github.com/ansible-collections/community.zabbix/pull/377)
- zabbix_agent - `zabbix_agent_src_reinstall` now defaults to `False` (https://github.com/ansible-collections/community.zabbix/pull/403)
- zabbix_agent - now supports setting AllowKey (https://github.com/ansible-collections/community.zabbix/pull/358)
- zabbix_globalmacros - it is now possible to create global macros using this module (https://github.com/ansible-collections/community.zabbix/pull/377).
- zabbix_inventory - Created Ansible - Zabbix inventory plugin to create dynamic inventory from Zabbix.
- zabbix_maintenance - it is now possible to target hosts by their technical name if it differs from the visible name
- zabbix_proxy - Add MySQL Python 3 package installation.
- zabbix_server - Add MySQL Python 3 package installation.
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
- Add new choices to request/response chunking parameter to accomodate TMOS v15 and above
- Add persistence target for disable action to bigip_policy_rule module
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

- all modules - ability to trace API calls and responses.

netapp.azure
~~~~~~~~~~~~

- azure_rm_netapp_account - support additional authentication schemes provided by AzureRMModuleBase.
- azure_rm_netapp_capacity_pool - support additional authentication schemes provided by AzureRMModuleBase, and tags.
- azure_rm_netapp_capacity_pool - wait for completion when creating, modifying, or deleting a pool.
- azure_rm_netapp_snapshot - support additional authentication schemes provided by AzureRMModuleBase.
- azure_rm_netapp_snapshot - wait for completion when creating, modifying, or deleting a pool.
- azure_rm_netapp_volume - new option ``feature_flags`` to selectively enable/disable a feature.
- azure_rm_netapp_volume - support additional authentication schemes provided by AzureRMModuleBase, and tags.

netapp.cloudmanager
~~~~~~~~~~~~~~~~~~~

- Only these parameters will be modified on the existing CVOs. svm_passowrd will be updated on each run.
- na_cloudmanager - Support pd-balanced in ``gcp_volume_type`` for CVO GCP, ``provider_volume_type`` in na_cloudmanager_snapmirror and na_cloudmanager_volume.
- na_cloudmanager - Support service account with new options ``sa_client_id`` and ``sa_secret_key`` to use for API operations.
- na_cloudmanager_aggregate - Add provider_volume_type gp3 support.
- na_cloudmanager_connector_azure - Change default value of ``virtual_machine_size`` to Standard_DS3_v2.
- na_cloudmanager_connector_gcp - rename option ``service_account_email`` and ``service_account_path`` to ``gcp_service_account_email`` and ``gcp_service_account_path`` respectively.
- na_cloudmanager_cvo_aws - Add ebs_volume_type gp3 support.
- na_cloudmanager_cvo_aws - Support update on svm_password, tier_level, and aws_tag.
- na_cloudmanager_cvo_aws - add new parameter ``kms_key_id`` and ``kms_key_arn`` as AWS encryption parameters to support AWS CVO encryption
- na_cloudmanager_cvo_azure - Add new parameter ``ha_enable_https`` for HA CVO to enable the HTTPS connection from CVO to storage accounts. This can impact write performance. The default is false.
- na_cloudmanager_cvo_azure - Support update on svm_password, tier_level, and azure_tag.
- na_cloudmanager_cvo_azure - add new parameter ``azure_encryption_parameters`` to support AZURE CVO encryption
- na_cloudmanager_cvo_gcp - Add selflink support on subnet_id, vpc0_node_and_data_connectivity, vpc1_cluster_connectivity, vpc2_ha_connectivity, vpc3_data_replication, subnet0_node_and_data_connectivity, subnet1_cluster_connectivity, subnet2_ha_connectivity, and subnet3_data_replication.
- na_cloudmanager_cvo_gcp - Support update on svm_password, tier_level, and gcp_labels.
- na_cloudmanager_cvo_gcp - add new parameter ``gcp_encryption_parameters`` to support GCP CVO encryption
- na_cloudmanager_snapmirror - Add provider_volume_type gp3 support.
- na_cloudmanager_volume - Add aggregate_name support on volume creation.
- na_cloudmanager_volume - Add provider_volume_type gp3 support.

netapp.ontap
~~~~~~~~~~~~

- License displayed correctly in Github
- na_ontap_cifs - new option ``comment`` to associate a description to a CIFS share.
- na_ontap_cifs_server - ``force`` option is supported when state is absent to ignore communication errors.
- na_ontap_cluster_peer - new option ``peer_options`` to use different credentials on peer.
- na_ontap_debug - additional checks when REST is available to help debug vserver connectivity issues.
- na_ontap_disks - added REST support for the module.
- na_ontap_disks - added functionality to reassign spare disks from a partner node to the desired node.
- na_ontap_disks - new option min_spares.
- na_ontap_flexcache - corrected module name in documentation Examples
- na_ontap_interface - new option ``from_name`` to rename an interface.
- na_ontap_job_schedule - new option ``month_offset`` to explictly select 0 or 1 for January.
- na_ontap_lun - new suboption ``exclude_aggregates`` for SAN application.
- na_ontap_net_port - change option types to bool and int respectively for ``autonegotiate_admin`` and ``mtu``.
- na_ontap_net_port - new option ``up_admin`` to set administrative state.
- na_ontap_ntp - Added REST support to the ntp module
- na_ontap_object_store - new option ``port``, ``certificate_validation_enabled``, ``ssl_enabled`` for target server.
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
- na_ontap_svm - new option ``services`` to allow and/or enable protocol services.
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
- Add private_key option to nb_lookup for secret decryption [#532](https://github.com/netbox-community/ansible_modules/pull/532)
- Added custom certificate support [#534](https://github.com/netbox-community/ansible_modules/pull/534)
- CI testing & integration tests now leverage ansible-core 2.11 - Fixes #583: Move to Ansible-core for CI tests  [#591](https://github.com/netbox-community/ansible_modules/pull/591)
- Correct Invalid NetBox readthedocs URL in nb_inventory docs [#568](https://github.com/netbox-community/ansible_modules/pull/568)
- Fixes to CI due to not pinning NetBox & NetBox-Docker version CI among other minor CI corrections - General CI Fix [573](https://github.com/netbox-community/ansible_modules/pull/573)
- README: Slack link and tidyup [#584](https://github.com/netbox-community/ansible_modules/pull/584)
- Release v3.1.2 [#594](https://github.com/netbox-community/ansible_modules/pull/594)
- Update netbox_region documentation - Documentation: netbox_region - Correct examples [#548](https://github.com/netbox-community/ansible_modules/pull/548)
- netbox_device_interface - Add custom_fields [#514](https://github.com/netbox-community/ansible_modules/pull/514)
- netbox_device_interface - Add label option.
- netbox_device_interface - Add mark_connected option.
- netbox_power_panel - Add location option.
- netbox_rack - Add location option.
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

- purefb_groupquota - New module for manage individual filesystem group quotas
- purefb_lag - Add support for LAG management
- purefb_snap - Add support for immeadiate snapshot to remote connected FlashBlade
- purefb_subnet - Add support for multiple LAGs.
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

t_systems_mms.icinga_director
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Add event_command parameter to icinga_service_apply module (https://github.com/T-Systems-MMS/ansible-collection-icinga-director/pull/132)
- Add event_command parameter to service apply playbook to enable usage (https://github.com/T-Systems-MMS/ansible-collection-icinga-director/pull/133)
- Add some more documentation on command template (https://github.com/T-Systems-MMS/ansible-collection-icinga-director/pull/128)
- Add support for retry_interval and max_check_attempts to host template (https://github.com/T-Systems-MMS/ansible-collection-icinga-director/pull/140)
- add "vars" variable to icinga_notification in the role (https://github.com/T-Systems-MMS/ansible-collection-icinga-director/pull/129)
- add notification_template to role (https://github.com/T-Systems-MMS/ansible-collection-icinga-director/pull/125)

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

community.dns
~~~~~~~~~~~~~

- All Hetzner modules and plugins which handle DNS records now work with unquoted TXT values by default. The old behavior can be obtained by setting ``txt_transformation=api`` (https://github.com/ansible-collections/community.dns/issues/48, https://github.com/ansible-collections/community.dns/pull/57, https://github.com/ansible-collections/community.dns/pull/60).
- Hosttech API creation - now requires a ``ModuleOptionProvider`` object instead of an ``AnsibleModule`` object. Alternatively an Ansible plugin instance can be passed (https://github.com/ansible-collections/community.dns/pull/37).
- The hetzner_dns_record_info and hosttech_dns_record_info modules have been renamed to hetzner_dns_record_set_info and hosttech_dns_record_set_info, respectively (https://github.com/ansible-collections/community.dns/pull/54).
- The hosttech_dns_record module has been renamed to hosttech_dns_record_set (https://github.com/ansible-collections/community.dns/pull/31).
- The internal bulk record updating helper (``bulk_apply_changes``) now also returns the records that were deleted, created or updated (https://github.com/ansible-collections/community.dns/pull/63).
- The internal record API no longer allows to manage comments explicitly (https://github.com/ansible-collections/community.dns/pull/63).
- When using the internal modules API, now a zone ID type and a provider information object must be passed (https://github.com/ansible-collections/community.dns/pull/27).
- hetzner_dns_record* modules - implement correct handling of default TTL. The value ``none`` is now accepted and returned in this case (https://github.com/ansible-collections/community.dns/pull/52, https://github.com/ansible-collections/community.dns/issues/50).
- hetzner_dns_record, hetzner_dns_record_set, hetzner_dns_record_sets - the default TTL is now 300 and no longer 3600, which equals the default in the web console (https://github.com/ansible-collections/community.dns/pull/43).
- hosttech_* module_utils - completely rewrite and refactor to support new JSON API and allow to re-use provider-independent module logic (https://github.com/ansible-collections/community.dns/pull/4).
- hosttech_dns_record_set - the option ``overwrite`` was replaced by a new option ``on_existing``. Specifying ``overwrite=true`` is equivalent to ``on_existing=replace`` (the new default). Specifying ``overwrite=false`` with ``state=present`` is equivalent to ``on_existing=keep_and_fail``, and specifying ``overwrite=false`` with ``state=absent`` is equivalent to ``on_existing=keep`` (https://github.com/ansible-collections/community.dns/pull/31).

community.okd
~~~~~~~~~~~~~

- drop python 2 support (https://github.com/openshift/community.okd/pull/93).

community.routeros
~~~~~~~~~~~~~~~~~~

- api - due to a programming error, the module never failed on errors. This has now been fixed. If you are relying on the module not failing in case of idempotent commands (resulting in errors like ``failure: already have such address``), you need to adjust your roles/playbooks. We suggest to use ``failed_when`` to accept failure in specific circumstances, for example ``failed_when: "'failure: already have ' in result.msg[0]"`` (https://github.com/ansible-collections/community.routeros/pull/39).

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

- ec2_elb - the ``ec2_elb`` module has been removed and redirected to the ``elb_instance`` module which functions identically. The original ``ec2_elb`` name is now deprecated and will be removed in release 3.0.0 (https://github.com/ansible-collections/community.aws/pull/586).
- ec2_elb_info - the boto based ``ec2_elb_info`` module has been deprecated in favour of the boto3 based ``elb_classic_lb_info`` module. The ``ec2_elb_info`` module will be removed in release 3.0.0 (https://github.com/ansible-collections/community.aws/pull/586).
- elb_classic_lb - the ``elb_classic_lb`` module has been removed and redirected to the ``amazon.aws.ec2_elb_lb`` module which functions identically.
- iam - the boto based ``iam`` module has been deprecated in favour of the boto3 based ``iam_user``, ``iam_group`` and ``iam_role`` modules. The ``iam`` module will be removed in release 3.0.0 (https://github.com/ansible-collections/community.aws/pull/664).
- rds - the boto based ``rds`` module has been deprecated in favour of the boto3 based ``rds_instance`` module. The ``rds`` module will be removed in release 3.0.0 (https://github.com/ansible-collections/community.aws/pull/663).
- script_inventory_ec2 - The ec2.py inventory script is being moved to a new repository. The script can now be downloaded from https://github.com/ansible-community/contrib-scripts/blob/main/inventory/ec2.py and will be removed from this collection in the 3.0 release. We recommend migrating from the script to the `amazon.aws.ec2` inventory plugin.

community.dns
~~~~~~~~~~~~~

- The hosttech_dns_records module has been renamed to hosttech_dns_record_sets. The old name will stop working in community.dns 3.0.0 (https://github.com/ansible-collections/community.dns/pull/31).

community.docker
~~~~~~~~~~~~~~~~

- docker_* modules and plugins, except ``docker_swarm`` connection plugin and ``docker_compose`` and ``docker_stack*` modules - the current default ``localhost`` for ``tls_hostname`` is deprecated. In community.docker 2.0.0 it will be computed from ``docker_host`` instead (https://github.com/ansible-collections/community.docker/pull/134).
- docker_container - the new ``command_handling``'s default value, ``compatibility``, is deprecated and will change to ``correct`` in community.docker 3.0.0. A deprecation warning is emitted by the module in cases where the behavior will change. Please note that ansible-core will output a deprecation warning only once, so if it is shown for an earlier task, there could be more tasks with this warning where it is not shown (https://github.com/ansible-collections/community.docker/pull/186).

community.general
~~~~~~~~~~~~~~~~~

- All inventory and vault scripts will be removed from community.general in version 4.0.0. If you are referencing them, please update your references to the new `contrib-scripts GitHub repository <https://github.com/ansible-community/contrib-scripts>`_ so your workflow will not break once community.general 4.0.0 is released (https://github.com/ansible-collections/community.general/pull/2697).
- The nios, nios_next_ip, nios_next_network lookup plugins, the nios documentation fragment, and the nios_host_record, nios_ptr_record, nios_mx_record, nios_fixed_address, nios_zone, nios_member, nios_a_record, nios_aaaa_record, nios_network, nios_dns_view, nios_txt_record, nios_naptr_record, nios_srv_record, nios_cname_record, nios_nsgroup, and nios_network_view module have been deprecated and will be removed from community.general 5.0.0. Please install the `infoblox.nios_modules <https://galaxy.ansible.com/infoblox/nios_modules>`_ collection instead and use its plugins and modules (https://github.com/ansible-collections/community.general/pull/2458).
- The vendored copy of ``ipaddress`` will be removed in community.general 4.0.0. Please switch to ``ipaddress`` from the Python 3 standard library, or `from pypi <https://pypi.org/project/ipaddress/>`_, if your code relies on the vendored version of ``ipaddress`` (https://github.com/ansible-collections/community.general/pull/2459).
- ali_instance_info - marked removal version of deprecated parameters ``availability_zone`` and ``instance_names`` (https://github.com/ansible-collections/community.general/issues/2429).
- linode - parameter ``backupsenabled`` is deprecated and will be removed in community.general 5.0.0 (https://github.com/ansible-collections/community.general/pull/2410).
- lxd inventory plugin - the plugin will require ``ipaddress`` installed when used with Python 2 from community.general 4.0.0 on. ``ipaddress`` is part of the Python 3 standard library, but can be installed for Python 2 from pypi (https://github.com/ansible-collections/community.general/pull/2459).
- scaleway_security_group_rule - the module will require ``ipaddress`` installed when used with Python 2 from community.general 4.0.0 on. ``ipaddress`` is part of the Python 3 standard library, but can be installed for Python 2 from pypi (https://github.com/ansible-collections/community.general/pull/2459).
- serverless - deprecating parameter ``functions`` because it was not used in the code (https://github.com/ansible-collections/community.general/pull/2845).

community.grafana
~~~~~~~~~~~~~~~~~

- grafana_dashboard lookup - Providing a mangled version of the API key is no longer preferred.

community.hashi_vault
~~~~~~~~~~~~~~~~~~~~~

- hashi_vault collection - support for Python 2 will be dropped in version ``2.0.0`` of ``community.hashi_vault`` (https://github.com/ansible-collections/community.hashi_vault/issues/81).
- hashi_vault collection - support for Python 3.5 will be dropped in version ``2.0.0`` of ``community.hashi_vault`` (https://github.com/ansible-collections/community.hashi_vault/issues/81).

community.kubernetes
~~~~~~~~~~~~~~~~~~~~

- The ``community.kubernetes`` collection is being renamed to ``kubernetes.core``. All content in the collection has been replaced by deprecated redirects to ``kubernetes.core``. If you are using FQCNs starting with ``community.kubernetes``, please update them to ``kubernetes.core`` (https://github.com/ansible-collections/community.kubernetes/pull/439).

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

Security Fixes
--------------

Ansible-core
~~~~~~~~~~~~

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
- ansible-test - Fix traceback when generating coverage reports and no coverage directory exists.
- ansible-test - Random port selection is no longer handled by ``ansible-test``, avoiding possible port conflicts. Previously ``ansible-test`` would, under some circumstances, use one host's available ports to determine those of another host.
- ansible-test - Running tests in a single test run with multiple "cloud" plugins no longer results in port conflicts. Previously two or more containers with overlapping ports could not be used in the same test run.
- ansible-test - Tab completion after options like ``--docker`` which accept an optional argument will no longer provide incorrect completions.
- ansible-test - The ``--python`` and ``--venv`` options are no longer ignored by some commands, such as ``coverage``.
- ansible-test - The ``docker inspect`` command is now used to check for existing images instead of the ``docker images`` command. This resolves an issue where a ``docker pull`` would be unnecessarily executed for an image referenced by checksum.
- ansible-test - Use ``--strict`` for ``pytest`` on Python 2.6 since ``--strict-markers`` is not available.
- ansible-test - Use documented API to retrieve build information from Azure Pipelines.
- ansible-test - Use pwsh to generate correct coverage line counts for stub files to get a more accurate coverage result
- ansible-test - add packaging python module to ``ansible-doc`` sanity test requirements.
- ansible-test - allow the same listening port on all container interfaces
- ansible-test - ensure the correct unit test target is given when the ``__init__.py`` file is modified inside the connection plugins directory
- ansible-test - make the ``a/`` and ``b/`` prefixes an optional match since these can be turned off with the ``diff.noprefix`` setting in ``git``
- ansible-test - restrict ``packaging`` to ``< 21.0`` for Python ``< 3.6`` (https://github.com/ansible/ansible/pull/75186).
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

- aws_s3 - Fix upload permission when an S3 bucket ACL policy requires a particular canned ACL (https://github.com/ansible-collections/amazon.aws/pull/318)
- ec2_ami - Fix ami issue when creating an ami with no_device parameter (https://github.com/ansible-collections/amazon.aws/pull/386)
- ec2_instance - ``ec2_instance`` was waiting on EC2 instance monitoring status to be ``OK`` when launching a new instance. This could cause a play to wait multiple minutes for AWS's monitoring to complete status checks (https://github.com/ansible-collections/amazon.aws/pull/481).
- ec2_snapshot - Fix snapshot issue when capturing a snapshot of a volume without tags (https://github.com/ansible-collections/amazon.aws/pull/383)
- ec2_vol - Fixes ``changed`` status when ``modify_volume`` is used, but no new  disk is being attached.  The module incorrectly reported that no change had  occurred even when disks had been modified (iops, throughput, type, etc.). (https://github.com/ansible-collections/amazon.aws/issues/482).
- ec2_vol - fix iops setting and enforce iops/throughput parameters usage (https://github.com/ansible-collections/amazon.aws/pull/334)
- inventory - ``include_filters`` won't be ignored anymore if ``filters`` is not set (https://github.com/ansible-collections/amazon.aws/issues/457).
- s3_bucket - Fix error handling when attempting to set a feature that is not implemented (https://github.com/ansible-collections/amazon.aws/pull/391).
- s3_bucket - Gracefully handle ``NotImplemented`` exceptions when fetching encryption settings (https://github.com/ansible-collections/amazon.aws/issues/390).

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
- win_dsc - Fix import errors when running against host that wasn't installed with the ``en-US`` locale - https://github.com/ansible-collections/ansible.windows/issues/83
- win_group - fixed ``description`` setting for a group that doesn't exist when running in check_mode (https://github.com/ansible-collections/ansible.windows/pull/260).
- win_reboot - Ensure documented return values are always returned even on a failure
- win_reboot - Fix local variable referenced before assignment issue - https://github.com/ansible-collections/ansible.windows/issues/276
- win_reboot - Handle connection failures when getting the first boot time command
- win_reboot - Handle more connection failures during the reboot phases
- win_reboot - User defined commands are run wrapped as a PowerShell command so they work on all shells - https://github.com/ansible-collections/ansible.windows/issues/36
- win_state - Fixed the ``creationtime``, ``lastaccesstime``, and ``lastwritetime`` to report the time in UTC. This matches the ``stat`` module's behaviour and what many would expect for a epoch based timestamp - https://github.com/ansible-collections/ansible.windows/issues/240
- win_updates - Always return the ``failed_updates_count`` on a standard failure - https://github.com/ansible-collections/ansible.windows/issues/13
- win_updates - Always use a scheduled task which should be less prone to random token errors when trying to connect to Windows Update - https://github.com/ansible-collections/ansible.windows/issues/193
- win_updates - Attempt a reboot once when ``reboot=True`` is set and a failure occurred - https://github.com/ansible-collections/ansible.windows/issues/22
- win_updates - Bypass execution policy checks when polling or cancelling the update task - https://github.com/ansible-collections/ansible.windows/issues/272
- win_updates - Fixed ``win_updates`` output to not cast to an integer to preserve original behaviour and issues with non integer values - https://github.com/ansible-collections/ansible.windows/issues/247
- win_updates - Improve the reboot detection behaviour when ``reboot=True`` is set - https://github.com/ansible-collections/ansible.windows/issues/25
- win_updates - Improve the reboot mechanism - https://github.com/ansible-collections/ansible.windows/issues/143
- win_updates - Reboot the host when ``reboot=True`` if the first search result indicates a reboot is required - https://github.com/ansible-collections/ansible.windows/issues/49
- win_updates - fallback to run as SYSTEM if current user does not have batch logon rights - https://github.com/ansible-collections/ansible.windows/issues/253
- win_user - Set validate user logic to always check local database

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

cisco.asa
~~~~~~~~~

- Fix TypeError argument of type 'NoneType' is not iterable in service-group when service-group does not exists.
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
- `nxos_facts` - Fix KeyError while gathering CDP neighbor facts (https://github.com/ansible-collections/cisco.nxos/issues/354).
- `nxos_facts` - Fix gathering CDP neighbor facts from certain N7Ks (https://github.com/ansible-collections/cisco.nxos/issues/329).
- `nxos_ospf_interfaces` - Correctly sort interface names before rendering.
- `nxos_vlans` - switching to `| json-pretty` instead of `| json` as a workaround for the timeout issue with `libssh` (https://github.com/ansible/pylibssh/issues/208)
- `nxos_zone_zoneset` - zone member addition with smart zoning in an already existing zone should be a no-op (https://github.com/ansible-collections/cisco.nxos/issues/339).

community.aws
~~~~~~~~~~~~~

- aws_secret - fix deletion idempotency when not using instant deletion (https://github.com/ansible-collections/community.aws/pull/681).
- aws_ssm - rename ``retries`` to ``reconnection_retries`` to avoid conflict with task retries
- ec2_vpc_peer - automatically retry when attempting to tag freshly created peering connections (https://github.com/ansible-collections/community.aws/pull/614).
- ec2_vpc_route_table - automatically retry when attempting to modify freshly created route tables (https://github.com/ansible-collections/community.aws/pull/616).
- ecs_taskdefinition - ensure cast to integer (https://github.com/ansible-collections/community.aws/pull/574).
- ecs_taskdefinition - fix idempotency (https://github.com/ansible-collections/community.aws/pull/574).
- ecs_taskdefinition - fix typo in ecs task defination for env file validations (https://github.com/ansible-collections/community.aws/pull/600).
- iam_role - Modified iam_role internal code to replace update_role_description with update_role (https://github.com/ansible-collections/community.aws/pull/697).
- route53 - fix typo in waiter configuration that prevented management of the delays (https://github.com/ansible-collections/community.aws/pull/564).
- s3_sync - fix handling individual file path to upload a individual file to s3 bucket (https://github.com/ansible-collections/community.aws/pull/692).
- sqs_queue - fix queue attribute comparison to make module idempotent (https://github.com/ansible-collections/community.aws/pull/592).

community.ciscosmb
~~~~~~~~~~~~~~~~~~

- Module command does not support check_mode - https://github.com/ansible-collections/community.ciscosmb/pull/45
- solves issue

community.crypto
~~~~~~~~~~~~~~~~

- acme_* modules - fix commands composed for OpenSSL backend to retrieve information on CSRs and certificates from stdin to use ``/dev/stdin`` instead of ``-``. This is needed for OpenSSL 1.0.1 and 1.0.2, apparently (https://github.com/ansible-collections/community.crypto/pull/279).
- acme_challenge_cert_helper - only return exception when cryptography is not installed, not when a too old version of it is installed. This prevents Ansible's callback to crash (https://github.com/ansible-collections/community.crypto/pull/281).
- keypair_backend module utils - simplify code to pass sanity tests (https://github.com/ansible-collections/community.crypto/pull/263).
- openssh_cert - fixed certificate generation to restore original certificate if an error is encountered (https://github.com/ansible-collections/community.crypto/pull/255).
- openssh_keypair - fix ``check_mode`` to populate return values for existing keypairs (https://github.com/ansible-collections/community.crypto/issues/113, https://github.com/ansible-collections/community.crypto/pull/230).
- openssh_keypair - fixed ``cryptography`` backend to preserve original file permissions when regenerating a keypair requires existing files to be overwritten (https://github.com/ansible-collections/community.crypto/pull/260).
- openssh_keypair - fixed a bug that prevented custom file attributes being applied to public keys (https://github.com/ansible-collections/community.crypto/pull/257).
- openssh_keypair - fixed error handling to restore original keypair if regeneration fails (https://github.com/ansible-collections/community.crypto/pull/260).
- openssl_csr and openssl_csr_pipe - make sure that Unicode strings are used to compare strings with the cryptography backend. This fixes idempotency problems with non-ASCII letters on Python 2 (https://github.com/ansible-collections/community.crypto/issues/270, https://github.com/ansible-collections/community.crypto/pull/271).
- openssl_pkcs12 - fix crash when loading passphrase-protected PKCS#12 files with ``cryptography`` backend (https://github.com/ansible-collections/community.crypto/issues/247, https://github.com/ansible-collections/community.crypto/pull/248).
- various modules - prevent crashes when modules try to set attributes on not yet existing files in check mode. This will be fixed in ansible-core 2.12, but it is not backported to every Ansible version we support (https://github.com/ansible-collections/community.crypto/issue/242, https://github.com/ansible-collections/community.crypto/pull/243).
- x509_certificate - fix crash when ``assertonly`` provider is used and some error conditions should be reported (https://github.com/ansible-collections/community.crypto/issues/240, https://github.com/ansible-collections/community.crypto/pull/241).
- x509_crl - restore inherited function signature to pass sanity tests (https://github.com/ansible-collections/community.crypto/pull/263).

community.digitalocean
~~~~~~~~~~~~~~~~~~~~~~

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
- digital_ocean_droplet - power on should poll/wait, resize should support "active" state (https://github.com/ansible-collections/community.digitalocean/pull/143).
- digital_ocean_droplet - state `present` with `wait` was not waiting (https://github.com/ansible-collections/community.digitalocean/issues/116).
- digital_ocean_droplet_info - Fix documentation link for `digital_ocean_droplet_info` (https://github.com/ansible-collections/community.digitalocean/pull/81).
- digital_ocean_firewall - fixed idempotence (https://github.com/ansible-collections/community.digitalocean/issues/122).
- digital_ocean_firewall - fixing integration test (https://github.com/ansible-collections/community.digitalocean/issues/114).
- digital_ocean_firewall_info - ensure return type is a list (https://github.com/ansible-collections/community.digitalocean/issues/55).
- digital_ocean_floating_ip - delete all Floating IPs initially during the integration test run (https://github.com/ansible-collections/community.digitalocean/issues/129).
- digital_ocean_floating_ip - fixes idempotence (https://github.com/ansible-collections/community.digitalocean/issues/5).
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
- digitalocean inventory - respect the TRANSFORM_INVALID_GROUP_CHARS configuration setting (https://github.com/ansible-collections/community.digitalocean/pull/138).
- digitalocean inventory plugin - Wire up advertised caching functionality (https://github.com/ansible-collections/community.digitalocean/pull/97).
- digitalocean inventory plugin - attributes available to filters are limited to explicitly required attributes and are prefixed with ``var_prefix`` (https://github.com/ansible-collections/community.digitalocean/pull/102).
- info modules - adding missing check mode support (https://github.com/ansible-collections/community.digitalocean/issues/139).

community.dns
~~~~~~~~~~~~~

- Avoid converting ASCII labels which contain underscores or other printable ASCII characters outside ``[a-zA-Z0-9-]`` to alabels during normalization (https://github.com/ansible-collections/community.dns/pull/13).
- Hetzner API - interpret missing TTL as 300, which is what the web console also does (https://github.com/ansible-collections/community.dns/pull/42).
- Update Public Suffix List.
- Updated Public Suffix List.
- hetzner API code - make sure to also handle errors returned by the API if the HTTP status code indicates success. This sometimes happens for 500 Internal Server Error (https://github.com/ansible-collections/community.dns/pull/58).
- hosttech_dns_record - correctly handle quoting in CAA records for JSON API (https://github.com/ansible-collections/community.dns/pull/30).
- hosttech_dns_zone_info - make sure that full information is returned both when requesting a zone by ID or by name (https://github.com/ansible-collections/community.dns/pull/56).
- hosttech_record - fix diff mode for ``state=absent`` (https://github.com/ansible-collections/community.dns/pull/4).
- hosttech_record_info - fix authentication error handling (https://github.com/ansible-collections/community.dns/pull/4).
- wait_for_txt - fix handling of too long TXT values (https://github.com/ansible-collections/community.dns/pull/65).
- wait_for_txt - resolving nameservers sometimes resulted in an empty list, yielding wrong results (https://github.com/ansible-collections/community.dns/pull/64).

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
- ali_instance_info - added support to check mode (https://github.com/ansible-collections/community.general/pull/3084).
- apache2_module - fix ``a2enmod``/``a2dismod`` detection, and error message when not found (https://github.com/ansible-collections/community.general/issues/3253).
- archive - fixed ``exclude_path`` values causing incorrect archive root (https://github.com/ansible-collections/community.general/pull/2816).
- archive - fixed improper file names for single file zip archives (https://github.com/ansible-collections/community.general/issues/2818).
- archive - fixed incorrect ``state`` result value documentation (https://github.com/ansible-collections/community.general/pull/2816).
- archive - fixed task failure when using the ``remove`` option with a ``path`` containing nested files for ``format``s other than ``zip`` (https://github.com/ansible-collections/community.general/issues/2919).
- archive - fixing archive root determination when longest common root is ``/`` (https://github.com/ansible-collections/community.general/pull/3036).
- consul_acl - update the hcl allowlist to include all supported options (https://github.com/ansible-collections/community.general/pull/2495).
- consul_kv lookup plugin - allow to set ``recurse``, ``index``, ``datacenter`` and ``token`` as keyword arguments (https://github.com/ansible-collections/community.general/issues/2124).
- copr - fix chroot naming issues, ``centos-stream`` changed naming to ``centos-stream-<number>`` (for exmaple ``centos-stream-8``) (https://github.com/ansible-collections/community.general/issues/2084, https://github.com/ansible-collections/community.general/pull/3237).
- cpanm - also use ``LC_ALL`` to enforce locale choice (https://github.com/ansible-collections/community.general/pull/2731).
- deploy_helper - improved parameter checking by using standard Ansible construct (https://github.com/ansible-collections/community.general/pull/3104).
- django_manage - argument ``command`` is being splitted again as it should (https://github.com/ansible-collections/community.general/issues/3215).
- django_manage - parameters ``apps`` and ``fixtures`` are now splitted instead of being used as a single argument (https://github.com/ansible-collections/community.general/issues/3333).
- django_manage - refactor to call ``run_command()`` passing command as a list instead of string (https://github.com/ansible-collections/community.general/pull/3098).
- ejabberd_user - replaced in-code check with ``required_if``, using ``get_bin_path()`` for the command, passing args to ``run_command()`` as list instead of string (https://github.com/ansible-collections/community.general/pull/3093).
- filesystem - repair ``reiserfs`` fstype support after adding it to integration tests (https://github.com/ansible-collections/community.general/pull/2472).
- gitlab_group_members - fixes issue when gitlab group has more then 20 members, pagination problem (https://github.com/ansible-collections/community.general/issues/3041).
- gitlab_project - user projects are created using namespace ID now, instead of user ID (https://github.com/ansible-collections/community.general/pull/2881).
- gitlab_project_members - fixes issue when gitlab group has more then 20 members, pagination problem (https://github.com/ansible-collections/community.general/issues/3041).
- idrac_redfish_info - added support to check mode (https://github.com/ansible-collections/community.general/pull/3084).
- influxdb_user - allow creation of admin users when InfluxDB authentication is enabled but no other user exists on the database. In this scenario, InfluxDB 1.x allows only ``CREATE USER`` queries and rejects any other query (https://github.com/ansible-collections/community.general/issues/2364).
- influxdb_user - fix bug where an influxdb user has no privileges for 2 or more databases (https://github.com/ansible-collections/community.general/pull/2499).
- influxdb_user - fix bug which removed current privileges instead of appending them to existing ones (https://github.com/ansible-collections/community.general/issues/2609, https://github.com/ansible-collections/community.general/pull/2614).
- ini_file - fix Unicode processing for Python 2 (https://github.com/ansible-collections/community.general/pull/2875).
- ini_file - fix inconsistency between empty value and no value (https://github.com/ansible-collections/community.general/issues/3031).
- interfaces_file - no longer reporting change when none happened (https://github.com/ansible-collections/community.general/pull/3328).
- ipa_sudorule - call ``sudorule_add_allow_command`` method instead of  ``sudorule_add_allow_command_group`` (https://github.com/ansible-collections/community.general/issues/2442).
- iptables_state - call ``async_status`` action plugin rather than its module (https://github.com/ansible-collections/community.general/issues/2700).
- iptables_state - fix a 'FutureWarning' in a regex and do some basic code clean up (https://github.com/ansible-collections/community.general/pull/2525).
- iptables_state - fix a broken query of ``async_status`` result with current ansible-core development version (https://github.com/ansible-collections/community.general/issues/2627, https://github.com/ansible-collections/community.general/pull/2671).
- iptables_state - fix initialization of iptables from null state when adressing more than one table (https://github.com/ansible-collections/community.general/issues/2523).
- java_cert - fix issue with incorrect alias used on PKCS#12 certificate import (https://github.com/ansible-collections/community.general/pull/2560).
- java_cert - import private key as well as public certificate from PKCS#12 (https://github.com/ansible-collections/community.general/issues/2460).
- java_keystore - add parameter ``keystore_type`` to control output file format and override ``keytool``'s default, which depends on Java version (https://github.com/ansible-collections/community.general/issues/2515).
- jenkins_build - examine presence of ``build_number`` before deleting a jenkins build (https://github.com/ansible-collections/community.general/pull/2850).
- jenkins_plugin - use POST method for sending request to jenkins API when ``state`` option is one of ``enabled``, ``disabled``, ``pinned``, ``unpinned``, or ``absent`` (https://github.com/ansible-collections/community.general/issues/2510).
- json_query filter plugin - avoid 'unknown type' errors for more Ansible internal types (https://github.com/ansible-collections/community.general/pull/2607).
- keycloak_authentication - fix bug when two identical executions are in the same authentication flow (https://github.com/ansible-collections/community.general/pull/2904).
- keycloak_realm - ``ssl_required`` changed from a boolean type to accept the strings ``none``, ``external`` or ``all``. This is not a breaking change since the module always failed when a boolean was supplied (https://github.com/ansible-collections/community.general/pull/2693).
- keycloak_realm - element type for ``events_listeners`` parameter should be ``string`` instead of ``dict`` (https://github.com/ansible-collections/community.general/pull/3231).
- keycloak_realm - remove warning that ``reset_password_allowed`` needs to be marked as ``no_log`` (https://github.com/ansible-collections/community.general/pull/2694).
- launchd - fixed sanity check in the module's code (https://github.com/ansible-collections/community.general/pull/2960).
- launchd - use private attribute to fix sanity errors (https://github.com/ansible-collections/community.general/pull/3194).
- linode inventory plugin - fix default value of new option ``ip_style`` (https://github.com/ansible-collections/community.general/issues/3337).
- logdns callback plugin - improve split call to fix sanity errors (https://github.com/ansible-collections/community.general/pull/3194).
- lvol - honor ``check_mode`` on thinpool (https://github.com/ansible-collections/community.general/issues/2934).
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
- nmcli - fixes team-slave configuration by adding connection.slave-type (https://github.com/ansible-collections/community.general/issues/766).
- npm - correctly handle cases where a dependency does not have a ``version`` property because it is either missing or invalid (https://github.com/ansible-collections/community.general/issues/2917).
- npm - when the ``version`` option is used the comparison of installed vs missing will use name@version instead of just name, allowing version specific updates (https://github.com/ansible-collections/community.general/issues/2021).
- one_template - change function argument name to fix sanity errors (https://github.com/ansible-collections/community.general/pull/3194).
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
- openwrt_init - calling ``run_command`` with arguments as ``list`` instead of ``str`` (https://github.com/ansible-collections/community.general/pull/3284).
- ovir4 inventory script - improve configparser creation to avoid crashes for options without values (https://github.com/ansible-collections/community.general/issues/674).
- packet_device - use generator to fix sanity errors (https://github.com/ansible-collections/community.general/pull/3194).
- packet_sshkey - use generator to fix sanity errors (https://github.com/ansible-collections/community.general/pull/3194).
- pacman - fix changed status when ignorepkg has been defined (https://github.com/ansible-collections/community.general/issues/1758).
- pamd - code for ``state=updated`` when dealing with the pam module arguments, made no distinction between ``None`` and an empty list (https://github.com/ansible-collections/community.general/issues/3260).
- pamd - fixed problem with files containing only one or two lines (https://github.com/ansible-collections/community.general/issues/2925).
- pids - avoid crashes for older ``psutil`` versions, like on RHEL6 and RHEL7 (https://github.com/ansible-collections/community.general/pull/2808).
- proxmox inventory plugin - fixed parsing failures when some cluster nodes are offline (https://github.com/ansible-collections/community.general/issues/2931).
- proxmox inventory plugin - fixed plugin failure when a ``qemu`` guest has no ``template`` key (https://github.com/ansible-collections/community.general/pull/3052).
- proxmox_kvm - clone operation should return the VMID of the target VM and not that of the source VM. This was failing when the target VM with the chosen name already existed (https://github.com/ansible-collections/community.general/pull/3266).
- proxmox_kvm - fix parsing of Proxmox VM information with device info not containing a comma, like disks backed by ZFS zvols (https://github.com/ansible-collections/community.general/issues/2840).
- proxmox_kvm - fix result of clone, now returns ``newid`` instead of ``vmid`` (https://github.com/ansible-collections/community.general/pull/3034).
- proxmox_kvm - fixed ``vmid`` return value when VM with ``name`` already exists (https://github.com/ansible-collections/community.general/issues/2648).
- rax_facts - added support to check mode (https://github.com/ansible-collections/community.general/pull/3084).
- redfish_command - fix extraneous error caused by missing ``bootdevice`` argument when using the ``DisableBootOverride`` sub-command (https://github.com/ansible-collections/community.general/issues/3005).
- redfish_info - added support to check mode (https://github.com/ansible-collections/community.general/pull/3084).
- redfish_utils module utils - if given, add account ID of user that should be created to HTTP request (https://github.com/ansible-collections/community.general/pull/3343/).
- redis cache - improved connection string parsing (https://github.com/ansible-collections/community.general/issues/497).
- rhsm_release - fix the issue that module considers 8, 7Client and 7Workstation as invalid releases (https://github.com/ansible-collections/community.general/pull/2571).
- saltstack connection plugin - fix function signature (https://github.com/ansible-collections/community.general/pull/3194).
- scaleway inventory script - improve split call to fix sanity errors (https://github.com/ansible-collections/community.general/pull/3195).
- scaleway module utils - improve split call to fix sanity errors (https://github.com/ansible-collections/community.general/pull/3194).
- scaleway plugin inventory - fix ``JSON object must be str, not 'bytes'`` with Python 3.5 (https://github.com/ansible-collections/community.general/issues/2769).
- smartos_image_info - added support to check mode (https://github.com/ansible-collections/community.general/pull/3084).
- snap - fix formatting of ``--channel`` argument when the ``channel`` option is used (https://github.com/ansible-collections/community.general/pull/3028).
- snap - fix various bugs which prevented the module from working at all, and which resulted in ``state=absent`` fail on absent snaps (https://github.com/ansible-collections/community.general/issues/2835, https://github.com/ansible-collections/community.general/issues/2906, https://github.com/ansible-collections/community.general/pull/2912).
- snap - fixed the order of the ``--classic`` parameter in the command line invocation (https://github.com/ansible-collections/community.general/issues/2916).
- snmp_facts - added support to check mode (https://github.com/ansible-collections/community.general/pull/3084).
- ssh_config - reduce stormssh searches based on host (https://github.com/ansible-collections/community.general/pull/2568/).
- stacki_host - when adding a new server, ``rack`` and ``rank`` must be passed, and network parameters are optional (https://github.com/ansible-collections/community.general/pull/2681).
- supervisorctl - state ``signalled`` was not working (https://github.com/ansible-collections/community.general/pull/3068).
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
- vbox inventory script - change function argument name to fix sanity errors (https://github.com/ansible-collections/community.general/pull/3195).
- vdo - boolean arguments now compared with proper ``true`` and ``false`` values instead of string representations like ``"yes"`` or ``"no"`` (https://github.com/ansible-collections/community.general/pull/3191).
- xenserver_facts - added support to check mode (https://github.com/ansible-collections/community.general/pull/3084).
- xfconf - also use ``LC_ALL`` to enforce locale choice (https://github.com/ansible-collections/community.general/issues/2715).
- xfconf_info - added support to check mode (https://github.com/ansible-collections/community.general/pull/3084).
- yum_versionlock - fix idempotency when using wildcard (asterisk) in ``name`` option (https://github.com/ansible-collections/community.general/issues/2761).
- zfs - treated received properties as local (https://github.com/ansible-collections/community.general/pull/502).
- zypper_repository - fix idempotency on adding repository with ``$releasever`` and ``$basearch`` variables (https://github.com/ansible-collections/community.general/issues/1985).

community.grafana
~~~~~~~~~~~~~~~~~

- Fix an issue with datasource uid now returned by the Grafana API (#176)
- Fix issue with trailing '/' in provided grafana_url. The modules now support values with trailing slashes.
- grafana_dashboard lookup - All valid API keys can be used, not just keys ending in '=='.
- grafana_dashboard now explicitely fails if the folder doesn't exist upon creation. It would previously silently pass but not create the dashboard. (https://github.com/ansible-collections/community.grafana/issues/153)
- grafana_team now able to handle spaces and other utf-8 chars in the name parameter. (https://github.com/ansible-collections/community.grafana/issues/164)

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

community.okd
~~~~~~~~~~~~~

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

- api - when using TLS/SSL, remove explicit cipher configuration to insecure values, which also makes it impossible to connect to newer RouterOS versions (https://github.com/ansible-collections/community.routeros/pull/34).

community.vmware
~~~~~~~~~~~~~~~~

- vmware - changed to use from isinstance to type in the if condition of option_diff method (https://github.com/ansible-collections/community.vmware/pull/983).
- vmware - fix that the return value should be returned None if moId doesn't exist of a virtual machine (https://github.com/ansible-collections/community.vmware/pull/867).
- vmware - fixed a bug that the guest_guestion in the facts doesn't convert to the dictionary (https://github.com/ansible-collections/community.vmware/pull/825).
- vmware - handle exception raised in ``get_all_objs`` and ``find_object_by_name`` which occurs due to multiple parallel operations (https://github.com/ansible-collections/community.vmware/issues/791).
- vmware_category - fixed some issues that the errors have occurred in executing the module (https://github.com/ansible-collections/community.vmware/pull/990).
- vmware_cluster_info - Fix a bug that returned enabled_vsan and vsan_auto_claim_storage as lists instead of just true or false (https://github.com/ansible-collections/community.vmware/issues/805).
- vmware_content_deploy_ovf_template - no longer requires host, datastore, resource_pool.
- vmware_content_deploy_xxx - deploys to recommended datastore in specified datastore_cluster.
- vmware_content_deploy_xxx - honors folder specified by fully qualified path name.
- vmware_evc_mode - fixed an issue that evc_mode is required when the state parameter set to absent (https://github.com/ansible-collections/community.vmware/pull/764).
- vmware_guest - Use hostname parameter in customization only if value is not None (https://github.com/ansible-collections/community.vmware/issues/655)
- vmware_guest - add message for `deploy_vm` method when it fails with timeout error while customizing the VM (https://github.com/ansible-collections/community.vmware/pull/933).
- vmware_guest - skip customvalues while deploying VM on a standalone ESXi (https://github.com/ansible-collections/community.vmware/issues/721).
- vmware_guest_instant_clone - fixed an issue that the module should be required the guestinfo_vars parameter when executing (https://github.com/ansible-collections/community.vmware/pull/962).
- vmware_guest_network - Fix adding more than one NIC to a VM before powering on (https://github.com/ansible-collections/community.vmware/issues/860).
- vmware_guest_powerstate - added the datacenter parameter to fix an issue that datacenter key error has been occurring (https://github.com/ansible-collections/community.vmware/pull/924).
- vmware_host_datastore - fixed an issue that the right error message isn't displayed (https://github.com/ansible-collections/community.vmware/pull/976).
- vmware_host_iscsi_info - fixed an issue that an error occurs gathering iSCSI information against an ESXi Host with iSCSI disabled (https://github.com/ansible-collections/community.vmware/pull/729).
- vmware_vm_info - handle vApp parent logic (https://github.com/ansible-collections/community.vmware/issues/777).
- vmware_vm_shell - handle exception raised while performing the operation (https://github.com/ansible-collections/community.vmware/issues/732).
- vmware_vm_storage_policy_info - fixed an issue that the module can't get storage policy info when the policy has the tag base rules (https://github.com/ansible-collections/community.vmware/pull/788).
- vmware_vmotion - Provide an meaningful error message when providing a bad ESXi node as ``destination_host`` (https://github.com/ansible-collections/vmware/pull/804).
- vmware_vmotion - implement new parameter named destination_datacenter to fix failure to move storage when datastores are shared across datacenters (https://github.com/ansible-collections/community.vmware/issues/858)

community.windows
~~~~~~~~~~~~~~~~~

- win_dns_record - Fix issue when trying to use the ``computer_name`` option - https://github.com/ansible-collections/community.windows/issues/276
- win_dns_zone - Fix idempotency when using a DNS zone with forwarders - https://github.com/ansible-collections/community.windows/issues/259
- win_domain_group_member - Fix faulty logic when comparing existing group members - https://github.com/ansible-collections/community.windows/issues/256
- win_domain_group_membership - Handle timeouts when dealing with group with lots of members - https://github.com/ansible-collections/community.windows/pull/204
- win_domain_user - Fallback to NETBIOS username for password verification check if the UPN is not set - https://github.com/ansible-collections/community.windows/pull/289
- win_domain_user - Make sure a password is set to change when it is marked as password needs to be changed before logging in - https://github.com/ansible-collections/community.windows/issues/223
- win_domain_user - fix reporting on user when running in check mode - https://github.com/ansible-collections/community.windows/pull/248
- win_initialize_disk - Ensure ``online: False`` doesn't bring the disk online again - https://github.com/ansible-collections/community.windows/pull/268
- win_lineinfile - Avoid stripping the newline at the end of a file - https://github.com/ansible-collections/community.windows/pull/219
- win_lineinfile - Fix crash when using ``insertbefore`` and ``insertafter`` at the same time - https://github.com/ansible-collections/community.windows/issues/220
- win_lineinfile - Fix up diff output with ending newlines - https://github.com/ansible-collections/community.windows/pull/283
- win_partition - Fix gtp_type setting in win_partition - https://github.com/ansible-collections/community.windows/issues/241
- win_product_facts - fixed an issue that the module doesn't correctly convert a product id (https://github.com/ansible-collections/community.windows/pull/251).
- win_psmodule - Makes sure ``-AllowClobber`` is used when updating pre-requisites if requested - https://github.com/ansible-collections/community.windows/issues/42
- win_pssession_configuration - the ``async_poll`` option was not actually used and polling mode was always used with the default poll delay; this change also formally disables ``async_poll=0`` (https://github.com/ansible-collections/community.windows/pull/212).
- win_region - Fix ``copy_settings`` on a host that has disabled ``reg.exe`` access - https://github.com/ansible-collections/community.windows/issues/287
- win_wait_for_process - Fix bug when specifying multiple ``process_name_exact`` values - https://github.com/ansible-collections/community.windows/issues/203

community.zabbix
~~~~~~~~~~~~~~~~

- zabbix_agent - StatusPort will be configured only when `zabbix_agent2_statusport` is defined (https://github.com/ansible-collections/community.zabbix/pull/378)
- zabbix_agent - fixed issue preventing installation of zabbix-agent 4.2 on Ubuntu Focal 20.04 (https://github.com/ansible-collections/community.zabbix/pull/390)
- zabbix_agent - role will now configure correct port for hostinterface in Zabbix Server if `zabbix_agent2_listenport` is defined (https://github.com/ansible-collections/community.zabbix/pull/400)
- zabbix_agent - should no longer be failing on Windows platform due to re-running all of the tasks for the 2nd time (https://github.com/ansible-collections/community.zabbix/pull/376)
- zabbix_agent - should no longer fail while cleaning up zabbix_agent installation if Zabbix Agent2 is being used (https://github.com/ansible-collections/community.zabbix/pull/409)
- zabbix_agent - will no longer install zabbix_get package on Debian systems when `zabbix_agent_install_agent_only` is defined (https://github.com/ansible-collections/community.zabbix/pull/363)
- zabbix_host - fixed issue where module was idempotent when multiple host interfaces of the same type were present (https://github.com/ansible-collections/community.zabbix/pull/391)
- zabbix_proxy (role) - will no longer fail on proxy creation in Zabbix Server when TLS parameters are used (https://github.com/ansible-collections/community.zabbix/pull/388)
- zabbix_server - Removed the removal everything from /tmp directory command as it removes things that it shouldnt do.
- zabbix_template - first time import of template now works with Zabbix 5.4 (https://github.com/ansible-collections/community.zabbix/pull/407), please note that rerunning the task will fail as there are breaking changes in Zabbix 5.4 API that module not yet covers.
- zabbix_user - now works with Zabbix 5.4 (https://github.com/ansible-collections/community.zabbix/pull/406)

containers.podman
~~~~~~~~~~~~~~~~~

- Add .service extension to systemd files
- Add aliases for image load/save
- Add meta/runtime.yml which is required for Galaxy now
- Add support for podman pod create --infra-name
- Avoid exposing pipelining support for podman connections
- Change present state to be as created state
- Change python version for ansible-core to 3.9
- Disable no-hosts idempotency
- Fix ansible-test issues for CI
- Fix failure when listing containers
- Fix idempotency for environment
- Fix idempotency when containers have a common network
- Fix idempotency with systemd podman files
- Fix ipv6=false issue
- Fix multi-containers options
- Fix overlayfs issue in CI for buildah connection
- Fix suboption key in podman_container/podman_pod for generate_systemd documentation
- Remove idempotency for volume UID/GID
- Remove idempotency leftovers of volumes GID,UID

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- Handled invalid share and unused imports cleanup for iDRAC modules (https://github.com/dell/dellemc-openmanage-ansible-modules/issues/268)
- dellemc_idrac_storage_volume - Module fails if the BlockSize, FreeSize, or Size state of the physical disk is set to "Not Available".

f5networks.f5_modules
~~~~~~~~~~~~~~~~~~~~~

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

fortinet.fortios
~~~~~~~~~~~~~~~~

- Disable check_mode feature from all global objects of configuration modules due to 'state' issue.
- Fix a bug in IP_PREFIX.match().
- Fix a regression bug caused by non-required attributes.
- Fix an intentional exception for listed options.
- Fix the KeyError caused by non-required multi-value attributes in an object.
- Fix the authorization fails at log in with username and password in FOS7.0.
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
- na_ontap_autosupport - KeyError - No element by given name validate-digital-certificate.
- na_ontap_autosupport - TypeError - '>' not supported between instances of 'str' and 'list'.
- na_ontap_cluster_peer - KeyError on dest_cluster_name if destination is unreachable.
- na_ontap_cluster_peer - KeyError on username when using certicate.
- na_ontap_export_policy_rule - change ``anonymous_user_id`` type to str to accept user name and user id.   (A warning is now triggered when a number is not quoted.)
- na_ontap_flexcache - one occurrence of msg missing in call to fail_json.
- na_ontap_igroup - one occurrence of msg missing in call to fail_json.
- na_ontap_igroups - nested igroups are not supported on ONTAP 9.9.0 but are on 9.9.1.
- na_ontap_iscsi_security - IndexError list index out of range if vserver does not exist
- na_ontap_iscsi_security - cannot change authentication_type
- na_ontap_job_schedule - fix documentation for REST ranges for months.
- na_ontap_job_schedule - fix idempotency issue with REST when job_minutes is set to -1.
- na_ontap_ldap_client - remove limitation on schema so that custom schemas can be used.
- na_ontap_lun - three occurrencse of msg missing in call to fail_json.
- na_ontap_lun_map_reporting_nodes - one occurrence of msg missing in call to fail_json.
- na_ontap_object_store - when using REST, wait for job status to correctly report errors.
- na_ontap_quotas - attempt to retry on ``13001:success`` ZAPI error.  Add debug data.
- na_ontap_quotas - fail to reinitialize on create if quota is already on.
- na_ontap_rest_cli - removed incorrect statement indicating that console access is required.
- na_ontap_snapmirror - improve error message when option is not supported with ZAPI.
- na_ontap_snapmirror - one occurrence of msg missing in call to fail_json.
- na_ontap_volume_clone - ``parent_vserver`` can not be given with ``junction_path``, ``uid``, or ``gid``
- na_ontap_vserver_delete role - delete iSCSI igroups and CIFS server before deleting vserver.
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
- Fix mapping between power_outlet_template and power_port_template.
- Inventory - Update plugin to support location for NetBox 2.11+ [#510](https://github.com/netbox-community/ansible_modules/pull/510)
- inventory - Fix rack-group -> location for NetBox 2.11 changes.
- inventory - Properly handle interface tags.
- netbox_tenant - Fix example to match argspec.

ngine_io.cloudstack
~~~~~~~~~~~~~~~~~~~

- cs_instance - Fixed attribute error in custom service offerings handling (https://github.com/ngine-io/ansible-collection-cloudstack/pull/87).
- cs_instance - Fixed custom service offerings usage (https://github.com/ngine-io/ansible-collection-cloudstack/issues/79).

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
- ome_smart_fabric_uplink - Issue(186024) ome_smart_fabric_uplink module does not allow the creation of multiple uplinks of the same name even though it is supported by OpenManage Enterprise Modular. If an uplink is created using the same name as an existing uplink, the existing uplink is modified.
- ome_smart_fabric_uplink - Issue(186024) ome_smart_fabric_uplink module does not allow the creation of multiple uplinks of the same name even though this is supported by OpenManage Enterprise Modular. If an uplink is created using the same name as an existing uplink, the existing uplink is modified.

New Plugins
-----------

Callback
~~~~~~~~

- community.general.opentelemetry - Create distributed traces with OpenTelemetry

Connection
~~~~~~~~~~

- community.docker.nsenter - execute on host running controller container

Filter
~~~~~~

- community.dns.get_public_suffix - Returns the public suffix of a DNS name
- community.dns.get_registrable_domain - Returns the registrable domain name of a DNS name
- community.dns.remove_public_suffix - Removes the public suffix from a DNS name
- community.dns.remove_registrable_domain - Removes the registrable domain name from a DNS name
- community.general.groupby_as_dict - Transform a sequence of dictionaries to a dictionary where the dictionaries are indexed by an attribute
- community.general.unicode_normalize - Normalizes unicode strings to facilitate comparison of characters with normalized forms
- community.sops.decrypt - Decrypt sops-encrypted data

Httpapi
~~~~~~~

- cisco.mso.mso - MSO Ansible HTTPAPI Plugin.

Inventory
~~~~~~~~~

- community.dns.hetzner_dns_records - Create inventory from Hetzner DNS records
- community.dns.hosttech_dns_records - Create inventory from Hosttech DNS records
- community.general.icinga2 - Icinga2 inventory source
- community.vmware.vmware_host_inventory - VMware ESXi hostsystem inventory source
- community.zabbix.zabbix_inventory - Zabbix Inventory Plugin

Lookup
~~~~~~

- community.general.dependent - Composes a list with nested elements of other lists or dicts which can depend on previous loop variables
- community.general.random_pet - Generates random pet names
- community.general.random_string - Generates random string
- kubernetes.core.kustomize - Build a set of kubernetes resources using a 'kustomization.yaml' file.

Netconf
~~~~~~~

- cisco.nxos.nxos - Use nxos netconf plugin to run netconf commands on Cisco NX-OS platform.

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

community.dns
~~~~~~~~~~~~~

- community.dns.hetzner_dns_record - Add or delete a single record in Hetzner DNS service
- community.dns.hetzner_dns_record_info - Retrieve records in Hetzner DNS service
- community.dns.hetzner_dns_record_set - Add or delete record sets in Hetzner DNS service
- community.dns.hetzner_dns_record_set_info - Retrieve record sets in Hetzner DNS service
- community.dns.hetzner_dns_record_sets - Bulk synchronize DNS record sets in Hetzner DNS service
- community.dns.hetzner_dns_zone_info - Retrieve zone information in Hetzner DNS service
- community.dns.hosttech_dns_record - Add or delete a single record in Hosttech DNS service
- community.dns.hosttech_dns_record_info - Retrieve records in Hosttech DNS service
- community.dns.hosttech_dns_record_set - Add or delete record sets in Hosttech DNS service
- community.dns.hosttech_dns_record_sets - Bulk synchronize DNS record sets in Hosttech DNS service
- community.dns.hosttech_dns_records - Bulk synchronize DNS records in Hosttech DNS service
- community.dns.hosttech_dns_zone_info - Retrieve zone information in Hosttech DNS service
- community.dns.wait_for_txt - Wait for TXT entries to be available on all authoritative nameservers

community.general
~~~~~~~~~~~~~~~~~

Cloud
^^^^^

Misc
....

- community.general.proxmox_nic - Management of a NIC of a Qemu(KVM) VM in a Proxmox VE cluster.

Database
^^^^^^^^

Misc
....

- community.general.redis_data - Set key value pairs in Redis
- community.general.redis_data_info - Get value of key in Redis database

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

Os
..

- community.general.pacman_key - Manage pacman's list of trusted keys

Source Control
^^^^^^^^^^^^^^

Gitlab
......

- community.general.gitlab_protected_branch - (un)Marking existing branches for protection

System
^^^^^^

- community.general.sap_task_list_execute - Perform SAP Task list execution
- community.general.xfconf_info - Retrieve XFCE4 configurations

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

- community.vmware.vmware_host_custom_attributes - Manage custom attributes from VMware for the given ESXi host
- community.vmware.vmware_host_passthrough - Manage PCI device passthrough settings on host
- community.vmware.vmware_host_tcpip_stacks - Manage the TCP/IP Stacks configuration of ESXi host
- community.vmware.vmware_object_custom_attributes_info - Gather custom attributes of an object
- community.vmware.vmware_object_role_permission_info - Gather information about object's permissions
- community.vmware.vmware_recommended_datastore - Returns the recommended datastore from a SDRS-enabled datastore cluster

community.windows
~~~~~~~~~~~~~~~~~

- community.windows.win_feature_info - Gather information about Windows features

community.zabbix
~~~~~~~~~~~~~~~~

- community.zabbix.zabbix_globalmacro - Create/update/delete Zabbix Global macros

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

- check_point.mgmt (still version 2.0.0)
- chocolatey.chocolatey (still version 1.1.0)
- cisco.aci (still version 2.0.0)
- cisco.nso (still version 1.0.3)
- cisco.ucs (still version 1.6.0)
- community.azure (still version 1.0.0)
- community.fortios (still version 1.0.0)
- community.google (still version 1.0.0)
- community.hrobot (still version 1.1.1)
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
- infinidat.infinibox (still version 1.2.4)
- mellanox.onyx (still version 1.0.0)
- ngine_io.exoscale (still version 1.0.0)
- ngine_io.vultr (still version 1.1.0)
- splunk.es (still version 1.0.2)
- wti.remote (still version 1.0.1)
