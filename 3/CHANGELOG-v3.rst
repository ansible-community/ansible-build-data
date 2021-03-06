=======================
Ansible 3 Release Notes
=======================

This changelog describes changes since Ansible 2.10.0.

.. contents::
  :local:
  :depth: 2

v3.4.0
======

.. contents::
  :local:
  :depth: 2

Release Summary
---------------

Release Date: 2021-05-11

`Porting Guide <https://docs.ansible.com/ansible/devel/porting_guides.html>`_

Ansible-base
------------

Ansible 3.4.0 contains Ansible-base version 2.10.9.
This is a newer version than version 2.10.8 contained in the previous Ansible release.

The changes are reported in the combined changelog below.

Changed Collections
-------------------

If not mentioned explicitly, the changes are reported in the combined changelog below.

+-------------------------------+---------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Collection                    | Ansible 3.3.0 | Ansible 3.4.0 | Notes                                                                                                                                                                                                                                      |
+===============================+===============+===============+============================================================================================================================================================================================================================================+
| amazon.aws                    | 1.4.1         | 1.5.0         |                                                                                                                                                                                                                                            |
+-------------------------------+---------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ansible.utils                 | 2.0.2         | 2.1.0         |                                                                                                                                                                                                                                            |
+-------------------------------+---------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cisco.intersight              | 1.0.12        | 1.0.15        | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.                                                                                                               |
+-------------------------------+---------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.aws                 | 1.4.0         | 1.5.0         |                                                                                                                                                                                                                                            |
+-------------------------------+---------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.crypto              | 1.6.1         | 1.6.2         |                                                                                                                                                                                                                                            |
+-------------------------------+---------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.digitalocean        | 1.1.1         | 1.3.0         |                                                                                                                                                                                                                                            |
+-------------------------------+---------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.docker              | 1.5.0         | 1.6.0         |                                                                                                                                                                                                                                            |
+-------------------------------+---------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.general             | 2.5.1         | 2.5.2         |                                                                                                                                                                                                                                            |
+-------------------------------+---------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.mysql               | 1.4.0         | 1.4.1         |                                                                                                                                                                                                                                            |
+-------------------------------+---------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.network             | 2.1.1         | 2.2.0         |                                                                                                                                                                                                                                            |
+-------------------------------+---------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.postgresql          | 1.2.0         | 1.3.0         |                                                                                                                                                                                                                                            |
+-------------------------------+---------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.vmware              | 1.9.0         | 1.10.0        |                                                                                                                                                                                                                                            |
+-------------------------------+---------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| dellemc.openmanage            | 3.2.0         | 3.3.0         |                                                                                                                                                                                                                                            |
+-------------------------------+---------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| f5networks.f5_modules         | 1.9.0         | 1.9.1         |                                                                                                                                                                                                                                            |
+-------------------------------+---------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| fortinet.fortimanager         | 2.0.1         | 2.0.2         | The collection did not have a changelog in this version.                                                                                                                                                                                   |
+-------------------------------+---------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| hetzner.hcloud                | 1.4.2         | 1.4.3         |                                                                                                                                                                                                                                            |
+-------------------------------+---------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| inspur.sm                     | 1.1.2         | 1.1.4         |                                                                                                                                                                                                                                            |
+-------------------------------+---------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| netapp.ontap                  | 21.4.0        | 21.6.0        |                                                                                                                                                                                                                                            |
+-------------------------------+---------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| netapp_eseries.santricity     | 1.2.7         | 1.2.8         |                                                                                                                                                                                                                                            |
+-------------------------------+---------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ovirt.ovirt                   | 1.4.1         | 1.4.2         |                                                                                                                                                                                                                                            |
+-------------------------------+---------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| purestorage.flasharray        | 1.7.0         | 1.8.0         |                                                                                                                                                                                                                                            |
+-------------------------------+---------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| purestorage.flashblade        | 1.5.0         | 1.6.0         |                                                                                                                                                                                                                                            |
+-------------------------------+---------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| sensu.sensu_go                | 1.9.4         | 1.10.0        |                                                                                                                                                                                                                                            |
+-------------------------------+---------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| t_systems_mms.icinga_director | 1.16.0        | 1.17.0        | You can find the collection's changelog at `https://github.com/T-Systems-MMS/ansible-collection-icinga-director/blob/master/CHANGELOG.md <https://github.com/T-Systems-MMS/ansible-collection-icinga-director/blob/master/CHANGELOG.md>`_. |
+-------------------------------+---------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Major Changes
-------------

Ansible-base
~~~~~~~~~~~~

- ansible-test - Tests run with the ``centos6`` and ``default`` test containers now use a PyPI proxy container to access PyPI when Python 2.6 is used. This allows tests running under Python 2.6 to continue functioning even though PyPI is discontinuing support for non-SNI capable clients.

community.postgresql
~~~~~~~~~~~~~~~~~~~~

- postgresql_query - the default value of the ``as_single_query`` option will be changed to ``yes`` in community.postgresql 2.0.0 (https://github.com/ansible-collections/community.postgresql/issues/85).

netapp.ontap
~~~~~~~~~~~~

- na_ontap_autosupport - Added REST support to the module.

Minor Changes
-------------

Ansible-base
~~~~~~~~~~~~

- Switch to hashlib.sha256() for ansible-test to allow for FIPs mode.

amazon.aws
~~~~~~~~~~

- AWS inventory plugins - use shared HAS_BOTO3 helper rather than copying code (https://github.com/ansible-collections/amazon.aws/pull/288).
- AWS lookup plugins - use shared HAS_BOTO3 helper rather than copying code (https://github.com/ansible-collections/amazon.aws/pull/288).
- aws_account_attribute - add retries on common AWS failures (https://github.com/ansible-collections/amazon.aws/pull/295).
- aws_ec2 inventory - expose a new configuration key ``use_contrib_script_compatible_ec2_tag_keys`` to reproduce a behavior of the old ``ec2.py`` inventory script. With this option enabled, each tag is exposed using a ``ec2_tag_TAGNAME`` key (https://github.com/ansible-collections/amazon.aws/pull/331).
- aws_ec2 inventory - expose to new keys called ``include_filters`` and ``exclude_filters`` to give the user the ability to compose an inventory with multiple queries (https://github.com/ansible-collections/amazon.aws/pull/328).
- aws_ec2 inventory plugin - Added support for using Jinja2 templates in the authentication fields (https://github.com/ansible-collections/amazon.aws/pull/57).
- cloudformation - added support for StackPolicyDuringUpdateBody (https://github.com/ansible-collections/amazon.aws/pull/155).
- ec2_metadata_facts - add support for IMDSv2 (https://github.com/ansible-collections/amazon.aws/pull/43).
- ec2_snapshot_info - add the ``max_results`` along with ``next_token_id`` option (https://github.com/ansible-collections/amazon.aws/pull/321).
- ec2_tag - use common code for tagging resources (https://github.com/ansible-collections/amazon.aws/pull/309).
- ec2_tag_info - use common code for tagging resources (https://github.com/ansible-collections/amazon.aws/pull/309).
- ec2_vol - add the ``purge_tags`` option (https://github.com/ansible-collections/amazon.aws/pull/242).
- ec2_vol - use common code for tagging resources (https://github.com/ansible-collections/amazon.aws/pull/309).
- ec2_vpc_net - use a custom waiter which can handle API rate limiting (https://github.com/ansible-collections/amazon.aws/pull/270).
- ec2_vpc_subnet - use AWSRetry decorator to more consistently handle API rate limiting (https://github.com/ansible-collections/amazon.aws/pull/270).
- ec2_vpc_subnet - use common code for tagging resources (https://github.com/ansible-collections/amazon.aws/pull/309).
- module_utils.cloudfront_facts - linting cleanup (https://github.com/ansible-collections/amazon.aws/pull/291).
- module_utils.ec2 - linting cleanup (https://github.com/ansible-collections/amazon.aws/pull/291).
- module_utils/core - add a helper function ``normalize_boto3_result`` (https://github.com/ansible-collections/amazon.aws/pull/271).
- module_utils/core - add parameter ``descend_into_lists`` to ``scrub_none_parameters`` helper function (https://github.com/ansible-collections/amazon.aws/pull/262).
- module_utils/ec2 - added additional helper functions for tagging EC2 resources (https://github.com/ansible-collections/amazon.aws/pull/309).
- sanity tests - add ignore.txt for 2.12 (https://github.com/ansible-collections/amazon.aws/pull/315).

ansible.utils
~~~~~~~~~~~~~

- Add from_xml and to_xml fiter plugin (https://github.com/ansible-collections/ansible.utils/pull/56).

community.aws
~~~~~~~~~~~~~

- aws_config_aggregator - Fix typos in attribute names (https://github.com/ansible-collections/community.aws/pull/553).
- aws_glue_connection - Added multple connection types (https://github.com/ansible-collections/community.aws/pull/503).
- aws_glue_connection - Added support for check mode (https://github.com/ansible-collections/community.aws/pull/503).
- aws_glue_job - added ``number_of_workers``, ``worker_type`` and ``glue_version`` attributes to the module (https://github.com/ansible-collections/community.aws/pull/370).
- aws_region_info - Add retries on common AWS failures (https://github.com/ansible-collections/community.aws/pull/422).
- aws_s3_bucket_info - new module options ``name``, ``name_filter``, ``bucket_facts`` and ``transform_location`` (https://github.com/ansible-collections/community.aws/pull/260).
- aws_ssm connection plugin - add support for specifying a profile to be used when connecting (https://github.com/ansible-collections/community.aws/pull/278).
- aws_ssm_parameter_store - added tier parameter option (https://github.com/ansible/ansible/issues/59738).
- ec2_asg module - add support for all mixed_instances_policy parameters (https://github.com/ansible-collections/community.aws/issues/231).
- ec2_asg_info - gather information about asg lifecycle hooks (https://github.com/ansible-collections/community.aws/pull/233).
- ec2_instance - wait for new instances to return a status before attempting to set additional parameters (https://github.com/ansible-collections/community.aws/pull/533).
- ec2_instance_info - add retries on common AWS failures (https://github.com/ansible-collections/community.aws/pull/521).
- ec2_launch_template - added ``metadata_options`` parameter to support changing the IMDS configuration for instances (https://github.com/ansible-collections/community.aws/pull/322).
- ec2_metric_alarm - Added support for check mode (https://github.com/ansible-collections/community.aws/pull/470).
- ec2_metric_alarm - Made ``unit`` parameter optional (https://github.com/ansible-collections/community.aws/pull/470).
- ec2_vpc_egress_igw - Add retries on common AWS failures (https://github.com/ansible-collections/community.aws/pull/421).
- ec2_vpc_endpoint - Add retries on common AWS failures. (https://github.com/ansible-collections/community.aws/pull/473)
- ec2_vpc_endpoint - Added support for specifying ``vpc_endpoint_type`` (https://github.com/ansible-collections/community.aws/pull/460).
- ec2_vpc_endpoint - The module now supports tagging endpoints. (https://github.com/ansible-collections/community.aws/pull/473)
- ec2_vpc_endpoint - The module will now lookup existing endpoints and try to match on the provided parameters before creating a new endpoint for better idempotency.  (https://github.com/ansible-collections/community.aws/pull/473)
- ec2_vpc_endpoint_info - ensure paginated endpoint description is retried on common AWS failures (https://github.com/ansible-collections/community.aws/pull/537).
- ec2_vpc_endpoint_info - use boto3 paginator when fetching services (https://github.com/ansible-collections/community.aws/pull/537).
- ec2_vpc_endpoint_service_info - new module added for fetching information about available VPC endpoint services (https://github.com/ansible-collections/community.aws/pull/346).
- ec2_vpc_nacl - add support for IPv6 (https://github.com/ansible-collections/community.aws/pull/398).
- ec2_vpc_nat_gateway - add AWSRetry decorators to improve reliability (https://github.com/ansible-collections/community.aws/pull/427).
- ec2_vpc_nat_gateway - code cleaning (https://github.com/ansible-collections/community.aws/pull/445)
- ec2_vpc_nat_gateway - imporove documentation (https://github.com/ansible-collections/community.aws/pull/445)
- ec2_vpc_nat_gateway - improve error handling (https://github.com/ansible-collections/community.aws/pull/445)
- ec2_vpc_nat_gateway - use custom waiters to manage NAT gateways states (deleted and available) (https://github.com/ansible-collections/community.aws/pull/445)
- ec2_vpc_nat_gateway - use pagination on describe calls to ensure all results are fetched (https://github.com/ansible-collections/community.aws/pull/427).
- ec2_vpc_nat_gateway_info - Add paginator (https://github.com/ansible-collections/community.aws/pull/472).
- ec2_vpc_nat_gateway_info - Improve documentation (https://github.com/ansible-collections/community.aws/pull/472).
- ec2_vpc_nat_gateway_info - Improve error handling (https://github.com/ansible-collections/community.aws/pull/472)
- ec2_vpc_nat_gateway_info - Use normalize_boto3_result (https://github.com/ansible-collections/community.aws/pull/472)
- ec2_vpc_nat_gateway_info - solve RequestLimitExceeded error by adding retry decorator (https://github.com/ansible-collections/community.aws/pull/446)
- ec2_vpc_peer - More return info added, also simplified module code a bit and extended tests (https://github.com/ansible-collections/community.aws/pull/355)
- ec2_vpc_peer - add support for waiting on state changes (https://github.com/ansible-collections/community.aws/pull/501).
- ec2_vpc_peering_info - add ``vpc_peering_connections`` return value to be consistent with boto3 modules (https://github.com/ansible-collections/community.aws/pull/501).
- ec2_vpc_peering_info - add retries on common AWS failures (https://github.com/ansible-collections/community.aws/pull/536).
- ec2_vpc_route_table - add AWSRetry decorators to improve reliability (https://github.com/ansible-collections/community.aws/pull/442).
- ec2_vpc_route_table - add boto3 pagination for some searches (https://github.com/ansible-collections/community.aws/pull/442).
- ec2_vpc_route_table_info - migrate to boto3 (https://github.com/ansible-collections/community.aws/pull/442).
- ec2_vpc_vgw - Add automatic retries for recoverable errors (https://github.com/ansible-collections/community.aws/pull/162).
- ec2_vpc_vpn - Add automatic retries for recoverable errors (https://github.com/ansible-collections/community.aws/pull/162).
- ecs_service - Add ``platform_version`` parameter to ``ecs_service`` (https://github.com/ansible-collections/community.aws/pull/353).
- ecs_task - added ``assign_public_ip`` option for network_configuration (https://github.com/ansible-collections/community.aws/pull/395).
- ecs_taskdefinition - Documentation improvement (https://github.com/ansible-collections/community.aws/issues/520)
- elasticache - Improve docs a little, add intgration tests (https://github.com/ansible-collections/community.aws/pull/410).
- elb_classic_info - If the provided load balancer doesn't exist, return an empty list instead of throwing an error. (https://github.com/ansible-collections/community.aws/pull/215).
- elb_target_group - Add elb target group attributes ``stickiness_app_cookie_name`` and ``stickiness_app_cookie_duration_seconds``. Also update docs for stickiness_type to mention application cookie (https://github.com/ansible-collections/community.aws/pull/548)
- iam - Make iam module more predictable when returning the ``user_name`` it creates or deletes (https://github.com/ansible-collections/community.aws/pull/369).
- iam_saml_federation - module now returns the state of the provider when no changes are made (https://github.com/ansible-collections/community.aws/pull/419).
- kinesis_stream - check_mode is now based on the live settings rather than comparisons with a hard coded/fake stream definition (https://github.com/ansible-collections/community.aws/pull/27).
- kinesis_stream - now returns changed more accurately (https://github.com/ansible-collections/community.aws/pull/27).
- kinesis_stream - now returns tags consistently (https://github.com/ansible-collections/community.aws/pull/27).
- kinesis_stream - return values are now the same format when working with both encrypted and un-encrypted streams (https://github.com/ansible-collections/community.aws/pull/27).
- lambda_alias - add retries on common AWS failures (https://github.com/ansible-collections/community.aws/pull/396).
- lambda_alias - use common helper functions to create AWS connections (https://github.com/ansible-collections/community.aws/pull/396).
- lambda_alias - use common helper functions to perform snake_case to CamelCase conversions (https://github.com/ansible-collections/community.aws/pull/396).
- rds_instance - new ``purge_security_groups`` parameter (https://github.com/ansible-collections/community.aws/issues/385).
- rds_param_group - Add AWSRetry (https://github.com/ansible-collections/community.aws/pull/532).
- rds_param_group - Fix integration tests (https://github.com/ansible-collections/community.aws/pull/532).
- rds_param_group - Support check_mode (https://github.com/ansible-collections/community.aws/pull/532).
- rds_snapshot - added to the aws module_defaults group (https://github.com/ansible-collections/community.aws/pull/515).
- route53 - fixes AWS API error when attempting to create Alias records (https://github.com/ansible-collections/community.aws/issues/434).
- s3_lifecycle - Add a ``wait`` parameter to wait for changes to propagate after being set (https://github.com/ansible-collections/community.aws/pull/448).
- s3_lifecycle - Add retries on common AWS failures (https://github.com/ansible-collections/community.aws/pull/448).
- s3_lifecycle - Fix idempotency when using dates instead of days (https://github.com/ansible-collections/community.aws/pull/448).
- s3_logging - added support for check_mode (https://github.com/ansible-collections/community.aws/pull/447).
- s3_logging - migrated from boto to boto3 (https://github.com/ansible-collections/community.aws/pull/447).
- s3_sync - new ``storage_class`` feature allowing to specify the storage class when any object is added to an S3 bucket (https://github.com/ansible-collections/community.aws/issues/358).
- sanity tests - add ignore.txt for 2.12 (https://github.com/ansible-collections/community.aws/pull/527).
- state_machine_arn - return ``state_machine_arn`` when state is unchanged (https://github.com/ansible-collections/community.aws/pull/302).

community.digitalocean
~~~~~~~~~~~~~~~~~~~~~~

- digital_ocean - ``ssh_key_ids`` list entries are now validated to be strings (https://github.com/ansible-collections/community.digitalocean/issues/13).
- digital_ocean_droplet - ``ssh_keys``, ``tags``, and ``volumes`` list entries are now validated to be strings (https://github.com/ansible-collections/community.digitalocean/issues/13).
- digital_ocean_droplet - adding ``active`` and ``inactive`` states (https://github.com/ansible-collections/community.digitalocean/issues/23).
- digital_ocean_droplet - adds Droplet resize functionality (https://github.com/ansible-collections/community.digitalocean/issues/4).

community.docker
~~~~~~~~~~~~~~~~

- common module utils - correct error messages for guiding to install proper Docker SDK for Python module (https://github.com/ansible-collections/community.docker/pull/125).
- docker_container - allow ``memory_swap: -1`` to set memory swap limit to unlimited. This is useful when the user cannot set memory swap limits due to cgroup limitations or other reasons, as by default Docker will try to set swap usage to two times the value of ``memory`` (https://github.com/ansible-collections/community.docker/pull/138).

community.vmware
~~~~~~~~~~~~~~~~

- vmware_cluster_drs - Make enable_drs an alias of enable and add a warning that the default will change from false to true in a future version (https://github.com/ansible-collections/community.vmware/pull/766)
- vmware_cluster_ha - Make enable_ha an alias of enable and add a warning that the default will change from false to true in a future version (https://github.com/ansible-collections/community.vmware/pull/766)
- vmware_cluster_vsan - Make enable_vsan an alias of enable and add a warning that the default will change from false to true in a future version (https://github.com/ansible-collections/community.vmware/pull/766)
- vmware_dvs_portgroup - Implement 'elastic' port group configuration (https://github.com/ansible-collections/community.vmware/issues/410).
- vmware_dvs_portgroup - Implement MAC learning configuration (https://github.com/ansible-collections/community.vmware/issues/644).
- vmware_dvs_portgroup - Implement configuration of active and standby uplinks (https://github.com/ansible-collections/community.vmware/issues/709).
- vmware_dvs_portgroup - Remove default for teaming_policy.inbound_policy (https://github.com/ansible-collections/community.vmware/pull/743).
- vmware_dvs_portgroup_info - Return information about MAC learning configuration (https://github.com/ansible-collections/community.vmware/issues/644).
- vmware_dvs_portgroup_info - Return information about uplinks (https://github.com/ansible-collections/community.vmware/issues/709).
- vmware_guest - add more documentation about ``is_template`` (https://github.com/ansible-collections/community.vmware/pull/794).
- vmware_host_iscsi_info - added a list(detected_iscsi_drives) of detected iscsi drives to the return value after set an iscsi config (https://github.com/ansible-collections/community.vmware/pull/729).
- vmware_tag - modified the category_id parameter to required (https://github.com/ansible-collections/community.vmware/pull/790).
- vmware_vm_inventory - set default to ``True`` for ``with_nested_properties`` (https://github.com/ansible-collections/community.vmware/issues/712).

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- ome_firmware_baseline - Allows to retrieve the device even if it not in the first 50 device IDs

f5networks.f5_modules
~~~~~~~~~~~~~~~~~~~~~

- Add ENV variable with better name, it should make it easier to understand when disabling F5 TEEM telemetry
- Add new choices to request/response chunking parameter to accomodate TMOS v15 and above

netapp.ontap
~~~~~~~~~~~~

- na_ontap_autosupport - new option ``local_collection_enabled`` to specify whether collection of AutoSupport data when the AutoSupport daemon is disabled.
- na_ontap_autosupport - new option ``max_http_size`` to specify delivery size limit for the HTTP transport protocol (in bytes).
- na_ontap_autosupport - new option ``max_smtp_size`` to specify delivery size limit for the SMTP transport protocol (in bytes).
- na_ontap_autosupport - new option ``nht_data_enabled`` to specify whether the disk health data is collected as part of the AutoSupport data.
- na_ontap_autosupport - new option ``ondemand_enabled`` to specify whether the AutoSupport OnDemand Download feature is enabled.
- na_ontap_autosupport - new option ``perf_data_enabled`` to specify whether the performance data is collected as part of the AutoSupport data.
- na_ontap_autosupport - new option ``private_data_removed`` to specify the removal of customer-supplied data.
- na_ontap_autosupport - new option ``reminder_enabled`` to specify whether AutoSupport reminders are enabled or disabled.
- na_ontap_autosupport - new option ``retry_count`` to specify the maximum number of delivery attempts for an AutoSupport message.
- na_ontap_autosupport - new option ``validate_digital_certificate`` which when set to true each node will validate the digital certificates that it receives.
- na_ontap_info - Added "autosupport_check_info" to the attributes that will be collected when gathering info using the module.
- na_ontap_rest_info - Added "autosupport_check_info"/"support/autosupport/check" to the attributes that will be collected when gathering info using the module.
- na_ontap_users - new option ``application_dicts`` to associate multiple authentication methods to an application.
- na_ontap_users - new option ``application_strs`` to disambiguate ``applications``.
- na_ontap_users - new option ``replace_existing_apps_and_methods``.
- na_ontap_users - new suboption ``second_authentication_method`` with ``application_dicts`` option.
- na_ontap_vserver_peer - new options ``local_name_for_source`` and ``local_name_for_peer`` added.

ovirt.ovirt
~~~~~~~~~~~

- hosted_engine_setup - Add an error message for FIPS on CentOS (https://github.com/oVirt/ovirt-ansible-collection/pull/250).
- hosted_engine_setup - Fix the appliance distribution (https://github.com/oVirt/ovirt-ansible-collection/pull/249).
- infra - remove target from ovirt_storage_connection (https://github.com/oVirt/ovirt-ansible-collection/pull/252).
- ovirt_vm - Allow migration between clusters (https://github.com/oVirt/ovirt-ansible-collection/pull/236).
- repositories - Add host ppc (https://github.com/oVirt/ovirt-ansible-collection/pull/248).
- repositories - Remove ansible channels from RHV 4.4 (https://github.com/oVirt/ovirt-ansible-collection/pull/242).
- repositories - fix ppc repos (https://github.com/oVirt/ovirt-ansible-collection/pull/254).

purestorage.flasharray
~~~~~~~~~~~~~~~~~~~~~~

- purefa_certs - New module for managing SSL certificates
- purefa_volume - New parameter pgroup to specify an existing protection group to put crwated volume(s) in.

purestorage.flashblade
~~~~~~~~~~~~~~~~~~~~~~

- purefa_virtualhost - New module to manage API Clients
- purefb_ad - New module to manage Active Directory Account
- purefb_eula - New module to sign EULA
- purefb_info - Add Active Directory, Kerberos and Object Store Account information
- purefb_info - Add extra info for Purity//FB 3.2+ systems
- purefb_keytabs - New module to manage Kerberos Keytabs
- purefb_s3user - Add access policy option to user creation
- purefb_timeout - Add module to set GUI idle timeout
- purefb_userpolicy - New module to manage object store user access policies
- purefb_virtualhost - New module to manage Object Store Virtual Hosts

sensu.sensu_go
~~~~~~~~~~~~~~

- Add modules for managing Sensu Go authentication providers.

Deprecated Features
-------------------

community.aws
~~~~~~~~~~~~~

- ec2_vpc_endpoint_info - the ``query`` option has been deprecated and will be removed after 2022-12-01 (https://github.com/ansible-collections/community.aws/pull/346). The ec2_vpc_endpoint_info now defaults to listing information about endpoints. The ability to search for information about available services has been moved to the dedicated module ``ec2_vpc_endpoint_service_info``.

community.docker
~~~~~~~~~~~~~~~~

- docker_* modules and plugins, except ``docker_swarm`` connection plugin and ``docker_compose`` and ``docker_stack*` modules - the current default ``localhost`` for ``tls_hostname`` is deprecated. In community.docker 2.0.0 it will be computed from ``docker_host`` instead (https://github.com/ansible-collections/community.docker/pull/134).

Security Fixes
--------------

community.aws
~~~~~~~~~~~~~

- aws_direct_connect_virtual_interface - mark the ``authentication_key`` parameter as ``no_log`` to avoid accidental leaking of secrets in logs (https://github.com/ansible-collections/community.aws/pull/475).
- aws_secret - flag the ``secret`` parameter as containing sensitive data which shouldn't be logged (https://github.com/ansible-collections/community.aws/pull/471).
- sts_assume_role - mark the ``mfa_token`` parameter as ``no_log`` to avoid accidental leaking of secrets in logs (https://github.com/ansible-collections/community.aws/pull/475).
- sts_session_token - mark the ``mfa_token`` parameter as ``no_log`` to avoid accidental leaking of secrets in logs (https://github.com/ansible-collections/community.aws/pull/475).

Bugfixes
--------

Ansible-base
~~~~~~~~~~~~

- Prevent ``ansible_failed_task`` from further templating (https://github.com/ansible/ansible/issues/74036)
- ansible-test - Avoid publishing the port used by the ``pypi-test-container`` since it is only accessed by other containers. This avoids issues when trying to run tests in parallel on a single host.
- ansible-test - Fix docker container IP address detection. The ``bridge`` network is no longer assumed to be the default.
- ansible-test - ensure the correct unit test target is given when the ``__init__.py`` file is modified inside the connection plugins directory
- ansible.utils.encrypt now handles missing or unusable 'crypt' library.
- facts - detect homebrew installed at /opt/homebrew/bin/brew
- interpreter discovery - Debian 8 and lower will avoid unsupported Python3 version in interpreter discovery
- undeprecate hash_merge setting and add more docs clarifying its use and why not to use it.
- wait_for module, move missing socket into function to get proper comparrison in time.

amazon.aws
~~~~~~~~~~

- ec2_vol - create or update now preserves the existing tags, including Name (https://github.com/ansible-collections/amazon.aws/issues/229)
- ec2_vol - fix exception when platform information isn't available (https://github.com/ansible-collections/amazon.aws/issues/305).

ansible.utils
~~~~~~~~~~~~~

- Add missing test requirements (https://github.com/ansible-collections/ansible.utils/pull/57).

community.aws
~~~~~~~~~~~~~

- aws_ssm - Adds destructor to SSM connection plugin to ensure connections are properly cleaned up after usage (https://github.com/ansible-collections/community.aws/pull/542).
- aws_ssm - enable aws ssm connections if **AWS_SESSION_TOKEN** is missing (https://github.com/ansible-collections/community.aws/pull/535).
- cloudtrail - fix always reporting changed = true when kms alias used (https://github.com/ansible-collections/community.aws/pull/506).
- cloudtrail - fix lower casing of tag keys (https://github.com/ansible-collections/community.aws/pull/506).
- ec2_asg - fix target group update logic (https://github.com/ansible-collections/community.aws/pull/493).
- ec2_instance - ensure that termination protection isn't modified when using check_mode (https://github.com/ansible/ansible/issues/67716).
- ec2_instance - fix key errors when instance has no tags (https://github.com/ansible-collections/community.aws/pull/476).
- ec2_launch_template - ensure that empty parameters are properly removed before passing to AWS (https://github.com/ansible-collections/community.aws/issues/230).
- ec2_launch_template - fixes parameter validation failure when passing a instance profile ARN instead of just the role name (https://github.com/ansible-collections/community.aws/pull/371).
- ec2_vpc_peer - fix idempotency when rejecting and deleting peering connections (https://github.com/ansible-collections/community.aws/pull/501).
- ec2_vpc_route_table - catch RouteAlreadyExists error when rerunning same task twice to make module idempotent (https://github.com/ansible-collections/community.aws/issues/357).
- elasticache - Fix ``KeyError`` issue when updating security group (https://github.com/ansible-collections/community.aws/pull/410).
- kinesis_stream - fixed issue where streams get marked as changed even if no encryption actions were necessary (https://github.com/ansible/ansible/issues/65928).
- rds_instance - fixes bug preventing the use of tags when creating an RDS instance from a snapshot (https://github.com/ansible-collections/community.aws/issues/530).
- route53 - ensure that the old return values are re-added along side the new ones (https://github.com/ansible-collections/community.aws/issues/523).
- route53 - fix ``AttributeError`` in ``get_zone_id_by_name`` when a vpc_id on a private zone is provided (https://github.com/ansible-collections/community.aws/issues/509).
- route53 - fix handling for characters escaped by AWS in record names, like ``*`` and ``@``. This fixes idempotency for such record names (https://github.com/ansible-collections/community.aws/issues/524).
- route53 - fix when using ``state=get`` on private DNS zones and add tests to cover this scenario (https://github.com/ansible-collections/community.aws/pull/424).
- route53 - make sure that CAA values order is again ignored during idempotency comparsion (https://github.com/ansible-collections/community.aws/issues/524).
- sns_topic - Add ``+`` to allowable characters in SMS endpoints (https://github.com/ansible-collections/community.aws/pull/454).
- sqs_queue - fix UnboundLocalError when passing a boolean parameter (https://github.com/ansible-collections/community.aws/issues/172).

community.crypto
~~~~~~~~~~~~~~~~

- acme_* modules - avoid crashing for ACME servers where the ``meta`` directory key is not present (https://github.com/ansible-collections/community.crypto/issues/220, https://github.com/ansible-collections/community.crypto/pull/221).

community.digitalocean
~~~~~~~~~~~~~~~~~~~~~~

- digital_ocean inventory script - fail cleaner on invalid ``HOST`` argument to ``--host`` option (https://github.com/ansible-collections/community.digitalocean/pull/44).
- digital_ocean inventory script - implement unimplemented ``use_private_network`` option and register missing ``do_ip_address``, ``do_private_ip_address`` host vars (https://github.com/ansible-collections/community.digitalocean/pull/45/files).
- digital_ocean inventory script - return JSON consistent with specification with ``--host`` (https://github.com/ansible-collections/community.digitalocean/pull/44).
- digital_ocean_domain - return zone records when creating a new zone (https://github.com/ansible-collections/community.digitalocean/issues/46).
- digital_ocean_droplet - add missing ``required=True`` on ``do_oauth_token`` in ``argument_spec`` (https://github.com/ansible-collections/community.digitalocean/issues/13).
- digital_ocean_floating_ip - fixes idempotence (https://github.com/ansible-collections/community.digitalocean/issues/5).

community.docker
~~~~~~~~~~~~~~~~

- docker-compose - fix not pulling when ``state: present`` and ``stopped: true`` (https://github.com/ansible-collections/community.docker/issues/12, https://github.com/ansible-collections/community.docker/pull/119).
- docker_plugin - also configure plugin after installing (https://github.com/ansible-collections/community.docker/issues/118, https://github.com/ansible-collections/community.docker/pull/135).
- docker_swarm_services - avoid crash during idempotence check if ``published_port`` is not specified (https://github.com/ansible-collections/community.docker/issues/107, https://github.com/ansible-collections/community.docker/pull/136).

community.general
~~~~~~~~~~~~~~~~~

- composer - use ``no-interaction`` option when discovering available options to avoid an issue where composer hangs (https://github.com/ansible-collections/community.general/pull/2348).
- hiera lookup plugin - converts the return type of plugin to unicode string (https://github.com/ansible-collections/community.general/pull/2329).
- influxdb_retention_policy - ensure idempotent module execution with different duration and shard duration parameter values (https://github.com/ansible-collections/community.general/issues/2281).
- influxdb_retention_policy - fix bug where ``INF`` duration values failed parsing (https://github.com/ansible-collections/community.general/pull/2385).
- inventory and vault scripts - change file permissions to make vendored inventory and vault scripts exectuable (https://github.com/ansible-collections/community.general/pull/2337).
- jenkins_plugin - fixes Python 2 compatibility issue (https://github.com/ansible-collections/community.general/pull/2340).
- jira - fixed error when loading base64-encoded content as attachment (https://github.com/ansible-collections/community.general/pull/2349).
- linode_v4 - changed the error message to point to the correct bugtracker URL (https://github.com/ansible-collections/community.general/pull/2430).
- nmap inventory plugin - fix cache and constructed group support (https://github.com/ansible-collections/community.general/issues/2242).
- nmcli - compare MAC addresses case insensitively to fix idempotency issue (https://github.com/ansible-collections/community.general/issues/2409).
- nmcli - if type is ``bridge-slave`` add ``slave-type bridge`` to ``nmcli`` command (https://github.com/ansible-collections/community.general/issues/2408).
- one_vm - Allow missing NIC keys (https://github.com/ansible-collections/community.general/pull/2435).
- ovirt* modules - remove bad unnecessary import for current ansible-core development version (https://github.com/ansible-collections/community.general/pull/2381).
- proxmox inventory - added handling of commas in KVM agent configuration string (https://github.com/ansible-collections/community.general/pull/2245).
- puppet - replace ``console` with ``stdout`` in ``logdest`` option when ``all`` has been chosen (https://github.com/ansible-collections/community.general/issues/1190).
- stackpath_compute inventory script - fix broken validation checks for client ID and client secret (https://github.com/ansible-collections/community.general/pull/2448).
- svr4pkg - convert string to a bytes-like object to avoid ``TypeError`` with Python 3 (https://github.com/ansible-collections/community.general/issues/2373).
- terraform - fix issue that cause the destroy to fail because from Terraform 0.15 on, the ``terraform destroy -force`` option is replaced with ``terraform destroy -auto-approve`` (https://github.com/ansible-collections/community.general/issues/2247).
- terraform - fix issue that cause the execution fail because from Terraform 0.15 on, the ``-var`` and ``-var-file`` options are no longer available on ``terraform validate`` (https://github.com/ansible-collections/community.general/pull/2246).
- terraform - remove uses of ``use_unsafe_shell=True`` (https://github.com/ansible-collections/community.general/pull/2246).
- zfs - certain ZFS properties, especially sizes, would lead to a task being falsely marked as "changed" even when no actual change was made (https://github.com/ansible-collections/community.general/issues/975, https://github.com/ansible-collections/community.general/pull/2454).

community.mysql
~~~~~~~~~~~~~~~

- mysql - revert changes of connector arguments made in pull request 116 causing the invalid keyword argument error (https://github.com/ansible-collections/community.mysql/pull/116).

community.postgresql
~~~~~~~~~~~~~~~~~~~~

- postgresql_privs - fix ``fail_on_role`` check (https://github.com/ansible-collections/community.postgresql/pull/82).

community.vmware
~~~~~~~~~~~~~~~~

- vmware - fixed a bug that the guest_guestion in the facts doesn't convert to the dictionary (https://github.com/ansible-collections/community.vmware/pull/825).
- vmware - handle exception raised in ``get_all_objs`` and ``find_object_by_name`` which occurs due to multiple parallel operations (https://github.com/ansible-collections/community.vmware/issues/791).
- vmware_cluster_info - Fix a bug that returned enabled_vsan and vsan_auto_claim_storage as lists instead of just true or false (https://github.com/ansible-collections/community.vmware/issues/805).
- vmware_evc_mode - fixed an issue that evc_mode is required when the state parameter set to absent (https://github.com/ansible-collections/community.vmware/pull/764).
- vmware_guest - skip customvalues while deploying VM on a standalone ESXi (https://github.com/ansible-collections/community.vmware/issues/721).
- vmware_host_iscsi_info - fixed an issue that an error occurs gathering iSCSI information against an ESXi Host with iSCSI disabled (https://github.com/ansible-collections/community.vmware/pull/729).
- vmware_vm_info - handle vApp parent logic (https://github.com/ansible-collections/community.vmware/issues/777).
- vmware_vm_shell - handle exception raised while performing the operation (https://github.com/ansible-collections/community.vmware/issues/732).
- vmware_vm_storage_policy_info - fixed an issue that the module can't get storage policy info when the policy has the tag base rules (https://github.com/ansible-collections/community.vmware/pull/788).
- vmware_vmotion - Provide an meaningful error message when providing a bad ESXi node as ``destination_host`` (https://github.com/ansible-collections/vmware/pull/804).

f5networks.f5_modules
~~~~~~~~~~~~~~~~~~~~~

- Disable cert validaton for Teem
- Fix bigip_gtm_wide_ip to support wildcard type a wide ips
- Fix imish config issue where last character is chopped off by adding extra space to commands
- Fix issue in bigip_firewall_dos_policy where in TMOS v15 and above creating dos vector containers requires additional step in the API
- Fix issue in bigip_gtm_topology_region where parameter region_members being set to empty list returned an error
- Fix issue in bigip_pool_member with module idempotency when pool member status was fqdn-down
- Fix issue where bigip_firewall_port_list was failing when removing objects (#1988)
- Fix issue where empty irules property on device would throw exception during comparison
- Fix issue where viprion platrform interfaces interface naming scheme prevented the use of module
- Fix issue with new telemetry environment variable not populated in provider
- Fix issue with send_teem function ignoring environment variable
- Fix teem version in constants.py
- Fix validation function for bigip_virtual_server module to include new api endpoints for checking SIP profiles
- Fix various minor regressions and improved functional testing in collection

hetzner.hcloud
~~~~~~~~~~~~~~

- hcloud_server Fix incompatbility with python < 3.6
- hcloud_server Improve error handling when using not existing server types

inspur.sm
~~~~~~~~~

- Add ansible 2.11 test.
- Add the no_log=true attribute to some modules.

netapp.ontap
~~~~~~~~~~~~

- na_ontap_autosupport - TypeError - '>' not supported between instances of 'str' and 'list'.
- na_ontap_qtree - wait for completion when creating or modifying a qtree with REST.
- na_ontap_quotas - fail to reinitialize on create if quota is already on.
- na_ontap_volume - ignore read error because of insufficient privileges for efficiency options so that the module can be run as vsadmin.

netapp_eseries.santricity
~~~~~~~~~~~~~~~~~~~~~~~~~

- Fix pkcs8 private key passphrase issue.
- Fix storage system admin password change from web services proxy in na_santricity_auth module.

purestorage.flasharray
~~~~~~~~~~~~~~~~~~~~~~

- purefa_dsrole - If using None for group or group_base incorrect change state applied
- purefa_network - Allow gateway paremeter to be set as None - needed for non-routing iSCSI ports
- purefa_pg - Check to ensure protection group name meets naming convention
- purefa_pgsnap - Fail with warning if trying to restore to a stretched ActiveCluster pod
- purefa_volume - Ensure REST version is high enough to support promotion_status

Known Issues
------------

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- idrac_user - Issue(192043) Module may error out with the message ``unable to perform the import or export operation because there are pending attribute changes or a configuration job is in progress``. Wait for the job to complete and run the task again.
- ome_configuration_compliance_info - Issue(195592) Module may error out with the message ``unable to process the request because an error occurred``. If the issue persists, report it to the system administrator.
- ome_smart_fabric - Issue(185322) Only three design types are supported by OpenManage Enterprise Modular but the module successfully creates a fabric when the design type is not supported.
- ome_smart_fabric_uplink - Issue(186024) ome_smart_fabric_uplink module does not allow the creation of multiple uplinks of the same name even though this is supported by OpenManage Enterprise Modular. If an uplink is created using the same name as an existing uplink, the existing uplink is modified.

New Plugins
-----------

Cliconf
~~~~~~~

- community.network.weos4 - Use weos4 cliconf to run commands on Westermo platform

New Modules
-----------

community.aws
~~~~~~~~~~~~~

- community.aws.ec2_vpc_endpoint_service_info - retrieves AWS VPC endpoint service details
- community.aws.wafv2_ip_set - wafv2_ip_set
- community.aws.wafv2_ip_set_info - Get information about wafv2 ip sets
- community.aws.wafv2_resources - wafv2_web_acl
- community.aws.wafv2_resources_info - wafv2_resources_info
- community.aws.wafv2_rule_group - wafv2_web_acl
- community.aws.wafv2_rule_group_info - wafv2_web_acl_info
- community.aws.wafv2_web_acl - wafv2_web_acl
- community.aws.wafv2_web_acl_info - wafv2_web_acl

community.digitalocean
~~~~~~~~~~~~~~~~~~~~~~

- community.digitalocean.digital_ocean_balance_info - Display DigitalOcean customer balance
- community.digitalocean.digital_ocean_database - Create and delete a DigitalOcean database
- community.digitalocean.digital_ocean_database_info - Gather information about DigitalOcean databases
- community.digitalocean.digital_ocean_kubernetes - Create and delete a DigitalOcean Kubernetes cluster
- community.digitalocean.digital_ocean_kubernetes_info - Returns information about an existing DigitalOcean Kubernetes cluster

community.vmware
~~~~~~~~~~~~~~~~

- community.vmware.vmware_host_tcpip_stacks - Manage the TCP/IP Stacks configuration of ESXi host

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- dellemc.openmanage.ome_device_group - Manages device group settings on OpenManage Enterprise
- dellemc.openmanage.ome_discovery - Create, modify or delete a discovery job on OpenManage Enterprise

purestorage.flasharray
~~~~~~~~~~~~~~~~~~~~~~

- purestorage.flasharray.purefa_certs - Manage FlashArray SSL Certificates

purestorage.flashblade
~~~~~~~~~~~~~~~~~~~~~~

- purestorage.flashblade.purefb_ad - Manage FlashBlade Active Directory Account
- purestorage.flashblade.purefb_apiclient - Manage FlashBlade API Clients
- purestorage.flashblade.purefb_eula - Sign Pure Storage FlashBlade EULA
- purestorage.flashblade.purefb_keytabs - Manage FlashBlade Kerberos Keytabs
- purestorage.flashblade.purefb_timeout - Configure Pure Storage FlashBlade GUI idle timeout
- purestorage.flashblade.purefb_userpolicy - Manage FlashBlade Object Store User Access Policies
- purestorage.flashblade.purefb_virtualhost - Manage FlashBlade Object Store Virtual Hosts

sensu.sensu_go
~~~~~~~~~~~~~~

- sensu.sensu_go.ad_auth_provider - Manage Sensu AD authentication provider
- sensu.sensu_go.auth_provider_info - List Sensu authentication providers
- sensu.sensu_go.ldap_auth_provider - Manage Sensu LDAP authentication provider
- sensu.sensu_go.oidc_auth_provider - Manage Sensu OIDC authentication provider

Unchanged Collections
---------------------

- ansible.netcommon (still version 1.5.0)
- ansible.posix (still version 1.2.0)
- ansible.windows (still version 1.5.0)
- arista.eos (still version 1.3.0)
- awx.awx (still version 17.1.0)
- azure.azcollection (still version 1.5.0)
- check_point.mgmt (still version 2.0.0)
- chocolatey.chocolatey (still version 1.1.0)
- cisco.aci (still version 2.0.0)
- cisco.asa (still version 1.0.4)
- cisco.ios (still version 1.3.0)
- cisco.iosxr (still version 1.2.1)
- cisco.meraki (still version 2.2.1)
- cisco.mso (still version 1.1.0)
- cisco.nso (still version 1.0.3)
- cisco.nxos (still version 1.4.0)
- cisco.ucs (still version 1.6.0)
- cloudscale_ch.cloud (still version 2.1.0)
- community.azure (still version 1.0.0)
- community.fortios (still version 1.0.0)
- community.google (still version 1.0.0)
- community.grafana (still version 1.2.1)
- community.hashi_vault (still version 1.1.3)
- community.hrobot (still version 1.1.1)
- community.kubernetes (still version 1.2.1)
- community.kubevirt (still version 1.0.0)
- community.libvirt (still version 1.0.1)
- community.mongodb (still version 1.2.1)
- community.okd (still version 1.1.2)
- community.proxysql (still version 1.0.0)
- community.rabbitmq (still version 1.0.3)
- community.routeros (still version 1.1.0)
- community.skydive (still version 1.0.0)
- community.sops (still version 1.0.6)
- community.windows (still version 1.3.0)
- community.zabbix (still version 1.3.0)
- containers.podman (still version 1.5.0)
- cyberark.conjur (still version 1.1.0)
- cyberark.pas (still version 1.0.6)
- dellemc.os10 (still version 1.1.1)
- dellemc.os6 (still version 1.0.7)
- dellemc.os9 (still version 1.0.4)
- fortinet.fortios (still version 1.1.9)
- frr.frr (still version 1.0.3)
- gluster.gluster (still version 1.0.1)
- google.cloud (still version 1.0.2)
- ibm.qradar (still version 1.0.3)
- infinidat.infinibox (still version 1.2.4)
- junipernetworks.junos (still version 1.3.0)
- kubernetes.core (still version 1.2.1)
- mellanox.onyx (still version 1.0.0)
- netapp.aws (still version 20.9.0)
- netapp.elementsw (still version 20.11.0)
- netbox.netbox (still version 2.1.0)
- ngine_io.cloudstack (still version 2.1.0)
- ngine_io.exoscale (still version 1.0.0)
- ngine_io.vultr (still version 1.1.0)
- openstack.cloud (still version 1.4.0)
- openvswitch.openvswitch (still version 1.2.0)
- servicenow.servicenow (still version 1.0.4)
- splunk.es (still version 1.0.2)
- theforeman.foreman (still version 1.5.1)
- vyos.vyos (still version 1.1.1)
- wti.remote (still version 1.0.1)

v3.3.0
======

.. contents::
  :local:
  :depth: 2

Release Summary
---------------

Release Date: 2021-04-20

`Porting Guide <https://docs.ansible.com/ansible/devel/porting_guides.html>`_

Ansible-base
------------

Ansible 3.3.0 contains Ansible-base version 2.10.8.
This is a newer version than version 2.10.7 contained in the previous Ansible release.

The changes are reported in the combined changelog below.

Changed Collections
-------------------

If not mentioned explicitly, the changes are reported in the combined changelog below.

+---------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| Collection                | Ansible 3.2.0 | Ansible 3.3.0 | Notes                                                                                                                        |
+===========================+===============+===============+==============================================================================================================================+
| ansible.windows           | 1.4.0         | 1.5.0         |                                                                                                                              |
+---------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| azure.azcollection        | 1.4.0         | 1.5.0         | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+---------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| chocolatey.chocolatey     | 1.0.2         | 1.1.0         |                                                                                                                              |
+---------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.crypto          | 1.6.0         | 1.6.1         |                                                                                                                              |
+---------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.digitalocean    | 1.0.0         | 1.1.1         |                                                                                                                              |
+---------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.docker          | 1.4.0         | 1.5.0         |                                                                                                                              |
+---------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.general         | 2.4.0         | 2.5.1         |                                                                                                                              |
+---------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.grafana         | 1.2.0         | 1.2.1         |                                                                                                                              |
+---------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.kubernetes      | 1.2.0         | 1.2.1         |                                                                                                                              |
+---------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.mysql           | 1.3.0         | 1.4.0         |                                                                                                                              |
+---------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.network         | 2.1.0         | 2.1.1         |                                                                                                                              |
+---------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.okd             | 1.1.0         | 1.1.2         |                                                                                                                              |
+---------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| community.vmware          | 1.8.0         | 1.9.0         |                                                                                                                              |
+---------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| containers.podman         | 1.4.4         | 1.5.0         |                                                                                                                              |
+---------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| f5networks.f5_modules     | 1.8.1         | 1.9.0         |                                                                                                                              |
+---------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| hetzner.hcloud            | 1.3.1         | 1.4.2         |                                                                                                                              |
+---------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| kubernetes.core           | 1.2.0         | 1.2.1         |                                                                                                                              |
+---------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| netapp.ontap              | 21.3.1        | 21.4.0        |                                                                                                                              |
+---------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| netapp_eseries.santricity | 1.1.0         | 1.2.7         |                                                                                                                              |
+---------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| ngine_io.cloudstack       | 2.0.0         | 2.1.0         |                                                                                                                              |
+---------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| openstack.cloud           | 1.3.0         | 1.4.0         | The collection did not have a changelog in this version.                                                                     |
+---------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| sensu.sensu_go            | 1.9.3         | 1.9.4         |                                                                                                                              |
+---------------------------+---------------+---------------+------------------------------------------------------------------------------------------------------------------------------+

Major Changes
-------------

community.mysql
~~~~~~~~~~~~~~~

- mysql_user - the ``REQUIRESSL`` is an alias for the ``ssl`` key in the ``tls_requires`` option in ``community.mysql`` 2.0.0 and support will be dropped altogether in ``community.mysql`` 3.0.0 (https://github.com/ansible-collections/community.mysql/issues/121).

Minor Changes
-------------

Ansible-base
~~~~~~~~~~~~

- module payload builder - module_utils imports in any nested block (eg, ``try``, ``if``) are treated as optional during module payload builds; this allows modules to implement runtime fallback behavior for module_utils that do not exist in older versions of Ansible.

ansible.windows
~~~~~~~~~~~~~~~

- win_certificate_store - Added functionality to open the store for a service account using ``store_type=service store_location=<service name>``
- win_user - Support specifying groups using the SecurityIdentifier - https://github.com/ansible-collections/ansible.windows/issues/153

chocolatey.chocolatey
~~~~~~~~~~~~~~~~~~~~~

- win_chocolatey - Support for removing dependencies added with remove_dependencies option.

community.digitalocean
~~~~~~~~~~~~~~~~~~~~~~

- digital_ocean_block_storage - included ability to resize Block Storage Volumes (https://github.com/ansible-collections/community.digitalocean/issues/38).

community.docker
~~~~~~~~~~~~~~~~

- Add the ``use_ssh_client`` option to most docker modules and plugins (https://github.com/ansible-collections/community.docker/issues/108, https://github.com/ansible-collections/community.docker/pull/114).

community.general
~~~~~~~~~~~~~~~~~

- apache2_mod_proxy - refactored/cleaned-up part of the code (https://github.com/ansible-collections/community.general/pull/2142).
- atomic_container - using ``get_bin_path()`` before calling ``run_command()`` (https://github.com/ansible-collections/community.general/pull/2144).
- atomic_host - using ``get_bin_path()`` before calling ``run_command()`` (https://github.com/ansible-collections/community.general/pull/2144).
- atomic_image - using ``get_bin_path()`` before calling ``run_command()`` (https://github.com/ansible-collections/community.general/pull/2144).
- beadm - minor refactor converting multiple statements to a single list literal (https://github.com/ansible-collections/community.general/pull/2160).
- bitbucket_pipeline_variable - removed unreachable code (https://github.com/ansible-collections/community.general/pull/2157).
- hiera lookup - minor refactor converting multiple statements to a single list literal (https://github.com/ansible-collections/community.general/pull/2160).
- ipa_config - add new options ``ipaconfigstring``, ``ipadefaultprimarygroup``, ``ipagroupsearchfields``, ``ipahomesrootdir``, ``ipabrkauthzdata``, ``ipamaxusernamelength``, ``ipapwdexpadvnotify``, ``ipasearchrecordslimit``, ``ipasearchtimelimit``, ``ipauserauthtype``, and ``ipausersearchfields`` (https://github.com/ansible-collections/community.general/pull/2116).
- ipa_user - fix ``userauthtype`` option to take in list of strings for the multi-select field instead of single string (https://github.com/ansible-collections/community.general/pull/2174).
- ipwcli_dns - minor refactor converting multiple statements to a single list literal (https://github.com/ansible-collections/community.general/pull/2160).
- java_cert - change ``state: present`` to check certificates by hash, not just alias name (https://github.com/ansible/ansible/issues/43249).
- jira - added ``attach`` operation, which allows a user to attach a file to an issue (https://github.com/ansible-collections/community.general/pull/2192).
- jira - added parameter ``account_id`` for compatibility with recent versions of JIRA (https://github.com/ansible-collections/community.general/issues/818, https://github.com/ansible-collections/community.general/pull/1978).
- known_hosts module utils - minor refactor converting multiple statements to a single list literal (https://github.com/ansible-collections/community.general/pull/2160).
- module_helper module utils - added management of facts and adhoc setting of the initial value for variables (https://github.com/ansible-collections/community.general/pull/2188).
- module_helper module utils - added mechanism to manage variables, providing automatic output of variables, change status and diff information (https://github.com/ansible-collections/community.general/pull/2162).
- nictagadm - minor refactor converting multiple statements to a single list literal (https://github.com/ansible-collections/community.general/pull/2160).
- npm - add ``no_bin_links`` option (https://github.com/ansible-collections/community.general/issues/2128).
- ovh_ip_failover - removed unreachable code (https://github.com/ansible-collections/community.general/pull/2157).
- proxmox inventory plugin - added ``Constructable`` class to the inventory to provide options ``strict``, ``keyed_groups``, ``groups``, and ``compose`` (https://github.com/ansible-collections/community.general/pull/2180).
- proxmox inventory plugin - added ``proxmox_agent_interfaces`` fact describing network interfaces returned from a QEMU guest agent (https://github.com/ansible-collections/community.general/pull/2148).
- rhevm - removed unreachable code (https://github.com/ansible-collections/community.general/pull/2157).
- smartos_image_info - minor refactor converting multiple statements to a single list literal (https://github.com/ansible-collections/community.general/pull/2160).
- svr4pkg - minor refactor converting multiple statements to a single list literal (https://github.com/ansible-collections/community.general/pull/2160).
- xattr - minor refactor converting multiple statements to a single list literal (https://github.com/ansible-collections/community.general/pull/2160).
- xfconf - changed implementation to use ``ModuleHelper`` new features (https://github.com/ansible-collections/community.general/pull/2188).
- zfs_facts - minor refactor converting multiple statements to a single list literal (https://github.com/ansible-collections/community.general/pull/2160).
- zpool_facts - minor refactor converting multiple statements to a single list literal (https://github.com/ansible-collections/community.general/pull/2160).

community.mysql
~~~~~~~~~~~~~~~

- mysql module utils - change deprecated connection parameters ``passwd`` and ``db`` to ``password`` and ``database`` (https://github.com/ansible-collections/community.mysql/pull/116).
- mysql_collection - introduce codebabse split to handle divergences between MySQL and MariaDB (https://github.com/ansible-collections/community.mysql/pull/103).
- mysql_info - add `version.full` and `version.suffix` return values (https://github.com/ansible-collections/community.mysql/issues/114).
- mysql_user - deprecate the ``REQUIRESSL`` privilege (https://github.com/ansible-collections/community.mysql/issues/101).

community.vmware
~~~~~~~~~~~~~~~~

- vmware_guest_instant_clone - supported esxi_hostname parameter as an alias (https://github.com/ansible-collections/community.vmware/pull/745).
- vmware_resource_pool - Add parent_resource_pool parameter which is mutually exclusive with cluster and esxi_hostname (https://github.com/ansible-collections/community.vmware/issues/717)
- vmware_vm_inventory - add an example of FQDN as hostname (https://github.com/ansible-collections/community.vmware/issues/678).
- vmware_vm_inventory - skip disconnected VMs.

containers.podman
~~~~~~~~~~~~~~~~~

- Podman login module

f5networks.f5_modules
~~~~~~~~~~~~~~~~~~~~~

- Add token refresh handling to bigiq local client
- Added requirement to install ipaddress package for python versions earlier than 3.5

hetzner.hcloud
~~~~~~~~~~~~~~

- hcloud_server - improve the handling of deprecated images
- hcloud_server - improve the validation and error response for not existing images
- inventory - support jinjia templating within `token`

netapp.ontap
~~~~~~~~~~~~

- na_ontap_igroups - new option ``initiator_names`` as a replacement for ``initiators`` (still supported as an alias).
- na_ontap_igroups - new option ``initiator_objects`` to support initiator comments (requires ONTAP 9.9).
- na_ontap_lun - allow new LUNs to use different igroup or os_type when using SAN application.
- na_ontap_lun - ignore small increase (lower than provisioned) and small decrease (< 10%) in ``total_size``.
- na_ontap_node - added REST support for ONTAP node modify and rename.
- na_ontap_volume - warn when attempting to modify application only options.
- na_ontap_volume_efficiency - new option 'start_ve_build_metadata' scan the entire and generate fingerprint database.
- na_ontap_volume_efficiency - new option 'start_ve_delete_checkpoint' delete checkpoint and start the operation from the begining.
- na_ontap_volume_efficiency - new option 'start_ve_qos_policy' defines the QoS policy for the operation.
- na_ontap_volume_efficiency - new option 'start_ve_queue_operation' queue if an exisitng operation is already running.
- na_ontap_volume_efficiency - new option 'start_ve_scan_all' scan the entire volume without applying share block optimization.
- na_ontap_volume_efficiency - new option 'start_ve_scan_old_data' scan the file system to process all the existing data.
- na_ontap_volume_efficiency - new option 'stop_ve_all_operations' all running and queued operations to be stopped.
- na_ontap_volume_efficiency - new option to allow volume efficiency to be started and stopped 'volume_efficiency'.

netapp_eseries.santricity
~~~~~~~~~~~~~~~~~~~~~~~~~

- Add IPv6 and FQDN support for NTP
- Add IPv6 support for DNS
- Add criteria_drive_max_size option to na_santricity_storagepool and nar_santricity_host role.
- Add resource-provisioned volumes option to globals and nar_santricity_management role.
- Added nvme4k as a drive type interface to the na_santricity_storagepool module.
- Added options for critical and warning threshold setting in na_santricity_storagepool module and nar_santricity_host role.
- Fix dynamic disk pool critical and warning threshold settings.
- Remove resource-provisioned volumes setting from na_santicity_global module and nar_santricity_management role."
- na_santricity_discover - Add support for discovering storage systems directly using devmgr/v2/storage-systems/1/about endpoint since its old method of discover is being deprecated.
- na_santricity_facts - Add storage system information to facilitate ``netapp_eseries.host`` collection various protocol configuration.
- na_santricity_server_certificate - New module to configure storage system's web server certificate configuration.
- na_santricity_snapshot - New module to configure NetApp E-Series Snapshot consistency groups any number of base volumes.
- na_santricity_volume - Add percentage size unit (pct) and which allows the creates volumes based on the total storage pool size.
- nar_santricity_host - Add eseries_storage_pool_configuration list options, criteria_volume_count, criteria_reserve_free_capacity_pct, and common_volume_host to facilitate volumes based on percentages of storage pool or volume group.
- nar_santricity_host - Add support for snapshot group creation.
- nar_santricity_host - Improve host mapping information discovery.
- nar_santricity_host - Improve storage system discovery related error messages.
- nar_santricity_management - Add support for server certificate management.

ngine_io.cloudstack
~~~~~~~~~~~~~~~~~~~

- cs_physical_network - Added VXLAN as an option of isolation methods (https://github.com/ngine-io/ansible-collection-cloudstack/pull/73).
- instance - New style inventory plugin implemented for instances (https://github.com/ngine-io/ansible-collection-cloudstack/pull/66)

Deprecated Features
-------------------

community.vmware
~~~~~~~~~~~~~~~~

- vmware_vmkernel_ip_config - deprecate in favor of vmware_vmkernel (https://github.com/ansible-collections/community.vmware/pull/667).

f5networks.f5_modules
~~~~~~~~~~~~~~~~~~~~~

- Support for Python versions earlier than 3.5 is being deprecated

Security Fixes
--------------

community.general
~~~~~~~~~~~~~~~~~

- java_cert - remove password from ``run_command`` arguments (https://github.com/ansible-collections/community.general/pull/2008).
- java_keystore - pass secret to keytool through an environment variable to not expose it as a commandline argument (https://github.com/ansible-collections/community.general/issues/1668).

community.vmware
~~~~~~~~~~~~~~~~

- vmware_host_iscsi - mark the ``chap_secret`` parameter as ``no_log`` to avoid accidental leaking of secrets in logs (https://github.com/ansible-collections/community.vmware/pull/715).
- vmware_host_iscsi - mark the ``mutual_chap_secret`` parameter as ``no_log`` to avoid accidental leaking of secrets in logs (https://github.com/ansible-collections/community.vmware/pull/715).
- vmware_vc_infraprofile_info - mark the ``decryption_key`` parameter as ``no_log`` to avoid accidental leaking of secrets in logs (https://github.com/ansible-collections/community.vmware/pull/715).
- vmware_vc_infraprofile_info - mark the ``encryption_key`` parameter as ``no_log`` to avoid accidental leaking of secrets in logs (https://github.com/ansible-collections/community.vmware/pull/715).

hetzner.hcloud
~~~~~~~~~~~~~~

- hcloud_certificate - mark the ``private_key`` parameter as ``no_log`` to prevent potential leaking of secret values (https://github.com/ansible-collections/hetzner.hcloud/pull/70).

Bugfixes
--------

Ansible-base
~~~~~~~~~~~~

- Fix adding unrelated candidate names to the plugin loader redirect list.
- Strategy - When building the task in the Strategy from the Worker, ensure it is properly marked as finalized and squashed. Addresses an issue with ``ansible_failed_task``. (https://github.com/ansible/ansible/issues/57399)
- ansible-test - The ``--export`` option for ``ansible-test coverage`` is now limited to the ``combine`` command. It was previously available for reporting commands on which it had no effect.
- ansible-test - The ``ansible-test coverage combine`` option ``--export`` now exports relative paths. This avoids loss of coverage data when aggregating across systems with different absolute paths. Paths will be converted back to absolute when generating reports.
- ansible-test - ensure unit test paths for connection and inventory plugins are correctly identified for collections (https://github.com/ansible/ansible/issues/73876).
- apt - fix policy_rc_d parameter throwing an exception when restoring original file (https://github.com/ansible/ansible/issues/66211)
- debug action - prevent setting facts when displaying ansible_facts (https://github.com/ansible/ansible/issues/74060).
- find - fix default pattern when use_regex is true (https://github.com/ansible/ansible/issues/50067).
- restrict module valid JSON parsed output to objects as lists are not valid responses.
- setup - fix error handling on bad subset given.
- setup, don't give up on all local facts gathering if one script file fails.
- su become plugin - ensure correct type for localization option (https://github.com/ansible/ansible/issues/73837).

ansible.windows
~~~~~~~~~~~~~~~

- setup - Return correct epoch integer value for the ``ansible_date_time.epoch_int`` fact
- win_template - Fix changed internal API that win_template uses to work with devel again
- win_user - Compare existing vs desired groups in a case insenstive way - https://github.com/ansible-collections/ansible.windows/issues/168

chocolatey.chocolatey
~~~~~~~~~~~~~~~~~~~~~

- All modules - Added fallback to default choco install path for auxiliary modules to workaround issue in OpenSSH library under Windows. (https://github.com/PowerShell/Win32-OpenSSH#1329)
- win_chocolatey - Module can now handle uninstallation correctly for both side-by-side and normal package installations.

community.crypto
~~~~~~~~~~~~~~~~

- acme_* modules - fix wrong usages of ``ACMEProtocolException`` (https://github.com/ansible-collections/community.crypto/pull/216, https://github.com/ansible-collections/community.crypto/pull/217).

community.digitalocean
~~~~~~~~~~~~~~~~~~~~~~

- digital_ocean_certificate_info - fix retrieving certificate by ID (https://github.com/ansible-collections/community.digitalocean/issues/35).
- digital_ocean_domain - module is now idempotent when called without IP (https://github.com/ansible-collections/community.digitalocean/issues/21).
- digital_ocean_load_balancer_info - fix retrieving load balancer by ID (https://github.com/ansible-collections/community.digitalocean/issues/35).
- digitalocean - Drop collection version from README.md (https://github.com/ansible-collections/community.digitalocean/issues/63).

community.docker
~~~~~~~~~~~~~~~~

- all modules - use ``to_native`` to convert exceptions to strings (https://github.com/ansible-collections/community.docker/pull/121).

community.general
~~~~~~~~~~~~~~~~~

- dimensiondata_network - bug when formatting message, instead of % a simple comma was used (https://github.com/ansible-collections/community.general/pull/2139).
- funcd connection plugin - can now load (https://github.com/ansible-collections/community.general/pull/2235).
- github_repo - PyGithub bug does not allow explicit port in ``base_url``. Specifying port is not required (https://github.com/PyGithub/PyGithub/issues/1913).
- haproxy - fix a bug preventing haproxy from properly entering ``DRAIN`` mode (https://github.com/ansible-collections/community.general/issues/1913).
- ipa_user - allow ``sshpubkey`` to permit multiple word comments (https://github.com/ansible-collections/community.general/pull/2159).
- java_cert - allow setting ``state: absent`` by providing just the ``cert_alias`` (https://github.com/ansible/ansible/issues/27982).
- java_cert - properly handle proxy arguments when the scheme is provided (https://github.com/ansible/ansible/issues/54481).
- java_keystore - improve error handling and return ``cmd`` as documented. Force ``LANG``, ``LC_ALL`` and ``LC_MESSAGES`` environment variables to ``C`` to rely on ``keytool`` output parsing. Fix pylint's ``unused-variable`` and ``no-else-return`` hints (https://github.com/ansible-collections/community.general/pull/2183).
- java_keystore - use tempfile lib to create temporary files with randomized names, and remove the temporary PKCS#12 keystore as well as other materials (https://github.com/ansible-collections/community.general/issues/1667).
- jira - fixed calling of ``isinstance`` (https://github.com/ansible-collections/community.general/issues/2234).
- jira - fixed fields' update in ticket transitions (https://github.com/ansible-collections/community.general/issues/818).
- kibana_plugin - added missing parameters to ``remove_plugin`` when using ``state=present force=true``, and fix potential quoting errors when invoking ``kibana`` (https://github.com/ansible-collections/community.general/pull/2143).
- module_helper module utils - fixed decorator ``cause_changes`` (https://github.com/ansible-collections/community.general/pull/2203).
- pkgutil - fixed calls to ``list.extend()`` (https://github.com/ansible-collections/community.general/pull/2161).
- vmadm - correct type of list elements in ``resolvers`` parameter (https://github.com/ansible-collections/community.general/issues/2135).
- xfconf - module was not honoring check mode when ``state`` was ``absent`` (https://github.com/ansible-collections/community.general/pull/2185).

community.grafana
~~~~~~~~~~~~~~~~~

- Fix issue with grafana_user that failed to create admin user (#142)

community.kubernetes
~~~~~~~~~~~~~~~~~~~~

- fix missing requirements.txt file in kubernetes.core (https://github.com/ansible-collections/community.kubernetes/pull/401).
- pin molecule version to <3.3.0 to fix breaking changes (https://github.com/ansible-collections/community.kubernetes/pull/403).

community.mysql
~~~~~~~~~~~~~~~

- mysql_user - add support for ``REPLICA MONITOR`` privilege (https://github.com/ansible-collections/community.mysql/issues/105).

community.network
~~~~~~~~~~~~~~~~~

- {cnos,icx}_static_route modules - fix modules to work with ansible-core 2.11 (https://github.com/ansible-collections/community.network/pull/228).

community.okd
~~~~~~~~~~~~~

- add missing requirements.txt file needed for execution environments (https://github.com/ansible-collections/community.okd/pull/78).
- include requirements.txt in downstream build process (https://github.com/ansible-collections/community.okd/pull/81).
- openshift_route - default to ``no_log=False`` for the ``key`` parameter in TLS configuration to fix sanity failures (https://github.com/ansible-collections/community.okd/pull/77).
- restrict molecule version to <3.3.0 to address breaking change (https://github.com/ansible-collections/community.okd/pull/77).
- update CI to work with ansible 2.11 (https://github.com/ansible-collections/community.okd/pull/80).

community.vmware
~~~~~~~~~~~~~~~~

- vmware - add the default value of parameter resource_pool_name in the find_resource_pool_by_name function (https://github.com/ansible-collections/community.vmware/pull/670).
- vmware_cluster_vsan - fixed a bug that made the module fail when advanced_options is not set (https://github.com/ansible-collections/community.vmware/issues/728).
- vmware_deploy_ovf - fixed an issue that a return value hasn't the instance key when the power_on parameter is False (https://github.com/ansible-collections/community.vmware/pull/698).
- vmware_deploy_ovf - fixed an issue that deploy template in datacenter with more than one standalone hosts (https://github.com/ansible-collections/community.vmware/pull/670).
- vmware_guest - fixed a bug that made the module fail when disk.controller_number or disk.unit_number are 0 (https://github.com/ansible-collections/community.vmware/issues/703).
- vmware_local_user_manager - fixed to require local_user_password when the state is present (https://github.com/ansible-collections/community.vmware/pull/724).
- vmware_vm_inventory - Skip over ghost tags attached to virtual machines (https://github.com/ansible-collections/community.vmware/issues/681).

containers.podman
~~~~~~~~~~~~~~~~~

- Add IPv6 support for publishing ports
- Add sigrtmin+3 signal (required for systemd containers)
- Add support for Podman Pod restart
- Convert IPv6 to shorten form
- Fix error with images info where no images
- Fix idempotency for rootless networks from v3
- Fix no_log for newer ansible-test
- Fix uppercase labels idempotency issue
- Stop pods without recreating them

f5networks.f5_modules
~~~~~~~~~~~~~~~~~~~~~

- Added Fix for bigip_config check mode issue
- Fix for bigip_device_license license reactivation
- Fix for documentation bigip_data_group module doesn't check records content
- Fix issue with expired tokens causing module run to fail in bigiq_device_discovery
- Fix lookup plugin support for bigiq_license
- Fixes issues with downloading ASM policies in binary format

hetzner.hcloud
~~~~~~~~~~~~~~

- hcloud_firewall - fix idempotence related to rules comparison (https://github.com/ansible-collections/hetzner.hcloud/pull/71).
- hcloud_load_balancer_service - fix imported wrong HealthCheck from hcloud-python (https://github.com/ansible-collections/hetzner.hcloud/pull/73).
- hcloud_server - fix idempotence related to firewall handling (https://github.com/ansible-collections/hetzner.hcloud/pull/71).
- inventory fix image name was set as server type instead of the correct server type

kubernetes.core
~~~~~~~~~~~~~~~

- fix missing requirements.txt file in kubernetes.core (https://github.com/ansible-collections/kubernetes.core/pull/401).
- pin molecule version to <3.3.0 to fix breaking changes (https://github.com/ansible-collections/kubernetes.core/pull/403).

netapp.ontap
~~~~~~~~~~~~

- na_ontap_autosupport - warn when password is present in ``proxy_url`` as it makes the operation not idempotent.
- na_ontap_cluster - ignore ZAPI EMS log error when in pre-cluster mode.
- na_ontap_lun - SAN application is not supported on 9.6 and only partially supported on 9.7 (no modify).
- na_ontap_svm - iscsi current status is not read correctly (mispelled issi).

netapp_eseries.santricity
~~~~~~~~~~~~~~~~~~~~~~~~~

- Add missing http(s) proxy username and password parameters from na_santricity_asup module and nar_santricity_management role."
- Add missing storage pool configuration parameter, criteria_drive_interface_type, to nar_santricity_host role.
- Fix drive firmware upgrade issue that prevented updating firware when drive was in use.
- Fix jinja issue with collecting certificates paths in nar_santricity_management role.
- nar_santricity_host - Fix README.md examples.

sensu.sensu_go
~~~~~~~~~~~~~~

- Make sure we lazy-load Windows-related content.

New Plugins
-----------

Filter
~~~~~~

- community.general.dict - The ``dict`` function as a filter: converts a list of tuples to a dictionary
- community.general.path_join - Redirects to ansible.builtin.path_join for ansible-base 2.10 or newer, and provides a compatible implementation for Ansible 2.9

Inventory
~~~~~~~~~

- community.digitalocean.digitalocean - DigitalOcean Inventory Plugin
- ngine_io.cloudstack.instance - Apache CloudStack instance inventory source

New Modules
-----------

ansible.windows
~~~~~~~~~~~~~~~

- ansible.windows.win_powershell - Run PowerShell scripts

community.digitalocean
~~~~~~~~~~~~~~~~~~~~~~

- community.digitalocean.digital_ocean_domain_record - Manage DigitalOcean domain records
- community.digitalocean.digital_ocean_firewall - Manage cloud firewalls within DigitalOcean

community.docker
~~~~~~~~~~~~~~~~

- community.docker.docker_container_exec - Execute command in a docker container

community.general
~~~~~~~~~~~~~~~~~

Identity
^^^^^^^^

Ipa
...

- community.general.ipa_otpconfig - Manage FreeIPA OTP Configuration Settings
- community.general.ipa_otptoken - Manage FreeIPA OTPs

Monitoring
^^^^^^^^^^

- community.general.spectrum_model_attrs - Enforce a model's attributes in CA Spectrum.

Net Tools
^^^^^^^^^

Pritunl
.......

- community.general.pritunl_org - Manages Pritunl Organizations using the Pritunl API
- community.general.pritunl_org_info - List Pritunl Organizations using the Pritunl API

community.vmware
~~~~~~~~~~~~~~~~

- community.vmware.vmware_guest_instant_clone - Instant Clone VM
- community.vmware.vmware_guest_storage_policy - Set VM Home and disk(s) storage policy profiles.

containers.podman
~~~~~~~~~~~~~~~~~

- containers.podman.podman_login - Login to a container registry using podman

netapp.ontap
~~~~~~~~~~~~

- netapp.ontap.na_ontap_cifs_local_user_modify - NetApp ONTAP modify local CIFS user.
- netapp.ontap.na_ontap_disk_options - NetApp ONTAP modify storage disk options
- netapp.ontap.na_ontap_fpolicy_event - NetApp ONTAP FPolicy policy event configuration
- netapp.ontap.na_ontap_fpolicy_ext_engine - NetApp ONTAP fPolicy external engine configuration.
- netapp.ontap.na_ontap_fpolicy_scope - NetApp ONTAP - Create, delete or modify an FPolicy policy scope configuration.
- netapp.ontap.na_ontap_fpolicy_status - NetApp ONTAP - Enables or disables the specified fPolicy policy
- netapp.ontap.na_ontap_snaplock_clock - NetApp ONTAP Sets the snaplock compliance clock.

Unchanged Collections
---------------------

- amazon.aws (still version 1.4.1)
- ansible.netcommon (still version 1.5.0)
- ansible.posix (still version 1.2.0)
- ansible.utils (still version 2.0.2)
- arista.eos (still version 1.3.0)
- awx.awx (still version 17.1.0)
- check_point.mgmt (still version 2.0.0)
- cisco.aci (still version 2.0.0)
- cisco.asa (still version 1.0.4)
- cisco.intersight (still version 1.0.12)
- cisco.ios (still version 1.3.0)
- cisco.iosxr (still version 1.2.1)
- cisco.meraki (still version 2.2.1)
- cisco.mso (still version 1.1.0)
- cisco.nso (still version 1.0.3)
- cisco.nxos (still version 1.4.0)
- cisco.ucs (still version 1.6.0)
- cloudscale_ch.cloud (still version 2.1.0)
- community.aws (still version 1.4.0)
- community.azure (still version 1.0.0)
- community.fortios (still version 1.0.0)
- community.google (still version 1.0.0)
- community.hashi_vault (still version 1.1.3)
- community.hrobot (still version 1.1.1)
- community.kubevirt (still version 1.0.0)
- community.libvirt (still version 1.0.1)
- community.mongodb (still version 1.2.1)
- community.postgresql (still version 1.2.0)
- community.proxysql (still version 1.0.0)
- community.rabbitmq (still version 1.0.3)
- community.routeros (still version 1.1.0)
- community.skydive (still version 1.0.0)
- community.sops (still version 1.0.6)
- community.windows (still version 1.3.0)
- community.zabbix (still version 1.3.0)
- cyberark.conjur (still version 1.1.0)
- cyberark.pas (still version 1.0.6)
- dellemc.openmanage (still version 3.2.0)
- dellemc.os10 (still version 1.1.1)
- dellemc.os6 (still version 1.0.7)
- dellemc.os9 (still version 1.0.4)
- fortinet.fortimanager (still version 2.0.1)
- fortinet.fortios (still version 1.1.9)
- frr.frr (still version 1.0.3)
- gluster.gluster (still version 1.0.1)
- google.cloud (still version 1.0.2)
- ibm.qradar (still version 1.0.3)
- infinidat.infinibox (still version 1.2.4)
- inspur.sm (still version 1.1.2)
- junipernetworks.junos (still version 1.3.0)
- mellanox.onyx (still version 1.0.0)
- netapp.aws (still version 20.9.0)
- netapp.elementsw (still version 20.11.0)
- netbox.netbox (still version 2.1.0)
- ngine_io.exoscale (still version 1.0.0)
- ngine_io.vultr (still version 1.1.0)
- openvswitch.openvswitch (still version 1.2.0)
- ovirt.ovirt (still version 1.4.1)
- purestorage.flasharray (still version 1.7.0)
- purestorage.flashblade (still version 1.5.0)
- servicenow.servicenow (still version 1.0.4)
- splunk.es (still version 1.0.2)
- t_systems_mms.icinga_director (still version 1.16.0)
- theforeman.foreman (still version 1.5.1)
- vyos.vyos (still version 1.1.1)
- wti.remote (still version 1.0.1)

v3.2.0
======

.. contents::
  :local:
  :depth: 2

Release Summary
---------------

Release Date: 2021-03-30

`Porting Guide <https://docs.ansible.com/ansible/devel/porting_guides.html>`_

Ansible-base
------------

Ansible 3.2.0 contains Ansible-base version 2.10.7.
This is a newer version than version 2.10.5 contained in the previous Ansible release.

The changes are reported in the combined changelog below.

Changed Collections
-------------------

If not mentioned explicitly, the changes are reported in the combined changelog below.

+-------------------------------+---------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Collection                    | Ansible 3.1.0 | Ansible 3.2.0 | Notes                                                                                                                                                                                                                                      |
+===============================+===============+===============+============================================================================================================================================================================================================================================+
| ansible.utils                 | 2.0.1         | 2.0.2         |                                                                                                                                                                                                                                            |
+-------------------------------+---------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cisco.intersight              | 1.0.11        | 1.0.12        | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.                                                                                                               |
+-------------------------------+---------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.crypto              | 1.5.0         | 1.6.0         |                                                                                                                                                                                                                                            |
+-------------------------------+---------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.docker              | 1.3.0         | 1.4.0         |                                                                                                                                                                                                                                            |
+-------------------------------+---------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.general             | 2.2.0         | 2.4.0         |                                                                                                                                                                                                                                            |
+-------------------------------+---------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.hashi_vault         | 1.1.2         | 1.1.3         |                                                                                                                                                                                                                                            |
+-------------------------------+---------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.network             | 2.0.1         | 2.1.0         |                                                                                                                                                                                                                                            |
+-------------------------------+---------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.postgresql          | 1.1.1         | 1.2.0         |                                                                                                                                                                                                                                            |
+-------------------------------+---------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.sops                | 1.0.5         | 1.0.6         |                                                                                                                                                                                                                                            |
+-------------------------------+---------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.zabbix              | 1.2.0         | 1.3.0         |                                                                                                                                                                                                                                            |
+-------------------------------+---------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cyberark.pas                  | 1.0.5         | 1.0.6         | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.                                                                                                               |
+-------------------------------+---------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| dellemc.openmanage            | 3.1.0         | 3.2.0         |                                                                                                                                                                                                                                            |
+-------------------------------+---------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| hetzner.hcloud                | 1.2.1         | 1.3.1         |                                                                                                                                                                                                                                            |
+-------------------------------+---------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ovirt.ovirt                   | 1.3.1         | 1.4.1         |                                                                                                                                                                                                                                            |
+-------------------------------+---------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| purestorage.flasharray        | 1.6.2         | 1.7.0         |                                                                                                                                                                                                                                            |
+-------------------------------+---------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| purestorage.flashblade        | 1.4.0         | 1.5.0         |                                                                                                                                                                                                                                            |
+-------------------------------+---------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| sensu.sensu_go                | 1.9.1         | 1.9.3         |                                                                                                                                                                                                                                            |
+-------------------------------+---------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| t_systems_mms.icinga_director | 1.15.0        | 1.16.0        | You can find the collection's changelog at `https://github.com/T-Systems-MMS/ansible-collection-icinga-director/blob/master/CHANGELOG.md <https://github.com/T-Systems-MMS/ansible-collection-icinga-director/blob/master/CHANGELOG.md>`_. |
+-------------------------------+---------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Minor Changes
-------------

Ansible-base
~~~~~~~~~~~~

- ansible-test - Added Ubuntu 20.04 LTS image to the default completion list
- ansible-test - Generation of an ``egg-info`` directory, if needed, is now done after installing test dependencies and before running tests. When running from an installed version of ``ansible-test`` a temporary directory is used to avoid permissions issues. Previously it was done before installing test dependencies and adjacent to the installed directory.
- ansible-test - now makes a better attempt to support podman when calling ``docker images`` and asking for JSON format.
- inventory cache - do not show a warning when the cache file does not (yet) exist.

community.crypto
~~~~~~~~~~~~~~~~

- acme module_utils - the ``acme`` module_utils has been split up into several Python modules (https://github.com/ansible-collections/community.crypto/pull/184).
- acme_* modules - codebase refactor which should not be visible to end-users (https://github.com/ansible-collections/community.crypto/pull/184).
- acme_* modules - support account key passphrases for ``cryptography`` backend (https://github.com/ansible-collections/community.crypto/issues/197, https://github.com/ansible-collections/community.crypto/pull/207).
- acme_certificate_revoke - support revoking by private keys that are passphrase protected for ``cryptography`` backend (https://github.com/ansible-collections/community.crypto/pull/207).
- acme_challenge_cert_helper - add ``private_key_passphrase`` parameter (https://github.com/ansible-collections/community.crypto/pull/207).

community.docker
~~~~~~~~~~~~~~~~

- docker_swarm_service - change ``publish.published_port`` option from mandatory to optional. Docker will assign random high port if not specified (https://github.com/ansible-collections/community.docker/issues/99).

community.general
~~~~~~~~~~~~~~~~~

- archive - refactored some reused code out into a couple of functions (https://github.com/ansible-collections/community.general/pull/2061).
- csv module utils - new module_utils for shared functions between ``from_csv`` filter and ``read_csv`` module (https://github.com/ansible-collections/community.general/pull/2037).
- ipa_sudorule - add support for setting sudo runasuser (https://github.com/ansible-collections/community.general/pull/2031).
- jenkins_job - add a ``validate_certs`` parameter that allows disabling TLS/SSL certificate validation (https://github.com/ansible-collections/community.general/issues/255).
- kibana_plugin - add parameter for passing ``--allow-root`` flag to kibana and kibana-plugin commands (https://github.com/ansible-collections/community.general/pull/2014).
- proxmox - added ``purge`` module parameter for use when deleting lxc's with HA options (https://github.com/ansible-collections/community.general/pull/2013).
- proxmox inventory plugin - added ``tags_parsed`` fact containing tags parsed as a list (https://github.com/ansible-collections/community.general/pull/1949).
- proxmox_kvm - added new module parameter ``tags`` for use with PVE 6+ (https://github.com/ansible-collections/community.general/pull/2000).
- rax - elements of list parameters are now validated (https://github.com/ansible-collections/community.general/pull/2006).
- rax_cdb_user - elements of list parameters are now validated (https://github.com/ansible-collections/community.general/pull/2006).
- rax_scaling_group - elements of list parameters are now validated (https://github.com/ansible-collections/community.general/pull/2006).
- read_csv - refactored read_csv module to use shared csv functions from csv module_utils (https://github.com/ansible-collections/community.general/pull/2037).
- redfish_* modules, redfish_utils module utils - add support for Redfish session create, delete, and authenticate (https://github.com/ansible-collections/community.general/issues/1975).
- snmp_facts - added parameters ``timeout`` and ``retries`` to module (https://github.com/ansible-collections/community.general/issues/980).
- vdo - add ``force`` option (https://github.com/ansible-collections/community.general/issues/2101).

community.network
~~~~~~~~~~~~~~~~~

- edgeos_config - match the space after ``set`` and ``delete`` commands (https://github.com/ansible-collections/community.network/pull/199).
- nclu - execute ``net commit description <description>`` only if changed ``net pending``'s diff field (https://github.com/ansible-collections/community.network/pull/219).

community.postgresql
~~~~~~~~~~~~~~~~~~~~

- postgresql_info - add the ``patch``, ``full``, and ``raw`` values of the ``version`` return value (https://github.com/ansible-collections/community.postgresql/pull/68).
- postgresql_ping - add the ``patch``, ``full``, and ``raw`` values of the ``server_version`` return value (https://github.com/ansible-collections/community.postgresql/pull/70).

community.zabbix
~~~~~~~~~~~~~~~~

- zabbix_agent - added support for installations on arm64 systems (https://github.com/ansible-collections/community.zabbix/pull/320).
- zabbix_proxy - now supports configuring StatsAllowedIP (https://github.com/ansible-collections/community.zabbix/pull/337).
- zabbix_server - added support for installtions on arm64 systems (https://github.com/ansible-collections/community.zabbix/pull/320).
- zabbix_web - added support for installtions on arm64 systems (https://github.com/ansible-collections/community.zabbix/pull/320).

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- ome_template - Allows to deploy a template on device groups.

hetzner.hcloud
~~~~~~~~~~~~~~

- Add firewalls to hcloud_server module

ovirt.ovirt
~~~~~~~~~~~

- cluster_upgrade - Add correlation-id header (https://github.com/oVirt/ovirt-ansible-collection/pull/222).
- engine_setup - Add skip renew pki confirm (https://github.com/oVirt/ovirt-ansible-collection/pull/228).
- examples - Add recipe for removing DM device (https://github.com/oVirt/ovirt-ansible-collection/pull/233).
- hosted_engine_setup - Filter devices with unsupported bond mode (https://github.com/oVirt/ovirt-ansible-collection/pull/226).
- infra - Add reboot host parameters (https://github.com/oVirt/ovirt-ansible-collection/pull/231).
- ovirt_disk - Add SATA support (https://github.com/oVirt/ovirt-ansible-collection/pull/225).
- ovirt_user - Add ssh_public_key (https://github.com/oVirt/ovirt-ansible-collection/pull/232)

purestorage.flasharray
~~~~~~~~~~~~~~~~~~~~~~

- purefa_maintenance - New module to set maintenance windows
- purefa_pg - Add support to rename protection groups
- purefa_syslog - Add support for naming SYSLOG servers for Purity//FA 6.1 or higher

purestorage.flashblade
~~~~~~~~~~~~~~~~~~~~~~

- purefb_certs - Add update functionality for array cert
- purefb_fs - Add multiprotocol ACL support
- purefb_info - Add information regarding filesystem multiprotocol (where available)
- purefb_info - Add new parameter to provide details on admin users
- purefb_info - Add replication performace statistics
- purefb_s3user - Add ability to remove an S3 users existing access key

Breaking Changes / Porting Guide
--------------------------------

community.docker
~~~~~~~~~~~~~~~~

- docker_swarm - if ``join_token`` is specified, a returned join token with the same value will be replaced by ``VALUE_SPECIFIED_IN_NO_LOG_PARAMETER``. Make sure that you do not blindly use the join tokens from the return value of this module when the module is invoked with ``join_token`` specified! This breaking change appears in a minor release since it is necessary to fix a security issue (https://github.com/ansible-collections/community.docker/pull/103).

Deprecated Features
-------------------

community.crypto
~~~~~~~~~~~~~~~~

- acme module_utils - the ``acme`` module_utils (``ansible_collections.community.crypto.plugins.module_utils.acme``) is deprecated and will be removed in community.crypto 2.0.0. Use the new Python modules in the ``acme`` package instead (``ansible_collections.community.crypto.plugins.module_utils.acme.xxx``) (https://github.com/ansible-collections/community.crypto/pull/184).

Security Fixes
--------------

Ansible-base
~~~~~~~~~~~~

- **security issue** - Mask default and fallback values for ``no_log`` module options (CVE-2021-20228)

community.docker
~~~~~~~~~~~~~~~~

- docker_swarm - the ``join_token`` option is now marked as ``no_log`` so it is no longer written into logs (https://github.com/ansible-collections/community.docker/pull/103).

community.network
~~~~~~~~~~~~~~~~~

- avi_cloudconnectoruser - mark the ``azure_userpass``, ``gcp_credentials``, ``oci_credentials``, and ``tencent_credentials`` parameters as ``no_log`` to prevent leaking of secret values (https://github.com/ansible-collections/community.network/pull/223).
- avi_sslkeyandcertificate - mark the ``enckey_base64`` parameter as ``no_log`` to prevent potential leaking of secret values (https://github.com/ansible-collections/community.network/pull/223).
- avi_webhook - mark the ``verification_token`` parameter as ``no_log`` to prevent potential leaking of secret values (https://github.com/ansible-collections/community.network/pull/223).

community.zabbix
~~~~~~~~~~~~~~~~

- zabbix_action - no longer exposes remote SSH command password used in operations, recovery & acknowledge operations to system logs (https://github.com/ansible-collections/community.zabbix/pull/345).
- zabbix_discovery_rule - no longer exposes SNMPv3 auth and priv passphrases to system logs (https://github.com/ansible-collections/community.zabbix/pull/345).
- zabbix_host - no longer exposes SNMPv3 auth and priv passphrases to system logs (https://github.com/ansible-collections/community.zabbix/pull/345).

Bugfixes
--------

Ansible-base
~~~~~~~~~~~~

- Added unsafe_writes test.
- Always mention the name of the deprecated or tombstoned plugin in routing deprecation/tombstone messages (https://github.com/ansible/ansible/pull/73059).
- ConfigManager - Normalize ConfigParser between Python2 and Python3 to for handling comments (https://github.com/ansible/ansible/issues/73709)
- Correct the inventory source error parse handling, specifically make the config INVENTORY_ANY_UNPARSED_IS_FAILED work as expected.
- Enabled unsafe_writes for get_url which was ignoring the paramter.
- Fix incorrect variable scoping when using ``import with context`` in Jinja2 templates. (https://github.com/ansible/ansible/issues/72615)
- InventoryManager - Fix unhandled exception when given limit file was actually a directory.
- InventoryManager - Fix unhandled exception when inventory directory was empty or contained empty subdirectories (https://github.com/ansible/ansible/issues/73658).
- Restored unsafe_writes functionality which was being skipped.
- add AlmaLinux to fact gathering (https://github.com/ansible/ansible/pull/73458)
- allow become method 'su' to work on 'local' connection by allocating a fake tty.
- ansble-test - only require a collection name in deprecation warnings when necessary (https://github.com/ansible/ansible/pull/72987)
- ansible-galaxy - fixed galaxy role init command (https://github.com/ansible/ansible/issues/71977).
- ansible-inventory CLI - Deal with failures when sorting JSON and you have incompatible key types (https://github.com/ansible/ansible/issues/68950).
- ansible-test - Running tests using an installed version of ``ansible-test`` against one Python version from another no longer fails due to a missing ``egg-info`` directory. This could occur when testing plugins which import ``pkg_resources``.
- ansible-test - Running tests using an installed version of ``ansible-test`` no longer generates an error attempting to create an ``egg-info`` directory when an existing one is not found in the expected location. This could occur if the existing ``egg-info`` directory included a Python version specifier in the name.
- ansible-test - Temporarily limit ``cryptography`` to versions before 3.4 to enable tests to function.
- ansible-test - The ``--remote`` option has been updated for Python 2.7 to work around breaking changes in the newly released ``get-pip.py`` bootstrapper.
- ansible-test - The ``--remote`` option has been updated to use a versioned ``get-pip.py`` bootstrapper to avoid issues with future releases.
- ansible-test sanity changelog test - bump dependency on antsibull-changelog to 0.9.0 so that `fragments that add new plugins or objects <https://github.com/ansible-community/antsibull-changelog/blob/main/docs/changelogs.rst#adding-new-roles-playbooks-test-and-filter-plugins>`_ will not fail validation (https://github.com/ansible/ansible/pull/73428).
- default callback - Ensure that the ``host_pinned`` strategy is not treated as lockstep (https://github.com/ansible/ansible/issues/73364)
- display correct error information when an error exists in the last line of the file (https://github.com/ansible/ansible/issues/16456)
- ensure find_mount_point consistently returns text.
- ensure we don't clobber role vars data when getting an empty file
- facts - properly report virtualization facts for Linux guests running on bhyve (https://github.com/ansible/ansible/issues/73167)
- find module - Stop traversing directories past the requested depth. (https://github.com/ansible/ansible/issues/73627)
- git - Only pass ``--raw`` flag to git verify commands (verify-tag, verify-commit) when ``gpg_whitelist`` is in use. Otherwise don't pass it so that non-whitelist GPG validation still works on older Git versions. (https://github.com/ansible/ansible/issues/64469)
- hostname - add Almalinux support (https://github.com/ansible/ansible/pull/73619)
- import_playbook - change warning about extra parameters to deprecation (https://github.com/ansible/ansible/issues/72745)
- pause - do not warn when running in the background if a timeout is provided (https://github.com/ansible/ansible/issues/73042)
- psrp connection plugin - ``to_text(stdout)`` before ``json.loads`` in psrp.Connection.put_file in case ``stdout`` is bytes.
- runtime routing - redirect ``firewalld`` to ``ansible.posix.firewalld`` FQCN (https://github.com/ansible/ansible/issues/73689).
- the unvault lookup plugin returned a byte string. Now returns a real string.
- validate-modules - do not raise an ``AttributeError`` if a value is assigned to a module attribute in a try/except block.
- yamllint - do not raise an ``AttributeError`` if a value is assigned to a module attribute at the top of the module.

ansible.utils
~~~~~~~~~~~~~

- Fix cli_parse template_path read error (https://github.com/ansible-collections/ansible.utils/pull/51).
- Fix jsonschema input data format checking (https://github.com/ansible-collections/ansible.utils/pull/50).

community.crypto
~~~~~~~~~~~~~~~~

- action_module plugin helper - make compatible with latest changes in ansible-core 2.11.0b3 (https://github.com/ansible-collections/community.crypto/pull/202).
- openssl_privatekey_pipe - make compatible with latest changes in ansible-core 2.11.0b3 (https://github.com/ansible-collections/community.crypto/pull/202).

community.docker
~~~~~~~~~~~~~~~~

- ``docker_swarm_service`` - fix KeyError on caused by reference to deprecated option ``update_failure_action`` (https://github.com/ansible-collections/community.docker/pull/100).
- docker_swarm_service - mark ``secrets`` module option with ``no_log=False`` since it does not leak secrets (https://github.com/ansible-collections/community.general/pull/2001).

community.general
~~~~~~~~~~~~~~~~~

- Mark various module options with ``no_log=False`` which have a name that potentially could leak secrets, but which do not (https://github.com/ansible-collections/community.general/pull/2001).
- git_config - fixed scope ``file`` behaviour and added integraton test for it (https://github.com/ansible-collections/community.general/issues/2117).
- module_helper module utils - actually ignoring formatting of parameters with value ``None`` (https://github.com/ansible-collections/community.general/pull/2024).
- module_helper module utils - handling ``ModuleHelperException`` now properly calls ``fail_json()`` (https://github.com/ansible-collections/community.general/pull/2024).
- module_helper module utils - use the command name as-is in ``CmdMixin`` if it fails ``get_bin_path()`` - allowing full path names to be passed (https://github.com/ansible-collections/community.general/pull/2024).
- nios* modules - fix modules to work with ansible-core 2.11 (https://github.com/ansible-collections/community.general/pull/2057).
- proxmox - removed requirement that root password is provided when containter state is ``present`` (https://github.com/ansible-collections/community.general/pull/1999).
- proxmox inventory - exclude qemu templates from inclusion to the inventory via pools (https://github.com/ansible-collections/community.general/issues/1986, https://github.com/ansible-collections/community.general/pull/1991).
- proxmox inventory plugin - allowed proxomox tag string to contain commas when returned as fact (https://github.com/ansible-collections/community.general/pull/1949).
- redfish_config module, redfish_utils module utils - fix IndexError in ``SetManagerNic`` command (https://github.com/ansible-collections/community.general/issues/1692).
- scaleway inventory plugin - fix pagination on scaleway inventory plugin (https://github.com/ansible-collections/community.general/pull/2036).
- stacki_host - replaced ``default`` to environment variables with ``fallback`` to them (https://github.com/ansible-collections/community.general/pull/2072).
- zypper, zypper_repository - respect ``PATH`` environment variable when resolving zypper executable path (https://github.com/ansible-collections/community.general/pull/2094).

community.hashi_vault
~~~~~~~~~~~~~~~~~~~~~

- hashi_vault - userpass authentication did not work with hvac 0.9.6 or higher (https://github.com/ansible-collections/community.hashi_vault/pull/68).

community.network
~~~~~~~~~~~~~~~~~

- nclu - fix ``net pending`` delimiter string (https://github.com/ansible-collections/community.network/pull/219).

community.sops
~~~~~~~~~~~~~~

- action_module plugin helper - make compatible with latest changes in ansible-core 2.11.0b3 (https://github.com/ansible-collections/community.sops/pull/58).
- community.sops.load_vars - make compatible with latest changes in ansible-core 2.11.0b3 (https://github.com/ansible-collections/community.sops/pull/58).

community.zabbix
~~~~~~~~~~~~~~~~

- zabbix_action - now properly filters discovery rule checks by name (https://github.com/ansible-collections/community.zabbix/pull/349).
- zabbix_agent - corrected version for Windows agents (https://github.com/ansible-collections/community.zabbix/pull/316).
- zabbix_agent - fixed download URL for MacOS (https://github.com/ansible-collections/community.zabbix/pull/325).
- zabbix_server - now installs correct MySQL client packages on RHEL8 systems (https://github.com/ansible-collections/community.zabbix/pull/343).
- zabbix_template - fixed an issue with Python2 where module wouldn't decode Unicode characters (https://github.com/ansible-collections/community.zabbix/pull/322).
- zabbix_web - fixed installation of python3-libsemanage package RHEL7 and older systems (https://github.com/ansible-collections/community.zabbix/pull/330).
- zabbix_web - role should now correctly determine naming of PHP packages on older systems (https://github.com/ansible-collections/community.zabbix/pull/344).
- zabbix_web - updated default PHP version for Debian10 (https://github.com/ansible-collections/community.zabbix/pull/323).

hetzner.hcloud
~~~~~~~~~~~~~~

- hcloud_server - fix a crash related to check mode if ``state=started`` or ``state=stopped`` (https://github.com/ansible-collections/hetzner.hcloud/issues/54).

ovirt.ovirt
~~~~~~~~~~~

- Set ``auth`` options into argument spec definition so Ansible will validate the user options
- Set ``no_log`` on ``password`` and ``token`` in the ``auth`` dict so the values are exposed in the invocation log
- hosted_engine_setup - Fix auth revoke (https://github.com/oVirt/ovirt-ansible-collection/pull/237).

purestorage.flasharray
~~~~~~~~~~~~~~~~~~~~~~

- purefa_info - Fix missing protection group snapshot info for local snapshots
- purefa_info - Resolve crash when an offload target is offline
- purefa_pgsnap - Ensure suffix rules only implemented for state=present
- purefa_user - Do not allow role changed for breakglass user (pureuser)
- purefa_user - Do not change role for existing user unless requested

purestorage.flashblade
~~~~~~~~~~~~~~~~~~~~~~

- purefb_* - Return a correct value for `changed` in all modules when in check mode
- purefb_dns - Deprecate search paramerter
- purefb_dsrole - Resolve idempotency issue
- purefb_lifecycle - Fix error when creating new bucket lifecycle rule.
- purefb_policy - Ensure undeclared variables are set correctly
- purefb_s3user - Fix maximum access_key count logic

Known Issues
------------

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- idrac_user - Issue(192043) Module may error out with the message ``unable to perform the import or export operation because there are pending attribute changes or a configuration job is in progress``. Wait for the job to complete and run the task again.
- ome_configuration_compliance_info - Issue(195592) Module may error out with the message ``unable to process the request because an error occurred``. If the issue persists, report it to the system administrator.
- ome_smart_fabric - Issue(185322) Only three design types are supported by OpenManage Enterprise Modular but the module successfully creates a fabric when the design type is not supported.
- ome_smart_fabric_uplink - Issue(186024) ome_smart_fabric_uplink module does not allow the creation of multiple uplinks of the same name even though this is supported by OpenManage Enterprise Modular. If an uplink is created using the same name as an existing uplink, the existing uplink is modified.

New Plugins
-----------

Become
~~~~~~

- community.general.sudosu - Run tasks using sudo su -

Callback
~~~~~~~~

- community.general.loganalytics - Posts task results to Azure Log Analytics

Filter
~~~~~~

- community.general.from_csv - Converts CSV text input into list of dicts

New Modules
-----------

community.general
~~~~~~~~~~~~~~~~~

Cloud
^^^^^

Opennebula
..........

- community.general.one_template - Manages OpenNebula templates

Net Tools
^^^^^^^^^

- community.general.gandi_livedns - Manage Gandi LiveDNS records

Pritunl
.......

- community.general.pritunl_user - Manage Pritunl Users using the Pritunl API
- community.general.pritunl_user_info - List Pritunl Users using the Pritunl API

Remote Management
^^^^^^^^^^^^^^^^^

Lenovoxcc
.........

- community.general.xcc_redfish_command - Manages Lenovo Out-Of-Band controllers using Redfish APIs

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- dellemc.openmanage.ome_configuration_compliance_baseline - Create, modify, delete and remediate a compliance configuration baseline on OpenManage Enterprise
- dellemc.openmanage.ome_configuration_compliance_info - Device compliance report for devices managed in OpenManage Enterprise

hetzner.hcloud
~~~~~~~~~~~~~~

- hetzner.hcloud.hcloud_firewall - Manage Hetzner Cloud Firewalls

purestorage.flasharray
~~~~~~~~~~~~~~~~~~~~~~

- purestorage.flasharray.purefa_maintenance - Configure Pure Storage FlashArray Maintence Windows

Unchanged Collections
---------------------

- amazon.aws (still version 1.4.1)
- ansible.netcommon (still version 1.5.0)
- ansible.posix (still version 1.2.0)
- ansible.windows (still version 1.4.0)
- arista.eos (still version 1.3.0)
- awx.awx (still version 17.1.0)
- azure.azcollection (still version 1.4.0)
- check_point.mgmt (still version 2.0.0)
- chocolatey.chocolatey (still version 1.0.2)
- cisco.aci (still version 2.0.0)
- cisco.asa (still version 1.0.4)
- cisco.ios (still version 1.3.0)
- cisco.iosxr (still version 1.2.1)
- cisco.meraki (still version 2.2.1)
- cisco.mso (still version 1.1.0)
- cisco.nso (still version 1.0.3)
- cisco.nxos (still version 1.4.0)
- cisco.ucs (still version 1.6.0)
- cloudscale_ch.cloud (still version 2.1.0)
- community.aws (still version 1.4.0)
- community.azure (still version 1.0.0)
- community.digitalocean (still version 1.0.0)
- community.fortios (still version 1.0.0)
- community.google (still version 1.0.0)
- community.grafana (still version 1.2.0)
- community.hrobot (still version 1.1.1)
- community.kubernetes (still version 1.2.0)
- community.kubevirt (still version 1.0.0)
- community.libvirt (still version 1.0.1)
- community.mongodb (still version 1.2.1)
- community.mysql (still version 1.3.0)
- community.okd (still version 1.1.0)
- community.proxysql (still version 1.0.0)
- community.rabbitmq (still version 1.0.3)
- community.routeros (still version 1.1.0)
- community.skydive (still version 1.0.0)
- community.vmware (still version 1.8.0)
- community.windows (still version 1.3.0)
- containers.podman (still version 1.4.4)
- cyberark.conjur (still version 1.1.0)
- dellemc.os10 (still version 1.1.1)
- dellemc.os6 (still version 1.0.7)
- dellemc.os9 (still version 1.0.4)
- f5networks.f5_modules (still version 1.8.1)
- fortinet.fortimanager (still version 2.0.1)
- fortinet.fortios (still version 1.1.9)
- frr.frr (still version 1.0.3)
- gluster.gluster (still version 1.0.1)
- google.cloud (still version 1.0.2)
- ibm.qradar (still version 1.0.3)
- infinidat.infinibox (still version 1.2.4)
- inspur.sm (still version 1.1.2)
- junipernetworks.junos (still version 1.3.0)
- kubernetes.core (still version 1.2.0)
- mellanox.onyx (still version 1.0.0)
- netapp.aws (still version 20.9.0)
- netapp.elementsw (still version 20.11.0)
- netapp.ontap (still version 21.3.1)
- netapp_eseries.santricity (still version 1.1.0)
- netbox.netbox (still version 2.1.0)
- ngine_io.cloudstack (still version 2.0.0)
- ngine_io.exoscale (still version 1.0.0)
- ngine_io.vultr (still version 1.1.0)
- openstack.cloud (still version 1.3.0)
- openvswitch.openvswitch (still version 1.2.0)
- servicenow.servicenow (still version 1.0.4)
- splunk.es (still version 1.0.2)
- theforeman.foreman (still version 1.5.1)
- vyos.vyos (still version 1.1.1)
- wti.remote (still version 1.0.1)

v3.1.0
======

.. contents::
  :local:
  :depth: 2

Release Summary
---------------

Release Date: 2021-03-10

`Porting Guide <https://docs.ansible.com/ansible/devel/porting_guides.html>`_

Ansible-base
------------

Ansible 3.1.0 contains Ansible-base version 2.10.5.
This is the same version of Ansible-base as in the previous Ansible release.


Changed Collections
-------------------

If not mentioned explicitly, the changes are reported in the combined changelog below.

+-------------------------------+---------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Collection                    | Ansible 3.0.0 | Ansible 3.1.0 | Notes                                                                                                                                                                                                                                      |
+===============================+===============+===============+============================================================================================================================================================================================================================================+
| amazon.aws                    | 1.3.0         | 1.4.1         |                                                                                                                                                                                                                                            |
+-------------------------------+---------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ansible.posix                 | 1.1.1         | 1.2.0         |                                                                                                                                                                                                                                            |
+-------------------------------+---------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ansible.utils                 | 2.0.0         | 2.0.1         |                                                                                                                                                                                                                                            |
+-------------------------------+---------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ansible.windows               | 1.3.0         | 1.4.0         |                                                                                                                                                                                                                                            |
+-------------------------------+---------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| awx.awx                       | 17.0.1        | 17.1.0        | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.                                                                                                               |
+-------------------------------+---------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cisco.intersight              | 1.0.10        | 1.0.11        | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.                                                                                                               |
+-------------------------------+---------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cisco.meraki                  | 2.2.0         | 2.2.1         |                                                                                                                                                                                                                                            |
+-------------------------------+---------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cloudscale_ch.cloud           | 2.0.0         | 2.1.0         |                                                                                                                                                                                                                                            |
+-------------------------------+---------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.aws                 | 1.3.0         | 1.4.0         |                                                                                                                                                                                                                                            |
+-------------------------------+---------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.crypto              | 1.4.0         | 1.5.0         |                                                                                                                                                                                                                                            |
+-------------------------------+---------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.docker              | 1.2.2         | 1.3.0         |                                                                                                                                                                                                                                            |
+-------------------------------+---------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.general             | 2.0.1         | 2.2.0         |                                                                                                                                                                                                                                            |
+-------------------------------+---------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.grafana             | 1.1.0         | 1.2.0         |                                                                                                                                                                                                                                            |
+-------------------------------+---------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.hashi_vault         | 1.0.0         | 1.1.2         |                                                                                                                                                                                                                                            |
+-------------------------------+---------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.hrobot              | 1.1.0         | 1.1.1         |                                                                                                                                                                                                                                            |
+-------------------------------+---------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.kubernetes          | 1.1.1         | 1.2.0         |                                                                                                                                                                                                                                            |
+-------------------------------+---------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.libvirt             | 1.0.0         | 1.0.1         |                                                                                                                                                                                                                                            |
+-------------------------------+---------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.mongodb             | 1.2.0         | 1.2.1         | The collection did not have a changelog in this version.                                                                                                                                                                                   |
+-------------------------------+---------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.mysql               | 1.2.0         | 1.3.0         |                                                                                                                                                                                                                                            |
+-------------------------------+---------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.okd                 | 1.0.1         | 1.1.0         |                                                                                                                                                                                                                                            |
+-------------------------------+---------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.rabbitmq            | 1.0.1         | 1.0.3         | The collection did not have a changelog in this version.                                                                                                                                                                                   |
+-------------------------------+---------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.sops                | 1.0.4         | 1.0.5         |                                                                                                                                                                                                                                            |
+-------------------------------+---------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.vmware              | 1.7.0         | 1.8.0         |                                                                                                                                                                                                                                            |
+-------------------------------+---------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.windows             | 1.2.0         | 1.3.0         |                                                                                                                                                                                                                                            |
+-------------------------------+---------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| containers.podman             | 1.4.1         | 1.4.4         |                                                                                                                                                                                                                                            |
+-------------------------------+---------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| dellemc.openmanage            | 3.0.0         | 3.1.0         |                                                                                                                                                                                                                                            |
+-------------------------------+---------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| dellemc.os6                   | 1.0.6         | 1.0.7         | There are no changes recorded in the changelog.                                                                                                                                                                                            |
+-------------------------------+---------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| dellemc.os9                   | 1.0.3         | 1.0.4         |                                                                                                                                                                                                                                            |
+-------------------------------+---------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| f5networks.f5_modules         | 1.7.1         | 1.8.1         |                                                                                                                                                                                                                                            |
+-------------------------------+---------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| fortinet.fortios              | 1.1.8         | 1.1.9         | The collection did not have a changelog in this version.                                                                                                                                                                                   |
+-------------------------------+---------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| kubernetes.core               | 1.1.1         | 1.2.0         |                                                                                                                                                                                                                                            |
+-------------------------------+---------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| netapp.ontap                  | 21.1.1        | 21.3.1        |                                                                                                                                                                                                                                            |
+-------------------------------+---------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| netbox.netbox                 | 2.0.0         | 2.1.0         |                                                                                                                                                                                                                                            |
+-------------------------------+---------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| openstack.cloud               | 1.2.1         | 1.3.0         | The collection did not have a changelog in this version.                                                                                                                                                                                   |
+-------------------------------+---------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| openvswitch.openvswitch       | 1.1.0         | 1.2.0         |                                                                                                                                                                                                                                            |
+-------------------------------+---------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ovirt.ovirt                   | 1.3.0         | 1.3.1         |                                                                                                                                                                                                                                            |
+-------------------------------+---------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| purestorage.flasharray        | 1.5.1         | 1.6.2         |                                                                                                                                                                                                                                            |
+-------------------------------+---------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| sensu.sensu_go                | 1.8.0         | 1.9.1         |                                                                                                                                                                                                                                            |
+-------------------------------+---------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| t_systems_mms.icinga_director | 1.13.0        | 1.15.0        | You can find the collection's changelog at `https://github.com/T-Systems-MMS/ansible-collection-icinga-director/blob/master/CHANGELOG.md <https://github.com/T-Systems-MMS/ansible-collection-icinga-director/blob/master/CHANGELOG.md>`_. |
+-------------------------------+---------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Major Changes
-------------

community.grafana
~~~~~~~~~~~~~~~~~

- introduce "skip_version_check" parameter in grafana_teams and grafana_folder modules (#147)

community.mysql
~~~~~~~~~~~~~~~

- mysql_replication - the mode options values ``getslave``, ``startslave``, ``stopslave``, ``resetslave``, ``resetslaveall` and the master_use_gtid option ``slave_pos`` are deprecated (see the alternative values) and will be removed in ``community.mysql`` 3.0.0 (https://github.com/ansible-collections/community.mysql/pull/97).
- mysql_replication - the word ``SLAVE`` in messages returned by the module will be changed to ``REPLICA`` in ``community.mysql`` 2.0.0 (https://github.com/ansible-collections/community.mysql/issues/98).

Minor Changes
-------------

amazon.aws
~~~~~~~~~~

- aws_ec2 - Add hostname options concatenation
- aws_ec2 inventory plugin - avoid a superfluous import of ``ansible.utils.display.Display`` (https://github.com/ansible-collections/amazon.aws/pull/226).
- aws_ec2 module - Replace inverse aws instance-state-name filters !terminated, !shutting-down in favor of postive filters pending, running, stopping, stopped. Issue 235. (https://github.com/ansible-collections/amazon.aws/pull/237)
- aws_secret - add ``bypath`` functionality (https://github.com/ansible-collections/amazon.aws/pull/192).
- ec2_key - add AWSRetry decorator to automatically retry on common temporary failures (https://github.com/ansible-collections/amazon.aws/pull/213).
- ec2_vol - Add support for gp3 volumes and support for modifying existing volumes (https://github.com/ansible-collections/amazon.aws/issues/55).
- module_utils - the ipaddress module utility has been vendored into this collection.  This eliminates the collection dependency on ansible.netcommon (which had removed the library in its 2.0 release).  The ipaddress library is provided for internal use in this collection only. (https://github.com/ansible-collections/amazon.aws/issues/273)-
- module_utils/elbv2 - add logic to compare_rules to suit Values list nested within dicts unique to each field type. Fixes issue (https://github.com/ansible-collections/amazon.aws/issues/187)
- various AWS plugins and module_utils - Cleanup unused imports (https://github.com/ansible-collections/amazon.aws/pull/217).

ansible.posix
~~~~~~~~~~~~~

- firewalld - bring the ``target`` feature back (https://github.com/ansible-collections/ansible.posix/issues/112).
- fix sanity test for various modules.
- synchronize - add the ``ssh_connection_multiplexing`` option to allow SSH connection multiplexing (https://github.com/ansible/ansible/issues/24365).

ansible.windows
~~~~~~~~~~~~~~~

- setup - Added more virtualization types to the virtual facts based on the Linux setup module

cloudscale_ch.cloud
~~~~~~~~~~~~~~~~~~~

- Add interface parameter to server module (https://github.com/cloudscale-ch/ansible-collection-cloudscale/pull/54).
- Rename server_uuids parameter to servers in volume module (https://github.com/cloudscale-ch/ansible-collection-cloudscale/pull/54).

community.aws
~~~~~~~~~~~~~

- aws_kms - add support for setting the deletion window using `pending_window` (PendingWindowInDays) (https://github.com/ansible-collections/community.aws/pull/200).
- aws_kms_info - Add ``key_id`` and ``alias`` parameters to support fetching a single key (https://github.com/ansible-collections/community.aws/pull/200).
- dynamodb_ttl - use ``botocore_at_least`` helper for checking the available botocore version (https://github.com/ansible-collections/community.aws/pull/280).
- ec2_instance - add automatic retries on all paginated queries for temporary errors (https://github.com/ansible-collections/community.aws/pull/373).
- ec2_instance - migrate to shared implementation of get_ec2_security_group_ids_from_names. The module will now return an error if the subnet provided isn't in the requested VPC. (https://github.com/ansible-collections/community.aws/pull/214)
- ec2_instance_info - added ``minimum_uptime`` option with alias ``uptime`` for filtering instances that have only been online for certain duration of time in minutes (https://github.com/ansible-collections/community.aws/pull/356).
- ec2_launch_template - Add retries on common AWS failures (https://github.com/ansible-collections/community.aws/pull/326).
- ec2_vpc_peer - use ``botocore_at_least`` helper for checking the available botocore version (https://github.com/ansible-collections/community.aws/pull/280).
- ecs_task - use ``botocore_at_least`` helper for checking the available botocore version (https://github.com/ansible-collections/community.aws/pull/280).
- route53 - migrated from boto to boto3 (https://github.com/ansible-collections/community.aws/pull/405).
- various community.aws modules - cleanup error handling to use ``is_boto3_error_code`` and ``is_boto3_error_message`` helpers (https://github.com/ansible-collections/community.aws/pull/268).
- various community.aws modules - cleanup of Python imports (https://github.com/ansible-collections/community.aws/pull/360).
- various community.aws modules - improve consistency of handling Boto3 exceptions (https://github.com/ansible-collections/community.aws/pull/268).
- various community.aws modules - migrate exception error message handling from fail_json to fail_json_aws (https://github.com/ansible-collections/community.aws/pull/361).

community.crypto
~~~~~~~~~~~~~~~~

- acme_account_info - when ``retrieve_orders`` is not ``ignore`` and the ACME server allows to query orders, the new return value ``order_uris`` is always populated with a list of URIs (https://github.com/ansible-collections/community.crypto/pull/178).
- luks_device - allow to specify sector size for LUKS2 containers with new ``sector_size`` parameter (https://github.com/ansible-collections/community.crypto/pull/193).

community.docker
~~~~~~~~~~~~~~~~

- docker_container - add ``storage_opts`` option to specify storage options (https://github.com/ansible-collections/community.docker/issues/91, https://github.com/ansible-collections/community.docker/pull/93).
- docker_image - allows to specify platform to pull for ``source=pull`` with new option ``pull_platform`` (https://github.com/ansible-collections/community.docker/issues/79, https://github.com/ansible-collections/community.docker/pull/89).
- docker_image - properly support image IDs (hashes) for loading and tagging images (https://github.com/ansible-collections/community.docker/issues/86, https://github.com/ansible-collections/community.docker/pull/87).
- docker_swarm_service - adding support for maximum number of tasks per node (``replicas_max_per_node``) when running swarm service in replicated mode. Introduced in API 1.40 (https://github.com/ansible-collections/community.docker/issues/7, https://github.com/ansible-collections/community.docker/pull/92).

community.general
~~~~~~~~~~~~~~~~~

- bundler - elements of list parameters are now validated (https://github.com/ansible-collections/community.general/pull/1885).
- clc_* modules - elements of list parameters are now validated (https://github.com/ansible-collections/community.general/pull/1771).
- consul - elements of list parameters are now validated (https://github.com/ansible-collections/community.general/pull/1885).
- consul_acl - elements of list parameters are now validated (https://github.com/ansible-collections/community.general/pull/1885).
- consul_io inventory script - conf options - allow custom configuration options via env variables (https://github.com/ansible-collections/community.general/pull/620).
- consul_session - elements of list parameters are now validated (https://github.com/ansible-collections/community.general/pull/1885).
- datadog_monitor - add missing monitor types ``query alert``, ``trace-analytics alert``, ``rum alert`` (https://github.com/ansible-collections/community.general/pull/1723).
- datadog_monitor - elements of list parameters are now validated (https://github.com/ansible-collections/community.general/pull/1885).
- dnsimple - add CAA records to the whitelist of valid record types (https://github.com/ansible-collections/community.general/pull/1814).
- dnsimple - elements of list parameters ``record_ids`` are now validated (https://github.com/ansible-collections/community.general/pull/1795).
- gitlab_runner - elements of list parameters ``tag_list`` are now validated (https://github.com/ansible-collections/community.general/pull/1795).
- grove - the option ``message`` has been renamed to ``message_content``. The old name ``message`` is kept as an alias and will be removed for community.general 4.0.0. This was done because ``message`` is used internally by Ansible (https://github.com/ansible-collections/community.general/pull/1929).
- heroku_collaborator - elements of list parameters are now validated (https://github.com/ansible-collections/community.general/pull/1970).
- homebrew_tap - add support to specify search path for ``brew`` executable (https://github.com/ansible-collections/community.general/issues/1702).
- keycloak_client - elements of list parameters ``default_roles``, ``redirect_uris``, ``web_origins`` are now validated (https://github.com/ansible-collections/community.general/pull/1795).
- librato_annotation - elements of list parameters ``links`` are now validated (https://github.com/ansible-collections/community.general/pull/1795).
- linode_v4 - elements of list parameters are now validated (https://github.com/ansible-collections/community.general/pull/1970).
- lxd_container - ``client_key`` and ``client_cert`` are now of type ``path`` and no longer ``str``. A side effect is that certain expansions are made, like ``~`` is replaced by the user's home directory, and environment variables like ``$HOME`` or ``$TEMP`` are evaluated (https://github.com/ansible-collections/community.general/pull/1741).
- lxd_container - elements of list parameter ``profiles`` are now validated (https://github.com/ansible-collections/community.general/pull/1795).
- lxd_profile - ``client_key`` and ``client_cert`` are now of type ``path`` and no longer ``str``. A side effect is that certain expansions are made, like ``~`` is replaced by the user's home directory, and environment variables like ``$HOME`` or ``$TEMP`` are evaluated (https://github.com/ansible-collections/community.general/pull/1741).
- lxd_profile - added ``merge_profile`` parameter to merge configurations from the play to an existing profile (https://github.com/ansible-collections/community.general/pull/1813).
- mail - elements of list parameters ``to``, ``cc``, ``bcc``, ``attach``, ``headers`` are now validated (https://github.com/ansible-collections/community.general/pull/1795).
- manageiq_alert_profiles - elements of list parameters are now validated (https://github.com/ansible-collections/community.general/pull/1970).
- manageiq_policies - elements of list parameters are now validated (https://github.com/ansible-collections/community.general/pull/1970).
- manageiq_tags - elements of list parameters are now validated (https://github.com/ansible-collections/community.general/pull/1970).
- manageiq_tags and manageiq_policies - added new parameter ``resource_id``. This parameter can be used instead of parameter ``resource_name`` (https://github.com/ansible-collections/community.general/pull/719).
- module_helper module utils - ``CmdMixin.run_command()`` now accepts ``dict`` command arguments, providing the parameter and its value (https://github.com/ansible-collections/community.general/pull/1867).
- na_ontap_gather_facts - elements of list parameters ``gather_subset`` are now validated (https://github.com/ansible-collections/community.general/pull/1795).
- nexmo - elements of list parameters ``dest`` are now validated (https://github.com/ansible-collections/community.general/pull/1795).
- nsupdate - elements of list parameters ``value`` are now validated (https://github.com/ansible-collections/community.general/pull/1795).
- oci_vcn - ``api_user_key_file`` is now of type ``path`` and no longer ``str``. A side effect is that certain expansions are made, like ``~`` is replaced by the user's home directory, and environment variables like ``$HOME`` or ``$TEMP`` are evaluated (https://github.com/ansible-collections/community.general/pull/1741).
- omapi_host - elements of list parameters ``statements`` are now validated (https://github.com/ansible-collections/community.general/pull/1795).
- one_host - elements of list parameters are now validated (https://github.com/ansible-collections/community.general/pull/1970).
- one_image_info - elements of list parameters are now validated (https://github.com/ansible-collections/community.general/pull/1970).
- one_vm - elements of list parameters are now validated (https://github.com/ansible-collections/community.general/pull/1970).
- oneandone_firewall_policy - elements of list parameters are now validated (https://github.com/ansible-collections/community.general/pull/1885).
- oneandone_load_balancer - elements of list parameters are now validated (https://github.com/ansible-collections/community.general/pull/1885).
- oneandone_monitoring_policy - elements of list parameters are now validated (https://github.com/ansible-collections/community.general/pull/1885).
- oneandone_private_network - elements of list parameters are now validated (https://github.com/ansible-collections/community.general/pull/1885).
- oneandone_server - elements of list parameters are now validated (https://github.com/ansible-collections/community.general/pull/1885).
- onepassword_info - elements of list parameters ``search_terms`` are now validated (https://github.com/ansible-collections/community.general/pull/1795).
- oneview_datacenter_info - elements of list parameters are now validated (https://github.com/ansible-collections/community.general/pull/1970).
- oneview_enclosure_info - elements of list parameters are now validated (https://github.com/ansible-collections/community.general/pull/1970).
- oneview_ethernet_network_info - elements of list parameters are now validated (https://github.com/ansible-collections/community.general/pull/1970).
- oneview_network_set_info - elements of list parameters are now validated (https://github.com/ansible-collections/community.general/pull/1970).
- packet_device - elements of list parameters ``device_ids``, ``hostnames`` are now validated (https://github.com/ansible-collections/community.general/pull/1795).
- pagerduty - elements of list parameters ``service`` are now validated (https://github.com/ansible-collections/community.general/pull/1795).
- plugins/module_utils/oracle/oci_utils.py - elements of list parameter ``key_by`` are now validated (https://github.com/ansible-collections/community.general/pull/1795).
- profitbricks - elements of list parameters are now validated (https://github.com/ansible-collections/community.general/pull/1885).
- profitbricks_volume - elements of list parameters are now validated (https://github.com/ansible-collections/community.general/pull/1885).
- proxmox_kvm module - actually implemented ``vmid`` and ``status`` return values. Updated documentation to reflect current situation (https://github.com/ansible-collections/community.general/issues/1410, https://github.com/ansible-collections/community.general/pull/1715).
- pubnub_blocks - elements of list parameters ``event_handlers`` are now validated (https://github.com/ansible-collections/community.general/pull/1795).
- redfish modules - explicitly setting lists' elements to ``str`` (https://github.com/ansible-collections/community.general/pull/1761).
- redfish_config - case insensitive search for situations where the hostname/FQDN case on iLO doesn't match variable's case (https://github.com/ansible-collections/community.general/pull/1744).
- redhat_subscription - elements of list parameters ``pool_ids``, ``addons`` are now validated (https://github.com/ansible-collections/community.general/pull/1795).
- rocketchat - elements of list parameters ``attachments`` are now validated (https://github.com/ansible-collections/community.general/pull/1795).
- scaleway_compute - elements of list parameters are now validated (https://github.com/ansible-collections/community.general/pull/1970).
- scaleway_lb - elements of list parameters are now validated (https://github.com/ansible-collections/community.general/pull/1970).
- sendgrid - elements of list parameters ``to_addresses``, ``cc``, ``bcc``, ``attachments`` are now validated (https://github.com/ansible-collections/community.general/pull/1795).
- sensu_check - elements of list parameters are now validated (https://github.com/ansible-collections/community.general/pull/1885).
- sensu_client - elements of list parameters are now validated (https://github.com/ansible-collections/community.general/pull/1885).
- sensu_handler - elements of list parameters are now validated (https://github.com/ansible-collections/community.general/pull/1885).
- sl_vm - elements of list parameters ``disks``, ``ssh_keys`` are now validated (https://github.com/ansible-collections/community.general/pull/1795).
- slack - elements of list parameters ``attachments`` are now validated (https://github.com/ansible-collections/community.general/pull/1795).
- statusio_maintenance - elements of list parameters ``components``, ``containers`` are now validated (https://github.com/ansible-collections/community.general/pull/1795).
- timezone - add Gentoo and Alpine Linux support (https://github.com/ansible-collections/community.general/issues/781).
- twilio - elements of list parameters ``to_numbers`` are now validated (https://github.com/ansible-collections/community.general/pull/1795).
- vmadm - elements of list parameters ``disks``, ``nics``, ``resolvers``, ``filesystems`` are now validated (https://github.com/ansible-collections/community.general/pull/1795).
- webfaction_domain - elements of list parameters are now validated (https://github.com/ansible-collections/community.general/pull/1885).
- webfaction_site - elements of list parameters are now validated (https://github.com/ansible-collections/community.general/pull/1885).
- xfconf - added option ``disable_facts`` to disable facts and its associated deprecation warning (https://github.com/ansible-collections/community.general/issues/1475).
- xml - elements of list parameters ``add_children``, ``set_children`` are now validated (https://github.com/ansible-collections/community.general/pull/1795).
- yum_versionlock - Do the lock/unlock concurrently to speed up (https://github.com/ansible-collections/community.general/pull/1912).

community.hashi_vault
~~~~~~~~~~~~~~~~~~~~~

- hashi_vault - add ``proxies`` option (https://github.com/ansible-collections/community.hashi_vault/pull/50).

community.kubernetes
~~~~~~~~~~~~~~~~~~~~

- Adjust the documentation to clarify the fact ``wait_condition.status`` is a string.
- Adjust the name of parameters of ``helm`` and ``helm_info`` to match the documentation. No playbook change required.
- The Helm modules (``helm``, ``helm_info``, ``helm_plugin``, ``helm_plugin_info``, ``helm_plugin_repository``) accept the K8S environment variables like the other modules of the collections.
- helm - add a ``skip_crds`` option to skip the installation of CRDs when installing or upgrading a chart (https://github.com/ansible-collections/community.kubernetes/issues/296).
- helm - add optional support for helm diff (https://github.com/ansible-collections/community.kubernetes/issues/248).
- helm_template - add helm_template module to support template functionality (https://github.com/ansible-collections/community.kubernetes/issues/367).
- k8s - add a ``delete_options`` parameter to control garbage collection behavior when deleting a resource (https://github.com/ansible-collections/community.kubernetes/issues/253).
- k8s - add an example for downloading manifest file and applying (https://github.com/ansible-collections/community.kubernetes/issues/352).
- k8s - check if kubeconfig file is located on remote node or on Ansible Controller (https://github.com/ansible-collections/community.kubernetes/issues/307).
- k8s - check if src file is located on remote node or on Ansible Controller (https://github.com/ansible-collections/community.kubernetes/issues/307).
- k8s_exec - add a note about required permissions for the module (https://github.com/ansible-collections/community.kubernetes/issues/339).
- k8s_info - add information about api_version while returning facts (https://github.com/ansible-collections/community.kubernetes/pull/308).
- runtime.yml - update minimum Ansible version required for Kubernetes collection (https://github.com/ansible-collections/community.kubernetes/issues/314).

community.mysql
~~~~~~~~~~~~~~~

- mysql_replication - deprecate offending terminology, add alternative choices to the ``mode`` option (https://github.com/ansible-collections/community.mysql/issues/78).

community.okd
~~~~~~~~~~~~~

- increase the kubernetes.core dependency version number (https://github.com/ansible-collections/community.okd/pull/71).
- restrict the version of kubernetes.core dependency (https://github.com/ansible-collections/community.okd/pull/66).

community.vmware
~~~~~~~~~~~~~~~~

- Define sub-options of disk in argument_spec (https://github.com/ansible-collections/community.vmware/pull/640).
- vmware_guest - Remove unnecessary hardware version check (https://github.com/ansible-collections/community.vmware/issues/636).
- vmware_vcenter_settings - supported the diff mode (https://github.com/ansible-collections/community.vmware/pull/641).

community.windows
~~~~~~~~~~~~~~~~~

- Extend win_domain_computer adding managedBy parameter.

f5networks.f5_modules
~~~~~~~~~~~~~~~~~~~~~

- Add disable action and appropriate scenarios to bigip_policy_rule module
- Add ends_with_any condition to bigip_policy_rule module
- Add http_header condition type with header_is_any condition to bigip_policy_rule module
- Add insert action and appropriate scenarios to bigip_policy_rule module
- Add path_contains condition to bigip_policy_rule module
- Add path_is_any option to conditions in bigip_policy_rule module
- Add remove action and appropriate scenarios to bigip_policy_rule module
- Add replace action and appropriate scenarios to bigip_policy_rule module
- Event types are now supported with forward type action
- Event types are now supported with reset type action
- Policy support with condition type TCP match with any of address/datagroup

kubernetes.core
~~~~~~~~~~~~~~~

- Adjust the documentation to clarify the fact ``wait_condition.status`` is a string.
- Adjust the name of parameters of ``helm`` and ``helm_info`` to match the documentation. No playbook change required.
- The Helm modules (``helm``, ``helm_info``, ``helm_plugin``, ``helm_plugin_info``, ``helm_plugin_repository``) accept the K8S environment variables like the other modules of the collections.
- helm - add a ``skip_crds`` option to skip the installation of CRDs when installing or upgrading a chart (https://github.com/ansible-collections/kubernetes.core/issues/296).
- helm - add optional support for helm diff (https://github.com/ansible-collections/kubernetes.core/issues/248).
- helm_template - add helm_template module to support template functionality (https://github.com/ansible-collections/kubernetes.core/issues/367).
- k8s - add a ``delete_options`` parameter to control garbage collection behavior when deleting a resource (https://github.com/ansible-collections/kubernetes.core/issues/253).
- k8s - add an example for downloading manifest file and applying (https://github.com/ansible-collections/kubernetes.core/issues/352).
- k8s - check if kubeconfig file is located on remote node or on Ansible Controller (https://github.com/ansible-collections/kubernetes.core/issues/307).
- k8s - check if src file is located on remote node or on Ansible Controller (https://github.com/ansible-collections/kubernetes.core/issues/307).
- k8s_exec - add a note about required permissions for the module (https://github.com/ansible-collections/kubernetes.core/issues/339).
- k8s_info - add information about api_version while returning facts (https://github.com/ansible-collections/kubernetes.core/pull/308).
- runtime.yml - update minimum Ansible version required for Kubernetes collection (https://github.com/ansible-collections/kubernetes.core/issues/314).

netapp.ontap
~~~~~~~~~~~~

- azure_rm_netapp_account - new option ``active_directories`` to support SMB volumes.
- azure_rm_netapp_volume - new option ``protocol_types`` to support SMB volumes.
- na_ontap_debug - improve error reporting for import errors on netapp_lib.
- na_ontap_flexcache - mount/unmount the FlexCache volume when using REST.
- na_ontap_flexcache - support REST APIs in addition to ZAPI for create and delete.
- na_ontap_flexcache - support for ``prepopulate`` option when using REST (requires ONTAP 9.8).
- na_ontap_igroup - added REST support for ONTAP igroup creation, modification, and deletion.
- na_ontap_igroups - new option ``igroups`` to support nested igroups (requires ONTAP 9.9).
- na_ontap_info - improve error reporting for import errors on netapp_lib, json, xlmtodict.
- na_ontap_lun - add ``comment`` option.
- na_ontap_lun - convert existing LUNs and supporting volume to a smart container within a SAN application.
- na_ontap_lun - new option ``qos_adaptive_policy_group``.
- na_ontap_lun - new option ``scope`` to explicitly force operations on the SAN application or a single LUN.
- na_ontap_motd - deprecated module warning and to use na_ontap_login_messages.
- na_ontap_node - added modify function for location and asset tag for node.
- na_ontap_snapmirror - add new options ``source_endpoint`` and ``destination_endpoint`` to group endpoint suboptions.
- na_ontap_snapmirror - add new suboptions ``consistency_group_volumes`` and ``ipspace`` to endpoint options.
- na_ontap_snapmirror - deprecate older options for source and destination paths, volumes, vservers, and clusters.
- na_ontap_snapmirror - improve error reporting or warn when REST option is not supported.
- na_ontap_snapmirror - report warning when relationship is present but not healthy.
- na_ontap_volume - new suboption ``dr_cache`` when creating flexcache using NAS application template.
- na_ontap_volume_efficiency - to allow for FAS ONTAP systems to enable volume efficiency when it does not exist and apply additional parameters.
- na_ontap_volume_efficiency - to allow for FAS ONTAP systems to enable volume efficiency when it does not exist.

netbox.netbox
~~~~~~~~~~~~~

- Inventory - Added ansible_host_dns_name to set ansible_host to dns_name
- netbox_device_role - Added description option
- netbox_platform -  Added description option

openvswitch.openvswitch
~~~~~~~~~~~~~~~~~~~~~~~

- Allow setting multiple properties on a port (https://github.com/ansible-collections/openvswitch.openvswitch/issues/63).

ovirt.ovirt
~~~~~~~~~~~

- hosted_engine_setup - Disable reboot_after_installation (https://github.com/oVirt/ovirt-ansible-collection/pull/218).
- ovirt_host - Add reboot_after_installation option (https://github.com/oVirt/ovirt-ansible-collection/pull/217).

purestorage.flasharray
~~~~~~~~~~~~~~~~~~~~~~

- purefa_connect - Add support for FC-based array replication
- purefa_ds - Add Purity v6 support for Directory Services, including Data DS and updating services
- purefa_info - Add support for FC Replication
- purefa_info - Add support for Remote Volume Snapshots
- purefa_info - Update directory_services dictionary to cater for FA-Files data DS. Change DS dict forward. Add deprecation warning.
- purefa_ntp - Ignore NTP configuration for CBS-based arrays
- purefa_pg - Add support for Protection Groups in AC pods
- purefa_snap - Add support for remote snapshot of individual volumes to offload targets

sensu.sensu_go
~~~~~~~~~~~~~~

- Add modules for managing Sensu Go clusters.
- Add modules for managing etcd replicatiors, which form the basis of the Sensu Go federation.
- Update list of available Sensu Go agent packages for Windows installations.

Deprecated Features
-------------------

cloudscale_ch.cloud
~~~~~~~~~~~~~~~~~~~

- The aliases ``server_uuids`` and ``server_uuid`` of the servers parameter in the volume module will be removed in version 3.0.0.

community.aws
~~~~~~~~~~~~~

- ec2_eip - formally deprecate the ``instance_id`` alias for ``device_id`` (https://github.com/ansible-collections/community.aws/pull/349).
- ec2_vpc_endpoint - deprecate the policy_file option and recommend using policy with a lookup (https://github.com/ansible-collections/community.aws/pull/366).

community.crypto
~~~~~~~~~~~~~~~~

- acme_account_info - when ``retrieve_orders=url_list``, ``orders`` will no longer be returned in community.crypto 2.0.0. Use ``order_uris`` instead (https://github.com/ansible-collections/community.crypto/pull/178).

community.general
~~~~~~~~~~~~~~~~~

- apt_rpm - deprecated invalid parameter alias ``update-cache``, will be removed in 5.0.0 (https://github.com/ansible-collections/community.general/pull/1927).
- composer - deprecated invalid parameter aliases ``working-dir``, ``global-command``, ``prefer-source``, ``prefer-dist``, ``no-dev``, ``no-scripts``, ``no-plugins``, ``optimize-autoloader``, ``classmap-authoritative``, ``apcu-autoloader``, ``ignore-platform-reqs``, will be removed in 5.0.0 (https://github.com/ansible-collections/community.general/pull/1927).
- github_deploy_key - deprecated invalid parameter alias ``2fa_token``, will be removed in 5.0.0 (https://github.com/ansible-collections/community.general/pull/1927).
- grove - the option ``message`` will be removed in community.general 4.0.0. Use the new option ``message_content`` instead (https://github.com/ansible-collections/community.general/pull/1929).
- homebrew - deprecated invalid parameter alias ``update-brew``, will be removed in 5.0.0 (https://github.com/ansible-collections/community.general/pull/1927).
- homebrew_cask - deprecated invalid parameter alias ``update-brew``, will be removed in 5.0.0 (https://github.com/ansible-collections/community.general/pull/1927).
- opkg - deprecated invalid parameter alias ``update-cache``, will be removed in 5.0.0 (https://github.com/ansible-collections/community.general/pull/1927).
- pacman - deprecated invalid parameter alias ``update-cache``, will be removed in 5.0.0 (https://github.com/ansible-collections/community.general/pull/1927).
- puppet - deprecated undocumented parameter ``show_diff``, will be removed in 7.0.0. (https://github.com/ansible-collections/community.general/pull/1927).
- runit - unused parameter ``dist`` marked for deprecation (https://github.com/ansible-collections/community.general/pull/1830).
- slackpkg - deprecated invalid parameter alias ``update-cache``, will be removed in 5.0.0 (https://github.com/ansible-collections/community.general/pull/1927).
- urmpi - deprecated invalid parameter aliases ``update-cache`` and ``no-recommends``, will be removed in 5.0.0 (https://github.com/ansible-collections/community.general/pull/1927).
- xbps - deprecated invalid parameter alias ``update-cache``, will be removed in 5.0.0 (https://github.com/ansible-collections/community.general/pull/1927).
- xfconf - returning output as facts is deprecated, this will be removed in community.general 4.0.0. Please register the task output in a variable and use it instead. You can already switch to the new behavior now by using the new ``disable_facts`` option (https://github.com/ansible-collections/community.general/pull/1747).

Removed Features (previously deprecated)
----------------------------------------

f5networks.f5_modules
~~~~~~~~~~~~~~~~~~~~~

- Removed TMOS v11 support for bigip_gtm_pool and bigip_gtm_wide_ip modules
- Removed quorum and monitor_type parameters in bigip_node module. See porting guides section at https://clouddocs.f5.com/products/orchestration/ansible/devel/usage/porting-guides.html
- Removed syslog_settings and pool_settings parameters in bigip_log_destination moduke. See porting guides section at https://clouddocs.f5.com/products/orchestration/ansible/devel/usage/porting-guides.html

Bugfixes
--------

amazon.aws
~~~~~~~~~~

- ec2_vol - a creation or update now returns a structure with an up to date list of tags (https://github.com/ansible-collections/amazon.aws/pull/241).

ansible.posix
~~~~~~~~~~~~~

- at - add AIX support (https://github.com/ansible-collections/ansible.posix/pull/99).
- synchronize - add ``community.docker.docker`` to the list of supported transports (https://github.com/ansible-collections/ansible.posix/issues/132).
- synchronize - do not prepend PWD when path is in form user@server:path or server:path (https://github.com/ansible-collections/ansible.posix/pull/118).
- synchronize - fix for private_key overriding in synchronize module.
- sysctl - do not persist sysctl when value is invalid (https://github.com/ansible-collections/ansible.posix/pull/101).

ansible.utils
~~~~~~~~~~~~~

- Fix ansible.utils.cli_parse action plugin to support old cli_parse sub-plugin structure in ansible.netcommon collection.

ansible.windows
~~~~~~~~~~~~~~~

- win_package - fix msi detection when the msi product is already installed under a different version - https://github.com/ansible-collections/ansible.windows/issues/166
- win_package - treat a missing ``creates_path`` when ``creates_version`` as though the package was not installed instead of a failure - https://github.com/ansible-collections/ansible.windows/issues/169

cisco.meraki
~~~~~~~~~~~~

- meraki_mx_content_filtering - Fix crash with idempotent condition due to improper sorting

community.aws
~~~~~~~~~~~~~

- aws_kms - fixes issue where module execution fails without the kms:GetKeyRotationStatus permission. (https://github.com/ansible-collections/community.aws/pull/200).
- aws_kms_info - ensure that searching by tag works when tag only exists on some CMKs (https://github.com/ansible-collections/community.aws/issues/276).
- aws_s3_cors - fix element type for rules parameter. (https://github.com/ansible-collections/community.aws/pull/408).
- aws_ssm - fix the generation of CURL URL used to download Ansible Python file from S3 bucket by ```_get_url()``` due to due to non-assignment of aws region in the URL and not using V4 signature as specified for AWS S3 signature URL by ```_get_boto_client()``` in (https://github.com/ansible-collections/community.aws/pull/352).
- aws_ssm - fixed ``UnicodeEncodeError`` error when using unicode file names (https://github.com/ansible-collections/community.aws/pull/295).
- ec2_eip - fix eip association by instance id & private ip address due to case-sensitivity of the ``PrivateIpAddress`` parameter (https://github.com/ansible-collections/community.aws/pull/328).
- ec2_vpc_endpoint - ensure ``changed`` is correctly set when deleting an endpoint (https://github.com/ansible-collections/community.aws/pull/362).
- ec2_vpc_endpoint - fix exception when attempting to delete an endpoint which has already been deleted (https://github.com/ansible-collections/community.aws/pull/362).
- ecs_task - use `required_if` to enforce mandatory parameters based on specified operation (https://github.com/ansible-collections/community.aws/pull/402).
- elb_application_lb - during the removal of an instance, the associated listeners are also removed.

community.crypto
~~~~~~~~~~~~~~~~

- openssl_csr - no longer fails when comparing CSR without basic constraint when ``basic_constraints`` is specified (https://github.com/ansible-collections/community.crypto/issues/179, https://github.com/ansible-collections/community.crypto/pull/180).

community.docker
~~~~~~~~~~~~~~~~

- docker_container - fix healthcheck disabling idempotency issue with strict comparison (https://github.com/ansible-collections/community.docker/issues/85).
- docker_image - prevent module failure when removing image that is removed between inspection and removal (https://github.com/ansible-collections/community.docker/pull/87).
- docker_image - prevent module failure when removing non-existant image by ID (https://github.com/ansible-collections/community.docker/pull/87).
- docker_image_info - prevent module failure when image vanishes between listing and inspection (https://github.com/ansible-collections/community.docker/pull/87).
- docker_image_info - prevent module failure when querying non-existant image by ID (https://github.com/ansible-collections/community.docker/pull/87).

community.general
~~~~~~~~~~~~~~~~~

- aerospike_migration - fix typo that caused ``migrate_tx_key`` instead of ``migrate_rx_key`` being used (https://github.com/ansible-collections/community.general/pull/1739).
- alternatives - internal refactoring: replaced uses of ``_`` with ``dummy`` (https://github.com/ansible-collections/community.general/pull/1819).
- beadm - internal refactoring: replaced uses of ``_`` with ``dummy`` (https://github.com/ansible-collections/community.general/pull/1819).
- bigpanda - actually use the ``deployment_message`` option (https://github.com/ansible-collections/community.general/pull/1928).
- chef_databag lookup plugin - wrapped usages of ``dict.keys()`` in ``list()`` for Python 3 compatibility (https://github.com/ansible-collections/community.general/pull/1861).
- cloudforms inventory - fixed issue that non-existing (archived) VMs were synced (https://github.com/ansible-collections/community.general/pull/720).
- cobbler_sync, cobbler_system - fix SSL/TLS certificate check when ``validate_certs`` set to ``false`` (https://github.com/ansible-collections/community.general/pull/1880).
- consul_io inventory script - kv_groups - fix byte chain decoding for Python 3 (https://github.com/ansible-collections/community.general/pull/620).
- cronvar - internal refactoring: replaced uses of ``_`` with ``dummy`` (https://github.com/ansible-collections/community.general/pull/1819).
- dconf - internal refactoring: replaced uses of ``_`` with ``dummy`` (https://github.com/ansible-collections/community.general/pull/1819).
- deploy_helper - allow ``state=clean`` to be used without defining a ``release`` (https://github.com/ansible-collections/community.general/issues/1852).
- diy callback plugin - wrapped usages of ``dict.keys()`` in ``list()`` for Python 3 compatibility (https://github.com/ansible-collections/community.general/pull/1861).
- elasticsearch_plugin - ``state`` parameter choices must use ``list()`` in python3 (https://github.com/ansible-collections/community.general/pull/1830).
- filesystem - internal refactoring: replaced uses of ``_`` with ``dummy`` (https://github.com/ansible-collections/community.general/pull/1819).
- filesystem - remove ``swap`` from list of FS supported by ``resizefs=yes`` (https://github.com/ansible-collections/community.general/issues/790).
- git_config - prevent ``run_command`` from expanding values (https://github.com/ansible-collections/community.general/issues/1776).
- gitlab_runner - parameter ``registration_token`` was required but is used only when ``state`` is ``present`` (https://github.com/ansible-collections/community.general/issues/1714).
- hipchat - internal refactoring: replaced uses of ``_`` with ``dummy`` (https://github.com/ansible-collections/community.general/pull/1819).
- idrac_redfish_command - wrapped usages of ``dict.keys()`` in ``list()`` for Python 3 compatibility (https://github.com/ansible-collections/community.general/pull/1861).
- idrac_redfish_config - wrapped usages of ``dict.keys()`` in ``list()`` for Python 3 compatibility (https://github.com/ansible-collections/community.general/pull/1861).
- idrac_redfish_info - wrapped usages of ``dict.keys()`` in ``list()`` for Python 3 compatibility (https://github.com/ansible-collections/community.general/pull/1861).
- imc_rest - explicitly logging out instead of registering the call in ```atexit``` (https://github.com/ansible-collections/community.general/issues/1735).
- infoblox inventory script - make sure that the script also works with Ansible 2.9, and returns a more helpful error when community.general is not installed as part of Ansible 2.10/3 (https://github.com/ansible-collections/community.general/pull/1871).
- ini_file - allows an empty string as a value for an option (https://github.com/ansible-collections/community.general/pull/1972).
- interfaces_file - internal refactoring: replaced uses of ``_`` with ``dummy`` (https://github.com/ansible-collections/community.general/pull/1819).
- iso_extract - use proper alias deprecation mechanism for ``thirsty`` alias of ``force`` (https://github.com/ansible-collections/community.general/pull/1830).
- java_cert - internal refactoring: replaced uses of ``_`` with ``dummy`` (https://github.com/ansible-collections/community.general/pull/1819).
- kibana_plugin - ``state`` parameter choices must use ``list()`` in python3 (https://github.com/ansible-collections/community.general/pull/1830).
- logstash_plugin - wrapped ``dict.keys()`` with ``list`` for use in ``choices`` setting (https://github.com/ansible-collections/community.general/pull/1830).
- lvg - internal refactoring: replaced uses of ``_`` with ``dummy`` (https://github.com/ansible-collections/community.general/pull/1819).
- lvol - internal refactoring: replaced uses of ``_`` with ``dummy`` (https://github.com/ansible-collections/community.general/pull/1819).
- lxc - internal refactoring: replaced uses of ``_`` with ``dummy`` (https://github.com/ansible-collections/community.general/pull/1819).
- lxc_container - internal refactoring: replaced uses of ``_`` with ``dummy`` (https://github.com/ansible-collections/community.general/pull/1819).
- lxc_container - wrapped usages of ``dict.keys()`` in ``list()`` for Python 3 compatibility (https://github.com/ansible-collections/community.general/pull/1861).
- lxd_container - wrapped usages of ``dict.keys()`` in ``list()`` for Python 3 compatibility (https://github.com/ansible-collections/community.general/pull/1861).
- manageiq_provider - wrapped ``dict.keys()`` with ``list`` for use in ``choices`` setting (https://github.com/ansible-collections/community.general/pull/1970).
- memcached cache plugin - wrapped usages of ``dict.keys()`` in ``list()`` for Python 3 compatibility (https://github.com/ansible-collections/community.general/pull/1861).
- meta/runtime.yml - improve deprecation messages (https://github.com/ansible-collections/community.general/pull/1918).
- net_tools.nios.api module_utils - wrapped usages of ``dict.keys()`` in ``list()`` for Python 3 compatibility (https://github.com/ansible-collections/community.general/pull/1861).
- nios_host_record - allow DNS Bypass for views other than default (https://github.com/ansible-collections/community.general/issues/1786).
- nmcli - add ``method4`` and ``method6`` options (https://github.com/ansible-collections/community.general/pull/1894).
- nmcli - ensure the ``slave-type`` option is passed to ``nmcli`` for type ``bond-slave`` (https://github.com/ansible-collections/community.general/pull/1882).
- nomad_job_info - fix module failure when nomad client returns no jobs (https://github.com/ansible-collections/community.general/pull/1721).
- nsot inventory script - wrapped usages of ``dict.keys()`` in ``list()`` for Python 3 compatibility (https://github.com/ansible-collections/community.general/pull/1861).
- oci_vcn - wrapped usages of ``dict.keys()`` in ``list()`` for Python 3 compatibility (https://github.com/ansible-collections/community.general/pull/1861).
- oneandone_monitoring_policy - wrapped usages of ``dict.keys()`` in ``list()`` for Python 3 compatibility (https://github.com/ansible-collections/community.general/pull/1861).
- packet_volume_attachment - removed extraneous ``print`` call - old debug? (https://github.com/ansible-collections/community.general/pull/1970).
- parted - internal refactoring: replaced uses of ``_`` with ``dummy`` (https://github.com/ansible-collections/community.general/pull/1819).
- proxmox inventory - added handling of extra trailing slashes in the URL (https://github.com/ansible-collections/community.general/pull/1914).
- proxmox lxc - only add the features flag when module parameter ``features`` is set. Before an empty string was send to proxmox in case the parameter was not used, which required to use ``root@pam`` for module execution (https://github.com/ansible-collections/community.general/pull/1763).
- proxmox* modules - refactored some parameter validation code into use of ``env_fallback``, ``required_if``, ``required_together``, ``required_one_of`` (https://github.com/ansible-collections/community.general/pull/1765).
- proxmox_kvm - do not add ``args`` if ``proxmox_default_behavior`` is set to no_defaults  (https://github.com/ansible-collections/community.general/issues/1641).
- proxmox_kvm - fix parameter ``vmid`` passed twice to ``exit_json`` while creating a virtual machine without cloning (https://github.com/ansible-collections/community.general/issues/1875, https://github.com/ansible-collections/community.general/pull/1895).
- proxmox_kvm - fix undefined local variable ``status`` when the parameter ``state`` is either ``stopped``, ``started``, ``restarted`` or ``absent`` (https://github.com/ansible-collections/community.general/pull/1847).
- proxmox_kvm - stop implicitly adding ``force`` equal to ``false``. Proxmox API requires not implemented parameters otherwise, and assumes ``force`` to be ``false`` by default anyways (https://github.com/ansible-collections/community.general/pull/1783).
- redfish_command - wrapped usages of ``dict.keys()`` in ``list()`` for Python 3 compatibility (https://github.com/ansible-collections/community.general/pull/1861).
- redfish_config - wrapped usages of ``dict.keys()`` in ``list()`` for Python 3 compatibility (https://github.com/ansible-collections/community.general/pull/1861).
- redhat_subscription - ``mutually_exclusive`` was referring to parameter alias instead of name (https://github.com/ansible-collections/community.general/pull/1795).
- redhat_subscription - wrapped usages of ``dict.keys()`` in ``list()`` for Python 3 compatibility (https://github.com/ansible-collections/community.general/pull/1861).
- redis cache plugin - wrapped usages of ``keys()`` in ``list()`` for Python 3 compatibility (https://github.com/ansible-collections/community.general/pull/1861).
- riak - parameters ``wait_for_handoffs`` and ``wait_for_ring`` are ``int`` but the default value was ``false`` (https://github.com/ansible-collections/community.general/pull/1830).
- rundeck_acl_policy - internal refactoring: replaced uses of ``_`` with ``dummy`` (https://github.com/ansible-collections/community.general/pull/1819).
- runit - removed unused code, and passing command as ``list`` instead of ``str`` to ``run_command()`` (https://github.com/ansible-collections/community.general/pull/1830).
- selective callback plugin - adjust import so that the plugin also works with ansible-core 2.11 (https://github.com/ansible-collections/community.general/pull/1807).
- selective callback plugin - wrapped usages of ``dict.keys()`` in ``list()`` for Python 3 compatibility (https://github.com/ansible-collections/community.general/pull/1861).
- sensu_check - wrapped usages of ``dict.keys()`` in ``list()`` for Python 3 compatibility (https://github.com/ansible-collections/community.general/pull/1861).
- spotinst_aws_elastigroup - wrapped usages of ``dict.keys()`` in ``list()`` for Python 3 compatibility (https://github.com/ansible-collections/community.general/pull/1861).
- statusio_maintenance - internal refactoring: replaced uses of ``_`` with ``dummy`` (https://github.com/ansible-collections/community.general/pull/1819).
- timezone - internal refactoring: replaced uses of ``_`` with ``dummy`` (https://github.com/ansible-collections/community.general/pull/1819).
- utm_utils module_utils - wrapped usages of ``dict.keys()`` in ``list()`` for Python 3 compatibility (https://github.com/ansible-collections/community.general/pull/1861).
- vdo - wrapped usages of ``dict.keys()`` in ``list()`` for Python 3 compatibility (https://github.com/ansible-collections/community.general/pull/1861).
- xfs_quota - the feedback for initializing project quota using xfs_quota binary from ``xfsprogs`` has changed since the version it was written for (https://github.com/ansible-collections/community.general/pull/1596).
- zfs - some ZFS properties could be passed when the dataset/volume did not exist, but would fail if the dataset already existed, even if the property matched what was specified in the ansible task (https://github.com/ansible-collections/community.general/issues/868, https://github.com/ansible-collections/community.general/pull/1833).
- zfs_delegate_admin - the elements of ``users``, ``groups`` and ``permissions`` are now enforced to be strings (https://github.com/ansible-collections/community.general/pull/1766).

community.grafana
~~~~~~~~~~~~~~~~~

- Fix issue with url when grafana_url has a trailing slash (#135)
- grafana_dashboard, Fix reference before assignment issue (#146)

community.hashi_vault
~~~~~~~~~~~~~~~~~~~~~

- hashi_vault - restore use of ``VAULT_ADDR`` environment variable as a low preference env var (https://github.com/ansible-collections/community.hashi_vault/pull/61).

community.hrobot
~~~~~~~~~~~~~~~~

- robot - force HTTP basic authentication to reduce number of HTTPS requests (https://github.com/ansible-collections/community.hrobot/pull/9).

community.kubernetes
~~~~~~~~~~~~~~~~~~~~

- helm - ``release_values`` makes ansible always show changed state (https://github.com/ansible-collections/community.kubernetes/issues/274)
- helm - make helm-diff plugin detection more reliable by splitting by any whitespace instead of explicit whitespace (``\s``) (https://github.com/ansible-collections/community.kubernetes/pull/362).
- helm - return values in check mode when release is not present (https://github.com/ansible-collections/community.kubernetes/issues/280).
- helm_plugin - make unused ``release_namespace`` parameter as optional (https://github.com/ansible-collections/community.kubernetes/issues/357).
- helm_plugin_info - make unused ``release_namespace`` parameter as optional (https://github.com/ansible-collections/community.kubernetes/issues/357).
- k8s - fix check_mode always showing changes when using stringData on Secrets (https://github.com/ansible-collections/community.kubernetes/issues/282).
- k8s - handle ValueError when namespace is not provided (https://github.com/ansible-collections/community.kubernetes/pull/330).
- respect the ``wait_timeout`` parameter in the ``k8s`` and ``k8s_info`` modules when a resource does not exist (https://github.com/ansible-collections/community.kubernetes/issues/344).

community.libvirt
~~~~~~~~~~~~~~~~~

- libvirt_qemu - Mitigate a CPU hammering active wait loop
- libvirt_qemu - add import error handling
- virt - Correctly get the error message from libvirt
- virt - Return "changed" status when using "define" command and domain XML was updated
- virt - The define action searchs for the domain name into the xml definition to determine if the domain needs to be created or updated. The xml variable contains the parsed definition but doesn't guarantee the existence of the name tag. This change targets to fix the scenario where the xml var is not empty but doesn't contain a name tag.
- virt_net - The name parameter is not required for the list_nets or facts command so we adjust the module to allow for that.

community.mysql
~~~~~~~~~~~~~~~

- mysql_user - fix handling of INSERT, UPDATE, REFERENCES on columns (https://github.com/ansible-collections/community.mysql/issues/106).
- mysql_user - the module is not idempotent when SELECT on columns granted (https://github.com/ansible-collections/community.mysql/issues/99).

community.sops
~~~~~~~~~~~~~~

- community.sops.sops_encrypt - use output type ``yaml`` when path ends with ``.yaml`` (https://github.com/ansible-collections/community.sops/pull/56).

community.vmware
~~~~~~~~~~~~~~~~

- vcenter_license - fixed a bug that the license doesn't assign in VCSA 7.0u1c (https://github.com/ansible-collections/community.vmware/pull/643).
- vmware - fixed an issue that a port group name doesn't compare correctly in the find_network_by_name function (https://github.com/ansible-collections/community.vmware/pull/661).
- vmware_category - append namespace to associable types (https://github.com/ansible-collections/community.vmware/issues/579).
- vmware_cluster_ha - fix enabling APD or PDL response (https://github.com/ansible-collections/community.vmware/issues/676).
- vmware_cluster_info - return VSAN status correctly (https://github.com/ansible-collections/community.vmware/issues/673).
- vmware_deploy_ovf - fixed an issue that an error message doesn't show when not finding a port group name (https://github.com/ansible-collections/community.vmware/pull/661).
- vmware_dvs_portgroup - fixed the issue that the VLAN configuration isn't compared correctly in the module (https://github.com/ansible-collections/community.vmware/pull/638).
- vmware_dvs_portgroup_find - fixed to decode the special characters URL-encoded in the dvs port group name (https://github.com/ansible-collections/community.vmware/pull/648).
- vmware_dvs_portgroup_info - fixed to decode the special characters URL-encoded in the dvs port group name (https://github.com/ansible-collections/community.vmware/pull/648).
- vmware_guest - add support for ``advanced settings`` in vmware_guest (https://github.com/ansible-collections/community.vmware/issues/602).
- vmware_guest_register_operation - fixed an issue that an error has been occurring when not specifying a datacenter name (https://github.com/ansible-collections/community.vmware/pull/693).
- vmware_vm_storage_policy - fixed an issue that an error for pyvmomi(SDK) occurred when a tag or category doesn't exist (https://github.com/ansible-collections/community.vmware/pull/682).

community.windows
~~~~~~~~~~~~~~~~~

- win_firewall_rule - Ensure ``service: any`` is set to match any service instead of the literal service called ``any`` as per the docs
- win_scoop - Make sure we enable TLS 1.2 when installing scoop
- win_xml - Fix ``PropertyNotFound`` exception when creating a new attribute - https://github.com/ansible-collections/community.windows/issues/166

containers.podman
~~~~~~~~~~~~~~~~~

- Add docs generation
- Attempt graceful stop when recreating container
- Don't calculate image digest in check mode
- Fix internal networks and DNS plugin for v3
- Fix podman_pod* modules for Podman v3
- Fixes for podman_container for Podman v3
- Update documentation
- documentation - Add docs to Github
- podman_container - Add 'created' state for podman_container
- podman_container - Change default log level for 3+ versions
- podman_container - Convert systemd option to a string
- podman_container - Don't recreate container if env_file is specified
- podman_container - Fix 'cap_add' and 'cap_drop' idempotency
- podman_container - Fix idempotency for multiple ports
- podman_container - Fix slirp4netns options idempotency
- podman_container - Fix uid/gid checks for podman 1.6.4 volumes
- podman_container - Handle slash removals for root volumes mount
- podman_container - Restart container in a simple manner
- podman_container - podman_container_lib - fix command idempotency
- podman_image - Add debug log and podman_actions to podman_image
- podman_image - Don't set default for validate-certs in podman_image

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- ome_firmware_baseline_compliance_info - OMEnt firmware baseline compliance info pagination support added (https://github.com/dell/dellemc-openmanage-ansible-modules/issues/171)
- ome_network_proxy - OMEnt network proxy check mode support added (https://github.com/dell/dellemc-openmanage-ansible-modules/issues/187)

dellemc.os9
~~~~~~~~~~~

- Fix issue in using list of strings for commands argument for os10_command module (https://github.com/ansible-collections/dellemc.os9/issues/15)
- Fixed sanity error found during the sanity tst of automation hub upload

f5networks.f5_modules
~~~~~~~~~~~~~~~~~~~~~

- Fix a bug with replace_with_all logic to consider ports in bigip_pool_member module
- Fix control characters causing url encoding errors in bigip_policy module
- Fix issue in bigip_pool_member module invwhere incorrect IF statement in function preveninv ted from reusing FQDN nodes for new pool members
- Fix issue where error messages were replaced by generic error message in bigip_device_policy module
- Fix issue with destination_address and destination_port parameters not being properly returned by bigip_device_info module
- Fix issue with removal action not allowing atomic rule updates in bigip_policy_rule module
- Fix virtual server type value displaying incorrect information in bigip_device_info module

kubernetes.core
~~~~~~~~~~~~~~~

- helm - ``release_values`` makes ansible always show changed state (https://github.com/ansible-collections/kubernetes.core/issues/274)
- helm - make helm-diff plugin detection more reliable by splitting by any whitespace instead of explicit whitespace (``\s``) (https://github.com/ansible-collections/kubernetes.core/pull/362).
- helm - return values in check mode when release is not present (https://github.com/ansible-collections/kubernetes.core/issues/280).
- helm_plugin - make unused ``release_namespace`` parameter as optional (https://github.com/ansible-collections/kubernetes.core/issues/357).
- helm_plugin_info - make unused ``release_namespace`` parameter as optional (https://github.com/ansible-collections/kubernetes.core/issues/357).
- k8s - fix check_mode always showing changes when using stringData on Secrets (https://github.com/ansible-collections/kubernetes.core/issues/282).
- k8s - handle ValueError when namespace is not provided (https://github.com/ansible-collections/kubernetes.core/pull/330).
- respect the ``wait_timeout`` parameter in the ``k8s`` and ``k8s_info`` modules when a resource does not exist (https://github.com/ansible-collections/kubernetes.core/issues/344).

netapp.ontap
~~~~~~~~~~~~

- All REST modules - ONTAP 9.4 and 9.5 are incorrectly detected as supporting REST with ``use_rest:auto``.
- na_ontap_igroup - report error when attempting to modify an option that cannot be changed.
- na_ontap_ldap_client - ``port`` was incorrectly used instead of ``tcp_port``.
- na_ontap_lun - ``qos_policy_group`` could not be modified if a value was not provided at creation.
- na_ontap_lun - tiering options were ignored in san_application_template.
- na_ontap_node - KeyError fix for location ans asset-tag parameters in get_node().
- na_ontap_snapmirror - SVM scoped policies were not found when using a destination path with REST application.
- na_ontap_snapmirror - check for consistency_group_volumes always fails on 9.7, and cluster or ipspace when using endpoints with ZAPI.
- na_ontap_volume - changes in ``encrypt`` settings were ignored.
- na_ontap_volume - report error from resize operation when using REST.
- na_ontap_volume - returns an error now if deleting a volume with REST api fails.
- na_ontap_volume - unmount volume before deleting it when using REST.

netbox.netbox
~~~~~~~~~~~~~

- netbox_ip_address - Added assigned_object to ALLOWED_QUERY_PARAMS

openvswitch.openvswitch
~~~~~~~~~~~~~~~~~~~~~~~

- Allow deleting key from table without specifying value (https://github.com/ansible-collections/openvswitch.openvswitch/issues/64).

purestorage.flasharray
~~~~~~~~~~~~~~~~~~~~~~

- purefa_hg - Ensure all hostname chacks are lowercase for consistency
- purefa_pgsnap - Add check to ensure suffix name meets naming conventions
- purefa_pgsnap - Ensure pgsnap restores work for AC PGs
- purefa_pod - Ensure all pod names are lowercase for consistency
- purefa_snap - Update suffix regex pattern
- purefa_volume - Add missing variable initialization
- purefa_volume - Fix issues with moving volumes into demoted or linked pods

sensu.sensu_go
~~~~~~~~~~~~~~

- Add ansible.windows dependency that we forgot to add when we introducted the Sensu Go agent installation on Windows.
- Allow downgrading Sensu Go packages on Linux distributions that use yum or dnf for package management.

Known Issues
------------

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- ome_smart_fabric - Issue(185322) Only three design types are supported by OpenManage Enterprise Modular but the module successfully creates a fabric when the design type is not supported.
- ome_smart_fabric_uplink - Issue(186024) ome_smart_fabric_uplink module does not allow the creation of multiple uplinks of the same name even though this is supported by OpenManage Enterprise Modular. If an uplink is created using the same name as an existing uplink, the existing uplink is modified.

New Plugins
-----------

Filter
~~~~~~

- community.general.version_sort - Sort a list according to version order instead of pure alphabetical one

New Modules
-----------

community.docker
~~~~~~~~~~~~~~~~

- community.docker.docker_image_load - Load docker image(s) from archives
- community.docker.docker_plugin - Manage Docker plugins

community.general
~~~~~~~~~~~~~~~~~

Cloud
^^^^^

Misc
....

- community.general.proxmox_storage_info - Retrieve information about one or more Proxmox VE storages

Monitoring
^^^^^^^^^^

- community.general.statsd - Send metrics to StatsD

Source Control
^^^^^^^^^^^^^^

Github
......

- community.general.github_repo - Manage your repositories on Github

Gitlab
......

- community.general.gitlab_project_members - Manage project members on GitLab Server

Web Infrastructure
^^^^^^^^^^^^^^^^^^

- community.general.jenkins_build - Manage jenkins builds

community.windows
~~~~~~~~~~~~~~~~~

- community.windows.win_psrepository_copy - Copies registered PSRepositories to other user profiles

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- dellemc.openmanage.ome_profile - Create, modify, delete, assign, unassign and migrate a profile on OpenManage Enterprise

netapp.ontap
~~~~~~~~~~~~

- netapp.ontap.na_ontap_cifs_local_group_member - NetApp Ontap - Add or remove CIFS local group member
- netapp.ontap.na_ontap_domain_tunnel - NetApp ONTAP domain tunnel
- netapp.ontap.na_ontap_fpolicy_policy - NetApp ONTAP - Create, delete or modify an FPolicy policy.
- netapp.ontap.na_ontap_log_forward - NetApp ONTAP Log Forward Configuration
- netapp.ontap.na_ontap_lun_map_reporting_nodes - NetApp ONTAP LUN maps reporting nodes
- netapp.ontap.na_ontap_security_config - NetApp ONTAP modify security config for SSL.
- netapp.ontap.na_ontap_storage_auto_giveback - Enables or disables NetApp ONTAP storage auto giveback for a specified node
- netapp.ontap.na_ontap_storage_failover - Enables or disables NetApp Ontap storage failover for a specified node
- netapp.ontap.na_ontap_volume_efficiency - NetApp Ontap enables, disables or modifies volume efficiency

sensu.sensu_go
~~~~~~~~~~~~~~

- sensu.sensu_go.cluster - Manage Sensu Go clusters
- sensu.sensu_go.cluster_info - List available Sensu Go clusters
- sensu.sensu_go.etcd_replicator - Manage Sensu Go etcd replicators
- sensu.sensu_go.etcd_replicator_info - List Sensu Go etcd replicators

Unchanged Collections
---------------------

- ansible.netcommon (still version 1.5.0)
- arista.eos (still version 1.3.0)
- azure.azcollection (still version 1.4.0)
- check_point.mgmt (still version 2.0.0)
- chocolatey.chocolatey (still version 1.0.2)
- cisco.aci (still version 2.0.0)
- cisco.asa (still version 1.0.4)
- cisco.ios (still version 1.3.0)
- cisco.iosxr (still version 1.2.1)
- cisco.mso (still version 1.1.0)
- cisco.nso (still version 1.0.3)
- cisco.nxos (still version 1.4.0)
- cisco.ucs (still version 1.6.0)
- community.azure (still version 1.0.0)
- community.digitalocean (still version 1.0.0)
- community.fortios (still version 1.0.0)
- community.google (still version 1.0.0)
- community.kubevirt (still version 1.0.0)
- community.network (still version 2.0.1)
- community.postgresql (still version 1.1.1)
- community.proxysql (still version 1.0.0)
- community.routeros (still version 1.1.0)
- community.skydive (still version 1.0.0)
- community.zabbix (still version 1.2.0)
- cyberark.conjur (still version 1.1.0)
- cyberark.pas (still version 1.0.5)
- dellemc.os10 (still version 1.1.1)
- fortinet.fortimanager (still version 2.0.1)
- frr.frr (still version 1.0.3)
- gluster.gluster (still version 1.0.1)
- google.cloud (still version 1.0.2)
- hetzner.hcloud (still version 1.2.1)
- ibm.qradar (still version 1.0.3)
- infinidat.infinibox (still version 1.2.4)
- inspur.sm (still version 1.1.2)
- junipernetworks.junos (still version 1.3.0)
- mellanox.onyx (still version 1.0.0)
- netapp.aws (still version 20.9.0)
- netapp.elementsw (still version 20.11.0)
- netapp_eseries.santricity (still version 1.1.0)
- ngine_io.cloudstack (still version 2.0.0)
- ngine_io.exoscale (still version 1.0.0)
- ngine_io.vultr (still version 1.1.0)
- purestorage.flashblade (still version 1.4.0)
- servicenow.servicenow (still version 1.0.4)
- splunk.es (still version 1.0.2)
- theforeman.foreman (still version 1.5.1)
- vyos.vyos (still version 1.1.1)
- wti.remote (still version 1.0.1)

v3.0.0
======

.. contents::
  :local:
  :depth: 2

Release Summary
---------------

Release Date: 2021-02-09

`Porting Guide <https://docs.ansible.com/ansible/devel/porting_guides.html>`_

Ansible-base
------------

Ansible 3.0.0 contains Ansible-base version 2.10.5.
This is a newer version than version 2.10.1 contained in the previous Ansible release.

The changes are reported in the combined changelog below.

Included Collections
--------------------

If not mentioned explicitly, the changes are reported in the combined changelog below.

+-------------------------------+----------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Collection                    | Ansible 2.10.0 | Ansible 3.0.0 | Notes                                                                                                                                                                                                                                      |
+===============================+================+===============+============================================================================================================================================================================================================================================+
| amazon.aws                    | 1.2.0          | 1.3.0         |                                                                                                                                                                                                                                            |
+-------------------------------+----------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ansible.netcommon             | 1.2.1          | 1.5.0         |                                                                                                                                                                                                                                            |
+-------------------------------+----------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ansible.utils                 |                | 2.0.0         |                                                                                                                                                                                                                                            |
+-------------------------------+----------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ansible.windows               | 1.0.0          | 1.3.0         |                                                                                                                                                                                                                                            |
+-------------------------------+----------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| arista.eos                    | 1.0.3          | 1.3.0         |                                                                                                                                                                                                                                            |
+-------------------------------+----------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| awx.awx                       | 14.1.0         | 17.0.1        | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.                                                                                                               |
+-------------------------------+----------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| azure.azcollection            | 1.0.0          | 1.4.0         | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.                                                                                                               |
+-------------------------------+----------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| check_point.mgmt              | 1.0.6          | 2.0.0         | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.                                                                                                               |
+-------------------------------+----------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cisco.aci                     | 1.0.0          | 2.0.0         |                                                                                                                                                                                                                                            |
+-------------------------------+----------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cisco.asa                     | 1.0.3          | 1.0.4         |                                                                                                                                                                                                                                            |
+-------------------------------+----------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cisco.intersight              | 1.0.8          | 1.0.10        | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.                                                                                                               |
+-------------------------------+----------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cisco.ios                     | 1.0.3          | 1.3.0         |                                                                                                                                                                                                                                            |
+-------------------------------+----------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cisco.iosxr                   | 1.0.5          | 1.2.1         |                                                                                                                                                                                                                                            |
+-------------------------------+----------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cisco.meraki                  | 2.0.0          | 2.2.0         |                                                                                                                                                                                                                                            |
+-------------------------------+----------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cisco.mso                     | 1.0.0          | 1.1.0         |                                                                                                                                                                                                                                            |
+-------------------------------+----------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cisco.nso                     |                | 1.0.3         |                                                                                                                                                                                                                                            |
+-------------------------------+----------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cisco.nxos                    | 1.1.0          | 1.4.0         |                                                                                                                                                                                                                                            |
+-------------------------------+----------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cisco.ucs                     | 1.5.0          | 1.6.0         | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.                                                                                                               |
+-------------------------------+----------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cloudscale_ch.cloud           | 1.1.0          | 2.0.0         |                                                                                                                                                                                                                                            |
+-------------------------------+----------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.aws                 | 1.2.0          | 1.3.0         |                                                                                                                                                                                                                                            |
+-------------------------------+----------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.crypto              | 1.1.1          | 1.4.0         |                                                                                                                                                                                                                                            |
+-------------------------------+----------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.docker              |                | 1.2.2         |                                                                                                                                                                                                                                            |
+-------------------------------+----------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.fortios             |                | 1.0.0         |                                                                                                                                                                                                                                            |
+-------------------------------+----------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.general             | 1.1.0          | 2.0.1         |                                                                                                                                                                                                                                            |
+-------------------------------+----------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.google              |                | 1.0.0         |                                                                                                                                                                                                                                            |
+-------------------------------+----------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.grafana             | 1.0.0          | 1.1.0         |                                                                                                                                                                                                                                            |
+-------------------------------+----------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.hashi_vault         |                | 1.0.0         |                                                                                                                                                                                                                                            |
+-------------------------------+----------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.hrobot              |                | 1.1.0         |                                                                                                                                                                                                                                            |
+-------------------------------+----------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.kubernetes          | 1.0.0          | 1.1.1         |                                                                                                                                                                                                                                            |
+-------------------------------+----------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.kubevirt            |                | 1.0.0         |                                                                                                                                                                                                                                            |
+-------------------------------+----------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.mongodb             | 1.0.0          | 1.2.0         |                                                                                                                                                                                                                                            |
+-------------------------------+----------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.mysql               | 1.0.0          | 1.2.0         |                                                                                                                                                                                                                                            |
+-------------------------------+----------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.network             | 1.1.0          | 2.0.1         |                                                                                                                                                                                                                                            |
+-------------------------------+----------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.okd                 |                | 1.0.1         |                                                                                                                                                                                                                                            |
+-------------------------------+----------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.postgresql          |                | 1.1.1         |                                                                                                                                                                                                                                            |
+-------------------------------+----------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.routeros            |                | 1.1.0         |                                                                                                                                                                                                                                            |
+-------------------------------+----------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.sops                |                | 1.0.4         |                                                                                                                                                                                                                                            |
+-------------------------------+----------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.vmware              | 1.2.0          | 1.7.0         |                                                                                                                                                                                                                                            |
+-------------------------------+----------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.windows             | 1.0.0          | 1.2.0         |                                                                                                                                                                                                                                            |
+-------------------------------+----------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.zabbix              | 1.0.0          | 1.2.0         |                                                                                                                                                                                                                                            |
+-------------------------------+----------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| containers.podman             | 1.2.0          | 1.4.1         |                                                                                                                                                                                                                                            |
+-------------------------------+----------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cyberark.conjur               | 1.0.7          | 1.1.0         | You can find the collection's changelog at `https://github.com/cyberark/ansible-conjur-collection/blob/master/CHANGELOG.md <https://github.com/cyberark/ansible-conjur-collection/blob/master/CHANGELOG.md>`_.                             |
+-------------------------------+----------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| dellemc.openmanage            |                | 3.0.0         |                                                                                                                                                                                                                                            |
+-------------------------------+----------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| dellemc.os10                  | 1.0.1          | 1.1.1         |                                                                                                                                                                                                                                            |
+-------------------------------+----------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| dellemc.os6                   | 1.0.2          | 1.0.6         |                                                                                                                                                                                                                                            |
+-------------------------------+----------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| dellemc.os9                   | 1.0.2          | 1.0.3         |                                                                                                                                                                                                                                            |
+-------------------------------+----------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| f5networks.f5_modules         | 1.5.0          | 1.7.1         |                                                                                                                                                                                                                                            |
+-------------------------------+----------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| fortinet.fortimanager         | 1.0.5          | 2.0.1         | The collection did not have a changelog in this version.                                                                                                                                                                                   |
+-------------------------------+----------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| fortinet.fortios              | 1.0.15         | 1.1.8         | The collection did not have a changelog in this version.                                                                                                                                                                                   |
+-------------------------------+----------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| google.cloud                  | 1.0.0          | 1.0.2         | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.                                                                                                               |
+-------------------------------+----------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| hetzner.hcloud                | 1.0.0          | 1.2.1         |                                                                                                                                                                                                                                            |
+-------------------------------+----------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| infinidat.infinibox           | 1.2.3          | 1.2.4         | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.                                                                                                               |
+-------------------------------+----------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| inspur.sm                     |                | 1.1.2         |                                                                                                                                                                                                                                            |
+-------------------------------+----------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| junipernetworks.junos         | 1.1.0          | 1.3.0         |                                                                                                                                                                                                                                            |
+-------------------------------+----------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| kubernetes.core               |                | 1.1.1         |                                                                                                                                                                                                                                            |
+-------------------------------+----------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| netapp.aws                    | 20.8.0         | 20.9.0        | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.                                                                                                               |
+-------------------------------+----------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| netapp.elementsw              | 20.8.0         | 20.11.0       |                                                                                                                                                                                                                                            |
+-------------------------------+----------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| netapp.ontap                  | 20.8.0         | 21.1.1        |                                                                                                                                                                                                                                            |
+-------------------------------+----------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| netapp_eseries.santricity     | 1.0.8          | 1.1.0         |                                                                                                                                                                                                                                            |
+-------------------------------+----------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| netbox.netbox                 | 1.0.2          | 2.0.0         |                                                                                                                                                                                                                                            |
+-------------------------------+----------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ngine_io.cloudstack           | 1.0.1          | 2.0.0         |                                                                                                                                                                                                                                            |
+-------------------------------+----------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ngine_io.vultr                | 1.0.0          | 1.1.0         |                                                                                                                                                                                                                                            |
+-------------------------------+----------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| openstack.cloud               | 1.1.0          | 1.2.1         |                                                                                                                                                                                                                                            |
+-------------------------------+----------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| openvswitch.openvswitch       | 1.0.5          | 1.1.0         |                                                                                                                                                                                                                                            |
+-------------------------------+----------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ovirt.ovirt                   | 1.1.3          | 1.3.0         |                                                                                                                                                                                                                                            |
+-------------------------------+----------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| purestorage.flasharray        | 1.4.0          | 1.5.1         |                                                                                                                                                                                                                                            |
+-------------------------------+----------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| purestorage.flashblade        | 1.3.0          | 1.4.0         |                                                                                                                                                                                                                                            |
+-------------------------------+----------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| sensu.sensu_go                |                | 1.8.0         |                                                                                                                                                                                                                                            |
+-------------------------------+----------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| servicenow.servicenow         | 1.0.2          | 1.0.4         |                                                                                                                                                                                                                                            |
+-------------------------------+----------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| t_systems_mms.icinga_director |                | 1.13.0        | You can find the collection's changelog at `https://github.com/T-Systems-MMS/ansible-collection-icinga-director/blob/master/CHANGELOG.md <https://github.com/T-Systems-MMS/ansible-collection-icinga-director/blob/master/CHANGELOG.md>`_. |
+-------------------------------+----------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| theforeman.foreman            | 1.1.0          | 1.5.1         |                                                                                                                                                                                                                                            |
+-------------------------------+----------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| vyos.vyos                     | 1.0.4          | 1.1.1         |                                                                                                                                                                                                                                            |
+-------------------------------+----------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Major Changes
-------------

cisco.aci
~~~~~~~~~

- Change certificate_name to name in aci_aaa_user_certificate module for query operation

community.general
~~~~~~~~~~~~~~~~~

- For community.general 3.0.0, the ``ome_device_info``, ``idrac_firmware`` and ``idrac_server_config_profile`` modules will be moved to the `dellemc.openmanage <https://galaxy.ansible.com/dellemc/openmanage>`_ collection.
  A redirection will be inserted so that users using ansible-base 2.10 or newer do not have to change anything.

  If you use Ansible 2.9 and explicitly use the DellEMC modules mentioned above from this collection, you will need to adjust your playbooks and roles to use FQCNs starting with ``dellemc.openmanage.`` instead of ``community.general.``,
  for example replace ``community.general.ome_device_info`` in a task by ``dellemc.openmanage.ome_device_info``.

  If you use ansible-base and installed ``community.general`` manually and rely on the DellEMC modules mentioned above, you have to make sure to install the ``dellemc.openmanage`` collection as well.
  If you are using FQCNs, for example ``community.general.ome_device_info`` instead of ``ome_device_info``, it will continue working, but we still recommend to adjust the FQCNs as well.
- The community.general collection no longer depends on the ansible.netcommon collection (https://github.com/ansible-collections/community.general/pull/1561).
- The community.general collection no longer depends on the ansible.posix collection (https://github.com/ansible-collections/community.general/pull/1157).

community.kubernetes
~~~~~~~~~~~~~~~~~~~~

- k8s - Add support for template parameter (https://github.com/ansible-collections/community.kubernetes/pull/230).
- k8s_* - Add support for vaulted kubeconfig and src (https://github.com/ansible-collections/community.kubernetes/pull/193).

community.okd
~~~~~~~~~~~~~

- Add custom k8s module, integrate better Molecule tests (https://github.com/ansible-collections/community.okd/pull/7).
- Add downstream build scripts to build redhat.openshift (https://github.com/ansible-collections/community.okd/pull/20).
- Add openshift connection plugin, update inventory plugin to use it (https://github.com/ansible-collections/community.okd/pull/18).
- Add openshift_process module for template rendering and optional application of rendered resources (https://github.com/ansible-collections/community.okd/pull/44).
- Add openshift_route module for creating routes from services (https://github.com/ansible-collections/community.okd/pull/40).
- Initial content migration from community.kubernetes (https://github.com/ansible-collections/community.okd/pull/3).
- openshift_auth - new module (migrated from k8s_auth in community.kubernetes) (https://github.com/ansible-collections/community.okd/pull/33).

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- Removed the existing deprecated modules.
- Standardization of ten iDRAC ansible modules based on ansible guidelines.
- Support for OpenManage Enterprise Modular.

dellemc.os10
~~~~~~~~~~~~

- os10_bgp - Enhanced router bgp keyword support for non-default vrf which are supported for default vrf and additional keyword to support both default and non-default vrf
- os10_snmp role - Added support for snmp V3 features in community, group, host, engineID

f5networks.f5_modules
~~~~~~~~~~~~~~~~~~~~~

- Add phone home Teem integration into all modules, functionality can be disabled by setting up F5_TEEM environment variable or no_f5_teem provider parameter
- Added async_timeout parameter to bigip_ucs_fetch module to allow customization of module wait for async interface
- Changed bigip_ucs_fetch module to use asynchronous interface when generating UCS files

kubernetes.core
~~~~~~~~~~~~~~~

- Add changelog and fragments and document changelog process (https://github.com/ansible-collections/kubernetes.core/pull/131).
- helm - New module for managing Helm charts (https://github.com/ansible-collections/kubernetes.core/pull/61).
- helm_info - New module for retrieving Helm chart information (https://github.com/ansible-collections/kubernetes.core/pull/61).
- helm_plugin - new module to manage Helm plugins (https://github.com/ansible-collections/kubernetes.core/pull/154).
- helm_plugin_info - new modules to gather information about Helm plugins (https://github.com/ansible-collections/kubernetes.core/pull/154).
- helm_repository - New module for managing Helm repositories (https://github.com/ansible-collections/kubernetes.core/pull/61).
- k8s - Add support for template parameter (https://github.com/ansible-collections/kubernetes.core/pull/230).
- k8s - Inventory source migrated from Ansible 2.9 to Kubernetes collection.
- k8s - Lookup plugin migrated from Ansible 2.9 to Kubernetes collection.
- k8s - Module migrated from Ansible 2.9 to Kubernetes collection.
- k8s_* - Add support for vaulted kubeconfig and src (https://github.com/ansible-collections/kubernetes.core/pull/193).
- k8s_auth - Module migrated from Ansible 2.9 to Kubernetes collection.
- k8s_config_resource_name - Filter plugin migrated from Ansible 2.9 to Kubernetes collection.
- k8s_exec - New module for executing commands on pods via Kubernetes API (https://github.com/ansible-collections/kubernetes.core/pull/14).
- k8s_exec - Return rc for the command executed (https://github.com/ansible-collections/kubernetes.core/pull/158).
- k8s_info - Module migrated from Ansible 2.9 to Kubernetes collection.
- k8s_log - New module for retrieving pod logs (https://github.com/ansible-collections/kubernetes.core/pull/16).
- k8s_scale - Module migrated from Ansible 2.9 to Kubernetes collection.
- k8s_service - Module migrated from Ansible 2.9 to Kubernetes collection.
- kubectl - Connection plugin migrated from Ansible 2.9 to Kubernetes collection.
- openshift - Inventory source migrated from Ansible 2.9 to Kubernetes collection.

netbox.netbox
~~~~~~~~~~~~~

- nb_inventory - Add ``dns_name`` option that adds ``dns_name`` to the host when ``True`` and device has a primary IP address. (#394)
- nb_inventory - Add ``status`` as a ``group_by`` option. (398)
- nb_inventory - Move around ``extracted_primary_ip`` to allow for ``config_context`` or ``custom_field`` to overwite. (#377)
- nb_inventory - Services are now a list of integers due to NetBox 2.10 changes. (#396)
- nb_lookup - Allow ID to be passed in and use ``.get`` instead of ``.filter``. (#376)
- nb_lookup - Allow ``api_endpoint`` and ``token`` to be found via env. (#391)

ovirt.ovirt
~~~~~~~~~~~

- cluster_upgrade - Migrate role (https://github.com/oVirt/ovirt-ansible-collection/pull/94).
- disaster_recovery - Migrate role (https://github.com/oVirt/ovirt-ansible-collection/pull/134).
- engine_setup - Migrate role (https://github.com/oVirt/ovirt-ansible-collection/pull/69).
- hosted_engine_setup - Migrate role (https://github.com/oVirt/ovirt-ansible-collection/pull/106).
- image_template - Migrate role (https://github.com/oVirt/ovirt-ansible-collection/pull/95).
- infra - Migrate role (https://github.com/oVirt/ovirt-ansible-collection/pull/92).
- manageiq - Migrate role (https://github.com/oVirt/ovirt-ansible-collection/pull/97).
- ovirt_system_option_info - Add new module (https://github.com/oVirt/ovirt-ansible-collection/pull/206).
- repositories - Migrate role (https://github.com/oVirt/ovirt-ansible-collection/pull/96).
- shutdown_env - Migrate role (https://github.com/oVirt/ovirt-ansible-collection/pull/112).
- vm_infra - Migrate role (https://github.com/oVirt/ovirt-ansible-collection/pull/93).

servicenow.servicenow
~~~~~~~~~~~~~~~~~~~~~

- add new tests (find with no result, search many)
- add related tests
- add support for ServiceNOW table api display_value exclude_reference_link and suppress_pagination_header
- use new API for pysnow >=0.6.0

Minor Changes
-------------

Ansible-base
~~~~~~~~~~~~

- ansible-doc - provide ``has_action`` field in JSON output for modules. That information is currently only available in the text view (https://github.com/ansible/ansible/pull/72359).
- ansible-galaxy - find any collection dependencies in the globally configured Galaxy servers and not just the server the parent collection is from.
- ansible-test - Add a ``--docker-network`` option to choose the network for running containers when using the ``--docker`` option.
- ansible-test - Added a ``--export`` option to the ``ansible-test coverage combine`` command to facilitate multi-stage aggregation of coverage in CI pipelines.
- ansible-test - Added the ``-remote rhel/7.9`` option to run tests on RHEL 7.9
- ansible-test - CentOS 8 container is now 8.2.2004 (https://github.com/ansible/distro-test-containers/pull/45).
- ansible-test - Changed the internal name of the custom plugin used to identify use of unwanted imports and functions.
- ansible-test - Collections can now specify pip constraints for unit and integration test requirements using ``tests/unit/constraints.txt`` and ``tests/integration/constraints.txt`` respectively.
- ansible-test - Fix container hostname/IP discovery for the ``acme`` test plugin.
- ansible-test - OpenSuse container now uses Leap 15.2 (https://github.com/ansible/distro-test-containers/pull/48).
- ansible-test - Raise the number of bytes scanned by ansible-test to determine if a file is binary to 4096.
- ansible-test - The ``pylint`` sanity test is now skipped with a warning on Python 3.9 due to unresolved upstream regressions.
- ansible-test - The ``pylint`` sanity test is now supported on Python 3.8.
- ansible-test - Ubuntu containers as well as ``default-test-container`` and ``ansible-base-test-container`` are now slightly smaller due to apt cleanup (https://github.com/ansible/distro-test-containers/pull/46).
- ansible-test - ``default-test-container`` and ``ansible-base-test-container`` now use Python 3.9.0 instead of 3.9.0rc1.
- ansible-test - add macOS 11.1 as a remote target (https://github.com/ansible/ansible/pull/72622)
- ansible-test - centos6 end of life - container image updated to point to vault base repository (https://github.com/ansible/distro-test-containers/pull/54)
- ansible-test - python-cryptography is now bounded at <3.2, as 3.2 drops support for OpenSSL 1.0.2 upon which some of our CI infrastructure still depends.
- ansible-test - remote macOS instances no longer install ``virtualenv`` during provisioning
- ansible-test - virtualenv helper scripts now prefer ``venv`` on Python 3 over ``virtualenv`` if the ``ANSIBLE_TEST_PREFER_VENV`` environment variable is set
- ansible-test validate-modules - no longer assume that ``default`` for ``type=bool`` options is ``false``, as the default is ``none`` and for some modules, ``none`` and ``false`` mean different things (https://github.com/ansible/ansible/issues/69561).
- dnf - now shows specific package changes (installations/removals) under ``results`` in check_mode. (https://github.com/ansible/ansible/issues/66132)
- iptables - reorder comment postition to be at the end (https://github.com/ansible/ansible/issues/71444).

amazon.aws
~~~~~~~~~~

- aws_caller_info - add AWSRetry decorator to automatically retry on common temporary failures (https://github.com/ansible-collections/amazon.aws/pull/208)
- aws_s3 - Add support for uploading templated content (https://github.com/ansible-collections/amazon.aws/pull/20).
- aws_secret - add "on_missing" and "on_denied" option (https://github.com/ansible-collections/amazon.aws/pull/122).
- ec2_ami - Add retries for ratelimiting related errors (https://github.com/ansible-collections/amazon.aws/pull/195).
- ec2_ami - fixed and streamlined ``max_attempts`` logic when waiting for AMI creation to finish (https://github.com/ansible-collections/amazon.aws/pull/194).
- ec2_ami - increased default ``wait_timeout`` to 1200 seconds (https://github.com/ansible-collections/amazon.aws/pull/194).
- ec2_ami_info - Add retries for ratelimiting related errors (https://github.com/ansible-collections/amazon.aws/pull/195).
- ec2_eni - Add support for tagging.
- ec2_eni - Improve reliability of the module by adding waiters and performing lookups by ENI ID rather than repeated searches (https://github.com/ansible-collections/amazon.aws/pull/180).
- ec2_eni - Port ec2_eni module to boto3 and add an integration test suite.
- ec2_eni_info - Add retries on transient AWS failures.
- ec2_eni_info - Add support for providing an ENI ID.
- ec2_eni_info - Improve reliability of the module by adding waiters and performing lookups by ENI ID rather than repeated searches (https://github.com/ansible-collections/amazon.aws/pull/180).
- ec2_group - add AWSRetry decorator to automatically retry on common temporary failures (https://github.com/ansible-collections/amazon.aws/pull/207)
- ec2_group_info - add AWSRetry decorator to automatically retry on common temporary failures (https://github.com/ansible-collections/amazon.aws/pull/207)
- ec2_snapshot_info - add AWSRetry decorator to automatically retry on common temporary failures (https://github.com/ansible-collections/amazon.aws/pull/208)
- ec2_vol - Add automatic retries on AWS rate limit errors (https://github.com/ansible-collections/amazon.aws/pull/199).
- ec2_vol - ported ec2_vol to use boto3 (https://github.com/ansible-collections/amazon.aws/pull/53).
- ec2_vpc_dhcp_option_info - add AWSRetry decorator to automatically retry on common temporary failures (https://github.com/ansible-collections/amazon.aws/pull/208)
- module_utils/core - add helper function ``scrub_none_parameters`` to remove params set to ``None`` (https://github.com/ansible-collections/community.aws/issues/251).
- module_utils/waiters - Add retries to our waiters for the same failure codes that we retry with AWSRetry (https://github.com/ansible-collections/amazon.aws/pull/185)
- s3_bucket - Add support for managing the ``public_access`` settings (https://github.com/ansible-collections/amazon.aws/pull/171).

ansible.netcommon
~~~~~~~~~~~~~~~~~

- 'prefix' added to NetworkTemplate class, inorder to handle the negate operation for vyos config commands.
- Add 'purged' to ACTION_STATES.
- Add support for json format input format for netconf modules using ``xmltodict``
- Confirmed commit fails with TypeError in IOS XR netconf plugin (https://github.com/ansible-collections/cisco.iosxr/issues/74)
- The netconf_config module now allows root tag with namespace prefix.
- Update docs for netconf_get and netconf_config examples using display=native
- cli_config: Add new return value diff which is returned when the cliconf plugin supports onbox diff
- cli_config: Clarify when commands is returned when the module is run

ansible.utils
~~~~~~~~~~~~~

- Add cli_parse module and plugins (https://github.com/ansible-collections/ansible.utils/pull/28)
- Added fact_diff plugin and sub plugin
- Added validate module/lookup/filter/test plugin to validate data based on given criteria
- Move CHANGELOG.rst file under changelogs folder as required

ansible.windows
~~~~~~~~~~~~~~~

- setup - add ``epoch_int`` option to date_time facts (https://github.com/ansible/ansible/issues/72479).
- win_environment - add ``variables`` dictionary option for setting many env vars at once (https://github.com/ansible-collections/ansible.windows/pull/113).
- win_find - Change ``hidden: yes`` to return hidden files and normal files to match the behaviour with ``find`` - https://github.com/ansible-collections/ansible.windows/issues/130
- win_service - Allow opening driver services using this module. Not all functionality is available for these types of services - https://github.com/ansible-collections/ansible.windows/issues/115

arista.eos
~~~~~~~~~~

- Added 'mode' to examples in documentation of eos_l2_interfaces.
- Added eos ospfv3 resource module (https://github.com/ansible-collections/arista.eos/pull/109).
- Added ospf_interfaces resource module. (https://github.com/ansible-collections/arista.eos/pull/125)
- Added unit test cases for eos_lldp_global module.
- Documented the necessity to use eos_interfaces and eos_l2_interfaces (for l2 configs) in eos_l3_interfaces module.
- modify short description in ospfv3 resource module.
- stop integration testing of local connection as it is deprecated.

cisco.aci
~~~~~~~~~

- Ability to add monitoring policy to epgs and anps
- Add Ansible Network ENV to fallback
- Add aci_l3out_external_path_to_member.py & aci_l3out_static_routes modules
- Add aci_node_mgmt_epg module to manage in band or out of band management EPGs
- Add aci_static_node_mgmt_address module & test file
- Add env_fallback for common connection params
- Add env_fallback for the rest of the argument spec
- Add new Subclass path support
- Add new module and test file for leaf breakout port group
- Add test file for aci_domain_to_encap_pool
- Add test file for aci_node_mgmt_epg
- Added failure message to aci_interface_policy_leaf_policy_group
- Enable/Disable infra vlan in aci_aep and its test module
- Set scope default value in aci_l3out_extsubnet
- Update README.md
- Update inventory
- aci_epg_to_domain addition of promiscuous mode (#79)
- aci_epg_to_domain moving child configs & classes to each domain type
- aci_interface_policy_port_security addition of attribute:timeout (#80)

cisco.ios
~~~~~~~~~

- Add ios_bgp_global module.
- Add ios_ospf_interfaces module.
- Add ios_ospfv3 module.

cisco.iosxr
~~~~~~~~~~~

- Added iosxr ospf_interfaces resource module (https://github.com/ansible-collections/cisco.iosxr/pull/84).
- Added iosxr ospfv3 resource module (https://github.com/ansible-collections/cisco.iosxr/pull/81).
- Platform supported coments token to be provided when invoking the object.

cisco.meraki
~~~~~~~~~~~~

- meraki_network - Update documentation to show querying of local or remote settings.
- meraki_ssid - Add Cisco ISE as a splash page option.

cisco.mso
~~~~~~~~~

- Add DHCP Policy Operations
- Add SVI MAC Addreess option in mso_schema_site_bd
- Add additional test file to add tenant from templated payload file
- Add attribute virtual_ip to mso_schema_site_bd_subnet
- Add capability for restore and download backup
- Add capability to upload backup
- Add check for undeploy under MSO version
- Add delete capability to mso_schema_site
- Add env_fallback for mso_argument_spec params
- Add error handeling test file
- Add error message to display when yaml has failed to load
- Add galaxy-importer check
- Add galaxy-importer config
- Add mso_dhcp_option_policy and mso_dhcp_option_policy_option and test files
- Add new module mso_rest and test case files to support GET api method
- Add new options to template bd and updated test file
- Add non existing template deletion test
- Add notes to use region_cidr module to create region
- Add task to undeploy the template from the site
- Add tasks in test file to remove templates for mso_schema_template_migrate
- Add test case for schema removing
- Add test cases to verify GET, PUT, POST and DELETE API methods for sites in mso_rest.py
- Add test file for mso_schema
- Add test file for mso_schema_template
- Add test file for mso_schema_template_anp
- Add test file for region module
- Add test file for site_bd_subnet
- Add test files yaml_inline and yaml_string to support YAML
- Add userAssociations to tenants to resolve CI issues
- Addition of cloud setting for ext epg
- Bump module to v1.0.1
- Changes made to payload of mso_schema_template_external_epg
- Changes to options in template bd
- Check warning
- Documentation Corrected
- Extent mso_tenant test case coverage
- Force arp flood to be true when l2unkwunicast is flood
- Make changes to display correct status code
- Modify mso library and updated test file
- Modify mso_rest test files to make PATCH available, and test other methods against schemas
- Move options for subnet from mso to the template_bd_subnet module
- Python lint corrected
- Redirect log to both stdout and log.txt file & Check warnings and errors
- Remove creation example in document of mso_schema_site_vrf_region
- Remove present state from mso_schema module
- Removed unused variable in mso_schema_site_vrf_region_hub_network
- Test DHCP Policy Provider added
- Test file for mso_dhcp_relay_policy added
- Test file for template_bd_subnet and new option foe module

cisco.nso
~~~~~~~~~

- Added See Also section to docs providing links to additional resources
- Added example for nso_action
- Corrected import paths in the test modules
- Defined data types for arguments in the docs where necessary to pass sanity tests
- Existing nso_config L3VPN example replaced with new examples due to existing example reliance on non-default l3vpn module
- Modified nso_verify module example
- Updated documentation with a See Also section providing links to NSO resources
- Updated examples for nso_show
- Updated examples in the documentation to align with the NSO DevNet Sandbox
- Verified all sanity and unit tests passing
- add GitHub Action to the repo for automated sanity and unit tests
- minor fixes to prepare for inclusion in Ansible 2.10
- nso_action can now handle YANG model choices as input parameters (https://github.com/CiscoDevNet/ansible-nso/issues/1)
- nso_config now supports setting commit flags such as "no-networking", "commit-queue", etc. (https://github.com/CiscoDevNet/ansible-nso/issues/2)
- nso_config will now return a commit_results dictionary containing the results such as commit-queue-id, rollback-id,  etc. (https://github.com/CiscoDevNet/ansible-nso/issues/3)

cisco.nxos
~~~~~~~~~~

- Add `echo_request` option for ICMP.
- Add nxos_bgp_global resource module.
- Add nxos_ospf_interfaces resource module.
- Add nxos_ospfv3 module.
- Allow other transfer protocols than scp to pull files from a NXOS device in nxos_file_copy module. sftp, http, https, tftp and ftp can be choosen as a transfer protocol, when the file_pull parameter is true..

cloudscale_ch.cloud
~~~~~~~~~~~~~~~~~~~

- Implemented identical naming support of the same resource type per zone (https://github.com/cloudscale-ch/ansible-collection-cloudscale/pull/46).
- floating_ip - Added an optional name parameter to gain idempotency. The parameter will be required for assigning a new floating IP with release of version 2.0.0 (https://github.com/cloudscale-ch/ansible-collection-cloudscale/pull/43/).
- floating_ip - Allow to reserve an IP without assignment to a server (https://github.com/cloudscale-ch/ansible-collection-cloudscale/pull/31/).
- server_group - The module has been refactored and the code simplifed (https://github.com/cloudscale-ch/ansible-collection-cloudscale/pull/23).
- volume - The module has been refactored and the code simplifed (https://github.com/cloudscale-ch/ansible-collection-cloudscale/pull/24).

community.aws
~~~~~~~~~~~~~

- aws_ssm connection plugin - Change the (internal) variable name from timeout to plugin_timeout to avoid conflicts with ansible/ansible default timeout (#69284,
- aws_ssm connection plugin - add STS token options to aws_ssm connection plugin.
- ec2_scaling_policy - Add support for step_adjustments
- ec2_scaling_policy - Migrate from boto to boto3
- ec2_vpc_igw - Add AWSRetry decorators to improve reliability (https://github.com/ansible-collections/community.aws/pull/318).
- ec2_vpc_igw - Add ``purge_tags`` parameter so that tags can be added without purging existing tags to match the collection standard tagging behaviour (https://github.com/ansible-collections/community.aws/pull/318).
- ec2_vpc_igw_info - Add AWSRetry decorators to improve reliability (https://github.com/ansible-collections/community.aws/pull/318).
- ec2_vpc_igw_info - Add ``convert_tags`` parameter so that tags can be returned in standard dict format rather than the both list of dict format (https://github.com/ansible-collections/community.aws/pull/318).
- rds_instance - set ``no_log=False`` on ``force_update_password`` to clear warning (https://github.com/ansible-collections/community.aws/issues/241).
- rds_subnet_group module - Add Boto3 support and remove Boto support.
- redshift - add support for setting tags.
- s3_lifecycle - Add support for intelligent tiering and deep archive storage classes (https://github.com/ansible-collections/community.aws/issues/270)

community.crypto
~~~~~~~~~~~~~~~~

- The ACME module_utils has been relicensed back from the Simplified BSD License (https://opensource.org/licenses/BSD-2-Clause) to the GPLv3+ (same license used by most other code in this collection). This undoes a licensing change when the original GPLv3+ licensed code was moved to module_utils in https://github.com/ansible/ansible/pull/40697 (https://github.com/ansible-collections/community.crypto/pull/165).
- The ``crypto/identify.py`` module_utils has been renamed to ``crypto/pem.py`` (https://github.com/ansible-collections/community.crypto/pull/166).
- acme_certificate - allow to pass CSR file as content with new option ``csr_content`` (https://github.com/ansible-collections/community.crypto/pull/115).
- luks_device - ``new_keyfile``, ``new_passphrase``, ``remove_keyfile`` and ``remove_passphrase`` are now idempotent (https://github.com/ansible-collections/community.crypto/issues/19, https://github.com/ansible-collections/community.crypto/pull/168).
- luks_device - allow to configure PBKDF (https://github.com/ansible-collections/community.crypto/pull/163).
- openssh_cert - add module parameter ``use_agent`` to enable using signing keys stored in ssh-agent (https://github.com/ansible-collections/community.crypto/issues/116).
- openssl_csr - refactor module to allow code re-use by openssl_csr_pipe (https://github.com/ansible-collections/community.crypto/pull/123).
- openssl_csr, openssl_csr_pipe - allow to specify CRL distribution endpoints with ``crl_distribution_points`` (https://github.com/ansible-collections/community.crypto/issues/147, https://github.com/ansible-collections/community.crypto/pull/167).
- openssl_pkcs12 - allow to specify certificate bundles in ``other_certificates`` by using new option ``other_certificates_parse_all`` (https://github.com/ansible-collections/community.crypto/issues/149, https://github.com/ansible-collections/community.crypto/pull/166).
- openssl_privatekey - refactor module to allow code re-use by openssl_privatekey_pipe (https://github.com/ansible-collections/community.crypto/pull/119).
- openssl_privatekey - the elliptic curve ``secp192r1`` now triggers a security warning. Elliptic curves of at least 224 bits should be used for new keys; see `here <https://cryptography.io/en/latest/hazmat/primitives/asymmetric/ec.html#elliptic-curves>`_ (https://github.com/ansible-collections/community.crypto/pull/132).
- x509_certificate - for the ``selfsigned`` provider, a CSR is not required anymore. If no CSR is provided, the module behaves as if a minimal CSR which only contains the public key has been provided (https://github.com/ansible-collections/community.crypto/issues/32, https://github.com/ansible-collections/community.crypto/pull/129).
- x509_certificate - refactor module to allow code re-use by x509_certificate_pipe (https://github.com/ansible-collections/community.crypto/pull/135).
- x509_certificate_info - add ``fingerprints`` return value which returns certificate fingerprints (https://github.com/ansible-collections/community.crypto/pull/121).

community.docker
~~~~~~~~~~~~~~~~

- Add collection-side support of the ``docker`` action group / module defaults group (https://github.com/ansible-collections/community.docker/pull/17).
- docker_container - added ``default_host_ip`` option which allows to explicitly set the default IP string for published ports without explicitly specified IPs. When using IPv6 binds with Docker 20.10.2 or newer, this needs to be set to an empty string (``""``) (https://github.com/ansible-collections/community.docker/issues/70, https://github.com/ansible-collections/community.docker/pull/71).
- docker_container - now supports the ``device_requests`` option, which allows to request additional resources such as GPUs (https://github.com/ansible/ansible/issues/65748, https://github.com/ansible-collections/community.general/pull/1119).
- docker_container - support specifying ``cgroup_parent`` (https://github.com/ansible-collections/community.docker/issues/6, https://github.com/ansible-collections/community.docker/pull/59).
- docker_container - when a container is started with ``detached=false``, ``status`` is now also returned when it is 0 (https://github.com/ansible-collections/community.docker/issues/26, https://github.com/ansible-collections/community.docker/pull/58).
- docker_image - return docker build output (https://github.com/ansible-collections/community.general/pull/805).
- docker_image - support ``platform`` when building images (https://github.com/ansible-collections/community.docker/issues/22, https://github.com/ansible-collections/community.docker/pull/54).
- docker_secret - add a warning when the secret does not have an ``ansible_key`` label but the ``force`` parameter is not set (https://github.com/ansible-collections/community.docker/issues/30, https://github.com/ansible-collections/community.docker/pull/31).

community.general
~~~~~~~~~~~~~~~~~

- A new filter ``lists_mergeby`` to merge two lists of dictionaries by an attribute.
  For example:

  .. code-block:: yaml

      [{'n': 'n1', 'p1': 'A', 'p2': 'F'},
       {'n': 'n2', 'p2': 'B'}] | community.general.lists_mergeby(
      [{'n': 'n1', 'p1': 'C'},
       {'n': 'n2', 'p2': 'D'},
       {'n': 'n3', 'p3': 'E'}], 'n') | list

  evaluates to

  .. code-block:: yaml

      [{'n': 'n1', 'p1': 'C', 'p2': 'F'},
       {'n': 'n2', 'p2': 'D'},
       {'n': 'n3', 'p3': 'E'}]

  (https://github.com/ansible-collections/community.general/pull/604).
- Add new filter plugin ``dict_kv`` which returns a single key-value pair from two arguments. Useful for generating complex dictionaries without using loops. For example ``'value' | community.general.dict_kv('key'))`` evaluates to ``{'key': 'value'}`` (https://github.com/ansible-collections/community.general/pull/1264).
- The collection dependencies were adjusted so that ``community.kubernetes`` is required to be of version 1.0.0 or newer (https://github.com/ansible-collections/community.general/pull/774).
- The collection is now actively tested in CI with the latest Ansible 2.9 release.
- airbrake_deployment - add ``version`` param; clarified docs on ``revision`` param (https://github.com/ansible-collections/community.general/pull/583).
- apk - added ``no_cache`` option (https://github.com/ansible-collections/community.general/pull/548).
- archive - fix parameter types (https://github.com/ansible-collections/community.general/pull/1039).
- cloudflare_dns - add support for environment variable ``CLOUDFLARE_TOKEN`` (https://github.com/ansible-collections/community.general/pull/1238).
- consul - added support for tcp checks (https://github.com/ansible-collections/community.general/issues/1128).
- datadog - mark ``notification_message`` as ``no_log`` (https://github.com/ansible-collections/community.general/pull/1338).
- datadog_monitor - add ``include_tags`` option (https://github.com/ansible/ansible/issues/57441).
- dconf - update documentation and logic code refactor (https://github.com/ansible-collections/community.general/pull/1585).
- django_manage - renamed parameter ``app_path`` to ``project_path``, adding ``app_path`` and ``chdir`` as aliases (https://github.com/ansible-collections/community.general/issues/1044).
- facter - added option for ``arguments`` (https://github.com/ansible-collections/community.general/pull/768).
- firewalld - the module has been moved to the ``ansible.posix`` collection. A redirection is active, which will be removed in version 2.0.0 (https://github.com/ansible-collections/community.general/pull/623).
- git_config - added parameter and scope ``file`` allowing user to change parameters in a custom file (https://github.com/ansible-collections/community.general/issues/1021).
- gitlab_project - add parameter ``lfs_enabled`` to specify Git LFS (https://github.com/ansible-collections/community.general/issues/1506).
- gitlab_project - add support for merge_method on projects (https://github.com/ansible/ansible/pull/66813).
- gitlab_project_variable - add support for ``environment_scope`` on projects variables (https://github.com/ansible-collections/community.general/pull/1197).
- gitlab_runner - add ``owned`` option to allow non-admin use (https://github.com/ansible-collections/community.general/pull/1491).
- gitlab_runners inventory plugin - permit environment variable input for ``server_url``, ``api_token`` and ``filter`` options (https://github.com/ansible-collections/community.general/pull/611).
- haproxy - add options to dis/enable health and agent checks.  When health and agent checks are enabled for a service, a disabled service will re-enable itself automatically.  These options also change the state of the agent checks to match the requested state for the backend (https://github.com/ansible-collections/community.general/issues/684).
- homebrew_cask - Homebrew will be deprecating use of ``brew cask`` commands as of version 2.6.0, see https://brew.sh/2020/12/01/homebrew-2.6.0/. Added logic to stop using ``brew cask`` for brew version >= 2.6.0 (https://github.com/ansible-collections/community.general/pull/1481).
- homebrew_tap - provide error message to user when module fails (https://github.com/ansible-collections/community.general/issues/1411).
- influxdb_retention_policy - add shard group duration parameter ``shard_group_duration`` (https://github.com/ansible-collections/community.general/pull/1590).
- infoblox inventory script - use stderr for reporting errors, and allow use of environment for configuration (https://github.com/ansible-collections/community.general/pull/436).
- ini_file - module now can create an empty section (https://github.com/ansible-collections/community.general/issues/479).
- ipa_host - silence warning about non-secret ``random_password`` option not having ``no_log`` set (https://github.com/ansible-collections/community.general/pull/1339).
- ipa_sudorule - added option to use command groups inside sudo rules (https://github.com/ansible-collections/community.general/issues/1555).
- ipa_user - add ``userauthtype`` option (https://github.com/ansible-collections/community.general/pull/951).
- ipa_user - silence warning about non-secret ``krbpasswordexpiration`` and ``update_password`` options not having ``no_log`` set (https://github.com/ansible-collections/community.general/pull/1339).
- iptables_state - use FQCN when calling a module from action plugin (https://github.com/ansible-collections/community.general/pull/967).
- jc - new filter to convert the output of many shell commands and file-types to JSON. Uses the jc library at https://github.com/kellyjonbrazil/jc. For example, filtering the STDOUT output of ``uname -a`` via ``{{ result.stdout | community.general.jc('uname') }}``. Requires Python 3.6+ (https://github.com/ansible-collections/community.general/pull/750).
- jira - added the traceback output to ``fail_json()`` calls deriving from exceptions (https://github.com/ansible-collections/community.general/pull/1536).
- ldap modules - allow to configure referral chasing (https://github.com/ansible-collections/community.general/pull/1618).
- linode inventory plugin - add support for ``keyed_groups``, ``groups``, and ``compose`` options (https://github.com/ansible-collections/community.general/issues/1326).
- linode inventory plugin - add support for ``tags`` option to filter instances by tag (https://github.com/ansible-collections/community.general/issues/1549).
- linode_v4 - added support for Linode StackScript usage when creating instances (https://github.com/ansible-collections/community.general/issues/723).
- log_plays callback - use v2 methods (https://github.com/ansible-collections/community.general/pull/442).
- logstash callback - add ini config (https://github.com/ansible-collections/community.general/pull/610).
- logstash callback - improve logstash message structure, needs to be enabled with the ``format_version`` option (https://github.com/ansible-collections/community.general/pull/641).
- logstash callback - migrate to python3-logstash (https://github.com/ansible-collections/community.general/pull/641).
- lvol - fix idempotency issue when using lvol with ``%VG`` or ``%PVS`` size options and VG is fully allocated (https://github.com/ansible-collections/community.general/pull/229).
- lxd_container - added support of ``--target`` flag for cluster deployments (https://github.com/ansible-collections/community.general/issues/637).
- make - add ``jobs`` parameter to allow specification of number of simultaneous jobs for make to run (https://github.com/ansible-collections/community.general/pull/1550).
- maven_artifact - added ``client_cert`` and ``client_key`` parameters to the maven_artifact module (https://github.com/ansible-collections/community.general/issues/1123).
- module_helper - added ModuleHelper class and a couple of convenience tools for module developers (https://github.com/ansible-collections/community.general/pull/1322).
- module_helper module utils - multiple convenience features added (https://github.com/ansible-collections/community.general/pull/1480).
- nagios - add the ``acknowledge`` action (https://github.com/ansible-collections/community.general/pull/820).
- nagios - add the ``host`` and ``all`` values for the ``forced_check`` action (https://github.com/ansible-collections/community.general/pull/998).
- nagios - add the ``service_check`` action (https://github.com/ansible-collections/community.general/pull/820).
- nagios - rename the ``service_check`` action to ``forced_check`` since we now are able to check both a particular service, all services of a particular host and the host itself (https://github.com/ansible-collections/community.general/pull/998).
- nios modules - clean up module argument spec processing (https://github.com/ansible-collections/community.general/pull/1598).
- nios_network - no longer requires the ansible.netcommon collection (https://github.com/ansible-collections/community.general/pull/1561).
- nmcli - add ``ipv4.routes``,  ``ipv4.route-metric`` and ``ipv4.never-default`` support (https://github.com/ansible-collections/community.general/pull/1260).
- nmcli - add ``zone`` parameter (https://github.com/ansible-collections/community.general/issues/949, https://github.com/ansible-collections/community.general/pull/1426).
- nmcli - add infiniband type support (https://github.com/ansible-collections/community.general/pull/1260).
- nmcli - refactor internal methods for simplicity and enhance reuse to support existing and future connection types (https://github.com/ansible-collections/community.general/pull/1113).
- nmcli - remove Python DBus and GTK Object library dependencies (https://github.com/ansible-collections/community.general/issues/1112).
- nmcli - the ``dns4``, ``dns4_search``, ``dns6``, and ``dns6_search`` arguments are retained internally as lists (https://github.com/ansible-collections/community.general/pull/1113).
- npm - add ``no-optional`` option (https://github.com/ansible-collections/community.general/issues/1421).
- odbc - added a parameter ``commit`` which allows users to disable the explicit commit after the execute call (https://github.com/ansible-collections/community.general/pull/1139).
- openbsd_pkg - added ``snapshot`` option (https://github.com/ansible-collections/community.general/pull/965).
- pacman - improve group expansion speed: query list of pacman groups once (https://github.com/ansible-collections/community.general/pull/349).
- pam_limits - add support for nice and priority limits (https://github.com/ansible/ansible/pull/47680).
- pam_limits - adds check mode (https://github.com/ansible-collections/community.general/issues/827).
- pam_limits - adds diff mode (https://github.com/ansible-collections/community.general/issues/828).
- parted - accept negative numbers in ``part_start`` and ``part_end``
- parted - add ``resize`` option to resize existing partitions (https://github.com/ansible-collections/community.general/pull/773).
- passwordstore lookup plugin - added ``umask`` option to set the desired file permisions on creation. This is done via the ``PASSWORD_STORE_UMASK`` environment variable (https://github.com/ansible-collections/community.general/pull/1156).
- pkgin - add support for installation of full versioned package names (https://github.com/ansible-collections/community.general/pull/1256).
- pkgng - added ``stdout`` and ``stderr`` attributes to the result (https://github.com/ansible-collections/community.general/pull/560).
- pkgng - added support for upgrading all packages using ``name: *, state: latest``, similar to other package providers (https://github.com/ansible-collections/community.general/pull/569).
- pkgng - present the ``ignore_osver`` option to pkg (https://github.com/ansible-collections/community.general/pull/1243).
- pkgutil - module can now accept a list of packages (https://github.com/ansible-collections/community.general/pull/799).
- pkgutil - module has a new option, ``force``, equivalent to the ``-f`` option to the `pkgutil <http://pkgutil.net/>`_ command (https://github.com/ansible-collections/community.general/pull/799).
- pkgutil - module now supports check mode (https://github.com/ansible-collections/community.general/pull/799).
- portage - add ``getbinpkgonly`` option, remove unnecessary note on internal portage behaviour (getbinpkg=yes), and remove the undocumented exclusiveness of the pkg options as portage makes no such restriction (https://github.com/ansible-collections/community.general/pull/1169).
- proxmox - add ``features`` option to LXC (https://github.com/ansible-collections/community.general/issues/816).
- proxmox - add new ``proxmox_default_behavior`` option (https://github.com/ansible-collections/community.general/pull/850).
- proxmox - add support for API tokens (https://github.com/ansible-collections/community.general/pull/1206).
- proxmox - extract common code and documentation (https://github.com/ansible-collections/community.general/pull/1331).
- proxmox - improve and extract more common documentation (https://github.com/ansible-collections/community.general/pull/1404).
- proxmox inventory plugin - add environment variable passthrough (https://github.com/ansible-collections/community.general/pull/1645).
- proxmox inventory plugin - ignore QEMU templates altogether instead of skipping the creation of the host in the inventory (https://github.com/ansible-collections/community.general/pull/1185).
- proxmox_kvm - add cloud-init support (new options: ``cicustom``, ``cipassword``, ``citype``, ``ciuser``, ``ipconfig``, ``nameservers``, ``searchdomains``, ``sshkeys``) (https://github.com/ansible-collections/community.general/pull/797).
- proxmox_kvm - add new ``proxmox_default_behavior`` option (https://github.com/ansible-collections/community.general/pull/850).
- proxmox_kvm - add support for API tokens (https://github.com/ansible-collections/community.general/pull/1206).
- proxmox_kvm - improve and extract more common documentation (https://github.com/ansible-collections/community.general/pull/1404).
- proxmox_kvm - improve code readability (https://github.com/ansible-collections/community.general/pull/934).
- proxmox_template - add support for API tokens (https://github.com/ansible-collections/community.general/pull/1206).
- proxmox_template - download proxmox applicance templates (pveam) (https://github.com/ansible-collections/community.general/pull/1046).
- proxmox_template - improve documentation (https://github.com/ansible-collections/community.general/pull/1404).
- pushover - add device parameter (https://github.com/ansible-collections/community.general/pull/802).
- redfish_command - add sub-command for ``EnableContinuousBootOverride`` and ``DisableBootOverride`` to allow setting BootSourceOverrideEnabled Redfish property (https://github.com/ansible-collections/community.general/issues/824).
- redfish_command - support same reset actions on Managers as on Systems (https://github.com/ansible-collections/community.general/issues/901).
- redis cache plugin - add redis sentinel functionality to cache plugin (https://github.com/ansible-collections/community.general/pull/1055).
- redis cache plugin - make the redis cache keyset name configurable (https://github.com/ansible-collections/community.general/pull/1036).
- rhn_register - added ``force`` parameter to allow forced registering (https://github.com/ansible-collections/community.general/issues/1454).
- rundeck_acl_policy - add check for rundeck_acl_policy name parameter (https://github.com/ansible-collections/community.general/pull/612).
- scaleway modules and inventory plugin - update regions and zones to add the new ones (https://github.com/ansible-collections/community.general/pull/1690).
- slack - add support for sending messages built with block kit (https://github.com/ansible-collections/community.general/issues/380).
- slack - add support for updating messages (https://github.com/ansible-collections/community.general/issues/304).
- splunk callback - add an option to allow not to validate certificate from HEC (https://github.com/ansible-collections/community.general/pull/596).
- splunk callback - new parameter ``include_milliseconds`` to add milliseconds to existing timestamp field (https://github.com/ansible-collections/community.general/pull/1462).
- telegram - now can call any methods in Telegram bot API. Previously this module was hardcoded to use "SendMessage" only. Usage of "SendMessage" API method was also librated, and now you can specify any arguments you need, for example, "disable_notificaton" (https://github.com/ansible-collections/community.general/pull/1642).
- terraform - add ``init_reconfigure`` option, which controls the ``-reconfigure`` flag (backend reconfiguration) (https://github.com/ansible-collections/community.general/pull/823).
- xfconf - add arrays support (https://github.com/ansible/ansible/issues/46308).
- xfconf - add support for ``double`` type (https://github.com/ansible-collections/community.general/pull/744).
- xfconf - add support for ``uint`` type (https://github.com/ansible-collections/community.general/pull/696).
- xfconf - removed unnecessary second execution of ``xfconf-query`` (https://github.com/ansible-collections/community.general/pull/1305).
- xml - fixed issue were changed was returned when removing non-existent xpath (https://github.com/ansible-collections/community.general/pull/1007).
- zypper_repository - proper failure when python-xml is missing (https://github.com/ansible-collections/community.general/pull/939).

community.grafana
~~~~~~~~~~~~~~~~~

- Update the version where `message` alias will disappear from `grafana_dashboard`. (Now 2.0.0)

community.hashi_vault
~~~~~~~~~~~~~~~~~~~~~

- Add optional ``aws_iam_server_id`` parameter as the value for ``X-Vault-AWS-IAM-Server-ID`` header (https://github.com/ansible-collections/community.hashi_vault/pull/27).
- hashi_vault - ``ANSIBLE_HASHI_VAULT_ADDR`` environment variable added for option ``url`` (https://github.com/ansible-collections/community.hashi_vault/issues/8).
- hashi_vault - ``ANSIBLE_HASHI_VAULT_AUTH_METHOD`` environment variable added for option ``auth_method`` (https://github.com/ansible-collections/community.hashi_vault/issues/17).
- hashi_vault - ``ANSIBLE_HASHI_VAULT_ROLE_ID`` environment variable added for option ``role_id`` (https://github.com/ansible-collections/community.hashi_vault/issues/20).
- hashi_vault - ``ANSIBLE_HASHI_VAULT_SECRET_ID`` environment variable added for option ``secret_id`` (https://github.com/ansible-collections/community.hashi_vault/issues/20).
- hashi_vault - ``ANSIBLE_HASHI_VAULT_TOKEN_FILE`` environment variable added for option ``token_file`` (https://github.com/ansible-collections/community.hashi_vault/issues/15).
- hashi_vault - ``ANSIBLE_HASHI_VAULT_TOKEN_PATH`` environment variable added for option ``token_path`` (https://github.com/ansible-collections/community.hashi_vault/issues/15).
- hashi_vault - ``namespace`` parameter can be specified in INI or via env vars ``ANSIBLE_HASHI_VAULT_NAMESPACE`` (new) and ``VAULT_NAMESPACE`` (lower preference)  (https://github.com/ansible-collections/community.hashi_vault/issues/14).
- hashi_vault - ``token`` parameter can now be specified via ``ANSIBLE_HASHI_VAULT_TOKEN`` as well as via ``VAULT_TOKEN`` (the latter with lower preference) (https://github.com/ansible-collections/community.hashi_vault/issues/16).
- hashi_vault - add ``token_validate`` option to control token validation (https://github.com/ansible-collections/community.hashi_vault/pull/24).
- hashi_vault - uses new AppRole method in hvac 0.10.6 with fallback to deprecated method with warning (https://github.com/ansible-collections/community.hashi_vault/pull/33).

community.kubernetes
~~~~~~~~~~~~~~~~~~~~

- Add Makefile and downstream build script for kubernetes.core (https://github.com/ansible-collections/community.kubernetes/pull/197).
- Add execution environment metadata (https://github.com/ansible-collections/community.kubernetes/pull/211).
- Add probot stale bot configuration to autoclose issues (https://github.com/ansible-collections/community.kubernetes/pull/196).
- Added a contribution guide (https://github.com/ansible-collections/community.kubernetes/pull/192).
- Refactor module_utils (https://github.com/ansible-collections/community.kubernetes/pull/223).
- Replace KubernetesAnsibleModule class with dummy class (https://github.com/ansible-collections/community.kubernetes/pull/227).
- Replace KubernetesRawModule class with K8sAnsibleMixin (https://github.com/ansible-collections/community.kubernetes/pull/231).
- common - Do not mark task as changed when diff is irrelevant (https://github.com/ansible-collections/community.kubernetes/pull/228).
- helm - Add appVersion idempotence check to Helm (https://github.com/ansible-collections/community.kubernetes/pull/246).
- helm - Return status in check mode (https://github.com/ansible-collections/community.kubernetes/pull/192).
- helm - Support for single or multiple values files (https://github.com/ansible-collections/community.kubernetes/pull/93).
- helm_* - Support vaulted kubeconfig (https://github.com/ansible-collections/community.kubernetes/pull/229).
- k8s - SelfSubjectAccessReviews supported when 405 response received (https://github.com/ansible-collections/community.kubernetes/pull/237).
- k8s - add testcase for adding multiple resources using template parameter (https://github.com/ansible-collections/community.kubernetes/issues/243).
- k8s_info - Add support for wait (https://github.com/ansible-collections/community.kubernetes/pull/235).
- k8s_info - update custom resource example (https://github.com/ansible-collections/community.kubernetes/issues/202).
- kubectl plugin - correct console log (https://github.com/ansible-collections/community.kubernetes/issues/200).
- raw - Handle exception raised by underlying APIs (https://github.com/ansible-collections/community.kubernetes/pull/180).

community.mysql
~~~~~~~~~~~~~~~

- mysql modules - add the ``check_hostname`` option (https://github.com/ansible-collections/community.mysql/issues/28).
- mysql modules - patch the ``Connection`` class to add a destructor that ensures connections to the server are explicitly closed (https://github.com/ansible-collections/community.mysql/pull/44).
- mysql_query - simple refactoring of query type check (https://github.com/ansible-collections/community.mysql/pull/58).
- mysql_user - refactor to reduce cursor.execute() calls in preparation for adding query logging (https://github.com/ansible-collections/community.mysql/pull/76).
- mysql_user - simple refactoring of priv type check (https://github.com/ansible-collections/community.mysql/pull/58).

community.network
~~~~~~~~~~~~~~~~~

- cnos terminal plugin - prevent timeout connection failure by adding "no logging terminal" after log in (https://github.com/ansible-collections/community.network/pull/16).
- edgeos_config - added diff result when applying configuration changes (https://github.com/ansible-collections/community.network/pull/184).
- edgeswitch_facts - added ``startupconfig`` to facts module - to allow the comparision between startup and running config (https://github.com/ansible-collections/community.network/pull/105).

community.okd
~~~~~~~~~~~~~

- Add a contribution guide (https://github.com/ansible-collections/community.okd/pull/37).
- Add incluster Makefile target for CI (https://github.com/ansible-collections/community.okd/pull/13).
- Add tests for inventory plugin (https://github.com/ansible-collections/community.okd/pull/16).
- CI Documentation for working with Prow (https://github.com/ansible-collections/community.okd/pull/15).
- Docker container can run as an arbitrary user (https://github.com/ansible-collections/community.okd/pull/12).
- Dockerfile now is properly set up to run tests in a rootless container (https://github.com/ansible-collections/community.okd/pull/11).
- Integrate stale bot for issue queue maintenance (https://github.com/ansible-collections/community.okd/pull/14).
- Released version 1 to Automation Hub as redhat.openshift (https://github.com/ansible-collections/community.okd/issues/51).
- Use the API Group APIVersion for the `Route` object (https://github.com/ansible-collections/community.okd/pull/27).

community.postgresql
~~~~~~~~~~~~~~~~~~~~

- postgresql_info - add ``in_recovery`` return value to show if a service in recovery mode or not (https://github.com/ansible-collections/community.general/issues/1068).
- postgresql_privs - add ``procedure`` type support (https://github.com/ansible-collections/community.general/issues/1002).
- postgresql_query - add ``as_single_query`` option to execute a script content as a single query to avoid semicolon related errors (https://github.com/ansible-collections/community.postgresql/pull/37).
- postgresql_query - add ``query_list`` and ``query_all_results`` return values (https://github.com/ansible-collections/community.general/issues/838).

community.routeros
~~~~~~~~~~~~~~~~~~

- command - added support for a dash (``-``) in username (https://github.com/ansible-collections/community.routeros/pull/18).
- facts - added support for a dash (``-``) in username (https://github.com/ansible-collections/community.routeros/pull/18).
- facts - now also collecting data about BGP and OSPF (https://github.com/ansible-collections/community.network/pull/101).
- facts - set configuration export on to verbose, for full configuration export (https://github.com/ansible-collections/community.network/pull/104).

community.sops
~~~~~~~~~~~~~~

- All plugins and modules: allow to pass generic sops options with new options ``config_path``, ``enable_local_keyservice``, ``keyservice``. Also allow to pass AWS parameters with options ``aws_profile``, ``aws_access_key_id``, ``aws_secret_access_key``, and ``aws_session_token`` (https://github.com/ansible-collections/community.sops/pull/47).
- community.sops.sops lookup plugin - add ``empty_on_not_exist`` option which allows to return an empty string instead of an error when the file does not exist (https://github.com/ansible-collections/community.sops/pull/33).
- community.sops.sops vars plugin - add option to control caching (https://github.com/ansible-collections/community.sops/pull/32).
- community.sops.sops vars plugin - add option to determine when vars are loaded (https://github.com/ansible-collections/community.sops/pull/32).
- community.sops.sops_encrypt - allow to pass encryption-specific options ``kms``, ``gcp_kms``, ``azure_kv``, ``hc_vault_transit``, ``pgp``, ``unencrypted_suffix``, ``encrypted_suffix``, ``unencrypted_regex``, ``encrypted_regex``, ``encryption_context``, and ``shamir_secret_sharing_threshold`` to sops (https://github.com/ansible-collections/community.sops/pull/47).

community.vmware
~~~~~~~~~~~~~~~~

- module_utils/vmware - Ignore leading and trailing whitespace when searching for objects (https://github.com/ansible-collections/vmware/issues/335)
- vmware_category - add additional associable object types (https://github.com/ansible-collections/community.vmware/issues/454).
- vmware_cluster_info - Fixed issue of a cluster name doesn't URL-decode(https://github.com/ansible-collections/vmware/pull/366)
- vmware_cluster_info - added a parent datacenter name of Cluster to the return value (https://github.com/ansible-collections/community.vmware/pull/591).
- vmware_content_deploy_ovf_template - added new parameter "content_library" to get the OVF template from (https://github.com/ansible-collections/community.vmware/issues/514).
- vmware_content_deploy_ovf_template - consistent ``eagerZeroedThick`` value (https://github.com/ansible-collections/community.vmware/issues/618).
- vmware_content_deploy_template - add datastore cluster parameter (https://github.com/ansible-collections/community.vmware/issues/397).
- vmware_content_deploy_template - make resource pool, host, cluster, datastore optional parameter and add check (https://github.com/ansible-collections/community.vmware/issues/397).
- vmware_drs_group - code refactor (https://github.com/ansible-collections/community.vmware/pull/475).
- vmware_dvswitch - Added support to create vds version 7.0.0.
- vmware_guest - Define sub-options of hardware and customization in argument_spec (https://github.com/ansible-collections/community.vmware/issues/555).
- vmware_guest - Fixed issue of checking hardware version when set VBS(https://github.com/ansible-collections/community.vmware/issues/351)
- vmware_guest - Fixed issue of comparing latest hardware version str type with int(https://github.com/ansible-collections/community.vmware/issues/381)
- vmware_guest - add documentation for networks parameters connected and start_connected (https://github.com/ansible-collections/community.vmware/issues/507).
- vmware_guest - takes now into account the ``esxi_hostname`` argument to create the vm on the right host according to the doc (https://github.com/ansible-collections/vmware/pull/359).
- vmware_guest_controller - error handling in task exception.
- vmware_guest_custom_attributes - Fixed issue when trying to set a VM custom attribute when there are custom attributes with the same name for other object types (https://github.com/ansible-collections/community.vmware/issues/412).
- vmware_guest_customization_info - Fixed to get values properly for LinuxPrep and SysPrep parameters(https://github.com/ansible-collections/vmware/pull/368)
- vmware_guest_disk - add new parameters controller_type and controller_number for supporting SATA and NVMe disk (https://github.com/ansible-collections/vmware/issues/196).
- vmware_guest_file_operation - provide useful error message when exception occurs (https://github.com/ansible-collections/community.vmware/issues/485).
- vmware_guest_info - Fix get tags API call (https://github.com/ansible-collections/community.vmware/issues/403).
- vmware_guest_info - added a new parameter to gather detailed information about tag from the given virtual machine.
- vmware_guest_network - Fixed to port group changes to work properly and NSX-T port group supported(https://github.com/ansible-collections/community.vmware/pull/401).
- vmware_guest_network - add support for private vlan id (https://github.com/ansible-collections/community.vmware/pull/511).
- vmware_guest_register_operation - supported the check_mode
- vmware_guest_video - gather facts for video devices even if the virtual machine is poweredoff (https://github.com/ansible-collections/community.vmware/issues/408).
- vmware_host - added a new state option, the ``disconnected`` (https://github.com/ansible-collections/community.vmware/pull/589).
- vmware_host_facts - Add ESXi host current time info in returned host facts(https://github.com/ansible-collections/community.vmware/issues/527)
- vmware_host_iscsi - added a name(iqn) changing option for iSCSI (https://github.com/ansible-collections/community.vmware/pull/617).
- vmware_host_iscsi_info - a new module for the ESXi hosts that is dedicated to gathering information of the iSCSI configuration(https://github.com/ansible-collections/community.vmware/pull/402).
- vmware_host_lockdown - Support check mode (https://github.com/ansible-collections/community.vmware/pull/633).
- vmware_object_role_permission - add missing required fields of hostname, username, and password to module examples (https://github.com/ansible-collections/community.vmware/issues/426).
- vmware_resource_pool - add new allocation shares options for cpu and memory(https://github.com/ansible-collections/community.vmware/pull/461).
- vmware_resource_pool - manage resource pools on ESXi hosts (https://github.com/ansible-collections/community.vmware/issues/492).
- vmware_resource_pool - relabel the change introduced in 1.5.0 as Minor Changes (https://github.com/ansible-collections/community.vmware/issues/540).
- vmware_vm_inventory - skip inaccessible vm configuration.
- vmware_vm_inventory - support for categories and tag, category relation (https://github.com/ansible-collections/community.vmware/issues/350).
- vmware_vm_inventory - update requirements doc.
- vmware_vsan_health_info - add new parameter to support datacenter.

community.windows
~~~~~~~~~~~~~~~~~

- win_dns_record - Support NS record creation,modification and deletion
- win_firewall - Support defining the default inbound and outbound action of traffic in Windows firewall.
- win_nssm - added new parameter 'app_environment' for managing service environment.
- win_psrepository - Added the ``proxy`` option that defines the proxy to use for the repository being managed
- win_scheduled_task - validate task name against invalid characters (https://github.com/ansible-collections/community.windows/pull/168)
- win_scheduled_task_stat - add check mode support (https://github.com/ansible-collections/community.windows/pull/167)

community.zabbix
~~~~~~~~~~~~~~~~

- Updated the roles to support Zabbix 5.2.
- all roles - added ``zabbix_{agent,web,server,proxy,javagateway}_conf_mode`` option for configuring a mode of the configuration file for each Zabbix service.
- zabbix_agent - Added a new property `zabbix_agent_dont_detect_ip` when set to true, it won't detect the ips and no need to install the python module `netaddr`.
- zabbix_agent - Added parameter `zabbix_agent_package_remove` when set to `true` and `zabbix_agent2` is set to `true` it will uninstall the `zabbix-agent` service and package.
- zabbix_agent - added `zabbix_agent_install_agent_only` Will only install the Zabbix Agent package and not the `zabbix-sender` or `zabbix-get` packages.
- zabbix_proxy (role) - added an option ``innodb_default_row_format`` for MariaDB/MySQL if it isn't set to ``dynamic``.
- zabbix_server - fixed installation output when using MySQL database to not print PostgreSQL.
- zabbix_template - Fixed to decode Unicode Escape of multibyte strings in an importing template data(https://github.com/ansible-collections/community.zabbix/pull/226).
- zabbix_user - ``passwd`` no longer required when ALL groups in ``usrgrps`` use LDAP as ``gui_access`` (see `#240 <https://github.com/ansible-collections/community.zabbix/issues/232>`_).
- zabbix_user - added new parameters to set timezone and role_name for users (https://github.com/ansible-collections/community.zabbix/pull/260).
- zabbix_user - no longer requires ``usrgrps`` when ``state=absent`` (see `#240 <https://github.com/ansible-collections/community.zabbix/issues/232>`_).
- zabbix_user - user_medias now defaults to None and is optional (https://github.com/ansible-collections/community.zabbix/pull/264).
- zabbix_web - added `zabbix_web_rhel_release` which enable scl on RHEL (https://github.com/ansible-collections/community.zabbix/pull/266).
- zabbix_web - added several configuration options for the PHP-FPM setup to configure the listen (socket) file.
- zabbix_web - added support for configuring Zabbix Web with Nginx, same way as with Apache.
- zabbix_web - quality of life improvements when using Nginx (https://github.com/ansible-collections/community.zabbix/pull/304).

containers.podman
~~~~~~~~~~~~~~~~~

- Create podman_network module for podman networks management
- podman_container - Add log level for Podman in module
- podman_container - Add mac_address field to podman_container module
- podman_container - Add strict image compare with hashes
- podman_container - Improve compatibility with docker_container by adding aliases
- podman_container - Move containers logic to module utils
- podman_image - reuse existing results in present()
- podman_network - Add IPv6 to network
- podman_network - Add support of network options like MTU, VLAN
- podman_pod - Move pod logic to separate library

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- Coding Guidelines, Contributor Agreement, and Code of Conduct files are added to the collection.
- New deprecation changes for ``dellemc_get_system_inventory`` and ``dellemc_get_firmware_inventory`` ignored for ansible 2.9 sanity test.
- The idrac_server_config_profile module supports IPv6 address format.
- The idrac_server_config_profile module supports a user provided file name for an export operation.
- The modules are standardized as per ansible guidelines.

dellemc.os10
~~~~~~~~~~~~

- Adding support for Ansible version 2.9 (https://github.com/ansible-collections/dellemc.os10/pull/58)
- Enhanced os10_bgp role to support internal BGP redistribution under address-family for V4 and V6
- Enhanced os10_bgp role to support maximum-prefix configuration under BGP peer and peer-group.
- os10_ntp role - Added support for vrf and sha1 and sha2-256 authentication-key types
- os10_snmp role - Added support for source-interface and vrf
- os10_template - add template for show spanning tree compatibility mode
- os10_template - add template for show vlt error disabled ports
- os10_uplink role - Added support for downstream disable-links and auto-recover

f5networks.f5_modules
~~~~~~~~~~~~~~~~~~~~~

- Add AS3 declaration information to the bigip_device_info module
- Add AS3, TS, CFE, and DO information to the bigip_device_info module
- Add CFE declaration information to the bigip_device_info module
- Add DO declaration information to the bigip_device_info module
- Add TS declaration information to the bigip_device_info module
- Add access policy information to the bigip_device_info module
- Add access profile information to the bigip_device_info module
- Add better error handling for TEEM telemetry connection
- Add meaningful error message for the wait_for parameter in the bigip_command module
- Add parent_policies and policies_pending_changes information parameters to obtain when gathering asm-policy-stats
- Add remote_syslog information to the bigip_device_info module.
- Add renewal option to the bigip_device_license module
- Add reuse_objects parameter to the bigip_apm_policy_import module
- Add sync-status information to the bigip_device_info module
- Add the ability to import API Protection policies to the bigip_apm_policy_import module
- Added apply information parameter to indicate if an ASM policy has pending changes that need to be applied.
- Changed apm_policy_fetch module to use standard download function
- Changed the meaning of policies_active and policies_inactive stat information due to changes in TMOS 13.x
- New bigip_ssl_key_cert module to manage SSL certificates and keys with the transaction interface

hetzner.hcloud
~~~~~~~~~~~~~~

- Dynamic Inventory Add option to specifiy the token_env variable which is used for identification if now token is set
- Improve imports of API Exception
- hcloud_floating_ip Allow creating Floating IP with protection
- hcloud_load_balancer Allow creating Load Balancer with protection
- hcloud_network Allow creating Network with protection
- hcloud_server Allow creating server with protection
- hcloud_server_network Allow updating alias ips
- hcloud_subnetwork Allow creating vswitch subnetworks
- hcloud_volume Allow creating Volumes with protection

inspur.sm
~~~~~~~~~

- Add CODE_OF_CONDUCT.md file.
- Add a meta/runtime.yml file.
- Add the code of conduct to the README.md file.
- Delete the Collections imported in the adapter_info.py.
- Delete the Collections imported in the module.
- Documentation, examples, and return use FQCNs to M(..).
- Modified version information to 1.1.1 in galaxy.yml.
- Modify ansible_test.yml to add push trigger rule.
- Modify ansibled-test. yml file, add timing execution script, run environment only keep Python 3.8 version.
- Modify inspur_sm_sdk in README.md to inspursmsdk.
- Modify paybooks,Using FQCN.
- Modify the README.md file to add Ansible Code of Conduct (COC).
- Modify the README.md file to add content for releasing, versioning and deprecation(https://github.com/ISIB-Group/inspur.sm/issues/27).
- Modify the README.md file to change the supported Anible version to 2.10.0
- Modify the ansible-test.yml file to Remove the Python Version from the Run sanity tests.
- Modify the ansible-test.yml file to add Ansible and Python versions.
- Modify the description of Ansible in README.md.
- Modify the format of DOCUMENTATION on Required in the module.
- Modify the github repository path referenced in galaxy.yml.
- Modify the module_utils/ism.py file to add check mode processing.
- Modify the state of chenged in the module when the operation changes.
- Modify the value of supports_check_mode in the module to False.
- Regenerate the.rst file.

junipernetworks.junos
~~~~~~~~~~~~~~~~~~~~~

- Add junos bgp global resource module.
- Add ospf interfaces resource module.
- Add ospfv3 resource module.
- Use FQCN to M() references in modules documentation (https://github.com/ansible-collections/junipernetworks.junos/pull/79)

kubernetes.core
~~~~~~~~~~~~~~~

- Add Makefile and downstream build script for kubernetes.core (https://github.com/ansible-collections/kubernetes.core/pull/197).
- Add action groups for playbooks with module_defaults (https://github.com/ansible-collections/kubernetes.core/pull/107).
- Add execution environment metadata (https://github.com/ansible-collections/kubernetes.core/pull/211).
- Add probot stale bot configuration to autoclose issues (https://github.com/ansible-collections/kubernetes.core/pull/196).
- Add requires_ansible version constraints to runtime.yml (https://github.com/ansible-collections/kubernetes.core/pull/126).
- Add sanity test ignore file for Ansible 2.11 (https://github.com/ansible-collections/kubernetes.core/pull/130).
- Add test for openshift apply bug (https://github.com/ansible-collections/kubernetes.core/pull/94).
- Add version_added to each new collection module (https://github.com/ansible-collections/kubernetes.core/pull/98).
- Added a contribution guide (https://github.com/ansible-collections/kubernetes.core/pull/192).
- Check Python code using flake8 (https://github.com/ansible-collections/kubernetes.core/pull/123).
- Don't require project coverage check on PRs (https://github.com/ansible-collections/kubernetes.core/pull/102).
- Ensure check mode results are as expected (https://github.com/ansible-collections/kubernetes.core/pull/155).
- Improve k8s Deployment and Daemonset wait conditions (https://github.com/ansible-collections/kubernetes.core/pull/35).
- Minor documentation fixes and use of FQCN in some examples (https://github.com/ansible-collections/kubernetes.core/pull/114).
- Refactor module_utils (https://github.com/ansible-collections/kubernetes.core/pull/223).
- Remove action_groups_redirection entry from meta/runtime.yml (https://github.com/ansible-collections/kubernetes.core/pull/127).
- Remove deprecated ANSIBLE_METADATA field (https://github.com/ansible-collections/kubernetes.core/pull/95).
- Rename repository to ``kubernetes.core`` (https://github.com/ansible-collections/kubernetes.core/pull/81).
- Replace KubernetesAnsibleModule class with dummy class (https://github.com/ansible-collections/kubernetes.core/pull/227).
- Replace KubernetesRawModule class with K8sAnsibleMixin (https://github.com/ansible-collections/kubernetes.core/pull/231).
- Update base branch to 'main' (https://github.com/ansible-collections/kubernetes.core/issues/148).
- Use FQCN in module docs and plugin examples (https://github.com/ansible-collections/kubernetes.core/pull/146).
- Use improved kubernetes diffs where possible (https://github.com/ansible-collections/kubernetes.core/pull/105).
- common - Do not mark task as changed when diff is irrelevant (https://github.com/ansible-collections/kubernetes.core/pull/228).
- helm - Add appVersion idempotence check to Helm (https://github.com/ansible-collections/kubernetes.core/pull/246).
- helm - Add support for K8S_AUTH_CONTEXT, K8S_AUTH_KUBECONFIG env (https://github.com/ansible-collections/kubernetes.core/pull/141).
- helm - Allow creating namespaces with Helm (https://github.com/ansible-collections/kubernetes.core/pull/157).
- helm - Return status in check mode (https://github.com/ansible-collections/kubernetes.core/pull/192).
- helm - Support for single or multiple values files (https://github.com/ansible-collections/kubernetes.core/pull/93).
- helm - add 'atomic' option (https://github.com/ansible-collections/kubernetes.core/pull/115).
- helm - add aliases context for kube_context (https://github.com/ansible-collections/kubernetes.core/pull/152).
- helm - add support for K8S_AUTH_KUBECONFIG and K8S_AUTH_CONTEXT environment variable (https://github.com/ansible-collections/kubernetes.core/issues/140).
- helm - minor code refactoring (https://github.com/ansible-collections/kubernetes.core/pull/110).
- helm_* - Support vaulted kubeconfig (https://github.com/ansible-collections/kubernetes.core/pull/229).
- helm_info - add aliases context for kube_context (https://github.com/ansible-collections/kubernetes.core/pull/152).
- helm_info - add support for K8S_AUTH_KUBECONFIG and K8S_AUTH_CONTEXT environment variable (https://github.com/ansible-collections/kubernetes.core/issues/140).
- helm_info and helm_repository - minor code refactor (https://github.com/ansible-collections/kubernetes.core/pull/117).
- k8s - Added ``persist_config`` option for persisting refreshed tokens (https://github.com/ansible-collections/kubernetes.core/issues/49).
- k8s - Handle set object retrieved from lookup plugin (https://github.com/ansible-collections/kubernetes.core/pull/118).
- k8s - SelfSubjectAccessReviews supported when 405 response received (https://github.com/ansible-collections/kubernetes.core/pull/237).
- k8s - add testcase for adding multiple resources using template parameter (https://github.com/ansible-collections/kubernetes.core/issues/243).
- k8s_exec - return RC for the command executed (https://github.com/ansible-collections/kubernetes.core/issues/122).
- k8s_info - Add support for wait (https://github.com/ansible-collections/kubernetes.core/pull/235).
- k8s_info - Update example using vars (https://github.com/ansible-collections/kubernetes.core/pull/156).
- k8s_info - update custom resource example (https://github.com/ansible-collections/kubernetes.core/issues/202).
- kubectl plugin - correct console log (https://github.com/ansible-collections/kubernetes.core/issues/200).
- raw - Handle exception raised by underlying APIs (https://github.com/ansible-collections/kubernetes.core/pull/180).

netapp.elementsw
~~~~~~~~~~~~~~~~

- na_elementsw_cluster - add new options ``encryption``, ``order_number``, and ``serial_number``.
- na_elementsw_network_interfaces - make all options not required, so that only bond_1g can be set for example.
- na_elementsw_network_interfaces - restructure options into 2 dictionaries ``bond_1g`` and ``bond_10g``, so that there is no shared option.  Disallow all older options.
- na_elementsw_node - ``cluster_name`` to set the cluster name on new nodes.
- na_elementsw_node - ``preset_only`` to only set the cluster name before creating a cluster with na_elementsw_cluster.
- na_elementsw_volume - ``qos_policy_name`` to provide a QOS policy name or ID.

netapp.ontap
~~~~~~~~~~~~

- all ZAPI modules - new ``classic_basic_authorization`` feature_flag to disable adding Authorization header proactively.
- all ZAPI modules - optimize Basic Authentication by adding Authorization header proactively.
- general - improve error reporting when older version of netapp-lib is used.
- na_ontap_cifs - output ``modified`` if a modify action is taken.
- na_ontap_cluster - ``node_name`` to set the node name when adding a node, or as an alternative to `cluster_ip_address`` to remove a node.
- na_ontap_cluster - ``state`` can be set to ``absent`` to remove a node identified with ``cluster_ip_address`` or ``node_name``.
- na_ontap_cluster - ``time_out`` to wait for cluster creation, adding and removing a node.
- na_ontap_cluster_peer - optional parameter ``ipspace`` added for cluster peer.
- na_ontap_debug - connection diagnostics added for invalid ipaddress and DNS hostname errors.
- na_ontap_export_policy_rule - minor doc updates.
- na_ontap_firmware_upgrade - new option for firmware type ``storage`` added.
- na_ontap_igroup - new option ``os_type`` to replace ``ostype`` (but ostype is still accepted).
- na_ontap_info - New options ``cifs_options_info``, ``cluster_log_forwarding_info``, ``event_notification_destination_info``, ``event_notification_info``, ``security_login_role_config_info``, ``security_login_role_info`` have been added.
- na_ontap_info - deprecate ``state`` option.
- na_ontap_info - do not require write access privileges.   This also enables other modules to work in check_mode without write access permissions.
- na_ontap_interface - minor example update.
- na_ontap_lun - ``use_exact_size`` to create a lun with the exact given size so that the lun is not rounded up.
- na_ontap_lun - new option ``from_name`` to rename a LUN.
- na_ontap_lun - new option ``os_type`` to replace ``ostype`` (but ostype is still accepted), and removed default to ``image``.
- na_ontap_lun - new option ``qos_policy_group`` to assign a qos_policy_group to a LUN.
- na_ontap_lun - new option ``san_application_template`` to create LUNs without explicitly creating a volume and using REST APIs.
- na_ontap_lun - new options ``total_size`` and ``total_size_unit`` when using SAN application template.
- na_ontap_lun - support increasing lun_count and total_size when using SAN application template.
- na_ontap_lun - support modify for space_allocation and space_reserve.
- na_ontap_mcc_mediator - improve error reporting when REST is not available.
- na_ontap_metrocluster - improve error reporting when REST is not available.
- na_ontap_qos_policy_group - new option ``is_shared`` for sharing QOS SLOs or not.
- na_ontap_qtree - ``wait_for_completion`` and ``time_out`` to wait for qtree deletion when using REST.
- na_ontap_quota - allow to turn quota on/off without providing quota_target or type.
- na_ontap_quota_policy - new option ``auto_assign`` to assign quota policy to vserver.
- na_ontap_quotas - New option ``activate_quota_on_change`` to resize or reinitialize quotas.
- na_ontap_quotas - New option ``perform_user_mapping`` to perform user mapping for the user specified in quota-target.
- na_ontap_quotas - ``soft_disk_limit`` and ``soft_file_limit`` for the quota target.
- na_ontap_rest_info - Support for gather subsets - ``application_info, application_template_info, autosupport_config_info , autosupport_messages_history, ontap_system_version, storage_flexcaches_info, storage_flexcaches_origin_info, storage_ports_info, storage_qos_policies, storage_qtrees_config, storage_quota_reports, storage_quota_policy_rules, storage_shelves_config, storage_snapshot_policies, support_ems_config, support_ems_events, support_ems_filters``
- na_ontap_rest_info - Support for gather subsets - ``cifs_home_directory_info, cluster_software_download, event_notification_info, event_notification_destination_info, security_login_info, security_login_rest_role_info``
- na_ontap_rest_info - Support for gather subsets - ``initiator_groups_info, san_fcp_services, san_iscsi_credentials, san_iscsi_services, san_lun_maps, storage_luns_info, storage_NVMe_namespaces.``
- na_ontap_rest_info - deprecate ``state`` option.
- na_ontap_snapmirror - new option ``create_destination`` to automatically create destination endpoint (ONTAP 9.7).
- na_ontap_snapmirror - new option ``destination_cluster`` to automatically create destination SVM for SVM DR (ONTAP 9.7).
- na_ontap_snapmirror - new option ``source_cluster`` to automatically set SVM peering (ONTAP 9.7).
- na_ontap_snapmirror - use REST API for create action if target supports it.  (ZAPIs are still used for all other actions).
- na_ontap_software_update - add `force_update` option to ignore current version.
- na_ontap_svm - output ``modified`` if a modify action is taken.
- na_ontap_volume - ``compression`` to enable compression on a FAS volume.
- na_ontap_volume - ``inline-compression`` to enable inline compression on a volume.
- na_ontap_volume - ``nas_application_template`` to create a volume using nas application REST API.
- na_ontap_volume - ``size_change_threshold`` to ignore small changes in volume size.
- na_ontap_volume - ``sizing_method`` to resize a FlexGroup using REST.
- na_ontap_volume - use REST API for delete operation if targets supports it.
- na_ontap_wwpn_alias - improve error reporting when REST is not available.

netapp_eseries.santricity
~~~~~~~~~~~~~~~~~~~~~~~~~

- Add functionality to remove all inventory configuration in the nar_santricity_host role. Set configuration.eseries_remove_all_configuration=True to remove all storage pool/volume configuration, host, hostgroup, and lun mapping configuration.
- Add host_types, host_port_protocols, host_port_information, hostside_io_interface_protocols to netapp_volumes_by_initiators in the na_santricity_facts module.
- Add storage pool information to the volume_by_initiator facts.
- Add storage system not found exception to the common role's build_info task.
- Add volume_metadata option to na_santricity_volume module, add volume_metadata information to the netapp_volumes_by_initiators dictionary in na_santricity_facts module, and update the nar_santricity_host role with the option.
- Improve nar_santricity_common storage system api determinations; attempts to discover the storage system using the information provided in the inventory before attempting to search the subnet.
- Increased the storage system discovery connection timeouts to 30 seconds to prevent systems from not being discovered over slow connections.
- Minimize the facts gathered for the host initiators.
- Update ib iser determination to account for changes in firmware 11.60.2.
- Use existing Web Services Proxy storage system identifier when one is already created and one is not provided in the inventory.
- Utilize eseries_iscsi_iqn before searching host for iqn in nar_santricity_host role.

netbox.netbox
~~~~~~~~~~~~~

- Add ``follow_redirects`` option to inventory plugin (https://github.com/netbox-community/ansible_modules/pull/323)
- Added ``import_targets`` and ``export_targets`` options to ``netbox_vrf``
- nb_inventory - Added ``status`` as host_var. (359)
- nb_inventory - Added documentation for using ``keyed_groups``. (#361)
- nb_inventory - Allow to use virtual chassis name instead of device name. (#383)
- nb_lookup - Allow lookup of plugin endpoints. (#360)
- nb_lookup - Documentation update to show Fully Qualified Collection Name (FQCN). (#355)
- netbox_service - Add ``ports`` option for NetBox 2.10+ and convert ``port`` to ``ports`` if NetBox 2.9 or lower. (#396)
- netbox_virtual_machine - Added ``comments`` option. (#380)
- netbox_virtual_machine - Added ``local_context_data`` option. (#357)

ngine_io.cloudstack
~~~~~~~~~~~~~~~~~~~

- Deprecated the funtionality of first returned zone to be the default zone because of an unreliable API. Zone will be required beginning with next major version 2.0.0.
- cs_instance - Fixed an edge case caused by `displaytext` not available (https://github.com/ngine-io/ansible-collection-cloudstack/pull/49).
- cs_ip_address - allow to pick a particular IP address for a network, available since CloudStack v4.13 (https://github.com/ngine-io/ansible-collection-cloudstack/issues/30).
- cs_network - Fixed constraints when creating networks. The param `gateway` is no longer required if the param `netmask` is given (https://github.com/ngine-io/ansible-collection-cloudstack/pull/54).

ngine_io.vultr
~~~~~~~~~~~~~~

- vultr_block_storage - Included ability to resize, attach and detach Block Storage Volumes.

openstack.cloud
~~~~~~~~~~~~~~~

- dns_zone - Migrating dns_zone from AnsibleModule to OpenStackModule
- dns_zone, recordset - Enable update for recordset and add tests for dns and recordset module
- endpoint - Do not fail when endpoint state is absent
- ironic - Refactor ironic authentication into a new module_utils module
- lb_health_monitor - Make it possible to create a health monitor to a pool
- loadbalancer - Refactor loadbalancer module
- network - Migrating network from AnsibleModule to OpenStackModule
- networks_info - Migrating networks_info from AnsibleModule to OpenStackModule
- openstack - Add galaxy.yml to support install from git
- openstack - Fix docs-args mismatch in modules
- openstack - OpenStackModule Support defining a minimum version of the SDK
- router - Migrating routers from AnsibleModule to OpenStackModule
- routers_info - Added deprecated_names for router_info module
- routers_info - Migrating routers_info from AnsibleModule to OpenStackModule
- security_group.py - Migrating security_group from AnsibleModule to OpenStackModule
- security_group_rule - Refactor TCP/UDP port check
- server.py - Improve "server" module with OpenstackModule class
- server_volume - Migrating server_volume from AnsibleModule to OpenStackModule
- subnet - Fix subnets update and idempotency
- subnet - Migrating subnet module from AnsibleModule to OpenStackModule
- subnets_info - Migrating subnets_info from AnsibleModule to OpenStackModule
- volume.py - Migrating volume from AnsibleModule to OpenStackModule
- volume_info - Fix volume_info arguments for SDK 0.19

openvswitch.openvswitch
~~~~~~~~~~~~~~~~~~~~~~~

- openvswitch_bond - New module for managing Open vSwitch bonds (https://github.com/ansible-collections/openvswitch.openvswitch/pull/58).

ovirt.ovirt
~~~~~~~~~~~

- Add GPL license (https://github.com/oVirt/ovirt-ansible-collection/pull/101).
- ansible-builder - Update bindep (https://github.com/oVirt/ovirt-ansible-collection/pull/197).
- engine_setup - Add missing restore task file and vars file (https://github.com/oVirt/ovirt-ansible-collection/pull/180).
- hosted_engine_setup - Add after_add_host hook (https://github.com/oVirt/ovirt-ansible-collection/pull/181).
- hosted_engine_setup - Add compatibility_version (https://github.com/oVirt/ovirt-ansible-collection/pull/125).
- hosted_engine_setup - Collect all engine /var/log (https://github.com/oVirt/ovirt-ansible-collection/pull/202).
- hosted_engine_setup - Use ovirt_system_option_info instead of REST API (https://github.com/oVirt/ovirt-ansible-collection/pull/209).
- infra - don't require passowrd for user (https://github.com/oVirt/ovirt-ansible-collection/pull/195).
- inventory - correct os_type name (https://github.com/oVirt/ovirt-ansible-collection/pull/194).
- ovirt_disk - Add install warning (https://github.com/oVirt/ovirt-ansible-collection/pull/208).
- ovirt_disk - automatically detect virtual size of qcow image (https://github.com/oVirt/ovirt-ansible-collection/pull/183).
- ovirt_disk - ignore move of HE disks (https://github.com/oVirt/ovirt-ansible-collection/pull/162).
- ovirt_info - Fragment add auth suboptions to documentation (https://github.com/oVirt/ovirt-ansible-collection/pull/205).
- ovirt_nic - Add template_version (https://github.com/oVirt/ovirt-ansible-collection/pull/145).
- ovirt_nic_info - Add template (https://github.com/oVirt/ovirt-ansible-collection/pull/146).
- ovirt_vm_info - Add current_cd (https://github.com/oVirt/ovirt-ansible-collection/pull/144).

purestorage.flasharray
~~~~~~~~~~~~~~~~~~~~~~

- purefa_apiclient - New module to support API Client management
- purefa_directory - Add support for managed directories
- purefa_export - Add support for filesystem exports
- purefa_fs - Add filesystem management support
- purefa_hg - Enforce case-sensitivity rules for hostgroup objects
- purefa_host - Add host rename function
- purefa_host - Add support for multi-host creation
- purefa_host - Enforce hostname case-sensitivity rules
- purefa_info - Add support for FA Files features
- purefa_offload - Add support for Google Cloud offload target
- purefa_pg - Enforce case-sensitivity rules for protection group objects
- purefa_policy - Add support for NFS, SMB and Snapshot policy management
- purefa_vg - Add support for multiple vgroup creation
- purefa_volume - Add support for multi-volume creation

purestorage.flashblade
~~~~~~~~~~~~~~~~~~~~~~

- purefb_banner - Module to manage the GUI and SSH login message
- purefb_certgrp - Module to manage FlashBlade Certificate Groups
- purefb_certs - Module to create and delete SSL certificates
- purefb_connect - Support idempotency when exisitng connection is incoming
- purefb_fs - Add new options for filesystem control (https://github.com/Pure-Storage-Ansible/FlashBlade-Collection/pull/81)
- purefb_fs - Default filesystem size on creation changes from 32G to ``unlimited``
- purefb_fs - Fix error in deletion and eradication of filesystem
- purefb_fs_replica - Remove condition to attach/detach policies on unhealthy replica-link
- purefb_info - Add support to list filesystem policies
- purefb_lifecycle - Module to manage FlashBlade Bucket Lifecycle Rules
- purefb_s3user - Add support for imported user access keys
- purefb_syslog - Module to manage syslog server configuration

sensu.sensu_go
~~~~~~~~~~~~~~

- Add *build* variable to the *install* role that further pins down the package version that gets installed.
- Add API key authentication support.
- Add module return value samples.
- Add modules for managing Sensu Go secret providers.
- Add modules for managing Sensu Go secrets.
- Add support for Debian installation.
- Add support for RHEL 7 to the install role (thanks, @danragnar).
- Add support for RHEL and CentOS 8.
- Add support for hashed password in user module.
- Add support for installing Sensu Go agents on Windows.
- Add support for installing Sensu Go on Amazon Linux.
- Add support for secrets to check module.
- Add support for secrets to mutator module.
- Add support for secrets to pipe handler module.
- Allow modules to supply custom CA bundle for backend certificate validation or skip the validation entirely.
- List version 6.2.0 and 6.1.3 in Windows lookup table.
- List version 6.2.1 and 6.2.2 in Windows lookup table.
- Specify minimal python version for modules.
- Support for Sensu Go 5.16 initialization in backend role.
- Support for external datastore management using *datastore* and *datastore_info* modules.
- Update code of conduct.

servicenow.servicenow
~~~~~~~~~~~~~~~~~~~~~

- adds the ability to use `SN_INSTANCE` (ex. `dev61775`) or `SN_HOST` (ex. `dev61775.service-now.com`) with the inventory plugin.

theforeman.foreman
~~~~~~~~~~~~~~~~~~

- compute_resource - added ``caching_enabled`` option for VMware compute resources
- content_upload - use ``to_native`` to decode RPM headers if needed (RPM 4.15+ returns strings)
- content_view_version - provide examples how to obtain detailed information about content view versions (https://bugzilla.redhat.com/show_bug.cgi?id=1868145)
- content_view_version_cleanup - new role for cleaning up unused content view versions (https://github.com/theforeman/foreman-ansible-modules/issues/497)
- domain, host, hostgroup, operatingsystem, subnet - manage parameters in a single API call (https://bugzilla.redhat.com/show_bug.cgi?id=1855008)
- external_usergroup - rename the ``auth_source_ldap`` parameter to ``auth_source`` (``auth_source_ldap`` is still supported via an alias)
- global_parameter - allow to set hidden flag (https://github.com/theforeman/foreman-ansible-modules/issues/1024)
- host - add ``compute_attributes`` parameter to module (https://bugzilla.redhat.com/show_bug.cgi?id=1871815)
- host - allow management of interfaces (https://github.com/theforeman/foreman-ansible-modules/issues/757)
- inventory plugin - add support for the Report API present in Foreman 1.24 and later
- inventory plugin - allow to compose the ``inventory_hostname`` (https://github.com/theforeman/foreman-ansible-modules/issues/1070)
- job_template - stricter validation of ``template_inputs`` sub-options
- manifest - new role for easier handling of subscription manifest workflows
- provisioning_template - update list of possible template kinds (https://bugzilla.redhat.com/show_bug.cgi?id=1871978)
- redhat_manifest - allow configuring content access mode (https://github.com/theforeman/foreman-ansible-modules/issues/820)
- repository - update supported parameters (https://github.com/theforeman/foreman-ansible-modules/issues/935)
- server URL and credentials can now also be specified using environment variables (https://github.com/theforeman/foreman-ansible-modules/issues/837)
- subnet - add new ``externalipam_group`` parameter
- subnet - add support for external IPAM (https://github.com/theforeman/foreman-ansible-modules/issues/966)
- subnet - verify the server has the ``remote_execution`` plugin when specifying ``remote_execution_proxies``
- the ``apypie`` library is vendored inside the collection, so users only have to install ``requests`` manually now.
- update vendored ``apypie`` to 0.3.2

vyos.vyos
~~~~~~~~~

- Added ospf_interfaces resource module.

Breaking Changes / Porting Guide
--------------------------------

Ansible-base
~~~~~~~~~~~~

- ansible-galaxy login command has been removed (see https://github.com/ansible/ansible/issues/71560)

ansible.utils
~~~~~~~~~~~~~

- If added custom sub plugins in your collection move from old location `plugins/<sub-plugin-name>` to the new location `plugins/sub_plugins/<sub-plugin-name>` and update the imports as required
- Move sub plugins cli_parsers, fact_diff and validate to `plugins/sub_plugins` folder
- The `cli_parsers` sub plugins folder name is changed to `cli_parse` to have consistent naming convention, that is all the cli_parse subplugins will now be in `plugins/sub_plugins/cli_parse` folder

cloudscale_ch.cloud
~~~~~~~~~~~~~~~~~~~

- floating_ip - ``name`` is required for assigning a new floating IP.

community.general
~~~~~~~~~~~~~~~~~

- If you use Ansible 2.9 and the Google cloud plugins or modules from this collection, community.general 2.0.0 results in errors when trying to use the Google cloud content by FQCN, like ``community.general.gce_img``.
  Since Ansible 2.9 is not able to use redirections, you will have to adjust your playbooks and roles manually to use the new FQCNs (``community.google.gce_img`` for the previous example) and to make sure that you have ``community.google`` installed.

  If you use ansible-base 2.10 or newer and did not install Ansible 3.0.0, but installed (and/or upgraded) community.general manually, you need to make sure to also install the ``community.google`` or ``google.cloud`` collections if you are using any of the Google cloud plugins or modules.
  While ansible-base 2.10 or newer can use the redirects that community.general 2.0.0 adds, the collection they point to (such as community.google) must be installed for them to work.
- If you use Ansible 2.9 and the Kubevirt plugins or modules from this collection, community.general 2.0.0 results in errors when trying to use the Kubevirt content by FQCN, like ``community.general.kubevirt_vm``.
  Since Ansible 2.9 is not able to use redirections, you will have to adjust your playbooks and roles manually to use the new FQCNs (``community.kubevirt.kubevirt_vm`` for the previous example) and to make sure that you have ``community.kubevirt`` installed.

  If you use ansible-base 2.10 or newer and did not install Ansible 3.0.0, but installed (and/or upgraded) community.general manually, you need to make sure to also install the ``community.kubevirt`` collection if you are using any of the Kubevirt plugins or modules.
  While ansible-base 2.10 or newer can use the redirects that community.general 2.0.0 adds, the collection they point to (such as community.google) must be installed for them to work.
- If you use Ansible 2.9 and the ``docker`` plugins or modules from this collections, community.general 2.0.0 results in errors when trying to use the docker content by FQCN, like ``community.general.docker_container``.
  Since Ansible 2.9 is not able to use redirections, you will have to adjust your playbooks and roles manually to use the new FQCNs (``community.docker.docker_container`` for the previous example) and to make sure that you have ``community.docker`` installed.

  If you use ansible-base 2.10 or newer and did not install Ansible 3.0.0, but installed (and/or upgraded) community.general manually, you need to make sure to also install ``community.docker`` if you are using any of the ``docker`` plugins or modules.
  While ansible-base 2.10 or newer can use the redirects that community.general 2.0.0 adds, the collection they point to (community.docker) must be installed for them to work.
- If you use Ansible 2.9 and the ``hashi_vault`` lookup plugin from this collections, community.general 2.0.0 results in errors when trying to use the Hashi Vault content by FQCN, like ``community.general.hashi_vault``.
  Since Ansible 2.9 is not able to use redirections, you will have to adjust your inventories, variable files, playbooks and roles manually to use the new FQCN (``community.hashi_vault.hashi_vault``) and to make sure that you have ``community.hashi_vault`` installed.

  If you use ansible-base 2.10 or newer and did not install Ansible 3.0.0, but installed (and/or upgraded) community.general manually, you need to make sure to also install ``community.hashi_vault`` if you are using the ``hashi_vault`` plugin.
  While ansible-base 2.10 or newer can use the redirects that community.general 2.0.0 adds, the collection they point to (community.hashi_vault) must be installed for them to work.
- If you use Ansible 2.9 and the ``hetzner`` modules from this collections, community.general 2.0.0 results in errors when trying to use the hetzner content by FQCN, like ``community.general.hetzner_firewall``.
  Since Ansible 2.9 is not able to use redirections, you will have to adjust your playbooks and roles manually to use the new FQCNs (``community.hrobot.firewall`` for the previous example) and to make sure that you have ``community.hrobot`` installed.

  If you use ansible-base 2.10 or newer and did not install Ansible 3.0.0, but installed (and/or upgraded) community.general manually, you need to make sure to also install ``community.hrobot`` if you are using any of the ``hetzner`` modules.
  While ansible-base 2.10 or newer can use the redirects that community.general 2.0.0 adds, the collection they point to (community.hrobot) must be installed for them to work.
- If you use Ansible 2.9 and the ``oc`` connection plugin from this collections, community.general 2.0.0 results in errors when trying to use the oc content by FQCN, like ``community.general.oc``.
  Since Ansible 2.9 is not able to use redirections, you will have to adjust your inventories, variable files, playbooks and roles manually to use the new FQCN (``community.okd.oc``) and to make sure that you have ``community.okd`` installed.

  If you use ansible-base 2.10 or newer and did not install Ansible 3.0.0, but installed (and/or upgraded) community.general manually, you need to make sure to also install ``community.okd`` if you are using the ``oc`` plugin.
  While ansible-base 2.10 or newer can use the redirects that community.general 2.0.0 adds, the collection they point to (community.okd) must be installed for them to work.
- If you use Ansible 2.9 and the ``postgresql`` modules from this collections, community.general 2.0.0 results in errors when trying to use the postgresql content by FQCN, like ``community.general.postgresql_info``.
  Since Ansible 2.9 is not able to use redirections, you will have to adjust your playbooks and roles manually to use the new FQCNs (``community.postgresql.postgresql_info`` for the previous example) and to make sure that you have ``community.postgresql`` installed.

  If you use ansible-base 2.10 or newer and did not install Ansible 3.0.0, but installed (and/or upgraded) community.general manually, you need to make sure to also install ``community.postgresql`` if you are using any of the ``postgresql`` modules.
  While ansible-base 2.10 or newer can use the redirects that community.general 2.0.0 adds, the collection they point to (community.postgresql) must be installed for them to work.
- The Google cloud inventory script ``gce.py`` has been migrated to the ``community.google`` collection. Install the ``community.google`` collection in order to continue using it.
- archive - remove path folder itself when ``remove`` parameter is true (https://github.com/ansible-collections/community.general/issues/1041).
- log_plays callback - add missing information to the logs generated by the callback plugin. This changes the log message format (https://github.com/ansible-collections/community.general/pull/442).
- passwordstore lookup plugin - now parsing a password store entry as YAML if possible, skipping the first line (which by convention only contains the password and nothing else). If it cannot be parsed as YAML, the old ``key: value`` parser will be used to process the entry. Can break backwards compatibility if YAML formatted code was parsed in a non-YAML interpreted way, e.g. ``foo: [bar, baz]`` will become a list with two elements in the new version, but a string ``'[bar, baz]'`` in the old (https://github.com/ansible-collections/community.general/issues/1673).
- pkgng - passing ``name: *`` with ``state: absent`` will no longer remove every installed package from the system. It is now a noop. (https://github.com/ansible-collections/community.general/pull/569).
- pkgng - passing ``name: *`` with ``state: latest`` or ``state: present`` will no longer install every package from the configured package repositories. Instead, ``name: *, state: latest`` will upgrade all already-installed packages, and ``name: *, state: present`` is a noop. (https://github.com/ansible-collections/community.general/pull/569).
- proxmox_kvm - recognize ``force=yes`` in conjunction with ``state=absent`` to forcibly remove a running VM (https://github.com/ansible-collections/community.general/pull/849).
- utm_proxy_auth_profile - the ``frontend_cookie_secret`` return value now contains a placeholder string instead of the module's ``frontend_cookie_secret`` parameter (https://github.com/ansible-collections/community.general/pull/1736).

community.hashi_vault
~~~~~~~~~~~~~~~~~~~~~

- hashi_vault - the ``VAULT_ADDR`` environment variable is now checked last for the ``url`` parameter. For details on which use cases are impacted, see (https://github.com/ansible-collections/community.hashi_vault/issues/8).

community.hrobot
~~~~~~~~~~~~~~~~

- firewall - now requires the `ipaddress <https://pypi.org/project/ipaddress/>`_ library (https://github.com/ansible-collections/community.hrobot/pull/2).

community.network
~~~~~~~~~~~~~~~~~

- If you use Ansible 2.9 and the FortiOS modules from this collection, community.network 2.0.0 results in errors when trying to use the FortiOS content by FQCN, like ``community.network.fmgr_device``.
  Since Ansible 2.9 is not able to use redirections, you will have to adjust your playbooks and roles manually to use the new FQCNs (``community.fortios.fmgr_device`` for the previous example) and to make sure that you have ``community.fortios`` installed.

  If you use ansible-base 2.10 or newer and did not install Ansible 3.0.0, but installed (and/or upgraded) community.network manually, you need to make sure to also install ``community.fortios`` if you are using any of the FortiOS modules.
  While ansible-base 2.10 or newer can use the redirects that community.network 2.0.0 adds, the collection they point to (community.fortios) must be installed for them to work.
- If you use Ansible 2.9 and the ``cp_publish`` module from this collection, community.network 2.0.0 results in errors when trying to use the module by FQCN, i.e. ``community.network.cp_publish``. Since Ansible 2.9 is not able to use redirections, you will have to adjust your playbooks and roles manually to use the new FQCNs (``check_point.mgmt.cp_mgmt_publish``) and to make sure that you have ``check_point.mgmt`` installed.
  If you use ansible-base 2.10 or newer and did not install Ansible 3.0.0, but installed (and/or upgraded) community.network manually, you need to make sure to also install ``check_point.mgmt`` if you are using the ``cp_publish`` module. While ansible-base 2.10 or newer can use the redirects that community.network 2.0.0 adds, the collection they point to (check_point.mgmt) must be installed for them to work.
- If you use Ansible 2.9 and the ``fortimanager`` httpapi plugin from this collection, community.network 2.0.0 results in errors when trying to use it by FQCN (``community.network.fortimanager``).
  Since Ansible 2.9 is not able to use redirections, you will have to adjust your playbooks and roles manually to use the new FQCN ``fortinet.fortimanager.fortimanager`` and to make sure that you have ``fortinet.fortimanager`` installed.

  If you use ansible-base 2.10 or newer and did not install Ansible 3.0.0, but installed (and/or upgraded) community.network manually, you need to make sure to also install ``fortinet.fortimanager`` if you are using the ``fortimanager`` httpapi plugin.
  While ansible-base 2.10 or newer can use the redirect that community.network 2.0.0 adds, the collection they point to (fortinet.fortimanager) must be installed for it to work.
- If you use Ansible 2.9 and the ``nso`` modules from this collection, community.network 2.0.0 results in errors when trying to use the nso content by FQCN, like ``community.network.nso_config``.
  Since Ansible 2.9 is not able to use redirections, you will have to adjust your playbooks and roles manually to use the new FQCNs (``cisco.nso.nso_config`` for the previous example) and to make sure that you have ``cisco.nso`` installed.

  If you use ansible-base 2.10 or newer and did not install Ansible 3.0.0, but installed (and/or upgraded) community.network manually, you need to make sure to also install ``cisco.nso`` if you are using any of the ``nso`` modules.
  While ansible-base 2.10 or newer can use the redirects that community.network 2.0.0 adds, the collection they point to (cisco.nso) must be installed for them to work.
- If you use Ansible 2.9 and the ``routeros`` plugins or modules from this collections, community.network 2.0.0 results in errors when trying to use the routeros content by FQCN, like ``community.network.routeros_command``.
  Since Ansible 2.9 is not able to use redirections, you will have to adjust your playbooks and roles manually to use the new FQCNs (``community.routeros.command`` for the previous example) and to make sure that you have ``community.routeros`` installed.

  If you use ansible-base 2.10 or newer and did not install Ansible 3.0.0, but installed (and/or upgraded) community.network manually, you need to make sure to also install ``community.routeros`` if you are using any of the ``routeros`` plugins or modules.
  While ansible-base 2.10 or newer can use the redirects that community.network 2.0.0 adds, the collection they point to (community.routeros) must be installed for them to work.
- cnos_static_route - move ipaddress import from ansible.netcommon to builtin or package before ipaddress is removed from ansible.netcommon. You need to make sure to have the ipaddress package installed if you are using this module on Python 2.7 (https://github.com/ansible-collections/community.network/pull/129).

dellemc.os10
~~~~~~~~~~~~

- os10_bgp - Changed "subnet"  key as list format instead of dictionary format under "listen" key to support multiple neighbor prefix for listen command
- os10_bgp - Changed "vrf" key as list format instead of dictionary format to supprot multiple VRF in router BGP and changed the "vrf" key name to "vrfs"

ngine_io.cloudstack
~~~~~~~~~~~~~~~~~~~

- Authentication option using INI files e.g. ``cloudstack.ini`` has been removed. The only supported option to authenticate is by using the module params with fallback to the ENV variables.
- default zone deprecation - The `zone` param default value, across multiple modules, has been deprecated due to unreliable API (https://github.com/ngine-io/ansible-collection-cloudstack/pull/62).

Deprecated Features
-------------------

cisco.nxos
~~~~~~~~~~

- Deprecated `nxos_bgp` and `nxos_bgp_neighbor` modules in favor of `nxos_bgp_global` resource module.
- Deprecated `nxos_interface_ospf` in favor of `nxos_ospf_interfaces` Resource Module.
- Deprecated `nxos_smu` in favour of `nxos_rpm` module.
- The `nxos_ospf_vrf` module is deprecated by `nxos_ospfv2` and `nxos_ospfv3` Resource Modules.

community.aws
~~~~~~~~~~~~~

- ec2_vpc_igw_info - After 2022-06-22 the ``convert_tags`` parameter default value will change from ``False`` to ``True`` to match the collection standard behavior (https://github.com/ansible-collections/community.aws/pull/318).

community.docker
~~~~~~~~~~~~~~~~

- docker_container - currently ``published_ports`` can contain port mappings next to the special value ``all``, in which case the port mappings are ignored. This behavior is deprecated for community.docker 2.0.0, at which point it will either be forbidden, or this behavior will be properly implemented similar to how the Docker CLI tool handles this (https://github.com/ansible-collections/community.docker/issues/8, https://github.com/ansible-collections/community.docker/pull/60).

community.general
~~~~~~~~~~~~~~~~~

- The ``gluster_heal_info``, ``gluster_peer`` and ``gluster_volume`` modules have migrated to the `gluster.gluster <https://galaxy.ansible.com/gluster/gluster>`_ collection. Ansible-base 2.10.1 adjusted the routing target to point to the modules in that collection, so we will remove these modules in community.general 3.0.0. If you use Ansible 2.9, or use FQCNs ``community.general.gluster_*`` in your playbooks and/or roles, please update them to use the modules from ``gluster.gluster`` instead.
- The ldap_attr module has been deprecated and will be removed in a later release; use ldap_attrs instead.
- django_manage - the parameter ``liveserver`` relates to a no longer maintained third-party module for django. It is now deprecated, and will be remove in community.general 3.0.0 (https://github.com/ansible-collections/community.general/pull/1154).
- proxmox - the default of the new ``proxmox_default_behavior`` option will change from ``compatibility`` to ``no_defaults`` in community.general 4.0.0. Set the option to an explicit value to avoid a deprecation warning (https://github.com/ansible-collections/community.general/pull/850).
- proxmox_kvm - the default of the new ``proxmox_default_behavior`` option will change from ``compatibility`` to ``no_defaults`` in community.general 4.0.0. Set the option to an explicit value to avoid a deprecation warning (https://github.com/ansible-collections/community.general/pull/850).
- syspatch - deprecate the redundant ``apply`` argument (https://github.com/ansible-collections/community.general/pull/360).
- xbps - the ``force`` option never had any effect. It is now deprecated, and will be removed in 3.0.0 (https://github.com/ansible-collections/community.general/pull/568).

community.hashi_vault
~~~~~~~~~~~~~~~~~~~~~

- hashi_vault - ``VAULT_ADDR`` environment variable for option ``url`` will have its precedence lowered in 1.0.0; use ``ANSIBLE_HASHI_VAULT_ADDR`` to intentionally override a config value (https://github.com/ansible-collections/community.hashi_vault/issues/8).
- hashi_vault - ``VAULT_AUTH_METHOD`` environment variable for option ``auth_method`` will be removed in 2.0.0, use ``ANSIBLE_HASHI_VAULT_AUTH_METHOD`` instead (https://github.com/ansible-collections/community.hashi_vault/issues/17).
- hashi_vault - ``VAULT_ROLE_ID`` environment variable for option ``role_id`` will be removed in 2.0.0, use ``ANSIBLE_HASHI_VAULT_ROLE_ID`` instead (https://github.com/ansible-collections/community.hashi_vault/issues/20).
- hashi_vault - ``VAULT_SECRET_ID`` environment variable for option ``secret_id`` will be removed in 2.0.0, use ``ANSIBLE_HASHI_VAULT_SECRET_ID`` instead (https://github.com/ansible-collections/community.hashi_vault/issues/20).
- hashi_vault - ``VAULT_TOKEN_FILE`` environment variable for option ``token_file`` will be removed in 2.0.0, use ``ANSIBLE_HASHI_VAULT_TOKEN_FILE`` instead (https://github.com/ansible-collections/community.hashi_vault/issues/15).
- hashi_vault - ``VAULT_TOKEN_PATH`` environment variable for option ``token_path`` will be removed in 2.0.0, use ``ANSIBLE_HASHI_VAULT_TOKEN_PATH`` instead (https://github.com/ansible-collections/community.hashi_vault/issues/15).

community.network
~~~~~~~~~~~~~~~~~

- Deprecate connection=local support for network platforms using persistent framework (https://github.com/ansible-collections/community.network/pull/120).

community.vmware
~~~~~~~~~~~~~~~~

- vmware_host_firewall_manager - the creation of new rule with no ``allowed_ip`` entry in the ``allowed_hosts`` dictionary won't be allowed after 2.0.0 release.

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- The ``dellemc_get_firmware_inventory`` module is deprecated and replaced with ``idrac_firmware_info``.
- The ``dellemc_get_system_inventory`` module is deprecated and replaced with ``idrac_system_info``.
- The dellemc_change_power_state module is deprecated and replaced with the redfish_powerstate module.
- The dellemc_configure_bios module is deprecated and replaced with the idrac_bios module.
- The dellemc_configure_idrac_network module is deprecated and replaced with the idrac_network module.
- The dellemc_configure_idrac_timezone module is deprecated and replaced with the idrac_timezone_ntp module.
- The dellemc_configure_idrac_users module is deprecated and replaced with the idrac_user module.
- The dellemc_delete_lc_job and dellemc_delete_lc_job_queue modules are deprecated and replaced with the idrac_lifecycle_controller_jobs module.
- The dellemc_export_lc_logs module is deprecated and replaced with the idrac_lifecycle_controller_logs module.
- The dellemc_get_lc_job_status module is deprecated and replaced with the idrac_lifecycle_controller_job_status_info module.
- The dellemc_get_lcstatus module is deprecated and replaced with the idrac_lifecycle_controller_status_info module.
- The dellemc_idrac_reset module is deprecated and replaced with the idrac_reset module.
- The dellemc_setup_idrac_syslog module is deprecated and replaced  with the idrac_syslog module.

Removed Features (previously deprecated)
----------------------------------------

community.docker
~~~~~~~~~~~~~~~~

- docker_container - no longer returns ``ansible_facts`` (https://github.com/ansible-collections/community.docker/pull/1).
- docker_container - the default of ``networks_cli_compatible`` changed to ``true`` (https://github.com/ansible-collections/community.docker/pull/1).
- docker_container - the unused option ``trust_image_content`` has been removed (https://github.com/ansible-collections/community.docker/pull/1).
- docker_image - ``state=build`` has been removed. Use ``present`` instead (https://github.com/ansible-collections/community.docker/pull/1).
- docker_image - the ``container_limits``, ``dockerfile``, ``http_timeout``, ``nocache``, ``rm``, ``path``, ``buildargs``, ``pull`` have been removed. Use the corresponding suboptions of ``build`` instead (https://github.com/ansible-collections/community.docker/pull/1).
- docker_image - the ``force`` option has been removed. Use the more specific ``force_*`` options instead (https://github.com/ansible-collections/community.docker/pull/1).
- docker_image - the ``source`` option is now mandatory (https://github.com/ansible-collections/community.docker/pull/1).
- docker_image - the ``use_tls`` option has been removed. Use ``tls`` and ``validate_certs`` instead (https://github.com/ansible-collections/community.docker/pull/1).
- docker_image - the default of the ``build.pull`` option changed to ``false`` (https://github.com/ansible-collections/community.docker/pull/1).
- docker_image_facts - this alias is on longer availabe, use ``docker_image_info`` instead (https://github.com/ansible-collections/community.docker/pull/1).
- docker_network - no longer returns ``ansible_facts`` (https://github.com/ansible-collections/community.docker/pull/1).
- docker_network - the ``ipam_options`` option has been removed. Use ``ipam_config`` instead (https://github.com/ansible-collections/community.docker/pull/1).
- docker_service - no longer returns ``ansible_facts`` (https://github.com/ansible-collections/community.docker/pull/1).
- docker_swarm - ``state=inspect`` has been removed. Use ``docker_swarm_info`` instead (https://github.com/ansible-collections/community.docker/pull/1).
- docker_swarm_service - the ``constraints`` option has been removed. Use ``placement.constraints`` instead (https://github.com/ansible-collections/community.docker/pull/1).
- docker_swarm_service - the ``limit_cpu`` and ``limit_memory`` options has been removed. Use the corresponding suboptions in ``limits`` instead (https://github.com/ansible-collections/community.docker/pull/1).
- docker_swarm_service - the ``log_driver`` and ``log_driver_options`` options has been removed. Use the corresponding suboptions in ``logging`` instead (https://github.com/ansible-collections/community.docker/pull/1).
- docker_swarm_service - the ``reserve_cpu`` and ``reserve_memory`` options has been removed. Use the corresponding suboptions in ``reservations`` instead (https://github.com/ansible-collections/community.docker/pull/1).
- docker_swarm_service - the ``restart_policy``, ``restart_policy_attempts``, ``restart_policy_delay`` and ``restart_policy_window`` options has been removed. Use the corresponding suboptions in ``restart_config`` instead (https://github.com/ansible-collections/community.docker/pull/1).
- docker_swarm_service - the ``update_delay``, ``update_parallelism``, ``update_failure_action``, ``update_monitor``, ``update_max_failure_ratio`` and ``update_order`` options has been removed. Use the corresponding suboptions in ``update_config`` instead (https://github.com/ansible-collections/community.docker/pull/1).
- docker_volume - no longer returns ``ansible_facts`` (https://github.com/ansible-collections/community.docker/pull/1).
- docker_volume - the ``force`` option has been removed. Use ``recreate`` instead (https://github.com/ansible-collections/community.docker/pull/1).

community.general
~~~~~~~~~~~~~~~~~

- All Google cloud modules and plugins have now been migrated away from this collection.
  They can be found in either the `community.google <https://galaxy.ansible.com/community/google>`_ or `google.cloud <https://galaxy.ansible.com/google/cloud>`_ collections.
  If you use ansible-base 2.10 or newer, redirections have been provided.

  If you use Ansible 2.9 and installed this collection, you need to adjust the FQCNs (``community.general.gce_img`` → ``community.google.gce_img``) and make sure to install the community.google or google.cloud collections as appropriate.
- All Kubevirt modules and plugins have now been migrated from community.general to the `community.kubevirt <https://galaxy.ansible.com/community/kubevirt>`_ Ansible collection.
  If you use ansible-base 2.10 or newer, redirections have been provided.

  If you use Ansible 2.9 and installed this collection, you need to adjust the FQCNs (``community.general.kubevirt_vm`` → ``community.kubevirt.kubevirt_vm``) and make sure to install the community.kubevirt collection.
- All ``docker`` modules and plugins have been removed from this collection.
  They have been migrated to the `community.docker <https://galaxy.ansible.com/community/docker>`_ collection.
  If you use ansible-base 2.10 or newer, redirections have been provided.

  If you use Ansible 2.9 and installed this collection, you need to adjust the FQCNs (``community.general.docker_container`` → ``community.docker.docker_container``) and make sure to install the community.docker collection.
- All ``hetzner`` modules have been removed from this collection.
  They have been migrated to the `community.hrobot <https://galaxy.ansible.com/community/hrobot>`_ collection.
  If you use ansible-base 2.10 or newer, redirections have been provided.

  If you use Ansible 2.9 and installed this collection, you need to adjust the FQCNs (``community.general.hetzner_firewall`` → ``community.hrobot.firewall``) and make sure to install the community.hrobot collection.
- All ``postgresql`` modules have been removed from this collection.
  They have been migrated to the `community.postgresql <https://galaxy.ansible.com/community/postgresql>`_ collection.

  If you use ansible-base 2.10 or newer, redirections have been provided.
  If you use Ansible 2.9 and installed this collection, you need to adjust the FQCNs (``community.general.postgresql_info`` → ``community.postgresql.postgresql_info``) and make sure to install the community.postgresql collection.
- The Google cloud inventory script ``gce.py`` has been migrated to the ``community.google`` collection. Install the ``community.google`` collection in order to continue using it.
- The ``hashi_vault`` lookup plugin has been removed from this collection.
  It has been migrated to the `community.hashi_vault <https://galaxy.ansible.com/community/hashi_vault>`_ collection.
  If you use ansible-base 2.10 or newer, redirections have been provided.

  If you use Ansible 2.9 and installed this collection, you need to adjust the FQCNs (``community.general.hashi_vault`` → ``community.hashi_vault.hashi_vault``) and make sure to install the community.hashi_vault collection.
- The ``oc`` connection plugin has been removed from this collection.
  It has been migrated to the `community.okd <https://galaxy.ansible.com/community/okd>`_ collection.
  If you use ansible-base 2.10 or newer, redirections have been provided.

  If you use Ansible 2.9 and installed this collection, you need to adjust the FQCNs (``community.general.oc`` → ``community.okd.oc``) and make sure to install the community.okd collection.
- The deprecated ``actionable`` callback plugin has been removed. Use the ``ansible.builtin.default`` callback plugin with ``display_skipped_hosts = no`` and ``display_ok_hosts = no`` options instead (https://github.com/ansible-collections/community.general/pull/1347).
- The deprecated ``foreman`` module has been removed. Use the modules from the theforeman.foreman collection instead (https://github.com/ansible-collections/community.general/pull/1347) (https://github.com/ansible-collections/community.general/pull/1347).
- The deprecated ``full_skip`` callback plugin has been removed. Use the ``ansible.builtin.default`` callback plugin with ``display_skipped_hosts = no`` option instead (https://github.com/ansible-collections/community.general/pull/1347).
- The deprecated ``gcdns_record`` module has been removed. Use ``google.cloud.gcp_dns_resource_record_set`` instead (https://github.com/ansible-collections/community.general/pull/1370).
- The deprecated ``gcdns_zone`` module has been removed. Use ``google.cloud.gcp_dns_managed_zone`` instead (https://github.com/ansible-collections/community.general/pull/1370).
- The deprecated ``gce`` module has been removed. Use ``google.cloud.gcp_compute_instance`` instead (https://github.com/ansible-collections/community.general/pull/1370).
- The deprecated ``gcp_backend_service`` module has been removed. Use ``google.cloud.gcp_compute_backend_service`` instead (https://github.com/ansible-collections/community.general/pull/1370).
- The deprecated ``gcp_forwarding_rule`` module has been removed. Use ``google.cloud.gcp_compute_forwarding_rule`` or ``google.cloud.gcp_compute_global_forwarding_rule`` instead (https://github.com/ansible-collections/community.general/pull/1370).
- The deprecated ``gcp_healthcheck`` module has been removed. Use ``google.cloud.gcp_compute_health_check``, ``google.cloud.gcp_compute_http_health_check`` or ``google.cloud.gcp_compute_https_health_check`` instead (https://github.com/ansible-collections/community.general/pull/1370).
- The deprecated ``gcp_target_proxy`` module has been removed. Use ``google.cloud.gcp_compute_target_http_proxy`` instead (https://github.com/ansible-collections/community.general/pull/1370).
- The deprecated ``gcp_url_map`` module has been removed. Use ``google.cloud.gcp_compute_url_map`` instead (https://github.com/ansible-collections/community.general/pull/1370).
- The deprecated ``gcspanner`` module has been removed. Use ``google.cloud.gcp_spanner_database`` and/or ``google.cloud.gcp_spanner_instance`` instead (https://github.com/ansible-collections/community.general/pull/1370).
- The deprecated ``github_hooks`` module has been removed. Use ``community.general.github_webhook`` and ``community.general.github_webhook_info`` instead (https://github.com/ansible-collections/community.general/pull/1347).
- The deprecated ``katello`` module has been removed. Use the modules from the theforeman.foreman collection instead (https://github.com/ansible-collections/community.general/pull/1347).
- The deprecated ``na_cdot_aggregate`` module has been removed. Use netapp.ontap.na_ontap_aggregate instead (https://github.com/ansible-collections/community.general/pull/1347).
- The deprecated ``na_cdot_license`` module has been removed. Use netapp.ontap.na_ontap_license instead (https://github.com/ansible-collections/community.general/pull/1347).
- The deprecated ``na_cdot_lun`` module has been removed. Use netapp.ontap.na_ontap_lun instead (https://github.com/ansible-collections/community.general/pull/1347).
- The deprecated ``na_cdot_qtree`` module has been removed. Use netapp.ontap.na_ontap_qtree instead (https://github.com/ansible-collections/community.general/pull/1347).
- The deprecated ``na_cdot_svm`` module has been removed. Use netapp.ontap.na_ontap_svm instead (https://github.com/ansible-collections/community.general/pull/1347).
- The deprecated ``na_cdot_user_role`` module has been removed. Use netapp.ontap.na_ontap_user_role instead (https://github.com/ansible-collections/community.general/pull/1347).
- The deprecated ``na_cdot_user`` module has been removed. Use netapp.ontap.na_ontap_user instead (https://github.com/ansible-collections/community.general/pull/1347).
- The deprecated ``na_cdot_volume`` module has been removed. Use netapp.ontap.na_ontap_volume instead (https://github.com/ansible-collections/community.general/pull/1347).
- The deprecated ``sf_account_manager`` module has been removed. Use netapp.elementsw.na_elementsw_account instead (https://github.com/ansible-collections/community.general/pull/1347).
- The deprecated ``sf_check_connections`` module has been removed. Use netapp.elementsw.na_elementsw_check_connections instead (https://github.com/ansible-collections/community.general/pull/1347).
- The deprecated ``sf_snapshot_schedule_manager`` module has been removed. Use netapp.elementsw.na_elementsw_snapshot_schedule instead (https://github.com/ansible-collections/community.general/pull/1347).
- The deprecated ``sf_volume_access_group_manager`` module has been removed. Use netapp.elementsw.na_elementsw_access_group instead (https://github.com/ansible-collections/community.general/pull/1347).
- The deprecated ``sf_volume_manager`` module has been removed. Use netapp.elementsw.na_elementsw_volume instead (https://github.com/ansible-collections/community.general/pull/1347).
- The deprecated ``stderr`` callback plugin has been removed. Use the ``ansible.builtin.default`` callback plugin with ``display_failed_stderr = yes`` option instead (https://github.com/ansible-collections/community.general/pull/1347).
- The redirect of the ``conjur_variable`` lookup plugin to ``cyberark.conjur.conjur_variable`` collection was removed (https://github.com/ansible-collections/community.general/pull/1346).
- The redirect of the ``firewalld`` module and the ``firewalld`` module_utils to the ``ansible.posix`` collection was removed (https://github.com/ansible-collections/community.general/pull/1346).
- The redirect to the ``community.digitalocean`` collection was removed for: the ``digital_ocean`` doc fragment, the ``digital_ocean`` module_utils, and the following modules: ``digital_ocean``, ``digital_ocean_account_facts``, ``digital_ocean_account_info``, ``digital_ocean_block_storage``, ``digital_ocean_certificate``, ``digital_ocean_certificate_facts``, ``digital_ocean_certificate_info``, ``digital_ocean_domain``, ``digital_ocean_domain_facts``, ``digital_ocean_domain_info``, ``digital_ocean_droplet``, ``digital_ocean_firewall_facts``, ``digital_ocean_firewall_info``, ``digital_ocean_floating_ip``, ``digital_ocean_floating_ip_facts``, ``digital_ocean_floating_ip_info``, ``digital_ocean_image_facts``, ``digital_ocean_image_info``, ``digital_ocean_load_balancer_facts``, ``digital_ocean_load_balancer_info``, ``digital_ocean_region_facts``, ``digital_ocean_region_info``, ``digital_ocean_size_facts``, ``digital_ocean_size_info``, ``digital_ocean_snapshot_facts``, ``digital_ocean_snapshot_info``, ``digital_ocean_sshkey``, ``digital_ocean_sshkey_facts``, ``digital_ocean_sshkey_info``, ``digital_ocean_tag``, ``digital_ocean_tag_facts``, ``digital_ocean_tag_info``, ``digital_ocean_volume_facts``, ``digital_ocean_volume_info`` (https://github.com/ansible-collections/community.general/pull/1346).
- The redirect to the ``community.mysql`` collection was removed for: the ``mysql`` doc fragment, the ``mysql`` module_utils, and the following modules: ``mysql_db``, ``mysql_info``, ``mysql_query``, ``mysql_replication``, ``mysql_user``, ``mysql_variables`` (https://github.com/ansible-collections/community.general/pull/1346).
- The redirect to the ``community.proxysql`` collection was removed for: the ``proxysql`` doc fragment, and the following modules: ``proxysql_backend_servers``, ``proxysql_global_variables``, ``proxysql_manage_config``, ``proxysql_mysql_users``, ``proxysql_query_rules``, ``proxysql_replication_hostgroups``, ``proxysql_scheduler`` (https://github.com/ansible-collections/community.general/pull/1346).
- The redirect to the ``infinidat.infinibox`` collection was removed for: the ``infinibox`` doc fragment, the ``infinibox`` module_utils, and the following modules: ``infini_export``, ``infini_export_client``, ``infini_fs``, ``infini_host``, ``infini_pool``, ``infini_vol`` (https://github.com/ansible-collections/community.general/pull/1346).
- conjur_variable lookup - has been moved to the ``cyberark.conjur`` collection. A redirection is active, which will be removed in version 2.0.0 (https://github.com/ansible-collections/community.general/pull/570).
- digital_ocean_* - all DigitalOcean modules have been moved to the ``community.digitalocean`` collection. A redirection is active, which will be removed in version 2.0.0 (https://github.com/ansible-collections/community.general/pull/622).
- infini_* - all infinidat modules have been moved to the ``infinidat.infinibox`` collection. A redirection is active, which will be removed in version 2.0.0 (https://github.com/ansible-collections/community.general/pull/607).
- iptables_state - the ``ANSIBLE_ASYNC_DIR`` environment is no longer supported, use the ``async_dir`` shell option instead (https://github.com/ansible-collections/community.general/pull/1371).
- logicmonitor - the module has been removed in 1.0.0 since it is unmaintained and the API used by the module has been turned off in 2017 (https://github.com/ansible-collections/community.general/issues/539, https://github.com/ansible-collections/community.general/pull/541).
- logicmonitor_facts - the module has been removed in 1.0.0 since it is unmaintained and the API used by the module has been turned off in 2017 (https://github.com/ansible-collections/community.general/issues/539, https://github.com/ansible-collections/community.general/pull/541).
- memcached cache plugin - do not import ``CacheModule``s directly. Use ``ansible.plugins.loader.cache_loader`` instead (https://github.com/ansible-collections/community.general/pull/1371).
- mysql_* - all MySQL modules have been moved to the ``community.mysql`` collection. A redirection is active, which will be removed in version 2.0.0 (https://github.com/ansible-collections/community.general/pull/633).
- proxysql_* - all ProxySQL modules have been moved to the ``community.proxysql`` collection. A redirection is active, which will be removed in version 2.0.0 (https://github.com/ansible-collections/community.general/pull/624).
- redis cache plugin - do not import ``CacheModule``s directly. Use ``ansible.plugins.loader.cache_loader`` instead (https://github.com/ansible-collections/community.general/pull/1371).
- xml - when ``content=attribute``, the ``attribute`` option is ignored (https://github.com/ansible-collections/community.general/pull/1371).

community.network
~~~~~~~~~~~~~~~~~

- All FortiOS modules and plugins have been removed from this collection.
  They have been migrated to the `community.fortios <https://galaxy.ansible.com/community/fortios>`_ collection.
  If you use ansible-base 2.10 or newer, redirections have been provided.

  If you use Ansible 2.9 and installed this collection, you need to adjust the FQCNs (``community.network.fmgr_device`` → ``community.fortios.fmgr_device``) and make sure to install the `community.fortios` collection.
- All ``nso`` modules have been removed from this collection.
  They have been migrated to the `cisco.nso <https://galaxy.ansible.com/cisco/nso>`_ collection.
  If you use ansible-base 2.10 or newer, redirections have been provided.

  If you use Ansible 2.9 and installed this collection, you need to adjust the FQCNs (``community.network.nso_config`` → ``cisco.nso.nso_config``) and make sure to install the `cisco.nso` collection.
- All ``routeros`` modules and plugins have been removed from this collection.
  They have been migrated to the `community.routeros <https://galaxy.ansible.com/community/routeros>`_ collection.
  If you use ansible-base 2.10 or newer, redirections have been provided.

  If you use Ansible 2.9 and installed this collection, you need to adjust the FQCNs (``community.network.routeros_command`` → ``community.routeros.command``) and make sure to install the community.routeros collection.
- The ``cp_publish`` module has been removed from this collection. It was a duplicate of ``check_point.mgmt.cp_mgmt_publish`` in the `check_point.mgmt <https://galaxy.ansible.com/check_point/mgmt>`_ collection. If you use ansible-base 2.10 or newer, redirections have been provided.
  If you use Ansible 2.9 and installed this collection, you need to adjust the FQCNs (``community.network.cp_publish`` → ``check_point.mgmt.cp_mgmt_publish``) and make sure to install the check_point.mgmt collection.
- The ``fortimanager`` httpapi plugin has been removed from this collection.
  It was a duplicate of the one in the `fortinet.fortimanager <https://galaxy.ansible.com/fortinet/fortimanager>`_ collection.
  If you use ansible-base 2.10 or newer, a redirection has been provided.

  If you use Ansible 2.9 and installed this collection, you need to adjust the FQCNs (``community.network.fortimanager`` → ``fortinet.fortimanager.fortimanager``) and make sure to install the `fortinet.fortimanager` collection.
- The dependency on the ``check_point.mgmt`` collection has been removed. If you depend on that installing ``community.network`` also installs ``check_point.mgmt``, you have to make sure to install ``check_point.mgmt`` explicitly.
- The deprecated Pluribus Networks modules ``pn_cluster``, ``pn_ospf``, ``pn_ospfarea``, ``pn_show``, ``pn_trunk``, ``pn_vlag``, ``pn_vlan``, ``pn_vrouter``, ``pn_vrouterbgp``, ``pn_vrouterif``, ``pn_vrouterlbif`` have been removed (https://github.com/ansible-collections/community.network/pull/176).
- The deprecated modules ``panos_admin``, ``panos_admpwd``, ``panos_cert_gen_ssh``, ``panos_check``, ``panos_commit``, ``panos_dag``, ``panos_dag_tags``, ``panos_import``, ``panos_interface``, ``panos_lic``, ``panos_loadcfg``, ``panos_match_rule``, ``panos_mgtconfig``, ``panos_nat_rule``, ``panos_object``, ``panos_op``, ``panos_pg``, ``panos_query_rules``, ``panos_restart``, ``panos_sag``, ``panos_security_rule``, ``panos_set`` have been removed. Use modules from the `paloaltonetworks.panos collection <https://galaxy.ansible.com/paloaltonetworks/panos>`_ instead (https://github.com/ansible-collections/community.network/pull/176).
- The redirect to the ``mellanox.onyx`` collection was removed for: the ``onyx`` cliconf plugin, terminal plugin, module_utils, action plugin, doc fragment, and the following modules: ``onyx_aaa``, ``onyx_bfd``, ``onyx_bgp``, ``onyx_buffer_pool``, ``onyx_command``, ``onyx_config``, ``onyx_facts``, ``onyx_igmp``, ``onyx_igmp_interface``, ``onyx_igmp_vlan``, ``onyx_interface``, ``onyx_l2_interface``, ``onyx_l3_interface``, ``onyx_linkagg``, ``onyx_lldp``, ``onyx_lldp_interface``, ``onyx_magp``, ``onyx_mlag_ipl``, ``onyx_mlag_vip``, ``onyx_ntp``, ``onyx_ntp_servers_peers``, ``onyx_ospf``, ``onyx_pfc_interface``, ``onyx_protocol``, ``onyx_ptp_global``, ``onyx_ptp_interface``, ``onyx_qos``, ``onyx_snmp``, ``onyx_snmp_hosts``, ``onyx_snmp_users``, ``onyx_syslog_files``, ``onyx_syslog_remote``, ``onyx_traffic_class``, ``onyx_username``, ``onyx_vlan``, ``onyx_vxlan``, ``onyx_wjh`` (https://github.com/ansible-collections/community.network/pull/175).
- onyx - all onyx modules and plugins have been moved to the mellanox.onyx collection. Redirects have been added that will be removed in community.network 2.0.0 (https://github.com/ansible-collections/community.network/pull/83).

f5networks.f5_modules
~~~~~~~~~~~~~~~~~~~~~

- Removed arp_state parameter from the bigip_virtual_address module

Security Fixes
--------------

cisco.nxos
~~~~~~~~~~

- Enable no_log for sensitive parameters in argspec.

community.crypto
~~~~~~~~~~~~~~~~

- openssl_csr - the option ``privatekey_content`` was not marked as ``no_log``, resulting in it being dumped into the system log by default, and returned in the registered results in the ``invocation`` field (CVE-2020-25646, https://github.com/ansible-collections/community.crypto/pull/125).
- openssl_privatekey_info - the option ``content`` was not marked as ``no_log``, resulting in it being dumped into the system log by default, and returned in the registered results in the ``invocation`` field (CVE-2020-25646, https://github.com/ansible-collections/community.crypto/pull/125).
- openssl_publickey - the option ``privatekey_content`` was not marked as ``no_log``, resulting in it being dumped into the system log by default, and returned in the registered results in the ``invocation`` field (CVE-2020-25646, https://github.com/ansible-collections/community.crypto/pull/125).
- openssl_signature - the option ``privatekey_content`` was not marked as ``no_log``, resulting in it being dumped into the system log by default, and returned in the registered results in the ``invocation`` field (CVE-2020-25646, https://github.com/ansible-collections/community.crypto/pull/125).
- x509_certificate - the options ``privatekey_content`` and ``ownca_privatekey_content`` were not marked as ``no_log``, resulting in it being dumped into the system log by default, and returned in the registered results in the ``invocation`` field (CVE-2020-25646, https://github.com/ansible-collections/community.crypto/pull/125).
- x509_crl - the option ``privatekey_content`` was not marked as ``no_log``, resulting in it being dumped into the system log by default, and returned in the registered results in the ``invocation`` field (CVE-2020-25646, https://github.com/ansible-collections/community.crypto/pull/125).

community.docker
~~~~~~~~~~~~~~~~

- docker_swarm - enabled ``no_log`` for the option ``signing_ca_key`` to prevent accidental disclosure (CVE-2021-20191, https://github.com/ansible-collections/community.docker/pull/80).

community.general
~~~~~~~~~~~~~~~~~

- bitbucket_pipeline_variable - **CVE-2021-20180** - hide user sensitive information which are marked as ``secured`` from logging into the console (https://github.com/ansible-collections/community.general/pull/1635).
- dnsmadeeasy - mark the ``account_key`` parameter as ``no_log`` to avoid leakage of secrets (https://github.com/ansible-collections/community.general/pull/1736).
- gitlab_runner - mark the ``registration_token`` parameter as ``no_log`` to avoid leakage of secrets (https://github.com/ansible-collections/community.general/pull/1736).
- hwc_ecs_instance - mark the ``admin_pass`` parameter as ``no_log`` to avoid leakage of secrets (https://github.com/ansible-collections/community.general/pull/1736).
- ibm_sa_host - mark the ``iscsi_chap_secret`` parameter as ``no_log`` to avoid leakage of secrets (https://github.com/ansible-collections/community.general/pull/1736).
- keycloak_* modules - mark the ``auth_client_secret`` parameter as ``no_log`` to avoid leakage of secrets (https://github.com/ansible-collections/community.general/pull/1736).
- keycloak_client - mark the ``registration_access_token`` parameter as ``no_log`` to avoid leakage of secrets (https://github.com/ansible-collections/community.general/pull/1736).
- librato_annotation - mark the ``api_key`` parameter as ``no_log`` to avoid leakage of secrets (https://github.com/ansible-collections/community.general/pull/1736).
- logentries_msg - mark the ``token`` parameter as ``no_log`` to avoid leakage of secrets (https://github.com/ansible-collections/community.general/pull/1736).
- module_utils/_netapp, na_ontap_gather_facts - enabled ``no_log`` for the options ``api_key`` and ``secret_key`` to prevent accidental disclosure (CVE-2021-20191, https://github.com/ansible-collections/community.general/pull/1725).
- module_utils/identity/keycloak, keycloak_client, keycloak_clienttemplate, keycloak_group - enabled ``no_log`` for the option ``auth_client_secret`` to prevent accidental disclosure (CVE-2021-20191, https://github.com/ansible-collections/community.general/pull/1725).
- nios_nsgroup - mark the ``tsig_key`` parameter as ``no_log`` to avoid leakage of secrets (https://github.com/ansible-collections/community.general/pull/1736).
- oneandone_firewall_policy, oneandone_load_balancer, oneandone_monitoring_policy, oneandone_private_network, oneandone_public_ip - mark the ``auth_token`` parameter as ``no_log`` to avoid leakage of secrets (https://github.com/ansible-collections/community.general/pull/1736).
- ovirt - mark the ``instance_key`` parameter as ``no_log`` to avoid leakage of secrets (https://github.com/ansible-collections/community.general/pull/1736).
- ovirt - mark the ``instance_rootpw`` parameter as ``no_log`` to avoid leakage of secrets (https://github.com/ansible-collections/community.general/pull/1736).
- pagerduty_alert - mark the ``api_key``, ``service_key`` and ``integration_key`` parameters as ``no_log`` to avoid leakage of secrets (https://github.com/ansible-collections/community.general/pull/1736).
- pagerduty_change - mark the ``integration_key`` parameter as ``no_log`` to avoid leakage of secrets (https://github.com/ansible-collections/community.general/pull/1736).
- pingdom - mark the ``key`` parameter as ``no_log`` to avoid leakage of secrets (https://github.com/ansible-collections/community.general/pull/1736).
- pulp_repo - mark the ``feed_client_key`` parameter as ``no_log`` to avoid leakage of secrets (https://github.com/ansible-collections/community.general/pull/1736).
- rax_clb_ssl - mark the ``private_key`` parameter as ``no_log`` to avoid leakage of secrets (https://github.com/ansible-collections/community.general/pull/1736).
- redfish_command - mark the ``update_creds.password`` parameter as ``no_log`` to avoid leakage of secrets (https://github.com/ansible-collections/community.general/pull/1736).
- rollbar_deployment - mark the ``token`` parameter as ``no_log`` to avoid leakage of secrets (https://github.com/ansible-collections/community.general/pull/1736).
- snmp_facts - **CVE-2021-20178** - hide user sensitive information such as ``privkey`` and ``authkey`` from logging into the console (https://github.com/ansible-collections/community.general/pull/1621).
- spotinst_aws_elastigroup - mark the ``multai_token`` and ``token`` parameters as ``no_log`` to avoid leakage of secrets (https://github.com/ansible-collections/community.general/pull/1736).
- stackdriver - mark the ``key`` parameter as ``no_log`` to avoid leakage of secrets (https://github.com/ansible-collections/community.general/pull/1736).
- utm_proxy_auth_profile - enabled ``no_log`` for the option ``frontend_cookie_secret`` to prevent accidental disclosure (CVE-2021-20191, https://github.com/ansible-collections/community.general/pull/1725).
- utm_proxy_auth_profile - mark the ``frontend_cookie_secret`` parameter as ``no_log`` to avoid leakage of secrets. This causes the ``utm_proxy_auth_profile`` return value to no longer containing the correct value, but a placeholder (https://github.com/ansible-collections/community.general/pull/1736).

community.network
~~~~~~~~~~~~~~~~~

- ce_vrrp - mark the ``auth_key`` parameter as ``no_log`` to avoid leakage of secrets (https://github.com/ansible-collections/community.network/pull/206).
- cloudengine/ce_vrrp - enabled ``no_log`` for the options ``auth_key`` to prevent accidental disclosure (CVE-2021-20191, https://github.com/ansible-collections/community.network/pull/203).
- cnos_* modules - mark the ``passwords`` parameter as ``no_log`` to avoid leakage of secrets (https://github.com/ansible-collections/community.network/pull/206).
- enos_* modules - mark the ``passwords`` parameter as ``no_log`` to avoid leakage of secrets (https://github.com/ansible-collections/community.network/pull/206).
- iap_start_workflow - mark the ``token_key`` parameter as ``no_log`` to avoid leakage of secrets (https://github.com/ansible-collections/community.network/pull/206).
- icx_system - mark the ``auth_key`` parameter as ``no_log`` to avoid leakage of secrets (https://github.com/ansible-collections/community.network/pull/206).
- itential/iap_start_workflow - enabled ``no_log`` for the options ``token_key`` to prevent accidental disclosure (CVE-2021-20191, https://github.com/ansible-collections/community.network/pull/203).
- netscaler/netscaler_lb_monitor - enabled ``no_log`` for the options ``radkey`` to prevent accidental disclosure (CVE-2021-20191, https://github.com/ansible-collections/community.network/pull/203).
- netscaler_lb_monitor - mark the ``password`` and ``secondarypassword`` parameters as ``no_log`` to avoid leakage of secrets (https://github.com/ansible-collections/community.network/pull/206).

community.sops
~~~~~~~~~~~~~~

- community.sops.sops_encrypt - mark the ``aws_secret_access_key`` and ``aws_session_token`` parameters as ``no_log`` to avoid leakage of secrets (https://github.com/ansible-collections/community.sops/pull/54).

kubernetes.core
~~~~~~~~~~~~~~~

- kubectl - Warn about information disclosure when using options like ``kubectl_password``, ``kubectl_extra_args``, and ``kubectl_token`` to pass data through to the command line using the ``kubectl`` connection plugin (https://github.com/ansible-collections/kubernetes.core/pull/51).
- kubectl - connection plugin now redact kubectl_token and kubectl_password in console log (https://github.com/ansible-collections/kubernetes.core/issues/65).
- kubectl - redacted token and password from console log (https://github.com/ansible-collections/kubernetes.core/pull/159).

Bugfixes
--------

Ansible-base
~~~~~~~~~~~~

- Adjust various hard-coded action names to also include their ``ansible.builtin.`` and ``ansible.legacy.`` prefixed version (https://github.com/ansible/ansible/issues/71817, https://github.com/ansible/ansible/issues/71818, https://github.com/ansible/ansible/pull/71824).
- AnsibleModule - added arg ``ignore_invalid_cwd`` to ``AnsibleModule.run_command()``, to control its behaviour when ``cwd`` is invalid. (https://github.com/ansible/ansible/pull/72390)
- Apply ``_wrap_native_text`` only for builtin filters specified in STRING_TYPE_FILTERS.
- Collection callbacks were ignoring options and rules for stdout and adhoc cases.
- Collections - Ensure ``action_loader.get`` is called with ``collection_list`` to properly find collections when ``collections:`` search is specified (https://github.com/ansible/ansible/issues/72170)
- Documentation change to the apt module to reference lock files (https://github.com/ansible/ansible/issues/73079).
- Fix --list-tasks format `role_name : task_name` when task name contains the role name. (https://github.com/ansible/ansible/issues/72505)
- Fix ``RecursionError`` when templating large vars structures (https://github.com/ansible/ansible/issues/71920)
- Fix ansible-galaxy collection list to show collections in site-packages (https://github.com/ansible/ansible/issues/70147)
- Fix bytestring vs string comparison in module_utils.basic.is_special_selinux_path() so that special-cased filesystems which don't support SELinux context attributes still allow files to be manipulated on them. (https://github.com/ansible/ansible/issues/70244)
- Fix notifying handlers via `role_name : handler_name` when handler name contains the role name. (https://github.com/ansible/ansible/issues/70582)
- Fixed issue when `netstat` is either missing or doesn't have execution permissions leading to incorrect command being executed.
- Improve Ansible config deprecations to show the source of the deprecation (ansible-base). Also remove space before a comma in config deprecations (https://github.com/ansible/ansible/pull/72697).
- Pass the connection's timeout to connection plugins instead of the task's timeout.
- Provide more information in AnsibleUndefinedVariable (https://github.com/ansible/ansible/issues/55152)
- Skip invalid collection names when listing in ansible-doc instead of throwing exception. Issue#72257
- The ``docker`` and ``k8s`` action groups / module default groups now also support the moved modules in `community.docker <https://galaxy.ansible.com/community/docker>`_, `community.kubevirt <https://github.com/ansible-collections/community.kubevirt>`_, `community.okd <https://galaxy.ansible.com/community/okd>`_, and `kubernetes.core <https://galaxy.ansible.com/kubernetes/core>`_ (https://github.com/ansible/ansible/pull/72428).
- account for bug in Python 2.6 that occurs during interpreter shutdown to avoid stack trace
- ansible-doc - plugin option deprecations now also get ``collection_name`` added (https://github.com/ansible/ansible/pull/71735).
- ansible-doc - properly show plugin name when ``name:`` is used instead of ``<plugin_type>:`` (https://github.com/ansible/ansible/pull/71966).
- ansible-test - Always connect additional Docker containers to the network used by the current container (if any).
- ansible-test - Always map ``/var/run/docker.sock`` into test containers created by the ``--docker`` option if the docker host is not ``localhost``.
- ansible-test - Attempt to detect the Docker hostname instead of assuming ``localhost``.
- ansible-test - Change classification using ``--changed`` now consistently handles common configuration files for supported CI providers.
- ansible-test - Correctly detect changes in a GitHub pull request when running on Azure Pipelines.
- ansible-test - Correctly detect running in a Docker container on Azure Pipelines.
- ansible-test - Prefer container IP at ``.NetworkSettings.Networks.{NetworkName}.IPAddress`` over ``.NetworkSettings.IPAddress``.
- ansible-test - Skip installing requirements if they are already installed.
- ansible-test - The ``cs`` and ``openshift`` test plugins now search for containers on the current network instead of assuming the ``bridge`` network.
- ansible-test - The ``resource_prefix`` variable provided to tests running on Azure Pipelines is now converted to lowercase to match other CI providers.
- ansible-test - Using the ``--remote`` option on Azure Pipelines now works from a job running in a container.
- ansible-test - ``cryptography`` is now limited to versions prior to 3.2 only when an incompatible OpenSSL version (earlier than 1.1.0) is detected
- ansible-test - add constraint for ``cffi`` to prevent failure on systems with older versions of ``gcc`` (https://foss.heptapod.net/pypy/cffi/-/issues/480)
- ansible-test - convert target paths to unicode on Python 2 to avoid ``UnicodeDecodeError`` (https://github.com/ansible/ansible/issues/68398, https://github.com/ansible/ansible/pull/72623).
- ansible-test - improve classification of changes to ``.gitignore``, ``COPYING``, ``LICENSE``, ``Makefile``, and all files ending with one of ``.in`, ``.md`, ``.rst``, ``.toml``, ``.txt`` in the collection root directory (https://github.com/ansible/ansible/pull/72353).
- ansible-test validate-modules - when a module uses ``add_file_common_args=True`` and does not use a keyword argument for ``argument_spec`` in ``AnsibleModule()``, the common file arguments were not considered added during validation (https://github.com/ansible/ansible/pull/72334).
- async - Fix Python 3 interpreter parsing from module by comparing with bytes (https://github.com/ansible/ansible/issues/70690)
- async_wrapper - Fix race condition when ``~/.ansible_async`` folder tries to be created by multiple async tasks at the same time - https://github.com/ansible/ansible/issues/59306
- basic.AnsibleModule - AnsibleModule.run_command silently ignores a non-existent directory in the ``cwd`` argument (https://github.com/ansible/ansible/pull/72390).
- blockinfile - properly insert a block at the end of a file that does not have a trailing newline character (https://github.com/ansible/ansible/issues/72055)
- collection loader - fix bogus code coverage entries for synthetic packages
- dnf - fix filtering to avoid dependncy conflicts (https://github.com/ansible/ansible/issues/72316)
- dnf - it is now possible to specify both ``security: true`` and ``bugfix: true`` to install updates of both types. Previously, only security would get installed if both were true. (https://github.com/ansible/ansible/issues/70854)
- ensure 'local' connection always has the correct default user for actions to consume.
- facts - fix distribution fact for SLES4SAP (https://github.com/ansible/ansible/pull/71559).
- inventory - pass the vars dictionary to combine_vars instead of an individual key's value (https://github.com/ansible/ansible/issues/72975).
- is_string/vault - Ensure the is_string helper properly identifies AnsibleVaultEncryptedUnicode as a string (https://github.com/ansible/ansible/pull/71609)
- paramiko connection plugin - Ensure we only reset the connection when one has been previously established (https://github.com/ansible/ansible/issues/65812)
- pause - Fix indefinite hang when using a pause task on a background process (https://github.com/ansible/ansible/issues/32142)
- powershell - remove getting the PowerShell version from the env var ``POWERSHELL_VERSION``. This feature never worked properly and can cause conflicts with other libraries that use this var
- psrp - Fix hang when copying an empty file to the remote target
- remove redundant remote_user setting in play_context for local as plugin already does it, also removes fork/thread issue from use of pwd library.
- runas - create a new token when running as ``SYSTEM`` to ensure it has the full privileges assigned to that account
- set_mode_if_different - handle symlink if it is inside a directory with sticky bit set (https://github.com/ansible/ansible/pull/45198)
- systemd - account for templated unit files using ``@`` when searching for the unit file (https://github.com/ansible/ansible/pull/72347#issuecomment-730626228)
- systemd - follow up fix to https://github.com/ansible/ansible/issues/72338 to use ``list-unit-files`` rather than ``list-units`` in order to show all units files on the system.
- systemd - preserve the full unit name when using a templated service and ``systemd`` failed to parse dbus due to a known bug in ``systemd`` (https://github.com/ansible/ansible/pull/72985)
- systemd - work around bug with ``systemd`` 245 and 5.8 kernel that does not correctly report service state (https://github.com/ansible/ansible/issues/71528)
- url lookup - make sure that options supplied in ansible.cfg are actually used (https://github.com/ansible/ansible/pull/71736).
- user - AnsibleModule.run_command returns a tuple of return code, stdout and stderr. The module main function of the user module expects user.create_user to return a tuple of return code, stdout and stderr. Fix the locations where stdout and stderr got reversed.
- user - Local users with an expiry date cannot be created as the ``luseradd`` / ``lusermod`` commands do not support the ``-e`` option. Set the expiry time in this case via ``lchage`` after the user was created / modified. (https://github.com/ansible/ansible/issues/71942)
- user - do the right thing when ``password_lock=True`` and ``password`` are used together (https://github.com/ansible/ansible/issues/72992)
- wait_for - catch and ignore errors when getting active connections with psutil (https://github.com/ansible/ansible/issues/72322)

amazon.aws
~~~~~~~~~~

- ec2 - Code fix so module can create ec2 instances with ``ec2_volume_iops`` option (https://github.com/ansible-collections/amazon.aws/pull/177).
- ec2 - ignore terminated instances and instances that are shutting down when starting and stopping (https://github.com/ansible-collections/amazon.aws/issues/146).
- ec2_group - Fixes error handling during tagging failures (https://github.com/ansible-collections/amazon.aws/issues/210).
- ec2_group_info - Code fix so module works with Python 3.8 (make dict immutable in loop) (https://github.com/ansible-collections/amazon.aws/pull/181)

ansible.netcommon
~~~~~~~~~~~~~~~~~

- Add netconf_config integration tests for nxos (https://github.com/ansible-collections/ansible.netcommon/pull/185)
- Added support for private key based authentication with libssh transport (https://github.com/ansible-collections/ansible.netcommon/issues/168)
- Fix GetReply object has no attribute strip() (https://github.com/ansible-collections/cisco.iosxr/issues/97)
- Fix config diff logic if parent configuration is present more than once in the candidate config and update docs (https://github.com/ansible-collections/ansible.netcommon/pull/189)
- Fix missing changed from net_get (https://github.com/ansible-collections/ansible.netcommon/issues/198)
- Fix netconf_config module integration test issuea (https://github.com/ansible-collections/ansible.netcommon/pull/177)
- Fix restconf_config incorrectly spoofs HTTP 409 codes (https://github.com/ansible-collections/ansible.netcommon/issues/191)
- Fixed ipaddr filter plugins in ansible.netcommon collections is not working with latest Ansible (https://github.com/ansible-collections/ansible.netcommon/issues/157)
- Fixed netconf_rpc task fails due to encoding issue in the response (https://github.com/ansible-collections/ansible.netcommon/issues/151)
- Fixed ssh_type none issue while using net_put and net_get module (https://github.com/ansible-collections/ansible.netcommon/issues/153)
- Fixed unit tests under python3.5
- Split checks for prompt and errors in network_cli so that detected errors are not lost if the prompt is in a later chunk.
- cli_parse - Ensure only native types are returned to the control node from the parser.
- ipaddr filter - query "address/prefix" (also: "gateway", "gw", "host/prefix", "hostnet", and "router") now handles addresses with /32 prefix or /255.255.255.255 netmask
- netconf - Changed log level for message of using default netconf plugin to match the level used when a platform-specific netconf plugin is found
- network_cli - Update underlying ssh connection's play_context in update_play_context, so that the username or password can be updated

ansible.utils
~~~~~~~~~~~~~

- linting and formatting for CI

ansible.windows
~~~~~~~~~~~~~~~

- setup - handle PATH environment vars that contain blank entries like ``C:\Windows;;C:\Program Files`` - https://github.com/ansible-collections/ansible.windows/pull/78#issuecomment-745229594
- win_copy - fix bug when copying a single file during a folder copy operation
- win_package - Do not fail when trying to set SYSTEM ACE on read only path - https://github.com/ansible-collections/ansible.windows/issues/142
- win_service - Fix edge case bug when running against PowerShell 5.0 - https://github.com/ansible-collections/ansible.windows/issues/125
- win_service - Fix opening services with limited rights - https://github.com/ansible-collections/ansible.windows/issues/118
- win_service - Fix up account name lookup when dealing with netlogon formatted accounts (``DOMAIN\account``) - https://github.com/ansible-collections/ansible.windows/issues/156
- win_service_info - Provide failure details in warning when failing to open service

arista.eos
~~~~~~~~~~

- Add version key to galaxy.yaml to work around ansible-galaxy bug
- Added 'mode' key to eos_interfaces to handle the layer2/3 switchport mode of an interface.
- Added fix to maintain the idempotency while using overridden operation.
- Check for existing configuration when trunk_allowed_vlans is issued, is added.
- Fix yaml formatting errors in documentation.
- Fixed typo and index out of range errors while handling protocol_options. (https://github.com/ansible-collections/arista.eos/pull/115)
- Uncap required ansible version in our collection.
- Update default values in module argspec and docs (https://github.com/ansible-collections/arista.eos/pull/154).
- Update docs to clarify the idemptonecy releated caveat and add it in the output warnings (https://github.com/ansible-collections/ansible.netcommon/pull/189)
- fixes eos interfaces rm where interface in description resulted in failure (https://github.com/ansible-collections/arista.eos/issues/86).
- replace list.copy() with list[:] to support python 2.7  and fix idempotent issue with replaced and overridden (https://github.com/ansible-collections/arista.eos/pull/142).
- updated config dict, with duplex key when speed changes from 'x' to 'forced x' (https://github.com/ansible-collections/arista.eos/pull/120).

cisco.aci
~~~~~~~~~

- Existing_config variable is not reset during loop
- Fix convertion of json/yaml payload to xml in aci_rest
- Fix dump of config for aci_rest
- Fix galaxy import warnings
- Fix how validity of private key/private key file is checked to support new types
- Fix incorrect domain types in aci_domain_to_encap_pool module
- Fix issue of "current" in firmware_source module
- Fix sanity issue in aci_epg_to_domain
- Fix sanity issue in aci_rest and bump version to v1.0.1

cisco.asa
~~~~~~~~~

- Add version key to galaxy.yaml to work around ansible-galaxy bug
- To fix ASA OGs module where delete by name was not resulting to an expected behaviour (https://github.com/ansible-collections/cisco.asa/pull/77).
- Update asa acls RM to use newer RM design approach and addeed support for any4/any6 feature (https://github.com/ansible-collections/cisco.asa/pull/64).

cisco.ios
~~~~~~~~~

- Add support for interface type Virtual-Template (https://github.com/ansible-collections/cisco.ios/pull/154).
- Add support size and df_bit options for ios_ping (https://github.com/ansible-collections/cisco.ios/pull/228).
- Add version key to galaxy.yaml to work around ansible-galaxy bug.
- Added support for interface Tunnel (https://github.com/ansible-collections/cisco.ios/pull/145).
- Fix element type of ios_command's command parameter (https://github.com/ansible-collections/cisco.ios/pull/151).
- IOS resource modules minor doc updates (https://github.com/ansible-collections/cisco.ios/pull/233).
- IOS_CONFIG, incorrectly claims success when Command Rejected (https://github.com/ansible-collections/cisco.ios/pull/215).
- To enable ios ospfv3 integration tests (https://github.com/ansible-collections/cisco.ios/pull/165).
- To fix IOS static routes idempotency issue coz of netmask to cidr conversion (https://github.com/ansible-collections/cisco.ios/pull/177).
- To fix ios_ospf_interfaces resource module authentication param behaviour (https://github.com/ansible-collections/cisco.ios/issues/209).
- To fix ios_static_routes facts parsing in presence of interface (https://github.com/ansible-collections/cisco.ios/pull/225).
- To fix ios_static_routes where interface ip route-cache config was being parsed and resulted traceback (https://github.com/ansible-collections/cisco.ios/pull/176).
- To fix ios_vlans traceback bug when the name had Remote in it and added unit TC for the module (https://github.com/ansible-collections/cisco.ios/pull/179).
- To fix the incorrect command displayed under ios_l3_interfaces resource module docs (https://github.com/ansible-collections/cisco.ios/pull/149).
- To fix the traceback issue for longer vlan name having more than 32 characters (https://github.com/ansible-collections/cisco.ios/pull/182).
- Update doc to clarify on input config pattern (https://github.com/ansible-collections/cisco.ios/pull/220).
- Updating ios acls module to use newer CLI RM approach to resolve all of the ACL related bugs (https://github.com/ansible-collections/cisco.ios/pull/211).

cisco.iosxr
~~~~~~~~~~~

- Add version key to galaxy.yaml to work around ansible-galaxy bug
- Fix iosxr_acls throwing a traceback with overridden (https://github.com/ansible-collections/cisco.iosxr/issues/87).
- Update docs to clarify the idemptonecy releated caveat and add it in the output warnings (https://github.com/ansible-collections/ansible.netcommon/pull/189)
- require one to specify a banner delimiter in order to fix a timeout when using multi-line strings

cisco.meraki
~~~~~~~~~~~~

- Remove test output as it made the collection, and Ansible, huge.
- meraki_device - Support pagination. This allows for more than 1,000 devices to be listed at a time.
- meraki_management_interface - Fix crash when modifying a non-MX management interface.
- meraki_network - Fix bug where local or remote settings always show changed.
- meraki_network - Support pagination. This allows for more than 1,000 networks to be listed at a time.

cisco.mso
~~~~~~~~~

- Fix anp idempotency issue
- Fix crash issue when using irrelevant site-template
- Fix default value for l2Stretch in mso_schema_template_bd module
- Fix default value for mso_schema state parameter
- Fix deletion of schema when wrong template is provided in single template schema
- Fix examples for mso_schema
- Fix examples in documentation for mso_schema_template_l3out and mso_user
- Fix galaxy-importer check warnings
- Fix issue on mso_schema_site_vrf_region_cidr_subnet to allow an AWS subnet to be used for a TGW Attachment (Hub Network)
- Fix module name in example of mso_schema_site_vrf_region
- Fix mso_backup upload issue
- Fix naming issue in deploy module
- Fix sanity test error mso_schema_site_bd
- Fix some coding standard and improvements to contributed mso_dhcp_relay modules and test files
- Fix space in asssertion
- Fix space in site_anp_epg_domain
- Fix space in test file
- Remove author emails due to length restriction
- Remove dead code branch in mso_schema_template
- Remove space from template name in all modules
- Remove space in template name

cisco.nxos
~~~~~~~~~~

- Add support for interfaces in mode 'fabricpath' to l2_interfaces (https://github.com/ansible-collections/cisco.nxos/issues/220).
- Add version key to galaxy.yaml to work around ansible-galaxy bug
- Allow `fex-fabric` option for mode key (https://github.com/ansible-collections/cisco.nxos/issues/166).
- Allow enabling `fabric forwarding` feature through nxos_feature (https://github.com/ansible-collections/cisco.nxos/issues/213).
- Allow nxos_user to run with MDS (https://github.com/ansible-collections/cisco.nxos/issues/163).
- Allow tag updates with state replaced (https://github.com/ansible-collections/cisco.nxos/issues/197).
- Correctly parse facts for lacp interfaces mode information (https://github.com/ansible-collections/cisco.nxos/pull/164).
- Fix for nxos smu issue (https://github.com/ansible-collections/cisco.nxos/pull/160).
- Fix for nxos_lag_interfaces issue (https://github.com/ansible-collections/cisco.nxos/pull/194).
- Fix regex for parsing configuration in nxos_lag_interfaces.
- Fix regexes in nxos_acl_interfaces facts and some code cleanup (https://github.com/ansible-collections/cisco.nxos/issues/149).
- Fix rendering of `log-adjacency-changes` commands.
- Fixes for nxos rpm issue (https://github.com/ansible-collections/cisco.nxos/pull/173).
- Fixes traceback while parsing power supply info in nxos_facts for newer NX-OS releases (https://github.com/ansible-collections/cisco.nxos/issues/192).
- Handle domain-name properly with vrf contexts (https://github.com/ansible-collections/cisco.nxos/issues/234).
- Make sure that the OSPF modules work properly when process_id is a string (https://github.com/ansible-collections/cisco.nxos/issues/198).
- Parse interface contexts properly (https://github.com/ansible-collections/cisco.nxos/issues/195).
- Preserve whitespaces in banner text (https://github.com/ansible-collections/cisco.nxos/pull/146).
- Properly handle partial matches in community string (https://github.com/ansible-collections/cisco.nxos/issues/203).
- Update argspecs with default value for parameters.
- Update docs to clarify the idemptonecy releated caveat and add it in the output warnings (https://github.com/ansible-collections/ansible.netcommon/pull/189)
- Update regex to accept the platform "N77" as supporting fabricpath.
- Vlan config diff was not removing default values
- config replace is actually supported for devices other than N9K and hence we should not fail, and instead let the device handle it (https://github.com/ansible-collections/cisco.nxos/issues/215).

cloudscale_ch.cloud
~~~~~~~~~~~~~~~~~~~

- Fix inventory plugin failing to launch (https://github.com/cloudscale-ch/ansible-collection-cloudscale/issues/49).

community.aws
~~~~~~~~~~~~~

- aws_kms_info - fixed incompatibility with external and custom key-store keys. The module was attempting to call `GetKeyRotationStatus`, which raises `UnsupportedOperationException` for these key types (https://github.com/ansible-collections/community.aws/pull/311).
- aws_ssm connection plugin - namespace file uploads to S3 into unique folders per host, to prevent name collisions. Also deletes files from S3 to ensure temp files are not left behind. (https://github.com/ansible-collections/community.aws/issues/221, https://github.com/ansible-collections/community.aws/issues/222)
- ec2_win_password - on success return state as not changed (https://github.com/ansible-collections/community.aws/issues/145)
- ec2_win_password - return failed if unable to decode the password (https://github.com/ansible-collections/community.aws/issues/142)
- ecs_service - fix element type for ``load_balancers`` parameter (https://github.com/ansible-collections/community.aws/issues/265).
- ecs_taskdefinition - fixes elements type for ``containers`` parameter (https://github.com/ansible-collections/community.aws/issues/264).
- iam_policy - Added jittered_backoff to handle AWS rate limiting (https://github.com/ansible-collections/community.aws/pull/324).
- iam_policy_info - Added jittered_backoff to handle AWS rate limiting (https://github.com/ansible-collections/community.aws/pull/324).
- kinesis_stream - fixes issue where kinesis streams with > 100 shards get stuck in an infinite loop (https://github.com/ansible-collections/community.aws/pull/93)
- rds_instance - fixed tag type conversion issue for creating read replicas.
- s3_sync - fix chunk_size calculation (https://github.com/ansible-collections/community.aws/issues/272)

community.crypto
~~~~~~~~~~~~~~~~

- acme_certificate - error when requested challenge type is not found for non-valid challenges, instead of hanging on step 2 (https://github.com/ansible-collections/community.crypto/issues/171, https://github.com/ansible-collections/community.crypto/pull/173).
- openssl_pkcs12 - do not crash when reading PKCS#12 file which has no private key and/or no main certificate (https://github.com/ansible-collections/community.crypto/issues/103).
- openssl_pkcs12 - report the correct state when ``action`` is ``parse`` (https://github.com/ansible-collections/community.crypto/issues/143).
- support code - improve handling of certificate and certificate signing request (CSR) loading with the ``cryptography`` backend when errors occur (https://github.com/ansible-collections/community.crypto/issues/138, https://github.com/ansible-collections/community.crypto/pull/139).
- x509_certificate - fix ``entrust`` provider, which was broken since community.crypto 0.1.0 due to a feature added before the collection move (https://github.com/ansible-collections/community.crypto/pull/135).

community.docker
~~~~~~~~~~~~~~~~

- docker connection plugin - fix Docker version parsing, as some docker versions have a leading ``v`` in the output of the command ``docker version --format "{{.Server.Version}}"`` (https://github.com/ansible-collections/community.docker/pull/76).
- docker_container - allow IPv6 zones (RFC 4007) in bind IPs (https://github.com/ansible-collections/community.docker/pull/66).
- docker_container - the validation for ``capabilities`` in ``device_requests`` was incorrect (https://github.com/ansible-collections/community.docker/issues/42, https://github.com/ansible-collections/community.docker/pull/43).
- docker_image - fix crash on loading images with versions of Docker SDK for Python before 2.5.0 (https://github.com/ansible-collections/community.docker/issues/72, https://github.com/ansible-collections/community.docker/pull/73).
- docker_image - if ``push=true`` is used with ``repository``, and the image does not need to be tagged, still push. This can happen if ``repository`` and ``name`` are equal (https://github.com/ansible-collections/community.docker/issues/52, https://github.com/ansible-collections/community.docker/pull/53).
- docker_image - report error when loading a broken archive that contains no image (https://github.com/ansible-collections/community.docker/issues/46, https://github.com/ansible-collections/community.docker/pull/55).
- docker_image - report error when the loaded archive does not contain the specified image (https://github.com/ansible-collections/community.docker/issues/41, https://github.com/ansible-collections/community.docker/pull/55).
- docker_login - fix internal config file storage to handle credentials for more than one registry (https://github.com/ansible-collections/community.general/issues/1117).

community.general
~~~~~~~~~~~~~~~~~

- aerospike_migrations - handle exception when unstable-cluster is returned (https://github.com/ansible-collections/community.general/pull/900).
- aix_filesystem - fix issues with ismount module_util pathing for Ansible 2.9 (https://github.com/ansible-collections/community.general/pull/567).
- apache2_module - amend existing module identifier workaround to also apply to updated Shibboleth modules (https://github.com/ansible-collections/community.general/issues/1379).
- beadm - fixed issue "list object has no attribute split" (https://github.com/ansible-collections/community.general/issues/791).
- bigpanda - removed the dynamic default for ``host`` param (https://github.com/ansible-collections/community.general/pull/1423).
- bitbucket_pipeline_variable - change pagination logic for pipeline variable get API (https://github.com/ansible-collections/community.general/issues/1425).
- capabilities - fix for a newer version of libcap release (https://github.com/ansible-collections/community.general/pull/1061).
- cobbler inventory plugin - ``name`` needed FQCN (https://github.com/ansible-collections/community.general/pull/722).
- cobbler inventory script - add Python 3 support (https://github.com/ansible-collections/community.general/issues/638).
- composer - fix bug in command idempotence with composer v2 (https://github.com/ansible-collections/community.general/issues/1179).
- consul_kv lookup - fix ``ANSIBLE_CONSUL_URL`` environment variable handling (https://github.com/ansible/ansible/issues/51960).
- consul_kv lookup - fix arguments handling (https://github.com/ansible-collections/community.general/pull/303).
- digital_ocean_tag_info - fix crash when querying for an individual tag (https://github.com/ansible-collections/community.general/pull/615).
- django_manage - fix idempotence for ``createcachetable`` (https://github.com/ansible-collections/community.general/pull/699).
- dnsmadeeasy - fix HTTP 400 errors when creating a TXT record (https://github.com/ansible-collections/community.general/issues/1237).
- doas become plugin - address a bug with the parameters handling that was breaking the plugin in community.general when ``become_flags`` and ``become_user`` were not explicitly specified (https://github.com/ansible-collections/community.general/pull/704).
- dsv lookup - use correct dict usage (https://github.com/ansible-collections/community.general/pull/743).
- dzdo become plugin - address a bug with the parameters handling that was breaking the plugin in community.general when ``become_user`` was not explicitly specified (https://github.com/ansible-collections/community.general/pull/708).
- filesystem - add option ``state`` with default ``present``. When set to ``absent``, filesystem signatures are removed (https://github.com/ansible-collections/community.general/issues/355).
- filesystem - do not fail when ``resizefs=yes`` and ``fstype=xfs`` if there is nothing to do, even if the filesystem is not mounted. This only covers systems supporting access to unmounted XFS filesystems. Others will still fail (https://github.com/ansible-collections/community.general/issues/1457, https://github.com/ansible-collections/community.general/pull/1478).
- filesystem - resizefs of xfs filesystems is fixed. Filesystem needs to be mounted.
- flatpak - use of the ``--non-interactive`` argument instead of ``-y`` when possible (https://github.com/ansible-collections/community.general/pull/1246).
- gcp_storage_files lookup plugin - make sure that plugin errors out on initialization if the required library is not found, and not on load-time (https://github.com/ansible-collections/community.general/pull/1297).
- gem - fix get_installed_versions: correctly parse ``default`` version (https://github.com/ansible-collections/community.general/pull/783).
- git_config - now raises an error for non-existent repository paths (https://github.com/ansible-collections/community.general/issues/630).
- git_config - using list instead of string as first parameter in the ``run_command()`` call (https://github.com/ansible-collections/community.general/issues/1021).
- gitlab_group - added description parameter to ``createGroup()`` call (https://github.com/ansible-collections/community.general/issues/138).
- gitlab_group_variable - support for GitLab pagination limitation by iterating over GitLab variable pages (https://github.com/ansible-collections/community.general/pull/968).
- gitlab_project_variable - support for GitLab pagination limitation by iterating over GitLab variable pages (https://github.com/ansible-collections/community.general/pull/968).
- gitlab_runner - fix compatiblity with some versions of python-gitlab (https://github.com/ansible-collections/community.general/pull/1491).
- gitlab_user - make updates to the ``isadmin``, ``password`` and ``confirm`` options of an already existing GitLab user work (https://github.com/ansible-collections/community.general/pull/1724).
- homebrew - add default search path for ``brew`` on Apple silicon hardware (https://github.com/ansible-collections/community.general/pull/1679).
- homebrew - fix package name validation for packages containing hypen ``-`` (https://github.com/ansible-collections/community.general/issues/1037).
- homebrew_cask - add default search path for ``brew`` on Apple silicon hardware (https://github.com/ansible-collections/community.general/pull/1679).
- homebrew_cask - fix package name validation for casks containing hypen ``-`` (https://github.com/ansible-collections/community.general/issues/1037).
- homebrew_cask - fixed issue where a cask with ``@`` in the name is incorrectly reported as invalid (https://github.com/ansible-collections/community.general/issues/733).
- homebrew_tap - add default search path for ``brew`` on Apple silicon hardware (https://github.com/ansible-collections/community.general/pull/1679).
- icinga2_host - fix returning error codes (https://github.com/ansible-collections/community.general/pull/335).
- influxdb - fix usage of path for older version of python-influxdb (https://github.com/ansible-collections/community.general/issues/997).
- ini_file - check for parameter ``value`` if ``state`` is ``present`` and ``allow_no_value`` is ``false`` (https://github.com/ansible-collections/community.general/issues/479).
- interfaces_file - escape regular expression characters in old value (https://github.com/ansible-collections/community.general/issues/777).
- inventory plugins - allow FQCN in ``plugin`` option (https://github.com/ansible-collections/community.general/pull/722).
- ipa_hostgroup - fix an issue with load-balanced ipa and cookie handling with Python 3 (https://github.com/ansible-collections/community.general/issues/737).
- iptables_state - fix race condition between module and its action plugin (https://github.com/ansible-collections/community.general/issues/1136).
- jenkins_plugin - replace MD5 checksum verification with SHA1 due to MD5 being disabled on systems with FIPS-only algorithms enabled (https://github.com/ansible/ansible/issues/34304).
- jira - ``fetch`` and ``search`` no longer indicate that something changed (https://github.com/ansible-collections/community.general/pull/1536).
- jira - ensured parameter ``issue`` is mandatory for operation ``transition`` (https://github.com/ansible-collections/community.general/pull/1536).
- jira - improve error message handling (https://github.com/ansible-collections/community.general/pull/311).
- jira - improve error message handling with multiple errors (https://github.com/ansible-collections/community.general/pull/707).
- jira - module no longer incorrectly reports change for information gathering operations (https://github.com/ansible-collections/community.general/pull/1536).
- jira - provide error message raised from exception (https://github.com/ansible-collections/community.general/issues/1504).
- jira - replaced custom parameter validation with ``required_if`` (https://github.com/ansible-collections/community.general/pull/1536).
- json_query - handle ``AnsibleUnicode`` and ``AnsibleUnsafeText`` (https://github.com/ansible-collections/community.general/issues/320).
- keycloak module_utils - provide meaningful error message to user when auth URL does not start with http or https (https://github.com/ansible-collections/community.general/issues/331).
- launchd - fix for user-level services (https://github.com/ansible-collections/community.general/issues/896).
- launchd - handle deprecated APIs like ``readPlist`` and ``writePlist`` in ``plistlib`` (https://github.com/ansible-collections/community.general/issues/1552).
- ldap modules - add ``sasl_class`` parameter to support passwordless SASL authentication via GSSAPI (kerberos), next to external (https://github.com/ansible-collections/community.general/issues/1523).
- ldap_entry - improvements in documentation, simplifications and replaced code with better ``AnsibleModule`` arguments (https://github.com/ansible-collections/community.general/pull/1516).
- ldap_search - ignore returned referrals (https://github.com/ansible-collections/community.general/issues/1067).
- ldap_search - the module no longer incorrectly reports a change (https://github.com/ansible-collections/community.general/issues/1040).
- linode inventory plugin - make sure that plugin errors out on initialization if the required library is not found, and not on load-time (https://github.com/ansible-collections/community.general/pull/1297).
- lldp - use ``get_bin_path`` to locate the ``lldpctl`` executable (https://github.com/ansible-collections/community.general/pull/1643).
- lxc_container - fix the type of the ``container_config`` parameter. It is now processed as a list and not a string (https://github.com/ansible-collections/community.general/pull/216).
- macports - fix failure to install a package whose name is contained within an already installed package's name or variant (https://github.com/ansible-collections/community.general/issues/1307).
- make - fixed ``make`` parameter used for check mode when running a non-GNU ``make`` (https://github.com/ansible-collections/community.general/pull/1574).
- mas - fix ``invalid literal`` when no app can be found (https://github.com/ansible-collections/community.general/pull/1436).
- maven_artifact - handle timestamped snapshot version strings properly (https://github.com/ansible-collections/community.general/issues/709).
- memcached cache plugin - make sure that plugin errors out on initialization if the required library is not found, and not on load-time (https://github.com/ansible-collections/community.general/pull/1297).
- monit - add support for all monit service checks (https://github.com/ansible-collections/community.general/pull/1532).
- monit - fix modules ability to determine the current state of the monitored process (https://github.com/ansible-collections/community.general/pull/1107).
- nios_fixed_address, nios_host_record, nios_zone - removed redundant parameter aliases causing warning messages to incorrectly appear in task output (https://github.com/ansible-collections/community.general/issues/852).
- nios_host_record - fix to remove ``aliases`` (CNAMES) for configuration comparison (https://github.com/ansible-collections/community.general/issues/1335).
- nios_member - fix Python 3 compatibility with nios api ``member_normalize`` function (https://github.com/ansible-collections/community.general/issues/1526).
- nmcli - cannot modify ``ifname`` after connection creation (https://github.com/ansible-collections/community.general/issues/1089).
- nmcli - fix idempotetency when modifying an existing connection (https://github.com/ansible-collections/community.general/issues/481).
- nmcli - remove ``bridge-slave`` from list of IP based connections ((https://github.com/ansible-collections/community.general/issues/1500).
- nmcli - set ``C`` locale when executing ``nmcli`` (https://github.com/ansible-collections/community.general/issues/989).
- nmcli - use consistent autoconnect parameters (https://github.com/ansible-collections/community.general/issues/459).
- npm - handle json decode exception while parsing command line output (https://github.com/ansible-collections/community.general/issues/1614).
- oc connection plugin - ``transport`` needed FQCN (https://github.com/ansible-collections/community.general/pull/722).
- omapi_host - fix compatibility with Python 3 (https://github.com/ansible-collections/community.general/issues/787).
- onepassword lookup plugin - updated to support password items, which place the password field directly in the payload's ``details`` attribute (https://github.com/ansible-collections/community.general/pull/1610).
- osx_defaults - fix handling negative integers (https://github.com/ansible-collections/community.general/issues/134).
- osx_defaults - unquote values and unescape double quotes when reading array values (https://github.com/ansible-collections/community.general/pull/358).
- packet_net.py inventory script - fixed failure w.r.t. operating system retrieval by changing array subscription back to attribute access (https://github.com/ansible-collections/community.general/pull/891).
- pacman - treat package names containing .zst as package files during installation (https://www.archlinux.org/news/now-using-zstandard-instead-of-xz-for-package-compression/, https://github.com/ansible-collections/community.general/pull/650).
- pamd - added logic to retain the comment line (https://github.com/ansible-collections/community.general/issues/1394).
- parted - change the regex that decodes the partition size to better support different formats that parted uses. Change the regex that validates parted's version string (https://github.com/ansible-collections/community.general/pull/1695).
- parted - fix creating partition when label is changed (https://github.com/ansible-collections/community.general/issues/522).
- passwordstore lookup plugin - always use explicit ``show`` command to retrieve password. This ensures compatibility with ``gopass`` and avoids problems when password names equal ``pass`` commands (https://github.com/ansible-collections/community.general/pull/1493).
- passwordstore lookup plugin - fix compatibility with gopass when used with ``create=true``. While pass returns 1 on a non-existent password, gopass returns 10, or 11, depending on whether a similar named password was stored. We now just check standard output and that the return code is not zero (https://github.com/ansible-collections/community.general/pull/1589).
- pbrun become plugin - address a bug with the parameters handling that was breaking the plugin in community.general when ``become_user`` was not explicitly specified (https://github.com/ansible-collections/community.general/pull/708).
- pkg5 - now works when Python 3 is used on the target (https://github.com/ansible-collections/community.general/pull/789).
- profitbricks_nic - removed the dynamic default for ``name`` param (https://github.com/ansible-collections/community.general/pull/1423).
- profitbricks_nic - replaced code with ``required`` and ``required_if`` (https://github.com/ansible-collections/community.general/pull/1423).
- proxmox_kvm - defer error-checking for non-existent VMs in order to fix idempotency of tasks using ``state=absent`` and properly recognize a success (https://github.com/ansible-collections/community.general/pull/811).
- proxmox_kvm - fix issue causing linked clones not being create by allowing ``format=unspecified`` (https://github.com/ansible-collections/community.general/issues/1027).
- proxmox_kvm - ignore unsupported ``pool`` parameter on update (https://github.com/ansible-collections/community.general/pull/1258).
- proxmox_kvm - improve handling of long-running tasks by creating a dedicated function (https://github.com/ansible-collections/community.general/pull/831).
- redfish_info module, redfish_utils module utils - add ``Name`` and ``Id`` properties to output of Redfish inventory commands (https://github.com/ansible-collections/community.general/issues/1650).
- redfish_info module, redfish_utils module utils - correct ``PartNumber`` property name in Redfish ``GetMemoryInventory`` command (https://github.com/ansible-collections/community.general/issues/1483).
- redfish_info, redfish_config, redfish_command - Fix Redfish response payload decode on Python 3.5 (https://github.com/ansible-collections/community.general/issues/686)
- redis - fixes parsing of config values which should not be converted to bytes (https://github.com/ansible-collections/community.general/pull/1079).
- redis cache plugin - make sure that plugin errors out on initialization if the required library is not found, and not on load-time (https://github.com/ansible-collections/community.general/pull/1297).
- rhn_channel - Python 2.7.5 fails if the certificate should not be validated. Fixed this by creating the correct ``ssl_context`` (https://github.com/ansible-collections/community.general/pull/470).
- saltstack connection plugin - use ``hashutil.base64_decodefile`` to ensure that the file checksum is preserved (https://github.com/ansible-collections/community.general/pull/1472).
- selective - mark task failed correctly (https://github.com/ansible/ansible/issues/63767).
- sendgrid - update documentation and warn user about sendgrid Python library version (https://github.com/ansible-collections/community.general/issues/1553).
- sensu-silence module - fix json parsing of sensu API responses on Python 3.5 (https://github.com/ansible-collections/community.general/pull/1703).
- slack - avoid trying to update existing message when sending messages that contain the string "ts" (https://github.com/ansible-collections/community.general/issues/1097).
- slack - fix ``xox[abp]`` token identification to capture everything after ``xox[abp]``, as the token is the only thing that should be in this argument (https://github.com/ansible-collections/community.general/issues/862).
- snmp_facts - skip ``EndOfMibView`` values (https://github.com/ansible/ansible/issues/49044).
- solaris_zone - fixed issue trying to configure zone in Python 3 (https://github.com/ansible-collections/community.general/issues/1081).
- syslogger - update ``syslog.openlog`` API call for older Python versions, and improve error handling (https://github.com/ansible-collections/community.general/issues/953).
- syspatch - fix bug where not setting ``apply=true`` would result in error (https://github.com/ansible-collections/community.general/pull/360).
- terraform - fix ``init_reconfigure`` option for proper CLI args (https://github.com/ansible-collections/community.general/pull/1620).
- terraform - fix incorrectly reporting a status of unchanged when number of resources added or destroyed are multiples of 10 (https://github.com/ansible-collections/community.general/issues/561).
- terraform - improve result code checking when executing terraform commands (https://github.com/ansible-collections/community.general/pull/1632).
- timezone - support Python3 on macos/darwin (https://github.com/ansible-collections/community.general/pull/945).
- udm_user - removed the dynamic default for ``userexpiry`` param (https://github.com/ansible-collections/community.general/pull/1423).
- utm_network_interface_address - changed param type from invalid 'boolean' to valid 'bool' (https://github.com/ansible-collections/community.general/pull/1423).
- utm_proxy_exception - four parameters had elements types set as 'string' (invalid), changed to 'str' (https://github.com/ansible-collections/community.general/pull/1399).
- vmadm - simplification of code (https://github.com/ansible-collections/community.general/pull/1415).
- xfconf - add in missing return values that are specified in the documentation (https://github.com/ansible-collections/community.general/issues/1418).
- xfconf - make it work in non-english locales (https://github.com/ansible-collections/community.general/pull/744).
- xfconf - parameter ``value`` no longer required for state ``absent`` (https://github.com/ansible-collections/community.general/issues/1329).
- xfconf - xfconf no longer passing the command args as a string, but rather as a list (https://github.com/ansible-collections/community.general/issues/1328).
- yaml callback plugin - do not remove non-ASCII Unicode characters from multiline string output (https://github.com/ansible-collections/community.general/issues/1519).
- yarn - fixed an index out of range error when no outdated packages where returned by yarn executable (see https://github.com/ansible-collections/community.general/pull/474).
- yarn - fixed an too many values to unpack error when scoped packages are installed (see https://github.com/ansible-collections/community.general/pull/474).
- zfs - fixed ``invalid character '@' in pool name"`` error when working with snapshots on a root zvol (https://github.com/ansible-collections/community.general/issues/932).
- zypper - force ``LANG=C`` to as zypper is looking in XML output where attribute could be translated (https://github.com/ansible-collections/community.general/issues/1175).

community.hashi_vault
~~~~~~~~~~~~~~~~~~~~~

- hashi_vault - ``mount_point`` parameter did not work with ``aws_iam_login`` auth method (https://github.com/ansible-collections/community.hashi_vault/issues/7)
- hashi_vault - fallback logic for handling deprecated style of auth in hvac was not implemented correctly (https://github.com/ansible-collections/community.hashi_vault/pull/33).
- hashi_vault - parameter ``mount_point`` does not work with JWT auth (https://github.com/ansible-collections/community.hashi_vault/issues/29).
- hashi_vault - tokens without ``lookup-self`` ability can't be used because of validation (https://github.com/ansible-collections/community.hashi_vault/issues/18).

community.kubernetes
~~~~~~~~~~~~~~~~~~~~

- common - handle exception raised due to DynamicClient (https://github.com/ansible-collections/community.kubernetes/pull/224).
- helm - add replace parameter (https://github.com/ansible-collections/community.kubernetes/issues/106).
- k8s (inventory) - Set the connection plugin and transport separately (https://github.com/ansible-collections/community.kubernetes/pull/208).
- k8s (inventory) - Specify FQCN for k8s inventory plugin to fix use with Ansible 2.9 (https://github.com/ansible-collections/community.kubernetes/pull/250).
- k8s - Fix sanity test 'compile' failing because of positional args (https://github.com/ansible-collections/community.kubernetes/issues/260).
- k8s_info - add wait functionality (https://github.com/ansible-collections/community.kubernetes/issues/18).

community.kubevirt
~~~~~~~~~~~~~~~~~~

- kubevirt - Add aliases 'interface_name' for network_name (https://github.com/ansible/ansible/issues/55641).

community.mysql
~~~~~~~~~~~~~~~

- mysql modules - fix crash when ``!includedir`` option is in config file (https://github.com/ansible-collections/community.mysql/issues/46).
- mysql_db - fix false warning related to ``unsafe_login_password`` option (https://github.com/ansible-collections/community.mysql/issues/33).
- mysql_query - fix failing when single-row query contains commas (https://github.com/ansible-collections/community.mysql/issues/51).
- mysql_replication - fix crashes of mariadb >= 10.5.1 and mysql >= 8.0.22 caused by using deprecated terminology (https://github.com/ansible-collections/community.mysql/issues/70).
- mysql_user - add ``SHOW_ROUTINE`` privilege support (https://github.com/ansible-collections/community.mysql/issues/86).
- mysql_user - added tests to verify that TLS requirements are removed with an empty ``tls_requires`` option (https://github.com/ansible-collections/community.mysql/issues/20).
- mysql_user - correct procedure to check existing TLS requirements (https://github.com/ansible-collections/community.mysql/pull/26).
- mysql_user - fix module's crash when modifying a user with ``host_all`` (https://github.com/ansible-collections/community.mysql/issues/39).
- mysql_user - fixed change detection when using append_privs (https://github.com/ansible-collections/community.mysql/pull/72).
- mysql_user - fixed creating user with encrypted password in MySQL 8.0 (https://github.com/ansible-collections/community.mysql/pull/79).
- mysql_user - minor syntax fixes (https://github.com/ansible-collections/community.mysql/pull/26).

community.network
~~~~~~~~~~~~~~~~~

- action pugins - add check for network_cli connection type (https://github.com/ansible-collections/community.network/issues/119, https://github.com/ansible-collections/community.network/pull/120).
- dladm_vnic - fixed issue where setting vlan in Python 3 caused a type error (https://github.com/ansible-collections/community.network/issues/131).
- dladm_vnic - vlan IDs 0 and 4095 are now correctly identified as invalid (https://github.com/ansible-collections/community.network/pull/132).
- edgeos_config - Added `cat` command to allow display of large files without `less`. Led to a timeout error. (https://github.com/ansible-collections/community.network/issues/79)
- edgeos_config - fixed issue where config could be saved while in check mode (https://github.com/ansible-collections/community.network/pull/78)
- edgeos_facts - Added `cat` command to allow display of large files without `less`. Led to a timeout error. (https://github.com/ansible-collections/community.network/issues/79)
- ftd httpapi plugin - make sure that plugin errors out on initialization if the required library is not found, and not on load-time (https://github.com/ansible-collections/community.network/pull/150).

community.okd
~~~~~~~~~~~~~

- Generate downstream redhat.openshift documentation (https://github.com/ansible-collections/community.okd/pull/59).

community.postgresql
~~~~~~~~~~~~~~~~~~~~

- postgresql_ext - fix the module crashes when available ext versions cannot be compared with current version (https://github.com/ansible-collections/community.general/issues/1095).
- postgresql_ext - fix version selection when ``version=latest`` (https://github.com/ansible-collections/community.general/pull/1078).
- postgresql_info - fix crash caused by wrong PgSQL version parsing (https://github.com/ansible-collections/community.postgresql/issues/40).
- postgresql_ping - fix crash caused by wrong PgSQL version parsing (https://github.com/ansible-collections/community.postgresql/issues/40).
- postgresql_privs - fix module fails when ``type`` group and passing ``objs`` value containing hyphens (https://github.com/ansible-collections/community.general/issues/1058).
- postgresql_query - add a warning to set ``as_single_query`` option explicitly (https://github.com/ansible-collections/community.postgresql/pull/54).
- postgresql_query - fix datetime.timedelta type handling (https://github.com/ansible-collections/community.postgresql/issues/47).
- postgresql_query - fix decimal handling (https://github.com/ansible-collections/community.postgresql/issues/45).
- postgresql_set - fails in check_mode on non-numeric values containing `B` (https://github.com/ansible-collections/community.postgresql/issues/48).
- postgresql_set - return a message instead of traceback when a passed parameter has not been found (https://github.com/ansible-collections/community.postgresql/issues/41).

community.routeros
~~~~~~~~~~~~~~~~~~

- api - fix crash when the ``ssl`` parameter is used (https://github.com/ansible-collections/community.routeros/pull/3).
- api - remove ``id to .id`` as default requirement which conflicts with RouterOS ``id`` configuration parameter (https://github.com/ansible-collections/community.routeros/pull/15).
- routeros terminal plugin - allow slashes in hostnames for terminal detection. Without this, slashes in hostnames will result in connection timeouts (https://github.com/ansible-collections/community.network/pull/138).

community.sops
~~~~~~~~~~~~~~

- community.sops.sops lookup plugins - fix wrong format of Ansible variables so that these are actually used (https://github.com/ansible-collections/community.sops/pull/51).
- community.sops.sops vars plugins - remove non-working Ansible variables (https://github.com/ansible-collections/community.sops/pull/51).

community.vmware
~~~~~~~~~~~~~~~~

- Fix remove hosts from cluster to use cluster name variable
- Fix vSwitch0 default port group removal to run against all hosts
- Fixed the find_obj method in the ``module_utils/vmware.py`` to handle an object name using special characters that URL-decoded(https://github.com/ansible-collections/community.vmware/pull/460).
- For vSphere 7.0u1, add steps to tests to remove vCLS VMs before removing datastore
- ``module_utils/vmware.py`` handles an object name using special characters that URL-decoded(https://github.com/ansible-collections/vmware/pull/380).
- vmware_cluster - consider datacenter name while creating cluster (https://github.com/ansible-collections/community.vmware/issues/575).
- vmware_cluster_drs - consider datacenter name while managing cluster (https://github.com/ansible-collections/community.vmware/issues/575).
- vmware_cluster_ha - added APD and PDL configuration (https://github.com/ansible-collections/community.vmware/issues/451).
- vmware_cluster_ha - consider datacenter name while managing cluster (https://github.com/ansible-collections/community.vmware/issues/575).
- vmware_cluster_info - return tag related information (https://github.com/ansible-collections/community.vmware/issues/453).
- vmware_cluster_vsan - consider datacenter name while managing cluster (https://github.com/ansible-collections/community.vmware/issues/575).
- vmware_content_library_manager - added support for subscribed library (https://github.com/ansible-collections/community.vmware/pull/569).
- vmware_datastore_cluster_manager - Fix idempotency in check mode (https://github.com/ansible-collections/community.vmware/issues/623).
- vmware_deploy_ovf - fixed an UnboundLocalError for variable 'name' in check mode (https://github.com/ansible-collections/community.vmware/pull/499).
- vmware_deploy_ovf - fixed network mapping in multi-datacenter environments
- vmware_dvswitch - correctly add contact information (https://github.com/ansible-collections/community.vmware/issues/608).
- vmware_dvswitch - fix an issue with vSphere 7 when no switch_version is defined (https://github.com/ansible-collections/community.vmware/issues/576)
- vmware_dvswitch_lacp - typecast uplink number in lag_options (https://github.com/ansible-collections/community.vmware/issues/111).
- vmware_folder_info - added the flat_folder_info in the return value.
- vmware_guest - fix an issue with vSphere 7 when adding several virtual disks and / or vNICs (https://github.com/ansible-collections/community.vmware/issues/545)
- vmware_guest - handle NoneType values before passing to ``len`` API (https://github.com/ansible-collections/community.vmware/issues/593).
- vmware_guest - handle computer name in existing VM customization (https://github.com/ansible-collections/community.vmware/issues/570).
- vmware_guest_disk - fix an issue with vSphere 7 when adding several virtual disks and (https://github.com/ansible-collections/community.vmware/issues/373)
- vmware_guest_sendkey - add sleep_time parameter to add delay in-between keys sent (https://github.com/ansible-collections/community.vmware/issues/404).
- vmware_host_logbundle - handle fetch_url status before attempting to read response.
- vmware_host_ntp - fix an issue with disconnected hosts (https://github.com/ansible-collections/community.vmware/issues/539)
- vmware_object_role_permission - add support for role name presented in vSphere Web UI (https://github.com/ansible-collections/community.vmware/issues/436).
- vmware_resource_pool - added a changing feature of resource pool config (https://github.com/ansible-collections/community.vmware/pull/469).
- vmware_resource_pool - fixed that always updates occur bug on vCenter Server even when not changing resource pool config (https://github.com/ansible-collections/community.vmware/pull/482).
- vmware_tag_manager - added new parameter 'moid' to identify VMware object to tag (https://github.com/ansible-collections/community.vmware/issues/430).
- vmware_vm_info - added the moid information in the return value.
- vmware_vm_inventory - ensure self.port is integer (https://github.com/ansible-collections/community.vmware/issues/488).
- vmware_vm_inventory - improve plugin performance (https://github.com/ansible-collections/community.vmware/issues/434).
- vmware_vm_vm_drs_rule - report changes in check mode (https://github.com/ansible-collections/community.vmware/issues/440).
- vsphere_copy - handle unboundlocalerror when timeout occurs (https://github.com/ansible-collections/community.vmware/issues/554).

community.windows
~~~~~~~~~~~~~~~~~

- win_partition - fix size comparison errors when size specified in bytes (https://github.com/ansible-collections/community.windows/pull/159)
- win_security_policy - read config file with correct encoding to avoid breaking non-ASCII chars
- win_security_policy - strip of null char added by secedit for ``LegalNoticeText`` so the existing value is preserved

community.zabbix
~~~~~~~~~~~~~~~~

- When installing the Zabbix packages, we disable all other yum repositories except the one for the Zabbix.
- all roles - missing ``become`` set to ``true`` was added to each task that requires admin privleges.
- zabbix_agent - Agent 2 also be able to use userparameters file.
- zabbix_agent - Also work on SLES 12 sp5
- zabbix_agent - Documented the property 'zabbix_proxy_ip' in the documentation.
- zabbix_agent - There was an task that wasn't able to use an http(s)_proxy environment while installing an package.
- zabbix_agent - Windows - Able to create PSK file
- zabbix_agent - Windows - Fixing download links to proper version/url
- zabbix_agent - Windows - Removal of not working property
- zabbix_agent - Zabbix packages were not able to install properly on Fedora. When the packages are installed, the version will be appended to the package name. This is eofr all RedHat related OS'es.
- zabbix_agent - added new properties and updated documentation to allow for correct Zabbix Agent2 configuration.
- zabbix_agent - fixed bug where Nginx prevented Apache from working as it was part of the FPM configuration.
- zabbix_agent - fixed issue with zabbix_agent2_tlspsk_auto having no effect when using zabbix_agent2
- zabbix_agent - fixed issue with zabbix_api_create_hosts and TLS configuration when using zabbix_agent2, where zabbix_agent_tls* settings were used instead of zabbix_agent2_tls*
- zabbix_host - module will no longer require ``interfaces`` to be present when creating host  with Zabbix 5.2 (https://github.com/ansible-collections/community.zabbix/pull/291).
- zabbix_host - should no longer fail with 'host cannot have more than one default interface' error (https://github.com/ansible-collections/community.zabbix/pull/309).
- zabbix_proxy (role) - Added missing paragraph for the SQLite3 as database.
- zabbix_proxy (role) - The become option was missing in some essential tasks when installing the Zabbix Proxy with SQLite3 as database.
- zabbix_proxy (role) - Various documentation fixes removing the Zabbix Server and replaced it with actual Zabbix Proxy information.
- zabbix_proxy - Added new property 'zabbix_proxy_ip' to determine ip for host running the Zabbix Proxy.
- zabbix_proxy - The 'interface' option was missing when creating an Proxy via the API.
- zabbix_template - fixed documentation for ``macros`` argument (https://github.com/ansible-collections/community.zabbix/pull/296).
- zabbix_template - fixed encode error when using Python2 (https://github.com/ansible-collections/community.zabbix/pull/297).
- zabbix_template - fixed issue when importing templates to zabbix version. >= 5.2
- zabbix_template_info - fixed encode error when using Python2 (https://github.com/ansible-collections/community.zabbix/pull/297).
- zabbix_user - disable no_log warning for option override_password.
- zabbix_user - fixed issue where module couldn't create a user since Zabbix 5.2 (https://github.com/ansible-collections/community.zabbix/pull/260).
- zabbix_web - fixed issue Role cannot install Zabbix web 5.0 on RHEL 7 (https://github.com/ansible-collections/community.zabbix/issues/202).

containers.podman
~~~~~~~~~~~~~~~~~

- multiple modules - fix diff calculation for lower/upper cases
- podman_container - Add note about containerPort setting
- podman_container - Convert gidmap to list for podman_container
- podman_container - Convert log-opts to dictionary and idempotent
- podman_container - Fix force restart option for containers
- podman_container - Fix idempotency for volume GID and UID
- podman_container - Fix init option it's boolean not string
- podman_container - Fix no_hosts idempotency for newer version
- podman_container - Fix signals case for podman_container
- podman_container - Remove 'detach' when creating container
- podman_container - Remove pyyaml from requirements
- podman_image - Fix doc defaults for podman_image
- podman_logout - Handle podman logout not logging out when logged in via different tool
- podman_network - Check if dnsname plugin installed for CNI
- podman_network - Correct IP range example for podman_network
- podman_volume - Fix return data from podman_volume module
- podman_volume - Set options for a volume as list and fix idempotency

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- Documentation improvement request `#140 <https://github.com/dell/dellemc-openmanage-ansible-modules/issues/140>`_
- Executing dellemc_configure_idrac_users twice fails the second attempt `#100 <https://github.com/dell/dellemc-openmanage-ansible-modules/issues/100>`_
- GitHub issue fix - Module dellemc_idrac_storage_volume.py broken. (https://github.com/dell/dellemc-openmanage-ansible-modules/issues/212)
- GitHub issue fix - ome_smart_fabric Fabric management is not supported on the specified system. (https://github.com/dell/dellemc-openmanage-ansible-modules/issues/179)
- Identity pool does not reset when a network VLAN is added to a template in the ome_template_network_vlan module. `#169 <https://github.com/dell/dellemc-openmanage-ansible-modules/issues /169>`_
- Known issue fix #187956: If an invalid job_id is provided, the idrac_lifecycle_controller_job_status_info module returns an error message with the description of the issue.
- Known issue fix #188267: No error message is displayed when the target iDRAC with firmware version less than 3.30.30.30 is updated.
- Missing parameter added in ome_smart_fabric_uplink module documenation. `#181 <https://github.com/dell/dellemc-openmanage-ansible-modules/issues/181>`_
- Sanity fixes as per ansible guidelines to all modules.
- dellemc_change_power_state fails if host is already on `#132 <https://github.com/dell/dellemc-openmanage-ansible-modules/issues/132>`_
- dellemc_change_power_state not idempotent `#115 <https://github.com/dell/dellemc-openmanage-ansible-modules/issues/115>`_
- dellemc_configure_idrac_users error `#26 <https://github.com/dell/dellemc-openmanage-ansible-modules/issues/26>`_
- dellemc_configure_idrac_users is unreliable - errors `#113 <https://github.com/dell/dellemc-openmanage-ansible-modules/issues/113>`_
- idrac_server_config_profile improvement requested (request) `#137 <https://github.com/dell/dellemc-openmanage-ansible-modules/issues/137>`_
- ome_firmware_catalog.yml example errors `#145 <https://github.com/dell/dellemc-openmanage-ansible-modules/issues/145>`_

dellemc.os10
~~~~~~~~~~~~

- Fix issue in using ip_and_mask along with members in os10_vlan role (https://github.com/ansible-collections/dellemc.os10/issues/42)
- Fix issue in using list of strings for `commands` argument for `os10_command` module (https://github.com/ansible-collections/dellemc.os10/issues/43)
- Fixed issue in using interface range in os10_vlan members. (https://github.com/ansible-collections/dellemc.os10/issues/53)
- Fixed os10_vlan role idempotency issue with description and members (https://github.com/ansible-collections/dellemc.os10/issues/46)

dellemc.os6
~~~~~~~~~~~

- Fix issue in using "os6_facts" module for non-legacy n-series platofrms
- Fix issue in using list of strings for `commands` argument for `os6_command` module
- command module change to keep similar changes across all dell networking OSs
- config module fix to handle issues faced while parsing running config and fixing idempotency issue for banner config
- config module fix to handle multiline banner
- module utils fix for exit handling in multilevel parent commands
- terminal plugin fix to handle error reported by management access lists
- terminal plugin fix to send "terminal length 0" command

f5networks.f5_modules
~~~~~~~~~~~~~~~~~~~~~

- Changed unicast_failover element type to dictionary
- Fix AFM firewall address list error
- Fix GTM virtual server depenedncy where path to Iapp resources were incorrectly stripped.
- Fix apm policy existence checks in bigip_apm_policy_fetch module
- Fix asm policy existence checks in bigip_asm_policy_fetch module
- Fix bigip_management_route module not idempotent
- Fix force parameter set to yes causing list index out of range error
- Fix host_begins_with_any, host_is_any, server_name_is_any and host_is_not_any parameters of the bigip_policy_rule module to enforce list as the required parameter type. Change was required since in Ansible a string conversion is applied when the provided argument type is not matching the expected one causing undesired side effects.
- Fix idempotency issue with gateway_address and route domain in bigip_static_route module
- Fix invalid parameter name in the bigip_config_sync action module
- Fix issue where ASM file download needs to be chunked for larger files.
- Fix issue with bigip_asm_policy_fetch where existing file would break the module run
- Fix issue with bigip_asm_policy_fetch where similiar policy names would cause wrong policy to be fetched
- Fix issue with bigip_asm_policy_manage where similiar policy names would cause wrong policy id to be selected
- Fix issue with retaining package files in the bigip_lx_package module
- Fix iteration bug in bigiq_device_info module
- Fix key error in list comprehension in the AsmPolicyStatsParameters class
- Fix missing ssh-keyfile parameter causing key error in the bigip action plugin

hetzner.hcloud
~~~~~~~~~~~~~~

- Inventory Restore Python 2.7 compatibility
- hcloud_floating_ip Fix idempotency when floating ip is assigned to server

inspur.sm
~~~~~~~~~

- Update 'supports_check_mode=False' to 'supports_check_mode=True' for all modules ending in '_info'.
- Update version_added field in ad_group, ldap_group, user, and user_group modules to match the collection version they were first introduced in.

junipernetworks.junos
~~~~~~~~~~~~~~~~~~~~~

- Add version key to galaxy.yaml to work around ansible-galaxy bug
- Updating unit tests for resource modules (https://github.com/ansible-collections/junipernetworks.junos/pull/127)
- allowing partial config filter for junos commands (https://github.com/ansible-collections/junipernetworks.junos/issues/112)
- changing prefix list type to list and correcting facts gathering (https://github.com/ansible-collections/junipernetworks.junos/issues/131)
- checking for units and family attributes in conf dictionary (https://github.com/ansible-collections/junipernetworks.junos/issues/121)
- constructing the facts based on the addresses per unit (https://github.com/ansible-collections/junipernetworks.junos/issues/111)
- release version added updated to 1.3.0 for junos_ospf_interfaces and junos_bgp_global module

kubernetes.core
~~~~~~~~~~~~~~~

- Fix suboption docs structure for inventory plugins (https://github.com/ansible-collections/kubernetes.core/pull/103).
- Handle invalid kubeconfig parsing error (https://github.com/ansible-collections/kubernetes.core/pull/119).
- Make sure Service changes run correctly in check_mode (https://github.com/ansible-collections/kubernetes.core/pull/84).
- Make sure extra files are not included in built collection (https://github.com/ansible-collections/kubernetes.core/pull/85).
- Test against stable ansible branch so molecule tests work (https://github.com/ansible-collections/kubernetes.core/pull/168).
- Update GitHub Actions workflow for better CI stability (https://github.com/ansible-collections/kubernetes.core/pull/78).
- Update openshift requirements in k8s module doc (https://github.com/ansible-collections/kubernetes.core/pull/153).
- common - handle exception raised due to DynamicClient (https://github.com/ansible-collections/kubernetes.core/pull/224).
- helm - add replace parameter (https://github.com/ansible-collections/kubernetes.core/issues/106).
- k8s (inventory) - Set the connection plugin and transport separately (https://github.com/ansible-collections/kubernetes.core/pull/208).
- k8s (inventory) - Specify FQCN for k8s inventory plugin to fix use with Ansible 2.9 (https://github.com/ansible-collections/kubernetes.core/pull/250).
- k8s - Add exception handling when retrieving k8s client (https://github.com/ansible-collections/kubernetes.core/pull/54).
- k8s - Fix argspec for 'elements' (https://github.com/ansible-collections/kubernetes.core/issues/13).
- k8s - Fix sanity test 'compile' failing because of positional args (https://github.com/ansible-collections/kubernetes.core/issues/260).
- k8s - Use ``from_yaml`` filter with lookup examples in ``k8s`` module documentation examples (https://github.com/ansible-collections/kubernetes.core/pull/56).
- k8s_info - add wait functionality (https://github.com/ansible-collections/kubernetes.core/issues/18).
- k8s_info - remove unneccessary k8s_facts deprecation notice (https://github.com/ansible-collections/kubernetes.core/pull/97).
- k8s_log - Module no longer attempts to parse log as JSON (https://github.com/ansible-collections/kubernetes.core/pull/69).
- k8s_scale - Fix scale wait and add tests (https://github.com/ansible-collections/kubernetes.core/pull/100).
- k8s_service - Fix argspec (https://github.com/ansible-collections/kubernetes.core/issues/33).
- kubectl - Fix documentation in kubectl connection plugin (https://github.com/ansible-collections/kubernetes.core/pull/52).
- raw - handle condition when definition is none (https://github.com/ansible-collections/kubernetes.core/pull/139).

netapp.elementsw
~~~~~~~~~~~~~~~~

- na_elementsw_node - fix check_mode so that no action is taken.
- na_elementsw_node - improve error reporting when cluster name cannot be set because node is already active.
- na_elementsw_schedule - missing imports TimeIntervalFrequency, Schedule, ScheduleInfo have been added back

netapp.ontap
~~~~~~~~~~~~

- All REST modules, will not fail if a job fails
- na_ontap_* - change version_added from '2.6' to '2.6.0' where applicable to satisfy sanity checker.
- na_ontap_aggregate - support concurrent actions for rename/modify/add_object_store and create/add_object_store.
- na_ontap_broadcast_domain_ports - handle ``changed`` for check_mode and report correctly.
- na_ontap_cifs - fix for AttributeError - 'NoneType' object has no attribute 'get' on line 300
- na_ontap_cifs - fix idempotency issue when ``show-previous-versions`` is used.
- na_ontap_cluster - ``check_mode`` is now working properly.
- na_ontap_cluster - ``single_node_cluster`` option was ignored.
- na_ontap_firmware_upgrade - fix ValueError issue when processing URL error.
- na_ontap_info - KeyError on ``tree`` for quota_report_info.
- na_ontap_info - Use ``node-id`` as key rather than ``current-version``.
- na_ontap_info - better reporting on KeyError traceback, option to ignore error.
- na_ontap_interface - ``home_node`` is not required in pre-cluster mode.
- na_ontap_interface - ``role`` is not required if ``service_policy`` is present and ONTAP version is 9.8.
- na_ontap_interface - traceback in get_interface if node is not reachable.
- na_ontap_ipspace - invalid call in error reporting (double error).
- na_ontap_job_schedule - allow ``job_minutes`` to set number to -1 for job creation with REST too.
- na_ontap_lun - REST expects 'all' for tiering policy and not 'backup'.
- na_ontap_qtree - fixed ``None is not subscriptable`` exception on rename operation.
- na_ontap_quotas - Handle blank string idempotency issue for ``quota_target`` in quotas module.
- na_ontap_rest_info - ``changed`` was set to "False" rather than boolean False.
- na_ontap_snapmirror - fix job update failures for load_sharing mirrors.
- na_ontap_snapmirror - report error when attempting to change relationship_type.
- na_ontap_snapmirror - wait up to 5 minutes for abort to complete before issuing a delete.
- na_ontap_snapmirror_policy - report error when attempting to change ``policy_type`` rather than taking no action.
- na_ontap_snmp - SNMP module wrong ``access_control`` issue and error handling fix.
- na_ontap_software_update - module is not idempotent.
- na_ontap_svm - warning for ``aggr_list`` wildcard value(``*``) in create idempotency.
- na_ontap_user - application expects only ``service_processor`` but module supports ``service-processor``.
- na_ontap_volume - REST expects 'all' for tiering policy and not 'backup'.
- na_ontap_volume - ``encrypt`` with a value of ``false`` is ignored when creating a volume.
- na_ontap_volume - checking for success before failure lead to 'NoneType' object has no attribute 'get_child_by_name' when modifying a Flexcache volume.
- na_ontap_volume - detect and report error when attempting to change FlexVol into FlexGroup.
- na_ontap_volume - fix volume type modify issue by reporting error.
- na_ontap_volume - fixed ``KeyError`` exception on ``size`` when reporting creation error.
- na_ontap_volume - report error if ``aggregate_name`` option is used with a FlexGroup.
- netapp.py - uncaught exception (traceback) on zapi.NaApiError.

netapp_eseries.santricity
~~~~~~~~~~~~~~~~~~~~~~~~~

- Fix check_port_type method for ib iser when ib is the port type.
- Fix examples in the netapp_e_mgmt_interface module.
- Fix issue with changing host port name.
- Fix na_santricity_lun_mapping unmapping issue; previously mapped volumes failed to be unmapped.

netbox.netbox
~~~~~~~~~~~~~

- Allow IDs to be passed into objects that accept a list (https://github.com/netbox-community/ansible_modules/issues/407)
- Prevent inventory plugin from failing on 403 and print warning message (https://github.com/netbox-community/ansible_modules/pull/354)
- Update ``netbox_ip_address`` module to accept ``assigned_object`` to work with NetBox 2.9 (https://github.com/netbox-community/ansible_modules/pull/345)
- Update inventory plugin to properly associate IP address to interfaces with NetBox 2.9 (https://github.com/netbox-community/ansible_modules/pull/334)
- Update inventory plugin to work with tags with NetBox 2.9 (https://github.com/netbox-community/ansible_modules/pull/340)
- Update modules to be able to properly update tags to work with NetBox 2.9 (https://github.com/netbox-community/ansible_modules/pull/345)
- Version checks were failing due to converting "2.10" to a float made it an integer of 2.1 which broke version related logic. (#396)
- netbox_device_interface - Fixed copy pasta in documentation. (#371)
- netbox_ip_address - Updated documentation to show that ``family`` option has been deprecated. (#388)
- netbox_site - Changed latitude/longitude type from float to str [#418](https://github.com/netbox-community/ansible_modules/pull/418)
- netbox_utils - Fixed typo for ``circuits.circuittermination`` searches. (#367)
- netbox_utils - If query_dict is None, fail and provide meaningful error [#419](https://github.com/netbox-community/ansible_modules/pull/419)
- netbox_utils - Remove manual manipulation for building query params for netbox_ip_address and assigned object [#421](https://github.com/netbox-community/ansible_modules/pull/421)
- netbox_utils - Skip all modifications to ``query_params`` when ``user_query_params`` is defined. (#389)
- netbox_vlan - Fixed uniqueness for vlan searches to add ``group``. (#386)

openvswitch.openvswitch
~~~~~~~~~~~~~~~~~~~~~~~

- Add version key to galaxy.yaml to work around ansible-galaxy bug (https://github.com/ansible-collections/openvswitch.openvswitch/issues/59)

ovirt.ovirt
~~~~~~~~~~~

- 01_create_target_hosted_engine_vm - Force basic authentication (https://github.com/oVirt/ovirt-ansible-collection/pull/131).
- disaster_recovery - Fix multiple configuration issues like paths, "~" support, user input messages, etc. (https://github.com/oVirt/ovirt-ansible-collection/pull/160).
- hosted_engine_setup - Allow uppercase characters in mac address (https://github.com/oVirt/ovirt-ansible-collection/pull/150).
- hosted_engine_setup - Clean VNC encryption config (https://github.com/oVirt/ovirt-ansible-collection/pull/175/).
- hosted_engine_setup - set custom bios type of hosted-engine VM to Q35+SeaBIOS (https://github.com/oVirt/ovirt-ansible-collection/pull/129).
- hosted_engine_setup - use zcat instead of gzip (https://github.com/oVirt/ovirt-ansible-collection/pull/130).
- inventory plugin - Fix timestamp for Python 2 (https://github.com/oVirt/ovirt-ansible-collection/pull/173).
- ovirt inventory - Add close of connection at the end (https://github.com/oVirt/ovirt-ansible-collection/pull/122).
- ovirt_disk - dont move disk when already in storage_domain (https://github.com/oVirt/ovirt-ansible-collection/pull/135)
- ovirt_disk - fix upload when direct upload fails (https://github.com/oVirt/ovirt-ansible-collection/pull/120).
- ovirt_vm - Fix template search (https://github.com/oVirt/ovirt-ansible-collection/pull/132).
- ovirt_vm - Rename q35_sea to q35_sea_bios (https://github.com/oVirt/ovirt-ansible-collection/pull/111).

purestorage.flasharray
~~~~~~~~~~~~~~~~~~~~~~

- purefa.py - Resolve issue when pypureclient doesn't handshake array correctly
- purefa_dns - Fix idempotency
- purefa_host - Correctly remove host that is in a hostgroup
- purefa_volume - Alert when volume selected for move does not exist
- purefa_volume - Fix failing idempotency on eradicate volume

purestorage.flashblade
~~~~~~~~~~~~~~~~~~~~~~

- purefa_policy - Resolve multiple issues related to incorrect use of timezones
- purefb_connect - Ensure changing encryption status on array connection is performed correctly
- purefb_connect - Fix breaking change created in purity_fb SDK 1.9.2 for deletion of array connections
- purefb_connect - Hide target array API token
- purefb_ds - Ensure updating directory service configurations completes correctly
- purefb_info - Fix issue getting array info when encrypted connection exists

sensu.sensu_go
~~~~~~~~~~~~~~

- Accept *str* and *unicode* instance as a valid string in *bonsai_asset* action plugin.
- Add Sensu Go 5.17.x and 5.18.x to the test suite and remove the unsupported versions (5.14.2 and lower).
- Do not die when encountering a deprecated asset format.
- Ensure backend initialization properly reports changed state.
- Expand documentation about the *check_hooks* parameter in the check module.
- Explain how the resource name parameter is used and what invariants need to hold in order for the Sensu Go to consider it a valid name.
- Fix resource metadata comparison on Sensu Go 5.19.0 and newer.
- Make API key authentication work even for regular users with limited permissions.
- Make it possible to use modules on Sensu Go backends with no version number.
- Make subscriptions comparison insensitive to ordering.
- Make sure agent entities handle *entity:{name}* automatic subscriptions.
- Make sure check module is as idempotent as possible.
- Make sure event module always returns a predicted result.
- Make user module compatible with Sensu Go >= 5.21.0.
- Make user module fully-idempotent. Previous versions did not properly detect the password changes.
- Mimic actual responses when user module runs in check mode.
- Reintroduce namespace support to *bonsai_asset* module (thanks, @jakeo)
- Remove unsupported Ubuntu versions from the test suite.
- Update entity comparator to handle new fields.
- Update return value documentation for info modules.
- Update the datastore module to cope with the minor API changes.
- Update the role metadata with proper platform markers.
- Use fully-qualified collection names in module documentation.

servicenow.servicenow
~~~~~~~~~~~~~~~~~~~~~

- fix inventory plugin transforming hostnames unnecessarily
- fix malformed documentation on docs.ansible.com

theforeman.foreman
~~~~~~~~~~~~~~~~~~

- Don't try to update an entity, if only parameters that aren't supported by the server are detected as changed. (https://github.com/theforeman/foreman-ansible-modules/issues/975)
- allow to pass an empty string when refering to entities, thus unsetting the value (https://github.com/theforeman/foreman-ansible-modules/issues/969)
- compute_profile - don't fail when trying to update compute attributes of a profile (https://github.com/theforeman/foreman-ansible-modules/issues/997)
- content_upload - Fix upload of files bigger than 2MB in Pulp3-based setups (https://github.com/theforeman/foreman-ansible-modules/issues/1043)
- content_view - remove CVs from lifecycle environments before deleting them (https://bugzilla.redhat.com/show_bug.cgi?id=1875314)
- content_view_version - make the ``version`` parameter not fail when the version was entered without a minor part (https://github.com/theforeman/foreman-ansible-modules/issues/1087)
- external_usergroup - support non-LDAP external groups (https://github.com/theforeman/foreman-ansible-modules/issues/956)
- host - fix subnet/domain assignment when multiple interfaces are defined (https://github.com/theforeman/foreman-ansible-modules/issues/1095)
- host - properly scope image lookups by the compute resource (https://bugzilla.redhat.com/show_bug.cgi?id=1878693)
- host, hostgroup - support ``None`` as the ``pxe_loader`` (https://github.com/theforeman/foreman-ansible-modules/issues/971)
- image - fix quoting of search values (https://github.com/theforeman/foreman-ansible-modules/issues/927)
- inventory plugin - include empty parent groups in the inventory (https://github.com/theforeman/foreman-ansible-modules/issues/919)
- job_invocation - properly submit ``ssh``, ``recurrence``, ``scheduling`` and ``concurrency_control`` to the server
- job_template - don't fail when trying to update template_inputs
- os_default_template - document possible template kind choices (https://bugzilla.redhat.com/show_bug.cgi?id=1889952)
- repository - don't emit a false warning about ``organization_id`` not being supported by the server (https://github.com/theforeman/foreman-ansible-modules/issues/1055)
- repository_set, repository - clarify documentation which module should be used for Red Hat Repositories (https://github.com/theforeman/foreman-ansible-modules/issues/1059)
- smart_class_parameters - don't fail when trying to update override_values

vyos.vyos
~~~~~~~~~

- Add version key to galaxy.yaml to work around ansible-galaxy bug
- Added openvpn vtu interface support.
- Enable configuring an interface which is not present in the running config.
- Update network integration auth timeout for connection local.
- terminal plugin - Overhaul ansi_re to remove more escape sequences
- vyos_config - Only process src files as commands when they actually contain commands. This fixes an issue were the whitespace preceding a configuration key named 'set' was stripped, tripping up the parser.

Known Issues
------------

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- Issue 1(186024): ome_smart_fabric_uplink module does not allow the creation of multiple uplinks of the same name even though this is supported by OpenManage Enterprise Modular. If an uplink is created using the same name as an existing uplink, the existing uplink is modified.
- Issue 2(187956): If an invalid job_id is provided, idrac_lifecycle_controller_job_status_info returns an error message. This error message does not contain information about the exact issue with the invalid job_id.
- Issue 3(188267): While updating the iDRAC firmware, the idrac_firmware module completes execution before the firmware update job is completed. An incorrect message is displayed in the task output as 'DRAC WSMAN endpoint returned HTTP code '400' Reason 'Bad Request''. This issue may occur if the target iDRAC firmware version is less than 3.30.30.30

New Plugins
-----------

Connection
~~~~~~~~~~

- community.docker.docker_api - Run tasks in docker containers

Inventory
~~~~~~~~~

- community.docker.docker_containers - Ansible dynamic inventory plugin for Docker containers.
- community.general.proxmox - Proxmox inventory source
- community.general.stackpath_compute - StackPath Edge Computing inventory source
- community.hrobot.robot - Hetzner Robot inventory source

Lookup
~~~~~~

- ansible.utils.get_path - Retrieve the value in a variable using a path
- ansible.utils.index_of - Find the indices of items in a list matching some criteria
- ansible.utils.to_paths - Flatten a complex object into a dictionary of paths and values
- ansible.utils.validate - Validate data with provided criteria
- community.sops.sops - Read sops encrypted file contents

Vars
~~~~

- community.sops.sops - Loading sops-encrypted vars files

New Modules
-----------

ansible.utils
~~~~~~~~~~~~~

- ansible.utils.cli_parse - Parse cli output or text using a variety of parsers
- ansible.utils.fact_diff - Find the difference between currently set facts
- ansible.utils.update_fact - Update currently set facts
- ansible.utils.validate - Validate data with provided criteria

arista.eos
~~~~~~~~~~

- arista.eos.eos_bgp_address_family - bgp_address_family resource module
- arista.eos.eos_bgp_global - bgp_global resource module
- arista.eos.eos_ospf_interfaces - ospf_interfaces resource module
- arista.eos.eos_ospfv3 - OSPFv3 resource module

cisco.ios
~~~~~~~~~

- cisco.ios.ios_bgp_global - BGP Global resource module
- cisco.ios.ios_ospf_interfaces - OSPF Interfaces resource module
- cisco.ios.ios_ospfv3 - OSPFv3 resource module

cisco.iosxr
~~~~~~~~~~~

- cisco.iosxr.iosxr_ospf_interfaces - OSPF Interfaces Resource Module.
- cisco.iosxr.iosxr_ospfv3 - ospfv3 resource module

cisco.meraki
~~~~~~~~~~~~

- cisco.meraki.meraki_alert - Manage alerts in the Meraki cloud
- cisco.meraki.meraki_mx_l2_interface - Configure MX layer 2 interfaces

cisco.nxos
~~~~~~~~~~

- cisco.nxos.nxos_bgp_global - BGP Global resource module.
- cisco.nxos.nxos_ospf_interfaces - OSPF Interfaces Resource Module.
- cisco.nxos.nxos_ospfv3 - OSPFv3 resource module

cloudscale_ch.cloud
~~~~~~~~~~~~~~~~~~~

- cloudscale_ch.cloud.network - Manages networks on the cloudscale.ch IaaS service
- cloudscale_ch.cloud.subnet - Manages subnets on the cloudscale.ch IaaS service

community.aws
~~~~~~~~~~~~~

- community.aws.s3_metrics_configuration - Manage s3 bucket metrics configuration in AWS

community.crypto
~~~~~~~~~~~~~~~~

- community.crypto.openssl_csr_pipe - Generate OpenSSL Certificate Signing Request (CSR)
- community.crypto.openssl_privatekey_pipe - Generate OpenSSL private keys without disk access
- community.crypto.x509_certificate_pipe - Generate and/or check OpenSSL certificates

community.docker
~~~~~~~~~~~~~~~~

- community.docker.current_container_facts - Return facts about whether the module runs in a Docker container

community.general
~~~~~~~~~~~~~~~~~

Cloud
^^^^^

Misc
....

- community.general.proxmox_domain_info - Retrieve information about one or more Proxmox VE domains
- community.general.proxmox_group_info - Retrieve information about one or more Proxmox VE groups
- community.general.proxmox_snap - Snapshot management of instances in Proxmox VE cluster
- community.general.proxmox_user_info - Retrieve information about one or more Proxmox VE users

Scaleway
........

- community.general.scaleway_database_backup - Scaleway database backups management module

Clustering
^^^^^^^^^^

Nomad
.....

- community.general.nomad_job - Launch a Nomad Job
- community.general.nomad_job_info - Get Nomad Jobs info

Identity
^^^^^^^^

Ipa
...

- community.general.ipa_pwpolicy - Manage FreeIPA password policies

Monitoring
^^^^^^^^^^

- community.general.pagerduty_change - Track a code or infrastructure change as a PagerDuty change event
- community.general.pagerduty_user - Manage a user account on PagerDuty

Datadog
.......

- community.general.datadog_downtime - Manages Datadog downtimes

Packaging
^^^^^^^^^

Os
..

- community.general.copr - Manage one of the Copr repositories
- community.general.rpm_ostree_pkg - Install or uninstall overlay additional packages
- community.general.yum_versionlock - Locks / unlocks a installed package(s) from being updated by yum package manager

Source Control
^^^^^^^^^^^^^^

Gitlab
......

- community.general.gitlab_group_members - Manage group members on GitLab Server
- community.general.gitlab_group_variable - Creates, updates, or deletes GitLab groups variables

System
^^^^^^

- community.general.iptables_state - Save iptables state into a file or restore it from a file
- community.general.shutdown - Shut down a machine
- community.general.ssh_config - Manage SSH config for user
- community.general.sysrc - Manage FreeBSD using sysrc
- community.general.sysupgrade - Manage OpenBSD system upgrades

community.grafana
~~~~~~~~~~~~~~~~~

- community.grafana.grafana_notification_channel - Manage Grafana Notification Channels

community.mongodb
~~~~~~~~~~~~~~~~~

- community.mongodb.mongodb_shell - Run commands via the MongoDB shell.

community.okd
~~~~~~~~~~~~~

- community.okd.openshift_auth - Authenticate to OpenShift clusters which require an explicit login step
- community.okd.openshift_process - Process an OpenShift template.openshift.io/v1 Template
- community.okd.openshift_route - Expose a Service as an OpenShift Route.

community.sops
~~~~~~~~~~~~~~

- community.sops.load_vars - Load sops-encrypted variables from files, dynamically within a task
- community.sops.sops_encrypt - Encrypt data with sops

community.vmware
~~~~~~~~~~~~~~~~

- community.vmware.vcenter_domain_user_group_info - Gather user or group information of a domain
- community.vmware.vmware_drs_group_manager - Manage VMs and Hosts in DRS group.
- community.vmware.vmware_first_class_disk - Manage VMware vSphere First Class Disks

community.windows
~~~~~~~~~~~~~~~~~

- community.windows.win_net_adapter_feature - Enable or disable certain network adapters.

containers.podman
~~~~~~~~~~~~~~~~~

- containers.podman.podman_containers - Manage multiple Podman containers at once
- containers.podman.podman_login_info - Get info about Podman logged in registries
- containers.podman.podman_logout - Log out with Podman from registries
- containers.podman.podman_network - Manage Podman networks

dellemc.openmanage
~~~~~~~~~~~~~~~~~~

- dellemc.openmanage.idrac_bios - Configure the BIOS attributes.
- dellemc.openmanage.idrac_lifecycle_controller_job_status_info - Get the status of a Lifecycle Controller job.
- dellemc.openmanage.idrac_lifecycle_controller_jobs - Delete the Lifecycle Controller Jobs.
- dellemc.openmanage.idrac_lifecycle_controller_logs - Export Lifecycle Controller logs to a network share.
- dellemc.openmanage.idrac_lifecycle_controller_status_info - Get the status of the Lifecycle Controller.
- dellemc.openmanage.idrac_network - Configures the iDRAC network attributes.
- dellemc.openmanage.idrac_reset - Reset iDRAC.
- dellemc.openmanage.idrac_syslog - Enable or disable the syslog on iDRAC.
- dellemc.openmanage.idrac_timezone_ntp - Configures time zone and NTP on iDRAC.
- dellemc.openmanage.idrac_user - Configure settings for user accounts.
- dellemc.openmanage.ome_network_port_breakout - This module allows to automate the port partitioning or breaking out to logical sub ports.
- dellemc.openmanage.ome_network_vlan - Create, modify & delete a VLAN.
- dellemc.openmanage.ome_network_vlan_info - Retrieves the information about networks VLAN(s) present in OpenManage Enterprise.
- dellemc.openmanage.ome_smart_fabric - Create, modify or delete a fabric on OpenManage Enterprise Modular.
- dellemc.openmanage.ome_smart_fabric_uplink - Create, modify or delete a uplink for a fabric on OpenManage Enterprise Modular.
- dellemc.openmanage.redfish_powerstate - Manage device power state.

f5networks.f5_modules
~~~~~~~~~~~~~~~~~~~~~

- f5networks.f5_modules.bigip_ssl_key_cert - Import/Delete SSL keys and certs from BIG-IP

hetzner.hcloud
~~~~~~~~~~~~~~

- hetzner.hcloud.hcloud_load_balancer_info - Gather infos about your Hetzner Cloud load_balancers.

junipernetworks.junos
~~~~~~~~~~~~~~~~~~~~~

- junipernetworks.junos.junos_bgp_global - Manages BGP Global configuration on devices running Juniper JUNOS.
- junipernetworks.junos.junos_ospf_interfaces - OSPF Interfaces Resource Module.
- junipernetworks.junos.junos_ospfv3 - OSPFv3 resource module

kubernetes.core
~~~~~~~~~~~~~~~

- kubernetes.core.helm - Manages Kubernetes packages with the Helm package manager
- kubernetes.core.helm_info - Get information from Helm package deployed inside the cluster
- kubernetes.core.helm_plugin - Manage Helm plugins
- kubernetes.core.helm_plugin_info - Gather information about Helm plugins
- kubernetes.core.helm_repository - Add and remove Helm repository
- kubernetes.core.k8s_exec - Execute command in Pod
- kubernetes.core.k8s_log - Fetch logs from Kubernetes resources

netapp.elementsw
~~~~~~~~~~~~~~~~

- netapp.elementsw.na_elementsw_info - NetApp Element Software Info
- netapp.elementsw.na_elementsw_qos_policy - NetApp Element Software create/modify/rename/delete QOS Policy

netapp.ontap
~~~~~~~~~~~~

- netapp.ontap.na_ontap_active_directory - NetApp ONTAP configure active directory
- netapp.ontap.na_ontap_debug - NetApp ONTAP Debug netapp-lib import and connection.
- netapp.ontap.na_ontap_mcc_mediator - NetApp ONTAP Add and Remove MetroCluster Mediator
- netapp.ontap.na_ontap_metrocluster - NetApp ONTAP set up a MetroCluster
- netapp.ontap.na_ontap_metrocluster_dr_group - NetApp ONTAP manage MetroCluster DR Group

netbox.netbox
~~~~~~~~~~~~~

- netbox.netbox.netbox_route_target - Creates or removes route targets from Netbox
- netbox.netbox.netbox_tag - Creates or removes tags from Netbox

openstack.cloud
~~~~~~~~~~~~~~~

- openstack.cloud.volume_backup module - Add/Delete Openstack volumes backup.
- openstack.cloud.volume_backup_info module - Retrieve information about Openstack volume backups.
- openstack.cloud.volume_snapshot_info module - Retrieve information about Openstack volume snapshots.

purestorage.flasharray
~~~~~~~~~~~~~~~~~~~~~~

- purestorage.flasharray.purefa_apiclient - Manage FlashArray API Clients
- purestorage.flasharray.purefa_directory - Manage FlashArray File System Directories
- purestorage.flasharray.purefa_export - Manage FlashArray File System Exports
- purestorage.flasharray.purefa_fs - Manage FlashArray File Systems
- purestorage.flasharray.purefa_policy - Manage FlashArray File System Policies

purestorage.flashblade
~~~~~~~~~~~~~~~~~~~~~~

- purestorage.flashblade.purefb_banner - Configure Pure Storage FlashBlade GUI and SSH MOTD message
- purestorage.flashblade.purefb_certgrp - Manage FlashBlade Certifcate Groups
- purestorage.flashblade.purefb_certs - Manage FlashBlade SSL Certifcates
- purestorage.flashblade.purefb_lifecycle - Manage FlashBlade object lifecycles
- purestorage.flashblade.purefb_syslog - Configure Pure Storage FlashBlade syslog settings

sensu.sensu_go
~~~~~~~~~~~~~~

- sensu.sensu_go.datastore - Manage Sensu external datastore providers
- sensu.sensu_go.datastore_info - List external Sensu datastore providers
- sensu.sensu_go.secret - Manage Sensu Go secrets
- sensu.sensu_go.secret_info - List available Sensu Go secrets
- sensu.sensu_go.secrets_provider_env - Manage Sensu Env secrets provider
- sensu.sensu_go.secrets_provider_info - List Sensu secrets providers
- sensu.sensu_go.secrets_provider_vault - Manage Sensu VaultProvider secrets provider

theforeman.foreman
~~~~~~~~~~~~~~~~~~

- theforeman.foreman.job_invocation - Invoke Remote Execution Jobs
- theforeman.foreman.smart_proxy - Manage Smart Proxies
- theforeman.foreman.status_info - Get status info

vyos.vyos
~~~~~~~~~

- vyos.vyos.vyos_ospf_interfaces - OSPF Interfaces resource module

Unchanged Collections
---------------------

- ansible.posix (still version 1.1.1)
- chocolatey.chocolatey (still version 1.0.2)
- community.azure (still version 1.0.0)
- community.digitalocean (still version 1.0.0)
- community.libvirt (still version 1.0.0)
- community.proxysql (still version 1.0.0)
- community.rabbitmq (still version 1.0.1)
- community.skydive (still version 1.0.0)
- cyberark.pas (still version 1.0.5)
- frr.frr (still version 1.0.3)
- gluster.gluster (still version 1.0.1)
- ibm.qradar (still version 1.0.3)
- mellanox.onyx (still version 1.0.0)
- ngine_io.exoscale (still version 1.0.0)
- splunk.es (still version 1.0.2)
- wti.remote (still version 1.0.1)
