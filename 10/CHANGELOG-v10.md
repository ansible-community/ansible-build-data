# Ansible 10 Release Notes

This changelog describes changes since Ansible 9\.0\.0\.

- <a href="#v10-7-0">v10\.7\.0</a>
    - <a href="#release-summary">Release Summary</a>
    - <a href="#ansible-core">Ansible\-core</a>
    - <a href="#changed-collections">Changed Collections</a>
    - <a href="#major-changes">Major Changes</a>
    - <a href="#minor-changes">Minor Changes</a>
    - <a href="#deprecated-features">Deprecated Features</a>
    - <a href="#security-fixes">Security Fixes</a>
    - <a href="#bugfixes">Bugfixes</a>
    - <a href="#known-issues">Known Issues</a>
    - <a href="#new-plugins">New Plugins</a>
    - <a href="#new-modules">New Modules</a>
    - <a href="#unchanged-collections">Unchanged Collections</a>
- <a href="#v10-6-0">v10\.6\.0</a>
    - <a href="#release-summary-1">Release Summary</a>
    - <a href="#ansible-core-4">Ansible\-core</a>
    - <a href="#changed-collections-1">Changed Collections</a>
    - <a href="#major-changes-1">Major Changes</a>
    - <a href="#minor-changes-1">Minor Changes</a>
    - <a href="#deprecated-features-1">Deprecated Features</a>
    - <a href="#security-fixes-1">Security Fixes</a>
    - <a href="#bugfixes-1">Bugfixes</a>
    - <a href="#known-issues-1">Known Issues</a>
    - <a href="#new-modules-1">New Modules</a>
    - <a href="#unchanged-collections-1">Unchanged Collections</a>
- <a href="#v10-5-0">v10\.5\.0</a>
    - <a href="#release-summary-2">Release Summary</a>
    - <a href="#ansible-core-8">Ansible\-core</a>
    - <a href="#changed-collections-2">Changed Collections</a>
    - <a href="#major-changes-2">Major Changes</a>
    - <a href="#minor-changes-2">Minor Changes</a>
    - <a href="#deprecated-features-2">Deprecated Features</a>
    - <a href="#bugfixes-2">Bugfixes</a>
    - <a href="#known-issues-2">Known Issues</a>
    - <a href="#new-modules-2">New Modules</a>
    - <a href="#unchanged-collections-2">Unchanged Collections</a>
- <a href="#v10-4-0">v10\.4\.0</a>
    - <a href="#release-summary-3">Release Summary</a>
    - <a href="#ansible-core-10">Ansible\-core</a>
    - <a href="#changed-collections-3">Changed Collections</a>
    - <a href="#major-changes-3">Major Changes</a>
    - <a href="#minor-changes-3">Minor Changes</a>
    - <a href="#deprecated-features-3">Deprecated Features</a>
    - <a href="#bugfixes-3">Bugfixes</a>
    - <a href="#known-issues-3">Known Issues</a>
    - <a href="#new-modules-3">New Modules</a>
    - <a href="#unchanged-collections-3">Unchanged Collections</a>
- <a href="#v10-3-0">v10\.3\.0</a>
    - <a href="#release-summary-4">Release Summary</a>
    - <a href="#ansible-core-12">Ansible\-core</a>
    - <a href="#changed-collections-4">Changed Collections</a>
    - <a href="#minor-changes-4">Minor Changes</a>
    - <a href="#deprecated-features-4">Deprecated Features</a>
    - <a href="#bugfixes-4">Bugfixes</a>
    - <a href="#known-issues-4">Known Issues</a>
    - <a href="#new-modules-4">New Modules</a>
    - <a href="#unchanged-collections-4">Unchanged Collections</a>
- <a href="#v10-2-0">v10\.2\.0</a>
    - <a href="#release-summary-5">Release Summary</a>
    - <a href="#added-collections">Added Collections</a>
    - <a href="#ansible-core-15">Ansible\-core</a>
    - <a href="#changed-collections-5">Changed Collections</a>
    - <a href="#major-changes-4">Major Changes</a>
    - <a href="#minor-changes-5">Minor Changes</a>
    - <a href="#deprecated-features-5">Deprecated Features</a>
    - <a href="#bugfixes-5">Bugfixes</a>
    - <a href="#known-issues-5">Known Issues</a>
    - <a href="#new-plugins-1">New Plugins</a>
    - <a href="#new-modules-5">New Modules</a>
    - <a href="#unchanged-collections-5">Unchanged Collections</a>
- <a href="#v10-1-0">v10\.1\.0</a>
    - <a href="#release-summary-6">Release Summary</a>
    - <a href="#added-collections-1">Added Collections</a>
    - <a href="#ansible-core-17">Ansible\-core</a>
    - <a href="#changed-collections-6">Changed Collections</a>
    - <a href="#major-changes-5">Major Changes</a>
    - <a href="#minor-changes-6">Minor Changes</a>
    - <a href="#deprecated-features-6">Deprecated Features</a>
    - <a href="#bugfixes-6">Bugfixes</a>
    - <a href="#known-issues-6">Known Issues</a>
    - <a href="#new-plugins-2">New Plugins</a>
    - <a href="#new-modules-6">New Modules</a>
    - <a href="#unchanged-collections-6">Unchanged Collections</a>
- <a href="#v10-0-1">v10\.0\.1</a>
    - <a href="#release-summary-7">Release Summary</a>
    - <a href="#ansible-core-20">Ansible\-core</a>
    - <a href="#changed-collections-7">Changed Collections</a>
    - <a href="#bugfixes-7">Bugfixes</a>
    - <a href="#unchanged-collections-7">Unchanged Collections</a>
- <a href="#v10-0-0">v10\.0\.0</a>
    - <a href="#release-summary-8">Release Summary</a>
    - <a href="#removed-collections">Removed Collections</a>
    - <a href="#added-collections-2">Added Collections</a>
    - <a href="#ansible-core-21">Ansible\-core</a>
    - <a href="#included-collections">Included Collections</a>
    - <a href="#major-changes-6">Major Changes</a>
    - <a href="#minor-changes-7">Minor Changes</a>
    - <a href="#breaking-changes--porting-guide">Breaking Changes / Porting Guide</a>
    - <a href="#deprecated-features-7">Deprecated Features</a>
    - <a href="#removed-features-previously-deprecated">Removed Features \(previously deprecated\)</a>
    - <a href="#security-fixes-2">Security Fixes</a>
    - <a href="#bugfixes-8">Bugfixes</a>
    - <a href="#known-issues-7">Known Issues</a>
    - <a href="#new-plugins-3">New Plugins</a>
    - <a href="#new-modules-7">New Modules</a>
    - <a href="#new-roles">New Roles</a>
    - <a href="#unchanged-collections-8">Unchanged Collections</a>

<a id="v10-7-0"></a>
## v10\.7\.0

- <a href="#release-summary">Release Summary</a>
- <a href="#ansible-core">Ansible\-core</a>
- <a href="#changed-collections">Changed Collections</a>
- <a href="#major-changes">Major Changes</a>
    - <a href="#dellemc-openmanage">dellemc\.openmanage</a>
- <a href="#minor-changes">Minor Changes</a>
    - <a href="#ansible-core-1">Ansible\-core</a>
    - <a href="#cisco-dnac">cisco\.dnac</a>
    - <a href="#community-dns">community\.dns</a>
    - <a href="#community-general">community\.general</a>
    - <a href="#community-mysql">community\.mysql</a>
    - <a href="#community-postgresql">community\.postgresql</a>
    - <a href="#fortinet-fortimanager">fortinet\.fortimanager</a>
    - <a href="#netapp-ontap">netapp\.ontap</a>
    - <a href="#purestorage-flasharray">purestorage\.flasharray</a>
    - <a href="#vmware-vmware">vmware\.vmware</a>
- <a href="#deprecated-features">Deprecated Features</a>
- <a href="#security-fixes">Security Fixes</a>
    - <a href="#ansible-core-2">Ansible\-core</a>
- <a href="#bugfixes">Bugfixes</a>
    - <a href="#ansible-core-3">Ansible\-core</a>
    - <a href="#cisco-ise">cisco\.ise</a>
    - <a href="#community-dns-1">community\.dns</a>
    - <a href="#community-docker">community\.docker</a>
    - <a href="#community-general-1">community\.general</a>
    - <a href="#community-mysql-1">community\.mysql</a>
    - <a href="#community-postgresql-1">community\.postgresql</a>
    - <a href="#community-vmware">community\.vmware</a>
    - <a href="#fortinet-fortimanager-1">fortinet\.fortimanager</a>
    - <a href="#infoblox-nios-modules">infoblox\.nios\_modules</a>
    - <a href="#netapp-ontap-1">netapp\.ontap</a>
    - <a href="#purestorage-flasharray-1">purestorage\.flasharray</a>
    - <a href="#telekom-mms-icinga-director">telekom\_mms\.icinga\_director</a>
    - <a href="#vmware-vmware-1">vmware\.vmware</a>
- <a href="#known-issues">Known Issues</a>
    - <a href="#dellemc-openmanage-1">dellemc\.openmanage</a>
- <a href="#new-plugins">New Plugins</a>
    - <a href="#filter">Filter</a>
    - <a href="#lookup">Lookup</a>
- <a href="#new-modules">New Modules</a>
    - <a href="#fortinet-fortimanager-2">fortinet\.fortimanager</a>
    - <a href="#netapp-ontap-2">netapp\.ontap</a>
- <a href="#unchanged-collections">Unchanged Collections</a>

<a id="release-summary"></a>
### Release Summary

Release Date\: 2024\-12\-03

[Porting Guide](https\://docs\.ansible\.com/ansible/devel/porting\_guides\.html)

<a id="ansible-core"></a>
### Ansible\-core

Ansible 10\.7\.0 contains ansible\-core version 2\.17\.7\.
This is a newer version than version 2\.17\.6 contained in the previous Ansible release\.

The changes are reported in the combined changelog below\.

<a id="changed-collections"></a>
### Changed Collections

If not mentioned explicitly\, the changes are reported in the combined changelog below\.

| Collection                  | Ansible 10.6.0 | Ansible 10.7.0 | Notes                                                                                                                        |
| --------------------------- | -------------- | -------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| cisco.dnac                  | 6.22.0         | 6.25.0         |                                                                                                                              |
| cisco.ise                   | 2.9.5          | 2.9.6          |                                                                                                                              |
| community.dns               | 3.0.6          | 3.1.0          |                                                                                                                              |
| community.docker            | 3.13.1         | 3.13.3         |                                                                                                                              |
| community.general           | 9.5.1          | 9.5.2          |                                                                                                                              |
| community.mysql             | 3.10.3         | 3.11.0         |                                                                                                                              |
| community.postgresql        | 3.7.0          | 3.9.0          |                                                                                                                              |
| community.vmware            | 4.8.0          | 4.8.1          |                                                                                                                              |
| cyberark.pas                | 1.0.27         | 1.0.30         | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
| dellemc.openmanage          | 9.8.0          | 9.9.0          |                                                                                                                              |
| fortinet.fortimanager       | 2.7.0          | 2.8.2          |                                                                                                                              |
| infoblox.nios_modules       | 1.7.0          | 1.7.1          |                                                                                                                              |
| netapp.ontap                | 22.12.0        | 22.13.0        |                                                                                                                              |
| openstack.cloud             | 2.2.0          | 2.3.0          | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
| purestorage.flasharray      | 1.31.1         | 1.32.0         |                                                                                                                              |
| telekom_mms.icinga_director | 2.2.0          | 2.2.1          |                                                                                                                              |
| vmware.vmware               | 1.6.0          | 1.7.1          |                                                                                                                              |

<a id="major-changes"></a>
### Major Changes

* The removal of netapp\.storagegrid was cancelled\. The collection will not be removed from Ansible 11 \([https\://forum\.ansible\.com/t/2811](https\://forum\.ansible\.com/t/2811)\)\.
  Maintenance of the collection has been taken over by another team at NetApp\.

<a id="dellemc-openmanage"></a>
#### dellemc\.openmanage

* omevv\_baseline\_profile \- This module allows to manage baseline profile\.
* omevv\_baseline\_profile\_info \- This module allows to retrieve baseline profile information\.
* omevv\_compliance\_info \- This module allows to retrieve firmware compliance reports\.

<a id="minor-changes"></a>
### Minor Changes

<a id="ansible-core-1"></a>
#### Ansible\-core

* remove extraneous selinux import \([https\://github\.com/ansible/ansible/issues/83657](https\://github\.com/ansible/ansible/issues/83657)\)\.

<a id="cisco-dnac"></a>
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

<a id="community-dns"></a>
#### community\.dns

* all controller code \- modernize Python code \([https\://github\.com/ansible\-collections/community\.dns/pull/231](https\://github\.com/ansible\-collections/community\.dns/pull/231)\)\.

<a id="community-general"></a>
#### community\.general

* proxmox inventory plugin \- fix urllib3 <code>InsecureRequestWarnings</code> not being suppressed when a token is used \([https\://github\.com/ansible\-collections/community\.general/pull/9099](https\://github\.com/ansible\-collections/community\.general/pull/9099)\)\.

<a id="community-mysql"></a>
#### community\.mysql

* mysql\_info \- adds the count of tables for each database to the returned values\. It is possible to exclude this new field using the <code>db\_table\_count</code> exclusion filter\. \([https\://github\.com/ansible\-collections/community\.mysql/pull/691](https\://github\.com/ansible\-collections/community\.mysql/pull/691)\)

<a id="community-postgresql"></a>
#### community\.postgresql

* postgresql\_pg\_hba \- changes ordering of entries that are identical except for the ip\-range\, but only if the ranges are of the same size\, this isn\'t breaking as ranges of equal size can\'t overlap \([https\://github\.com/ansible\-collections/community\.postgresql/pull/772](https\://github\.com/ansible\-collections/community\.postgresql/pull/772)\)
* postgresql\_pg\_hba \- orders auth\-options alphabetically\, this isn\'t breaking as the order of those options is not relevant to postgresql \([https\://github\.com/ansible\-collections/community\.postgresql/pull/772](https\://github\.com/ansible\-collections/community\.postgresql/pull/772)\)
* postgresql\_pg\_hba \- show the number of the line with the issue if parsing a file fails \([https\://github\.com/ansible\-collections/community\.postgresql/pull/766](https\://github\.com/ansible\-collections/community\.postgresql/pull/766)\)
* postgresql\_publication \- add possibility of creating publication with column list \([https\://github\.com/ansible\-collections/community\.postgresql/pull/763](https\://github\.com/ansible\-collections/community\.postgresql/pull/763)\)\.

<a id="fortinet-fortimanager"></a>
#### fortinet\.fortimanager

* Supported FortiManager 6\.2\.13\, 6\.4\.15\, 7\.0\.13\, 7\.2\.8\, 7\.4\.5\, 7\.6\.1\. Added 1 new module\.
* Supported check diff for some modules except \"fmgr\_generic\"\. You can use \"ansible\-playbook \-i \<your\-host\-file\> \<your\-playbook\> \-\-check \-\-diff\" to check what changes your playbook will make to the FortiManager\.

<a id="netapp-ontap"></a>
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

<a id="purestorage-flasharray"></a>
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

<a id="vmware-vmware"></a>
#### vmware\.vmware

* cluster\_info \- Migrate cluster\_info module from the community\.vmware collection to here
* content\_library\_item\_info \- Migrate content\_library\_item\_info module from the vmware\.vmware\_rest collection to here

<a id="deprecated-features"></a>
### Deprecated Features

* The collection <code>ibm\.spectrum\_virtualize</code> was renamed to <code>ibm\.storage\_virtualize</code>\.
  For now both collections are included in Ansible\.
  The collection will be completely removed from Ansible 12\.
  Please update your FQCNs from <code>ibm\.spectrum\_virtualize</code> to <code>ibm\.storage\_virtualize</code>\.

<a id="security-fixes"></a>
### Security Fixes

<a id="ansible-core-2"></a>
#### Ansible\-core

* Templating will not prefer AnsibleUnsafe when a variable is referenced via hostvars \- CVE\-2024\-11079

<a id="bugfixes"></a>
### Bugfixes

<a id="ansible-core-3"></a>
#### Ansible\-core

* Fix returning \'unreachable\' for the overall task result\. This prevents false positives when a looped task has unignored unreachable items \([https\://github\.com/ansible/ansible/issues/84019](https\://github\.com/ansible/ansible/issues/84019)\)\.
* ansible\-test \- Fix traceback that occurs after an interactive command fails\.
* dnf5 \- fix installing a package using <code>state\=latest</code> when a binary of the same name as the package is already installed \([https\://github\.com/ansible/ansible/issues/84259](https\://github\.com/ansible/ansible/issues/84259)\)
* dnf5 \- matching on a binary can be achieved only by specifying a full path \([https\://github\.com/ansible/ansible/issues/84334](https\://github\.com/ansible/ansible/issues/84334)\)

<a id="cisco-ise"></a>
#### cisco\.ise

* network\_device \- Fix mask validation to handle None values in NetworkDeviceIPList

<a id="community-dns-1"></a>
#### community\.dns

* Update Public Suffix List\.

<a id="community-docker"></a>
#### community\.docker

* docker\_compose\_v2\_exec\, docker\_compose\_v2\_run \- fix missing <code>\-\-env</code> flag while assembling env arguments \([https\://github\.com/ansible\-collections/community\.docker/pull/992](https\://github\.com/ansible\-collections/community\.docker/pull/992)\)\.
* docker\_compose\_v2\_run \- make sure to sanitize <code>labels</code> before sending them to the Docker Daemon \([https\://github\.com/ansible\-collections/community\.docker/pull/985](https\://github\.com/ansible\-collections/community\.docker/pull/985)\)\.
* docker\_config \- make sure to sanitize <code>labels</code> before sending them to the Docker Daemon \([https\://github\.com/ansible\-collections/community\.docker/pull/985](https\://github\.com/ansible\-collections/community\.docker/pull/985)\)\.
* docker\_host\_info \- ensure that the module always returns <code>can\_talk\_to\_docker</code>\, and that it provides the correct value even if <code>api\_version</code> is specified \([https\://github\.com/ansible\-collections/community\.docker/issues/993](https\://github\.com/ansible\-collections/community\.docker/issues/993)\, [https\://github\.com/ansible\-collections/community\.docker/pull/995](https\://github\.com/ansible\-collections/community\.docker/pull/995)\)\.
* docker\_network \- make sure to sanitize <code>labels</code> before sending them to the Docker Daemon \([https\://github\.com/ansible\-collections/community\.docker/pull/985](https\://github\.com/ansible\-collections/community\.docker/pull/985)\)\.
* docker\_node \- make sure to sanitize <code>labels</code> before sending them to the Docker Daemon \([https\://github\.com/ansible\-collections/community\.docker/pull/985](https\://github\.com/ansible\-collections/community\.docker/pull/985)\)\.
* docker\_secret \- make sure to sanitize <code>labels</code> before sending them to the Docker Daemon \([https\://github\.com/ansible\-collections/community\.docker/pull/985](https\://github\.com/ansible\-collections/community\.docker/pull/985)\)\.
* docker\_swarm \- make sure to sanitize <code>labels</code> before sending them to the Docker Daemon \([https\://github\.com/ansible\-collections/community\.docker/pull/985](https\://github\.com/ansible\-collections/community\.docker/pull/985)\)\.
* docker\_swarm\_service \- make sure to sanitize <code>labels</code> and <code>container\_labels</code> before sending them to the Docker Daemon \([https\://github\.com/ansible\-collections/community\.docker/pull/985](https\://github\.com/ansible\-collections/community\.docker/pull/985)\)\.
* docker\_volume \- make sure to sanitize <code>labels</code> before sending them to the Docker Daemon \([https\://github\.com/ansible\-collections/community\.docker/pull/985](https\://github\.com/ansible\-collections/community\.docker/pull/985)\)\.

<a id="community-general-1"></a>
#### community\.general

* dnf\_config\_manager \- fix hanging when prompting to import GPG keys \([https\://github\.com/ansible\-collections/community\.general/pull/9124](https\://github\.com/ansible\-collections/community\.general/pull/9124)\, [https\://github\.com/ansible\-collections/community\.general/issues/8830](https\://github\.com/ansible\-collections/community\.general/issues/8830)\)\.
* dnf\_config\_manager \- forces locale to <code>C</code> before module starts\. If the locale was set to non\-English\, the output of the <code>dnf config\-manager</code> could not be parsed \([https\://github\.com/ansible\-collections/community\.general/pull/9157](https\://github\.com/ansible\-collections/community\.general/pull/9157)\, [https\://github\.com/ansible\-collections/community\.general/issues/9046](https\://github\.com/ansible\-collections/community\.general/issues/9046)\)\.
* flatpak \- force the locale language to <code>C</code> when running the flatpak command \([https\://github\.com/ansible\-collections/community\.general/pull/9187](https\://github\.com/ansible\-collections/community\.general/pull/9187)\, [https\://github\.com/ansible\-collections/community\.general/issues/8883](https\://github\.com/ansible\-collections/community\.general/issues/8883)\)\.
* github\_key \- in check mode\, a faulty call to <code>\`datetime\.strftime\(\.\.\.\)\`</code> was being made which generated an exception \([https\://github\.com/ansible\-collections/community\.general/issues/9185](https\://github\.com/ansible\-collections/community\.general/issues/9185)\)\.
* homebrew\_cask \- allow <code>\+</code> symbol in Homebrew cask name validation regex \([https\://github\.com/ansible\-collections/community\.general/pull/9128](https\://github\.com/ansible\-collections/community\.general/pull/9128)\)\.
* keycloak\_client \- fix diff by removing code that turns the attributes dict which contains additional settings into a list \([https\://github\.com/ansible\-collections/community\.general/pull/9077](https\://github\.com/ansible\-collections/community\.general/pull/9077)\)\.
* keycloak\_clientscope \- fix diff and <code>end\_state</code> by removing the code that turns the attributes dict\, which contains additional config items\, into a list \([https\://github\.com/ansible\-collections/community\.general/pull/9082](https\://github\.com/ansible\-collections/community\.general/pull/9082)\)\.
* keycloak\_clientscope\_type \- sort the default and optional clientscope lists to improve the diff \([https\://github\.com/ansible\-collections/community\.general/pull/9202](https\://github\.com/ansible\-collections/community\.general/pull/9202)\)\.
* redfish\_utils module utils \- remove undocumented default applytime \([https\://github\.com/ansible\-collections/community\.general/pull/9114](https\://github\.com/ansible\-collections/community\.general/pull/9114)\)\.
* slack \- fail if Slack API response is not OK with error message \([https\://github\.com/ansible\-collections/community\.general/pull/9198](https\://github\.com/ansible\-collections/community\.general/pull/9198)\)\.

<a id="community-mysql-1"></a>
#### community\.mysql

* mysql\_user\,mysql\_role \- The sql\_mode ANSI\_QUOTES affects how the modules mysql\_user and mysql\_role compare the existing privileges with the configured privileges\, as well as decide whether double quotes or backticks should be used in the GRANT statements\. Pointing out in issue 671\, the modules mysql\_user and mysql\_role allow users to enable/disable ANSI\_QUOTES in session variable \(within a DB session\, the session variable always overwrites the global one\)\. But due to the issue\, the modules do not check for ANSI\_MODE in the session variable\, instead\, they only check in the GLOBAL one\.That behavior is not only limiting the users\' flexibility\, but also not allowing users to explicitly disable ANSI\_MODE to work around such bugs like [https\://bugs\.mysql\.com/bug\.php\?id\=115953](https\://bugs\.mysql\.com/bug\.php\?id\=115953)\. \([https\://github\.com/ansible\-collections/community\.mysql/issues/671](https\://github\.com/ansible\-collections/community\.mysql/issues/671)\)

<a id="community-postgresql-1"></a>
#### community\.postgresql

* postgresql\_pg\_hba \- fixes \#420 by properly handling hash\-symbols in quotes \([https\://github\.com/ansible\-collections/community\.postgresql/pull/766](https\://github\.com/ansible\-collections/community\.postgresql/pull/766)\)
* postgresql\_pg\_hba \- fixes \#705 by preventing invalid strings to be written \([https\://github\.com/ansible\-collections/community\.postgresql/pull/761](https\://github\.com/ansible\-collections/community\.postgresql/pull/761)\)
* postgresql\_pg\_hba \- fixes \#730 by extending the key we use to identify a rule with the connection type \([https\://github\.com/ansible\-collections/community\.postgresql/pull/770](https\://github\.com/ansible\-collections/community\.postgresql/pull/770)\)
* postgresql\_pg\_hba \- improves parsing of quoted strings and escaped newlines \([https\://github\.com/ansible\-collections/community\.postgresql/pull/761](https\://github\.com/ansible\-collections/community\.postgresql/pull/761)\)
* postgresql\_user \- doesn\'t take password\_encryption into account when checking if a password should be updated \([https\://github\.com/ansible\-collections/community\.postgresql/issues/688](https\://github\.com/ansible\-collections/community\.postgresql/issues/688)\)\.

<a id="community-vmware"></a>
#### community\.vmware

* vm\_device\_helper \- Fix \'invalid configuration for device\' error caused by missing fileoperation parameter\. \([https\://github\.com/ansible\-collections/community\.vmware/pull/2009](https\://github\.com/ansible\-collections/community\.vmware/pull/2009)\)\.
* vmware\_guest \- Fix errors occuring during hardware version upgrade not being reported\. \([https\://github\.com/ansible\-collections/community\.vmware/pull/2010](https\://github\.com/ansible\-collections/community\.vmware/pull/2010)\)\.
* vmware\_guest \- Fix vmware\_guest always reporting change when using dvswitch\. \([https\://github\.com/ansible\-collections/community\.vmware/pull/2000](https\://github\.com/ansible\-collections/community\.vmware/pull/2000)\)\.

<a id="fortinet-fortimanager-1"></a>
#### fortinet\.fortimanager

* Changed all input argument name in ansible built\-in documentation to the underscore format\. E\.g\.\, changed \"var\-name\" to \"var\_name\"\.
* Fixed a bug where rc\_failed and rc\_succeeded did not work\.
* Improved code logic\, reduced redundant requests for system information\.
* Modified built\-in document to support sanity tests in ansible\-core 2\.18\.0\. No functionality changed\.

<a id="infoblox-nios-modules"></a>
#### infoblox\.nios\_modules

* For Host IPv6\, the mac parameter has been renamed to duid\.
* Refined Host record return fields to ensure use\_nextserver and nextserver are only included for IPv4\, as these fields are not applicable to IPv6\.

<a id="netapp-ontap-1"></a>
#### netapp\.ontap

* all modules supporting REST \- avoid duplicate calls to api/cluster to get ONTAP version\.
* na\_ontap\_broadcast\_domain \- fix issue with port modification in REST\.
* na\_ontap\_flexcache \- fix typo error in the query \'origins\.cluster\.name\' in REST\.
* na\_ontap\_rest\_info \- rectified subset name to <em class="title-reference">cluster/firmware/history</em>\.
* na\_ontap\_snapshot\_policy \- fix issue with \'retention\_period\' in REST\.

<a id="purestorage-flasharray-1"></a>
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

<a id="telekom-mms-icinga-director"></a>
#### telekom\_mms\.icinga\_director

* Add Icinga notification template imports \([https\://github\.com/telekom\-mms/ansible\-collection\-icinga\-director/pull/267](https\://github\.com/telekom\-mms/ansible\-collection\-icinga\-director/pull/267)\)

<a id="vmware-vmware-1"></a>
#### vmware\.vmware

* content\_library\_item\_info \- Library name and ID are ignored if item ID is provided so updated docs and arg parse rules to reflect this

<a id="known-issues"></a>
### Known Issues

<a id="dellemc-openmanage-1"></a>
#### dellemc\.openmanage

* idrac\_diagnostics \- Issue\(285322\) \- This module doesn\'t support export of diagnostics file to HTTP and HTTPS share via SOCKS proxy\.
* idrac\_firmware \- Issue\(279282\) \- This module does not support firmware update using HTTP\, HTTPS\, and FTP shares with authentication on iDRAC8\.
* ome\_smart\_fabric\_uplink \- Issue\(186024\) \- The module supported by OpenManage Enterprise Modular\, however it does not allow the creation of multiple uplinks of the same name\. If an uplink is created using the same name as an existing uplink\, then the existing uplink is modified\.

<a id="new-plugins"></a>
### New Plugins

<a id="filter"></a>
#### Filter

* community\.dns\.reverse\_pointer \- Convert an IP address into a DNS name for reverse lookup\.

<a id="lookup"></a>
#### Lookup

* community\.dns\.reverse\_lookup \- Reverse\-look up IP addresses\.

<a id="new-modules"></a>
### New Modules

<a id="fortinet-fortimanager-2"></a>
#### fortinet\.fortimanager

* fortinet\.fortimanager\.fmgr\_pkg\_videofilter\_youtubekey \- Configure YouTube API keys\.

<a id="netapp-ontap-2"></a>
#### netapp\.ontap

* netapp\.ontap\.na\_ontap\_bgp\_config \- NetApp ONTAP network BGP configuration
* netapp\.ontap\.na\_ontap\_cifs\_privileges \- NetApp ONTAP CIFS privileges

<a id="unchanged-collections"></a>
### Unchanged Collections

* amazon\.aws \(still version 8\.2\.1\)
* ansible\.netcommon \(still version 6\.1\.3\)
* ansible\.posix \(still version 1\.6\.2\)
* ansible\.utils \(still version 4\.1\.0\)
* ansible\.windows \(still version 2\.5\.0\)
* arista\.eos \(still version 9\.0\.0\)
* awx\.awx \(still version 24\.6\.1\)
* azure\.azcollection \(still version 2\.7\.0\)
* check\_point\.mgmt \(still version 5\.2\.3\)
* chocolatey\.chocolatey \(still version 1\.5\.3\)
* cisco\.aci \(still version 2\.10\.1\)
* cisco\.asa \(still version 5\.0\.1\)
* cisco\.intersight \(still version 2\.0\.20\)
* cisco\.ios \(still version 8\.0\.0\)
* cisco\.iosxr \(still version 9\.0\.0\)
* cisco\.meraki \(still version 2\.18\.3\)
* cisco\.mso \(still version 2\.9\.0\)
* cisco\.nxos \(still version 8\.1\.0\)
* cisco\.ucs \(still version 1\.14\.0\)
* cloud\.common \(still version 3\.0\.0\)
* cloudscale\_ch\.cloud \(still version 2\.4\.0\)
* community\.aws \(still version 8\.0\.0\)
* community\.ciscosmb \(still version 1\.0\.9\)
* community\.crypto \(still version 2\.22\.3\)
* community\.digitalocean \(still version 1\.27\.0\)
* community\.grafana \(still version 1\.9\.1\)
* community\.hashi\_vault \(still version 6\.2\.0\)
* community\.hrobot \(still version 2\.0\.2\)
* community\.library\_inventory\_filtering\_v1 \(still version 1\.0\.2\)
* community\.libvirt \(still version 1\.3\.0\)
* community\.mongodb \(still version 1\.7\.8\)
* community\.network \(still version 5\.1\.0\)
* community\.okd \(still version 3\.0\.1\)
* community\.proxysql \(still version 1\.6\.0\)
* community\.rabbitmq \(still version 1\.3\.0\)
* community\.routeros \(still version 2\.20\.0\)
* community\.sap\_libs \(still version 1\.4\.2\)
* community\.sops \(still version 1\.9\.1\)
* community\.windows \(still version 2\.3\.0\)
* community\.zabbix \(still version 2\.5\.1\)
* containers\.podman \(still version 1\.16\.2\)
* cyberark\.conjur \(still version 1\.3\.1\)
* dellemc\.enterprise\_sonic \(still version 2\.5\.1\)
* dellemc\.powerflex \(still version 2\.5\.0\)
* dellemc\.unity \(still version 2\.0\.0\)
* f5networks\.f5\_modules \(still version 1\.32\.1\)
* fortinet\.fortios \(still version 2\.3\.8\)
* frr\.frr \(still version 2\.0\.2\)
* google\.cloud \(still version 1\.4\.1\)
* grafana\.grafana \(still version 5\.6\.0\)
* hetzner\.hcloud \(still version 3\.1\.1\)
* ibm\.qradar \(still version 3\.0\.0\)
* ibm\.spectrum\_virtualize \(still version 2\.0\.0\)
* ibm\.storage\_virtualize \(still version 2\.5\.0\)
* ieisystem\.inmanage \(still version 2\.0\.0\)
* infinidat\.infinibox \(still version 1\.4\.5\)
* inspur\.ispim \(still version 2\.2\.3\)
* inspur\.sm \(still version 2\.3\.0\)
* junipernetworks\.junos \(still version 8\.0\.0\)
* kaytus\.ksmanage \(still version 1\.2\.2\)
* kubernetes\.core \(still version 3\.2\.0\)
* kubevirt\.core \(still version 1\.5\.0\)
* lowlydba\.sqlserver \(still version 2\.3\.4\)
* microsoft\.ad \(still version 1\.7\.1\)
* netapp\.cloudmanager \(still version 21\.24\.0\)
* netapp\.storagegrid \(still version 21\.13\.0\)
* netapp\_eseries\.santricity \(still version 1\.4\.1\)
* netbox\.netbox \(still version 3\.20\.0\)
* ngine\_io\.cloudstack \(still version 2\.5\.0\)
* ngine\_io\.exoscale \(still version 1\.1\.0\)
* openvswitch\.openvswitch \(still version 2\.1\.1\)
* ovirt\.ovirt \(still version 3\.2\.0\)
* purestorage\.flashblade \(still version 1\.19\.1\)
* sensu\.sensu\_go \(still version 1\.14\.0\)
* splunk\.es \(still version 3\.0\.0\)
* t\_systems\_mms\.icinga\_director \(still version 2\.0\.1\)
* theforeman\.foreman \(still version 4\.2\.0\)
* vmware\.vmware\_rest \(still version 3\.2\.0\)
* vultr\.cloud \(still version 1\.13\.0\)
* vyos\.vyos \(still version 4\.1\.0\)
* wti\.remote \(still version 1\.0\.10\)

<a id="v10-6-0"></a>
## v10\.6\.0

- <a href="#release-summary-1">Release Summary</a>
- <a href="#ansible-core-4">Ansible\-core</a>
- <a href="#changed-collections-1">Changed Collections</a>
- <a href="#major-changes-1">Major Changes</a>
    - <a href="#ansible-posix">ansible\.posix</a>
    - <a href="#dellemc-openmanage-2">dellemc\.openmanage</a>
    - <a href="#fortinet-fortios">fortinet\.fortios</a>
    - <a href="#grafana-grafana">grafana\.grafana</a>
- <a href="#minor-changes-1">Minor Changes</a>
    - <a href="#ansible-core-5">Ansible\-core</a>
    - <a href="#ansible-posix-1">ansible\.posix</a>
    - <a href="#cisco-dnac-1">cisco\.dnac</a>
    - <a href="#community-general-2">community\.general</a>
    - <a href="#community-postgresql-2">community\.postgresql</a>
    - <a href="#community-routeros">community\.routeros</a>
    - <a href="#community-vmware-1">community\.vmware</a>
    - <a href="#dellemc-openmanage-3">dellemc\.openmanage</a>
    - <a href="#f5networks-f5-modules">f5networks\.f5\_modules</a>
    - <a href="#netapp-cloudmanager">netapp\.cloudmanager</a>
    - <a href="#purestorage-flashblade">purestorage\.flashblade</a>
    - <a href="#telekom-mms-icinga-director-1">telekom\_mms\.icinga\_director</a>
    - <a href="#vmware-vmware-2">vmware\.vmware</a>
- <a href="#deprecated-features-1">Deprecated Features</a>
    - <a href="#community-network">community\.network</a>
    - <a href="#community-vmware-2">community\.vmware</a>
- <a href="#security-fixes-1">Security Fixes</a>
    - <a href="#ansible-core-6">Ansible\-core</a>
- <a href="#bugfixes-1">Bugfixes</a>
    - <a href="#ansible-core-7">Ansible\-core</a>
    - <a href="#ansible-posix-2">ansible\.posix</a>
    - <a href="#cisco-ise-1">cisco\.ise</a>
    - <a href="#cisco-meraki">cisco\.meraki</a>
    - <a href="#community-crypto">community\.crypto</a>
    - <a href="#community-dns-2">community\.dns</a>
    - <a href="#community-docker-1">community\.docker</a>
    - <a href="#community-general-3">community\.general</a>
    - <a href="#community-postgresql-3">community\.postgresql</a>
    - <a href="#community-vmware-3">community\.vmware</a>
    - <a href="#containers-podman">containers\.podman</a>
    - <a href="#dellemc-openmanage-4">dellemc\.openmanage</a>
    - <a href="#f5networks-f5-modules-1">f5networks\.f5\_modules</a>
    - <a href="#fortinet-fortios-1">fortinet\.fortios</a>
    - <a href="#purestorage-flashblade-1">purestorage\.flashblade</a>
    - <a href="#vmware-vmware-3">vmware\.vmware</a>
- <a href="#known-issues-1">Known Issues</a>
    - <a href="#dellemc-openmanage-5">dellemc\.openmanage</a>
- <a href="#new-modules-1">New Modules</a>
    - <a href="#purestorage-flashblade-2">purestorage\.flashblade</a>
- <a href="#unchanged-collections-1">Unchanged Collections</a>

<a id="release-summary-1"></a>
### Release Summary

Release Date\: 2024\-11\-05

[Porting Guide](https\://docs\.ansible\.com/ansible/devel/porting\_guides\.html)

<a id="ansible-core-4"></a>
### Ansible\-core

Ansible 10\.6\.0 contains ansible\-core version 2\.17\.6\.
This is a newer version than version 2\.17\.5 contained in the previous Ansible release\.

The changes are reported in the combined changelog below\.

<a id="changed-collections-1"></a>
### Changed Collections

If not mentioned explicitly\, the changes are reported in the combined changelog below\.

| Collection                               | Ansible 10.5.0 | Ansible 10.6.0 | Notes                                                                                                                                                                                                        |
| ---------------------------------------- | -------------- | -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| ansible.posix                            | 1.5.4          | 1.6.2          |                                                                                                                                                                                                              |
| cisco.dnac                               | 6.20.0         | 6.22.0         |                                                                                                                                                                                                              |
| cisco.ise                                | 2.9.3          | 2.9.5          |                                                                                                                                                                                                              |
| cisco.meraki                             | 2.18.2         | 2.18.3         |                                                                                                                                                                                                              |
| community.crypto                         | 2.22.1         | 2.22.3         |                                                                                                                                                                                                              |
| community.dns                            | 3.0.5          | 3.0.6          |                                                                                                                                                                                                              |
| community.docker                         | 3.13.0         | 3.13.1         |                                                                                                                                                                                                              |
| community.general                        | 9.5.0          | 9.5.1          |                                                                                                                                                                                                              |
| community.library_inventory_filtering_v1 | 1.0.1          | 1.0.2          |                                                                                                                                                                                                              |
| community.mongodb                        | 1.7.7          | 1.7.8          | There are no changes recorded in the changelog.                                                                                                                                                              |
| community.network                        | 5.0.3          | 5.1.0          |                                                                                                                                                                                                              |
| community.postgresql                     | 3.6.1          | 3.7.0          |                                                                                                                                                                                                              |
| community.routeros                       | 2.19.0         | 2.20.0         |                                                                                                                                                                                                              |
| community.vmware                         | 4.7.1          | 4.8.0          |                                                                                                                                                                                                              |
| containers.podman                        | 1.16.1         | 1.16.2         |                                                                                                                                                                                                              |
| cyberark.conjur                          | 1.3.0          | 1.3.1          | You can find the collection's changelog at [https://github.com/cyberark/ansible-conjur-collection/blob/master/CHANGELOG.md](https://github.com/cyberark/ansible-conjur-collection/blob/master/CHANGELOG.md). |
| dellemc.openmanage                       | 9.7.0          | 9.8.0          |                                                                                                                                                                                                              |
| f5networks.f5_modules                    | 1.31.0         | 1.32.1         |                                                                                                                                                                                                              |
| fortinet.fortios                         | 2.3.7          | 2.3.8          |                                                                                                                                                                                                              |
| grafana.grafana                          | 5.5.1          | 5.6.0          |                                                                                                                                                                                                              |
| netapp.cloudmanager                      | 21.22.1        | 21.24.0        |                                                                                                                                                                                                              |
| netapp.storagegrid                       | 21.12.0        | 21.13.0        | There are no changes recorded in the changelog.                                                                                                                                                              |
| purestorage.flashblade                   | 1.18.0         | 1.19.1         |                                                                                                                                                                                                              |
| telekom_mms.icinga_director              | 2.1.2          | 2.2.0          |                                                                                                                                                                                                              |
| vmware.vmware                            | 1.5.0          | 1.6.0          |                                                                                                                                                                                                              |

<a id="major-changes-1"></a>
### Major Changes

<a id="ansible-posix"></a>
#### ansible\.posix

* Dropping support for Ansible 2\.9\, ansible\-core 2\.15 will be minimum required version for this release

<a id="dellemc-openmanage-2"></a>
#### dellemc\.openmanage

* omevv\_firmware\_repository\_profile \- This module allows to manage firmware repository profile\.
* omevv\_firmware\_repository\_profile\_info \- This module allows to retrieve firmware repository profile information\.
* omevv\_vcenter\_info \- This module allows to retrieve vCenter information\.

<a id="fortinet-fortios"></a>
#### fortinet\.fortios

* Improve the logic for SET function to send GET request first then PUT or POST
* Mantis
* Support new FOS versions 7\.6\.0\.

<a id="grafana-grafana"></a>
#### grafana\.grafana

* Adding \"distributor\" section support to mimir config file by \@HamzaKhait in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/247](https\://github\.com/grafana/grafana\-ansible\-collection/pull/247)
* Allow alloy\_user\_groups variable again by \@pjezek in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/276](https\://github\.com/grafana/grafana\-ansible\-collection/pull/276)
* Alloy Role Improvements by \@voidquark in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/281](https\://github\.com/grafana/grafana\-ansible\-collection/pull/281)
* Bump ansible\-lint from 24\.6\.0 to 24\.9\.2 by \@dependabot in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/270](https\://github\.com/grafana/grafana\-ansible\-collection/pull/270)
* Bump pylint from 3\.2\.5 to 3\.3\.1 by \@dependabot in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/273](https\://github\.com/grafana/grafana\-ansible\-collection/pull/273)
* Ensure check\-mode works for otel collector by \@pieterlexis\-tomtom in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/264](https\://github\.com/grafana/grafana\-ansible\-collection/pull/264)
* Fix message argument of dashboard task by \@Nemental in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/256](https\://github\.com/grafana/grafana\-ansible\-collection/pull/256)
* Update Alloy variables to use the <em class="title-reference">grafana\_alloy\_</em> namespace so they are unique by \@Aethylred in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/209](https\://github\.com/grafana/grafana\-ansible\-collection/pull/209)
* Update README\.md by \@aioue in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/272](https\://github\.com/grafana/grafana\-ansible\-collection/pull/272)
* Update README\.md by \@aioue in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/275](https\://github\.com/grafana/grafana\-ansible\-collection/pull/275)
* Update main\.yml by \@aioue in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/274](https\://github\.com/grafana/grafana\-ansible\-collection/pull/274)
* add grafana\_plugins\_ops to defaults and docs by \@weakcamel in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/251](https\://github\.com/grafana/grafana\-ansible\-collection/pull/251)
* add option to populate google\_analytics\_4\_id value by \@copolycube in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/249](https\://github\.com/grafana/grafana\-ansible\-collection/pull/249)
* fix ansible\-lint warnings on Forbidden implicit octal value \"0640\" by \@copolycube in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/279](https\://github\.com/grafana/grafana\-ansible\-collection/pull/279)

<a id="minor-changes-1"></a>
### Minor Changes

<a id="ansible-core-5"></a>
#### Ansible\-core

* ansible\-test \- Improve container runtime probe error handling\. When unexpected probe output is encountered\, an error with more useful debugging information is provided\.

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

<a id="cisco-dnac-1"></a>
#### cisco\.dnac

* Added \'lan\_automation\_workflow\_manager\' to automate network discovery\, deployment\, and device configuration with LAN Automation\.
* Added \'sda\_extranet\_policies\_workflow\_manager\' to manage SDA Extranet Policies\.
* Added \'sda\_fabric\_devices\_workflow\_manager\' to manage SDA fabric devices\.
* Added \'sda\_fabric\_virtual\_networks\_workflow\_manager\' to configure fabric VLANs\, Virtual Networks\, and Anycast Gateways\.
* Added \'sda\_host\_port\_onboarding\_workflow\_manager\' to manage host port onboarding in SD\-Access Fabric\.
* Ansible utils requirement updated\.
* Bug fixes in accesspoint\_workflow\_manager module
* Bug fixes in network\_settings\_workflow\_manager module
* Bug fixes in pnp\_workflow\_manager module
* Changes in accesspoint\_workflow\_manager module\.
* Changes in device\_configs\_backup\_workflow\_manager module
* Changes in device\_credential\_workflow\_manager module\.
* Changes in dnac\.py
* Changes in dnac\.py to support common APIs
* Changes in events\_and\_notifications\_workflow\_manager module\.
* Changes in inventory\_workflow\_manager module\.
* Changes in ise\_radius\_integration\_workflow\_manager module\.
* Changes in sda\_fabric\_transits\_workflow\_manager module\.
* Changes in user\_role\_workflow\_manager module\.
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
* accesspoint\_workflow\_manager\.py \- added attribute \'factory\_reset\_aps\'\.
* device\_credential\_workflow\_manager\.py \- added attribute \'apply\_credentials\_to\_site\'\.
* inventory\_workflow\_manager\.py \- Removed attribute hostname\_list\, serial\_number\_list and mac\_address\_list
* inventory\_workflow\_manager\.py \- added attribute hostnames\, serial\_numbers and mac\_addresses

<a id="community-general-2"></a>
#### community\.general

* redfish\_utils module utils \- schedule a BIOS configuration job at next reboot when the BIOS config is changed \([https\://github\.com/ansible\-collections/community\.general/pull/9012](https\://github\.com/ansible\-collections/community\.general/pull/9012)\)\.

<a id="community-postgresql-2"></a>
#### community\.postgresql

* postgresql\_set \- adds the <code>queries</code> return value to return executed DML statements\.

<a id="community-routeros"></a>
#### community\.routeros

* api\_info\, api\_modify \- add new parameters from the RouterOS 7\.16 release \([https\://github\.com/ansible\-collections/community\.routeros/pull/323](https\://github\.com/ansible\-collections/community\.routeros/pull/323)\)\.
* api\_info\, api\_modify \- add support <code>interface l2tp\-client</code> configuration \([https\://github\.com/ansible\-collections/community\.routeros/pull/322](https\://github\.com/ansible\-collections/community\.routeros/pull/322)\)\.
* api\_info\, api\_modify \- add support for the <code>cpu\-frequency</code>\, <code>memory\-frequency</code>\, <code>preboot\-etherboot</code> and <code>preboot\-etherboot\-server</code> properties in <code>system routerboard settings</code> \([https\://github\.com/ansible\-collections/community\.routeros/pull/320](https\://github\.com/ansible\-collections/community\.routeros/pull/320)\)\.
* api\_info\, api\_modify \- add support for the <code>matching\-type</code> property in <code>ip dhcp\-server matcher</code> introduced by RouterOS 7\.16 \([https\://github\.com/ansible\-collections/community\.routeros/pull/321](https\://github\.com/ansible\-collections/community\.routeros/pull/321)\)\.

<a id="community-vmware-1"></a>
#### community\.vmware

* vmware\_vm\_info \- Improve performance when parsing custom attributes information \([https\://github\.com/ansible\-collections/community\.vmware/pull/2194](https\://github\.com/ansible\-collections/community\.vmware/pull/2194)\)

<a id="dellemc-openmanage-3"></a>
#### dellemc\.openmanage

* idrac\_firmware\_info \- This module is enhanced to support iDRAC10 and OMSDK dependency is removed\.

<a id="f5networks-f5-modules"></a>
#### f5networks\.f5\_modules

* bigip\_gtm\_server \- Added check for datacenter existence in Check Mode\.

<a id="netapp-cloudmanager"></a>
#### netapp\.cloudmanager

* na\_cloudmanager\_cvo\_aws \- increase timeout for creating cvo to 90 mins\.
* na\_cloudmanager\_cvo\_azure \- increase timeout for creating cvo to 90 mins\.
* na\_cloudmanager\_cvo\_gcp \- increase timeout for creating cvo to 90 mins\.

<a id="purestorage-flashblade"></a>
#### purestorage\.flashblade

* multiple \- YAML lint fixes based on updated <code>ansible\-lint</code> version
* purefb\_bucket \- Allow bucket quotas to be modified\.
* purefb\_info \- Add <code>time\_remaining\_status</code> to bucket information from REST 2\.14
* purefb\_info \- Expose SMTP encryption mode
* purefb\_policy \- Add new policy type of <code>worm</code> which is availble from Purity//FB 4\.5\.0
* purefb\_smtp \- Add encryption mode support from Purity//FB 4\.5\.0
* purefb\_snap \- Change <code>targets</code> to <code>target\` and from \`\`list</code> to <code>str</code>\. <code>targets</code> added as alias and code to ensure existing list in playbooks is translated as a string\.
* purefb\_syslog \- Enable <code>services</code> parameter and also the ability update existing syslog servers from REST 2\.14

<a id="telekom-mms-icinga-director-1"></a>
#### telekom\_mms\.icinga\_director

* Add vars parameter to user\_template and user modules \([https\://github\.com/telekom\-mms/ansible\-collection\-icinga\-director/pull/262](https\://github\.com/telekom\-mms/ansible\-collection\-icinga\-director/pull/262)\)

<a id="vmware-vmware-2"></a>
#### vmware\.vmware

* cluster\_dpm \- Migrated module from community\.vmware to configure DPM in a vCenter cluster
* cluster\_drs\_recommendations \- Migrated module from community\.vmware to apply any DRS recommendations the vCenter cluster may have

<a id="deprecated-features-1"></a>
### Deprecated Features

* The <code>community\.network</code> collection has been deprecated\.
  It will be removed from Ansible 12 if no one starts maintaining it again before Ansible 12\.
  See [Collections Removal Process for unmaintained collections](https\://docs\.ansible\.com/ansible/devel/community/collection\_contributors/collection\_package\_removal\.html\#unmaintained\-collections) for more details \([https\://forum\.ansible\.com/t/8030](https\://forum\.ansible\.com/t/8030)\)\.
* The google\.cloud collection will be removed from Ansible 12 due to violations of the Ansible inclusion requirements\.
  The collection has [unresolved sanity test failures](https\://github\.com/ansible\-collections/google\.cloud/issues/613)\.
  See [Collections Removal Process for collections not satisfying the collection requirements](https\://docs\.ansible\.com/ansible/devel/community/collection\_contributors/collection\_package\_removal\.html\#collections\-not\-satisfying\-the\-collection\-requirements) for more details\, including for how this can be cancelled \([https\://forum\.ansible\.com/t/8609](https\://forum\.ansible\.com/t/8609)\)\.
  After removal\, users can still install this collection with <code>ansible\-galaxy collection install google\.cloud</code>\.

<a id="community-network"></a>
#### community\.network

* This collection and all content in it is unmaintained and deprecated \([https\://forum\.ansible\.com/t/8030](https\://forum\.ansible\.com/t/8030)\)\. If you are interested in maintaining parts of the collection\, please copy them to your own repository\, and tell others about in the Forum discussion\. See the [collection creator path](https\://docs\.ansible\.com/ansible/devel/dev\_guide/developing\_collections\_path\.html) for details\.

<a id="community-vmware-2"></a>
#### community\.vmware

* vmware\_cluster\_dpm \- the module has been deprecated and will be removed in community\.vmware 6\.0\.0 \([https\://github\.com/ansible\-collections/community\.vmware/pull/2217](https\://github\.com/ansible\-collections/community\.vmware/pull/2217)\)\.
* vmware\_cluster\_drs\_recommendations \- the module has been deprecated and will be removed in community\.vmware 6\.0\.0 \([https\://github\.com/ansible\-collections/community\.vmware/pull/2218](https\://github\.com/ansible\-collections/community\.vmware/pull/2218)\)\.

<a id="security-fixes-1"></a>
### Security Fixes

<a id="ansible-core-6"></a>
#### Ansible\-core

* include\_vars action \- Ensure that result masking is correctly requested when vault\-encrypted files are read\. \(CVE\-2024\-8775\)
* task result processing \- Ensure that action\-sourced result masking \(<code>\_ansible\_no\_log\=True</code>\) is preserved\. \(CVE\-2024\-8775\)
* user action won\'t allow ssh\-keygen\, chown and chmod to run on existing ssh public key file\, avoiding traversal on existing symlinks \(CVE\-2024\-9902\)\.

<a id="bugfixes-1"></a>
### Bugfixes

<a id="ansible-core-7"></a>
#### Ansible\-core

* Fix disabling SSL verification when installing collections and roles from git repositories\. If <code>\-\-ignore\-certs</code> isn\'t provided\, the value for the <code>GALAXY\_IGNORE\_CERTS</code> configuration option will be used \([https\://github\.com/ansible/ansible/issues/83326](https\://github\.com/ansible/ansible/issues/83326)\)\.
* Improve performance on large inventories by reducing the number of implicit meta tasks\.
* Use the requested error message in the ansible\.module\_utils\.facts\.timeout timeout function instead of hardcoding one\.
* ansible\-test \- Enable the <code>sys\.unraisablehook</code> work\-around for the <code>pylint</code> sanity test on Python 3\.11\. Previously the work\-around was only enabled for Python 3\.12 and later\. However\, the same issue has been discovered on Python 3\.11\.
* debconf \- set empty password values \([https\://github\.com/ansible/ansible/issues/83214](https\://github\.com/ansible/ansible/issues/83214)\)\.
* facts \- skip if distribution file path is directory\, instead of raising error \([https\://github\.com/ansible/ansible/issues/84006](https\://github\.com/ansible/ansible/issues/84006)\)\.
* user action will now require O\(force\) to overwrite the public part of an ssh key when generating ssh keys\, as was already the case for the private part\.
* user module now avoids changing ownership of files symlinked in provided home dir skeleton

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

<a id="cisco-ise-1"></a>
#### cisco\.ise

* Collection not compatible with ansible\.utils 5\.x\.y
* Getting deployment info for entire deployment does not work
* cisco\.ise\.pan\_ha object has no attribute \'enable\_pan\_ha\'
* cisco\.ise\.support\_bundle\_download keeps failing after downloading the file

<a id="cisco-meraki"></a>
#### cisco\.meraki

* Ansible utils requirements updated\.
* cisco\.meraki\.networks\_clients\_info \- incorrect API endpoint\, fixing info module\.
* cisco\.meraki\.networks\_switch\_stacks delete stack not working\, fixing path parameters\.

<a id="community-crypto"></a>
#### community\.crypto

* acme\_\* modules \- when using the OpenSSL backend\, explicitly use the UTC timezone in Python code \([https\://github\.com/ansible\-collections/community\.crypto/pull/811](https\://github\.com/ansible\-collections/community\.crypto/pull/811)\)\.
* acme\_certificate \- fix authorization failure when CSR contains SANs with mixed case \([https\://github\.com/ansible\-collections/community\.crypto/pull/803](https\://github\.com/ansible\-collections/community\.crypto/pull/803)\)\.
* time module utils \- fix conversion of naive <code>datetime</code> objects to UNIX timestamps for Python 3 \([https\://github\.com/ansible\-collections/community\.crypto/issues/808](https\://github\.com/ansible\-collections/community\.crypto/issues/808)\, [https\://github\.com/ansible\-collections/community\.crypto/pull/810](https\://github\.com/ansible\-collections/community\.crypto/pull/810)\)\.

<a id="community-dns-2"></a>
#### community\.dns

* Update Public Suffix List\.

<a id="community-docker-1"></a>
#### community\.docker

* docker\_compose\_v2 \- improve parsing of dry\-run image build operations from JSON events \([https\://github\.com/ansible\-collections/community\.docker/issues/975](https\://github\.com/ansible\-collections/community\.docker/issues/975)\, [https\://github\.com/ansible\-collections/community\.docker/pull/976](https\://github\.com/ansible\-collections/community\.docker/pull/976)\)\.

<a id="community-general-3"></a>
#### community\.general

* bitwarden lookup plugin \- support BWS v0\.3\.0 syntax breaking change \([https\://github\.com/ansible\-collections/community\.general/pull/9028](https\://github\.com/ansible\-collections/community\.general/pull/9028)\)\.
* collection\_version lookup plugin \- use <code>importlib</code> directly instead of the deprecated and in ansible\-core 2\.19 removed <code>ansible\.module\_utils\.compat\.importlib</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9084](https\://github\.com/ansible\-collections/community\.general/pull/9084)\)\.
* gitlab\_label \- update label\'s color \([https\://github\.com/ansible\-collections/community\.general/pull/9010](https\://github\.com/ansible\-collections/community\.general/pull/9010)\)\.
* keycloak\_clientscope\_type \- fix detect changes in check mode \([https\://github\.com/ansible\-collections/community\.general/issues/9092](https\://github\.com/ansible\-collections/community\.general/issues/9092)\, [https\://github\.com/ansible\-collections/community\.general/pull/9093](https\://github\.com/ansible\-collections/community\.general/pull/9093)\)\.
* keycloak\_group \- fix crash caused in subgroup creation\. The crash was caused by a missing or empty <code>subGroups</code> property in Keycloak ≥23 \([https\://github\.com/ansible\-collections/community\.general/issues/8788](https\://github\.com/ansible\-collections/community\.general/issues/8788)\, [https\://github\.com/ansible\-collections/community\.general/pull/8979](https\://github\.com/ansible\-collections/community\.general/pull/8979)\)\.
* modprobe \- fix check mode not being honored for <code>persistent</code> option \([https\://github\.com/ansible\-collections/community\.general/issues/9051](https\://github\.com/ansible\-collections/community\.general/issues/9051)\, [https\://github\.com/ansible\-collections/community\.general/pull/9052](https\://github\.com/ansible\-collections/community\.general/pull/9052)\)\.
* one\_host \- fix if statements for cases when <code>ID\=0</code> \([https\://github\.com/ansible\-collections/community\.general/issues/1199](https\://github\.com/ansible\-collections/community\.general/issues/1199)\, [https\://github\.com/ansible\-collections/community\.general/pull/8907](https\://github\.com/ansible\-collections/community\.general/pull/8907)\)\.
* one\_image \- fix module failing due to a class method typo \([https\://github\.com/ansible\-collections/community\.general/pull/9056](https\://github\.com/ansible\-collections/community\.general/pull/9056)\)\.
* one\_image\_info \- fix module failing due to a class method typo \([https\://github\.com/ansible\-collections/community\.general/pull/9056](https\://github\.com/ansible\-collections/community\.general/pull/9056)\)\.
* one\_vnet \- fix module failing due to a variable typo \([https\://github\.com/ansible\-collections/community\.general/pull/9019](https\://github\.com/ansible\-collections/community\.general/pull/9019)\)\.
* redfish\_utils module utils \- fix issue with URI parsing to gracefully handling trailing slashes when extracting member identifiers \([https\://github\.com/ansible\-collections/community\.general/issues/9047](https\://github\.com/ansible\-collections/community\.general/issues/9047)\, [https\://github\.com/ansible\-collections/community\.general/pull/9057](https\://github\.com/ansible\-collections/community\.general/pull/9057)\)\.

<a id="community-postgresql-3"></a>
#### community\.postgresql

* postgresql\_set \- fixes resetting logic to allow resetting shared\_preload\_libraries with <code>reset\: true</code> \([https\://github\.com/ansible\-collections/community\.postgresql/issues/744](https\://github\.com/ansible\-collections/community\.postgresql/issues/744)\)\.
* postgresql\_set \- forbids resetting shared\_preload\_libraries by passing an empty string \([https\://github\.com/ansible\-collections/community\.postgresql/issues/744](https\://github\.com/ansible\-collections/community\.postgresql/issues/744)\)\.

<a id="community-vmware-3"></a>
#### community\.vmware

* vmware\_guest \- Fix existing disk erroneously being re\-created when modifying vm with 8 or more disks\. \([https\://github\.com/ansible\-collections/community\.vmware/pull/2173](https\://github\.com/ansible\-collections/community\.vmware/pull/2173)\)\.
* vmware\_vmotion \- Fix a <em class="title-reference">list index out of range</em> error when vSphere doesn\'t provide a placement recommendation \([https\://github\.com/ansible\-collections/community\.vmware/pull/2208](https\://github\.com/ansible\-collections/community\.vmware/pull/2208)\)\.

<a id="containers-podman"></a>
#### containers\.podman

* Add missing parameters for podman container quadlet
* Add new options for podman\_network
* Add option to specify kube file content in module
* Add quadlet file mode option to specify file permission
* Add secret to login module
* Don\'t check image availability in Quadlet
* Fix max\_size idempotency issue
* Fix typo in quadlet generator
* Fix unsupported pull policy in example on podman\_container\.py
* fix quadlet cmd\_args append mistake
* podman\_login does not support check\_mode

<a id="dellemc-openmanage-4"></a>
#### dellemc\.openmanage

* idrac\_storage\_volume \- Issue\(290766\) \- The module will report success instead of showing failure for new virtual creation on the BOSS\-N1 controller if a virtual disk is already present on the same controller\.
* idrac\_support\_assist \- Issue\(308550\) \- This module fails when the NFS share path contains sub directory\.
* ome\_diagnostics \- Issue\(279193\) \- Export of SupportAssist collection logs to the share location fails on OME version 4\.0\.0\.

<a id="f5networks-f5-modules-1"></a>
#### f5networks\.f5\_modules

* bigip\_imish\_config \- fixed a bug that resulted in incomplete config when using BGV route domain

<a id="fortinet-fortios-1"></a>
#### fortinet\.fortios

* Github
* Mantis
* Return invalid json content instead of error while adding redundant comma at the end of the last variable in <em class="title-reference">fortios\_json\_generic</em>\.

<a id="purestorage-flashblade-1"></a>
#### purestorage\.flashblade

* purefb\_certs \- Fix issue with importing certificates
* purefb\_certs \- Fix parameter mispelling of <code>intermeadiate\_cert</code> to <code>intermediate\_cert</code>\. Keep original mispelling as an alias\.
* purefb\_ds \- Initialize variable correctly
* purefb\_policy \- Initialize variable correctly
* purefb\_ra \- Fix incorrect import statement
* purefb\_snap \- Fix issue with immeadiate remote snapshots not executing

<a id="vmware-vmware-3"></a>
#### vmware\.vmware

* Fix typos in all module documentation and README
* cluster\_drs \- fixed backwards vMotion rate \(input 1 set rate to 5 in vCenter\) \([https\://github\.com/ansible\-collections/vmware\.vmware/issues/68](https\://github\.com/ansible\-collections/vmware\.vmware/issues/68)\)

<a id="known-issues-1"></a>
### Known Issues

<a id="dellemc-openmanage-5"></a>
#### dellemc\.openmanage

* idrac\_diagnostics \- Issue\(285322\) \- This module doesn\'t support export of diagnostics file to HTTP and HTTPS share via SOCKS proxy\.
* idrac\_firmware \- Issue\(279282\) \- This module does not support firmware update using HTTP\, HTTPS\, and FTP shares with authentication on iDRAC8\.
* ome\_smart\_fabric\_uplink \- Issue\(186024\) \- The module supported by OpenManage Enterprise Modular\, however it does not allow the creation of multiple uplinks of the same name\. If an uplink is created using the same name as an existing uplink\, then the existing uplink is modified\.

<a id="new-modules-1"></a>
### New Modules

<a id="purestorage-flashblade-2"></a>
#### purestorage\.flashblade

* purestorage\.flashblade\.purefb\_saml \- Manage FlashBlade SAML2 service and identity providers

<a id="unchanged-collections-1"></a>
### Unchanged Collections

* amazon\.aws \(still version 8\.2\.1\)
* ansible\.netcommon \(still version 6\.1\.3\)
* ansible\.utils \(still version 4\.1\.0\)
* ansible\.windows \(still version 2\.5\.0\)
* arista\.eos \(still version 9\.0\.0\)
* awx\.awx \(still version 24\.6\.1\)
* azure\.azcollection \(still version 2\.7\.0\)
* check\_point\.mgmt \(still version 5\.2\.3\)
* chocolatey\.chocolatey \(still version 1\.5\.3\)
* cisco\.aci \(still version 2\.10\.1\)
* cisco\.asa \(still version 5\.0\.1\)
* cisco\.intersight \(still version 2\.0\.20\)
* cisco\.ios \(still version 8\.0\.0\)
* cisco\.iosxr \(still version 9\.0\.0\)
* cisco\.mso \(still version 2\.9\.0\)
* cisco\.nxos \(still version 8\.1\.0\)
* cisco\.ucs \(still version 1\.14\.0\)
* cloud\.common \(still version 3\.0\.0\)
* cloudscale\_ch\.cloud \(still version 2\.4\.0\)
* community\.aws \(still version 8\.0\.0\)
* community\.ciscosmb \(still version 1\.0\.9\)
* community\.digitalocean \(still version 1\.27\.0\)
* community\.grafana \(still version 1\.9\.1\)
* community\.hashi\_vault \(still version 6\.2\.0\)
* community\.hrobot \(still version 2\.0\.2\)
* community\.libvirt \(still version 1\.3\.0\)
* community\.mysql \(still version 3\.10\.3\)
* community\.okd \(still version 3\.0\.1\)
* community\.proxysql \(still version 1\.6\.0\)
* community\.rabbitmq \(still version 1\.3\.0\)
* community\.sap\_libs \(still version 1\.4\.2\)
* community\.sops \(still version 1\.9\.1\)
* community\.windows \(still version 2\.3\.0\)
* community\.zabbix \(still version 2\.5\.1\)
* cyberark\.pas \(still version 1\.0\.27\)
* dellemc\.enterprise\_sonic \(still version 2\.5\.1\)
* dellemc\.powerflex \(still version 2\.5\.0\)
* dellemc\.unity \(still version 2\.0\.0\)
* fortinet\.fortimanager \(still version 2\.7\.0\)
* frr\.frr \(still version 2\.0\.2\)
* google\.cloud \(still version 1\.4\.1\)
* hetzner\.hcloud \(still version 3\.1\.1\)
* ibm\.qradar \(still version 3\.0\.0\)
* ibm\.spectrum\_virtualize \(still version 2\.0\.0\)
* ibm\.storage\_virtualize \(still version 2\.5\.0\)
* ieisystem\.inmanage \(still version 2\.0\.0\)
* infinidat\.infinibox \(still version 1\.4\.5\)
* infoblox\.nios\_modules \(still version 1\.7\.0\)
* inspur\.ispim \(still version 2\.2\.3\)
* inspur\.sm \(still version 2\.3\.0\)
* junipernetworks\.junos \(still version 8\.0\.0\)
* kaytus\.ksmanage \(still version 1\.2\.2\)
* kubernetes\.core \(still version 3\.2\.0\)
* kubevirt\.core \(still version 1\.5\.0\)
* lowlydba\.sqlserver \(still version 2\.3\.4\)
* microsoft\.ad \(still version 1\.7\.1\)
* netapp\.ontap \(still version 22\.12\.0\)
* netapp\_eseries\.santricity \(still version 1\.4\.1\)
* netbox\.netbox \(still version 3\.20\.0\)
* ngine\_io\.cloudstack \(still version 2\.5\.0\)
* ngine\_io\.exoscale \(still version 1\.1\.0\)
* openstack\.cloud \(still version 2\.2\.0\)
* openvswitch\.openvswitch \(still version 2\.1\.1\)
* ovirt\.ovirt \(still version 3\.2\.0\)
* purestorage\.flasharray \(still version 1\.31\.1\)
* sensu\.sensu\_go \(still version 1\.14\.0\)
* splunk\.es \(still version 3\.0\.0\)
* t\_systems\_mms\.icinga\_director \(still version 2\.0\.1\)
* theforeman\.foreman \(still version 4\.2\.0\)
* vmware\.vmware\_rest \(still version 3\.2\.0\)
* vultr\.cloud \(still version 1\.13\.0\)
* vyos\.vyos \(still version 4\.1\.0\)
* wti\.remote \(still version 1\.0\.10\)

<a id="v10-5-0"></a>
## v10\.5\.0

- <a href="#release-summary-2">Release Summary</a>
- <a href="#ansible-core-8">Ansible\-core</a>
- <a href="#changed-collections-2">Changed Collections</a>
- <a href="#major-changes-2">Major Changes</a>
    - <a href="#dellemc-openmanage-6">dellemc\.openmanage</a>
- <a href="#minor-changes-2">Minor Changes</a>
    - <a href="#chocolatey-chocolatey">chocolatey\.chocolatey</a>
    - <a href="#cisco-dnac-2">cisco\.dnac</a>
    - <a href="#cisco-meraki-1">cisco\.meraki</a>
    - <a href="#community-general-4">community\.general</a>
    - <a href="#community-postgresql-4">community\.postgresql</a>
    - <a href="#containers-podman-1">containers\.podman</a>
    - <a href="#f5networks-f5-modules-2">f5networks\.f5\_modules</a>
    - <a href="#ibm-storage-virtualize">ibm\.storage\_virtualize</a>
    - <a href="#infoblox-nios-modules-1">infoblox\.nios\_modules</a>
    - <a href="#netbox-netbox">netbox\.netbox</a>
    - <a href="#ngine-io-cloudstack">ngine\_io\.cloudstack</a>
    - <a href="#vmware-vmware-rest">vmware\.vmware\_rest</a>
- <a href="#deprecated-features-2">Deprecated Features</a>
    - <a href="#community-general-5">community\.general</a>
- <a href="#bugfixes-2">Bugfixes</a>
    - <a href="#ansible-core-9">Ansible\-core</a>
    - <a href="#chocolatey-chocolatey-1">chocolatey\.chocolatey</a>
    - <a href="#community-crypto-1">community\.crypto</a>
    - <a href="#community-dns-3">community\.dns</a>
    - <a href="#community-docker-2">community\.docker</a>
    - <a href="#community-general-6">community\.general</a>
    - <a href="#community-postgresql-5">community\.postgresql</a>
    - <a href="#community-sops">community\.sops</a>
    - <a href="#community-vmware-4">community\.vmware</a>
    - <a href="#containers-podman-2">containers\.podman</a>
    - <a href="#dellemc-enterprise-sonic">dellemc\.enterprise\_sonic</a>
    - <a href="#dellemc-openmanage-7">dellemc\.openmanage</a>
    - <a href="#ibm-storage-virtualize-1">ibm\.storage\_virtualize</a>
    - <a href="#infoblox-nios-modules-2">infoblox\.nios\_modules</a>
    - <a href="#lowlydba-sqlserver">lowlydba\.sqlserver</a>
    - <a href="#netapp-eseries-santricity">netapp\_eseries\.santricity</a>
    - <a href="#netbox-netbox-1">netbox\.netbox</a>
    - <a href="#ngine-io-cloudstack-1">ngine\_io\.cloudstack</a>
- <a href="#known-issues-2">Known Issues</a>
    - <a href="#dellemc-openmanage-8">dellemc\.openmanage</a>
- <a href="#new-modules-2">New Modules</a>
    - <a href="#community-docker-3">community\.docker</a>
    - <a href="#community-general-7">community\.general</a>
    - <a href="#containers-podman-3">containers\.podman</a>
    - <a href="#infoblox-nios-modules-3">infoblox\.nios\_modules</a>
    - <a href="#netbox-netbox-2">netbox\.netbox</a>
- <a href="#unchanged-collections-2">Unchanged Collections</a>

<a id="release-summary-2"></a>
### Release Summary

Release Date\: 2024\-10\-08

[Porting Guide](https\://docs\.ansible\.com/ansible/devel/porting\_guides\.html)

<a id="ansible-core-8"></a>
### Ansible\-core

Ansible 10\.5\.0 contains ansible\-core version 2\.17\.5\.
This is a newer version than version 2\.17\.4 contained in the previous Ansible release\.

The changes are reported in the combined changelog below\.

<a id="changed-collections-2"></a>
### Changed Collections

If not mentioned explicitly\, the changes are reported in the combined changelog below\.

| Collection                | Ansible 10.4.0 | Ansible 10.5.0 | Notes                                                                                                                        |
| ------------------------- | -------------- | -------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| chocolatey.chocolatey     | 1.5.1          | 1.5.3          |                                                                                                                              |
| cisco.dnac                | 6.18.0         | 6.20.0         |                                                                                                                              |
| cisco.intersight          | 2.0.17         | 2.0.20         | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
| cisco.meraki              | 2.18.1         | 2.18.2         |                                                                                                                              |
| cisco.ucs                 | 1.11.0         | 1.14.0         | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
| community.crypto          | 2.22.0         | 2.22.1         |                                                                                                                              |
| community.dns             | 3.0.4          | 3.0.5          |                                                                                                                              |
| community.docker          | 3.12.1         | 3.13.0         |                                                                                                                              |
| community.general         | 9.4.0          | 9.5.0          |                                                                                                                              |
| community.hrobot          | 2.0.1          | 2.0.2          |                                                                                                                              |
| community.mongodb         | 1.7.6          | 1.7.7          | There are no changes recorded in the changelog.                                                                              |
| community.postgresql      | 3.5.0          | 3.6.1          |                                                                                                                              |
| community.sops            | 1.9.0          | 1.9.1          |                                                                                                                              |
| community.vmware          | 4.7.0          | 4.7.1          |                                                                                                                              |
| containers.podman         | 1.15.4         | 1.16.1         |                                                                                                                              |
| dellemc.enterprise_sonic  | 2.5.0          | 2.5.1          |                                                                                                                              |
| dellemc.openmanage        | 9.6.0          | 9.7.0          |                                                                                                                              |
| f5networks.f5_modules     | 1.30.1         | 1.31.0         |                                                                                                                              |
| grafana.grafana           | 5.5.0          | 5.5.1          |                                                                                                                              |
| ibm.storage_virtualize    | 2.4.1          | 2.5.0          |                                                                                                                              |
| infoblox.nios_modules     | 1.6.1          | 1.7.0          |                                                                                                                              |
| lowlydba.sqlserver        | 2.3.3          | 2.3.4          |                                                                                                                              |
| netapp_eseries.santricity | 1.4.0          | 1.4.1          |                                                                                                                              |
| netbox.netbox             | 3.19.1         | 3.20.0         |                                                                                                                              |
| ngine_io.cloudstack       | 2.4.0          | 2.5.0          |                                                                                                                              |
| vmware.vmware_rest        | 3.1.0          | 3.2.0          |                                                                                                                              |
| wti.remote                | 1.0.8          | 1.0.10         | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |

<a id="major-changes-2"></a>
### Major Changes

<a id="dellemc-openmanage-6"></a>
#### dellemc\.openmanage

* idrac\_secure\_boot \- This module allows to Configure attributes\, import\, or export secure boot certificate\, and reset keys\.
* idrac\_system\_erase \- This module allows to Erase system and storage components of the server on iDRAC\.

<a id="minor-changes-2"></a>
### Minor Changes

<a id="chocolatey-chocolatey"></a>
#### chocolatey\.chocolatey

* Remove support for End of Life ansible\-core 2\.13\, 2\.14

<a id="cisco-dnac-2"></a>
#### cisco\.dnac

* Added \'fabric\_transits\_workflow\_manager\.py\' to perform operations on SDA fabric transits\.
* Adding  support to update  password  in user\_role\_workflow\_manager module\.
* Changes in inventory\_workflow\_manager module\.
* Changes in ise\_radius\_integration\_workflow\_manager module to check ise certification status\.
* Changes in network\_compliance\_workflow\_manager module\.
* Changes in network\_settings\_workflow\_manager module to support exception handling\.
* Changes in rma\_workflow\_manager module\.
* Changes in sda\_extranet\_policies\_workflow\_manager module\.
* Changes in swim\_workflow\_manager module to support CCO image\.
* Changes in user\_role\_workflow\_manager module\.
* Minor bug fixes in network\_compliance\_workflow\_manager module\.
* Removed sda\_extranet\_policies\_workflow\_manager\.py module\.
* Removing git release workflows\.
* Setting dnac versions and compare for version based routing\.
* Unit test automation for worflow\_manager modules\.

<a id="cisco-meraki-1"></a>
#### cisco\.meraki

* Include networks\_appliance\_traffic\_shaping\_custom\_performance\_classes\_info plugin\.

<a id="community-general-4"></a>
#### community\.general

* dig lookup plugin \- add <code>port</code> option to specify DNS server port \([https\://github\.com/ansible\-collections/community\.general/pull/8966](https\://github\.com/ansible\-collections/community\.general/pull/8966)\)\.
* flatpak \- improve the parsing of Flatpak application IDs based on official guidelines \([https\://github\.com/ansible\-collections/community\.general/pull/8909](https\://github\.com/ansible\-collections/community\.general/pull/8909)\)\.
* gio\_mime \- adjust code ahead of the old <code>VardDict</code> deprecation \([https\://github\.com/ansible\-collections/community\.general/pull/8855](https\://github\.com/ansible\-collections/community\.general/pull/8855)\)\.
* gitlab\_deploy\_key \- better construct when using <code>dict\.items\(\)</code> \([https\://github\.com/ansible\-collections/community\.general/pull/8876](https\://github\.com/ansible\-collections/community\.general/pull/8876)\)\.
* gitlab\_group \- add many new parameters \([https\://github\.com/ansible\-collections/community\.general/pull/8908](https\://github\.com/ansible\-collections/community\.general/pull/8908)\)\.
* gitlab\_group \- better construct when using <code>dict\.items\(\)</code> \([https\://github\.com/ansible\-collections/community\.general/pull/8876](https\://github\.com/ansible\-collections/community\.general/pull/8876)\)\.
* gitlab\_issue \- better construct when using <code>dict\.items\(\)</code> \([https\://github\.com/ansible\-collections/community\.general/pull/8876](https\://github\.com/ansible\-collections/community\.general/pull/8876)\)\.
* gitlab\_merge\_request \- better construct when using <code>dict\.items\(\)</code> \([https\://github\.com/ansible\-collections/community\.general/pull/8876](https\://github\.com/ansible\-collections/community\.general/pull/8876)\)\.
* gitlab\_runner \- better construct when using <code>dict\.items\(\)</code> \([https\://github\.com/ansible\-collections/community\.general/pull/8876](https\://github\.com/ansible\-collections/community\.general/pull/8876)\)\.
* icinga2\_host \- replace loop with dict comprehension \([https\://github\.com/ansible\-collections/community\.general/pull/8876](https\://github\.com/ansible\-collections/community\.general/pull/8876)\)\.
* jira \- adjust code ahead of the old <code>VardDict</code> deprecation \([https\://github\.com/ansible\-collections/community\.general/pull/8856](https\://github\.com/ansible\-collections/community\.general/pull/8856)\)\.
* keycloak\_client \- add <code>client\-x509</code> choice to <code>client\_authenticator\_type</code> \([https\://github\.com/ansible\-collections/community\.general/pull/8973](https\://github\.com/ansible\-collections/community\.general/pull/8973)\)\.
* keycloak\_user\_federation \- add the user federation config parameter <code>referral</code> to the module arguments \([https\://github\.com/ansible\-collections/community\.general/pull/8954](https\://github\.com/ansible\-collections/community\.general/pull/8954)\)\.
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
* one\_image \- add option <code>persistent</code> to manage image persistence \([https\://github\.com/ansible\-collections/community\.general/issues/3578](https\://github\.com/ansible\-collections/community\.general/issues/3578)\, [https\://github\.com/ansible\-collections/community\.general/pull/8889](https\://github\.com/ansible\-collections/community\.general/pull/8889)\)\.
* one\_image \- extend xsd scheme to make it return a lot more info about image \([https\://github\.com/ansible\-collections/community\.general/pull/8889](https\://github\.com/ansible\-collections/community\.general/pull/8889)\)\.
* one\_image \- refactor code to make it more similar to <code>one\_template</code> and <code>one\_vnet</code> \([https\://github\.com/ansible\-collections/community\.general/pull/8889](https\://github\.com/ansible\-collections/community\.general/pull/8889)\)\.
* one\_image\_info \- extend xsd scheme to make it return a lot more info about image \([https\://github\.com/ansible\-collections/community\.general/pull/8889](https\://github\.com/ansible\-collections/community\.general/pull/8889)\)\.
* one\_image\_info \- refactor code to make it more similar to <code>one\_template</code> and <code>one\_vnet</code> \([https\://github\.com/ansible\-collections/community\.general/pull/8889](https\://github\.com/ansible\-collections/community\.general/pull/8889)\)\.
* open\_iscsi \- allow login to a portal with multiple targets without specifying any of them \([https\://github\.com/ansible\-collections/community\.general/pull/8719](https\://github\.com/ansible\-collections/community\.general/pull/8719)\)\.
* opennebula\.py \- add VM <code>id</code> and VM <code>host</code> to inventory host data \([https\://github\.com/ansible\-collections/community\.general/pull/8532](https\://github\.com/ansible\-collections/community\.general/pull/8532)\)\.
* passwordstore lookup plugin \- add subkey creation/update support \([https\://github\.com/ansible\-collections/community\.general/pull/8952](https\://github\.com/ansible\-collections/community\.general/pull/8952)\)\.
* proxmox inventory plugin \- clean up authentication code \([https\://github\.com/ansible\-collections/community\.general/pull/8917](https\://github\.com/ansible\-collections/community\.general/pull/8917)\)\.
* redfish\_command \- add handling of the <code>PasswordChangeRequired</code> message from services in the <code>UpdateUserPassword</code> command to directly modify the user\'s password if the requested user is the one invoking the operation \([https\://github\.com/ansible\-collections/community\.general/issues/8652](https\://github\.com/ansible\-collections/community\.general/issues/8652)\, [https\://github\.com/ansible\-collections/community\.general/pull/8653](https\://github\.com/ansible\-collections/community\.general/pull/8653)\)\.
* redfish\_confg \- remove <code>CapacityBytes</code> from required paramaters of the <code>CreateVolume</code> command \([https\://github\.com/ansible\-collections/community\.general/pull/8956](https\://github\.com/ansible\-collections/community\.general/pull/8956)\)\.
* redfish\_config \- add parameter <code>storage\_none\_volume\_deletion</code> to <code>CreateVolume</code> command in order to control the automatic deletion of non\-RAID volumes \([https\://github\.com/ansible\-collections/community\.general/pull/8990](https\://github\.com/ansible\-collections/community\.general/pull/8990)\)\.
* redfish\_info \- adds <code>RedfishURI</code> and <code>StorageId</code> to Disk inventory \([https\://github\.com/ansible\-collections/community\.general/pull/8937](https\://github\.com/ansible\-collections/community\.general/pull/8937)\)\.
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
* scaleway\_user\_data \- better construct when using <code>dict\.items\(\)</code> \([https\://github\.com/ansible\-collections/community\.general/pull/8876](https\://github\.com/ansible\-collections/community\.general/pull/8876)\)\.
* udm\_dns\_record \- replace loop with <code>dict\.update\(\)</code> \([https\://github\.com/ansible\-collections/community\.general/pull/8876](https\://github\.com/ansible\-collections/community\.general/pull/8876)\)\.

<a id="community-postgresql-4"></a>
#### community\.postgresql

* postgresql\_privs \- adds support for granting and revoking privileges on foreign tables \([https\://github\.com/ansible\-collections/community\.postgresql/issues/724](https\://github\.com/ansible\-collections/community\.postgresql/issues/724)\)\.
* postgresql\_subscription \- adds support for managing subscriptions in the situation where the <code>subconninfo</code> column is unavailable \(such as in CloudSQL\) \([https\://github\.com/ansible\-collections/community\.postgresql/issues/726](https\://github\.com/ansible\-collections/community\.postgresql/issues/726)\)\.

<a id="containers-podman-1"></a>
#### containers\.podman

* Add arch to podman build command explicitly
* Add group\_add parameter for podman quadlet
* Add support for check\_mode in Quadlet
* Trigger a new image build when we detect that the Containerfile has changed\.
* Update inspection info about objects in modules

<a id="f5networks-f5-modules-2"></a>
#### f5networks\.f5\_modules

* bigip\_asm\_dos\_application \- add support for creating dos profile\.
* bigip\_device\_info \- virtual\-servers \- return per\_flow\_request\_access\_policy if defined\.
* bigip\_virtual\_server \- set per\_flow\_request\_access\_policy and stay idempotent\.

<a id="ibm-storage-virtualize"></a>
#### ibm\.storage\_virtualize

* ibm\_sv\_manage\_storage\_partition \- Added support for creating draft partition\, publishing a draft partition\, and merging 2 partitions
* ibm\_sv\_manage\_syslog\_server \- Added support for creating TLS syslog server\, and modifying existing UDP or TCP servers to TLS server
* ibm\_sv\_manage\_truststore\_for\_replication \- Added support for enabling various options \(syslog\, RESTAPI\, vasa\, ipsec\, snmp and email\) during truststore creation
* ibm\_svc\_host \- Added support to add host into draft partition and to create an NVMeFC host
* ibm\_svc\_manage\_portset \- Added support to create a high\-speed replication portset
* ibm\_svc\_manage\_volumegroup \- Added support to add existing volumegroups into draft partition
* ibm\_svcinfo\_command \- Added support for sainfo commands
* ibm\_svctask\_command \- Added support for satask commands

<a id="infoblox-nios-modules-1"></a>
#### infoblox\.nios\_modules

* Added IPv6 network container support for the <em class="title-reference">nios\_next\_network</em> lookup plugin\.
* Added <em class="title-reference">use\_range</em> parameter to the nios\_next\_ip lookup plugin\, enabling lookup for the next available IP from a network range\.
* Added support for the <em class="title-reference">use\_dns\_ea\_inheritance</em> parameter in Host Record to inherit EA from associated zone\.
* Added support for the <em class="title-reference">use\_for\_ea\_inheritance</em> parameter in Host Record to inherit EA from Host address\.
* Enabled IPv4 support for PXE server configuration in the Host Record module\.
* Improved handling of DHCP options in DHCP Range\, Network\, and Network Container\.
* Introduced <em class="title-reference">use\_logic\_filter\_rules</em> \& <em class="title-reference">logic\_filter\_rules</em> support for both IPv4 and IPv6 network and network container\.
* Upgraded the base WAPI version to 2\.12\.3\.

<a id="netbox-netbox"></a>
#### netbox\.netbox

* Add <code>facility</code> to <code>location</code> \([https\://github\.com/netbox\-community/ansible\_modules/issues/1280](https\://github\.com/netbox\-community/ansible\_modules/issues/1280)\)
* Add <code>related\_object\_type</code> to <code>netbox\_custom\_filed</code> \([https\://github\.com/netbox\-community/ansible\_modules/issues/1268](https\://github\.com/netbox\-community/ansible\_modules/issues/1268)\)
* Add <code>status</code> to <code>location</code> \([https\://github\.com/netbox\-community/ansible\_modules/issues/1279](https\://github\.com/netbox\-community/ansible\_modules/issues/1279)\)
* Add <em class="title-reference">description</em> to <em class="title-reference">netbox\_cluster\_group</em> module \([https\://github\.com/netbox\-community/ansible\_modules/issues/1276](https\://github\.com/netbox\-community/ansible\_modules/issues/1276)\)
* Add <em class="title-reference">serial</em> to <em class="title-reference">netbox\_virtual\_machine</em> module \([https\://github\.com/netbox\-community/ansible\_modules/issues/1309](https\://github\.com/netbox\-community/ansible\_modules/issues/1309)\)
* Add <em class="title-reference">status</em> to <em class="title-reference">netbox\_cluster</em> \([https\://github\.com/netbox\-community/ansible\_modules/issues/1275](https\://github\.com/netbox\-community/ansible\_modules/issues/1275)\)
* Add <em class="title-reference">vid\_ranges</em> to <em class="title-reference">netbox\_vlan\_group</em> module \([https\://github\.com/netbox\-community/ansible\_modules/issues/1307](https\://github\.com/netbox\-community/ansible\_modules/issues/1307)\)
* Add ability to rename variables set on the host by <code>netbox\.netbox\.nb\_inventory</code> through configuration\.
* Added option <em class="title-reference">hostname\_field</em> to <code>nb\_inventory</code> to be able to set the inventory hostname from a field in custom\_fields
* Adjust tests for various modules
* Fix the form\_factor option on netbox\_rack
* Update CI for NetBox 4\.1

<a id="ngine-io-cloudstack"></a>
#### ngine\_io\.cloudstack

* cs\_instance \- Added new arguments <code>user\_data\_name</code> and <code>user\_data\_details</code> \([https\://github\.com/ngine\-io/ansible\-collection\-cloudstack/pull/134](https\://github\.com/ngine\-io/ansible\-collection\-cloudstack/pull/134)\)\.
* cs\_service\_offering \- Add support for storagetag \([https\://github\.com/ngine\-io/ansible\-collection\-cloudstack/pull/118](https\://github\.com/ngine\-io/ansible\-collection\-cloudstack/pull/118)\)\.

<a id="vmware-vmware-rest"></a>
#### vmware\.vmware\_rest

* Removed the scenario guides which are pretty much unmaintained and\, therefor\, possibly outdated and misleading \([https\://github\.com/ansible\-collections/vmware\.vmware\_rest/pull/524](https\://github\.com/ansible\-collections/vmware\.vmware\_rest/pull/524)\)\.

<a id="deprecated-features-2"></a>
### Deprecated Features

* The <code>ngine\_io\.exoscale</code> collection has been deprecated\.
  It will be removed from Ansible 11 if no one starts maintaining it again before Ansible 11\.
  See [Collections Removal Process for unmaintained collections](https\://docs\.ansible\.com/ansible/devel/community/collection\_contributors/collection\_package\_removal\.html\#unmaintained\-collections) for more details \([https\://forum\.ansible\.com/t/2572](https\://forum\.ansible\.com/t/2572)\)\.
* The collection <code>t\_systems\_mms\.icinga\_director</code> was renamed to <code>telekom\_mms\.icinga\_director</code>\.
  For now both collections are included in Ansible\.
  The content in <code>t\_systems\_mms\.icinga\_director</code> has been replaced by deprecated redirects in Ansible 9\.0\.0\.
  The collection will be completely removed from Ansible 11\.
  Please update your FQCNs from <code>t\_systems\_mms\.icinga\_director</code> to <code>telekom\_mms\.icinga\_director</code>\.
* The sensu\.sensu\_go collection will be removed from Ansible 12 due to violations of the Ansible inclusion requirements\.
  The collection has [unresolved sanity test failures](https\://github\.com/sensu/sensu\-go\-ansible/issues/362)\.
  See [Collections Removal Process for collections not satisfying the collection requirements](https\://docs\.ansible\.com/ansible/devel/community/collection\_contributors/collection\_package\_removal\.html\#collections\-not\-satisfying\-the\-collection\-requirements) for more details\, including for how this can be cancelled \([https\://forum\.ansible\.com/t/8380](https\://forum\.ansible\.com/t/8380)\)\.
  After removal\, users can still install this collection with <code>ansible\-galaxy collection install sensu\.sensu\_go</code>\.

<a id="community-general-5"></a>
#### community\.general

* hipchat \- the hipchat service has been discontinued and the self\-hosted variant has been End of Life since 2020\. The module is therefore deprecated and will be removed from community\.general 11\.0\.0 if nobody provides compelling reasons to still keep it \([https\://github\.com/ansible\-collections/community\.general/pull/8919](https\://github\.com/ansible\-collections/community\.general/pull/8919)\)\.

<a id="bugfixes-2"></a>
### Bugfixes

<a id="ansible-core-9"></a>
#### Ansible\-core

* Add descriptions for <code>ansible\-galaxy install \-\-help\` and \`\`ansible\-galaxy role\|collection install \-\-help</code>\.
* Errors now preserve stacked error messages even when YAML is involved\.
* <code>ansible\-galaxy install \-\-help</code> \- Fix the usage text and document that the requirements file passed to <code>\-r</code> can include collections and roles\.
* copy \- mtime/atime not updated\. Fix now update mtime/atime\([https\://github\.com/ansible/ansible/issues/83013](https\://github\.com/ansible/ansible/issues/83013)\)
* delay keyword is now a float\, matching the underlying \'time\' API and user expectations\.
* dnf5 \- re\-introduce the <code>state\: installed</code> alias to <code>state\: present</code> \([https\://github\.com/ansible/ansible/issues/83960](https\://github\.com/ansible/ansible/issues/83960)\)
* module\_utils atomic\_move \(used by most file based modules\)\, now correctly handles permission copy and setting mtime correctly across all paths

<a id="chocolatey-chocolatey-1"></a>
#### chocolatey\.chocolatey

* win\_chocolatey \- task crashes if PATH contains multiple choco\.exe on the target machine

<a id="community-crypto-1"></a>
#### community\.crypto

* acme\_\* modules \- when querying renewal information\, make sure to insert a slash between the base URL and the certificate identifier \([https\://github\.com/ansible\-collections/community\.crypto/issues/801](https\://github\.com/ansible\-collections/community\.crypto/issues/801)\, [https\://github\.com/ansible\-collections/community\.crypto/pull/802](https\://github\.com/ansible\-collections/community\.crypto/pull/802)\)\.
* various modules \- pass absolute paths to <code>module\.atomic\_move\(\)</code> \([https\://github\.com/ansible/ansible/issues/83950](https\://github\.com/ansible/ansible/issues/83950)\, [https\://github\.com/ansible\-collections/community\.crypto/pull/799](https\://github\.com/ansible\-collections/community\.crypto/pull/799)\)\.

<a id="community-dns-3"></a>
#### community\.dns

* Update Public Suffix List\.

<a id="community-docker-2"></a>
#### community\.docker

* docker\_prune \- fix handling of lists for the filter options \([https\://github\.com/ansible\-collections/community\.docker/issues/961](https\://github\.com/ansible\-collections/community\.docker/issues/961)\, [https\://github\.com/ansible\-collections/community\.docker/pull/966](https\://github\.com/ansible\-collections/community\.docker/pull/966)\)\.

<a id="community-general-6"></a>
#### community\.general

* cloudflare\_dns \- fix changing Cloudflare SRV records \([https\://github\.com/ansible\-collections/community\.general/issues/8679](https\://github\.com/ansible\-collections/community\.general/issues/8679)\, [https\://github\.com/ansible\-collections/community\.general/pull/8948](https\://github\.com/ansible\-collections/community\.general/pull/8948)\)\.
* cmd\_runner module utils \- call to <code>get\_best\_parsable\_locales\(\)</code> was missing parameter \([https\://github\.com/ansible\-collections/community\.general/pull/8929](https\://github\.com/ansible\-collections/community\.general/pull/8929)\)\.
* dig lookup plugin \- fix using only the last nameserver specified \([https\://github\.com/ansible\-collections/community\.general/pull/8970](https\://github\.com/ansible\-collections/community\.general/pull/8970)\)\.
* django\_command \- option <code>command</code> is now split lexically before passed to underlying PythonRunner \([https\://github\.com/ansible\-collections/community\.general/pull/8944](https\://github\.com/ansible\-collections/community\.general/pull/8944)\)\.
* homectl \- the module now tries to use <code>legacycrypt</code> on Python 3\.13\+ \([https\://github\.com/ansible\-collections/community\.general/issues/4691](https\://github\.com/ansible\-collections/community\.general/issues/4691)\, [https\://github\.com/ansible\-collections/community\.general/pull/8987](https\://github\.com/ansible\-collections/community\.general/pull/8987)\)\.
* ini\_file \- pass absolute paths to <code>module\.atomic\_move\(\)</code> \([https\://github\.com/ansible/ansible/issues/83950](https\://github\.com/ansible/ansible/issues/83950)\, [https\://github\.com/ansible\-collections/community\.general/pull/8925](https\://github\.com/ansible\-collections/community\.general/pull/8925)\)\.
* ipa\_host \- add <code>force\_create</code>\, fix <code>enabled</code> and <code>disabled</code> states \([https\://github\.com/ansible\-collections/community\.general/issues/1094](https\://github\.com/ansible\-collections/community\.general/issues/1094)\, [https\://github\.com/ansible\-collections/community\.general/pull/8920](https\://github\.com/ansible\-collections/community\.general/pull/8920)\)\.
* ipa\_hostgroup \- fix <code>enabled \`\` and \`\`disabled</code> states \([https\://github\.com/ansible\-collections/community\.general/issues/8408](https\://github\.com/ansible\-collections/community\.general/issues/8408)\, [https\://github\.com/ansible\-collections/community\.general/pull/8900](https\://github\.com/ansible\-collections/community\.general/pull/8900)\)\.
* java\_keystore \- pass absolute paths to <code>module\.atomic\_move\(\)</code> \([https\://github\.com/ansible/ansible/issues/83950](https\://github\.com/ansible/ansible/issues/83950)\, [https\://github\.com/ansible\-collections/community\.general/pull/8925](https\://github\.com/ansible\-collections/community\.general/pull/8925)\)\.
* jenkins\_plugin \- pass absolute paths to <code>module\.atomic\_move\(\)</code> \([https\://github\.com/ansible/ansible/issues/83950](https\://github\.com/ansible/ansible/issues/83950)\, [https\://github\.com/ansible\-collections/community\.general/pull/8925](https\://github\.com/ansible\-collections/community\.general/pull/8925)\)\.
* kdeconfig \- pass absolute paths to <code>module\.atomic\_move\(\)</code> \([https\://github\.com/ansible/ansible/issues/83950](https\://github\.com/ansible/ansible/issues/83950)\, [https\://github\.com/ansible\-collections/community\.general/pull/8925](https\://github\.com/ansible\-collections/community\.general/pull/8925)\)\.
* keycloak\_realm \- fix change detection in check mode by sorting the lists in the realms beforehand \([https\://github\.com/ansible\-collections/community\.general/pull/8877](https\://github\.com/ansible\-collections/community\.general/pull/8877)\)\.
* keycloak\_user\_federation \- add module argument allowing users to configure the update mode for the parameter <code>bindCredential</code> \([https\://github\.com/ansible\-collections/community\.general/pull/8898](https\://github\.com/ansible\-collections/community\.general/pull/8898)\)\.
* keycloak\_user\_federation \- minimize change detection by setting <code>krbPrincipalAttribute</code> to <code>\'\'</code> in Keycloak responses if missing \([https\://github\.com/ansible\-collections/community\.general/pull/8785](https\://github\.com/ansible\-collections/community\.general/pull/8785)\)\.
* keycloak\_user\_federation \- remove <code>lastSync</code> parameter from Keycloak responses to minimize diff/changes \([https\://github\.com/ansible\-collections/community\.general/pull/8812](https\://github\.com/ansible\-collections/community\.general/pull/8812)\)\.
* keycloak\_userprofile \- fix empty response when fetching userprofile component by removing <code>parent\=parent\_id</code> filter \([https\://github\.com/ansible\-collections/community\.general/pull/8923](https\://github\.com/ansible\-collections/community\.general/pull/8923)\)\.
* keycloak\_userprofile \- improve diff by deserializing the fetched <code>kc\.user\.profile\.config</code> and serialize it only when sending back \([https\://github\.com/ansible\-collections/community\.general/pull/8940](https\://github\.com/ansible\-collections/community\.general/pull/8940)\)\.
* lxd\_container \- fix bug introduced in previous commit \([https\://github\.com/ansible\-collections/community\.general/pull/8895](https\://github\.com/ansible\-collections/community\.general/pull/8895)\, [https\://github\.com/ansible\-collections/community\.general/issues/8888](https\://github\.com/ansible\-collections/community\.general/issues/8888)\)\.
* one\_service \- fix service creation after it was deleted with <code>unique</code> parameter \([https\://github\.com/ansible\-collections/community\.general/issues/3137](https\://github\.com/ansible\-collections/community\.general/issues/3137)\, [https\://github\.com/ansible\-collections/community\.general/pull/8887](https\://github\.com/ansible\-collections/community\.general/pull/8887)\)\.
* pam\_limits \- pass absolute paths to <code>module\.atomic\_move\(\)</code> \([https\://github\.com/ansible/ansible/issues/83950](https\://github\.com/ansible/ansible/issues/83950)\, [https\://github\.com/ansible\-collections/community\.general/pull/8925](https\://github\.com/ansible\-collections/community\.general/pull/8925)\)\.
* python\_runner module utils \- parameter <code>path\_prefix</code> was being handled as string when it should be a list \([https\://github\.com/ansible\-collections/community\.general/pull/8944](https\://github\.com/ansible\-collections/community\.general/pull/8944)\)\.
* udm\_user \- the module now tries to use <code>legacycrypt</code> on Python 3\.13\+ \([https\://github\.com/ansible\-collections/community\.general/issues/4690](https\://github\.com/ansible\-collections/community\.general/issues/4690)\, [https\://github\.com/ansible\-collections/community\.general/pull/8987](https\://github\.com/ansible\-collections/community\.general/pull/8987)\)\.

<a id="community-postgresql-5"></a>
#### community\.postgresql

* postgresql\_db \- fix issues due to columns in pg\_database changing in Postgres 17\. \([https\://github\.com/ansible\-collections/community\.postgresql/issues/729](https\://github\.com/ansible\-collections/community\.postgresql/issues/729)\)\.
* postgresql\_info \- Use a server check that works on beta and rc versions as well as on actual releases\.
* postgresql\_user \- remove a comment from unit tests that breaks pre\-compile \([https\://github\.com/ansible\-collections/community\.postgresql/issues/737](https\://github\.com/ansible\-collections/community\.postgresql/issues/737)\)\.

<a id="community-sops"></a>
#### community\.sops

* sops\_encrypt \- pass absolute paths to <code>module\.atomic\_move\(\)</code> \([https\://github\.com/ansible/ansible/issues/83950](https\://github\.com/ansible/ansible/issues/83950)\, [https\://github\.com/ansible\-collections/community\.sops/pull/208](https\://github\.com/ansible\-collections/community\.sops/pull/208)\)\.

<a id="community-vmware-4"></a>
#### community\.vmware

* vcenter\_standard\_key\_provider \- Fix documentation \([https\://github\.com/ansible\-collections/community\.vmware/pull/2192](https\://github\.com/ansible\-collections/community\.vmware/pull/2192)\)\.
* vmware\_all\_snapshots\_info \- fixed the datacenter parameter was ignored\([https\://github\.com/ansible\-collections/community\.vmware/pull/2165](https\://github\.com/ansible\-collections/community\.vmware/pull/2165)\)\.
* vmware\_dvswitch \- Fix Pylint issue \([https\://github\.com/ansible\-collections/community\.vmware/pull/2186](https\://github\.com/ansible\-collections/community\.vmware/pull/2186)\)\.
* vmware\_dvswitch\_nioc \- Fix documentation \([https\://github\.com/ansible\-collections/community\.vmware/pull/2192](https\://github\.com/ansible\-collections/community\.vmware/pull/2192)\)\.
* vmware\_dvswitch\_pvlans \- Fix Pylint issue \([https\://github\.com/ansible\-collections/community\.vmware/pull/2186](https\://github\.com/ansible\-collections/community\.vmware/pull/2186)\)\.
* vmware\_guest \- Fix documentation \([https\://github\.com/ansible\-collections/community\.vmware/pull/2192](https\://github\.com/ansible\-collections/community\.vmware/pull/2192)\)\.
* vmware\_guest\_controller \- Fix documentation \([https\://github\.com/ansible\-collections/community\.vmware/pull/2192](https\://github\.com/ansible\-collections/community\.vmware/pull/2192)\)\.
* vmware\_guest\_disk \- Fix documentation \([https\://github\.com/ansible\-collections/community\.vmware/pull/2192](https\://github\.com/ansible\-collections/community\.vmware/pull/2192)\)\.
* vmware\_guest\_serial\_port \- Fix documentation \([https\://github\.com/ansible\-collections/community\.vmware/pull/2192](https\://github\.com/ansible\-collections/community\.vmware/pull/2192)\)\.
* vmware\_guest\_tpm \- Fix Pylint issue \([https\://github\.com/ansible\-collections/community\.vmware/pull/2186](https\://github\.com/ansible\-collections/community\.vmware/pull/2186)\)\.
* vmware\_host \- Fix Pylint issue \([https\://github\.com/ansible\-collections/community\.vmware/pull/2186](https\://github\.com/ansible\-collections/community\.vmware/pull/2186)\)\.
* vmware\_host\_dns \- Fix Pylint issue \([https\://github\.com/ansible\-collections/community\.vmware/pull/2186](https\://github\.com/ansible\-collections/community\.vmware/pull/2186)\)\.
* vmware\_host\_inventory \- Fix Pylint issue \([https\://github\.com/ansible\-collections/community\.vmware/pull/2186](https\://github\.com/ansible\-collections/community\.vmware/pull/2186)\)\.
* vmware\_host\_powerstate \- Fix Pylint issue \([https\://github\.com/ansible\-collections/community\.vmware/pull/2186](https\://github\.com/ansible\-collections/community\.vmware/pull/2186)\)\.
* vmware\_tools \- Fix documentation \([https\://github\.com/ansible\-collections/community\.vmware/pull/2192](https\://github\.com/ansible\-collections/community\.vmware/pull/2192)\)\.
* vmware\_vm\_inventory \- Fix Pylint issue \([https\://github\.com/ansible\-collections/community\.vmware/pull/2186](https\://github\.com/ansible\-collections/community\.vmware/pull/2186)\)\.
* vmware\_vmotion \- Fix Pylint issue \([https\://github\.com/ansible\-collections/community\.vmware/pull/2186](https\://github\.com/ansible\-collections/community\.vmware/pull/2186)\)\.

<a id="containers-podman-2"></a>
#### containers\.podman

* CI \- Add images removal for tests
* CI \- Fix podman CI test container images
* CI \- add ignore list for Ansible sanity for 2\.19
* CI \- bump artifacts versions for GHactions
* CI \- change k8s\.gcr\.io to registry\.k8s\.io in tests
* CI \- fix Podman search of invalid image
* Disable idempotency for pod\_id\_file
* Fix command idempotency with quotes
* Fix health\-startup\-cmd
* Fix logic in Podman images
* Fix podman image permissions issue and runlable test
* Fix quadlet parameters when container uses rootfs
* don\'t document quadlet\_dir as required when setting state\=quadlet
* fix for tls\_verify being ignored
* fix\(podman\_image\) \- skip empty volume items
* fix\(podman\_save\) \- always changed when force
* modify error and docs

<a id="dellemc-enterprise-sonic"></a>
#### dellemc\.enterprise\_sonic

* ConnectionError \- Add the needed import of the Ansible ConnectionError exception class for all files where it was previously missing\. \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/445](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/445)\)\.
* Update regex search expression for \'not found\' error message in httpapi/sonic\.py \'edit\_config\' method \([https\://github\.com/ansible\-collection/dellemc\.enterprise\_sonic/pull/443](https\://github\.com/ansible\-collection/dellemc\.enterprise\_sonic/pull/443)\)\.
* sonic\_system \- Catch the ConnectionError exception caused by unconditional fetching of auditd and ip loadshare hash algorithm configuration\, and return empty configuration instead of allowing the uncaught exception to abort all \"system\" operations on SONiC images older than version 4\.4\.0 \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/441](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/441)\)\.

<a id="dellemc-openmanage-7"></a>
#### dellemc\.openmanage

* Resolved the issue in <code>idrac\_gather\_facts</code> role where it was failing for some component in iDRAC8\. \([https\://github\.com/dell/dellemc\-openmanage\-ansible\-modules/issues/718](https\://github\.com/dell/dellemc\-openmanage\-ansible\-modules/issues/718)\)

<a id="ibm-storage-virtualize-1"></a>
#### ibm\.storage\_virtualize

* ibm\_svc\_manage\_callhome \- Added support to change a subset of proxy settings

<a id="infoblox-nios-modules-2"></a>
#### infoblox\.nios\_modules

* Adjusted unit test assertions for Mock\.called\_once\_with\.
* Fixed an issue in the <em class="title-reference">nios\_host\_record</em> module where the <em class="title-reference">mac</em> parameter was not handled correctly\.
* Fixed the update operation in the <em class="title-reference">nios\_network</em> module where the <em class="title-reference">network</em> parameter was not handled correctly\.
* Omits DNS view from filter critera when renaming a host object and DNS is bypassed\. \([https\://github\.com/infobloxopen/infoblox\-ansible/issues/230](https\://github\.com/infobloxopen/infoblox\-ansible/issues/230)\)
* nios\_host\_record \- rename logic included DNS view in filter critera\, even when DNS had been bypassed\.

<a id="lowlydba-sqlserver"></a>
#### lowlydba\.sqlserver

* Include warning logs in failure output for the restore module to indicate root causes \([https\://github\.com/lowlydba/lowlydba\.sqlserver/pull/266](https\://github\.com/lowlydba/lowlydba\.sqlserver/pull/266)\)\.

<a id="netapp-eseries-santricity"></a>
#### netapp\_eseries\.santricity

* Fixed pep8\, pylint\, and validate\-modules issues found by ansible\-test\.
* Updated outdated command in unit tests\.

<a id="netbox-netbox-1"></a>
#### netbox\.netbox

* If <em class="title-reference">fetch\_all</em> is <em class="title-reference">false</em>\, prefix lookup depends on site lookup\, so move it to secondary lookup \([https\://github\.com/netbox\-community/ansible\_modules/issues/733](https\://github\.com/netbox\-community/ansible\_modules/issues/733)\)

<a id="ngine-io-cloudstack-1"></a>
#### ngine\_io\.cloudstack

* Fixed a bug related to the new option <code>validate\_certs</code> \([https\://github\.com/ngine\-io/ansible\-collection\-cloudstack/pull/135](https\://github\.com/ngine\-io/ansible\-collection\-cloudstack/pull/135)\)\.

<a id="known-issues-2"></a>
### Known Issues

<a id="dellemc-openmanage-8"></a>
#### dellemc\.openmanage

* idrac\_diagnostics \- Issue\(285322\) \- This module doesn\'t support export of diagnostics file to HTTP and HTTPS share via SOCKS proxy\.
* idrac\_firmware \- Issue\(279282\) \- This module does not support firmware update using HTTP\, HTTPS\, and FTP shares with authentication on iDRAC8\.
* idrac\_storage\_volume \- Issue\(290766\) \- The module will report success instead of showing failure for new virtual creation on the BOSS\-N1 controller if a virtual disk is already present on the same controller\.
* idrac\_support\_assist \- Issue\(308550\) \- This module fails when the NFS share path contains sub directory\.
* ome\_diagnostics \- Issue\(279193\) \- Export of SupportAssist collection logs to the share location fails on OME version 4\.0\.0\.
* ome\_smart\_fabric\_uplink \- Issue\(186024\) \- The module supported by OpenManage Enterprise Modular\, however it does not allow the creation of multiple uplinks of the same name\. If an uplink is created using the same name as an existing uplink\, then the existing uplink is modified\.

<a id="new-modules-2"></a>
### New Modules

<a id="community-docker-3"></a>
#### community\.docker

* community\.docker\.docker\_compose\_v2\_exec \- Run command in a container of a Compose service\.
* community\.docker\.docker\_compose\_v2\_run \- Run command in a new container of a Compose service\.

<a id="community-general-7"></a>
#### community\.general

* community\.general\.ipa\_getkeytab \- Manage keytab file in FreeIPA\.

<a id="containers-podman-3"></a>
#### containers\.podman

* containers\.podman\.podman\_container\_copy \- Copy file to or from a container

<a id="infoblox-nios-modules-3"></a>
#### infoblox\.nios\_modules

* infoblox\.nios\_modules\.nios\_extensible\_attribute \- Configure Infoblox NIOS extensible attribute definition
* infoblox\.nios\_modules\.nios\_nsgroup\_delegation \- Configure InfoBlox DNS Nameserver Delegation Groups
* infoblox\.nios\_modules\.nios\_nsgroup\_forwardingmember \- Configure InfoBlox DNS Nameserver Forward/Stub Server Groups
* infoblox\.nios\_modules\.nios\_nsgroup\_forwardstubserver \- Configure InfoBlox DNS Nameserver Forwarding Member Groups
* infoblox\.nios\_modules\.nios\_nsgroup\_stubmember \- Configure InfoBlox DNS Nameserver Stub Member Groups

<a id="netbox-netbox-2"></a>
#### netbox\.netbox

* netbox\.netbox\.netbox\_permission \- Creates or removes permissions from NetBox
* netbox\.netbox\.netbox\_token \- Creates or removes tokens from NetBox
* netbox\.netbox\.netbox\_tunnel \- Create\, update or delete tunnels within NetBox
* netbox\.netbox\.netbox\_tunnel\_group \- Create\, update or delete tunnel groups within NetBox
* netbox\.netbox\.netbox\_user \- Creates or removes users from NetBox
* netbox\.netbox\.netbox\_user\_group \- Creates or removes user groups from NetBox

<a id="unchanged-collections-2"></a>
### Unchanged Collections

* amazon\.aws \(still version 8\.2\.1\)
* ansible\.netcommon \(still version 6\.1\.3\)
* ansible\.posix \(still version 1\.5\.4\)
* ansible\.utils \(still version 4\.1\.0\)
* ansible\.windows \(still version 2\.5\.0\)
* arista\.eos \(still version 9\.0\.0\)
* awx\.awx \(still version 24\.6\.1\)
* azure\.azcollection \(still version 2\.7\.0\)
* check\_point\.mgmt \(still version 5\.2\.3\)
* cisco\.aci \(still version 2\.10\.1\)
* cisco\.asa \(still version 5\.0\.1\)
* cisco\.ios \(still version 8\.0\.0\)
* cisco\.iosxr \(still version 9\.0\.0\)
* cisco\.ise \(still version 2\.9\.3\)
* cisco\.mso \(still version 2\.9\.0\)
* cisco\.nxos \(still version 8\.1\.0\)
* cloud\.common \(still version 3\.0\.0\)
* cloudscale\_ch\.cloud \(still version 2\.4\.0\)
* community\.aws \(still version 8\.0\.0\)
* community\.ciscosmb \(still version 1\.0\.9\)
* community\.digitalocean \(still version 1\.27\.0\)
* community\.grafana \(still version 1\.9\.1\)
* community\.hashi\_vault \(still version 6\.2\.0\)
* community\.library\_inventory\_filtering\_v1 \(still version 1\.0\.1\)
* community\.libvirt \(still version 1\.3\.0\)
* community\.mysql \(still version 3\.10\.3\)
* community\.network \(still version 5\.0\.3\)
* community\.okd \(still version 3\.0\.1\)
* community\.proxysql \(still version 1\.6\.0\)
* community\.rabbitmq \(still version 1\.3\.0\)
* community\.routeros \(still version 2\.19\.0\)
* community\.sap\_libs \(still version 1\.4\.2\)
* community\.windows \(still version 2\.3\.0\)
* community\.zabbix \(still version 2\.5\.1\)
* cyberark\.conjur \(still version 1\.3\.0\)
* cyberark\.pas \(still version 1\.0\.27\)
* dellemc\.powerflex \(still version 2\.5\.0\)
* dellemc\.unity \(still version 2\.0\.0\)
* fortinet\.fortimanager \(still version 2\.7\.0\)
* fortinet\.fortios \(still version 2\.3\.7\)
* frr\.frr \(still version 2\.0\.2\)
* google\.cloud \(still version 1\.4\.1\)
* hetzner\.hcloud \(still version 3\.1\.1\)
* ibm\.qradar \(still version 3\.0\.0\)
* ibm\.spectrum\_virtualize \(still version 2\.0\.0\)
* ieisystem\.inmanage \(still version 2\.0\.0\)
* infinidat\.infinibox \(still version 1\.4\.5\)
* inspur\.ispim \(still version 2\.2\.3\)
* inspur\.sm \(still version 2\.3\.0\)
* junipernetworks\.junos \(still version 8\.0\.0\)
* kaytus\.ksmanage \(still version 1\.2\.2\)
* kubernetes\.core \(still version 3\.2\.0\)
* kubevirt\.core \(still version 1\.5\.0\)
* microsoft\.ad \(still version 1\.7\.1\)
* netapp\.cloudmanager \(still version 21\.22\.1\)
* netapp\.ontap \(still version 22\.12\.0\)
* netapp\.storagegrid \(still version 21\.12\.0\)
* ngine\_io\.exoscale \(still version 1\.1\.0\)
* openstack\.cloud \(still version 2\.2\.0\)
* openvswitch\.openvswitch \(still version 2\.1\.1\)
* ovirt\.ovirt \(still version 3\.2\.0\)
* purestorage\.flasharray \(still version 1\.31\.1\)
* purestorage\.flashblade \(still version 1\.18\.0\)
* sensu\.sensu\_go \(still version 1\.14\.0\)
* splunk\.es \(still version 3\.0\.0\)
* t\_systems\_mms\.icinga\_director \(still version 2\.0\.1\)
* telekom\_mms\.icinga\_director \(still version 2\.1\.2\)
* theforeman\.foreman \(still version 4\.2\.0\)
* vmware\.vmware \(still version 1\.5\.0\)
* vultr\.cloud \(still version 1\.13\.0\)
* vyos\.vyos \(still version 4\.1\.0\)

<a id="v10-4-0"></a>
## v10\.4\.0

- <a href="#release-summary-3">Release Summary</a>
- <a href="#ansible-core-10">Ansible\-core</a>
- <a href="#changed-collections-3">Changed Collections</a>
- <a href="#major-changes-3">Major Changes</a>
    - <a href="#dellemc-openmanage-9">dellemc\.openmanage</a>
    - <a href="#grafana-grafana-1">grafana\.grafana</a>
- <a href="#minor-changes-3">Minor Changes</a>
    - <a href="#amazon-aws">amazon\.aws</a>
    - <a href="#ansible-windows">ansible\.windows</a>
    - <a href="#cisco-dnac-3">cisco\.dnac</a>
    - <a href="#community-crypto-2">community\.crypto</a>
    - <a href="#community-general-8">community\.general</a>
    - <a href="#community-mysql-2">community\.mysql</a>
    - <a href="#community-postgresql-6">community\.postgresql</a>
    - <a href="#community-routeros-1">community\.routeros</a>
    - <a href="#community-sops-1">community\.sops</a>
    - <a href="#community-vmware-5">community\.vmware</a>
    - <a href="#community-windows">community\.windows</a>
    - <a href="#dellemc-enterprise-sonic-1">dellemc\.enterprise\_sonic</a>
    - <a href="#dellemc-openmanage-10">dellemc\.openmanage</a>
    - <a href="#fortinet-fortimanager-3">fortinet\.fortimanager</a>
    - <a href="#google-cloud">google\.cloud</a>
    - <a href="#microsoft-ad">microsoft\.ad</a>
    - <a href="#ngine-io-cloudstack-2">ngine\_io\.cloudstack</a>
    - <a href="#purestorage-flasharray-2">purestorage\.flasharray</a>
    - <a href="#theforeman-foreman">theforeman\.foreman</a>
    - <a href="#vmware-vmware-4">vmware\.vmware</a>
    - <a href="#vmware-vmware-rest-1">vmware\.vmware\_rest</a>
- <a href="#deprecated-features-3">Deprecated Features</a>
    - <a href="#amazon-aws-1">amazon\.aws</a>
    - <a href="#community-general-9">community\.general</a>
    - <a href="#community-mysql-3">community\.mysql</a>
    - <a href="#community-vmware-6">community\.vmware</a>
- <a href="#bugfixes-3">Bugfixes</a>
    - <a href="#ansible-core-11">Ansible\-core</a>
    - <a href="#amazon-aws-2">amazon\.aws</a>
    - <a href="#ansible-windows-1">ansible\.windows</a>
    - <a href="#community-dns-4">community\.dns</a>
    - <a href="#community-general-10">community\.general</a>
    - <a href="#community-mysql-4">community\.mysql</a>
    - <a href="#community-postgresql-7">community\.postgresql</a>
    - <a href="#community-vmware-7">community\.vmware</a>
    - <a href="#community-windows-1">community\.windows</a>
    - <a href="#dellemc-enterprise-sonic-2">dellemc\.enterprise\_sonic</a>
    - <a href="#fortinet-fortimanager-4">fortinet\.fortimanager</a>
    - <a href="#google-cloud-1">google\.cloud</a>
    - <a href="#microsoft-ad-1">microsoft\.ad</a>
    - <a href="#purestorage-flasharray-3">purestorage\.flasharray</a>
    - <a href="#theforeman-foreman-1">theforeman\.foreman</a>
    - <a href="#vmware-vmware-5">vmware\.vmware</a>
- <a href="#known-issues-3">Known Issues</a>
    - <a href="#dellemc-openmanage-11">dellemc\.openmanage</a>
- <a href="#new-modules-3">New Modules</a>
    - <a href="#community-general-11">community\.general</a>
    - <a href="#dellemc-enterprise-sonic-3">dellemc\.enterprise\_sonic</a>
    - <a href="#fortinet-fortimanager-5">fortinet\.fortimanager</a>
    - <a href="#microsoft-ad-2">microsoft\.ad</a>
    - <a href="#purestorage-flasharray-4">purestorage\.flasharray</a>
- <a href="#unchanged-collections-3">Unchanged Collections</a>

<a id="release-summary-3"></a>
### Release Summary

Release Date\: 2024\-09\-10

[Porting Guide](https\://docs\.ansible\.com/ansible/devel/porting\_guides\.html)

<a id="ansible-core-10"></a>
### Ansible\-core

Ansible 10\.4\.0 contains ansible\-core version 2\.17\.4\.
This is a newer version than version 2\.17\.3 contained in the previous Ansible release\.

The changes are reported in the combined changelog below\.

<a id="changed-collections-3"></a>
### Changed Collections

If not mentioned explicitly\, the changes are reported in the combined changelog below\.

| Collection               | Ansible 10.3.0 | Ansible 10.4.0 | Notes                                                                                                                        |
| ------------------------ | -------------- | -------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| amazon.aws               | 8.1.0          | 8.2.1          |                                                                                                                              |
| ansible.windows          | 2.4.0          | 2.5.0          |                                                                                                                              |
| azure.azcollection       | 2.6.0          | 2.7.0          | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
| cisco.dnac               | 6.17.1         | 6.18.0         |                                                                                                                              |
| cisco.intersight         | 2.0.10         | 2.0.17         | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
| cisco.ucs                | 1.10.0         | 1.11.0         | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
| community.crypto         | 2.21.1         | 2.22.0         |                                                                                                                              |
| community.digitalocean   | 1.26.0         | 1.27.0         | There are no changes recorded in the changelog.                                                                              |
| community.dns            | 3.0.3          | 3.0.4          |                                                                                                                              |
| community.general        | 9.3.0          | 9.4.0          |                                                                                                                              |
| community.mysql          | 3.9.0          | 3.10.3         |                                                                                                                              |
| community.postgresql     | 3.4.1          | 3.5.0          |                                                                                                                              |
| community.routeros       | 2.18.0         | 2.19.0         |                                                                                                                              |
| community.sops           | 1.8.2          | 1.9.0          |                                                                                                                              |
| community.vmware         | 4.5.0          | 4.7.0          |                                                                                                                              |
| community.windows        | 2.2.0          | 2.3.0          |                                                                                                                              |
| dellemc.enterprise_sonic | 2.4.0          | 2.5.0          |                                                                                                                              |
| dellemc.openmanage       | 9.5.0          | 9.6.0          |                                                                                                                              |
| fortinet.fortimanager    | 2.6.0          | 2.7.0          |                                                                                                                              |
| google.cloud             | 1.3.0          | 1.4.1          |                                                                                                                              |
| grafana.grafana          | 5.4.0          | 5.5.0          |                                                                                                                              |
| microsoft.ad             | 1.6.0          | 1.7.1          |                                                                                                                              |
| ngine_io.cloudstack      | 2.3.0          | 2.4.0          |                                                                                                                              |
| purestorage.flasharray   | 1.30.2         | 1.31.1         |                                                                                                                              |
| theforeman.foreman       | 4.1.0          | 4.2.0          |                                                                                                                              |
| vmware.vmware            | 1.4.0          | 1.5.0          |                                                                                                                              |
| vmware.vmware_rest       | 3.0.1          | 3.1.0          |                                                                                                                              |
| wti.remote               | 1.0.5          | 1.0.8          | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |

<a id="major-changes-3"></a>
### Major Changes

<a id="dellemc-openmanage-9"></a>
#### dellemc\.openmanage

* idrac\_secure\_boot \- This module allows to import the secure boot certificate\.
* idrac\_support\_assist \- This module allows to run and export SupportAssist collection logs on iDRAC\.

<a id="grafana-grafana-1"></a>
#### grafana\.grafana

* fix\:mimir molecule should use ansible core 2\.16 by \@GVengelen in https\://github\.com/grafana/grafana\-ansible\-collection/pull/254

<a id="minor-changes-3"></a>
### Minor Changes

<a id="amazon-aws"></a>
#### amazon\.aws

* cloudwatch\_metric\_alarm \- add  support for <code>evaluate\_low\_sample\_count\_percentile\`</code> parameter\.
* cloudwatch\_metric\_alarm \- support DatapointsToAlarm config \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2196](https\://github\.com/ansible\-collections/amazon\.aws/pull/2196)\)\.
* ec2\_ami \- Add support for uefi\-preferred boot mode \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2253](https\://github\.com/ansible\-collections/amazon\.aws/pull/2253)\)\.
* ec2\_instance \- Add support for <code>network\_interfaces</code> and <code>network\_interfaces\_ids</code> options replacing deprecated option <code>network</code> \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2123](https\://github\.com/ansible\-collections/amazon\.aws/pull/2123)\)\.
* ec2\_instance \- <code>network\.source\_dest\_check</code> option has been deprecated and replaced by new option <code>source\_dest\_check</code> \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2123](https\://github\.com/ansible\-collections/amazon\.aws/pull/2123)\)\.
* ec2\_instance \- add the possibility to create instance with multiple network interfaces \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2123](https\://github\.com/ansible\-collections/amazon\.aws/pull/2123)\)\.
* ec2\_metadata\_facts \- Add parameter <code>metadata\_token\_ttl\_seconds</code> \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2209](https\://github\.com/ansible\-collections/amazon\.aws/pull/2209)\)\.
* rds\_cluster \- Add support for I/O\-Optimized storage configuration for aurora clusters \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2063](https\://github\.com/ansible\-collections/amazon\.aws/pull/2063)\)\.
* rds\_instance \- snake case for parameter <code>performance\_insights\_kms\_key\_id</code> was incorrect according to boto documentation \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2163](https\://github\.com/ansible\-collections/amazon\.aws/pull/2163)\)\.
* s3\_bucket \- Add support for bucket inventories \([https\://docs\.aws\.amazon\.com/AmazonS3/latest/userguide/storage\-inventory\.html](https\://docs\.aws\.amazon\.com/AmazonS3/latest/userguide/storage\-inventory\.html)\)
* s3\_object \- Add support for <code>expected\_bucket\_owner</code> option \([https\://github\.com/ansible\-collections/amazon\.aws/issues/2114](https\://github\.com/ansible\-collections/amazon\.aws/issues/2114)\)\.
* ssm parameter lookup \- add new option <code>droppath</code> to drop the hierarchical search path from ssm parameter lookup results \([https\://github\.com/ansible\-collections/amazon\.aws/pull/1756](https\://github\.com/ansible\-collections/amazon\.aws/pull/1756)\)\.

<a id="ansible-windows"></a>
#### ansible\.windows

* Set minimum supported Ansible version to 2\.15 to align with the versions still supported by Ansible\.
* owner \- Migrated to <code>Ansible\.Basic</code> format to add basic checks like invocation args checking
* win\_powershell \- Changed <em class="title-reference">sensitive\_parameters</em> to use <em class="title-reference">New\-Object</em>\, rather than <em class="title-reference">\:\:new\(\)</em>

<a id="cisco-dnac-3"></a>
#### cisco\.dnac

* Added \'fabric\_sites\_zones\_workflow\_manager\.py\' to manage fabric sites/zones and update the authentication profile template\.
* Added \'sda\_extranet\_policies\_workflow\_manager\' to provide SDA Extranet Policies for managing SDA Extranet Policy\.
* Added Circle CI support for integration testing\.
* Bug fixes in user\_role\_workflow\_manager module\.
* Changes in accesspoint\_workflow\_manager module\.
* Changes in device\_configs\_backup\_workflow\_manager to support name of the site to which the device is assigned\.
* Changes in inventory\_workflow\_manager to support maximum devices to resync\, and resync timeout\.
* Changes in network\_settings\_workflow\_manager to support reserve ip subpools\.
* Changes in provision\_workflow\_manager to support enhanced log messages\.
* Changes in rma\_workflow\_manager module to support pre check for device replacement\.
* device\_configs\_backup\_workflow\_manager\.py\. added attribute \'site\'\.

<a id="community-crypto-2"></a>
#### community\.crypto

* openssl\_privatekey\, openssl\_privatekey\_pipe \- add default value <code>auto</code> for <code>cipher</code> option\, which happens to be the only supported value for this option anyway\. Therefore it is no longer necessary to specify <code>cipher\=auto</code> when providing <code>passphrase</code> \([https\://github\.com/ansible\-collections/community\.crypto/issues/793](https\://github\.com/ansible\-collections/community\.crypto/issues/793)\, [https\://github\.com/ansible\-collections/community\.crypto/pull/794](https\://github\.com/ansible\-collections/community\.crypto/pull/794)\)\.

<a id="community-general-8"></a>
#### community\.general

* MH module utils \- add parameter <code>when</code> to <code>cause\_changes</code> decorator \([https\://github\.com/ansible\-collections/community\.general/pull/8766](https\://github\.com/ansible\-collections/community\.general/pull/8766)\)\.
* MH module utils \- minor refactor in decorators \([https\://github\.com/ansible\-collections/community\.general/pull/8766](https\://github\.com/ansible\-collections/community\.general/pull/8766)\)\.
* alternatives \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8833](https\://github\.com/ansible\-collections/community\.general/pull/8833)\)\.
* apache2\_mod\_proxy \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8814](https\://github\.com/ansible\-collections/community\.general/pull/8814)\)\.
* apache2\_mod\_proxy \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8833](https\://github\.com/ansible\-collections/community\.general/pull/8833)\)\.
* consul\_acl \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8833](https\://github\.com/ansible\-collections/community\.general/pull/8833)\)\.
* copr \- Added <code>includepkgs</code> and <code>excludepkgs</code> parameters to limit the list of packages fetched or excluded from the repository\([https\://github\.com/ansible\-collections/community\.general/pull/8779](https\://github\.com/ansible\-collections/community\.general/pull/8779)\)\.
* credstash lookup plugin \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8822](https\://github\.com/ansible\-collections/community\.general/pull/8822)\)\.
* csv module utils \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8814](https\://github\.com/ansible\-collections/community\.general/pull/8814)\)\.
* deco MH module utils \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8822](https\://github\.com/ansible\-collections/community\.general/pull/8822)\)\.
* etcd3 \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8822](https\://github\.com/ansible\-collections/community\.general/pull/8822)\)\.
* gio\_mime \- mute the  old <code>VarDict</code> deprecation \([https\://github\.com/ansible\-collections/community\.general/pull/8776](https\://github\.com/ansible\-collections/community\.general/pull/8776)\)\.
* gitlab\_group \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8814](https\://github\.com/ansible\-collections/community\.general/pull/8814)\)\.
* gitlab\_project \- add option <code>issues\_access\_level</code> to enable/disable project issues \([https\://github\.com/ansible\-collections/community\.general/pull/8760](https\://github\.com/ansible\-collections/community\.general/pull/8760)\)\.
* gitlab\_project \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8822](https\://github\.com/ansible\-collections/community\.general/pull/8822)\)\.
* gitlab\_project \- sorted parameters in order to avoid future merge conflicts \([https\://github\.com/ansible\-collections/community\.general/pull/8759](https\://github\.com/ansible\-collections/community\.general/pull/8759)\)\.
* hashids filter plugin \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8814](https\://github\.com/ansible\-collections/community\.general/pull/8814)\)\.
* hwc\_ecs\_instance \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8822](https\://github\.com/ansible\-collections/community\.general/pull/8822)\)\.
* hwc\_evs\_disk \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8822](https\://github\.com/ansible\-collections/community\.general/pull/8822)\)\.
* hwc\_vpc\_eip \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8822](https\://github\.com/ansible\-collections/community\.general/pull/8822)\)\.
* hwc\_vpc\_peering\_connect \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8822](https\://github\.com/ansible\-collections/community\.general/pull/8822)\)\.
* hwc\_vpc\_port \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8822](https\://github\.com/ansible\-collections/community\.general/pull/8822)\)\.
* hwc\_vpc\_subnet \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8822](https\://github\.com/ansible\-collections/community\.general/pull/8822)\)\.
* imc\_rest \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8833](https\://github\.com/ansible\-collections/community\.general/pull/8833)\)\.
* ipa\_otptoken \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8822](https\://github\.com/ansible\-collections/community\.general/pull/8822)\)\.
* jira \- mute the  old <code>VarDict</code> deprecation \([https\://github\.com/ansible\-collections/community\.general/pull/8776](https\://github\.com/ansible\-collections/community\.general/pull/8776)\)\.
* jira \- replace deprecated params when using decorator <code>cause\_changes</code> \([https\://github\.com/ansible\-collections/community\.general/pull/8791](https\://github\.com/ansible\-collections/community\.general/pull/8791)\)\.
* keep\_keys filter plugin \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8814](https\://github\.com/ansible\-collections/community\.general/pull/8814)\)\.
* keycloak module utils \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8822](https\://github\.com/ansible\-collections/community\.general/pull/8822)\)\.
* keycloak\_client \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8814](https\://github\.com/ansible\-collections/community\.general/pull/8814)\)\.
* keycloak\_clientscope \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8814](https\://github\.com/ansible\-collections/community\.general/pull/8814)\)\.
* keycloak\_identity\_provider \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8814](https\://github\.com/ansible\-collections/community\.general/pull/8814)\)\.
* keycloak\_user\_federation \- add module argument allowing users to optout of the removal of unspecified mappers\, for example to keep the keycloak default mappers \([https\://github\.com/ansible\-collections/community\.general/pull/8764](https\://github\.com/ansible\-collections/community\.general/pull/8764)\)\.
* keycloak\_user\_federation \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8814](https\://github\.com/ansible\-collections/community\.general/pull/8814)\)\.
* keycloak\_user\_federation \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8822](https\://github\.com/ansible\-collections/community\.general/pull/8822)\)\.
* keycloak\_user\_federation \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8833](https\://github\.com/ansible\-collections/community\.general/pull/8833)\)\.
* linode \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8814](https\://github\.com/ansible\-collections/community\.general/pull/8814)\)\.
* lxc\_container \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8822](https\://github\.com/ansible\-collections/community\.general/pull/8822)\)\.
* lxd\_container \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8814](https\://github\.com/ansible\-collections/community\.general/pull/8814)\)\.
* manageiq\_provider \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8814](https\://github\.com/ansible\-collections/community\.general/pull/8814)\)\.
* ocapi\_utils \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8833](https\://github\.com/ansible\-collections/community\.general/pull/8833)\)\.
* one\_service \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8814](https\://github\.com/ansible\-collections/community\.general/pull/8814)\)\.
* one\_vm \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8814](https\://github\.com/ansible\-collections/community\.general/pull/8814)\)\.
* onepassword lookup plugin \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8833](https\://github\.com/ansible\-collections/community\.general/pull/8833)\)\.
* pids \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8833](https\://github\.com/ansible\-collections/community\.general/pull/8833)\)\.
* pipx \- added new states <code>install\_all</code>\, <code>uninject</code>\, <code>upgrade\_shared</code>\, <code>pin</code>\, and <code>unpin</code> \([https\://github\.com/ansible\-collections/community\.general/pull/8809](https\://github\.com/ansible\-collections/community\.general/pull/8809)\)\.
* pipx \- added parameter <code>global</code> to module \([https\://github\.com/ansible\-collections/community\.general/pull/8793](https\://github\.com/ansible\-collections/community\.general/pull/8793)\)\.
* pipx \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8833](https\://github\.com/ansible\-collections/community\.general/pull/8833)\)\.
* pipx\_info \- added parameter <code>global</code> to module \([https\://github\.com/ansible\-collections/community\.general/pull/8793](https\://github\.com/ansible\-collections/community\.general/pull/8793)\)\.
* pipx\_info \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8833](https\://github\.com/ansible\-collections/community\.general/pull/8833)\)\.
* pkg5\_publisher \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8833](https\://github\.com/ansible\-collections/community\.general/pull/8833)\)\.
* proxmox \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8814](https\://github\.com/ansible\-collections/community\.general/pull/8814)\)\.
* proxmox\_disk \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8814](https\://github\.com/ansible\-collections/community\.general/pull/8814)\)\.
* proxmox\_kvm \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8814](https\://github\.com/ansible\-collections/community\.general/pull/8814)\)\.
* proxmox\_kvm \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8822](https\://github\.com/ansible\-collections/community\.general/pull/8822)\)\.
* redfish\_utils \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8833](https\://github\.com/ansible\-collections/community\.general/pull/8833)\)\.
* redfish\_utils module utils \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8822](https\://github\.com/ansible\-collections/community\.general/pull/8822)\)\.
* redis cache plugin \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8833](https\://github\.com/ansible\-collections/community\.general/pull/8833)\)\.
* remove\_keys filter plugin \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8814](https\://github\.com/ansible\-collections/community\.general/pull/8814)\)\.
* replace\_keys filter plugin \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8814](https\://github\.com/ansible\-collections/community\.general/pull/8814)\)\.
* scaleway \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8833](https\://github\.com/ansible\-collections/community\.general/pull/8833)\)\.
* scaleway module utils \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8822](https\://github\.com/ansible\-collections/community\.general/pull/8822)\)\.
* scaleway\_compute \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8833](https\://github\.com/ansible\-collections/community\.general/pull/8833)\)\.
* scaleway\_ip \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8833](https\://github\.com/ansible\-collections/community\.general/pull/8833)\)\.
* scaleway\_lb \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8833](https\://github\.com/ansible\-collections/community\.general/pull/8833)\)\.
* scaleway\_security\_group \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8822](https\://github\.com/ansible\-collections/community\.general/pull/8822)\)\.
* scaleway\_security\_group \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8833](https\://github\.com/ansible\-collections/community\.general/pull/8833)\)\.
* scaleway\_user\_data \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8833](https\://github\.com/ansible\-collections/community\.general/pull/8833)\)\.
* sensu\_silence \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8833](https\://github\.com/ansible\-collections/community\.general/pull/8833)\)\.
* snmp\_facts \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8833](https\://github\.com/ansible\-collections/community\.general/pull/8833)\)\.
* sorcery \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8833](https\://github\.com/ansible\-collections/community\.general/pull/8833)\)\.
* ufw \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8822](https\://github\.com/ansible\-collections/community\.general/pull/8822)\)\.
* unsafe plugin utils \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8814](https\://github\.com/ansible\-collections/community\.general/pull/8814)\)\.
* vardict module utils \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8814](https\://github\.com/ansible\-collections/community\.general/pull/8814)\)\.
* vars MH module utils \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8814](https\://github\.com/ansible\-collections/community\.general/pull/8814)\)\.
* vmadm \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8822](https\://github\.com/ansible\-collections/community\.general/pull/8822)\)\.

<a id="community-mysql-2"></a>
#### community\.mysql

* mysql\_info \- Add <code>tls\_requires</code> returned value for the <code>users\_info</code> filter \([https\://github\.com/ansible\-collections/community\.mysql/pull/628](https\://github\.com/ansible\-collections/community\.mysql/pull/628)\)\.
* mysql\_info \- return a database server engine used \([https\://github\.com/ansible\-collections/community\.mysql/issues/644](https\://github\.com/ansible\-collections/community\.mysql/issues/644)\)\.
* mysql\_replication \- Adds support for <em class="title-reference">CHANGE REPLICATION SOURCE TO</em> statement \([https\://github\.com/ansible\-collections/community\.mysql/issues/635](https\://github\.com/ansible\-collections/community\.mysql/issues/635)\)\.
* mysql\_replication \- Adds support for <em class="title-reference">SHOW BINARY LOG STATUS</em> and <em class="title-reference">SHOW BINLOG STATUS</em> on getprimary mode\.
* mysql\_replication \- Improve detection of IsReplica and IsPrimary by inspecting the dictionary returned from the SQL query instead of relying on variable types\. This ensures compatibility with changes in the connector or the output of SHOW REPLICA STATUS and SHOW MASTER STATUS\, allowing for easier maintenance if these change in the future\.
* mysql\_user \- Add salt parameter to generate static hash for <em class="title-reference">caching\_sha2\_password</em> and <em class="title-reference">sha256\_password</em> plugins\.

<a id="community-postgresql-6"></a>
#### community\.postgresql

* postgres \- add support for postgres <code>infinity</code> timestamps by replacing them with <code>datetime\.min</code> / <code>datetime\.max</code> values \([https\://github\.com/ansible\-collections/community\.postgresql/pull/714](https\://github\.com/ansible\-collections/community\.postgresql/pull/714)\)\.
* postgresql\_publication \- add the <code>tables\_in\_schema</code> argument to implement <code>FOR TABLES IN SCHEMA</code> feature \([https\://github\.com/ansible\-collections/community\.postgresql/issues/709](https\://github\.com/ansible\-collections/community\.postgresql/issues/709)\)\.
* postgresql\_user \- adds the <code>configuration</code> argument that allows to manage user\-specific default configuration \([https\://github\.com/ansible\-collections/community\.postgresql/issues/598](https\://github\.com/ansible\-collections/community\.postgresql/issues/598)\)\.

<a id="community-routeros-1"></a>
#### community\.routeros

* api\_info\, api\_modify \- add support for the <code>ip dns adlist</code> path implemented by RouterOS 7\.15 and newer \([https\://github\.com/ansible\-collections/community\.routeros/pull/310](https\://github\.com/ansible\-collections/community\.routeros/pull/310)\)\.
* api\_info\, api\_modify \- add support for the <code>mld\-version</code> and <code>multicast\-querier</code> properties in <code>interface bridge</code> \([https\://github\.com/ansible\-collections/community\.routeros/pull/315](https\://github\.com/ansible\-collections/community\.routeros/pull/315)\)\.
* api\_info\, api\_modify \- add support for the <code>routing filter num\-list</code> path implemented by RouterOS 7 and newer \([https\://github\.com/ansible\-collections/community\.routeros/pull/313](https\://github\.com/ansible\-collections/community\.routeros/pull/313)\)\.
* api\_info\, api\_modify \- add support for the <code>routing igmp\-proxy</code> path \([https\://github\.com/ansible\-collections/community\.routeros/pull/309](https\://github\.com/ansible\-collections/community\.routeros/pull/309)\)\.
* api\_modify\, api\_info \- add read\-only <code>default</code> field to <code>snmp community</code> \([https\://github\.com/ansible\-collections/community\.routeros/pull/311](https\://github\.com/ansible\-collections/community\.routeros/pull/311)\)\.

<a id="community-sops-1"></a>
#### community\.sops

* decrypt filter plugin \- now supports the input and output type <code>ini</code> \([https\://github\.com/ansible\-collections/community\.sops/pull/204](https\://github\.com/ansible\-collections/community\.sops/pull/204)\)\.
* sops lookup plugin \- new option <code>extract</code> allows extracting a single key out of a JSON or YAML file\, equivalent to sops\' <code>decrypt \-\-extract</code> \([https\://github\.com/ansible\-collections/community\.sops/pull/200](https\://github\.com/ansible\-collections/community\.sops/pull/200)\)\.
* sops lookup plugin \- now supports the input and output type <code>ini</code> \([https\://github\.com/ansible\-collections/community\.sops/pull/204](https\://github\.com/ansible\-collections/community\.sops/pull/204)\)\.

<a id="community-vmware-5"></a>
#### community\.vmware

* vmware\_vm\_vm\_drs\_rule \- added datacenter argument to correctly deal with multiple clusters with same name\([https\://github\.com/ansible\-collections/community\.vmware/issues/2101](https\://github\.com/ansible\-collections/community\.vmware/issues/2101)\)\.
* vsphere\_file \- Fix examples in documentation \([https\://github\.com/ansible\-collections/community\.vmware/issues/2110](https\://github\.com/ansible\-collections/community\.vmware/issues/2110)\)\.

<a id="community-windows"></a>
#### community\.windows

* Set minimum supported Ansible version to 2\.15 to align with the versions still supported by Asnible\.

<a id="dellemc-enterprise-sonic-1"></a>
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

<a id="dellemc-openmanage-10"></a>
#### dellemc\.openmanage

* ome\_application\_certificate \- This module is enhanced to support the upload of certificate chain\.

<a id="fortinet-fortimanager-3"></a>
#### fortinet\.fortimanager

* Supported FortiManager 7\.6\.0\. Added 7 new modules\.
* Supported check mode for all modules except \"fmgr\_generic\"\. You can use \"ansible\-playbook \-i \<your\-host\-file\> \<your\-playbook\> \-\-check\" to validate whether your playbook will make any changes to the FortiManager\.

<a id="google-cloud"></a>
#### google\.cloud

* ansible \- 2\.16\.0 is now the minimum version supported
* ansible \- 3\.10 is now the minimum Python version
* ansible\-test \- integration tests are now run against 2\.16\.0 and 2\.17\.0
* gcloud role \- use dnf instead of yum on RHEL
* gcp\_secret\_manager \- add as a module and lookup plugin \([https\://github\.com/ansible\-collections/google\.cloud/pull/578](https\://github\.com/ansible\-collections/google\.cloud/pull/578)\)
* gcp\_secret\_manager \- support more than 10 versions \([https\://github\.com/ansible\-collections/google\.cloud/pull/634](https\://github\.com/ansible\-collections/google\.cloud/pull/634)\)
* restore google\_cloud\_ops\_agents submodule \([https\://github\.com/ansible\-collections/google\.cloud/pull/594](https\://github\.com/ansible\-collections/google\.cloud/pull/594)\)

<a id="microsoft-ad"></a>
#### microsoft\.ad

* Set minimum supported Ansible version to 2\.15 to align with the versions still supported by Ansible\.
* microsoft\.ad\.computer \- Added the <code>do\_not\_append\_dollar\_to\_sam</code> option which can create a computer account without the <code>\$</code> suffix when an explicit <code>sam\_account\_name</code> was provided without one\.
* microsoft\.ad\.domain \- Added <code>reboot\_timeout</code> option to control how long a reboot can go for\.
* microsoft\.ad\.domain\_child \- Added <code>reboot\_timeout</code> option to control how long a reboot can go for\.
* microsoft\.ad\.domain\_controller \- Added <code>reboot\_timeout</code> option to control how long a reboot can go for\.
* microsoft\.ad\.membership \- Added <code>domain\_server</code> option to specify the DC to use for domain join operations \- [https\://github\.com/ansible\-collections/microsoft\.ad/issues/131\#issuecomment\-2201151651](https\://github\.com/ansible\-collections/microsoft\.ad/issues/131\#issuecomment\-2201151651)
* microsoft\.ad\.membership \- Added <code>reboot\_timeout</code> option to control how long a reboot can go for\.

<a id="ngine-io-cloudstack-2"></a>
#### ngine\_io\.cloudstack

* Added possiblity to disable certs validation using <code>validate\_certs</code> argument \([https\://github\.com/ngine\-io/ansible\-collection\-cloudstack/pull/131](https\://github\.com/ngine\-io/ansible\-collection\-cloudstack/pull/131)\)\.
* cs\_project \- Extended to pass <code>cleanup\=true</code> to the deleteProject API when deleting a project \([https\://github\.com/ngine\-io/ansible\-collection\-cloudstack/pull/122](https\://github\.com/ngine\-io/ansible\-collection\-cloudstack/pull/122)\)\.

<a id="purestorage-flasharray-2"></a>
#### purestorage\.flasharray

* purefa\_token \- Add <code>disable\_warnings</code> support

<a id="theforeman-foreman"></a>
#### theforeman\.foreman

* content\_export\_\* \- document that <code>chunk\_size\_gb</code> parameter is only applicable for <code>importable</code> exports \([https\://github\.com/theforeman/foreman\-ansible\-modules/issues/1738](https\://github\.com/theforeman/foreman\-ansible\-modules/issues/1738)\)
* lifecycle\_environments role \- allow setting <code>state</code> for the LCE\, allowing deletion of existing ones
* location\, locations role \- add <code>description</code> parameter to set the description

<a id="vmware-vmware-4"></a>
#### vmware\.vmware

* Add action group \([https\://github\.com/ansible\-collections/vmware\.vmware/pull/59](https\://github\.com/ansible\-collections/vmware\.vmware/pull/59)\)\.
* cluster \- Added cluster module\, which is meant to succeed the community\.vmware\.vmware\_cluster module \([https\://github\.com/ansible\-collections/vmware\.vmware/pull/60](https\://github\.com/ansible\-collections/vmware\.vmware/pull/60)\)\.
* cluster\_vcls \- Added module to manage vCLS settings\, based on community\.vmware\.vmware\_cluster\_vcls \([https\://github\.com/ansible\-collections/vmware\.vmware/pull/61](https\://github\.com/ansible\-collections/vmware\.vmware/pull/61)\)\.
* folder\_template\_from\_vm \- Use a more robust method when waiting for tasks to complete to improve accuracy \([https\://github\.com/ansible\-collections/vmware\.vmware/pull/64](https\://github\.com/ansible\-collections/vmware\.vmware/pull/64)\)\.

<a id="vmware-vmware-rest-1"></a>
#### vmware\.vmware\_rest

* cluster\_moid \- updated documentation around lookup plugin usage
* datacenter\_moid \- updated documentation around lookup plugin usage
* datastore\_moid \- updated documentation around lookup plugin usage
* folder\_moid \- updated documentation around lookup plugin usage
* host\_moid \- updated documentation around lookup plugin usage
* network\_moid \- updated documentation around lookup plugin usage
* resource\_pool\_moid \- updated documentation around lookup plugin usage
* vm\_moid \- updated documentation around lookup plugin usage

<a id="deprecated-features-3"></a>
### Deprecated Features

<a id="amazon-aws-1"></a>
#### amazon\.aws

* iam\_role \- support for creating and deleting IAM instance profiles using the <code>create\_instance\_profile</code> and <code>delete\_instance\_profile</code> options has been deprecated and will be removed in a release after 2026\-05\-01\.  To manage IAM instance profiles the <code>amazon\.aws\.iam\_instance\_profile</code> module can be used instead \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2221](https\://github\.com/ansible\-collections/amazon\.aws/pull/2221)\)\.

<a id="community-general-9"></a>
#### community\.general

* MH decorator cause\_changes module utils \- deprecate parameters <code>on\_success</code> and <code>on\_failure</code> \([https\://github\.com/ansible\-collections/community\.general/pull/8791](https\://github\.com/ansible\-collections/community\.general/pull/8791)\)\.
* pipx \- support for versions of the command line tool <code>pipx</code> older than <code>1\.7\.0</code> is deprecated and will be removed in community\.general 11\.0\.0 \([https\://github\.com/ansible\-collections/community\.general/pull/8793](https\://github\.com/ansible\-collections/community\.general/pull/8793)\)\.
* pipx\_info \- support for versions of the command line tool <code>pipx</code> older than <code>1\.7\.0</code> is deprecated and will be removed in community\.general 11\.0\.0 \([https\://github\.com/ansible\-collections/community\.general/pull/8793](https\://github\.com/ansible\-collections/community\.general/pull/8793)\)\.

<a id="community-mysql-3"></a>
#### community\.mysql

* collection \- support of mysqlclient connector is deprecated \- use PyMySQL connector instead\! We will stop testing against it in collection version 4\.0\.0 and remove the related code in 5\.0\.0 \([https\://github\.com/ansible\-collections/community\.mysql/issues/654](https\://github\.com/ansible\-collections/community\.mysql/issues/654)\)\.
* mysql\_info \- The <code>users\_info</code> filter returned variable <code>plugin\_auth\_string</code> contains the hashed password and it\'s misleading\, it will be removed from community\.mysql 4\.0\.0\. Use the <em class="title-reference">plugin\_hash\_string</em> return value instead \([https\://github\.com/ansible\-collections/community\.mysql/pull/629](https\://github\.com/ansible\-collections/community\.mysql/pull/629)\)\.
* mysql\_user \- the <code>user</code> alias of the <code>name</code> argument has been deprecated and will be removed in collection version 5\.0\.0\. Use the <code>name</code> argument instead\.

<a id="community-vmware-6"></a>
#### community\.vmware

* vmware\_cluster \- the module has been deprecated and will be removed in community\.vmware 6\.0\.0 \([https\://github\.com/ansible\-collections/community\.vmware/pull/2143](https\://github\.com/ansible\-collections/community\.vmware/pull/2143)\)\.
* vmware\_cluster\_drs \- the module has been deprecated and will be removed in community\.vmware 6\.0\.0 \([https\://github\.com/ansible\-collections/community\.vmware/pull/2136](https\://github\.com/ansible\-collections/community\.vmware/pull/2136)\)\.
* vmware\_cluster\_vcls \- the module has been deprecated and will be removed in community\.vmware 6\.0\.0 \([https\://github\.com/ansible\-collections/community\.vmware/pull/2156](https\://github\.com/ansible\-collections/community\.vmware/pull/2156)\)\.

<a id="bugfixes-3"></a>
### Bugfixes

<a id="ansible-core-11"></a>
#### Ansible\-core

* Fix <code>SemanticVersion\.parse\(\)</code> to store the version string so that <code>\_\_repr\_\_</code> reports it instead of <code>None</code> \([https\://github\.com/ansible/ansible/pull/83831](https\://github\.com/ansible/ansible/pull/83831)\)\.
* Fix an issue where registered variable was not available for templating in <code>loop\_control\.label</code> on skipped looped tasks \([https\://github\.com/ansible/ansible/issues/83619](https\://github\.com/ansible/ansible/issues/83619)\)
* Fix for <code>meta</code> tasks breaking host/fork affinity with <code>host\_pinned</code> strategy \([https\://github\.com/ansible/ansible/issues/83294](https\://github\.com/ansible/ansible/issues/83294)\)
* Fix using the current task\'s directory for looking up relative paths within roles \([https\://github\.com/ansible/ansible/issues/82695](https\://github\.com/ansible/ansible/issues/82695)\)\.
* atomic\_move \- fix using the setgid bit on the parent directory when creating files \([https\://github\.com/ansible/ansible/issues/46742](https\://github\.com/ansible/ansible/issues/46742)\, [https\://github\.com/ansible/ansible/issues/67177](https\://github\.com/ansible/ansible/issues/67177)\)\.
* connection plugins using the \'extras\' option feature would need variables to match the plugin\'s loaded name\, sometimes requiring fqcn\, which is not the same as the documented/declared/expected variables\. Now we fall back to the \'basename\' of the fqcn\, but plugin authors can still set the expected value directly\.
* csvfile lookup \- give an error when no search term is provided using modern config syntax \([https\://github\.com/ansible/ansible/issues/83689](https\://github\.com/ansible/ansible/issues/83689)\)\.
* include\_tasks \- Display location when attempting to load a task list where <code>include\_\*</code> did not specify any value \- [https\://github\.com/ansible/ansible/issues/83874](https\://github\.com/ansible/ansible/issues/83874)
* powershell \- Improve CLIXML decoding to decode all control characters and unicode characters that are encoded as surrogate pairs\.
* psrp \- Fix bug when attempting to fetch a file path that contains special glob characters like <code>\[\]</code>
* runtime\-metadata sanity test \- do not crash on deprecations if <code>galaxy\.yml</code> contains an empty <code>version</code> field \([https\://github\.com/ansible/ansible/pull/83831](https\://github\.com/ansible/ansible/pull/83831)\)\.
* ssh \- Fix bug when attempting to fetch a file path with characters that should be quoted when using the <code>piped</code> transfer method

<a id="amazon-aws-2"></a>
#### amazon\.aws

* cloudwatch\_metric\_alarm \- Fix idempotency when creating cloudwatch metric alarm without dimensions \([https\://github\.com/ansible\-collections/amazon\.aws/pull/1865](https\://github\.com/ansible\-collections/amazon\.aws/pull/1865)\)\.
* ec2\_instance \- fix state processing when exact\_count is used \([https\://github\.com/ansible\-collections/amazon\.aws/pull/1659](https\://github\.com/ansible\-collections/amazon\.aws/pull/1659)\)\.
* iam\_role \- fixes <code>EntityAlreadyExists</code> exception when <code>create\_instance\_profile</code> was set to <code>false</code> and the instance profile already existed \([https\://github\.com/ansible\-collections/amazon\.aws/issues/2102](https\://github\.com/ansible\-collections/amazon\.aws/issues/2102)\)\.
* iam\_role \- fixes issue where IAM instance profiles were created when <code>create\_instance\_profile</code> was set to <code>false</code> \([https\://github\.com/ansible\-collections/amazon\.aws/issues/2281](https\://github\.com/ansible\-collections/amazon\.aws/issues/2281)\)\.
* rds\_cluster \- Limit params sent to api call to DBClusterIdentifier when using state started or stopped \([https\://github\.com/ansible\-collections/amazon\.aws/issues/2197](https\://github\.com/ansible\-collections/amazon\.aws/issues/2197)\)\.
* route53 \- modify the return value to return diff only when <code>module\.\_diff</code> is set to true \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2136](https\://github\.com/ansible\-collections/amazon\.aws/pull/2136)\)\.
* s3\_bucket \- catch <code>UnsupportedArgument</code> when calling API <code>GetBucketAccelerationConfig</code> on region where it is not supported \([https\://github\.com/ansible\-collections/amazon\.aws/issues/2180](https\://github\.com/ansible\-collections/amazon\.aws/issues/2180)\)\.
* s3\_bucket \- change the default behaviour of the new <code>accelerate\_enabled</code> option to only update the configuration if explicitly passed \([https\://github\.com/ansible\-collections/amazon\.aws/issues/2220](https\://github\.com/ansible\-collections/amazon\.aws/issues/2220)\)\.
* s3\_bucket \- fixes <code>MethodNotAllowed</code> exceptions caused by fetching transfer acceleration state in regions that don\'t support it \([https\://github\.com/ansible\-collections/amazon\.aws/issues/2266](https\://github\.com/ansible\-collections/amazon\.aws/issues/2266)\)\.
* s3\_bucket \- fixes <code>TypeError\: cannot unpack non\-iterable NoneType object</code> errors related to bucket versioning\, policies\, tags or encryption \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2228](https\://github\.com/ansible\-collections/amazon\.aws/pull/2228)\)\.

<a id="ansible-windows-1"></a>
#### ansible\.windows

* setup \- Better handle orphaned users when attempting to retrieve <code>ansible\_machine\_id</code> \- [https\://github\.com/ansible\-collections/ansible\.windows/issues/606](https\://github\.com/ansible\-collections/ansible\.windows/issues/606)
* win\_owner \- Try to enable extra privileges if available to set the owner even when the caller may not have explicit rights to do so normally \- [https\://github\.com/ansible\-collections/ansible\.windows/issues/633](https\://github\.com/ansible\-collections/ansible\.windows/issues/633)
* win\_powershell \- Fix up depth handling on <code>\$Ansible\.Result</code> when using a custom <code>executable</code> \- [https\://github\.com/ansible\-collections/ansible\.windows/issues/642](https\://github\.com/ansible\-collections/ansible\.windows/issues/642)
* win\_powershell \- increase open timeout for <code>executable</code> parameter to prevent exceptions on first\-run or slower targets\. \([https\://github\.com/ansible\-collections/ansible\.windows/issues/644](https\://github\.com/ansible\-collections/ansible\.windows/issues/644)\)\.
* win\_updates \- Base64 encode the update wrapper and payload to prevent locale\-specific encoding issues\.
* win\_updates \- Handle race condition when <code>Wait\-Process</code> did not handle when the process had ended \- [https\://github\.com/ansible\-collections/ansible\.windows/issues/623](https\://github\.com/ansible\-collections/ansible\.windows/issues/623)

<a id="community-dns-4"></a>
#### community\.dns

* Update Public Suffix List\.

<a id="community-general-10"></a>
#### community\.general

* gitlab\_group\_access\_token \- fix crash in check mode caused by attempted access to a newly created access token \([https\://github\.com/ansible\-collections/community\.general/pull/8796](https\://github\.com/ansible\-collections/community\.general/pull/8796)\)\.
* gitlab\_project \- fix <code>container\_expiration\_policy</code> not being applied when creating a new project \([https\://github\.com/ansible\-collections/community\.general/pull/8790](https\://github\.com/ansible\-collections/community\.general/pull/8790)\)\.
* gitlab\_project \- fix crash caused by old Gitlab projects not having a <code>container\_expiration\_policy</code> attribute \([https\://github\.com/ansible\-collections/community\.general/pull/8790](https\://github\.com/ansible\-collections/community\.general/pull/8790)\)\.
* gitlab\_project\_access\_token \- fix crash in check mode caused by attempted access to a newly created access token \([https\://github\.com/ansible\-collections/community\.general/pull/8796](https\://github\.com/ansible\-collections/community\.general/pull/8796)\)\.
* keycloak\_realm\_key \- fix invalid usage of <code>parent\_id</code> \([https\://github\.com/ansible\-collections/community\.general/issues/7850](https\://github\.com/ansible\-collections/community\.general/issues/7850)\, [https\://github\.com/ansible\-collections/community\.general/pull/8823](https\://github\.com/ansible\-collections/community\.general/pull/8823)\)\.
* keycloak\_user\_federation \- fix key error when removing mappers during an update and new mappers are specified in the module args \([https\://github\.com/ansible\-collections/community\.general/pull/8762](https\://github\.com/ansible\-collections/community\.general/pull/8762)\)\.
* keycloak\_user\_federation \- fix the <code>UnboundLocalError</code> that occurs when an ID is provided for a user federation mapper \([https\://github\.com/ansible\-collections/community\.general/pull/8831](https\://github\.com/ansible\-collections/community\.general/pull/8831)\)\.
* keycloak\_user\_federation \- sort desired and after mapper list by name \(analog to before mapper list\) to minimize diff and make change detection more accurate \([https\://github\.com/ansible\-collections/community\.general/pull/8761](https\://github\.com/ansible\-collections/community\.general/pull/8761)\)\.
* proxmox inventory plugin \- fixed a possible error on concatenating responses from proxmox\. In case an API call unexpectedly returned an empty result\, the inventory failed with a fatal error\. Added check for empty response \([https\://github\.com/ansible\-collections/community\.general/issues/8798](https\://github\.com/ansible\-collections/community\.general/issues/8798)\, [https\://github\.com/ansible\-collections/community\.general/pull/8794](https\://github\.com/ansible\-collections/community\.general/pull/8794)\)\.

<a id="community-mysql-4"></a>
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

<a id="community-postgresql-7"></a>
#### community\.postgresql

* postgres \- psycopg2 automatically sets the datestyle on the connection to iso whenever it encounters a datestyle configuration it doesn\'t recognize\, but psycopg3 does not\. Fix now enforces iso datestyle when using psycopg3 \([https\://github\.com/ansible\-collections/community\.postgresql/issues/711](https\://github\.com/ansible\-collections/community\.postgresql/issues/711)\)\.

<a id="community-vmware-7"></a>
#### community\.vmware

* Document dependency on requests \([https\://github\.com/ansible\-collections/community\.vmware/issues/2127](https\://github\.com/ansible\-collections/community\.vmware/issues/2127)\)\.
* vmware\_guest\_disk \- round size to int\, supporting float values properly \([https\://github\.com/ansible\-collections/community\.vmware/issues/123](https\://github\.com/ansible\-collections/community\.vmware/issues/123)\)\.
* vmware\_guest\_snapshot \- Update documentation regarding snapshot\_id parameter \([https\://github\.com/ansible\-collections/community\.vmware/issues/2145](https\://github\.com/ansible\-collections/community\.vmware/issues/2145)\)\.

<a id="community-windows-1"></a>
#### community\.windows

* win\_mapped\_drive \- Use correct P/Invoke signature to fix mapped network drives on 32 Bit OS\.
* win\_mapped\_drive \- better handle failures when attempting to set mapped drive that already exists but was seen as a local path\.

<a id="dellemc-enterprise-sonic-2"></a>
#### dellemc\.enterprise\_sonic

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
* sonic\_vlans \- Fix exception when gathering facts \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/377](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/377)\)\.

<a id="fortinet-fortimanager-4"></a>
#### fortinet\.fortimanager

* Fixed Bug in \"fmgr\_fact\"
* Improved documentation\.

<a id="google-cloud-1"></a>
#### google\.cloud

* ansible\-lint \- remove jinja templates from test assertions
* gcp\_kms\_filters \- add DOCUMENTATION string
* gcp\_secret\_manager \- make an f\-string usage backward compatible

<a id="microsoft-ad-1"></a>
#### microsoft\.ad

* Fix <code>microsoft\.ad\.debug\_ldap\_client</code> documentation problem so it appears in the <code>ansible\-doc</code> plugin list and online documentation\.
* Removed usages of the python call <code>datetime\.datetime\.utcnow\(\)</code> in favour of <code>datetime\.datetime\.now\(datetime\.timezone\.utc\)</code>\. The original method is now deprecated in Python 3\.12 and will be removed in a later version\.
* group \- fix error when creating a group with no members explicitly set \- [https\://github\.com/ansible\-collections/microsoft\.ad/issues/141](https\://github\.com/ansible\-collections/microsoft\.ad/issues/141)
* ldap \- Filter out managed service accounts in the default LDAP filter used\. The <code>filter\_without\_computer</code> can be used to disable the default filter if needed\.
* membership \- allow domain join with hostname change if the account for that host already exists \- [https\://github\.com/ansible\-collections/microsoft\.ad/pull/145](https\://github\.com/ansible\-collections/microsoft\.ad/pull/145)
* microsoft\.ad\.computer \- Added fallback <code>identity</code> lookup for <code>sAMAccountName</code> with the <code>\$</code> suffix\. This ensures that finding the computer object will work with or without the <code>\$</code> suffix\. \- [https\://github\.com/ansible\-collections/microsoft\.ad/issues/124](https\://github\.com/ansible\-collections/microsoft\.ad/issues/124)
* microsoft\.ad\.group \- Fix setting group members of Builtin groups of a domain controller \- [https\://github\.com/ansible\-collections/microsoft\.ad/issues/130](https\://github\.com/ansible\-collections/microsoft\.ad/issues/130)

<a id="purestorage-flasharray-3"></a>
#### purestorage\.flasharray

* purefa\_dsrole \- Fix version check logic
* purefa\_pod \- Fix issue with pod not creating correctly
* purefa\_subnet \- Initialize varaible correctly
* purefa\_syslog\_settings \- Initialize varaible correctly
* purefa\_volume \- Fixes <code>eradicate</code> so it doesn\'t report success when it hasn\'t actually eradicated
* purefa\_volume \- Fixes <code>volfact</code> response when in <code>check\_mode</code>
* purefa\_volume \- Fixes issue where malformed <code>volfact</code> will cause the <code>move</code> to apparently fail\.

<a id="theforeman-foreman-1"></a>
#### theforeman\.foreman

* callback plugin \- correctly catch facts with vault data and replace it with <code>ENCRYPTED\_VAULT\_VALUE\_NOT\_REPORTED</code>\, preventing <code>Object of type AnsibleVaultEncryptedUnicode is not JSON serializable</code> errors
* redhat\_manifest \- do not send empty JSON bodies in GET requests which confuse the portal sometimes \([https\://github\.com/theforeman/foreman\-ansible\-modules/issues/1768](https\://github\.com/theforeman/foreman\-ansible\-modules/issues/1768)\)

<a id="vmware-vmware-5"></a>
#### vmware\.vmware

* README \- Fix typos in README \([https\://github\.com/ansible\-collections/vmware\.vmware/pull/66](https\://github\.com/ansible\-collections/vmware\.vmware/pull/66)\)\.

<a id="known-issues-3"></a>
### Known Issues

<a id="dellemc-openmanage-11"></a>
#### dellemc\.openmanage

* idrac\_diagnostics \- Issue\(285322\) \- This module doesn\'t support export of diagnostics file to HTTP and HTTPS share via SOCKS proxy\.
* idrac\_firmware \- Issue\(279282\) \- This module does not support firmware update using HTTP\, HTTPS\, and FTP shares with authentication on iDRAC8\.
* idrac\_storage\_volume \- Issue\(290766\) \- The module will report success instead of showing failure for new virtual creation on the BOSS\-N1 controller if a virtual disk is already present on the same controller\.
* idrac\_support\_assist \- Issue\(308550\) \- This module fails when the NFS share path contains sub directory\.
* ome\_diagnostics \- Issue\(279193\) \- Export of SupportAssist collection logs to the share location fails on OME version 4\.0\.0\.
* ome\_smart\_fabric\_uplink \- Issue\(186024\) \- The module supported by OpenManage Enterprise Modular\, however it does not allow the creation of multiple uplinks of the same name\. If an uplink is created using the same name as an existing uplink\, then the existing uplink is modified\.

<a id="new-modules-3"></a>
### New Modules

<a id="community-general-11"></a>
#### community\.general

* community\.general\.keycloak\_userprofile \- Allows managing Keycloak User Profiles\.
* community\.general\.one\_vnet \- Manages OpenNebula virtual networks\.

<a id="dellemc-enterprise-sonic-3"></a>
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

<a id="fortinet-fortimanager-5"></a>
#### fortinet\.fortimanager

* fortinet\.fortimanager\.fmgr\_fmg\_sasemanager\_settings \- Fmg sase manager settings
* fortinet\.fortimanager\.fmgr\_fmg\_sasemanager\_status \- Fmg sase manager status
* fortinet\.fortimanager\.fmgr\_pm\_config\_pblock\_firewall\_proxypolicy \- Configure proxy policies\.
* fortinet\.fortimanager\.fmgr\_pm\_config\_pblock\_firewall\_proxypolicy\_sectionvalue \- Configure proxy policies\.
* fortinet\.fortimanager\.fmgr\_system\_admin\_user\_policyblock \- Policy block write access\.
* fortinet\.fortimanager\.fmgr\_system\_fmgcluster \- fmg clsuter\.
* fortinet\.fortimanager\.fmgr\_system\_fmgcluster\_peer \- Peer\.

<a id="microsoft-ad-2"></a>
#### microsoft\.ad

* microsoft\.ad\.service\_account \- Manage Active Directory service account objects

<a id="purestorage-flasharray-4"></a>
#### purestorage\.flasharray

* purestorage\.flasharray\.purefa\_dsrole\_old \- Configure FlashArray Directory Service Roles \(pre\-6\.6\.3\)

<a id="unchanged-collections-3"></a>
### Unchanged Collections

* ansible\.netcommon \(still version 6\.1\.3\)
* ansible\.posix \(still version 1\.5\.4\)
* ansible\.utils \(still version 4\.1\.0\)
* arista\.eos \(still version 9\.0\.0\)
* awx\.awx \(still version 24\.6\.1\)
* check\_point\.mgmt \(still version 5\.2\.3\)
* chocolatey\.chocolatey \(still version 1\.5\.1\)
* cisco\.aci \(still version 2\.10\.1\)
* cisco\.asa \(still version 5\.0\.1\)
* cisco\.ios \(still version 8\.0\.0\)
* cisco\.iosxr \(still version 9\.0\.0\)
* cisco\.ise \(still version 2\.9\.3\)
* cisco\.meraki \(still version 2\.18\.1\)
* cisco\.mso \(still version 2\.9\.0\)
* cisco\.nxos \(still version 8\.1\.0\)
* cloud\.common \(still version 3\.0\.0\)
* cloudscale\_ch\.cloud \(still version 2\.4\.0\)
* community\.aws \(still version 8\.0\.0\)
* community\.ciscosmb \(still version 1\.0\.9\)
* community\.docker \(still version 3\.12\.1\)
* community\.grafana \(still version 1\.9\.1\)
* community\.hashi\_vault \(still version 6\.2\.0\)
* community\.hrobot \(still version 2\.0\.1\)
* community\.library\_inventory\_filtering\_v1 \(still version 1\.0\.1\)
* community\.libvirt \(still version 1\.3\.0\)
* community\.mongodb \(still version 1\.7\.6\)
* community\.network \(still version 5\.0\.3\)
* community\.okd \(still version 3\.0\.1\)
* community\.proxysql \(still version 1\.6\.0\)
* community\.rabbitmq \(still version 1\.3\.0\)
* community\.sap\_libs \(still version 1\.4\.2\)
* community\.zabbix \(still version 2\.5\.1\)
* containers\.podman \(still version 1\.15\.4\)
* cyberark\.conjur \(still version 1\.3\.0\)
* cyberark\.pas \(still version 1\.0\.27\)
* dellemc\.powerflex \(still version 2\.5\.0\)
* dellemc\.unity \(still version 2\.0\.0\)
* f5networks\.f5\_modules \(still version 1\.30\.1\)
* fortinet\.fortios \(still version 2\.3\.7\)
* frr\.frr \(still version 2\.0\.2\)
* hetzner\.hcloud \(still version 3\.1\.1\)
* ibm\.qradar \(still version 3\.0\.0\)
* ibm\.spectrum\_virtualize \(still version 2\.0\.0\)
* ibm\.storage\_virtualize \(still version 2\.4\.1\)
* ieisystem\.inmanage \(still version 2\.0\.0\)
* infinidat\.infinibox \(still version 1\.4\.5\)
* infoblox\.nios\_modules \(still version 1\.6\.1\)
* inspur\.ispim \(still version 2\.2\.3\)
* inspur\.sm \(still version 2\.3\.0\)
* junipernetworks\.junos \(still version 8\.0\.0\)
* kaytus\.ksmanage \(still version 1\.2\.2\)
* kubernetes\.core \(still version 3\.2\.0\)
* kubevirt\.core \(still version 1\.5\.0\)
* lowlydba\.sqlserver \(still version 2\.3\.3\)
* netapp\.cloudmanager \(still version 21\.22\.1\)
* netapp\.ontap \(still version 22\.12\.0\)
* netapp\.storagegrid \(still version 21\.12\.0\)
* netapp\_eseries\.santricity \(still version 1\.4\.0\)
* netbox\.netbox \(still version 3\.19\.1\)
* ngine\_io\.exoscale \(still version 1\.1\.0\)
* openstack\.cloud \(still version 2\.2\.0\)
* openvswitch\.openvswitch \(still version 2\.1\.1\)
* ovirt\.ovirt \(still version 3\.2\.0\)
* purestorage\.flashblade \(still version 1\.18\.0\)
* sensu\.sensu\_go \(still version 1\.14\.0\)
* splunk\.es \(still version 3\.0\.0\)
* t\_systems\_mms\.icinga\_director \(still version 2\.0\.1\)
* telekom\_mms\.icinga\_director \(still version 2\.1\.2\)
* vultr\.cloud \(still version 1\.13\.0\)
* vyos\.vyos \(still version 4\.1\.0\)

<a id="v10-3-0"></a>
## v10\.3\.0

- <a href="#release-summary-4">Release Summary</a>
- <a href="#ansible-core-12">Ansible\-core</a>
- <a href="#changed-collections-4">Changed Collections</a>
- <a href="#minor-changes-4">Minor Changes</a>
    - <a href="#ansible-core-13">Ansible\-core</a>
    - <a href="#cisco-dnac-4">cisco\.dnac</a>
    - <a href="#cisco-mso">cisco\.mso</a>
    - <a href="#cloudscale-ch-cloud">cloudscale\_ch\.cloud</a>
    - <a href="#community-docker-4">community\.docker</a>
    - <a href="#community-general-12">community\.general</a>
    - <a href="#community-routeros-2">community\.routeros</a>
    - <a href="#dellemc-openmanage-12">dellemc\.openmanage</a>
    - <a href="#f5networks-f5-modules-3">f5networks\.f5\_modules</a>
    - <a href="#fortinet-fortimanager-6">fortinet\.fortimanager</a>
    - <a href="#netapp-ontap-3">netapp\.ontap</a>
    - <a href="#purestorage-flashblade-3">purestorage\.flashblade</a>
    - <a href="#theforeman-foreman-2">theforeman\.foreman</a>
    - <a href="#vmware-vmware-6">vmware\.vmware</a>
- <a href="#deprecated-features-4">Deprecated Features</a>
    - <a href="#community-docker-5">community\.docker</a>
    - <a href="#community-routeros-3">community\.routeros</a>
    - <a href="#community-sops-2">community\.sops</a>
- <a href="#bugfixes-4">Bugfixes</a>
    - <a href="#ansible-core-14">Ansible\-core</a>
    - <a href="#cisco-ise-2">cisco\.ise</a>
    - <a href="#cisco-mso-1">cisco\.mso</a>
    - <a href="#community-crypto-3">community\.crypto</a>
    - <a href="#community-dns-5">community\.dns</a>
    - <a href="#community-docker-6">community\.docker</a>
    - <a href="#community-general-13">community\.general</a>
    - <a href="#community-routeros-4">community\.routeros</a>
    - <a href="#community-sops-3">community\.sops</a>
    - <a href="#fortinet-fortimanager-7">fortinet\.fortimanager</a>
    - <a href="#netapp-ontap-4">netapp\.ontap</a>
    - <a href="#purestorage-flasharray-5">purestorage\.flasharray</a>
    - <a href="#purestorage-flashblade-4">purestorage\.flashblade</a>
    - <a href="#vmware-vmware-7">vmware\.vmware</a>
- <a href="#known-issues-4">Known Issues</a>
    - <a href="#community-docker-7">community\.docker</a>
    - <a href="#dellemc-openmanage-13">dellemc\.openmanage</a>
- <a href="#new-modules-4">New Modules</a>
    - <a href="#community-general-14">community\.general</a>
    - <a href="#fortinet-fortimanager-8">fortinet\.fortimanager</a>
    - <a href="#theforeman-foreman-3">theforeman\.foreman</a>
    - <a href="#vmware-vmware-8">vmware\.vmware</a>
- <a href="#unchanged-collections-4">Unchanged Collections</a>

<a id="release-summary-4"></a>
### Release Summary

Release Date\: 2024\-08\-13

[Porting Guide](https\://docs\.ansible\.com/ansible/devel/porting\_guides\.html)

<a id="ansible-core-12"></a>
### Ansible\-core

Ansible 10\.3\.0 contains ansible\-core version 2\.17\.3\.
This is a newer version than version 2\.17\.2 contained in the previous Ansible release\.

The changes are reported in the combined changelog below\.

<a id="changed-collections-4"></a>
### Changed Collections

If not mentioned explicitly\, the changes are reported in the combined changelog below\.

| Collection             | Ansible 10.2.0 | Ansible 10.3.0 | Notes                                                                                                                        |
| ---------------------- | -------------- | -------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| cisco.dnac             | 6.16.0         | 6.17.1         |                                                                                                                              |
| cisco.intersight       | 2.0.9          | 2.0.10         | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
| cisco.ise              | 2.9.2          | 2.9.3          |                                                                                                                              |
| cisco.mso              | 2.8.0          | 2.9.0          |                                                                                                                              |
| cloudscale_ch.cloud    | 2.3.1          | 2.4.0          |                                                                                                                              |
| community.crypto       | 2.21.0         | 2.21.1         |                                                                                                                              |
| community.dns          | 3.0.2          | 3.0.3          |                                                                                                                              |
| community.docker       | 3.11.0         | 3.12.1         |                                                                                                                              |
| community.general      | 9.2.0          | 9.3.0          |                                                                                                                              |
| community.mongodb      | 1.7.5          | 1.7.6          | There are no changes recorded in the changelog.                                                                              |
| community.routeros     | 2.17.0         | 2.18.0         |                                                                                                                              |
| community.sops         | 1.8.0          | 1.8.2          |                                                                                                                              |
| cyberark.pas           | 1.0.25         | 1.0.27         | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
| dellemc.openmanage     | 9.4.0          | 9.5.0          |                                                                                                                              |
| f5networks.f5_modules  | 1.29.0         | 1.30.1         |                                                                                                                              |
| fortinet.fortimanager  | 2.5.0          | 2.6.0          |                                                                                                                              |
| grafana.grafana        | 5.3.0          | 5.4.0          |                                                                                                                              |
| netapp.ontap           | 22.11.0        | 22.12.0        |                                                                                                                              |
| purestorage.flasharray | 1.30.0         | 1.30.2         |                                                                                                                              |
| purestorage.flashblade | 1.17.0         | 1.18.0         |                                                                                                                              |
| theforeman.foreman     | 4.0.0          | 4.1.0          |                                                                                                                              |
| vmware.vmware          | 1.3.0          | 1.4.0          |                                                                                                                              |

<a id="minor-changes-4"></a>
### Minor Changes

<a id="ansible-core-13"></a>
#### Ansible\-core

* ansible\-test \- Improve the error message shown when an unknown <code>\-\-remote</code> or <code>\-\-docker</code> option is given\.
* ansible\-test \- Removed the <code>vyos/1\.1\.8</code> network remote as it is no longer functional\.

<a id="cisco-dnac-4"></a>
#### cisco\.dnac

* Added \'accesspoint\_workflow\_manager\' module to manage access point configurations\.
* Added \'rma\_workflow\_manager\' module to manage RMA workflow\.
* Added \'user\_role\_workflow\_manager\' module to manage operations to create\, update\, and delete users and roles\.
* Added Circle CI support for integration testing\.
* Adding pyzipper support in device\_configs workflow manager module\.
* Adding run\_compliance\_batch\_size support in network\_compliance module\.
* Changes in provision workflow manager module\.
* Checking the device list in swim workflow manager module\.
* Exporting export\_device\_details\_limit in inventory workflow module\.
* Fix family name from userand\_roles to user\_and\_roles\.
* UT and IT cases for worflow manager modules\.

<a id="cisco-mso"></a>
#### cisco\.mso

* Add new module ndo\_schema\_template\_bd\_dhcp\_policy to support BD DHCP Policy configuration in NDO version 4\.1 and later
* Add support to use an APIC DN as VRF reference in mso\_schema\_site\_bd\_l3out

<a id="cloudscale-ch-cloud"></a>
#### cloudscale\_ch\.cloud

* Update source\_format of custom images with actually available choices\.

<a id="community-docker-4"></a>
#### community\.docker

* docker\, docker\_api connection plugins \- allow to determine the working directory when executing commands with the new <code>working\_dir</code> option \([https\://github\.com/ansible\-collections/community\.docker/pull/943](https\://github\.com/ansible\-collections/community\.docker/pull/943)\)\.
* docker\, docker\_api connection plugins \- allow to execute commands with extended privileges with the new <code>privileges</code> option \([https\://github\.com/ansible\-collections/community\.docker/pull/943](https\://github\.com/ansible\-collections/community\.docker/pull/943)\)\.
* docker\, docker\_api connection plugins \- allow to pass extra environment variables when executing commands with the new <code>extra\_env</code> option \([https\://github\.com/ansible\-collections/community\.docker/issues/937](https\://github\.com/ansible\-collections/community\.docker/issues/937)\, [https\://github\.com/ansible\-collections/community\.docker/pull/940](https\://github\.com/ansible\-collections/community\.docker/pull/940)\)\.
* docker\_compose\_v2\* modules \- support Docker Compose 2\.29\.0\'s <code>json</code> progress writer to avoid having to parse text output \([https\://github\.com/ansible\-collections/community\.docker/pull/931](https\://github\.com/ansible\-collections/community\.docker/pull/931)\)\.
* docker\_compose\_v2\_pull \- add new options <code>ignore\_buildable</code>\, <code>include\_deps</code>\, and <code>services</code> \([https\://github\.com/ansible\-collections/community\.docker/issues/941](https\://github\.com/ansible\-collections/community\.docker/issues/941)\, [https\://github\.com/ansible\-collections/community\.docker/pull/942](https\://github\.com/ansible\-collections/community\.docker/pull/942)\)\.
* docker\_container \- when creating a container\, directly pass all networks to connect to to the Docker Daemon for API version 1\.44 and newer\. This makes creation more efficient and works around a bug in Docker Daemon that does not use the specified MAC address in at least some cases\, though only for creation \([https\://github\.com/ansible\-collections/community\.docker/pull/933](https\://github\.com/ansible\-collections/community\.docker/pull/933)\)\.

<a id="community-general-12"></a>
#### community\.general

* cgroup\_memory\_recap\, hipchat\, jabber\, log\_plays\, loganalytics\, logentries\, logstash\, slack\, splunk\, sumologic\, syslog\_json callback plugins \- make sure that all options are typed \([https\://github\.com/ansible\-collections/community\.general/pull/8628](https\://github\.com/ansible\-collections/community\.general/pull/8628)\)\.
* chef\_databag\, consul\_kv\, cyberarkpassword\, dsv\, etcd\, filetree\, hiera\, onepassword\, onepassword\_doc\, onepassword\_raw\, passwordstore\, redis\, shelvefile\, tss lookup plugins \- make sure that all options are typed \([https\://github\.com/ansible\-collections/community\.general/pull/8626](https\://github\.com/ansible\-collections/community\.general/pull/8626)\)\.
* chroot\, funcd\, incus\, iocage\, jail\, lxc\, lxd\, qubes\, zone connection plugins \- make sure that all options are typed \([https\://github\.com/ansible\-collections/community\.general/pull/8627](https\://github\.com/ansible\-collections/community\.general/pull/8627)\)\.
* cobbler\, linode\, lxd\, nmap\, online\, scaleway\, stackpath\_compute\, virtualbox inventory plugins \- make sure that all options are typed \([https\://github\.com/ansible\-collections/community\.general/pull/8625](https\://github\.com/ansible\-collections/community\.general/pull/8625)\)\.
* doas\, dzdo\, ksu\, machinectl\, pbrun\, pfexec\, pmrun\, sesu\, sudosu become plugins \- make sure that all options are typed \([https\://github\.com/ansible\-collections/community\.general/pull/8623](https\://github\.com/ansible\-collections/community\.general/pull/8623)\)\.
* gconftool2 \- make use of <code>ModuleHelper</code> features to simplify code \([https\://github\.com/ansible\-collections/community\.general/pull/8711](https\://github\.com/ansible\-collections/community\.general/pull/8711)\)\.
* gitlab\_project \- add option <code>container\_expiration\_policy</code> to schedule container registry cleanup \([https\://github\.com/ansible\-collections/community\.general/pull/8674](https\://github\.com/ansible\-collections/community\.general/pull/8674)\)\.
* gitlab\_project \- add option <code>model\_registry\_access\_level</code> to disable model registry \([https\://github\.com/ansible\-collections/community\.general/pull/8688](https\://github\.com/ansible\-collections/community\.general/pull/8688)\)\.
* gitlab\_project \- add option <code>pages\_access\_level</code> to disable project pages \([https\://github\.com/ansible\-collections/community\.general/pull/8688](https\://github\.com/ansible\-collections/community\.general/pull/8688)\)\.
* gitlab\_project \- add option <code>repository\_access\_level</code> to disable project repository \([https\://github\.com/ansible\-collections/community\.general/pull/8674](https\://github\.com/ansible\-collections/community\.general/pull/8674)\)\.
* gitlab\_project \- add option <code>service\_desk\_enabled</code> to disable service desk \([https\://github\.com/ansible\-collections/community\.general/pull/8688](https\://github\.com/ansible\-collections/community\.general/pull/8688)\)\.
* locale\_gen \- add support for multiple locales \([https\://github\.com/ansible\-collections/community\.general/issues/8677](https\://github\.com/ansible\-collections/community\.general/issues/8677)\, [https\://github\.com/ansible\-collections/community\.general/pull/8682](https\://github\.com/ansible\-collections/community\.general/pull/8682)\)\.
* memcached\, pickle\, redis\, yaml cache plugins \- make sure that all options are typed \([https\://github\.com/ansible\-collections/community\.general/pull/8624](https\://github\.com/ansible\-collections/community\.general/pull/8624)\)\.
* opentelemetry callback plugin \- fix default value for <code>store\_spans\_in\_file</code> causing traces to be produced to a file named <code>None</code> \([https\://github\.com/ansible\-collections/community\.general/issues/8566](https\://github\.com/ansible\-collections/community\.general/issues/8566)\, [https\://github\.com/ansible\-collections/community\.general/pull/8741](https\://github\.com/ansible\-collections/community\.general/pull/8741)\)\.
* passwordstore lookup plugin \- add the current user to the lockfile file name to address issues on multi\-user systems \([https\://github\.com/ansible\-collections/community\.general/pull/8689](https\://github\.com/ansible\-collections/community\.general/pull/8689)\)\.
* pipx \- add parameter <code>suffix</code> to module \([https\://github\.com/ansible\-collections/community\.general/pull/8675](https\://github\.com/ansible\-collections/community\.general/pull/8675)\, [https\://github\.com/ansible\-collections/community\.general/issues/8656](https\://github\.com/ansible\-collections/community\.general/issues/8656)\)\.
* pkgng \- add option <code>use\_globs</code> \(default <code>true</code>\) to optionally disable glob patterns \([https\://github\.com/ansible\-collections/community\.general/issues/8632](https\://github\.com/ansible\-collections/community\.general/issues/8632)\, [https\://github\.com/ansible\-collections/community\.general/pull/8633](https\://github\.com/ansible\-collections/community\.general/pull/8633)\)\.
* proxmox inventory plugin \- add new fact for LXC interface details \([https\://github\.com/ansible\-collections/community\.general/pull/8713](https\://github\.com/ansible\-collections/community\.general/pull/8713)\)\.
* redis\, redis\_info \- add <code>client\_cert</code> and <code>client\_key</code> options to specify path to certificate for Redis authentication  \([https\://github\.com/ansible\-collections/community\.general/pull/8654](https\://github\.com/ansible\-collections/community\.general/pull/8654)\)\.

<a id="community-routeros-2"></a>
#### community\.routeros

* api\_info \- allow to restrict the output by limiting fields to specific values with the new <code>restrict</code> option \([https\://github\.com/ansible\-collections/community\.routeros/pull/305](https\://github\.com/ansible\-collections/community\.routeros/pull/305)\)\.
* api\_info\, api\_modify \- add support for the <code>ip dhcp\-server matcher</code> path \([https\://github\.com/ansible\-collections/community\.routeros/pull/300](https\://github\.com/ansible\-collections/community\.routeros/pull/300)\)\.
* api\_info\, api\_modify \- add support for the <code>ipv6 nd prefix</code> path \([https\://github\.com/ansible\-collections/community\.routeros/pull/303](https\://github\.com/ansible\-collections/community\.routeros/pull/303)\)\.
* api\_info\, api\_modify \- add support for the <code>name</code> and <code>is\-responder</code> properties under the <code>interface wireguard peers</code> path introduced in RouterOS 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/304](https\://github\.com/ansible\-collections/community\.routeros/pull/304)\)\.
* api\_info\, api\_modify \- add support for the <code>routing ospf static\-neighbor</code> path in RouterOS 7 \([https\://github\.com/ansible\-collections/community\.routeros/pull/302](https\://github\.com/ansible\-collections/community\.routeros/pull/302)\)\.
* api\_info\, api\_modify \- set default for <code>force</code> in <code>ip dhcp\-server option</code> to an explicit <code>false</code> \([https\://github\.com/ansible\-collections/community\.routeros/pull/300](https\://github\.com/ansible\-collections/community\.routeros/pull/300)\)\.
* api\_modify \- allow to restrict what is updated by limiting fields to specific values with the new <code>restrict</code> option \([https\://github\.com/ansible\-collections/community\.routeros/pull/305](https\://github\.com/ansible\-collections/community\.routeros/pull/305)\)\.

<a id="dellemc-openmanage-12"></a>
#### dellemc\.openmanage

* idrac\_redfish\_powerstate \- This module is enhanced to support full virtual A/C power cycle\.
* idrac\_redfish\_storage\_controller \- This module is enhanced to support secure and/or cryptographic erase of the physical disk\.
* ome\_application\_network\_proxy \- This module is enhanced to manage the Proxy Exclusion List and Certificate Validation\.

<a id="f5networks-f5-modules-3"></a>
#### f5networks\.f5\_modules

* bigip\_ucs \- Fix for bigip\_ucs module to restore UCS file on BIG\-IP devices\.

<a id="fortinet-fortimanager-6"></a>
#### fortinet\.fortimanager

* Supported FortiManager 7\.4\.3\. 7 new modules\.
* Supported ansible\-core 2\.17\.

<a id="netapp-ontap-3"></a>
#### netapp\.ontap

* all modules supporting ZAPI \& REST \- throw authentication error instead of falling back to ZAPI when username/password is incorrect\.
* na\_ontap\_bgp\_peer\_group \- added new option <em class="title-reference">use\_peer\_as\_next\_hop</em>\, requires ONTAP 9\.9 or later\.
* na\_ontap\_cifs \- added REST support for option <em class="title-reference">vscan\_fileop\_profile</em>\, requires ONTAP 9\.15\.1 or later\.
* na\_ontap\_rest\_cli \- return command output for GET and OPTIONS verbs during check mode\.
* na\_ontap\_security\_key\_manager \- added warning message in REST when passphrase is not changed\.
* na\_ontap\_snapshot\_policy \- new option <em class="title-reference">retention\_period</em> added in REST\, requires ONTAP 9\.12 or later\.
* na\_ontap\_volume \- new option <em class="title-reference">activity\_tracking</em> added in REST\, requires ONTAP 9\.10 or later\.
* na\_ontap\_volume \- new option <em class="title-reference">snapshot\_locking</em> added in REST\, requires ONTAP 9\.12 or later\.

<a id="purestorage-flashblade-3"></a>
#### purestorage\.flashblade

* all \- add <code>disable\_warnings</code> parameters
* purefb\_bucket \- Add <code>safemode</code> option for <code>retention\_mode</code>
* purefb\_certs \- Update module to use REST v2 code\. This brings in new parameters for certificate management\.
* purefb\_fs \- Set default for group\_ownership to be creator
* purefb\_ra \- Add <code>duration</code> option from REST 2\.14
* purefb\_ra \- Update to REST2

<a id="theforeman-foreman-2"></a>
#### theforeman\.foreman

* redhat\_manifest \- report <code>changed</code> when manifest is regenerated and downloaded \([https\://github\.com/theforeman/foreman\-ansible\-modules/issues/1473](https\://github\.com/theforeman/foreman\-ansible\-modules/issues/1473)\)

<a id="vmware-vmware-6"></a>
#### vmware\.vmware

* cluster\_drs \- added cluster\_drs module to manage DRS settings in vcenter
* folder\_template\_from\_vm \- add module and tests to create a template from an existing VM in vcenter and store the template in a folder
* guest\_info \- migrated functionality from community vmware\_guest\_info and vmware\_vm\_info into guest\_info\. Changes are backwards compatible but legacy outputs are deprecated
* module\_utils/vmware\_tasks \- added shared utils to monitor long running tasks in vcenter
* module\_utils/vmware\_type\_utils \- added shared utils for validating\, transforming\, and comparing vcenter settings with python variables
* vm\_portgroup\_info \- add module to get all the portgroups that associated with VMs

<a id="deprecated-features-4"></a>
### Deprecated Features

<a id="community-docker-5"></a>
#### community\.docker

* The collection deprecates support for all ansible\-core versions that are currently End of Life\, [according to the ansible\-core support matrix](https\://docs\.ansible\.com/ansible\-core/devel/reference\_appendices/release\_and\_maintenance\.html\#ansible\-core\-support\-matrix)\. This means that the next major release of the collection will no longer support ansible\-core 2\.11\, ansible\-core 2\.12\, ansible\-core 2\.13\, and ansible\-core 2\.14\.

<a id="community-routeros-3"></a>
#### community\.routeros

* The collection deprecates support for all Ansible/ansible\-base/ansible\-core versions that are currently End of Life\, [according to the ansible\-core support matrix](https\://docs\.ansible\.com/ansible\-core/devel/reference\_appendices/release\_and\_maintenance\.html\#ansible\-core\-support\-matrix)\. This means that the next major release of the collection will no longer support Ansible 2\.9\, ansible\-base 2\.10\, ansible\-core 2\.11\, ansible\-core 2\.12\, ansible\-core 2\.13\, and ansible\-core 2\.14\.

<a id="community-sops-2"></a>
#### community\.sops

* The collection deprecates support for all Ansible/ansible\-base/ansible\-core versions that are currently End of Life\, [according to the ansible\-core support matrix](https\://docs\.ansible\.com/ansible\-core/devel/reference\_appendices/release\_and\_maintenance\.html\#ansible\-core\-support\-matrix)\. This means that the next major release of the collection will no longer support Ansible 2\.9\, ansible\-base 2\.10\, ansible\-core 2\.11\, ansible\-core 2\.12\, ansible\-core 2\.13\, and ansible\-core 2\.14\.

<a id="bugfixes-4"></a>
### Bugfixes

<a id="ansible-core-14"></a>
#### Ansible\-core

* Warning now includes filename and line number of variable when specifying a list of dictionaries for vars \([https\://github\.com/ansible/ansible/issues/82528](https\://github\.com/ansible/ansible/issues/82528)\)\.
* config\, restored the ability to set module compression via a variable
* debconf \- fix normalization of value representation for boolean vtypes in new packages \([https\://github\.com/ansible/ansible/issues/83594](https\://github\.com/ansible/ansible/issues/83594)\)
* linear strategy\: fix handlers included via <code>include\_tasks</code> handler to be executed in lockstep \([https\://github\.com/ansible/ansible/issues/83019](https\://github\.com/ansible/ansible/issues/83019)\)

<a id="cisco-ise-2"></a>
#### cisco\.ise

* endpoint\_group \- add missing parameter parentID\.
* mnt\_session\_active\_list\_info \- fix response xml\.
* network\_device \- mask param can be string or int\, cast to int at the end\.
* reservation \- remove duplicate parameter\.
* support\_bundle\_download \- remove duplicate parameter\.
* trusted\_certificate \- fix comparison between request and current object\.

<a id="cisco-mso-1"></a>
#### cisco\.mso

* Fix to be able to reference APIC only L3Out in mso\_schema\_site\_external\_epg

<a id="community-crypto-3"></a>
#### community\.crypto

* When using cryptography \>\= 43\.0\.0\, use offset\-aware <code>datetime\.datetime</code> objects \(with timezone UTC\) instead of offset\-naive UTC timestamps for the <code>InvalidityDate</code> X\.509 CRL extension \([https\://github\.com/ansible\-collections/community\.crypto/issues/726](https\://github\.com/ansible\-collections/community\.crypto/issues/726)\, [https\://github\.com/ansible\-collections/community\.crypto/pull/730](https\://github\.com/ansible\-collections/community\.crypto/pull/730)\)\.

<a id="community-dns-5"></a>
#### community\.dns

* Update Public Suffix List\.

<a id="community-docker-6"></a>
#### community\.docker

* docker\_compose\_v2 \- handle yet another random unstructured error output from pre\-2\.29\.0 Compose versions \([https\://github\.com/ansible\-collections/community\.docker/issues/948](https\://github\.com/ansible\-collections/community\.docker/issues/948)\, [https\://github\.com/ansible\-collections/community\.docker/pull/949](https\://github\.com/ansible\-collections/community\.docker/pull/949)\)\.
* docker\_compose\_v2 \- make sure that services provided in <code>services</code> are appended to the command line after <code>\-\-</code> and not before it \([https\://github\.com/ansible\-collections/community\.docker/pull/942](https\://github\.com/ansible\-collections/community\.docker/pull/942)\)\.
* docker\_compose\_v2\* modules\, docker\_image\_build \- provide better error message when required fields are not present in <code>docker version</code> or <code>docker info</code> output\. This can happen if Podman is used instead of Docker \([https\://github\.com/ansible\-collections/community\.docker/issues/891](https\://github\.com/ansible\-collections/community\.docker/issues/891)\, [https\://github\.com/ansible\-collections/community\.docker/pull/935](https\://github\.com/ansible\-collections/community\.docker/pull/935)\)\.
* docker\_container \- fix idempotency if <code>network\_mode\=default</code> and Docker 26\.1\.0 or later is used\. There was a breaking change in Docker 26\.1\.0 regarding normalization of <code>NetworkMode</code> \([https\://github\.com/ansible\-collections/community\.docker/issues/934](https\://github\.com/ansible\-collections/community\.docker/issues/934)\, [https\://github\.com/ansible\-collections/community\.docker/pull/936](https\://github\.com/ansible\-collections/community\.docker/pull/936)\)\.
* docker\_container \- restore behavior of the module from community\.docker 2\.x\.y that passes the first network to the Docker Deamon while creating the container \([https\://github\.com/ansible\-collections/community\.docker/pull/933](https\://github\.com/ansible\-collections/community\.docker/pull/933)\)\.
* docker\_image\_build \- fix <code>\-\-output</code> parameter composition for <code>type\=docker</code> and <code>type\=image</code> \([https\://github\.com/ansible\-collections/community\.docker/issues/946](https\://github\.com/ansible\-collections/community\.docker/issues/946)\, [https\://github\.com/ansible\-collections/community\.docker/pull/947](https\://github\.com/ansible\-collections/community\.docker/pull/947)\)\.

<a id="community-general-13"></a>
#### community\.general

* gitlab\_runner \- fix <code>paused</code> parameter being ignored \([https\://github\.com/ansible\-collections/community\.general/pull/8648](https\://github\.com/ansible\-collections/community\.general/pull/8648)\)\.
* homebrew\_cask \- fix <code>upgrade\_all</code> returns <code>changed</code> when nothing upgraded \([https\://github\.com/ansible\-collections/community\.general/issues/8707](https\://github\.com/ansible\-collections/community\.general/issues/8707)\, [https\://github\.com/ansible\-collections/community\.general/pull/8708](https\://github\.com/ansible\-collections/community\.general/pull/8708)\)\.
* keycloak\_user\_federation \- get cleartext IDP <code>clientSecret</code> from full realm info to detect changes to it \([https\://github\.com/ansible\-collections/community\.general/issues/8294](https\://github\.com/ansible\-collections/community\.general/issues/8294)\, [https\://github\.com/ansible\-collections/community\.general/pull/8735](https\://github\.com/ansible\-collections/community\.general/pull/8735)\)\.
* keycloak\_user\_federation \- remove existing user federation mappers if they are not present in the federation configuration and will not be updated \([https\://github\.com/ansible\-collections/community\.general/issues/7169](https\://github\.com/ansible\-collections/community\.general/issues/7169)\, [https\://github\.com/ansible\-collections/community\.general/pull/8695](https\://github\.com/ansible\-collections/community\.general/pull/8695)\)\.
* proxmox \- fixed an issue where the new volume handling incorrectly converted <code>null</code> values into <code>\"None\"</code> strings \([https\://github\.com/ansible\-collections/community\.general/pull/8646](https\://github\.com/ansible\-collections/community\.general/pull/8646)\)\.
* proxmox \- fixed an issue where volume strings where overwritten instead of appended to in the new <code>build\_volume\(\)</code> method \([https\://github\.com/ansible\-collections/community\.general/pull/8646](https\://github\.com/ansible\-collections/community\.general/pull/8646)\)\.
* proxmox \- removed the forced conversion of non\-string values to strings to be consistent with the module documentation \([https\://github\.com/ansible\-collections/community\.general/pull/8646](https\://github\.com/ansible\-collections/community\.general/pull/8646)\)\.

<a id="community-routeros-4"></a>
#### community\.routeros

* api\_modify\, api\_info \- change the default of <code>ingress\-filtering</code> in paths <code>interface bridge</code> and <code>interface bridge port</code> back to <code>false</code> for RouterOS before version 7 \([https\://github\.com/ansible\-collections/community\.routeros/pull/305](https\://github\.com/ansible\-collections/community\.routeros/pull/305)\)\.

<a id="community-sops-3"></a>
#### community\.sops

* Pass <code>config\_path</code> on SOPS 3\.9\.0 before the subcommand instead of after it \([https\://github\.com/ansible\-collections/community\.sops/issues/195](https\://github\.com/ansible\-collections/community\.sops/issues/195)\, [https\://github\.com/ansible\-collections/community\.sops/pull/197](https\://github\.com/ansible\-collections/community\.sops/pull/197)\)\.

<a id="fortinet-fortimanager-7"></a>
#### fortinet\.fortimanager

* Added more description in the documentation\.
* Deleted 9 fmgr\_switchcontroller\_managedswitch\_\* modules\. Will support them in FortiManager Device Ansible\.
* Improved fmgr\_fact\, fmgr\_clone\, fmgr\_move\.

<a id="netapp-ontap-4"></a>
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

<a id="purestorage-flasharray-5"></a>
#### purestorage\.flasharray

* purefa\_dsrole \- Fix function name typo
* purefa\_info \- Fixed issue trying to collect deleted volumes perfomance stats
* purefa\_pg \- Fix parameter name typo
* purefa\_volume \- Fix issue with creating volume using old Purity version \(6\.1\.19\)

<a id="purestorage-flashblade-4"></a>
#### purestorage\.flashblade

* purefb\_fs \- Fix conflict with SMB mode and ACL safeguarding
* purefb\_fs \- Fix error checking for SMB parameter in non\-SMB filesystem
* purefb\_info \- Fix space reporting issue

<a id="vmware-vmware-7"></a>
#### vmware\.vmware

* \_vmware\_facts \- fixed typo in hw\_interfaces fact key and added missing annotation fact key and value
* \_vmware\_folder\_paths \- fixed issue where resolved folder paths incorrectly included a leading slash
* guest\_info \- added more optional attributes to the example
* module\_utils/vmware\_rest\_client \- rename get\_vm\_by\_name method as there is same signature already

<a id="known-issues-4"></a>
### Known Issues

<a id="community-docker-7"></a>
#### community\.docker

* docker\_container \- when specifying a MAC address for a container\'s network\, and the network is attached after container creation \(for example\, due to idempotency checks\)\, the MAC address is at least in some cases ignored by the Docker Daemon \([https\://github\.com/ansible\-collections/community\.docker/pull/933](https\://github\.com/ansible\-collections/community\.docker/pull/933)\)\.

<a id="dellemc-openmanage-13"></a>
#### dellemc\.openmanage

* idrac\_diagnostics \- Issue\(285322\) \- This module doesn\'t support export of diagnostics file to HTTP and HTTPS share via SOCKS proxy\.
* idrac\_firmware \- Issue\(279282\) \- This module does not support firmware update using HTTP\, HTTPS\, and FTP shares with authentication on iDRAC8\.
* idrac\_storage\_volume \- Issue\(290766\) \- The module will report success instead of showing failure for new virtual creation on the BOSS\-N1 controller if a virtual disk is already present on the same controller\.
* ome\_diagnostics \- Issue\(279193\) \- Export of SupportAssist collection logs to the share location fails on OME version 4\.0\.0\.
* ome\_smart\_fabric\_uplink \- Issue\(186024\) \- The module supported by OpenManage Enterprise Modular\, however it does not allow the creation of multiple uplinks of the same name\. If an uplink is created using the same name as an existing uplink\, then the existing uplink is modified\.

<a id="new-modules-4"></a>
### New Modules

<a id="community-general-14"></a>
#### community\.general

* community\.general\.bootc\_manage \- Bootc Switch and Upgrade\.
* community\.general\.homebrew\_services \- Services manager for Homebrew\.
* community\.general\.keycloak\_realm\_keys\_metadata\_info \- Allows obtaining Keycloak realm keys metadata via Keycloak API\.

<a id="fortinet-fortimanager-8"></a>
#### fortinet\.fortimanager

* fortinet\.fortimanager\.fmgr\_extensioncontroller\_extenderprofile\_wifi \- FortiExtender wifi configuration\.
* fortinet\.fortimanager\.fmgr\_extensioncontroller\_extenderprofile\_wifi\_radio1 \- Radio\-1 config for Wi\-Fi 2\.
* fortinet\.fortimanager\.fmgr\_extensioncontroller\_extenderprofile\_wifi\_radio2 \- Radio\-2 config for Wi\-Fi 5GHz
* fortinet\.fortimanager\.fmgr\_firewall\_sslsshprofile\_echoutersni \- ClientHelloOuter SNIs to be blocked\.
* fortinet\.fortimanager\.fmgr\_system\_log\_ueba \- UEBAsettings\.
* fortinet\.fortimanager\.fmgr\_system\_npu\_icmpratectrl \- Configure the rate of ICMP messages generated by this FortiGate\.
* fortinet\.fortimanager\.fmgr\_user\_externalidentityprovider \- Configure external identity provider\.

<a id="theforeman-foreman-3"></a>
#### theforeman\.foreman

* theforeman\.foreman\.content\_import\_info \- List content imports
* theforeman\.foreman\.content\_import\_library \- Manage library content imports
* theforeman\.foreman\.content\_import\_repository \- Manage repository content imports
* theforeman\.foreman\.content\_import\_version \- Manage content view version content imports

<a id="vmware-vmware-8"></a>
#### vmware\.vmware

* vmware\.vmware\.vm\_portgroup\_info \- Returns information about the portgroups of virtual machines

<a id="unchanged-collections-4"></a>
### Unchanged Collections

* amazon\.aws \(still version 8\.1\.0\)
* ansible\.netcommon \(still version 6\.1\.3\)
* ansible\.posix \(still version 1\.5\.4\)
* ansible\.utils \(still version 4\.1\.0\)
* ansible\.windows \(still version 2\.4\.0\)
* arista\.eos \(still version 9\.0\.0\)
* awx\.awx \(still version 24\.6\.1\)
* azure\.azcollection \(still version 2\.6\.0\)
* check\_point\.mgmt \(still version 5\.2\.3\)
* chocolatey\.chocolatey \(still version 1\.5\.1\)
* cisco\.aci \(still version 2\.10\.1\)
* cisco\.asa \(still version 5\.0\.1\)
* cisco\.ios \(still version 8\.0\.0\)
* cisco\.iosxr \(still version 9\.0\.0\)
* cisco\.meraki \(still version 2\.18\.1\)
* cisco\.nxos \(still version 8\.1\.0\)
* cisco\.ucs \(still version 1\.10\.0\)
* cloud\.common \(still version 3\.0\.0\)
* community\.aws \(still version 8\.0\.0\)
* community\.ciscosmb \(still version 1\.0\.9\)
* community\.digitalocean \(still version 1\.26\.0\)
* community\.grafana \(still version 1\.9\.1\)
* community\.hashi\_vault \(still version 6\.2\.0\)
* community\.hrobot \(still version 2\.0\.1\)
* community\.library\_inventory\_filtering\_v1 \(still version 1\.0\.1\)
* community\.libvirt \(still version 1\.3\.0\)
* community\.mysql \(still version 3\.9\.0\)
* community\.network \(still version 5\.0\.3\)
* community\.okd \(still version 3\.0\.1\)
* community\.postgresql \(still version 3\.4\.1\)
* community\.proxysql \(still version 1\.6\.0\)
* community\.rabbitmq \(still version 1\.3\.0\)
* community\.sap\_libs \(still version 1\.4\.2\)
* community\.vmware \(still version 4\.5\.0\)
* community\.windows \(still version 2\.2\.0\)
* community\.zabbix \(still version 2\.5\.1\)
* containers\.podman \(still version 1\.15\.4\)
* cyberark\.conjur \(still version 1\.3\.0\)
* dellemc\.enterprise\_sonic \(still version 2\.4\.0\)
* dellemc\.powerflex \(still version 2\.5\.0\)
* dellemc\.unity \(still version 2\.0\.0\)
* fortinet\.fortios \(still version 2\.3\.7\)
* frr\.frr \(still version 2\.0\.2\)
* google\.cloud \(still version 1\.3\.0\)
* hetzner\.hcloud \(still version 3\.1\.1\)
* ibm\.qradar \(still version 3\.0\.0\)
* ibm\.spectrum\_virtualize \(still version 2\.0\.0\)
* ibm\.storage\_virtualize \(still version 2\.4\.1\)
* ieisystem\.inmanage \(still version 2\.0\.0\)
* infinidat\.infinibox \(still version 1\.4\.5\)
* infoblox\.nios\_modules \(still version 1\.6\.1\)
* inspur\.ispim \(still version 2\.2\.3\)
* inspur\.sm \(still version 2\.3\.0\)
* junipernetworks\.junos \(still version 8\.0\.0\)
* kaytus\.ksmanage \(still version 1\.2\.2\)
* kubernetes\.core \(still version 3\.2\.0\)
* kubevirt\.core \(still version 1\.5\.0\)
* lowlydba\.sqlserver \(still version 2\.3\.3\)
* microsoft\.ad \(still version 1\.6\.0\)
* netapp\.cloudmanager \(still version 21\.22\.1\)
* netapp\.storagegrid \(still version 21\.12\.0\)
* netapp\_eseries\.santricity \(still version 1\.4\.0\)
* netbox\.netbox \(still version 3\.19\.1\)
* ngine\_io\.cloudstack \(still version 2\.3\.0\)
* ngine\_io\.exoscale \(still version 1\.1\.0\)
* openstack\.cloud \(still version 2\.2\.0\)
* openvswitch\.openvswitch \(still version 2\.1\.1\)
* ovirt\.ovirt \(still version 3\.2\.0\)
* sensu\.sensu\_go \(still version 1\.14\.0\)
* splunk\.es \(still version 3\.0\.0\)
* t\_systems\_mms\.icinga\_director \(still version 2\.0\.1\)
* telekom\_mms\.icinga\_director \(still version 2\.1\.2\)
* vmware\.vmware\_rest \(still version 3\.0\.1\)
* vultr\.cloud \(still version 1\.13\.0\)
* vyos\.vyos \(still version 4\.1\.0\)
* wti\.remote \(still version 1\.0\.5\)

<a id="v10-2-0"></a>
## v10\.2\.0

- <a href="#release-summary-5">Release Summary</a>
- <a href="#added-collections">Added Collections</a>
- <a href="#ansible-core-15">Ansible\-core</a>
- <a href="#changed-collections-5">Changed Collections</a>
- <a href="#major-changes-4">Major Changes</a>
    - <a href="#dellemc-openmanage-14">dellemc\.openmanage</a>
    - <a href="#fortinet-fortios-2">fortinet\.fortios</a>
    - <a href="#grafana-grafana-2">grafana\.grafana</a>
- <a href="#minor-changes-5">Minor Changes</a>
    - <a href="#amazon-aws-3">amazon\.aws</a>
    - <a href="#cisco-aci">cisco\.aci</a>
    - <a href="#cisco-mso-2">cisco\.mso</a>
    - <a href="#community-crypto-4">community\.crypto</a>
    - <a href="#community-docker-8">community\.docker</a>
    - <a href="#community-general-15">community\.general</a>
    - <a href="#community-proxysql">community\.proxysql</a>
    - <a href="#community-routeros-5">community\.routeros</a>
    - <a href="#community-sops-4">community\.sops</a>
    - <a href="#community-vmware-8">community\.vmware</a>
    - <a href="#containers-podman-4">containers\.podman</a>
    - <a href="#dellemc-openmanage-15">dellemc\.openmanage</a>
    - <a href="#f5networks-f5-modules-4">f5networks\.f5\_modules</a>
    - <a href="#ibm-storage-virtualize-2">ibm\.storage\_virtualize</a>
    - <a href="#purestorage-flasharray-6">purestorage\.flasharray</a>
- <a href="#deprecated-features-5">Deprecated Features</a>
- <a href="#bugfixes-5">Bugfixes</a>
    - <a href="#ansible-core-16">Ansible\-core</a>
    - <a href="#cisco-aci-1">cisco\.aci</a>
    - <a href="#cisco-mso-3">cisco\.mso</a>
    - <a href="#community-dns-6">community\.dns</a>
    - <a href="#community-docker-9">community\.docker</a>
    - <a href="#community-general-16">community\.general</a>
    - <a href="#community-proxysql-1">community\.proxysql</a>
    - <a href="#community-sops-5">community\.sops</a>
    - <a href="#community-vmware-9">community\.vmware</a>
    - <a href="#containers-podman-5">containers\.podman</a>
    - <a href="#dellemc-openmanage-16">dellemc\.openmanage</a>
    - <a href="#fortinet-fortios-3">fortinet\.fortios</a>
    - <a href="#ibm-storage-virtualize-3">ibm\.storage\_virtualize</a>
    - <a href="#purestorage-flasharray-7">purestorage\.flasharray</a>
- <a href="#known-issues-5">Known Issues</a>
    - <a href="#dellemc-openmanage-17">dellemc\.openmanage</a>
- <a href="#new-plugins-1">New Plugins</a>
    - <a href="#filter-1">Filter</a>
    - <a href="#test">Test</a>
- <a href="#new-modules-5">New Modules</a>
    - <a href="#purestorage-flasharray-8">purestorage\.flasharray</a>
- <a href="#unchanged-collections-5">Unchanged Collections</a>

<a id="release-summary-5"></a>
### Release Summary

Release Date\: 2024\-07\-16

[Porting Guide](https\://docs\.ansible\.com/ansible/devel/porting\_guides\.html)

<a id="added-collections"></a>
### Added Collections

* kubevirt\.core \(version 1\.5\.0\)
* vmware\.vmware \(version 1\.3\.0\)

<a id="ansible-core-15"></a>
### Ansible\-core

Ansible 10\.2\.0 contains ansible\-core version 2\.17\.2\.
This is a newer version than version 2\.17\.1 contained in the previous Ansible release\.

The changes are reported in the combined changelog below\.

<a id="changed-collections-5"></a>
### Changed Collections

If not mentioned explicitly\, the changes are reported in the combined changelog below\.

| Collection             | Ansible 10.1.0 | Ansible 10.2.0 | Notes                                                                                                                        |
| ---------------------- | -------------- | -------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| amazon.aws             | 8.0.1          | 8.1.0          |                                                                                                                              |
| awx.awx                | 24.5.0         | 24.6.1         | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
| azure.azcollection     | 2.4.0          | 2.6.0          | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
| cisco.aci              | 2.9.0          | 2.10.1         |                                                                                                                              |
| cisco.mso              | 2.6.0          | 2.8.0          |                                                                                                                              |
| community.crypto       | 2.20.0         | 2.21.0         |                                                                                                                              |
| community.dns          | 3.0.1          | 3.0.2          |                                                                                                                              |
| community.docker       | 3.10.4         | 3.11.0         |                                                                                                                              |
| community.general      | 9.1.0          | 9.2.0          |                                                                                                                              |
| community.mongodb      | 1.7.4          | 1.7.5          | There are no changes recorded in the changelog.                                                                              |
| community.proxysql     | 1.5.1          | 1.6.0          |                                                                                                                              |
| community.routeros     | 2.16.0         | 2.17.0         |                                                                                                                              |
| community.sops         | 1.6.7          | 1.8.0          |                                                                                                                              |
| community.vmware       | 4.4.0          | 4.5.0          |                                                                                                                              |
| containers.podman      | 1.15.2         | 1.15.4         |                                                                                                                              |
| dellemc.openmanage     | 9.3.0          | 9.4.0          |                                                                                                                              |
| f5networks.f5_modules  | 1.28.0         | 1.29.0         |                                                                                                                              |
| fortinet.fortios       | 2.3.6          | 2.3.7          |                                                                                                                              |
| grafana.grafana        | 5.2.0          | 5.3.0          |                                                                                                                              |
| ibm.storage_virtualize | 2.3.1          | 2.4.1          |                                                                                                                              |
| kubevirt.core          |                | 1.5.0          | The collection was added to Ansible                                                                                          |
| purestorage.flasharray | 1.28.1         | 1.30.0         |                                                                                                                              |
| vmware.vmware          |                | 1.3.0          | The collection was added to Ansible                                                                                          |

<a id="major-changes-4"></a>
### Major Changes

<a id="dellemc-openmanage-14"></a>
#### dellemc\.openmanage

* idrac\_server\_config\_profile \- This module is enhanced to allow you to export and import custom defaults on iDRAC\.
* ome\_configuration\_compliance\_baseline \- This module is enhanced to schedule the remediation job and stage the reboot\.

<a id="fortinet-fortios-2"></a>
#### fortinet\.fortios

* Add a sanity\_test\.yaml file to trigger CI tests in GitHub\.
* Support Ansible\-core 2\.17\.
* Support new FOS versions 7\.4\.4\.

<a id="grafana-grafana-2"></a>
#### grafana\.grafana

* Add a config check before restarting mimir by \@panfantastic in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/198](https\://github\.com/grafana/grafana\-ansible\-collection/pull/198)
* Add support for configuring feature\_toggles in grafana role by \@LexVar in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/173](https\://github\.com/grafana/grafana\-ansible\-collection/pull/173)
* Backport post\-setup healthcheck from agent to alloy by \@v\-zhuravlev in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/213](https\://github\.com/grafana/grafana\-ansible\-collection/pull/213)
* Bump ansible\-lint from 24\.2\.3 to 24\.5\.0 by \@dependabot in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/207](https\://github\.com/grafana/grafana\-ansible\-collection/pull/207)
* Bump ansible\-lint from 24\.5\.0 to 24\.6\.0 by \@dependabot in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/216](https\://github\.com/grafana/grafana\-ansible\-collection/pull/216)
* Bump braces from 3\.0\.2 to 3\.0\.3 in the npm\_and\_yarn group across 1 directory by \@dependabot in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/218](https\://github\.com/grafana/grafana\-ansible\-collection/pull/218)
* Bump pylint from 3\.1\.0 to 3\.1\.1 by \@dependabot in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/200](https\://github\.com/grafana/grafana\-ansible\-collection/pull/200)
* Bump pylint from 3\.1\.1 to 3\.2\.2 by \@dependabot in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/208](https\://github\.com/grafana/grafana\-ansible\-collection/pull/208)
* Bump pylint from 3\.2\.2 to 3\.2\.3 by \@dependabot in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/217](https\://github\.com/grafana/grafana\-ansible\-collection/pull/217)
* Bump pylint from 3\.2\.3 to 3\.2\.5 by \@dependabot in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/234](https\://github\.com/grafana/grafana\-ansible\-collection/pull/234)
* Change from config\.river to config\.alloy by \@cardasac in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/225](https\://github\.com/grafana/grafana\-ansible\-collection/pull/225)
* Fix Grafana Configuration for Unified and Legacy Alerting Based on Version by \@voidquark in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/215](https\://github\.com/grafana/grafana\-ansible\-collection/pull/215)
* Support adding alloy user to extra groups by \@v\-zhuravlev in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/212](https\://github\.com/grafana/grafana\-ansible\-collection/pull/212)
* Updated result\.json\[\'message\'\] to result\.json\(\)\[\'message\'\] by \@CPreun in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/223](https\://github\.com/grafana/grafana\-ansible\-collection/pull/223)

<a id="minor-changes-5"></a>
### Minor Changes

<a id="amazon-aws-3"></a>
#### amazon\.aws

* s3\_bucket \- Add <code>object\_lock\_default\_retention</code> to set Object Lock default retention configuration for S3 buckets \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2062](https\://github\.com/ansible\-collections/amazon\.aws/pull/2062)\)\.
* s3\_bucket \- Add support for enabling Amazon S3 Transfer Acceleration by setting the <code>accelerate\_enabled</code> option \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2046](https\://github\.com/ansible\-collections/amazon\.aws/pull/2046)\)\.

<a id="cisco-aci"></a>
#### cisco\.aci

* Add aci\_esg\_to\_contract module for esg contract relationship objects fvRsCons \(consumer\)\, fvRsConsIf \(consumer interface\)\, fvRsProv \(provider\) and fvRsIntraEpg \(intra\_esg\)
* Add aci\_system\_connectivity\_preference module \(\#601\)
* Added suppress\-previous flag option to reduce the number of API calls\. \(\#636\)
* Enable relative path and/or filename of private key for the aci httpapi plugin\.

<a id="cisco-mso-2"></a>
#### cisco\.mso

* Add module mso\_schema\_template\_vrf\_rp to support multicast vrf rp in application templates
* Add module ndo\_dhcp\_option\_policy to support dhcp option policy configuration in tenant templates
* Add module ndo\_dhcp\_relay\_policy to support dhcp relay policy configuration in tenant templates
* Add module ndo\_l3\_domain and ndo\_physical\_domain to support domain configuration in fabric policy templates
* Add module ndo\_vlan\_pool to support vlan pool configuration in fabric policy templates
* Add site\_aware\_policy\_enforcement and bd\_enforcement\_status arguments to the mso\_schema\_template\_vrf module
* Add support for multicast route map filters in mso\_schema\_template\_bd
* Added module ndo\_route\_map\_policy\_multicast to support multicast route map policies configuration in tenant templates
* Added module ndo\_template to support creation of tenant\, l3out\, fabric\_policy\, fabric\_resource\, monitoring\_tenant\, monitoring\_access and service\_device templates

<a id="community-crypto-4"></a>
#### community\.crypto

* certificate\_complete\_chain \- add ability to identify Ed25519 and Ed448 complete chains \([https\://github\.com/ansible\-collections/community\.crypto/pull/777](https\://github\.com/ansible\-collections/community\.crypto/pull/777)\)\.
* get\_certificate \- adds <code>tls\_ctx\_options</code> option for specifying SSL CTX options \([https\://github\.com/ansible\-collections/community\.crypto/pull/779](https\://github\.com/ansible\-collections/community\.crypto/pull/779)\)\.
* get\_certificate \- allow to obtain the certificate chain sent by the server\, and the one used for validation\, with the new <code>get\_certificate\_chain</code> option\. Note that this option only works if the module is run with Python 3\.10 or newer \([https\://github\.com/ansible\-collections/community\.crypto/issues/568](https\://github\.com/ansible\-collections/community\.crypto/issues/568)\, [https\://github\.com/ansible\-collections/community\.crypto/pull/784](https\://github\.com/ansible\-collections/community\.crypto/pull/784)\)\.

<a id="community-docker-8"></a>
#### community\.docker

* docker\_container \- add support for <code>device\_cgroup\_rules</code> \([https\://github\.com/ansible\-collections/community\.docker/pull/910](https\://github\.com/ansible\-collections/community\.docker/pull/910)\)\.
* docker\_container \- the new <code>state\=healthy</code> allows to wait for a container to become healthy on startup\. The <code>healthy\_wait\_timeout</code> option allows to configure the maximum time to wait for this to happen \([https\://github\.com/ansible\-collections/community\.docker/issues/890](https\://github\.com/ansible\-collections/community\.docker/issues/890)\, [https\://github\.com/ansible\-collections/community\.docker/pull/921](https\://github\.com/ansible\-collections/community\.docker/pull/921)\)\.

<a id="community-general-15"></a>
#### community\.general

* CmdRunner module utils \- the parameter <code>force\_lang</code> now supports the special value <code>auto</code> which will automatically try and determine the best parsable locale in the system \([https\://github\.com/ansible\-collections/community\.general/pull/8517](https\://github\.com/ansible\-collections/community\.general/pull/8517)\)\.
* proxmox \- add <code>disk\_volume</code> and <code>mount\_volumes</code> keys for better readability \([https\://github\.com/ansible\-collections/community\.general/pull/8542](https\://github\.com/ansible\-collections/community\.general/pull/8542)\)\.
* proxmox \- translate the old <code>disk</code> and <code>mounts</code> keys to the new handling internally \([https\://github\.com/ansible\-collections/community\.general/pull/8542](https\://github\.com/ansible\-collections/community\.general/pull/8542)\)\.
* proxmox\_template \- small refactor in logic for determining whether a template exists or not \([https\://github\.com/ansible\-collections/community\.general/pull/8516](https\://github\.com/ansible\-collections/community\.general/pull/8516)\)\.
* redfish\_\* modules \- adds <code>ciphers</code> option for custom cipher selection \([https\://github\.com/ansible\-collections/community\.general/pull/8533](https\://github\.com/ansible\-collections/community\.general/pull/8533)\)\.
* sudosu become plugin \- added an option \(<code>alt\_method</code>\) to enhance compatibility with more versions of <code>su</code> \([https\://github\.com/ansible\-collections/community\.general/pull/8214](https\://github\.com/ansible\-collections/community\.general/pull/8214)\)\.
* virtualbox inventory plugin \- expose a new parameter <code>enable\_advanced\_group\_parsing</code> to change how the VirtualBox dynamic inventory parses VM groups \([https\://github\.com/ansible\-collections/community\.general/issues/8508](https\://github\.com/ansible\-collections/community\.general/issues/8508)\, [https\://github\.com/ansible\-collections/community\.general/pull/8510](https\://github\.com/ansible\-collections/community\.general/pull/8510)\)\.
* wdc\_redfish\_command \- minor change to handle upgrade file for Redfish WD platforms \([https\://github\.com/ansible\-collections/community\.general/pull/8444](https\://github\.com/ansible\-collections/community\.general/pull/8444)\)\.

<a id="community-proxysql"></a>
#### community\.proxysql

* proxysql role \- add the pidfile location management \([https\://github\.com/ansible\-collections/community\.proxysql/pull/145](https\://github\.com/ansible\-collections/community\.proxysql/pull/145)\)\.
* role\_proxysql \- Update default proxysql version and fix small bugs \([https\://github\.com/ansible\-collections/community\.proxysql/pull/92](https\://github\.com/ansible\-collections/community\.proxysql/pull/92)\)\.

<a id="community-routeros-5"></a>
#### community\.routeros

* api\_info\, api\_modify \- add <code>system health settings</code> path \([https\://github\.com/ansible\-collections/community\.routeros/pull/294](https\://github\.com/ansible\-collections/community\.routeros/pull/294)\)\.
* api\_info\, api\_modify \- add missing path <code>/system resource irq rps</code> \([https\://github\.com/ansible\-collections/community\.routeros/pull/295](https\://github\.com/ansible\-collections/community\.routeros/pull/295)\)\.
* api\_info\, api\_modify \- add parameter <code>host\-key\-type</code> for <code>ip ssh</code> path \([https\://github\.com/ansible\-collections/community\.routeros/issues/280](https\://github\.com/ansible\-collections/community\.routeros/issues/280)\, [https\://github\.com/ansible\-collections/community\.routeros/pull/297](https\://github\.com/ansible\-collections/community\.routeros/pull/297)\)\.

<a id="community-sops-4"></a>
#### community\.sops

* Detect SOPS 3\.9\.0 and use new <code>decrypt</code> and <code>encrypt</code> subcommands \([https\://github\.com/ansible\-collections/community\.sops/pull/190](https\://github\.com/ansible\-collections/community\.sops/pull/190)\)\.
* sops vars plugin \- allow to configure the valid extensions with an <code>ansible\.cfg</code> entry or with an environment variable \([https\://github\.com/ansible\-collections/community\.sops/pull/185](https\://github\.com/ansible\-collections/community\.sops/pull/185)\)\.
* sops vars plugin \- new option <code>handle\_unencrypted\_files</code> allows to control behavior when encountering unencrypted files with SOPS 3\.9\.0\+ \([https\://github\.com/ansible\-collections/community\.sops/pull/190](https\://github\.com/ansible\-collections/community\.sops/pull/190)\)\.

<a id="community-vmware-8"></a>
#### community\.vmware

* vmware\_host\_logbundle \- Add timeout parameter \([https\://github\.com/ansible\-collections/community\.vmware/pull/2092](https\://github\.com/ansible\-collections/community\.vmware/pull/2092)\)\.

<a id="containers-podman-4"></a>
#### containers\.podman

* CI Update python for latest Ansible to 3\.11 in CI

<a id="dellemc-openmanage-15"></a>
#### dellemc\.openmanage

* idrac\_reset \- This module is enhanced to provide default username and default password for the reset operation\.

<a id="f5networks-f5-modules-4"></a>
#### f5networks\.f5\_modules

* bigip\_pool\_member \- Removed state from the Returnables\.

<a id="ibm-storage-virtualize-2"></a>
#### ibm\.storage\_virtualize

* ibm\_sv\_manage\_security \- Added support to allow automatic download of security patches
* ibm\_svc\_info \- Added support to display concise view of all SVC objects not covered by I\(gather\_subset\)\, detailed view for all SVC objects\, concise view of a subset of objects allowing a I\(filtervalue\)

<a id="purestorage-flasharray-6"></a>
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

<a id="deprecated-features-5"></a>
### Deprecated Features

* The <code>frr\.frr</code> collection has been deprecated\.
  It will be removed from Ansible 11 if no one starts maintaining it again before Ansible 11\.
  See [Collections Removal Process for unmaintained collections](https\://docs\.ansible\.com/ansible/devel/community/collection\_contributors/collection\_package\_removal\.html\#unmaintained\-collections) for more details \([https\://forum\.ansible\.com/t/6243](https\://forum\.ansible\.com/t/6243)\)\.
* The <code>openvswitch\.openvswitch</code> collection has been deprecated\.
  It will be removed from Ansible 11 if no one starts maintaining it again before Ansible 11\.
  See [Collections Removal Process for unmaintained collections](https\://docs\.ansible\.com/ansible/devel/community/collection\_contributors/collection\_package\_removal\.html\#unmaintained\-collections) for more details \([https\://forum\.ansible\.com/t/6245](https\://forum\.ansible\.com/t/6245)\)\.

<a id="bugfixes-5"></a>
### Bugfixes

<a id="ansible-core-16"></a>
#### Ansible\-core

* Fix a traceback when an environment variable contains certain special characters \([https\://github\.com/ansible/ansible/issues/83498](https\://github\.com/ansible/ansible/issues/83498)\)
* dnf \- reverted incomplete fix from 2\.17\.2rc1 \([https\://github\.com/ansible/ansible/pull/83504](https\://github\.com/ansible/ansible/pull/83504)\)
* dnf\, dnf5 \- fix for installing a set of packages by specifying them using a wildcard character \([https\://github\.com/ansible/ansible/issues/83373](https\://github\.com/ansible/ansible/issues/83373)\)
* linear strategy now provides a properly templated task name to the v2\_runner\_on\_started callback event\.
* package\_facts \- ignore warnings sent by apk on stderr \([https\://github\.com/ansible/ansible/issues/83501](https\://github\.com/ansible/ansible/issues/83501)\)\.
* replace \- Updated before/after example \([https\://github\.com/ansible/ansible/issues/83390](https\://github\.com/ansible/ansible/issues/83390)\)\.
* templating hostvars under native jinja will not cause serialization errors anymore\.

<a id="cisco-aci-1"></a>
#### cisco\.aci

* Remove duplicate alias name for attribute epg in aci\_epg\_subnet module

<a id="cisco-mso-3"></a>
#### cisco\.mso

* Fix to avoid making updates to attributes that are not provided which could lead to removal of configuration in mso\_schema\_template\_bd
* Fix to avoid making updates to attributes that are not provided which could lead to removal of configuration in mso\_schema\_template\_vrf

<a id="community-dns-6"></a>
#### community\.dns

* Update Public Suffix List\.

<a id="community-docker-9"></a>
#### community\.docker

* docker\_compose\_v2\* modules \- fix parsing of skipped pull messages for Docker Compose 2\.28\.x \([https\://github\.com/ansible\-collections/community\.docker/issues/911](https\://github\.com/ansible\-collections/community\.docker/issues/911)\, [https\://github\.com/ansible\-collections/community\.docker/pull/916](https\://github\.com/ansible\-collections/community\.docker/pull/916)\)\.
* docker\_compose\_v2\*\, docker\_stack\*\, docker\_image\_build modules \- using <code>cli\_context</code> no longer leads to an invalid parameter combination being passed to the corresponding Docker CLI tool\, unless <code>docker\_host</code> is also provided\. Combining <code>cli\_context</code> and <code>docker\_host</code> is no longer allowed \([https\://github\.com/ansible\-collections/community\.docker/issues/892](https\://github\.com/ansible\-collections/community\.docker/issues/892)\, [https\://github\.com/ansible\-collections/community\.docker/pull/895](https\://github\.com/ansible\-collections/community\.docker/pull/895)\)\.
* docker\_container \- fix possible infinite loop if <code>removal\_wait\_timeout</code> is set \([https\://github\.com/ansible\-collections/community\.docker/pull/922](https\://github\.com/ansible\-collections/community\.docker/pull/922)\)\.
* vendored Docker SDK for Python \- use <code>LooseVersion</code> instead of <code>StrictVersion</code> to compare urllib3 versions\. This is needed for development versions \([https\://github\.com/ansible\-collections/community\.docker/pull/902](https\://github\.com/ansible\-collections/community\.docker/pull/902)\)\.

<a id="community-general-16"></a>
#### community\.general

* bitwarden lookup plugin \- fix <code>KeyError</code> in <code>search\_field</code> \([https\://github\.com/ansible\-collections/community\.general/issues/8549](https\://github\.com/ansible\-collections/community\.general/issues/8549)\, [https\://github\.com/ansible\-collections/community\.general/pull/8557](https\://github\.com/ansible\-collections/community\.general/pull/8557)\)\.
* keycloak\_clientscope \- remove IDs from clientscope and its protocol mappers on comparison for changed check \([https\://github\.com/ansible\-collections/community\.general/pull/8545](https\://github\.com/ansible\-collections/community\.general/pull/8545)\)\.
* nsupdate \- fix \'index out of range\' error when changing NS records by falling back to authority section of the response \([https\://github\.com/ansible\-collections/community\.general/issues/8612](https\://github\.com/ansible\-collections/community\.general/issues/8612)\, [https\://github\.com/ansible\-collections/community\.general/pull/8614](https\://github\.com/ansible\-collections/community\.general/pull/8614)\)\.
* proxmox \- fix idempotency on creation of mount volumes using Proxmox\' special <code>\<storage\>\:\<size\></code> syntax \([https\://github\.com/ansible\-collections/community\.general/issues/8407](https\://github\.com/ansible\-collections/community\.general/issues/8407)\, [https\://github\.com/ansible\-collections/community\.general/pull/8542](https\://github\.com/ansible\-collections/community\.general/pull/8542)\)\.
* redfish\_utils module utils \- do not fail when language is not exactly \"en\" \([https\://github\.com/ansible\-collections/community\.general/pull/8613](https\://github\.com/ansible\-collections/community\.general/pull/8613)\)\.

<a id="community-proxysql-1"></a>
#### community\.proxysql

* module\_utils \- fix ProxySQL version parsing that fails when a suffix wasn\'t present in the version \([https\://github\.com/ansible\-collections/community\.proxysql/issues/154](https\://github\.com/ansible\-collections/community\.proxysql/issues/154)\)\.
* role\_proxysql \- Correct package name \(python3\-mysqldb instead of python\-mysqldb\) \([https\://github\.com/ansible\-collections/community\.proxysql/pull/89](https\://github\.com/ansible\-collections/community\.proxysql/pull/89)\)\.
* role\_proxysql \- Dynamic user/password in \.my\.cnf \([https\://github\.com/ansible\-collections/community\.proxysql/pull/89](https\://github\.com/ansible\-collections/community\.proxysql/pull/89)\)\.

<a id="community-sops-5"></a>
#### community\.sops

* Fix RPM URL for the 3\.9\.0 release \([https\://github\.com/ansible\-collections/community\.sops/pull/188](https\://github\.com/ansible\-collections/community\.sops/pull/188)\)\.
* sops\_encrypt \- properly support <code>path\_regex</code> in <code>\.sops\.yaml</code> when SOPS 3\.9\.0 or later is used \([https\://github\.com/ansible\-collections/community\.sops/issues/153](https\://github\.com/ansible\-collections/community\.sops/issues/153)\, [https\://github\.com/ansible\-collections/community\.sops/pull/190](https\://github\.com/ansible\-collections/community\.sops/pull/190)\)\.

<a id="community-vmware-9"></a>
#### community\.vmware

* vcenter\_folder \- removed documentation that incorrectly said <em class="title-reference">folder\_type</em> had no effect when <em class="title-reference">parent\_folder</em> was set
* vmware\_cluster\_vcls \- fixed bug caused by pyvmomi \>\=7\.0\.3 returning the vlcs cluster config attribute as None when it was previously undefined\. Now if the vCLS config is not initialized on the cluster\, the module will initialize it using the user\'s desired state\.
* vmware\_host\_logbundle \- Manifests previously was separared by \"\&\"\, thus selecting first manifest\. Fix now separates manifests with URL encoded space\, thus correctly supplying the manifests\.  \([https\://github\.com/ansible\-collections/community\.vmware/pull/2090](https\://github\.com/ansible\-collections/community\.vmware/pull/2090)\)\.

<a id="containers-podman-5"></a>
#### containers\.podman

* Fix idempotency for empty values
* Fix missing entries in network quadlet generated file
* Fix quadlet parameters for restart policy
* Idempotency improvements
* params gpus should be exit\_policy

<a id="dellemc-openmanage-16"></a>
#### dellemc\.openmanage

* Resolved the issue in <code>idrac\_reset</code> module where it fails when iDRAC is in busy state\. \([https\://github\.com/dell/dellemc\-openmanage\-ansible\-modules/issues/652](https\://github\.com/dell/dellemc\-openmanage\-ansible\-modules/issues/652)\)

<a id="fortinet-fortios-3"></a>
#### fortinet\.fortios

* Fix some issues in sanity test\.
* Github issue
* mantis issue

<a id="ibm-storage-virtualize-3"></a>
#### ibm\.storage\_virtualize

* ibm\_svc\_manage\_callhome \- Setting censorcallhome does not work
* ibm\_svc\_utils \- REST API timeout due to slow response
* ibm\_svc\_utils \- Return correct error in case of error code 500

<a id="purestorage-flasharray-7"></a>
#### purestorage\.flasharray

* purefa\_hg \- Fix edge case with incorrectly deleted hostgroup when empty array sent for volumes or hosts
* purefa\_info \- Fix typo from PR
* purefa\_info \- Resolve issue with performance stats trying to report for remote hosts

<a id="known-issues-5"></a>
### Known Issues

<a id="dellemc-openmanage-17"></a>
#### dellemc\.openmanage

* idrac\_diagnostics \- Issue\(285322\) \- This module doesn\'t support export of diagnostics file to HTTP and HTTPS share via SOCKS proxy\.
* idrac\_firmware \- Issue\(279282\) \- This module does not support firmware update using HTTP\, HTTPS\, and FTP shares with authentication on iDRAC8\.
* idrac\_storage\_volume \- Issue\(290766\) \- The module will report success instead of showing failure for new virtual creation on the BOSS\-N1 controller if a virtual disk is already present on the same controller\.
* ome\_diagnostics \- Issue\(279193\) \- Export of SupportAssist collection logs to the share location fails on OME version 4\.0\.0\.
* ome\_smart\_fabric\_uplink \- Issue\(186024\) \- The module supported by OpenManage Enterprise Modular\, however it does not allow the creation of multiple uplinks of the same name\. If an uplink is created using the same name as an existing uplink\, then the existing uplink is modified\.

<a id="new-plugins-1"></a>
### New Plugins

<a id="filter-1"></a>
#### Filter

* community\.general\.reveal\_ansible\_type \- Return input type\.

<a id="test"></a>
#### Test

* community\.general\.ansible\_type \- Validate input type\.

<a id="new-modules-5"></a>
### New Modules

<a id="purestorage-flasharray-8"></a>
#### purestorage\.flasharray

* purestorage\.flasharray\.purefa\_audits \- List FlashArray Audit Events
* purestorage\.flasharray\.purefa\_sessions \- List FlashArray Sessions

<a id="unchanged-collections-5"></a>
### Unchanged Collections

* ansible\.netcommon \(still version 6\.1\.3\)
* ansible\.posix \(still version 1\.5\.4\)
* ansible\.utils \(still version 4\.1\.0\)
* ansible\.windows \(still version 2\.4\.0\)
* arista\.eos \(still version 9\.0\.0\)
* check\_point\.mgmt \(still version 5\.2\.3\)
* chocolatey\.chocolatey \(still version 1\.5\.1\)
* cisco\.asa \(still version 5\.0\.1\)
* cisco\.dnac \(still version 6\.16\.0\)
* cisco\.intersight \(still version 2\.0\.9\)
* cisco\.ios \(still version 8\.0\.0\)
* cisco\.iosxr \(still version 9\.0\.0\)
* cisco\.ise \(still version 2\.9\.2\)
* cisco\.meraki \(still version 2\.18\.1\)
* cisco\.nxos \(still version 8\.1\.0\)
* cisco\.ucs \(still version 1\.10\.0\)
* cloud\.common \(still version 3\.0\.0\)
* cloudscale\_ch\.cloud \(still version 2\.3\.1\)
* community\.aws \(still version 8\.0\.0\)
* community\.ciscosmb \(still version 1\.0\.9\)
* community\.digitalocean \(still version 1\.26\.0\)
* community\.grafana \(still version 1\.9\.1\)
* community\.hashi\_vault \(still version 6\.2\.0\)
* community\.hrobot \(still version 2\.0\.1\)
* community\.library\_inventory\_filtering\_v1 \(still version 1\.0\.1\)
* community\.libvirt \(still version 1\.3\.0\)
* community\.mysql \(still version 3\.9\.0\)
* community\.network \(still version 5\.0\.3\)
* community\.okd \(still version 3\.0\.1\)
* community\.postgresql \(still version 3\.4\.1\)
* community\.rabbitmq \(still version 1\.3\.0\)
* community\.sap\_libs \(still version 1\.4\.2\)
* community\.windows \(still version 2\.2\.0\)
* community\.zabbix \(still version 2\.5\.1\)
* cyberark\.conjur \(still version 1\.3\.0\)
* cyberark\.pas \(still version 1\.0\.25\)
* dellemc\.enterprise\_sonic \(still version 2\.4\.0\)
* dellemc\.powerflex \(still version 2\.5\.0\)
* dellemc\.unity \(still version 2\.0\.0\)
* fortinet\.fortimanager \(still version 2\.5\.0\)
* frr\.frr \(still version 2\.0\.2\)
* google\.cloud \(still version 1\.3\.0\)
* hetzner\.hcloud \(still version 3\.1\.1\)
* ibm\.qradar \(still version 3\.0\.0\)
* ibm\.spectrum\_virtualize \(still version 2\.0\.0\)
* ieisystem\.inmanage \(still version 2\.0\.0\)
* infinidat\.infinibox \(still version 1\.4\.5\)
* infoblox\.nios\_modules \(still version 1\.6\.1\)
* inspur\.ispim \(still version 2\.2\.3\)
* inspur\.sm \(still version 2\.3\.0\)
* junipernetworks\.junos \(still version 8\.0\.0\)
* kaytus\.ksmanage \(still version 1\.2\.2\)
* kubernetes\.core \(still version 3\.2\.0\)
* lowlydba\.sqlserver \(still version 2\.3\.3\)
* microsoft\.ad \(still version 1\.6\.0\)
* netapp\.cloudmanager \(still version 21\.22\.1\)
* netapp\.ontap \(still version 22\.11\.0\)
* netapp\.storagegrid \(still version 21\.12\.0\)
* netapp\_eseries\.santricity \(still version 1\.4\.0\)
* netbox\.netbox \(still version 3\.19\.1\)
* ngine\_io\.cloudstack \(still version 2\.3\.0\)
* ngine\_io\.exoscale \(still version 1\.1\.0\)
* openstack\.cloud \(still version 2\.2\.0\)
* openvswitch\.openvswitch \(still version 2\.1\.1\)
* ovirt\.ovirt \(still version 3\.2\.0\)
* purestorage\.flashblade \(still version 1\.17\.0\)
* sensu\.sensu\_go \(still version 1\.14\.0\)
* splunk\.es \(still version 3\.0\.0\)
* t\_systems\_mms\.icinga\_director \(still version 2\.0\.1\)
* telekom\_mms\.icinga\_director \(still version 2\.1\.2\)
* theforeman\.foreman \(still version 4\.0\.0\)
* vmware\.vmware\_rest \(still version 3\.0\.1\)
* vultr\.cloud \(still version 1\.13\.0\)
* vyos\.vyos \(still version 4\.1\.0\)
* wti\.remote \(still version 1\.0\.5\)

<a id="v10-1-0"></a>
## v10\.1\.0

- <a href="#release-summary-6">Release Summary</a>
- <a href="#added-collections-1">Added Collections</a>
- <a href="#ansible-core-17">Ansible\-core</a>
- <a href="#changed-collections-6">Changed Collections</a>
- <a href="#major-changes-5">Major Changes</a>
    - <a href="#containers-podman-6">containers\.podman</a>
    - <a href="#dellemc-openmanage-18">dellemc\.openmanage</a>
- <a href="#minor-changes-6">Minor Changes</a>
    - <a href="#ansible-core-18">Ansible\-core</a>
    - <a href="#ansible-windows-2">ansible\.windows</a>
    - <a href="#cisco-dnac-5">cisco\.dnac</a>
    - <a href="#cisco-nxos">cisco\.nxos</a>
    - <a href="#community-general-17">community\.general</a>
    - <a href="#community-routeros-6">community\.routeros</a>
    - <a href="#community-zabbix">community\.zabbix</a>
    - <a href="#containers-podman-7">containers\.podman</a>
    - <a href="#dellemc-openmanage-19">dellemc\.openmanage</a>
    - <a href="#dellemc-powerflex">dellemc\.powerflex</a>
    - <a href="#kubernetes-core">kubernetes\.core</a>
    - <a href="#microsoft-ad-3">microsoft\.ad</a>
    - <a href="#netbox-netbox-3">netbox\.netbox</a>
    - <a href="#vultr-cloud">vultr\.cloud</a>
- <a href="#deprecated-features-6">Deprecated Features</a>
    - <a href="#community-general-18">community\.general</a>
- <a href="#bugfixes-6">Bugfixes</a>
    - <a href="#ansible-core-19">Ansible\-core</a>
    - <a href="#amazon-aws-4">amazon\.aws</a>
    - <a href="#ansible-netcommon">ansible\.netcommon</a>
    - <a href="#ansible-windows-3">ansible\.windows</a>
    - <a href="#cisco-ise-3">cisco\.ise</a>
    - <a href="#cisco-nxos-1">cisco\.nxos</a>
    - <a href="#community-dns-7">community\.dns</a>
    - <a href="#community-docker-10">community\.docker</a>
    - <a href="#community-general-19">community\.general</a>
    - <a href="#community-hrobot">community\.hrobot</a>
    - <a href="#community-network-1">community\.network</a>
    - <a href="#community-zabbix-1">community\.zabbix</a>
    - <a href="#containers-podman-8">containers\.podman</a>
    - <a href="#dellemc-openmanage-20">dellemc\.openmanage</a>
    - <a href="#inspur-ispim">inspur\.ispim</a>
    - <a href="#lowlydba-sqlserver-1">lowlydba\.sqlserver</a>
    - <a href="#microsoft-ad-4">microsoft\.ad</a>
    - <a href="#netbox-netbox-4">netbox\.netbox</a>
    - <a href="#purestorage-flasharray-9">purestorage\.flasharray</a>
- <a href="#known-issues-6">Known Issues</a>
    - <a href="#community-general-20">community\.general</a>
    - <a href="#dellemc-openmanage-21">dellemc\.openmanage</a>
- <a href="#new-plugins-2">New Plugins</a>
    - <a href="#filter-2">Filter</a>
- <a href="#new-modules-6">New Modules</a>
    - <a href="#community-general-21">community\.general</a>
    - <a href="#containers-podman-9">containers\.podman</a>
    - <a href="#dellemc-openmanage-22">dellemc\.openmanage</a>
- <a href="#unchanged-collections-6">Unchanged Collections</a>

<a id="release-summary-6"></a>
### Release Summary

Release Date\: 2024\-06\-18

[Porting Guide](https\://docs\.ansible\.com/ansible/devel/porting\_guides\.html)

<a id="added-collections-1"></a>
### Added Collections

* ieisystem\.inmanage \(version 2\.0\.0\)

<a id="ansible-core-17"></a>
### Ansible\-core

Ansible 10\.1\.0 contains ansible\-core version 2\.17\.1\.
This is a newer version than version 2\.17\.0 contained in the previous Ansible release\.

The changes are reported in the combined changelog below\.

<a id="changed-collections-6"></a>
### Changed Collections

If not mentioned explicitly\, the changes are reported in the combined changelog below\.

| Collection             | Ansible 10.0.1 | Ansible 10.1.0 | Notes                                                                                                                                                                                                        |
| ---------------------- | -------------- | -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| amazon.aws             | 8.0.0          | 8.0.1          |                                                                                                                                                                                                              |
| ansible.netcommon      | 6.1.2          | 6.1.3          |                                                                                                                                                                                                              |
| ansible.windows        | 2.3.0          | 2.4.0          |                                                                                                                                                                                                              |
| awx.awx                | 24.3.1         | 24.5.0         | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.                                                                                 |
| azure.azcollection     | 2.3.0          | 2.4.0          | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.                                                                                 |
| cisco.dnac             | 6.13.3         | 6.16.0         |                                                                                                                                                                                                              |
| cisco.ise              | 2.9.1          | 2.9.2          |                                                                                                                                                                                                              |
| cisco.nxos             | 8.0.0          | 8.1.0          |                                                                                                                                                                                                              |
| community.dns          | 3.0.0          | 3.0.1          |                                                                                                                                                                                                              |
| community.docker       | 3.10.3         | 3.10.4         |                                                                                                                                                                                                              |
| community.general      | 9.0.1          | 9.1.0          |                                                                                                                                                                                                              |
| community.hrobot       | 2.0.0          | 2.0.1          |                                                                                                                                                                                                              |
| community.network      | 5.0.2          | 5.0.3          |                                                                                                                                                                                                              |
| community.routeros     | 2.15.0         | 2.16.0         |                                                                                                                                                                                                              |
| community.zabbix       | 2.4.0          | 2.5.1          |                                                                                                                                                                                                              |
| containers.podman      | 1.13.0         | 1.15.2         |                                                                                                                                                                                                              |
| cyberark.conjur        | 1.2.2          | 1.3.0          | You can find the collection's changelog at [https://github.com/cyberark/ansible-conjur-collection/blob/master/CHANGELOG.md](https://github.com/cyberark/ansible-conjur-collection/blob/master/CHANGELOG.md). |
| dellemc.openmanage     | 9.2.0          | 9.3.0          |                                                                                                                                                                                                              |
| dellemc.powerflex      | 2.4.0          | 2.5.0          |                                                                                                                                                                                                              |
| ieisystem.inmanage     |                | 2.0.0          | The collection was added to Ansible                                                                                                                                                                          |
| inspur.ispim           | 2.2.2          | 2.2.3          |                                                                                                                                                                                                              |
| kubernetes.core        | 3.1.0          | 3.2.0          |                                                                                                                                                                                                              |
| lowlydba.sqlserver     | 2.3.2          | 2.3.3          |                                                                                                                                                                                                              |
| microsoft.ad           | 1.5.0          | 1.6.0          |                                                                                                                                                                                                              |
| netbox.netbox          | 3.18.0         | 3.19.1         |                                                                                                                                                                                                              |
| purestorage.flasharray | 1.28.0         | 1.28.1         |                                                                                                                                                                                                              |
| vultr.cloud            | 1.12.1         | 1.13.0         |                                                                                                                                                                                                              |

<a id="major-changes-5"></a>
### Major Changes

<a id="containers-podman-6"></a>
#### containers\.podman

* Add mount and unmount for volumes
* Add multiple subnets for networks
* Add new options for podman\_container
* Add new options to pod module
* Add podman search
* Improve idempotency for networking in podman\_container
* Redesign idempotency for Podman Pod module

<a id="dellemc-openmanage-18"></a>
#### dellemc\.openmanage

* Added support to use session ID for authentication of iDRAC\, OpenManage Enterprise and OpenManage Enterprise Modular\.
* ome\_session \- This module allows you to create and delete the sessions on OpenManage Enterprise and OpenManage Enterprise Modular\.

<a id="minor-changes-6"></a>
### Minor Changes

<a id="ansible-core-18"></a>
#### Ansible\-core

* ansible\-test \- Update <code>pypi\-test\-container</code> to version 3\.1\.0\.

<a id="ansible-windows-2"></a>
#### ansible\.windows

* win\_powershell \- Added the <code>sensitive\_parameters</code> option that can be used to pass in a SecureString or PSCredential parameter value\.
* win\_setup \- Added the <code>ansible\_win\_rm\_certificate\_thumbprint</code> fact to display the thumbprint of the certificate in use
* win\_user \- Added the ability to set an account expiration date using the <code>account\_expires</code> option \- [https\://github\.com/ansible\-collections/ansible\.windows/issues/610](https\://github\.com/ansible\-collections/ansible\.windows/issues/610)

<a id="cisco-dnac-5"></a>
#### cisco\.dnac

* Added API to validate the server address
* Added detailed documentation in network\_settings\_workflow\_manager\.py
* Added example playbooks in device\_provision\_workflow\.yml
* Added example playbooks in network\_compliance\_workflow\_manager\.py
* Added new attribute \'ise\_integration\_wait\_time\' in ise\_radius\_integration\_workflow\_manager\.py
* Added the code for creating/updating/deleting events subscription notification with specified destination and added the playbook and documentation with examples
* Changes in inventory and swim workflow manager modules\.
* Checking SNMP versions in events\_and\_notifications\_workflow\_manager\.py module
* Fix module name from network\_device\_config\_\_info to configuration\_archive\_details\_info\.
* Minor bug fixes in device\_credential\_workflow\_manager\.py module
* application\_policy\_application\_set \- new module
* application\_policy\_application\_set\_count\_info \- new module
* application\_policy\_application\_set\_info \- new module
* applications\_count\_v2\_info \- new module
* applications\_v2 \- new module
* applications\_v2\_info \- new module
* auth\_token\_create \- new module
* authentication\_policy\_servers \- new module
* device\_configs\_backup\_workflow\_manager \- New workflow manager module for device configuration backup functions\.
* device\_credential\_workflow\_manager \- Updated the log messages\.
* device\_reboot\_apreboot \- new module
* dna\_event\_snmp\_config\_info \- new module
* event\_snmp\_config \- new module
* event\_webhook\_read\_info \- new module
* events\_and\_notifications\_workflow\_manager \- New workflow manager for configuring various types of destinations\(Webhook\, Email\, Syslog\, SNMP\, ITSM\) to deliver event notifications\.
* events\_and\_notifications\_workflow\_manager\.py \- Added attributes \'webhook\_event\_notification\'\, \'email\_event\_notification\'\, \'syslog\_event\_notification\'
* flexible\_report\_content\_info \- new module
* flexible\_report\_execute \- new module
* flexible\_report\_executions\_info \- new module
* flexible\_report\_schedule  \- new module
* flexible\_report\_schedule\_info \- new module
* integration\_settings\_itsm\_instances\_info \- new module
* integration\_settings\_status\_info \- new module
* inventory\_workflow\_manager \- Updated changes related to provisioning devices\.
* ise\_integration\_status\_info \- new module
* ise\_radius\_integration\_workflow\_manager \- New workflow manager for Authentication and Policy Servers\(ISE/AAA\)\.
* ise\_radius\_integration\_workflow\_manager \- Removed the attributes \'port\' and \'subscriber\_name\'\. Added the attribute \'ise\_integration\_wait\_time\'\.
* lan\_automation\_sessions\_info \- new module
* lan\_automation\_update \- new module
* lan\_automation\_update\_device \- new module
* lan\_automation\_update\_v2 \- new module
* lan\_automation\_v2 \- new module
* network\_compliance\_workflow\_manager \- New workflow manager for Network Compliance module for managing network compliance tasks on reachable device\(s\)\.
* network\_device\_user\_defined\_field\_delete \- new module
* network\_settings\_workflow\_manager \- Added attributes \'ipv4\_global\_pool\_name\'\.
* provision\_workflow\_manager \- Updated changes related to handle errors\.
* provision\_workflow\_manager\.py \- Added attribute \'provisioning\'
* site\_workflow\_manager \- Updated changes in Site updation\.
* template\_workflow\_manager \- Removed attributes \'create\_time\'\, \'failure\_policy\'\, \'last\_update\_time\'\, \'latest\_version\_time\'\, \'parent\_template\_id\'\, \'project\_id\'\, \'validation\_errors\'\, \'rollback\_template\_params\' and \'rollback\_template\_content\'\.
* template\_workflow\_manager\.py \- Added attributes \'choices\'\, \'failure\_policy\'
* users\_external\_authentication \- new module
* users\_external\_servers\_aaa\_attribute \- new module

<a id="cisco-nxos"></a>
#### cisco\.nxos

* route\_maps \- support simple route\-maps that do not contain set or match statements\. it allows for the creation and management of purely basic route\-map entries like \'route\-map test\-1 permit 10\'\.

<a id="community-general-17"></a>
#### community\.general

* CmdRunner module util \- argument formats can be specified as plain functions without calling <code>cmd\_runner\_fmt\.as\_func\(\)</code> \([https\://github\.com/ansible\-collections/community\.general/pull/8479](https\://github\.com/ansible\-collections/community\.general/pull/8479)\)\.
* ansible\_galaxy\_install \- add upgrade feature \([https\://github\.com/ansible\-collections/community\.general/pull/8431](https\://github\.com/ansible\-collections/community\.general/pull/8431)\, [https\://github\.com/ansible\-collections/community\.general/issues/8351](https\://github\.com/ansible\-collections/community\.general/issues/8351)\)\.
* cargo \- add option <code>directory</code>\, which allows source directory to be specified \([https\://github\.com/ansible\-collections/community\.general/pull/8480](https\://github\.com/ansible\-collections/community\.general/pull/8480)\)\.
* cmd\_runner module utils \- add decorator <code>cmd\_runner\_fmt\.stack</code> \([https\://github\.com/ansible\-collections/community\.general/pull/8415](https\://github\.com/ansible\-collections/community\.general/pull/8415)\)\.
* cmd\_runner\_fmt module utils \- simplify implementation of <code>cmd\_runner\_fmt\.as\_bool\_not\(\)</code> \([https\://github\.com/ansible\-collections/community\.general/pull/8512](https\://github\.com/ansible\-collections/community\.general/pull/8512)\)\.
* ipa\_dnsrecord \- adds <code>SSHFP</code> record type for managing SSH fingerprints in FreeIPA DNS \([https\://github\.com/ansible\-collections/community\.general/pull/8404](https\://github\.com/ansible\-collections/community\.general/pull/8404)\)\.
* keycloak\_client \- assign auth flow by name \([https\://github\.com/ansible\-collections/community\.general/pull/8428](https\://github\.com/ansible\-collections/community\.general/pull/8428)\)\.
* openbsd\_pkg \- adds diff support to show changes in installed package list\. This does not yet work for check mode \([https\://github\.com/ansible\-collections/community\.general/pull/8402](https\://github\.com/ansible\-collections/community\.general/pull/8402)\)\.
* proxmox \- allow specification of the API port when using proxmox\_\* \([https\://github\.com/ansible\-collections/community\.general/issues/8440](https\://github\.com/ansible\-collections/community\.general/issues/8440)\, [https\://github\.com/ansible\-collections/community\.general/pull/8441](https\://github\.com/ansible\-collections/community\.general/pull/8441)\)\.
* proxmox\_vm\_info \- add <code>network</code> option to retrieve current network information \([https\://github\.com/ansible\-collections/community\.general/pull/8471](https\://github\.com/ansible\-collections/community\.general/pull/8471)\)\.
* redfish\_command \- add <code>wait</code> and <code>wait\_timeout</code> options to allow a user to block a command until a service is accessible after performing the requested command \([https\://github\.com/ansible\-collections/community\.general/issues/8051](https\://github\.com/ansible\-collections/community\.general/issues/8051)\, [https\://github\.com/ansible\-collections/community\.general/pull/8434](https\://github\.com/ansible\-collections/community\.general/pull/8434)\)\.
* redfish\_info \- add command <code>CheckAvailability</code> to check if a service is accessible \([https\://github\.com/ansible\-collections/community\.general/issues/8051](https\://github\.com/ansible\-collections/community\.general/issues/8051)\, [https\://github\.com/ansible\-collections/community\.general/pull/8434](https\://github\.com/ansible\-collections/community\.general/pull/8434)\)\.
* redis\_info \- adds support for getting cluster info \([https\://github\.com/ansible\-collections/community\.general/pull/8464](https\://github\.com/ansible\-collections/community\.general/pull/8464)\)\.

<a id="community-routeros-6"></a>
#### community\.routeros

* api\_info\, api\_modify \- add missing path <code>/ppp secret</code> \([https\://github\.com/ansible\-collections/community\.routeros/pull/286](https\://github\.com/ansible\-collections/community\.routeros/pull/286)\)\.
* api\_info\, api\_modify \- minor changes <code>/interface ethernet</code> path fields \([https\://github\.com/ansible\-collections/community\.routeros/pull/288](https\://github\.com/ansible\-collections/community\.routeros/pull/288)\)\.

<a id="community-zabbix"></a>
#### community\.zabbix

* agent role \- Standardized all configuration variables using the <em class="title-reference">zabbix\_agent</em> prefix vs <em class="title-reference">zabbix\_agent2</em>\.  Support for <em class="title-reference">zabbix\_agent2</em> to be removed in 3\.0\.0
* agent role \- Standardized templating of agent\.conf file
* all roles \- Added support for Ubuntu 24\.04 \(Noble Numbat\)
* zabbix\_discoveryrule module added
* zabbix\_host\_events\_update module added
* zabbix\_item \- add support for setting master items by name
* zabbix\_item module added
* zabbix\_itemprototype \- add support for setting master items by name
* zabbix\_itemprototype module added
* zabbix\_trigger module added
* zabbix\_triggerprototype module added

<a id="containers-podman-7"></a>
#### containers\.podman

* Add autodiscovery for build context in podman\_image
* Add docs\, tests and more examples for podman\_pod
* Add extra\_args for podman\_image push and pull
* Add idempotency for mounts and volumes in podman\_container
* Add new functionality tests for podman\_secret
* Add option for inline Containerfile in podman\_image
* Add path and env options for podman\_secret
* Add route\, dns and ipam\_driver to podman\_network
* Create podman secret when skip\_existing\=True and it does not exist

<a id="dellemc-openmanage-19"></a>
#### dellemc\.openmanage

* Added support for Python 3\.12\.
* Added time\_to\_wait option in <code>idrac\_storage\_volume</code> module\.

<a id="dellemc-powerflex"></a>
#### dellemc\.powerflex

* Added support for PowerFlex Onyx version\(4\.6\.x\)\.
* Fixed the roles to support attaching the MDM cluster to the gateway\.
* The storage pool module has been enhanced to support more features\.

<a id="kubernetes-core"></a>
#### kubernetes\.core

* connection/kubectl\.py \- Added an example of using the kubectl connection plugin to the documentation \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/741](https\://github\.com/ansible\-collections/kubernetes\.core/pull/741)\)\.
* inventory/k8s\.py \- Defer removal of k8s inventory plugin to version 6\.0\.0 \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/734](https\://github\.com/ansible\-collections/kubernetes\.core/pull/734)\)\.

<a id="microsoft-ad-3"></a>
#### microsoft\.ad

* microsoft\.ad AD modules \- Added <code>domain\_credentials</code> as a common module option that can be used to specify credentials for specific AD servers\.
* microsoft\.ad AD modules \- Added <code>lookup\_failure\_action</code> on all modules that can specify a list of distinguishedName values to control what should happen if the lookup fails\.
* microsoft\.ad\.computer \- Added the ability to lookup a distinguishedName on a specific domain server for <code>delegates</code> and <code>managed\_by</code>\.
* microsoft\.ad\.group \- Added the ability to lookup a distinguishedName on a specific domain server for <code>managed\_by</code> and <code>members</code>\.
* microsoft\.ad\.ou \- Added the ability to lookup a distinguishedName on a specific domain server for <code>managed\_by</code>\.
* microsoft\.ad\.user \- Added the ability to lookup a distinguishedName on a specific domain server for <code>delegates</code>\.
* microsoft\.ad\.user \- Rename the option <code>groups\.missing\_action</code> to <code>groups\.lookup\_failure\_action</code> to make the option more consistent with other modules\. The <code>missing\_action</code> option is still supported as an alias\.
* microsoft\.ad\.user \- Support group member lookup on alternative server using the DN lookup syntax\. This syntax uses a dictionary where <code>name</code> defined the group to lookup and <code>server</code> defines the server to lookup the group on\.

<a id="netbox-netbox-3"></a>
#### netbox\.netbox

* Add cluster host to dynamic inventory response [\#1219](https\://github\.com/netbox\-community/ansible\_modules/pull/1219)
* Add galaxy\-importer to CI process [\#1245](https\://github\.com/netbox\-community/ansible\_modules/issues/1245)
* Adjust modules to support NetBox v4\.0\.0 [\#1234](https\://github\.com/netbox\-community/ansible\_modules/pull/1234)
* Bump jinja2 from 3\.1\.2 to 3\.1\.4 [\#1226](https\://github\.com/netbox\-community/ansible\_modules/pull/1226)
* Bump requests from 2\.31\.0 to 2\.32\.0 [\#1236](https\://github\.com/netbox\-community/ansible\_modules/pull/1236)
* Bump version 3\.19\.1
* Drop obsolete Ansible and Python versions and fix tests [\#1241](https\://github\.com/netbox\-community/ansible\_modules/issues/1241)
* Get ansible\-lint passing again \(sequence after [\#1241](https\://github\.com/netbox\-community/ansible\_modules/issues/1241)\) [\#1243](https\://github\.com/netbox\-community/ansible\_modules/issues/1243)
* Update CI process to follow Ansible Collection Standards [\#1247](https\://github\.com/netbox\-community/ansible\_modules/issues/1247)
* Update CI to use master instead of main\. [\#1253](https\://github\.com/netbox\-community/ansible\_modules/issues/1253)
* Update ansible\-lint to ignore changelog file for yaml indentation\. [\#1256](https\://github\.com/netbox\-community/ansible\_modules/issues/1256)
* Update top\-level README with new minimum Ansible version \(sequence after [\#1241](https\://github\.com/netbox\-community/ansible\_modules/issues/1241) [\#1244](https\://github\.com/netbox\-community/ansible\_modules/issues/1244)
* Updated CI to only run changelog job if PR into devel branch is detected\. [\#1251](https\://github\.com/netbox\-community/ansible\_modules/issues/1251)
* Updated CI to support NetBox 4\.0 [\#1230](https\://github\.com/netbox\-community/ansible\_modules/pull/1230)
* Updates to top\-level README\.md to align collection with Ansible best practices [\#1238](https\://github\.com/netbox\-community/ansible\_modules/issues/1238)

<a id="vultr-cloud"></a>
#### vultr\.cloud

* instance\, bare\_metal \- Implemented a new option <code>skip\_wait</code> \([https\://github\.com/vultr/ansible\-collection\-vultr/issues/119](https\://github\.com/vultr/ansible\-collection\-vultr/issues/119)\)\.

<a id="deprecated-features-6"></a>
### Deprecated Features

<a id="community-general-18"></a>
#### community\.general

* CmdRunner module util \- setting the value of the <code>ignore\_none</code> parameter within a <code>CmdRunner</code> context is deprecated and that feature should be removed in community\.general 12\.0\.0 \([https\://github\.com/ansible\-collections/community\.general/pull/8479](https\://github\.com/ansible\-collections/community\.general/pull/8479)\)\.
* git\_config \- the <code>list\_all</code> option has been deprecated and will be removed in community\.general 11\.0\.0\. Use the <code>community\.general\.git\_config\_info</code> module instead \([https\://github\.com/ansible\-collections/community\.general/pull/8453](https\://github\.com/ansible\-collections/community\.general/pull/8453)\)\.
* git\_config \- using <code>state\=present</code> without providing <code>value</code> is deprecated and will be disallowed in community\.general 11\.0\.0\. Use the <code>community\.general\.git\_config\_info</code> module instead to read a value \([https\://github\.com/ansible\-collections/community\.general/pull/8453](https\://github\.com/ansible\-collections/community\.general/pull/8453)\)\.

<a id="bugfixes-6"></a>
### Bugfixes

<a id="ansible-core-19"></a>
#### Ansible\-core

* Fix rapid memory usage growth when notifying handlers using the <code>listen</code> keyword \([https\://github\.com/ansible/ansible/issues/83392](https\://github\.com/ansible/ansible/issues/83392)\)
* Fix the task attribute <code>resolved\_action</code> to show the FQCN instead of <code>None</code> when <code>action</code> or <code>local\_action</code> is used in the playbook\.
* Fix using <code>module\_defaults</code> with <code>local\_action</code>/<code>action</code> \([https\://github\.com/ansible/ansible/issues/81905](https\://github\.com/ansible/ansible/issues/81905)\)\.
* fixed unit test test\_borken\_cowsay to address mock not been properly applied when existing unix system already have cowsay installed\.
* powershell \- Implement more robust deletion mechanism for C\# code compilation temporary files\. This should avoid scenarios where the underlying temporary directory may be temporarily locked by antivirus tools or other IO problems\. A failure to delete one of these temporary directories will result in a warning rather than an outright failure\.
* shell plugin \- properly quote all needed components of shell commands \([https\://github\.com/ansible/ansible/issues/82535](https\://github\.com/ansible/ansible/issues/82535)\)

<a id="amazon-aws-4"></a>
#### amazon\.aws

* backup\_plan\_info \- Bugfix to enable getting info of all backup plans \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2083](https\://github\.com/ansible\-collections/amazon\.aws/pull/2083)\)\.
* ec2\_instance \- do not ignore IPv6 addresses when a single network interface is specified \([https\://github\.com/ansible\-collections/amazon\.aws/pull/1979](https\://github\.com/ansible\-collections/amazon\.aws/pull/1979)\)\.
* s3\_object \- fixed issue which was causing <code>MemoryError</code> exceptions when downloading large files \([https\://github\.com/ansible\-collections/amazon\.aws/issues/2107](https\://github\.com/ansible\-collections/amazon\.aws/issues/2107)\)\.

<a id="ansible-netcommon"></a>
#### ansible\.netcommon

* The v6\.1\.2 release introduced a change in cliconfbase\'s edit\_config\(\) signature which broke many platform cliconfs\. This patch release reverts that change\.

<a id="ansible-windows-3"></a>
#### ansible\.windows

* setup \- Provide WMI/CIM fallback for facts that rely on SMBIOS when that is unavailable

<a id="cisco-ise-3"></a>
#### cisco\.ise

* Added main\.yml to aws\_deployment role
* Update min\_ansible\_version to 2\.15\.0 in runtime\.yml and roles

<a id="cisco-nxos-1"></a>
#### cisco\.nxos

* nxos\_l3\_interfaces \- fail if encapsulation exists on a different sub\-interface\.
* nxos\_static\_routes \- correctly generate command when track parameter is specified\.

<a id="community-dns-7"></a>
#### community\.dns

* Update Public Suffix List\.

<a id="community-docker-10"></a>
#### community\.docker

* docker\_compose \- make sure that the module uses the <code>api\_version</code> parameter \([https\://github\.com/ansible\-collections/community\.docker/pull/881](https\://github\.com/ansible\-collections/community\.docker/pull/881)\)\.
* docker\_compose\_v2\* modules \- there was no check to make sure that one of <code>project\_src</code> and <code>definition</code> is provided\. The modules crashed if none were provided \([https\://github\.com/ansible\-collections/community\.docker/issues/885](https\://github\.com/ansible\-collections/community\.docker/issues/885)\, [https\://github\.com/ansible\-collections/community\.docker/pull/886](https\://github\.com/ansible\-collections/community\.docker/pull/886)\)\.

<a id="community-general-19"></a>
#### community\.general

* git\_config \- fix behavior of <code>state\=absent</code> if <code>value</code> is present \([https\://github\.com/ansible\-collections/community\.general/issues/8436](https\://github\.com/ansible\-collections/community\.general/issues/8436)\, [https\://github\.com/ansible\-collections/community\.general/pull/8452](https\://github\.com/ansible\-collections/community\.general/pull/8452)\)\.
* keycloak\_realm \- add normalizations for <code>attributes</code> and <code>protocol\_mappers</code> \([https\://github\.com/ansible\-collections/community\.general/pull/8496](https\://github\.com/ansible\-collections/community\.general/pull/8496)\)\.
* launched \- correctly report changed status in check mode \([https\://github\.com/ansible\-collections/community\.general/pull/8406](https\://github\.com/ansible\-collections/community\.general/pull/8406)\)\.
* opennebula inventory plugin \- fix invalid reference to IP when inventory runs against NICs with no IPv4 address \([https\://github\.com/ansible\-collections/community\.general/pull/8489](https\://github\.com/ansible\-collections/community\.general/pull/8489)\)\.
* opentelemetry callback \- do not save the JSON response when using the <code>ansible\.builtin\.uri</code> module \([https\://github\.com/ansible\-collections/community\.general/pull/8430](https\://github\.com/ansible\-collections/community\.general/pull/8430)\)\.
* opentelemetry callback \- do not save the content response when using the <code>ansible\.builtin\.slurp</code> module \([https\://github\.com/ansible\-collections/community\.general/pull/8430](https\://github\.com/ansible\-collections/community\.general/pull/8430)\)\.
* paman \- do not fail if an empty list of packages has been provided and there is nothing to do \([https\://github\.com/ansible\-collections/community\.general/pull/8514](https\://github\.com/ansible\-collections/community\.general/pull/8514)\)\.

<a id="community-hrobot"></a>
#### community\.hrobot

* boot \- use PHP array form encoding when sending multiple <code>authorized\_key</code> \([https\://github\.com/ansible\-collections/community\.hrobot/issues/112](https\://github\.com/ansible\-collections/community\.hrobot/issues/112)\, [https\://github\.com/ansible\-collections/community\.hrobot/pull/113](https\://github\.com/ansible\-collections/community\.hrobot/pull/113)\)\.

<a id="community-network-1"></a>
#### community\.network

* exos \- Add error handling of <code>Permission denied</code> errors \([https\://github\.com/ansible\-collections/community\.network/pull/571](https\://github\.com/ansible\-collections/community\.network/pull/571)\)\.

<a id="community-zabbix-1"></a>
#### community\.zabbix

* zabbix\_agent \- Fix reading existing psk
* zabbix\_agent \- Fix role when zabbix\_agent\_listenip is undefined
* zabbix\_web \- make the FPM socket group\-writable so the web server can properly forward requests to the FPM process

<a id="containers-podman-8"></a>
#### containers\.podman

* Fix idempotency for pod with 0\.0\.0\.0
* Fix idempotency for pods in case of systemd generation
* Fix idempotency for systemd generations
* Fix issue with pushing podman image to repo name and org
* Fix transports issues in podman\_image
* fix\(\#747\) set correct HealthCmd

<a id="dellemc-openmanage-20"></a>
#### dellemc\.openmanage

* Resolved the issue in <code>idrac\_certificates</code> module where subject\_alt\_name parameter was only accepting first item in list\. \([https\://github\.com/dell/dellemc\-openmanage\-ansible\-modules/issues/584](https\://github\.com/dell/dellemc\-openmanage\-ansible\-modules/issues/584)\)
* Resolved the issue in <code>idrac\_virtual\_media</code> module where the Authorization request header was included in the request\. \([https\://github\.com/dell/dellemc\-openmanage\-ansible\-modules/issues/612](https\://github\.com/dell/dellemc\-openmanage\-ansible\-modules/issues/612)\)
* Resolved the issue in <code>ome\_application\_certificate</code> module related to a padding error in generated CSR file\. \([https\://github\.com/dell/dellemc\-openmanage\-ansible\-modules/issues/370](https\://github\.com/dell/dellemc\-openmanage\-ansible\-modules/issues/370)\)

<a id="inspur-ispim"></a>
#### inspur\.ispim

* Change the ansible version in meta/runtime\.yml to 2\.15\.0\([https\://github\.com/ispim/inspur\.ispim/pull/37](https\://github\.com/ispim/inspur\.ispim/pull/37)\)\.

<a id="lowlydba-sqlserver-1"></a>
#### lowlydba\.sqlserver

* fixed the expected type of the ip\_address\, subnet\_ip\, and subnet\_mask parameters to be lists instead of strings \(lowlydba\.sqlserver\.ag\_listener\)

<a id="microsoft-ad-4"></a>
#### microsoft\.ad

* microsoft\.ad\.membership \- Fix hostname check to work with hostnames longer than 15 characters long \- [https\://github\.com/ansible\-collections/microsoft\.ad/issues/113](https\://github\.com/ansible\-collections/microsoft\.ad/issues/113)
* microsoft\.ad\.user \- Fix issue when creating a new user account with <code>account\_locked\: false</code> \- [https\://github\.com/ansible\-collections/microsoft\.ad/issues/108](https\://github\.com/ansible\-collections/microsoft\.ad/issues/108)

<a id="netbox-netbox-4"></a>
#### netbox\.netbox

* Added ALLOWED\_QUERY\_PARAMS module\_bay by device [\#1228](https\://github\.com/netbox\-community/ansible\_modules/pull/1228)
* Added label to power outlet [\#1222](https\://github\.com/netbox\-community/ansible\_modules/pull/1222)
* Added power outlet type iec\-60320\-c21 to power outlet template and power outlet modules [\#1229](https\://github\.com/netbox\-community/ansible\_modules/issues/1229)
* Extend query param for parent\_location [\#1233](https\://github\.com/netbox\-community/ansible\_modules/issues/1233)

<a id="purestorage-flasharray-9"></a>
#### purestorage\.flasharray

* purefa\_network \- Fix issue with clearing network interface addresses
* purefa\_network \- Resolve issue when setting a network port on a new array
* purefa\_policy \- Enhanced idempotency for snapshot policy rules

<a id="known-issues-6"></a>
### Known Issues

<a id="community-general-20"></a>
#### community\.general

* homectl \- the module does not work under Python 3\.13 or newer\, since it relies on the removed <code>crypt</code> standard library module \([https\://github\.com/ansible\-collections/community\.general/issues/4691](https\://github\.com/ansible\-collections/community\.general/issues/4691)\, [https\://github\.com/ansible\-collections/community\.general/pull/8497](https\://github\.com/ansible\-collections/community\.general/pull/8497)\)\.
* udm\_user \- the module does not work under Python 3\.13 or newer\, since it relies on the removed <code>crypt</code> standard library module \([https\://github\.com/ansible\-collections/community\.general/issues/4690](https\://github\.com/ansible\-collections/community\.general/issues/4690)\, [https\://github\.com/ansible\-collections/community\.general/pull/8497](https\://github\.com/ansible\-collections/community\.general/pull/8497)\)\.

<a id="dellemc-openmanage-21"></a>
#### dellemc\.openmanage

* idrac\_diagnostics \- Issue\(285322\) \- This module doesn\'t support export of diagnostics file to HTTP and HTTPS share via SOCKS proxy\.
* idrac\_firmware \- Issue\(279282\) \- This module does not support firmware update using HTTP\, HTTPS\, and FTP shares with authentication on iDRAC8\.
* idrac\_storage\_volume \- Issue\(290766\) \- The module will report success instead of showing failure for new virtual creation on the BOSS\-N1 controller if a virtual disk is already present on the same controller\.
* ome\_diagnostics \- Issue\(279193\) \- Export of SupportAssist collection logs to the share location fails on OME version 4\.0\.0\.
* ome\_smart\_fabric\_uplink \- Issue\(186024\) \- The module supported by OpenManage Enterprise Modular\, however it does not allow the creation of multiple uplinks of the same name\. If an uplink is created using the same name as an existing uplink\, then the existing uplink is modified\.

<a id="new-plugins-2"></a>
### New Plugins

<a id="filter-2"></a>
#### Filter

* community\.general\.keep\_keys \- Keep specific keys from dictionaries in a list\.
* community\.general\.remove\_keys \- Remove specific keys from dictionaries in a list\.
* community\.general\.replace\_keys \- Replace specific keys in a list of dictionaries\.

<a id="new-modules-6"></a>
### New Modules

<a id="community-general-21"></a>
#### community\.general

* community\.general\.consul\_agent\_check \- Add\, modify\, and delete checks within a consul cluster\.
* community\.general\.consul\_agent\_service \- Add\, modify and delete services within a consul cluster\.
* community\.general\.django\_check \- Wrapper for C\(django\-admin check\)\.
* community\.general\.django\_createcachetable \- Wrapper for C\(django\-admin createcachetable\)\.

<a id="containers-podman-9"></a>
#### containers\.podman

* containers\.podman\.podman\_search \- Search for remote images using podman

<a id="dellemc-openmanage-22"></a>
#### dellemc\.openmanage

* dellemc\.openmanage\.ome\_session \- This module allows you to create and delete sessions on OpenManage Enterprise and OpenManage Enterprise Modular\.

<a id="unchanged-collections-6"></a>
### Unchanged Collections

* ansible\.posix \(still version 1\.5\.4\)
* ansible\.utils \(still version 4\.1\.0\)
* arista\.eos \(still version 9\.0\.0\)
* check\_point\.mgmt \(still version 5\.2\.3\)
* chocolatey\.chocolatey \(still version 1\.5\.1\)
* cisco\.aci \(still version 2\.9\.0\)
* cisco\.asa \(still version 5\.0\.1\)
* cisco\.intersight \(still version 2\.0\.9\)
* cisco\.ios \(still version 8\.0\.0\)
* cisco\.iosxr \(still version 9\.0\.0\)
* cisco\.meraki \(still version 2\.18\.1\)
* cisco\.mso \(still version 2\.6\.0\)
* cisco\.ucs \(still version 1\.10\.0\)
* cloud\.common \(still version 3\.0\.0\)
* cloudscale\_ch\.cloud \(still version 2\.3\.1\)
* community\.aws \(still version 8\.0\.0\)
* community\.ciscosmb \(still version 1\.0\.9\)
* community\.crypto \(still version 2\.20\.0\)
* community\.digitalocean \(still version 1\.26\.0\)
* community\.grafana \(still version 1\.9\.1\)
* community\.hashi\_vault \(still version 6\.2\.0\)
* community\.library\_inventory\_filtering\_v1 \(still version 1\.0\.1\)
* community\.libvirt \(still version 1\.3\.0\)
* community\.mongodb \(still version 1\.7\.4\)
* community\.mysql \(still version 3\.9\.0\)
* community\.okd \(still version 3\.0\.1\)
* community\.postgresql \(still version 3\.4\.1\)
* community\.proxysql \(still version 1\.5\.1\)
* community\.rabbitmq \(still version 1\.3\.0\)
* community\.sap\_libs \(still version 1\.4\.2\)
* community\.sops \(still version 1\.6\.7\)
* community\.vmware \(still version 4\.4\.0\)
* community\.windows \(still version 2\.2\.0\)
* cyberark\.pas \(still version 1\.0\.25\)
* dellemc\.enterprise\_sonic \(still version 2\.4\.0\)
* dellemc\.unity \(still version 2\.0\.0\)
* f5networks\.f5\_modules \(still version 1\.28\.0\)
* fortinet\.fortimanager \(still version 2\.5\.0\)
* fortinet\.fortios \(still version 2\.3\.6\)
* frr\.frr \(still version 2\.0\.2\)
* google\.cloud \(still version 1\.3\.0\)
* grafana\.grafana \(still version 5\.2\.0\)
* hetzner\.hcloud \(still version 3\.1\.1\)
* ibm\.qradar \(still version 3\.0\.0\)
* ibm\.spectrum\_virtualize \(still version 2\.0\.0\)
* ibm\.storage\_virtualize \(still version 2\.3\.1\)
* infinidat\.infinibox \(still version 1\.4\.5\)
* infoblox\.nios\_modules \(still version 1\.6\.1\)
* inspur\.sm \(still version 2\.3\.0\)
* junipernetworks\.junos \(still version 8\.0\.0\)
* kaytus\.ksmanage \(still version 1\.2\.2\)
* netapp\.cloudmanager \(still version 21\.22\.1\)
* netapp\.ontap \(still version 22\.11\.0\)
* netapp\.storagegrid \(still version 21\.12\.0\)
* netapp\_eseries\.santricity \(still version 1\.4\.0\)
* ngine\_io\.cloudstack \(still version 2\.3\.0\)
* ngine\_io\.exoscale \(still version 1\.1\.0\)
* openstack\.cloud \(still version 2\.2\.0\)
* openvswitch\.openvswitch \(still version 2\.1\.1\)
* ovirt\.ovirt \(still version 3\.2\.0\)
* purestorage\.flashblade \(still version 1\.17\.0\)
* sensu\.sensu\_go \(still version 1\.14\.0\)
* splunk\.es \(still version 3\.0\.0\)
* t\_systems\_mms\.icinga\_director \(still version 2\.0\.1\)
* telekom\_mms\.icinga\_director \(still version 2\.1\.2\)
* theforeman\.foreman \(still version 4\.0\.0\)
* vmware\.vmware\_rest \(still version 3\.0\.1\)
* vyos\.vyos \(still version 4\.1\.0\)
* wti\.remote \(still version 1\.0\.5\)

<a id="v10-0-1"></a>
## v10\.0\.1

- <a href="#release-summary-7">Release Summary</a>
- <a href="#ansible-core-20">Ansible\-core</a>
- <a href="#changed-collections-7">Changed Collections</a>
- <a href="#bugfixes-7">Bugfixes</a>
    - <a href="#inspur-ispim-1">inspur\.ispim</a>
    - <a href="#kaytus-ksmanage">kaytus\.ksmanage</a>
- <a href="#unchanged-collections-7">Unchanged Collections</a>

<a id="release-summary-7"></a>
### Release Summary

Release Date\: 2024\-06\-06

[Porting Guide](https\://docs\.ansible\.com/ansible/devel/porting\_guides\.html)

This release updates 10\.0\.0 by removing binary files from a Windows venv that accidentally were included in two collection releases\.

<a id="ansible-core-20"></a>
### Ansible\-core

Ansible 10\.0\.1 contains ansible\-core version 2\.17\.0\.
This is the same version of ansible\-core as in the previous Ansible release\.

<a id="changed-collections-7"></a>
### Changed Collections

If not mentioned explicitly\, the changes are reported in the combined changelog below\.

| Collection      | Ansible 10.0.0 | Ansible 10.0.1 | Notes |
| --------------- | -------------- | -------------- | ----- |
| inspur.ispim    | 2.2.1          | 2.2.2          |       |
| kaytus.ksmanage | 1.2.1          | 1.2.2          |       |

<a id="bugfixes-7"></a>
### Bugfixes

<a id="inspur-ispim-1"></a>
#### inspur\.ispim

* Remove venv files that were accidentally bundled in 2\.2\.1 \([https\://github\.com/ispim/inspur\.ispim/pull/35](https\://github\.com/ispim/inspur\.ispim/pull/35)\)\.

<a id="kaytus-ksmanage"></a>
#### kaytus\.ksmanage

* Remove venv files that were accidentally bundled in 1\.2\.2\([https\://github\.com/ieisystem/kaytus\.ksmanage/pull/23](https\://github\.com/ieisystem/kaytus\.ksmanage/pull/23)\)\.

<a id="unchanged-collections-7"></a>
### Unchanged Collections

* amazon\.aws \(still version 8\.0\.0\)
* ansible\.netcommon \(still version 6\.1\.2\)
* ansible\.posix \(still version 1\.5\.4\)
* ansible\.utils \(still version 4\.1\.0\)
* ansible\.windows \(still version 2\.3\.0\)
* arista\.eos \(still version 9\.0\.0\)
* awx\.awx \(still version 24\.3\.1\)
* azure\.azcollection \(still version 2\.3\.0\)
* check\_point\.mgmt \(still version 5\.2\.3\)
* chocolatey\.chocolatey \(still version 1\.5\.1\)
* cisco\.aci \(still version 2\.9\.0\)
* cisco\.asa \(still version 5\.0\.1\)
* cisco\.dnac \(still version 6\.13\.3\)
* cisco\.intersight \(still version 2\.0\.9\)
* cisco\.ios \(still version 8\.0\.0\)
* cisco\.iosxr \(still version 9\.0\.0\)
* cisco\.ise \(still version 2\.9\.1\)
* cisco\.meraki \(still version 2\.18\.1\)
* cisco\.mso \(still version 2\.6\.0\)
* cisco\.nxos \(still version 8\.0\.0\)
* cisco\.ucs \(still version 1\.10\.0\)
* cloud\.common \(still version 3\.0\.0\)
* cloudscale\_ch\.cloud \(still version 2\.3\.1\)
* community\.aws \(still version 8\.0\.0\)
* community\.ciscosmb \(still version 1\.0\.9\)
* community\.crypto \(still version 2\.20\.0\)
* community\.digitalocean \(still version 1\.26\.0\)
* community\.dns \(still version 3\.0\.0\)
* community\.docker \(still version 3\.10\.3\)
* community\.general \(still version 9\.0\.1\)
* community\.grafana \(still version 1\.9\.1\)
* community\.hashi\_vault \(still version 6\.2\.0\)
* community\.hrobot \(still version 2\.0\.0\)
* community\.library\_inventory\_filtering\_v1 \(still version 1\.0\.1\)
* community\.libvirt \(still version 1\.3\.0\)
* community\.mongodb \(still version 1\.7\.4\)
* community\.mysql \(still version 3\.9\.0\)
* community\.network \(still version 5\.0\.2\)
* community\.okd \(still version 3\.0\.1\)
* community\.postgresql \(still version 3\.4\.1\)
* community\.proxysql \(still version 1\.5\.1\)
* community\.rabbitmq \(still version 1\.3\.0\)
* community\.routeros \(still version 2\.15\.0\)
* community\.sap\_libs \(still version 1\.4\.2\)
* community\.sops \(still version 1\.6\.7\)
* community\.vmware \(still version 4\.4\.0\)
* community\.windows \(still version 2\.2\.0\)
* community\.zabbix \(still version 2\.4\.0\)
* containers\.podman \(still version 1\.13\.0\)
* cyberark\.conjur \(still version 1\.2\.2\)
* cyberark\.pas \(still version 1\.0\.25\)
* dellemc\.enterprise\_sonic \(still version 2\.4\.0\)
* dellemc\.openmanage \(still version 9\.2\.0\)
* dellemc\.powerflex \(still version 2\.4\.0\)
* dellemc\.unity \(still version 2\.0\.0\)
* f5networks\.f5\_modules \(still version 1\.28\.0\)
* fortinet\.fortimanager \(still version 2\.5\.0\)
* fortinet\.fortios \(still version 2\.3\.6\)
* frr\.frr \(still version 2\.0\.2\)
* google\.cloud \(still version 1\.3\.0\)
* grafana\.grafana \(still version 5\.2\.0\)
* hetzner\.hcloud \(still version 3\.1\.1\)
* ibm\.qradar \(still version 3\.0\.0\)
* ibm\.spectrum\_virtualize \(still version 2\.0\.0\)
* ibm\.storage\_virtualize \(still version 2\.3\.1\)
* infinidat\.infinibox \(still version 1\.4\.5\)
* infoblox\.nios\_modules \(still version 1\.6\.1\)
* inspur\.sm \(still version 2\.3\.0\)
* junipernetworks\.junos \(still version 8\.0\.0\)
* kubernetes\.core \(still version 3\.1\.0\)
* lowlydba\.sqlserver \(still version 2\.3\.2\)
* microsoft\.ad \(still version 1\.5\.0\)
* netapp\.cloudmanager \(still version 21\.22\.1\)
* netapp\.ontap \(still version 22\.11\.0\)
* netapp\.storagegrid \(still version 21\.12\.0\)
* netapp\_eseries\.santricity \(still version 1\.4\.0\)
* netbox\.netbox \(still version 3\.18\.0\)
* ngine\_io\.cloudstack \(still version 2\.3\.0\)
* ngine\_io\.exoscale \(still version 1\.1\.0\)
* openstack\.cloud \(still version 2\.2\.0\)
* openvswitch\.openvswitch \(still version 2\.1\.1\)
* ovirt\.ovirt \(still version 3\.2\.0\)
* purestorage\.flasharray \(still version 1\.28\.0\)
* purestorage\.flashblade \(still version 1\.17\.0\)
* sensu\.sensu\_go \(still version 1\.14\.0\)
* splunk\.es \(still version 3\.0\.0\)
* t\_systems\_mms\.icinga\_director \(still version 2\.0\.1\)
* telekom\_mms\.icinga\_director \(still version 2\.1\.2\)
* theforeman\.foreman \(still version 4\.0\.0\)
* vmware\.vmware\_rest \(still version 3\.0\.1\)
* vultr\.cloud \(still version 1\.12\.1\)
* vyos\.vyos \(still version 4\.1\.0\)
* wti\.remote \(still version 1\.0\.5\)

<a id="v10-0-0"></a>
## v10\.0\.0

- <a href="#release-summary-8">Release Summary</a>
- <a href="#removed-collections">Removed Collections</a>
- <a href="#added-collections-2">Added Collections</a>
- <a href="#ansible-core-21">Ansible\-core</a>
- <a href="#included-collections">Included Collections</a>
- <a href="#major-changes-6">Major Changes</a>
    - <a href="#ansible-core-22">Ansible\-core</a>
    - <a href="#ansible-netcommon-1">ansible\.netcommon</a>
    - <a href="#ansible-utils">ansible\.utils</a>
    - <a href="#arista-eos">arista\.eos</a>
    - <a href="#cisco-asa">cisco\.asa</a>
    - <a href="#cisco-ios">cisco\.ios</a>
    - <a href="#cisco-iosxr">cisco\.iosxr</a>
    - <a href="#cisco-nxos-2">cisco\.nxos</a>
    - <a href="#community-dns-8">community\.dns</a>
    - <a href="#community-docker-11">community\.docker</a>
    - <a href="#community-hashi-vault">community\.hashi\_vault</a>
    - <a href="#community-hrobot-1">community\.hrobot</a>
    - <a href="#community-mysql-5">community\.mysql</a>
    - <a href="#containers-podman-10">containers\.podman</a>
    - <a href="#dellemc-openmanage-23">dellemc\.openmanage</a>
    - <a href="#dellemc-unity">dellemc\.unity</a>
    - <a href="#fortinet-fortios-4">fortinet\.fortios</a>
    - <a href="#grafana-grafana-3">grafana\.grafana</a>
    - <a href="#ibm-qradar">ibm\.qradar</a>
    - <a href="#infoblox-nios-modules-4">infoblox\.nios\_modules</a>
    - <a href="#junipernetworks-junos">junipernetworks\.junos</a>
    - <a href="#splunk-es">splunk\.es</a>
- <a href="#minor-changes-7">Minor Changes</a>
    - <a href="#ansible-core-23">Ansible\-core</a>
    - <a href="#amazon-aws-5">amazon\.aws</a>
    - <a href="#ansible-netcommon-2">ansible\.netcommon</a>
    - <a href="#ansible-utils-1">ansible\.utils</a>
    - <a href="#ansible-windows-4">ansible\.windows</a>
    - <a href="#arista-eos-1">arista\.eos</a>
    - <a href="#check-point-mgmt">check\_point\.mgmt</a>
    - <a href="#cisco-aci-2">cisco\.aci</a>
    - <a href="#cisco-dnac-6">cisco\.dnac</a>
    - <a href="#cisco-ios-1">cisco\.ios</a>
    - <a href="#cisco-iosxr-1">cisco\.iosxr</a>
    - <a href="#cisco-ise-4">cisco\.ise</a>
    - <a href="#cisco-meraki-2">cisco\.meraki</a>
    - <a href="#cisco-mso-4">cisco\.mso</a>
    - <a href="#cisco-nxos-3">cisco\.nxos</a>
    - <a href="#community-aws">community\.aws</a>
    - <a href="#community-ciscosmb">community\.ciscosmb</a>
    - <a href="#community-crypto-5">community\.crypto</a>
    - <a href="#community-digitalocean">community\.digitalocean</a>
    - <a href="#community-dns-9">community\.dns</a>
    - <a href="#community-docker-12">community\.docker</a>
    - <a href="#community-general-22">community\.general</a>
    - <a href="#community-grafana">community\.grafana</a>
    - <a href="#community-hashi-vault-1">community\.hashi\_vault</a>
    - <a href="#community-hrobot-2">community\.hrobot</a>
    - <a href="#community-mysql-6">community\.mysql</a>
    - <a href="#community-postgresql-8">community\.postgresql</a>
    - <a href="#community-rabbitmq">community\.rabbitmq</a>
    - <a href="#community-routeros-7">community\.routeros</a>
    - <a href="#community-vmware-10">community\.vmware</a>
    - <a href="#community-windows-2">community\.windows</a>
    - <a href="#community-zabbix-2">community\.zabbix</a>
    - <a href="#containers-podman-11">containers\.podman</a>
    - <a href="#dellemc-enterprise-sonic-4">dellemc\.enterprise\_sonic</a>
    - <a href="#dellemc-openmanage-24">dellemc\.openmanage</a>
    - <a href="#dellemc-powerflex-1">dellemc\.powerflex</a>
    - <a href="#f5networks-f5-modules-5">f5networks\.f5\_modules</a>
    - <a href="#fortinet-fortimanager-9">fortinet\.fortimanager</a>
    - <a href="#google-cloud-2">google\.cloud</a>
    - <a href="#grafana-grafana-4">grafana\.grafana</a>
    - <a href="#hetzner-hcloud">hetzner\.hcloud</a>
    - <a href="#ibm-storage-virtualize-4">ibm\.storage\_virtualize</a>
    - <a href="#infoblox-nios-modules-5">infoblox\.nios\_modules</a>
    - <a href="#inspur-ispim-2">inspur\.ispim</a>
    - <a href="#junipernetworks-junos-1">junipernetworks\.junos</a>
    - <a href="#kubernetes-core-1">kubernetes\.core</a>
    - <a href="#lowlydba-sqlserver-2">lowlydba\.sqlserver</a>
    - <a href="#microsoft-ad-5">microsoft\.ad</a>
    - <a href="#netapp-ontap-5">netapp\.ontap</a>
    - <a href="#netapp-storagegrid">netapp\.storagegrid</a>
    - <a href="#netbox-netbox-5">netbox\.netbox</a>
    - <a href="#purestorage-flasharray-10">purestorage\.flasharray</a>
    - <a href="#purestorage-flashblade-5">purestorage\.flashblade</a>
    - <a href="#telekom-mms-icinga-director-2">telekom\_mms\.icinga\_director</a>
    - <a href="#theforeman-foreman-4">theforeman\.foreman</a>
    - <a href="#vmware-vmware-rest-2">vmware\.vmware\_rest</a>
    - <a href="#vultr-cloud-1">vultr\.cloud</a>
- <a href="#breaking-changes--porting-guide">Breaking Changes / Porting Guide</a>
    - <a href="#ansible-core-24">Ansible\-core</a>
    - <a href="#amazon-aws-6">amazon\.aws</a>
    - <a href="#cloud-common">cloud\.common</a>
    - <a href="#community-aws-1">community\.aws</a>
    - <a href="#community-ciscosmb-1">community\.ciscosmb</a>
    - <a href="#community-dns-10">community\.dns</a>
    - <a href="#community-general-23">community\.general</a>
    - <a href="#community-hrobot-3">community\.hrobot</a>
    - <a href="#community-okd">community\.okd</a>
    - <a href="#hetzner-hcloud-1">hetzner\.hcloud</a>
    - <a href="#kubernetes-core-2">kubernetes\.core</a>
    - <a href="#theforeman-foreman-5">theforeman\.foreman</a>
    - <a href="#vmware-vmware-rest-3">vmware\.vmware\_rest</a>
- <a href="#deprecated-features-7">Deprecated Features</a>
    - <a href="#ansible-core-25">Ansible\-core</a>
    - <a href="#amazon-aws-7">amazon\.aws</a>
    - <a href="#community-aws-2">community\.aws</a>
    - <a href="#community-crypto-6">community\.crypto</a>
    - <a href="#community-dns-11">community\.dns</a>
    - <a href="#community-docker-13">community\.docker</a>
    - <a href="#community-general-24">community\.general</a>
    - <a href="#community-hrobot-4">community\.hrobot</a>
    - <a href="#community-okd-1">community\.okd</a>
    - <a href="#community-vmware-11">community\.vmware</a>
    - <a href="#dellemc-openmanage-25">dellemc\.openmanage</a>
    - <a href="#kubernetes-core-3">kubernetes\.core</a>
- <a href="#removed-features-previously-deprecated">Removed Features \(previously deprecated\)</a>
    - <a href="#ansible-core-26">Ansible\-core</a>
    - <a href="#amazon-aws-8">amazon\.aws</a>
    - <a href="#arista-eos-2">arista\.eos</a>
    - <a href="#cisco-ios-2">cisco\.ios</a>
    - <a href="#cisco-iosxr-2">cisco\.iosxr</a>
    - <a href="#cisco-nxos-4">cisco\.nxos</a>
    - <a href="#community-dns-12">community\.dns</a>
    - <a href="#community-general-25">community\.general</a>
    - <a href="#community-grafana-1">community\.grafana</a>
    - <a href="#community-hrobot-5">community\.hrobot</a>
    - <a href="#junipernetworks-junos-2">junipernetworks\.junos</a>
- <a href="#security-fixes-2">Security Fixes</a>
    - <a href="#ansible-core-27">Ansible\-core</a>
    - <a href="#community-dns-13">community\.dns</a>
    - <a href="#community-docker-14">community\.docker</a>
    - <a href="#community-general-26">community\.general</a>
    - <a href="#community-hrobot-6">community\.hrobot</a>
- <a href="#bugfixes-8">Bugfixes</a>
    - <a href="#ansible-core-28">Ansible\-core</a>
    - <a href="#amazon-aws-9">amazon\.aws</a>
    - <a href="#ansible-netcommon-3">ansible\.netcommon</a>
    - <a href="#ansible-utils-2">ansible\.utils</a>
    - <a href="#ansible-windows-5">ansible\.windows</a>
    - <a href="#arista-eos-3">arista\.eos</a>
    - <a href="#check-point-mgmt-1">check\_point\.mgmt</a>
    - <a href="#cisco-aci-3">cisco\.aci</a>
    - <a href="#cisco-asa-1">cisco\.asa</a>
    - <a href="#cisco-ios-3">cisco\.ios</a>
    - <a href="#cisco-iosxr-3">cisco\.iosxr</a>
    - <a href="#cisco-ise-5">cisco\.ise</a>
    - <a href="#cisco-meraki-3">cisco\.meraki</a>
    - <a href="#cisco-mso-5">cisco\.mso</a>
    - <a href="#cisco-nxos-5">cisco\.nxos</a>
    - <a href="#community-aws-3">community\.aws</a>
    - <a href="#community-ciscosmb-2">community\.ciscosmb</a>
    - <a href="#community-crypto-7">community\.crypto</a>
    - <a href="#community-digitalocean-1">community\.digitalocean</a>
    - <a href="#community-dns-14">community\.dns</a>
    - <a href="#community-docker-15">community\.docker</a>
    - <a href="#community-general-27">community\.general</a>
    - <a href="#community-grafana-2">community\.grafana</a>
    - <a href="#community-hrobot-7">community\.hrobot</a>
    - <a href="#community-mysql-7">community\.mysql</a>
    - <a href="#community-postgresql-9">community\.postgresql</a>
    - <a href="#community-routeros-8">community\.routeros</a>
    - <a href="#community-sap-libs">community\.sap\_libs</a>
    - <a href="#community-vmware-12">community\.vmware</a>
    - <a href="#community-windows-3">community\.windows</a>
    - <a href="#community-zabbix-3">community\.zabbix</a>
    - <a href="#containers-podman-12">containers\.podman</a>
    - <a href="#dellemc-enterprise-sonic-5">dellemc\.enterprise\_sonic</a>
    - <a href="#dellemc-openmanage-26">dellemc\.openmanage</a>
    - <a href="#f5networks-f5-modules-6">f5networks\.f5\_modules</a>
    - <a href="#fortinet-fortimanager-10">fortinet\.fortimanager</a>
    - <a href="#fortinet-fortios-5">fortinet\.fortios</a>
    - <a href="#hetzner-hcloud-2">hetzner\.hcloud</a>
    - <a href="#ibm-qradar-1">ibm\.qradar</a>
    - <a href="#ibm-storage-virtualize-5">ibm\.storage\_virtualize</a>
    - <a href="#infoblox-nios-modules-6">infoblox\.nios\_modules</a>
    - <a href="#junipernetworks-junos-3">junipernetworks\.junos</a>
    - <a href="#kubernetes-core-4">kubernetes\.core</a>
    - <a href="#lowlydba-sqlserver-3">lowlydba\.sqlserver</a>
    - <a href="#microsoft-ad-6">microsoft\.ad</a>
    - <a href="#netapp-ontap-6">netapp\.ontap</a>
    - <a href="#netapp-storagegrid-1">netapp\.storagegrid</a>
    - <a href="#netbox-netbox-6">netbox\.netbox</a>
    - <a href="#purestorage-flasharray-11">purestorage\.flasharray</a>
    - <a href="#purestorage-flashblade-6">purestorage\.flashblade</a>
    - <a href="#splunk-es-1">splunk\.es</a>
    - <a href="#telekom-mms-icinga-director-3">telekom\_mms\.icinga\_director</a>
    - <a href="#theforeman-foreman-6">theforeman\.foreman</a>
    - <a href="#vmware-vmware-rest-4">vmware\.vmware\_rest</a>
    - <a href="#vultr-cloud-2">vultr\.cloud</a>
- <a href="#known-issues-7">Known Issues</a>
    - <a href="#community-docker-16">community\.docker</a>
    - <a href="#dellemc-openmanage-27">dellemc\.openmanage</a>
- <a href="#new-plugins-3">New Plugins</a>
    - <a href="#become">Become</a>
    - <a href="#callback">Callback</a>
    - <a href="#connection">Connection</a>
    - <a href="#filter-3">Filter</a>
    - <a href="#lookup-1">Lookup</a>
    - <a href="#test-1">Test</a>
- <a href="#new-modules-7">New Modules</a>
    - <a href="#amazon-aws-10">amazon\.aws</a>
    - <a href="#ansible-netcommon-4">ansible\.netcommon</a>
    - <a href="#check-point-mgmt-2">check\_point\.mgmt</a>
    - <a href="#cisco-ios-4">cisco\.ios</a>
    - <a href="#community-aws-4">community\.aws</a>
    - <a href="#community-crypto-8">community\.crypto</a>
    - <a href="#community-digitalocean-2">community\.digitalocean</a>
    - <a href="#community-docker-17">community\.docker</a>
    - <a href="#community-general-28">community\.general</a>
    - <a href="#community-hashi-vault-2">community\.hashi\_vault</a>
    - <a href="#community-zabbix-4">community\.zabbix</a>
    - <a href="#containers-podman-13">containers\.podman</a>
    - <a href="#dellemc-enterprise-sonic-6">dellemc\.enterprise\_sonic</a>
    - <a href="#dellemc-openmanage-28">dellemc\.openmanage</a>
    - <a href="#dellemc-powerflex-2">dellemc\.powerflex</a>
    - <a href="#fortinet-fortimanager-11">fortinet\.fortimanager</a>
    - <a href="#hetzner-hcloud-3">hetzner\.hcloud</a>
    - <a href="#infoblox-nios-modules-7">infoblox\.nios\_modules</a>
    - <a href="#netapp-ontap-7">netapp\.ontap</a>
    - <a href="#netbox-netbox-7">netbox\.netbox</a>
    - <a href="#purestorage-flasharray-12">purestorage\.flasharray</a>
    - <a href="#purestorage-flashblade-7">purestorage\.flashblade</a>
    - <a href="#theforeman-foreman-7">theforeman\.foreman</a>
    - <a href="#vultr-cloud-3">vultr\.cloud</a>
- <a href="#new-roles">New Roles</a>
- <a href="#unchanged-collections-8">Unchanged Collections</a>

<a id="release-summary-8"></a>
### Release Summary

Release Date\: 2024\-06\-04

[Porting Guide](https\://docs\.ansible\.com/ansible/devel/porting\_guides\.html)

<a id="removed-collections"></a>
### Removed Collections

* community\.azure \(previously included version\: 2\.0\.0\)
* community\.sap \(previously included version\: 2\.0\.0\)
* gluster\.gluster \(previously included version\: 1\.0\.2\)
* hpe\.nimble \(previously included version\: 1\.1\.4\)
* netapp\.aws \(previously included version\: 21\.7\.1\)
* netapp\.azure \(previously included version\: 21\.10\.1\)
* netapp\.elementsw \(previously included version\: 21\.7\.0\)
* netapp\.um\_info \(previously included version\: 21\.8\.1\)
* purestorage\.fusion \(previously included version\: 1\.6\.0\)

You can still install a removed collection manually with <code>ansible\-galaxy collection install \<name\-of\-collection\></code>\.

<a id="added-collections-2"></a>
### Added Collections

* community\.library\_inventory\_filtering\_v1 \(version 1\.0\.1\)
* kaytus\.ksmanage \(version 1\.2\.1\)

<a id="ansible-core-21"></a>
### Ansible\-core

Ansible 10\.0\.0 contains ansible\-core version 2\.17\.0\.
This is a newer version than version 2\.16\.0 contained in the previous Ansible release\.

The changes are reported in the combined changelog below\.

<a id="included-collections"></a>
### Included Collections

If not mentioned explicitly\, the changes are reported in the combined changelog below\.

| Collection                               | Ansible 9.0.0 | Ansible 10.0.0 | Notes                                                                                                                        |
| ---------------------------------------- | ------------- | -------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| amazon.aws                               | 7.0.0         | 8.0.0          |                                                                                                                              |
| ansible.netcommon                        | 5.3.0         | 6.1.2          |                                                                                                                              |
| ansible.utils                            | 2.11.0        | 4.1.0          |                                                                                                                              |
| ansible.windows                          | 2.1.0         | 2.3.0          |                                                                                                                              |
| arista.eos                               | 6.2.1         | 9.0.0          |                                                                                                                              |
| awx.awx                                  | 23.3.1        | 24.3.1         | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
| azure.azcollection                       | 1.19.0        | 2.3.0          | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
| check_point.mgmt                         | 5.1.1         | 5.2.3          |                                                                                                                              |
| cisco.aci                                | 2.8.0         | 2.9.0          |                                                                                                                              |
| cisco.asa                                | 4.0.3         | 5.0.1          |                                                                                                                              |
| cisco.dnac                               | 6.7.6         | 6.13.3         |                                                                                                                              |
| cisco.intersight                         | 2.0.3         | 2.0.9          | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
| cisco.ios                                | 5.2.0         | 8.0.0          |                                                                                                                              |
| cisco.iosxr                              | 6.1.0         | 9.0.0          |                                                                                                                              |
| cisco.ise                                | 2.5.16        | 2.9.1          |                                                                                                                              |
| cisco.meraki                             | 2.16.14       | 2.18.1         |                                                                                                                              |
| cisco.mso                                | 2.5.0         | 2.6.0          |                                                                                                                              |
| cisco.nxos                               | 5.2.1         | 8.0.0          |                                                                                                                              |
| cloud.common                             | 2.1.4         | 3.0.0          |                                                                                                                              |
| community.aws                            | 7.0.0         | 8.0.0          |                                                                                                                              |
| community.ciscosmb                       | 1.0.7         | 1.0.9          |                                                                                                                              |
| community.crypto                         | 2.16.0        | 2.20.0         |                                                                                                                              |
| community.digitalocean                   | 1.24.0        | 1.26.0         |                                                                                                                              |
| community.dns                            | 2.6.3         | 3.0.0          |                                                                                                                              |
| community.docker                         | 3.4.11        | 3.10.3         |                                                                                                                              |
| community.general                        | 8.0.2         | 9.0.1          |                                                                                                                              |
| community.grafana                        | 1.6.1         | 1.9.1          |                                                                                                                              |
| community.hashi_vault                    | 6.0.0         | 6.2.0          |                                                                                                                              |
| community.hrobot                         | 1.8.2         | 2.0.0          |                                                                                                                              |
| community.library_inventory_filtering_v1 |               | 1.0.1          | The collection was added to Ansible                                                                                          |
| community.mongodb                        | 1.6.3         | 1.7.4          | There are no changes recorded in the changelog.                                                                              |
| community.mysql                          | 3.8.0         | 3.9.0          |                                                                                                                              |
| community.okd                            | 2.3.0         | 3.0.1          |                                                                                                                              |
| community.postgresql                     | 3.2.0         | 3.4.1          |                                                                                                                              |
| community.rabbitmq                       | 1.2.3         | 1.3.0          |                                                                                                                              |
| community.routeros                       | 2.10.0        | 2.15.0         |                                                                                                                              |
| community.sap_libs                       | 1.4.1         | 1.4.2          |                                                                                                                              |
| community.vmware                         | 4.0.0         | 4.4.0          |                                                                                                                              |
| community.windows                        | 2.0.0         | 2.2.0          |                                                                                                                              |
| community.zabbix                         | 2.1.0         | 2.4.0          |                                                                                                                              |
| containers.podman                        | 1.11.0        | 1.13.0         |                                                                                                                              |
| cyberark.pas                             | 1.0.23        | 1.0.25         | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
| dellemc.enterprise_sonic                 | 2.2.0         | 2.4.0          |                                                                                                                              |
| dellemc.openmanage                       | 8.4.0         | 9.2.0          |                                                                                                                              |
| dellemc.powerflex                        | 2.0.1         | 2.4.0          |                                                                                                                              |
| dellemc.unity                            | 1.7.1         | 2.0.0          |                                                                                                                              |
| f5networks.f5_modules                    | 1.27.0        | 1.28.0         |                                                                                                                              |
| fortinet.fortimanager                    | 2.3.0         | 2.5.0          |                                                                                                                              |
| fortinet.fortios                         | 2.3.4         | 2.3.6          |                                                                                                                              |
| google.cloud                             | 1.2.0         | 1.3.0          |                                                                                                                              |
| grafana.grafana                          | 2.2.3         | 5.2.0          |                                                                                                                              |
| hetzner.hcloud                           | 2.3.0         | 3.1.1          |                                                                                                                              |
| ibm.qradar                               | 2.1.0         | 3.0.0          |                                                                                                                              |
| ibm.storage_virtualize                   | 2.1.0         | 2.3.1          |                                                                                                                              |
| infinidat.infinibox                      | 1.3.12        | 1.4.5          | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
| infoblox.nios_modules                    | 1.5.0         | 1.6.1          |                                                                                                                              |
| inspur.ispim                             | 2.1.0         | 2.2.1          |                                                                                                                              |
| junipernetworks.junos                    | 5.3.0         | 8.0.0          |                                                                                                                              |
| kaytus.ksmanage                          |               | 1.2.1          | The collection was added to Ansible                                                                                          |
| kubernetes.core                          | 2.4.0         | 3.1.0          |                                                                                                                              |
| lowlydba.sqlserver                       | 2.2.2         | 2.3.2          |                                                                                                                              |
| microsoft.ad                             | 1.3.0         | 1.5.0          |                                                                                                                              |
| netapp.ontap                             | 22.8.2        | 22.11.0        |                                                                                                                              |
| netapp.storagegrid                       | 21.11.1       | 21.12.0        |                                                                                                                              |
| netbox.netbox                            | 3.15.0        | 3.18.0         |                                                                                                                              |
| openstack.cloud                          | 2.1.0         | 2.2.0          | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
| purestorage.flasharray                   | 1.22.0        | 1.28.0         |                                                                                                                              |
| purestorage.flashblade                   | 1.14.0        | 1.17.0         |                                                                                                                              |
| splunk.es                                | 2.1.0         | 3.0.0          |                                                                                                                              |
| telekom_mms.icinga_director              | 1.34.1        | 2.1.2          |                                                                                                                              |
| theforeman.foreman                       | 3.14.0        | 4.0.0          |                                                                                                                              |
| vmware.vmware_rest                       | 2.3.1         | 3.0.1          |                                                                                                                              |
| vultr.cloud                              | 1.10.0        | 1.12.1         |                                                                                                                              |

<a id="major-changes-6"></a>
### Major Changes

<a id="ansible-core-22"></a>
#### Ansible\-core

* urls\.py \- Removed support for Python 2

<a id="ansible-netcommon-1"></a>
#### ansible\.netcommon

* Bumping <em class="title-reference">requires\_ansible</em> to <em class="title-reference">\>\=2\.14\.0</em>\, since previous ansible\-core versions are EoL now\.

<a id="ansible-utils"></a>
#### ansible\.utils

* Bumping <em class="title-reference">netaddr</em> to <em class="title-reference">\>\=0\.10\.1</em>\, means that starting from this release\, the minimum <em class="title-reference">netaddr</em> version this collection requires is <em class="title-reference">\>\=0\.10\.1</em>\.
* Bumping <em class="title-reference">requires\_ansible</em> to <em class="title-reference">\>\=2\.14\.0</em>\, since previous ansible\-core versions are EoL now\.
* This release mainly addresses the breaking changes in the <em class="title-reference">netaddr</em> library\.
* With the new release of <em class="title-reference">netaddr</em> 1\.0\.0\, the <em class="title-reference">IPAddress\.is\_private\(\)</em> method has been removed and instead\, the <em class="title-reference">IPAddress\.is\_global\(\)</em> method has been extended to support the same functionality\. This change has been reflected in the <em class="title-reference">ipaddr</em> filter plugin\.

<a id="arista-eos"></a>
#### arista\.eos

* Bumping <em class="title-reference">requires\_ansible</em> to <em class="title-reference">\>\=2\.14\.0</em>\, since previous ansible\-core versions are EoL now\.
* This release removes previously deprecated modules and attributes from this collection\. Please refer to the <strong>Removed Features</strong> section for details\.
* Update the netcommon base version 6\.1\.0 to support cli\_restore plugin\.

<a id="cisco-asa"></a>
#### cisco\.asa

* Bumping <em class="title-reference">requires\_ansible</em> to <em class="title-reference">\>\=2\.14\.0</em>\, since previous ansible\-core versions are EoL now\.

<a id="cisco-ios"></a>
#### cisco\.ios

* Bumping <em class="title-reference">requires\_ansible</em> to <em class="title-reference">\>\=2\.14\.0</em>\, since previous ansible\-core versions are EoL now\.
* Update the netcommon base version 6\.1\.0 to support cli\_restore plugin\.
* ios\_ntp \- Remove deprecated ntp legacy module

<a id="cisco-iosxr"></a>
#### cisco\.iosxr

* Bumping <em class="title-reference">requires\_ansible</em> to <em class="title-reference">\>\=2\.14\.0</em>\, since previous ansible\-core versions are EoL now\.
* This release removes previously deprecated module and attributes from this collection\. Please refer to the <strong>Removed Features</strong> section for details\.
* Update the netcommon base version to support cli\_restore plugin\.

<a id="cisco-nxos-2"></a>
#### cisco\.nxos

* Bumping <em class="title-reference">requires\_ansible</em> to <em class="title-reference">\>\=2\.14\.0</em>\, since previous ansible\-core versions are EoL now\.
* This release removes four previously deprecated modules from this collection\. Please refer to the <strong>Removed Features</strong> section for details\.
* Updated the minimum required ansible\.netcommon version to 6\.1\.0 to support the cli\_restore module\.

<a id="community-dns-8"></a>
#### community\.dns

* The <code>community\.dns</code> collection now depends on the <code>community\.library\_inventory\_filtering\_v1</code> collection\. This utility collection provides host filtering functionality for inventory plugins\. If you use the Ansible community package\, both collections are included and you do not have to do anything special\. If you install the collection with <code>ansible\-galaxy collection install</code>\, it will be installed automatically\. If you install the collection by copying the files of the collection to a place where ansible\-core can find it\, for example by cloning the git repository\, you need to make sure that you also have to install the dependency if you are using the inventory plugins \([https\://github\.com/ansible\-collections/community\.dns/pull/196](https\://github\.com/ansible\-collections/community\.dns/pull/196)\)\.

<a id="community-docker-11"></a>
#### community\.docker

* The <code>community\.docker</code> collection now depends on the <code>community\.library\_inventory\_filtering\_v1</code> collection\. This utility collection provides host filtering functionality for inventory plugins\. If you use the Ansible community package\, both collections are included and you do not have to do anything special\. If you install the collection with <code>ansible\-galaxy collection install</code>\, it will be installed automatically\. If you install the collection by copying the files of the collection to a place where ansible\-core can find it\, for example by cloning the git repository\, you need to make sure that you also have to install the dependency if you are using the inventory plugins \([https\://github\.com/ansible\-collections/community\.docker/pull/698](https\://github\.com/ansible\-collections/community\.docker/pull/698)\)\.

<a id="community-hashi-vault"></a>
#### community\.hashi\_vault

* requirements \- the <code>requests</code> package which is required by <code>hvac</code> now has a more restrictive range for this collection in certain use cases due to breaking security changes in <code>ansible\-core</code> that were backported \([https\://github\.com/ansible\-collections/community\.hashi\_vault/pull/416](https\://github\.com/ansible\-collections/community\.hashi\_vault/pull/416)\)\.

<a id="community-hrobot-1"></a>
#### community\.hrobot

* The <code>community\.hrobot</code> collection now depends on the <code>community\.library\_inventory\_filtering\_v1</code> collection\. This utility collection provides host filtering functionality for inventory plugins\. If you use the Ansible community package\, both collections are included and you do not have to do anything special\. If you install the collection with <code>ansible\-galaxy collection install</code>\, it will be installed automatically\. If you install the collection by copying the files of the collection to a place where ansible\-core can find it\, for example by cloning the git repository\, you need to make sure that you also have to install the dependency if you are using the inventory plugin \([https\://github\.com/ansible\-collections/community\.hrobot/pull/101](https\://github\.com/ansible\-collections/community\.hrobot/pull/101)\)\.

<a id="community-mysql-5"></a>
#### community\.mysql

* Collection version 2\.\*\.\* is EOL\, no more bugfixes will be backported\. Please consider upgrading to the latest version\.

<a id="containers-podman-10"></a>
#### containers\.podman

* Add quadlet support for Podman modules

<a id="dellemc-openmanage-23"></a>
#### dellemc\.openmanage

* All OME modules are enhanced to support the environment variables <em class="title-reference">OME\_USERNAME</em> and <em class="title-reference">OME\_PASSWORD</em> as fallback for credentials\.
* All iDRAC and Redfish modules are enhanced to support the environment variables <em class="title-reference">IDRAC\_USERNAME</em> and <em class="title-reference">IDRAC\_PASSWORD</em> as fallback for credentials\.
* idrac\_certificates \- The module is enhanced to support the import and export of <em class="title-reference">CUSTOMCERTIFICATE</em>\.
* idrac\_diagnostics \- The module is introduced to run and export diagnostics on iDRAC\.
* idrac\_gather\_facts \- This role is enhanced to support secure boot\.
* idrac\_license \- The module is introduced to configure iDRAC licenses\.
* idrac\_session \- This module allows you to create and delete the sessions on iDRAC\.
* idrac\_user \- This role is introduced to manage local users of iDRAC\.

<a id="dellemc-unity"></a>
#### dellemc\.unity

* Adding support for Unity Puffin v5\.4\.

<a id="fortinet-fortios-4"></a>
#### fortinet\.fortios

* Add notes for backup modules in the documentation in both monitor and monitor\_fact modules\.
* Supported new FOS versions 7\.4\.2 and 7\.4\.3\, and support data type mac\_address in the collection\.
* Update all the boolean values to true/false in the documents and examples\.
* Update the document of log\_fact\.
* Update the documentation for the supported versions from latest to a fix version number\.
* Update the mismatched version message with version ranges\.
* Update the required ansible version to 2\.14\.
* Update the required ansible version to 2\.15\.
* Update the supported version ranges instead of concrete version numbers to reduce the collection size\.

<a id="grafana-grafana-3"></a>
#### grafana\.grafana

* Add Grafana Loki role by \@voidquark in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/188](https\://github\.com/grafana/grafana\-ansible\-collection/pull/188)
* Add Grafana Mimir role by \@GVengelen in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/183](https\://github\.com/grafana/grafana\-ansible\-collection/pull/183)
* Add a new config part to configure KeyCloak based auth by \@he0s in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/191](https\://github\.com/grafana/grafana\-ansible\-collection/pull/191)
* Add an Ansible role for Grafana Alloy by \@ishanjainn in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/169](https\://github\.com/grafana/grafana\-ansible\-collection/pull/169)
* Add an Ansible role for OpenTelemetry Collector by \@ishanjainn in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/138](https\://github\.com/grafana/grafana\-ansible\-collection/pull/138)
* Add promtail role by \@voidquark in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/197](https\://github\.com/grafana/grafana\-ansible\-collection/pull/197)
* Bump ansible\-lint from 24\.2\.2 to 24\.2\.3 by \@dependabot in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/195](https\://github\.com/grafana/grafana\-ansible\-collection/pull/195)

<a id="ibm-qradar"></a>
#### ibm\.qradar

* Bumping <em class="title-reference">requires\_ansible</em> to <em class="title-reference">\>\=2\.14\.0</em>\, since previous ansible\-core versions are EoL now\.

<a id="infoblox-nios-modules-4"></a>
#### infoblox\.nios\_modules

* Upgrade Ansible version support from 2\.13 to 2\.16\.
* Upgrade Python version support from 3\.8 to 3\.10\.

<a id="junipernetworks-junos"></a>
#### junipernetworks\.junos

* Bumping <em class="title-reference">requires\_ansible</em> to <em class="title-reference">\>\=2\.14\.0</em>\, since previous ansible\-core versions are EoL now\.
* This release removes previously deprecated modules from this collection\. Please refer to the <strong>Removed Features</strong> section for details\.
* Update the netcommon base version 6\.1\.0 to support cli\_restore plugin\.

<a id="splunk-es"></a>
#### splunk\.es

* Bumping <em class="title-reference">requires\_ansible</em> to <em class="title-reference">\>\=2\.14\.0</em>\, since previous ansible\-core versions are EoL now\.

<a id="minor-changes-7"></a>
### Minor Changes

<a id="ansible-core-23"></a>
#### Ansible\-core

* Add <code>dump</code> and <code>passno</code> mount information to facts component \([https\://github\.com/ansible/ansible/issues/80478](https\://github\.com/ansible/ansible/issues/80478)\)
* Added MIRACLE LINUX 9\.2 in RedHat OS Family\.
* Interpreter Discovery \- Remove hardcoded references to specific python interpreters to use for certain distro versions\, and modify logic for python3 to become the default\.
* Use Python\'s built\-in <code>functools\.update\_wrapper</code> instead an inline copy from Python 3\.7\.
* User can now set ansible\.log to record higher verbosity than what is specified for display via new configuration item LOG\_VERBOSITY\.
* <code>DEFAULT\_PRIVATE\_ROLE\_VARS</code> is now overridden by explicit setting of <code>public</code> for <code>include\_roles</code> and <code>import\_roles</code>\.
* <code>ansible\-galaxy role\|collection init</code> \- accept <code>\-\-extra\-vars</code> to supplement/override the variables <code>ansible\-galaxy</code> injects for templating <code>\.j2</code> files in the skeleton\.
* <code>import\_role</code> action now also gets a <code>public</code> option that controls variable exports\,  default depending on <code>DEFAULT\_PRIVATE\_ROLE\_VARS</code> \(if using defaults equates to <code>public\=True</code>\)\.
* added configuration item <code>TARGET\_LOG\_INFO</code> that allows the user/author to add an information string to the log output on targets\.
* ansible\-doc \- treat double newlines in documentation strings as paragraph breaks\. This is useful to create multi\-paragraph notes in module/plugin documentation \([https\://github\.com/ansible/ansible/pull/82465](https\://github\.com/ansible/ansible/pull/82465)\)\.
* ansible\-doc output has been revamped to make it more visually pleasing when going to a terminal\, also more concise\, use \-v to show extra information\.
* ansible\-galaxy \- Started normalizing build directory with a trailing separator when building collections\, internally\. \([https\://github\.com/ansible/ansible/pull/81619](https\://github\.com/ansible/ansible/pull/81619)\)\.
* ansible\-galaxy dependency resolution messages have changed the unexplained \'virtual\' collection for the specific type \(\'scm\'\, \'dir\'\, etc\) that is more user friendly
* ansible\-test \- Add Alpine 3\.19 container\.
* ansible\-test \- Add Alpine 3\.19 to remotes\.
* ansible\-test \- Add Fedora 39 container\.
* ansible\-test \- Add Fedora 39 remote\.
* ansible\-test \- Add a work\-around for permission denied errors when using <code>pytest \>\= 8</code> on multi\-user systems with an installed version of <code>ansible\-test</code>\.
* ansible\-test \- Add support for RHEL 9\.3 remotes\.
* ansible\-test \- Added a macOS 14\.3 remote VM\.
* ansible\-test \- Bump the <code>nios\-test\-container</code> from version 2\.0\.0 to version 3\.0\.0\.
* ansible\-test \- Containers and remotes managed by ansible\-test will have their Python <code>EXTERNALLY\-MANAGED</code> marker \(PEP668\) removed\. This provides backwards compatibility for existing tests running in newer environments which mark their Python as externally managed\. A future version of ansible\-test may change this behavior\, requiring tests to be adapted to such environments\.
* ansible\-test \- Make Python 3\.12 the default version used in the <code>base</code> and <code>default</code> containers\.
* ansible\-test \- Remove Alpine 3\(\.18\) container\.
* ansible\-test \- Remove Alpine 3\.18 from remotes\.
* ansible\-test \- Remove Fedora 38 remote support\.
* ansible\-test \- Remove Fedora 38 test container\.
* ansible\-test \- Remove rhel/9\.2 test remote
* ansible\-test \- Remove the FreeBSD 13\.2 remote\.
* ansible\-test \- Removed fallback to <code>virtualenv</code> when <code>\-m venv</code> is non\-functional\.
* ansible\-test \- Removed test remotes\: macos/13\.2
* ansible\-test \- Removed the <code>no\-basestring</code> sanity test\. The test is no longer necessary now that Python 3 is required\.
* ansible\-test \- Removed the <code>no\-dict\-iteritems</code>\, <code>no\-dict\-iterkeys</code> and <code>no\-dict\-itervalues</code> sanity tests\. The tests are no longer necessary since Python 3 is required\.
* ansible\-test \- Removed the <code>no\-main\-display</code> sanity test\. The unwanted pattern is unlikely to occur\, since the test has existed since Ansible 2\.8\.
* ansible\-test \- Removed the <code>no\-unicode\-literals</code> sanity test\. The test is unnecessary now that Python 3 is required and the <code>unicode\_literals</code> feature has no effect\.
* ansible\-test \- Special handling for installation of <code>cryptography</code> has been removed\, as it is no longer necessary\.
* ansible\-test \- The <code>shellcheck</code> sanity test no longer disables the <code>SC2164</code> check\. In most cases\, seeing this error means the script is missing <code>set \-e</code>\.
* ansible\-test \- The <code>unidiomatic\-typecheck</code> rule has been enabled in the <code>pylint</code> sanity test\.
* ansible\-test \- The <code>unidiomatic\-typecheck</code> rule has been removed from the <code>validate\-modules</code> sanity test\.
* ansible\-test \- Update the base and default containers to use Ubuntu 22\.04 for the base image\. This also updates PowerShell to version 7\.4\.0 with \.NET 8\.0\.0 and ShellCheck to version 0\.8\.0\.
* ansible\-test \- Updated the CloudStack test container to version 1\.7\.0\.
* ansible\-test \- Updated the distro test containers to version 6\.3\.0 to include coverage 7\.3\.2 for Python 3\.8\+\. The alpine3 container is now based on 3\.18 instead of 3\.17 and includes Python 3\.11 instead of Python 3\.10\.
* ansible\-test \- Updated the distro test containers to version 7\.1\.0\.
* ansible\-test \- When ansible\-test installs requirements\, it now instructs pip to allow installs on externally managed environments as defined by PEP 668\. This only occurs in ephemeral environments managed by ansible\-test\, such as containers\, or when the <em class="title-reference">\-\-requirements</em> option is used\.
* ansible\-test \- When invoking <code>sleep</code> in containers during container setup\, the <code>env</code> command is used to avoid invoking the shell builtin\, if present\.
* ansible\-test \- document block name now included in error message for YAML parsing errors \([https\://github\.com/ansible/ansible/issues/82353](https\://github\.com/ansible/ansible/issues/82353)\)\.
* ansible\-test \- sanity test allows <code>EXAMPLES</code> to be multi\-document YAML \([https\://github\.com/ansible/ansible/issues/82353](https\://github\.com/ansible/ansible/issues/82353)\)\.
* ansible\-test now has FreeBSD 13\.3 and 14\.0 support
* ansible\.builtin\.user \- Remove user not found warning \([https\://github\.com/ansible/ansible/issues/80267](https\://github\.com/ansible/ansible/issues/80267)\)
* apt\_repository\.py \- use api\.launchpad\.net endpoint instead of launchpad\.net/api
* async tasks can now also support check mode at the same time\.
* async\_status now supports check mode\.
* constructed inventory plugin \- Adding a note that only group\_vars of explicit groups are loaded \([https\://github\.com/ansible/ansible/pull/82580](https\://github\.com/ansible/ansible/pull/82580)\)\.
* csvfile \- add a keycol parameter to specify in which column to search\.
* dnf \- add the <code>best</code> option
* dnf5 \- add the <code>best</code> option
* filter plugin \- Add the count and mandatory\_count parameters in the regex\_replace filter
* find \- add a encoding parameter to specify which encoding of the files to be searched\.
* git module \- gpg\_allowlist name was added in 2\.17 and we will eventually deprecate the gpg\_whitelist alias\.
* import\_role \- allow subdirectories with <code>\_from</code> options for parity with <code>include\_role</code> \([https\://github\.com/ansible/ansible/issues/82584](https\://github\.com/ansible/ansible/issues/82584)\)\.
* module argument spec \- Allow module authors to include arbitrary additional context in the argument spec\, by making use of a new top level key called <code>context</code>\. This key should be a dict type\. This allows for users to customize what they place in the argument spec\, without having to ignore sanity tests that validate the schema\.
* modules \- Add the ability for an action plugin to call <code>self\.\_execute\_module\(\*\, ignore\_unknown\_opts\=True\)</code> to execute a module with options that may not be supported for the version being called\. This tells the module basic wrapper to ignore validating the options provided match the arg spec\.
* package action now has a configuration that overrides the detected package manager\, it is still overridden itself by the use option\.
* py3compat \- Remove <code>ansible\.utils\.py3compat</code> as it is no longer necessary
* removed the unused argument <code>create\_new\_password</code> from <code>CLI\.build\_vault\_ids</code> \([https\://github\.com/ansible/ansible/pull/82066](https\://github\.com/ansible/ansible/pull/82066)\)\.
* urls \- Add support for TLS 1\.3 post handshake certificate authentication \- [https\://github\.com/ansible/ansible/issues/81782](https\://github\.com/ansible/ansible/issues/81782)
* urls \- reduce complexity of <code>Request\.open</code>
* user \- accept yescrypt hash as user password
* validate\-modules tests now correctly handles <code>choices</code> in dictionary format\.

<a id="amazon-aws-5"></a>
#### amazon\.aws

* AnsibeAWSModule \- added <code>fail\_json\_aws\_error\(\)</code> as a wrapper for <code>fail\_json\(\)</code> and <code>fail\_json\_aws\(\)</code> when passed an <code>AnsibleAWSError</code> exception \([https\://github\.com/ansible\-collections/amazon\.aws/pull/1997](https\://github\.com/ansible\-collections/amazon\.aws/pull/1997)\)\.
* autoscaling\_group \- minor PEP8 whitespace sanity fixes \([https\://github\.com/ansible\-collections/amazon\.aws/pull/1846](https\://github\.com/ansible\-collections/amazon\.aws/pull/1846)\)\.
* autoscaling\_group \- removed unused code \([https\://github\.com/ansible\-collections/amazon\.aws/pull/1996](https\://github\.com/ansible\-collections/amazon\.aws/pull/1996)\)\.
* backup\_plan \- Let user to set <code>schedule\_expression\_timezone</code> for backup plan rules when when using botocore \>\= 1\.31\.36 \([https\://github\.com/ansible\-collections/amazon\.aws/issues/1952](https\://github\.com/ansible\-collections/amazon\.aws/issues/1952)\)\.
* cloudformation \- apply automatic retries when paginating through stack events without a filter \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2049](https\://github\.com/ansible\-collections/amazon\.aws/pull/2049)\)\.
* cloudtrail \- removed unused code \([https\://github\.com/ansible\-collections/amazon\.aws/pull/1996](https\://github\.com/ansible\-collections/amazon\.aws/pull/1996)\)\.
* ec2\_ami\_info \- simplify parameters to <code>get\_image\_attribute</code> to only pass ID of image \([https\://github\.com/ansible\-collections/amazon\.aws/pull/1846](https\://github\.com/ansible\-collections/amazon\.aws/pull/1846)\)\.
* ec2\_eip \- use <code>ResourceTags</code> to set initial tags upon creation \([https\://github\.com/ansible\-collections/amazon\.aws/issues/1843](https\://github\.com/ansible\-collections/amazon\.aws/issues/1843)\)
* ec2\_instance \- Add support for modifying metadata options of an existing instance \([https\://github\.com/ansible\-collections/amazon\.aws/pull/1918](https\://github\.com/ansible\-collections/amazon\.aws/pull/1918)\)\.
* ec2\_instance \- add support for AdditionalInfo option when creating an instance \([https\://github\.com/ansible\-collections/amazon\.aws/pull/1828](https\://github\.com/ansible\-collections/amazon\.aws/pull/1828)\)\.
* ec2\_instance \- add support for <code>host</code> option in placement\.tenancy \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2026](https\://github\.com/ansible\-collections/amazon\.aws/pull/2026)\)\.
* ec2\_instance \- removed unused code \([https\://github\.com/ansible\-collections/amazon\.aws/pull/1996](https\://github\.com/ansible\-collections/amazon\.aws/pull/1996)\)\.
* ec2\_security\_group \- use <code>ResourceTags</code> to set initial tags upon creation \([https\://github\.com/ansible\-collections/amazon\.aws/pull/1844](https\://github\.com/ansible\-collections/amazon\.aws/pull/1844)\)
* ec2\_vol \- Ensure volume state is not one of <code>deleted</code> or <code>deleting</code> when trying to delete volume\, to guaranty idempotency \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2052](https\://github\.com/ansible\-collections/amazon\.aws/pull/2052)\)\.
* ec2\_vol \- removed unused code \([https\://github\.com/ansible\-collections/amazon\.aws/pull/1996](https\://github\.com/ansible\-collections/amazon\.aws/pull/1996)\)\.
* ec2\_vpc\_igw \- use <code>ResourceTags</code> to set initial tags upon creation \([https\://github\.com/ansible\-collections/amazon\.aws/issues/1843](https\://github\.com/ansible\-collections/amazon\.aws/issues/1843)\)
* ec2\_vpc\_route\_table \- use <code>ResourceTags</code> to set initial tags upon creation \([https\://github\.com/ansible\-collections/amazon\.aws/issues/1843](https\://github\.com/ansible\-collections/amazon\.aws/issues/1843)\)
* ec2\_vpc\_subnet \- the default value for <code>tags</code> has been changed from <code>\{\}</code> to <code>None</code>\, to remove tags from a subnet an empty map must be explicitly passed to the module \([https\://github\.com/ansible\-collections/amazon\.aws/pull/1876](https\://github\.com/ansible\-collections/amazon\.aws/pull/1876)\)\.
* ec2\_vpc\_subnet \- use <code>ResourceTags</code> to set initial tags upon creation \([https\://github\.com/ansible\-collections/amazon\.aws/issues/1843](https\://github\.com/ansible\-collections/amazon\.aws/issues/1843)\)
* ec2\_vpc\_subnet \- use <code>wait\_timeout</code> to also control maximum time to wait for initial creation of subnets \([https\://github\.com/ansible\-collections/amazon\.aws/pull/1848](https\://github\.com/ansible\-collections/amazon\.aws/pull/1848)\)\.
* elb\_classic\_lb \- removed unused code \([https\://github\.com/ansible\-collections/amazon\.aws/pull/1996](https\://github\.com/ansible\-collections/amazon\.aws/pull/1996)\)\.
* iam\_access\_key \- refactored code to use <code>AnsibleIAMError</code> and <code>IAMErrorHandler</code> as well as moving shared code into module\_utils\.iam \([https\://github\.com/ansible\-collections/amazon\.aws/pull/1998](https\://github\.com/ansible\-collections/amazon\.aws/pull/1998)\)\.
* iam\_access\_key\_info \- refactored code to use <code>AnsibleIAMError</code> and <code>IAMErrorHandler</code> as well as moving shared code into module\_utils\.iam \([https\://github\.com/ansible\-collections/amazon\.aws/pull/1998](https\://github\.com/ansible\-collections/amazon\.aws/pull/1998)\)\.
* iam\_group \- Basic testing of <code>name</code> and <code>path</code> has been added to improve error messages \([https\://github\.com/ansible\-collections/amazon\.aws/pull/1933](https\://github\.com/ansible\-collections/amazon\.aws/pull/1933)\)\.
* iam\_group \- <code>group\_name</code> has been added as an alias to <code>name</code> for consistency with other IAM modules \([https\://github\.com/ansible\-collections/amazon\.aws/pull/1933](https\://github\.com/ansible\-collections/amazon\.aws/pull/1933)\)\.
* iam\_group \- add support for setting group path \([https\://github\.com/ansible\-collections/amazon\.aws/pull/1892](https\://github\.com/ansible\-collections/amazon\.aws/pull/1892)\)\.
* iam\_group \- adds attached\_policies return value \([https\://github\.com/ansible\-collections/amazon\.aws/pull/1892](https\://github\.com/ansible\-collections/amazon\.aws/pull/1892)\)\.
* iam\_group \- code refactored to avoid single long function \([https\://github\.com/ansible\-collections/amazon\.aws/pull/1892](https\://github\.com/ansible\-collections/amazon\.aws/pull/1892)\)\.
* iam\_group \- refactored code to use <code>AnsibleIAMError</code> and <code>IAMErrorHandler</code> as well as moving shared code into module\_utils\.iam \([https\://github\.com/ansible\-collections/amazon\.aws/pull/1998](https\://github\.com/ansible\-collections/amazon\.aws/pull/1998)\)\.
* iam\_instance\_profile \- Basic testing of <code>name</code> and <code>path</code> has been added to improve error messages \([https\://github\.com/ansible\-collections/amazon\.aws/pull/1933](https\://github\.com/ansible\-collections/amazon\.aws/pull/1933)\)\.
* iam\_instance\_profile \- attempting to change the <code>path</code> for an existing profile will now generate a warning\, previously this was silently ignored \([https\://github\.com/ansible\-collections/amazon\.aws/pull/1933](https\://github\.com/ansible\-collections/amazon\.aws/pull/1933)\)\.
* iam\_instance\_profile \- refactored code to use <code>AnsibleIAMError</code> and <code>IAMErrorHandler</code> as well as moving shared code into module\_utils\.iam \([https\://github\.com/ansible\-collections/amazon\.aws/pull/1998](https\://github\.com/ansible\-collections/amazon\.aws/pull/1998)\)\.
* iam\_instance\_profile \- the <code>prefix</code> parameter has been renamed <code>path</code> for consistency with other IAM modules\, <code>prefix</code> remains as an alias\. No change to playbooks is required \([https\://github\.com/ansible\-collections/amazon\.aws/pull/1933](https\://github\.com/ansible\-collections/amazon\.aws/pull/1933)\)\.
* iam\_instance\_profile \- the default value for <code>path</code> has been removed\.  New instances will still be created with a default path of <code>/</code>\. No change to playbooks is required \([https\://github\.com/ansible\-collections/amazon\.aws/pull/1933](https\://github\.com/ansible\-collections/amazon\.aws/pull/1933)\)\.
* iam\_instance\_profile\_info \- refactored code to use <code>AnsibleIAMError</code> and <code>IAMErrorHandler</code> as well as moving shared code into module\_utils\.iam \([https\://github\.com/ansible\-collections/amazon\.aws/pull/1998](https\://github\.com/ansible\-collections/amazon\.aws/pull/1998)\)\.
* iam\_managed\_policy \- Basic testing of <code>name</code> and <code>path</code> has been added to improve error messages \([https\://github\.com/ansible\-collections/amazon\.aws/pull/1933](https\://github\.com/ansible\-collections/amazon\.aws/pull/1933)\)\.
* iam\_managed\_policy \- <code>description</code> attempting to update the description now results in a warning\, previously it was simply ignored \([https\://github\.com/ansible\-collections/amazon\.aws/pull/1936](https\://github\.com/ansible\-collections/amazon\.aws/pull/1936)\)\.
* iam\_managed\_policy \- <code>policy</code> is no longer a required parameter \([https\://github\.com/ansible\-collections/amazon\.aws/pull/1936](https\://github\.com/ansible\-collections/amazon\.aws/pull/1936)\)\.
* iam\_managed\_policy \- added support for tagging managed policies \([https\://github\.com/ansible\-collections/amazon\.aws/pull/1936](https\://github\.com/ansible\-collections/amazon\.aws/pull/1936)\)\.
* iam\_managed\_policy \- more consistently perform retries on rate limiting errors \([https\://github\.com/ansible\-collections/amazon\.aws/pull/1936](https\://github\.com/ansible\-collections/amazon\.aws/pull/1936)\)\.
* iam\_managed\_policy \- refactored code to use <code>AnsibleIAMError</code> and <code>IAMErrorHandler</code> as well as moving shared code into module\_utils\.iam \([https\://github\.com/ansible\-collections/amazon\.aws/pull/1998](https\://github\.com/ansible\-collections/amazon\.aws/pull/1998)\)\.
* iam\_managed\_policy \- support for setting <code>path</code> \([https\://github\.com/ansible\-collections/amazon\.aws/pull/1936](https\://github\.com/ansible\-collections/amazon\.aws/pull/1936)\)\.
* iam\_managed\_policy \- the <code>policy\_description</code> parameter has been renamed <code>description</code> for consistency with other IAM modules\, <code>policy\_description</code> remains as an alias\. No change to playbooks is required \([https\://github\.com/ansible\-collections/amazon\.aws/pull/1933](https\://github\.com/ansible\-collections/amazon\.aws/pull/1933)\)\.
* iam\_managed\_policy \- the <code>policy\_name</code> parameter has been renamed <code>name</code> for consistency with other IAM modules\, <code>policy\_name</code> remains as an alias\. No change to playbooks is required \([https\://github\.com/ansible\-collections/amazon\.aws/pull/1933](https\://github\.com/ansible\-collections/amazon\.aws/pull/1933)\)\.
* iam\_mfa\_device\_info \- refactored code to use <code>AnsibleIAMError</code> and <code>IAMErrorHandler</code> as well as moving shared code into module\_utils\.iam \([https\://github\.com/ansible\-collections/amazon\.aws/pull/1998](https\://github\.com/ansible\-collections/amazon\.aws/pull/1998)\)\.
* iam\_role \- Basic testing of <code>name</code> and <code>path</code> has been added to improve error messages \([https\://github\.com/ansible\-collections/amazon\.aws/pull/1933](https\://github\.com/ansible\-collections/amazon\.aws/pull/1933)\)\.
* iam\_role \- <code>prefix</code> and <code>path\_prefix</code> have been added as aliases to <code>path</code> for consistency with other IAM modules \([https\://github\.com/ansible\-collections/amazon\.aws/pull/1933](https\://github\.com/ansible\-collections/amazon\.aws/pull/1933)\)\.
* iam\_role \- <code>role\_name</code> has been added as an alias to <code>name</code> for consistency with other IAM modules \([https\://github\.com/ansible\-collections/amazon\.aws/pull/1933](https\://github\.com/ansible\-collections/amazon\.aws/pull/1933)\)\.
* iam\_role \- attempting to change the <code>path</code> for an existing profile will now generate a warning\, previously this was silently ignored \([https\://github\.com/ansible\-collections/amazon\.aws/pull/1933](https\://github\.com/ansible\-collections/amazon\.aws/pull/1933)\)\.
* iam\_role \- refactored code to use <code>AnsibleIAMError</code> and <code>IAMErrorHandler</code> as well as moving shared code into module\_utils\.iam \([https\://github\.com/ansible\-collections/amazon\.aws/pull/1998](https\://github\.com/ansible\-collections/amazon\.aws/pull/1998)\)\.
* iam\_role \- the default value for <code>path</code> has been removed\.  New roles will still be created with a default path of <code>/</code>\. No change to playbooks is required \([https\://github\.com/ansible\-collections/amazon\.aws/pull/1933](https\://github\.com/ansible\-collections/amazon\.aws/pull/1933)\)\.
* iam\_role\_info \- <code>path</code> and <code>prefix</code> have been added as aliases to <code>path\_prefix</code> for consistency with other IAM modules \([https\://github\.com/ansible\-collections/amazon\.aws/pull/1933](https\://github\.com/ansible\-collections/amazon\.aws/pull/1933)\)\.
* iam\_role\_info \- refactored code to use <code>AnsibleIAMError</code> and <code>IAMErrorHandler</code> as well as moving shared code into module\_utils\.iam \([https\://github\.com/ansible\-collections/amazon\.aws/pull/1998](https\://github\.com/ansible\-collections/amazon\.aws/pull/1998)\)\.
* iam\_user \- Basic testing of <code>name</code> and <code>path</code> has been added to improve error messages \([https\://github\.com/ansible\-collections/amazon\.aws/pull/1933](https\://github\.com/ansible\-collections/amazon\.aws/pull/1933)\)\.
* iam\_user \- <code>user\_name</code> has been added as an alias to <code>name</code> for consistency with other IAM modules \([https\://github\.com/ansible\-collections/amazon\.aws/pull/1933](https\://github\.com/ansible\-collections/amazon\.aws/pull/1933)\)\.
* iam\_user \- add <code>boundary</code> parameter to support managing boundary policy on users \([https\://github\.com/ansible\-collections/amazon\.aws/pull/1912](https\://github\.com/ansible\-collections/amazon\.aws/pull/1912)\)\.
* iam\_user \- add <code>path</code> parameter to support managing user path \([https\://github\.com/ansible\-collections/amazon\.aws/pull/1912](https\://github\.com/ansible\-collections/amazon\.aws/pull/1912)\)\.
* iam\_user \- added <code>attached\_policies</code> to return value \([https\://github\.com/ansible\-collections/amazon\.aws/pull/1912](https\://github\.com/ansible\-collections/amazon\.aws/pull/1912)\)\.
* iam\_user \- refactored code to reduce complexity \([https\://github\.com/ansible\-collections/amazon\.aws/pull/1912](https\://github\.com/ansible\-collections/amazon\.aws/pull/1912)\)\.
* iam\_user \- refactored code to use <code>AnsibleIAMError</code> and <code>IAMErrorHandler</code> as well as moving shared code into module\_utils\.iam \([https\://github\.com/ansible\-collections/amazon\.aws/pull/1998](https\://github\.com/ansible\-collections/amazon\.aws/pull/1998)\)\.
* iam\_user \- refactored error handling to use a decorator \([https\://github\.com/ansible\-collections/amazon\.aws/pull/1951](https\://github\.com/ansible\-collections/amazon\.aws/pull/1951)\)\.
* iam\_user\_info \- Add <code>login\_profile</code> to return info that is get from a user\, to know if they can login from AWS console \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2012](https\://github\.com/ansible\-collections/amazon\.aws/pull/2012)\)\.
* iam\_user\_info \- <code>prefix</code> has been added as an alias to <code>path\_prefix</code> for consistency with other IAM modules \([https\://github\.com/ansible\-collections/amazon\.aws/pull/1933](https\://github\.com/ansible\-collections/amazon\.aws/pull/1933)\)\.
* iam\_user\_info \- refactored code to use <code>AnsibleIAMError</code> and <code>IAMErrorHandler</code> as well as moving shared code into module\_utils\.iam \([https\://github\.com/ansible\-collections/amazon\.aws/pull/1998](https\://github\.com/ansible\-collections/amazon\.aws/pull/1998)\)\.
* iam\_user\_info \- the <code>path</code> parameter has been renamed <code>path\_prefix</code> for consistency with other IAM modules\, <code>path</code> remains as an alias\. No change to playbooks is required \([https\://github\.com/ansible\-collections/amazon\.aws/pull/1933](https\://github\.com/ansible\-collections/amazon\.aws/pull/1933)\)\.
* kms\_key \- removed unused code \([https\://github\.com/ansible\-collections/amazon\.aws/pull/1996](https\://github\.com/ansible\-collections/amazon\.aws/pull/1996)\)\.
* lambda \- added support for using ECR images for the function \([https\://github\.com/ansible\-collections/amazon\.aws/pull/1939](https\://github\.com/ansible\-collections/amazon\.aws/pull/1939)\)\.
* lambda\_event \- Add support for setting the <code>maximum\_batching\_window\_in\_seconds</code> option \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2025](https\://github\.com/ansible\-collections/amazon\.aws/pull/2025)\)\.
* module\_uils/botocore \- support sets and tuples of errors as well as lists \([https\://github\.com/ansible\-collections/amazon\.aws/pull/1829](https\://github\.com/ansible\-collections/amazon\.aws/pull/1829)\)\.
* module\_utils\.errors \- added a basic error handler decorator \([https\://github\.com/ansible\-collections/amazon\.aws/pull/1951](https\://github\.com/ansible\-collections/amazon\.aws/pull/1951)\)\.
* module\_utils\.iam \- refactored normalization functions to use <code>boto3\_resource\_to\_ansible\_dict\(\)</code> and <code>boto3\_resource\_list\_to\_ansible\_dict\(\)</code> \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2006](https\://github\.com/ansible\-collections/amazon\.aws/pull/2006)\)\.
* module\_utils\.transformations \- add <code>boto3\_resource\_to\_ansible\_dict\(\)</code> and <code>boto3\_resource\_list\_to\_ansible\_dict\(\)</code> helpers \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2006](https\://github\.com/ansible\-collections/amazon\.aws/pull/2006)\)\.
* module\_utils/elbv2 \- Add support for adding listener with multiple certificates during ALB creation\. Allows elb\_application\_elb module to handle mentioned use case\. \([https\://github\.com/ansible\-collections/amazon\.aws/pull/1950](https\://github\.com/ansible\-collections/amazon\.aws/pull/1950)\)\.
* module\_utils/elbv2 \- Add the possibility to update <code>SslPolicy</code>\, <code>Certificates</code> and <code>AlpnPolicy</code> for TLS listeners \([https\://github\.com/ansible\-collections/amazon\.aws/issues/1198](https\://github\.com/ansible\-collections/amazon\.aws/issues/1198)\)\.
* rds\_cluster \- Add support for ServerlessV2ScalingConfiguration to create and modify cluster operations \([https\://github\.com/ansible\-collections/amazon\.aws/pull/1839](https\://github\.com/ansible\-collections/amazon\.aws/pull/1839)\)\.
* rds\_instance \- Allow passing empty list to <code>enable\_cloudwatch\_logs\_exports</code> in order to remove all existing exports \([https\://github\.com/ansible\-collections/amazon\.aws/pull/1917](https\://github\.com/ansible\-collections/amazon\.aws/pull/1917)\)\.
* rds\_instance\_snapshot \- minor PEP8 whitespace sanity fixes \([https\://github\.com/ansible\-collections/amazon\.aws/pull/1846](https\://github\.com/ansible\-collections/amazon\.aws/pull/1846)\)\.
* s3\_bucket \- refactor s3\_bucket module code for improved readability and maintainability \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2057](https\://github\.com/ansible\-collections/amazon\.aws/pull/2057)\)\.
* s3\_bucket\_info \- add parameter <code>bucket\_versioning</code> to return the versioning state of a bucket \([https\://github\.com/ansible\-collections/amazon\.aws/pull/1919](https\://github\.com/ansible\-collections/amazon\.aws/pull/1919)\)\.
* s3\_object \- removed unused code \([https\://github\.com/ansible\-collections/amazon\.aws/pull/1996](https\://github\.com/ansible\-collections/amazon\.aws/pull/1996)\)\.
* s3\_object\_info \- fix exception raised when listing objects from empty bucket \([https\://github\.com/ansible\-collections/amazon\.aws/pull/1919](https\://github\.com/ansible\-collections/amazon\.aws/pull/1919)\)\.

<a id="ansible-netcommon-2"></a>
#### ansible\.netcommon

* Add new module cli\_restore that exclusively handles restoring of backup configuration to target applaince\.

<a id="ansible-utils-1"></a>
#### ansible\.utils

* Add support in fact\_diff filter plugin to show common lines\.\([https\://github\.com/ansible\-collections/ansible\.utils/issues/311](https\://github\.com/ansible\-collections/ansible\.utils/issues/311)\)
* Fact\_diff filter plugin \- Add fact\_diff filter plugin\. \([https\://github\.com/ansible\-collections/ansible\.utils/issues/78](https\://github\.com/ansible\-collections/ansible\.utils/issues/78)\)\.

<a id="ansible-windows-4"></a>
#### ansible\.windows

* Set minimum supported Ansible version to 2\.14 to align with the versions still supported by Ansible\.
* win\_share \- Added a new param called <code>scope\_name</code> that allows file shares to be scoped for Windows Server failover cluster roles\.
* win\_uri \- Max depth for json object conversion used to be 2\. Can now send json objects with up to 20 levels of nesting

<a id="arista-eos-1"></a>
#### arista\.eos

* Add support for cli\_restore functionality\.
* Please refer the PR to know more about core changes \([https\://github\.com/ansible\-collections/ansible\.netcommon/pull/618](https\://github\.com/ansible\-collections/ansible\.netcommon/pull/618)\)\.
* cli\_restore module is part of netcommon\.

<a id="check-point-mgmt"></a>
#### check\_point\.mgmt

* New resource modules for R81\.20 JHF Take 43
* meta/runtime\.yml \- update minimum Ansible version required to 2\.14\.0\.

<a id="cisco-aci-2"></a>
#### cisco\.aci

* Add Authentification option for EIGRP interface profile\.
* Add L3out Floating SVI modules \(aci\_l3out\_floating\_svi\, aci\_l3out\_floating\_svi\_path\, aci\_l3out\_floating\_svi\_path\_secondary\_ip and aci\_l3out\_floating\_svi\_secondary\_ip\) \(\#478\)
* Add No\-verification flag option to reduce the number of API calls\. If true\, a verifying GET will not be sent after a POST update to APIC
* Add access spine interface selector and port block binding in aci\_access\_port\_block\_to\_access\_port
* Add aci\_access\_spine\_interface\_selector module
* Add aci\_action\_rule\_additional\_communities module
* Add aci\_action\_rule\_set\_as\_path and aci\_action\_rule\_set\_as\_path\_asn modules
* Add aci\_bgp\_peer\_prefix\_policy\, aci\_bgp\_route\_summarization\_policy and aci\_bgp\_address\_family\_context\_policy modules
* Add aci\_fabric\_pod\, aci\_fabric\_pod\_external\_tep\, aci\_fabric\_pod\_profile\, aci\_fabric\_pod\_remote\_pool modules \(\#558\)
* Add aci\_hsrp\_interface\_policy\, aci\_l3out\_hsrp\_group\, aci\_l3out\_hsrp\_interface\_profile and aci\_l3out\_hsrp\_secondary\_vip modules \(\#505\)
* Add aci\_interface\_policy\_eigrp \(class\:eigrpIfPol\) module
* Add aci\_interface\_policy\_pim module
* Add aci\_interface\_policy\_storm\_control module
* Add aci\_keychain\_policy and aci\_key\_policy modules
* Add aci\_l3out\_bfd\_multihop\_interface\_profile\, aci\_l3out\_bfd\_interface\_profile\, aci\_interface\_policy\_bfd\_multihop\, aci\_interface\_policy\_bfd and aci\_bfd\_multihop\_node\_policy modules \(\#492\)
* Add aci\_l3out\_dhcp\_relay\_label\, aci\_dhcp\_option\_policy and aci\_dhcp\_option modules
* Add aci\_l3out\_eigrp\_interface\_profile module
* Add aci\_listify filter plugin to flattens nested dictionaries
* Add aci\_netflow\_exporter\_policy module
* Add aci\_netflow\_monitor\_policy and aci\_netflow\_record\_policy modules
* Add aci\_netflow\_monitor\_to\_exporter module
* Add aci\_node\_block module
* Add aci\_pim\_route\_map\_policy and aci\_pim\_route\_map\_entry modules
* Add aci\_qos\_custom\_policy and aci\_qos\_dscp\_class modules
* Add aci\_qos\_dot1p\_class module
* Add action rules attributes to aci\_tenant\_action\_rule\_profile\.
* Add auto to speed attribute options in aci\_interface\_policy\_link\_level module \(\#577\)
* Add missing options to aci\_bd module
* Add modules aci\_bd\_to\_netflow\_monitor\_policy and aci\_bd\_rogue\_exception\_mac \(\#600\)
* Add modules for Fabric External Connection Policies and its childs
* Add option to set delimiter to  \_  in aci\_epg\_to\_domain module
* Add qos\_custom\_policy\, pim\_interface\_policy and igmp\_interface\_policy as new child\_classes for aci\_l3out\_logical\_interface\_profile\.
* Add support for annotation in aci\_rest module \(\#437\)
* Add support for block statements in useg attributes with the aci\_epg\_useg\_attribute\_block\_statement module
* Add support for configuration of access switch policy groups with aci\_access\_switch\_policy\_group module
* Add support for configuration of certificate authorities in aci\_aaa\_certificate\_authority
* Add support for configuration of fabric management access policies in aci\_fabric\_management\_access
* Add support for configuration of vrf multicast with aci\_vrf\_multicast module
* Add support for configuring Azure cloud subnets using the aci\_cloud\_subnet module
* Add support for encap scope in aci\_l3out\_interface
* Add support for https ssl cipher configuration in aci\_fabric\_management\_access\_https\_cipher
* Add support for infra l3out nodes bgp\-evpn loopback\, mpls transport loopback and segment id in aci\_l3out\_logical\_node
* Add support for infra sr mpls micro bfd in aci\_l3out\_interface
* Add support for intra epg\, taboo\, and contract interface in aci\_epg\_to\_contract
* Add support for key ring configuration in aci\_aaa\_key\_ring
* Add support for mac and description in aci\_l3out\_interface
* Add support for mpls custom qos policy for infra sr mpls l3outs node profiles in aci\_l3out\_logical\_node\_profile
* Add support for security default settings configuration in aci\_aaa\_security\_default\_settings
* Add support for simple statements in useg attributes with the aci\_epg\_useg\_attribute\_simple\_statement module
* Add support for sr\-mpls bgpInfraPeerP and bgp\_password in aci\_l3out\_bgp\_peer module \(\#543\)
* Add support for sr\-mpls in aci\_l3out module
* Add support for sr\-mpls l3out to infra l3out in aci\_l3out\_to\_sr\_mpls\_infra\_l3out
* Add support for subject labels for EPG\, EPG Contract\, ESG\, Contract Subject\, L2Out External EPG\, L3out External EPG\, and L3out External EPG Contract with the aci\_subject\_label module
* Add support for taboo contract\, contract interface and intra\_epg contract in aci\_l3out\_extepg\_to\_contract
* Add support for useg default block statement configuration for useg epg in aci\_epg
* Modify child class node block conditions to be optional in aci\_switch\_leaf\_selector

<a id="cisco-dnac-6"></a>
#### cisco\.dnac

* Added a method to validate IP addresses\.
* Added attributes \'dnac\_api\_task\_timeout\' and \'dnac\_task\_poll\_interval\' in intent and workflow\_manager modules\.
* Added the op\_modifies\=True when calling SDK APIs in the workflow manager modules\.
* Adding support to importing a template using JSON file
* Addressed image un\-tagging issues in inherited site settings\.
* Changes in discovery workflow manager modules  relating to different states of the discovery job
* Changes the minimum supported version from Ansible v2\.9\.10 to v2\.14\.0
* Corrected site creation issues in the site module when optional parameters are missing\.
* Fixed a minor issue in the site workflow manager module\.
* Fixed management IP updates for devices on SNMP version v2\.
* Introduced sample playbooks for the discovery module\.
* Provided documentation for EWLC templates in Cisco Catalyst Center version 2\.3\.7\.x\.
* Resolved a \'NoneType\' error in discovery module credentials\.
* Updating galaxy\.yml ansible\.utils dependencies\.
* inventory\_workflow\_manager \- Added attributes \'add\_user\_defined\_field\'\, \'update\_interface\_details\'\, \'export\_device\_list\' and \'admin\_status\'
* inventory\_workflow\_manager \- Removed attributes \'provision\_wireless\_device\'\, \'reprovision\_wired\_device\'

<a id="cisco-ios-1"></a>
#### cisco\.ios

* Add support for cli\_restore functionality\.
* Added ios\_evpn\_evi resource module\.
* Added ios\_evpn\_global resource module\.
* Added ios\_vxlan\_vtep resource module\.
* Fixed ios\_evpn\_evi resource module integration test failure \- code to remove VLAN config\.
* Please refer the PR to know more about core changes \([https\://github\.com/ansible\-collections/ansible\.netcommon/pull/618](https\://github\.com/ansible\-collections/ansible\.netcommon/pull/618)\)\.
* cli\_restore module is part of netcommon\.
* ios\_bgp\_address\_family \- Fixed an issue with inherit peer\-policy CLI
* ios\_bgp\_address\_family \- added \'advertise\' key
* ios\_bgp\_global \- added \'bgp\.default\.ipv4\_unicast\' and \'bgp\.default\.route\_target\.filter\' key
* ios\_l3\_interfaces \- added \'autostate\'\, \'mac\_address\'\, \'ipv4\.source\_interface\'\, and \'ipv6\.enable\' key
* ios\_vlans \- Add purged state to deal with toplevel vlan and vlan configuration config\.
* ios\_vlans \- added vlan config CLI feature\.
* ios\_vrf \- added MDT related keys

<a id="cisco-iosxr-1"></a>
#### cisco\.iosxr

* Add missing options in afi and safi in address\-family of bgp\_templates RM\.
* Add support for cli\_restore functionality\.
* Please refer the PR to know more about core changes \([https\://github\.com/ansible\-collections/ansible\.netcommon/pull/618](https\://github\.com/ansible\-collections/ansible\.netcommon/pull/618)\)\.
* cli\_restore module is part of netcommon\.
* iosxr\_facts \- Add cdp neighbors in ansible\_net\_neighbors dictionary \([https\://github\.com/ansible\-collections/cisco\.iosxr/pull/457](https\://github\.com/ansible\-collections/cisco\.iosxr/pull/457)\)\.

<a id="cisco-ise-4"></a>
#### cisco\.ise

* Changes the minimum supported version from Ansible v2\.9\.10 to v2\.14\.0
* Services included configuration\, edda\, dataconnect\_services\, subscriber\.
* cisco\.ise collection now supports ansible\.utils v3

<a id="cisco-meraki-2"></a>
#### cisco\.meraki

* Adding support to ansible\.utils \"\>\=2\.0\.0\, \<4\.00\"\.
* Ansible collection now support v1\.44\.1 of Dashboard Api\.
* Fixing problem of naming in <em class="title-reference">organizations\_appliance\_vpn\_third\_party\_vpnpeers\_info</em>\.
* Removing <em class="title-reference">state</em> from allowed parameters for <em class="title-reference">networks\_syslog\_servers</em> module\.
* The <em class="title-reference">id</em> parameter is change type to an <em class="title-reference">integer</em> in <em class="title-reference">networks\_appliance\_vlans</em> module\.
* The <em class="title-reference">id</em> parameter is now required for <em class="title-reference">networks\_appliance\_vlans</em> module\.
* administered\_licensing\_subscription\_entitlements\_info \- new plugin\.
* administered\_licensing\_subscription\_subscriptions\_bind \- new plugin\.
* administered\_licensing\_subscription\_subscriptions\_claim \- new plugin\.
* administered\_licensing\_subscription\_subscriptions\_claim\_key\_validate \- new plugin\.
* administered\_licensing\_subscription\_subscriptions\_compliance\_statuses\_info \- new plugin\.
* administered\_licensing\_subscription\_subscriptions\_info \- new plugin\.
* devices\_appliance\_radio\_settings \- new plugin\.
* devices\_appliance\_radio\_settings\_info \- new plugin\.
* devices\_live\_tools\_arp\_table \- new plugin\.
* devices\_live\_tools\_arp\_table\_info \- new plugin\.
* devices\_live\_tools\_cable\_test \- new plugin\.
* devices\_live\_tools\_cable\_test\_info \- new plugin\.
* devices\_live\_tools\_throughput\_test \- new plugin\.
* devices\_live\_tools\_throughput\_test\_info \- new plugin\.
* devices\_live\_tools\_wake\_on\_lan \- new plugin\.
* devices\_live\_tools\_wake\_on\_lan\_info \- new plugin\.
* devices\_wireless\_alternate\_management\_interface\_ipv6 \- new plugin\.
* networks\_appliance\_rf\_profiles \- new plugin\.
* networks\_appliance\_rf\_profiles\_info \- new plugin\.
* networks\_appliance\_traffic\_shaping\_vpn\_exclusions \- new plugin\.
* networks\_sm\_devices\_install\_apps \- new plugin\.
* networks\_sm\_devices\_reboot \- new plugin\.
* networks\_sm\_devices\_shutdown \- new plugin\.
* networks\_sm\_devices\_uninstall\_apps \- new plugin\.
* networks\_vlan\_profiles \- new plugin\.
* networks\_vlan\_profiles\_assignments\_by\_device\_info \- new plugin\.
* networks\_vlan\_profiles\_assignments\_reassign \- new plugin\.
* networks\_vlan\_profiles\_info \- new plugin\.
* networks\_wireless\_ethernet\_ports\_profiles \- new plugin\.
* networks\_wireless\_ethernet\_ports\_profiles\_assign \- new plugin\.
* networks\_wireless\_ethernet\_ports\_profiles\_info \- new plugin\.
* networks\_wireless\_ethernet\_ports\_profiles\_set\_default \- new plugin\.
* organizations\_appliance\_traffic\_shaping\_vpn\_exclusions\_by\_network\_info \- new plugin\.
* organizations\_appliance\_uplinks\_statuses\_overview\_info \- new plugin\.
* organizations\_appliance\_uplinks\_usage\_by\_network\_info \- new plugin\.
* organizations\_camera\_boundaries\_areas\_by\_device\_info \- new plugin\.
* organizations\_camera\_boundaries\_lines\_by\_device\_info \- new plugin\.
* organizations\_camera\_detections\_history\_by\_boundary\_by\_interval\_info \- new plugin\.
* organizations\_camera\_permissions\_info \- new plugin\.
* organizations\_camera\_roles \- new plugin\.
* organizations\_camera\_roles\_info \- new plugin\.
* organizations\_devices\_availabilities\_change\_history\_info \- new plugin\.
* organizations\_devices\_boots\_history\_info \- new plugin\.
* organizations\_sm\_admins\_roles \- new plugin\.
* organizations\_sm\_admins\_roles\_info \- new plugin\.
* organizations\_sm\_sentry\_policies\_assignments \- new plugin\.
* organizations\_sm\_sentry\_policies\_assignments\_by\_network\_info \- new plugin\.
* organizations\_summary\_top\_networks\_by\_status\_info \- new plugin\.
* organizations\_webhooks\_callbacks\_statuses\_info \- new plugin\.
* organizations\_wireless\_devices\_channel\_utilization\_by\_device\_info \- new plugin\.
* organizations\_wireless\_devices\_channel\_utilization\_by\_network\_info \- new plugin\.
* organizations\_wireless\_devices\_channel\_utilization\_history\_by\_device\_by\_interval\_info \- new plugin\.
* organizations\_wireless\_devices\_channel\_utilization\_history\_by\_network\_by\_interval\_info \- new plugin\.
* organizations\_wireless\_devices\_packet\_loss\_by\_client\_info \- new plugin\.
* organizations\_wireless\_devices\_packet\_loss\_by\_device\_info \- new plugin\.
* organizations\_wireless\_devices\_packet\_loss\_by\_network\_info \- new plugin\.

<a id="cisco-mso-4"></a>
#### cisco\.mso

* Add Azure Cloud site support to mso\_schema\_site\_contract\_service\_graph
* Add Azure Cloud site support to mso\_schema\_site\_service\_graph
* Add functionality to resolve same name in remote and local user\.
* Add l3out\_template and l3out\_schema arguments to mso\_schema\_site\_external\_epg \(\#394\)
* Add mso\_schema\_site\_contract\_service\_graph module to manage site contract service graph
* Add mso\_schema\_site\_contract\_service\_graph\_listener module to manage Azure site contract service graph listeners and update other modules
* Add new parameter remote\_user to add multiple remote users associated with multiple login domains
* Add support for replacing all existing contracts with new provided contracts in a single operation with one request and adding/removing multiple contracts in multiple operations with a single request in mso\_schema\_template\_anp\_epg\_contract module
* Add support for replacing all existing static ports with new provided static ports in a single operation with one request and adding/removing multiple static ports in multiple operations with a single request in mso\_schema\_template\_anp\_epg\_staticport module
* Add support for required attributes introduced in NDO 4\.2 for mso\_schema\_site\_anp\_epg\_domain
* Support for creation of schemas without templates with the mso\_schema module

<a id="cisco-nxos-3"></a>
#### cisco\.nxos

* Add support for cli\_restore functionality\.
* Please refer the PR to know more about core changes \([https\://github\.com/ansible\-collections/ansible\.netcommon/pull/618](https\://github\.com/ansible\-collections/ansible\.netcommon/pull/618)\)\. The cli\_restore module is a part of ansible\.netcommon\.
* nxos\_config \- Relax restrictions on I\(src\) parameter so it can be used more like I\(lines\)\. \([https\://github\.com/ansible\-collections/cisco\.nxos/issues/89](https\://github\.com/ansible\-collections/cisco\.nxos/issues/89)\)\.

<a id="community-aws"></a>
#### community\.aws

* api\_gateway \- use fstrings where appropriate \([https\://github\.com/ansible\-collections/amazon\.aws/pull/1962](https\://github\.com/ansible\-collections/amazon\.aws/pull/1962)\)\.
* api\_gateway\_info \- use fstrings where appropriate \([https\://github\.com/ansible\-collections/amazon\.aws/pull/1962](https\://github\.com/ansible\-collections/amazon\.aws/pull/1962)\)\.
* aws\_ssm \- Updated the documentation to explicitly state that an S3 bucket is required\, the behavior of the files in that bucket\, and requirements around that\. \([https\://github\.com/ansible\-collections/community\.aws/issues/1775](https\://github\.com/ansible\-collections/community\.aws/issues/1775)\)\.
* cloudfront\_distribution \- added support for <code>cache\_policy\_id</code> and <code>origin\_request\_policy\_id</code> for behaviors \([https\://github\.com/ansible\-collections/community\.aws/pull/1589](https\://github\.com/ansible\-collections/community\.aws/pull/1589)\)
* community\.aws collection \- apply isort code formatting to ensure consistent formatting of code \([https\://github\.com/ansible\-collections/community\.aws/pull/1962](https\://github\.com/ansible\-collections/community\.aws/pull/1962)\)
* ecs\_taskdefinition \- Add parameter <code>runtime\_platform</code> \([https\://github\.com/ansible\-collections/community\.aws/issues/1891](https\://github\.com/ansible\-collections/community\.aws/issues/1891)\)\.
* eks\_nodegroup \- ensure wait also waits for deletion to complete when <code>wait\=\=True</code> \([https\://github\.com/ansible\-collections/community\.aws/pull/1994](https\://github\.com/ansible\-collections/community\.aws/pull/1994)\)\.
* elb\_network\_lb \- add support for Application\-Layer Protocol Negotiation \(ALPN\) policy <code>AlpnPolicy</code> for TLS listeners \([https\://github\.com/ansible\-collections/community\.aws/issues/1566](https\://github\.com/ansible\-collections/community\.aws/issues/1566)\)\.
* elb\_network\_lb \- add the possibly to update <code>SslPolicy</code> and <code>Certificates</code> for TLS listeners \(\)\.
* glue\_job \- add support for 2 new instance types which are G\.4X and G\.8X \([https\://github\.com/ansible\-collections/community\.aws/pull/2048](https\://github\.com/ansible\-collections/community\.aws/pull/2048)\)\.
* mq\_broker \- add support to wait for broker state via <code>wait</code> and <code>wait\_timeout</code> parameter values \([https\://github\.com/ansible\-collections/community\.aws/pull/1879](https\://github\.com/ansible\-collections/community\.aws/pull/1879)\)\.
* msk\_cluster \- Support for additional <code>m5</code> and <code>m7g</code> types of MSK clusters \([https\://github\.com/ansible\-collections/community\.aws/pull/1947](https\://github\.com/ansible\-collections/community\.aws/pull/1947)\)\.

<a id="community-ciscosmb"></a>
#### community\.ciscosmb

* added additional attribute \- add interface \'bandwidth\' attribute
* docs \- addeed info about SG\-250 support and testing
* reverted attribute change \- keep interface \'bandwith\' attribute

<a id="community-crypto-5"></a>
#### community\.crypto

* When using cryptography \>\= 42\.0\.0\, use offset\-aware <code>datetime\.datetime</code> objects \(with timezone UTC\) instead of offset\-naive UTC timestamps \([https\://github\.com/ansible\-collections/community\.crypto/issues/726](https\://github\.com/ansible\-collections/community\.crypto/issues/726)\, [https\://github\.com/ansible\-collections/community\.crypto/pull/727](https\://github\.com/ansible\-collections/community\.crypto/pull/727)\)\.
* acme\_certificate \- add <code>include\_renewal\_cert\_id</code> option to allow requesting renewal of a specific certificate according to the current ACME Renewal Information specification draft \([https\://github\.com/ansible\-collections/community\.crypto/pull/739](https\://github\.com/ansible\-collections/community\.crypto/pull/739)\)\.
* luks\_device \- add allow discards option \([https\://github\.com/ansible\-collections/community\.crypto/pull/693](https\://github\.com/ansible\-collections/community\.crypto/pull/693)\)\.
* openssh\_cert \- avoid UTC functions deprecated in Python 3\.12 when using Python 3 \([https\://github\.com/ansible\-collections/community\.crypto/pull/727](https\://github\.com/ansible\-collections/community\.crypto/pull/727)\)\.
* x509\_crl \- the new option <code>serial\_numbers</code> allow to configure in which format serial numbers can be provided to <code>revoked\_certificates\[\]\.serial\_number</code>\. The default is as integers \(<code>serial\_numbers\=integer</code>\) for backwards compatibility\; setting <code>serial\_numbers\=hex\-octets</code> allows to specify colon\-separated hex octet strings like <code>00\:11\:22\:FF</code> \([https\://github\.com/ansible\-collections/community\.crypto/issues/687](https\://github\.com/ansible\-collections/community\.crypto/issues/687)\, [https\://github\.com/ansible\-collections/community\.crypto/pull/715](https\://github\.com/ansible\-collections/community\.crypto/pull/715)\)\.

<a id="community-digitalocean"></a>
#### community\.digitalocean

* digital\_ocean\_kubernetes \- add project\_name parameter \([https\://github\.com/ansible\-collections/community\.digitalocean/issues/264](https\://github\.com/ansible\-collections/community\.digitalocean/issues/264)\)\.
* fix sanity tests \([https\://github\.com/ansible\-collections/community\.digitalocean/issues/323](https\://github\.com/ansible\-collections/community\.digitalocean/issues/323)\)\.

<a id="community-dns-9"></a>
#### community\.dns

* hetzner\_dns\_records and hosttech\_dns\_records inventory plugins \- the <code>filters</code> option has been renamed to <code>simple\_filters</code>\. The old name still works until community\.hrobot 2\.0\.0\. Then it will change to allow more complex filtering with the <code>community\.library\_inventory\_filtering\_v1</code> collection\'s functionality \([https\://github\.com/ansible\-collections/community\.dns/pull/181](https\://github\.com/ansible\-collections/community\.dns/pull/181)\)\.
* inventory plugins \- add <code>filter</code> option which allows to include and exclude hosts based on Jinja2 conditions \([https\://github\.com/ansible\-collections/community\.dns/pull/196](https\://github\.com/ansible\-collections/community\.dns/pull/196)\)\.
* lookup\, lookup\_as\_dict \- it is now possible to configure whether the input should be treated as an absolute domain name \(<code>search\=false</code>\)\, or potentially as a relative domain name \(<code>search\=true</code>\)  \([https\://github\.com/ansible\-collections/community\.dns/issues/200](https\://github\.com/ansible\-collections/community\.dns/issues/200)\, [https\://github\.com/ansible\-collections/community\.dns/pull/201](https\://github\.com/ansible\-collections/community\.dns/pull/201)\)\.
* nameserver\_info and nameserver\_record\_info \- add <code>server</code> parameter to specify custom DNS servers \([https\://github\.com/ansible\-collections/community\.dns/pull/168](https\://github\.com/ansible\-collections/community\.dns/pull/168)\, [https\://github\.com/ansible\-collections/community\.dns/pull/178](https\://github\.com/ansible\-collections/community\.dns/pull/178)\)\.
* wait\_for\_txt \- add <code>server</code> parameter to specify custom DNS servers \([https\://github\.com/ansible\-collections/community\.dns/pull/178](https\://github\.com/ansible\-collections/community\.dns/pull/178)\)\.

<a id="community-docker-12"></a>
#### community\.docker

* The EE requirements now include PyYAML\, since the <code>docker\_compose\_v2\*</code> modules depend on it when the <code>definition</code> option is used\. This should not have a noticable effect on generated EEs since ansible\-core itself depends on PyYAML as well\, and ansible\-builder explicitly ignores this dependency \([https\://github\.com/ansible\-collections/community\.docker/pull/832](https\://github\.com/ansible\-collections/community\.docker/pull/832)\)\.
* The <code>ca\_cert</code> option available to almost all modules and plugins has been renamed to <code>ca\_path</code>\. The name <code>ca\_path</code> is also used for similar options in ansible\-core and other collections\. The old name has been added as an alias and can still be used \([https\://github\.com/ansible\-collections/community\.docker/pull/744](https\://github\.com/ansible\-collections/community\.docker/pull/744)\)\.
* The <code>docker\_stack\*</code> modules now use the common CLI\-based module code added for the <code>docker\_image\_build</code> and <code>docker\_compose\_v2</code> modules\. This means that the modules now have various more configuration options with respect to talking to the Docker Daemon\, and now also are part of the <code>community\.docker\.docker</code> and <code>docker</code> module default groups \([https\://github\.com/ansible\-collections/community\.docker/pull/745](https\://github\.com/ansible\-collections/community\.docker/pull/745)\)\.
* docker\_compose\_v2 \- add <code>scale</code> option to allow to explicitly scale services \([https\://github\.com/ansible\-collections/community\.docker/pull/776](https\://github\.com/ansible\-collections/community\.docker/pull/776)\)\.
* docker\_compose\_v2 \- allow to wait until containers are running/health when running <code>docker compose up</code> with the new <code>wait</code> option \([https\://github\.com/ansible\-collections/community\.docker/issues/794](https\://github\.com/ansible\-collections/community\.docker/issues/794)\, [https\://github\.com/ansible\-collections/community\.docker/pull/796](https\://github\.com/ansible\-collections/community\.docker/pull/796)\)\.
* docker\_compose\_v2\* \- the new option <code>check\_files\_existing</code> allows to disable the check for one of the files <code>compose\.yaml</code>\, <code>compose\.yml</code>\, <code>docker\-compose\.yaml</code>\, and <code>docker\-compose\.yml</code> in <code>project\_src</code> if <code>files</code> is not specified\. This is necessary if a non\-standard compose filename is specified through other means\, like the <code>COMPOSE\_FILE</code> environment variable \([https\://github\.com/ansible\-collections/community\.docker/issues/838](https\://github\.com/ansible\-collections/community\.docker/issues/838)\, [https\://github\.com/ansible\-collections/community\.docker/pull/839](https\://github\.com/ansible\-collections/community\.docker/pull/839)\)\.
* docker\_compose\_v2\* modules \- allow to provide an inline definition of the compose content instead of having to provide a <code>project\_src</code> directory with the compose file written into it \([https\://github\.com/ansible\-collections/community\.docker/issues/829](https\://github\.com/ansible\-collections/community\.docker/issues/829)\, [https\://github\.com/ansible\-collections/community\.docker/pull/832](https\://github\.com/ansible\-collections/community\.docker/pull/832)\)\.
* docker\_compose\_v2\, docker\_compose\_v2\_pull \- support <code>files</code> parameter to specify multiple Compose files \([https\://github\.com/ansible\-collections/community\.docker/issues/772](https\://github\.com/ansible\-collections/community\.docker/issues/772)\, [https\://github\.com/ansible\-collections/community\.docker/pull/775](https\://github\.com/ansible\-collections/community\.docker/pull/775)\)\.
* docker\_container \- add <code>networks\[\]\.mac\_address</code> option for Docker API 1\.44\+\. Note that Docker API 1\.44 no longer uses the global <code>mac\_address</code> option\, this new option is the only way to set the MAC address for a container \([https\://github\.com/ansible\-collections/community\.docker/pull/763](https\://github\.com/ansible\-collections/community\.docker/pull/763)\)\.
* docker\_container \- adds <code>healthcheck\.start\_interval</code> to support healthcheck start interval setting on containers \([https\://github\.com/ansible\-collections/community\.docker/pull/848](https\://github\.com/ansible\-collections/community\.docker/pull/848)\)\.
* docker\_container \- adds <code>healthcheck\.test\_cli\_compatible</code> to allow omit test option on containers without remove existing image test \([https\://github\.com/ansible\-collections/community\.docker/pull/847](https\://github\.com/ansible\-collections/community\.docker/pull/847)\)\.
* docker\_container \- implement better <code>platform</code> string comparisons to improve idempotency \([https\://github\.com/ansible\-collections/community\.docker/issues/654](https\://github\.com/ansible\-collections/community\.docker/issues/654)\, [https\://github\.com/ansible\-collections/community\.docker/pull/705](https\://github\.com/ansible\-collections/community\.docker/pull/705)\)\.
* docker\_container \- internal refactorings which allow comparisons to use more information like details of the current image or the Docker host config \([https\://github\.com/ansible\-collections/community\.docker/pull/713](https\://github\.com/ansible\-collections/community\.docker/pull/713)\)\.
* docker\_container \- the <code>pull\_check\_mode\_behavior</code> option now allows to control the module\'s behavior in check mode when <code>pull\=always</code> \([https\://github\.com/ansible\-collections/community\.docker/issues/792](https\://github\.com/ansible\-collections/community\.docker/issues/792)\, [https\://github\.com/ansible\-collections/community\.docker/pull/797](https\://github\.com/ansible\-collections/community\.docker/pull/797)\)\.
* docker\_container \- the <code>pull</code> option now accepts the three values <code>never</code>\, <code>missing\_image</code> \(default\)\, and <code>never</code>\, next to the previously valid values <code>true</code> \(equivalent to <code>always</code>\) and <code>false</code> \(equivalent to <code>missing\_image</code>\)\. This allows the equivalent to <code>\-\-pull\=never</code> from the Docker command line \([https\://github\.com/ansible\-collections/community\.docker/issues/783](https\://github\.com/ansible\-collections/community\.docker/issues/783)\, [https\://github\.com/ansible\-collections/community\.docker/pull/797](https\://github\.com/ansible\-collections/community\.docker/pull/797)\)\.
* docker\_image \- allow to specify labels and <code>/dev/shm</code> size when building images \([https\://github\.com/ansible\-collections/community\.docker/issues/726](https\://github\.com/ansible\-collections/community\.docker/issues/726)\, [https\://github\.com/ansible\-collections/community\.docker/pull/727](https\://github\.com/ansible\-collections/community\.docker/pull/727)\)\.
* docker\_image \- allow to specify memory size and swap memory size in other units than bytes \([https\://github\.com/ansible\-collections/community\.docker/pull/727](https\://github\.com/ansible\-collections/community\.docker/pull/727)\)\.
* docker\_image\_build \- add <code>outputs</code> option to allow configuring outputs for the build \([https\://github\.com/ansible\-collections/community\.docker/pull/852](https\://github\.com/ansible\-collections/community\.docker/pull/852)\)\.
* docker\_image\_build \- add <code>secrets</code> option to allow passing secrets to the build \([https\://github\.com/ansible\-collections/community\.docker/pull/852](https\://github\.com/ansible\-collections/community\.docker/pull/852)\)\.
* docker\_image\_build \- allow <code>platform</code> to be a list of platforms instead of only a single platform for multi\-platform builds \([https\://github\.com/ansible\-collections/community\.docker/pull/852](https\://github\.com/ansible\-collections/community\.docker/pull/852)\)\.
* docker\_network \- adds <code>config\_only</code> and <code>config\_from</code> to support creating and using config only networks \([https\://github\.com/ansible\-collections/community\.docker/issues/395](https\://github\.com/ansible\-collections/community\.docker/issues/395)\)\.
* docker\_prune \- add new options <code>builder\_cache\_all</code>\, <code>builder\_cache\_filters</code>\, and <code>builder\_cache\_keep\_storage</code>\, and a new return value <code>builder\_cache\_caches\_deleted</code> for pruning build caches \([https\://github\.com/ansible\-collections/community\.docker/issues/844](https\://github\.com/ansible\-collections/community\.docker/issues/844)\, [https\://github\.com/ansible\-collections/community\.docker/issues/845](https\://github\.com/ansible\-collections/community\.docker/issues/845)\)\.
* docker\_swarm\_service \- adds <code>sysctls</code> to support sysctl settings on swarm services \([https\://github\.com/ansible\-collections/community\.docker/issues/190](https\://github\.com/ansible\-collections/community\.docker/issues/190)\)\.
* inventory plugins \- add <code>filter</code> option which allows to include and exclude hosts based on Jinja2 conditions \([https\://github\.com/ansible\-collections/community\.docker/pull/698](https\://github\.com/ansible\-collections/community\.docker/pull/698)\, [https\://github\.com/ansible\-collections/community\.docker/issues/610](https\://github\.com/ansible\-collections/community\.docker/issues/610)\)\.
* vendored Docker SDK for Python \- remove unused code that relies on functionality deprecated in Python 3\.12 \([https\://github\.com/ansible\-collections/community\.docker/pull/834](https\://github\.com/ansible\-collections/community\.docker/pull/834)\)\.

<a id="community-general-22"></a>
#### community\.general

* PythonRunner module utils \- specialisation of <code>CmdRunner</code> to execute Python scripts \([https\://github\.com/ansible\-collections/community\.general/pull/8289](https\://github\.com/ansible\-collections/community\.general/pull/8289)\)\.
* Use offset\-aware <code>datetime\.datetime</code> objects \(with timezone UTC\) instead of offset\-naive UTC timestamps\, which are deprecated in Python 3\.12 \([https\://github\.com/ansible\-collections/community\.general/pull/8222](https\://github\.com/ansible\-collections/community\.general/pull/8222)\)\.
* aix\_lvol \- refactor module to pass list of arguments to <code>module\.run\_command\(\)</code> instead of relying on interpretation by a shell \([https\://github\.com/ansible\-collections/community\.general/pull/8264](https\://github\.com/ansible\-collections/community\.general/pull/8264)\)\.
* ansible\_galaxy\_install \- minor refactor in the module \([https\://github\.com/ansible\-collections/community\.general/pull/8413](https\://github\.com/ansible\-collections/community\.general/pull/8413)\)\.
* apt\_rpm \- add new states <code>latest</code> and <code>present\_not\_latest</code>\. The value <code>latest</code> is equivalent to the current behavior of <code>present</code>\, which will upgrade a package if a newer version exists\. <code>present\_not\_latest</code> does what most users would expect <code>present</code> to do\: it does not upgrade if the package is already installed\. The current behavior of <code>present</code> will be deprecated in a later version\, and eventually changed to that of <code>present\_not\_latest</code> \([https\://github\.com/ansible\-collections/community\.general/issues/8217](https\://github\.com/ansible\-collections/community\.general/issues/8217)\, [https\://github\.com/ansible\-collections/community\.general/pull/8247](https\://github\.com/ansible\-collections/community\.general/pull/8247)\)\.
* apt\_rpm \- refactor module to pass list of arguments to <code>module\.run\_command\(\)</code> instead of relying on interpretation by a shell \([https\://github\.com/ansible\-collections/community\.general/pull/8264](https\://github\.com/ansible\-collections/community\.general/pull/8264)\)\.
* bitwarden lookup plugin \- add <code>bw\_session</code> option\, to pass session key instead of reading from env \([https\://github\.com/ansible\-collections/community\.general/pull/7994](https\://github\.com/ansible\-collections/community\.general/pull/7994)\)\.
* bitwarden lookup plugin \- add support to filter by organization ID \([https\://github\.com/ansible\-collections/community\.general/pull/8188](https\://github\.com/ansible\-collections/community\.general/pull/8188)\)\.
* bitwarden lookup plugin \- allows to fetch all records of a given collection ID\, by allowing to pass an empty value for <code>search\_value</code> when <code>collection\_id</code> is provided \([https\://github\.com/ansible\-collections/community\.general/pull/8013](https\://github\.com/ansible\-collections/community\.general/pull/8013)\)\.
* bitwarden lookup plugin \- when looking for items using an item ID\, the item is now accessed directly with <code>bw get item</code> instead of searching through all items\. This doubles the lookup speed \([https\://github\.com/ansible\-collections/community\.general/pull/7468](https\://github\.com/ansible\-collections/community\.general/pull/7468)\)\.
* btrfs\_subvolume \- refactor module to pass list of arguments to <code>module\.run\_command\(\)</code> instead of relying on interpretation by a shell \([https\://github\.com/ansible\-collections/community\.general/pull/8264](https\://github\.com/ansible\-collections/community\.general/pull/8264)\)\.
* cmd\_runner module\_utils \- add validation for minimum and maximum length in the value passed to <code>cmd\_runner\_fmt\.as\_list\(\)</code> \([https\://github\.com/ansible\-collections/community\.general/pull/8288](https\://github\.com/ansible\-collections/community\.general/pull/8288)\)\.
* consul\_auth\_method\, consul\_binding\_rule\, consul\_policy\, consul\_role\, consul\_session\, consul\_token \- added action group <code>community\.general\.consul</code> \([https\://github\.com/ansible\-collections/community\.general/pull/7897](https\://github\.com/ansible\-collections/community\.general/pull/7897)\)\.
* consul\_policy \- added support for diff and check mode \([https\://github\.com/ansible\-collections/community\.general/pull/7878](https\://github\.com/ansible\-collections/community\.general/pull/7878)\)\.
* consul\_policy\, consul\_role\, consul\_session \- removed dependency on <code>requests</code> and factored out common parts \([https\://github\.com/ansible\-collections/community\.general/pull/7826](https\://github\.com/ansible\-collections/community\.general/pull/7826)\, [https\://github\.com/ansible\-collections/community\.general/pull/7878](https\://github\.com/ansible\-collections/community\.general/pull/7878)\)\.
* consul\_role \- <code>node\_identities</code> now expects a <code>node\_name</code> option to match the Consul API\, the old <code>name</code> is still supported as alias \([https\://github\.com/ansible\-collections/community\.general/pull/7878](https\://github\.com/ansible\-collections/community\.general/pull/7878)\)\.
* consul\_role \- <code>service\_identities</code> now expects a <code>service\_name</code> option to match the Consul API\, the old <code>name</code> is still supported as alias \([https\://github\.com/ansible\-collections/community\.general/pull/7878](https\://github\.com/ansible\-collections/community\.general/pull/7878)\)\.
* consul\_role \- added support for diff mode \([https\://github\.com/ansible\-collections/community\.general/pull/7878](https\://github\.com/ansible\-collections/community\.general/pull/7878)\)\.
* consul\_role \- added support for templated policies \([https\://github\.com/ansible\-collections/community\.general/pull/7878](https\://github\.com/ansible\-collections/community\.general/pull/7878)\)\.
* elastic callback plugin \- close elastic client to not leak resources \([https\://github\.com/ansible\-collections/community\.general/pull/7517](https\://github\.com/ansible\-collections/community\.general/pull/7517)\)\.
* filesystem \- add bcachefs support \([https\://github\.com/ansible\-collections/community\.general/pull/8126](https\://github\.com/ansible\-collections/community\.general/pull/8126)\)\.
* gandi\_livedns \- adds support for personal access tokens \([https\://github\.com/ansible\-collections/community\.general/issues/7639](https\://github\.com/ansible\-collections/community\.general/issues/7639)\, [https\://github\.com/ansible\-collections/community\.general/pull/8337](https\://github\.com/ansible\-collections/community\.general/pull/8337)\)\.
* gconftool2 \- use <code>ModuleHelper</code> with <code>VarDict</code> \([https\://github\.com/ansible\-collections/community\.general/pull/8226](https\://github\.com/ansible\-collections/community\.general/pull/8226)\)\.
* git\_config \- allow multiple git configs for the same name with the new <code>add\_mode</code> option \([https\://github\.com/ansible\-collections/community\.general/pull/7260](https\://github\.com/ansible\-collections/community\.general/pull/7260)\)\.
* git\_config \- the <code>after</code> and <code>before</code> fields in the <code>diff</code> of the return value can be a list instead of a string in case more configs with the same key are affected \([https\://github\.com/ansible\-collections/community\.general/pull/7260](https\://github\.com/ansible\-collections/community\.general/pull/7260)\)\.
* git\_config \- when a value is unset\, all configs with the same key are unset \([https\://github\.com/ansible\-collections/community\.general/pull/7260](https\://github\.com/ansible\-collections/community\.general/pull/7260)\)\.
* gitlab modules \- add <code>ca\_path</code> option \([https\://github\.com/ansible\-collections/community\.general/pull/7472](https\://github\.com/ansible\-collections/community\.general/pull/7472)\)\.
* gitlab modules \- remove duplicate <code>gitlab</code> package check \([https\://github\.com/ansible\-collections/community\.general/pull/7486](https\://github\.com/ansible\-collections/community\.general/pull/7486)\)\.
* gitlab\_deploy\_key\, gitlab\_group\_members\, gitlab\_group\_variable\, gitlab\_hook\, gitlab\_instance\_variable\, gitlab\_project\_badge\, gitlab\_project\_variable\, gitlab\_user \- improve API pagination and compatibility with different versions of <code>python\-gitlab</code> \([https\://github\.com/ansible\-collections/community\.general/pull/7790](https\://github\.com/ansible\-collections/community\.general/pull/7790)\)\.
* gitlab\_hook \- adds <code>releases\_events</code> parameter for supporting Releases events triggers on GitLab hooks \([https\://github\.com/ansible\-collections/community\.general/pull/7956](https\://github\.com/ansible\-collections/community\.general/pull/7956)\)\.
* gitlab\_runner \- add support for new runner creation workflow \([https\://github\.com/ansible\-collections/community\.general/pull/7199](https\://github\.com/ansible\-collections/community\.general/pull/7199)\)\.
* homebrew \- adds <code>force\_formula</code> parameter to disambiguate a formula from a cask of the same name \([https\://github\.com/ansible\-collections/community\.general/issues/8274](https\://github\.com/ansible\-collections/community\.general/issues/8274)\)\.
* homebrew\, homebrew\_cask \- refactor common argument validation logic into a dedicated <code>homebrew</code> module utils \([https\://github\.com/ansible\-collections/community\.general/issues/8323](https\://github\.com/ansible\-collections/community\.general/issues/8323)\, [https\://github\.com/ansible\-collections/community\.general/pull/8324](https\://github\.com/ansible\-collections/community\.general/pull/8324)\)\.
* icinga2 inventory plugin \- add Jinja2 templating support to <code>url</code>\, <code>user</code>\, and <code>password</code> paramenters \([https\://github\.com/ansible\-collections/community\.general/issues/7074](https\://github\.com/ansible\-collections/community\.general/issues/7074)\, [https\://github\.com/ansible\-collections/community\.general/pull/7996](https\://github\.com/ansible\-collections/community\.general/pull/7996)\)\.
* icinga2 inventory plugin \- adds new parameter <code>group\_by\_hostgroups</code> in order to make grouping by Icinga2 hostgroups optional \([https\://github\.com/ansible\-collections/community\.general/pull/7998](https\://github\.com/ansible\-collections/community\.general/pull/7998)\)\.
* ini\_file \- add an optional parameter <code>section\_has\_values</code>\. If the target ini file contains more than one <code>section</code>\, use <code>section\_has\_values</code> to specify which one should be updated \([https\://github\.com/ansible\-collections/community\.general/pull/7505](https\://github\.com/ansible\-collections/community\.general/pull/7505)\)\.
* ini\_file \- support optional spaces between section names and their surrounding brackets \([https\://github\.com/ansible\-collections/community\.general/pull/8075](https\://github\.com/ansible\-collections/community\.general/pull/8075)\)\.
* installp \- refactor module to pass list of arguments to <code>module\.run\_command\(\)</code> instead of relying on interpretation by a shell \([https\://github\.com/ansible\-collections/community\.general/pull/8264](https\://github\.com/ansible\-collections/community\.general/pull/8264)\)\.
* ipa\_config \- adds <code>passkey</code> choice to <code>ipauserauthtype</code> parameter\'s choices \([https\://github\.com/ansible\-collections/community\.general/pull/7588](https\://github\.com/ansible\-collections/community\.general/pull/7588)\)\.
* ipa\_dnsrecord \- adds ability to manage NS record types \([https\://github\.com/ansible\-collections/community\.general/pull/7737](https\://github\.com/ansible\-collections/community\.general/pull/7737)\)\.
* ipa\_pwpolicy \- refactor module and exchange a sequence <code>if</code> statements with a <code>for</code> loop \([https\://github\.com/ansible\-collections/community\.general/pull/7723](https\://github\.com/ansible\-collections/community\.general/pull/7723)\)\.
* ipa\_pwpolicy \- update module to support <code>maxrepeat</code>\, <code>maxsequence</code>\, <code>dictcheck</code>\, <code>usercheck</code>\, <code>gracelimit</code> parameters in FreeIPA password policies \([https\://github\.com/ansible\-collections/community\.general/pull/7723](https\://github\.com/ansible\-collections/community\.general/pull/7723)\)\.
* ipa\_sudorule \- adds options to include denied commands or command groups \([https\://github\.com/ansible\-collections/community\.general/pull/7415](https\://github\.com/ansible\-collections/community\.general/pull/7415)\)\.
* ipa\_user \- adds <code>idp</code> and <code>passkey</code> choice to <code>ipauserauthtype</code> parameter\'s choices \([https\://github\.com/ansible\-collections/community\.general/pull/7589](https\://github\.com/ansible\-collections/community\.general/pull/7589)\)\.
* irc \- add <code>validate\_certs</code> option\, and rename <code>use\_ssl</code> to <code>use\_tls</code>\, while keeping <code>use\_ssl</code> as an alias\. The default value for <code>validate\_certs</code> is <code>false</code> for backwards compatibility\. We recommend to every user of this module to explicitly set <code>use\_tls\=true</code> and <em class="title-reference">validate\_certs\=true\`</em> whenever possible\, especially when communicating to IRC servers over the internet \([https\://github\.com/ansible\-collections/community\.general/pull/7550](https\://github\.com/ansible\-collections/community\.general/pull/7550)\)\.
* java\_cert \- add <code>cert\_content</code> argument \([https\://github\.com/ansible\-collections/community\.general/pull/8153](https\://github\.com/ansible\-collections/community\.general/pull/8153)\)\.
* java\_cert \- enable <code>owner</code>\, <code>group</code>\, <code>mode</code>\, and other generic file arguments \([https\://github\.com/ansible\-collections/community\.general/pull/8116](https\://github\.com/ansible\-collections/community\.general/pull/8116)\)\.
* kernel\_blacklist \- use <code>ModuleHelper</code> with <code>VarDict</code> \([https\://github\.com/ansible\-collections/community\.general/pull/8226](https\://github\.com/ansible\-collections/community\.general/pull/8226)\)\.
* keycloak module utils \- expose error message from Keycloak server for HTTP errors in some specific situations \([https\://github\.com/ansible\-collections/community\.general/pull/7645](https\://github\.com/ansible\-collections/community\.general/pull/7645)\)\.
* keycloak\_client\, keycloak\_clientscope\, keycloak\_clienttemplate \- added <code>docker\-v2</code> protocol support\, enhancing alignment with Keycloak\'s protocol options \([https\://github\.com/ansible\-collections/community\.general/issues/8215](https\://github\.com/ansible\-collections/community\.general/issues/8215)\, [https\://github\.com/ansible\-collections/community\.general/pull/8216](https\://github\.com/ansible\-collections/community\.general/pull/8216)\)\.
* keycloak\_realm\_key \- the <code>config\.algorithm</code> option now supports 8 additional key algorithms \([https\://github\.com/ansible\-collections/community\.general/pull/7698](https\://github\.com/ansible\-collections/community\.general/pull/7698)\)\.
* keycloak\_realm\_key \- the <code>config\.certificate</code> option value is no longer defined with <code>no\_log\=True</code> \([https\://github\.com/ansible\-collections/community\.general/pull/7698](https\://github\.com/ansible\-collections/community\.general/pull/7698)\)\.
* keycloak\_realm\_key \- the <code>provider\_id</code> option now supports RSA encryption key usage \(value <code>rsa\-enc</code>\) \([https\://github\.com/ansible\-collections/community\.general/pull/7698](https\://github\.com/ansible\-collections/community\.general/pull/7698)\)\.
* keycloak\_user\_federation \- add option for <code>krbPrincipalAttribute</code> \([https\://github\.com/ansible\-collections/community\.general/pull/7538](https\://github\.com/ansible\-collections/community\.general/pull/7538)\)\.
* keycloak\_user\_federation \- allow custom user storage providers to be set through <code>provider\_id</code> \([https\://github\.com/ansible\-collections/community\.general/pull/7789](https\://github\.com/ansible\-collections/community\.general/pull/7789)\)\.
* ldap\_attrs \- module now supports diff mode\, showing which attributes are changed within an operation \([https\://github\.com/ansible\-collections/community\.general/pull/8073](https\://github\.com/ansible\-collections/community\.general/pull/8073)\)\.
* lvg \- refactor module to pass list of arguments to <code>module\.run\_command\(\)</code> instead of relying on interpretation by a shell \([https\://github\.com/ansible\-collections/community\.general/pull/8264](https\://github\.com/ansible\-collections/community\.general/pull/8264)\)\.
* lvol \- change <code>pvs</code> argument type to list of strings \([https\://github\.com/ansible\-collections/community\.general/pull/7676](https\://github\.com/ansible\-collections/community\.general/pull/7676)\, [https\://github\.com/ansible\-collections/community\.general/issues/7504](https\://github\.com/ansible\-collections/community\.general/issues/7504)\)\.
* lvol \- refactor module to pass list of arguments to <code>module\.run\_command\(\)</code> instead of relying on interpretation by a shell \([https\://github\.com/ansible\-collections/community\.general/pull/8264](https\://github\.com/ansible\-collections/community\.general/pull/8264)\)\.
* lxd connection plugin \- tighten the detection logic for lxd <code>Instance not found</code> errors\, to avoid false detection on unrelated errors such as <code>/usr/bin/python3\: not found</code> \([https\://github\.com/ansible\-collections/community\.general/pull/7521](https\://github\.com/ansible\-collections/community\.general/pull/7521)\)\.
* lxd\_container \- uses <code>/1\.0/instances</code> API endpoint\, if available\. Falls back to <code>/1\.0/containers</code> or <code>/1\.0/virtual\-machines</code>\. Fixes issue when using Incus or LXD 5\.19 due to migrating to <code>/1\.0/instances</code> endpoint \([https\://github\.com/ansible\-collections/community\.general/pull/7980](https\://github\.com/ansible\-collections/community\.general/pull/7980)\)\.
* macports \- refactor module to pass list of arguments to <code>module\.run\_command\(\)</code> instead of relying on interpretation by a shell \([https\://github\.com/ansible\-collections/community\.general/pull/8264](https\://github\.com/ansible\-collections/community\.general/pull/8264)\)\.
* mail \- add <code>Message\-ID</code> header\; which is required by some mail servers \([https\://github\.com/ansible\-collections/community\.general/pull/7740](https\://github\.com/ansible\-collections/community\.general/pull/7740)\)\.
* mail module\, mail callback plugin \- allow to configure the domain name of the Message\-ID header with a new <code>message\_id\_domain</code> option \([https\://github\.com/ansible\-collections/community\.general/pull/7765](https\://github\.com/ansible\-collections/community\.general/pull/7765)\)\.
* mssql\_script \- adds transactional \(rollback/commit\) support via optional boolean param <code>transaction</code> \([https\://github\.com/ansible\-collections/community\.general/pull/7976](https\://github\.com/ansible\-collections/community\.general/pull/7976)\)\.
* netcup\_dns \- adds support for record types <code>OPENPGPKEY</code>\, <code>SMIMEA</code>\, and <code>SSHFP</code> \([https\://github\.com/ansible\-collections/community\.general/pull/7489](https\://github\.com/ansible\-collections/community\.general/pull/7489)\)\.
* nmcli \- add support for new connection type <code>loopback</code> \([https\://github\.com/ansible\-collections/community\.general/issues/6572](https\://github\.com/ansible\-collections/community\.general/issues/6572)\)\.
* nmcli \- adds OpenvSwitch support with new <code>type</code> values <code>ovs\-port</code>\, <code>ovs\-interface</code>\, and <code>ovs\-bridge</code>\, and new <code>slave\_type</code> value <code>ovs\-port</code> \([https\://github\.com/ansible\-collections/community\.general/pull/8154](https\://github\.com/ansible\-collections/community\.general/pull/8154)\)\.
* nmcli \- allow for <code>infiniband</code> slaves of <code>bond</code> interface types \([https\://github\.com/ansible\-collections/community\.general/pull/7569](https\://github\.com/ansible\-collections/community\.general/pull/7569)\)\.
* nmcli \- allow for the setting of <code>MTU</code> for <code>infiniband</code> and <code>bond</code> interface types \([https\://github\.com/ansible\-collections/community\.general/pull/7499](https\://github\.com/ansible\-collections/community\.general/pull/7499)\)\.
* nmcli \- allow setting <code>MTU</code> for <code>bond\-slave</code> interface types \([https\://github\.com/ansible\-collections/community\.general/pull/8118](https\://github\.com/ansible\-collections/community\.general/pull/8118)\)\.
* onepassword lookup plugin \- support 1Password Connect with the opv2 client by setting the connect\_host and connect\_token parameters \([https\://github\.com/ansible\-collections/community\.general/pull/7116](https\://github\.com/ansible\-collections/community\.general/pull/7116)\)\.
* onepassword\_raw lookup plugin \- support 1Password Connect with the opv2 client by setting the connect\_host and connect\_token parameters \([https\://github\.com/ansible\-collections/community\.general/pull/7116](https\://github\.com/ansible\-collections/community\.general/pull/7116)\)
* opentelemetry \- add support for HTTP trace\_exporter and configures the behavior via <code>OTEL\_EXPORTER\_OTLP\_TRACES\_PROTOCOL</code> \([https\://github\.com/ansible\-collections/community\.general/issues/7888](https\://github\.com/ansible\-collections/community\.general/issues/7888)\, [https\://github\.com/ansible\-collections/community\.general/pull/8321](https\://github\.com/ansible\-collections/community\.general/pull/8321)\)\.
* opentelemetry \- add support for exporting spans in a file via <code>ANSIBLE\_OPENTELEMETRY\_STORE\_SPANS\_IN\_FILE</code> \([https\://github\.com/ansible\-collections/community\.general/issues/7888](https\://github\.com/ansible\-collections/community\.general/issues/7888)\, [https\://github\.com/ansible\-collections/community\.general/pull/8363](https\://github\.com/ansible\-collections/community\.general/pull/8363)\)\.
* opkg \- use <code>ModuleHelper</code> with <code>VarDict</code> \([https\://github\.com/ansible\-collections/community\.general/pull/8226](https\://github\.com/ansible\-collections/community\.general/pull/8226)\)\.
* osx\_defaults \- add option <code>check\_types</code> to enable changing the type of existing defaults on the fly \([https\://github\.com/ansible\-collections/community\.general/pull/8173](https\://github\.com/ansible\-collections/community\.general/pull/8173)\)\.
* parted \- refactor module to pass list of arguments to <code>module\.run\_command\(\)</code> instead of relying on interpretation by a shell \([https\://github\.com/ansible\-collections/community\.general/pull/8264](https\://github\.com/ansible\-collections/community\.general/pull/8264)\)\.
* passwordstore \- adds <code>timestamp</code> and <code>preserve</code> parameters to modify the stored password format \([https\://github\.com/ansible\-collections/community\.general/pull/7426](https\://github\.com/ansible\-collections/community\.general/pull/7426)\)\.
* passwordstore lookup \- add <code>missing\_subkey</code> parameter defining the behavior of the lookup when a passwordstore subkey is missing \([https\://github\.com/ansible\-collections/community\.general/pull/8166](https\://github\.com/ansible\-collections/community\.general/pull/8166)\)\.
* pipx \- use <code>ModuleHelper</code> with <code>VarDict</code> \([https\://github\.com/ansible\-collections/community\.general/pull/8226](https\://github\.com/ansible\-collections/community\.general/pull/8226)\)\.
* pkg5 \- add support for non\-silent execution \([https\://github\.com/ansible\-collections/community\.general/issues/8379](https\://github\.com/ansible\-collections/community\.general/issues/8379)\, [https\://github\.com/ansible\-collections/community\.general/pull/8382](https\://github\.com/ansible\-collections/community\.general/pull/8382)\)\.
* pkgin \- refactor module to pass list of arguments to <code>module\.run\_command\(\)</code> instead of relying on interpretation by a shell \([https\://github\.com/ansible\-collections/community\.general/pull/8264](https\://github\.com/ansible\-collections/community\.general/pull/8264)\)\.
* portage \- adds the possibility to explicitely tell portage to write packages to world file \([https\://github\.com/ansible\-collections/community\.general/issues/6226](https\://github\.com/ansible\-collections/community\.general/issues/6226)\, [https\://github\.com/ansible\-collections/community\.general/pull/8236](https\://github\.com/ansible\-collections/community\.general/pull/8236)\)\.
* portinstall \- refactor module to pass list of arguments to <code>module\.run\_command\(\)</code> instead of relying on interpretation by a shell \([https\://github\.com/ansible\-collections/community\.general/pull/8264](https\://github\.com/ansible\-collections/community\.general/pull/8264)\)\.
* proxmox \- adds <code>startup</code> parameters to configure startup order\, startup delay and shutdown delay \([https\://github\.com/ansible\-collections/community\.general/pull/8038](https\://github\.com/ansible\-collections/community\.general/pull/8038)\)\.
* proxmox \- adds <code>template</code> value to the <code>state</code> parameter\, allowing conversion of container to a template \([https\://github\.com/ansible\-collections/community\.general/pull/7143](https\://github\.com/ansible\-collections/community\.general/pull/7143)\)\.
* proxmox \- adds <code>update</code> parameter\, allowing update of an already existing containers configuration \([https\://github\.com/ansible\-collections/community\.general/pull/7540](https\://github\.com/ansible\-collections/community\.general/pull/7540)\)\.
* proxmox inventory plugin \- adds an option to exclude nodes from the dynamic inventory generation\. The new setting is optional\, not using this option will behave as usual \([https\://github\.com/ansible\-collections/community\.general/issues/6714](https\://github\.com/ansible\-collections/community\.general/issues/6714)\, [https\://github\.com/ansible\-collections/community\.general/pull/7461](https\://github\.com/ansible\-collections/community\.general/pull/7461)\)\.
* proxmox\* modules \- there is now a <code>community\.general\.proxmox</code> module defaults group that can be used to set default options for all Proxmox modules \([https\://github\.com/ansible\-collections/community\.general/pull/8334](https\://github\.com/ansible\-collections/community\.general/pull/8334)\)\.
* proxmox\_disk \- add ability to manipulate CD\-ROM drive \([https\://github\.com/ansible\-collections/community\.general/pull/7495](https\://github\.com/ansible\-collections/community\.general/pull/7495)\)\.
* proxmox\_kvm \- add parameter <code>update\_unsafe</code> to avoid limitations when updating dangerous values \([https\://github\.com/ansible\-collections/community\.general/pull/7843](https\://github\.com/ansible\-collections/community\.general/pull/7843)\)\.
* proxmox\_kvm \- adds <code>template</code> value to the <code>state</code> parameter\, allowing conversion of a VM to a template \([https\://github\.com/ansible\-collections/community\.general/pull/7143](https\://github\.com/ansible\-collections/community\.general/pull/7143)\)\.
* proxmox\_kvm \- adds\`\`usb\`\` parameter for setting USB devices on proxmox KVM VMs \([https\://github\.com/ansible\-collections/community\.general/pull/8199](https\://github\.com/ansible\-collections/community\.general/pull/8199)\)\.
* proxmox\_kvm \- support the <code>hookscript</code> parameter \([https\://github\.com/ansible\-collections/community\.general/issues/7600](https\://github\.com/ansible\-collections/community\.general/issues/7600)\)\.
* proxmox\_ostype \- it is now possible to specify the <code>ostype</code> when creating an LXC container \([https\://github\.com/ansible\-collections/community\.general/pull/7462](https\://github\.com/ansible\-collections/community\.general/pull/7462)\)\.
* proxmox\_vm\_info \- add ability to retrieve configuration info \([https\://github\.com/ansible\-collections/community\.general/pull/7485](https\://github\.com/ansible\-collections/community\.general/pull/7485)\)\.
* puppet \- new feature to set <code>\-\-waitforlock</code> option \([https\://github\.com/ansible\-collections/community\.general/pull/8282](https\://github\.com/ansible\-collections/community\.general/pull/8282)\)\.
* redfish\_command \- add command <code>ResetToDefaults</code> to reset manager to default state \([https\://github\.com/ansible\-collections/community\.general/issues/8163](https\://github\.com/ansible\-collections/community\.general/issues/8163)\)\.
* redfish\_config \- add command <code>SetServiceIdentification</code> to set service identification \([https\://github\.com/ansible\-collections/community\.general/issues/7916](https\://github\.com/ansible\-collections/community\.general/issues/7916)\)\.
* redfish\_info \- add boolean return value <code>MultipartHttpPush</code> to <code>GetFirmwareUpdateCapabilities</code> \([https\://github\.com/ansible\-collections/community\.general/issues/8194](https\://github\.com/ansible\-collections/community\.general/issues/8194)\, [https\://github\.com/ansible\-collections/community\.general/pull/8195](https\://github\.com/ansible\-collections/community\.general/pull/8195)\)\.
* redfish\_info \- add command <code>GetServiceIdentification</code> to get service identification \([https\://github\.com/ansible\-collections/community\.general/issues/7882](https\://github\.com/ansible\-collections/community\.general/issues/7882)\)\.
* redfish\_info \- adding the <code>BootProgress</code> property when getting <code>Systems</code> info \([https\://github\.com/ansible\-collections/community\.general/pull/7626](https\://github\.com/ansible\-collections/community\.general/pull/7626)\)\.
* revbitspss lookup plugin \- removed a redundant unicode prefix\. The prefix was not necessary for Python 3 and has been cleaned up to streamline the code \([https\://github\.com/ansible\-collections/community\.general/pull/8087](https\://github\.com/ansible\-collections/community\.general/pull/8087)\)\.
* rundeck module utils \- allow to pass <code>Content\-Type</code> to API requests \([https\://github\.com/ansible\-collections/community\.general/pull/7684](https\://github\.com/ansible\-collections/community\.general/pull/7684)\)\.
* slackpkg \- refactor module to pass list of arguments to <code>module\.run\_command\(\)</code> instead of relying on interpretation by a shell \([https\://github\.com/ansible\-collections/community\.general/pull/8264](https\://github\.com/ansible\-collections/community\.general/pull/8264)\)\.
* ssh\_config \- adds <code>controlmaster</code>\, <code>controlpath</code> and <code>controlpersist</code> parameters \([https\://github\.com/ansible\-collections/community\.general/pull/7456](https\://github\.com/ansible\-collections/community\.general/pull/7456)\)\.
* ssh\_config \- allow <code>accept\-new</code> as valid value for <code>strict\_host\_key\_checking</code> \([https\://github\.com/ansible\-collections/community\.general/pull/8257](https\://github\.com/ansible\-collections/community\.general/pull/8257)\)\.
* ssh\_config \- new feature to set <code>AddKeysToAgent</code> option to <code>yes</code> or <code>no</code> \([https\://github\.com/ansible\-collections/community\.general/pull/7703](https\://github\.com/ansible\-collections/community\.general/pull/7703)\)\.
* ssh\_config \- new feature to set <code>IdentitiesOnly</code> option to <code>yes</code> or <code>no</code> \([https\://github\.com/ansible\-collections/community\.general/pull/7704](https\://github\.com/ansible\-collections/community\.general/pull/7704)\)\.
* sudoers \- add support for the <code>NOEXEC</code> tag in sudoers rules \([https\://github\.com/ansible\-collections/community\.general/pull/7983](https\://github\.com/ansible\-collections/community\.general/pull/7983)\)\.
* svr4pkg \- refactor module to pass list of arguments to <code>module\.run\_command\(\)</code> instead of relying on interpretation by a shell \([https\://github\.com/ansible\-collections/community\.general/pull/8264](https\://github\.com/ansible\-collections/community\.general/pull/8264)\)\.
* swdepot \- refactor module to pass list of arguments to <code>module\.run\_command\(\)</code> instead of relying on interpretation by a shell \([https\://github\.com/ansible\-collections/community\.general/pull/8264](https\://github\.com/ansible\-collections/community\.general/pull/8264)\)\.
* terraform \- add support for <code>diff\_mode</code> for terraform resource\_changes \([https\://github\.com/ansible\-collections/community\.general/pull/7896](https\://github\.com/ansible\-collections/community\.general/pull/7896)\)\.
* terraform \- fix <code>diff\_mode</code> in state <code>absent</code> and when terraform <code>resource\_changes</code> does not exist \([https\://github\.com/ansible\-collections/community\.general/pull/7963](https\://github\.com/ansible\-collections/community\.general/pull/7963)\)\.
* xcc\_redfish\_command \- added support for raw POSTs \(<code>command\=PostResource</code> in <code>category\=Raw</code>\) without a specific action info \([https\://github\.com/ansible\-collections/community\.general/pull/7746](https\://github\.com/ansible\-collections/community\.general/pull/7746)\)\.
* xfconf \- use <code>ModuleHelper</code> with <code>VarDict</code> \([https\://github\.com/ansible\-collections/community\.general/pull/8226](https\://github\.com/ansible\-collections/community\.general/pull/8226)\)\.
* xfconf\_info \- use <code>ModuleHelper</code> with <code>VarDict</code> \([https\://github\.com/ansible\-collections/community\.general/pull/8226](https\://github\.com/ansible\-collections/community\.general/pull/8226)\)\.

<a id="community-grafana"></a>
#### community\.grafana

* Add Quickwit search engine datasource \([https\://quickwit\.io](https\://quickwit\.io)\)\.
* Add new module <em class="title-reference">grafana\_silence</em> to create and delete silences through the API
* Add parameter <em class="title-reference">org\_name</em> to <em class="title-reference">grafana\_dashboard</em>
* Add parameter <em class="title-reference">org\_name</em> to <em class="title-reference">grafana\_datasource</em>
* Add parameter <em class="title-reference">org\_name</em> to <em class="title-reference">grafana\_organization\_user</em>
* Add role components for <em class="title-reference">grafana\_silence</em> module
* Add support for Grafana Tempo datasource type \([https\://grafana\.com/docs/grafana/latest/datasources/tempo/](https\://grafana\.com/docs/grafana/latest/datasources/tempo/)\)
* Manage <em class="title-reference">grafana\_folder</em> for organizations
* Merged ansible role telekom\-mms/ansible\-role\-grafana into ansible\-collections/community\.grafana
* added <em class="title-reference">community\.grafana\.notification\_channel</em> to role
* default to true/false in docs and code
* grafana\_dashboard \- add check\_mode support
* lookup \- grafana\_dashboards \- add <em class="title-reference">validate\_certs</em> and <em class="title-reference">ca\_path</em> options to plugin for custom certs validation

<a id="community-hashi-vault-1"></a>
#### community\.hashi\_vault

* cert auth \- add option to set the <code>cert\_auth\_public\_key</code> and <code>cert\_auth\_private\_key</code> parameters using the variables <code>ansible\_hashi\_vault\_cert\_auth\_public\_key</code> and <code>ansible\_hashi\_vault\_cert\_auth\_private\_key</code> \([https\://github\.com/ansible\-collections/community\.hashi\_vault/issues/428](https\://github\.com/ansible\-collections/community\.hashi\_vault/issues/428)\)\.

<a id="community-hrobot-2"></a>
#### community\.hrobot

* robot inventory plugin \- add <code>filter</code> option which allows to include and exclude hosts based on Jinja2 conditions \([https\://github\.com/ansible\-collections/community\.hrobot/pull/101](https\://github\.com/ansible\-collections/community\.hrobot/pull/101)\)\.
* robot inventory plugin \- the <code>filters</code> option has been renamed to <code>simple\_filters</code>\. The old name still works until community\.hrobot 2\.0\.0\. Then it will change to allow more complex filtering with the <code>community\.library\_inventory\_filtering\_v1</code> collection\'s functionality \([https\://github\.com/ansible\-collections/community\.hrobot/pull/94](https\://github\.com/ansible\-collections/community\.hrobot/pull/94)\)\.

<a id="community-mysql-6"></a>
#### community\.mysql

* mysql\_user \- add the <code>password\_expire</code> and <code>password\_expire\_interval</code> arguments to implement the password expiration management for mysql user \([https\://github\.com/ansible\-collections/community\.mysql/pull/598](https\://github\.com/ansible\-collections/community\.mysql/pull/598)\)\.
* mysql\_user \- add user attribute support via the <code>attributes</code> parameter and return value \([https\://github\.com/ansible\-collections/community\.mysql/pull/604](https\://github\.com/ansible\-collections/community\.mysql/pull/604)\)\.

<a id="community-postgresql-8"></a>
#### community\.postgresql

* postgresql\_db \- add the <code>comment</code> argument \([https\://github\.com/ansible\-collections/community\.postgresql/issues/614](https\://github\.com/ansible\-collections/community\.postgresql/issues/614)\)\.
* postgresql\_db \- add the <code>icu\_locale</code> argument \([https\://github\.com/ansible\-collections/community\.postgresql/issues/666](https\://github\.com/ansible\-collections/community\.postgresql/issues/666)\)\.
* postgresql\_db \- add the <code>locale\_provider</code> argument \([https\://github\.com/ansible\-collections/community\.postgresql/issues/666](https\://github\.com/ansible\-collections/community\.postgresql/issues/666)\)\.
* postgresql\_ext \- add the <code>comment</code> argument \([https\://github\.com/ansible\-collections/community\.postgresql/issues/354](https\://github\.com/ansible\-collections/community\.postgresql/issues/354)\)\.
* postgresql\_publication \- add the <code>comment</code> argument \([https\://github\.com/ansible\-collections/community\.postgresql/issues/354](https\://github\.com/ansible\-collections/community\.postgresql/issues/354)\)\.
* postgresql\_schema \- add the <code>comment</code> argument \([https\://github\.com/ansible\-collections/community\.postgresql/issues/354](https\://github\.com/ansible\-collections/community\.postgresql/issues/354)\)\.
* postgresql\_subscription \- add the <code>comment</code> argument \([https\://github\.com/ansible\-collections/community\.postgresql/issues/354](https\://github\.com/ansible\-collections/community\.postgresql/issues/354)\)\.
* postgresql\_tablespace \- add the <code>comment</code> argument \([https\://github\.com/ansible\-collections/community\.postgresql/issues/354](https\://github\.com/ansible\-collections/community\.postgresql/issues/354)\)\.

<a id="community-rabbitmq"></a>
#### community\.rabbitmq

* rabbitmq\_user \- add support to user manipulation through RabbitMQ API \([https\://github\.com/ansible\-collections/community\.rabbitmq/issues/76](https\://github\.com/ansible\-collections/community\.rabbitmq/issues/76)\)

<a id="community-routeros-7"></a>
#### community\.routeros

* api\_info\, api\_modify \- Add RouterOS 7\.x support to <code>/mpls ldp</code> path \([https\://github\.com/ansible\-collections/community\.routeros/pull/271](https\://github\.com/ansible\-collections/community\.routeros/pull/271)\)\.
* api\_info\, api\_modify \- add <code>/ip route rule</code> path for RouterOS 6\.x \([https\://github\.com/ansible\-collections/community\.routeros/pull/278](https\://github\.com/ansible\-collections/community\.routeros/pull/278)\)\.
* api\_info\, api\_modify \- add <code>/routing filter</code> path for RouterOS 6\.x \([https\://github\.com/ansible\-collections/community\.routeros/pull/279](https\://github\.com/ansible\-collections/community\.routeros/pull/279)\)\.
* api\_info\, api\_modify \- add <code>interface ovpn\-client</code> path \([https\://github\.com/ansible\-collections/community\.routeros/issues/242](https\://github\.com/ansible\-collections/community\.routeros/issues/242)\, [https\://github\.com/ansible\-collections/community\.routeros/pull/244](https\://github\.com/ansible\-collections/community\.routeros/pull/244)\)\.
* api\_info\, api\_modify \- add <code>radius</code> path \([https\://github\.com/ansible\-collections/community\.routeros/issues/241](https\://github\.com/ansible\-collections/community\.routeros/issues/241)\, [https\://github\.com/ansible\-collections/community\.routeros/pull/245](https\://github\.com/ansible\-collections/community\.routeros/pull/245)\)\.
* api\_info\, api\_modify \- add <code>routing rule</code> path \([https\://github\.com/ansible\-collections/community\.routeros/issues/162](https\://github\.com/ansible\-collections/community\.routeros/issues/162)\, [https\://github\.com/ansible\-collections/community\.routeros/pull/246](https\://github\.com/ansible\-collections/community\.routeros/pull/246)\)\.
* api\_info\, api\_modify \- add default value for <code>from\-pool</code> field in <code>/ipv6 address</code> \([https\://github\.com/ansible\-collections/community\.routeros/pull/270](https\://github\.com/ansible\-collections/community\.routeros/pull/270)\)\.
* api\_info\, api\_modify \- add missing DoH parameters <code>doh\-max\-concurrent\-queries</code>\, <code>doh\-max\-server\-connections</code>\, and <code>doh\-timeout</code> to the <code>ip dns</code> path \([https\://github\.com/ansible\-collections/community\.routeros/issues/230](https\://github\.com/ansible\-collections/community\.routeros/issues/230)\, [https\://github\.com/ansible\-collections/community\.routeros/pull/235](https\://github\.com/ansible\-collections/community\.routeros/pull/235)\)
* api\_info\, api\_modify \- add missing parameters <code>address\-list</code>\, <code>address\-list\-timeout</code>\, <code>randomise\-ports</code>\, and <code>realm</code> to subpaths of the <code>ip firewall</code> path \([https\://github\.com/ansible\-collections/community\.routeros/issues/236](https\://github\.com/ansible\-collections/community\.routeros/issues/236)\, [https\://github\.com/ansible\-collections/community\.routeros/pull/237](https\://github\.com/ansible\-collections/community\.routeros/pull/237)\)\.
* api\_info\, api\_modify \- add missing path <code>/interface pppoe\-server server</code> \([https\://github\.com/ansible\-collections/community\.routeros/pull/273](https\://github\.com/ansible\-collections/community\.routeros/pull/273)\)\.
* api\_info\, api\_modify \- add missing path <code>/ip dhcp\-relay</code> \([https\://github\.com/ansible\-collections/community\.routeros/pull/276](https\://github\.com/ansible\-collections/community\.routeros/pull/276)\)\.
* api\_info\, api\_modify \- add missing path <code>/queue simple</code> \([https\://github\.com/ansible\-collections/community\.routeros/pull/269](https\://github\.com/ansible\-collections/community\.routeros/pull/269)\)\.
* api\_info\, api\_modify \- add missing path <code>/queue type</code> \([https\://github\.com/ansible\-collections/community\.routeros/pull/274](https\://github\.com/ansible\-collections/community\.routeros/pull/274)\)\.
* api\_info\, api\_modify \- add missing path <code>routing bgp template</code> \([https\://github\.com/ansible\-collections/community\.routeros/pull/243](https\://github\.com/ansible\-collections/community\.routeros/pull/243)\)\.
* api\_info\, api\_modify \- add missing paths <code>/routing bgp aggregate</code>\, <code>/routing bgp network</code> and <code>/routing bgp peer</code> \([https\://github\.com/ansible\-collections/community\.routeros/pull/277](https\://github\.com/ansible\-collections/community\.routeros/pull/277)\)\.
* api\_info\, api\_modify \- add read\-only fields <code>installed\-version</code>\, <code>latest\-version</code> and <code>status</code> in <code>system package update</code> \([https\://github\.com/ansible\-collections/community\.routeros/pull/263](https\://github\.com/ansible\-collections/community\.routeros/pull/263)\)\.
* api\_info\, api\_modify \- add support for paths <code>/mpls interface</code>\, <code>/mpls ldp accept\-filter</code>\, <code>/mpls ldp advertise\-filter</code> and <code>mpls ldp interface</code> \([https\://github\.com/ansible\-collections/community\.routeros/pull/272](https\://github\.com/ansible\-collections/community\.routeros/pull/272)\)\.
* api\_info\, api\_modify \- add support for the <code>tx\-power</code> attribute in <code>interface wireless</code> \([https\://github\.com/ansible\-collections/community\.routeros/pull/239](https\://github\.com/ansible\-collections/community\.routeros/pull/239)\)\.
* api\_info\, api\_modify \- added support for <code>interface wifi</code> and its sub\-paths \([https\://github\.com/ansible\-collections/community\.routeros/pull/266](https\://github\.com/ansible\-collections/community\.routeros/pull/266)\)\.
* api\_info\, api\_modify \- make path <code>user group</code> modifiable and add <code>comment</code> attribute \([https\://github\.com/ansible\-collections/community\.routeros/issues/256](https\://github\.com/ansible\-collections/community\.routeros/issues/256)\, [https\://github\.com/ansible\-collections/community\.routeros/pull/257](https\://github\.com/ansible\-collections/community\.routeros/pull/257)\)\.
* api\_info\, api\_modify \- mark the <code>interface wireless</code> parameter <code>running</code> as read\-only \([https\://github\.com/ansible\-collections/community\.routeros/pull/233](https\://github\.com/ansible\-collections/community\.routeros/pull/233)\)\.
* api\_info\, api\_modify \- remove default value for read\-only <code>running</code> field in <code>interface wireless</code> \([https\://github\.com/ansible\-collections/community\.routeros/pull/264](https\://github\.com/ansible\-collections/community\.routeros/pull/264)\)\.
* api\_info\, api\_modify \- removed <code>host</code> primary key in <code>tool netwatch</code> path \([https\://github\.com/ansible\-collections/community\.routeros/pull/248](https\://github\.com/ansible\-collections/community\.routeros/pull/248)\)\.
* api\_info\, api\_modify \- set the default value to <code>false</code> for the  <code>disabled</code> parameter in some more paths where it can be seen in the documentation \([https\://github\.com/ansible\-collections/community\.routeros/pull/237](https\://github\.com/ansible\-collections/community\.routeros/pull/237)\)\.
* api\_modify \- add missing <code>comment</code> attribute to <code>/routing id</code> \([https\://github\.com/ansible\-collections/community\.routeros/pull/234](https\://github\.com/ansible\-collections/community\.routeros/pull/234)\)\.
* api\_modify \- add missing attributes to the <code>routing bgp connection</code> path \([https\://github\.com/ansible\-collections/community\.routeros/pull/234](https\://github\.com/ansible\-collections/community\.routeros/pull/234)\)\.
* api\_modify \- add versioning to the <code>/tool e\-mail</code> path \(RouterOS 7\.12 release\) \([https\://github\.com/ansible\-collections/community\.routeros/pull/234](https\://github\.com/ansible\-collections/community\.routeros/pull/234)\)\.
* api\_modify \- make <code>/ip traffic\-flow target</code> a multiple value attribute \([https\://github\.com/ansible\-collections/community\.routeros/pull/234](https\://github\.com/ansible\-collections/community\.routeros/pull/234)\)\.
* api\_modify\, api\_info \- add support for the <code>ip vrf</code> path in RouterOS 7  \([https\://github\.com/ansible\-collections/community\.routeros/pull/259](https\://github\.com/ansible\-collections/community\.routeros/pull/259)\)
* api\_modify\, api\_info \- added support for <code>interface wifiwave2</code> \([https\://github\.com/ansible\-collections/community\.routeros/pull/226](https\://github\.com/ansible\-collections/community\.routeros/pull/226)\)\.

<a id="community-vmware-10"></a>
#### community\.vmware

* Add standard function vmware\_argument\_spec\(\) from module\_utils for using default env fallback function\. [https\://github\.com/ansible\-collections/community\.vmware/issues/1977](https\://github\.com/ansible\-collections/community\.vmware/issues/1977)
* Document that all parameters and VMware object names are case sensitive \([https\://github\.com/ansible\-collections/community\.vmware/issues/2019](https\://github\.com/ansible\-collections/community\.vmware/issues/2019)\)\.
* Drop the outdated \(and actually unmaintained\) scenario guides \([https\://github\.com/ansible\-collections/community\.vmware/pull/2022](https\://github\.com/ansible\-collections/community\.vmware/pull/2022)\)\.
* vmware\_dvs\_portgroup \- Make <em class="title-reference">state</em> default to <em class="title-reference">present</em> instead of having it as a required parameter \([https\://github\.com/ansible\-collections/community\.vmware/pull/2055](https\://github\.com/ansible\-collections/community\.vmware/pull/2055)\)\.
* vmware\_dvswitch \- Add switchIpAddress/switch\_ip parameter for netflow config
* vmware\_first\_class\_disk\_info \- Add a module to gather informations about first class disks\. \([https\://github\.com/ansible\-collections/community\.vmware/pull/1996](https\://github\.com/ansible\-collections/community\.vmware/pull/1996)\)\. \([https\://github\.com/ansible\-collections/community\.vmware/issues/1988](https\://github\.com/ansible\-collections/community\.vmware/issues/1988)\)\.
* vmware\_guest \- Add IPv6 support for VM network interfaces \([https\://github\.com/ansible\-collections/community\.vmware/pull/1937](https\://github\.com/ansible\-collections/community\.vmware/pull/1937)\)\.
* vmware\_guest\_sendkey \- Add Windows key \([https\://github\.com/ansible\-collections/community\.vmware/issues/1959](https\://github\.com/ansible\-collections/community\.vmware/issues/1959)\)\.
* vmware\_guest\_tools\_info \- Use <em class="title-reference">toolsVersionStatus2</em> instead of <em class="title-reference">toolsVersionStatus</em> \([https\://github\.com/ansible\-collections/community\.vmware/issues/2033](https\://github\.com/ansible\-collections/community\.vmware/issues/2033)\)\.
* vmware\_guest\_tools\_upgrade \- Add parameter <em class="title-reference">installer\_options</em> to pass command line options to the installer to modify the installation procedure for tools \([https\://github\.com/ansible\-collections/community\.vmware/pull/1059](https\://github\.com/ansible\-collections/community\.vmware/pull/1059)\)\.
* vmware\_host\_facts \- Add the possibility to get the related datacenter\. \([https\://github\.com/ansible\-collections/community\.vmware/pull/1994](https\://github\.com/ansible\-collections/community\.vmware/pull/1994)\)\.
* vmware\_vm\_inventory \- Add parameter <em class="title-reference">subproperties</em> \([https\://github\.com/ansible\-collections/community\.vmware/pull/1972](https\://github\.com/ansible\-collections/community\.vmware/pull/1972)\)\.
* vmware\_vmkernel \- Add the function to set the enable\_backup\_nfc setting \([https\://github\.com/ansible\-collections/community\.vmware/pull/1978](https\://github\.com/ansible\-collections/community\.vmware/pull/1978)\)
* vsphere\_copy \- Add parameter to tell vsphere\_copy which diskformat is being uploaded \([https\://github\.com/ansible\-collections/community\.vmware/pull/1995](https\://github\.com/ansible\-collections/community\.vmware/pull/1995)\)\.

<a id="community-windows-2"></a>
#### community\.windows

* Set minimum supported Ansible version to 2\.14 to align with the versions still supported by Ansible\.
* win\_regmerge \- Add content \'content\' parameter for specifying registry file contents directly

<a id="community-zabbix-2"></a>
#### community\.zabbix

* Add slash at the end of the location directives\, to prevent path traversal attacks\.
* Added active\_since and active\_till in zabbix\_maintenance
* Added content\_type for email in zabbix\_mediatypes
* Added zabbix\_group\_events\_info module
* Introduce flag <em class="title-reference">enable\_version\_check</em> to allow installations on non\-supported platforms\.
* action module \- Added notify\_if\_canceled property
* agent and proxy roles \- Set default <em class="title-reference">zabbix\_api\_server\_port</em> to 80 or 443 based on <em class="title-reference">zabbix\_api\_use\_ssl</em>
* agent role \- Removed duplicative Windows agent task
* agent role \- Standardized default yum priority to 99
* agent\, javagateway\, proxy\, server\, and web role \- added the http\_proxy and https\_proxy environment variables to \"Debian \| Download gpg key\" analog to other tasks
* agent\, javagateway\, proxy\, server\, and web role \- introduced default variable zabbix\_repo\_deb\_gpg\_key\_url with value [http\://repo\.zabbix\.com/zabbix\-official\-repo\.key](http\://repo\.zabbix\.com/zabbix\-official\-repo\.key)
* agent\, javagateway\, proxy\, server\, and web role \- introduced default variable zabbix\_repo\_deb\_include\_deb\_src with value true
* agent\, javagateway\, proxy\, server\, and web role \- removed superfluous slash in zabbix\_gpg\_key of the Debian vars and renamed key to zabbix\-repo instead of zabbix\-official\-repo
* agent\, javagateway\, proxy\, server\, and web role \- used variable zabbix\_repo\_deb\_include\_deb\_src in \"Debian \| Installing repository\" to determine whether deb\-src should be added to /etc/apt/sources\.list\.d/zabbix\.sources
* agent\, javagateway\, proxy\, server\, and web role \- used zabbix\_repo\_deb\_gpg\_key\_url in \"Debian \| Download gpg key\" instead of hardcoded url
* all roles \- Re\-added ability to override Debian repo source
* all roles \- Updated Debian repository format to 822 standard
* api\_requests \- Handled error from depricated CertificateError class
* multiple roles \- Removed unneeded Apt Clean commands\.
* proxy role \- Updated MariaDB version for Centos 7 to 10\.11
* various \- updated testing modules
* various \- updated to fully qualified module names
* zabbix agent \- Added capability to add additional configuration includes
* zabbix web \- Allowed the independent configuration of php\-fpm without creating vhost\.
* zabbix\_api\_info module added
* zabbix\_correlation module added
* zabbix\_host\_info \- added ability to get all the hosts configured in Zabbix
* zabbix\_proxy role \- Add variable zabbix\_proxy\_dbpassword\_hash\_method to control whether you want postgresql user password to be hashed with md5 or want to use db default\. When zabbix\_proxy\_dbpassword\_hash\_method is set to anything other than md5 then do not hash the password with md5 so you could use postgresql scram\-sha\-256 hashing method\.
* zabbix\_server role \- Add variable zabbix\_server\_dbpassword\_hash\_method to control whether you want postgresql user password to be hashed with md5 or want to use db default\. When zabbix\_server\_dbpassword\_hash\_method is set to anything other than md5 then do not hash the password with md5 so you could use postgresql scram\-sha\-256 hashing method\.
* zabbix\_service\_info module added
* zabbix\_template \- Add template\_yaml parameter\.
* zabbix\_templategroup module added
* zabbix\_user module \- add current\_passwd optional parameter to enable password updating of the currently logged in user \([https\://www\.zabbix\.com/documentation/6\.4/en/manual/api/reference/user/update](https\://www\.zabbix\.com/documentation/6\.4/en/manual/api/reference/user/update)\)
* zabbix\_web role\, Refactored zabbix\_selinux variable names to correlate with selinux boolean names\.

<a id="containers-podman-11"></a>
#### containers\.podman

* Add log\_opt and annotaion options to podman\_play module
* Add option to parse CreateCommand easily for diff calc
* Add support for setting underlying interface in podman\_network
* Alias generate systemd options stop\_timeout and time
* CI \- Fix rootfs test in CI
* CI \- add custom podman path to tasks
* CI \- add parametrized executables to tests
* Fix CI rootfs for podman\_container
* Fix broken conmon version in CI install
* Improve security\_opt comparison between existing container
* podman\_container \- Add new arguments to podman status commands
* podman\_container \- Add pasta as default network mode after v5
* podman\_container \- Update env\_file to accept a list of files instead of a single file
* podman\_container\_exec \- Return data for podman exec module
* podman\_generate\_systemd \- Fix broken example for podman\_generate\_systemd \(\#708\)
* podman\_login \- Update podman\_login\.py
* podman\_play \- Add support for kube yaml files with multi\-documents \(\#724\)
* podman\_play \- Update the logic for deleting pods/containers in podman\_play
* podman\_pod\_info \- handle return being list in Podman 5 \(\#713\)
* podman\_secret\_info \- Add secrets info module

<a id="dellemc-enterprise-sonic-4"></a>
#### dellemc\.enterprise\_sonic

* sonic\_aaa \- Add support for playbook check and diff modes \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/304](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/304)\)\.
* sonic\_aaa \- Enhance config diff generation function \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/318](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/318)\)\.
* sonic\_acl\_interfaces \- Add support for playbook check and diff modes \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/306](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/306)\)\.
* sonic\_acl\_interfaces \- Enhance config diff generation function \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/318](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/318)\)\.
* sonic\_bgp\_as\_paths \- Add support for replaced and overridden states \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/290](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/290)\)\.
* sonic\_bgp\_communities \- Add support for replaced and overridden states \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/251](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/251)\)\.
* sonic\_bgp\_ext\_communities \- Add support for replaced and overridden states \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/252](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/252)\)\.
* sonic\_interfaces \- Add support for playbook check and diff modes \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/301](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/301)\)\.
* sonic\_interfaces \- Add support for replaced and overridden states \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/314](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/314)\)\.
* sonic\_interfaces \- Change deleted design for interfaces module \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/310](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/310)\)\.
* sonic\_interfaces \- Enhance config diff generation function \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/318](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/318)\)\.
* sonic\_ip\_neighbor \- Add support for playbook check and diff modes \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/285](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/285)\)\.
* sonic\_ip\_neighbor \- Enhance config diff generation function \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/318](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/318)\)\.
* sonic\_l2\_acls \- Add support for playbook check and diff modes \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/306](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/306)\)\.
* sonic\_l2\_acls \- Enhance config diff generation function \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/318](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/318)\)\.
* sonic\_l2\_interfaces \- Add support for playbook check and diff modes \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/303](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/303)\)\.
* sonic\_l2\_interfaces \- Enhance config diff generation function \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/318](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/318)\)\.
* sonic\_l3\_acls \- Add support for playbook check and diff modes \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/306](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/306)\)\.
* sonic\_l3\_acls \- Enhance config diff generation function \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/318](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/318)\)\.
* sonic\_l3\_interfaces \- Add support for replaced and overridden states \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/241](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/241)\)\.
* sonic\_lag\_interfaces \- Add support for playbook check and diff modes \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/303](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/303)\)\.
* sonic\_lag\_interfaces \- Enhance config diff generation function \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/318](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/318)\)\.
* sonic\_logging \- Add support for playbook check and diff modes \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/285](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/285)\)\.
* sonic\_logging \- Enhance config diff generation function \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/318](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/318)\)\.
* sonic\_mclag \- Add VLAN range support for \'unique\_ip\' and \'peer\_gateway\' options \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/288](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/288)\)\.
* sonic\_mclag \- Add support for replaced and overridden states \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/288](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/288)\)\.
* sonic\_ntp \- Add support for playbook check and diff modes \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/281](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/281)\)\.
* sonic\_ntp \- Enhance config diff generation function \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/318](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/318)\)\.
* sonic\_port\_breakout \- Add Ansible support for all port breakout modes now allowed in Enterprise SONiC \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/276](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/276)\)\.
* sonic\_port\_breakout \- Add support for replaced and overridden states \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/291](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/291)\)\.
* sonic\_port\_group \- Add support for playbook check and diff modes \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/284](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/284)\)\.
* sonic\_port\_group \- Enhance config diff generation function \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/318](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/318)\)\.
* sonic\_radius\_server \- Add support for playbook check and diff modes \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/279](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/279)\)\.
* sonic\_radius\_server \- Enhance config diff generation function \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/318](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/318)\)\.
* sonic\_static\_routes \- Add playbook check and diff modes support for static routes resource module \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/313](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/313)\)\.
* sonic\_static\_routes \- Enhance config diff generation function \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/318](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/318)\)\.
* sonic\_system \- Add support for playbook check and diff modes \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/284](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/284)\)\.
* sonic\_system \- Enhance config diff generation function \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/318](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/318)\)\.
* sonic\_tacacs\_server \- Add support for playbook check and diff modes \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/281](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/281)\)\.
* sonic\_tacacs\_server \- Enhance config diff generation function \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/318](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/318)\)\.
* sonic\_users \- Add support for playbook check and diff modes \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/304](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/304)\)\.
* sonic\_users \- Enhance config diff generation function \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/318](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/318)\)\.
* sonic\_vlans \- Add support for playbook check and diff modes \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/301](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/301)\)\.
* sonic\_vlans \- Enhance config diff generation function \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/318](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/318)\)\.
* sonic\_vrfs \- Add mgmt VRF replaced state handling to sonic\_vrfs module \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/298](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/298)\)\.
* sonic\_vrfs \- Add mgmt VRF support to sonic\_vrfs module \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/293](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/293)\)\.
* sonic\_vrfs \- Add support for playbook check and diff modes \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/285](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/285)\)\.
* sonic\_vrfs \- Enhance config diff generation function \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/318](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/318)\)\.
* tests \- Add UTs for BFD\, COPP\, and MAC modules \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/287](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/287)\)\.
* tests \- Enable contiguous execution of all regression integration tests on an S5296f \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/277](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/277)\)\.
* tests \- Fix the bgp CLI test base\_cfg\_path derivation of the bgp role\_path by avoiding relative pathing from the possibly external playbook\_dir \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/283](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/283)\)\.

<a id="dellemc-openmanage-24"></a>
#### dellemc\.openmanage

* Ansible lint issues are fixed for the collections\.
* For idrac\_certificate role\, added support for import operation of <em class="title-reference">HTTPS</em> certificate with the SSL key\.
* For idrac\_certificates module\, below enhancements are made\: Added support for import operation of <em class="title-reference">HTTPS</em> certificate with the SSL key\. The <em class="title-reference">email\_address</em> has been made as an optional parameter\.
* For idrac\_gather\_facts role\, added storage controller details in the role output\.
* Module <code>redfish\_storage\_volume</code> is enhanced to support reboot options and job tracking operation\.
* idrac\_reset \- This module allows you to reset the iDRAC to factory default settings\.
* redfish\_storage\_volume \- This module is enhanced to support iDRAC8\.

<a id="dellemc-powerflex-1"></a>
#### dellemc\.powerflex

* Added support for PowerFlex Denver version\(4\.5\.x\) to TB and Config role\.
* Added support for PowerFlex ansible modules and roles on Azure\.
* Added support for executing Ansible PowerFlex modules and roles on AWS environment\.
* Added support for resource group provisioning to validate\, deploy\, edit\, add nodes and delete a resource group\.
* The Info module is enhanced to list the firmware repositories\.
* The Info module is enhanced to retrieve lists related to fault sets\, service templates\, deployments\, and managed devices\.
* The SDS module has been enhanced to facilitate SDS creation within a fault set\.

<a id="f5networks-f5-modules-5"></a>
#### f5networks\.f5\_modules

* bigiq\_device\_discovery \- Changes in documentation related to Provider block

<a id="fortinet-fortimanager-9"></a>
#### fortinet\.fortimanager

* Added deprecated warning to invalid argument name\, please change the invalid argument name such as \"var\-name\"\, \"var name\" to \"var\_name\"\.
* Renamed the input argument \"message\" to \"fmgr\_message\" to comply with Ansible requirements\.
* Supported fortimanager 7\.4\.2\, 21 new modules\.

<a id="google-cloud-2"></a>
#### google\.cloud

* anisble\-test \- integration tests are now run against 2\.14\.0 and 2\.15\.0
* ansible \- 2\.14\.0 is now the minimum version supported
* ansible\-lint \- fixed over a thousand reported errors
* ansible\-lint \- upgraded to 6\.22
* ansible\-test \- add support for GCP application default credentials \([https\://github\.com/ansible\-collections/google\.cloud/issues/359](https\://github\.com/ansible\-collections/google\.cloud/issues/359)\)\.
* gcp\_serviceusage\_service \- added backoff when checking for operation completion\.
* gcp\_serviceusage\_service \- use alloyb API for the integration test as spanner conflicts with other tests
* gcp\_sql\_ssl\_cert \- made sha1\_fingerprint optional\, which enables resource creation
* gcp\_storage\_default\_object\_acl \- removed non\-existent fields\; the resource is not usable\.

<a id="grafana-grafana-4"></a>
#### grafana\.grafana

* Add \'run\_once\' to download\&unzip tasks by \@v\-zhuravlev in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/136](https\://github\.com/grafana/grafana\-ansible\-collection/pull/136)
* Adding <em class="title-reference">oauth\_allow\_insecure\_email\_lookup</em> to fix oauth user sync error by \@hypery2k in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/132](https\://github\.com/grafana/grafana\-ansible\-collection/pull/132)
* Bump ansible\-core from 2\.15\.4 to 2\.15\.8 by \@dependabot in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/137](https\://github\.com/grafana/grafana\-ansible\-collection/pull/137)
* Bump ansible\-lint from 24\.2\.0 to 24\.2\.1 by \@dependabot in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/164](https\://github\.com/grafana/grafana\-ansible\-collection/pull/164)
* Bump ansible\-lint from 24\.2\.0 to 24\.2\.1 by \@dependabot in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/168](https\://github\.com/grafana/grafana\-ansible\-collection/pull/168)
* Bump ansible\-lint from 6\.13\.1 to 6\.14\.3 by \@dependabot in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/139](https\://github\.com/grafana/grafana\-ansible\-collection/pull/139)
* Bump ansible\-lint from 6\.14\.3 to 6\.22\.2 by \@dependabot in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/142](https\://github\.com/grafana/grafana\-ansible\-collection/pull/142)
* Bump ansible\-lint from 6\.22\.2 to 24\.2\.0 by \@dependabot in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/150](https\://github\.com/grafana/grafana\-ansible\-collection/pull/150)
* Bump black from 24\.1\.1 to 24\.3\.0 by \@dependabot in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/165](https\://github\.com/grafana/grafana\-ansible\-collection/pull/165)
* Bump cryptography from 41\.0\.4 to 41\.0\.6 by \@dependabot in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/126](https\://github\.com/grafana/grafana\-ansible\-collection/pull/126)
* Bump jinja2 from 3\.1\.2 to 3\.1\.3 by \@dependabot in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/129](https\://github\.com/grafana/grafana\-ansible\-collection/pull/129)
* Bump pylint from 2\.16\.2 to 3\.0\.3 by \@dependabot in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/141](https\://github\.com/grafana/grafana\-ansible\-collection/pull/141)
* Bump pylint from 3\.0\.3 to 3\.1\.0 by \@dependabot in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/158](https\://github\.com/grafana/grafana\-ansible\-collection/pull/158)
* Bump pylint from 3\.0\.3 to 3\.1\.0 by \@dependabot in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/161](https\://github\.com/grafana/grafana\-ansible\-collection/pull/161)
* Bump the pip group across 1 directories with 1 update by \@dependabot in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/156](https\://github\.com/grafana/grafana\-ansible\-collection/pull/156)
* Bump yamllint from 1\.29\.0 to 1\.33\.0 by \@dependabot in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/140](https\://github\.com/grafana/grafana\-ansible\-collection/pull/140)
* Bump yamllint from 1\.29\.0 to 1\.33\.0 by \@dependabot in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/143](https\://github\.com/grafana/grafana\-ansible\-collection/pull/143)
* Bump yamllint from 1\.33\.0 to 1\.34\.0 by \@dependabot in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/151](https\://github\.com/grafana/grafana\-ansible\-collection/pull/151)
* Bump yamllint from 1\.33\.0 to 1\.35\.1 by \@dependabot in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/155](https\://github\.com/grafana/grafana\-ansible\-collection/pull/155)
* Bump yamllint from 1\.33\.0 to 1\.35\.1 by \@dependabot in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/159](https\://github\.com/grafana/grafana\-ansible\-collection/pull/159)
* Change handler to systemd by \@v\-zhuravlev in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/135](https\://github\.com/grafana/grafana\-ansible\-collection/pull/135)
* Clarify grafana\-server configuration in README by \@VGerris in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/177](https\://github\.com/grafana/grafana\-ansible\-collection/pull/177)
* Drop curl check by \@v\-zhuravlev in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/120](https\://github\.com/grafana/grafana\-ansible\-collection/pull/120)
* ExecStartPre and EnvironmentFile settings to system unit file by \@fabiiw05 in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/157](https\://github\.com/grafana/grafana\-ansible\-collection/pull/157)
* Fix check mode for grafana role by \@Boschung\-Mecatronic\-AG\-Infrastructure in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/125](https\://github\.com/grafana/grafana\-ansible\-collection/pull/125)
* Fix check mode in Grafana Agent by \@AmandaCameron in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/124](https\://github\.com/grafana/grafana\-ansible\-collection/pull/124)
* Fix links in grafana\_agent/defaults/main\.yaml by \@PabloCastellano in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/134](https\://github\.com/grafana/grafana\-ansible\-collection/pull/134)
* Topic/grafana agent idempotency by \@ohdearaugustin in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/147](https\://github\.com/grafana/grafana\-ansible\-collection/pull/147)
* Update description to match module by \@brmurphy in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/179](https\://github\.com/grafana/grafana\-ansible\-collection/pull/179)
* Update tags in README by \@ishanjainn in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/121](https\://github\.com/grafana/grafana\-ansible\-collection/pull/121)
* datasources url parameter fix by \@dergudzon in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/162](https\://github\.com/grafana/grafana\-ansible\-collection/pull/162)

<a id="hetzner-hcloud"></a>
#### hetzner\.hcloud

* Add the <em class="title-reference">hetzner\.hcloud\.all</em> group to configure all the modules using <em class="title-reference">module\_defaults</em>\.
* Allow to set the <em class="title-reference">api\_endpoint</em> module argument using the <em class="title-reference">HCLOUD\_ENDPOINT</em> environment variable\.
* Removed the <em class="title-reference">hcloud\_</em> prefix from all modules names\, e\.g\. <em class="title-reference">hetzner\.hcloud\.hcloud\_firewall</em> was renamed to <em class="title-reference">hetzner\.hcloud\.firewall</em>\. Old module names will continue working\.
* Renamed the <em class="title-reference">endpoint</em> module argument to <em class="title-reference">api\_endpoint</em>\, backward compatibility is maintained using an alias\.
* Replace deprecated <em class="title-reference">ansible\.netcommon</em> ip utils with python <em class="title-reference">ipaddress</em> module\. The <em class="title-reference">ansible\.netcommon</em> collection is no longer required by the collections\.
* firewall \- Allow forcing the deletion of firewalls that are still in use\.
* firewall \- Do not silence \'firewall still in use\' delete failures\.
* firewall \- Return resources the firewall is <em class="title-reference">applied\_to</em>\.
* firewall\_info \- Add new <em class="title-reference">firewall\_info</em> module to gather firewalls info\.
* firewall\_resource \- Add new <em class="title-reference">firewall\_resource</em> module to manage firewalls resources\.
* hcloud inventory \- Add the <em class="title-reference">api\_endpoint</em> option\.
* hcloud inventory \- Deprecate the <em class="title-reference">api\_token\_env</em> option\, suggest using a lookup plugin \(<em class="title-reference">\{\{ lookup\(\'ansible\.builtin\.env\'\, \'YOUR\_ENV\_VAR\'\) \}\}</em>\) or use the well\-known <em class="title-reference">HCLOUD\_TOKEN</em> environment variable name\.
* hcloud inventory \- Rename the <em class="title-reference">token\_env</em> option to <em class="title-reference">api\_token\_env</em>\, use aliases for backward compatibility\.
* hcloud inventory \- Rename the <em class="title-reference">token</em> option to <em class="title-reference">api\_token</em>\, use aliases for backward compatibility\.
* inventory \- Add <em class="title-reference">hostname</em> option used to template the hostname of the instances\.
* inventory \- Add <em class="title-reference">hostvars\_prefix</em> and hostvars\_suffix\` options to customize the inventory host variables keys\.
* network \- Allow renaming networks\.
* primary\_ip \- Use the <em class="title-reference">server</em> option to assign a Primary IP being created to a server\.
* server \- Allow passing Datacenter name or ID to the <em class="title-reference">datacenter</em> argument\.
* server \- Allow passing Image name or ID to the <em class="title-reference">image</em> argument\.
* server \- Allow passing Location name or ID to the <em class="title-reference">location</em> argument\.
* server \- Allow passing SSH Keys names or IDs to the <em class="title-reference">ssh\_keys</em> argument\.
* server \- Allow passing Volume names or IDs to the <em class="title-reference">volumes</em> argument\.
* server \- Renamed the <em class="title-reference">allow\_deprecated\_image</em> option to <em class="title-reference">image\_allow\_deprecated</em>\.

<a id="ibm-storage-virtualize-4"></a>
#### ibm\.storage\_virtualize

* ibm\_sv\_manage\_replication\_policy \- Added support to configure a 2\-site\-ha policy\.
* ibm\_sv\_manage\_snapshot \- Added support to restore entire volumegroup from a snapshot of that volumegroup\.
* ibm\_sv\_manage\_snapshot \- Added support to restore subset of volumes of a volumegroup from a snapshot
* ibm\_svc\_host \- Added support to create nvmetcp host\.
* ibm\_svc\_info \- Added support to display information about partition\, quorum\, IO group\, VG replication and enclosure\, snmp server and ldap server
* ibm\_svc\_info \- Added support to display information about thinclone/clone volumes and volumegroups\.
* ibm\_svc\_manage\_volume \- Added support to create clone or thinclone from snapshot
* ibm\_svc\_manage\_volumgroup \- Added support to create clone or thinkclone volumegroup from snapshot from a subset of volumes
* ibm\_svc\_manage\_volumgroup \- Added support to delete volumegroups keeping volumes via \'evictvolumes\'\.

<a id="infoblox-nios-modules-5"></a>
#### infoblox\.nios\_modules

* Ansible core version in the dependencies updated to 2\.14 or later\.

<a id="inspur-ispim-2"></a>
#### inspur\.ispim

* Modify ansible\-test\.yml to add the ansible 2\.17 test [https\://github\.com/ispim/inspur\.ispim/pull/33](https\://github\.com/ispim/inspur\.ispim/pull/33)\.
* Modify ansible\-test\.yml to add the ansible2\.16 test\.
* Modify edit\_smtp\_com and add description information\.

<a id="junipernetworks-junos-1"></a>
#### junipernetworks\.junos

* Add support for cli\_restore functionality\.
* Please refer the PR to know more about core changes \([https\://github\.com/ansible\-collections/ansible\.netcommon/pull/618](https\://github\.com/ansible\-collections/ansible\.netcommon/pull/618)\)\.
* cli\_restore module is part of netcommon\.

<a id="kubernetes-core-1"></a>
#### kubernetes\.core

* helm \- add <code>reuse\_values</code> and <code>reset\_values</code> support to helm module \([https\://github\.com/ansible\-collections/kubernetes\.core/issues/394](https\://github\.com/ansible\-collections/kubernetes\.core/issues/394)\)\.
* k8s \- add new option <code>delete\_all</code> to support deletion of all resources when state is set to <code>absent</code>\. \([https\://github\.com/ansible\-collections/kubernetes\.core/issues/504](https\://github\.com/ansible\-collections/kubernetes\.core/issues/504)\)
* k8s\, k8s\_info \- add a hidden\_fields option to allow fields to be hidden in the results of k8s and k8s\_info
* k8s\_drain \- add ability to filter the list of pods to be drained by a pod label selector \([https\://github\.com/ansible\-collections/kubernetes\.core/issues/474](https\://github\.com/ansible\-collections/kubernetes\.core/issues/474)\)\.
* kubectl \- added support of local enviroment variable that will be used for kubectl and may be requried for establishing connections ifself \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/702](https\://github\.com/ansible\-collections/kubernetes\.core/pull/702)\)
* kustomize \- new parameter added to \-\-enable\-helm \([https\://github\.com/ansible\-collections/kubernetes\.core/issues/568](https\://github\.com/ansible\-collections/kubernetes\.core/issues/568)\)

<a id="lowlydba-sqlserver-2"></a>
#### lowlydba\.sqlserver

* Add ability to prevent changing login\'s password\, even if password supplied\.
* Add new input strings to be compatible with dbops v0\.9\.x \([https\://github\.com/lowlydba/lowlydba\.sqlserver/pull/231](https\://github\.com/lowlydba/lowlydba\.sqlserver/pull/231)\)

<a id="microsoft-ad-5"></a>
#### microsoft\.ad

* Added <code>group/microsoft\.ad\.domain</code> module defaults group for the <code>computer</code>\, <code>group</code>\, <code>object\_info</code>\, <code>object</code>\, <code>ou</code>\, and <code>user</code> module\. Users can use this defaults group to set common connection options for these modules such as the <code>domain\_server</code>\, <code>domain\_username</code>\, and <code>domain\_password</code> options\.
* Added support for Jinja2 templating in ldap inventory\.
* Make <code>name</code> an optional parameter for the AD modules\. Either <code>name</code> or <code>identity</code> needs to be set with their respective behaviours\. If creating a new AD user and only <code>identity</code> is set\, that will be the value used for the name of the object\.
* Set minimum supported Ansible version to 2\.14 to align with the versions still supported by Ansible\.
* object\_info \- Add ActiveDirectory module import

<a id="netapp-ontap-5"></a>
#### netapp\.ontap

* na\_ontap\_cifs \- new option <em class="title-reference">offline\_files</em> added in REST\, requires ONTAP 9\.10 or later\.
* na\_ontap\_cifs\_server \- new option <em class="title-reference">is\_multichannel\_enabled</em> added in REST\, requires ONTAP 9\.10 or later\.
* na\_ontap\_cifs\_server \- new option <em class="title-reference">lm\_compatibility\_level</em> added in REST\, requires ONTAP 9\.8 or later\.
* na\_ontap\_cluster \- new option <em class="title-reference">certificate\.uuid</em> added in REST\, requires ONTAP 9\.10 or later\.
* na\_ontap\_cluster\_peer \- added REST only support for modifying remote intercluster addresses in cluster peer relation\.
* na\_ontap\_ems\_destination \- new options <em class="title-reference">syslog</em>\, <em class="title-reference">port</em>\, <em class="title-reference">transport</em>\, <em class="title-reference">message\_format</em>\, <em class="title-reference">timestamp\_format\_override</em> and <em class="title-reference">hostname\_format\_override</em> added in REST\, requires ONTAP 9\.12\.1 or later\.
* na\_ontap\_export\_policy\_rule \- added <em class="title-reference">actions</em> and <em class="title-reference">modify</em> in module output\.
* na\_ontap\_file\_security\_permissions\_acl \- added <em class="title-reference">actions</em> and <em class="title-reference">modify</em> in module output\.
* na\_ontap\_igroup\_initiator \- added <em class="title-reference">actions</em> in module output\.
* na\_ontap\_lun\_map \- added <em class="title-reference">actions</em> in module output\.
* na\_ontap\_lun\_map\_reporting\_nodes \- added <em class="title-reference">actions</em> in module output\.
* na\_ontap\_name\_mappings \- added <em class="title-reference">actions</em> and <em class="title-reference">modify</em> in module output\.
* na\_ontap\_net\_ifgrp \- updated documentation for parameter <em class="title-reference">name</em>\.
* na\_ontap\_node \- added <em class="title-reference">modify</em> in module output\.
* na\_ontap\_rest\_info \- added warning message if given subset doesn\'t support option <em class="title-reference">owning\_resource</em>\.
* na\_ontap\_s3\_services \- create\, modify S3 service returns <em class="title-reference">s3\_service\_info</em> in module output\.
* na\_ontap\_snapmirror \- updated resync and resume operation for synchronous snapmirror relationship in REST\.
* na\_ontap\_storage\_auto\_giveback \- added information on modified attributes in module output\.
* na\_ontap\_vscan\_scanner\_pool \- added REST support to Vscan Scanner Pools Configuration module\, requires ONTAP 9\.6 or later\.
* na\_ontap\_vserver\_audit \- new options <em class="title-reference">schedule\.\*</em> added under <em class="title-reference">log\.rotation</em>\, requires ONTAP 9\.6 or later\.

<a id="netapp-storagegrid"></a>
#### netapp\.storagegrid

* na\_sg\_grid\_account \- New option <code>allow\_select\_object\_content</code> for enabling use of the S3 SelectObjectContent API\.
* na\_sg\_grid\_account \- New option <code>description</code> for setting additional identifying information for the tenant account\.

<a id="netbox-netbox-5"></a>
#### netbox\.netbox

* CI \- CI adjustments \[\#1154\]\([https\://github\.com/netbox\-community/ansible\_modules/pull/1154](https\://github\.com/netbox\-community/ansible\_modules/pull/1154)\) \[\#1155\]\([https\://github\.com/netbox\-community/ansible\_modules/pull/1155](https\://github\.com/netbox\-community/ansible\_modules/pull/1155)\) \[\#1157\]\([https\://github\.com/netbox\-community/ansible\_modules/pull/1157](https\://github\.com/netbox\-community/ansible\_modules/pull/1157)\)
* nb\_inventory \- Add Virtual Disks to inventory \[\#1188\]\([https\://github\.com/netbox\-community/ansible\_modules/pull/1188](https\://github\.com/netbox\-community/ansible\_modules/pull/1188)\)
* nb\_inventory \- Add facility group\_by option \[\#1059\]\([https\://github\.com/netbox\-community/ansible\_modules/pull/1059](https\://github\.com/netbox\-community/ansible\_modules/pull/1059)\)
* nb\_inventory \- Don\'t extract null values from custom fields \[\#1184\]\([https\://github\.com/netbox\-community/ansible\_modules/pull/1184](https\://github\.com/netbox\-community/ansible\_modules/pull/1184)\)
* nb\_inventory \- Enable ansible\-vault strings in config\-context data \[\#1114\]\([https\://github\.com/netbox\-community/ansible\_modules/pull/1114](https\://github\.com/netbox\-community/ansible\_modules/pull/1114)\)
* nb\_inventory \- Improve documentation for oob\_ip\_as\_primary\_ip \[\#1218\]\([https\://github\.com/netbox\-community/ansible\_modules/pull/1218](https\://github\.com/netbox\-community/ansible\_modules/pull/1218)\)
* nb\_inventory \- Make oob\_ip available regardless of oob\_ip\_as\_primary\_ip option \[\#1211\]\([https\://github\.com/netbox\-community/ansible\_modules/pull/1211](https\://github\.com/netbox\-community/ansible\_modules/pull/1211)\)
* nb\_lookup \- Add custom field choice set \[\#1186\]\([https\://github\.com/netbox\-community/ansible\_modules/pull/1186](https\://github\.com/netbox\-community/ansible\_modules/pull/1186)\)
* nb\_lookup \- Add endpoint for Virtual Disks \[\#1177\]\([https\://github\.com/netbox\-community/ansible\_modules/pull/1177](https\://github\.com/netbox\-community/ansible\_modules/pull/1177)\)
* nb\_lookup \- Add new VPN endpoints for NetBox 3\.7 support \[\#1162\]\([https\://github\.com/netbox\-community/ansible\_modules/pull/1162](https\://github\.com/netbox\-community/ansible\_modules/pull/1162)\)
* netbox\_device\_type and netbox\_rack \- Change u\_height to float \[\#1200\]\([https\://github\.com/netbox\-community/ansible\_modules/pull/1200](https\://github\.com/netbox\-community/ansible\_modules/pull/1200)\)
* netbox\_export\_templates \- Update documentation \[\#1214\]\([https\://github\.com/netbox\-community/ansible\_modules/pull/1214](https\://github\.com/netbox\-community/ansible\_modules/pull/1214)\)
* netbox\_platform \- Add config\_template option to netbox\_platform \[\#1119\]\([https\://github\.com/netbox\-community/ansible\_modules/pull/1119](https\://github\.com/netbox\-community/ansible\_modules/pull/1119)\)
* netbox\_power\_port \- Add label \[\#1202\]\([https\://github\.com/netbox\-community/ansible\_modules/pull/1202](https\://github\.com/netbox\-community/ansible\_modules/pull/1202)\)
* netbox\_power\_port\_template \- Add option module\_type to netbox\_power\_port\_template \[\#1105\]\([https\://github\.com/netbox\-community/ansible\_modules/pull/1105](https\://github\.com/netbox\-community/ansible\_modules/pull/1105)\)
* netbox\_rack\_role \- Add description option \[\#1143\]\([https\://github\.com/netbox\-community/ansible\_modules/pull/1143](https\://github\.com/netbox\-community/ansible\_modules/pull/1143)\)
* netbox\_virtual\_disk \- New module \[\#1153\]\([https\://github\.com/netbox\-community/ansible\_modules/pull/1153](https\://github\.com/netbox\-community/ansible\_modules/pull/1153)\)
* netbox\_virtual\_machine and netbox\_device \- Add option config\_template \[\#1171\]\([https\://github\.com/netbox\-community/ansible\_modules/pull/1171](https\://github\.com/netbox\-community/ansible\_modules/pull/1171)\)

<a id="purestorage-flasharray-10"></a>
#### purestorage\.flasharray

* all \- <code>distro</code> package added as a pre\-requisite
* multiple \- Remove packaging pre\-requisite\.
* multiple \- Where only REST 2\.x endpoints are used\, convert to REST 2\.x methodology\.
* purefa\_arrayname \- Convert to REST v2
* purefa\_dns \- Added facility to add a CA certifcate to management DNS and check peer\.
* purefa\_eula \- Only sign if not previously signed\. From REST 2\.30 name\, title and company are no longer required
* purefa\_hg \- Add support to rename existing hostgroup
* purefa\_info \- Add NSID value for NVMe namespace in <em class="title-reference">hosts</em> response
* purefa\_info \- Add <code>is\_local</code> parameter for snapshots
* purefa\_info \- Add performance data for some subsets
* purefa\_info \- Add service\_mode to identify if array is Evergreen//One or standard FlashArray
* purefa\_info \- Add support for controller uptime from Purity//FA 6\.6\.3
* purefa\_info \- Expose NFS security flavor for policies
* purefa\_info \- Expose cloud capacity details if array is a Cloud Block Store\.
* purefa\_info \- Subset <em class="title-reference">pgroups</em> now also provides a new dict called <em class="title-reference">deleted\_pgroups</em>
* purefa\_inventory \- Convert to REST v2
* purefa\_ntp \- Convert to REST v2
* purefa\_offload \- Convert to REST v2
* purefa\_offload \- Remove <em class="title-reference">nfs</em> as an option when Purity//FA 6\.6\.0 or higher is detected
* purefa\_pg \- Enhance <code>state absent</code> to work on volumes\, hosts and hostgroups
* purefa\_pgsnap \- Module now requires minimum FlashArray Purity//FA 6\.1\.0
* purefa\_policy \- Add SMB user based enumeration parameter
* purefa\_policy \- Added NFS security flavors for accessing files in the mount point\.
* purefa\_policy \- Remove default setting for nfs\_version to allow for change of version at policy level
* purefa\_ra \- Add <code>present</code> and <code>absent</code> as valid <code>state</code> options
* purefa\_ra \- Add connecting as valid status of RA to perform operations on
* purefa\_ra \- Convert to REST v2
* purefa\_snap \- Add <code>created\_epoch</code> parameter in response
* purefa\_snap \- Add support for suffix on remote offload snapshots
* purefa\_syslog \- <code>name</code> becomes a required parameter as module converts to full REST 2 support
* purefa\_vnc \- Convert to REST v2

<a id="purestorage-flashblade-5"></a>
#### purestorage\.flashblade

* purefb\_bucket \- Add support for public buckets
* purefb\_bucket \- Add support for strict 17a\-4 WORM compliance\.
* purefb\_bucket \- From REST 2\.12 the <em class="title-reference">mode</em> parameter default changes to <em class="title-reference">multi\-site\-writable</em>\.
* purefb\_connect \- Increase Fan\-In and Fan\-Out maximums
* purefb\_ds \- Add <em class="title-reference">force\_bind\_password</em> parameter to allow module to be idempotent\.
* purefb\_fs \- Add <code>group\_ownership</code> parameter from Purity//FB 4\.4\.0\.
* purefb\_fs \- Added SMB Continuous Availability parameter\. Requires REST 2\.12 or higher\.
* purefb\_info \- Added enhanced information for buckets\, filesystems and snapshots\, based on new features in REST 2\.12
* purefb\_info \- Show array network access policy from Purity//FB 4\.4\.0
* purefb\_policy \- Add support for network access policies from Purity//FB 4\.4\.0
* purefb\_s3acc \- Add support for public buckets
* purefb\_s3acc \- Remove default requirements for <code>hard\_limit</code> and <code>default\_hard\_limit</code>

<a id="telekom-mms-icinga-director-2"></a>
#### telekom\_mms\.icinga\_director

* Extended docs and examples for multiple assign\_filter conditions \([https\://github\.com/telekom\-mms/ansible\-collection\-icinga\-director/pull/227](https\://github\.com/telekom\-mms/ansible\-collection\-icinga\-director/pull/227)\)
* Increase sleep to 5 seconds \([https\://github\.com/telekom\-mms/ansible\-collection\-icinga\-director/pull/245](https\://github\.com/telekom\-mms/ansible\-collection\-icinga\-director/pull/245)\)

<a id="theforeman-foreman-4"></a>
#### theforeman\.foreman

* content\_view\_publish role \- allow passing <code>async</code> and <code>poll</code> to the module \([https\://github\.com/theforeman/foreman\-ansible\-modules/pull/1676](https\://github\.com/theforeman/foreman\-ansible\-modules/pull/1676)\)
* convert2rhel role \- install <code>convert2rhel</code> from <code>cdn\-public\.redhat\.com</code>\, dropping the requirement of a custom CA cert

<a id="vmware-vmware-rest-2"></a>
#### vmware\.vmware\_rest

* Add requires\_ansible to manifest \([https\://github\.com/ansible\-community/ansible\.content\_builder/pull/76](https\://github\.com/ansible\-community/ansible\.content\_builder/pull/76)\)\.
* Generate action\_groups for the vmware\.vmware\_rest collection \([https\://github\.com/ansible\-community/ansible\.content\_builder/issues/75](https\://github\.com/ansible\-community/ansible\.content\_builder/issues/75)\)\.
* Use 7\.0 U3 API spec to build the modules \([https\://github\.com/ansible\-collections/vmware\.vmware\_rest/pull/449](https\://github\.com/ansible\-collections/vmware\.vmware\_rest/pull/449)\)\.
* Use folder attribute for host and dc module only \([https\://github\.com/ansible\-community/ansible\.content\_builder/pull/79](https\://github\.com/ansible\-community/ansible\.content\_builder/pull/79)\)\.

<a id="vultr-cloud-1"></a>
#### vultr\.cloud

* Added retry on HTTP 504 returned by the API \([https\://github\.com/vultr/ansible\-collection\-vultr/pull/104](https\://github\.com/vultr/ansible\-collection\-vultr/pull/104)\)\.
* Implemented a feature to distinguish resources by region if available\. This allows to have identical name per region e\.g\. a VPC named <code>default</code> in each region\. \([https\://github\.com/vultr/ansible\-collection\-vultr/pull/98](https\://github\.com/vultr/ansible\-collection\-vultr/pull/98)\)\.
* instance \- Added a new param <code>user\_scheme</code> to change user scheme to non\-root on Linux while creating the instance \([https\://github\.com/vultr/ansible\-collection\-vultr/issues/96](https\://github\.com/vultr/ansible\-collection\-vultr/issues/96)\)\.

<a id="breaking-changes--porting-guide"></a>
### Breaking Changes / Porting Guide

<a id="ansible-core-24"></a>
#### Ansible\-core

* assert \- Nested templating may result in an inability for the conditional to be evaluated\. See the porting guide for more information\.

<a id="amazon-aws-6"></a>
#### amazon\.aws

* amazon\.aws collection \- Support for ansible\-core \< 2\.15 has been dropped \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2093](https\://github\.com/ansible\-collections/amazon\.aws/pull/2093)\)\.
* iam\_role \- <code>iam\_role\.assume\_role\_policy\_document</code> is no longer converted from CamelCase to snake\_case \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2040](https\://github\.com/ansible\-collections/amazon\.aws/pull/2040)\)\.
* iam\_role\_info \- <code>iam\_role\.assume\_role\_policy\_document</code> is no longer converted from CamelCase to snake\_case \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2040](https\://github\.com/ansible\-collections/amazon\.aws/pull/2040)\)\.
* kms\_key \- the <code>policies</code> return value has been renamed to <code>key\_policies</code> the contents has not been changed \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2040](https\://github\.com/ansible\-collections/amazon\.aws/pull/2040)\)\.
* kms\_key\_info \- the <code>policies</code> return value has been renamed to <code>key\_policies</code> the contents has not been changed \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2040](https\://github\.com/ansible\-collections/amazon\.aws/pull/2040)\)\.
* lambda\_event \- \| <code>batch\_size</code> no longer defaults to 100\. According to the boto3 API \([https\://boto3\.amazonaws\.com/v1/documentation/api/1\.26\.78/reference/services/lambda\.html\#Lambda\.Client\.create\_event\_source\_mapping](https\://boto3\.amazonaws\.com/v1/documentation/api/1\.26\.78/reference/services/lambda\.html\#Lambda\.Client\.create\_event\_source\_mapping)\)\, <code>batch\_size</code> defaults to 10 for sqs sources and to 100 for stream sources \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2025](https\://github\.com/ansible\-collections/amazon\.aws/pull/2025)\)\.

<a id="cloud-common"></a>
#### cloud\.common

* Bump minimum Python supported version to 3\.9\.
* Remove support for ansible\-core \< 2\.14\.

<a id="community-aws-1"></a>
#### community\.aws

* The community\.aws collection has dropped support for <code>botocore\<1\.29\.0</code> and <code>boto3\<1\.26\.0</code>\. Most modules will continue to work with older versions of the AWS SDK\, however compatability with older versions of the SDK is not guaranteed and will not be tested\. When using older versions of the SDK a warning will be emitted by Ansible \([https\://github\.com/ansible\-collections/amazon\.aws/pull/1763](https\://github\.com/ansible\-collections/amazon\.aws/pull/1763)\)\.
* aws\_region\_info \- The module has been migrated from the <code>community\.aws</code> collection\. Playbooks using the Fully Qualified Collection Name for this module should be updated to use <code>amazon\.aws\.aws\_region\_info</code>\.
* aws\_s3\_bucket\_info \- The module has been migrated from the <code>community\.aws</code> collection\. Playbooks using the Fully Qualified Collection Name for this module should be updated to use <code>amazon\.aws\.aws\_s3\_bucket\_info</code>\.
* community\.aws collection \- Support for ansible\-core \< 2\.15 has been dropped \([https\://github\.com/ansible\-collections/community\.aws/pull/2074](https\://github\.com/ansible\-collections/community\.aws/pull/2074)\)\.
* community\.aws collection \- due to the AWS SDKs announcing the end of support for Python less than 3\.7 \([https\://aws\.amazon\.com/blogs/developer/python\-support\-policy\-updates\-for\-aws\-sdks\-and\-tools/](https\://aws\.amazon\.com/blogs/developer/python\-support\-policy\-updates\-for\-aws\-sdks\-and\-tools/)\) support for Python less than 3\.7 by this collection wss been deprecated in release 6\.0\.0 and removed in release 7\.0\.0\. \([https\://github\.com/ansible\-collections/amazon\.aws/pull/1763](https\://github\.com/ansible\-collections/amazon\.aws/pull/1763)\)\.
* iam\_access\_key \- The module has been migrated from the <code>community\.aws</code> collection\. Playbooks using the Fully Qualified Collection Name for this module should be updated to use <code>amazon\.aws\.iam\_access\_key</code>\.
* iam\_access\_key\_info \- The module has been migrated from the <code>community\.aws</code> collection\. Playbooks using the Fully Qualified Collection Name for this module should be updated to use <code>amazon\.aws\.iam\_access\_key\_info</code>\.
* iam\_group \- The module has been migrated from the <code>community\.aws</code> collection\. Playbooks using the Fully Qualified Collection Name for this module should be updated to use <code>amazon\.aws\.iam\_group</code> \([https\://github\.com/ansible\-collections/community\.aws/pull/1945](https\://github\.com/ansible\-collections/community\.aws/pull/1945)\)\.
* iam\_managed\_policy \- The module has been migrated from the <code>community\.aws</code> collection\. Playbooks using the Fully Qualified Collection Name for this module should be updated to use <code>amazon\.aws\.iam\_managed\_policy</code> \([https\://github\.com/ansible\-collections/community\.aws/pull/1954](https\://github\.com/ansible\-collections/community\.aws/pull/1954)\)\.
* iam\_mfa\_device\_info \- The module has been migrated from the <code>community\.aws</code> collection\. Playbooks using the Fully Qualified Collection Name for this module should be updated to use <code>amazon\.aws\.iam\_mfa\_device\_info</code> \([https\://github\.com/ansible\-collections/community\.aws/pull/1953](https\://github\.com/ansible\-collections/community\.aws/pull/1953)\)\.
* iam\_password\_policy \- The module has been migrated from the <code>community\.aws</code> collection\. Playbooks using the Fully Qualified Collection Name for this module should be updated to use <code>amazon\.aws\.iam\_password\_policy</code>\.
* iam\_role \- The module has been migrated from the <code>community\.aws</code> collection\. Playbooks using the Fully Qualified Collection Name for this module should be updated to use <code>amazon\.aws\.iam\_role</code> \([https\://github\.com/ansible\-collections/community\.aws/pull/1948](https\://github\.com/ansible\-collections/community\.aws/pull/1948)\)\.
* iam\_role\_info \- The module has been migrated from the <code>community\.aws</code> collection\. Playbooks using the Fully Qualified Collection Name for this module should be updated to use <code>amazon\.aws\.iam\_role\_info</code> \([https\://github\.com/ansible\-collections/community\.aws/pull/1948](https\://github\.com/ansible\-collections/community\.aws/pull/1948)\)\.
* s3\_bucket\_info \- The module has been migrated from the <code>community\.aws</code> collection\. Playbooks using the Fully Qualified Collection Name for this module should be updated to use <code>amazon\.aws\.s3\_bucket\_info</code>\.
* sts\_assume\_role \- The module has been migrated from the <code>community\.aws</code> collection\. Playbooks using the Fully Qualified Collection Name for this module should be updated to use <code>amazon\.aws\.sts\_assume\_role</code>\.

<a id="community-ciscosmb-1"></a>
#### community\.ciscosmb

* in facts of interface \'bandwith\' changed to \'bandwidth\'

<a id="community-dns-10"></a>
#### community\.dns

* The default for the <code>txt\_character\_encoding</code> options in various modules and plugins changed from <code>octal</code> to <code>decimal</code> \([https\://github\.com/ansible\-collections/community\.dns/pull/196](https\://github\.com/ansible\-collections/community\.dns/pull/196)\)\.
* inventory plugins \- <code>filters</code> is now no longer an alias of <code>simple\_filters</code>\, but a new\, different option \([https\://github\.com/ansible\-collections/community\.dns/pull/196](https\://github\.com/ansible\-collections/community\.dns/pull/196)\)\.
* inventory plugins \- the <code>plugin</code> option is now required \([https\://github\.com/ansible\-collections/community\.dns/pull/196](https\://github\.com/ansible\-collections/community\.dns/pull/196)\)\.
* lookup\, lookup\_as\_dict \- the default for <code>search</code> changed from <code>false</code> \(implicit default for community\.dns 2\.x\.y\) to <code>true</code> \([https\://github\.com/ansible\-collections/community\.dns/issues/200](https\://github\.com/ansible\-collections/community\.dns/issues/200)\, [https\://github\.com/ansible\-collections/community\.dns/pull/201](https\://github\.com/ansible\-collections/community\.dns/pull/201)\)\.

<a id="community-general-23"></a>
#### community\.general

* cpanm \- the default of the <code>mode</code> option changed from <code>compatibility</code> to <code>new</code> \([https\://github\.com/ansible\-collections/community\.general/pull/8198](https\://github\.com/ansible\-collections/community\.general/pull/8198)\)\.
* django\_manage \- the module now requires Django \>\= 4\.1 \([https\://github\.com/ansible\-collections/community\.general/pull/8198](https\://github\.com/ansible\-collections/community\.general/pull/8198)\)\.
* django\_manage \- the module will now fail if <code>virtualenv</code> is specified but no virtual environment exists at that location \([https\://github\.com/ansible\-collections/community\.general/pull/8198](https\://github\.com/ansible\-collections/community\.general/pull/8198)\)\.
* redfish\_command\, redfish\_config\, redfish\_info \- change the default for <code>timeout</code> from 10 to 60 \([https\://github\.com/ansible\-collections/community\.general/pull/8198](https\://github\.com/ansible\-collections/community\.general/pull/8198)\)\.

<a id="community-hrobot-3"></a>
#### community\.hrobot

* robot inventory plugin \- <code>filters</code> is now no longer an alias of <code>simple\_filters</code>\, but a new\, different option \([https\://github\.com/ansible\-collections/community\.hrobot/pull/101](https\://github\.com/ansible\-collections/community\.hrobot/pull/101)\)\.

<a id="community-okd"></a>
#### community\.okd

* Bump minimum Python suupported version to 3\.9 \([https\://github\.com/openshift/community\.okd/pull/202](https\://github\.com/openshift/community\.okd/pull/202)\)\.
* Remove support for ansible\-core \< 2\.14 \([https\://github\.com/openshift/community\.okd/pull/202](https\://github\.com/openshift/community\.okd/pull/202)\)\.

<a id="hetzner-hcloud-1"></a>
#### hetzner\.hcloud

* Drop support for ansible\-core 2\.13\.
* certificate \- The <em class="title-reference">not\_valid\_before</em> and <em class="title-reference">not\_valid\_after</em> values are now returned as ISO\-8601 formatted strings\.
* certificate\_info \- The <em class="title-reference">not\_valid\_before</em> and <em class="title-reference">not\_valid\_after</em> values are now returned as ISO\-8601 formatted strings\.
* inventory \- Remove the deprecated <em class="title-reference">api\_token\_env</em> option\, you may use the <em class="title-reference">ansible\.builtin\.env</em> lookup as alternative\.
* iso\_info \- The <em class="title-reference">deprecated</em> value is now returned as ISO\-8601 formatted strings\.

<a id="kubernetes-core-2"></a>
#### kubernetes\.core

* Remove support for ansible\-core \< 2\.14
* Update python kubernetes library to 24\.2\.0\, helm/kind\-action to 1\.8\.0\, kubernetes \>\= 1\.24\.

<a id="theforeman-foreman-5"></a>
#### theforeman\.foreman

* content\_view\_filter \- stop managing rules from this module\, <code>content\_view\_filter\_rule</code> should be used for that
* inventory plugin \- do not default to <code>http\://localhost\:3000</code> as the Foreman URL\, providing a URL is now mandatory

<a id="vmware-vmware-rest-3"></a>
#### vmware\.vmware\_rest

* Remove support for ansible\-core \< 2\.14

<a id="deprecated-features-7"></a>
### Deprecated Features

* The <code>inspur\.sm</code> collection is considered unmaintained and will be removed from Ansible 11 if no one starts maintaining it again before Ansible 11\.
  See [Collections Removal Process for unmaintained collections](https\://docs\.ansible\.com/ansible/devel/community/collection\_contributors/collection\_package\_removal\.html\#unmaintained\-collections) for more details\, including for how this can be cancelled \([https\://forum\.ansible\.com/t/2854](https\://forum\.ansible\.com/t/2854)\)\.
  After removal\, users can still install this collection with <code>ansible\-galaxy collection install inspur\.sm</code>\.
* The <code>netapp\.storagegrid</code> collection is considered unmaintained and will be removed from Ansible 11 if no one starts maintaining it again before Ansible 11\.
  See [Collections Removal Process for unmaintained collections](https\://docs\.ansible\.com/ansible/devel/community/collection\_contributors/collection\_package\_removal\.html\#unmaintained\-collections) for more details\, including for how this can be cancelled \([https\://forum\.ansible\.com/t/2811](https\://forum\.ansible\.com/t/2811)\)\.
  After removal\, users can still install this collection with <code>ansible\-galaxy collection install netapp\.storagegrid</code>\.

<a id="ansible-core-25"></a>
#### Ansible\-core

* Old style vars plugins which use the entrypoints <em class="title-reference">get\_host\_vars</em> or <em class="title-reference">get\_group\_vars</em> are deprecated\. The plugin should be updated to inherit from <em class="title-reference">BaseVarsPlugin</em> and define a <em class="title-reference">get\_vars</em> method as the entrypoint\.
* The \'required\' parameter in \'ansible\.module\_utils\.common\.process\.get\_bin\_path\' API is deprecated \([https\://github\.com/ansible/ansible/issues/82464](https\://github\.com/ansible/ansible/issues/82464)\)\.
* <code>module\_utils</code> \- importing the following convenience helpers from <code>ansible\.module\_utils\.basic</code> has been deprecated\: <code>get\_exception</code>\, <code>literal\_eval</code>\, <code>\_literal\_eval</code>\, <code>datetime</code>\, <code>signal</code>\, <code>types</code>\, <code>chain</code>\, <code>repeat</code>\, <code>PY2</code>\, <code>PY3</code>\, <code>b</code>\, <code>binary\_type</code>\, <code>integer\_types</code>\, <code>iteritems</code>\, <code>string\_types</code>\, <code>test\_type</code>\, <code>map</code> and <code>shlex\_quote</code>\.
* ansible\-doc \- role entrypoint attributes are deprecated and eventually will no longer be shown in ansible\-doc from ansible\-core 2\.20 on \([https\://github\.com/ansible/ansible/issues/82639](https\://github\.com/ansible/ansible/issues/82639)\, [https\://github\.com/ansible/ansible/pull/82678](https\://github\.com/ansible/ansible/pull/82678)\)\.
* paramiko connection plugin\, configuration items in the global scope are being deprecated and will be removed in favor or the existing same options in the plugin itself\. Users should not need to change anything \(how to configure them are the same\) but plugin authors using the global constants should move to using the plugin\'s get\_option\(\)\.

<a id="amazon-aws-7"></a>
#### amazon\.aws

* aws\_ec2 inventory plugin \- removal of the previously deprecated <code>include\_extra\_api\_calls</code> option has been assigned to release 9\.0\.0 \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2040](https\://github\.com/ansible\-collections/amazon\.aws/pull/2040)\)\.
* cloudformation \- the <code>template</code> parameter has been deprecated and will be removed in a release after 2026\-05\-01\.  The <code>template\_body</code> parameter can be used in conjungtion with the lookup plugin \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2048](https\://github\.com/ansible\-collections/amazon\.aws/pull/2048)\)\.
* iam\_policy \- removal of the previously deprecated <code>policies</code> return key has been assigned to release 9\.0\.0\.  Use the <code>policy\_names</code> return key instead \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2040](https\://github\.com/ansible\-collections/amazon\.aws/pull/2040)\)\.
* iam\_role\_info \- in a release after 2026\-05\-01 paths must begin and end with <code>/</code> \([https\://github\.com/ansible\-collections/amazon\.aws/pull/1998](https\://github\.com/ansible\-collections/amazon\.aws/pull/1998)\)\.
* module\_utils\.botocore \- the <code>boto3</code> parameter for <code>get\_aws\_connection\_info\(\)</code> will be removed in a release after 2025\-05\-01\. The <code>boto3</code> parameter has been ignored since release 4\.0\.0 \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2047](https\://github\.com/ansible\-collections/amazon\.aws/pull/2047)\)\.
* module\_utils\.botocore \- the <code>boto3</code> parameter for <code>get\_aws\_region\(\)</code> will be removed in a release after 2025\-05\-01\. The <code>boto3</code> parameter has been ignored since release 4\.0\.0 \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2047](https\://github\.com/ansible\-collections/amazon\.aws/pull/2047)\)\.
* module\_utils\.ec2 \- the <code>boto3</code> parameter for <code>get\_ec2\_security\_group\_ids\_from\_names\(\)</code> will be removed in a release after 2025\-05\-01\. The <code>boto3</code> parameter has been ignored since release 4\.0\.0 \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2047](https\://github\.com/ansible\-collections/amazon\.aws/pull/2047)\)\.
* rds\_param\_group \- the <code>rds\_param\_group</code> module has been renamed to <code>rds\_instance\_param\_group</code>\. The usage of the module has not changed\. The rds\_param\_group alias will be removed in version 10\.0\.0 \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2058](https\://github\.com/ansible\-collections/amazon\.aws/pull/2058)\)\.

<a id="community-aws-2"></a>
#### community\.aws

* aws\_glue\_connection \- updated the deprecation for removal of the <code>connection\_parameters</code> return key from <code>after 2024\-06\-01</code> to release version <code>9\.0\.0</code>\, it is being replaced by the <code>raw\_connection\_parameters</code> key \([https\://github\.com/ansible\-collections/community\.aws/pull/518](https\://github\.com/ansible\-collections/community\.aws/pull/518)\)\.
* ecs\_cluster \- updated the deprecation for updated default of <code>purge\_capacity\_providers</code>\, the current default of <code>False</code> will be changed to <code>True</code> in release <code>9\.0\.0</code>\.  To maintain the current behaviour explicitly set <code>purge\_capacity\_providers\=False</code> \([https\://github\.com/ansible\-collections/community\.aws/pull/1640](https\://github\.com/ansible\-collections/community\.aws/pull/1640)\)\.
* ecs\_service \- updated the deprecation for updated default of <code>purge\_placement\_constraints</code>\, the current default of <code>False</code> will be changed to <code>True</code> in release <code>9\.0\.0</code>\.  To maintain the current behaviour explicitly set <code>purge\_placement\_constraints\=False</code> \([https\://github\.com/ansible\-collections/community\.aws/pull/1716](https\://github\.com/ansible\-collections/community\.aws/pull/1716)\)\.
* ecs\_service \- updated the deprecation for updated default of <code>purge\_placement\_strategy</code>\, the current default of <code>False</code> will be changed to <code>True</code> in release <code>9\.0\.0</code>\.  To maintain the current behaviour explicitly set <code>purge\_placement\_strategy\=False</code> \([https\://github\.com/ansible\-collections/community\.aws/pull/1716](https\://github\.com/ansible\-collections/community\.aws/pull/1716)\)\.

<a id="community-crypto-6"></a>
#### community\.crypto

* acme documentation fragment \- the default <code>community\.crypto\.acme\[\.documentation\]</code> docs fragment is deprecated and will be removed from community\.crypto 3\.0\.0\. Replace it with both the new <code>community\.crypto\.acme\.basic</code> and <code>community\.crypto\.acme\.account</code> fragments \([https\://github\.com/ansible\-collections/community\.crypto/pull/735](https\://github\.com/ansible\-collections/community\.crypto/pull/735)\)\.
* acme\.backends module utils \- from community\.crypto on\, all implementations of <code>CryptoBackend</code> must override <code>get\_ordered\_csr\_identifiers\(\)</code>\. The current default implementation\, which simply sorts the result of <code>get\_csr\_identifiers\(\)</code>\, will then be removed \([https\://github\.com/ansible\-collections/community\.crypto/pull/725](https\://github\.com/ansible\-collections/community\.crypto/pull/725)\)\.
* acme\.backends module utils \- the <code>get\_cert\_information\(\)</code> method for a ACME crypto backend must be implemented from community\.crypto 3\.0\.0 on \([https\://github\.com/ansible\-collections/community\.crypto/pull/736](https\://github\.com/ansible\-collections/community\.crypto/pull/736)\)\.
* crypto\.module\_backends\.common module utils \- the <code>crypto\.module\_backends\.common</code> module utils is deprecated and will be removed from community\.crypto 3\.0\.0\. Use the improved <code>argspec</code> module util instead \([https\://github\.com/ansible\-collections/community\.crypto/pull/749](https\://github\.com/ansible\-collections/community\.crypto/pull/749)\)\.
* openssl\_csr\_pipe\, openssl\_privatekey\_pipe\, x509\_certificate\_pipe \- the current behavior of check mode is deprecated and will change in community\.crypto 3\.0\.0\. The current behavior is similar to the modules without <code>\_pipe</code>\: if the object needs to be \(re\-\)generated\, only the <code>changed</code> status is set\, but the object is not updated\. From community\.crypto 3\.0\.0 on\, the modules will ignore check mode and always act as if check mode is not active\. This behavior can already achieved now by adding <code>check\_mode\: false</code> to the task\. If you think this breaks your use\-case of this module\, please [create an issue in the community\.crypto repository](https\://github\.com/ansible\-collections/community\.crypto/issues/new/choose) \([https\://github\.com/ansible\-collections/community\.crypto/issues/712](https\://github\.com/ansible\-collections/community\.crypto/issues/712)\, [https\://github\.com/ansible\-collections/community\.crypto/pull/714](https\://github\.com/ansible\-collections/community\.crypto/pull/714)\)\.

<a id="community-dns-11"></a>
#### community\.dns

* hetzner\_dns\_records and hosttech\_dns\_records inventory plugins \- the <code>filters</code> option has been renamed to <code>simple\_filters</code>\. The old name will stop working in community\.hrobot 2\.0\.0 \([https\://github\.com/ansible\-collections/community\.dns/pull/181](https\://github\.com/ansible\-collections/community\.dns/pull/181)\)\.

<a id="community-docker-13"></a>
#### community\.docker

* docker\_compose \- the Docker Compose v1 module is deprecated and will be removed from community\.docker 4\.0\.0\. Please migrate to the <code>community\.docker\.docker\_compose\_v2</code> module\, which works with Docker Compose v2 \([https\://github\.com/ansible\-collections/community\.docker/issues/823](https\://github\.com/ansible\-collections/community\.docker/issues/823)\, [https\://github\.com/ansible\-collections/community\.docker/pull/833](https\://github\.com/ansible\-collections/community\.docker/pull/833)\)\.
* docker\_container \- the default <code>ignore</code> for the <code>image\_name\_mismatch</code> parameter has been deprecated and will switch to <code>recreate</code> in community\.docker 4\.0\.0\. A deprecation warning will be printed in situations where the default value is used and where a behavior would change once the default changes \([https\://github\.com/ansible\-collections/community\.docker/pull/703](https\://github\.com/ansible\-collections/community\.docker/pull/703)\)\.
* various modules and plugins \- the <code>ssl\_version</code> option has been deprecated and will be removed from community\.docker 4\.0\.0\. It has already been removed from Docker SDK for Python 7\.0\.0\, and was only necessary in the past to work around SSL/TLS issues \([https\://github\.com/ansible\-collections/community\.docker/pull/853](https\://github\.com/ansible\-collections/community\.docker/pull/853)\)\.

<a id="community-general-24"></a>
#### community\.general

* MH DependencyCtxMgr module\_utils \- deprecate <code>module\_utils\.mh\.mixin\.deps\.DependencyCtxMgr</code> in favour of <code>module\_utils\.deps</code> \([https\://github\.com/ansible\-collections/community\.general/pull/8280](https\://github\.com/ansible\-collections/community\.general/pull/8280)\)\.
* ModuleHelper module\_utils \- deprecate <code>plugins\.module\_utils\.module\_helper\.AnsibleModule</code> \([https\://github\.com/ansible\-collections/community\.general/pull/8280](https\://github\.com/ansible\-collections/community\.general/pull/8280)\)\.
* ModuleHelper module\_utils \- deprecate <code>plugins\.module\_utils\.module\_helper\.DependencyCtxMgr</code> \([https\://github\.com/ansible\-collections/community\.general/pull/8280](https\://github\.com/ansible\-collections/community\.general/pull/8280)\)\.
* ModuleHelper module\_utils \- deprecate <code>plugins\.module\_utils\.module\_helper\.StateMixin</code> \([https\://github\.com/ansible\-collections/community\.general/pull/8280](https\://github\.com/ansible\-collections/community\.general/pull/8280)\)\.
* ModuleHelper module\_utils \- deprecate <code>plugins\.module\_utils\.module\_helper\.VarDict\,</code> \([https\://github\.com/ansible\-collections/community\.general/pull/8280](https\://github\.com/ansible\-collections/community\.general/pull/8280)\)\.
* ModuleHelper module\_utils \- deprecate <code>plugins\.module\_utils\.module\_helper\.VarMeta</code> \([https\://github\.com/ansible\-collections/community\.general/pull/8280](https\://github\.com/ansible\-collections/community\.general/pull/8280)\)\.
* ModuleHelper module\_utils \- deprecate <code>plugins\.module\_utils\.module\_helper\.VarsMixin</code> \([https\://github\.com/ansible\-collections/community\.general/pull/8280](https\://github\.com/ansible\-collections/community\.general/pull/8280)\)\.
* ModuleHelper module\_utils \- deprecate use of <code>VarsMixin</code> in favor of using the <code>VardDict</code> module\_utils \([https\://github\.com/ansible\-collections/community\.general/pull/8226](https\://github\.com/ansible\-collections/community\.general/pull/8226)\)\.
* ModuleHelper vars module\_utils \- bump deprecation of <code>VarMeta</code>\, <code>VarDict</code> and <code>VarsMixin</code> to version 11\.0\.0 \([https\://github\.com/ansible\-collections/community\.general/pull/8226](https\://github\.com/ansible\-collections/community\.general/pull/8226)\)\.
* apt\_rpm \- the behavior of <code>state\=present</code> and <code>state\=installed</code> is deprecated and will change in community\.general 11\.0\.0\. Right now the module will upgrade a package to the latest version if one of these two states is used\. You should explicitly use <code>state\=latest</code> if you want this behavior\, and switch to <code>state\=present\_not\_latest</code> if you do not want to upgrade the package if it is already installed\. In community\.general 11\.0\.0 the behavior of <code>state\=present</code> and <code>state\=installed</code> will change to that of <code>state\=present\_not\_latest</code> \([https\://github\.com/ansible\-collections/community\.general/issues/8217](https\://github\.com/ansible\-collections/community\.general/issues/8217)\, [https\://github\.com/ansible\-collections/community\.general/pull/8285](https\://github\.com/ansible\-collections/community\.general/pull/8285)\)\.
* consul\_acl \- the module has been deprecated and will be removed in community\.general 10\.0\.0\. <code>consul\_token</code> and <code>consul\_policy</code> can be used instead \([https\://github\.com/ansible\-collections/community\.general/pull/7901](https\://github\.com/ansible\-collections/community\.general/pull/7901)\)\.
* django\_manage \- the <code>ack\_venv\_creation\_deprecation</code> option has no more effect and will be removed from community\.general 11\.0\.0 \([https\://github\.com/ansible\-collections/community\.general/pull/8198](https\://github\.com/ansible\-collections/community\.general/pull/8198)\)\.
* gitlab modules \- the basic auth method on GitLab API have been deprecated and will be removed in community\.general 10\.0\.0 \([https\://github\.com/ansible\-collections/community\.general/pull/8383](https\://github\.com/ansible\-collections/community\.general/pull/8383)\)\.
* hipchat callback plugin \- the hipchat service has been discontinued and the self\-hosted variant has been End of Life since 2020\. The callback plugin is therefore deprecated and will be removed from community\.general 10\.0\.0 if nobody provides compelling reasons to still keep it \([https\://github\.com/ansible\-collections/community\.general/issues/8184](https\://github\.com/ansible\-collections/community\.general/issues/8184)\, [https\://github\.com/ansible\-collections/community\.general/pull/8189](https\://github\.com/ansible\-collections/community\.general/pull/8189)\)\.
* irc \- the defaults <code>false</code> for <code>use\_tls</code> and <code>validate\_certs</code> have been deprecated and will change to <code>true</code> in community\.general 10\.0\.0 to improve security\. You can already improve security now by explicitly setting them to <code>true</code>\. Specifying values now disables the deprecation warning \([https\://github\.com/ansible\-collections/community\.general/pull/7578](https\://github\.com/ansible\-collections/community\.general/pull/7578)\)\.

<a id="community-hrobot-4"></a>
#### community\.hrobot

* robot inventory plugin \- the <code>filters</code> option has been renamed to <code>simple\_filters</code>\. The old name will stop working in community\.hrobot 2\.0\.0 \([https\://github\.com/ansible\-collections/community\.hrobot/pull/94](https\://github\.com/ansible\-collections/community\.hrobot/pull/94)\)\.

<a id="community-okd-1"></a>
#### community\.okd

* openshift \- the <code>openshift</code> inventory plugin has been deprecated and will be removed in release 4\.0\.0 \([https\://github\.com/ansible\-collections/kubernetes\.core/issues/31](https\://github\.com/ansible\-collections/kubernetes\.core/issues/31)\)\.

<a id="community-vmware-11"></a>
#### community\.vmware

* vmware\_guest\_tools\_info \- <em class="title-reference">vm\_tools\_install\_status</em> will be removed from next major version \(5\.0\.0\) of the collection since the API call that provides this information has been deprecated by VMware\. Use <em class="title-reference">vm\_tools\_running\_status</em> / <em class="title-reference">vm\_tools\_version\_status</em> instead \([https\://github\.com/ansible\-collections/community\.vmware/issues/2033](https\://github\.com/ansible\-collections/community\.vmware/issues/2033)\)\.

<a id="dellemc-openmanage-25"></a>
#### dellemc\.openmanage

* The <code>dellemc\_idrac\_storage\_volume</code> module is deprecated and replaced with <code>idrac\_storage\_volume</code>\.

<a id="kubernetes-core-3"></a>
#### kubernetes\.core

* k8s \- the <code>k8s</code> inventory plugin has been deprecated and will be removed in release 4\.0\.0 \([https\://github\.com/ansible\-collections/kubernetes\.core/issues/31](https\://github\.com/ansible\-collections/kubernetes\.core/issues/31)\)\.

<a id="removed-features-previously-deprecated"></a>
### Removed Features \(previously deprecated\)

* The <code>community\.azure</code> collection was considered unmaintained and has been removed from Ansible 10 \([https\://github\.com/ansible\-community/community\-topics/issues/263](https\://github\.com/ansible\-community/community\-topics/issues/263)\)\.
  Users can still install this collection with <code>ansible\-galaxy collection install community\.azure</code>\.
* The <code>gluster\.gluster</code> collection was considered unmaintained and has been removed from Ansible 10 \([https\://github\.com/ansible\-community/community\-topics/issues/225](https\://github\.com/ansible\-community/community\-topics/issues/225)\)\.
  Users can still install this collection with <code>ansible\-galaxy collection install gluster\.gluster</code>\.
* The <code>hpe\.nimble</code> collection was considered unmaintained and has been removed from Ansible 10 \([https\://github\.com/ansible\-community/community\-topics/issues/254](https\://github\.com/ansible\-community/community\-topics/issues/254)\)\.
  Users can still install this collection with <code>ansible\-galaxy collection install hpe\.nimble</code>\.
* The <code>netapp\.aws</code> collection was considered unmaintained and has been removed from Ansible 10 \([https\://github\.com/ansible\-community/community\-topics/issues/223](https\://github\.com/ansible\-community/community\-topics/issues/223)\)\.
  Users can still install this collection with <code>ansible\-galaxy collection install netapp\.aws</code>\.
* The <code>netapp\.azure</code> collection was considered unmaintained and has been removed from Ansible 10 \([https\://github\.com/ansible\-community/community\-topics/issues/234](https\://github\.com/ansible\-community/community\-topics/issues/234)\)\.
  Users can still install this collection with <code>ansible\-galaxy collection install netapp\.azure</code>\.
* The <code>netapp\.elementsw</code> collection was considered unmaintained and has been removed from Ansible 10 \([https\://github\.com/ansible\-community/community\-topics/issues/235](https\://github\.com/ansible\-community/community\-topics/issues/235)\)\.
  Users can still install this collection with <code>ansible\-galaxy collection install netapp\.elementsw</code>\.
* The <code>netapp\.um\_info</code> collection was considered unmaintained and has been removed from Ansible 10 \([https\://github\.com/ansible\-community/community\-topics/issues/244](https\://github\.com/ansible\-community/community\-topics/issues/244)\)\.
  Users can still install this collection with <code>ansible\-galaxy collection install netapp\.um\_info</code>\.
* The collection <code>community\.sap</code> has been completely removed from Ansible\.
  It has been renamed to <code>community\.sap\_libs</code>\.
  The collection will be completely removed from Ansible eventually\.
  Please update your FQCNs from <code>community\.sap</code> to <code>community\.sap\_libs</code>\.
* The deprecated <code>purestorage\.fusion</code> collection has been removed \([https\://forum\.ansible\.com/t/3712](https\://forum\.ansible\.com/t/3712)\)\.

<a id="ansible-core-26"></a>
#### Ansible\-core

* Remove deprecated APIs from ansible\-docs \([https\://github\.com/ansible/ansible/issues/81716](https\://github\.com/ansible/ansible/issues/81716)\)\.
* Remove deprecated JINJA2\_NATIVE\_WARNING environment variable \([https\://github\.com/ansible/ansible/issues/81714](https\://github\.com/ansible/ansible/issues/81714)\)
* Remove deprecated <code>scp\_if\_ssh</code> from ssh connection plugin \([https\://github\.com/ansible/ansible/issues/81715](https\://github\.com/ansible/ansible/issues/81715)\)\.
* Remove deprecated crypt support from ansible\.utils\.encrypt \([https\://github\.com/ansible/ansible/issues/81717](https\://github\.com/ansible/ansible/issues/81717)\)
* Removed Python 2\.7 and Python 3\.6 as a supported remote version\. Python 3\.7\+ is now required for target execution\.
* With the removal of Python 2 support\, the yum module and yum action plugin are removed and redirected to <code>dnf</code>\.

<a id="amazon-aws-8"></a>
#### amazon\.aws

* iam\_role \- the <code>iam\_role\.assume\_role\_policy\_document\_raw</code> return value has been deprecated\.  <code>iam\_role\.assume\_role\_policy\_document</code> now returns the same format as <code>iam\_role\.assume\_role\_policy\_document\_raw</code> \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2040](https\://github\.com/ansible\-collections/amazon\.aws/pull/2040)\)\.
* iam\_role\_info \- the <code>iam\_role\.assume\_role\_policy\_document\_raw</code> return value has been deprecated\.  <code>iam\_role\.assume\_role\_policy\_document</code> now returns the same format as <code>iam\_role\.assume\_role\_policy\_document\_raw</code> \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2040](https\://github\.com/ansible\-collections/amazon\.aws/pull/2040)\)\.
* module\_utils\.policy \- the previously deprecated <code>sort\_json\_policy\_dict\(\)</code> function has been removed\, consider using <code>compare\_policies\(\)</code> instead \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2052](https\://github\.com/ansible\-collections/amazon\.aws/pull/2052)\)\.

<a id="arista-eos-2"></a>
#### arista\.eos

* Remove depreacted eos\_bgp module which is replaced with eos\_bgp\_global and eos\_bgp\_address\_family\.
* Remove deprecated eos\_logging module which is replaced with eos\_logging\_global resource module\.
* Remove deprecated timers\.throttle attribute\.

<a id="cisco-ios-2"></a>
#### cisco\.ios

* Deprecated ios\_ntp module in favor of ios\_ntp\_global\.
* Removed previously deprecated ios\_bgp module in favor of ios\_bgp\_global and ios\_bgp\_address\_family\.

<a id="cisco-iosxr-2"></a>
#### cisco\.iosxr

* Remove deprecated iosxr\_logging module which is replaced with iosxr\_logging\_global resource module\.

<a id="cisco-nxos-4"></a>
#### cisco\.nxos

* The nxos\_logging module has been removed with this release\.
* The nxos\_ntp module has been removed with this release\.
* The nxos\_ntp\_auth module has been removed with this release\.
* The nxos\_ntp\_options module has been removed with this release\.

<a id="community-dns-12"></a>
#### community\.dns

* The collection no longer supports Ansible\, ansible\-base\, and ansible\-core releases that are currently End of Life at the time of the 3\.0\.0 release\. This means that Ansible 2\.9\, ansible\-base 2\.10\, ansible\-core 2\.11\, ansible\-core 2\.12\, and ansible\-core 2\.13 are no longer supported\. The collection might still work with these versions\, but it can stop working at any moment without advance notice\, and this will not be considered a bug \([https\://github\.com/ansible\-collections/community\.dns/pull/196](https\://github\.com/ansible\-collections/community\.dns/pull/196)\)\.
* hetzner\_dns\_record\_set\, hetzner\_dns\_record \- the deprecated alias <code>name</code> of the prefix option was removed \([https\://github\.com/ansible\-collections/community\.dns/pull/196](https\://github\.com/ansible\-collections/community\.dns/pull/196)\)\.
* hosttech\_dns\_records \- the redirect to the <code>hosttech\_dns\_record\_sets</code> module has been removed \([https\://github\.com/ansible\-collections/community\.dns/pull/196](https\://github\.com/ansible\-collections/community\.dns/pull/196)\)\.

<a id="community-general-25"></a>
#### community\.general

* The deprecated redirects for internal module names have been removed\. These internal redirects were extra\-long FQCNs like <code>community\.general\.packaging\.os\.apt\_rpm</code> that redirect to the short FQCN <code>community\.general\.apt\_rpm</code>\. They were originally needed to implement flatmapping\; as various tooling started to recommend users to use the long names flatmapping was removed from the collection and redirects were added for users who already followed these incorrect recommendations \([https\://github\.com/ansible\-collections/community\.general/pull/7835](https\://github\.com/ansible\-collections/community\.general/pull/7835)\)\.
* ansible\_galaxy\_install \- the <code>ack\_ansible29</code> and <code>ack\_min\_ansiblecore211</code> options have been removed\. They no longer had any effect \([https\://github\.com/ansible\-collections/community\.general/pull/8198](https\://github\.com/ansible\-collections/community\.general/pull/8198)\)\.
* cloudflare\_dns \- remove support for SPF records\. These are no longer supported by CloudFlare \([https\://github\.com/ansible\-collections/community\.general/pull/7782](https\://github\.com/ansible\-collections/community\.general/pull/7782)\)\.
* django\_manage \- support for the <code>command</code> values <code>cleanup</code>\, <code>syncdb</code>\, and <code>validate</code> were removed\. Use <code>clearsessions</code>\, <code>migrate</code>\, and <code>check</code> instead\, respectively \([https\://github\.com/ansible\-collections/community\.general/pull/8198](https\://github\.com/ansible\-collections/community\.general/pull/8198)\)\.
* flowdock \- this module relied on HTTPS APIs that do not exist anymore and was thus removed \([https\://github\.com/ansible\-collections/community\.general/pull/8198](https\://github\.com/ansible\-collections/community\.general/pull/8198)\)\.
* mh\.mixins\.deps module utils \- the <code>DependencyMixin</code> has been removed\. Use the <code>deps</code> module utils instead \([https\://github\.com/ansible\-collections/community\.general/pull/8198](https\://github\.com/ansible\-collections/community\.general/pull/8198)\)\.
* proxmox \- the <code>proxmox\_default\_behavior</code> option has been removed \([https\://github\.com/ansible\-collections/community\.general/pull/8198](https\://github\.com/ansible\-collections/community\.general/pull/8198)\)\.
* rax\* modules\, rax module utils\, rax docs fragment \- the Rackspace modules relied on the deprecated package <code>pyrax</code> and were thus removed \([https\://github\.com/ansible\-collections/community\.general/pull/8198](https\://github\.com/ansible\-collections/community\.general/pull/8198)\)\.
* redhat module utils \- the classes <code>Rhsm</code>\, <code>RhsmPool</code>\, and <code>RhsmPools</code> have been removed \([https\://github\.com/ansible\-collections/community\.general/pull/8198](https\://github\.com/ansible\-collections/community\.general/pull/8198)\)\.
* redhat\_subscription \- the alias <code>autosubscribe</code> of the <code>auto\_attach</code> option was removed \([https\://github\.com/ansible\-collections/community\.general/pull/8198](https\://github\.com/ansible\-collections/community\.general/pull/8198)\)\.
* stackdriver \- this module relied on HTTPS APIs that do not exist anymore and was thus removed \([https\://github\.com/ansible\-collections/community\.general/pull/8198](https\://github\.com/ansible\-collections/community\.general/pull/8198)\)\.
* webfaction\_\* modules \- these modules relied on HTTPS APIs that do not exist anymore and were thus removed \([https\://github\.com/ansible\-collections/community\.general/pull/8198](https\://github\.com/ansible\-collections/community\.general/pull/8198)\)\.

<a id="community-grafana-1"></a>
#### community\.grafana

* removed deprecated <em class="title-reference">message</em> argument in <em class="title-reference">grafana\_dashboard</em>

<a id="community-hrobot-5"></a>
#### community\.hrobot

* The collection no longer supports Ansible\, ansible\-base\, and ansible\-core releases that are currently End of Life at the time of the 2\.0\.0 release\. This means that Ansible 2\.9\, ansible\-base 2\.10\, ansible\-core 2\.11\, ansible\-core 2\.12\, and ansible\-core 2\.13 are no longer supported\. The collection might still work with these versions\, but it can stop working at any moment without advance notice\, and this will not be considered a bug \([https\://github\.com/ansible\-collections/community\.hrobot/pull/101](https\://github\.com/ansible\-collections/community\.hrobot/pull/101)\)\.

<a id="junipernetworks-junos-2"></a>
#### junipernetworks\.junos

* Remove deprected junos\_logging module which is replaced by junos\_logging\_global resource module\.

<a id="security-fixes-2"></a>
### Security Fixes

<a id="ansible-core-27"></a>
#### Ansible\-core

* ANSIBLE\_NO\_LOG \- Address issue where ANSIBLE\_NO\_LOG was ignored \(CVE\-2024\-0690\)
* ansible\-galaxy \- Prevent roles from using symlinks to overwrite files outside of the installation directory \(CVE\-2023\-5115\)
* templating \- Address issues where internal templating can cause unsafe variables to lose their unsafe designation \(CVE\-2023\-5764\)

<a id="community-dns-13"></a>
#### community\.dns

* hosttech\_dns\_records and hetzner\_dns\_records inventory plugins \- make sure all data received from the remote servers is marked as unsafe\, so remote code execution by obtaining texts that can be evaluated as templates is not possible \([https\://www\.die\-welt\.net/2024/03/remote\-code\-execution\-in\-ansible\-dynamic\-inventory\-plugins/](https\://www\.die\-welt\.net/2024/03/remote\-code\-execution\-in\-ansible\-dynamic\-inventory\-plugins/)\, [https\://github\.com/ansible\-collections/community\.dns/pull/189](https\://github\.com/ansible\-collections/community\.dns/pull/189)\)\.

<a id="community-docker-14"></a>
#### community\.docker

* docker\_containers\, docker\_machine\, and docker\_swarm inventory plugins \- make sure all data received from the Docker daemon / Docker machine is marked as unsafe\, so remote code execution by obtaining texts that can be evaluated as templates is not possible \([https\://www\.die\-welt\.net/2024/03/remote\-code\-execution\-in\-ansible\-dynamic\-inventory\-plugins/](https\://www\.die\-welt\.net/2024/03/remote\-code\-execution\-in\-ansible\-dynamic\-inventory\-plugins/)\, [https\://github\.com/ansible\-collections/community\.docker/pull/815](https\://github\.com/ansible\-collections/community\.docker/pull/815)\)\.

<a id="community-general-26"></a>
#### community\.general

* cobbler\, gitlab\_runners\, icinga2\, linode\, lxd\, nmap\, online\, opennebula\, proxmox\, scaleway\, stackpath\_compute\, virtualbox\, and xen\_orchestra inventory plugin \- make sure all data received from the remote servers is marked as unsafe\, so remote code execution by obtaining texts that can be evaluated as templates is not possible \([https\://www\.die\-welt\.net/2024/03/remote\-code\-execution\-in\-ansible\-dynamic\-inventory\-plugins/](https\://www\.die\-welt\.net/2024/03/remote\-code\-execution\-in\-ansible\-dynamic\-inventory\-plugins/)\, [https\://github\.com/ansible\-collections/community\.general/pull/8098](https\://github\.com/ansible\-collections/community\.general/pull/8098)\)\.
* keycloak\_identity\_provider \- the client secret was not correctly sanitized by the module\. The return values <code>proposed</code>\, <code>existing</code>\, and <code>end\_state</code>\, as well as the diff\, did contain the client secret unmasked \([https\://github\.com/ansible\-collections/community\.general/pull/8355](https\://github\.com/ansible\-collections/community\.general/pull/8355)\)\.

<a id="community-hrobot-6"></a>
#### community\.hrobot

* robot inventory plugin \- make sure all data received from the Hetzner robot service server is marked as unsafe\, so remote code execution by obtaining texts that can be evaluated as templates is not possible \([https\://www\.die\-welt\.net/2024/03/remote\-code\-execution\-in\-ansible\-dynamic\-inventory\-plugins/](https\://www\.die\-welt\.net/2024/03/remote\-code\-execution\-in\-ansible\-dynamic\-inventory\-plugins/)\, [https\://github\.com/ansible\-collections/community\.hrobot/pull/99](https\://github\.com/ansible\-collections/community\.hrobot/pull/99)\)\.

<a id="bugfixes-8"></a>
### Bugfixes

<a id="ansible-core-28"></a>
#### Ansible\-core

* Add a version ceiling constraint for pypsrp to avoid potential breaking changes in the 1\.0\.0 release\.
* All core lookups now use set\_option\(s\) even when doing their own custom parsing\. This ensures that the options are always the proper type\.
* Allow for searching handler subdir for included task via include\_role \([https\://github\.com/ansible/ansible/issues/81722](https\://github\.com/ansible/ansible/issues/81722)\)
* AnsibleModule\.atomic\_move \- fix preserving extended ACLs of the destination when it exists \([https\://github\.com/ansible/ansible/issues/72929](https\://github\.com/ansible/ansible/issues/72929)\)\.
* Cache host\_group\_vars after instantiating it once and limit the amount of repetitive work it needs to do every time it runs\.
* Call PluginLoader\.all\(\) once for vars plugins\, and load vars plugins that run automatically or are enabled specifically by name subsequently\.
* Consolidate systemd detection logic into one place \([https\://github\.com/ansible/ansible/issues/80975](https\://github\.com/ansible/ansible/issues/80975)\)\.
* Consolidated the list of internal static vars\, centralized them as constant and completed from some missing entries\.
* Do not print undefined error message twice \([https\://github\.com/ansible/ansible/issues/78703](https\://github\.com/ansible/ansible/issues/78703)\)\.
* Enable file cache for vaulted files during vars lookup to fix a strong performance penalty in huge and complex playbboks\.
* Fix NEVRA parsing of package names that include digit\(s\) in them \([https\://github\.com/ansible/ansible/issues/76463](https\://github\.com/ansible/ansible/issues/76463)\, [https\://github\.com/ansible/ansible/issues/81018](https\://github\.com/ansible/ansible/issues/81018)\)
* Fix <code>force\_handlers</code> not working with <code>any\_errors\_fatal</code> \([https\://github\.com/ansible/ansible/issues/36308](https\://github\.com/ansible/ansible/issues/36308)\)
* Fix <code>run\_once</code> being incorrectly interpreted on handlers \([https\://github\.com/ansible/ansible/issues/81666](https\://github\.com/ansible/ansible/issues/81666)\)
* Fix an issue when setting a plugin name from an unsafe source resulted in <code>ValueError\: unmarshallable object</code> \([https\://github\.com/ansible/ansible/issues/82708](https\://github\.com/ansible/ansible/issues/82708)\)
* Fix check for missing \_sub\_plugin attribute in older connection plugins \([https\://github\.com/ansible/ansible/pull/82954](https\://github\.com/ansible/ansible/pull/82954)\)
* Fix condition for unquoting configuration strings from ini files \([https\://github\.com/ansible/ansible/issues/82387](https\://github\.com/ansible/ansible/issues/82387)\)\.
* Fix for when <code>any\_errors\_fatal</code> was ignored if error occurred in a block with always \([https\://github\.com/ansible/ansible/issues/31543](https\://github\.com/ansible/ansible/issues/31543)\)
* Fix handlers not being executed in lockstep using the linear strategy in some cases \([https\://github\.com/ansible/ansible/issues/82307](https\://github\.com/ansible/ansible/issues/82307)\)
* Fix handling missing urls in ansible\.module\_utils\.urls\.fetch\_file for Python 3\.
* Fix issue where an <code>include\_tasks</code> handler in a role was not able to locate a file in <code>tasks/</code> when <code>tasks\_from</code> was used as a role entry point and <code>main\.yml</code> was not present \([https\://github\.com/ansible/ansible/issues/82241](https\://github\.com/ansible/ansible/issues/82241)\)
* Fix issues when tasks withing nested blocks wouldn\'t run when <code>force\_handlers</code> is set \([https\://github\.com/ansible/ansible/issues/81533](https\://github\.com/ansible/ansible/issues/81533)\)
* Fix loading vars\_plugins in roles \([https\://github\.com/ansible/ansible/issues/82239](https\://github\.com/ansible/ansible/issues/82239)\)\.
* Fix notifying role handlers by listen keyword topics with the \"role\_name \: \" prefix \([https\://github\.com/ansible/ansible/issues/82849](https\://github\.com/ansible/ansible/issues/82849)\)\.
* Fix setting proper locale for git executable when running on non english systems\, ensuring git output can always be parsed\.
* Fix tasks in always section not being executed for nested blocks with <code>any\_errors\_fatal</code> \([https\://github\.com/ansible/ansible/issues/73246](https\://github\.com/ansible/ansible/issues/73246)\)
* Fixes permission for cache json file from 600 to 644 \([https\://github\.com/ansible/ansible/issues/82683](https\://github\.com/ansible/ansible/issues/82683)\)\.
* Give the tombstone error for <code>include</code> pre\-fork like other tombstoned action/module plugins\.
* Harden python templates for respawn and ansiballz around str literal quoting
* Include the task location when a module or action plugin is deprecated \([https\://github\.com/ansible/ansible/issues/82450](https\://github\.com/ansible/ansible/issues/82450)\)\.
* Interpreter discovery \- Add <code>Amzn</code> to <code>OS\_FAMILY\_MAP</code> for correct family fallback for interpreter discovery \([https\://github\.com/ansible/ansible/issues/80882](https\://github\.com/ansible/ansible/issues/80882)\)\.
* Mirror the behavior of dnf on the command line when handling NEVRAs with omitted epoch \([https\://github\.com/ansible/ansible/issues/71808](https\://github\.com/ansible/ansible/issues/71808)\)
* Plugin loader does not dedupe nor cache filter/test plugins by file basename\, but full path name\.
* Properly template tags in parent blocks \([https\://github\.com/ansible/ansible/issues/81053](https\://github\.com/ansible/ansible/issues/81053)\)
* Provide additional information about the alternative plugin in the deprecation message \([https\://github\.com/ansible/ansible/issues/80561](https\://github\.com/ansible/ansible/issues/80561)\)\.
* Remove the galaxy\_info field <code>platforms</code> from the role templates \([https\://github\.com/ansible/ansible/issues/82453](https\://github\.com/ansible/ansible/issues/82453)\)\.
* Restoring the ability of filters/tests can have same file base name but different tests/filters defined inside\.
* Reword the error message when the module fails to parse parameters in JSON format \([https\://github\.com/ansible/ansible/issues/81188](https\://github\.com/ansible/ansible/issues/81188)\)\.
* Reword warning if the reserved keyword \_ansible\_ used as a module parameter \([https\://github\.com/ansible/ansible/issues/82514](https\://github\.com/ansible/ansible/issues/82514)\)\.
* Run all handlers with the same <code>listen</code> topic\, even when notified from another handler \([https\://github\.com/ansible/ansible/issues/82363](https\://github\.com/ansible/ansible/issues/82363)\)\.
* Slight optimization to hostvars \(instantiate template only once per host\, vs per call to var\)\.
* Stopped misleadingly advertising <code>async</code> mode support in the <code>reboot</code> module \([https\://github\.com/ansible/ansible/issues/71517](https\://github\.com/ansible/ansible/issues/71517)\)\.
* <code>ansible\-galaxy role import</code> \- fix using the <code>role\_name</code> in a standalone role\'s <code>galaxy\_info</code> metadata by disabling automatic removal of the <code>ansible\-role\-</code> prefix\. This matches the behavior of the Galaxy UI which also no longer implicitly removes the <code>ansible\-role\-</code> prefix\. Use the <code>\-\-role\-name</code> option or add a <code>role\_name</code> to the <code>galaxy\_info</code> dictionary in the role\'s <code>meta/main\.yml</code> to use an alternate role name\.
* <code>ansible\-test sanity \-\-test runtime\-metadata</code> \- add <code>action\_plugin</code> as a valid field for modules in the schema \([https\://github\.com/ansible/ansible/pull/82562](https\://github\.com/ansible/ansible/pull/82562)\)\.
* <code>ansible\.module\_utils\.service</code> \- ensure binary data transmission in <code>daemonize\(\)</code>
* <code>any\_errors\_fatal</code> should fail all hosts and rescue all of them when a <code>rescue</code> section is specified \([https\://github\.com/ansible/ansible/issues/80981](https\://github\.com/ansible/ansible/issues/80981)\)
* <code>include\_role</code> \- properly execute <code>v2\_playbook\_on\_include</code> and <code>v2\_runner\_on\_failed</code> callbacks as well as increase <code>ok</code> and <code>failed</code> stats in the play recap\, when appropriate \([https\://github\.com/ansible/ansible/issues/77336](https\://github\.com/ansible/ansible/issues/77336)\)
* allow\_duplicates \- fix evaluating if the current role allows duplicates instead of using the initial value from the duplicate\'s cached role\.
* ansible\-config init will now dedupe ini entries from plugins\.
* ansible\-config will now properly template defaults before dumping them\.
* ansible\-doc \- fixed \"inicates\" typo in output
* ansible\-doc \- format top\-level descriptions with multiple paragraphs as multiple paragraphs\, instead of concatenating them \([https\://github\.com/ansible/ansible/pull/83155](https\://github\.com/ansible/ansible/pull/83155)\)\.
* ansible\-galaxy \- Deprecate use of the Galaxy v2 API \([https\://github\.com/ansible/ansible/issues/81781](https\://github\.com/ansible/ansible/issues/81781)\)
* ansible\-galaxy \- Provide a better error message when using a requirements file with an invalid format \- [https\://github\.com/ansible/ansible/issues/81901](https\://github\.com/ansible/ansible/issues/81901)
* ansible\-galaxy \- Resolve issue with the dataclass used for galaxy\.yml manifest caused by using future annotations
* ansible\-galaxy \- ensure path to ansible collection when installing or downloading doesn\'t have a backslash \([https\://github\.com/ansible/ansible/pull/79705](https\://github\.com/ansible/ansible/pull/79705)\)\.
* ansible\-galaxy \- started allowing the use of pre\-releases for collections that do not have any stable versions published\. \([https\://github\.com/ansible/ansible/pull/81606](https\://github\.com/ansible/ansible/pull/81606)\)
* ansible\-galaxy \- started allowing the use of pre\-releases for dependencies on any level of the dependency tree that specifically demand exact pre\-release versions of collections and not version ranges\. \([https\://github\.com/ansible/ansible/pull/81606](https\://github\.com/ansible/ansible/pull/81606)\)
* ansible\-galaxy error on dependency resolution will not error itself due to \'virtual\' collections not having a name/namespace\.
* ansible\-galaxy info \- fix reporting no role found when lookup\_role\_by\_name returns None\.
* ansible\-galaxy role import \- exit with 1 when the import fails \([https\://github\.com/ansible/ansible/issues/82175](https\://github\.com/ansible/ansible/issues/82175)\)\.
* ansible\-galaxy role install \- fix installing roles from Galaxy that have version <code>None</code> \([https\://github\.com/ansible/ansible/issues/81832](https\://github\.com/ansible/ansible/issues/81832)\)\.
* ansible\-galaxy role install \- fix symlinks \([https\://github\.com/ansible/ansible/issues/82702](https\://github\.com/ansible/ansible/issues/82702)\, [https\://github\.com/ansible/ansible/issues/81965](https\://github\.com/ansible/ansible/issues/81965)\)\.
* ansible\-galaxy role install \- normalize tarfile paths and symlinks using <code>ansible\.utils\.path\.unfrackpath</code> and consider them valid as long as the realpath is in the tarfile\'s role directory \([https\://github\.com/ansible/ansible/issues/81965](https\://github\.com/ansible/ansible/issues/81965)\)\.
* ansible\-inventory \- index available\_hosts for major performance boost when dumping large inventories
* ansible\-pull now will expand relative paths for the <code>\-d\|\-\-directory</code> option is now expanded before use\.
* ansible\-pull will now correctly handle become and connection password file options for ansible\-playbook\.
* ansible\-test \- Add a <code>pylint</code> plugin to work around a known issue on Python 3\.12\.
* ansible\-test \- Explicitly supply <code>ControlPath\=none</code> when setting up port forwarding over SSH to address the scenario where the local ssh configuration uses <code>ControlPath</code> for all hosts\, and would prevent ports to be forwarded after the initial connection to the host\.
* ansible\-test \- Fix parsing of cgroup entries which contain a <code>\:</code> in the path \([https\://github\.com/ansible/ansible/issues/81977](https\://github\.com/ansible/ansible/issues/81977)\)\.
* ansible\-test \- Include missing <code>pylint</code> requirements for Python 3\.10\.
* ansible\-test \- Properly detect docker host when using <code>ssh\://</code> protocol for connecting to the docker daemon\.
* ansible\-test \- The <code>libexpat</code> package is automatically upgraded during remote bootstrapping to maintain compatibility with newer Python packages\.
* ansible\-test \- The <code>validate\-modules</code> sanity test no longer attempts to process files with unrecognized extensions as Python \(resolves [https\://github\.com/ansible/ansible/issues/82604](https\://github\.com/ansible/ansible/issues/82604)\)\.
* ansible\-test \- Update <code>pylint</code> to version 3\.0\.1\.
* ansible\-test ansible\-doc sanity test \- do not remove underscores from plugin names in collections before calling <code>ansible\-doc</code> \([https\://github\.com/ansible/ansible/pull/82574](https\://github\.com/ansible/ansible/pull/82574)\)\.
* ansible\-test validate\-modules sanity test \- do not treat leading underscores for plugin names in collections as an attempted deprecation \([https\://github\.com/ansible/ansible/pull/82575](https\://github\.com/ansible/ansible/pull/82575)\)\.
* ansible\-test — Python 3\.8–3\.12 will use <code>coverage</code> v7\.3\.2\.
* ansible\.builtin\.apt \- calling clean \= true does not properly clean certain cache files such as /var/cache/apt/pkgcache\.bin and /var/cache/apt/pkgcache\.bin \([https\://github\.com/ansible/ansible/issues/82611](https\://github\.com/ansible/ansible/issues/82611)\)
* ansible\.builtin\.uri \- the module was ignoring the <code>force</code> parameter and always requesting a cached copy \(via the <code>If\-Modified\-Since</code> header\) when downloading to an existing local file\. Disable caching when <code>force</code> is <code>true</code>\, as documented \([https\://github\.com/ansible/ansible/issues/82166](https\://github\.com/ansible/ansible/issues/82166)\)\.
* ansible\_managed restored it\'s \'templatability\' by ensuring the possible injection routes are cut off earlier in the process\.
* apt \- honor install\_recommends and dpkg\_options while installing python3\-apt library \([https\://github\.com/ansible/ansible/issues/40608](https\://github\.com/ansible/ansible/issues/40608)\)\.
* apt \- install recommended packages when installing package via deb file \([https\://github\.com/ansible/ansible/issues/29726](https\://github\.com/ansible/ansible/issues/29726)\)\.
* apt\_repository \- do not modify repo files if the file is a symlink \([https\://github\.com/ansible/ansible/issues/49809](https\://github\.com/ansible/ansible/issues/49809)\)\.
* apt\_repository \- update PPA URL to point to https URL \([https\://github\.com/ansible/ansible/issues/82463](https\://github\.com/ansible/ansible/issues/82463)\)\.
* assemble \- fixed missing parameter \'content\' in \_get\_diff\_data API \([https\://github\.com/ansible/ansible/issues/82359](https\://github\.com/ansible/ansible/issues/82359)\)\.
* async \- Fix bug that stopped running async task in <code>\-\-check</code> when <code>check\_mode\: False</code> was set as a task attribute \- [https\://github\.com/ansible/ansible/issues/82811](https\://github\.com/ansible/ansible/issues/82811)
* blockinfile \- when <code>create\=true</code> is used with a filename without path\, the module crashed \([https\://github\.com/ansible/ansible/pull/81638](https\://github\.com/ansible/ansible/pull/81638)\)\.
* check if there are attributes to set before attempting to set them \([https\://github\.com/ansible/ansible/issues/76727](https\://github\.com/ansible/ansible/issues/76727)\)
* copy action now also generates temprary files as hidden \(\'\.\' prefixed\) to avoid accidental pickup by running services that glob by extension\.
* copy action now ensures that tempfiles use the same suffix as destination\, to allow for <code>validate</code> to work with utilities that check extensions\.
* deb822\_repository \- handle idempotency if the order of parameters is changed \([https\://github\.com/ansible/ansible/issues/82454](https\://github\.com/ansible/ansible/issues/82454)\)\.
* debconf \- allow user to specify a list for value when vtype is multiselect \([https\://github\.com/ansible/ansible/issues/81345](https\://github\.com/ansible/ansible/issues/81345)\)\.
* delegate\_to when set to an empty or undefined variable will now give a proper error\.
* distribution\.py \- Recognize ALP\-Dolomite as part of the SUSE OS family in Ansible\, fixing its previous misidentification \([https\://github\.com/ansible/ansible/pull/82496](https\://github\.com/ansible/ansible/pull/82496)\)\.
* distro \- bump bundled distro version from 1\.6\.0 to 1\.8\.0 \([https\://github\.com/ansible/ansible/issues/81713](https\://github\.com/ansible/ansible/issues/81713)\)\.
* dnf \- fix an issue when cached RPMs were left in the cache directory even when the keepcache setting was unset \([https\://github\.com/ansible/ansible/issues/81954](https\://github\.com/ansible/ansible/issues/81954)\)
* dnf \- fix an issue when installing a package by specifying a file it provides could result in installing a different package providing the same file than the package already installed resulting in resolution failure \([https\://github\.com/ansible/ansible/issues/82461](https\://github\.com/ansible/ansible/issues/82461)\)
* dnf \- properly set gpg check options on enabled repositories according to the <code>disable\_gpg\_check</code> option \([https\://github\.com/ansible/ansible/issues/80110](https\://github\.com/ansible/ansible/issues/80110)\)
* dnf \- properly skip unavailable packages when <code>skip\_broken</code> is enabled \([https\://github\.com/ansible/ansible/issues/80590](https\://github\.com/ansible/ansible/issues/80590)\)
* dnf \- the <code>nobest</code> option only overrides the distribution default when explicitly used\, and is used for all supported operations \([https\://github\.com/ansible/ansible/issues/82616](https\://github\.com/ansible/ansible/issues/82616)\)
* dnf5 \- replace removed API calls
* dnf5 \- respect <code>allow\_downgrade</code> when installing packages directly from rpm files
* dnf5 \- the <code>nobest</code> option only overrides the distribution default when used
* dwim functions for lookups should be better at detectging role context even in abscense of tasks/main\.
* ensure we have logger before we log when we have increased verbosity\.
* expect \- fix argument spec error using timeout\=null \([https\://github\.com/ansible/ansible/issues/80982](https\://github\.com/ansible/ansible/issues/80982)\)\.
* fact gathering on linux now handles thread count by using rounding vs dropping decimals\, it should give slightly more accurate numbers\.
* facts \- add a generic detection for VMware in product name\.
* facts \- detect VMware ESXi 8\.0 virtualization by product name VMware20\,1
* fetch \- Do not calculate the file size for Windows fetch targets to improve performance\.
* fetch \- add error message when using <code>dest</code> with a trailing slash that becomes a local directory \- [https\://github\.com/ansible/ansible/issues/82878](https\://github\.com/ansible/ansible/issues/82878)
* find \- do not fail on Permission errors \([https\://github\.com/ansible/ansible/issues/82027](https\://github\.com/ansible/ansible/issues/82027)\)\.
* first\_found lookup now always returns a full \(absolute\) and normalized path
* first\_found lookup now always takes into account k\=v options
* flush\_handlers \- properly handle a handler failure in a nested block when <code>force\_handlers</code> is set \([http\://github\.com/ansible/ansible/issues/81532](http\://github\.com/ansible/ansible/issues/81532)\)
* galaxy \- skip verification for unwanted Python compiled bytecode files \([https\://github\.com/ansible/ansible/issues/81628](https\://github\.com/ansible/ansible/issues/81628)\)\.
* handle exception raised while validating with elements\=\'int\' and value is not within choices \([https\://github\.com/ansible/ansible/issues/82776](https\://github\.com/ansible/ansible/issues/82776)\)\.
* include\_tasks \- include <em class="title-reference">ansible\_loop\_var</em> and <em class="title-reference">ansible\_index\_var</em> in a loop \([https\://github\.com/ansible/ansible/issues/82655](https\://github\.com/ansible/ansible/issues/82655)\)\.
* include\_vars \- fix calculating <code>depth</code> relative to the root and ensure all files are included \([https\://github\.com/ansible/ansible/issues/80987](https\://github\.com/ansible/ansible/issues/80987)\)\.
* interpreter\_discovery \- handle AnsibleError exception raised while interpreter discovery \([https\://github\.com/ansible/ansible/issues/78264](https\://github\.com/ansible/ansible/issues/78264)\)\.
* iptables \- add option choices \'src\,src\' and \'dst\,dst\' in match\_set\_flags \([https\://github\.com/ansible/ansible/issues/81281](https\://github\.com/ansible/ansible/issues/81281)\)\.
* iptables \- set jump to DSCP when set\_dscp\_mark or set\_dscp\_mark\_class is set \([https\://github\.com/ansible/ansible/issues/77077](https\://github\.com/ansible/ansible/issues/77077)\)\.
* known\_hosts \- Fix issue with <em class="title-reference">\@cert\-authority</em> entries in known\_hosts incorrectly being removed\.
* module no\_log will no longer affect top level booleans\, for example <code>no\_log\_module\_parameter\=\'a\'</code> will no longer hide <code>changed\=False</code> as a \'no log value\' \(matches \'a\'\)\.
* moved assemble\, raw\, copy\, fetch\, reboot\, script and wait\_for\_connection to query task instead of play\_context ensuring they get the lastest and most correct data\.
* reboot action now handles connections with \'timeout\' vs only \'connection\_timeout\' settings\.
* role params now have higher precedence than host facts again\, matching documentation\, this had unintentionally changed in 2\.15\.
* roles\, code cleanup and performance optimization of dependencies\, now cached\,  and <code>public</code> setting is now determined once\, at role instantiation\.
* roles\, the <code>static</code> property is now correctly set\, this will fix issues with <code>public</code> and <code>DEFAULT\_PRIVATE\_ROLE\_VARS</code> controls on exporting vars\.
* set\_option method for plugins to update config now properly passes through type casting and validation\.
* ssh \- add tests for the SSH connection plugin\.
* support url\-encoded credentials in URLs like [http\://x\%40\:\%40\@example\.com](http\://x\%40\:\%40\@example\.com) \([https\://github\.com/ansible/ansible/pull/82552](https\://github\.com/ansible/ansible/pull/82552)\)
* syslog \- Handle ValueError exception raised when sending Null Characters to syslog with Python 3\.12\.
* systemd\_services \- update documentation regarding required\_one\_of and required\_by parameters \([https\://github\.com/ansible/ansible/issues/82914](https\://github\.com/ansible/ansible/issues/82914)\)\.
* template \- Fix error when templating an unsafe string which corresponds to an invalid type in Python \([https\://github\.com/ansible/ansible/issues/82600](https\://github\.com/ansible/ansible/issues/82600)\)\.
* template action will also inherit the behavior from copy \(as it uses it internally\)\.
* templating \- ensure syntax errors originating from a template being compiled into Python code object result in a failure \([https\://github\.com/ansible/ansible/issues/82606](https\://github\.com/ansible/ansible/issues/82606)\)
* unarchive \- add support for 8 character permission strings for zip archives \([https\://github\.com/ansible/ansible/pull/81705](https\://github\.com/ansible/ansible/pull/81705)\)\.
* unarchive \- force unarchive if symlink target changes \([https\://github\.com/ansible/ansible/issues/30420](https\://github\.com/ansible/ansible/issues/30420)\)\.
* unarchive modules now uses zipinfo options without relying on implementation defaults\, making it more compatible with all OS/distributions\.
* unsafe data \- Address an incompatibility when iterating or getting a single index from <code>AnsibleUnsafeBytes</code>
* unsafe data \- Address an incompatibility with <code>AnsibleUnsafeText</code> and <code>AnsibleUnsafeBytes</code> when pickling with <code>protocol\=0</code>
* unsafe data \- Enable directly using <code>AnsibleUnsafeText</code> with Python <code>pathlib</code> \([https\://github\.com/ansible/ansible/issues/82414](https\://github\.com/ansible/ansible/issues/82414)\)
* uri \- update the documentation for follow\_redirects\.
* uri action plugin now skipped during check mode \(not supported\) instead of even trying to execute the module\, which already skipped\, this does not really change the result\, but returns much faster\.
* vars \- handle exception while combining VarsWithSources and dict \([https\://github\.com/ansible/ansible/issues/81659](https\://github\.com/ansible/ansible/issues/81659)\)\.
* wait\_for should not handle \'non mmapable files\' again\.
* winrm \- Better handle send input failures when communicating with hosts under load
* winrm \- Do not raise another exception during cleanup when a task is timed out \- [https\://github\.com/ansible/ansible/issues/81095](https\://github\.com/ansible/ansible/issues/81095)
* winrm \- does not hang when attempting to get process output when stdin write failed

<a id="amazon-aws-9"></a>
#### amazon\.aws

* backup\_plan \- Fix idempotency issue when using botocore \>\= 1\.31\.36 \([https\://github\.com/ansible\-collections/amazon\.aws/issues/1952](https\://github\.com/ansible\-collections/amazon\.aws/issues/1952)\)\.
* cloudwatchevent\_rule \- Fix to avoid adding quotes to JSON input for provided input\_template \([https\://github\.com/ansible\-collections/amazon\.aws/pull/1883](https\://github\.com/ansible\-collections/amazon\.aws/pull/1883)\)\.
* cloudwatchlogs\_log\_group\_info \- Implement exponential backoff when making API calls to prevent throttling exceptions \([https\://github\.com/ansible\-collections/amazon\.aws/issues/2011](https\://github\.com/ansible\-collections/amazon\.aws/issues/2011)\)\.
* ec2\_vpc\_subnet \- cleanly handle failure when subnet isn\'t created in time \([https\://github\.com/ansible\-collections/amazon\.aws/pull/1848](https\://github\.com/ansible\-collections/amazon\.aws/pull/1848)\)\.
* elb\_classic\_lb \- fixes bug where <code>proxy\_protocol</code> not being set or being set to <code>None</code> may result in unexpected behaviour or errors \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2049](https\://github\.com/ansible\-collections/amazon\.aws/pull/2049)\)\.
* iam\_managed\_policy \- fixed an issue where only partial results were returned \([https\://github\.com/ansible\-collections/amazon\.aws/pull/1936](https\://github\.com/ansible\-collections/amazon\.aws/pull/1936)\)\.
* iam\_managed\_policy \- fixes bug that causes <code>ParamValidationError</code> when attempting to delete a policy that\'s attached to a role or a user \([https\://github\.com/ansible\-collections/amazon\.aws/issues/2067](https\://github\.com/ansible\-collections/amazon\.aws/issues/2067)\)\.
* iam\_role\_info \- fixes bug in handling paths missing the <code>/</code> prefix and/or suffix \([https\://github\.com/ansible\-collections/amazon\.aws/issues/2065](https\://github\.com/ansible\-collections/amazon\.aws/issues/2065)\)\.
* lambda\_event \- Fix when <code>batch\_size</code> is greater than 10\, by enabling support for setting <code>maximum\_batching\_window\_in\_seconds</code> \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2025](https\://github\.com/ansible\-collections/amazon\.aws/pull/2025)\)\.
* lambda\_event \- Retrieve function ARN using AWS API \(get\_function\) instead of building it with AWS account information \([https\://github\.com/ansible\-collections/amazon\.aws/issues/1859](https\://github\.com/ansible\-collections/amazon\.aws/issues/1859)\)\.
* lookup/secretsmanager\_secret \- fix the issue when the nested secret is missing and on\_missing is set to warn\, the lookup was raising an error instead of a warning message \([https\://github\.com/ansible\-collections/amazon\.aws/issues/1781](https\://github\.com/ansible\-collections/amazon\.aws/issues/1781)\)\.
* module\_utils/elbv2 \- Fix issue when creating or modifying Load balancer rule type authenticate\-oidc using <code>ClientSecret</code> parameter and <code>UseExistingClientSecret\=true</code> \([https\://github\.com/ansible\-collections/amazon\.aws/issues/1877](https\://github\.com/ansible\-collections/amazon\.aws/issues/1877)\)\.
* plugin\_utils\.inventory \- Ensure templated options in lookup plugins are converted \([https\://github\.com/ansible\-collections/amazon\.aws/issues/1955](https\://github\.com/ansible\-collections/amazon\.aws/issues/1955)\)\.
* plugins/inventory/aws\_ec2 \- Fix failure when retrieving information for more than 40 instances with use\_ssm\_inventory \([https\://github\.com/ansible\-collections/amazon\.aws/issues/1713](https\://github\.com/ansible\-collections/amazon\.aws/issues/1713)\)\.
* s3\_object \- Fix the issue when copying an object with overriding metadata\. \([https\://github\.com/ansible\-collections/amazon\.aws/issues/1991](https\://github\.com/ansible\-collections/amazon\.aws/issues/1991)\)\.
* s3\_object \- Fix typo that caused false deprecation warning when setting <code>overwrite\=latest</code> \([https\://github\.com/ansible\-collections/amazon\.aws/pull/1847](https\://github\.com/ansible\-collections/amazon\.aws/pull/1847)\)\.
* s3\_object \- fix idempotency issue when copying object uploaded using multipart upload \([https\://github\.com/ansible\-collections/amazon\.aws/issues/2016](https\://github\.com/ansible\-collections/amazon\.aws/issues/2016)\)\.
* s3\_object \- when doing a put and specifying <code>Content\-Type</code> in metadata\, this module \(since 6\.0\.0\) erroneously set the <code>Content\-Type</code> to <code>None</code> causing the put to fail\. Fix now correctly honours the specified <code>Content\-Type</code> \([https\://github\.com/ansible\-collections/amazon\.aws/issues/1881](https\://github\.com/ansible\-collections/amazon\.aws/issues/1881)\)\.

<a id="ansible-netcommon-3"></a>
#### ansible\.netcommon

* Added guidance for users to open an issue for the respective platform if plugin support is needed\.
* Improved module execution to gracefully handle cases where plugin support is required\, providing a clear error message to the user\.
* libssh connection plugin \- stop using deprecated <code>PlayContext\.verbosity</code> property that is no longer present in ansible\-core 2\.18 \([https\://github\.com/ansible\-collections/ansible\.netcommon/pull/626](https\://github\.com/ansible\-collections/ansible\.netcommon/pull/626)\)\.
* network\_cli \- removed deprecated play\_context\.verbosity property\.

<a id="ansible-utils-2"></a>
#### ansible\.utils

* Avoid unnecessary use of persistent connection in <em class="title-reference">cli\_parse</em>\, <em class="title-reference">fact\_diff</em>\, <em class="title-reference">update\_fact</em> and <em class="title-reference">validate</em> as this action does not require a connection\.

<a id="ansible-windows-5"></a>
#### ansible\.windows

* Process\.cs \- Fix up the <code>ProcessCreationFlags\.CreateProtectedProcess</code> typo in the enum name
* setup \- Fix up typo <code>collection \-\> collect</code> when a timeout occurred during a fact subset
* win\_acl \- Fix broken path in case of volume junction
* win\_get\_url \- Fix Tls1\.3 getting removed from the list of security protocols
* win\_powershell \- Remove unecessary using in code causing stray error records in output \- [https\://github\.com/ansible\-collections/ansible\.windows/issues/571](https\://github\.com/ansible\-collections/ansible\.windows/issues/571)
* win\_service\_info \- Warn and not fail if ERROR\_FILE\_NOT\_FOUND when trying to query a service \- [https\://github\.com/ansible\-collections/ansible\.windows/issues/556](https\://github\.com/ansible\-collections/ansible\.windows/issues/556)
* win\_updates \- Fix up typo for Download progress event messages \- [https\://github\.com/ansible\-collections/ansible\.windows/issues/554](https\://github\.com/ansible\-collections/ansible\.windows/issues/554)

<a id="arista-eos-3"></a>
#### arista\.eos

* This fix is needed because static\_routes and vlans are not returning anything when resources are not configured\.
* This got noticed in this issue \([https\://github\.com/network\-automation/toolkit/issues/47](https\://github\.com/network\-automation/toolkit/issues/47)\)
* correct a missing whitespace and add \'auth\' string\.
* correct the parsing of the elements in \'name\_servers\' in \'eos\_system\' module\.
* correct the reference of string attribute \'reference\_bandwith\'\.
* when static\_routes and vlans are not confirgured then return empty list\.

<a id="check-point-mgmt-1"></a>
#### check\_point\.mgmt

* httpapi/checkpoint\.py \- Raise a fatal error if login wasn\'t successful\.

<a id="cisco-aci-3"></a>
#### cisco\.aci

* Fix auto logout issue in aci connection plugin to keep connection active between tasks
* Fix idempotency for l3out configuration when l3protocol is used in aci\_l3out
* Fix issues with new attributes in aci\_interface\_policy\_leaf\_policy\_group module by adding conditions to include attributes in the payload only when they are specified by the user \(\#578\)
* Fix query in aci\_vmm\_controller

<a id="cisco-asa-1"></a>
#### cisco\.asa

* Prevents module\_defaults from were being incorrectly applied to the platform action\, instead of the concerned module\.

<a id="cisco-ios-3"></a>
#### cisco\.ios

* Prevents module\_defaults from were being incorrectly applied to the platform action\, instead of the concerned module\.
* Updated the ios\_ping ping module to support size param\.
* ios\_acls \- Adds back existing remarks for an ace entry when updated with replaced or overridden state\, as all remarks for a specific sequence gets removed when ace entry is updated\.
* ios\_acls \- Fix replaced state to consider remarks and ace entries while comparing configuration\.
* ios\_acls \- correctly match the different line for ACL without sequence number
* ios\_acls \- make sequence optional for rendering of standard acls\.
* ios\_acls \- take correctly in case where we want to push an ACL from a different type
* ios\_acls \- update module to apply remarks entry with sequence numbers\.
* ios\_bgp\_address\_family \- description attribute\, evalutated as complex object casted to string\.
* ios\_bgp\_global \- Explicitly add neighbor address to every parser\.
* ios\_bgp\_global \- Shutdown attributes generates negate command on set as false\.
* ios\_bgp\_global \- description attribute\, evalutated as complex object casted to string\.
* ios\_bgp\_global \- fix template attribute to generate configuration commands\.
* ios\_bgp\_global \- remote\_as not mendatory for neighbors\.
* ios\_interfaces \- description attribute\, evalutated as complex object casted to string\.
* ios\_l3\_interfaces \- remove validation from ipv6 address parameter\.
* ios\_ospfv2 \- Fix improper rendering of admin\_distance attribute\.
* ios\_prefix\_lists \- description attribute\, evalutated as complex object casted to string\.
* ios\_route\_maps \- description attribute\, evalutated as complex object casted to string\.
* ios\_snmp\_server \- fix group and user IPv6 ACL commands\.
* ios\_snmp\_server \- fixed config issue with snmp user password update being idempotent on consecutive runs\.
* ios\_user \- Fix configuration of hashed passwords and secrets\.
* ios\_user \- fix configuration of user with hashed password\.
* ios\_user \- fixed configuration removal of ssh users using purge\.
* ios\_vlans \- Make behaviour of the action states consistent\.
* ios\_vlans \- Top level configuration attribute is not required\, the module works with vlan and vlan configuration both\.
* ios\_vlans \- fixes behaviour of shutdown attribute with action states\.
* ios\_vrf \- Update and add missing argspec keys that define the attributes\.
* ios\_vrf \- added MDT related keys

<a id="cisco-iosxr-3"></a>
#### cisco\.iosxr

* Fix \'afi\' value in bgp\_templates RM to valid values\.
* Fix issue in gathered state of interfaces and l3\_interfaces RMs\([https\://github\.com/ansible\-collections/cisco\.iosxr/issues/452](https\://github\.com/ansible\-collections/cisco\.iosxr/issues/452)\, [https\://github\.com/ansible\-collections/cisco\.iosxr/issues/451](https\://github\.com/ansible\-collections/cisco\.iosxr/issues/451)\)

<a id="cisco-ise-5"></a>
#### cisco\.ise

* Added missing import re in endpoint module
* Service included active\_directories\.
* Service included ad\_groups\.
* Service included custom\_attributes\.
* Service included duo\_identity\_sync\.
* Service included duo\_mfa\.
* Service included enable\_mfa\.
* Service included endpoint\_stop\_replication\_service\.
* Service included endpoints\.
* Service included full\_upgrade\.
* Service included is\_mfa\_enabled\.
* Service included native\_ipsec\.
* Service included px\_grid\_direct\.
* Service included sgt\_range\_reservation\.
* Service included user\_equipment\.
* Updated to use ciscoisesdk v2\.1\.1 or newer fixing ciscoisesdk problem\.
* ansible\.utils changes to <em class="title-reference">\"\>\=2\.0\.0\,\<5\.0\"</em> in galaxy\.yml dependencies\.
* network\_device\_group \- change parameter name from ndgtype to othername\.
* network\_device\_group\_info \- change parameter name from ndgtype to othername\.

<a id="cisco-meraki-3"></a>
#### cisco\.meraki

* Adding <em class="title-reference">network\_clients\_info</em> and <em class="title-reference">network\_client\_info</em>\.
* Adding <em class="title-reference">platform\_meraki\.rst</em> to docs\.
* Adding <em class="title-reference">product\_types</em> for update request on networks\.
* Adding <em class="title-reference">smartquotes \= False</em> to <em class="title-reference">conf\.py</em> and romoving <em class="title-reference">\'</em> from rst files\.
* Adding build\_ignore property to galaxy file\.
* Adding support to ansible\.utils \>\=3\.0
* Idempotency bugs fixed in devices\_switch\_ports\.
* Parameter\`organization\_id\` change to <em class="title-reference">organizationId</em> organizations\_claim\.
* Parameter\`organization\_id\` change to <em class="title-reference">organizationId</em> organizations\_clone\.
* Parameter\`organization\_id\` change to <em class="title-reference">organizationId</em> organizations\_inventory\_claim\.
* Parameter\`organization\_id\` change to <em class="title-reference">organizationId</em> organizations\_inventory\_onboarding\_cloud\_monitoring\_export\_events\.
* Parameter\`organization\_id\` change to <em class="title-reference">organizationId</em> organizations\_inventory\_onboarding\_cloud\_monitoring\_prepare\.
* Parameter\`organization\_id\` change to <em class="title-reference">organizationId</em> organizations\_inventory\_release\.
* Parameter\`organization\_id\` change to <em class="title-reference">organizationId</em> organizations\_licenses\_assign\_seats\.
* Parameter\`organization\_id\` change to <em class="title-reference">organizationId</em> organizations\_licenses\_move\.
* Parameter\`organization\_id\` change to <em class="title-reference">organizationId</em> organizations\_licenses\_move\_seats\.
* Parameter\`organization\_id\` change to <em class="title-reference">organizationId</em> organizations\_licenses\_renew\_seats\.
* Parameter\`organization\_id\` change to <em class="title-reference">organizationId</em> organizations\_licensing\_coterm\_licenses\_move\.
* Parameter\`organization\_id\` change to <em class="title-reference">organizationId</em> organizations\_networks\_combine\.
* Parameter\`organization\_id\` change to <em class="title-reference">organizationId</em> organizations\_switch\_devices\_clone\.
* Parameter\`organization\_id\` change to <em class="title-reference">organizationId</em> organizations\_users\.
* Removing logs in meraki\.py\.
* networks\_syslog\_servers is now just an Update action to API\.

<a id="cisco-mso-5"></a>
#### cisco\.mso

* Fix TypeError for iteration on NoneType in mso\_schema\_template
* Fixed the useg\_subnet logic in mso\_schema\_template\_anp\_epg\_useg\_attribute

<a id="cisco-nxos-5"></a>
#### cisco\.nxos

* Prevents module\_defaults from were being incorrectly applied to the platform action\, instead of the concerned module\.
* nxos\_acls \- Fix parsing of ace entries with range in it\. \([https\://github\.com/ansible\-collections/cisco\.nxos/issues/788](https\://github\.com/ansible\-collections/cisco\.nxos/issues/788)\)
* nxos\_facts \- correct parse JSON output when multiple interfaces have IPv6 address assigned \([https\://github\.com/ansible\-collections/cisco\.nxos/issues/771](https\://github\.com/ansible\-collections/cisco\.nxos/issues/771)\)\.
* nxos\_file\_copy \- correctly set file\_pull\_timeout/persistent\_command\_timeout value\.
* nxos\_interfaces \- Correctly enable L3 interfaces on supported N3K platforms \([https\://github\.com/ansible\-collections/cisco\.nxos/issues/749](https\://github\.com/ansible\-collections/cisco\.nxos/issues/749)\)\.

<a id="community-aws-3"></a>
#### community\.aws

* aws\_ssm \- disable <code>enable\-bracketed\-paste</code> to fix issue with amazon linux 2023 and other OSes \([https\://github\.com/ansible\-collections/community\.aws/issues/1756](https\://github\.com/ansible\-collections/community\.aws/issues/1756)\)
* mq\_broker \- ensure broker is created with <code>tags</code> when passed \([https\://github\.com/ansible\-collections/community\.aws/issues/1832](https\://github\.com/ansible\-collections/community\.aws/issues/1832)\)\.
* opensearch \- Don\'t try to read a non existing key from the domain config \([https\://github\.com/ansible\-collections/community\.aws/pull/1910](https\://github\.com/ansible\-collections/community\.aws/pull/1910)\)\.
* ssm\(connection\) \- fix bucket region logic when region is <code>us\-east\-1</code> \([https\://github\.com/ansible\-collections/community\.aws/pull/1908](https\://github\.com/ansible\-collections/community\.aws/pull/1908)\)\.

<a id="community-ciscosmb-2"></a>
#### community\.ciscosmb

* issue
* solved issue
* typo in changelog fragment template
* typo in test script

<a id="community-crypto-7"></a>
#### community\.crypto

* acme\_\* modules \- also retry requests in case of socket errors\, bad status lines\, and unknown connection errors\; improve error messages in these cases \([https\://github\.com/ansible\-collections/community\.crypto/issues/680](https\://github\.com/ansible\-collections/community\.crypto/issues/680)\)\.
* acme\_\* modules \- directly react on bad return data for account creation/retrieval/updating requests \([https\://github\.com/ansible\-collections/community\.crypto/pull/682](https\://github\.com/ansible\-collections/community\.crypto/pull/682)\)\.
* acme\_\* modules \- fix improved error reporting in case of socket errors\, bad status lines\, and unknown connection errors \([https\://github\.com/ansible\-collections/community\.crypto/pull/684](https\://github\.com/ansible\-collections/community\.crypto/pull/684)\)\.
* acme\_\* modules \- increase number of retries from 5 to 10 to increase stability with unstable ACME endpoints \([https\://github\.com/ansible\-collections/community\.crypto/pull/685](https\://github\.com/ansible\-collections/community\.crypto/pull/685)\)\.
* acme\_\* modules \- make account registration handling more flexible to accept 404 instead of 400 send by DigiCert\'s ACME endpoint when an account does not exist \([https\://github\.com/ansible\-collections/community\.crypto/pull/681](https\://github\.com/ansible\-collections/community\.crypto/pull/681)\)\.
* acme\_certificate \- respect the order of the CNAME and SAN identifiers that are passed on when creating an ACME order \([https\://github\.com/ansible\-collections/community\.crypto/issues/723](https\://github\.com/ansible\-collections/community\.crypto/issues/723)\, [https\://github\.com/ansible\-collections/community\.crypto/pull/725](https\://github\.com/ansible\-collections/community\.crypto/pull/725)\)\.
* crypto\.math module utils \- change return values for <code>quick\_is\_not\_prime\(\)</code> and <code>convert\_int\_to\_bytes\(0\, 0\)</code> for special cases that do not appear when using the collection \([https\://github\.com/ansible\-collections/community\.crypto/pull/733](https\://github\.com/ansible\-collections/community\.crypto/pull/733)\)\.
* ecs\_certificate \- fixed <code>csr</code> option to be empty and allow renewal of a specific certificate according to the Renewal Information specification \([https\://github\.com/ansible\-collections/community\.crypto/pull/740](https\://github\.com/ansible\-collections/community\.crypto/pull/740)\)\.
* luks\_device \- fixed module a bug that prevented using <code>remove\_keyslot</code> with the value <code>0</code> \([https\://github\.com/ansible\-collections/community\.crypto/pull/710](https\://github\.com/ansible\-collections/community\.crypto/pull/710)\)\.
* luks\_device \- fixed module falsely outputting <code>changed\=false</code> when trying to add a new slot with a key that is already present in another slot\. The module now rejects adding keys that are already present in another slot \([https\://github\.com/ansible\-collections/community\.crypto/pull/710](https\://github\.com/ansible\-collections/community\.crypto/pull/710)\)\.
* luks\_device \- fixed testing of LUKS passphrases in when specifying a keyslot for cryptsetup version 2\.0\.3\. The output of this cryptsetup version slightly differs from later versions \([https\://github\.com/ansible\-collections/community\.crypto/pull/710](https\://github\.com/ansible\-collections/community\.crypto/pull/710)\)\.
* openssl\_dhparam \- was using an internal function instead of the public API to load DH param files when using the <code>cryptography</code> backend\. The internal function was removed in cryptography 42\.0\.0\. The module now uses the public API\, which has been available since support for DH params was added to cryptography \([https\://github\.com/ansible\-collections/community\.crypto/pull/698](https\://github\.com/ansible\-collections/community\.crypto/pull/698)\)\.
* openssl\_privatekey\_info \- <code>check\_consistency\=true</code> no longer works for RSA keys with cryptography 42\.0\.0\+ \([https\://github\.com/ansible\-collections/community\.crypto/pull/701](https\://github\.com/ansible\-collections/community\.crypto/pull/701)\)\.
* openssl\_privatekey\_info \- <code>check\_consistency\=true</code> now reports a warning if it cannot determine consistency \([https\://github\.com/ansible\-collections/community\.crypto/pull/705](https\://github\.com/ansible\-collections/community\.crypto/pull/705)\)\.
* x509\_certificate \- since community\.crypto 2\.19\.0 the module was no longer idempotent with respect to <code>not\_before</code> and <code>not\_after</code> times\. This is now fixed \([https\://github\.com/ansible\-collections/community\.crypto/issues/753](https\://github\.com/ansible\-collections/community\.crypto/issues/753)\, [https\://github\.com/ansible\-collections/community\.crypto/pull/754](https\://github\.com/ansible\-collections/community\.crypto/pull/754)\)\.
* x509\_crl\, x509\_certificate\, x509\_certificate\_info \- when parsing absolute timestamps which omitted the second count\, the first digit of the minutes was used as a one\-digit minutes count\, and the second digit of the minutes as a one\-digit second count \([https\://github\.com/ansible\-collections/community\.crypto/pull/745](https\://github\.com/ansible\-collections/community\.crypto/pull/745)\)\.

<a id="community-digitalocean-1"></a>
#### community\.digitalocean

* The C\(project\_name\) parameter for many modules was used by alias C\(project\) internally in the codebase\, but to work properly C\(project\_name\) must be used in the code\. Replace self\.module\.params\.get\(\"project\"\) with self\.module\.params\.get\(\"project\_name\"\) \([https\://github\.com/ansible\-collections/community\.digitalocean/issues/326](https\://github\.com/ansible\-collections/community\.digitalocean/issues/326)\)\.
* digital\_ocean\_kubernetes \- module didn\'t return kubeconfig properly\, return documentation was invalid\. Fixed version returns data with the same structure all the time\, also it is aligned with M\(community\.digitalocean\.digital\_ocean\_kubernetes\_info\) documentation return data now\. \([https\://github\.com/ansible\-collections/community\.digitalocean/issues/322](https\://github\.com/ansible\-collections/community\.digitalocean/issues/322)\)\.
* inventory plugin \- restore reading auth token from env variables \([https\://github\.com/ansible\-collections/community\.digitalocean/pull/315](https\://github\.com/ansible\-collections/community\.digitalocean/pull/315)\)\.

<a id="community-dns-14"></a>
#### community\.dns

* DNS record modules\, inventory plugins \- fix the TXT entry encoder to avoid splitting up escape sequences for quotes and backslashes over multiple TXT strings \([https\://github\.com/ansible\-collections/community\.dns/issues/190](https\://github\.com/ansible\-collections/community\.dns/issues/190)\, [https\://github\.com/ansible\-collections/community\.dns/pull/191](https\://github\.com/ansible\-collections/community\.dns/pull/191)\)\.
* Update Public Suffix List\.
* inventory plugins \- add unsafe wrapper to avoid marking strings that do not contain <code>\{</code> or <code>\}</code> as unsafe\, to work around a bug in AWX \([https\://github\.com/ansible\-collections/community\.dns/pull/197](https\://github\.com/ansible\-collections/community\.dns/pull/197)\)\.
* nameserver\_record\_info \- fix crash when more than one record is retrieved \([https\://github\.com/ansible\-collections/community\.dns/pull/172](https\://github\.com/ansible\-collections/community\.dns/pull/172)\)\.
* wait\_for\_txt\, nameserver\_info\, nameserver\_record\_info \- when looking up nameservers for a domain\, do not treat <code>NXDOMAIN</code> as a fatal error \([https\://github\.com/ansible\-collections/community\.dns/pull/177](https\://github\.com/ansible\-collections/community\.dns/pull/177)\)\.

<a id="community-docker-15"></a>
#### community\.docker

* Use <code>unix\:///var/run/docker\.sock</code> instead of the legacy <code>unix\://var/run/docker\.sock</code> as default for <code>docker\_host</code> \([https\://github\.com/ansible\-collections/community\.docker/pull/736](https\://github\.com/ansible\-collections/community\.docker/pull/736)\)\.
* docker and nsenter connection plugins\, docker\_container\_exec module \- avoid using the deprecated <code>ansible\.module\_utils\.compat\.selectors</code> module util with Python 3 \([https\://github\.com/ansible\-collections/community\.docker/issues/870](https\://github\.com/ansible\-collections/community\.docker/issues/870)\, [https\://github\.com/ansible\-collections/community\.docker/pull/871](https\://github\.com/ansible\-collections/community\.docker/pull/871)\)\.
* docker\_compose\_v2 \- do not consider a <code>Waiting</code> event as an action/change \([https\://github\.com/ansible\-collections/community\.docker/pull/804](https\://github\.com/ansible\-collections/community\.docker/pull/804)\)\.
* docker\_compose\_v2 \- do not fail when non\-fatal errors occur\. This can happen when pulling an image fails\, but then the image can be built for another service\. Docker Compose emits an error in that case\, but <code>docker compose up</code> still completes successfully \([https\://github\.com/ansible\-collections/community\.docker/issues/807](https\://github\.com/ansible\-collections/community\.docker/issues/807)\, [https\://github\.com/ansible\-collections/community\.docker/pull/810](https\://github\.com/ansible\-collections/community\.docker/pull/810)\, [https\://github\.com/ansible\-collections/community\.docker/pull/811](https\://github\.com/ansible\-collections/community\.docker/pull/811)\)\.
* docker\_compose\_v2 \- do not treat service\-level pull events as changes to avoid incorrect <code>changed\=true</code> return value of <code>pull\=always</code> \([https\://github\.com/ansible\-collections/community\.docker/issues/802](https\://github\.com/ansible\-collections/community\.docker/issues/802)\, [https\://github\.com/ansible\-collections/community\.docker/pull/803](https\://github\.com/ansible\-collections/community\.docker/pull/803)\)\.
* docker\_compose\_v2 \- properly parse dry\-run build events from <code>stderr</code> \([https\://github\.com/ansible\-collections/community\.docker/issues/778](https\://github\.com/ansible\-collections/community\.docker/issues/778)\, [https\://github\.com/ansible\-collections/community\.docker/pull/779](https\://github\.com/ansible\-collections/community\.docker/pull/779)\)\.
* docker\_compose\_v2\* \- allow <code>project\_src</code> to be a relative path\, by converting it to an absolute path before using it \([https\://github\.com/ansible\-collections/community\.docker/issues/827](https\://github\.com/ansible\-collections/community\.docker/issues/827)\, [https\://github\.com/ansible\-collections/community\.docker/pull/828](https\://github\.com/ansible\-collections/community\.docker/pull/828)\)\.
* docker\_compose\_v2\* modules \- abort with a nice error message instead of crash when the Docker Compose CLI plugin version is <code>dev</code> \([https\://github\.com/ansible\-collections/community\.docker/issues/825](https\://github\.com/ansible\-collections/community\.docker/issues/825)\, [https\://github\.com/ansible\-collections/community\.docker/pull/826](https\://github\.com/ansible\-collections/community\.docker/pull/826)\)\.
* docker\_compose\_v2\* modules \- correctly parse <code>Warning</code> events emitted by Docker Compose \([https\://github\.com/ansible\-collections/community\.docker/issues/807](https\://github\.com/ansible\-collections/community\.docker/issues/807)\, [https\://github\.com/ansible\-collections/community\.docker/pull/811](https\://github\.com/ansible\-collections/community\.docker/pull/811)\)\.
* docker\_compose\_v2\* modules \- parse <code>logfmt</code> warnings emitted by Docker Compose \([https\://github\.com/ansible\-collections/community\.docker/issues/787](https\://github\.com/ansible\-collections/community\.docker/issues/787)\, [https\://github\.com/ansible\-collections/community\.docker/pull/811](https\://github\.com/ansible\-collections/community\.docker/pull/811)\)\.
* docker\_compose\_v2\, docker\_compose\_v2\_pull \- fix parsing of pull messages for Docker Compose 2\.20\.0 \([https\://github\.com/ansible\-collections/community\.docker/issues/785](https\://github\.com/ansible\-collections/community\.docker/issues/785)\, [https\://github\.com/ansible\-collections/community\.docker/pull/786](https\://github\.com/ansible\-collections/community\.docker/pull/786)\)\.
* docker\_compose\_v2\_pull \- fixing idempotence by checking actual pull progress events instead of service\-level pull request when <code>policy\=always</code>\. This stops the module from reporting <code>changed\=true</code> if no actual change happened when pulling\. In check mode\, it has to assume that a change happens though \([https\://github\.com/ansible\-collections/community\.docker/issues/813](https\://github\.com/ansible\-collections/community\.docker/issues/813)\, [https\://github\.com/ansible\-collections/community\.docker/pull/814](https\://github\.com/ansible\-collections/community\.docker/pull/814)\)\.
* docker\_compose\_v2\_pull \- the module was documented as part of the <code>community\.docker\.docker</code> action group\, but was not actually part of it\. That has now been fixed \([https\://github\.com/ansible\-collections/community\.docker/pull/773](https\://github\.com/ansible\-collections/community\.docker/pull/773)\)\.
* docker\_image \- fix archiving idempotency with Docker API 1\.44 or later \([https\://github\.com/ansible\-collections/community\.docker/pull/765](https\://github\.com/ansible\-collections/community\.docker/pull/765)\)\.
* inventory plugins \- add unsafe wrapper to avoid marking strings that do not contain <code>\{</code> or <code>\}</code> as unsafe\, to work around a bug in AWX \([https\://github\.com/ansible\-collections/community\.docker/pull/835](https\://github\.com/ansible\-collections/community\.docker/pull/835)\)\.
* modules and plugins using the Docker SDK for Python \- remove <code>ssl\_version</code> from the parameters passed to Docker SDK for Python 7\.0\.0\+\. Explicitly fail with a nicer error message if it was explicitly set in this case \([https\://github\.com/ansible\-collections/community\.docker/pull/715](https\://github\.com/ansible\-collections/community\.docker/pull/715)\)\.
* modules and plugins using the Docker SDK for Python \- remove <code>tls\_hostname</code> from the parameters passed to Docker SDK for Python 7\.0\.0\+\. Explicitly fail with a nicer error message if it was explicitly set in this case \([https\://github\.com/ansible\-collections/community\.docker/pull/721](https\://github\.com/ansible\-collections/community\.docker/pull/721)\)\.
* vendored Docker SDK for Python \- avoid passing on <code>ssl\_version</code> and <code>tls\_hostname</code> if they were not provided by the user\. Remove dead code\. \([https\://github\.com/ansible\-collections/community\.docker/pull/722](https\://github\.com/ansible\-collections/community\.docker/pull/722)\)\.
* vendored Docker SDK for Python \- include a fix requests 2\.32\.2\+ compatibility \([https\://github\.com/ansible\-collections/community\.docker/issues/860](https\://github\.com/ansible\-collections/community\.docker/issues/860)\, [https\://github\.com/psf/requests/issues/6707](https\://github\.com/psf/requests/issues/6707)\, [https\://github\.com/ansible\-collections/community\.docker/pull/864](https\://github\.com/ansible\-collections/community\.docker/pull/864)\)\.
* vendored Docker SDK for Python \- include a hotfix for requests 2\.32\.0 compatibility \([https\://github\.com/ansible\-collections/community\.docker/issues/860](https\://github\.com/ansible\-collections/community\.docker/issues/860)\, [https\://github\.com/docker/docker\-py/issues/3256](https\://github\.com/docker/docker\-py/issues/3256)\, [https\://github\.com/ansible\-collections/community\.docker/pull/861](https\://github\.com/ansible\-collections/community\.docker/pull/861)\)\.

<a id="community-general-27"></a>
#### community\.general

* aix\_filesystem \- fix <code>\_validate\_vg</code> not passing VG name to <code>lsvg\_cmd</code> \([https\://github\.com/ansible\-collections/community\.general/issues/8151](https\://github\.com/ansible\-collections/community\.general/issues/8151)\)\.
* aix\_filesystem \- fix issue with empty list items in crfs logic and option order \([https\://github\.com/ansible\-collections/community\.general/pull/8052](https\://github\.com/ansible\-collections/community\.general/pull/8052)\)\.
* apt\-rpm \- the module did not upgrade packages if a newer version exists\. Now the package will be reinstalled if the candidate is newer than the installed version \([https\://github\.com/ansible\-collections/community\.general/issues/7414](https\://github\.com/ansible\-collections/community\.general/issues/7414)\)\.
* apt\_rpm \- when checking whether packages were installed after running <code>apt\-get \-y install \<packages\></code>\, only the last package name was checked \([https\://github\.com/ansible\-collections/community\.general/pull/8263](https\://github\.com/ansible\-collections/community\.general/pull/8263)\)\.
* bitwarden\_secrets\_manager lookup plugin \- implements retry with exponential backoff to avoid lookup errors when Bitwardn\'s API rate limiting is encountered \([https\://github\.com/ansible\-collections/community\.general/issues/8230](https\://github\.com/ansible\-collections/community\.general/issues/8230)\, [https\://github\.com/ansible\-collections/community\.general/pull/8238](https\://github\.com/ansible\-collections/community\.general/pull/8238)\)\.
* cargo \- fix idempotency issues when using a custom installation path for packages \(using the <code>\-\-path</code> parameter\)\. The initial installation runs fine\, but subsequent runs use the <code>get\_installed\(\)</code> function which did not check the given installation location\, before running <code>cargo install</code>\. This resulted in a false <code>changed</code> state\. Also the removal of packeges using <code>state\: absent</code> failed\, as the installation check did not use the given parameter \([https\://github\.com/ansible\-collections/community\.general/pull/7970](https\://github\.com/ansible\-collections/community\.general/pull/7970)\)\.
* cloudflare\_dns \- fix Cloudflare lookup of SHFP records \([https\://github\.com/ansible\-collections/community\.general/issues/7652](https\://github\.com/ansible\-collections/community\.general/issues/7652)\)\.
* consul\_token \- fix token creation without <code>accessor\_id</code> \([https\://github\.com/ansible\-collections/community\.general/pull/8091](https\://github\.com/ansible\-collections/community\.general/pull/8091)\)\.
* cpanm \- use new <code>VarDict</code> to prevent deprecation warning \([https\://github\.com/ansible\-collections/community\.general/issues/8410](https\://github\.com/ansible\-collections/community\.general/issues/8410)\, [https\://github\.com/ansible\-collections/community\.general/pull/8411](https\://github\.com/ansible\-collections/community\.general/pull/8411)\)\.
* django module utils \- use new <code>VarDict</code> to prevent deprecation warning \([https\://github\.com/ansible\-collections/community\.general/issues/8410](https\://github\.com/ansible\-collections/community\.general/issues/8410)\, [https\://github\.com/ansible\-collections/community\.general/pull/8411](https\://github\.com/ansible\-collections/community\.general/pull/8411)\)\.
* from\_ini filter plugin \- disabling interpolation of <code>ConfigParser</code> to allow converting values with a <code>\%</code> sign \([https\://github\.com/ansible\-collections/community\.general/issues/8183](https\://github\.com/ansible\-collections/community\.general/issues/8183)\, [https\://github\.com/ansible\-collections/community\.general/pull/8185](https\://github\.com/ansible\-collections/community\.general/pull/8185)\)\.
* gconftool2\_info \- use new <code>VarDict</code> to prevent deprecation warning \([https\://github\.com/ansible\-collections/community\.general/issues/8410](https\://github\.com/ansible\-collections/community\.general/issues/8410)\, [https\://github\.com/ansible\-collections/community\.general/pull/8411](https\://github\.com/ansible\-collections/community\.general/pull/8411)\)\.
* gitlab\_group\_members \- fix gitlab constants call in <code>gitlab\_group\_members</code> module \([https\://github\.com/ansible\-collections/community\.general/issues/7467](https\://github\.com/ansible\-collections/community\.general/issues/7467)\)\.
* gitlab\_issue \- fix behavior to search GitLab issue\, using <code>search</code> keyword instead of <code>title</code> \([https\://github\.com/ansible\-collections/community\.general/issues/7846](https\://github\.com/ansible\-collections/community\.general/issues/7846)\)\.
* gitlab\_issue\, gitlab\_label\, gitlab\_milestone \- avoid crash during version comparison when the python\-gitlab Python module is not installed \([https\://github\.com/ansible\-collections/community\.general/pull/8158](https\://github\.com/ansible\-collections/community\.general/pull/8158)\)\.
* gitlab\_project\_members \- fix gitlab constants call in <code>gitlab\_project\_members</code> module \([https\://github\.com/ansible\-collections/community\.general/issues/7467](https\://github\.com/ansible\-collections/community\.general/issues/7467)\)\.
* gitlab\_protected\_branches \- fix gitlab constants call in <code>gitlab\_protected\_branches</code> module \([https\://github\.com/ansible\-collections/community\.general/issues/7467](https\://github\.com/ansible\-collections/community\.general/issues/7467)\)\.
* gitlab\_runner \- fix pagination when checking for existing runners \([https\://github\.com/ansible\-collections/community\.general/pull/7790](https\://github\.com/ansible\-collections/community\.general/pull/7790)\)\.
* gitlab\_user \- fix gitlab constants call in <code>gitlab\_user</code> module \([https\://github\.com/ansible\-collections/community\.general/issues/7467](https\://github\.com/ansible\-collections/community\.general/issues/7467)\)\.
* haproxy \- fix an issue where HAProxy could get stuck in DRAIN mode when the backend was unreachable \([https\://github\.com/ansible\-collections/community\.general/issues/8092](https\://github\.com/ansible\-collections/community\.general/issues/8092)\)\.
* homebrew \- detect already installed formulae and casks using JSON output from <code>brew info</code> \([https\://github\.com/ansible\-collections/community\.general/issues/864](https\://github\.com/ansible\-collections/community\.general/issues/864)\)\.
* homebrew \- do not fail when brew prints warnings \([https\://github\.com/ansible\-collections/community\.general/pull/8406](https\://github\.com/ansible\-collections/community\.general/pull/8406)\, [https\://github\.com/ansible\-collections/community\.general/issues/7044](https\://github\.com/ansible\-collections/community\.general/issues/7044)\)\.
* homebrew \- error returned from brew command was ignored and tried to parse empty JSON\. Fix now checks for an error and raises it to give accurate error message to users \([https\://github\.com/ansible\-collections/community\.general/issues/8047](https\://github\.com/ansible\-collections/community\.general/issues/8047)\)\.
* hponcfg \- use new <code>VarDict</code> to prevent deprecation warning \([https\://github\.com/ansible\-collections/community\.general/issues/8410](https\://github\.com/ansible\-collections/community\.general/issues/8410)\, [https\://github\.com/ansible\-collections/community\.general/pull/8411](https\://github\.com/ansible\-collections/community\.general/pull/8411)\)\.
* incus connection plugin \- treats <code>inventory\_hostname</code> as a variable instead of a literal in remote connections \([https\://github\.com/ansible\-collections/community\.general/issues/7874](https\://github\.com/ansible\-collections/community\.general/issues/7874)\)\.
* interface\_files \- also consider <code>address\_family</code> when changing <code>option\=method</code> \([https\://github\.com/ansible\-collections/community\.general/issues/7610](https\://github\.com/ansible\-collections/community\.general/issues/7610)\, [https\://github\.com/ansible\-collections/community\.general/pull/7612](https\://github\.com/ansible\-collections/community\.general/pull/7612)\)\.
* inventory plugins \- add unsafe wrapper to avoid marking strings that do not contain <code>\{</code> or <code>\}</code> as unsafe\, to work around a bug in AWX \(\([https\://github\.com/ansible\-collections/community\.general/issues/8212](https\://github\.com/ansible\-collections/community\.general/issues/8212)\, [https\://github\.com/ansible\-collections/community\.general/pull/8225](https\://github\.com/ansible\-collections/community\.general/pull/8225)\)\.
* ipa \- fix get version regex in IPA module\_utils \([https\://github\.com/ansible\-collections/community\.general/pull/8175](https\://github\.com/ansible\-collections/community\.general/pull/8175)\)\.
* ipa\_hbacrule \- the module uses a string for <code>ipaenabledflag</code> for new FreeIPA versions while the returned value is a boolean \([https\://github\.com/ansible\-collections/community\.general/pull/7880](https\://github\.com/ansible\-collections/community\.general/pull/7880)\)\.
* ipa\_otptoken \- the module expect <code>ipatokendisabled</code> as string but the <code>ipatokendisabled</code> value is returned as a boolean \([https\://github\.com/ansible\-collections/community\.general/pull/7795](https\://github\.com/ansible\-collections/community\.general/pull/7795)\)\.
* ipa\_sudorule \- the module uses a string for <code>ipaenabledflag</code> for new FreeIPA versions while the returned value is a boolean \([https\://github\.com/ansible\-collections/community\.general/pull/7880](https\://github\.com/ansible\-collections/community\.general/pull/7880)\)\.
* iptables\_state \- fix idempotency issues when restoring incomplete iptables dumps \([https\://github\.com/ansible\-collections/community\.general/issues/8029](https\://github\.com/ansible\-collections/community\.general/issues/8029)\)\.
* irc \- replace <code>ssl\.wrap\_socket</code> that was removed from Python 3\.12 with code for creating a proper SSL context \([https\://github\.com/ansible\-collections/community\.general/pull/7542](https\://github\.com/ansible\-collections/community\.general/pull/7542)\)\.
* kernel\_blacklist \- use new <code>VarDict</code> to prevent deprecation warning \([https\://github\.com/ansible\-collections/community\.general/issues/8410](https\://github\.com/ansible\-collections/community\.general/issues/8410)\, [https\://github\.com/ansible\-collections/community\.general/pull/8411](https\://github\.com/ansible\-collections/community\.general/pull/8411)\)\.
* keycloak\_\* \- fix Keycloak API client to quote <code>/</code> properly \([https\://github\.com/ansible\-collections/community\.general/pull/7641](https\://github\.com/ansible\-collections/community\.general/pull/7641)\)\.
* keycloak\_authz\_permission \- resource payload variable for scope\-based permission was constructed as a string\, when it needs to be a list\, even for a single item \([https\://github\.com/ansible\-collections/community\.general/issues/7151](https\://github\.com/ansible\-collections/community\.general/issues/7151)\)\.
* keycloak\_client \- add sorted <code>defaultClientScopes</code> and <code>optionalClientScopes</code> to normalizations \([https\://github\.com/ansible\-collections/community\.general/pull/8223](https\://github\.com/ansible\-collections/community\.general/pull/8223)\)\.
* keycloak\_client \- fix TypeError when sanitizing the <code>saml\.signing\.private\.key</code> attribute in the module\'s diff or state output\. The <code>sanitize\_cr</code> function expected a dict where in some cases a list might occur \([https\://github\.com/ansible\-collections/community\.general/pull/8403](https\://github\.com/ansible\-collections/community\.general/pull/8403)\)\.
* keycloak\_client \- fixes issue when metadata is provided in desired state when task is in check mode \([https\://github\.com/ansible\-collections/community\.general/issues/1226](https\://github\.com/ansible\-collections/community\.general/issues/1226)\, [https\://github\.com/ansible\-collections/community\.general/pull/7881](https\://github\.com/ansible\-collections/community\.general/pull/7881)\)\.
* keycloak\_identity\_provider \- <code>mappers</code> processing was not idempotent if the mappers configuration list had not been sorted by name \(in ascending order\)\. Fix resolves the issue by sorting mappers in the desired state using the same key which is used for obtaining existing state \([https\://github\.com/ansible\-collections/community\.general/pull/7418](https\://github\.com/ansible\-collections/community\.general/pull/7418)\)\.
* keycloak\_identity\_provider \- it was not possible to reconfigure \(add\, remove\) <code>mappers</code> once they were created initially\. Removal was ignored\, adding new ones resulted in dropping the pre\-existing unmodified mappers\. Fix resolves the issue by supplying correct input to the internal update call \([https\://github\.com/ansible\-collections/community\.general/pull/7418](https\://github\.com/ansible\-collections/community\.general/pull/7418)\)\.
* keycloak\_realm \- add normalizations for <code>enabledEventTypes</code> and <code>supportedLocales</code> \([https\://github\.com/ansible\-collections/community\.general/pull/8224](https\://github\.com/ansible\-collections/community\.general/pull/8224)\)\.
* keycloak\_user \- when <code>force</code> is set\, but user does not exist\, do not try to delete it \([https\://github\.com/ansible\-collections/community\.general/pull/7696](https\://github\.com/ansible\-collections/community\.general/pull/7696)\)\.
* keycloak\_user\_federation \- fix diff of empty <code>krbPrincipalAttribute</code> \([https\://github\.com/ansible\-collections/community\.general/pull/8320](https\://github\.com/ansible\-collections/community\.general/pull/8320)\)\.
* ldap \- previously the order number \(if present\) was expected to follow an equals sign in the DN\. This makes it so the order number string is identified correctly anywhere within the DN \([https\://github\.com/ansible\-collections/community\.general/issues/7646](https\://github\.com/ansible\-collections/community\.general/issues/7646)\)\.
* linode inventory plugin \- add descriptive error message for linode inventory plugin \([https\://github\.com/ansible\-collections/community\.general/pull/8133](https\://github\.com/ansible\-collections/community\.general/pull/8133)\)\.
* locale\_gen \- use new <code>VarDict</code> to prevent deprecation warning \([https\://github\.com/ansible\-collections/community\.general/issues/8410](https\://github\.com/ansible\-collections/community\.general/issues/8410)\, [https\://github\.com/ansible\-collections/community\.general/pull/8411](https\://github\.com/ansible\-collections/community\.general/pull/8411)\)\.
* log\_entries callback plugin \- replace <code>ssl\.wrap\_socket</code> that was removed from Python 3\.12 with code for creating a proper SSL context \([https\://github\.com/ansible\-collections/community\.general/pull/7542](https\://github\.com/ansible\-collections/community\.general/pull/7542)\)\.
* lvol \- test for output messages in both <code>stdout</code> and <code>stderr</code> \([https\://github\.com/ansible\-collections/community\.general/pull/7601](https\://github\.com/ansible\-collections/community\.general/pull/7601)\, [https\://github\.com/ansible\-collections/community\.general/issues/7182](https\://github\.com/ansible\-collections/community\.general/issues/7182)\)\.
* merge\_variables lookup plugin \- fixing cross host merge\: providing access to foreign hosts variables to the perspective of the host that is performing the merge \([https\://github\.com/ansible\-collections/community\.general/pull/8303](https\://github\.com/ansible\-collections/community\.general/pull/8303)\)\.
* mksysb \- use new <code>VarDict</code> to prevent deprecation warning \([https\://github\.com/ansible\-collections/community\.general/issues/8410](https\://github\.com/ansible\-collections/community\.general/issues/8410)\, [https\://github\.com/ansible\-collections/community\.general/pull/8411](https\://github\.com/ansible\-collections/community\.general/pull/8411)\)\.
* modprobe \- listing modules files or modprobe files could trigger a FileNotFoundError if <code>/etc/modprobe\.d</code> or <code>/etc/modules\-load\.d</code> did not exist\. Relevant functions now return empty lists if the directories do not exist to avoid crashing the module \([https\://github\.com/ansible\-collections/community\.general/issues/7717](https\://github\.com/ansible\-collections/community\.general/issues/7717)\)\.
* mssql\_script \- make the module work with Python 2 \([https\://github\.com/ansible\-collections/community\.general/issues/7818](https\://github\.com/ansible\-collections/community\.general/issues/7818)\, [https\://github\.com/ansible\-collections/community\.general/pull/7821](https\://github\.com/ansible\-collections/community\.general/pull/7821)\)\.
* nmcli \- fix <code>connection\.slave\-type</code> wired to <code>bond</code> and not with parameter <code>slave\_type</code> in case of connection type <code>wifi</code> \([https\://github\.com/ansible\-collections/community\.general/issues/7389](https\://github\.com/ansible\-collections/community\.general/issues/7389)\)\.
* ocapi\_utils\, oci\_utils\, redfish\_utils module utils \- replace <code>type\(\)</code> calls with <code>isinstance\(\)</code> calls \([https\://github\.com/ansible\-collections/community\.general/pull/7501](https\://github\.com/ansible\-collections/community\.general/pull/7501)\)\.
* onepassword lookup plugin \- failed for fields that were in sections and had uppercase letters in the label/ID\. Field lookups are now case insensitive in all cases \([https\://github\.com/ansible\-collections/community\.general/pull/7919](https\://github\.com/ansible\-collections/community\.general/pull/7919)\)\.
* onepassword lookup plugin \- field and section titles are now case insensitive when using op CLI version two or later\. This matches the behavior of version one \([https\://github\.com/ansible\-collections/community\.general/pull/7564](https\://github\.com/ansible\-collections/community\.general/pull/7564)\)\.
* opentelemetry callback plugin \- close spans always \([https\://github\.com/ansible\-collections/community\.general/pull/8367](https\://github\.com/ansible\-collections/community\.general/pull/8367)\)\.
* opentelemetry callback plugin \- honour the <code>disable\_logs</code> option to avoid storing task results since they are not used regardless \([https\://github\.com/ansible\-collections/community\.general/pull/8373](https\://github\.com/ansible\-collections/community\.general/pull/8373)\)\.
* pacemaker\_cluster \- actually implement check mode\, which the module claims to support\. This means that until now the module also did changes in check mode \([https\://github\.com/ansible\-collections/community\.general/pull/8081](https\://github\.com/ansible\-collections/community\.general/pull/8081)\)\.
* pam\_limits \- when the file does not exist\, do not create it in check mode \([https\://github\.com/ansible\-collections/community\.general/issues/8050](https\://github\.com/ansible\-collections/community\.general/issues/8050)\, [https\://github\.com/ansible\-collections/community\.general/pull/8057](https\://github\.com/ansible\-collections/community\.general/pull/8057)\)\.
* pipx module utils \- change the CLI argument formatter for the <code>pip\_args</code> parameter \([https\://github\.com/ansible\-collections/community\.general/issues/7497](https\://github\.com/ansible\-collections/community\.general/issues/7497)\, [https\://github\.com/ansible\-collections/community\.general/pull/7506](https\://github\.com/ansible\-collections/community\.general/pull/7506)\)\.
* pipx\_info \- use new <code>VarDict</code> to prevent deprecation warning \([https\://github\.com/ansible\-collections/community\.general/issues/8410](https\://github\.com/ansible\-collections/community\.general/issues/8410)\, [https\://github\.com/ansible\-collections/community\.general/pull/8411](https\://github\.com/ansible\-collections/community\.general/pull/8411)\)\.
* pkgin \- pkgin \(pkgsrc package manager used by SmartOS\) raises erratic exceptions and spurious <code>changed\=true</code> \([https\://github\.com/ansible\-collections/community\.general/pull/7971](https\://github\.com/ansible\-collections/community\.general/pull/7971)\)\.
* proxmox \- fix updating a container config if the setting does not already exist \([https\://github\.com/ansible\-collections/community\.general/pull/7872](https\://github\.com/ansible\-collections/community\.general/pull/7872)\)\.
* proxmox\_kvm \- fixed status check getting from node\-specific API endpoint \([https\://github\.com/ansible\-collections/community\.general/issues/7817](https\://github\.com/ansible\-collections/community\.general/issues/7817)\)\.
* proxmox\_kvm \- running <code>state\=template</code> will first check whether VM is already a template \([https\://github\.com/ansible\-collections/community\.general/pull/7792](https\://github\.com/ansible\-collections/community\.general/pull/7792)\)\.
* proxmox\_pool\_member \- absent state for type VM did not delete VMs from the pools \([https\://github\.com/ansible\-collections/community\.general/pull/7464](https\://github\.com/ansible\-collections/community\.general/pull/7464)\)\.
* puppet \- add option <code>environment\_lang</code> to set the environment language encoding\. Defaults to lang <code>C</code>\. It is recommended to set it to <code>C\.UTF\-8</code> or <code>en\_US\.UTF\-8</code> depending on what is available on your system\. \([https\://github\.com/ansible\-collections/community\.general/issues/8000](https\://github\.com/ansible\-collections/community\.general/issues/8000)\)
* redfish\_command \- fix usage of message parsing in <code>SimpleUpdate</code> and <code>MultipartHTTPPushUpdate</code> commands to treat the lack of a <code>MessageId</code> as no message \([https\://github\.com/ansible\-collections/community\.general/issues/7465](https\://github\.com/ansible\-collections/community\.general/issues/7465)\, [https\://github\.com/ansible\-collections/community\.general/pull/7471](https\://github\.com/ansible\-collections/community\.general/pull/7471)\)\.
* redfish\_info \- allow for a GET operation invoked by <code>GetUpdateStatus</code> to allow for an empty response body for cases where a service returns 204 No Content \([https\://github\.com/ansible\-collections/community\.general/issues/8003](https\://github\.com/ansible\-collections/community\.general/issues/8003)\)\.
* redfish\_info \- correct uncaught exception when attempting to retrieve <code>Chassis</code> information \([https\://github\.com/ansible\-collections/community\.general/pull/7952](https\://github\.com/ansible\-collections/community\.general/pull/7952)\)\.
* redhat\_subscription \- use the D\-Bus registration on RHEL 7 only on 7\.4 and
  greater\; older versions of RHEL 7 do not have it
  \([https\://github\.com/ansible\-collections/community\.general/issues/7622](https\://github\.com/ansible\-collections/community\.general/issues/7622)\,
  [https\://github\.com/ansible\-collections/community\.general/pull/7624](https\://github\.com/ansible\-collections/community\.general/pull/7624)\)\.
* riak \- support <code>riak admin</code> sub\-command in newer Riak KV versions beside the legacy <code>riak\-admin</code> main command \([https\://github\.com/ansible\-collections/community\.general/pull/8211](https\://github\.com/ansible\-collections/community\.general/pull/8211)\)\.
* snap \- use new <code>VarDict</code> to prevent deprecation warning \([https\://github\.com/ansible\-collections/community\.general/issues/8410](https\://github\.com/ansible\-collections/community\.general/issues/8410)\, [https\://github\.com/ansible\-collections/community\.general/pull/8411](https\://github\.com/ansible\-collections/community\.general/pull/8411)\)\.
* snap\_alias \- use new <code>VarDict</code> to prevent deprecation warning \([https\://github\.com/ansible\-collections/community\.general/issues/8410](https\://github\.com/ansible\-collections/community\.general/issues/8410)\, [https\://github\.com/ansible\-collections/community\.general/pull/8411](https\://github\.com/ansible\-collections/community\.general/pull/8411)\)\.
* statusio\_maintenance \- fix error caused by incorrectly formed API data payload\. Was raising \"Failed to create maintenance HTTP Error 400 Bad Request\" caused by bad data type for date/time and deprecated dict keys \([https\://github\.com/ansible\-collections/community\.general/pull/7754](https\://github\.com/ansible\-collections/community\.general/pull/7754)\)\.
* terraform \- fix multiline string handling in complex variables \([https\://github\.com/ansible\-collections/community\.general/pull/7535](https\://github\.com/ansible\-collections/community\.general/pull/7535)\)\.
* to\_ini filter plugin \- disabling interpolation of <code>ConfigParser</code> to allow converting values with a <code>\%</code> sign \([https\://github\.com/ansible\-collections/community\.general/issues/8183](https\://github\.com/ansible\-collections/community\.general/issues/8183)\, [https\://github\.com/ansible\-collections/community\.general/pull/8185](https\://github\.com/ansible\-collections/community\.general/pull/8185)\)\.
* xml \- make module work with lxml 5\.1\.1\, which removed some internals that the module was relying on \([https\://github\.com/ansible\-collections/community\.general/pull/8169](https\://github\.com/ansible\-collections/community\.general/pull/8169)\)\.

<a id="community-grafana-2"></a>
#### community\.grafana

* Add <em class="title-reference">grafana\_organiazion\_user</em> to <em class="title-reference">action\_groups\.grafana</em>
* Fixed orgId handling in diff comparison for <em class="title-reference">grafana\_datasource</em> if using org\_name
* Handling of desired default state for first <em class="title-reference">grafana\_datasource</em>
* Ignore <em class="title-reference">type</em> argument for diff comparison if <em class="title-reference">grafana\-postgresq\-datasource</em> alias <em class="title-reference">postgres</em> is used
* Set umask for <em class="title-reference">grafana\_plugin</em> command
* test\: replace deprecated <em class="title-reference">TestCase\.assertEquals</em> to support Python 3\.12
* undo removed deprecated <em class="title-reference">message</em> argument in <em class="title-reference">grafana\_dashboard</em>

<a id="community-hrobot-7"></a>
#### community\.hrobot

* inventory plugins \- add unsafe wrapper to avoid marking strings that do not contain <code>\{</code> or <code>\}</code> as unsafe\, to work around a bug in AWX \([https\://github\.com/ansible\-collections/community\.hrobot/pull/102](https\://github\.com/ansible\-collections/community\.hrobot/pull/102)\)\.

<a id="community-mysql-7"></a>
#### community\.mysql

* mysql\_info \- the <code>slave\_status</code> filter was returning an empty list on MariaDB with multiple replication channels\. It now returns all channels by running <code>SHOW ALL SLAVES STATUS</code> for MariaDB servers \([https\://github\.com/ansible\-collections/community\.mysql/issues/603](https\://github\.com/ansible\-collections/community\.mysql/issues/603)\)\.

<a id="community-postgresql-9"></a>
#### community\.postgresql

* postgresql\_db \- <code>restore</code> custom format as file instead of stdin to allow the use of \-\-job flag in <code>target\_opts</code> \([https\://github\.com/ansible\-collections/community\.postgresql/issues/594](https\://github\.com/ansible\-collections/community\.postgresql/issues/594)\)\.
* postgresql\_ext \- Reconnect before upgrade to avoid accidental load of the upgraded extension \([https\://github\.com/ansible\-collections/community\.postgresql/pull/689](https\://github\.com/ansible\-collections/community\.postgresql/pull/689)\)\.
* postgresql\_idx \- consider schema name when checking for index \([https\://github\.com/ansible\-collections/community\.postgresql/issues/692](https\://github\.com/ansible\-collections/community\.postgresql/issues/692)\)\.  Index names are only unique within a schema\. This allows using the same index name in multiple schemas\.
* postgresql\_privs \- Enables the ability to revoke functions from user \([https\://github\.com/ansible\-collections/community\.postgresql/issues/687](https\://github\.com/ansible\-collections/community\.postgresql/issues/687)\)\.
* postgresql\_privs \- fix a failure when altering privileges with <code>grant\_option\: true</code> \([https\://github\.com/ansible\-collections/community\.postgresql/issues/668](https\://github\.com/ansible\-collections/community\.postgresql/issues/668)\)\.
* postgresql\_query \- now reports not changed for queries starting with \"SHOW\" \([https\://github\.com/ansible\-collections/community\.postgresql/pull/592](https\://github\.com/ansible\-collections/community\.postgresql/pull/592)\)\.
* postgresql\_user \- module failed when running against an SQL\_ASCII encoded database as the user\'s current password was returned as bytes as opposed to a str\. Fix now checks for this case and decodes the bytes as an ascii encoded string\. \([https\://github\.com/ansible\-collections/community\.postgresql/issues/584](https\://github\.com/ansible\-collections/community\.postgresql/issues/584)\)\.

<a id="community-routeros-8"></a>
#### community\.routeros

* facts \- fix date not getting removed for idempotent config export \([https\://github\.com/ansible\-collections/community\.routeros/pull/262](https\://github\.com/ansible\-collections/community\.routeros/pull/262)\)\.

<a id="community-sap-libs"></a>
#### community\.sap\_libs

* fixes failures in sanity test for all modules

<a id="community-vmware-12"></a>
#### community\.vmware

* Clarify pyVmomi requirement \([https\://github\.com/ansible\-collections/community\.vmware/pull/2071](https\://github\.com/ansible\-collections/community\.vmware/pull/2071)\)\.
* Fix InsecureRequestWarning for modules based on the VmwareRestClient module util when setting <code>validate\_certs</code> to <code>False</code> \([https\://github\.com/ansible\-collections/community\.vmware/pull/1969](https\://github\.com/ansible\-collections/community\.vmware/pull/1969)\)\.
* Use <em class="title-reference">isinstance\(\)</em> instead of <em class="title-reference">type\(\)</em> for a typecheck \([https\://github\.com/ansible\-collections/community\.vmware/pull/2011](https\://github\.com/ansible\-collections/community\.vmware/pull/2011)\)\.
* module\_utils/vmware\.py \- remove ssl\.wrap\_socet\(\) function\. Replaced for code based on ssl\.get\_server\_certificate \([https\://github\.com/ansible\-collections/community\.vmware/issues/1930](https\://github\.com/ansible\-collections/community\.vmware/issues/1930)\)\.
* vmware\_cluster\_dpm \- Handle case where DPM config has not been initialized yet and is None \([https\://github\.com/ansible\-collections/community\.vmware/pull/2057](https\://github\.com/ansible\-collections/community\.vmware/pull/2057)\)\.
* vmware\_dvs\_portgroup \- Fix erroneously reporting a change when <em class="title-reference">port\_binding</em> is static and <em class="title-reference">num\_ports</em> not specified \([https\://github\.com/ansible\-collections/community\.vmware/pull/2053](https\://github\.com/ansible\-collections/community\.vmware/pull/2053)\)\.
* vmware\_guest \- Fix a error while updating the VM by adding a new disk\. While adding a disk to an  existing VM\, it leaves it in invalid state\. \([https\://github\.com/ansible\-collections/community\.vmware/pull/2044](https\://github\.com/ansible\-collections/community\.vmware/pull/2044)\)\.
* vmware\_guest \- Fix a missing error message while setting a template parameter with inconsistency guest\_os ID \([https\://github\.com/ansible\-collections/community\.vmware/pull/2036](https\://github\.com/ansible\-collections/community\.vmware/pull/2036)\)\.
* vmware\_guest \- Fix failure of vm reconfiguration with enabled virt\_based\_security \([https\://github\.com/ansible\-collections/community\.vmware/pull/1848](https\://github\.com/ansible\-collections/community\.vmware/pull/1848)\)\.
* vmware\_vm\_info \- Fix an AttributeError when gathering network information \([https\://github\.com/ansible\-collections/community\.vmware/pull/1919](https\://github\.com/ansible\-collections/community\.vmware/pull/1919)\)\.

<a id="community-windows-3"></a>
#### community\.windows

* Remove some code which is no longer valid for dotnet 5\+
* community\.windows\.win\_psmodule\_info \- exception thrown when host has no Installed Module\. Fix now checks that variable \$installedModules is not null before calling the \.Contains\(\.\.\) function on it\.
* win\_format\, win\_partition \- Add support for Windows failover cluster disks
* win\_psmodule \- Fix up error message with <code>state\=latest</code>
* win\_rabbitmq\_plugin \- Avoid using <code>Invoke\-Expression</code> when running external commands
* win\_rds\_rap \- The module crashed when creating a RAP with Gateway Managed Computer Group \([https\://github\.com/ansible\-collections/community\.windows/issues/184](https\://github\.com/ansible\-collections/community\.windows/issues/184)\)\.
* win\_robocopy \- Fix up <code>cmd</code> return value to include the executable <code>robocopy</code>

<a id="community-zabbix-3"></a>
#### community\.zabbix

* Avoid to update user\-directory configuration in dry run\.
* api module \- Fixed certificiate errors
* proxy and server roles \- Defaulted location of fping and fping6 based on OS\.
* proxy role \- Removed requirement for mysql group definition\.
* server role \- typo in configuration var StasAllowedIP to StatsAllowedIP
* zabbix\-\{agent\, javagateway\, proxy\, server\, web\} \- support raspberry pi without repository url specification
* zabbix\_agent \- Fixed IPMI authentication algorithm default setting
* zabbix\_agent \- Fixed issue to where scripts can be deployed alongside userparameters
* zabbix\_host \- Don\'t reset IPMI setting when update inventory data of a host
* zabbix\_host \- Finish task with failed if host\_group parameter is empty list
* zabbix\_inventory \- fixed handeling of add\_zabbix\_groups option
* zabbix\_server \- proper indentaion of become in selinux\.yaml
* zabbix\_template \- fix template export when template\'s content has \"error\" word
* zabbix\_web \- Added missing semicolon to nginx vhost template\.
* zabbix\_web role \- fix variable naming issues \(undefined\) to zabbix\_web\_version and zabbix\_web\_apt\_repository
* zabbix\_web role\, Add missing selinux\.yml tasks\.

<a id="containers-podman-12"></a>
#### containers\.podman

* Add idempotency for podman\_secret module
* Catch exceptions when no JSON output in podman\_image
* Fail if systemd generation failed and it\'s explicitly set
* Fix example name
* Fix idempotency for podman\_network
* Fix idempotency when using 0\.0\.0\.0 in ports
* Fix multi\-image support for podman\_save
* Fix pod info for non\-existant pods
* Fix volume inspection by name in podman\_volume
* Recreate stopped containers if recreate flag is enabled
* podman\_container \- Add check and fixed for v5 network diff
* podman\_container \- Fix pasta networking idempotency for v5 \(\#728\)
* podman\_container\_exec \- Remove unnecessary quotes in podman\_container\_exec module
* podman\_image\_info \- Fix wrong return data type in podman\_image\_info
* podman\_play \- Fix kube play annotations
* podman\_pod \- Fix broken info of pods in Podman v5
* podman\_pod \- Fix pod for Podman v5
* podman\_pod \- Fix podman pod v5 broken info issue

<a id="dellemc-enterprise-sonic-5"></a>
#### dellemc\.enterprise\_sonic

* requirements \- Update requires\_ansible version in meta/runtime\.yml to the oldest supported version \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/321](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/321)\)\.
* sonic\_bgp\_communities \- Fix incorrect \"facts\" handling for parsing of a BGP community list configured with an empty \"members\" list \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/319](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/319)\)\.
* sonic\_bgp\_neighbors \- Fix prefix\-limit issue \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/289](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/289)\)\.
* sonic\_interfaces \- Add warnings when speed and auto\_negotiate is configured at same time \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/314](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/314)\)\.
* sonic\_interfaces \- Fix support for standard naming interfaces \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/314](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/314)\)\.
* sonic\_interfaces \- Prevent configuring speed in port group interfaces \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/314](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/314)\)\.
* sonic\_stp \- Correct the commands list for STP delete state \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/302](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/302)\)\.

<a id="dellemc-openmanage-26"></a>
#### dellemc\.openmanage

* Added support for RAID creation using NVMe disks\.\([https\://github\.com/dell/dellemc\-openmanage\-ansible\-modules/issues/635](https\://github\.com/dell/dellemc\-openmanage\-ansible\-modules/issues/635)\)
* Fixed the issue for ignoring the environment variable <em class="title-reference">NO\_PROXY</em> earlier\. \([https\://github\.com/dell/dellemc\-openmanage\-ansible\-modules/issues/554](https\://github\.com/dell/dellemc\-openmanage\-ansible\-modules/issues/554)\)
* For idrac\_certificates module\, the <em class="title-reference">email\_address</em> has been made as an optional parameter\. \([https\://github\.com/dell/dellemc\-openmanage\-ansible\-modules/issues/582](https\://github\.com/dell/dellemc\-openmanage\-ansible\-modules/issues/582)\)\.
* Issue is fixed for deploying a new configuration on quick deploy slot when IPv6 is disabled\.\([https\://github\.com/dell/dellemc\-openmanage\-ansible\-modules/issues/533](https\://github\.com/dell/dellemc\-openmanage\-ansible\-modules/issues/533)\)
* idrac\_network\_attributes \- Issue\(279049\) \-  If unsupported values are provided for the parameter <code>ome\_network\_attributes</code>\, then this module does not provide a correct error message\.
* ome\_device\_network\_services \- Issue\(212681\) \- The module does not provide a proper error message if unsupported values are provided for the following parameters\- port\_number\, community\_name\, max\_sessions\, max\_auth\_retries\, and idle\_timeout\.
* ome\_device\_power\_settings \- Issue\(212679\) \- The module displays the following message if the value provided for the parameter <code>power\_cap</code> is not within the supported range of 0 to 32767\, <code>Unable to complete the request because PowerCap does not exist or is not applicable for the resource URI\.</code>
* ome\_inventory \- The plugin returns 50 results when a group is specified\. No results are shown when a group is not specified\. \([https\://github\.com/dell/dellemc\-openmanage\-ansible\-modules/issues/575](https\://github\.com/dell/dellemc\-openmanage\-ansible\-modules/issues/575)\)\.
* redfish\_storage\_volume is enhanced to support iDRAC8\.\([https\://github\.com/dell/dellemc\-openmanage\-ansible\-modules/issues/625](https\://github\.com/dell/dellemc\-openmanage\-ansible\-modules/issues/625)\)

<a id="f5networks-f5-modules-6"></a>
#### f5networks\.f5\_modules

* bigip\_gtm\_monitor\_bigip \- fixed an issue where IP and port were not applied correctly when creating new monitor\.
* bigip\_gtm\_monitor\_firepass \- fixed an issue where IP and port were not applied correctly when creating new monitor\.
* bigip\_gtm\_monitor\_http \- fixed an issue where IP and port were not applied correctly when creating new monitor\.
* bigip\_gtm\_monitor\_https\- fixed an issue where IP and port were not applied correctly when creating new monitor\.
* bigip\_gtm\_monitor\_tcp \- fixed an issue where IP and port were not applied correctly when creating new monitor\.
* bigip\_gtm\_monitor\_tcp\_half\_open \- fixed an issue where IP and port were not applied correctly when creating new monitor\.
* bigip\_gtm\_topology\_region \- fixed an issue where if multiple states with spaces in values were defined\, module would throw invalid command error
* bigip\_gtm\_topology\_region \- fixed an issue where states names that contained spaces caused the idempotency to break\.
* bigip\_ssl\_key\_cert \- fixed an issue where the passphrase was not being properly send to the BIG\-IP\.

<a id="fortinet-fortimanager-10"></a>
#### fortinet\.fortimanager

* Added missing enum values for some arguments\.
* Change minimum required ansible\-core version to 2\.14\.0
* Changed revision to v\_range to reduce the size of the code\.
* Fixed a bug where ansible may skip update incorrectly\.
* Fixed the behavior of module fmgr\_firewall\_internetservicecustom\.
* Fixed the behavior of some modules that contain the argument policyid\.
* Improved bypass\_validation\. If you now set bypass\_validation to true\, it will allow you to send parameters that are not defined in the schema\.
* Improved documentation\, added description for all \"no description\" modules\.
* Improved documentation\.
* Improved example ansible playbooks\.
* Improved the logic of fmgr\_fact\, fmgr\_clone\, fmgr\_rename\, fmgr\_move\. Usage remains unchanged\.
* Reduced the size of module\_arg\_spec in each module\.
* Removed most of the sanity test ignores\.
* Support FortiManager 7\.0\.10
* Supported \"state\:absent\" for all modules end with \"\_objectmember\"\, \"\_scopemember\"\, and \"\_scetionvalue\"\.
* Supported FortiManager 6\.4\.14\, 7\.0\.11\, 7\.0\.12\, 7\.2\.5\.

<a id="fortinet-fortios-5"></a>
#### fortinet\.fortios

* Fix the issue that ssl\-certificate cannot be set in <em class="title-reference">fortios\_firewall\_vip</em> and <em class="title-reference">fortios\_firewall\_vip6</em>\.
* Github issue
* mantis issue

<a id="hetzner-hcloud-2"></a>
#### hetzner\.hcloud

* hcloud inventory \- Ensure the API client use a new cache for every <em>cached session</em>\.
* inventory \- Ensure inventory host variables are serializable and can be cached\.
* load\_balancer\_info \- Correctly return the <em class="title-reference">cookie\_lifetime</em> value\.
* load\_balancer\_service \- Correctly return the <em class="title-reference">cookie\_lifetime</em> value\.
* primary\_ip \- Added the missing <em class="title-reference">auto\_delete</em> field to the return values\.
* primary\_ip \- The <em class="title-reference">auto\_delete</em> option is now used when creating or updating a Primary IP\.
* primary\_ip\_info \- Added the missing <em class="title-reference">auto\_delete</em> field to the return values\.
* server \- Do not remove the server from its placement group when the <em class="title-reference">placement\_group</em> argument is not specified\.
* server \- Pass an empty string to the <em class="title-reference">placement\_group</em> argument to remove a server from its placement group\.
* server\_network \- The returned <em class="title-reference">alias\_ips</em> list is now sorted\.

<a id="ibm-qradar-1"></a>
#### ibm\.qradar

* A bunch of ansible\-lint and ansible\-test sanity issues have been fixed\.

<a id="ibm-storage-virtualize-5"></a>
#### ibm\.storage\_virtualize

* ibm\_svc\_info \- Command and release mapping to remove errors in gather\_subset\=all
* ibm\_svc\_info \- Return error in listing entities that require object name

<a id="infoblox-nios-modules-6"></a>
#### infoblox\.nios\_modules

* Fixes environment variable max\_results using INFOBLOX\_MAX\_RESULTS [\#209](https\://github\.com/infobloxopen/infoblox\-ansible/pull/209)
* Fixes index error for transform fields in DTC LBDN \(auth\_zone and Pool\) and DTC POOL \(servers and monitors\)\. [\#209](https\://github\.com/infobloxopen/infoblox\-ansible/pull/209)
* Fixes typo for environment variable INFOBLOX\_WAPI\_VERSION [\#209](https\://github\.com/infobloxopen/infoblox\-ansible/pull/209)

<a id="junipernetworks-junos-3"></a>
#### junipernetworks\.junos

* Fix the empty facts list placement
* Prevents module\_defaults from were being incorrectly applied to the platform action\, instead of the concerned module\.
* acls
* fix to gather l2\_interfaces facts with default port\-mode access\.
* initialize facts dictionary with empty containers for respective resources mentioned below
* lldp\_global
* lldp\_interfaces
* logging\_global
* ntp\_global
* ospf\_interfaces
* ospfv2
* ospfv3
* prefix\_lists
* routing\_instances
* routing\_options
* security\_policies
* security\_policies\_global
* security\_zones
* snmp\_server
* static\_routes
* vlans

<a id="kubernetes-core-4"></a>
#### kubernetes\.core

* Resolve Collections util resource discovery fails when complex subresources present \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/676](https\://github\.com/ansible\-collections/kubernetes\.core/pull/676)\)\.
* align <em class="title-reference">helmdiff\_check\(\)</em> function commandline rendering with the <em class="title-reference">deploy\(\)</em> function \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/670](https\://github\.com/ansible\-collections/kubernetes\.core/pull/670)\)\.
* helm \- Put the chart\_ref into quotes when running <code>helm show chart</code>\, <code>helm upgrade</code> and <code>helm dependency update</code> commands \([https\://github\.com/ansible\-collections/kubernetes\.core/issues/653](https\://github\.com/ansible\-collections/kubernetes\.core/issues/653)\)\.
* helm \- delete temporary file created when deploying chart with option <code>release\_values</code> set \([https\://github\.com/ansible\-collections/kubernetes\.core/issues/530](https\://github\.com/ansible\-collections/kubernetes\.core/issues/530)\)\.
* helm \- expand kubeconfig path with user\'s home directory for consistency with k8s
* helm \- fix issue occurring when uninstalling chart with statues others than <code>deployed</code> \([https\://github\.com/ansible\-collections/kubernetes\.core/issues/319](https\://github\.com/ansible\-collections/kubernetes\.core/issues/319)\)\.
* helm \- fix post\_renderer argument breaking the helm deploy\_command \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/586](https\://github\.com/ansible\-collections/kubernetes\.core/pull/586)\)\.
* helm \- use <code>reuse\-values</code> when running <code>helm diff</code> command \([https\://github\.com/ansible\-collections/kubernetes\.core/issues/680](https\://github\.com/ansible\-collections/kubernetes\.core/issues/680)\)\.
* helm \- use post\_renderer when checking <code>changed</code> status for a helm release \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/588](https\://github\.com/ansible\-collections/kubernetes\.core/pull/588)\)\.
* integrations test helm\_kubeconfig \- set helm version to v3\.10\.3 to avoid incompatability with new bitnami charts \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/670](https\://github\.com/ansible\-collections/kubernetes\.core/pull/670)\)\.
* k8s\_json\_patch \- rename action symlink to ensure k8s action plugin is used \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/652](https\://github\.com/ansible\-collections/kubernetes\.core/pull/652)\)\.
* k8s\_scale \- clean handling of ResourceTimeout exception \([https\://github\.com/ansible\-collections/kubernetes\.core/issues/583](https\://github\.com/ansible\-collections/kubernetes\.core/issues/583)\)\.
* k8s\_scale \- fix issue when scaling StatefulSets with <code>updateStrategy\=OnDelete</code> \([https\://github\.com/ansible\-collections/kubernetes\.core/issues/579](https\://github\.com/ansible\-collections/kubernetes\.core/issues/579)\)\.

<a id="lowlydba-sqlserver-3"></a>
#### lowlydba\.sqlserver

* Add ActiveStartDate to the compare properties so this item is marked accurately as changed\.
* Fixed the formatting of the SPN by updating the backslash to a forward\-slash for the \$spn var \(lowlydba\.sqlserver\.spn\)
* Update documentation for agent\_job\_schedule to reflect proper input formatting\. \([https\://github\.com/lowlydba/lowlydba\.sqlserver/pull/229](https\://github\.com/lowlydba/lowlydba\.sqlserver/pull/229)\)

<a id="microsoft-ad-6"></a>
#### microsoft\.ad

* debug\_ldap\_client \- handle failures when attempting to get the krb5 context and default CCache rather than fail with a traceback
* microsoft\.ad\.group \- Support membership lookup of groups that are longer than 20 characters long
* microsoft\.ad\.membership \- Add helpful hint when the failure was due to a missing/invalid <code>domain\_ou\_path</code> \- [https\://github\.com/ansible\-collections/microsoft\.ad/issues/88](https\://github\.com/ansible\-collections/microsoft\.ad/issues/88)

<a id="netapp-ontap-6"></a>
#### netapp\.ontap

* na\_ontap\_dns \- fix issue with modifying DNS servers in REST\.
* na\_ontap\_ems\_destination \- fix field error with <em class="title-reference">certificate\.name</em> for ONTAP 9\.11\.1 or later in REST\.
* na\_ontap\_fpolicy\_policy \- fixed issue with idempotency in REST\.
* na\_ontap\_igroup\_initiator \- fixed issue with idempotency\.
* na\_ontap\_nfs \- fix error with <em class="title-reference">windows</em> in REST for ONTAP 9\.10 or earlier\.
* na\_ontap\_quotas \- fixed issue with idempotency in REST\.
* na\_ontap\_security\_certificates \- fix error with ontap\_info returned in module output in REST\.
* na\_ontap\_security\_config \- added warning for missing <em class="title-reference">supported\_cipher\_suites</em> to maintain idempotency in REST\.
* na\_ontap\_snapshot\_policy \- fix issue with modifying snapshot policy in REST\.
* na\_ontap\_volume \- modified <em class="title-reference">type</em> to be case insensitive in REST\.
* na\_ontap\_vserver\_peer \- fix issue with peering multiple clusters with same vserver name in REST\.

<a id="netapp-storagegrid-1"></a>
#### netapp\.storagegrid

* Removed fetch limit in API request and implemented pagination\.

<a id="netbox-netbox-6"></a>
#### netbox\.netbox

* Improve error reporting for missing module \[\#1126\]\([https\://github\.com/netbox\-community/ansible\_modules/pull/1126](https\://github\.com/netbox\-community/ansible\_modules/pull/1126)\)
* nb\_inventory \- Fix API cache failure \[\#1111\]\([https\://github\.com/netbox\-community/ansible\_modules/pull/1111](https\://github\.com/netbox\-community/ansible\_modules/pull/1111)\)
* nb\_lookup \- Allow multiple IDs in nb\_lookup \[\#1042\]\([https\://github\.com/netbox\-community/ansible\_modules/pull/1042](https\://github\.com/netbox\-community/ansible\_modules/pull/1042)\)
* netbox\_vlan \- Fix documentation of vlan\_group \[\#1138\]\([https\://github\.com/netbox\-community/ansible\_modules/pull/1138](https\://github\.com/netbox\-community/ansible\_modules/pull/1138)\)

<a id="purestorage-flasharray-11"></a>
#### purestorage\.flasharray

* purefa\_cert \- Fixed issue where parts of the subject where not included in the CSR if they did not exist in the currently used cert\.
* purefa\_certs \- Allow certificates of over 3000 characters to be imported\.
* purefa\_dns \- Fixed attribute error on deletion of management DNS
* purefa\_ds \- Fix issue with SDK returning empty data for data directory services even when it does exist
* purefa\_host \- Allows all current host inititators to be correctly removed
* purefa\_host \- Fix idempotency issue with connected volume
* purefa\_info \- Resolved issue with KeyError when LACP bonds are in use
* purefa\_inventory \- Fix issue with iSCSI\-only FlashArrays
* purefa\_pg \- Allows a protection group to be correctly created when <em class="title-reference">target</em> is specified as well as other objects\, such as <em class="title-reference">volumes</em> or <em class="title-reference">hosts</em>
* purefa\_pgsched \- Fixed issue with disabling schedules
* purefa\_pgsnap \- Add support for restoring volumes connected to hosts in a host\-based protection group and hosts in a hostgroup\-based protection group\.
* purefa\_pgsnap \- Fixed incorrect parameter name
* purefa\_policy \- Fix incorrect call of psot instead of patch for NFS policies
* purefa\_volume \- Ensure module response for creation of volume and rerun are the same
* purefa\_volume \- Fix idempotency issue with delete volume

<a id="purestorage-flashblade-6"></a>
#### purestorage\.flashblade

* purefb\_bucket \- Changed logic to allow complex buckets to be created in a single call\, rather than having to split into two tasks\.
* purefb\_info \- Added missing object lock retention details if enabledd
* purefb\_lag \- Enable LAG port configuration with multi\-chassis
* purefb\_timeout \- Fixed arithmetic error that resulted in module incorrectly reporting changed when no change was required\.

<a id="splunk-es-1"></a>
#### splunk\.es

* Fixed argspec validation for plugins with empty task attributes when run with Ansible 2\.9\.

<a id="telekom-mms-icinga-director-3"></a>
#### telekom\_mms\.icinga\_director

* Fixes \#190 \- Workaround for service apply bug \([https\://github\.com/telekom\-mms/ansible\-collection\-icinga\-director/pull/239](https\://github\.com/telekom\-mms/ansible\-collection\-icinga\-director/pull/239)\)
* change notification interval variable to int\-type \([https\://github\.com/telekom\-mms/ansible\-collection\-icinga\-director/pull/254](https\://github\.com/telekom\-mms/ansible\-collection\-icinga\-director/pull/254)\)
* set user\_groups in notification to empty list \([https\://github\.com/telekom\-mms/ansible\-collection\-icinga\-director/pull/255](https\://github\.com/telekom\-mms/ansible\-collection\-icinga\-director/pull/255)\)

<a id="theforeman-foreman-6"></a>
#### theforeman\.foreman

* compute\_profile\, host \- refer to VMware storage pods by name\, not id \([https\://github\.com/theforeman/foreman\-ansible\-modules/issues/1247](https\://github\.com/theforeman/foreman\-ansible\-modules/issues/1247)\)
* content\_view\_filter\_rule \- handle multiple rules for the same package but different architectures and versions correctly \([https\://bugzilla\.redhat\.com/show\_bug\.cgi\?id\=2189687](https\://bugzilla\.redhat\.com/show\_bug\.cgi\?id\=2189687)\)

<a id="vmware-vmware-rest-4"></a>
#### vmware\.vmware\_rest

* content\_library\_item\_info \- fixed error with unsupported property
* lookup plugins \- Refactor to use native options configuration via doc\_fragment\, which ensures that vcenter\_validate\_certs\=false is honored \([https\://github\.com/ansible\-collections/vmware\.vmware\_rest/issues/425](https\://github\.com/ansible\-collections/vmware\.vmware\_rest/issues/425)\)\.

<a id="vultr-cloud-2"></a>
#### vultr\.cloud

* Fixed an error while waiting for a specific state and the API returns an empty response\. \([https\://github\.com/vultr/ansible\-collection\-vultr/issues/108](https\://github\.com/vultr/ansible\-collection\-vultr/issues/108)\)\.
* Fixed an issue with waiting for state \([https\://github\.com/vultr/ansible\-collection\-vultr/pull/102](https\://github\.com/vultr/ansible\-collection\-vultr/pull/102)\)\.
* instance \- Fixed an issue detecting the instance state returned by the API \([https\://github\.com/vultr/ansible\-collection\-vultr/pull/89](https\://github\.com/vultr/ansible\-collection\-vultr/pull/89)\)\.
* instance\_info \- Fixed the alias <code>name</code> being was used on the wrong argument\. \([https\://github\.com/vultr/ansible\-collection\-vultr/issues/105](https\://github\.com/vultr/ansible\-collection\-vultr/issues/105)\)\.
* reserved\_ip \- Fixed an issue which caused the module to fail\, also enabled integration tests \([https\://github\.com/vultr/ansible\-collection\-vultr/issues/92](https\://github\.com/vultr/ansible\-collection\-vultr/issues/92)\)\.

<a id="known-issues-7"></a>
### Known Issues

<a id="community-docker-16"></a>
#### community\.docker

* Please note that the fix for requests 2\.32\.0 included in community\.docker 3\.10\.1 only
  fixes problems with the <em>vendored</em> Docker SDK for Python code\. Modules and plugins that
  use Docker SDK for Python can still fail due to the SDK currently being incompatible
  with requests 2\.32\.0\.

  If you still experience problems with requests 2\.32\.0\, such as error messages like
  <code>Not supported URL scheme http\+docker</code>\, please restrict requests to <code>\<2\.32\.0</code>\.

<a id="dellemc-openmanage-27"></a>
#### dellemc\.openmanage

* idrac\_diagnostics \- Issue\(285322\) \- This module doesn\'t support export of diagnostics file to HTTP and HTTPS share via SOCKS proxy\.
* idrac\_firmware \- Issue\(279282\) \- This module does not support firmware update using HTTP\, HTTPS\, and FTP shares with authentication on iDRAC8\.
* idrac\_network\_attributes \- Issue\(279049\) \-  If unsupported values are provided for the parameter <code>ome\_network\_attributes</code>\, then this module does not provide a correct error message\.
* idrac\_storage\_volume \- Issue\(290766\) \- The module will report success instead of showing failure for new virtual creation on the BOSS\-N1 controller if a virtual disk is already present on the same controller\.
* ome\_device\_network\_services \- Issue\(212681\) \- The module does not provide a proper error message if unsupported values are provided for the following parameters\- port\_number\, community\_name\, max\_sessions\, max\_auth\_retries\, and idle\_timeout\.
* ome\_device\_power\_settings \- Issue\(212679\) \- The module displays the following message if the value provided for the parameter <code>power\_cap</code> is not within the supported range of 0 to 32767\, <code>Unable to complete the request because PowerCap does not exist or is not applicable for the resource URI\.</code>
* ome\_device\_quick\_deploy \- Issue\(275231\) \- This module does not deploy a new configuration to a slot that has disabled IPv6\.
* ome\_diagnostics \- Issue\(279193\) \- Export of SupportAssist collection logs to the share location fails on OME version 4\.0\.0\.
* ome\_smart\_fabric\_uplink \- Issue\(186024\) \- The module supported by OpenManage Enterprise Modular\, however it does not allow the creation of multiple uplinks of the same name\. If an uplink is created using the same name as an existing uplink\, then the existing uplink is modified\.

<a id="new-plugins-3"></a>
### New Plugins

<a id="become"></a>
#### Become

* community\.general\.run0 \- Systemd\'s run0\.

<a id="callback"></a>
#### Callback

* community\.general\.default\_without\_diff \- The default ansible callback without diff output\.
* community\.general\.timestamp \- Adds simple timestamp for each header\.

<a id="connection"></a>
#### Connection

* community\.general\.incus \- Run tasks in Incus instances via the Incus CLI\.

<a id="filter-3"></a>
#### Filter

* ansible\.utils\.fact\_diff \- Find the difference between currently set facts
* community\.crypto\.parse\_serial \- Convert a serial number as a colon\-separated list of hex numbers to an integer
* community\.crypto\.to\_serial \- Convert an integer to a colon\-separated list of hex numbers
* community\.dns\.quote\_txt \- Quotes a string to use as a TXT record entry
* community\.dns\.unquote\_txt \- Unquotes a TXT record entry to a string
* community\.general\.from\_ini \- Converts INI text input into a dictionary\.
* community\.general\.lists\_difference \- Difference of lists with a predictive order\.
* community\.general\.lists\_intersect \- Intersection of lists with a predictive order\.
* community\.general\.lists\_symmetric\_difference \- Symmetric Difference of lists with a predictive order\.
* community\.general\.lists\_union \- Union of lists with a predictive order\.
* community\.general\.to\_ini \- Converts a dictionary to the INI file format\.
* microsoft\.ad\.dn\_escape \- Escape an LDAP DistinguishedName value string\.
* microsoft\.ad\.parse\_dn \- Parses an LDAP DistinguishedName string into an object\.

<a id="lookup-1"></a>
#### Lookup

* community\.general\.github\_app\_access\_token \- Obtain short\-lived Github App Access tokens\.
* community\.general\.onepassword\_doc \- Fetch documents stored in 1Password\.

<a id="test-1"></a>
#### Test

* community\.general\.fqdn\_valid \- Validates fully\-qualified domain names against RFC 1123\.

<a id="new-modules-7"></a>
### New Modules

<a id="amazon-aws-10"></a>
#### amazon\.aws

* amazon\.aws\.rds\_cluster\_param\_group \- Manage RDS cluster parameter groups
* amazon\.aws\.rds\_cluster\_param\_group\_info \- Describes the properties of specific RDS cluster parameter group\.
* amazon\.aws\.rds\_engine\_versions\_info \- Describes the properties of specific versions of DB engines\.

<a id="ansible-netcommon-4"></a>
#### ansible\.netcommon

* ansible\.netcommon\.cli\_restore \- Restore device configuration to network devices over network\_cli

<a id="check-point-mgmt-2"></a>
#### check\_point\.mgmt

* check\_point\.mgmt\.cp\_mgmt\_add\_central\_license \- Add central license\.
* check\_point\.mgmt\.cp\_mgmt\_central\_license\_facts \- Get central\-license objects facts on Checkpoint over Web Services API\.
* check\_point\.mgmt\.cp\_mgmt\_delete\_central\_license \- Delete central license\.
* check\_point\.mgmt\.cp\_mgmt\_distribute\_cloud\_licenses \- Distribute licenses to target CloudGuard gateways\.
* check\_point\.mgmt\.cp\_mgmt\_show\_cloud\_licenses\_usage \- Show attached licenses usage\.
* check\_point\.mgmt\.cp\_mgmt\_show\_ha\_status \- Retrieve domain high availability status\.

<a id="cisco-ios-4"></a>
#### cisco\.ios

* cisco\.ios\.ios\_evpn\_evi \- Resource module to configure L2VPN EVPN EVI\.
* cisco\.ios\.ios\_evpn\_global \- Resource module to configure L2VPN EVPN\.
* cisco\.ios\.ios\_vxlan\_vtep \- Resource module to configure VXLAN VTEP interface\.

<a id="community-aws-4"></a>
#### community\.aws

* community\.aws\.dynamodb\_table\_info \- Returns information about a Dynamo DB table

<a id="community-crypto-8"></a>
#### community\.crypto

* community\.crypto\.acme\_ari\_info \- Retrieves ACME Renewal Information \(ARI\) for a certificate\.
* community\.crypto\.acme\_certificate\_deactivate\_authz \- Deactivate all authz for an ACME v2 order\.
* community\.crypto\.acme\_certificate\_renewal\_info \- Determine whether a certificate should be renewed or not\.
* community\.crypto\.x509\_certificate\_convert \- Convert X\.509 certificates

<a id="community-digitalocean-2"></a>
#### community\.digitalocean

* community\.digitalocean\.digital\_ocean\_project\_resource\_info \- Gather information about DigitalOcean Project Resources

<a id="community-docker-17"></a>
#### community\.docker

* community\.docker\.docker\_compose\_v2 \- Manage multi\-container Docker applications with Docker Compose CLI plugin
* community\.docker\.docker\_compose\_v2\_pull \- Pull a Docker compose project
* community\.docker\.docker\_image\_build \- Build Docker images using Docker buildx
* community\.docker\.docker\_image\_export \- Export \(archive\) Docker images
* community\.docker\.docker\_image\_pull \- Pull Docker images from registries
* community\.docker\.docker\_image\_push \- Push Docker images to registries
* community\.docker\.docker\_image\_remove \- Remove Docker images
* community\.docker\.docker\_image\_tag \- Tag Docker images with new names and/or tags

<a id="community-general-28"></a>
#### community\.general

* community\.general\.consul\_acl\_bootstrap \- Bootstrap ACLs in Consul\.
* community\.general\.consul\_auth\_method \- Manipulate Consul auth methods\.
* community\.general\.consul\_binding\_rule \- Manipulate Consul binding rules\.
* community\.general\.consul\_token \- Manipulate Consul tokens\.
* community\.general\.django\_command \- Run Django admin commands\.
* community\.general\.dnf\_config\_manager \- Enable or disable dnf repositories using config\-manager\.
* community\.general\.git\_config\_info \- Read git configuration\.
* community\.general\.gitlab\_group\_access\_token \- Manages GitLab group access tokens\.
* community\.general\.gitlab\_issue \- Create\, update\, or delete GitLab issues\.
* community\.general\.gitlab\_label \- Creates/updates/deletes GitLab Labels belonging to project or group\.
* community\.general\.gitlab\_milestone \- Creates/updates/deletes GitLab Milestones belonging to project or group\.
* community\.general\.gitlab\_project\_access\_token \- Manages GitLab project access tokens\.
* community\.general\.keycloak\_client\_rolescope \- Allows administration of Keycloak client roles scope to restrict the usage of certain roles to a other specific client applications\.
* community\.general\.keycloak\_component\_info \- Retrive component info in Keycloak\.
* community\.general\.keycloak\_realm\_rolemapping \- Allows administration of Keycloak realm role mappings into groups with the Keycloak API\.
* community\.general\.nomad\_token \- Manage Nomad ACL tokens\.
* community\.general\.proxmox\_node\_info \- Retrieve information about one or more Proxmox VE nodes\.
* community\.general\.proxmox\_storage\_contents\_info \- List content from a Proxmox VE storage\.
* community\.general\.usb\_facts \- Allows listing information about USB devices\.

<a id="community-hashi-vault-2"></a>
#### community\.hashi\_vault

* community\.hashi\_vault\.vault\_database\_connection\_configure \- Configures the database engine
* community\.hashi\_vault\.vault\_database\_connection\_delete \- Delete a Database Connection
* community\.hashi\_vault\.vault\_database\_connection\_read \- Returns the configuration settings for a O\(connection\_name\)
* community\.hashi\_vault\.vault\_database\_connection\_reset \- Closes a O\(connection\_name\) and its underlying plugin and restarts it with the configuration stored
* community\.hashi\_vault\.vault\_database\_connections\_list \- Returns a list of available connections
* community\.hashi\_vault\.vault\_database\_role\_create \- Creates or updates a \(dynamic\) role definition
* community\.hashi\_vault\.vault\_database\_role\_delete \- Delete a role definition
* community\.hashi\_vault\.vault\_database\_role\_read \- Queries a dynamic role definition
* community\.hashi\_vault\.vault\_database\_roles\_list \- Returns a list of available \(dynamic\) roles
* community\.hashi\_vault\.vault\_database\_rotate\_root\_credentials \- Rotates the root credentials stored for the database connection\. This user must have permissions to update its own password\.
* community\.hashi\_vault\.vault\_database\_static\_role\_create \- Create or update a static role
* community\.hashi\_vault\.vault\_database\_static\_role\_get\_credentials \- Returns the current credentials based on the named static role
* community\.hashi\_vault\.vault\_database\_static\_role\_read \- Queries a static role definition
* community\.hashi\_vault\.vault\_database\_static\_role\_rotate\_credentials \- Trigger the credential rotation for a static role
* community\.hashi\_vault\.vault\_database\_static\_roles\_list \- Returns a list of available static roles

<a id="community-zabbix-4"></a>
#### community\.zabbix

* community\.zabbix\.zabbix\_correlation \- Create/update/delete Zabbix correlation

<a id="containers-podman-13"></a>
#### containers\.podman

* containers\.podman\.podman\_secret\_info \- Secrets info module

<a id="dellemc-enterprise-sonic-6"></a>
#### dellemc\.enterprise\_sonic

* dellemc\.enterprise\_sonic\.sonic\_dhcp\_snooping \- Manage DHCP Snooping on SONiC
* dellemc\.enterprise\_sonic\.sonic\_pki \- Manages PKI attributes of Enterprise Sonic
* dellemc\.enterprise\_sonic\.sonic\_stp \- Manage STP configuration on SONiC

<a id="dellemc-openmanage-28"></a>
#### dellemc\.openmanage

* dellemc\.openmanage\.idrac\_diagnostics \- This module allows to run and export diagnostics on iDRAC\.
* dellemc\.openmanage\.idrac\_license \- This module allows to import\, export\, and delete licenses on iDRAC\.
* dellemc\.openmanage\.idrac\_session \- Allows you to create and delete the sessions on iDRAC\.
* dellemc\.openmanage\.idrac\_storage\_volume \- Configures the RAID configuration attributes\.

<a id="dellemc-powerflex-2"></a>
#### dellemc\.powerflex

* dellemc\.powerflex\.fault\_set \- Manage Fault Sets on Dell PowerFlex
* dellemc\.powerflex\.resource\_group \- Manage resource group deployments on Dell PowerFlex

<a id="fortinet-fortimanager-11"></a>
#### fortinet\.fortimanager

* fortinet\.fortimanager\.fmgr\_diameterfilter\_profile \- Configure Diameter filter profiles\.
* fortinet\.fortimanager\.fmgr\_firewall\_accessproxysshclientcert \- Configure Access Proxy SSH client certificate\.
* fortinet\.fortimanager\.fmgr\_firewall\_accessproxysshclientcert\_certextension \- Configure certificate extension for user certificate\.
* fortinet\.fortimanager\.fmgr\_firewall\_vip6\_quic \- QUIC setting\.
* fortinet\.fortimanager\.fmgr\_firewall\_vip\_gslbpublicips \- Publicly accessible IP addresses for the FortiGSLB service\.
* fortinet\.fortimanager\.fmgr\_sctpfilter\_profile \- Configure SCTP filter profiles\.
* fortinet\.fortimanager\.fmgr\_sctpfilter\_profile\_ppidfilters \- PPID filters list\.
* fortinet\.fortimanager\.fmgr\_switchcontroller\_managedswitch\_vlan \- Configure VLAN assignment priority\.
* fortinet\.fortimanager\.fmgr\_system\_admin\_profile\_writepasswdprofiles \- Profile list\.
* fortinet\.fortimanager\.fmgr\_system\_admin\_profile\_writepasswduserlist \- User list\.
* fortinet\.fortimanager\.fmgr\_system\_npu\_nputcam \- Configure NPU TCAM policies\.
* fortinet\.fortimanager\.fmgr\_system\_npu\_nputcam\_data \- Data fields of TCAM\.
* fortinet\.fortimanager\.fmgr\_system\_npu\_nputcam\_mask \- Mask fields of TCAM\.
* fortinet\.fortimanager\.fmgr\_system\_npu\_nputcam\_miract \- Mirror action of TCAM\.
* fortinet\.fortimanager\.fmgr\_system\_npu\_nputcam\_priact \- Priority action of TCAM\.
* fortinet\.fortimanager\.fmgr\_system\_npu\_nputcam\_sact \- Source action of TCAM\.
* fortinet\.fortimanager\.fmgr\_system\_npu\_nputcam\_tact \- Target action of TCAM\.
* fortinet\.fortimanager\.fmgr\_videofilter\_keyword \- Configure video filter keywords\.
* fortinet\.fortimanager\.fmgr\_videofilter\_keyword\_word \- List of keywords\.
* fortinet\.fortimanager\.fmgr\_videofilter\_profile\_filters \- YouTube filter entries\.
* fortinet\.fortimanager\.fmgr\_videofilter\_youtubekey \- Configure YouTube API keys\.

<a id="hetzner-hcloud-3"></a>
#### hetzner\.hcloud

* hetzner\.hcloud\.firewall\_resource \- Manage Resources a Hetzner Cloud Firewall is applied to\.

<a id="infoblox-nios-modules-7"></a>
#### infoblox\.nios\_modules

* infoblox\.nios\_modules\.nios\_dtc\_monitor\_http \- Configures the Infoblox NIOS DTC HTTP monitor\.
* infoblox\.nios\_modules\.nios\_dtc\_monitor\_icmp \- Configures the Infoblox NIOS DTC ICMP monitor
* infoblox\.nios\_modules\.nios\_dtc\_monitor\_pdp \- Configures the Infoblox NIOS DTC PDP monitor
* infoblox\.nios\_modules\.nios\_dtc\_monitor\_sip \- Configures the Infoblox NIOS DTC SIP monitor
* infoblox\.nios\_modules\.nios\_dtc\_monitor\_snmp \- Configures the Infoblox NIOS DTC SNMP monitor
* infoblox\.nios\_modules\.nios\_dtc\_monitor\_tcp \- Configures the Infoblox NIOS DTC TCP monitor
* infoblox\.nios\_modules\.nios\_dtc\_topology \- Configures the Infoblox NIOS DTC Topology

<a id="netapp-ontap-7"></a>
#### netapp\.ontap

* netapp\.ontap\.na\_ontap\_cifs\_unix\_symlink\_mapping \- NetApp ONTAP module to manage UNIX symbolic link mapping for CIFS clients\.
* netapp\.ontap\.na\_ontap\_cli\_timeout \- NetApp ONTAP module to set the CLI inactivity timeout value\.
* netapp\.ontap\.na\_ontap\_snmp\_config \- NetApp ONTAP module to modify SNMP configuration\.

<a id="netbox-netbox-7"></a>
#### netbox\.netbox

* netbox\.netbox\.netbox\_custom\_field\_choice\_set \- Create\, updates\, or removes Custom Field Choice sets
* netbox\.netbox\.netbox\_module\_bay \- Create\, updates\, or removes Module Bay
* netbox\.netbox\.netbox\_virtual\_disk \- Create\, updates\, or removes a disk from a Virtual Machine

<a id="purestorage-flasharray-12"></a>
#### purestorage\.flasharray

* purestorage\.flasharray\.purefa\_hardware \- Manage FlashArray Hardware Identification

<a id="purestorage-flashblade-7"></a>
#### purestorage\.flashblade

* purestorage\.flashblade\.purefb\_hardware \- Manage FlashBlade Hardware

<a id="theforeman-foreman-7"></a>
#### theforeman\.foreman

* theforeman\.foreman\.registration\_command \- Manage Registration Command
* theforeman\.foreman\.webhook \- Manage Webhooks

<a id="vultr-cloud-3"></a>
#### vultr\.cloud

* vultr\.cloud\.object\_storage \- Manages object storages on Vultr

<a id="new-roles"></a>
### New Roles

* dellemc\.openmanage\.idrac\_user \- Role to manage local users of iDRAC\.

<a id="unchanged-collections-8"></a>
### Unchanged Collections

* ansible\.posix \(still version 1\.5\.4\)
* chocolatey\.chocolatey \(still version 1\.5\.1\)
* cisco\.ucs \(still version 1\.10\.0\)
* cloudscale\_ch\.cloud \(still version 2\.3\.1\)
* community\.libvirt \(still version 1\.3\.0\)
* community\.network \(still version 5\.0\.2\)
* community\.proxysql \(still version 1\.5\.1\)
* community\.sops \(still version 1\.6\.7\)
* cyberark\.conjur \(still version 1\.2\.2\)
* frr\.frr \(still version 2\.0\.2\)
* ibm\.spectrum\_virtualize \(still version 2\.0\.0\)
* inspur\.sm \(still version 2\.3\.0\)
* netapp\.cloudmanager \(still version 21\.22\.1\)
* netapp\_eseries\.santricity \(still version 1\.4\.0\)
* ngine\_io\.cloudstack \(still version 2\.3\.0\)
* ngine\_io\.exoscale \(still version 1\.1\.0\)
* openvswitch\.openvswitch \(still version 2\.1\.1\)
* ovirt\.ovirt \(still version 3\.2\.0\)
* sensu\.sensu\_go \(still version 1\.14\.0\)
* t\_systems\_mms\.icinga\_director \(still version 2\.0\.1\)
* vyos\.vyos \(still version 4\.1\.0\)
* wti\.remote \(still version 1\.0\.5\)
