=======================
Ansible 8 Release Notes
=======================

This changelog describes changes since Ansible 7.0.0.

.. contents::
  :local:
  :depth: 2

v8.0.0a3
========

.. contents::
  :local:
  :depth: 2

Release Summary
---------------

Release Date: 2023-05-02

`Porting Guide <https://docs.ansible.com/ansible/devel/porting_guides.html>`_

Ansible-core
------------

Ansible 8.0.0a3 contains Ansible-core version 2.15.0rc2.
This is a newer version than version 2.15.0rc1 contained in the previous Ansible release.

The changes are reported in the combined changelog below.

Changed Collections
-------------------

If not mentioned explicitly, the changes are reported in the combined changelog below.

+-------------------------+-----------------+-----------------+-------+
| Collection              | Ansible 8.0.0a2 | Ansible 8.0.0a3 | Notes |
+=========================+=================+=================+=======+
| ansible.windows         | 1.13.0          | 1.14.0          |       |
+-------------------------+-----------------+-----------------+-------+
| cisco.iosxr             | 5.0.1           | 5.0.2           |       |
+-------------------------+-----------------+-----------------+-------+
| community.crypto        | 2.12.0          | 2.13.0          |       |
+-------------------------+-----------------+-----------------+-------+
| community.docker        | 3.4.3           | 3.4.4           |       |
+-------------------------+-----------------+-----------------+-------+
| community.hashi_vault   | 4.2.0           | 4.2.1           |       |
+-------------------------+-----------------+-----------------+-------+
| community.windows       | 1.12.0          | 1.13.0          |       |
+-------------------------+-----------------+-----------------+-------+
| ibm.spectrum_virtualize | 1.11.0          | 1.12.0          |       |
+-------------------------+-----------------+-----------------+-------+
| junipernetworks.junos   | 5.0.0           | 5.1.0           |       |
+-------------------------+-----------------+-----------------+-------+
| lowlydba.sqlserver      | 1.3.1           | 2.0.0           |       |
+-------------------------+-----------------+-----------------+-------+
| microsoft.ad            | 1.0.0           | 1.1.0           |       |
+-------------------------+-----------------+-----------------+-------+
| openvswitch.openvswitch | 2.1.0           | 2.1.1           |       |
+-------------------------+-----------------+-----------------+-------+

Minor Changes
-------------

Ansible-core
~~~~~~~~~~~~

- The minimum required ``setuptools`` version is now 45.2.0, as it is the oldest version to support Python 3.10.
- Use ``package_data`` instead of ``include_package_data`` for ``setup.cfg`` to avoid ``setuptools`` warnings.

ansible.windows
~~~~~~~~~~~~~~~

- Process - Add support for starting a process with a custom parent
- win_updates - Added the ``rebooted`` return value to document if a host was rebooted - https://github.com/ansible-collections/ansible.windows/issues/485

community.crypto
~~~~~~~~~~~~~~~~

