=======================
Ansible 4 Release Notes
=======================

This changelog describes changes since Ansible 3.0.0.

.. contents::
  :local:
  :depth: 2

v4.0.0a2
========

.. contents::
  :local:
  :depth: 2

Release Summary
---------------

Release Date: 2021-03-23

`Porting Guide <https://docs.ansible.com/ansible/devel/porting_guides.html>`_

Ansible-core
------------

Ansible 4.0.0a2 contains Ansible-core version 2.11.0b3.
This is a newer version than version 2.11.0b2 contained in the previous Ansible release.

The changes are reported in the combined changelog below.

Changed Collections
-------------------

If not mentioned explicitly, the changes are reported in the combined changelog below.

+-----------------------+-----------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| Collection            | Ansible 4.0.0a1 | Ansible 4.0.0a2 | Notes                                                                                                                        |
+=======================+=================+=================+==============================================================================================================================+
| awx.awx               | 17.1.0          | 18.0.0          | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+-----------------------+-----------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.crypto      | 1.5.0           | 1.6.0           |                                                                                                                              |
+-----------------------+-----------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.general     | 2.2.0           | 2.3.0           |                                                                                                                              |
+-----------------------+-----------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.hashi_vault | 1.1.2           | 1.1.3           |                                                                                                                              |
+-----------------------+-----------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.network     | 2.0.1           | 2.1.0           |                                                                                                                              |
+-----------------------+-----------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| community.sops        | 1.0.5           | 1.0.6           |                                                                                                                              |
+-----------------------+-----------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| cyberark.pas          | 1.0.5           | 1.0.6           | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
+-----------------------+-----------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| hetzner.hcloud        | 1.3.0           | 1.3.1           |                                                                                                                              |
+-----------------------+-----------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| ovirt.ovirt           | 1.4.0           | 1.4.1           |                                                                                                                              |
+-----------------------+-----------------+-----------------+------------------------------------------------------------------------------------------------------------------------------+

Major Changes
-------------

Ansible-core
~~~~~~~~~~~~

- AnsibleModule - use ``ArgumentSpecValidator`` class for validating argument spec and remove private methods related to argument spec validation. Any modules using private methods should now use the ``ArgumentSpecValidator`` class or the appropriate validation function.

Minor Changes
-------------

Ansible-core
~~~~~~~~~~~~

