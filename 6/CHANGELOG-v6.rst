=======================
Ansible 6 Release Notes
=======================

This changelog describes changes since Ansible 5.0.0.

.. contents::
  :local:
  :depth: 2

v6.1.0
======

.. contents::
  :local:
  :depth: 2

Release Summary
---------------

Release Date: 2022-07-12

`Porting Guide <https://docs.ansible.com/ansible/devel/porting_guides.html>`_

Added Collections
-----------------

- purestorage.fusion (version 1.0.2)

Ansible-core
------------

Ansible 6.1.0 contains Ansible-core version 2.13.1.
This is a newer version than version 2.13.0 contained in the previous Ansible release.

The changes are reported in the combined changelog below.

Changed Collections
-------------------

If not mentioned explicitly, the changes are reported in the combined changelog below.

+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| Collection                    | Ansible 6.0.0 | Ansible 6.1.0 | Notes                                                                                                                        |
+===============================+===============+===============+==============================================================================================================================+
| amazon.aws                    | 3.2.0         | 3.3.1         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| awx.awx                       | 21.0.0        | 21.2.0        | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| azure.azcollection            | 1.12.0        | 1.13.0        | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| chocolatey.chocolatey         | 1.2.0         | 1.3.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.asa                     | 3.0.0         | 3.1.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.dnac                    | 6.4.0         | 6.5.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.ios                     | 3.0.0         | 3.2.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.iosxr                   | 3.0.0         | 3.2.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.ise                     | 2.4.1         | 2.5.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.meraki                  | 2.6.2         | 2.10.0        |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.nxos                    | 3.0.0         | 3.1.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cloud.common                  | 2.1.1         | 2.1.2         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.aws                 | 3.2.1         | 3.4.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.crypto              | 2.3.2         | 2.4.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.digitalocean        | 1.19.0        | 1.21.0        |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.dns                 | 2.1.1         | 2.2.1         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.docker              | 2.6.0         | 2.7.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.general             | 5.0.2         | 5.3.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.grafana             | 1.4.0         | 1.5.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.hrobot              | 1.3.1         | 1.4.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.mongodb             | 1.4.0         | 1.4.1         | There are no changes recorded in the changelog.                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.mysql               | 3.2.1         | 3.3.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.sops                | 1.2.2         | 1.2.3         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.vmware              | 2.5.0         | 2.7.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| containers.podman             | 1.9.3         | 1.9.4         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| dellemc.openmanage            | 5.4.0         | 5.5.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| f5networks.f5_modules         | 1.17.0        | 1.18.0        |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| hetzner.hcloud                | 1.6.0         | 1.8.1         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| infoblox.nios_modules         | 1.2.2         | 1.3.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| junipernetworks.junos         | 3.0.1         | 3.1.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| kubernetes.core               | 2.3.1         | 2.3.2         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| netapp.cloudmanager           | 21.17.0       | 21.18.0       |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| netapp.ontap                  | 21.19.1       | 21.20.0       |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| ngine_io.vultr                | 1.1.1         | 1.1.2         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| ovirt.ovirt                   | 2.0.4         | 2.1.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| purestorage.fusion            |               | 1.0.2         | The collection was added to Ansible                                                                                          |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| t_systems_mms.icinga_director | 1.29.0        | 1.30.0        |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| vmware.vmware_rest            | 2.1.5         | 2.2.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| wti.remote                    | 1.0.3         | 1.0.4         | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+

Major Changes
-------------

chocolatey.chocolatey
~~~~~~~~~~~~~~~~~~~~~

- win_chocolatey - Added bootstrap_script option to allow users to target a script URL for installing Chocolatey on clients.
- win_chocolatey_facts - Added outdated packages list to data returned.

infoblox.nios_modules
~~~~~~~~~~~~~~~~~~~~~

- Update `text` field of TXT Record `#128 <https://github.com/infobloxopen/infoblox-ansible/pull/128>`_
- Update operation using `old_name` and `new_name` for the object with dummy name in `old_name` (which does not exist in system) will not create a new object in the system. An error will be thrown stating the object does not exist in the system `#129 <https://github.com/infobloxopen/infoblox-ansible/pull/129>`_

Minor Changes
-------------

Ansible-core
~~~~~~~~~~~~

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
- ansible-galaxy - Support resolvelib versions 0.6.x, 0.7.x, and 0.8.x. The full range of supported versions is now >= 0.5.3, < 0.9.0.
- ansible-test - Add RHEL 9.0 remote support.
- ansible-test - Add support for Ubuntu VMs using the ``--remote`` option.
- ansible-test - Add support for exporting inventory with ``ansible-test shell --export {path}``.
- ansible-test - Add support for multi-arch remotes.
- ansible-test - Add support for running non-interactive commands with ``ansible-test shell``.
- ansible-test - Avoid using the ``mock_use_standalone_module`` setting for unit tests running on Python 3.8 or later.
- ansible-test - Blocking mode is now enforced for stdin, stdout and stderr. If any of these are non-blocking then ansible-test will exit during startup with an error.
- ansible-test - Improve consistency of output messages by using stdout or stderr for most output, but not both.
- ansible-test - The ``shell`` command can be used outside a collection if no controller delegation is required.

amazon.aws
~~~~~~~~~~