- x509_crl - the ``crl_mode`` option has been added to replace the existing ``mode`` option (https://github.com/ansible-collections/community.crypto/issues/596).

community.docker
~~~~~~~~~~~~~~~~

- Restrict requests to versions before 2.29.0, and urllib3 to versions before 2.0.0. This is necessary until the vendored code from Docker SDK for Python has been fully adjusted to work with a feature of urllib3 that is used since requests 2.29.0 (https://github.com/ansible-collections/community.docker/issues/611, https://github.com/ansible-collections/community.docker/pull/612).

community.windows
~~~~~~~~~~~~~~~~~

- Raise minimum Ansible version to ``2.12`` or newer
- win_dns_record - Add parameter ``aging`` for creating non-static DNS records.
- win_domain_computer - Add ActiveDirectory module import
- win_domain_object_info - Add ActiveDirectory module import
- win_psmodule - add ``force`` option to allow overwriting/updating existing module dependency only if requested
- win_pssession_configuration - Add diff mode support

ibm.spectrum_virtualize
~~~~~~~~~~~~~~~~~~~~~~~

- ibm_svc_host - Added support for NVMe ROCE host.
- ibm_svc_info - Added new options for gather_subset parameter.
- ibm_svc_manage_portset - Added support for FC portset and rename functionality.
- ibm_svc_mdiskgrp - Added more parameters for storage pool configuration.

junipernetworks.junos
~~~~~~~~~~~~~~~~~~~~~

- Adding unlink option to junos package installation.

Breaking Changes / Porting Guide
--------------------------------

lowlydba.sqlserver
~~~~~~~~~~~~~~~~~~

- Updating minimum DBATools version to v2.0.0 to allow for pwsh 7.3+ compatibility. There may also be breaking change behavior in DBATools, see https://blog.netnerds.net/2023/03/whats-new-dbatools-2.0/. (https://github.com/lowlydba/lowlydba.sqlserver/pull/181)

Deprecated Features
-------------------

community.crypto
~~~~~~~~~~~~~~~~

- x509_crl - the ``mode`` option is deprecated; use ``crl_mode`` instead. The ``mode`` option will change its meaning in community.crypto 3.0.0, and will refer to the CRL file's mode instead (https://github.com/ansible-collections/community.crypto/issues/596).

Bugfixes
--------

Ansible-core
~~~~~~~~~~~~

- ansible-galaxy - fix installing signed collections (https://github.com/ansible/ansible/issues/80648).
- ansible-galaxy collection verify - fix verifying signed collections when the keyring is not configured.

ansible.windows
~~~~~~~~~~~~~~~

- setup - Be more resilient when parsing the BIOS release date - https://github.com/ansible-collections/ansible.windows/pull/496
- win_package - Fix ``product_id`` check and skip downloaded requested file if the package is already installed - https://github.com/ansible-collections/ansible.windows/issues/479
- win_updates - Add better handling for the polling output for connection plugins that might drop newlines on the output - https://github.com/ansible-collections/ansible.windows/issues/477
- win_updates - Ensure failure condition doesn't lock the polling file - https://github.com/ansible-collections/ansible.windows/issues/490
- win_updates - Improve batch task runner reliability and attempt to return more info on failures - https://github.com/ansible-collections/ansible.windows/issues/448

cisco.iosxr
~~~~~~~~~~~

- interfaces - Fix issue in ``overridden`` state of interfaces RM. (https://github.com/ansible-collections/cisco.iosxr/issues/377)

community.crypto
~~~~~~~~~~~~~~~~

- openssh_keypair - always generate a new key pair if the private key does not exist. Previously, the module would fail when ``regenerate=fail`` without an existing key, contradicting the documentation (https://github.com/ansible-collections/community.crypto/pull/598).
- x509_crl - remove problem with ansible-core 2.16 due to ``AnsibleModule`` is now validating the ``mode`` parameter's values (https://github.com/ansible-collections/community.crypto/issues/596).

community.windows
~~~~~~~~~~~~~~~~~

- win_disk_facts - Fix issue when enumerating non-physical disks or disks without numbers - https://github.com/ansible-collections/community.windows/issues/474
- win_firewall_rule - fix program cannot be set to any on existing rules.
- win_psmodule - Fix missing AcceptLicense parameter that occurs when the pre-reqs have been installed - https://github.com/ansible-collections/community.windows/issues/487
- win_pssession_configuration - Fix parser error (Invalid JSON primitive: icrosoft.WSMan.Management.WSManConfigContainerElement)
- win_xml - Fixes the issue when no childnode is defined and will allow adding a new element to an empty element.
- win_zip - fix source appears to use backslashes as path separators issue when extracting Zip archve in non-Windows environment - https://github.com/ansible-collections/community.windows/issues/442

junipernetworks.junos
~~~~~~~~~~~~~~~~~~~~~

- Fix enabled attribute implementation.
- Fix lldp_global_assertion.
- Fix sanity issues.
- Fix the snmp view and traps configuration.
- fix the implementation of disabling interface.
- module should return with failure when rollback is 0 and device is not reachable.

microsoft.ad
~~~~~~~~~~~~

- microsoft.ad.user - Fix setting ``password_expired`` when creating a new user - https://github.com/ansible-collections/microsoft.ad/issues/25

openvswitch.openvswitch
~~~~~~~~~~~~~~~~~~~~~~~

- Fix galaxy version issue when installing this collection.

Known Issues
------------

community.docker
~~~~~~~~~~~~~~~~

- The modules and plugins using the vendored code from Docker SDK for Python currently do not work with requests 2.29.0 and/or urllib3 2.0.0. The same is currently true for the latest version of Docker SDK for Python itself (https://github.com/ansible-collections/community.docker/issues/611, https://github.com/ansible-collections/community.docker/pull/612).

New Plugins
-----------

Filter
~~~~~~

- microsoft.ad.as_datetime - Converts an LDAP value to a datetime string
- microsoft.ad.as_guid - Converts an LDAP value to a GUID string
- microsoft.ad.as_sid - Converts an LDAP value to a Security Identifier string

Inventory
~~~~~~~~~

- microsoft.ad.ldap - Inventory plugin for Active Directory

New Modules
-----------

ibm.spectrum_virtualize
~~~~~~~~~~~~~~~~~~~~~~~

- ibm.spectrum_virtualize.ibm_sv_manage_fc_partnership - Manages FC partnership on Spectrum Virtualize systems
- ibm.spectrum_virtualize.ibm_sv_manage_fcportsetmember - Manages addition or removal of ports from the Fibre Channel (FC) portsets on Spectrum Virtualize storage systems

microsoft.ad
~~~~~~~~~~~~

- microsoft.ad.debug_ldap_client - Get host information for debugging LDAP connections

Unchanged Collections
---------------------

- amazon.aws (still version 5.4.0)
- ansible.netcommon (still version 5.1.0)
- ansible.posix (still version 1.5.2)
- ansible.utils (still version 2.9.0)
- arista.eos (still version 6.0.1)
- awx.awx (still version 22.1.0)
- azure.azcollection (still version 1.15.0)
- check_point.mgmt (still version 5.0.0)
- chocolatey.chocolatey (still version 1.4.0)
- cisco.aci (still version 2.6.0)
- cisco.asa (still version 4.0.0)
- cisco.dnac (still version 6.7.1)
- cisco.intersight (still version 1.0.27)
- cisco.ios (still version 4.5.0)
- cisco.ise (still version 2.5.12)
- cisco.meraki (still version 2.15.1)
- cisco.mso (still version 2.4.0)
- cisco.nso (still version 1.0.3)
- cisco.nxos (still version 4.3.0)
- cisco.ucs (still version 1.8.0)
- cloud.common (still version 2.1.3)
- cloudscale_ch.cloud (still version 2.2.4)
- community.aws (still version 5.4.0)
- community.azure (still version 2.0.0)
- community.ciscosmb (still version 1.0.5)
- community.digitalocean (still version 1.23.0)
- community.dns (still version 2.5.3)
- community.fortios (still version 1.0.0)
- community.general (still version 6.6.0)
- community.google (still version 1.0.0)
- community.grafana (still version 1.5.4)
- community.hrobot (still version 1.8.0)
- community.libvirt (still version 1.2.0)
- community.mongodb (still version 1.5.2)
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
- community.zabbix (still version 1.9.3)
- containers.podman (still version 1.10.1)
- cyberark.conjur (still version 1.2.0)
- cyberark.pas (still version 1.0.17)
- dellemc.enterprise_sonic (still version 2.0.0)
- dellemc.openmanage (still version 7.5.0)
- dellemc.powerflex (still version 1.6.0)
- dellemc.unity (still version 1.6.0)
- f5networks.f5_modules (still version 1.24.0)
- fortinet.fortimanager (still version 2.1.7)
- fortinet.fortios (still version 2.2.3)
- frr.frr (still version 2.0.2)
- gluster.gluster (still version 1.0.2)
- google.cloud (still version 1.1.3)
- grafana.grafana (still version 2.0.0)
- hetzner.hcloud (still version 1.11.0)
- hpe.nimble (still version 1.1.4)
- ibm.qradar (still version 2.1.0)
- infinidat.infinibox (still version 1.3.12)
- infoblox.nios_modules (still version 1.4.1)
- inspur.ispim (still version 1.3.0)
- inspur.sm (still version 2.3.0)
- kubernetes.core (still version 2.4.0)
- netapp.aws (still version 21.7.0)
- netapp.azure (still version 21.10.0)
- netapp.cloudmanager (still version 21.22.0)
- netapp.elementsw (still version 21.7.0)
- netapp.ontap (still version 22.5.0)
- netapp.storagegrid (still version 21.11.1)
- netapp.um_info (still version 21.8.0)
- netapp_eseries.santricity (still version 1.4.0)
- netbox.netbox (still version 3.12.0)
- ngine_io.cloudstack (still version 2.3.0)
- ngine_io.exoscale (still version 1.0.0)
- ngine_io.vultr (still version 1.1.3)
- openstack.cloud (still version 2.1.0)
- ovirt.ovirt (still version 3.1.2)
- purestorage.flasharray (still version 1.17.2)
- purestorage.flashblade (still version 1.11.0)
- purestorage.fusion (still version 1.4.2)
- sensu.sensu_go (still version 1.13.2)
- servicenow.servicenow (still version 1.0.6)
- splunk.es (still version 2.1.0)
- t_systems_mms.icinga_director (still version 1.32.2)
- theforeman.foreman (still version 3.10.0)
- vmware.vmware_rest (still version 2.3.1)
- vultr.cloud (still version 1.7.0)
- vyos.vyos (still version 4.0.2)
- wti.remote (still version 1.0.4)

v8.0.0a2
========

.. contents::
  :local:
  :depth: 2

Release Summary
---------------

Release Date: 2023-04-26

`Porting Guide <https://docs.ansible.com/ansible/devel/porting_guides.html>`_

Ansible-core
------------

Ansible 8.0.0a2 contains Ansible-core version 2.15.0rc1.
This is a newer version than version 2.15.0b2 contained in the previous Ansible release.

The changes are reported in the combined changelog below.

Changed Collections
-------------------

If not mentioned explicitly, the changes are reported in the combined changelog below.

+------------------------+-----------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| Collection             | Ansible 8.0.0a1 | Ansible 8.0.0a2 | Notes                                                                                                                        |
+========================+=================+=================+==============================================================================================================================+
| awx.awx                | 22.0.0          | 22.1.0          | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+------------------------+-----------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| check_point.mgmt       | 4.0.0           | 5.0.0           |                                                                                                                              |
+------------------------+-----------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.aci              | 2.5.0           | 2.6.0           |                                                                                                                              |
+------------------------+-----------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.dnac             | 6.7.0           | 6.7.1           | The collection did not have a changelog in this version.                                                                     |
+------------------------+-----------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.intersight       | 1.0.24          | 1.0.27          | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+------------------------+-----------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.ios              | 4.4.1           | 4.5.0           |                                                                                                                              |
+------------------------+-----------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.mso              | 2.3.0           | 2.4.0           |                                                                                                                              |
+------------------------+-----------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.crypto       | 2.11.1          | 2.12.0          |                                                                                                                              |
+------------------------+-----------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.dns          | 2.5.2           | 2.5.3           |                                                                                                                              |
+------------------------+-----------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.general      | 6.5.0           | 6.6.0           |                                                                                                                              |
+------------------------+-----------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| dellemc.openmanage     | 7.4.0           | 7.5.0           |                                                                                                                              |
+------------------------+-----------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| f5networks.f5_modules  | 1.23.0          | 1.24.0          |                                                                                                                              |
+------------------------+-----------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| frr.frr                | 2.0.0           | 2.0.2           |                                                                                                                              |
+------------------------+-----------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| openstack.cloud        | 2.0.0           | 2.1.0           | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+------------------------+-----------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| purestorage.flashblade | 1.10.0          | 1.11.0          |                                                                                                                              |
+------------------------+-----------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+

Minor Changes
-------------

cisco.aci
~~~~~~~~~

- Add aci_access_span_dst_group module for fabric access policies span destination group support (#405)
- Add aci_access_span_filter_group and aci_access_span_filter_group_entry modules for access span filter group support (#407)
- Add aci_config_export_policy module (#380)
- Add aci_igmp_interface_policy module (#381)

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

f5networks.f5_modules
~~~~~~~~~~~~~~~~~~~~~

- bigip_ssl_certificate - added an option to prevent adding .crt extension to cert names
- bigip_ssl_key - added an option to prevent adding .key extension to key names
- bigip_ssl_key_cert - added an option to prevent adding .key and .crt extensions to key and cert names respectively

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

Deprecated Features
-------------------

check_point.mgmt
~~~~~~~~~~~~~~~~

- add/set/delete nat-rule modules - will be replaced by the single cp_mgmt_nat_rule module.
- cp_mgmt_show_task/s modules - will be replaced by the by the single cp_mgmt_task_facts module.

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

- Display - Defensively configure writing to stdout and stderr with a custom encoding error handler that will replace invalid characters while providing a deprecation warning that non-utf8 text will result in an error in a future version.
- Fix post-validating looped task fields so the strategy uses the correct values after task execution.
- Prevent running same handler multiple times when included via ``include_role`` (https://github.com/ansible/ansible/issues/73643)
- ``pkg_mgr`` - fix the default dnf version detection
- ansible-galaxy - fix installing collections from directories that have a trailing path separator (https://github.com/ansible/ansible/issues/77803).
- ansible-test - Add support for ``argcomplete`` version 3.
- ansible-test - Update ``pylint`` to 2.17.2 to resolve several possible false positives.
- ansible-test - Update ``pylint`` to 2.17.3 to resolve several possible false positives.
- ansible-test - When bootstrapping remote FreeBSD instances, use the OS packaged ``setuptools`` instead of installing the latest version from PyPI.
- dnf5 - Use ``transaction.check_gpg_signatures`` API call to check package signatures AND possibly to recover from when keys are missing.
- handlers - fix ``v2_playbook_on_notify`` callback not being called when notifying handlers
- module responses - Ensure that module responses are utf-8 adhereing to JSON RFC and expectations of the core code.
- module/role argument spec - validate the type for options that are None when the option is required or has a non-None default (https://github.com/ansible/ansible/issues/79656).
- pep517 build backend - Use the documented ``import_module`` import from ``importlib``.
- syntax check - Limit ``--syntax-check`` to ``ansible-playbook`` only, as that is the only CLI affected by this argument (https://github.com/ansible/ansible/issues/80506)

cisco.ios
~~~~~~~~~

- ios_bgp_address_family - fix issue where no commands are generated when redistributing OSPFv2 and OSPFv3
- ios_bgp_address_family - fix missing negations in overridden and replaced states when redistributing OSPF
- ios_bgp_address_family - fix option and syntax for OSPF E1 and E2 routes
- ios_bgp_address_family - fix option and syntax for OSPF N1 and N2 routes
- ios_bgp_address_family - fix order of generated OSPF redistribution command options to achieve idempotency
- ios_bgp_global - fix configuration of timers under neighbor. (https://github.com/ansible-collections/cisco.ios/issues/794)
- ios_l3_interfaces - prevent configuration line generation when enable is false.
- ios_logging_global - logging history configuration command fixed for supported appliance versions.

cisco.mso
~~~~~~~~~

- Add attributes to payload for changed schema behaviour of deploymentImmediacy (deployImmediacy) and vmmDomainProperties (properties at domain level in payload) (#362)
- Fix mso_backup for NDO and ND-based MSO v3.2+ (#333)
- Fix validation condition for path in mso_schema_site_anp_epg_bulk_staticport module (#360)

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

f5networks.f5_modules
~~~~~~~~~~~~~~~~~~~~~

- bigip_device_info - fix fqdn_up_interval and fqdn_down_interval to no longer cause string values not castable to int to raise an error
- bigip_device_info - fixed flaw in code to ignore fields that do not exist in the response for license info

purestorage.flashblade
~~~~~~~~~~~~~~~~~~~~~~

- purefa_info - Fixed issue when more than 10 buckets have lifecycle rules.
- purefb_s3user - Fix incorrect response when bad key/secret pair provided for new user

Known Issues
------------

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- idrac_os_deployment- Issue(260496) - OS installation will support only NFS and CIFS share to store the custom ISO in the destination_path, HTTP/HTTPS/FTP not supported
- idrac_redfish_storage_contoller - Issue(256164) - If incorrect value is provided for one of the attributes in the provided attribute list for controller configuration, then this module does not exit with error.
- idrac_user - Issue(192043) The module may error out with the message ``Unable to perform the import or export operation because there are pending attribute changes or a configuration job is in progress``. Wait for the job to complete and run the task again.
- ome_application_alerts_syslog - Issue(215374) - The module does not provide a proper error message if the destination_address is more than 255 characters.
- ome_device_network_services - Issue(212681) - The module does not provide a proper error message if unsupported values are provided for the following parameters- port_number, community_name, max_sessions, max_auth_retries, and idle_timeout.
- ome_device_power_settings - Issue(212679) - The module displays the following message if the value provided for the parameter ``power_cap`` is not within the supported range of 0 to 32767, ``Unable to complete the request because PowerCap does not exist or is not applicable for the resource URI.``
- ome_smart_fabric_uplink - Issue(186024) - Despite the module supported by OpenManage Enterprise Modular, it does not allow the creation of multiple uplinks of the same name. If an uplink is created using the same name as an existing uplink, the existing uplink is modified.

New Modules
-----------

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

community.general
~~~~~~~~~~~~~~~~~

- community.general.btrfs_info - Query btrfs filesystem info
- community.general.btrfs_subvolume - Manage btrfs subvolumes
- community.general.ilo_redfish_command - Manages Out-Of-Band controllers using Redfish APIs
- community.general.keycloak_authz_authorization_scope - Allows administration of Keycloak client authorization scopes via Keycloak API
- community.general.keycloak_clientscope_type - Set the type of aclientscope in realm or client via Keycloak API

purestorage.flashblade
~~~~~~~~~~~~~~~~~~~~~~

- purestorage.flashblade.purefb_pingtrace - Employ the internal FlashBlade ping and trace mechanisms

New Roles
---------

- dellemc.openmanage.idrac_firmware - Firmware update from a repository on a network share (CIFS, NFS, HTTP, HTTPS, FTP).
- dellemc.openmanage.redfish_firmware - To perform a component firmware update using the image file available on the local or remote system.
- dellemc.openmanage.redfish_storage_volume - Role to manage the storage volume configuration.

Unchanged Collections
---------------------

- amazon.aws (still version 5.4.0)
- ansible.netcommon (still version 5.1.0)
- ansible.posix (still version 1.5.2)
- ansible.utils (still version 2.9.0)
- ansible.windows (still version 1.13.0)
- arista.eos (still version 6.0.1)
- azure.azcollection (still version 1.15.0)
- chocolatey.chocolatey (still version 1.4.0)
- cisco.asa (still version 4.0.0)
- cisco.iosxr (still version 5.0.1)
- cisco.ise (still version 2.5.12)
- cisco.meraki (still version 2.15.1)
- cisco.nso (still version 1.0.3)
- cisco.nxos (still version 4.3.0)
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
- community.mongodb (still version 1.5.2)
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
- community.zabbix (still version 1.9.3)
- containers.podman (still version 1.10.1)
- cyberark.conjur (still version 1.2.0)
- cyberark.pas (still version 1.0.17)
- dellemc.enterprise_sonic (still version 2.0.0)
- dellemc.powerflex (still version 1.6.0)
- dellemc.unity (still version 1.6.0)
- fortinet.fortimanager (still version 2.1.7)
- fortinet.fortios (still version 2.2.3)
- gluster.gluster (still version 1.0.2)
- google.cloud (still version 1.1.3)
- grafana.grafana (still version 2.0.0)
- hetzner.hcloud (still version 1.11.0)
- hpe.nimble (still version 1.1.4)
- ibm.qradar (still version 2.1.0)
- ibm.spectrum_virtualize (still version 1.11.0)
- infinidat.infinibox (still version 1.3.12)
- infoblox.nios_modules (still version 1.4.1)
- inspur.ispim (still version 1.3.0)
- inspur.sm (still version 2.3.0)
- junipernetworks.junos (still version 5.0.0)
- kubernetes.core (still version 2.4.0)
- lowlydba.sqlserver (still version 1.3.1)
- microsoft.ad (still version 1.0.0)
- netapp.aws (still version 21.7.0)
- netapp.azure (still version 21.10.0)
- netapp.cloudmanager (still version 21.22.0)
- netapp.elementsw (still version 21.7.0)
- netapp.ontap (still version 22.5.0)
- netapp.storagegrid (still version 21.11.1)
- netapp.um_info (still version 21.8.0)
- netapp_eseries.santricity (still version 1.4.0)
- netbox.netbox (still version 3.12.0)
- ngine_io.cloudstack (still version 2.3.0)
- ngine_io.exoscale (still version 1.0.0)
- ngine_io.vultr (still version 1.1.3)
- openvswitch.openvswitch (still version 2.1.0)
- ovirt.ovirt (still version 3.1.2)
- purestorage.flasharray (still version 1.17.2)
- purestorage.fusion (still version 1.4.2)
- sensu.sensu_go (still version 1.13.2)
- servicenow.servicenow (still version 1.0.6)
- splunk.es (still version 2.1.0)
- t_systems_mms.icinga_director (still version 1.32.2)
- theforeman.foreman (still version 3.10.0)
- vmware.vmware_rest (still version 2.3.1)
- vultr.cloud (still version 1.7.0)
- vyos.vyos (still version 4.0.2)
- wti.remote (still version 1.0.4)

v8.0.0a1
========

.. contents::
  :local:
  :depth: 2

Release Summary
---------------

Release Date: 2023-04-12

`Porting Guide <https://docs.ansible.com/ansible/devel/porting_guides.html>`_

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
- microsoft.ad (version 1.0.0)
- servicenow.servicenow (version 1.0.6)

Ansible-core
------------

Ansible 8.0.0a1 contains Ansible-core version 2.15.0b2.
This is a newer version than version 2.14.0 contained in the previous Ansible release.

The changes are reported in the combined changelog below.

Included Collections
--------------------

If not mentioned explicitly, the changes are reported in the combined changelog below.

+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| Collection                    | Ansible 7.0.0 | Ansible 8.0.0a1 | Notes                                                                                                                        |
+===============================+===============+=================+==============================================================================================================================+
| amazon.aws                    | 5.1.0         | 5.4.0           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| ansible.netcommon             | 4.1.0         | 5.1.0           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| ansible.posix                 | 1.4.0         | 1.5.2           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| ansible.utils                 | 2.7.0         | 2.9.0           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| ansible.windows               | 1.12.0        | 1.13.0          |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| arista.eos                    | 6.0.0         | 6.0.1           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| awx.awx                       | 21.8.0        | 22.0.0          | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| azure.azcollection            | 1.14.0        | 1.15.0          | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| chocolatey.chocolatey         | 1.3.1         | 1.4.0           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.aci                     | 2.3.0         | 2.5.0           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.dnac                    | 6.6.0         | 6.7.0           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.intersight              | 1.0.20        | 1.0.24          | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.ios                     | 4.0.0         | 4.4.1           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.iosxr                   | 4.0.2         | 5.0.1           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.ise                     | 2.5.9         | 2.5.12          |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.meraki                  | 2.11.0        | 2.15.1          |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.mso                     | 2.1.0         | 2.3.0           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.nxos                    | 4.0.0         | 4.3.0           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| cloud.common                  | 2.1.2         | 2.1.3           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| cloudscale_ch.cloud           | 2.2.2         | 2.2.4           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.aws                 | 5.0.0         | 5.4.0           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.crypto              | 2.8.1         | 2.11.1          |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.digitalocean        | 1.22.0        | 1.23.0          |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.dns                 | 2.4.1         | 2.5.2           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.docker              | 3.2.1         | 3.4.3           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.general             | 6.0.1         | 6.5.0           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.grafana             | 1.5.3         | 1.5.4           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.hashi_vault         | 4.0.0         | 4.2.0           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.hrobot              | 1.6.0         | 1.8.0           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.mongodb             | 1.4.2         | 1.5.2           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.mysql               | 3.5.1         | 3.6.0           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.okd                 | 2.2.0         | 2.3.0           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.postgresql          | 2.3.0         | 2.3.2           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.proxysql            | 1.4.0         | 1.5.1           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.routeros            | 2.3.1         | 2.8.0           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.sap_libs            | 1.3.0         | 1.4.1           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.sops                | 1.4.1         | 1.6.1           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.vmware              | 3.1.0         | 3.5.0           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.windows             | 1.11.1        | 1.12.0          |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.zabbix              | 1.8.0         | 1.9.3           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| containers.podman             | 1.9.4         | 1.10.1          |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| cyberark.pas                  | 1.0.14        | 1.0.17          | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| dellemc.openmanage            | 6.3.0         | 7.4.0           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| dellemc.powerflex             |               | 1.6.0           | The collection was added to Ansible                                                                                          |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| dellemc.unity                 |               | 1.6.0           | The collection was added to Ansible                                                                                          |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| f5networks.f5_modules         | 1.20.0        | 1.23.0          |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| fortinet.fortios              | 2.1.7         | 2.2.3           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| google.cloud                  | 1.0.2         | 1.1.3           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| grafana.grafana               |               | 2.0.0           | The collection was added to Ansible                                                                                          |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| hetzner.hcloud                | 1.8.2         | 1.11.0          |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| ibm.spectrum_virtualize       | 1.10.0        | 1.11.0          |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| infinidat.infinibox           | 1.3.7         | 1.3.12          | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| infoblox.nios_modules         | 1.4.0         | 1.4.1           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| inspur.ispim                  | 1.2.0         | 1.3.0           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| junipernetworks.junos         | 4.0.0         | 5.0.0           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| kubernetes.core               | 2.3.2         | 2.4.0           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| lowlydba.sqlserver            | 1.0.4         | 1.3.1           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| microsoft.ad                  |               | 1.0.0           | The collection was added to Ansible                                                                                          |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| netapp.cloudmanager           | 21.21.0       | 21.22.0         |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| netapp.ontap                  | 22.0.1        | 22.5.0          |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| netapp_eseries.santricity     | 1.3.1         | 1.4.0           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| netbox.netbox                 | 3.8.1         | 3.12.0          |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| ngine_io.cloudstack           | 2.2.4         | 2.3.0           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| ngine_io.vultr                | 1.1.2         | 1.1.3           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| openstack.cloud               | 1.10.0        | 2.0.0           | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| ovirt.ovirt                   | 2.3.1         | 3.1.2           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| purestorage.flasharray        | 1.14.0        | 1.17.2          |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| purestorage.fusion            | 1.1.1         | 1.4.2           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| sensu.sensu_go                | 1.13.1        | 1.13.2          |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| servicenow.servicenow         |               | 1.0.6           | The collection was added to Ansible                                                                                          |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| t_systems_mms.icinga_director | 1.31.4        | 1.32.2          |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| theforeman.foreman            | 3.7.0         | 3.10.0          |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| vmware.vmware_rest            | 2.2.0         | 2.3.1           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| vultr.cloud                   | 1.3.1         | 1.7.0           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| vyos.vyos                     | 4.0.0         | 4.0.2           |                                                                                                                              |
+-------------------------------+---------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+

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
- Use ``ansible.module_utils.six.moves.collections_abc`` instead of ``ansible.module_utils.common._collections_compat`` in modules and module_utils.
- Use ``collections.abc`` instead of ``ansible.module_utils.common._collections_compat`` in controller code.
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

- amazon.aws collection - refacterization of code to use argument specification ``fallback`` when falling back to environment variables for security credentials and AWS connection details (https://github.com/ansible-collections/amazon.aws/pull/1174).
- ec2_instance - more consistently return ``instances`` information (https://github.com/ansible-collections/amazon.aws/pull/964).
- ec2_instance - remove unused import (https://github.com/ansible-collections/amazon.aws/pull/1350).
- ec2_key - Add unit-tests coverage (https://github.com/ansible-collections/amazon.aws/pull/1288).
- ec2_spot_instance - add parameter ``terminate_instances`` to support terminate instances associated with spot requests. (https://github.com/ansible-collections/amazon.aws/pull/1402).
- ec2_vpc_nat_gateway - ensure allocation_id is defined before potential access (https://github.com/ansible-collections/amazon.aws/pull/1350).
- rds_instance - Split up the integration test-suite in a series of smaller tests (https://github.com/ansible-collections/amazon.aws/pull/1185).
- rds_instance - add support for gp3 storage type (https://github.com/ansible-collections/amazon.aws/pull/1266).
- route53_health_check -  added support for enabling Latency graphs (MeasureLatency) during creation of a Route53 Health Check. (https://github.com/ansible-collections/amazon.aws/pull/1201).
- route53_zone - added support for associating multiple VPCs to route53 hosted zones (https://github.com/ansible-collections/amazon.aws/pull/1300).
- s3_bucket - add option to support creation of buckets with object lock enabled (https://github.com/ansible-collections/amazon.aws/pull/1372).

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

ansible.windows
~~~~~~~~~~~~~~~

- win_reboot - Display connection messages under 4 v's ``-vvvv`` instead of 3

cisco.aci
~~~~~~~~~

- Add Node Profile BGP Peer and Route Control Profile functionalities to aci_l3out_bgp_peer module (#340)
- Add SVI auto state support (auto_state attribute) to aci_l3out_interface (#348)
- Add aci_aaa_domain, aci_aaa_role and aci_custom_privilege modules (#226)
- Add aci_fabric_pod_policy_group module (#230)
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
- ios_facts - Add ip value to ansible_net_neighbors dictionary for cdp neighbours. (https://github.com/ansible-collections/cisco.ios/pull/748)
- ios_facts - Add ip value to ansible_net_neighbors dictionary for lldp neighbours. (https://github.com/ansible-collections/cisco.ios/pull/760)
- ios_facts - default facts to show operating state data autonomous or controller mode.
- ios_interfaces - Add mode attribute in ios_interfaces, which supports layer2 and layer3 as options.
- ios_l2_interfaces - more options for modes attribute added.
- ios_route_maps - added 32-bit number support (https://github.com/ansible-collections/cisco.ios/pull/692)

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
- ecs_cluster - add support for ``capacity_providers`` and ``capacity_provider_strategy`` features (https://github.com/ansible-collections/community.aws/pull/1640).
- ecs_cluster - append default value to documentation (https://github.com/ansible-collections/community.aws/pull/1636).
- ecs_ecr - add ``encryption_configuration`` option (https://github.com/ansible-collections/community.aws/pull/1623).
- ecs_service - ``task_definition`` is now optional when ``force_new_deployment`` is ``True`` (https://github.com/ansible-collections/community.aws/pull/1680).
- ecs_service - added new parameter ``enable_execute_command`` (https://github.com/ansible-collections/community.aws/pull/488).
- ecs_service - handle SDK errors more cleanly on update failures (https://github.com/ansible-collections/community.aws/pull/488).
- ecs_service - new parameter ``purge_placement_constraints``  to have the ability to remove the placement constraints of an ECS Service (https://github.com/ansible-collections/community.aws/pull/1716).
- ecs_service - new parameter ``purge_placement_strategy`` to have the ability to remove the placement strategy of an ECS Service (https://github.com/ansible-collections/community.aws/pull/1716).
- ecs_service - support load balancer update for existing ECS services (https://github.com/ansible-collections/community.aws/pull/1625).
- elasticache_parameter_group - add ``redis6.x`` group family on the module input choices (https://github.com/ansible-collections/community.aws/pull/1476).
- elb_target_group - add support for ``protocol_version`` parameter (https://github.com/ansible-collections/community.aws/pull/1496).
- iam_role - Drop deprecation warning, because the standard value for purge parameters is ``true`` (https://github.com/ansible-collections/community.aws/pull/1636).
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
- ssm_parameter - fix typo in examples ``paramater`` (https://github.com/ansible-collections/community.aws/issues/1642).

community.crypto
~~~~~~~~~~~~~~~~

- get_certificate - adds ``ciphers`` option for custom cipher selection (https://github.com/ansible-collections/community.crypto/pull/571).
- x509_certificate_info - adds ``issuer_uri`` field in return value based on Authority Information Access data (https://github.com/ansible-collections/community.crypto/pull/530).

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
- dconf - parse GVariants for equality comparison when the Python module ``gi.repository`` is available (https://github.com/ansible-collections/community.general/pull/6049).
- dig lookup plugin - support CAA record type (https://github.com/ansible-collections/community.general/pull/5913).
- dnsimple - set custom User-Agent for API requests to DNSimple (https://github.com/ansible-collections/community.general/pull/5927).
- flatpak_remote - add new boolean option ``enabled``. It controls, whether the remote is enabled or not (https://github.com/ansible-collections/community.general/pull/5926).
- gconftool2 - refactor using ``ModuleHelper`` and ``CmdRunner`` (https://github.com/ansible-collections/community.general/pull/5545).
- gitlab_project - add ``builds_access_level``, ``container_registry_access_level`` and ``forking_access_level`` options (https://github.com/ansible-collections/community.general/pull/5706).
- gitlab_project - add ``releases_access_level``, ``environments_access_level``, ``feature_flags_access_level``, ``infrastructure_access_level``, ``monitor_access_level``, and ``security_and_compliance_access_level`` options (https://github.com/ansible-collections/community.general/pull/5986).
- gitlab_runner - add new boolean option ``access_level_on_creation``. It controls, whether the value of ``access_level`` is used for runner registration or not. The option ``access_level`` has been ignored on registration so far and was only used on updates (https://github.com/ansible-collections/community.general/issues/5907, https://github.com/ansible-collections/community.general/pull/5908).
- gitlab_runner - allow to register group runner (https://github.com/ansible-collections/community.general/pull/3935).
- ilo_redfish_utils module utils - change implementation of DNS Server IP and NTP Server IP update (https://github.com/ansible-collections/community.general/pull/5804).
- ipa_group - allow to add and remove external users with the ``external_user`` option (https://github.com/ansible-collections/community.general/pull/5897).
- iptables_state - minor refactoring within the module (https://github.com/ansible-collections/community.general/pull/5844).
- java_certs - add more detailed error output when extracting certificate from PKCS12 fails (https://github.com/ansible-collections/community.general/pull/5550).
- jc filter plugin - added the ability to use parser plugins (https://github.com/ansible-collections/community.general/pull/6043).
- jenkins_plugin - refactor code to module util to fix sanity check (https://github.com/ansible-collections/community.general/pull/5565).
- jira - add worklog functionality (https://github.com/ansible-collections/community.general/issues/6209, https://github.com/ansible-collections/community.general/pull/6210).
- keycloak_group - add new optional module parameter ``parents`` to properly handle keycloak subgroups (https://github.com/ansible-collections/community.general/pull/5814).
- keycloak_user_federation - make ``org.keycloak.storage.ldap.mappers.LDAPStorageMapper`` the default value for mappers ``providerType`` (https://github.com/ansible-collections/community.general/pull/5863).
- ldap modules - add ``ca_path`` option (https://github.com/ansible-collections/community.general/pull/6185).
- ldap modules - add ``xorder_discovery`` option (https://github.com/ansible-collections/community.general/issues/6045, https://github.com/ansible-collections/community.general/pull/6109).
- lxd_container - add diff and check mode (https://github.com/ansible-collections/community.general/pull/5866).
- lxd_project - refactored code out to module utils to clear sanity check (https://github.com/ansible-collections/community.general/pull/5549).
- make - add ``command`` return value to the module output (https://github.com/ansible-collections/community.general/pull/6160).
- mattermost, rocketchat, slack - replace missing default favicon with docs.ansible.com favicon (https://github.com/ansible-collections/community.general/pull/5928).
- modprobe - add ``persistent`` option (https://github.com/ansible-collections/community.general/issues/4028, https://github.com/ansible-collections/community.general/pull/542).
- nmap inventory plugin - add new option ``open`` for only returning open ports (https://github.com/ansible-collections/community.general/pull/6200).
- nmap inventory plugin - add new option ``port`` for port specific scan (https://github.com/ansible-collections/community.general/pull/6165).
- nmap inventory plugin - add new options ``udp_scan``, ``icmp_timestamp``, and ``dns_resolve`` for different types of scans (https://github.com/ansible-collections/community.general/pull/5566).
- nmcli - add ``default`` and ``default-or-eui64`` to the list of valid choices for ``addr_gen_mode6`` parameter (https://github.com/ansible-collections/community.general/pull/5974).
- nmcli - add support for ``team.runner-fast-rate`` parameter for ``team`` connections (https://github.com/ansible-collections/community.general/issues/6065).
- one_vm - add a new ``updateconf`` option which implements the ``one.vm.updateconf`` API call (https://github.com/ansible-collections/community.general/pull/5812).
- openbsd_pkg - set ``TERM`` to ``'dumb'`` in ``execute_command()`` to make module less dependant on the ``TERM`` environment variable set on the Ansible controller (https://github.com/ansible-collections/community.general/pull/6149).
- opkg - allow installing a package in a certain version (https://github.com/ansible-collections/community.general/pull/5688).
- opkg - refactored module to use ``CmdRunner`` for executing ``opkg`` (https://github.com/ansible-collections/community.general/pull/5718).
- osx_defaults - include stderr in error messages (https://github.com/ansible-collections/community.general/pull/6011).
- pipx - optional ``install_apps`` parameter added to install applications from injected packages (https://github.com/ansible-collections/community.general/pull/6198).
- proxmox - added new module parameter ``tags`` for use with PVE 7+ (https://github.com/ansible-collections/community.general/pull/5714).
- proxmox - suppress urllib3 ``InsecureRequestWarnings`` when ``validate_certs`` option is ``false`` (https://github.com/ansible-collections/community.general/pull/5931).
- proxmox_kvm - add new ``archive`` parameter. This is needed to create a VM from an archive (backup) (https://github.com/ansible-collections/community.general/pull/6159).
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
- slack - add option ``prepend_hash`` which allows to control whether a ``#`` is prepended to ``channel_id``. The current behavior (value ``auto``) is to prepend ``#`` unless some specific prefixes are found. That list of prefixes is incomplete, and there does not seem to exist a documented condition on when exactly ``#`` must not be prepended. We recommend to explicitly set ``prepend_hash=always`` or ``prepend_hash=never`` to avoid any ambiguity (https://github.com/ansible-collections/community.general/pull/5629).
- snap - minor refactor when executing module (https://github.com/ansible-collections/community.general/pull/5773).
- snap_alias - refactored module to use ``CmdRunner`` to execute ``snap`` (https://github.com/ansible-collections/community.general/pull/5486).
- spotinst_aws_elastigroup - add ``elements`` attribute when missing in ``list`` parameters (https://github.com/ansible-collections/community.general/pull/5553).
- ssh_config - add ``host_key_algorithms`` option (https://github.com/ansible-collections/community.general/pull/5605).
- ssh_config - add ``proxyjump`` option (https://github.com/ansible-collections/community.general/pull/5970).
- ssh_config - refactor code to module util to fix sanity check (https://github.com/ansible-collections/community.general/pull/5720).
- ssh_config - vendored StormSSH's config parser to avoid having to install StormSSH to use the module (https://github.com/ansible-collections/community.general/pull/6117).
- sudoers - add ``setenv`` parameters to support passing environment variables via sudo. (https://github.com/ansible-collections/community.general/pull/5883)
- sudoers - adds ``host`` parameter for setting hostname restrictions in sudoers rules (https://github.com/ansible-collections/community.general/issues/5702).
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

- mysql_info - add ``connector_name`` and ``connector_version`` to returned values (https://github.com/ansible-collections/community.mysql/pull/497).
- mysql_role - enable auto_commit to avoid MySQL metadata table lock (https://github.com/ansible-collections/community.mysql/issues/479).
- mysql_user - add plugin_auth_string as optional parameter to use a specific pam service if pam/auth_pam plugin is used (https://github.com/ansible-collections/community.mysql/pull/445).
- mysql_user - add the ``session_vars`` argument to set session variables at the beginning of module execution (https://github.com/ansible-collections/community.mysql/issues/478).
- mysql_user - display a more informative invalid privilege exception. Changes the exception handling of the granting permission logic to show the query executed , params and the exception message granting privileges fails` (https://github.com/ansible-collections/community.mysql/issues/465).
- mysql_user - enable auto_commit to avoid MySQL metadata table lock (https://github.com/ansible-collections/community.mysql/issues/479).
- setup_mysql - update MySQL tarball URL (https://github.com/ansible-collections/community.mysql/pull/491).

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

- win_dns_record - Added support for DHCID (RFC 4701) records
- win_domain_user - Added the ``display_name`` option to set the users display name attribute

community.zabbix
~~~~~~~~~~~~~~~~

- ansible_zabbix_url_path introduced to be able to specify non-default Zabbix WebUI path, e.g. http://<FQDN>/zabbixeu
- collection now supports creating ``module_defaults`` for ``group/community.zabbix.zabbix`` (see https://github.com/ansible-collections/community.zabbix/issues/326)
- fixed ``zabbix_server`` role failure running in check_mode (see https://github.com/ansible-collections/community.zabbix/issues/804)
- httpapi plugin - updated to work with Zabbix 6.4.
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

- ibm_svc_host - Added support for modification of iSCSI host.
- ibm_svc_manage_migraiton - Added support for volume migration across pools.

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
- na_ontap_aggregate - new option ``allow_flexgroups`` added.
- na_ontap_cifs - new options ``access_based_enumeration``, ``change_notify``, ``encryption``, ``home_directory``, ``oplocks``, ``show_snapshot``, ``allow_unencrypted_access``, ``namespace_caching`` and ``continuously_available`` added in REST.
- na_ontap_cifs - new options ``browsable`` and ``show_previous_versions`` added in REST.
- na_ontap_cifs - removed default value for ``unix_symlink`` as its not supported with ZAPI.
- na_ontap_cifs - updated documentation and examples for REST.
- na_ontap_cifs_local_group_member - Added REST API support to retrieve, add and remove CIFS group member.
- na_ontap_cifs_local_group_member - REST support is from ONTAP 9.10.1 or later.
- na_ontap_cifs_server - skip ``service_state`` option if not set in create.
- na_ontap_dns - ``skip_validation`` option requires 9.9.1 or later with REST and ignored for cluster DNS operations.
- na_ontap_dns - support cluster scope for modify and delete.
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
- na_ontap_quotas - for qtree type, allow quota_target in path format /vol/vol_name/qtree_name in REST.
- na_ontap_rest_cli - returns changed only for verbs POST, PATCH and DELETE.
- na_ontap_rest_info - improved documentation for ``parameters`` option.
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
- na_ontap_volume - report error if vserver does not exist or is not a data vserver on create.
- na_ontap_volume_efficiency - REST support for ``policy`` requires 9.7 or later, ``path`` requires 9.9.1 or later and ``volume_efficiency`` and ``start_ve_scan_old_data`` requires 9.11.1 or later.
- na_ontap_volume_efficiency - ``schedule``, ``start_ve_scan_all``, ``start_ve_build_metadata``, ``start_ve_delete_checkpoint``, ``start_ve_queue_operation``, ``start_ve_qos_policy`` and ``stop_ve_all_operations`` options are not supported with REST.
- na_ontap_volume_efficiency - new option ``volume_name`` added.
- na_ontap_volume_efficiency - updated private cli with REST API.

netapp_eseries.santricity
~~~~~~~~~~~~~~~~~~~~~~~~~

- netapp_eseries.santricity.na_santricity_iscsi_interface - Add support of iSCSI HIC speed.
- netapp_eseries.santricity.nar_santricity_host - Add support of iSCSI HIC speed.

netbox.netbox
~~~~~~~~~~~~~

- Add options for NetBox 3.4 [#905](https://github.com/netbox-community/ansible_modules/pull/905)
- nb_inventory - Add serial and asset tag to extracted attributes [#826](https://github.com/netbox-community/ansible_modules/pull/826)
- nb_lookup - Add 3.3 endpoints for lookup [#865](https://github.com/netbox-community/ansible_modules/pull/865)
- netbox_aggregate - Add tenant as parameter to module [#968](https://github.com/netbox-community/ansible_modules/pull/968)
- netbox_asn - Add module [#947](https://github.com/netbox-community/ansible_modules/pull/947)
- netbox_console_server and netbox_console_server_port - Add new field [#866](https://github.com/netbox-community/ansible_modules/pull/866)
- netbox_custom_field - Add group_name [#882](https://github.com/netbox-community/ansible_modules/pull/882)
- netbox_device_bay - Add label [#868](https://github.com/netbox-community/ansible_modules/pull/868)
- netbox_device_type and netbox_device - Add airflow [#907](https://github.com/netbox-community/ansible_modules/pull/907)
- netbox_fhrp_group - Add module [#957](https://github.com/netbox-community/ansible_modules/pull/957)
- netbox_invventory_item_role - Add module [#885](https://github.com/netbox-community/ansible_modules/pull/885)
- netbox_journal_entry - Add module [#961](https://github.com/netbox-community/ansible_modules/pull/961)
- netbox_l2vpn - Add module [#846](https://github.com/netbox-community/ansible_modules/pull/846)
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

- purefa_host - Add support for VLAN ID tagging for a host (Requires Purity//FA 6.3.5)
- purefa_info - Add new subset alerts
- purefa_info - Added default protection information to `config` section
- purefa_network - Added support for NVMe-RoCE and NVMe-TCP service types
- purefa_network - Added support for servicelist updates
- purefa_user - Added Ops Admin role to choices
- purefa_vlan - Added support for NVMe-TCP service type
- purefa_vlan - Extend VLAN support to cover NVMe-RoCE and file interfaces
- purefa_volume - Added support for volume promotion/demotion

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

ansible.netcommon
~~~~~~~~~~~~~~~~~

- NetworkConnectionBase now inherits from PersistentConnectionBase in ansible.utils. As a result, the minimum ansible.utils version has increased to 2.7.0.
- NetworkTemplate is no longer importable from ansible_collections.ansible.netcommon.plugins.module_utils.network.common and should now be found at its proper location ansible_collections.ansible.netcommon.plugins.module_utils.network.common.rm_base.network_template
- ResourceModule is no longer importable from ansible_collections.ansible.netcommon.plugins.module_utils.network.common and should now be found at its proper location ansible_collections.ansible.netcommon.plugins.module_utils.network.common.rm_base.resource_module
- VALID_MASKS, is_masklen, is_netmask, to_bits, to_ipv6_network, to_masklen, to_netmask, and to_subnet are no longer importable from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils and should now be found at their proper location ansible.module_utils.common.network

community.general
~~~~~~~~~~~~~~~~~

- ModuleHelper module utils - when the module sets output variables named ``msg``, ``exception``, ``output``, ``vars``, or ``changed``, the actual output will prefix those names with ``_`` (underscore symbol) only when they clash with output variables generated by ModuleHelper itself, which only occurs when handling exceptions. Please note that this breaking change does not require a new major release since before this release, it was not possible to add such variables to the output `due to a bug <https://github.com/ansible-collections/community.general/pull/5755>`__ (https://github.com/ansible-collections/community.general/pull/5765).

hetzner.hcloud
~~~~~~~~~~~~~~

- inventory plugin - Python v3.5+ is now required.

Deprecated Features
-------------------

- The cisco.nso collection is considered unmaintained and will be removed from Ansible 9 if no one starts maintaining it again before Ansible 9. See `the removal process for details on how this works <https://github.com/ansible-collections/overview/blob/main/removal_from_ansible.rst#cancelling-removal-of-an-unmaintained-collection>`__ (https://github.com/ansible-community/community-topics/issues/155).
- The community.fortios collection is considered unmaintained and will be removed from Ansible 9 if no one starts maintaining it again before Ansible 9. See `the removal process for details on how this works <https://github.com/ansible-collections/overview/blob/main/removal_from_ansible.rst#cancelling-removal-of-an-unmaintained-collection>`__ (https://github.com/ansible-community/community-topics/issues/162).
- The community.google collection is considered unmaintained and will be removed from Ansible 9 if no one starts maintaining it again before Ansible 9. See `the removal process for details on how this works <https://github.com/ansible-collections/overview/blob/main/removal_from_ansible.rst#cancelling-removal-of-an-unmaintained-collection>`__ (https://github.com/ansible-community/community-topics/issues/160).
- The community.skydive collection is considered unmaintained and will be removed from Ansible 9 if no one starts maintaining it again before Ansible 9. See `the removal process for details on how this works <https://github.com/ansible-collections/overview/blob/main/removal_from_ansible.rst#cancelling-removal-of-an-unmaintained-collection>`__ (https://github.com/ansible-community/community-topics/issues/171).

Ansible-core
~~~~~~~~~~~~

- The ``ConnectionBase()._new_stdin`` attribute is deprecated, use ``display.prompt_until(msg)`` instead.
- ansible-test - The ``foreman`` test plugin is now deprecated. It will be removed in a future release.
- ansible-test - The ``govcsim`` simulator in the ``vcenter`` test plugin is now deprecated. It will be removed in a future release. Users should switch to providing their own test environment through a static configuration file.
- password_hash - deprecate using passlib.hash.hashtype if hashtype isn't in the list of documented choices.
- vars - Specifying a list of dictionaries for ``vars:`` is deprecated in favor of specifying a dictionary.

amazon.aws
~~~~~~~~~~

- support for passing both profile and security tokens through a mix of environment variables and parameters has been deprecated and support will be removed in release 6.0.0. After release 6.0.0 it will only be possible to pass either a profile or security tokens, regardless of mechanism used to pass them.  To explicitly block a parameter coming from an environment variable pass an empty string as the parameter value.  Support for passing profile and security tokens together was originally deprecated in release 1.2.0, however only partially implemented in release 5.0.0 (https://github.com/ansible-collections/amazon.aws/pull/1355).

chocolatey.chocolatey
~~~~~~~~~~~~~~~~~~~~~

- win_chocolatey - Deprecate side-by-side installs.

cisco.ios
~~~~~~~~~

- ios_bgp_address_family - deprecate neighbors.address/tag/ipv6_adddress with neighbor_address which enables common attributes for facts rendering
- ios_bgp_address_family - deprecate neighbors.password with password_options which allows encryption and password
- ios_bgp_address_family - deprecate slow_peer with slow_peer_options which supports a dict attribute

community.aws
~~~~~~~~~~~~~

- ecs_service -  In a release after 2024-06-01, tha default value of ``purge_placement_constraints`` will be change from ``false`` to ``true`` (https://github.com/ansible-collections/community.aws/pull/1716).
- ecs_service -  In a release after 2024-06-01, tha default value of ``purge_placement_strategy`` will be change from ``false`` to ``true`` (https://github.com/ansible-collections/community.aws/pull/1716).
- iam_role - All top level return values other than ``iam_role`` and ``changed`` have been deprecated and will be removed in a release after 2023-12-01 (https://github.com/ansible-collections/community.aws/issues/551).
- iam_role - In a release after 2023-12-01 the contents of ``assume_role_policy_document`` will no longer be converted from CamelCase to snake_case.  The ``assume_role_policy_document_raw`` return value already returns the policy document in this future format (https://github.com/ansible-collections/community.aws/issues/551).
- iam_role_info - In a release after 2023-12-01 the contents of ``assume_role_policy_document`` will no longer be converted from CamelCase to snake_case.  The ``assume_role_policy_document_raw`` return value already returns the policy document in this future format (https://github.com/ansible-collections/community.aws/issues/551).

community.dns
~~~~~~~~~~~~~

- The default of the newly added option ``txt_character_encoding`` will change from ``octal`` to ``decimal`` in community.dns 3.0.0. The new default will be compatible with `RFC 1035 <https://www.ietf.org/rfc/rfc1035.txt>`__ (https://github.com/ansible-collections/community.dns/pull/134).

community.general
~~~~~~~~~~~~~~~~~

- The ``sap`` modules ``sapcar_extract``, ``sap_task_list_execute``, and ``hana_query``, will be removed from this collection in community.general 7.0.0 and replaced with redirects to ``community.sap_libs``. If you want to continue using these modules, make sure to also install ``community.sap_libs`` (it is part of the Ansible package) (https://github.com/ansible-collections/community.general/pull/5614).
- consul - deprecate using parameters unused for ``state=absent`` (https://github.com/ansible-collections/community.general/pull/5772).
- gitlab_runner - the default of the new option ``access_level_on_creation`` will change from ``false`` to ``true`` in community.general 7.0.0. This will cause ``access_level`` to be used during runner registration as well, and not only during updates (https://github.com/ansible-collections/community.general/pull/5908).
- gitlab_runner - the option ``access_level`` will lose its default value in community.general 8.0.0. From that version on, you have set this option to ``ref_protected`` explicitly, if you want to have a protected runner (https://github.com/ansible-collections/community.general/issues/5925).
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

ansible.netcommon
~~~~~~~~~~~~~~~~~

- cli_parse - This plugin was moved to ansible.utils in version 1.0.0, and the redirect to that collection has now been removed.

Bugfixes
--------

Ansible-core
~~~~~~~~~~~~

- Ansible.Basic.cs - Ignore compiler warning (reported as an error) when running under PowerShell 7.3.x.
- AnsibleModule.run_command - Only use selectors when needed, and rely on Python stdlib subprocess for the simple task of collecting stdout/stderr when prompt matching is not required.
- BSD network facts - Do not assume column indexes, look for ``netmask`` and ``broadcast`` for determining the correct columns when parsing ``inet`` line (https://github.com/ansible/ansible/issues/79117)
- Correctly count rescued tasks in play recap (https://github.com/ansible/ansible/issues/79711)
- Do not crash when templating an expression with a test or filter that is not a valid Ansible filter name (https://github.com/ansible/ansible/issues/78912, https://github.com/ansible/ansible/pull/78913).
- Fix ``MANIFEST.in`` to exclude unwanted files in the ``packaging/`` directory.
- Fix ``MANIFEST.in`` to include ``*.md`` files in the ``test/support/`` directory.
- Fix a traceback occuring when a task is named ``meta`` (https://github.com/ansible/ansible/issues/79459)
- Fix an issue where the value of ``become`` was ignored when used on a role used as a dependency in ``main/meta.yml`` (https://github.com/ansible/ansible/issues/79777)
- Fix bug in `vars` applied to roles, they were being incorrectly exported among others while only vars/main.yml was meant to be. Also adjusted the precedence to act the same as inline params.
- Fix conditionally notifying ``include_tasks` handlers when ``force_handlers`` is used (https://github.com/ansible/ansible/issues/79776)
- Fix reusing a connection in a task loop that uses a redirected or aliased name - https://github.com/ansible/ansible/issues/78425
- Fix setting become activation in a task loop - https://github.com/ansible/ansible/issues/78425
- Fix traceback when using the ``template`` module and running with ``ANSIBLE_DEBUG=1`` (https://github.com/ansible/ansible/issues/79763)
- Fix using ``GALAXY_IGNORE_CERTS`` in conjunction with collections in requirements files which specify a specific ``source`` that isn't in the configured servers.
- Fix using ``GALAXY_IGNORE_CERTS`` when downloading tarballs from Galaxy servers (https://github.com/ansible/ansible/issues/79557).
- Fixes leftover _valid_attrs usage.
- Fixes the password lookup to not rewrite files if they are not changed when using the "encrypt" parameter (#79430).
- Module and role argument validation - include the valid suboption choices in the error when an invalid suboption is provided.
- Perform type check on data passed to Display.display to enforce the requirement of being given a python3 unicode string
- TaskExecutor - don't ignore templated _raw_params that k=v parser failed to parse (https://github.com/ansible/ansible/issues/79862)
- Windows - Display a warning if the module failed to cleanup any temporary files rather than failing the task. The warning contains a brief description of what failed to be deleted.
- Windows - Ensure the module temp directory contains more unique values to avoid conflicts with concurrent runs - https://github.com/ansible/ansible/issues/80294
- Windows - Improve temporary file cleanup used by modules. Will use a more reliable delete operation on Windows Server 2016 and newer to delete files that might still be open by other software like Anti Virus scanners. There are still scenarios where a file or directory cannot be deleted but the new method should work in more scenarios.
- ``ansible-galaxy search rolename`` - give a warning instead of non-zero return code when search results are empty. This is similar to the behavior when listing roles, which gives a warning if a role cannot be found and exits with a return code of ``0``.
- ``ansible_eval_concat`` - avoid redundant unsafe wrapping of templated strings converted to Python types
- ansible-config limit shorthand format to assigned values
- ansible-doc - stop generating wrong module URLs for module see-alsos. The URLs for modules in ansible.builtin do now work, and URLs for modules outside ansible.builtin are no longer added (https://github.com/ansible/ansible/pull/80280).
- ansible-doc now will correctly display short descriptions on listing filters/tests no matter the directory sorting.
- ansible-galaxy - Improve retries for collection installs, to properly retry, and extend retry logic to common URL related connection errors (https://github.com/ansible/ansible/issues/80170 https://github.com/ansible/ansible/issues/80174)
- ansible-galaxy - fix installing collections in git repositories/directories which contain a MANIFEST.json file (https://github.com/ansible/ansible/issues/79796).
- ansible-galaxy - make initial call to Galaxy server on-demand only when installing, getting info about, and listing roles.
- ansible-galaxy - reduce API calls to servers by fetching signatures only for final candidates.
- ansible-galaxy collection install - respect symlinks when installing from source or local repository (https://github.com/ansible/ansible/issues/78442)
- ansible-galaxy collection/role init - preserve symlinks (https://github.com/ansible/ansible/issues/39334).
- ansible-galaxy role info - fix unhandled AttributeError by catching the correct exception.
- ansible-inventory will no longer duplicate host entries if they were part of a group's childrens tree.
- ansible-inventory will not explicitly sort groups/hosts anymore, giving a chance (depending on output format) to match the order in the input sources.
- ansible-playbook -K breaks when passwords have quotes (https://github.com/ansible/ansible/issues/79836).
- ansible-test - Add ``wheel < 0.38.0`` constraint for Python 3.6 and earlier.
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
- ansible-test - Update the ``pylint`` sanity test requirements to resolve crashes on Python 3.11. (https://github.com/ansible/ansible/issues/78882)
- ansible-test - Update the ``pylint`` sanity test to use version 2.15.4.
- ansible-test - Update the ``pylint`` sanity test to use version 2.15.5.
- ansible-test - Use consistent file permissions when delegating tests to a container or remote host. Files with any execute bit set will use permissions ``755``. All other files will use permissions ``644``. (Resolves issue https://github.com/ansible/ansible/issues/75079)
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
- dnf5 - fix module and package names in the message following failed module respawn attempt
- dnf5 - use the logs API to determine transaction problems
- file - touch action in check mode was always returning ok. Fix now evaluates the different conditions and returns the appropriate changed status. (https://github.com/ansible/ansible/issues/79360)
- file lookup now handles missing files more gracefully.
- file lookup now plays nice with generic lookup ``errors`` option.
- get_url - Ensure we are passing ciphers to all url_get calls (https://github.com/ansible/ansible/issues/79717)
- get_url module - Added a documentation reference to ``hashlib`` regarding algorithms, as well as a note about ``md5`` support on systems running in FIPS compliant mode.
- get_url module - Removed out-of-date documentation stating that ``hashlib`` is a third-party library.
- handlers - fix an issue where the ``flush_handlers`` meta task could not be used with FQCN: ``ansible.builtin.meta`` (https://github.com/ansible/ansible/issues/79023)
- include_role - Inherit from role parents beyond a depth of 3 (https://github.com/ansible/ansible/issues/47023).
- jinja2_native - fix intermittent 'could not find job' failures when a value of ``ansible_job_id`` from a result of an async task was inadvertently changed during execution; to prevent this a format of ``ansible_job_id`` was changed.
- jinja2_native: preserve quotes in strings (https://github.com/ansible/ansible/issues/79083)
- keyword inheritance - Ensure that we do not squash keywords in validate (https://github.com/ansible/ansible/issues/79021)
- known_hosts - do not return changed status when a non-existing key is removed (https://github.com/ansible/ansible/issues/78598)
- list-tags now shows the 'never' tag, which was being excluded by default. To list all tasks you still need to add `--list-tasks --tags never,all`.
- loops/delegate_to - Do not double calculate the values of loops and ``delegate_to`` (https://github.com/ansible/ansible/issues/80038)
- module_utils/basic.py - Fix detection of available hashing algorithms on Python 3.x. All supported algorithms are now available instead of being limited to a hard-coded list. This affects modules such as ``get_url`` which accept an arbitrary checksum algorithm.
- normal action plugin - remove obsolete ``if`` (https://github.com/ansible/ansible/pull/79690).
- omit on keywords was resetting to default value, ignoring inheritance.
- paramiko - Add a new option to allow paramiko >= 2.9 to easily work with all devices now that rsa-sha2 support was added to paramiko, which prevented communication with numerous platforms. (https://github.com/ansible/ansible/issues/76737)
- paramiko - Add back support for ``ssh_args``, ``ssh_common_args``, and ``ssh_extra_args`` for parsing the ``ProxyCommand`` (https://github.com/ansible/ansible/issues/78750)
- paramiko connection was still using outdated playcontext, this should bring it up to date to use the 'correct' data for each task/loop.
- password lookup now correctly reads stored ident fields.
- password_hash - handle errors using unknown passlib hashtypes more gracefully (https://github.com/ansible/ansible/issues/45392).
- plugin loader, fix detection for existing configuration before initializing for a plugin
- role deduplication - Always create new role object, regardless of deduplication. Deduplication will only affect whether a duplicate call to a role will execute, as opposed to re-using the same object. (https://github.com/ansible/ansible/pull/78661)
- roles - Fix templating ``public``, ``allow_duplicates`` and ``rolespec_validate`` (https://github.com/ansible/ansible/issues/80304).
- service_facts - Use python re to parse service output instead of grep (https://github.com/ansible/ansible/issues/78541)
- strategy plugins now correctly identify bad registered variables, even on skip.
- strategy plugins: get the correctly templated and validated run_once value on strategy linear (https://github.com/ansible/ansible/issues/78492)
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

- aws_rds - fixes bug in RDS inventory plugin where config file was ignored (https://github.com/ansible-collections/amazon.aws/issues/1304).
- cloudtrail - support to disabling encryption using ``kms_key_id`` (https://github.com/ansible-collections/amazon.aws/pull/1384).
- ec2_key - fix issue when trying to update existing key pair with the same key material (https://github.com/ansible-collections/amazon.aws/pull/1383).
- ec2_metadata_facts - fix ``AttributeError`` when running the ec2_metadata_facts module on Python 2 managed nodes (https://github.com/ansible-collections/amazon.aws/issues/1358).
- ec2_vol - handle ec2_vol.tags when the associated instance already exists (https://github.com/ansible-collections/amazon.aws/pull/1071).
- lambda - fix flaky integration test which assumes there are no other lambdas in the account (https://github.com/ansible-collections/amazon.aws/issues/1277)
- module_utils/elbv2 - fix change detection by adding default values for ``Scope`` and ``SessionTimeout`` parameters in ``authenticate-oidc`` rules (https://github.com/ansible-collections/amazon.aws/pull/1270).
- module_utils/elbv2 - respect ``UseExistingClientSecret`` parameter in ``authenticate-oidc`` rules (https://github.com/ansible-collections/amazon.aws/pull/1270).
- rds_instance - Fixed ``TypeError`` when tagging RDS DB with storage type ``gp3`` (https://github.com/ansible-collections/amazon.aws/pull/1437).
- revert breaking change introduced in 5.2.0 when passing credentials through a mix of environment variables and parameters (https://github.com/ansible-collections/amazon.aws/issues/1353).
- route53_info - Add new return key ``health_check_observations`` for health check operations (https://github.com/ansible-collections/amazon.aws/pull/1419).
- route53_info - Fixed ``Key Error`` when getting status or failure_reason of a health check (https://github.com/ansible-collections/amazon.aws/pull/1419).
- s3_bucket - empty bucket policy was throwing a JSONDecodeError - deal with it gracefully instead (https://github.com/ansible-collections/amazon.aws/pull/1368)

ansible.netcommon
~~~~~~~~~~~~~~~~~

- Cast AnsibleUnsafeText to str in convert_doc_to_ansible_module_kwargs() to keep CSafeLoader happy. This fixes issues with content scaffolding tools.
- httpapi - ``send()`` method no longer applied leftover kwargs to ``open_url()``. Fix applies those arguments as intended (https://github.com/ansible-collections/ansible.netcommon/pull/524).
- network_cli - network cli connection avoids traceback when using invalid user
- network_cli - when receiving longer responses with libssh, parts of the response were sometimes repeated. The response is now returned as it is received (https://github.com/ansible-collections/community.routeros/issues/132).
- network_resource - fix a potential UnboundLocalError if the module fails to import a Resource Module. (https://github.com/ansible-collections/ansible.netcommon/pull/513)
- restconf - creation of new resources is no longer erroneously forced to use POST. (https://github.com/ansible-collections/ansible.netcommon/issues/502)

ansible.posix
~~~~~~~~~~~~~

- Fixed a bug where firewalld module fails to create/remove zones when the daemon is stopped
- Removed contentious terminology to match reference documentation in profile_tasks.
- firewall - Fixed to output a more complete missing library message.
- rhel_facts - Call exit_json with all keyword arguments
- synchronize - Fixed hosts involved in rsync require the same password

ansible.utils
~~~~~~~~~~~~~

- Accept int input for ipaddr filters.
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
- ios_bgp_address_family - fix path_attribute to support float parameter
- ios_bgp_global - fix neighbor shutdown command on set value being false.
- ios_command - Run & evaluate commands at least once even when retries is set to 0 (https://github.com/ansible-collections/cisco.nxos/issues/607).
- ios_l2_interfaces - fix command to remove allowed_vlans and pruning_vlans from configuration.
- ios_l2_interfaces - fix dynamic option for mode attribute.
- ios_l2_interfaces - fix state operation for existing vlans.
- ios_l3_interfaces - fix command generation on attribute value being false.
- ios_lag_interfaces - fix deleted state to delete only sub attribute values.
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

- Fix MSO HTTPAPI plugin login domain issue (#317)
- Fix datetime support for python2.7 in mso_backup_schedule (#323)
- Fix deploymentImmediacy key inconsistency in the API used by mso_schema_site_anp and mso_schema_site_anp_epg (#283)
- Fix idempotency for mso_schema_site_bd_l3out
- Fix mso_schema_template_bd issue when created with unicast_routing as false (#278)
- Fix to be able to add multiple filter and filters with "-" in their names (#306)

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
- ec2_snapshot_copy - including tags caused the erorr "Tag specification resource type must have a value". Fix sets the ResourceType to snapshot to resolve this issue (https://github.com/ansible-collections/community.aws/pull/1419).
- ecs_ecr - fix a ``RepositoryNotFound`` exception when trying to create repositories in check mode (https://github.com/ansible-collections/community.aws/pull/1550).
- ecs_service - respect ``placement_constraints`` for existing ECS services (https://github.com/ansible-collections/community.aws/pull/1601).
- eks_cluster - adding tags to eks cluster creation (https://github.com/ansible-collections/community.aws/pull/1591).
- opensearch - Fix cluster creation when using advanced security options (https://github.com/ansible-collections/community.aws/pull/1613).
- s3_lifecycle - module no longer calls ``put_lifecycle_configuration`` if there is no change (https://github.com/ansible-collections/community.aws/issues/1624).
- sns_topic - avoid fetching attributes from subscribers when not setting them, this can cause permissions issues (https://github.com/ansible-collections/community.aws/pull/1418).
- ssm_parameter - fix a ``KeyError`` when adding a description to an existing parameter (https://github.com/ansible-collections/community.aws/issues/1471).

community.crypto
~~~~~~~~~~~~~~~~

- action plugin helper - fix handling of deprecations for ansible-core 2.14.2 (https://github.com/ansible-collections/community.crypto/pull/572).
- execution environment binary dependencies (bindep.txt) - fix ``python3-pyOpenSSL`` dependency resolution on RHEL 9+ / CentOS Stream 9+ platforms (https://github.com/ansible-collections/community.crypto/pull/575).
- openssl_csr, openssl_csr_pipe - prevent invalid values for ``crl_distribution_points`` that do not have one of ``full_name``, ``relative_name``, and ``crl_issuer`` (https://github.com/ansible-collections/community.crypto/pull/560).
- openssl_publickey_info - do not crash with internal error when public key cannot be parsed (https://github.com/ansible-collections/community.crypto/pull/551).
- various plugins - remove unnecessary imports (https://github.com/ansible-collections/community.crypto/pull/569).

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
- various plugins and modules - remove unnecessary imports (https://github.com/ansible-collections/community.docker/pull/574).
- vendored latest Docker SDK for Python bugfix (https://github.com/ansible-collections/community.docker/pull/513, https://github.com/docker/docker-py/issues/3045).

community.general
~~~~~~~~~~~~~~~~~

- ModuleHelper - fix bug when adjusting the name of reserved output variables (https://github.com/ansible-collections/community.general/pull/5755).
- alternatives - support subcommands on Fedora 37, which uses ``follower`` instead of ``slave`` (https://github.com/ansible-collections/community.general/pull/5794).
- ansible_galaxy_install - set default to raise exception if command's return code is different from zero (https://github.com/ansible-collections/community.general/pull/5680).
- ansible_galaxy_install - try ``C.UTF-8`` and then fall back to ``en_US.UTF-8`` before failing (https://github.com/ansible-collections/community.general/pull/5680).
- archive - avoid deprecated exception class on Python 3 (https://github.com/ansible-collections/community.general/pull/6180).
- bitwarden lookup plugin - clarify what to do, if the bitwarden vault is not unlocked (https://github.com/ansible-collections/community.general/pull/5811).
- cartesian and flattened lookup plugins - adjust to parameter deprecation in ansible-core 2.14's ``listify_lookup_plugin_terms`` helper function (https://github.com/ansible-collections/community.general/pull/6074).
- chroot connection plugin - add ``inventory_hostname`` to vars under ``remote_addr``. This is needed for compatibility with ansible-core 2.13 (https://github.com/ansible-collections/community.general/pull/5570).
- cloudflare_dns - fixed the idempotency for SRV DNS records (https://github.com/ansible-collections/community.general/pull/5972).
- cloudflare_dns - fixed the possiblity of setting a root-level SRV DNS record (https://github.com/ansible-collections/community.general/pull/5972).
- cmd_runner module utils - fixed bug when handling default cases in ``cmd_runner_fmt.as_map()`` (https://github.com/ansible-collections/community.general/pull/5538).
- cmd_runner module utils - formatting arguments ``cmd_runner_fmt.as_fixed()`` was expecting an non-existing argument (https://github.com/ansible-collections/community.general/pull/5538).
- dig lookup plugin - correctly handle DNSKEY record type's ``algorithm`` field (https://github.com/ansible-collections/community.general/pull/5914).
- gem - fix force parameter not being passed to gem command when uninstalling (https://github.com/ansible-collections/community.general/pull/5822).
- gem - fix hang due to interactive prompt for confirmation on specific version uninstall (https://github.com/ansible-collections/community.general/pull/5751).
- github_webhook - fix always changed state when no secret is provided (https://github.com/ansible-collections/community.general/pull/5994).
- gitlab_deploy_key - also update ``title`` and not just ``can_push`` (https://github.com/ansible-collections/community.general/pull/5888).
- gitlab_group_variables - fix dropping variables accidentally when GitLab introduced new properties (https://github.com/ansible-collections/community.general/pull/5667).
- gitlab_project_variables - fix dropping variables accidentally when GitLab introduced new properties (https://github.com/ansible-collections/community.general/pull/5667).
- gitlab_runner - fix ``KeyError`` on runner creation and update (https://github.com/ansible-collections/community.general/issues/6112).
- influxdb_user - fix running in check mode when the user does not exist yet (https://github.com/ansible-collections/community.general/pull/6111).
- interfaces_file - fix reading options in lines not starting with a space (https://github.com/ansible-collections/community.general/issues/6120).
- jail connection plugin - add ``inventory_hostname`` to vars under ``remote_addr``. This is needed for compatibility with ansible-core 2.13 (https://github.com/ansible-collections/community.general/pull/6118).
- jenkins_plugin - fix error due to undefined variable when updates file is not downloaded (https://github.com/ansible-collections/community.general/pull/6100).
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
- nmcli - fix change handling of values specified as an integer 0 (https://github.com/ansible-collections/community.general/pull/5431).
- nmcli - fix failure to handle WIFI settings when connection type not specified (https://github.com/ansible-collections/community.general/pull/5431).
- nmcli - fix improper detection of changes to ``wifi.wake-on-wlan`` (https://github.com/ansible-collections/community.general/pull/5431).
- nmcli - fixed idempotency issue for bridge connections. Module forced default value of ``bridge.priority`` to nmcli if not set; if ``bridge.stp`` is disabled nmcli ignores it and keep default (https://github.com/ansible-collections/community.general/issues/3216, https://github.com/ansible-collections/community.general/issues/4683).
- nmcli - fixed idempotency issue when module params is set to ``may_fail4=false`` and ``method4=disabled``; in this case nmcli ignores change and keeps their own default value ``yes`` (https://github.com/ansible-collections/community.general/pull/6106).
- nmcli - implemented changing mtu value on vlan interfaces (https://github.com/ansible-collections/community.general/issues/4387).
- nmcli - order is significant for lists of addresses (https://github.com/ansible-collections/community.general/pull/6048).
- nsupdate - fix zone lookup. The SOA record for an existing zone is returned as an answer RR and not as an authority RR (https://github.com/ansible-collections/community.general/issues/5817, https://github.com/ansible-collections/community.general/pull/5818).
- onepassword lookup plugin - Changed to ignore errors from "op account get" calls. Previously, errors would prevent auto-signin code from executing (https://github.com/ansible-collections/community.general/pull/5942).
- opkg - fix issue that ``force=reinstall`` would not reinstall an existing package (https://github.com/ansible-collections/community.general/pull/5705).
- opkg - fixes bug when using ``update_cache=true`` (https://github.com/ansible-collections/community.general/issues/6004).
- proxmox inventory plugin - fix bug while templating when using templates for the ``url``, ``user``, ``password``, ``token_id``, or ``token_secret`` options (https://github.com/ansible-collections/community.general/pull/5640).
- proxmox inventory plugin - handle tags delimited by semicolon instead of comma, which happens from Proxmox 7.3 on (https://github.com/ansible-collections/community.general/pull/5602).
- proxmox_disk - fixed issue with read timeout on import action (https://github.com/ansible-collections/community.general/pull/5803).
- proxmox_disk - fixed possible issues with redundant ``vmid`` parameter (https://github.com/ansible-collections/community.general/issues/5492, https://github.com/ansible-collections/community.general/pull/5672).
- proxmox_nic - fixed possible issues with redundant ``vmid`` parameter (https://github.com/ansible-collections/community.general/issues/5492, https://github.com/ansible-collections/community.general/pull/5672).
- redfish_utils - removed basic auth HTTP header when performing a GET on the service root resource and when performing a POST to the session collection (https://github.com/ansible-collections/community.general/issues/5886).
- redhat_subscription - do not ignore ``consumer_name`` and other variables if ``activationkey`` is specified (https://github.com/ansible-collections/community.general/issues/3486, https://github.com/ansible-collections/community.general/pull/5627).
- redhat_subscription - do not pass arguments to ``subscription-manager register`` for things already configured; now a specified ``rhsm_baseurl`` is properly set for subscription-manager (https://github.com/ansible-collections/community.general/pull/5583).
- redhat_subscription, rhsm_release, rhsm_repository - cleanly fail when not running as root, rather than hanging on an interactive ``console-helper`` prompt; they all interact with ``subscription-manager``, which already requires to be run as root (https://github.com/ansible-collections/community.general/issues/734, https://github.com/ansible-collections/community.general/pull/6211).
- splunk callback plugin - adjust type of callback to ``notification``, it was incorrectly classified as ``aggregate`` before (https://github.com/ansible-collections/community.general/pull/5761).
- sumologic callback plugin - adjust type of callback to ``notification``, it was incorrectly classified as ``aggregate`` before (https://github.com/ansible-collections/community.general/pull/5761).
- syslog_json callback plugin - adjust type of callback to ``notification``, it was incorrectly classified as ``aggregate`` before (https://github.com/ansible-collections/community.general/pull/5761).
- terraform - fix ``current`` workspace never getting appended to the ``all`` key in the ``workspace_ctf`` object (https://github.com/ansible-collections/community.general/pull/5735).
- terraform - fix ``terraform init`` failure when there are multiple workspaces on the remote backend and when ``default`` workspace is missing by setting ``TF_WORKSPACE`` environmental variable to the value of ``workspace`` when used (https://github.com/ansible-collections/community.general/pull/5735).
- terraform and timezone - slight refactoring to avoid linter reporting potentially undefined variables (https://github.com/ansible-collections/community.general/pull/5933).
- terraform module - disable ANSI escape sequences during validation phase (https://github.com/ansible-collections/community.general/pull/5843).
- unixy callback plugin - fix plugin to work with ansible-core 2.14 by using Ansible's configuration manager for handling options (https://github.com/ansible-collections/community.general/issues/5600).
- unixy callback plugin - fix typo introduced when updating to use Ansible's configuration manager for handling options (https://github.com/ansible-collections/community.general/issues/5600).
- various plugins and modules - remove unnecessary imports (https://github.com/ansible-collections/community.general/pull/5940).
- vdo - now uses ``yaml.safe_load()`` to parse command output instead of the deprecated ``yaml.load()`` which is potentially unsafe. Using ``yaml.load()`` without explicitely setting a ``Loader=`` is also an error in pyYAML 6.0 (https://github.com/ansible-collections/community.general/pull/5632).
- vmadm - fix for index out of range error in ``get_vm_uuid`` (https://github.com/ansible-collections/community.general/pull/5628).
- xenorchestra inventory plugin - fix failure to receive objects from server due to not checking the id of the response (https://github.com/ansible-collections/community.general/pull/6227).
- xml - fixed a bug where empty ``children`` list would not be set (https://github.com/ansible-collections/community.general/pull/5808).
- yarn - fix ``global=true`` to check for the configured global folder instead of assuming the default (https://github.com/ansible-collections/community.general/pull/5829)
- yarn - fix ``global=true`` to not fail when `executable` wasn't specified (https://github.com/ansible-collections/community.general/pull/6132)
- yarn - fix ``state=absent`` not working with ``global=true`` when the package does not include a binary (https://github.com/ansible-collections/community.general/pull/5829)
- yarn - fix ``state=latest`` not working with ``global=true`` (https://github.com/ansible-collections/community.general/issues/5712).
- yarn - fixes bug where yarn module tasks would fail when warnings were emitted from Yarn. The ``yarn.list`` method was not filtering out warnings (https://github.com/ansible-collections/community.general/issues/6127).
- zfs_delegate_admin - zfs allow output can now be parsed when uids/gids are not known to the host system (https://github.com/ansible-collections/community.general/pull/5943).
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

- mysql_user - when revoke privs consists only of ``GRANT``, a 2nd revoke query is executed with empty privs to revoke that ended in an SQL exception (https://github.com/ansible-collections/community.mysql/pull/503).
- mysql_variables - add uppercase character pattern to regex to allow GLOBAL variables containing uppercase characters. This recognizes variable names used in Galera, for example, ``wsrep_OSU_method``, which breaks the normal pattern of all lowercase characters (https://github.com/ansible-collections/community.mysql/pull/501).

community.okd
~~~~~~~~~~~~~

- openshift_adm_groups_sync - initialize OpenshiftGroupSync attributes early to avoid Attribute error (https://github.com/openshift/community.okd/issues/155).
- openshift_auth - Review the way the discard process is working, add openshift algorithm to convert token to resource object name (https://github.com/openshift/community.okd/issues/176).

community.postgresql
~~~~~~~~~~~~~~~~~~~~

- postgresql_pg_hba - fix ``changed`` return value for when ``overwrite`` is enabled (https://github.com/ansible-collections/community.postgresql/pull/378).
- postgresql_privs - fails with ``type=default_privs``, ``privs=ALL``, ``objs=ALL_DEFAULT`` (https://github.com/ansible-collections/community.postgresql/issues/373).
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

community.windows
~~~~~~~~~~~~~~~~~

- win_firewall_rule - fix problem in check mode with multiple ip addresses not in same order
- win_partition - fix problem in auto assigning a drive letter should the user use either a, u, t or o as a drive letter

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

junipernetworks.junos
~~~~~~~~~~~~~~~~~~~~~

- enable provider support for junos_scp and junos_package.
- fix diff to result when prepared diff exists.
- fix junos_security_zones facts gathering when we have single interface configured.
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
- na_ontap_file_directory_policy - updated doc with deprecation warning as it is a ZAPI only module.
- na_ontap_file_security_permissions - error if more than one desired ACLs has same user, access, access_control and apply_to.
- na_ontap_file_security_permissions - fix TypeError when current acls is None.
- na_ontap_file_security_permissions - fix idempotency issue on ``acls.propagation_mode`` option.
- na_ontap_file_security_permissions - updated notes to indicate ONTAP 9.9.1 or later is required.
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
- na_ontap_qtree - fix cannot get current qtree if enclosed in curly braces.
- na_ontap_qtree - ignore job entry does not exist error when creating qtree with REST to bypass ONTAP issue with FSx.
- na_ontap_quota_policy - updated doc with deprecation warning as it is a ZAPI only module.
- na_ontap_quotas - fix default tree quota rule gets modified when ``quota_target`` is set in REST.
- na_ontap_quotas - fix duplicate entry error when trying to add quota rule in REST.
- na_ontap_quotas - fix entry does not exist error when trying to modify quota status in REST.
- na_ontap_quotas - fix user/group quota rule without qtree gets modified when ``qtree`` is set.
- na_ontap_quotas - ignore job entry does not exist error when creating quota with REST to bypass ONTAP issue with FSx.
- na_ontap_rest_info - fix field issue with private/cli and support/autosupport/check APIs.
- na_ontap_san_create - Role documentation correct to from nas to san
- na_ontap_security_config - fix error on specifying protocol version ``TLSv1.1`` when fips is enabled.
- na_ontap_security_ipsec_policy - fix KeyError on ``authentication_method``.
- na_ontap_security_ipsec_policy - fix cannot get current security IPsec policy with ipspace.
- na_ontap_security_key_manager - requires 9.7+ to work with REST.
- na_ontap_snapmirror - Added option ``identity_preservation`` support from ONTAP 9.11.1 in REST.
- na_ontap_snapmirror - error if identity_preservation set in ZAPI.
- na_ontap_snapmirror - fix invalid value error for return_timeout, modified the value to 120 seconds.
- na_ontap_snapmirror_policy - deleting all retention rules would trigger an error when the existing policy requires at least one rule.
- na_ontap_snapmirror_policy - fix desired policy type not configured in cli with REST.
- na_ontap_snapmirror_policy - fixed idempotency issue on ``identity_preservation`` option when using REST.
- na_ontap_snapmirror_policy - index error on rules with ONTAP 9.12.1 as not all fields are present.
- na_ontap_snapshot - fix cannot modify ``snapmirror_label``, ``expiry_time`` and ``comment`` if not configured in create.
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
- netbox_location - Add multiple filter options to make sure we find the unique location [#963](https://github.com/netbox-community/ansible_modules/pull/963)
- netbox_virtual_machine - Fix idempotency with virtual machine and NetBox 3.0 [#859](https://github.com/netbox-community/ansible_modules/pull/859)
- netbox_webhook - Fix conditions bug [#926](https://github.com/netbox-community/ansible_modules/pull/926)

ngine_io.vultr
~~~~~~~~~~~~~~

- iventory - Fixed ``allowed_bandwidth_gb`` to be returned as float (https://github.com/ngine-io/ansible-collection-vultr/pull/35).
- vultr_server - Fixed ``allowed_bandwidth_gb`` to be returned as float (https://github.com/ngine-io/ansible-collection-vultr/pull/35).
- vultr_server_baremetal - Fixed ``allowed_bandwidth_gb`` to be returned as float (https://github.com/ngine-io/ansible-collection-vultr/pull/35).

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
- purefa_pg - Resolves issue with destroyed pgroup snapshot on an offload target not have a time remaining value
- purefa_pgsched - Fix error when setting schedule for pod based protection group
- purefa_policy - Fixed missing parameters in function calls
- purefa_smtp - Fix parameter name
- purefa_vg - Fix issue with VG creation on newer Purity versions
- purefa_vg - Fix typeerror when using newer Purity versions and setting VG QoS
- purefa_volume - Ensure promotion_stateus is returned correctly on creation
- purefa_volume - Fix bug when overwriting volume using invalid parmaeters
- purefa_volume - Fixed idempotency bug when creating volumes with QoS
- purefa_volume - Fixed issue with promotion status not being called correctly

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
- instance_info - The problem that the module was missing in the runtime action group has been fixed.

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

community.routeros
~~~~~~~~~~~~~~~~~~

- api_modify - when limits for entries in ``queue tree`` are defined as human readable - for example ``25M`` -, the configuration will be correctly set in ROS, but the module will indicate the item is changed on every run even when there was no change done. This is caused by the ROS API which returns the number in bytes - for example ``25000000`` (which is inconsistent with the CLI behavior). In order to mitigate that, the limits have to be defined in bytes (those will still appear as human readable in the ROS CLI) (https://github.com/ansible-collections/community.routeros/pull/131).
- api_modify, api_info - ``routing ospf area``, ``routing ospf area range``, ``routing ospf instance``, ``routing ospf interface-template`` paths are not fully implemeted for ROS6 due to the significat changes between ROS6 and ROS7 (https://github.com/ansible-collections/community.routeros/pull/131).

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

community.aws
~~~~~~~~~~~~~

- community.aws.eks_nodegroup - Manage EKS Nodegroup module

community.docker
~~~~~~~~~~~~~~~~

- community.docker.docker_container_copy_into - Copy a file into a Docker container

community.general
~~~~~~~~~~~~~~~~~

- community.general.gitlab_project_badge - Manage project badges on GitLab Server
- community.general.kdeconfig - Manage KDE configuration files
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
- netapp.ontap.na_ontap_security_ipsec_ca_certificate - NetApp ONTAP module to add or delete ipsec ca certificate.
- netapp.ontap.na_ontap_security_ipsec_config - NetApp ONTAP module to configure IPsec config.
- netapp.ontap.na_ontap_security_ipsec_policy - NetApp ONTAP module to create, modify or delete security IPsec policy.
- netapp.ontap.na_ontap_vserver_audit - NetApp Ontap - create, delete or modify vserver audit configuration.
- netapp.ontap.na_ontap_vserver_peer_permissions - NetApp Ontap - create, delete or modify vserver peer permission.

netbox.netbox
~~~~~~~~~~~~~

- netbox.netbox.netbox_asn - Create, update or delete ASN in NetBox
- netbox.netbox.netbox_fhrp_group - Create, update or delete FHRP groups in NetBox
- netbox.netbox.netbox_inventory_item_role - Create, update or delete inventory item roles in NetBox
- netbox.netbox.netbox_journal_entry - Create journal entries in NetBox
- netbox.netbox.netbox_l2vpn - Create, update or delete L2VPN objects in NetBox
- netbox.netbox.netbox_module_type - Create, update or delete module types in NetBox
- netbox.netbox.netbox_service_template - Create, update or delete service templates in NetBox

purestorage.flasharray
~~~~~~~~~~~~~~~~~~~~~~

- purestorage.flasharray.purefa_snmp_agent - Configure the FlashArray SNMP Agent

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
- dellemc.openmanage.idrac_gather_facts - Role to gather facts from the iDRAC Server.
- dellemc.openmanage.idrac_import_server_config_profile - Role to import iDRAC Server Configuration Profile (SCP).
- dellemc.openmanage.idrac_os_deployment - Role to deploy specified operating system and version on the servers.
- dellemc.openmanage.idrac_server_powerstate - Role to manage the different power states of the specified device.

Unchanged Collections
---------------------

- check_point.mgmt (still version 4.0.0)
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
- frr.frr (still version 2.0.0)
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
- openvswitch.openvswitch (still version 2.1.0)
- purestorage.flashblade (still version 1.10.0)
- splunk.es (still version 2.1.0)
- wti.remote (still version 1.0.4)
