# Ansible 13 Release Notes

This changelog describes changes since Ansible 12\.0\.0\.

- <a href="#v13-0-0a1">v13\.0\.0a1</a>
    - <a href="#release-summary">Release Summary</a>
    - <a href="#removed-collections">Removed Collections</a>
    - <a href="#added-collections">Added Collections</a>
    - <a href="#ansible-core">Ansible\-core</a>
    - <a href="#included-collections">Included Collections</a>
    - <a href="#major-changes">Major Changes</a>
    - <a href="#minor-changes">Minor Changes</a>
    - <a href="#breaking-changes--porting-guide">Breaking Changes / Porting Guide</a>
    - <a href="#deprecated-features">Deprecated Features</a>
    - <a href="#removed-features-previously-deprecated">Removed Features \(previously deprecated\)</a>
    - <a href="#bugfixes">Bugfixes</a>
    - <a href="#known-issues">Known Issues</a>
    - <a href="#new-plugins">New Plugins</a>
    - <a href="#new-modules">New Modules</a>
    - <a href="#unchanged-collections">Unchanged Collections</a>

<a id="v13-0-0a1"></a>
## v13\.0\.0a1

- <a href="#release-summary">Release Summary</a>
- <a href="#removed-collections">Removed Collections</a>
- <a href="#added-collections">Added Collections</a>
- <a href="#ansible-core">Ansible\-core</a>
- <a href="#included-collections">Included Collections</a>
- <a href="#major-changes">Major Changes</a>
    - <a href="#ansible-core-1">Ansible\-core</a>
    - <a href="#community-vmware">community\.vmware</a>
    - <a href="#containers-podman">containers\.podman</a>
    - <a href="#dellemc-openmanage">dellemc\.openmanage</a>
- <a href="#minor-changes">Minor Changes</a>
    - <a href="#ansible-core-2">Ansible\-core</a>
    - <a href="#check-point-mgmt">check\_point\.mgmt</a>
    - <a href="#cisco-dnac">cisco\.dnac</a>
    - <a href="#community-general">community\.general</a>
    - <a href="#community-mysql">community\.mysql</a>
    - <a href="#community-routeros">community\.routeros</a>
    - <a href="#community-vmware-1">community\.vmware</a>
    - <a href="#community-zabbix">community\.zabbix</a>
    - <a href="#containers-podman-1">containers\.podman</a>
    - <a href="#google-cloud">google\.cloud</a>
    - <a href="#hitachivantara-vspone-block">hitachivantara\.vspone\_block</a>
    - <a href="#ibm-storage-virtualize">ibm\.storage\_virtualize</a>
    - <a href="#purestorage-flasharray">purestorage\.flasharray</a>
    - <a href="#purestorage-flashblade">purestorage\.flashblade</a>
    - <a href="#theforeman-foreman">theforeman\.foreman</a>
- <a href="#breaking-changes--porting-guide">Breaking Changes / Porting Guide</a>
    - <a href="#ansible-core-3">Ansible\-core</a>
    - <a href="#community-mysql-1">community\.mysql</a>
    - <a href="#community-vmware-2">community\.vmware</a>
    - <a href="#ibm-storage-virtualize-1">ibm\.storage\_virtualize</a>
- <a href="#deprecated-features">Deprecated Features</a>
    - <a href="#ansible-core-4">Ansible\-core</a>
    - <a href="#community-general-1">community\.general</a>
    - <a href="#community-vmware-3">community\.vmware</a>
    - <a href="#community-zabbix-1">community\.zabbix</a>
    - <a href="#purestorage-flasharray-1">purestorage\.flasharray</a>
- <a href="#removed-features-previously-deprecated">Removed Features \(previously deprecated\)</a>
    - <a href="#ansible-core-5">Ansible\-core</a>
    - <a href="#community-vmware-4">community\.vmware</a>
- <a href="#bugfixes">Bugfixes</a>
    - <a href="#ansible-core-6">Ansible\-core</a>
    - <a href="#cisco-meraki">cisco\.meraki</a>
    - <a href="#community-dns">community\.dns</a>
    - <a href="#community-general-2">community\.general</a>
    - <a href="#community-routeros-1">community\.routeros</a>
    - <a href="#community-vmware-5">community\.vmware</a>
    - <a href="#community-zabbix-2">community\.zabbix</a>
    - <a href="#containers-podman-2">containers\.podman</a>
    - <a href="#dellemc-openmanage-1">dellemc\.openmanage</a>
    - <a href="#google-cloud-1">google\.cloud</a>
    - <a href="#ibm-storage-virtualize-2">ibm\.storage\_virtualize</a>
    - <a href="#purestorage-flasharray-2">purestorage\.flasharray</a>
    - <a href="#purestorage-flashblade-1">purestorage\.flashblade</a>
- <a href="#known-issues">Known Issues</a>
    - <a href="#ansible-core-7">Ansible\-core</a>
    - <a href="#dellemc-openmanage-2">dellemc\.openmanage</a>
- <a href="#new-plugins">New Plugins</a>
    - <a href="#filter">Filter</a>
    - <a href="#inventory">Inventory</a>
- <a href="#new-modules">New Modules</a>
    - <a href="#check-point-mgmt-1">check\_point\.mgmt</a>
    - <a href="#community-general-3">community\.general</a>
    - <a href="#containers-podman-3">containers\.podman</a>
    - <a href="#hitachivantara-vspone-block-1">hitachivantara\.vspone\_block</a>
- <a href="#unchanged-collections">Unchanged Collections</a>

<a id="release-summary"></a>
### Release Summary

Release Date\: 2025\-09\-24