- Callbacks - Migrate more places in the ``TaskExecutor`` to sending callbacks directly over the queue, instead of sending them as ``TaskResult`` and short circuiting in the Strategy to send the callback. This enables closer to real time callbacks of retries and loop results (https://github.com/ansible/ansible/issues/73899)
- setup - fix distribution facts for Older Amazon Linux with ``/etc/os-release`` (https://github.com/ansible/ansible/issues/73946).

community.crypto
~~~~~~~~~~~~~~~~

- acme module_utils - the ``acme`` module_utils has been split up into several Python modules (https://github.com/ansible-collections/community.crypto/pull/184).
- acme_* modules - codebase refactor which should not be visible to end-users (https://github.com/ansible-collections/community.crypto/pull/184).
- acme_* modules - support account key passphrases for ``cryptography`` backend (https://github.com/ansible-collections/community.crypto/issues/197, https://github.com/ansible-collections/community.crypto/pull/207).
- acme_certificate_revoke - support revoking by private keys that are passphrase protected for ``cryptography`` backend (https://github.com/ansible-collections/community.crypto/pull/207).
- acme_challenge_cert_helper - add ``private_key_passphrase`` parameter (https://github.com/ansible-collections/community.crypto/pull/207).

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

community.network
~~~~~~~~~~~~~~~~~

- edgeos_config - match the space after ``set`` and ``delete`` commands (https://github.com/ansible-collections/community.network/pull/199).
- nclu - execute ``net commit description <description>`` only if changed ``net pending``'s diff field (https://github.com/ansible-collections/community.network/pull/219).

Deprecated Features
-------------------

community.crypto
~~~~~~~~~~~~~~~~

- acme module_utils - the ``acme`` module_utils (``ansible_collections.community.crypto.plugins.module_utils.acme``) is deprecated and will be removed in community.crypto 2.0.0. Use the new Python modules in the ``acme`` package instead (``ansible_collections.community.crypto.plugins.module_utils.acme.xxx``) (https://github.com/ansible-collections/community.crypto/pull/184).

Security Fixes
--------------

community.network
~~~~~~~~~~~~~~~~~

- avi_cloudconnectoruser - mark the ``azure_userpass``, ``gcp_credentials``, ``oci_credentials``, and ``tencent_credentials`` parameters as ``no_log`` to prevent leaking of secret values (https://github.com/ansible-collections/community.network/pull/223).
- avi_sslkeyandcertificate - mark the ``enckey_base64`` parameter as ``no_log`` to prevent potential leaking of secret values (https://github.com/ansible-collections/community.network/pull/223).
- avi_webhook - mark the ``verification_token`` parameter as ``no_log`` to prevent potential leaking of secret values (https://github.com/ansible-collections/community.network/pull/223).

Bugfixes
--------

Ansible-core
~~~~~~~~~~~~

- Fix adding unrelated candidate names to the plugin loader redirect list.
- Strategy - When building the task in the Strategy from the Worker, ensure it is properly marked as finalized and squashed. Addresses an issue with ``ansible_failed_task``. (https://github.com/ansible/ansible/issues/57399)
- ansible-pull - Run all playbooks that when multiple are supplied via the command line (https://github.com/ansible/ansible/issues/72708)
- find module, fix default pattern when use_regex is true.

community.crypto
~~~~~~~~~~~~~~~~

- action_module plugin helper - make compatible with latest changes in ansible-core 2.11.0b3 (https://github.com/ansible-collections/community.crypto/pull/202).
- openssl_privatekey_pipe - make compatible with latest changes in ansible-core 2.11.0b3 (https://github.com/ansible-collections/community.crypto/pull/202).

community.general
~~~~~~~~~~~~~~~~~

- Mark various module options with ``no_log=False`` which have a name that potentially could leak secrets, but which do not (https://github.com/ansible-collections/community.general/pull/2001).
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

hetzner.hcloud
~~~~~~~~~~~~~~

- hcloud_server - fix a crash related to check mode if ``state=started`` or ``state=stopped`` (https://github.com/ansible-collections/hetzner.hcloud/issues/54).

ovirt.ovirt
~~~~~~~~~~~

- hosted_engine_setup - Fix auth revoke (https://github.com/oVirt/ovirt-ansible-collection/pull/237).

New Plugins
-----------

Filter
~~~~~~

- community.general.from_csv - Converts CSV text input into list of dicts

New Modules
-----------

community.general
~~~~~~~~~~~~~~~~~

Net Tools
^^^^^^^^^

- community.general.gandi_livedns - Manage Gandi LiveDNS records

Pritunl
.......

- community.general.pritunl_user - Manage Pritunl Users using the Pritunl API
- community.general.pritunl_user_info - List Pritunl Users using the Pritunl API

Unchanged Collections
---------------------

- amazon.aws (still version 1.4.1)
- ansible.netcommon (still version 2.0.0)
- ansible.posix (still version 1.2.0)
- ansible.utils (still version 2.0.1)
- ansible.windows (still version 1.4.0)
- arista.eos (still version 2.0.0)
- azure.azcollection (still version 1.4.0)
- check_point.mgmt (still version 2.0.0)
- chocolatey.chocolatey (still version 1.0.2)
- cisco.aci (still version 2.0.0)
- cisco.asa (still version 2.0.0)
- cisco.intersight (still version 1.0.12)
- cisco.ios (still version 2.0.0)
- cisco.iosxr (still version 2.0.0)
- cisco.meraki (still version 2.2.1)
- cisco.mso (still version 1.1.0)
- cisco.nso (still version 1.0.3)
- cisco.nxos (still version 2.0.0)
- cisco.ucs (still version 1.6.0)
- cloudscale_ch.cloud (still version 2.1.0)
- community.aws (still version 1.4.0)
- community.azure (still version 1.0.0)
- community.digitalocean (still version 1.0.0)
- community.docker (still version 1.4.0)
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
- community.postgresql (still version 1.1.1)
- community.proxysql (still version 1.0.0)
- community.rabbitmq (still version 1.0.3)
- community.routeros (still version 1.1.0)
- community.skydive (still version 1.0.0)
- community.vmware (still version 1.8.0)
- community.windows (still version 1.3.0)
- community.zabbix (still version 1.2.0)
- containers.podman (still version 1.4.4)
- cyberark.conjur (still version 1.1.0)
- dellemc.openmanage (still version 3.1.0)
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
- junipernetworks.junos (still version 2.0.0)
- kubernetes.core (still version 1.2.0)
- mellanox.onyx (still version 1.0.0)
- netapp.aws (still version 21.2.0)
- netapp.elementsw (still version 21.3.0)
- netapp.ontap (still version 21.3.1)
- netapp_eseries.santricity (still version 1.1.0)
- netbox.netbox (still version 3.0.0)
- ngine_io.cloudstack (still version 2.0.0)
- ngine_io.exoscale (still version 1.0.0)
- ngine_io.vultr (still version 1.1.0)
- openstack.cloud (still version 1.3.0)
- openvswitch.openvswitch (still version 2.0.0)
- purestorage.flasharray (still version 1.6.2)
- purestorage.flashblade (still version 1.4.0)
- sensu.sensu_go (still version 1.9.1)
- servicenow.servicenow (still version 1.0.4)
- splunk.es (still version 1.0.2)
- t_systems_mms.icinga_director (still version 1.16.0)
- theforeman.foreman (still version 2.0.1)
- vyos.vyos (still version 2.0.0)
- wti.remote (still version 1.0.1)

v4.0.0a1
========

.. contents::
  :local:
  :depth: 2

Release Summary
---------------

Release Date: 2021-03-16

`Porting Guide <https://docs.ansible.com/ansible/devel/porting_guides.html>`_

Ansible-core
------------

Ansible 4.0.0a1 contains Ansible-core version 2.11.0b2.
This is a newer version than version 2.10.5 contained in the previous Ansible release.

The changes are reported in the combined changelog below.

Included Collections
--------------------

If not mentioned explicitly, the changes are reported in the combined changelog below.

+-------------------------------+---------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Collection                    | Ansible 3.0.0 | Ansible 4.0.0a1 | Notes                                                                                                                                                                                                                                      |
+===============================+===============+=================+============================================================================================================================================================================================================================================+
| amazon.aws                    | 1.3.0         | 1.4.1           |                                                                                                                                                                                                                                            |
+-------------------------------+---------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ansible.netcommon             | 1.5.0         | 2.0.0           |                                                                                                                                                                                                                                            |
+-------------------------------+---------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ansible.posix                 | 1.1.1         | 1.2.0           |                                                                                                                                                                                                                                            |
+-------------------------------+---------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ansible.utils                 | 2.0.0         | 2.0.1           |                                                                                                                                                                                                                                            |
+-------------------------------+---------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ansible.windows               | 1.3.0         | 1.4.0           |                                                                                                                                                                                                                                            |
+-------------------------------+---------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| arista.eos                    | 1.3.0         | 2.0.0           |                                                                                                                                                                                                                                            |
+-------------------------------+---------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| awx.awx                       | 17.0.1        | 17.1.0          | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.                                                                                                               |
+-------------------------------+---------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cisco.asa                     | 1.0.4         | 2.0.0           |                                                                                                                                                                                                                                            |
+-------------------------------+---------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cisco.intersight              | 1.0.10        | 1.0.12          | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.                                                                                                               |
+-------------------------------+---------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cisco.ios                     | 1.3.0         | 2.0.0           |                                                                                                                                                                                                                                            |
+-------------------------------+---------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cisco.iosxr                   | 1.2.1         | 2.0.0           |                                                                                                                                                                                                                                            |
+-------------------------------+---------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cisco.meraki                  | 2.2.0         | 2.2.1           |                                                                                                                                                                                                                                            |
+-------------------------------+---------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cisco.nxos                    | 1.4.0         | 2.0.0           |                                                                                                                                                                                                                                            |
+-------------------------------+---------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cloudscale_ch.cloud           | 2.0.0         | 2.1.0           |                                                                                                                                                                                                                                            |
+-------------------------------+---------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.aws                 | 1.3.0         | 1.4.0           |                                                                                                                                                                                                                                            |
+-------------------------------+---------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.crypto              | 1.4.0         | 1.5.0           |                                                                                                                                                                                                                                            |
+-------------------------------+---------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.docker              | 1.2.2         | 1.4.0           |                                                                                                                                                                                                                                            |
+-------------------------------+---------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.general             | 2.0.1         | 2.2.0           |                                                                                                                                                                                                                                            |
+-------------------------------+---------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.grafana             | 1.1.0         | 1.2.0           |                                                                                                                                                                                                                                            |
+-------------------------------+---------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.hashi_vault         | 1.0.0         | 1.1.2           |                                                                                                                                                                                                                                            |
+-------------------------------+---------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.hrobot              | 1.1.0         | 1.1.1           |                                                                                                                                                                                                                                            |
+-------------------------------+---------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.kubernetes          | 1.1.1         | 1.2.0           |                                                                                                                                                                                                                                            |
+-------------------------------+---------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.libvirt             | 1.0.0         | 1.0.1           |                                                                                                                                                                                                                                            |
+-------------------------------+---------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.mongodb             | 1.2.0         | 1.2.1           | The collection did not have a changelog in this version.                                                                                                                                                                                   |
+-------------------------------+---------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.mysql               | 1.2.0         | 1.3.0           |                                                                                                                                                                                                                                            |
+-------------------------------+---------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.okd                 | 1.0.1         | 1.1.0           |                                                                                                                                                                                                                                            |
+-------------------------------+---------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.rabbitmq            | 1.0.1         | 1.0.3           | The collection did not have a changelog in this version.                                                                                                                                                                                   |
+-------------------------------+---------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.sops                | 1.0.4         | 1.0.5           |                                                                                                                                                                                                                                            |
+-------------------------------+---------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.vmware              | 1.7.0         | 1.8.0           |                                                                                                                                                                                                                                            |
+-------------------------------+---------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| community.windows             | 1.2.0         | 1.3.0           |                                                                                                                                                                                                                                            |
+-------------------------------+---------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| containers.podman             | 1.4.1         | 1.4.4           |                                                                                                                                                                                                                                            |
+-------------------------------+---------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| dellemc.openmanage            | 3.0.0         | 3.1.0           | You can find the collection's changelog at `https://github.com/dell/dellemc-openmanage-ansible-modules/blob/collections/CHANGELOG.rst <https://github.com/dell/dellemc-openmanage-ansible-modules/blob/collections/CHANGELOG.rst>`_.       |
+-------------------------------+---------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| dellemc.os6                   | 1.0.6         | 1.0.7           | There are no changes recorded in the changelog.                                                                                                                                                                                            |
+-------------------------------+---------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| dellemc.os9                   | 1.0.3         | 1.0.4           |                                                                                                                                                                                                                                            |
+-------------------------------+---------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| f5networks.f5_modules         | 1.7.1         | 1.8.1           |                                                                                                                                                                                                                                            |
+-------------------------------+---------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| fortinet.fortios              | 1.1.8         | 1.1.9           | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.                                                                                                               |
+-------------------------------+---------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| hetzner.hcloud                | 1.2.1         | 1.3.0           |                                                                                                                                                                                                                                            |
+-------------------------------+---------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| junipernetworks.junos         | 1.3.0         | 2.0.0           |                                                                                                                                                                                                                                            |
+-------------------------------+---------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| kubernetes.core               | 1.1.1         | 1.2.0           |                                                                                                                                                                                                                                            |
+-------------------------------+---------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| netapp.aws                    | 20.9.0        | 21.2.0          | The collection did not have a changelog in this version.                                                                                                                                                                                   |
+-------------------------------+---------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| netapp.elementsw              | 20.11.0       | 21.3.0          | The collection did not have a changelog in this version.                                                                                                                                                                                   |
+-------------------------------+---------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| netapp.ontap                  | 21.1.1        | 21.3.1          | The collection did not have a changelog in this version.                                                                                                                                                                                   |
+-------------------------------+---------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| netbox.netbox                 | 2.0.0         | 3.0.0           |                                                                                                                                                                                                                                            |
+-------------------------------+---------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| openstack.cloud               | 1.2.1         | 1.3.0           | The collection did not have a changelog in this version.                                                                                                                                                                                   |
+-------------------------------+---------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| openvswitch.openvswitch       | 1.1.0         | 2.0.0           |                                                                                                                                                                                                                                            |
+-------------------------------+---------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ovirt.ovirt                   | 1.3.0         | 1.4.0           |                                                                                                                                                                                                                                            |
+-------------------------------+---------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| purestorage.flasharray        | 1.5.1         | 1.6.2           |                                                                                                                                                                                                                                            |
+-------------------------------+---------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| sensu.sensu_go                | 1.8.0         | 1.9.1           |                                                                                                                                                                                                                                            |
+-------------------------------+---------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| t_systems_mms.icinga_director | 1.13.0        | 1.16.0          | You can find the collection's changelog at `https://github.com/T-Systems-MMS/ansible-collection-icinga-director/blob/master/CHANGELOG.md <https://github.com/T-Systems-MMS/ansible-collection-icinga-director/blob/master/CHANGELOG.md>`_. |
+-------------------------------+---------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| theforeman.foreman            | 1.5.1         | 2.0.1           |                                                                                                                                                                                                                                            |
+-------------------------------+---------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| vyos.vyos                     | 1.1.1         | 2.0.0           |                                                                                                                                                                                                                                            |
+-------------------------------+---------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Major Changes
-------------

Ansible-core
~~~~~~~~~~~~

- A collection can be reinstalled with new version requirements without using the ``--force`` flag. The collection's dependencies will also be updated if necessary with the new requirements. Use ``--upgrade`` to force transitive dependency updates.
- Declared ``resolvelib >= 0.5.3, < 0.6.0`` a direct dependency of
  ansible-core. Refs:
  - https://github.com/sarugaku/resolvelib
  - https://pypi.org/p/resolvelib
  - https://pradyunsg.me/blog/2020/03/27/pip-resolver-testing
- It became possible to install Ansible Collections from local folders and namespaces folder similar to SCM structure with multiple collections.
- It became possible to upgrade Ansible collections from Galaxy servers using the ``--upgrade`` option with ``ansible-galaxy collection install``.
- Support for role argument specification validation at role execution time. When a role contains an argument spec, an implicit validation task is inserted at the start of role execution.
- add ``ArgumentSpecValidator`` class for validating parameters against an argument spec outside of ``AnsibleModule`` (https://github.com/ansible/ansible/pull/73335)

ansible.netcommon
~~~~~~~~~~~~~~~~~

- Remove deprecated connection arguments from netconf_config

arista.eos
~~~~~~~~~~

- Requires ansible.netcommon v2.0.0+ to support `ansible_network_single_user_mode` and `ansible_network_import_modules` - Please refer to ansible.netcommon `changelog <https://github.com/ansible-collections/ansible.netcommon/blob/main/changelogs/CHANGELOG.rst#ansible-netcommon-collection-release-notes>`_ for more details.

cisco.asa
~~~~~~~~~

- Please refer to ansible.netcommon `changelog <https://github.com/ansible-collections/ansible.netcommon/blob/main/changelogs/CHANGELOG.rst#ansible-netcommon-collection-release-notes>` for more details.
- Requires ansible.netcommon v2.0.0+ to support `ansible_network_single_user_mode` and `ansible_network_import_modules`.

cisco.ios
~~~~~~~~~

- Please refer to ansible.netcommon `changelog <https://github.com/ansible-collections/ansible.netcommon/blob/main/changelogs/CHANGELOG.rst#ansible-netcommon-collection-release-notes>`_ for more details.
- Requires ansible.netcommon v2.0.0+ to support `ansible_network_single_user_mode` and `ansible_network_import_modules`.

cisco.iosxr
~~~~~~~~~~~

- Please refer to ansible.netcommon `changelog <https://github.com/ansible-collections/ansible.netcommon/blob/main/changelogs/CHANGELOG.rst#ansible-netcommon-collection-release-notes>`_ for more details.
- Requires ansible.netcommon v2.0.0+ to support `ansible_network_single_user_mode` and `ansible_network_import_modules`.
- ipaddress is no longer in ansible.netcommon. For Python versions without ipaddress (< 3.0), the ipaddress package is now required.

cisco.nxos
~~~~~~~~~~

- Please refer to ansible.netcommon `changelog <https://github.com/ansible-collections/ansible.netcommon/blob/main/changelogs/CHANGELOG.rst#ansible-netcommon-collection-release-notes>`_ for more details.
- Requires ansible.netcommon v2.0.0+ to support `ansible_network_single_user_mode` and `ansible_network_import_modules`.

community.grafana
~~~~~~~~~~~~~~~~~

- introduce "skip_version_check" parameter in grafana_teams and grafana_folder modules (#147)

community.mysql
~~~~~~~~~~~~~~~

- mysql_replication - the mode options values ``getslave``, ``startslave``, ``stopslave``, ``resetslave``, ``resetslaveall` and the master_use_gtid option ``slave_pos`` are deprecated (see the alternative values) and will be removed in ``community.mysql`` 3.0.0 (https://github.com/ansible-collections/community.mysql/pull/97).
- mysql_replication - the word ``SLAVE`` in messages returned by the module will be changed to ``REPLICA`` in ``community.mysql`` 2.0.0 (https://github.com/ansible-collections/community.mysql/issues/98).

junipernetworks.junos
~~~~~~~~~~~~~~~~~~~~~

- Please refer to ansible.netcommon `changelog <https://github.com/ansible-collections/ansible.netcommon/blob/main/changelogs/CHANGELOG.rst#ansible-netcommon-collection-release-notes>`_ for more details.
- Requires ansible.netcommon v2.0.0+ to support `ansible_network_single_user_mode` and `ansible_network_import_modules`.

vyos.vyos
~~~~~~~~~

- Please refer to ansible.netcommon `changelog <https://github.com/ansible-collections/ansible.netcommon/blob/main/changelogs/CHANGELOG.rst#ansible-netcommon-collection-release-notes>`_ for more details.
- Requires ansible.netcommon v2.0.0+ to support `ansible_network_single_user_mode` and `ansible_network_import_modules`
- ipaddress is no longer in ansible.netcommon. For Python versions without ipaddress (< 3.0), the ipaddress package is now required.

Minor Changes
-------------

Ansible-core
~~~~~~~~~~~~

- Add ``--format`` CLI option to ``ansible-galaxy collection list`` which allows for ``human`` (default), ``yaml``, or ``json``. (https://github.com/ansible/ansible/pull/73474)
- Add an example for using var in with_sequence (https://github.com/ansible/ansible/issues/68836).
- Add new rolespec_validate option to the import/include_role modules do allow disabling of the implicit role arg validation task on a per-role basis.
- Add option to pass extra vars to ansible-inventory
- Add path of collection location in Ansible CLI version info.
- Add standard Python 2/3 compatibility boilerplate to setup script, module_utils and docs_fragments which were missing them.
- Add support for `argument_specs` data in role metadata.
- Add support for datetime.date object type in module result (https://github.com/ansible/ansible/issues/70583).
- Add which conditional is being evaluated at each step when debugging.
- Add yum/dnf version comparison documentation for package install
- Added NO_COLOR environment var to ansible color configuration, allowing it to integrate with existing convention.
- Added name of aliases in user error (https://github.com/ansible/ansible/issues/58752).
- Added support for GSSAPI/Kerberos authentication with ``urls.py`` that is used by ``uri`` and ``get_url``.
- Added support for specify custom credentials for GSSAPI authentication.
- Allow an attribute to be passed to the min and max filters with Jinja 2.10+
- Allow for the skipped filter to be used on a registered looped task results. (https://github.com/ansible/ansible/issues/16949)
- Allow inventory plugins access to extra vars by default
- Allow unsafe_writes to be set on target via env var, for those targets that need a blanket setting.
- Also added extra vars cli option to console CLI.
- AnsiballZ - Improve performance of ``ModuleDepFinder`` by using faster lookups and reducing the object types that are walked while looking for ``import`` statements. (https://github.com/ansible/ansible/pull/70475)
- CLI - Specify jinja version in ``--version`` output
- CLI - Specify whether PyYAML includes libyaml support in version output
- CLI version displays clarified as core version
- Collection routing: Cisco NSO content from community.network migrated to cisco.nso (https://github.com/ansible/ansible/pull/73046).
- Collection routing: DellEMC content from community.general migrated to dellemc.openmanage (https://github.com/ansible/ansible/pull/73046).
- Collection routing: FortiOS content from community.network migrated to community.fortios (https://github.com/ansible/ansible/pull/73046).
- Collection routing: Google content from community.general migrated to community.google (https://github.com/ansible/ansible/pull/73046).
- Collection routing: Hashi Vault content from community.general migrated to community.hashi_vault (https://github.com/ansible/ansible/pull/73046).
- Collection routing: Hetzner Robot content from community.general migrated to community.hrobot (https://github.com/ansible/ansible/pull/73046).
- Collection routing: KubeVirt content from community.general migrated to community.kubevirt (https://github.com/ansible/ansible/pull/73046).
- Collection routing: OC content from community.general migrated to community.okd (https://github.com/ansible/ansible/pull/73046).
- Collection routing: PostgreSQL content from community.general migrated to community.postgresql (https://github.com/ansible/ansible/pull/73046).
- Collection routing: RouterOS content from community.network migrated to community.routeros (https://github.com/ansible/ansible/pull/73046).
- Collection routing: docker content from community.general migrated to community.docker (https://github.com/ansible/ansible/pull/73046).
- Controller - Add warning for Ansible 2.11 when running a Python version older than Python 3.8 to inform users that 2.12 will only support Python 3.8 and newer on the controller. Starting with Ansible 2.11, the project will only be packaged for Python 3.8 and newer.
- Discourage the use of 'hexdigits' in password lookup, as it distorts expected entropy.
- Enable extra vars for inventory plugin options
- Errors - Ensure that errors passed with ``orig_exc`` include the context of that exception (https://github.com/ansible/ansible/issues/68605)
- Filters - Add new ``split`` filter for splitting strings
- Fixed ansible-doc to not substitute for words followed by parenthesis.  For instance, ``IBM(International Business Machines)`` will no longer be substituted with a link to a non-existent module. https://github.com/ansible/ansible/pull/71070
- Force the template module to use non-native Jinja2 (https://github.com/ansible/ansible/issues/46169)
- Internal config entries will not be documented, to mark an entry as internal it must start with `_`.
- Interpreter Discovery - Add Python 3.8 and Python 3.9 to the fallback list
- Minor code cleanup in plugin loader.
- Module API - libselinux-python is no longer required for basic module API selinux operations (affects core modules assemble, blockinfile, copy, cron, file, get_url, lineinfile, setup, replace, unarchive, uri, user, yum_repository)
- Module API - new module_respawn API allows modules that need to run under a specific Python interpreter to respawn in place under that interpreter
- Module iptables multiport destination support added (https://github.com/ansible/ansible/pull/72928)
- Module iptables set/ipset support added (https://github.com/ansible/ansible/pull/72984)
- New 'timeout' feature added to adhoc and console CLIs, corresponding to the recent 'timeout' task keyword.
- New virtualization facts, ``virtualization_tech_guest`` and ``virtualization_tech_host`` now allow for conveying when a system is a host or guest of multiple virtualization technologies.
- Now 'choices' keyword in config definitions also restricts valid values for the entry.
- Refactored ``ansible-galaxy collection [download|install|list|verify]`` CLI subcommands with the public interface kept intact.
- Restructured _fixup_perms2() in ansible.plugins.action to make it more linear
- Shadow prompt input to ansible-vault encrypt-string unless the ``--show-input`` flag is set
- Switch to hashlib.sha256() for ansible-test to allow for FIPs mode.
- TOML inventory plugin is no longer in preview status
- Templar - reduce the complexity of ``Templar._lookup`` (https://github.com/ansible/ansible/pull/73277)
- The ``csvfile`` lookup plugin now uses ``parse_kv()`` internally. As a result, multi-word search keys can now be passed.
- The ``csvfile`` lookup plugin's documentation has been fixed; it erroneously said that the delimiter could be ``t`` which was never true. We now accept ``\t``, however, and the error in the documentation has been fixed to note that.
- The constructed inventory plugin has new option to force using vars plugins on previouslly processed inventory sources.
- The find module is now more specific about the reasons it skips candidate files.
- The logging functionality in module_utils.basic now returns a nicer error when it falls back to syslog but ends up getting a TypeError thrown back.
- The new dependency resolver prefers ``MANIFEST.json`` over ``galaxy.yml`` if it exists in the target directory.
- The plugin loader now keeps track of the collection where a plugin was resolved to, in particular whether the plugin was loaded from ansible-core's internal paths (``ansible.builtin``) or from user-supplied paths (no collection name).
- Toggle allowing usage of extra_vars in compose
- When connecting as an unprivileged user, and becoming an unprivileged user, we now fall back to also trying ``chmod +a`` which works on macOS and makes use of ACLs.
- allow tree callback plugin to be configurable, for use with playbooks.
- ansible-doc - In Windows setup steps, ``ExecutionPolicy`` should be restored to default value ``RemoteSigned`` (https://github.com/ansible/ansible/pull/72993).
- ansible-doc - provide ``has_action`` field in JSON output for modules. That information is currently only available in the text view (https://github.com/ansible/ansible/pull/72359).
- ansible-doc has new option to show keyword documentation.
- ansible-doc will now format, ``L()``, ``R()``, and ``HORIZONTALLINE`` in plugin docs just as the website docs do.  https://github.com/ansible/ansible/pull/71070
- ansible-galaxy - Add installation successful message
- ansible-galaxy - Added caching mechanisms when retrieving collection info to speed up installs and downloads
- ansible-galaxy - Change the output verbosity level of the download message from 3 to 0 (https://github.com/ansible/ansible/issues/70010)
- ansible-galaxy - Ensure ``get_collection_versions`` returns an empty list when a collection does not exist for consistency across API versions.
- ansible-galaxy - find any collection dependencies in the globally configured Galaxy servers and not just the server the parent collection is from.
- ansible-test - A warning is no longer emitted when a ``pip*`` or ``python*`` binary is found without a matching couterpart.
- ansible-test - Add ``macos/10.15`` as a supported value for the ``--remote`` option.
- ansible-test - Add a ``--docker-network`` option to choose the network for running containers when using the ``--docker`` option.
- ansible-test - Add support for running tests on Fedora 33 (https://github.com/ansible/ansible/pull/72861).
- ansible-test - Added Ubuntu 20.04 LTS image to the default completion list
- ansible-test - Added a ``--export`` option to the ``ansible-test coverage combine`` command to facilitate multi-stage aggregation of coverage in CI pipelines.
- ansible-test - Added the ``-remote rhel/7.9`` option to run tests on RHEL 7.9
- ansible-test - Allow custom ``--remote-stage`` options for development and testing.
- ansible-test - CentOS 8 container is now 8.2.2004 (https://github.com/ansible/distro-test-containers/pull/45).
- ansible-test - Changed the internal name of the custom plugin used to identify use of unwanted imports and functions.
- ansible-test - Cleaned up code to resolve warnings and errors reported by PyCharm.
- ansible-test - Code cleanup in the ``import`` sanity test.
- ansible-test - Code cleanup in the internal logic for code coverage collection of PowerShell modules.
- ansible-test - Collections can now specify pip constraints for unit and integration test requirements using ``tests/unit/constraints.txt`` and ``tests/integration/constraints.txt`` respectively.
- ansible-test - Containers used with the ``--remote`` option have been updated to version 1.29.0 to include the latest Ansible requirements.
- ansible-test - Files used to track remote instances no longer have a region suffix.
- ansible-test - Fix ``ansible-test coverage`` reporting sub-commands (``report``, ``html``, ``xml``) on Python 2.6.
- ansible-test - Fix container hostname/IP discovery for the ``acme`` test plugin.
- ansible-test - FreeBSD 11.4 and 12.2 provisioning can now be used with the ``--python 3.8`` option.
- ansible-test - FreeBSD instances provisioned with ``--remote`` now make ``libyaml`` available for use with PyYAML installation.
- ansible-test - Generation of an ``egg-info`` directory, if needed, is now done after installing test dependencies and before running tests. When running from an installed version of ``ansible-test`` a temporary directory is used to avoid permissions issues. Previously it was done before installing test dependencies and adjacent to the installed directory.
- ansible-test - Implemented CloudStack test container selection by ENV variable `ANSIBLE_CLOUDSTACK_CONTAINER` with a default to `quay.io/ansible/cloudstack-test-container:1.4.0`.
- ansible-test - Improved handling of minimum Python version requirements for sanity tests. Supported versions are now included in warning messages displayed when tests are skipped.
- ansible-test - More sanity test requirements have been pinned to specific versions to provide consistent test results.
- ansible-test - Most sanity test specific ``pip`` constraints are now used only when running sanity tests. This should reduce conflicts with ``pip`` requirements and constraints when testing collections.
- ansible-test - Most sanity tests are now skipped on Python 3.5 and earlier with a warning. Previously this was done for Python 2.7 and earlier.
- ansible-test - Now supports freebsd/11.4 remote (https://github.com/ansible/ansible/issues/48782).
- ansible-test - Now supports freebsd/12.2 remote (https://github.com/ansible/ansible/issues/72366).
- ansible-test - OpenSuse container now uses Leap 15.2 (https://github.com/ansible/distro-test-containers/pull/48).
- ansible-test - Pin the ``virtualenv`` version used for ``--remote`` pip installs to the latest version supported by Python 2.x, which is version 16.7.10.
- ansible-test - Provisioning of RHEL instances now includes installation of pinned versions of ``packaging`` and ``pyparsing`` to match the downstream vendored versions.
- ansible-test - RHEL 8.2+ provisioning can now be used with the ``--python 3.8`` option, taking advantage of the Python 3.8 AppStream.
- ansible-test - Raise the number of bytes scanned by ansible-test to determine if a file is binary to 4096.
- ansible-test - Refactor code for installing ``cryptography`` to allow re-use in the future.
- ansible-test - Refactor code to remove unused logic for obsolete support of multiple provisioning endpoints.
- ansible-test - Remove ``pytest < 6.0.0`` constraint for managed installations on Python 3.x now that pytest 6 is supported.
- ansible-test - Remove em dash from the Pytest configuration file in order to be readable on systems where preferred encoding is ASCII. (https://github.com/ansible/ansible/issues/71739)
- ansible-test - Remove outdated ``--docker`` completion entries: fedora30, fedora31, ubuntu1604
- ansible-test - Remove outdated ``--remote`` completion entries: freebsd/11.1, freebsd/12.1, osx/10.11, macos/10.15, rhel/7.6, rhel/7.8, rhel/8.1, rhel/8.2
- ansible-test - Remove outdated ``--windows`` completion entries: 2008, 2008-R2
- ansible-test - Remove the discontinued ``us-east-2`` choice from the ``--remote-aws-region`` option.
- ansible-test - Remove unused ``--remote`` completion entry: power/centos/7
- ansible-test - Removed ``pip`` constraints related to integration tests that have been moved to collections. This should reduce conflicts with ``pip`` requirements and constraints when testing collections.
- ansible-test - Removed the obsolete ``--remote-aws-region`` provisioning option.
- ansible-test - Removed the obsolete ``tower`` test plugin for testing Tower modules.
- ansible-test - Removed unused provisioning code and cleaned up remote provider management logic.
- ansible-test - Rename internal functions to match associated constant names that were previously updated.
- ansible-test - Reorganize internal ``pylint`` configuration files for easier comparison and maintenance.
- ansible-test - Report the correct line number in the ``yamllint`` sanity test when reporting ``libyaml`` parse errors in module documentation.
- ansible-test - Request remote resources by provider name for all provider types.
- ansible-test - Show a warning when the obsolete ``--remote-aws-region`` option is used.
- ansible-test - Silence ``pip`` warnings about Python 3.5 being EOL when installing requirements.
- ansible-test - Support custom remote endpoints with the ``--remote-endpoint`` option.
- ansible-test - The ``--remote`` option no longer pre-installs the ``virtualenv`` module on Python 3.x instances. The Python built-in ``venv`` module should be used instead.
- ansible-test - The ``default`` container for both collections and core have been updated to versions 2.11.0 and 1.9.0 respectively.
- ansible-test - The ``pylint`` sanity test is now skipped with a warning on Python 3.9 due to unresolved upstream regressions.
- ansible-test - The ``pylint`` sanity test is now supported on Python 3.8.
- ansible-test - The ``rstcheck`` sanity test is no longer used for collections, but continues to be used for ansible-core.
- ansible-test - The generated ``resource_prefix`` variable now meets the host name syntax requirements specified in RFC 1123 and RFC 952. The value used for local tests now places the random number before the hostname component, rather than after. If the resulting value is too long, it will be truncated.
- ansible-test - Ubuntu containers as well as ``default-test-container`` and ``ansible-base-test-container`` are now slightly smaller due to apt cleanup (https://github.com/ansible/distro-test-containers/pull/46).
- ansible-test - Update ``pylint`` and its dependencies to the latest available versions to support Python 3.9.
- ansible-test - Update built-in service endpoints for the ``--remote`` option.
- ansible-test - Updated the default test containers to version 3.1.0.
- ansible-test - Upgrade ansible-runner version used in compatibility tests, remove some tasks that were only needed with older versions, and skip in python2 because ansible-runner is soon dropping it.
- ansible-test - Use new endpoint for Parallels based instances with the ``--remote`` option.
- ansible-test - ``default-test-container`` and ``ansible-base-test-container`` now use Python 3.9.0 instead of 3.9.0rc1.
- ansible-test - add https endpoint for ansible-test
- ansible-test - add macOS 11.1 as a remote target (https://github.com/ansible/ansible/pull/72622)
- ansible-test - add the collection plugin directories ``plugin_utils`` and ``sub_plugins`` to list of plugin types. This ensures such plugins are tested for the ``import`` sanity test (https://github.com/ansible/ansible/pull/73599).
- ansible-test - centos6 end of life - container image updated to point to vault base repository (https://github.com/ansible/distro-test-containers/pull/54)
- ansible-test - centos6 image now has multiple fallback yum repositories for CentOS Vault.
- ansible-test - default container now uses default-test-container 2.7.0 and ansible-base-test-container 1.6.0. This brings in Python 3.9.0rc1 for testing.
- ansible-test - now makes a better attempt to support podman when calling ``docker images`` and asking for JSON format.
- ansible-test - python-cryptography is now bounded at <3.2, as 3.2 drops support for OpenSSL 1.0.2 upon which some of our CI infrastructure still depends.
- ansible-test - remote macOS instances no longer install ``virtualenv`` during provisioning
- ansible-test - the ACME test container was updated, it now supports external account creation and has a basic OCSP responder (https://github.com/ansible/ansible/pull/71097, https://github.com/ansible/acme-test-container/releases/tag/2.0.0).
- ansible-test - the ``import`` sanity test now also tries to import all non-module and non-module_utils Python files in ``lib/ansible/`` resp. ``plugins/`` (https://github.com/ansible/ansible/pull/72497).
- ansible-test - virtualenv helper scripts now prefer ``venv`` on Python 3 over ``virtualenv``
- ansible-test Now supports RHEL 8.3
- ansible-test pylint - ensure that removal collection version numbers conform to the semantic versioning specification at https://semver.org/ (https://github.com/ansible/ansible/pull/71679).
- ansible-test pylint sanity test - stop ignoring ``used-before-assignment`` errors (https://github.com/ansible/ansible/pull/73639).
- ansible-test runtime-metadata - compare deprecation and tombstone versions to the current version to ensure that they are correct (https://github.com/ansible/ansible/pull/72625).
- ansible-test runtime-metadata - ensure that removal collection version numbers conform to the semantic versioning specification at https://semver.org/ (https://github.com/ansible/ansible/pull/71679).
- ansible-test runtime-metadata - ensure that the tombstone removal date is not in the future (https://github.com/ansible/ansible/pull/72625).
- ansible-test runtime-metadata - validate removal version numbers, and check removal dates more strictly (https://github.com/ansible/ansible/pull/71679).
- ansible-test validate-modules - ensure that removal collection version numbers and version_added collection version numbers conform to the semantic versioning specification at https://semver.org/ (https://github.com/ansible/ansible/pull/71679).
- ansible-test validate-modules - no longer assume that ``default`` for ``type=bool`` options is ``false``, as the default is ``none`` and for some modules, ``none`` and ``false`` mean different things (https://github.com/ansible/ansible/issues/69561).
- ansible-test validate-modules - option names that seem to indicate they contain secret information that should be marked ``no_log=True`` are now flagged in the validate-modules sanity test. False positives can be marked by explicitly setting ``no_log=False`` for these options in the argument spec. Please note that many false positives are expected; the assumption is that it is by far better to have false positives than false negatives (https://github.com/ansible/ansible/pull/73508).
- ansible-test validate-modules - validate removal version numbers (https://github.com/ansible/ansible/pull/71679).
- ansible.utils.encrypt now returns `AnsibleError` instead of crypt.crypt's `OSError` on Python 3.9
- apt - module now works under any supported Python interpreter
- apt_repository - module now works under any supported Python interpreter
- callback plugins - ``meta`` tasks now get sent to ``v2_playbook_on_task_start``. Explicit tasks are always sent. Plugins can opt in to receiving implicit ones.
- callbacks - Add feature allowing forks to send callback events (https://github.com/ansible/ansible/issues/14681)
- conditionals - change the default of CONDITIONAL_BARE_VARS to False (https://github.com/ansible/ansible/issues/70682).
- config - more types are now automatically coerced to string when ``type: str`` is used and the value is parsed as a different type
- constructed - Add a toggle to allow the separator to be omitted if no prefix has been provided.
- constructed inventory plugin - Sanitize group names created from the ``groups`` option silently.
- create ``get_type_validator`` standalone function and move that functionality out of ``AnsibleModule`` (https://github.com/ansible/ansible/pull/72667)
- create ``get_unsupported_parameters`` validation function (https://github.com/ansible/ansible/pull/72447/files)
- debconf - add a note about no_log=True since module might expose sensitive information to logs (https://github.com/ansible/ansible/issues/32386).
- default callback - add ``show_task_path_on_failure`` option to display file and line number of tasks only on failed tasks when running at normal verbosity level (https://github.com/ansible/ansible/issues/64625)
- default callback - task name is now shown for ``include_tasks`` when using the ``free`` strategy (https://github.com/ansible/ansible/issues/71277).
- default callback - task name is now shown for ``include_tasks`` when using the ``linear`` strategy with ``ANSIBLE_DISPLAY_SKIPPED_HOSTS=0``.
- default_callback - moving 'check_mode_markers' documentation in default_callback doc_fragment (https://github.com/ansible-collections/community.general/issues/565).
- distribution - add facts about Amazon Linux Distribution facts (https://github.com/ansible/ansible/issues/73742).
- distribution - add support for DragonFly distribution (https://github.com/ansible/ansible/issues/43739).
- distribution - added distribution fact and hostname support for Parrot OS (https://github.com/ansible/ansible/pull/69158).
- distribution - handle NetBSD OS Family (https://github.com/ansible/ansible/issues/43739).
- distribution facts - ``distribution_release`` is now ``"Stream"`` on CentOS Stream (https://github.com/ansible/ansible/issues/73027).
- dnf - Add nobest option (https://github.com/ansible/ansible/issues/69983)
- dnf - When ``state: absent``, package names are now matched similarly to how the ``dnf`` CLI matches them (https://github.com/ansible/ansible/issues/72809).
- dnf - module now works under any supported Python interpreter
- dnf - now shows specific package changes (installations/removals) under ``results`` in check_mode. (https://github.com/ansible/ansible/issues/66132)
- facts - ``/dev/kvm`` is now consulted in Linux virtualization facts, and the host is considered a KVM host if this file exists and none of the pre-existing checks matched.
- facts - add new fact ``date_time['tz_dst']``, which returns the daylight saving timezone (https://github.com/ansible/ansible/issues/69004).
- facts - add uptime to openbsd
- find module - Now has a ``read_whole_file`` boolean parameter which allows for reading the whole file and doing an ``re.search()`` regex evaluation on it when searching using the ``contains`` option. This allows (for example) for ensuring the very end of the file matches a pattern.
- galaxy - add documentation about galaxy parameters in examples/ansible.cfg (https://github.com/ansible/ansible/issues/68402).
- galaxy - handle token as dict while loading from yaml file (https://github.com/ansible/ansible/issues/70887).
- get_url - allow checksum urls to point to file:// resources, moving scheme test to function
- get_url - handle same SHA sum for checksum file (https://github.com/ansible/ansible/issues/71420).
- git - add ``single_branch`` parameter (https://github.com/ansible/ansible/pull/28465)
- hash filter - fail when unsupported hash type is passed as an argument (https://github.com/ansible/ansible/issues/70258)
- inventory cache - do not show a warning when the cache file does not (yet) exist.
- iptables - add a note about ipv6-icmp in protocol parameter (https://github.com/ansible/ansible/issues/70905).
- iptables - fixed get_chain_policy API (https://github.com/ansible/ansible/issues/68612).
- iptables - reorder comment postition to be at the end (https://github.com/ansible/ansible/issues/71444).
- lineinfile - add search_string parameter for non-regexp searching (https://github.com/ansible/ansible/issues/70470)
- linux facts - Add additional check to ensure 'container' virtual fact gets added to guest_tech when appropriate (https://github.com/ansible/ansible/pull/71385)
- meta - now include a ``skip_reason`` when skipped (https://github.com/ansible/ansible/pull/71355).
- module payload builder - module_utils imports in any nested block (eg, ``try``, ``if``) are treated as optional during module payload builds; this allows modules to implement runtime fallback behavior for module_utils that do not exist in older versions of Ansible.
- module_utils - ``get_file_attributes()`` now takes an optional ``include_version`` boolean parameter. When ``True`` (default), the file's version/generation number is included in the result (but requires ``lsattr -v`` to work on the target platform).
- now !unsafe works on all types of data, not just strings, even recursively for mappings and sequences.
- package_facts - module support for apt and rpm now works under any supported Python interpreter
- pipe lookup - update docs for Popen with shell=True usages (https://github.com/ansible/ansible/issues/70159).
- plugin examples - Allow non-YAML examples, so that examples for plugins like the INI and TOML inventory plugins can be directly represented (https://github.com/ansible/ansible/pull/71184)
- plugin option validation - now the option type ``dict``/``dictionary`` is also validated by the config manager (https://github.com/ansible/ansible/pull/71928).
- reboot - add ``reboot_command`` parameter to allow specifying the command used to reboot the system (https://github.com/ansible/ansible/issues/51359)
- remove ``excommunicate`` debug command from AnsiballZ
- selinux - return selinux_getpolicytype facts correctly.
- service_facts - return service state information on AIX.
- setup - allow list of filters (https://github.com/ansible/ansible/pull/68551).
- setup.py - Declare that Python 3.9 is now supported (https://github.com/ansible/ansible/pull/72861).
- setup.py - Skip doing conflict checks for ``sdist`` and ``egg_info`` commands (https://github.com/ansible/ansible/pull/71310)
- subelements - clarify the lookup plugin documentation for parameter handling (https://github.com/ansible/ansible/issues/38182).
- subversion - ``validate_certs`` option, which, when true, will avoid passing ``--trust-server-cert`` to ``svn`` commands (https://github.com/ansible/ansible/issues/22599).
- unarchive - Add support for .tar.zst (zstd compression) (https://github.com/ansible/ansible/pull/73265).
- unarchive - add ``RETURN`` documentation (https://github.com/ansible/ansible/issues/67445).
- unarchive - add ``include`` parameter to allow extracting specific files from an archive (https://github.com/ansible/ansible/pull/40522)
- update sphinx to 2.1.2 and rstcheck to 3.3.1 for building documentation.
- uri - add ``ca_path`` argument to allow specification of a CA certificate (https://github.com/ansible/ansible/pull/71979).
- user - add new parameters ``password_expire_max`` and ``password_expire_min`` for controlling password expiration (https://github.com/ansible/ansible/issues/68775)
- varnames lookup plugin - Fixed grammar error in exception message when the plugin is given a non-string term.
- vault - Provide better error for single value encrypted values to indicate the file, line, and column of the errant vault (https://github.com/ansible/ansible/issues/72276)
- version test - Add semantic version functionality
- virtual facts - containerd cgroup is now recognized as container tech (https://github.com/ansible/ansible/issues/66304).
- virtualization facts - Detect ``vdsmd`` in addition to ``vdsm`` when trying to detect RHEV hosts. (https://github.com/ansible/ansible/issues/66147)
- winrm - Added ``ansible_winrm_kinit_args`` that can be used to control the args that are sent to the ``kinit`` call for Kerberos authentication.
- yum - module now works under any supported Python interpreter
- yum_repository - added boolean option module_hotfixes which allows to enable functionality for dnf.

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

ansible.netcommon
~~~~~~~~~~~~~~~~~

- Add SCP support when using ssh_type libssh
- Add `single_user_mode` option for command output caching.
- Move cli_config idempotent warning message with the task response under `warnings` key if `changed` is `True`
- Reduce CPU usage and network module run time when using `ansible_network_import_modules`
- Support any() and all() filters in Jinja2.

ansible.posix
~~~~~~~~~~~~~

- firewalld - bring the ``target`` feature back (https://github.com/ansible-collections/ansible.posix/issues/112).
- fix sanity test for various modules.
- synchronize - add the ``ssh_connection_multiplexing`` option to allow SSH connection multiplexing (https://github.com/ansible/ansible/issues/24365).

ansible.windows
~~~~~~~~~~~~~~~

- setup - Added more virtualization types to the virtual facts based on the Linux setup module

arista.eos
~~~~~~~~~~

- Add support for configuration caching (single_user_mode).
- Add support for syntax changes in ospf bfd command in 4.23 (https://github.com/ansible-collections/arista.eos/pull/134/)
- Move eos_config idempotent warning message with the task response under `warnings` key if `changed` is `True`
- Re-use device_info dictionary in cliconf

cisco.asa
~~~~~~~~~

- Adds support for single_user_mode command output caching. (https://github.com/ansible-collections/cisco.ios/pull/204).

cisco.ios
~~~~~~~~~

- Add ios_bgp_address_family Resource Module. (https://github.com/ansible-collections/cisco.ios/pull/219).
- Adds support for `single_user_mode` command output caching. (https://github.com/ansible-collections/cisco.ios/pull/204).

cisco.iosxr
~~~~~~~~~~~

- Add iosxr_bgp_address_family resource module (https://github.com/ansible-collections/cisco.iosxr/pull/105.).
- Add iosxr_bgp_global resource module (https://github.com/ansible-collections/cisco.iosxr/pull/101.).
- Add iosxr_bgp_neighbor_address_family resource module (https://github.com/ansible-collections/cisco.iosxr/pull/107.).
- Add missing examples for bgp_address_family module.
- Add support for single_user_mode.
- Fix integration testcases for bgp_address_family and bgp_neighbor_address_family.
- Fix issue in delete state in bgp_address_family (https://github.com/ansible-collections/cisco.iosxr/pull/109).
- Move iosxr_config idempotent warning message with the task response under `warnings` key if `changed` is `True`
- Re-use device_info dict instead of building it every time.

cisco.nxos
~~~~~~~~~~

- Add bfd option for neighbors (https://github.com/ansible-collections/cisco.nxos/issues/241).
- Add hello_interval_ms option in nxos_pim_interface module to support sub-second intervals (https://github.com/ansible-collections/cisco.nxos/issues/226).
- Add nxos_bgp_address_family Resource Module.
- Add nxos_bgp_neighbor_address_family Resource Module.
- Add support df_bit and size option for nxos_ping (https://github.com/ansible-collections/cisco.nxos/pull/237).
- Adds support for `single_user_mode` command output caching.
- Move nxos_config idempotent warning message with the task response under `warnings` key if `changed` is `True`

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
- docker_swarm_service - change ``publish.published_port`` option from mandatory to optional. Docker will assign random high port if not specified (https://github.com/ansible-collections/community.docker/issues/99).

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

hetzner.hcloud
~~~~~~~~~~~~~~

- Add firewalls to hcloud_server module

junipernetworks.junos
~~~~~~~~~~~~~~~~~~~~~

- Add junos_bgp_address_family resource module.
- Add support for autonomous-system routing-options for bgp global and updating tests and documentation.
- Add support for bgp group and neighbors in bgp_global resource module.
- Add support for configuration caching (single_user_mode).
- Re-use device_info dictionary in cliconf.

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

netbox.netbox
~~~~~~~~~~~~~

- Allow rack to be in query_param_ids [#443](https://github.com/netbox-community/ansible_modules/pull/443)
- Inventory - Added ansible_host_dns_name to set ansible_host to dns_name
- netbox_cable -  Add tags option [#455](https://github.com/netbox-community/ansible_modules/pull/455)
- netbox_cluster_type - Add description option [#451](https://github.com/netbox-community/ansible_modules/pull/451)
- netbox_device_role - Added description option
- netbox_ipam_role - Add description option [#451](https://github.com/netbox-community/ansible_modules/pull/451)
- netbox_manufacturer - Add description option [#451](https://github.com/netbox-community/ansible_modules/pull/451)
- netbox_platform -  Added description option
- netbox_rir - Add description option [#451](https://github.com/netbox-community/ansible_modules/pull/451)
- netbox_tenant_group - Add parent_tenant_group option [#460](https://github.com/netbox-community/ansible_modules/pull/460)

openvswitch.openvswitch
~~~~~~~~~~~~~~~~~~~~~~~

- Allow setting multiple properties on a port (https://github.com/ansible-collections/openvswitch.openvswitch/issues/63).

ovirt.ovirt
~~~~~~~~~~~

- cluster_upgrade - Add correlation-id header (https://github.com/oVirt/ovirt-ansible-collection/pull/222).
- engine_setup - Add skip renew pki confirm (https://github.com/oVirt/ovirt-ansible-collection/pull/228).
- examples - Add recipe for removing DM device (https://github.com/oVirt/ovirt-ansible-collection/pull/233).
- hosted_engine_setup - Disable reboot_after_installation (https://github.com/oVirt/ovirt-ansible-collection/pull/218).
- hosted_engine_setup - Filter devices with unsupported bond mode (https://github.com/oVirt/ovirt-ansible-collection/pull/226).
- infra - Add reboot host parameters (https://github.com/oVirt/ovirt-ansible-collection/pull/231).
- ovirt_disk - Add SATA support (https://github.com/oVirt/ovirt-ansible-collection/pull/225).
- ovirt_host - Add reboot_after_installation option (https://github.com/oVirt/ovirt-ansible-collection/pull/217).
- ovirt_user - Add ssh_public_key (https://github.com/oVirt/ovirt-ansible-collection/pull/232)

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

theforeman.foreman
~~~~~~~~~~~~~~~~~~

- Add a role `activation_keys` to manage activation keys
- Add a role `lifecycle_environments` to manage lifecycle environments
- Add a role `repositories` to manage products, repositories, and repository_sets
- Add a role `sync_plans` to manage sync plans
- activation_key - add support for selecting subscriptions by ``upstream_pool_id``
- compute_resource - add ``set_console_password``, ``keyboard_layout`` and ``public_key`` parameters (https://github.com/theforeman/foreman-ansible-modules/issues/1052)
- host - clarify that ``owner`` refers to a users login, not their full name (https://github.com/theforeman/foreman-ansible-modules/issues/1045)
- host - look up the correct network id for a network given as part of ``interfaces_attributes`` (https://github.com/theforeman/foreman-ansible-modules/issues/1104)
- host, hostgroup - add ``activation_keys`` parameter to ease configuring activation keys for deploments

vyos.vyos
~~~~~~~~~

- Add support for configuration caching (single_user_mode).
- Add vyos BGP global resource module.(https://github.com/ansible-collections/vyos.vyos/pull/125).
- Re-use device_info dictionary in cliconf.

Breaking Changes / Porting Guide
--------------------------------

Ansible-core
~~~~~~~~~~~~

- Made SCM collections be reinstalled regardless of ``--force`` being present.
- NetBSD virtualization facts (specifically ``ansible_virtualization_type``) now returns a more accurate value by checking the value of the ``machdep.hypervisor`` ``sysctl`` key. This change is breaking because in some cases previously, we would erroneously report ``xen`` even when the target is not running on Xen. This prevents that behavior in most cases. (https://github.com/ansible/ansible/issues/69352)
- Replaced the in-tree dependency resolver with an external implementation that pip >= 20.3 uses now by default — ``resolvelib``. (https://github.com/ansible/ansible/issues/71784)
- The ``meta`` module now supports tags for user-defined tasks. Internal ``meta`` tasks continue to always run. (https://github.com/ansible/ansible/issues/64558)
- ansible-galaxy login command has been removed (see https://github.com/ansible/ansible/issues/71560)

ansible.netcommon
~~~~~~~~~~~~~~~~~

- Removed vendored ipaddress package from collection.

community.docker
~~~~~~~~~~~~~~~~

- docker_swarm - if ``join_token`` is specified, a returned join token with the same value will be replaced by ``VALUE_SPECIFIED_IN_NO_LOG_PARAMETER``. Make sure that you do not blindly use the join tokens from the return value of this module when the module is invoked with ``join_token`` specified! This breaking change appears in a minor release since it is necessary to fix a security issue (https://github.com/ansible-collections/community.docker/pull/103).

theforeman.foreman
~~~~~~~~~~~~~~~~~~

- All role variables are now prefixed with ``foreman_`` to avoid clashes with similarly named variables from roles outside this collection.

Deprecated Features
-------------------

Ansible-core
~~~~~~~~~~~~

- Starting in 2.14, shell and command modules will no longer have the option to warn and suggest modules in lieu of commands. The ``warn`` parameter to these modules is now deprecated and defaults to ``False``. Similarly, the ``COMMAND_WARNINGS`` configuration option is also deprecated and defaults to ``False``. These will be removed and their presence will become an error in 2.14.
- apt_key - the paramater ``key`` does not have any effect, has been deprecated and will be removed in ansible-core version 2.14 (https://github.com/ansible/ansible/pull/70319).
- psrp - Set the minimum version of ``pypsrp`` to ``0.4.0``.

ansible.netcommon
~~~~~~~~~~~~~~~~~

- Deprecate cli_parse module and textfsm, ttp, xml, json parser plugins as they are moved to ansible.utils collection (https://github.com/ansible-collections/ansible.netcommon/pull/182 https://github.com/ansible-collections/ansible.utils/pull/28)

cisco.nxos
~~~~~~~~~~

- Deprecated nxos_bgp_af in favour of nxos_bgp_address_family resource module.
- Deprecated nxos_bgp_neighbor_af in favour of nxos_bgp_neighbor_address_family resource module.

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

Ansible-core
~~~~~~~~~~~~

- Removed `SharedPluginLoaderObj` class from ansible.plugins.strategy. It was deprecated in favor of using the standard plugin loader.
- Removed `_get_item()` alias from callback plugin base class which had been deprecated in favor of `_get_item_label()`.
- The "user" parameter was previously deprecated and is now removed in favor of "scope"
- The deprecated ``ansible.constants.BECOME_METHODS`` has been removed.
- The deprecated ``ansible.constants.get_config()`` has been removed.
- The deprecated ``ansible.constants.mk_boolean()`` has been removed.
- `with_*` loops are no longer optimized for modules whose `name` parameters can take lists (mostly package managers). Use `name` instead of looping over individual names with `with_items` and friends.

f5networks.f5_modules
~~~~~~~~~~~~~~~~~~~~~

- Removed TMOS v11 support for bigip_gtm_pool and bigip_gtm_wide_ip modules
- Removed quorum and monitor_type parameters in bigip_node module. See porting guides section at https://clouddocs.f5.com/products/orchestration/ansible/devel/usage/porting-guides.html
- Removed syslog_settings and pool_settings parameters in bigip_log_destination moduke. See porting guides section at https://clouddocs.f5.com/products/orchestration/ansible/devel/usage/porting-guides.html

Security Fixes
--------------

Ansible-core
~~~~~~~~~~~~

- **security issue** - Mask default and fallback values for ``no_log`` module options (CVE-2021-20228)
- **security issue** - copy - Redact the value of the no_log 'content' parameter in the result's invocation.module_args in check mode. Previously when used with check mode and with '-vvv', the module would not censor the content if a change would be made to the destination path. (CVE-2020-14332)
- Sanitize no_log values from any response keys that might be returned from the uri module (CVE-2020-14330).
- dnf - Previously, regardless of the ``disable_gpg_check`` option, packages were not GPG validated. They are now. (CVE-2020-14365)

community.docker
~~~~~~~~~~~~~~~~

- docker_swarm - the ``join_token`` option is now marked as ``no_log`` so it is no longer written into logs (https://github.com/ansible-collections/community.docker/pull/103).

Bugfixes
--------

Ansible-core
~~~~~~~~~~~~

- A handler defined within a role will now search handlers subdir for included tasks (issue https://github.com/ansible/ansible/issues/71222).
- ALLOW_WORLD_READABLE_TMP, switched to 'moved' message as 'deprecation' is misleading since config settings still work w/o needing change.
- ANSIBLE_COLLECTIONS_PATHS - remove deprecation so that users of Ansible 2.9 and 2.10+ can use the same var when specifying a collection path without a warning.
- Added unsafe_writes test.
- Address compat with rpmfluff-0.6 for integration tests
- Address the deprecation of the use of stdlib distutils in packaging. It's a short-term hotfix for the problem (https://github.com/ansible/ansible/issues/70456, https://github.com/pypa/setuptools/issues/2230, https://github.com/pypa/setuptools/commit/bd110264)
- Adjust various hard-coded action names to also include their ``ansible.builtin.`` and ``ansible.legacy.`` prefixed version (https://github.com/ansible/ansible/issues/71817, https://github.com/ansible/ansible/issues/71818, https://github.com/ansible/ansible/pull/71824).
- Allow TypeErrors on Undefined variables in filters to be handled or deferred when processing for loops.
- Allow `~` to be present in file names in galaxy roles (https://github.com/ansible/ansible/issues/72966)
- Always mention the name of the deprecated or tombstoned plugin in routing deprecation/tombstone messages (https://github.com/ansible/ansible/pull/73059).
- Ansible output now uses stdout to determine column width instead of stdin
- AnsibleModule - added arg ``ignore_invalid_cwd`` to ``AnsibleModule.run_command()``, to control its behaviour when ``cwd`` is invalid. (https://github.com/ansible/ansible/pull/72390)
- Apply ``_wrap_native_text`` only for builtin filters specified in STRING_TYPE_FILTERS.
- Automatically remove async cache files for polled async tasks that have completed (issue https://github.com/ansible/ansible/issues/73206).
- Be smarter about collection paths ending with ansible_collections, emulating a-galaxy behaviour. Issue 72628
- CLI - Restore git information in version output when running from source
- Collection callbacks were ignoring options and rules for stdout and adhoc cases.
- Collections - Ensure ``action_loader.get`` is called with ``collection_list`` to properly find collections when ``collections:`` search is specified (https://github.com/ansible/ansible/issues/72170)
- Command module now returns stdout & stderr if executable is missing or an unknown error occurs
- ConfigManager - Normalize ConfigParser between Python2 and Python3 to for handling comments (https://github.com/ansible/ansible/issues/73709)
- Continue execution when  'flatten' filter when it hits a None/null value as part of the list.
- Correct the inventory source error parse handling, specifically make the config INVENTORY_ANY_UNPARSED_IS_FAILED work as expected.
- Deal with failures when sorting JSON and you have incompatible key types.
- Display - Use wcswidth to calculate printable width of a text string (https://github.com/ansible/ansible/issues/63105)
- Enabled unsafe_writes for get_url which was ignoring the paramter.
- Ensure Ansible's unique filter preserves order (https://github.com/ansible/ansible/issues/63417)
- Ensure if a traceback halts ``strategy.run`` that we still attempt to clean up (https://github.com/ansible/ansible/issues/23958)
- Ensure password passed in by -k is used on delegated hosts that do not have ansible_password set
- Ensure the correct options are used when ssh executables are used that don't match ssh executable names.
- Facts collection - get serial number of NVMe device without sg_inq (https://github.com/ansible/ansible/issues/66663).
- Fix --list-tasks format `role_name : task_name` when task name contains the role name. (https://github.com/ansible/ansible/issues/72505)
- Fix ``RecursionError`` when templating large vars structures (https://github.com/ansible/ansible/issues/71920)
- Fix ``delegate_facts: true`` when ``ansible_python_interpreter`` is not set. (https://github.com/ansible/ansible/issues/70168)
- Fix an exit code for a non-failing playbook (https://github.com/ansible/ansible/issues/71306)
- Fix ansible-galaxy collection list to show collections in site-packages (https://github.com/ansible/ansible/issues/70147)
- Fix bytestring vs string comparison in module_utils.basic.is_special_selinux_path() so that special-cased filesystems which don't support SELinux context attributes still allow files to be manipulated on them. (https://github.com/ansible/ansible/issues/70244)
- Fix execution of the meta tasks 'clear_facts', 'clear_host_errors', 'end_play', 'end_host', and 'reset_connection' when the CLI flag '--flush-cache' is provided.
- Fix fileglob bug where it could return different results for different order of parameters (https://github.com/ansible/ansible/issues/72873).
- Fix incorrect msg in the results dict in loops
- Fix incorrect re-run of roles with tags (https://github.com/ansible/ansible/issues/69848)
- Fix incorrect variable scoping when using ``import with context`` in Jinja2 templates. (https://github.com/ansible/ansible/issues/72615)
- Fix jsonfile cache plugin option '_uri' to be a type path instead of a string. (https://github.com/ansible/ansible/issues/38002)
- Fix notifying handlers via `role_name : handler_name` when handler name contains the role name. (https://github.com/ansible/ansible/issues/70582)
- Fix parsing of values when using empty string as a key (https://github.com/ansible/ansible/issues/57132)
- Fix statistics reporting when rescue block contains another block (issue https://github.com/ansible/ansible/issues/61253).
- Fix to previous deprecation change (#70504) which caused command warning deprecation to show in all cases, even when not specified by the user.
- Fixed TypeError instancemethod expecting at least 2 arguments for apt_repository(issue https://github.com/ansible/ansible/issues/69308, PR https://github.com/ansible/ansible/pull/69463)
- Fixed issue when `netstat` is either missing or doesn't have execution permissions leading to incorrect command being executed.
- Fixes ``ansible-galaxy role info`` to support multiple roles on the command line (https://github.com/ansible/ansible/pull/70148)
- Fixes ansible-test traceback when plugin author is not a string or a list of strings (https://github.com/ansible/ansible/pull/70507)
- Handle more varnames that can create conflicts, expand a function in general, handle jinja2 globals in particular (https://github.com/ansible/ansible/issues/41955).
- INTERPRETER_PYTHON_DISTRO_MAP - prefer ``/usr/libexec/platform-python`` on ``oraclelinux 8`` when other pythons are present.
- Improve Ansible config deprecations to show the source of the deprecation (ansible-core). Also remove space before a comma in config deprecations (https://github.com/ansible/ansible/pull/72697).
- Improved/fixed regular expressions in ``validate-modules/validate_modules/schema.py`` and ``utils/collection_loader/_collection_finder.py`` (https://github.com/ansible/ansible/pull/73577).
- Includes - Explicitly get the include task, and not assume it is the parent (https://github.com/ansible/ansible/issues/65710)
- InventoryManager - Fix unhandled exception when given limit file was actually a directory.
- InventoryManager - Fix unhandled exception when inventory directory was empty or contained empty subdirectories (https://github.com/ansible/ansible/issues/73658).
- JSON Encoder - Ensure we treat single vault encrypted values as strings (https://github.com/ansible/ansible/issues/70784)
- Lookup user by UID in password database if login name is not found (https://github.com/ansible/ansible/issues/17029)
- Pass expression in angle-bracket notation as filename argument to a ``compile()`` built-in function, so that Python debuggers do not try to parse it as filename.
- Pass the connection's timeout to connection plugins instead of the task's timeout.
- Provide more information in AnsibleUndefinedVariable (https://github.com/ansible/ansible/issues/55152)
- Python module_utils finder - refactor logic to eliminate many corner cases, remove recursion, fix base module_utils redirections
- Remove an embedded function from RoleMixin and add tests for it (https://github.com/ansible/ansible/pull/72754).
- Remove the warning displayed when validating the arg spec of a role with dependencies and add it to the documentation.
- Restore the ability for changed_when/failed_when to function with group_by (#70844).
- Restored unsafe_writes functionality which was being skipped.
- Restructured pipelining settings to be at the connection plugins leaving base config as global and for backwards compatiblity.
- SSH plugin - Improve error message when ssh client is not found on the host
- Setup virtualization_facts - add RHV and oVirt type. This change will fully work for VMs in clusters at cluster level 4.4 or newer (https://github.com/ansible/ansible/pull/72876).
- Skip invalid collection names when listing in ansible-doc instead of throwing exception. Issue#72257
- Skip literal_eval for string filters results in native jinja. (https://github.com/ansible/ansible/issues/70831)
- Stop adding the connection variables to the output results
- Suppress warning when user directory used in --playbook-dir option with ansible-inventory command (https://github.com/ansible/ansible/issues/65262).
- TOML inventory - Ensure we register dump functions for ``AnsibleUnsafe`` to support dumping unsafe values. Note that the TOML format has no functionality to mark that the data is unsafe for re-consumption. (https://github.com/ansible/ansible/issues/71307)
- Terminal plugins - add "\e[m" to the list of ANSI sequences stripped from device output
- The ``docker`` and ``k8s`` action groups / module default groups now also support the moved modules in `community.docker <https://galaxy.ansible.com/community/docker>`_, `community.kubevirt <https://github.com/ansible-collections/community.kubevirt>`_, `community.okd <https://galaxy.ansible.com/community/okd>`_, and `kubernetes.core <https://galaxy.ansible.com/kubernetes/core>`_ (https://github.com/ansible/ansible/pull/72428).
- The ``flush()`` method of ``CachePluginAdjudicator`` now calls the plugin's ``flush()`` method instead of iterating over the keys that the adjudicator knows about and deleting those from the cache. (https://github.com/ansible/ansible/issues/68770)
- The `ansible_become` value was not being treated as a boolean value when set in an INI format inventory file (fixes bug https://github.com/ansible/ansible/issues/70476).
- The machine-readable changelog ``changelogs/changelog.yaml`` is now contained in the release.
- Updated docs and added warning on max_fail_percentage and free strategy usage. fixes issue 16666.
- VariableManager - Add the 'vars' key before getting delegated variables (https://github.com/ansible/ansible/issues/71092).
- Vault - Allow single vault encrypted values to be used directly as module parameters. (https://github.com/ansible/ansible/issues/68275)
- [set_fact] Corrected and expanded documentation as well as now raise errors that were previously ignored.
- account for bug in Python 2.6 that occurs during interpreter shutdown to avoid stack trace
- action plugins - change all action/module delegations to use FQ names while allowing overrides (https://github.com/ansible/ansible/issues/69788)
- add AlmaLinux to fact gathering (https://github.com/ansible/ansible/pull/73458)
- add constraints file for ``ansible_runner`` test since an update to ``psutil`` is now causing test failures
- add magic/connection vars updates from delegated host info.
- add support for alpine linux 'apk' package manager in package_facts
- allow become method 'su' to work on 'local' connection by allocating a fake tty.
- ansible-console - Ctrl+C (in a task) abort current task, and put you back on prompt (this behavior doesn't change) (ditto)
- ansible-console - Ctrl+C (on prompt) used to exit the shell, unlike most shells, it should just reset the current line (ie. abort it and spawn a new prompt) (https://github.com/ansible/ansible/issues/68529)
- ansible-console - Ctrl+D (on prompt) now exit the shell, this is the expected behavior in a shell (cf bash, sh, zsh, ipython, ...) (ditto)
- ansible-console - add more documentation, specifically on various commands[1] (https://github.com/ansible/ansible/issues/72195)
- ansible-console - fixes few strings' typos
- ansible-console - remove useless and poorly formatted comment section (replaced with [1])
- ansible-doc - account for an empty ``meta/main.yml`` file when displaying role information (https://github.com/ansible/ansible/pull/73590)
- ansible-doc - collection name for plugin top-level deprecation was not inserted when deprecating by version (https://github.com/ansible/ansible/pull/70344).
- ansible-doc - improve error message in text formatter when ``description`` is missing for a (sub-)option or a return value or its ``contains`` (https://github.com/ansible/ansible/pull/70046).
- ansible-doc - improve man page formatting to avoid problems when YAML anchors are used (https://github.com/ansible/ansible/pull/70045).
- ansible-doc - include the collection name in the text output (https://github.com/ansible/ansible/pull/70401).
- ansible-doc - plugin option deprecations now also get ``collection_name`` added (https://github.com/ansible/ansible/pull/71735).
- ansible-doc - properly show plugin name when ``name:`` is used instead of ``<plugin_type>:`` (https://github.com/ansible/ansible/pull/71966).
- ansible-galaxy - Cache the responses for available collection versions after getting all pages. (https://github.com/ansible/ansible/issues/73071)
- ansible-galaxy - Instead of assuming the first defined server is galaxy, filter based on the servers that support the v1 API, and return the first of those (https://github.com/ansible/ansible/issues/65440)
- ansible-galaxy - Use ``sys.exit`` instead of ``exit`` when reporting an error for the removed login command.
- ansible-galaxy - correct ``collections-path`` command line argument (https://github.com/ansible/ansible/issues/73127)
- ansible-galaxy - fixed galaxy role init command (https://github.com/ansible/ansible/issues/71977).
- ansible-galaxy collection download - fix downloading tar.gz files and collections in git repositories (https://github.com/ansible/ansible/issues/70429)
- ansible-galaxy collection install - fix fallback mechanism if the AH server did not have the collection requested - https://github.com/ansible/ansible/issues/70940
- ansible-galaxy download - fix bug when downloading a collection in a SCM subdirectory
- ansible-test - Add ``pytest < 6.0.0`` constraint for managed installations on Python 3.x to avoid issues with relative imports.
- ansible-test - Always connect additional Docker containers to the network used by the current container (if any).
- ansible-test - Always map ``/var/run/docker.sock`` into test containers created by the ``--docker`` option if the docker host is not ``localhost``.
- ansible-test - Attempt to detect the Docker hostname instead of assuming ``localhost``.
- ansible-test - Avoid using ``/tmp`` to resolve occasional failures starting tests with the ``--docker`` option.
- ansible-test - Change classification using ``--changed`` now consistently handles common configuration files for supported CI providers.
- ansible-test - Change detection now properly resolves relative imports instead of treating them as absolute imports.
- ansible-test - Correctly detect changes in a GitHub pull request when running on Azure Pipelines.
- ansible-test - Correctly detect running in a Docker container on Azure Pipelines.
- ansible-test - Do not try to validate PowerShell modules ``setup.ps1``, ``slurp.ps1``, and ``async_status.ps1``
- ansible-test - Prefer container IP at ``.NetworkSettings.Networks.{NetworkName}.IPAddress`` over ``.NetworkSettings.IPAddress``.
- ansible-test - Running tests using an installed version of ``ansible-test`` against one Python version from another no longer fails due to a missing ``egg-info`` directory. This could occur when testing plugins which import ``pkg_resources``.
- ansible-test - Running tests using an installed version of ``ansible-test`` no longer generates an error attempting to create an ``egg-info`` directory when an existing one is not found in the expected location. This could occur if the existing ``egg-info`` directory included a Python version specifier in the name.
- ansible-test - Skip installing requirements if they are already installed.
- ansible-test - Symbolic links are no longer used to inject ``python`` into the environment, since they do not work reliably in all cases. Instead, the existing Python based exec wrapper is always used.
- ansible-test - Temporarily limit ``cryptography`` to versions before 3.4 to enable tests to function.
- ansible-test - The ``--raw`` option for ``ansible-test shell --remote`` now uses ``sh`` for the shell instead of ``bash``, which may not be present.
- ansible-test - The ``--remote`` option has been updated for Python 2.7 to work around breaking changes in the newly released ``get-pip.py`` bootstrapper.
- ansible-test - The ``--remote`` option has been updated to use a versioned ``get-pip.py`` bootstrapper to avoid issues with future releases.
- ansible-test - The ``ansible-doc`` sanity test now works for ``netconf`` plugins.
- ansible-test - The ``changelog`` sanity test has been updated to ensure ``rstcheck`` does not load the ``sphinx`` module.
- ansible-test - The ``cs`` and ``openshift`` test plugins now search for containers on the current network instead of assuming the ``bridge`` network.
- ansible-test - The ``resource_prefix`` variable provided to tests running on Azure Pipelines is now converted to lowercase to match other CI providers.
- ansible-test - Unified SSH key management for all instances created with the ``--remote`` or ``--docker`` options.
- ansible-test - Using the ``--remote`` option on Azure Pipelines now works from a job running in a container.
- ansible-test - ``cryptography`` is now limited to versions prior to 3.2 only when an incompatible OpenSSL version (earlier than 1.1.0) is detected
- ansible-test - add constraint for ``cffi`` to prevent failure on systems with older versions of ``gcc`` (https://foss.heptapod.net/pypy/cffi/-/issues/480)
- ansible-test - convert target paths to unicode on Python 2 to avoid ``UnicodeDecodeError`` (https://github.com/ansible/ansible/issues/68398, https://github.com/ansible/ansible/pull/72623).
- ansible-test - ensure unit test paths for connection and inventory plugins are correctly identified for collections (https://github.com/ansible/ansible/issues/73876).
- ansible-test - improve classification of changes to ``.gitignore``, ``COPYING``, ``LICENSE``, ``Makefile``, and all files ending with one of ``.in`, ``.md`, ``.rst``, ``.toml``, ``.txt`` in the collection root directory (https://github.com/ansible/ansible/pull/72353).
- ansible-test - integration and unit test change detection now works for filter, lookup and test plugins
- ansible-test now always uses the ``--python`` option for ``virtualenv`` to select the correct interpreter when creating environments with the ``--venv`` option
- ansible-test sanity changelog test - bump dependency on antsibull-changelog to 0.9.0 so that `fragments that add new plugins or objects <https://github.com/ansible-community/antsibull-changelog/blob/main/docs/changelogs.rst#adding-new-roles-playbooks-test-and-filter-plugins>`_ will not fail validation (https://github.com/ansible/ansible/pull/73428).
- ansible-test units - fixed collection location code to work under pytest >= 6.0.0
- ansible-test validate-modules - ``version_added`` on module level was not validated for modules in collections (https://github.com/ansible/ansible/pull/70869).
- ansible-test validate-modules - return correct error codes ``option-invalid-version-added`` resp. ``return-invalid-version-added`` instead of the wrong error ``deprecation-either-date-or-version`` when an invalid value of ``version_added`` is specified for an option or a return value (https://github.com/ansible/ansible/pull/70869).
- ansible-test validate-modules - when a module uses ``add_file_common_args=True`` and does not use a keyword argument for ``argument_spec`` in ``AnsibleModule()``, the common file arguments were not considered added during validation (https://github.com/ansible/ansible/pull/72334).
- ansible_pkg_mgr fact - now correctly returns ``atomic_container`` when run on "RHEL for Edge" images and Fedora/RHEL/CentOS Atomic Host (https://github.com/ansible/ansible/issues/73084).
- api - time.clock is removed in Python 3.8, add backward compatible code (https://github.com/ansible/ansible/issues/70649).
- apt - add ``fail_on_autoremove`` param to apt module to avoid unintended package removals (https://github.com/ansible/ansible/issues/63231)
- apt - include exception message from apt python library in error output
- apt_key - Specifying ``file`` as mutually exclusive with ``data``, ``keyserver``, ``url`` (https://github.com/ansible/ansible/pull/70492).
- apt_repository - fixes ``mode`` doc to remove ineffective default (https://github.com/ansible/ansible/pull/70319).
- assemble - fix decrypt argument in the module (https://github.com/ansible/ansible/issues/65450).
- async - Fix Python 3 interpreter parsing from module by comparing with bytes (https://github.com/ansible/ansible/issues/70690)
- async_wrapper - Fix race condition when ``~/.ansible_async`` folder tries to be created by multiple async tasks at the same time - https://github.com/ansible/ansible/issues/59306
- avoid possible errors accessing os.environ by not assuming existance of variables.
- basic - handle exceptions for default selectors in Python 2.7 (https://github.com/ansible/ansible/issues/71704).
- basic - use PollSelector implementation when DefaultSelector fails (https://github.com/ansible/ansible/issues/70238).
- bcrypt hashing - Ensure we repair the salt, to avoid warnings (https://github.com/ansible/ansible/issues/36129)
- blockinfile - properly insert a block at the end of a file that does not have a trailing newline character (https://github.com/ansible/ansible/issues/72055)
- blockinfile now returns name of backup file when this option is used.
- clarified changed status to reflect existing rule that had never been written down.
- collection loader - fix bogus code coverage entries for synthetic packages
- collection metadata - ensure collection loader uses libyaml/CSafeLoader to parse collection metadata if available
- connection/ssh, ensure parameters come from correct source get_option, so functionality matches docs.
- connection/ssh, fix reset to use same parameters to check if socket exists as actually used, was hardcoded to default string construction previouslly.
- cron - cron file should not be empty after adding var (https://github.com/ansible/ansible/pull/71207)
- cron - encode and decode crontab files in UTF-8 explicitly to allow non-ascii chars in cron filepath and job (https://github.com/ansible/ansible/issues/69492)
- default callback - Ensure that the ``host_pinned`` strategy is not treated as lockstep (https://github.com/ansible/ansible/issues/73364)
- delegate_to - Ensure that calculating ``delegate_to`` vars with a loop uses the correct context to correctly evaluate the loop (https://github.com/ansible/ansible/issues/37132)
- display correct error information when an error exists in the last line of the file (https://github.com/ansible/ansible/issues/16456)
- distribution - add support for Pardus Linux distribution (https://github.com/ansible/ansible/issues/71636).
- distribution facts - Allow ``distribution_major_version`` and ``distribution_version`` to work for RC and PRERELEASE versions of FreeBSD (and derived distributions) (https://github.com/ansible/ansible/issues/72331).
- dnf - fix filtering to avoid dependncy conflicts (https://github.com/ansible/ansible/issues/72316)
- dnf - it is now possible to specify both ``security: true`` and ``bugfix: true`` to install updates of both types. Previously, only security would get installed if both were true. (https://github.com/ansible/ansible/issues/70854)
- ensure 'local' connection always has the correct default user for actions to consume.
- ensure delegated vars can resolve hostvars object and access vars from hostvars[inventory_hostname].
- ensure find_mount_point consistently returns text.
- ensure we don't clobber role vars data when getting an empty file
- expect - Operate pexpect with bytes to avoid potential encoding issues (https://github.com/ansible/ansible/issues/29351)
- facts - account for Slackware OS with ``+`` in the name (https://github.com/ansible/ansible/issues/38760)
- facts - fix distribution fact for SLES4SAP (https://github.com/ansible/ansible/pull/71559).
- facts - fix incorrect UTC timestamp in ``iso8601_micro`` and ``iso8601``
- facts - properly report virtualization facts for Linux guests running on bhyve (https://github.com/ansible/ansible/issues/73167)
- file - prevent link src from being rewritten when src is not specified explicitly (https://github.com/ansible/ansible/issues/65448)
- file - the module should warn in check_mode when path an owner/group don't exist (https://github.com/ansible/ansible/issues/67307).
- find module - Don't treat empty excludes as a match (https://github.com/ansible/ansible/issues/70640)
- find module - Stop traversing directories past the requested depth. (https://github.com/ansible/ansible/issues/73627)
- fix issue with inventory_hostname and delegated host vars mixing on connection settings.
- fortimanager httpapi plugin - fix redirect to point to the ``fortinet.fortimanager`` collection (https://github.com/ansible/ansible/pull/71073).
- galaxy - handle plus sign in user token appearing in role url (https://github.com/ansible/ansible/issues/45475).
- get_sysctl now handles multiline values and does not die silently anymore.
- get_url - skip checksum during ``--check`` (https://github.com/ansible/ansible/issues/61369).
- git - Only pass ``--raw`` flag to git verify commands (verify-tag, verify-commit) when ``gpg_whitelist`` is in use. Otherwise don't pass it so that non-whitelist GPG validation still works on older Git versions. (https://github.com/ansible/ansible/issues/64469)
- gluster modules - fix redirect to point to the ``gluster.gluster`` collection (https://github.com/ansible/ansible/pull/71240).
- hostname - Fixed an issue where the hostname on the alinux could not be set.
- hostname - add Almalinux support (https://github.com/ansible/ansible/pull/73619)
- hostname - add macOS support (https://github.com/ansible/ansible/pull/54439)
- if the ``type`` for a module parameter in the argument spec is callable, do not pass ``kwargs`` to avoid errors (https://github.com/ansible/ansible/issues/70017)
- import_playbook - change warning about extra parameters to deprecation (https://github.com/ansible/ansible/issues/72745)
- improve deprecation message when using bare variable (https://github.com/ansible/ansible/pull/70687)
- inventory - pass the vars dictionary to combine_vars instead of an individual key's value (https://github.com/ansible/ansible/issues/72975).
- inventory plugins - Let plugins define the sanitization method for the constructed ``groups`` feature.
- inventory_hostnames - Use ``InventoryManager`` instead of trying to replicate its behavior (https://github.com/ansible/ansible/issues/17268)
- is_string/vault - Ensure the is_string helper properly identifies AnsibleVaultEncryptedUnicode as a string (https://github.com/ansible/ansible/pull/71609)
- j2 plugin loader clarified comments, made note with better fqcn detection.
- lineinfile - fix not subscriptable error in exception handling around file creation
- linux network facts - get the correct value for broadcast address (https://github.com/ansible/ansible/issues/64384)
- native jinja2 types - properly handle Undefined in nested data.
- notify keyword is not ignored anymore on import_tasks, also able to apply to blocks now.
- package - use list of built in package managers from facts rather than creating a new list
- paramiko connection plugin - Ensure we only reset the connection when one has been previously established (https://github.com/ansible/ansible/issues/65812)
- password hashing - Ensure we validate salts against allowed characters and length when using ``crypt`` (https://github.com/ansible/ansible/issues/71107)
- password lookup - Try to automatically generate salts using known salt sizes (https://github.com/ansible/ansible/issues/53750)
- pause - Fix indefinite hang when using a pause task on a background process (https://github.com/ansible/ansible/issues/32142)
- pause - catch additional error on setting up curses (https://github.com/ansible/ansible/pull/73588).
- pause - do not warn when running in the background if a timeout is provided (https://github.com/ansible/ansible/issues/73042)
- pause - handle exception when there is no stdout (https://github.com/ansible/ansible/pull/47851)
- powershell - fix escaping of strings that broken modules like fetch when dealing with special chars - https://github.com/ansible/ansible/issues/62781
- powershell - fix the CLIXML parser when it contains nested CLIXML objects - https://github.com/ansible/ansible/issues/69550
- powershell - remove getting the PowerShell version from the env var ``POWERSHELL_VERSION``. This feature never worked properly and can cause conflicts with other libraries that use this var
- psrp - Fix hang when copying an empty file to the remote target
- psrp - Use native PSRP mechanism when copying files to support custom endpoints
- quote filter - normalize how ``None`` is handled, to match Python3 behavior (https://github.com/ansible/ansible/issues/32174)
- reboot - Add support for the runit init system, used on Void Linux, that does not support the normal Linux syntax.
- remove contradictory recomendation from template docs. https://github.com/ansible/ansible/issues/63484
- remove redundant remote_user setting in play_context for local as plugin already does it, also removes fork/thread issue from use of pwd library.
- reset logging level to INFO due to CVE-2019-14846.
- restrict module valid JSON parsed output to objects as lists are not valid responses.
- runas - create a new token when running as ``SYSTEM`` to ensure it has the full privileges assigned to that account
- service - Fix for the BSD rcconf code using a Python 2 specific string replace function
- set_mode_if_different - handle symlink if it is inside a directory with sticky bit set (https://github.com/ansible/ansible/pull/45198)
- setup, don't give up on all local facts gathering if one script file fails.
- several fixes to make apt_key better at identifying needs for change and also to avoid changes in check_mode.
- shell - fix quoting of mkdir command in creation of remote_tmp in order to allow spaces and other special characters (https://github.com/ansible/ansible/issues/69577).
- splunk httpapi plugin - switch from splunk.enterprise_security to splunk.es in runtime.yml to reflect upstream change of Collection Name
- ssh connection plugin - use ``get_option()`` rather than ``_play_context`` to ensure ``ANSBILE_SSH_ARGS`` are applied properly (https://github.com/ansible/ansible/issues/70437)
- stat - handle colons in filename while parsing the mimetype output (https://github.com/ansible/ansible/issues/70256).
- strftime filter - Input epoch is allowed to be a float (https://github.com/ansible/ansible/issues/71257)
- su become plugin, ensure correct type for localization option.
- systemd - account for templated unit files using ``@`` when searching for the unit file (https://github.com/ansible/ansible/pull/72347#issuecomment-730626228)
- systemd - fixed chroot usage on new versions of systemd, that broke because of upstream changes in systemctl output
- systemd - follow up fix to https://github.com/ansible/ansible/issues/72338 to use ``list-unit-files`` rather than ``list-units`` in order to show all units files on the system.
- systemd - made the systemd module work correctly when the SYSTEMD_OFFLINE environment variable is set
- systemd - preserve the full unit name when using a templated service and ``systemd`` failed to parse dbus due to a known bug in ``systemd`` (https://github.com/ansible/ansible/pull/72985)
- systemd - work around bug with ``systemd`` 245 and 5.8 kernel that does not correctly report service state (https://github.com/ansible/ansible/issues/71528)
- task parsing - strip spaces from action name when using ``action: foo bar=baz`` form. (https://github.com/ansible/ansible/issues/62136)
- templating - fix error message for ``x in y`` when y is undefined (https://github.com/ansible/ansible/issues/70984)
- the unvault lookup plugin returned a byte string. Now returns a real string.
- to_text(stdout) before json.loads in psrp.Connection.put_file in case stdout is bytes
- unarchive - ``zip`` unarchive no longer errors on RHEL/CentOS 6 and old Fedora when attempting to use a numeric gid (https://github.com/ansible/ansible/issues/71903).
- unarchive - check ``fut_gid`` against ``run_gid`` in addition to supplemental groups (https://github.com/ansible/ansible/issues/49284)
- undeprecate hash_merge setting and add more docs clarifying its use and why not to use it.
- uri - ``status_code`` elements are type ``int``
- url lookup - make sure that options supplied in ansible.cfg are actually used (https://github.com/ansible/ansible/pull/71736).
- url lookup - set default user agent to ``ansible-httpget`` (https://github.com/ansible/ansible/pull/72324)
- urls - Close filedescriptor of certificate chain tempfile to prevent stale filedescriptor leakage (https://github.com/ansible/ansible/pull/71825).
- user - AnsibleModule.run_command returns a tuple of return code, stdout and stderr. The module main function of the user module expects user.create_user to return a tuple of return code, stdout and stderr. Fix the locations where stdout and stderr got reversed.
- user - Local users with an expiry date cannot be created as the ``luseradd`` / ``lusermod`` commands do not support the ``-e`` option. Set the expiry time in this case via ``lchage`` after the user was created / modified. (https://github.com/ansible/ansible/issues/71942)
- user - do the right thing when ``password_lock=True`` and ``password`` are used together (https://github.com/ansible/ansible/issues/72992)
- user - don't create home directory and missing parents when create_home == false (https://github.com/ansible/ansible/pull/70600).
- validate-modules - do not raise an ``AttributeError`` if a value is assigned to a module attribute in a try/except block.
- vault - Support reading raw binary data from stdin under python3
- virtual facts - kubevirt is now identified as "KubeVirt" and with a "guest" role instead of "kvm" and "host" role (https://github.com/ansible/ansible/issues/72001).
- wait_for - catch and ignore errors when getting active connections with psutil (https://github.com/ansible/ansible/issues/72322)
- win setup - Fix redirection path for the windows setup module
- windows async - use full path when calling PowerShell to reduce reliance on environment vars being correct - https://github.com/ansible/ansible/issues/70655
- winrm - preserve winrm forensic data on put_file failures
- yamllint - do not raise an ``AttributeError`` if a value is assigned to a module attribute at the top of the module.

amazon.aws
~~~~~~~~~~

- ec2_vol - a creation or update now returns a structure with an up to date list of tags (https://github.com/ansible-collections/amazon.aws/pull/241).

ansible.netcommon
~~~~~~~~~~~~~~~~~

- Expose connection class object to rm_template (https://github.com/ansible-collections/ansible.netcommon/pull/180)
- network_cli - When using ssh_type libssh, handle closed connection gracefully instead of throwing an exception

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

arista.eos
~~~~~~~~~~

- Add 'virtual' key to denote the existence of virtual address on an interface.(https://github.com/ansible-collections/arista.eos/pull/170).
- Fixed the regex to parse the running config correctly.(https://github.com/ansible-collections/arista.eos/issues/150)
- cliconf plugin - Prevent `get_capabilities()` from getting larger every time it is called

cisco.asa
~~~~~~~~~

- To fix ASA acls module where replace wasn't working as expected (https://github.com/ansible-collections/cisco.asa/pull/92).

cisco.ios
~~~~~~~~~

- To fix ios_acls parsed state example under module doc (https://github.com/ansible-collections/cisco.ios/pull/244).
- fix error when comparing two vlan using string instead of the int value (https://github.com/ansible-collections/cisco.ios/pull/249).

cisco.iosxr
~~~~~~~~~~~

- Fix to accurately report configuration failure during pseudo-atomic operation fior iosxr-6.6.3 (https://github.com/ansible-collections/cisco.iosxr/issues/92).

cisco.meraki
~~~~~~~~~~~~

- meraki_mx_content_filtering - Fix crash with idempotent condition due to improper sorting

cisco.nxos
~~~~~~~~~~

- Fail gracefully when BGP is already configured with a different ASN when states merged or replaced is used.
- Fixes to nxos_logging, nxos_igmp_snooping, nxos_l3_interfaces, nxos_ospf_interfaces and nxos_static_routes to conform with latest CLI behaviour.
- Properly configure neighbor timers and shutdown state (https://github.com/ansible-collections/cisco.nxos/issues/240).

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

- ``docker_swarm_service`` - fix KeyError on caused by reference to deprecated option ``update_failure_action`` (https://github.com/ansible-collections/community.docker/pull/100).
- docker_container - fix healthcheck disabling idempotency issue with strict comparison (https://github.com/ansible-collections/community.docker/issues/85).
- docker_image - prevent module failure when removing image that is removed between inspection and removal (https://github.com/ansible-collections/community.docker/pull/87).
- docker_image - prevent module failure when removing non-existant image by ID (https://github.com/ansible-collections/community.docker/pull/87).
- docker_image_info - prevent module failure when image vanishes between listing and inspection (https://github.com/ansible-collections/community.docker/pull/87).
- docker_image_info - prevent module failure when querying non-existant image by ID (https://github.com/ansible-collections/community.docker/pull/87).
- docker_swarm_service - mark ``secrets`` module option with ``no_log=False`` since it does not leak secrets (https://github.com/ansible-collections/community.general/pull/2001).

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

netbox.netbox
~~~~~~~~~~~~~

- Remove ansible.netcommon and community.general dependencies from collection
- netbox_ip_address - Added assigned_object to ALLOWED_QUERY_PARAMS

openvswitch.openvswitch
~~~~~~~~~~~~~~~~~~~~~~~

- Allow deleting key from table without specifying value (https://github.com/ansible-collections/openvswitch.openvswitch/issues/64).

ovirt.ovirt
~~~~~~~~~~~

- Set ``auth`` options into argument spec definition so Ansible will validate the user options
- Set ``no_log`` on ``password`` and ``token`` in the ``auth`` dict so the values are exposed in the invocation log

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

theforeman.foreman
~~~~~~~~~~~~~~~~~~

- content_view_version - make the ``version`` parameter not fail when the version was entered without a minor part (https://github.com/theforeman/foreman-ansible-modules/issues/1087)
- host - allow moving hosts between Organizations and Locations (https://bugzilla.redhat.com/show_bug.cgi?id=1901716)
- host - don't filter ``false`` values for ``interfaces_attributes`` (https://github.com/theforeman/foreman-ansible-modules/issues/1148)
- host - fix subnet/domain assignment when multiple interfaces are defined (https://github.com/theforeman/foreman-ansible-modules/issues/1095)
- host, hostgroup - select kickstart_repository based on lifecycle_environment and content_view if those are set (https://github.com/theforeman/foreman-ansible-modules/issues/1090, https://bugzilla.redhat.com/1915872)
- host_info, repository_info - correctly fetch all entities when neither ``name`` nor ``search`` is set
- host_info, repository_info - enforce mutual exclusivity of ``name`` and ``search``
- resource_info - correctly show the exact resource when passing ``id`` in ``params``

vyos.vyos
~~~~~~~~~

- Update docs to clarify the idemptonecy releated caveat and add it in the output warnings (https://github.com/ansible-collections/ansible.netcommon/pull/189)
- cliconf plugin - Prevent `get_capabilities()` from getting larger every time it is called

Known Issues
------------

Ansible-core
~~~~~~~~~~~~

- ansible-test - The ``pylint`` sanity test no longer correctly detects "bad" variable names for non-constants. See https://github.com/PyCQA/pylint/issues/3701 for additional details.

New Plugins
-----------

Cache
~~~~~

- ansible.netcommon.memory - RAM backed, non persistent cache.

Filter
~~~~~~

- community.general.version_sort - Sort a list according to version order instead of pure alphabetical one

New Modules
-----------

Ansible-core
~~~~~~~~~~~~

- ansible.builtin.validate_argument_spec - Validate role argument specs.

cisco.ios
~~~~~~~~~

- cisco.ios.ios_bgp_address_family - BGP Address Family resource module.

cisco.iosxr
~~~~~~~~~~~

- cisco.iosxr.iosxr_bgp_address_family - Manages BGP Address Family resource module.
- cisco.iosxr.iosxr_bgp_global - Manages BGP global resource module.
- cisco.iosxr.iosxr_bgp_neighbor_address_family - Manages BGP neighbor address family resource module.

cisco.nxos
~~~~~~~~~~

- cisco.nxos.nxos_bgp_address_family - BGP Address Family resource module.
- cisco.nxos.nxos_bgp_neighbor_address_family - BGP Neighbor Address Family resource module.

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

hetzner.hcloud
~~~~~~~~~~~~~~

- hetzner.hcloud.hcloud_firewall - Manage Hetzner Cloud Firewalls

junipernetworks.junos
~~~~~~~~~~~~~~~~~~~~~

- junipernetworks.junos.junos_bgp_address_family - Manage BGP Address Family attributes of interfaces on Junos devices.

sensu.sensu_go
~~~~~~~~~~~~~~

- sensu.sensu_go.cluster - Manage Sensu Go clusters
- sensu.sensu_go.cluster_info - List available Sensu Go clusters
- sensu.sensu_go.etcd_replicator - Manage Sensu Go etcd replicators
- sensu.sensu_go.etcd_replicator_info - List Sensu Go etcd replicators

theforeman.foreman
~~~~~~~~~~~~~~~~~~

- theforeman.foreman.host_info - Fetch information about Hosts
- theforeman.foreman.puppetclasses_import - Import Puppet Classes from a Proxy
- theforeman.foreman.repository_info - Fetch information about Repositories

vyos.vyos
~~~~~~~~~

- vyos.vyos.vyos_bgp_global - BGP Global Resource Module.

Unchanged Collections
---------------------

- azure.azcollection (still version 1.4.0)
- check_point.mgmt (still version 2.0.0)
- chocolatey.chocolatey (still version 1.0.2)
- cisco.aci (still version 2.0.0)
- cisco.mso (still version 1.1.0)
- cisco.nso (still version 1.0.3)
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
- ibm.qradar (still version 1.0.3)
- infinidat.infinibox (still version 1.2.4)
- inspur.sm (still version 1.1.2)
- mellanox.onyx (still version 1.0.0)
- netapp_eseries.santricity (still version 1.1.0)
- ngine_io.cloudstack (still version 2.0.0)
- ngine_io.exoscale (still version 1.0.0)
- ngine_io.vultr (still version 1.1.0)
- purestorage.flashblade (still version 1.4.0)
- servicenow.servicenow (still version 1.0.4)
- splunk.es (still version 1.0.2)
- wti.remote (still version 1.0.1)
