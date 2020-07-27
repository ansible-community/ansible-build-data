==========================
Ansible 2.10 Release Notes
==========================

.. contents::
  :local:
  :depth: 2

v2.10.0a5
=========

.. contents::
  :local:
  :depth: 2

Ansible Base
------------

Ansible 2.10.0a5 contains Ansible-base version 2.10.0rc2.
The changes are reported in the combined changelog below.

Changed Collections
-------------------

- amazon.aws was upgraded to version 1.0.1-dev9.
  Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.
- ansible.netcommon was upgraded to version 1.0.1-dev8.
  The changes are reported in the combined changelog below.
- ansible.posix was upgraded to version 1.1.1-dev4.
  Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.
- ansible.windows was upgraded to version 0.2.0.
  The changes are reported in the combined changelog below.
- arista.eos was upgraded to version 1.0.1-dev9.
  The changes are reported in the combined changelog below.
- awx.awx was upgraded to version 13.0.0.
  Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.
- azure.azcollection was upgraded to version 0.3.0.
  Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.
- check_point.mgmt was upgraded to version 1.0.6.
  Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.
- chocolatey.chocolatey was upgraded to version 1.0.2.
  Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.
- cisco.aci was upgraded to version 0.0.7.
  Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.
- cisco.asa was upgraded to version 1.0.1-dev4.
  The changes are reported in the combined changelog below.
- cisco.intersight was upgraded to version 1.0.7.
  Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.
- cisco.ios was upgraded to version 1.0.1-dev6.
  The changes are reported in the combined changelog below.
- cisco.iosxr was upgraded to version 1.0.3-dev7.
  The changes are reported in the combined changelog below.
- cisco.meraki was upgraded to version 1.3.2.
  The changes are reported in the combined changelog below.
- cisco.mso was upgraded to version 0.0.8.
  Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.
- cisco.nxos was upgraded to version 1.0.1-dev9.
  The changes are reported in the combined changelog below.
- cisco.ucs was upgraded to version 1.4.0.
  Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.
- cloudscale_ch.cloud was upgraded to version 1.0.0.
  Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.
- community.aws was upgraded to version 1.0.1-dev1.
  Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.
- community.azure was upgraded to version 0.1.0.
  Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.
- community.crypto was upgraded to version 1.0.0.
  The changes are reported in the combined changelog below.
- community.digitalocean was upgraded to version 0.1.0.
  The changes are reported in the combined changelog below.
- community.general was upgraded to version 0.3.0-experimental.meta.redirects-3.
  The changes are reported in the combined changelog below.
- community.grafana was upgraded to version 0.2.2.
  Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.
- community.kubernetes was upgraded to version 0.11.1.
  The changes are reported in the combined changelog below.
- community.libvirt was upgraded to version 0.1.0.
  Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.
- community.mongodb was upgraded to version 0.1.2.
  Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.
- community.mysql was upgraded to version 0.1.0.
  Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.
- community.network was upgraded to version 0.2.1.
  The changes are reported in the combined changelog below.
- community.proxysql was upgraded to version 0.1.0.
  Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.
- community.rabbitmq was upgraded to version 0.1.0.
  Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.
- community.vmware was upgraded to version 1.0.1-dev9.
  The changes are reported in the combined changelog below.
- community.windows was upgraded to version 0.2.0.
  The changes are reported in the combined changelog below.
- community.zabbix was upgraded to version 0.2.0.
  Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.
- containers.podman was upgraded to version 1.1.2.
  Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.
- cyberark.conjur was upgraded to version 1.0.6.
  Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.
- cyberark.pas was upgraded to version 1.0.5.
  Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.
- dellemc.os10 was upgraded to version 0.1.0-dev2.
  Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.
- f5networks.f5_modules was upgraded to version 1.5.0.
  Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.
- fortinet.fortimanager was upgraded to version 1.0.3.
  Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.
- fortinet.fortios was upgraded to version 1.0.13.
  Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.
- frr.frr was upgraded to version 1.0.1-dev2.
  The changes are reported in the combined changelog below.
- google.cloud was upgraded to version 0.10.1.
  Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.
- hetzner.hcloud was upgraded to version 0.2.0.
  The changes are reported in the combined changelog below.
- ibm.qradar was upgraded to version 1.0.2-dev1.
  Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.
- infinidat.infinibox was upgraded to version 1.2.3.
  Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.
- junipernetworks.junos was upgraded to version 1.0.1-dev6.
  The changes are reported in the combined changelog below.
- mellanox.onyx was upgraded to version 0.1.0.
  Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.
- netapp.aws was upgraded to version 20.6.0.
  Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.
- netapp.elementsw was upgraded to version 20.6.0.
  Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.
- netapp.ontap was upgraded to version 20.7.0.
  Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.
- netapp_eseries.santricity was upgraded to version 1.0.8.
  Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.
- netbox.netbox was upgraded to version 0.3.1.
  Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.
- ngine_io.cloudstack was upgraded to version 0.3.0.
  The changes are reported in the combined changelog below.
- ngine_io.exoscale was upgraded to version 0.1.1.
  Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.
- ngine_io.vultr was upgraded to version 0.3.0.
  The changes are reported in the combined changelog below.
- openstack.cloud was upgraded to version 1.0.1.
  Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.
- openvswitch.openvswitch was upgraded to version 1.0.1-dev4.
  The changes are reported in the combined changelog below.
- ovirt.ovirt was upgraded to version 1.0.0.
  Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.
- purestorage.flasharray was upgraded to version 1.3.1.
  Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.
- purestorage.flashblade was upgraded to version 1.2.6.
  Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.
- servicenow.servicenow was upgraded to version 1.0.3-dev2.
  Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.
- skydive.skydive was upgraded to version 0.0.1-dev6.
  Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.
- splunk.es was upgraded to version 1.0.1-dev1.
  Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.
- theforeman.foreman was upgraded to version 1.0.1.
  Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.
- vyos.vyos was upgraded to version 1.0.2-dev6.
  The changes are reported in the combined changelog below.
- wti.remote was upgraded to version 1.0.1.
  Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.

Major Changes
-------------

Ansible Base
~~~~~~~~~~~~

- Both ansible-doc and ansible-console's help command will error for modules and plugins whose return documentation cannot be parsed as YAML. All modules and plugins passing ``ansible-test sanity --test yamllint`` will not be affected by this.
- Collections may declare a list of supported/tested Ansible versions for the collection. A warning is issued if a collection does not support the Ansible version that loads it (can also be configured as silent or a fatal error). Collections that do not declare supported Ansible versions do not issue a warning/error.
- Plugin routing allows collections to declare deprecation, redirection targets, and removals for all plugin types.
- Plugins that import module_utils and other ansible namespaces that have moved to collections should continue to work unmodified.
- Routing data built into Ansible 2.10 ensures that 2.9 content should work unmodified on 2.10. Formerly included modules and plugins that were moved to collections are still accessible by their original unqualified names, so long as their destination collections are installed.
- When deprecations are done in code, they to specify a ``collection_name`` so that deprecation warnings can mention which collection - or ansible-base - is deprecating a feature. This affects all ``Display.deprecated()`` or ``AnsibleModule.deprecate()`` or ``Ansible.Basic.Deprecate()`` calls, and ``removed_in_version``/``removed_at_date`` or ``deprecated_aliases`` in module argument specs.
- ansible-test now uses a different ``default`` test container for Ansible Collections

community.general
~~~~~~~~~~~~~~~~~

- docker_container - the ``network_mode`` option will be set by default to the name of the first network in ``networks`` if at least one network is given and ``networks_cli_compatible`` is ``true`` (will be default from community.general 2.0.0 on). Set to an explicit value to avoid deprecation warnings if you specify networks and set ``networks_cli_compatible`` to ``true``. The current default (not specifying it) is equivalent to the value ``default``.
- docker_container - the module has a new option, ``container_default_behavior``, whose default value will change from ``compatibility`` to ``no_defaults``. Set to an explicit value to avoid deprecation warnings.
- gitlab_user - no longer requires ``name``, ``email`` and ``password`` arguments when ``state=absent``.
- zabbix_action - no longer requires ``esc_period`` and ``event_source`` arguments when ``state=absent``.