[Porting Guide](https\://docs\.ansible\.com/ansible/devel/porting\_guides\.html)

<a id="removed-collections"></a>
### Removed Collections

* ibm\.qradar \(previously included version\: 4\.0\.0\)

You can still install a removed collection manually with <code>ansible\-galaxy collection install \<name\-of\-collection\></code>\.

<a id="added-collections"></a>
### Added Collections

* ravendb\.ravendb \(version 1\.0\.3\)

<a id="ansible-core"></a>
### Ansible\-core

Ansible 13\.0\.0a1 contains ansible\-core version 2\.20\.0b1\.
This is a newer version than version 2\.19\.1 contained in the previous Ansible release\.

The changes are reported in the combined changelog below\.

<a id="included-collections"></a>
### Included Collections

If not mentioned explicitly\, the changes are reported in the combined changelog below\.

| Collection                  | Ansible 12.0.0 | Ansible 13.0.0a1 | Notes                                                                                                                        |
| --------------------------- | -------------- | ---------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| check_point.mgmt            | 6.4.1          | 6.5.0            |                                                                                                                              |
| cisco.dnac                  | 6.39.0         | 6.40.0           |                                                                                                                              |
| cisco.intersight            | 2.2.0          | 2.3.0            | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
| cisco.meraki                | 2.21.4         | 2.21.5           |                                                                                                                              |
| community.dns               | 3.3.2          | 3.3.3            |                                                                                                                              |
| community.general           | 11.2.1         | 11.3.0           |                                                                                                                              |
| community.mysql             | 3.15.0         | 4.0.0            |                                                                                                                              |
| community.routeros          | 3.10.0         | 3.11.0           |                                                                                                                              |
| community.vmware            | 5.7.2          | 6.0.0            |                                                                                                                              |
| community.zabbix            | 4.1.0          | 4.1.1            |                                                                                                                              |
| containers.podman           | 1.17.0         | 1.18.0           |                                                                                                                              |
| dellemc.openmanage          | 9.12.3         | 10.0.0           |                                                                                                                              |
| google.cloud                | 1.7.0          | 1.8.0            |                                                                                                                              |
| hitachivantara.vspone_block | 4.1.0          | 4.2.0            |                                                                                                                              |
| ibm.storage_virtualize      | 2.7.4          | 3.0.0            |                                                                                                                              |
| purestorage.flasharray      | 1.36.0         | 1.38.0           |                                                                                                                              |
| purestorage.flashblade      | 1.20.0         | 1.21.2           |                                                                                                                              |
| ravendb.ravendb             |                | 1.0.3            | The collection was added to Ansible                                                                                          |
| theforeman.foreman          | 5.5.0          | 5.6.0            |                                                                                                                              |

<a id="major-changes"></a>
### Major Changes

<a id="ansible-core-1"></a>
#### Ansible\-core

* ansible \- Add support for Python 3\.14\.
* ansible \- Drop support for Python 3\.11 on the controller\.
* ansible \- Drop support for Python 3\.8 on targets\.

<a id="community-vmware"></a>
#### community\.vmware

* Re\-use code from <code>vmware\.vmware</code> \([https\://github\.com/ansible\-collections/community\.vmware/pull/2459](https\://github\.com/ansible\-collections/community\.vmware/pull/2459)\)\.

<a id="containers-podman"></a>
#### containers\.podman

* Add inventory plugins for buildah and podman
* Add podman system connection modules

<a id="dellemc-openmanage"></a>
#### dellemc\.openmanage

* idrac\_certificate \- This role is enhanced to support iDRAC10\.
* idrac\_export\_server\_config\_profile \- This role is enhanced to support iDRAC10\.
* idrac\_firmware \- This role is enhanced to support iDRAC10\.
* idrac\_import\_server\_config\_profile \- This role is enhanced to support iDRAC10\.
* idrac\_license \- This module is enhanced to support iDRAC10\.
* idrac\_os\_deployment \- This module is enhanced to support iDRAC10\.
* idrac\_os\_deployment \- This role is enhanced to support iDRAC10\.
* idrac\_redfish\_storage\_controller \- This module is enhanced to support iDRAC10\.
* idrac\_server\_config\_profile \- This module is enhanced to support iDRAC10\.
* idrac\_storage\_controller \- This role is enhanced to support iDRAC10\.
* idrac\_storage\_volume \- This module is enhanced to support iDRAC10\.
* redfish\_firmware \- This role is enhanced to support iDRAC10\.
* redfish\_firmware\_rollback \- This module is enhanced to support iDRAC10\.
* redfish\_storage\_volume \- This module is enhanced to support iDRAC10\.
* redfish\_storage\_volume \- This role is enhanced to support iDRAC10\.

<a id="minor-changes"></a>
### Minor Changes

<a id="ansible-core-2"></a>
#### Ansible\-core

* Add tech preview play argument spec validation\, which can be enabled by setting the play keyword <code>validate\_argspec</code> to <code>True</code> or the name of an argument spec\. When <code>validate\_argspec</code> is set to <code>True</code>\, a play <code>name</code> is required and used as the argument spec name\. When enabled\, the argument spec is loaded from a file matching the pattern \<playbook\_name\>\.meta\.yml\. At minimum\, this file should contain <code>\{\"argument\_specs\"\: \{\"name\"\: \{\"options\"\: \{\}\}\}\}</code>\, where \"name\" is the name of the play or configured argument spec\.
* Added Univention Corporate Server as a part of Debian OS distribution family \([https\://github\.com/ansible/ansible/issues/85490](https\://github\.com/ansible/ansible/issues/85490)\)\.
* AnsibleModule \- Add temporary internal monkeypatch\-able hook to alter module result serialization by splitting serialization from <code>\_return\_formatted</code> into <code>\_record\_module\_result</code>\.
* Python type hints applied to <code>to\_text</code> and <code>to\_bytes</code> functions for better type hint interactions with code utilizing these functions\.
* ansible now warns if you use reserved tags that were only meant for selection and not for use in play\.
* ansible\-doc \- Return a more verbose error message when the <code>description</code> field is missing\.
* ansible\-doc \- show <code>notes</code>\, <code>seealso</code>\, and top\-level <code>version\_added</code> for role entrypoints \([https\://github\.com/ansible/ansible/pull/81796](https\://github\.com/ansible/ansible/pull/81796)\)\.
* ansible\-doc adds support for RETURN documentation to support doc fragment plugins
* ansible\-test \- Implement new authentication methods for accessing the Ansible Core CI service\.
* ansible\-test \- Improve formatting of generated coverage config file\.
* ansible\-test \- Removed support for automatic provisioning of obsolete instances for network\-integration tests\.
* ansible\-test \- Replace FreeBSD 14\.2 with 14\.3\.
* ansible\-test \- Replace RHEL 9\.5 with 9\.6\.
* ansible\-test \- Update Ubuntu containers\.
* ansible\-test \- Update pinned sanity test requirements\.
* ansible\-test \- Update test containers\.
* ansible\-test \- Upgrade Alpine 3\.21 to 3\.22\.
* ansible\-test \- Upgrade Fedora 41 to Fedora 42\.
* ansible\-test \- Upgrade to <code>coverage</code> version 7\.10\.6 for Python 3\.9 and later\.
* ansible\-test \- Use OS packages to satisfy controller requirements on FreeBSD 13\.5 during managed instance bootstrapping\.
* apt\_repository \- use correct debug method to print debug message\.
* blockinfile \- add new module option <code>encoding</code> to support files in encodings other than UTF\-8 \([https\://github\.com/ansible/ansible/pull/85291](https\://github\.com/ansible/ansible/pull/85291)\)\.
* deb822\_repository \- Add automatic installation of the <code>python3\-debian</code> package if it is missing by adding the parameter <code>install\_python\_debian</code>
* default callback plugin \- add option to configure indentation for JSON and YAML output \([https\://github\.com/ansible/ansible/pull/85497](https\://github\.com/ansible/ansible/pull/85497)\)\.
* encrypt \- check datatype of salt\_size in password\_hash filter\.
* fetch\_file \- add ca\_path and cookies parameter arguments \([https\://github\.com/ansible/ansible/issues/85172](https\://github\.com/ansible/ansible/issues/85172)\)\.
* include\_vars \- Raise an error if \'extensions\' is not specified as a list\.
* include\_vars \- Raise an error if \'ignore\_files\' is not specified as a list\.
* lineinfile \- add new module option <code>encoding</code> to support files in encodings other than UTF\-8 \([https\://github\.com/ansible/ansible/pull/84999](https\://github\.com/ansible/ansible/pull/84999)\)\.
* regex \- Document the match\_type fullmatch\.
* regex \- Ensure that match\_type is one of match\, fullmatch\, or search \([https\://github\.com/ansible/ansible/pull/85629](https\://github\.com/ansible/ansible/pull/85629)\)\.
* replace \- read/write files in text\-mode as unicode chars instead of as bytes and switch regex matching to unicode chars instead of bytes\. \([https\://github\.com/ansible/ansible/pull/85785](https\://github\.com/ansible/ansible/pull/85785)\)\.
* service\_facts \- handle keyerror exceptions with warning\.
* service\_facts \- warn user about missing service details instead of ignoring\.
* setup \- added new subkey <code>lvs</code> within each entry of <code>ansible\_facts\[\'vgs\'\]</code> to provide complete logical volume data scoped by volume group\. The top level <code>lvs</code> fact by comparison\, deduplicates logical volume names across volume groups and may be incomplete\. \([https\://github\.com/ansible/ansible/issues/85632](https\://github\.com/ansible/ansible/issues/85632)\)
* six \- bump six version from 1\.16\.0 to 1\.17\.0 \([https\://github\.com/ansible/ansible/issues/85408](https\://github\.com/ansible/ansible/issues/85408)\)\.
* stat module \- add SELinux context as a return value\, and add a new option to trigger this return\, which is False by default\. \([https\://github\.com/ansible/ansible/issues/85217](https\://github\.com/ansible/ansible/issues/85217)\)\.
* tags now warn when using reserved keywords\.
* wrapt \- bump version from 1\.15\.0 to 1\.17\.2 \([https\://github\.com/ansible/ansible/issues/85407](https\://github\.com/ansible/ansible/issues/85407)\)\.

<a id="check-point-mgmt"></a>
#### check\_point\.mgmt

* added new parameter \'ips\_settings\' to \'cp\_mgmt\_simple\_cluster\' and \'cp\_mgmt\_simple\_gateway\' modules\.
* added new parameter \'override\_vpn\_domains\' to \'cp\_mgmt\_set\_vpn\_community\_remote\_access\' module\.
* added new parameter \'show\_installation\_targets\' to \'cp\_mgmt\_package\_facts\' module\.
* added new parameters \(such as \'permanent\_tunnels\'\, excluded\_services\, etc\.\) to \'cp\_mgmt\_vpn\_community\_meshed\' and \'cp\_mgmt\_vpn\_community\_star\' modules\.

<a id="cisco-dnac"></a>
#### cisco\.dnac

* Added attribute \'slots\' in assurance\_icap\_settings\_workflow\_manager module
* Added attribute \'transit\_site\_hierarchy\' in sda\_fabric\_transits\_workflow\_manager module
* Added attributes \'wireless\_flooding\_enable\'\, \'resource\_guard\_enable\'\, \'flooding\_address\_assignment\'\, \'flooding\_address\' in sda\_fabric\_transits\_workflow\_manager module
* Changes in assurance\_icap\_settings\_workflow\_manager module
* Changes in assurance\_issue\_workflow\_manager module
* Changes in inventory\_workflow\_manager module
* Changes in network\_profile\_switching\_workflow\_manager module
* Changes in network\_settings\_workflow\_manager module
* Changes in sda\_fabric\_devices\_workflow\_manager module
* Changes in sda\_fabric\_sites\_zones\_workflow\_manager module
* Changes in sda\_fabric\_transits\_workflow\_manager module
* Changes in sda\_virtual\_networks\_workflow\_manager module
* Changes in template\_workflow\_manager module
* Removed attribute \'slot\' in assurance\_icap\_settings\_workflow\_manager module

<a id="community-general"></a>
#### community\.general

* android\_sdk \- minor refactor to improve readability \([https\://github\.com/ansible\-collections/community\.general/pull/10712](https\://github\.com/ansible\-collections/community\.general/pull/10712)\)\.
* django module utils \- simplify/consolidate the common settings for the command line \([https\://github\.com/ansible\-collections/community\.general/pull/10684](https\://github\.com/ansible\-collections/community\.general/pull/10684)\)\.
* django\_check \- rename parameter <code>database</code> to <code>databases</code>\, add alias for compatibility \([https\://github\.com/ansible\-collections/community\.general/pull/10700](https\://github\.com/ansible\-collections/community\.general/pull/10700)\)\.
* django\_check \- simplify/consolidate the common settings for the command line \([https\://github\.com/ansible\-collections/community\.general/pull/10684](https\://github\.com/ansible\-collections/community\.general/pull/10684)\)\.
* django\_createcachetable \- simplify/consolidate the common settings for the command line \([https\://github\.com/ansible\-collections/community\.general/pull/10684](https\://github\.com/ansible\-collections/community\.general/pull/10684)\)\.
* elasticsearch\_plugin \- minor refactor to improve readability \([https\://github\.com/ansible\-collections/community\.general/pull/10712](https\://github\.com/ansible\-collections/community\.general/pull/10712)\)\.
* filesize \- minor refactor to simplify string formatting \([https\://github\.com/ansible\-collections/community\.general/pull/10727](https\://github\.com/ansible\-collections/community\.general/pull/10727)\)\.
* github\_app\_access\_token lookup plugin \- support both <code>jwt</code> and <code>pyjwt</code> to avoid conflict with other modules requirements \([https\://github\.com/ansible\-collections/community\.general/issues/10299](https\://github\.com/ansible\-collections/community\.general/issues/10299)\)\.
* gitlab\_group\_access\_token \- add <code>planner</code> access level \([https\://github\.com/ansible\-collections/community\.general/pull/10679](https\://github\.com/ansible\-collections/community\.general/pull/10679)\)\.
* gitlab\_group\_access\_token \- add missing scopes \([https\://github\.com/ansible\-collections/community\.general/pull/10785](https\://github\.com/ansible\-collections/community\.general/pull/10785)\)\.
* gitlab\_group\_variable \- support masked\-and\-hidden variables \([https\://github\.com/ansible\-collections/community\.general/pull/10787](https\://github\.com/ansible\-collections/community\.general/pull/10787)\)\.
* gitlab\_label \- minor refactor to improve readability \([https\://github\.com/ansible\-collections/community\.general/pull/10711](https\://github\.com/ansible\-collections/community\.general/pull/10711)\)\.
* gitlab\_milestone \- minor refactor to improve readability \([https\://github\.com/ansible\-collections/community\.general/pull/10711](https\://github\.com/ansible\-collections/community\.general/pull/10711)\)\.
* gitlab\_project\_access\_token \- add <code>planner</code> access level \([https\://github\.com/ansible\-collections/community\.general/pull/10679](https\://github\.com/ansible\-collections/community\.general/pull/10679)\)\.
* gitlab\_project\_access\_token \- add missing scopes \([https\://github\.com/ansible\-collections/community\.general/pull/10785](https\://github\.com/ansible\-collections/community\.general/pull/10785)\)\.
* gitlab\_project\_variable \- support masked\-and\-hidden variables \([https\://github\.com/ansible\-collections/community\.general/pull/10787](https\://github\.com/ansible\-collections/community\.general/pull/10787)\)\.
* gitlab\_protected\_branch \- add <code>allow\_force\_push</code>\, <code>code\_owner\_approval\_required</code> \([https\://github\.com/ansible\-collections/community\.general/pull/10795](https\://github\.com/ansible\-collections/community\.general/pull/10795)\, [https\://github\.com/ansible\-collections/community\.general/issues/6432](https\://github\.com/ansible\-collections/community\.general/issues/6432)\, [https\://github\.com/ansible\-collections/community\.general/issues/10289](https\://github\.com/ansible\-collections/community\.general/issues/10289)\, [https\://github\.com/ansible\-collections/community\.general/issues/10765](https\://github\.com/ansible\-collections/community\.general/issues/10765)\)\.
* gitlab\_protected\_branch \- update protected branches if possible instead of recreating them \([https\://github\.com/ansible\-collections/community\.general/pull/10795](https\://github\.com/ansible\-collections/community\.general/pull/10795)\)\.
* iocage inventory plugin \- minor refactor to improve readability \([https\://github\.com/ansible\-collections/community\.general/pull/10712](https\://github\.com/ansible\-collections/community\.general/pull/10712)\)\.
* ipa\_host \- minor refactor to improve readability \([https\://github\.com/ansible\-collections/community\.general/pull/10711](https\://github\.com/ansible\-collections/community\.general/pull/10711)\)\.
* iptables\_state \- minor refactor to simplify string formatting \([https\://github\.com/ansible\-collections/community\.general/pull/10727](https\://github\.com/ansible\-collections/community\.general/pull/10727)\)\.
* keycloak\_realm \- add support for WebAuthn policy configuration options\, including both regular and passwordless WebAuthn policies \([https\://github\.com/ansible\-collections/community\.general/pull/10791](https\://github\.com/ansible\-collections/community\.general/pull/10791)\)\.
* lvg\_rename \- minor refactor to improve readability \([https\://github\.com/ansible\-collections/community\.general/pull/10711](https\://github\.com/ansible\-collections/community\.general/pull/10711)\)\.
* manageiq \- minor refactor to improve readability \([https\://github\.com/ansible\-collections/community\.general/pull/10712](https\://github\.com/ansible\-collections/community\.general/pull/10712)\)\.
* manageiq\_alert\_profiles \- minor refactor to improve readability \([https\://github\.com/ansible\-collections/community\.general/pull/10712](https\://github\.com/ansible\-collections/community\.general/pull/10712)\)\.
* manageiq\_group \- minor refactor to simplify string formatting \([https\://github\.com/ansible\-collections/community\.general/pull/10727](https\://github\.com/ansible\-collections/community\.general/pull/10727)\)\.
* manageiq\_tenant \- minor refactor to simplify string formatting \([https\://github\.com/ansible\-collections/community\.general/pull/10727](https\://github\.com/ansible\-collections/community\.general/pull/10727)\)\.
* mssql\_db \- minor refactor to simplify string formatting \([https\://github\.com/ansible\-collections/community\.general/pull/10727](https\://github\.com/ansible\-collections/community\.general/pull/10727)\)\.
* one\_vm \- minor refactor to improve readability \([https\://github\.com/ansible\-collections/community\.general/pull/10712](https\://github\.com/ansible\-collections/community\.general/pull/10712)\)\.
* openbsd\_pkg \- add <code>autoremove</code> parameter to remove unused dependencies \([https\://github\.com/ansible\-collections/community\.general/pull/10705](https\://github\.com/ansible\-collections/community\.general/pull/10705)\)\.
* openbsd\_pkg \- minor refactor to simplify string formatting \([https\://github\.com/ansible\-collections/community\.general/pull/10727](https\://github\.com/ansible\-collections/community\.general/pull/10727)\)\.
* pacemaker\_resource \- add <code>state\=cleanup</code> for cleaning up pacemaker resources \([https\://github\.com/ansible\-collections/community\.general/pull/10413](https\://github\.com/ansible\-collections/community\.general/pull/10413)\)
* pacemaker\_resource \- add <code>state\=cloned</code> for cloning pacemaker resources or groups \([https\://github\.com/ansible\-collections/community\.general/issues/10322](https\://github\.com/ansible\-collections/community\.general/issues/10322)\, [https\://github\.com/ansible\-collections/community\.general/pull/10665](https\://github\.com/ansible\-collections/community\.general/pull/10665)\)\.
* pacemaker\_resource \- the parameter <code>name</code> is no longer a required parameter in community\.general 11\.3\.0 \([https\://github\.com/ansible\-collections/community\.general/pull/10413](https\://github\.com/ansible\-collections/community\.general/pull/10413)\)
* parted \- using safer mechanism to run external command \([https\://github\.com/ansible\-collections/community\.general/pull/10642](https\://github\.com/ansible\-collections/community\.general/pull/10642)\)\.
* random\_string lookup plugin \- allow to specify seed while generating random string \([https\://github\.com/ansible\-collections/community\.general/issues/5362](https\://github\.com/ansible\-collections/community\.general/issues/5362)\, [https\://github\.com/ansible\-collections/community\.general/pull/10710](https\://github\.com/ansible\-collections/community\.general/pull/10710)\)\.
* scaleway modules \- add a <code>scaleway</code> group to use <code>module\_defaults</code> \([https\://github\.com/ansible\-collections/community\.general/pull/10647](https\://github\.com/ansible\-collections/community\.general/pull/10647)\)\.
* scaleway\_container \- add a <code>cpu\_limit</code> argument \([https\://github\.com/ansible\-collections/community\.general/pull/10646](https\://github\.com/ansible\-collections/community\.general/pull/10646)\)\.
* terraform \- minor refactor to improve readability \([https\://github\.com/ansible\-collections/community\.general/pull/10711](https\://github\.com/ansible\-collections/community\.general/pull/10711)\)\.
* ufw \- minor refactor to simplify string formatting \([https\://github\.com/ansible\-collections/community\.general/pull/10727](https\://github\.com/ansible\-collections/community\.general/pull/10727)\)\.
* xenserver module utils \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10769](https\://github\.com/ansible\-collections/community\.general/pull/10769)\)\.
* xenserver\_facts \- minor refactor to simplify string formatting \([https\://github\.com/ansible\-collections/community\.general/pull/10727](https\://github\.com/ansible\-collections/community\.general/pull/10727)\)\.
* zfs\_facts \- minor refactor to simplify string formatting \([https\://github\.com/ansible\-collections/community\.general/pull/10727](https\://github\.com/ansible\-collections/community\.general/pull/10727)\)\.
* zypper \- support the <code>\-\-gpg\-auto\-import\-keys</code> option in zypper \([https\://github\.com/ansible\-collections/community\.general/issues/10660](https\://github\.com/ansible\-collections/community\.general/issues/10660)\, [https\://github\.com/ansible\-collections/community\.general/pull/10661](https\://github\.com/ansible\-collections/community\.general/pull/10661)\)\.

<a id="community-mysql"></a>
#### community\.mysql

* <em class="title-reference">mysql\_query</em> \- add new <em class="title-reference">session\_vars</em> argument\, similar to ansible\-collections/community\.mysql\#489\.

<a id="community-routeros"></a>
#### community\.routeros

* api\_find\_and\_modify\, api\_modify \- instead of comparing supplied values as\-is to values retrieved from the API and converted to some types \(int\, bool\) by librouteros\, instead compare values by converting them to strings first\, using similar conversion rules that librouteros uses \([https\://github\.com/ansible\-collections/community\.routeros/issues/389](https\://github\.com/ansible\-collections/community\.routeros/issues/389)\, [https\://github\.com/ansible\-collections/community\.routeros/issues/370](https\://github\.com/ansible\-collections/community\.routeros/issues/370)\, [https\://github\.com/ansible\-collections/community\.routeros/issues/325](https\://github\.com/ansible\-collections/community\.routeros/issues/325)\, [https\://github\.com/ansible\-collections/community\.routeros/issues/169](https\://github\.com/ansible\-collections/community\.routeros/issues/169)\, [https\://github\.com/ansible\-collections/community\.routeros/pull/397](https\://github\.com/ansible\-collections/community\.routeros/pull/397)\)\.

<a id="community-vmware-1"></a>
#### community\.vmware

* vcenter\_license \- Add support for VCF license keys\. \([https\://github\.com/ansible\-collections/community\.vmware/pull/2451](https\://github\.com/ansible\-collections/community\.vmware/pull/2451)\)
* vsphere\_file \- Remove <code>ansible\.module\_utils\.six\.PY2</code> \([https\://github\.com/ansible\-collections/community\.vmware/pull/2475](https\://github\.com/ansible\-collections/community\.vmware/pull/2475)\)\.

<a id="community-zabbix"></a>
#### community\.zabbix

* repo role \- Added proxy support when downloading RedHat GPG key\.
* repo role \- Added support for <em class="title-reference">zabbix\_repo\_deb\_schema</em>
* repo role \- defaulting <em class="title-reference">zabbix\_repo\_apt\_priority</em> to 1001
* repo role \- defaulting <em class="title-reference">zabbix\_repo\_version</em> to 7\.4
* repo role \- defaulting <em class="title-reference">zabbix\_repo\_yum\_gpgcheck</em> to 1
* roles/agent\, check to see if zabbix\_agent\_version\_long is already supplied
* roles/agent\, swap uri with win\_uri
* server role \- fixing zabbix\_repo\_package to repo role
* zabbix\_agent \- Removed zabbix\_win\_install\_dir variable and replaced with zabbix\_agent\_win\_install\_dir
* zabbix\_agent \- Removed zabbix\_win\_install\_dir\_conf variable and replaced with zabbix\_agent\_win\_install\_dir\_conf
* zabbix\_maintenance \- Added support for multiple outage periods within a single event
* zabbix\_maintenance \- Added support for recuring maintenance windows
* zabbix\_script \- Added support for type \'url\'
* zabbix\_script \- Added support for user input\.

<a id="containers-podman-1"></a>
#### containers\.podman

* Add building Podman from source
* Add podman image scp option
* Add unittests for podman\_image
* Improve docs and guides
* Rewrite podman\_image and add tests
* Update docs and script

<a id="google-cloud"></a>
#### google\.cloud

* iap \- enable use of Identity Aware Proxy ssh connections to compute instances \([https\://github\.com/ansible\-collections/google\.cloud/pull/709](https\://github\.com/ansible\-collections/google\.cloud/pull/709)\)\.

<a id="hitachivantara-vspone-block"></a>
#### hitachivantara\.vspone\_block

* Added a new <em class="title-reference">\"hv\_sds\_block\_capacity\_management\_settings\_facts\"</em> module to retrieve capacity management settings from SDS block cluster\.
* Added a new <em class="title-reference">\"hv\_sds\_block\_drive\"</em> module to turn ON and Off the drive locator LED\, remove a drive from SDS block cluster\.
* Added a new <em class="title-reference">\"hv\_sds\_block\_storage\_controller\"</em> module to edit storage controller settings on SDS block cluster\.
* Added a new <em class="title-reference">\"hv\_sds\_block\_storage\_node\_bmc\_connection\_facts\"</em> module to retrieve BMC connection details from SDS block cluster\.
* Added a new <em class="title-reference">\"hv\_sds\_block\_storage\_pool\_estimated\_capacity\_facts\"</em> module to retrieve storage pool estimated capacity from SDS block cluster on AWS\.
* Added a new <em class="title-reference">\"hv\_vsp\_one\_volume\"</em> module to enable creation\, modification\, and deletion of volumes\, as well as attaching and detaching to servers on VSP E series and VSP One B2X storages\.
* Added a new <em class="title-reference">\"hv\_vsp\_one\_volume\_facts\"</em> module to retrieve volumes information from servers on VSP E series and VSP One B2X storages\.
* Added support for SDS block cluster on Microsoft Azure\.
* Added support to \"Edit storage pool settings\" to hv\_sds\_block\_storage\_pool module\.
* Added support to \"Edit the capacity balancing settings\" to hv\_sds\_block\_cluster module\.
* Added support with new parameters \"start\_ldev\"\, \"end\_ldev\"\, \"external\_parity\_groups\" to hv\_resource\_group module\.

<a id="ibm-storage-virtualize"></a>
#### ibm\.storage\_virtualize

* ibm\_sv\_manage\_flashsystem\_grid \- Added support for new FlashSystem grid APIs
* ibm\_sv\_manage\_storage\_partition \- Added support for management portset and renaming partition
* ibm\_sv\_manage\_truststore\_for\_replication \- Added support for new FlashSystem grid APIs
* ibm\_svc\_hostcluster \- Added support for partition and for managing host mappings during hostcluster deletion
* ibm\_svc\_info \- Added support for new FlashSystem grid APIs
* ibm\_svc\_manage\_ip \- Changes for management portset
* ibm\_svc\_manage\_portset \- Added support for management portset
* ibm\_svc\_manage\_volume \- Added support for HA volumes volume expansion\, volumegroup\, volume rename and grainsize

<a id="purestorage-flasharray"></a>
#### purestorage\.flasharray

* plugins/module\_utils/purefa\.py \- Removed <code>get\_system</code> function as REST v1 no longer supported by Collection
* purefa\_connect \- Allow asynchronous FC\-based replication
* purefa\_default\_protection \- Added Fusion support\.
* purefa\_dsrole\_old \- Upgraded to REST v2
* purefa\_info \- Added new subsets <code>workloads</code> and <code>presets</code>
* purefa\_info \- Converted to use REST 2
* purefa\_network \- Converted to REST v2
* purefa\_ntp \- Added Fusion support\.
* purefa\_pod \- Added support for SafeMode protection group configuration
* purefa\_policy \- Upgraded to REST v2
* purefa\_syslog \- Added Fusion support\.
* purefa\_user \- All AD users to have SSH keys and/or API tokens assigned\, even if they have never accessed the FlashArray before\. AD users must have <code>ad\_user</code> set as <code>true</code>\.
* purefa\_volume\_tags \- Add <em class="title-reference">tag</em> parameter to specify tag to be deleted by key name
* purefa\_volume\_tags \- Upgraded to REST v2 and added Fusion support

<a id="purestorage-flashblade"></a>
#### purestorage\.flashblade

* purefb\_ad \- Revert removal of <code>service</code> parameter \(breaking change\)\. Added more logic to use of <code>service</code> parameter and recommend use of <code>service\_principals</code> with service incorporated\.
* purefb\_ad \- <code>service</code> parameter removed to comply with underlying API structure\. <code>service</code> should be included in the <code>service\_principals</code> strings as shown in the documentation\.
* purefb\_saml \- Added <code>entity\_id</code> parameter
* purefb\_snap \- Add support to delete/eradicate remote snapshots\, including the latest replica
* purefb\_user \- All AD users to have SSH keys and/or API tokens assigned\, even if they have never accessed the FlashArray before\. AD users must have <code>ad\_user</code> set as <code>true</code>\.

<a id="theforeman-foreman"></a>
#### theforeman\.foreman

* content\_upload \- fall\-back to rpm binary when library can\'t be imported
* registration\_command \- clarify example to show where the generated command needs to be executed

<a id="breaking-changes--porting-guide"></a>
### Breaking Changes / Porting Guide

<a id="ansible-core-3"></a>
#### Ansible\-core

* powershell \- Removed code that tried to remote quotes from paths when performing Windows operations like copying and fetching file\. This should not affect normal playbooks unless a value is quoted too many times\.

<a id="community-mysql-1"></a>
#### community\.mysql

* Since version 4\.0\.0\, the collection accepts code written in Python 3\. Modules aren\'t tested against Python 2 and might not work in Python 2 environments\.
* collection \- stop testing against mysqlclient connector as its support was deprecated in this collection \- use PyMySQL connector instead\! It\'ll stop working in 5\.0\.0 when we remove all related code \([https\://github\.com/ansible\-collections/community\.mysql/issues/654](https\://github\.com/ansible\-collections/community\.mysql/issues/654)\)\.
* mysql\_db \- the <code>pipefail</code> argument\'s default value is set to <code>true</code>\.  If your target machines do not use <code>bash</code> as a default interpreter\, set <code>pipefail</code> to <code>false</code> explicitly\. However\, we strongly recommend setting up <code>bash</code> as a default and <code>pipefail\=true</code> as it will protect you from getting broken dumps you don\'t know about \([https\://github\.com/ansible\-collections/community\.mysql/issues/407](https\://github\.com/ansible\-collections/community\.mysql/issues/407)\)\.
* mysql\_info \- The <code>users\_info</code> filter does not return the <code>plugin\_auth\_string</code> field anymore\. Use the <em class="title-reference">plugin\_hash\_string</em> return value instead \([https\://github\.com/ansible\-collections/community\.mysql/pull/629](https\://github\.com/ansible\-collections/community\.mysql/pull/629)\)\.
* mysql\_role \- the <code>column\_case\_sensitive</code> argument\'s default value has been changed to <code>true</code>\. If your playbook expected the column to be automatically uppercased for your users privileges\, you should set this to <code>false</code> explicitly \([https\://github\.com/ansible\-collections/community\.mysql/issues/578](https\://github\.com/ansible\-collections/community\.mysql/issues/578)\)\.
* mysql\_user \- the <code>column\_case\_sensitive</code> argument\'s default value has been changed to <code>true</code>\. If your playbook expected the column to be automatically uppercased for your users privileges\, you should set this to <code>false</code> explicitly \([https\://github\.com/ansible\-collections/community\.mysql/issues/577](https\://github\.com/ansible\-collections/community\.mysql/issues/577)\)\.

<a id="community-vmware-2"></a>
#### community\.vmware

* Removed support for ansible\-core \< 2\.19\.0\.
* Removed support for vmware\.vmware \< 2\.0\.0\.
* Replace the dependencies on <code>pyvmomi</code>\, <code>vmware\-vcenter</code> and <code>vmware\-vapi\-common\-client</code> with <code>vcf\-sdk</code> \([https\://github\.com/ansible\-collections/community\.vmware/pull/2457](https\://github\.com/ansible\-collections/community\.vmware/pull/2457)\)\.

<a id="ibm-storage-virtualize-1"></a>
#### ibm\.storage\_virtualize

* ibm\_sv\_manage\_flashsystem\_grid \- The flashsystem grid module now uses newer FlashSystem REST APIs to perform tasks\.

<a id="deprecated-features"></a>
### Deprecated Features

<a id="ansible-core-4"></a>
#### Ansible\-core

* Deprecated the shell plugin\'s <code>wrap\_for\_exec</code> function\. This API is not used in Ansible or any known collection and is being removed to simplify the plugin API\. Plugin authors should wrap their command to execute within an explicit shell or other known executable\.
* INJECT\_FACTS\_AS\_VARS configuration currently defaults to <code>True</code>\, this is now deprecated and it will switch to <code>False</code> by Ansible 2\.24\. You will only get notified if you are accessing \'injected\' facts \(for example\, ansible\_os\_distribution vs ansible\_facts\[\'os\_distribution\'\]\)\.
* hash\_params function in roles/\_\_init\_\_ is being deprecated as it is not in use\.
* include\_vars \- Specifying \'ignore\_files\' as a string is deprecated\.
* vars\, the internal variable cache will be removed in 2\.24\. This cache\, once used internally exposes variables in inconsistent states\, the \'vars\' and \'varnames\' lookups should be used instead\.

<a id="community-general-1"></a>
#### community\.general

* hiera lookup plugin \- retrieving data with Hiera has been deprecated a long time ago\; because of that this plugin will be removed from community\.general 13\.0\.0\. If you disagree with this deprecation\, please create an issue in the community\.general repository \([https\://github\.com/ansible\-collections/community\.general/issues/4462](https\://github\.com/ansible\-collections/community\.general/issues/4462)\, [https\://github\.com/ansible\-collections/community\.general/pull/10779](https\://github\.com/ansible\-collections/community\.general/pull/10779)\)\.
* oci\_utils module utils \- utils is deprecated and will be removed in community\.general 13\.0\.0 \([https\://github\.com/ansible\-collections/community\.general/issues/10318](https\://github\.com/ansible\-collections/community\.general/issues/10318)\, [https\://github\.com/ansible\-collections/community\.general/pull/10652](https\://github\.com/ansible\-collections/community\.general/pull/10652)\)\.
* oci\_vcn \- module is deprecated and will be removed in community\.general 13\.0\.0 \([https\://github\.com/ansible\-collections/community\.general/issues/10318](https\://github\.com/ansible\-collections/community\.general/issues/10318)\, [https\://github\.com/ansible\-collections/community\.general/pull/10652](https\://github\.com/ansible\-collections/community\.general/pull/10652)\)\.
* oracle\* doc fragments \- fragments are deprecated and will be removed in community\.general 13\.0\.0 \([https\://github\.com/ansible\-collections/community\.general/issues/10318](https\://github\.com/ansible\-collections/community\.general/issues/10318)\, [https\://github\.com/ansible\-collections/community\.general/pull/10652](https\://github\.com/ansible\-collections/community\.general/pull/10652)\)\.

<a id="community-vmware-3"></a>
#### community\.vmware

* vmware\_guest\_snapshot \- the module has been deprecated and will be removed in community\.vmware 8\.0\.0 \([https\://github\.com/ansible\-collections/community\.vmware/pull/2467](https\://github\.com/ansible\-collections/community\.vmware/pull/2467)\)\.

<a id="community-zabbix-1"></a>
#### community\.zabbix

* zabbix\_maintenance module \- Depreicated <em class="title-reference">minutes</em> argument for <em class="title-reference">time\_periods</em>

<a id="purestorage-flasharray-1"></a>
#### purestorage\.flasharray

* purefa\_volume\_tags \- Deprecated due to removal of REST 1\.x support\. Will be removed in Collection 2\.0\.0

<a id="removed-features-previously-deprecated"></a>
### Removed Features \(previously deprecated\)

* The deprecated <code>ibm\.qradar</code> collection has been removed \([https\://forum\.ansible\.com/t/44259](https\://forum\.ansible\.com/t/44259)\)\.

<a id="ansible-core-5"></a>
#### Ansible\-core

* Removed the option to set the <code>DEFAULT\_TRANSPORT</code> configuration to <code>smart</code> that selects the default transport as either <code>ssh</code> or <code>paramiko</code> based on the underlying platform configuraton\.
* <code>vault</code>/<code>unvault</code> filters \- remove the deprecated <code>vaultid</code> parameter\.
* ansible\-doc \- role entrypoint attributes are no longer shown
* ansible\-galaxy \- removed the v2 Galaxy server API\. Galaxy servers hosting collections must support v3\.
* dnf/dnf5 \- remove deprecated <code>install\_repoquery</code> option\.
* encrypt \- remove deprecated passlib\_or\_crypt API\.
* paramiko \- Removed the <code>PARAMIKO\_HOST\_KEY\_AUTO\_ADD</code> and <code>PARAMIKO\_LOOK\_FOR\_KEYS</code> configuration keys\, which were previously deprecated\.
* py3compat \- remove deprecated <code>py3compat\.environ</code> call\.
* vars plugins \- removed the deprecated <code>get\_host\_vars</code> or <code>get\_group\_vars</code> fallback for vars plugins that do not inherit from <code>BaseVarsPlugin</code> and define a <code>get\_vars</code> method\.
* yum\_repository \- remove deprecated <code>keepcache</code> option\.

<a id="community-vmware-4"></a>
#### community\.vmware

* vmware\_cluster \- The deprecated module has been removed\. Use <code>vmware\.vmware\.cluster</code> instead \([https\://github\.com/ansible\-collections/community\.vmware/pull/2455](https\://github\.com/ansible\-collections/community\.vmware/pull/2455)\)\.
* vmware\_cluster\_dpm \- The deprecated module has been removed\. Use <code>vmware\.vmware\.cluster\_dpm</code> instead \([https\://github\.com/ansible\-collections/community\.vmware/pull/2455](https\://github\.com/ansible\-collections/community\.vmware/pull/2455)\)\.
* vmware\_cluster\_drs \- The deprecated module has been removed\. Use <code>vmware\.vmware\.cluster\_drs</code> instead \([https\://github\.com/ansible\-collections/community\.vmware/pull/2455](https\://github\.com/ansible\-collections/community\.vmware/pull/2455)\)\.
* vmware\_cluster\_drs\_recommendations \- The deprecated module has been removed\. Use <code>vmware\.vmware\.cluster\_drs\_recommendations</code> instead \([https\://github\.com/ansible\-collections/community\.vmware/pull/2455](https\://github\.com/ansible\-collections/community\.vmware/pull/2455)\)\.
* vmware\_cluster\_vcls \- The deprecated module has been removed\. Use <code>vmware\.vmware\.cluster\_vcls</code> instead \([https\://github\.com/ansible\-collections/community\.vmware/pull/2455](https\://github\.com/ansible\-collections/community\.vmware/pull/2455)\)\.

<a id="bugfixes"></a>
### Bugfixes

<a id="ansible-core-6"></a>
#### Ansible\-core

* Do not re\-add <code>tags</code> on blocks from within <code>import\_tasks</code>\.
* The <code>ansible\_failed\_task</code> variable is now correctly exposed in a rescue section\, even when a failing handler is triggered by the <code>flush\_handlers</code> task in the corresponding <code>block</code> \([https\://github\.com/ansible/ansible/issues/85682](https\://github\.com/ansible/ansible/issues/85682)\)
* Windows async \- Handle running PowerShell modules with trailing data after the module result
* <code>ansible\-galaxy collection list</code> \- fail when none of the configured collection paths exist\.
* <code>ternary</code> filter \- evaluate values lazily \([https\://github\.com/ansible/ansible/issues/85743](https\://github\.com/ansible/ansible/issues/85743)\)
* ansible\-doc \-\-list/\-\-list\_files/\-\-metadata\-dump \- fixed relative imports in nested filter/test plugin files \([https\://github\.com/ansible/ansible/issues/85753](https\://github\.com/ansible/ansible/issues/85753)\)\.
* ansible\-galaxy \- Use the provided import task url\, instead of parsing to get the task id and reconstructing the URL
* ansible\-galaxy no longer shows the internal protomatter collection when listing\.
* ansible\-test \- Always exclude the <code>tests/output/</code> directory from a collection\'s code coverage\. \([https\://github\.com/ansible/ansible/issues/84244](https\://github\.com/ansible/ansible/issues/84244)\)
* ansible\-test \- Fix a traceback that can occur when using delegation before the ansible\-test temp directory is created\.
* ansible\-test \- Limit package install retries during managed remote instance bootstrapping\.
* ansible\-test \- Use a consistent coverage config for all collection testing\.
* apt \- mark dependencies installed as part of deb file installation as auto \([https\://github\.com/ansible/ansible/issues/78123](https\://github\.com/ansible/ansible/issues/78123)\)\.
* argspec validation \- The <code>str</code> argspec type treats <code>None</code> values as empty string for better consistency with pre\-2\.19 templating conversions\.
* cache plugins \- close temp cache file before moving it to fix error on WSL\. \([https\://github\.com/ansible/ansible/pull/85816](https\://github\.com/ansible/ansible/pull/85816)\)
* callback plugins \- fix displaying the rendered <code>ansible\_host</code> variable with <code>delegate\_to</code> \([https\://github\.com/ansible/ansible/issues/84922](https\://github\.com/ansible/ansible/issues/84922)\)\.
* callback plugins \- improve consistency accessing the Task object\'s resolved\_action attribute\.
* conditionals \- When displaying a broken conditional error or deprecation warning\, the origin of the non\-boolean result is included \(if available\)\, and the raw result is omitted\.
* display \- Fixed reference to undefined <em class="title-reference">\_DeferredWarningContext</em> when issuing early warnings during startup\. \([https\://github\.com/ansible/ansible/issues/85886](https\://github\.com/ansible/ansible/issues/85886)\)
* dnf \- Check if installroot is directory or not \([https\://github\.com/ansible/ansible/issues/85680](https\://github\.com/ansible/ansible/issues/85680)\)\.
* failed\_when \- When using <code>failed\_when</code> to suppress an error\, the <code>exception</code> key in the result is renamed to <code>failed\_when\_suppressed\_exception</code>\. This prevents the error from being displayed by callbacks after being suppressed\. \([https\://github\.com/ansible/ansible/issues/85505](https\://github\.com/ansible/ansible/issues/85505)\)
* import\_tasks \- fix templating parent include arguments\.
* include\_role \- allow host specific values in all <code>\*\_from</code> arguments \([https\://github\.com/ansible/ansible/issues/66497](https\://github\.com/ansible/ansible/issues/66497)\)
* pip \- Fix pip module output so that it returns changed when the only operation is initializing a venv\.
* plugins config\, get\_option\_and\_origin now correctly displays the value and origin of the option\.
* run\_command \- Fixed premature selector unregistration on empty read from stdout/stderr that caused truncated output or hangs in rare situations\.
* script inventory plugin will now show correct \'incorrect\' type when doing implicit conversions on groups\.
* ssh connection \- fix documented variables for the <code>host</code> option\. Connection options can be configured with delegated variables in general\.
* template lookup \- Skip finalization on the internal templating operation to allow markers to be returned and handled by\, e\.g\. the <code>default</code> filter\. Previously\, finalization tripped markers\, causing an exception to end processing of the current template pipeline\. \([https\://github\.com/ansible/ansible/issues/85674](https\://github\.com/ansible/ansible/issues/85674)\)
* templating \- Avoid tripping markers within Jinja generated code\. \([https\://github\.com/ansible/ansible/issues/85674](https\://github\.com/ansible/ansible/issues/85674)\)
* templating \- Ensure filter plugin result processing occurs under the correct call context\. \([https\://github\.com/ansible/ansible/issues/85585](https\://github\.com/ansible/ansible/issues/85585)\)
* templating \- Fix slicing of tuples in templating \([https\://github\.com/ansible/ansible/issues/85606](https\://github\.com/ansible/ansible/issues/85606)\)\.
* templating \- Multi\-node template results coerce embedded <code>None</code> nodes to empty string \(instead of rendering literal <code>None</code> to the output\)\.
* templating \- Undefined marker values sourced from the Jinja <code>getattr\-\>getitem</code> fallback are now accessed correctly\, raising AnsibleUndefinedVariable for user plugins that do not understand markers\. Previously\, these values were erroneously returned to user plugin code that had not opted in to marker acceptance\.
* tqm \- use display\.error\_as\_warning instead of display\.warning\_as\_error\.
* tqm \- use display\.error\_as\_warning instead of self\.warning\.
* uri \- fix form\-multipart file not being found when task is retried \([https\://github\.com/ansible/ansible/issues/85009](https\://github\.com/ansible/ansible/issues/85009)\)
* validate\-modules sanity test \- fix handling of missing doc fragments \([https\://github\.com/ansible/ansible/pull/85638](https\://github\.com/ansible/ansible/pull/85638)\)\.

<a id="cisco-meraki"></a>
#### cisco\.meraki

* cisco\.meraki\.devices\_appliance\_uplinks\_settings \- fix idempotency error\.

<a id="community-dns"></a>
#### community\.dns

* Update Public Suffix List\.

<a id="community-general-2"></a>
#### community\.general

* kdeconfig \- <code>kwriteconfig</code> executable could not be discovered automatically on systems with only <code>kwriteconfig6</code> installed\. <code>kwriteconfig6</code> can now be discovered by Ansible \([https\://github\.com/ansible\-collections/community\.general/issues/10746](https\://github\.com/ansible\-collections/community\.general/issues/10746)\, [https\://github\.com/ansible\-collections/community\.general/pull/10751](https\://github\.com/ansible\-collections/community\.general/pull/10751)\)\.
* monit \- fix crash caused by an unknown status value returned from the monit service \([https\://github\.com/ansible\-collections/community\.general/issues/10742](https\://github\.com/ansible\-collections/community\.general/issues/10742)\, [https\://github\.com/ansible\-collections/community\.general/pull/10743](https\://github\.com/ansible\-collections/community\.general/pull/10743)\)\.
* pacemaker \- use regex for matching <code>maintenance\-mode</code> output to determine cluster maintenance status \([https\://github\.com/ansible\-collections/community\.general/issues/10426](https\://github\.com/ansible\-collections/community\.general/issues/10426)\, [https\://github\.com/ansible\-collections/community\.general/pull/10707](https\://github\.com/ansible\-collections/community\.general/pull/10707)\)\.
* selective callback plugin \- specify <code>ansible\_loop\_var</code> instead of the explicit value <code>item</code> when printing task result \([https\://github\.com/ansible\-collections/community\.general/pull/10752](https\://github\.com/ansible\-collections/community\.general/pull/10752)\)\.

<a id="community-routeros-1"></a>
#### community\.routeros

* api \- allow querying for keys containing <code>id</code>\, as long as the key itself is not <code>id</code> \([https\://github\.com/ansible\-collections/community\.routeros/issues/396](https\://github\.com/ansible\-collections/community\.routeros/issues/396)\, [https\://github\.com/ansible\-collections/community\.routeros/pull/398](https\://github\.com/ansible\-collections/community\.routeros/pull/398)\)\.

<a id="community-vmware-5"></a>
#### community\.vmware

* vmware\_guest\_file\_operation \- fix <code>replace\(\) argument 2 must be str\, not int</code> error \([https\://github\.com/ansible\-collections/community\.vmware/issues/2447](https\://github\.com/ansible\-collections/community\.vmware/issues/2447)\)\.
* vmware\_tools \- fix <code>replace\(\) argument 2 must be str\, not int</code> error \([https\://github\.com/ansible\-collections/community\.vmware/issues/2447](https\://github\.com/ansible\-collections/community\.vmware/issues/2447)\)\.

<a id="community-zabbix-2"></a>
#### community\.zabbix

* Proxy Role \- Fixed a deprication error with <em class="title-reference">ProxyConfigFrequency</em>
* web role \- Fixed a value test in nginx\_vhost\.conf
* zabbix\_agent \- Fix all variables related to windows installation paths
* zabbix\_agent role \- Fix windows paths to download and install zabbix agent msi
* zabbix\_agent role \- fixes too many requests to check latest zabbix release
* zabbix\_maintenance \- Fixed a bug that caused start time to update across multiple runs
* zabbix\_template \- Removed need for PY2
* zabbix\_template\_info \- Removed need for PY2

<a id="containers-podman-2"></a>
#### containers\.podman

* Fix podman logout for newer Podman
* Fix podman\_image correct delimiter logic for [version\@digest](mailto\:version\@digest) tags
* Remove quiet mode from pulling image

<a id="dellemc-openmanage-1"></a>
#### dellemc\.openmanage

* idrac\_server\_config\_profile \- \(Issue 959\) Can\'t export SCP \(Server configuration profile\) on iDRAC 10\. \([https\://github\.com/dell/dellemc\-openmanage\-ansible\-modules/issues/959](https\://github\.com/dell/dellemc\-openmanage\-ansible\-modules/issues/959)\)
* idrac\_system\_info \- \(Issue 967\) \- idrac\_system\_info fails on iDRAC10 with GPU\. \([https\://github\.com/dell/dellemc\-openmanage\-ansible\-modules/issues/967](https\://github\.com/dell/dellemc\-openmanage\-ansible\-modules/issues/967)\)

<a id="google-cloud-1"></a>
#### google\.cloud

* gcp\_compute\_instance \- add suppport for attaching disks to compute instances \([https\://github\.com/ansible\-collections/google\.cloud/pull/711](https\://github\.com/ansible\-collections/google\.cloud/pull/711)\)\.
* gcp\_secret\_manager \- use service\_account\_contents instead of service\_account\_info \([https\://github\.com/ansible\-collections/google\.cloud/pull/703](https\://github\.com/ansible\-collections/google\.cloud/pull/703)\)\.

<a id="ibm-storage-virtualize-2"></a>
#### ibm\.storage\_virtualize

* ibm\_svc\_mdiskgrp \- Removed mandatory system mask setting during pool\-linking

<a id="purestorage-flasharray-2"></a>
#### purestorage\.flasharray

* purefa\_certs \- Resolved error with incorrect use of <code>key\_size</code> for imported certificates
* purefa\_connect \- Ensured that encrypted connections use encrypted connection keys
* purefa\_eradication \- Fixed idempotency issue
* purefa\_eula \- Fix AttributeError when first sogning EULA
* purefa\_host \- Fixed Pydantic error when updating preferred\_arrays
* purefa\_info \- Ensured that volumes\, hosts\, host\_groups and transfers are correctly listed for protection groups
* purefa\_info \- Fixed AttributeError in config section related to SSO SAML2
* purefa\_info \- Fixed issue with replication connection throttle reporting
* purefa\_info \- Fixed issue with undo\-demote pods not reporting correctly
* purefa\_info \- Resolved AttributeError in volume subset
* purefa\_network \- Resolve typo that causes network updates to not apply correctly
* purefa\_pg \- Changing target for PG no longer requires a <code>FixedReference</code>
* purefa\_subnet \- Fixed failure when trying to update a subnet with no gateway defined

<a id="purestorage-flashblade-1"></a>
#### purestorage\.flashblade

* purefb\_ad \- Fixed issue where updating an AD account required unnecessary parameters\.
* purefb\_bucket \- Fix versioning control and access rules for public buckets
* purefb\_bucket \- Fixed issue where a bucket with no versioning defined was incorrectly created\.
* purefb\_bucket \- Fixed issue with default retention parameter
* purefb\_bucket\_access \- Fixed typo in CORS rule definition
* purefb\_certs \- Fixed issues with importing external certificates
* purefb\_certs \- Updated email regex pattern to fix <code>re</code> failures
* purefb\_dns \- Fixed multiple issues for data DNS configuration
* purefb\_fs \- Ensured that NFS rules are emprty if requested filesystem is SMB only
* purefb\_info \- Fixed error when <code>default</code> subset fails if SMD has been disabled on the FLashBlade
* purefb\_policy \- Fixed typo when calling object store policy rule deletion
* purefb\_s3user \- Fixed typo in imported keys code
* purefb\_subnet \- Ensured prefix is required for subnet creation or update

<a id="known-issues"></a>
### Known Issues

<a id="ansible-core-7"></a>
#### Ansible\-core

* templating \- Exceptions raised in a Jinja <code>set</code> or <code>with</code> block which are not accessed by the template are ignored in the same manner as undefined values\.
* templating \- Passing a container created in a Jinja <code>set</code> or <code>with</code> block to a method results in a copy of that container\. Mutations to that container which are not returned by the method will be discarded\.

<a id="dellemc-openmanage-2"></a>
#### dellemc\.openmanage

* idrac\_attributes \- The module accepts both the string as well as integer value for the field \"SNMP\.1\.AgentCommunity\" for iDRAC10\.
* idrac\_diagnostics \- This module does not support export of diagnostics file to HTTP and HTTPS share via SOCKS proxy\.
* idrac\_license \- Due to API limitation\, proxy parameters are ignored during the import operation\.
* idrac\_license \- The module will fail to export license to NFS Share\.
* idrac\_license \- The module will give different error messages for iDRAC9 and iDRAC10 when user imports license with invalid share name\.
* idrac\_os\_deployment \- The module continues to return a 200 response and marks the job as completed\, even when an outdated date is supplied in the Expose duration\.
* idrac\_redfish\_storage\_controller \- PatrolReadRatePercent attribute cannot be set in iDRAC10\.
* idrac\_server\_config\_profile \- When attempting to revert iDRAC settings using a previously exported SCP file\, the import operation will complete with errors if a new user was created after the export \(Instead of restoring the system to its previous state\, including the removal of newly added users\)\.
* idrac\_system\_info \- The module will show empty video list despite having Embedded VIDEO controller\.
* ome\_smart\_fabric\_uplink \- The module supported by OpenManage Enterprise Modular\, however it does not allow the creation of multiple uplinks of the same name\. If an uplink is created using the same name as an existing uplink\, then the existing uplink is modified\.
* redfish\_storage\_volume \- Encryption type and block\_io\_size bytes will be read only property in iDRAC 9 and iDRAC 10 and hence the module ignores these parameters\.

<a id="new-plugins"></a>
### New Plugins

<a id="filter"></a>
#### Filter

* community\.general\.to\_nice\_yaml \- Convert variable to YAML string\.
* community\.general\.to\_yaml \- Convert variable to YAML string\.

<a id="inventory"></a>
#### Inventory

* containers\.podman\.buildah\_containers \- Inventory plugin that discovers Buildah working containers as hosts
* containers\.podman\.podman\_containers \- Inventory plugin that discovers Podman containers as hosts

<a id="new-modules"></a>
### New Modules

<a id="check-point-mgmt-1"></a>
#### check\_point\.mgmt

* check\_point\.mgmt\.cp\_mgmt\_identity\_provider \- Manages identity\-provider objects on Checkpoint over Web Services API
* check\_point\.mgmt\.cp\_mgmt\_identity\_provider\_facts \- Get identity\-provider objects facts on Checkpoint over Web Services API
* check\_point\.mgmt\.cp\_mgmt\_if\_map\_server \- Manages if\-map\-server objects on Checkpoint over Web Services API
* check\_point\.mgmt\.cp\_mgmt\_if\_map\_server\_facts \- Get if\-map\-server objects facts on Checkpoint over Web Services API
* check\_point\.mgmt\.cp\_mgmt\_ldap\_group \- Manages ldap\-group objects on Checkpoint over Web Services API
* check\_point\.mgmt\.cp\_mgmt\_ldap\_group\_facts \- Get ldap\-group objects facts on Checkpoint over Web Services API
* check\_point\.mgmt\.cp\_mgmt\_log\_exporter \- Manages log\-exporter objects on Checkpoint over Web Services API
* check\_point\.mgmt\.cp\_mgmt\_log\_exporter\_facts \- Get log\-exporter objects facts on Checkpoint over Web Services API
* check\_point\.mgmt\.cp\_mgmt\_resource\_mms \- Manages resource\-mms objects on Checkpoint over Web Services API
* check\_point\.mgmt\.cp\_mgmt\_resource\_mms\_facts \- Get resource\-mms objects facts on Checkpoint over Web Services API
* check\_point\.mgmt\.cp\_mgmt\_resource\_tcp \- Manages resource\-tcp objects on Checkpoint over Web Services API
* check\_point\.mgmt\.cp\_mgmt\_resource\_tcp\_facts \- Get resource\-tcp objects facts on Checkpoint over Web Services API
* check\_point\.mgmt\.cp\_mgmt\_resource\_uri\_for\_qos \- Manages resource\-uri\-for\-qos objects on Checkpoint over Web Services API
* check\_point\.mgmt\.cp\_mgmt\_resource\_uri\_for\_qos\_facts \- Get resource\-uri\-for\-qos objects facts on Checkpoint over Web Services API
* check\_point\.mgmt\.cp\_mgmt\_run\_app\_control\_update \- Runs Application Control \& URL Filtering database update\.
* check\_point\.mgmt\.cp\_mgmt\_securemote\_dns\_server \- Manages securemote\-dns\-server objects on Checkpoint over Web Services API
* check\_point\.mgmt\.cp\_mgmt\_securemote\_dns\_server\_facts \- Get securemote\-dns\-server objects facts on Checkpoint over Web Services API
* check\_point\.mgmt\.cp\_mgmt\_securid\_server \- Manages securid\-server objects on Checkpoint over Web Services API
* check\_point\.mgmt\.cp\_mgmt\_securid\_server\_facts \- Get securid\-server objects facts on Checkpoint over Web Services API
* check\_point\.mgmt\.cp\_mgmt\_set\_anti\_malware\_update\_schedule \- Set both Anti\-Bot and Anti\-Virus update schedules\.
* check\_point\.mgmt\.cp\_mgmt\_set\_app\_control\_update\_schedule \- Set the Application Control and URL Filtering update schedule\.
* check\_point\.mgmt\.cp\_mgmt\_show\_anti\_malware\_update\_schedule \- Retrieve existing Anti\-Bot and Anti\-Virus update schedules\.
* check\_point\.mgmt\.cp\_mgmt\_show\_app\_control\_status \- Get app\-control\-status objects facts on Checkpoint over Web Services API
* check\_point\.mgmt\.cp\_mgmt\_show\_app\_control\_update\_schedule \- Get app\-control\-status objects facts on Checkpoint over Web Services API
* check\_point\.mgmt\.cp\_mgmt\_syslog\_server \- Manages syslog\-server objects on Checkpoint over Web Services API
* check\_point\.mgmt\.cp\_mgmt\_syslog\_server\_facts \- Get syslog\-server objects facts on Checkpoint over Web Services API

<a id="community-general-3"></a>
#### community\.general

* community\.general\.django\_dumpdata \- Wrapper for C\(django\-admin dumpdata\)\.
* community\.general\.django\_loaddata \- Wrapper for C\(django\-admin loaddata\)\.
* community\.general\.pacemaker\_stonith \- Manage Pacemaker STONITH\.

<a id="containers-podman-3"></a>
#### containers\.podman

* containers\.podman\.podman\_system\_connection \- Manage Podman system connections
* containers\.podman\.podman\_system\_connection\_info \- Get info about Podman system connections

<a id="hitachivantara-vspone-block-1"></a>
#### hitachivantara\.vspone\_block

<a id="sds-block"></a>
##### Sds Block

* hitachivantara\.vspone\_block\.hv\_sds\_block\_capacity\_management\_settings\_facts \- Get capacity management settings from storage system\.
* hitachivantara\.vspone\_block\.hv\_sds\_block\_drive \- Manages drive on Hitachi SDS Block storage systems\.
* hitachivantara\.vspone\_block\.hv\_sds\_block\_storage\_controller \- Edits the settings for the storage controller on Hitachi SDS Block storage systems\.
* hitachivantara\.vspone\_block\.hv\_sds\_block\_storage\_node\_bmc\_connection\_facts \- Get storage node BMC access settings from storage system\.
* hitachivantara\.vspone\_block\.hv\_sds\_block\_storage\_pool\_estimated\_capacity\_facts \- Obtains the preliminary calculation results of the storage pool logical capacity \(unit TiB\)\.

<a id="vsp"></a>
##### Vsp

* hitachivantara\.vspone\_block\.hv\_vsp\_one\_volume \- Manages volumes on Hitachi VSP One storage systems\.
* hitachivantara\.vspone\_block\.hv\_vsp\_one\_volume\_facts \- Retrieves facts about Hitachi VSP One storage system volumes\.

<a id="unchanged-collections"></a>
### Unchanged Collections

* amazon\.aws \(still version 10\.1\.1\)
* ansible\.netcommon \(still version 8\.1\.0\)
* ansible\.posix \(still version 2\.1\.0\)
* ansible\.utils \(still version 6\.0\.0\)
* ansible\.windows \(still version 3\.2\.0\)
* arista\.eos \(still version 12\.0\.0\)
* awx\.awx \(still version 24\.6\.1\)
* azure\.azcollection \(still version 3\.8\.0\)
* chocolatey\.chocolatey \(still version 1\.5\.3\)
* cisco\.aci \(still version 2\.12\.0\)
* cisco\.ios \(still version 11\.0\.0\)
* cisco\.iosxr \(still version 12\.0\.0\)
* cisco\.mso \(still version 2\.11\.0\)
* cisco\.nxos \(still version 11\.0\.0\)
* cisco\.ucs \(still version 1\.16\.0\)
* cloudscale\_ch\.cloud \(still version 2\.5\.2\)
* community\.aws \(still version 10\.0\.0\)
* community\.ciscosmb \(still version 1\.0\.11\)
* community\.crypto \(still version 3\.0\.3\)
* community\.digitalocean \(still version 1\.27\.0\)
* community\.docker \(still version 4\.7\.0\)
* community\.grafana \(still version 2\.3\.0\)
* community\.hashi\_vault \(still version 7\.0\.0\)
* community\.hrobot \(still version 2\.5\.0\)
* community\.library\_inventory\_filtering\_v1 \(still version 1\.1\.1\)
* community\.libvirt \(still version 2\.0\.0\)
* community\.mongodb \(still version 1\.7\.10\)
* community\.okd \(still version 5\.0\.0\)
* community\.postgresql \(still version 4\.1\.0\)
* community\.proxmox \(still version 1\.3\.0\)
* community\.proxysql \(still version 1\.6\.0\)
* community\.rabbitmq \(still version 1\.6\.0\)
* community\.sap\_libs \(still version 1\.4\.2\)
* community\.sops \(still version 2\.2\.2\)
* community\.windows \(still version 3\.0\.1\)
* cyberark\.conjur \(still version 1\.3\.7\)
* cyberark\.pas \(still version 1\.0\.35\)
* dellemc\.enterprise\_sonic \(still version 3\.0\.0\)
* dellemc\.powerflex \(still version 2\.6\.1\)
* dellemc\.unity \(still version 2\.1\.0\)
* f5networks\.f5\_modules \(still version 1\.38\.0\)
* fortinet\.fortimanager \(still version 2\.10\.0\)
* fortinet\.fortios \(still version 2\.4\.0\)
* grafana\.grafana \(still version 6\.0\.3\)
* hetzner\.hcloud \(still version 5\.2\.0\)
* ieisystem\.inmanage \(still version 3\.0\.0\)
* infinidat\.infinibox \(still version 1\.6\.3\)
* infoblox\.nios\_modules \(still version 1\.8\.0\)
* inspur\.ispim \(still version 2\.2\.3\)
* junipernetworks\.junos \(still version 11\.0\.0\)
* kaytus\.ksmanage \(still version 2\.0\.0\)
* kubernetes\.core \(still version 6\.1\.0\)
* kubevirt\.core \(still version 2\.2\.3\)
* lowlydba\.sqlserver \(still version 2\.7\.0\)
* microsoft\.ad \(still version 1\.9\.2\)
* microsoft\.iis \(still version 1\.0\.3\)
* netapp\.cloudmanager \(still version 21\.24\.0\)
* netapp\.ontap \(still version 23\.1\.0\)
* netapp\.storagegrid \(still version 21\.15\.0\)
* netapp\_eseries\.santricity \(still version 1\.4\.1\)
* netbox\.netbox \(still version 3\.21\.0\)
* ngine\_io\.cloudstack \(still version 2\.5\.0\)
* openstack\.cloud \(still version 2\.4\.1\)
* ovirt\.ovirt \(still version 3\.2\.1\)
* splunk\.es \(still version 4\.0\.0\)
* telekom\_mms\.icinga\_director \(still version 2\.4\.0\)
* vmware\.vmware \(still version 2\.3\.0\)
* vmware\.vmware\_rest \(still version 4\.9\.0\)
* vultr\.cloud \(still version 1\.13\.0\)
* vyos\.vyos \(still version 6\.0\.0\)
* wti\.remote \(still version 1\.0\.10\)