- aws_ec2 inventory - Allow for literal strings in hostname that don't match filter parameters in ec2 describe-instances (https://github.com/ansible-collections/amazon.aws/pull/826).
- aws_ssm - Add support for ``endpoint`` parameter (https://github.com/ansible-collections/amazon.aws/pull/837).
- module.utils.rds - add retry_codes to get_rds_method_attribute return data to use in call_method and add unit tests (https://github.com/ansible-collections/amazon.aws/pull/776).
- module.utils.rds - refactor to utilize get_rds_method_attribute return data (https://github.com/ansible-collections/amazon.aws/pull/776).
- module_utils - add new aliases ``aws_session_token`` and ``session_token`` to the ``security_token`` parameter to be more in-line with the boto SDK (https://github.com/ansible-collections/amazon.aws/pull/631).
- module_utils.rds - Add support and unit tests for addition/removal of IAM roles to/from a db instance in module_utils.rds with waiters (https://github.com/ansible-collections/amazon.aws/pull/714).

chocolatey.chocolatey
~~~~~~~~~~~~~~~~~~~~~

- All collection modules - assorted style/linting fixes in documentation and scripts.

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

cisco.ios
~~~~~~~~~

- Also collect a list of serial numbers comprised in a vss system as virtual_switch_serialnums
- Fixing Detection of Virtual Switch System to facts (https://github.com/ansible-collections/cisco.ios/pull/471)
- `ios_interfaces` - Add purged state to ios_interfaces.
- `ios_ping` - Add ipv6 options.

cisco.iosxr
~~~~~~~~~~~

- Add label and comment to commit_confirmed functionality in IOSXR.
- `iosxr_ping` - Add iosxr_ping module.

cisco.ise
~~~~~~~~~

- Update requirements to use ciscoisesdk >= 2.0.3.

cisco.meraki
~~~~~~~~~~~~

- meraki_action_batch - New module for CRUD operations on Meraki Action Batches
- meraki_mx_network_vlan_settings - New module to enable or disable VLANs on a network
- meraki_mx_third_party_vpn_peers - New module for managing third party VPM peers
- meraki_network - Add support for `copy_from_network_id`.
- meraki_switchport - Add support for flexible stacking

cisco.nxos
~~~~~~~~~~

- `nxos_snmp_server` - Add support for localizedV2key (https://github.com/ansible-collections/cisco.nxos/issues/415).
- `nxos_snmp_server` - Add support for sha-256 based based user authentication.

community.aws
~~~~~~~~~~~~~

- aws_codebuild - add support for ``purge_tags`` parameter (https://github.com/ansible-collections/community.aws/pull/1221).
- aws_codebuild - add the ``resource_tags`` parameter which takes the dictionary format for tags instead of the list of dictionaries format (https://github.com/ansible-collections/community.aws/pull/1221).
- aws_codebuild - add the ``resource_tags`` return value which returns the standard dictionary format for tags instead of the list of dictionaries format (https://github.com/ansible-collections/community.aws/pull/1221).
- aws_codebuild - the ``source`` and ``artifacts`` parameters are now optional unless creating a new project (https://github.com/ansible-collections/community.aws/pull/1221).
- aws_kms - add extra key/value pair to return data (key_policies) to return each policy as a dictionary rather than json string (https://github.com/ansible-collections/community.aws/pull/1052).
- aws_kms - fix some bugs in integration tests and add check mode support for key rotation as well as document issues with time taken for requested changes to be reflected on AWS (https://github.com/ansible-collections/community.aws/pull/1052).
- ec2_asg - add check mode support (https://github.com/ansible-collections/community.aws/pull/1033).
- ecs_service - ``deployment_circuit_breaker`` has been added as a supported feature (https://github.com/ansible-collections/community.aws/pull/1215).
- ecs_service - add ``service`` alias to address the ecs service name with the same parameter as the ecs_service_info module is doing (https://github.com/ansible-collections/community.aws/pull/1187).
- ecs_service_info - add ``name`` alias to address the ecs service name with the same parameter as the ecs_service module is doing (https://github.com/ansible-collections/community.aws/pull/1187).
- ecs_tag - ``resource_tags`` has been added as an alias for the ``tags`` parameter (https://github.com/ansible-collections/community.aws/pull/1184).
- efs_tag - ``resource_tags`` has been added as an alias for the ``tags`` parameter (https://github.com/ansible-collections/community.aws/pull/1184).
- iam_policy - update broken examples and add RETURN section to documentation; add extra integration tests for idempotency check mode runs (https://github.com/ansible-collections/community.aws/pull/1093).
- iam_user - add ``user`` value to return data structure to deprecate old ``iam_user`` (https://github.com/ansible-collections/community.aws/pull/1059).
- lambda - add kms_key_arn parameter (https://github.com/ansible-collections/community.aws/pull/1108).
- rds_instance - add ``deletion_protection`` parameter (https://github.com/ansible-collections/community.aws/pull/1105).
- rds_instance - add snapshot tests to test suite to test restoring db from snapshot (https://github.com/ansible-collections/community.aws/pull/1081).
- rds_instance - add support for addition/removal of iam roles to db instance (https://github.com/ansible-collections/community.aws/pull/1002).
- rds_instance_info - add retries on common AWS failures (https://github.com/ansible-collections/community.aws/pull/1026).
- rds_instance_snapshot - add ``check_mode`` (https://github.com/ansible-collections/community.aws/pull/789).
- rds_instance_snapshot - add copy_db_snapshot functionality (https://github.com/ansible-collections/community.aws/pull/1078).
- rds_instance_snapshot - add integration tests (https://github.com/ansible-collections/community.aws/pull/789).
- rds_instance_snapshot - update module to use handlers defined in module_utils/rds.py (https://github.com/ansible-collections/community.aws/pull/789).
- route53 - add support for GeoLocation param (https://github.com/ansible-collections/amazon.aws/pull/1117).
- wafv2_web_acl - relax botocore requirement to bare minimum required (https://github.com/ansible-collections/community.aws/pull/1216).

community.digitalocean
~~~~~~~~~~~~~~~~~~~~~~

- digital_ocean - add sanity test ignores for Ansible 2.12 and 2.13 (https://github.com/ansible-collections/community.digitalocean/issues/247).
- digital_ocean_cdn_endpoints - update Spaces endpoint and add a few delays to the integration test (https://github.com/ansible-collections/community.digitalocean/issues/267).
- digital_ocean_load_balancer - Allow creating a load balancer and associating droplets by tag as an alternative to ``droplet_ids``.

community.dns
~~~~~~~~~~~~~

- hetzner_dns_records and hosttech_dns_records inventory plugins - allow to template provider-specific credentials and the ``zone_name``, ``zone_id`` options (https://github.com/ansible-collections/community.dns/pull/106).
- wait_for_txt - improve error messages so that in case of SERVFAILs or other DNS errors it is clear which record was queried from which DNS server (https://github.com/ansible-collections/community.dns/pull/105).

community.docker
~~~~~~~~~~~~~~~~

- Move common utility functions from the ``common`` module_util to a new module_util called ``util``. This should not have any user-visible effect (https://github.com/ansible-collections/community.docker/pull/390).

community.general
~~~~~~~~~~~~~~~~~

- ModuleHelper module utils - improved ``ModuleHelperException``, using ``to_native()`` for the exception message (https://github.com/ansible-collections/community.general/pull/4755).
- alternatives - add ``state=absent`` to be able to remove an alternative (https://github.com/ansible-collections/community.general/pull/4654).
- alternatives - add ``subcommands`` parameter (https://github.com/ansible-collections/community.general/pull/4654).
- ansible_galaxy_install - minor refactoring using latest ``ModuleHelper`` updates (https://github.com/ansible-collections/community.general/pull/4752).
- cmd_runner module util - added parameters ``check_mode_skip`` and ``check_mode_return`` to ``CmdRunner.context()``, so that the command is not executed when ``check_mode=True`` (https://github.com/ansible-collections/community.general/pull/4736).
- cmd_runner module utils - add ``__call__`` method to invoke context (https://github.com/ansible-collections/community.general/pull/4791).
- machinectl become plugin - can now be used with a password from another user than root, if a polkit rule is present (https://github.com/ansible-collections/community.general/pull/4849).
- nmcli - adds ``vpn`` type and parameter for supporting VPN with service type L2TP and PPTP (https://github.com/ansible-collections/community.general/pull/4746).
- opentelemetry callback plugin - allow configuring opentelementry callback via config file (https://github.com/ansible-collections/community.general/pull/4916).
- passwordstore lookup plugin - allow using alternative password managers by detecting wrapper scripts, allow explicit configuration of pass and gopass backends (https://github.com/ansible-collections/community.general/issues/4766).
- proxmox inventory plugin - added new flag ``qemu_extended_statuses`` and new groups ``<group_prefix>prelaunch``, ``<group_prefix>paused``. They will be populated only when ``want_facts=true``, ``qemu_extended_statuses=true`` and only for ``QEMU`` machines (https://github.com/ansible-collections/community.general/pull/4723).
- puppet - adds ``confdir`` parameter to configure a custom confir location (https://github.com/ansible-collections/community.general/pull/4740).
- redfish_info - add ``GetManagerInventory`` to report list of Manager inventory information (https://github.com/ansible-collections/community.general/issues/4899).
- sudoers - will attempt to validate the proposed sudoers rule using visudo if available, optionally skipped, or required (https://github.com/ansible-collections/community.general/pull/4794, https://github.com/ansible-collections/community.general/issues/4745).
- xfconf - changed implementation to use ``cmd_runner`` (https://github.com/ansible-collections/community.general/pull/4776).
- xfconf module utils - created new module util ``xfconf`` providing a ``cmd_runner`` specific for ``xfconf`` modules (https://github.com/ansible-collections/community.general/pull/4776).
- xfconf_info - changed implementation to use ``cmd_runner`` (https://github.com/ansible-collections/community.general/pull/4776).

community.grafana
~~~~~~~~~~~~~~~~~

- community.grafana.grafana_datasource supports grafana-azure-monitor-datasource.

community.hrobot
~~~~~~~~~~~~~~~~

- robot inventory plugin - allow to template ``hetzner_user`` and ``hetzner_password`` (https://github.com/ansible-collections/community.hrobot/pull/49).

community.mysql
~~~~~~~~~~~~~~~

- mysql_role - add the argument ``members_must_exist`` (boolean, default true). The assertion that the users supplied in the ``members`` argument exist is only executed when the new argument ``members_must_exist`` is ``true``, to allow opt-out (https://github.com/ansible-collections/community.mysql/pull/369).
- mysql_user - Add the option ``on_new_username`` to argument ``update_password`` to reuse the password (plugin and authentication_string) when creating a new user if some user with the same name already exists. If the existing user with the same name have varying passwords, the password from the arguments is used like with ``update_password: always`` (https://github.com/ansible-collections/community.mysql/pull/365).
- mysql_user - Add the result field ``password_changed`` (boolean). It is true, when the user got a new password. When the user was created with ``update_password: on_new_username`` and an existing password was reused, ``password_changed`` is false (https://github.com/ansible-collections/community.mysql/pull/365).

community.vmware
~~~~~~~~~~~~~~~~

- vmware_dvswitch.py - Add Netflow Settings. (https://github.com/ansible-collections/community.vmware/pull/1352)
- vmware_dvswitch_nioc.py - Add backupNfc and nvmetcp to the resources. (https://github.com/ansible-collections/community.vmware/pull/1351)
- vmware_guest_disk - Add a new disk type to support add/reconfigure/remove vPMem disk (https://github.com/ansible-collections/community.vmware/pull/1382).
- vmware_host_passthrough - Support the PCI id in the devices parameter(https://github.com/ansible-collections/community.vmware/pull/1365).
- vmware_object_role_permission.py - Add StoragePod to the list of object_types. (https://github.com/ansible-collections/community.vmware/pull/1338)
- vmware_object_role_permission_info.py - Add StoragePod and DistributedVirtalPortgroup to the list of object_types. (https://github.com/ansible-collections/community.vmware/pull/1338)
- vmware_vmotion - Add the feature to use cluster and datastore cluster (storage pods) to define where the vmotion shold go. (https://github.com/ansible-collections/community.vmware/pull/1240)

containers.podman
~~~~~~~~~~~~~~~~~

- Remove distutils as deprecated
- Run CI on Ubuntu 22.04
- Use 2.13 Ansible version in CI jobs instead of 2.11

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- idrac_redfish_storage_controller - This module is updated to use the Job Service URL instead of Task Service URL for job tracking.
- idrac_server_config_profile - This module is updated to use the Job Service URL instead of Task Service URL for job tracking.
- redfish_firmware - This module is updated to use the Job Service URL instead of Task Service URL for job tracking.

f5networks.f5_modules
~~~~~~~~~~~~~~~~~~~~~

- bigip_pool - add three new parameters named, min_up_members, min_up_members_action and min_up_members_checking

hetzner.hcloud
~~~~~~~~~~~~~~

- inventory - allow filtering by server status
- inventory - support jinjia templating within `network`

junipernetworks.junos
~~~~~~~~~~~~~~~~~~~~~

- Add mac-vrf instance type.

kubernetes.core
~~~~~~~~~~~~~~~

- helm_repository - mark `pass_credentials` as no_log=True to silence false warning (https://github.com/ansible-collections/kubernetes.core/issues/412).
- kubectl.py - replace distutils.spawn.find_executable with shutil.which in the kubectl connection plugin (https://github.com/ansible-collections/kubernetes.core/pull/456).

netapp.cloudmanager
~~~~~~~~~~~~~~~~~~~

- na_cloudmanager_connector_azure - Support full ``subnet_id`` and ``vnet_id``.

netapp.ontap
~~~~~~~~~~~~

- na_ontap_aggregate - updated ``disk_types`` in documentation.
- na_ontap_cifs_server - Added ``security`` options in REST.
- na_ontap_export_policy_rule - Add ``from_rule_index`` for both REST and ZAPI. Change ``rule_index`` to required.
- na_ontap_nvme_namespace - Added REST support.
- na_ontap_nvme_subsystem - Added REST support.
- na_ontap_portset - Added REST support.
- na_ontap_snapmirror - new option ``peer_options`` to define source connection parameters.
- na_ontap_snapmirror - new option ``transferring_time_out`` to define how long to wait for transfer to complete on create or initialize.
- na_ontap_snapmirror - rewrite update for REST using POST to initiate transfer.
- na_ontap_snapmirror - when deleting, attempt to delete even when the relationship cannot be broken.
- na_ontap_software_update - added REST support.
- na_ontap_svm - Added documentation for ``allowed_protocol``, ndmp is default in REST.
- na_ontap_user - add support for SAML authentication_method.
- na_ontap_vscan_on_access_policy - Added REST support.
- na_ontap_vscan_on_access_policy - new REST options ``scan_readonly_volumes`` and ``only_execute_access`` added.
- na_ontap_vscan_on_demand_task - Added REST support.
- na_ontap_vserver_cifs_security - Added ``use_ldaps_for_ad_ldap`` and ``use_start_tls_for_ad_ldap`` as mutually exclusive in ZAPI.
- na_ontap_vserver_cifs_security - Added option ``encryption_required_for_dc_connections`` and ``use_ldaps_for_ad_ldap`` in ZAPI.
- na_ontap_vserver_cifs_security - fall back to ZAPI when ``use_rest`` is set to ``auto`` or fail when REST is desired.

ngine_io.vultr
~~~~~~~~~~~~~~

- Documentation fixes.

ovirt.ovirt
~~~~~~~~~~~

- Add convert_to_bytes filter (https://github.com/oVirt/ovirt-ansible-collection/pull/515).
- automation - Use python38 on el8 with ansible-core 2.12 and python39 on el9 with ansible-core 2.13  (https://github.com/oVirt/ovirt-ansible-collection/pull/518).
- cloud.py - Sync with orgin (https://github.com/oVirt/ovirt-ansible-collection/pull/519).
- engine_setup - Allow to disable cert validation (https://github.com/oVirt/ovirt-ansible-collection/pull/517).
- hosted_engine_setup - make vdsm config cleanup optional (https://github.com/oVirt/ovirt-ansible-collection/pull/521).
- ovirt - Remove deprecated distutils (https://github.com/oVirt/ovirt-ansible-collection/pull/516).
- ovirt_vm - add wait_after_lease (https://github.com/oVirt/ovirt-ansible-collection/pull/524).

t_systems_mms.icinga_director
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Add action_group to enable module default groups (https://github.com/T-Systems-MMS/ansible-collection-icinga-director/pull/175)

vmware.vmware_rest
~~~~~~~~~~~~~~~~~~

- Add news example for clone, instant clone and template on Content Library.
- documentation - clarify that the VMware vCenter API doesn't allow the cloning of template if there are not if Library.
- vcenter_vm - Add new examples (clone and instant clone).

Deprecated Features
-------------------

cisco.ios
~~~~~~~~~

- Deprecated ios_linkagg_module in favor of ios_lag_interfaces.

community.aws
~~~~~~~~~~~~~

- aws_codebuild - The ``tags`` parameter currently uses a non-standard format and has been deprecated.  In release 6.0.0 this parameter will accept a simple key/value pair dictionary instead of the current list of dictionaries.  It is recommended to migrate to using the resource_tags parameter which already accepts the simple dictionary format (https://github.com/ansible-collections/community.aws/pull/1221).
- route53_info - The CamelCase return values for ``HostedZones``, ``ResourceRecordSets``, and ``HealthChecks`` have been deprecated, in the future release you must use snake_case return values ``hosted_zones``, ``resource_record_sets``, and ``health_checks`` instead respectively".

community.crypto
~~~~~~~~~~~~~~~~

- Support for Ansible 2.9 and ansible-base 2.10 is deprecated, and will be removed in the next major release (community.crypto 3.0.0). Some modules might still work with these versions afterwards, but we will no longer keep compatibility code that was needed to support them (https://github.com/ansible-collections/community.crypto/pull/460).

community.docker
~~~~~~~~~~~~~~~~

- Support for Docker API version 1.20 to 1.24 has been deprecated and will be removed in community.docker 3.0.0. The first Docker version supporting API version 1.25 was Docker 1.13, released in January 2017. This affects the modules ``docker_container``, ``docker_container_exec``, ``docker_container_info``, ``docker_compose``, ``docker_login``, ``docker_image``, ``docker_image_info``, ``docker_image_load``, ``docker_host_info``, ``docker_network``, ``docker_network_info``, ``docker_node_info``, ``docker_swarm_info``, ``docker_swarm_service``, ``docker_swarm_service_info``, ``docker_volume_info``, and ``docker_volume``, whose minimally supported API version is between 1.20 and 1.24 (https://github.com/ansible-collections/community.docker/pull/396).
- Support for Python 2.6 is deprecated and will be removed in the next major release (community.docker 3.0.0). Some modules might still work with Python 2.6, but we will no longer try to ensure compatibility (https://github.com/ansible-collections/community.docker/pull/388).

community.general
~~~~~~~~~~~~~~~~~

- cmd_runner module utils - deprecated ``fmt`` in favour of ``cmd_runner_fmt`` as the parameter format object (https://github.com/ansible-collections/community.general/pull/4777).

Bugfixes
--------

Ansible-core
~~~~~~~~~~~~

- Add PyYAML >= 5.1 as a dependency of ansible-core to be compatible with Python 3.8+.
- ansible-config dump - Only display plugin type headers when plugin options are changed if --only-changed is specified.
- ansible-galaxy - handle unsupported versions of resolvelib gracefully.
- ansible-test - Fix internal validation of remote completion configuration.
- ansible-test - Prevent ``--target-`` prefixed options for the ``shell`` command from being combined with legacy environment options.
- ansible-test - Sanity test output with the ``--lint`` option is no longer mixed in with bootstrapping output.
- ansible-test - Subprocesses are now isolated from the stdin, stdout and stderr of ansible-test. This avoids issues with subprocesses tampering with the file descriptors, such as SSH making them non-blocking. As a result of this change, subprocess output from unit and integration tests on stderr now go to stdout.
- ansible-test - Subprocesses no longer have access to the TTY ansible-test is connected to, if any. This maintains consistent behavior between local testing and CI systems, which typically do not provide a TTY. Tests which require a TTY should use pexpect or another mechanism to create a PTY.
- apt module now correctly handles virtual packages.
- lookup plugin - catch KeyError when lookup returns dictionary (https://github.com/ansible/ansible/pull/77789).
- pip - fix cases where resolution of pip Python module fails when importlib.util has not already been imported
- plugin loader - Sort results when fuzzy matching plugin names (https://github.com/ansible/ansible/issues/77966).
- plugin loader will now load config data for plugin by name instead of by file to avoid issues with the same file being loaded under different names (fqcn + short name).
- psrp connection now handles default to inventory_hostname correctly.
- winrm connection now handles default to inventory_hostname correctly.

amazon.aws
~~~~~~~~~~

- Include ``PSF-license.txt`` file for ``plugins/module_utils/_version.py``.
- aws_account_attribute lookup plugin - fix linting errors in documentation data (https://github.com/ansible-collections/amazon.aws/pull/701).
- aws_ec2 inventory plugin - fix linting errors in documentation data (https://github.com/ansible-collections/amazon.aws/pull/701).
- aws_rds inventory plugin - fix linting errors in documentation data (https://github.com/ansible-collections/amazon.aws/pull/701).
- aws_resource_actions callback plugin - fix linting errors in documentation data (https://github.com/ansible-collections/amazon.aws/pull/701).
- aws_secret lookup plugin - fix linting errors in documentation data (https://github.com/ansible-collections/amazon.aws/pull/701).
- aws_service_ip_ranges lookup plugin - fix linting errors in documentation data (https://github.com/ansible-collections/amazon.aws/pull/701).
- aws_ssm - Fix environment variables for client configuration (e.g., AWS_PROFILE, AWS_ACCESS_KEY_ID) (https://github.com/ansible-collections/amazon.aws/pull/837).
- aws_ssm lookup plugin - fix linting errors in documentation data (https://github.com/ansible-collections/amazon.aws/pull/701).
- ec2_instance - ec2_instance module broken in Python 3.8 - dict keys modified during iteration (https://github.com/ansible-collections/amazon.aws/issues/709).
- module.utils.rds - Add waiter for promoting read replica to fix idempotency issue (https://github.com/ansible-collections/amazon.aws/pull/714).
- module.utils.rds - Catch InvalidDBSecurityGroupStateFault when modifying a db instance (https://github.com/ansible-collections/amazon.aws/pull/776).
- module.utils.s3 - Update validate_bucket_name minimum length to 3 (https://github.com/ansible-collections/amazon.aws/pull/802).

cisco.asa
~~~~~~~~~

- Fix service-object port range rendering
- Fixes asa_ogs port object range issue and duplicate service cmd (https://github.com/ansible-collections/cisco.asa/issues/165, https://github.com/ansible-collections/cisco.asa/issues/166).
- Unit TC for svc src/dst port range

cisco.ios
~~~~~~~~~

- `ios_acl` - Handle ACL config parsing when match/matches are present.
- `ios_bgp_global` - Parse local_as commands correctly.
- `ios_interfaces` - Fix enable attribute.
- `ios_interfaces` - Parse interface shutdown config correctly.
- `ios_lag_interfaces` - Fix commands generation on action states.
- `ios_lag_interfaces` - Module functionality not restricted to GigabitEthernet.
- `ios_logging_global` - Parse monitor and buffered config correctly.
- `ios_ntp` - Handle regex matching server attributes gracefully.
- `ios_snmp_server` - Render group and views commands correctly when having common names.

cisco.iosxr
~~~~~~~~~~~

- Fix commit confirmed for IOSXR versions with atomic commands.
- Fix commit confirmed to render proper command without timeout.
- Remove irrelevant warning from facts.

cisco.ise
~~~~~~~~~

- Fixed ISE version 3.1.1 to 3.1_Patch_1 which is the correct version name.
- repository - Fixed a bug, now repositoryName and name are used to perform the search.
- repository_files_info - Fixed a bug that did not make the get call.

cisco.meraki
~~~~~~~~~~~~

- meraki_mx_static_route - Add support for gateway_vlan_id otherwise requests could error
- meraki_switchport - Setting VLAN to 0 on trunk port clears the VLAN.

cisco.nxos
~~~~~~~~~~

- `nxos_file_copy` - Skip `vrf` when running against MDS switches (https://github.com/ansible-collections/cisco.nxos/issues/508).
- `nxos_interfaces` - Enable all virtual interfaces with `enabled` set to True (https://github.com/ansible-collections/cisco.nxos/issues/335).
- `nxos_ntp_global` - Ensure idempotence for aliased keys (https://github.com/ansible-collections/cisco.nxos/issues/484).
- `nxos_snmp_server` - Fix typo for traps link cisco-xcvr-mon-status-chg.

cloud.common
~~~~~~~~~~~~

- Ensure we don't shutdown the server when we've still got some ongoing tasks (https://github.com/ansible-collections/cloud.common/pull/109).

community.aws
~~~~~~~~~~~~~

- aws_codebuild - fix bug where the result may be spuriously flagged as ``changed`` when multiple tags were set on the project (https://github.com/ansible-collections/community.aws/pull/1221).
- dynamodb_table - fix an issue when creating secondary indexes with global_keys_only (https://github.com/ansible-collections/community.aws/issues/967).
- ecs_service - add missing change detect of ``health_check_grace_period_seconds`` parameter (https://github.com/ansible-collections/community.aws/pull/1145).
- ecs_service - fix broken change detect of ``health_check_grace_period_seconds`` parameter when not specified (https://github.com/ansible-collections/community.aws/pull/1212).
- ecs_service - fix broken compare of ``task_definition`` that results always in a changed task (https://github.com/ansible-collections/community.aws/pull/1145).
- ecs_service - fix validation for ``placement_constraints``. It's possible to use ``distinctInstance`` placement constraint now (https://github.com/ansible-collections/community.aws/issues/1058)
- ecs_service - use default cluster name of ``default`` when not input (https://github.com/ansible-collections/community.aws/pull/1212).
- ecs_task - dont require ``cluster`` and use name of ``default`` when not input (https://github.com/ansible-collections/community.aws/pull/1212).
- ecs_taskdefinition - fix broken change detect of ``launch_type`` parameter (https://github.com/ansible-collections/community.aws/pull/1145).
- execute_lambda - add waiter for function_updated (https://github.com/ansible-collections/community.aws/pull/1108).
- execute_lambda - fix check mode and update RETURN documentation (https://github.com/ansible-collections/community.aws/pull/1115).
- iam_policy - require one of ``policy_document`` and ``policy_json`` when state is present to prevent MalformedPolicyDocumentException from being thrown (https://github.com/ansible-collections/community.aws/pull/1093).
- iam_user - don't delete user login profile on check mode (https://github.com/ansible-collections/community.aws/pull/1059).
- iam_user_info - gracefully handle when no users are found (https://github.com/ansible-collections/community.aws/pull/1059).
- lambda - fix check mode on creation (https://github.com/ansible-collections/community.aws/pull/1108).
- lambda_info - fix bug that forces query=config when getting info for all lambdas. Now, if function name is specified, query will default to all.  This may have a performance impact when querying a large number of lambdas. If function name is not specified, query will default to config (https://github.com/ansible-collections/community.aws/pull/1152).
- rds_instance - fix bugs associated with restoring db instance from snapshot (https://github.com/ansible-collections/community.aws/pull/1081).
- rds_instance - fix check_mode and idempotency issues and added integration tests for all tests in suite (https://github.com/ansible-collections/community.aws/pull/1002).
- rds_instance_snapshot - don't require ``db_instance_identifier`` on state = present (https://github.com/ansible-collections/community.aws/pull/1078).
- s3_lifecycle - add support of value *0* for ``transition_days`` (https://github.com/ansible-collections/community.aws/pull/1077).
- s3_lifecycle - check that configuration is complete before returning (https://github.com/ansible-collections/community.aws/pull/1085).
- wafv2_ip_set - fix bug where incorrect changed state was returned when only changing the description (https://github.com/ansible-collections/community.aws/pull/1211).
- wafv2_web_acl - consistently return web ACL info as described in module documentation (https://github.com/ansible-collections/community.aws/pull/1216).
- wafv2_web_acl - fix ``changed`` status when description not specified (https://github.com/ansible-collections/community.aws/pull/1216).

community.crypto
~~~~~~~~~~~~~~~~

- Include ``Apache-2.0.txt`` file for ``plugins/module_utils/crypto/_obj2txt.py`` and ``plugins/module_utils/crypto/_objects_data.py``.
- openssl_csr - the module no longer crashes with 'permitted_subtrees/excluded_subtrees must be a non-empty list or None' if only one of ``name_constraints_permitted`` and ``name_constraints_excluded`` is provided (https://github.com/ansible-collections/community.crypto/issues/481).
- openssl_pkcs12 - when using the pyOpenSSL backend, do not crash when trying to read non-existing other certificates (https://github.com/ansible-collections/community.crypto/issues/486, https://github.com/ansible-collections/community.crypto/pull/487).
- x509_crl - do not crash when signing CRL with Ed25519 or Ed448 keys (https://github.com/ansible-collections/community.crypto/issues/473, https://github.com/ansible-collections/community.crypto/pull/474).

community.digitalocean
~~~~~~~~~~~~~~~~~~~~~~

- digital_ocean_droplet - fix regression in droplet deletion where ``name`` and ``unique_name`` (set to true) are required and ``id`` alone is insufficient (though ``id`` is sufficient to uniquely identify a droplet for deletion). (https://github.com/ansible-collections/community.digitalocean/issues/260)
- digital_ocean_droplet - fix regression where droplet info (for example networking) doesn't update when waiting during creation unless ``unique_name`` is set to true (https://github.com/ansible-collections/community.digitalocean/issues/220).
- digital_ocean_droplet - if the JSON response lacks a key and the associated variable is set to ``None``, then don't treat that variable like a ``dict`` and call ``get()`` on it without first testing it (https://github.com/ansible-collections/community.digitalocean/issues/272).

community.dns
~~~~~~~~~~~~~

- Update Public Suffix List.

community.docker
~~~~~~~~~~~~~~~~

- Docker SDK for Python based modules and plugins - if the API version is specified as an option, use that one to validate API version requirements of module/plugin options instead of the latest API version supported by the Docker daemon. This also avoids one unnecessary API call per module/plugin (https://github.com/ansible-collections/community.docker/pull/389).

community.general
~~~~~~~~~~~~~~~~~

- Include ``PSF-license.txt`` file for ``plugins/module_utils/_mount.py``.
- alternatives - do not set the priority if the priority was not set by the user (https://github.com/ansible-collections/community.general/pull/4810).
- alternatives - only pass subcommands when they are specified as module arguments (https://github.com/ansible-collections/community.general/issues/4803, https://github.com/ansible-collections/community.general/issues/4804, https://github.com/ansible-collections/community.general/pull/4836).
- alternatives - when ``subcommands`` is specified, ``link`` must be given for every subcommand. This was already mentioned in the documentation, but not enforced by the code (https://github.com/ansible-collections/community.general/pull/4836).
- cmd_runner module utils - fix bug caused by using the ``command`` variable instead of ``self.command`` when looking for binary path (https://github.com/ansible-collections/community.general/pull/4903).
- dsv lookup plugin - do not ignore the ``tld`` parameter (https://github.com/ansible-collections/community.general/pull/4911).
- lxd connection plugin - fix incorrect ``inventory_hostname`` in ``remote_addr``. This is needed for compatibility with ansible-core 2.13 (https://github.com/ansible-collections/community.general/issues/4886).
- nmcli - fix error caused by adding undefined module arguments for list options (https://github.com/ansible-collections/community.general/issues/4373, https://github.com/ansible-collections/community.general/pull/4813).
- proxmox inventory plugin - fix crash when ``enabled=1`` is used in agent config string (https://github.com/ansible-collections/community.general/pull/4910).
- proxmox inventory plugin - fixed extended status detection for qemu (https://github.com/ansible-collections/community.general/pull/4816).
- rax_clb_nodes - fix code to be compatible with Python 3 (https://github.com/ansible-collections/community.general/pull/4933).
- redfish_command - fix the check if a virtual media is unmounted to just check for ``instered= false`` caused by Supermicro hardware that does not clear the ``ImageName`` (https://github.com/ansible-collections/community.general/pull/4839).
- redfish_command - the Supermicro Redfish implementation only supports the ``image_url`` parameter in the underlying API calls to ``VirtualMediaInsert`` and ``VirtualMediaEject``. Any values set (or the defaults) for ``write_protected`` or ``inserted`` will be ignored (https://github.com/ansible-collections/community.general/pull/4839).
- redfish_info - fix to ``GetChassisPower`` to correctly report power information when multiple chassis exist, but not all chassis report power information (https://github.com/ansible-collections/community.general/issues/4901).
- redhat_subscription - fix unsubscribing on RHEL 9 (https://github.com/ansible-collections/community.general/issues/4741).
- sudoers - ensure sudoers config files are created with the permissions requested by sudoers (0440) (https://github.com/ansible-collections/community.general/pull/4814).
- sudoers - fix incorrect handling of ``state: absent`` (https://github.com/ansible-collections/community.general/issues/4852).

community.grafana
~~~~~~~~~~~~~~~~~

- Fix a bug that causes a fatal error when using `url` parameter in `grafana_dashboard` and `grafana_notification_channel` modules.
- Fix a bug that causes an update error when using the `grafana_datasource` module on Grafana >=9.0.0 (https://github.com/ansible-collections/community.grafana/issues/248).

community.mysql
~~~~~~~~~~~~~~~

- mysql_query - fix false change reports when ``IF EXISTS/IF NOT EXISTS`` clause is used (https://github.com/ansible-collections/community.mysql/issues/268).
- mysql_role - don't add members to a role when creating the role and ``detach_members: true`` is set (https://github.com/ansible-collections/community.mysql/pull/367).
- mysql_role - in some cases (when "SHOW GRANTS" did not use backticks for quotes), no unwanted members were detached from the role (and redundant "GRANT" statements were executed for wanted members). This is fixed by querying the existing role members from the mysql.role_edges (MySQL) or mysql.roles_mapping (MariaDB) tables instead of parsing the "SHOW GRANTS" output (https://github.com/ansible-collections/community.mysql/pull/368).
- mysql_user - fix logic when ``update_password`` is set to ``on_create`` for users using ``plugin*`` arguments (https://github.com/ansible-collections/community.mysql/issues/334). The ``on_create`` sets ``password`` to None for old mysql_native_authentication but not for authentiation methods which uses the ``plugin*`` arguments. This PR changes this so ``on_create`` also exchange ``plugin``, ``plugin_hash_string``, ``plugin_auth_string`` to None in the list of arguments to change

community.vmware
~~~~~~~~~~~~~~~~

- vmware_cfg_backup - Fix a bug that failed the module when port 80 is blocked (https://github.com/ansible-collections/community.vmware/issues/1270).
- vmware_content_deploy_ovf_template - Fixed a bug that ignored `resource_pool` in some cases. (https://github.com/ansible-collections/community.vmware/issues/1290).
- vmware_content_deploy_template - Fixed a bug that ignored `resource_pool` in some cases. (https://github.com/ansible-collections/community.vmware/issues/1290).
- vmware_guest_disk - Ignore datastores in maintenance mode (https://github.com/ansible-collections/community.vmware/pull/1321).
- vmware_guest_instant_clone - Support FQPN in the folder parameter.
- vmware_guest_network - Fix a typo in the code for SR-IOV NICs (https://github.com/ansible-collections/community.vmware/issues/1317).
- vmware_guest_network - Fix an `AttributeError` when using SR-IOV NICs (https://github.com/ansible-collections/community.vmware/issues/1318).
- vmware_host_facts - Fix a bug that crashes the module when a host is disconnected (https://github.com/ansible-collections/vmware/issues/184).
- vmware_host_vmnic_info - Fix a bug that crashes the module when a host is disconnected (https://github.com/ansible-collections/community.vmware/pull/1337).

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

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- idrac_server_config_profile - Issue(234817) – When an XML format is exported using the SCP, the module breaks while waiting for the job completion.
- ome_application_console_preferences - Issue(224690) - The module does not display a proper error message when an unsupported value is provided for the parameters report_row_limit, email_sender_settings, and metric_collection_settings, and the value is applied on OpenManage Enterprise

f5networks.f5_modules
~~~~~~~~~~~~~~~~~~~~~

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
- bigip_monitor_mysql - fixed bug related to ip extraction from monitor.
- bigip_monitor_oracle - fixed bug related to ip extraction from monitor.
- bigip_monitor_smtp - fixed bug related to ip extraction from monitor.
- bigip_monitor_tcp - fixed bug related to ip extraction from monitor.
- bigip_monitor_udp - fixed bug related to ip extraction from monitor.

hetzner.hcloud
~~~~~~~~~~~~~~

- hcloud_server_network - fixes changed alias_ips by using sorted

junipernetworks.junos
~~~~~~~~~~~~~~~~~~~~~

- fixes the nighbors list overwrite issue.

netapp.ontap
~~~~~~~~~~~~

- na_ontap_autosupport - TypeError on ``ondemand_enabled`` field with ONTAP 9.11.
- na_ontap_autosupport - TypeError on ``support`` field with ONTAP 9.11.
- na_ontap_autosupport - fix idempotency issue on ``state`` field with ONTAP 9.11.
- na_ontap_cluster_config - fix the role to be able to create intercluster LIFs with REST (ipspace is required).
- na_ontap_interface - ignore ``vserver`` when using REST if role is one of 'cluster', 'node-mgmt', 'intercluster', 'cluster-mgmt'.
- na_ontap_net_subnet - delete fails if ipspace is different than Default.
- na_ontap_nvme - fixed ``status_admin`` option is ignored if set to False when creating nvme service in REST.
- na_ontap_nvme - fixed invalid boolean value error for ``status_admin`` when creating nvme service in ZAPI.
- na_ontap_portset - fixed error when trying to remove partial ports from portset if igroups are bound to it.
- na_ontap_portset - fixed idempotency issue when ``ports`` has identical values.
- na_ontap_quotas - fix another quota operation is currently in progress issue.
- na_ontap_quotas - fix idempotency issue on ``threshold`` option.
- na_ontap_service_policy - fixed error in modify by changing resulting json of an existing record in REST.
- na_ontap_snapmirror - fix error in snapmirror restore by changing option ``clean_up_failure`` as optional when using ZAPI.
- na_ontap_snapmirror - fix issues where there was no wait on quiesce before aborting.
- na_ontap_snapmirror - fix issues where there was no wait on the relationship to end transferring.
- na_ontap_snapmirror - support for SSL certificate authentication for both sides when using ONTAP.
- na_ontap_snapmirror - when using REST with a policy, fix AttributeError - 'str' object has no attribute 'get'.
- na_ontap_snapmirror - when using ZAPI, wait for the relationship to be quiesced before breaking.
- na_ontap_software_update - now reports changed=False when the package is already present.
- na_ontap_user - fix idempotency issue with SSH with second_authentication_method.
- na_ontap_vscan_on_access_policy - fixed options ``filters``, ``file_ext_to_exclude`` and ``paths_to_exclude`` cannot be reset to empty values in ZAPI.
- na_ontap_zapit - fix failure in precluster mode.

ovirt.ovirt
~~~~~~~~~~~

- hosted_engine_setup - Fix "'ansible' ModuleNotFoundError" in Disaster Recovery scripts (https://github.com/oVirt/ovirt-ansible-collection/pull/503).
- hosted_engine_setup - Use command instead of firewalld module (https://github.com/oVirt/ovirt-ansible-collection/pull/508).
- ovirt_vm - Fix parsing None arguments (https://github.com/oVirt/ovirt-ansible-collection/pull/486).
- ovirt_vm - check if the snapshot exists (https://github.com/oVirt/ovirt-ansible-collection/pull/525).

vmware.vmware_rest
~~~~~~~~~~~~~~~~~~

- vcenter_datacenter - Ensure the idempotency works as expected.

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
- ome_device_power_settings - Issue(212679) - The module displays the following message if the value provided for the parameter ``power_cap`` is not within the supported range of 0 to 32767, ``Unable to complete the request because PowerCap does not exist or is not applicable for the resource URI.``
- ome_device_quick_deploy - Issue(216352) - The module does not display a proper error message if an unsupported value is provided for the ipv6_prefix_length and vlan_id parameters.
- ome_smart_fabric_uplink - Issue(186024) - The module does not allow the creation of multiple uplinks of the same name even though it is supported by OpenManage Enterprise Modular. If an uplink is created using the same name as an existing uplink, the existing uplink is modified.

New Modules
-----------

community.aws
~~~~~~~~~~~~~

- community.aws.aws_api_gateway_domain - Manage AWS API Gateway custom domains

community.general
~~~~~~~~~~~~~~~~~

Cloud
^^^^^

Scaleway
........

- community.general.scaleway_compute_private_network - Scaleway compute - private network management

System
^^^^^^

- community.general.gconftool2_info - Retrieve GConf configurations
- community.general.keyring - Set or delete a passphrase using the Operating System's native keyring
- community.general.keyring_info - Get a passphrase using the Operating System's native keyring

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- dellemc.openmanage.idrac_certificates - Configure certificates for iDRAC.

hetzner.hcloud
~~~~~~~~~~~~~~

Hetzner
^^^^^^^

Hcloud
......

- hetzner.hcloud.hcloud_primary_ip - Create and manage cloud Primary IPs on the Hetzner Cloud.

netapp.ontap
~~~~~~~~~~~~

- netapp.ontap.na_ontap_s3_services - NetApp ONTAP S3 services
- netapp.ontap.na_ontap_s3_users - NetApp ONTAP S3 users

vmware.vmware_rest
~~~~~~~~~~~~~~~~~~

- vmware.vmware_rest.vcenter_vmtemplate_libraryitems - Creates a library item in content library from a virtual machine
- vmware.vmware_rest.vcenter_vmtemplate_libraryitems_info - Returns information about a virtual machine template contained in the library item specified by {@param.name templateLibraryItem}

Unchanged Collections
---------------------

- ansible.netcommon (still version 3.0.1)
- ansible.posix (still version 1.4.0)
- ansible.utils (still version 2.6.1)
- ansible.windows (still version 1.10.0)
- arista.eos (still version 5.0.1)
- check_point.mgmt (still version 2.3.0)
- cisco.aci (still version 2.2.0)
- cisco.intersight (still version 1.0.19)
- cisco.mso (still version 2.0.0)
- cisco.nso (still version 1.0.3)
- cisco.ucs (still version 1.8.0)
- cloudscale_ch.cloud (still version 2.2.2)
- community.azure (still version 1.1.0)
- community.ciscosmb (still version 1.0.5)
- community.fortios (still version 1.0.0)
- community.google (still version 1.0.0)
- community.hashi_vault (still version 3.0.0)
- community.libvirt (still version 1.1.0)
- community.network (still version 4.0.1)
- community.okd (still version 2.2.0)
- community.postgresql (still version 2.1.5)
- community.proxysql (still version 1.4.0)
- community.rabbitmq (still version 1.2.1)
- community.routeros (still version 2.1.0)
- community.sap (still version 1.0.0)
- community.sap_libs (still version 1.1.0)
- community.skydive (still version 1.0.0)
- community.windows (still version 1.10.0)
- community.zabbix (still version 1.7.0)
- cyberark.conjur (still version 1.1.0)
- cyberark.pas (still version 1.0.14)
- dellemc.enterprise_sonic (still version 1.1.1)
- dellemc.os10 (still version 1.1.1)
- dellemc.os6 (still version 1.0.7)
- dellemc.os9 (still version 1.0.4)
- fortinet.fortimanager (still version 2.1.5)
- fortinet.fortios (still version 2.1.6)
- frr.frr (still version 2.0.0)
- gluster.gluster (still version 1.0.2)
- google.cloud (still version 1.0.2)
- hpe.nimble (still version 1.1.4)
- ibm.qradar (still version 2.0.0)
- infinidat.infinibox (still version 1.3.3)
- inspur.sm (still version 2.0.0)
- mellanox.onyx (still version 1.0.0)
- netapp.aws (still version 21.7.0)
- netapp.azure (still version 21.10.0)
- netapp.elementsw (still version 21.7.0)
- netapp.storagegrid (still version 21.10.0)
- netapp.um_info (still version 21.8.0)
- netapp_eseries.santricity (still version 1.3.0)
- netbox.netbox (still version 3.7.1)
- ngine_io.cloudstack (still version 2.2.4)
- ngine_io.exoscale (still version 1.0.0)
- openstack.cloud (still version 1.8.0)
- openvswitch.openvswitch (still version 2.1.0)
- purestorage.flasharray (still version 1.13.0)
- purestorage.flashblade (still version 1.9.0)
- sensu.sensu_go (still version 1.13.1)
- servicenow.servicenow (still version 1.0.6)
- splunk.es (still version 2.0.0)
- theforeman.foreman (still version 3.4.0)
- vyos.vyos (still version 3.0.1)

v6.0.0
======

.. contents::
  :local:
  :depth: 2

Release Summary
---------------

Release Date: 2022-06-21

`Porting Guide <https://docs.ansible.com/ansible/devel/porting_guides.html>`_

Removed Collections
-------------------

- community.kubernetes (previously included version: 2.0.1)
- community.kubevirt (previously included version: 1.0.0)

Added Collections
-----------------

- cisco.dnac (version 6.4.0)
- community.sap (version 1.0.0)
- community.sap_libs (version 1.1.0)
- vmware.vmware_rest (version 2.1.5)

Ansible-core
------------

Ansible 6.0.0 contains Ansible-core version 2.13.0.
This is a newer version than version 2.12.0 contained in the previous Ansible release.

The changes are reported in the combined changelog below.

Included Collections
--------------------

If not mentioned explicitly, the changes are reported in the combined changelog below.

+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| Collection                    | Ansible 5.0.0 | Ansible 6.0.0 | Notes                                                                                                                        |
+===============================+===============+===============+==============================================================================================================================+
| amazon.aws                    | 2.1.0         | 3.2.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| ansible.netcommon             | 2.4.0         | 3.0.1         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| ansible.posix                 | 1.3.0         | 1.4.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| ansible.utils                 | 2.4.2         | 2.6.1         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| ansible.windows               | 1.8.0         | 1.10.0        |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| arista.eos                    | 3.1.0         | 5.0.1         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| awx.awx                       | 19.4.0        | 21.0.0        | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| azure.azcollection            | 1.10.0        | 1.12.0        | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| check_point.mgmt              | 2.1.1         | 2.3.0         | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| chocolatey.chocolatey         | 1.1.0         | 1.2.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.aci                     | 2.1.0         | 2.2.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.asa                     | 2.1.0         | 3.0.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.dnac                    |               | 6.4.0         | The collection was added to Ansible                                                                                          |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.intersight              | 1.0.17        | 1.0.19        | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.ios                     | 2.5.0         | 3.0.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.iosxr                   | 2.5.0         | 3.0.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.ise                     | 1.2.1         | 2.4.1         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.meraki                  | 2.5.0         | 2.6.2         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.mso                     | 1.2.0         | 2.0.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.nxos                    | 2.7.1         | 3.0.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cisco.ucs                     | 1.6.0         | 1.8.0         | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cloud.common                  | 2.1.0         | 2.1.1         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cloudscale_ch.cloud           | 2.2.0         | 2.2.2         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.aws                 | 2.1.0         | 3.2.1         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.ciscosmb            | 1.0.4         | 1.0.5         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.crypto              | 2.0.1         | 2.3.2         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.digitalocean        | 1.12.0        | 1.19.0        |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.dns                 | 2.0.3         | 2.1.1         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.docker              | 2.0.1         | 2.6.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.general             | 4.0.2         | 5.0.2         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.grafana             | 1.2.3         | 1.4.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.hashi_vault         | 2.0.0         | 3.0.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.hrobot              | 1.2.1         | 1.3.1         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.libvirt             | 1.0.2         | 1.1.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.mongodb             | 1.3.2         | 1.4.0         | There are no changes recorded in the changelog.                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.mysql               | 2.3.1         | 3.2.1         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.network             | 3.0.0         | 4.0.1         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.okd                 | 2.1.0         | 2.2.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.postgresql          | 1.5.0         | 2.1.5         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.proxysql            | 1.3.0         | 1.4.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.rabbitmq            | 1.1.0         | 1.2.1         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.routeros            | 2.0.0         | 2.1.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.sap                 |               | 1.0.0         | The collection was added to Ansible                                                                                          |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.sap_libs            |               | 1.1.0         | The collection was added to Ansible                                                                                          |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.sops                | 1.2.0         | 1.2.2         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.vmware              | 1.16.0        | 2.5.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.windows             | 1.8.0         | 1.10.0        |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.zabbix              | 1.5.0         | 1.7.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| containers.podman             | 1.8.2         | 1.9.3         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| cyberark.pas                  | 1.0.13        | 1.0.14        | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| dellemc.enterprise_sonic      | 1.1.0         | 1.1.1         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| dellemc.openmanage            | 4.2.0         | 5.4.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| f5networks.f5_modules         | 1.12.0        | 1.17.0        |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| fortinet.fortimanager         | 2.1.4         | 2.1.5         | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| fortinet.fortios              | 2.1.3         | 2.1.6         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| frr.frr                       | 1.0.3         | 2.0.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| hpe.nimble                    | 1.1.3         | 1.1.4         | The collection did not have a changelog in this version.                                                                     |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| ibm.qradar                    | 1.0.3         | 2.0.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| infinidat.infinibox           | 1.3.0         | 1.3.3         | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| infoblox.nios_modules         | 1.1.2         | 1.2.2         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| inspur.sm                     | 1.3.0         | 2.0.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| junipernetworks.junos         | 2.6.0         | 3.0.1         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| kubernetes.core               | 2.2.1         | 2.3.1         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| netapp.cloudmanager           | 21.12.0       | 21.17.0       |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| netapp.ontap                  | 21.13.1       | 21.19.1       |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| netapp.storagegrid            | 21.7.0        | 21.10.0       |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| netapp_eseries.santricity     | 1.2.13        | 1.3.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| netbox.netbox                 | 3.3.0         | 3.7.1         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| ngine_io.cloudstack           | 2.2.2         | 2.2.4         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| ngine_io.vultr                | 1.1.0         | 1.1.1         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| openstack.cloud               | 1.5.3         | 1.8.0         | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| openvswitch.openvswitch       | 2.0.2         | 2.1.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| ovirt.ovirt                   | 1.6.5         | 2.0.4         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| purestorage.flasharray        | 1.11.0        | 1.13.0        |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| purestorage.flashblade        | 1.8.1         | 1.9.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| sensu.sensu_go                | 1.12.0        | 1.13.1        |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| splunk.es                     | 1.0.2         | 2.0.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| t_systems_mms.icinga_director | 1.24.0        | 1.29.0        |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| theforeman.foreman            | 2.2.0         | 3.4.0         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| vmware.vmware_rest            |               | 2.1.5         | The collection was added to Ansible                                                                                          |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| vyos.vyos                     | 2.6.0         | 3.0.1         |                                                                                                                              |
+-------------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+

Major Changes
-------------

- Add a ``ansible-community`` CLI tool that allows to print the version of the Ansible community distribution. Use ``ansible-community --version`` to print this version.

Ansible-core
~~~~~~~~~~~~

- Jinja2 Controller Requirement - Jinja2 3.0.0 or newer is required for the control node (the machine that runs Ansible) (https://github.com/ansible/ansible/pull/75881)
- Templating - remove ``safe_eval`` in favor of using ``NativeEnvironment`` but utilizing ``literal_eval`` only in cases when ``safe_eval`` was used (https://github.com/ansible/ansible/pull/75587)

amazon.aws
~~~~~~~~~~

- amazon.aws collection - The amazon.aws collection has dropped support for ``botocore<1.19.0`` and ``boto3<1.16.0``. Most modules will continue to work with older versions of the AWS SDK, however compatability with older versions of the SDK is not guaranteed and will not be tested. When using older versions of the SDK a warning will be emitted by Ansible (https://github.com/ansible-collections/amazon.aws/pull/574).

ansible.netcommon
~~~~~~~~~~~~~~~~~

- cli_parse - this module has been moved to the ansible.utils collection. ``ansible.netcommon.cli_parse`` will continue to work to reference the module in its new location, but this redirect will be removed in a future release
- network_cli - Change default value of `ssh_type` option from `paramiko` to `auto`. This value will use libssh if the ansible-pylibssh module is installed, otherwise will fallback to paramiko.

arista.eos
~~~~~~~~~~

- Minimum required ansible.netcommon version is 2.5.1.
- Updated base plugin references to ansible.netcommon.
- `eos_facts` - change default gather_subset to `min` from `!config` (https://github.com/ansible-collections/arista.eos/issues/306).

chocolatey.chocolatey
~~~~~~~~~~~~~~~~~~~~~

- win_chocolatey - Added choco_args option to pass additional arguments directly to Chocolatey.

cisco.asa
~~~~~~~~~

- Minimum required ansible.netcommon version is 2.5.1.
- Updated base plugin references to ansible.netcommon.

cisco.ios
~~~~~~~~~

- Minimum required ansible.netcommon version is 2.5.1.
- Updated base plugin references to ansible.netcommon.
- `facts` - default value for `gather_subset` is changed to min instead of !config.

cisco.iosxr
~~~~~~~~~~~

- Minimum required ansible.netcommon version is 2.5.1.
- Updated base plugin references to ansible.netcommon.
- `facts` - default value for `gather_subset` is changed to min instead of !config.

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

cisco.nxos
~~~~~~~~~~

- The minimum required ansible.netcommon version has been bumped to v2.6.1.
- Updated base plugin references to ansible.netcommon.
- `nxos_facts` - change default gather_subset to `min` from `!config` (https://github.com/ansible-collections/cisco.nxos/issues/418).
- nxos_file_copy has been rewritten as a module. This change also removes the dependency on pexpect for file_pull operation. Since this now uses AnsibleModule class for argspec validation, the validation messages will be slighlty different. Expect changes in the return payload in some cases. All functionality remains unchanged.

community.aws
~~~~~~~~~~~~~

- community.aws collection - The community.aws collection has dropped support for ``botocore<1.19.0`` and ``boto3<1.16.0``. Most modules will continue to work with older versions of the AWS SDK, however compatability with older versions of the SDK is not guaranteed and will not be tested. When using older versions of the SDK a warning will be emitted by Ansible (https://github.com/ansible-collections/community.aws/pull/809).
- s3_bucket_notifications - refactor module to support SNS / SQS targets as well as the existing support for Lambda functions (https://github.com/ansible-collections/community.aws/issues/140).

community.general
~~~~~~~~~~~~~~~~~

- The community.general collection no longer supports Ansible 2.9 and ansible-base 2.10. While we take no active measures to prevent usage, we will remove a lot of compatibility code and other compatility measures that will effectively prevent using most content from this collection with Ansible 2.9, and some content of this collection with ansible-base 2.10. Both Ansible 2.9 and ansible-base 2.10 will very soon be End of Life and if you are still using them, you should consider upgrading to ansible-core 2.11 or later as soon as possible (https://github.com/ansible-collections/community.general/pull/4548).

community.mysql
~~~~~~~~~~~~~~~

- The community.mysql collection no longer supports ``Ansible 2.9`` and ``ansible-base 2.10``. While we take no active measures to prevent usage and there are no plans to introduce incompatible code to the modules, we will stop testing against ``Ansible 2.9`` and ``ansible-base 2.10``. Both will very soon be End of Life and if you are still using them, you should consider upgrading to the ``latest Ansible / ansible-core 2.11 or later`` as soon as possible (https://github.com/ansible-collections/community.mysql/pull/343).

community.network
~~~~~~~~~~~~~~~~~

- The community.network collection no longer supports Ansible 2.9 and ansible-base 2.10. While we take no active measures to prevent usage, we will remove compatibility code and other compatility measures that will effectively prevent using most content from this collection with Ansible 2.9, and some content of this collection with ansible-base 2.10. Both Ansible 2.9 and ansible-base 2.10 will very soon be End of Life and if you are still using them, you should consider upgrading to ansible-core 2.11 or later as soon as possible (https://github.com/ansible-collections/community.network/pull/426).

community.postgresql
~~~~~~~~~~~~~~~~~~~~

- The community.postgresql collection no longer supports ``Ansible 2.9`` and ``ansible-base 2.10``. While we take no active measures to prevent usage and there are no plans to introduce incompatible code to the modules, we will stop testing against ``Ansible 2.9`` and ``ansible-base 2.10``. Both will very soon be End of Life and if you are still using them, you should consider upgrading to the ``latest Ansible / ansible-core 2.11 or later`` as soon as possible (https://github.com/ansible-collections/community.postgresql/pull/245).
- postgresql_privs - the ``usage_on_types`` feature have been deprecated and will be removed in ``community.postgresql 3.0.0``. Please use the ``type`` option with the ``type`` value to explicitly grant/revoke privileges on types (https://github.com/ansible-collections/community.postgresql/issues/207).
- postgresql_query - the ``path_to_script`` and ``as_single_query`` options as well as the ``query_list`` and ``query_all_results`` return values have been deprecated and will be removed in ``community.postgresql 3.0.0``. Please use the ``community.postgresql.postgresql_script`` module to execute statements from scripts (https://github.com/ansible-collections/community.postgresql/issues/189).
- postgresql_query - the default value of the ``as_single_query`` option changes to ``yes``. If the related behavior of your tasks where the module is involved changes, please adjust the parameter's value correspondingly (https://github.com/ansible-collections/community.postgresql/issues/85).
- postgresql_user - the ``priv`` argument has been deprecated and will be removed in ``community.postgresql 3.0.0``. Please use the ``postgresql_privs`` module to grant/revoke privileges instead (https://github.com/ansible-collections/community.postgresql/issues/212).

community.vmware
~~~~~~~~~~~~~~~~

- Drop VCSIM as a test target (https://github.com/ansible-collections/community.vmware/pull/1294).

containers.podman
~~~~~~~~~~~~~~~~~

- Add podman_tag module
- Add secrets driver and driver opts support

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- All modules can read custom or organizational CA signed certificate from the environment variables. Please refer to `SSL Certificate Validation <https://github.com/dell/dellemc-openmanage-ansible-modules#ssl-certificate-validation>`_ section in the `README.md <https://github.com/dell/dellemc-openmanage-ansible-modules/blob/collections/README.md#SSL-Certificate-Validation>`_ for modification to existing playbooks or setting environment variable.
- All modules now support SSL over HTTPS and socket level timeout.
- idrac_server_config_profile - The module is enhanced to support export, import, and preview the SCP configuration using Redfish and added support for check mode.

f5networks.f5_modules
~~~~~~~~~~~~~~~~~~~~~

- bigip_device_info - pagination logic has also been added to help with api stability.
- bigip_device_info - the module no longer gathers information from all partitions on device. This change will stabalize the module by gathering resources only from the given partition and prevent the module from gathering way too much information that might result in crashing.

fortinet.fortios
~~~~~~~~~~~~~~~~

- Support FortiOS 7.0.2, 7.0.3, 7.0.4, 7.0.5.

frr.frr
~~~~~~~

- Minimum required ansible.netcommon version is 2.5.1.
- Updated base plugin references to ansible.netcommon.

ibm.qradar
~~~~~~~~~~

- Minimum required ansible.netcommon version is 2.5.1.
- Updated base plugin references to ansible.netcommon.

junipernetworks.junos
~~~~~~~~~~~~~~~~~~~~~

- Minimum required ansible.netcommon version is 2.5.1.
- Updated base plugin references to ansible.netcommon.
- `junos_facts` - change default gather_subset to `min` from `!config`.

ovirt.ovirt
~~~~~~~~~~~

- manageiq - role removed (https://github.com/oVirt/ovirt-ansible-collection/pull/375).

splunk.es
~~~~~~~~~

- Minimum required ansible.netcommon version is 2.5.1.
- Updated base plugin references to ansible.netcommon.

vyos.vyos
~~~~~~~~~

- Add 'pool' as value to server key in ntp_global.
- Minimum required ansible.netcommon version is 2.5.1.
- Updated base plugin references to ansible.netcommon.
- `vyos_facts` - change default gather_subset to `min` from `!config` (https://github.com/ansible-collections/vyos.vyos/issues/231).

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
- ansible-test - Update ``default`` containers to version 5.9.0.
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

ansible.posix
~~~~~~~~~~~~~

- firewalld - Show warning message that variable type of ``masquerade`` and ``icmp_block_inversion`` will be changed from ``str`` to ``boolean`` in the future release (https://github.com/ansible-collections/ansible.posix/pull/254).
- selinux - optionally update kernel boot params when disabling/re-enabling SELinux (https://github.com/ansible-collections/ansible.posix/pull/142).

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

- setup - Added ipv4, ipv6, mtu and speed data to ansible_interfaces
- win_dsc - deduplicated error writing code with a new function. No actual error text was changed.
- win_environment - Trigger ``WM_SETTINGCHANGE`` on a change to notify other host processes of an environment change
- win_path - Migrate to newer style module parser that adds features like module invocation under ``-vvv``
- win_path - Trigger ``WM_SETTINGCHANGE`` on a change to notify other host processes of an environment change
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
- Add new keys ge, eq, le for iosxr_prefix_lists.
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
- pxGrid_node_approve - new module
- pxGrid_node_delete - new module
- pxGrid_node_info - new module
- pxGrid_settings_auto_approve - new module
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

- Add execution-environment.yml in meta as the base to a Meraki ee
- meraki_mx_l7_firewall - Allow passing an empty ruleset to delete all rules
- meraki_network - Add Products to net_type list
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
- `nxos_snmp_server` - add support for BGP, OSPF and OSPFv3 traps.

cloud.common
~~~~~~~~~~~~

- Move the content of README_ansible_turbo.module.rst in the main README.md to get visibility on Ansible Galaxy.

cloudscale_ch.cloud
~~~~~~~~~~~~~~~~~~~

- Fixed inventory documentation.
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
- elb_instance - ``wait`` parameter is no longer ignored (https://github.com/ansible-collections/community.aws/pull/826)
- elb_target_group - add support for alb target_type and update documentation (https://github.com/ansible-collections/community.aws/pull/966).
- elb_target_group - add support for parameter ``deregistration_connection_termination`` (https://github.com/ansible-collections/community.aws/pull/913).
- elb_target_group - add support for setting load_balancing_algorithm_type (https://github.com/ansible-collections/community.aws/pull/1016).
- iam_managed_policy - refactor module adding ``check_mode`` and better AWSRetry backoff logic (https://github.com/ansible-collections/community.aws/pull/893).
- iam_role - delete inline policies prior to deleting role (https://github.com/ansible-collections/community.aws/pull/1054).
- iam_role - remove global vars and refactor accordingly (https://github.com/ansible-collections/community.aws/pull/1054).
- iam_user - add boto3 waiter for iam user creation (https://github.com/ansible-collections/community.aws/pull/822).
- iam_user - add parameter ``password_reset_required`` (https://github.com/ansible-collections/community.aws/pull/860).
- iam_user - add password management support bringing parity with ``iam`` module (https://github.com/ansible-collections/community.aws/pull/822).
- rds_instance - add ``choices`` for valid engine value (https://github.com/ansible-collections/community.aws/pull/1034).
- rds_subnet_group - add ``check_mode`` (https://github.com/ansible-collections/community.aws/pull/562).
- rds_subnet_group - add ``tags`` feature (https://github.com/ansible-collections/community.aws/pull/562).
- route53 - ``ttl``  and ``value`` are not required for deleting records (https://github.com/ansible-collections/community.aws/pull/801).
- route53_info - ``max_items`` and ``type`` are no longer ignored fixing a regression (https://github.com/ansible-collections/community.aws/pull/813).
- s3_lifecycle - Add ``abort_incomplete_multipart_upload_days`` and ``expire_object_delete_marker`` parameters (https://github.com/ansible-collections/community.aws/pull/794).
- wafv2_web_acl - Documentation updates wafv2_web_acl and aws_waf_web_acl (https://github.com/ansible-collections/community.aws/pull/721).
- wafv2_web_acl - Extended the wafv2_web_acl module to also take the ``custom_response_bodies`` argument (https://github.com/ansible-collections/community.aws/pull/721).

community.ciscosmb
~~~~~~~~~~~~~~~~~~

- CI  change <plugin_type> <name> to name <name> for validate-module
- CI - add ansible 2.13 to test matrix

community.crypto
~~~~~~~~~~~~~~~~

- Adjust error messages that indicate ``cryptography`` is not installed from ``Can't`` to ``Cannot`` (https://github.com/ansible-collections/community.crypto/pull/374).
- Prepare collection for inclusion in an Execution Environment by declaring its dependencies. Please note that system packages are used for cryptography and PyOpenSSL, which can be rather limited. If you need features from newer cryptography versions, you will have to manually force a newer version to be installed by pip by specifying something like ``cryptography >= 37.0.0`` in your Execution Environment's Python dependencies file (https://github.com/ansible-collections/community.crypto/pull/440).
- Support automatic conversion for Internalionalized Domain Names (IDNs). When passing general names, for example Subject Altenative Names to ``community.crypto.openssl_csr``, these will automatically be converted to IDNA. Conversion will be done per label to IDNA2008 if possible, and IDNA2003 if IDNA2008 conversion fails for that label. Note that IDNA conversion requires `the Python idna library <https://pypi.org/project/idna/>`_ to be installed. Please note that depending on which versions of the cryptography library are used, it could try to process the converted IDNA another time with the Python ``idna`` library and reject IDNA2003 encoded values. Using a new enough ``cryptography`` version avoids this (https://github.com/ansible-collections/community.crypto/issues/426, https://github.com/ansible-collections/community.crypto/pull/436).
- acme_* modules - add parameter ``request_timeout`` to manage HTTP(S) request timeout (https://github.com/ansible-collections/community.crypto/issues/447, https://github.com/ansible-collections/community.crypto/pull/448).
- luks_devices - added ``perf_same_cpu_crypt``, ``perf_submit_from_crypt_cpus``, ``perf_no_read_workqueue``, ``perf_no_write_workqueue`` for performance tuning when opening LUKS2 containers (https://github.com/ansible-collections/community.crypto/issues/427).
- luks_devices - added ``persistent`` option when opening LUKS2 containers (https://github.com/ansible-collections/community.crypto/pull/434).
- openssh_cert - added ``ignore_timestamps`` parameter so it can be used semi-idempotent with relative timestamps in ``valid_to``/``valid_from`` (https://github.com/ansible-collections/community.crypto/issues/379).
- openssl_csr_info - add ``name_encoding`` option to control the encoding (IDNA, Unicode) used to return domain names in general names (https://github.com/ansible-collections/community.crypto/pull/436).
- openssl_pkcs12 - allow to provide the private key as text instead of having to read it from a file. This allows to store the private key in an encrypted form, for example in Ansible Vault (https://github.com/ansible-collections/community.crypto/pull/452).
- x509_certificate_info - add ``name_encoding`` option to control the encoding (IDNA, Unicode) used to return domain names in general names (https://github.com/ansible-collections/community.crypto/pull/436).
- x509_crl - add ``name_encoding`` option to control the encoding (IDNA, Unicode) used to return domain names in general names (https://github.com/ansible-collections/community.crypto/pull/436).
- x509_crl_info - add ``name_encoding`` option to control the encoding (IDNA, Unicode) used to return domain names in general names (https://github.com/ansible-collections/community.crypto/pull/436).

community.digitalocean
~~~~~~~~~~~~~~~~~~~~~~

- Set Python 3.9 as the C(python-version) and C(target-python-version) in the integration, sanity, and unit tests for Ansible > 2.9 (3.8 otherwise).
- Updates DigitalOcean API documentation links to current domain with working URL anchors (https://github.com/ansible-collections/community.digitalocean/issues/223).
- black test - added a 15 minute timeout (https://github.com/ansible-collections/community.digitalocean/issues/228).
- ci - adding stable-2.13 to sanity and unit testing (https://github.com/ansible-collections/community.digitalocean/issues/239).
- digital_ocean - parameterize the DigitalOcean API base url (https://github.com/ansible-collections/community.digitalocean/issues/237).
- digital_ocean - reference C(DO_API_TOKEN) consistently in module documentation and examples (https://github.com/ansible-collections/community.digitalocean/issues/248).
- digital_ocean_domain - add support for IPv6 apex domain records (https://github.com/ansible-collections/community.digitalocean/issues/226).
- digital_ocean_droplet - allow the user to override the Droplet action and status polling interval (https://github.com/ansible-collections/community.digitalocean/issues/194).
- digital_ocean_kubernetes - adding support for HA control plane (https://github.com/ansible-collections/community.digitalocean/issues/190).
- digital_ocean_kubernetes_info - switching C(changed=True) to C(changed=False) since getting information is read-only in nature (https://github.com/ansible-collections/community.digitalocean/issues/204).
- digital_ocean_spaces - set C(no_log=True) for C(aws_access_key_id) parameter (https://github.com/ansible-collections/community.digitalocean/issues/243).
- digital_ocean_spaces_info - set C(no_log=True) for C(aws_access_key_id) parameter (https://github.com/ansible-collections/community.digitalocean/issues/243).
- integration tests - added a 120 minute timeout (https://github.com/ansible-collections/community.digitalocean/issues/228).
- sanity and unit tests - added a 30 minute timeout (https://github.com/ansible-collections/community.digitalocean/issues/228).

community.dns
~~~~~~~~~~~~~

- Prepare collection for inclusion in an Execution Environment by declaring its dependencies (https://github.com/ansible-collections/community.dns/pull/93).

community.docker
~~~~~~~~~~~~~~~~

- Prepare collection for inclusion in an Execution Environment by declaring its dependencies. The ``docker_stack*`` modules are not supported (https://github.com/ansible-collections/community.docker/pull/336).
- current_container_facts - add detection for GitHub Actions (https://github.com/ansible-collections/community.docker/pull/336).
- docker connection plugin - implement connection reset by clearing internal container user cache (https://github.com/ansible-collections/community.docker/pull/312).
- docker connection plugin - simplify ``actual_user`` handling code (https://github.com/ansible-collections/community.docker/pull/311).
- docker connection plugin - the plugin supports new ways to define the timeout. These are the ``ANSIBLE_DOCKER_TIMEOUT`` environment variable, the ``timeout`` setting in the ``docker_connection`` section of ``ansible.cfg``, and the ``ansible_docker_timeout`` variable (https://github.com/ansible-collections/community.docker/pull/297).
- docker_api connection plugin - implement connection reset by clearing internal container user/group ID cache (https://github.com/ansible-collections/community.docker/pull/312).
- docker_api connection plugin - the plugin supports new ways to define the timeout. These are the ``ANSIBLE_DOCKER_TIMEOUT`` environment variable, the ``timeout`` setting in the ``docker_connection`` section of ``ansible.cfg``, and the ``ansible_docker_timeout`` variable (https://github.com/ansible-collections/community.docker/pull/308).
- docker_config - add support for ``template_driver`` with one option ``golang`` (https://github.com/ansible-collections/community.docker/issues/332, https://github.com/ansible-collections/community.docker/pull/345).
- docker_config - add support for rolling update, set ``rolling_versions`` to ``true`` to enable (https://github.com/ansible-collections/community.docker/pull/295, https://github.com/ansible-collections/community.docker/issues/109).
- docker_container - added ``image_label_mismatch`` parameter (https://github.com/ansible-collections/community.docker/issues/314, https://github.com/ansible-collections/community.docker/pull/370).
- docker_container - support returning Docker container log output when using Docker's ``local`` logging driver, an optimized local logging driver introduced in Docker 18.09 (https://github.com/ansible-collections/community.docker/pull/337).
- docker_container_exec - add ``detach`` parameter (https://github.com/ansible-collections/community.docker/issues/250, https://github.com/ansible-collections/community.docker/pull/255).
- docker_container_exec - add ``env`` option (https://github.com/ansible-collections/community.docker/issues/248, https://github.com/ansible-collections/community.docker/pull/254).
- docker_secret - add support for rolling update, set ``rolling_versions`` to ``true`` to enable (https://github.com/ansible-collections/community.docker/pull/293, https://github.com/ansible-collections/community.docker/issues/21).
- docker_swarm - adds ``data_path_addr`` parameter during swarm initialization or when joining (https://github.com/ansible-collections/community.docker/issues/339).
- docker_swarm_service - add support for setting capabilities with the ``cap_add`` and ``cap_drop`` parameters. Usage is the same as with the ``capabilities`` and ``cap_drop`` parameters for ``docker_container`` (https://github.com/ansible-collections/community.docker/pull/294).

community.general
~~~~~~~~~~~~~~~~~

- Avoid internal ansible-core module_utils in favor of equivalent public API available since at least Ansible 2.9. This fixes some instances added since the last time this was fixed (https://github.com/ansible-collections/community.general/pull/4232).
- ModuleHelper module utils - ``ModuleHelperBase` now delegates the attributes ``check_mode``, ``get_bin_path``, ``warn``, and ``deprecate`` to the underlying ``AnsibleModule`` instance (https://github.com/ansible-collections/community.general/pull/4600).
- ModuleHelper module utils - ``ModuleHelperBase`` now has a convenience method ``do_raise`` (https://github.com/ansible-collections/community.general/pull/4660).
- Remove vendored copy of ``distutils.version`` in favor of vendored copy included with ansible-core 2.12+. For ansible-core 2.11, uses ``distutils.version`` for Python < 3.12. There is no support for ansible-core 2.11 with Python 3.12+ (https://github.com/ansible-collections/community.general/pull/3988).
- aix_filesystem - calling ``run_command`` with arguments as ``list`` instead of ``str`` (https://github.com/ansible-collections/community.general/pull/3833).
- aix_lvg - calling ``run_command`` with arguments as ``list`` instead of ``str`` (https://github.com/ansible-collections/community.general/pull/3834).
- alternatives - add ``state`` parameter, which provides control over whether the alternative should be set as the active selection for its alternatives group (https://github.com/ansible-collections/community.general/issues/4543, https://github.com/ansible-collections/community.general/pull/4557).
- ansible_galaxy_install - added option ``no_deps`` to the module (https://github.com/ansible-collections/community.general/issues/4174).
- atomic_container - minor refactoring (https://github.com/ansible-collections/community.general/pull/4567).
- clc_alert_policy - minor refactoring (https://github.com/ansible-collections/community.general/pull/4556).
- clc_group - minor refactoring (https://github.com/ansible-collections/community.general/pull/4556).
- clc_loadbalancer - minor refactoring (https://github.com/ansible-collections/community.general/pull/4556).
- clc_server - minor refactoring (https://github.com/ansible-collections/community.general/pull/4556).
- cmd_runner module util - reusable command runner with consistent argument formatting and sensible defaults (https://github.com/ansible-collections/community.general/pull/4476).
- cobbler inventory plugin - add ``include_profiles`` option (https://github.com/ansible-collections/community.general/pull/4068).
- cpanm - using ``do_raise()`` to raise exceptions in ``ModuleHelper`` derived modules (https://github.com/ansible-collections/community.general/pull/4674).
- datadog_monitor - support new datadog event monitor of type `event-v2 alert` (https://github.com/ansible-collections/community.general/pull/4457)
- filesystem - add support for resizing btrfs (https://github.com/ansible-collections/community.general/issues/4465).
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
- ipa_dnsrecord - add new argument ``record_values``, mutually exclusive to ``record_value``, which supports multiple values for one record (https://github.com/ansible-collections/community.general/pull/4578).
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
- lxd_container - adds ``project`` option to allow selecting project for LXD instance (https://github.com/ansible-collections/community.general/pull/4479).
- lxd_container - adds ``type`` option which also allows to operate on virtual machines and not just containers (https://github.com/ansible-collections/community.general/pull/3661).
- lxd_profile - adds ``project`` option to allow selecting project for LXD profile (https://github.com/ansible-collections/community.general/pull/4479).
- mail callback plugin - add ``Message-ID`` and ``Date`` headers (https://github.com/ansible-collections/community.general/issues/4055, https://github.com/ansible-collections/community.general/pull/4056).
- mail callback plugin - properly use Ansible's option handling to split lists (https://github.com/ansible-collections/community.general/pull/4140).
- mattermost - add the possibility to send attachments instead of text messages (https://github.com/ansible-collections/community.general/pull/3946).
- mksysb - revamped the module using ``ModuleHelper`` (https://github.com/ansible-collections/community.general/pull/3295).
- mksysb - using ``do_raise()`` to raise exceptions in ``ModuleHelper`` derived modules (https://github.com/ansible-collections/community.general/pull/4674).
- module_helper module utils - added decorators ``check_mode_skip`` and ``check_mode_skip_returns`` for skipping methods when ``check_mode=True`` (https://github.com/ansible-collections/community.general/pull/3849).
- monit - calling ``run_command`` with arguments as ``list`` instead of ``str`` (https://github.com/ansible-collections/community.general/pull/3821).
- nmap inventory plugin - add ``sudo`` option in plugin in order to execute ``sudo nmap`` so that ``nmap`` runs with elevated privileges (https://github.com/ansible-collections/community.general/pull/4506).
- nmcli - add ``wireguard`` connection type (https://github.com/ansible-collections/community.general/pull/3985).
- nmcli - add missing connection aliases ``802-3-ethernet`` and ``802-11-wireless`` (https://github.com/ansible-collections/community.general/pull/4108).
- nmcli - add multiple addresses support for ``ip4`` parameter (https://github.com/ansible-collections/community.general/issues/1088, https://github.com/ansible-collections/community.general/pull/3738).
- nmcli - add multiple addresses support for ``ip6`` parameter (https://github.com/ansible-collections/community.general/issues/1088).
- nmcli - add support for ``eui64`` and ``ipv6privacy`` parameters (https://github.com/ansible-collections/community.general/issues/3357).
- nmcli - adds ``routes6`` and ``route_metric6`` parameters for supporting IPv6 routes (https://github.com/ansible-collections/community.general/issues/4059).
- nmcli - remove nmcli modify dependency on ``type`` parameter (https://github.com/ansible-collections/community.general/issues/2858).
- nomad_job - minor refactoring (https://github.com/ansible-collections/community.general/pull/4567).
- nomad_job_info - minor refactoring (https://github.com/ansible-collections/community.general/pull/4567).
- npm - add ability to use ``production`` flag when ``ci`` is set (https://github.com/ansible-collections/community.general/pull/4299).
- open_iscsi - extended module to allow rescanning of established session for one or all targets (https://github.com/ansible-collections/community.general/issues/3763).
- opennebula - add the release action for VMs in the ``HOLD`` state (https://github.com/ansible-collections/community.general/pull/4036).
- opentelemetry_plugin - enrich service when using the ``docker_login`` (https://github.com/ansible-collections/community.general/pull/4104).
- opentelemetry_plugin - enrich service when using the ``jenkins``, ``hetzner`` or ``jira`` modules (https://github.com/ansible-collections/community.general/pull/4105).
- packet_device - minor refactoring (https://github.com/ansible-collections/community.general/pull/4567).
- packet_sshkey - minor refactoring (https://github.com/ansible-collections/community.general/pull/4567).
- packet_volume - minor refactoring (https://github.com/ansible-collections/community.general/pull/4567).
- pacman - add ``remove_nosave`` parameter to avoid saving modified configuration files as ``.pacsave`` files. (https://github.com/ansible-collections/community.general/pull/4316, https://github.com/ansible-collections/community.general/issues/4315).
- pacman - add ``stdout`` and ``stderr`` as return values (https://github.com/ansible-collections/community.general/pull/3758).
- pacman - now implements proper change detection for ``update_cache=true``. Adds ``cache_updated`` return value to when ``update_cache=true`` to report this result independently of the module's overall changed return value (https://github.com/ansible-collections/community.general/pull/4337).
- pacman - the module has been rewritten and is now much faster when using ``state=latest``. Operations are now done all packages at once instead of package per package and the configured output format of ``pacman`` no longer affect the module's operation. (https://github.com/ansible-collections/community.general/pull/3907, https://github.com/ansible-collections/community.general/issues/3783, https://github.com/ansible-collections/community.general/issues/4079)
- passwordstore lookup plugin - add configurable ``lock`` and ``locktimeout`` options to avoid race conditions in itself and in the ``pass`` utility it calls. By default, the plugin now locks on write operations (https://github.com/ansible-collections/community.general/pull/4194).
- pipx - added options ``editable`` and ``pip_args`` (https://github.com/ansible-collections/community.general/issues/4300).
- pipx - using ``do_raise()`` to raise exceptions in ``ModuleHelper`` derived modules (https://github.com/ansible-collections/community.general/pull/4674).
- pritunl_user - add ``mac_addresses`` parameter (https://github.com/ansible-collections/community.general/pull/4535).
- profitbricks - minor refactoring (https://github.com/ansible-collections/community.general/pull/4567).
- proxmox - add ``clone`` parameter (https://github.com/ansible-collections/community.general/pull/3930).
- proxmox - minor refactoring (https://github.com/ansible-collections/community.general/pull/4567).
- proxmox inventory plugin - add support for client-side jinja filters (https://github.com/ansible-collections/community.general/issues/3553).
- proxmox inventory plugin - add support for templating the ``url``, ``user``, and ``password`` options (https://github.com/ansible-collections/community.general/pull/4418).
- proxmox inventory plugin - add token authentication as an alternative to username/password (https://github.com/ansible-collections/community.general/pull/4540).
- proxmox inventory plugin - parse LXC configs returned by the proxmox API (https://github.com/ansible-collections/community.general/pull/4472).
- proxmox modules - move ``HAS_PROXMOXER`` check into ``module_utils`` (https://github.com/ansible-collections/community.general/pull/4030).
- proxmox modules - move common code into ``module_utils`` (https://github.com/ansible-collections/community.general/pull/4029).
- proxmox_kvm - added EFI disk support when creating VM with OVMF UEFI BIOS with new ``efidisk0`` option (https://github.com/ansible-collections/community.general/pull/4106, https://github.com/ansible-collections/community.general/issues/1638).
- proxmox_kwm - add ``win11`` to ``ostype`` parameter for Windows 11 and Windows Server 2022 support (https://github.com/ansible-collections/community.general/issues/4023, https://github.com/ansible-collections/community.general/pull/4191).
- proxmox_snap - add restore snapshot option (https://github.com/ansible-collections/community.general/pull/4377).
- proxmox_snap - fixed timeout value to correctly reflect time in seconds. The timeout was off by one second (https://github.com/ansible-collections/community.general/pull/4377).
- puppet - remove deprecation for ``show_diff`` parameter. Its alias ``show-diff`` is still deprecated and will be removed in community.general 7.0.0 (https://github.com/ansible-collections/community.general/pull/3980).
- python_requirements_info - returns python version broken down into its components, and some minor refactoring (https://github.com/ansible-collections/community.general/pull/3797).
- rax_files_objects - minor refactoring improving code quality (https://github.com/ansible-collections/community.general/pull/4649).
- redfish_* modules - the contents of ``@Message.ExtendedInfo`` will be returned as a string in the event that ``@Message.ExtendedInfo.Messages`` does not exist. This is likely more useful than the standard HTTP error (https://github.com/ansible-collections/community.general/pull/4596).
- redfish_command - add ``GetHostInterfaces`` command to enable reporting Redfish Host Interface information (https://github.com/ansible-collections/community.general/issues/3693).
- redfish_command - add ``IndicatorLedOn``, ``IndicatorLedOff``, and ``IndicatorLedBlink`` commands to the Systems category for controling system LEDs (https://github.com/ansible-collections/community.general/issues/4084).
- redfish_command - add ``SetHostInterface`` command to enable configuring the Redfish Host Interface (https://github.com/ansible-collections/community.general/issues/3632).
- redis - add authentication parameters ``login_user``, ``tls``, ``validate_certs``, and ``ca_certs`` (https://github.com/ansible-collections/community.general/pull/4207).
- scaleway inventory plugin - add profile parameter ``scw_profile`` (https://github.com/ansible-collections/community.general/pull/4049).
- scaleway_compute - add possibility to use project identifier (new ``project`` option) instead of deprecated organization identifier (https://github.com/ansible-collections/community.general/pull/3951).
- scaleway_volume - all volumes are systematically created on par1 (https://github.com/ansible-collections/community.general/pull/3964).
- seport - minor refactoring (https://github.com/ansible-collections/community.general/pull/4471).
- smartos_image_info - minor refactoring (https://github.com/ansible-collections/community.general/pull/4567).
- snap - add option ``options`` permitting to set options using the ``snap set`` command (https://github.com/ansible-collections/community.general/pull/3943).
- snap - using ``do_raise()`` to raise exceptions in ``ModuleHelper`` derived modules (https://github.com/ansible-collections/community.general/pull/4674).
- sudoers - add support for ``runas`` parameter (https://github.com/ansible-collections/community.general/issues/4379).
- svc - calling ``run_command`` with arguments as ``list`` instead of ``str`` (https://github.com/ansible-collections/community.general/pull/3829).
- syslog_json - add option to skip logging of ``gather_facts`` playbook tasks; use v2 callback API (https://github.com/ansible-collections/community.general/pull/4223).
- terraform - adds ``terraform_upgrade`` parameter which allows ``terraform init`` to satisfy new provider constraints in an existing Terraform project (https://github.com/ansible-collections/community.general/issues/4333).
- to_time_unit filter plugins - the time filters has been extended to also allow ``0`` as input (https://github.com/ansible-collections/community.general/pull/4612).
- udm_group - minor refactoring (https://github.com/ansible-collections/community.general/pull/4556).
- udm_share - minor refactoring (https://github.com/ansible-collections/community.general/pull/4556).
- vmadm - minor refactoring (https://github.com/ansible-collections/community.general/pull/4567).
- vmadm - minor refactoring and improvement on the module (https://github.com/ansible-collections/community.general/pull/4581).
- vmadm - minor refactoring and improvement on the module (https://github.com/ansible-collections/community.general/pull/4648).
- webfaction_app - minor refactoring (https://github.com/ansible-collections/community.general/pull/4567).
- webfaction_db - minor refactoring (https://github.com/ansible-collections/community.general/pull/4567).
- xattr - calling ``run_command`` with arguments as ``list`` instead of ``str`` (https://github.com/ansible-collections/community.general/pull/3806).
- xfconf - added missing value types ``char``, ``uchar``, ``int64`` and ``uint64`` (https://github.com/ansible-collections/community.general/pull/4534).
- xfconf - minor refactor on the base class for the module (https://github.com/ansible-collections/community.general/pull/3919).
- xfconf - using ``do_raise()`` to raise exceptions in ``ModuleHelper`` derived modules (https://github.com/ansible-collections/community.general/pull/4674).
- zfs - minor refactoring in the code (https://github.com/ansible-collections/community.general/pull/4650).
- zypper - add support for ``--clean-deps`` option to remove packages that depend on a package being removed (https://github.com/ansible-collections/community.general/pull/4195).

community.grafana
~~~~~~~~~~~~~~~~~

- Remove requirement for `ds_type` and `ds_url` parameters when deleting a datasource
- add `grafana` action group in `meta/runtime.yml` to support for module group defaults
- community.grafana.grafana_datasource supports aws_auth_type of default.
- refactor grafana_notification_channel module

community.hashi_vault
~~~~~~~~~~~~~~~~~~~~~

- The Filter guide has been added to the collection's docsite.
- vault_login module & lookup - no friendly error message was given when ``hvac`` was missing (https://github.com/ansible-collections/community.hashi_vault/issues/257).
- vault_pki_certificate - add ``vault_pki_certificate`` to the ``community.hashi_vault.vault`` action group (https://github.com/ansible-collections/community.hashi_vault/issues/251).
- vault_read module & lookup - no friendly error message was given when ``hvac`` was missing (https://github.com/ansible-collections/community.hashi_vault/issues/257).
- vault_token_create - add ``vault_token_create`` to the ``community.hashi_vault.vault`` action group (https://github.com/ansible-collections/community.hashi_vault/issues/251).
- vault_token_create module & lookup - no friendly error message was given when ``hvac`` was missing (https://github.com/ansible-collections/community.hashi_vault/issues/257).
- vault_write - add ``vault_write`` to the ``community.hashi_vault.vault`` action group (https://github.com/ansible-collections/community.hashi_vault/issues/251).

community.hrobot
~~~~~~~~~~~~~~~~

- Prepare collection for inclusion in an Execution Environment by declaring its dependencies (https://github.com/ansible-collections/community.hrobot/pull/45).

community.mysql
~~~~~~~~~~~~~~~

- Added explicit description of the supported versions of databases and connectors. Changes to the collection are **NOT** tested against database versions older than `mysql 5.7.31` and `mariadb 10.2.37` or connector versions older than `pymysql 0.7.10` and `mysqlclient 2.0.1`. (https://github.com/ansible-collections/community.mysql/discussions/141)
- mysql_user - added the ``force_context`` boolean option to set the default database context for the queries to be the ``mysql`` database. This way replication/binlog filters can catch the statements (https://github.com/ansible-collections/community.mysql/issues/265).
- mysql_user and mysql_role: Add the argument ``subtract_privs`` (boolean, default false, mutually exclusive with ``append_privs``). If set, the privileges given in ``priv`` are revoked and existing privileges are kept (https://github.com/ansible-collections/community.mysql/pull/333).

community.network
~~~~~~~~~~~~~~~~~

- community.network.ce_switchport - add support of decode a few stdout values from bitmap to human readable format(https://github.com/ansible-collections/community.network/issues/315)
- community.network.edgeos_config - append save command into result (https://github.com/ansible-collections/community.network/pull/189)

community.okd
~~~~~~~~~~~~~

- add action groups to runtime.yml (https://github.com/openshift/community.okd/issues/41).

community.proxysql
~~~~~~~~~~~~~~~~~~

- module_utils - Refactor save_config_to_disk and load_config_to_runtime (https://github.com/ansible-collections/community.proxysql/pull/78).
- proxysql_mysql_users - Add missing ``no_log`` option to ``encrypt_password`` parameter (https://github.com/ansible-collections/community.proxysql/pull/86).

community.rabbitmq
~~~~~~~~~~~~~~~~~~

- rabbitmq_user - add support for `topic authorization <https://www.rabbitmq.com/access-control.html#topic-authorisation>`_ (featured in RabbitMQ 3.7.0) (https://github.com/ansible-collections/community.rabbitmq/pull/73).

community.routeros
~~~~~~~~~~~~~~~~~~

- Added a ``community.routeros.api`` module defaults group. Use with ``group/community.routeros.api`` to provide options for all API-based modules (https://github.com/ansible-collections/community.routeros/pull/89).
- Prepare collection for inclusion in an Execution Environment by declaring its dependencies (https://github.com/ansible-collections/community.routeros/pull/83).
- api - add new option ``extended query`` more complex queries against RouterOS API (https://github.com/ansible-collections/community.routeros/pull/63).
- api - update ``query`` to accept symbolic parameters (https://github.com/ansible-collections/community.routeros/pull/63).
- api* modules - allow to set an encoding other than the default ASCII for communicating with the API (https://github.com/ansible-collections/community.routeros/pull/95).

community.vmware
~~~~~~~~~~~~~~~~

- Remove `version_added` documentation that pre-dates the collection, that is refers to Ansible < 2.10 (https://github.com/ansible-collections/community.vmware/pull/1215).
- vmware_datastore_info - added show_tag parameters to allow datastore tags to be read in a uniform way across _info modules  (https://github.com/ansible-collections/community.vmware/pull/1085).
- vmware_dvs_portgroup - Add the feature to configure ingress and egress traffinc shaping and netflow on the dvs portgroup. (https://github.com/ansible-collections/community.vmware/pull/1224)
- vmware_export_ovf - Add a new parameter 'export_with_extraconfig' to support export extra config options in ovf (https://github.com/ansible-collections/community.vmware/pull/1161).
- vmware_guest_disk - Added a new key 'cluster_disk' which allows you to use a filename originating from a VM with an RDM.
- vmware_guest_disk - Added bus_sharing as an option for SCSI devices.
- vmware_guest_disk - Enabled the use of up to 64 disks on a paravirtual SCSI controller when the hardware is version 14 or higher.
- vmware_guest_network - Add parameters `physical_function_backing`, `virtual_function_backing` and `allow_guest_os_mtu_change` (https://github.com/ansible-collections/community.vmware/pull/1218)
- vmware_guest_sendkey - added additional USB scan codes for HOME and END.
- vmware_guest_storage_policy - New parameter `controller_number` to support multiple SCSI controllers (https://github.com/ansible-collections/community.vmware/issues/1203).
- vmware_host_scanhba - add rescan_vmfs parameter to allow rescaning for new VMFS volumes. Also add rescan_hba parameter with default true to allow for not rescaning HBAs as this might be very slow. (https://github.com/ansible-collections/community.vmware/issues/479)
- vmware_host_snmp - implement setting syscontact and syslocation (https://github.com/ansible-collections/community.vmware/issues/1044).
- vmware_maintenancemode - Add support for check_mode (https://github.com/ansible-collections/community.vmware/pull/1311).
- vmware_migrate_vmk - Add `migrate_vlan_id` to use for the VMK interface when migrating from VDS to VSS (https://github.com/ansible-collections/community.vmware/issues/1297).
- vmware_object_role_permission - added VMware DV portgroup object_type for setting permissions (https://github.com/ansible-collections/community.vmware/pull/1176)
- vmware_rest_client module_util - added function get_tags_for_datastore for convenient tag collection (https://github.com/ansible-collections/community.vmware/pull/1085).
- vmware_vm_config_option - Fix the parameter not correct issue when hostname is set to ESXi host(https://github.com/ansible-collections/community.vmware/pull/1171).
- vmware_vm_info - Add the feature to get the output of allocated storage, cpu und memory. (https://github.com/ansible-collections/community.vmware/pull/1283)
- vmware_vm_info - Add the posibility to get the configuration informations of only one vm by name. (https://github.com/ansible-collections/community.vmware/pull/1241)
- vmware_vm_info - adding fact about ``datastore_url`` to output (https://github.com/ansible-collections/community.vmware/pull/1143).
- vmware_vswitch - Add support to manage security, teaming and traffic shaping policies on vSwitches. (https://github.com/ansible-collections/community.vmware/pull/1298).
- vmware_vswitch_info - Add support to return security, teaming and traffic shaping policies on vSwitches. (https://github.com/ansible-collections/community.vmware/pull/1309).

community.windows
~~~~~~~~~~~~~~~~~

- win_disk_facts - Added ``filter`` option to filter returned facts by type of disk information - https://github.com/ansible-collections/community.windows/issues/33
- win_disk_facts - Converted from ``#Requires -Module Ansible.ModuleUtils.Legacy`` to ``#AnsibleRequires -CSharpUtil Ansible.Basic``
- win_domain_user - Add support for managing service prinicpal names via the ``spn`` param and principals allowed to delegate via the ``delegates`` param (https://github.com/ansible-collections/community.windows/pull/365)
- win_domain_user - Added the ``groups_missing_behaviour`` option that controls the behaviour when a group specified does not exist - https://github.com/ansible-collections/community.windows/pull/375
- win_hotfix - Added the ``identifiers`` and ``kbs`` return value that is always a list of identifiers and kbs inside a hotfix
- win_iis_virtualdirectory - Added the ``connect_as``, ``username``, and ``password`` options to control the virtual directory authentication - https://github.com/ansible-collections/community.windows/issues/346
- win_power_plan - Added ``guid`` option to specify plan by a unique identifier - https://github.com/ansible-collections/community.windows/issues/310
- win_psmodule - Add credential support for through the ``username`` and ``password`` options
- win_psrepository - Add credential support for through the ``username`` and ``password`` options

community.zabbix
~~~~~~~~~~~~~~~~

- Enabled usage of environment variables for modules by adding a fallback lookup in the module_utils/helpers.py - zabbix_common_argument_spec
- all modules - prepare for deprecation of distutils LooseVersion.
- collection - Add dependencies to other collections. This helps Ansible Galaxy automatically downloading collections that this collection relies on to run.
- connection.httpapi (plugin) - add initial httpapi connection plugin.
- helpers.helper_compare_lists() changed logic to not consider the order of elements in lists. (https://github.com/ansible-collections/community.zabbix/pull/683)
- httpapi.jsonrpc (plugin) - add initial httpapi for future handling of json-rpc.
- new module zabbix authentication for configuring global authentication settings in Zabbix Server's Settings section of GUI.
- new module zabbix_autoregister for configuring global autoregistration settings in Zabbix Server's Settings section of GUI.
- new module zabbix_housekeeping for configuring global housekeeping settings in Zabbix Server's Settings section of GUI.
- test_zabbix_host_info - fix Template/Group names for 5.4
- test_zabbix_screen - disable testing for screen in 5.4 (deprecated)
- zabbix_action - additional fixes to make module work with Zabbix 6.0 (https://github.com/ansible-collections/community.zabbix/pull/664)
- zabbix_action - module ported to work with Zabbix 6.0 (https://github.com/ansible-collections/community.zabbix/pull/648, https://github.com/ansible-collections/community.zabbix/pull/653)
- zabbix_action - should now correctly actions with maintenance_status conditions (https://github.com/ansible-collections/community.zabbix/pull/667)
- zabbix_action, zabbix_maintenance, zabbix_mediatype, zabbix_proxy, zabbix_service - updated to work with Zabbix 6.0. (https://github.com/ansible-collections/community.zabbix/pull/683)
- zabbix_agent - Check if 'firewalld' exist and is running when handler is executed.
- zabbix_agent - Fixed use of bare variables in conditions (https://github.com/ansible-collections/community.zabbix/pull/663)
- zabbix_agent - Install the correct Python libxml2 package on SLES15
- zabbix_agent - Move inclusion of the apache.yml tasks to later stage during execution of role.
- zabbix_agent - Prepare for Zabbix 6.0.
- zabbix_agent - Specify a minor version with zabbix_agent_version_minor for RH systems.
- zabbix_agent - There was no way to configure a specific type for the macro.
- zabbix_agent - Use multiple aliases in the configuration file with ``zabbix_agent_zabbix_alias`` or ``zabbix_agent2_zabbix_alias``.
- zabbix_maintenance - added new module parameter `tags`, which allows configuring Problem Tags on maintenances.
- zabbix_maintenance - fixed to work with Zabbix 6.0+ and Python 3.9+ (https://github.com/ansible-collections/community.zabbix/pull/665)
- zabbix_proxy - Prepare for Zabbix 6.0.
- zabbix_proxy - Specify a minor version with zabbix_proxy_version_minor for RH systems.
- zabbix_proxy - Support for Sangoma and treat it like a RHEL system.
- zabbix_script module added (https://github.com/ansible-collections/community.zabbix/issues/634)
- zabbix_server - Check the 'zabbix_server_install_database_client' variable in RedHat tasks.
- zabbix_server - Prepare for Zabbix 6.0.
- zabbix_server - Specify a minor version with zabbix_server_version_minor for RH systems.
- zabbix_user - change alias property to username (changed in 5.4) (alias is now an alias for username)
- zabbix_user_info - change alias property to username (changed in 5.4) (alias is now an alias for username)
- zabbix_web - Change format ENCRYPTION, VERIFY_HOST from string to boolean.
- zabbix_web - Specify a minor version with zabbix_web_version_minor for RH systems.

containers.podman
~~~~~~~~~~~~~~~~~

- Add a second example to podman_pod_module.html
- Add new options for pod module
- Add requires option to podman_container module
- Fix sanity issues with a new Ansible version
- Use yaml syntax highlighting where appropriate

dellemc.enterprise_sonic
~~~~~~~~~~~~~~~~~~~~~~~~

- README - describe branch naming conventions for the "main" and "1.x" branches (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/54).
- README - describe the mapping of SONiC release versions to the corresponding branch and release names in the Dell SONiC Enterprise Ansible collection. (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/84).
- bgp_as_paths - Add a 'permit/deny' attribute (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/52).
- bgp_neighbors - add 'password' and 'description' attributes (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/69).
- meta - add the newly required execution_environment.yml file to the 'meta' directory (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/89).
- port_breakout - modify port numbers to match commonly available breakout ports (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/89).
- workflows - add stable-2.12 to the CI test matrix (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/51).
- workflows - add stable-2.13 to the CI test matrix (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/91).

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- idrac_redfish_storage_controller - This module is enhanced to support the following settings with check mode and idempotency - UnassignSpare, EnableControllerEncryption, BlinkTarget, UnBlinkTarget,  ConvertToRAID, ConvertToNonRAID, ChangePDStateToOnline, ChangePDStateToOffline.
- ome_application_network_address - The module is enhanced to support check mode and idempotency.
- ome_device_info - The module is enhanced to return a blank list when devices or baselines are not present in the system.
- ome_diagnostics - Added "supportassist_collection" as a choice for the log_type argument to export SupportAssist logs. (https://github.com/dell/dellemc-openmanage-ansible-modules/issues/309)
- ome_diagnostics - The module is enhanced to support check mode and idempotency. (https://github.com/dell/dellemc-openmanage-ansible-modules/issues/345)
- ome_diagnostics - The module is enhanced to support debug logs. (https://github.com/dell/dellemc-openmanage-ansible-modules/issues/308)
- ome_diagnostics - This module is enhanced to extract log from lead chassis. (https://github.com/dell/dellemc-openmanage-ansible-modules/issues/310)
- ome_firmware - The module is enhanced to support check mode and idempotency (https://github.com/dell/dellemc-openmanage-ansible-modules/issues/274)
- ome_firmware_baseline_compliance_info - The module is enhanced to return a blank list when devices or baselines are not present in the system.
- ome_firmware_baseline_info - The module is enhanced to return a blank list when devices or baselines are not present in the system.
- ome_identity_pool - The iSCSI Initiator and Initiator IP Pool attributes are not mandatory to create an identity pool. (https://github.com/dell/dellemc-openmanage-ansible-modules/issues/329)
- ome_identity_pool - The module is enhanced to support check mode and idempotency. (https://github.com/dell/dellemc-openmanage-ansible-modules/issues/328)
- ome_profile - The module is enhanced to support check mode and idempotency.
- ome_profile - The module is enhanced to support modifying a profile based on the attribute names instead of the ID.
- ome_smart_fabric_uplink - The module is enhanced to support idempotency. (https://github.com/dell/dellemc-openmanage-ansible-modules/issues/253)
- ome_template - An example task is added to create a compliance template from reference device (https://github.com/dell/dellemc-openmanage-ansible-modules/issues/339)
- ome_template - The module is enhanced to support check mode and idempotency. (https://github.com/dell/dellemc-openmanage-ansible-modules/issues/255)
- ome_template - The module is enhanced to support modifying a template based on the attribute names instead of the ID. (https://github.com/dell/dellemc-openmanage-ansible-modules/issues/358)
- ome_template_identity_pool - The module is enhanced to support check mode and idempotency.
- redfish_event_subscription - The module is enhanced to support check mode and idempotency.
- redfish_storage_volume - The module is enhanced to support check mode and idempotency. (https://github.com/dell/dellemc-openmanage-ansible-modules/issues/245)

f5networks.f5_modules
~~~~~~~~~~~~~~~~~~~~~

- Added no_log=True to content parameters in bigip_ssl_key and bigip_ssl_key_cert module to stop key and cert content fomr being logged.
- bigip_device_info - Added a new meta choice, packages, which groups information about as3, do, cfe and ts. This change was done to ensure users with non admin access can use this module to get information that does not require admin access.
- bigip_device_info - add UCS creation date to the data gathered
- bigip_device_info - add fqdn related parameters to be gathered on nodes
- bigip_device_info - add parent to the data gathered for ServerSSL Profiles
- bigip_device_info - added stats parameter for each virtual_server resource attached to a gtm_server
- bigip_device_info - this module can gather information about ucs backup files.
- bigip_pool_member - add checkmode bypass so that existence checks for pool is always returns true when using check mode
- bigip_profile_http_compression - Add content_type_include parameter to bigip_profile_fastl4 module
- bigip_virtual_server - add service_down_immediate_action parameter
- bigiq_regkey_license - add addon_keys parameter to the module

infoblox.nios_modules
~~~~~~~~~~~~~~~~~~~~~

- Added tags 'cloud' and 'networking' in 'galaxy.yaml'
- Allow specifying a template when creating a network `#105 <https://github.com/infobloxopen/infoblox-ansible/pull/105>`_
- Expanding for disable value `#119 <https://github.com/infobloxopen/infoblox-ansible/pull/119>`_
- Fix to create PTR record in different network views `#103 <https://github.com/infobloxopen/infoblox-ansible/pull/103>`_
- Fix unit and sanity test issues `#117 <https://github.com/infobloxopen/infoblox-ansible/pull/117>`_
- Following options are made required in the modules | Record | Option made required | | ------ | -------------------- | | A | ipv4addr | | AAAA | ipv6addr | | CNAME | canonical | | MX | mail_exchanger, preference | | PTR | ptrdname |
- Remove use_option for DHCP option 60 `#104 <https://github.com/infobloxopen/infoblox-ansible/pull/104>`_
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

- Add integration test to check handling of module_defaults (https://github.com/ansible-collections/kubernetes.core/pull/296).
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
- na_cloudmanager_aws_fsx - Import AWS FSX to CloudManager by adding new parameters ``import_file_system`` and ``file_system_id``.
- na_cloudmanager_connector_aws - automatically fetch client_id and instance_id for delete.
- na_cloudmanager_connector_aws - make the module idempotent for create and delete.
- na_cloudmanager_connector_aws - report client_id and instance_id if connector already exists.
- na_cloudmanager_connector_azure - Support user defined ``storage_account`` name. The ``storage_account`` can be created automatically. When ``storage_account`` is not set, the name is constructed by appending 'sa' to the connector ``name``.
- na_cloudmanager_connector_gcp - when using the user application default credential authentication by running the command gcloud auth application-default login, ``gcp_service_account_path`` is not needed.
- na_cloudmanager_cvo_aws - Support instance_type update
- na_cloudmanager_cvo_aws - Support license_type update
- na_cloudmanager_cvo_azure - Support instance_type update
- na_cloudmanager_cvo_azure - Support license_type update
- na_cloudmanager_cvo_gcp - Support instance_type update
- na_cloudmanager_cvo_gcp - Support license_type update
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
- na_ontap_cifs - Added ``unix_symlink`` option in REST.
- na_ontap_cifs_acl - Added REST support to the cifs share access control module.
- na_ontap_cifs_acl - new option ``type`` for user-group-type.
- na_ontap_cifs_server - Added REST support to the cifs server module.
- na_ontap_cifs_server - Added ``force`` option for create, delete and rename cifs server when using REST.
- na_ontap_cifs_server - Added ``from_name`` option to rename cifs server when using REST.
- na_ontap_cifs_share - Added REST support to the cifs share module.
- na_ontap_cluster_config role - use na_ontap_login_messages as na_ontap_motd is deprecated.
- na_ontap_cluster_peer - Added REST support to the cluster_peer module.
- na_ontap_debug - report ansible version and ONTAP collection version.
- na_ontap_efficiency_policy - Added REST support.
- na_ontap_export_policy_rule - new option ``ntfs_unix_security`` for NTFS export UNIX security options added.
- na_ontap_export_policy_rule -- Added Rest support for Export Policy Rules
- na_ontap_fcp -- Added REST support for FCP
- na_ontap_firmware_upgrade - REST support to download firmware and reboot SP.
- na_ontap_igroup_initiator - Added REST support.
- na_ontap_interface - use REST when ``use_rest`` is set to ``auto``.
- na_ontap_iscsi - Added REST support.
- na_ontap_license - Added REST support to the license module.
- na_ontap_lun - Added REST support.
- na_ontap_lun_map - Added REST support.
- na_ontap_net_ifgrp - Added REST support to the net ifgrp module.
- na_ontap_net_ifgrp - new REST only options ``from_lag_ports``, ``broadcast_domain`` and ``ipspace`` added.
- na_ontap_net_port - Added REST support to the net port module
- na_ontap_nfs - Added Rest Support
- na_ontap_nvme - Added REST support.
- na_ontap_ports - Added REST support to the ports module.
- na_ontap_qos_adaptive_policy_group - warn about deprecation, fall back to ZAPI or fail when REST is desired.
- na_ontap_qos_policy_group - Added REST only supported option ``adaptive_qos_options`` for configuring adaptive policy.
- na_ontap_qos_policy_group - Added REST only supported option ``fixed_qos_options`` for configuring max/min throughput policy.
- na_ontap_qos_policy_group - Added REST support.
- na_ontap_quotas - support TB as a unit, update doc with size format description.
- na_ontap_rest_info - new option ``owning_resource`` for REST info that requires an owning resource. For instance volume for a snapshot
- na_ontap_rest_info - support added for protocols/nfs/export-policies/rules (Requires owning_resource to be set)
- na_ontap_rest_info - support added for storage/volumes/snapshots (Requires owning_resource to be set)
- na_ontap_rest_info - update documention for `fields` to clarify the list of fields that are return by default.
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
- na_ontap_volume_autosize - improve error reporting.
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
- Add meta information for use in Execution Environments [#753](https://github.com/netbox-community/ansible_modules/pull/753)
- Add tags to modules missing it [#725](https://github.com/netbox-community/ansible_modules/pull/725)
- Multiple modules - add new parameters added in NetBox 3.2 [#768](https://github.com/netbox-community/ansible_modules/pull/768)
- nb_inventory - Add a racks option [#701](https://github.com/netbox-community/ansible_modules/pull/701)
- nb_inventory - Add documentation for use of inventory plugin in Tower/AWX [#648](https://github.com/netbox-community/ansible_modules/pull/648)
- nb_inventory - Add site_group as an option [#755](https://github.com/netbox-community/ansible_modules/pull/755)
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
- netbox_front_port and netbox_rear_port - Add label as parameter [#766](https://github.com/netbox-community/ansible_modules/pull/766)
- netbox_inventory_item - Add label and custom fields to module [#632](https://github.com/netbox-community/ansible_modules/pull/632)
- netbox_inventory_item - Add parent field to module [#682](https://github.com/netbox-community/ansible_modules/pull/682)
- netbox_provider_network - Add module for handling provider networks [#653](https://github.com/netbox-community/ansible_modules/pull/653)
- netbox_region - Add description, tags, custom_fields to module [#689](https://github.com/netbox-community/ansible_modules/pull/689)
- netbox_service - Add virtual_machine as an allowed query parameter for ipaddresses [#718](https://github.com/netbox-community/ansible_modules/pull/718)
- netbox_virtual_chassis - Add custom_fields to netbox_virtual_chassis [#657](https://github.com/netbox-community/ansible_modules/pull/657)
- netbox_vm_interface - Add custom fields to module [#637](https://github.com/netbox-community/ansible_modules/pull/637)
- netbox_webhook - Add module [#738](https://github.com/netbox-community/ansible_modules/pull/738)
- netbox_wireless_lan, netbox_wireless_lan_group, netbox_wireless_link - Add modules [#678](https://github.com/netbox-community/ansible_modules/pull/678)

ngine_io.cloudstack
~~~~~~~~~~~~~~~~~~~

- Various documentation fixes and code improvements to address ansible sanity tests failure.

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
- ovirt_affinity_group - Add affinity labels (https://github.com/oVirt/ovirt-ansible-collection/pull/481).
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
- purefa_fs - Add support for replicated file systems
- purefa_info - Add QoS information for volume groups
- purefa_info - Add SAML2SSO configutration information
- purefa_info - Add Safe Mode status
- purefa_info - Add info for protection group safe mode setting (Requires Purity//FA 6.3.0 or higher)
- purefa_info - Add info for protection group snapshots
- purefa_info - Add priority adjustment information for volumes and volume groups
- purefa_info - Fix Active Directory configuration details
- purefa_info - Split volume groups into live and deleted dicts
- purefa_network - Resolve bug stopping management IP address being changed correctly
- purefa_offload - Add support for multiple, homogeneous, offload targets
- purefa_pg - Add support for protection group SafeMode. Requires Purity//FA 6.3.0 or higher
- purefa_policy - Allow directories in snapshot policies to be managed
- purefa_saml - Add support for SAML2 SSO IdPs
- purefa_vg - Add DMM Priority Adjustment support
- purefa_volume - Add support for DMM Priority Adjustment
- purefa_volume - Provide volume facts for volume after recovery
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
- Added support for ansible 2.13
- Removed support for CentOS 8

t_systems_mms.icinga_director
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Add Icinga scheduled downtime module (https://github.com/T-Systems-MMS/ansible-collection-icinga-director/pull/146)
- Add icinga_serviceset module (https://github.com/T-Systems-MMS/ansible-collection-icinga-director/pull/163)
- Add possibility to use Compose and keyed groups in inventory-module (https://github.com/T-Systems-MMS/ansible-collection-icinga-director/pull/155)
- Added missing fields to 'icinga_host' and 'icinga_host_template' (https://github.com/T-Systems-MMS/ansible-collection-icinga-director/pull/158)
- Test more ansible versions (https://github.com/T-Systems-MMS/ansible-collection-icinga-director/pull/162)
- add option to append arguments to all modules (https://github.com/T-Systems-MMS/ansible-collection-icinga-director/pull/153)

theforeman.foreman
~~~~~~~~~~~~~~~~~~

- Add a role `convert2rhel` to perform setup for converting systems to RHEL
- Warn if the user tries to use a plain HTTP server URL and fail if the URL is neither HTTPS nor HTTP.
- add support for module defaults groups for Ansible core 2.12 (https://github.com/theforeman/foreman-ansible-modules/issues/1015)
- all modules - report smaller diffs by dropping ``null`` values. This should result in not showing fields that were unset to begin with, and mark fields that were explicitly removed as "deleted" instead of "replaced by ``null``"
- compute_resource - update libvirt examples (https://bugzilla.redhat.com/show_bug.cgi?id=1990119)
- content_upload - add support for OSTree content uploads (https://github.com/theforeman/foreman-ansible-modules/issues/628, https://projects.theforeman.org/issues/33299)
- content_view - add support to set label during creation.
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
- repository - add ``rhel-9`` to os version filter choices
- repository - add support for ``mirroring_policy`` for Katello 4.4+ (https://github.com/theforeman/foreman-ansible-modules/issues/1388)
- repository - new ``download_concurrency`` parameter (https://github.com/theforeman/foreman-ansible-modules/issues/1273)

vyos.vyos
~~~~~~~~~

- Add vyos_hostname resource module.
- Add vyos_snmp_server resource module.
- Change preconfig hostname from vyos to vyosuser
- Rename V4-EGRESS/V6-EGRESS to EGRESS in the tests to test the same-name situation
- Update vyos_facts to support IPv4 and IPv6 rule sets having the same name
- Update vyos_firewall_rules to support IPv4 and IPv6 rule sets having the same name
- firewall_rules - icmpv6 type - add support for vyos sw >= 1.4.
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

ansible.netcommon
~~~~~~~~~~~~~~~~~

- httpapi - Change default value of ``import_modules`` option from ``no`` to ``yes``
- netconf - Change default value of ``import_modules`` option from ``no`` to ``yes``
- network_cli - Change default value of ``import_modules`` option from ``no`` to ``yes``

arista.eos
~~~~~~~~~~

- eos_command - new suboption ``version`` of parameter ``command``, which controls the JSON response version. Previously the value was assumed to be "latest" for network_cli and "1" for httpapi, but the default will now be "latest" for both connections. This option is also available for use in modules making their own device requests with ``plugins.module_utils.network.eos.eos.run_commands()`` with the same new default behavior. (https://github.com/ansible-collections/arista.eos/pull/258).
- httpapi - the ``eos_use_sessions`` option is now a boolean instead of an integer.

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

community.general
~~~~~~~~~~~~~~~~~

- Parts of this collection do not work with ansible-core 2.11 on Python 3.12+. Please either upgrade to ansible-core 2.12+, or use Python 3.11 or earlier (https://github.com/ansible-collections/community.general/pull/3988).
- The symbolic links used to implement flatmapping for all modules were removed and replaced by ``meta/runtime.yml`` redirects. This effectively breaks compatibility with Ansible 2.9 for all modules (without using their "long" names, which is discouraged and which can change without previous notice since they are considered an implementation detail) (https://github.com/ansible-collections/community.general/pull/4548).
- a_module test plugin - remove Ansible 2.9 compatibility code (https://github.com/ansible-collections/community.general/pull/4548).
- archive - remove Ansible 2.9 compatibility code (https://github.com/ansible-collections/community.general/pull/4548).
- git_config - remove Ansible 2.9 and early ansible-base 2.10 compatibility code (https://github.com/ansible-collections/community.general/pull/4548).
- java_keystore - remove Ansible 2.9 compatibility code (https://github.com/ansible-collections/community.general/pull/4548).
- lists_mergeby and groupby_as_dict filter plugins - adjust filter plugin filename. This change is not visible to end-users, it only affects possible other collections importing Python paths (https://github.com/ansible-collections/community.general/pull/4625).
- lists_mergeby filter plugin - remove Ansible 2.9 compatibility code (https://github.com/ansible-collections/community.general/pull/4548).
- maven_artifact - remove Ansible 2.9 compatibility code (https://github.com/ansible-collections/community.general/pull/4548).
- memcached cache plugin - remove Ansible 2.9 compatibility code (https://github.com/ansible-collections/community.general/pull/4548).
- path_join filter plugin shim - remove Ansible 2.9 compatibility code (https://github.com/ansible-collections/community.general/pull/4548).
- redis cache plugin - remove Ansible 2.9 compatibility code (https://github.com/ansible-collections/community.general/pull/4548).
- yarn - remove unsupported and unnecessary ``--no-emoji`` flag (https://github.com/ansible-collections/community.general/pull/4662).

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

- The collection ``community.sap`` has been renamed to ``community.sap_libs``. For now both collections are included in Ansible. The content in ``community.sap`` will be replaced with deprecated redirects to the new collection in Ansible 7.0.0, and these redirects will eventually be removed from Ansible. Please update your FQCNs for ``community.sap``.

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

community.docker
~~~~~~~~~~~~~~~~

- Support for Ansible 2.9 and ansible-base 2.10 is deprecated, and will be removed in the next major release (community.docker 3.0.0). Some modules might still work with these versions afterwards, but we will no longer keep compatibility code that was needed to support them (https://github.com/ansible-collections/community.docker/pull/361).
- The dependency on docker-compose for Execution Environments is deprecated and will be removed in community.docker 3.0.0. The `Python docker-compose library <https://pypi.org/project/docker-compose/>`__ is unmaintained and can cause dependency issues. You can manually still install it in an Execution Environment when needed (https://github.com/ansible-collections/community.docker/pull/373).
- Various modules - the default of ``tls_hostname`` that was supposed to be removed in community.docker 2.0.0 will now be removed in version 3.0.0 (https://github.com/ansible-collections/community.docker/pull/362).
- docker_stack - the return values ``out`` and ``err`` that were supposed to be removed in community.docker 2.0.0 will now be removed in version 3.0.0 (https://github.com/ansible-collections/community.docker/pull/362).

community.general
~~~~~~~~~~~~~~~~~

- ansible_galaxy_install - deprecated support for ``ansible`` 2.9 and ``ansible-base`` 2.10 (https://github.com/ansible-collections/community.general/pull/4601).
- dig lookup plugin - the ``DLV`` record type has been decommissioned in 2017 and support for it will be removed from community.general 6.0.0 (https://github.com/ansible-collections/community.general/pull/4618).
- gem - the default of the ``norc`` option has been deprecated and will change to ``true`` in community.general 6.0.0. Explicitly specify a value to avoid a deprecation warning (https://github.com/ansible-collections/community.general/pull/4517).
- mail callback plugin - not specifying ``sender`` is deprecated and will be disallowed in community.general 6.0.0 (https://github.com/ansible-collections/community.general/pull/4140).
- module_helper module utils - deprecated the attribute ``ModuleHelper.VarDict`` (https://github.com/ansible-collections/community.general/pull/3801).
- nmcli - deprecate default hairpin mode for a bridge. This so we can change it to ``false`` in community.general 7.0.0, as this is also the default in ``nmcli`` (https://github.com/ansible-collections/community.general/pull/4334).
- pacman - from community.general 5.0.0 on, the ``changed`` status of ``update_cache`` will no longer be ignored if ``name`` or ``upgrade`` is specified. To keep the old behavior, add something like ``register: result`` and ``changed_when: result.packages | length > 0`` to your task (https://github.com/ansible-collections/community.general/pull/4329).
- proxmox inventory plugin - the current default ``true`` of the ``want_proxmox_nodes_ansible_host`` option has been deprecated. The default will change to ``false`` in community.general 6.0.0. To keep the current behavior, explicitly set ``want_proxmox_nodes_ansible_host`` to ``true`` in your inventory configuration. We suggest to already switch to the new behavior by explicitly setting it to ``false``, and by using ``compose:`` to set ``ansible_host`` to the correct value. See the examples in the plugin documentation for details (https://github.com/ansible-collections/community.general/pull/4466).
- vmadm - deprecated module parameter ``debug`` that was not used anywhere (https://github.com/ansible-collections/community.general/pull/4580).

community.hashi_vault
~~~~~~~~~~~~~~~~~~~~~

- Support for Ansible 2.9 and ansible-base 2.10 is deprecated, and will be removed in the next major release (community.hashi_vault 3.0.0) next spring (https://github.com/ansible-community/community-topics/issues/50, https://github.com/ansible-collections/community.hashi_vault/issues/189).
- aws_iam_login auth method - the ``aws_iam_login`` method has been renamed to ``aws_iam``. The old name will be removed in collection version ``3.0.0``. Until then both names will work, and a warning will be displayed when using the old name (https://github.com/ansible-collections/community.hashi_vault/pull/193).
- token_validate options - the shared auth option ``token_validate`` will change its default from ``True`` to ``False`` in community.hashi_vault version 4.0.0. The ``vault_login`` lookup and module will keep the default value of ``True`` (https://github.com/ansible-collections/community.hashi_vault/issues/248).
- token_validate options - the shared auth option ``token_validate`` will change its default from ``true`` to ``false`` in community.hashi_vault version 4.0.0. The ``vault_login`` lookup and module will keep the default value of ``true`` (https://github.com/ansible-collections/community.hashi_vault/issues/248).

community.network
~~~~~~~~~~~~~~~~~

- Support for Ansible 2.9 and ansible-base 2.10 is deprecated, and will be removed in the next major release (community.network 4.0.0) this spring. While most content will probably still work with ansible-base 2.10, we will remove symbolic links for modules and action plugins, which will make it impossible to use them with Ansible 2.9 anymore. Please use community.network 3.x.y with Ansible 2.9 and ansible-base 2.10, as these releases will continue to support Ansible 2.9 and ansible-base 2.10 even after they are End of Life (https://github.com/ansible-community/community-topics/issues/50, https://github.com/ansible-collections/community.network/pull/382).

junipernetworks.junos
~~~~~~~~~~~~~~~~~~~~~

- 'router_id' options is deprecated from junos_ospf_interfaces, junos_ospfv2 and junos_ospfv3 resuorce module.

purestorage.flasharray
~~~~~~~~~~~~~~~~~~~~~~

- purefa_sso - Deprecated in favor of M(purefa_admin). Will be removed in Collection 2.0

Removed Features (previously deprecated)
----------------------------------------

- The community.kubernetes collection has been removed from Ansible 6. It has been deprecated since Ansible 4.2, and version 2.0.0 included since Ansible 5 is only a set of deprecated redirects from community.kubernetes to kubernetes.core. If you still need the redirects, you can manually install community.kubernetes with ``ansible-galaxy collection install community.kubernetes`` (https://github.com/ansible-community/community-topics/issues/93).
- The community.kubevirt collection has been removed from Ansible 6. It has not been working with the community.kubernetes collection included since Ansible 5.0.0, and unfortunately nobody managed to adjust the collection to work with kubernetes.core >= 2.0.0. If you need to use this collection, you need to manually install community.kubernetes < 2.0.0 together with community.kubevirt with ``ansible-galaxy collection install community.kubevirt 'community.kubernetes:<2.0.0'`` (https://github.com/ansible-community/community-topics/issues/92).

Ansible-core
~~~~~~~~~~~~

- Remove deprecated ``Templar.set_available_variables()`` method (https://github.com/ansible/ansible/issues/75828)
- cli - remove deprecated ability to set verbosity before the sub-command (https://github.com/ansible/ansible/issues/75823)
- copy - remove deprecated ``thirsty`` alias (https://github.com/ansible/ansible/issues/75824)
- psrp - Removed fallback on ``put_file`` with older ``pypsrp`` versions. Users must have at least ``pypsrp>=0.4.0``.
- url_argument_spec - remove deprecated ``thirsty`` alias for ``get_url`` and ``uri`` modules (https://github.com/ansible/ansible/issues/75825, https://github.com/ansible/ansible/issues/75826)

community.general
~~~~~~~~~~~~~~~~~

- ali_instance_info - removed the options ``availability_zone``, ``instance_ids``, and ``instance_names``. Use filter item ``zone_id`` instead of ``availability_zone``, filter item ``instance_ids`` instead of ``instance_ids``, and filter item ``instance_name`` instead of ``instance_names`` (https://github.com/ansible-collections/community.general/pull/4516).
- apt_rpm - removed the deprecated alias ``update-cache`` of ``update_cache`` (https://github.com/ansible-collections/community.general/pull/4516).
- compose - removed various deprecated aliases. Use the version with ``_`` instead of ``-`` instead (https://github.com/ansible-collections/community.general/pull/4516).
- dnsimple - remove support for dnsimple < 2.0.0 (https://github.com/ansible-collections/community.general/pull/4516).
- github_deploy_key - removed the deprecated alias ``2fa_token`` of ``otp`` (https://github.com/ansible-collections/community.general/pull/4516).
- homebrew, homebrew_cask - removed the deprecated alias ``update-brew`` of ``update_brew`` (https://github.com/ansible-collections/community.general/pull/4516).
- linode - removed the ``backupsenabled`` option. Use ``backupweeklyday`` or ``backupwindow`` to enable backups (https://github.com/ansible-collections/community.general/pull/4516).
- opkg - removed the deprecated alias ``update-cache`` of ``update_cache`` (https://github.com/ansible-collections/community.general/pull/4516).
- pacman - if ``update_cache=true`` is used with ``name`` or ``upgrade``, the changed state will now also indicate if only the cache was updated. To keep the old behavior - only indicate ``changed`` when a package was installed/upgraded -, use ``changed_when`` as indicated in the module examples (https://github.com/ansible-collections/community.general/pull/4516).
- pacman - removed the deprecated alias ``update-cache`` of ``update_cache`` (https://github.com/ansible-collections/community.general/pull/4516).
- proxmox, proxmox_kvm, proxmox_snap - no longer allow to specify a VM name that matches multiple VMs. If this happens, the modules now fail (https://github.com/ansible-collections/community.general/pull/4516).
- serverless - removed the ``functions`` option. It was not used by the module (https://github.com/ansible-collections/community.general/pull/4516).
- slackpkg - removed the deprecated alias ``update-cache`` of ``update_cache`` (https://github.com/ansible-collections/community.general/pull/4516).
- urpmi - removed the deprecated alias ``no-recommends`` of ``no_recommends`` (https://github.com/ansible-collections/community.general/pull/4516).
- urpmi - removed the deprecated alias ``update-cache`` of ``update_cache`` (https://github.com/ansible-collections/community.general/pull/4516).
- xbps - removed the deprecated alias ``update-cache`` of ``update_cache`` (https://github.com/ansible-collections/community.general/pull/4516).
- xfconf - the ``get`` state has been removed. Use the ``xfconf_info`` module instead (https://github.com/ansible-collections/community.general/pull/4516).

community.hashi_vault
~~~~~~~~~~~~~~~~~~~~~

- aws_iam auth - the deprecated alias ``aws_iam_login`` for the ``aws_iam`` value of the ``auth_method`` option has been removed (https://github.com/ansible-collections/community.hashi_vault/issues/194).
- community.hashi_vault collection - support for Ansible 2.9 and ansible-base 2.10 has been removed (https://github.com/ansible-collections/community.hashi_vault/issues/189).
- hashi_vault lookup - the deprecated ``[lookup_hashi_vault]`` INI config section has been removed in favor of the collection-wide ``[hashi_vault_collection]`` section (https://github.com/ansible-collections/community.hashi_vault/issues/179).
- the "legacy" integration test setup has been removed; this does not affect end users and is only relevant to contributors (https://github.com/ansible-collections/community.hashi_vault/pull/191).

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
- Prevent losing unsafe on results returned from lookups (https://github.com/ansible/ansible/issues/77535)
- Templating - Ensure we catch exceptions when getting ``.filters`` and ``.tests`` attributes on their respective plugins and properly error, instead of aborting which results in no filters being added to the jinja2 environment
- Trigger an undefined error when an undefined variable is detected within a dictionary and/or list (https://github.com/ansible/ansible/pull/75587)
- _run_loop - Add the task name to the warning (https://github.com/ansible/ansible/issues/76011)
- ``Templar.copy_with_new_env`` - set the ``finalize`` method of the new ``Templar`` object for the new environment (https://github.com/ansible/ansible/issues/76379)
- add_host/group_by: fix using changed_when in a loop (https://github.com/ansible/ansible/issues/71627)
- ansible - Exclude Python 2.6 from Python interpreter discovery.
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
- arg_spec - Fix incorrect ``no_log`` warning when a parameter alias is used (https://github.com/ansible/ansible/pull/77576)
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
- git module fix docs and proper use of ssh wrapper script and GIT_SSH_COMMAND depending on version.
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
- variablemanager, more efficient read of vars files
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
- httpapi - Fix for improperly set hostname in url
- libssh - Fix for improperly set hostname in connect
- network_cli - Provide clearer error message when a prompt regex fails to compile
- network_cli - fix issue when multiple terminal_initial_(prompt|answer) values are given (https://github.com/ansible-collections/ansible.netcommon/issues/331).
- restconf - When non-JSON data is encountered, return the bytes found instead of nothing.

ansible.posix
~~~~~~~~~~~~~

- Fix for whitespace in source full path causing error ```code 23) at main.c(1330) [sender=3.2.3]``` (https://github.com/ansible-collections/ansible.posix/pull/278)
- Include ``PSF-license.txt`` file for ``plugins/module_utils/_version.py``.
- Use vendored version of ``distutils.version`` instead of the deprecated Python standard library to address PEP 632 (https://github.com/ansible-collections/ansible.posix/issues/303).
- firewalld - Correct usage of queryForwardPort (https://github.com/ansible-collections/ansible.posix/issues/247).
- firewalld - Refine the handling of exclusive options (https://github.com/ansible-collections/ansible.posix/issues/255).
- mount - add a newline at the end of line in ``fstab`` (https://github.com/ansible-collections/ansible.posix/issues/210).
- profile_tasks - Correctly calculate task execution time with serial execution (https://github.com/ansible-collections/ansible.posix/issues/83).
- seboolean - add ``python3-libsemanage`` package dependency for RHEL8+ systems.

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
- win_reboot - Always set a minimum of 2 seconds for ``pre_reboot_delay`` to ensure the plugin can read the result
- win_shell - Use the 24 hour format for the hours of ``start`` and ``end`` - https://github.com/ansible-collections/ansible.windows/issues/303
- win_updates - Fix return value for ``updates`` and ``filtered_updates`` to match original stucture - https://github.com/ansible-collections/ansible.windows/issues/307
- win_updates - Fixed issue when attempting to run ``task.ps1`` with a host that has a restrictive execution policy set through GPO
- win_updates - prevent the host from going to sleep if a low sleep timeout is set - https://github.com/ansible-collections/ansible.windows/issues/310

arista.eos
~~~~~~~~~~

- Add and fix bgp_global neighbor parsers.
- Add check mode support to bgp_global and bgp_address_family
- Add logic to add new interface using overridden.
- Add logic to skip unwanted configs from running-config, to collect bgp af facts.
- Add symlink of modules under plugins/action.
- Automatiaclly named sessions (ansible_XXXXXXXXX) now use two digits of sub-second precision (if available). This is to work around tasks reusing a session if the previous task completed very quickly.
- Fix added to change snmp communities with or without acl.
- Fix parser to parse maximum-paths ecmp command correctly.
- Fix the logic to add new aces using replaced and overriden state.
- Fixed an invalid parameter used in example for eos_l2_interfaces
- Normalize interface name from want before comaparing with the interface in have.
- Normalize ntp server source interface.
- arista.eos.eos_acls - fixed issue that would cause a key value error on `aces` element when no ACEs exist in the access-list.
- arista.eos.eos_acls - fixed issue where protcol_options were rendered to command line using the key _underscore_ value rather than the hyphen nominclature.
- eos_acls - fixes state replaced where new ACEs are not all added
- eos_bgp_global - Add alias for peer -  neighbor_address
- httpapi - detect session support more robustly when ``eos_use_sessions`` is not specified.

cisco.aci
~~~~~~~~~

- Add pool_allocation_mode to the required parameter list in aci_vlan_pool_encap_block module
- Fix bfd issues in aci_l3out_static_routes module on pre-4.2 APICs
- Fix output_path to support multiple APIC runs in parallel
- Fix small sanity issue in aci_epg_to_contract
- Remove owner_key, owner_tag and annotation from module that do not support them
- Removed block_name from the required parameter list in aci_vlan_pool_encap_block module

cisco.asa
~~~~~~~~~

- Fixes asa_ogs services object and port object issue ((https://github.com/ansible-collections/cisco.asa/issues/152).

cisco.ios
~~~~~~~~~

- 'ios_acls'- filters out dynamically generated reflexive type acls.
- 'ios_banner' - Bugfix for presence of multiple delimitation chars in the banner's declaration and idempotence improvement.
- Add symlink of modules under plugins/action.
- Fix become raises error when exec prompt timestamp is configured.
- Fix ntp_global - remove no_log for key_id under peer and server attributes.
- Fix ntp_global - to handle when attribute value is false.
- `acl_interfaces` - optimization and bugfixes.
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
- `ios_l3_interface` - config code to generate proper ordering of commands on action states.
- `ios_logging_global` - Added alias to render host under hosts not hostname.
- `ios_logging_global` - fix host ipv6 commands not parsed correctly.
- `ios_logging_global` - fix wrong ordering of commands fired on replaced state.
- `ios_route_maps` - Fix parsers for correct rendering of as_number as list.
- `ios_snmp_server` - Change key from `users` to `views` in rm template to fix failure when collecting snmp server facts from devices that have a view defined in the configuration (https://github.com/ansible-collections/cisco.ios/issues/491).
- `ios_snmp_server` - Fix parsers for views facts collection.
- `ios_static_routes` - Consider only config containing routes to render facts.
- `ios_static_routes` - Fixes static routes unable to identify interface names when supplied with destination attribute.
- `ios_vlans` - fix parsing of VLAN names with spaces.
- `ios_vlans` - fix parsing of VLAN ranges under remote span.
- acls parser didn't only checked if the proto_options variable existed without validating that it was a dictionary before trying to use it as one.

cisco.iosxr
~~~~~~~~~~~

- Add symlink of modules under plugins/action.
- Fix iosxr_ospfv2 throwing a traceback with gathered (https://github.com/ansible-collections/cisco.iosxr/issues/227).
- `iosxr_acls` - fix acl for parsing wrong command on ( num matches ) data
- `iosxr_snmp_server` - Add aliases for access-lists in snmp-server(https://github.com/ansible-collections/cisco.iosxr/pull/225).
- fix issue of local variable 'start_index' referenced before assignment with cisco.iosxr.iosxr_config.
- iosxr_bgp_global - Add alias for neighbor_address (https://github.com/ansible-collections/cisco.iosxr/issues/216)
- iosxr_snmp_server - Fix gather_facts issue in snmp_servers (https://github.com/ansible-collections/cisco.iosxr/issues/215)
- iosxr_user - replaced custom paramiko sftp and ssh usage with native "copy_file" and "send_command" functions. Fixed issue when ssh key copying doesn't work with network_cli or netconf plugin by deleting "provider" usage. Fixed improper handling of "No such configuration item" when getting data for username section, without that ansible always tried to delete user "No" when purging if there is no any user in config. Fixed one-line admin mode commands not work anymore for ssh key management on IOS XR Software, Version 7.1.3, and add support of "admin" module property (https://github.com/ansible-collections/cisco.iosxr/pull/15)

cisco.ise
~~~~~~~~~

- Change description from Aci to ACI
- Change description from Acl to ACL
- Change description from Anc to ANC
- Change description from Byod to BYOD
- Change description from Ca to CA
- Change description from Csr to CSR
- Change description from Mnt to MNT
- Change description from Nbar to NBAR
- Change description from Pxgrid to pxGrid
- Change description from Radius to RADIUS
- Change description from Rest to REST
- Change description from Sg Acl to SGACL
- Change description from Sg to SG
- Change description from Sgt to SGT
- Change description from Sms to SMS
- Change description from Smtp to SMTP
- Change description from Ssid to SSID
- Change description from Sxp to SXP
- Change description from Tacacs to TACACS
- Change description from Vlan to VLAN
- Change description from Vn to VN
- Change description from Vpns to VPNs
- Update ISE version to 3.1.0 on vars example
- Update README recommended SDK version in compatibility matrix
- Update README, add ISE 3.1 + Patch 1 and ISE API Versioning notes
- Update README, update Compatibility matrix.
- Update documentation of the modules.
- Update recommended SDK version in modules from 1.4.0 to 1.5.0
- device_administration_authentication_rules - added a validation reading the data
- device_administration_authorization_rules - added a validation reading the data
- device_administration_global_exception_rules - added a validation reading the data
- device_administration_local_exception_rules - added a validation reading the data
- network_access_authentication_rules - added a validation reading the data
- network_access_authorization_rules - added a validation reading the data
- network_access_authorization_rules - added a validation when reading the data
- network_access_global_exception_rules - added a validation reading the data
- network_access_local_exception_rules - added a validation reading the data
- node_group_node_create - fix family execution call from Node Deployment to Node Group.
- node_group_node_delete - fix family execution call from Node Deployment to Node Group.
- node_group_node_info - fix family execution call from Node Deployment to Node Group.
- node_services_interfaces_info - change the validation.
- node_services_profiler_probe_config - fixes params used for module.
- node_services_sxp_interfaces - fixes params used for module.
- plugin/modules - update documentation block.
- repository - change path parameter from name to repositoryName
- repository - fixes params used for modules. Fix for issue 19.
- repository_files_info - change path parameter from name to repositoryName
- repository_files_info - fixes params used for module.
- repository_info - change path parameter from name to repositoryName
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

- meraki_alert - Updates now properly set default destination webhook
- meraki_mr_rf_profile - Fix issue with idempotency and creation of RF Profiles by name only
- meraki_mr_ssid - Fix issue with SSID removal idempotency when ID doesn't exist
- meraki_syslog -  Fix crash due to incorrect dictionary reference
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
- `nxos_lag_interfaces` - Fix KeyError with state overridden when port-channel has no members (https://github.com/ansible-collections/cisco.nxos/issues/452).
- `nxos_ntp_global` - Aliased `vrf` to `use_vrf` wherever applicable to maintain consistency with models for other platforms.
- `nxos_ntp_global` - In some cases, there is an extra whitespace in the source-interface line. This patch accounts for this behaviour in config (https://github.com/ansible-collections/cisco.nxos/issues/399).
- `nxos_ntp_global` - correctly propagate CLI failure for non-existent auth keys (https://github.com/ansible-collections/cisco.nxos/issues/467).
- `nxos_snmp_server` - Fix rendering context command (https://github.com/ansible-collections/cisco.nxos/issues/406).
- `nxos_snmp_server` - Properly handle corner cases for snmp-server user (https://github.com/ansible-collections/cisco.nxos/issues/454).
- `snmp_server` - Snmp contact/location and location were not gathered if containing whitespaces.
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
- ec2_asg - Change the default value of ``purge_tags`` to ``false``. Restores previous behaviour (https://github.com/ansible-collections/community.aws/pull/1064).
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

- Include ``PSF-license.txt`` file for ``plugins/module_utils/_version.py``.
- Include ``simplified_bsd.txt`` license file for the ECS module utils.
- Make collection more robust when PyOpenSSL is used with an incompatible cryptography version (https://github.com/ansible-collections/community.crypto/pull/445).
- Various modules and plugins - use vendored version of ``distutils.version`` instead of the deprecated Python standard library ``distutils`` (https://github.com/ansible-collections/community.crypto/pull/353).
- certificate_complete_chain - allow multiple potential intermediate certificates to have the same subject (https://github.com/ansible-collections/community.crypto/issues/399, https://github.com/ansible-collections/community.crypto/pull/403).
- certificate_complete_chain - do not append root twice if the chain already ends with a root certificate (https://github.com/ansible-collections/community.crypto/pull/360).
- certificate_complete_chain - do not hang when infinite loop is found (https://github.com/ansible-collections/community.crypto/issues/355, https://github.com/ansible-collections/community.crypto/pull/360).
- certificate_complete_chain - do not stop execution if an unsupported signature algorithm is encountered; warn instead (https://github.com/ansible-collections/community.crypto/pull/457).
- luks_device - fix parsing of ``lsblk`` output when device name ends with ``crypt`` (https://github.com/ansible-collections/community.crypto/issues/409, https://github.com/ansible-collections/community.crypto/pull/410).
- luks_devices - set ``LANG`` and similar environment variables to avoid translated output, which can break some of the module's functionality like key management (https://github.com/ansible-collections/community.crypto/pull/388, https://github.com/ansible-collections/community.crypto/issues/385).
- openssh_* modules - fix exception handling to report traceback to users for enhanced traceability (https://github.com/ansible-collections/community.crypto/pull/417).
- openssh_cert - fixed false ``changed`` status for ``host`` certificates when using ``full_idempotence`` (https://github.com/ansible-collections/community.crypto/issues/395, https://github.com/ansible-collections/community.crypto/pull/396).
- x509_certificate - for the ``ownca`` provider, check whether the CA private key actually belongs to the CA certificate (https://github.com/ansible-collections/community.crypto/pull/407).
- x509_certificate - regenerate certificate when the CA's public key changes for ``provider=ownca`` (https://github.com/ansible-collections/community.crypto/pull/407).
- x509_certificate - regenerate certificate when the CA's subject changes for ``provider=ownca`` (https://github.com/ansible-collections/community.crypto/issues/400, https://github.com/ansible-collections/community.crypto/pull/402).
- x509_certificate - regenerate certificate when the private key changes for ``provider=selfsigned`` (https://github.com/ansible-collections/community.crypto/pull/407).
- x509_crl - fix crash when ``issuer`` for a revoked certificate is specified (https://github.com/ansible-collections/community.crypto/pull/441).

community.digitalocean
~~~~~~~~~~~~~~~~~~~~~~

- Update README.md with updated Droplet examples (https://github.com/ansible-collections/community.digitalocean/issues/199).
- digital_ocean_cdn_endpoints - defaulting optional string parameters as strings (https://github.com/ansible-collections/community.digitalocean/issues/205).
- digital_ocean_cdn_endpoints - remove non-API parameters before posting to the API (https://github.com/ansible-collections/community.digitalocean/issues/252).
- digital_ocean_cdn_endpoints - updating Spaces endpoint for the integration test (https://github.com/ansible-collections/community.digitalocean/issues/205).
- digital_ocean_cdn_endpoints - use the correct module name in the C(EXAMPLES) (https://github.com/ansible-collections/community.digitalocean/issues/251).
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
- Include ``PSF-license.txt`` file for ``plugins/module_utils/_version.py``.
- Various modules and plugins - use vendored version of ``distutils.version`` included in ansible-core 2.12 if available. This avoids breakage when ``distutils`` is removed from the standard library of Python 3.12. Note that ansible-core 2.11, ansible-base 2.10 and Ansible 2.9 are right now not compatible with Python 3.12, hence this fix does not target these ansible-core/-base/2.9 versions (https://github.com/ansible-collections/community.docker/pull/258).
- docker connection plugin - fix option handling to be compatible with ansible-core 2.13 (https://github.com/ansible-collections/community.docker/pull/297, https://github.com/ansible-collections/community.docker/issues/307).
- docker connection plugin - make sure that ``docker_extra_args`` is used for querying the Docker version. Also ensures that the Docker version is only queried when needed. This is currently the case if a remote user is specified (https://github.com/ansible-collections/community.docker/issues/325, https://github.com/ansible-collections/community.docker/pull/327).
- docker connection plugin - replace deprecated ``distutils.spawn.find_executable`` with Ansible's ``get_bin_path`` to find the ``docker`` executable (https://github.com/ansible-collections/community.docker/pull/257).
- docker_api connection plugin - avoid passing an unnecessary argument to a Docker SDK for Python call that is only supported by version 3.0.0 or later (https://github.com/ansible-collections/community.docker/pull/243).
- docker_api connection plugin - fix option handling to be compatible with ansible-core 2.13 (https://github.com/ansible-collections/community.docker/pull/308).
- docker_compose - fix Python 3 type error when extracting warnings or errors from docker-compose's output (https://github.com/ansible-collections/community.docker/pull/305).
- docker_container - fail with a meaningful message instead of crashing if a port is specified with more than three colon-separated parts (https://github.com/ansible-collections/community.docker/pull/367, https://github.com/ansible-collections/community.docker/issues/365).
- docker_container - remove unused code that will cause problems with Python 3.13 (https://github.com/ansible-collections/community.docker/pull/354).
- docker_container, docker_image - adjust image finding code to pecularities of ``podman-docker``'s API emulation when Docker short names like ``redis`` are used (https://github.com/ansible-collections/community.docker/issues/292).
- docker_container_exec - ``chdir`` is only supported since Docker SDK for Python 3.0.0. Make sure that this option can only use when 3.0.0 or later is installed, and prevent passing this parameter on when ``chdir`` is not provided to this module (https://github.com/ansible-collections/community.docker/pull/243, https://github.com/ansible-collections/community.docker/issues/242).
- docker_container_exec - disallow using the ``chdir`` option for Docker API before 1.35 (https://github.com/ansible-collections/community.docker/pull/253).
- nsenter connection plugin - ensure the ``nsenter_pid`` option is retrieved in ``_connect`` instead of ``__init__`` to prevent a crasher due to bad initialization order (https://github.com/ansible-collections/community.docker/pull/249).
- nsenter connection plugin - replace the use of ``--all-namespaces`` with specific namespaces to support compatibility with Busybox nsenter (used on, for example, Alpine containers) (https://github.com/ansible-collections/community.docker/pull/249).

community.general
~~~~~~~~~~~~~~~~~

- Include ``simplified_bsd.txt`` license file for various module utils, the ``lxca_common`` docs fragment, and the ``utm_utils`` unit tests.
- Various modules and plugins - use vendored version of ``distutils.version`` instead of the deprecated Python standard library ``distutils`` (https://github.com/ansible-collections/community.general/pull/3936).
- a_module test plugin - fix crash when testing a module name that was tombstoned (https://github.com/ansible-collections/community.general/pull/3660).
- alternatives - fix output parsing for alternatives groups (https://github.com/ansible-collections/community.general/pull/3976).
- cargo - fix detection of outdated packages when ``state=latest`` (https://github.com/ansible-collections/community.general/pull/4052).
- cargo - fix incorrectly reported changed status for packages with a name containing a hyphen (https://github.com/ansible-collections/community.general/issues/4044, https://github.com/ansible-collections/community.general/pull/4052).
- consul - fixed bug introduced in PR 4590 (https://github.com/ansible-collections/community.general/issues/4680).
- consul - fixed bug where class ``ConsulService`` was overwriting the field ``checks``, preventing the addition of checks to a service (https://github.com/ansible-collections/community.general/pull/4590).
- counter_enabled callback plugin - fix output to correctly display host and task counters in serial mode (https://github.com/ansible-collections/community.general/pull/3709).
- dconf - skip processes that disappeared while we inspected them (https://github.com/ansible-collections/community.general/issues/4151).
- dnsmadeeasy - fix failure on deleting DNS entries when API response does not contain monitor value (https://github.com/ansible-collections/community.general/issues/3620).
- dsv lookup plugin - raise an Ansible error if the wrong ``python-dsv-sdk`` version is installed (https://github.com/ansible-collections/community.general/pull/4422).
- filesize - add support for busybox dd implementation, that is used by default on Alpine linux (https://github.com/ansible-collections/community.general/pull/4288, https://github.com/ansible-collections/community.general/issues/4259).
- filesystem - handle ``fatresize --info`` output lines without ``:`` (https://github.com/ansible-collections/community.general/pull/4700).
- filesystem - improve error messages when output cannot be parsed by including newlines in escaped form (https://github.com/ansible-collections/community.general/pull/4700).
- gconftool2 - properly escape values when passing them to ``gconftool-2`` (https://github.com/ansible-collections/community.general/pull/4647).
- git_branch - remove deprecated and unnecessary branch ``unprotect`` method (https://github.com/ansible-collections/community.general/pull/4496).
- github_repo - ``private`` and ``description`` attributes should not be set to default values when the repo already exists (https://github.com/ansible-collections/community.general/pull/2386).
- gitlab_group - improve searching for projects inside group on deletion (https://github.com/ansible-collections/community.general/pull/4491).
- gitlab_group_members - handle more than 20 groups when finding a group (https://github.com/ansible-collections/community.general/pull/4491, https://github.com/ansible-collections/community.general/issues/4460, https://github.com/ansible-collections/community.general/issues/3729).
- gitlab_group_variable - add missing documentation about GitLab versions that support ``environment_scope`` and ``variable_type`` (https://github.com/ansible-collections/community.general/pull/4038).
- gitlab_group_variable - allow to set same variable name under different environment scopes. Due this change, the return value ``group_variable`` differs from previous version in check mode. It was counting ``updated`` values, because it was accidentally overwriting environment scopes (https://github.com/ansible-collections/community.general/pull/4038).
- gitlab_group_variable - fix idempotent change behaviour for float and integer variables (https://github.com/ansible-collections/community.general/pull/4038).
- gitlab_hook - avoid errors during idempotency check when an attribute does not exist (https://github.com/ansible-collections/community.general/pull/4668).
- gitlab_hook - handle more than 20 hooks when finding a hook (https://github.com/ansible-collections/community.general/pull/4491).
- gitlab_project - handle more than 20 namespaces when finding a namespace (https://github.com/ansible-collections/community.general/pull/4491).
- gitlab_project_members - handle more than 20 projects and users when finding a project resp. user (https://github.com/ansible-collections/community.general/pull/4491).
- gitlab_project_variable - ``value`` is not necessary when deleting variables (https://github.com/ansible-collections/community.general/pull/4150).
- gitlab_project_variable - add missing documentation about GitLab versions that support ``environment_scope`` and ``variable_type`` (https://github.com/ansible-collections/community.general/issues/4038).
- gitlab_project_variable - allow to set same variable name under different environment scopes. Due this change, the return value ``project_variable`` differs from previous version in check mode. It was counting ``updated`` values, because it was accidentally overwriting environment scopes (https://github.com/ansible-collections/community.general/issues/4038).
- gitlab_project_variable - fix idempotent change behaviour for float and integer variables (https://github.com/ansible-collections/community.general/issues/4038).
- gitlab_runner - make ``project`` and ``owned`` mutually exclusive (https://github.com/ansible-collections/community.general/pull/4136).
- gitlab_runner - use correct API endpoint to create and retrieve project level runners when using ``project`` (https://github.com/ansible-collections/community.general/pull/3965).
- gitlab_user - handle more than 20 users and SSH keys when finding a user resp. SSH key (https://github.com/ansible-collections/community.general/pull/4491).
- homebrew_cask - fix force install operation (https://github.com/ansible-collections/community.general/issues/3703).
- icinga2 inventory plugin - handle 404 error when filter produces no results (https://github.com/ansible-collections/community.general/issues/3875, https://github.com/ansible-collections/community.general/pull/3906).
- imc_rest - fixes the module failure due to the usage of ``itertools.izip_longest`` which is not available in Python 3 (https://github.com/ansible-collections/community.general/issues/4206).
- ini_file - when removing nothing do not report changed (https://github.com/ansible-collections/community.general/issues/4154).
- interfaces_file - fixed the check for existing option in interface (https://github.com/ansible-collections/community.general/issues/3841).
- jail connection plugin - replace deprecated ``distutils.spawn.find_executable`` with Ansible's ``get_bin_path`` to find the executable (https://github.com/ansible-collections/community.general/pull/3934).
- jira - fixed bug where module returns error related to dictionary key ``body`` (https://github.com/ansible-collections/community.general/issues/3419).
- keycloak - fix parameters types for ``defaultDefaultClientScopes`` and ``defaultOptionalClientScopes`` from list of dictionaries to list of strings (https://github.com/ansible-collections/community.general/pull/4526).
- keycloak_* - the documented ``validate_certs`` parameter was not taken into account when calling the ``open_url`` function in some cases, thus enforcing certificate validation even when ``validate_certs`` was set to ``false``. (https://github.com/ansible-collections/community.general/pull/4382)
- keycloak_realm - fix default groups and roles (https://github.com/ansible-collections/community.general/issues/4241).
- keycloak_user_federation - creating a user federation while specifying an ID (that does not exist yet) no longer fail with a 404 Not Found (https://github.com/ansible-collections/community.general/pull/4212).
- keycloak_user_federation - mappers auto-created by keycloak are matched and merged by their name and no longer create duplicated entries (https://github.com/ansible-collections/community.general/pull/4212).
- ldap_search - allow it to be used even in check mode (https://github.com/ansible-collections/community.general/issues/3619).
- linode inventory plugin - fix configuration handling relating to inventory filtering (https://github.com/ansible-collections/community.general/pull/4336).
- listen_ports_facts - local port regex was not handling well IPv6 only binding. Fixes the regex for ``ss`` (https://github.com/ansible-collections/community.general/pull/4092).
- lvol - allows logical volumes to be created with certain size arguments prefixed with ``+`` to preserve behavior of older versions of this module (https://github.com/ansible-collections/community.general/issues/3665).
- lxd connection plugin - replace deprecated ``distutils.spawn.find_executable`` with Ansible's ``get_bin_path`` to find the ``lxc`` executable (https://github.com/ansible-collections/community.general/pull/3934).
- lxd inventory plugin - do not crash if OS and release metadata are not present
  (https://github.com/ansible-collections/community.general/pull/4351).
- mail callback plugin - fix crash on Python 3 (https://github.com/ansible-collections/community.general/issues/4025, https://github.com/ansible-collections/community.general/pull/4026).
- mail callback plugin - fix encoding of the name of sender and recipient (https://github.com/ansible-collections/community.general/issues/4060, https://github.com/ansible-collections/community.general/pull/4061).
- mksysb - fixed bug for parameter ``backup_dmapi_fs`` was passing the wrong CLI argument (https://github.com/ansible-collections/community.general/pull/3295).
- nmcli - fix returning "changed" when no mask set for IPv4 or IPv6 addresses on task rerun (https://github.com/ansible-collections/community.general/issues/3768).
- nmcli - fix returning "changed" when routes parameters set, also suggest new routes4 and routes6 format (https://github.com/ansible-collections/community.general/issues/4131).
- nmcli - fixed falsely reported changed status when ``mtu`` is omitted with ``dummy`` connections (https://github.com/ansible-collections/community.general/issues/3612, https://github.com/ansible-collections/community.general/pull/3625).
- nmcli - pass ``flags``, ``ingress``, ``egress`` params to ``nmcli`` (https://github.com/ansible-collections/community.general/issues/1086).
- nrdp callback plugin - fix error ``string arguments without an encoding`` (https://github.com/ansible-collections/community.general/issues/3903).
- onepassword - search all valid configuration locations and use the first found (https://github.com/ansible-collections/community.general/pull/4640).
- opennebula inventory plugin - complete the implementation of ``constructable`` for opennebula inventory plugin. Now ``keyed_groups``, ``compose``, ``groups`` actually work (https://github.com/ansible-collections/community.general/issues/4497).
- opentelemetry - fix generating a trace with a task containing ``no_log: true`` (https://github.com/ansible-collections/community.general/pull/4043).
- opentelemetry callback plugin - fix task message attribute that is reported failed regardless of the task result (https://github.com/ansible-collections/community.general/pull/4624).
- opentelemetry callback plugin - fix warning for the include_tasks (https://github.com/ansible-collections/community.general/pull/4623).
- opentelemetry_plugin - honour ``ignore_errors`` when a task has failed instead of reporting an error (https://github.com/ansible-collections/community.general/pull/3837).
- pacman - Use ``--groups`` instead of ``--group`` (https://github.com/ansible-collections/community.general/pull/4312).
- pacman - fix URL based package installation (https://github.com/ansible-collections/community.general/pull/4286, https://github.com/ansible-collections/community.general/issues/4285).
- pacman - fix ``upgrade=yes`` (https://github.com/ansible-collections/community.general/pull/4275, https://github.com/ansible-collections/community.general/issues/4274).
- pacman - fixed bug where ``absent`` state did not work for locally installed packages (https://github.com/ansible-collections/community.general/pull/4464).
- pacman - make sure that ``packages`` is always returned when ``name`` or ``upgrade`` is specified, also if nothing is done (https://github.com/ansible-collections/community.general/pull/4329).
- pacman - when the ``update_cache`` option is combined with another option such as ``upgrade``, report ``changed`` based on the actions performed by the latter option. This was the behavior in community.general 4.4.0 and before. In community.general 4.5.0, a task combining these options would always report ``changed`` (https://github.com/ansible-collections/community.general/pull/4318).
- passwordstore lookup plugin - fix error detection for non-English locales (https://github.com/ansible-collections/community.general/pull/4219).
- passwordstore lookup plugin - prevent returning path names as passwords by accident (https://github.com/ansible-collections/community.general/issues/4185, https://github.com/ansible-collections/community.general/pull/4192).
- passwordstore lookup plugin - replace deprecated ``distutils.util.strtobool`` with Ansible's ``convert_bool.boolean`` to interpret values for the ``create``, ``returnall``, ``overwrite``, 'backup``, and ``nosymbols`` options (https://github.com/ansible-collections/community.general/pull/3934).
- pipx - passes the correct command line option ``--include-apps`` (https://github.com/ansible-collections/community.general/issues/3791).
- pritunl - fixed bug where pritunl plugin api add unneeded data in ``auth_string`` parameter (https://github.com/ansible-collections/community.general/issues/4527).
- proxmox - fixed ``onboot`` parameter causing module failures when undefined (https://github.com/ansible-collections/community.general/issues/3844).
- proxmox inventory plugin - always convert strings that follow the ``key=value[,key=value[...]]`` form into dictionaries (https://github.com/ansible-collections/community.general/pull/4349).
- proxmox inventory plugin - fix error when parsing container with LXC configs (https://github.com/ansible-collections/community.general/issues/4472, https://github.com/ansible-collections/community.general/pull/4472).
- proxmox inventory plugin - fixed the ``description`` field being ignored if it contained a comma (https://github.com/ansible-collections/community.general/issues/4348).
- proxmox inventory plugin - fixed the ``tags_parsed`` field when Proxmox returns a single space for the ``tags`` entry (https://github.com/ansible-collections/community.general/pull/4378).
- proxmox_kvm - fix a bug when getting a state of VM without name will fail (https://github.com/ansible-collections/community.general/pull/4508).
- proxmox_kvm - fix error in check when creating or cloning (https://github.com/ansible-collections/community.general/pull/4306).
- proxmox_kvm - fix error when checking whether Proxmox VM exists (https://github.com/ansible-collections/community.general/pull/4287).
- python_requirements_info - fails if version operator used without version (https://github.com/ansible-collections/community.general/pull/3785).
- python_requirements_info - store ``mismatched`` return values per package as documented in the module (https://github.com/ansible-collections/community.general/pull/4078).
- redfish_command - the iLO4 Redfish implementation only supports the ``image_url`` parameter in the underlying API calls to ``VirtualMediaInsert`` and ``VirtualMediaEject``. Any values set (or the defaults) for ``write_protected`` or ``inserted`` will be ignored (https://github.com/ansible-collections/community.general/pull/4596).
- redis* modules - fix call to ``module.fail_json`` when failing because of missing Python libraries (https://github.com/ansible-collections/community.general/pull/4733).
- say callback plugin - replace deprecated ``distutils.spawn.find_executable`` with Ansible's ``get_bin_path`` to find the ``say`` resp. ``espeak`` executables (https://github.com/ansible-collections/community.general/pull/3934).
- scaleway_user_data - fix double-quote added where no double-quote is needed to user data in scaleway's server (``Content-type`` -> ``Content-Type``) (https://github.com/ansible-collections/community.general/pull/3940).
- slack - add ``charset`` to HTTP headers to avoid Slack API warning (https://github.com/ansible-collections/community.general/issues/3932).
- terraform - fix command options being ignored during planned/plan in function ``build_plan`` such as ``lock`` or ``lock_timeout`` (https://github.com/ansible-collections/community.general/issues/3707, https://github.com/ansible-collections/community.general/pull/3726).
- terraform - fix list initialization to support both Python 2 and Python 3 (https://github.com/ansible-collections/community.general/issues/4531).
- vdo - fix options error (https://github.com/ansible-collections/community.general/pull/4163).
- xattr - fix exception caused by ``_run_xattr()`` raising a ``ValueError`` due to a mishandling of base64-encoded value (https://github.com/ansible-collections/community.general/issues/3673).
- xbps - fix error message that is reported when installing packages fails (https://github.com/ansible-collections/community.general/pull/4438).
- xcc_redfish_command - for compatibility due to Redfish spec changes the virtualMedia resource location changed from Manager to System (https://github.com/ansible-collections/community.general/pull/4682).
- yarn - fix incorrect handling of ``yarn list`` and ``yarn global list`` output that could result in fatal error (https://github.com/ansible-collections/community.general/pull/4050).
- yarn - fix incorrectly reported status when installing a package globally (https://github.com/ansible-collections/community.general/issues/4045, https://github.com/ansible-collections/community.general/pull/4050).
- yarn - fix missing ``~`` expansion in yarn global install folder which resulted in incorrect task status (https://github.com/ansible-collections/community.general/issues/4045, https://github.com/ansible-collections/community.general/pull/4048).
- yum_versionlock - fix matching of existing entries with names passed to the module. Match yum and dnf lock format (https://github.com/ansible-collections/community.general/pull/4183).
- zfs - fix wrong quoting of properties (https://github.com/ansible-collections/community.general/issues/4707, https://github.com/ansible-collections/community.general/pull/4726).
- zone connection plugin - replace deprecated ``distutils.spawn.find_executable`` with Ansible's ``get_bin_path`` to find the executable (https://github.com/ansible-collections/community.general/pull/3934).
- zypper - fix undefined variable when running in check mode (https://github.com/ansible-collections/community.general/pull/4667).
- zypper - fixed bug that caused zypper to always report [ok] and do nothing on ``state=present`` when all packages in ``name`` had a version specification (https://github.com/ansible-collections/community.general/issues/4371, https://github.com/ansible-collections/community.general/pull/4421).

community.grafana
~~~~~~~~~~~~~~~~~

- Fix an issue with grafana_datasource for Prometheus with basic auth credential management. (#204)
- Fix an issue with threema notification channel that was not creating gateway, recipient and api_secret in Grafana. (#208)
- Fix issue with datasource names that could not contain slashes (#125)

community.hrobot
~~~~~~~~~~~~~~~~

- Include ``simplified_bsd.txt`` license file for the ``robot`` and ``failover`` module utils.
- boot - fix incorrect handling of SSH authorized keys (https://github.com/ansible-collections/community.hrobot/issues/32, https://github.com/ansible-collections/community.hrobot/pull/33).
- robot inventory plugin - do not crash if a server neither has name or primary IP set. Instead, fall back to using the server's number as the name. This can happen if unnamed rack reservations show up in your server list (https://github.com/ansible-collections/community.hrobot/issues/40, https://github.com/ansible-collections/community.hrobot/pull/47).

community.libvirt
~~~~~~~~~~~~~~~~~

- replace deprecated ``distutils.spawn.find_executable`` with Ansible's ``get_bin_path`` in ``_search_executable`` function.

community.mysql
~~~~~~~~~~~~~~~

- Collection core functions - fixes related to the mysqlclient Python connector (https://github.com/ansible-collections/community.mysql/issues/292).
- Collection core functions - use vendored version of ``distutils.version`` instead of the deprecated Python standard library ``distutils`` (https://github.com/ansible-collections/community.mysql/pull/269).
- Include ``PSF-license.txt`` file for ``plugins/module_utils/_version.py``.
- mysql_replication - fails when using the `primary_use_gtid` option with `slave_pos` or `replica_pos` (https://github.com/ansible-collections/community.mysql/issues/335).
- mysql_role - make the ``set_default_role_all`` parameter actually working (https://github.com/ansible-collections/community.mysql/pull/282).
- mysql_role - remove redundant connection closing (https://github.com/ansible-collections/community.mysql/pull/330).
- mysql_user - fix missing dynamic privileges after revoke and grant privileges to user (https://github.com/ansible-collections/community.mysql/issues/120).
- mysql_user - fix parsing privs when a user has roles assigned (https://github.com/ansible-collections/community.mysql/issues/231).
- mysql_user - fix the possibility for a race condition that breaks certain (circular) replication configurations when ``DROP USER`` is executed on multiple nodes in the replica set. Adding ``IF EXISTS`` avoids the need to use ``sql_log_bin: no`` making the statement always replication safe (https://github.com/ansible-collections/community.mysql/pull/287).

community.network
~~~~~~~~~~~~~~~~~

- Collection core functions - use vendored version of ``distutils.version`` instead of the deprecated Python standard library ``distutils``.
- Include ``PSF-license.txt`` file for ``plugins/module_utils/_version.py``.
- ce - Modify the bug in the query configuration method (https://github.com/ansible-collections/community.network/pull/56).
- community.network.ce_switchport - fix error causing by ``KeyError:`` ``host`` due to properties aren't used anywhere (https://github.com/ansible-collections/community.network/issues/313)
- exos_config - fix a hang due to an unexpected prompt during save_when (https://github.com/ansible-collections/community.network/pull/110).
- weos4 cliconf plugin - fix linting errors in documentation data (https://github.com/ansible-collections/community.network/pull/368).

community.okd
~~~~~~~~~~~~~

- fix ocp auth failing against cluster api url with trailing slash (https://github.com/openshift/community.okd/issues/139)

community.postgresql
~~~~~~~~~~~~~~~~~~~~

- Collection core functions - use vendored version of ``distutils.version`` instead of the deprecated Python standard library ``distutils`` (https://github.com/ansible-collections/community.postgresql/pull/179).
- Include ``PSF-license.txt`` file for ``plugins/module_utils/_version.py``.
- collection core functions - fix attribute error `nonetype` by always calling `ensure_required_libs` (https://github.com/ansible-collections/community.postgresql/issues/252).
- module core functions - get rid of the deprecated psycopg2 connection alias ``database`` in favor of ``dbname`` when psycopg2 is 2.7+ (https://github.com/ansible-collections/community.postgresql/pull/196).
- postgres_info - It now works on AWS RDS Postgres.
- postgres_info - Specific info (namespaces, extensions, languages) of each database was not being shown properly. Instead, the info from the DB that was connected was always being shown (https://github.com/ansible-collections/community.postgresql/issues/172).
- postgresql_db - get rid of the deprecated psycopg2 connection alias ``database`` in favor of ``dbname`` when psycopg2 is 2.7+ is used (https://github.com/ansible-collections/community.postgresql/issues/194, https://github.com/ansible-collections/community.postgresql/pull/196).
- postgresql_ext - Handle postgresql extension updates through path validation instead of version comparison (https://github.com/ansible-collections/community.postgresql/issues/129).
- postgresql_query - cannot handle .sql file with \\n at end of file (https://github.com/ansible-collections/community.postgresql/issues/180).

community.proxysql
~~~~~~~~~~~~~~~~~~

- module_utils/mysql.py - Proxysql version suffix may not be an integer (https://github.com/ansible-collections/community.proxysql/pull/96).
- roles/proxysql - As of ProxySQL 2.4.0, `client_found_rows` mysql variable has been removed (https://github.com/ansible-collections/community.proxysql/pull/101).

community.rabbitmq
~~~~~~~~~~~~~~~~~~

- Collection core functions - use vendored version of ``distutils.version`` instead of the deprecated Python standard library ``distutils``.
- Include ``PSF-license.txt`` file for ``plugins/module_utils/_version.py``.

community.routeros
~~~~~~~~~~~~~~~~~~

- query - fix query function check for ``.id`` vs. ``id`` arguments to not conflict with routeros arguments like ``identity`` (https://github.com/ansible-collections/community.routeros/pull/68, https://github.com/ansible-collections/community.routeros/issues/67).
- quoting and unquoting filter plugins, api module - handle the escape sequence ``\_`` correctly as escaping a space and not an underscore (https://github.com/ansible-collections/community.routeros/pull/89).

community.sops
~~~~~~~~~~~~~~

- Include ``simplified_bsd.txt`` license file for the ``sops`` module utils.

community.vmware
~~~~~~~~~~~~~~~~

- Various modules and plugins - use vendored version of ``distutils.version`` included in ansible-core 2.12 if available. This avoids breakage when ``distutils`` is removed from the standard library of Python 3.12. Note that ansible-core 2.11, ansible-base 2.10 and Ansible 2.9 are right now not compatible with Python 3.12, hence this fix does not target these ansible-core/-base/2.9 versions.
- create_nic - add advanced SR-IOV options from the VMware API (PCI dev PF/VF backing and guest OS MTU change)
- vcenter_folder - fixed folders search collision issue (https://github.com/ansible-collections/community.vmware/issues/1112).
- vmware_dvs_host - match the list of the host nics in the correct order based on the uplink port name in vCenter (https://github.com/ansible-collections/community.vmware/issues/1242).
- vmware_dvs_portgroup - Fix an idempotency issue when `num_ports` is unset (https://github.com/ansible-collections/community.vmware/pull/1286).
- vmware_guest - when ``customization.password`` is not defined, the Administrator password is made empty instead of setting it to string 'None' (https://github.com/ansible-collections/community.vmware/issues/1017).
- vmware_guest_network - fix a bug that can crash the module due to an uncaught exception (https://github.com/ansible-collections/community.vmware/issues/25).
- vmware_guest_powerstate - Ignore trailing `/` in `folder` parameter like other guest modules do (https://github.com/ansible-collections/community.vmware/issues/1238).
- vmware_guest_powerstate - `shutdownguest` power state is not idempotent (https://github.com/ansible-collections/community.vmware/pull/1227).
- vmware_host_powerstate - Do not execute the powerstate changes in check_mode. (https://github.com/ansible-collections/community.vmware/pull/1299).
- vmware_vmotion - Like already define in the examples, allow Storage vMotion without defining a resource pool. (https://github.com/ansible-collections/community.vmware/pull/1236).

community.windows
~~~~~~~~~~~~~~~~~

- win_domain_user - Module now properly captures and reports bad password - https://github.com/ansible-collections/community.windows/issues/316
- win_domain_user - Module now reports user created and changed properly - https://github.com/ansible-collections/community.windows/issues/316
- win_domain_user - The AD user's existing identity is searched using their sAMAccountName name preferentially and falls back to the provided name property instead - https://github.com/ansible-collections/community.windows/issues/344
- win_hotfix - Supports hotfixes that contain multiple updates inside the supplied update msu - https://github.com/ansible-collections/community.windows/issues/284
- win_iis_virtualdirectory - Fixed an issue where virtual directory information could not be obtained correctly when the parameter ``application`` was set
- win_iis_webapplication - Fix physical path check for broken configurations - https://github.com/ansible-collections/community.windows/pull/385
- win_rds_cap - Fix SID lookup with any account ending with the ``@builtin`` UPN suffix
- win_rds_rap - Fix SID lookup with any account ending with the ``@builtin`` UPN suffix
- win_region - Fix junk output when copying settings across users
- win_scoop - Fix bootstrapping process to properly work when running as admin
- win_scoop_bucket - Fix handling of output and errors from each scoop command

community.zabbix
~~~~~~~~~~~~~~~~

- Include ``PSF-license.txt`` file for ``plugins/module_utils/_version.py``.
- Various modules and plugins - use vendored version of ``distutils.version`` instead of the deprecated Python standard library ``distutils`` (https://github.com/ansible-collections/community.zabbix/pull/603). This superseedes #597.
- ZapiWrapper (module_utils) - fix only partial zabbix version is returned.
- template - use templateid property when linking templates for ``template.create`` and ``template.update`` API calls.
- zabbix inventory - Moved ZABBIX_VALIDATE_CERTS to correct option, validate_certs.
- zabbix_action - will no longer wipe `esc_step_to` and `esc_step_from` (https://github.com/ansible-collections/community.zabbix/issues/692)
- zabbix_agent - Create the actual configuration file for Windows setups.
- zabbix_agent - Fix typo for correct using the zabbix_windows_service.exists
- zabbix_agent - Install Zabbix packages when zabbix_repo == other is used with yum.
- zabbix_agent - Install the Agent for MacOSX sooner than its configuration.
- zabbix_agent - The ``Install gpg key`` task for Debian did not work when a http proxy is configured.
- zabbix_agent - Use the correct URL with correct version.
- zabbix_agent - Use the correct path to determine Zabbix Agent 2 installation on Windows.
- zabbix_agent - Using the correct hostgroup as default now.
- zabbix_agent - added support for zabbix-agent on Ubuntu 22.04 (https://github.com/ansible-collections/community.zabbix/pull/681)
- zabbix_agent - fix for the autopsk, incl. tests with Molecule.
- zabbix_agent - now properly creates webroot for issuing LE certificates (https://github.com/ansible-collections/community.zabbix/pull/677, https://github.com/ansible-collections/community.zabbix/pull/682)
- zabbix_agent - tlspsk_auto to support become on Linux and ignore on windows
- zabbix_host - Added small notification that an user should have read access to get hostgroups overview.
- zabbix_host - adapter changed properties for interface comparisson
- zabbix_maintenance - should now work when creating maintenace on Zabbix 6.0 server
- zabbix_proxy (module) - passive proxy should be now correctly created in Zabbix 6.0 (https://github.com/ansible-collections/community.zabbix/pull/697)
- zabbix_proxy (role) - fixed accidental regression of TLS psk file being generated for passive agent (#528) caused in (#663) (https://github.com/ansible-collections/community.zabbix/issues/680)
- zabbix_proxy - 'zcat' the zipped sql files to /tmp before executing it.
- zabbix_proxy - Check MySQL version before settings mysql_innodb_default_row_format value.
- zabbix_proxy - Install Zabbix packages when zabbix_repo == other is used with yum.
- zabbix_server - 'zcat' the zipped sql files to /tmp before executing it.
- zabbix_server - Check MySQL version before settings mysql_innodb_default_row_format value.
- zabbix_server - Install Zabbix packages when zabbix_repo == other is used with yum.
- zabbix_template - setting correct null values to fix unintentional changes
- zabbix_user - fix zabbix_user require password only on internal.
- zabbix_web - Added some default variables if the geerlingguys apache role is not used.
- zabbix_web - Specified the correct versions for php.

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

dellemc.enterprise_sonic
~~~~~~~~~~~~~~~~~~~~~~~~

- Fixes incorrect grouping of parameters to be used for invocation of the "send_command" API for sending commands to a device. (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/71).
- aaa - fix a logic mistake in validating authentication data (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/52).
- aaa - modify a 'delete' test case to eliminate a subsequent idempotency failure for a 'merge' test case restoring the deleted attribute. The attribute that was being used for the test case had a non-idempotent effect in the SONiC switch functional code. This did not allow verification of the correct idempotency logic in the Ansible handling of the attribute 'delete' and 'restore' functionality. (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/80).
- bgp - removed unnecessary brackets in a configuration handling instruction (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/52).
- bgp_neighbors - add a 'maxsplit' value in facts handling (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/52).
- bgp_neighbors - removed unnecessary brackets in configuration handling instructions (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/52).
- radius_server - add a missing 'get' in configuration handling (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/52).
- system - delete an initial test case requiring 'changed' state for deletion of final configuration attributes assuming 'leftover' configuration from previous execution. Replace this initial test case with cleanup of any residual state with no assumption of leftover residual state. Do the final deletion of configuration at the end of the test instead of at the beginning to retain verification that the deletion works correctly (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/87).
- tacacs_server - correct an argument spelling error in facts handling (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/52).

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
- bigip_command - fixed a bug that interpreted a pipe symbol inside an input string as pipe used to combine commands
- bigip_device_certificate - adds missing space to tmsh command
- bigip_device_info - changes cipher and cipher_group parameters to register when the actual value is 'none'.
- bigip_device_info - fixed bug regarding handling of negated meta options.
- bigip_device_license - fixed issue that resulted in only first of the multiple add-on keys getting added to the device.
- bigip_device_syslog - this change is done so that only unescaped " is replaced with ' in the value of include parameter.
- bigip_firewall_address_list - fixed issue where addresses that contained RD would cause an error.
- bigip_gtm_wide_ip - fix idempotency bugs encountered when adding/removing irules, pools and last_resort_pool
- bigip_gtm_wide_ip - fixed a bug that prevented creation of gtm wide ips in disabled state.
- bigip_gtm_wide_ip - fixed inability to change persistence setting on existing wide ip objects
- bigip_gtm_wide_ip - irules can be added to existing gtm wide ips
- bigip_monitor_http - fixed extraction of ip from the destination value
- bigip_monitor_https - fixed extraction of ip from the destination value
- bigip_monitor_ldap - fixed idempotency issue with security parameter in module.
- bigip_node - the fqdn_autopopulate is now only enabled when fqdn is specified.
- fix for displaying src, checksum and other parameters when running ucs_fetch module
- fix for source capability for bigip_device_auth_ldap module
- multiple modules - Add no_log=False setting to update_password parameter in respective modules avoid false positive security warnings.

fortinet.fortios
~~~~~~~~~~~~~~~~

- Add defaut value for enable_log param.
- Fix import issues in sanity-test and improve unit tests.
- Fix issues in version mismatch logic.
- Fix parameter-list-no-elements error in sanity-test.
- Fix status issue in fortios_json_generic().
- Fix syntax issue in python2.7.
- Fix the issue of inconsistent data types in different schemas.
- Fix the syntax error in the three wireless_controller_hotspot20 modules.
- Relicense the FortiOS Collection under GPLv3+.
- Update the logic in check_legacy_fortiosapi.
- Use collection version number in the doc.

infoblox.nios_modules
~~~~~~~~~~~~~~~~~~~~~

- Ansible playbook fails to update canonical name of CName Record `#97 <https://github.com/infobloxopen/infoblox-ansible/pull/97>`_
- nios_a_record module - KeyError 'old_ipv4addr' `#79 <https://github.com/infobloxopen/infoblox-ansible/issues/79>`_

junipernetworks.junos
~~~~~~~~~~~~~~~~~~~~~

- Fix incorrect param pass to to_text.
- Fix junos_acl fact gathering when only destination port defined (https://github.com/ansible-collections/junipernetworks.junos/issues/268).
- Fix junos_command output when empty config response is received for show commands (https://github.com/ansible-collections/junipernetworks.junos/issues/249).
- Fix ospf router_id overlap issue.

kubernetes.core
~~~~~~~~~~~~~~~

- Catch expectation raised when the process is waiting for resources (https://github.com/ansible-collections/kubernetes.core/issues/407).
- Remove `omit` placeholder when defining resource using template parameter (https://github.com/ansible-collections/kubernetes.core/issues/431).
- Various modules and plugins - use vendored version of ``distutils.version`` instead of the deprecated Python standard library ``distutils`` (https://github.com/ansible-collections/kubernetes.core/pull/314).
- common - Ensure the label_selectors parameter of _wait_for method is optional.
- helm_template - evaluate release_values after values_files, insuring highest precedence (now same behavior as in helm module). (https://github.com/ansible-collections/kubernetes.core/pull/348)
- import exception from ``kubernetes.client.rest``.
- k8s - fix the issue when trying to delete resources using label_selectors options (https://github.com/ansible-collections/kubernetes.core/issues/433).
- k8s_cp - fix issue when using parameter local_path with file on managed node. (https://github.com/ansible-collections/kubernetes.core/issues/421).
- k8s_drain - fix error caused by accessing an undefined variable when pods have local storage (https://github.com/ansible-collections/kubernetes.core/issues/292).
- k8s_drain - fix error occurring when trying to drain node with disable_eviction set to yes (https://github.com/ansible-collections/kubernetes.core/issues/416).
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
- na_ontap_cifs - fixed `symlink_properties` option silently ignored for cifs share creation when using REST.
- na_ontap_cifs - fixed error in modifying comment if it is not set while creating CIFS share in REST.
- na_ontap_cifs_local_user_modify - KeyError on ``description`` or ``full_name`` with REST.
- na_ontap_cifs_local_user_modify - unexpected argument ``name`` error with REST.
- na_ontap_cifs_server -  error out if ZAPI only options ``force`` or ``workgroup`` are used with REST.
- na_ontap_cluster_config - fix the role to be able to create intercluster LIFs with REST (ipspace is required).
- na_ontap_cluster_peer - Fixed KeyError if both ``source_intercluster_lifs`` and ``dest_intercluster_lifs`` not present in cluster create.
- na_ontap_command - document that a READONLY user is not supported, even for show commands.
- na_ontap_command - fix typo in example.
- na_ontap_disk_options - ONTAP 9.10.1 returns on/off rather than True/False.
- na_ontap_export_policy - fix error if more than 1 verser matched search name, the wrong uuid could be given
- na_ontap_export_policy_rule - Fixed bug that prevent ZAPI and REST calls from working correctly
- na_ontap_igroup - ``force_remove_initiator`` option was ignored when removing initiators from existing igroup.
- na_ontap_info - Add active_directory_account_info.
- na_ontap_info - Fixes issue with na_ontap_info failing in 9.1 because of ``job-schedule-cluster``.
- na_ontap_info - fix KeyError on node for aggr_efficiency_info option against a metrocluster system.
- na_ontap_interface - ignore ``vserver`` when using REST if role is one of 'cluster', 'node-mgmt', 'intercluster', 'cluster-mgmt'.
- na_ontap_interface - rename fails with 'inconsistency in rename action' for cluster interface with REST.
- na_ontap_iscsi - Fixed issue with ``start_state`` always being set to stopped when creating an ISCSI.
- na_ontap_iscsi - fixed error starting iscsi service on vserver where Service, adapter, or operation already started.
- na_ontap_login_messages - fix typo in examples for username.
- na_ontap_lun - Fixed KeyError on options ``force_resize``, ``force_remove`` and ``force_remove_fenced`` in Zapi.
- na_ontap_lun - Fixed ``force_remove`` option silently ignored in REST.
- na_ontap_lun_map - Fixed bug when deleting lun map using REST.
- na_ontap_lun_map - TypeError - '>' not supported between instances of 'int' and 'str '.
- na_ontap_lun_map - fixed bugs resulting in REST support to not work.
- na_ontap_net_ifgrp - fix error in modify ports with zapi.
- na_ontap_net_routes - metric was not always modified with ZAPI.
- na_ontap_net_routes - support cluster-scoped routes with REST.
- na_ontap_nfs - fix TypeError on NoneType as ``tcp_max_xfer_size`` is not supported in earlier ONTAP versions.
- na_ontap_nfs - fix ``Extra input`` error with ZAPI for ``is-nfsv4-enabled``.
- na_ontap_nvme - fixed ``status_admin`` option is ignored if set to False when creating nvme service in REST.
- na_ontap_nvme - fixed invalid boolean value error for ``status_admin`` when creating nvme service in ZAPI.
- na_ontap_qtree - Fixed issue with ``oplocks`` not being changed during a modify in Zapi.
- na_ontap_qtree - Fixed issue with ``oplocks`` not warning user about not being supported in REST
- na_ontap_quotas - fix idempotency issue on ``disk_limit`` and ``soft_disk_limit``.
- na_ontap_rest_info - Fixed an issues with adding field to specific info that didn't have a direct REST equivalent.
- na_ontap_rest_info - Fixed example with wrong indentation for ``use_python_keys``.
- na_ontap_security_certificates - ``intermediate_certificates`` option was ignored.
- na_ontap_service_policy - fix examples in documentation.
- na_ontap_service_policy - fixed error in modify by changing resulting json of an existing record in REST.
- na_ontap_snapmirror - Added use_rest condition for the REST support to work when use_rest `always`.
- na_ontap_snapmirror - when using REST with a policy, fix AttributeError - 'str' object has no attribute 'get'.
- na_ontap_snapmirror - when using ZAPI, wait for the relationship to be quiesced before breaking.
- na_ontap_snapshot - add error message if volume is not found with REST.
- na_ontap_snapshot - fix key error on volume when using REST.
- na_ontap_snapshot_policy - Do not validate parameter when state is ``absent`` and fix KeyError on ``comment``.
- na_ontap_svm - fixed KeyError issue on protocols when vserver is stopped.
- na_ontap_user - Fixed TypeError 'tuple' object does not support item assignment.
- na_ontap_user - Fixed issue when attempting to change pasword for absent user when set_password is set.
- na_ontap_user - Fixed lock state is not set if password is not changed.
- na_ontap_volume - Fixed error when creating a flexGroup when ``aggregate_name`` and ``aggr_list_multiplier`` are not set in rest.
- na_ontap_volume - Fixed error with unmounting junction_path in rest.
- na_ontap_volume - Fixed issue that would fail the module in REST when changing `is_online` if two vserver volume had the same name.
- na_ontap_volume - If using REST and ONTAP 9.6 and `efficiency_policy` module will fail as `efficiency_policy` is not supported in ONTAP 9.6.
- na_ontap_volume - QOS policy was not set when using NAS application.
- na_ontap_volume - correctly warn when attempting to modify NAS application.
- na_ontap_volume - do not attempt to mount volume if current state is offline.
- na_ontap_volume - do not set encrypt on modify, as it is already handled with specialized ZAPI calls.
- na_ontap_volume - fix idempotency issue with compression settings when using REST.
- na_ontap_volume - report error when attempting to change the nas_application tiering control from disalllowed to required, or reciprocally.
- na_ontap_volume - use ``time_out`` value when creating/modifying/deleting volumes with REST rathar than hardcoded value.
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
- nb_inventory - Ensure inventory works on NetBox versions without the site group model [#781](https://github.com/netbox-community/ansible_modules/pull/781)
- nb_inventory - Fix netbox_inventory site_group group_by @ryanmerolle in [#780](https://github.com/netbox-community/ansible_modules/pull/780)
- nb_lookup - Fix documentation of validate_cert [#629](https://github.com/netbox-community/ansible_modules/pull/629)
- netbox_contact_group - Fix field description [#762](https://github.com/netbox-community/ansible_modules/pull/762)
- netbox_rack - Add location as a query parameter for uniqueness check [#751](https://github.com/netbox-community/ansible_modules/pull/751)
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
- Fix the admin user name when using keycloak (https://github.com/oVirt/ovirt-ansible-collection/pull/488).
- Make storage_format optional - do not fail if missing (https://github.com/oVirt/ovirt-ansible-collection/pull/471).
- Use cryptography < 37.0.0, as 37.0.0 emits a warning that fails testing. (https://github.com/oVirt/ovirt-ansible-collection/pull/492).
- Use rstcheck < 3.5.0, as 3.5.0 emits a warning that fails testing. (https://github.com/oVirt/ovirt-ansible-collection/pull/490).
- cluster_upgrade - fix wait_condition (https://github.com/oVirt/ovirt-ansible-collection/pull/510).
- hosted_engine_setup - Add OpenSCAP security profile name parameter (https://github.com/oVirt/ovirt-ansible-collection/pull/411).
- hosted_engine_setup - Add an option to set the storage format when createing a storage domain and use it (https://github.com/oVirt/ovirt-ansible-collection/pull/463).
- hosted_engine_setup - Adjust files permissions (https://github.com/oVirt/ovirt-ansible-collection/pull/409).
- hosted_engine_setup - Allocate 128MiB instead of 1GiB for he_metadata (https://github.com/oVirt/ovirt-ansible-collection/pull/489).
- hosted_engine_setup - Collect logs also on failures in 03_hosted_engine_final_tasks.yml (https://github.com/oVirt/ovirt-ansible-collection/pull/504).
- hosted_engine_setup - Fix call to engine-psql for vds_spm_id (https://github.com/oVirt/ovirt-ansible-collection/pull/459).
- hosted_engine_setup - Fix cloud-init package removal in airgapped environment (https://github.com/oVirt/ovirt-ansible-collection/pull/442)
- hosted_engine_setup - Fix keycloak activation/checking (https://github.com/oVirt/ovirt-ansible-collection/pull/509).
- hosted_engine_setup - Remove SPICE graphic protocol (https://github.com/oVirt/ovirt-ansible-collection/pull/394).
- hosted_engine_setup - Replace xml community module (https://github.com/oVirt/ovirt-ansible-collection/pull/438).
- hosted_engine_setup - Require 'detail' to be 'Up' (https://github.com/oVirt/ovirt-ansible-collection/pull/498).
- hosted_engine_setup - Support disa stig profile (https://github.com/oVirt/ovirt-ansible-collection/pull/426).
- hosted_engine_setup - Use cat command (https://github.com/oVirt/ovirt-ansible-collection/pull/443).
- hosted_engine_setup - Use tpgt in iscsi login (https://github.com/oVirt/ovirt-ansible-collection/pull/338)
- hosted_engine_setup - fix archive ownership (https://github.com/oVirt/ovirt-ansible-collection/pull/501).
- image_template - Remove static no - unsupported in ansible 2.12 (https://github.com/oVirt/ovirt-ansible-collection/pull/341).
- infra - add warning for multiple storage connections (https://github.com/oVirt/ovirt-ansible-collection/pull/500).
- invenory - Fix url address (https://github.com/oVirt/ovirt-ansible-collection/pull/482).
- ovirt_host - Fix failed_state_after_reinstall condition (https://github.com/oVirt/ovirt-ansible-collection/pull/371).
- ovirt_template - Fix creating templates where the base template version number is not 1 (https://github.com/oVirt/ovirt-ansible-collection/pull/370).
- ovirt_vm - Fix creating a RAW VM from a COW template  (https://github.com/oVirt/ovirt-ansible-collection/pull/466).
- repositories - Fix dnf module variable (https://github.com/oVirt/ovirt-ansible-collection/pull/454).
- repositories - fix force flag on subscription-manager (https://github.com/oVirt/ovirt-ansible-collection/pull/430).

purestorage.flasharray
~~~~~~~~~~~~~~~~~~~~~~

- purefa_certs - Allow a certificate to be imported over an existing SSL certificate
- purefa_eula - Reolve EULA signing issue
- purefa_host - Allow multi-host creation without requiring a suffix string
- purefa_info - Fix issue where remote arrays are not in a valid connected state
- purefa_info - Fix space reporting issue
- purefa_network - Fix bug introduced with management of FC ports
- purefa_policy - Fix idempotency issue with quota policy rules
- purefa_policy - Fix issue when creating multiple rules in an NFS policy
- purefa_policy - Fix issue with SMB Policy creation
- purefa_subnet - Fix subnet update checks when no gateway in existing subnet configuration

splunk.es
~~~~~~~~~

- Fix ansible test sanity failures and fix flake8 issues.

t_systems_mms.icinga_director
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- added a fix for the new scheduled_downtime module (https://github.com/T-Systems-MMS/ansible-collection-icinga-director/pull/150)
- role: add check_command to icinga_service_apply (https://github.com/T-Systems-MMS/ansible-collection-icinga-director/pull/161)

theforeman.foreman
~~~~~~~~~~~~~~~~~~

- callback plugin - include timezone information in the callback reported data (https://github.com/theforeman/foreman-ansible-modules/issues/1171)
- content_upload - clarify that ``src`` refers to a remote file (https://bugzilla.redhat.com/show_bug.cgi?id=2055416)
- content_upload - properly detect SRPMs and ensure idempotency during uploads (https://github.com/theforeman/foreman-ansible-modules/issues/1274)
- host, hostgroup - fix updating puppetclasses while also updating description (or other string-like attributes) (https://github.com/theforeman/foreman-ansible-modules/issues/1231)
- hostgroup, location - don't fail when trying to delete a Hostgroup or Location where the parent is already absent
- inventory plugin - fetch *all* facts, not only the first 250, when using the old Hosts API
- inventory plugin - fix caching for Report API (https://github.com/theforeman/foreman-ansible-modules/issues/1246)
- operatingsystem - find operatingsystems by title or full (name,major,minor) tuple (https://github.com/theforeman/foreman-ansible-modules/issues/1401)
- os_default_template, provisioning_template - don't document invalid template kind ``ptable`` (https://bugzilla.redhat.com/show_bug.cgi?id=1970132)

vyos.vyos
~~~~~~~~~

- Add symlink of modules under plugins/action

Known Issues
------------

Ansible-core
~~~~~~~~~~~~

- get_url - document ``check_mode`` correctly with unreliable changed status (https://github.com/ansible/ansible/issues/65687).

ansible.netcommon
~~~~~~~~~~~~~~~~~

- eos - When using eos modules on Ansible 2.9, tasks will occasionally fail with ``import_modules`` enabled. This can be avoided by setting ``import_modules: no``

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

Connection
~~~~~~~~~~

- community.zabbix.httpapi - Use httpapi to run command on network appliances

Filter
~~~~~~

- community.general.counter - Counts hashable elements in a sequence
- community.hashi_vault.vault_login_token - Extracts the client token from a Vault login response

Httpapi
~~~~~~~

- community.zabbix.jsonrpc - HttpApi Plugin for Zabbix

Lookup
~~~~~~

- community.hashi_vault.vault_ansible_settings - Returns plugin settings (options)
- community.hashi_vault.vault_kv1_get - Get a secret from HashiCorp Vault's KV version 1 secret store
- community.hashi_vault.vault_kv2_get - Get a secret from HashiCorp Vault's KV version 2 secret store
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

community.grafana
~~~~~~~~~~~~~~~~~

- community.grafana.grafana_organization - Manage Grafana Organization

community.hashi_vault
~~~~~~~~~~~~~~~~~~~~~

- community.hashi_vault.vault_kv1_get - Get a secret from HashiCorp Vault's KV version 1 secret store
- community.hashi_vault.vault_kv2_get - Get a secret from HashiCorp Vault's KV version 2 secret store
- community.hashi_vault.vault_login - Perform a login operation against HashiCorp Vault
- community.hashi_vault.vault_pki_generate_certificate - Generates a new set of credentials (private key and certificate) using HashiCorp Vault PKI
- community.hashi_vault.vault_token_create - Create a HashiCorp Vault token
- community.hashi_vault.vault_write - Perform a write operation against HashiCorp Vault

community.okd
~~~~~~~~~~~~~

- community.okd.openshift_adm_migrate_template_instances - Update TemplateInstances to point to the latest group-version-kinds
- community.okd.openshift_adm_prune_auth - Removes references to the specified roles, clusterroles, users, and groups
- community.okd.openshift_adm_prune_deployments - Remove old completed and failed deployment configs
- community.okd.openshift_adm_prune_images - Remove unreferenced images
- community.okd.openshift_import_image - Import the latest image information from a tag in a container image registry.
- community.okd.openshift_registry_info - Display information about the integrated registry.

community.postgresql
~~~~~~~~~~~~~~~~~~~~

- community.postgresql.postgresql_script - Run PostgreSQL statements from a file

community.routeros
~~~~~~~~~~~~~~~~~~

- community.routeros.api_facts - Collect facts from remote devices running MikroTik RouterOS using the API
- community.routeros.api_find_and_modify - Find and modify information using the API

community.vmware
~~~~~~~~~~~~~~~~

- community.vmware.vmware_guest_vgpu - Modify vGPU video card profile of the specified virtual machine in the given vCenter infrastructure
- community.vmware.vmware_host_user_manager - Manage users of ESXi

community.windows
~~~~~~~~~~~~~~~~~

- community.windows.win_listen_ports_facts - Recopilates the facts of the listening ports of the machine

community.zabbix
~~~~~~~~~~~~~~~~

- community.zabbix.zabbix_authentication - Update Zabbix authentication
- community.zabbix.zabbix_autoregister - Update Zabbix autoregistration
- community.zabbix.zabbix_housekeeping - Update Zabbix housekeeping
- community.zabbix.zabbix_script - Create/update/delete Zabbix scripts

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

f5networks.f5_modules
~~~~~~~~~~~~~~~~~~~~~

- f5networks.f5_modules.bigip_ltm_global - Manages global LTM settings

inspur.sm
~~~~~~~~~

- inspur.sm.onboard_disk_info - Get onboard disks information.

junipernetworks.junos
~~~~~~~~~~~~~~~~~~~~~

- junipernetworks.junos.junos_hostname - Manage Hostname server configuration on Junos devices.
- junipernetworks.junos.junos_routing_options - Manage routing-options configuration on Junos devices.
- junipernetworks.junos.junos_security_policies - Create and manage security policies on Juniper JUNOS devices
- junipernetworks.junos.junos_security_policies_global - Manage global security policy settings on Juniper JUNOS devices
- junipernetworks.junos.junos_security_zones - Manage security zones on Juniper JUNOS devices
- junipernetworks.junos.junos_snmp_server - Manage SNMP server configuration on Junos devices.

kubernetes.core
~~~~~~~~~~~~~~~

- kubernetes.core.k8s_taint - Taint a node in a Kubernetes/OpenShift cluster

netapp.cloudmanager
~~~~~~~~~~~~~~~~~~~

- netapp.cloudmanager.na_cloudmanager_aws_fsx - Cloud ONTAP file system(FSX) in AWS

netapp.ontap
~~~~~~~~~~~~

- netapp.ontap.na_ontap_s3_buckets - NetApp ONTAP S3 Buckets

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

t_systems_mms.icinga_director
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- t_systems_mms.icinga_director.icinga_serviceset - Manage servicesets in Icinga2

vyos.vyos
~~~~~~~~~

- vyos.vyos.vyos_hostname - Manages hostname resource module
- vyos.vyos.vyos_snmp_server - Manages snmp_server resource module

Unchanged Collections
---------------------

- cisco.nso (still version 1.0.3)
- community.azure (still version 1.1.0)
- community.fortios (still version 1.0.0)
- community.google (still version 1.0.0)
- community.skydive (still version 1.0.0)
- cyberark.conjur (still version 1.1.0)
- dellemc.os10 (still version 1.1.1)
- dellemc.os6 (still version 1.0.7)
- dellemc.os9 (still version 1.0.4)
- gluster.gluster (still version 1.0.2)
- google.cloud (still version 1.0.2)
- hetzner.hcloud (still version 1.6.0)
- mellanox.onyx (still version 1.0.0)
- netapp.aws (still version 21.7.0)
- netapp.azure (still version 21.10.0)
- netapp.elementsw (still version 21.7.0)
- netapp.um_info (still version 21.8.0)
- ngine_io.exoscale (still version 1.0.0)
- servicenow.servicenow (still version 1.0.6)
- wti.remote (still version 1.0.3)