community.kubernetes
~~~~~~~~~~~~~~~~~~~~

- Add changelog and fragments and document changelog process (https://github.com/ansible-collections/community.kubernetes/pull/131).
- helm - New module for managing Helm charts (https://github.com/ansible-collections/community.kubernetes/pull/61).
- helm_info - New module for retrieving Helm chart information (https://github.com/ansible-collections/community.kubernetes/pull/61).
- helm_repository - New module for managing Helm repositories (https://github.com/ansible-collections/community.kubernetes/pull/61).
- k8s - Inventory source migrated from Ansible 2.9 to Kubernetes collection.
- k8s - Lookup plugin migrated from Ansible 2.9 to Kubernetes collection.
- k8s - Module migrated from Ansible 2.9 to Kubernetes collection.
- k8s_auth - Module migrated from Ansible 2.9 to Kubernetes collection.
- k8s_config_resource_name - Filter plugin migrated from Ansible 2.9 to Kubernetes collection.
- k8s_exec - New module for executing commands on pods via Kubernetes API (https://github.com/ansible-collections/community.kubernetes/pull/14).
- k8s_info - Module migrated from Ansible 2.9 to Kubernetes collection.
- k8s_log - New module for retrieving pod logs (https://github.com/ansible-collections/community.kubernetes/pull/16).
- k8s_scale - Module migrated from Ansible 2.9 to Kubernetes collection.
- k8s_service - Module migrated from Ansible 2.9 to Kubernetes collection.
- kubectl - Connection plugin migrated from Ansible 2.9 to Kubernetes collection.
- openshift - Inventory source migrated from Ansible 2.9 to Kubernetes collection.

Minor Changes
-------------

Ansible Base
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
- ansible-test - Add a test to prevent ``state=get``
- ansible-test - Add a test to prevent ``state=list`` and ``state=info``
- ansible-test - Add a verbosity option for displaying warnings.
- ansible-test - Add support for Python 3.9.
- ansible-test - Added CI provider support for Azure Pipelines.
- ansible-test - Added a ``ansible-test coverage analyze targets filter`` command to filter aggregated coverage reports by path and/or target name.
- ansible-test - Added a ``ansible-test coverage analyze targets`` command to analyze integration test code coverage by test target.
- ansible-test - Added support for Ansible Core CI request signing for Shippable.
- ansible-test - Added support for testing on Fedora 32.
- ansible-test - General code cleanup.
- ansible-test - Now includes testing support for RHEL 8.2
- ansible-test - Provisioning of RHEL instances now includes installation of pinned versions of ``packaging`` and ``pyparsing`` to match the downstream vendored versions.
- ansible-test - Refactor code to consolidate filesystem access and improve handling of encoding.
- ansible-test - Refactored CI related logic into a basic provider abstraction.
- ansible-test - Remove obsolete support for provisioning remote vCenter instances. The supporting services are no longer available.
- ansible-test - Report the correct line number in the ``yamllint`` sanity test when reporting ``libyaml`` parse errors in module documentation.
- ansible-test - Support writing compact JSON files instead of formatting and indenting the output.
- ansible-test - Update Ubuntu 18.04 test container to version 1.13 which includes ``venv``
- ansible-test - Update ``default-test-container`` to version 1.11, which includes Python 3.9.0a4.
- ansible-test - Updated the default test containers to include Python 3.9.0b3.
- ansible-test - Upgrade OpenSUSE containers to use Leap 15.1.
- ansible-test - Upgrade distro test containers from 1.16.0 to 1.17.0
- ansible-test - Upgrade from ansible-base-test-container 1.1 to 2.2
- ansible-test - Upgrade from default-test-container 2.1 to 2.2
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
- ansible-test - enable deprecated version testing for modules and ``module.deprecate()`` calls (https://github.com/ansible/ansible/pull/66920/).
- ansible-test - extend alias validation.
- ansible-test - fixed ``units`` command with ``--docker`` to (mostly) work under podman
- ansible-test - improve module validation so that ``default``, ``sample`` and ``example`` contain JSON values and not arbitrary YAML values, like ``datetime`` objects or dictionaries with non-string keys.
- ansible-test - module validation will now consider arguments added by ``add_file_common_arguments=True`` correctly.
- ansible-test - switch from testing RHEL 8.0 and RHEL 8.1 Beta to RHEL 8.1
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
- distro - Update bundled version of distro from 1.4.0 to 1.5.0
- dnf - Properly handle idempotent transactions with package name wildcard globs (https://github.com/ansible/ansible/issues/62809)
- dnf - Properly handle module AppStreams that don't define stream (https://github.com/ansible/ansible/issues/63683)
- dnf param to pass allowerasing
- downstream packagers may install packages under ansible._vendor, which will be added to head of sys.path at ansible package load
- file - specifying ``src`` without ``state`` is now an error
- get_bin_path() - change the interface to always raise ``ValueError`` if the command is not found (https://github.com/ansible/ansible/pull/56813)
- get_url - Remove deprecated string format support for the headers option (https://github.com/ansible/ansible/issues/61891)
- git - added an ``archive_prefix`` option to set a prefix to add to each file path in archive
- host_group_vars plugin - Require whitelisting and whitelist by default.
- new magic variable - ``ansible_config_file`` - full path of used Ansible config file
- package_facts.py - Add support for Pacman package manager.
- pipe lookup - update docs for Popen with shell=True usages (https://github.com/ansible/ansible/issues/70159).
- plugin loader - Add MODULE_IGNORE_EXTS config option to skip over certain extensions when looking for script and binary modules.
- powershell (shell plugin) - Fix `join_path` to support UNC paths (https://github.com/ansible/ansible/issues/66341)
- regexp_replace filter - add multiline support for regex_replace filter (https://github.com/ansible/ansible/issues/61985)
- rename ``_find_existing_collections()`` to ``find_existing_collections()`` to reflect its use across multiple files
- reorganized code for the ``ansible-test coverage`` command for easier maintenance and feature additions
- service_facts - Added undocumented 'indirect' and 'static' as service status (https://github.com/ansible/ansible/issues/69752).
- ssh - connection plugin now supports a new variable ``sshpass_prompt`` which gets passed to ``sshpass`` allowing the user to set a custom substring to search for a password prompt (requires sshpass 1.06+)
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
- win_package - Added proxy support for retrieving packages from a URL - https://github.com/ansible/ansible/issues/43818
- win_package - Added support for ``.appx``, ``.msix``, ``.appxbundle``, and ``.msixbundle`` package - https://github.com/ansible/ansible/issues/50765
- win_package - Added support for ``.msp`` packages - https://github.com/ansible/ansible/issues/22789
- win_package - Added support for specifying the HTTP method when getting files from a URL - https://github.com/ansible/ansible/issues/35377
- win_package - Move across to ``Ansible.Basic`` for better invocation logging
- win_package - Read uninstall strings from the ``QuietUninstallString`` if present to better support argumentless uninstalls of registry based packages.
- win_package - Scan packages in the current user's registry hive - https://github.com/ansible/ansible/issues/45950
- win_regedit - Use new Ansible.Basic wrapper for better invocation reporting
- win_share - Implement append parameter for access rules (https://github.com/ansible/ansible/issues/59237)
- windows setup - Added ``ansible_os_installation_type`` to denote the type of Windows installation the remote host is.

cisco.iosxr
~~~~~~~~~~~

- Bring plugin table to correct position (https://github.com/ansible-collections/cisco.iosxr/pull/44)

cisco.meraki
~~~~~~~~~~~~

- meraki_device - Added deprecation notices to some parameters
- meraki_network - Added deprecation notices to some parameters

community.crypto
~~~~~~~~~~~~~~~~

- luks_device - accept ``passphrase``, ``new_passphrase`` and ``remove_passphrase``.
- luks_device - add ``keysize`` parameter to set key size at LUKS container creation
- luks_device - added support to use UUIDs, and labels with LUKS2 containers
- luks_device - added the ``type`` option that allows user explicit define the LUKS container format version
- openssh_keypair - instead of regenerating some broken or password protected keys, fail the module. Keys can still be regenerated by calling the module with ``force=yes``.
- openssh_keypair - the ``regenerate`` option allows to configure the module's behavior when it should or needs to regenerate private keys.
- openssl_* modules - the cryptography backend now properly supports ``dirName``, ``otherName`` and ``RID`` (Registered ID) names.
- openssl_certificate - Add option for changing which ACME directory to use with acme-tiny. Set the default ACME directory to Let's Encrypt instead of using acme-tiny's default. (acme-tiny also uses Let's Encrypt at the time being, so no action should be neccessary.)
- openssl_certificate - Change the required version of acme-tiny to >= 4.0.0
- openssl_certificate - allow to provide content of some input files via the ``csr_content``, ``privatekey_content``, ``ownca_privatekey_content`` and ``ownca_content`` options.
- openssl_certificate - allow to return the existing/generated certificate directly as ``certificate`` by setting ``return_content`` to ``yes``.
- openssl_certificate_info - allow to provide certificate content via ``content`` option (https://github.com/ansible/ansible/issues/64776).
- openssl_csr - Add support for specifying the SAN ``otherName`` value in the OpenSSL ASN.1 UTF8 string format, ``otherName:<OID>;UTF8:string value``.
- openssl_csr - allow to provide private key content via ``private_key_content`` option.
- openssl_csr - allow to return the existing/generated CSR directly as ``csr`` by setting ``return_content`` to ``yes``.
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
- Follow up changes in homebrew_cask (https://github.com/ansible/ansible/issues/34696).
- Moved OpenStack dynamic inventory script to Openstack Collection.
- Remove redundant encoding in json.load call in ipa module_utils (https://github.com/ansible/ansible/issues/66592).
- Updated documentation about netstat command requirement for listen_ports_facts module (https://github.com/ansible/ansible/issues/68077).
- airbrake_deployment - Allow passing ``project_id`` and ``project_key`` for v4 api deploy compatibility
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
- flatpak and flatpak_remote - use ``module.run_command()`` instead of ``subprocess.Popen()``.
- gitlab_project_variable - implement masked and protected attributes
- gitlab_project_variable - implemented variable_type attribute.
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
- jira - added search function with support for Jira JQL (https://github.com/ansible-collections/community.general/pull/22).
- jira - added update function which can update Jira Selects etc (https://github.com/ansible-collections/community.general/pull/22).
- lvg - add ``pvresize`` new parameter (https://github.com/ansible/ansible/issues/29139).
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
- slack - Add support for user/bot/application tokens (using Slack WebAPI)
- slack - Return ``thread_id`` with thread timestamp when user/bot/application tokens are used
- syslogger - added new parameter ident to specify the name of application which is sending the message to syslog (https://github.com/ansible-collections/community.general/issues/319).
- terraform - Adds option ``backend_config_files``. This can accept a list of paths to multiple configuration files (https://github.com/ansible-collections/community.general/pull/394).
- terraform - Adds option ``variables_files`` for multiple var-files (https://github.com/ansible-collections/community.general/issues/224).
- ufw - accept ``interface_in`` and ``interface_out`` as parameters.
- zabbix_action - allow str values for ``esc_period`` options (https://github.com/ansible/ansible/pull/66841).
- zabbix_host - now supports configuring user macros and host tags on the managed host (see https://github.com/ansible/ansible/pull/66777)
- zabbix_host_info - ``host_name`` based search results now include host groups.
- zabbix_hostmacro - ``macro_name`` now accepts macros in zabbix native format as well (e.g. ``{$MACRO}``)
- zabbix_hostmacro - ``macro_value`` is no longer required when ``state=absent``
- zabbix_proxy - ``interface`` sub-options ``type`` and ``main`` are now deprecated and will be removed in community.general 3.0.0. Also, the values passed to ``interface`` are now checked for correct types and unexpected keys.
- zabbix_proxy - added option proxy_address for comma-delimited list of IP/CIDR addresses or DNS names to accept active proxy requests from
- zabbix_template - add new option omit_date to remove date from exported/dumped template (https://github.com/ansible/ansible/pull/67302)
- zabbix_template - adding new update rule templateLinkage.deleteMissing for newer zabbix versions (https://github.com/ansible/ansible/pull/66747).
- zabbix_template_info - add new option omit_date to remove date from exported/dumped template (https://github.com/ansible/ansible/pull/67302)
- zypper - Added ``allow_vendor_change`` and ``replacefiles`` zypper options (https://github.com/ansible-collections/community.general/issues/381)

community.kubernetes
~~~~~~~~~~~~~~~~~~~~

- Add action groups for playbooks with module_defaults (https://github.com/ansible-collections/community.kubernetes/pull/107).
- Add requires_ansible version constraints to runtime.yml (https://github.com/ansible-collections/community.kubernetes/pull/126).
- Add sanity test ignore file for Ansible 2.11 (https://github.com/ansible-collections/community.kubernetes/pull/130).
- Add test for openshift apply bug (https://github.com/ansible-collections/community.kubernetes/pull/94).
- Add version_added to each new collection module (https://github.com/ansible-collections/community.kubernetes/pull/98).
- Check Python code using flake8 (https://github.com/ansible-collections/community.kubernetes/pull/123).
- Don't require project coverage check on PRs (https://github.com/ansible-collections/community.kubernetes/pull/102).
- Improve k8s Deployment and Daemonset wait conditions (https://github.com/ansible-collections/community.kubernetes/pull/35).
- Minor documentation fixes and use of FQCN in some examples (https://github.com/ansible-collections/community.kubernetes/pull/114).
- Remove action_groups_redirection entry from meta/runtime.yml (https://github.com/ansible-collections/community.kubernetes/pull/127).
- Remove deprecated ANSIBLE_METADATA field (https://github.com/ansible-collections/community.kubernetes/pull/95).
- Rename repository to ``community.kubernetes`` (https://github.com/ansible-collections/community.kubernetes/pull/81).
- Use FQCN in module docs and plugin examples (https://github.com/ansible-collections/community.kubernetes/pull/146).
- Use improved kubernetes diffs where possible (https://github.com/ansible-collections/community.kubernetes/pull/105).
- helm - add 'atomic' option (https://github.com/ansible-collections/community.kubernetes/pull/115).
- helm - minor code refactoring (https://github.com/ansible-collections/community.kubernetes/pull/110).
- helm_info and helm_repository - minor code refactor (https://github.com/ansible-collections/community.kubernetes/pull/117).
- k8s - Added ``persist_config`` option for persisting refreshed tokens (https://github.com/ansible-collections/community.kubernetes/issues/49).
- k8s - Handle set object retrieved from lookup plugin (https://github.com/ansible-collections/community.kubernetes/pull/118).

community.network
~~~~~~~~~~~~~~~~~

- ce_bgp_neighbor_af - Rename the parameter ``redirect_ip_vaildation`` to ``redirect_ip_validation`` (https://github.com/ansible/ansible/pull/62403).

community.vmware
~~~~~~~~~~~~~~~~

- A `vmware` module_defaults group has been added to simplify parameters for multiple VMware tasks. This group includes all VMware modules.
- Add a flag 'force_upgrade' to force VMware tools upgrade installation (https://github.com/ansible-collections/vmware/issues/75).
- Add powerstates to match vmware_guest_powerstate module with vmware_guest (https://github.com/ansible/ansible/issues/55653).
- Added a timeout parameter `wait_for_ip_address_timeout` for `wait_for_ip_address` for longer-running tasks in vmware_guest.
- Added missing backing_disk_mode information about disk which was removed by mistake in vmware_guest_disk_info.
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
- vmware_content_deploy_template - added new field "content_library" to search template inside the specified content library.
- vmware_datastore_cluster - Added basic SDRS configuration (https://github.com/ansible/ansible/issues/65154).
- vmware_datastore_info - added ``properties`` and ``schema`` options.
- vmware_datastore_maintenancemode now returns datastore_status instead of Ansible internal key results (https://github.com/ansible/ansible/issues/62083).
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
- vmware_guest_disk - add support for setting the sharing/multi-writer mode of virtual disks (https://github.com/ansible-collections/vmware/issues/212)
- vmware_guest_network - network adapters can be configured without lists
- vmware_guest_network - network_info returns a list of dictionaries for ease of use
- vmware_guest_network - put deprecation warning for the networks parameter
- vmware_guest_tools_wait now exposes a ``timeout`` parameter that allow the user to adjust the timeout (second).
- vmware_host_active_directory - Fail when there are unrecoverable problems with AD membership instead of reporting a change that doesn't take place (https://github.com/ansible-collections/vmware/issues/59).
- vmware_host_dns - New module replacing vmware_dns_config with increased functionality.
- vmware_host_dns can now set the following empty values, ``domain``, ``search_domains`` and ``dns_servers``.
- vmware_host_facts - added ``properties`` and ``schema`` options.
- vmware_host_firewall_manager - ``allowed_hosts`` excpects a dict as parameter, list is deprecated
- vmware_host_kernel_manager now returns host_kernel_status instead of Ansible internal key results (https://github.com/ansible/ansible/issues/62083).
- vmware_host_logbundle - new code module for a new feature for ESXi support log bundle download operation
- vmware_host_logbundle_info - new code module for a new feature for getting manifests  for ESXi support log bundle
- vmware_host_ntp now returns host_ntp_status instead of Ansible internal key results (https://github.com/ansible/ansible/issues/62083).
- vmware_host_service_manager now returns host_service_status instead of Ansible internal key results (https://github.com/ansible/ansible/issues/62083).
- vmware_rest_client - Added a new definition get_library_item_from_content_library_name.
- vmware_tag now returns tag_status instead of Ansible internal key results (https://github.com/ansible/ansible/issues/62083).
- vmware_vm_inventory inventory plugin, raise more descriptive error when all template strings in ``hostnames`` fail.

community.windows
~~~~~~~~~~~~~~~~~

- win_disk_facts - Set output array order to be by disk number property - https://github.com/ansible/ansible/issues/63998
- win_domain_computer - ``sam_account_name`` with missing ``$`` will have it added automatically (https://github.com/ansible-collections/community.windows/pull/93)
- win_domain_computer - add support for offline domain join (https://github.com/ansible-collections/community.windows/pull/93)
- win_domain_group_membership - Add multi-domain forest support - https://github.com/ansible/ansible/issues/59829
- win_domain_user - Added the ``identity`` module option to explicitly set the identity of the user when searching for it - https://github.com/ansible/ansible/issues/45298
- win_firewall- Change req check from wmf version to cmdlets presence - https://github.com/ansible/ansible/issues/63003
- win_firewall_rule - add parameter to support ICMP Types and Codes (https://github.com/ansible/ansible/issues/46809)
- win_iis_webapplication - add new options ``connect_as``, ``username``, ``password``.
- win_iis_webapplication - now uses the current application pool of the website instead of the DefaultAppPool if none was specified.
- win_nssm - Implement additional parameters - (https://github.com/ansible/ansible/issues/62620)
- win_pester - Only execute ``*.tests.ps1`` in ``path`` to match the default behaviour in Pester - https://github.com/ansible/ansible/issues/55736

ngine_io.cloudstack
~~~~~~~~~~~~~~~~~~~

- Added support for SSL CA cert verification (https://github.com/ngine-io/ansible-collection-cloudstack/pull/3)

ngine_io.vultr
~~~~~~~~~~~~~~

- vultr_server_info, vultr_server - Improved handling of discontinued plans (https://github.com/ansible/ansible/issues/66707).

vyos.vyos
~~~~~~~~~

- Add doc plugin fixes (https://github.com/ansible-collections/vyos.vyos/pull/51)

Breaking Changes / Porting Guide
--------------------------------

ansible.windows
~~~~~~~~~~~~~~~

- setup - Make sure ``ansible_date_time.epoch`` is seconds since EPOCH in UTC to mirror the POSIX facts. The ``ansible_date_time.epoch_local`` contains seconds since EPOCH in the local timezone for backwards compatibility
- setup - Will now add the IPv6 scope on link local addresses for ``ansible_ip_addresses``
- setup - ``ansible_processor`` will now return the index before the other values to match the POSIX fact behaviour
- win_find - No longer filters by size on directories, this feature had a lot of bugs, slowed down the module, and not a supported scenario with the ``find`` module.

community.general
~~~~~~~~~~~~~~~~~

- The environment variable for the auth context for the oc.py connection plugin has been corrected (K8S_CONTEXT).  It was using an initial lowercase k by mistake. (https://github.com/ansible-collections/community.general/pull/377).
- bigpanda - the parameter ``message`` was renamed to ``deployment_message`` since ``message`` is used by Ansible Core engine internally.
- cisco_spark - the module option ``message`` was renamed to ``msg``, as ``message`` is used internally in Ansible Core engine (https://github.com/ansible/ansible/issues/39295)
- datadog - the parameter ``message`` was renamed to ``notification_message`` since ``message`` is used by Ansible Core engine internally.
- docker_container - no longer passes information on non-anonymous volumes or binds as ``Volumes`` to the Docker daemon. This increases compatibility with the ``docker`` CLI program. Note that if you specify ``volumes: strict`` in ``comparisons``, this could cause existing containers created with docker_container from Ansible 2.9 or earlier to restart.
- docker_container - support for port ranges was adjusted to be more compatible to the ``docker`` command line utility: a one-port container range combined with a multiple-port host range will no longer result in only the first host port be used, but the whole range being passed to Docker so that a free port in that range will be used.
- hashi_vault lookup - now returns the latest version when using the KV v2 secrets engine. Previously, it returned all versions of the secret which required additional steps to extract and filter the desired version.

community.network
~~~~~~~~~~~~~~~~~

- routeros_facts - allow multiple addresses and neighbors per interface. This makes ``ansible_net_neighbors`` a list instead of a dict (https://github.com/ansible-collections/community.network/pull/6).

Deprecated Features
-------------------

Ansible Base
~~~~~~~~~~~~

- Using the DefaultCallback without the correspodning doc_fragment or copying the documentation.
- hash_behaviour - Deprecate ``hash_behaviour`` for future removal.
- script inventory plugin - The 'cache' option is deprecated and will be removed in 2.12. Its use has been removed from the plugin since it has never had any effect.

ansible.windows
~~~~~~~~~~~~~~~

- win_domain_computer - Deprecated the undocumented ``log_path`` option. This option will be removed in a major release after ``2022-07-01``.
- win_regedit - Deprecated using forward slashes as a path separator, use backslashes to avoid ambiguity between a forward slash in the key name or a forward slash as a path separator. This feature will be removed in a major release after ``2021-07-01``.

community.crypto
~~~~~~~~~~~~~~~~

- openssl_csr - all values for the ``version`` option except ``1`` are deprecated. The value 1 denotes the current only standardized CSR version.

community.general
~~~~~~~~~~~~~~~~~

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
- zabbix_proxy - deprecates ``interface`` sub-options ``type`` and ``main`` when proxy type is set to passive via ``status=passive``. Make sure these suboptions are removed from your playbook as they were never supported by Zabbix in the first place.

community.vmware
~~~~~~~~~~~~~~~~

- vmware_dns_config - Deprecate in favour of new module vmware_host_dns.

Removed Features (previously deprecated)
----------------------------------------

Ansible Base
~~~~~~~~~~~~

- core - remove support for ``check_invalid_arguments`` in ``AnsibleModule``, ``AzureModule`` and ``UTMModule``.

community.crypto
~~~~~~~~~~~~~~~~

- The ``letsencrypt`` module has been removed. Use ``acme_certificate`` instead.

community.general
~~~~~~~~~~~~~~~~~

- core - remove support for ``check_invalid_arguments`` in ``UTMModule``.
- logicmonitor - the module has been removed in 1.0.0 since it is unmaintained and the API used by the module has been turned off in 2017 (https://github.com/ansible-collections/community.general/issues/539, https://github.com/ansible-collections/community.general/pull/541).
- logicmonitor_facts - the module has been removed in 1.0.0 since it is unmaintained and the API used by the module has been turned off in 2017 (https://github.com/ansible-collections/community.general/issues/539, https://github.com/ansible-collections/community.general/pull/541).
- pacman - Removed deprecated ``recurse`` option, use ``extra_args=--recursive`` instead

community.vmware
~~~~~~~~~~~~~~~~

- vmware_guest_find - Removed deprecated ``datacenter`` option
- vmware_vmkernel - Removed deprecated ``ip_address`` option; use sub-option ip_address in the network option instead
- vmware_vmkernel - Removed deprecated ``subnet_mask`` option; use sub-option subnet_mask in the network option instead

community.windows
~~~~~~~~~~~~~~~~~

- win_disk_image - removed the deprecated return value ``mount_path`` in favour of ``mount_paths``.

Security Fixes
--------------

Ansible Base
~~~~~~~~~~~~

- **security issue** - Convert CLI provided passwords to text initially, to prevent unsafe context being lost when converting from bytes->text during post processing of PlayContext. This prevents CLI provided passwords from being incorrectly templated (CVE-2019-14856)
- **security issue** - Redact cloud plugin secrets in ansible-test when running integration tests using cloud plugins. Only present in 2.9.0b1.
- **security issue** - TaskExecutor - Ensure we don't erase unsafe context in TaskExecutor.run on bytes. Only present in 2.9.0beta1 (https://github.com/ansible/ansible/issues/62237)
- **security issue** - The ``subversion`` module provided the password via the svn command line option ``--password`` and can be retrieved from the host's /proc/<pid>/cmdline file. Update the module to use the secure ``--password-from-stdin`` option instead, and add a warning in the module and in the documentation if svn version is too old to support it. (CVE-2020-1739)
- **security issue** - Update ``AnsibleUnsafeText`` and ``AnsibleUnsafeBytes`` to maintain unsafe context by overriding ``.encode`` and ``.decode``. This prevents future issues with ``to_text``, ``to_bytes``, or ``to_native`` removing the unsafe wrapper when converting between string types (CVE-2019-14856)
- **security issue** - properly hide parameters marked with ``no_log`` in suboptions when invalid parameters are passed to the module (CVE-2019-14858)
- **security issue** win_unzip - normalize paths in archive to ensure extracted files do not escape from the target directory (CVE-2020-1737)
- **security_issue** - create temporary vault file with strict permissions when editing and prevent race condition (CVE-2020-1740)
- Ensure we get an error when creating a remote tmp if it already exists. CVE-2020-1733
- In fetch action, avoid using slurp return to set up dest, also ensure no dir traversal CVE-2020-1735.
- ansible-galaxy - Error when install finds a tar with a file that will be extracted outside the collection install directory - CVE-2020-10691

community.general
~~~~~~~~~~~~~~~~~

- **SECURITY** - CVE-2019-14904 - solaris_zone module accepts zone name and performs actions related to that. However, there is no user input validation done while performing actions. A malicious user could provide a crafted zone name which allows executing commands into the server manipulating the module behaviour. Adding user input validation as per Solaris Zone documentation fixes this issue.
- **security issue** - Ansible: Splunk and Sumologic callback plugins leak sensitive data in logs (CVE-2019-14864)
- ldap_attr, ldap_entry - The ``params`` option has been removed in Ansible-2.10 as it circumvents Ansible's option handling.  Setting ``bind_pw`` with the ``params`` option was disallowed in Ansible-2.7, 2.8, and 2.9 as it was insecure.  For information about this policy, see the discussion at: https://meetbot.fedoraproject.org/ansible-meeting/2017-09-28/ansible_dev_meeting.2017-09-28-15.00.log.html This fixes CVE-2020-1746

community.kubernetes
~~~~~~~~~~~~~~~~~~~~

- kubectl - Warn about information disclosure when using options like ``kubectl_password``, ``kubectl_extra_args``, and ``kubectl_token`` to pass data through to the command line using the ``kubectl`` connection plugin (https://github.com/ansible-collections/community.kubernetes/pull/51).

Bugfixes
--------

Ansible Base
~~~~~~~~~~~~

- **security issue** atomic_move - change default permissions when creating temporary files so they are not world readable (https://github.com/ansible/ansible/issues/67794) (CVE-2020-1736)
- ActionBase - Add new ``cleanup`` method that is explicitly run by the ``TaskExecutor`` to ensure that the shell plugins ``tmpdir`` is always removed. This change means that individual action plugins need not be responsible for removing the temporary directory, which ensures that we don't have code paths that accidentally leave behind the temporary directory.
- Add example setting for ``collections_paths`` parameter to ``examples/ansible.cfg``
- Add missing gcp modules to gcp module defaults group
- Added support for Flatcar Container Linux in distribution and hostname modules. (https://github.com/ansible/ansible/pull/69627)
- Added support for OSMC distro in hostname module (https://github.com/ansible/ansible/issues/66189).
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
- Correctly process raw_params in add_hosts.
- Create an ``import_module`` compat util, for use across the codebase, to allow collection loading to work properly on Python26
- DUPLICATE_YAML_DICT_KEY - Fix error output when configuration option DUPLICATE_YAML_DICT_KEY is set to error (https://github.com/ansible/ansible/issues/65366)
- Do not keep empty blocks in PlayIterator after skipping tasks with tags.
- Ensure DataLoader temp files are removed at appropriate times and that we observe the LOCAL_TMP setting.
- Ensure that ``--version`` works with non-ascii ansible project paths (https://github.com/ansible/ansible/issues/66617)
- Ensure that keywords defined as booleans are correctly interpreting their input, before patch any random string would be interpreted as False
- Ensure we don't allow ansible_facts subkey of ansible_facts to override top level, also fix 'deprefixing' to prevent key transforms.
- Fact Delegation - Add ability to indicate which facts must always be delegated. Primarily for ``discovered_interpreter_python`` right now, but extensible later. (https://github.com/ansible/ansible/issues/61002)
- Fix ``delegate_facts: true`` when ``ansible_python_interpreter`` is not set. (https://github.com/ansible/ansible/issues/70168)
- Fix a bug when a host was not removed from a play after ``meta: end_host`` and as a result the host was still present in ``ansible_play_hosts`` and ``ansible_play_batch`` variables.
- Fix an issue with the ``fileglob`` plugin where passing a subdirectory of non-existent directory would cause it to fail - https://github.com/ansible/ansible/issues/69450
- Fix case sensitivity for ``lookup()`` (https://github.com/ansible/ansible/issues/66464)
- Fix collection install error that happened if a dependency specified dependencies to be null (https://github.com/ansible/ansible/issues/67574).
- Fix https://github.com/ansible/galaxy-dev/issues/96 Add support for automation-hub authentication to ansible-galaxy
- Fix incorrect "Could not match supplied host pattern" warning (https://github.com/ansible/ansible/issues/66764)
- Fix issue git module cannot use custom `key_file` or `ssh_opts` as non-root user on system with noexec `/tmp` (https://github.com/ansible/ansible/issues/30064).
- Fix issue git module ignores remote_tmp (https://github.com/ansible/ansible/issues/33947).
- Fix issue where the collection loader tracebacks if ``collections_paths = ./`` is set in the config
- Fix issue with callbacks ``set_options`` method that was not called with collections
- Fix label lookup in the default callback for includes (https://github.com/ansible/ansible/issues/65904)
- Fix regression when ``ansible_failed_task`` and ``ansible_failed_result`` are not defined in the rescue block (https://github.com/ansible/ansible/issues/64789)
- Fix string parsing of inline vault strings for plugin config variable sources
- Fix traceback when printing ``HostVars`` on native Jinja2 (https://github.com/ansible/ansible/issues/65365)
- Fixed a bug with the copy action plugin where mode=preserve was being passed on symlink files and causing a traceback (https://github.com/ansible/ansible/issues/68471).
- Fixed the equality check for IncludedFiles to ensure they are not accidently merged when process_include_results runs.
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
- Role Installation - Ensure that a role containing files with non-ascii characters can be installed (https://github.com/ansible/ansible/issues/69133)
- RoleRequirement - include stderr in the error message if a scm command fails (https://github.com/ansible/ansible/issues/41336)
- SSH plugin - Improve error message when ssh client is not found on the host
- Sanitize no_log values from any response keys that might be returned from the uri module.
- Skipping of become for ``network_cli`` connections now works when ``network_cli`` is sourced from a collection.
- Stop adding the connection variables to the output results
- Strictly check string datatype for 'tasks_from', 'vars_from', 'defaults_from', and 'handlers_from' in include_role (https://github.com/ansible/ansible/issues/68515).
- Strip no log values from module response keys (https://github.com/ansible/ansible/issues/68400)
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
- ansible-galaxy role - Fix issue where ``--server`` was not being used for certain ``ansible-galaxy role`` actions - https://github.com/ansible/ansible/issues/61609
- ansible-galaxy- On giving an invalid subcommand to ansible-galaxy, the help would be shown only for role subcommand (collection subcommand help is not shown). With this change, the entire help for ansible-galaxy (same as ansible-galaxy --help) is displayed along with the help for role subcommand. (https://github.com/ansible/ansible/issues/69009)
- ansible-inventory - Fix long standing bug not loading vars plugins for group vars relative to the playbook dir when the '--playbook-dir' and '--export' flags are used together.
- ansible-inventory - Fix regression loading vars plugins. (https://github.com/ansible/ansible/issues/65064)
- ansible-inventory - Properly hide arguments that should not be shown (https://github.com/ansible/ansible/issues/61604)
- ansible-inventory - Restore functionality to allow ``--graph`` to be limited by a host pattern
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
- ansible-test validate-modules - Fix arg spec collector for PowerShell to find utils in both a collection and base.
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
- facts - introduce fact "ansible_processor_nproc" which reflects the number of vcpus available to processes (falls back to the number of vcpus available to the scheduler)
- file - Removed unreachable code in module
- file - change ``_diff_peek`` in argument spec to be the correct type, which is ``bool`` (https://github.com/ansible/ansible/issues/59433)
- file - return ``'state': 'absent'`` when a file does not exist (https://github.com/ansible/ansible/issues/66171)
- find - clarify description of ``contains`` (https://github.com/ansible/ansible/issues/61983)
- fix issue in which symlinked collection cannot be listed, though the docs/plugins can be loaded if referenced directly.
- fix issue with inventory_hostname and delegated host vars mixing on connection settings.
- fix wrong command line length calculation in ``ansible-console`` when long command inputted
- for those running uids for invalid users (containers), fallback to uid=<uid> when logging fixes #68007
- free strategy - Include failed hosts when filtering notified hosts for handlers. The strategy base should determine whether or not to run handlers on those hosts depending on whether forcing handlers is enabled (https://github.com/ansible/ansible/issues/65254).
- galaxy - Fix an AttributeError on ansible-galaxy install with an empty requirements.yml (https://github.com/ansible/ansible/issues/66725).
- get_url - Don't treat no checksum as a checksum match (https://github.com/ansible/ansible/issues/61978)
- get_url pass incorrect If-Modified-Since header (https://github.com/ansible/ansible/issues/67417)
- git - when force=True, apply --force flag to git fetches as well
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
- lineinfile - properly handle inserting a line when backrefs are enabled and the line already exists in the file (https://github.com/ansible/ansible/issues/63756)
- lineinfile - use ``module.tmpdir`` to allow configuration of the remote temp directory (https://github.com/ansible/ansible/issues/68218)
- lineinfile - use correct index value when inserting a line at the end of a file (https://github.com/ansible/ansible/issues/63684)
- loops - Do not indiscriminately mark loop items as unsafe, only apply unsafe to ``with_`` style loops. The items from ``loop`` should not be explicitly wrapped in unsafe. The underlying templating mechanism should dictate this. (https://github.com/ansible/ansible/issues/64379)
- make ``no_log=False`` on a module option silence the ``no_log`` warning (https://github.com/ansible/ansible/issues/49465 https://github.com/ansible/ansible/issues/64656)
- match docs for ssh and ensure pipelining is configurable per connection plugin.
- module executor - Address issue where changes to Ansiballz module code, change the behavior of module execution as it pertains to ``__file__`` and ``sys.modules`` (https://github.com/ansible/ansible/issues/64664)
- module_defaults - support candidate action names for relocated content
- module_defaults - support short group names for content relocated to collections
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
- psexec - Fix issue where the Kerberos package was not detected as being available.
- psexec - Fix issue where the ``interactive`` option was not being passed down to the library.
- reboot, win_reboot - add ``boot_time_command`` parameter to override the default command used to determine whether or not a system was rebooted (https://github.com/ansible/ansible/issues/58868)
- remove update/restore of vars from play_context as it is now redundant.
- replace use of deprecated functions from ``ansible.module_utils.basic``.
- roles - Ensure that ``allow_duplicates: true`` enables to run single role multiple times (https://github.com/ansible/ansible/issues/64902)
- runas - Fix the ``runas`` ``become_pass`` variable fallback from ``ansible_runas_runas`` to ``ansible_runas_pass``
- service_facts - Now correctly parses systemd list-unit-files for systemd >=245
- setup - properly detect yum package manager for IBM i.
- setup - service_mgr - detect systemd even if it isn't running, such as during a container build
- shell - fix quoting of mkdir command in creation of remote_tmp in order to allow spaces and other special characters (https://github.com/ansible/ansible/issues/69577).
- shell cmd - Properly escape double quotes in the command argument
- splunk httpapi plugin - switch from splunk.enterprise_security to splunk.es in runtime.yml to reflect upstream change of Collection Name
- ssh connection plugin - use ``get_option()`` rather than ``_play_context`` to ensure ``ANSBILE_SSH_ARGS`` are applied properly (https://github.com/ansible/ansible/issues/70437)
- synchronize - allow data to be passed between two managed nodes when using the docker connection plugin (https://github.com/ansible/ansible/pull/65698)
- synchronize - fix password authentication on Python 2 (https://github.com/ansible/ansible/issues/56629)
- sysctl - Remove FIXME comments to avoid confusion
- systemd - don't require systemd to be running to enable/disable or mask/unmask units
- systemd - the module should fail in check_mode when service not found on host (https://github.com/ansible/ansible/pull/68136).
- sysvinit - Add missing parameter ``module`` in call to ``daemonize()``.
- template lookup - ensure changes to the templar in the lookup, do not affect the templar context outside of the lookup (https://github.com/ansible/ansible/issues/60106)
- template lookup - fix regression when templating hostvars (https://github.com/ansible/ansible/issues/63940)
- the default parsing will now show existing JSON errors and not just YAML (last attempted), also we avoid YAML parsing when we know we only want JSON issue
- throttle: the linear strategy didn't always stuck with the throttle limit
- unarchive - Remove incorrect and unused function arguments.
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

cisco.meraki
~~~~~~~~~~~~

- Fixed sanity errors in all modules including documentation and argument specs
- Remove unnecessary files from the collection package, significantly reduces package size
- meraki_ssid - Specifying tags for VLAN information would crash as it was an improper type
- meraki_webhook - Fix crash with missing variable
- meraki_webhook - Fix response when creating webhook test

community.crypto
~~~~~~~~~~~~~~~~

- ACME modules: fix bug in ACME v1 account update code
- ACME modules: make sure some connection errors are handled properly
- ACME modules: support Buypass' ACME v1 endpoint
- acme_certificate - fix crash when module is used with Python 2.x.
- acme_certificate - fix misbehavior when ACME v1 is used with ``modify_account`` set to ``false``.
- ecs_certificate - Always specify header ``connection: keep-alive`` for ECS API connections.
- ecs_certificate - Fix formatting of contents of ``full_chain_path``.
- get_certificate - Fix cryptography backend when pyopenssl is unavailable (https://github.com/ansible/ansible/issues/67900)
- openssh_keypair - add logic to avoid breaking password protected keys.
- openssh_keypair - fixes idempotence issue with public key (https://github.com/ansible/ansible/issues/64969).
- openssh_keypair - public key's file attributes (permissions, owner, group, etc.) are now set to the same values as the private key.
- openssl_* modules - prevent crash on fingerprint determination in FIPS mode (https://github.com/ansible/ansible/issues/67213).
- openssl_certificate - When provider is ``entrust``, use a ``connection: keep-alive`` header for ECS API connections.
- openssl_certificate - ``provider`` option was documented as required, but it was not checked whether it was provided. It is now only required when ``state`` is ``present``.
- openssl_certificate - fix ``assertonly`` provider certificate verification, causing 'private key mismatch' and 'subject mismatch' errors.
- openssl_certificate and openssl_csr - fix Ed25519 and Ed448 private key support for ``cryptography`` backend. This probably needs at least cryptography 2.8, since older versions have problems with signing certificates or CSRs with such keys. (https://github.com/ansible/ansible/issues/59039, PR https://github.com/ansible/ansible/pull/63984)
- openssl_csr - a warning is issued if an unsupported value for ``version`` is used for the ``cryptography`` backend.
- openssl_csr - the module will now enforce that ``privatekey_path`` is specified when ``state=present``.
- openssl_publickey - fix a module crash caused when pyOpenSSL is not installed (https://github.com/ansible/ansible/issues/67035).

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
- docker connection plugin - do not prefix remote path if running on Windows containers.
- docker_compose - add a condition to prevent service startup if parameter ``stopped`` is true. Otherwise, the service will be started on each play and stopped again immediately due to the ``stopped`` parameter and breaks the idempotency of the module (https://github.com/ansible-collections/community.general/issues/532).
- docker_compose - disallow usage of the parameters ``stopped`` and ``restarted`` at the same time. This breaks also the idempotency (https://github.com/ansible-collections/community.general/issues/532).
- docker_compose - fix issue where docker deprecation warning results in ansible erroneously reporting a failure
- docker_container - fix idempotency for IP addresses for networks. The old implementation checked the effective IP addresses assigned by the Docker daemon, and not the specified ones. This causes idempotency issues for containers which are not running, since they have no effective IP addresses assigned.
- docker_container - fix network idempotence comparison error.
- docker_container - improve error behavior when parsing port ranges fails.
- docker_container - make sure that when image is missing, check mode indicates a change (image will be pulled).
- docker_container - passing ``test: [NONE]`` now actually disables the image's healthcheck, as documented.
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
- docker_swarm_service - ``source`` must no longer be specified for ``tmpfs`` mounts.
- docker_swarm_service - fix task always reporting as changed when using ``healthcheck.start_period``.
- docker_swarm_service - passing ``test: [NONE]`` now actually disables the image's healthcheck, as documented.
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
- ipa modules - fix error when IPA_HOST is empty and fallback on DNS (https://github.com/ansible-collections/community.general/pull/241)
- java_keystore - make module compatible with older Ansible versions (https://github.com/ansible-collections/community.general/pull/306).
- jira - printing full error message from jira server (https://github.com/ansible-collections/community.general/pull/22).
- jira - transition issue not working (https://github.com/ansible-collections/community.general/issues/109).
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
- nmcli - typecast parameters to string as required (https://github.com/ansible/ansible/issues/59095).
- nsupdate - Do not try fixing non-existing TXT values (https://github.com/ansible/ansible/issues/63364)
- nsupdate - Fix zone name lookup of internal/private zones (https://github.com/ansible/ansible/issues/62052)
- one_vm - improve file handling by using a context manager.
- ovirt - don't ignore ``instance_cpus`` parameter
- pacman - Fix pacman output parsing on localized environment. (https://github.com/ansible/ansible/issues/65237)
- pacman - fix module crash with ``IndexError: list index out of range`` (https://github.com/ansible/ansible/issues/63077)
- pamd - Bugfix for attribute error when removing the first or last line
- parted - added 'undefined' align option to support parted versions < 2.1 (https://github.com/ansible-collections/community.general/pull/405).
- parted - consider current partition state even in check mode (https://github.com/ansible-collections/community.general/issues/183).
- passwordstore lookup - Honor equal sign in userpass
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
- postgresql_privs - fix sorting lists with None elements for python3 (https://github.com/ansible/ansible/issues/65761).
- postgresql_privs - sort results before comparing so that the values are compared and not the result of ``.sort()`` (https://github.com/ansible/ansible/pull/65125)
- postgresql_privs.py - fix reports as changed behavior of module when using ``type=default_privs`` (https://github.com/ansible/ansible/issues/64371).
- postgresql_publication - fix typo in module.warn method name (https://github.com/ansible/ansible/issues/64582).
- postgresql_publication - use query params arg with cursor object (https://github.com/ansible/ansible/issues/65404).
- postgresql_query - improve file handling by using a context manager.
- postgresql_query - the module doesn't support non-ASCII characters in SQL files with Python3 (https://github.com/ansible/ansible/issues/65367).
- postgresql_schema - use query parameters with cursor object (https://github.com/ansible/ansible/pull/65679).
- postgresql_sequence - use query parameters with cursor object (https://github.com/ansible/ansible/pull/65787).
- postgresql_set - fix converting value to uppercase (https://github.com/ansible/ansible/issues/67377).
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
- redhat_subscription - do not set the default quantity to ``1`` when no quantity is provided (https://github.com/ansible/ansible/issues/66478)
- replace use of deprecated functions from ``ansible.module_utils.basic``.
- rshm_repository - reduce execution time when changed is False (https://github.com/ansible-collections/community.general/pull/458).
- runas - Fix the ``runas`` ``become_pass`` variable fallback from ``ansible_runas_runas`` to ``ansible_runas_pass``
- scaleway - Fix bug causing KeyError exception on JSON http requests. (https://github.com/ansible-collections/community.general/pull/444)
- scaleway: use jsonify unmarshaller only for application/json requests to avoid breaking the multiline configuration with requests in text/plain (https://github.com/ansible/ansible/issues/65036)
- scaleway_compute - fix transition handling that could cause errors when removing a node (https://github.com/ansible-collections/community.general/pull/444).
- scaleway_compute(check_image_id): use get image instead loop on first page of images results
- sesu - make use of the prompt specified in the code
- slack - Fix ``thread_id`` data type
- slackpkg - fix matching some special cases in package names (https://github.com/ansible-collections/community.general/pull/505).
- slackpkg - fix name matching in package installation (https://github.com/ansible-collections/community.general/issues/450).
- spacewalk inventory - improve file handling by using a context manager.
- syslog_json callback - fix plugin exception when running (https://github.com/ansible-collections/community.general/issues/407).
- syslogger callback plugin - remove check mode support since it did nothing anyway
- terraform - adding support for absolute paths additionally to the relative path within project_path (https://github.com/ansible/ansible/issues/58578)
- terraform - reset out and err before plan creation (https://github.com/ansible/ansible/issues/64369)
- terraform module - fixes usage for providers not supporting workspaces
- yarn - Return correct values when running yarn in check mode (https://github.com/ansible-collections/community.general/pull/153).
- yarn - handle no version when installing module by name (https://github.com/ansible/ansible/issues/55097)
- zabbix_action - arguments ``event_source`` and ``esc_period`` no longer required when ``state=absent``
- zabbix_host - fixed inventory_mode key error, which occurs with Zabbix 4.4.1 or more (https://github.com/ansible/ansible/issues/65304).
- zabbix_host - was not possible to update a host where visible_name was not set in zabbix
- zabbix_mediatype - Fixed to support zabbix 4.4 or more and python3 (https://github.com/ansible/ansible/pull/67693)
- zabbix_template - fixed error when providing empty ``link_templates`` to the module (see https://github.com/ansible/ansible/issues/66417)
- zabbix_template - fixed invalid (non-importable) output provided by exporting XML (see https://github.com/ansible/ansible/issues/66466)
- zabbix_user - Fixed an issue where module failed with zabbix 4.4 or above (see https://github.com/ansible/ansible/pull/67475)
- zfs_delegate_admin - add missing choices diff/hold/release to the permissions parameter (https://github.com/ansible-collections/community.general/pull/278)

community.kubernetes
~~~~~~~~~~~~~~~~~~~~

- Fix suboption docs structure for inventory plugins (https://github.com/ansible-collections/community.kubernetes/pull/103).
- Handle invalid kubeconfig parsing error (https://github.com/ansible-collections/community.kubernetes/pull/119).
- Make sure Service changes run correctly in check_mode (https://github.com/ansible-collections/community.kubernetes/pull/84).
- Make sure extra files are not included in built collection (https://github.com/ansible-collections/community.kubernetes/pull/85).
- Update GitHub Actions workflow for better CI stability (https://github.com/ansible-collections/community.kubernetes/pull/78).
- k8s - Add exception handling when retrieving k8s client (https://github.com/ansible-collections/community.kubernetes/pull/54).
- k8s - Fix argspec for 'elements' (https://github.com/ansible-collections/community.kubernetes/issues/13).
- k8s - Use ``from_yaml`` filter with lookup examples in ``k8s`` module documentation examples (https://github.com/ansible-collections/community.kubernetes/pull/56).
- k8s_info - remove unneccessary k8s_facts deprecation notice (https://github.com/ansible-collections/community.kubernetes/pull/97).
- k8s_log - Module no longer attempts to parse log as JSON (https://github.com/ansible-collections/community.kubernetes/pull/69).
- k8s_scale - Fix scale wait and add tests (https://github.com/ansible-collections/community.kubernetes/pull/100).
- k8s_service - Fix argspec (https://github.com/ansible-collections/community.kubernetes/issues/33).
- kubectl - Fix documentation in kubectl connection plugin (https://github.com/ansible-collections/community.kubernetes/pull/52).
- raw - handle condition when definition is none (https://github.com/ansible-collections/community.kubernetes/pull/139).

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
- edgeos_config - fix issue where module would silently filter out encrypted passwords
- edgeos_config - fixed issue of handling single quotation marks. Now fails when unmatched (odd numbers)
- edgeos_config - fixed issue where any change in check mode would cause all subsequent tasks to be treated as changes
- netscaler_nitro_request - use all filters for get_filtered instead of only the first one (https://github.com/ansible-collections/community.network/issues/48).
- plugins-netconf-ce - Fix failed to get version information.
- plugins-netconf-ce - to get attribute 'set-id' from rpc-reply.
- routeros module_utils - created a ``try``/``except`` block on the function ``get_capabilities`` (https://github.com/ansible-collections/community.network/pull/27).
- routeros_facts - Prevent crash of module when ``ipv6`` package is not installed

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
- vmware_content_deploy_template - Added param content_library to the main function
- vmware_deploy_ovf - Fixed ova deploy error occur if vm exists
- vmware_dvs_portgroup - Implemented configuration changes on an existing Distributed vSwitch portgroup.
- vmware_dvs_portgroup_find - Cast variable to integer for comparison.
- vmware_guest - Add ability to upgrade the guest hardware version to latest fix issue (https://github.com/ansible/ansible/issues/56273).
- vmware_guest - Allow '-' (Dash) special char in windows DNS name.
- vmware_guest - Exclude dvswitch_name from triggering guest os customization.
- vmware_guest - Updated reference link to vapp_properties property
- vmware_host_capability_facts - Fixed vSphere API legacy version errors occur in pyvmomi 7.0 and later
- vmware_host_capability_info - Fixed vSphere API legacy version errors occur in pyvmomi 7.0 and later
- vmware_host_facts - handle facts when ESXi hostsystem is poweredoff (https://github.com/ansible-collections/vmware/issues/183).
- vmware_host_firewall_manager - Ensure we can set rule with no ``allowed_hosts`` key (https://github.com/ansible/ansible/issues/61332)
- vmware_host_firewall_manager - Fixed creating IP specific firewall rules with Python 2 (https://github.com/ansible/ansible/issues/67303)
- vmware_host_vmhba_info - fixed node_wwn and port_wwn for FC HBA to hexadecimal format(https://github.com/ansible/ansible/issues/63045).
- vmware_vcenter_settings - Fixed when runtime_settings parameters not defined occur error(https://github.com/ansible/ansible/issues/66713)
- vmware_vcenter_statistics - Fix some corner cases like increasing some interval and decreasing another at the same time.
- vmware_vm_inventory inventory plugin, use the port value while connecting to vCenter (https://github.com/ansible/ansible/issues/64096).
- vmware_vmkernel - Remove duplicate checks.
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
- win_timezone - Allow for _dstoff timezones
- win_unzip - Fix support for paths with square brackets not being detected properly

hetzner.hcloud
~~~~~~~~~~~~~~

- hcloud inventory plugin - Allow usage of hcloud.yml and hcloud.yaml - this was removed by error within the migration from build-in ansible to our collection

ngine_io.vultr
~~~~~~~~~~~~~~

- vultr - Fixed the issue retry max delay param was ignored.

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

Lookup
~~~~~~

- ansible.builtin.unvault - read vaulted file(s) contents
- community.general.etcd3 - Get key values from etcd3 server
- community.general.lmdb_kv - fetch data from LMDB

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

community.crypto
~~~~~~~~~~~~~~~~

- community.crypto.ecs_domain - Request validation of a domain with the Entrust Certificate Services (ECS) API
- community.crypto.x509_crl - Generate Certificate Revocation Lists (CRLs)
- community.crypto.x509_crl_info - Retrieve information on Certificate Revocation Lists (CRLs)

community.general
~~~~~~~~~~~~~~~~~

Cloud
^^^^^

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
- community.general.lbu - Local Backup Utility for Alpine Linux

community.kubernetes
~~~~~~~~~~~~~~~~~~~~

- community.kubernetes.helm - Manages Kubernetes packages with the Helm package manager
- community.kubernetes.helm_info - Get information from Helm package deployed inside the cluster
- community.kubernetes.helm_repository - Add and remove Helm repository
- community.kubernetes.k8s_exec - Execute command in Pod
- community.kubernetes.k8s_log - Fetch logs from Kubernetes resources

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

frr.frr
~~~~~~~

- frr.frr.frr_bgp - Configure global BGP settings on Free Range Routing(FRR).
- frr.frr.frr_facts - Collect facts from remote devices running Free Range Routing (FRR).

hetzner.hcloud
~~~~~~~~~~~~~~

- hetzner.hcloud.hcloud_floating_ip - Create and manage cloud Floating IPs on the Hetzner Cloud.
- hetzner.hcloud.hcloud_load_balancer - Create and manage cloud Load Balancers on the Hetzner Cloud.
- hetzner.hcloud.hcloud_load_balancer_network - Manage the relationship between Hetzner Cloud Networks and Load Balancers
- hetzner.hcloud.hcloud_load_balancer_service - Create and manage the services of cloud Load Balancers on the Hetzner Cloud.
- hetzner.hcloud.hcloud_load_balancer_target - Manage Hetzner Cloud Load Balancer targets
- hetzner.hcloud.hcloud_load_balancer_type_info - Gather infos about the Hetzner Cloud Load Balancer types.

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

ngine_io.vultr
~~~~~~~~~~~~~~

- ngine_io.vultr.vultr_plan_baremetal_info - Gather information about the Vultr Bare Metal plans available.
- ngine_io.vultr.vultr_server_baremetal - Manages baremetal servers on Vultr.

openvswitch.openvswitch
~~~~~~~~~~~~~~~~~~~~~~~

- openvswitch.openvswitch.openvswitch_bridge - Manage Open vSwitch bridges
- openvswitch.openvswitch.openvswitch_db - Configure open vswitch database.
- openvswitch.openvswitch.openvswitch_port - Manage Open vSwitch ports

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
