# Ansible 11 Release Notes

This changelog describes changes since Ansible 10\.0\.0\.

- <a href="#v11-7-0">v11\.7\.0</a>
    - <a href="#release-summary">Release Summary</a>
    - <a href="#added-collections">Added Collections</a>
    - <a href="#ansible-core">Ansible\-core</a>
    - <a href="#changed-collections">Changed Collections</a>
    - <a href="#major-changes">Major Changes</a>
    - <a href="#minor-changes">Minor Changes</a>
    - <a href="#deprecated-features">Deprecated Features</a>
    - <a href="#bugfixes">Bugfixes</a>
    - <a href="#known-issues">Known Issues</a>
    - <a href="#new-modules">New Modules</a>
    - <a href="#unchanged-collections">Unchanged Collections</a>
- <a href="#v11-6-0">v11\.6\.0</a>
    - <a href="#release-summary-1">Release Summary</a>
    - <a href="#ansible-core-1">Ansible\-core</a>
    - <a href="#changed-collections-1">Changed Collections</a>
    - <a href="#major-changes-1">Major Changes</a>
    - <a href="#minor-changes-1">Minor Changes</a>
    - <a href="#deprecated-features-1">Deprecated Features</a>
    - <a href="#bugfixes-1">Bugfixes</a>
    - <a href="#known-issues-1">Known Issues</a>
    - <a href="#new-plugins">New Plugins</a>
    - <a href="#new-modules-1">New Modules</a>
    - <a href="#unchanged-collections-1">Unchanged Collections</a>
- <a href="#v11-5-0">v11\.5\.0</a>
    - <a href="#release-summary-2">Release Summary</a>
    - <a href="#added-collections-1">Added Collections</a>
    - <a href="#ansible-core-4">Ansible\-core</a>
    - <a href="#changed-collections-2">Changed Collections</a>
    - <a href="#major-changes-2">Major Changes</a>
    - <a href="#minor-changes-2">Minor Changes</a>
    - <a href="#deprecated-features-2">Deprecated Features</a>
    - <a href="#bugfixes-2">Bugfixes</a>
    - <a href="#known-issues-2">Known Issues</a>
    - <a href="#new-plugins-1">New Plugins</a>
    - <a href="#new-modules-2">New Modules</a>
    - <a href="#unchanged-collections-2">Unchanged Collections</a>
- <a href="#v11-4-0">v11\.4\.0</a>
    - <a href="#release-summary-3">Release Summary</a>
    - <a href="#ansible-core-6">Ansible\-core</a>
    - <a href="#changed-collections-3">Changed Collections</a>
    - <a href="#major-changes-3">Major Changes</a>
    - <a href="#minor-changes-3">Minor Changes</a>
    - <a href="#breaking-changes--porting-guide">Breaking Changes / Porting Guide</a>
    - <a href="#deprecated-features-3">Deprecated Features</a>
    - <a href="#bugfixes-3">Bugfixes</a>
    - <a href="#new-modules-3">New Modules</a>
    - <a href="#unchanged-collections-3">Unchanged Collections</a>
- <a href="#v11-3-0">v11\.3\.0</a>
    - <a href="#release-summary-4">Release Summary</a>
    - <a href="#ansible-core-8">Ansible\-core</a>
    - <a href="#changed-collections-4">Changed Collections</a>
    - <a href="#minor-changes-4">Minor Changes</a>
    - <a href="#deprecated-features-4">Deprecated Features</a>
    - <a href="#bugfixes-4">Bugfixes</a>
    - <a href="#known-issues-3">Known Issues</a>
    - <a href="#new-plugins-2">New Plugins</a>
    - <a href="#new-modules-4">New Modules</a>
    - <a href="#unchanged-collections-4">Unchanged Collections</a>
- <a href="#v11-2-0">v11\.2\.0</a>
    - <a href="#release-summary-5">Release Summary</a>
    - <a href="#ansible-core-11">Ansible\-core</a>
    - <a href="#changed-collections-5">Changed Collections</a>
    - <a href="#major-changes-4">Major Changes</a>
    - <a href="#minor-changes-5">Minor Changes</a>
    - <a href="#deprecated-features-5">Deprecated Features</a>
    - <a href="#security-fixes">Security Fixes</a>
    - <a href="#bugfixes-5">Bugfixes</a>
    - <a href="#known-issues-4">Known Issues</a>
    - <a href="#new-plugins-3">New Plugins</a>
    - <a href="#new-modules-5">New Modules</a>
    - <a href="#unchanged-collections-5">Unchanged Collections</a>
- <a href="#v11-1-0">v11\.1\.0</a>
    - <a href="#release-summary-6">Release Summary</a>
    - <a href="#ansible-core-13">Ansible\-core</a>
    - <a href="#changed-collections-6">Changed Collections</a>
    - <a href="#major-changes-5">Major Changes</a>
    - <a href="#minor-changes-6">Minor Changes</a>
    - <a href="#deprecated-features-6">Deprecated Features</a>
    - <a href="#security-fixes-1">Security Fixes</a>
    - <a href="#bugfixes-6">Bugfixes</a>
    - <a href="#known-issues-5">Known Issues</a>
    - <a href="#new-plugins-4">New Plugins</a>
    - <a href="#new-modules-6">New Modules</a>
    - <a href="#unchanged-collections-6">Unchanged Collections</a>
- <a href="#v11-0-0">v11\.0\.0</a>
    - <a href="#release-summary-7">Release Summary</a>
    - <a href="#removed-collections">Removed Collections</a>
    - <a href="#added-collections-2">Added Collections</a>
    - <a href="#ansible-core-17">Ansible\-core</a>
    - <a href="#included-collections">Included Collections</a>
    - <a href="#major-changes-6">Major Changes</a>
    - <a href="#minor-changes-7">Minor Changes</a>
    - <a href="#breaking-changes--porting-guide-1">Breaking Changes / Porting Guide</a>
    - <a href="#deprecated-features-7">Deprecated Features</a>
    - <a href="#removed-features-previously-deprecated">Removed Features \(previously deprecated\)</a>
    - <a href="#security-fixes-2">Security Fixes</a>
    - <a href="#bugfixes-7">Bugfixes</a>
    - <a href="#known-issues-6">Known Issues</a>
    - <a href="#new-plugins-5">New Plugins</a>
    - <a href="#new-modules-7">New Modules</a>
    - <a href="#unchanged-collections-7">Unchanged Collections</a>

<a id="v11-7-0"></a>
## v11\.7\.0

- <a href="#release-summary">Release Summary</a>
- <a href="#added-collections">Added Collections</a>
- <a href="#ansible-core">Ansible\-core</a>
- <a href="#changed-collections">Changed Collections</a>
- <a href="#major-changes">Major Changes</a>
    - <a href="#dellemc-openmanage">dellemc\.openmanage</a>
- <a href="#minor-changes">Minor Changes</a>
    - <a href="#cloud-common">cloud\.common</a>
    - <a href="#cloudscale-ch-cloud">cloudscale\_ch\.cloud</a>
    - <a href="#community-general">community\.general</a>
    - <a href="#community-libvirt">community\.libvirt</a>
    - <a href="#community-mysql">community\.mysql</a>
    - <a href="#community-rabbitmq">community\.rabbitmq</a>
    - <a href="#community-routeros">community\.routeros</a>
    - <a href="#community-sops">community\.sops</a>
    - <a href="#community-vmware">community\.vmware</a>
    - <a href="#hitachivantara-vspone-block">hitachivantara\.vspone\_block</a>
    - <a href="#ibm-storage-virtualize">ibm\.storage\_virtualize</a>
    - <a href="#ovirt-ovirt">ovirt\.ovirt</a>
    - <a href="#telekom-mms-icinga-director">telekom\_mms\.icinga\_director</a>
- <a href="#deprecated-features">Deprecated Features</a>
    - <a href="#community-crypto">community\.crypto</a>
    - <a href="#community-general-1">community\.general</a>
    - <a href="#community-vmware-1">community\.vmware</a>
- <a href="#bugfixes">Bugfixes</a>
    - <a href="#check-point-mgmt">check\_point\.mgmt</a>
    - <a href="#cisco-meraki">cisco\.meraki</a>
    - <a href="#cloudscale-ch-cloud-1">cloudscale\_ch\.cloud</a>
    - <a href="#community-crypto-1">community\.crypto</a>
    - <a href="#community-dns">community\.dns</a>
    - <a href="#community-docker">community\.docker</a>
    - <a href="#community-general-2">community\.general</a>
    - <a href="#community-hrobot">community\.hrobot</a>
    - <a href="#community-mysql-1">community\.mysql</a>
    - <a href="#community-postgresql">community\.postgresql</a>
    - <a href="#community-rabbitmq-1">community\.rabbitmq</a>
    - <a href="#community-vmware-2">community\.vmware</a>
    - <a href="#containers-podman">containers\.podman</a>
    - <a href="#f5networks-f5-modules">f5networks\.f5\_modules</a>
    - <a href="#hitachivantara-vspone-block-1">hitachivantara\.vspone\_block</a>
    - <a href="#ibm-storage-virtualize-1">ibm\.storage\_virtualize</a>
    - <a href="#microsoft-ad">microsoft\.ad</a>
    - <a href="#ovirt-ovirt-1">ovirt\.ovirt</a>
    - <a href="#telekom-mms-icinga-director-1">telekom\_mms\.icinga\_director</a>
- <a href="#known-issues">Known Issues</a>
    - <a href="#dellemc-openmanage-1">dellemc\.openmanage</a>
- <a href="#new-modules">New Modules</a>
    - <a href="#cloudscale-ch-cloud-2">cloudscale\_ch\.cloud</a>
    - <a href="#community-hrobot-1">community\.hrobot</a>
    - <a href="#community-libvirt-1">community\.libvirt</a>
    - <a href="#hitachivantara-vspone-block-2">hitachivantara\.vspone\_block</a>
    - <a href="#telekom-mms-icinga-director-2">telekom\_mms\.icinga\_director</a>
- <a href="#unchanged-collections">Unchanged Collections</a>

<a id="release-summary"></a>
### Release Summary

Release Date\: 2025\-06\-17

[Porting Guide](https\://docs\.ansible\.com/ansible/devel/porting\_guides\.html)

<a id="added-collections"></a>
### Added Collections

* community\.proxmox \(version 1\.0\.1\)

<a id="ansible-core"></a>
### Ansible\-core

Ansible 11\.7\.0 contains ansible\-core version 2\.18\.6\.
This is the same version of ansible\-core as in the previous Ansible release\.

<a id="changed-collections"></a>
### Changed Collections

If not mentioned explicitly\, the changes are reported in the combined changelog below\.

| Collection                  | Ansible 11.6.0 | Ansible 11.7.0 | Notes                                                                                                                        |
| --------------------------- | -------------- | -------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| azure.azcollection          | 3.3.1          | 3.4.0          | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
| check_point.mgmt            | 6.4.0          | 6.4.1          |                                                                                                                              |
| cisco.meraki                | 2.21.1         | 2.21.3         |                                                                                                                              |
| cloud.common                | 4.1.0          | 4.2.0          |                                                                                                                              |
| cloudscale_ch.cloud         | 2.4.1          | 2.5.1          |                                                                                                                              |
| community.crypto            | 2.26.1         | 2.26.3         |                                                                                                                              |
| community.dns               | 3.2.4          | 3.2.5          |                                                                                                                              |
| community.docker            | 4.6.0          | 4.6.1          |                                                                                                                              |
| community.general           | 10.7.0         | 10.7.1         |                                                                                                                              |
| community.hrobot            | 2.3.0          | 2.4.0          |                                                                                                                              |
| community.libvirt           | 1.3.1          | 1.4.0          |                                                                                                                              |
| community.mongodb           | 1.7.9          | 1.7.10         | There are no changes recorded in the changelog.                                                                              |
| community.mysql             | 3.13.0         | 3.14.0         |                                                                                                                              |
| community.okd               | 4.0.1          | 4.0.2          |                                                                                                                              |
| community.postgresql        | 3.14.1         | 3.14.2         |                                                                                                                              |
| community.proxmox           |                | 1.0.1          | The collection was added to Ansible                                                                                          |
| community.rabbitmq          | 1.4.0          | 1.5.0          |                                                                                                                              |
| community.routeros          | 3.6.0          | 3.8.0          |                                                                                                                              |
| community.sops              | 2.0.5          | 2.1.0          |                                                                                                                              |
| community.vmware            | 5.6.0          | 5.7.0          |                                                                                                                              |
| containers.podman           | 1.16.3         | 1.16.4         |                                                                                                                              |
| dellemc.openmanage          | 9.12.0         | 9.12.1         |                                                                                                                              |
| f5networks.f5_modules       | 1.35.0         | 1.36.0         |                                                                                                                              |
| hitachivantara.vspone_block | 3.4.1          | 3.5.0          |                                                                                                                              |
| ibm.storage_virtualize      | 2.7.3          | 2.7.4          |                                                                                                                              |
| kubevirt.core               | 2.2.2          | 2.2.3          | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
| microsoft.ad                | 1.9.0          | 1.9.1          |                                                                                                                              |
| ovirt.ovirt                 | 3.2.0          | 3.2.1          |                                                                                                                              |
| telekom_mms.icinga_director | 2.2.2          | 2.3.0          |                                                                                                                              |

<a id="major-changes"></a>
### Major Changes

<a id="dellemc-openmanage"></a>
#### dellemc\.openmanage

* idrac\_attributes \- This module is enhanced to support iDRAC10\.
* idrac\_attributes \- This role is enhanced to support iDRAC10\.
* idrac\_lifecycle\_controller\_jobs \- This module is enhanced to support iDRAC10\.
* idrac\_lifecycle\_controller\_status\_info \- This module is enhanced to support iDRAC10\.
* idrac\_syslog \- This module is deprecated\.
* idrac\_user\_info \- This module is enhanced to support iDRAC10\.
* idrac\_virtual\_media \- This module is enhanced to support iDRAC10\.

<a id="minor-changes"></a>
### Minor Changes

<a id="cloud-common"></a>
#### cloud\.common

* plugins/module\_utils/turbo/server \- Update how the async loop is created to support python 3\.12\+ \([https\://github\.com/ansible\-collections/cloud\.common/pull/169](https\://github\.com/ansible\-collections/cloud\.common/pull/169)\)\.

<a id="cloudscale-ch-cloud"></a>
#### cloudscale\_ch\.cloud

* Add ansible\-core 2\.19\+ compatibility
* volume \- Add revert parameter\.

<a id="community-general"></a>
#### community\.general

* git\_config \- remove redundant <code>required\=False</code> from <code>argument\_spec</code> \([https\://github\.com/ansible\-collections/community\.general/pull/10177](https\://github\.com/ansible\-collections/community\.general/pull/10177)\)\.
* proxmox\_snap \- correctly handle proxmox\_snap timeout parameter \([https\://github\.com/ansible\-collections/community\.proxmox/issues/73](https\://github\.com/ansible\-collections/community\.proxmox/issues/73)\, [https\://github\.com/ansible\-collections/community\.proxmox/issues/95](https\://github\.com/ansible\-collections/community\.proxmox/issues/95)\, [https\://github\.com/ansible\-collections/community\.general/pull/10176](https\://github\.com/ansible\-collections/community\.general/pull/10176)\)\.

<a id="community-libvirt"></a>
#### community\.libvirt

* virt \- implement basic check mode functionality \([https\://github\.com/ansible\-collections/community\.libvirt/issue/98](https\://github\.com/ansible\-collections/community\.libvirt/issue/98)\)
* virt \- implement the gathering of Dom UUIDs as per FR [https\://github\.com/ansible\-collections/community\.libvirt/issues/187](https\://github\.com/ansible\-collections/community\.libvirt/issues/187)
* virt \- implement the gathering of Dom interface names and mac addresses as per FR [https\://github\.com/ansible\-collections/community\.libvirt/issues/189](https\://github\.com/ansible\-collections/community\.libvirt/issues/189)
* virt \- implement the removal of volumes for a dom as per FR [https\://github\.com/ansible\-collections/community\.libvirt/issues/177](https\://github\.com/ansible\-collections/community\.libvirt/issues/177)

<a id="community-mysql"></a>
#### community\.mysql

* mysql\_replication \- change default value for <code>primary\_ssl\_verify\_server\_cert</code> from False to None\. This should not affect existing playbooks \([https\://github\.com/ansible\-collections/community\.mysql/pull/707](https\://github\.com/ansible\-collections/community\.mysql/pull/707)\)\.

<a id="community-rabbitmq"></a>
#### community\.rabbitmq

* rabbitmq\_vhost \- add support to vhost manipulation through RabbitMQ API \([https\://github\.com/ansible\-collections/community\.rabbitmq/issues/171](https\://github\.com/ansible\-collections/community\.rabbitmq/issues/171)\)

<a id="community-routeros"></a>
#### community\.routeros

* api\_find\_and\_modify \- allow to control whether <code>dynamic</code> and/or <code>builtin</code> entries are ignored with the new <code>ignore\_dynamic</code> and <code>ignore\_builtin</code> options \([https\://github\.com/ansible\-collections/community\.routeros/issues/372](https\://github\.com/ansible\-collections/community\.routeros/issues/372)\, [https\://github\.com/ansible\-collections/community\.routeros/pull/373](https\://github\.com/ansible\-collections/community\.routeros/pull/373)\)\.
* api\_info\, api\_modify \- add <code>interface ethernet switch port\-isolation</code> which is supported since RouterOS 6\.43 \([https\://github\.com/ansible\-collections/community\.routeros/pull/375](https\://github\.com/ansible\-collections/community\.routeros/pull/375)\)\.
* api\_info\, api\_modify \- add <code>port\-cost\-mode</code> to <code>interface bridge</code> which is supported since RouterOS 7\.13 \([https\://github\.com/ansible\-collections/community\.routeros/pull/371](https\://github\.com/ansible\-collections/community\.routeros/pull/371)\)\.
* api\_info\, api\_modify \- add <code>routing bfd configuration</code>\. Officially stabilized BFD support for BGP and OSPF is available since RouterOS 7\.11
  \([https\://github\.com/ansible\-collections/community\.routeros/pull/375](https\://github\.com/ansible\-collections/community\.routeros/pull/375)\)\.
* api\_modify\, api\_info \- support API path <code>ip ipsec mode\-config</code> \([https\://github\.com/ansible\-collections/community\.routeros/pull/376](https\://github\.com/ansible\-collections/community\.routeros/pull/376)\)\.

<a id="community-sops"></a>
#### community\.sops

* Now supports specifying SSH private keys for age with the new <code>age\_ssh\_private\_keyfile</code> option \([https\://github\.com/ansible\-collections/community\.sops/pull/241](https\://github\.com/ansible\-collections/community\.sops/pull/241)\)\.

<a id="community-vmware"></a>
#### community\.vmware

* vcenter\_extension \- Stop using <code>connect\_to\_api</code> \([https\://github\.com/ansible\-collections/community\.vmware/pull/2372](https\://github\.com/ansible\-collections/community\.vmware/pull/2372)\)\.
* vmware\_guest\_cross\_vc\_clone \- Stop using <code>connect\_to\_api</code> \([https\://github\.com/ansible\-collections/community\.vmware/pull/2372](https\://github\.com/ansible\-collections/community\.vmware/pull/2372)\)\.
* vmware\_guest\_instant\_clone \- Stop using <code>connect\_to\_api</code> \([https\://github\.com/ansible\-collections/community\.vmware/pull/2372](https\://github\.com/ansible\-collections/community\.vmware/pull/2372)\)\.
* vmware\_vm\_inventory \- Stop using <code>connect\_to\_api</code> \([https\://github\.com/ansible\-collections/community\.vmware/pull/2372](https\://github\.com/ansible\-collections/community\.vmware/pull/2372)\)\.
* vmware\_vsan\_cluster \- Stop using <code>connect\_to\_api</code> \([https\://github\.com/ansible\-collections/community\.vmware/pull/2372](https\://github\.com/ansible\-collections/community\.vmware/pull/2372)\)\.

<a id="hitachivantara-vspone-block"></a>
#### hitachivantara\.vspone\_block

* Added additional parameters primary\_volume\_device\_group\_name and secondary\_volume\_device\_group\_name to retrieve ShadowImage group details more quickly\.
* Added new module <em class="title-reference">hv\_external\_parity\_group\_facts</em> to retrieve information about External Parity Group\.
* Added new module <em class="title-reference">hv\_external\_path\_group\_facts</em> to retrieve information about External Path Group\.
* Added new module <em class="title-reference">hv\_external\_path\_group</em> to manage External Path Groups\.
* Added new module <em class="title-reference">hv\_mp\_facts</em> to retrieve MP Blades information from VSP storage models\.
* Added support for begin\_secondary\_volume\_id and end\_secondary\_volume\_id to the remote replication modules \- hv\_gad\, hv\_hur\, hv\_truecopy\.
* Added support for cloning a Thin Image pair to the hv\_snapshot module\.
* Added support for cloning pairs in a specified snapshot group to the hv\_snapshot\_group module\.
* Added support for deleting an iSCSI name of an external storage system that is registered to a port on the local storage system to the hv\_storage\_port module\.
* Added support for deleting garbage data for all Thin Image pairs in a snapshot tree to the hv\_snapshot module\.
* Added support for disconnecting from a volume on the external storage system to the hv\_external\_volume module\.
* Added support for getting a list of LUs defined for a port on an external storage system to the hv\_storage\_port\_facts module\.
* Added support for getting a list of ports on an external storage system to the hv\_storage\_port\_facts module\.
* Added support for getting information about a specific LU path to the hv\_hostgroup\_facts module\.
* Added support for getting information about a specific LU path to the hv\_iscsi\_target\_facts module\.
* Added support for getting information about an iSCSI target of a port on an external storage system to the hv\_storage\_port\_facts module\.
* Added support for getting the iSCSI name of an external storage system that is registered to a port on the local storage system to the hv\_storage\_port\_facts module\.
* Added support for lun\_id for the secondary host group for TC and HUR\. For GAD\, lun\_id and enable\_preferred\_path are supported\.
* Added support for performing a login test on an iSCSI target of an external storage system that is registered to a port on the local storage system to the hv\_storage\_port module\.
* Added support for reclaiming the zero pages of a DP volume to the hv\_ldev module\.
* Added support for registering an iSCSI name of an external storage system to a port on the local storage system to the hv\_storage\_port module\.
* Added support for releasing the host reservation status by specifying a host group to the hv\_hostgroup module\.
* Added support for releasing the host reservation status by specifying an iSCSI target to the hv\_iscsi\_target module\.
* Added support for releasing the host reservation status by specifying the LU path to the hv\_hostgroup module\.
* Added support for releasing the host reservation status by specifying the LU path to the hv\_iscsi\_target module\.
* Added support for setting the nickname for a WWN to the hv\_hostgroup module\.
* Added support for setting the nickname for an iSCSI name to the hv\_iscsi\_target module\.
* Added support for setting the nickname of an IQN initiator to the hv\_iscsi\_target module\.
* Added the ability to change the settings of the following parameters of an LDEV using the hv\_ldev module \- data\_reduction\_process\_mode\, is\_compression\_acceleration\_enabled\, is\_relocation\_enabled\,is\_full\_allocation\_enabled\, is\_alua\_enabled
* Added the ability to format a volume to the hv\_ldev module\.
* Added the ability to set the nick\_name of an iSCSI using the hv\_iscsi\_target module\.
* Added the following new parameters to the output of hv\_ldev\_facts is\_compression\_acceleration\_enabled\, data\_reduction\_process\_mode\, is\_relocation\_enabled\, is\_full\_allocation\_enabled
* Added the following parameters to creating an LDEV using the hv\_ldev module is\_parallel\_execution\_enabled\, start\_ldev\_id\, end\_ldev\_id\, external\_parity\_group\, is\_compression\_acceleration\_enabled
* Enabled host group name together with port ID as identifiers for a host group\.
* Enabled the iSCSI target name together with the port ID as identifiers for the iSCSI target\.if both ID and name are specified\, the ID is used together with the port ID as the iSCSI target identifier\.

<a id="ibm-storage-virtualize"></a>
#### ibm\.storage\_virtualize

* ibm\_svc\_host\.py \- Added support for adding and removing preferred location\, and IO Groups
* ibm\_svc\_hostcluster\.py \- Added support for adding site
* ibm\_svc\_manage\_volume \- Added support for warning parameter

<a id="ovirt-ovirt"></a>
#### ovirt\.ovirt

* Enable and start postfix service so that ovirt\-ha\-agent logs are not filled with mail notification errors \([https\://github\.com/oVirt/ovirt\-ansible\-collection/pull/741](https\://github\.com/oVirt/ovirt\-ansible\-collection/pull/741)\)
* Maintenance tasks regarding linting\, testing and CI \([https\://github\.com/oVirt/ovirt\-ansible\-collection/pull/762](https\://github\.com/oVirt/ovirt\-ansible\-collection/pull/762)\)

<a id="telekom-mms-icinga-director"></a>
#### telekom\_mms\.icinga\_director

* Add API timeout option for all modules \([https\://github\.com/telekom\-mms/ansible\-collection\-icinga\-director/pull/282](https\://github\.com/telekom\-mms/ansible\-collection\-icinga\-director/pull/282)\)
* Add support for IcingaDB in inventory plugin \([https\://github\.com/telekom\-mms/ansible\-collection\-icinga\-director/pull/274](https\://github\.com/telekom\-mms/ansible\-collection\-icinga\-director/pull/274)\)
* Icinga dependency modules implementation \([https\://github\.com/telekom\-mms/ansible\-collection\-icinga\-director/pull/272](https\://github\.com/telekom\-mms/ansible\-collection\-icinga\-director/pull/272)\)

<a id="deprecated-features"></a>
### Deprecated Features

<a id="community-crypto"></a>
#### community\.crypto

* The Entrust service in currently being sunsetted after the sale of Entrust\'s Public Certificates Business to Sectigo\; see [the announcement with key dates](https\://www\.entrust\.com/tls\-certificate\-information\-center) and [the migration brief for customers](https\://www\.sectigo\.com/uploads/resources/EOL\_Migration\-Brief\-End\-Customer\.pdf) for details \([https\://github\.com/ansible\-collections/community\.crypto/issues/895](https\://github\.com/ansible\-collections/community\.crypto/issues/895)\, [https\://github\.com/ansible\-collections/community\.crypto/pull/901](https\://github\.com/ansible\-collections/community\.crypto/pull/901)\)\.
* ecs\_certificate \- the module will be removed from community\.crypto 3\.0\.0 \([https\://github\.com/ansible\-collections/community\.crypto/issues/895](https\://github\.com/ansible\-collections/community\.crypto/issues/895)\, [https\://github\.com/ansible\-collections/community\.crypto/pull/901](https\://github\.com/ansible\-collections/community\.crypto/pull/901)\)\.
* ecs\_domain \- the module will be removed from community\.crypto 3\.0\.0 \([https\://github\.com/ansible\-collections/community\.crypto/issues/895](https\://github\.com/ansible\-collections/community\.crypto/issues/895)\, [https\://github\.com/ansible\-collections/community\.crypto/pull/901](https\://github\.com/ansible\-collections/community\.crypto/pull/901)\)\.
* x509\_certificate \- the <code>entrust</code> provider will be removed from community\.crypto 3\.0\.0 \([https\://github\.com/ansible\-collections/community\.crypto/issues/895](https\://github\.com/ansible\-collections/community\.crypto/issues/895)\, [https\://github\.com/ansible\-collections/community\.crypto/pull/901](https\://github\.com/ansible\-collections/community\.crypto/pull/901)\)\.
* x509\_certificate\_pipe \- the <code>entrust</code> provider will be removed from community\.crypto 3\.0\.0 \([https\://github\.com/ansible\-collections/community\.crypto/issues/895](https\://github\.com/ansible\-collections/community\.crypto/issues/895)\, [https\://github\.com/ansible\-collections/community\.crypto/pull/901](https\://github\.com/ansible\-collections/community\.crypto/pull/901)\)\.

<a id="community-general-1"></a>
#### community\.general

* yaml callback plugin \- the YAML callback plugin was deprecated for removal in community\.general 13\.0\.0\. Since it needs to use ansible\-core internals since ansible\-core 2\.19 that are changing a lot\, we will remove this plugin already from community\.general 12\.0\.0 to ease the maintenance burden \([https\://github\.com/ansible\-collections/community\.general/pull/10213](https\://github\.com/ansible\-collections/community\.general/pull/10213)\)\.

<a id="community-vmware-1"></a>
#### community\.vmware

* module\_utils\.vmware \- Deprecate <code>connect\_to\_api</code> \([https\://github\.com/ansible\-collections/community\.vmware/pull/2372](https\://github\.com/ansible\-collections/community\.vmware/pull/2372)\)\.
* vmware\_guest\_powerstate \- the module has been deprecated and will be removed in community\.vmware 7\.0\.0 \([https\://github\.com/ansible\-collections/community\.vmware/pull/2398](https\://github\.com/ansible\-collections/community\.vmware/pull/2398)\)\.

<a id="bugfixes"></a>
### Bugfixes

<a id="check-point-mgmt"></a>
#### check\_point\.mgmt

* Added required management version to the documentation for all collection modules\.
* module\_utils/checkpoint \- Prevent redundant logout call when there is no authentication header \'X\-chkp\-sid\'\.

<a id="cisco-meraki"></a>
#### cisco\.meraki

* cisco\.meraki\.devices\_cellular\_sims \- fix idempotency error\.
* cisco\.meraki\.networks\_appliance\_firewall\_l7\_firewall\_rules \- fix idempotency error\.

<a id="cloudscale-ch-cloud-1"></a>
#### cloudscale\_ch\.cloud

* floating\_ip \- Fix sanity tests\.

<a id="community-crypto-1"></a>
#### community\.crypto

* acme\_account \- make work with CAs that do not accept any account request without External Account Binding data \([https\://github\.com/ansible\-collections/community\.crypto/issues/918](https\://github\.com/ansible\-collections/community\.crypto/issues/918)\, [https\://github\.com/ansible\-collections/community\.crypto/pull/919](https\://github\.com/ansible\-collections/community\.crypto/pull/919)\)\.

<a id="community-dns"></a>
#### community\.dns

* Update Public Suffix List\.
* lookup and lookup\_as\_dict lookup plugins \- removed type <code>ALL</code>\, which never worked \([https\://github\.com/ansible\-collections/community\.dns/issues/264](https\://github\.com/ansible\-collections/community\.dns/issues/264)\, [https\://github\.com/ansible\-collections/community\.dns/pull/265](https\://github\.com/ansible\-collections/community\.dns/pull/265)\)\.

<a id="community-docker"></a>
#### community\.docker

* docker\_compose\_v2 \- handle a \(potentially unintentional\) breaking change in Docker Compose 2\.37\.0\. Note that <code>ContainerName</code> is no longer part of the return value \([https\://github\.com/ansible\-collections/community\.docker/issues/1082](https\://github\.com/ansible\-collections/community\.docker/issues/1082)\, [https\://github\.com/ansible\-collections/community\.docker/pull/1083](https\://github\.com/ansible\-collections/community\.docker/pull/1083)\)\.
* docker\_container \- fix idempotency if <code>command\=\[\]</code> and <code>command\_handling\=correct</code> \([https\://github\.com/ansible\-collections/community\.docker/issues/1080](https\://github\.com/ansible\-collections/community\.docker/issues/1080)\, [https\://github\.com/ansible\-collections/community\.docker/pull/1085](https\://github\.com/ansible\-collections/community\.docker/pull/1085)\)\.

<a id="community-general-2"></a>
#### community\.general

* cobbler\_system \- update minimum version number to avoid wrong comparisons that happen in some cases using LooseVersion class which results in TypeError \([https\://github\.com/ansible\-collections/community\.general/issues/8506](https\://github\.com/ansible\-collections/community\.general/issues/8506)\, [https\://github\.com/ansible\-collections/community\.general/pull/10145](https\://github\.com/ansible\-collections/community\.general/pull/10145)\, [https\://github\.com/ansible\-collections/community\.general/pull/10178](https\://github\.com/ansible\-collections/community\.general/pull/10178)\)\.
* gitlab\_group\_access\_token\, gitlab\_project\_access\_token \- fix handling of group and project access tokens for changes in GitLab 17\.10 \([https\://github\.com/ansible\-collections/community\.general/pull/10196](https\://github\.com/ansible\-collections/community\.general/pull/10196)\)\.
* keycloak \- update more than 10 sub\-groups \([https\://github\.com/ansible\-collections/community\.general/issues/9690](https\://github\.com/ansible\-collections/community\.general/issues/9690)\, [https\://github\.com/ansible\-collections/community\.general/pull/9692](https\://github\.com/ansible\-collections/community\.general/pull/9692)\)\.
* yaml callback plugin \- adjust to latest changes in ansible\-core devel \([https\://github\.com/ansible\-collections/community\.general/pull/10212](https\://github\.com/ansible\-collections/community\.general/pull/10212)\)\.
* yaml callback plugin \- when using ansible\-core 2\.19\.0b2 or newer\, uses a new utility provided by ansible\-core\. This allows us to remove all hacks and vendored code that was part of the plugin for ansible\-core versions with Data Tagging so far \([https\://github\.com/ansible\-collections/community\.general/pull/10242](https\://github\.com/ansible\-collections/community\.general/pull/10242)\)\.
* zypper\_repository \- make compatible with Python 3\.12\+ \([https\://github\.com/ansible\-collections/community\.general/issues/10222](https\://github\.com/ansible\-collections/community\.general/issues/10222)\, [https\://github\.com/ansible\-collections/community\.general/pull/10223](https\://github\.com/ansible\-collections/community\.general/pull/10223)\)\.
* zypper\_repository \- use <code>metalink</code> attribute to identify repositories without <code>\<url/\></code> element \([https\://github\.com/ansible\-collections/community\.general/issues/10224](https\://github\.com/ansible\-collections/community\.general/issues/10224)\, [https\://github\.com/ansible\-collections/community\.general/pull/10225](https\://github\.com/ansible\-collections/community\.general/pull/10225)\)\.

<a id="community-hrobot"></a>
#### community\.hrobot

* storagebox \- make sure that changes of boolean parameters are sent correctly to the Robot service \([https\://github\.com/ansible\-collections/community\.hrobot/issues/160](https\://github\.com/ansible\-collections/community\.hrobot/issues/160)\, [https\://github\.com/ansible\-collections/community\.hrobot/pull/161](https\://github\.com/ansible\-collections/community\.hrobot/pull/161)\)\.

<a id="community-mysql-1"></a>
#### community\.mysql

* mysql\_info \- fix a crash \(ERROR 1141\, There is no such grant defined for user \'PUBLIC\' on host \'\%\'\) when using the <code>users\_info</code> filter with a PUBLIC role present in MariaDB 10\.11\+\. Do note that the fix doesn\'t change the fact that the module won\'t return the privileges from the PUBLIC role in the users privileges list\. It can\'t do that because you have to login as the particular user and use <em class="title-reference">SHOW GRANTS FOR CURRENT\_USER</em>\. We considered using an aggregation with the <em class="title-reference">SHOW GRANTS FOR PUBLIC</em> command\. However\, this approach would make copying users from one server to another transform the privileges inherited from the role as if they were direct privileges on the user\.
* mysql\_replication \- fixed an issue where setting <code>primary\_ssl\_verify\_server\_cert</code> to false had no effect \([https\://github\.com/ansible\-collections/community\.mysql/issues/689](https\://github\.com/ansible\-collections/community\.mysql/issues/689)\)\.

<a id="community-postgresql"></a>
#### community\.postgresql

* postgresql\_schema \- change reported in check\_mode was negated\. Now it reports a change when removing an existing schema \([https\://github\.com/ansible\-collections/community\.postgresql/pull/858](https\://github\.com/ansible\-collections/community\.postgresql/pull/858)\)

<a id="community-rabbitmq-1"></a>
#### community\.rabbitmq

* rabbitmq\_binding \- fix idempotency when arguments and/or routing\_key are given \([https\://github\.com/ansible\-collections/community\.rabbitmq/pull/191](https\://github\.com/ansible\-collections/community\.rabbitmq/pull/191)\)

<a id="community-vmware-2"></a>
#### community\.vmware

* vm\_device\_helper \- Fix an issue with ansible\-core 2\.19 \([https\://github\.com/ansible\-collections/community\.vmware/pull/2391](https\://github\.com/ansible\-collections/community\.vmware/pull/2391)\)\.
* vmware\_guest\_controller \- Fix an issue with ansible\-core 2\.19 \([https\://github\.com/ansible\-collections/community\.vmware/pull/2391](https\://github\.com/ansible\-collections/community\.vmware/pull/2391)\)\.
* vmware\_guest\_disk \- Fix an issue with ansible\-core 2\.19 \([https\://github\.com/ansible\-collections/community\.vmware/pull/2391](https\://github\.com/ansible\-collections/community\.vmware/pull/2391)\)\.
* vmware\_host\_inventory \- New option <code>enable\_backward\_compatability</code> that can be set to <code>false</code> to work with ansible\-core 2\.19 \([https\://github\.com/ansible\-collections/community\.vmware/pull/2391](https\://github\.com/ansible\-collections/community\.vmware/pull/2391)\)\.
* vmware\_target\_canonical\_info \- Fix an issue with ansible\-core 2\.19 \([https\://github\.com/ansible\-collections/community\.vmware/pull/2391](https\://github\.com/ansible\-collections/community\.vmware/pull/2391)\)\.
* vmware\_vm\_inventory \- New option <code>enable\_backward\_compatability</code> that can be set to <code>false</code> to work with ansible\-core 2\.19 \([https\://github\.com/ansible\-collections/community\.vmware/pull/2391](https\://github\.com/ansible\-collections/community\.vmware/pull/2391)\)\.

<a id="containers-podman"></a>
#### containers\.podman

* Document that sdnotify can be set to healthy
* Fix CI for podman\_image\_info
* Fix None values in LogOpt in Quadlet
* Fix conditions in CI jobs
* Fix idempotency for any podman secret driver
* Fix idempotency for systemd keyword
* Fix setuptools
* Handle image arguments in podman\_container
* Remove docker protocol when inspecting image
* Set custom tmpfs idempotency
* Use usedforsecurity for hashlib\.sha256 only in python version \>\=3\.9
* correctly quote labels and environment variables for quadlets
* doc \- podman\_secret \- fix indentation error in example
* fix\(podman\_image\) \- correct intendation on \'loop\' keyword

<a id="f5networks-f5-modules"></a>
#### f5networks\.f5\_modules

* bigip\_virtual\_server fix module crash issue

<a id="hitachivantara-vspone-block-1"></a>
#### hitachivantara\.vspone\_block

* Fixed output details of <em class="title-reference">host\_group\_number</em> and <em class="title-reference">host\_group\_id</em> in <em class="title-reference">hv\_hg</em> and \'hv\_hg\_facts\' modules to be consistent\.
* Fixed the mapping lun to multiple HostGroup/Iscsi Target issues for remote replication\.
* Resolved various documentation inconsistencies\.

<a id="ibm-storage-virtualize-1"></a>
#### ibm\.storage\_virtualize

* ibm\_svc\_ssh \- Added fix for nginx timeout
* ibm\_svc\_utils \- Added fix for nginx timeout

<a id="microsoft-ad"></a>
#### microsoft\.ad

* microsoft\.ad\.ldap \- Ensure the encrypted LAPS value is marked as unsafe to stop unexpected templating of the raw JSON result value \- [https\://github\.com/ansible\-collections/microsoft\.ad/issues/194](https\://github\.com/ansible\-collections/microsoft\.ad/issues/194)

<a id="ovirt-ovirt-1"></a>
#### ovirt\.ovirt

* ovirt\_disk \- fix documentation for lun\_id parameter \([https\://github\.com/oVirt/ovirt\-ansible\-collection/pull/740](https\://github\.com/oVirt/ovirt\-ansible\-collection/pull/740)\)
* ovirt\_proxied\_check \- fix documentation string \([https\://github\.com/oVirt/ovirt\-ansible\-collection/pull/761](https\://github\.com/oVirt/ovirt\-ansible\-collection/pull/761)\)
* roles \- Fix ansible\-test errors change include to include\_tasks \([https\://github\.com/oVirt/ovirt\-ansible\-collection/pull/733](https\://github\.com/oVirt/ovirt\-ansible\-collection/pull/733)\)\.

<a id="telekom-mms-icinga-director-1"></a>
#### telekom\_mms\.icinga\_director

* Bug\: dependency apply module raises error when using a variable for parent host or service \([https\://github\.com/telekom\-mms/ansible\-collection\-icinga\-director/pull/276](https\://github\.com/telekom\-mms/ansible\-collection\-icinga\-director/pull/276)\)
* Extend checks in diff as a workaround for type confusion with the Director API \([https\://github\.com/telekom\-mms/ansible\-collection\-icinga\-director/pull/278](https\://github\.com/telekom\-mms/ansible\-collection\-icinga\-director/pull/278)\)
* add \'groups\' parameter to task \'icinga\_user\.yml\' \([https\://github\.com/telekom\-mms/ansible\-collection\-icinga\-director/pull/284](https\://github\.com/telekom\-mms/ansible\-collection\-icinga\-director/pull/284)\)

<a id="known-issues"></a>
### Known Issues

<a id="dellemc-openmanage-1"></a>
#### dellemc\.openmanage

* idrac\_diagnostics \- Issue\(285322\) \- This module doesn\'t support export of diagnostics file to HTTP and HTTPS share via SOCKS proxy\.
* idrac\_firmware \- Issue\(279282\) \- This module does not support firmware update using HTTP\, HTTPS\, and FTP shares with authentication on iDRAC8\.
* ome\_smart\_fabric\_uplink \- Issue\(186024\) \- The module supported by OpenManage Enterprise Modular\, however it does not allow the creation of multiple uplinks of the same name\. If an uplink is created using the same name as an existing uplink\, then the existing uplink is modified\.

<a id="new-modules"></a>
### New Modules

<a id="cloudscale-ch-cloud-2"></a>
#### cloudscale\_ch\.cloud

* cloudscale\_ch\.cloud\.volume\_snapshot \- Manage volume snapshots on the cloudscale\.ch IaaS service

<a id="community-hrobot-1"></a>
#### community\.hrobot

* community\.hrobot\.storagebox\_snapshot\_info \- Query the snapshots for a storage box\.
* community\.hrobot\.storagebox\_subaccount \- Create\, update\, or delete a subaccount for a storage box\.
* community\.hrobot\.storagebox\_subaccount\_info \- Query the subaccounts for a storage box\.

<a id="community-libvirt-1"></a>
#### community\.libvirt

* community\.libvirt\.virt\_volume \- Manage libvirt volumes inside a storage pool

<a id="hitachivantara-vspone-block-2"></a>
#### hitachivantara\.vspone\_block

<a id="vsp"></a>
##### Vsp

* hitachivantara\.vspone\_block\.hv\_external\_parity\_group\_facts \- Retrieves information about External Parity Group from Hitachi VSP storage systems\.
* hitachivantara\.vspone\_block\.hv\_external\_path\_group \- Manages External Path Groups in the Hitachi VSP storage systems\.
* hitachivantara\.vspone\_block\.hv\_external\_path\_group\_facts \- Retrieves information about External Path Group from Hitachi VSP storage systems\.
* hitachivantara\.vspone\_block\.hv\_mp\_facts \- Retrieves MP blades information from Hitachi VSP storage systems\.

<a id="telekom-mms-icinga-director-2"></a>
#### telekom\_mms\.icinga\_director

* telekom\_mms\.icinga\_director\.icinga\_dependency\_apply \- Manage dependency apply rules in Icinga2

<a id="unchanged-collections"></a>
### Unchanged Collections

* amazon\.aws \(still version 9\.5\.0\)
* ansible\.netcommon \(still version 7\.2\.0\)
* ansible\.posix \(still version 1\.6\.2\)
* ansible\.utils \(still version 5\.1\.2\)
* ansible\.windows \(still version 2\.8\.0\)
* arista\.eos \(still version 10\.1\.1\)
* awx\.awx \(still version 24\.6\.1\)
* chocolatey\.chocolatey \(still version 1\.5\.3\)
* cisco\.aci \(still version 2\.11\.0\)
* cisco\.asa \(still version 6\.1\.0\)
* cisco\.dnac \(still version 6\.31\.3\)
* cisco\.intersight \(still version 2\.1\.0\)
* cisco\.ios \(still version 9\.2\.0\)
* cisco\.iosxr \(still version 10\.3\.1\)
* cisco\.ise \(still version 2\.10\.0\)
* cisco\.mso \(still version 2\.10\.0\)
* cisco\.nxos \(still version 9\.4\.0\)
* cisco\.ucs \(still version 1\.16\.0\)
* community\.aws \(still version 9\.3\.0\)
* community\.ciscosmb \(still version 1\.0\.10\)
* community\.digitalocean \(still version 1\.27\.0\)
* community\.grafana \(still version 2\.2\.0\)
* community\.hashi\_vault \(still version 6\.2\.0\)
* community\.library\_inventory\_filtering\_v1 \(still version 1\.1\.1\)
* community\.network \(still version 5\.1\.0\)
* community\.proxysql \(still version 1\.6\.0\)
* community\.sap\_libs \(still version 1\.4\.2\)
* community\.windows \(still version 2\.4\.0\)
* community\.zabbix \(still version 3\.3\.0\)
* cyberark\.conjur \(still version 1\.3\.3\)
* cyberark\.pas \(still version 1\.0\.35\)
* dellemc\.enterprise\_sonic \(still version 2\.5\.1\)
* dellemc\.powerflex \(still version 2\.6\.0\)
* dellemc\.unity \(still version 2\.0\.0\)
* fortinet\.fortimanager \(still version 2\.9\.1\)
* fortinet\.fortios \(still version 2\.4\.0\)
* google\.cloud \(still version 1\.5\.3\)
* grafana\.grafana \(still version 5\.7\.0\)
* hetzner\.hcloud \(still version 4\.3\.0\)
* ibm\.qradar \(still version 4\.0\.0\)
* ibm\.spectrum\_virtualize \(still version 2\.0\.0\)
* ieisystem\.inmanage \(still version 3\.0\.0\)
* infinidat\.infinibox \(still version 1\.4\.5\)
* infoblox\.nios\_modules \(still version 1\.8\.0\)
* inspur\.ispim \(still version 2\.2\.3\)
* junipernetworks\.junos \(still version 9\.1\.0\)
* kaytus\.ksmanage \(still version 2\.0\.0\)
* kubernetes\.core \(still version 5\.3\.0\)
* lowlydba\.sqlserver \(still version 2\.6\.1\)
* microsoft\.iis \(still version 1\.0\.2\)
* netapp\.cloudmanager \(still version 21\.24\.0\)
* netapp\.ontap \(still version 22\.14\.0\)
* netapp\.storagegrid \(still version 21\.14\.0\)
* netapp\_eseries\.santricity \(still version 1\.4\.1\)
* netbox\.netbox \(still version 3\.21\.0\)
* ngine\_io\.cloudstack \(still version 2\.5\.0\)
* openstack\.cloud \(still version 2\.4\.1\)
* purestorage\.flasharray \(still version 1\.34\.1\)
* purestorage\.flashblade \(still version 1\.20\.0\)
* sensu\.sensu\_go \(still version 1\.14\.0\)
* splunk\.es \(still version 4\.0\.0\)
* theforeman\.foreman \(still version 4\.2\.0\)
* vmware\.vmware \(still version 1\.11\.0\)
* vmware\.vmware\_rest \(still version 4\.7\.0\)
* vultr\.cloud \(still version 1\.13\.0\)
* vyos\.vyos \(still version 5\.0\.0\)
* wti\.remote \(still version 1\.0\.10\)

<a id="v11-6-0"></a>
## v11\.6\.0

- <a href="#release-summary-1">Release Summary</a>
- <a href="#ansible-core-1">Ansible\-core</a>
- <a href="#changed-collections-1">Changed Collections</a>
- <a href="#major-changes-1">Major Changes</a>
    - <a href="#dellemc-openmanage-2">dellemc\.openmanage</a>
- <a href="#minor-changes-1">Minor Changes</a>
    - <a href="#ansible-core-2">Ansible\-core</a>
    - <a href="#amazon-aws">amazon\.aws</a>
    - <a href="#cisco-meraki-1">cisco\.meraki</a>
    - <a href="#cloud-common-1">cloud\.common</a>
    - <a href="#community-aws">community\.aws</a>
    - <a href="#community-docker-1">community\.docker</a>
    - <a href="#community-general-3">community\.general</a>
    - <a href="#community-grafana">community\.grafana</a>
    - <a href="#hitachivantara-vspone-block-3">hitachivantara\.vspone\_block</a>
    - <a href="#kubernetes-core">kubernetes\.core</a>
    - <a href="#lowlydba-sqlserver">lowlydba\.sqlserver</a>
    - <a href="#microsoft-ad-1">microsoft\.ad</a>
    - <a href="#purestorage-flashblade">purestorage\.flashblade</a>
- <a href="#deprecated-features-1">Deprecated Features</a>
    - <a href="#community-general-4">community\.general</a>
- <a href="#bugfixes-1">Bugfixes</a>
    - <a href="#ansible-core-3">Ansible\-core</a>
    - <a href="#amazon-aws-1">amazon\.aws</a>
    - <a href="#cisco-meraki-2">cisco\.meraki</a>
    - <a href="#community-crypto-2">community\.crypto</a>
    - <a href="#community-dns-1">community\.dns</a>
    - <a href="#community-general-5">community\.general</a>
    - <a href="#community-grafana-1">community\.grafana</a>
    - <a href="#community-postgresql-1">community\.postgresql</a>
    - <a href="#dellemc-openmanage-3">dellemc\.openmanage</a>
    - <a href="#google-cloud">google\.cloud</a>
    - <a href="#kubernetes-core-1">kubernetes\.core</a>
    - <a href="#microsoft-ad-2">microsoft\.ad</a>
    - <a href="#purestorage-flashblade-1">purestorage\.flashblade</a>
- <a href="#known-issues-1">Known Issues</a>
    - <a href="#dellemc-openmanage-4">dellemc\.openmanage</a>
- <a href="#new-plugins">New Plugins</a>
    - <a href="#callback">Callback</a>
    - <a href="#filter">Filter</a>
- <a href="#new-modules-1">New Modules</a>
    - <a href="#community-general-6">community\.general</a>
    - <a href="#community-hrobot-2">community\.hrobot</a>
    - <a href="#hitachivantara-vspone-block-4">hitachivantara\.vspone\_block</a>
    - <a href="#purestorage-flashblade-2">purestorage\.flashblade</a>
- <a href="#unchanged-collections-1">Unchanged Collections</a>

<a id="release-summary-1"></a>
### Release Summary

Release Date\: 2025\-05\-20

[Porting Guide](https\://docs\.ansible\.com/ansible/devel/porting\_guides\.html)

<a id="ansible-core-1"></a>
### Ansible\-core

Ansible 11\.6\.0 contains ansible\-core version 2\.18\.6\.
This is a newer version than version 2\.18\.5 contained in the previous Ansible release\.

The changes are reported in the combined changelog below\.

<a id="changed-collections-1"></a>
### Changed Collections

If not mentioned explicitly\, the changes are reported in the combined changelog below\.

| Collection                  | Ansible 11.5.0 | Ansible 11.6.0 | Notes                                                                                                                        |
| --------------------------- | -------------- | -------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| amazon.aws                  | 9.4.0          | 9.5.0          |                                                                                                                              |
| cisco.intersight            | 2.0.20         | 2.1.0          | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
| cisco.meraki                | 2.20.10        | 2.21.1         |                                                                                                                              |
| cloud.common                | 4.0.0          | 4.1.0          |                                                                                                                              |
| community.aws               | 9.2.0          | 9.3.0          |                                                                                                                              |
| community.crypto            | 2.26.0         | 2.26.1         |                                                                                                                              |
| community.dns               | 3.2.3          | 3.2.4          |                                                                                                                              |
| community.docker            | 4.5.2          | 4.6.0          |                                                                                                                              |
| community.general           | 10.6.0         | 10.7.0         |                                                                                                                              |
| community.grafana           | 2.1.0          | 2.2.0          |                                                                                                                              |
| community.hrobot            | 2.2.0          | 2.3.0          |                                                                                                                              |
| community.postgresql        | 3.14.0         | 3.14.1         |                                                                                                                              |
| cyberark.pas                | 1.0.30         | 1.0.35         | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
| dellemc.openmanage          | 9.11.0         | 9.12.0         |                                                                                                                              |
| google.cloud                | 1.5.1          | 1.5.3          |                                                                                                                              |
| hitachivantara.vspone_block | 3.3.0          | 3.4.1          |                                                                                                                              |
| kubernetes.core             | 5.2.0          | 5.3.0          |                                                                                                                              |
| kubevirt.core               | 2.1.0          | 2.2.2          | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
| lowlydba.sqlserver          | 2.6.0          | 2.6.1          |                                                                                                                              |
| microsoft.ad                | 1.8.1          | 1.9.0          |                                                                                                                              |
| purestorage.flashblade      | 1.19.2         | 1.20.0         |                                                                                                                              |

<a id="major-changes-1"></a>
### Major Changes

<a id="dellemc-openmanage-2"></a>
#### dellemc\.openmanage

* idrac\_gather\_facts \- This role is enhanced to support iDRAC10\.
* idrac\_lifecycle\_controller\_job\_status\_info \- This module is enhanced to support iDRAC10\.
* idrac\_system\_info \- This module is enhanced to support iDRAC10\.

<a id="minor-changes-1"></a>
### Minor Changes

<a id="ansible-core-2"></a>
#### Ansible\-core

* ansible\-test \- Use the <code>\-t</code> option to set the stop timeout when stopping a container\. This avoids use of the <code>\-\-time</code> option which was deprecated in Docker v28\.0\.

<a id="amazon-aws"></a>
#### amazon\.aws

* Bump version of ansible\-lint to 25\.1\.2 \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2590](https\://github\.com/ansible\-collections/amazon\.aws/pull/2590)\)\.
* iam\_user\_info \- Add tags to ListUsers or GetGroup results \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2567](https\://github\.com/ansible\-collections/amazon\.aws/pull/2567)\)\.
* iam\_user\_info \- Return empty user list when invalid group name is provided instead of python error \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2567](https\://github\.com/ansible\-collections/amazon\.aws/pull/2567)\)\.
* module\_utils/modules\.py \- call to <code>deprecate\(\)</code> without specifying <code>collection\_name</code>\, <code>version</code> or <code>date</code> arguments raises a sanity errors \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2607](https\://github\.com/ansible\-collections/amazon\.aws/pull/2607)\)\.

<a id="cisco-meraki-1"></a>
#### cisco\.meraki

* plugins/action/devices\_sensor\_commands \- new plugin\.
* plugins/action/devices\_sensor\_commands\_info \- new plugin\.
* plugins/action/networks\_appliance\_firewall\_multicast\_forwarding \- new plugin\.
* plugins/action/organizations\_appliance\_dns\_local\_profiles \- new plugin\.
* plugins/action/organizations\_appliance\_dns\_local\_profiles\_assignments\_bulk\_create \- new plugin\.
* plugins/action/organizations\_appliance\_dns\_local\_profiles\_assignments\_bulk\_delete \- new plugin\.
* plugins/action/organizations\_appliance\_dns\_local\_profiles\_assignments\_info \- new plugin\.
* plugins/action/organizations\_appliance\_dns\_local\_profiles\_info \- new plugin\.
* plugins/action/organizations\_appliance\_dns\_local\_records \- new plugin\.
* plugins/action/organizations\_appliance\_dns\_local\_records\_info \- new plugin\.
* plugins/action/organizations\_appliance\_dns\_split\_profiles \- new plugin\.
* plugins/action/organizations\_appliance\_dns\_split\_profiles\_assignments\_bulk\_create \- new plugin\.
* plugins/action/organizations\_appliance\_dns\_split\_profiles\_assignments\_bulk\_delete \- new plugin\.
* plugins/action/organizations\_appliance\_dns\_split\_profiles\_assignments\_info \- new plugin\.
* plugins/action/organizations\_appliance\_dns\_split\_profiles\_info \- new plugin\.
* plugins/action/organizations\_appliance\_firewall\_multicast\_forwarding\_by\_network\_info \- new plugin\.
* plugins/action/organizations\_devices\_controller\_migrations \- new plugin\.
* plugins/action/organizations\_devices\_controller\_migrations\_info \- new plugin\.
* plugins/action/organizations\_devices\_system\_memory\_usage\_history\_by\_interval\_info \- new plugin\.
* plugins/action/organizations\_integrations\_xdr\_networks\_disable \- new plugin\.
* plugins/action/organizations\_integrations\_xdr\_networks\_enable \- new plugin\.
* plugins/action/organizations\_integrations\_xdr\_networks\_info \- new plugin\.
* plugins/action/organizations\_switch\_ports\_usage\_history\_by\_device\_by\_interval\_info \- new plugin\.
* plugins/action/organizations\_wireless\_devices\_power\_mode\_history\_info \- new plugin\.
* plugins/action/organizations\_wireless\_devices\_system\_cpu\_load\_history\_info \- new plugin\.
* plugins/action/organizations\_wireless\_ssids\_firewall\_isolation\_allowlist\_entries \- new plugin\.
* plugins/action/organizations\_wireless\_ssids\_firewall\_isolation\_allowlist\_entries\_info \- new plugin\.

<a id="cloud-common-1"></a>
#### cloud\.common

* Bump version of ansible\-lint to minimum 25\.1\.2
* module\_utils/turbo/module \- Add support for 2\.19 by returning a json compatible arg obj instead of a dict if possible \([https\://github\.com/ansible\-collections/cloud\.common/pull/167](https\://github\.com/ansible\-collections/cloud\.common/pull/167)\)\.
* module\_utils/turbo/server \- Add support for 2\.19 by making FakeStdin implement the IOBase ABC \([https\://github\.com/ansible\-collections/cloud\.common/pull/167](https\://github\.com/ansible\-collections/cloud\.common/pull/167)\)\.

<a id="community-aws"></a>
#### community\.aws

* Bump version of ansible\-lint to 25\.1\.2\.
* aws\_ssm \- Move the <code>aws\_ssm</code> connection plugin\'s plugin\_utils into a dedicated folder \([https\://github\.com/ansible\-collections/community\.aws/pull/2279](https\://github\.com/ansible\-collections/community\.aws/pull/2279)\)\.
* aws\_ssm \- Refactor S3 operations methods for improved clarity \([https\://github\.com/ansible\-collections/community\.aws/pull/2275](https\://github\.com/ansible\-collections/community\.aws/pull/2275)\)\.
* aws\_ssm \- Refactor connection/aws\_ssm to add new TerminalManager class and move relevant methods to the new class \([https\://github\.com/ansible\-collections/community\.aws/pull/2270](https\://github\.com/ansible\-collections/community\.aws/pull/2270)\)\.
* aws\_ssm \- Refactor connection/aws\_ssm to add new <code>FileTransferManager</code> class and move relevant methods to the new class \([https\://github\.com/ansible\-collections/community\.aws/pull/2273](https\://github\.com/ansible\-collections/community\.aws/pull/2273)\)\.
* aws\_ssm \- Refactor connection/aws\_ssm to add new <code>SSMSessionManager</code> and <code>ProcessManager</code> classes and move relevant methods to the new class \([https\://github\.com/ansible\-collections/community\.aws/pull/2272](https\://github\.com/ansible\-collections/community\.aws/pull/2272)\)\.

<a id="community-docker-1"></a>
#### community\.docker

* docker\_container\_copy\_into \- add <code>mode\_parse</code> parameter which determines how <code>mode</code> is parsed \([https\://github\.com/ansible\-collections/community\.docker/pull/1074](https\://github\.com/ansible\-collections/community\.docker/pull/1074)\)\.

<a id="community-general-3"></a>
#### community\.general

* cobbler inventory plugin \- add <code>connection\_timeout</code> option to specify the connection timeout to the cobbler server \([https\://github\.com/ansible\-collections/community\.general/pull/11063](https\://github\.com/ansible\-collections/community\.general/pull/11063)\)\.
* cobbler inventory plugin \- add <code>facts\_level</code> option to allow requesting fully rendered variables for Cobbler systems \([https\://github\.com/ansible\-collections/community\.general/issues/9419](https\://github\.com/ansible\-collections/community\.general/issues/9419)\, [https\://github\.com/ansible\-collections/community\.general/pull/9975](https\://github\.com/ansible\-collections/community\.general/pull/9975)\)\.
* ini\_file \- modify an inactive option also when there are spaces in front of the comment symbol \([https\://github\.com/ansible\-collections/community\.general/pull/10102](https\://github\.com/ansible\-collections/community\.general/pull/10102)\, [https\://github\.com/ansible\-collections/community\.general/issues/8539](https\://github\.com/ansible\-collections/community\.general/issues/8539)\)\.
* pipx \- parameter <code>name</code> now accepts Python package specifiers \([https\://github\.com/ansible\-collections/community\.general/issues/7815](https\://github\.com/ansible\-collections/community\.general/issues/7815)\, [https\://github\.com/ansible\-collections/community\.general/pull/10031](https\://github\.com/ansible\-collections/community\.general/pull/10031)\)\.
* pipx module\_utils \- filtering application list by name now happens in the modules \([https\://github\.com/ansible\-collections/community\.general/pull/10031](https\://github\.com/ansible\-collections/community\.general/pull/10031)\)\.
* pipx\_info \- filtering application list by name now happens in the module  \([https\://github\.com/ansible\-collections/community\.general/pull/10031](https\://github\.com/ansible\-collections/community\.general/pull/10031)\)\.

<a id="community-grafana"></a>
#### community\.grafana

* Add argument <em class="title-reference">tls\_servername</em> for <em class="title-reference">grafana\_datasource</em>
* Support <em class="title-reference">alertmanager</em> as type for <em class="title-reference">grafana\_datasource</em>
* grafana\_dashboard \- allow creating dashboards in subfolders

<a id="hitachivantara-vspone-block-3"></a>
#### hitachivantara\.vspone\_block

* Added back \'mu\_number\' parameter to the <em class="title-reference">hv\_gad</em> module\.
* Added iSCSI target support for GAD\, TrueCopy\, HUR\, ShadowImage\, and Snapshot/ThinImage modules\.
* Added new module <em class="title-reference">hv\_ddp\_pool\_facts</em> to retrieve DDP\-based pool details on VSP One Block storage models\.
* Added new module <em class="title-reference">hv\_ddp\_pool</em> to create\, update\, and delete DDP\-based pools on VSP One Block storage models\.
* Added support to delete SVOL post\-pair deletion for GAD\, TrueCopy\, HUR\, ShadowImage\, and Snapshot/ThinImage modules\.
* Enhanced <em class="title-reference">hv\_ldev\_facts</em> module to support query parameters\.
* Enhanced <em class="title-reference">hv\_shadow\_image</em> module\: support for local copy group and copy pair name for shadow image pair management\; group management of shadow image pairs\.
* Enhanced <em class="title-reference">hv\_snapshot\_group</em> module to support retention period\.
* Enhanced <em class="title-reference">hv\_snapshot</em> module\: added copy speed\, clones automation\, retention period\, support for Floating Snapshot\, and pair creation with specific or auto\-selected SVOL and mirror unit\.
* Enhanced <em class="title-reference">hv\_storage\_port</em> module to support attributes like connection\, speed\, and type\.
* Removed gateway connection type from all the modules\.
* Resolved various documentation inconsistencies\.

<a id="kubernetes-core"></a>
#### kubernetes\.core

* Bump version of ansible\-lint to 25\.1\.2 \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/919](https\://github\.com/ansible\-collections/kubernetes\.core/pull/919)\)\.
* action/k8s\_info \- update templating mechanism with changes from <code>ansible\-core 2\.19</code> \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/888](https\://github\.com/ansible\-collections/kubernetes\.core/pull/888)\)\.
* helm \- add reset\_then\_reuse\_values support to helm module \([https\://github\.com/ansible\-collections/kubernetes\.core/issues/803](https\://github\.com/ansible\-collections/kubernetes\.core/issues/803)\)\.
* helm \- add support for <code>insecure\_skip\_tls\_verify</code> option to helm and helm\_repository\([https\://github\.com/ansible\-collections/kubernetes\.core/issues/694](https\://github\.com/ansible\-collections/kubernetes\.core/issues/694)\)\.

<a id="lowlydba-sqlserver"></a>
#### lowlydba\.sqlserver

* Added support for Ansible 2\.19
* Updated the test matrix to include Ansible 2\.19 and remove Ansible 2\.16

<a id="microsoft-ad-1"></a>
#### microsoft\.ad

* Set minimum supported Ansible version to 2\.16 to align with the versions still supported by Ansible\.

<a id="purestorage-flashblade"></a>
#### purestorage\.flashblade

* purefb\_ad \- Add support for Global Catalog Servers
* purefb\_dns \- Added support for multiple DNS configurations\.
* purefb\_ds \- SMB directory services deprecated from Purity//FB 4\.5\.2
* purefb\_info \- Add support for Active Directory Global Catalog Servers
* purefb\_info \- Added snapshot creation date\-time and time\_remaining\, if snapshot is not deleted\, to the <code>snapshots</code> response\.
* purefb\_info \- Added support for multiple DNS configurations\.
* purefb\_policy \- Snapshot policies can now have specific filesystems and/or replica links added or deletred from the policy
* purefb\_proxy \- Added support to update existing proxy
* purefb\_proxy \- Updated to REST v2
* purefb\_s3user \- Changed <code>key\_state</code> state to be <code>keystate</code> as <code>key\_state</code> is reserved\.
* purefb\_s3user \- Changed <code>remove\_key</code> parameter to <code>key\_name</code> and add new <code>state</code> of <code>key\_state</code> to allow a specificed key to be enabled/disabled using the new parameter <code>enable\_key</code>\.
* purefb\_s3user \- Updated failure messages for applying policies to an object user account\.
* purefb\_subnet \- <code>prefix</code> removed as a required parameter for updating an existing subnet

<a id="deprecated-features-1"></a>
### Deprecated Features

<a id="community-general-4"></a>
#### community\.general

* The proxmox content \(modules and plugins\) is being moved to the [new collection community\.proxmox](https\://github\.com/ansible\-collections/community\.proxmox)\. In community\.general 11\.0\.0\, these modules and plugins will be replaced by deprecated redirections to community\.proxmox\. You need to explicitly install community\.proxmox\, for example with <code>ansible\-galaxy collection install community\.proxmox</code>\. We suggest to update your roles and playbooks to use the new FQCNs as soon as possible to avoid getting deprecation messages \([https\://github\.com/ansible\-collections/community\.general/pull/10109](https\://github\.com/ansible\-collections/community\.general/pull/10109)\)\.
* pipx module\_utils \- function <code>make\_process\_list\(\)</code> is deprecated and will be removed in community\.general 13\.0\.0 \([https\://github\.com/ansible\-collections/community\.general/pull/10031](https\://github\.com/ansible\-collections/community\.general/pull/10031)\)\.

<a id="bugfixes-1"></a>
### Bugfixes

<a id="ansible-core-3"></a>
#### Ansible\-core

* Ansible will now ensure predictable permissions on remote artifacts\, until now it only ensured executable and relied on system masks for the rest\.
* ansible\-doc \- fix indentation for first line of descriptions of suboptions and sub\-return values \([https\://github\.com/ansible/ansible/pull/84690](https\://github\.com/ansible/ansible/pull/84690)\)\.
* ansible\-doc \- fix line wrapping for first line of description of options and return values \([https\://github\.com/ansible/ansible/pull/84690](https\://github\.com/ansible/ansible/pull/84690)\)\.
* dnf5 \- avoid generating excessive transaction entries in the dnf5 history \([https\://github\.com/ansible/ansible/issues/85046](https\://github\.com/ansible/ansible/issues/85046)\)
* dnf5 \- when <code>bugfix</code> and/or <code>security</code> is specified\, skip packages that do not have any such updates\, even for new versions of libdnf5 where this functionality changed and it is considered failure
* script \- Fix up become support for Windows scripts when become was set through host variables and not on the task directly \- [https\://github\.com/ansible/ansible/issues/85076](https\://github\.com/ansible/ansible/issues/85076)

<a id="amazon-aws-1"></a>
#### amazon\.aws

* iam\_user\_info \- Actually call GetUser when only user name is supplied instead of listing and filtering from all users \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2567](https\://github\.com/ansible\-collections/amazon\.aws/pull/2567)\)\.
* iam\_user\_info \- Actually filter users by path prefix when one is provided \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2567](https\://github\.com/ansible\-collections/amazon\.aws/pull/2567)\)\.
* route53\_info \- removes jijna delimiters from example using when \([https\://github\.com/ansible\-collections/amazon\.aws/issues/2594](https\://github\.com/ansible\-collections/amazon\.aws/issues/2594)\)\.

<a id="cisco-meraki-2"></a>
#### cisco\.meraki

* cisco\.meraki\.devices\_switch\_ports \- fix get\_object\_by\_name method\.

<a id="community-crypto-2"></a>
#### community\.crypto

* luks\_device \- mark parameter <code>passphrase\_encoding</code> as <code>no\_log\=False</code> to avoid confusing warning \([https\://github\.com/ansible\-collections/community\.crypto/pull/867](https\://github\.com/ansible\-collections/community\.crypto/pull/867)\)\.
* luks\_device \- removing a specific keyslot with <code>remove\_keyslot</code> caused the module to hang while cryptsetup was waiting for a passphrase from stdin\, while the module did not supply one\. Since a keyslot is not necessary\, do not provide one \([https\://github\.com/ansible\-collections/community\.crypto/issues/864](https\://github\.com/ansible\-collections/community\.crypto/issues/864)\, [https\://github\.com/ansible\-collections/community\.crypto/pull/868](https\://github\.com/ansible\-collections/community\.crypto/pull/868)\)\.

<a id="community-dns-1"></a>
#### community\.dns

* Update Public Suffix List\.

<a id="community-general-5"></a>
#### community\.general

* cobbler\_system \- fix bug with Cobbler \>\= 3\.4\.0 caused by giving more than 2 positional arguments to <code>CobblerXMLRPCInterface\.get\_system\_handle\(\)</code> \([https\://github\.com/ansible\-collections/community\.general/issues/8506](https\://github\.com/ansible\-collections/community\.general/issues/8506)\, [https\://github\.com/ansible\-collections/community\.general/pull/10145](https\://github\.com/ansible\-collections/community\.general/pull/10145)\)\.
* kdeconfig \- allow option values beginning with a dash \([https\://github\.com/ansible\-collections/community\.general/issues/10127](https\://github\.com/ansible\-collections/community\.general/issues/10127)\, [https\://github\.com/ansible\-collections/community\.general/pull/10128](https\://github\.com/ansible\-collections/community\.general/pull/10128)\)\.
* keycloak\_user\_rolemapping \- fix <code>\-\-diff</code> mode \([https\://github\.com/ansible\-collections/community\.general/issues/10067](https\://github\.com/ansible\-collections/community\.general/issues/10067)\, [https\://github\.com/ansible\-collections/community\.general/pull/10075](https\://github\.com/ansible\-collections/community\.general/pull/10075)\)\.
* pickle cache plugin \- avoid extra JSON serialization with ansible\-core \>\= 2\.19 \([https\://github\.com/ansible\-collections/community\.general/pull/10136](https\://github\.com/ansible\-collections/community\.general/pull/10136)\)\.
* proxmox \- fix crash in module when the used on an existing LXC container with <code>state\=present</code> and <code>force\=true</code> \([https\://github\.com/ansible\-collections/community\.proxmox/pull/91](https\://github\.com/ansible\-collections/community\.proxmox/pull/91)\, [https\://github\.com/ansible\-collections/community\.general/pull/10155](https\://github\.com/ansible\-collections/community\.general/pull/10155)\)\.
* rundeck\_acl\_policy \- ensure that project ACLs are sent to the correct endpoint \([https\://github\.com/ansible\-collections/community\.general/pull/10097](https\://github\.com/ansible\-collections/community\.general/pull/10097)\)\.
* sysrc \- split the output of <code>sysrc \-e \-a</code> on the first <code>\=</code> only \([https\://github\.com/ansible\-collections/community\.general/issues/10120](https\://github\.com/ansible\-collections/community\.general/issues/10120)\, [https\://github\.com/ansible\-collections/community\.general/pull/10121](https\://github\.com/ansible\-collections/community\.general/pull/10121)\)\.

<a id="community-grafana-1"></a>
#### community\.grafana

* Remove field <em class="title-reference">apiVersion</em> from return of current <em class="title-reference">grafana\_datasource</em> for working diff
* grafana\_dashboard \- add uid to payload
* test\: replace more deprecated <em class="title-reference">TestCase\.assertEquals</em> to support Python 3\.12

<a id="community-postgresql-1"></a>
#### community\.postgresql

* postgresql\_alter\_system \- fix failure when max\_val contains a huge number written in scientific notation \([https\://github\.com/ansible\-collections/community\.postgresql/issues/853](https\://github\.com/ansible\-collections/community\.postgresql/issues/853)\)\.

<a id="dellemc-openmanage-3"></a>
#### dellemc\.openmanage

* idrac\_system\_info \- \(Issue 812\) \- idrac\_system\_info fails on iDRAC10\.

<a id="google-cloud"></a>
#### google\.cloud

* gcp\_compute \- fixed get\_project\_disks to process all responses \([https\://github\.com/ansible\-collections/google\.cloud/pull/677](https\://github\.com/ansible\-collections/google\.cloud/pull/677)\)\.
* updated README to match required format \([https\://github\.com/ansible\-collections/google\.cloud/pull/682](https\://github\.com/ansible\-collections/google\.cloud/pull/682)\)\.

<a id="kubernetes-core-1"></a>
#### kubernetes\.core

* module\_utils/k8s/service \- fix issue when trying to delete resource using <em class="title-reference">delete\_options</em> and <em class="title-reference">check\_mode\=true</em> \([https\://github\.com/ansible\-collections/kubernetes\.core/issues/892](https\://github\.com/ansible\-collections/kubernetes\.core/issues/892)\)\.

<a id="microsoft-ad-2"></a>
#### microsoft\.ad

* ldap inventory \- Fix up support for Ansible 2\.19\.

<a id="purestorage-flashblade-1"></a>
#### purestorage\.flashblade

* purefb\_bucket \- Resolved issue with removing bucket quota
* purefb\_info \- Fixed issue after SMD Directory Services no longer avaible from REST 2\.16
* purefb\_policy \- Fixed creation of snapshot policies with assigned filesystems and/or replica links
* purefb\_s3acc \- Fixed issue with public access config settings not being correctly for an account

<a id="known-issues-1"></a>
### Known Issues

<a id="dellemc-openmanage-4"></a>
#### dellemc\.openmanage

* idrac\_diagnostics \- Issue\(285322\) \- This module doesn\'t support export of diagnostics file to HTTP and HTTPS share via SOCKS proxy\.
* idrac\_firmware \- Issue\(279282\) \- This module does not support firmware update using HTTP\, HTTPS\, and FTP shares with authentication on iDRAC8\.
* ome\_smart\_fabric\_uplink \- Issue\(186024\) \- The module supported by OpenManage Enterprise Modular\, however it does not allow the creation of multiple uplinks of the same name\. If an uplink is created using the same name as an existing uplink\, then the existing uplink is modified\.

<a id="new-plugins"></a>
### New Plugins

<a id="callback"></a>
#### Callback

* community\.general\.print\_task \- Prints playbook task snippet to job output\.

<a id="filter"></a>
#### Filter

* community\.general\.to\_prettytable \- Format a list of dictionaries as an ASCII table\.

<a id="new-modules-1"></a>
### New Modules

<a id="community-general-6"></a>
#### community\.general

* community\.general\.xdg\_mime \- Set default handler for MIME types\, for applications using XDG tools\.

<a id="community-hrobot-2"></a>
#### community\.hrobot

* community\.hrobot\.storagebox\_snapshot \- Create\, update\, or delete a snapshot of a storage box\.

<a id="hitachivantara-vspone-block-4"></a>
#### hitachivantara\.vspone\_block

<a id="vsp-1"></a>
##### Vsp

* hitachivantara\.vspone\_block\.hv\_ddp\_pool \- Manages DDP Pools on Hitachi VSP storage systems\.
* hitachivantara\.vspone\_block\.hv\_ddp\_pool\_facts \- Get facts of DDP Pools on Hitachi VSP storage systems\.

<a id="purestorage-flashblade-2"></a>
#### purestorage\.flashblade

* purestorage\.flashblade\.purefb\_bucket\_access \- Manage FlashBlade bucket access policies
* purestorage\.flashblade\.purefb\_fleet \- Manage Fusion Fleet
* purestorage\.flashblade\.purefb\_server \- Manage FlashBlade servers

<a id="unchanged-collections-1"></a>
### Unchanged Collections

* ansible\.netcommon \(still version 7\.2\.0\)
* ansible\.posix \(still version 1\.6\.2\)
* ansible\.utils \(still version 5\.1\.2\)
* ansible\.windows \(still version 2\.8\.0\)
* arista\.eos \(still version 10\.1\.1\)
* awx\.awx \(still version 24\.6\.1\)
* azure\.azcollection \(still version 3\.3\.1\)
* check\_point\.mgmt \(still version 6\.4\.0\)
* chocolatey\.chocolatey \(still version 1\.5\.3\)
* cisco\.aci \(still version 2\.11\.0\)
* cisco\.asa \(still version 6\.1\.0\)
* cisco\.dnac \(still version 6\.31\.3\)
* cisco\.ios \(still version 9\.2\.0\)
* cisco\.iosxr \(still version 10\.3\.1\)
* cisco\.ise \(still version 2\.10\.0\)
* cisco\.mso \(still version 2\.10\.0\)
* cisco\.nxos \(still version 9\.4\.0\)
* cisco\.ucs \(still version 1\.16\.0\)
* cloudscale\_ch\.cloud \(still version 2\.4\.1\)
* community\.ciscosmb \(still version 1\.0\.10\)
* community\.digitalocean \(still version 1\.27\.0\)
* community\.hashi\_vault \(still version 6\.2\.0\)
* community\.library\_inventory\_filtering\_v1 \(still version 1\.1\.1\)
* community\.libvirt \(still version 1\.3\.1\)
* community\.mongodb \(still version 1\.7\.9\)
* community\.mysql \(still version 3\.13\.0\)
* community\.network \(still version 5\.1\.0\)
* community\.okd \(still version 4\.0\.1\)
* community\.proxysql \(still version 1\.6\.0\)
* community\.rabbitmq \(still version 1\.4\.0\)
* community\.routeros \(still version 3\.6\.0\)
* community\.sap\_libs \(still version 1\.4\.2\)
* community\.sops \(still version 2\.0\.5\)
* community\.vmware \(still version 5\.6\.0\)
* community\.windows \(still version 2\.4\.0\)
* community\.zabbix \(still version 3\.3\.0\)
* containers\.podman \(still version 1\.16\.3\)
* cyberark\.conjur \(still version 1\.3\.3\)
* dellemc\.enterprise\_sonic \(still version 2\.5\.1\)
* dellemc\.powerflex \(still version 2\.6\.0\)
* dellemc\.unity \(still version 2\.0\.0\)
* f5networks\.f5\_modules \(still version 1\.35\.0\)
* fortinet\.fortimanager \(still version 2\.9\.1\)
* fortinet\.fortios \(still version 2\.4\.0\)
* grafana\.grafana \(still version 5\.7\.0\)
* hetzner\.hcloud \(still version 4\.3\.0\)
* ibm\.qradar \(still version 4\.0\.0\)
* ibm\.spectrum\_virtualize \(still version 2\.0\.0\)
* ibm\.storage\_virtualize \(still version 2\.7\.3\)
* ieisystem\.inmanage \(still version 3\.0\.0\)
* infinidat\.infinibox \(still version 1\.4\.5\)
* infoblox\.nios\_modules \(still version 1\.8\.0\)
* inspur\.ispim \(still version 2\.2\.3\)
* junipernetworks\.junos \(still version 9\.1\.0\)
* kaytus\.ksmanage \(still version 2\.0\.0\)
* microsoft\.iis \(still version 1\.0\.2\)
* netapp\.cloudmanager \(still version 21\.24\.0\)
* netapp\.ontap \(still version 22\.14\.0\)
* netapp\.storagegrid \(still version 21\.14\.0\)
* netapp\_eseries\.santricity \(still version 1\.4\.1\)
* netbox\.netbox \(still version 3\.21\.0\)
* ngine\_io\.cloudstack \(still version 2\.5\.0\)
* openstack\.cloud \(still version 2\.4\.1\)
* ovirt\.ovirt \(still version 3\.2\.0\)
* purestorage\.flasharray \(still version 1\.34\.1\)
* sensu\.sensu\_go \(still version 1\.14\.0\)
* splunk\.es \(still version 4\.0\.0\)
* telekom\_mms\.icinga\_director \(still version 2\.2\.2\)
* theforeman\.foreman \(still version 4\.2\.0\)
* vmware\.vmware \(still version 1\.11\.0\)
* vmware\.vmware\_rest \(still version 4\.7\.0\)
* vultr\.cloud \(still version 1\.13\.0\)
* vyos\.vyos \(still version 5\.0\.0\)
* wti\.remote \(still version 1\.0\.10\)

<a id="v11-5-0"></a>
## v11\.5\.0

- <a href="#release-summary-2">Release Summary</a>
- <a href="#added-collections-1">Added Collections</a>
- <a href="#ansible-core-4">Ansible\-core</a>
- <a href="#changed-collections-2">Changed Collections</a>
- <a href="#major-changes-2">Major Changes</a>
    - <a href="#fortinet-fortios">fortinet\.fortios</a>
- <a href="#minor-changes-2">Minor Changes</a>
    - <a href="#amazon-aws-2">amazon\.aws</a>
    - <a href="#ansible-netcommon">ansible\.netcommon</a>
    - <a href="#cisco-aci">cisco\.aci</a>
    - <a href="#cisco-dnac">cisco\.dnac</a>
    - <a href="#cisco-ios">cisco\.ios</a>
    - <a href="#cisco-mso">cisco\.mso</a>
    - <a href="#cisco-nxos">cisco\.nxos</a>
    - <a href="#community-aws-1">community\.aws</a>
    - <a href="#community-general-7">community\.general</a>
    - <a href="#community-library-inventory-filtering-v1">community\.library\_inventory\_filtering\_v1</a>
    - <a href="#community-routeros-1">community\.routeros</a>
    - <a href="#community-vmware-3">community\.vmware</a>
    - <a href="#ibm-storage-virtualize-2">ibm\.storage\_virtualize</a>
    - <a href="#kubernetes-core-2">kubernetes\.core</a>
    - <a href="#lowlydba-sqlserver-1">lowlydba\.sqlserver</a>
    - <a href="#purestorage-flasharray">purestorage\.flasharray</a>
    - <a href="#vmware-vmware">vmware\.vmware</a>
    - <a href="#vmware-vmware-rest">vmware\.vmware\_rest</a>
- <a href="#deprecated-features-2">Deprecated Features</a>
    - <a href="#ansible-netcommon-1">ansible\.netcommon</a>
    - <a href="#cisco-ios-1">cisco\.ios</a>
    - <a href="#community-general-8">community\.general</a>
    - <a href="#community-postgresql-2">community\.postgresql</a>
    - <a href="#community-vmware-4">community\.vmware</a>
- <a href="#bugfixes-2">Bugfixes</a>
    - <a href="#ansible-core-5">Ansible\-core</a>
    - <a href="#amazon-aws-3">amazon\.aws</a>
    - <a href="#ansible-netcommon-2">ansible\.netcommon</a>
    - <a href="#cisco-aci-1">cisco\.aci</a>
    - <a href="#cisco-ios-2">cisco\.ios</a>
    - <a href="#cisco-iosxr">cisco\.iosxr</a>
    - <a href="#cisco-meraki-3">cisco\.meraki</a>
    - <a href="#cisco-mso-1">cisco\.mso</a>
    - <a href="#cisco-nxos-1">cisco\.nxos</a>
    - <a href="#community-dns-2">community\.dns</a>
    - <a href="#community-general-9">community\.general</a>
    - <a href="#community-library-inventory-filtering-v1-1">community\.library\_inventory\_filtering\_v1</a>
    - <a href="#community-postgresql-3">community\.postgresql</a>
    - <a href="#community-sops-1">community\.sops</a>
    - <a href="#community-vmware-5">community\.vmware</a>
    - <a href="#dellemc-openmanage-5">dellemc\.openmanage</a>
    - <a href="#f5networks-f5-modules-1">f5networks\.f5\_modules</a>
    - <a href="#fortinet-fortios-1">fortinet\.fortios</a>
    - <a href="#ibm-storage-virtualize-3">ibm\.storage\_virtualize</a>
    - <a href="#purestorage-flasharray-1">purestorage\.flasharray</a>
    - <a href="#vmware-vmware-1">vmware\.vmware</a>
- <a href="#known-issues-2">Known Issues</a>
    - <a href="#community-general-10">community\.general</a>
    - <a href="#dellemc-openmanage-6">dellemc\.openmanage</a>
- <a href="#new-plugins-1">New Plugins</a>
    - <a href="#connection">Connection</a>
- <a href="#new-modules-2">New Modules</a>
    - <a href="#cisco-ios-3">cisco\.ios</a>
    - <a href="#community-postgresql-4">community\.postgresql</a>
    - <a href="#ibm-storage-virtualize-4">ibm\.storage\_virtualize</a>
- <a href="#unchanged-collections-2">Unchanged Collections</a>

<a id="release-summary-2"></a>
### Release Summary

Release Date\: 2025\-04\-22

[Porting Guide](https\://docs\.ansible\.com/ansible/devel/porting\_guides\.html)

<a id="added-collections-1"></a>
### Added Collections

* hitachivantara\.vspone\_block \(version 3\.3\.0\)
* microsoft\.iis \(version 1\.0\.2\)

<a id="ansible-core-4"></a>
### Ansible\-core

Ansible 11\.5\.0 contains ansible\-core version 2\.18\.5\.
This is a newer version than version 2\.18\.4 contained in the previous Ansible release\.

The changes are reported in the combined changelog below\.

<a id="changed-collections-2"></a>
### Changed Collections

If not mentioned explicitly\, the changes are reported in the combined changelog below\.

| Collection                               | Ansible 11.4.0 | Ansible 11.5.0 | Notes                                                                                                                        |
| ---------------------------------------- | -------------- | -------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| amazon.aws                               | 9.3.0          | 9.4.0          |                                                                                                                              |
| ansible.netcommon                        | 7.1.0          | 7.2.0          |                                                                                                                              |
| cisco.aci                                | 2.10.1         | 2.11.0         |                                                                                                                              |
| cisco.dnac                               | 6.31.0         | 6.31.3         |                                                                                                                              |
| cisco.ios                                | 9.1.2          | 9.2.0          |                                                                                                                              |
| cisco.iosxr                              | 10.3.0         | 10.3.1         |                                                                                                                              |
| cisco.meraki                             | 2.20.8         | 2.20.10        |                                                                                                                              |
| cisco.mso                                | 2.9.0          | 2.10.0         |                                                                                                                              |
| cisco.nxos                               | 9.3.0          | 9.4.0          |                                                                                                                              |
| cisco.ucs                                | 1.15.0         | 1.16.0         | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
| community.aws                            | 9.1.0          | 9.2.0          |                                                                                                                              |
| community.dns                            | 3.2.2          | 3.2.3          |                                                                                                                              |
| community.general                        | 10.5.0         | 10.6.0         |                                                                                                                              |
| community.library_inventory_filtering_v1 | 1.0.2          | 1.1.1          |                                                                                                                              |
| community.postgresql                     | 3.12.0         | 3.14.0         |                                                                                                                              |
| community.routeros                       | 3.5.0          | 3.6.0          |                                                                                                                              |
| community.sops                           | 2.0.3          | 2.0.5          |                                                                                                                              |
| community.vmware                         | 5.5.0          | 5.6.0          |                                                                                                                              |
| dellemc.openmanage                       | 9.10.0         | 9.11.0         |                                                                                                                              |
| f5networks.f5_modules                    | 1.34.1         | 1.35.0         |                                                                                                                              |
| fortinet.fortios                         | 2.3.9          | 2.4.0          |                                                                                                                              |
| hitachivantara.vspone_block              |                | 3.3.0          | The collection was added to Ansible                                                                                          |
| ibm.storage_virtualize                   | 2.6.0          | 2.7.3          |                                                                                                                              |
| kubernetes.core                          | 5.1.0          | 5.2.0          |                                                                                                                              |
| lowlydba.sqlserver                       | 2.5.0          | 2.6.0          |                                                                                                                              |
| microsoft.ad                             | 1.8.0          | 1.8.1          |                                                                                                                              |
| microsoft.iis                            |                | 1.0.2          | The collection was added to Ansible                                                                                          |
| purestorage.flasharray                   | 1.33.1         | 1.34.1         |                                                                                                                              |
| vmware.vmware                            | 1.10.1         | 1.11.0         |                                                                                                                              |
| vmware.vmware_rest                       | 4.6.0          | 4.7.0          |                                                                                                                              |

<a id="major-changes-2"></a>
### Major Changes

<a id="fortinet-fortios"></a>
#### fortinet\.fortios

* Supported new versions 7\.6\.1 and 7\.6\.2\.
* Updated the examples with correct values that have minimum or maximum values\.

<a id="minor-changes-2"></a>
### Minor Changes

<a id="amazon-aws-2"></a>
#### amazon\.aws

* inventory/aws\_ec2 \- Update templating mechanism to support ansible\-core 2\.19 changes \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2552](https\://github\.com/ansible\-collections/amazon\.aws/pull/2552)\)\.

<a id="ansible-netcommon"></a>
#### ansible\.netcommon

* Exposes new libssh options to configure publickey\_accepted\_algorithms and hostkeys\. This requires ansible\-pylibssh v1\.1\.0 or higher\.

<a id="cisco-aci"></a>
#### cisco\.aci

* Add aci\_endpoint\_tag\_ip and aci\_endpoint\_tag\_mac modules to manage Endpoint IP and MAC Tags\.
* Add aci\_ip\_sla\_monitoring\_policy module\.
* Add management\_epg and management\_epg\_type attributes in aci\_dns\_profile module\.
* Add stratum attribute to aci\_ntp\_policy module\.
* Add support for Ansible 2\.18 and dropped support for Ansible 2\.15 as required by Ansible Galaxy\.

<a id="cisco-dnac"></a>
#### cisco\.dnac

* \.ansible\-lint is added to handle a formatting issue in Red Hat\.
* The file format was changed to conform to the requested standards\.
* noqa all is used to ignore rules in some files\.

<a id="cisco-ios"></a>
#### cisco\.ios

* Add ios\_evpn\_ethernet resource module\.

<a id="cisco-mso"></a>
#### cisco\.mso

* Add ep\_move\_detection\_mode attribute in mso\_schema\_template\_bd\.
* Add mso\_schema\_template\_anp\_epg\_annotation module\.
* Add mso\_schema\_template\_anp\_epg\_intra\_epg\_contract module\.
* Add name attribute to mso\_schema\_template\_external\_epg\_subnet module\.
* Add ndo\_ipsla\_track\_list and ndo\_ipsla\_monitoring\_policy modules\.
* Add ndo\_l3out\_node\_routing\_policy\, ndo\_l3out\_interface\_routing\_policy\, and ndo\_tenant\_bgp\_peer\_prefix\_policy modules\.
* Add ndo\_l3out\_template\, ndo\_l3out\_annotation\, ndo\_l3out\_interface\_group\_policy\, and ndo\_l3out\_node\_group\_policy modules\.
* Add ndo\_mcp\_global\_policy module\.
* Add ndo\_ntp\_policy\, ndo\_ptp\_policy\, and ndo\_ptp\_policy\_profiles modules\.
* Add ndo\_physical\_interface\, ndo\_port\_channel\_interface\, ndo\_virtual\_port\_channel\_interface\, ndo\_node\_profile\, and ndo\_fex\_device modules to support NDO Fabric Resource Policies\.
* Add ndo\_qos\_dscp\_cos\_translation\_policy module\.
* Add ndo\_synce\_interface\_policy\, ndo\_interface\_setting\, ndo\_node\_setting\, and ndo\_macsec\_policy modules\.
* Add ndo\_tenant\_custom\_qos\_policy module\.
* Add ndo\_tenant\_igmp\_interface\_policy\, ndo\_tenant\_igmp\_snooping\_policy\, and ndo\_tenant\_mld\_snooping\_policy modules\.
* Add qos\_level attribute to the mso\_schema\_template\_external\_epg module\.
* Add support for Ansible 2\.18 and dropped support for Ansible 2\.15 as required by Ansible Galaxy\.
* Add support for site configuration for tenant policy template in ndo\_template module\.

<a id="cisco-nxos"></a>
#### cisco\.nxos

* nxos\_vpc \- Added support for peer\-switch feature configuration\.

<a id="community-aws-1"></a>
#### community\.aws

* aws\_ssm \- Refactor <code>\_exec\_transport\_commands</code>\, <code>\_generate\_commands</code>\, and <code>\_exec\_transport\_commands</code> methods for improved clarity \([https\://github\.com/ansible\-collections/community\.aws/pull/2248](https\://github\.com/ansible\-collections/community\.aws/pull/2248)\)\.
* aws\_ssm \- Refactor connection/aws\_ssm to add new S3ClientManager class and move relevant methods to the new class \([https\://github\.com/ansible\-collections/community\.aws/pull/2255](https\://github\.com/ansible\-collections/community\.aws/pull/2255)\)\.
* aws\_ssm \- Refactor display/verbosity\-related methods in aws\_ssm to simplify the code and avoid repetition \([https\://github\.com/ansible\-collections/community\.aws/pull/2264](https\://github\.com/ansible\-collections/community\.aws/pull/2264)\)\.

<a id="community-general-7"></a>
#### community\.general

* apache2\_module \- added workaround for new PHP module name\, from <code>php7\_module</code> to <code>php\_module</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9951](https\://github\.com/ansible\-collections/community\.general/pull/9951)\)\.
* gitlab\_project \- add option <code>build\_timeout</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9960](https\://github\.com/ansible\-collections/community\.general/pull/9960)\)\.
* gitlab\_project\_members \- extend choices parameter <code>access\_level</code> by missing upstream valid value <code>owner</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9953](https\://github\.com/ansible\-collections/community\.general/pull/9953)\)\.
* hpilo\_boot \- add option to get an idempotent behavior while powering on server\, resulting in success instead of failure when using <code>state\: boot\_once</code> option \([https\://github\.com/ansible\-collections/community\.general/pull/9646](https\://github\.com/ansible\-collections/community\.general/pull/9646)\)\.
* idrac\_redfish\_command\, idrac\_redfish\_config\, idrac\_redfish\_info \- add <code>validate\_certs</code>\, <code>ca\_path</code>\, and <code>ciphers</code> options to configure TLS/SSL \([https\://github\.com/ansible\-collections/community\.general/issues/3686](https\://github\.com/ansible\-collections/community\.general/issues/3686)\, [https\://github\.com/ansible\-collections/community\.general/pull/9964](https\://github\.com/ansible\-collections/community\.general/pull/9964)\)\.
* ilo\_redfish\_command\, ilo\_redfish\_config\, ilo\_redfish\_info \- add <code>validate\_certs</code>\, <code>ca\_path</code>\, and <code>ciphers</code> options to configure TLS/SSL \([https\://github\.com/ansible\-collections/community\.general/issues/3686](https\://github\.com/ansible\-collections/community\.general/issues/3686)\, [https\://github\.com/ansible\-collections/community\.general/pull/9964](https\://github\.com/ansible\-collections/community\.general/pull/9964)\)\.
* keycloak module\_utils \- user groups can now be referenced by their name\, like <code>staff</code>\, or their path\, like <code>/staff/engineering</code>\. The path syntax allows users to reference subgroups\, which is not possible otherwise \([https\://github\.com/ansible\-collections/community\.general/pull/9898](https\://github\.com/ansible\-collections/community\.general/pull/9898)\)\.
* keycloak\_user module \- user groups can now be referenced by their name\, like <code>staff</code>\, or their path\, like <code>/staff/engineering</code>\. The path syntax allows users to reference subgroups\, which is not possible otherwise \([https\://github\.com/ansible\-collections/community\.general/pull/9898](https\://github\.com/ansible\-collections/community\.general/pull/9898)\)\.
* nmcli \- add support for Infiniband MAC setting when <code>type</code> is <code>infiniband</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9962](https\://github\.com/ansible\-collections/community\.general/pull/9962)\)\.
* one\_vm \- update allowed values for <code>updateconf</code> to include new parameters as per the latest OpenNebula API documentation\.
  Added parameters\:

  - <code>OS</code>\: <code>FIRMWARE</code>\;
  - <code>CPU\_MODEL</code>\: <code>MODEL</code>\, <code>FEATURES</code>\;
  - <code>FEATURES</code>\: <code>VIRTIO\_BLK\_QUEUES</code>\, <code>VIRTIO\_SCSI\_QUEUES</code>\, <code>IOTHREADS</code>\;
  - <code>GRAPHICS</code>\: <code>PORT</code>\, <code>COMMAND</code>\;
  - <code>VIDEO</code>\: <code>ATS</code>\, <code>IOMMU</code>\, <code>RESOLUTION</code>\, <code>TYPE</code>\, <code>VRAM</code>\;
  - <code>RAW</code>\: <code>VALIDATE</code>\;
  - <code>BACKUP\_CONFIG</code>\: <code>FS\_FREEZE</code>\, <code>KEEP\_LAST</code>\, <code>BACKUP\_VOLATILE</code>\, <code>MODE</code>\, <code>INCREMENT\_MODE</code>\.

  \([https\://github\.com/ansible\-collections/community\.general/pull/9959](https\://github\.com/ansible\-collections/community\.general/pull/9959)\)\.
* proxmox and proxmox\_kvm modules \- allow uppercase characters in VM/container tags \([https\://github\.com/ansible\-collections/community\.general/issues/9895](https\://github\.com/ansible\-collections/community\.general/issues/9895)\, [https\://github\.com/ansible\-collections/community\.general/pull/10024](https\://github\.com/ansible\-collections/community\.general/pull/10024)\)\.
* puppet \- improve parameter formatting\, no impact to user \([https\://github\.com/ansible\-collections/community\.general/pull/10014](https\://github\.com/ansible\-collections/community\.general/pull/10014)\)\.
* redfish module utils \- add <code>REDFISH\_COMMON\_ARGUMENT\_SPEC</code>\, a corresponding <code>redfish</code> docs fragment\, and support for its <code>validate\_certs</code>\, <code>ca\_path</code>\, and <code>ciphers</code> options \([https\://github\.com/ansible\-collections/community\.general/issues/3686](https\://github\.com/ansible\-collections/community\.general/issues/3686)\, [https\://github\.com/ansible\-collections/community\.general/pull/9964](https\://github\.com/ansible\-collections/community\.general/pull/9964)\)\.
* redfish\_command\, redfish\_config\, redfish\_info \- add <code>validate\_certs</code> and <code>ca\_path</code> options to configure TLS/SSL \([https\://github\.com/ansible\-collections/community\.general/issues/3686](https\://github\.com/ansible\-collections/community\.general/issues/3686)\, [https\://github\.com/ansible\-collections/community\.general/pull/9964](https\://github\.com/ansible\-collections/community\.general/pull/9964)\)\.
* rocketchat \- fix duplicate JSON conversion for Rocket\.Chat \< 7\.4\.0 \([https\://github\.com/ansible\-collections/community\.general/pull/9965](https\://github\.com/ansible\-collections/community\.general/pull/9965)\)\.
* wdc\_redfish\_command\, wdc\_redfish\_info \- add <code>validate\_certs</code>\, <code>ca\_path</code>\, and <code>ciphers</code> options to configure TLS/SSL \([https\://github\.com/ansible\-collections/community\.general/issues/3686](https\://github\.com/ansible\-collections/community\.general/issues/3686)\, [https\://github\.com/ansible\-collections/community\.general/pull/9964](https\://github\.com/ansible\-collections/community\.general/pull/9964)\)\.
* xcc\_redfish\_command \- add <code>validate\_certs</code>\, <code>ca\_path</code>\, and <code>ciphers</code> options to configure TLS/SSL \([https\://github\.com/ansible\-collections/community\.general/issues/3686](https\://github\.com/ansible\-collections/community\.general/issues/3686)\, [https\://github\.com/ansible\-collections/community\.general/pull/9964](https\://github\.com/ansible\-collections/community\.general/pull/9964)\)\.
* zypper \- adds <code>skip\_post\_errors</code> that allows to skip RPM post\-install errors \(Zypper return code 107\) \([https\://github\.com/ansible\-collections/community\.general/issues/9972](https\://github\.com/ansible\-collections/community\.general/issues/9972)\)\.

<a id="community-library-inventory-filtering-v1"></a>
#### community\.library\_inventory\_filtering\_v1

* Add typing information for the <code>inventory\_filter</code> plugin utils \([https\://github\.com/ansible\-collections/community\.library\_inventory\_filtering/pull/22](https\://github\.com/ansible\-collections/community\.library\_inventory\_filtering/pull/22)\)\.

<a id="community-routeros-1"></a>
#### community\.routeros

* api\_info\, api\_modify \- add <code>mdns\-repeat\-ifaces</code> to <code>ip dns</code> for RouterOS 7\.16 and newer \([https\://github\.com/ansible\-collections/community\.routeros/pull/358](https\://github\.com/ansible\-collections/community\.routeros/pull/358)\)\.
* api\_info\, api\_modify \- field name change in <code>routing bgp connection</code> path implemented by RouterOS 7\.19 and newer \([https\://github\.com/ansible\-collections/community\.routeros/pull/360](https\://github\.com/ansible\-collections/community\.routeros/pull/360)\)\.
* api\_info\, api\_modify \- rename <code>is\-responder</code> property in <code>interface wireguard peers</code> to <code>responder</code> for RouterOS 7\.17 and newer \([https\://github\.com/ansible\-collections/community\.routeros/pull/364](https\://github\.com/ansible\-collections/community\.routeros/pull/364)\)\.

<a id="community-vmware-3"></a>
#### community\.vmware

* module\_utils\.vmware \- Move <code>vmware\_argument\_spec</code> to a dedicated file \([https\://github\.com/ansible\-collections/community\.vmware/pull/2370](https\://github\.com/ansible\-collections/community\.vmware/pull/2370)\)\.
* module\_utils\.vmware\_rest\_client \- Move <code>vmware\_client\_argument\_spec</code> to a dedicated file \([https\://github\.com/ansible\-collections/community\.vmware/pull/2370](https\://github\.com/ansible\-collections/community\.vmware/pull/2370)\)\.
* vmware\_dvs\_portgroup \- New option <code>network\_policy\.mac\_learning</code> to replace <code>mac\_learning</code> \([https\://github\.com/ansible\-collections/community\.vmware/pull/2360](https\://github\.com/ansible\-collections/community\.vmware/pull/2360)\)\.
* vmware\_object\_role\_permission \- Document setting permissions on vCenter level \([https\://github\.com/ansible\-collections/community\.vmware/pull/2374](https\://github\.com/ansible\-collections/community\.vmware/pull/2374)\)\.

<a id="ibm-storage-virtualize-2"></a>
#### ibm\.storage\_virtualize

* ibm\_sv\_manage\_replication\_policy \- Added support for highly\-available snapshots
* ibm\_sv\_manage\_snapshot\- Add support for restoring highly\-available volumes and volumegroups from local snapshots
* ibm\_sv\_manage\_truststore\_for\_replication \- Added support for creating truststore for flashsystem grid
* ibm\_svc\_host \- Added support for specifying host location in PBHA\, support for FDMI discovery\, suppressing offline alert\, updating IO groups\, and for specifying fcscsi and iscsi protocols during host creation
* ibm\_svc\_info \- Added support for flashsystem grid
* ibm\_svc\_initial\_setup \- Added support for vdisk protection settings\, iscsiauthmethod and improved REST API calls
* ibm\_svc\_manage\_flashcopy \- Added support for enabling cleanrate during flashcopy creation and update
* ibm\_svc\_manage\_replication \- Added support for highly\-available snapshots
* ibm\_svc\_manage\_volume \- Added support for unmapping hosts\, remote\-copy and flashcopy during volume deletion
* ibm\_svc\_mdisk \- Added support for updating tier
* ibm\_svc\_mdiskgrp \- Improved probe function for storage pools

<a id="kubernetes-core-2"></a>
#### kubernetes\.core

* k8s \- Extend hidden\_fields to allow the expression of more complex field types to be hidden \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/872](https\://github\.com/ansible\-collections/kubernetes\.core/pull/872)\)
* k8s\_info \- Extend hidden\_fields to allow the expression of more complex field types to be hidden \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/872](https\://github\.com/ansible\-collections/kubernetes\.core/pull/872)\)
* waiter\.py \- add ClusterOperator support\. The module can now check OpenShift cluster health by verifying ClusterOperator status requiring \'Available\: True\'\, \'Degraded\: False\'\, and \'Progressing\: False\' for success\. \([https\://github\.com/ansible\-collections/kubernetes\.core/issues/869](https\://github\.com/ansible\-collections/kubernetes\.core/issues/869)\)

<a id="lowlydba-sqlserver-1"></a>
#### lowlydba\.sqlserver

* Added support for contained Availability Groups using dbatools 2\.1\.15 \([https\://github\.com/lowlydba/lowlydba\.sqlserver/pull/249](https\://github\.com/lowlydba/lowlydba\.sqlserver/pull/249)\)\.

<a id="purestorage-flasharray"></a>
#### purestorage\.flasharray

* purefa\_timeout \- Convert to REST v2
* purefa\_user \- Added parameter for SSH public keys and API token timeout
* purefa\_user \- Converted to use REST v2
* purefa\_user \- When changing API token or timout for an existing user\, the user role must be provided or it will revert to <code>readonly</code>

<a id="vmware-vmware"></a>
#### vmware\.vmware

* \_module\_pyvmomi\_base \- Make sure to use the folder param when searching for VMs based on other common params in get\_vms\_using\_params
* added vm\_resource\_info module to collect cpu/memory facts about vms
* clients/\_pyvmomi \- adds explicit init params instead of using dict
* clients/\_rest \- adds explicit init params instead of using dict
* esxi\_hosts \- Add inventory host filtering based on jinja statements
* esxi\_hosts inventory \- include moid property in output always
* pyvmomi \- update object search by name method to use propertycollector\, which speeds up results significantly
* upload\_content\_library\_ovf \- Add module to upload an ovf/ova to a content library
* vm\_powerstate \- migrate vmware\_guest\_powerstate module from community to here
* vms \- Add inventory host filtering based on jinja statements
* vms inventory \- include moid property in output always

<a id="vmware-vmware-rest"></a>
#### vmware\.vmware\_rest

* Deprecated modules with redundant functionality in vmware\.vmware\. The next major release is currently not planned\, so no removal date is provided\. See [https\://github\.com/ansible\-collections/vmware\.vmware\_rest/issues/589](https\://github\.com/ansible\-collections/vmware\.vmware\_rest/issues/589)

<a id="deprecated-features-2"></a>
### Deprecated Features

<a id="ansible-netcommon-1"></a>
#### ansible\.netcommon

* Added deprecation warnings for the above plugins\, displayed when running respective filter plugins\.
* <em class="title-reference">parse\_cli\_textfsm</em> filter plugin is deprecated and will be removed in a future release after 2027\-02\-01\. Use <em class="title-reference">ansible\.utils\.cli\_parse</em> with the <em class="title-reference">ansible\.utils\.textfsm\_parser</em> parser as a replacement\.
* <em class="title-reference">parse\_cli</em> filter plugin is deprecated and will be removed in a future release after 2027\-02\-01\. Use <em class="title-reference">ansible\.utils\.cli\_parse</em> as a replacement\.
* <em class="title-reference">parse\_xml</em> filter plugin is deprecated and will be removed in a future release after 2027\-02\-01\. Use <em class="title-reference">ansible\.utils\.cli\_parse</em> with the <em class="title-reference">ansible\.utils\.xml\_parser</em> parser as a replacement\.

<a id="cisco-ios-1"></a>
#### cisco\.ios

* ios\_vlans \- deprecate mtu\, please use ios\_interfaces to configure mtu to the interface where vlans is applied\.

<a id="community-general-8"></a>
#### community\.general

* manifold lookup plugin \- plugin is deprecated and will be removed in community\.general 11\.0\.0 \([https\://github\.com/ansible\-collections/community\.general/pull/10028](https\://github\.com/ansible\-collections/community\.general/pull/10028)\)\.
* stackpath\_compute inventory plugin \- plugin is deprecated and will be removed in community\.general 11\.0\.0 \([https\://github\.com/ansible\-collections/community\.general/pull/10026](https\://github\.com/ansible\-collections/community\.general/pull/10026)\)\.

<a id="community-postgresql-2"></a>
#### community\.postgresql

* postgresql\_copy \- the parameter aliases db and database are deprecated and will be removed in community\.postgresql 5\.0\.0\. Use login\_db instead\.
* postgresql\_db \- the <code>rename</code> choice of the state option is deprecated and will be removed in version 5\.0\.0\, use the <code>postgresql\_query</code> module instead\.
* postgresql\_ext \- the parameter aliases db and database are deprecated and will be removed in community\.postgresql 5\.0\.0\. Use login\_db instead\.
* postgresql\_idx \- the parameter aliases db and database are deprecated and will be removed in community\.postgresql 5\.0\.0\. Use login\_db instead\.
* postgresql\_membership \- the parameter aliases db and database are deprecated and will be removed in community\.postgresql 5\.0\.0\. Use login\_db instead\.
* postgresql\_owner \- the parameter aliases db and database are deprecated and will be removed in community\.postgresql 5\.0\.0\. Use login\_db instead\.
* postgresql\_ping \- the parameter aliases db and database are deprecated and will be removed in community\.postgresql 5\.0\.0\. Use login\_db instead\.
* postgresql\_privs \- the parameter aliases db and database are deprecated and will be removed in community\.postgresql 5\.0\.0\. Use login\_db instead\.
* postgresql\_publication \- the parameter aliases db and database are deprecated and will be removed in community\.postgresql 5\.0\.0\. Use login\_db instead\.
* postgresql\_query \- the parameter aliases db and database are deprecated and will be removed in community\.postgresql 5\.0\.0\. Use login\_db instead\.
* postgresql\_schema \- the parameter aliases db and database are deprecated and will be removed in community\.postgresql 5\.0\.0\. Use login\_db instead\.
* postgresql\_script \- the parameter aliases db and database are deprecated and will be removed in community\.postgresql 5\.0\.0\. Use login\_db instead\.
* postgresql\_sequence \- the <code>rename\_to</code> option is deprecated and will be removed in version 5\.0\.0\, use the <code>postgresql\_query</code> module instead\.
* postgresql\_sequence \- the parameter aliases db and database are deprecated and will be removed in community\.postgresql 5\.0\.0\. Use login\_db instead\.
* postgresql\_set \- the parameter aliases db and database are deprecated and will be removed in community\.postgresql 5\.0\.0\. Use login\_db instead\.
* postgresql\_slot \- the parameter aliases db and database are deprecated and will be removed in community\.postgresql 5\.0\.0\. Use login\_db instead\.
* postgresql\_subscription \- the parameter aliases db and database are deprecated and will be removed in community\.postgresql 5\.0\.0\. Use login\_db instead\.
* postgresql\_table \- the <code>rename</code> option is deprecated and will be removed in version 5\.0\.0\, use the <code>postgresql\_query module</code> instead\.
* postgresql\_table \- the parameter aliases db and database are deprecated and will be removed in community\.postgresql 5\.0\.0\. Use login\_db instead\.
* postgresql\_tablespace \- the <code>rename\_to</code> option is deprecated and will be removed in version 5\.0\.0\, use the <code>postgresql\_query</code> module instead\.
* postgresql\_tablespace \- the parameter aliases db and database are deprecated and will be removed in community\.postgresql 5\.0\.0\. Use login\_db instead\.
* postgresql\_user\_obj\_stat\_info \- the parameter aliases db and database are deprecated and will be removed in community\.postgresql 5\.0\.0\. Use login\_db instead\.

<a id="community-vmware-4"></a>
#### community\.vmware

* vmware\_dvs\_portgroup \- <code>mac\_learning</code> is deprecated in favour of <code>network\_policy\.mac\_learning</code> \([https\://github\.com/ansible\-collections/community\.vmware/pull/2360](https\://github\.com/ansible\-collections/community\.vmware/pull/2360)\)\.

<a id="bugfixes-2"></a>
### Bugfixes

<a id="ansible-core-5"></a>
#### Ansible\-core

* build \- Pin <code>wheel</code> in <code>pyproject\.toml</code> to ensure compatibility with supported <code>setuptools</code> versions\.
* dnf5 \- Handle forwarded exceptions from dnf5\-5\.2\.13 where a generic <code>RuntimeError</code> was previously raised
* find \- skip ENOENT error code while recursively enumerating files\. find module will now be tolerant to race conditions that remove files or directories from the target it is currently inspecting\. \([https\://github\.com/ansible/ansible/issues/84873](https\://github\.com/ansible/ansible/issues/84873)\)\.
* gather\_facts action\, will now add setup when \'smart\' appears with other modules in the FACTS\_MODULES setting \(\#84750\)\.
* uri \- Form location correctly when the server returns a relative redirect \([https\://github\.com/ansible/ansible/issues/84540](https\://github\.com/ansible/ansible/issues/84540)\)

<a id="amazon-aws-3"></a>
#### amazon\.aws

* lookup/aws\_account\_attribute \- plugin should return a list when <code>wantlist\=True</code> \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2552](https\://github\.com/ansible\-collections/amazon\.aws/pull/2552)\)\.

<a id="ansible-netcommon-2"></a>
#### ansible\.netcommon

* libssh connection plugin \- stop using long\-deprecated and now removed internal field from ansible\-core\'s base connection plugin class \([https\://github\.com/ansible\-collections/ansible\.netcommon/issues/522](https\://github\.com/ansible\-collections/ansible\.netcommon/issues/522)\, [https\://github\.com/ansible\-collections/ansible\.netcommon/issues/690](https\://github\.com/ansible\-collections/ansible\.netcommon/issues/690)\, [https\://github\.com/ansible\-collections/ansible\.netcommon/pull/691](https\://github\.com/ansible\-collections/ansible\.netcommon/pull/691)\)\.

<a id="cisco-aci-1"></a>
#### cisco\.aci

* Fix aci\_rest module to only add annotation when the value is a dictionary
* Fix payload to define the correct vPC member side in aci\_l3out\_logical\_interface\_vpc\_member \(\#663\)
* Fix subclass issue in aci\_domain\_to\_vlan\_pool to fix deletion of binding \(\#695\)
* Modify interface\_configs requirement using required\_if dependency for aci\_bulk\_static\_binding\_to\_epg

<a id="cisco-ios-2"></a>
#### cisco\.ios

* ios\_logging\_global \- Fixed issue where cisco\.ios\.logging\_global module was not showing idempotent behaviour when trap was set to informational\.
* ios\_vlans \- Defaut mtu would be captured \(1500\) and no configuration for mtu is allowed via ios\_vlans module\.
* ios\_vlans \- Fixed an issue in the <em class="title-reference">cisco\.ios\.ios\_vlans</em> module on Cisco Catalyst 9000 switches where using state\:purged generated an incorrect command syntax \(<em class="title-reference">no vlan configuration \<vlan\_id\></em> instead of <em class="title-reference">no vlan \<vlan\_id\></em>\)\.
* ios\_vlans \- Resolved a failure in the <em class="title-reference">cisco\.ios\.ios\_vlans</em> module when using state\:deleted\, where the module incorrectly attempted to remove VLANs using <em class="title-reference">no mtu \<value\></em>\, causing an invalid input error\. The fix ensures that the module does not generate <em class="title-reference">no mtu</em> commands during VLAN deletion\, aligning with the correct VLAN removal behavior on Catalyst 9000 switches\.

<a id="cisco-iosxr"></a>
#### cisco\.iosxr

* Fixes a bug to allow connections to IOS XRd with cliconf\.
* Fixes idempotency for static routes with encap interfaces

<a id="cisco-meraki-3"></a>
#### cisco\.meraki

* Added validation for <em class="title-reference">radiusServerAttemptsLimit</em> with choices <em class="title-reference">\[1\, 2\, 3\, 4\, 5\]</em>\.
* Added validation for <em class="title-reference">radiusServerTimeout</em> with a range of valid values <em class="title-reference">\[1\-10\]</em>\.
* Fixed parameter handling for <em class="title-reference">update\_by\_id\_params</em> in cisco\.meraki\.networks\_wireless\_ssids to correctly map the following parameters \- <em class="title-reference">perClientBandwidthLimitDown</em> \- <em class="title-reference">perClientBandwidthLimitUp</em> \- <em class="title-reference">perSsidBandwidthLimitDown</em> \- <em class="title-reference">perSsidBandwidthLimitUp</em> \- <em class="title-reference">defaultVlanId</em> \- <em class="title-reference">radiusAccountingInterimInterval</em> \- <em class="title-reference">radiusGuestVlanId</em> \- <em class="title-reference">vlanId</em> \- <em class="title-reference">radiusServerAttemptsLimit</em> \- <em class="title-reference">radiusServerTimeout</em>
* cisco\.meraki\.devices\_wireless\_radio\_settings changed compare equality method to use <em class="title-reference">meraki\_compare\_equality</em>
* cisco\.meraki\.networks\_wireless\_ssids refactor parameter handling to avoid None values

<a id="cisco-mso-1"></a>
#### cisco\.mso

* Fix query results for bulk query to display correct static\_paths in mso\_schema\_site\_anp\_epg\_staticport module
* Fix replace operation for bulk present without force replace in mso\_schema\_site\_anp\_epg\_staticport module

<a id="cisco-nxos-1"></a>
#### cisco\.nxos

* nxos\_facts \- Fixes an issue in nxos\_facts where IPv6 addresses within VRF contexts were not being collected in <em class="title-reference">net\_all\_ipv6\_addresses</em>\.
* nxos\_user \- fixes wrong command being generated for purge function
* nxos\_vpc \- fixes failure due to kickstart\_ver\_str not being present

<a id="community-dns-2"></a>
#### community\.dns

* Update Public Suffix List\.

<a id="community-general-9"></a>
#### community\.general

* dependent look plugin \- make compatible with ansible\-core\'s Data Tagging feature \([https\://github\.com/ansible\-collections/community\.general/pull/9833](https\://github\.com/ansible\-collections/community\.general/pull/9833)\)\.
* diy callback plugin \- make compatible with ansible\-core\'s Data Tagging feature \([https\://github\.com/ansible\-collections/community\.general/pull/9833](https\://github\.com/ansible\-collections/community\.general/pull/9833)\)\.
* github\_deploy\_key \- check that key really exists on 422 to avoid masking other errors \([https\://github\.com/ansible\-collections/community\.general/issues/6718](https\://github\.com/ansible\-collections/community\.general/issues/6718)\, [https\://github\.com/ansible\-collections/community\.general/pull/10011](https\://github\.com/ansible\-collections/community\.general/pull/10011)\)\.
* hashids and unicode\_normalize filter plugins \- avoid deprecated <code>AnsibleFilterTypeError</code> on ansible\-core 2\.19 \([https\://github\.com/ansible\-collections/community\.general/pull/9992](https\://github\.com/ansible\-collections/community\.general/pull/9992)\)\.
* homebrew \- emit a useful error message if <code>brew info</code> reports a package tap is <code>null</code> \([https\://github\.com/ansible\-collections/community\.general/pull/10013](https\://github\.com/ansible\-collections/community\.general/pull/10013)\, [https\://github\.com/ansible\-collections/community\.general/issues/10012](https\://github\.com/ansible\-collections/community\.general/issues/10012)\)\.
* java\_cert \- the module no longer fails if the optional parameters <code>pkcs12\_alias</code> and <code>cert\_alias</code> are not provided \([https\://github\.com/ansible\-collections/community\.general/pull/9970](https\://github\.com/ansible\-collections/community\.general/pull/9970)\)\.
* keycloak\_authentication \- fix authentification config duplication for Keycloak \< 26\.2\.0 \([https\://github\.com/ansible\-collections/community\.general/pull/9987](https\://github\.com/ansible\-collections/community\.general/pull/9987)\)\.
* keycloak\_client \- fix the idempotency regression by normalizing the Keycloak response for <code>after\_client</code> \([https\://github\.com/ansible\-collections/community\.general/issues/9905](https\://github\.com/ansible\-collections/community\.general/issues/9905)\, [https\://github\.com/ansible\-collections/community\.general/pull/9976](https\://github\.com/ansible\-collections/community\.general/pull/9976)\)\.
* proxmox inventory plugin \- fix <code>ansible\_host</code> staying empty for certain Proxmox nodes \([https\://github\.com/ansible\-collections/community\.general/issues/5906](https\://github\.com/ansible\-collections/community\.general/issues/5906)\, [https\://github\.com/ansible\-collections/community\.general/pull/9952](https\://github\.com/ansible\-collections/community\.general/pull/9952)\)\.
* proxmox\_disk \- fail gracefully if <code>storage</code> is required but not provided by the user \([https\://github\.com/ansible\-collections/community\.general/issues/9941](https\://github\.com/ansible\-collections/community\.general/issues/9941)\, [https\://github\.com/ansible\-collections/community\.general/pull/9963](https\://github\.com/ansible\-collections/community\.general/pull/9963)\)\.
* reveal\_ansible\_type filter plugin and ansible\_type test plugin \- make compatible with ansible\-core\'s Data Tagging feature \([https\://github\.com/ansible\-collections/community\.general/pull/9833](https\://github\.com/ansible\-collections/community\.general/pull/9833)\)\.
* sysrc \- no longer always reporting <code>changed\=true</code> when <code>state\=absent</code>\. This fixes the method <code>exists\(\)</code> \([https\://github\.com/ansible\-collections/community\.general/issues/10004](https\://github\.com/ansible\-collections/community\.general/issues/10004)\, [https\://github\.com/ansible\-collections/community\.general/pull/10005](https\://github\.com/ansible\-collections/community\.general/pull/10005)\)\.
* yaml callback plugin \- use ansible\-core internals to avoid breakage with Data Tagging \([https\://github\.com/ansible\-collections/community\.general/pull/9833](https\://github\.com/ansible\-collections/community\.general/pull/9833)\)\.

<a id="community-library-inventory-filtering-v1-1"></a>
#### community\.library\_inventory\_filtering\_v1

* inventory\_filter plugin utils \- make compatible with ansible\-core\'s Data Tagging feature \([https\://github\.com/ansible\-collections/community\.library\_inventory\_filtering/pull/24](https\://github\.com/ansible\-collections/community\.library\_inventory\_filtering/pull/24)\)\.
* inventory\_plugin plugin util \- <code>parse\_filters</code> now filters <code>None</code> values with allowed keys \([https\://github\.com/ansible\-collections/community\.library\_inventory\_filtering/pull/27](https\://github\.com/ansible\-collections/community\.library\_inventory\_filtering/pull/27)\)\.

<a id="community-postgresql-3"></a>
#### community\.postgresql

* postgresql\_table \- consider schema name when checking for table \([https\://github\.com/ansible\-collections/community\.postgresql/issues/817](https\://github\.com/ansible\-collections/community\.postgresql/issues/817)\)\.  Table names are only unique within a schema\. This allows using the same table name in multiple schemas\.

<a id="community-sops-1"></a>
#### community\.sops

* load\_vars \- make evaluation compatible with Data Tagging in upcoming ansible\-core release \([https\://github\.com/ansible\-collections/community\.sops/pull/225](https\://github\.com/ansible\-collections/community\.sops/pull/225)\)\.

<a id="community-vmware-5"></a>
#### community\.vmware

* vmware\_dvs\_portgroup \- Fix idempotency issue with <code>mac\_learning</code> \([https\://github\.com/ansible\-collections/community\.vmware/issues/1873](https\://github\.com/ansible\-collections/community\.vmware/issues/1873)\)\.

<a id="dellemc-openmanage-5"></a>
#### dellemc\.openmanage

* Internal defect fixes were done for the following modules \- <code>idrac\_network\_attributes</code>\, <code>idrac\_certificates</code>\, <code>idrac\_redfish\_storage\_controller</code>\, <code>idrac\_boot\_order</code> and <code>idrac\_firmware</code>
* Resolved the issue in <code>idrac\_redfish\_storage\_volume</code> module where it returns 404 error on job creation when enabling encryption for virtual drives\. \([https\://github\.com/dell/dellemc\-openmanage\-ansible\-modules/issues](https\://github\.com/dell/dellemc\-openmanage\-ansible\-modules/issues) /713\)

<a id="f5networks-f5-modules-1"></a>
#### f5networks\.f5\_modules

* bigip\_firewall\_address\_list to support both cidr and route domain
* bigip\_profile\_server\_ssl to support parent\'s \[None\, \"\"\, \"None\"\] profiles

<a id="fortinet-fortios-1"></a>
#### fortinet\.fortios

* Github Issue
* Mantis Issue

<a id="ibm-storage-virtualize-3"></a>
#### ibm\.storage\_virtualize

* ibm\_svc\_manage\_replication \- Added checks for mutually\-exclusive parameters and policing for updating remote\-copy relationship

<a id="purestorage-flasharray-1"></a>
#### purestorage\.flasharray

* purefa\_dsrole \- Fixed bug with DS role having no group or group base cannot be updated
* purefa\_pgsnap \- Fixed issue with overwrite failing
* purefa\_vg \- Fixed idempotency issue when clearing volume group QoS settings
* purefa\_vg \- Fixed issue with creating non\-QoS volume groups
* purefa\_vlan \- Allow LACP bonds to be subnet interfaces

<a id="vmware-vmware-1"></a>
#### vmware\.vmware

* vms inventory \- fix handling of VMs within VApps

<a id="known-issues-2"></a>
### Known Issues

<a id="community-general-10"></a>
#### community\.general

* reveal\_ansible\_type filter plugin and ansible\_type test plugin \- note that ansible\-core\'s Data Tagging feature implements new aliases\, such as <code>\_AnsibleTaggedStr</code> for <code>str</code>\, <code>\_AnsibleTaggedInt</code> for <code>int</code>\, and <code>\_AnsibleTaggedFloat</code> for <code>float</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9833](https\://github\.com/ansible\-collections/community\.general/pull/9833)\)\.

<a id="dellemc-openmanage-6"></a>
#### dellemc\.openmanage

* idrac\_diagnostics \- Issue\(285322\) \- This module doesn\'t support export of diagnostics file to HTTP and HTTPS share via SOCKS proxy\.
* idrac\_firmware \- Issue\(279282\) \- This module does not support firmware update using HTTP\, HTTPS\, and FTP shares with authentication on iDRAC8\.
* ome\_smart\_fabric\_uplink \- Issue\(186024\) \- The module supported by OpenManage Enterprise Modular\, however it does not allow the creation of multiple uplinks of the same name\. If an uplink is created using the same name as an existing uplink\, then the existing uplink is modified\.

<a id="new-plugins-1"></a>
### New Plugins

<a id="connection"></a>
#### Connection

* community\.general\.wsl \- Run tasks in WSL distribution using wsl\.exe CLI via SSH\.

<a id="new-modules-2"></a>
### New Modules

<a id="cisco-ios-3"></a>
#### cisco\.ios

* cisco\.ios\.ios\_evpn\_ethernet \- Resource module to configure L2VPN EVPN Ethernet Segment\.

<a id="community-postgresql-4"></a>
#### community\.postgresql

* community\.postgresql\.postgresql\_alter\_system \- Change a PostgreSQL server configuration parameter

<a id="ibm-storage-virtualize-4"></a>
#### ibm\.storage\_virtualize

* ibm\.storage\_virtualize\.ibm\_sv\_manage\_flashsystem\_grid \- Manages operations of Flashsystem grid containing multiple Storage Virtualize systems

<a id="unchanged-collections-2"></a>
### Unchanged Collections

* ansible\.posix \(still version 1\.6\.2\)
* ansible\.utils \(still version 5\.1\.2\)
* ansible\.windows \(still version 2\.8\.0\)
* arista\.eos \(still version 10\.1\.1\)
* awx\.awx \(still version 24\.6\.1\)
* azure\.azcollection \(still version 3\.3\.1\)
* check\_point\.mgmt \(still version 6\.4\.0\)
* chocolatey\.chocolatey \(still version 1\.5\.3\)
* cisco\.asa \(still version 6\.1\.0\)
* cisco\.intersight \(still version 2\.0\.20\)
* cisco\.ise \(still version 2\.10\.0\)
* cloud\.common \(still version 4\.0\.0\)
* cloudscale\_ch\.cloud \(still version 2\.4\.1\)
* community\.ciscosmb \(still version 1\.0\.10\)
* community\.crypto \(still version 2\.26\.0\)
* community\.digitalocean \(still version 1\.27\.0\)
* community\.docker \(still version 4\.5\.2\)
* community\.grafana \(still version 2\.1\.0\)
* community\.hashi\_vault \(still version 6\.2\.0\)
* community\.hrobot \(still version 2\.2\.0\)
* community\.libvirt \(still version 1\.3\.1\)
* community\.mongodb \(still version 1\.7\.9\)
* community\.mysql \(still version 3\.13\.0\)
* community\.network \(still version 5\.1\.0\)
* community\.okd \(still version 4\.0\.1\)
* community\.proxysql \(still version 1\.6\.0\)
* community\.rabbitmq \(still version 1\.4\.0\)
* community\.sap\_libs \(still version 1\.4\.2\)
* community\.windows \(still version 2\.4\.0\)
* community\.zabbix \(still version 3\.3\.0\)
* containers\.podman \(still version 1\.16\.3\)
* cyberark\.conjur \(still version 1\.3\.3\)
* cyberark\.pas \(still version 1\.0\.30\)
* dellemc\.enterprise\_sonic \(still version 2\.5\.1\)
* dellemc\.powerflex \(still version 2\.6\.0\)
* dellemc\.unity \(still version 2\.0\.0\)
* fortinet\.fortimanager \(still version 2\.9\.1\)
* google\.cloud \(still version 1\.5\.1\)
* grafana\.grafana \(still version 5\.7\.0\)
* hetzner\.hcloud \(still version 4\.3\.0\)
* ibm\.qradar \(still version 4\.0\.0\)
* ibm\.spectrum\_virtualize \(still version 2\.0\.0\)
* ieisystem\.inmanage \(still version 3\.0\.0\)
* infinidat\.infinibox \(still version 1\.4\.5\)
* infoblox\.nios\_modules \(still version 1\.8\.0\)
* inspur\.ispim \(still version 2\.2\.3\)
* junipernetworks\.junos \(still version 9\.1\.0\)
* kaytus\.ksmanage \(still version 2\.0\.0\)
* kubevirt\.core \(still version 2\.1\.0\)
* netapp\.cloudmanager \(still version 21\.24\.0\)
* netapp\.ontap \(still version 22\.14\.0\)
* netapp\.storagegrid \(still version 21\.14\.0\)
* netapp\_eseries\.santricity \(still version 1\.4\.1\)
* netbox\.netbox \(still version 3\.21\.0\)
* ngine\_io\.cloudstack \(still version 2\.5\.0\)
* openstack\.cloud \(still version 2\.4\.1\)
* ovirt\.ovirt \(still version 3\.2\.0\)
* purestorage\.flashblade \(still version 1\.19\.2\)
* sensu\.sensu\_go \(still version 1\.14\.0\)
* splunk\.es \(still version 4\.0\.0\)
* telekom\_mms\.icinga\_director \(still version 2\.2\.2\)
* theforeman\.foreman \(still version 4\.2\.0\)
* vultr\.cloud \(still version 1\.13\.0\)
* vyos\.vyos \(still version 5\.0\.0\)
* wti\.remote \(still version 1\.0\.10\)

<a id="v11-4-0"></a>
## v11\.4\.0

- <a href="#release-summary-3">Release Summary</a>
- <a href="#ansible-core-6">Ansible\-core</a>
- <a href="#changed-collections-3">Changed Collections</a>
- <a href="#major-changes-3">Major Changes</a>
    - <a href="#community-zabbix">community\.zabbix</a>
- <a href="#minor-changes-3">Minor Changes</a>
    - <a href="#amazon-aws-4">amazon\.aws</a>
    - <a href="#ansible-windows">ansible\.windows</a>
    - <a href="#cisco-dnac-1">cisco\.dnac</a>
    - <a href="#community-aws-2">community\.aws</a>
    - <a href="#community-crypto-3">community\.crypto</a>
    - <a href="#community-docker-2">community\.docker</a>
    - <a href="#community-general-11">community\.general</a>
    - <a href="#community-mysql-2">community\.mysql</a>
    - <a href="#community-postgresql-5">community\.postgresql</a>
    - <a href="#community-routeros-2">community\.routeros</a>
    - <a href="#community-vmware-6">community\.vmware</a>
    - <a href="#community-windows">community\.windows</a>
    - <a href="#community-zabbix-1">community\.zabbix</a>
    - <a href="#hetzner-hcloud">hetzner\.hcloud</a>
    - <a href="#netbox-netbox">netbox\.netbox</a>
- <a href="#breaking-changes--porting-guide">Breaking Changes / Porting Guide</a>
    - <a href="#community-postgresql-6">community\.postgresql</a>
- <a href="#deprecated-features-3">Deprecated Features</a>
    - <a href="#community-vmware-7">community\.vmware</a>
- <a href="#bugfixes-3">Bugfixes</a>
    - <a href="#ansible-core-7">Ansible\-core</a>
    - <a href="#ansible-windows-1">ansible\.windows</a>
    - <a href="#cisco-ios-4">cisco\.ios</a>
    - <a href="#community-aws-3">community\.aws</a>
    - <a href="#community-dns-3">community\.dns</a>
    - <a href="#community-docker-3">community\.docker</a>
    - <a href="#community-general-12">community\.general</a>
    - <a href="#community-mysql-3">community\.mysql</a>
    - <a href="#community-postgresql-7">community\.postgresql</a>
    - <a href="#community-sops-2">community\.sops</a>
    - <a href="#community-vmware-8">community\.vmware</a>
    - <a href="#community-zabbix-2">community\.zabbix</a>
    - <a href="#fortinet-fortimanager">fortinet\.fortimanager</a>
    - <a href="#netbox-netbox-1">netbox\.netbox</a>
- <a href="#new-modules-3">New Modules</a>
    - <a href="#amazon-aws-5">amazon\.aws</a>
    - <a href="#community-general-13">community\.general</a>
    - <a href="#community-hrobot-3">community\.hrobot</a>
    - <a href="#community-zabbix-3">community\.zabbix</a>
    - <a href="#netbox-netbox-2">netbox\.netbox</a>
- <a href="#unchanged-collections-3">Unchanged Collections</a>

<a id="release-summary-3"></a>
### Release Summary

Release Date\: 2025\-03\-25

[Porting Guide](https\://docs\.ansible\.com/ansible/devel/porting\_guides\.html)

<a id="ansible-core-6"></a>
### Ansible\-core

Ansible 11\.4\.0 contains ansible\-core version 2\.18\.4\.
This is a newer version than version 2\.18\.3 contained in the previous Ansible release\.

The changes are reported in the combined changelog below\.

<a id="changed-collections-3"></a>
### Changed Collections

If not mentioned explicitly\, the changes are reported in the combined changelog below\.

| Collection            | Ansible 11.3.0 | Ansible 11.4.0 | Notes                                                                                                                                                                                                        |
| --------------------- | -------------- | -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| amazon.aws            | 9.2.0          | 9.3.0          |                                                                                                                                                                                                              |
| ansible.windows       | 2.7.0          | 2.8.0          |                                                                                                                                                                                                              |
| azure.azcollection    | 3.2.0          | 3.3.1          | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.                                                                                 |
| cisco.dnac            | 6.30.0         | 6.31.0         |                                                                                                                                                                                                              |
| cisco.ios             | 9.1.1          | 9.1.2          |                                                                                                                                                                                                              |
| community.aws         | 9.0.0          | 9.1.0          |                                                                                                                                                                                                              |
| community.crypto      | 2.25.0         | 2.26.0         |                                                                                                                                                                                                              |
| community.dns         | 3.2.1          | 3.2.2          |                                                                                                                                                                                                              |
| community.docker      | 4.4.0          | 4.5.2          |                                                                                                                                                                                                              |
| community.general     | 10.4.0         | 10.5.0         |                                                                                                                                                                                                              |
| community.hrobot      | 2.1.0          | 2.2.0          |                                                                                                                                                                                                              |
| community.mysql       | 3.12.0         | 3.13.0         |                                                                                                                                                                                                              |
| community.postgresql  | 3.10.2         | 3.12.0         |                                                                                                                                                                                                              |
| community.routeros    | 3.4.0          | 3.5.0          |                                                                                                                                                                                                              |
| community.sops        | 2.0.2          | 2.0.3          |                                                                                                                                                                                                              |
| community.vmware      | 5.4.0          | 5.5.0          |                                                                                                                                                                                                              |
| community.windows     | 2.3.0          | 2.4.0          |                                                                                                                                                                                                              |
| community.zabbix      | 3.2.0          | 3.3.0          |                                                                                                                                                                                                              |
| cyberark.conjur       | 1.3.2          | 1.3.3          | You can find the collection's changelog at [https://github.com/cyberark/ansible-conjur-collection/blob/master/CHANGELOG.md](https://github.com/cyberark/ansible-conjur-collection/blob/master/CHANGELOG.md). |
| fortinet.fortimanager | 2.9.0          | 2.9.1          |                                                                                                                                                                                                              |
| hetzner.hcloud        | 4.2.2          | 4.3.0          |                                                                                                                                                                                                              |
| netbox.netbox         | 3.20.0         | 3.21.0         |                                                                                                                                                                                                              |

<a id="major-changes-3"></a>
### Major Changes

<a id="community-zabbix"></a>
#### community\.zabbix

* All Roles \- Updated to support version 7\.2

<a id="minor-changes-3"></a>
### Minor Changes

<a id="amazon-aws-4"></a>
#### amazon\.aws

* s3\_object \- support passing metadata in <code>create</code> mode \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2529](https\://github\.com/ansible\-collections/amazon\.aws/pull/2529)\)\.

<a id="ansible-windows"></a>
#### ansible\.windows

* setup \- Remove dependency on shared function loaded by Ansible
* win\_get\_url \- Added <code>checksum</code> and <code>checksum\_algorithm</code> to verify the package before installation\. Also returns <code>checksum</code> if <code>checksum\_algorithm</code> is provided \- [https\://github\.com/ansible\-collections/ansible\.windows/issues/596](https\://github\.com/ansible\-collections/ansible\.windows/issues/596)

<a id="cisco-dnac-1"></a>
#### cisco\.dnac

* Adding Unit Test automation in github actions
* Changes in device\_credential\_workflow\_manager module
* Changes in network\_settings\_workflow\_manager module
* Changes in provision\_workflow\_manager module
* Changes in sda\_fabric\_site\_zones\_workflow\_manager module
* Changes in sda\_fabric\_virtual\_networks\_workflow\_manager module
* Changes in swim\_workflow\_manager module
* Changes in swim\_workflow\_manager module to support list of images
* Update Readme
* sda\_fabric\_site\_zones\_workflow\_manager \- attributes \'apply\_pending\_events\'\,  \'pre\_auth\_acl\'\, was added

<a id="community-aws-2"></a>
#### community\.aws

* aws\_ssm \-  Refactor <code>\_init\_clients</code> Method for Improved Clarity and Efficiency \([https\://github\.com/ansible\-collections/community\.aws/pull/2223](https\://github\.com/ansible\-collections/community\.aws/pull/2223)\)\.
* aws\_ssm \-  Refactor <code>\_prepare\_terminal\(\)</code> Method for Improved Clarity and Efficiency \([https\://github\.com/ansible\-collections/community\.aws/pull/](https\://github\.com/ansible\-collections/community\.aws/pull/)\)\.
* aws\_ssm \-  Refactor exec\_command Method for Improved Clarity and Efficiency \([https\://github\.com/ansible\-collections/community\.aws/pull/2224](https\://github\.com/ansible\-collections/community\.aws/pull/2224)\)\.
* aws\_ssm \- Add the possibility to define <code>aws\_ssm plugin</code> variable via environment variable and by default use the version found on the \$PATH rather than require that you provide an absolute path \([https\://github\.com/ansible\-collections/community\.aws/issues/1990](https\://github\.com/ansible\-collections/community\.aws/issues/1990)\)\.
* aws\_ssm \- add function to generate random strings for SSM CLI delimitation \([https\://github\.com/ansible\-collections/community\.aws/pull/2235](https\://github\.com/ansible\-collections/community\.aws/pull/2235)\)\.
* dms\_endpoint \- improve resilience of parameter comparison \([https\://github\.com/ansible\-collections/community\.aws/pull/2221](https\://github\.com/ansible\-collections/community\.aws/pull/2221)\)\.
* s3\_lifecycle \- Support for min and max object size when applying the filter rules \([https\://github\.com/ansible\-collections/community\.aws/pull/2205](https\://github\.com/ansible\-collections/community\.aws/pull/2205)\)\.
* various modules \- linting fixups \([https\://github\.com/ansible\-collections/community\.aws/pull/2221](https\://github\.com/ansible\-collections/community\.aws/pull/2221)\)\.
* waf\_condition \- adds missing options validation to filters \([https\://github\.com/ansible\-collections/community\.aws/pull/2220](https\://github\.com/ansible\-collections/community\.aws/pull/2220)\)\.

<a id="community-crypto-3"></a>
#### community\.crypto

* openssl\_pkcs12 \- the module now supports <code>certificate\_content</code>/<code>other\_certificates\_content</code> for cases where the data already exists in memory and not yet in a file \([https\://github\.com/ansible\-collections/community\.crypto/issues/847](https\://github\.com/ansible\-collections/community\.crypto/issues/847)\, [https\://github\.com/ansible\-collections/community\.crypto/pull/848](https\://github\.com/ansible\-collections/community\.crypto/pull/848)\)\.

<a id="community-docker-2"></a>
#### community\.docker

* docker\_compose\_v2 \- add <code>assume\_yes</code> parameter for <code>docker compose up</code> \([https\://github\.com/ansible\-collections/community\.docker/pull/1045](https\://github\.com/ansible\-collections/community\.docker/pull/1045)\)\.
* docker\_network \- add <code>enable\_ipv4</code> option \([https\://github\.com/ansible\-collections/community\.docker/issues/1047](https\://github\.com/ansible\-collections/community\.docker/issues/1047)\, [https\://github\.com/ansible\-collections/community\.docker/pull/1049](https\://github\.com/ansible\-collections/community\.docker/pull/1049)\)\.

<a id="community-general-11"></a>
#### community\.general

* CmdRunner module utils \- the convenience method <code>cmd\_runner\_fmt\.as\_fixed\(\)</code> now accepts multiple arguments as a list \([https\://github\.com/ansible\-collections/community\.general/pull/9893](https\://github\.com/ansible\-collections/community\.general/pull/9893)\)\.
* apache2\_mod\_proxy \- code simplification\, no change in functionality \([https\://github\.com/ansible\-collections/community\.general/pull/9457](https\://github\.com/ansible\-collections/community\.general/pull/9457)\)\.
* consul\_token \- fix idempotency when <code>policies</code> or <code>roles</code> are supplied by name \([https\://github\.com/ansible\-collections/community\.general/issues/9841](https\://github\.com/ansible\-collections/community\.general/issues/9841)\, [https\://github\.com/ansible\-collections/community\.general/pull/9845](https\://github\.com/ansible\-collections/community\.general/pull/9845)\)\.
* keycloak\_realm \- remove ID requirement when creating a realm to allow Keycloak generating its own realm ID \([https\://github\.com/ansible\-collections/community\.general/pull/9768](https\://github\.com/ansible\-collections/community\.general/pull/9768)\)\.
* nmap inventory plugin \- adds <code>dns\_servers</code> option for specifying DNS servers for name resolution\. Accepts hostnames or IP addresses in the same format as the <code>exclude</code> option \([https\://github\.com/ansible\-collections/community\.general/pull/9849](https\://github\.com/ansible\-collections/community\.general/pull/9849)\)\.
* proxmox\_kvm \- add missing audio hardware device handling \([https\://github\.com/ansible\-collections/community\.general/issues/5192](https\://github\.com/ansible\-collections/community\.general/issues/5192)\, [https\://github\.com/ansible\-collections/community\.general/pull/9847](https\://github\.com/ansible\-collections/community\.general/pull/9847)\)\.
* redfish\_config \- add command <code>SetPowerRestorePolicy</code> to set the desired power state of the system when power is restored \([https\://github\.com/ansible\-collections/community\.general/pull/9837](https\://github\.com/ansible\-collections/community\.general/pull/9837)\)\.
* redfish\_info \- add command <code>GetPowerRestorePolicy</code> to get the desired power state of the system when power is restored \([https\://github\.com/ansible\-collections/community\.general/pull/9824](https\://github\.com/ansible\-collections/community\.general/pull/9824)\)\.
* rocketchat \- option <code>is\_pre740</code> has been added to control the format of the payload\. For Rocket\.Chat 7\.4\.0 or newer\, it must be set to <code>false</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9882](https\://github\.com/ansible\-collections/community\.general/pull/9882)\)\.
* slack callback plugin \- add <code>http\_agent</code> option to enable the user to set a custom user agent for slack callback plugin \([https\://github\.com/ansible\-collections/community\.general/issues/9813](https\://github\.com/ansible\-collections/community\.general/issues/9813)\, [https\://github\.com/ansible\-collections/community\.general/pull/9836](https\://github\.com/ansible\-collections/community\.general/pull/9836)\)\.
* systemd\_info \- add wildcard expression support in <code>unitname</code> option \([https\://github\.com/ansible\-collections/community\.general/pull/9821](https\://github\.com/ansible\-collections/community\.general/pull/9821)\)\.
* systemd\_info \- extend support to timer units \([https\://github\.com/ansible\-collections/community\.general/pull/9891](https\://github\.com/ansible\-collections/community\.general/pull/9891)\)\.
* vmadm \- add new options <code>flexible\_disk\_size</code> and <code>owner\_uuid</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9892](https\://github\.com/ansible\-collections/community\.general/pull/9892)\)\.

<a id="community-mysql-2"></a>
#### community\.mysql

* Integration tests for MariaDB 11\.4 have replaced those for 10\.5\. The previous version is now 10\.11\.
* mysql\_user \- add <code>locked</code> option to lock/unlock users\, this is mainly used to have users that will act as definers on stored procedures\.

<a id="community-postgresql-5"></a>
#### community\.postgresql

* postgresql\_pg\_hba \- adds \'pg\_hba\_string\' which contains the string that is written to the file to the output of the module \([https\://github\.com/ansible\-collections/community\.postgresql/pull/778](https\://github\.com/ansible\-collections/community\.postgresql/pull/778)\)
* postgresql\_pg\_hba \- adds a parameter \'sort\_rules\' that allows the user to disable sorting in the module\, the default is the previous behavior \([https\://github\.com/ansible\-collections/community\.postgresql/pull/778](https\://github\.com/ansible\-collections/community\.postgresql/pull/778)\)
* postgresql\_pg\_hba \- regarding \#795 will read all kinds of includes and add them to the end of the file in the same order as they were in the original file\, does not allow to add includes \([https\://github\.com/ansible\-collections/community\.postgresql/pull/778](https\://github\.com/ansible\-collections/community\.postgresql/pull/778)\)
* postgresql\_publication \- added <code>rowfilters</code> parameter that adds support for row filtering on PG publications \([https\://github\.com/ansible\-collections/community\.postgresql/pull/813](https\://github\.com/ansible\-collections/community\.postgresql/pull/813)\)
* postgresql\_user \- now there is a <code>quote\_configuration\_values</code> parameter that allows to turn off quoting for values which when set to <code>false</code> allows to set <code>search\_path</code> \([https\://github\.com/ansible\-collections/community\.postgresql/pull/806](https\://github\.com/ansible\-collections/community\.postgresql/pull/806)\)

<a id="community-routeros-2"></a>
#### community\.routeros

* api\_info\, api\_modify \- change default for <code>/ip/cloud/ddns\-enabled</code> for RouterOS 7\.17 and newer from <code>yes</code> to <code>auto</code> \([https\://github\.com/ansible\-collections/community\.routeros/pull/350](https\://github\.com/ansible\-collections/community\.routeros/pull/350)\)\.

<a id="community-vmware-6"></a>
#### community\.vmware

* vcenter\_standard\_key\_provider \- Drop unused HAS\_PYVMOMI \([https\://github\.com/ansible\-collections/community\.vmware/pull/2327](https\://github\.com/ansible\-collections/community\.vmware/pull/2327)\)\.
* vmware\_category \- Don\'t test for vSphere \< 7 anymore \([https\://github\.com/ansible\-collections/community\.vmware/pull/2326](https\://github\.com/ansible\-collections/community\.vmware/pull/2326)\)\.
* vmware\_guest \- Drop unused HAS\_PYVMOMI \([https\://github\.com/ansible\-collections/community\.vmware/pull/2327](https\://github\.com/ansible\-collections/community\.vmware/pull/2327)\)\.
* vmware\_guest\_storage\_policy \- Drop unnecessary HAS\_PYVMOMI \([https\://github\.com/ansible\-collections/community\.vmware/pull/2328](https\://github\.com/ansible\-collections/community\.vmware/pull/2328)\)\.
* vmware\_guest\_tpm \- Drop unused HAS\_PYVMOMI \([https\://github\.com/ansible\-collections/community\.vmware/pull/2327](https\://github\.com/ansible\-collections/community\.vmware/pull/2327)\)\.
* vmware\_host\_graphics \- Drop unnecessary HAS\_PYVMOMI \([https\://github\.com/ansible\-collections/community\.vmware/pull/2328](https\://github\.com/ansible\-collections/community\.vmware/pull/2328)\)\.
* vmware\_host\_lockdown \- Drop unnecessary HAS\_PYVMOMI \([https\://github\.com/ansible\-collections/community\.vmware/pull/2328](https\://github\.com/ansible\-collections/community\.vmware/pull/2328)\)\.
* vmware\_host\_lockdown\_exceptions \- Drop unnecessary HAS\_PYVMOMI \([https\://github\.com/ansible\-collections/community\.vmware/pull/2328](https\://github\.com/ansible\-collections/community\.vmware/pull/2328)\)\.
* vmware\_host\_snmp \- Drop unnecessary HAS\_PYVMOMI \([https\://github\.com/ansible\-collections/community\.vmware/pull/2328](https\://github\.com/ansible\-collections/community\.vmware/pull/2328)\)\.
* vmware\_migrate\_vmk \- Drop unnecessary HAS\_PYVMOMI \([https\://github\.com/ansible\-collections/community\.vmware/pull/2328](https\://github\.com/ansible\-collections/community\.vmware/pull/2328)\)\.
* vmware\_migrate\_vmk \- Inherit from / sub\-class PyVmomi \([https\://github\.com/ansible\-collections/community\.vmware/pull/2324](https\://github\.com/ansible\-collections/community\.vmware/pull/2324)\)\.
* vmware\_resource\_pool \- Drop unnecessary HAS\_PYVMOMI \([https\://github\.com/ansible\-collections/community\.vmware/pull/2328](https\://github\.com/ansible\-collections/community\.vmware/pull/2328)\)\.
* vmware\_vc\_infraprofile\_info \- Don\'t test for vSphere \< 7 anymore \([https\://github\.com/ansible\-collections/community\.vmware/pull/2326](https\://github\.com/ansible\-collections/community\.vmware/pull/2326)\)\.
* vmware\_vm\_config\_option \- Drop unused HAS\_PYVMOMI \([https\://github\.com/ansible\-collections/community\.vmware/pull/2327](https\://github\.com/ansible\-collections/community\.vmware/pull/2327)\)\.
* vmware\_vm\_vss\_dvs\_migrate \- Inherit from / sub\-class PyVmomi \([https\://github\.com/ansible\-collections/community\.vmware/pull/2325](https\://github\.com/ansible\-collections/community\.vmware/pull/2325)\)\.
* vmware\_vsan\_health\_info \- Drop unused HAS\_PYVMOMI \([https\://github\.com/ansible\-collections/community\.vmware/pull/2327](https\://github\.com/ansible\-collections/community\.vmware/pull/2327)\)\.

<a id="community-windows"></a>
#### community\.windows

* Added support for Windows Server 2025
* This issue fixes installation of requirements as it requires a confirmation when installed as a depedency to PowershellGet\. Installing it by itself prevents this confirmation dialog and allows required components to be installed \([https\://github\.com/ansible\-collections/community\.windows/issues/147](https\://github\.com/ansible\-collections/community\.windows/issues/147)\)\.
* win\_file\_version \- Add file\_version\_raw result for cases where file\_version might be empty or in not in the right format\.
* win\_iis\_webapppool  \- this pull request fixes the portion where building an app pool with the word \"value\" in it fails unexpectedly\. [https\://github\.com/ansible\-collections/community\.windows/issues/410](https\://github\.com/ansible\-collections/community\.windows/issues/410)\.
* win\_psrepository\_copy \- Add Force option that deletes repositories that are not present in the source

<a id="community-zabbix-1"></a>
#### community\.zabbix

* added support for Zabbix 7\.2 for all modules
* zabbix\_action module \- added Add host tags and Remove host tags operations
* zabbix\_action module fixed SNMP discovery check condition in discovery rule\.
* zabbix\_agent role \- accept several IPs in <em class="title-reference">zabbix\_agent\_listenip</em> variable\.
* zabbix\_connector module added
* zabbix\_discoveryrule \- add support for renaming discoveryrules
* zabbix\_group\_events\_info \- add tag support
* zabbix\_item \- add support for renaming items
* zabbix\_itemprototype \- add support for renaming itemprototypes
* zabbix\_maintenance \- Added ability to append host or host groups to existing maintenance\.
* zabbix\_mediatype module \- fix failure that started to happen since Zabbix 7\.0\.9
* zabbix\_proxy role \- fix Zabbix proxy creation/update at Zabbix \>\= 7\.0
* zabbix\_proxy role \- fix Zabbix proxy creation/update at Zabbix server when PSK used
* zabbix\_regexp\_info module added
* zabbix\_settings \- add support for additional timeout settings
* zabbix\_settings \- allow setting <code>auditlog\_mode</code> on Zabbix 7\.0 or higher\. With this setting you can enable or disable audit logging of system actions\.
* zabbix\_trigger \- add support for renaming triggers
* zabbix\_triggerprototype \- add support for renaming triggerprototypes

<a id="hetzner-hcloud"></a>
#### hetzner\.hcloud

* server \- Add <em class="title-reference">created</em> state that creates a server but do not start it\.

<a id="netbox-netbox"></a>
#### netbox\.netbox

* Add <em class="title-reference">label</em>\, <em class="title-reference">description</em> and <em class="title-reference">enabled</em> to <em class="title-reference">netbox\_device\_interface\_template</em> \([https\://github\.com/netbox\-community/ansible\_modules/issues/1333](https\://github\.com/netbox\-community/ansible\_modules/issues/1333)\)
* Add example for using ansible variables in lookup
* Add name as option to netbox\_fhrp\_group
* Add support for custom headers
* netbox\_cluster \- Add options scope and scope\_type for NetBox 4\.2\+
* netbox\_device\_interface \- Add primary\_mac\_address option for NetBox 4\.2\+
* netbox\_prefix \- Add options scope and scope\_type for NetBox 4\.2\+
* netbox\_vm\_interface \- Add primary\_mac\_address option for NetBox 4\.2\+

<a id="breaking-changes--porting-guide"></a>
### Breaking Changes / Porting Guide

<a id="community-postgresql-6"></a>
#### community\.postgresql

* postgresql\_info \- the <code>db</code> alias is deprecated and will be removed in the next major release\, use the <code>login\_db</code> argument instead\.
* postgresql\_pg\_hba \- regarding \#776 \'keep\_comments\_at\_rules\' has been deprecated and won\'t do anything\, the default is to keep the comments at the rules they are specified with\. keep\_comments\_at\_rules will be removed in 5\.0\.0 \([https\://github\.com/ansible\-collections/community\.postgresql/pull/778](https\://github\.com/ansible\-collections/community\.postgresql/pull/778)\)
* postgresql\_user \- the <code>db</code> alias is deprecated and will be removed in the next major release\, use the <code>login\_db</code> argument instead\.

<a id="deprecated-features-3"></a>
### Deprecated Features

<a id="community-vmware-7"></a>
#### community\.vmware

* vcenter\_folder \- the module has been deprecated and will be removed in community\.vmware 7\.0\.0 \([https\://github\.com/ansible\-collections/community\.vmware/pull/2340](https\://github\.com/ansible\-collections/community\.vmware/pull/2340)\)\.
* vmware\_cluster\_ha \- the module has been deprecated and will be removed in community\.vmware 7\.0\.0 \([https\://github\.com/ansible\-collections/community\.vmware/pull/2321](https\://github\.com/ansible\-collections/community\.vmware/pull/2321)\)\.
* vmware\_content\_deploy\_ovf\_template \- the module has been deprecated and will be removed in community\.vmware 7\.0\.0 \([https\://github\.com/ansible\-collections/community\.vmware/pull/2332](https\://github\.com/ansible\-collections/community\.vmware/pull/2332)\)\.
* vmware\_content\_deploy\_template \- the module has been deprecated and will be removed in community\.vmware 7\.0\.0 \([https\://github\.com/ansible\-collections/community\.vmware/pull/2332](https\://github\.com/ansible\-collections/community\.vmware/pull/2332)\)\.
* vmware\_content\_library\_manager \- the module has been deprecated and will be removed in community\.vmware 7\.0\.0 \([https\://github\.com/ansible\-collections/community\.vmware/pull/2345](https\://github\.com/ansible\-collections/community\.vmware/pull/2345)\)\.
* vmware\_host \- the module has been deprecated and will be removed in community\.vmware 7\.0\.0 \([https\://github\.com/ansible\-collections/community\.vmware/pull/2337](https\://github\.com/ansible\-collections/community\.vmware/pull/2337)\)\.

<a id="bugfixes-3"></a>
### Bugfixes

<a id="ansible-core-7"></a>
#### Ansible\-core

* Windows \- add support for running on system where WDAC is in audit mode with <code>Dynamic Code Security</code> enabled\.
* dnf5 \- fix <code>is\_installed</code> check for packages that are not installed but listed as provided by an installed package \([https\://github\.com/ansible/ansible/issues/84578](https\://github\.com/ansible/ansible/issues/84578)\)
* dnf5 \- libdnf5 \- use <code>conf\.pkg\_gpgcheck</code> instead of deprecated <code>conf\.gpgcheck</code> which is used only as a fallback
* facts \- gather pagesize and calculate respective values depending upon architecture \([https\://github\.com/ansible/ansible/issues/84773](https\://github\.com/ansible/ansible/issues/84773)\)\.
* module respawn \- limit to supported Python versions

<a id="ansible-windows-1"></a>
#### ansible\.windows

* setup \- Add better detection for VMWare base virtualization platforms \- [https\://github\.com/ansible\-collections/ansible\.windows/issues/753](https\://github\.com/ansible\-collections/ansible\.windows/issues/753)
* win\_package \- Support check mode with local file path sources

<a id="cisco-ios-4"></a>
#### cisco\.ios

* ios\_acls \- Fixed issue where cisco\.ios\.ios\_acls module failed to process IPv6 ACL remarks\, causing unsupported parameter errors\.
* ios\_route\_maps \- Fixes an issue where \'no description value\' is an invalid command on the latest devices\.

<a id="community-aws-3"></a>
#### community\.aws

* aws\_ssm \- use <code>head\_bucket</code> to access bucket locations in foreign aws accounts \([https\://github\.com/ansible\-collections/community\.aws/pull/1987](https\://github\.com/ansible\-collections/community\.aws/pull/1987)\)\.
* ssm \- strip Powershell CLIXML from stdout \([https\://github\.com/ansible\-collections/community\.aws/issues/1952](https\://github\.com/ansible\-collections/community\.aws/issues/1952)\)\.

<a id="community-dns-3"></a>
#### community\.dns

* Update Public Suffix List\.

<a id="community-docker-3"></a>
#### community\.docker

* docker\_compose\_v2 \- fix version check for <code>assume\_yes</code> \([https\://github\.com/ansible\-collections/community\.docker/pull/1054](https\://github\.com/ansible\-collections/community\.docker/pull/1054)\)\.
* docker\_compose\_v2 \- rename flag for <code>assume\_yes</code> parameter for <code>docker compose up</code> to <code>\-y</code> \([https\://github\.com/ansible\-collections/community\.docker/pull/1054](https\://github\.com/ansible\-collections/community\.docker/pull/1054)\)\.
* docker\_compose\_v2 \- use <code>\-\-yes</code> instead of <code>\-y</code> from Docker Compose 2\.34\.0 on \([https\://github\.com/ansible\-collections/community\.docker/pull/1060](https\://github\.com/ansible\-collections/community\.docker/pull/1060)\)\.

<a id="community-general-12"></a>
#### community\.general

* cloudlare\_dns \- handle exhausted response stream in case of HTTP errors to show nice error message to the user \([https\://github\.com/ansible\-collections/community\.general/issues/9782](https\://github\.com/ansible\-collections/community\.general/issues/9782)\, [https\://github\.com/ansible\-collections/community\.general/pull/9818](https\://github\.com/ansible\-collections/community\.general/pull/9818)\)\.
* dnf\_versionlock \- add support for dnf5 \([https\://github\.com/ansible\-collections/community\.general/issues/9556](https\://github\.com/ansible\-collections/community\.general/issues/9556)\)\.
* homebrew \- fix crash when package names include tap \([https\://github\.com/ansible\-collections/community\.general/issues/9777](https\://github\.com/ansible\-collections/community\.general/issues/9777)\, [https\://github\.com/ansible\-collections/community\.general/pull/9803](https\://github\.com/ansible\-collections/community\.general/pull/9803)\)\.
* homebrew\_cask \- handle unusual brew version strings \([https\://github\.com/ansible\-collections/community\.general/issues/8432](https\://github\.com/ansible\-collections/community\.general/issues/8432)\, [https\://github\.com/ansible\-collections/community\.general/pull/9881](https\://github\.com/ansible\-collections/community\.general/pull/9881)\)\.
* nmcli \- enable changing only the order of DNS servers or search suffixes \([https\://github\.com/ansible\-collections/community\.general/issues/8724](https\://github\.com/ansible\-collections/community\.general/issues/8724)\, [https\://github\.com/ansible\-collections/community\.general/pull/9880](https\://github\.com/ansible\-collections/community\.general/pull/9880)\)\.
* proxmox \- add missing key selection of <code>\'status\'</code> key to <code>get\_lxc\_status</code> \([https\://github\.com/ansible\-collections/community\.general/issues/9696](https\://github\.com/ansible\-collections/community\.general/issues/9696)\, [https\://github\.com/ansible\-collections/community\.general/pull/9809](https\://github\.com/ansible\-collections/community\.general/pull/9809)\)\.
* proxmox\_vm\_info \- the module no longer expects that the key <code>template</code> exists in a dictionary returned by Proxmox \([https\://github\.com/ansible\-collections/community\.general/issues/9875](https\://github\.com/ansible\-collections/community\.general/issues/9875)\, [https\://github\.com/ansible\-collections/community\.general/pull/9910](https\://github\.com/ansible\-collections/community\.general/pull/9910)\)\.
* sudoers \- display stdout and stderr raised while failed validation \([https\://github\.com/ansible\-collections/community\.general/issues/9674](https\://github\.com/ansible\-collections/community\.general/issues/9674)\, [https\://github\.com/ansible\-collections/community\.general/pull/9871](https\://github\.com/ansible\-collections/community\.general/pull/9871)\)\.

<a id="community-mysql-3"></a>
#### community\.mysql

* mysql\_db \- fix dump and import to find MariaDB binaries \(mariadb and mariadb\-dump\) when MariaDB 11\+ is used and symbolic links to MySQL binaries are absent\.

<a id="community-postgresql-7"></a>
#### community\.postgresql

* postgresql\_pg\_hba \- fixes \#776 the module won\'t be adding/moving comments repeatedly if \'keep\_comments\_at\_rules\' is \'false\' \([https\://github\.com/ansible\-collections/community\.postgresql/pull/778](https\://github\.com/ansible\-collections/community\.postgresql/pull/778)\)

<a id="community-sops-2"></a>
#### community\.sops

* install role \- <code>sops\_install\_on\_localhost\=false</code> was not working properly if the role was running on more than one host due to a bug in ansible\-core \([https\://github\.com/ansible\-collections/community\.sops/issues/223](https\://github\.com/ansible\-collections/community\.sops/issues/223)\, [https\://github\.com/ansible\-collections/community\.sops/pull/224](https\://github\.com/ansible\-collections/community\.sops/pull/224)\)\.

<a id="community-vmware-8"></a>
#### community\.vmware

* vmware\_object\_role\_permission \- The module ignores changing <code>recursive</code> \([https\://github\.com/ansible\-collections/community\.vmware/pull/2350](https\://github\.com/ansible\-collections/community\.vmware/pull/2350)\)\.

<a id="community-zabbix-2"></a>
#### community\.zabbix

* Java Gateway Role \- Temporary work around to solve failure on RHEL9\.
* zabbix inventory plugin \- do not require <code>login\_user</code> and <code>login\_password</code> to be present when <code>auth\_token</code> is provided \([https\://github\.com/ansible\-collections/community\.zabbix/pull/1439](https\://github\.com/ansible\-collections/community\.zabbix/pull/1439)\)\.

<a id="fortinet-fortimanager"></a>
#### fortinet\.fortimanager

* Changed the default playbook examples for each module to pass ansible\-lint\.
* Corrected mainkey of some modules\.

<a id="netbox-netbox-1"></a>
#### netbox\.netbox

* Fix missing netbox\_config\_template module in module\_defaults
* Fixed an isssue with module\_default parameter inheritance for modules netbox\_config\_template\, netbox\_custom\_field\_choice\_set\, netbox\_permission\, netbox\_token\, netbox\_user\, and netbox\_user\_group\.
* fix call /api/status/ instead /api/status in nb\_inventory plugin\. \([https\://github\.com/netbox\-community/ansible\_modules/issues/1335](https\://github\.com/netbox\-community/ansible\_modules/issues/1335)\)\.
* netbox\_ip\_address \- Fixed the problem preventing assignment of an IP address to a network interface

<a id="new-modules-3"></a>
### New Modules

<a id="amazon-aws-5"></a>
#### amazon\.aws

* amazon\.aws\.ec2\_dedicated\_host \- Create\, update or delete \(release\) EC2 dedicated host
* amazon\.aws\.ec2\_dedicated\_host\_info \- Gather information about EC2 Dedicated Hosts in AWS

<a id="community-general-13"></a>
#### community\.general

* community\.general\.pacemaker\_resource \- Manage pacemaker resources\.

<a id="community-hrobot-3"></a>
#### community\.hrobot

* community\.hrobot\.reset\_info \- Query information on the resetter of a dedicated server\.

<a id="community-zabbix-3"></a>
#### community\.zabbix

* community\.zabbix\.zabbix\_connector \- Create/Delete/Update Zabbix connectors
* community\.zabbix\.zabbix\_regexp\_info \- Retrieve Zabbix regular expression

<a id="netbox-netbox-2"></a>
#### netbox\.netbox

* netbox\.netbox\.netbox\_mac\_address \- Create\, update or delete MAC addresses within NetBox

<a id="unchanged-collections-3"></a>
### Unchanged Collections

* ansible\.netcommon \(still version 7\.1\.0\)
* ansible\.posix \(still version 1\.6\.2\)
* ansible\.utils \(still version 5\.1\.2\)
* arista\.eos \(still version 10\.1\.1\)
* awx\.awx \(still version 24\.6\.1\)
* check\_point\.mgmt \(still version 6\.4\.0\)
* chocolatey\.chocolatey \(still version 1\.5\.3\)
* cisco\.aci \(still version 2\.10\.1\)
* cisco\.asa \(still version 6\.1\.0\)
* cisco\.intersight \(still version 2\.0\.20\)
* cisco\.iosxr \(still version 10\.3\.0\)
* cisco\.ise \(still version 2\.10\.0\)
* cisco\.meraki \(still version 2\.20\.8\)
* cisco\.mso \(still version 2\.9\.0\)
* cisco\.nxos \(still version 9\.3\.0\)
* cisco\.ucs \(still version 1\.15\.0\)
* cloud\.common \(still version 4\.0\.0\)
* cloudscale\_ch\.cloud \(still version 2\.4\.1\)
* community\.ciscosmb \(still version 1\.0\.10\)
* community\.digitalocean \(still version 1\.27\.0\)
* community\.grafana \(still version 2\.1\.0\)
* community\.hashi\_vault \(still version 6\.2\.0\)
* community\.library\_inventory\_filtering\_v1 \(still version 1\.0\.2\)
* community\.libvirt \(still version 1\.3\.1\)
* community\.mongodb \(still version 1\.7\.9\)
* community\.network \(still version 5\.1\.0\)
* community\.okd \(still version 4\.0\.1\)
* community\.proxysql \(still version 1\.6\.0\)
* community\.rabbitmq \(still version 1\.4\.0\)
* community\.sap\_libs \(still version 1\.4\.2\)
* containers\.podman \(still version 1\.16\.3\)
* cyberark\.pas \(still version 1\.0\.30\)
* dellemc\.enterprise\_sonic \(still version 2\.5\.1\)
* dellemc\.openmanage \(still version 9\.10\.0\)
* dellemc\.powerflex \(still version 2\.6\.0\)
* dellemc\.unity \(still version 2\.0\.0\)
* f5networks\.f5\_modules \(still version 1\.34\.1\)
* fortinet\.fortios \(still version 2\.3\.9\)
* google\.cloud \(still version 1\.5\.1\)
* grafana\.grafana \(still version 5\.7\.0\)
* ibm\.qradar \(still version 4\.0\.0\)
* ibm\.spectrum\_virtualize \(still version 2\.0\.0\)
* ibm\.storage\_virtualize \(still version 2\.6\.0\)
* ieisystem\.inmanage \(still version 3\.0\.0\)
* infinidat\.infinibox \(still version 1\.4\.5\)
* infoblox\.nios\_modules \(still version 1\.8\.0\)
* inspur\.ispim \(still version 2\.2\.3\)
* junipernetworks\.junos \(still version 9\.1\.0\)
* kaytus\.ksmanage \(still version 2\.0\.0\)
* kubernetes\.core \(still version 5\.1\.0\)
* kubevirt\.core \(still version 2\.1\.0\)
* lowlydba\.sqlserver \(still version 2\.5\.0\)
* microsoft\.ad \(still version 1\.8\.0\)
* netapp\.cloudmanager \(still version 21\.24\.0\)
* netapp\.ontap \(still version 22\.14\.0\)
* netapp\.storagegrid \(still version 21\.14\.0\)
* netapp\_eseries\.santricity \(still version 1\.4\.1\)
* ngine\_io\.cloudstack \(still version 2\.5\.0\)
* openstack\.cloud \(still version 2\.4\.1\)
* ovirt\.ovirt \(still version 3\.2\.0\)
* purestorage\.flasharray \(still version 1\.33\.1\)
* purestorage\.flashblade \(still version 1\.19\.2\)
* sensu\.sensu\_go \(still version 1\.14\.0\)
* splunk\.es \(still version 4\.0\.0\)
* telekom\_mms\.icinga\_director \(still version 2\.2\.2\)
* theforeman\.foreman \(still version 4\.2\.0\)
* vmware\.vmware \(still version 1\.10\.1\)
* vmware\.vmware\_rest \(still version 4\.6\.0\)
* vultr\.cloud \(still version 1\.13\.0\)
* vyos\.vyos \(still version 5\.0\.0\)
* wti\.remote \(still version 1\.0\.10\)

<a id="v11-3-0"></a>
## v11\.3\.0

- <a href="#release-summary-4">Release Summary</a>
- <a href="#ansible-core-8">Ansible\-core</a>
- <a href="#changed-collections-4">Changed Collections</a>
- <a href="#minor-changes-4">Minor Changes</a>
    - <a href="#ansible-core-9">Ansible\-core</a>
    - <a href="#amazon-aws-6">amazon\.aws</a>
    - <a href="#arista-eos">arista\.eos</a>
    - <a href="#check-point-mgmt-1">check\_point\.mgmt</a>
    - <a href="#cisco-dnac-2">cisco\.dnac</a>
    - <a href="#community-crypto-4">community\.crypto</a>
    - <a href="#community-dns-4">community\.dns</a>
    - <a href="#community-general-14">community\.general</a>
    - <a href="#community-routeros-3">community\.routeros</a>
    - <a href="#community-vmware-9">community\.vmware</a>
    - <a href="#fortinet-fortimanager-1">fortinet\.fortimanager</a>
    - <a href="#netapp-ontap">netapp\.ontap</a>
    - <a href="#netapp-storagegrid">netapp\.storagegrid</a>
    - <a href="#purestorage-flasharray-2">purestorage\.flasharray</a>
    - <a href="#vmware-vmware-2">vmware\.vmware</a>
- <a href="#deprecated-features-4">Deprecated Features</a>
    - <a href="#community-general-15">community\.general</a>
    - <a href="#community-vmware-10">community\.vmware</a>
- <a href="#bugfixes-4">Bugfixes</a>
    - <a href="#ansible-core-10">Ansible\-core</a>
    - <a href="#amazon-aws-7">amazon\.aws</a>
    - <a href="#arista-eos-1">arista\.eos</a>
    - <a href="#cisco-ios-5">cisco\.ios</a>
    - <a href="#cisco-meraki-4">cisco\.meraki</a>
    - <a href="#community-dns-5">community\.dns</a>
    - <a href="#community-docker-4">community\.docker</a>
    - <a href="#community-general-16">community\.general</a>
    - <a href="#community-routeros-4">community\.routeros</a>
    - <a href="#community-sops-3">community\.sops</a>
    - <a href="#containers-podman-1">containers\.podman</a>
    - <a href="#fortinet-fortimanager-2">fortinet\.fortimanager</a>
    - <a href="#google-cloud-1">google\.cloud</a>
    - <a href="#netapp-ontap-1">netapp\.ontap</a>
    - <a href="#purestorage-flasharray-3">purestorage\.flasharray</a>
    - <a href="#vmware-vmware-3">vmware\.vmware</a>
- <a href="#known-issues-3">Known Issues</a>
    - <a href="#purestorage-flasharray-4">purestorage\.flasharray</a>
- <a href="#new-plugins-2">New Plugins</a>
    - <a href="#lookup">Lookup</a>
- <a href="#new-modules-4">New Modules</a>
    - <a href="#amazon-aws-8">amazon\.aws</a>
    - <a href="#check-point-mgmt-2">check\_point\.mgmt</a>
    - <a href="#community-docker-5">community\.docker</a>
    - <a href="#community-general-17">community\.general</a>
    - <a href="#fortinet-fortimanager-3">fortinet\.fortimanager</a>
    - <a href="#infoblox-nios-modules">infoblox\.nios\_modules</a>
    - <a href="#netapp-storagegrid-1">netapp\.storagegrid</a>
    - <a href="#purestorage-flasharray-5">purestorage\.flasharray</a>
- <a href="#unchanged-collections-4">Unchanged Collections</a>

<a id="release-summary-4"></a>
### Release Summary

Release Date\: 2025\-02\-25

[Porting Guide](https\://docs\.ansible\.com/ansible/devel/porting\_guides\.html)

<a id="ansible-core-8"></a>
### Ansible\-core

Ansible 11\.3\.0 contains ansible\-core version 2\.18\.3\.
This is a newer version than version 2\.18\.2 contained in the previous Ansible release\.

The changes are reported in the combined changelog below\.

<a id="changed-collections-4"></a>
### Changed Collections

If not mentioned explicitly\, the changes are reported in the combined changelog below\.

| Collection             | Ansible 11.2.0 | Ansible 11.3.0 | Notes                                                                                                                        |
| ---------------------- | -------------- | -------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| amazon.aws             | 9.1.1          | 9.2.0          |                                                                                                                              |
| arista.eos             | 10.0.1         | 10.1.1         |                                                                                                                              |
| azure.azcollection     | 3.1.0          | 3.2.0          | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
| check_point.mgmt       | 6.2.1          | 6.4.0          |                                                                                                                              |
| cisco.dnac             | 6.28.0         | 6.30.0         |                                                                                                                              |
| cisco.ios              | 9.1.0          | 9.1.1          |                                                                                                                              |
| cisco.meraki           | 2.20.5         | 2.20.8         |                                                                                                                              |
| community.crypto       | 2.24.0         | 2.25.0         |                                                                                                                              |
| community.dns          | 3.1.2          | 3.2.1          |                                                                                                                              |
| community.docker       | 4.3.1          | 4.4.0          |                                                                                                                              |
| community.general      | 10.3.0         | 10.4.0         |                                                                                                                              |
| community.routeros     | 3.3.0          | 3.4.0          |                                                                                                                              |
| community.sops         | 2.0.1          | 2.0.2          |                                                                                                                              |
| community.vmware       | 5.3.0          | 5.4.0          |                                                                                                                              |
| containers.podman      | 1.16.2         | 1.16.3         |                                                                                                                              |
| fortinet.fortimanager  | 2.8.2          | 2.9.0          |                                                                                                                              |
| google.cloud           | 1.5.0          | 1.5.1          |                                                                                                                              |
| infoblox.nios_modules  | 1.7.1          | 1.8.0          |                                                                                                                              |
| netapp.ontap           | 22.13.0        | 22.14.0        |                                                                                                                              |
| netapp.storagegrid     | 21.13.0        | 21.14.0        |                                                                                                                              |
| purestorage.flasharray | 1.32.0         | 1.33.1         |                                                                                                                              |
| vmware.vmware          | 1.9.0          | 1.10.1         |                                                                                                                              |
| vmware.vmware_rest     | 4.5.0          | 4.6.0          | There are no changes recorded in the changelog.                                                                              |

<a id="minor-changes-4"></a>
### Minor Changes

<a id="ansible-core-9"></a>
#### Ansible\-core

* ansible\-test \- Automatically retry HTTP GET/PUT/DELETE requests on exceptions\.
* ansible\-test \- Use Python\'s <code>urllib</code> instead of <code>curl</code> for HTTP requests\.

<a id="amazon-aws-6"></a>
#### amazon\.aws

* autoscaling\_group \- avoid assignment to unused variable in except block \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2464](https\://github\.com/ansible\-collections/amazon\.aws/pull/2464)\)\.
* ec2\_ami \- avoid redefining <code>delete\_snapshot</code> inside <code>DeregisterImage\.do</code> \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2444](https\://github\.com/ansible\-collections/amazon\.aws/pull/2444)\)\.
* ec2\_transit\_gateway \- avoid assignment to unused <code>retry\_decorator</code> variable \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2464](https\://github\.com/ansible\-collections/amazon\.aws/pull/2464)\)\.
* ec2\_vpc\_egress\_igw \- avoid assignment to unused <code>vpc\_id</code> variable \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2464](https\://github\.com/ansible\-collections/amazon\.aws/pull/2464)\)\.
* ec2\_vpc\_nacl \- avoid assignment to unused <code>result</code> variable \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2464](https\://github\.com/ansible\-collections/amazon\.aws/pull/2464)\)\.
* ec2\_vpc\_vpn \- minor linting fixups \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2444](https\://github\.com/ansible\-collections/amazon\.aws/pull/2444)\)\.
* iam\_password\_policy \- avoid assignment to unused variable in except block \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2464](https\://github\.com/ansible\-collections/amazon\.aws/pull/2464)\)\.
* iam\_role \- avoid assignment to unused variable in except block \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2464](https\://github\.com/ansible\-collections/amazon\.aws/pull/2464)\)\.
* inventory/aws\_ec2 \- Support jinja2 expression in <code>hostnames</code> variable\([https\://github\.com/ansible\-collections/amazon\.aws/issues/2402](https\://github\.com/ansible\-collections/amazon\.aws/issues/2402)\)\.
* kms\_key \- avoid assignment to unused variable in except block \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2464](https\://github\.com/ansible\-collections/amazon\.aws/pull/2464)\)\.
* lambda \- avoid assignment to unused <code>architecture</code> variable \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2464](https\://github\.com/ansible\-collections/amazon\.aws/pull/2464)\)\.
* lambda \- avoid assignment to unused <code>required\_by</code> variable \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2464](https\://github\.com/ansible\-collections/amazon\.aws/pull/2464)\)\.
* module\_utils\.\_s3 \- explicitly cast super to the parent type \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2497](https\://github\.com/ansible\-collections/amazon\.aws/pull/2497)\)\.
* module\_utils\.botocore \- avoid assigning unused parts of exc\_info return \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2497](https\://github\.com/ansible\-collections/amazon\.aws/pull/2497)\)\.
* module\_utils\.exceptions \- avoid assigning unused parts of exc\_info return \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2497](https\://github\.com/ansible\-collections/amazon\.aws/pull/2497)\)\.
* module\_utils\.iam \- avoid assignment to unused <code>result</code> variable \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2464](https\://github\.com/ansible\-collections/amazon\.aws/pull/2464)\)\.
* module\_utils\.s3 \- avoid assignment to unused <code>endpoint</code> variable \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2464](https\://github\.com/ansible\-collections/amazon\.aws/pull/2464)\)\.
* plugin\_utils/inventory \- Add <code>filters</code> to list of templatable inventory options \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2379](https\://github\.com/ansible\-collections/amazon\.aws/pull/2379)\)
* route53 \- Add support for type <code>SSHFP</code> records \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2430](https\://github\.com/ansible\-collections/amazon\.aws/pull/2430)\)\.
* route53\_zone \- Add support for enabling DNSSEC signing in a specific hosted zone \([https\://github\.com/ansible\-collections/amazon\.aws/issues/1976](https\://github\.com/ansible\-collections/amazon\.aws/issues/1976)\)\.
* route53\_zone \- avoid assignmenta to unused <code>current\_vpc\_ids</code> and <code>current\_vpc\_regions</code> variables \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2464](https\://github\.com/ansible\-collections/amazon\.aws/pull/2464)\)\.
* s3\_bucket \- avoid assignment to unused variable in except block \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2464](https\://github\.com/ansible\-collections/amazon\.aws/pull/2464)\)\.
* s3\_bucket \- avoid redefining <code>id</code> inside <code>handle\_bucket\_inventory</code> and <code>delete\_bucket\_inventory</code> \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2444](https\://github\.com/ansible\-collections/amazon\.aws/pull/2444)\)\.
* s3\_object \- avoid redefining <code>key\_check</code> inside <code>\_head\_object</code> \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2444](https\://github\.com/ansible\-collections/amazon\.aws/pull/2444)\)\.
* s3\_object \- simplify <code>path\_check</code> logic \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2444](https\://github\.com/ansible\-collections/amazon\.aws/pull/2444)\)\.
* s3\_object \- use the <code>copy</code> rather than <code>copy\_object</code> method when performing an S3 to S3 copy \([https\://github\.com/ansible\-collections/amazon\.aws/issues/2117](https\://github\.com/ansible\-collections/amazon\.aws/issues/2117)\)\.
* s3\_object\_info \- add support to list objects under a specific prefix \([https\://github\.com/ansible\-collections/amazon\.aws/issues/2477](https\://github\.com/ansible\-collections/amazon\.aws/issues/2477)\)\.
* s3\_object\_info \- avoid assignment to unused variable in except block \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2464](https\://github\.com/ansible\-collections/amazon\.aws/pull/2464)\)\.

<a id="arista-eos"></a>
#### arista\.eos

* Adds a new module <em class="title-reference">eos\_vrf\_global</em> in favor of <em class="title-reference">eos\_vrf</em> legacy module to manage VRF global configurations on Arista EOS devices\.

<a id="check-point-mgmt-1"></a>
#### check\_point\.mgmt

* added missing parameters such as \'filter\'\, \'domains\_to\_process\' and \'async\_response\' to the relevant resources modules\.
* check\_point\.mgmt\.cp\_mgmt\_lsm\_cluster \- support additional parameters \(dynamic\-objects\, tags and topology\)
* check\_point\.mgmt\.cp\_mgmt\_lsm\_gateway \- support additional parameters \(device\_id\, dynamic\-objects\, tags and topology\)

<a id="cisco-dnac-2"></a>
#### cisco\.dnac

* Bug fixes in sda\_fabric\_devices\_workflow\_manager
* Bug fixes in sda\_fabric\_transits\_workflow\_manager
* Bug fixes in sda\_fabric\_transits\_workflow\_manager module
* Bug fixes in site\_workflow\_manager module
* Bug fixes in swim\_workflow\_manager module
* Bug fixes in template\_workflow\_manager module
* Bug fixes in user\_role\_workflow\_manager module
* Changes in device\_credential\_workflow\_manager module
* Changes in inventory\_workflow\_manager module
* Changes in ise\_radius\_integration\_workflow\_manager module
* Changes in network\_settings\_workflow\_manager module
* Changes in pnp\_workflow\_manager module
* Changes in provision\_workflow\_manager module
* Changes in sda\_fabric\_virtual\_networks\_workflow\_manager module
* Changes in sda\_host\_port\_onboarding\_workflow\_manager module
* Changes in site\_workflow\_manager module
* Enhancements in provision\_workflow\_manager module
* Some parameters were modified in tag\_member\_v1\_info
* playbooks were added
* sda\_fabric\_devices\_workflow\_manager \- attribute \'route\_distribution\_protocol\' was removed
* site\_workflow\_manager \- attribute \'force\_upload\_floor\_image\' was added
* template\_workflow\_manager \- attribute \'new\_template\_name\' was added

<a id="community-crypto-4"></a>
#### community\.crypto

* luks\_device \- allow passphrases to contain newlines \([https\://github\.com/ansible\-collections/community\.crypto/pull/844](https\://github\.com/ansible\-collections/community\.crypto/pull/844)\)\.

<a id="community-dns-4"></a>
#### community\.dns

* all filter\, inventory\, and lookup plugins\, and plugin utils \- add type hints to all Python 3 only code \([https\://github\.com/ansible\-collections/community\.dns/pull/239](https\://github\.com/ansible\-collections/community\.dns/pull/239)\)\.
* get\_public\_suffix\, get\_registrable\_domain\, remove\_public\_suffix\, and remove\_registrable\_domain filter plugin \- validate parameters\, and correctly handle byte strings when passed for input \([https\://github\.com/ansible\-collections/community\.dns/pull/239](https\://github\.com/ansible\-collections/community\.dns/pull/239)\)\.

<a id="community-general-14"></a>
#### community\.general

* bitwarden lookup plugin \- add new option <code>collection\_name</code> to filter results by collection name\, and new option <code>result\_count</code> to validate number of results \([https\://github\.com/ansible\-collections/community\.general/pull/9728](https\://github\.com/ansible\-collections/community\.general/pull/9728)\)\.
* incus connection plugin \- adds <code>remote\_user</code> and <code>incus\_become\_method</code> parameters for allowing a non\-root user to connect to an Incus instance \([https\://github\.com/ansible\-collections/community\.general/pull/9743](https\://github\.com/ansible\-collections/community\.general/pull/9743)\)\.
* iocage inventory plugin \- the new parameter <code>hooks\_results</code> of the plugin is a list of files inside a jail that provide configuration parameters for the inventory\. The inventory plugin reads the files from the jails and put the contents into the items of created variable <code>iocage\_hooks</code> \([https\://github\.com/ansible\-collections/community\.general/issues/9650](https\://github\.com/ansible\-collections/community\.general/issues/9650)\, [https\://github\.com/ansible\-collections/community\.general/pull/9651](https\://github\.com/ansible\-collections/community\.general/pull/9651)\)\.
* jira \- adds <code>client\_cert</code> and <code>client\_key</code> parameters for supporting client certificate authentification when connecting to Jira \([https\://github\.com/ansible\-collections/community\.general/pull/9753](https\://github\.com/ansible\-collections/community\.general/pull/9753)\)\.
* lldp \- adds <code>multivalues</code> parameter to control behavior when lldpctl outputs an attribute multiple times \([https\://github\.com/ansible\-collections/community\.general/pull/9657](https\://github\.com/ansible\-collections/community\.general/pull/9657)\)\.
* lvg \- add <code>remove\_extra\_pvs</code> parameter to control if ansible should remove physical volumes which are not in the <code>pvs</code> parameter \([https\://github\.com/ansible\-collections/community\.general/pull/9698](https\://github\.com/ansible\-collections/community\.general/pull/9698)\)\.
* lxd connection plugin \- adds <code>remote\_user</code> and <code>lxd\_become\_method</code> parameters for allowing a non\-root user to connect to an LXD instance \([https\://github\.com/ansible\-collections/community\.general/pull/9659](https\://github\.com/ansible\-collections/community\.general/pull/9659)\)\.
* nmcli \- adds VRF support with new <code>type</code> value <code>vrf</code> and new <code>slave\_type</code> value <code>vrf</code> as well as new <code>table</code> parameter \([https\://github\.com/ansible\-collections/community\.general/pull/9658](https\://github\.com/ansible\-collections/community\.general/pull/9658)\, [https\://github\.com/ansible\-collections/community\.general/issues/8014](https\://github\.com/ansible\-collections/community\.general/issues/8014)\)\.
* onepassword\_ssh\_key \- refactor to move code to lookup class \([https\://github\.com/ansible\-collections/community\.general/pull/9633](https\://github\.com/ansible\-collections/community\.general/pull/9633)\)\.
* proxmox\_kvm \- allow hibernation and suspending of VMs \([https\://github\.com/ansible\-collections/community\.general/issues/9620](https\://github\.com/ansible\-collections/community\.general/issues/9620)\, [https\://github\.com/ansible\-collections/community\.general/pull/9653](https\://github\.com/ansible\-collections/community\.general/pull/9653)\)\.
* redfish\_command \- add <code>PowerFullPowerCycle</code> to power command options \([https\://github\.com/ansible\-collections/community\.general/pull/9729](https\://github\.com/ansible\-collections/community\.general/pull/9729)\)\.
* ssh\_config \- add <code>other\_options</code> option \([https\://github\.com/ansible\-collections/community\.general/issues/8053](https\://github\.com/ansible\-collections/community\.general/issues/8053)\, [https\://github\.com/ansible\-collections/community\.general/pull/9684](https\://github\.com/ansible\-collections/community\.general/pull/9684)\)\.
* xen\_orchestra inventory plugin \- add <code>use\_vm\_uuid</code> and <code>use\_host\_uuid</code> boolean options to allow switching over to using VM/Xen name labels instead of UUIDs as item names \([https\://github\.com/ansible\-collections/community\.general/pull/9787](https\://github\.com/ansible\-collections/community\.general/pull/9787)\)\.

<a id="community-routeros-3"></a>
#### community\.routeros

* api\_info\, api\_modify \- add support for the <code>ip dns forwarders</code> path implemented by RouterOS 7\.17 and newer \([https\://github\.com/ansible\-collections/community\.routeros/pull/343](https\://github\.com/ansible\-collections/community\.routeros/pull/343)\)\.

<a id="community-vmware-9"></a>
#### community\.vmware

* vmware\_guest \- Print details about the error message when the returned task result contains \([https\://github\.com/ansible\-collections/community\.vmware/pull/2301](https\://github\.com/ansible\-collections/community\.vmware/pull/2301)\)\.

<a id="fortinet-fortimanager-1"></a>
#### fortinet\.fortimanager

* Supported FortiManager 7\.2\.9\, 7\.4\.6\, 7\.6\.2\. Added 3 new modules\.

<a id="netapp-ontap"></a>
#### netapp\.ontap

* Multiple modules \- Standardize hostname\, username\, and password parameters to use netapp\_hostname\, netapp\_username\, and netapp\_password as values\.
* Multiple modules \- Update examples to use Fully Qualified Collection Name\.
* Update dead link in doc\_fragments\.
* na\_ontap\_dns \- updated documentation for <em class="title-reference">vserver</em>\.
* na\_ontap\_flexcache \- new options <em class="title-reference">relative\_size</em>\, <em class="title-reference">override\_encryption</em>\, <em class="title-reference">atime\_scrub</em>\, <em class="title-reference">cifs\_change\_notify\_enabled</em>\, <em class="title-reference">global\_file\_locking\_enabled</em>\, <em class="title-reference">guarantee\_type</em>\, <em class="title-reference">dr\_cache</em> added in REST\.
* na\_ontap\_rest\_cli \- Add POST and DELETE examples\.
* na\_ontap\_snapmirror \- new option <em class="title-reference">quiesced\_time\_out</em> added to wait for quiesce job to complete\.
* na\_ontap\_svm \- updated documentation for <em class="title-reference">allowed\_protocols</em> \& <em class="title-reference">services</em>\.
* na\_ontap\_volume \- new option <em class="title-reference">large\_size\_enabled</em> added in REST\, requires ONTAP 9\.12 or later\.

<a id="netapp-storagegrid"></a>
#### netapp\.storagegrid

* na\_sg\_grid\_account \- new option <em class="title-reference">allow\_compliance\_mode</em> and <em class="title-reference">max\_retention\_days</em> added for tenant account\, requires storageGRID 11\.9 or later\.
* na\_sg\_grid\_gateway \- new option <em class="title-reference">enable\_tenant\_manager</em>\, <em class="title-reference">enable\_grid\_manager</em> and <em class="title-reference">node\_type</em> added to support management interfaces\.
* na\_sg\_grid\_group \- new option <em class="title-reference">read\_only</em> added for grid groups\.
* na\_sg\_grid\_info \- LB endpoints and HA group in info module\.
* na\_sg\_org\_group \- new option <em class="title-reference">read\_only</em> added for tenant groups\.

<a id="purestorage-flasharray-2"></a>
#### purestorage\.flasharray

* all \- Minimum <code>py\-pure\-client</code> version increased to 1\.57\.0 due to release of Realms feature
* purefa\_hg \- Added support for Fusion
* purefa\_host \- Added Fusion support
* purefa\_info \- Add performance data for network interfaces
* purefa\_info \- Added new section <code>realms</code>\.
* purefa\_info \- Added new subset <code>fleet</code>
* purefa\_info \- Deprecate <code>network\.\<interface\>\.hwaddr</code> \- replaced by <code>network\.\<interface\>\.mac\_address</code>
* purefa\_info \- Deprecate <code>network\.\<interface\>\.slaves</code> \- replaced by <code>network\.\<interface\>\.subinterfaces</code>
* purefa\_info \- VNC feature deprecated from Purity//FA 6\.8\.0\.
* purefa\_pg \- Added Fusion support\.
* purefa\_pgsched \- Added support for Fusion\.
* purefa\_pgsnap \- Added support for Fusion\.
* purefa\_pod\_replica \- Added Fusion support\.
* purefa\_pods \- Added support for Fusion with <code>context</code> parameter\.
* purefa\_smtp \- Added support for additional parameters\, including encryption mode and email prefixs and email sender name\.
* purefa\_snap \- Added Fusion support\.
* purefa\_vg \- Added support for Fusion
* purefa\_vlan \- Convert to REST v2
* purefa\_vnc \- VNC feature deprecated from Purity//FA 6\.8\.0\.
* purefa\_volume \- Added <code>context</code> parameter to support fleet operations

<a id="vmware-vmware-2"></a>
#### vmware\.vmware

* cluster\_ha \- migrate the vmware\_cluster\_ha module from community to here
* deploy\_content\_library\_ovf \- migrate the vmware\_content\_deploy\_ovf\_template module from community to here
* deploy\_content\_library\_ovf \- update parameters to be consistent with other deploy modules
* deploy\_content\_library\_template \- migrate the vmware\_content\_deploy\_template module from community to here
* deploy\_content\_library\_template \- update parameters to be consistent with other deploy modules
* deploy\_folder\_template \- add module to deploy a vm from a template in a vsphere folder
* esxi\_connection \- migrate the vmware\_host module from community to here
* esxi\_host \- migrate the vmware\_host module from community to here
* folder \- migrate vmware\_folder module from community to here
* local\_content\_library \- migrate the vmware\_content\_library\_manager module from community to here
* subscribed\_content\_library \- migrate the vmware\_content\_library\_manager module from community to here

<a id="deprecated-features-4"></a>
### Deprecated Features

<a id="community-general-15"></a>
#### community\.general

* profitbricks \- module is deprecated and will be removed in community\.general 11\.0\.0 \([https\://github\.com/ansible\-collections/community\.general/pull/9733](https\://github\.com/ansible\-collections/community\.general/pull/9733)\)\.
* profitbricks\_datacenter \- module is deprecated and will be removed in community\.general 11\.0\.0 \([https\://github\.com/ansible\-collections/community\.general/pull/9733](https\://github\.com/ansible\-collections/community\.general/pull/9733)\)\.
* profitbricks\_nic \- module is deprecated and will be removed in community\.general 11\.0\.0 \([https\://github\.com/ansible\-collections/community\.general/pull/9733](https\://github\.com/ansible\-collections/community\.general/pull/9733)\)\.
* profitbricks\_volume \- module is deprecated and will be removed in community\.general 11\.0\.0 \([https\://github\.com/ansible\-collections/community\.general/pull/9733](https\://github\.com/ansible\-collections/community\.general/pull/9733)\)\.
* profitbricks\_volume\_attachments \- module is deprecated and will be removed in community\.general 11\.0\.0 \([https\://github\.com/ansible\-collections/community\.general/pull/9733](https\://github\.com/ansible\-collections/community\.general/pull/9733)\)\.

<a id="community-vmware-10"></a>
#### community\.vmware

* module\_utils\.vmware \- host\_version\_at\_least is deprecated and will be removed in community\.vmware 7\.0\.0 \([https\://github\.com/ansible\-collections/community\.vmware/pull/2303](https\://github\.com/ansible\-collections/community\.vmware/pull/2303)\)\.
* plugin\_utils\.inventory \- this plugin util is deprecated and will be removed in community\.vmware 7\.0\.0 \([https\://github\.com/ansible\-collections/community\.vmware/pull/2304](https\://github\.com/ansible\-collections/community\.vmware/pull/2304)\)\.
* plugins\.httpapi \- this is deprecated and will be removed in community\.vmware 7\.0\.0 \([https\://github\.com/ansible\-collections/community\.vmware/pull/2306](https\://github\.com/ansible\-collections/community\.vmware/pull/2306)\)\.
* vm\_device\_helper\.py \- is\_nvdimm\_controller is deprecated and will be removed in community\.vmware 7\.0\.0 \([https\://github\.com/ansible\-collections/community\.vmware/pull/2311](https\://github\.com/ansible\-collections/community\.vmware/pull/2311)\)\.
* vm\_device\_helper\.py \- is\_nvdimm\_device is deprecated and will be removed in community\.vmware 7\.0\.0 \([https\://github\.com/ansible\-collections/community\.vmware/pull/2311](https\://github\.com/ansible\-collections/community\.vmware/pull/2311)\)\.
* vmware \- find\_host\_portgroup\_by\_name is deprecated and will be removed in community\.vmware 7\.0\.0 \([https\://github\.com/ansible\-collections/community\.vmware/pull/2311](https\://github\.com/ansible\-collections/community\.vmware/pull/2311)\)\.
* vmware \- find\_vmdk\_file is deprecated and will be removed in community\.vmware 7\.0\.0 \([https\://github\.com/ansible\-collections/community\.vmware/pull/2311](https\://github\.com/ansible\-collections/community\.vmware/pull/2311)\)\.
* vmware \- network\_exists\_by\_name is deprecated and will be removed in community\.vmware 7\.0\.0 \([https\://github\.com/ansible\-collections/community\.vmware/pull/2311](https\://github\.com/ansible\-collections/community\.vmware/pull/2311)\)\.
* vmware \- vmdk\_disk\_path\_split is deprecated and will be removed in community\.vmware 7\.0\.0 \([https\://github\.com/ansible\-collections/community\.vmware/pull/2311](https\://github\.com/ansible\-collections/community\.vmware/pull/2311)\)\.
* vmware\_host\_inventory \- the inventory plugin is deprecated and will be removed in community\.vmware 7\.0\.0 \([https\://github\.com/ansible\-collections/community\.vmware/pull/2283](https\://github\.com/ansible\-collections/community\.vmware/pull/2283)\)\.
* vmware\_maintenancemode \- the module has been deprecated and will be removed in community\.vmware 7\.0\.0 \([https\://github\.com/ansible\-collections/community\.vmware/pull/2293](https\://github\.com/ansible\-collections/community\.vmware/pull/2293)\)\.
* vmware\_rest\_client \- get\_folder\_by\_name is deprecated and will be removed in community\.vmware 7\.0\.0 \([https\://github\.com/ansible\-collections/community\.vmware/pull/2311](https\://github\.com/ansible\-collections/community\.vmware/pull/2311)\)\.
* vmware\_vm\_inventory \- the inventory plugin is deprecated and will be removed in community\.vmware 7\.0\.0 \([https\://github\.com/ansible\-collections/community\.vmware/pull/2283](https\://github\.com/ansible\-collections/community\.vmware/pull/2283)\)\.

<a id="bugfixes-4"></a>
### Bugfixes

<a id="ansible-core-10"></a>
#### Ansible\-core

* include\_vars \- fixed erroneous warning if an unreserved variable name contains a single character that matches a reserved variable\. \([https\://github\.com/ansible/ansible/issues/84623](https\://github\.com/ansible/ansible/issues/84623)\)
* linear strategy \- fix executing <code>end\_role</code> meta tasks for each host\, instead of handling these as implicit run\_once tasks \([https\://github\.com/ansible/ansible/issues/84660](https\://github\.com/ansible/ansible/issues/84660)\)\.

<a id="amazon-aws-7"></a>
#### amazon\.aws

* ec2\_instance \- Fix issue where EC2 instance module failed to apply security groups when both <code>network</code> and <code>vpc\_subnet\_id</code> were specified\, caused by passing <code>None</code> to discover\_security\_groups\(\) \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2488](https\://github\.com/ansible\-collections/amazon\.aws/pull/2488)\)\.
* ec2\_vpc\_nacl\_info \- Fix failure when listing NetworkACLs and no ACLs are found \([https\://github\.com/ansible\-collections/amazon\.aws/issues/2425](https\://github\.com/ansible\-collections/amazon\.aws/issues/2425)\)\.
* iam\_access\_key \- add missing requirements checks \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2465](https\://github\.com/ansible\-collections/amazon\.aws/pull/2465)\)\.
* module\_utils\.botocore \- fixed type aliasing \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2497](https\://github\.com/ansible\-collections/amazon\.aws/pull/2497)\)\.
* plugin\_utils\.botocore \- fixed type aliasing \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2497](https\://github\.com/ansible\-collections/amazon\.aws/pull/2497)\)\.
* s3\_bucket \- Do not use default region as location constraint when creating bucket on ceph cluster \([https\://github\.com/ansible\-collections/amazon\.aws/issues/2420](https\://github\.com/ansible\-collections/amazon\.aws/issues/2420)\)\.

<a id="arista-eos-1"></a>
#### arista\.eos

* Fixed an issue in the <em class="title-reference">compare\_configs</em> method where unnecessary negate commands were generated for ACL entries already present in both <em class="title-reference">have</em> and <em class="title-reference">want</em> configurations\.
* Improved validation logic for ACL sequence numbers and content matching to ensure idempotency\.
* Prevented redundant configuration updates for Access Control Lists\.
* fix facts gathering for ebgp\-multihop attribute\.

<a id="cisco-ios-5"></a>
#### cisco\.ios

* Added support for FourHundredGigE\, FiftyGigE and FourHundredGigabitEthernet\.

<a id="cisco-meraki-4"></a>
#### cisco\.meraki

* Changes at compare equality function\.
* Unable to create Syslog Server Object\. Action module manually fixing\.
* cisco\.meraki\.devices\_switch\_ports idempotency error fixed\.
* cisco\.meraki\.networks\_appliance\_traffic\_shaping\_rules Always Pushes Configuration Even When Unchanged\.
* cisco\.meraki\.organizations\_login\_security module update organization security settings\.

<a id="community-dns-5"></a>
#### community\.dns

* Fix various issues and potential bugs pointed out by linters \([https\://github\.com/ansible\-collections/community\.dns/pull/242](https\://github\.com/ansible\-collections/community\.dns/pull/242)\, [https\://github\.com/ansible\-collections/community\.dns/pull/243](https\://github\.com/ansible\-collections/community\.dns/pull/243)\)\.
* Update Public Suffix List\.

<a id="community-docker-4"></a>
#### community\.docker

* docker\_compose\_v2\_run \- the module has a conflict between the type of parameter it expects and the one it tries to sanitize\. Fix removes the label sanitization step because they are already validated by the parameter definition \([https\://github\.com/ansible\-collections/community\.docker/pull/1034](https\://github\.com/ansible\-collections/community\.docker/pull/1034)\)\.
* vendored Docker SDK for Python \- do not assume that <code>KeyError</code> is always for <code>ApiVersion</code> when querying version fails \([https\://github\.com/ansible\-collections/community\.docker/issues/1033](https\://github\.com/ansible\-collections/community\.docker/issues/1033)\, [https\://github\.com/ansible\-collections/community\.docker/pull/1034](https\://github\.com/ansible\-collections/community\.docker/pull/1034)\)\.

<a id="community-general-16"></a>
#### community\.general

* apache2\_mod\_proxy \- make compatible with Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9762](https\://github\.com/ansible\-collections/community\.general/pull/9762)\)\.
* apache2\_mod\_proxy \- passing the cluster\'s page as referer for the member\'s pages\. This makes the module actually work again for halfway modern Apache versions\. According to some comments founds on the net the referer was required since at least 2019 for some versions of Apache 2 \([https\://github\.com/ansible\-collections/community\.general/pull/9762](https\://github\.com/ansible\-collections/community\.general/pull/9762)\)\.
* cloudflare\_dns \- fix crash when deleting a DNS record or when updating a record with <code>solo\=true</code> \([https\://github\.com/ansible\-collections/community\.general/issues/9652](https\://github\.com/ansible\-collections/community\.general/issues/9652)\, [https\://github\.com/ansible\-collections/community\.general/pull/9649](https\://github\.com/ansible\-collections/community\.general/pull/9649)\)\.
* elasticsearch\_plugin \- fix <code>ERROR\: D is not a recognized option</code> issue when configuring proxy settings \([https\://github\.com/ansible\-collections/community\.general/pull/9774](https\://github\.com/ansible\-collections/community\.general/pull/9774)\, [https\://github\.com/ansible\-collections/community\.general/issues/9773](https\://github\.com/ansible\-collections/community\.general/issues/9773)\)\.
* homebrew \- make package name parsing more resilient \([https\://github\.com/ansible\-collections/community\.general/pull/9665](https\://github\.com/ansible\-collections/community\.general/pull/9665)\, [https\://github\.com/ansible\-collections/community\.general/issues/9641](https\://github\.com/ansible\-collections/community\.general/issues/9641)\)\.
* ipa\_host \- module revoked existing host certificates even if <code>user\_certificate</code> was not given \([https\://github\.com/ansible\-collections/community\.general/pull/9694](https\://github\.com/ansible\-collections/community\.general/pull/9694)\)\.
* keycloak module utils \- replaces missing return in get\_role\_composites method which caused it to return None instead of composite roles \([https\://github\.com/ansible\-collections/community\.general/issues/9678](https\://github\.com/ansible\-collections/community\.general/issues/9678)\, [https\://github\.com/ansible\-collections/community\.general/pull/9691](https\://github\.com/ansible\-collections/community\.general/pull/9691)\)\.
* keycloak\_client \- fix and improve existing tests\. The module showed a diff without actual changes\, solved by improving the <code>normalise\_cr\(\)</code> function \([https\://github\.com/ansible\-collections/community\.general/pull/9644](https\://github\.com/ansible\-collections/community\.general/pull/9644)\)\.
* keycloak\_client \- in check mode\, detect whether the lists in before client \(for example redirect URI list\) contain items that the lists in the desired client do not contain \([https\://github\.com/ansible\-collections/community\.general/pull/9739](https\://github\.com/ansible\-collections/community\.general/pull/9739)\)\.
* lldp \- fix crash caused by certain lldpctl output where an attribute is defined as branch and leaf \([https\://github\.com/ansible\-collections/community\.general/pull/9657](https\://github\.com/ansible\-collections/community\.general/pull/9657)\)\.
* onepassword\_doc lookup plugin \- ensure that 1Password Connect support also works for this plugin \([https\://github\.com/ansible\-collections/community\.general/pull/9625](https\://github\.com/ansible\-collections/community\.general/pull/9625)\)\.
* passwordstore lookup plugin \- fix subkey creation even when <code>create\=false</code> \([https\://github\.com/ansible\-collections/community\.general/issues/9105](https\://github\.com/ansible\-collections/community\.general/issues/9105)\, [https\://github\.com/ansible\-collections/community\.general/pull/9106](https\://github\.com/ansible\-collections/community\.general/pull/9106)\)\.
* proxmox \- adds the <code>pubkey</code> parameter \(back to\) the <code>update</code> state \([https\://github\.com/ansible\-collections/community\.general/issues/9642](https\://github\.com/ansible\-collections/community\.general/issues/9642)\, [https\://github\.com/ansible\-collections/community\.general/pull/9645](https\://github\.com/ansible\-collections/community\.general/pull/9645)\)\.
* proxmox \- fixes a typo in the translation of the <code>pubkey</code> parameter to proxmox\' <code>ssh\-public\-keys</code> \([https\://github\.com/ansible\-collections/community\.general/issues/9642](https\://github\.com/ansible\-collections/community\.general/issues/9642)\, [https\://github\.com/ansible\-collections/community\.general/pull/9645](https\://github\.com/ansible\-collections/community\.general/pull/9645)\)\.
* proxmox inventory plugin \- plugin did not update cache correctly after <code>meta\: refresh\_inventory</code> \([https\://github\.com/ansible\-collections/community\.general/issues/9710](https\://github\.com/ansible\-collections/community\.general/issues/9710)\, [https\://github\.com/ansible\-collections/community\.general/pull/9760](https\://github\.com/ansible\-collections/community\.general/pull/9760)\)\.
* redhat\_subscription \- use the \"enable\_content\" option \(when available\) when
  registering using D\-Bus\, to ensure that subscription\-manager enables the
  content on registration\; this is particular important on EL 10\+ and Fedora
  41\+
  \([https\://github\.com/ansible\-collections/community\.general/pull/9778](https\://github\.com/ansible\-collections/community\.general/pull/9778)\)\.
* xml \- ensure file descriptor is closed \([https\://github\.com/ansible\-collections/community\.general/pull/9695](https\://github\.com/ansible\-collections/community\.general/pull/9695)\)\.
* zfs \- fix handling of multi\-line values of user\-defined ZFS properties \([https\://github\.com/ansible\-collections/community\.general/pull/6264](https\://github\.com/ansible\-collections/community\.general/pull/6264)\)\.
* zfs\_facts \- parameter <code>type</code> now accepts multple values as documented \([https\://github\.com/ansible\-collections/community\.general/issues/5909](https\://github\.com/ansible\-collections/community\.general/issues/5909)\, [https\://github\.com/ansible\-collections/community\.general/pull/9697](https\://github\.com/ansible\-collections/community\.general/pull/9697)\)\.

<a id="community-routeros-4"></a>
#### community\.routeros

* api\_info\, api\_modify \- remove the primary key <code>action</code> from the <code>interface wifi provisioning</code> path\, since RouterOS also allows to create completely duplicate entries \([https\://github\.com/ansible\-collections/community\.routeros/issues/344](https\://github\.com/ansible\-collections/community\.routeros/issues/344)\, [https\://github\.com/ansible\-collections/community\.routeros/pull/345](https\://github\.com/ansible\-collections/community\.routeros/pull/345)\)\.

<a id="community-sops-3"></a>
#### community\.sops

* install role \- when used with Debian on ARM architecture\, the architecture name is now correctly translated from <code>aarch64</code> to <code>arm64</code> \([https\://github\.com/ansible\-collections/community\.sops/issues/220](https\://github\.com/ansible\-collections/community\.sops/issues/220)\, [https\://github\.com/ansible\-collections/community\.sops/pull/221](https\://github\.com/ansible\-collections/community\.sops/pull/221)\)\.

<a id="containers-podman-1"></a>
#### containers\.podman

* Don\'t pull image when state is absent or pull\=never \(\#889\)
* Fix idempotency for containers with env vars containing MAX\_SIZE \(\#893\)
* Fix list tags failure in podman\_search \(\#875\)
* Fix podman\_container\_copy examples \(\#882\)
* docs\(podman\_container\) \- improve comments on network property \(\#878\)

<a id="fortinet-fortimanager-2"></a>
#### fortinet\.fortimanager

* Changed parameter type of some parameters\.

<a id="google-cloud-1"></a>
#### google\.cloud

* run integration test with Ansible 2\.16 to match <em class="title-reference">requires\_ansible</em> version

<a id="netapp-ontap-1"></a>
#### netapp\.ontap

* Resolved Ansible lint issues\.
* na\_ontap\_aggregate \- fix issue with \'raid\_type\' change in REST\.
* na\_ontap\_kerberos\_interface \- updated example in module documentation\.
* na\_ontap\_qtree \- fix timeout issue with qtree delete in REST\.

<a id="purestorage-flasharray-3"></a>
#### purestorage\.flasharray

* purefa\_ds \- Fixed issue with trying to create a pre\-existing system\-defined role
* purefa\_hg \- Fixed issue when <code>check\_mode \= true</code> not reporting correct status when adding new hosts to hostgroup\.
* purefa\_host \- Fix issue with no VLAN provided when Purity//FA is a recent version\.
* purefa\_host \- Fix issue with setting preferred\_arrays for a host\.
* purefa\_pod \- Errored out when setting failover preference for pod
* purefa\_ra \- Fixed duration check logic
* purefa\_volume \- Fixes issue of moving protected volume into volume group

<a id="vmware-vmware-3"></a>
#### vmware\.vmware

* folder \- replaced non\-existent \'storage\' type with \'datastore\' type
* module\_deploy\_vm\_base \- fix attribute error when deploying to a resource pool

<a id="known-issues-3"></a>
### Known Issues

<a id="purestorage-flasharray-4"></a>
#### purestorage\.flasharray

* All Fusion fleet members will be assumed to be at the same Purity//FA version level as the array connected to by Ansible\.
* FlashArray//CBS is not currently supported as a member of a Fusion fleet

<a id="new-plugins-2"></a>
### New Plugins

<a id="lookup"></a>
#### Lookup

* infoblox\.nios\_modules\.nios\_next\_vlan\_id \- Return the next available VLAN ID

<a id="new-modules-4"></a>
### New Modules

<a id="amazon-aws-8"></a>
#### amazon\.aws

* amazon\.aws\.route53\_key\_signing\_key \- Manages a key\-signing key \(KSK\)

<a id="check-point-mgmt-2"></a>
#### check\_point\.mgmt

* check\_point\.mgmt\.cp\_mgmt\_user \- Manages user objects on Checkpoint over Web Services API
* check\_point\.mgmt\.cp\_mgmt\_user\_facts \- Get user objects facts on Checkpoint over Web Services API
* check\_point\.mgmt\.cp\_mgmt\_user\_template \- Manages user\-template objects on Checkpoint over Web Services API
* check\_point\.mgmt\.cp\_mgmt\_user\_template\_facts \- Get user\-template objects facts on Checkpoint over Web Services API

<a id="community-docker-5"></a>
#### community\.docker

* community\.docker\.docker\_context\_info \- Retrieve information on Docker contexts for the current user\.

<a id="community-general-17"></a>
#### community\.general

* community\.general\.systemd\_info \- Gather C\(systemd\) unit info\.

<a id="fortinet-fortimanager-3"></a>
#### fortinet\.fortimanager

* fortinet\.fortimanager\.fmgr\_gtp\_ieallowlist \- IE allow list\.
* fortinet\.fortimanager\.fmgr\_gtp\_ieallowlist\_entries \- Entries of allow list for unknown or out\-of\-state IEs\.
* fortinet\.fortimanager\.fmgr\_ums\_setting \- Ums setting

<a id="infoblox-nios-modules"></a>
#### infoblox\.nios\_modules

* infoblox\.nios\_modules\.nios\_adminuser \- Configure Infoblox NIOS Admin Users
* infoblox\.nios\_modules\.nios\_vlan \- Configure Infoblox NIOS VLANs

<a id="netapp-storagegrid-1"></a>
#### netapp\.storagegrid

* netapp\.storagegrid\.na\_sg\_grid\_ec\_profile \- Manage EC profiles on StorageGRID\.
* netapp\.storagegrid\.na\_sg\_grid\_ilm\_policy \- Manage ILM policies on StorageGRID\.
* netapp\.storagegrid\.na\_sg\_grid\_ilm\_policy\_tag \- Manage ILM policy tags on StorageGRID\.
* netapp\.storagegrid\.na\_sg\_grid\_ilm\_pool \- Manage ILM pools on StorageGRID\.
* netapp\.storagegrid\.na\_sg\_grid\_ilm\_rule \- Manage ILM rules on StorageGRID\.

<a id="purestorage-flasharray-5"></a>
#### purestorage\.flasharray

* purestorage\.flasharray\.purefa\_fleet \- Manage Fusion Fleet
* purestorage\.flasharray\.purefa\_realm \- Manage realms on Pure Storage FlashArrays

<a id="unchanged-collections-4"></a>
### Unchanged Collections

* ansible\.netcommon \(still version 7\.1\.0\)
* ansible\.posix \(still version 1\.6\.2\)
* ansible\.utils \(still version 5\.1\.2\)
* ansible\.windows \(still version 2\.7\.0\)
* awx\.awx \(still version 24\.6\.1\)
* chocolatey\.chocolatey \(still version 1\.5\.3\)
* cisco\.aci \(still version 2\.10\.1\)
* cisco\.asa \(still version 6\.1\.0\)
* cisco\.intersight \(still version 2\.0\.20\)
* cisco\.iosxr \(still version 10\.3\.0\)
* cisco\.ise \(still version 2\.10\.0\)
* cisco\.mso \(still version 2\.9\.0\)
* cisco\.nxos \(still version 9\.3\.0\)
* cisco\.ucs \(still version 1\.15\.0\)
* cloud\.common \(still version 4\.0\.0\)
* cloudscale\_ch\.cloud \(still version 2\.4\.1\)
* community\.aws \(still version 9\.0\.0\)
* community\.ciscosmb \(still version 1\.0\.10\)
* community\.digitalocean \(still version 1\.27\.0\)
* community\.grafana \(still version 2\.1\.0\)
* community\.hashi\_vault \(still version 6\.2\.0\)
* community\.hrobot \(still version 2\.1\.0\)
* community\.library\_inventory\_filtering\_v1 \(still version 1\.0\.2\)
* community\.libvirt \(still version 1\.3\.1\)
* community\.mongodb \(still version 1\.7\.9\)
* community\.mysql \(still version 3\.12\.0\)
* community\.network \(still version 5\.1\.0\)
* community\.okd \(still version 4\.0\.1\)
* community\.postgresql \(still version 3\.10\.2\)
* community\.proxysql \(still version 1\.6\.0\)
* community\.rabbitmq \(still version 1\.4\.0\)
* community\.sap\_libs \(still version 1\.4\.2\)
* community\.windows \(still version 2\.3\.0\)
* community\.zabbix \(still version 3\.2\.0\)
* cyberark\.conjur \(still version 1\.3\.2\)
* cyberark\.pas \(still version 1\.0\.30\)
* dellemc\.enterprise\_sonic \(still version 2\.5\.1\)
* dellemc\.openmanage \(still version 9\.10\.0\)
* dellemc\.powerflex \(still version 2\.6\.0\)
* dellemc\.unity \(still version 2\.0\.0\)
* f5networks\.f5\_modules \(still version 1\.34\.1\)
* fortinet\.fortios \(still version 2\.3\.9\)
* grafana\.grafana \(still version 5\.7\.0\)
* hetzner\.hcloud \(still version 4\.2\.2\)
* ibm\.qradar \(still version 4\.0\.0\)
* ibm\.spectrum\_virtualize \(still version 2\.0\.0\)
* ibm\.storage\_virtualize \(still version 2\.6\.0\)
* ieisystem\.inmanage \(still version 3\.0\.0\)
* infinidat\.infinibox \(still version 1\.4\.5\)
* inspur\.ispim \(still version 2\.2\.3\)
* junipernetworks\.junos \(still version 9\.1\.0\)
* kaytus\.ksmanage \(still version 2\.0\.0\)
* kubernetes\.core \(still version 5\.1\.0\)
* kubevirt\.core \(still version 2\.1\.0\)
* lowlydba\.sqlserver \(still version 2\.5\.0\)
* microsoft\.ad \(still version 1\.8\.0\)
* netapp\.cloudmanager \(still version 21\.24\.0\)
* netapp\_eseries\.santricity \(still version 1\.4\.1\)
* netbox\.netbox \(still version 3\.20\.0\)
* ngine\_io\.cloudstack \(still version 2\.5\.0\)
* openstack\.cloud \(still version 2\.4\.1\)
* ovirt\.ovirt \(still version 3\.2\.0\)
* purestorage\.flashblade \(still version 1\.19\.2\)
* sensu\.sensu\_go \(still version 1\.14\.0\)
* splunk\.es \(still version 4\.0\.0\)
* telekom\_mms\.icinga\_director \(still version 2\.2\.2\)
* theforeman\.foreman \(still version 4\.2\.0\)
* vultr\.cloud \(still version 1\.13\.0\)
* vyos\.vyos \(still version 5\.0\.0\)
* wti\.remote \(still version 1\.0\.10\)

<a id="v11-2-0"></a>
## v11\.2\.0

- <a href="#release-summary-5">Release Summary</a>
- <a href="#ansible-core-11">Ansible\-core</a>
- <a href="#changed-collections-5">Changed Collections</a>
- <a href="#major-changes-4">Major Changes</a>
    - <a href="#community-vmware-11">community\.vmware</a>
    - <a href="#dellemc-openmanage-7">dellemc\.openmanage</a>
    - <a href="#fortinet-fortios-2">fortinet\.fortios</a>
    - <a href="#google-cloud-2">google\.cloud</a>
    - <a href="#grafana-grafana">grafana\.grafana</a>
- <a href="#minor-changes-5">Minor Changes</a>
    - <a href="#amazon-aws-9">amazon\.aws</a>
    - <a href="#ansible-windows-2">ansible\.windows</a>
    - <a href="#cisco-asa">cisco\.asa</a>
    - <a href="#cisco-dnac-3">cisco\.dnac</a>
    - <a href="#cisco-ios-6">cisco\.ios</a>
    - <a href="#cisco-iosxr-1">cisco\.iosxr</a>
    - <a href="#cisco-ise">cisco\.ise</a>
    - <a href="#cisco-meraki-5">cisco\.meraki</a>
    - <a href="#cisco-nxos-2">cisco\.nxos</a>
    - <a href="#community-ciscosmb">community\.ciscosmb</a>
    - <a href="#community-crypto-5">community\.crypto</a>
    - <a href="#community-docker-6">community\.docker</a>
    - <a href="#community-general-18">community\.general</a>
    - <a href="#community-hrobot-4">community\.hrobot</a>
    - <a href="#community-mysql-4">community\.mysql</a>
    - <a href="#community-okd">community\.okd</a>
    - <a href="#community-postgresql-8">community\.postgresql</a>
    - <a href="#community-rabbitmq-2">community\.rabbitmq</a>
    - <a href="#community-routeros-5">community\.routeros</a>
    - <a href="#community-vmware-12">community\.vmware</a>
    - <a href="#dellemc-openmanage-8">dellemc\.openmanage</a>
    - <a href="#dellemc-powerflex">dellemc\.powerflex</a>
    - <a href="#f5networks-f5-modules-2">f5networks\.f5\_modules</a>
    - <a href="#google-cloud-3">google\.cloud</a>
    - <a href="#ibm-storage-virtualize-5">ibm\.storage\_virtualize</a>
    - <a href="#kubernetes-core-3">kubernetes\.core</a>
    - <a href="#lowlydba-sqlserver-2">lowlydba\.sqlserver</a>
    - <a href="#microsoft-ad-3">microsoft\.ad</a>
    - <a href="#vmware-vmware-4">vmware\.vmware</a>
    - <a href="#vmware-vmware-rest-1">vmware\.vmware\_rest</a>
- <a href="#deprecated-features-5">Deprecated Features</a>
    - <a href="#amazon-aws-10">amazon\.aws</a>
    - <a href="#community-crypto-6">community\.crypto</a>
    - <a href="#community-general-19">community\.general</a>
    - <a href="#community-hrobot-5">community\.hrobot</a>
    - <a href="#community-vmware-13">community\.vmware</a>
- <a href="#security-fixes">Security Fixes</a>
    - <a href="#cloudscale-ch-cloud-3">cloudscale\_ch\.cloud</a>
    - <a href="#community-general-20">community\.general</a>
- <a href="#bugfixes-5">Bugfixes</a>
    - <a href="#ansible-core-12">Ansible\-core</a>
    - <a href="#amazon-aws-11">amazon\.aws</a>
    - <a href="#ansible-windows-3">ansible\.windows</a>
    - <a href="#cisco-asa-1">cisco\.asa</a>
    - <a href="#cisco-ios-7">cisco\.ios</a>
    - <a href="#cisco-ise-1">cisco\.ise</a>
    - <a href="#cisco-meraki-6">cisco\.meraki</a>
    - <a href="#cisco-nxos-3">cisco\.nxos</a>
    - <a href="#community-crypto-7">community\.crypto</a>
    - <a href="#community-dns-6">community\.dns</a>
    - <a href="#community-docker-7">community\.docker</a>
    - <a href="#community-general-21">community\.general</a>
    - <a href="#community-libvirt-2">community\.libvirt</a>
    - <a href="#community-postgresql-9">community\.postgresql</a>
    - <a href="#community-rabbitmq-3">community\.rabbitmq</a>
    - <a href="#community-vmware-14">community\.vmware</a>
    - <a href="#dellemc-openmanage-9">dellemc\.openmanage</a>
    - <a href="#f5networks-f5-modules-3">f5networks\.f5\_modules</a>
    - <a href="#fortinet-fortios-3">fortinet\.fortios</a>
    - <a href="#google-cloud-4">google\.cloud</a>
    - <a href="#ibm-storage-virtualize-6">ibm\.storage\_virtualize</a>
    - <a href="#kubernetes-core-4">kubernetes\.core</a>
    - <a href="#lowlydba-sqlserver-3">lowlydba\.sqlserver</a>
    - <a href="#purestorage-flashblade-3">purestorage\.flashblade</a>
    - <a href="#vmware-vmware-5">vmware\.vmware</a>
    - <a href="#vmware-vmware-rest-2">vmware\.vmware\_rest</a>
- <a href="#known-issues-4">Known Issues</a>
    - <a href="#dellemc-openmanage-10">dellemc\.openmanage</a>
- <a href="#new-plugins-3">New Plugins</a>
    - <a href="#connection-1">Connection</a>
    - <a href="#filter-1">Filter</a>
    - <a href="#inventory">Inventory</a>
    - <a href="#lookup-1">Lookup</a>
- <a href="#new-modules-5">New Modules</a>
    - <a href="#amazon-aws-12">amazon\.aws</a>
    - <a href="#ansible-windows-4">ansible\.windows</a>
    - <a href="#cisco-iosxr-2">cisco\.iosxr</a>
    - <a href="#cisco-nxos-4">cisco\.nxos</a>
    - <a href="#community-crypto-8">community\.crypto</a>
    - <a href="#community-general-22">community\.general</a>
    - <a href="#community-hrobot-6">community\.hrobot</a>
    - <a href="#dellemc-powerflex-1">dellemc\.powerflex</a>
    - <a href="#kubernetes-core-5">kubernetes\.core</a>
    - <a href="#lowlydba-sqlserver-4">lowlydba\.sqlserver</a>
- <a href="#unchanged-collections-5">Unchanged Collections</a>

<a id="release-summary-5"></a>
### Release Summary

Release Date\: 2025\-01\-28

[Porting Guide](https\://docs\.ansible\.com/ansible/devel/porting\_guides\.html)

<a id="ansible-core-11"></a>
### Ansible\-core

Ansible 11\.2\.0 contains ansible\-core version 2\.18\.2\.
This is a newer version than version 2\.18\.1 contained in the previous Ansible release\.

The changes are reported in the combined changelog below\.

<a id="changed-collections-5"></a>
### Changed Collections

If not mentioned explicitly\, the changes are reported in the combined changelog below\.

| Collection                  | Ansible 11.1.0 | Ansible 11.2.0 | Notes                                                                                                                                                                                                        |
| --------------------------- | -------------- | -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| amazon.aws                  | 9.0.0          | 9.1.1          |                                                                                                                                                                                                              |
| ansible.windows             | 2.5.0          | 2.7.0          |                                                                                                                                                                                                              |
| cisco.asa                   | 6.0.0          | 6.1.0          |                                                                                                                                                                                                              |
| cisco.dnac                  | 6.25.0         | 6.28.0         |                                                                                                                                                                                                              |
| cisco.ios                   | 9.0.3          | 9.1.0          |                                                                                                                                                                                                              |
| cisco.iosxr                 | 10.2.2         | 10.3.0         |                                                                                                                                                                                                              |
| cisco.ise                   | 2.9.6          | 2.10.0         |                                                                                                                                                                                                              |
| cisco.meraki                | 2.18.3         | 2.20.5         |                                                                                                                                                                                                              |
| cisco.nxos                  | 9.2.1          | 9.3.0          |                                                                                                                                                                                                              |
| cisco.ucs                   | 1.14.0         | 1.15.0         | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.                                                                                 |
| cloudscale_ch.cloud         | 2.4.0          | 2.4.1          |                                                                                                                                                                                                              |
| community.ciscosmb          | 1.0.9          | 1.0.10         |                                                                                                                                                                                                              |
| community.crypto            | 2.22.3         | 2.24.0         |                                                                                                                                                                                                              |
| community.dns               | 3.1.0          | 3.1.2          |                                                                                                                                                                                                              |
| community.docker            | 4.1.0          | 4.3.1          |                                                                                                                                                                                                              |
| community.general           | 10.1.0         | 10.3.0         |                                                                                                                                                                                                              |
| community.hrobot            | 2.0.2          | 2.1.0          |                                                                                                                                                                                                              |
| community.libvirt           | 1.3.0          | 1.3.1          |                                                                                                                                                                                                              |
| community.mongodb           | 1.7.8          | 1.7.9          | There are no changes recorded in the changelog.                                                                                                                                                              |
| community.mysql             | 3.11.0         | 3.12.0         |                                                                                                                                                                                                              |
| community.okd               | 4.0.0          | 4.0.1          |                                                                                                                                                                                                              |
| community.postgresql        | 3.9.0          | 3.10.2         |                                                                                                                                                                                                              |
| community.rabbitmq          | 1.3.0          | 1.4.0          |                                                                                                                                                                                                              |
| community.routeros          | 3.1.0          | 3.3.0          |                                                                                                                                                                                                              |
| community.sops              | 2.0.0          | 2.0.1          |                                                                                                                                                                                                              |
| community.vmware            | 5.2.0          | 5.3.0          |                                                                                                                                                                                                              |
| cyberark.conjur             | 1.3.1          | 1.3.2          | You can find the collection's changelog at [https://github.com/cyberark/ansible-conjur-collection/blob/master/CHANGELOG.md](https://github.com/cyberark/ansible-conjur-collection/blob/master/CHANGELOG.md). |
| dellemc.openmanage          | 9.9.0          | 9.10.0         |                                                                                                                                                                                                              |
| dellemc.powerflex           | 2.5.0          | 2.6.0          |                                                                                                                                                                                                              |
| f5networks.f5_modules       | 1.32.1         | 1.34.1         |                                                                                                                                                                                                              |
| fortinet.fortios            | 2.3.8          | 2.3.9          |                                                                                                                                                                                                              |
| google.cloud                | 1.4.1          | 1.5.0          |                                                                                                                                                                                                              |
| grafana.grafana             | 5.6.0          | 5.7.0          |                                                                                                                                                                                                              |
| ibm.storage_virtualize      | 2.5.0          | 2.6.0          |                                                                                                                                                                                                              |
| kubernetes.core             | 5.0.0          | 5.1.0          |                                                                                                                                                                                                              |
| lowlydba.sqlserver          | 2.3.4          | 2.5.0          |                                                                                                                                                                                                              |
| microsoft.ad                | 1.7.1          | 1.8.0          |                                                                                                                                                                                                              |
| openstack.cloud             | 2.3.0          | 2.4.1          | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.                                                                                 |
| purestorage.flashblade      | 1.19.1         | 1.19.2         |                                                                                                                                                                                                              |
| telekom_mms.icinga_director | 2.2.1          | 2.2.2          |                                                                                                                                                                                                              |
| vmware.vmware               | 1.7.1          | 1.9.0          |                                                                                                                                                                                                              |
| vmware.vmware_rest          | 4.3.0          | 4.5.0          |                                                                                                                                                                                                              |

<a id="major-changes-4"></a>
### Major Changes

<a id="community-vmware-11"></a>
#### community\.vmware

* vmware\_dvswitch\_pvlans \- The VLAN ID type has been updated to be handled as an integer \([https\://github\.com/ansible\-collections/community\.vmware/pull/2267](https\://github\.com/ansible\-collections/community\.vmware/pull/2267)\)\.

<a id="dellemc-openmanage-7"></a>
#### dellemc\.openmanage

* omevv\_firmware \- This module allows to update firmware of the single host and single cluster\.

<a id="fortinet-fortios-2"></a>
#### fortinet\.fortios

* Support check\_mode on all the configuration modules\.

<a id="google-cloud-2"></a>
#### google\.cloud

* google\_cloud\_ops\_agents \- role submodule removed because it prevents the collection from passing sanity and lint tests

<a id="grafana-grafana"></a>
#### grafana\.grafana

* Ability to set custom directory path for \*\.alloy config files by \@voidquark in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/294](https\://github\.com/grafana/grafana\-ansible\-collection/pull/294)
* Fix \'dict object\' has no attribute \'path\' when running with \-\-check by \@JMLX42 in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/283](https\://github\.com/grafana/grafana\-ansible\-collection/pull/283)
* Update grafana template by \@santilococo in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/300](https\://github\.com/grafana/grafana\-ansible\-collection/pull/300)
* add loki bloom support by \@voidquark in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/298](https\://github\.com/grafana/grafana\-ansible\-collection/pull/298)
* grafana\.ini yaml syntax by \@intermittentnrg in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/232](https\://github\.com/grafana/grafana\-ansible\-collection/pull/232)

<a id="minor-changes-5"></a>
### Minor Changes

<a id="amazon-aws-9"></a>
#### amazon\.aws

* autoscaling\_group \- adds <code>group\_name</code> as an alias for the <code>name</code> parameter \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2396](https\://github\.com/ansible\-collections/amazon\.aws/pull/2396)\)\.
* autoscaling\_group\_info \- adds <code>group\_name</code> as an alias for the <code>name</code> parameter \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2396](https\://github\.com/ansible\-collections/amazon\.aws/pull/2396)\)\.
* autoscaling\_instance\_refresh \- adds <code>group\_name</code> as an alias for the <code>name</code> parameter \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2396](https\://github\.com/ansible\-collections/amazon\.aws/pull/2396)\)\.
* autoscaling\_instance\_refresh\_info \- adds <code>group\_name</code> as an alias for the <code>name</code> parameter \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2396](https\://github\.com/ansible\-collections/amazon\.aws/pull/2396)\)\.
* ec2\_instance \- Fix the issue when trying to run instances using launch template in an AWS environment where no default subnet is defined\([https\://github\.com/ansible\-collections/amazon\.aws/issues/2321](https\://github\.com/ansible\-collections/amazon\.aws/issues/2321)\)\.
* ec2\_metadata\_facts \- add <code>ansible\_ec2\_instance\_tags</code> to return values \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2398](https\://github\.com/ansible\-collections/amazon\.aws/pull/2398)\)\.
* ec2\_transit\_gateway \- handle empty description while deleting transit gateway \([https\://github\.com/ansible\-collections/community\.aws/pull/2086](https\://github\.com/ansible\-collections/community\.aws/pull/2086)\)\.

<a id="ansible-windows-2"></a>
#### ansible\.windows

* Added support for Windows Server 2025
* setup \- Added <code>ansible\_os\_install\_date</code> as the OS installation date in the ISO 8601 format <code>yyyy\-MM\-ddTHH\:mm\:ssZ</code>\. This date is represented in the UTC timezone \- [https\://github\.com/ansible\-collections/ansible\.windows/issues/663](https\://github\.com/ansible\-collections/ansible\.windows/issues/663)
* win\_get\_url \- if checksum is passed and destination file exists with different checksum file is always downloaded \([https\://github\.com/ansible\-collections/ansible\.windows/issues/717](https\://github\.com/ansible\-collections/ansible\.windows/issues/717)\)
* win\_get\_url \- if checksum is passed and destination file exists with identical checksum no download is done unless force\=yes \([https\://github\.com/ansible\-collections/ansible\.windows/issues/717](https\://github\.com/ansible\-collections/ansible\.windows/issues/717)\)
* win\_group \- Added <code>\-\-diff</code> output support\.
* win\_group \- Added <code>members</code> option to set the group membership\. This is designed to replace the functionality of the <code>win\_group\_membership</code> module\.
* win\_group \- Added <code>sid</code> return value representing the security identifier of the group when <code>state\=present</code>\.
* win\_group \- Migrate to newer Ansible\.Basic fragment for better input validation and testing support\.

<a id="cisco-asa"></a>
#### cisco\.asa

* cisco\.asa\.asa \- add support to fetch hardware specific information in facts
* cisco\.asa\.asa\_acls \- add support for specifying object\-group as protocol

<a id="cisco-dnac-3"></a>
#### cisco\.dnac

* Added sample playbook for Device Configs Backup Module
* Bug fixes in \[sda\_fabric\_sites\_zones\_workflow\_manager module
* Bug fixes in accesspoint\_workflow\_manager module
* Bug fixes in lan\_automation\_workflow\_manager module
* Bug fixes in pnp\_workflow\_manager module
* Bug fixes in sda\_fabric\_devices\_workflow\_manager
* Bug fixes in sda\_fabric\_transits\_workflow\_manager
* Bug fixes in template\_workflow\_manager module
* Changes in dnac\.py file
* Changes in inventory\_workflow\_manager module
* Changes in ise\_radius\_integration\_workflow\_manager
* Changes in network\_compliance\_workflow\_manager
* Changes in network\_settings\_workflow\_manager
* Changes in sda\_fabric\_devices\_workflow\_manager module
* Changes in site\_workflow\_manager module
* Changes in swim\_workflow\_manager module
* Changes in template\_workflow\_manager
* Enhancements in \[sda\_fabric\_virtual\_networks\_workflow\_manager module to support batch operation\.
* Enhancements in device\_configs\_backup\_workflow\_manager module to support unzipped backup file after download
* Enhancements in device\_credential\_workflow\_manager module
* Enhancements in provision\_workflow\_manager module
* Enhancements in sda\_host\_port\_onboarding\_workflow\_manager module
* Fixed issues in module sda\_anycast\_gateways\_v1
* Fixed issues in module sda\_layer3\_virtual\_networks\_v1
* Supporting unmarking the devices in rma\_workflow\_manager module
* Unit test modules added for pnp\_workflow\_manager module
* aaa\_services\_count\_v1\_info \- new module
* aaa\_services\_id\_trend\_analytics\_v1 \- new module
* aaa\_services\_id\_v1\_info \- new module
* aaa\_services\_query\_count\_v1 \- new module
* aaa\_services\_query\_v1 \- new module
* aaa\_services\_summary\_analytics\_v1 \- new module
* aaa\_services\_top\_n\_analytics\_v1 \- new module
* aaa\_services\_trend\_analytics\_v1 \- new module
* aaa\_services\_v1\_info \- new module
* application of the changes made in pull request 207
* application\_visibility\_network\_devices\_count\_v1\_info \- new module
* application\_visibility\_network\_devices\_disable\_app\_telemetry\_v1 \- new module
* application\_visibility\_network\_devices\_disable\_cbar\_v1 \- new module
* application\_visibility\_network\_devices\_enable\_app\_telemetry\_v1 \- new module
* application\_visibility\_network\_devices\_enable\_cbar\_v1 \- new module
* application\_visibility\_network\_devices\_v1\_info \- new module
* assurance\_tasks\_count\_v1\_info \- new module
* assurance\_tasks\_id\_v1\_info \- new module
* assurance\_tasks\_v1\_info \- new module
* cisco\_imcs\_id\_v1 \- new module
* cisco\_imcs\_id\_v1\_info \- new module
* cisco\_imcs\_v1 \- new module
* cisco\_imcs\_v1\_info \- new module
* compliance\_device\_create\_v1 \- new module
* connection\_modesetting\_v1 \- new module
* connection\_modesetting\_v1\_info \- new module
* device\_configs\_backup\_workflow\_manager \- attribute \'unzip\_backup\' was added
* dhcp\_services\_count\_v1\_info \- new module
* dhcp\_services\_id\_trend\_analytics\_v1 \- new module
* dhcp\_services\_id\_v1\_info \- new module
* dhcp\_services\_query\_count\_v1 \- new module
* dhcp\_services\_query\_v1 \- new module
* dhcp\_services\_summary\_analytics\_v1 \- new module
* dhcp\_services\_top\_n\_analytics\_v1 \- new module
* dhcp\_services\_trend\_analytics\_v1 \- new module
* dhcp\_services\_v1\_info \- new module
* diagnostic\_tasks\_id\_detail\_v1\_info \- new module
* diagnostic\_tasks\_id\_v1\_info \- new module
* dna\_health\_score\_definitions\_count\_v1\_info \- new module
* dna\_network\_devices\_query\_count\_v1 \- new module
* dns\_services\_count\_v1\_info \- new module
* dns\_services\_id\_trend\_analytics\_v1 \- new module
* dns\_services\_id\_v1\_info \- new module
* dns\_services\_query\_count\_v1 \- new module
* dns\_services\_query\_v1 \- new module
* dns\_services\_summary\_analytics\_v1 \- new module
* dns\_services\_top\_n\_analytics\_v1 \- new module
* dns\_services\_trend\_analytics\_v1 \- new module
* dns\_services\_v1\_info \- new module
* fabric\_site\_health\_summaries\_count\_v1\_info \- new module
* fabric\_site\_health\_summaries\_id\_trend\_analytics\_v1\_info \- new module
* fabric\_site\_health\_summaries\_id\_v1\_info \- new module
* fabric\_site\_health\_summaries\_v1\_info \- new module
* fabric\_summary\_v1\_info \- new module
* fabrics\_fabric\_id\_switch\_wireless\_setting\_reload\_v1 \- new module
* fabrics\_fabric\_id\_switch\_wireless\_setting\_v1 \- new module
* fabrics\_fabric\_id\_switch\_wireless\_setting\_v1\_info \- new module
* fabrics\_fabric\_id\_wireless\_multicast\_v1 \- new module
* fabrics\_fabric\_id\_wireless\_multicast\_v1\_info \- new module
* field\_notices\_results\_network\_devices\_count\_v1\_info \- new module
* field\_notices\_results\_network\_devices\_network\_device\_id\_notices\_count\_v1\_info \- new module
* field\_notices\_results\_network\_devices\_network\_device\_id\_notices\_id\_v1\_info \- new module
* field\_notices\_results\_network\_devices\_network\_device\_id\_notices\_v1\_info \- new module
* field\_notices\_results\_network\_devices\_network\_device\_id\_v1\_info \- new module
* field\_notices\_results\_network\_devices\_v1\_info \- new module
* field\_notices\_results\_notices\_id\_network\_devices\_count\_v1\_info \- new module
* field\_notices\_results\_notices\_id\_network\_devices\_network\_device\_id\_v1\_info \- new module
* field\_notices\_results\_notices\_id\_network\_devices\_v1\_info \- new module
* field\_notices\_results\_notices\_id\_v1\_info \- new module
* field\_notices\_results\_notices\_v1\_info \- new module
* field\_notices\_trials\_v1 \- new module
* field\_notices\_trials\_v1\_info \- new module
* field\_notices\_trigger\_scan\_v1 \- new module
* floors\_floor\_id\_access\_point\_positions\_bulk\_change\_v2 \- new module
* floors\_floor\_id\_access\_point\_positions\_count\_v2\_info \- new module
* floors\_floor\_id\_access\_point\_positions\_v2\_info \- new module
* floors\_floor\_id\_planned\_access\_point\_positions\_assign\_access\_point\_positions\_v2 \- new module
* floors\_floor\_id\_planned\_access\_point\_positions\_bulk\_change\_v2 \- new module
* floors\_floor\_id\_planned\_access\_point\_positions\_bulk\_v2 \- new module
* floors\_floor\_id\_planned\_access\_point\_positions\_count\_v2\_info \- new module
* floors\_floor\_id\_planned\_access\_point\_positions\_id\_v2 \- new module
* floors\_floor\_id\_planned\_access\_point\_positions\_v2\_info \- new module
* icap\_capture\_files\_count\_v1\_info \- new module
* icap\_capture\_files\_id\_download\_v1\_info \- new module
* icap\_capture\_files\_id\_v1\_info \- new module
* icap\_capture\_files\_v1\_info \- new module
* icap\_clients\_id\_stats\_v1 \- new module
* icap\_radios\_id\_stats\_v1 \- new module
* icap\_settings\_configuration\_models\_id\_delete\_deploy\_v1 \- new module
* icap\_settings\_configuration\_models\_preview\_activity\_id\_deploy\_v1 \- new module
* icap\_settings\_configuration\_models\_preview\_activity\_id\_network\_device\_status\_details\_v1\_info \- new module
* icap\_settings\_configuration\_models\_preview\_activity\_id\_network\_devices\_network\_device\_id\_config\_v1 \- new module
* icap\_settings\_configuration\_models\_preview\_activity\_id\_network\_devices\_network\_device\_id\_config\_v1\_info \- new module
* icap\_settings\_configuration\_models\_preview\_activity\_id\_v1 \- new module
* icap\_settings\_configuration\_models\_v1 \- new module
* icap\_settings\_count\_v1\_info \- new module
* icap\_settings\_deploy\_id\_delete\_deploy\_v1 \- new module
* icap\_settings\_deploy\_v1 \- new module
* icap\_settings\_device\_deployments\_count\_v1\_info \- new module
* icap\_settings\_device\_deployments\_v1\_info \- new module
* icap\_settings\_v1\_info \- new module
* icap\_spectrum\_interference\_device\_reports\_v1\_info \- new module
* icap\_spectrum\_sensor\_reports\_v1\_info \- new module
* images\_cco\_sync\_v1 \- new module
* images\_id\_sites\_site\_id\_tag\_golden\_v1 \- new module
* images\_id\_sites\_site\_id\_untag\_golden\_v1 \- new module
* images\_id\_v1 \- new module
* intent\_network\_devices\_query\_count\_v1 \- new module
* intent\_network\_devices\_query\_v1 \- new module
* interfaces\_id\_trend\_analytics\_v1 \- new module
* ipam\_global\_ip\_address\_pools\_count\_v1\_info \- new module
* ipam\_global\_ip\_address\_pools\_global\_ip\_address\_pool\_id\_subpools\_count\_v1\_info \- new module
* ipam\_global\_ip\_address\_pools\_global\_ip\_address\_pool\_id\_subpools\_v1\_info \- new module
* ipam\_global\_ip\_address\_pools\_id\_v1 \- new module
* ipam\_global\_ip\_address\_pools\_id\_v1\_info \- new module
* ipam\_global\_ip\_address\_pools\_v1 \- new module
* ipam\_global\_ip\_address\_pools\_v1\_info \- new module
* ipam\_site\_ip\_address\_pools\_count\_v1\_info \- new module
* ipam\_site\_ip\_address\_pools\_id\_v1 \- new module
* ipam\_site\_ip\_address\_pools\_id\_v1\_info \- new module
* ipam\_site\_ip\_address\_pools\_v1 \- new module
* ipam\_site\_ip\_address\_pools\_v1\_info \- new module
* license\_deregister\_v1 \- new module
* license\_last\_operation\_status\_v1\_info \- new module
* license\_register\_v1 \- new module
* license\_renew\_v1 \- new module
* license\_status\_v1\_info \- new module
* network\_applications\_count\_v1\_info \- new module
* network\_applications\_trend\_analytics\_v1 \- new module
* network\_applications\_v1\_info \- new module
* network\_bugs\_results\_bugs\_count\_v1\_info \- new module
* network\_bugs\_results\_bugs\_id\_network\_devices\_count\_v1\_info \- new module
* network\_bugs\_results\_bugs\_id\_network\_devices\_network\_device\_id\_v1\_info \- new module
* network\_bugs\_results\_bugs\_id\_network\_devices\_v1\_info \- new module
* network\_bugs\_results\_bugs\_id\_v1\_info \- new module
* network\_bugs\_results\_bugs\_v1\_info \- new module
* network\_bugs\_results\_network\_devices\_count\_v1\_info \- new module
* network\_bugs\_results\_network\_devices\_network\_device\_id\_bugs\_count\_v1\_info \- new module
* network\_bugs\_results\_network\_devices\_network\_device\_id\_bugs\_id\_v1\_info \- new module
* network\_bugs\_results\_network\_devices\_network\_device\_id\_bugs\_v1\_info \- new module
* network\_bugs\_results\_network\_devices\_network\_device\_id\_v1\_info \- new module
* network\_bugs\_results\_network\_devices\_v1\_info \- new module
* network\_bugs\_results\_trend\_count\_v1\_info \- new module
* network\_bugs\_results\_trend\_v1\_info \- new module
* network\_bugs\_trials\_v1 \- new module
* network\_bugs\_trials\_v1\_info \- new module
* network\_bugs\_trigger\_scan\_v1 \- new module
* network\_device\_config\_files\_count\_v1\_info \- new module
* network\_device\_config\_files\_id\_download\_masked\_v1 \- new module
* network\_device\_config\_files\_id\_download\_unmasked\_v1 \- new module
* network\_device\_config\_files\_id\_v1\_info \- new module
* network\_device\_config\_files\_v1\_info \- new module
* network\_device\_maintenance\_schedules\_count\_v1\_info \- new module
* network\_device\_maintenance\_schedules\_id\_v1 \- new module
* network\_device\_maintenance\_schedules\_id\_v1\_info \- new module
* network\_device\_maintenance\_schedules\_v1 \- new module
* network\_device\_maintenance\_schedules\_v1\_info \- new module
* network\_device\_replacements\_id\_v1\_info \- new module
* network\_device\_replacements\_v1\_info \- new module
* network\_devices\_delete\_with\_cleanup\_v1 \- new module
* network\_devices\_delete\_without\_cleanup\_v1 \- new module
* network\_devices\_id\_v1\_info \- new module
* network\_devices\_intent\_count\_v1\_info \- new module
* network\_devices\_intent\_v1\_info \- new module
* network\_devices\_top\_n\_analytics\_v1 \- new module
* network\_profiles\_for\_sites\_profile\_id\_templates\_count\_v1\_info \- new module
* network\_profiles\_for\_sites\_profile\_id\_templates\_v1\_info \- new module
* network\_settings\_workflow\_manager \- attribute \'force\_delete\' was added
* projects\_count\_v1\_info \- new module
* projects\_project\_id\_v1 \- new module
* projects\_project\_id\_v1\_info \- new module
* projects\_v1 \- new module
* projects\_v1\_info \- new module
* qos\_policy\_setting\_v1 \- new module
* qos\_policy\_setting\_v1\_info \- new module
* sda\_fabric\_devices\_workflow\_manager \- attribute \'delete\_fabric\_device\' was removed
* sda\_host\_port\_onboarding\_workflow\_manager \- attributes \'port\_channel\_details\'\, \'port\_assignment\_details\' were removed
* sda\_host\_port\_onboarding\_workflow\_manager \- attributes \'port\_channels\'\, \'fabric\_site\_name\_hierarchy\'\, \'port\_assignments\'\, \'wireless\_ssids\' were added
* sda\_pending\_fabric\_events\_apply\_v1 \- new module
* sda\_pending\_fabric\_events\_v1\_info \- new module
* security\_advisories\_results\_advisories\_count\_v1\_info \- new module
* security\_advisories\_results\_advisories\_id\_network\_devices\_count\_v1\_info \- new module
* security\_advisories\_results\_advisories\_id\_network\_devices\_network\_device\_id\_v1\_info \- new module
* security\_advisories\_results\_advisories\_id\_network\_devices\_v1\_info \- new module
* security\_advisories\_results\_advisories\_id\_v1\_info \- new module
* security\_advisories\_results\_advisories\_v1\_info \- new module
* security\_advisories\_results\_network\_devices\_network\_device\_id\_advisories\_count\_v1\_info \- new module
* security\_advisories\_results\_network\_devices\_network\_device\_id\_advisories\_id\_v1\_info \- new module
* security\_advisories\_results\_network\_devices\_network\_device\_id\_advisories\_v1\_info \- new module
* security\_advisories\_results\_network\_devices\_network\_device\_id\_v1\_info \- new module
* security\_advisories\_results\_network\_devices\_v1\_info \- new module
* security\_advisories\_results\_trend\_count\_v1\_info \- new module
* security\_advisories\_results\_trend\_v1\_info \- new module
* security\_advisories\_trials\_v1 \- new module
* security\_advisories\_trials\_v1\_info \- new module
* security\_advisories\_trigger\_scan\_v1 \- new module
* site\_health\_summaries\_id\_trend\_analytics\_v1\_info \- new module
* site\_health\_summaries\_trend\_analytics\_v1\_info \- new module
* site\_kpi\_summaries\_count\_v1\_info \- new module
* site\_kpi\_summaries\_id\_v1\_info \- new module
* site\_kpi\_summaries\_query\_count\_v1 \- new module
* site\_kpi\_summaries\_query\_v1 \- new module
* site\_kpi\_summaries\_summary\_analytics\_v1 \- new module
* site\_kpi\_summaries\_summary\_analytics\_v1\_info \- new module
* site\_kpi\_summaries\_top\_n\_analytics\_v1\_info \- new module
* site\_kpi\_summaries\_trend\_analytics\_v1 \- new module
* site\_kpi\_summaries\_v1\_info \- new module
* site\_wise\_images\_summary\_v1\_info \- new module
* sites\_site\_id\_wireless\_settings\_ssids\_id\_update\_v1 \- new module
* tags\_interfaces\_members\_associations\_bulk\_v1 \- new module
* tags\_network\_devices\_members\_associations\_bulk\_v1 \- new module
* templates\_template\_id\_network\_profiles\_for\_sites\_bulk\_create\_v1 \- new module
* templates\_template\_id\_network\_profiles\_for\_sites\_bulk\_delete\_v1 \- new module
* templates\_template\_id\_network\_profiles\_for\_sites\_count\_v1\_info \- new module
* templates\_template\_id\_network\_profiles\_for\_sites\_profile\_id\_delete\_v1 \- new module
* templates\_template\_id\_network\_profiles\_for\_sites\_v1 \- new module
* templates\_template\_id\_network\_profiles\_for\_sites\_v1\_info \- new module
* templates\_template\_id\_versions\_commit\_v1 \- new module
* templates\_template\_id\_versions\_count\_v1\_info \- new module
* templates\_template\_id\_versions\_v1\_info \- new module
* templates\_template\_id\_versions\_version\_id\_v1\_info \- new module
* transit\_network\_health\_summaries\_count\_v1\_info \- new module
* transit\_network\_health\_summaries\_id\_trend\_analytics\_v1\_info \- new module
* transit\_network\_health\_summaries\_id\_v1\_info \- new module
* transit\_network\_health\_summaries\_v1\_info \- new module
* virtual\_network\_health\_summaries\_count\_v1\_info \- new module
* virtual\_network\_health\_summaries\_id\_trend\_analytics\_v1\_info \- new module
* virtual\_network\_health\_summaries\_id\_v1\_info \- new module
* virtual\_network\_health\_summaries\_v1\_info \- new module
* wireless\_accesspoint\_configuration\_count\_v1\_info \- new module
* wireless\_controllers\_anchor\_capable\_devices\_v1\_info \- new module
* wireless\_controllers\_mesh\_ap\_neighbours\_count\_v1\_info \- new module
* wireless\_controllers\_mesh\_ap\_neighbours\_v1\_info \- new module
* wireless\_controllers\_network\_device\_id\_ap\_authorization\_lists\_v1\_info \- new module
* wireless\_profiles\_id\_policy\_tags\_bulk\_v1 \- new module
* wireless\_profiles\_id\_policy\_tags\_count\_v1\_info \- new module
* wireless\_profiles\_id\_policy\_tags\_policy\_tag\_id\_v1 \- new module
* wireless\_profiles\_id\_policy\_tags\_policy\_tag\_id\_v1\_info \- new module
* wireless\_profiles\_id\_site\_tags\_bulk\_v1 \- new module
* wireless\_profiles\_id\_site\_tags\_count\_v1\_info \- new module
* wireless\_profiles\_id\_site\_tags\_site\_tag\_id\_v1 \- new module
* wireless\_profiles\_id\_site\_tags\_site\_tag\_id\_v1\_info \- new module
* wireless\_profiles\_id\_site\_tags\_v1\_info \- new module
* wireless\_settings\_anchor\_groups\_count\_v1\_info \- new module
* wireless\_settings\_anchor\_groups\_id\_v1 \- new module
* wireless\_settings\_anchor\_groups\_id\_v1\_info \- new module
* wireless\_settings\_anchor\_groups\_v1 \- new module
* wireless\_settings\_anchor\_groups\_v1\_info \- new module
* wireless\_settings\_ap\_authorization\_lists\_count\_v1\_info \- new module
* wireless\_settings\_ap\_authorization\_lists\_id\_v1 \- new module
* wireless\_settings\_ap\_authorization\_lists\_id\_v1\_info \- new module
* wireless\_settings\_ap\_authorization\_lists\_v1 \- new module
* wireless\_settings\_ap\_authorization\_lists\_v1\_info \- new module
* wireless\_settings\_ap\_profiles\_count\_v1\_info \- new module
* wireless\_settings\_ap\_profiles\_id\_v1 \- new module
* wireless\_settings\_ap\_profiles\_id\_v1\_info \- new module
* wireless\_settings\_ap\_profiles\_v1 \- new module
* wireless\_settings\_ap\_profiles\_v1\_info \- new module
* wireless\_settings\_network\_device\_id\_assign\_anchor\_managed\_ap\_locations\_v1 \- new module
* wireless\_settings\_power\_profiles\_count\_v1\_info \- new module
* wireless\_settings\_power\_profiles\_id\_v1 \- new module
* wireless\_settings\_power\_profiles\_id\_v1\_info \- new module
* wireless\_settings\_power\_profiles\_v1 \- new module
* wireless\_settings\_power\_profiles\_v1\_info \- new module
* wireless\_settings\_ssids\_override\_at\_sites\_v1\_info \- new module

<a id="cisco-ios-6"></a>
#### cisco\.ios

* Added ios\_vrf\_interfaces resource module\,that helps with configuration of vrfs within interface
* Adds a new module <em class="title-reference">ios\_vrf\_address\_family</em> to manage VRFs address families on Cisco IOS devices\.

<a id="cisco-iosxr-1"></a>
#### cisco\.iosxr

* Added iosxr\_vrf\_interfaces resource module\, that helps with configuration of vrfs within interface\.
* Adds support for setting local\-preference with plus/minus values in route policies

<a id="cisco-ise"></a>
#### cisco\.ise

* Fix linting issues\.

<a id="cisco-meraki-5"></a>
#### cisco\.meraki

* Sanity and CI fixes\.
* administered\_identities\_me\_api\_keys\_info \- new plugin\.
* administered\_identities\_me\_api\_keys\_revoke \- new plugin\.
* devices\_live\_tools\_leds\_blink \- new plugin\.
* devices\_wireless\_electronic\_shelf\_label \- new plugin\.
* devices\_wireless\_electronic\_shelf\_label\_info \- new plugin\.
* networks\_appliance\_sdwan\_internet\_policies \- new plugin\.
* networks\_cancel \- new plugin\.
* networks\_floor\_plans\_auto\_locate\_jobs\_batch \- new plugin\.
* networks\_floor\_plans\_devices\_batch\_update \- new plugin\.
* networks\_publish \- new plugin\.
* networks\_recalculate \- new plugin\.
* networks\_wireless\_air\_marshal\_rules \- new plugin\.
* networks\_wireless\_air\_marshal\_rules\_delete \- new plugin\.
* networks\_wireless\_air\_marshal\_rules\_update \- new plugin\.
* networks\_wireless\_air\_marshal\_settings \- new plugin\.
* networks\_wireless\_electronic\_shelf\_label \- new plugin\.
* organizations\_assets \- new plugin\.
* organizations\_assurance\_alerts\_info \- new plugin\.
* organizations\_assurance\_alerts\_overview\_by\_network\_info \- new plugin\.
* organizations\_assurance\_alerts\_overview\_by\_type\_info \- new plugin\.
* organizations\_assurance\_alerts\_overview\_historical\_info \- new plugin\.
* organizations\_assurance\_alerts\_overview\_info \- new plugin\.
* organizations\_assurance\_alerts\_restore \- new plugin\.
* organizations\_cellular\_gateway\_esims\_inventory\_info \- new plugin\.
* organizations\_cellular\_gateway\_esims\_service\_providers\_accounts \- new plugin\.
* organizations\_cellular\_gateway\_esims\_service\_providers\_accounts\_communication\_plans\_info \- new plugin\.
* organizations\_cellular\_gateway\_esims\_service\_providers\_accounts\_info \- new plugin\.
* organizations\_cellular\_gateway\_esims\_service\_providers\_accounts\_rate\_plans\_info \- new plugin\.
* organizations\_cellular\_gateway\_esims\_service\_providers\_info \- new plugin\.
* organizations\_cellular\_gateway\_esims\_swap \- new plugin\.
* organizations\_devices\_details\_bulk\_update \- new plugin\.
* organizations\_devices\_overview\_by\_model\_info \- new plugin\.
* organizations\_floor\_plans\_auto\_locate\_devices\_info \- new plugin\.
* organizations\_floor\_plans\_auto\_locate\_statuses\_info \- new plugin\.
* organizations\_splash\_themes \- new plugin\.
* organizations\_splash\_themes\_info \- new plugin\.
* organizations\_summary\_top\_applications\_by\_usage\_info \- new plugin\.
* organizations\_summary\_top\_applications\_categories\_by\_usage\_info \- new plugin\.
* organizations\_switch\_ports\_clients\_overview\_by\_device\_info \- new plugin\.
* organizations\_switch\_ports\_overview\_info \- new plugin\.
* organizations\_switch\_ports\_statuses\_by\_switch\_info \- new plugin\.
* organizations\_switch\_ports\_topology\_discovery\_by\_device\_info \- new plugin\.
* organizations\_wireless\_air\_marshal\_rules\_info \- new plugin\.
* organizations\_wireless\_air\_marshal\_settings\_by\_network\_info \- new plugin\.
* organizations\_wireless\_clients\_overview\_by\_device\_info \- new plugin\.
* organizations\_wireless\_controller\_clients\_overview\_history\_by\_device\_by\_interval\_info \- new plugin\.
* organizations\_wireless\_controller\_connections\_info \- new plugin\.
* organizations\_wireless\_controller\_devices\_interfaces\_l2\_by\_device\_info \- new plugin\.
* organizations\_wireless\_controller\_devices\_interfaces\_l2\_statuses\_change\_history\_by\_device\_info \- new plugin\.
* organizations\_wireless\_controller\_devices\_interfaces\_l2\_usage\_history\_by\_interval\_info \- new plugin\.
* organizations\_wireless\_controller\_devices\_interfaces\_l3\_by\_device\_info \- new plugin\.
* organizations\_wireless\_controller\_devices\_interfaces\_l3\_statuses\_change\_history\_by\_device\_info \- new plugin\.
* organizations\_wireless\_controller\_devices\_interfaces\_l3\_usage\_history\_by\_interval\_info \- new plugin\.
* organizations\_wireless\_controller\_devices\_interfaces\_packets\_overview\_by\_device\_info \- new plugin\.
* organizations\_wireless\_controller\_devices\_interfaces\_usage\_history\_by\_interval\_info \- new plugin\.
* organizations\_wireless\_controller\_devices\_redundancy\_failover\_history\_info \- new plugin\.
* organizations\_wireless\_controller\_devices\_redundancy\_statuses\_info \- new plugin\.
* organizations\_wireless\_controller\_devices\_system\_utilization\_history\_by\_interval\_info \- new plugin\.
* organizations\_wireless\_controller\_overview\_by\_device\_info \- new plugin\.
* organizations\_wireless\_devices\_wireless\_controllers\_by\_device\_info \- new plugin\.
* organizations\_wireless\_radio\_auto\_rf\_channels\_recalculate \- new plugin\.
* organizations\_wireless\_rf\_profiles\_assignments\_by\_device\_info \- new plugin\.
* organizations\_wireless\_ssids\_statuses\_by\_device\_info \- new plugin\.

<a id="cisco-nxos-2"></a>
#### cisco\.nxos

* Add support for VRF address family via <em class="title-reference">vrf\_address\_family</em> resource module\.
* Added nxos\_vrf\_interfaces resource module\, that helps with configuration of vrfs within interface in favor of nxos\_vrf\_interface module\.
* nxos\_telemetry \- Added support for \'overridden\' state to provide complete configuration override capabilities\.

<a id="community-ciscosmb"></a>
#### community\.ciscosmb

* added Catalyst 1300 to supported platforms
* parsing neighbour table allowes empty 4th column to allow Cisco Catalyst 1300 support

<a id="community-crypto-5"></a>
#### community\.crypto

* acme\_certificate \- add compatibility for ACME CAs that are not fully RFC8555 compliant and do not provide <code>challenges</code> in authz objects \([https\://github\.com/ansible\-collections/community\.crypto/issues/824](https\://github\.com/ansible\-collections/community\.crypto/issues/824)\, [https\://github\.com/ansible\-collections/community\.crypto/pull/832](https\://github\.com/ansible\-collections/community\.crypto/pull/832)\)\.
* acme\_certificate \- add options <code>order\_creation\_error\_strategy</code> and <code>order\_creation\_max\_retries</code> which allow to configure the error handling behavior if creating a new ACME order fails\. This is particularly important when using the <code>include\_renewal\_cert\_id</code> option\, and the default value <code>auto</code> for <code>order\_creation\_error\_strategy</code> tries to gracefully handle related errors \([https\://github\.com/ansible\-collections/community\.crypto/pull/842](https\://github\.com/ansible\-collections/community\.crypto/pull/842)\)\.
* acme\_certificate \- allow to chose a profile for certificate generation\, in case the CA supports this using Internet\-Draft [draft\-aaron\-acme\-profiles](https\://datatracker\.ietf\.org/doc/draft\-aaron\-acme\-profiles/) \([https\://github\.com/ansible\-collections/community\.crypto/pull/835](https\://github\.com/ansible\-collections/community\.crypto/pull/835)\)\.
* acme\_certificate\_renewal\_info \- add <code>exists</code> and <code>parsable</code> return values and <code>treat\_parsing\_error\_as\_non\_existing</code> option \([https\://github\.com/ansible\-collections/community\.crypto/pull/838](https\://github\.com/ansible\-collections/community\.crypto/pull/838)\)\.
* luks\_device \- allow to provide passphrases base64\-encoded \([https\://github\.com/ansible\-collections/community\.crypto/issues/827](https\://github\.com/ansible\-collections/community\.crypto/issues/827)\, [https\://github\.com/ansible\-collections/community\.crypto/pull/829](https\://github\.com/ansible\-collections/community\.crypto/pull/829)\)\.
* x509\_certificate\_convert \- add new option <code>verify\_cert\_parsable</code> which allows to check whether the certificate can actually be parsed \([https\://github\.com/ansible\-collections/community\.crypto/issues/809](https\://github\.com/ansible\-collections/community\.crypto/issues/809)\, [https\://github\.com/ansible\-collections/community\.crypto/pull/830](https\://github\.com/ansible\-collections/community\.crypto/pull/830)\)\.

<a id="community-docker-6"></a>
#### community\.docker

* docker\_compose\_v2 \- add <code>ignore\_build\_events</code> option \(default value <code>true</code>\) which allows to \(not\) ignore build events for change detection \([https\://github\.com/ansible\-collections/community\.docker/issues/1005](https\://github\.com/ansible\-collections/community\.docker/issues/1005)\, [https\://github\.com/ansible\-collections/community\.docker/issues/pull/1011](https\://github\.com/ansible\-collections/community\.docker/issues/pull/1011)\)\.
* docker\_compose\_v2\* modules \- determine compose version with <code>docker compose version</code> and only then fall back to <code>docker info</code> \([https\://github\.com/ansible\-collections/community\.docker/pull/1021](https\://github\.com/ansible\-collections/community\.docker/pull/1021)\)\.
* docker\_image\_build \- <code>outputs\[\]\.name</code> can now be a list of strings \([https\://github\.com/ansible\-collections/community\.docker/pull/1006](https\://github\.com/ansible\-collections/community\.docker/pull/1006)\)\.
* docker\_image\_build \- the executed command is now returned in the <code>command</code> return value in case of success and some errors \([https\://github\.com/ansible\-collections/community\.docker/pull/1006](https\://github\.com/ansible\-collections/community\.docker/pull/1006)\)\.
* docker\_network \- added <code>ingress</code> option \([https\://github\.com/ansible\-collections/community\.docker/pull/999](https\://github\.com/ansible\-collections/community\.docker/pull/999)\)\.

<a id="community-general-18"></a>
#### community\.general

* MH module utils \- delegate <code>debug</code> to the underlying <code>AnsibleModule</code> instance or issues a warning if an attribute already exists with that name \([https\://github\.com/ansible\-collections/community\.general/pull/9577](https\://github\.com/ansible\-collections/community\.general/pull/9577)\)\.
* apache2\_mod\_proxy \- better handling regexp extraction \([https\://github\.com/ansible\-collections/community\.general/pull/9609](https\://github\.com/ansible\-collections/community\.general/pull/9609)\)\.
* apache2\_mod\_proxy \- change type of <code>state</code> to a list of strings\. No change for the users \([https\://github\.com/ansible\-collections/community\.general/pull/9600](https\://github\.com/ansible\-collections/community\.general/pull/9600)\)\.
* apache2\_mod\_proxy \- improve readability when using results from <code>fecth\_url\(\)</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9608](https\://github\.com/ansible\-collections/community\.general/pull/9608)\)\.
* apache2\_mod\_proxy \- refactor repeated code into method \([https\://github\.com/ansible\-collections/community\.general/pull/9599](https\://github\.com/ansible\-collections/community\.general/pull/9599)\)\.
* apache2\_mod\_proxy \- remove unused parameter and code from <code>Balancer</code> constructor \([https\://github\.com/ansible\-collections/community\.general/pull/9614](https\://github\.com/ansible\-collections/community\.general/pull/9614)\)\.
* apache2\_mod\_proxy \- simplified and improved string manipulation \([https\://github\.com/ansible\-collections/community\.general/pull/9614](https\://github\.com/ansible\-collections/community\.general/pull/9614)\)\.
* apache2\_mod\_proxy \- use <code>deps</code> to handle dependencies \([https\://github\.com/ansible\-collections/community\.general/pull/9612](https\://github\.com/ansible\-collections/community\.general/pull/9612)\)\.
* bitwarden lookup plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9324](https\://github\.com/ansible\-collections/community\.general/pull/9324)\)\.
* cgroup\_memory\_recap callback plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9583](https\://github\.com/ansible\-collections/community\.general/pull/9583)\)\.
* cgroup\_memory\_recap callback plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9321](https\://github\.com/ansible\-collections/community\.general/pull/9321)\)\.
* chef\_databag lookup plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9324](https\://github\.com/ansible\-collections/community\.general/pull/9324)\)\.
* chroot connection plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9584](https\://github\.com/ansible\-collections/community\.general/pull/9584)\)\.
* chroot connection plugin \- clean up string conversions \([https\://github\.com/ansible\-collections/community\.general/pull/9379](https\://github\.com/ansible\-collections/community\.general/pull/9379)\)\.
* chroot connection plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9322](https\://github\.com/ansible\-collections/community\.general/pull/9322)\)\.
* cloud\_init\_data\_facts \- open file using <code>open\(\)</code> as a context manager \([https\://github\.com/ansible\-collections/community\.general/pull/9579](https\://github\.com/ansible\-collections/community\.general/pull/9579)\)\.
* cobbler inventory plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9584](https\://github\.com/ansible\-collections/community\.general/pull/9584)\)\.
* cobbler inventory plugin \- clean up string conversions \([https\://github\.com/ansible\-collections/community\.general/pull/9379](https\://github\.com/ansible\-collections/community\.general/pull/9379)\)\.
* cobbler inventory plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9323](https\://github\.com/ansible\-collections/community\.general/pull/9323)\)\.
* collection\_version lookup plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9324](https\://github\.com/ansible\-collections/community\.general/pull/9324)\)\.
* consul\_kv lookup plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9324](https\://github\.com/ansible\-collections/community\.general/pull/9324)\)\.
* context\_demo callback plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9583](https\://github\.com/ansible\-collections/community\.general/pull/9583)\)\.
* context\_demo callback plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9321](https\://github\.com/ansible\-collections/community\.general/pull/9321)\)\.
* counter filter plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9585](https\://github\.com/ansible\-collections/community\.general/pull/9585)\)\.
* counter\_enabled callback plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9583](https\://github\.com/ansible\-collections/community\.general/pull/9583)\)\.
* counter\_enabled callback plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9321](https\://github\.com/ansible\-collections/community\.general/pull/9321)\)\.
* cpanm \- enable usage of option <code>\-\-with\-recommends</code> \([https\://github\.com/ansible\-collections/community\.general/issues/9554](https\://github\.com/ansible\-collections/community\.general/issues/9554)\, [https\://github\.com/ansible\-collections/community\.general/pull/9555](https\://github\.com/ansible\-collections/community\.general/pull/9555)\)\.
* cpanm \- enable usage of option <code>\-\-with\-suggests</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9555](https\://github\.com/ansible\-collections/community\.general/pull/9555)\)\.
* crc32 filter plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9585](https\://github\.com/ansible\-collections/community\.general/pull/9585)\)\.
* credstash lookup plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9324](https\://github\.com/ansible\-collections/community\.general/pull/9324)\)\.
* cronvar \- open file using <code>open\(\)</code> as a context manager \([https\://github\.com/ansible\-collections/community\.general/pull/9579](https\://github\.com/ansible\-collections/community\.general/pull/9579)\)\.
* crypttab \- open file using <code>open\(\)</code> as a context manager \([https\://github\.com/ansible\-collections/community\.general/pull/9579](https\://github\.com/ansible\-collections/community\.general/pull/9579)\)\.
* cyberarkpassword lookup plugin \- clean up string conversions \([https\://github\.com/ansible\-collections/community\.general/pull/9379](https\://github\.com/ansible\-collections/community\.general/pull/9379)\)\.
* cyberarkpassword lookup plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9324](https\://github\.com/ansible\-collections/community\.general/pull/9324)\)\.
* default\_without\_diff callback plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9583](https\://github\.com/ansible\-collections/community\.general/pull/9583)\)\.
* dense callback plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9583](https\://github\.com/ansible\-collections/community\.general/pull/9583)\)\.
* dense callback plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9321](https\://github\.com/ansible\-collections/community\.general/pull/9321)\)\.
* dependent lookup plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9324](https\://github\.com/ansible\-collections/community\.general/pull/9324)\)\.
* dict filter plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9585](https\://github\.com/ansible\-collections/community\.general/pull/9585)\)\.
* dict\_kv filter plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9585](https\://github\.com/ansible\-collections/community\.general/pull/9585)\)\.
* dig lookup plugin \- clean up string conversions \([https\://github\.com/ansible\-collections/community\.general/pull/9379](https\://github\.com/ansible\-collections/community\.general/pull/9379)\)\.
* dig lookup plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9324](https\://github\.com/ansible\-collections/community\.general/pull/9324)\)\.
* diy callback plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9583](https\://github\.com/ansible\-collections/community\.general/pull/9583)\)\.
* diy callback plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9321](https\://github\.com/ansible\-collections/community\.general/pull/9321)\)\.
* dnstxt lookup plugin \- clean up string conversions \([https\://github\.com/ansible\-collections/community\.general/pull/9379](https\://github\.com/ansible\-collections/community\.general/pull/9379)\)\.
* dnstxt lookup plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9324](https\://github\.com/ansible\-collections/community\.general/pull/9324)\)\.
* doas become plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9583](https\://github\.com/ansible\-collections/community\.general/pull/9583)\)\.
* doas become plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9319](https\://github\.com/ansible\-collections/community\.general/pull/9319)\)\.
* dsv lookup plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9324](https\://github\.com/ansible\-collections/community\.general/pull/9324)\)\.
* dzdo become plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9583](https\://github\.com/ansible\-collections/community\.general/pull/9583)\)\.
* dzdo become plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9319](https\://github\.com/ansible\-collections/community\.general/pull/9319)\)\.
* elastic callback plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9583](https\://github\.com/ansible\-collections/community\.general/pull/9583)\)\.
* elastic callback plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9321](https\://github\.com/ansible\-collections/community\.general/pull/9321)\)\.
* etcd lookup plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9324](https\://github\.com/ansible\-collections/community\.general/pull/9324)\)\.
* etcd3 lookup plugin \- clean up string conversions \([https\://github\.com/ansible\-collections/community\.general/pull/9379](https\://github\.com/ansible\-collections/community\.general/pull/9379)\)\.
* etcd3 lookup plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9324](https\://github\.com/ansible\-collections/community\.general/pull/9324)\)\.
* filetree lookup plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9324](https\://github\.com/ansible\-collections/community\.general/pull/9324)\)\.
* from\_csv filter plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9585](https\://github\.com/ansible\-collections/community\.general/pull/9585)\)\.
* from\_csv filter plugin \- clean up string conversions \([https\://github\.com/ansible\-collections/community\.general/pull/9379](https\://github\.com/ansible\-collections/community\.general/pull/9379)\)\.
* from\_ini filter plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9585](https\://github\.com/ansible\-collections/community\.general/pull/9585)\)\.
* from\_ini filter plugin \- clean up string conversions \([https\://github\.com/ansible\-collections/community\.general/pull/9379](https\://github\.com/ansible\-collections/community\.general/pull/9379)\)\.
* funcd connection plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9584](https\://github\.com/ansible\-collections/community\.general/pull/9584)\)\.
* funcd connection plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9322](https\://github\.com/ansible\-collections/community\.general/pull/9322)\)\.
* github\_app\_access\_token lookup plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9324](https\://github\.com/ansible\-collections/community\.general/pull/9324)\)\.
* gitlab\_instance\_variable \- add support for <code>raw</code> variables suboption \([https\://github\.com/ansible\-collections/community\.general/pull/9425](https\://github\.com/ansible\-collections/community\.general/pull/9425)\)\.
* gitlab\_runners inventory plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9584](https\://github\.com/ansible\-collections/community\.general/pull/9584)\)\.
* gitlab\_runners inventory plugin \- clean up string conversions \([https\://github\.com/ansible\-collections/community\.general/pull/9379](https\://github\.com/ansible\-collections/community\.general/pull/9379)\)\.
* gitlab\_runners inventory plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9323](https\://github\.com/ansible\-collections/community\.general/pull/9323)\)\.
* groupby\_as\_dict filter plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9585](https\://github\.com/ansible\-collections/community\.general/pull/9585)\)\.
* hashids filter plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9585](https\://github\.com/ansible\-collections/community\.general/pull/9585)\)\.
* hiera lookup plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9324](https\://github\.com/ansible\-collections/community\.general/pull/9324)\)\.
* icinga2 inventory plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9584](https\://github\.com/ansible\-collections/community\.general/pull/9584)\)\.
* icinga2 inventory plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9323](https\://github\.com/ansible\-collections/community\.general/pull/9323)\)\.
* incus connection plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9584](https\://github\.com/ansible\-collections/community\.general/pull/9584)\)\.
* incus connection plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9322](https\://github\.com/ansible\-collections/community\.general/pull/9322)\)\.
* iocage connection plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9584](https\://github\.com/ansible\-collections/community\.general/pull/9584)\)\.
* iocage connection plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9322](https\://github\.com/ansible\-collections/community\.general/pull/9322)\)\.
* iocage inventory plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9584](https\://github\.com/ansible\-collections/community\.general/pull/9584)\)\.
* iocage inventory plugin \- clean up string conversions \([https\://github\.com/ansible\-collections/community\.general/pull/9379](https\://github\.com/ansible\-collections/community\.general/pull/9379)\)\.
* iocage inventory plugin \- the new parameter <code>sudo</code> of the plugin lets the command <code>iocage list \-l</code> to run as root on the iocage host\. This is needed to get the IPv4 of a running DHCP jail \([https\://github\.com/ansible\-collections/community\.general/issues/9572](https\://github\.com/ansible\-collections/community\.general/issues/9572)\, [https\://github\.com/ansible\-collections/community\.general/pull/9573](https\://github\.com/ansible\-collections/community\.general/pull/9573)\)\.
* iptables\_state action plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9583](https\://github\.com/ansible\-collections/community\.general/pull/9583)\)\.
* iptables\_state action plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9318](https\://github\.com/ansible\-collections/community\.general/pull/9318)\)\.
* jabber callback plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9583](https\://github\.com/ansible\-collections/community\.general/pull/9583)\)\.
* jabber callback plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9321](https\://github\.com/ansible\-collections/community\.general/pull/9321)\)\.
* jail connection plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9584](https\://github\.com/ansible\-collections/community\.general/pull/9584)\)\.
* jail connection plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9322](https\://github\.com/ansible\-collections/community\.general/pull/9322)\)\.
* jc filter plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9585](https\://github\.com/ansible\-collections/community\.general/pull/9585)\)\.
* jira \- transition operation now has <code>status\_id</code> to directly reference wanted transition \([https\://github\.com/ansible\-collections/community\.general/pull/9602](https\://github\.com/ansible\-collections/community\.general/pull/9602)\)\.
* json\_query filter plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9585](https\://github\.com/ansible\-collections/community\.general/pull/9585)\)\.
* keep\_keys filter plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9585](https\://github\.com/ansible\-collections/community\.general/pull/9585)\)\.
* keycloak \- add an action group for Keycloak modules to allow <code>module\_defaults</code> to be set for Keycloak tasks \([https\://github\.com/ansible\-collections/community\.general/pull/9284](https\://github\.com/ansible\-collections/community\.general/pull/9284)\)\.
* keycloak\_\* modules \- <code>refresh\_token</code> parameter added\. When multiple authentication parameters are provided \(<code>token</code>\, <code>refresh\_token</code>\, and <code>auth\_username</code>/<code>auth\_password</code>\)\, modules will now automatically retry requests upon authentication errors \(401\)\, using in order the token\, refresh token\, and username/password \([https\://github\.com/ansible\-collections/community\.general/pull/9494](https\://github\.com/ansible\-collections/community\.general/pull/9494)\)\.
* keyring lookup plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9324](https\://github\.com/ansible\-collections/community\.general/pull/9324)\)\.
* known\_hosts \- open file using <code>open\(\)</code> as a context manager \([https\://github\.com/ansible\-collections/community\.general/pull/9579](https\://github\.com/ansible\-collections/community\.general/pull/9579)\)\.
* ksu become plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9583](https\://github\.com/ansible\-collections/community\.general/pull/9583)\)\.
* ksu become plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9319](https\://github\.com/ansible\-collections/community\.general/pull/9319)\)\.
* lastpass lookup plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9324](https\://github\.com/ansible\-collections/community\.general/pull/9324)\)\.
* linode inventory plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9584](https\://github\.com/ansible\-collections/community\.general/pull/9584)\)\.
* linode inventory plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9323](https\://github\.com/ansible\-collections/community\.general/pull/9323)\)\.
* lists filter plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9585](https\://github\.com/ansible\-collections/community\.general/pull/9585)\)\.
* lists\_mergeby filter plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9585](https\://github\.com/ansible\-collections/community\.general/pull/9585)\)\.
* lmdb\_kv lookup plugin \- clean up string conversions \([https\://github\.com/ansible\-collections/community\.general/pull/9379](https\://github\.com/ansible\-collections/community\.general/pull/9379)\)\.
* lmdb\_kv lookup plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9324](https\://github\.com/ansible\-collections/community\.general/pull/9324)\)\.
* locale\_gen \- invert the logic to determine <code>ubuntu\_mode</code>\, making it look first for <code>/etc/locale\.gen</code> \(set <code>ubuntu\_mode</code> to <code>False</code>\) and only then looking for <code>/var/lib/locales/supported\.d/</code> \(set <code>ubuntu\_mode</code> to <code>True</code>\) \([https\://github\.com/ansible\-collections/community\.general/pull/9238](https\://github\.com/ansible\-collections/community\.general/pull/9238)\, [https\://github\.com/ansible\-collections/community\.general/issues/9131](https\://github\.com/ansible\-collections/community\.general/issues/9131)\, [https\://github\.com/ansible\-collections/community\.general/issues/8487](https\://github\.com/ansible\-collections/community\.general/issues/8487)\)\.
* locale\_gen \- new return value <code>mechanism</code> to better express the semantics of the <code>ubuntu\_mode</code>\, with the possible values being either <code>glibc</code> \(<code>ubuntu\_mode\=False</code>\) or <code>ubuntu\_legacy</code> \(<code>ubuntu\_mode\=True</code>\) \([https\://github\.com/ansible\-collections/community\.general/pull/9238](https\://github\.com/ansible\-collections/community\.general/pull/9238)\)\.
* log\_plays callback plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9583](https\://github\.com/ansible\-collections/community\.general/pull/9583)\)\.
* log\_plays callback plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9321](https\://github\.com/ansible\-collections/community\.general/pull/9321)\)\.
* loganalytics callback plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9583](https\://github\.com/ansible\-collections/community\.general/pull/9583)\)\.
* loganalytics callback plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9321](https\://github\.com/ansible\-collections/community\.general/pull/9321)\)\.
* logdna callback plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9583](https\://github\.com/ansible\-collections/community\.general/pull/9583)\)\.
* logdna callback plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9321](https\://github\.com/ansible\-collections/community\.general/pull/9321)\)\.
* logentries callback plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9583](https\://github\.com/ansible\-collections/community\.general/pull/9583)\)\.
* logentries callback plugin \- clean up string conversions \([https\://github\.com/ansible\-collections/community\.general/pull/9379](https\://github\.com/ansible\-collections/community\.general/pull/9379)\)\.
* logentries callback plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9321](https\://github\.com/ansible\-collections/community\.general/pull/9321)\)\.
* logstash callback plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9583](https\://github\.com/ansible\-collections/community\.general/pull/9583)\)\.
* lxc connection plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9584](https\://github\.com/ansible\-collections/community\.general/pull/9584)\)\.
* lxc connection plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9322](https\://github\.com/ansible\-collections/community\.general/pull/9322)\)\.
* lxd connection plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9584](https\://github\.com/ansible\-collections/community\.general/pull/9584)\)\.
* lxd connection plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9322](https\://github\.com/ansible\-collections/community\.general/pull/9322)\)\.
* lxd inventory plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9584](https\://github\.com/ansible\-collections/community\.general/pull/9584)\)\.
* lxd inventory plugin \- clean up string conversions \([https\://github\.com/ansible\-collections/community\.general/pull/9379](https\://github\.com/ansible\-collections/community\.general/pull/9379)\)\.
* lxd inventory plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9323](https\://github\.com/ansible\-collections/community\.general/pull/9323)\)\.
* machinectl become plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9583](https\://github\.com/ansible\-collections/community\.general/pull/9583)\)\.
* machinectl become plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9319](https\://github\.com/ansible\-collections/community\.general/pull/9319)\)\.
* mail callback plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9583](https\://github\.com/ansible\-collections/community\.general/pull/9583)\)\.
* mail callback plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9321](https\://github\.com/ansible\-collections/community\.general/pull/9321)\)\.
* manageiq\_alert\_profiles \- improve handling of parameter requirements \([https\://github\.com/ansible\-collections/community\.general/pull/9449](https\://github\.com/ansible\-collections/community\.general/pull/9449)\)\.
* manifold lookup plugin \- clean up string conversions \([https\://github\.com/ansible\-collections/community\.general/pull/9379](https\://github\.com/ansible\-collections/community\.general/pull/9379)\)\.
* manifold lookup plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9324](https\://github\.com/ansible\-collections/community\.general/pull/9324)\)\.
* memcached cache plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9583](https\://github\.com/ansible\-collections/community\.general/pull/9583)\)\.
* memcached cache plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9320](https\://github\.com/ansible\-collections/community\.general/pull/9320)\)\.
* merge\_variables lookup plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9324](https\://github\.com/ansible\-collections/community\.general/pull/9324)\)\.
* nmap inventory plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9584](https\://github\.com/ansible\-collections/community\.general/pull/9584)\)\.
* nmap inventory plugin \- clean up string conversions \([https\://github\.com/ansible\-collections/community\.general/pull/9379](https\://github\.com/ansible\-collections/community\.general/pull/9379)\)\.
* nmap inventory plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9323](https\://github\.com/ansible\-collections/community\.general/pull/9323)\)\.
* nmcli \- add a option <code>fail\_over\_mac</code> \([https\://github\.com/ansible\-collections/community\.general/issues/9570](https\://github\.com/ansible\-collections/community\.general/issues/9570)\, [https\://github\.com/ansible\-collections/community\.general/pull/9571](https\://github\.com/ansible\-collections/community\.general/pull/9571)\)\.
* nrdp callback plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9583](https\://github\.com/ansible\-collections/community\.general/pull/9583)\)\.
* nrdp callback plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9321](https\://github\.com/ansible\-collections/community\.general/pull/9321)\)\.
* null callback plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9583](https\://github\.com/ansible\-collections/community\.general/pull/9583)\)\.
* one\_template \- adds <code>filter</code> option for retrieving templates which are not owned by the user \([https\://github\.com/ansible\-collections/community\.general/pull/9547](https\://github\.com/ansible\-collections/community\.general/pull/9547)\, [https\://github\.com/ansible\-collections/community\.general/issues/9278](https\://github\.com/ansible\-collections/community\.general/issues/9278)\)\.
* onepassword lookup plugin \- clean up string conversions \([https\://github\.com/ansible\-collections/community\.general/pull/9379](https\://github\.com/ansible\-collections/community\.general/pull/9379)\)\.
* onepassword lookup plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9324](https\://github\.com/ansible\-collections/community\.general/pull/9324)\)\.
* onepassword\_doc lookup plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9324](https\://github\.com/ansible\-collections/community\.general/pull/9324)\)\.
* online inventory plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9584](https\://github\.com/ansible\-collections/community\.general/pull/9584)\)\.
* online inventory plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9323](https\://github\.com/ansible\-collections/community\.general/pull/9323)\)\.
* opennebula inventory plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9584](https\://github\.com/ansible\-collections/community\.general/pull/9584)\)\.
* opennebula inventory plugin \- clean up string conversions \([https\://github\.com/ansible\-collections/community\.general/pull/9379](https\://github\.com/ansible\-collections/community\.general/pull/9379)\)\.
* opennebula inventory plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9323](https\://github\.com/ansible\-collections/community\.general/pull/9323)\)\.
* opentelemetry callback plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9583](https\://github\.com/ansible\-collections/community\.general/pull/9583)\)\.
* opentelemetry callback plugin \- remove code handling Python versions prior to 3\.7 \([https\://github\.com/ansible\-collections/community\.general/pull/9482](https\://github\.com/ansible\-collections/community\.general/pull/9482)\)\.
* opentelemetry callback plugin \- remove code handling Python versions prior to 3\.7 \([https\://github\.com/ansible\-collections/community\.general/pull/9503](https\://github\.com/ansible\-collections/community\.general/pull/9503)\)\.
* opentelemetry callback plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9321](https\://github\.com/ansible\-collections/community\.general/pull/9321)\)\.
* pacemaker\_cluster \- remove unused code \([https\://github\.com/ansible\-collections/community\.general/pull/9471](https\://github\.com/ansible\-collections/community\.general/pull/9471)\)\.
* pacemaker\_cluster \- using safer mechanism to run external command \([https\://github\.com/ansible\-collections/community\.general/pull/9471](https\://github\.com/ansible\-collections/community\.general/pull/9471)\)\.
* parted \- open file using <code>open\(\)</code> as a context manager \([https\://github\.com/ansible\-collections/community\.general/pull/9579](https\://github\.com/ansible\-collections/community\.general/pull/9579)\)\.
* passwordstore lookup plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9324](https\://github\.com/ansible\-collections/community\.general/pull/9324)\)\.
* pbrun become plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9583](https\://github\.com/ansible\-collections/community\.general/pull/9583)\)\.
* pbrun become plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9319](https\://github\.com/ansible\-collections/community\.general/pull/9319)\)\.
* pfexec become plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9583](https\://github\.com/ansible\-collections/community\.general/pull/9583)\)\.
* pfexec become plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9319](https\://github\.com/ansible\-collections/community\.general/pull/9319)\)\.
* pickle cache plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9583](https\://github\.com/ansible\-collections/community\.general/pull/9583)\)\.
* pmrun become plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9583](https\://github\.com/ansible\-collections/community\.general/pull/9583)\)\.
* pmrun become plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9319](https\://github\.com/ansible\-collections/community\.general/pull/9319)\)\.
* proxmox \- refactors the proxmox module \([https\://github\.com/ansible\-collections/community\.general/pull/9225](https\://github\.com/ansible\-collections/community\.general/pull/9225)\)\.
* proxmox inventory plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9584](https\://github\.com/ansible\-collections/community\.general/pull/9584)\)\.
* proxmox inventory plugin \- clean up string conversions \([https\://github\.com/ansible\-collections/community\.general/pull/9379](https\://github\.com/ansible\-collections/community\.general/pull/9379)\)\.
* proxmox inventory plugin \- strip whitespace from <code>user</code>\, <code>token\_id</code>\, and <code>token\_secret</code> \([https\://github\.com/ansible\-collections/community\.general/issues/9227](https\://github\.com/ansible\-collections/community\.general/issues/9227)\, [https\://github\.com/ansible\-collections/community\.general/pull/9228/](https\://github\.com/ansible\-collections/community\.general/pull/9228/)\)\.
* proxmox inventory plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9323](https\://github\.com/ansible\-collections/community\.general/pull/9323)\)\.
* proxmox module utils \- add method <code>api\_task\_complete</code> that can wait for task completion and return error message \([https\://github\.com/ansible\-collections/community\.general/pull/9256](https\://github\.com/ansible\-collections/community\.general/pull/9256)\)\.
* proxmox\_backup \- refactor permission checking to improve code readability and maintainability \([https\://github\.com/ansible\-collections/community\.general/pull/9239](https\://github\.com/ansible\-collections/community\.general/pull/9239)\)\.
* proxmox\_pct\_remote connection plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9584](https\://github\.com/ansible\-collections/community\.general/pull/9584)\)\.
* proxmox\_template \- add support for checksum validation with new options <code>checksum\_algorithm</code> and <code>checksum</code> \([https\://github\.com/ansible\-collections/community\.general/issues/9553](https\://github\.com/ansible\-collections/community\.general/issues/9553)\, [https\://github\.com/ansible\-collections/community\.general/pull/9601](https\://github\.com/ansible\-collections/community\.general/pull/9601)\)\.
* pulp\_repo \- open file using <code>open\(\)</code> as a context manager \([https\://github\.com/ansible\-collections/community\.general/pull/9579](https\://github\.com/ansible\-collections/community\.general/pull/9579)\)\.
* qubes connection plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9584](https\://github\.com/ansible\-collections/community\.general/pull/9584)\)\.
* qubes connection plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9322](https\://github\.com/ansible\-collections/community\.general/pull/9322)\)\.
* random\_mac filter plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9585](https\://github\.com/ansible\-collections/community\.general/pull/9585)\)\.
* random\_pet lookup plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9324](https\://github\.com/ansible\-collections/community\.general/pull/9324)\)\.
* redfish\_info \- add command <code>GetAccountServiceConfig</code> to get full information about AccountService configuration \([https\://github\.com/ansible\-collections/community\.general/pull/9403](https\://github\.com/ansible\-collections/community\.general/pull/9403)\)\.
* redhat\_subscription \- open file using <code>open\(\)</code> as a context manager \([https\://github\.com/ansible\-collections/community\.general/pull/9579](https\://github\.com/ansible\-collections/community\.general/pull/9579)\)\.
* redis cache plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9583](https\://github\.com/ansible\-collections/community\.general/pull/9583)\)\.
* redis cache plugin \- clean up string conversions \([https\://github\.com/ansible\-collections/community\.general/pull/9379](https\://github\.com/ansible\-collections/community\.general/pull/9379)\)\.
* redis cache plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9320](https\://github\.com/ansible\-collections/community\.general/pull/9320)\)\.
* redis lookup plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9324](https\://github\.com/ansible\-collections/community\.general/pull/9324)\)\.
* remove\_keys filter plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9585](https\://github\.com/ansible\-collections/community\.general/pull/9585)\)\.
* replace\_keys filter plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9585](https\://github\.com/ansible\-collections/community\.general/pull/9585)\)\.
* revbitspss lookup plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9324](https\://github\.com/ansible\-collections/community\.general/pull/9324)\)\.
* reveal\_ansible\_type filter plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9585](https\://github\.com/ansible\-collections/community\.general/pull/9585)\)\.
* run0 become plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9583](https\://github\.com/ansible\-collections/community\.general/pull/9583)\)\.
* saltstack connection plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9584](https\://github\.com/ansible\-collections/community\.general/pull/9584)\)\.
* saltstack connection plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9322](https\://github\.com/ansible\-collections/community\.general/pull/9322)\)\.
* say callback plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9583](https\://github\.com/ansible\-collections/community\.general/pull/9583)\)\.
* say callback plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9321](https\://github\.com/ansible\-collections/community\.general/pull/9321)\)\.
* scaleway inventory plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9584](https\://github\.com/ansible\-collections/community\.general/pull/9584)\)\.
* scaleway inventory plugin \- clean up string conversions \([https\://github\.com/ansible\-collections/community\.general/pull/9379](https\://github\.com/ansible\-collections/community\.general/pull/9379)\)\.
* scaleway inventory plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9323](https\://github\.com/ansible\-collections/community\.general/pull/9323)\)\.
* selective callback plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9583](https\://github\.com/ansible\-collections/community\.general/pull/9583)\)\.
* selective callback plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9321](https\://github\.com/ansible\-collections/community\.general/pull/9321)\)\.
* sesu become plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9583](https\://github\.com/ansible\-collections/community\.general/pull/9583)\)\.
* sesu become plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9319](https\://github\.com/ansible\-collections/community\.general/pull/9319)\)\.
* shelvefile lookup plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9324](https\://github\.com/ansible\-collections/community\.general/pull/9324)\)\.
* shutdown action plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9583](https\://github\.com/ansible\-collections/community\.general/pull/9583)\)\.
* shutdown action plugin \- clean up string conversions \([https\://github\.com/ansible\-collections/community\.general/pull/9379](https\://github\.com/ansible\-collections/community\.general/pull/9379)\)\.
* shutdown action plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9318](https\://github\.com/ansible\-collections/community\.general/pull/9318)\)\.
* slack callback plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9583](https\://github\.com/ansible\-collections/community\.general/pull/9583)\)\.
* slack callback plugin \- clean up string conversions \([https\://github\.com/ansible\-collections/community\.general/pull/9379](https\://github\.com/ansible\-collections/community\.general/pull/9379)\)\.
* slack callback plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9321](https\://github\.com/ansible\-collections/community\.general/pull/9321)\)\.
* snap \- add return value <code>version</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9598](https\://github\.com/ansible\-collections/community\.general/pull/9598)\)\.
* snap\_alias \- add return value <code>version</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9598](https\://github\.com/ansible\-collections/community\.general/pull/9598)\)\.
* solaris\_zone \- open file using <code>open\(\)</code> as a context manager \([https\://github\.com/ansible\-collections/community\.general/pull/9579](https\://github\.com/ansible\-collections/community\.general/pull/9579)\)\.
* sorcery \- open file using <code>open\(\)</code> as a context manager \([https\://github\.com/ansible\-collections/community\.general/pull/9579](https\://github\.com/ansible\-collections/community\.general/pull/9579)\)\.
* splunk callback plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9583](https\://github\.com/ansible\-collections/community\.general/pull/9583)\)\.
* splunk callback plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9321](https\://github\.com/ansible\-collections/community\.general/pull/9321)\)\.
* stackpath\_compute inventory plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9584](https\://github\.com/ansible\-collections/community\.general/pull/9584)\)\.
* stackpath\_compute inventory plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9323](https\://github\.com/ansible\-collections/community\.general/pull/9323)\)\.
* sudosu become plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9583](https\://github\.com/ansible\-collections/community\.general/pull/9583)\)\.
* sudosu become plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9319](https\://github\.com/ansible\-collections/community\.general/pull/9319)\)\.
* sumologic callback plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9583](https\://github\.com/ansible\-collections/community\.general/pull/9583)\)\.
* syslog\_json callback plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9583](https\://github\.com/ansible\-collections/community\.general/pull/9583)\)\.
* time filter plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9585](https\://github\.com/ansible\-collections/community\.general/pull/9585)\)\.
* timestamp callback plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9583](https\://github\.com/ansible\-collections/community\.general/pull/9583)\)\.
* timestamp callback plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9321](https\://github\.com/ansible\-collections/community\.general/pull/9321)\)\.
* timezone \- open file using <code>open\(\)</code> as a context manager \([https\://github\.com/ansible\-collections/community\.general/pull/9579](https\://github\.com/ansible\-collections/community\.general/pull/9579)\)\.
* to\_ini filter plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9585](https\://github\.com/ansible\-collections/community\.general/pull/9585)\)\.
* to\_ini filter plugin \- clean up string conversions \([https\://github\.com/ansible\-collections/community\.general/pull/9379](https\://github\.com/ansible\-collections/community\.general/pull/9379)\)\.
* tss lookup plugin \- clean up string conversions \([https\://github\.com/ansible\-collections/community\.general/pull/9379](https\://github\.com/ansible\-collections/community\.general/pull/9379)\)\.
* tss lookup plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9324](https\://github\.com/ansible\-collections/community\.general/pull/9324)\)\.
* ufw \- add support for <code>vrrp</code> protocol \([https\://github\.com/ansible\-collections/community\.general/issues/9562](https\://github\.com/ansible\-collections/community\.general/issues/9562)\, [https\://github\.com/ansible\-collections/community\.general/pull/9582](https\://github\.com/ansible\-collections/community\.general/pull/9582)\)\.
* unicode\_normalize filter plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9585](https\://github\.com/ansible\-collections/community\.general/pull/9585)\)\.
* unixy callback plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9583](https\://github\.com/ansible\-collections/community\.general/pull/9583)\)\.
* unixy callback plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9321](https\://github\.com/ansible\-collections/community\.general/pull/9321)\)\.
* version\_sort filter plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9585](https\://github\.com/ansible\-collections/community\.general/pull/9585)\)\.
* virtualbox inventory plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9584](https\://github\.com/ansible\-collections/community\.general/pull/9584)\)\.
* virtualbox inventory plugin \- clean up string conversions \([https\://github\.com/ansible\-collections/community\.general/pull/9379](https\://github\.com/ansible\-collections/community\.general/pull/9379)\)\.
* virtualbox inventory plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9323](https\://github\.com/ansible\-collections/community\.general/pull/9323)\)\.
* xbps \- add <code>root</code> and <code>repository</code> options to enable bootstrapping new void installations \([https\://github\.com/ansible\-collections/community\.general/pull/9174](https\://github\.com/ansible\-collections/community\.general/pull/9174)\)\.
* xen\_orchestra inventory plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9584](https\://github\.com/ansible\-collections/community\.general/pull/9584)\)\.
* xen\_orchestra inventory plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9323](https\://github\.com/ansible\-collections/community\.general/pull/9323)\)\.
* xfconf \- add return value <code>version</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9226](https\://github\.com/ansible\-collections/community\.general/pull/9226)\)\.
* xfconf\_info \- add return value <code>version</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9226](https\://github\.com/ansible\-collections/community\.general/pull/9226)\)\.
* yaml cache plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9583](https\://github\.com/ansible\-collections/community\.general/pull/9583)\)\.
* yaml callback plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9583](https\://github\.com/ansible\-collections/community\.general/pull/9583)\)\.
* yaml callback plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9321](https\://github\.com/ansible\-collections/community\.general/pull/9321)\)\.
* zone connection plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9584](https\://github\.com/ansible\-collections/community\.general/pull/9584)\)\.
* zone connection plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9322](https\://github\.com/ansible\-collections/community\.general/pull/9322)\)\.
* zypper \- add <code>quiet</code> option \([https\://github\.com/ansible\-collections/community\.general/pull/9270](https\://github\.com/ansible\-collections/community\.general/pull/9270)\)\.
* zypper \- add <code>simple\_errors</code> option \([https\://github\.com/ansible\-collections/community\.general/pull/9270](https\://github\.com/ansible\-collections/community\.general/pull/9270)\)\.

<a id="community-hrobot-4"></a>
#### community\.hrobot

* All modules and plugins now have a <code>rate\_limit\_retry\_timeout</code> option\, which allows to configure for how long to wait in case of rate limiting errors\. By default\, the modules wait indefinitely\. Setting the option to <code>0</code> does not retry \(this was the behavior in previous versions\)\, and a positive value sets a number of seconds to wait at most \([https\://github\.com/ansible\-collections/community\.hrobot/pull/140](https\://github\.com/ansible\-collections/community\.hrobot/pull/140)\)\.
* boot \- it is now possible to specify SSH public keys in <code>authorized\_keys</code>\. The fingerprint needed by the Robot API will be extracted automatically \([https\://github\.com/ansible\-collections/community\.hrobot/pull/134](https\://github\.com/ansible\-collections/community\.hrobot/pull/134)\)\.
* v\_switch \- the module is now part of the <code>community\.hrobot\.robot</code> action group\, despite already being documented as part of it \([https\://github\.com/ansible\-collections/community\.hrobot/pull/136](https\://github\.com/ansible\-collections/community\.hrobot/pull/136)\)\.

<a id="community-mysql-4"></a>
#### community\.mysql

* mysql\_db \- added <code>zstd</code> \(de\)compression support for <code>import</code>/<code>dump</code> states \([https\://github\.com/ansible\-collections/community\.mysql/issues/696](https\://github\.com/ansible\-collections/community\.mysql/issues/696)\)\.
* mysql\_query \- returns the <code>execution\_time\_ms</code> list containing execution time per query in milliseconds\.

<a id="community-okd"></a>
#### community\.okd

* openshift\_auth \- fix issue where openshift\_auth module sometimes does not delete the auth token\. Based on stale PR \([https\://github\.com/openshift/community\.okd/pull/194](https\://github\.com/openshift/community\.okd/pull/194)\)\.

<a id="community-postgresql-8"></a>
#### community\.postgresql

* postgresql\_query \- returns the <em class="title-reference">execution\_time\_ms</em> list containing execution time per query in milliseconds \([https\://github\.com/ansible\-collections/community\.postgresql/issues/787](https\://github\.com/ansible\-collections/community\.postgresql/issues/787)\)\.

<a id="community-rabbitmq-2"></a>
#### community\.rabbitmq

* rabbitmq\_policy \- adjust the <em class="title-reference">apply\_to</em> parameter to also accept the new options <em class="title-reference">classic\_queues</em>\, <em class="title-reference">quorum\_queues</em> and <em class="title-reference">streams</em> which are supported since rabbitmq 3\.12

<a id="community-routeros-5"></a>
#### community\.routeros

* api\_info\, api\_modify \- add missing attribute <code>require\-message\-auth</code> for the <code>radius</code> path which exists since RouterOS version 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/issues/338](https\://github\.com/ansible\-collections/community\.routeros/issues/338)\, [https\://github\.com/ansible\-collections/community\.routeros/pull/339](https\://github\.com/ansible\-collections/community\.routeros/pull/339)\)\.
* api\_info\, api\_modify \- add support for the <code>routing filter community\-list</code> path implemented by RouterOS 7 and newer \([https\://github\.com/ansible\-collections/community\.routeros/pull/331](https\://github\.com/ansible\-collections/community\.routeros/pull/331)\)\.
* api\_info\, api\_modify \- add the <code>interface 6to4</code> path\. Used to manage IPv6 tunnels via tunnel\-brokers like HE\, where native IPv6 is not provided \([https\://github\.com/ansible\-collections/community\.routeros/pull/342](https\://github\.com/ansible\-collections/community\.routeros/pull/342)\)\.
* api\_info\, api\_modify \- add the <code>interface wireless access\-list</code> and <code>interface wireless connect\-list</code> paths \([https\://github\.com/ansible\-collections/community\.routeros/issues/284](https\://github\.com/ansible\-collections/community\.routeros/issues/284)\, [https\://github\.com/ansible\-collections/community\.routeros/pull/340](https\://github\.com/ansible\-collections/community\.routeros/pull/340)\)\.
* api\_info\, api\_modify \- add the <code>use\-interface\-duid</code> option for <code>ipv6 dhcp\-client</code> path\. This option prevents issues with Fritzbox modems and routers\, when using virtual interfaces \(like VLANs\) may create duplicated records in hosts config\, this breaks original \"expose\-host\" function\. Also add the <code>script</code>\, <code>custom\-duid</code> and <code>validate\-server\-duid</code> as backport from 7\.15 version update \([https\://github\.com/ansible\-collections/community\.routeros/pull/341](https\://github\.com/ansible\-collections/community\.routeros/pull/341)\)\.

<a id="community-vmware-12"></a>
#### community\.vmware

* vmware\_guest \- Add new cutomization spec param <em class="title-reference">domainOU</em>\. \([https\://github\.com/ansible\-collections/community\.vmware/issues/2275](https\://github\.com/ansible\-collections/community\.vmware/issues/2275)\)
* vmware\_guest \- Speedup network search \([https\://github\.com/ansible\-collections/community\.vmware/pull/2278](https\://github\.com/ansible\-collections/community\.vmware/pull/2278)\)\.
* vmware\_guest\_network \- Speedup network search \([https\://github\.com/ansible\-collections/community\.vmware/pull/2277](https\://github\.com/ansible\-collections/community\.vmware/pull/2277)\)\.

<a id="dellemc-openmanage-8"></a>
#### dellemc\.openmanage

* idrac\_certificates \-  This module is enhanced to support SSL CSR generation for 4096 key size\.
* omevv\_firmware\_repository\_profile \- This module allows to resync the repository profiles from the OpenManage Update Manager Plug\-in\.

<a id="dellemc-powerflex"></a>
#### dellemc\.powerflex

* Added Ansible role to support installation and uninstallation of SDT\.
* Info module is enhanced to support the listing of SDTs and NVMe hosts\.

<a id="f5networks-f5-modules-2"></a>
#### f5networks\.f5\_modules

* bigip\_virtual\_server \- Fixed issue \- Disabling/Enabling Virtual Server does not require profiles\, type in Update

<a id="google-cloud-3"></a>
#### google\.cloud

* gcp\_pubsub\_subscription \- allows to create GCS subscription

<a id="ibm-storage-virtualize-5"></a>
#### ibm\.storage\_virtualize

* ibm\_sv\_manage\_replication\_policy \- Added support for disaster recovery
* ibm\_sv\_manage\_storage\_partition \- Added support for partition migration and disaster recovery
* ibm\_sv\_manage\_truststore\_for\_replication \- Added support for enabling various options \(syslog\, RESTAPI\, vasa\, ipsec\, snmp and email\) for existing truststore
* ibm\_svc\_initial\_setup \- Added support for flashcopy default grain size and SI \(Storage Insights\) to be able to control partition migration
* ibm\_svc\_manage\_portset \- Added support for linking portset of 2 clusters for PBHA
* ibm\_svc\_manage\_volume \- Added support for converting thinclone volume\(s\) to clone
* ibm\_svc\_manage\_volumegroup \- Added support for disaster recovery and converting thinclone volumegroup to clone

<a id="kubernetes-core-3"></a>
#### kubernetes\.core

* Bump version of ansible\-lint to minimum 24\.7\.0 \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/765](https\://github\.com/ansible\-collections/kubernetes\.core/pull/765)\)\.
* Parameter insecure\_registry added to helm\_template as equivalent of insecure\-skip\-tls\-verify \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/805](https\://github\.com/ansible\-collections/kubernetes\.core/pull/805)\)\.
* k8s\_drain \- Improve error message for pod disruption budget when draining a node \([https\://github\.com/ansible\-collections/kubernetes\.core/issues/797](https\://github\.com/ansible\-collections/kubernetes\.core/issues/797)\)\.

<a id="lowlydba-sqlserver-2"></a>
#### lowlydba\.sqlserver

* Add new <em class="title-reference">login\_role</em> module to add/remove server roles for logins \([https\://github\.com/lowlydba/lowlydba\.sqlserver/pull/293](https\://github\.com/lowlydba/lowlydba\.sqlserver/pull/293)\)\.
* Add new user\_role module to manage users\' membership to database roles \([https\://github\.com/lowlydba/lowlydba\.sqlserver/pull/292](https\://github\.com/lowlydba/lowlydba\.sqlserver/pull/292)\)\.

<a id="microsoft-ad-3"></a>
#### microsoft\.ad

* Added support for Windows Server 2025
* domain \- Added <code>replication\_source\_dc</code> to specify the domain controller to use as the replication source for the new domain \- [https\://github\.com/ansible\-collections/microsoft\.ad/issues/159](https\://github\.com/ansible\-collections/microsoft\.ad/issues/159)
* domain\_controller \- Added <code>replication\_source\_dc</code> to specify the domain controller to use as the replication source for the new domain controller \- [https\://github\.com/ansible\-collections/microsoft\.ad/issues/159](https\://github\.com/ansible\-collections/microsoft\.ad/issues/159)
* microsoft\.ad\.user \- Added <code>groups\.permissions\_failure\_action</code> to control the behaviour when failing to modify the user\'s groups \- \([https\://github\.com/ansible\-collections/microsoft\.ad/issues/140](https\://github\.com/ansible\-collections/microsoft\.ad/issues/140)\)\.

<a id="vmware-vmware-4"></a>
#### vmware\.vmware

* \_vmware \- standardize getter method names and documentation
* argument specs \- Remove redundant argument specs\. Update pyvmomi modules to use new consolidated spec
* content\_template \- Fix bad reference of library variable that was refactored to library\_id
* doc fragments \- Remove redundant fragments\. Update pyvmomi modules to use new consolidated docs
* esxi\_host \- Added inventory plugin to gather info about ESXi hosts
* esxi\_maintenance\_mode \- migrate esxi maintenance module from community
* info \- Made vm\_name variable required only when state is set to present in content\_template module
* pyvmomi module base \- refactor class to use the pyvmomi shared client util class as a base
* rest module base \- refactor class to use the rest shared client util class as a base
* vms \- added vms inventory plugin\. consolidated shared docs/code with esxi hosts inventory plugin

<a id="vmware-vmware-rest-1"></a>
#### vmware\.vmware\_rest

* info \- changed relative links in README\.md to absolute links

<a id="deprecated-features-5"></a>
### Deprecated Features

* The <code>cisco\.asa</code> collection has been deprecated\.
  It will be removed from Ansible 12 if no one starts maintaining it again before Ansible 12\.
  See [Collections Removal Process for unmaintained collections](https\://docs\.ansible\.com/ansible/devel/community/collection\_contributors/collection\_package\_removal\.html\#unmaintained\-collections) for more details \([https\://forum\.ansible\.com/t/38960](https\://forum\.ansible\.com/t/38960)\)\.

<a id="amazon-aws-10"></a>
#### amazon\.aws

* autoscaling\_group \- the <code>decrement\_desired\_capacity</code> parameter has been deprecated and will be removed in release 14\.0\.0 of this collection\. Management of instances attached an autoscaling group can be performed using the  <code>amazon\.aws\.autoscaling\_instance</code> module \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2396](https\://github\.com/ansible\-collections/amazon\.aws/pull/2396)\)\.
* autoscaling\_group \- the <code>replace\_batch\_size</code>\, <code>lc\_check</code> and <code>lt\_check</code> parameters have been deprecated and will be removed in release 14\.0\.0 of this collection\. Rolling replacement of instances in an autoscaling group can be performed using the  <code>amazon\.aws\.autoscaling\_instance\_refresh</code> module \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2396](https\://github\.com/ansible\-collections/amazon\.aws/pull/2396)\)\.
* autoscaling\_group \- the functionality provided through the <code>detach\_instances</code> parameter has been deprecated and will be removed in release 14\.0\.0 of this collection\. Management of instances attached an autoscaling group can be performed using the  <code>amazon\.aws\.autoscaling\_instance</code> module \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2396](https\://github\.com/ansible\-collections/amazon\.aws/pull/2396)\)\.
* autoscaling\_group \- the functionality provided through the <code>replace\_all\_instances</code> parameter has been deprecated and will be removed in release 14\.0\.0 of this collection\. Rolling replacement of instances in an autoscaling group can be performed using the  <code>amazon\.aws\.autoscaling\_instance\_refresh</code> module \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2396](https\://github\.com/ansible\-collections/amazon\.aws/pull/2396)\)\.
* autoscaling\_group \- the functionality provided through the <code>replace\_instances</code> parameter has been deprecated and will be removed in release 14\.0\.0 of this collection\. Management of instances attached an autoscaling group can be performed using the  <code>amazon\.aws\.autoscaling\_instance</code> module \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2396](https\://github\.com/ansible\-collections/amazon\.aws/pull/2396)\)\.

<a id="community-crypto-6"></a>
#### community\.crypto

* Support for ansible\-core 2\.11\, 2\.12\, 2\.13\, 2\.14\, 2\.15\, and 2\.16 is deprecated\, and will be removed in the next major release \(community\.crypto 3\.0\.0\)\. Some modules might still work with some of these versions afterwards\, but we will no longer keep compatibility code that was needed to support them\. Note that this means that support for all Python versions before 3\.7 will be dropped\, also on the target side \([https\://github\.com/ansible\-collections/community\.crypto/issues/559](https\://github\.com/ansible\-collections/community\.crypto/issues/559)\, [https\://github\.com/ansible\-collections/community\.crypto/pull/839](https\://github\.com/ansible\-collections/community\.crypto/pull/839)\)\.
* Support for cryptography \< 3\.4 is deprecated\, and will be removed in the next major release \(community\.crypto 3\.0\.0\)\. Some modules might still work with older versions of cryptography\, but we will no longer keep compatibility code that was needed to support them \([https\://github\.com/ansible\-collections/community\.crypto/issues/559](https\://github\.com/ansible\-collections/community\.crypto/issues/559)\, [https\://github\.com/ansible\-collections/community\.crypto/pull/839](https\://github\.com/ansible\-collections/community\.crypto/pull/839)\)\.
* openssl\_pkcs12 \- the PyOpenSSL based backend is deprecated and will be removed from community\.crypto 3\.0\.0\. From that point on you need cryptography 3\.0 or newer to use this module \([https\://github\.com/ansible\-collections/community\.crypto/issues/667](https\://github\.com/ansible\-collections/community\.crypto/issues/667)\, [https\://github\.com/ansible\-collections/community\.crypto/pull/831](https\://github\.com/ansible\-collections/community\.crypto/pull/831)\)\.

<a id="community-general-19"></a>
#### community\.general

* MH module utils \- attribute <code>debug</code> definition in subclasses of MH is now deprecated\, as that name will become a delegation to <code>AnsibleModule</code> in community\.general 12\.0\.0\, and any such attribute will be overridden by that delegation in that version \([https\://github\.com/ansible\-collections/community\.general/pull/9577](https\://github\.com/ansible\-collections/community\.general/pull/9577)\)\.
* atomic\_container \- module is deprecated and will be removed in community\.general 13\.0\.0 \([https\://github\.com/ansible\-collections/community\.general/pull/9487](https\://github\.com/ansible\-collections/community\.general/pull/9487)\)\.
* atomic\_host \- module is deprecated and will be removed in community\.general 13\.0\.0 \([https\://github\.com/ansible\-collections/community\.general/pull/9487](https\://github\.com/ansible\-collections/community\.general/pull/9487)\)\.
* atomic\_image \- module is deprecated and will be removed in community\.general 13\.0\.0 \([https\://github\.com/ansible\-collections/community\.general/pull/9487](https\://github\.com/ansible\-collections/community\.general/pull/9487)\)\.
* facter \- module is deprecated and will be removed in community\.general 12\.0\.0\, use <code>community\.general\.facter\_facts</code> instead \([https\://github\.com/ansible\-collections/community\.general/pull/9451](https\://github\.com/ansible\-collections/community\.general/pull/9451)\)\.
* locale\_gen \- <code>ubuntu\_mode\=True</code>\, or <code>mechanism\=ubuntu\_legacy</code> is deprecated and will be removed in community\.general 13\.0\.0 \([https\://github\.com/ansible\-collections/community\.general/pull/9238](https\://github\.com/ansible\-collections/community\.general/pull/9238)\)\.
* proxmox \- removes default value <code>false</code> of <code>update</code> parameter\. This will be changed to a default of <code>true</code> in community\.general 11\.0\.0 \([https\://github\.com/ansible\-collections/community\.general/pull/9225](https\://github\.com/ansible\-collections/community\.general/pull/9225)\)\.
* pure module utils \- the module utils is deprecated and will be removed from community\.general 12\.0\.0\. The modules using this were removed in community\.general 3\.0\.0 \([https\://github\.com/ansible\-collections/community\.general/pull/9432](https\://github\.com/ansible\-collections/community\.general/pull/9432)\)\.
* purestorage doc fragments \- the doc fragment is deprecated and will be removed from community\.general 12\.0\.0\. The modules using this were removed in community\.general 3\.0\.0 \([https\://github\.com/ansible\-collections/community\.general/pull/9432](https\://github\.com/ansible\-collections/community\.general/pull/9432)\)\.
* sensu\_check \- module is deprecated and will be removed in community\.general 13\.0\.0\, use collection <code>sensu\.sensu\_go</code> instead \([https\://github\.com/ansible\-collections/community\.general/pull/9483](https\://github\.com/ansible\-collections/community\.general/pull/9483)\)\.
* sensu\_client \- module is deprecated and will be removed in community\.general 13\.0\.0\, use collection <code>sensu\.sensu\_go</code> instead \([https\://github\.com/ansible\-collections/community\.general/pull/9483](https\://github\.com/ansible\-collections/community\.general/pull/9483)\)\.
* sensu\_handler \- module is deprecated and will be removed in community\.general 13\.0\.0\, use collection <code>sensu\.sensu\_go</code> instead \([https\://github\.com/ansible\-collections/community\.general/pull/9483](https\://github\.com/ansible\-collections/community\.general/pull/9483)\)\.
* sensu\_silence \- module is deprecated and will be removed in community\.general 13\.0\.0\, use collection <code>sensu\.sensu\_go</code> instead \([https\://github\.com/ansible\-collections/community\.general/pull/9483](https\://github\.com/ansible\-collections/community\.general/pull/9483)\)\.
* sensu\_subscription \- module is deprecated and will be removed in community\.general 13\.0\.0\, use collection <code>sensu\.sensu\_go</code> instead \([https\://github\.com/ansible\-collections/community\.general/pull/9483](https\://github\.com/ansible\-collections/community\.general/pull/9483)\)\.
* slack \- the default value <code>auto</code> of the <code>prepend\_hash</code> option is deprecated and will change to <code>never</code> in community\.general 12\.0\.0 \([https\://github\.com/ansible\-collections/community\.general/pull/9443](https\://github\.com/ansible\-collections/community\.general/pull/9443)\)\.
* yaml callback plugin \- deprecate plugin in favor of <code>result\_format\=yaml</code> in plugin <code>ansible\.bulitin\.default</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9456](https\://github\.com/ansible\-collections/community\.general/pull/9456)\)\.

<a id="community-hrobot-5"></a>
#### community\.hrobot

* boot \- the various <code>arch</code> suboptions have been deprecated and will be removed from community\.hrobot 3\.0\.0 \([https\://github\.com/ansible\-collections/community\.hrobot/pull/134](https\://github\.com/ansible\-collections/community\.hrobot/pull/134)\)\.

<a id="community-vmware-13"></a>
#### community\.vmware

* vmware\_cluster\_info \- the module has been deprecated and will be removed in community\.vmware 7\.0\.0 \([https\://github\.com/ansible\-collections/community\.vmware/pull/2260](https\://github\.com/ansible\-collections/community\.vmware/pull/2260)\)\.

<a id="security-fixes"></a>
### Security Fixes

<a id="cloudscale-ch-cloud-3"></a>
#### cloudscale\_ch\.cloud

* Validate API tokens before passing them to Ansible\, to ensure that a badly formed one \(i\.e\.\, one with newlines\) is not accidentally logged\.

<a id="community-general-20"></a>
#### community\.general

* keycloak\_authentication \- API calls did not properly set the <code>priority</code> during update resulting in incorrectly sorted authentication flows\. This apparently only affects Keycloak 25 or newer \([https\://github\.com/ansible\-collections/community\.general/pull/9263](https\://github\.com/ansible\-collections/community\.general/pull/9263)\)\.
* keycloak\_client \- Sanitize <code>saml\.encryption\.private\.key</code> so it does not show in the logs \([https\://github\.com/ansible\-collections/community\.general/pull/9621](https\://github\.com/ansible\-collections/community\.general/pull/9621)\)\.

<a id="bugfixes-5"></a>
### Bugfixes

<a id="ansible-core-12"></a>
#### Ansible\-core

* Ansible will now also warn when reserved keywords are set via a module \(set\_fact\, include\_vars\, etc\)\.
* Ansible\.Basic \- Fix <code>required\_if</code> check when the option value to check is unset or set to null\.
* Use consistent multiprocessing context for action write locks
* ansible\-test \- Fix up coverage reporting to properly translate the temporary path of integration test modules to the expected static test module path\.
* ansible\-vault will now correctly handle <em class="title-reference">\-\-prompt</em>\, previously it would issue an error about stdin if no 2nd argument was passed
* copy action now prevents user from setting internal options\.
* gather\_facts action now defaults to <em class="title-reference">ansible\.legacy\.setup</em> if <em class="title-reference">smart</em> was set\, no network OS was found and no other alias for <em class="title-reference">setup</em> was present\.
* gather\_facts action will now issues errors and warnings as appropriate if a network OS is detected but no facts modules are defined for it\.
* ssh \- Improve the logic for parsing CLIXML data in stderr when working with Windows host\. This fixes issues when the raw stderr contains invalid UTF\-8 byte sequences and improves embedded CLIXML sequences\.
* ssh \- connection options were incorrectly templated during <code>reset\_connection</code> tasks \([https\://github\.com/ansible/ansible/pull/84238](https\://github\.com/ansible/ansible/pull/84238)\)\.

<a id="amazon-aws-11"></a>
#### amazon\.aws

* cloudformation \- Fix bug where termination protection is not updated when create\_changeset\=true is used for stack updates \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2391](https\://github\.com/ansible\-collections/amazon\.aws/pull/2391)\)\.
* ec2\_security\_group \- Fix the diff mode issue when creating a security group containing a rule with a managed prefix list \([https\://github\.com/ansible\-collections/amazon\.aws/issues/2373](https\://github\.com/ansible\-collections/amazon\.aws/issues/2373)\)\.
* ec2\_vpc\_net \- handle ipv6\_cidr <code>false</code> and no Ipv6CidrBlockAssociationSet in vpc \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2374](https\://github\.com/ansible\-collections/amazon\.aws/pull/2374)\)\.
* elbv2 \- Fix load balancer listener comparison when DefaultActions contain any action other than forward \([https\://github\.com/ansible\-collections/amazon\.aws/issues/2377](https\://github\.com/ansible\-collections/amazon\.aws/issues/2377)\)\.
* lambda \- Remove non UTF\-8 data \(contents of Lambda ZIP file\) from the module output to avoid Ansible error \([https\://github\.com/ansible\-collections/amazon\.aws/issues/2386](https\://github\.com/ansible\-collections/amazon\.aws/issues/2386)\)\.
* module\_utils/ec2 \- catch error code <code>InvalidElasticIpID\.NotFound</code> on function <code>create\_nat\_gateway\(\)</code>\, sometimes the <code>allocate\_address</code> API calls will return the ID for a new elastic IP resource before it can be consistently referenced \([https\://github\.com/ansible\-collections/amazon\.aws/issues/1872](https\://github\.com/ansible\-collections/amazon\.aws/issues/1872)\)\.
* rds\_cluster \- Fix issue occurring when updating RDS cluster domain \([https\://github\.com/ansible\-collections/amazon\.aws/issues/2390](https\://github\.com/ansible\-collections/amazon\.aws/issues/2390)\)\.

<a id="ansible-windows-3"></a>
#### ansible\.windows

* ansible\.windows\.win\_powershell \- Add extra checks to avoid <code>GetType</code> error when converting the output object \- ttps\://github\.com/ansible\-collections/ansible\.windows/issues/708
* win\_group\_membership \- Fix bug when input <code>members</code> contained duplicate members that were not already present in the group \- [https\://github\.com/ansible\-collections/ansible\.windows/issues/736](https\://github\.com/ansible\-collections/ansible\.windows/issues/736)
* win\_powershell \- Ensure <code>\$Ansible\.Result \= \@\(\)</code> as an empty array is returned as an empty list and not null \- [https\://github\.com/ansible\-collections/ansible\.windows/issues/686](https\://github\.com/ansible\-collections/ansible\.windows/issues/686)
* win\_updates \- Only set the Access control sections on the temporary directory created by the module\. This avoids the error when the <code>SeSecurityPrivilege</code> privilege isn\'t present\.

<a id="cisco-asa-1"></a>
#### cisco\.asa

* cisco\.asa \- fixed Cliconf\.edit\_config\(\) got an unexpected keyword argument \'candidate\' error
* cisco\.asa\.asa\_acls \- fixed ace parsing when source is object\-group and its name contains dots
* cisco\.asa\.asa\_acls \- fixed acl modification commands order if object/group name contains <em class="title-reference">no</em>

<a id="cisco-ios-7"></a>
#### cisco\.ios

* Added a test to validate the gathered state for VLAN configuration context\, improving reliability\.
* Cleaned up unit tests that were passing for the wrong reasons\. The updated tests now ensure the right config sections are verified for VLAN configurations\.
* Fix overridden state operations to ensure excluded VLANs in the provided configuration are removed\, thus overriding the VLAN configuration\.
* Fix purged state operation to enable users to completely remove VLAN configurations\.
* Fixed an issue with VLAN configuration gathering where pre\-filled data was blocking proper fetching of dynamic VLAN details\. Now VLAN facts are populated correctly for all cases\.
* Fixes an issue with facts gathering failing when an sub interface is in a deleted state\.
* Improve documentation to provide clarity on the \"shutdown\" variable\.
* Improve unit tests to align with the changes made\.
* Made improvements to ensure VLAN facts are gathered properly\, both for specific configurations and general VLAN settings\.
* ios\_route\_maps \- Fix removal of ACLs in replaced state to properly remove unspecified ACLs while leaving specified ones intact\.
* ios\_route\_maps \- Fix removal of ACLs logic in replaced state to properly remove unspecified ACLs while leaving specified ones intact\.

<a id="cisco-ise-1"></a>
#### cisco\.ise

* personas\_promote\_primary \- fix timeout issue\.

<a id="cisco-meraki-6"></a>
#### cisco\.meraki

* Ansible utils requirements updated\.
* Change alias \'message\' to \'message\_rule\' due is a reserved ansible word in meraki\_mx\_intrusion\_prevention module\.
* Issue fixes for workflow\-ansible\-lint\.
* Old playbook tests removed\.
* README fixes\.
* cisco\.meraki\.networks\_appliance\_firewall\_l3\_firewall\_rules fails with \"Unexpected failure during module execution \'rules\' \- specific \'rules\' extraction has been removed\.
* cisco\.meraki\.networks\_appliance\_vlans\_settings fails with \"msg\" \"Object does not exists\, plugin only has update\" \- specific \'vlansEnabled\' extraction has been removed\.
* cisco\.meraki\.networks\_clients\_info \- incorrect API endpoint\, fixing info module\.
* cisco\.meraki\.networks\_devices\_claim failed with error unexpected keyword argument \'add\_atomically\' \- bad naming solved\.
* cisco\.meraki\.networks\_switch\_stacks delete stack not working\, fixing path parameters\.
* runtime updated requires\_ansible from 2\.14\.0 to \'\>\=2\.15\.0\'\.

<a id="cisco-nxos-3"></a>
#### cisco\.nxos

* Fixed hardware fact gathering failure for CPU utilization parsing on NX\-OS 9\.3\(3\) by handling both list and single value formats of onemin\_percent
* Fixed the invalid feature name error for port\-security by updating the feature mapping from <em class="title-reference">eth\_port\_sec</em> to <em class="title-reference">eth\-port\-sec</em>\.
* Fixes mixed usage of f\-string and format string in action plugin for consistency\.
* Fixes nxos\_user purge deleting non\-local users\,ensuring only local users are removed\.
* \[bgp\_templates\] \- fix the show commands used to ensure task does not fail if BGP is not enabled on the device\.
* lag\_interfaces \- Fix bug where lag interfaces was not erroring on command failure\. \([https\://github\.com/ansible\-collections/cisco\.nxos/pull/923](https\://github\.com/ansible\-collections/cisco\.nxos/pull/923)\)
* nxos\_l2\_interfaces \- Fixed handling of \'none\' value in allowed\_vlans to properly set trunk VLAN none

<a id="community-crypto-7"></a>
#### community\.crypto

* crypto\_info \- when running the module on Fedora 41 with <code>cryptography</code> installed from the package repository\, the module crashed apparently due to some elliptic curves being removed from libssl against which cryptography is running\, which cryptography did not expect \([https\://github\.com/ansible\-collections/community\.crypto/pull/834](https\://github\.com/ansible\-collections/community\.crypto/pull/834)\)\.

<a id="community-dns-6"></a>
#### community\.dns

* Update Public Suffix List\.

<a id="community-docker-7"></a>
#### community\.docker

* Fix label sanitization code to avoid crashes in case of errors \([https\://github\.com/ansible\-collections/community\.docker/issues/1028](https\://github\.com/ansible\-collections/community\.docker/issues/1028)\, [https\://github\.com/ansible\-collections/community\.docker/pull/1029](https\://github\.com/ansible\-collections/community\.docker/pull/1029)\)\.
* docker\_compose\_v2 \- when using Compose 2\.31\.0 or newer\, revert to the old behavior that image rebuilds\, for example if <code>rebuild\=always</code>\, only result in <code>changed</code> if a container has been restarted \([https\://github\.com/ansible\-collections/community\.docker/issues/1005](https\://github\.com/ansible\-collections/community\.docker/issues/1005)\, [https\://github\.com/ansible\-collections/community\.docker/issues/pull/1011](https\://github\.com/ansible\-collections/community\.docker/issues/pull/1011)\)\.
* docker\_image\_build \- work around bug resp\. very unexpected behavior in Docker buildx that overwrites all image names in <code>\-\-output</code> parameters if <code>\-\-tag</code> is provided\, which the module did by default in the past\. The module now only supplies <code>\-\-tag</code> if <code>outputs</code> is empty\. If <code>outputs</code> has entries\, it will add an additional entry with <code>type\=image</code> if no entry of <code>type\=image</code> contains the image name specified by the <code>name</code> and <code>tag</code> options \([https\://github\.com/ansible\-collections/community\.docker/issues/1001](https\://github\.com/ansible\-collections/community\.docker/issues/1001)\, [https\://github\.com/ansible\-collections/community\.docker/pull/1006](https\://github\.com/ansible\-collections/community\.docker/pull/1006)\)\.
* docker\_network \- added waiting while container actually disconnect from Swarm network \([https\://github\.com/ansible\-collections/community\.docker/pull/999](https\://github\.com/ansible\-collections/community\.docker/pull/999)\)\.
* docker\_network \- containers are only reconnected to a network if they really exist \([https\://github\.com/ansible\-collections/community\.docker/pull/999](https\://github\.com/ansible\-collections/community\.docker/pull/999)\)\.
* docker\_network \- enabled \"force\" option in Docker network container disconnect API call \([https\://github\.com/ansible\-collections/community\.docker/pull/999](https\://github\.com/ansible\-collections/community\.docker/pull/999)\)\.
* docker\_swarm\_info \- do not crash when finding Swarm jobs if <code>services\=true</code> \([https\://github\.com/ansible\-collections/community\.docker/issues/1003](https\://github\.com/ansible\-collections/community\.docker/issues/1003)\)\.

<a id="community-general-21"></a>
#### community\.general

* dig lookup plugin \- correctly handle <code>NoNameserver</code> exception \([https\://github\.com/ansible\-collections/community\.general/pull/9363](https\://github\.com/ansible\-collections/community\.general/pull/9363)\, [https\://github\.com/ansible\-collections/community\.general/issues/9362](https\://github\.com/ansible\-collections/community\.general/issues/9362)\)\.
* homebrew \- fix incorrect handling of aliased homebrew modules when the alias is requested \([https\://github\.com/ansible\-collections/community\.general/pull/9255](https\://github\.com/ansible\-collections/community\.general/pull/9255)\, [https\://github\.com/ansible\-collections/community\.general/issues/9240](https\://github\.com/ansible\-collections/community\.general/issues/9240)\)\.
* homebrew \- fix incorrect handling of homebrew modules when a tap is requested \([https\://github\.com/ansible\-collections/community\.general/pull/9546](https\://github\.com/ansible\-collections/community\.general/pull/9546)\, [https\://github\.com/ansible\-collections/community\.general/issues/9533](https\://github\.com/ansible\-collections/community\.general/issues/9533)\)\.
* htpasswd \- report changes when file permissions are adjusted \([https\://github\.com/ansible\-collections/community\.general/issues/9485](https\://github\.com/ansible\-collections/community\.general/issues/9485)\, [https\://github\.com/ansible\-collections/community\.general/pull/9490](https\://github\.com/ansible\-collections/community\.general/pull/9490)\)\.
* iocage inventory plugin \- the plugin parses the IP4 tab of the jails list and put the elements into the new variable <code>iocage\_ip4\_dict</code>\. In multiple interface format the variable <code>iocage\_ip4</code> keeps the comma\-separated list of IP4 \([https\://github\.com/ansible\-collections/community\.general/issues/9538](https\://github\.com/ansible\-collections/community\.general/issues/9538)\)\.
* pipx \- honor option <code>global</code> when <code>state\=latest</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9623](https\://github\.com/ansible\-collections/community\.general/pull/9623)\)\.
* proxmox \- fixes idempotency of template conversions \([https\://github\.com/ansible\-collections/community\.general/pull/9225](https\://github\.com/ansible\-collections/community\.general/pull/9225)\, [https\://github\.com/ansible\-collections/community\.general/issues/8811](https\://github\.com/ansible\-collections/community\.general/issues/8811)\)\.
* proxmox \- fixes incorrect parsing for bind\-only mounts \([https\://github\.com/ansible\-collections/community\.general/pull/9225](https\://github\.com/ansible\-collections/community\.general/pull/9225)\, [https\://github\.com/ansible\-collections/community\.general/issues/8982](https\://github\.com/ansible\-collections/community\.general/issues/8982)\)\.
* proxmox \- fixes issues with disk\_volume variable \([https\://github\.com/ansible\-collections/community\.general/pull/9225](https\://github\.com/ansible\-collections/community\.general/pull/9225)\, [https\://github\.com/ansible\-collections/community\.general/issues/9065](https\://github\.com/ansible\-collections/community\.general/issues/9065)\)\.
* proxmox module utils \- fixes ignoring of <code>choose\_first\_if\_multiple</code> argument in <code>get\_vmid</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9225](https\://github\.com/ansible\-collections/community\.general/pull/9225)\)\.
* proxmox\_backup \- fix incorrect key lookup in vmid permission check \([https\://github\.com/ansible\-collections/community\.general/pull/9223](https\://github\.com/ansible\-collections/community\.general/pull/9223)\)\.
* proxmox\_disk \- fix async method and make <code>resize\_disk</code> method handle errors correctly \([https\://github\.com/ansible\-collections/community\.general/pull/9256](https\://github\.com/ansible\-collections/community\.general/pull/9256)\)\.
* proxmox\_template \- fix the wrong path called on <code>proxmox\_template\.task\_status</code> \([https\://github\.com/ansible\-collections/community\.general/issues/9276](https\://github\.com/ansible\-collections/community\.general/issues/9276)\, [https\://github\.com/ansible\-collections/community\.general/pull/9277](https\://github\.com/ansible\-collections/community\.general/pull/9277)\)\.
* qubes connection plugin \- fix the printing of debug information \([https\://github\.com/ansible\-collections/community\.general/pull/9334](https\://github\.com/ansible\-collections/community\.general/pull/9334)\)\.
* redfish\_utils module utils \- Fix <code>VerifyBiosAttributes</code> command on multi system resource nodes \([https\://github\.com/ansible\-collections/community\.general/pull/9234](https\://github\.com/ansible\-collections/community\.general/pull/9234)\)\.
* redhat\_subscription \- do not try to unsubscribe \(i\.e\. remove subscriptions\)
  when unregistering a system\: newer versions of subscription\-manager\, as
  available in EL 10 and Fedora 41\+\, do not support entitlements anymore\, and
  thus unsubscribing will fail
  \([https\://github\.com/ansible\-collections/community\.general/pull/9578](https\://github\.com/ansible\-collections/community\.general/pull/9578)\)\.

<a id="community-libvirt-2"></a>
#### community\.libvirt

* libvirt\_lxc \- add configuration for libvirt\_lxc\_noseclabel\.

<a id="community-postgresql-9"></a>
#### community\.postgresql

* postgresql\_info \- fix failure when a default database is used \(neither <code>db</code> nor <code>login\_db</code> are specified\) \([https\://github\.com/ansible\-collections/community\.postgresql/issues/794](https\://github\.com/ansible\-collections/community\.postgresql/issues/794)\)\.
* postgresql\_info \- fix issue when gathering information fails if user doesn\'t have access to all databases \([https\://github\.com/ansible\-collections/community\.postgresql/pull/788](https\://github\.com/ansible\-collections/community\.postgresql/pull/788)\)\.
* postgresql\_info \- fix module failure when the <code>db</code> parameter is used instead of <code>login\_db</code> \([https\://github\.com/ansible\-collections/community\.postgresql/issues/794](https\://github\.com/ansible\-collections/community\.postgresql/issues/794)\)\.
* postgresql\_pg\_hba \- fixes \#777 the module will ignore the \'address\' and \'netmask\' options again when the contype is \'local\' \([https\://github\.com/ansible\-collections/community\.postgresql/pull/779](https\://github\.com/ansible\-collections/community\.postgresql/pull/779)\)
* postgresql\_privs \-  fix the error occurring when trying to grant a function execution and set the schema to not\-specified \([https\://github\.com/ansible\-collections/community\.postgresql/pull/783](https\://github\.com/ansible\-collections/community\.postgresql/pull/783)\)\.

<a id="community-rabbitmq-3"></a>
#### community\.rabbitmq

* rabbitmq\_publish \- fix support for publishing headers as a part of a message \([https\://github\.com/ansible\-collections/community\.rabbitmq/pull/182](https\://github\.com/ansible\-collections/community\.rabbitmq/pull/182)\)

<a id="community-vmware-14"></a>
#### community\.vmware

* vmware\_guest \- setting vApp properties on virtual machines without vApp options raised an AttributeError\. Fix now gracefully handles a <em class="title-reference">None</em> value for vApp options when retrieving current vApp properties \([https\://github\.com/ansible\-collections/community\.vmware/pull/2220](https\://github\.com/ansible\-collections/community\.vmware/pull/2220)\)\.

<a id="dellemc-openmanage-9"></a>
#### dellemc\.openmanage

* idrac\_certificates \- \(Issue 737\) \- Fixed SSL CSR generation for 4096 key size\.

<a id="f5networks-f5-modules-3"></a>
#### f5networks\.f5\_modules

* bigip\_monitor\_external \- external monitor user\-defined variables not reflected for non\-common partition
* bigip\_profile\_server\_ssl \- Fixed bug \- create server SSL profile if SSL key is passphrase protected
* bigip\_snmp\_community \- Allow v3 usernames that begin with a number or contains any special characters\.

<a id="fortinet-fortios-3"></a>
#### fortinet\.fortios

* Fix errors in Ansible sanity test with Ansible\-core 2\.18
* Github

<a id="google-cloud-4"></a>
#### google\.cloud

* ansible \- 2\.17 is now the minimum version supported
* ansible \- 3\.11 is now the minimum Python version
* ansible\-test \- fixed sanity tests
* ansible\-test \- integration tests are now run against 2\.17 and 2\.18
* gcp\_bigquery\_table \- properly handle BigQuery table clustering fields
* gcp\_pubsub\_subscription \- fixed improper subscription uprade PATCH request

<a id="ibm-storage-virtualize-6"></a>
#### ibm\.storage\_virtualize

* ibm\_svc\_manage\_flashcopy \- Added support for creating flashcopy with existing target volume

<a id="kubernetes-core-4"></a>
#### kubernetes\.core

* helm \- Helm version checks did not support RC versions\. They now accept any version tags\. \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/745](https\://github\.com/ansible\-collections/kubernetes\.core/pull/745)\)\.
* helm\_pull \- Apply no\_log\=True to pass\_credentials to silence false positive warning\. \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/796](https\://github\.com/ansible\-collections/kubernetes\.core/pull/796)\)\.
* k8s\_drain \- Fix k8s\_drain does not wait for single pod \([https\://github\.com/ansible\-collections/kubernetes\.core/issues/769](https\://github\.com/ansible\-collections/kubernetes\.core/issues/769)\)\.
* k8s\_drain \- Fix k8s\_drain runs into a timeout when evicting a pod which is part of a stateful set  \([https\://github\.com/ansible\-collections/kubernetes\.core/issues/792](https\://github\.com/ansible\-collections/kubernetes\.core/issues/792)\)\.
* kubeconfig option should not appear in module invocation log \([https\://github\.com/ansible\-collections/kubernetes\.core/issues/782](https\://github\.com/ansible\-collections/kubernetes\.core/issues/782)\)\.
* kustomize \- kustomize plugin fails with deprecation warnings \([https\://github\.com/ansible\-collections/kubernetes\.core/issues/639](https\://github\.com/ansible\-collections/kubernetes\.core/issues/639)\)\.
* waiter \- Fix waiting for daemonset when desired number of pods is 0\. \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/756](https\://github\.com/ansible\-collections/kubernetes\.core/pull/756)\)\.

<a id="lowlydba-sqlserver-3"></a>
#### lowlydba\.sqlserver

* Fix error that occurred when creating a login with <em class="title-reference">skip\_password\_reset</em> as true\. \([https\://github\.com/lowlydba/lowlydba\.sqlserver/pull/287](https\://github\.com/lowlydba/lowlydba\.sqlserver/pull/287)\)
* Fix error when creating an agent job schedule with <em class="title-reference">enabled</em> as true\. \([https\://github\.com/lowlydba/lowlydba\.sqlserver/pull/288](https\://github\.com/lowlydba/lowlydba\.sqlserver/pull/288)\)

<a id="purestorage-flashblade-3"></a>
#### purestorage\.flashblade

* purefb\_bucket \- Fixed issue with idempotency reported when <code>hard\_limit</code> not provided\.
* purefb\_info \- Fixed <code>AttributeError</code> for <code>snapshot</code> subset when snapshot had been created manually\, rather than using a snapshot policy
* purefb\_info \- Fixed issue with admin token creation time and bucket policies
* purefb\_policy \- Fixed syntax error is account name\.
* purefb\_smtp \- Fix errors that occurred after adding support for smtp encrpytion and using the module on older FlashBlades\.
* purefb\_snap \- Fixed issue where <code>target</code> incorrectly required for a regular snapshot

<a id="vmware-vmware-5"></a>
#### vmware\.vmware

* client utils \- Fixed error message when required library could not be imported

<a id="vmware-vmware-rest-2"></a>
#### vmware\.vmware\_rest

* module\_utils \- fixed return value for vmware\.vmware\_rest\.vcenter\_vm\_guest\_filesystem\_directories module
* vcenter\_ovf\_libraryitem \- Update documentation to mention the metadata cannot be updated via conventional means\. Added example showing workaround \([https\://github\.com/ansible\-collections/vmware\.vmware\_rest/issues/385](https\://github\.com/ansible\-collections/vmware\.vmware\_rest/issues/385)\)

<a id="known-issues-4"></a>
### Known Issues

<a id="dellemc-openmanage-10"></a>
#### dellemc\.openmanage

* idrac\_diagnostics \- Issue\(285322\) \- This module doesn\'t support export of diagnostics file to HTTP and HTTPS share via SOCKS proxy\.
* idrac\_firmware \- Issue\(279282\) \- This module does not support firmware update using HTTP\, HTTPS\, and FTP shares with authentication on iDRAC8\.
* ome\_smart\_fabric\_uplink \- Issue\(186024\) \- The module supported by OpenManage Enterprise Modular\, however it does not allow the creation of multiple uplinks of the same name\. If an uplink is created using the same name as an existing uplink\, then the existing uplink is modified\.

<a id="new-plugins-3"></a>
### New Plugins

<a id="connection-1"></a>
#### Connection

* community\.general\.proxmox\_pct\_remote \- Run tasks in Proxmox LXC container instances using pct CLI via SSH\.

<a id="filter-1"></a>
#### Filter

* community\.general\.json\_diff \- Create a JSON patch by comparing two JSON files\.
* community\.general\.json\_patch \- Apply a JSON\-Patch \(RFC 6902\) operation to an object\.
* community\.general\.json\_patch\_recipe \- Apply JSON\-Patch \(RFC 6902\) operations to an object\.
* microsoft\.ad\.split\_dn \- Splits an LDAP DistinguishedName\.

<a id="inventory"></a>
#### Inventory

* community\.general\.iocage \- iocage inventory source\.

<a id="lookup-1"></a>
#### Lookup

* community\.general\.onepassword\_ssh\_key \- Fetch SSH keys stored in 1Password\.

<a id="new-modules-5"></a>
### New Modules

<a id="amazon-aws-12"></a>
#### amazon\.aws

* amazon\.aws\.rds\_instance\_param\_group\_info \- Describes the RDS parameter group\.

<a id="ansible-windows-4"></a>
#### ansible\.windows

* ansible\.windows\.win\_audit\_policy\_system \- Used to make changes to the system wide Audit Policy
* ansible\.windows\.win\_audit\_rule \- Adds an audit rule to files\, folders\, or registry keys
* ansible\.windows\.win\_auto\_logon \- Adds or Sets auto logon registry keys\.
* ansible\.windows\.win\_certificate\_info \- Get information on certificates from a Windows Certificate Store
* ansible\.windows\.win\_computer\_description \- Set windows description\, owner and organization
* ansible\.windows\.win\_credential \- Manages Windows Credentials in the Credential Manager
* ansible\.windows\.win\_dhcp\_lease \- Manage Windows Server DHCP Leases
* ansible\.windows\.win\_dns\_record \- Manage Windows Server DNS records
* ansible\.windows\.win\_dns\_zone \- Manage Windows Server DNS Zones
* ansible\.windows\.win\_eventlog \- Manage Windows event logs
* ansible\.windows\.win\_feature\_info \- Gather information about Windows features
* ansible\.windows\.win\_file\_compression \- Alters the compression of files and directories on NTFS partitions\.
* ansible\.windows\.win\_firewall \- Enable or disable the Windows Firewall
* ansible\.windows\.win\_hosts \- Manages hosts file entries on Windows\.
* ansible\.windows\.win\_hotfix \- Install and uninstalls Windows hotfixes
* ansible\.windows\.win\_http\_proxy \- Manages proxy settings for WinHTTP
* ansible\.windows\.win\_inet\_proxy \- Manages proxy settings for WinINet and Internet Explorer
* ansible\.windows\.win\_listen\_ports\_facts \- Recopilates the facts of the listening ports of the machine
* ansible\.windows\.win\_mapped\_drive \- Map network drives for users
* ansible\.windows\.win\_product\_facts \- Provides Windows product and license information
* ansible\.windows\.win\_region \- Set the region and format settings
* ansible\.windows\.win\_route \- Add or remove a static route
* ansible\.windows\.win\_timezone \- Sets Windows machine timezone
* ansible\.windows\.win\_user\_profile \- Manages the Windows user profiles\.

<a id="cisco-iosxr-2"></a>
#### cisco\.iosxr

* cisco\.iosxr\.iosxr\_vrf\_interfaces \- Resource module to configure VRF interfaces\.

<a id="cisco-nxos-4"></a>
#### cisco\.nxos

* cisco\.nxos\.nxos\_vrf\_address\_family \- Resource module to configure VRF address family definitions\.

<a id="community-crypto-8"></a>
#### community\.crypto

* community\.crypto\.acme\_certificate\_order\_create \- Create an ACME v2 order\.
* community\.crypto\.acme\_certificate\_order\_finalize \- Finalize an ACME v2 order\.
* community\.crypto\.acme\_certificate\_order\_info \- Obtain information for an ACME v2 order\.
* community\.crypto\.acme\_certificate\_order\_validate \- Validate authorizations of an ACME v2 order\.

<a id="community-general-22"></a>
#### community\.general

* community\.general\.android\_sdk \- Manages Android SDK packages\.
* community\.general\.ldap\_inc \- Use the Modify\-Increment LDAP V3 feature to increment an attribute value\.
* community\.general\.proxmox\_backup\_info \- Retrieve information on Proxmox scheduled backups\.
* community\.general\.systemd\_creds\_decrypt \- C\(systemd\)\'s C\(systemd\-creds decrypt\) plugin\.
* community\.general\.systemd\_creds\_encrypt \- C\(systemd\)\'s C\(systemd\-creds encrypt\) plugin\.

<a id="community-hrobot-6"></a>
#### community\.hrobot

* community\.hrobot\.storagebox \- Modify a storage box\'s basic configuration\.
* community\.hrobot\.storagebox\_info \- Query information on one or more storage boxes\.
* community\.hrobot\.storagebox\_set\_password \- \(Re\)set the password for a storage box\.
* community\.hrobot\.storagebox\_snapshot\_plan \- Modify a storage box\'s snapshot plans\.
* community\.hrobot\.storagebox\_snapshot\_plan\_info \- Query the snapshot plans for a storage box\.

<a id="dellemc-powerflex-1"></a>
#### dellemc\.powerflex

* dellemc\.powerflex\.nvme\_host \- Manage NVMe Hosts on Dell PowerFlex
* dellemc\.powerflex\.sdt \- Manage SDTs on Dell PowerFlex

<a id="kubernetes-core-5"></a>
#### kubernetes\.core

* kubernetes\.core\.helm\_registry\_auth \- Helm registry authentication module

<a id="lowlydba-sqlserver-4"></a>
#### lowlydba\.sqlserver

* lowlydba\.sqlserver\.login\_role \- Configures a login\'s  server roles\.
* lowlydba\.sqlserver\.user\_role \- Configures a user\'s role in a database\.

<a id="unchanged-collections-5"></a>
### Unchanged Collections

* ansible\.netcommon \(still version 7\.1\.0\)
* ansible\.posix \(still version 1\.6\.2\)
* ansible\.utils \(still version 5\.1\.2\)
* arista\.eos \(still version 10\.0\.1\)
* awx\.awx \(still version 24\.6\.1\)
* azure\.azcollection \(still version 3\.1\.0\)
* check\_point\.mgmt \(still version 6\.2\.1\)
* chocolatey\.chocolatey \(still version 1\.5\.3\)
* cisco\.aci \(still version 2\.10\.1\)
* cisco\.intersight \(still version 2\.0\.20\)
* cisco\.mso \(still version 2\.9\.0\)
* cloud\.common \(still version 4\.0\.0\)
* community\.aws \(still version 9\.0\.0\)
* community\.digitalocean \(still version 1\.27\.0\)
* community\.grafana \(still version 2\.1\.0\)
* community\.hashi\_vault \(still version 6\.2\.0\)
* community\.library\_inventory\_filtering\_v1 \(still version 1\.0\.2\)
* community\.network \(still version 5\.1\.0\)
* community\.proxysql \(still version 1\.6\.0\)
* community\.sap\_libs \(still version 1\.4\.2\)
* community\.windows \(still version 2\.3\.0\)
* community\.zabbix \(still version 3\.2\.0\)
* containers\.podman \(still version 1\.16\.2\)
* cyberark\.pas \(still version 1\.0\.30\)
* dellemc\.enterprise\_sonic \(still version 2\.5\.1\)
* dellemc\.unity \(still version 2\.0\.0\)
* fortinet\.fortimanager \(still version 2\.8\.2\)
* hetzner\.hcloud \(still version 4\.2\.2\)
* ibm\.qradar \(still version 4\.0\.0\)
* ibm\.spectrum\_virtualize \(still version 2\.0\.0\)
* ieisystem\.inmanage \(still version 3\.0\.0\)
* infinidat\.infinibox \(still version 1\.4\.5\)
* infoblox\.nios\_modules \(still version 1\.7\.1\)
* inspur\.ispim \(still version 2\.2\.3\)
* junipernetworks\.junos \(still version 9\.1\.0\)
* kaytus\.ksmanage \(still version 2\.0\.0\)
* kubevirt\.core \(still version 2\.1\.0\)
* netapp\.cloudmanager \(still version 21\.24\.0\)
* netapp\.ontap \(still version 22\.13\.0\)
* netapp\.storagegrid \(still version 21\.13\.0\)
* netapp\_eseries\.santricity \(still version 1\.4\.1\)
* netbox\.netbox \(still version 3\.20\.0\)
* ngine\_io\.cloudstack \(still version 2\.5\.0\)
* ovirt\.ovirt \(still version 3\.2\.0\)
* purestorage\.flasharray \(still version 1\.32\.0\)
* sensu\.sensu\_go \(still version 1\.14\.0\)
* splunk\.es \(still version 4\.0\.0\)
* theforeman\.foreman \(still version 4\.2\.0\)
* vultr\.cloud \(still version 1\.13\.0\)
* vyos\.vyos \(still version 5\.0\.0\)
* wti\.remote \(still version 1\.0\.10\)

<a id="v11-1-0"></a>
## v11\.1\.0

- <a href="#release-summary-6">Release Summary</a>
- <a href="#ansible-core-13">Ansible\-core</a>
- <a href="#changed-collections-6">Changed Collections</a>
- <a href="#major-changes-5">Major Changes</a>
    - <a href="#dellemc-openmanage-11">dellemc\.openmanage</a>
- <a href="#minor-changes-6">Minor Changes</a>
    - <a href="#ansible-core-14">Ansible\-core</a>
    - <a href="#cisco-dnac-4">cisco\.dnac</a>
    - <a href="#community-dns-7">community\.dns</a>
    - <a href="#community-docker-8">community\.docker</a>
    - <a href="#community-general-23">community\.general</a>
    - <a href="#community-mysql-5">community\.mysql</a>
    - <a href="#community-postgresql-10">community\.postgresql</a>
    - <a href="#community-routeros-6">community\.routeros</a>
    - <a href="#community-vmware-15">community\.vmware</a>
    - <a href="#fortinet-fortimanager-4">fortinet\.fortimanager</a>
    - <a href="#netapp-ontap-2">netapp\.ontap</a>
    - <a href="#purestorage-flasharray-6">purestorage\.flasharray</a>
    - <a href="#vmware-vmware-6">vmware\.vmware</a>
- <a href="#deprecated-features-6">Deprecated Features</a>
    - <a href="#community-general-24">community\.general</a>
    - <a href="#vmware-vmware-rest-3">vmware\.vmware\_rest</a>
- <a href="#security-fixes-1">Security Fixes</a>
    - <a href="#ansible-core-15">Ansible\-core</a>
- <a href="#bugfixes-6">Bugfixes</a>
    - <a href="#ansible-core-16">Ansible\-core</a>
    - <a href="#cisco-ise-2">cisco\.ise</a>
    - <a href="#community-dns-8">community\.dns</a>
    - <a href="#community-docker-9">community\.docker</a>
    - <a href="#community-general-25">community\.general</a>
    - <a href="#community-mysql-6">community\.mysql</a>
    - <a href="#community-postgresql-11">community\.postgresql</a>
    - <a href="#community-routeros-7">community\.routeros</a>
    - <a href="#community-vmware-16">community\.vmware</a>
    - <a href="#community-zabbix-4">community\.zabbix</a>
    - <a href="#fortinet-fortimanager-5">fortinet\.fortimanager</a>
    - <a href="#hetzner-hcloud-1">hetzner\.hcloud</a>
    - <a href="#infoblox-nios-modules-1">infoblox\.nios\_modules</a>
    - <a href="#netapp-ontap-3">netapp\.ontap</a>
    - <a href="#purestorage-flasharray-7">purestorage\.flasharray</a>
    - <a href="#telekom-mms-icinga-director-3">telekom\_mms\.icinga\_director</a>
    - <a href="#vmware-vmware-7">vmware\.vmware</a>
    - <a href="#vmware-vmware-rest-4">vmware\.vmware\_rest</a>
- <a href="#known-issues-5">Known Issues</a>
    - <a href="#dellemc-openmanage-12">dellemc\.openmanage</a>
- <a href="#new-plugins-4">New Plugins</a>
    - <a href="#filter-2">Filter</a>
    - <a href="#lookup-2">Lookup</a>
- <a href="#new-modules-6">New Modules</a>
    - <a href="#community-general-26">community\.general</a>
    - <a href="#community-vmware-17">community\.vmware</a>
    - <a href="#fortinet-fortimanager-6">fortinet\.fortimanager</a>
    - <a href="#netapp-ontap-4">netapp\.ontap</a>
- <a href="#unchanged-collections-6">Unchanged Collections</a>

<a id="release-summary-6"></a>
### Release Summary

Release Date\: 2024\-12\-03

[Porting Guide](https\://docs\.ansible\.com/ansible/devel/porting\_guides\.html)

<a id="ansible-core-13"></a>
### Ansible\-core

Ansible 11\.1\.0 contains ansible\-core version 2\.18\.1\.
This is a newer version than version 2\.18\.0 contained in the previous Ansible release\.

The changes are reported in the combined changelog below\.

<a id="changed-collections-6"></a>
### Changed Collections

If not mentioned explicitly\, the changes are reported in the combined changelog below\.

| Collection                  | Ansible 11.0.0 | Ansible 11.1.0 | Notes                                                                                                                        |
| --------------------------- | -------------- | -------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| azure.azcollection          | 3.0.0          | 3.1.0          | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
| cisco.dnac                  | 6.22.0         | 6.25.0         |                                                                                                                              |
| cisco.ise                   | 2.9.5          | 2.9.6          |                                                                                                                              |
| community.dns               | 3.0.7          | 3.1.0          |                                                                                                                              |
| community.docker            | 4.0.1          | 4.1.0          |                                                                                                                              |
| community.general           | 10.0.1         | 10.1.0         |                                                                                                                              |
| community.mysql             | 3.10.3         | 3.11.0         |                                                                                                                              |
| community.postgresql        | 3.7.0          | 3.9.0          |                                                                                                                              |
| community.routeros          | 3.0.0          | 3.1.0          |                                                                                                                              |
| community.vmware            | 5.1.0          | 5.2.0          |                                                                                                                              |
| community.zabbix            | 3.1.2          | 3.2.0          |                                                                                                                              |
| cyberark.pas                | 1.0.27         | 1.0.30         | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
| dellemc.openmanage          | 9.8.0          | 9.9.0          |                                                                                                                              |
| fortinet.fortimanager       | 2.7.0          | 2.8.2          |                                                                                                                              |
| hetzner.hcloud              | 4.2.1          | 4.2.2          |                                                                                                                              |
| infoblox.nios_modules       | 1.7.0          | 1.7.1          |                                                                                                                              |
| netapp.ontap                | 22.12.0        | 22.13.0        |                                                                                                                              |
| openstack.cloud             | 2.2.0          | 2.3.0          | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
| purestorage.flasharray      | 1.31.1         | 1.32.0         |                                                                                                                              |
| telekom_mms.icinga_director | 2.2.0          | 2.2.1          |                                                                                                                              |
| vmware.vmware               | 1.6.0          | 1.7.1          |                                                                                                                              |
| vmware.vmware_rest          | 4.2.0          | 4.3.0          |                                                                                                                              |

<a id="major-changes-5"></a>
### Major Changes

<a id="dellemc-openmanage-11"></a>
#### dellemc\.openmanage

* omevv\_baseline\_profile \- This module allows to manage baseline profile\.
* omevv\_baseline\_profile\_info \- This module allows to retrieve baseline profile information\.
* omevv\_compliance\_info \- This module allows to retrieve firmware compliance reports\.

<a id="minor-changes-6"></a>
### Minor Changes

<a id="ansible-core-14"></a>
#### Ansible\-core

* ansible\-test \- When detection of the current container network fails\, a warning is now issued and execution continues\. This simplifies usage in cases where the current container cannot be inspected\, such as when running in GitHub Codespaces\.

<a id="cisco-dnac-4"></a>
#### cisco\.dnac

* Added support for bulk operations on multiple access points in accesspoint\_workflow\_manager
* Aliases were implemented to handle v1 and v2 of the API\.
* Bug fixes in inventory\_workflow\_manager
* Bug fixes in network\_settings\_workflow\_manager
* Bug fixes in sda\_fabric\_virtual\_networks\_workflow\_manager\.py
* Changes in circleci and yaml lint files
* Changes in circleci to run test cases in integration branch
* Changes in sda\_extranet\_policy\_workflow\_manager
* Changes in site\_workflow\_manager
* Enhancements in sda\_fabric\_devices\_workflow\_manager\.py to support route distribution protocol
* Enhancements in sda\_fabric\_sites\_zones\_workflow\_manager\.py
* Modifications due to documentation errors
* Removing duplicates in the discovery\.py module\. snmpRwCommunity property\.
* accesspoint\_workflow\_manager \- added attribute bulk\_update\_aps
* sda\_fabric\_devices\_workflow\_manager\.py \- added attribute route\_distribution\_protocol
* sda\_fabric\_sites\_zones\_workflow\_manager\.py \- added attribute site\_name\_hierarchy and removed attribute site\_name

<a id="community-dns-7"></a>
#### community\.dns

* all controller code \- modernize Python code \([https\://github\.com/ansible\-collections/community\.dns/pull/231](https\://github\.com/ansible\-collections/community\.dns/pull/231)\)\.

<a id="community-docker-8"></a>
#### community\.docker

* docker\_stack \- allow to add <code>\-\-detach\=false</code> option to <code>docker stack deploy</code> command \([https\://github\.com/ansible\-collections/community\.docker/pull/987](https\://github\.com/ansible\-collections/community\.docker/pull/987)\)\.

<a id="community-general-23"></a>
#### community\.general

* alternatives \- add <code>family</code> parameter that allows to utilize the <code>\-\-family</code> option available in RedHat version of update\-alternatives \([https\://github\.com/ansible\-collections/community\.general/issues/5060](https\://github\.com/ansible\-collections/community\.general/issues/5060)\, [https\://github\.com/ansible\-collections/community\.general/pull/9096](https\://github\.com/ansible\-collections/community\.general/pull/9096)\)\.
* cloudflare\_dns \- add support for <code>comment</code> and <code>tags</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9132](https\://github\.com/ansible\-collections/community\.general/pull/9132)\)\.
* deps module utils \- add <code>deps\.clear\(\)</code> to clear out previously declared dependencies \([https\://github\.com/ansible\-collections/community\.general/pull/9179](https\://github\.com/ansible\-collections/community\.general/pull/9179)\)\.
* homebrew \- greatly speed up module when multiple packages are passed in the <code>name</code> option \([https\://github\.com/ansible\-collections/community\.general/pull/9181](https\://github\.com/ansible\-collections/community\.general/pull/9181)\)\.
* homebrew \- remove duplicated package name validation \([https\://github\.com/ansible\-collections/community\.general/pull/9076](https\://github\.com/ansible\-collections/community\.general/pull/9076)\)\.
* iso\_extract \- adds <code>password</code> parameter that is passed to 7z \([https\://github\.com/ansible\-collections/community\.general/pull/9159](https\://github\.com/ansible\-collections/community\.general/pull/9159)\)\.
* launchd \- add <code>plist</code> option for services such as sshd\, where the plist filename doesn\'t match the service name \([https\://github\.com/ansible\-collections/community\.general/pull/9102](https\://github\.com/ansible\-collections/community\.general/pull/9102)\)\.
* nmcli \- add <code>sriov</code> parameter that enables support for SR\-IOV settings \([https\://github\.com/ansible\-collections/community\.general/pull/9168](https\://github\.com/ansible\-collections/community\.general/pull/9168)\)\.
* pipx \- add return value <code>version</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9180](https\://github\.com/ansible\-collections/community\.general/pull/9180)\)\.
* pipx\_info \- add return value <code>version</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9180](https\://github\.com/ansible\-collections/community\.general/pull/9180)\)\.
* proxmox\_template \- add server side artifact fetching support \([https\://github\.com/ansible\-collections/community\.general/pull/9113](https\://github\.com/ansible\-collections/community\.general/pull/9113)\)\.
* redfish\_command \- add <code>update\_custom\_oem\_header</code>\, <code>update\_custom\_oem\_params</code>\, and <code>update\_custom\_oem\_mime\_type</code> options \([https\://github\.com/ansible\-collections/community\.general/pull/9123](https\://github\.com/ansible\-collections/community\.general/pull/9123)\)\.
* redfish\_utils module utils \- remove redundant code \([https\://github\.com/ansible\-collections/community\.general/pull/9190](https\://github\.com/ansible\-collections/community\.general/pull/9190)\)\.
* rpm\_ostree\_pkg \- added the options <code>apply\_live</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9167](https\://github\.com/ansible\-collections/community\.general/pull/9167)\)\.
* rpm\_ostree\_pkg \- added the return value <code>needs\_reboot</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9167](https\://github\.com/ansible\-collections/community\.general/pull/9167)\)\.
* scaleway\_lb \- minor simplification in the code \([https\://github\.com/ansible\-collections/community\.general/pull/9189](https\://github\.com/ansible\-collections/community\.general/pull/9189)\)\.
* ssh\_config \- add <code>dynamicforward</code> option \([https\://github\.com/ansible\-collections/community\.general/pull/9192](https\://github\.com/ansible\-collections/community\.general/pull/9192)\)\.

<a id="community-mysql-5"></a>
#### community\.mysql

* mysql\_info \- adds the count of tables for each database to the returned values\. It is possible to exclude this new field using the <code>db\_table\_count</code> exclusion filter\. \([https\://github\.com/ansible\-collections/community\.mysql/pull/691](https\://github\.com/ansible\-collections/community\.mysql/pull/691)\)

<a id="community-postgresql-10"></a>
#### community\.postgresql

* postgresql\_pg\_hba \- changes ordering of entries that are identical except for the ip\-range\, but only if the ranges are of the same size\, this isn\'t breaking as ranges of equal size can\'t overlap \([https\://github\.com/ansible\-collections/community\.postgresql/pull/772](https\://github\.com/ansible\-collections/community\.postgresql/pull/772)\)
* postgresql\_pg\_hba \- orders auth\-options alphabetically\, this isn\'t breaking as the order of those options is not relevant to postgresql \([https\://github\.com/ansible\-collections/community\.postgresql/pull/772](https\://github\.com/ansible\-collections/community\.postgresql/pull/772)\)
* postgresql\_pg\_hba \- show the number of the line with the issue if parsing a file fails \([https\://github\.com/ansible\-collections/community\.postgresql/pull/766](https\://github\.com/ansible\-collections/community\.postgresql/pull/766)\)
* postgresql\_publication \- add possibility of creating publication with column list \([https\://github\.com/ansible\-collections/community\.postgresql/pull/763](https\://github\.com/ansible\-collections/community\.postgresql/pull/763)\)\.

<a id="community-routeros-6"></a>
#### community\.routeros

* api\_info\, api\_modify \- add missing fields <code>comment</code>\, <code>next\-pool</code> to <code>ip pool</code> path \([https\://github\.com/ansible\-collections/community\.routeros/pull/327](https\://github\.com/ansible\-collections/community\.routeros/pull/327)\)\.

<a id="community-vmware-15"></a>
#### community\.vmware

* vmware\.py \- Add logic for handling the case where the <em class="title-reference">datacenter</em> property is not provided\.
* vmware\_guest\_info \- <em class="title-reference">datacenter</em> property is now optional as it only required in cases where the VM is not uniquely identified by <em class="title-reference">name</em>\.

<a id="fortinet-fortimanager-4"></a>
#### fortinet\.fortimanager

* Supported FortiManager 6\.2\.13\, 6\.4\.15\, 7\.0\.13\, 7\.2\.8\, 7\.4\.5\, 7\.6\.1\. Added 1 new module\.
* Supported check diff for some modules except \"fmgr\_generic\"\. You can use \"ansible\-playbook \-i \<your\-host\-file\> \<your\-playbook\> \-\-check \-\-diff\" to check what changes your playbook will make to the FortiManager\.

<a id="netapp-ontap-2"></a>
#### netapp\.ontap

* all modules supporting only REST \- change in documentation for <em class="title-reference">use\_rest</em>\.
* all modules supporting only REST \- updated <em class="title-reference">extends\_documentation\_fragment</em> \& argument spec\.
* na\_ontap\_active\_directory \- return error message when attempting to modify <em class="title-reference">account\_name</em>\.
* na\_ontap\_bgp\_config \- REST only support for managing BGP configuration for a node\, requires ONTAP 9\.6 or later\.
* na\_ontap\_cifs\_privileges \- REST only support for managing privileges of the local or Active Directory user or group\, requires ONTAP 9\.10\.1 or later\.
* na\_ontap\_cifs\_server \- added new option <em class="title-reference">comment</em> for cifs server\, requires ONTAP 9\.6 or later\.
* na\_ontap\_flexcache \- new option to enable <em class="title-reference">writeback</em> added in REST\, requires ONTAP 9\.12 or later\.
* na\_ontap\_rest\_info \- removed example which has option <em class="title-reference">gather\_subset</em> set to <em class="title-reference">all</em> from documentation\.
* na\_ontap\_rest\_info \- updated <em class="title-reference">extends\_documentation\_fragment</em> \& argument spec\.
* na\_ontap\_s3\_buckets \- added new option <em class="title-reference">versioning\_state</em>\, requires ONTAP 9\.11\.1 or later\.
* na\_ontap\_s3\_buckets \- updated <em class="title-reference">extends\_documentation\_fragment</em> \& argument spec\.
* na\_ontap\_s3\_services \- added <em class="title-reference">is\_http\_enabled</em>\, <em class="title-reference">is\_https\_enabled</em>\, <em class="title-reference">port</em> and <em class="title-reference">secure\_port</em> option for <em class="title-reference">s3</em> service\, requires ONTAP 9\.8 or later\.
* na\_ontap\_s3\_users \- new option <em class="title-reference">regenerate\_keys</em> and <em class="title-reference">delete\_keys</em> added in REST\, <em class="title-reference">delete\_keys</em> requires ONTAP 9\.14 or later\.
* na\_ontap\_svm \- added <em class="title-reference">allowed</em> option for <em class="title-reference">s3</em> service\, requires ONTAP 9\.7 or later\.
* na\_ontap\_volume \- new option <em class="title-reference">granular\_data</em> added in REST\, requires ONTAP 9\.12 or later\.
* na\_ontap\_volume \- new option <em class="title-reference">nas\_application\_template\.cifs\_share\_name</em> added in REST\, requires ONTAP 9\.11 or later\.
* na\_ontap\_volume \- new option <em class="title-reference">nas\_application\_template\.snaplock\.\*</em> added in REST\, requires ONTAP 9\.12 or later\.
* na\_ontap\_volume \- new option <em class="title-reference">nas\_application\_template\.snapshot\_locking\_enabled</em> added in REST\, requires ONTAP 9\.13\.1 or later\.

<a id="purestorage-flasharray-6"></a>
#### purestorage\.flasharray

* purefa\_dsrole \- Add support for non\-system\-defined directory service roles with new parameter <em class="title-reference">name</em>
* purefa\_info \- Add <code>enabled</code> value for network subnets
* purefa\_info \- Add <code>policies\` list of dicts to \`\`filesystem</code> subset for each share\.
* purefa\_info \- Add <code>time\_remaining</code> field for non\-deleted directory snapshots
* purefa\_info \- Expose directory service role management access policies if they exist
* purefa\_info \- Exposed password policy information
* purefa\_info \- SnaptoNFS support removed from Purity//FA 6\.6\.0 and higher\.
* purefa\_info \- Update KMIP information collection to use REST v2\, exposing full certifcate content
* purefa\_offload \- Add support for S3 Offload <code>uri</code> and <code>auth\_region</code> parameters
* purefa\_pgsnap \- Expose created protection group snapshot data in the module return dict
* purefa\_policy \- New policy type of <code>password</code> added\. Currently the only default management policy can be updated
* purefa\_subnet \- Remove default value for MTU t ostop restting to default on enable/disable of subnet\. Creation will still default to 1500 if not provided\.

<a id="vmware-vmware-6"></a>
#### vmware\.vmware

* cluster\_info \- Migrate cluster\_info module from the community\.vmware collection to here
* content\_library\_item\_info \- Migrate content\_library\_item\_info module from the vmware\.vmware\_rest collection to here

<a id="deprecated-features-6"></a>
### Deprecated Features

* The collection <code>ibm\.spectrum\_virtualize</code> was renamed to <code>ibm\.storage\_virtualize</code>\.
  For now both collections are included in Ansible\.
  The collection will be completely removed from Ansible 12\.
  Please update your FQCNs from <code>ibm\.spectrum\_virtualize</code> to <code>ibm\.storage\_virtualize</code>\.

<a id="community-general-24"></a>
#### community\.general

* opkg \- deprecate value <code>\"\"</code> for parameter <code>force</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9172](https\://github\.com/ansible\-collections/community\.general/pull/9172)\)\.
* redfish\_utils module utils \- deprecate method <code>RedfishUtils\.\_init\_session\(\)</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9190](https\://github\.com/ansible\-collections/community\.general/pull/9190)\)\.

<a id="vmware-vmware-rest-3"></a>
#### vmware\.vmware\_rest

* content\_library\_item\_info \- the module has been deprecated and will be removed in vmware\.vmware\_rest 5\.0\.0

<a id="security-fixes-1"></a>
### Security Fixes

<a id="ansible-core-15"></a>
#### Ansible\-core

* Templating will not prefer AnsibleUnsafe when a variable is referenced via hostvars \- CVE\-2024\-11079

<a id="bugfixes-6"></a>
### Bugfixes

<a id="ansible-core-16"></a>
#### Ansible\-core

* Fix returning \'unreachable\' for the overall task result\. This prevents false positives when a looped task has unignored unreachable items \([https\://github\.com/ansible/ansible/issues/84019](https\://github\.com/ansible/ansible/issues/84019)\)\.
* ansible\-test \- Fix traceback that occurs after an interactive command fails\.
* dnf5 \- fix installing a package using <code>state\=latest</code> when a binary of the same name as the package is already installed \([https\://github\.com/ansible/ansible/issues/84259](https\://github\.com/ansible/ansible/issues/84259)\)
* dnf5 \- matching on a binary can be achieved only by specifying a full path \([https\://github\.com/ansible/ansible/issues/84334](https\://github\.com/ansible/ansible/issues/84334)\)
* runas become \- Fix up become logic to still get the SYSTEM token with the most privileges when running as SYSTEM\.

<a id="cisco-ise-2"></a>
#### cisco\.ise

* network\_device \- Fix mask validation to handle None values in NetworkDeviceIPList

<a id="community-dns-8"></a>
#### community\.dns

* Update Public Suffix List\.

<a id="community-docker-9"></a>
#### community\.docker

* docker\_compose\_v2\_exec\, docker\_compose\_v2\_run \- fix missing <code>\-\-env</code> flag while assembling env arguments \([https\://github\.com/ansible\-collections/community\.docker/pull/992](https\://github\.com/ansible\-collections/community\.docker/pull/992)\)\.
* docker\_host\_info \- ensure that the module always returns <code>can\_talk\_to\_docker</code>\, and that it provides the correct value even if <code>api\_version</code> is specified \([https\://github\.com/ansible\-collections/community\.docker/issues/993](https\://github\.com/ansible\-collections/community\.docker/issues/993)\, [https\://github\.com/ansible\-collections/community\.docker/pull/995](https\://github\.com/ansible\-collections/community\.docker/pull/995)\)\.

<a id="community-general-25"></a>
#### community\.general

* dnf\_config\_manager \- fix hanging when prompting to import GPG keys \([https\://github\.com/ansible\-collections/community\.general/pull/9124](https\://github\.com/ansible\-collections/community\.general/pull/9124)\, [https\://github\.com/ansible\-collections/community\.general/issues/8830](https\://github\.com/ansible\-collections/community\.general/issues/8830)\)\.
* dnf\_config\_manager \- forces locale to <code>C</code> before module starts\. If the locale was set to non\-English\, the output of the <code>dnf config\-manager</code> could not be parsed \([https\://github\.com/ansible\-collections/community\.general/pull/9157](https\://github\.com/ansible\-collections/community\.general/pull/9157)\, [https\://github\.com/ansible\-collections/community\.general/issues/9046](https\://github\.com/ansible\-collections/community\.general/issues/9046)\)\.
* flatpak \- force the locale language to <code>C</code> when running the flatpak command \([https\://github\.com/ansible\-collections/community\.general/pull/9187](https\://github\.com/ansible\-collections/community\.general/pull/9187)\, [https\://github\.com/ansible\-collections/community\.general/issues/8883](https\://github\.com/ansible\-collections/community\.general/issues/8883)\)\.
* gio\_mime \- fix command line when determining version of <code>gio</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9171](https\://github\.com/ansible\-collections/community\.general/pull/9171)\, [https\://github\.com/ansible\-collections/community\.general/issues/9158](https\://github\.com/ansible\-collections/community\.general/issues/9158)\)\.
* github\_key \- in check mode\, a faulty call to <code>\`datetime\.strftime\(\.\.\.\)\`</code> was being made which generated an exception \([https\://github\.com/ansible\-collections/community\.general/issues/9185](https\://github\.com/ansible\-collections/community\.general/issues/9185)\)\.
* homebrew\_cask \- allow <code>\+</code> symbol in Homebrew cask name validation regex \([https\://github\.com/ansible\-collections/community\.general/pull/9128](https\://github\.com/ansible\-collections/community\.general/pull/9128)\)\.
* keycloak\_clientscope\_type \- sort the default and optional clientscope lists to improve the diff \([https\://github\.com/ansible\-collections/community\.general/pull/9202](https\://github\.com/ansible\-collections/community\.general/pull/9202)\)\.
* slack \- fail if Slack API response is not OK with error message \([https\://github\.com/ansible\-collections/community\.general/pull/9198](https\://github\.com/ansible\-collections/community\.general/pull/9198)\)\.

<a id="community-mysql-6"></a>
#### community\.mysql

* mysql\_user\,mysql\_role \- The sql\_mode ANSI\_QUOTES affects how the modules mysql\_user and mysql\_role compare the existing privileges with the configured privileges\, as well as decide whether double quotes or backticks should be used in the GRANT statements\. Pointing out in issue 671\, the modules mysql\_user and mysql\_role allow users to enable/disable ANSI\_QUOTES in session variable \(within a DB session\, the session variable always overwrites the global one\)\. But due to the issue\, the modules do not check for ANSI\_MODE in the session variable\, instead\, they only check in the GLOBAL one\.That behavior is not only limiting the users\' flexibility\, but also not allowing users to explicitly disable ANSI\_MODE to work around such bugs like [https\://bugs\.mysql\.com/bug\.php\?id\=115953](https\://bugs\.mysql\.com/bug\.php\?id\=115953)\. \([https\://github\.com/ansible\-collections/community\.mysql/issues/671](https\://github\.com/ansible\-collections/community\.mysql/issues/671)\)

<a id="community-postgresql-11"></a>
#### community\.postgresql

* postgresql\_pg\_hba \- fixes \#420 by properly handling hash\-symbols in quotes \([https\://github\.com/ansible\-collections/community\.postgresql/pull/766](https\://github\.com/ansible\-collections/community\.postgresql/pull/766)\)
* postgresql\_pg\_hba \- fixes \#705 by preventing invalid strings to be written \([https\://github\.com/ansible\-collections/community\.postgresql/pull/761](https\://github\.com/ansible\-collections/community\.postgresql/pull/761)\)
* postgresql\_pg\_hba \- fixes \#730 by extending the key we use to identify a rule with the connection type \([https\://github\.com/ansible\-collections/community\.postgresql/pull/770](https\://github\.com/ansible\-collections/community\.postgresql/pull/770)\)
* postgresql\_pg\_hba \- improves parsing of quoted strings and escaped newlines \([https\://github\.com/ansible\-collections/community\.postgresql/pull/761](https\://github\.com/ansible\-collections/community\.postgresql/pull/761)\)
* postgresql\_user \- doesn\'t take password\_encryption into account when checking if a password should be updated \([https\://github\.com/ansible\-collections/community\.postgresql/issues/688](https\://github\.com/ansible\-collections/community\.postgresql/issues/688)\)\.

<a id="community-routeros-7"></a>
#### community\.routeros

* api\_info\, api\_modify \- fields <code>log</code> and <code>log\-prefix</code> in paths <code>ip firewall filter</code>\, <code>ip firewall mangle</code>\, <code>ip firewall nat</code>\, <code>ip firewall raw</code> now have the correct default values \([https\://github\.com/ansible\-collections/community\.routeros/pull/324](https\://github\.com/ansible\-collections/community\.routeros/pull/324)\)\.

<a id="community-vmware-16"></a>
#### community\.vmware

* vm\_device\_helper \- Fix \'invalid configuration for device\' error caused by missing fileoperation parameter\. \([https\://github\.com/ansible\-collections/community\.vmware/pull/2009](https\://github\.com/ansible\-collections/community\.vmware/pull/2009)\)\.
* vmware\_guest \- Fix errors occuring during hardware version upgrade not being reported\. \([https\://github\.com/ansible\-collections/community\.vmware/pull/2010](https\://github\.com/ansible\-collections/community\.vmware/pull/2010)\)\.
* vmware\_guest \- Fix vmware\_guest always reporting change when using dvswitch\. \([https\://github\.com/ansible\-collections/community\.vmware/pull/2000](https\://github\.com/ansible\-collections/community\.vmware/pull/2000)\)\.
* vmware\_guest\_tools\_upgrade \- Account for all possible tools status \([https\://github\.com/ansible\-collections/community\.vmware/issues/2237](https\://github\.com/ansible\-collections/community\.vmware/issues/2237)\)\.

<a id="community-zabbix-4"></a>
#### community\.zabbix

* zabbix\_agent Role \- Add Zabbix 7\.0 LTS in supported versions for windows\.
* zabbix\_agent Role \- Added ability to set the monitored\_by and proxy\_group values\.
* zabbix\_agent Role \- Set become parameter explicitly to false for API tasks to run without sudo on the local computer\.

<a id="fortinet-fortimanager-5"></a>
#### fortinet\.fortimanager

* Changed all input argument name in ansible built\-in documentation to the underscore format\. E\.g\.\, changed \"var\-name\" to \"var\_name\"\.
* Fixed a bug where rc\_failed and rc\_succeeded did not work\.
* Improved code logic\, reduced redundant requests for system information\.
* Modified built\-in document to support sanity tests in ansible\-core 2\.18\.0\. No functionality changed\.

<a id="hetzner-hcloud-1"></a>
#### hetzner\.hcloud

* hcloud\_load\_balancer\_service \- Improve unknown certificate id or name error\.
* hcloud\_server \- Only rebuild existing servers\, skip rebuild if the server was just created\.

<a id="infoblox-nios-modules-1"></a>
#### infoblox\.nios\_modules

* For Host IPv6\, the mac parameter has been renamed to duid\.
* Refined Host record return fields to ensure use\_nextserver and nextserver are only included for IPv4\, as these fields are not applicable to IPv6\.

<a id="netapp-ontap-3"></a>
#### netapp\.ontap

* all modules supporting REST \- avoid duplicate calls to api/cluster to get ONTAP version\.
* na\_ontap\_broadcast\_domain \- fix issue with port modification in REST\.
* na\_ontap\_flexcache \- fix typo error in the query \'origins\.cluster\.name\' in REST\.
* na\_ontap\_rest\_info \- rectified subset name to <em class="title-reference">cluster/firmware/history</em>\.
* na\_ontap\_snapshot\_policy \- fix issue with \'retention\_period\' in REST\.

<a id="purestorage-flasharray-7"></a>
#### purestorage\.flasharray

* purefa\_alert \- Fix unreferenced variable error
* purefa\_audits \- Fix issue when <code>start</code> parameter not supplied
* purefa\_dirsnap \- Fixed issues with <code>keep\_for</code> setting and issues related to recovery of deleted snapshots
* purefa\_dsrole \- Fixed bug in role creation\.
* purefa\_eradication \- Fix incorrect timer settings
* purefa\_info \- Cater for zero used space in NFS offloads
* purefa\_info \- <code>exports</code> dict for each share changed to a list of dicts in <code>filesystm</code> subset
* purefa\_inventory \- Fixed quiet failures due to attribute errors
* purefa\_network \- Allow LACP bonds to be children of a VIF
* purefa\_network \- Fix compatability issue with <code>netaddr\>\=1\.2\.0</code>
* purefa\_ntp \- Fix issue with deletion of NTP servers
* purefa\_offload \- Corrected version check logic
* purefa\_pod \- Allow pd to be deleted with contents if <code>delete\_contents</code> specified
* purefa\_sessions \- Correctly report sessions with no start or end time
* purefa\_smtp \- Fixed SMTP deletion issue
* purefa\_snmp \- Fix issues with deleting SNMP entries
* purefa\_snmp\_agent \- Fix issues with deleting v3 agent
* purefa\_volume \- Added error message to warn about moving protected volume
* purefa\_volume \- Errors out when pgroup and add\_to\_pgs used incorrectly
* purefa\_volume \- Fixed issue of unable to move volume from pod to vgroup

<a id="telekom-mms-icinga-director-3"></a>
#### telekom\_mms\.icinga\_director

* Add Icinga notification template imports \([https\://github\.com/telekom\-mms/ansible\-collection\-icinga\-director/pull/267](https\://github\.com/telekom\-mms/ansible\-collection\-icinga\-director/pull/267)\)

<a id="vmware-vmware-7"></a>
#### vmware\.vmware

* content\_library\_item\_info \- Library name and ID are ignored if item ID is provided so updated docs and arg parse rules to reflect this

<a id="vmware-vmware-rest-4"></a>
#### vmware\.vmware\_rest

* lookup plugins \- Fixed issue where datacenter search filter was never properly set

<a id="known-issues-5"></a>
### Known Issues

<a id="dellemc-openmanage-12"></a>
#### dellemc\.openmanage

* idrac\_diagnostics \- Issue\(285322\) \- This module doesn\'t support export of diagnostics file to HTTP and HTTPS share via SOCKS proxy\.
* idrac\_firmware \- Issue\(279282\) \- This module does not support firmware update using HTTP\, HTTPS\, and FTP shares with authentication on iDRAC8\.
* ome\_smart\_fabric\_uplink \- Issue\(186024\) \- The module supported by OpenManage Enterprise Modular\, however it does not allow the creation of multiple uplinks of the same name\. If an uplink is created using the same name as an existing uplink\, then the existing uplink is modified\.

<a id="new-plugins-4"></a>
### New Plugins

<a id="filter-2"></a>
#### Filter

* community\.dns\.reverse\_pointer \- Convert an IP address into a DNS name for reverse lookup\.
* community\.general\.accumulate \- Produce a list of accumulated sums of the input list contents\.

<a id="lookup-2"></a>
#### Lookup

* community\.dns\.reverse\_lookup \- Reverse\-look up IP addresses\.

<a id="new-modules-6"></a>
### New Modules

<a id="community-general-26"></a>
#### community\.general

* community\.general\.decompress \- Decompresses compressed files\.
* community\.general\.proxmox\_backup \- Start a VM backup in Proxmox VE cluster\.

<a id="community-vmware-17"></a>
#### community\.vmware

* community\.vmware\.vmware\_drs\_override \- Configure DRS behavior for a specific VM in vSphere

<a id="fortinet-fortimanager-6"></a>
#### fortinet\.fortimanager

* fortinet\.fortimanager\.fmgr\_pkg\_videofilter\_youtubekey \- Configure YouTube API keys\.

<a id="netapp-ontap-4"></a>
#### netapp\.ontap

* netapp\.ontap\.na\_ontap\_bgp\_config \- NetApp ONTAP network BGP configuration
* netapp\.ontap\.na\_ontap\_cifs\_privileges \- NetApp ONTAP CIFS privileges

<a id="unchanged-collections-6"></a>
### Unchanged Collections

* amazon\.aws \(still version 9\.0\.0\)
* ansible\.netcommon \(still version 7\.1\.0\)
* ansible\.posix \(still version 1\.6\.2\)
* ansible\.utils \(still version 5\.1\.2\)
* ansible\.windows \(still version 2\.5\.0\)
* arista\.eos \(still version 10\.0\.1\)
* awx\.awx \(still version 24\.6\.1\)
* check\_point\.mgmt \(still version 6\.2\.1\)
* chocolatey\.chocolatey \(still version 1\.5\.3\)
* cisco\.aci \(still version 2\.10\.1\)
* cisco\.asa \(still version 6\.0\.0\)
* cisco\.intersight \(still version 2\.0\.20\)
* cisco\.ios \(still version 9\.0\.3\)
* cisco\.iosxr \(still version 10\.2\.2\)
* cisco\.meraki \(still version 2\.18\.3\)
* cisco\.mso \(still version 2\.9\.0\)
* cisco\.nxos \(still version 9\.2\.1\)
* cisco\.ucs \(still version 1\.14\.0\)
* cloud\.common \(still version 4\.0\.0\)
* cloudscale\_ch\.cloud \(still version 2\.4\.0\)
* community\.aws \(still version 9\.0\.0\)
* community\.ciscosmb \(still version 1\.0\.9\)
* community\.crypto \(still version 2\.22\.3\)
* community\.digitalocean \(still version 1\.27\.0\)
* community\.grafana \(still version 2\.1\.0\)
* community\.hashi\_vault \(still version 6\.2\.0\)
* community\.hrobot \(still version 2\.0\.2\)
* community\.library\_inventory\_filtering\_v1 \(still version 1\.0\.2\)
* community\.libvirt \(still version 1\.3\.0\)
* community\.mongodb \(still version 1\.7\.8\)
* community\.network \(still version 5\.1\.0\)
* community\.okd \(still version 4\.0\.0\)
* community\.proxysql \(still version 1\.6\.0\)
* community\.rabbitmq \(still version 1\.3\.0\)
* community\.sap\_libs \(still version 1\.4\.2\)
* community\.sops \(still version 2\.0\.0\)
* community\.windows \(still version 2\.3\.0\)
* containers\.podman \(still version 1\.16\.2\)
* cyberark\.conjur \(still version 1\.3\.1\)
* dellemc\.enterprise\_sonic \(still version 2\.5\.1\)
* dellemc\.powerflex \(still version 2\.5\.0\)
* dellemc\.unity \(still version 2\.0\.0\)
* f5networks\.f5\_modules \(still version 1\.32\.1\)
* fortinet\.fortios \(still version 2\.3\.8\)
* google\.cloud \(still version 1\.4\.1\)
* grafana\.grafana \(still version 5\.6\.0\)
* ibm\.qradar \(still version 4\.0\.0\)
* ibm\.spectrum\_virtualize \(still version 2\.0\.0\)
* ibm\.storage\_virtualize \(still version 2\.5\.0\)
* ieisystem\.inmanage \(still version 3\.0\.0\)
* infinidat\.infinibox \(still version 1\.4\.5\)
* inspur\.ispim \(still version 2\.2\.3\)
* junipernetworks\.junos \(still version 9\.1\.0\)
* kaytus\.ksmanage \(still version 2\.0\.0\)
* kubernetes\.core \(still version 5\.0\.0\)
* kubevirt\.core \(still version 2\.1\.0\)
* lowlydba\.sqlserver \(still version 2\.3\.4\)
* microsoft\.ad \(still version 1\.7\.1\)
* netapp\.cloudmanager \(still version 21\.24\.0\)
* netapp\.storagegrid \(still version 21\.13\.0\)
* netapp\_eseries\.santricity \(still version 1\.4\.1\)
* netbox\.netbox \(still version 3\.20\.0\)
* ngine\_io\.cloudstack \(still version 2\.5\.0\)
* ovirt\.ovirt \(still version 3\.2\.0\)
* purestorage\.flashblade \(still version 1\.19\.1\)
* sensu\.sensu\_go \(still version 1\.14\.0\)
* splunk\.es \(still version 4\.0\.0\)
* theforeman\.foreman \(still version 4\.2\.0\)
* vultr\.cloud \(still version 1\.13\.0\)
* vyos\.vyos \(still version 5\.0\.0\)
* wti\.remote \(still version 1\.0\.10\)

<a id="v11-0-0"></a>
## v11\.0\.0

- <a href="#release-summary-7">Release Summary</a>
- <a href="#removed-collections">Removed Collections</a>
- <a href="#added-collections-2">Added Collections</a>
- <a href="#ansible-core-17">Ansible\-core</a>
- <a href="#included-collections">Included Collections</a>
- <a href="#major-changes-6">Major Changes</a>
    - <a href="#amazon-aws-13">amazon\.aws</a>
    - <a href="#ansible-netcommon-3">ansible\.netcommon</a>
    - <a href="#ansible-posix">ansible\.posix</a>
    - <a href="#ansible-utils">ansible\.utils</a>
    - <a href="#arista-eos-2">arista\.eos</a>
    - <a href="#check-point-mgmt-3">check\_point\.mgmt</a>
    - <a href="#cisco-asa-2">cisco\.asa</a>
    - <a href="#cisco-ios-8">cisco\.ios</a>
    - <a href="#cisco-iosxr-3">cisco\.iosxr</a>
    - <a href="#cisco-nxos-5">cisco\.nxos</a>
    - <a href="#community-vmware-18">community\.vmware</a>
    - <a href="#community-zabbix-5">community\.zabbix</a>
    - <a href="#containers-podman-2">containers\.podman</a>
    - <a href="#dellemc-openmanage-13">dellemc\.openmanage</a>
    - <a href="#fortinet-fortios-4">fortinet\.fortios</a>
    - <a href="#grafana-grafana-1">grafana\.grafana</a>
    - <a href="#ibm-qradar">ibm\.qradar</a>
    - <a href="#junipernetworks-junos">junipernetworks\.junos</a>
    - <a href="#kaytus-ksmanage">kaytus\.ksmanage</a>
    - <a href="#splunk-es">splunk\.es</a>
    - <a href="#vyos-vyos">vyos\.vyos</a>
- <a href="#minor-changes-7">Minor Changes</a>
    - <a href="#ansible-core-18">Ansible\-core</a>
    - <a href="#amazon-aws-14">amazon\.aws</a>
    - <a href="#ansible-netcommon-4">ansible\.netcommon</a>
    - <a href="#ansible-posix-1">ansible\.posix</a>
    - <a href="#ansible-utils-1">ansible\.utils</a>
    - <a href="#ansible-windows-5">ansible\.windows</a>
    - <a href="#chocolatey-chocolatey">chocolatey\.chocolatey</a>
    - <a href="#cisco-aci-2">cisco\.aci</a>
    - <a href="#cisco-dnac-5">cisco\.dnac</a>
    - <a href="#cisco-ios-9">cisco\.ios</a>
    - <a href="#cisco-iosxr-4">cisco\.iosxr</a>
    - <a href="#cisco-meraki-7">cisco\.meraki</a>
    - <a href="#cisco-mso-2">cisco\.mso</a>
    - <a href="#cisco-nxos-6">cisco\.nxos</a>
    - <a href="#cloudscale-ch-cloud-4">cloudscale\_ch\.cloud</a>
    - <a href="#community-aws-4">community\.aws</a>
    - <a href="#community-crypto-9">community\.crypto</a>
    - <a href="#community-docker-10">community\.docker</a>
    - <a href="#community-general-27">community\.general</a>
    - <a href="#community-grafana-2">community\.grafana</a>
    - <a href="#community-mysql-7">community\.mysql</a>
    - <a href="#community-okd-1">community\.okd</a>
    - <a href="#community-postgresql-12">community\.postgresql</a>
    - <a href="#community-proxysql">community\.proxysql</a>
    - <a href="#community-routeros-8">community\.routeros</a>
    - <a href="#community-sops-4">community\.sops</a>
    - <a href="#community-vmware-19">community\.vmware</a>
    - <a href="#community-windows-1">community\.windows</a>
    - <a href="#community-zabbix-6">community\.zabbix</a>
    - <a href="#containers-podman-3">containers\.podman</a>
    - <a href="#dellemc-enterprise-sonic">dellemc\.enterprise\_sonic</a>
    - <a href="#dellemc-openmanage-14">dellemc\.openmanage</a>
    - <a href="#dellemc-powerflex-2">dellemc\.powerflex</a>
    - <a href="#f5networks-f5-modules-4">f5networks\.f5\_modules</a>
    - <a href="#fortinet-fortimanager-7">fortinet\.fortimanager</a>
    - <a href="#google-cloud-5">google\.cloud</a>
    - <a href="#hetzner-hcloud-2">hetzner\.hcloud</a>
    - <a href="#ibm-storage-virtualize-7">ibm\.storage\_virtualize</a>
    - <a href="#infoblox-nios-modules-2">infoblox\.nios\_modules</a>
    - <a href="#junipernetworks-junos-1">junipernetworks\.junos</a>
    - <a href="#kubernetes-core-6">kubernetes\.core</a>
    - <a href="#microsoft-ad-4">microsoft\.ad</a>
    - <a href="#netapp-cloudmanager">netapp\.cloudmanager</a>
    - <a href="#netapp-ontap-5">netapp\.ontap</a>
    - <a href="#netbox-netbox-3">netbox\.netbox</a>
    - <a href="#ngine-io-cloudstack">ngine\_io\.cloudstack</a>
    - <a href="#purestorage-flasharray-8">purestorage\.flasharray</a>
    - <a href="#purestorage-flashblade-4">purestorage\.flashblade</a>
    - <a href="#telekom-mms-icinga-director-4">telekom\_mms\.icinga\_director</a>
    - <a href="#theforeman-foreman">theforeman\.foreman</a>
    - <a href="#vmware-vmware-rest-5">vmware\.vmware\_rest</a>
    - <a href="#vultr-cloud">vultr\.cloud</a>
    - <a href="#vyos-vyos-1">vyos\.vyos</a>
- <a href="#breaking-changes--porting-guide-1">Breaking Changes / Porting Guide</a>
    - <a href="#ansible-core-19">Ansible\-core</a>
    - <a href="#amazon-aws-15">amazon\.aws</a>
    - <a href="#cloud-common-2">cloud\.common</a>
    - <a href="#community-aws-5">community\.aws</a>
    - <a href="#community-docker-11">community\.docker</a>
    - <a href="#community-general-28">community\.general</a>
    - <a href="#community-routeros-9">community\.routeros</a>
    - <a href="#community-vmware-20">community\.vmware</a>
    - <a href="#community-zabbix-7">community\.zabbix</a>
    - <a href="#hetzner-hcloud-3">hetzner\.hcloud</a>
    - <a href="#kubernetes-core-7">kubernetes\.core</a>
    - <a href="#vmware-vmware-rest-6">vmware\.vmware\_rest</a>
- <a href="#deprecated-features-7">Deprecated Features</a>
    - <a href="#ansible-core-20">Ansible\-core</a>
    - <a href="#amazon-aws-16">amazon\.aws</a>
    - <a href="#cisco-ios-10">cisco\.ios</a>
    - <a href="#community-aws-6">community\.aws</a>
    - <a href="#community-docker-12">community\.docker</a>
    - <a href="#community-general-29">community\.general</a>
    - <a href="#community-grafana-3">community\.grafana</a>
    - <a href="#community-mysql-8">community\.mysql</a>
    - <a href="#community-network">community\.network</a>
    - <a href="#community-routeros-10">community\.routeros</a>
    - <a href="#community-sops-5">community\.sops</a>
    - <a href="#community-vmware-21">community\.vmware</a>
- <a href="#removed-features-previously-deprecated">Removed Features \(previously deprecated\)</a>
    - <a href="#ansible-core-21">Ansible\-core</a>
    - <a href="#community-docker-13">community\.docker</a>
    - <a href="#community-general-30">community\.general</a>
    - <a href="#community-grafana-4">community\.grafana</a>
    - <a href="#community-okd-2">community\.okd</a>
    - <a href="#community-routeros-11">community\.routeros</a>
    - <a href="#community-sops-6">community\.sops</a>
    - <a href="#kubernetes-core-8">kubernetes\.core</a>
- <a href="#security-fixes-2">Security Fixes</a>
    - <a href="#ansible-core-22">Ansible\-core</a>
- <a href="#bugfixes-7">Bugfixes</a>
    - <a href="#ansible-core-23">Ansible\-core</a>
    - <a href="#amazon-aws-17">amazon\.aws</a>
    - <a href="#ansible-netcommon-5">ansible\.netcommon</a>
    - <a href="#ansible-posix-2">ansible\.posix</a>
    - <a href="#ansible-utils-2">ansible\.utils</a>
    - <a href="#ansible-windows-6">ansible\.windows</a>
    - <a href="#arista-eos-3">arista\.eos</a>
    - <a href="#check-point-mgmt-4">check\_point\.mgmt</a>
    - <a href="#chocolatey-chocolatey-1">chocolatey\.chocolatey</a>
    - <a href="#cisco-aci-3">cisco\.aci</a>
    - <a href="#cisco-ios-11">cisco\.ios</a>
    - <a href="#cisco-iosxr-5">cisco\.iosxr</a>
    - <a href="#cisco-ise-3">cisco\.ise</a>
    - <a href="#cisco-meraki-8">cisco\.meraki</a>
    - <a href="#cisco-mso-3">cisco\.mso</a>
    - <a href="#cisco-nxos-7">cisco\.nxos</a>
    - <a href="#cloud-common-3">cloud\.common</a>
    - <a href="#community-aws-7">community\.aws</a>
    - <a href="#community-crypto-10">community\.crypto</a>
    - <a href="#community-dns-9">community\.dns</a>
    - <a href="#community-docker-14">community\.docker</a>
    - <a href="#community-general-31">community\.general</a>
    - <a href="#community-grafana-5">community\.grafana</a>
    - <a href="#community-hrobot-7">community\.hrobot</a>
    - <a href="#community-mysql-9">community\.mysql</a>
    - <a href="#community-network-1">community\.network</a>
    - <a href="#community-postgresql-13">community\.postgresql</a>
    - <a href="#community-proxysql-1">community\.proxysql</a>
    - <a href="#community-routeros-12">community\.routeros</a>
    - <a href="#community-sops-7">community\.sops</a>
    - <a href="#community-vmware-22">community\.vmware</a>
    - <a href="#community-windows-2">community\.windows</a>
    - <a href="#community-zabbix-8">community\.zabbix</a>
    - <a href="#containers-podman-4">containers\.podman</a>
    - <a href="#dellemc-enterprise-sonic-1">dellemc\.enterprise\_sonic</a>
    - <a href="#dellemc-openmanage-15">dellemc\.openmanage</a>
    - <a href="#f5networks-f5-modules-5">f5networks\.f5\_modules</a>
    - <a href="#fortinet-fortimanager-8">fortinet\.fortimanager</a>
    - <a href="#fortinet-fortios-5">fortinet\.fortios</a>
    - <a href="#google-cloud-6">google\.cloud</a>
    - <a href="#hetzner-hcloud-4">hetzner\.hcloud</a>
    - <a href="#ibm-storage-virtualize-8">ibm\.storage\_virtualize</a>
    - <a href="#infoblox-nios-modules-3">infoblox\.nios\_modules</a>
    - <a href="#inspur-ispim">inspur\.ispim</a>
    - <a href="#junipernetworks-junos-2">junipernetworks\.junos</a>
    - <a href="#kaytus-ksmanage-1">kaytus\.ksmanage</a>
    - <a href="#kubernetes-core-9">kubernetes\.core</a>
    - <a href="#lowlydba-sqlserver-5">lowlydba\.sqlserver</a>
    - <a href="#microsoft-ad-5">microsoft\.ad</a>
    - <a href="#netapp-ontap-6">netapp\.ontap</a>
    - <a href="#netapp-eseries-santricity">netapp\_eseries\.santricity</a>
    - <a href="#netbox-netbox-4">netbox\.netbox</a>
    - <a href="#ngine-io-cloudstack-1">ngine\_io\.cloudstack</a>
    - <a href="#purestorage-flasharray-9">purestorage\.flasharray</a>
    - <a href="#purestorage-flashblade-5">purestorage\.flashblade</a>
    - <a href="#theforeman-foreman-1">theforeman\.foreman</a>
    - <a href="#vmware-vmware-rest-7">vmware\.vmware\_rest</a>
- <a href="#known-issues-6">Known Issues</a>
    - <a href="#ansible-core-24">Ansible\-core</a>
    - <a href="#ansible-netcommon-6">ansible\.netcommon</a>
    - <a href="#community-docker-15">community\.docker</a>
    - <a href="#community-general-32">community\.general</a>
    - <a href="#dellemc-openmanage-16">dellemc\.openmanage</a>
- <a href="#new-plugins-5">New Plugins</a>
    - <a href="#filter-3">Filter</a>
    - <a href="#test">Test</a>
- <a href="#new-modules-7">New Modules</a>
    - <a href="#ansible-core-25">Ansible\-core</a>
    - <a href="#amazon-aws-18">amazon\.aws</a>
    - <a href="#check-point-mgmt-5">check\_point\.mgmt</a>
    - <a href="#cisco-iosxr-6">cisco\.iosxr</a>
    - <a href="#community-docker-16">community\.docker</a>
    - <a href="#community-general-33">community\.general</a>
    - <a href="#community-grafana-6">community\.grafana</a>
    - <a href="#community-zabbix-9">community\.zabbix</a>
    - <a href="#containers-podman-5">containers\.podman</a>
    - <a href="#dellemc-enterprise-sonic-2">dellemc\.enterprise\_sonic</a>
    - <a href="#dellemc-openmanage-17">dellemc\.openmanage</a>
    - <a href="#fortinet-fortimanager-9">fortinet\.fortimanager</a>
    - <a href="#infoblox-nios-modules-4">infoblox\.nios\_modules</a>
    - <a href="#kaytus-ksmanage-2">kaytus\.ksmanage</a>
    - <a href="#microsoft-ad-6">microsoft\.ad</a>
    - <a href="#netbox-netbox-5">netbox\.netbox</a>
    - <a href="#purestorage-flasharray-10">purestorage\.flasharray</a>
    - <a href="#purestorage-flashblade-6">purestorage\.flashblade</a>
    - <a href="#theforeman-foreman-2">theforeman\.foreman</a>
- <a href="#unchanged-collections-7">Unchanged Collections</a>

<a id="release-summary-7"></a>
### Release Summary

Release Date\: 2024\-11\-19

[Porting Guide](https\://docs\.ansible\.com/ansible/devel/porting\_guides\.html)

<a id="removed-collections"></a>
### Removed Collections

* frr\.frr \(previously included version\: 2\.0\.2\)
* inspur\.sm \(previously included version\: 2\.3\.0\)
* ngine\_io\.exoscale \(previously included version\: 1\.1\.0\)
* openvswitch\.openvswitch \(previously included version\: 2\.1\.1\)
* t\_systems\_mms\.icinga\_director \(previously included version\: 2\.0\.1\)

You can still install a removed collection manually with <code>ansible\-galaxy collection install \<name\-of\-collection\></code>\.

<a id="added-collections-2"></a>
### Added Collections

* ieisystem\.inmanage \(version 3\.0\.0\)
* kubevirt\.core \(version 2\.1\.0\)
* vmware\.vmware \(version 1\.6\.0\)

<a id="ansible-core-17"></a>
### Ansible\-core

Ansible 11\.0\.0 contains ansible\-core version 2\.18\.0\.
This is a newer version than version 2\.17\.0 contained in the previous Ansible release\.

The changes are reported in the combined changelog below\.

<a id="included-collections"></a>
### Included Collections

If not mentioned explicitly\, the changes are reported in the combined changelog below\.

| Collection                               | Ansible 10.0.0 | Ansible 11.0.0 | Notes                                                                                                                                                                                                        |
| ---------------------------------------- | -------------- | -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| amazon.aws                               | 8.0.0          | 9.0.0          |                                                                                                                                                                                                              |
| ansible.netcommon                        | 6.1.2          | 7.1.0          |                                                                                                                                                                                                              |
| ansible.posix                            | 1.5.4          | 1.6.2          |                                                                                                                                                                                                              |
| ansible.utils                            | 4.1.0          | 5.1.2          |                                                                                                                                                                                                              |
| ansible.windows                          | 2.3.0          | 2.5.0          |                                                                                                                                                                                                              |
| arista.eos                               | 9.0.0          | 10.0.1         |                                                                                                                                                                                                              |
| awx.awx                                  | 24.3.1         | 24.6.1         | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.                                                                                 |
| azure.azcollection                       | 2.3.0          | 3.0.0          | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.                                                                                 |
| check_point.mgmt                         | 5.2.3          | 6.2.1          |                                                                                                                                                                                                              |
| chocolatey.chocolatey                    | 1.5.1          | 1.5.3          |                                                                                                                                                                                                              |
| cisco.aci                                | 2.9.0          | 2.10.1         |                                                                                                                                                                                                              |
| cisco.asa                                | 5.0.1          | 6.0.0          |                                                                                                                                                                                                              |
| cisco.dnac                               | 6.13.3         | 6.22.0         |                                                                                                                                                                                                              |
| cisco.intersight                         | 2.0.9          | 2.0.20         | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.                                                                                 |
| cisco.ios                                | 8.0.0          | 9.0.3          |                                                                                                                                                                                                              |
| cisco.iosxr                              | 9.0.0          | 10.2.2         |                                                                                                                                                                                                              |
| cisco.ise                                | 2.9.1          | 2.9.5          |                                                                                                                                                                                                              |
| cisco.meraki                             | 2.18.1         | 2.18.3         |                                                                                                                                                                                                              |
| cisco.mso                                | 2.6.0          | 2.9.0          |                                                                                                                                                                                                              |
| cisco.nxos                               | 8.0.0          | 9.2.1          |                                                                                                                                                                                                              |
| cisco.ucs                                | 1.10.0         | 1.14.0         | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.                                                                                 |
| cloud.common                             | 3.0.0          | 4.0.0          |                                                                                                                                                                                                              |
| cloudscale_ch.cloud                      | 2.3.1          | 2.4.0          |                                                                                                                                                                                                              |
| community.aws                            | 8.0.0          | 9.0.0          |                                                                                                                                                                                                              |
| community.crypto                         | 2.20.0         | 2.22.3         |                                                                                                                                                                                                              |
| community.digitalocean                   | 1.26.0         | 1.27.0         | There are no changes recorded in the changelog.                                                                                                                                                              |
| community.dns                            | 3.0.0          | 3.0.7          |                                                                                                                                                                                                              |
| community.docker                         | 3.10.3         | 4.0.1          |                                                                                                                                                                                                              |
| community.general                        | 9.0.1          | 10.0.1         |                                                                                                                                                                                                              |
| community.grafana                        | 1.9.1          | 2.1.0          |                                                                                                                                                                                                              |
| community.hrobot                         | 2.0.0          | 2.0.2          |                                                                                                                                                                                                              |
| community.library_inventory_filtering_v1 | 1.0.1          | 1.0.2          |                                                                                                                                                                                                              |
| community.mongodb                        | 1.7.4          | 1.7.8          | There are no changes recorded in the changelog.                                                                                                                                                              |
| community.mysql                          | 3.9.0          | 3.10.3         |                                                                                                                                                                                                              |
| community.network                        | 5.0.2          | 5.1.0          |                                                                                                                                                                                                              |
| community.okd                            | 3.0.1          | 4.0.0          |                                                                                                                                                                                                              |
| community.postgresql                     | 3.4.1          | 3.7.0          |                                                                                                                                                                                                              |
| community.proxysql                       | 1.5.1          | 1.6.0          |                                                                                                                                                                                                              |
| community.routeros                       | 2.15.0         | 3.0.0          |                                                                                                                                                                                                              |
| community.sops                           | 1.6.7          | 2.0.0          |                                                                                                                                                                                                              |
| community.vmware                         | 4.4.0          | 5.1.0          |                                                                                                                                                                                                              |
| community.windows                        | 2.2.0          | 2.3.0          |                                                                                                                                                                                                              |
| community.zabbix                         | 2.4.0          | 3.1.2          |                                                                                                                                                                                                              |
| containers.podman                        | 1.13.0         | 1.16.2         |                                                                                                                                                                                                              |
| cyberark.conjur                          | 1.2.2          | 1.3.1          | You can find the collection's changelog at [https://github.com/cyberark/ansible-conjur-collection/blob/master/CHANGELOG.md](https://github.com/cyberark/ansible-conjur-collection/blob/master/CHANGELOG.md). |
| cyberark.pas                             | 1.0.25         | 1.0.27         | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.                                                                                 |
| dellemc.enterprise_sonic                 | 2.4.0          | 2.5.1          |                                                                                                                                                                                                              |
| dellemc.openmanage                       | 9.2.0          | 9.8.0          |                                                                                                                                                                                                              |
| dellemc.powerflex                        | 2.4.0          | 2.5.0          |                                                                                                                                                                                                              |
| f5networks.f5_modules                    | 1.28.0         | 1.32.1         |                                                                                                                                                                                                              |
| fortinet.fortimanager                    | 2.5.0          | 2.7.0          |                                                                                                                                                                                                              |
| fortinet.fortios                         | 2.3.6          | 2.3.8          |                                                                                                                                                                                                              |
| google.cloud                             | 1.3.0          | 1.4.1          |                                                                                                                                                                                                              |
| grafana.grafana                          | 5.2.0          | 5.6.0          |                                                                                                                                                                                                              |
| hetzner.hcloud                           | 3.1.1          | 4.2.1          |                                                                                                                                                                                                              |
| ibm.qradar                               | 3.0.0          | 4.0.0          |                                                                                                                                                                                                              |
| ibm.storage_virtualize                   | 2.3.1          | 2.5.0          |                                                                                                                                                                                                              |
| ieisystem.inmanage                       |                | 3.0.0          | The collection was added to Ansible                                                                                                                                                                          |
| infoblox.nios_modules                    | 1.6.1          | 1.7.0          |                                                                                                                                                                                                              |
| inspur.ispim                             | 2.2.1          | 2.2.3          |                                                                                                                                                                                                              |
| junipernetworks.junos                    | 8.0.0          | 9.1.0          |                                                                                                                                                                                                              |
| kaytus.ksmanage                          | 1.2.1          | 2.0.0          |                                                                                                                                                                                                              |
| kubernetes.core                          | 3.1.0          | 5.0.0          |                                                                                                                                                                                                              |
| kubevirt.core                            |                | 2.1.0          | The collection was added to Ansible                                                                                                                                                                          |
| lowlydba.sqlserver                       | 2.3.2          | 2.3.4          |                                                                                                                                                                                                              |
| microsoft.ad                             | 1.5.0          | 1.7.1          |                                                                                                                                                                                                              |
| netapp.cloudmanager                      | 21.22.1        | 21.24.0        |                                                                                                                                                                                                              |
| netapp.ontap                             | 22.11.0        | 22.12.0        |                                                                                                                                                                                                              |
| netapp.storagegrid                       | 21.12.0        | 21.13.0        | There are no changes recorded in the changelog.                                                                                                                                                              |
| netapp_eseries.santricity                | 1.4.0          | 1.4.1          |                                                                                                                                                                                                              |
| netbox.netbox                            | 3.18.0         | 3.20.0         |                                                                                                                                                                                                              |
| ngine_io.cloudstack                      | 2.3.0          | 2.5.0          |                                                                                                                                                                                                              |
| purestorage.flasharray                   | 1.28.0         | 1.31.1         |                                                                                                                                                                                                              |
| purestorage.flashblade                   | 1.17.0         | 1.19.1         |                                                                                                                                                                                                              |
| splunk.es                                | 3.0.0          | 4.0.0          |                                                                                                                                                                                                              |
| telekom_mms.icinga_director              | 2.1.2          | 2.2.0          |                                                                                                                                                                                                              |
| theforeman.foreman                       | 4.0.0          | 4.2.0          |                                                                                                                                                                                                              |
| vmware.vmware                            |                | 1.6.0          | The collection was added to Ansible                                                                                                                                                                          |
| vmware.vmware_rest                       | 3.0.1          | 4.2.0          |                                                                                                                                                                                                              |
| vultr.cloud                              | 1.12.1         | 1.13.0         |                                                                                                                                                                                                              |
| vyos.vyos                                | 4.1.0          | 5.0.0          |                                                                                                                                                                                                              |
| wti.remote                               | 1.0.5          | 1.0.10         | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.                                                                                 |

<a id="major-changes-6"></a>
### Major Changes

<a id="amazon-aws-13"></a>
#### amazon\.aws

* autoscaling\_instance\_refresh \- The module has been migrated from the <code>community\.aws</code> collection\. Playbooks using the Fully Qualified Collection Name for this module should be updated to use <code>amazon\.aws\.autoscaling\_instance\_refresh</code> \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2338](https\://github\.com/ansible\-collections/amazon\.aws/pull/2338)\)\.
* autoscaling\_instance\_refresh\_info \- The module has been migrated from the <code>community\.aws</code> collection\. Playbooks using the Fully Qualified Collection Name for this module should be updated to use <code>amazon\.aws\.autoscaling\_instance\_refresh\_info</code> \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2338](https\://github\.com/ansible\-collections/amazon\.aws/pull/2338)\)\.
* ec2\_launch\_template \- The module has been migrated from the <code>community\.aws</code> collection\. Playbooks using the Fully Qualified Collection Name for this module should be updated to use <code>amazon\.aws\.ec2\_launch\_template</code> \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2348](https\://github\.com/ansible\-collections/amazon\.aws/pull/2348)\)\.
* ec2\_placement\_group \- The module has been migrated from the <code>community\.aws</code> collection\. Playbooks using the Fully Qualified Collection Name for this module should be updated to use <code>amazon\.aws\.ec2\_placement\_group</code>\.
* ec2\_placement\_group\_info \- The module has been migrated from the <code>community\.aws</code> collection\. Playbooks using the Fully Qualified Collection Name for this module should be updated to use <code>amazon\.aws\.ec2\_placement\_group\_info</code>\.
* ec2\_transit\_gateway \- The module has been migrated from the <code>community\.aws</code> collection\. Playbooks using the Fully Qualified Collection Name for this module should be updated to use <code>amazon\.aws\.ec2\_transit\_gateway</code>\.
* ec2\_transit\_gateway\_info \- The module has been migrated from the <code>community\.aws</code> collection\. Playbooks using the Fully Qualified Collection Name for this module should be updated to use <code>amazon\.aws\.ec2\_transit\_gateway\_info</code>\.
* ec2\_transit\_gateway\_vpc\_attachment \- The module has been migrated from the <code>community\.aws</code> collection\. Playbooks using the Fully Qualified Collection Name for this module should be updated to use <code>amazon\.aws\.ec2\_transit\_gateway\_vpc\_attachment</code>\.
* ec2\_transit\_gateway\_vpc\_attachment\_info \- The module has been migrated from the <code>community\.aws</code> collection\. Playbooks using the Fully Qualified Collection Name for this module should be updated to use <code>amazon\.aws\.ec2\_transit\_gateway\_vpc\_attachment\_info</code>\.
* ec2\_vpc\_egress\_igw \- The module has been migrated from the <code>community\.aws</code> collection\. Playbooks using the Fully Qualified Collection Name for this module should be updated to use <code>amazon\.aws\.ec2\_vpc\_egress\_igw</code> \([https\://api\.github\.com/repos/ansible\-collections/amazon\.aws/pulls/2327](https\://api\.github\.com/repos/ansible\-collections/amazon\.aws/pulls/2327)\)\.
* ec2\_vpc\_nacl \- The module has been migrated from the <code>community\.aws</code> collection\. Playbooks using the Fully Qualified Collection Name for this module should be updated to use <code>amazon\.aws\.ec2\_vpc\_nacl</code> \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2339](https\://github\.com/ansible\-collections/amazon\.aws/pull/2339)\)\.
* ec2\_vpc\_nacl\_info \- The module has been migrated from the <code>community\.aws</code> collection\. Playbooks using the Fully Qualified Collection Name for this module should be updated to use <code>amazon\.aws\.ec2\_vpc\_nacl\_info</code> \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2339](https\://github\.com/ansible\-collections/amazon\.aws/pull/2339)\)\.
* ec2\_vpc\_peer \- The module has been migrated from the <code>community\.aws</code> collection\. Playbooks using the Fully Qualified Collection Name for this module should be updated to use <code>amazon\.aws\.ec2\_vpc\_peer</code>\.
* ec2\_vpc\_peering\_info \- The module has been migrated from the <code>community\.aws</code> collection\. Playbooks using the Fully Qualified Collection Name for this module should be updated to use <code>amazon\.aws\.ec2\_vpc\_peering\_info</code>\.
* ec2\_vpc\_vgw \- The module has been migrated from the <code>community\.aws</code> collection\. Playbooks using the Fully Qualified Collection Name for this module should be updated to use <code>amazon\.aws\.ec2\_vpc\_vgw</code>\.
* ec2\_vpc\_vgw\_info \- The module has been migrated from the <code>community\.aws</code> collection\. Playbooks using the Fully Qualified Collection Name for this module should be updated to use <code>amazon\.aws\.ec2\_vpc\_vgw\_info</code>\.
* ec2\_vpc\_vpn \- The module has been migrated from the <code>community\.aws</code> collection\. Playbooks using the Fully Qualified Collection Name for this module should be updated to use <code>amazon\.aws\.ec2\_vpc\_vpn</code>\.
* ec2\_vpc\_vpn\_info \- The module has been migrated from the <code>community\.aws</code> collection\. Playbooks using the Fully Qualified Collection Name for this module should be updated to use <code>amazon\.aws\.ec2\_vpc\_vpn\_info</code>\.
* elb\_classic\_lb\_info \- The module has been migrated from the <code>community\.aws</code> collection\. Playbooks using the Fully Qualified Collection Name for this module should be updated to use <code>amazon\.aws\.elb\_classic\_lb\_info</code>\.

<a id="ansible-netcommon-3"></a>
#### ansible\.netcommon

* Bumping <em class="title-reference">requires\_ansible</em> to <em class="title-reference">\>\=2\.15\.0</em>\, since previous ansible\-core versions are EoL now\.

<a id="ansible-posix"></a>
#### ansible\.posix

* Dropping support for Ansible 2\.9\, ansible\-core 2\.15 will be minimum required version for this release

<a id="ansible-utils"></a>
#### ansible\.utils

* Bumping <em class="title-reference">requires\_ansible</em> to <em class="title-reference">\>\=2\.15\.0</em>\, since previous ansible\-core versions are EoL now\.

<a id="arista-eos-2"></a>
#### arista\.eos

* Bumping <em class="title-reference">requires\_ansible</em> to <em class="title-reference">\>\=2\.15\.0</em> due to the end\-of\-life status of previous <em class="title-reference">ansible\-core</em> versions\.

<a id="check-point-mgmt-3"></a>
#### check\_point\.mgmt

* New R82 Resource Modules
* Support relative positioning for sections

<a id="cisco-asa-2"></a>
#### cisco\.asa

* Bumping <em class="title-reference">requires\_ansible</em> to <em class="title-reference">\>\=2\.15\.0</em>\, since previous ansible\-core versions are EoL now\.

<a id="cisco-ios-8"></a>
#### cisco\.ios

* Bumping <em class="title-reference">requires\_ansible</em> to <em class="title-reference">\>\=2\.15\.0</em>\, since previous ansible\-core versions are EoL now\.

<a id="cisco-iosxr-3"></a>
#### cisco\.iosxr

* Bumping <em class="title-reference">requires\_ansible</em> to <em class="title-reference">\>\=2\.15\.0</em>\, since previous ansible\-core versions are EoL now\.

<a id="cisco-nxos-5"></a>
#### cisco\.nxos

* Bumping <em class="title-reference">requires\_ansible</em> to <em class="title-reference">\>\=2\.15\.0</em>\, since previous ansible\-core versions are EoL now\.

<a id="community-vmware-18"></a>
#### community\.vmware

* vmware\_guest\_tools\_upgrade \- Subsitute the deprecated <code>guest\.toolsStatus</code> \([https\://github\.com/ansible\-collections/community\.vmware/pull/2174](https\://github\.com/ansible\-collections/community\.vmware/pull/2174)\)\.
* vmware\_vm\_shell \- Subsitute the deprecated <code>guest\.toolsStatus</code> \([https\://github\.com/ansible\-collections/community\.vmware/pull/2174](https\://github\.com/ansible\-collections/community\.vmware/pull/2174)\)\.

<a id="community-zabbix-5"></a>
#### community\.zabbix

* All Roles \- Add support for openSUSE Leap 15 and SLES 15\.
* All Roles \- Separate installation of Zabbix repo from all other roles and link them together\.

<a id="containers-podman-2"></a>
#### containers\.podman

* Add mount and unmount for volumes
* Add multiple subnets for networks
* Add new options for podman\_container
* Add new options to pod module
* Add podman search
* Improve idempotency for networking in podman\_container
* Redesign idempotency for Podman Pod module

<a id="dellemc-openmanage-13"></a>
#### dellemc\.openmanage

* Added support to use session ID for authentication of iDRAC\, OpenManage Enterprise and OpenManage Enterprise Modular\.
* idrac\_secure\_boot \- This module allows to Configure attributes\, import\, or export secure boot certificate\, and reset keys\.
* idrac\_secure\_boot \- This module allows to import the secure boot certificate\.
* idrac\_server\_config\_profile \- This module is enhanced to allow you to export and import custom defaults on iDRAC\.
* idrac\_support\_assist \- This module allows to run and export SupportAssist collection logs on iDRAC\.
* idrac\_system\_erase \- This module allows to Erase system and storage components of the server on iDRAC\.
* ome\_configuration\_compliance\_baseline \- This module is enhanced to schedule the remediation job and stage the reboot\.
* ome\_session \- This module allows you to create and delete the sessions on OpenManage Enterprise and OpenManage Enterprise Modular\.
* omevv\_firmware\_repository\_profile \- This module allows to manage firmware repository profile\.
* omevv\_firmware\_repository\_profile\_info \- This module allows to retrieve firmware repository profile information\.
* omevv\_vcenter\_info \- This module allows to retrieve vCenter information\.

<a id="fortinet-fortios-4"></a>
#### fortinet\.fortios

* Add a sanity\_test\.yaml file to trigger CI tests in GitHub\.
* Improve the logic for SET function to send GET request first then PUT or POST
* Mantis
* Remove Tokens from URLs for Improved Security
* Support Ansible\-core 2\.17\.
* Support new FOS versions 7\.4\.4\.
* Support new FOS versions 7\.6\.0\.

<a id="grafana-grafana-1"></a>
#### grafana\.grafana

* Add a config check before restarting mimir by \@panfantastic in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/198](https\://github\.com/grafana/grafana\-ansible\-collection/pull/198)
* Add support for configuring feature\_toggles in grafana role by \@LexVar in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/173](https\://github\.com/grafana/grafana\-ansible\-collection/pull/173)
* Adding \"distributor\" section support to mimir config file by \@HamzaKhait in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/247](https\://github\.com/grafana/grafana\-ansible\-collection/pull/247)
* Allow alloy\_user\_groups variable again by \@pjezek in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/276](https\://github\.com/grafana/grafana\-ansible\-collection/pull/276)
* Alloy Role Improvements by \@voidquark in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/281](https\://github\.com/grafana/grafana\-ansible\-collection/pull/281)
* Backport post\-setup healthcheck from agent to alloy by \@v\-zhuravlev in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/213](https\://github\.com/grafana/grafana\-ansible\-collection/pull/213)
* Bump ansible\-lint from 24\.2\.3 to 24\.5\.0 by \@dependabot in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/207](https\://github\.com/grafana/grafana\-ansible\-collection/pull/207)
* Bump ansible\-lint from 24\.5\.0 to 24\.6\.0 by \@dependabot in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/216](https\://github\.com/grafana/grafana\-ansible\-collection/pull/216)
* Bump ansible\-lint from 24\.6\.0 to 24\.9\.2 by \@dependabot in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/270](https\://github\.com/grafana/grafana\-ansible\-collection/pull/270)
* Bump braces from 3\.0\.2 to 3\.0\.3 in the npm\_and\_yarn group across 1 directory by \@dependabot in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/218](https\://github\.com/grafana/grafana\-ansible\-collection/pull/218)
* Bump pylint from 3\.1\.0 to 3\.1\.1 by \@dependabot in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/200](https\://github\.com/grafana/grafana\-ansible\-collection/pull/200)
* Bump pylint from 3\.1\.1 to 3\.2\.2 by \@dependabot in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/208](https\://github\.com/grafana/grafana\-ansible\-collection/pull/208)
* Bump pylint from 3\.2\.2 to 3\.2\.3 by \@dependabot in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/217](https\://github\.com/grafana/grafana\-ansible\-collection/pull/217)
* Bump pylint from 3\.2\.3 to 3\.2\.5 by \@dependabot in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/234](https\://github\.com/grafana/grafana\-ansible\-collection/pull/234)
* Bump pylint from 3\.2\.5 to 3\.3\.1 by \@dependabot in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/273](https\://github\.com/grafana/grafana\-ansible\-collection/pull/273)
* Change from config\.river to config\.alloy by \@cardasac in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/225](https\://github\.com/grafana/grafana\-ansible\-collection/pull/225)
* Ensure check\-mode works for otel collector by \@pieterlexis\-tomtom in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/264](https\://github\.com/grafana/grafana\-ansible\-collection/pull/264)
* Fix Grafana Configuration for Unified and Legacy Alerting Based on Version by \@voidquark in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/215](https\://github\.com/grafana/grafana\-ansible\-collection/pull/215)
* Fix message argument of dashboard task by \@Nemental in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/256](https\://github\.com/grafana/grafana\-ansible\-collection/pull/256)
* Support adding alloy user to extra groups by \@v\-zhuravlev in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/212](https\://github\.com/grafana/grafana\-ansible\-collection/pull/212)
* Update Alloy variables to use the <em class="title-reference">grafana\_alloy\_</em> namespace so they are unique by \@Aethylred in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/209](https\://github\.com/grafana/grafana\-ansible\-collection/pull/209)
* Update README\.md by \@aioue in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/272](https\://github\.com/grafana/grafana\-ansible\-collection/pull/272)
* Update README\.md by \@aioue in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/275](https\://github\.com/grafana/grafana\-ansible\-collection/pull/275)
* Update main\.yml by \@aioue in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/274](https\://github\.com/grafana/grafana\-ansible\-collection/pull/274)
* Updated result\.json\[\'message\'\] to result\.json\(\)\[\'message\'\] by \@CPreun in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/223](https\://github\.com/grafana/grafana\-ansible\-collection/pull/223)
* add grafana\_plugins\_ops to defaults and docs by \@weakcamel in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/251](https\://github\.com/grafana/grafana\-ansible\-collection/pull/251)
* add option to populate google\_analytics\_4\_id value by \@copolycube in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/249](https\://github\.com/grafana/grafana\-ansible\-collection/pull/249)
* fix ansible\-lint warnings on Forbidden implicit octal value \"0640\" by \@copolycube in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/279](https\://github\.com/grafana/grafana\-ansible\-collection/pull/279)
* fix\:mimir molecule should use ansible core 2\.16 by \@GVengelen in https\://github\.com/grafana/grafana\-ansible\-collection/pull/254

<a id="ibm-qradar"></a>
#### ibm\.qradar

* Bumping <em class="title-reference">requires\_ansible</em> to <em class="title-reference">\>\=2\.15\.0</em>\, since previous ansible\-core versions are EoL now\.

<a id="junipernetworks-junos"></a>
#### junipernetworks\.junos

* Bumping <em class="title-reference">requires\_ansible</em> to <em class="title-reference">\>\=2\.15\.0</em>\, since previous ansible\-core versions are EoL now\.

<a id="kaytus-ksmanage"></a>
#### kaytus\.ksmanage

* Add new modules system\_lock\_mode\_info\, edit\_system\_lock\_mode\([https\://github\.com/ieisystem/kaytus\.ksmanage/pull/27](https\://github\.com/ieisystem/kaytus\.ksmanage/pull/27)\)\.

<a id="splunk-es"></a>
#### splunk\.es

* Bumping <em class="title-reference">requires\_ansible</em> to <em class="title-reference">\>\=2\.15\.0</em>\, since previous ansible\-core versions are EoL now\.

<a id="vyos-vyos"></a>
#### vyos\.vyos

* Bumping <em class="title-reference">requires\_ansible</em> to <em class="title-reference">\>\=2\.15\.0</em>\, since previous ansible\-core versions are EoL now\.

<a id="minor-changes-7"></a>
### Minor Changes

<a id="ansible-core-18"></a>
#### Ansible\-core

* Add <code>gid\_min</code>\, <code>gid\_max</code> to the group plugin to overwrite the defaults provided by the <code>/etc/login\.defs</code> file \([https\://github\.com/ansible/ansible/pull/81770](https\://github\.com/ansible/ansible/pull/81770)\)\.
* Add <code>python3\.13</code> to the default <code>INTERPRETER\_PYTHON\_FALLBACK</code> list\.
* Add <code>uid\_min</code>\, <code>uid\_max</code> to the user plugin to overwrite the defaults provided by the <code>/etc/login\.defs</code> file \([https\://github\.com/ansible/ansible/pull/81770](https\://github\.com/ansible/ansible/pull/81770)\)\.
* Add a new meta task <code>end\_role</code> \([https\://github\.com/ansible/ansible/issues/22286](https\://github\.com/ansible/ansible/issues/22286)\)
* Add a new mount\_facts module to support gathering information about mounts that are excluded by default fact gathering\.
* Introducing COLOR\_INCLUDED parameter\. This can set a specific color for \"included\" events\.
* Removed the shell <code>environment</code> config entry as this is already covered by the play/task directives documentation and the value itself is not used in the shell plugins\. This should remove any confusion around how people set the environment for a task\.
* Suppress cryptography deprecation warnings for Blowfish and TripleDES when the <code>paramiko</code> Python module is installed\.
* The minimum supported Python version on targets is now Python 3\.8\.
* <code>ansible\-galaxy collection publish</code> \- add configuration options for the initial poll interval and the exponential when checking the import status of a collection\, since the default is relatively slow\.
* ansible\-config has new \'validate\' option to find mispelled/forgein configurations in ini file or environment variables\.
* ansible\-doc \- show examples in role entrypoint argument specs \([https\://github\.com/ansible/ansible/pull/82671](https\://github\.com/ansible/ansible/pull/82671)\)\.
* ansible\-galaxy \- Handle authentication errors and token expiration
* ansible\-test \- Add Ubuntu 24\.04 remote\.
* ansible\-test \- Add support for Python 3\.13\.
* ansible\-test \- An <code>ansible\_core\.egg\-info</code> directory is no longer generated when running tests\.
* ansible\-test \- Connection options can be set for ansible\-test managed remote Windows instances\.
* ansible\-test \- Default to Python 3\.13 in the <code>base</code> and <code>default</code> containers\.
* ansible\-test \- Disable the <code>deprecated\-</code> prefixed <code>pylint</code> rules as their results vary by Python version\.
* ansible\-test \- Improve container runtime probe error handling\. When unexpected probe output is encountered\, an error with more useful debugging information is provided\.
* ansible\-test \- Improve the error message shown when an unknown <code>\-\-remote</code> or <code>\-\-docker</code> option is given\.
* ansible\-test \- Remove Python 2\.7 compatibility imports\.
* ansible\-test \- Removed the <code>vyos/1\.1\.8</code> network remote as it is no longer functional\.
* ansible\-test \- Replace Alpine 3\.19 container and remote with Alpine 3\.20\.
* ansible\-test \- Replace Fedora 39 container and remote with Fedora 40\.
* ansible\-test \- Replace FreeBSD 14\.0 remote with FreeBSD 14\.1\.
* ansible\-test \- Replace RHEL 9\.3 remote with RHEL 9\.4\.
* ansible\-test \- Replace Ubuntu 20\.04 container with Ubuntu 24\.04 container\.
* ansible\-test \- The <code>empty\-init</code> sanity test no longer applies to <code>module\_utils</code> packages\.
* ansible\-test \- Update <code>ansible\-test\-utility\-container</code> to version 3\.1\.0\.
* ansible\-test \- Update <code>base</code> and <code>default</code> containers to omit Python 3\.7\.
* ansible\-test \- Update <code>coverage</code> to version 7\.6\.1\.
* ansible\-test \- Update <code>http\-test\-container</code> to version 3\.0\.0\.
* ansible\-test \- Update <code>nios\-test\-container</code> to version 5\.0\.0\.
* ansible\-test \- Update <code>pylint</code> sanity test to use version 3\.3\.1\.
* ansible\-test \- Update <code>pypi\-test\-container</code> to version 3\.2\.0\.
* ansible\-test \- Update the <code>base</code> and <code>default</code> containers\.
* ansible\-test \- Updated the frozen requirements for all sanity tests\.
* ansible\-test \- Upgrade <code>pip</code> used in ansible\-test managed virtual environments from version 24\.0 to 24\.2\.
* ansible\-test \- Virtual environments created by ansible\-test no longer include the <code>wheel</code> or <code>setuptools</code> packages\.
* ansible\-test \- update HTTP test container to 3\.2\.0 \([https\://github\.com/ansible/ansible/pull/83469](https\://github\.com/ansible/ansible/pull/83469)\)\.
* ansible\.log now also shows log severity field
* distribution\.py \- Added SL\-Micro in Suse OS Family\. \([https\://github\.com/ansible/ansible/pull/83541](https\://github\.com/ansible/ansible/pull/83541)\)
* dnf \- minor internal changes in how the errors from the dnf API are handled\; rely solely on the exceptions rather than inspecting text embedded in them
* dnf \- remove legacy code for unsupported dnf versions
* dnf5 \- implement <code>enable\_plugin</code> and <code>disable\_plugin</code> options
* fact gathering \- Gather /proc/sysinfo facts on s390 Linux on Z
* facts \- add systemd version and features
* find \- change the datatype of <code>elements</code> to <code>path</code> in option <code>paths</code> \([https\://github\.com/ansible/ansible/pull/83575](https\://github\.com/ansible/ansible/pull/83575)\)\.
* ini lookup \- add new <code>interpolation</code> option \([https\://github\.com/ansible/ansible/issues/83755](https\://github\.com/ansible/ansible/issues/83755)\)
* isidentifier \- remove unwanted Python 2 specific code\.
* loop\_control \- add a break\_when option to to break out of a task loop early based on Jinja2 expressions \([https\://github\.com/ansible/ansible/issues/83442](https\://github\.com/ansible/ansible/issues/83442)\)\.
* package\_facts module now supports using aliases for supported package managers\, for example managers\=yum or managers\=dnf will resolve to using the underlying rpm\.
* plugins\, deprecations and warnings concerning configuration are now displayed to the user\, technical issue that prevented \'de\-duplication\' have been resolved\.
* psrp \- Remove connection plugin extras vars lookup\. This should have no affect on existing users as all options have been documented\.
* remove extraneous selinux import \([https\://github\.com/ansible/ansible/issues/83657](https\://github\.com/ansible/ansible/issues/83657)\)\.
* replace random with secrets library\.
* rpm\_key \- allow validation of gpg key with a subkey fingerprint
* rpm\_key \- enable gpg validation that requires presence of multiple fingerprints
* service\_mgr \- add support for dinit service manager \([https\://github\.com/ansible/ansible/pull/83489](https\://github\.com/ansible/ansible/pull/83489)\)\.
* task timeout now returns timedout key with frame/code that was in execution when the timeout is triggered\.
* timedout test for checking if a task result represents a \'timed out\' task\.
* unarchive \- Remove Python 2\.7 compatibility imports\.
* validate\-modules sanity test \- detect if names of an option \(option name \+ aliases\) do not match between argument spec and documentation \([https\://github\.com/ansible/ansible/issues/83598](https\://github\.com/ansible/ansible/issues/83598)\, [https\://github\.com/ansible/ansible/pull/83599](https\://github\.com/ansible/ansible/pull/83599)\)\.
* validate\-modules sanity test \- reject option/aliases names that are identical up to casing but belong to different options \([https\://github\.com/ansible/ansible/pull/83530](https\://github\.com/ansible/ansible/pull/83530)\)\.
* vaulted\_file test filter added\, to test if the provided path is an \'Ansible vaulted\' file
* yum\_repository \- add <code>excludepkgs</code> alias to the <code>exclude</code> option\.

<a id="amazon-aws-14"></a>
#### amazon\.aws

* Add support for transit gateway vpc attachment module \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2314](https\://github\.com/ansible\-collections/amazon\.aws/pull/2314)\)\.
* Bump version of ansible\-lint to minimum 24\.7\.0 \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2201](https\://github\.com/ansible\-collections/amazon\.aws/pull/2201)\)\.
* Move function <code>determine\_iam\_role</code> from module <code>ec2\_instance</code> to module\_utils/ec2 so that it can be used by <code>community\.aws\.ec2\_launch\_template</code> module \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2319](https\://github\.com/ansible\-collections/amazon\.aws/pull/2319)\)\.
* aws\_az\_info \- refactored code to use <code>AnsibleEC2Error</code> as well as moving shared code into module\_utils\.ec2 \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2163](https\://github\.com/ansible\-collections/amazon\.aws/pull/2163)\)\.  \- aws\_region\_info \- refactored code to use <code>AnsibleEC2Error</code> as well as moving shared code into module\_utils\.ec2 \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2163](https\://github\.com/ansible\-collections/amazon\.aws/pull/2163)\)\.
* backup\_vault \- Update code to remove unnecessary return values returned as None \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2105](https\://github\.com/ansible\-collections/amazon\.aws/pull/2105)\)\.
* cloudwatch\_metric\_alarm \- add  support for <code>evaluate\_low\_sample\_count\_percentile</code> parameter\.
* cloudwatch\_metric\_alarm \- support DatapointsToAlarm config \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2196](https\://github\.com/ansible\-collections/amazon\.aws/pull/2196)\)\.
* cloudwatchlogs\_log\_group\_metric\_filter \- Add support for <code>unit</code> and <code>dimensions</code> options \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2286](https\://github\.com/ansible\-collections/amazon\.aws/pull/2286)\)
* ec2\_ami \- Add support for uefi\-preferred boot mode \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2253](https\://github\.com/ansible\-collections/amazon\.aws/pull/2253)\)\.
* ec2\_ami \- refactored code to use <code>AnsibleEC2Error</code> as well as moving shared code into module\_utils\.ec2 \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2164](https\://github\.com/ansible\-collections/amazon\.aws/pull/2164)\)\.
* ec2\_ami\_info \- refactored code to use <code>AnsibleEC2Error</code> as well as moving shared code into module\_utils\.ec2 \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2164](https\://github\.com/ansible\-collections/amazon\.aws/pull/2164)\)\.
* ec2\_eip \- Add support to update reverse DNS record of an EIP \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2292](https\://github\.com/ansible\-collections/amazon\.aws/pull/2292)\)\.
* ec2\_eip \- refactored code to use <code>AnsibleEC2Error</code> as well as moving shared code into module\_utils\.ec2 \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2165](https\://github\.com/ansible\-collections/amazon\.aws/pull/2165)\)\.  \- ec2\_eip\_info \- refactored code to use <code>AnsibleEC2Error</code> as well as moving shared code into module\_utils\.ec2 \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2165](https\://github\.com/ansible\-collections/amazon\.aws/pull/2165)\)\.
* ec2\_eni \- refactored code to use <code>AnsibleEC2Error</code> as well as moving shared code into module\_utils\.ec2 \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2166](https\://github\.com/ansible\-collections/amazon\.aws/pull/2166)\)\.
* ec2\_eni\_info \- refactored code to use <code>AnsibleEC2Error</code> as well as moving shared code into module\_utils\.ec2 \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2166](https\://github\.com/ansible\-collections/amazon\.aws/pull/2166)\)\.
* ec2\_import\_image \- refactored code to use <code>AnsibleEC2Error</code> as well as moving shared code into module\_utils\.ec2 \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2167](https\://github\.com/ansible\-collections/amazon\.aws/pull/2167)\)\.
* ec2\_import\_image\_info \- refactored code to use <code>AnsibleEC2Error</code> as well as moving shared code into module\_utils\.ec2 \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2167](https\://github\.com/ansible\-collections/amazon\.aws/pull/2167)\)\.
* ec2\_instance \- Add support for <code>network\_interfaces</code> and <code>network\_interfaces\_ids</code> options replacing deprecated option <code>network</code> \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2123](https\://github\.com/ansible\-collections/amazon\.aws/pull/2123)\)\.
* ec2\_instance \- Pass variables <code>client</code> and <code>module</code> as function arguments instead of global variables \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2192](https\://github\.com/ansible\-collections/amazon\.aws/pull/2192)\)\.
* ec2\_instance \- <code>network\.source\_dest\_check</code> option has been deprecated and replaced by new option <code>source\_dest\_check</code> \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2123](https\://github\.com/ansible\-collections/amazon\.aws/pull/2123)\)\.
* ec2\_instance \- add the possibility to create instance with multiple network interfaces \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2123](https\://github\.com/ansible\-collections/amazon\.aws/pull/2123)\)\.
* ec2\_instance \- add the possibility to upgrade / downgrade existing ec2 instance type \([https\://github\.com/ansible\-collections/amazon\.aws/issues/469](https\://github\.com/ansible\-collections/amazon\.aws/issues/469)\)\.
* ec2\_instance \- refactored code to use <code>AnsibleEC2Error</code> and shared code from module\_utils\.ec2 \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2192](https\://github\.com/ansible\-collections/amazon\.aws/pull/2192)\)\.
* ec2\_instance\_info \- Replaced call to deprecated function <code>datetime\.utcnow\(\)</code> by <code>datetime\.now\(timezone\.utc\)</code> \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2192](https\://github\.com/ansible\-collections/amazon\.aws/pull/2192)\)\.
* ec2\_instance\_info \- refactored code to use <code>AnsibleEC2Error</code> and shared code from module\_utils\.ec2 \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2192](https\://github\.com/ansible\-collections/amazon\.aws/pull/2192)\)\.
* ec2\_key \- refactored code to use <code>AnsibleEC2Error</code> as well as moving shared code into module\_utils\.ec2 \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2168](https\://github\.com/ansible\-collections/amazon\.aws/pull/2168)\)\.
* ec2\_key\_info \- refactored code to use <code>AnsibleEC2Error</code> as well as moving shared code into module\_utils\.ec2 \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2168](https\://github\.com/ansible\-collections/amazon\.aws/pull/2168)\)\.
* ec2\_metadata\_facts \- Add parameter <code>metadata\_token\_ttl\_seconds</code> \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2209](https\://github\.com/ansible\-collections/amazon\.aws/pull/2209)\)\.
* ec2\_security\_group \- refactored code to use <code>AnsibleEC2Error</code> as well as moving shared code into module\_utils\.ec2 \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2169](https\://github\.com/ansible\-collections/amazon\.aws/pull/2169)\)\.
* ec2\_security\_group\_info \- refactored code to use <code>AnsibleEC2Error</code> as well as moving shared code into module\_utils\.ec2 \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2169](https\://github\.com/ansible\-collections/amazon\.aws/pull/2169)\)\.
* ec2\_snapshot \- refactored code to use <code>AnsibleEC2Error</code> as well as moving shared code into module\_utils\.ec2 \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2099](https\://github\.com/ansible\-collections/amazon\.aws/pull/2099)\)\.
* ec2\_snapshot\_info \- refactored code to use <code>AnsibleEC2Error</code> as well as moving shared code into module\_utils\.ec2 \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2099](https\://github\.com/ansible\-collections/amazon\.aws/pull/2099)\)\.
* ec2\_spot\_instance \- refactored code to use <code>AnsibleEC2Error</code> as well as moving shared code into module\_utils\.ec2 \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2099](https\://github\.com/ansible\-collections/amazon\.aws/pull/2099)\)\.
* ec2\_spot\_instance\_info \- refactored code to use <code>AnsibleEC2Error</code> as well as moving shared code into module\_utils\.ec2 \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2099](https\://github\.com/ansible\-collections/amazon\.aws/pull/2099)\)\.
* ec2\_vol \- refactored code to use <code>AnsibleEC2Error</code> as well as moving shared code into module\_utils\.ec2 \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2170](https\://github\.com/ansible\-collections/amazon\.aws/pull/2170)\)\.
* ec2\_vol\_info \- refactored code to use <code>AnsibleEC2Error</code> as well as moving shared code into module\_utils\.ec2 \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2170](https\://github\.com/ansible\-collections/amazon\.aws/pull/2170)\)\.
* ec2\_vpc\_dhcp\_option \- refactored code to use <code>AnsibleEC2Error</code> as well as moving shared code into module\_utils\.ec2 \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2097](https\://github\.com/ansible\-collections/amazon\.aws/pull/2097)\)\.
* ec2\_vpc\_dhcp\_option\_info \- refactored code to use <code>AnsibleEC2Error</code> as well as moving shared code into module\_utils\.ec2 \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2097](https\://github\.com/ansible\-collections/amazon\.aws/pull/2097)\)\.
* ec2\_vpc\_endpoint \- refactored code to use <code>AnsibleEC2Error</code> as well as moving shared code into module\_utils\.ec2 \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2097](https\://github\.com/ansible\-collections/amazon\.aws/pull/2097)\)\.
* ec2\_vpc\_endpoint\_info \- refactored code to use <code>AnsibleEC2Error</code> as well as moving shared code into module\_utils\.ec2 \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2097](https\://github\.com/ansible\-collections/amazon\.aws/pull/2097)\)\.
* ec2\_vpc\_endpoint\_service\_info \- refactored code to use <code>AnsibleEC2Error</code> as well as moving shared code into module\_utils\.ec2 \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2097](https\://github\.com/ansible\-collections/amazon\.aws/pull/2097)\)\.
* ec2\_vpc\_igw \- refactored code to use <code>AnsibleEC2Error</code> as well as moving shared code into module\_utils\.ec2 \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2099](https\://github\.com/ansible\-collections/amazon\.aws/pull/2099)\)\.
* ec2\_vpc\_igw\_info \- refactored code to use <code>AnsibleEC2Error</code> as well as moving shared code into module\_utils\.ec2 \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2099](https\://github\.com/ansible\-collections/amazon\.aws/pull/2099)\)\.
* ec2\_vpc\_nat\_gateway \- refactored code to use <code>AnsibleEC2Error</code> as well as moving shared code into module\_utils\.ec2 \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2099](https\://github\.com/ansible\-collections/amazon\.aws/pull/2099)\)\.
* ec2\_vpc\_nat\_gateway\_info \- refactored code to use <code>AnsibleEC2Error</code> as well as moving shared code into module\_utils\.ec2 \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2099](https\://github\.com/ansible\-collections/amazon\.aws/pull/2099)\)\.
* ec2\_vpc\_net \- refactored code to use <code>AnsibleEC2Error</code> as well as moving shared code into module\_utils\.ec2 \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2158](https\://github\.com/ansible\-collections/amazon\.aws/pull/2158)\)\.
* ec2\_vpc\_net\_info \- refactored code to use <code>AnsibleEC2Error</code> as well as moving shared code into module\_utils\.ec2 \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2158](https\://github\.com/ansible\-collections/amazon\.aws/pull/2158)\)\.
* ec2\_vpc\_route\_table \- refactored code to use <code>AnsibleEC2Error</code> as well as moving shared code into module\_utils\.ec2 \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2159](https\://github\.com/ansible\-collections/amazon\.aws/pull/2159)\)\.
* ec2\_vpc\_route\_table \- update the ec2\_vpc\_route\_table routes parameter to support the transit gateway id \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2291](https\://github\.com/ansible\-collections/amazon\.aws/pull/2291)\)\.
* ec2\_vpc\_route\_table\_info \- refactored code to use <code>AnsibleEC2Error</code> as well as moving shared code into module\_utils\.ec2 \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2159](https\://github\.com/ansible\-collections/amazon\.aws/pull/2159)\)\.
* ec2\_vpc\_subnet \- refactored code to use <code>AnsibleEC2Error</code> as well as moving shared code into module\_utils\.ec2 \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2160](https\://github\.com/ansible\-collections/amazon\.aws/pull/2160)\)\.
* ec2\_vpc\_subnet\_info \- refactored code to use <code>AnsibleEC2Error</code> as well as moving shared code into module\_utils\.ec2 \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2160](https\://github\.com/ansible\-collections/amazon\.aws/pull/2160)\)\.
* module\_utils\.botocore \- replace use of <code>botocore\.Session</code> with <code>boto3\.Session</code> for consistency \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2157](https\://github\.com/ansible\-collections/amazon\.aws/pull/2157)\)\.
* module\_utils\.botocore \- the <code>boto3\_conn</code> method now catches <code>BotoCoreError</code> rather than an incomplete list of subclasses \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2157](https\://github\.com/ansible\-collections/amazon\.aws/pull/2157)\)\.
* module\_utils/autoscaling \- create utils to handle AWS call for the <code>autoscaling</code> client \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2301](https\://github\.com/ansible\-collections/amazon\.aws/pull/2301)\)\.
* module\_utils/ec2 \- add some shared code for Launch template AWS API calls \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2319](https\://github\.com/ansible\-collections/amazon\.aws/pull/2319)\)\.
* module\_utils/ec2 \- add utils for the ec2\_placement\_group\* modules \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2322](https\://github\.com/ansible\-collections/amazon\.aws/pull/2322)\)\.
* module\_utils/ec2 \- add utils for the ec2\_transit\_gateway\_\* modules \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2325](https\://github\.com/ansible\-collections/amazon\.aws/pull/2325)\)\.
* module\_utils/ec2 \- add utils for the ec2\_vpc\_peer\* modules \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2303](https\://github\.com/ansible\-collections/amazon\.aws/pull/2303)\)\.
* module\_utils/ec2 \- add utils for the ec2\_vpc\_vgw\_\* modules \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2331](https\://github\.com/ansible\-collections/amazon\.aws/pull/2331)\)\.
* module\_utils/ec2 \- add utils for the ec2\_vpc\_vpn\* modules \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2312](https\://github\.com/ansible\-collections/amazon\.aws/pull/2312)\)\.
* module\_utils/ec2 \- move shared code for ec2 client \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2302](https\://github\.com/ansible\-collections/amazon\.aws/pull/2302)\)\.
* module\_utils/elbv2 \- Refactor listeners and rules comparison logic \([https\://github\.com/ansible\-collections/amazon\.aws/issues/1981](https\://github\.com/ansible\-collections/amazon\.aws/issues/1981)\)\.
* module\_utils/rds\.py \- Add shared functionality from rds snapshot modules \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2138](https\://github\.com/ansible\-collections/amazon\.aws/pull/2138)\)\.
* module\_utils/rds\.py \- Refactor shared boto3 client functionality\, add type hinting and function docstrings \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2119](https\://github\.com/ansible\-collections/amazon\.aws/pull/2119)\)\.
* plugin\_utils\.botocore \- the <code>boto3\_conn</code> method now catches <code>BotoCoreError</code> rather than an incomplete list of subclasses \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2157](https\://github\.com/ansible\-collections/amazon\.aws/pull/2157)\)\.
* rds\_cluster \- Add support for I/O\-Optimized storage configuration for aurora clusters \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2063](https\://github\.com/ansible\-collections/amazon\.aws/pull/2063)\)\.
* rds\_cluster\_snapshot \- Refactor shared boto3 client functionality\, add type hinting and function docstrings \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2138](https\://github\.com/ansible\-collections/amazon\.aws/pull/2138)\)\.
* rds\_instance \- Add support for  Multi\-Tenant CDB Databases\([https\://github\.com/ansible\-collections/amazon\.aws/pull/2275](https\://github\.com/ansible\-collections/amazon\.aws/pull/2275)\)\.
* rds\_instance \- Refactor shared boto3 client functionality\, add type hinting and function docstrings \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2119](https\://github\.com/ansible\-collections/amazon\.aws/pull/2119)\)\.
* rds\_instance \- Remove shared functioanlity added to module\_utils/rds\.py \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2138](https\://github\.com/ansible\-collections/amazon\.aws/pull/2138)\)\.
* rds\_instance \- snake case for parameter <code>performance\_insights\_kms\_key\_id</code> was incorrect according to boto documentation \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2163](https\://github\.com/ansible\-collections/amazon\.aws/pull/2163)\)\.
* rds\_instance\_info \- Refactor shared boto3 client functionality\, add type hinting and function docstrings \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2119](https\://github\.com/ansible\-collections/amazon\.aws/pull/2119)\)\.
* rds\_instance\_info \- Refactor shared boto3 client functionality\, add type hinting and function docstrings \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2138](https\://github\.com/ansible\-collections/amazon\.aws/pull/2138)\)\.
* rds\_instance\_snapshot \- Refactor shared boto3 client functionality\, add type hinting and function docstrings \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2138](https\://github\.com/ansible\-collections/amazon\.aws/pull/2138)\)\.
* rds\_snapshot\_info \- Refactor shared boto3 client functionality\, add type hinting and function docstrings \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2138](https\://github\.com/ansible\-collections/amazon\.aws/pull/2138)\)\.
* s3\_bucket \- Add <code>object\_lock\_default\_retention</code> to set Object Lock default retention configuration for S3 buckets \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2062](https\://github\.com/ansible\-collections/amazon\.aws/pull/2062)\)\.
* s3\_bucket \- Add support for bucket inventories \([https\://docs\.aws\.amazon\.com/AmazonS3/latest/userguide/storage\-inventory\.html](https\://docs\.aws\.amazon\.com/AmazonS3/latest/userguide/storage\-inventory\.html)\)
* s3\_bucket \- Add support for enabling Amazon S3 Transfer Acceleration by setting the <code>accelerate\_enabled</code> option \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2046](https\://github\.com/ansible\-collections/amazon\.aws/pull/2046)\)\.
* s3\_object \- Add support for <code>expected\_bucket\_owner</code> option \([https\://github\.com/ansible\-collections/amazon\.aws/issues/2114](https\://github\.com/ansible\-collections/amazon\.aws/issues/2114)\)\.
* s3\_object\_info \- Added support for <code>max\_keys</code> and <code>marker</code> parameter \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2328](https\://github\.com/ansible\-collections/amazon\.aws/pull/2328)\)\.
* ssm parameter lookup \- add new option <code>droppath</code> to drop the hierarchical search path from ssm parameter lookup results \([https\://github\.com/ansible\-collections/amazon\.aws/pull/1756](https\://github\.com/ansible\-collections/amazon\.aws/pull/1756)\)\.

<a id="ansible-netcommon-4"></a>
#### ansible\.netcommon

* ansible\.netcommon\.persistent \- Connection local is marked deprecated and all dependent collections are advised to move to a proper connection plugin\, complete support of connection local will be removed in a release after 01\-01\-2027\.

<a id="ansible-posix-1"></a>
#### ansible\.posix

* Add summary\_only parameter to profile\_roles and profile\_tasks callbacks\.
* firewalld \- add functionality to set forwarding \([https\://github\.com/ansible\-collections/ansible\.posix/pull/548](https\://github\.com/ansible\-collections/ansible\.posix/pull/548)\)\.
* firewalld \- added offline flag implementation \([https\://github\.com/ansible\-collections/ansible\.posix/pull/484](https\://github\.com/ansible\-collections/ansible\.posix/pull/484)\)
* firewalld \- respawn module to use the system python interpreter when the <code>firewall</code> python module is not available for <code>ansible\_python\_interpreter</code> \([https\://github\.com/ansible\-collections/ansible\.posix/pull/460](https\://github\.com/ansible\-collections/ansible\.posix/pull/460)\)\.
* firewalld\_info \- Only warn about ignored zones\, when there are zones ignored\.
* firewalld\_info \- respawn module to use the system python interpreter when the <code>firewall</code> python module is not available for <code>ansible\_python\_interpreter</code> \([https\://github\.com/ansible\-collections/ansible\.posix/pull/460](https\://github\.com/ansible\-collections/ansible\.posix/pull/460)\)\.
* mount \- add no\_log option for opts parameter \([https\://github\.com/ansible\-collections/ansible\.posix/pull/563](https\://github\.com/ansible\-collections/ansible\.posix/pull/563)\)\.
* seboolean \- respawn module to use the system python interpreter when the <code>selinux</code> python module is not available for <code>ansible\_python\_interpreter</code> \([https\://github\.com/ansible\-collections/ansible\.posix/pull/460](https\://github\.com/ansible\-collections/ansible\.posix/pull/460)\)\.
* selinux \- respawn module to use the system python interpreter when the <code>selinux</code> python module is not available for <code>ansible\_python\_interpreter</code> \([https\://github\.com/ansible\-collections/ansible\.posix/pull/460](https\://github\.com/ansible\-collections/ansible\.posix/pull/460)\)\.

<a id="ansible-utils-1"></a>
#### ansible\.utils

* Allows the cli\_parse module to find parser\.template\_path inside roles or collections when a path relative to the role/collection directory is provided\.
* Fix cli\_parse module to require a connection\.
* Previously\, the ansible\.utils\.ipcut filter only supported IPv6 addresses\, leading to confusing error messages when used with IPv4 addresses\. This fix ensures that the filter now appropriately handles both IPv4 and IPv6 addresses\.
* Removed conditional check for deprecated ansible\.netcommon\.cli\_parse from ansible\.utils\.cli\_parse
* The from\_xml filter returns a python dictionary instead of a json string\.

<a id="ansible-windows-5"></a>
#### ansible\.windows

* Set minimum supported Ansible version to 2\.15 to align with the versions still supported by Ansible\.
* owner \- Migrated to <code>Ansible\.Basic</code> format to add basic checks like invocation args checking
* win\_powershell \- Added the <code>sensitive\_parameters</code> option that can be used to pass in a SecureString or PSCredential parameter value\.
* win\_powershell \- Changed <em class="title-reference">sensitive\_parameters</em> to use <em class="title-reference">New\-Object</em>\, rather than <em class="title-reference">\:\:new\(\)</em>
* win\_setup \- Added the <code>ansible\_win\_rm\_certificate\_thumbprint</code> fact to display the thumbprint of the certificate in use
* win\_user \- Added the ability to set an account expiration date using the <code>account\_expires</code> option \- [https\://github\.com/ansible\-collections/ansible\.windows/issues/610](https\://github\.com/ansible\-collections/ansible\.windows/issues/610)

<a id="chocolatey-chocolatey"></a>
#### chocolatey\.chocolatey

* Remove support for End of Life ansible\-core 2\.13\, 2\.14

<a id="cisco-aci-2"></a>
#### cisco\.aci

* Add aci\_esg\_to\_contract module for esg contract relationship objects fvRsCons \(consumer\)\, fvRsConsIf \(consumer interface\)\, fvRsProv \(provider\) and fvRsIntraEpg \(intra\_esg\)
* Add aci\_system\_connectivity\_preference module \(\#601\)
* Added suppress\-previous flag option to reduce the number of API calls\. \(\#636\)
* Enable relative path and/or filename of private key for the aci httpapi plugin\.

<a id="cisco-dnac-5"></a>
#### cisco\.dnac

* Added \'accesspoint\_workflow\_manager\' module to manage access point configurations\.
* Added \'fabric\_sites\_zones\_workflow\_manager\.py\' to manage fabric sites/zones and update the authentication profile template\.
* Added \'fabric\_transits\_workflow\_manager\.py\' to perform operations on SDA fabric transits\.
* Added \'lan\_automation\_workflow\_manager\' to automate network discovery\, deployment\, and device configuration with LAN Automation\.
* Added \'rma\_workflow\_manager\' module to manage RMA workflow\.
* Added \'sda\_extranet\_policies\_workflow\_manager\' to manage SDA Extranet Policies\.
* Added \'sda\_extranet\_policies\_workflow\_manager\' to provide SDA Extranet Policies for managing SDA Extranet Policy\.
* Added \'sda\_fabric\_devices\_workflow\_manager\' to manage SDA fabric devices\.
* Added \'sda\_fabric\_virtual\_networks\_workflow\_manager\' to configure fabric VLANs\, Virtual Networks\, and Anycast Gateways\.
* Added \'sda\_host\_port\_onboarding\_workflow\_manager\' to manage host port onboarding in SD\-Access Fabric\.
* Added \'user\_role\_workflow\_manager\' module to manage operations to create\, update\, and delete users and roles\.
* Added API to validate the server address
* Added Circle CI support for integration testing\.
* Added detailed documentation in network\_settings\_workflow\_manager\.py
* Added example playbooks in device\_provision\_workflow\.yml
* Added example playbooks in network\_compliance\_workflow\_manager\.py
* Added new attribute \'ise\_integration\_wait\_time\' in ise\_radius\_integration\_workflow\_manager\.py
* Added the code for creating/updating/deleting events subscription notification with specified destination and added the playbook and documentation with examples
* Adding  support to update  password  in user\_role\_workflow\_manager module\.
* Adding pyzipper support in device\_configs workflow manager module\.
* Adding run\_compliance\_batch\_size support in network\_compliance module\.
* Ansible utils requirement updated\.
* Bug fixes in accesspoint\_workflow\_manager module
* Bug fixes in network\_settings\_workflow\_manager module
* Bug fixes in pnp\_workflow\_manager module
* Bug fixes in user\_role\_workflow\_manager module\.
* Changes in accesspoint\_workflow\_manager module\.
* Changes in device\_configs\_backup\_workflow\_manager module
* Changes in device\_configs\_backup\_workflow\_manager to support name of the site to which the device is assigned\.
* Changes in device\_credential\_workflow\_manager module\.
* Changes in dnac\.py
* Changes in dnac\.py to support common APIs
* Changes in events\_and\_notifications\_workflow\_manager module\.
* Changes in inventory and swim workflow manager modules\.
* Changes in inventory\_workflow\_manager module\.
* Changes in inventory\_workflow\_manager to support maximum devices to resync\, and resync timeout\.
* Changes in ise\_radius\_integration\_workflow\_manager module to check ise certification status\.
* Changes in ise\_radius\_integration\_workflow\_manager module\.
* Changes in network\_compliance\_workflow\_manager module\.
* Changes in network\_settings\_workflow\_manager module to support exception handling\.
* Changes in network\_settings\_workflow\_manager to support reserve ip subpools\.
* Changes in provision workflow manager module\.
* Changes in provision\_workflow\_manager to support enhanced log messages\.
* Changes in rma\_workflow\_manager module to support pre check for device replacement\.
* Changes in rma\_workflow\_manager module\.
* Changes in sda\_extranet\_policies\_workflow\_manager module\.
* Changes in sda\_fabric\_transits\_workflow\_manager module\.
* Changes in swim\_workflow\_manager module to support CCO image\.
* Changes in user\_role\_workflow\_manager module\.
* Checking SNMP versions in events\_and\_notifications\_workflow\_manager\.py module
* Checking the device list in swim workflow manager module\.
* Code change in template\_workflow\_manager module
* Code change in user\_role\_manager module
* Code changes in network\_compliance\_workflow\_manager module
* Code changes in rma\_workflow\_manager module
* Code changes in sda\_fabric\_devices\_workflow\_manager module
* Code changes in sda\_fabric\_sites\_zones\_workflow\_manager module
* Code changes in sda\_fabric\_virtual\_networks\_workflow\_manager module
* Code changes in sda\_host\_port\_onboarding\_workflow\_manager module
* Code changes in site\_workflow\_manager module
* Code changes in swim\_workflow\_manager module
* Code enhancements in device\_credential\_workflow\_manager module
* Enhancements in ise\_radius\_integration\_workflow\_manager module
* Enhancements in network\_settings\_workflow\_manager module\.
* Enhancements in swim\_workflow\_manager module\.
* Exporting export\_device\_details\_limit in inventory workflow module\.
* Fix family name from userand\_roles to user\_and\_roles\.
* Fix module name from network\_device\_config\_\_info to configuration\_archive\_details\_info\.
* Minor bug fixes in device\_credential\_workflow\_manager\.py module
* Minor bug fixes in network\_compliance\_workflow\_manager module\.
* Removed sda\_extranet\_policies\_workflow\_manager\.py module\.
* Removing git release workflows\.
* Setting dnac versions and compare for version based routing\.
* UT and IT cases for worflow manager modules\.
* Unit test automation for worflow\_manager modules\.
* access\_point\_workflow\_manager module\.py \- added attributes \'hostname\' and \'management\_ip\_address\'
* accesspoint\_workflow\_manager\.py \- added attribute \'factory\_reset\_aps\'\.
* accesspoint\_workflow\_manager\.py \- added attribute \'reboot\_aps\'\.
* accesspoint\_workflow\_manager\.py \- added attributes \'is\_assigned\_site\_as\_location\'\, and other new attributes\.
* application\_policy\_application\_set \- new module
* application\_policy\_application\_set\_count\_info \- new module
* application\_policy\_application\_set\_info \- new module
* applications\_count\_v2\_info \- new module
* applications\_v2 \- new module
* applications\_v2\_info \- new module
* auth\_token\_create \- new module
* authentication\_policy\_servers \- new module
* device\_configs\_backup\_workflow\_manager \- New workflow manager module for device configuration backup functions\.
* device\_configs\_backup\_workflow\_manager\.py \- added attributes \'hostname\_list\' and \'ip\_address\_list\'\, \'site\_list\'\, \'mac\_address\_list\'\, \'serial\_number\_list\'
* device\_configs\_backup\_workflow\_manager\.py \- removed attributes \'hostname\'\, \'ip\_address\'\, \'site\'\, \'mac\_address\' and \'serial\_number\'
* device\_configs\_backup\_workflow\_manager\.py\. added attribute \'site\'\.
* device\_credential\_workflow\_manager \- Updated the log messages\.
* device\_credential\_workflow\_manager\.py \- added attribute \'apply\_credentials\_to\_site\'\.
* device\_reboot\_apreboot \- new module
* discovery\_intent\.py \- Changed attribute name \'desc\' to \'description\'\.
* discovery\_workflow\_manager\.py \- Changed attribute name \'desc\' to \'description\'\.
* dna\_event\_snmp\_config\_info \- new module
* event\_snmp\_config \- new module
* event\_webhook\_read\_info \- new module
* events\_and\_notifications\_worflow\_manager\.py \- Changed attribute names from \'from\_email\'\, \'to\_email\'\, \'to send\_email\' and \'recipient\_email\'\.
* events\_and\_notifications\_workflow\_manager \- New workflow manager for configuring various types of destinations\(Webhook\, Email\, Syslog\, SNMP\, ITSM\) to deliver event notifications\.
* events\_and\_notifications\_workflow\_manager\.py \- Added attributes \'webhook\_event\_notification\'\, \'email\_event\_notification\'\, \'syslog\_event\_notification\'
* fabric\_sites\_zones\_workflow\_manager\.py \- added attribute \'fabric\_type\'\.
* fabric\_sites\_zones\_workflow\_manager\.py \- removed attribute \'site\_type\'\.
* flexible\_report\_content\_info \- new module
* flexible\_report\_execute \- new module
* flexible\_report\_executions\_info \- new module
* flexible\_report\_schedule  \- new module
* flexible\_report\_schedule\_info \- new module
* integration\_settings\_itsm\_instances\_info \- new module
* integration\_settings\_status\_info \- new module
* inventory\_intent\.py \- added attribute \'export\_device\_details\_limit\'\.
* inventory\_workflow\_manager \- Updated changes related to provisioning devices\.
* inventory\_workflow\_manager\.py \- Removed attribute hostname\_list\, serial\_number\_list and mac\_address\_list
* inventory\_workflow\_manager\.py \- added attribute \'export\_device\_details\_limit\'\.
* inventory\_workflow\_manager\.py \- added attribute hostnames\, serial\_numbers and mac\_addresses
* inventory\_workflow\_manager\.py \- added attributes resync\_device\_count and resync\_max\_timeout
* ise\_integration\_status\_info \- new module
* ise\_radius\_integration\_workflow\_manager \- New workflow manager for Authentication and Policy Servers\(ISE/AAA\)\.
* ise\_radius\_integration\_workflow\_manager \- Removed the attributes \'port\' and \'subscriber\_name\'\. Added the attribute \'ise\_integration\_wait\_time\'\.
* ise\_radius\_integration\_workflow\_manager\.py \- changed the type of \'authentication\_policy\_server\' from \'dict\' to \'list\'\.
* lan\_automation\_sessions\_info \- new module
* lan\_automation\_update \- new module
* lan\_automation\_update\_device \- new module
* lan\_automation\_update\_v2 \- new module
* lan\_automation\_v2 \- new module
* network\_compliance\_workflow\_manager \- New workflow manager for Network Compliance module for managing network compliance tasks on reachable device\(s\)\.
* network\_compliance\_workflow\_manager\.py \- added attribute \'run\_compliance\_batch\_size\'\.
* network\_device\_user\_defined\_field\_delete \- new module
* network\_settings\_workflow\_manager \- Added attributes \'ipv4\_global\_pool\_name\'\.
* network\_settings\_workflow\_manager\.py \- added attributes \'wired\_data\_collection\'\, \'wireless\_telemetry\'\, and \'netflow\_collector\'\.
* network\_settings\_workflow\_manager\.py \- changed the type of network\_management\_details from \'dic\' to \'list\'\.
* provision\_workflow\_manager \- Updated changes related to handle errors\.
* provision\_workflow\_manager\.py \- Added attribute \'provisioning\'
* provision\_workflow\_manager\.py \- added attribute \'force\_provisioning\'\.
* site\_workflow\_manager \- Updated changes in Site updation\.
* swim\_workflow\_manager\.py \- added attribute \'cco\_image\_details\'\.
* template\_workflow\_manager \- Removed attributes \'create\_time\'\, \'failure\_policy\'\, \'last\_update\_time\'\, \'latest\_version\_time\'\, \'parent\_template\_id\'\, \'project\_id\'\, \'validation\_errors\'\, \'rollback\_template\_params\' and \'rollback\_template\_content\'\.
* template\_workflow\_manager\.py \- Added attributes \'choices\'\, \'failure\_policy\'
* template\_workflow\_manager\.py \- added project\_file and payload\.
* user\_role\_workflow\_manager \- added attribute \'password\_update\'\.
* users\_external\_authentication \- new module
* users\_external\_servers\_aaa\_attribute \- new module

<a id="cisco-ios-9"></a>
#### cisco\.ios

* Add ios\_vrf\_global resource module in favor of ios\_vrf module \(fixes \- [https\://github\.com/ansible\-collections/cisco\.ios/pull/1055](https\://github\.com/ansible\-collections/cisco\.ios/pull/1055)\)

<a id="cisco-iosxr-4"></a>
#### cisco\.iosxr

* Added iosxr\_route\_maps resource module\, that helps with configuration of route\-policy\.
* Adds a new module <em class="title-reference">iosxr\_vrf\_address\_family</em> to manage VRFs address families on Cisco IOS\-XR devices \([https\://github\.com/ansible\-collections/cisco\.iosxr/pull/489](https\://github\.com/ansible\-collections/cisco\.iosxr/pull/489)\)\.
* Adds a new module <em class="title-reference">iosxr\_vrf\_global</em> to manage VRF global configurations on Cisco IOS\-XR devices \([https\://github\.com/ansible\-collections/cisco\.iosxr/pull/467](https\://github\.com/ansible\-collections/cisco\.iosxr/pull/467)\)\.

<a id="cisco-meraki-7"></a>
#### cisco\.meraki

* Include networks\_appliance\_traffic\_shaping\_custom\_performance\_classes\_info plugin\.

<a id="cisco-mso-2"></a>
#### cisco\.mso

* Add module mso\_schema\_template\_vrf\_rp to support multicast vrf rp in application templates
* Add module ndo\_dhcp\_option\_policy to support dhcp option policy configuration in tenant templates
* Add module ndo\_dhcp\_relay\_policy to support dhcp relay policy configuration in tenant templates
* Add module ndo\_l3\_domain and ndo\_physical\_domain to support domain configuration in fabric policy templates
* Add module ndo\_vlan\_pool to support vlan pool configuration in fabric policy templates
* Add new module ndo\_schema\_template\_bd\_dhcp\_policy to support BD DHCP Policy configuration in NDO version 4\.1 and later
* Add site\_aware\_policy\_enforcement and bd\_enforcement\_status arguments to the mso\_schema\_template\_vrf module
* Add support for multicast route map filters in mso\_schema\_template\_bd
* Add support to use an APIC DN as VRF reference in mso\_schema\_site\_bd\_l3out
* Added module ndo\_route\_map\_policy\_multicast to support multicast route map policies configuration in tenant templates
* Added module ndo\_template to support creation of tenant\, l3out\, fabric\_policy\, fabric\_resource\, monitoring\_tenant\, monitoring\_access and service\_device templates

<a id="cisco-nxos-6"></a>
#### cisco\.nxos

* Add nxos\_vrf\_global resource module in favor of nxos\_vrf module \([https\://github\.com/ansible\-collections/cisco\.nxos/pull/870](https\://github\.com/ansible\-collections/cisco\.nxos/pull/870)\)\.
* nxos\_bgp\_global \- Deprecate local\_as with local\_as\_config which supports more configuration attributes\, under neighbor\.
* route\_maps \- support simple route\-maps that do not contain set or match statements\. it allows for the creation and management of purely basic route\-map entries like \'route\-map test\-1 permit 10\'\.

<a id="cloudscale-ch-cloud-4"></a>
#### cloudscale\_ch\.cloud

* Update source\_format of custom images with actually available choices\.

<a id="community-aws-4"></a>
#### community\.aws

* autoscaling\_instance\_refresh \- Add support for <code>skip\_matching</code> and <code>max\_healthy\_percentage</code> in <code>preference</code> \([https\://github\.com/ansible\-collections/community\.aws/pull/2150](https\://github\.com/ansible\-collections/community\.aws/pull/2150)\)\.
* autoscaling\_instance\_refresh \- refactor module to use shared code from <code>ansible\_collections\.amazon\.aws\.plugins\.module\_utils\.autoscaling</code> and add type hinting \([https\://github\.com/ansible\-collections/community\.aws/pull/2150](https\://github\.com/ansible\-collections/community\.aws/pull/2150)\)\.
* autoscaling\_instance\_refresh\_info \- refactor module to use shared code from <code>ansible\_collections\.amazon\.aws\.plugins\.module\_utils\.autoscaling</code> and add type hinting \([https\://github\.com/ansible\-collections/community\.aws/pull/2150](https\://github\.com/ansible\-collections/community\.aws/pull/2150)\)\.
* ec2\_launch\_template \- Add option <code>tag\_specifications</code> to define tags to be applied to the resources created with the launch template \([https\://github\.com/ansible\-collections/community\.aws/issues/176](https\://github\.com/ansible\-collections/community\.aws/issues/176)\)\.
* ec2\_launch\_template \- Add suboption <code>throughput</code> to <code>block\_device\_mappings</code> argument \([https\://github\.com/ansible\-collections/community\.aws/issues/1944](https\://github\.com/ansible\-collections/community\.aws/issues/1944)\)\.
* ec2\_launch\_template \- Add support <code>purge\_tags</code> parameter \([https\://github\.com/ansible\-collections/community\.aws/issues/176](https\://github\.com/ansible\-collections/community\.aws/issues/176)\)\.
* ec2\_launch\_template \- Add the possibility to delete specific versions of a launch template using <code>versions\_to\_delete</code> \([https\://github\.com/ansible\-collections/community\.aws/pull/2164](https\://github\.com/ansible\-collections/community\.aws/pull/2164)\)\.
* ec2\_launch\_template \- Refactor module to use shared code from <code>amazon\.aws\.plugins\.module\_utils\.ec2</code> and update <code>RETURN</code> block \([https\://github\.com/ansible\-collections/community\.aws/pull/2164](https\://github\.com/ansible\-collections/community\.aws/pull/2164)\)\.
* ec2\_placement\_group \- Added support for creating with <code>tags</code> \([https\://github\.com/ansible\-collections/community\.aws/pull/2081](https\://github\.com/ansible\-collections/community\.aws/pull/2081)\)\.
* ec2\_placement\_group \- Refactor module to use shared code from <code>amazon\.aws\.plugins\.module\_utils\.ec2</code> and update <code>RETURN</code> block \([https\://github\.com/ansible\-collections/community\.aws/pull/2167](https\://github\.com/ansible\-collections/community\.aws/pull/2167)\)\.
* ec2\_transit\_gateway \- Refactor module to use shared code from <code>amazon\.aws\.plugins\.module\_utils\.ec2</code> and update <code>RETURN</code> block \([https\://github\.com/ansible\-collections/community\.aws/pull/2158](https\://github\.com/ansible\-collections/community\.aws/pull/2158)\)\.
* ec2\_transit\_gateway \- Support for enable multicast on Transit Gateway \([https\://github\.com/ansible\-collections/community\.aws/pull/2063](https\://github\.com/ansible\-collections/community\.aws/pull/2063)\)\.
* ec2\_transit\_gateway \- Support for enabling multicast on Transit Gateway \([https\://github\.com/ansible\-collections/community\.aws/pull/2063](https\://github\.com/ansible\-collections/community\.aws/pull/2063)\)\.
* ec2\_transit\_gateway\_info \- Refactor module to use shared code from <code>amazon\.aws\.plugins\.module\_utils\.ec2</code> and update <code>RETURN</code> block \([https\://github\.com/ansible\-collections/community\.aws/pull/2158](https\://github\.com/ansible\-collections/community\.aws/pull/2158)\)\.
* ec2\_transit\_gateway\_vpc\_attachment \- Modify doumentation and refactor to adhere to coding guidelines \([https\://github\.com/ansible\-collections/community\.aws/pull/2157](https\://github\.com/ansible\-collections/community\.aws/pull/2157)\)\.
* ec2\_vpc\_egress\_igw \- Add the possibility to update/add tags on Egress only internet gateway \([https\://github\.com/ansible\-collections/community\.aws/pull/2152](https\://github\.com/ansible\-collections/community\.aws/pull/2152)\)\.
* ec2\_vpc\_egress\_igw \- Refactor module to use shared code from <code>amazon\.aws\.plugins\.module\_utils\.ec2</code> util \([https\://github\.com/ansible\-collections/community\.aws/pull/2152](https\://github\.com/ansible\-collections/community\.aws/pull/2152)\)\.
* ec2\_vpc\_nacl \- Refactor module to use shared code from <em class="title-reference">amazon\.aws\.plugins\.module\_utils\.ec2</em> \([https\://github\.com/ansible\-collections/community\.aws/pull/2159](https\://github\.com/ansible\-collections/community\.aws/pull/2159)\)\.
* ec2\_vpc\_nacl\_info \- Refactor module to use shared code from <em class="title-reference">amazon\.aws\.plugins\.module\_utils\.ec2</em> \([https\://github\.com/ansible\-collections/community\.aws/pull/2159](https\://github\.com/ansible\-collections/community\.aws/pull/2159)\)\.
* ec2\_vpc\_peer \- Refactor module to use shared code from <code>amazon\.aws\.plugins\.module\_utils\.ec2</code> \([https\://github\.com/ansible\-collections/community\.aws/pull/2153](https\://github\.com/ansible\-collections/community\.aws/pull/2153)\)\.
* ec2\_vpc\_peering\_info \- Refactor module to use shared code from <code>amazon\.aws\.plugins\.module\_utils\.ec2</code> \([https\://github\.com/ansible\-collections/community\.aws/pull/2153](https\://github\.com/ansible\-collections/community\.aws/pull/2153)\)\.
* ec2\_vpc\_vgw \- Fix call to parent static method in class <code>VGWRetry</code> \([https\://github\.com/ansible\-collections/community\.aws/pull/2140](https\://github\.com/ansible\-collections/community\.aws/pull/2140)\)\.
* ec2\_vpc\_vgw \- Refactor module to use shared code from <code>amazon\.aws\.plugins\.module\_utils\.ec2</code> and update <code>RETURN</code> block \([https\://github\.com/ansible\-collections/community\.aws/pull/2171](https\://github\.com/ansible\-collections/community\.aws/pull/2171)\)\.
* ec2\_vpc\_vgw\_info \- Refactor module to use shared code from <code>amazon\.aws\.plugins\.module\_utils\.ec2</code> and update <code>RETURN</code> block \([https\://github\.com/ansible\-collections/community\.aws/pull/2171](https\://github\.com/ansible\-collections/community\.aws/pull/2171)\)\.
* ec2\_vpc\_vpn \- Refactor module to use shared code from <code>amazon\.aws\.plugins\.module\_utils\.ec2</code> \([https\://github\.com/ansible\-collections/community\.aws/pull/2160](https\://github\.com/ansible\-collections/community\.aws/pull/2160)\)\.
* ec2\_vpc\_vpn\_info \- Refactor module to use shared code from <code>amazon\.aws\.plugins\.module\_utils\.ec2</code> \([https\://github\.com/ansible\-collections/community\.aws/pull/2160](https\://github\.com/ansible\-collections/community\.aws/pull/2160)\)\.
* elb\_classic\_lb\_info \- Refactor elb\_classic\_lb\_info module \([https\://github\.com/ansible\-collections/community\.aws/pull/2139](https\://github\.com/ansible\-collections/community\.aws/pull/2139)\)\.

<a id="community-crypto-9"></a>
#### community\.crypto

* certificate\_complete\_chain \- add ability to identify Ed25519 and Ed448 complete chains \([https\://github\.com/ansible\-collections/community\.crypto/pull/777](https\://github\.com/ansible\-collections/community\.crypto/pull/777)\)\.
* get\_certificate \- adds <code>tls\_ctx\_options</code> option for specifying SSL CTX options \([https\://github\.com/ansible\-collections/community\.crypto/pull/779](https\://github\.com/ansible\-collections/community\.crypto/pull/779)\)\.
* get\_certificate \- allow to obtain the certificate chain sent by the server\, and the one used for validation\, with the new <code>get\_certificate\_chain</code> option\. Note that this option only works if the module is run with Python 3\.10 or newer \([https\://github\.com/ansible\-collections/community\.crypto/issues/568](https\://github\.com/ansible\-collections/community\.crypto/issues/568)\, [https\://github\.com/ansible\-collections/community\.crypto/pull/784](https\://github\.com/ansible\-collections/community\.crypto/pull/784)\)\.
* openssl\_privatekey\, openssl\_privatekey\_pipe \- add default value <code>auto</code> for <code>cipher</code> option\, which happens to be the only supported value for this option anyway\. Therefore it is no longer necessary to specify <code>cipher\=auto</code> when providing <code>passphrase</code> \([https\://github\.com/ansible\-collections/community\.crypto/issues/793](https\://github\.com/ansible\-collections/community\.crypto/issues/793)\, [https\://github\.com/ansible\-collections/community\.crypto/pull/794](https\://github\.com/ansible\-collections/community\.crypto/pull/794)\)\.

<a id="community-docker-10"></a>
#### community\.docker

* docker\, docker\_api connection plugins \- allow to determine the working directory when executing commands with the new <code>working\_dir</code> option \([https\://github\.com/ansible\-collections/community\.docker/pull/943](https\://github\.com/ansible\-collections/community\.docker/pull/943)\)\.
* docker\, docker\_api connection plugins \- allow to execute commands with extended privileges with the new <code>privileges</code> option \([https\://github\.com/ansible\-collections/community\.docker/pull/943](https\://github\.com/ansible\-collections/community\.docker/pull/943)\)\.
* docker\, docker\_api connection plugins \- allow to pass extra environment variables when executing commands with the new <code>extra\_env</code> option \([https\://github\.com/ansible\-collections/community\.docker/issues/937](https\://github\.com/ansible\-collections/community\.docker/issues/937)\, [https\://github\.com/ansible\-collections/community\.docker/pull/940](https\://github\.com/ansible\-collections/community\.docker/pull/940)\)\.
* docker\_compose\_v2 \- add <code>renew\_anon\_volumes</code> parameter for <code>docker compose up</code> \([https\://github\.com/ansible\-collections/community\.docker/pull/977](https\://github\.com/ansible\-collections/community\.docker/pull/977)\)\.
* docker\_compose\_v2\* modules \- support Docker Compose 2\.29\.0\'s <code>json</code> progress writer to avoid having to parse text output \([https\://github\.com/ansible\-collections/community\.docker/pull/931](https\://github\.com/ansible\-collections/community\.docker/pull/931)\)\.
* docker\_compose\_v2\_pull \- add new options <code>ignore\_buildable</code>\, <code>include\_deps</code>\, and <code>services</code> \([https\://github\.com/ansible\-collections/community\.docker/issues/941](https\://github\.com/ansible\-collections/community\.docker/issues/941)\, [https\://github\.com/ansible\-collections/community\.docker/pull/942](https\://github\.com/ansible\-collections/community\.docker/pull/942)\)\.
* docker\_container \- add support for <code>device\_cgroup\_rules</code> \([https\://github\.com/ansible\-collections/community\.docker/pull/910](https\://github\.com/ansible\-collections/community\.docker/pull/910)\)\.
* docker\_container \- the new <code>state\=healthy</code> allows to wait for a container to become healthy on startup\. The <code>healthy\_wait\_timeout</code> option allows to configure the maximum time to wait for this to happen \([https\://github\.com/ansible\-collections/community\.docker/issues/890](https\://github\.com/ansible\-collections/community\.docker/issues/890)\, [https\://github\.com/ansible\-collections/community\.docker/pull/921](https\://github\.com/ansible\-collections/community\.docker/pull/921)\)\.
* docker\_container \- when creating a container\, directly pass all networks to connect to to the Docker Daemon for API version 1\.44 and newer\. This makes creation more efficient and works around a bug in Docker Daemon that does not use the specified MAC address in at least some cases\, though only for creation \([https\://github\.com/ansible\-collections/community\.docker/pull/933](https\://github\.com/ansible\-collections/community\.docker/pull/933)\)\.

<a id="community-general-27"></a>
#### community\.general

* CmdRunner module util \- argument formats can be specified as plain functions without calling <code>cmd\_runner\_fmt\.as\_func\(\)</code> \([https\://github\.com/ansible\-collections/community\.general/pull/8479](https\://github\.com/ansible\-collections/community\.general/pull/8479)\)\.
* CmdRunner module utils \- the parameter <code>force\_lang</code> now supports the special value <code>auto</code> which will automatically try and determine the best parsable locale in the system \([https\://github\.com/ansible\-collections/community\.general/pull/8517](https\://github\.com/ansible\-collections/community\.general/pull/8517)\)\.
* MH module utils \- add parameter <code>when</code> to <code>cause\_changes</code> decorator \([https\://github\.com/ansible\-collections/community\.general/pull/8766](https\://github\.com/ansible\-collections/community\.general/pull/8766)\)\.
* MH module utils \- minor refactor in decorators \([https\://github\.com/ansible\-collections/community\.general/pull/8766](https\://github\.com/ansible\-collections/community\.general/pull/8766)\)\.
* alternatives \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8833](https\://github\.com/ansible\-collections/community\.general/pull/8833)\)\.
* ansible\_galaxy\_install \- add return value <code>version</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9060](https\://github\.com/ansible\-collections/community\.general/pull/9060)\)\.
* ansible\_galaxy\_install \- add upgrade feature \([https\://github\.com/ansible\-collections/community\.general/pull/8431](https\://github\.com/ansible\-collections/community\.general/pull/8431)\, [https\://github\.com/ansible\-collections/community\.general/issues/8351](https\://github\.com/ansible\-collections/community\.general/issues/8351)\)\.
* ansible\_galaxy\_install \- minor refactor in the module \([https\://github\.com/ansible\-collections/community\.general/pull/8413](https\://github\.com/ansible\-collections/community\.general/pull/8413)\)\.
* apache2\_mod\_proxy \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8814](https\://github\.com/ansible\-collections/community\.general/pull/8814)\)\.
* apache2\_mod\_proxy \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8833](https\://github\.com/ansible\-collections/community\.general/pull/8833)\)\.
* cargo \- add option <code>directory</code>\, which allows source directory to be specified \([https\://github\.com/ansible\-collections/community\.general/pull/8480](https\://github\.com/ansible\-collections/community\.general/pull/8480)\)\.
* cgroup\_memory\_recap\, hipchat\, jabber\, log\_plays\, loganalytics\, logentries\, logstash\, slack\, splunk\, sumologic\, syslog\_json callback plugins \- make sure that all options are typed \([https\://github\.com/ansible\-collections/community\.general/pull/8628](https\://github\.com/ansible\-collections/community\.general/pull/8628)\)\.
* chef\_databag\, consul\_kv\, cyberarkpassword\, dsv\, etcd\, filetree\, hiera\, onepassword\, onepassword\_doc\, onepassword\_raw\, passwordstore\, redis\, shelvefile\, tss lookup plugins \- make sure that all options are typed \([https\://github\.com/ansible\-collections/community\.general/pull/8626](https\://github\.com/ansible\-collections/community\.general/pull/8626)\)\.
* chroot\, funcd\, incus\, iocage\, jail\, lxc\, lxd\, qubes\, zone connection plugins \- make sure that all options are typed \([https\://github\.com/ansible\-collections/community\.general/pull/8627](https\://github\.com/ansible\-collections/community\.general/pull/8627)\)\.
* cmd\_runner module utils \- add decorator <code>cmd\_runner\_fmt\.stack</code> \([https\://github\.com/ansible\-collections/community\.general/pull/8415](https\://github\.com/ansible\-collections/community\.general/pull/8415)\)\.
* cmd\_runner module utils \- refactor argument formatting code to its own Python module \([https\://github\.com/ansible\-collections/community\.general/pull/8964](https\://github\.com/ansible\-collections/community\.general/pull/8964)\)\.
* cmd\_runner\_fmt module utils \- simplify implementation of <code>cmd\_runner\_fmt\.as\_bool\_not\(\)</code> \([https\://github\.com/ansible\-collections/community\.general/pull/8512](https\://github\.com/ansible\-collections/community\.general/pull/8512)\)\.
* cobbler\, linode\, lxd\, nmap\, online\, scaleway\, stackpath\_compute\, virtualbox inventory plugins \- make sure that all options are typed \([https\://github\.com/ansible\-collections/community\.general/pull/8625](https\://github\.com/ansible\-collections/community\.general/pull/8625)\)\.
* consul\_acl \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8833](https\://github\.com/ansible\-collections/community\.general/pull/8833)\)\.
* consul\_kv \- add argument for the datacenter option on Consul API \([https\://github\.com/ansible\-collections/community\.general/pull/9026](https\://github\.com/ansible\-collections/community\.general/pull/9026)\)\.
* copr \- Added <code>includepkgs</code> and <code>excludepkgs</code> parameters to limit the list of packages fetched or excluded from the repository\([https\://github\.com/ansible\-collections/community\.general/pull/8779](https\://github\.com/ansible\-collections/community\.general/pull/8779)\)\.
* cpanm \- add return value <code>cpanm\_version</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9061](https\://github\.com/ansible\-collections/community\.general/pull/9061)\)\.
* credstash lookup plugin \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8822](https\://github\.com/ansible\-collections/community\.general/pull/8822)\)\.
* csv module utils \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8814](https\://github\.com/ansible\-collections/community\.general/pull/8814)\)\.
* deco MH module utils \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8822](https\://github\.com/ansible\-collections/community\.general/pull/8822)\)\.
* dig lookup plugin \- add <code>port</code> option to specify DNS server port \([https\://github\.com/ansible\-collections/community\.general/pull/8966](https\://github\.com/ansible\-collections/community\.general/pull/8966)\)\.
* django module utils \- always retrieve version \([https\://github\.com/ansible\-collections/community\.general/pull/9063](https\://github\.com/ansible\-collections/community\.general/pull/9063)\)\.
* django\_check \- add return value <code>version</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9063](https\://github\.com/ansible\-collections/community\.general/pull/9063)\)\.
* django\_command \- add return value <code>version</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9063](https\://github\.com/ansible\-collections/community\.general/pull/9063)\)\.
* django\_createcachetable \- add return value <code>version</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9063](https\://github\.com/ansible\-collections/community\.general/pull/9063)\)\.
* doas\, dzdo\, ksu\, machinectl\, pbrun\, pfexec\, pmrun\, sesu\, sudosu become plugins \- make sure that all options are typed \([https\://github\.com/ansible\-collections/community\.general/pull/8623](https\://github\.com/ansible\-collections/community\.general/pull/8623)\)\.
* etcd3 \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8822](https\://github\.com/ansible\-collections/community\.general/pull/8822)\)\.
* flatpak \- improve the parsing of Flatpak application IDs based on official guidelines \([https\://github\.com/ansible\-collections/community\.general/pull/8909](https\://github\.com/ansible\-collections/community\.general/pull/8909)\)\.
* gconftool2 \- make use of <code>ModuleHelper</code> features to simplify code \([https\://github\.com/ansible\-collections/community\.general/pull/8711](https\://github\.com/ansible\-collections/community\.general/pull/8711)\)\.
* gcontool2 \- add return value <code>version</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9064](https\://github\.com/ansible\-collections/community\.general/pull/9064)\)\.
* gcontool2 module utils \- add argument formatter <code>version</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9064](https\://github\.com/ansible\-collections/community\.general/pull/9064)\)\.
* gcontool2\_info \- add return value <code>version</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9064](https\://github\.com/ansible\-collections/community\.general/pull/9064)\)\.
* gio\_mime \- add return value <code>version</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9067](https\://github\.com/ansible\-collections/community\.general/pull/9067)\)\.
* gio\_mime \- adjust code ahead of the old <code>VardDict</code> deprecation \([https\://github\.com/ansible\-collections/community\.general/pull/8855](https\://github\.com/ansible\-collections/community\.general/pull/8855)\)\.
* gio\_mime \- mute the  old <code>VarDict</code> deprecation \([https\://github\.com/ansible\-collections/community\.general/pull/8776](https\://github\.com/ansible\-collections/community\.general/pull/8776)\)\.
* gio\_mime module utils \- add argument formatter <code>version</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9067](https\://github\.com/ansible\-collections/community\.general/pull/9067)\)\.
* github\_app\_access\_token lookup plugin \- adds new <code>private\_key</code> parameter \([https\://github\.com/ansible\-collections/community\.general/pull/8989](https\://github\.com/ansible\-collections/community\.general/pull/8989)\)\.
* gitlab\_deploy\_key \- better construct when using <code>dict\.items\(\)</code> \([https\://github\.com/ansible\-collections/community\.general/pull/8876](https\://github\.com/ansible\-collections/community\.general/pull/8876)\)\.
* gitlab\_group \- add many new parameters \([https\://github\.com/ansible\-collections/community\.general/pull/8908](https\://github\.com/ansible\-collections/community\.general/pull/8908)\)\.
* gitlab\_group \- better construct when using <code>dict\.items\(\)</code> \([https\://github\.com/ansible\-collections/community\.general/pull/8876](https\://github\.com/ansible\-collections/community\.general/pull/8876)\)\.
* gitlab\_group \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8814](https\://github\.com/ansible\-collections/community\.general/pull/8814)\)\.
* gitlab\_issue \- better construct when using <code>dict\.items\(\)</code> \([https\://github\.com/ansible\-collections/community\.general/pull/8876](https\://github\.com/ansible\-collections/community\.general/pull/8876)\)\.
* gitlab\_merge\_request \- better construct when using <code>dict\.items\(\)</code> \([https\://github\.com/ansible\-collections/community\.general/pull/8876](https\://github\.com/ansible\-collections/community\.general/pull/8876)\)\.
* gitlab\_project \- add option <code>container\_expiration\_policy</code> to schedule container registry cleanup \([https\://github\.com/ansible\-collections/community\.general/pull/8674](https\://github\.com/ansible\-collections/community\.general/pull/8674)\)\.
* gitlab\_project \- add option <code>issues\_access\_level</code> to enable/disable project issues \([https\://github\.com/ansible\-collections/community\.general/pull/8760](https\://github\.com/ansible\-collections/community\.general/pull/8760)\)\.
* gitlab\_project \- add option <code>model\_registry\_access\_level</code> to disable model registry \([https\://github\.com/ansible\-collections/community\.general/pull/8688](https\://github\.com/ansible\-collections/community\.general/pull/8688)\)\.
* gitlab\_project \- add option <code>pages\_access\_level</code> to disable project pages \([https\://github\.com/ansible\-collections/community\.general/pull/8688](https\://github\.com/ansible\-collections/community\.general/pull/8688)\)\.
* gitlab\_project \- add option <code>repository\_access\_level</code> to disable project repository \([https\://github\.com/ansible\-collections/community\.general/pull/8674](https\://github\.com/ansible\-collections/community\.general/pull/8674)\)\.
* gitlab\_project \- add option <code>service\_desk\_enabled</code> to disable service desk \([https\://github\.com/ansible\-collections/community\.general/pull/8688](https\://github\.com/ansible\-collections/community\.general/pull/8688)\)\.
* gitlab\_project \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8822](https\://github\.com/ansible\-collections/community\.general/pull/8822)\)\.
* gitlab\_project \- sorted parameters in order to avoid future merge conflicts \([https\://github\.com/ansible\-collections/community\.general/pull/8759](https\://github\.com/ansible\-collections/community\.general/pull/8759)\)\.
* gitlab\_runner \- better construct when using <code>dict\.items\(\)</code> \([https\://github\.com/ansible\-collections/community\.general/pull/8876](https\://github\.com/ansible\-collections/community\.general/pull/8876)\)\.
* hashids filter plugin \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8814](https\://github\.com/ansible\-collections/community\.general/pull/8814)\)\.
* homebrew \- speed up brew install and upgrade \([https\://github\.com/ansible\-collections/community\.general/pull/9022](https\://github\.com/ansible\-collections/community\.general/pull/9022)\)\.
* hwc\_ecs\_instance \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8822](https\://github\.com/ansible\-collections/community\.general/pull/8822)\)\.
* hwc\_evs\_disk \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8822](https\://github\.com/ansible\-collections/community\.general/pull/8822)\)\.
* hwc\_vpc\_eip \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8822](https\://github\.com/ansible\-collections/community\.general/pull/8822)\)\.
* hwc\_vpc\_peering\_connect \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8822](https\://github\.com/ansible\-collections/community\.general/pull/8822)\)\.
* hwc\_vpc\_port \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8822](https\://github\.com/ansible\-collections/community\.general/pull/8822)\)\.
* hwc\_vpc\_subnet \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8822](https\://github\.com/ansible\-collections/community\.general/pull/8822)\)\.
* icinga2\_host \- replace loop with dict comprehension \([https\://github\.com/ansible\-collections/community\.general/pull/8876](https\://github\.com/ansible\-collections/community\.general/pull/8876)\)\.
* imc\_rest \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8833](https\://github\.com/ansible\-collections/community\.general/pull/8833)\)\.
* ipa\_dnsrecord \- adds <code>SSHFP</code> record type for managing SSH fingerprints in FreeIPA DNS \([https\://github\.com/ansible\-collections/community\.general/pull/8404](https\://github\.com/ansible\-collections/community\.general/pull/8404)\)\.
* ipa\_otptoken \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8822](https\://github\.com/ansible\-collections/community\.general/pull/8822)\)\.
* jenkins\_node \- add <code>offline\_message</code> parameter for updating a Jenkins node offline cause reason when the state is \"disabled\" \(offline\) \([https\://github\.com/ansible\-collections/community\.general/pull/9084](https\://github\.com/ansible\-collections/community\.general/pull/9084)\)\.\"
* jira \- adjust code ahead of the old <code>VardDict</code> deprecation \([https\://github\.com/ansible\-collections/community\.general/pull/8856](https\://github\.com/ansible\-collections/community\.general/pull/8856)\)\.
* jira \- mute the  old <code>VarDict</code> deprecation \([https\://github\.com/ansible\-collections/community\.general/pull/8776](https\://github\.com/ansible\-collections/community\.general/pull/8776)\)\.
* jira \- replace deprecated params when using decorator <code>cause\_changes</code> \([https\://github\.com/ansible\-collections/community\.general/pull/8791](https\://github\.com/ansible\-collections/community\.general/pull/8791)\)\.
* keep\_keys filter plugin \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8814](https\://github\.com/ansible\-collections/community\.general/pull/8814)\)\.
* keycloak module utils \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8822](https\://github\.com/ansible\-collections/community\.general/pull/8822)\)\.
* keycloak\_client \- add <code>client\-x509</code> choice to <code>client\_authenticator\_type</code> \([https\://github\.com/ansible\-collections/community\.general/pull/8973](https\://github\.com/ansible\-collections/community\.general/pull/8973)\)\.
* keycloak\_client \- assign auth flow by name \([https\://github\.com/ansible\-collections/community\.general/pull/8428](https\://github\.com/ansible\-collections/community\.general/pull/8428)\)\.
* keycloak\_client \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8814](https\://github\.com/ansible\-collections/community\.general/pull/8814)\)\.
* keycloak\_clientscope \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8814](https\://github\.com/ansible\-collections/community\.general/pull/8814)\)\.
* keycloak\_identity\_provider \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8814](https\://github\.com/ansible\-collections/community\.general/pull/8814)\)\.
* keycloak\_realm \- add boolean toggle to configure organization support for a given keycloak realm \([https\://github\.com/ansible\-collections/community\.general/issues/9027](https\://github\.com/ansible\-collections/community\.general/issues/9027)\, [https\://github\.com/ansible\-collections/community\.general/pull/8927/](https\://github\.com/ansible\-collections/community\.general/pull/8927/)\)\.
* keycloak\_user\_federation \- add module argument allowing users to optout of the removal of unspecified mappers\, for example to keep the keycloak default mappers \([https\://github\.com/ansible\-collections/community\.general/pull/8764](https\://github\.com/ansible\-collections/community\.general/pull/8764)\)\.
* keycloak\_user\_federation \- add the user federation config parameter <code>referral</code> to the module arguments \([https\://github\.com/ansible\-collections/community\.general/pull/8954](https\://github\.com/ansible\-collections/community\.general/pull/8954)\)\.
* keycloak\_user\_federation \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8814](https\://github\.com/ansible\-collections/community\.general/pull/8814)\)\.
* keycloak\_user\_federation \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8822](https\://github\.com/ansible\-collections/community\.general/pull/8822)\)\.
* keycloak\_user\_federation \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8833](https\://github\.com/ansible\-collections/community\.general/pull/8833)\)\.
* linode \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8814](https\://github\.com/ansible\-collections/community\.general/pull/8814)\)\.
* locale\_gen \- add support for multiple locales \([https\://github\.com/ansible\-collections/community\.general/issues/8677](https\://github\.com/ansible\-collections/community\.general/issues/8677)\, [https\://github\.com/ansible\-collections/community\.general/pull/8682](https\://github\.com/ansible\-collections/community\.general/pull/8682)\)\.
* lxc\_container \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8822](https\://github\.com/ansible\-collections/community\.general/pull/8822)\)\.
* lxd\_container \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8814](https\://github\.com/ansible\-collections/community\.general/pull/8814)\)\.
* manageiq\_provider \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8814](https\://github\.com/ansible\-collections/community\.general/pull/8814)\)\.
* mattermost \- adds support for message priority \([https\://github\.com/ansible\-collections/community\.general/issues/9068](https\://github\.com/ansible\-collections/community\.general/issues/9068)\, [https\://github\.com/ansible\-collections/community\.general/pull/9087](https\://github\.com/ansible\-collections/community\.general/pull/9087)\)\.
* memcached\, pickle\, redis\, yaml cache plugins \- make sure that all options are typed \([https\://github\.com/ansible\-collections/community\.general/pull/8624](https\://github\.com/ansible\-collections/community\.general/pull/8624)\)\.
* memset\_dns\_reload \- replace loop with <code>dict\(\)</code> \([https\://github\.com/ansible\-collections/community\.general/pull/8876](https\://github\.com/ansible\-collections/community\.general/pull/8876)\)\.
* memset\_memstore\_info \- replace loop with <code>dict\(\)</code> \([https\://github\.com/ansible\-collections/community\.general/pull/8876](https\://github\.com/ansible\-collections/community\.general/pull/8876)\)\.
* memset\_server\_info \- replace loop with <code>dict\(\)</code> \([https\://github\.com/ansible\-collections/community\.general/pull/8876](https\://github\.com/ansible\-collections/community\.general/pull/8876)\)\.
* memset\_zone \- replace loop with <code>dict\(\)</code> \([https\://github\.com/ansible\-collections/community\.general/pull/8876](https\://github\.com/ansible\-collections/community\.general/pull/8876)\)\.
* memset\_zone\_domain \- replace loop with <code>dict\(\)</code> \([https\://github\.com/ansible\-collections/community\.general/pull/8876](https\://github\.com/ansible\-collections/community\.general/pull/8876)\)\.
* memset\_zone\_record \- replace loop with <code>dict\(\)</code> \([https\://github\.com/ansible\-collections/community\.general/pull/8876](https\://github\.com/ansible\-collections/community\.general/pull/8876)\)\.
* nmcli \- add <code>conn\_enable</code> param to reload connection \([https\://github\.com/ansible\-collections/community\.general/issues/3752](https\://github\.com/ansible\-collections/community\.general/issues/3752)\, [https\://github\.com/ansible\-collections/community\.general/issues/8704](https\://github\.com/ansible\-collections/community\.general/issues/8704)\, [https\://github\.com/ansible\-collections/community\.general/pull/8897](https\://github\.com/ansible\-collections/community\.general/pull/8897)\)\.
* nmcli \- add <code>state\=up</code> and <code>state\=down</code> to enable/disable connections \([https\://github\.com/ansible\-collections/community\.general/issues/3752](https\://github\.com/ansible\-collections/community\.general/issues/3752)\, [https\://github\.com/ansible\-collections/community\.general/issues/8704](https\://github\.com/ansible\-collections/community\.general/issues/8704)\, [https\://github\.com/ansible\-collections/community\.general/issues/7152](https\://github\.com/ansible\-collections/community\.general/issues/7152)\, [https\://github\.com/ansible\-collections/community\.general/pull/8897](https\://github\.com/ansible\-collections/community\.general/pull/8897)\)\.
* nmcli \- better construct when using <code>dict\.items\(\)</code> \([https\://github\.com/ansible\-collections/community\.general/pull/8876](https\://github\.com/ansible\-collections/community\.general/pull/8876)\)\.
* npm \- add <code>force</code> parameter to allow <code>\-\-force</code> \([https\://github\.com/ansible\-collections/community\.general/pull/8885](https\://github\.com/ansible\-collections/community\.general/pull/8885)\)\.
* ocapi\_utils \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8833](https\://github\.com/ansible\-collections/community\.general/pull/8833)\)\.
* one\_image \- add <code>create</code>\, <code>template</code> and <code>datastore\_id</code> arguments for image creation \([https\://github\.com/ansible\-collections/community\.general/pull/9075](https\://github\.com/ansible\-collections/community\.general/pull/9075)\)\.
* one\_image \- add <code>wait\_timeout</code> argument for adjustable timeouts \([https\://github\.com/ansible\-collections/community\.general/pull/9075](https\://github\.com/ansible\-collections/community\.general/pull/9075)\)\.
* one\_image \- add option <code>persistent</code> to manage image persistence \([https\://github\.com/ansible\-collections/community\.general/issues/3578](https\://github\.com/ansible\-collections/community\.general/issues/3578)\, [https\://github\.com/ansible\-collections/community\.general/pull/8889](https\://github\.com/ansible\-collections/community\.general/pull/8889)\)\.
* one\_image \- extend xsd scheme to make it return a lot more info about image \([https\://github\.com/ansible\-collections/community\.general/pull/8889](https\://github\.com/ansible\-collections/community\.general/pull/8889)\)\.
* one\_image \- refactor code to make it more similar to <code>one\_template</code> and <code>one\_vnet</code> \([https\://github\.com/ansible\-collections/community\.general/pull/8889](https\://github\.com/ansible\-collections/community\.general/pull/8889)\)\.
* one\_image\_info \- extend xsd scheme to make it return a lot more info about image \([https\://github\.com/ansible\-collections/community\.general/pull/8889](https\://github\.com/ansible\-collections/community\.general/pull/8889)\)\.
* one\_image\_info \- refactor code to make it more similar to <code>one\_template</code> and <code>one\_vnet</code> \([https\://github\.com/ansible\-collections/community\.general/pull/8889](https\://github\.com/ansible\-collections/community\.general/pull/8889)\)\.
* one\_service \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8814](https\://github\.com/ansible\-collections/community\.general/pull/8814)\)\.
* one\_vm \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8814](https\://github\.com/ansible\-collections/community\.general/pull/8814)\)\.
* onepassword lookup plugin \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8833](https\://github\.com/ansible\-collections/community\.general/pull/8833)\)\.
* open\_iscsi \- allow login to a portal with multiple targets without specifying any of them \([https\://github\.com/ansible\-collections/community\.general/pull/8719](https\://github\.com/ansible\-collections/community\.general/pull/8719)\)\.
* openbsd\_pkg \- adds diff support to show changes in installed package list\. This does not yet work for check mode \([https\://github\.com/ansible\-collections/community\.general/pull/8402](https\://github\.com/ansible\-collections/community\.general/pull/8402)\)\.
* opennebula\.py \- add VM <code>id</code> and VM <code>host</code> to inventory host data \([https\://github\.com/ansible\-collections/community\.general/pull/8532](https\://github\.com/ansible\-collections/community\.general/pull/8532)\)\.
* opentelemetry callback plugin \- fix default value for <code>store\_spans\_in\_file</code> causing traces to be produced to a file named <code>None</code> \([https\://github\.com/ansible\-collections/community\.general/issues/8566](https\://github\.com/ansible\-collections/community\.general/issues/8566)\, [https\://github\.com/ansible\-collections/community\.general/pull/8741](https\://github\.com/ansible\-collections/community\.general/pull/8741)\)\.
* opkg \- add return value <code>version</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9086](https\://github\.com/ansible\-collections/community\.general/pull/9086)\)\.
* passwordstore lookup plugin \- add subkey creation/update support \([https\://github\.com/ansible\-collections/community\.general/pull/8952](https\://github\.com/ansible\-collections/community\.general/pull/8952)\)\.
* passwordstore lookup plugin \- add the current user to the lockfile file name to address issues on multi\-user systems \([https\://github\.com/ansible\-collections/community\.general/pull/8689](https\://github\.com/ansible\-collections/community\.general/pull/8689)\)\.
* pids \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8833](https\://github\.com/ansible\-collections/community\.general/pull/8833)\)\.
* pipx \- add parameter <code>suffix</code> to module \([https\://github\.com/ansible\-collections/community\.general/pull/8675](https\://github\.com/ansible\-collections/community\.general/pull/8675)\, [https\://github\.com/ansible\-collections/community\.general/issues/8656](https\://github\.com/ansible\-collections/community\.general/issues/8656)\)\.
* pipx \- added new states <code>install\_all</code>\, <code>uninject</code>\, <code>upgrade\_shared</code>\, <code>pin</code>\, and <code>unpin</code> \([https\://github\.com/ansible\-collections/community\.general/pull/8809](https\://github\.com/ansible\-collections/community\.general/pull/8809)\)\.
* pipx \- added parameter <code>global</code> to module \([https\://github\.com/ansible\-collections/community\.general/pull/8793](https\://github\.com/ansible\-collections/community\.general/pull/8793)\)\.
* pipx \- refactor out parsing of <code>pipx list</code> output to module utils \([https\://github\.com/ansible\-collections/community\.general/pull/9044](https\://github\.com/ansible\-collections/community\.general/pull/9044)\)\.
* pipx \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8833](https\://github\.com/ansible\-collections/community\.general/pull/8833)\)\.
* pipx\_info \- add new return value <code>pinned</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9044](https\://github\.com/ansible\-collections/community\.general/pull/9044)\)\.
* pipx\_info \- added parameter <code>global</code> to module \([https\://github\.com/ansible\-collections/community\.general/pull/8793](https\://github\.com/ansible\-collections/community\.general/pull/8793)\)\.
* pipx\_info \- refactor out parsing of <code>pipx list</code> output to module utils \([https\://github\.com/ansible\-collections/community\.general/pull/9044](https\://github\.com/ansible\-collections/community\.general/pull/9044)\)\.
* pipx\_info \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8833](https\://github\.com/ansible\-collections/community\.general/pull/8833)\)\.
* pkg5\_publisher \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8833](https\://github\.com/ansible\-collections/community\.general/pull/8833)\)\.
* pkgng \- add option <code>use\_globs</code> \(default <code>true</code>\) to optionally disable glob patterns \([https\://github\.com/ansible\-collections/community\.general/issues/8632](https\://github\.com/ansible\-collections/community\.general/issues/8632)\, [https\://github\.com/ansible\-collections/community\.general/pull/8633](https\://github\.com/ansible\-collections/community\.general/pull/8633)\)\.
* proxmox \- add <code>disk\_volume</code> and <code>mount\_volumes</code> keys for better readability \([https\://github\.com/ansible\-collections/community\.general/pull/8542](https\://github\.com/ansible\-collections/community\.general/pull/8542)\)\.
* proxmox \- allow specification of the API port when using proxmox\_\* \([https\://github\.com/ansible\-collections/community\.general/issues/8440](https\://github\.com/ansible\-collections/community\.general/issues/8440)\, [https\://github\.com/ansible\-collections/community\.general/pull/8441](https\://github\.com/ansible\-collections/community\.general/pull/8441)\)\.
* proxmox \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8814](https\://github\.com/ansible\-collections/community\.general/pull/8814)\)\.
* proxmox \- translate the old <code>disk</code> and <code>mounts</code> keys to the new handling internally \([https\://github\.com/ansible\-collections/community\.general/pull/8542](https\://github\.com/ansible\-collections/community\.general/pull/8542)\)\.
* proxmox inventory plugin \- add new fact for LXC interface details \([https\://github\.com/ansible\-collections/community\.general/pull/8713](https\://github\.com/ansible\-collections/community\.general/pull/8713)\)\.
* proxmox inventory plugin \- clean up authentication code \([https\://github\.com/ansible\-collections/community\.general/pull/8917](https\://github\.com/ansible\-collections/community\.general/pull/8917)\)\.
* proxmox inventory plugin \- fix urllib3 <code>InsecureRequestWarnings</code> not being suppressed when a token is used \([https\://github\.com/ansible\-collections/community\.general/pull/9099](https\://github\.com/ansible\-collections/community\.general/pull/9099)\)\.
* proxmox\_disk \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8814](https\://github\.com/ansible\-collections/community\.general/pull/8814)\)\.
* proxmox\_kvm \- adds the <code>ciupgrade</code> parameter to specify whether cloud\-init should upgrade system packages at first boot \([https\://github\.com/ansible\-collections/community\.general/pull/9066](https\://github\.com/ansible\-collections/community\.general/pull/9066)\)\.
* proxmox\_kvm \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8814](https\://github\.com/ansible\-collections/community\.general/pull/8814)\)\.
* proxmox\_kvm \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8822](https\://github\.com/ansible\-collections/community\.general/pull/8822)\)\.
* proxmox\_template \- small refactor in logic for determining whether a template exists or not \([https\://github\.com/ansible\-collections/community\.general/pull/8516](https\://github\.com/ansible\-collections/community\.general/pull/8516)\)\.
* proxmox\_vm\_info \- add <code>network</code> option to retrieve current network information \([https\://github\.com/ansible\-collections/community\.general/pull/8471](https\://github\.com/ansible\-collections/community\.general/pull/8471)\)\.
* redfish\_\* modules \- adds <code>ciphers</code> option for custom cipher selection \([https\://github\.com/ansible\-collections/community\.general/pull/8533](https\://github\.com/ansible\-collections/community\.general/pull/8533)\)\.
* redfish\_command \- add <code>UpdateUserAccountTypes</code> command \([https\://github\.com/ansible\-collections/community\.general/issues/9058](https\://github\.com/ansible\-collections/community\.general/issues/9058)\, [https\://github\.com/ansible\-collections/community\.general/pull/9059](https\://github\.com/ansible\-collections/community\.general/pull/9059)\)\.
* redfish\_command \- add <code>wait</code> and <code>wait\_timeout</code> options to allow a user to block a command until a service is accessible after performing the requested command \([https\://github\.com/ansible\-collections/community\.general/issues/8051](https\://github\.com/ansible\-collections/community\.general/issues/8051)\, [https\://github\.com/ansible\-collections/community\.general/pull/8434](https\://github\.com/ansible\-collections/community\.general/pull/8434)\)\.
* redfish\_command \- add handling of the <code>PasswordChangeRequired</code> message from services in the <code>UpdateUserPassword</code> command to directly modify the user\'s password if the requested user is the one invoking the operation \([https\://github\.com/ansible\-collections/community\.general/issues/8652](https\://github\.com/ansible\-collections/community\.general/issues/8652)\, [https\://github\.com/ansible\-collections/community\.general/pull/8653](https\://github\.com/ansible\-collections/community\.general/pull/8653)\)\.
* redfish\_confg \- remove <code>CapacityBytes</code> from required paramaters of the <code>CreateVolume</code> command \([https\://github\.com/ansible\-collections/community\.general/pull/8956](https\://github\.com/ansible\-collections/community\.general/pull/8956)\)\.
* redfish\_config \- add parameter <code>storage\_none\_volume\_deletion</code> to <code>CreateVolume</code> command in order to control the automatic deletion of non\-RAID volumes \([https\://github\.com/ansible\-collections/community\.general/pull/8990](https\://github\.com/ansible\-collections/community\.general/pull/8990)\)\.
* redfish\_info \- add command <code>CheckAvailability</code> to check if a service is accessible \([https\://github\.com/ansible\-collections/community\.general/issues/8051](https\://github\.com/ansible\-collections/community\.general/issues/8051)\, [https\://github\.com/ansible\-collections/community\.general/pull/8434](https\://github\.com/ansible\-collections/community\.general/pull/8434)\)\.
* redfish\_info \- adds <code>RedfishURI</code> and <code>StorageId</code> to Disk inventory \([https\://github\.com/ansible\-collections/community\.general/pull/8937](https\://github\.com/ansible\-collections/community\.general/pull/8937)\)\.
* redfish\_utils \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8833](https\://github\.com/ansible\-collections/community\.general/pull/8833)\)\.
* redfish\_utils module utils \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8822](https\://github\.com/ansible\-collections/community\.general/pull/8822)\)\.
* redfish\_utils module utils \- schedule a BIOS configuration job at next reboot when the BIOS config is changed \([https\://github\.com/ansible\-collections/community\.general/pull/9012](https\://github\.com/ansible\-collections/community\.general/pull/9012)\)\.
* redis cache plugin \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8833](https\://github\.com/ansible\-collections/community\.general/pull/8833)\)\.
* redis\, redis\_info \- add <code>client\_cert</code> and <code>client\_key</code> options to specify path to certificate for Redis authentication  \([https\://github\.com/ansible\-collections/community\.general/pull/8654](https\://github\.com/ansible\-collections/community\.general/pull/8654)\)\.
* redis\_info \- adds support for getting cluster info \([https\://github\.com/ansible\-collections/community\.general/pull/8464](https\://github\.com/ansible\-collections/community\.general/pull/8464)\)\.
* remove\_keys filter plugin \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8814](https\://github\.com/ansible\-collections/community\.general/pull/8814)\)\.
* replace\_keys filter plugin \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8814](https\://github\.com/ansible\-collections/community\.general/pull/8814)\)\.
* scaleway \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8833](https\://github\.com/ansible\-collections/community\.general/pull/8833)\)\.
* scaleway module utils \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8822](https\://github\.com/ansible\-collections/community\.general/pull/8822)\)\.
* scaleway\_compute \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8833](https\://github\.com/ansible\-collections/community\.general/pull/8833)\)\.
* scaleway\_container \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8858](https\://github\.com/ansible\-collections/community\.general/pull/8858)\)\.
* scaleway\_container\_info \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8858](https\://github\.com/ansible\-collections/community\.general/pull/8858)\)\.
* scaleway\_container\_namespace \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8858](https\://github\.com/ansible\-collections/community\.general/pull/8858)\)\.
* scaleway\_container\_namespace\_info \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8858](https\://github\.com/ansible\-collections/community\.general/pull/8858)\)\.
* scaleway\_container\_registry \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8858](https\://github\.com/ansible\-collections/community\.general/pull/8858)\)\.
* scaleway\_container\_registry\_info \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8858](https\://github\.com/ansible\-collections/community\.general/pull/8858)\)\.
* scaleway\_function \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8858](https\://github\.com/ansible\-collections/community\.general/pull/8858)\)\.
* scaleway\_function\_info \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8858](https\://github\.com/ansible\-collections/community\.general/pull/8858)\)\.
* scaleway\_function\_namespace \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8858](https\://github\.com/ansible\-collections/community\.general/pull/8858)\)\.
* scaleway\_function\_namespace\_info \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8858](https\://github\.com/ansible\-collections/community\.general/pull/8858)\)\.
* scaleway\_ip \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8833](https\://github\.com/ansible\-collections/community\.general/pull/8833)\)\.
* scaleway\_lb \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8833](https\://github\.com/ansible\-collections/community\.general/pull/8833)\)\.
* scaleway\_security\_group \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8822](https\://github\.com/ansible\-collections/community\.general/pull/8822)\)\.
* scaleway\_security\_group \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8833](https\://github\.com/ansible\-collections/community\.general/pull/8833)\)\.
* scaleway\_user\_data \- better construct when using <code>dict\.items\(\)</code> \([https\://github\.com/ansible\-collections/community\.general/pull/8876](https\://github\.com/ansible\-collections/community\.general/pull/8876)\)\.
* scaleway\_user\_data \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8833](https\://github\.com/ansible\-collections/community\.general/pull/8833)\)\.
* sensu\_silence \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8833](https\://github\.com/ansible\-collections/community\.general/pull/8833)\)\.
* snmp\_facts \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8833](https\://github\.com/ansible\-collections/community\.general/pull/8833)\)\.
* sorcery \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8833](https\://github\.com/ansible\-collections/community\.general/pull/8833)\)\.
* sudosu become plugin \- added an option \(<code>alt\_method</code>\) to enhance compatibility with more versions of <code>su</code> \([https\://github\.com/ansible\-collections/community\.general/pull/8214](https\://github\.com/ansible\-collections/community\.general/pull/8214)\)\.
* udm\_dns\_record \- replace loop with <code>dict\.update\(\)</code> \([https\://github\.com/ansible\-collections/community\.general/pull/8876](https\://github\.com/ansible\-collections/community\.general/pull/8876)\)\.
* ufw \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8822](https\://github\.com/ansible\-collections/community\.general/pull/8822)\)\.
* unsafe plugin utils \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8814](https\://github\.com/ansible\-collections/community\.general/pull/8814)\)\.
* vardict module utils \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8814](https\://github\.com/ansible\-collections/community\.general/pull/8814)\)\.
* vars MH module utils \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8814](https\://github\.com/ansible\-collections/community\.general/pull/8814)\)\.
* virtualbox inventory plugin \- expose a new parameter <code>enable\_advanced\_group\_parsing</code> to change how the VirtualBox dynamic inventory parses VM groups \([https\://github\.com/ansible\-collections/community\.general/issues/8508](https\://github\.com/ansible\-collections/community\.general/issues/8508)\, [https\://github\.com/ansible\-collections/community\.general/pull/8510](https\://github\.com/ansible\-collections/community\.general/pull/8510)\)\.
* vmadm \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8822](https\://github\.com/ansible\-collections/community\.general/pull/8822)\)\.
* wdc\_redfish\_command \- minor change to handle upgrade file for Redfish WD platforms \([https\://github\.com/ansible\-collections/community\.general/pull/8444](https\://github\.com/ansible\-collections/community\.general/pull/8444)\)\.

<a id="community-grafana-2"></a>
#### community\.grafana

* Add <em class="title-reference">grafana\_contact\_point</em> module
* Add support of <em class="title-reference">grafana\_contact\_point</em> in grafana role
* Manage subfolders for <em class="title-reference">grafana\_folder</em> and specify uid
* add org switch by <em class="title-reference">org\_id</em> and <em class="title-reference">org\_name</em> in <em class="title-reference">grafana\_silence</em>

<a id="community-mysql-7"></a>
#### community\.mysql

* mysql\_info \- Add <code>tls\_requires</code> returned value for the <code>users\_info</code> filter \([https\://github\.com/ansible\-collections/community\.mysql/pull/628](https\://github\.com/ansible\-collections/community\.mysql/pull/628)\)\.
* mysql\_info \- return a database server engine used \([https\://github\.com/ansible\-collections/community\.mysql/issues/644](https\://github\.com/ansible\-collections/community\.mysql/issues/644)\)\.
* mysql\_replication \- Adds support for <em class="title-reference">CHANGE REPLICATION SOURCE TO</em> statement \([https\://github\.com/ansible\-collections/community\.mysql/issues/635](https\://github\.com/ansible\-collections/community\.mysql/issues/635)\)\.
* mysql\_replication \- Adds support for <em class="title-reference">SHOW BINARY LOG STATUS</em> and <em class="title-reference">SHOW BINLOG STATUS</em> on getprimary mode\.
* mysql\_replication \- Improve detection of IsReplica and IsPrimary by inspecting the dictionary returned from the SQL query instead of relying on variable types\. This ensures compatibility with changes in the connector or the output of SHOW REPLICA STATUS and SHOW MASTER STATUS\, allowing for easier maintenance if these change in the future\.
* mysql\_user \- Add salt parameter to generate static hash for <em class="title-reference">caching\_sha2\_password</em> and <em class="title-reference">sha256\_password</em> plugins\.

<a id="community-okd-1"></a>
#### community\.okd

* connection/oc \- added support of local enviroment variable that will be used for <code>oc</code> and may be requried for establishing connections ifself \([https\://github\.com/openshift/community\.okd/pull/225](https\://github\.com/openshift/community\.okd/pull/225)\)\.
* inventory/openshift\.py \- Defer removal of k8s inventory plugin to version 5\.0\.0 \([https\://github\.com/openshift/community\.okd/pull/224](https\://github\.com/openshift/community\.okd/pull/224)\)\.

<a id="community-postgresql-12"></a>
#### community\.postgresql

* postgres \- add support for postgres <code>infinity</code> timestamps by replacing them with <code>datetime\.min</code> / <code>datetime\.max</code> values \([https\://github\.com/ansible\-collections/community\.postgresql/pull/714](https\://github\.com/ansible\-collections/community\.postgresql/pull/714)\)\.
* postgresql\_privs \- adds support for granting and revoking privileges on foreign tables \([https\://github\.com/ansible\-collections/community\.postgresql/issues/724](https\://github\.com/ansible\-collections/community\.postgresql/issues/724)\)\.
* postgresql\_publication \- add the <code>tables\_in\_schema</code> argument to implement <code>FOR TABLES IN SCHEMA</code> feature \([https\://github\.com/ansible\-collections/community\.postgresql/issues/709](https\://github\.com/ansible\-collections/community\.postgresql/issues/709)\)\.
* postgresql\_set \- adds the <code>queries</code> return value to return executed DML statements\.
* postgresql\_subscription \- adds support for managing subscriptions in the situation where the <code>subconninfo</code> column is unavailable \(such as in CloudSQL\) \([https\://github\.com/ansible\-collections/community\.postgresql/issues/726](https\://github\.com/ansible\-collections/community\.postgresql/issues/726)\)\.
* postgresql\_user \- adds the <code>configuration</code> argument that allows to manage user\-specific default configuration \([https\://github\.com/ansible\-collections/community\.postgresql/issues/598](https\://github\.com/ansible\-collections/community\.postgresql/issues/598)\)\.

<a id="community-proxysql"></a>
#### community\.proxysql

* proxysql role \- add the pidfile location management \([https\://github\.com/ansible\-collections/community\.proxysql/pull/145](https\://github\.com/ansible\-collections/community\.proxysql/pull/145)\)\.
* role\_proxysql \- Update default proxysql version and fix small bugs \([https\://github\.com/ansible\-collections/community\.proxysql/pull/92](https\://github\.com/ansible\-collections/community\.proxysql/pull/92)\)\.

<a id="community-routeros-8"></a>
#### community\.routeros

* api\_info \- allow to restrict the output by limiting fields to specific values with the new <code>restrict</code> option \([https\://github\.com/ansible\-collections/community\.routeros/pull/305](https\://github\.com/ansible\-collections/community\.routeros/pull/305)\)\.
* api\_info\, api\_modify \- add <code>system health settings</code> path \([https\://github\.com/ansible\-collections/community\.routeros/pull/294](https\://github\.com/ansible\-collections/community\.routeros/pull/294)\)\.
* api\_info\, api\_modify \- add missing path <code>/ppp secret</code> \([https\://github\.com/ansible\-collections/community\.routeros/pull/286](https\://github\.com/ansible\-collections/community\.routeros/pull/286)\)\.
* api\_info\, api\_modify \- add missing path <code>/system resource irq rps</code> \([https\://github\.com/ansible\-collections/community\.routeros/pull/295](https\://github\.com/ansible\-collections/community\.routeros/pull/295)\)\.
* api\_info\, api\_modify \- add new parameters from the RouterOS 7\.16 release \([https\://github\.com/ansible\-collections/community\.routeros/pull/323](https\://github\.com/ansible\-collections/community\.routeros/pull/323)\)\.
* api\_info\, api\_modify \- add parameter <code>host\-key\-type</code> for <code>ip ssh</code> path \([https\://github\.com/ansible\-collections/community\.routeros/issues/280](https\://github\.com/ansible\-collections/community\.routeros/issues/280)\, [https\://github\.com/ansible\-collections/community\.routeros/pull/297](https\://github\.com/ansible\-collections/community\.routeros/pull/297)\)\.
* api\_info\, api\_modify \- add support <code>interface l2tp\-client</code> configuration \([https\://github\.com/ansible\-collections/community\.routeros/pull/322](https\://github\.com/ansible\-collections/community\.routeros/pull/322)\)\.
* api\_info\, api\_modify \- add support for the <code>cpu\-frequency</code>\, <code>memory\-frequency</code>\, <code>preboot\-etherboot</code> and <code>preboot\-etherboot\-server</code> properties in <code>system routerboard settings</code> \([https\://github\.com/ansible\-collections/community\.routeros/pull/320](https\://github\.com/ansible\-collections/community\.routeros/pull/320)\)\.
* api\_info\, api\_modify \- add support for the <code>ip dhcp\-server matcher</code> path \([https\://github\.com/ansible\-collections/community\.routeros/pull/300](https\://github\.com/ansible\-collections/community\.routeros/pull/300)\)\.
* api\_info\, api\_modify \- add support for the <code>ip dns adlist</code> path implemented by RouterOS 7\.15 and newer \([https\://github\.com/ansible\-collections/community\.routeros/pull/310](https\://github\.com/ansible\-collections/community\.routeros/pull/310)\)\.
* api\_info\, api\_modify \- add support for the <code>ipv6 nd prefix</code> path \([https\://github\.com/ansible\-collections/community\.routeros/pull/303](https\://github\.com/ansible\-collections/community\.routeros/pull/303)\)\.
* api\_info\, api\_modify \- add support for the <code>matching\-type</code> property in <code>ip dhcp\-server matcher</code> introduced by RouterOS 7\.16 \([https\://github\.com/ansible\-collections/community\.routeros/pull/321](https\://github\.com/ansible\-collections/community\.routeros/pull/321)\)\.
* api\_info\, api\_modify \- add support for the <code>mld\-version</code> and <code>multicast\-querier</code> properties in <code>interface bridge</code> \([https\://github\.com/ansible\-collections/community\.routeros/pull/315](https\://github\.com/ansible\-collections/community\.routeros/pull/315)\)\.
* api\_info\, api\_modify \- add support for the <code>name</code> and <code>is\-responder</code> properties under the <code>interface wireguard peers</code> path introduced in RouterOS 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/304](https\://github\.com/ansible\-collections/community\.routeros/pull/304)\)\.
* api\_info\, api\_modify \- add support for the <code>routing filter num\-list</code> path implemented by RouterOS 7 and newer \([https\://github\.com/ansible\-collections/community\.routeros/pull/313](https\://github\.com/ansible\-collections/community\.routeros/pull/313)\)\.
* api\_info\, api\_modify \- add support for the <code>routing igmp\-proxy</code> path \([https\://github\.com/ansible\-collections/community\.routeros/pull/309](https\://github\.com/ansible\-collections/community\.routeros/pull/309)\)\.
* api\_info\, api\_modify \- add support for the <code>routing ospf static\-neighbor</code> path in RouterOS 7 \([https\://github\.com/ansible\-collections/community\.routeros/pull/302](https\://github\.com/ansible\-collections/community\.routeros/pull/302)\)\.
* api\_info\, api\_modify \- minor changes <code>/interface ethernet</code> path fields \([https\://github\.com/ansible\-collections/community\.routeros/pull/288](https\://github\.com/ansible\-collections/community\.routeros/pull/288)\)\.
* api\_info\, api\_modify \- set default for <code>force</code> in <code>ip dhcp\-server option</code> to an explicit <code>false</code> \([https\://github\.com/ansible\-collections/community\.routeros/pull/300](https\://github\.com/ansible\-collections/community\.routeros/pull/300)\)\.
* api\_modify \- allow to restrict what is updated by limiting fields to specific values with the new <code>restrict</code> option \([https\://github\.com/ansible\-collections/community\.routeros/pull/305](https\://github\.com/ansible\-collections/community\.routeros/pull/305)\)\.
* api\_modify\, api\_info \- add read\-only <code>default</code> field to <code>snmp community</code> \([https\://github\.com/ansible\-collections/community\.routeros/pull/311](https\://github\.com/ansible\-collections/community\.routeros/pull/311)\)\.

<a id="community-sops-4"></a>
#### community\.sops

* Detect SOPS 3\.9\.0 and use new <code>decrypt</code> and <code>encrypt</code> subcommands \([https\://github\.com/ansible\-collections/community\.sops/pull/190](https\://github\.com/ansible\-collections/community\.sops/pull/190)\)\.
* decrypt filter plugin \- now supports the input and output type <code>ini</code> \([https\://github\.com/ansible\-collections/community\.sops/pull/204](https\://github\.com/ansible\-collections/community\.sops/pull/204)\)\.
* sops lookup plugin \- new option <code>extract</code> allows extracting a single key out of a JSON or YAML file\, equivalent to sops\' <code>decrypt \-\-extract</code> \([https\://github\.com/ansible\-collections/community\.sops/pull/200](https\://github\.com/ansible\-collections/community\.sops/pull/200)\)\.
* sops lookup plugin \- now supports the input and output type <code>ini</code> \([https\://github\.com/ansible\-collections/community\.sops/pull/204](https\://github\.com/ansible\-collections/community\.sops/pull/204)\)\.
* sops vars plugin \- allow to configure the valid extensions with an <code>ansible\.cfg</code> entry or with an environment variable \([https\://github\.com/ansible\-collections/community\.sops/pull/185](https\://github\.com/ansible\-collections/community\.sops/pull/185)\)\.
* sops vars plugin \- new option <code>handle\_unencrypted\_files</code> allows to control behavior when encountering unencrypted files with SOPS 3\.9\.0\+ \([https\://github\.com/ansible\-collections/community\.sops/pull/190](https\://github\.com/ansible\-collections/community\.sops/pull/190)\)\.

<a id="community-vmware-19"></a>
#### community\.vmware

* vmware\_host\_logbundle \- Add timeout parameter \([https\://github\.com/ansible\-collections/community\.vmware/pull/2092](https\://github\.com/ansible\-collections/community\.vmware/pull/2092)\)\.
* vmware\_vm\_info \- Improve performance when parsing custom attributes information \([https\://github\.com/ansible\-collections/community\.vmware/pull/2194](https\://github\.com/ansible\-collections/community\.vmware/pull/2194)\)
* vmware\_vm\_vm\_drs\_rule \- added datacenter argument to correctly deal with multiple clusters with same name\([https\://github\.com/ansible\-collections/community\.vmware/issues/2101](https\://github\.com/ansible\-collections/community\.vmware/issues/2101)\)\.
* vsphere\_file \- Fix examples in documentation \([https\://github\.com/ansible\-collections/community\.vmware/issues/2110](https\://github\.com/ansible\-collections/community\.vmware/issues/2110)\)\.

<a id="community-windows-1"></a>
#### community\.windows

* Set minimum supported Ansible version to 2\.15 to align with the versions still supported by Asnible\.

<a id="community-zabbix-6"></a>
#### community\.zabbix

* All Roles \- Add support for yum authentication on RHEL based operating systems\.
* All Roles \- Add the <em class="title-reference">zabbix\_manage\_repo</em> variable\.
* All Roles \- Added support for Ubuntu 24\.04 \(Noble Numbat\)
* All Roles \- Changed logic for installing selinux related changes based the status of selinux on the target system\.
* All Roles \- Include installation of GPG key for RHEL based operating systems\.
* All Roles \- Updated all Zabbix configuration bool variables to be <em class="title-reference">true</em>/<em class="title-reference">false</em>\.
* All Roles \- Updated include option to include all \.conf files\.
* added new module zabbix\_proxy\_group \(Zabbix 7\.0\)
* httpapi \- added ability to switch username/password during playbook execution\.
* zabbix\_agent Role \- Fixes assert warning \'conditional statements should not include jinja2 templating delimiters such as\.\.\'
* zabbix\_agent Role \- Reworked Include logic based on Alias logic
* zabbix\_agent Role \- Set <em class="title-reference">no\_log</em> parameter to hostmacro API call\.
* zabbix\_agent role \- Standardized all configuration variables using the <em class="title-reference">zabbix\_agent</em> prefix vs <em class="title-reference">zabbix\_agent2</em>\.  Support for <em class="title-reference">zabbix\_agent2</em> to be removed in 3\.0\.0
* zabbix\_agent role \- Standardized templating of agent\.conf file
* zabbix\_agent role \- Updated defaults to be inline with Zabbix defaults\.
* zabbix\_agent role \- added 10 retries to agent API calls to workaround connection problems on macOS
* zabbix\_agent role \- refactored userparameter tasks to be more efficient\.
* zabbix\_discovery\_rule\, zabbix\_group\_events\_info\, zabbix\_host\, zabbix\_host\_events\_info\, zabbix\_proxy\, zabbix\_proxy\_info modules updated to work wih Zabbix 7\.0
* zabbix\_discoveryrule module added
* zabbix\_host\_events\_info \- add tag support
* zabbix\_host\_events\_update module added
* zabbix\_inventory Plugin \- Add support for jinja2 templating for auth\_token in zabbix\_inventory\.yml
* zabbix\_item \- add support for setting master items by name
* zabbix\_item module added
* zabbix\_itemprototype \- add support for setting master items by name
* zabbix\_itemprototype module added
* zabbix\_mfa module added
* zabbix\_trigger module added
* zabbix\_triggerprototype module added

<a id="containers-podman-3"></a>
#### containers\.podman

* Add arch to podman build command explicitly
* Add autodiscovery for build context in podman\_image
* Add docs\, tests and more examples for podman\_pod
* Add extra\_args for podman\_image push and pull
* Add group\_add parameter for podman quadlet
* Add idempotency for mounts and volumes in podman\_container
* Add new functionality tests for podman\_secret
* Add option for inline Containerfile in podman\_image
* Add path and env options for podman\_secret
* Add route\, dns and ipam\_driver to podman\_network
* Add support for check\_mode in Quadlet
* CI Update python for latest Ansible to 3\.11 in CI
* Create podman secret when skip\_existing\=True and it does not exist
* Trigger a new image build when we detect that the Containerfile has changed\.
* Update inspection info about objects in modules

<a id="dellemc-enterprise-sonic"></a>
#### dellemc\.enterprise\_sonic

* bgp\_af \- Add support for \'import vrf\' commands \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/351](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/351)\)\.
* sonic\_bfd \- Add playbook check and diff modes support for bfd module \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/346](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/346)\)\.
* sonic\_bgp \- Add playbook check and diff modes support for bgp module \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/350](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/350)\)\.
* sonic\_bgp \- Add support BGP Asn Notation \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/417](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/417)\)\.
* sonic\_bgp \- Fix GitHub issue\# 416 \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/418](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/418)\)\.
* sonic\_bgp\_af \- Add playbook check and diff modes support for bgp\_af module \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/350](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/350)\)\.
* sonic\_bgp\_af \- Add support for BGP Asn Notation \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/417](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/417)\)\.
* sonic\_bgp\_af \- Add support for aggregate address configuration\([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/398](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/398)\)\.
* sonic\_bgp\_af \- Update replaced state handling \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/400](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/400)\)
* sonic\_bgp\_as\_paths \- Add playbook check and diff modes support for bgp\_as\_paths module \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/350](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/350)\)\.
* sonic\_bgp\_communities \- Add playbook check and diff modes support for bgp\_communities module \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/350](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/350)\)\.
* sonic\_bgp\_ext\_communities \- Add playbook check and diff modes support for bgp\_ext\_communities module \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/350](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/350)\)\.
* sonic\_bgp\_neighbors \- Add playbook check and diff modes support for bgp\_neighbors module \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/360](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/360)\)\.
* sonic\_bgp\_neighbors \- Add support for BGP Asn Notation \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/417](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/417)\)\.
* sonic\_bgp\_neighbors \- Add support for replaced and overridden states \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/335](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/335)\)\.
* sonic\_bgp\_neighbors \- Add support for replaced and overridden states \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/336](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/336)\)\.
* sonic\_bgp\_neighbors \- Add support for the \"fabric\_external\" option \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/336](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/336)\)\.
* sonic\_bgp\_neighbors\_af \- Add playbook check and diff modes support for bgp\_neighbors\_af module \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/360](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/360)\)\.
* sonic\_bgp\_neighbors\_af \- Add support for BGP Asn Notation \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/417](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/417)\)\.
* sonic\_copp \- Add playbook check and diff modes support for copp module \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/346](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/346)\)\.
* sonic\_dhcp\_relay \- Add playbook check and diff modes support for dhcp\_relay module \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/346](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/346)\)\.
* sonic\_dhcp\_snooping \- Add playbook check and diff modes support for dhcp\_snooping module \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/346](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/346)\)\.
* sonic\_interfaces \- Add description\, enabled option support for Loopback interfaces \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/364](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/364)\)\.
* sonic\_interfaces \- Fix GitHub issue 357 \- set proper default value when deleted \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/366](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/366)\)\.
* sonic\_interfaces \- Update replaced state handling \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/364](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/364)\)\.
* sonic\_l3\_interfaces \- Add playbook check and diff modes support for l3\_interfaces module \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/328](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/328)\)\.
* sonic\_l3\_interfaces \- Add support for USGv6R1 related features \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/374](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/374)\)\.
* sonic\_l3\_interfaces \- Fix IPv6 default dad configuration handling \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/428](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/428)\)\.
* sonic\_lag\_interfaces \- Add evpn ethernet\-segment support for LAG interfaces \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/403](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/403)\)\.
* sonic\_lldp\_global \- Add playbook check and diff modes support for lldp\_global module \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/338](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/338)\)\.
* sonic\_logging \- Add support for protocol option in logging module \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/317](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/317)\)\.
* sonic\_mac \- Add playbook check and diff modes support for mac module \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/338](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/338)\)\.
* sonic\_mclag \- Add playbook check and diff modes support for mclag module \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/337](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/337)\)\.
* sonic\_mclag \- Enable session\-vrf command support in mclag\([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/299](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/299)\)\.
* sonic\_port\_breakout \- Add playbook check and diff modes support for port\_breakout module \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/337](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/337)\)\.
* sonic\_port\_group \- Make error message for port group facts gathering more descriptive \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/396](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/396)\)\.
* sonic\_prefix\_lists \- Add playbook check and diff modes support for prefix\_lists module \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/331](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/331)\)\.
* sonic\_qos\_maps \- Comment out PFC priority group map tests cases \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/395](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/395)\)\.
* sonic\_qos\_scheduler \- Update states implementation \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/373](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/373)\)\.
* sonic\_route\_maps \- Add UT for route maps module \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/384](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/384)\)\.
* sonic\_route\_maps \- Add playbook check and diff modes support for route\_maps module \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/331](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/331)\)\.
* sonic\_route\_maps \- Add support for BGP Asn Notation \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/417](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/417)\)\.
* sonic\_route\_maps \- Add support for the \'set tag\' option and synchronize module documentation with argspec and model \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/413](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/413)\)\.
* sonic\_stp \- Add playbook check and diff modes support for stp module \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/338](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/338)\)\.
* sonic\_system \- Add support for \'standard\_extended\' interface\-naming mode \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/352](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/352)\)\.
* sonic\_system \- Add support for configuring auto\-breakout feature \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/342](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/342)\)\.
* sonic\_system \- Adding Versatile Hash feature\.\([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/401](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/401)\)\.
* sonic\_system \- Enable auditd command support\([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/405](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/405)\)\.
* sonic\_system \- Update replaced state handling \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/388](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/388)\)\.
* sonic\_vxlan \- Fix GitHub issue 376 \- Change vxlan module get\_fact function \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/393](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/393)\)\.
* sonic\_vxlans \- Add playbook check and diff modes support for vxlans module \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/337](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/337)\)\.
* sonic\_vxlans \- Add support for the \"external\_ip\" vxlan option \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/330](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/330)\)\.

<a id="dellemc-openmanage-14"></a>
#### dellemc\.openmanage

* Added support for Python 3\.12\.
* Added time\_to\_wait option in <code>idrac\_storage\_volume</code> module\.
* idrac\_firmware\_info \- This module is enhanced to support iDRAC10\.
* idrac\_redfish\_powerstate \- This module is enhanced to support full virtual A/C power cycle\.
* idrac\_redfish\_storage\_controller \- This module is enhanced to support secure and/or cryptographic erase of the physical disk\.
* idrac\_reset \- This module is enhanced to provide default username and default password for the reset operation\.
* ome\_application\_certificate \- This module is enhanced to support the upload of certificate chain\.
* ome\_application\_network\_proxy \- This module is enhanced to manage the Proxy Exclusion List and Certificate Validation\.

<a id="dellemc-powerflex-2"></a>
#### dellemc\.powerflex

* Added support for PowerFlex Onyx version\(4\.6\.x\)\.
* Fixed the roles to support attaching the MDM cluster to the gateway\.
* The storage pool module has been enhanced to support more features\.

<a id="f5networks-f5-modules-4"></a>
#### f5networks\.f5\_modules

* bigip\_asm\_dos\_application \- add support for creating dos profile\.
* bigip\_device\_info \- virtual\-servers \- return per\_flow\_request\_access\_policy if defined\.
* bigip\_gtm\_server \- Added check for datacenter existence in Check Mode\.
* bigip\_pool\_member \- Removed state from the Returnables\.
* bigip\_ucs \- Fix for bigip\_ucs module to restore UCS file on BIG\-IP devices\.
* bigip\_virtual\_server \- set per\_flow\_request\_access\_policy and stay idempotent\.

<a id="fortinet-fortimanager-7"></a>
#### fortinet\.fortimanager

* Supported FortiManager 7\.4\.3\. 7 new modules\.
* Supported FortiManager 7\.6\.0\. Added 7 new modules\.
* Supported ansible\-core 2\.17\.
* Supported check mode for all modules except \"fmgr\_generic\"\. You can use \"ansible\-playbook \-i \<your\-host\-file\> \<your\-playbook\> \-\-check\" to validate whether your playbook will make any changes to the FortiManager\.

<a id="google-cloud-5"></a>
#### google\.cloud

* ansible \- 2\.16\.0 is now the minimum version supported
* ansible \- 3\.10 is now the minimum Python version
* ansible\-test \- integration tests are now run against 2\.16\.0 and 2\.17\.0
* gcloud role \- use dnf instead of yum on RHEL
* gcp\_secret\_manager \- add as a module and lookup plugin \([https\://github\.com/ansible\-collections/google\.cloud/pull/578](https\://github\.com/ansible\-collections/google\.cloud/pull/578)\)
* gcp\_secret\_manager \- support more than 10 versions \([https\://github\.com/ansible\-collections/google\.cloud/pull/634](https\://github\.com/ansible\-collections/google\.cloud/pull/634)\)
* restore google\_cloud\_ops\_agents submodule \([https\://github\.com/ansible\-collections/google\.cloud/pull/594](https\://github\.com/ansible\-collections/google\.cloud/pull/594)\)

<a id="hetzner-hcloud-2"></a>
#### hetzner\.hcloud

* Use a truncated exponential backoff algorithm when polling actions from the API\.
* load\_balancer\_status \- Add new filter to compute the status of a Load Balancer based on its targets\.
* server\_type\_info \- The \'included\_traffic\' return value is deprecated and will be set to \'None\' on 5 August 2024\. See [https\://docs\.hetzner\.cloud/changelog\#2024\-07\-25\-cloud\-api\-returns\-traffic\-information\-in\-different\-format](https\://docs\.hetzner\.cloud/changelog\#2024\-07\-25\-cloud\-api\-returns\-traffic\-information\-in\-different\-format)\.

<a id="ibm-storage-virtualize-7"></a>
#### ibm\.storage\_virtualize

* ibm\_sv\_manage\_security \- Added support to allow automatic download of security patches
* ibm\_sv\_manage\_storage\_partition \- Added support for creating draft partition\, publishing a draft partition\, and merging 2 partitions
* ibm\_sv\_manage\_syslog\_server \- Added support for creating TLS syslog server\, and modifying existing UDP or TCP servers to TLS server
* ibm\_sv\_manage\_truststore\_for\_replication \- Added support for enabling various options \(syslog\, RESTAPI\, vasa\, ipsec\, snmp and email\) during truststore creation
* ibm\_svc\_host \- Added support to add host into draft partition and to create an NVMeFC host
* ibm\_svc\_info \- Added support to display concise view of all SVC objects not covered by I\(gather\_subset\)\, detailed view for all SVC objects\, concise view of a subset of objects allowing a I\(filtervalue\)
* ibm\_svc\_manage\_portset \- Added support to create a high\-speed replication portset
* ibm\_svc\_manage\_volumegroup \- Added support to add existing volumegroups into draft partition
* ibm\_svcinfo\_command \- Added support for sainfo commands
* ibm\_svctask\_command \- Added support for satask commands

<a id="infoblox-nios-modules-2"></a>
#### infoblox\.nios\_modules

* Added IPv6 network container support for the <em class="title-reference">nios\_next\_network</em> lookup plugin\.
* Added <em class="title-reference">use\_range</em> parameter to the nios\_next\_ip lookup plugin\, enabling lookup for the next available IP from a network range\.
* Added support for the <em class="title-reference">use\_dns\_ea\_inheritance</em> parameter in Host Record to inherit EA from associated zone\.
* Added support for the <em class="title-reference">use\_for\_ea\_inheritance</em> parameter in Host Record to inherit EA from Host address\.
* Enabled IPv4 support for PXE server configuration in the Host Record module\.
* Improved handling of DHCP options in DHCP Range\, Network\, and Network Container\.
* Introduced <em class="title-reference">use\_logic\_filter\_rules</em> \& <em class="title-reference">logic\_filter\_rules</em> support for both IPv4 and IPv6 network and network container\.
* Upgraded the base WAPI version to 2\.12\.3\.

<a id="junipernetworks-junos-1"></a>
#### junipernetworks\.junos

* Add implementation to gather ether\-channels for gig\-ether\-options\.
* Added support for virtual\-switch instances\.
* Based on ether\-option\-type create supported commands for config module\.
* Implemented bridge\-domains configuration management for routing instances\.
* Implemented support for setting the Maximum Transmission Unit \(MTU\) in Layer 3 \(L3\) Internet Protocol \(IP\) interfaces\.
* Tested successfully on Junos MX204\.

<a id="kubernetes-core-6"></a>
#### kubernetes\.core

* connection/kubectl\.py \- Added an example of using the kubectl connection plugin to the documentation \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/741](https\://github\.com/ansible\-collections/kubernetes\.core/pull/741)\)\.
* inventory/k8s\.py \- Defer removal of k8s inventory plugin to version 5\.0 \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/723](https\://github\.com/ansible\-collections/kubernetes\.core/pull/723)\)\.
* inventory/k8s\.py \- Defer removal of k8s inventory plugin to version 6\.0\.0 \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/734](https\://github\.com/ansible\-collections/kubernetes\.core/pull/734)\)\.
* k8s \- The module and K8sService were changed so warnings returned by the K8S API are now displayed to the user\.
* k8s\_drain \- Improve error message for pod disruption budget when draining a node \([https\://github\.com/ansible\-collections/kubernetes\.core/issues/797](https\://github\.com/ansible\-collections/kubernetes\.core/issues/797)\)\.

<a id="microsoft-ad-4"></a>
#### microsoft\.ad

* Set minimum supported Ansible version to 2\.15 to align with the versions still supported by Ansible\.
* microsoft\.ad AD modules \- Added <code>domain\_credentials</code> as a common module option that can be used to specify credentials for specific AD servers\.
* microsoft\.ad AD modules \- Added <code>lookup\_failure\_action</code> on all modules that can specify a list of distinguishedName values to control what should happen if the lookup fails\.
* microsoft\.ad\.computer \- Added the <code>do\_not\_append\_dollar\_to\_sam</code> option which can create a computer account without the <code>\$</code> suffix when an explicit <code>sam\_account\_name</code> was provided without one\.
* microsoft\.ad\.computer \- Added the ability to lookup a distinguishedName on a specific domain server for <code>delegates</code> and <code>managed\_by</code>\.
* microsoft\.ad\.domain \- Added <code>reboot\_timeout</code> option to control how long a reboot can go for\.
* microsoft\.ad\.domain\_child \- Added <code>reboot\_timeout</code> option to control how long a reboot can go for\.
* microsoft\.ad\.domain\_controller \- Added <code>reboot\_timeout</code> option to control how long a reboot can go for\.
* microsoft\.ad\.group \- Added the ability to lookup a distinguishedName on a specific domain server for <code>managed\_by</code> and <code>members</code>\.
* microsoft\.ad\.membership \- Added <code>domain\_server</code> option to specify the DC to use for domain join operations \- [https\://github\.com/ansible\-collections/microsoft\.ad/issues/131\#issuecomment\-2201151651](https\://github\.com/ansible\-collections/microsoft\.ad/issues/131\#issuecomment\-2201151651)
* microsoft\.ad\.membership \- Added <code>reboot\_timeout</code> option to control how long a reboot can go for\.
* microsoft\.ad\.ou \- Added the ability to lookup a distinguishedName on a specific domain server for <code>managed\_by</code>\.
* microsoft\.ad\.user \- Added the ability to lookup a distinguishedName on a specific domain server for <code>delegates</code>\.
* microsoft\.ad\.user \- Rename the option <code>groups\.missing\_action</code> to <code>groups\.lookup\_failure\_action</code> to make the option more consistent with other modules\. The <code>missing\_action</code> option is still supported as an alias\.
* microsoft\.ad\.user \- Support group member lookup on alternative server using the DN lookup syntax\. This syntax uses a dictionary where <code>name</code> defined the group to lookup and <code>server</code> defines the server to lookup the group on\.

<a id="netapp-cloudmanager"></a>
#### netapp\.cloudmanager

* na\_cloudmanager\_cvo\_aws \- increase timeout for creating cvo to 90 mins\.
* na\_cloudmanager\_cvo\_azure \- increase timeout for creating cvo to 90 mins\.
* na\_cloudmanager\_cvo\_gcp \- increase timeout for creating cvo to 90 mins\.

<a id="netapp-ontap-5"></a>
#### netapp\.ontap

* all modules supporting ZAPI \& REST \- throw authentication error instead of falling back to ZAPI when username/password is incorrect\.
* na\_ontap\_bgp\_peer\_group \- added new option <em class="title-reference">use\_peer\_as\_next\_hop</em>\, requires ONTAP 9\.9 or later\.
* na\_ontap\_cifs \- added REST support for option <em class="title-reference">vscan\_fileop\_profile</em>\, requires ONTAP 9\.15\.1 or later\.
* na\_ontap\_rest\_cli \- return command output for GET and OPTIONS verbs during check mode\.
* na\_ontap\_security\_key\_manager \- added warning message in REST when passphrase is not changed\.
* na\_ontap\_snapshot\_policy \- new option <em class="title-reference">retention\_period</em> added in REST\, requires ONTAP 9\.12 or later\.
* na\_ontap\_volume \- new option <em class="title-reference">activity\_tracking</em> added in REST\, requires ONTAP 9\.10 or later\.
* na\_ontap\_volume \- new option <em class="title-reference">snapshot\_locking</em> added in REST\, requires ONTAP 9\.12 or later\.

<a id="netbox-netbox-3"></a>
#### netbox\.netbox

* Add <code>facility</code> to <code>location</code> \([https\://github\.com/netbox\-community/ansible\_modules/issues/1280](https\://github\.com/netbox\-community/ansible\_modules/issues/1280)\)
* Add <code>related\_object\_type</code> to <code>netbox\_custom\_filed</code> \([https\://github\.com/netbox\-community/ansible\_modules/issues/1268](https\://github\.com/netbox\-community/ansible\_modules/issues/1268)\)
* Add <code>status</code> to <code>location</code> \([https\://github\.com/netbox\-community/ansible\_modules/issues/1279](https\://github\.com/netbox\-community/ansible\_modules/issues/1279)\)
* Add <em class="title-reference">description</em> to <em class="title-reference">netbox\_cluster\_group</em> module \([https\://github\.com/netbox\-community/ansible\_modules/issues/1276](https\://github\.com/netbox\-community/ansible\_modules/issues/1276)\)
* Add <em class="title-reference">serial</em> to <em class="title-reference">netbox\_virtual\_machine</em> module \([https\://github\.com/netbox\-community/ansible\_modules/issues/1309](https\://github\.com/netbox\-community/ansible\_modules/issues/1309)\)
* Add <em class="title-reference">status</em> to <em class="title-reference">netbox\_cluster</em> \([https\://github\.com/netbox\-community/ansible\_modules/issues/1275](https\://github\.com/netbox\-community/ansible\_modules/issues/1275)\)
* Add <em class="title-reference">vid\_ranges</em> to <em class="title-reference">netbox\_vlan\_group</em> module \([https\://github\.com/netbox\-community/ansible\_modules/issues/1307](https\://github\.com/netbox\-community/ansible\_modules/issues/1307)\)
* Add ability to rename variables set on the host by <code>netbox\.netbox\.nb\_inventory</code> through configuration\.
* Add cluster host to dynamic inventory response [\#1219](https\://github\.com/netbox\-community/ansible\_modules/pull/1219)
* Add galaxy\-importer to CI process [\#1245](https\://github\.com/netbox\-community/ansible\_modules/issues/1245)
* Added option <em class="title-reference">hostname\_field</em> to <code>nb\_inventory</code> to be able to set the inventory hostname from a field in custom\_fields
* Adjust modules to support NetBox v4\.0\.0 [\#1234](https\://github\.com/netbox\-community/ansible\_modules/pull/1234)
* Adjust tests for various modules
* Bump jinja2 from 3\.1\.2 to 3\.1\.4 [\#1226](https\://github\.com/netbox\-community/ansible\_modules/pull/1226)
* Bump requests from 2\.31\.0 to 2\.32\.0 [\#1236](https\://github\.com/netbox\-community/ansible\_modules/pull/1236)
* Bump version 3\.19\.1
* Drop obsolete Ansible and Python versions and fix tests [\#1241](https\://github\.com/netbox\-community/ansible\_modules/issues/1241)
* Fix the form\_factor option on netbox\_rack
* Get ansible\-lint passing again \(sequence after [\#1241](https\://github\.com/netbox\-community/ansible\_modules/issues/1241)\) [\#1243](https\://github\.com/netbox\-community/ansible\_modules/issues/1243)
* Update CI for NetBox 4\.1
* Update CI process to follow Ansible Collection Standards [\#1247](https\://github\.com/netbox\-community/ansible\_modules/issues/1247)
* Update CI to use master instead of main\. [\#1253](https\://github\.com/netbox\-community/ansible\_modules/issues/1253)
* Update ansible\-lint to ignore changelog file for yaml indentation\. [\#1256](https\://github\.com/netbox\-community/ansible\_modules/issues/1256)
* Update top\-level README with new minimum Ansible version \(sequence after [\#1241](https\://github\.com/netbox\-community/ansible\_modules/issues/1241) [\#1244](https\://github\.com/netbox\-community/ansible\_modules/issues/1244)
* Updated CI to only run changelog job if PR into devel branch is detected\. [\#1251](https\://github\.com/netbox\-community/ansible\_modules/issues/1251)
* Updated CI to support NetBox 4\.0 [\#1230](https\://github\.com/netbox\-community/ansible\_modules/pull/1230)
* Updates to top\-level README\.md to align collection with Ansible best practices [\#1238](https\://github\.com/netbox\-community/ansible\_modules/issues/1238)

<a id="ngine-io-cloudstack"></a>
#### ngine\_io\.cloudstack

* Added possiblity to disable certs validation using <code>validate\_certs</code> argument \([https\://github\.com/ngine\-io/ansible\-collection\-cloudstack/pull/131](https\://github\.com/ngine\-io/ansible\-collection\-cloudstack/pull/131)\)\.
* cs\_instance \- Added new arguments <code>user\_data\_name</code> and <code>user\_data\_details</code> \([https\://github\.com/ngine\-io/ansible\-collection\-cloudstack/pull/134](https\://github\.com/ngine\-io/ansible\-collection\-cloudstack/pull/134)\)\.
* cs\_project \- Extended to pass <code>cleanup\=true</code> to the deleteProject API when deleting a project \([https\://github\.com/ngine\-io/ansible\-collection\-cloudstack/pull/122](https\://github\.com/ngine\-io/ansible\-collection\-cloudstack/pull/122)\)\.
* cs\_service\_offering \- Add support for storagetag \([https\://github\.com/ngine\-io/ansible\-collection\-cloudstack/pull/118](https\://github\.com/ngine\-io/ansible\-collection\-cloudstack/pull/118)\)\.

<a id="purestorage-flasharray-8"></a>
#### purestorage\.flasharray

* all \- add <code>disable\_warnings</code> parameters
* purefa\_alert \- Add new <code>state</code> of <code>test</code> to check alert manager configuration
* purefa\_alert \- Converted to REST v2
* purefa\_connect \- Add support for TLS encrypted array connections
* purefa\_connect \- Convert to REST v2
* purefa\_console \- Convert to REST v2
* purefa\_dns \- Convert to REST v2
* purefa\_ds \- Add new <code>state</code> of <code>test</code> to check directory services configuration
* purefa\_ds \- Convert to REST v2 removing all parameters used unsupported Purity versions
* purefa\_dsrole \- Convert to REST v2
* purefa\_info \- Add SMTP server information
* purefa\_info \- Fix regression of code that caused volume host connectivity info to be lost
* purefa\_info \- Provide array connection path information
* purefa\_kmip \- Add new <code>state</code> of <code>test</code> to check KMIP object configuration
* purefa\_ntp \- Add new <code>state</code> of <code>test</code> to check NTP configuration
* purefa\_phonehome \- Convert to REST v2
* purefa\_pod \- Add <code>delete\_contents</code> parameter for eradication of pods\.
* purefa\_pod \- Add support for <code>throttle</code> parameter from REST 2\.31\.
* purefa\_pod \- Convert to REST v2\.
* purefa\_ra \- Add new <code>state</code> of <code>test</code> to check remote support configuration
* purefa\_saml \- Add new <code>state</code> of <code>test</code> to check SAML2 IdP configuration
* purefa\_snmp \- Add new <code>state</code> of <code>test</code> to check SNMP manager configuration
* purefa\_syslog \- Add new <code>state</code> of <code>test</code> to check syslog server configuration
* purefa\_token \- Add <code>disable\_warnings</code> support

<a id="purestorage-flashblade-4"></a>
#### purestorage\.flashblade

* all \- add <code>disable\_warnings</code> parameters
* multiple \- YAML lint fixes based on updated <code>ansible\-lint</code> version
* purefb\_bucket \- Add <code>safemode</code> option for <code>retention\_mode</code>
* purefb\_bucket \- Allow bucket quotas to be modified\.
* purefb\_certs \- Update module to use REST v2 code\. This brings in new parameters for certificate management\.
* purefb\_fs \- Set default for group\_ownership to be creator
* purefb\_info \- Add <code>time\_remaining\_status</code> to bucket information from REST 2\.14
* purefb\_info \- Expose SMTP encryption mode
* purefb\_policy \- Add new policy type of <code>worm</code> which is availble from Purity//FB 4\.5\.0
* purefb\_ra \- Add <code>duration</code> option from REST 2\.14
* purefb\_ra \- Update to REST2
* purefb\_smtp \- Add encryption mode support from Purity//FB 4\.5\.0
* purefb\_snap \- Change <code>targets</code> to <code>target\` and from \`\`list</code> to <code>str</code>\. <code>targets</code> added as alias and code to ensure existing list in playbooks is translated as a string\.
* purefb\_syslog \- Enable <code>services</code> parameter and also the ability update existing syslog servers from REST 2\.14

<a id="telekom-mms-icinga-director-4"></a>
#### telekom\_mms\.icinga\_director

* Add vars parameter to user\_template and user modules \([https\://github\.com/telekom\-mms/ansible\-collection\-icinga\-director/pull/262](https\://github\.com/telekom\-mms/ansible\-collection\-icinga\-director/pull/262)\)

<a id="theforeman-foreman"></a>
#### theforeman\.foreman

* content\_export\_\* \- document that <code>chunk\_size\_gb</code> parameter is only applicable for <code>importable</code> exports \([https\://github\.com/theforeman/foreman\-ansible\-modules/issues/1738](https\://github\.com/theforeman/foreman\-ansible\-modules/issues/1738)\)
* lifecycle\_environments role \- allow setting <code>state</code> for the LCE\, allowing deletion of existing ones
* location\, locations role \- add <code>description</code> parameter to set the description
* redhat\_manifest \- report <code>changed</code> when manifest is regenerated and downloaded \([https\://github\.com/theforeman/foreman\-ansible\-modules/issues/1473](https\://github\.com/theforeman/foreman\-ansible\-modules/issues/1473)\)

<a id="vmware-vmware-rest-5"></a>
#### vmware\.vmware\_rest

* add a new ci job to the collection to run integration tests on bm vmware env
* cluster\_moid \- Fix bug where lookup would return incosistent results for objects in nested paths\. Fixes issues [https\://github\.com/ansible\-collections/vmware\.vmware\_rest/issues/500](https\://github\.com/ansible\-collections/vmware\.vmware\_rest/issues/500) [https\://github\.com/ansible\-collections/vmware\.vmware\_rest/pull/445](https\://github\.com/ansible\-collections/vmware\.vmware\_rest/pull/445) [https\://github\.com/ansible\-collections/vmware\.vmware\_rest/issues/324](https\://github\.com/ansible\-collections/vmware\.vmware\_rest/issues/324) \([https\://github\.com/ansible\-collections/vmware\.vmware\_rest/pull/523](https\://github\.com/ansible\-collections/vmware\.vmware\_rest/pull/523)\)
* cluster\_moid \- updated documentation around lookup plugin usage
* datacenter\_moid \- Fix bug where lookup would return incosistent results for objects in nested paths Fixes issues [https\://github\.com/ansible\-collections/vmware\.vmware\_rest/issues/500](https\://github\.com/ansible\-collections/vmware\.vmware\_rest/issues/500) [https\://github\.com/ansible\-collections/vmware\.vmware\_rest/pull/445](https\://github\.com/ansible\-collections/vmware\.vmware\_rest/pull/445) [https\://github\.com/ansible\-collections/vmware\.vmware\_rest/issues/324](https\://github\.com/ansible\-collections/vmware\.vmware\_rest/issues/324) \([https\://github\.com/ansible\-collections/vmware\.vmware\_rest/pull/523](https\://github\.com/ansible\-collections/vmware\.vmware\_rest/pull/523)\)
* datacenter\_moid \- updated documentation around lookup plugin usage
* datastore\_moid \- Fix bug where lookup would return incosistent results for objects in nested paths Fixes issues [https\://github\.com/ansible\-collections/vmware\.vmware\_rest/issues/500](https\://github\.com/ansible\-collections/vmware\.vmware\_rest/issues/500) [https\://github\.com/ansible\-collections/vmware\.vmware\_rest/pull/445](https\://github\.com/ansible\-collections/vmware\.vmware\_rest/pull/445) [https\://github\.com/ansible\-collections/vmware\.vmware\_rest/issues/324](https\://github\.com/ansible\-collections/vmware\.vmware\_rest/issues/324) \([https\://github\.com/ansible\-collections/vmware\.vmware\_rest/pull/523](https\://github\.com/ansible\-collections/vmware\.vmware\_rest/pull/523)\)
* datastore\_moid \- updated documentation around lookup plugin usage
* folder\_moid \- Fix bug where lookup would return incosistent results for objects in nested paths Fixes issues [https\://github\.com/ansible\-collections/vmware\.vmware\_rest/issues/500](https\://github\.com/ansible\-collections/vmware\.vmware\_rest/issues/500) [https\://github\.com/ansible\-collections/vmware\.vmware\_rest/pull/445](https\://github\.com/ansible\-collections/vmware\.vmware\_rest/pull/445) [https\://github\.com/ansible\-collections/vmware\.vmware\_rest/issues/324](https\://github\.com/ansible\-collections/vmware\.vmware\_rest/issues/324) \([https\://github\.com/ansible\-collections/vmware\.vmware\_rest/pull/523](https\://github\.com/ansible\-collections/vmware\.vmware\_rest/pull/523)\)
* folder\_moid \- updated documentation around lookup plugin usage
* host\_moid \- Fix bug where lookup would return incosistent results for objects in nested paths Fixes issues [https\://github\.com/ansible\-collections/vmware\.vmware\_rest/issues/500](https\://github\.com/ansible\-collections/vmware\.vmware\_rest/issues/500) [https\://github\.com/ansible\-collections/vmware\.vmware\_rest/pull/445](https\://github\.com/ansible\-collections/vmware\.vmware\_rest/pull/445) [https\://github\.com/ansible\-collections/vmware\.vmware\_rest/issues/324](https\://github\.com/ansible\-collections/vmware\.vmware\_rest/issues/324) \([https\://github\.com/ansible\-collections/vmware\.vmware\_rest/pull/523](https\://github\.com/ansible\-collections/vmware\.vmware\_rest/pull/523)\)
* host\_moid \- updated documentation around lookup plugin usage
* network\_moid \- Fix bug where lookup would return incosistent results for objects in nested paths Fixes issues [https\://github\.com/ansible\-collections/vmware\.vmware\_rest/issues/500](https\://github\.com/ansible\-collections/vmware\.vmware\_rest/issues/500) [https\://github\.com/ansible\-collections/vmware\.vmware\_rest/pull/445](https\://github\.com/ansible\-collections/vmware\.vmware\_rest/pull/445) [https\://github\.com/ansible\-collections/vmware\.vmware\_rest/issues/324](https\://github\.com/ansible\-collections/vmware\.vmware\_rest/issues/324) \([https\://github\.com/ansible\-collections/vmware\.vmware\_rest/pull/523](https\://github\.com/ansible\-collections/vmware\.vmware\_rest/pull/523)\)
* network\_moid \- updated documentation around lookup plugin usage
* resource\_pool\_moid \- Fix bug where lookup would return incosistent results for objects in nested paths Fixes issues [https\://github\.com/ansible\-collections/vmware\.vmware\_rest/issues/500](https\://github\.com/ansible\-collections/vmware\.vmware\_rest/issues/500) [https\://github\.com/ansible\-collections/vmware\.vmware\_rest/pull/445](https\://github\.com/ansible\-collections/vmware\.vmware\_rest/pull/445) [https\://github\.com/ansible\-collections/vmware\.vmware\_rest/issues/324](https\://github\.com/ansible\-collections/vmware\.vmware\_rest/issues/324) \([https\://github\.com/ansible\-collections/vmware\.vmware\_rest/pull/523](https\://github\.com/ansible\-collections/vmware\.vmware\_rest/pull/523)\)
* resource\_pool\_moid \- updated documentation around lookup plugin usage
* vcenter\_vm\_guest\_customization \- Added better examples that cover more use\-cases \([https\://github\.com/ansible\-collections/vmware\.vmware\_rest/pull/534](https\://github\.com/ansible\-collections/vmware\.vmware\_rest/pull/534)\)\.
* vm\_moid \- Fix bug where lookup would return incosistent results for objects in nested paths Fixes issues [https\://github\.com/ansible\-collections/vmware\.vmware\_rest/issues/500](https\://github\.com/ansible\-collections/vmware\.vmware\_rest/issues/500) [https\://github\.com/ansible\-collections/vmware\.vmware\_rest/pull/445](https\://github\.com/ansible\-collections/vmware\.vmware\_rest/pull/445) [https\://github\.com/ansible\-collections/vmware\.vmware\_rest/issues/324](https\://github\.com/ansible\-collections/vmware\.vmware\_rest/issues/324) \([https\://github\.com/ansible\-collections/vmware\.vmware\_rest/pull/523](https\://github\.com/ansible\-collections/vmware\.vmware\_rest/pull/523)\)
* vm\_moid \- updated documentation around lookup plugin usage

<a id="vultr-cloud"></a>
#### vultr\.cloud

* instance\, bare\_metal \- Implemented a new option <code>skip\_wait</code> \([https\://github\.com/vultr/ansible\-collection\-vultr/issues/119](https\://github\.com/vultr/ansible\-collection\-vultr/issues/119)\)\.

<a id="vyos-vyos-1"></a>
#### vyos\.vyos

* All GHA workflows have been updated to use ones from ansible\-content\-actions\.
* Passes latest ansible\-lint with production profile\.
* Removes deprecation notice for vyos\.vyos\.
* Uncaps supported ansible\-core versions\, this collection now supports ansible\-core\>\=2\.15\.

<a id="breaking-changes--porting-guide-1"></a>
### Breaking Changes / Porting Guide

<a id="ansible-core-19"></a>
#### Ansible\-core

* Stopped wrapping all commands sent over SSH on a Windows target with a <code>powershell\.exe</code> executable\. This results in one less process being started on each command for Windows to improve efficiency\, simplify the code\, and make <code>raw</code> an actual raw command run with the default shell configured on the Windows sshd settings\. This should have no affect on most tasks except for <code>raw</code> which now is not guaranteed to always be running in a PowerShell shell and from having the console output codepage set to UTF\-8\. To avoid this issue either swap to using <code>ansible\.windows\.win\_command</code>\, <code>ansible\.windows\.win\_shell</code>\, <code>ansible\.windows\.win\_powershell</code> or manually wrap the raw command with the shell commands needed to set the output console encoding\.
* persistent connection plugins \- The <code>ANSIBLE\_CONNECTION\_PATH</code> config option no longer has any effect\.

<a id="amazon-aws-15"></a>
#### amazon\.aws

* The amazon\.aws collection has dropped support for <code>botocore\<1\.31\.0</code> and <code>boto3\<1\.28\.0</code>\. Most modules will continue to work with older versions of the AWS SDK\.  However\, compatability with older versions of the SDK is not guaranteed and will not be tested\. When using older versions of the SDK a warning will be emitted by Ansible \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2161](https\://github\.com/ansible\-collections/amazon\.aws/pull/2161)\)\.
* aws\_ec2 \- the parameter <code>include\_extra\_api\_calls</code> was previously deprecated and has been removed \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2320](https\://github\.com/ansible\-collections/amazon\.aws/pull/2320)\)\.
* iam\_policy \- the <code>policies</code> return key was previously deprecated and has been removed\, please use <code>policy\_names</code> instead \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2320](https\://github\.com/ansible\-collections/amazon\.aws/pull/2320)\)\.
* module\_utils\.botocore \- <code>boto3\_conn</code>\'s  <code>conn\_type</code> parameter is now mandatory \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2157](https\://github\.com/ansible\-collections/amazon\.aws/pull/2157)\)\.

<a id="cloud-common-2"></a>
#### cloud\.common

* cloud\.common collection \- Support for ansible\-core \< 2\.15 has been dropped \([https\://github\.com/ansible\-collections/cloud\.common/pull/145/files](https\://github\.com/ansible\-collections/cloud\.common/pull/145/files)\)\.

<a id="community-aws-5"></a>
#### community\.aws

* The community\.aws collection has dropped support for <code>botocore\<1\.31\.0</code> and <code>boto3\<1\.28\.0</code>\. Most modules will continue to work with older versions of the AWS SDK\.  However\, compatability with older versions of the SDK is not guaranteed and will not be tested\. When using older versions of the SDK a warning will be emitted by Ansible \([https\://github\.com/ansible\-collections/community\.aws/pull/2195](https\://github\.com/ansible\-collections/community\.aws/pull/2195)\)\.
* autoscaling\_instance\_refresh \- The module has been migrated from the <code>community\.aws</code> collection\. Playbooks using the Fully Qualified Collection Name for this module should be updated to use <code>amazon\.aws\.autoscaling\_instance\_refresh</code> \([https\://github\.com/ansible\-collections/community\.aws/pull/2177](https\://github\.com/ansible\-collections/community\.aws/pull/2177)\)\.
* autoscaling\_instance\_refresh\_info \- The module has been migrated from the <code>community\.aws</code> collection\. Playbooks using the Fully Qualified Collection Name for this module should be updated to use <code>amazon\.aws\.autoscaling\_instance\_refresh\_info</code> \([https\://github\.com/ansible\-collections/community\.aws/pull/2177](https\://github\.com/ansible\-collections/community\.aws/pull/2177)\)\.
* ec2\_launch\_template \- Tags defined using option <code>tags</code> are now applied to the launch template resources not the resource created using this launch template \([https\://github\.com/ansible\-collections/community\.aws/issues/176](https\://github\.com/ansible\-collections/community\.aws/issues/176)\)\.
* ec2\_launch\_template \- The module has been migrated from the <code>community\.aws</code> collection\. Playbooks using the Fully Qualified Collection Name for this module should be updated to use <code>amazon\.aws\.ec2\_launch\_template</code> \([https\://github\.com/ansible\-collections/community\.aws/pull/2185](https\://github\.com/ansible\-collections/community\.aws/pull/2185)\)\.
* ec2\_placement\_group \- The module has been migrated from the <code>community\.aws</code> collection\. Playbooks using the Fully Qualified Collection Name for this module should be updated to use <code>amazon\.aws\.ec2\_placement\_group</code>\.
* ec2\_placement\_group\_info \- The module has been migrated from the <code>community\.aws</code> collection\. Playbooks using the Fully Qualified Collection Name for this module should be updated to use <code>amazon\.aws\.ec2\_placement\_group\_info</code>\.
* ec2\_transit\_gateway \- The module has been migrated from the <code>community\.aws</code> collection\. Playbooks using the Fully Qualified Collection Name for this module should be updated to use <code>amazon\.aws\.ec2\_transit\_gateway</code>\.
* ec2\_transit\_gateway\_info \- The module has been migrated from the <code>community\.aws</code> collection\. Playbooks using the Fully Qualified Collection Name for this module should be updated to use <code>amazon\.aws\.ec2\_transit\_gateway\_info</code>\.
* ec2\_transit\_gateway\_vpc\_attachment \- The module has been migrated from the <code>community\.aws</code> collection\. Playbooks using the Fully Qualified Collection Name for this module should be updated to use <code>amazon\.aws\.ec2\_transit\_gateway\_vpc\_attachment</code>\.
* ec2\_transit\_gateway\_vpc\_attachment\_info \- The module has been migrated from the <code>community\.aws</code> collection\. Playbooks using the Fully Qualified Collection Name for this module should be updated to use <code>amazon\.aws\.ec2\_transit\_gateway\_vpc\_attachment\_info</code>\.
* ec2\_vpc\_egress\_igw \- The module has been migrated from the <code>community\.aws</code> collection\. Playbooks using the Fully Qualified Collection Name for this module should be updated to use <code>amazon\.aws\.ec2\_vpc\_egress\_igw</code> \([https\://api\.github\.com/repos/ansible\-collections/community\.aws/pulls/2169](https\://api\.github\.com/repos/ansible\-collections/community\.aws/pulls/2169)\)\.
* ec2\_vpc\_nacl \- The module has been migrated from the <code>community\.aws</code> collection\. Playbooks using the Fully Qualified Collection Name for this module should be updated to use <code>amazon\.aws\.ec2\_vpc\_nacl</code> \([https\://github\.com/ansible\-collections/community\.aws/pull/2178](https\://github\.com/ansible\-collections/community\.aws/pull/2178)\)\.
* ec2\_vpc\_nacl\_info \- The module has been migrated from the <code>community\.aws</code> collection\. Playbooks using the Fully Qualified Collection Name for this module should be updated to use <code>amazon\.aws\.ec2\_vpc\_nacl\_info</code> \([https\://github\.com/ansible\-collections/community\.aws/pull/2178](https\://github\.com/ansible\-collections/community\.aws/pull/2178)\)\.
* ec2\_vpc\_peer \- The module has been migrated from the <code>community\.aws</code> collection\. Playbooks using the Fully Qualified Collection Name for this module should be updated to use <code>amazon\.aws\.ec2\_vpc\_peer</code>\.
* ec2\_vpc\_peering\_info \- The module has been migrated from the <code>community\.aws</code> collection\. Playbooks using the Fully Qualified Collection Name for this module should be updated to use <code>amazon\.aws\.ec2\_vpc\_peering\_info</code>\.
* ec2\_vpc\_vgw \- The module has been migrated from the <code>community\.aws</code> collection\. Playbooks using the Fully Qualified Collection Name for this module should be updated to use <code>amazon\.aws\.ec2\_vpc\_vgw</code>\.
* ec2\_vpc\_vgw\_info \- The module has been migrated from the <code>community\.aws</code> collection\. Playbooks using the Fully Qualified Collection Name for this module should be updated to use <code>amazon\.aws\.ec2\_vpc\_vgw\_info</code>\.
* ec2\_vpc\_vpn \- The module has been migrated from the <code>community\.aws</code> collection\. Playbooks using the Fully Qualified Collection Name for this module should be updated to use <code>amazon\.aws\.ec2\_vpc\_vpn</code>\.
* ec2\_vpc\_vpn\_info \- The module has been migrated from the <code>community\.aws</code> collection\. Playbooks using the Fully Qualified Collection Name for this module should be updated to use <code>amazon\.aws\.ec2\_vpc\_vpn\_info</code>\.
* ecs\_cluster \- the parameter <code>purge\_capacity\_providers</code> defaults to true\. \([https\://github\.com/ansible\-collections/community\.aws/pull/2165](https\://github\.com/ansible\-collections/community\.aws/pull/2165)\)\.
* elb\_classic\_lb\_info \- The module has been migrated from the <code>community\.aws</code> collection\. Playbooks using the Fully Qualified Collection Name for this module should be updated to use <code>amazon\.aws\.elb\_classic\_lb\_info</code>\.
* iam\_policy \- the <code>connection\_properties</code> return key was previously deprecated and has been removed\, please use <code>raw\_connection\_properties</code> instead \([https\://github\.com/ansible\-collections/community\.aws/pull/2165](https\://github\.com/ansible\-collections/community\.aws/pull/2165)\)\.

<a id="community-docker-11"></a>
#### community\.docker

* docker\_container \- the default of <code>image\_name\_mismatch</code> changed from <code>ignore</code> to <code>recreate</code> \([https\://github\.com/ansible\-collections/community\.docker/pull/971](https\://github\.com/ansible\-collections/community\.docker/pull/971)\)\.

<a id="community-general-28"></a>
#### community\.general

* The collection no longer supports ansible\-core 2\.13 and ansible\-core 2\.14\. While most \(or even all\) modules and plugins might still work with these versions\, they are no longer tested in CI and breakages regarding them will not be fixed \([https\://github\.com/ansible\-collections/community\.general/pull/8921](https\://github\.com/ansible\-collections/community\.general/pull/8921)\)\.
* cmd\_runner module utils \- CLI arguments created directly from module parameters are no longer assigned a default formatter \([https\://github\.com/ansible\-collections/community\.general/pull/8928](https\://github\.com/ansible\-collections/community\.general/pull/8928)\)\.
* irc \- the defaults of <code>use\_tls</code> and <code>validate\_certs</code> changed from <code>false</code> to <code>true</code> \([https\://github\.com/ansible\-collections/community\.general/pull/8918](https\://github\.com/ansible\-collections/community\.general/pull/8918)\)\.
* rhsm\_repository \- the states <code>present</code> and <code>absent</code> have been removed\. Use <code>enabled</code> and <code>disabled</code> instead \([https\://github\.com/ansible\-collections/community\.general/pull/8918](https\://github\.com/ansible\-collections/community\.general/pull/8918)\)\.

<a id="community-routeros-9"></a>
#### community\.routeros

* command \- the module no longer declares that it supports check mode \([https\://github\.com/ansible\-collections/community\.routeros/pull/318](https\://github\.com/ansible\-collections/community\.routeros/pull/318)\)\.

<a id="community-vmware-20"></a>
#### community\.vmware

* Adding a dependency on the <code>vmware\.vmware</code> collection \([https\://github\.com/ansible\-collections/community\.vmware/pull/2159](https\://github\.com/ansible\-collections/community\.vmware/pull/2159)\)\.
* Depending on <code>vmware\-vcenter</code> and <code>vmware\-vapi\-common\-client</code> instead of <code>https\://github\.com/vmware/vsphere\-automation\-sdk\-python\.git</code> \([https\://github\.com/ansible\-collections/community\.vmware/pull/2163](https\://github\.com/ansible\-collections/community\.vmware/pull/2163)\)\.
* Dropping support for pyVmomi \< 8\.0\.3\.0\.1 \([https\://github\.com/ansible\-collections/community\.vmware/pull/2163](https\://github\.com/ansible\-collections/community\.vmware/pull/2163)\)\.
* Module utils \- Removed <code>vmware\.run\_command\_in\_guest\(\)</code> \([https\://github\.com/ansible\-collections/community\.vmware/pull/2175](https\://github\.com/ansible\-collections/community\.vmware/pull/2175)\)\.
* Removed support for ansible\-core version \< 2\.17\.0\.
* vmware\_dvs\_portgroup \- Removed <code>security\_override</code> alias for <code>mac\_management\_override</code> and support for <code>securityPolicyOverrideAllowed</code> which has been deprected in the vSphere API \([https\://github\.com/ansible\-collections/community\.vmware/issues/1998](https\://github\.com/ansible\-collections/community\.vmware/issues/1998)\)\.
* vmware\_dvs\_portgroup\_info \- Removed <code>security\_override</code> because it\'s deprecated in the vSphere API \([https\://github\.com/ansible\-collections/community\.vmware/issues/1998](https\://github\.com/ansible\-collections/community\.vmware/issues/1998)\)\.
* vmware\_guest\_tools\_info \- Removed deprecated <code>vm\_tools\_install\_status</code> from the result \([https\://github\.com/ansible\-collections/community\.vmware/issues/2078](https\://github\.com/ansible\-collections/community\.vmware/issues/2078)\)\.

<a id="community-zabbix-7"></a>
#### community\.zabbix

* All Roles \- Remove support for Centos 7
* All Roles \- Remove support for Python2
* All Roles \- Removed support for Debian 10\.
* All Roles \- Removed support for Ubuntu 18\.08 \(Bionic\)
* Remove support for Ansible \< 2\.15 and Python \< 3\.9
* Remove support for Zabbix 6\.2
* Removed support for Zabbix 6\.2
* zabbix\_agent role \- Remove support for <em class="title-reference">zabbix\_agent\_zabbix\_alias</em>\.
* zabbix\_agent role \- Remove support for <em class="title-reference">zabbix\_get\_package</em> variable\.
* zabbix\_agent role \- Remove support for <em class="title-reference">zabbix\_sender\_package</em> variable\.
* zabbix\_agent role \- Remove support for all <em class="title-reference">zabbix\_agent2\_\*</em> variables\.

<a id="hetzner-hcloud-3"></a>
#### hetzner\.hcloud

* Drop support for ansible\-core 2\.14\.

<a id="kubernetes-core-7"></a>
#### kubernetes\.core

* Remove support for <code>ansible\-core\<2\.15</code> \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/737](https\://github\.com/ansible\-collections/kubernetes\.core/pull/737)\)\.

<a id="vmware-vmware-rest-6"></a>
#### vmware\.vmware\_rest

* Removing any support for ansible\-core \<\=2\.14

<a id="deprecated-features-7"></a>
### Deprecated Features

* The <code>community\.network</code> collection has been deprecated\.
  It will be removed from Ansible 12 if no one starts maintaining it again before Ansible 12\.
  See [Collections Removal Process for unmaintained collections](https\://docs\.ansible\.com/ansible/devel/community/collection\_contributors/collection\_package\_removal\.html\#unmaintained\-collections) for more details \([https\://forum\.ansible\.com/t/8030](https\://forum\.ansible\.com/t/8030)\)\.
* The google\.cloud collection will be removed from Ansible 12 due to violations of the Ansible inclusion requirements\.
  The collection has [unresolved sanity test failures](https\://github\.com/ansible\-collections/google\.cloud/issues/613)\.
  See [Collections Removal Process for collections not satisfying the collection requirements](https\://docs\.ansible\.com/ansible/devel/community/collection\_contributors/collection\_package\_removal\.html\#collections\-not\-satisfying\-the\-collection\-requirements) for more details\, including for how this can be cancelled \([https\://forum\.ansible\.com/t/8609](https\://forum\.ansible\.com/t/8609)\)\.
  After removal\, users can still install this collection with <code>ansible\-galaxy collection install google\.cloud</code>\.
* The sensu\.sensu\_go collection will be removed from Ansible 12 due to violations of the Ansible inclusion requirements\.
  The collection has [unresolved sanity test failures](https\://github\.com/sensu/sensu\-go\-ansible/issues/362)\.
  See [Collections Removal Process for collections not satisfying the collection requirements](https\://docs\.ansible\.com/ansible/devel/community/collection\_contributors/collection\_package\_removal\.html\#collections\-not\-satisfying\-the\-collection\-requirements) for more details\, including for how this can be cancelled \([https\://forum\.ansible\.com/t/8380](https\://forum\.ansible\.com/t/8380)\)\.
  After removal\, users can still install this collection with <code>ansible\-galaxy collection install sensu\.sensu\_go</code>\.

<a id="ansible-core-20"></a>
#### Ansible\-core

* Deprecate <code>ansible\.module\_utils\.basic\.AnsibleModule\.safe\_eval</code> and <code>ansible\.module\_utils\.common\.safe\_eval</code> as they are no longer used\.
* persistent connection plugins \- The <code>ANSIBLE\_CONNECTION\_PATH</code> config option no longer has any effect\, and will be removed in a future release\.
* yum\_repository \- deprecate <code>async</code> option as it has been removed in RHEL 8 and will be removed in ansible\-core 2\.22\.
* yum\_repository \- the following options are deprecated\: <code>deltarpm\_metadata\_percentage</code>\, <code>gpgcakey</code>\, <code>http\_caching</code>\, <code>keepalive</code>\, <code>metadata\_expire\_filter</code>\, <code>mirrorlist\_expire</code>\, <code>protect</code>\, <code>ssl\_check\_cert\_permissions</code>\, <code>ui\_repoid\_vars</code> as they have no effect for dnf as an underlying package manager\. The options will be removed in ansible\-core 2\.22\.

<a id="amazon-aws-16"></a>
#### amazon\.aws

* amazon\.aws collection \- due to the AWS SDKs announcing the end of support for Python less than 3\.8 \([https\://aws\.amazon\.com/blogs/developer/python\-support\-policy\-updates\-for\-aws\-sdks\-and\-tools/](https\://aws\.amazon\.com/blogs/developer/python\-support\-policy\-updates\-for\-aws\-sdks\-and\-tools/)\) support for Python less than 3\.8 by this collection has been deprecated and will removed in release 10\.0\.0 \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2161](https\://github\.com/ansible\-collections/amazon\.aws/pull/2161)\)\.
* ec2\_vpc\_peer \- the <code>ec2\_vpc\_peer</code> module has been renamed to <code>ec2\_vpc\_peering</code>\. The usage of the module has not changed\. The ec2\_vpc\_peer alias will be removed in version 13\.0\.0 \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2356](https\://github\.com/ansible\-collections/amazon\.aws/pull/2356)\)\.
* ec2\_vpc\_peering\_info \- <code>result</code> return key has been deprecated and will be removed in release 11\.0\.0\.  Use the <code>vpc\_peering\_connections</code> return key instead \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2359](https\://github\.com/ansible\-collections/amazon\.aws/pull/2359)\)\.
* iam\_role \- support for creating and deleting IAM instance profiles using the <code>create\_instance\_profile</code> and <code>delete\_instance\_profile</code> options has been deprecated and will be removed in a release after 2026\-05\-01\.  To manage IAM instance profiles the <code>amazon\.aws\.iam\_instance\_profile</code> module can be used instead \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2221](https\://github\.com/ansible\-collections/amazon\.aws/pull/2221)\)\.
* s3\_object \- Support for <code>mode\=list</code> has been deprecated\.  <code>amazon\.aws\.s3\_object\_info</code> should be used instead \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2328](https\://github\.com/ansible\-collections/amazon\.aws/pull/2328)\)\.

<a id="cisco-ios-10"></a>
#### cisco\.ios

* ios\_bgp\_address\_family \- deprecated attribute password in favour of password\_options within neigbhors\.
* ios\_bgp\_global \- deprecated attributes aggregate\_address\, bestpath\, inject\_map\, ipv4\_with\_subnet\, ipv6\_with\_subnet\, nopeerup\_delay\, distribute\_list\, address\, tag\, ipv6\_addresses\, password\, route\_map\, route\_server\_context and scope
* ios\_linkagg \- deprecate legacy module ios\_linkagg
* ios\_lldp \- deprecate legacy module ios\_lldp

<a id="community-aws-6"></a>
#### community\.aws

* community\.aws collection \- due to the AWS SDKs announcing the end of support for Python less than 3\.8 \([https\://aws\.amazon\.com/blogs/developer/python\-support\-policy\-updates\-for\-aws\-sdks\-and\-tools/](https\://aws\.amazon\.com/blogs/developer/python\-support\-policy\-updates\-for\-aws\-sdks\-and\-tools/)\) support for Python less than 3\.8 by this collection has been deprecated and will removed in release 10\.0\.0 \([https\://github\.com/ansible\-collections/community\.aws/pull/2195](https\://github\.com/ansible\-collections/community\.aws/pull/2195)\)\.

<a id="community-docker-12"></a>
#### community\.docker

* The collection deprecates support for all ansible\-core versions that are currently End of Life\, [according to the ansible\-core support matrix](https\://docs\.ansible\.com/ansible\-core/devel/reference\_appendices/release\_and\_maintenance\.html\#ansible\-core\-support\-matrix)\. This means that the next major release of the collection will no longer support ansible\-core 2\.11\, ansible\-core 2\.12\, ansible\-core 2\.13\, and ansible\-core 2\.14\.

<a id="community-general-29"></a>
#### community\.general

* CmdRunner module util \- setting the value of the <code>ignore\_none</code> parameter within a <code>CmdRunner</code> context is deprecated and that feature should be removed in community\.general 12\.0\.0 \([https\://github\.com/ansible\-collections/community\.general/pull/8479](https\://github\.com/ansible\-collections/community\.general/pull/8479)\)\.
* MH decorator cause\_changes module utils \- deprecate parameters <code>on\_success</code> and <code>on\_failure</code> \([https\://github\.com/ansible\-collections/community\.general/pull/8791](https\://github\.com/ansible\-collections/community\.general/pull/8791)\)\.
* git\_config \- the <code>list\_all</code> option has been deprecated and will be removed in community\.general 11\.0\.0\. Use the <code>community\.general\.git\_config\_info</code> module instead \([https\://github\.com/ansible\-collections/community\.general/pull/8453](https\://github\.com/ansible\-collections/community\.general/pull/8453)\)\.
* git\_config \- using <code>state\=present</code> without providing <code>value</code> is deprecated and will be disallowed in community\.general 11\.0\.0\. Use the <code>community\.general\.git\_config\_info</code> module instead to read a value \([https\://github\.com/ansible\-collections/community\.general/pull/8453](https\://github\.com/ansible\-collections/community\.general/pull/8453)\)\.
* hipchat \- the hipchat service has been discontinued and the self\-hosted variant has been End of Life since 2020\. The module is therefore deprecated and will be removed from community\.general 11\.0\.0 if nobody provides compelling reasons to still keep it \([https\://github\.com/ansible\-collections/community\.general/pull/8919](https\://github\.com/ansible\-collections/community\.general/pull/8919)\)\.
* pipx \- support for versions of the command line tool <code>pipx</code> older than <code>1\.7\.0</code> is deprecated and will be removed in community\.general 11\.0\.0 \([https\://github\.com/ansible\-collections/community\.general/pull/8793](https\://github\.com/ansible\-collections/community\.general/pull/8793)\)\.
* pipx\_info \- support for versions of the command line tool <code>pipx</code> older than <code>1\.7\.0</code> is deprecated and will be removed in community\.general 11\.0\.0 \([https\://github\.com/ansible\-collections/community\.general/pull/8793](https\://github\.com/ansible\-collections/community\.general/pull/8793)\)\.

<a id="community-grafana-3"></a>
#### community\.grafana

* Deprecate <em class="title-reference">grafana\_notification\_channel</em>\. It will be removed in version 3\.0\.0

<a id="community-mysql-8"></a>
#### community\.mysql

* collection \- support of mysqlclient connector is deprecated \- use PyMySQL connector instead\! We will stop testing against it in collection version 4\.0\.0 and remove the related code in 5\.0\.0 \([https\://github\.com/ansible\-collections/community\.mysql/issues/654](https\://github\.com/ansible\-collections/community\.mysql/issues/654)\)\.
* mysql\_info \- The <code>users\_info</code> filter returned variable <code>plugin\_auth\_string</code> contains the hashed password and it\'s misleading\, it will be removed from community\.mysql 4\.0\.0\. Use the <em class="title-reference">plugin\_hash\_string</em> return value instead \([https\://github\.com/ansible\-collections/community\.mysql/pull/629](https\://github\.com/ansible\-collections/community\.mysql/pull/629)\)\.
* mysql\_user \- the <code>user</code> alias of the <code>name</code> argument has been deprecated and will be removed in collection version 5\.0\.0\. Use the <code>name</code> argument instead\.

<a id="community-network"></a>
#### community\.network

* This collection and all content in it is unmaintained and deprecated \([https\://forum\.ansible\.com/t/8030](https\://forum\.ansible\.com/t/8030)\)\. If you are interested in maintaining parts of the collection\, please copy them to your own repository\, and tell others about in the Forum discussion\. See the [collection creator path](https\://docs\.ansible\.com/ansible/devel/dev\_guide/developing\_collections\_path\.html) for details\.

<a id="community-routeros-10"></a>
#### community\.routeros

* The collection deprecates support for all Ansible/ansible\-base/ansible\-core versions that are currently End of Life\, [according to the ansible\-core support matrix](https\://docs\.ansible\.com/ansible\-core/devel/reference\_appendices/release\_and\_maintenance\.html\#ansible\-core\-support\-matrix)\. This means that the next major release of the collection will no longer support Ansible 2\.9\, ansible\-base 2\.10\, ansible\-core 2\.11\, ansible\-core 2\.12\, ansible\-core 2\.13\, and ansible\-core 2\.14\.

<a id="community-sops-5"></a>
#### community\.sops

* The collection deprecates support for all Ansible/ansible\-base/ansible\-core versions that are currently End of Life\, [according to the ansible\-core support matrix](https\://docs\.ansible\.com/ansible\-core/devel/reference\_appendices/release\_and\_maintenance\.html\#ansible\-core\-support\-matrix)\. This means that the next major release of the collection will no longer support Ansible 2\.9\, ansible\-base 2\.10\, ansible\-core 2\.11\, ansible\-core 2\.12\, ansible\-core 2\.13\, and ansible\-core 2\.14\.

<a id="community-vmware-21"></a>
#### community\.vmware

* vmware\_cluster \- the module has been deprecated and will be removed in community\.vmware 6\.0\.0 \([https\://github\.com/ansible\-collections/community\.vmware/pull/2143](https\://github\.com/ansible\-collections/community\.vmware/pull/2143)\)\.
* vmware\_cluster\_dpm \- the module has been deprecated and will be removed in community\.vmware 6\.0\.0 \([https\://github\.com/ansible\-collections/community\.vmware/pull/2217](https\://github\.com/ansible\-collections/community\.vmware/pull/2217)\)\.
* vmware\_cluster\_drs \- the module has been deprecated and will be removed in community\.vmware 6\.0\.0 \([https\://github\.com/ansible\-collections/community\.vmware/pull/2136](https\://github\.com/ansible\-collections/community\.vmware/pull/2136)\)\.
* vmware\_cluster\_drs\_recommendations \- the module has been deprecated and will be removed in community\.vmware 6\.0\.0 \([https\://github\.com/ansible\-collections/community\.vmware/pull/2218](https\://github\.com/ansible\-collections/community\.vmware/pull/2218)\)\.
* vmware\_cluster\_vcls \- the module has been deprecated and will be removed in community\.vmware 6\.0\.0 \([https\://github\.com/ansible\-collections/community\.vmware/pull/2156](https\://github\.com/ansible\-collections/community\.vmware/pull/2156)\)\.

<a id="removed-features-previously-deprecated"></a>
### Removed Features \(previously deprecated\)

* The <code>inspur\.sm</code> collection was considered unmaintained and has been removed from Ansible 11 \([https\://forum\.ansible\.com/t/2854](https\://forum\.ansible\.com/t/2854)\)\.
  Users can still install this collection with <code>ansible\-galaxy collection install inspur\.sm</code>\.
* The collection <code>t\_systems\_mms\.icinga\_director</code> has been completely removed from Ansible\.
  It has been renamed to <code>telekom\_mms\.icinga\_director</code>\.
  <code>t\_systems\_mms\.icinga\_director</code> has been replaced by deprecated redirects to <code>telekom\_mms\.icinga\_director</code> in Ansible 9\.0\.0\.
  Please update your FQCNs from <code>t\_systems\_mms\.icinga\_director</code> to <code>telekom\_mms\.icinga\_director</code>\.
* The deprecated <code>frr\.frr</code> collection has been removed \([https\://forum\.ansible\.com/t/6243](https\://forum\.ansible\.com/t/6243)\)\.
* The deprecated <code>ngine\_io\.exoscale</code> collection has been removed \([https\://forum\.ansible\.com/t/2572](https\://forum\.ansible\.com/t/2572)\)\.
* The deprecated <code>openvswitch\.openvswitch</code> collection has been removed \([https\://forum\.ansible\.com/t/6245](https\://forum\.ansible\.com/t/6245)\)\.

<a id="ansible-core-21"></a>
#### Ansible\-core

* Play \- removed deprecated <code>ROLE\_CACHE</code> property in favor of <code>role\_cache</code>\.
* Remove deprecated <em class="title-reference">VariableManager\.\_get\_delegated\_vars</em> method \([https\://github\.com/ansible/ansible/issues/82950](https\://github\.com/ansible/ansible/issues/82950)\)
* Removed Python 3\.10 as a supported version on the controller\. Python 3\.11 or newer is required\.
* Removed support for setting the <code>vars</code> keyword to lists of dictionaries\. It is now required to be a single dictionary\.
* loader \- remove deprecated non\-inclusive words \([https\://github\.com/ansible/ansible/issues/82947](https\://github\.com/ansible/ansible/issues/82947)\)\.
* paramiko\_ssh \- removed deprecated ssh\_args from the paramiko\_ssh connection plugin \([https\://github\.com/ansible/ansible/issues/82939](https\://github\.com/ansible/ansible/issues/82939)\)\.
* paramiko\_ssh \- removed deprecated ssh\_common\_args from the paramiko\_ssh connection plugin \([https\://github\.com/ansible/ansible/issues/82940](https\://github\.com/ansible/ansible/issues/82940)\)\.
* paramiko\_ssh \- removed deprecated ssh\_extra\_args from the paramiko\_ssh connection plugin \([https\://github\.com/ansible/ansible/issues/82941](https\://github\.com/ansible/ansible/issues/82941)\)\.
* play\_context \- remove deprecated PlayContext\.verbosity property \([https\://github\.com/ansible/ansible/issues/82945](https\://github\.com/ansible/ansible/issues/82945)\)\.
* utils/listify \- remove deprecated \'loader\' argument from listify\_lookup\_plugin\_terms API \([https\://github\.com/ansible/ansible/issues/82949](https\://github\.com/ansible/ansible/issues/82949)\)\.

<a id="community-docker-13"></a>
#### community\.docker

* The collection no longer supports ansible\-core 2\.11\, 2\.12\, 2\.13\, and 2\.14\. You need ansible\-core 2\.15\.0 or newer to use community\.docker 4\.x\.y \([https\://github\.com/ansible\-collections/community\.docker/pull/971](https\://github\.com/ansible\-collections/community\.docker/pull/971)\)\.
* The docker\_compose module has been removed\. Please migrate to community\.docker\.docker\_compose\_v2 \([https\://github\.com/ansible\-collections/community\.docker/pull/971](https\://github\.com/ansible\-collections/community\.docker/pull/971)\)\.
* docker\_container \- the <code>ignore\_image</code> option has been removed\. Use <code>image\: ignore</code> in <code>comparisons</code> instead \([https\://github\.com/ansible\-collections/community\.docker/pull/971](https\://github\.com/ansible\-collections/community\.docker/pull/971)\)\.
* docker\_container \- the <code>purge\_networks</code> option has been removed\. Use <code>networks\: strict</code> in <code>comparisons</code> instead and make sure that <code>networks</code> is specified \([https\://github\.com/ansible\-collections/community\.docker/pull/971](https\://github\.com/ansible\-collections/community\.docker/pull/971)\)\.
* various modules and plugins \- remove the <code>ssl\_version</code> option \([https\://github\.com/ansible\-collections/community\.docker/pull/971](https\://github\.com/ansible\-collections/community\.docker/pull/971)\)\.

<a id="community-general-30"></a>
#### community\.general

* The consul\_acl module has been removed\. Use community\.general\.consul\_token and/or community\.general\.consul\_policy instead \([https\://github\.com/ansible\-collections/community\.general/pull/8921](https\://github\.com/ansible\-collections/community\.general/pull/8921)\)\.
* The hipchat callback plugin has been removed\. The hipchat service has been discontinued and the self\-hosted variant has been End of Life since 2020 \([https\://github\.com/ansible\-collections/community\.general/pull/8921](https\://github\.com/ansible\-collections/community\.general/pull/8921)\)\.
* The redhat module utils has been removed \([https\://github\.com/ansible\-collections/community\.general/pull/8921](https\://github\.com/ansible\-collections/community\.general/pull/8921)\)\.
* The rhn\_channel module has been removed \([https\://github\.com/ansible\-collections/community\.general/pull/8921](https\://github\.com/ansible\-collections/community\.general/pull/8921)\)\.
* The rhn\_register module has been removed \([https\://github\.com/ansible\-collections/community\.general/pull/8921](https\://github\.com/ansible\-collections/community\.general/pull/8921)\)\.
* consul \- removed the <code>ack\_params\_state\_absent</code> option\. It had no effect anymore \([https\://github\.com/ansible\-collections/community\.general/pull/8918](https\://github\.com/ansible\-collections/community\.general/pull/8918)\)\.
* ejabberd\_user \- removed the <code>logging</code> option \([https\://github\.com/ansible\-collections/community\.general/pull/8918](https\://github\.com/ansible\-collections/community\.general/pull/8918)\)\.
* gitlab modules \- remove basic auth feature \([https\://github\.com/ansible\-collections/community\.general/pull/8405](https\://github\.com/ansible\-collections/community\.general/pull/8405)\)\.
* proxmox\_kvm \- removed the <code>proxmox\_default\_behavior</code> option\. Explicitly specify the old default values if you were using <code>proxmox\_default\_behavior\=compatibility</code>\, otherwise simply remove it \([https\://github\.com/ansible\-collections/community\.general/pull/8918](https\://github\.com/ansible\-collections/community\.general/pull/8918)\)\.
* redhat\_subscriptions \- removed the <code>pool</code> option\. Use <code>pool\_ids</code> instead \([https\://github\.com/ansible\-collections/community\.general/pull/8918](https\://github\.com/ansible\-collections/community\.general/pull/8918)\)\.

<a id="community-grafana-4"></a>
#### community\.grafana

* removed check and handling of mangled api key in <em class="title-reference">grafana\_dashboard</em> lookup
* removed deprecated <em class="title-reference">message</em> argument in <em class="title-reference">grafana\_dashboard</em>

<a id="community-okd-2"></a>
#### community\.okd

* k8s \- Support for <code>merge\_type\=json</code> has been removed in version 4\.0\.0\. Please use <code>kubernetes\.core\.k8s\_json\_patch</code> instead \([https\://github\.com/openshift/community\.okd/pull/226](https\://github\.com/openshift/community\.okd/pull/226)\)\.

<a id="community-routeros-11"></a>
#### community\.routeros

* The collection no longer supports Ansible 2\.9\, ansible\-base 2\.10\, ansible\-core 2\.11\, ansible\-core 2\.12\, ansible\-core 2\.13\, and ansible\-core 2\.14\. If you need to continue using End of Life versions of Ansible/ansible\-base/ansible\-core\, please use community\.routeros 2\.x\.y \([https\://github\.com/ansible\-collections/community\.routeros/pull/318](https\://github\.com/ansible\-collections/community\.routeros/pull/318)\)\.

<a id="community-sops-6"></a>
#### community\.sops

* The collection no longer supports Ansible 2\.9\, ansible\-base 2\.10\, ansible\-core 2\.11\, ansible\-core 2\.12\, ansible\-core 2\.13\, and ansible\-core 2\.14\. If you need to continue using End of Life versions of Ansible/ansible\-base/ansible\-core\, please use community\.sops 1\.x\.y \([https\://github\.com/ansible\-collections/community\.sops/pull/206](https\://github\.com/ansible\-collections/community\.sops/pull/206)\)\.

<a id="kubernetes-core-8"></a>
#### kubernetes\.core

* k8s \- Support for <code>merge\_type\=json</code> has been removed in version 4\.0\.0\. Please use <code>kubernetes\.core\.k8s\_json\_patch</code> instead \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/722](https\://github\.com/ansible\-collections/kubernetes\.core/pull/722)\)\.
* k8s\_exec \- the previously deprecated <code>result\.return\_code</code> return value has been removed\, consider using <code>result\.rc</code> instead \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/726](https\://github\.com/ansible\-collections/kubernetes\.core/pull/726)\)\.
* module\_utils/common\.py \- the previously deprecated <code>K8sAnsibleMixin</code> class has been removed \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/726](https\://github\.com/ansible\-collections/kubernetes\.core/pull/726)\)\.
* module\_utils/common\.py \- the previously deprecated <code>configuration\_digest\(\)</code> function has been removed \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/726](https\://github\.com/ansible\-collections/kubernetes\.core/pull/726)\)\.
* module\_utils/common\.py \- the previously deprecated <code>get\_api\_client\(\)</code> function has been removed \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/726](https\://github\.com/ansible\-collections/kubernetes\.core/pull/726)\)\.
* module\_utils/common\.py \- the previously deprecated <code>unique\_string\(\)</code> function has been removed \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/726](https\://github\.com/ansible\-collections/kubernetes\.core/pull/726)\)\.

<a id="security-fixes-2"></a>
### Security Fixes

<a id="ansible-core-22"></a>
#### Ansible\-core

* include\_vars action \- Ensure that result masking is correctly requested when vault\-encrypted files are read\. \(CVE\-2024\-8775\)
* task result processing \- Ensure that action\-sourced result masking \(<code>\_ansible\_no\_log\=True</code>\) is preserved\. \(CVE\-2024\-8775\)
* user action won\'t allow ssh\-keygen\, chown and chmod to run on existing ssh public key file\, avoiding traversal on existing symlinks \(CVE\-2024\-9902\)\.

<a id="bugfixes-7"></a>
### Bugfixes

<a id="ansible-core-23"></a>
#### Ansible\-core

* \-\> runas become \- Generate new token for the SYSTEM token to use for become\. This should result in the full SYSTEM token being used and problems starting the process that fails with <code>The process creation has been blocked</code>\.
* Add a version ceiling constraint for pypsrp to avoid potential breaking changes in the 1\.0\.0 release\.
* Add descriptions for <code>ansible\-galaxy install \-\-help\` and \`\`ansible\-galaxy role\|collection install \-\-help</code>\.
* Avoid truncating floats when casting into int\, as it can lead to truncation and unexpected results\. 0\.99999 will be 0\, not 1\.
* COLOR\_SKIP will not alter \"included\" events color display anymore\.
* Callbacks now correctly get the resolved connection plugin name as the connection used\.
* Darwin \- add unit tests for Darwin hardware fact gathering\.
* Errors now preserve stacked error messages even when YAML is involved\.
* Fix <code>SemanticVersion\.parse\(\)</code> to store the version string so that <code>\_\_repr\_\_</code> reports it instead of <code>None</code> \([https\://github\.com/ansible/ansible/pull/83831](https\://github\.com/ansible/ansible/pull/83831)\)\.
* Fix a traceback when an environment variable contains certain special characters \([https\://github\.com/ansible/ansible/issues/83498](https\://github\.com/ansible/ansible/issues/83498)\)
* Fix an issue when setting a plugin name from an unsafe source resulted in <code>ValueError\: unmarshallable object</code> \([https\://github\.com/ansible/ansible/issues/82708](https\://github\.com/ansible/ansible/issues/82708)\)
* Fix an issue where registered variable was not available for templating in <code>loop\_control\.label</code> on skipped looped tasks \([https\://github\.com/ansible/ansible/issues/83619](https\://github\.com/ansible/ansible/issues/83619)\)
* Fix disabling SSL verification when installing collections and roles from git repositories\. If <code>\-\-ignore\-certs</code> isn\'t provided\, the value for the <code>GALAXY\_IGNORE\_CERTS</code> configuration option will be used \([https\://github\.com/ansible/ansible/issues/83326](https\://github\.com/ansible/ansible/issues/83326)\)\.
* Fix for <code>meta</code> tasks breaking host/fork affinity with <code>host\_pinned</code> strategy \([https\://github\.com/ansible/ansible/issues/83294](https\://github\.com/ansible/ansible/issues/83294)\)
* Fix handlers not being executed in lockstep using the linear strategy in some cases \([https\://github\.com/ansible/ansible/issues/82307](https\://github\.com/ansible/ansible/issues/82307)\)
* Fix rapid memory usage growth when notifying handlers using the <code>listen</code> keyword \([https\://github\.com/ansible/ansible/issues/83392](https\://github\.com/ansible/ansible/issues/83392)\)
* Fix the task attribute <code>resolved\_action</code> to show the FQCN instead of <code>None</code> when <code>action</code> or <code>local\_action</code> is used in the playbook\.
* Fix using <code>module\_defaults</code> with <code>local\_action</code>/<code>action</code> \([https\://github\.com/ansible/ansible/issues/81905](https\://github\.com/ansible/ansible/issues/81905)\)\.
* Fix using the current task\'s directory for looking up relative paths within roles \([https\://github\.com/ansible/ansible/issues/82695](https\://github\.com/ansible/ansible/issues/82695)\)\.
* Improve performance on large inventories by reducing the number of implicit meta tasks\.
* Remove deprecated config options DEFAULT\_FACT\_PATH\, DEFAULT\_GATHER\_SUBSET\, and DEFAULT\_GATHER\_TIMEOUT in favor of setting <code>fact\_path</code>\, <code>gather\_subset</code> and <code>gather\_timeout</code> as <code>module\_defaults</code> for <code>ansible\.builtin\.setup</code>\.
  These will apply to both the <code>gather\_facts</code> play keyword\, and any <code>ansible\.builtin\.setup</code> tasks\.
  To configure these options only for the <code>gather\_facts</code> keyword\, set these options as play keywords also\.
* Set LANGUAGE environment variable is set to a non\-English locale \([https\://github\.com/ansible/ansible/issues/83608](https\://github\.com/ansible/ansible/issues/83608)\)\.
* Use the requested error message in the ansible\.module\_utils\.facts\.timeout timeout function instead of hardcoding one\.
* <code>ansible\-galaxy install \-\-help</code> \- Fix the usage text and document that the requirements file passed to <code>\-r</code> can include collections and roles\.
* <code>ansible\-galaxy role install</code> \- update the default timeout to download archive URLs from 20 seconds to 60 \([https\://github\.com/ansible/ansible/issues/83521](https\://github\.com/ansible/ansible/issues/83521)\)\.
* <code>end\_host</code> \- fix incorrect return code when executing <code>end\_host</code> in the <code>rescue</code> section \([https\://github\.com/ansible/ansible/issues/83447](https\://github\.com/ansible/ansible/issues/83447)\)
* <code>package</code>/<code>dnf</code> action plugins \- provide the reason behind the failure to gather the <code>ansible\_pkg\_mgr</code> fact to identify the package backend
* addressed issue of trailing text been ignored\, non\-ASCII characters are parsed\, enhance white space handling and fixed overly permissive issue of human\_to\_bytes filter\([https\://github\.com/ansible/ansible/issues/82075](https\://github\.com/ansible/ansible/issues/82075)\)
* ansible\-config will now properly template defaults before dumping them\.
* ansible\-doc \- fixed \"inicates\" typo in output
* ansible\-doc \- format top\-level descriptions with multiple paragraphs as multiple paragraphs\, instead of concatenating them \([https\://github\.com/ansible/ansible/pull/83155](https\://github\.com/ansible/ansible/pull/83155)\)\.
* ansible\-doc \- handle no\_fail condition for role\.
* ansible\-doc \- make colors configurable\.
* ansible\-galaxy collection install \- remove old installation info when installing collections \([https\://github\.com/ansible/ansible/issues/83182](https\://github\.com/ansible/ansible/issues/83182)\)\.
* ansible\-galaxy role install \- fix symlinks \([https\://github\.com/ansible/ansible/issues/82702](https\://github\.com/ansible/ansible/issues/82702)\, [https\://github\.com/ansible/ansible/issues/81965](https\://github\.com/ansible/ansible/issues/81965)\)\.
* ansible\-test \- Enable the <code>sys\.unraisablehook</code> work\-around for the <code>pylint</code> sanity test on Python 3\.11\. Previously the work\-around was only enabled for Python 3\.12 and later\. However\, the same issue has been discovered on Python 3\.11\.
* ansible\-test \- The <code>pylint</code> sanity test now includes the controller/target context of files when grouping them\. This allows the <code>\-\-py\-version</code> option to be passed to <code>pylint</code> to indicate the minimum supported Python version for each test context\, preventing <code>pylint</code> from defaulting to the Python version used to invoke the test\.
* ansible\-test action\-plugin\-docs \- Fix to check for sidecar documentation for action plugins
* ansible\_managed restored it\'s \'templatability\' by ensuring the possible injection routes are cut off earlier in the process\.
* apt \- report changed\=True when some packages are being removed \([https\://github\.com/ansible/ansible/issues/46314](https\://github\.com/ansible/ansible/issues/46314)\)\.
* apt\_\* \- add more info messages raised while updating apt cache \([https\://github\.com/ansible/ansible/issues/77941](https\://github\.com/ansible/ansible/issues/77941)\)\.
* assemble \- update argument\_spec with \'decrypt\' option which is required by action plugin \([https\://github\.com/ansible/ansible/issues/80840](https\://github\.com/ansible/ansible/issues/80840)\)\.
* atomic\_move \- fix using the setgid bit on the parent directory when creating files \([https\://github\.com/ansible/ansible/issues/46742](https\://github\.com/ansible/ansible/issues/46742)\, [https\://github\.com/ansible/ansible/issues/67177](https\://github\.com/ansible/ansible/issues/67177)\)\.
* config\, restored the ability to set module compression via a variable
* connection plugins using the \'extras\' option feature would need variables to match the plugin\'s loaded name\, sometimes requiring fqcn\, which is not the same as the documented/declared/expected variables\. Now we fall back to the \'basename\' of the fqcn\, but plugin authors can still set the expected value directly\.
* copy \- mtime/atime not updated\. Fix now update mtime/atime\([https\://github\.com/ansible/ansible/issues/83013](https\://github\.com/ansible/ansible/issues/83013)\)
* csvfile lookup \- give an error when no search term is provided using modern config syntax \([https\://github\.com/ansible/ansible/issues/83689](https\://github\.com/ansible/ansible/issues/83689)\)\.
* debconf \- fix normalization of value representation for boolean vtypes in new packages \([https\://github\.com/ansible/ansible/issues/83594](https\://github\.com/ansible/ansible/issues/83594)\)
* debconf \- set empty password values \([https\://github\.com/ansible/ansible/issues/83214](https\://github\.com/ansible/ansible/issues/83214)\)\.
* delay keyword is now a float\, matching the underlying \'time\' API and user expectations\.
* display \- warn user about empty log filepath \([https\://github\.com/ansible/ansible/issues/79959](https\://github\.com/ansible/ansible/issues/79959)\)\.
* display now does a better job of mapping warnings/errors to the proper log severity when using ansible\.log\. We still use color as a fallback mapping \(now prioritiezed by severity\) but mostly rely on it beind directly set by warnning/errors calls\.
* distro package \- update the distro package version from 1\.8\.0 to 1\.9\.0  \([https\://github\.com/ansible/ansible/issues/82935](https\://github\.com/ansible/ansible/issues/82935)\)
* dnf \- Ensure that we are handling DownloadError properly in the dnf module
* dnf \- Substitute variables in DNF cache path \([https\://github\.com/ansible/ansible/pull/80094](https\://github\.com/ansible/ansible/pull/80094)\)\.
* dnf \- fix an issue where two packages of the same <code>evr</code> but different arch failed to install \([https\://github\.com/ansible/ansible/issues/83406](https\://github\.com/ansible/ansible/issues/83406)\)
* dnf \- honor installroot for <code>cachedir</code>\, <code>logdir</code> and <code>persistdir</code>
* dnf \- perform variable substitutions in <code>logdir</code> and <code>persistdir</code>
* dnf\, dnf5 \- fix for installing a set of packages by specifying them using a wildcard character \([https\://github\.com/ansible/ansible/issues/83373](https\://github\.com/ansible/ansible/issues/83373)\)
* dnf5 \- fix traceback when <code>enable\_plugins</code>/<code>disable\_plugins</code> is used on <code>python3\-libdnf5</code> versions that do not support this functionality
* dnf5 \- re\-introduce the <code>state\: installed</code> alias to <code>state\: present</code> \([https\://github\.com/ansible/ansible/issues/83960](https\://github\.com/ansible/ansible/issues/83960)\)
* dnf5 \- replace removed API calls
* ensure we have logger before we log when we have increased verbosity\.
* facts \- <em class="title-reference">support\_discard</em> now returns <em class="title-reference">0</em> if either <em class="title-reference">discard\_granularity</em> or <em class="title-reference">discard\_max\_hw\_bytes</em> is zero\; otherwise it returns the value of <em class="title-reference">discard\_granularity</em>\, as before \([https\://github\.com/ansible/ansible/pull/83480](https\://github\.com/ansible/ansible/pull/83480)\)\.
* facts \- add a generic detection for VMware in product name\.
* facts \- add facts about x86\_64 flags to detect microarchitecture \([https\://github\.com/ansible/ansible/issues/83331](https\://github\.com/ansible/ansible/issues/83331)\)\.
* facts \- skip if distribution file path is directory\, instead of raising error \([https\://github\.com/ansible/ansible/issues/84006](https\://github\.com/ansible/ansible/issues/84006)\)\.
* fetch \- add error message when using <code>dest</code> with a trailing slash that becomes a local directory \- [https\://github\.com/ansible/ansible/issues/82878](https\://github\.com/ansible/ansible/issues/82878)
* file \- retrieve the link\'s full path when hard linking a soft link with follow \([https\://github\.com/ansible/ansible/issues/33911](https\://github\.com/ansible/ansible/issues/33911)\)\.
* fixed the issue of creating user directory using tilde\(\~\) always reported \"changed\"\.\([https\://github\.com/ansible/ansible/issues/82490](https\://github\.com/ansible/ansible/issues/82490)\)
* fixed unit test test\_borken\_cowsay to address mock not been properly applied when existing unix system already have cowsay installed\.
* freebsd \- refactor dmidecode fact gathering code for simplicity\.
* freebsd \- update disk and slices regex for fact gathering \([https\://github\.com/ansible/ansible/pull/82081](https\://github\.com/ansible/ansible/pull/82081)\)\.
* get\_url \- Verify checksum using tmpsrc\, not dest \([https\://github\.com/ansible/ansible/pull/64092](https\://github\.com/ansible/ansible/pull/64092)\)
* git \- check if git version is available or not before using it for comparison \([https\://github\.com/ansible/ansible/issues/72321](https\://github\.com/ansible/ansible/issues/72321)\)\.
* include\_tasks \- Display location when attempting to load a task list where <code>include\_\*</code> did not specify any value \- [https\://github\.com/ansible/ansible/issues/83874](https\://github\.com/ansible/ansible/issues/83874)
* known\_hosts \- the returned module invocation now accurately reflects the module arguments\.
* linear strategy now provides a properly templated task name to the v2\_runner\_on\_started callback event\.
* linear strategy\: fix handlers included via <code>include\_tasks</code> handler to be executed in lockstep \([https\://github\.com/ansible/ansible/issues/83019](https\://github\.com/ansible/ansible/issues/83019)\)
* linux \- remove extraneous get\_bin\_path API call\.
* local \- handle error while parsing values in ini files \([https\://github\.com/ansible/ansible/issues/82717](https\://github\.com/ansible/ansible/issues/82717)\)\.
* lookup \- Fixed examples of csv lookup plugin \([https\://github\.com/ansible/ansible/issues/83031](https\://github\.com/ansible/ansible/issues/83031)\)\.
* module\_defaults \- do not display action/module deprecation warnings when using an action\_group that contains a deprecated plugin \([https\://github\.com/ansible/ansible/issues/83490](https\://github\.com/ansible/ansible/issues/83490)\)\.
* module\_utils atomic\_move \(used by most file based modules\)\, now correctly handles permission copy and setting mtime correctly across all paths
* package\_facts \- apk fix when cache is empty \([https\://github\.com/ansible/ansible/issues/83126](https\://github\.com/ansible/ansible/issues/83126)\)\.
* package\_facts \- no longer fails silently when the selected package manager is unable to list packages\.
* package\_facts \- returns the correct warning when package listing fails\.
* persistent connection plugins \- The correct Ansible persistent connection helper is now always used\. Previously\, the wrong script could be used\, depending on the value of the <code>PATH</code> environment variable\. As a result\, users were sometimes required to set <code>ANSIBLE\_CONNECTION\_PATH</code> to use the correct script\.
* powershell \- Implement more robust deletion mechanism for C\# code compilation temporary files\. This should avoid scenarios where the underlying temporary directory may be temporarily locked by antivirus tools or other IO problems\. A failure to delete one of these temporary directories will result in a warning rather than an outright failure\.
* powershell \- Improve CLIXML decoding to decode all control characters and unicode characters that are encoded as surrogate pairs\.
* psrp \- Fix bug when attempting to fetch a file path that contains special glob characters like <code>\[\]</code>
* replace \- Updated before/after example \([https\://github\.com/ansible/ansible/issues/83390](https\://github\.com/ansible/ansible/issues/83390)\)\.
* runtime\-metadata sanity test \- do not crash on deprecations if <code>galaxy\.yml</code> contains an empty <code>version</code> field \([https\://github\.com/ansible/ansible/pull/83831](https\://github\.com/ansible/ansible/pull/83831)\)\.
* service \- fix order of CLI arguments on FreeBSD \([https\://github\.com/ansible/ansible/pull/81377](https\://github\.com/ansible/ansible/pull/81377)\)\.
* service\_facts \- don\'t crash if OpenBSD rcctl variable contains \'\=\' character \([https\://github\.com/ansible/ansible/issues/83457](https\://github\.com/ansible/ansible/issues/83457)\)
* service\_facts will now detect failed services more accurately across systemd implementations\.
* setup module \(fact gathering\)\, added fallbcak code path to handle mount fact gathering in linux when threading is not available
* setup/gather\_facts will skip missing <code>sysctl</code> instead of being a fatal error \([https\://github\.com/ansible/ansible/pull/81297](https\://github\.com/ansible/ansible/pull/81297)\)\.
* shell plugin \- properly quote all needed components of shell commands \([https\://github\.com/ansible/ansible/issues/82535](https\://github\.com/ansible/ansible/issues/82535)\)
* ssh \- Fix bug when attempting to fetch a file path with characters that should be quoted when using the <code>piped</code> transfer method
* support the countme option when using yum\_repository
* systemd \- extend systemctl is\-enabled check to handle \"enabled\-runtime\" \([https\://github\.com/ansible/ansible/pull/77754](https\://github\.com/ansible/ansible/pull/77754)\)\.
* systemd facts \- handle AttributeError raised while gathering facts on non\-systemd hosts\.
* systemd\_service \- handle mask operation failure \([https\://github\.com/ansible/ansible/issues/81649](https\://github\.com/ansible/ansible/issues/81649)\)\.
* templating hostvars under native jinja will not cause serialization errors anymore\.
* the raw arguments error now just displays the short names of modules instead of every possible variation
* unarchive \- Better handling of files with an invalid timestamp in zip file \([https\://github\.com/ansible/ansible/issues/81092](https\://github\.com/ansible/ansible/issues/81092)\)\.
* unarchive \- trigger change when size and content differ when other properties are unchanged \([https\://github\.com/ansible/ansible/pull/83454](https\://github\.com/ansible/ansible/pull/83454)\)\.
* unsafe data \- Address an incompatibility when iterating or getting a single index from <code>AnsibleUnsafeBytes</code>
* unsafe data \- Address an incompatibility with <code>AnsibleUnsafeText</code> and <code>AnsibleUnsafeBytes</code> when pickling with <code>protocol\=0</code>
* unsafe data \- Enable directly using <code>AnsibleUnsafeText</code> with Python <code>pathlib</code> \([https\://github\.com/ansible/ansible/issues/82414](https\://github\.com/ansible/ansible/issues/82414)\)
* uri \- deprecate \'yes\' and \'no\' value for \'follow\_redirects\' parameter\.
* user action will now require O\(force\) to overwrite the public part of an ssh key when generating ssh keys\, as was already the case for the private part\.
* user module now avoids changing ownership of files symlinked in provided home dir skeleton
* vault \- handle vault password file value when it is directory \([https\://github\.com/ansible/ansible/issues/42960](https\://github\.com/ansible/ansible/issues/42960)\)\.
* vault\.is\_encrypted\_file is now optimized to be called in runtime and not for being called in tests
* vault\_encrypted test documentation\, name and examples have been fixed\, other parts were clarified
* winrm \- Add retry after exceeding commands per user quota that can occur in loops and action plugins running multiple commands\.

<a id="amazon-aws-17"></a>
#### amazon\.aws

* aws\_ec2 \- fix SSM inventory collection for multiple \(\>40\) hosts  \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2227](https\://github\.com/ansible\-collections/amazon\.aws/pull/2227)\)\.
* backup\_plan\_info \- Bugfix to enable getting info of all backup plans \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2083](https\://github\.com/ansible\-collections/amazon\.aws/pull/2083)\)\.
* cloudformation \- Fix bug where termination protection is not updated when create\_changeset\=true is used for stack updates \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2391](https\://github\.com/ansible\-collections/amazon\.aws/pull/2391)\)\.
* cloudwatch\_metric\_alarm \- Fix idempotency when creating cloudwatch metric alarm without dimensions \([https\://github\.com/ansible\-collections/amazon\.aws/pull/1865](https\://github\.com/ansible\-collections/amazon\.aws/pull/1865)\)\.
* ec2\_instance \- Fix issue where EC2 instance module failed to apply security groups when both <code>network</code> and <code>vpc\_subnet\_id</code> were specified\, caused by passing <code>None</code> to discover\_security\_groups\(\) \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2488](https\://github\.com/ansible\-collections/amazon\.aws/pull/2488)\)\.
* ec2\_instance \- do not ignore IPv6 addresses when a single network interface is specified \([https\://github\.com/ansible\-collections/amazon\.aws/pull/1979](https\://github\.com/ansible\-collections/amazon\.aws/pull/1979)\)\.
* ec2\_instance \- fix state processing when exact\_count is used \([https\://github\.com/ansible\-collections/amazon\.aws/pull/1659](https\://github\.com/ansible\-collections/amazon\.aws/pull/1659)\)\.
* ec2\_security\_group \- Fix the diff mode issue when creating a security group containing a rule with a managed prefix list \([https\://github\.com/ansible\-collections/amazon\.aws/issues/2373](https\://github\.com/ansible\-collections/amazon\.aws/issues/2373)\)\.
* ec2\_vol \- output volume informations when volume exists in check mode \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2133](https\://github\.com/ansible\-collections/amazon\.aws/pull/2133)\)\.
* ec2\_vpc\_net \- handle ipv6\_cidr <code>false</code> and no Ipv6CidrBlockAssociationSet in vpc \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2374](https\://github\.com/ansible\-collections/amazon\.aws/pull/2374)\)\.
* iam\_role \- fixes <code>EntityAlreadyExists</code> exception when <code>create\_instance\_profile</code> was set to <code>false</code> and the instance profile already existed \([https\://github\.com/ansible\-collections/amazon\.aws/issues/2102](https\://github\.com/ansible\-collections/amazon\.aws/issues/2102)\)\.
* iam\_role \- fixes issue where IAM instance profiles were created when <code>create\_instance\_profile</code> was set to <code>false</code> \([https\://github\.com/ansible\-collections/amazon\.aws/issues/2281](https\://github\.com/ansible\-collections/amazon\.aws/issues/2281)\)\.
* lambda \- Remove non UTF\-8 data \(contents of Lambda ZIP file\) from the module output to avoid Ansible error \([https\://github\.com/ansible\-collections/amazon\.aws/issues/2386](https\://github\.com/ansible\-collections/amazon\.aws/issues/2386)\)\.
* rds\_cluster \- Fix issue occurring when updating RDS cluster domain \([https\://github\.com/ansible\-collections/amazon\.aws/issues/2390](https\://github\.com/ansible\-collections/amazon\.aws/issues/2390)\)\.
* rds\_cluster \- Limit params sent to api call to DBClusterIdentifier when using state started or stopped \([https\://github\.com/ansible\-collections/amazon\.aws/issues/2197](https\://github\.com/ansible\-collections/amazon\.aws/issues/2197)\)\.
* route53 \- modify the return value to return diff only when <code>module\.\_diff</code> is set to true \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2136](https\://github\.com/ansible\-collections/amazon\.aws/pull/2136)\)\.
* s3\_bucket \- Do not use default region as location constraint when creating bucket on ceph cluster \([https\://github\.com/ansible\-collections/amazon\.aws/issues/2420](https\://github\.com/ansible\-collections/amazon\.aws/issues/2420)\)\.
* s3\_bucket \- Fixes Python 3\.7 compilation issue due to addition of typing information \([https\://github\.com/ansible\-collections/amazon\.aws/issues/2287](https\://github\.com/ansible\-collections/amazon\.aws/issues/2287)\)\.
* s3\_bucket \- catch <code>UnsupportedArgument</code> when calling API <code>GetBucketAccelerationConfig</code> on region where it is not supported \([https\://github\.com/ansible\-collections/amazon\.aws/issues/2180](https\://github\.com/ansible\-collections/amazon\.aws/issues/2180)\)\.
* s3\_bucket \- change the default behaviour of the new <code>accelerate\_enabled</code> option to only update the configuration if explicitly passed \([https\://github\.com/ansible\-collections/amazon\.aws/issues/2220](https\://github\.com/ansible\-collections/amazon\.aws/issues/2220)\)\.
* s3\_bucket \- fixes <code>MethodNotAllowed</code> exceptions caused by fetching transfer acceleration state in regions that don\'t support it \([https\://github\.com/ansible\-collections/amazon\.aws/issues/2266](https\://github\.com/ansible\-collections/amazon\.aws/issues/2266)\)\.
* s3\_bucket \- fixes <code>TypeError\: cannot unpack non\-iterable NoneType object</code> errors related to bucket versioning\, policies\, tags or encryption \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2228](https\://github\.com/ansible\-collections/amazon\.aws/pull/2228)\)\.
* s3\_object \- Fixed an issue where <code>max\_keys</code> was not respected \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2328](https\://github\.com/ansible\-collections/amazon\.aws/pull/2328)\)\.
* s3\_object \- fixed issue which was causing <code>MemoryError</code> exceptions when downloading large files \([https\://github\.com/ansible\-collections/amazon\.aws/issues/2107](https\://github\.com/ansible\-collections/amazon\.aws/issues/2107)\)\.

<a id="ansible-netcommon-5"></a>
#### ansible\.netcommon

* Fix get api call during scp with libssh\.
* Handle sftp error messages for file not present for routerOS\.
* The v6\.1\.2 release introduced a change in cliconfbase\'s edit\_config\(\) signature which broke many platform cliconfs\. This patch release reverts that change\.
* Updated the error message for the content\_templates parser to include the correct parser name and detailed error information\.

<a id="ansible-posix-2"></a>
#### ansible\.posix

* Bugfix in the documentation regarding the path option for authorised\_key\([https\://github\.com/ansible\-collections/ansible\.posix/issues/483](https\://github\.com/ansible\-collections/ansible\.posix/issues/483)\)\.
* acl \- Fixed to set ACLs on paths mounted with NFS version 4 correctly \([https\://github\.com/ansible\-collections/ansible\.posix/issues/240](https\://github\.com/ansible\-collections/ansible\.posix/issues/240)\)\.
* backport \- Drop ansible\-core 2\.14 and set 2\.15 minimum version \([https\://github\.com/ansible\-collections/ansible\.posix/issues/578](https\://github\.com/ansible\-collections/ansible\.posix/issues/578)\)\.
* mount \- Handle <code>boot</code> option on Linux\, NetBSD and OpenBSD correctly \([https\://github\.com/ansible\-collections/ansible\.posix/issues/364](https\://github\.com/ansible\-collections/ansible\.posix/issues/364)\)\.
* seboolean \- make it work with disabled SELinux
* skippy \- Revert removal of skippy plugin\. It will be removed in version 2\.0\.0 \([https\://github\.com/ansible\-collections/ansible\.posix/issues/573](https\://github\.com/ansible\-collections/ansible\.posix/issues/573)\)\.
* synchronize \- maintain proper formatting of the remote paths \([https\://github\.com/ansible\-collections/ansible\.posix/pull/361](https\://github\.com/ansible\-collections/ansible\.posix/pull/361)\)\.
* sysctl \- fix sysctl to work properly on symlinks \([https\://github\.com/ansible\-collections/ansible\.posix/issues/111](https\://github\.com/ansible\-collections/ansible\.posix/issues/111)\)\.

<a id="ansible-utils-2"></a>
#### ansible\.utils

* keep\_keys \- Fixes issue where all keys are removed when data is passed in as a dict\.
* keep\_keys \- Fixes keep\_keys filter to retain the entire node when a key match occurs\, rather than just the leaf node values\.

<a id="ansible-windows-6"></a>
#### ansible\.windows

* setup \- Better handle orphaned users when attempting to retrieve <code>ansible\_machine\_id</code> \- [https\://github\.com/ansible\-collections/ansible\.windows/issues/606](https\://github\.com/ansible\-collections/ansible\.windows/issues/606)
* setup \- Provide WMI/CIM fallback for facts that rely on SMBIOS when that is unavailable
* win\_owner \- Try to enable extra privileges if available to set the owner even when the caller may not have explicit rights to do so normally \- [https\://github\.com/ansible\-collections/ansible\.windows/issues/633](https\://github\.com/ansible\-collections/ansible\.windows/issues/633)
* win\_powershell \- Fix up depth handling on <code>\$Ansible\.Result</code> when using a custom <code>executable</code> \- [https\://github\.com/ansible\-collections/ansible\.windows/issues/642](https\://github\.com/ansible\-collections/ansible\.windows/issues/642)
* win\_powershell \- increase open timeout for <code>executable</code> parameter to prevent exceptions on first\-run or slower targets\. \([https\://github\.com/ansible\-collections/ansible\.windows/issues/644](https\://github\.com/ansible\-collections/ansible\.windows/issues/644)\)\.
* win\_updates \- Base64 encode the update wrapper and payload to prevent locale\-specific encoding issues\.
* win\_updates \- Handle race condition when <code>Wait\-Process</code> did not handle when the process had ended \- [https\://github\.com/ansible\-collections/ansible\.windows/issues/623](https\://github\.com/ansible\-collections/ansible\.windows/issues/623)

<a id="arista-eos-3"></a>
#### arista\.eos

* Adds a missing word in the \'bgp client\-to\-client reflection\' command in eos\_bgp\_global module\.
* Ensure IPv6 static route definitions are correctly filtered during facts gathering\.
* Fixes a typo in always\-compare\-med attribute in eos\_bgp\_global module\.
* Handles exception when translating an unknown port to its service name\.
* This fix make sure to fetch timer with <em class="title-reference">lldp</em> string at the start\.
* Update integration tests for parse operations to ensure that ordering or address family \(AF\) does not affect assertions\.
* Update the filter to accurately retrieve relevant static route configurations\.

<a id="check-point-mgmt-4"></a>
#### check\_point\.mgmt

* module\_utils/checkpoint\.py \- Remove usage of CertificateError causing failures in ansible\-core 2\.17\.

<a id="chocolatey-chocolatey-1"></a>
#### chocolatey\.chocolatey

* win\_chocolatey \- task crashes if PATH contains multiple choco\.exe on the target machine

<a id="cisco-aci-3"></a>
#### cisco\.aci

* Remove duplicate alias name for attribute epg in aci\_epg\_subnet module

<a id="cisco-ios-11"></a>
#### cisco\.ios

* bgp\_global \- fix ebgp\_multihop recognnition and hop\_count settings
* ios\_acls \- fix incorrect mapping of port 135/udp to msrpc\.
* ios\_bgp\_address\_family \- Add support for maximum\-paths configuration\.
* ios\_bgp\_address\_family \- Add support for maximum\-secondary\-paths configuration\.
* ios\_bgp\_address\_family \- fix parsing of password\_options while gathering password configuration from appliance\.
* ios\_bgp\_global \- fix parsing of password\_options while gathering password configuration from appliance\.
* ios\_interfaces \- Fixes rendering of FiftyGigabitEthernet as it was wrongly rendering FiftyGigabitEthernet as FiveGigabitEthernet\.
* ios\_l3\_interfaces \- Fix gathering wrong facts for source interface in ipv4\.
* ios\_service \- Add tcp\_small\_servers and udp\_small\_servers attributes\, to generate configuration\.
* ios\_service \- Fix a typo causing log timestamps not being configurable
* ios\_service \- Fix timestamps attribute\, to generate right configuration\.
* ios\_snmp\_server \- Fixes an issue where enabling the read\-only \(ro\) attribute in communities was not idempotent\.
* ios\_static\_routes \- Fix gathering facts by properly distinguising routes\.
* ios\_static\_routes \- Fix processing of metric\_distance as it was wrongly populated under the forward\_router\_address attribute\.
* ios\_vlans \- Make the module fail when vlan name is longer than 32 characters with configuration as VTPv1 and VTPv2\.
* l2\_interfaces \- If a large number of VLANs are affected\, the configuration will now be correctly split into several commands\.
* snmp\_server \- Fix configuration command for snmp\-server host\.
* snmp\_server \- Fix wrong syntax of snmp\-server host command generation\.
* static\_routes \- add TenGigabitEthernet as valid interface

<a id="cisco-iosxr-5"></a>
#### cisco\.iosxr

* iosxr\_acls\_facts \- Fix incorrect rendering of some acl facts causing errors\.
* iosxr\_static\_routes \- Fix incorrect handling of the vrf keyword between the destination address and next\-hop interface in both global and VRF contexts for IPv4 and IPv6 static\_route configurations\.

<a id="cisco-ise-3"></a>
#### cisco\.ise

* Added main\.yml to aws\_deployment role
* Collection not compatible with ansible\.utils 5\.x\.y
* Getting deployment info for entire deployment does not work
* Update min\_ansible\_version to 2\.15\.0 in runtime\.yml and roles
* cisco\.ise\.pan\_ha object has no attribute \'enable\_pan\_ha\'
* cisco\.ise\.support\_bundle\_download keeps failing after downloading the file
* endpoint\_group \- add missing parameter parentID\.
* mnt\_session\_active\_list\_info \- fix response xml\.
* network\_device \- mask param can be string or int\, cast to int at the end\.
* reservation \- remove duplicate parameter\.
* support\_bundle\_download \- remove duplicate parameter\.
* trusted\_certificate \- fix comparison between request and current object\.

<a id="cisco-meraki-8"></a>
#### cisco\.meraki

* Ansible utils requirements updated\.
* cisco\.meraki\.networks\_clients\_info \- incorrect API endpoint\, fixing info module\.
* cisco\.meraki\.networks\_switch\_stacks delete stack not working\, fixing path parameters\.

<a id="cisco-mso-3"></a>
#### cisco\.mso

* Fix to avoid making updates to attributes that are not provided which could lead to removal of configuration in mso\_schema\_template\_bd
* Fix to avoid making updates to attributes that are not provided which could lead to removal of configuration in mso\_schema\_template\_vrf
* Fix to be able to reference APIC only L3Out in mso\_schema\_site\_external\_epg

<a id="cisco-nxos-7"></a>
#### cisco\.nxos

* acls \- Fix lookup of range port conversion from int to string to allow strings \([https\://github\.com/ansible\-collections/cisco\.nxos/pull/888](https\://github\.com/ansible\-collections/cisco\.nxos/pull/888)\)\.
* facts \- Fixes issue where the LLDP neighbor information returns an error when empty\.
* nxos\_l3\_interfaces \- fail if encapsulation exists on a different sub\-interface\.
* nxos\_snmp\_server \- correctly render entity traps \([https\://github\.com/ansible\-collections/cisco\.nxos/issues/820](https\://github\.com/ansible\-collections/cisco\.nxos/issues/820)\)\.
* nxos\_static\_routes \- correctly generate command when track parameter is specified\.

<a id="cloud-common-3"></a>
#### cloud\.common

* module\_utils/turbo/server \- Ensure all import statements in run\_as\_lookup\_plugin\(\) are in a try/except block \([https\://github\.com/ansible\-collections/cloud\.common/pull/143](https\://github\.com/ansible\-collections/cloud\.common/pull/143)\)\.

<a id="community-aws-7"></a>
#### community\.aws

* autoscaling\_instance\_refresh \- Fix typo in module <code>exit\_json</code> \([https\://github\.com/ansible\-collections/community\.aws/issues/2019](https\://github\.com/ansible\-collections/community\.aws/issues/2019)\)\.
* ecs\_taskdefinition \- Avoid throttling exceptions on task definitions with a large number of revisions by using the retry mechanism \([https\://github\.com/ansible\-collections/community\.aws/issues/2123](https\://github\.com/ansible\-collections/community\.aws/issues/2123)\)\.
* ecs\_taskdefinition \- avoid throttling exceptions on task definitions with a large number of revisions by using the retry mechanism \([https\://github\.com/ansible\-collections/community\.aws/issues/2123](https\://github\.com/ansible\-collections/community\.aws/issues/2123)\)\.

<a id="community-crypto-10"></a>
#### community\.crypto

* When using cryptography \>\= 43\.0\.0\, use offset\-aware <code>datetime\.datetime</code> objects \(with timezone UTC\) instead of offset\-naive UTC timestamps for the <code>InvalidityDate</code> X\.509 CRL extension \([https\://github\.com/ansible\-collections/community\.crypto/issues/726](https\://github\.com/ansible\-collections/community\.crypto/issues/726)\, [https\://github\.com/ansible\-collections/community\.crypto/pull/730](https\://github\.com/ansible\-collections/community\.crypto/pull/730)\)\.
* acme\_\* modules \- when querying renewal information\, make sure to insert a slash between the base URL and the certificate identifier \([https\://github\.com/ansible\-collections/community\.crypto/issues/801](https\://github\.com/ansible\-collections/community\.crypto/issues/801)\, [https\://github\.com/ansible\-collections/community\.crypto/pull/802](https\://github\.com/ansible\-collections/community\.crypto/pull/802)\)\.
* acme\_\* modules \- when using the OpenSSL backend\, explicitly use the UTC timezone in Python code \([https\://github\.com/ansible\-collections/community\.crypto/pull/811](https\://github\.com/ansible\-collections/community\.crypto/pull/811)\)\.
* acme\_certificate \- fix authorization failure when CSR contains SANs with mixed case \([https\://github\.com/ansible\-collections/community\.crypto/pull/803](https\://github\.com/ansible\-collections/community\.crypto/pull/803)\)\.
* time module utils \- fix conversion of naive <code>datetime</code> objects to UNIX timestamps for Python 3 \([https\://github\.com/ansible\-collections/community\.crypto/issues/808](https\://github\.com/ansible\-collections/community\.crypto/issues/808)\, [https\://github\.com/ansible\-collections/community\.crypto/pull/810](https\://github\.com/ansible\-collections/community\.crypto/pull/810)\)\.
* various modules \- pass absolute paths to <code>module\.atomic\_move\(\)</code> \([https\://github\.com/ansible/ansible/issues/83950](https\://github\.com/ansible/ansible/issues/83950)\, [https\://github\.com/ansible\-collections/community\.crypto/pull/799](https\://github\.com/ansible\-collections/community\.crypto/pull/799)\)\.

<a id="community-dns-9"></a>
#### community\.dns

* Update Public Suffix List\.

<a id="community-docker-14"></a>
#### community\.docker

* docker\_compose \- make sure that the module uses the <code>api\_version</code> parameter \([https\://github\.com/ansible\-collections/community\.docker/pull/881](https\://github\.com/ansible\-collections/community\.docker/pull/881)\)\.
* docker\_compose\_v2 \- handle yet another random unstructured error output from pre\-2\.29\.0 Compose versions \([https\://github\.com/ansible\-collections/community\.docker/issues/948](https\://github\.com/ansible\-collections/community\.docker/issues/948)\, [https\://github\.com/ansible\-collections/community\.docker/pull/949](https\://github\.com/ansible\-collections/community\.docker/pull/949)\)\.
* docker\_compose\_v2 \- improve parsing of dry\-run image build operations from JSON events \([https\://github\.com/ansible\-collections/community\.docker/issues/975](https\://github\.com/ansible\-collections/community\.docker/issues/975)\, [https\://github\.com/ansible\-collections/community\.docker/pull/976](https\://github\.com/ansible\-collections/community\.docker/pull/976)\)\.
* docker\_compose\_v2 \- make sure that services provided in <code>services</code> are appended to the command line after <code>\-\-</code> and not before it \([https\://github\.com/ansible\-collections/community\.docker/pull/942](https\://github\.com/ansible\-collections/community\.docker/pull/942)\)\.
* docker\_compose\_v2\* modules \- fix parsing of skipped pull messages for Docker Compose 2\.28\.x \([https\://github\.com/ansible\-collections/community\.docker/issues/911](https\://github\.com/ansible\-collections/community\.docker/issues/911)\, [https\://github\.com/ansible\-collections/community\.docker/pull/916](https\://github\.com/ansible\-collections/community\.docker/pull/916)\)\.
* docker\_compose\_v2\* modules \- there was no check to make sure that one of <code>project\_src</code> and <code>definition</code> is provided\. The modules crashed if none were provided \([https\://github\.com/ansible\-collections/community\.docker/issues/885](https\://github\.com/ansible\-collections/community\.docker/issues/885)\, [https\://github\.com/ansible\-collections/community\.docker/pull/886](https\://github\.com/ansible\-collections/community\.docker/pull/886)\)\.
* docker\_compose\_v2\* modules\, docker\_image\_build \- provide better error message when required fields are not present in <code>docker version</code> or <code>docker info</code> output\. This can happen if Podman is used instead of Docker \([https\://github\.com/ansible\-collections/community\.docker/issues/891](https\://github\.com/ansible\-collections/community\.docker/issues/891)\, [https\://github\.com/ansible\-collections/community\.docker/pull/935](https\://github\.com/ansible\-collections/community\.docker/pull/935)\)\.
* docker\_compose\_v2\*\, docker\_stack\*\, docker\_image\_build modules \- using <code>cli\_context</code> no longer leads to an invalid parameter combination being passed to the corresponding Docker CLI tool\, unless <code>docker\_host</code> is also provided\. Combining <code>cli\_context</code> and <code>docker\_host</code> is no longer allowed \([https\://github\.com/ansible\-collections/community\.docker/issues/892](https\://github\.com/ansible\-collections/community\.docker/issues/892)\, [https\://github\.com/ansible\-collections/community\.docker/pull/895](https\://github\.com/ansible\-collections/community\.docker/pull/895)\)\.
* docker\_compose\_v2\_run \- make sure to sanitize <code>labels</code> before sending them to the Docker Daemon \([https\://github\.com/ansible\-collections/community\.docker/pull/985](https\://github\.com/ansible\-collections/community\.docker/pull/985)\)\.
* docker\_config \- make sure to sanitize <code>labels</code> before sending them to the Docker Daemon \([https\://github\.com/ansible\-collections/community\.docker/pull/985](https\://github\.com/ansible\-collections/community\.docker/pull/985)\)\.
* docker\_container \- fix idempotency if <code>network\_mode\=default</code> and Docker 26\.1\.0 or later is used\. There was a breaking change in Docker 26\.1\.0 regarding normalization of <code>NetworkMode</code> \([https\://github\.com/ansible\-collections/community\.docker/issues/934](https\://github\.com/ansible\-collections/community\.docker/issues/934)\, [https\://github\.com/ansible\-collections/community\.docker/pull/936](https\://github\.com/ansible\-collections/community\.docker/pull/936)\)\.
* docker\_container \- fix possible infinite loop if <code>removal\_wait\_timeout</code> is set \([https\://github\.com/ansible\-collections/community\.docker/pull/922](https\://github\.com/ansible\-collections/community\.docker/pull/922)\)\.
* docker\_container \- restore behavior of the module from community\.docker 2\.x\.y that passes the first network to the Docker Deamon while creating the container \([https\://github\.com/ansible\-collections/community\.docker/pull/933](https\://github\.com/ansible\-collections/community\.docker/pull/933)\)\.
* docker\_image\_build \- fix <code>\-\-output</code> parameter composition for <code>type\=docker</code> and <code>type\=image</code> \([https\://github\.com/ansible\-collections/community\.docker/issues/946](https\://github\.com/ansible\-collections/community\.docker/issues/946)\, [https\://github\.com/ansible\-collections/community\.docker/pull/947](https\://github\.com/ansible\-collections/community\.docker/pull/947)\)\.
* docker\_network \- make sure to sanitize <code>labels</code> before sending them to the Docker Daemon \([https\://github\.com/ansible\-collections/community\.docker/pull/985](https\://github\.com/ansible\-collections/community\.docker/pull/985)\)\.
* docker\_node \- make sure to sanitize <code>labels</code> before sending them to the Docker Daemon \([https\://github\.com/ansible\-collections/community\.docker/pull/985](https\://github\.com/ansible\-collections/community\.docker/pull/985)\)\.
* docker\_prune \- fix handling of lists for the filter options \([https\://github\.com/ansible\-collections/community\.docker/issues/961](https\://github\.com/ansible\-collections/community\.docker/issues/961)\, [https\://github\.com/ansible\-collections/community\.docker/pull/966](https\://github\.com/ansible\-collections/community\.docker/pull/966)\)\.
* docker\_secret \- make sure to sanitize <code>labels</code> before sending them to the Docker Daemon \([https\://github\.com/ansible\-collections/community\.docker/pull/985](https\://github\.com/ansible\-collections/community\.docker/pull/985)\)\.
* docker\_swarm \- make sure to sanitize <code>labels</code> before sending them to the Docker Daemon \([https\://github\.com/ansible\-collections/community\.docker/pull/985](https\://github\.com/ansible\-collections/community\.docker/pull/985)\)\.
* docker\_swarm\_service \- make sure to sanitize <code>labels</code> and <code>container\_labels</code> before sending them to the Docker Daemon \([https\://github\.com/ansible\-collections/community\.docker/pull/985](https\://github\.com/ansible\-collections/community\.docker/pull/985)\)\.
* docker\_volume \- make sure to sanitize <code>labels</code> before sending them to the Docker Daemon \([https\://github\.com/ansible\-collections/community\.docker/pull/985](https\://github\.com/ansible\-collections/community\.docker/pull/985)\)\.
* vendored Docker SDK for Python \- use <code>LooseVersion</code> instead of <code>StrictVersion</code> to compare urllib3 versions\. This is needed for development versions \([https\://github\.com/ansible\-collections/community\.docker/pull/902](https\://github\.com/ansible\-collections/community\.docker/pull/902)\)\.

<a id="community-general-31"></a>
#### community\.general

* bitwarden lookup plugin \- fix <code>KeyError</code> in <code>search\_field</code> \([https\://github\.com/ansible\-collections/community\.general/issues/8549](https\://github\.com/ansible\-collections/community\.general/issues/8549)\, [https\://github\.com/ansible\-collections/community\.general/pull/8557](https\://github\.com/ansible\-collections/community\.general/pull/8557)\)\.
* bitwarden lookup plugin \- support BWS v0\.3\.0 syntax breaking change \([https\://github\.com/ansible\-collections/community\.general/pull/9028](https\://github\.com/ansible\-collections/community\.general/pull/9028)\)\.
* cloudflare\_dns \- fix changing Cloudflare SRV records \([https\://github\.com/ansible\-collections/community\.general/issues/8679](https\://github\.com/ansible\-collections/community\.general/issues/8679)\, [https\://github\.com/ansible\-collections/community\.general/pull/8948](https\://github\.com/ansible\-collections/community\.general/pull/8948)\)\.
* cmd\_runner module utils \- call to <code>get\_best\_parsable\_locales\(\)</code> was missing parameter \([https\://github\.com/ansible\-collections/community\.general/pull/8929](https\://github\.com/ansible\-collections/community\.general/pull/8929)\)\.
* collection\_version lookup plugin \- use <code>importlib</code> directly instead of the deprecated and in ansible\-core 2\.19 removed <code>ansible\.module\_utils\.compat\.importlib</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9084](https\://github\.com/ansible\-collections/community\.general/pull/9084)\)\.
* cpanm \- use new <code>VarDict</code> to prevent deprecation warning \([https\://github\.com/ansible\-collections/community\.general/issues/8410](https\://github\.com/ansible\-collections/community\.general/issues/8410)\, [https\://github\.com/ansible\-collections/community\.general/pull/8411](https\://github\.com/ansible\-collections/community\.general/pull/8411)\)\.
* dig lookup plugin \- fix using only the last nameserver specified \([https\://github\.com/ansible\-collections/community\.general/pull/8970](https\://github\.com/ansible\-collections/community\.general/pull/8970)\)\.
* django module utils \- use new <code>VarDict</code> to prevent deprecation warning \([https\://github\.com/ansible\-collections/community\.general/issues/8410](https\://github\.com/ansible\-collections/community\.general/issues/8410)\, [https\://github\.com/ansible\-collections/community\.general/pull/8411](https\://github\.com/ansible\-collections/community\.general/pull/8411)\)\.
* django\_command \- option <code>command</code> is now split lexically before passed to underlying PythonRunner \([https\://github\.com/ansible\-collections/community\.general/pull/8944](https\://github\.com/ansible\-collections/community\.general/pull/8944)\)\.
* gconftool2\_info \- use new <code>VarDict</code> to prevent deprecation warning \([https\://github\.com/ansible\-collections/community\.general/issues/8410](https\://github\.com/ansible\-collections/community\.general/issues/8410)\, [https\://github\.com/ansible\-collections/community\.general/pull/8411](https\://github\.com/ansible\-collections/community\.general/pull/8411)\)\.
* git\_config \- fix behavior of <code>state\=absent</code> if <code>value</code> is present \([https\://github\.com/ansible\-collections/community\.general/issues/8436](https\://github\.com/ansible\-collections/community\.general/issues/8436)\, [https\://github\.com/ansible\-collections/community\.general/pull/8452](https\://github\.com/ansible\-collections/community\.general/pull/8452)\)\.
* gitlab\_group\_access\_token \- fix crash in check mode caused by attempted access to a newly created access token \([https\://github\.com/ansible\-collections/community\.general/pull/8796](https\://github\.com/ansible\-collections/community\.general/pull/8796)\)\.
* gitlab\_label \- update label\'s color \([https\://github\.com/ansible\-collections/community\.general/pull/9010](https\://github\.com/ansible\-collections/community\.general/pull/9010)\)\.
* gitlab\_project \- fix <code>container\_expiration\_policy</code> not being applied when creating a new project \([https\://github\.com/ansible\-collections/community\.general/pull/8790](https\://github\.com/ansible\-collections/community\.general/pull/8790)\)\.
* gitlab\_project \- fix crash caused by old Gitlab projects not having a <code>container\_expiration\_policy</code> attribute \([https\://github\.com/ansible\-collections/community\.general/pull/8790](https\://github\.com/ansible\-collections/community\.general/pull/8790)\)\.
* gitlab\_project\_access\_token \- fix crash in check mode caused by attempted access to a newly created access token \([https\://github\.com/ansible\-collections/community\.general/pull/8796](https\://github\.com/ansible\-collections/community\.general/pull/8796)\)\.
* gitlab\_runner \- fix <code>paused</code> parameter being ignored \([https\://github\.com/ansible\-collections/community\.general/pull/8648](https\://github\.com/ansible\-collections/community\.general/pull/8648)\)\.
* homebrew \- do not fail when brew prints warnings \([https\://github\.com/ansible\-collections/community\.general/pull/8406](https\://github\.com/ansible\-collections/community\.general/pull/8406)\, [https\://github\.com/ansible\-collections/community\.general/issues/7044](https\://github\.com/ansible\-collections/community\.general/issues/7044)\)\.
* homebrew\_cask \- fix <code>upgrade\_all</code> returns <code>changed</code> when nothing upgraded \([https\://github\.com/ansible\-collections/community\.general/issues/8707](https\://github\.com/ansible\-collections/community\.general/issues/8707)\, [https\://github\.com/ansible\-collections/community\.general/pull/8708](https\://github\.com/ansible\-collections/community\.general/pull/8708)\)\.
* homectl \- the module now tries to use <code>legacycrypt</code> on Python 3\.13\+ \([https\://github\.com/ansible\-collections/community\.general/issues/4691](https\://github\.com/ansible\-collections/community\.general/issues/4691)\, [https\://github\.com/ansible\-collections/community\.general/pull/8987](https\://github\.com/ansible\-collections/community\.general/pull/8987)\)\.
* hponcfg \- use new <code>VarDict</code> to prevent deprecation warning \([https\://github\.com/ansible\-collections/community\.general/issues/8410](https\://github\.com/ansible\-collections/community\.general/issues/8410)\, [https\://github\.com/ansible\-collections/community\.general/pull/8411](https\://github\.com/ansible\-collections/community\.general/pull/8411)\)\.
* ini\_file \- pass absolute paths to <code>module\.atomic\_move\(\)</code> \([https\://github\.com/ansible/ansible/issues/83950](https\://github\.com/ansible/ansible/issues/83950)\, [https\://github\.com/ansible\-collections/community\.general/pull/8925](https\://github\.com/ansible\-collections/community\.general/pull/8925)\)\.
* ipa\_host \- add <code>force\_create</code>\, fix <code>enabled</code> and <code>disabled</code> states \([https\://github\.com/ansible\-collections/community\.general/issues/1094](https\://github\.com/ansible\-collections/community\.general/issues/1094)\, [https\://github\.com/ansible\-collections/community\.general/pull/8920](https\://github\.com/ansible\-collections/community\.general/pull/8920)\)\.
* ipa\_hostgroup \- fix <code>enabled \`\` and \`\`disabled</code> states \([https\://github\.com/ansible\-collections/community\.general/issues/8408](https\://github\.com/ansible\-collections/community\.general/issues/8408)\, [https\://github\.com/ansible\-collections/community\.general/pull/8900](https\://github\.com/ansible\-collections/community\.general/pull/8900)\)\.
* java\_keystore \- pass absolute paths to <code>module\.atomic\_move\(\)</code> \([https\://github\.com/ansible/ansible/issues/83950](https\://github\.com/ansible/ansible/issues/83950)\, [https\://github\.com/ansible\-collections/community\.general/pull/8925](https\://github\.com/ansible\-collections/community\.general/pull/8925)\)\.
* jenkins\_node \- fixed <code>enabled</code>\, <code>disable</code> and <code>absent</code> node state redirect authorization issues\, same as was present for <code>present</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9084](https\://github\.com/ansible\-collections/community\.general/pull/9084)\)\.
* jenkins\_plugin \- pass absolute paths to <code>module\.atomic\_move\(\)</code> \([https\://github\.com/ansible/ansible/issues/83950](https\://github\.com/ansible/ansible/issues/83950)\, [https\://github\.com/ansible\-collections/community\.general/pull/8925](https\://github\.com/ansible\-collections/community\.general/pull/8925)\)\.
* kdeconfig \- pass absolute paths to <code>module\.atomic\_move\(\)</code> \([https\://github\.com/ansible/ansible/issues/83950](https\://github\.com/ansible/ansible/issues/83950)\, [https\://github\.com/ansible\-collections/community\.general/pull/8925](https\://github\.com/ansible\-collections/community\.general/pull/8925)\)\.
* kernel\_blacklist \- use new <code>VarDict</code> to prevent deprecation warning \([https\://github\.com/ansible\-collections/community\.general/issues/8410](https\://github\.com/ansible\-collections/community\.general/issues/8410)\, [https\://github\.com/ansible\-collections/community\.general/pull/8411](https\://github\.com/ansible\-collections/community\.general/pull/8411)\)\.
* keycloak\_client \- fix TypeError when sanitizing the <code>saml\.signing\.private\.key</code> attribute in the module\'s diff or state output\. The <code>sanitize\_cr</code> function expected a dict where in some cases a list might occur \([https\://github\.com/ansible\-collections/community\.general/pull/8403](https\://github\.com/ansible\-collections/community\.general/pull/8403)\)\.
* keycloak\_client \- fix diff by removing code that turns the attributes dict which contains additional settings into a list \([https\://github\.com/ansible\-collections/community\.general/pull/9077](https\://github\.com/ansible\-collections/community\.general/pull/9077)\)\.
* keycloak\_clientscope \- fix diff and <code>end\_state</code> by removing the code that turns the attributes dict\, which contains additional config items\, into a list \([https\://github\.com/ansible\-collections/community\.general/pull/9082](https\://github\.com/ansible\-collections/community\.general/pull/9082)\)\.
* keycloak\_clientscope \- remove IDs from clientscope and its protocol mappers on comparison for changed check \([https\://github\.com/ansible\-collections/community\.general/pull/8545](https\://github\.com/ansible\-collections/community\.general/pull/8545)\)\.
* keycloak\_clientscope\_type \- fix detect changes in check mode \([https\://github\.com/ansible\-collections/community\.general/issues/9092](https\://github\.com/ansible\-collections/community\.general/issues/9092)\, [https\://github\.com/ansible\-collections/community\.general/pull/9093](https\://github\.com/ansible\-collections/community\.general/pull/9093)\)\.
* keycloak\_group \- fix crash caused in subgroup creation\. The crash was caused by a missing or empty <code>subGroups</code> property in Keycloak ≥23 \([https\://github\.com/ansible\-collections/community\.general/issues/8788](https\://github\.com/ansible\-collections/community\.general/issues/8788)\, [https\://github\.com/ansible\-collections/community\.general/pull/8979](https\://github\.com/ansible\-collections/community\.general/pull/8979)\)\.
* keycloak\_realm \- add normalizations for <code>attributes</code> and <code>protocol\_mappers</code> \([https\://github\.com/ansible\-collections/community\.general/pull/8496](https\://github\.com/ansible\-collections/community\.general/pull/8496)\)\.
* keycloak\_realm \- fix change detection in check mode by sorting the lists in the realms beforehand \([https\://github\.com/ansible\-collections/community\.general/pull/8877](https\://github\.com/ansible\-collections/community\.general/pull/8877)\)\.
* keycloak\_realm\_key \- fix invalid usage of <code>parent\_id</code> \([https\://github\.com/ansible\-collections/community\.general/issues/7850](https\://github\.com/ansible\-collections/community\.general/issues/7850)\, [https\://github\.com/ansible\-collections/community\.general/pull/8823](https\://github\.com/ansible\-collections/community\.general/pull/8823)\)\.
* keycloak\_user\_federation \- add module argument allowing users to configure the update mode for the parameter <code>bindCredential</code> \([https\://github\.com/ansible\-collections/community\.general/pull/8898](https\://github\.com/ansible\-collections/community\.general/pull/8898)\)\.
* keycloak\_user\_federation \- fix key error when removing mappers during an update and new mappers are specified in the module args \([https\://github\.com/ansible\-collections/community\.general/pull/8762](https\://github\.com/ansible\-collections/community\.general/pull/8762)\)\.
* keycloak\_user\_federation \- fix the <code>UnboundLocalError</code> that occurs when an ID is provided for a user federation mapper \([https\://github\.com/ansible\-collections/community\.general/pull/8831](https\://github\.com/ansible\-collections/community\.general/pull/8831)\)\.
* keycloak\_user\_federation \- get cleartext IDP <code>clientSecret</code> from full realm info to detect changes to it \([https\://github\.com/ansible\-collections/community\.general/issues/8294](https\://github\.com/ansible\-collections/community\.general/issues/8294)\, [https\://github\.com/ansible\-collections/community\.general/pull/8735](https\://github\.com/ansible\-collections/community\.general/pull/8735)\)\.
* keycloak\_user\_federation \- minimize change detection by setting <code>krbPrincipalAttribute</code> to <code>\'\'</code> in Keycloak responses if missing \([https\://github\.com/ansible\-collections/community\.general/pull/8785](https\://github\.com/ansible\-collections/community\.general/pull/8785)\)\.
* keycloak\_user\_federation \- remove <code>lastSync</code> parameter from Keycloak responses to minimize diff/changes \([https\://github\.com/ansible\-collections/community\.general/pull/8812](https\://github\.com/ansible\-collections/community\.general/pull/8812)\)\.
* keycloak\_user\_federation \- remove existing user federation mappers if they are not present in the federation configuration and will not be updated \([https\://github\.com/ansible\-collections/community\.general/issues/7169](https\://github\.com/ansible\-collections/community\.general/issues/7169)\, [https\://github\.com/ansible\-collections/community\.general/pull/8695](https\://github\.com/ansible\-collections/community\.general/pull/8695)\)\.
* keycloak\_user\_federation \- sort desired and after mapper list by name \(analog to before mapper list\) to minimize diff and make change detection more accurate \([https\://github\.com/ansible\-collections/community\.general/pull/8761](https\://github\.com/ansible\-collections/community\.general/pull/8761)\)\.
* keycloak\_userprofile \- fix empty response when fetching userprofile component by removing <code>parent\=parent\_id</code> filter \([https\://github\.com/ansible\-collections/community\.general/pull/8923](https\://github\.com/ansible\-collections/community\.general/pull/8923)\)\.
* keycloak\_userprofile \- improve diff by deserializing the fetched <code>kc\.user\.profile\.config</code> and serialize it only when sending back \([https\://github\.com/ansible\-collections/community\.general/pull/8940](https\://github\.com/ansible\-collections/community\.general/pull/8940)\)\.
* launched \- correctly report changed status in check mode \([https\://github\.com/ansible\-collections/community\.general/pull/8406](https\://github\.com/ansible\-collections/community\.general/pull/8406)\)\.
* locale\_gen \- use new <code>VarDict</code> to prevent deprecation warning \([https\://github\.com/ansible\-collections/community\.general/issues/8410](https\://github\.com/ansible\-collections/community\.general/issues/8410)\, [https\://github\.com/ansible\-collections/community\.general/pull/8411](https\://github\.com/ansible\-collections/community\.general/pull/8411)\)\.
* lxd\_container \- fix bug introduced in previous commit \([https\://github\.com/ansible\-collections/community\.general/pull/8895](https\://github\.com/ansible\-collections/community\.general/pull/8895)\, [https\://github\.com/ansible\-collections/community\.general/issues/8888](https\://github\.com/ansible\-collections/community\.general/issues/8888)\)\.
* mksysb \- use new <code>VarDict</code> to prevent deprecation warning \([https\://github\.com/ansible\-collections/community\.general/issues/8410](https\://github\.com/ansible\-collections/community\.general/issues/8410)\, [https\://github\.com/ansible\-collections/community\.general/pull/8411](https\://github\.com/ansible\-collections/community\.general/pull/8411)\)\.
* modprobe \- fix check mode not being honored for <code>persistent</code> option \([https\://github\.com/ansible\-collections/community\.general/issues/9051](https\://github\.com/ansible\-collections/community\.general/issues/9051)\, [https\://github\.com/ansible\-collections/community\.general/pull/9052](https\://github\.com/ansible\-collections/community\.general/pull/9052)\)\.
* nsupdate \- fix \'index out of range\' error when changing NS records by falling back to authority section of the response \([https\://github\.com/ansible\-collections/community\.general/issues/8612](https\://github\.com/ansible\-collections/community\.general/issues/8612)\, [https\://github\.com/ansible\-collections/community\.general/pull/8614](https\://github\.com/ansible\-collections/community\.general/pull/8614)\)\.
* one\_host \- fix if statements for cases when <code>ID\=0</code> \([https\://github\.com/ansible\-collections/community\.general/issues/1199](https\://github\.com/ansible\-collections/community\.general/issues/1199)\, [https\://github\.com/ansible\-collections/community\.general/pull/8907](https\://github\.com/ansible\-collections/community\.general/pull/8907)\)\.
* one\_image \- fix module failing due to a class method typo \([https\://github\.com/ansible\-collections/community\.general/pull/9056](https\://github\.com/ansible\-collections/community\.general/pull/9056)\)\.
* one\_image\_info \- fix module failing due to a class method typo \([https\://github\.com/ansible\-collections/community\.general/pull/9056](https\://github\.com/ansible\-collections/community\.general/pull/9056)\)\.
* one\_service \- fix service creation after it was deleted with <code>unique</code> parameter \([https\://github\.com/ansible\-collections/community\.general/issues/3137](https\://github\.com/ansible\-collections/community\.general/issues/3137)\, [https\://github\.com/ansible\-collections/community\.general/pull/8887](https\://github\.com/ansible\-collections/community\.general/pull/8887)\)\.
* one\_vnet \- fix module failing due to a variable typo \([https\://github\.com/ansible\-collections/community\.general/pull/9019](https\://github\.com/ansible\-collections/community\.general/pull/9019)\)\.
* opennebula inventory plugin \- fix invalid reference to IP when inventory runs against NICs with no IPv4 address \([https\://github\.com/ansible\-collections/community\.general/pull/8489](https\://github\.com/ansible\-collections/community\.general/pull/8489)\)\.
* opentelemetry callback \- do not save the JSON response when using the <code>ansible\.builtin\.uri</code> module \([https\://github\.com/ansible\-collections/community\.general/pull/8430](https\://github\.com/ansible\-collections/community\.general/pull/8430)\)\.
* opentelemetry callback \- do not save the content response when using the <code>ansible\.builtin\.slurp</code> module \([https\://github\.com/ansible\-collections/community\.general/pull/8430](https\://github\.com/ansible\-collections/community\.general/pull/8430)\)\.
* pam\_limits \- pass absolute paths to <code>module\.atomic\_move\(\)</code> \([https\://github\.com/ansible/ansible/issues/83950](https\://github\.com/ansible/ansible/issues/83950)\, [https\://github\.com/ansible\-collections/community\.general/pull/8925](https\://github\.com/ansible\-collections/community\.general/pull/8925)\)\.
* paman \- do not fail if an empty list of packages has been provided and there is nothing to do \([https\://github\.com/ansible\-collections/community\.general/pull/8514](https\://github\.com/ansible\-collections/community\.general/pull/8514)\)\.
* pipx \- it was ignoring <code>global</code> when listing existing applications \([https\://github\.com/ansible\-collections/community\.general/pull/9044](https\://github\.com/ansible\-collections/community\.general/pull/9044)\)\.
* pipx module utils \- add missing command line formatter for argument <code>spec\_metadata</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9044](https\://github\.com/ansible\-collections/community\.general/pull/9044)\)\.
* pipx\_info \- use new <code>VarDict</code> to prevent deprecation warning \([https\://github\.com/ansible\-collections/community\.general/issues/8410](https\://github\.com/ansible\-collections/community\.general/issues/8410)\, [https\://github\.com/ansible\-collections/community\.general/pull/8411](https\://github\.com/ansible\-collections/community\.general/pull/8411)\)\.
* proxmox \- fix idempotency on creation of mount volumes using Proxmox\' special <code>\<storage\>\:\<size\></code> syntax \([https\://github\.com/ansible\-collections/community\.general/issues/8407](https\://github\.com/ansible\-collections/community\.general/issues/8407)\, [https\://github\.com/ansible\-collections/community\.general/pull/8542](https\://github\.com/ansible\-collections/community\.general/pull/8542)\)\.
* proxmox \- fixed an issue where the new volume handling incorrectly converted <code>null</code> values into <code>\"None\"</code> strings \([https\://github\.com/ansible\-collections/community\.general/pull/8646](https\://github\.com/ansible\-collections/community\.general/pull/8646)\)\.
* proxmox \- fixed an issue where volume strings where overwritten instead of appended to in the new <code>build\_volume\(\)</code> method \([https\://github\.com/ansible\-collections/community\.general/pull/8646](https\://github\.com/ansible\-collections/community\.general/pull/8646)\)\.
* proxmox \- removed the forced conversion of non\-string values to strings to be consistent with the module documentation \([https\://github\.com/ansible\-collections/community\.general/pull/8646](https\://github\.com/ansible\-collections/community\.general/pull/8646)\)\.
* proxmox inventory plugin \- fixed a possible error on concatenating responses from proxmox\. In case an API call unexpectedly returned an empty result\, the inventory failed with a fatal error\. Added check for empty response \([https\://github\.com/ansible\-collections/community\.general/issues/8798](https\://github\.com/ansible\-collections/community\.general/issues/8798)\, [https\://github\.com/ansible\-collections/community\.general/pull/8794](https\://github\.com/ansible\-collections/community\.general/pull/8794)\)\.
* python\_runner module utils \- parameter <code>path\_prefix</code> was being handled as string when it should be a list \([https\://github\.com/ansible\-collections/community\.general/pull/8944](https\://github\.com/ansible\-collections/community\.general/pull/8944)\)\.
* redfish\_utils module utils \- do not fail when language is not exactly \"en\" \([https\://github\.com/ansible\-collections/community\.general/pull/8613](https\://github\.com/ansible\-collections/community\.general/pull/8613)\)\.
* redfish\_utils module utils \- fix issue with URI parsing to gracefully handling trailing slashes when extracting member identifiers \([https\://github\.com/ansible\-collections/community\.general/issues/9047](https\://github\.com/ansible\-collections/community\.general/issues/9047)\, [https\://github\.com/ansible\-collections/community\.general/pull/9057](https\://github\.com/ansible\-collections/community\.general/pull/9057)\)\.
* redfish\_utils module utils \- remove undocumented default applytime \([https\://github\.com/ansible\-collections/community\.general/pull/9114](https\://github\.com/ansible\-collections/community\.general/pull/9114)\)\.
* snap \- use new <code>VarDict</code> to prevent deprecation warning \([https\://github\.com/ansible\-collections/community\.general/issues/8410](https\://github\.com/ansible\-collections/community\.general/issues/8410)\, [https\://github\.com/ansible\-collections/community\.general/pull/8411](https\://github\.com/ansible\-collections/community\.general/pull/8411)\)\.
* snap\_alias \- use new <code>VarDict</code> to prevent deprecation warning \([https\://github\.com/ansible\-collections/community\.general/issues/8410](https\://github\.com/ansible\-collections/community\.general/issues/8410)\, [https\://github\.com/ansible\-collections/community\.general/pull/8411](https\://github\.com/ansible\-collections/community\.general/pull/8411)\)\.
* udm\_user \- the module now tries to use <code>legacycrypt</code> on Python 3\.13\+ \([https\://github\.com/ansible\-collections/community\.general/issues/4690](https\://github\.com/ansible\-collections/community\.general/issues/4690)\, [https\://github\.com/ansible\-collections/community\.general/pull/8987](https\://github\.com/ansible\-collections/community\.general/pull/8987)\)\.

<a id="community-grafana-5"></a>
#### community\.grafana

* Add missing function argument in <em class="title-reference">grafana\_contact\_point</em> for org handling
* Fix var prefixes in silence\-task in role
* Fixed check if grafana\_api\_key is defined for <em class="title-reference">grafana\_dashboard</em> lookup

<a id="community-hrobot-7"></a>
#### community\.hrobot

* boot \- use PHP array form encoding when sending multiple <code>authorized\_key</code> \([https\://github\.com/ansible\-collections/community\.hrobot/issues/112](https\://github\.com/ansible\-collections/community\.hrobot/issues/112)\, [https\://github\.com/ansible\-collections/community\.hrobot/pull/113](https\://github\.com/ansible\-collections/community\.hrobot/pull/113)\)\.

<a id="community-mysql-9"></a>
#### community\.mysql

* mysql\_info \- Add <code>plugin\_hash\_string</code> to <code>users\_info</code> filter\'s output\. The existing <code>plugin\_auth\_string</code> contained the hashed password and thus is missleading\, it will be removed from community\.mysql 4\.0\.0\. \([https\://github\.com/ansible\-collections/community\.mysql/pull/629](https\://github\.com/ansible\-collections/community\.mysql/pull/629)\)\.
* mysql\_user \- Added a warning to update\_password\'s on\_new\_username option if multiple accounts with the same username but different passwords exist \([https\://github\.com/ansible\-collections/community\.mysql/pull/642](https\://github\.com/ansible\-collections/community\.mysql/pull/642)\)\.
* mysql\_user \- Fix <code>tls\_requires</code> not removing <code>SSL</code> and <code>X509</code> when sets as empty \([https\://github\.com/ansible\-collections/community\.mysql/pull/628](https\://github\.com/ansible\-collections/community\.mysql/pull/628)\)\.
* mysql\_user \- Fix idempotence when using variables from the <code>users\_info</code> filter of <code>mysql\_info</code> as an input \([https\://github\.com/ansible\-collections/community\.mysql/pull/628](https\://github\.com/ansible\-collections/community\.mysql/pull/628)\)\.
* mysql\_user \- Fixed an IndexError in the update\_password functionality introduced in PR [https\://github\.com/ansible\-collections/community\.mysql/pull/580](https\://github\.com/ansible\-collections/community\.mysql/pull/580) and released in community\.mysql 3\.8\.0\. If you used this functionality\, please avoid versions 3\.8\.0 to 3\.9\.0 \([https\://github\.com/ansible\-collections/community\.mysql/pull/642](https\://github\.com/ansible\-collections/community\.mysql/pull/642)\)\.
* mysql\_user \- add correct <code>ed25519</code> auth plugin handling \([https\://github\.com/ansible\-collections/community\.mysql/issues/6](https\://github\.com/ansible\-collections/community\.mysql/issues/6)\)\.
* mysql\_user \- add correct <code>ed25519</code> auth plugin handling when creating a user \([https\://github\.com/ansible\-collections/community\.mysql/issues/672](https\://github\.com/ansible\-collections/community\.mysql/issues/672)\)\.
* mysql\_user \- add correct <code>ed25519</code> auth plugin handling when creating a user \([https\://github\.com/ansible\-collections/community\.mysql/pull/676](https\://github\.com/ansible\-collections/community\.mysql/pull/676)\)\.
* mysql\_user \- module makes changes when is executed with <code>plugin\_auth\_string</code> parameter and check mode\.
* mysql\_variables \- fix the module always changes on boolean values \([https\://github\.com/ansible\-collections/community\.mysql/issues/652](https\://github\.com/ansible\-collections/community\.mysql/issues/652)\)\.

<a id="community-network-1"></a>
#### community\.network

* exos \- Add error handling of <code>Permission denied</code> errors \([https\://github\.com/ansible\-collections/community\.network/pull/571](https\://github\.com/ansible\-collections/community\.network/pull/571)\)\.

<a id="community-postgresql-13"></a>
#### community\.postgresql

* postgres \- psycopg2 automatically sets the datestyle on the connection to iso whenever it encounters a datestyle configuration it doesn\'t recognize\, but psycopg3 does not\. Fix now enforces iso datestyle when using psycopg3 \([https\://github\.com/ansible\-collections/community\.postgresql/issues/711](https\://github\.com/ansible\-collections/community\.postgresql/issues/711)\)\.
* postgresql\_db \- fix issues due to columns in pg\_database changing in Postgres 17\. \([https\://github\.com/ansible\-collections/community\.postgresql/issues/729](https\://github\.com/ansible\-collections/community\.postgresql/issues/729)\)\.
* postgresql\_info \- Use a server check that works on beta and rc versions as well as on actual releases\.
* postgresql\_set \- fixes resetting logic to allow resetting shared\_preload\_libraries with <code>reset\: true</code> \([https\://github\.com/ansible\-collections/community\.postgresql/issues/744](https\://github\.com/ansible\-collections/community\.postgresql/issues/744)\)\.
* postgresql\_set \- forbids resetting shared\_preload\_libraries by passing an empty string \([https\://github\.com/ansible\-collections/community\.postgresql/issues/744](https\://github\.com/ansible\-collections/community\.postgresql/issues/744)\)\.
* postgresql\_user \- remove a comment from unit tests that breaks pre\-compile \([https\://github\.com/ansible\-collections/community\.postgresql/issues/737](https\://github\.com/ansible\-collections/community\.postgresql/issues/737)\)\.

<a id="community-proxysql-1"></a>
#### community\.proxysql

* module\_utils \- fix ProxySQL version parsing that fails when a suffix wasn\'t present in the version \([https\://github\.com/ansible\-collections/community\.proxysql/issues/154](https\://github\.com/ansible\-collections/community\.proxysql/issues/154)\)\.
* role\_proxysql \- Correct package name \(python3\-mysqldb instead of python\-mysqldb\) \([https\://github\.com/ansible\-collections/community\.proxysql/pull/89](https\://github\.com/ansible\-collections/community\.proxysql/pull/89)\)\.
* role\_proxysql \- Dynamic user/password in \.my\.cnf \([https\://github\.com/ansible\-collections/community\.proxysql/pull/89](https\://github\.com/ansible\-collections/community\.proxysql/pull/89)\)\.

<a id="community-routeros-12"></a>
#### community\.routeros

* api\_modify\, api\_info \- change the default of <code>ingress\-filtering</code> in paths <code>interface bridge</code> and <code>interface bridge port</code> back to <code>false</code> for RouterOS before version 7 \([https\://github\.com/ansible\-collections/community\.routeros/pull/305](https\://github\.com/ansible\-collections/community\.routeros/pull/305)\)\.

<a id="community-sops-7"></a>
#### community\.sops

* Fix RPM URL for the 3\.9\.0 release \([https\://github\.com/ansible\-collections/community\.sops/pull/188](https\://github\.com/ansible\-collections/community\.sops/pull/188)\)\.
* Pass <code>config\_path</code> on SOPS 3\.9\.0 before the subcommand instead of after it \([https\://github\.com/ansible\-collections/community\.sops/issues/195](https\://github\.com/ansible\-collections/community\.sops/issues/195)\, [https\://github\.com/ansible\-collections/community\.sops/pull/197](https\://github\.com/ansible\-collections/community\.sops/pull/197)\)\.
* sops\_encrypt \- pass absolute paths to <code>module\.atomic\_move\(\)</code> \([https\://github\.com/ansible/ansible/issues/83950](https\://github\.com/ansible/ansible/issues/83950)\, [https\://github\.com/ansible\-collections/community\.sops/pull/208](https\://github\.com/ansible\-collections/community\.sops/pull/208)\)\.
* sops\_encrypt \- properly support <code>path\_regex</code> in <code>\.sops\.yaml</code> when SOPS 3\.9\.0 or later is used \([https\://github\.com/ansible\-collections/community\.sops/issues/153](https\://github\.com/ansible\-collections/community\.sops/issues/153)\, [https\://github\.com/ansible\-collections/community\.sops/pull/190](https\://github\.com/ansible\-collections/community\.sops/pull/190)\)\.

<a id="community-vmware-22"></a>
#### community\.vmware

* Document dependency on requests \([https\://github\.com/ansible\-collections/community\.vmware/issues/2127](https\://github\.com/ansible\-collections/community\.vmware/issues/2127)\)\.
* vcenter\_folder \- removed documentation that incorrectly said <em class="title-reference">folder\_type</em> had no effect when <em class="title-reference">parent\_folder</em> was set
* vcenter\_standard\_key\_provider \- Fix documentation \([https\://github\.com/ansible\-collections/community\.vmware/pull/2192](https\://github\.com/ansible\-collections/community\.vmware/pull/2192)\)\.
* vmware\_all\_snapshots\_info \- fixed the datacenter parameter was ignored\([https\://github\.com/ansible\-collections/community\.vmware/pull/2165](https\://github\.com/ansible\-collections/community\.vmware/pull/2165)\)\.
* vmware\_cluster\_vcls \- fixed bug caused by pyvmomi \>\=7\.0\.3 returning the vlcs cluster config attribute as None when it was previously undefined\. Now if the vCLS config is not initialized on the cluster\, the module will initialize it using the user\'s desired state\.
* vmware\_dvswitch \- Fix Pylint issue \([https\://github\.com/ansible\-collections/community\.vmware/pull/2186](https\://github\.com/ansible\-collections/community\.vmware/pull/2186)\)\.
* vmware\_dvswitch\_nioc \- Fix documentation \([https\://github\.com/ansible\-collections/community\.vmware/pull/2192](https\://github\.com/ansible\-collections/community\.vmware/pull/2192)\)\.
* vmware\_dvswitch\_pvlans \- Fix Pylint issue \([https\://github\.com/ansible\-collections/community\.vmware/pull/2186](https\://github\.com/ansible\-collections/community\.vmware/pull/2186)\)\.
* vmware\_guest \- Fix documentation \([https\://github\.com/ansible\-collections/community\.vmware/pull/2192](https\://github\.com/ansible\-collections/community\.vmware/pull/2192)\)\.
* vmware\_guest \- Fix existing disk erroneously being re\-created when modifying vm with 8 or more disks\. \([https\://github\.com/ansible\-collections/community\.vmware/pull/2173](https\://github\.com/ansible\-collections/community\.vmware/pull/2173)\)\.
* vmware\_guest\_controller \- Fix documentation \([https\://github\.com/ansible\-collections/community\.vmware/pull/2192](https\://github\.com/ansible\-collections/community\.vmware/pull/2192)\)\.
* vmware\_guest\_disk \- Fix documentation \([https\://github\.com/ansible\-collections/community\.vmware/pull/2192](https\://github\.com/ansible\-collections/community\.vmware/pull/2192)\)\.
* vmware\_guest\_disk \- round size to int\, supporting float values properly \([https\://github\.com/ansible\-collections/community\.vmware/issues/123](https\://github\.com/ansible\-collections/community\.vmware/issues/123)\)\.
* vmware\_guest\_serial\_port \- Fix documentation \([https\://github\.com/ansible\-collections/community\.vmware/pull/2192](https\://github\.com/ansible\-collections/community\.vmware/pull/2192)\)\.
* vmware\_guest\_snapshot \- Update documentation regarding snapshot\_id parameter \([https\://github\.com/ansible\-collections/community\.vmware/issues/2145](https\://github\.com/ansible\-collections/community\.vmware/issues/2145)\)\.
* vmware\_guest\_tpm \- Fix Pylint issue \([https\://github\.com/ansible\-collections/community\.vmware/pull/2186](https\://github\.com/ansible\-collections/community\.vmware/pull/2186)\)\.
* vmware\_host \- Fix Pylint issue \([https\://github\.com/ansible\-collections/community\.vmware/pull/2186](https\://github\.com/ansible\-collections/community\.vmware/pull/2186)\)\.
* vmware\_host\_dns \- Fix Pylint issue \([https\://github\.com/ansible\-collections/community\.vmware/pull/2186](https\://github\.com/ansible\-collections/community\.vmware/pull/2186)\)\.
* vmware\_host\_inventory \- Fix Pylint issue \([https\://github\.com/ansible\-collections/community\.vmware/pull/2186](https\://github\.com/ansible\-collections/community\.vmware/pull/2186)\)\.
* vmware\_host\_logbundle \- Manifests previously was separared by \"\&\"\, thus selecting first manifest\. Fix now separates manifests with URL encoded space\, thus correctly supplying the manifests\.  \([https\://github\.com/ansible\-collections/community\.vmware/pull/2090](https\://github\.com/ansible\-collections/community\.vmware/pull/2090)\)\.
* vmware\_host\_powerstate \- Fix Pylint issue \([https\://github\.com/ansible\-collections/community\.vmware/pull/2186](https\://github\.com/ansible\-collections/community\.vmware/pull/2186)\)\.
* vmware\_tools \- Fix documentation \([https\://github\.com/ansible\-collections/community\.vmware/pull/2192](https\://github\.com/ansible\-collections/community\.vmware/pull/2192)\)\.
* vmware\_vm\_inventory \- Fix Pylint issue \([https\://github\.com/ansible\-collections/community\.vmware/pull/2186](https\://github\.com/ansible\-collections/community\.vmware/pull/2186)\)\.
* vmware\_vmotion \- Fix Pylint issue \([https\://github\.com/ansible\-collections/community\.vmware/pull/2186](https\://github\.com/ansible\-collections/community\.vmware/pull/2186)\)\.
* vmware\_vmotion \- Fix a <em class="title-reference">list index out of range</em> error when vSphere doesn\'t provide a placement recommendation \([https\://github\.com/ansible\-collections/community\.vmware/pull/2208](https\://github\.com/ansible\-collections/community\.vmware/pull/2208)\)\.

<a id="community-windows-2"></a>
#### community\.windows

* win\_mapped\_drive \- Use correct P/Invoke signature to fix mapped network drives on 32 Bit OS\.
* win\_mapped\_drive \- better handle failures when attempting to set mapped drive that already exists but was seen as a local path\.

<a id="community-zabbix-8"></a>
#### community\.zabbix

* remove references to tags in LLD rules
* zabbix\_actions \- fix proxy get compatibility for zabbix 7\.0
* zabbix\_agent Role \- Fix Configure zabbix\_agent
* zabbix\_agent Role \- Fix for userparameter because include\_dir is list
* zabbix\_agent Role \- Fix include\_dir directory creation logic
* zabbix\_agent Role \- Fixed several issues related to <em class="title-reference">zabbix\_agent\_include\_dir</em> and <em class="title-reference">zabbix\_agent\_include</em>
* zabbix\_agent Role \- Fixes a mispelling of the <em class="title-reference">zabbix\_agent\_logfile</em> variable
* zabbix\_agent Role \- Fixes error in the double assignment of values for the <em class="title-reference">zabbix\_agent\_tlspskidentity\_check</em> and <em class="title-reference">zabbix\_agent\_tlspskcheck</em> variables\.
* zabbix\_agent Role \- Fixes multiple errors related to the Windows install
* zabbix\_agent Role \- fix TLSAccept parameter provisioning in zabbix\_agentd\.conf
* zabbix\_agent Role \- fixed problem with Windows include dir\.
* zabbix\_agent role \- Fix for removal of wrong agent include directory \([https\://github\.com/ansible\-collections/community\.zabbix/issues/1236](https\://github\.com/ansible\-collections/community\.zabbix/issues/1236)\)
* zabbix\_agent role \- Fix reading existing psk
* zabbix\_agent role \- Fix role when zabbix\_agent\_listenip is undefined
* zabbix\_agent role \- Fix windows agent installation issue
* zabbix\_agent role \- Fixed logic problem that would break if anything other than PSK was used\.
* zabbix\_agent role \- Fixed missing setting for <em class="title-reference">zabbix\_agent\_persistentbuffer</em>
* zabbix\_agent role \- fix error when <code>zabbix\_agent\_tlsaccept</code> is not set
* zabbix\_agent role \- fix error when <code>zabbix\_agent\_tlsconnect</code> is not set
* zabbix\_agent role \- fix name of Zabbix Agent 2 config filename
* zabbix\_agent role \- in <code>zabbix\_agent\_interfaces</code> directly use <code>zabbix\_agent\_listenport</code>\, which does already contains the agent2 value if needed
* zabbix\_agent\, zabbix\_proxy\, and zabbix\_server roles \- Fixed problem with include file
* zabbix\_authentication \- fix inability to set passwd\_check\_rules to empty list
* zabbix\_authentication \- fix inability to update passwd\_check\_rules
* zabbix\_host \- delete denied parameter from interfaces
* zabbix\_proxy Role \- Fixed TLS configuration
* zabbix\_repo Role \- Fixes error that attempts to use the repo name as a variable\.
* zabbix\_server Role \- fixed creating TimescaleDB hypertables for Zabbix 7\.0
* zabbix\_web \- make the FPM socket group\-writable so the web server can properly forward requests to the FPM process

<a id="containers-podman-4"></a>
#### containers\.podman

* Add missing parameters for podman container quadlet
* Add new options for podman\_network
* Add option to specify kube file content in module
* Add quadlet file mode option to specify file permission
* Add secret to login module
* CI \- Add images removal for tests
* CI \- Fix podman CI test container images
* CI \- add ignore list for Ansible sanity for 2\.19
* CI \- bump artifacts versions for GHactions
* CI \- change k8s\.gcr\.io to registry\.k8s\.io in tests
* CI \- fix Podman search of invalid image
* Disable idempotency for pod\_id\_file
* Don\'t check image availability in Quadlet
* Fix command idempotency with quotes
* Fix health\-startup\-cmd
* Fix idempotency for empty values
* Fix idempotency for pod with 0\.0\.0\.0
* Fix idempotency for pods in case of systemd generation
* Fix idempotency for systemd generations
* Fix issue with pushing podman image to repo name and org
* Fix logic in Podman images
* Fix max\_size idempotency issue
* Fix missing entries in network quadlet generated file
* Fix podman image permissions issue and runlable test
* Fix quadlet parameters for restart policy
* Fix quadlet parameters when container uses rootfs
* Fix transports issues in podman\_image
* Fix typo in quadlet generator
* Fix unsupported pull policy in example on podman\_container\.py
* Idempotency improvements
* don\'t document quadlet\_dir as required when setting state\=quadlet
* fix for tls\_verify being ignored
* fix quadlet cmd\_args append mistake
* fix\(\#747\) set correct HealthCmd
* fix\(podman\_image\) \- skip empty volume items
* fix\(podman\_save\) \- always changed when force
* modify error and docs
* params gpus should be exit\_policy
* podman\_login does not support check\_mode

<a id="dellemc-enterprise-sonic-1"></a>
#### dellemc\.enterprise\_sonic

* ConnectionError \- Add the needed import of the Ansible ConnectionError exception class for all files where it was previously missing\. \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/445](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/445)\)\.
* Update regex search expression for \'not found\' error message in httpapi/sonic\.py \'edit\_config\' method \([https\://github\.com/ansible\-collection/dellemc\.enterprise\_sonic/pull/443](https\://github\.com/ansible\-collection/dellemc\.enterprise\_sonic/pull/443)\)\.
* sonic\_bfd \- Fix BFD states implementation bug \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/383](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/383)\)\.
* sonic\_bgp\_neighbors \- Fix issues with deleted state \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/335](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/335)\)\.
* sonic\_copp \- Fix CoPP states implementation bug \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/381](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/381)\)\.
* sonic\_interfaces \- Fix exception when gathering facts \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/377](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/377)\)\.
* sonic\_interfaces \- Fix replaced and overridden state handling for Loopback interfaces \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/364](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/364)\)\.
* sonic\_l2\_interfaces \- Fix exception when gathering facts \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/410](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/410)\)\.
* sonic\_l3\_interfaces \- Fix replaced state handling \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/431](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/431)\)\.
* sonic\_mac \- Fix MAC states implementation bug \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/383](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/383)\)\.
* sonic\_prefix\_lists \- Fix idempotency failure \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/354](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/354)\)\.
* sonic\_prefix\_lists \- Fix replaced state handling \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/354](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/354)\)\.
* sonic\_qos\_pfc \- Add back accidentally deleted line of code  \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/391](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/391)\)\.
* sonic\_static\_routes \- Fix static routes states implementation bug \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/383](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/383)\)\.
* sonic\_system \- Catch the ConnectionError exception caused by unconditional fetching of auditd and ip loadshare hash algorithm configuration\, and return empty configuration instead of allowing the uncaught exception to abort all \"system\" operations on SONiC images older than version 4\.4\.0 \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/441](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/441)\)\.
* sonic\_vlans \- Fix exception when gathering facts \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/377](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/377)\)\.

<a id="dellemc-openmanage-15"></a>
#### dellemc\.openmanage

* Resolved the issue in <code>idrac\_certificates</code> module where subject\_alt\_name parameter was only accepting first item in list\. \([https\://github\.com/dell/dellemc\-openmanage\-ansible\-modules/issues/584](https\://github\.com/dell/dellemc\-openmanage\-ansible\-modules/issues/584)\)
* Resolved the issue in <code>idrac\_gather\_facts</code> role where it was failing for some component in iDRAC8\. \([https\://github\.com/dell/dellemc\-openmanage\-ansible\-modules/issues/718](https\://github\.com/dell/dellemc\-openmanage\-ansible\-modules/issues/718)\)
* Resolved the issue in <code>idrac\_reset</code> module where it fails when iDRAC is in busy state\. \([https\://github\.com/dell/dellemc\-openmanage\-ansible\-modules/issues/652](https\://github\.com/dell/dellemc\-openmanage\-ansible\-modules/issues/652)\)
* Resolved the issue in <code>idrac\_virtual\_media</code> module where the Authorization request header was included in the request\. \([https\://github\.com/dell/dellemc\-openmanage\-ansible\-modules/issues/612](https\://github\.com/dell/dellemc\-openmanage\-ansible\-modules/issues/612)\)
* Resolved the issue in <code>ome\_application\_certificate</code> module related to a padding error in generated CSR file\. \([https\://github\.com/dell/dellemc\-openmanage\-ansible\-modules/issues/370](https\://github\.com/dell/dellemc\-openmanage\-ansible\-modules/issues/370)\)
* idrac\_storage\_volume \- Issue\(290766\) \- The module will report success instead of showing failure for new virtual creation on the BOSS\-N1 controller if a virtual disk is already present on the same controller\.
* idrac\_support\_assist \- Issue\(308550\) \- This module fails when the NFS share path contains sub directory\.
* ome\_diagnostics \- Issue\(279193\) \- Export of SupportAssist collection logs to the share location fails on OME version 4\.0\.0\.

<a id="f5networks-f5-modules-5"></a>
#### f5networks\.f5\_modules

* bigip\_imish\_config \- fixed a bug that resulted in incomplete config when using BGV route domain

<a id="fortinet-fortimanager-8"></a>
#### fortinet\.fortimanager

* Added more description in the documentation\.
* Deleted 9 fmgr\_switchcontroller\_managedswitch\_\* modules\. Will support them in FortiManager Device Ansible\.
* Fixed Bug in \"fmgr\_fact\"
* Improved documentation\.
* Improved fmgr\_fact\, fmgr\_clone\, fmgr\_move\.

<a id="fortinet-fortios-5"></a>
#### fortinet\.fortios

* Fix some issues in sanity test\.
* Fix the issue using diff feature in check\_mode\.
* Github
* Github issue
* Mantis
* Return invalid json content instead of error while adding redundant comma at the end of the last variable in <em class="title-reference">fortios\_json\_generic</em>\.
* mantis issue

<a id="google-cloud-6"></a>
#### google\.cloud

* ansible\-lint \- remove jinja templates from test assertions
* gcp\_kms\_filters \- add DOCUMENTATION string
* gcp\_secret\_manager \- make an f\-string usage backward compatible

<a id="hetzner-hcloud-4"></a>
#### hetzner\.hcloud

* server \- Keep <em class="title-reference">force\_upgrade</em> deprecated alias for another major version\.
* server \- Wait up to 30 minutes for every action returned from server create

<a id="ibm-storage-virtualize-8"></a>
#### ibm\.storage\_virtualize

* ibm\_svc\_manage\_callhome \- Added support to change a subset of proxy settings
* ibm\_svc\_manage\_callhome \- Setting censorcallhome does not work
* ibm\_svc\_utils \- REST API timeout due to slow response
* ibm\_svc\_utils \- Return correct error in case of error code 500

<a id="infoblox-nios-modules-3"></a>
#### infoblox\.nios\_modules

* Adjusted unit test assertions for Mock\.called\_once\_with\.
* Fixed an issue in the <em class="title-reference">nios\_host\_record</em> module where the <em class="title-reference">mac</em> parameter was not handled correctly\.
* Fixed the update operation in the <em class="title-reference">nios\_network</em> module where the <em class="title-reference">network</em> parameter was not handled correctly\.
* Omits DNS view from filter criteria when renaming a host object and DNS is bypassed\. \([https\://github\.com/infobloxopen/infoblox\-ansible/issues/230](https\://github\.com/infobloxopen/infoblox\-ansible/issues/230)\)
* nios\_host\_record \- rename logic included DNS view in filter criteria\, even when DNS had been bypassed\.

<a id="inspur-ispim"></a>
#### inspur\.ispim

* Change the ansible version in meta/runtime\.yml to 2\.15\.0\([https\://github\.com/ispim/inspur\.ispim/pull/37](https\://github\.com/ispim/inspur\.ispim/pull/37)\)\.
* Remove venv files that were accidentally bundled in 2\.2\.1 \([https\://github\.com/ispim/inspur\.ispim/pull/35](https\://github\.com/ispim/inspur\.ispim/pull/35)\)\.

<a id="junipernetworks-junos-2"></a>
#### junipernetworks\.junos

* Fix the lag\_interfaces facts for gigether supported model\.

<a id="kaytus-ksmanage-1"></a>
#### kaytus\.ksmanage

* Edit ansible devel version tests to our CI test scripts \([https\://github\.com/ieisystem/kaytus\.ksmanage/pull/26](https\://github\.com/ieisystem/kaytus\.ksmanage/pull/26)\)\.
* Modify the title information in changelogs config\.yaml \([https\://github\.com/ieisystem/kaytus\.ksmanage/pull/25](https\://github\.com/ieisystem/kaytus\.ksmanage/pull/25)\)\.
* Remove venv files that were accidentally bundled in 1\.2\.2\([https\://github\.com/ieisystem/kaytus\.ksmanage/pull/23](https\://github\.com/ieisystem/kaytus\.ksmanage/pull/23)\)\.

<a id="kubernetes-core-9"></a>
#### kubernetes\.core

* Resolve Collections util resource discovery fails when complex subresources present \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/676](https\://github\.com/ansible\-collections/kubernetes\.core/pull/676)\)\.
* align <em class="title-reference">helmdiff\_check\(\)</em> function commandline rendering with the <em class="title-reference">deploy\(\)</em> function \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/670](https\://github\.com/ansible\-collections/kubernetes\.core/pull/670)\)\.
* avoid unsafe conditions in integration tests \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/665](https\://github\.com/ansible\-collections/kubernetes\.core/pull/665)\)\.
* helm \- Helm version checks did not support RC versions\. They now accept any version tags\. \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/745](https\://github\.com/ansible\-collections/kubernetes\.core/pull/745)\)\.
* helm \- use <code>reuse\-values</code> when running <code>helm diff</code> command \([https\://github\.com/ansible\-collections/kubernetes\.core/issues/680](https\://github\.com/ansible\-collections/kubernetes\.core/issues/680)\)\.
* helm\_pull \- Apply no\_log\=True to pass\_credentials to silence false positive warning\. \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/796](https\://github\.com/ansible\-collections/kubernetes\.core/pull/796)\)\.
* integrations test helm\_kubeconfig \- set helm version to v3\.10\.3 to avoid incompatability with new bitnami charts \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/670](https\://github\.com/ansible\-collections/kubernetes\.core/pull/670)\)\.
* k8s\_drain \- Fix k8s\_drain does not wait for single pod \([https\://github\.com/ansible\-collections/kubernetes\.core/issues/769](https\://github\.com/ansible\-collections/kubernetes\.core/issues/769)\)\.
* k8s\_drain \- Fix k8s\_drain runs into a timeout when evicting a pod which is part of a stateful set  \([https\://github\.com/ansible\-collections/kubernetes\.core/issues/792](https\://github\.com/ansible\-collections/kubernetes\.core/issues/792)\)\.
* kubeconfig option should not appear in module invocation log \([https\://github\.com/ansible\-collections/kubernetes\.core/issues/782](https\://github\.com/ansible\-collections/kubernetes\.core/issues/782)\)\.
* kustomize \- kustomize plugin fails with deprecation warnings \([https\://github\.com/ansible\-collections/kubernetes\.core/issues/639](https\://github\.com/ansible\-collections/kubernetes\.core/issues/639)\)\.
* waiter \- Fix waiting for daemonset when desired number of pods is 0\. \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/756](https\://github\.com/ansible\-collections/kubernetes\.core/pull/756)\)\.

<a id="lowlydba-sqlserver-5"></a>
#### lowlydba\.sqlserver

* Include warning logs in failure output for the restore module to indicate root causes \([https\://github\.com/lowlydba/lowlydba\.sqlserver/pull/266](https\://github\.com/lowlydba/lowlydba\.sqlserver/pull/266)\)\.
* fixed the expected type of the ip\_address\, subnet\_ip\, and subnet\_mask parameters to be lists instead of strings \(lowlydba\.sqlserver\.ag\_listener\)

<a id="microsoft-ad-5"></a>
#### microsoft\.ad

* Fix <code>microsoft\.ad\.debug\_ldap\_client</code> documentation problem so it appears in the <code>ansible\-doc</code> plugin list and online documentation\.
* Removed usages of the python call <code>datetime\.datetime\.utcnow\(\)</code> in favour of <code>datetime\.datetime\.now\(datetime\.timezone\.utc\)</code>\. The original method is now deprecated in Python 3\.12 and will be removed in a later version\.
* group \- fix error when creating a group with no members explicitly set \- [https\://github\.com/ansible\-collections/microsoft\.ad/issues/141](https\://github\.com/ansible\-collections/microsoft\.ad/issues/141)
* ldap \- Filter out managed service accounts in the default LDAP filter used\. The <code>filter\_without\_computer</code> can be used to disable the default filter if needed\.
* membership \- allow domain join with hostname change if the account for that host already exists \- [https\://github\.com/ansible\-collections/microsoft\.ad/pull/145](https\://github\.com/ansible\-collections/microsoft\.ad/pull/145)
* microsoft\.ad\.computer \- Added fallback <code>identity</code> lookup for <code>sAMAccountName</code> with the <code>\$</code> suffix\. This ensures that finding the computer object will work with or without the <code>\$</code> suffix\. \- [https\://github\.com/ansible\-collections/microsoft\.ad/issues/124](https\://github\.com/ansible\-collections/microsoft\.ad/issues/124)
* microsoft\.ad\.group \- Fix setting group members of Builtin groups of a domain controller \- [https\://github\.com/ansible\-collections/microsoft\.ad/issues/130](https\://github\.com/ansible\-collections/microsoft\.ad/issues/130)
* microsoft\.ad\.membership \- Fix hostname check to work with hostnames longer than 15 characters long \- [https\://github\.com/ansible\-collections/microsoft\.ad/issues/113](https\://github\.com/ansible\-collections/microsoft\.ad/issues/113)
* microsoft\.ad\.user \- Fix issue when creating a new user account with <code>account\_locked\: false</code> \- [https\://github\.com/ansible\-collections/microsoft\.ad/issues/108](https\://github\.com/ansible\-collections/microsoft\.ad/issues/108)

<a id="netapp-ontap-6"></a>
#### netapp\.ontap

* na\_ontap\_export\_policy\_rule \- fix issue with idempotency in REST\.
* na\_ontap\_file\_security\_permissions \- set <em class="title-reference">apply\_to</em> as optional and default value as true\.
* na\_ontap\_flexcache \- add warning for flexcache relationship deletion in ZAPI\.
* na\_ontap\_qtree \- add warning for job still running for deletion operation in REST\, when wait\_for\_completion is not set\.
* na\_ontap\_quotas \- fix error with <em class="title-reference">quota\_target</em> while trying to set default user quota rule in REST\.
* na\_ontap\_rest\_info \- fixed issue with capturing error\.
* na\_ontap\_snapshot\_policy \- fix issue with idempotency when <em class="title-reference">snapmirror\_label</em> is set to empty in REST\.
* na\_ontap\_user\_role \- fix issue with setting multiple permissions with REST\.
* na\_ontap\_volume \- added error message while trying to modify efficiency configuration for a volume in REST\, when efficiency is disabled\.
* na\_ontap\_volume\_efficiency \- fix issue with modifying volume efficiency in REST\.

<a id="netapp-eseries-santricity"></a>
#### netapp\_eseries\.santricity

* Fixed pep8\, pylint\, and validate\-modules issues found by ansible\-test\.
* Updated outdated command in unit tests\.

<a id="netbox-netbox-4"></a>
#### netbox\.netbox

* Added ALLOWED\_QUERY\_PARAMS module\_bay by device [\#1228](https\://github\.com/netbox\-community/ansible\_modules/pull/1228)
* Added label to power outlet [\#1222](https\://github\.com/netbox\-community/ansible\_modules/pull/1222)
* Added power outlet type iec\-60320\-c21 to power outlet template and power outlet modules [\#1229](https\://github\.com/netbox\-community/ansible\_modules/issues/1229)
* Extend query param for parent\_location [\#1233](https\://github\.com/netbox\-community/ansible\_modules/issues/1233)
* If <em class="title-reference">fetch\_all</em> is <em class="title-reference">false</em>\, prefix lookup depends on site lookup\, so move it to secondary lookup \([https\://github\.com/netbox\-community/ansible\_modules/issues/733](https\://github\.com/netbox\-community/ansible\_modules/issues/733)\)

<a id="ngine-io-cloudstack-1"></a>
#### ngine\_io\.cloudstack

* Fixed a bug related to the new option <code>validate\_certs</code> \([https\://github\.com/ngine\-io/ansible\-collection\-cloudstack/pull/135](https\://github\.com/ngine\-io/ansible\-collection\-cloudstack/pull/135)\)\.

<a id="purestorage-flasharray-9"></a>
#### purestorage\.flasharray

* purefa\_dsrole \- Fix function name typo
* purefa\_dsrole \- Fix version check logic
* purefa\_hg \- Fix edge case with incorrectly deleted hostgroup when empty array sent for volumes or hosts
* purefa\_info \- Fix typo from PR
* purefa\_info \- Fixed issue trying to collect deleted volumes perfomance stats
* purefa\_info \- Resolve issue with performance stats trying to report for remote hosts
* purefa\_network \- Fix issue with clearing network interface addresses
* purefa\_network \- Resolve issue when setting a network port on a new array
* purefa\_pg \- Fix parameter name typo
* purefa\_pod \- Fix issue with pod not creating correctly
* purefa\_policy \- Enhanced idempotency for snapshot policy rules
* purefa\_subnet \- Initialize varaible correctly
* purefa\_syslog\_settings \- Initialize varaible correctly
* purefa\_volume \- Fix issue with creating volume using old Purity version \(6\.1\.19\)
* purefa\_volume \- Fixes <code>eradicate</code> so it doesn\'t report success when it hasn\'t actually eradicated
* purefa\_volume \- Fixes <code>volfact</code> response when in <code>check\_mode</code>
* purefa\_volume \- Fixes issue where malformed <code>volfact</code> will cause the <code>move</code> to apparently fail\.

<a id="purestorage-flashblade-5"></a>
#### purestorage\.flashblade

* purefb\_certs \- Fix issue with importing certificates
* purefb\_certs \- Fix parameter mispelling of <code>intermeadiate\_cert</code> to <code>intermediate\_cert</code>\. Keep original mispelling as an alias\.
* purefb\_ds \- Initialize variable correctly
* purefb\_fs \- Fix conflict with SMB mode and ACL safeguarding
* purefb\_fs \- Fix error checking for SMB parameter in non\-SMB filesystem
* purefb\_info \- Fix space reporting issue
* purefb\_policy \- Initialize variable correctly
* purefb\_ra \- Fix incorrect import statement
* purefb\_snap \- Fix issue with immeadiate remote snapshots not executing

<a id="theforeman-foreman-1"></a>
#### theforeman\.foreman

* callback plugin \- correctly catch facts with vault data and replace it with <code>ENCRYPTED\_VAULT\_VALUE\_NOT\_REPORTED</code>\, preventing <code>Object of type AnsibleVaultEncryptedUnicode is not JSON serializable</code> errors
* redhat\_manifest \- do not send empty JSON bodies in GET requests which confuse the portal sometimes \([https\://github\.com/theforeman/foreman\-ansible\-modules/issues/1768](https\://github\.com/theforeman/foreman\-ansible\-modules/issues/1768)\)

<a id="vmware-vmware-rest-7"></a>
#### vmware\.vmware\_rest

* Fixed grammatical error in vcenter\_rest\_log\_file parameter description
* README \- fixed various typos in documentation
* Removed the scenario guides which are pretty much unmaintained and\, therefor\, possibly outdated and misleading \([https\://github\.com/ansible\-collections/vmware\.vmware\_rest/pull/524](https\://github\.com/ansible\-collections/vmware\.vmware\_rest/pull/524)\)\.
* lookup \- fixed issue where searching for datacenter contents would throw an exception instead of returning expected results
* vcenter\_vm\_guest\_customization \- Fixed typos and spacing in the module examples

<a id="known-issues-6"></a>
### Known Issues

<a id="ansible-core-24"></a>
#### Ansible\-core

* ansible\-test \- When using ansible\-test containers with Podman on a Ubuntu 24\.04 host\, ansible\-test must be run as a non\-root user to avoid permission issues caused by AppArmor\.
* ansible\-test \- When using the Fedora 40 container with Podman on a Ubuntu 24\.04 host\, the <code>unix\-chkpwd</code> AppArmor profile must be disabled on the host to allow SSH connections to the container\.

<a id="ansible-netcommon-6"></a>
#### ansible\.netcommon

* libssh \- net\_put and net\_get fail when the destination file intended to be fetched is not present\.

<a id="community-docker-15"></a>
#### community\.docker

* docker\_container \- when specifying a MAC address for a container\'s network\, and the network is attached after container creation \(for example\, due to idempotency checks\)\, the MAC address is at least in some cases ignored by the Docker Daemon \([https\://github\.com/ansible\-collections/community\.docker/pull/933](https\://github\.com/ansible\-collections/community\.docker/pull/933)\)\.

<a id="community-general-32"></a>
#### community\.general

* jenkins\_node \- the module is not able to update offline message when node is already offline due to internally using toggleOffline API \([https\://github\.com/ansible\-collections/community\.general/pull/9084](https\://github\.com/ansible\-collections/community\.general/pull/9084)\)\.

<a id="dellemc-openmanage-16"></a>
#### dellemc\.openmanage

* idrac\_diagnostics \- Issue\(285322\) \- This module doesn\'t support export of diagnostics file to HTTP and HTTPS share via SOCKS proxy\.
* idrac\_firmware \- Issue\(279282\) \- This module does not support firmware update using HTTP\, HTTPS\, and FTP shares with authentication on iDRAC8\.
* idrac\_storage\_volume \- Issue\(290766\) \- The module will report success instead of showing failure for new virtual creation on the BOSS\-N1 controller if a virtual disk is already present on the same controller\.
* idrac\_support\_assist \- Issue\(308550\) \- This module fails when the NFS share path contains sub directory\.
* ome\_diagnostics \- Issue\(279193\) \- Export of SupportAssist collection logs to the share location fails on OME version 4\.0\.0\.
* ome\_smart\_fabric\_uplink \- Issue\(186024\) \- The module supported by OpenManage Enterprise Modular\, however it does not allow the creation of multiple uplinks of the same name\. If an uplink is created using the same name as an existing uplink\, then the existing uplink is modified\.

<a id="new-plugins-5"></a>
### New Plugins

<a id="filter-3"></a>
#### Filter

* community\.general\.keep\_keys \- Keep specific keys from dictionaries in a list\.
* community\.general\.remove\_keys \- Remove specific keys from dictionaries in a list\.
* community\.general\.replace\_keys \- Replace specific keys in a list of dictionaries\.
* community\.general\.reveal\_ansible\_type \- Return input type\.

<a id="test"></a>
#### Test

* ansible\.builtin\.timedout \- did the task time out
* ansible\.builtin\.vaulted\_file \- Is this file an encrypted vault
* community\.general\.ansible\_type \- Validate input type\.

<a id="new-modules-7"></a>
### New Modules

<a id="ansible-core-25"></a>
#### Ansible\-core

<a id="lib"></a>
##### Lib

<a id="ansible-modules"></a>
###### Ansible\.Modules

* ansible\.builtin\.mount\_facts \- Retrieve mount information\.

<a id="amazon-aws-18"></a>
#### amazon\.aws

* amazon\.aws\.autoscaling\_instance \- manage instances associated with AWS AutoScaling Groups \(ASGs\)
* amazon\.aws\.autoscaling\_instance\_info \- describe instances associated with AWS AutoScaling Groups \(ASGs\)
* amazon\.aws\.ec2\_launch\_template\_info \- Gather information about launch templates and versions
* amazon\.aws\.ec2\_vpc\_egress\_igw\_info \- Gather information about AWS VPC Egress Only Internet gateway

<a id="check-point-mgmt-5"></a>
#### check\_point\.mgmt

* check\_point\.mgmt\.cp\_mgmt\_add\_custom\_trusted\_ca\_certificate \- Create new custom trusted CA certificate\.
* check\_point\.mgmt\.cp\_mgmt\_add\_outbound\_inspection\_certificate \- Add outbound\-inspection\-certificate
* check\_point\.mgmt\.cp\_mgmt\_cp\_trusted\_ca\_certificate\_facts \- Retrieve existing Check Point trusted CA certificate objects facts on Checkpoint devices\.
* check\_point\.mgmt\.cp\_mgmt\_custom\_trusted\_ca\_certificate\_facts \- Retrieve existing custom trusted CA certificate objects facts on Checkpoint devices\.
* check\_point\.mgmt\.cp\_mgmt\_data\_type\_compound\_group \- Manages data\-type\-compound\-group objects on Checkpoint over Web Services API
* check\_point\.mgmt\.cp\_mgmt\_data\_type\_compound\_group\_facts \- Get data\-type\-compound\-group objects facts on Checkpoint over Web Services API
* check\_point\.mgmt\.cp\_mgmt\_data\_type\_file\_attributes \- Manages data\-type\-file\-attributes objects on Checkpoint over Web Services API
* check\_point\.mgmt\.cp\_mgmt\_data\_type\_file\_attributes\_facts \- Get data\-type\-file\-attributes objects facts on Checkpoint over Web Services API
* check\_point\.mgmt\.cp\_mgmt\_data\_type\_file\_group\_facts \- Get data\-type\-file\-group objects facts on Checkpoint over Web Services API
* check\_point\.mgmt\.cp\_mgmt\_data\_type\_group \- Manages data\-type\-group objects on Checkpoint over Web Services API
* check\_point\.mgmt\.cp\_mgmt\_data\_type\_group\_facts \- Get data\-type\-group objects facts on Checkpoint over Web Services API
* check\_point\.mgmt\.cp\_mgmt\_data\_type\_keywords \- Manages data\-type\-keywords objects on Checkpoint over Web Services API
* check\_point\.mgmt\.cp\_mgmt\_data\_type\_keywords\_facts \- Get data\-type\-keywords objects facts on Checkpoint over Web Services API
* check\_point\.mgmt\.cp\_mgmt\_data\_type\_patterns \- Manages data\-type\-patterns objects on Checkpoint over Web Services API
* check\_point\.mgmt\.cp\_mgmt\_data\_type\_patterns\_facts \- Get data\-type\-patterns objects facts on Checkpoint over Web Services API
* check\_point\.mgmt\.cp\_mgmt\_data\_type\_traditional\_group \- Manages data\-type\-traditional\-group objects on Checkpoint over Web Services API
* check\_point\.mgmt\.cp\_mgmt\_data\_type\_traditional\_group\_facts \- Get data\-type\-traditional\-group objects facts on Checkpoint over Web Services API
* check\_point\.mgmt\.cp\_mgmt\_data\_type\_weighted\_keywords \- Manages data\-type\-weighted\-keywords objects on Checkpoint over Web Services API
* check\_point\.mgmt\.cp\_mgmt\_data\_type\_weighted\_keywords\_facts \- Get data\-type\-weighted\-keywords objects facts on Checkpoint over Web Services API
* check\_point\.mgmt\.cp\_mgmt\_delete\_custom\_trusted\_ca\_certificate \- Delete existing custom trusted CA certificate using name or uid\.
* check\_point\.mgmt\.cp\_mgmt\_delete\_infinity\_idp \- Delete Infinity Identity Provider from the Infinity Portal using object name or uid\.
* check\_point\.mgmt\.cp\_mgmt\_delete\_infinity\_idp\_object \- Delete users/groups/machines from the Identity Provider using object name or uid\.
* check\_point\.mgmt\.cp\_mgmt\_delete\_outbound\_inspection\_certificate \- Delete outbound\-inspection\-certificate
* check\_point\.mgmt\.cp\_mgmt\_external\_trusted\_ca \- Manages external\-trusted\-ca objects on Checkpoint over Web Services API
* check\_point\.mgmt\.cp\_mgmt\_external\_trusted\_ca\_facts \- Get external\-trusted\-ca objects facts on Checkpoint over Web Services API
* check\_point\.mgmt\.cp\_mgmt\_https\_rule \- Manages https\-rule objects on Checkpoint over Web Services API
* check\_point\.mgmt\.cp\_mgmt\_https\_rule\_facts \- Get https\-rule objects facts on Checkpoint over Web Services API
* check\_point\.mgmt\.cp\_mgmt\_import\_outbound\_inspection\_certificate \- Import Outbound Inspection certificate for HTTPS inspection\.
* check\_point\.mgmt\.cp\_mgmt\_infinity\_idp\_facts \- Get Infinity Identity Provider objects facts from the Infinity Portal\.
* check\_point\.mgmt\.cp\_mgmt\_infinity\_idp\_object\_facts \- Retrieve users/groups/machines objects facts from the Identity Provider\.
* check\_point\.mgmt\.cp\_mgmt\_interface \- Manages interface objects on Checkpoint over Web Services API
* check\_point\.mgmt\.cp\_mgmt\_interface\_facts \- Get interface objects facts on Checkpoint over Web Services API
* check\_point\.mgmt\.cp\_mgmt\_limit \- Manages limit objects on Checkpoint over Web Services API
* check\_point\.mgmt\.cp\_mgmt\_limit\_facts \- Get limit objects facts on Checkpoint over Web Services API
* check\_point\.mgmt\.cp\_mgmt\_mobile\_access\_profile\_rule \- Manages mobile\-access\-profile\-rule objects on Checkpoint over Web Services API
* check\_point\.mgmt\.cp\_mgmt\_mobile\_access\_profile\_rule\_facts \- Get mobile\-access\-profile\-rule objects facts on Checkpoint over Web Services API
* check\_point\.mgmt\.cp\_mgmt\_mobile\_access\_profile\_section \- Manages mobile\-access\-profile\-section objects on Checkpoint over Web Services API
* check\_point\.mgmt\.cp\_mgmt\_mobile\_access\_rule \- Manages mobile\-access\-rule objects on Checkpoint over Web Services API
* check\_point\.mgmt\.cp\_mgmt\_mobile\_access\_rule\_facts \- Get mobile\-access\-rule objects facts on Checkpoint over Web Services API
* check\_point\.mgmt\.cp\_mgmt\_mobile\_access\_section \- Manages mobile\-access\-section objects on Checkpoint over Web Services API
* check\_point\.mgmt\.cp\_mgmt\_mobile\_profile \- Manages mobile\-profile objects on Checkpoint over Web Services API
* check\_point\.mgmt\.cp\_mgmt\_mobile\_profile\_facts \- Get mobile\-profile objects facts on Checkpoint over Web Services API
* check\_point\.mgmt\.cp\_mgmt\_multiple\_key\_exchanges \- Manages multiple\-key\-exchanges objects on Checkpoint over Web Services API
* check\_point\.mgmt\.cp\_mgmt\_multiple\_key\_exchanges\_facts \- Get multiple\-key\-exchanges objects facts on Checkpoint over Web Services API
* check\_point\.mgmt\.cp\_mgmt\_network\_probe \- Manages network\-probe objects on Checkpoint over Web Services API
* check\_point\.mgmt\.cp\_mgmt\_network\_probe\_facts \- Get network\-probe objects facts on Checkpoint over Web Services API
* check\_point\.mgmt\.cp\_mgmt\_opsec\_trusted\_ca \- Manages opsec\-trusted\-ca objects on Checkpoint over Web Services API
* check\_point\.mgmt\.cp\_mgmt\_opsec\_trusted\_ca\_facts \- Get opsec\-trusted\-ca objects facts on Checkpoint over Web Services API
* check\_point\.mgmt\.cp\_mgmt\_outbound\_inspection\_certificate\_facts \- Get outbound\-inspection\-certificate objects facts on Checkpoint over Web Services API
* check\_point\.mgmt\.cp\_mgmt\_override\_categorization \- Manages override\-categorization objects on Checkpoint over Web Services API
* check\_point\.mgmt\.cp\_mgmt\_override\_categorization\_facts \- Get override\-categorization objects facts on Checkpoint over Web Services API
* check\_point\.mgmt\.cp\_mgmt\_passcode\_profile \- Manages passcode\-profile objects on Checkpoint over Web Services API
* check\_point\.mgmt\.cp\_mgmt\_passcode\_profile\_facts \- Get passcode\-profile objects facts on Checkpoint over Web Services API
* check\_point\.mgmt\.cp\_mgmt\_resource\_cifs \- Manages resource\-cifs objects on Checkpoint over Web Services API
* check\_point\.mgmt\.cp\_mgmt\_resource\_cifs\_facts \- Get resource\-cifs objects facts on Checkpoint over Web Services API
* check\_point\.mgmt\.cp\_mgmt\_resource\_ftp \- Manages resource\-ftp objects on Checkpoint over Web Services API
* check\_point\.mgmt\.cp\_mgmt\_resource\_ftp\_facts \- Get resource\-ftp objects facts on Checkpoint over Web Services API
* check\_point\.mgmt\.cp\_mgmt\_resource\_smtp \- Manages resource\-smtp objects on Checkpoint over Web Services API
* check\_point\.mgmt\.cp\_mgmt\_resource\_smtp\_facts \- Get resource\-smtp objects facts on Checkpoint over Web Services API
* check\_point\.mgmt\.cp\_mgmt\_resource\_uri \- Manages resource\-uri objects on Checkpoint over Web Services API
* check\_point\.mgmt\.cp\_mgmt\_resource\_uri\_facts \- Get resource\-uri objects facts on Checkpoint over Web Services API
* check\_point\.mgmt\.cp\_mgmt\_set\_app\_control\_advanced\_settings \- Edit Application Control \& URL Filtering Blades\' Settings\.
* check\_point\.mgmt\.cp\_mgmt\_set\_content\_awareness\_advanced\_settings \- Edit Content Awareness Blades\' Settings\.
* check\_point\.mgmt\.cp\_mgmt\_set\_cp\_trusted\_ca\_certificate \- Edit existing Check Point trusted CA certificate using name or uid\.
* check\_point\.mgmt\.cp\_mgmt\_set\_gateway\_global\_use \- Enable or disable global usage on a specific target\.
* check\_point\.mgmt\.cp\_mgmt\_set\_https\_advanced\_settings \- Configure advanced settings for HTTPS Inspection\.
* check\_point\.mgmt\.cp\_mgmt\_set\_internal\_trusted\_ca \- Edit existing Internal CA object\.
* check\_point\.mgmt\.cp\_mgmt\_set\_outbound\_inspection\_certificate \- Edit outbound\-inspection\-certificate
* check\_point\.mgmt\.cp\_mgmt\_show\_app\_control\_advanced\_settings \- Show Application Control \& URL Filtering Blades\' Settings\.
* check\_point\.mgmt\.cp\_mgmt\_show\_content\_awareness\_advanced\_settings \- Show Content Awareness Blades\' Settings\.
* check\_point\.mgmt\.cp\_mgmt\_show\_gateway\_capabilities \- Show supported Check Point Gateway capabilities such as versions\, hardwares\, platforms and blades\.
* check\_point\.mgmt\.cp\_mgmt\_show\_gateway\_global\_use \- Show global usage of a specific target\.
* check\_point\.mgmt\.cp\_mgmt\_show\_https\_advanced\_settings \- Show advanced settings for HTTPS Inspection\.
* check\_point\.mgmt\.cp\_mgmt\_show\_internal\_trusted\_ca \- Retrieve existing Internal CA object\.
* check\_point\.mgmt\.cp\_mgmt\_show\_last\_published\_session \- Shows the last published session\.
* check\_point\.mgmt\.cp\_mgmt\_show\_mobile\_access\_profile\_section \- Retrieve existing Mobile Access Profile section using section name or uid\.
* check\_point\.mgmt\.cp\_mgmt\_show\_mobile\_access\_section \- Retrieve existing Mobile Access section using section name or uid\.
* check\_point\.mgmt\.cp\_mgmt\_verify\_management\_license \- Check how many Security Gateway objects the Management Server license supports\.
* check\_point\.mgmt\.cp\_mgmt\_vsx\_provisioning\_tool \- Run the VSX provisioning tool with the specified parameters\.

<a id="cisco-iosxr-6"></a>
#### cisco\.iosxr

* cisco\.iosxr\.iosxr\_route\_maps \- Resource module to configure route maps\.

<a id="community-docker-16"></a>
#### community\.docker

* community\.docker\.docker\_compose\_v2\_exec \- Run command in a container of a Compose service\.
* community\.docker\.docker\_compose\_v2\_run \- Run command in a new container of a Compose service\.

<a id="community-general-33"></a>
#### community\.general

* community\.general\.bootc\_manage \- Bootc Switch and Upgrade\.
* community\.general\.consul\_agent\_check \- Add\, modify\, and delete checks within a consul cluster\.
* community\.general\.consul\_agent\_service \- Add\, modify and delete services within a consul cluster\.
* community\.general\.django\_check \- Wrapper for C\(django\-admin check\)\.
* community\.general\.django\_createcachetable \- Wrapper for C\(django\-admin createcachetable\)\.
* community\.general\.homebrew\_services \- Services manager for Homebrew\.
* community\.general\.ipa\_getkeytab \- Manage keytab file in FreeIPA\.
* community\.general\.jenkins\_node \- Manage Jenkins nodes\.
* community\.general\.keycloak\_component \- Allows administration of Keycloak components via Keycloak API\.
* community\.general\.keycloak\_realm\_keys\_metadata\_info \- Allows obtaining Keycloak realm keys metadata via Keycloak API\.
* community\.general\.keycloak\_userprofile \- Allows managing Keycloak User Profiles\.
* community\.general\.krb\_ticket \- Kerberos utils for managing tickets\.
* community\.general\.one\_vnet \- Manages OpenNebula virtual networks\.
* community\.general\.zypper\_repository\_info \- List Zypper repositories\.

<a id="community-grafana-6"></a>
#### community\.grafana

* community\.grafana\.grafana\_contact\_point \- Manage Grafana Contact Points

<a id="community-zabbix-9"></a>
#### community\.zabbix

* community\.zabbix\.zabbix\_mfa \- Create/update/delete Zabbix MFA method

<a id="containers-podman-5"></a>
#### containers\.podman

* containers\.podman\.podman\_container\_copy \- Copy file to or from a container
* containers\.podman\.podman\_search \- Search for remote images using podman

<a id="dellemc-enterprise-sonic-2"></a>
#### dellemc\.enterprise\_sonic

* dellemc\.enterprise\_sonic\.sonic\_ldap \- Configure global LDAP server settings on SONiC\.
* dellemc\.enterprise\_sonic\.sonic\_login\_lockout \- Manage Global Login Lockout configurations on SONiC\.
* dellemc\.enterprise\_sonic\.sonic\_mgmt\_servers \- Manage management servers configuration on SONiC\.
* dellemc\.enterprise\_sonic\.sonic\_ospf\_area \- configure OSPF area settings on SONiC\.
* dellemc\.enterprise\_sonic\.sonic\_ospfv2 \- Configure global OSPFv2 protocol settings on SONiC\.
* dellemc\.enterprise\_sonic\.sonic\_ospfv2\_interfaces \- Configure OSPFv2 interface mode protocol settings on SONiC\.
* dellemc\.enterprise\_sonic\.sonic\_pim\_global \- Manage global PIM configurations on SONiC\.
* dellemc\.enterprise\_sonic\.sonic\_pim\_interfaces \- Manage interface\-specific PIM configurations on SONiC\.
* dellemc\.enterprise\_sonic\.sonic\_poe \- Manage PoE configuration on SONiC\.
* dellemc\.enterprise\_sonic\.sonic\_qos\_buffer \- Manage QoS buffer configuration on SONiC\.
* dellemc\.enterprise\_sonic\.sonic\_qos\_interfaces \- Manage QoS interfaces configuration on SONiC\.
* dellemc\.enterprise\_sonic\.sonic\_qos\_maps \- Manage QoS maps configuration on SONiC\.
* dellemc\.enterprise\_sonic\.sonic\_qos\_pfc \- Manage QoS PFC configuration on SONiC\.
* dellemc\.enterprise\_sonic\.sonic\_qos\_scheduler \- Manage QoS scheduler configuration on SONiC\.
* dellemc\.enterprise\_sonic\.sonic\_qos\_wred \- Manage QoS WRED profiles configuration on SONiC\.
* dellemc\.enterprise\_sonic\.sonic\_roce \- Manage RoCE QoS configuration on SONiC\.
* dellemc\.enterprise\_sonic\.sonic\_sflow \- configure sflow settings on SONiC\.
* dellemc\.enterprise\_sonic\.sonic\_vrrp \- Configure VRRP protocol settings on SONiC\.

<a id="dellemc-openmanage-17"></a>
#### dellemc\.openmanage

* dellemc\.openmanage\.ome\_session \- This module allows you to create and delete sessions on OpenManage Enterprise and OpenManage Enterprise Modular\.

<a id="fortinet-fortimanager-9"></a>
#### fortinet\.fortimanager

* fortinet\.fortimanager\.fmgr\_extensioncontroller\_extenderprofile\_wifi \- FortiExtender wifi configuration\.
* fortinet\.fortimanager\.fmgr\_extensioncontroller\_extenderprofile\_wifi\_radio1 \- Radio\-1 config for Wi\-Fi 2\.
* fortinet\.fortimanager\.fmgr\_extensioncontroller\_extenderprofile\_wifi\_radio2 \- Radio\-2 config for Wi\-Fi 5GHz
* fortinet\.fortimanager\.fmgr\_firewall\_sslsshprofile\_echoutersni \- ClientHelloOuter SNIs to be blocked\.
* fortinet\.fortimanager\.fmgr\_fmg\_sasemanager\_settings \- Fmg sase manager settings
* fortinet\.fortimanager\.fmgr\_fmg\_sasemanager\_status \- Fmg sase manager status
* fortinet\.fortimanager\.fmgr\_pm\_config\_pblock\_firewall\_proxypolicy \- Configure proxy policies\.
* fortinet\.fortimanager\.fmgr\_pm\_config\_pblock\_firewall\_proxypolicy\_sectionvalue \- Configure proxy policies\.
* fortinet\.fortimanager\.fmgr\_system\_admin\_user\_policyblock \- Policy block write access\.
* fortinet\.fortimanager\.fmgr\_system\_fmgcluster \- fmg clsuter\.
* fortinet\.fortimanager\.fmgr\_system\_fmgcluster\_peer \- Peer\.
* fortinet\.fortimanager\.fmgr\_system\_log\_ueba \- UEBAsettings\.
* fortinet\.fortimanager\.fmgr\_system\_npu\_icmpratectrl \- Configure the rate of ICMP messages generated by this FortiGate\.
* fortinet\.fortimanager\.fmgr\_user\_externalidentityprovider \- Configure external identity provider\.

<a id="infoblox-nios-modules-4"></a>
#### infoblox\.nios\_modules

* infoblox\.nios\_modules\.nios\_extensible\_attribute \- Configure Infoblox NIOS extensible attribute definition
* infoblox\.nios\_modules\.nios\_nsgroup\_delegation \- Configure InfoBlox DNS Nameserver Delegation Groups
* infoblox\.nios\_modules\.nios\_nsgroup\_forwardingmember \- Configure InfoBlox DNS Nameserver Forward/Stub Server Groups
* infoblox\.nios\_modules\.nios\_nsgroup\_forwardstubserver \- Configure InfoBlox DNS Nameserver Forwarding Member Groups
* infoblox\.nios\_modules\.nios\_nsgroup\_stubmember \- Configure InfoBlox DNS Nameserver Stub Member Groups

<a id="kaytus-ksmanage-2"></a>
#### kaytus\.ksmanage

* kaytus\.ksmanage\.edit\_system\_lock\_mode \- Set system lock mode information
* kaytus\.ksmanage\.system\_lock\_mode\_info \- Get system lock mode information

<a id="microsoft-ad-6"></a>
#### microsoft\.ad

* microsoft\.ad\.service\_account \- Manage Active Directory service account objects

<a id="netbox-netbox-5"></a>
#### netbox\.netbox

* netbox\.netbox\.netbox\_permission \- Creates or removes permissions from NetBox
* netbox\.netbox\.netbox\_token \- Creates or removes tokens from NetBox
* netbox\.netbox\.netbox\_tunnel \- Create\, update or delete tunnels within NetBox
* netbox\.netbox\.netbox\_tunnel\_group \- Create\, update or delete tunnel groups within NetBox
* netbox\.netbox\.netbox\_user \- Creates or removes users from NetBox
* netbox\.netbox\.netbox\_user\_group \- Creates or removes user groups from NetBox

<a id="purestorage-flasharray-10"></a>
#### purestorage\.flasharray

* purestorage\.flasharray\.purefa\_audits \- List FlashArray Audit Events
* purestorage\.flasharray\.purefa\_dsrole\_old \- Configure FlashArray Directory Service Roles \(pre\-6\.6\.3\)
* purestorage\.flasharray\.purefa\_sessions \- List FlashArray Sessions

<a id="purestorage-flashblade-6"></a>
#### purestorage\.flashblade

* purestorage\.flashblade\.purefb\_saml \- Manage FlashBlade SAML2 service and identity providers

<a id="theforeman-foreman-2"></a>
#### theforeman\.foreman

* theforeman\.foreman\.content\_import\_info \- List content imports
* theforeman\.foreman\.content\_import\_library \- Manage library content imports
* theforeman\.foreman\.content\_import\_repository \- Manage repository content imports
* theforeman\.foreman\.content\_import\_version \- Manage content view version content imports

<a id="unchanged-collections-7"></a>
### Unchanged Collections

* community\.ciscosmb \(still version 1\.0\.9\)
* community\.hashi\_vault \(still version 6\.2\.0\)
* community\.libvirt \(still version 1\.3\.0\)
* community\.rabbitmq \(still version 1\.3\.0\)
* community\.sap\_libs \(still version 1\.4\.2\)
* dellemc\.unity \(still version 2\.0\.0\)
* ibm\.spectrum\_virtualize \(still version 2\.0\.0\)
* infinidat\.infinibox \(still version 1\.4\.5\)
* openstack\.cloud \(still version 2\.2\.0\)
* ovirt\.ovirt \(still version 3\.2\.0\)
* sensu\.sensu\_go \(still version 1\.14\.0\)
