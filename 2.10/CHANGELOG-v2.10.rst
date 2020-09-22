==========================
Ansible 2.10 Release Notes
==========================

This changelog describes changes since Ansible 2.9.0.

.. contents::
  :local:
  :depth: 2

v2.10.0
=======

.. contents::
  :local:
  :depth: 2

Release Summary
---------------

Release Date: 2020-09-15

`Porting Guide <https://docs.ansible.com/ansible/devel/porting_guides.html>`_

Ansible-base
------------

Ansible 2.10.0 contains Ansible-base version 2.10.1.
The changes are reported in the combined changelog below.

Included Collections
--------------------

- amazon.aws with version 1.2.0.
  The changes are reported in the combined changelog below.
- ansible.netcommon with version 1.2.1.
  The changes are reported in the combined changelog below.
- ansible.posix with version 1.1.1.
  The changes are reported in the combined changelog below.
- ansible.windows with version 1.0.0.
  The changes are reported in the combined changelog below.
- arista.eos with version 1.0.3.
  The changes are reported in the combined changelog below.
- awx.awx with version 14.1.0.
  Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.
- azure.azcollection with version 1.0.0.
  Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.
- check_point.mgmt with version 1.0.6.
  Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.
- chocolatey.chocolatey with version 1.0.2.
  Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.
- cisco.aci with version 1.0.0.
  The changes are reported in the combined changelog below.
- cisco.asa with version 1.0.3.
  The changes are reported in the combined changelog below.
- cisco.intersight with version 1.0.8.
  Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.
- cisco.ios with version 1.0.3.
  The changes are reported in the combined changelog below.
- cisco.iosxr with version 1.0.5.
  The changes are reported in the combined changelog below.
- cisco.meraki with version 2.0.0.
  The changes are reported in the combined changelog below.
- cisco.mso with version 1.0.0.
  The changes are reported in the combined changelog below.
- cisco.nxos with version 1.1.0.
  The changes are reported in the combined changelog below.
- cisco.ucs with version 1.5.0.
  Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.
- cloudscale_ch.cloud with version 1.1.0.
  The changes are reported in the combined changelog below.
- community.aws with version 1.2.0.
  The changes are reported in the combined changelog below.
- community.azure with version 1.0.0.
  The collection did not have a changelog in this version.
- community.crypto with version 1.1.1.
  The changes are reported in the combined changelog below.
- community.digitalocean with version 1.0.0.
  The changes are reported in the combined changelog below.
- community.general with version 1.1.0.
  The changes are reported in the combined changelog below.
- community.grafana with version 1.0.0.
  The changes are reported in the combined changelog below.
- community.kubernetes with version 1.0.0.
  The changes are reported in the combined changelog below.
- community.libvirt with version 1.0.0.
  The changes are reported in the combined changelog below.
- community.mongodb with version 1.0.0.
  The changes are reported in the combined changelog below.
- community.mysql with version 1.0.0.
  The changes are reported in the combined changelog below.
- community.network with version 1.1.0.
  The changes are reported in the combined changelog below.
- community.proxysql with version 1.0.0.
  The changes are reported in the combined changelog below.
- community.rabbitmq with version 1.0.1.
  The changes are reported in the combined changelog below.
- community.skydive with version 1.0.0.
  The changes are reported in the combined changelog below.
- community.vmware with version 1.2.0.
  The changes are reported in the combined changelog below.
- community.windows with version 1.0.0.
  The changes are reported in the combined changelog below.
- community.zabbix with version 1.0.0.
  The changes are reported in the combined changelog below.
- containers.podman with version 1.2.0.
  The changes are reported in the combined changelog below.
- cyberark.conjur with version 1.0.7.
  You can find the collection's changelog at `https://github.com/cyberark/ansible-conjur-collection/blob/master/CHANGELOG.md <https://github.com/cyberark/ansible-conjur-collection/blob/master/CHANGELOG.md>`_.
- cyberark.pas with version 1.0.5.
  Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.
- dellemc.os10 with version 1.0.1.
  The changes are reported in the combined changelog below.
- dellemc.os6 with version 1.0.2.
  The changes are reported in the combined changelog below.
- dellemc.os9 with version 1.0.2.
  The changes are reported in the combined changelog below.
- f5networks.f5_modules with version 1.5.0.
  Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.
- fortinet.fortimanager with version 1.0.5.
  The changes are reported in the combined changelog below.
- fortinet.fortios with version 1.0.15.
  The changes are reported in the combined changelog below.
- frr.frr with version 1.0.3.
  The changes are reported in the combined changelog below.
- gluster.gluster with version 1.0.1.
  The changes are reported in the combined changelog below.
- google.cloud with version 1.0.0.
  Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.
- hetzner.hcloud with version 1.0.0.
  The changes are reported in the combined changelog below.
- ibm.qradar with version 1.0.3.
  The changes are reported in the combined changelog below.
- infinidat.infinibox with version 1.2.3.
  Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.
- junipernetworks.junos with version 1.1.0.
  The changes are reported in the combined changelog below.
- mellanox.onyx with version 1.0.0.
  The changes are reported in the combined changelog below.
- netapp.aws with version 20.8.0.
  Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.
- netapp.elementsw with version 20.8.0.
  Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.
- netapp.ontap with version 20.8.0.
  Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.
- netapp_eseries.santricity with version 1.0.8.
  Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.
- netbox.netbox with version 1.0.2.
  The changes are reported in the combined changelog below.
- ngine_io.cloudstack with version 1.0.1.
  The changes are reported in the combined changelog below.
- ngine_io.exoscale with version 1.0.0.
  There are no changes recorded in the changelog.
- ngine_io.vultr with version 1.0.0.
  The changes are reported in the combined changelog below.
- openstack.cloud with version 1.1.0.
  The changes are reported in the combined changelog below.
- openvswitch.openvswitch with version 1.0.5.
  The changes are reported in the combined changelog below.
- ovirt.ovirt with version 1.1.3.
  The changes are reported in the combined changelog below.
- purestorage.flasharray with version 1.4.0.
  The changes are reported in the combined changelog below.
- purestorage.flashblade with version 1.3.0.
  The changes are reported in the combined changelog below.
- servicenow.servicenow with version 1.0.2.
  Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.
- splunk.es with version 1.0.2.
  The changes are reported in the combined changelog below.
- theforeman.foreman with version 1.1.0.
  The changes are reported in the combined changelog below.
- vyos.vyos with version 1.0.4.
  The changes are reported in the combined changelog below.
- wti.remote with version 1.0.1.
  Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.

Major Changes
-------------

Ansible-base
~~~~~~~~~~~~

- Both ansible-doc and ansible-console's help command will error for modules and plugins whose return documentation cannot be parsed as YAML. All modules and plugins passing ``ansible-test sanity --test yamllint`` will not be affected by this.
- Collections may declare a list of supported/tested Ansible versions for the collection. A warning is issued if a collection does not support the Ansible version that loads it (can also be configured as silent or a fatal error). Collections that do not declare supported Ansible versions do not issue a warning/error.
- Plugin routing allows collections to declare deprecation, redirection targets, and removals for all plugin types.
- Plugins that import module_utils and other ansible namespaces that have moved to collections should continue to work unmodified.
- Routing data built into Ansible 2.10 ensures that 2.9 content should work unmodified on 2.10. Formerly included modules and plugins that were moved to collections are still accessible by their original unqualified names, so long as their destination collections are installed.
- When deprecations are done in code, they to specify a ``collection_name`` so that deprecation warnings can mention which collection - or ansible-base - is deprecating a feature. This affects all ``Display.deprecated()`` or ``AnsibleModule.deprecate()`` or ``Ansible.Basic.Deprecate()`` calls, and ``removed_in_version``/``removed_at_date`` or ``deprecated_aliases`` in module argument specs.
- ansible-test now uses a different ``default`` test container for Ansible Collections

amazon.aws
~~~~~~~~~~

- ec2 module_utils - The ``AWSRetry`` decorator no longer catches ``NotFound`` exceptions by default.  ``NotFound`` exceptions need to be explicitly added using ``catch_extra_error_codes``.  Some AWS modules may see an increase in transient failures due to AWS''s eventual consistency model.

ansible.netcommon
~~~~~~~~~~~~~~~~~

- Add libssh connection plugin and refactor network_cli (https://github.com/ansible-collections/ansible.netcommon/pull/30)

ansible.posix
~~~~~~~~~~~~~

- Bootstrap Collection (https://github.com/ansible-collections/ansible.posix/pull/1).

cisco.meraki
~~~~~~~~~~~~

- Rewrite requests method for version 1.0 API and improved readability
- meraki_mr_rf_profile - Configure wireless RF profiles.
- meraki_mr_settings - Configure network settings for wireless.
- meraki_ms_l3_interface - New module
- meraki_ms_ospf - Configure OSPF.

community.general
~~~~~~~~~~~~~~~~~

- docker_container - the ``network_mode`` option will be set by default to the name of the first network in ``networks`` if at least one network is given and ``networks_cli_compatible`` is ``true`` (will be default from community.general 2.0.0 on). Set to an explicit value to avoid deprecation warnings if you specify networks and set ``networks_cli_compatible`` to ``true``. The current default (not specifying it) is equivalent to the value ``default``.
- docker_container - the module has a new option, ``container_default_behavior``, whose default value will change from ``compatibility`` to ``no_defaults``. Set to an explicit value to avoid deprecation warnings.
- gitlab_user - no longer requires ``name``, ``email`` and ``password`` arguments when ``state=absent``.

community.grafana
~~~~~~~~~~~~~~~~~

- Add changelog management for ansible 2.10 (#112)
- grafana_datasource ; adding additional_json_data param

community.kubernetes
~~~~~~~~~~~~~~~~~~~~

- Add changelog and fragments and document changelog process (https://github.com/ansible-collections/community.kubernetes/pull/131).
- helm - New module for managing Helm charts (https://github.com/ansible-collections/community.kubernetes/pull/61).
- helm_info - New module for retrieving Helm chart information (https://github.com/ansible-collections/community.kubernetes/pull/61).
- helm_plugin - new module to manage Helm plugins (https://github.com/ansible-collections/community.kubernetes/pull/154).
- helm_plugin_info - new modules to gather information about Helm plugins (https://github.com/ansible-collections/community.kubernetes/pull/154).
- helm_repository - New module for managing Helm repositories (https://github.com/ansible-collections/community.kubernetes/pull/61).
- k8s - Inventory source migrated from Ansible 2.9 to Kubernetes collection.
- k8s - Lookup plugin migrated from Ansible 2.9 to Kubernetes collection.
- k8s - Module migrated from Ansible 2.9 to Kubernetes collection.
- k8s_auth - Module migrated from Ansible 2.9 to Kubernetes collection.
- k8s_config_resource_name - Filter plugin migrated from Ansible 2.9 to Kubernetes collection.
- k8s_exec - New module for executing commands on pods via Kubernetes API (https://github.com/ansible-collections/community.kubernetes/pull/14).
- k8s_exec - Return rc for the command executed (https://github.com/ansible-collections/community.kubernetes/pull/158).
- k8s_info - Module migrated from Ansible 2.9 to Kubernetes collection.
- k8s_log - New module for retrieving pod logs (https://github.com/ansible-collections/community.kubernetes/pull/16).
- k8s_scale - Module migrated from Ansible 2.9 to Kubernetes collection.
- k8s_service - Module migrated from Ansible 2.9 to Kubernetes collection.
- kubectl - Connection plugin migrated from Ansible 2.9 to Kubernetes collection.
- openshift - Inventory source migrated from Ansible 2.9 to Kubernetes collection.

community.libvirt
~~~~~~~~~~~~~~~~~

- added generic libvirt inventory plugin
- removed libvirt_lxc inventory script

gluster.gluster
~~~~~~~~~~~~~~~

- geo_rep - Added the independent module of geo rep with other gluster modules (https://github.com/gluster/gluster-ansible-collection/pull/2).

ovirt.ovirt
~~~~~~~~~~~

- ovirt_disk - Add backup (https://github.com/oVirt/ovirt-ansible-collection/pull/57).
- ovirt_disk - Support direct upload/download (https://github.com/oVirt/ovirt-ansible-collection/pull/35).
- ovirt_host - Add ssh_port (https://github.com/oVirt/ovirt-ansible-collection/pull/60).
- ovirt_vm_os_info - Creation of module (https://github.com/oVirt/ovirt-ansible-collection/pull/26).

purestorage.flasharray
~~~~~~~~~~~~~~~~~~~~~~

- purefa_console - manage Console Lock setting for the FlashArray
- purefa_endpoint - manage VMware protocol-endpoints on the FlashArray
- purefa_eula - sign, or resign, FlashArray EULA
- purefa_inventory - get hardware inventory information from a FlashArray
- purefa_network - manage the physical and virtual network settings on the FlashArray
- purefa_pgsched - manage protection group snapshot and replication schedules on the FlashArray
- purefa_pod - manage ActiveCluster pods in FlashArrays
- purefa_pod_replica - manage ActiveDR pod replica links in FlashArrays
- purefa_proxy - manage the phonehome HTTPS proxy setting for the FlashArray
- purefa_smis - manage SMI-S settings on the FlashArray
- purefa_subnet - manage network subnets on the FlashArray
- purefa_timeout - manage the GUI idle timeout on the FlashArray
- purefa_vlan - manage VLAN interfaces on the FlashArray
- purefa_vnc - manage VNC for installed applications on the FlashArray
- purefa_volume_tags - manage volume tags on the FlashArray

purestorage.flashblade
~~~~~~~~~~~~~~~~~~~~~~

- purefb_alert - manage alert email settings on a FlashBlade
- purefb_bladename - manage FlashBlade name
- purefb_bucket_replica - manage bucket replica links on a FlashBlade
- purefb_connect - manage connections between FlashBlades
- purefb_dns - manage DNS settings on a FlashBlade
- purefb_fs_replica - manage filesystem replica links on a FlashBlade
- purefb_inventory - get information about the hardware inventory of a FlashBlade
- purefb_ntp - manage the NTP settings for a FlashBlade
- purefb_phonehome - manage the phone home settings for a FlashBlade
- purefb_policy - manage the filesystem snapshot policies for a FlashBlade
- purefb_proxy - manage the phone home HTTP proxy settings for a FlashBlade
- purefb_remote_cred - manage the Object Store Remote Credentials on a FlashBlade
- purefb_snmp_agent - modify the FlashBlade SNMP Agent
- purefb_snmp_mgr - manage SNMP Managers on a FlashBlade
- purefb_target - manage remote S3-capable targets for a FlashBlade
- purefb_user - manage local ``pureuser`` account password on a FlashBlade

Minor Changes
-------------

Ansible-base
~~~~~~~~~~~~

- 'Edit on GitHub' link for plugin, cli documentation fixed to navigate to correct plugin, cli source.
- Add 'auth_url' field to galaxy server config stanzas in ansible.cfg The url should point to the token_endpoint of a Keycloak server.
- Add --ask-vault-password and --vault-pass-file options to ansible cli commands
- Add ``--pre`` flag to ``ansible-galaxy collection install`` to allow pulling in the most recent pre-release version of a collection (https://github.com/ansible/ansible/issues/64905)
- Add a global toggle to control when vars plugins are executed (per task by default for backward compatibility or after importing inventory).
- Add a new config parameter, WIN_ASYNC_STARTUP_TIMEOUT, which allows configuration of the named pipe connection timeout under Windows when launching async tasks.
- Add a per-plugin stage option to override the global toggle to control the execution of individual vars plugins (per task, after inventory, or both).
- Add an additional check for importing journal from systemd-python module (https://github.com/ansible/ansible/issues/60595).
- Add an example for using var in with_sequence (https://github.com/ansible/ansible/issues/68836).
- Add new magic variable ``ansible_collection`` that contains the collection name
- Add new magic variable ``ansible_role_name`` that contains the FQCN of the role
- Add standard Python 2/3 compatibility boilerplate to setup script, module_utils and docs_fragments which were missing them.
- Added PopOS as a part of Debian OS distribution family (https://github.com/ansible/ansible/issues/69286).
- Added hostname support for PopOS in hostname module.
- Added openEuler OS in RedHat OS Family.
- Added the ability to set ``DEFAULT_NO_TARGET_SYSLOG`` through the ``ansible_no_target_syslog`` variable on a task
- Ansible CLI fails with warning if extra_vars parameter is used with filename without @ sign (https://github.com/ansible/ansible/issues/51857).
- Ansible modules created with ``add_file_common_args=True`` added a number of undocumented arguments which were mostly there to ease implementing certain action plugins. The undocumented arguments ``src``, ``follow``, ``force``, ``content``, ``backup``, ``remote_src``, ``regexp``, ``delimiter``, and ``directory_mode`` are now no longer added. Modules relying on these options to be added need to specify them by themselves. Also, action plugins relying on these extra elements in ``FILE_COMMON_ARGUMENTS`` need to be adjusted.
- Ansible now allows deprecation by date instead of deprecation by version. This is possible for plugins and modules (``meta/runtime.yml`` and ``deprecated.removed_at_date`` in ``DOCUMENTATION``, instead of ``deprecated.removed_in``), for plugin options (``deprecated.date`` instead of ``deprecated.version`` in ``DOCUMENTATION``), for module options (``removed_at_date`` instead of ``removed_in_version`` in argument spec), and for module option aliases (``deprecated_aliases.date`` instead of ``deprecated_aliases.version`` in argument spec).
- Ansible should fail with error when non-existing limit file is provided in command line.
- Ansible.Basic - Added the ability to specify multiple fragments to load in a generic way for modules that use a module_util with fragment options
- Ansible.Basic.cs - Added support for ``deprecated_aliases`` to deprecated aliases in a standard way
- Ansible.ModuleUtils.WebRequest - Move username and password aliases out of util to avoid option name collision
- Change order of arguments in ansible cli to use --ask-vault-password and --vault-password-file by default
- CollectionRequirement - Add a metadata property to update and retrieve the _metadata attribute.
- Command module: Removed suggestions to use modules which have moved to collections and out of ansible-base
- Enable Ansible Collections loader to discover and import collections from ``site-packages`` dir and ``PYTHONPATH``-added locations.
- Enable testing the AIX platform as a remote OS in ansible-test
- Fixed ansible-doc to not substitute for words followed by parenthesis.  For instance, ``IBM(International Business Machines)`` will no longer be substituted with a link to a non-existent module. https://github.com/ansible/ansible/pull/71070
- Flatten the directory hierarchy of modules
- Ignore plesk-release file while parsing distribution release (https://github.com/ansible/ansible/issues/64101).
- Openstack inventory script is migrated to ansible-openstack-collection, adjusted the link in documentation accordingly.
- Openstack inventory script is moved to openstack.cloud from community.general.
- PowerShell Add-Type - Add an easier way to reference extra types when compiling C# code on PowerShell Core
- PowerShell Add-Type - Added the ``X86`` and ``AMD64`` preprocessor symbols for conditional compiling
- Prevent losing useful error information by including both the loop and the conditional error messages (https://github.com/ansible/ansible/issues/66529)
- Provides additional information about collection namespace name restrictions (https://github.com/ansible/ansible/issues/65151).
- Raise error when no task file is provided to import_tasks (https://github.com/ansible/ansible/issues/54095).
- Refactor test_distribution_version testcases.
- Remove the deprecation message for the ``TRANSFORM_INVALID_GROUP_CHARS`` setting. (https://github.com/ansible/ansible/issues/61889)
- Removed extras_require support from setup.py (and [azure] extra). Requirements will float with the collections, so it's not appropriate for ansible-base to host requirements for them any longer.
- Simplify dict2items filter example in loop documentation (https://github.com/ansible/ansible/issues/65505).
- Templating - Add globals to the jinja2 environment at ``Templar`` instantiation, instead of customizing the template object. Only customize the template object, to disable lookups. (https://github.com/ansible/ansible/pull/69278)
- Templating - Add support to auto unroll generators produced by jinja2 filters, to prevent the need of explicit use of ``|list`` (https://github.com/ansible/ansible/pull/68014)
- The plugin loader now keeps track of the collection where a plugin was resolved to, in particular whether the plugin was loaded from ansible-base's internal paths (``ansible.builtin``) or from user-supplied paths (no collection name).
- The results queue and counter for results are now split for standard / handler results. This allows the governing strategy to be truly independent from the handler strategy, which basically follows the linear methodology.
- Update required library message with correct grammer in basic.py.
- Updated inventory script location for EC2, Openstack, and Cobbler after collection (https://github.com/ansible/ansible/issues/68897).
- Updated inventory script location for infoblox, ec2 and other after collection migration (https://github.com/ansible/ansible/issues/69139).
- Updated network integration auth timeout to 90 secs.
- Updates ``ansible_role_names``, ``ansible_play_role_names``, and ``ansible_dependent_role_names`` to include the FQCN
- Use OrderedDict by default when importing mappings from YAML.
- Windows - Add a check for the minimum PowerShell version so we can create a friendly error message on older hosts
- Windows - add deprecation notice in the Windows setup module when running on Server 2008, 2008 R2, and Windows 7
- `AnsibleModule.fail_json()` has always required that a message be passed in which informs the end user why the module failed.  In the past this message had to be passed as the `msg` keyword argument but it can now be passed as the first positional argument instead.
- ``AnsibleModule.load_file_common_arguments`` now allows to simply override ``path``.
- add mechanism for storing warnings and deprecations globally and not attached to an ``AnsibleModule`` object (https://github.com/ansible/ansible/pull/58993)
- added more ways to configure new uri options in 2.10.
- ansible-doc - improve suboptions formatting (https://github.com/ansible/ansible/pull/69795).
- ansible-doc - now indicates if an option is added by a doc fragment from another collection by prepending the collection name, or ``ansible.builtin`` for ansible-base, to the version number.
- ansible-doc - return values will be properly formatted (https://github.com/ansible/ansible/pull/69796).
- ansible-doc will now format, ``L()``, ``R()``, and ``HORIZONTALLINE`` in plugin docs just as the website docs do.  https://github.com/ansible/ansible/pull/71070
- ansible-galaxy - Add ``download`` option for ``ansible-galaxy collection`` to download collections and their dependencies for an offline install
- ansible-galaxy - Add a `verify` subcommand to `ansible-galaxy collection`. The collection found on the galaxy server is downloaded to a tempfile to compare the checksums of the files listed in the MANIFEST.json and the FILES.json with the contents of the installed collection.
- ansible-galaxy - Add installation successful message
- ansible-galaxy - Added the ability to display the progress wheel through the C.GALAXY_DISPLAY_PROGRESS config option. Also this now defaults to displaying the progress wheel if stdout has a tty.
- ansible-galaxy - Added the ability to ignore further files and folders using a pattern with the ``build_ignore`` key in a collection's ``galaxy.yml`` (https://github.com/ansible/ansible/issues/59228).
- ansible-galaxy - Allow installing collections from git repositories.
- ansible-galaxy - Always ignore the ``tests/output`` directory when building a collection as it is used by ``ansible-test`` for test output (https://github.com/ansible/ansible/issues/59228).
- ansible-galaxy - Change the output verbosity level of the download message from 3 to 0 (https://github.com/ansible/ansible/issues/70010)
- ansible-galaxy - Display message if both collections and roles are specified in a requirements file but can't be installed together.
- ansible-galaxy - Install both collections and roles with ``ansible-galaxy install -r requirements.yml`` in certain scenarios.
- ansible-galaxy - Requirement entries for collections now support a 'type' key to indicate whether the collection is a galaxy artifact, file, url, or git repo.
- ansible-galaxy - Support both 'galaxy.yml' and 'galaxy.yaml' files for collections.
- ansible-galaxy - add ``--token`` argument which is the same as ``--api-key`` (https://github.com/ansible/ansible/issues/65955)
- ansible-galaxy - add ``collection list`` command for listing installed collections (https://github.com/ansible/ansible/pull/65022)
- ansible-galaxy - add ``validate_collection_path()`` utility function ()
- ansible-galaxy - add collections path argument
- ansible-galaxy - allow role to define dependency requirements that will be only installed by defining them in ``meta/requirements.yml`` (https://github.com/ansible/proposals/issues/57)
- ansible-test - --docker flag now has an associated --docker-terminate flag which controls if and when the docker container is removed following tests
- ansible-test - Add ``macos/10.15`` as a supported value for the ``--remote`` option.
- ansible-test - Add a test to prevent ``state=get``
- ansible-test - Add a test to prevent ``state=list`` and ``state=info``
- ansible-test - Add a verbosity option for displaying warnings.
- ansible-test - Add support for Python 3.9.
- ansible-test - Added CI provider support for Azure Pipelines.
- ansible-test - Added a ``ansible-test coverage analyze targets filter`` command to filter aggregated coverage reports by path and/or target name.
- ansible-test - Added a ``ansible-test coverage analyze targets`` command to analyze integration test code coverage by test target.
- ansible-test - Added support for Ansible Core CI request signing for Shippable.
- ansible-test - Added support for testing on Fedora 32.
- ansible-test - Allow custom ``--remote-stage`` options for development and testing.
- ansible-test - Fix ``ansible-test coverage`` reporting sub-commands (``report``, ``html``, ``xml``) on Python 2.6.
- ansible-test - General code cleanup.
- ansible-test - Now includes testing support for RHEL 8.2
- ansible-test - Provisioning of RHEL instances now includes installation of pinned versions of ``packaging`` and ``pyparsing`` to match the downstream vendored versions.
- ansible-test - Refactor code to consolidate filesystem access and improve handling of encoding.
- ansible-test - Refactored CI related logic into a basic provider abstraction.
- ansible-test - Remove ``pytest < 6.0.0`` constraint for managed installations on Python 3.x now that pytest 6 is supported.
- ansible-test - Remove obsolete support for provisioning remote vCenter instances. The supporting services are no longer available.
- ansible-test - Remove the discontinued ``us-east-2`` choice from the ``--remote-aws-region`` option.
- ansible-test - Report the correct line number in the ``yamllint`` sanity test when reporting ``libyaml`` parse errors in module documentation.
- ansible-test - Request remote resources by provider name for all provider types.
- ansible-test - Show a warning when the obsolete ``--remote-aws-region`` option is used.
- ansible-test - Support custom remote endpoints with the ``--remote-endpoint`` option.
- ansible-test - Support writing compact JSON files instead of formatting and indenting the output.
- ansible-test - Update Ubuntu 18.04 test container to version 1.13 which includes ``venv``
- ansible-test - Update ``default-test-container`` to version 1.11, which includes Python 3.9.0a4.
- ansible-test - Update built-in service endpoints for the ``--remote`` option.
- ansible-test - Updated the default test containers to include Python 3.9.0b3.
- ansible-test - Upgrade OpenSUSE containers to use Leap 15.1.
- ansible-test - Upgrade distro test containers from 1.16.0 to 1.17.0
- ansible-test - Upgrade from ansible-base-test-container 1.1 to 2.2
- ansible-test - Upgrade from default-test-container 2.1 to 2.2
- ansible-test - Use new endpoint for Parallels based instances with the ``--remote`` option.
- ansible-test - ``mutually_exclusive``, ``required_if``, ``required_by``, ``required_together`` and ``required_one_of`` in modules are now validated.
- ansible-test - ``validate-modules`` now also accepts an ISO 8601 formatted date as ``deprecated.removed_at_date``, instead of requiring a version number in ``deprecated.removed_in``.
- ansible-test - ``validate-modules`` now makes sure that module documentation deprecation removal version and/or date matches with removal version and/or date in meta/runtime.yml.
- ansible-test - ``validate-modules`` now validates all version numbers in documentation and argument spec. Version numbers for collections are checked for being valid semantic versioning version number strings.
- ansible-test - add ``validate-modules`` tests for ``removed_in_version`` and ``deprecated_aliases`` (https://github.com/ansible/ansible/pull/66920/).
- ansible-test - add check for ``print()`` calls in modules and module_utils.
- ansible-test - added a ``--no-pip-check`` option
- ansible-test - added a ``--venv-system-site-packages`` option for use with the ``--venv`` option
- ansible-test - added new ``changelog`` test, which runs if a `antsibull-changelog <https://pypi.org/project/antsibull-changelog/>`_ configuration or files in ``changelogs/fragments/`` are found (https://github.com/ansible/ansible/pull/69313).
- ansible-test - allow delegation config to specify equivalents to the ``--no-pip-check``, ``--disable-httptester`` and `--no-temp-unicode`` options
- ansible-test - allow sanity tests to check for optional errors by specifying ``--enable-optional-errors`` (https://github.com/ansible/ansible/pull/66920/).
- ansible-test - also run the ``ansible-doc`` sanity test with ``--json`` to ensure that the documentation does not contain something that cannot be exported as JSON (https://github.com/ansible/ansible/issues/69238).
- ansible-test - default container now uses default-test-container 2.7.0 and ansible-base-test-container 1.6.0. This brings in Python 3.9.0rc1 for testing.
- ansible-test - enable deprecated version testing for modules and ``module.deprecate()`` calls (https://github.com/ansible/ansible/pull/66920/).
- ansible-test - extend alias validation.
- ansible-test - fixed ``units`` command with ``--docker`` to (mostly) work under podman
- ansible-test - improve module validation so that ``default``, ``sample`` and ``example`` contain JSON values and not arbitrary YAML values, like ``datetime`` objects or dictionaries with non-string keys.
- ansible-test - module validation will now consider arguments added by ``add_file_common_arguments=True`` correctly.
- ansible-test - switch from testing RHEL 8.0 and RHEL 8.1 Beta to RHEL 8.1
- ansible-test - the ACME test container was updated, it now supports external account creation and has a basic OCSP responder (https://github.com/ansible/ansible/pull/71097, https://github.com/ansible/acme-test-container/releases/tag/2.0.0).
- ansible-test - the argument spec of modules is now validated by a YAML schema.
- ansible-test - the module validation code now checks whether ``elements`` documentation for options matches the argument_spec.
- ansible-test - the module validation code now checks whether ``elements`` is defined when ``type=list``
- ansible-test - the module validation code now checks whether ``requirement`` for options is documented correctly.
- ansible-test add pyparsing constraint for Python 2.x to avoid compatibility issues with the upcoming pyparsing 3 release
- ansible-test defaults to redacting sensitive values (disable with the ``--no-redact`` option)
- ansible-test has been updated to use ``default-test-container:1.13`` which includes fewer Python requirements now that most modules and tests have been migrated to collections.
- ansible-test no longer detects ``git`` submodule directories as files.
- ansible-test no longer provides a ``--tox`` option. Use the ``--venv`` option instead. This only affects testing the Ansible source. The feature was never available for Ansible Collections or when running from an Ansible install.
- ansible-test no longer tries to install sanity test dependencies on unsupported Python versions
- ansible-test now checks for the minimum and maximum supported versions when importing ``coverage``
- ansible-test now filters out unnecessary warnings and messages from pip when installing its own requirements
- ansible-test now has a ``--list-files`` option to list files using the ``env`` command.
- ansible-test now includes the ``pylint`` plugin ``mccabe`` in optional sanity tests enabled with ``--enable-optional-errors``
- ansible-test now places the ansible source and collections content in separate directories when using the ``--docker`` or ``--remote`` options.
- ansible-test now provides a more helpful error when loading coverage files created by ``coverage`` version 5 or later
- ansible-test now supports provisioning of network resources when testing network collections
- ansible-test now supports skip aliases in the format ``skip/{arch}/{platform}`` and ``skip/{arch}/{platform}/{version}`` where ``arch`` can be ``power``. These aliases are only effective for the ``--remote`` option.
- ansible-test now supports skip aliases in the format ``skip/{platform}/{version}`` for the ``--remote`` option. This is preferred over the older ``skip/{platform}{version}`` format which included no ``/`` between the platform and version.
- ansible-test now supports testing against RHEL 7.8 when using the ``--remote`` option.
- ansible-test now supports the ``--remote power/centos/7`` platform option.
- ansible-test now validates the schema of ansible_builtin_runtime.yml and a collections meta/runtime.yml file.
- ansible-test provides clearer error messages when failing to detect the provider to use with the ``--remote`` option.
- ansible-test provisioning of network devices for ``network-integration`` has been updated to use collections.
- ansible_native_concat() - use ``to_text`` function rather than Jinja2's ``text_type`` which has been removed in Jinja2 master branch.
- apt - Implemented an exponential backoff behaviour when retrying to update the cache with new params ``update_cache_retry_max_delay`` and ``update_cache_retries`` to control the behavior.
- apt_repository - Implemented an exponential backoff behaviour when retrying to update the apt cache with new params ``update_cache_retry_max_delay`` and ``update_cache_retries`` to control the behavior.
- blockinfile - Update module documentation to clarify insertbefore/insertafter usage.
- callbacks - Allow modules to return `None` as before/after entries for diff. This should make it easier for modules to report the "not existing" state of the entity they touched.
- combine filter - now accept a ``list_merge`` argument which modifies its behaviour when the hashes to merge contain arrays/lists.
- conditionals - change the default of CONDITIONAL_BARE_VARS to False (https://github.com/ansible/ansible/issues/70682).
- config - accept singular version of ``collections_path`` ini setting and ``ANSIBLE_COLLECTIONS_PATH`` environment variable setting
- core filters - Adding ``path_join`` filter to the core filters list
- debconf - add a note about no_log=True since module might expose sensitive information to logs (https://github.com/ansible/ansible/issues/32386).
- default_callback - moving 'check_mode_markers' documentation in default_callback doc_fragment (https://github.com/ansible-collections/community.general/issues/565).
- distro - Update bundled version of distro from 1.4.0 to 1.5.0
- dnf - Properly handle idempotent transactions with package name wildcard globs (https://github.com/ansible/ansible/issues/62809)
- dnf - Properly handle module AppStreams that don't define stream (https://github.com/ansible/ansible/issues/63683)
- dnf param to pass allowerasing
- downstream packagers may install packages under ansible._vendor, which will be added to head of sys.path at ansible package load
- file - specifying ``src`` without ``state`` is now an error
- galaxy - add documentation about galaxy parameters in examples/ansible.cfg (https://github.com/ansible/ansible/issues/68402).
- get_bin_path() - change the interface to always raise ``ValueError`` if the command is not found (https://github.com/ansible/ansible/pull/56813)
- get_url - Remove deprecated string format support for the headers option (https://github.com/ansible/ansible/issues/61891)
- git - added an ``archive_prefix`` option to set a prefix to add to each file path in archive
- host_group_vars plugin - Require whitelisting and whitelist by default.
- iptables - add a note about ipv6-icmp in protocol parameter (https://github.com/ansible/ansible/issues/70905).
- new magic variable - ``ansible_config_file`` - full path of used Ansible config file
- package_facts.py - Add support for Pacman package manager.
- pipe lookup - update docs for Popen with shell=True usages (https://github.com/ansible/ansible/issues/70159).
- plugin loader - Add MODULE_IGNORE_EXTS config option to skip over certain extensions when looking for script and binary modules.
- powershell (shell plugin) - Fix `join_path` to support UNC paths (https://github.com/ansible/ansible/issues/66341)
- regexp_replace filter - add multiline support for regex_replace filter (https://github.com/ansible/ansible/issues/61985)
- rename ``_find_existing_collections()`` to ``find_existing_collections()`` to reflect its use across multiple files
- reorganized code for the ``ansible-test coverage`` command for easier maintenance and feature additions
- service_facts - Added undocumented 'indirect' and 'static' as service status (https://github.com/ansible/ansible/issues/69752).
- setup.py - Skip doing conflict checks for ``sdist`` and ``egg_info`` commands (https://github.com/ansible/ansible/pull/71310)
- ssh - connection plugin now supports a new variable ``sshpass_prompt`` which gets passed to ``sshpass`` allowing the user to set a custom substring to search for a password prompt (requires sshpass 1.06+)
- subelements - clarify the lookup plugin documentation for parameter handling (https://github.com/ansible/ansible/issues/38182).
- systemd - default scope is now explicitly "system"
- tests - Add new ``truthy`` and ``falsy`` jinja2 tests to evaluate the truthiness or falsiness of a value
- to_nice_json filter - Removed now-useless exception handler
- to_uuid - add a named parameter to let the user optionally set a custom namespace
- update ansible-test default-test-container from version 1.13 to 1.14, which includes an update from Python 3.9.0a6 to Python 3.9.0b1
- update ansible-test default-test-container from version 1.9.1 to 1.9.2
- update ansible-test default-test-container from version 1.9.2 to 1.9.3
- update ansible-test default-test-container from version 1.9.3 to 1.10.1
- update ansible-test images to 1.16.0, which includes system updates and pins CentOS versions
- uri/galaxy - Add new ``prepare_multipart`` helper function for creating a ``multipart/form-data`` body (https://github.com/ansible/ansible/pull/69376)
- url_lookup_plugin - add parameters to match what is available in ``module_utils/urls.py``
- user - allow groups, append parameters with local
- user - usage of ``append: True`` without setting a list of groups. This is currently a no-op with a warning, and will change to an error in 2.14. (https://github.com/ansible/ansible/pull/65795)
- validate-modules checks for deprecated in collections against meta/runtime.yml
- validation - Sort missing parameters in exception message thrown by check_required_arguments
- vars plugins - Support vars plugins in collections by adding the ability to whitelist plugins.
- vars_prompt - throw error when encountering unsupported key
- win_package - Added proxy support for retrieving packages from a URL - https://github.com/ansible/ansible/issues/43818
- win_package - Added support for ``.appx``, ``.msix``, ``.appxbundle``, and ``.msixbundle`` package - https://github.com/ansible/ansible/issues/50765
- win_package - Added support for ``.msp`` packages - https://github.com/ansible/ansible/issues/22789
- win_package - Added support for specifying the HTTP method when getting files from a URL - https://github.com/ansible/ansible/issues/35377
- win_package - Read uninstall strings from the ``QuietUninstallString`` if present to better support argumentless uninstalls of registry based packages.
- win_package - Scan packages in the current user's registry hive - https://github.com/ansible/ansible/issues/45950
- windows collections - Support relative module util imports in PowerShell modules and module_utils

amazon.aws
~~~~~~~~~~

- Add `aws_security_token`, `aws_endpoint_url` and `endpoint_url` aliases to improve AWS module parameter naming consistency.
- Add support for `aws_ca_bundle` to boto3 based AWS modules
- Add support for configuring boto3 profiles using `AWS_PROFILE` and `AWS_DEFAULT_PROFILE`
- Added check_mode support to aws_az_info
- Added check_mode support to ec2_eni_info
- Added check_mode support to ec2_snapshot_info
- ansible_dict_to_boto3_filter_list - convert integers and bools to strings before using them in filters.
- aws_direct_connect_virtual_interface - add direct_connect_gateway_id parameter. This field is only applicable in private VIF cases (public=False) and is mutually exclusive to virtual_gateway_id.
- cloudformation - Return change_set_id in the cloudformation output if a change set was created.
- ec2 - deprecate allowing both group and group_id - currently we ignore group_id if both are passed.
- ec2 module_utils - Update ``ec2_connect`` (boto2) behaviour so that ``ec2_url`` overrides ``region``.
- ec2_ami_info - allow integer and bool values for filtering images (https://github.com/ansible/ansible/issues/43570).
- ec2_asg - Add support for Max Instance Lifetime
- ec2_asg - Add the ability to use mixed_instance_policy in launch template driven autoscaling groups
- ec2_asg - Migrated to AnsibleAWSModule
- ec2_placement_group - make `name` a required field.
- ec2_vol_info - Code cleanup and use of the AWSRetry decorator to improve stability
- ec2_vpc_net - Enable IPv6 CIDR assignment
- module_utils.core - Support passing arbitrary extra keys to fail_json_aws, matching capabilities of fail_json.

ansible.netcommon
~~~~~~~~~~~~~~~~~

- Add content option validation for netconf_config module (https://github.com/ansible-collections/ansible.netcommon/pull/66)
- Added description to collection galaxy.yml file.
- Documentation of module arguments updated to match expected types where missing.
- NetworkConfig objects now have an optional `comment_tokens` parameter which takes a list of strings which will override the DEFAULT_COMMENT_TOKENS list.
- New cli_parse module for parsing structured text using a variety of parsers. The initial implemetation of cli_parse can be used with json, native, ntc_templates, pyats, textfsm, ttp, and xml.
- Resource Modules: changed flag is set to true in check_mode for all ACTION_STATES (https://github.com/ansible-collections/ansible.netcommon/pull/82)
- The httpapi connection plugin now works with `wait_for_connection`. This will periodically request the root page of the server described by the plugin's options until the request succeeds. This can only test that the server is reachable, the correctness or usability of the API is not guaranteed.

ansible.posix
~~~~~~~~~~~~~

- CI should use devel (https://github.com/ansible-collections/ansible.posix/pull/6).
- Enable tests for at, patch and synchronize modules (https://github.com/ansible-collections/ansible.posix/pull/5).
- Enabled tags in galaxy.yml (https://github.com/ansible-collections/ansible.posix/issues/18).
- Migrate hacking/cgroup_perf_recap_graph.py to this collection, since the cgroup_perf_recap callback lives here.
- Remove license key from galaxy.yml.
- Remove sanity jobs from shippable (https://github.com/ansible-collections/ansible.posix/pull/43).
- Removed ANSIBLE_METADATA from all the modules.
- Revert "Enable at, patch and synchronize tests (https://github.com/ansible-collections/ansible.posix/pull/5)".
- Update EXAMPLES section in modules to use FQCN.
- Update README.md (https://github.com/ansible-collections/ansible.posix/pull/4/).
- firewalld - add firewalld module to ansible.posix collection
- skippy - fixed the deprecation warning (by date) for skippy callback plugin

ansible.windows
~~~~~~~~~~~~~~~

- Checks for and resolves a condition where effective nameservers are obfucated, usually by malware. See https://www.welivesecurity.com/2016/06/02/crouching-tiger-hidden-dns/
- Windows - add deprecation notice in the Windows setup module when running on Server 2008, 2008 R2, and Windows 7
- setup - Added `ansible_architecture2`` to match the same format that setup on POSIX hosts return. Unlike ``ansible_architecture`` this value is not localized to the host's language settings.
- setup - Implemented the ``gather_timeout`` option to restrict how long each subset can run for
- setup - Refactor to speed up the time taken to run the module
- setup.ps1 - parity with linux regarding missing local facts path (https://github.com/ansible/ansible/issues/57974)
- win_command, win_shell - Add the ability to override the console output encoding with ``output_encoding_override`` - https://github.com/ansible/ansible/issues/54896
- win_dns_client - Added support for setting IPv6 DNS servers - https://github.com/ansible/ansible/issues/55962
- win_domain_computer - Use new Ansible.Basic wrapper for better invocation reporting
- win_domain_controller - Added the ``domain_log_path`` to control the directory for the new AD log files location - https://github.com/ansible/ansible/issues/59348
- win_find - Improve performance when scanning heavily nested directories and align behaviour to the ``find`` module.
- win_hostname - Added diff mode support
- win_hostname - Use new ``Ansible.Basic.AnsibleModule`` wrapper
- win_package - Added proxy support for retrieving packages from a URL - https://github.com/ansible/ansible/issues/43818
- win_package - Added support for ``.appx``, ``.msix``, ``.appxbundle``, and ``.msixbundle`` package - https://github.com/ansible/ansible/issues/50765
- win_package - Added support for ``.msp`` packages - https://github.com/ansible/ansible/issues/22789
- win_package - Added support for specifying the HTTP method when getting files from a URL - https://github.com/ansible/ansible/issues/35377
- win_package - Move across to ``Ansible.Basic`` for better invocation logging
- win_package - Read uninstall strings from the ``QuietUninstallString`` if present to better support argumentless uninstalls of registry based packages.
- win_package - Scan packages in the current user's registry hive - https://github.com/ansible/ansible/issues/45950
- win_regedit - Use new Ansible.Basic wrapper for better invocation reporting
- win_share - Implement append parameter for access rules (https://github.com/ansible/ansible/issues/59237)
- win_user - Added check mode support
- win_user - Added diff mode support
- win_user - Added the ``home_directory`` option
- win_user - Added the ``login_script`` option
- win_user - Added the ``profile`` option
- win_user - Use new ``Ansible.Basic.AnsibleModule`` wrapper for better invocation reporting
- win_user_right - Improved error messages to show what right and account an operation failed on
- win_user_right - Refactored to use ``Ansible.Basic.AnsibleModule`` for better module invocation reporting
- windows setup - Added ``ansible_os_installation_type`` to denote the type of Windows installation the remote host is.

arista.eos
~~~~~~~~~~

- Add round trip testcases to the 2.9 resource modules.
- Add unit testcases to the eos_l3_interfaces resource modules.
- Add unit testcases to the eos_lag_interfaces resource modules.
- Sorted the list of params of ip address before forming the tuple.
- Updated docs.

cisco.aci
~~~~~~~~~

- Add Fex capability to aci_interface_policy_leaf_profile, aci_access_port_to_interface_policy_leaf_profile and aci_access_port_block_to_access_port
- Add LICENSE file
- Add aci_epg_to_contract_master module
- Add annotation attribute to aci.py and to doc fragment.
- Add annotation to every payload and add test case for annotation.
- Add changelog
- Add collection prefix to all integration tests
- Add galaxy.yml file for collection listing
- Add github action CI pipeline
- Add module and test file for aci_bd_dhcp_label
- Add modules and test files for aci_cloud_ctx_profile, aci_cloud_cidr, aci_cloud_subnet and aci_cloud_zone
- Add modules and test files for aci_l2out, aci_l2out_extepg and aci_l3out_extepg_to_contract
- Add names to documentation examples for modules from community.network
- Add preferred group support to aci_vrf
- Add support for Azure on all cloud modules
- Add support for output_path to allow dump of REST API objects
- Add support for owner_key and owner_tag for all modules and add test case for it.
- Add vpn gateway dedicated module and remove vpn_gateway from cloud_ctx_profile module
- Fix M() and module to use FQCN
- Initial commit based on the collection migration available at "ansible-collection-migration/cisco.aci" which contains the ACI module from Ansible Core
- Move aci.py to base of module_utils and fix references
- Move test file to root of tests/unit/module_utils
- Update Ansible version in CI and add 2.10.0 to sanity in CI.
- Update Readme with supported versions
- Update to test files to make the tests work on both 3.2 and 4.2.

cisco.asa
~~~~~~~~~

- Removes Cisco ASA sanity ignores and sync for argspec and docstring (https://github.com/ansible-collections/cisco.asa/pull/59).
- Updated docs.

cisco.ios
~~~~~~~~~

- Removes IOS sanity ignores and sync for argspec and docstring (https://github.com/ansible-collections/cisco.ios/pull/114).
- Updated docs.

cisco.iosxr
~~~~~~~~~~~

- Bring plugin table to correct position (https://github.com/ansible-collections/cisco.iosxr/pull/44)

cisco.meraki
~~~~~~~~~~~~

- meraki_admin - Update endpoints for API v1
- meraki_device - Added query parameter
- meraki_intrusion_prevention - Change documentation to show proper way to clear rules
- meraki_mx_uplink - Renamed to meraki_mx_uplink_bandwidth
- meraki_ssid - Add `WPA3 Only` and `WPA3 Transition Mode`
- meraki_switchport - Add support for `access_policy_type` parameter

cisco.mso
~~~~~~~~~

- ACI/MSO - Use get() dict lookups (https://github.com/ansible/ansible/pull/63074)
- Add EPG and ANP at site level when needed
- Add Login Domain support to mso_site
- Add aliases file for contract_filter module
- Add changelog
- Add contract information in current and previous part
- Add github action CI pipeline with test coverage
- Add l3out, preferred_group and test file for mso_schema_template_externalepg
- Add login domain support for authentication in all modules
- Add mso_schema_template_vrf_contract module and test file
- Add new attribute choice "policy_compression" to mso_Schema_template_contract_filter
- Add new functionality - Direct Port Channel (dpc), micro-seg-vlan and default values
- Add new module and test file to query MSO version
- Add new module for anp-epg-selector in site level
- Add new module mso_schema_template_anp_epg_selector and its test file
- Add new module mso_schema_vrf_contract
- Add new module mso_tenant_site to support cloud and non-cloud sites association with a tenant and test file (https://github.com/CiscoDevNet/ansible-mso/pull/62)
- Add new mso_site_external_epg_selector module and test file
- Add site external epg and contract filter test
- Add support for DHCP querier to all subnet objects. Add partial test in mso_schema_template_bd integration test.
- Add support for VGW attribute in mso_schema_site_vrf_region_cidr_subnet
- Add support for clean output if needed for debuging
- Add support to set account as inactive using account_status attribute in mso_user
- Add test file for mso_schema_template_anp_epg
- Add test for mso_schema_site_vrf_region_cidr module
- Add test for mso_schema_site_vrf_region_cidr_subnet module
- Add vzAny attribute in mso_schema_template_vrf
- Added DHCP relay options and scope options to MSO schema template bd
- Added ability to bind epg to static fex port
- Added module to manage contracts for external EPG in Cisco MSO (https://github.com/ansible/ansible/pull/63550)
- Added module to manage template external epg subnet for Cisco MSO (https://github.com/ansible/ansible/pull/63542)
- Automatically add ANP and EPG at site level and new test file for mso_schema_site_anp_epg_staticport (https://github.com/CiscoDevNet/ansible-mso/pull/55)
- Disabling tests for the role modules as API is not supported after 2.2.3i until further notice
- Fix M() and module to use FQCN
- Increased test coverage for existing module integration tests.
- Modified External EPG module and addition of new Selector module
- Modified fail messages for site and updated documentation
- Moving test to Ansible v2.9.9 and increasing timelimit for mutex to 30+ min
- New backup module and test file (https://github.com/CiscoDevNet/ansible-mso/pull/80)
- Renaming mso_schema_template_externalepg module to mso_schema_template_external_epg while keeping both working.
- Update Ansible version in CI and add 2.10.0 to sanity in CI.
- Update Readme with supported versions
- Update authors.
- Update cidr module, udpate attributes in hub network module and its test file
- Update mso_schema_site_anp.py (https://github.com/ansible/ansible/pull/67099)
- Updated Test File Covering all conditions
- Use a function to reuuse duplicate part
- mso_schema_site_anp_epg_staticport - Add VPC support (https://github.com/ansible/ansible/pull/62803)

cisco.nxos
~~~~~~~~~~

- Add N9K multisite support(https://github.com/ansible-collections/cisco.nxos/pull/142)
- documentation - Use FQCN when refering to modules (https://github.com/ansible-collections/cisco.nxos/pull/116)

cloudscale_ch.cloud
~~~~~~~~~~~~~~~~~~~

- floating_ip - added tags support (https://github.com/cloudscale-ch/ansible-collection-cloudscale/pull/16)

community.aws
~~~~~~~~~~~~~

- Add retries for aws_api_gateway when AWS throws `TooManyRequestsException`
- Allow all params that boto support in aws_api_gateway module
- Migrate the remaning boto3 based modules to the module based helpers for creating AWS connections.
- Remaining community.aws AnsibleModule based modules migrated to AnsibleAWSModule.
- aws_acm - Add the module to group/aws for module_defaults.
- aws_acm - Update automatic retries to stabilize the integration tests.
- aws_codecommit - Support updating the description
- aws_kms - Adds the ``enable_key_rotation`` option to enable or disable automatically key rotation.
- aws_kms - code refactor, some error messages updated
- aws_kms_info - Adds the ``enable_key_rotation`` info to the return value.
- ec2_asg - Add support for Max Instance Lifetime
- ec2_asg - Add the ability to use mixed_instance_policy in launch template driven autoscaling groups
- ec2_asg - Migrated to AnsibleAWSModule
- ec2_placement_group - make ``name`` a required field.
- ecs_task_definition - Add network_mode=default to support Windows ECS tasks.
- elb_network_lb - added support to UDP and TCP_UDP protocols
- elb_target - add awsretry to prevent rate exceeded errors (https://github.com/ansible/ansible/issues/51108)
- elb_target_group - allow UDP and TCP_UDP protocols; permit only HTTP/HTTPS health checks using response codes and paths
- iam - make ``name`` a required field.
- iam_cert - make ``name`` a required field.
- iam_policy - The iam_policy module has been migrated from boto to boto3.
- iam_policy - make ``iam_name`` a required field.
- iam_role - Add support for managing the maximum session duration
- iam_role - Add support for removing the related instance profile when we delete the role
- iam_role, iam_user and iam_group - the managed_policy option has been renamed to managed_policies (with an alias added)
- iam_role, iam_user and iam_group - the purge_policy option has been renamed to purge_policies (with an alias added)
- lambda - add a tracing_mode parameter to set the TracingConfig for AWS X-Ray. Also allow updating Lambda runtime.
- purefa_volume - Change I(qos) parameter to I(bw_iops), but retain I(qos) as an alias for backwards compatability (https://github.com/ansible/ansible/pull/61577).
- redshift - Add AWSRetry calls for errors outside our control
- route53 - the module now has diff support.
- sanity - add future imports in all missing places.
- sns_topic - Add backoff when we get Topic ``NotFound`` exceptions while listing the subscriptions.
- sqs_queue - Add support for tagging, KMS and FIFO queues
- sqs_queue - updated to use boto3 instead of boto

community.crypto
~~~~~~~~~~~~~~~~

- acme_account - add ``external_account_binding`` option to allow creation of ACME accounts with External Account Binding (https://github.com/ansible-collections/community.crypto/issues/89).
- acme_certificate - allow new selector ``test_certificates: first`` for ``select_chain`` parameter (https://github.com/ansible-collections/community.crypto/pull/102).
- cryptography backends - support arbitrary dotted OIDs (https://github.com/ansible-collections/community.crypto/issues/39).
- get_certificate - add support for SNI (https://github.com/ansible-collections/community.crypto/issues/69).
- luks_device - accept ``passphrase``, ``new_passphrase`` and ``remove_passphrase``.
- luks_device - add ``keysize`` parameter to set key size at LUKS container creation
- luks_device - add support for encryption options on container creation (https://github.com/ansible-collections/community.crypto/pull/97).
- luks_device - added support to use UUIDs, and labels with LUKS2 containers
- luks_device - added the ``type`` option that allows user explicit define the LUKS container format version
- openssh_cert - add support for PKCS#11 tokens (https://github.com/ansible-collections/community.crypto/pull/95).
- openssh_keypair - instead of regenerating some broken or password protected keys, fail the module. Keys can still be regenerated by calling the module with ``force=yes``.
- openssh_keypair - the ``regenerate`` option allows to configure the module's behavior when it should or needs to regenerate private keys.
- openssl_* modules - the cryptography backend now properly supports ``dirName``, ``otherName`` and ``RID`` (Registered ID) names.
- openssl_certificate - Add option for changing which ACME directory to use with acme-tiny. Set the default ACME directory to Let's Encrypt instead of using acme-tiny's default. (acme-tiny also uses Let's Encrypt at the time being, so no action should be neccessary.)
- openssl_certificate - Change the required version of acme-tiny to >= 4.0.0
- openssl_certificate - allow to provide content of some input files via the ``csr_content``, ``privatekey_content``, ``ownca_privatekey_content`` and ``ownca_content`` options.
- openssl_certificate - allow to return the existing/generated certificate directly as ``certificate`` by setting ``return_content`` to ``yes``.
- openssl_certificate - the PyOpenSSL backend now uses 160 bits of randomness for serial numbers, instead of a random number between 1000 and 99999. Please note that this is not a high quality random number (https://github.com/ansible-collections/community.crypto/issues/76).
- openssl_certificate_info - allow to provide certificate content via ``content`` option (https://github.com/ansible/ansible/issues/64776).
- openssl_csr - Add support for specifying the SAN ``otherName`` value in the OpenSSL ASN.1 UTF8 string format, ``otherName:<OID>;UTF8:string value``.
- openssl_csr - add support for name constraints extension (https://github.com/ansible-collections/community.crypto/issues/46).
- openssl_csr - allow to provide private key content via ``private_key_content`` option.
- openssl_csr - allow to return the existing/generated CSR directly as ``csr`` by setting ``return_content`` to ``yes``.
- openssl_csr_info - add support for name constraints extension (https://github.com/ansible-collections/community.crypto/issues/46).
- openssl_csr_info - allow to provide CSR content via ``content`` option.
- openssl_dhparam - allow to return the existing/generated DH params directly as ``dhparams`` by setting ``return_content`` to ``yes``.
- openssl_dhparam - now supports a ``cryptography``-based backend. Auto-detection can be overwritten with the ``select_crypto_backend`` option.
- openssl_pkcs12 - allow to return the existing/generated PKCS#12 directly as ``pkcs12`` by setting ``return_content`` to ``yes``.
- openssl_privatekey - add ``format`` and ``format_mismatch`` options.
- openssl_privatekey - allow to return the existing/generated private key directly as ``privatekey`` by setting ``return_content`` to ``yes``.
- openssl_privatekey - the ``regenerate`` option allows to configure the module's behavior when it should or needs to regenerate private keys.
- openssl_privatekey_info - allow to provide private key content via ``content`` option.
- openssl_publickey - allow to provide private key content via ``private_key_content`` option.
- openssl_publickey - allow to return the existing/generated public key directly as ``publickey`` by setting ``return_content`` to ``yes``.

community.general
~~~~~~~~~~~~~~~~~

- A new filter ``to_time_unit`` with specializations ``to_milliseconds``, ``to_seconds``, ``to_minutes``, ``to_hours``, ``to_days``, ``to_weeks``, ``to_months`` and ``to_years`` has been added. For example ``'2d 4h' | community.general.to_hours`` evaluates to 52.
- Add a make option to the make module to be able to choose a specific make executable
- Add information about changed packages in homebrew returned facts (https://github.com/ansible/ansible/issues/59376).
- Add the ``gcpubsub``, ``gcpubsub_info`` and ``gcpubsub_facts`` (to be removed in 3.0.0) modules. These were originally in community.general, but removed on the assumption that they have been moved to google.cloud. Since this turned out to be incorrect, we re-added them for 1.0.0.
- Add the deprecated ``gcp_backend_service``, ``gcp_forwarding_rule`` and ``gcp_healthcheck`` modules, which will be removed in 2.0.0. These were originally in community.general, but removed on the assumption that they have been moved to google.cloud. Since this turned out to be incorrect, we re-added them for 1.0.0.
- Follow up changes in homebrew_cask (https://github.com/ansible/ansible/issues/34696).
- Moved OpenStack dynamic inventory script to Openstack Collection.
- Remove redundant encoding in json.load call in ipa module_utils (https://github.com/ansible/ansible/issues/66592).
- The collection dependencies where adjusted so that ``community.kubernetes`` and ``google.cloud`` are required to be of version 1.0.0 or newer (https://github.com/ansible-collections/community.general/pull/774).
- The collection is now actively tested in CI with the latest Ansible 2.9 release.
- Updated documentation about netstat command requirement for listen_ports_facts module (https://github.com/ansible/ansible/issues/68077).
- airbrake_deployment - Allow passing ``project_id`` and ``project_key`` for v4 api deploy compatibility
- airbrake_deployment - add ``version`` param; clarified docs on ``revision`` param (https://github.com/ansible-collections/community.general/pull/583).
- ali_instance - Add params ``unique_suffix``, ``tags``, ``purge_tags``, ``ram_role_name``, ``spot_price_limit``, ``spot_strategy``, ``period_unit``, ``dry_run``, ``include_data_disks``
- ali_instance and ali_instance_info - the required package footmark needs a version higher than 1.19.0
- ali_instance_info - Add params ``name_prefix``, ``filters``
- alicloud modules - Add authentication params to all modules
- alicloud modules - now only support Python 3.6, not support Python 2.x
- apk - added ``no_cache`` option (https://github.com/ansible-collections/community.general/pull/548).
- cisco_spark - the module has been renamed to ``cisco_webex`` (https://github.com/ansible-collections/community.general/pull/457).
- cloudflare_dns - Report unexpected failure with more detail (https://github.com/ansible-collections/community.general/pull/511).
- database - add support to unique indexes in postgresql_idx
- digital_ocean_droplet - add support for new vpc_uuid parameter
- docker connection plugin - run Powershell modules on Windows containers.
- docker_container - add ``cpus`` option (https://github.com/ansible/ansible/issues/34320).
- docker_container - add new ``container_default_behavior`` option (PR https://github.com/ansible/ansible/pull/63419).
- docker_container - allow to configure timeout when the module waits for a container's removal.
- docker_container - only passes anonymous volumes to docker daemon as ``Volumes``. This increases compatibility with the ``docker`` CLI program. Note that if you specify ``volumes: strict`` in ``comparisons``, this could cause existing containers created with docker_container from Ansible 2.9 or earlier to restart.
- docker_container - support for port ranges was adjusted to be more compatible to the ``docker`` command line utility: a one-port container range combined with a multiple-port host range will no longer result in only the first host port be used, but the whole range being passed to Docker so that a free port in that range will be used.
- docker_container.py - update a containers restart_policy without restarting the container (https://github.com/ansible/ansible/issues/65993)
- docker_stack - Added ``stdout``, ``stderr``, and ``rc`` to return values.
- docker_swarm_service - Added support for ``init`` option.
- docker_swarm_service - Sort lists when checking for changes.
- firewalld - new feature, can now set ``target`` for a ``zone`` (https://github.com/ansible-collections/community.general/pull/526).
- firewalld - the module has been moved to the ``ansible.posix`` collection. A redirection is active, which will be removed in version 2.0.0 (https://github.com/ansible-collections/community.general/pull/623).
- flatpak and flatpak_remote - use ``module.run_command()`` instead of ``subprocess.Popen()``.
- gitlab_project - add support for merge_method on projects (https://github.com/ansible/ansible/pull/66813).
- gitlab_project_variable - implement masked and protected attributes
- gitlab_project_variable - implemented variable_type attribute.
- gitlab_runners inventory plugin - permit environment variable input for ``server_url``, ``api_token`` and ``filter`` options (https://github.com/ansible-collections/community.general/pull/611).
- haproxy - add options to dis/enable health and agent checks.  When health and agent checks are enabled for a service, a disabled service will re-enable itself automatically.  These options also change the state of the agent checks to match the requested state for the backend (https://github.com/ansible-collections/community.general/issues/684).
- hashi_vault - AWS IAM auth method added. Accepts standard ansible AWS params and only loads AWS libraries when needed.
- hashi_vault - INI and additional ENV sources made available for some new and old options.
- hashi_vault - ``secret`` can now be an unnamed argument if it's specified first in the term string (see examples).
- hashi_vault - ``token`` is now an explicit option (and the default) in the choices for ``auth_method``. This matches previous behavior (``auth_method`` omitted resulted in token auth) but makes the value clearer and allows it to be explicitly specified.
- hashi_vault - new option ``return_format`` added to control how secrets are returned, including options for multiple secrets and returning raw values with metadata.
- hashi_vault - previous (undocumented) behavior was to attempt to read token from ``~/.vault-token`` if not specified. This is now controlled through ``token_path`` and ``token_file`` options (defaults will mimic previous behavior).
- hashi_vault - previously all options had to be supplied via key=value pairs in the term string; now a mix of string and parameters can be specified (see examples).
- hashi_vault - uses newer authentication calls in the HVAC library and falls back to older ones with deprecation warnings.
- homebrew - Added environment variable to honor update_homebrew setting (https://github.com/ansible/ansible/issues/56650).
- homebrew - New option ``upgrade_options`` allows to pass flags to upgrade
- homebrew - ``install_options`` is now validated to be a list of strings.
- homebrew_tap - ``name`` is now validated to be a list of strings.
- idrac_redfish_config - Support for multiple manager attributes configuration
- java_keystore - add the private_key_passphrase parameter (https://github.com/ansible-collections/community.general/pull/276).
- jc - new filter to convert the output of many shell commands and file-types to JSON. Uses the jc library at https://github.com/kellyjonbrazil/jc. For example, filtering the STDOUT output of ``uname -a`` via ``{{ result.stdout | community.general.jc('uname') }}``. Requires Python 3.6+ (https://github.com/ansible-collections/community.general/pull/750).
- jira - added search function with support for Jira JQL (https://github.com/ansible-collections/community.general/pull/22).
- jira - added update function which can update Jira Selects etc (https://github.com/ansible-collections/community.general/pull/22).
- log_plays callback - use v2 methods (https://github.com/ansible-collections/community.general/pull/442).
- logstash callback - add ini config (https://github.com/ansible-collections/community.general/pull/610).
- lvg - add ``pvresize`` new parameter (https://github.com/ansible/ansible/issues/29139).
- lxd_container - added support of ``--target`` flag for cluster deployments (https://github.com/ansible-collections/community.general/issues/637).
- mysql_db - add ``master_data`` parameter (https://github.com/ansible/ansible/pull/66048).
- mysql_db - add ``skip_lock_tables`` option (https://github.com/ansible/ansible/pull/66688).
- mysql_db - add the ``check_implicit_admin`` parameter (https://github.com/ansible/ansible/issues/24418).
- mysql_db - add the ``config_overrides_defaults`` parameter (https://github.com/ansible/ansible/issues/26919).
- mysql_db - add the ``dump_extra_args`` parameter (https://github.com/ansible/ansible/pull/67747).
- mysql_db - add the ``executed_commands`` returned value (https://github.com/ansible/ansible/pull/65498).
- mysql_db - add the ``force`` parameter (https://github.com/ansible/ansible/pull/65547).
- mysql_db - add the ``restrict_config_file`` parameter (https://github.com/ansible/ansible/issues/34488).
- mysql_db - add the ``unsafe_login_password`` parameter (https://github.com/ansible/ansible/issues/63955).
- mysql_db - add the ``use_shell`` parameter (https://github.com/ansible/ansible/issues/20196).
- mysql_info - add ``exclude_fields`` parameter (https://github.com/ansible/ansible/issues/63319).
- mysql_info - add ``global_status`` filter parameter option and return (https://github.com/ansible/ansible/pull/63189).
- mysql_info - add ``return_empty_dbs`` parameter to list empty databases (https://github.com/ansible/ansible/issues/65727).
- mysql_replication - add ``channel`` parameter (https://github.com/ansible/ansible/issues/29311).
- mysql_replication - add ``connection_name`` parameter (https://github.com/ansible/ansible/issues/46243).
- mysql_replication - add ``fail_on_error`` parameter (https://github.com/ansible/ansible/pull/66252).
- mysql_replication - add ``master_delay`` parameter (https://github.com/ansible/ansible/issues/51326).
- mysql_replication - add ``master_use_gtid`` parameter (https://github.com/ansible/ansible/pull/62648).
- mysql_replication - add ``queries`` return value (https://github.com/ansible/ansible/pull/63036).
- mysql_replication - add support of ``resetmaster`` choice to ``mode`` parameter (https://github.com/ansible/ansible/issues/42870).
- mysql_user - ``priv`` parameter can be string or dictionary (https://github.com/ansible/ansible/issues/57533).
- mysql_user - add ``plugin_auth_string`` parameter (https://github.com/ansible/ansible/pull/44267).
- mysql_user - add ``plugin_hash_string`` parameter (https://github.com/ansible/ansible/pull/44267).
- mysql_user - add ``plugin`` parameter (https://github.com/ansible/ansible/pull/44267).
- mysql_user - add the resource_limits parameter (https://github.com/ansible-collections/community.general/issues/133).
- mysql_variables - add ``mode`` parameter (https://github.com/ansible/ansible/issues/60119).
- nagios module - a start parameter has been added, allowing the time a Nagios outage starts to be set. It defaults to the current time if not provided, preserving the previous behavior and ensuring compatibility with existing playbooks.
- nsupdate - Use provided TSIG key to not only sign update queries but also lookup queries
- open_iscsi - allow ``portal`` parameter to be a domain name by resolving the portal ip address beforehand (https://github.com/ansible-collections/community.general/pull/461).
- packet_device - add ``tags`` parameter on device creation (https://github.com/ansible-collections/community.general/pull/418)
- pacman - Improve package state detection speed: Don't query for full details of a package.
- parted - accept negative numbers in ``part_start`` and ``part_end``
- parted - add the ``fs_type`` parameter (https://github.com/ansible-collections/community.general/issues/135).
- pear - added ``prompts`` parameter to allow users to specify expected prompt that could hang Ansible execution (https://github.com/ansible-collections/community.general/pull/530).
- pkgng - added ``stdout`` and ``stderr`` attributes to the result (https://github.com/ansible-collections/community.general/pull/560).
- pkgng - added support for upgrading all packages using ``name: *, state: latest``, similar to other package providers (https://github.com/ansible-collections/community.general/pull/569).
- postgresql_copy - add the ``trust_input`` parameter (https://github.com/ansible-collections/community.general/pull/313).
- postgresql_db - add ``dump_extra_args`` parameter (https://github.com/ansible/ansible/pull/66717).
- postgresql_db - add support for .pgc file format for dump and restores.
- postgresql_db - add the ``executed_commands`` returned value (https://github.com/ansible/ansible/pull/65542).
- postgresql_db - add the ``trust_input`` parameter (https://github.com/ansible-collections/community.general/issues/106).
- postgresql_ext - add the ``trust_input`` parameter (https://github.com/ansible-collections/community.general/pull/282).
- postgresql_ext - refactor to simplify and remove dead code (https://github.com/ansible-collections/community.general/pull/291)
- postgresql_ext - use query parameters with cursor object (https://github.com/ansible/ansible/pull/64994).
- postgresql_idx - add the ``trust_input`` parameter (https://github.com/ansible-collections/community.general/pull/264).
- postgresql_idx - refactor to simplify code (https://github.com/ansible-collections/community.general/pull/291)
- postgresql_info - add collecting info about logical replication publications in databases (https://github.com/ansible/ansible/pull/67614).
- postgresql_info - add collection info about replication subscriptions (https://github.com/ansible/ansible/pull/67464).
- postgresql_info - add the ``trust_input`` parameter (https://github.com/ansible-collections/community.general/pull/308).
- postgresql_lang - add ``owner`` parameter (https://github.com/ansible/ansible/pull/62999).
- postgresql_lang - add the ``trust_input`` parameter (https://github.com/ansible-collections/community.general/pull/272).
- postgresql_membership - add the ``trust_input`` parameter (https://github.com/ansible-collections/community.general/pull/158).
- postgresql_owner - add the ``trust_input`` parameter (https://github.com/ansible-collections/community.general/pull/198).
- postgresql_ping - add the ``session_role`` parameter (https://github.com/ansible-collections/community.general/pull/312).
- postgresql_ping - add the ``trust_input`` parameter (https://github.com/ansible-collections/community.general/pull/312).
- postgresql_privs - add support for TYPE as object types in postgresql_privs module (https://github.com/ansible/ansible/issues/62432).
- postgresql_privs - add the ``trust_input`` parameter (https://github.com/ansible-collections/community.general/pull/177).
- postgresql_publication - add the ``session_role`` parameter (https://github.com/ansible-collections/community.general/pull/279).
- postgresql_publication - add the ``trust_input`` parameter (https://github.com/ansible-collections/community.general/pull/279).
- postgresql_query - add search_path parameter (https://github.com/ansible-collections/community.general/issues/625).
- postgresql_query - add the ``encoding`` parameter (https://github.com/ansible/ansible/issues/65367).
- postgresql_query - add the ``trust_input`` parameter (https://github.com/ansible-collections/community.general/pull/294).
- postgresql_schema - add the ``trust_input`` parameter (https://github.com/ansible-collections/community.general/pull/259).
- postgresql_sequence - add the ``trust_input`` parameter (https://github.com/ansible-collections/community.general/pull/295).
- postgresql_set - add the ``trust_input`` parameter (https://github.com/ansible-collections/community.general/pull/302).
- postgresql_slot - add the ``trust_input`` parameter (https://github.com/ansible-collections/community.general/pull/298).
- postgresql_subscription - add the ``session_role`` parameter (https://github.com/ansible-collections/community.general/pull/280).
- postgresql_subscription - add the ``trust_input`` parameter (https://github.com/ansible-collections/community.general/pull/280).
- postgresql_table - add the ``trust_input`` parameter (https://github.com/ansible-collections/community.general/pull/307).
- postgresql_tablespace - add the ``trust_input`` parameter (https://github.com/ansible-collections/community.general/pull/240).
- postgresql_user - add scram-sha-256 support (https://github.com/ansible/ansible/issues/49878).
- postgresql_user - add the ``trust_input`` parameter (https://github.com/ansible-collections/community.general/pull/116).
- postgresql_user - add the comment parameter (https://github.com/ansible/ansible/pull/66711).
- postgresql_user_obj_stat_info - add the ``trust_input`` parameter (https://github.com/ansible-collections/community.general/pull/310).
- postgresql_user_obj_stat_info - refactor to simplify code (https://github.com/ansible-collections/community.general/pull/291)
- proxmox - add the ``description`` and ``hookscript`` parameter (https://github.com/ansible-collections/community.general/pull/245).
- redfish_command - Support for virtual media insert and eject commands (https://github.com/ansible-collections/community.general/issues/493)
- redfish_config - New ``bios_attributes`` option to allow setting multiple BIOS attributes in one command.
- redfish_config, redfish_command - Add ``resource_id`` option to specify which System, Manager, or Chassis resource to modify.
- redis - add TLS support to redis cache plugin (https://github.com/ansible-collections/community.general/pull/410).
- rhn_channel - Added ``validate_certs`` option (https://github.com/ansible/ansible/issues/68374).
- rundeck modules - added new options ``client_cert``, ``client_key``, ``force``, ``force_basic_auth``, ``http_agent``, ``url_password``, ``url_username``, ``use_proxy``, ``validate_certs`` to allow changing fetch_url parameters.
- rundeck_acl_policy - add check for rundeck_acl_policy name parameter (https://github.com/ansible-collections/community.general/pull/612).
- slack - Add support for user/bot/application tokens (using Slack WebAPI)
- slack - Return ``thread_id`` with thread timestamp when user/bot/application tokens are used
- slack - add support for sending messages built with block kit (https://github.com/ansible-collections/community.general/issues/380).
- splunk callback - add an option to allow not to validate certificate from HEC (https://github.com/ansible-collections/community.general/pull/596).
- syslogger - added new parameter ident to specify the name of application which is sending the message to syslog (https://github.com/ansible-collections/community.general/issues/319).
- terraform - Adds option ``backend_config_files``. This can accept a list of paths to multiple configuration files (https://github.com/ansible-collections/community.general/pull/394).
- terraform - Adds option ``variables_files`` for multiple var-files (https://github.com/ansible-collections/community.general/issues/224).
- ufw - accept ``interface_in`` and ``interface_out`` as parameters.
- xfconf - add arrays support (https://github.com/ansible/ansible/issues/46308).
- xfconf - add support for ``double`` type (https://github.com/ansible-collections/community.general/pull/744).
- xfconf - add support for ``uint`` type (https://github.com/ansible-collections/community.general/pull/696).
- zypper - Added ``allow_vendor_change`` and ``replacefiles`` zypper options (https://github.com/ansible-collections/community.general/issues/381)

community.grafana
~~~~~~~~~~~~~~~~~

- Add Thruk as Grafana Datasource
- Add `grafana_folder` module
- Add `grafana_user` module
- Use `module_utils` to allow code factorization

community.kubernetes
~~~~~~~~~~~~~~~~~~~~

- Add action groups for playbooks with module_defaults (https://github.com/ansible-collections/community.kubernetes/pull/107).
- Add requires_ansible version constraints to runtime.yml (https://github.com/ansible-collections/community.kubernetes/pull/126).
- Add sanity test ignore file for Ansible 2.11 (https://github.com/ansible-collections/community.kubernetes/pull/130).
- Add test for openshift apply bug (https://github.com/ansible-collections/community.kubernetes/pull/94).
- Add version_added to each new collection module (https://github.com/ansible-collections/community.kubernetes/pull/98).
- Check Python code using flake8 (https://github.com/ansible-collections/community.kubernetes/pull/123).
- Don't require project coverage check on PRs (https://github.com/ansible-collections/community.kubernetes/pull/102).
- Ensure check mode results are as expected (https://github.com/ansible-collections/community.kubernetes/pull/155).
- Improve k8s Deployment and Daemonset wait conditions (https://github.com/ansible-collections/community.kubernetes/pull/35).
- Minor documentation fixes and use of FQCN in some examples (https://github.com/ansible-collections/community.kubernetes/pull/114).
- Remove action_groups_redirection entry from meta/runtime.yml (https://github.com/ansible-collections/community.kubernetes/pull/127).
- Remove deprecated ANSIBLE_METADATA field (https://github.com/ansible-collections/community.kubernetes/pull/95).
- Rename repository to ``community.kubernetes`` (https://github.com/ansible-collections/community.kubernetes/pull/81).
- Update base branch to 'main' (https://github.com/ansible-collections/community.kubernetes/issues/148).
- Use FQCN in module docs and plugin examples (https://github.com/ansible-collections/community.kubernetes/pull/146).
- Use improved kubernetes diffs where possible (https://github.com/ansible-collections/community.kubernetes/pull/105).
- helm - Add support for K8S_AUTH_CONTEXT, K8S_AUTH_KUBECONFIG env (https://github.com/ansible-collections/community.kubernetes/pull/141).
- helm - Allow creating namespaces with Helm (https://github.com/ansible-collections/community.kubernetes/pull/157).
- helm - add 'atomic' option (https://github.com/ansible-collections/community.kubernetes/pull/115).
- helm - add aliases context for kube_context (https://github.com/ansible-collections/community.kubernetes/pull/152).
- helm - add support for K8S_AUTH_KUBECONFIG and K8S_AUTH_CONTEXT environment variable (https://github.com/ansible-collections/community.kubernetes/issues/140).
- helm - minor code refactoring (https://github.com/ansible-collections/community.kubernetes/pull/110).
- helm_info - add aliases context for kube_context (https://github.com/ansible-collections/community.kubernetes/pull/152).
- helm_info - add support for K8S_AUTH_KUBECONFIG and K8S_AUTH_CONTEXT environment variable (https://github.com/ansible-collections/community.kubernetes/issues/140).
- helm_info and helm_repository - minor code refactor (https://github.com/ansible-collections/community.kubernetes/pull/117).
- k8s - Added ``persist_config`` option for persisting refreshed tokens (https://github.com/ansible-collections/community.kubernetes/issues/49).
- k8s - Handle set object retrieved from lookup plugin (https://github.com/ansible-collections/community.kubernetes/pull/118).
- k8s_exec - return RC for the command executed (https://github.com/ansible-collections/community.kubernetes/issues/122).
- k8s_info - Update example using vars (https://github.com/ansible-collections/community.kubernetes/pull/156).

community.mysql
~~~~~~~~~~~~~~~

- mysql_db - add ``master_data`` parameter (https://github.com/ansible/ansible/pull/66048).
- mysql_db - add ``skip_lock_tables`` option (https://github.com/ansible/ansible/pull/66688).
- mysql_db - add the ``check_implicit_admin`` parameter (https://github.com/ansible/ansible/issues/24418).
- mysql_db - add the ``dump_extra_args`` parameter (https://github.com/ansible/ansible/pull/67747).
- mysql_db - add the ``executed_commands`` returned value (https://github.com/ansible/ansible/pull/65498).
- mysql_db - add the ``force`` parameter (https://github.com/ansible/ansible/pull/65547).
- mysql_db - add the ``restrict_config_file`` parameter (https://github.com/ansible/ansible/issues/34488).
- mysql_db - add the ``unsafe_login_password`` parameter (https://github.com/ansible/ansible/issues/63955).
- mysql_db - add the ``use_shell`` parameter (https://github.com/ansible/ansible/issues/20196).
- mysql_info - add ``exclude_fields`` parameter (https://github.com/ansible/ansible/issues/63319).
- mysql_info - add ``global_status`` filter parameter option and return (https://github.com/ansible/ansible/pull/63189).
- mysql_info - add ``return_empty_dbs`` parameter to list empty databases (https://github.com/ansible/ansible/issues/65727).
- mysql_replication - add ``channel`` parameter (https://github.com/ansible/ansible/issues/29311).
- mysql_replication - add ``connection_name`` parameter (https://github.com/ansible/ansible/issues/46243).
- mysql_replication - add ``fail_on_error`` parameter (https://github.com/ansible/ansible/pull/66252).
- mysql_replication - add ``master_delay`` parameter (https://github.com/ansible/ansible/issues/51326).
- mysql_replication - add ``master_use_gtid`` parameter (https://github.com/ansible/ansible/pull/62648).
- mysql_replication - add ``queries`` return value (https://github.com/ansible/ansible/pull/63036).
- mysql_replication - add support of ``resetmaster`` choice to ``mode`` parameter (https://github.com/ansible/ansible/issues/42870).
- mysql_user - ``priv`` parameter can be string or dictionary (https://github.com/ansible/ansible/issues/57533).
- mysql_user - add TLS REQUIRES parameters (https://github.com/ansible-collections/community.mysql/pull/9).
- mysql_user - add ``plugin_auth_string`` parameter (https://github.com/ansible/ansible/pull/44267).
- mysql_user - add ``plugin_hash_string`` parameter (https://github.com/ansible/ansible/pull/44267).
- mysql_user - add ``plugin`` parameter (https://github.com/ansible/ansible/pull/44267).
- mysql_user - add the resource_limits parameter (https://github.com/ansible-collections/community.general/issues/133).
- mysql_variables - add ``mode`` parameter (https://github.com/ansible/ansible/issues/60119).

community.network
~~~~~~~~~~~~~~~~~

- ce_bgp_neighbor_af - Rename the parameter ``redirect_ip_vaildation`` to ``redirect_ip_validation`` (https://github.com/ansible/ansible/pull/62403).
- cnos terminal plugin - prevent timeout connection failure by adding "no logging terminal" after log in (https://github.com/ansible-collections/community.network/pull/16).

community.rabbitmq
~~~~~~~~~~~~~~~~~~

- rabbitmq_publish - Support for connecting with SSL certificates.

community.vmware
~~~~~~~~~~~~~~~~

- A `vmware` module_defaults group has been added to simplify parameters for multiple VMware tasks. This group includes all VMware modules.
- Add a flag 'force_upgrade' to force VMware tools upgrade installation (https://github.com/ansible-collections/vmware/issues/75).
- Add powerstates to match vmware_guest_powerstate module with vmware_guest (https://github.com/ansible/ansible/issues/55653).
- Added a timeout parameter `wait_for_ip_address_timeout` for `wait_for_ip_address` for longer-running tasks in vmware_guest.
- Added missing backing_disk_mode information about disk which was removed by mistake in vmware_guest_disk_info.
- Added module to be able to create, update, or delete VMware VM storage policies for virtual machines.
- Correct datatype for state in vmware_host_lockdown module.
- Correct example from doc of `vmware_local_role_info.py` to match the change of returned structure.
- Correct example from doc of `vmware_local_role_info.py` to match the change of returned structure.
- Handle exceptions raised in connect_to_vsphere_client API.
- Minor typo fixes in vmware_httpapi related modules and module_utils.
- Removed ANSIBLE_METADATA from all the modules.
- Return additional information about hosts inside the cluster using vmware_cluster_info.
- Update Module examples with FQCN.
- Update README.md for installing any third party required Python libraries using pip (https://github.com/ansible-collections/vmware/issues/154).
- add storage_provisioning type into vmware_content_deploy_ovf_template.
- add vmware_content_deploy_ovf_template module for creating VMs from OVF templates
- new code module for new feature for operations of VCenter infra profile config.
- vmware.py - Only add configured network interfaces to facts.
- vmware_cluster_drs - Implemented DRS advanced settings (https://github.com/ansible/ansible/issues/66217)
- vmware_cluster_ha - Implemented HA advanced settings (https://github.com/ansible/ansible/issues/61421)
- vmware_cluster_ha - Remove a wrong parameter from an example in the documentation.
- vmware_cluster_ha - treat truthy advanced options ('true', 'false') as strings instead of booleans (https://github.com/ansible-collections/vmware/issues/286).
- vmware_cluster_info - added ``properties`` and ``schema`` options and supported the getting of clusters resource summary information.
- vmware_cluster_vsan - implement advanced VSAN options (https://github.com/ansible-collections/vmware/issues/260).
- vmware_cluster_vsan - requires the vSAN Management SDK, which needs to be downloaded from VMware and installed manually.
- vmware_content_deploy_ovf_template - handle exception while deploying VM using OVF template.
- vmware_content_deploy_ovf_template - requires the resource_pool parameter.
- vmware_content_deploy_template - added new field "content_library" to search template inside the specified content library.
- vmware_content_deploy_template - handle exception while deploying VM (https://github.com/ansible-collections/vmware/issues/182).
- vmware_datastore_cluster - Added basic SDRS configuration (https://github.com/ansible/ansible/issues/65154).
- vmware_datastore_info - added ``properties`` and ``schema`` options.
- vmware_datastore_maintenancemode now returns datastore_status instead of Ansible internal key results (https://github.com/ansible/ansible/issues/62083).
- vmware_dvs_portgroup - Added support for distributed port group with private VLAN.
- vmware_dvs_portgroup_info - Include the value of the Portgroup ``key`` in the result
- vmware_dvswitch now returns the UUID of the switch
- vmware_dvswitch_info also returns the switch UUID
- vmware_export_ovf - increase default timeout to 30s
- vmware_export_ovf - timeout value is actually in seconds, not minutes
- vmware_guest - Don't search for VMDK if filename is defined.
- vmware_guest - Extracts repeated code from configure_vapp_properties() to set_vapp_properties() in vmware_guest.py.
- vmware_guest - add support VM creation and reconfiguration with multiple types of disk controllers and disks
- vmware_guest - add support for create and reconfigure CDROMs attaching to SATA (https://github.com/ansible/ansible/issues/42995)
- vmware_guest - add support hardware version 17 for vSphere 7.0
- vmware_guest_custom_attributes does not require VM name (https://github.com/ansible/ansible/issues/63222).
- vmware_guest_disk - Add `destroy` option which allows to remove a disk without deleting the VMDK file.
- vmware_guest_disk - Add `filename` option which allows to create a disk from an existing VMDK.
- vmware_guest_disk - add backing_uuid value to return (https://github.com/ansible-collections/vmware/pull/348).
- vmware_guest_disk - add support for setting the sharing/multi-writer mode of virtual disks (https://github.com/ansible-collections/vmware/issues/212)
- vmware_guest_network - network adapters can be configured without lists
- vmware_guest_network - network_info returns a list of dictionaries for ease of use
- vmware_guest_network - put deprecation warning for the networks parameter
- vmware_guest_serial_port - ensure we can run the module two times in a row without unexpected side effect(https://github.com/ansible-collections/vmware/pull/358).
- vmware_guest_snapshot_info - Document that `folder` is required if the VM `name` is defined (https://github.com/ansible-collections/vmware/issues/243)
- vmware_guest_tools_wait now exposes a ``timeout`` parameter that allow the user to adjust the timeout (second).
- vmware_host_active_directory - Fail when there are unrecoverable problems with AD membership instead of reporting a change that doesn't take place (https://github.com/ansible-collections/vmware/issues/59).
- vmware_host_dns - New module replacing vmware_dns_config with increased functionality.
- vmware_host_dns can now set the following empty values, ``domain``, ``search_domains`` and ``dns_servers``.
- vmware_host_facts - added ``properties`` and ``schema`` options.
- vmware_host_firewall_manager - ``allowed_hosts`` excpects a dict as parameter, list is deprecated
- vmware_host_iscsi - a new module for the ESXi hosts that is dedicated to the management of the iSCSI configuration
- vmware_host_kernel_manager now returns host_kernel_status instead of Ansible internal key results (https://github.com/ansible/ansible/issues/62083).
- vmware_host_logbundle - new code module for a new feature for ESXi support log bundle download operation
- vmware_host_logbundle_info - new code module for a new feature for getting manifests  for ESXi support log bundle
- vmware_host_ntp now returns host_ntp_status instead of Ansible internal key results (https://github.com/ansible/ansible/issues/62083).
- vmware_host_service_manager now returns host_service_status instead of Ansible internal key results (https://github.com/ansible/ansible/issues/62083).
- vmware_migrate_vmk - allow migration from a VMware vSphere Distrubuted Switch to a ESXi Standard Switch
- vmware_rest_client - Added a new definition get_library_item_from_content_library_name.
- vmware_tag now returns tag_status instead of Ansible internal key results (https://github.com/ansible/ansible/issues/62083).
- vmware_vcenter_settings_info - a new module for gather information about vCenter settings
- vmware_vm_inventory inventory plugin, raise more descriptive error when all template strings in ``hostnames`` fail.

community.windows
~~~~~~~~~~~~~~~~~

- win_disk_facts - Set output array order to be by disk number property - https://github.com/ansible/ansible/issues/63998
- win_dns_record - Added support for managing ``SRV`` records
- win_domain_computer - ``sam_account_name`` with missing ``$`` will have it added automatically (https://github.com/ansible-collections/community.windows/pull/93)
- win_domain_computer - add support for offline domain join (https://github.com/ansible-collections/community.windows/pull/93)
- win_domain_group_membership - Add multi-domain forest support - https://github.com/ansible/ansible/issues/59829
- win_domain_user - Added the ``identity`` module option to explicitly set the identity of the user when searching for it - https://github.com/ansible/ansible/issues/45298
- win_firewall- Change req check from wmf version to cmdlets presence - https://github.com/ansible/ansible/issues/63003
- win_firewall_rule - Support editing rules by the group it belongs to
- win_firewall_rule - Support editing rules that have a duplicated name
- win_firewall_rule - add parameter to support ICMP Types and Codes (https://github.com/ansible/ansible/issues/46809)
- win_iis_webapplication - add new options ``connect_as``, ``username``, ``password``.
- win_iis_webapplication - now uses the current application pool of the website instead of the DefaultAppPool if none was specified.
- win_nssm - Implement additional parameters - (https://github.com/ansible/ansible/issues/62620)
- win_pester - Only execute ``*.tests.ps1`` in ``path`` to match the default behaviour in Pester - https://github.com/ansible/ansible/issues/55736

community.zabbix
~~~~~~~~~~~~~~~~

- Added the possibility to configure the ``mode`` for the ``zabbix_{agent,server,proxy}_include`` directories.
- All roles now **support Zabbix 5.0** and by default install this version (see `#131 <https://github.com/ansible-collections/community.zabbix/pull/131>`_ and `#121 <https://github.com/ansible-collections/community.zabbix/pull/121>`_).
- Documentation for roles moved to ``docs/`` sub-directory in the collection.
- New **role zabbix_agent** - previously known as dj-wasabi/zabbix-agent (also see `UPGRADE.md <https://github.com/ansible-collections/community.zabbix/blob/main/docs/UPGRADE.md>`_ for each role).
- New **role zabbix_javagateway** - previously known as dj-wasabi/zabbix-javagateway.
- New **role zabbix_proxy** - previously known as dj-wasabi/zabbix-proxy.
- New **role zabbix_server** - previously known as dj-wasabi/zabbix-server.
- New **role zabbix_web** - previously known as dj-wasabi/zabbix-web.
- Roles will now install gnupg on Debian OS family if not present.
- all roles - added the possibility to configure the ``mode`` for the ``yum`` repositories files in case it contains credentials.
- zabbix_action - arguments ``event_source`` and ``esc_period`` no longer required when ``state=absent``.
- zabbix_action - new alias ``update_operations`` for ``acknowledge_operations`` parameter.
- zabbix_action - no longer requires ``password`` and ``ssh_*key_file`` parameters at the same time for ``remote_command`` operations of type SSH.
- zabbix_action - parameter ``ssh_auth_type`` for SSH ``remote_command`` operation now correctly identifies which other parameters are required.
- zabbix_agent - ``zabbix-sender`` and ``zabbix-get`` will not be installed when ``zabbix_repo`` is set to ``epel``, as they are not part of the repository.
- zabbix_agent - added option to change between HTTP/HTTPS with ``zabbix_repo_yum_schema``.
- zabbix_agent - can also install the zabbix-agent2 application when ``zabbix_agent2`` is set to ``true``.
- zabbix_discovery_rule - refactoring module to use ``module_utils`` classes and functions, adjust return values on success, add documentation for return values.
- zabbix_discovery_rule - refactoring the module to remove unnecessary variables and fix a variable typo.
- zabbix_host - ``macros`` now support new macro types ``text`` and ``secret``.
- zabbix_host - fixed inventory_mode key error, which occurs with Zabbix 4.4.1 or more (see `#65304 <https://github.com/ansible/ansible/issues/65304>`_).
- zabbix_host - new option ``details`` (additional SNMP details) for ``interfaces`` parameter.
- zabbix_host - now supports Zabbix 5.0.
- zabbix_host - was not possible to update a host where visible_name was not set in zabbix.
- zabbix_mediatype - Fixed to support zabbix 4.4 or more and python3 (see `#67693 <https://github.com/ansible/ansible/pull/67693>`_).
- zabbix_mediatype - new options ``message_templates``, ``description`` and many more related to ``type=webhook``.
- zabbix_mediatype - now supports new ``webhook`` media type.
- zabbix_proxy (module) - now supports Zabbix 5.0.
- zabbix_proxy (role) - a user and group are created on the host when ``zabbix_repo`` is set to ``epel``.
- zabbix_proxy (role) - now supports ``startpreprocessors`` setting and encryption when connecting to database (see `#164 <https://github.com/ansible-collections/community.zabbix/pull/164>`_).
- zabbix_screen - ``host_group`` parameter now accepts multiple groups.
- zabbix_server - a user and group are created on the host when ``zabbix_repo`` is set to ``epel``.
- zabbix_server - added option to change between HTTP/HTTPS with ``zabbix_repo_yum_schema``.
- zabbix_server - now supports ``startpreprocessors`` setting and encryption when connecting to database (see `#164 <https://github.com/ansible-collections/community.zabbix/pull/164>`_).
- zabbix_template - fixed error when providing empty ``link_templates`` to the module (see `#66417 <https://github.com/ansible/ansible/issues/66417>`_).
- zabbix_template - fixed invalid (non-importable) output provided by exporting XML (see `#66466 <https://github.com/ansible/ansible/issues/66466>`_).
- zabbix_user - Fixed an issue where module failed with zabbix 4.4 or above (see `#67475 <https://github.com/ansible/ansible/pull/67475>`_).
- zabbix_web - a property is added ``zabbix_web_doubleprecision`` which currently is set to ``false`` for default installations. For new installations this should be set to ``True``. For upgraded installations, please read database `upgrade notes <https://www.zabbix.com/documentation/current/manual/installation/upgrade_notes_500>`_ (Paragraph "Enabling extended range of numeric (float) values") before enabling this option.
- zabbix_web - added option to change between HTTP/HTTPS with ``zabbix_repo_yum_schema``.
- zabbix_web - don't remove the files that Zabbix will install during installation when you don't want to configure a virtual host configuration.

containers.podman
~~~~~~~~~~~~~~~~~

- Add changelog file to collection.
- Add pip installation for podman collection.
- Add podman pod and pod info modules
- Create podman_volume module for volumes management
- Relicense under GPLv3 and clean up modules
- buildah_connection - add support of specific user
- buildah_connection - added Buildah connection rootless
- podman_connection - add user flags before container id in podman exec

frr.frr
~~~~~~~

- Regenerated docs, add description to galaxy.yml and linked changelog to README (https://github.com/ansible-collections/frr.frr/pull/28)

hetzner.hcloud
~~~~~~~~~~~~~~

- hcloud_load_balancer Allow changing the type of a Load Balancer
- hcloud_server Allow the creation of servers with enabled backups

junipernetworks.junos
~~~~~~~~~~~~~~~~~~~~~

- Gathered state operation enabled, Parsed and rendered state operations implemented for junos_lacp.
- Gathered state operation enabled, Parsed and rendered state operations implemented for junos_lldp_global.
- Gathered state operation enabled, Parsed and rendered state operations implemented for junos_lldp_interfaces.
- Gathered state operation enabled, Parsed and rendered state operations implemented for ospfv2, acl_interfaces, vlans and static_routes RM.
- Gathered state operation enabled. Parsed and rendered state operations implemented.
- Gathered state operation enabledand Parsed and rendered state operations implemented.

netbox.netbox
~~~~~~~~~~~~~

- Add ``custom_fields`` to ``netbox_virtual_machine`` (https://github.com/netbox-community/ansible_modules/issues/170)
- Add ``device_query_filters`` and ``vm_query_filters`` to allow users to specify query filters for the specific type (https://github.com/netbox-community/ansible_modules/issues/140)
- Add ``local_context_data`` and ``flatten_local_context_data`` option to ``nb_inventory`` (https://github.com/netbox-community/ansible_modules/pull/258)
- Add ``local_context_data`` option to ``netbox_device`` (https://github.com/netbox-community/ansible_modules/pull/258)
- Add ``primary_ip4/6`` to ``netbox_ip_address`` (https://github.com/netbox-community/ansible_modules/issues/10)
- Add ``virtual_chassis``, ``vc_position``, ``vc_priority`` to ``netbox_device`` options (https://github.com/netbox-community/ansible_modules/pull/251)
- Add dns_name to netbox_ip_address (https://github.com/netbox-community/ansible_modules/issues/84)
- Add region and region_id to query_filter for Netbox Inventory plugin (https://github.com/netbox-community/ansible_modules/issues/83)
- Added 21" width to netbox_rack (https://github.com/netbox-community/ansible_modules/pull/190)
- Added ``group_names_raw`` option to the netbox inventory to allow users have the group names be the slug rather than prepending the group name with the type (https://github.com/netbox-community/ansible_modules/issues/138)
- Added ``raw_output`` option to netbox lookup plugin to return the exact output from the API with no doctoring (https://github.com/netbox-community/ansible_modules/pull/136)
- Added ``services`` option to the netbox inventory to allow users to toggle whether services are included or not (https://github.com/netbox-community/ansible_modules/pull/143)
- Added ``update_vc_child`` option to netbox_device_interface to allow child interfaces to be updated if device specified is the master device within the virtual chassis (https://github.com/netbox-community/ansible_modules/issues/105)
- Added cluster, cluster_type, and cluster_group to group_by option in inventory plugin (https://github.com/netbox-community/ansible_modules/issues/188)
- Added fetching services for devices in Netbox Inventory Plugin (https://github.com/netbox-community/ansible_modules/issues/58)
- Added option for interfaces and IP addresses of interfaces to be fetched via inventory plugin (https://github.com/netbox-community/ansible_modules/issues/60)
- Added option to change host_vars to singular rather than having single element lists (https://github.com/netbox-community/ansible_modules/issues/141)
- Added option to flatten ``config_context`` and ``custom_fields`` (https://github.com/netbox-community/ansible_modules/issues/193)
- Adds ``discovered`` field to ``netbox_inventory_item`` (https://github.com/netbox-community/ansible_modules/issues/187)
- Adds ``query_params`` to all modules to allow users to define the ``query_params`` (https://github.com/netbox-community/ansible_modules/issues/215)
- Adds ``tenant`` field to ``netbox_cluster`` (https://github.com/netbox-community/ansible_modules/pull/219)
- Allows private key to be passed in to ``validate_certs`` within modules (https://github.com/netbox-community/ansible_modules/issues/216)
- Better error handling if read-only token is provided for modules. Updated README as well to say that a ``write-enabled`` token is required (https://github.com/netbox-community/ansible_modules/pull/238)
- Change lookups to property for subclassing of inventory plugin (https://github.com/netbox-community/ansible_modules/issues/62)
- Changed ``validate_certs`` to ``raw`` to allow private keys to be passed in (https://github.com/netbox-community/ansible_modules/issues/211)
- Inventory - Add group_by option ``rack_role`` and ``rack_group``
- Inventory - Add group_by option ``services`` (https://github.com/netbox-community/ansible_modules/pull/286)
- Remove token from being required for nb_inventory as some NetBox setups don't require authorization for GET functions (https://github.com/netbox-community/ansible_modules/issues/177)
- Remove token from being required for nb_lookup as some NetBox setups don't require authorization for GET functions (https://github.com/netbox-community/ansible_modules/issues/183)

ngine_io.cloudstack
~~~~~~~~~~~~~~~~~~~

- Added support for SSL CA cert verification (https://github.com/ngine-io/ansible-collection-cloudstack/pull/3)
- cs_configuration - Workaround for empty global settings idempotency (https://github.com/ngine-io/ansible-collection-cloudstack/pull/25).
- cs_vlan_ip_range - Added support to set IP range for system VMs (https://github.com/ngine-io/ansible-collection-cloudstack/pull/18)
- cs_vlan_ip_range - Added support to specify pod name (https://github.com/ngine-io/ansible-collection-cloudstack/pull/20)

ngine_io.vultr
~~~~~~~~~~~~~~

- vultr_server_info, vultr_server - Improved handling of discontinued plans (https://github.com/ansible/ansible/issues/66707).

openstack.cloud
~~~~~~~~~~~~~~~

- A basic module subclass was introduced and a few modules moved to inherit from it.
- Added changelog.
- Added more useful information from exception
- Added pip installation option for collection.
- Added template for generation of artibtrary module.
- Renaming all modules and removing "os" prefix from names.
- baremetal modules - Do not require ironic_url if cloud or auth.endpoint is provided
- baremetal_node_action - Support json type for the ironic_node config_drive parameter
- config - Update os_client_config to use openstacksdk
- host_aggregate - Add support for not 'purging' missing hosts
- inventory_openstack - Add openstack logger and Ansible display utility
- loadbalancer - Add support for setting the Flavor when creating a load balancer
- project - Add properties for os_project
- server_action - pass imageRef to rebuild
- subnet - Updated allocation pool checks

openvswitch.openvswitch
~~~~~~~~~~~~~~~~~~~~~~~

- Regenerated docs, add description to galaxy.yml and linked changelog to README (https://github.com/ansible-collections/openvswitch.openvswitch/pull/53).

ovirt.ovirt
~~~~~~~~~~~

- Add GPL license (https://github.com/oVirt/ovirt-ansible-collection/pull/101).
- ovirt inventory - Add creation_time (https://github.com/oVirt/ovirt-ansible-collection/pull/34).
- ovirt inventory - Set inventory plugin insecure if no cafile defined (https://github.com/oVirt/ovirt-ansible-collection/pull/58).
- ovirt_cluster - Add migration_encrypted option (https://github.com/oVirt/ovirt-ansible-collection/pull/17).
- ovirt_disk - Add upload image warning for correct format (https://github.com/oVirt/ovirt-ansible-collection/pull/22).
- ovirt_disk - Force wait when uploading disk (https://github.com/oVirt/ovirt-ansible-collection/pull/43).
- ovirt_disk - Upload_image_path autodetect size (https://github.com/oVirt/ovirt-ansible-collection/pull/19).
- ovirt_network - Add support of removing vlan_tag (https://github.com/oVirt/ovirt-ansible-collection/pull/21).
- ovirt_permission - Fix FQCN documentation (https://github.com/oVirt/ovirt-ansible-collection/pull/63).
- ovirt_vm - Add bios_type (https://github.com/oVirt/ovirt-ansible-collection/pull/15).
- ovirt_vm - Add documentation for custom_script under sysprep (https://github.com/oVirt/ovirt-ansible-collection/pull/52).
- ovirt_vm - Hard code nic on_boot to true (https://github.com/oVirt/ovirt-ansible-collection/pull/45).

purestorage.flasharray
~~~~~~~~~~~~~~~~~~~~~~

- purefa_hg - All LUN ID to be set for single volume
- purefa_host - Add CHAP support
- purefa_host - Add support for Cloud Block Store
- purefa_host - Add volume disconnection support
- purefa_info - Certificate times changed to human readable rather than time since epoch
- purefa_info - new options added for information collection
- purefa_info - return dict names changed from ``ansible_facts`` to ``ra_info`` and ``user_info`` in approproate sections
- purefa_offload - Add support for Azure
- purefa_pgsnap - Add offload support
- purefa_snap - Allow recovery of deleted snapshot
- purefa_vg - Add QoS support

purestorage.flashblade
~~~~~~~~~~~~~~~~~~~~~~

- purefb_bucket - Versioning support added
- purefb_info - new options added for information collection
- purefb_network - Add replication service type
- purefb_s3user - Limit ``access_key`` recreation to 3 times
- purefb_s3user - return dict changed from ``ansible_facts`` to ``s3user_info``

theforeman.foreman
~~~~~~~~~~~~~~~~~~

- activation_key - add ``description`` parameter (https://github.com/theforeman/foreman-ansible-modules/issues/915)
- callback plugin - add reporter to report logs sent to Foreman (https://github.com/theforeman/foreman-ansible-modules/issues/836)
- document return values of modules (https://github.com/theforeman/foreman-ansible-modules/pull/901)
- inventory plugin - allow to control batch size when pulling hosts from Foreman (https://github.com/theforeman/foreman-ansible-modules/pull/865)
- subnet - Require mask/cidr only on ipv4 (https://github.com/theforeman/foreman-ansible-modules/issues/878)

vyos.vyos
~~~~~~~~~

- Add doc plugin fixes (https://github.com/ansible-collections/vyos.vyos/pull/51)
- Fixed the typo in the modulename of ospfv2 and ospfv3 unit tests.
- Moved intent testcases from integration suite to unit tests.
- Reformatted files with latest version of Black (20.8b1).
- Updated docs.
- terminal plugin - Added additional escape sequence to be removed from terminal output.

Breaking Changes / Porting Guide
--------------------------------

- cisco.nxos.nxos_igmp_interface - no longer supports the deprecated ``oif_prefix`` and ``oif_source`` options. These have been superceeded by ``oif_ps``.
- community.grafana.grafana_dashboard - the parameter ``message`` is renamed to ``commit_message`` since ``message`` is used by Ansible Core engine internally.
- purestorage.flashblade.purefb_fs - no longer supports the deprecated ``nfs`` option. This has been superceeded by ``nfsv3``.

amazon.aws
~~~~~~~~~~

- aws_s3 - can now delete versioned buckets even when they are not empty - set mode to delete to delete a versioned bucket and everything in it.

ansible.windows
~~~~~~~~~~~~~~~

- setup - Make sure ``ansible_date_time.epoch`` is seconds since EPOCH in UTC to mirror the POSIX facts. The ``ansible_date_time.epoch_local`` contains seconds since EPOCH in the local timezone for backwards compatibility
- setup - Will now add the IPv6 scope on link local addresses for ``ansible_ip_addresses``
- setup - ``ansible_processor`` will now return the index before the other values to match the POSIX fact behaviour
- win_find - No longer filters by size on directories, this feature had a lot of bugs, slowed down the module, and not a supported scenario with the ``find`` module.
- win_find - module has been refactored to better match the behaviour of the ``find`` module. Here is what has changed:
    * When the directory specified by ``paths`` does not exist or is a file, it will no longer fail and will just warn the user
    * Junction points are no longer reported as ``islnk``, use ``isjunction`` to properly report these files. This behaviour matches the win_stat module
    * Directories no longer return a ``size``, this matches the ``stat`` and ``find`` behaviour and has been removed due to the difficulties in correctly reporting the size of a directory
- win_user - Change idempotency checks for ``description`` to be case sensitive
- win_user - Change idempotency checks for ``fullname`` to be case sensitive

cisco.meraki
~~~~~~~~~~~~

- meraki_device - Changed tags from string to list
- meraki_device - Removed serial_lldp_cdp parameter
- meraki_device - Removed serial_uplink parameter
- meraki_intrusion_prevention - Rename whitedlisted_rules to allowed_rules
- meraki_mx_l3_firewall - Rule responses are now in a `rules` list
- meraki_mx_l7_firewall - Rename blacklisted_countries to blocked_countries
- meraki_mx_l7_firewall - Rename whitelisted_countries to allowed_countries
- meraki_network - Local and remote status page settings cannot be set during network creation
- meraki_network - `disableRemoteStatusPage` response is now `remote_status_page_enabled`
- meraki_network - `disable_my_meraki_com` response is now `local_status_page_enabled`
- meraki_network - `disable_my_meraki` has been deprecated
- meraki_network - `enable_my_meraki` is now called `local_status_page_enabled`
- meraki_network - `enable_remote_status_page` is now called `remote_status_page_enabled`
- meraki_network - `enabled` response for VLAN status is now `vlans_enabled`
- meraki_network - `tags` and `type` now return a list
- meraki_snmp - peer_ips is now a list
- meraki_switchport - `access_policy_number` is now an int and not a string
- meraki_switchport - `tags` is now a list and not a string
- meraki_webhook - Querying test status now uses state of query.

community.general
~~~~~~~~~~~~~~~~~

- The environment variable for the auth context for the oc.py connection plugin has been corrected (K8S_CONTEXT).  It was using an initial lowercase k by mistake. (https://github.com/ansible-collections/community.general/pull/377).
- bigpanda - the parameter ``message`` was renamed to ``deployment_message`` since ``message`` is used by Ansible Core engine internally.
- cisco_spark - the module option ``message`` was renamed to ``msg``, as ``message`` is used internally in Ansible Core engine (https://github.com/ansible/ansible/issues/39295)
- datadog - the parameter ``message`` was renamed to ``notification_message`` since ``message`` is used by Ansible Core engine internally.
- docker_container - no longer passes information on non-anonymous volumes or binds as ``Volumes`` to the Docker daemon. This increases compatibility with the ``docker`` CLI program. Note that if you specify ``volumes: strict`` in ``comparisons``, this could cause existing containers created with docker_container from Ansible 2.9 or earlier to restart.
- docker_container - support for port ranges was adjusted to be more compatible to the ``docker`` command line utility: a one-port container range combined with a multiple-port host range will no longer result in only the first host port be used, but the whole range being passed to Docker so that a free port in that range will be used.
- hashi_vault lookup - now returns the latest version when using the KV v2 secrets engine. Previously, it returned all versions of the secret which required additional steps to extract and filter the desired version.
- log_plays callback - add missing information to the logs generated by the callback plugin. This changes the log message format (https://github.com/ansible-collections/community.general/pull/442).
- pkgng - passing ``name: *`` with ``state: absent`` will no longer remove every installed package from the system. It is now a noop. (https://github.com/ansible-collections/community.general/pull/569).
- pkgng - passing ``name: *`` with ``state: latest`` or ``state: present`` will no longer install every package from the configured package repositories. Instead, ``name: *, state: latest`` will upgrade all already-installed packages, and ``name: *, state: present`` is a noop. (https://github.com/ansible-collections/community.general/pull/569).

community.network
~~~~~~~~~~~~~~~~~

- routeros_facts - allow multiple addresses and neighbors per interface. This makes ``ansible_net_neighbors`` a list instead of a dict (https://github.com/ansible-collections/community.network/pull/6).

community.vmware
~~~~~~~~~~~~~~~~

- vmware_datastore_maintenancemode - now returns ``datastore_status`` instead of Ansible internal key ``results``.
- vmware_guest_custom_attributes - does not require VM name which was a required parameter for releases prior to Ansible 2.10.
- vmware_guest_find - the ``datacenter`` option has been removed.
- vmware_host_kernel_manager - now returns ``host_kernel_status`` instead of Ansible internal key ``results``.
- vmware_host_ntp - now returns ``host_ntp_status`` instead of Ansible internal key ``results``.
- vmware_host_service_manager - now returns ``host_service_status`` instead of Ansible internal key ``results``.
- vmware_tag - now returns ``tag_status`` instead of Ansible internal key ``results``.
- vmware_vmkernel - the options ``ip_address`` and ``subnet_mask`` have been removed; use the suboptions ``ip_address`` and ``subnet_mask`` of the ``network`` option instead.

community.windows
~~~~~~~~~~~~~~~~~

- win_pester - no longer runs all ``*.ps1`` file in the directory specified due to it executing potentially unknown scripts. It will follow the default behaviour of only running tests for files that are like ``*.tests.ps1`` which is built into Pester itself.

community.zabbix
~~~~~~~~~~~~~~~~

- zabbix_javagateway - options ``javagateway_pidfile``, ``javagateway_listenip``, ``javagateway_listenport`` and ``javagateway_startpollers`` renamed to ``zabbix_javagateway_xyz`` (see `UPGRADE.md <https://github.com/ansible-collections/community.zabbix/blob/main/docs/UPGRADE.md>`_).

netbox.netbox
~~~~~~~~~~~~~

- Change ``ip-addresses`` key in netbox inventory plugin to ``ip_addresses`` (https://github.com/netbox-community/ansible_modules/issues/139)
- Changed ``group`` to ``tenant_group`` in ``netbox_tenant.py`` (https://github.com/netbox-community/ansible_modules/issues/9)
- Changed ``role`` to ``prefix_role`` in ``netbox_prefix.py`` (https://github.com/netbox-community/ansible_modules/issues/9)
- Module failures when required fields arent provided (https://github.com/netbox-community/ansible_modules/issues/24)
- Renamed ``netbox_interface`` to ``netbox_device_interface`` (https://github.com/netbox-community/ansible_modules/issues/9)
- This version has a few breaking changes due to new namespace and collection name. I felt it necessary to change the name of the lookup plugin and inventory plugin just not to have a non descriptive namespace call to use them. Below is an example:
  ``netbox.netbox.netbox`` would be used for both inventory plugin and lookup plugin, but in different contexts so no collision will arise, but confusion will.
  I renamed the lookup plugin to ``nb_lookup`` so it will be used with the FQCN ``netbox.netbox.nb_lookup``.
  The inventory plugin will now be called within an inventory file by ``netbox.netbox.nb_inventory``
- To pass in integers via Ansible Jinja filters for a key in ``data`` that
  requires querying an endpoint is now done by making it a dictionary with
  an ``id`` key. The previous behavior was to just pass in an integer and
  it was converted when normalizing the data, but some people may have names
  that are all integers and those were being converted erroneously so we made
  the decision to change the method to convert to an integer for the NetBox
  API.

  ::

    tasks:
      - name: Create device within NetBox with only required information
        netbox_device:
          netbox_url: http://netbox-demo.org:32768
          netbox_token: 0123456789abcdef0123456789abcdef01234567
          data:
            name: Test66
            device_type:
              id: "{{ some_jinja_variable }}"
            device_role: Core Switch
            site: Test Site
            status: Staged
          state: present
- ``pynetbox`` changed to using ``requests.Session()`` to manage the HTTP session
  which broke passing in ``ssl_verify`` when building the NetBox API client.
  This PR makes ``pynetbox 5.0.4+`` the new required version of `pynetbox` for
  the Ansible modules and lookup plugin. (https://github.com/netbox-community/ansible_modules/pull/269)

theforeman.foreman
~~~~~~~~~~~~~~~~~~

- All modules were renamed to drop the ``foreman_`` and ``katello_`` prefixes.
  Additionally to the prefix removal, the following modules were further ranamed:

  * katello_upload to content_upload
  * katello_sync to repository_sync
  * katello_manifest to subscription_manifest
  * foreman_search_facts to resource_info
  * foreman_ptable to partition_table
  * foreman_model to hardware_model
  * foreman_environment to puppet_environment

Deprecated Features
-------------------

- The vyos.vyos.vyos_static_route module has been deprecated and will be removed in a later release; use vyos.vyos.vyos_static_routes instead.

Ansible-base
~~~~~~~~~~~~

- Using the DefaultCallback without the correspodning doc_fragment or copying the documentation.
- hash_behaviour - Deprecate ``hash_behaviour`` for future removal.
- script inventory plugin - The 'cache' option is deprecated and will be removed in 2.12. Its use has been removed from the plugin since it has never had any effect.

amazon.aws
~~~~~~~~~~

- All AWS Modules - ``aws_access_key``, ``aws_secret_key`` and ``security_token`` will be made mutually exclusive with ``profile`` after 2022-06-01.
- cloudformation - The ``template_format`` option had no effect since Ansible 2.3 and will be removed after 2022-06-01
- cloudformation - the ``template_format`` option has been deprecated and will be removed in a later release. It has been ignored by the module since Ansible 2.3.
- data_pipeline - The ``version`` option had no effect and will be removed in after 2022-06-01
- ec2 - in a later release, the ``group`` and ``group_id`` options will become mutually exclusive.  Currently ``group_id`` is ignored if you pass both.
- ec2_ami - The ``no_device`` alias ``NoDevice`` has been deprecated  and will be removed after 2022-06-01
- ec2_ami - The ``virtual_name`` alias ``VirtualName`` has been deprecated and will be removed after 2022-06-01
- ec2_eip - The ``wait_timeout`` option had no effect and will be removed after 2022-06-01
- ec2_key - The ``wait_timeout`` option had no effect and will be removed after 2022-06-01
- ec2_key - The ``wait`` option had no effect and will be removed after 2022-06-01
- ec2_key - the ``wait_timeout`` option has been deprecated and will be removed in a later release. It has had no effect since Ansible 2.5.
- ec2_key - the ``wait`` option has been deprecated and will be removed in a later release. It has had no effect since Ansible 2.5.
- ec2_lc - The ``associate_public_ip_address`` option had no effect and will be removed after 2022-06-01
- ec2_tag - deprecate the ``list`` option in favor of ec2_tag_info
- ec2_tag - support for ``list`` as a state has been deprecated and will be removed in a later release.  The ``ec2_tag_info`` can be used to fetch the tags on an EC2 resource.

ansible.windows
~~~~~~~~~~~~~~~

- win_domain_computer - Deprecated the undocumented ``log_path`` option. This option will be removed in a major release after ``2022-07-01``.
- win_domain_controller - the ``log_path`` option has been deprecated and will be removed in a later release. This was undocumented and only related to debugging information for module development.
- win_package - the ``ensure`` alias for the ``state`` option has been deprecated and will be removed in a later release. Please use ``state`` instead of ``ensure``.
- win_package - the ``productid`` alias for the ``product_id`` option has been deprecated and will be removed in a later release. Please use ``product_id`` instead of ``productid``.
- win_package - the ``username`` and ``password`` options has been deprecated and will be removed in a later release. The same functionality can be done by using ``become: yes`` and ``become_flags: logon_type=new_credentials logon_flags=netcredentials_only`` on the task.
- win_regedit - Deprecated using forward slashes as a path separator, use backslashes to avoid ambiguity between a forward slash in the key name or a forward slash as a path separator. This feature will be removed in a major release after ``2021-07-01``.

community.aws
~~~~~~~~~~~~~

- cloudformation - The ``template_format`` option had no effect since Ansible 2.3 and will be removed after 2022-06-01
- data_pipeline - The ``version`` option had no effect and will be removed after 2022-06-01
- data_pipeline - the ``version`` option has been deprecated and will be removed in a later release. It has always been ignored by the module.
- ec2_eip - The ``wait_timeout`` option had no effect and will be removed after 2022-06-01
- ec2_eip - the ``wait_timeout`` option has been deprecated and will be removed in a later release. It has had no effect since Ansible 2.3.
- ec2_key - The ``wait_timeout`` option had no effect and will be removed after 2022-06-01
- ec2_key - The ``wait`` option had no effect and will be removed after 2022-06-01
- ec2_lc - The ``associate_public_ip_address`` option had no effect and will be removed after 2022-06-01
- ec2_lc - the ``associate_public_ip_address`` option has been deprecated and will be removed after a later release. It has always been ignored by the module.
- elb_network_lb - The current default value of the ``state`` option has been deprecated and will change from absent to present after 2022-06-01
- elb_network_lb - in a later release, the default behaviour for the ``state`` option will change from ``absent`` to ``present``.  To maintain the existing behavior explicitly set state to ``absent``.
- iam_managed_policy - The ``fail_on_delete`` option had no effect and will be removed after 2022-06-01
- iam_managed_policy - the ``fail_on_delete`` option has been deprecated and will be removed after a later release.  It has always been ignored by the module.
- iam_policy - The ``policy_document`` will be removed after 2022-06-01.  To maintain the existing behavior use the ``policy_json`` option and read the file with the ``lookup`` plugin.
- iam_policy - The default value of ``skip_duplicates`` will change after 2022-06-01 from ``true`` to ``false``.
- iam_policy - in a later release, the default value for the ``skip_duplicates`` option will change from ``true`` to ``false``.  To maintain the existing behavior explicitly set it to ``true``.
- iam_policy - the ``policy_document`` option has been deprecated and will be removed after a later release. To maintain the existing behavior use the ``policy_json`` option and read the file with the ``lookup`` plugin.
- iam_role - The default value of the purge_policies has been deprecated and will change from true to false after 2022-06-01
- iam_role - in a later release, the ``purge_policies`` option (also know as ``purge_policy``) default value will change from ``true`` to ``false``
- s3_lifecycle - The ``requester_pays`` option had no effect and will be removed after 2022-06-01
- s3_lifecycle - the ``requester_pays`` option has been deprecated and will be removed after a later release. It has always been ignored by the module.
- s3_sync - The ``retries`` option had no effect and will be removed after 2022-06-01
- s3_sync - the ``retries`` option has been deprecated and will be removed after 2022-06-01. It has always been ignored by the module.

community.crypto
~~~~~~~~~~~~~~~~

- openssl_csr - all values for the ``version`` option except ``1`` are deprecated. The value 1 denotes the current only standardized CSR version.

community.general
~~~~~~~~~~~~~~~~~

- The ldap_attr module has been deprecated and will be removed in a later release; use ldap_attrs instead.
- airbrake_deployment - Add deprecation notice for ``token`` parameter and v2 api deploys. This feature will be removed in community.general 3.0.0.
- clc_aa_policy - The ``wait`` option had no effect and will be removed in community.general 3.0.0.
- clc_aa_policy - the ``wait`` parameter will be removed. It has always been ignored by the module.
- docker_container - the ``trust_image_content`` option is now deprecated and will be removed in community.general 3.0.0. It has never been used by the module.
- docker_container - the ``trust_image_content`` option will be removed. It has always been ignored by the module.
- docker_container - the default of ``container_default_behavior`` will change from ``compatibility`` to ``no_defaults`` in community.general 3.0.0. Set the option to an explicit value to avoid a deprecation warning.
- docker_container - the default value for ``network_mode`` will change in community.general 3.0.0, provided at least one network is specified and ``networks_cli_compatible`` is ``true``. See porting guide, module documentation or deprecation warning for more details.
- docker_stack - Return values ``out`` and ``err`` have been deprecated and will be removed in community.general 3.0.0. Use ``stdout`` and ``stderr`` instead.
- docker_stack - the return values ``err`` and ``out`` have been deprecated. Use ``stdout`` and ``stderr`` from now on instead.
- helm - Put ``helm`` module to deprecated. New implementation is available in community.kubernetes collection.
- redfish_config - Deprecate ``bios_attribute_name`` and ``bios_attribute_value`` in favor of new `bios_attributes`` option.
- redfish_config - the ``bios_attribute_name`` and ``bios_attribute_value`` options will be removed. To maintain the existing behavior use the ``bios_attributes`` option instead.
- redfish_config and redfish_command - the behavior to select the first System, Manager, or Chassis resource to modify when multiple are present will be removed. Use the new ``resource_id`` option to specify target resource to modify.
- redfish_config, redfish_command - Behavior to modify the first System, Mananger, or Chassis resource when multiple are present is deprecated. Use the new ``resource_id`` option to specify target resource to modify.
- xbps - the ``force`` option never had any effect. It is now deprecated, and will be removed in 3.0.0 (https://github.com/ansible-collections/community.general/pull/568).

community.vmware
~~~~~~~~~~~~~~~~

- The vmware_dns_config module has been deprecated and will be removed in a later release; use vmware_host_dns instead.
- vca - vca_fw, vca_nat, vca_app are deprecated since these modules rely on deprecated part of Pyvcloud library.
- vmware_dns_config - Deprecate in favour of new module vmware_host_dns.
- vmware_guest - deprecate specifying CDROM configuration as a dict, instead use a list.
- vmware_tag_info - in a later release, the module will not return ``tag_facts`` since it does not return multiple tags with the same name and different category id. To maintain the existing behavior use ``tag_info`` which is a list of tag metadata.

community.zabbix
~~~~~~~~~~~~~~~~

- zabbix_proxy (module) - deprecates ``interface`` sub-options ``type`` and ``main`` when proxy type is set to passive via ``status=passive``. Make sure these suboptions are removed from your playbook as they were never supported by Zabbix in the first place.

openstack.cloud
~~~~~~~~~~~~~~~

- foo - The bar option has been deprecated. Use the username option instead.
- send_request - The quic option has been deprecated. Use the protocol option instead.

Removed Features (previously deprecated)
----------------------------------------

Ansible-base
~~~~~~~~~~~~

- core - remove support for ``check_invalid_arguments`` in ``AnsibleModule``, ``AzureModule`` and ``UTMModule``.

ansible.netcommon
~~~~~~~~~~~~~~~~~

- module_utils.network.common.utils.ComplexDict has been removed

ansible.windows
~~~~~~~~~~~~~~~

- win_stat - removed the deprecated ``get_md55`` option and ``md5`` return value.

community.crypto
~~~~~~~~~~~~~~~~

- The ``letsencrypt`` module has been removed. Use ``acme_certificate`` instead.

community.general
~~~~~~~~~~~~~~~~~

- conjur_variable lookup - has been moved to the ``cyberark.conjur`` collection. A redirection is active, which will be removed in version 2.0.0 (https://github.com/ansible-collections/community.general/pull/570).
- core - remove support for ``check_invalid_arguments`` in ``UTMModule``.
- digital_ocean_* - all DigitalOcean modules have been moved to the ``community.digitalocean`` collection. A redirection is active, which will be removed in version 2.0.0 (https://github.com/ansible-collections/community.general/pull/622).
- infini_* - all infinidat modules have been moved to the ``infinidat.infinibox`` collection. A redirection is active, which will be removed in version 2.0.0 (https://github.com/ansible-collections/community.general/pull/607).
- logicmonitor - the module has been removed in 1.0.0 since it is unmaintained and the API used by the module has been turned off in 2017 (https://github.com/ansible-collections/community.general/issues/539, https://github.com/ansible-collections/community.general/pull/541).
- logicmonitor_facts - the module has been removed in 1.0.0 since it is unmaintained and the API used by the module has been turned off in 2017 (https://github.com/ansible-collections/community.general/issues/539, https://github.com/ansible-collections/community.general/pull/541).
- mysql_* - all MySQL modules have been moved to the ``community.mysql`` collection. A redirection is active, which will be removed in version 2.0.0 (https://github.com/ansible-collections/community.general/pull/633).
- pacman - Removed deprecated ``recurse`` option, use ``extra_args=--recursive`` instead
- proxysql_* - all ProxySQL modules have been moved to the ``community.proxysql`` collection. A redirection is active, which will be removed in version 2.0.0 (https://github.com/ansible-collections/community.general/pull/624).

community.network
~~~~~~~~~~~~~~~~~

- onyx - all onyx modules and plugins have been moved to the mellanox.onyx collection. Redirects have been added that will be removed in community.network 2.0.0 (https://github.com/ansible-collections/community.network/pull/83).

community.vmware
~~~~~~~~~~~~~~~~

- vmware_guest_find - Removed deprecated ``datacenter`` option
- vmware_portgroup - removed 'inbound_policy', and 'rolling_order' deprecated options.
- vmware_vmkernel - Removed deprecated ``ip_address`` option; use sub-option ip_address in the network option instead
- vmware_vmkernel - Removed deprecated ``subnet_mask`` option; use sub-option subnet_mask in the network option instead

community.windows
~~~~~~~~~~~~~~~~~

- win_disk_image - removed the deprecated return value ``mount_path`` in favour of ``mount_paths``.
- win_psexec - removed the deprecated ``extra_opts`` option.

Security Fixes
--------------

Ansible-base
~~~~~~~~~~~~

- **security issue** - Convert CLI provided passwords to text initially, to prevent unsafe context being lost when converting from bytes->text during post processing of PlayContext. This prevents CLI provided passwords from being incorrectly templated (CVE-2019-14856)
- **security issue** - Redact cloud plugin secrets in ansible-test when running integration tests using cloud plugins. Only present in 2.9.0b1.
- **security issue** - TaskExecutor - Ensure we don't erase unsafe context in TaskExecutor.run on bytes. Only present in 2.9.0beta1 (https://github.com/ansible/ansible/issues/62237)
- **security issue** - The ``subversion`` module provided the password via the svn command line option ``--password`` and can be retrieved from the host's /proc/<pid>/cmdline file. Update the module to use the secure ``--password-from-stdin`` option instead, and add a warning in the module and in the documentation if svn version is too old to support it. (CVE-2020-1739)
- **security issue** - Update ``AnsibleUnsafeText`` and ``AnsibleUnsafeBytes`` to maintain unsafe context by overriding ``.encode`` and ``.decode``. This prevents future issues with ``to_text``, ``to_bytes``, or ``to_native`` removing the unsafe wrapper when converting between string types (CVE-2019-14856)
- **security issue** - copy - Redact the value of the no_log 'content' parameter in the result's invocation.module_args in check mode. Previously when used with check mode and with '-vvv', the module would not censor the content if a change would be made to the destination path. (CVE-2020-14332)
- **security issue** - properly hide parameters marked with ``no_log`` in suboptions when invalid parameters are passed to the module (CVE-2019-14858)
- **security issue** atomic_move - change default permissions when creating temporary files so they are not world readable (https://github.com/ansible/ansible/issues/67794) (CVE-2020-1736)
- **security issue** win_unzip - normalize paths in archive to ensure extracted files do not escape from the target directory (CVE-2020-1737)
- **security_issue** - create temporary vault file with strict permissions when editing and prevent race condition (CVE-2020-1740)
- Ensure we get an error when creating a remote tmp if it already exists. CVE-2020-1733
- In fetch action, avoid using slurp return to set up dest, also ensure no dir traversal CVE-2020-1735.
- Sanitize no_log values from any response keys that might be returned from the uri module (CVE-2020-14330).
- The fix for CVE-2020-1736 has been reverted. Users are encouraged to specify a ``mode`` parameter in their file-based tasks when the files being manipulated contain sensitive data.
- ansible-galaxy - Error when install finds a tar with a file that will be extracted outside the collection install directory - CVE-2020-10691
- dnf - Previously, regardless of the ``disable_gpg_check`` option, packages were not GPG validated. They are now. (CVE-2020-14365)

cisco.meraki
~~~~~~~~~~~~

- meraki_webhook - diff output may show data for values set to not display

community.general
~~~~~~~~~~~~~~~~~

- **SECURITY** - CVE-2019-14904 - solaris_zone module accepts zone name and performs actions related to that. However, there is no user input validation done while performing actions. A malicious user could provide a crafted zone name which allows executing commands into the server manipulating the module behaviour. Adding user input validation as per Solaris Zone documentation fixes this issue.
- **security issue** - Ansible: Splunk and Sumologic callback plugins leak sensitive data in logs (CVE-2019-14864)
- ldap_attr, ldap_entry - The ``params`` option has been removed in Ansible-2.10 as it circumvents Ansible's option handling.  Setting ``bind_pw`` with the ``params`` option was disallowed in Ansible-2.7, 2.8, and 2.9 as it was insecure.  For information about this policy, see the discussion at: https://meetbot.fedoraproject.org/ansible-meeting/2017-09-28/ansible_dev_meeting.2017-09-28-15.00.log.html This fixes CVE-2020-1746

community.kubernetes
~~~~~~~~~~~~~~~~~~~~

- kubectl - Warn about information disclosure when using options like ``kubectl_password``, ``kubectl_extra_args``, and ``kubectl_token`` to pass data through to the command line using the ``kubectl`` connection plugin (https://github.com/ansible-collections/community.kubernetes/pull/51).
- kubectl - connection plugin now redact kubectl_token and kubectl_password in console log (https://github.com/ansible-collections/community.kubernetes/issues/65).
- kubectl - redacted token and password from console log (https://github.com/ansible-collections/community.kubernetes/pull/159).

Bugfixes
--------

Ansible-base
~~~~~~~~~~~~

- ANSIBLE_COLLECTIONS_PATHS - remove deprecation so that users of Ansible 2.9 and 2.10+ can use the same var when specifying a collection path without a warning.
- ActionBase - Add new ``cleanup`` method that is explicitly run by the ``TaskExecutor`` to ensure that the shell plugins ``tmpdir`` is always removed. This change means that individual action plugins need not be responsible for removing the temporary directory, which ensures that we don't have code paths that accidentally leave behind the temporary directory.
- Add example setting for ``collections_paths`` parameter to ``examples/ansible.cfg``
- Add missing gcp modules to gcp module defaults group
- Added support for Flatcar Container Linux in distribution and hostname modules. (https://github.com/ansible/ansible/pull/69627)
- Added support for OSMC distro in hostname module (https://github.com/ansible/ansible/issues/66189).
- Address compat with rpmfluff-0.6 for integration tests
- Address the deprecation of the use of stdlib distutils in packaging. It's a short-term hotfix for the problem (https://github.com/ansible/ansible/issues/70456, https://github.com/pypa/setuptools/issues/2230, https://github.com/pypa/setuptools/commit/bd110264)
- Allow TypeErrors on Undefined variables in filters to be handled or deferred when processing for loops.
- Allow tasks to notify a fqcn handler name (https://github.com/ansible/ansible/issues/68181)
- An invalid value is hard to track down if you don't know where it came from, return field name instead.
- Ansible output now uses stdout to determine column width instead of stdin
- Ansible.Basic - Fix issue when setting a ``no_log`` parameter to an empty string - https://github.com/ansible/ansible/issues/62613
- Ansible.ModuleUtils.WebRequest - actually set no proxy when ``use_proxy: no`` is set on a Windows module - https://github.com/ansible/ansible/issues/68528
- AnsibleDumper - Add a representer for AnsibleUnsafeBytes (https://github.com/ansible/ansible/issues/62562).
- AnsibleModule.run_command() - set ``close_fds`` to ``False`` on Python 2 if ``pass_fds`` are passed to ``run_command()``. Since ``subprocess.Popen()`` on Python 2 does not have the ``pass_fds`` option, there is no way to exclude a specific list of file descriptors from being closed.
- Avoid bare select() for running commands to avoid too large file descriptor numbers failing tasks
- Avoid running subfunctions that are passed to show_vars function when it will be a noop.
- By passing the module_tmpdir as a parameter in the write_ssh_wrapper function instead of initalizing module_tmpdir via get_module_path()
- CLI - the `ANSIBLE_PLAYBOOK_DIR` envvar or `playbook_dir` config can now substitute for the --playbook-dir arg on CLIs that support it (https://github.com/ansible/ansible/issues/59464)
- Check NoneType for raw_params before proceeding in include_vars (https://github.com/ansible/ansible/issues/64939).
- Collections - Allow a collection role to call a stand alone role, without needing to explicitly add ``ansible.legacy`` to the collection search order within the collection role. (https://github.com/ansible/ansible/issues/69101)
- Confirmed commit fails with TypeError in IOS XR netconf plugin (https://github.com/ansible-collections/cisco.iosxr/issues/74)
- Correctly process raw_params in add_hosts.
- Create an ``import_module`` compat util, for use across the codebase, to allow collection loading to work properly on Python26
- DUPLICATE_YAML_DICT_KEY - Fix error output when configuration option DUPLICATE_YAML_DICT_KEY is set to error (https://github.com/ansible/ansible/issues/65366)
- Do not keep empty blocks in PlayIterator after skipping tasks with tags.
- Ensure DataLoader temp files are removed at appropriate times and that we observe the LOCAL_TMP setting.
- Ensure password passed in by -k is used on delegated hosts that do not have ansible_password set
- Ensure that ``--version`` works with non-ascii ansible project paths (https://github.com/ansible/ansible/issues/66617)
- Ensure that keywords defined as booleans are correctly interpreting their input, before patch any random string would be interpreted as False
- Ensure we don't allow ansible_facts subkey of ansible_facts to override top level, also fix 'deprefixing' to prevent key transforms.
- Fact Delegation - Add ability to indicate which facts must always be delegated. Primarily for ``discovered_interpreter_python`` right now, but extensible later. (https://github.com/ansible/ansible/issues/61002)
- Fix ``delegate_facts: true`` when ``ansible_python_interpreter`` is not set. (https://github.com/ansible/ansible/issues/70168)
- Fix a bug when a host was not removed from a play after ``meta: end_host`` and as a result the host was still present in ``ansible_play_hosts`` and ``ansible_play_batch`` variables.
- Fix an exit code for a non-failing playbook (https://github.com/ansible/ansible/issues/71306)
- Fix an issue with the ``fileglob`` plugin where passing a subdirectory of non-existent directory would cause it to fail - https://github.com/ansible/ansible/issues/69450
- Fix case sensitivity for ``lookup()`` (https://github.com/ansible/ansible/issues/66464)
- Fix collection install error that happened if a dependency specified dependencies to be null (https://github.com/ansible/ansible/issues/67574).
- Fix execution of the meta tasks 'clear_facts', 'clear_host_errors', 'end_play', 'end_host', and 'reset_connection' when the CLI flag '--flush-cache' is provided.
- Fix https://github.com/ansible/galaxy-dev/issues/96 Add support for automation-hub authentication to ansible-galaxy
- Fix incorrect "Could not match supplied host pattern" warning (https://github.com/ansible/ansible/issues/66764)
- Fix issue git module cannot use custom `key_file` or `ssh_opts` as non-root user on system with noexec `/tmp` (https://github.com/ansible/ansible/issues/30064).
- Fix issue git module ignores remote_tmp (https://github.com/ansible/ansible/issues/33947).
- Fix issue where the collection loader tracebacks if ``collections_paths = ./`` is set in the config
- Fix issue with callbacks ``set_options`` method that was not called with collections
- Fix label lookup in the default callback for includes (https://github.com/ansible/ansible/issues/65904)
- Fix regression when ``ansible_failed_task`` and ``ansible_failed_result`` are not defined in the rescue block (https://github.com/ansible/ansible/issues/64789)
- Fix statistics reporting when rescue block contains another block (issue https://github.com/ansible/ansible/issues/61253).
- Fix string parsing of inline vault strings for plugin config variable sources
- Fix traceback when printing ``HostVars`` on native Jinja2 (https://github.com/ansible/ansible/issues/65365)
- Fix warning for default permission change when no mode is specified. Follow up to https://github.com/ansible/ansible/issues/67794. (CVE-2020-1736)
- Fixed Ansible reporting validate not supported by netconf server when enabled in netconf - (https://github.com/ansible-collections/ansible.netcommon/issues/119).
- Fixed a bug with the copy action plugin where mode=preserve was being passed on symlink files and causing a traceback (https://github.com/ansible/ansible/issues/68471).
- Fixed the equality check for IncludedFiles to ensure they are not accidently merged when process_include_results runs.
- Fixes ansible-test traceback when plugin author is not a string or a list of strings (https://github.com/ansible/ansible/pull/70507)
- Fixes in network action plugins load from collections using module prefix (https://github.com/ansible/ansible/issues/65071)
- Force collection names to be static so that a warning is generated because templating currently does not work (see https://github.com/ansible/ansible/issues/68704).
- Handle empty extra vars in ansible cli (https://github.com/ansible/ansible/issues/61497).
- Handle empty roles and empty collections in requirements.yml in ansible-galaxy install command (https://github.com/ansible/ansible/issues/68186).
- Handle exception encountered while parsing the argument description in module when invoked via ansible-doc command (https://github.com/ansible/ansible/issues/60587).
- Handle exception when /etc/shadow file is missing or not found, while operating user operation in user module (https://github.com/ansible/ansible/issues/63490).
- HostVarsVars - Template the __repr__ value (https://github.com/ansible/ansible/issues/64128).
- JSON Encoder - Ensure we treat single vault encrypted values as strings (https://github.com/ansible/ansible/issues/70784)
- Make netconf plugin configurable to set ncclient device handler name in netconf plugin (https://github.com/ansible/ansible/pull/65718)
- Make sure if a collection is supplied as a string that we transform it into a list.
- Misc typo fixes in various documentation pages.
- Module arguments in suboptions which were marked as deprecated with ``removed_in_version`` did not result in a warning.
- On HTTP status code 304, return status_code
- Plugin Metadata is supposed to have default values.  When the metadata was missing entirely, we were properly setting the defaults.  Fixed the metadata parsing so that the defaults are also set when we were missing just a few fields.
- Prevent a race condition when running handlers using a combination of the free strategy and include_role.
- Prevent rewriting nested Block's data in filter_tagged_tasks
- Prevent templating unused variables for {% include %} (https://github.com/ansible/ansible/issues/68699)
- Properly handle unicode in ``safe_eval``. (https://github.com/ansible/ansible/issues/66943)
- Python module_utils finder - refactor logic to eliminate many corner cases, remove recursion, fix base module_utils redirections
- Remove a temp directory created by wait_for_connection action plugin (https://github.com/ansible/ansible/issues/62407).
- Remove the unnecessary warning about aptitude not being installed (https://github.com/ansible/ansible/issues/56832).
- Remove unused Python imports in ``ansible-inventory``.
- Restore the ability for changed_when/failed_when to function with group_by (#70844).
- Role Installation - Ensure that a role containing files with non-ascii characters can be installed (https://github.com/ansible/ansible/issues/69133)
- RoleRequirement - include stderr in the error message if a scm command fails (https://github.com/ansible/ansible/issues/41336)
- SSH plugin - Improve error message when ssh client is not found on the host
- Skip literal_eval for string filters results in native jinja. (https://github.com/ansible/ansible/issues/70831)
- Skipping of become for ``network_cli`` connections now works when ``network_cli`` is sourced from a collection.
- Stop adding the connection variables to the output results
- Strategy - Ensure we only process expected types from the results queue and produce warnings for any object we receive from the queue that doesn't match our expectations. (https://github.com/ansible/ansible/issues/70023)
- Strictly check string datatype for 'tasks_from', 'vars_from', 'defaults_from', and 'handlers_from' in include_role (https://github.com/ansible/ansible/issues/68515).
- Strip no log values from module response keys (https://github.com/ansible/ansible/issues/68400)
- TOML inventory - Ensure we register dump functions for ``AnsibleUnsafe`` to support dumping unsafe values. Note that the TOML format has no functionality to mark that the data is unsafe for re-consumption. (https://github.com/ansible/ansible/issues/71307)
- TaskExecutor - Handle unexpected errors as failed while post validating loops (https://github.com/ansible/ansible/issues/70050).
- TaskQueueManager - Explicitly set the mutliprocessing start method to ``fork`` to avoid issues with the default on macOS now being ``spawn``.
- Template connection variables before using them (https://github.com/ansible/ansible/issues/70598).
- Templating - Ansible was caching results of Jinja2 expressions in some cases where these expressions could have dynamic results, like password generation (https://github.com/ansible/ansible/issues/34144).
- Terminal plugins - add "\e[m" to the list of ANSI sequences stripped from device output
- The `ansible_become` value was not being treated as a boolean value when set in an INI format inventory file (fixes bug https://github.com/ansible/ansible/issues/70476).
- The ansible-galaxy publish command was using an incorrect URL for v3 servers. The configuration for v3 servers includes part of the path fragment that was added in the new test.
- The machine-readable changelog ``changelogs/changelog.yaml`` is now contained in the release.
- Update ActionBase._low_level_execute_command to honor executable (https://github.com/ansible/ansible/issues/68054)
- Update the warning message for ``CONDITIONAL_BARE_VARS`` to list the original conditional not the value of the original conditional (https://github.com/ansible/ansible/issues/67735)
- Use ``sys.exit`` instead of ``exit`` in ``ansible-inventory``.
- Use fqcr from command module invocation using shell module. Fixes https://github.com/ansible/ansible/issues/69788
- Use hostnamectl command to get current hostname for host while using systemd strategy (https://github.com/ansible/ansible/issues/59438).
- Using --start-at-task would fail when it attempted to skip over tasks with no name.
- Validate include args in handlers.
- Vault - Allow single vault encrypted values to be used directly as module parameters. (https://github.com/ansible/ansible/issues/68275)
- Vault - Make the single vaulted value ``AnsibleVaultEncryptedUnicode`` class work more like a string by replicating the behavior of ``collections.UserString`` from Python. These changes don't allow it to be considered a string, but most common python string actions will now work as expected. (https://github.com/ansible/ansible/pull/67823)
- ``AnsibleUnsafe``/``AnsibleContext``/``Templar`` - Do not treat ``AnsibleUndefined`` as being "unsafe" (https://github.com/ansible/ansible/issues/65198)
- account for empty strings in when splitting the host pattern (https://github.com/ansible/ansible/issues/61964)
- action plugins - change all action/module delegations to use FQ names while allowing overrides (https://github.com/ansible/ansible/issues/69788)
- add constraints file for ``anisble_runner`` test since an update to ``psutil`` is now causing test failures
- add magic/connection vars updates from delegated host info.
- add parameter name to warning message when values are converted to strings (https://github.com/ansible/ansible/pull/57145)
- add_host action now correctly shows idempotency/changed status
- added 'unimplemented' prefix to file based caching
- added new option for default callback to compat variable to avoid old 3rd party plugins from erroring out.
- adhoc CLI - when playbook-dir is specified and inside a collection, use default collection logic to resolve modules/actions
- allow external collections to be created in the 'ansible' collection namespace (https://github.com/ansible/ansible/issues/59988)
- also strip spaces around config values in pathlist as we do in list types
- ansiballz - remove '' and '.' from sys.path to fix a permissions issue on OpenBSD with pipelining (#69320)
- ansible command now correctly sends v2_playbook_on_start to callbacks
- ansible-connection persists even after playbook run is completed (https://github.com/ansible/ansible/pull/61591)
- ansible-doc - Allow and give precedence to `removed_at_date` for deprecated modules.
- ansible-doc - collection name for plugin top-level deprecation was not inserted when deprecating by version (https://github.com/ansible/ansible/pull/70344).
- ansible-doc - improve error message in text formatter when ``description`` is missing for a (sub-)option or a return value or its ``contains`` (https://github.com/ansible/ansible/pull/70046).
- ansible-doc - improve man page formatting to avoid problems when YAML anchors are used (https://github.com/ansible/ansible/pull/70045).
- ansible-doc - include the collection name in the text output (https://github.com/ansible/ansible/pull/70401).
- ansible-doc now properly handles removed modules/plugins
- ansible-galaxy - Default collection install path to first path in COLLECTIONS_PATHS (https://github.com/ansible/ansible/pull/62870)
- ansible-galaxy - Display proper error when invalid token is used for Galaxy servers
- ansible-galaxy - Ensure we preserve the new URL when appending ``/api`` for the case where the GET succeeds on galaxy.ansible.com
- ansible-galaxy - Expand the ``User-Agent`` to include more information and add it to more calls to Galaxy endpoints.
- ansible-galaxy - Fix ``collection install`` when installing from a URL or a file - https://github.com/ansible/ansible/issues/65109
- ansible-galaxy - Fix ``multipart/form-data`` body to include extra CRLF (https://github.com/ansible/ansible/pull/67942)
- ansible-galaxy - Fix issue when compared installed dependencies with a collection having no ``MANIFEST.json`` or an empty version string in the json
- ansible-galaxy - Fix pagination issue when retrieving role versions for install - https://github.com/ansible/ansible/issues/64355
- ansible-galaxy - Fix up pagination searcher for collection versions on Automation Hub
- ansible-galaxy - Fix url building to not truncate the URL (https://github.com/ansible/ansible/issues/61624)
- ansible-galaxy - Handle the different task resource urls in API responses from publishing collection artifacts to galaxy servers using v2 and v3 APIs.
- ansible-galaxy - Preserve symlinks when building and installing a collection
- ansible-galaxy - Remove uneeded verbose messages when accessing local token file
- ansible-galaxy - Return the HTTP code reason if no error msg was returned by the server - https://github.com/ansible/ansible/issues/64850
- ansible-galaxy - Send SHA256 hashes when publishing a collection
- ansible-galaxy - Set ``User-Agent`` to Ansible version when interacting with Galaxy or Automation Hub
- ansible-galaxy - Treat the ``GALAXY_SERVER_LIST`` config entry that is defined but with no values as an empty list
- ansible-galaxy - Utilize ``Templar`` for templating skeleton files, so that they have access to Ansible filters/tests/lookups (https://github.com/ansible/ansible/issues/69104)
- ansible-galaxy - fix a bug where listing a specific role if it was not in the first path failed to find the role
- ansible-galaxy - fix regression that prenented roles from being listed
- ansible-galaxy - hide warning during collection installation if other installed collections do not contain a ``MANIFEST.json`` (https://github.com/ansible/ansible/issues/67490)
- ansible-galaxy - properly list roles when the role name also happens to be in the role path (https://github.com/ansible/ansible/issues/67365)
- ansible-galaxy - properly show the role description when running offline (https://github.com/ansible/ansible/issues/60167)
- ansible-galaxy cli - fixed ``--version`` argument
- ansible-galaxy collection - Preserve executable bit on build and preserve mode on install from what tar member is set to - https://github.com/ansible/ansible/issues/68415
- ansible-galaxy collection download - fix downloading tar.gz files and collections in git repositories (https://github.com/ansible/ansible/issues/70429)
- ansible-galaxy collection install - fix fallback mechanism if the AH server did not have the collection requested - https://github.com/ansible/ansible/issues/70940
- ansible-galaxy download - fix bug when downloading a collection in a SCM subdirectory
- ansible-galaxy role - Fix issue where ``--server`` was not being used for certain ``ansible-galaxy role`` actions - https://github.com/ansible/ansible/issues/61609
- ansible-galaxy- On giving an invalid subcommand to ansible-galaxy, the help would be shown only for role subcommand (collection subcommand help is not shown). With this change, the entire help for ansible-galaxy (same as ansible-galaxy --help) is displayed along with the help for role subcommand. (https://github.com/ansible/ansible/issues/69009)
- ansible-inventory - Fix long standing bug not loading vars plugins for group vars relative to the playbook dir when the '--playbook-dir' and '--export' flags are used together.
- ansible-inventory - Fix regression loading vars plugins. (https://github.com/ansible/ansible/issues/65064)
- ansible-inventory - Properly hide arguments that should not be shown (https://github.com/ansible/ansible/issues/61604)
- ansible-inventory - Restore functionality to allow ``--graph`` to be limited by a host pattern
- ansible-test - Add ``pytest < 6.0.0`` constraint for managed installations on Python 3.x to avoid issues with relative imports.
- ansible-test - Change detection now properly resolves relative imports instead of treating them as absolute imports.
- ansible-test - Code cleanup.
- ansible-test - Disabled the ``duplicate-code`` and ``cyclic-import`` checks for the ``pylint`` sanity test due to inconsistent results.
- ansible-test - Do not try to validate PowerShell modules ``setup.ps1``, ``slurp.ps1``, and ``async_status.ps1``
- ansible-test - Do not warn on missing PowerShell or C# util that are in other collections
- ansible-test - Fix PowerShell module util analysis to properly detect the names of a util when running in a collection
- ansible-test - Fix regression introduced in https://github.com/ansible/ansible/pull/67063 which caused module_utils analysis to fail on Python 2.x.
- ansible-test - Fix traceback in validate-modules test when argument_spec is None.
- ansible-test - Make sure import sanity test virtual environments also remove ``pkg-resources`` if it is not removed by uninstalling ``setuptools``.
- ansible-test - Remove out-of-date constraint on installing paramiko versions 2.5.0 or later in tests.
- ansible-test - The ``ansible-doc`` sanity test now works for ``netconf`` plugins.
- ansible-test - The ``import`` sanity test now correctly blocks access to python modules, not just packages, in the ``ansible`` package.
- ansible-test - The ``import`` sanity test now correctly provides an empty ``ansible`` package.
- ansible-test - The shebang sanity test now correctly identifies modules in subdirectories in collections.
- ansible-test - Updated Python constraints for installing ``coverage`` to resolve issues on multiple Python versions when using the ``--coverage`` option.
- ansible-test - Updated requirements to limit ``boto3`` and ``botocore`` versions on Python 2.6 to supported versions.
- ansible-test - Use ``sys.exit`` instead of ``exit``.
- ansible-test - Use ``virtualenv`` versions before 20 on provisioned macOS instances to remain compatible with an older pip install.
- ansible-test - avoid use of deprecated junit_xml method
- ansible-test - bump version of ACME test container. The new version includes updated dependencies.
- ansible-test - during module validation, handle add_file_common_args only for top-level arguments.
- ansible-test - during module validation, improve alias handling.
- ansible-test - for local change detection, allow to specify branch to compare to with ``--base-branch`` for all types of tests (https://github.com/ansible/ansible/pull/69508).
- ansible-test - improve ``deprecate()`` call checker.
- ansible-test - integration and unit test change detection now works for filter, lookup and test plugins
- ansible-test can now install argparse with ``--requirements`` or delegation when the pip version in use is older than version 7.1
- ansible-test change detection - Run only sanity tests on ``docs/`` and ``changelogs/`` in collections, to avoid triggering full CI runs of integration and unit tests when files in these directories change.
- ansible-test coverage - Fix the ``--all`` argument when generating coverage reports - https://github.com/ansible/ansible/issues/62096
- ansible-test import sanity test now consistently reports errors against the file being tested.
- ansible-test import sanity test now consistently reports warnings as errors.
- ansible-test import sanity test now properly handles relative imports.
- ansible-test import sanity test now properly invokes Ansible modules as scripts.
- ansible-test is now able to find its ``egg-info`` directory when it contains the Ansible version number
- ansible-test no longer errors reporting coverage when no Python coverage exists. This fixes issues reporting on PowerShell only coverage from collections.
- ansible-test no longer fails when downloading test results for a collection without a ``tests`` directory when using the ``--docker`` option.
- ansible-test no longer optimizes setting ``PATH`` by prepending the directory containing the selected Python interpreter when it is named ``python``. This avoids unintentionally making other programs available on ``PATH``, including an already installed version of Ansible.
- ansible-test no longer tracebacks during change analysis due to processing an empty python file
- ansible-test no longer tries to install ``coverage`` 5.0+ since those versions are unsupported
- ansible-test no longer tries to install ``setuptools`` 45+ on Python 2.x since those versions are unsupported
- ansible-test now always uses the ``--python`` option for ``virtualenv`` to select the correct interpreter when creating environments with the ``--venv`` option
- ansible-test now correctly collects code coverage on the last task in a play. This should resolve issues with missing code coverage, empty coverage files and corrupted coverage files resulting from early worker termination.
- ansible-test now correctly enumerates submodules when a collection resides below the repository root
- ansible-test now correctly excludes the test results temporary directory when copying files from the remote test system to the local system
- ansible-test now correctly includes inventory files ignored by git when running tests with the ``--docker`` option
- ansible-test now correctly installs the requirements specified by the collection's unit and integration tests instead of the requirements specified for Ansible's own unit and integration tests
- ansible-test now correctly recognizes imports in collections when using the ``--changed`` option.
- ansible-test now correctly rewrites coverage paths for PowerShell files when testing collections
- ansible-test now creates its integration test temporary directory within the collection so ansible-playbook can properly detect the default collection
- ansible-test now enables color ``ls`` on a remote host only if the host supports the feature
- ansible-test now ignores empty ``*.py`` files when analyzing module_utils imports for change detection
- ansible-test now ignores version control within subdirectories of collections. Previously this condition was an error.
- ansible-test now ignores warnings when comparing pip versions before and after integration tests run
- ansible-test now installs sanity test requirements specific to each test instead of installing requirements for all sanity tests
- ansible-test now installs the correct version of ``cryptography`` with ``--requirements`` or delegation when setuptools is older than version 18.5
- ansible-test now limits Jinja2 installs to version 2.10 and earlier on Python 2.6
- ansible-test now limits ``pathspec`` to versions prior to 0.6.0 on Python 2.6 to avoid installation errors
- ansible-test now limits installation of ``hcloud`` to Python 2.7 and 3.5 - 3.8 since other versions are unsupported
- ansible-test now limits the version of ``setuptools`` on Python 2.6 to versions older than 37
- ansible-test now loads the collection loader plugin early enough for ansible_collections imports to work in unit test conftest.py modules
- ansible-test now preserves existing SSH authorized keys when provisioning a remote host
- ansible-test now properly activates the vcenter plugin for vcenter tests when docker is available
- ansible-test now properly activates virtual environments created using the --venv option
- ansible-test now properly creates a virtual environment using ``venv`` when running in a ``virtualenv`` created virtual environment
- ansible-test now properly excludes the ``tests/output/`` directory from code coverage
- ansible-test now properly handles creation of Python execv wrappers when the selected interpreter is a script
- ansible-test now properly handles enumeration of git submodules. Enumeration is now done with ``git submodule status --recursive`` without specifying ``.`` for the path, since that could cause the command to fail. Instead, relative paths outside the current directory are filtered out of the results. Errors from ``git`` commands will now once again be reported as errors instead of warnings.
- ansible-test now properly handles warnings for removed modules/plugins
- ansible-test now properly ignores the ``tests/output//`` directory when not using git
- ansible-test now properly installs requirements for multiple Python versions when running sanity tests
- ansible-test now properly recognizes modules and module_utils in collections when using the ``blacklist`` plugin for the ``pylint`` sanity test
- ansible-test now properly registers its own code in a virtual environment when running from an install
- ansible-test now properly reports import errors for collections when running the import sanity test
- ansible-test now properly searches for ``pythonX.Y`` instead of ``python`` when looking for the real python that created a ``virtualenv``
- ansible-test now properly sets PYTHONPATH for tests when running from an Ansible installation
- ansible-test now properly sets ``ANSIBLE_PLAYBOOK_DIR`` for integration tests so unqualified collection references work for adhoc ``ansible`` usage
- ansible-test now properly uses a fresh copy of environment variables for each command invocation to avoid mixing vars between commands
- ansible-test now shows sanity test doc links when installed (previously the links were only visible when running from source)
- ansible-test now shows the correct source path instead of ``%s`` for collection role based test targets when the ``-v`` option is used
- ansible-test now supports submodules using older ``git`` versions which require querying status from the top level directory of the repo.
- ansible-test now updates SSH keys it generates with newer versions of ssh-keygen to function with Paramiko
- ansible-test now upgrades ``pip`` with `--requirements`` or delegation as needed when the pip version in use is older than version 7.1
- ansible-test now uses GNU tar format instead of the Python default when creating payloads for remote systems
- ansible-test now uses ``pycodestyle`` frozen at version 2.6.0 for consistent test results.
- ansible-test now uses modules from the ``ansible.windows`` collection for setup and teardown of ``windows-integration`` tests and code coverage
- ansible-test once again properly collects code coverage for ``ansible-connection``
- ansible-test units - fixed collection location code to work under pytest >= 6.0.0
- ansible-test validate-modules - Fix arg spec collector for PowerShell to find utils in both a collection and base.
- ansible-test validate-modules - ``version_added`` on module level was not validated for modules in collections (https://github.com/ansible/ansible/pull/70869).
- ansible-test validate-modules - return correct error codes ``option-invalid-version-added`` resp. ``return-invalid-version-added`` instead of the wrong error ``deprecation-either-date-or-version`` when an invalid value of ``version_added`` is specified for an option or a return value (https://github.com/ansible/ansible/pull/70869).
- ansible-test validate-modules sanity test code ``missing-module-utils-import-c#-requirements`` is now ``missing-module-utils-import-csharp-requirements`` (fixes ignore bug).
- ansible-test validate-modules sanity test code ``multiple-c#-utils-per-requires`` is now ``multiple-csharp-utils-per-requires`` (fixes ignore bug).
- ansible-test validate-modules sanity test now checks for AnsibleModule initialization instead of module_utils imports, which did not work in many cases.
- ansible-test validate-modules sanity test now properly handles collections imports using the Ansible collection loader.
- ansible-test validate-modules sanity test now properly handles relative imports.
- ansible-test validate-modules sanity test now properly handles sys.exit in modules.
- ansible-test validate-modules sanity test now properly invokes Ansible modules as scripts.
- ansible-test windows coverage - Ensure coverage reports are UTF-8 encoded without a BOM
- ansible-test windows coverage - Output temp files as UTF-8 with BOM to standardise against non coverage runs
- ansible-vault - Fix ``encrypt_string`` output in a tty when using ``--sdtin-name`` option (https://github.com/ansible/ansible/issues/65121)
- ansible-vault create - Fix exception on no arguments given
- api - time.clock is removed in Python 3.8, add backward compatible code (https://github.com/ansible/ansible/issues/70649).
- apt - Fixed the issue the cache being updated while auto-installing its dependencies even when ``update_cache`` is set to false.
- apt - include exception message from apt python library in error output
- assemble - fix decrypt argument in the module (https://github.com/ansible/ansible/issues/65450).
- assemble module - fix documentation - the remote_src property specified a default value of no but it's actually yes.
- avoid clobbering existing facts inside loop when task also returns ansible_facts.
- avoid fatal traceback when a bad FQCN for a callback is supplied in the whitelist (#69401).
- basic - use PollSelector implementation when DefaultSelector fails (https://github.com/ansible/ansible/issues/70238).
- become - Fix various plugins that still used play_context to get the become password instead of through the plugin - https://github.com/ansible/ansible/issues/62367
- blockinfile - fix regression that results in incorrect block in file when the block to be inserted does not end in a line separator (https://github.com/ansible/ansible/pull/69734)
- blockinfile - preserve line endings on update (https://github.com/ansible/ansible/issues/64966)
- clean_facts - use correct variable to avoid unnecessary handling of ``AttributeError``
- code - removes some Python compatibility code for dealing with socket timeouts in ``wait_for``
- collection loader - ensure Jinja function cache is fully-populated before lookup
- collection loader - fixed relative imports on Python 2.7, ensure pluginloader caches use full name to prevent names from being clobbered (https://github.com/ansible/ansible/pull/60317)
- collection metadata - ensure collection loader uses libyaml/CSafeLoader to parse collection metadata if available
- collection_loader - sort Windows modules below other plugin types so the correct builtin plugin inside a role is selected (https://github.com/ansible/ansible/issues/65298)
- collections - Handle errors better for filters and tests in collections, where a non-existent collection is specified, or importing the plugin results in an exception (https://github.com/ansible/ansible/issues/66721)
- combine filter - ``[dict1, [dict2]] | combine`` now raise an error; previously ``combine`` had an undocumented behaviour where it was flattening the list before combining it (https://github.com/ansible/ansible/pull/57894#discussion_r339517518).
- config - encoding failures on config values should be non-fatal (https://github.com/ansible/ansible/issues/63310)
- copy - Fix copy modes when using remote_src=yes and src is a directory with trailing slash.
- copy - Fixed copy module not working in case that remote_src is enabled and dest ends in a / (https://github.com/ansible/ansible/pull/47238)
- copy - recursive copy with ``remote_src=yes`` now recurses beyond first level. (Fixes https://github.com/ansible/ansible/issues/58284)
- core - remove unneeded Python version checks.
- core - replace a compatibility import of pycompat24.literal_eval with ast.literal_eval.
- core filters - fix ``extract()`` filter when key does not exist in container (https://github.com/ansible/ansible/issues/64957)
- cron - cron file should not be empty after adding var (https://github.com/ansible/ansible/pull/71207)
- cron - encode and decode crontab files in UTF-8 explicitly to allow non-ascii chars in cron filepath and job (https://github.com/ansible/ansible/issues/69492)
- cron and cronvar - use get_bin_path utility to locate the default crontab executable instead of the hardcoded /usr/bin/crontab. (https://github.com/ansible/ansible/pull/59765)
- cron cronvar - only run ``get_bin_path()`` once
- cronvar - use correct binary name (https://github.com/ansible/ansible/issues/63274)
- deal with cases in which just a file is pased and not a path with directories, now fileglob correctly searches in 'files/' subdirs.
- debug - fixed an issue introduced in Ansible 2.4 where a loop of debug tasks would lose the "changed" status on each item.
- discovery will NOT update incorrect host anymore when in delegate_to task.
- display - Improve method of removing extra new line after warnings so it does not break Tower/Runner (https://github.com/ansible/ansible/pull/68517)
- display - remove extra new line after warnings (https://github.com/ansible/ansible/pull/65199)
- display - remove leading space when displaying WARNING messages
- display logging - Fix issue where 3rd party modules will print tracebacks when attempting to log information when ``ANSIBLE_LOG_PATH`` is set - https://github.com/ansible/ansible/issues/65249
- display logging - Fixed up the logging formatter to use the proper prefixes for ``u=user`` and ``p=process``
- display logging - Re-added the ``name`` attribute to the log formatter so that the source of the log can be seen
- dnf - Fix idempotence of `state: installed` (https://github.com/ansible/ansible/issues/64963)
- dnf - Unified error messages when trying to install a nonexistent package with newer dnf (4.2.18) vs older dnf (4.2.9)
- dnf - Unified error messages when trying to remove a wildcard name that is not currently installed, with newer dnf (4.2.18) vs older dnf (4.2.9)
- dnf - enable logging using setup_loggers() API in dnf-4.2.17-6 or later
- dnf - remove custom ``fetch_rpm_from_url`` method in favor of more general ``ansible.module_utils.urls.fetch_file``.
- dnf module - Ensure the modules exit_json['msg'] response is always string, not sometimes a tuple.
- ensure delegated vars can resolve hostvars object and access vars from hostvars[inventory_hostname].
- ensure we pass on interpreter discovery values to delegated host.
- env lookup plugin - Fix handling of environment variables values containing utf-8 characters. (https://github.com/ansible/ansible/issues/65298)
- fact gathering - Display warnings and deprecation messages that are created during the fact gathering phase
- facts - account for Slackware OS with ``+`` in the name (https://github.com/ansible/ansible/issues/38760)
- facts - fix detection of virtualization type when dmi product name is KVM Server
- facts - fix incorrect UTC timestamp in ``iso8601_micro`` and ``iso8601``
- facts - introduce fact "ansible_processor_nproc" which reflects the number of vcpus available to processes (falls back to the number of vcpus available to the scheduler)
- file - Removed unreachable code in module
- file - change ``_diff_peek`` in argument spec to be the correct type, which is ``bool`` (https://github.com/ansible/ansible/issues/59433)
- file - return ``'state': 'absent'`` when a file does not exist (https://github.com/ansible/ansible/issues/66171)
- find - clarify description of ``contains`` (https://github.com/ansible/ansible/issues/61983)
- fix issue in which symlinked collection cannot be listed, though the docs/plugins can be loaded if referenced directly.
- fix issue with inventory_hostname and delegated host vars mixing on connection settings.
- fix wrong command line length calculation in ``ansible-console`` when long command inputted
- for those running uids for invalid users (containers), fallback to uid=<uid> when logging fixes #68007
- fortimanager httpapi plugin - fix redirect to point to the ``fortinet.fortimanager`` collection (https://github.com/ansible/ansible/pull/71073).
- free strategy - Include failed hosts when filtering notified hosts for handlers. The strategy base should determine whether or not to run handlers on those hosts depending on whether forcing handlers is enabled (https://github.com/ansible/ansible/issues/65254).
- galaxy - Fix an AttributeError on ansible-galaxy install with an empty requirements.yml (https://github.com/ansible/ansible/issues/66725).
- get_url - Don't treat no checksum as a checksum match (https://github.com/ansible/ansible/issues/61978)
- get_url pass incorrect If-Modified-Since header (https://github.com/ansible/ansible/issues/67417)
- git - when force=True, apply --force flag to git fetches as well
- gluster modules - fix redirect to point to the ``gluster.gluster`` collection (https://github.com/ansible/ansible/pull/71240).
- group - The group module was not correctly detecting whether a local group is existing or not with local set to yes if the same group exists in a non local group repository e.g. LDAP. (https://github.com/ansible/ansible/issues/58619)
- group_by now should correctly refect changed status.
- hostname - Fixed an issue where the hostname on the cloudlinux 6 server could not be set.
- hostname - make module work on Manjaro Linux (https://github.com/ansible/ansible/issues/61382)
- hurd - Address FIXMEs. Extract functionality and exit early.
- if the ``type`` for a module parameter in the argument spec is callable, do not pass ``kwargs`` to avoid errors (https://github.com/ansible/ansible/issues/70017)
- include_vars - fix stack trace when passing ``dirs`` in an ad-hoc command (https://github.com/ansible/ansible/issues/62633)
- interpreter discovery will now use correct vars (from delegated host) when in delegate_to task.
- junit callback - avoid use of deprecated junit_xml method
- lineinfile - add example of using alternative backrefs syntax (https://github.com/ansible/ansible/issues/42794)
- lineinfile - don't attempt mkdirs when path doesn't contain directory path
- lineinfile - fix bug that caused multiple line insertions (https://github.com/ansible/ansible/issues/58923).
- lineinfile - fix not subscriptable error in exception handling around file creation
- lineinfile - properly handle inserting a line when backrefs are enabled and the line already exists in the file (https://github.com/ansible/ansible/issues/63756)
- lineinfile - use ``module.tmpdir`` to allow configuration of the remote temp directory (https://github.com/ansible/ansible/issues/68218)
- lineinfile - use correct index value when inserting a line at the end of a file (https://github.com/ansible/ansible/issues/63684)
- linux network facts - get the correct value for broadcast address (https://github.com/ansible/ansible/issues/64384)
- loops - Do not indiscriminately mark loop items as unsafe, only apply unsafe to ``with_`` style loops. The items from ``loop`` should not be explicitly wrapped in unsafe. The underlying templating mechanism should dictate this. (https://github.com/ansible/ansible/issues/64379)
- make ``no_log=False`` on a module option silence the ``no_log`` warning (https://github.com/ansible/ansible/issues/49465 https://github.com/ansible/ansible/issues/64656)
- match docs for ssh and ensure pipelining is configurable per connection plugin.
- module executor - Address issue where changes to Ansiballz module code, change the behavior of module execution as it pertains to ``__file__`` and ``sys.modules`` (https://github.com/ansible/ansible/issues/64664)
- module_defaults - support candidate action names for relocated content
- module_defaults - support short group names for content relocated to collections
- native jinja2 types - properly handle Undefined in nested data.
- now correclty merge and not just overwrite facts when gathering using multiple modules.
- objects - Remove FIXME comment because no fix is needed.
- optimize 'smart' detection from being run over and over and preferably do it at config time.
- package_facts - fix value of ``vital`` attribute which is returned when ``pkg`` manager is used
- package_facts - use module warnings rather than a custom implementation for reporting warnings
- packaging_yum - replace legacy file handling with a file manager.
- paramiko - catch and handle exception to prevent stack trace when running in FIPS mode
- paramiko_ssh - Removed redundant conditional statement in ``_parse_proxy_command`` that always evaluated to True.
- paramiko_ssh - improve authentication error message so it is less confusing
- paramiko_ssh - optimized file handling by using a context manager.
- pause - handle exception when there is no stdout (https://github.com/ansible/ansible/pull/47851)
- pip - The virtualenv_command option can now include arguments without requiring the full path to the binary. (https://github.com/ansible/ansible/issues/52275)
- pip - check_mode with ``state: present`` now returns the correct state for pre-release versioned packages
- playbooks - detect and propagate failures in ``always`` blocks after ``rescue`` (https://github.com/ansible/ansible/issues/70000)
- plugins - Allow ensure_type to decrypt the value for string types (and implicit string types) when value is an inline vault.
- powershell - fix escaping of strings that broken modules like fetch when dealing with special chars - https://github.com/ansible/ansible/issues/62781
- powershell - fix the CLIXML parser when it contains nested CLIXML objects - https://github.com/ansible/ansible/issues/69550
- psexec - Fix issue where the Kerberos package was not detected as being available.
- psexec - Fix issue where the ``interactive`` option was not being passed down to the library.
- psrp - Use native PSRP mechanism when copying files to support custom endpoints
- reboot - Add support for the runit init system, used on Void Linux, that does not support the normal Linux syntax.
- reboot, win_reboot - add ``boot_time_command`` parameter to override the default command used to determine whether or not a system was rebooted (https://github.com/ansible/ansible/issues/58868)
- remove update/restore of vars from play_context as it is now redundant.
- replace use of deprecated functions from ``ansible.module_utils.basic``.
- reset logging level to INFO due to CVE-2019-14846.
- roles - Ensure that ``allow_duplicates: true`` enables to run single role multiple times (https://github.com/ansible/ansible/issues/64902)
- runas - Fix the ``runas`` ``become_pass`` variable fallback from ``ansible_runas_runas`` to ``ansible_runas_pass``
- service_facts - Now correctly parses systemd list-unit-files for systemd >=245
- setup - properly detect yum package manager for IBM i.
- setup - service_mgr - detect systemd even if it isn't running, such as during a container build
- shell - fix quoting of mkdir command in creation of remote_tmp in order to allow spaces and other special characters (https://github.com/ansible/ansible/issues/69577).
- shell cmd - Properly escape double quotes in the command argument
- splunk httpapi plugin - switch from splunk.enterprise_security to splunk.es in runtime.yml to reflect upstream change of Collection Name
- ssh connection plugin - use ``get_option()`` rather than ``_play_context`` to ensure ``ANSBILE_SSH_ARGS`` are applied properly (https://github.com/ansible/ansible/issues/70437)
- strftime filter - Input epoch is allowed to be a float (https://github.com/ansible/ansible/issues/71257)
- synchronize - allow data to be passed between two managed nodes when using the docker connection plugin (https://github.com/ansible/ansible/pull/65698)
- synchronize - fix password authentication on Python 2 (https://github.com/ansible/ansible/issues/56629)
- sysctl - Remove FIXME comments to avoid confusion
- systemd - don't require systemd to be running to enable/disable or mask/unmask units
- systemd - fixed chroot usage on new versions of systemd, that broke because of upstream changes in systemctl output
- systemd - made the systemd module work correctly when the SYSTEMD_OFFLINE environment variable is set
- systemd - the module should fail in check_mode when service not found on host (https://github.com/ansible/ansible/pull/68136).
- sysvinit - Add missing parameter ``module`` in call to ``daemonize()``.
- template lookup - ensure changes to the templar in the lookup, do not affect the templar context outside of the lookup (https://github.com/ansible/ansible/issues/60106)
- template lookup - fix regression when templating hostvars (https://github.com/ansible/ansible/issues/63940)
- templating - fix error message for ``x in y`` when y is undefined (https://github.com/ansible/ansible/issues/70984)
- the default parsing will now show existing JSON errors and not just YAML (last attempted), also we avoid YAML parsing when we know we only want JSON issue
- throttle: the linear strategy didn't always stuck with the throttle limit
- unarchive - Remove incorrect and unused function arguments.
- unarchive - check ``fut_gid`` against ``run_gid`` in addition to supplemental groups (https://github.com/ansible/ansible/issues/49284)
- unsafe_proxy - Ensure that data within a tuple is marked as unsafe (https://github.com/ansible/ansible/issues/65722)
- update ``user`` module to support silencing ``no_log`` warnings in the future (see: https://github.com/ansible/ansible/pull/64733)
- uri - Don't return the body even if it failed (https://github.com/ansible/ansible/issues/21003)
- user - allow 13 asterisk characters in password field without warning
- user - don't create home directory and missing parents when create_home == false (https://github.com/ansible/ansible/pull/70600).
- user - fix comprasion on macOS so module does not improperly report a change (https://github.com/ansible/ansible/issues/62969)
- user - fix stack trace on AIX when attempting to parse shadow file that does not exist (https://github.com/ansible/ansible/issues/62510)
- user - on systems using busybox, honor the ``on_changed`` parameter to prevent unnecessary password changing (https://github.com/ansible/ansible/issues/65711)
- user - update docs to reflect proper way to remove account from all groups
- validate-modules - Fix hang when inspecting module with a delegate args spec type
- virtual facts - detect generic container environment based on non-empty "container" env var
- wait_for_connection - with pipelining enabled, interpreter discovery would fail if the first connection attempt was not successful
- win setup - Fix redirection path for the windows setup module
- win_exec_wrapper - Be more defensive when it comes to getting unhandled exceptions
- win_package - Handle quoted and unquoted strings in the registry ``UninstallString`` value - https://github.com/ansible/ansible/issues/40973
- win_uri win_get_url - Fix the behaviour of ``follow_redirects: safe`` to actual redirect on ``GET`` and ``HEAD`` requests - https://github.com/ansible/ansible/issues/65556
- windows async - use full path when calling PowerShell to reduce reliance on environment vars being correct - https://github.com/ansible/ansible/issues/70655
- windows environment - Support env vars that contain the unicode variant of single quotes - https://github.com/ansible-collections/ansible.windows/issues/45
- winrm - preserve winrm forensic data on put_file failures
- yum - fix bug that caused ``enablerepo`` to not be honored when used with disablerepo all wildcard/glob (https://github.com/ansible/ansible/issues/66549)
- yum - fixed the handling of releasever parameter
- yum - performance bugfix, the YumBase object was being  instantiated multiple times unnecessarily, which lead to considerable overhead when operating against large sets of packages.
- yum - yum tasks can no longer end up running non-yum modules
- yum/dnf - check type of elements in a name

amazon.aws
~~~~~~~~~~

- aws_ec2 - fix idempotency when managing tags
- aws_ec2 - fix idempotency when metrics are enable
- aws_s3 - Delete objects and delete markers so versioned buckets can be removed.
- aws_s3 - Try to wait for the bucket to exist before setting the access control list.
- cloudformation_info - Fix a KeyError returning information about the stack(s).
- ec2 module_utils - Ensure boto3 verify parameter isn't overridden by setting a profile (https://github.com/ansible-collections/amazon.aws/issues/129)
- ec2_asg - Ensure "wait" is honored during replace operations
- ec2_launch_template - Update output to include latest_version and default_version, matching the documentation
- ec2_transit_gateway - Use AWSRetry before ClientError is handled when describing transit gateways
- ec2_transit_gateway - fixed issue where auto_attach set to yes was not being honored (https://github.com/ansible/ansible/issues/61907)
- ec2_vol - fix filtering bug
- s3_bucket - Accept XNotImplemented response to support NetApp StorageGRID.
- s3_bucket - Ceph compatibility: treat error code NoSuchTagSetError used by Ceph synonymously to NoSuchTagSet used by AWS

ansible.netcommon
~~~~~~~~~~~~~~~~~

- Fixed "Object of type Capabilities is not JSON serializable" when using default netconf plugin.
- Replace deprecated `getiterator` call with `iter`
- cli_config fixes issue when rollback_id = 0 evalutes to False
- ipaddr - "host" query supports /31 subnets properly
- ipaddr filter - Fixed issue where the first IPv6 address in a subnet was not being considered a valid address.
- ipaddr filter now returns empty list instead of False on empty list input
- net_put - Restore missing function removed when action plugin stopped inheriting NetworkActionBase
- nthhost filter now returns str instead of IPAddress object
- slaac filter now returns str instead of IPAddress object
- sort_list will sort a list of dicts using the sorted method with key as an argument.

ansible.posix
~~~~~~~~~~~~~

- Allow unsetting existing environment vars via environment by specifying a null value (https://github.com/ansible/ansible/pull/68236).
- Fix synchronize to work with renamed docker and buildah connection plugins.
- Mount - Handle remount with new options (https://github.com/ansible/ansible/issues/59460).
- Profile_tasks - result was a odict_items which is not subscriptable, so the slicing was failing (https://github.com/ansible/ansible/issues/59059).
- Revert "mount - Check if src exists before mounted (ansible/ansible#61752)".
- Typecast results before use in profile_tasks callback (https://github.com/ansible/ansible/issues/69563).
- authorized_keys - Added FIDO2 security keys (https://github.com/ansible-collections/ansible.posix/issues/17).
- authorized_keys - fix inconsistent return value for check mode (https://github.com/ansible-collections/ansible.posix/issues/37)
- json callback - Fix host result to task references in the resultant JSON output for non-lockstep strategy plugins such as free (https://github.com/ansible/ansible/issues/65931)
- mount - fix issues with ismount module_util pathing for Ansible 2.9 (fixes https://github.com/ansible-collections/ansible.posix/issues/21)
- patch - fix FQCN usage for action plugin (https://github.com/ansible-collections/ansible.posix/issues/11)
- selinux - add missing configuration keys for /etc/selinux/config (https://github.com/ansible-collections/ansible.posix/issues/23)
- synchronize - fix FQCN usage for action plugin (https://github.com/ansible-collections/ansible.posix/issues/11)

ansible.windows
~~~~~~~~~~~~~~~

- Fix detection of DHCP setting so that resetting to DHCP doesn't cause ``CHANGED`` status on every run. See https://github.com/ansible/ansible/issues/66450
- setup - Remove usage of WMI to speed up execution time and work with standard user accounts
- win_acl - Fixed error when setting rights on directory for which inheritance from parent directory has been disabled.
- win_dns_client - Only configure network adapters that are IP Enabled - https://github.com/ansible/ansible/issues/58958
- win_dsc - Always import module that contains DSC resource to ensure the required assemblies are loaded before parsing it - https://github.com/ansible-collections/ansible.windows/issues/66
- win_find - Fix deduped files mistaken for directories (https://github.com/ansible/ansible/issues/58511)
- win_find - Get-FileStat used [int] instead of [int64] for file size calculations
- win_package - Handle quoted and unquoted strings in the registry ``UninstallString`` value - https://github.com/ansible/ansible/issues/40973
- win_reboot - add ``boot_time_command`` parameter to override the default command used to determine whether or not a system was rebooted (https://github.com/ansible/ansible/issues/58868)
- win_share - Allow for root letters paths
- win_uri win_get_url - Fix the behaviour of ``follow_redirects: safe`` to actual redirect on ``GET`` and ``HEAD`` requests - https://github.com/ansible/ansible/issues/65556

arista.eos
~~~~~~~~~~

- Added error pattern to the terminal plugin to handle change mode error seen in lag interfaces config.
- Fixes mismatch in documentation and code for using eos_lag_interfaces where the code required 'Port-Channel\d.*:' but the docs did not document this. The module now supports both 'Port-Channel\d.*:' and '\d.*:'.
- Make `src`, `backup` and `backup_options` in eos_config work when module alias is used (https://github.com/ansible-collections/arista.eos/pull/85).

cisco.aci
~~~~~~~~~

- Fix sanity issues to support 2.10.0
- Fix some doc issues for a few modules
- Fix some formatting issues (flake8) in unit tests.
- Fixing integration tests and sanity. Tested on ACI 4.2(3l).

cisco.asa
~~~~~~~~~

- Make `src`, `backup` and `backup_options` in asa_config work when module alias is used (https://github.com/ansible-collections/cisco.asa/pull/61).
- Unexpected set of CMDs fired when source and destination were both set to hosts acl (https://github.com/ansible-collections/cisco.asa/pull/69).

cisco.ios
~~~~~~~~~

- Make `src`, `backup` and `backup_options` in ios_config work when module alias is used (https://github.com/ansible-collections/cisco.ios/pull/107).

cisco.iosxr
~~~~~~~~~~~

- Confirmed commit fails with TypeError in IOS XR netconf plugin (https://github.com/ansible-collections/cisco.iosxr/issues/74)
- Make `src`, `backup` and `backup_options` in iosxr_config work when module alias is used (https://github.com/ansible-collections/cisco.iosxr/pull/63).
- Makes sure that docstring and argspec are in sync and removes sanity ignores (https://github.com/ansible-collections/cisco.iosxr/pull/62).
- Update docs after sanity fixes to modules.
- running config data for interface split when substring interface starts with newline

cisco.meraki
~~~~~~~~~~~~

- Remove unnecessary files from the collection package, significantly reduces package size
- meraki_admin - Fix error when adding network privileges to admin using network name
- meraki_switch_stack - Fix situation where module may crash due to switch being in or not in a stack already
- meraki_webhook - Proper response is shown when creating webhook test

cisco.mso
~~~~~~~~~

- Add aliases for backward support of permissions in role module.
- Add integration test for mso_schema_template_db and fix un-needed push to API found by integration test.
- Add login_domain to existing test.
- Add missing tests for VRF settings and changing those settings.
- Add test for specifying read-only roles and increase overall test coverage of mso_user (https://github.com/CiscoDevNet/ansible-mso/pull/77)
- Add test to mso_schema_template_vrf, mso_schema_template_external_epg and mso_schema_template_anp_epg to check for API error when pushing changes to object with existing contract.
- Cleanup unused imports, unused variables and branches and change a variable from ambiguous name to reduce warnings at Ansible Galaxy import
- Consistent object output on domain_associations
- Fix API error when pushing EPG with existing contracts
- Fix EPG / External EPG Contract issue and create test for mso_schema_template_anp_epg_contract and mso_schema_template_external_epg_contract
- Fix contract filter issue and add contract-filter test file
- Fix duplicate user, add admin user to associated user list and update tenant test file
- Fix intersite_multicast_source attribute issue in mso_schema_template_anp_epg and add the proxy_arp argument.
- Fix mso_schema_site_vrf_region_cidr to automatically create VRF and Region if not present at site level
- Fix mso_schema_template_anp_epg idempotancy for both EPG and EPG with contracts
- Fix query condition when VRF or Region do not exist at site level
- Fix role tests to work with pre/post 2.2.4 and re-enable them
- Fix sanity issues to support 2.10.0
- Fix site issue if no site present and fix test issues with MSO v3.0
- Fixing External EPG renaming for 2.9 and later
- Fixing L3MCast test to pass on 2.2.4
- Fixing wrong removal of schemas
- Remove label with test domain before create it
- Remove unused regions attribute from mso_schema_template_vrf
- Send context instead of vrf when vrf parameter is used
- Test hub network module after creating region manually
- Update mso_schema_template_bd.py example for BD in another schema
- Updating Azure site IP in inventory and add second MSO version to inventory

cisco.nxos
~~~~~~~~~~

- Allow facts round trip to work on nxos_vlans (https://github.com/ansible-collections/cisco.nxos/pull/141).
- Element type of `commands` key should be `raw` since it accepts both strings and dicts (https://github.com/ansible-collections/cisco.nxos/pull/126).
- Fix nxos_interfaces states replaced and overridden (https://github.com/ansible-collections/cisco.nxos/pull/102).
- Fixed force option in lag_interfaces.py (https://github.com/ansible-collections/cisco.nxos/pull/111).
- Make `src`, `backup` and `backup_options` in nxos_config work when module alias is used (https://github.com/ansible-collections/cisco.nxos/pull/121).
- Makes sure that docstring and argspec are in sync and removes sanity ignores (https://github.com/ansible-collections/cisco.nxos/pull/112).
- Update docs after sanity fixes to modules.
- nxos_user - do not fail when a custom role is used (https://github.com/ansible-collections/cisco.nxos/pull/130)

community.aws
~~~~~~~~~~~~~

- **security issue** - Convert CLI provided passwords to text initially, to prevent unsafe context being lost when converting from bytes->text during post processing of PlayContext. This prevents CLI provided passwords from being incorrectly templated (CVE-2019-14856)
- **security issue** - Update ``AnsibleUnsafeText`` and ``AnsibleUnsafeBytes`` to maintain unsafe context by overriding ``.encode`` and ``.decode``. This prevents future issues with ``to_text``, ``to_bytes``, or ``to_native`` removing the unsafe wrapper when converting between string types (CVE-2019-14856)
- aws_codecommit - fixes issue where module execution would fail if an existing repository has empty description (https://github.com/ansible-collections/community.aws/pull/195)
- aws_kms_info - fixes issue where module execution fails because certain AWS KMS keys (e.g. aws/acm) do not permit the calling the API kms:GetKeyRotationStatus (example - https://forums.aws.amazon.com/thread.jspa?threadID=312992) (https://github.com/ansible-collections/community.aws/pull/199)
- azure_rm_dnsrecordset_info - no longer returns empty ``azure_dnsrecordset`` facts when called as ``_info`` module.
- azure_rm_resourcegroup_info - no longer returns ``azure_resourcegroups`` facts when called as ``_info`` module.
- azure_rm_storageaccount_info - no longer returns empty ``azure_storageaccounts`` facts when called as ``_info`` module.
- azure_rm_virtualmachineimage_info - no longer returns empty ``azure_vmimages`` facts when called as ``_info`` module.
- azure_rm_virtualmachinescaleset_info - fix wrongly empty result, or ``ansible_facts`` result, when called as ``_info`` module.
- azure_rm_virtualnetwork_info - no longer returns empty ``azure_virtualnetworks`` facts when called as ``_info`` module.
- cloudfront_distribution - Always add field_level_encryption_id to cache behaviour to match AWS requirements
- cloudwatchlogs_log_group - Fix a KeyError when updating a log group that does not have a retention period (https://github.com/ansible/ansible/issues/47945)
- cloudwatchlogs_log_group_info - remove limitation of max 50 results
- ec2_asg - Ensure "wait" is honored during replace operations
- ec2_instance - Fix a bug where tags were updated in check_mode.
- ec2_instance - fixes issue where security groups were not changed if the instance already existed.  https://github.com/ansible-collections/community.aws/pull/22
- ec2_launch_template - Update output to include latest_version and default_version, matching the documentation
- ec2_transit_gateway - Use AWSRetry before ClientError is handled when describing transit gateways
- ec2_transit_gateway - fixed issue where auto_attach set to yes was not being honored (https://github.com/ansible/ansible/issues/61907)
- edgeos_config - fix issue where module would silently filter out encrypted passwords
- fixed issue with sns_topic's delivery_policy option resulting in changed always being true
- iam - Fix false positive warning regarding use of ``no_log`` on ``update_password``
- lineinfile - properly handle inserting a line when backrefs are enabled and the line already exists in the file (https://github.com/ansible/ansible/issues/63756)
- route53 - improve handling of octal encoded characters
- win_credential - Fix issue that errors when trying to add a ``name`` with wildcards.

community.crypto
~~~~~~~~~~~~~~~~

- ACME modules: fix bug in ACME v1 account update code
- ACME modules: make sure some connection errors are handled properly
- ACME modules: support Buypass' ACME v1 endpoint
- acme_certificate - fix crash when module is used with Python 2.x.
- acme_certificate - fix misbehavior when ACME v1 is used with ``modify_account`` set to ``false``.
- acme_inspect - fix problem with Python 3.5 that JSON was not decoded (https://github.com/ansible-collections/community.crypto/issues/86).
- ecs_certificate - Always specify header ``connection: keep-alive`` for ECS API connections.
- ecs_certificate - Fix formatting of contents of ``full_chain_path``.
- get_certificate - Fix cryptography backend when pyopenssl is unavailable (https://github.com/ansible/ansible/issues/67900)
- get_certificate - fix ``ca_cert`` option handling when ``proxy_host`` is used (https://github.com/ansible-collections/community.crypto/pull/84).
- meta/runtime.yml - convert Ansible version numbers for old names of modules to collection version numbers (https://github.com/ansible-collections/community.crypto/pull/108).
- openssh_keypair - add logic to avoid breaking password protected keys.
- openssh_keypair - fixes idempotence issue with public key (https://github.com/ansible/ansible/issues/64969).
- openssh_keypair - public key's file attributes (permissions, owner, group, etc.) are now set to the same values as the private key.
- openssl_* modules - prevent crash on fingerprint determination in FIPS mode (https://github.com/ansible/ansible/issues/67213).
- openssl_*, x509_* modules - fix handling of general names which refer to IP networks and not IP addresses (https://github.com/ansible-collections/community.crypto/pull/92).
- openssl_certificate - When provider is ``entrust``, use a ``connection: keep-alive`` header for ECS API connections.
- openssl_certificate - ``provider`` option was documented as required, but it was not checked whether it was provided. It is now only required when ``state`` is ``present``.
- openssl_certificate - fix ``assertonly`` provider certificate verification, causing 'private key mismatch' and 'subject mismatch' errors.
- openssl_certificate and openssl_csr - fix Ed25519 and Ed448 private key support for ``cryptography`` backend. This probably needs at least cryptography 2.8, since older versions have problems with signing certificates or CSRs with such keys. (https://github.com/ansible/ansible/issues/59039, PR https://github.com/ansible/ansible/pull/63984)
- openssl_csr - a warning is issued if an unsupported value for ``version`` is used for the ``cryptography`` backend.
- openssl_csr - improve handling of IDNA errors (https://github.com/ansible-collections/community.crypto/issues/105).
- openssl_csr - the module will now enforce that ``privatekey_path`` is specified when ``state=present``.
- openssl_publickey - fix a module crash caused when pyOpenSSL is not installed (https://github.com/ansible/ansible/issues/67035).

community.digitalocean
~~~~~~~~~~~~~~~~~~~~~~

- Sanity test documentation fixes (https://github.com/ansible-collections/community.digitalocean/pull/3).
- Update docs examples to use FQCN (https://github.com/ansible-collections/community.digitalocean/issues/14).

community.general
~~~~~~~~~~~~~~~~~

- Convert MD5SUM to lowercase before comparison in maven_artifact module (https://github.com/ansible-collections/community.general/issues/186).
- Fix GitLab modules authentication by handling `python-gitlab` library version >= 1.13.0 (https://github.com/ansible/ansible/issues/64770)
- Fix SSL protocol references in the ``mqtt`` module to prevent failures on Python 2.6.
- Fix the ``xml`` module to use ``list(elem)`` instead of ``elem.getchildren()`` since it is being removed in Python 3.9
- Fix to return XML as a string even for python3 (https://github.com/ansible/ansible/pull/64032).
- Fixes the url handling in lxd_container module that url cannot be specified in lxd environment created by snap.
- Fixes the url handling in lxd_profile module that url cannot be specified in lxd environment created by snap.
- Redact GitLab Project variables which might include sensetive information such as password, api_keys and other project related details.
- Run command in absent state in atomic_image module.
- While deleting gitlab user, name, email and password is no longer required ini gitlab_user module (https://github.com/ansible/ansible/issues/61921).
- airbrake_deployment - Allow deploy notifications for Airbrake compatible v2 api (e.g. Errbit)
- aix_filesystem - fix issues with ismount module_util pathing for Ansible 2.9 (https://github.com/ansible-collections/community.general/pull/567).
- apt_rpm - fix ``package`` type from ``str`` to ``list`` to fix invoking with list of packages (https://github.com/ansible-collections/community.general/issues/143).
- archive - make module compatible with older Ansible versions (https://github.com/ansible-collections/community.general/pull/306).
- become - Fix various plugins that still used play_context to get the become password instead of through the plugin - https://github.com/ansible/ansible/issues/62367
- cloudflare_dns - fix KeyError 'success' (https://github.com/ansible-collections/community.general/issues/236).
- cobbler inventory plugin - ``name`` needed FQCN (https://github.com/ansible-collections/community.general/pull/722).
- consul_kv lookup - fix ``ANSIBLE_CONSUL_URL`` environment variable handling (https://github.com/ansible/ansible/issues/51960).
- consul_kv lookup - fix arguments handling (https://github.com/ansible-collections/community.general/pull/303).
- cronvar - only run ``get_bin_path()`` once
- cronvar - use correct binary name (https://github.com/ansible/ansible/issues/63274)
- cronvar - use get_bin_path utility to locate the default crontab executable instead of the hardcoded /usr/bin/crontab. (https://github.com/ansible/ansible/pull/59765)
- cyberarkpassword - fix invalid attribute access (https://github.com/ansible/ansible/issues/66268)
- datadog_monitor - Corrects ``_update_monitor`` to use ``notification_message`` insteade of deprecated ``message`` (https://github.com/ansible-collections/community.general/pull/389).
- datadog_monitor - added missing ``log alert`` type to ``type`` choices (https://github.com/ansible-collections/community.general/issues/251).
- dense callback - fix plugin access to its configuration variables and remove a warning message (https://github.com/ansible/ansible/issues/64628).
- digital_ocean_droplet - Fix creation of DigitalOcean droplets using digital_ocean_droplet module (https://github.com/ansible/ansible/pull/61655)
- digital_ocean_tag_info - fix crash when querying for an individual tag (https://github.com/ansible-collections/community.general/pull/615).
- doas become plugin - address a bug with the parameters handling that was breaking the plugin in community.general when ``become_flags`` and ``become_user`` were not explicitly specified (https://github.com/ansible-collections/community.general/pull/704).
- docker connection plugin - do not prefix remote path if running on Windows containers.
- docker_compose - add a condition to prevent service startup if parameter ``stopped`` is true. Otherwise, the service will be started on each play and stopped again immediately due to the ``stopped`` parameter and breaks the idempotency of the module (https://github.com/ansible-collections/community.general/issues/532).
- docker_compose - disallow usage of the parameters ``stopped`` and ``restarted`` at the same time. This breaks also the idempotency (https://github.com/ansible-collections/community.general/issues/532).
- docker_compose - fix issue where docker deprecation warning results in ansible erroneously reporting a failure
- docker_container - fix idempotency for IP addresses for networks. The old implementation checked the effective IP addresses assigned by the Docker daemon, and not the specified ones. This causes idempotency issues for containers which are not running, since they have no effective IP addresses assigned.
- docker_container - fix network idempotence comparison error.
- docker_container - improve error behavior when parsing port ranges fails.
- docker_container - make sure that when image is missing, check mode indicates a change (image will be pulled).
- docker_container - passing ``test: [NONE]`` now actually disables the image's healthcheck, as documented.
- docker_container - use Config MacAddress by default instead of Networks. Networks MacAddress is empty in some cases (https://github.com/ansible/ansible/issues/70206).
- docker_container - various error fixes in string handling for Python 2 to avoid crashes when non-ASCII characters are used in strings (https://github.com/ansible-collections/community.general/issues/640).
- docker_container - wait for removal of container if docker API returns early (https://github.com/ansible/ansible/issues/65811).
- docker_image - fix validation of build options.
- docker_image - improve file handling when loading images from disk.
- docker_image - make sure that deprecated options also emit proper deprecation warnings next to warnings which indicate how to replace them.
- docker_login - Use ``with`` statement when accessing files, to prevent that invalid JSON output is produced.
- docker_login - correct broken fix for https://github.com/ansible/ansible/pull/60381 which crashes for Python 3.
- docker_login - fix error handling when ``username`` or ``password`` is not specified when ``state`` is ``present``.
- docker_login - make sure that ``~/.docker/config.json`` is created with permissions ``0600``.
- docker_machine - fallback to ip subcommand output if IPAddress is missing (https://github.com/ansible-collections/community.general/issues/412).
- docker_network - fix idempotence comparison error.
- docker_network - fix idempotency for multiple IPAM configs of the same IP version (https://github.com/ansible/ansible/issues/65815).
- docker_network - validate IPAM config subnet CIDR notation on module setup and not during idempotence checking.
- docker_node_info - improve error handling when service inspection fails, for example because node name being ambiguous (https://github.com/ansible/ansible/issues/63353, PR https://github.com/ansible/ansible/pull/63418).
- docker_swarm - removes ``advertise_addr`` from list of required arguments when ``state`` is ``"join"`` (https://github.com/ansible-collections/community.general/issues/439).
- docker_swarm_service - ``source`` must no longer be specified for ``tmpfs`` mounts.
- docker_swarm_service - fix task always reporting as changed when using ``healthcheck.start_period``.
- docker_swarm_service - passing ``test: [NONE]`` now actually disables the image's healthcheck, as documented.
- dsv lookup - use correct dict usage (https://github.com/ansible-collections/community.general/pull/743).
- dzdo become plugin - address a bug with the parameters handling that was breaking the plugin in community.general when ``become_user`` was not explicitly specified (https://github.com/ansible-collections/community.general/pull/708).
- filesystem - resizefs of xfs filesystems is fixed. Filesystem needs to be mounted.
- firewalld - enable the firewalld module to function offline with firewalld version 0.7.0 and newer (https://github.com/ansible/ansible/issues/63254)
- flatpak and flatpak_remote - fix command line construction to build commands as lists instead of strings.
- gcp_storage_file lookup - die gracefully when the ``google.cloud`` collection is not installed, or changed in an incompatible way.
- github_deploy_key - added support for pagination
- gitlab_user - Fix adding ssh key to new/changed user and adding group membership for new/changed user
- hashi_vault - Fix KV v2 lookup to always return latest version
- hashi_vault - Handle equal sign in key=value (https://github.com/ansible/ansible/issues/55658).
- hashi_vault - error messages are now user friendly and don't contain the secret name ( https://github.com/ansible-collections/community.general/issues/54 )
- hashi_vault - if used via ``with_hashi_vault`` and a list of n secrets to retrieve, only the first one would be retrieved and returned n times.
- hashi_vault - when a non-token authentication method like ldap or userpass failed, but a valid token was loaded anyway (via env or token file), the token was used to attempt authentication, hiding the failure of the requested auth method.
- homebrew - fix Homebrew module's some functions ignored check_mode option (https://github.com/ansible/ansible/pull/65387).
- influxdb_user - Don't grant admin privilege in check mode
- inventory plugins - allow FQCN in ``plugin`` option (https://github.com/ansible-collections/community.general/pull/722).
- ipa modules - fix error when IPA_HOST is empty and fallback on DNS (https://github.com/ansible-collections/community.general/pull/241)
- ipa_hostgroup - fix an issue with load-balanced ipa and cookie handling with Python 3 (https://github.com/ansible-collections/community.general/issues/737).
- java_keystore - make module compatible with older Ansible versions (https://github.com/ansible-collections/community.general/pull/306).
- jenkins_plugin - replace MD5 checksum verification with SHA1 due to MD5 being disabled on systems with FIPS-only algorithms enabled (https://github.com/ansible/ansible/issues/34304).
- jira - improve error message handling (https://github.com/ansible-collections/community.general/pull/311).
- jira - improve error message handling with multiple errors (https://github.com/ansible-collections/community.general/pull/707).
- jira - printing full error message from jira server (https://github.com/ansible-collections/community.general/pull/22).
- jira - transition issue not working (https://github.com/ansible-collections/community.general/issues/109).
- kubevirt - Add aliases 'interface_name' for network_name (https://github.com/ansible/ansible/issues/55641).
- linode inventory plugin - fix parsing of access_token (https://github.com/ansible/ansible/issues/66874)
- manageiq_provider - fix serialization error when running on python3 environment.
- maven_artifact - make module compatible with older Ansible versions (https://github.com/ansible-collections/community.general/pull/306).
- mysql - dont mask ``mysql_connect`` function errors from modules (https://github.com/ansible/ansible/issues/64560).
- mysql_db - fix Broken pipe error appearance when state is import and the target file is compressed (https://github.com/ansible/ansible/issues/20196).
- mysql_db - fix bug in the ``db_import`` function introduced by https://github.com/ansible/ansible/pull/56721 (https://github.com/ansible/ansible/issues/65351).
- mysql_info - add parameter for __collect to get only what are wanted (https://github.com/ansible-collections/community.general/pull/136).
- mysql_replication - allow to pass empty values to parameters (https://github.com/ansible/ansible/issues/23976).
- mysql_user - Fix idempotence when long grant lists are used (https://github.com/ansible/ansible/issues/68044)
- mysql_user - Remove false positive ``no_log`` warning for ``update_password`` option
- mysql_user - add ``INVOKE LAMBDA`` privilege support (https://github.com/ansible-collections/community.general/issues/283).
- mysql_user - fix ``host_all`` arguments conversion string formatting error (https://github.com/ansible/ansible/issues/29644).
- mysql_user - fix support privileges with underscore (https://github.com/ansible/ansible/issues/66974).
- mysql_user - fix the error No database selected (https://github.com/ansible/ansible/issues/68070).
- mysql_user - make sure current_pass_hash is a string before using it in comparison (https://github.com/ansible/ansible/issues/60567).
- mysql_variable - fix the module doesn't support variables name with dot (https://github.com/ansible/ansible/issues/54239).
- nmcli - fix idempotetency when modifying an existing connection (https://github.com/ansible-collections/community.general/issues/481).
- nmcli - typecast parameters to string as required (https://github.com/ansible/ansible/issues/59095).
- nsupdate - Do not try fixing non-existing TXT values (https://github.com/ansible/ansible/issues/63364)
- nsupdate - Fix zone name lookup of internal/private zones (https://github.com/ansible/ansible/issues/62052)
- oc connection plugin - ``transport`` needed FQCN (https://github.com/ansible-collections/community.general/pull/722).
- one_vm - improve file handling by using a context manager.
- osx_defaults - fix handling negative integers (https://github.com/ansible-collections/community.general/issues/134).
- ovirt - don't ignore ``instance_cpus`` parameter
- pacman - Fix pacman output parsing on localized environment. (https://github.com/ansible/ansible/issues/65237)
- pacman - fix module crash with ``IndexError: list index out of range`` (https://github.com/ansible/ansible/issues/63077)
- pacman - treat package names containing .zst as package files during installation (https://www.archlinux.org/news/now-using-zstandard-instead-of-xz-for-package-compression/, https://github.com/ansible-collections/community.general/pull/650).
- pamd - Bugfix for attribute error when removing the first or last line
- parted - added 'undefined' align option to support parted versions < 2.1 (https://github.com/ansible-collections/community.general/pull/405).
- parted - consider current partition state even in check mode (https://github.com/ansible-collections/community.general/issues/183).
- passwordstore lookup - Honor equal sign in userpass
- pbrun become plugin - address a bug with the parameters handling that was breaking the plugin in community.general when ``become_user`` was not explicitly specified (https://github.com/ansible-collections/community.general/pull/708).
- pmrun plugin - The success_command string was no longer quoted. This caused unusual use-cases like ``become_flags=su - root -c`` to fail.
- postgres - use query params with cursor.execute in module_utils.postgres.PgMembership class (https://github.com/ansible/ansible/pull/65164).
- postgres.py - add a new keyword argument ``query_params`` (https://github.com/ansible/ansible/pull/64661).
- postgres_user - Remove false positive ``no_log`` warning for ``no_password_changes`` option
- postgresql_db - Removed exception for 'LibraryError' (https://github.com/ansible/ansible/issues/65223).
- postgresql_db - allow to pass users names which contain dots (https://github.com/ansible/ansible/issues/63204).
- postgresql_idx.py - use the ``query_params`` arg of exec_sql function (https://github.com/ansible/ansible/pull/64661).
- postgresql_lang - use query params with cursor.execute (https://github.com/ansible/ansible/pull/65093).
- postgresql_membership - make the ``groups`` and ``target_roles`` parameters required (https://github.com/ansible/ansible/pull/67046).
- postgresql_membership - remove unused import of exec_sql function (https://github.com/ansible-collections/community.general/pull/178).
- postgresql_owner - use query_params with cursor object (https://github.com/ansible/ansible/pull/65310).
- postgresql_privs - fix crash when set privileges on schema with hyphen in the name (https://github.com/ansible-collections/community.general/issues/656).
- postgresql_privs - fix sorting lists with None elements for python3 (https://github.com/ansible/ansible/issues/65761).
- postgresql_privs - sort results before comparing so that the values are compared and not the result of ``.sort()`` (https://github.com/ansible/ansible/pull/65125)
- postgresql_privs.py - fix reports as changed behavior of module when using ``type=default_privs`` (https://github.com/ansible/ansible/issues/64371).
- postgresql_publication - fix typo in module.warn method name (https://github.com/ansible/ansible/issues/64582).
- postgresql_publication - use query params arg with cursor object (https://github.com/ansible/ansible/issues/65404).
- postgresql_query - improve file handling by using a context manager.
- postgresql_query - the module doesn't support non-ASCII characters in SQL files with Python3 (https://github.com/ansible/ansible/issues/65367).
- postgresql_schema - use query parameters with cursor object (https://github.com/ansible/ansible/pull/65679).
- postgresql_sequence - use query parameters with cursor object (https://github.com/ansible/ansible/pull/65787).
- postgresql_set - allow to pass an empty string to the ``value`` parameter (https://github.com/ansible-collections/community.general/issues/775).
- postgresql_set - fix converting value to uppercase (https://github.com/ansible/ansible/issues/67377).
- postgresql_set - only display a warning about restarts, when restarting is needed (https://github.com/ansible-collections/community.general/pull/651).
- postgresql_set - use query parameters with cursor object (https://github.com/ansible/ansible/pull/65791).
- postgresql_slot - make the ``name`` parameter required (https://github.com/ansible/ansible/pull/67046).
- postgresql_slot - use query parameters with cursor object (https://github.com/ansible/ansible/pull/65791).
- postgresql_subscription - fix typo in module.warn method name (https://github.com/ansible/ansible/pull/64583).
- postgresql_subscription - use query parameters with cursor object (https://github.com/ansible/ansible/pull/65791).
- postgresql_table - use query parameters with cursor object (https://github.com/ansible/ansible/pull/65862).
- postgresql_tablespace - make the ``tablespace`` parameter required (https://github.com/ansible/ansible/pull/67046).
- postgresql_tablespace - use query parameters with cursor object (https://github.com/ansible/ansible/pull/65862).
- postgresql_user - allow to pass user name which contains dots (https://github.com/ansible/ansible/issues/63204).
- postgresql_user - use query parameters with cursor object (https://github.com/ansible/ansible/pull/65862).
- proxmox - fix version detection of proxmox 6 and up (Fixes https://github.com/ansible/ansible/issues/59164)
- proxysql - fixed mysql dictcursor
- pulp_repo - the ``client_cert`` and ``client_key`` options were used for both requests to the Pulp instance and for the repo to sync with, resulting in errors when they were used. Use the new options ``feed_client_cert`` and ``feed_client_key`` for client certificates that should only be used for repo synchronisation, and not for communication with the Pulp instance. (https://github.com/ansible/ansible/issues/59513)
- puppet - fix command line construction for check mode and ``manifest:``
- pure - fix incorrect user_string setting in module_utils file (https://github.com/ansible/ansible/pull/66914)
- redfish_command - fix EnableAccount if Enabled property is not present in Account resource (https://github.com/ansible/ansible/issues/59822)
- redfish_command - fix error when deleting a disabled Redfish account (https://github.com/ansible/ansible/issues/64684)
- redfish_command - fix power ResetType mapping logic (https://github.com/ansible/ansible/issues/59804)
- redfish_config - fix support for boolean bios attrs (https://github.com/ansible/ansible/pull/68251)
- redfish_facts - fix KeyError exceptions in GetLogs (https://github.com/ansible/ansible/issues/59797)
- redfish_info, redfish_config, redfish_command - Fix Redfish response payload decode on Python 3.5 (https://github.com/ansible-collections/community.general/issues/686)
- redhat_subscription - do not set the default quantity to ``1`` when no quantity is provided (https://github.com/ansible/ansible/issues/66478)
- replace use of deprecated functions from ``ansible.module_utils.basic``.
- rshm_repository - reduce execution time when changed is False (https://github.com/ansible-collections/community.general/pull/458).
- runas - Fix the ``runas`` ``become_pass`` variable fallback from ``ansible_runas_runas`` to ``ansible_runas_pass``
- scaleway - Fix bug causing KeyError exception on JSON http requests. (https://github.com/ansible-collections/community.general/pull/444)
- scaleway: use jsonify unmarshaller only for application/json requests to avoid breaking the multiline configuration with requests in text/plain (https://github.com/ansible/ansible/issues/65036)
- scaleway_compute - fix transition handling that could cause errors when removing a node (https://github.com/ansible-collections/community.general/pull/444).
- scaleway_compute(check_image_id): use get image instead loop on first page of images results
- selective - mark task failed correctly (https://github.com/ansible/ansible/issues/63767).
- sesu - make use of the prompt specified in the code
- slack - Fix ``thread_id`` data type
- slackpkg - fix matching some special cases in package names (https://github.com/ansible-collections/community.general/pull/505).
- slackpkg - fix name matching in package installation (https://github.com/ansible-collections/community.general/issues/450).
- snmp_facts - skip ``EndOfMibView`` values (https://github.com/ansible/ansible/issues/49044).
- spacewalk inventory - improve file handling by using a context manager.
- syslog_json callback - fix plugin exception when running (https://github.com/ansible-collections/community.general/issues/407).
- syslogger callback plugin - remove check mode support since it did nothing anyway
- terraform - adding support for absolute paths additionally to the relative path within project_path (https://github.com/ansible/ansible/issues/58578)
- terraform - reset out and err before plan creation (https://github.com/ansible/ansible/issues/64369)
- terraform module - fixes usage for providers not supporting workspaces
- xfconf - make it work in non-english locales (https://github.com/ansible-collections/community.general/pull/744).
- yarn - Return correct values when running yarn in check mode (https://github.com/ansible-collections/community.general/pull/153).
- yarn - fixed an index out of range error when no outdated packages where returned by yarn executable (see https://github.com/ansible-collections/community.general/pull/474).
- yarn - fixed an too many values to unpack error when scoped packages are installed (see https://github.com/ansible-collections/community.general/pull/474).
- yarn - handle no version when installing module by name (https://github.com/ansible/ansible/issues/55097)
- zfs_delegate_admin - add missing choices diff/hold/release to the permissions parameter (https://github.com/ansible-collections/community.general/pull/278)

community.grafana
~~~~~~~~~~~~~~~~~

- Fix an issue in `grafana_dashboard` that made dashboard import no more detecting changes and fail.
- Fix an issue with `grafana_datasource` idempotency
- Fix issue `#45` in `grafana_plugin`
- Refactor module `grafana_datasource` to ease its support.

community.kubernetes
~~~~~~~~~~~~~~~~~~~~

- Fix suboption docs structure for inventory plugins (https://github.com/ansible-collections/community.kubernetes/pull/103).
- Handle invalid kubeconfig parsing error (https://github.com/ansible-collections/community.kubernetes/pull/119).
- Make sure Service changes run correctly in check_mode (https://github.com/ansible-collections/community.kubernetes/pull/84).
- Make sure extra files are not included in built collection (https://github.com/ansible-collections/community.kubernetes/pull/85).
- Test against stable ansible branch so molecule tests work (https://github.com/ansible-collections/community.kubernetes/pull/168).
- Update GitHub Actions workflow for better CI stability (https://github.com/ansible-collections/community.kubernetes/pull/78).
- Update openshift requirements in k8s module doc (https://github.com/ansible-collections/community.kubernetes/pull/153).
- k8s - Add exception handling when retrieving k8s client (https://github.com/ansible-collections/community.kubernetes/pull/54).
- k8s - Fix argspec for 'elements' (https://github.com/ansible-collections/community.kubernetes/issues/13).
- k8s - Use ``from_yaml`` filter with lookup examples in ``k8s`` module documentation examples (https://github.com/ansible-collections/community.kubernetes/pull/56).
- k8s_info - remove unneccessary k8s_facts deprecation notice (https://github.com/ansible-collections/community.kubernetes/pull/97).
- k8s_log - Module no longer attempts to parse log as JSON (https://github.com/ansible-collections/community.kubernetes/pull/69).
- k8s_scale - Fix scale wait and add tests (https://github.com/ansible-collections/community.kubernetes/pull/100).
- k8s_service - Fix argspec (https://github.com/ansible-collections/community.kubernetes/issues/33).
- kubectl - Fix documentation in kubectl connection plugin (https://github.com/ansible-collections/community.kubernetes/pull/52).
- raw - handle condition when definition is none (https://github.com/ansible-collections/community.kubernetes/pull/139).

community.mysql
~~~~~~~~~~~~~~~

- mysql - dont mask ``mysql_connect`` function errors from modules (https://github.com/ansible/ansible/issues/64560).
- mysql_db - fix Broken pipe error appearance when state is import and the target file is compressed (https://github.com/ansible/ansible/issues/20196).
- mysql_db - fix bug in the ``db_import`` function introduced by https://github.com/ansible/ansible/pull/56721 (https://github.com/ansible/ansible/issues/65351).
- mysql_info - add parameter for __collect to get only what are wanted (https://github.com/ansible-collections/community.general/pull/136).
- mysql_replication - allow to pass empty values to parameters (https://github.com/ansible/ansible/issues/23976).
- mysql_user - Fix idempotence when long grant lists are used (https://github.com/ansible/ansible/issues/68044)
- mysql_user - Remove false positive ``no_log`` warning for ``update_password`` option
- mysql_user - add ``INVOKE LAMBDA`` privilege support (https://github.com/ansible-collections/community.general/issues/283).
- mysql_user - add missed privileges to support (https://github.com/ansible-collections/community.general/issues/617).
- mysql_user - fix ``host_all`` arguments conversion string formatting error (https://github.com/ansible/ansible/issues/29644).
- mysql_user - fix overriding password to the same (https://github.com/ansible-collections/community.general/issues/543).
- mysql_user - fix support privileges with underscore (https://github.com/ansible/ansible/issues/66974).
- mysql_user - fix the error No database selected (https://github.com/ansible/ansible/issues/68070).
- mysql_user - make sure current_pass_hash is a string before using it in comparison (https://github.com/ansible/ansible/issues/60567).
- mysql_variable - fix the module doesn't support variables name with dot (https://github.com/ansible/ansible/issues/54239).

community.network
~~~~~~~~~~~~~~~~~

- Cloudengine module_utils - the ``set-id`` (RPC-REPLY XML attribute) may change over the time althougth ``set-id`` is the identity of the next RPC packet.
- Cloudengine netconf plugin - add a dispatch RPC function,just return original RPC-REPLY, the function is used by ``Cloudengine module_utils``.
- Fixes in network action plugins to work in network connection plugin and modules in collection
- Make netconf plugin configurable to set ncclient device handler name in netconf plugin (https://github.com/ansible/ansible/pull/65718)
- Some cloudengine modules have options which should have been removed for Ansible 2.9. see https://github.com/ansible/ansible/issues/67020 and https://github.com/ansible-collections/community.network/pull/68
- Some cloudengine modules were missing ``import __future__`` and ``metaclass``. (https://github.com/ansible/ansible/pull/67634).
- Some cloudengine modules were missing ``import __future__`` and ``metaclass``. (https://github.com/ansible/ansible/pull/67635).
- action/ce - fix a bug, some new version os will not discard uncommitted configure with a return directly.(https://github.com/ansible/ansible/pull/63513).
- ce - Modify exception handling method to make display information more obvious (https://github.com/ansible-collections/community.network/pull/51).
- ce - Modify the way of parsing NETCONF XML message in ce.py (https://github.com/ansible-collections/community.network/pull/39).
- ce_config - fixed issue - Re-building commands(config src) by replacing '#' with 'quit','quit' commands may close connection (https://github.com/ansible/ansible/issues/62872)
- ce_is_is_interface - fix compile error for Python 3.9 (https://github.com/ansible-collections/community.network/pull/36).
- edgeos_config - Added `cat` command to allow display of large files without `less`. Led to a timeout error. (https://github.com/ansible-collections/community.network/issues/79)
- edgeos_config - fix issue where module would silently filter out encrypted passwords
- edgeos_config - fixed issue of handling single quotation marks. Now fails when unmatched (odd numbers)
- edgeos_config - fixed issue where any change in check mode would cause all subsequent tasks to be treated as changes
- edgeos_config - fixed issue where config could be saved while in check mode (https://github.com/ansible-collections/community.network/pull/78)
- edgeos_facts - Added `cat` command to allow display of large files without `less`. Led to a timeout error. (https://github.com/ansible-collections/community.network/issues/79)
- netscaler_nitro_request - use all filters for get_filtered instead of only the first one (https://github.com/ansible-collections/community.network/issues/48).
- plugins-netconf-ce - Fix failed to get version information.
- plugins-netconf-ce - to get attribute 'set-id' from rpc-reply.
- routeros module_utils - created a ``try``/``except`` block on the function ``get_capabilities`` (https://github.com/ansible-collections/community.network/pull/27).
- routeros_facts - Prevent crash of module when ``ipv6`` package is not installed

community.rabbitmq
~~~~~~~~~~~~~~~~~~

- Refactor RabbitMQ user module to first check the version of the daemon and then, when possible add flags to `rabbitmqctl` so that a machine readable  output is returned. Also, depending on the version, parse the output in correctly. Expands tests accordingly. (https://github.com/ansible/ansible/issues/48890)
- rabbitmq lookup plugin - Fix for rabbitmq lookups failing when using pika v1.0.0 and newer.
- rabbitmq_publish - Fix to ensure the module works correctly for pika v1.0.0 and later. (https://github.com/ansible/ansible/pull/61960)

community.vmware
~~~~~~~~~~~~~~~~

- Added 'compose' and 'groups' feature in vmware_vm_inventory plugin.
- Added keyed_groups feature in vmware_vm_inventory plugin.
- Added support to vmware_tag_manager module for specifying tag and category as dict if any of the name contains colon (https://github.com/ansible/ansible/issues/65765).
- Check for virtualNicManager in Esxi host system before accessing properties in vmware_vmkernel_info (https://github.com/ansible/ansible/issues/62772).
- Fixed typo in vmware_guest_powerstate module (https://github.com/ansible/ansible/issues/65161).
- Handle Base64 Binary while JSON serialization in vmware_vm_inventory.
- Handle NoneType error when accessing service system info in vmware_host_service_info module (https://github.com/ansible/ansible/issues/67615).
- Handle list items in vSphere schema while handling facts using to_json API (https://github.com/ansible-collections/vmware/issues/33).
- Handle multiple tags name with different category id in vmware_tag module (https://github.com/ansible/ansible/issues/66340).
- Handle slashes in VMware network name (https://github.com/ansible/ansible/issues/64399).
- In inventory plugin, serialize properties user specifies which are objects as dicts (https://github.com/ansible-collections/vmware/pull/58).
- In vmware_guest_network module use appropriate network while creating or reconfiguring (https://github.com/ansible/ansible/issues/65968).
- Made vmnics attributes optional when creating DVS as they are optional on the API and GUI as well.
- VMware Guest Inventory plugin enhancements and features.
- VMware guest inventory plugin support for filters.
- Vmware Fix for Create overwrites a VM of same name even when the folder is different(https://github.com/ansible/ansible/issues/43161)
- `vmware_content_deploy_template`'s `cluster` argument no longer fails with an error message about resource pools.
- return correct datastore cluster placement recommendations during when adding disk using the vmware_guest_disk module
- vmware - Ensure we can use the modules with Python < 2.7.9 or RHEL/CentOS < 7.4, this as soon as ``validate_certs`` is disabled.
- vmware_category - fix associable datatypes (https://github.com/ansible-collections/vmware/issues/197).
- vmware_content_deploy_ovf_template - fixed issue where wrong resource pool identifier was returned when same resource pool name was used across clusters in the same datacenter (https://github.com/ansible-collections/vmware/pull/363)
- vmware_content_deploy_ovf_template - use datastore_id in deployment_spec (https://github.com/ansible-collections/vmware/pull/287).
- vmware_content_deploy_template - Added param content_library to the main function
- vmware_deploy_ovf - Fixed ova deploy error occur if vm exists
- vmware_dvs_portgroup - Implemented configuration changes on an existing Distributed vSwitch portgroup.
- vmware_dvs_portgroup_find - Cast variable to integer for comparison.
- vmware_dvs_portgroup_find - Fix comparison between str and int on method vlan_match (https://github.com/ansible-collections/vmware/pull/52).
- vmware_guest - Add ability to upgrade the guest hardware version to latest fix issue (https://github.com/ansible/ansible/issues/56273).
- vmware_guest - Allow '-' (Dash) special char in windows DNS name.
- vmware_guest - Exclude dvswitch_name from triggering guest os customization.
- vmware_guest - Updated reference link to vapp_properties property
- vmware_guest - cdrom.controller_number, cdrom.unit_number are handled as integer. (https://github.com/ansible-collections/vmware/issues/274).
- vmware_host_capability_facts - Fixed vSphere API legacy version errors occur in pyvmomi 7.0 and later
- vmware_host_capability_info - Fixed vSphere API legacy version errors occur in pyvmomi 7.0 and later
- vmware_host_facts - handle facts when ESXi hostsystem is poweredoff (https://github.com/ansible-collections/vmware/issues/183).
- vmware_host_firewall_manager - Ensure we can set rule with no ``allowed_hosts`` key (https://github.com/ansible/ansible/issues/61332)
- vmware_host_firewall_manager - Fixed creating IP specific firewall rules with Python 2 (https://github.com/ansible/ansible/issues/67303)
- vmware_host_vmhba_info - fixed node_wwn and port_wwn for FC HBA to hexadecimal format(https://github.com/ansible/ansible/issues/63045).
- vmware_vcenter_settings - Fixed when runtime_settings parameters not defined occur error(https://github.com/ansible/ansible/issues/66713)
- vmware_vcenter_statistics - Fix some corner cases like increasing some interval and decreasing another at the same time.
- vmware_vm_inventory - CustomFieldManager is not present in ESXi, handle this condition (https://github.com/ansible-collections/vmware/issues/269).
- vmware_vm_inventory inventory plugin, use the port value while connecting to vCenter (https://github.com/ansible/ansible/issues/64096).
- vmware_vmkernel - Remove duplicate checks.
- vmware_vmkernel - fixed issue where Repl and ReplNFC services were not being identified as enabled on a vmk interface (https://github.com/ansible-collections/vmware/issues/362).
- vmware_vspan_session - Extract repeated code and reduce complexity of function.

community.windows
~~~~~~~~~~~~~~~~~

- **security issue** win_unzip - normalize paths in archive to ensure extracted files do not escape from the target directory (CVE-2020-1737)
- psexec - Fix issue where the Kerberos package was not detected as being available.
- psexec - Fix issue where the ``interactive`` option was not being passed down to the library.
- win_credential - Fix issue that errors when trying to add a ``name`` with wildcards.
- win_domain_computer - Fix idempotence checks when ``sAMAccountName`` is different from ``name``
- win_domain_computer - Honour the explicit domain server and credentials when moving or removing a computer object - https://github.com/ansible/ansible/pull/63093
- win_domain_user - Better handle cases when getting a new user's groups fail - https://github.com/ansible/ansible/issues/54331
- win_format - Idem not working if file exist but same fs (https://github.com/ansible/ansible/issues/58302)
- win_format - fixed issue where module would not change allocation unit size (https://github.com/ansible/ansible/issues/56961)
- win_iis_webapppool - Do not try and set attributes in check mode when the pool did not exist
- win_iis_website - Actually restart the site when ``state=restarted`` - https://github.com/ansible/ansible/issues/63828
- win_partition - Fix invalid variable name causing a failure on checks - https://github.com/ansible/ansible/issues/62401
- win_partition - don't resize partitions if size difference is < 1 MiB
- win_scoop - add checks for globally installed packages for better idempotency checks
- win_timezone - Allow for _dstoff timezones
- win_unzip - Fix support for paths with square brackets not being detected properly

community.zabbix
~~~~~~~~~~~~~~~~

- all roles - a ``handler`` is configured when ``zabbix_http(s)_proxy`` is defined which will remove the proxy line from the repository files. This results that execution of the roles are not idempotent anymore.
- zabbix_action - allow str values for ``esc_period`` options (see `#66841 <https://github.com/ansible/ansible/pull/66841>`_).
- zabbix_action - choices for the ``inventory`` paramter sub option in ``*operations`` arguments have been clarified to ``manual`` and ``automatic``.
- zabbix_action - documented ``value2`` parameter and ``notify_all_involved`` option.
- zabbix_action - fixed error on changed API fields ``*default_message`` and ``*default_subject`` for Zabbix 5.0 (see `#92 <https://github.com/ansible-collections/community.zabbix/pull/92>`_).
- zabbix_action - module will no longer fail when searching for global script provided to ``script_name`` parameter.
- zabbix_action - no longer requires ``esc_period`` and ``event_source`` arguments when ``state=absent``.
- zabbix_action - now correctly selects mediatype for the (normal|recovery|update) operations with Zabbix 4.4 and newer.
- zabbix_agent - fixed installation of agent on Windows to directories with spaces.
- zabbix_agent - role should no longer fail when looking for ``getenforce`` binary.
- zabbix_host - module will no longer convert context part of user macro to upper case.
- zabbix_host - now supports configuring user macros and host tags on the managed host (see `#66777 <https://github.com/ansible/ansible/pull/66777>`_).
- zabbix_host_info - ``host_name`` based search results now include host groups.
- zabbix_hostmacro - ``macro_name`` now accepts macros in zabbix native format as well (e.g. ``{$MACRO}``).
- zabbix_hostmacro - ``macro_value`` is no longer required when ``state=absent``.
- zabbix_maintenance - changing value of ``description`` parameter now actually updates maintenance's description.
- zabbix_proxy (module) - ``interface`` sub-options ``type`` and ``main`` are now deprecated and will be removed in community.general 3.0.0. Also, the values passed to ``interface`` are now checked for correct types and unexpected keys.
- zabbix_proxy (module) - added option proxy_address for comma-delimited list of IP/CIDR addresses or DNS names to accept active proxy requests from.
- zabbix_proxy (role) - ``StartPreprocessors`` only works with version 4.2 or higher. When a lower version is used, it will not be added to the configuration.
- zabbix_proxy (role) - only install the sql files that needs to be executed for when ``zabbix_repo`` is set to ``epel``.
- zabbix_proxy (role) - will now correctly install python3-libsemanage on RHEL OS family.
- zabbix_server - ``StartPreprocessors`` only works with version 4.2 or higher. When a lower version is used, it will not be added to the configuration.
- zabbix_server - only install the sql files that needs to be executed for when ``zabbix_repo`` is set to ``epel``.
- zabbix_service - fixed the zabbix_service has no idempotency with Zabbix 5.0.
- zabbix_template - add new option omit_date to remove date from exported/dumped template (see `#67302 <https://github.com/ansible/ansible/pull/67302>`_).
- zabbix_template - adding new update rule templateLinkage.deleteMissing for newer zabbix versions (see `#66747 <https://github.com/ansible/ansible/pull/66747>`_).
- zabbix_template - is now able to perform ``state=dump`` when using ``ansible-playbook --check``.
- zabbix_template - no longer imports template from ``template_json`` or ``template_xml`` when using ``ansible-playbook --check``.
- zabbix_template_info - add new option omit_date to remove date from exported/dumped template (see `#67302 <https://github.com/ansible/ansible/pull/67302>`_).
- zabbix_web - now no longer fails when rendering apache vhost template.

containers.podman
~~~~~~~~~~~~~~~~~

- buildah_connection - Fix buildah debug output for py2
- podman_connection - Add check for empty dir for podman connection mount
- podman_connection - Chown file for users when copy them to container
- podman_connection - Increase verbosity for mount failure messages
- podman_connection - Run pause=false w/o message condition
- podman_container - Add idempotency for existing local volumes
- podman_container - Add idempotency for ulimits and tests
- podman_container - Add idempotency for user and stop signal
- podman_container - Add inspect of image and user idempotency
- podman_container - Fix idempotency for case with = in env
- podman_container - Fix idempotency for networks and add tests
- podman_container - Fix idempotency for podman > 2 versions
- podman_container - Fix idempotency issues with workdir and volumes
- podman_container - Fix image, healthcheck and other idempotency
- podman_container - Fix issue with idempotency uts, ipc with pod
- podman_container - Improve idempotency for volumes with slashesAdd idempotency for ulimits and tests
- podman_container - Improve idempotency of podman_container in uts, ipc, networks, cpu_shares
- podman_container - Improve ports idempotency and support UDP
- podman_image - Add option for tls_verify=false for images
- podman_image - only set changed=true if there is a new image
- podman_image - use correct option for remove_signatures flag
- podman_volume_info - Improve podman volume info tests with new module

fortinet.fortios
~~~~~~~~~~~~~~~~

- Add events param to special attributes file(https://github.com/fortinet-solutions-cse/ansible_generator/pull/22)
- Add vpn_ipsec_phase2_interface.proposal into exceptional multilist (https://github.com/fortinet-solutions-cse/ansible_generator/pull/15)
- Fix fgd_alert_subscription multiple choices problem (https://github.com/fortinet-solutions-cse/ansible_generator/pull/14)
- Fix issue 26 of ansible_fgt_modules (https://github.com/fortinet-solutions-cse/ansible_generator/pull/18)
- Module fortios_vpn_ssl_settings -  banned_cipher doesn't work(https://github.com/fortinet-ansible-dev/ansible-galaxy-fortios-collection/issues/10)
- Support special identifier validation and repair (https://github.com/fortinet-solutions-cse/ansible_generator/pull/11)
- Update underscore_to_hyphen function and supported version file (https://github.com/fortinet-solutions-cse/ansible_generator/pull/21)
- Update valid_identifiers.lst (https://github.com/fortinet-solutions-cse/ansible_generator/pull/12)
- facts (https://github.com/fortinet-ansible-dev/fortios-ansible-generator/commit/b2abfaaac1312dd23e6c8e8c243ce24edc33a25c)
- fix issue 24 of ansible_fgt_modules for generator (https://github.com/fortinet-solutions-cse/ansible_generator/pull/19)
- fix the mkey encoding in fortios api URL(https://github.com/fortinet-ansible-dev/ansible-galaxy-fortios-collection/pull/2)
- jsonraw (https://github.com/fortinet-ansible-dev/fortios-ansible-generator/commit/722fa8e8facdddca78e7e1ebc46912540986793e)
- minor fix for feild:required to be consistent with schema definition (https://github.com/fortinet-solutions-cse/ansible_generator/pull/20)
- support revision_change in response since fortigate 6.2.3 (https://github.com/fortinet-solutions-cse/ansible_generator/pull/17)
- vmlicence (https://github.com/fortinet-ansible-dev/fortios-ansible-generator/commit/2180645d8bf008dc4ee1900eb0324c45912bd88d)

frr.frr
~~~~~~~

- Makes sure that docstring and argspec are in sync and removes sanity ignores (https://github.com/ansible-collections/frr.frr/pull/23).
- Update docs after sanity fixes to modules.

hetzner.hcloud
~~~~~~~~~~~~~~

- hcloud inventory plugin - Allow usage of hcloud.yml and hcloud.yaml - this was removed by error within the migration from build-in ansible to our collection

junipernetworks.junos
~~~~~~~~~~~~~~~~~~~~~

- Make `src`, `backup` and `backup_options` in junos_config work when module alias is used (https://github.com/ansible-collections/junipernetworks.junos/pull/83).
- Update docs after sanity fixes to modules.
- set_config called only when state is not gathered so that gathered opeartion works fine (https://github.com/ansible-collections/junipernetworks.junos/issues/89).
- set_config called only when state is not gathered so that gathered opeartion works fine (https://github.com/ansible-collections/junipernetworks.junos/issues/93).
- set_config called only when state is not gathered so that gathered opeartion works fine for l2_interfaces resource module (https://github.com/ansible-collections/junipernetworks.junos/issues/91).

netbox.netbox
~~~~~~~~~~~~~

- Add ``virtual_machine_role=slug`` to ``QUERY_TYPES`` to properly search for Virtual Machine roles and not use the default ``q`` search (https://github.com/netbox-community/ansible_modules/pull/327)
- Add argument specs for every module to validate data passed in. Fixes some idempotency issues. POSSIBLE BREAKING CHANGE (https://github.com/netbox-community/ansible_modules/issues/68)
- Add error handling for invalid key_file for lookup plugin (https://github.com/netbox-community/ansible_modules/issues/52)
- Added ``interfaces`` to ``ALLOWED_QUERY_PARAMS`` for ip addresses searches (https://github.com/netbox-community/ansible_modules/issues/201)
- Added ``type`` to ``ALLOWED_QUERY_PARAMS`` for interface searches (https://github.com/netbox-community/ansible_modules/issues/208)
- Added ``type`` to ``netbox_device_interface`` and deprecation notice for ``form_factor`` (https://github.com/netbox-community/ansible_modules/issues/193)
- Allow endpoint choices to be an integer of the choice rather than attempting to dynamically determine the choice ID (https://github.com/netbox-community/ansible_modules/issues/47)
- Allow integers to be passed in via Jinja string to properly convert back to integer (https://github.com/netbox-community/ansible_modules/issues/45)
- Allow name updates to manufacturers (https://github.com/netbox-community/ansible_modules/issues/76)
- Allow services to be created with a different protocol (https://github.com/netbox-community/ansible_modules/issues/174)
- Allows OR operations in API fitlers for ``nb_lookup`` plugin (https://github.com/netbox-community/ansible_modules/issues/246)
- Assigning to parent log now finds LAG interface type dynamically rather than set statically in code (https://github.com/netbox-community/ansible_modules/issues/106)
- Build the ``rear_port`` and ``rear_port_template`` query_params to properly find rear port (https://github.com/netbox-community/ansible_modules/issues/262)
- Builds slug for netbox_device_type from model which is now required and slug is optional. Model will be slugified if slug is not provided BREAKING CHANGE (https://github.com/netbox-community/ansible_modules/issues/77)
- Compares tags as a set to prevent issues with order difference between user supplied tags and NetBox API (https://github.com/netbox-community/ansible_modules/issues/242)
- Create device with empty string to assign the device a UUID (https://github.com/netbox-community/ansible_modules/issues/107)
- Default ``validate_certs`` to ``True`` (https://github.com/netbox-community/ansible_modules/issues/273)
- Fail module with proper exception when connection to Netbox API cannot be established (https://github.com/netbox-community/ansible_modules/issues/80)
- Fix ``nb_inventory`` cache for ip addresses (https://github.com/netbox-community/ansible_modules/issues/276)
- Fix query_dict for device_bay/interface_template to use ``devicetype_id`` (https://github.com/netbox-community/ansible_modules/issues/282)
- Fixed issue with netbox_vm_interface where it would fail if different virtual machine had the same interface name (https://github.com/netbox-community/ansible_modules/issues/40)
- Fixed vlan searching with vlan_group for netbox_prefix (https://github.com/netbox-community/ansible_modules/issues/85)
- Fixes bug in ``netbox_prefix`` failing when using ``check_mode`` (https://github.com/netbox-community/ansible_modules/issues/228)
- Fixes bug in inventory plugin that fails if there are either no virtual machines, but devices defined in NetBox or vice versa from failing when ``fetch_all`` is set to ``False`` (https://github.com/netbox-community/ansible_modules/issues/214)
- Fixes inventory performance issues, properly shows virtual chassis masters. (https://github.com/netbox-community/ansible_modules/pull/202)
- Fixes typo for ``CONVERT_TO_ID`` mapping in ``netbox_utils`` for ``dcim.powerport`` and ``dcim.poweroutlet`` (https://github.com/netbox-community/ansible_modules/pull/265)
- Fixes typo for ``CONVERT_TO_ID`` mapping in ``netbox_utils`` for ``dcim.rearport`` (https://github.com/netbox-community/ansible_modules/pull/261)
- If interface existed already, caused traceback and crashed playbook (https://github.com/netbox-community/ansible_modules/issues/114)
- If query_filters supplied are not allowed for either device or VM lookups, or no valid query filters, it will not attempt to fetch from devices or VMs. This should prevent devices or VMs from being fetched that do not meet the query_filters specified. (https://github.com/netbox-community/ansible_modules/issues/63)
- Normalize ``mac_address`` to upper case (https://github.com/netbox-community/ansible_modules/issues/254)
- Normalize any string values that are passed in via Jinja into an integer within the `_normalize_data` method (https://github.com/netbox-community/ansible_modules/issues/231)
- Normalize descriptions to remove any extra whitespace (https://github.com/netbox-community/ansible_modules/issues/243)
- Properly create interface on correct device when in a VC (https://github.com/netbox-community/ansible_modules/issues/105)
- Properly find LAG if defined just as a string rather than dictionary with the relevant data (https://github.com/netbox-community/ansible_modules/issues/166)
- Remove ``device`` being ``required`` and implemented ``required_one_of`` to allow either ``device`` or ``virtual_machine`` to be specified for ``netbox_service`` (https://github.com/netbox-community/ansible_modules/pull/326)
- Remove ``rack`` as a choice when creating virtual machines (https://github.com/netbox-community/ansible_modules/pull/221)
- Removed choices within argument_spec for ``mode`` in ``netbox_device_interface`` and ``netbox_vm_interface``. This allows the API to return any error if an invalid choice is selected for ``mode`` (https://github.com/netbox-community/ansible_modules/issues/151)
- Removed static choices from netbox_utils and now pulls the choices for each endpoint from the Netbox API at call time (https://github.com/netbox-community/ansible_modules/issues/67)
- Return HTTPError body output when encountering HTTP errors (https://github.com/netbox-community/ansible_modules/issues/294)
- This expands the fix to all `_template` modules to use `devicetype_id` for the query_dict when attempting to resolve the search (https://github.com/netbox-community/ansible_modules/pull/300)
- Update ``netbox_tenant`` and ``netbox_tenant_group`` to use slugs for searching (available since NetBox 2.6). Added slug options to netbox_site, netbox_tenant, netbox_tenant_group (https://github.com/netbox-community/ansible_modules/pull/120)
- Updated _to_slug to follow same constructs NetBox uses (https://github.com/netbox-community/ansible_modules/issues/95)
- Updated inventory plugin name from netbox.netbox.netbox to netbox.netbox.nb_inventory (https://github.com/netbox-community/ansible_modules/pull/129)
- Updated netbox_ip_address to find interfaces on virtual machines correctly (https://github.com/netbox-community/ansible_modules/issues/40)
- Updated rack width choices for latest NetBox version (https://github.com/netbox-community/ansible_modules/issues/167)
- When tags specified, it prevents other data from being updated on the object. (https://github.com/netbox-community/ansible_modules/pull/325)
- netbox_device_interface Lag no longer has to be a dictionary and the value of the key can be the name of the LAG (https://github.com/netbox-community/ansible_modules/issues/81)
- netbox_ip_address If no address has no CIDR notation, it will convert it into a /32 and pass to Netbox. Fixes idempotency cidr notation is not provided (https://github.com/netbox-community/ansible_modules/issues/78)

ngine_io.vultr
~~~~~~~~~~~~~~

- vultr - Fixed the issue retry max delay param was ignored.

openstack.cloud
~~~~~~~~~~~~~~~

- Fix non existing attribuites in SDK exception
- baremetal_node - Correct parameter name
- coe_cluster - Retrive id/uuid correctly
- federation_mapping - Fixup some minor nits found in followup reviews
- inventory_openstack - Fix constructed compose
- network - Bump minimum openstacksdk version when using os_network/dns_domain
- role_assignment - Fix os_user_role for groups in multidomain context
- role_assignment - Fix os_user_role issue to grant a role in a domain
- security_group_rule - Don't pass tenant_id for remote group
- server_info - Fix broken server_info module and add tests

openvswitch.openvswitch
~~~~~~~~~~~~~~~~~~~~~~~

- Makes sure that docstring and argspec are in sync and removes sanity ignores (https://github.com/ansible-collections/openvswitch.openvswitch/pull/46).
- Update docs after sanity fixes to modules.

ovirt.ovirt
~~~~~~~~~~~

- ovirt_disk - Fix activate (https://github.com/oVirt/ovirt-ansible-collection/pull/61).
- ovirt_host_network - Fix custom_properties default value (https://github.com/oVirt/ovirt-ansible-collection/pull/65).
- ovirt_quota - Fix vcpu_limit (https://github.com/oVirt/ovirt-ansible-collection/pull/44).
- ovirt_snapshot - Disk id was incorrectly set as disk_snapshot_id (https://github.com/oVirt/ovirt-ansible-collection/pull/5).
- ovirt_storage_domain - Fix update_check warning_low_space (https://github.com/oVirt/ovirt-ansible-collection/pull/10).
- ovirt_vm - Fix cd_iso get all disks from storage domains (https://github.com/oVirt/ovirt-ansible-collection/pull/66).
- ovirt_vm - Fix cd_iso search by name (https://github.com/oVirt/ovirt-ansible-collection/pull/51).
- ovirt_vm - Remove deprecated warning of boot params (https://github.com/oVirt/ovirt-ansible-collection/pull/3).

purestorage.flasharray
~~~~~~~~~~~~~~~~~~~~~~

- purefa_host - resolve hostname case inconsistencies
- purefa_host - resolve issue found when using in Pure Storage Test Drive

purestorage.flashblade
~~~~~~~~~~~~~~~~~~~~~~

- purefb_bucket - Add warning message if ``state`` is ``absent`` without ``eradicate:``
- purefb_fs - Add graceful exist when ``state`` is ``absent`` and filesystem not eradicated
- purefb_fs - Add warning message if ``state`` is ``absent`` without ``eradicate``

theforeman.foreman
~~~~~~~~~~~~~~~~~~

- inventory plugin - fix want_params handling (https://github.com/theforeman/foreman-ansible-modules/issues/847)

vyos.vyos
~~~~~~~~~

- Added workaround to avoid set_fact dynamically assigning value. This behavior seems to have been broken after ansible2.9.
- Make `src`, `backup` and `backup_options` in vyos_config work when module alias is used (https://github.com/ansible-collections/vyos.vyos/pull/67).
- vyos_config - fixed issue where config could be saved while in check mode (https://github.com/ansible-collections/vyos.vyos/pull/53)

Known Issues
------------

- Due to a limitation in pip, you cannot ``pip install --upgrade`` from ansible-2.9 or earlier to ansible-2.10 or higher. Instead, you must explicitly use ``pip uninstall ansible`` before pip installing the new version. If you attempt to upgrade Ansible with pip without first uninstalling, the installer warns you to uninstall first.
- The individual collections that make up the ansible-2.10.0 package can be viewed independently. However, they are not currently listed by ansible-galaxy. To view these collections with ansible-galaxy, explicitly specify where ansible has installed the collections -- ``COLLECTION_INSTALL=$(python -c 'import ansible, os.path ; print("%s/../ansible_collections" % os.path.dirname(ansible.__file__))') ansible-galaxy collection list -p "$COLLECTION_INSTALL"``.
- These fortios modules are not automatically redirected from their 2.9.x names to the new 2.10.x names within collections. You must modify your playbooks to use fully qualified collection names for them. You can use the documentation (https://docs.ansible.com/ansible/2.10/collections/fortinet/fortios/) for the ``fortinet.fortios`` collection to determine what the fully qualified collection names are.

  * fortios_address
  * fortios_config
  * fortios_firewall_DoS_policy
  * fortios_firewall_DoS_policy6
  * fortios_ipv4_policy
  * fortios_switch_controller_802_1X_settings
  * fortios_switch_controller_security_policy_802_1X
  * fortios_system_firmware_upgrade
  * fortios_system_nd_proxy
  * fortios_webfilter

community.grafana
~~~~~~~~~~~~~~~~~

- grafana_datasource doesn't set password correctly (#113)

New Plugins
-----------

Become
~~~~~~

- ansible.netcommon.enable - Switch to elevated permissions on a network device

Callback
~~~~~~~~

- community.general.diy - Customize the output

Cliconf
~~~~~~~

- arista.eos.eos - Use eos cliconf to run command on Arista EOS platform
- cisco.asa.asa - Use asa cliconf to run command on Cisco ASA platform
- cisco.ios.ios - Use ios cliconf to run command on Cisco IOS platform
- cisco.iosxr.iosxr - Use iosxr cliconf to run command on Cisco IOS XR platform
- cisco.nxos.nxos - Use NX-OS cliconf to run commands on Cisco NX-OS platform
- dellemc.os10.os10 - Use OS10 cliconf to run commands on Dell EMC PowerSwitch devices.
- frr.frr.frr - Use frr cliconf to run command on Free Range Routing platform
- junipernetworks.junos.junos - Use junos cliconf to run command on Juniper Junos OS platform
- vyos.vyos.vyos - Use vyos cliconf to run command on VyOS platform

Connection
~~~~~~~~~~

- ansible.netcommon.httpapi - Use httpapi to run command on network appliances
- ansible.netcommon.napalm - Provides persistent connection using NAPALM
- ansible.netcommon.netconf - Provides a persistent connection using the netconf protocol
- ansible.netcommon.network_cli - Use network_cli to run command on network appliances
- ansible.netcommon.persistent - Use a persistent unix socket for connection

Httpapi
~~~~~~~

- ansible.netcommon.restconf - HttpApi Plugin for devices supporting Restconf API
- arista.eos.eos - Use eAPI to run command on eos platform
- cisco.nxos.nxos - Use NX-API to run commands on Cisco NX-OS platform

Inventory
~~~~~~~~~

- community.general.cobbler - Cobbler inventory source
- ovirt.ovirt.ovirt - oVirt inventory source

Lookup
~~~~~~

- ansible.builtin.unvault - read vaulted file(s) contents
- community.general.dsv - Get secrets from Thycotic DevOps Secrets Vault
- community.general.etcd3 - Get key values from etcd3 server
- community.general.lmdb_kv - fetch data from LMDB
- community.general.tss - Get secrets from Thycotic Secret Server

Netconf
~~~~~~~

- ansible.netcommon.default - Use default netconf plugin to run standard netconf commands as per RFC
- cisco.iosxr.iosxr - Use iosxr netconf plugin to run netconf commands on Cisco IOSXR platform
- junipernetworks.junos.junos - Use junos netconf plugin to run netconf commands on Juniper JUNOS platform

New Modules
-----------

ansible.netcommon
~~~~~~~~~~~~~~~~~

- ansible.netcommon.cli_command - Run a cli command on cli-based network devices
- ansible.netcommon.cli_config - Push text based configuration to network devices over network_cli
- ansible.netcommon.cli_parse - Parse cli output or text using a variety of parsers
- ansible.netcommon.net_banner - (deprecated, removed after 2022-06-01) Manage multiline banners on network devices
- ansible.netcommon.net_get - Copy a file from a network device to Ansible Controller
- ansible.netcommon.net_interface - (deprecated, removed after 2022-06-01) Manage Interface on network devices
- ansible.netcommon.net_l2_interface - (deprecated, removed after 2022-06-01) Manage Layer-2 interface on network devices
- ansible.netcommon.net_l3_interface - (deprecated, removed after 2022-06-01) Manage L3 interfaces on network devices
- ansible.netcommon.net_linkagg - (deprecated, removed after 2022-06-01) Manage link aggregation groups on network devices
- ansible.netcommon.net_lldp - (deprecated, removed after 2022-06-01) Manage LLDP service configuration on network devices
- ansible.netcommon.net_lldp_interface - (deprecated, removed after 2022-06-01) Manage LLDP interfaces configuration on network devices
- ansible.netcommon.net_logging - (deprecated, removed after 2022-06-01) Manage logging on network devices
- ansible.netcommon.net_ping - Tests reachability using ping from a network device
- ansible.netcommon.net_put - Copy a file from Ansible Controller to a network device
- ansible.netcommon.net_static_route - (deprecated, removed after 2022-06-01) Manage static IP routes on network appliances (routers, switches et. al.)
- ansible.netcommon.net_system - (deprecated, removed after 2022-06-01) Manage the system attributes on network devices
- ansible.netcommon.net_user - (deprecated, removed after 2022-06-01) Manage the aggregate of local users on network device
- ansible.netcommon.net_vlan - (deprecated, removed after 2022-06-01) Manage VLANs on network devices
- ansible.netcommon.net_vrf - (deprecated, removed after 2022-06-01) Manage VRFs on network devices
- ansible.netcommon.netconf_config - netconf device configuration
- ansible.netcommon.netconf_get - Fetch configuration/state data from NETCONF enabled network devices.
- ansible.netcommon.netconf_rpc - Execute operations on NETCONF enabled network devices.
- ansible.netcommon.restconf_config - Handles create, update, read and delete of configuration data on RESTCONF enabled devices.
- ansible.netcommon.restconf_get - Fetch configuration/state data from RESTCONF enabled devices.
- ansible.netcommon.telnet - Executes a low-down and dirty telnet command

ansible.posix
~~~~~~~~~~~~~

- ansible.posix.acl - Set and retrieve file ACL information.
- ansible.posix.at - Schedule the execution of a command or script file via the at command
- ansible.posix.authorized_key - Adds or removes an SSH authorized key
- ansible.posix.mount - Control active and configured mount points
- ansible.posix.patch - Apply patch files using the GNU patch tool
- ansible.posix.seboolean - Toggles SELinux booleans
- ansible.posix.selinux - Change policy and state of SELinux
- ansible.posix.synchronize - A wrapper around rsync to make common tasks in your playbooks quick and easy
- ansible.posix.sysctl - Manage entries in sysctl.conf.

arista.eos
~~~~~~~~~~

- arista.eos.eos_acl_interfaces - ACL interfaces resource module
- arista.eos.eos_acls - ACLs resource module
- arista.eos.eos_banner - Manage multiline banners on Arista EOS devices
- arista.eos.eos_bgp - Configure global BGP protocol settings on Arista EOS.
- arista.eos.eos_command - Run arbitrary commands on an Arista EOS device
- arista.eos.eos_config - Manage Arista EOS configuration sections
- arista.eos.eos_eapi - Manage and configure Arista EOS eAPI.
- arista.eos.eos_facts - Collect facts from remote devices running Arista EOS
- arista.eos.eos_interface - (deprecated, removed after 2022-06-01) Manage Interface on Arista EOS network devices
- arista.eos.eos_interfaces - Interfaces resource module
- arista.eos.eos_l2_interface - (deprecated, removed after 2022-06-01) Manage L2 interfaces on Arista EOS network devices.
- arista.eos.eos_l2_interfaces - L2 interfaces resource module
- arista.eos.eos_l3_interface - (deprecated, removed after 2022-06-01) Manage L3 interfaces on Arista EOS network devices.
- arista.eos.eos_l3_interfaces - L3 interfaces resource module
- arista.eos.eos_lacp - LACP resource module
- arista.eos.eos_lacp_interfaces - LACP interfaces resource module
- arista.eos.eos_lag_interfaces - LAG interfaces resource module
- arista.eos.eos_linkagg - (deprecated, removed after 2022-06-01) Manage link aggregation groups on Arista EOS network devices
- arista.eos.eos_lldp - Manage LLDP configuration on Arista EOS network devices
- arista.eos.eos_lldp_global - LLDP resource module
- arista.eos.eos_lldp_interfaces - LLDP interfaces resource module
- arista.eos.eos_logging - Manage logging on network devices
- arista.eos.eos_ospfv2 - OSPFv2 resource module
- arista.eos.eos_static_route - (deprecated, removed after 2022-06-01) Manage static IP routes on Arista EOS network devices
- arista.eos.eos_static_routes - Static routes resource module
- arista.eos.eos_system - Manage the system attributes on Arista EOS devices
- arista.eos.eos_user - Manage the collection of local users on EOS devices
- arista.eos.eos_vlan - (deprecated, removed after 2022-06-01) Manage VLANs on Arista EOS network devices
- arista.eos.eos_vlans - VLANs resource module
- arista.eos.eos_vrf - Manage VRFs on Arista EOS network devices

cisco.asa
~~~~~~~~~

- cisco.asa.asa_acl - (deprecated, removed after 2022-06-01) Manage access-lists on a Cisco ASA
- cisco.asa.asa_acls - Access-Lists resource module
- cisco.asa.asa_command - Run arbitrary commands on Cisco ASA devices
- cisco.asa.asa_config - Manage configuration sections on Cisco ASA devices
- cisco.asa.asa_facts - Collect facts from remote devices running Cisco ASA
- cisco.asa.asa_og - (deprecated, removed after 2022-06-01) Manage object groups on a Cisco ASA
- cisco.asa.asa_ogs - Object Group resource module

cisco.ios
~~~~~~~~~

- cisco.ios.ios_acl_interfaces - ACL interfaces resource module
- cisco.ios.ios_acls - ACLs resource module
- cisco.ios.ios_banner - Manage multiline banners on Cisco IOS devices
- cisco.ios.ios_bgp - Configure global BGP protocol settings on Cisco IOS.
- cisco.ios.ios_command - Run commands on remote devices running Cisco IOS
- cisco.ios.ios_config - Manage Cisco IOS configuration sections
- cisco.ios.ios_facts - Collect facts from remote devices running Cisco IOS
- cisco.ios.ios_interface - (deprecated, removed after 2022-06-01) Manage Interface on Cisco IOS network devices
- cisco.ios.ios_interfaces - Interfaces resource module
- cisco.ios.ios_l2_interface - (deprecated, removed after 2022-06-01) Manage Layer-2 interface on Cisco IOS devices.
- cisco.ios.ios_l2_interfaces - L2 interfaces resource module
- cisco.ios.ios_l3_interface - (deprecated, removed after 2022-06-01) Manage Layer-3 interfaces on Cisco IOS network devices.
- cisco.ios.ios_l3_interfaces - L3 interfaces resource module
- cisco.ios.ios_lacp - LACP resource module
- cisco.ios.ios_lacp_interfaces - LACP interfaces resource module
- cisco.ios.ios_lag_interfaces - LAG interfaces resource module
- cisco.ios.ios_linkagg - Manage link aggregation groups on Cisco IOS network devices
- cisco.ios.ios_lldp - Manage LLDP configuration on Cisco IOS network devices.
- cisco.ios.ios_lldp_global - LLDP resource module
- cisco.ios.ios_lldp_interfaces - LLDP interfaces resource module
- cisco.ios.ios_logging - Manage logging on network devices
- cisco.ios.ios_ntp - Manages core NTP configuration.
- cisco.ios.ios_ospfv2 - OSPFv2 resource module
- cisco.ios.ios_ping - Tests reachability using ping from Cisco IOS network devices
- cisco.ios.ios_static_route - (deprecated, removed after 2022-06-01) Manage static IP routes on Cisco IOS network devices
- cisco.ios.ios_static_routes - Static routes resource module
- cisco.ios.ios_system - Manage the system attributes on Cisco IOS devices
- cisco.ios.ios_user - Manage the aggregate of local users on Cisco IOS device
- cisco.ios.ios_vlan - (deprecated, removed after 2022-06-01) Manage VLANs on IOS network devices
- cisco.ios.ios_vlans - VLANs resource module
- cisco.ios.ios_vrf - Manage the collection of VRF definitions on Cisco IOS devices

cisco.iosxr
~~~~~~~~~~~

- cisco.iosxr.iosxr_acl_interfaces - ACL interfaces resource module
- cisco.iosxr.iosxr_acls - ACLs resource module
- cisco.iosxr.iosxr_banner - Manage multiline banners on Cisco IOS XR devices
- cisco.iosxr.iosxr_bgp - Configure global BGP protocol settings on Cisco IOS-XR
- cisco.iosxr.iosxr_command - Run commands on remote devices running Cisco IOS XR
- cisco.iosxr.iosxr_config - Manage Cisco IOS XR configuration sections
- cisco.iosxr.iosxr_facts - Get facts about iosxr devices.
- cisco.iosxr.iosxr_interface - (deprecated, removed after 2022-06-01) Manage Interface on Cisco IOS XR network devices
- cisco.iosxr.iosxr_interfaces - Interfaces resource module
- cisco.iosxr.iosxr_l2_interfaces - L2 interfaces resource module
- cisco.iosxr.iosxr_l3_interfaces - L3 interfaces resource module
- cisco.iosxr.iosxr_lacp - LACP resource module
- cisco.iosxr.iosxr_lacp_interfaces - LACP interfaces resource module
- cisco.iosxr.iosxr_lag_interfaces - LAG interfaces resource module
- cisco.iosxr.iosxr_lldp_global - LLDP resource module
- cisco.iosxr.iosxr_lldp_interfaces - LLDP interfaces resource module
- cisco.iosxr.iosxr_logging - Configuration management of system logging services on network devices
- cisco.iosxr.iosxr_netconf - Configures NetConf sub-system service on Cisco IOS-XR devices
- cisco.iosxr.iosxr_ospfv2 - OSPFv2 resource module
- cisco.iosxr.iosxr_static_routes - Static routes resource module
- cisco.iosxr.iosxr_system - Manage the system attributes on Cisco IOS XR devices
- cisco.iosxr.iosxr_user - Manage the aggregate of local users on Cisco IOS XR device

cisco.nxos
~~~~~~~~~~

- cisco.nxos.nxos_aaa_server - Manages AAA server global configuration.
- cisco.nxos.nxos_aaa_server_host - Manages AAA server host-specific configuration.
- cisco.nxos.nxos_acl - (deprecated, removed after 2022-06-01) Manages access list entries for ACLs.
- cisco.nxos.nxos_acl_interface - (deprecated, removed after 2022-06-01) Manages applying ACLs to interfaces.
- cisco.nxos.nxos_acl_interfaces - ACL interfaces resource module
- cisco.nxos.nxos_acls - ACLs resource module
- cisco.nxos.nxos_banner - Manage multiline banners on Cisco NXOS devices
- cisco.nxos.nxos_bfd_global - Bidirectional Forwarding Detection (BFD) global-level configuration
- cisco.nxos.nxos_bfd_interfaces - BFD interfaces resource module
- cisco.nxos.nxos_bgp - Manages BGP configuration.
- cisco.nxos.nxos_bgp_af - Manages BGP Address-family configuration.
- cisco.nxos.nxos_bgp_neighbor - Manages BGP neighbors configurations.
- cisco.nxos.nxos_bgp_neighbor_af - Manages BGP address-family's neighbors configuration.
- cisco.nxos.nxos_command - Run arbitrary command on Cisco NXOS devices
- cisco.nxos.nxos_config - Manage Cisco NXOS configuration sections
- cisco.nxos.nxos_evpn_global - Handles the EVPN control plane for VXLAN.
- cisco.nxos.nxos_evpn_vni - Manages Cisco EVPN VXLAN Network Identifier (VNI).
- cisco.nxos.nxos_facts - Gets facts about NX-OS switches
- cisco.nxos.nxos_feature - Manage features in NX-OS switches.
- cisco.nxos.nxos_file_copy - Copy a file to a remote NXOS device.
- cisco.nxos.nxos_gir - Trigger a graceful removal or insertion (GIR) of the switch.
- cisco.nxos.nxos_gir_profile_management - Create a maintenance-mode or normal-mode profile for GIR.
- cisco.nxos.nxos_hsrp - Manages HSRP configuration on NX-OS switches.
- cisco.nxos.nxos_hsrp_interfaces - HSRP interfaces resource module
- cisco.nxos.nxos_igmp - Manages IGMP global configuration.
- cisco.nxos.nxos_igmp_interface - Manages IGMP interface configuration.
- cisco.nxos.nxos_igmp_snooping - Manages IGMP snooping global configuration.
- cisco.nxos.nxos_install_os - Set boot options like boot, kickstart image and issu.
- cisco.nxos.nxos_interface - (deprecated, removed after 2022-06-01) Manages physical attributes of interfaces.
- cisco.nxos.nxos_interface_ospf - Manages configuration of an OSPF interface instance.
- cisco.nxos.nxos_interfaces - Interfaces resource module
- cisco.nxos.nxos_l2_interface - (deprecated, removed after 2022-06-01) Manage Layer-2 interface on Cisco NXOS devices.
- cisco.nxos.nxos_l2_interfaces - L2 interfaces resource module
- cisco.nxos.nxos_l3_interface - (deprecated, removed after 2022-06-01) Manage L3 interfaces on Cisco NXOS network devices
- cisco.nxos.nxos_l3_interfaces - L3 interfaces resource module
- cisco.nxos.nxos_lacp - LACP resource module
- cisco.nxos.nxos_lacp_interfaces - LACP interfaces resource module
- cisco.nxos.nxos_lag_interfaces - LAG interfaces resource module
- cisco.nxos.nxos_linkagg - (deprecated, removed after 2022-06-01) Manage link aggregation groups on Cisco NXOS devices.
- cisco.nxos.nxos_lldp - (deprecated, removed after 2022-06-01) Manage LLDP configuration on Cisco NXOS network devices.
- cisco.nxos.nxos_lldp_global - LLDP resource module
- cisco.nxos.nxos_lldp_interfaces - LLDP interfaces resource module
- cisco.nxos.nxos_logging - Manage logging on network devices
- cisco.nxos.nxos_ntp - Manages core NTP configuration.
- cisco.nxos.nxos_ntp_auth - Manages NTP authentication.
- cisco.nxos.nxos_ntp_options - Manages NTP options.
- cisco.nxos.nxos_nxapi - Manage NXAPI configuration on an NXOS device.
- cisco.nxos.nxos_ospf - (deprecated, removed after 2022-06-01) Manages configuration of an ospf instance.
- cisco.nxos.nxos_ospf_vrf - Manages a VRF for an OSPF router.
- cisco.nxos.nxos_ospfv2 - OSPFv2 resource module
- cisco.nxos.nxos_overlay_global - Configures anycast gateway MAC of the switch.
- cisco.nxos.nxos_pim - Manages configuration of a PIM instance.
- cisco.nxos.nxos_pim_interface - Manages PIM interface configuration.
- cisco.nxos.nxos_pim_rp_address - Manages configuration of an PIM static RP address instance.
- cisco.nxos.nxos_ping - Tests reachability using ping from Nexus switch.
- cisco.nxos.nxos_reboot - Reboot a network device.
- cisco.nxos.nxos_rollback - Set a checkpoint or rollback to a checkpoint.
- cisco.nxos.nxos_rpm - Install patch or feature rpms on Cisco NX-OS devices.
- cisco.nxos.nxos_smu - Perform SMUs on Cisco NX-OS devices.
- cisco.nxos.nxos_snapshot - Manage snapshots of the running states of selected features.
- cisco.nxos.nxos_snmp_community - Manages SNMP community configs.
- cisco.nxos.nxos_snmp_contact - Manages SNMP contact info.
- cisco.nxos.nxos_snmp_host - Manages SNMP host configuration.
- cisco.nxos.nxos_snmp_location - Manages SNMP location information.
- cisco.nxos.nxos_snmp_traps - Manages SNMP traps.
- cisco.nxos.nxos_snmp_user - Manages SNMP users for monitoring.
- cisco.nxos.nxos_static_route - (deprecated, removed after 2022-06-01) Manages static route configuration
- cisco.nxos.nxos_static_routes - Static routes resource module
- cisco.nxos.nxos_system - Manage the system attributes on Cisco NXOS devices
- cisco.nxos.nxos_telemetry - TELEMETRY resource module
- cisco.nxos.nxos_udld - Manages UDLD global configuration params.
- cisco.nxos.nxos_udld_interface - Manages UDLD interface configuration params.
- cisco.nxos.nxos_user - Manage the collection of local users on Nexus devices
- cisco.nxos.nxos_vlan - (deprecated, removed after 2022-06-01) Manages VLAN resources and attributes.
- cisco.nxos.nxos_vlans - VLANs resource module
- cisco.nxos.nxos_vpc - Manages global VPC configuration
- cisco.nxos.nxos_vpc_interface - Manages interface VPC configuration
- cisco.nxos.nxos_vrf - Manages global VRF configuration.
- cisco.nxos.nxos_vrf_af - Manages VRF AF.
- cisco.nxos.nxos_vrf_interface - Manages interface specific VRF configuration.
- cisco.nxos.nxos_vrrp - Manages VRRP configuration on NX-OS switches.
- cisco.nxos.nxos_vtp_domain - Manages VTP domain configuration.
- cisco.nxos.nxos_vtp_password - Manages VTP password configuration.
- cisco.nxos.nxos_vtp_version - Manages VTP version configuration.
- cisco.nxos.nxos_vxlan_vtep - Manages VXLAN Network Virtualization Endpoint (NVE).
- cisco.nxos.nxos_vxlan_vtep_vni - Creates a Virtual Network Identifier member (VNI)

Storage
^^^^^^^

- cisco.nxos.nxos_devicealias - Configuration of device alias.
- cisco.nxos.nxos_vsan - Configuration of vsan.
- cisco.nxos.nxos_zone_zoneset - Configuration of zone/zoneset.

cloudscale_ch.cloud
~~~~~~~~~~~~~~~~~~~

- cloudscale_ch.cloud.objects_user - Manages objects users on the cloudscale.ch IaaS service

community.aws
~~~~~~~~~~~~~

- community.aws.aws_acm - Upload and delete certificates in the AWS Certificate Manager service
- community.aws.aws_acm_info - Retrieve certificate information from AWS Certificate Manager service
- community.aws.aws_api_gateway - Manage AWS API Gateway APIs
- community.aws.aws_application_scaling_policy - Manage Application Auto Scaling Scaling Policies
- community.aws.aws_batch_compute_environment - Manage AWS Batch Compute Environments
- community.aws.aws_batch_job_definition - Manage AWS Batch Job Definitions
- community.aws.aws_batch_job_queue - Manage AWS Batch Job Queues
- community.aws.aws_codebuild - Create or delete an AWS CodeBuild project
- community.aws.aws_codecommit - Manage repositories in AWS CodeCommit
- community.aws.aws_codepipeline - Create or delete AWS CodePipelines
- community.aws.aws_config_aggregation_authorization - Manage cross-account AWS Config authorizations
- community.aws.aws_config_aggregator - Manage AWS Config aggregations across multiple accounts
- community.aws.aws_config_delivery_channel - Manage AWS Config delivery channels
- community.aws.aws_config_recorder - Manage AWS Config Recorders
- community.aws.aws_config_rule - Manage AWS Config resources
- community.aws.aws_direct_connect_connection - Creates, deletes, modifies a DirectConnect connection
- community.aws.aws_direct_connect_gateway - Manage AWS Direct Connect gateway
- community.aws.aws_direct_connect_link_aggregation_group - Manage Direct Connect LAG bundles
- community.aws.aws_direct_connect_virtual_interface - Manage Direct Connect virtual interfaces
- community.aws.aws_eks_cluster - Manage Elastic Kubernetes Service Clusters
- community.aws.aws_elasticbeanstalk_app - Create, update, and delete an elastic beanstalk application
- community.aws.aws_glue_connection - Manage an AWS Glue connection
- community.aws.aws_glue_job - Manage an AWS Glue job
- community.aws.aws_inspector_target - Create, Update and Delete Amazon Inspector Assessment Targets
- community.aws.aws_kms - Perform various KMS management tasks.
- community.aws.aws_kms_info - Gather information about AWS KMS keys
- community.aws.aws_region_info - Gather information about AWS regions.
- community.aws.aws_s3_bucket_info - Lists S3 buckets in AWS
- community.aws.aws_s3_cors - Manage CORS for S3 buckets in AWS
- community.aws.aws_secret - Manage secrets stored in AWS Secrets Manager.
- community.aws.aws_ses_identity - Manages SES email and domain identity
- community.aws.aws_ses_identity_policy - Manages SES sending authorization policies
- community.aws.aws_ses_rule_set - Manages SES inbound receipt rule sets
- community.aws.aws_sgw_info - Fetch AWS Storage Gateway information
- community.aws.aws_ssm_parameter_store - Manage key-value pairs in aws parameter store.
- community.aws.aws_step_functions_state_machine - Manage AWS Step Functions state machines
- community.aws.aws_step_functions_state_machine_execution - Start or stop execution of an AWS Step Functions state machine.
- community.aws.aws_waf_condition - Create and delete WAF Conditions
- community.aws.aws_waf_info - Retrieve information for WAF ACLs, Rule , Conditions and Filters.
- community.aws.aws_waf_rule - Create and delete WAF Rules
- community.aws.aws_waf_web_acl - Create and delete WAF Web ACLs.
- community.aws.cloudformation_exports_info - Read a value from CloudFormation Exports
- community.aws.cloudformation_stack_set - Manage groups of CloudFormation stacks
- community.aws.cloudfront_distribution - Create, update and delete AWS CloudFront distributions.
- community.aws.cloudfront_info - Obtain facts about an AWS CloudFront distribution
- community.aws.cloudfront_invalidation - create invalidations for AWS CloudFront distributions
- community.aws.cloudfront_origin_access_identity - Create, update and delete origin access identities for a CloudFront distribution
- community.aws.cloudtrail - manage CloudTrail create, delete, update
- community.aws.cloudwatchevent_rule - Manage CloudWatch Event rules and targets
- community.aws.cloudwatchlogs_log_group - create or delete log_group in CloudWatchLogs
- community.aws.cloudwatchlogs_log_group_info - Get information about log_group in CloudWatchLogs
- community.aws.cloudwatchlogs_log_group_metric_filter - Manage CloudWatch log group metric filter
- community.aws.data_pipeline - Create and manage AWS Datapipelines
- community.aws.dms_endpoint - Creates or destroys a data migration services endpoint
- community.aws.dms_replication_subnet_group - creates or destroys a data migration services subnet group
- community.aws.dynamodb_table - Create, update or delete AWS Dynamo DB tables
- community.aws.dynamodb_ttl - Set TTL for a given DynamoDB table
- community.aws.ec2_ami_copy - copies AMI between AWS regions, return new image id
- community.aws.ec2_asg - Create or delete AWS AutoScaling Groups (ASGs)
- community.aws.ec2_asg_info - Gather information about ec2 Auto Scaling Groups (ASGs) in AWS
- community.aws.ec2_asg_lifecycle_hook - Create, delete or update AWS ASG Lifecycle Hooks.
- community.aws.ec2_customer_gateway - Manage an AWS customer gateway
- community.aws.ec2_customer_gateway_info - Gather information about customer gateways in AWS
- community.aws.ec2_eip - manages EC2 elastic IP (EIP) addresses.
- community.aws.ec2_eip_info - List EC2 EIP details
- community.aws.ec2_elb - De-registers or registers instances from EC2 ELBs
- community.aws.ec2_elb_info - Gather information about EC2 Elastic Load Balancers in AWS
- community.aws.ec2_instance - Create & manage EC2 instances
- community.aws.ec2_instance_info - Gather information about ec2 instances in AWS
- community.aws.ec2_launch_template - Manage EC2 launch templates
- community.aws.ec2_lc - Create or delete AWS Autoscaling Launch Configurations
- community.aws.ec2_lc_find - Find AWS Autoscaling Launch Configurations
- community.aws.ec2_lc_info - Gather information about AWS Autoscaling Launch Configurations.
- community.aws.ec2_metric_alarm - Create/update or delete AWS Cloudwatch 'metric alarms'
- community.aws.ec2_placement_group - Create or delete an EC2 Placement Group
- community.aws.ec2_placement_group_info - List EC2 Placement Group(s) details
- community.aws.ec2_scaling_policy - Create or delete AWS scaling policies for Autoscaling groups
- community.aws.ec2_snapshot_copy - Copies an EC2 snapshot and returns the new Snapshot ID.
- community.aws.ec2_transit_gateway - Create and delete AWS Transit Gateways
- community.aws.ec2_transit_gateway_info - Gather information about ec2 transit gateways in AWS
- community.aws.ec2_vpc_egress_igw - Manage an AWS VPC Egress Only Internet gateway
- community.aws.ec2_vpc_endpoint - Create and delete AWS VPC Endpoints.
- community.aws.ec2_vpc_endpoint_info - Retrieves AWS VPC endpoints details using AWS methods.
- community.aws.ec2_vpc_igw - Manage an AWS VPC Internet gateway
- community.aws.ec2_vpc_igw_info - Gather information about internet gateways in AWS
- community.aws.ec2_vpc_nacl - create and delete Network ACLs.
- community.aws.ec2_vpc_nacl_info - Gather information about Network ACLs in an AWS VPC
- community.aws.ec2_vpc_nat_gateway - Manage AWS VPC NAT Gateways.
- community.aws.ec2_vpc_nat_gateway_info - Retrieves AWS VPC Managed Nat Gateway details using AWS methods.
- community.aws.ec2_vpc_peer - create, delete, accept, and reject VPC peering connections between two VPCs.
- community.aws.ec2_vpc_peering_info - Retrieves AWS VPC Peering details using AWS methods.
- community.aws.ec2_vpc_route_table - Manage route tables for AWS virtual private clouds
- community.aws.ec2_vpc_route_table_info - Gather information about ec2 VPC route tables in AWS
- community.aws.ec2_vpc_vgw - Create and delete AWS VPN Virtual Gateways.
- community.aws.ec2_vpc_vgw_info - Gather information about virtual gateways in AWS
- community.aws.ec2_vpc_vpn - Create, modify, and delete EC2 VPN connections.
- community.aws.ec2_vpc_vpn_info - Gather information about VPN Connections in AWS.
- community.aws.ec2_win_password - Gets the default administrator password for ec2 windows instances
- community.aws.ecs_attribute - manage ecs attributes
- community.aws.ecs_cluster - Create or terminate ECS clusters.
- community.aws.ecs_ecr - Manage Elastic Container Registry repositories
- community.aws.ecs_service - Create, terminate, start or stop a service in ECS
- community.aws.ecs_service_info - List or describe services in ECS
- community.aws.ecs_tag - create and remove tags on Amazon ECS resources
- community.aws.ecs_task - Run, start or stop a task in ecs
- community.aws.ecs_taskdefinition - register a task definition in ecs
- community.aws.ecs_taskdefinition_info - Describe a task definition in ECS
- community.aws.efs - create and maintain EFS file systems
- community.aws.efs_info - Get information about Amazon EFS file systems
- community.aws.elasticache - Manage cache clusters in Amazon ElastiCache
- community.aws.elasticache_info - Retrieve information for AWS ElastiCache clusters
- community.aws.elasticache_parameter_group - Manage cache parameter groups in Amazon ElastiCache.
- community.aws.elasticache_snapshot - Manage cache snapshots in Amazon ElastiCache
- community.aws.elasticache_subnet_group - manage ElastiCache subnet groups
- community.aws.elb_application_lb - Manage an Application load balancer
- community.aws.elb_application_lb_info - Gather information about application ELBs in AWS
- community.aws.elb_classic_lb - Creates or destroys Amazon ELB.
- community.aws.elb_classic_lb_info - Gather information about EC2 Elastic Load Balancers in AWS
- community.aws.elb_instance - De-registers or registers instances from EC2 ELBs
- community.aws.elb_network_lb - Manage a Network Load Balancer
- community.aws.elb_target - Manage a target in a target group
- community.aws.elb_target_group - Manage a target group for an Application or Network load balancer
- community.aws.elb_target_group_info - Gather information about ELB target groups in AWS
- community.aws.elb_target_info - Gathers which target groups a target is associated with.
- community.aws.execute_lambda - Execute an AWS Lambda function
- community.aws.iam - Manage IAM users, groups, roles and keys
- community.aws.iam_cert - Manage server certificates for use on ELBs and CloudFront
- community.aws.iam_group - Manage AWS IAM groups
- community.aws.iam_managed_policy - Manage User Managed IAM policies
- community.aws.iam_mfa_device_info - List the MFA (Multi-Factor Authentication) devices registered for a user
- community.aws.iam_password_policy - Update an IAM Password Policy
- community.aws.iam_policy - Manage inline IAM policies for users, groups, and roles
- community.aws.iam_policy_info - Retrieve inline IAM policies for users, groups, and roles
- community.aws.iam_role - Manage AWS IAM roles
- community.aws.iam_role_info - Gather information on IAM roles
- community.aws.iam_saml_federation - Maintain IAM SAML federation configuration.
- community.aws.iam_server_certificate_info - Retrieve the information of a server certificate
- community.aws.iam_user - Manage AWS IAM users
- community.aws.iam_user_info - Gather IAM user(s) facts in AWS
- community.aws.kinesis_stream - Manage a Kinesis Stream.
- community.aws.lambda - Manage AWS Lambda functions
- community.aws.lambda_alias - Creates, updates or deletes AWS Lambda function aliases
- community.aws.lambda_event - Creates, updates or deletes AWS Lambda function event mappings
- community.aws.lambda_facts - Gathers AWS Lambda function details as Ansible facts
- community.aws.lambda_info - Gathers AWS Lambda function details
- community.aws.lambda_policy - Creates, updates or deletes AWS Lambda policy statements.
- community.aws.lightsail - Manage instances in AWS Lightsail
- community.aws.rds - create, delete, or modify Amazon rds instances, rds snapshots, and related facts
- community.aws.rds_instance - Manage RDS instances
- community.aws.rds_instance_info - obtain information about one or more RDS instances
- community.aws.rds_param_group - manage RDS parameter groups
- community.aws.rds_snapshot - manage Amazon RDS snapshots.
- community.aws.rds_snapshot_info - obtain information about one or more RDS snapshots
- community.aws.rds_subnet_group - manage RDS database subnet groups
- community.aws.redshift_cross_region_snapshots - Manage Redshift Cross Region Snapshots
- community.aws.redshift_info - Gather information about Redshift cluster(s)
- community.aws.route53 - add or delete entries in Amazons Route53 DNS service
- community.aws.route53_health_check - Add or delete health-checks in Amazons Route53 DNS service
- community.aws.route53_info - Retrieves route53 details using AWS methods
- community.aws.route53_zone - add or delete Route53 zones
- community.aws.s3_bucket_notification - Creates, updates or deletes S3 Bucket notification for lambda
- community.aws.s3_lifecycle - Manage s3 bucket lifecycle rules in AWS
- community.aws.s3_logging - Manage logging facility of an s3 bucket in AWS
- community.aws.s3_sync - Efficiently upload multiple files to S3
- community.aws.s3_website - Configure an s3 bucket as a website
- community.aws.sns - Send Amazon Simple Notification Service messages
- community.aws.sns_topic - Manages AWS SNS topics and subscriptions
- community.aws.sqs_queue - Creates or deletes AWS SQS queues.
- community.aws.sts_assume_role - Assume a role using AWS Security Token Service and obtain temporary credentials
- community.aws.sts_session_token - Obtain a session token from the AWS Security Token Service

community.crypto
~~~~~~~~~~~~~~~~

- community.crypto.ecs_domain - Request validation of a domain with the Entrust Certificate Services (ECS) API
- community.crypto.openssl_signature - Sign data with openssl
- community.crypto.openssl_signature_info - Verify signatures with openssl
- community.crypto.x509_crl - Generate Certificate Revocation Lists (CRLs)
- community.crypto.x509_crl_info - Retrieve information on Certificate Revocation Lists (CRLs)

community.general
~~~~~~~~~~~~~~~~~

Cloud
^^^^^

Docker
......

- community.general.docker_stack_info - Return information on a docker stack
- community.general.docker_stack_task_info - Return information of the tasks on a docker stack

Huawei
......

- community.general.hwc_ecs_instance - Creates a resource of Ecs/Instance in Huawei Cloud
- community.general.hwc_evs_disk - Creates a resource of Evs/Disk in Huawei Cloud
- community.general.hwc_vpc_eip - Creates a resource of Vpc/EIP in Huawei Cloud
- community.general.hwc_vpc_peering_connect - Creates a resource of Vpc/PeeringConnect in Huawei Cloud
- community.general.hwc_vpc_port - Creates a resource of Vpc/Port in Huawei Cloud
- community.general.hwc_vpc_private_ip - Creates a resource of Vpc/PrivateIP in Huawei Cloud
- community.general.hwc_vpc_route - Creates a resource of Vpc/Route in Huawei Cloud
- community.general.hwc_vpc_security_group - Creates a resource of Vpc/SecurityGroup in Huawei Cloud
- community.general.hwc_vpc_security_group_rule - Creates a resource of Vpc/SecurityGroupRule in Huawei Cloud
- community.general.hwc_vpc_subnet - Creates a resource of Vpc/Subnet in Huawei Cloud

Ovh
...

- community.general.ovh_monthly_billing - Manage OVH monthly billing

Packet
......

- community.general.packet_ip_subnet - Assign IP subnet to a bare metal server.
- community.general.packet_project - Create/delete a project in Packet host.
- community.general.packet_volume - Create/delete a volume in Packet host.
- community.general.packet_volume_attachment - Attach/detach a volume to a device in the Packet host.

Database
^^^^^^^^

Misc
....

- community.general.odbc - Execute SQL via ODBC
- community.general.redis_info - Gather information about Redis servers

Mysql
.....

- community.general.mysql_query - Run MySQL queries

Postgresql
..........

- community.general.postgresql_subscription - Add, update, or remove PostgreSQL subscription
- community.general.postgresql_user_obj_stat_info - Gather statistics about PostgreSQL user objects

Files
^^^^^

- community.general.iso_create - Generate ISO file with specified files or folders

Net Tools
^^^^^^^^^

- community.general.hetzner_firewall - Manage Hetzner's dedicated server firewall
- community.general.hetzner_firewall_info - Manage Hetzner's dedicated server firewall
- community.general.ipwcli_dns - Manage DNS Records for Ericsson IPWorks via ipwcli

Ldap
....

- community.general.ldap_attrs - Add or remove multiple LDAP attribute values
- community.general.ldap_search - Search for entries in a LDAP server

Packaging
^^^^^^^^^

Os
..

- community.general.mas - Manage Mac App Store applications with mas-cli

System
^^^^^^

- community.general.dpkg_divert - Override a debian package's version of a file
- community.general.iptables_state - Save iptables state into a file or restore it from a file
- community.general.launchd - Manage macOS services
- community.general.lbu - Local Backup Utility for Alpine Linux
- community.general.shutdown - Shut down a machine
- community.general.sysupgrade - Manage OpenBSD system upgrades

community.kubernetes
~~~~~~~~~~~~~~~~~~~~

- community.kubernetes.helm - Manages Kubernetes packages with the Helm package manager
- community.kubernetes.helm_info - Get information from Helm package deployed inside the cluster
- community.kubernetes.helm_plugin - Manage Helm plugins
- community.kubernetes.helm_plugin_info - Gather information about Helm plugins
- community.kubernetes.helm_repository - Add and remove Helm repository
- community.kubernetes.k8s_exec - Execute command in Pod
- community.kubernetes.k8s_log - Fetch logs from Kubernetes resources

community.mongodb
~~~~~~~~~~~~~~~~~

- community.mongodb.mongodb_balancer - Manages the MongoDB Sharded Cluster Balancer.
- community.mongodb.mongodb_index - Creates or drops indexes on MongoDB collections.
- community.mongodb.mongodb_info - Gather information about MongoDB instance.
- community.mongodb.mongodb_maintenance - Enables or disables maintnenance mode for a secondary member.
- community.mongodb.mongodb_oplog - Resizes the MongoDB oplog.
- community.mongodb.mongodb_parameter - Change an administrative parameter on a MongoDB server
- community.mongodb.mongodb_replicaset - Initialises a MongoDB replicaset.
- community.mongodb.mongodb_shard - Add or remove shards from a MongoDB Cluster
- community.mongodb.mongodb_shutdown - Cleans up all database resources and then terminates the process.
- community.mongodb.mongodb_status - Validates the status of the cluster.
- community.mongodb.mongodb_stepdown - Step down the MongoDB node from a PRIMARY state.
- community.mongodb.mongodb_user - Adds or removes a user from a MongoDB database

community.network
~~~~~~~~~~~~~~~~~

Network
^^^^^^^

Apconos
.......

- community.network.apconos_command - Run arbitrary commands on APCON devices

Cloudengine
...........

- community.network.ce_is_is_instance - Manages isis process id configuration on HUAWEI CloudEngine devices.
- community.network.ce_is_is_interface - Manages isis interface configuration on HUAWEI CloudEngine devices.
- community.network.ce_is_is_view - Manages isis view configuration on HUAWEI CloudEngine devices.
- community.network.ce_lacp - Manages Eth-Trunk interfaces on HUAWEI CloudEngine switches
- community.network.ce_lldp - Manages LLDP configuration on HUAWEI CloudEngine switches.
- community.network.ce_lldp_interface - Manages INTERFACE LLDP configuration on HUAWEI CloudEngine switches.
- community.network.ce_mdn_interface - Manages MDN configuration on HUAWEI CloudEngine switches.
- community.network.ce_multicast_global - Manages multicast global configuration on HUAWEI CloudEngine switches.
- community.network.ce_multicast_igmp_enable - Manages multicast igmp enable configuration on HUAWEI CloudEngine switches.
- community.network.ce_static_route_bfd - Manages static route configuration on HUAWEI CloudEngine switches.

Exos
....

- community.network.exos_l2_interfaces - Manage L2 interfaces on Extreme Networks EXOS devices.
- community.network.exos_lldp_interfaces - Manage link layer discovery protocol (LLDP) attributes of interfaces on EXOS platforms.
- community.network.exos_vlans - Manage VLANs on Extreme Networks EXOS devices.

Onyx
....

- community.network.onyx_aaa - Configures AAA parameters
- community.network.onyx_bfd - Configures BFD parameters
- community.network.onyx_ntp - Manage NTP general configurations and ntp keys configurations on Mellanox ONYX network devices
- community.network.onyx_ntp_servers_peers - Configures NTP peers and servers parameters
- community.network.onyx_snmp - Manages SNMP general configurations on Mellanox ONYX network devices
- community.network.onyx_snmp_hosts - Configures SNMP host parameters
- community.network.onyx_snmp_users - Configures SNMP User parameters
- community.network.onyx_syslog_files - Configure file management syslog module
- community.network.onyx_syslog_remote - Configure remote syslog module
- community.network.onyx_username - Configure username module

Routeros
........

- community.network.routeros_api - Ansible module for RouterOS API

community.windows
~~~~~~~~~~~~~~~~~

- community.windows.win_scoop_bucket - Manage Scoop buckets

community.zabbix
~~~~~~~~~~~~~~~~

- community.zabbix.zabbix_discovery_rule - Manage Zabbix discovery rules
- community.zabbix.zabbix_usergroup - Manage Zabbix user groups

containers.podman
~~~~~~~~~~~~~~~~~

- containers.podman.podman_container - Manage Podman containers
- containers.podman.podman_network_info module - Retrieve information about Podman networks
- containers.podman.podman_pod - Manage Podman pods
- containers.podman.podman_pod_info - Retrieve information about Podman pods
- containers.podman.podman_volume - Manage Podman volumes

dellemc.os10
~~~~~~~~~~~~

- dellemc.os10.os10_command - Run commands on devices running Dell EMC SmartFabric OS1O.
- dellemc.os10.os10_config - Manage configuration on devices running OS10.
- dellemc.os10.os10_facts - Collect facts from devices running OS10.

dellemc.os6
~~~~~~~~~~~

- dellemc.os6.os6_command - Run commands on devices running Dell EMC os6.
- dellemc.os6.os6_config - Manage configuration on devices running os6.
- dellemc.os6.os6_facts - Collect facts from devices running os6.

dellemc.os9
~~~~~~~~~~~

- dellemc.os9.os9_command - Run commands on devices running Dell EMC os9.
- dellemc.os9.os9_config - Manage configuration on devices running os9.
- dellemc.os9.os9_facts - Collect facts from devices running os9.

fortinet.fortimanager
~~~~~~~~~~~~~~~~~~~~~

- fortinet.fortimanager.fmgr_antivirus_profile - Configure AntiVirus profiles.
- fortinet.fortimanager.fmgr_antivirus_profile_obj - Configure AntiVirus profiles.
- fortinet.fortimanager.fmgr_application_list - Configure application control lists.
- fortinet.fortimanager.fmgr_application_list_obj - Configure application control lists.
- fortinet.fortimanager.fmgr_devprof_device_profile_fortianalyzer - no description
- fortinet.fortimanager.fmgr_devprof_device_profile_fortiguard - no description
- fortinet.fortimanager.fmgr_devprof_log_syslogd_filter - Filters for remote system server.
- fortinet.fortimanager.fmgr_devprof_log_syslogd_setting - Global settings for remote syslog server.
- fortinet.fortimanager.fmgr_devprof_system_centralmanagement - Configure central management.
- fortinet.fortimanager.fmgr_devprof_system_dns - Configure DNS.
- fortinet.fortimanager.fmgr_devprof_system_emailserver - Configure the email server used by the FortiGate various things. For example, for sending email messages to users to support user authen...
- fortinet.fortimanager.fmgr_devprof_system_global - Configure global attributes.
- fortinet.fortimanager.fmgr_devprof_system_ntp - Configure system NTP information.
- fortinet.fortimanager.fmgr_devprof_system_snmp_community - SNMP community configuration.
- fortinet.fortimanager.fmgr_devprof_system_snmp_community_obj - SNMP community configuration.
- fortinet.fortimanager.fmgr_devprof_system_snmp_sysinfo - SNMP system info configuration.
- fortinet.fortimanager.fmgr_devprof_system_snmp_user - SNMP user configuration.
- fortinet.fortimanager.fmgr_devprof_system_snmp_user_obj - SNMP user configuration.
- fortinet.fortimanager.fmgr_dnsfilter_profile - Configure DNS domain filter profiles.
- fortinet.fortimanager.fmgr_dnsfilter_profile_obj - Configure DNS domain filter profiles.
- fortinet.fortimanager.fmgr_dvm_cmd_add_device - Add a device to the Device Manager database.
- fortinet.fortimanager.fmgr_dvm_cmd_del_device - Delete a device.
- fortinet.fortimanager.fmgr_dvm_cmd_discover_device - Probe a remote device and retrieve its device information and system status.
- fortinet.fortimanager.fmgr_dvm_cmd_update_device - Refresh the FGFM connection and system information of a device.
- fortinet.fortimanager.fmgr_dvmdb_device - Device table, most attributes are read-only and can only be changed internally. Refer to Device Manager Command module for API to add, d...
- fortinet.fortimanager.fmgr_dvmdb_device_obj - Device table, most attributes are read-only and can only be changed internally. Refer to Device Manager Command module for API to add, d...
- fortinet.fortimanager.fmgr_dvmdb_group - Device group table.
- fortinet.fortimanager.fmgr_dvmdb_group_obj - Device group table.
- fortinet.fortimanager.fmgr_dvmdb_script - Script table.
- fortinet.fortimanager.fmgr_dvmdb_script_execute - Run script.
- fortinet.fortimanager.fmgr_dvmdb_script_obj - Script table.
- fortinet.fortimanager.fmgr_firewall_address - Configure IPv4 addresses.
- fortinet.fortimanager.fmgr_firewall_address6 - Configure IPv6 firewall addresses.
- fortinet.fortimanager.fmgr_firewall_address6_obj - Configure IPv6 firewall addresses.
- fortinet.fortimanager.fmgr_firewall_address_obj - Configure IPv4 addresses.
- fortinet.fortimanager.fmgr_firewall_addrgrp - Configure IPv4 address groups.
- fortinet.fortimanager.fmgr_firewall_addrgrp6 - Configure IPv6 address groups.
- fortinet.fortimanager.fmgr_firewall_addrgrp6_obj - Configure IPv6 address groups.
- fortinet.fortimanager.fmgr_firewall_addrgrp_obj - Configure IPv4 address groups.
- fortinet.fortimanager.fmgr_firewall_ippool - Configure IPv4 IP pools.
- fortinet.fortimanager.fmgr_firewall_ippool6 - Configure IPv6 IP pools.
- fortinet.fortimanager.fmgr_firewall_ippool6_obj - Configure IPv6 IP pools.
- fortinet.fortimanager.fmgr_firewall_ippool_obj - Configure IPv4 IP pools.
- fortinet.fortimanager.fmgr_firewall_multicastaddress - Configure multicast addresses.
- fortinet.fortimanager.fmgr_firewall_multicastaddress_obj - Configure multicast addresses.
- fortinet.fortimanager.fmgr_firewall_profilegroup - Configure profile groups.
- fortinet.fortimanager.fmgr_firewall_profilegroup_obj - Configure profile groups.
- fortinet.fortimanager.fmgr_firewall_service_category - Configure service categories.
- fortinet.fortimanager.fmgr_firewall_service_category_obj - Configure service categories.
- fortinet.fortimanager.fmgr_firewall_service_custom - Configure custom services.
- fortinet.fortimanager.fmgr_firewall_service_custom_obj - Configure custom services.
- fortinet.fortimanager.fmgr_firewall_service_group - Configure service groups.
- fortinet.fortimanager.fmgr_firewall_service_group_obj - Configure service groups.
- fortinet.fortimanager.fmgr_firewall_sslsshprofile - Configure SSL/SSH protocol options.
- fortinet.fortimanager.fmgr_firewall_sslsshprofile_obj - Configure SSL/SSH protocol options.
- fortinet.fortimanager.fmgr_firewall_vip - Configure virtual IP for IPv4.
- fortinet.fortimanager.fmgr_firewall_vip_obj - Configure virtual IP for IPv4.
- fortinet.fortimanager.fmgr_ips_sensor - Configure IPS sensor.
- fortinet.fortimanager.fmgr_ips_sensor_obj - Configure IPS sensor.
- fortinet.fortimanager.fmgr_pkg_firewall_policy - Configure IPv4 policies.
- fortinet.fortimanager.fmgr_pkg_firewall_policy_obj - Configure IPv4 policies.
- fortinet.fortimanager.fmgr_pm_devprof_adom_obj - no description
- fortinet.fortimanager.fmgr_pm_devprof_obj - no description
- fortinet.fortimanager.fmgr_pm_pkg_adom_obj - no description
- fortinet.fortimanager.fmgr_pm_pkg_obj - no description
- fortinet.fortimanager.fmgr_securityconsole_install_device - no description
- fortinet.fortimanager.fmgr_securityconsole_install_package - Copy and install a policy package to devices.
- fortinet.fortimanager.fmgr_spamfilter_profile - Configure AntiSpam profiles.
- fortinet.fortimanager.fmgr_spamfilter_profile_obj - Configure AntiSpam profiles.
- fortinet.fortimanager.fmgr_system_global - Global range attributes.
- fortinet.fortimanager.fmgr_system_ha - HA configuration.
- fortinet.fortimanager.fmgr_system_ha_peer - Peer.
- fortinet.fortimanager.fmgr_system_interface - Interface configuration.
- fortinet.fortimanager.fmgr_system_interface_obj - Interface configuration.
- fortinet.fortimanager.fmgr_task_task - Read-only table containing the 10000 most recent tasks of the system. This table can be used for tracking non-blocking tasks initiated b...
- fortinet.fortimanager.fmgr_task_task_obj - Read-only table containing the 10000 most recent tasks of the system. This table can be used for tracking non-blocking tasks initiated b...
- fortinet.fortimanager.fmgr_voip_profile - Configure VoIP profiles.
- fortinet.fortimanager.fmgr_voip_profile_obj - Configure VoIP profiles.
- fortinet.fortimanager.fmgr_waf_profile - Web application firewall configuration.
- fortinet.fortimanager.fmgr_waf_profile_obj - Web application firewall configuration.
- fortinet.fortimanager.fmgr_wanopt_profile - Configure WAN optimization profiles.
- fortinet.fortimanager.fmgr_wanopt_profile_obj - Configure WAN optimization profiles.
- fortinet.fortimanager.fmgr_webfilter_profile - Configure Web filter profiles.
- fortinet.fortimanager.fmgr_webfilter_profile_obj - Configure Web filter profiles.
- fortinet.fortimanager.fmgr_webproxy_profile - Configure web proxy profiles.
- fortinet.fortimanager.fmgr_webproxy_profile_obj - Configure web proxy profiles.

frr.frr
~~~~~~~

- frr.frr.frr_bgp - Configure global BGP settings on Free Range Routing(FRR).
- frr.frr.frr_facts - Collect facts from remote devices running Free Range Routing (FRR).

gluster.gluster
~~~~~~~~~~~~~~~

- gluster.gluster.geo_rep - Manage geo-replication sessions
- gluster.gluster.gluster_heal_info - Gather facts about either self-heal or rebalance status
- gluster.gluster.gluster_peer - Attach/Detach peers to/from the cluster
- gluster.gluster.gluster_volume - Manage GlusterFS volumes

hetzner.hcloud
~~~~~~~~~~~~~~

- hetzner.hcloud.hcloud_floating_ip - Create and manage cloud Floating IPs on the Hetzner Cloud.
- hetzner.hcloud.hcloud_load_balancer - Create and manage cloud Load Balancers on the Hetzner Cloud.
- hetzner.hcloud.hcloud_load_balancer_network - Manage the relationship between Hetzner Cloud Networks and Load Balancers
- hetzner.hcloud.hcloud_load_balancer_service - Create and manage the services of cloud Load Balancers on the Hetzner Cloud.
- hetzner.hcloud.hcloud_load_balancer_target - Manage Hetzner Cloud Load Balancer targets
- hetzner.hcloud.hcloud_load_balancer_type_info - Gather infos about the Hetzner Cloud Load Balancer types.

ibm.qradar
~~~~~~~~~~

- ibm.qradar.ibm.qradar.deploy - Trigger a qradar configuration deployment
- ibm.qradar.ibm.qradar.log_source_management - Manage Log Sources in QRadar
- ibm.qradar.ibm.qradar.offense_action - Take action on a QRadar Offense
- ibm.qradar.ibm.qradar.offense_info - Obtain information about one or many QRadar Offenses, with filter options
- ibm.qradar.ibm.qradar.offense_note - Create or update a QRadar Offense Note
- ibm.qradar.ibm.qradar.rule - Manage state of QRadar Rules, with filter options
- ibm.qradar.ibm.qradar.rule_info - Obtain information about one or many QRadar Rules, with filter options

junipernetworks.junos
~~~~~~~~~~~~~~~~~~~~~

- junipernetworks.junos.junos_acl_interfaces - ACL interfaces resource module
- junipernetworks.junos.junos_acls - ACLs resource module
- junipernetworks.junos.junos_banner - Manage multiline banners on Juniper JUNOS devices
- junipernetworks.junos.junos_command - Run arbitrary commands on an Juniper JUNOS device
- junipernetworks.junos.junos_config - Manage configuration on devices running Juniper JUNOS
- junipernetworks.junos.junos_facts - Collect facts from remote devices running Juniper Junos
- junipernetworks.junos.junos_interface - (deprecated, removed after 2022-06-01) Manage Interface on Juniper JUNOS network devices
- junipernetworks.junos.junos_interfaces - Junos Interfaces resource module
- junipernetworks.junos.junos_l2_interface - (deprecated, removed after 2022-06-01) Manage L2 Interface on Juniper JUNOS network devices
- junipernetworks.junos.junos_l2_interfaces - L2 interfaces resource module
- junipernetworks.junos.junos_l3_interface - (deprecated, removed after 2022-06-01) Manage L3 interfaces on Juniper JUNOS network devices
- junipernetworks.junos.junos_l3_interfaces - L3 interfaces resource module
- junipernetworks.junos.junos_lacp - Global Link Aggregation Control Protocol (LACP) Junos resource module
- junipernetworks.junos.junos_lacp_interfaces - LACP interfaces resource module
- junipernetworks.junos.junos_lag_interfaces - Link Aggregation Juniper JUNOS resource module
- junipernetworks.junos.junos_linkagg - (deprecated, removed after 2022-06-01) Manage link aggregation groups on Juniper JUNOS network devices
- junipernetworks.junos.junos_lldp - (deprecated, removed after 2022-06-01) Manage LLDP configuration on Juniper JUNOS network devices
- junipernetworks.junos.junos_lldp_global - LLDP resource module
- junipernetworks.junos.junos_lldp_interface - (deprecated, removed after 2022-06-01) Manage LLDP interfaces configuration on Juniper JUNOS network devices
- junipernetworks.junos.junos_lldp_interfaces - LLDP interfaces resource module
- junipernetworks.junos.junos_logging - Manage logging on network devices
- junipernetworks.junos.junos_netconf - Configures the Junos Netconf system service
- junipernetworks.junos.junos_ospfv2 - OSPFv2 resource module
- junipernetworks.junos.junos_package - Installs packages on remote devices running Junos
- junipernetworks.junos.junos_ping - Tests reachability using ping from devices running Juniper JUNOS
- junipernetworks.junos.junos_rpc - Runs an arbitrary RPC over NetConf on an Juniper JUNOS device
- junipernetworks.junos.junos_scp - Transfer files from or to remote devices running Junos
- junipernetworks.junos.junos_static_route - (deprecated, removed after 2022-06-01) Manage static IP routes on Juniper JUNOS network devices
- junipernetworks.junos.junos_static_routes - Static routes resource module
- junipernetworks.junos.junos_system - Manage the system attributes on Juniper JUNOS devices
- junipernetworks.junos.junos_user - Manage local user accounts on Juniper JUNOS devices
- junipernetworks.junos.junos_vlan - (deprecated, removed after 2022-06-01) Manage VLANs on Juniper JUNOS network devices
- junipernetworks.junos.junos_vlans - VLANs resource module
- junipernetworks.junos.junos_vrf - Manage the VRF definitions on Juniper JUNOS devices

netbox.netbox
~~~~~~~~~~~~~

- netbox.netbox.netbox_aggregate - Creates or removes aggregates from Netbox
- netbox.netbox.netbox_cable - Create, update or delete cables within Netbox
- netbox.netbox.netbox_circuit - Create, update or delete circuits within Netbox
- netbox.netbox.netbox_circuit_termination - Create, update or delete circuit terminations within Netbox
- netbox.netbox.netbox_circuit_type - Create, update or delete circuit types within Netbox
- netbox.netbox.netbox_cluster - Create, update or delete clusters within Netbox
- netbox.netbox.netbox_cluster_group - Create, update or delete cluster groups within Netbox
- netbox.netbox.netbox_cluster_type - Create, update or delete cluster types within Netbox
- netbox.netbox.netbox_console_port - Create, update or delete console ports within Netbox
- netbox.netbox.netbox_console_port_template - Create, update or delete console port templates within Netbox
- netbox.netbox.netbox_console_server_port - Create, update or delete console server ports within Netbox
- netbox.netbox.netbox_console_server_port_template - Create, update or delete console server port templates within Netbox
- netbox.netbox.netbox_device_bay - Create, update or delete device bays within Netbox
- netbox.netbox.netbox_device_bay_template - Create, update or delete device bay templates within Netbox
- netbox.netbox.netbox_device_interface_template - Creates or removes interfaces on devices from Netbox
- netbox.netbox.netbox_device_role - Create, update or delete devices roles within Netbox
- netbox.netbox.netbox_device_type - Create, update or delete device types within Netbox
- netbox.netbox.netbox_front_port - Create, update or delete front ports within Netbox
- netbox.netbox.netbox_front_port_template - Create, update or delete front port templates within Netbox
- netbox.netbox.netbox_inventory_item - Creates or removes inventory items from Netbox
- netbox.netbox.netbox_ipam_role - Creates or removes ipam roles from Netbox
- netbox.netbox.netbox_manufacturer - Create or delete manufacturers within Netbox
- netbox.netbox.netbox_platform - Create or delete platforms within Netbox
- netbox.netbox.netbox_power_feed - Create, update or delete power feeds within Netbox
- netbox.netbox.netbox_power_outlet - Create, update or delete power outlets within Netbox
- netbox.netbox.netbox_power_outlet_template - Create, update or delete power outlet templates within Netbox
- netbox.netbox.netbox_power_panel - Create, update or delete power panels within Netbox
- netbox.netbox.netbox_power_port - Create, update or delete power ports within Netbox
- netbox.netbox.netbox_power_port_template - Create, update or delete power port templates within Netbox
- netbox.netbox.netbox_provider - Create, update or delete providers within Netbox
- netbox.netbox.netbox_rack - Create, update or delete racks within Netbox
- netbox.netbox.netbox_rack_group - Create, update or delete racks groups within Netbox
- netbox.netbox.netbox_rack_role - Create, update or delete racks roles within Netbox
- netbox.netbox.netbox_rear_port - Create, update or delete rear ports within Netbox
- netbox.netbox.netbox_rear_port_template - Create, update or delete rear port templates within Netbox
- netbox.netbox.netbox_region - Creates or removes regions from Netbox
- netbox.netbox.netbox_rir - Create, update or delete RIRs within Netbox
- netbox.netbox.netbox_service - Creates or removes service from Netbox
- netbox.netbox.netbox_tenant - Creates or removes tenants from Netbox
- netbox.netbox.netbox_tenant_group - Creates or removes tenant groups from Netbox
- netbox.netbox.netbox_virtual_chassis - Create, update or delete virtual chassis within Netbox
- netbox.netbox.netbox_virtual_machine - Create, update or delete virtual_machines within Netbox
- netbox.netbox.netbox_vlan - Create, update or delete vlans within Netbox
- netbox.netbox.netbox_vlan_group - Create, update or delete vlans groups within Netbox
- netbox.netbox.netbox_vm_interface - Creates or removes interfaces from virtual machines in Netbox
- netbox.netbox.netbox_vrf - Create, update or delete vrfs within Netbox

ngine_io.vultr
~~~~~~~~~~~~~~

- ngine_io.vultr.vultr_plan_baremetal_info - Gather information about the Vultr Bare Metal plans available.
- ngine_io.vultr.vultr_server_baremetal - Manages baremetal servers on Vultr.

openstack.cloud
~~~~~~~~~~~~~~~

- openstack.cloud.federation_idp - Add support for Keystone Identity Providers
- openstack.cloud.federation_idp_info - Add support for fetching the information about federation IDPs
- openstack.cloud.federation_mapping - Add support for Keystone mappings
- openstack.cloud.federation_mapping_info - Add support for fetching the information about Keystone mappings
- openstack.cloud.keystone_federation_protocol - Add support for Keystone federation Protocols
- openstack.cloud.keystone_federation_protocol_info - Add support for getting information about Keystone federation Protocols
- openstack.cloud.routers_info - Retrieve information about one or more OpenStack routers.
- openstack.cloud.volume_info - Retrieve information about Openstack volumes.

openvswitch.openvswitch
~~~~~~~~~~~~~~~~~~~~~~~

- openvswitch.openvswitch.openvswitch_bridge - Manage Open vSwitch bridges
- openvswitch.openvswitch.openvswitch_db - Configure open vswitch database.
- openvswitch.openvswitch.openvswitch_port - Manage Open vSwitch ports

ovirt.ovirt
~~~~~~~~~~~

- ovirt.ovirt.ovirt_affinity_group - Module to manage affinity groups in oVirt/RHV
- ovirt.ovirt.ovirt_affinity_label - Module to manage affinity labels in oVirt/RHV
- ovirt.ovirt.ovirt_affinity_label_info - Retrieve information about one or more oVirt/RHV affinity labels
- ovirt.ovirt.ovirt_api_info - Retrieve information about the oVirt/RHV API
- ovirt.ovirt.ovirt_auth - Module to manage authentication to oVirt/RHV
- ovirt.ovirt.ovirt_cluster - Module to manage clusters in oVirt/RHV
- ovirt.ovirt.ovirt_cluster_info - Retrieve information about one or more oVirt/RHV clusters
- ovirt.ovirt.ovirt_datacenter - Module to manage data centers in oVirt/RHV
- ovirt.ovirt.ovirt_datacenter_info - Retrieve information about one or more oVirt/RHV datacenters
- ovirt.ovirt.ovirt_disk - Module to manage Virtual Machine and floating disks in oVirt/RHV
- ovirt.ovirt.ovirt_disk_info - Retrieve information about one or more oVirt/RHV disks
- ovirt.ovirt.ovirt_event - Create or delete an event in oVirt/RHV
- ovirt.ovirt.ovirt_event_info - This module can be used to retrieve information about one or more oVirt/RHV events
- ovirt.ovirt.ovirt_external_provider - Module to manage external providers in oVirt/RHV
- ovirt.ovirt.ovirt_external_provider_info - Retrieve information about one or more oVirt/RHV external providers
- ovirt.ovirt.ovirt_group - Module to manage groups in oVirt/RHV
- ovirt.ovirt.ovirt_group_info - Retrieve information about one or more oVirt/RHV groups
- ovirt.ovirt.ovirt_host - Module to manage hosts in oVirt/RHV
- ovirt.ovirt.ovirt_host_info - Retrieve information about one or more oVirt/RHV hosts
- ovirt.ovirt.ovirt_host_network - Module to manage host networks in oVirt/RHV
- ovirt.ovirt.ovirt_host_pm - Module to manage power management of hosts in oVirt/RHV
- ovirt.ovirt.ovirt_host_storage_info - Retrieve information about one or more oVirt/RHV HostStorages (applicable only for block storage)
- ovirt.ovirt.ovirt_instance_type - Module to manage Instance Types in oVirt/RHV
- ovirt.ovirt.ovirt_job - Module to manage jobs in oVirt/RHV
- ovirt.ovirt.ovirt_mac_pool - Module to manage MAC pools in oVirt/RHV
- ovirt.ovirt.ovirt_network - Module to manage logical networks in oVirt/RHV
- ovirt.ovirt.ovirt_network_info - Retrieve information about one or more oVirt/RHV networks
- ovirt.ovirt.ovirt_nic - Module to manage network interfaces of Virtual Machines in oVirt/RHV
- ovirt.ovirt.ovirt_nic_info - Retrieve information about one or more oVirt/RHV virtual machine network interfaces
- ovirt.ovirt.ovirt_permission - Module to manage permissions of users/groups in oVirt/RHV
- ovirt.ovirt.ovirt_permission_info - Retrieve information about one or more oVirt/RHV permissions
- ovirt.ovirt.ovirt_quota - Module to manage datacenter quotas in oVirt/RHV
- ovirt.ovirt.ovirt_quota_info - Retrieve information about one or more oVirt/RHV quotas
- ovirt.ovirt.ovirt_role - Module to manage roles in oVirt/RHV
- ovirt.ovirt.ovirt_scheduling_policy_info - Retrieve information about one or more oVirt scheduling policies
- ovirt.ovirt.ovirt_snapshot - Module to manage Virtual Machine Snapshots in oVirt/RHV
- ovirt.ovirt.ovirt_snapshot_info - Retrieve information about one or more oVirt/RHV virtual machine snapshots
- ovirt.ovirt.ovirt_storage_connection - Module to manage storage connections in oVirt
- ovirt.ovirt.ovirt_storage_domain - Module to manage storage domains in oVirt/RHV
- ovirt.ovirt.ovirt_storage_domain_info - Retrieve information about one or more oVirt/RHV storage domains
- ovirt.ovirt.ovirt_storage_template_info - Retrieve information about one or more oVirt/RHV templates relate to a storage domain.
- ovirt.ovirt.ovirt_storage_vm_info - Retrieve information about one or more oVirt/RHV virtual machines relate to a storage domain.
- ovirt.ovirt.ovirt_tag - Module to manage tags in oVirt/RHV
- ovirt.ovirt.ovirt_tag_info - Retrieve information about one or more oVirt/RHV tags
- ovirt.ovirt.ovirt_template - Module to manage virtual machine templates in oVirt/RHV
- ovirt.ovirt.ovirt_template_info - Retrieve information about one or more oVirt/RHV templates
- ovirt.ovirt.ovirt_user - Module to manage users in oVirt/RHV
- ovirt.ovirt.ovirt_user_info - Retrieve information about one or more oVirt/RHV users
- ovirt.ovirt.ovirt_vm - Module to manage Virtual Machines in oVirt/RHV
- ovirt.ovirt.ovirt_vm_info - Retrieve information about one or more oVirt/RHV virtual machines
- ovirt.ovirt.ovirt_vm_os_info - Retrieve information on all supported oVirt/RHV operating systems
- ovirt.ovirt.ovirt_vmpool - Module to manage VM pools in oVirt/RHV
- ovirt.ovirt.ovirt_vmpool_info - Retrieve information about one or more oVirt/RHV vmpools
- ovirt.ovirt.ovirt_vnic_profile - Module to manage vNIC profile of network in oVirt/RHV
- ovirt.ovirt.ovirt_vnic_profile_info - Retrieve information about one or more oVirt/RHV vnic profiles

splunk.es
~~~~~~~~~

- splunk.es.splunk.es.adaptive_response_notable_event - Manage Splunk Enterprise Security Notable Event Adaptive Responses
- splunk.es.splunk.es.correlation_search - Manage Splunk Enterprise Security Correlation Searches
- splunk.es.splunk.es.correlation_search_info - Manage Splunk Enterprise Security Correlation Searches
- splunk.es.splunk.es.data_input_monitor - Manage Splunk Data Inputs of type Monitor
- splunk.es.splunk.es.data_input_network - Manage Splunk Data Inputs of type TCP or UDP

theforeman.foreman
~~~~~~~~~~~~~~~~~~

- theforeman.foreman.activation_key - Manage Activation Keys
- theforeman.foreman.architecture - Manage Architectures
- theforeman.foreman.auth_source_ldap - Manage LDAP Authentication Sources
- theforeman.foreman.bookmark - Manage Bookmarks
- theforeman.foreman.compute_attribute - Manage Compute Attributes
- theforeman.foreman.compute_profile - Manage Compute Profiles
- theforeman.foreman.compute_resource - Manage Compute Resources
- theforeman.foreman.config_group - Manage (Puppet) Config Groups
- theforeman.foreman.content_credential - Manage Content Credentials
- theforeman.foreman.content_upload - Upload content to a repository
- theforeman.foreman.content_view - Manage Content Views
- theforeman.foreman.content_view_filter - Manage Content View Filters
- theforeman.foreman.content_view_version - Manage Content View Versions
- theforeman.foreman.domain - Manage Domains
- theforeman.foreman.external_usergroup - Manage External User Groups
- theforeman.foreman.global_parameter - Manage Global Parameters
- theforeman.foreman.hardware_model - Manage Hardware Models
- theforeman.foreman.host - Manage Hosts
- theforeman.foreman.host_collection - Manage Host Collections
- theforeman.foreman.host_power - Manage Power State of Hosts
- theforeman.foreman.hostgroup - Manage Hostgroups
- theforeman.foreman.http_proxy - Manage HTTP Proxies
- theforeman.foreman.image - Manage Images
- theforeman.foreman.installation_medium - Manage Installation Media
- theforeman.foreman.job_template - Manage Job Templates
- theforeman.foreman.lifecycle_environment - Manage Lifecycle Environments
- theforeman.foreman.location - Manage Locations
- theforeman.foreman.operatingsystem - Manage Operating Systems
- theforeman.foreman.organization - Manage Organizations
- theforeman.foreman.os_default_template - Manage Default Template Associations To Operating Systems
- theforeman.foreman.partition_table - Manage Partition Table Templates
- theforeman.foreman.product - Manage Products
- theforeman.foreman.provisioning_template - Manage Provisioning Templates
- theforeman.foreman.puppet_environment - Manage Puppet Environments
- theforeman.foreman.realm - Manage Realms
- theforeman.foreman.redhat_manifest - Interact with a Red Hat Satellite Subscription Manifest
- theforeman.foreman.repository - Manage Repositories
- theforeman.foreman.repository_set - Enable/disable Repositories in Repository Sets
- theforeman.foreman.repository_sync - Sync a Repository or Product
- theforeman.foreman.resource_info - Gather information about resources
- theforeman.foreman.role - Manage Roles
- theforeman.foreman.scap_content - Manage SCAP content
- theforeman.foreman.scap_tailoring_file - Manage SCAP Tailoring Files
- theforeman.foreman.scc_account - Manage SUSE Customer Center Accounts
- theforeman.foreman.scc_product - Subscribe SUSE Customer Center Account Products
- theforeman.foreman.setting - Manage Settings
- theforeman.foreman.smart_class_parameter - Manage Smart Class Parameters
- theforeman.foreman.snapshot - Manage Snapshots
- theforeman.foreman.subnet - Manage Subnets
- theforeman.foreman.subscription_manifest - Manage Subscription Manifests
- theforeman.foreman.sync_plan - Manage Sync Plans
- theforeman.foreman.templates_import - Sync Templates from a repository
- theforeman.foreman.user - Manage Users
- theforeman.foreman.usergroup - Manage User Groups

vyos.vyos
~~~~~~~~~

- vyos.vyos.vyos_banner - Manage multiline banners on VyOS devices
- vyos.vyos.vyos_command - Run one or more commands on VyOS devices
- vyos.vyos.vyos_config - Manage VyOS configuration on remote device
- vyos.vyos.vyos_facts - Get facts about vyos devices.
- vyos.vyos.vyos_firewall_global - FIREWALL global resource module
- vyos.vyos.vyos_firewall_interfaces - FIREWALL interfaces resource module
- vyos.vyos.vyos_firewall_rules - FIREWALL rules resource module
- vyos.vyos.vyos_interface - (deprecated, removed after 2022-06-01) Manage Interface on VyOS network devices
- vyos.vyos.vyos_interfaces - Interfaces resource module
- vyos.vyos.vyos_l3_interface - (deprecated, removed after 2022-06-01) Manage L3 interfaces on VyOS network devices
- vyos.vyos.vyos_l3_interfaces - L3 interfaces resource module
- vyos.vyos.vyos_lag_interfaces - LAG interfaces resource module
- vyos.vyos.vyos_linkagg - (deprecated, removed after 2022-06-01) Manage link aggregation groups on VyOS network devices
- vyos.vyos.vyos_lldp - (deprecated, removed after 2022-06-01) Manage LLDP configuration on VyOS network devices
- vyos.vyos.vyos_lldp_global - LLDP global resource module
- vyos.vyos.vyos_lldp_interface - (deprecated, removed after 2022-06-01) Manage LLDP interfaces configuration on VyOS network devices
- vyos.vyos.vyos_lldp_interfaces - LLDP interfaces resource module
- vyos.vyos.vyos_logging - Manage logging on network devices
- vyos.vyos.vyos_ospfv2 - OSPFv2 resource module
- vyos.vyos.vyos_ospfv3 - OSPFV3 resource module
- vyos.vyos.vyos_ping - Tests reachability using ping from VyOS network devices
- vyos.vyos.vyos_static_route - (deprecated, removed after 2022-06-01) Manage static IP routes on Vyatta VyOS network devices
- vyos.vyos.vyos_static_routes - Static routes resource module
- vyos.vyos.vyos_system - Run `set system` commands on VyOS devices
- vyos.vyos.vyos_user - Manage the collection of local users on VyOS device
- vyos.vyos.vyos_vlan - Manage VLANs on VyOS network devices
