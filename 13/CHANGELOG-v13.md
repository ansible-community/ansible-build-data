# Ansible 13 Release Notes

This changelog describes changes since Ansible 12\.0\.0\.

- <a href="#v13-6-0">v13\.6\.0</a>
    - <a href="#release-summary">Release Summary</a>
    - <a href="#ansible-core">Ansible\-core</a>
    - <a href="#changed-collections">Changed Collections</a>
    - <a href="#major-changes">Major Changes</a>
    - <a href="#minor-changes">Minor Changes</a>
    - <a href="#deprecated-features">Deprecated Features</a>
    - <a href="#bugfixes">Bugfixes</a>
    - <a href="#known-issues">Known Issues</a>
    - <a href="#new-plugins">New Plugins</a>
    - <a href="#new-modules">New Modules</a>
    - <a href="#unchanged-collections">Unchanged Collections</a>
- <a href="#v13-5-0">v13\.5\.0</a>
    - <a href="#release-summary-1">Release Summary</a>
    - <a href="#added-collections">Added Collections</a>
    - <a href="#ansible-core-3">Ansible\-core</a>
    - <a href="#changed-collections-1">Changed Collections</a>
    - <a href="#major-changes-1">Major Changes</a>
    - <a href="#minor-changes-1">Minor Changes</a>
    - <a href="#breaking-changes--porting-guide">Breaking Changes / Porting Guide</a>
    - <a href="#deprecated-features-1">Deprecated Features</a>
    - <a href="#security-fixes">Security Fixes</a>
    - <a href="#bugfixes-1">Bugfixes</a>
    - <a href="#known-issues-1">Known Issues</a>
    - <a href="#new-modules-1">New Modules</a>
    - <a href="#unchanged-collections-1">Unchanged Collections</a>
- <a href="#v13-4-0">v13\.4\.0</a>
    - <a href="#release-summary-2">Release Summary</a>
    - <a href="#ansible-core-6">Ansible\-core</a>
    - <a href="#changed-collections-2">Changed Collections</a>
    - <a href="#major-changes-2">Major Changes</a>
    - <a href="#minor-changes-2">Minor Changes</a>
    - <a href="#deprecated-features-2">Deprecated Features</a>
    - <a href="#security-fixes-1">Security Fixes</a>
    - <a href="#bugfixes-2">Bugfixes</a>
    - <a href="#new-plugins-1">New Plugins</a>
    - <a href="#new-modules-2">New Modules</a>
    - <a href="#unchanged-collections-2">Unchanged Collections</a>
- <a href="#v13-3-0">v13\.3\.0</a>
    - <a href="#release-summary-3">Release Summary</a>
    - <a href="#added-collections-1">Added Collections</a>
    - <a href="#ansible-core-9">Ansible\-core</a>
    - <a href="#changed-collections-3">Changed Collections</a>
    - <a href="#major-changes-3">Major Changes</a>
    - <a href="#minor-changes-3">Minor Changes</a>
    - <a href="#deprecated-features-3">Deprecated Features</a>
    - <a href="#bugfixes-3">Bugfixes</a>
    - <a href="#new-plugins-2">New Plugins</a>
    - <a href="#new-modules-3">New Modules</a>
    - <a href="#unchanged-collections-3">Unchanged Collections</a>
- <a href="#v13-2-0">v13\.2\.0</a>
    - <a href="#release-summary-4">Release Summary</a>
    - <a href="#ansible-core-12">Ansible\-core</a>
    - <a href="#changed-collections-4">Changed Collections</a>
    - <a href="#major-changes-4">Major Changes</a>
    - <a href="#minor-changes-4">Minor Changes</a>
    - <a href="#deprecated-features-4">Deprecated Features</a>
    - <a href="#bugfixes-4">Bugfixes</a>
    - <a href="#new-modules-4">New Modules</a>
    - <a href="#unchanged-collections-4">Unchanged Collections</a>
- <a href="#v13-1-0">v13\.1\.0</a>
    - <a href="#release-summary-5">Release Summary</a>
    - <a href="#ansible-core-13">Ansible\-core</a>
    - <a href="#changed-collections-5">Changed Collections</a>
    - <a href="#major-changes-5">Major Changes</a>
    - <a href="#minor-changes-5">Minor Changes</a>
    - <a href="#deprecated-features-5">Deprecated Features</a>
    - <a href="#bugfixes-5">Bugfixes</a>
    - <a href="#known-issues-2">Known Issues</a>
    - <a href="#new-modules-5">New Modules</a>
    - <a href="#unchanged-collections-5">Unchanged Collections</a>
- <a href="#v13-0-0">v13\.0\.0</a>
    - <a href="#release-summary-6">Release Summary</a>
    - <a href="#removed-collections">Removed Collections</a>
    - <a href="#added-collections-2">Added Collections</a>
    - <a href="#ansible-core-15">Ansible\-core</a>
    - <a href="#included-collections">Included Collections</a>
    - <a href="#major-changes-6">Major Changes</a>
    - <a href="#minor-changes-6">Minor Changes</a>
    - <a href="#breaking-changes--porting-guide-1">Breaking Changes / Porting Guide</a>
    - <a href="#deprecated-features-6">Deprecated Features</a>
    - <a href="#removed-features-previously-deprecated">Removed Features \(previously deprecated\)</a>
    - <a href="#security-fixes-2">Security Fixes</a>
    - <a href="#bugfixes-6">Bugfixes</a>
    - <a href="#known-issues-3">Known Issues</a>
    - <a href="#new-plugins-3">New Plugins</a>
    - <a href="#new-modules-6">New Modules</a>
    - <a href="#unchanged-collections-6">Unchanged Collections</a>

<a id="v13-6-0"></a>
## v13\.6\.0

- <a href="#release-summary">Release Summary</a>
- <a href="#ansible-core">Ansible\-core</a>
- <a href="#changed-collections">Changed Collections</a>
- <a href="#major-changes">Major Changes</a>
    - <a href="#chocolatey-chocolatey">chocolatey\.chocolatey</a>
    - <a href="#fortinet-fortios">fortinet\.fortios</a>
- <a href="#minor-changes">Minor Changes</a>
    - <a href="#ansible-core-1">Ansible\-core</a>
    - <a href="#ansible-netcommon">ansible\.netcommon</a>
    - <a href="#cisco-iosxr">cisco\.iosxr</a>
    - <a href="#community-crypto">community\.crypto</a>
    - <a href="#community-docker">community\.docker</a>
    - <a href="#community-general">community\.general</a>
    - <a href="#community-libvirt">community\.libvirt</a>
    - <a href="#community-routeros">community\.routeros</a>
    - <a href="#community-sops">community\.sops</a>
    - <a href="#community-zabbix">community\.zabbix</a>
    - <a href="#containers-podman">containers\.podman</a>
    - <a href="#dellemc-openmanage">dellemc\.openmanage</a>
    - <a href="#google-cloud">google\.cloud</a>
    - <a href="#graphiant-naas">graphiant\.naas</a>
    - <a href="#ibm-storage-virtualize">ibm\.storage\_virtualize</a>
    - <a href="#lowlydba-sqlserver">lowlydba\.sqlserver</a>
    - <a href="#theforeman-foreman">theforeman\.foreman</a>
- <a href="#deprecated-features">Deprecated Features</a>
    - <a href="#ansible-netcommon-1">ansible\.netcommon</a>
    - <a href="#community-routeros-1">community\.routeros</a>
- <a href="#bugfixes">Bugfixes</a>
    - <a href="#ansible-core-2">Ansible\-core</a>
    - <a href="#ansible-netcommon-2">ansible\.netcommon</a>
    - <a href="#ansible-utils">ansible\.utils</a>
    - <a href="#cisco-iosxr-1">cisco\.iosxr</a>
    - <a href="#cisco-meraki">cisco\.meraki</a>
    - <a href="#community-crypto-1">community\.crypto</a>
    - <a href="#community-dns">community\.dns</a>
    - <a href="#community-general-1">community\.general</a>
    - <a href="#community-libvirt-1">community\.libvirt</a>
    - <a href="#community-zabbix-1">community\.zabbix</a>
    - <a href="#containers-podman-1">containers\.podman</a>
    - <a href="#dellemc-openmanage-1">dellemc\.openmanage</a>
    - <a href="#fortinet-fortios-1">fortinet\.fortios</a>
    - <a href="#ibm-storage-virtualize-1">ibm\.storage\_virtualize</a>
- <a href="#known-issues">Known Issues</a>
    - <a href="#dellemc-openmanage-2">dellemc\.openmanage</a>
- <a href="#new-plugins">New Plugins</a>
    - <a href="#filter">Filter</a>
- <a href="#new-modules">New Modules</a>
    - <a href="#community-general-2">community\.general</a>
- <a href="#unchanged-collections">Unchanged Collections</a>

<a id="release-summary"></a>
### Release Summary

Release Date\: 2026\-04\-21

[Porting Guide](https\://docs\.ansible\.com/projects/ansible/devel/porting\_guides\.html)

<a id="ansible-core"></a>
### Ansible\-core

Ansible 13\.6\.0 contains ansible\-core version 2\.20\.5\.
This is a newer version than version 2\.20\.4 contained in the previous Ansible release\.

The changes are reported in the combined changelog below\.

<a id="changed-collections"></a>
### Changed Collections

If not mentioned explicitly\, the changes are reported in the combined changelog below\.

| Collection             | Ansible 13.5.0 | Ansible 13.6.0 | Notes                                                                                                                        |
| ---------------------- | -------------- | -------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| ansible.netcommon      | 8.4.0          | 8.5.0          |                                                                                                                              |
| ansible.utils          | 6.0.1          | 6.0.2          |                                                                                                                              |
| chocolatey.chocolatey  | 1.5.3          | 1.6.0          |                                                                                                                              |
| cisco.intersight       | 2.16.0         | 2.18.0         | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
| cisco.iosxr            | 12.1.1         | 12.2.1         |                                                                                                                              |
| cisco.meraki           | 2.23.1         | 2.23.2         |                                                                                                                              |
| community.crypto       | 3.1.1          | 3.2.0          |                                                                                                                              |
| community.dns          | 3.5.3          | 3.5.4          |                                                                                                                              |
| community.docker       | 5.1.0          | 5.2.0          |                                                                                                                              |
| community.general      | 12.5.0         | 12.6.0         |                                                                                                                              |
| community.libvirt      | 2.1.0          | 2.2.0          |                                                                                                                              |
| community.routeros     | 3.18.0         | 3.20.0         |                                                                                                                              |
| community.sops         | 2.2.7          | 2.3.0          |                                                                                                                              |
| community.zabbix       | 4.1.1          | 4.2.0          |                                                                                                                              |
| containers.podman      | 1.19.0         | 1.19.2         |                                                                                                                              |
| dellemc.openmanage     | 10.0.1         | 10.0.2         |                                                                                                                              |
| fortinet.fortios       | 2.5.0          | 2.5.1          |                                                                                                                              |
| google.cloud           | 1.12.0         | 1.13.0         |                                                                                                                              |
| graphiant.naas         | 26.2.4         | 26.3.0         |                                                                                                                              |
| ibm.storage_virtualize | 3.2.0          | 3.3.0          |                                                                                                                              |
| lowlydba.sqlserver     | 2.7.0          | 2.8.1          |                                                                                                                              |
| theforeman.foreman     | 5.10.0         | 5.11.0         |                                                                                                                              |

<a id="major-changes"></a>
### Major Changes

<a id="chocolatey-chocolatey"></a>
#### chocolatey\.chocolatey

* win\_chocolatey \- add option to ignore pinned status of pinned packages

<a id="fortinet-fortios"></a>
#### fortinet\.fortios

* Added a generic <em class="title-reference">headers</em> parameter to <em class="title-reference">fortios\_json\_generic</em> to support admin\-password confirmation headers and future custom request headers\.
* Updated FAQ to illustrate the use of <em class="title-reference">headers</em> in <em class="title-reference">fortios\_json\_generic</em> module\.
* Updated deprecated import of to\_text from ansible\.module\_utils\.\_text to the supported implementation\.

<a id="minor-changes"></a>
### Minor Changes

<a id="ansible-core-1"></a>
#### Ansible\-core

* ansible\-test \- Generate <code>dist\_info</code> when running tests\.
* ansible\-test \- Replace the <code>parallels</code> managed macOS provider with a new <code>mac</code> provider\.
* ansible\-test \- Switch managed macOS remotes from x86\_64 to aarch64\.

<a id="ansible-netcommon"></a>
#### ansible\.netcommon

* The dependency on ansible\-pylibssh \(for ssh\_type\=libssh / network\_cli\) is now ansible\-pylibssh\>\=1\.4\.0 in requirements\.txt\, raised from the previous \>\=0\.2\.0 requirement\. Installations still on ansible\-pylibssh 0\.x or 1\.x below 1\.4\.0 must upgrade to use the libssh connection path with this collection release\.
* libssh connection \- When log\_path is set \(e\.g\. via ANSIBLE\_LOG\_PATH or log\_path in ansible\.cfg\)\, the plugin now routes ansible\-pylibssh \(libssh\) logs into the same Ansible log file\. Log level is derived from display\.verbosity using Python standard logging\: verbosity 0 \-\> WARNING\, 1\-2 \-\> INFO\, 3\+ \-\> DEBUG\. This allows SSH/libssh debug and trace output to appear in the configured log file for troubleshooting without changing ansible\-pylibssh configuration manually\.
* network\_cli \- The in\-collection paramiko path supports the same host key policy behavior \(including host\_key\_auto\_add and known\_hosts handling\) and persistent connection caching as the previous ansible\-core paramiko integration\.
* network\_cli \- When ssh\_type is set to paramiko\, the connection plugin now uses an in\-collection paramiko implementation instead of loading ansible\-core\'s paramiko connection plugin\. This allows network\_cli to work with versions of ansible\-core\, where the paramiko connection plugin was removed\.

<a id="cisco-iosxr"></a>
#### cisco\.iosxr

* iosxr\_l3\_interfaces \- Added support for <em class="title-reference">flow\.ipv4\.direction</em> and <em class="title-reference">flow\.ipv6\.direction</em> value <em class="title-reference">bidirectional</em>\. The module now expands bidirectional flow configuration into both ingress and egress IOS\-XR flow monitor commands\.

<a id="community-crypto"></a>
#### community\.crypto

* acme\_\* modules \- experimentally support <code>dns\-account\-01</code> challenge type according to [acme\-dns\-account\-label draft 02](https\://datatracker\.ietf\.org/doc/html/draft\-ietf\-acme\-dns\-account\-label\-02)\. Note that breaking changes to this challenge type can also happen in minor releases until the acme\-dns\-account\-label draft has been finalized as an RFC \([https\://github\.com/ansible\-collections/community\.crypto/pull/996](https\://github\.com/ansible\-collections/community\.crypto/pull/996)\)\.
* acme\_\* modules \- experimentally support <code>dns\-persist\-01</code> challenge type according to [acme\-dns\-persist draft 01](https\://www\.ietf\.org/archive/id/draft\-ietf\-acme\-dns\-persist\-01\.html)\. Note that breaking changes to this challenge type can also happen in minor releases until the acme\-dns\-persist draft has been finalized as an RFC \([https\://github\.com/ansible\-collections/community\.crypto/pull/997](https\://github\.com/ansible\-collections/community\.crypto/pull/997)\)\.

<a id="community-docker"></a>
#### community\.docker

* docker\_image\_export \- adds <code>platform</code> parameter to allow exporting a specific platform variant from a multi\-arch image \([https\://github\.com/ansible\-collections/community\.docker/issues/1064](https\://github\.com/ansible\-collections/community\.docker/issues/1064)\, [https\://github\.com/ansible\-collections/community\.docker/pull/1251](https\://github\.com/ansible\-collections/community\.docker/pull/1251)\)\.

<a id="community-general"></a>
#### community\.general

* cobbler\_sync \- minor code cleanup \([https\://github\.com/ansible\-collections/community\.general/pull/11879](https\://github\.com/ansible\-collections/community\.general/pull/11879)\)\.
* cobbler\_system \- minor code cleanup \([https\://github\.com/ansible\-collections/community\.general/pull/11879](https\://github\.com/ansible\-collections/community\.general/pull/11879)\)\.
* composer \- add <code>force</code> parameter\; when <code>command\=create\-project</code>\, the module now checks whether a <code>composer\.json</code> already exists in <code>working\_dir</code> and skips the command if so\, making the task idempotent\. Set <code>force\=true</code> to always run the command regardless \([https\://github\.com/ansible\-collections/community\.general/issues/725](https\://github\.com/ansible\-collections/community\.general/issues/725)\, [https\://github\.com/ansible\-collections/community\.general/pull/11689](https\://github\.com/ansible\-collections/community\.general/pull/11689)\)\.
* consul\_kv \- add <code>ca\_path</code> option to specify a CA bundle for HTTPS connections \([https\://github\.com/ansible\-collections/community\.general/pull/11817](https\://github\.com/ansible\-collections/community\.general/pull/11817)\)\.
* consul\_kv lookup plugin \- add <code>ca\_path</code> option to specify a CA bundle for HTTPS connections \([https\://github\.com/ansible\-collections/community\.general/issues/2876](https\://github\.com/ansible\-collections/community\.general/issues/2876)\, [https\://github\.com/ansible\-collections/community\.general/pull/11817](https\://github\.com/ansible\-collections/community\.general/pull/11817)\)\.
* dconf \- add support for C\(dbus\-broker\) \([https\://github\.com/ansible\-collections/community\.general/issues/495](https\://github\.com/ansible\-collections/community\.general/issues/495)\, [https\://github\.com/ansible\-collections/community\.general/pull/11772](https\://github\.com/ansible\-collections/community\.general/pull/11772)\)\.
* filesystem \- migrate <code>LVM\.get\_fs\_size\(\)</code> to use <code>CmdRunner</code>\, ensuring locale\-independent output parsing \([https\://github\.com/ansible\-collections/community\.general/pull/11888](https\://github\.com/ansible\-collections/community\.general/pull/11888)\)\.
* flatpak \- add new parameter <code>from\_url</code> to install a flatpak from a <code>\.flatpakref</code> URL \([https\://github\.com/ansible\-collections/community\.general/issues/4000](https\://github\.com/ansible\-collections/community\.general/issues/4000)\, [https\://github\.com/ansible\-collections/community\.general/pull/11748](https\://github\.com/ansible\-collections/community\.general/pull/11748)\)\.
* gem \- refactor module to use <code>CmdRunner</code> \([https\://github\.com/ansible\-collections/community\.general/pull/11733](https\://github\.com/ansible\-collections/community\.general/pull/11733)\)\.
* homebrew\_services \- remove various redundancies including dead state validation\, unused return values\, and unnecessary locale environment variables \([https\://github\.com/ansible\-collections/community\.general/pull/11839](https\://github\.com/ansible\-collections/community\.general/pull/11839)\)\.
* homebrew\_tap \- avoid redundant <code>brew tap</code> calls when processing multiple taps by fetching the tap list once upfront \([https\://github\.com/ansible\-collections/community\.general/pull/11848](https\://github\.com/ansible\-collections/community\.general/pull/11848)\)\.
* ipa\_dnsrecord \- add <code>exclusive</code> parameter to allow appending values to existing records without replacing them \([https\://github\.com/ansible\-collections/community\.general/issues/682](https\://github\.com/ansible\-collections/community\.general/issues/682)\, [https\://github\.com/ansible\-collections/community\.general/pull/11694](https\://github\.com/ansible\-collections/community\.general/pull/11694)\)\.
* java\_cert \- support proxy authentication when <code>https\_proxy</code> environment variable includes credentials \([https\://github\.com/ansible\-collections/community\.general/issues/4126](https\://github\.com/ansible\-collections/community\.general/issues/4126)\, [https\://github\.com/ansible\-collections/community\.general/pull/11753](https\://github\.com/ansible\-collections/community\.general/pull/11753)\)\.
* jira \- add <code>cloud</code> option to support Jira Cloud\'s new search endpoint <code>/rest/api/2/search/jql</code>\, since the legacy <code>/rest/api/2/search</code> endpoint has been removed on Jira Cloud \([https\://github\.com/ansible\-collections/community\.general/issues/10786](https\://github\.com/ansible\-collections/community\.general/issues/10786)\, [https\://github\.com/ansible\-collections/community\.general/pull/11701](https\://github\.com/ansible\-collections/community\.general/pull/11701)\)\.
* jira \- when <code>cloud\=true</code>\, user\-type fields \(<code>assignee</code>\, <code>reporter</code>\, and any listed in the new <code>custom\_user\_fields</code> parameter\) containing an email address are automatically resolved to Jira Cloud account IDs \([https\://github\.com/ansible\-collections/community\.general/issues/11734](https\://github\.com/ansible\-collections/community\.general/issues/11734)\, [https\://github\.com/ansible\-collections/community\.general/pull/11735](https\://github\.com/ansible\-collections/community\.general/pull/11735)\)\.
* logrotate \- adds optional <code>backup</code> parameter to create a backup of the existing configuration file before writing changes \([https\://github\.com/ansible\-collections/community\.general/pull/11764](https\://github\.com/ansible\-collections/community\.general/pull/11764)\)\.
* lvg \- migrate to <code>CmdRunner</code>\, removing direct <code>run\_command</code> calls and <code>run\_command\_environ\_update</code> \([https\://github\.com/ansible\-collections/community\.general/pull/11835](https\://github\.com/ansible\-collections/community\.general/pull/11835)\)\.
* lvm\_pv \- migrate to <code>CmdRunner</code> using shared runners from <code>module\_utils/\_lvm</code> \([https\://github\.com/ansible\-collections/community\.general/pull/11811](https\://github\.com/ansible\-collections/community\.general/pull/11811)\)\.
* lvol \- migrate to <code>CmdRunner</code> \([https\://github\.com/ansible\-collections/community\.general/pull/11887](https\://github\.com/ansible\-collections/community\.general/pull/11887)\)\.
* manageiq module utils \- minor code cleanup \([https\://github\.com/ansible\-collections/community\.general/pull/11879](https\://github\.com/ansible\-collections/community\.general/pull/11879)\)\.
* manageiq\_alert\_profiles \- minor code cleanup \([https\://github\.com/ansible\-collections/community\.general/pull/11879](https\://github\.com/ansible\-collections/community\.general/pull/11879)\)\.
* manageiq\_alerts \- minor code cleanup \([https\://github\.com/ansible\-collections/community\.general/pull/11879](https\://github\.com/ansible\-collections/community\.general/pull/11879)\)\.
* oneview module utils \- minor code cleanup \([https\://github\.com/ansible\-collections/community\.general/pull/11879](https\://github\.com/ansible\-collections/community\.general/pull/11879)\)\.
* oneview\_san\_manager \- minor code cleanup \([https\://github\.com/ansible\-collections/community\.general/pull/11879](https\://github\.com/ansible\-collections/community\.general/pull/11879)\)\.
* opendj\_backendprop \- refactor to use <code>CmdRunner</code> \([https\://github\.com/ansible\-collections/community\.general/pull/11728](https\://github\.com/ansible\-collections/community\.general/pull/11728)\)\.
* packet\_device \- minor code cleanup \([https\://github\.com/ansible\-collections/community\.general/pull/11879](https\://github\.com/ansible\-collections/community\.general/pull/11879)\)\.
* packet\_ip\_subnet \- minor code cleanup \([https\://github\.com/ansible\-collections/community\.general/pull/11879](https\://github\.com/ansible\-collections/community\.general/pull/11879)\)\.
* pacman \- add <code>root</code>\, <code>cachedir</code>\, and <code>config</code> options to support installing packages into an alternative root directory \([https\://github\.com/ansible\-collections/community\.general/issues/438](https\://github\.com/ansible\-collections/community\.general/issues/438)\, [https\://github\.com/ansible\-collections/community\.general/pull/11681](https\://github\.com/ansible\-collections/community\.general/pull/11681)\)\.
* parted \- add <code>unit\_preserve\_case</code> option to control the case of the <code>unit</code> field in the return value\, fixing the round\-trip use case where the returned unit is fed back as input \([https\://github\.com/ansible\-collections/community\.general/issues/1860](https\://github\.com/ansible\-collections/community\.general/issues/1860)\, [https\://github\.com/ansible\-collections/community\.general/pull/11813](https\://github\.com/ansible\-collections/community\.general/pull/11813)\)\.
* pubnub\_blocks \- minor code cleanup \([https\://github\.com/ansible\-collections/community\.general/pull/11879](https\://github\.com/ansible\-collections/community\.general/pull/11879)\)\.
* terraform \- minor code cleanup \([https\://github\.com/ansible\-collections/community\.general/pull/11879](https\://github\.com/ansible\-collections/community\.general/pull/11879)\)\.
* xenserver\_guest \- use <code>enumerate\(\)</code> instead of manual index variable in <code>for</code> loop \([https\://github\.com/ansible\-collections/community\.general/pull/11721](https\://github\.com/ansible\-collections/community\.general/pull/11721)\)\.

<a id="community-libvirt"></a>
#### community\.libvirt

* virt\_cloud\_instance \- added commands return field to provide visibility into executed commands during VM provisioning\.
* virt\_install \- added commands return field to provide visibility into executed commands during VM provisioning\.

<a id="community-routeros"></a>
#### community\.routeros

* api\_info \- add missing <code>numbers</code> parameter across numerous existing paths for RouterOS \>\= 7\.15\.2 \([https\://github\.com/ansible\-collections/community\.routeros/pull/458](https\://github\.com/ansible\-collections/community\.routeros/pull/458)\)\.
* api\_info \- add support for the <code>interface dot1x server active</code>\, <code>ip hotspot active</code>\, <code>ip ipsec active\-peers</code>\, <code>ip proxy cache\-contents</code>\, <code>ip socks connections</code>\, <code>user active</code>\, and <code>user\-manager session</code> paths as info\-only \(read\-only\) paths \([https\://github\.com/ansible\-collections/community\.routeros/pull/458](https\://github\.com/ansible\-collections/community\.routeros/pull/458)\)\.
* api\_info \- adds support for additional read\-only parameters in the <code>app</code> path for RouterOS \>\= 7\.22 \([https\://github\.com/ansible\-collections/community\.routeros/pull/457](https\://github\.com/ansible\-collections/community\.routeros/pull/457)\)\.
* api\_info\, api\_modify \- add 46 new parameters to the <code>interface ethernet switch port</code> path for RouterOS \>\= 7\.15 \(CRS1xx/2xx variant\) including QoS\, mirroring\, VLAN\, and learning control parameters \([https\://github\.com/ansible\-collections/community\.routeros/pull/463](https\://github\.com/ansible\-collections/community\.routeros/pull/463)\)\.
* api\_info\, api\_modify \- add <code>color</code> parameter to the <code>zerotier interface</code> path for RouterOS \>\= 7\.22\.1 \([https\://github\.com/ansible\-collections/community\.routeros/pull/459](https\://github\.com/ansible\-collections/community\.routeros/pull/459)\)\.
* api\_info\, api\_modify \- add <code>comment</code>\, <code>disabled</code>\, <code>independent\-learning</code>\, <code>qos\-group</code>\, <code>svl</code>\, and <code>switch</code> parameters to the <code>interface ethernet switch vlan</code> path for RouterOS \>\= 7\.15 \(CRS1xx/2xx variant\) \([https\://github\.com/ansible\-collections/community\.routeros/pull/463](https\://github\.com/ansible\-collections/community\.routeros/pull/463)\)\.
* api\_info\, api\_modify \- add <code>current\-defaults</code> parameter to the <code>ip dns</code> path for RouterOS \>\= 7\.22\.1 \([https\://github\.com/ansible\-collections/community\.routeros/pull/459](https\://github\.com/ansible\-collections/community\.routeros/pull/459)\)\.
* api\_info\, api\_modify \- add <code>mld\-datapath</code> parameter to the <code>interface wifi cap</code> path for RouterOS \>\= 7\.22\.1 \([https\://github\.com/ansible\-collections/community\.routeros/pull/459](https\://github\.com/ansible\-collections/community\.routeros/pull/459)\)\.
* api\_info\, api\_modify \- add <code>switch\-all\-ports</code> parameter in the <code>interface ethernet switch</code> path for RouterOS \>\= 7\.22 \([https\://github\.com/ansible\-collections/community\.routeros/pull/463](https\://github\.com/ansible\-collections/community\.routeros/pull/463)\)\.
* api\_info\, api\_modify \- add support for <code>interface ethernet switch acl policer</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/463](https\://github\.com/ansible\-collections/community\.routeros/pull/463)\)\.
* api\_info\, api\_modify \- add support for <code>interface ethernet switch acl</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/463](https\://github\.com/ansible\-collections/community\.routeros/pull/463)\)\.
* api\_info\, api\_modify \- add support for <code>interface ethernet switch dscp\-qos\-map</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/463](https\://github\.com/ansible\-collections/community\.routeros/pull/463)\)\.
* api\_info\, api\_modify \- add support for <code>interface ethernet switch dscp\-to\-dscp</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/463](https\://github\.com/ansible\-collections/community\.routeros/pull/463)\)\.
* api\_info\, api\_modify \- add support for <code>interface ethernet switch egress\-vlan\-tag</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/463](https\://github\.com/ansible\-collections/community\.routeros/pull/463)\)\.
* api\_info\, api\_modify \- add support for <code>interface ethernet switch egress\-vlan\-translation</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/463](https\://github\.com/ansible\-collections/community\.routeros/pull/463)\)\.
* api\_info\, api\_modify \- add support for <code>interface ethernet switch ingress\-port\-policer</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/463](https\://github\.com/ansible\-collections/community\.routeros/pull/463)\)\.
* api\_info\, api\_modify \- add support for <code>interface ethernet switch ingress\-vlan\-translation</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/463](https\://github\.com/ansible\-collections/community\.routeros/pull/463)\)\.
* api\_info\, api\_modify \- add support for <code>interface ethernet switch mac\-based\-vlan</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/463](https\://github\.com/ansible\-collections/community\.routeros/pull/463)\)\.
* api\_info\, api\_modify \- add support for <code>interface ethernet switch multicast\-fdb</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/463](https\://github\.com/ansible\-collections/community\.routeros/pull/463)\)\.
* api\_info\, api\_modify \- add support for <code>interface ethernet switch one2one\-vlan\-switching</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/463](https\://github\.com/ansible\-collections/community\.routeros/pull/463)\)\.
* api\_info\, api\_modify \- add support for <code>interface ethernet switch policer\-qos\-map</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/463](https\://github\.com/ansible\-collections/community\.routeros/pull/463)\)\.
* api\_info\, api\_modify \- add support for <code>interface ethernet switch port\-leakage</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/463](https\://github\.com/ansible\-collections/community\.routeros/pull/463)\)\.
* api\_info\, api\_modify \- add support for <code>interface ethernet switch protocol\-based\-vlan</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/463](https\://github\.com/ansible\-collections/community\.routeros/pull/463)\)\.
* api\_info\, api\_modify \- add support for <code>interface ethernet switch qos\-group</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/463](https\://github\.com/ansible\-collections/community\.routeros/pull/463)\)\.
* api\_info\, api\_modify \- add support for <code>interface ethernet switch reserved\-fdb</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/463](https\://github\.com/ansible\-collections/community\.routeros/pull/463)\)\.
* api\_info\, api\_modify \- add support for <code>interface ethernet switch shaper</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/463](https\://github\.com/ansible\-collections/community\.routeros/pull/463)\)\.
* api\_info\, api\_modify \- add support for <code>interface ethernet switch stats</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/463](https\://github\.com/ansible\-collections/community\.routeros/pull/463)\)\.
* api\_info\, api\_modify \- add support for <code>interface ethernet switch trunk</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/463](https\://github\.com/ansible\-collections/community\.routeros/pull/463)\)\.
* api\_info\, api\_modify \- add support for <code>interface ethernet switch unicast\-fdb</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/463](https\://github\.com/ansible\-collections/community\.routeros/pull/463)\)\.
* api\_info\, api\_modify \- add support for dynamic hardware detection of CRS1xx/2xx switch variants\. Operations on <code>interface ethernet switch</code> and <code>interface ethernet switch port\-isolation</code> paths now automatically adapt to detected hardware \(single\-entry vs multi\-entry switch chips\) \([https\://github\.com/ansible\-collections/community\.routeros/pull/463](https\://github\.com/ansible\-collections/community\.routeros/pull/463)\)\.
* api\_info\, api\_modify \- adds support for multiple <code>healthcheck\-\*</code> parameters in the <code>container</code> path for RouterOS \>\= 7\.22 \([https\://github\.com/ansible\-collections/community\.routeros/pull/457](https\://github\.com/ansible\-collections/community\.routeros/pull/457)\)\.
* api\_info\, api\_modify \- adds support for new <code>input\.add\-path</code> and <code>output\.add\-path</code> parameters replacing <code>add\-path\-out</code> in BGP\-related paths for RouterOS \>\= 7\.22 \([https\://github\.com/ansible\-collections/community\.routeros/pull/457](https\://github\.com/ansible\-collections/community\.routeros/pull/457)\)\.
* api\_info\, api\_modify \- adds support for the <code>add\-topics\-string</code> and <code>script</code> parameters in the <code>system logging action</code> path for RouterOS \>\= 7\.22 \([https\://github\.com/ansible\-collections/community\.routeros/pull/457](https\://github\.com/ansible\-collections/community\.routeros/pull/457)\)\.
* api\_info\, api\_modify \- adds support for the <code>app\-store\-urls</code> parameter in the <code>app settings</code> path for RouterOS \>\= 7\.22 \([https\://github\.com/ansible\-collections/community\.routeros/pull/457](https\://github\.com/ansible\-collections/community\.routeros/pull/457)\)\.
* api\_info\, api\_modify \- adds support for the <code>chain</code>\, <code>realm</code>\, and <code>vrf</code> parameters in the <code>routing rule</code> path for RouterOS \>\= 7\.22 \([https\://github\.com/ansible\-collections/community\.routeros/pull/457](https\://github\.com/ansible\-collections/community\.routeros/pull/457)\)\.
* api\_info\, api\_modify \- adds support for the <code>channel\.preamble\-puncturing</code> parameter in the <code>interface wifi configuration</code> path for RouterOS \>\= 7\.22 \([https\://github\.com/ansible\-collections/community\.routeros/pull/457](https\://github\.com/ansible\-collections/community\.routeros/pull/457)\)\.
* api\_info\, api\_modify \- adds support for the <code>channel\.preamble\-puncturing</code>\, <code>mld\-interface</code>\, and <code>mld\-name</code> parameters in the <code>interface wifi</code> path for RouterOS \>\= 7\.22 \([https\://github\.com/ansible\-collections/community\.routeros/pull/457](https\://github\.com/ansible\-collections/community\.routeros/pull/457)\)\.
* api\_info\, api\_modify \- adds support for the <code>comment</code> parameter in the <code>system logging</code> path for RouterOS \>\= 7\.22 \([https\://github\.com/ansible\-collections/community\.routeros/pull/457](https\://github\.com/ansible\-collections/community\.routeros/pull/457)\)\.
* api\_info\, api\_modify \- adds support for the <code>ddos\-cookie\-threshold</code> parameter in the <code>ip ipsec settings</code> path for RouterOS \>\= 7\.22 \([https\://github\.com/ansible\-collections/community\.routeros/pull/457](https\://github\.com/ansible\-collections/community\.routeros/pull/457)\)\.
* api\_info\, api\_modify \- adds support for the <code>dhcp6\-pd\-preferred</code> parameter in the <code>ipv6 nd prefix</code> and <code>ipv6 nd prefix default</code> paths for RouterOS \>\= 7\.22 \([https\://github\.com/ansible\-collections/community\.routeros/pull/457](https\://github\.com/ansible\-collections/community\.routeros/pull/457)\)\.
* api\_info\, api\_modify \- adds support for the <code>from\-pool</code> parameter in the <code>ipv6 pool</code> path for RouterOS \>\= 7\.22 \([https\://github\.com/ansible\-collections/community\.routeros/pull/457](https\://github\.com/ansible\-collections/community\.routeros/pull/457)\)\.
* api\_info\, api\_modify \- adds support for the <code>interface wifi network</code> and <code>interface wifi network radio</code> paths for RouterOS \>\= 7\.22 \([https\://github\.com/ansible\-collections/community\.routeros/pull/457](https\://github\.com/ansible\-collections/community\.routeros/pull/457)\)\.
* api\_info\, api\_modify \- adds support for the <code>interframe\-gap</code> parameter in the <code>iot modbus</code> path for RouterOS \>\= 7\.22 \([https\://github\.com/ansible\-collections/community\.routeros/pull/457](https\://github\.com/ansible\-collections/community\.routeros/pull/457)\)\.
* api\_info\, api\_modify \- adds support for the <code>ip reverse\-proxy</code> path for RouterOS \>\= 7\.22 \([https\://github\.com/ansible\-collections/community\.routeros/pull/457](https\://github\.com/ansible\-collections/community\.routeros/pull/457)\)\.
* api\_info\, api\_modify \- adds support for the <code>mlag\-heartbeat</code>\, <code>mlag\-peer\-port</code>\, <code>mlag\-priority</code>\, and <code>ra\-guard</code> parameters in the <code>interface bridge</code> path for RouterOS \>\= 7\.22 \([https\://github\.com/ansible\-collections/community\.routeros/pull/457](https\://github\.com/ansible\-collections/community\.routeros/pull/457)\)\.
* api\_info\, api\_modify \- adds support for the <code>mld\-static</code> parameter in the <code>interface wifi cap</code> path for RouterOS \>\= 7\.22 \([https\://github\.com/ansible\-collections/community\.routeros/pull/457](https\://github\.com/ansible\-collections/community\.routeros/pull/457)\)\.
* api\_info\, api\_modify \- adds support for the <code>multi\-link\-mode</code> and <code>supported\-hw\-caps</code> parameters in the <code>interface wifi provisioning</code> path for RouterOS \>\= 7\.22 \([https\://github\.com/ansible\-collections/community\.routeros/pull/457](https\://github\.com/ansible\-collections/community\.routeros/pull/457)\)\.
* api\_info\, api\_modify \- adds support for the <code>multipath</code> parameter in the <code>routing bgp instance</code> path for RouterOS \>\= 7\.22 \([https\://github\.com/ansible\-collections/community\.routeros/pull/457](https\://github\.com/ansible\-collections/community\.routeros/pull/457)\)\.
* api\_info\, api\_modify \- adds support for the <code>name</code> parameter in the <code>ip dhcp\-client</code> path for RouterOS \>\= 7\.22 \([https\://github\.com/ansible\-collections/community\.routeros/pull/457](https\://github\.com/ansible\-collections/community\.routeros/pull/457)\)\.
* api\_info\, api\_modify \- adds support for the <code>otp\-secret</code> parameter in the <code>ip hotspot user</code> path for RouterOS \>\= 7\.21\.3 \([https\://github\.com/ansible\-collections/community\.routeros/pull/457](https\://github\.com/ansible\-collections/community\.routeros/pull/457)\)\.
* api\_info\, api\_modify \- adds support for the <code>password</code> parameter in the <code>system package local\-update update\-package\-source</code> path for RouterOS \>\= 7\.22 \([https\://github\.com/ansible\-collections/community\.routeros/pull/457](https\://github\.com/ansible\-collections/community\.routeros/pull/457)\)\.
* api\_info\, api\_modify \- adds support for the <code>policy\-rules</code> parameter in the <code>routing settings</code> path for RouterOS \>\= 7\.22 \([https\://github\.com/ansible\-collections/community\.routeros/pull/457](https\://github\.com/ansible\-collections/community\.routeros/pull/457)\)\.
* api\_info\, api\_modify \- adds support for the <code>preamble\-puncturing</code> parameter in the <code>interface wifi channel</code> path for RouterOS \>\= 7\.22 \([https\://github\.com/ansible\-collections/community\.routeros/pull/457](https\://github\.com/ansible\-collections/community\.routeros/pull/457)\)\.
* api\_info\, api\_modify \- adds support for the <code>preferred\-architecture</code> parameter in the <code>system routerboard settings</code> path for RouterOS \>\= 7\.22 \([https\://github\.com/ansible\-collections/community\.routeros/pull/457](https\://github\.com/ansible\-collections/community\.routeros/pull/457)\)\.
* api\_info\, api\_modify \- adds support for the <code>pvid</code>\, <code>use\-https</code>\, and <code>yaml</code> parameters in the <code>app</code> path for RouterOS \>\= 7\.22 \([https\://github\.com/ansible\-collections/community\.routeros/pull/457](https\://github\.com/ansible\-collections/community\.routeros/pull/457)\)\.
* api\_info\, api\_modify \- adds support for the <code>request\-interval</code> parameter in the <code>interface detect\-internet</code> path for RouterOS \>\= 7\.22 \([https\://github\.com/ansible\-collections/community\.routeros/pull/457](https\://github\.com/ansible\-collections/community\.routeros/pull/457)\)\.
* api\_info\, api\_modify \- adds support for the <code>trusted\-ra</code> parameter in the <code>interface bridge port</code> path for RouterOS \>\= 7\.22 \([https\://github\.com/ansible\-collections/community\.routeros/pull/457](https\://github\.com/ansible\-collections/community\.routeros/pull/457)\)\.
* api\_info\, api\_modify \- adjusts handling of required parameters in the <code>interface wifi</code> path by removing <code>default\-name</code> from <code>required\_one\_of</code> for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/457](https\://github\.com/ansible\-collections/community\.routeros/pull/457)\)\.
* api\_info\, api\_modify \- removed support for the <code>add\-path\-out</code> parameter in BGP\-related paths for RouterOS \>\= 7\.22 \([https\://github\.com/ansible\-collections/community\.routeros/pull/457](https\://github\.com/ansible\-collections/community\.routeros/pull/457)\)\.
* api\_info\, api\_modify \- removed support for the <code>system package local\-update</code> path for RouterOS \>\= 7\.22 \([https\://github\.com/ansible\-collections/community\.routeros/pull/457](https\://github\.com/ansible\-collections/community\.routeros/pull/457)\)\.
* api\_modify\, api\_info \- sort versioned buckets numerically so tighter bounds match before broader ones \([https\://github\.com/ansible\-collections/community\.routeros/pull/456](https\://github\.com/ansible\-collections/community\.routeros/pull/456)\)\.

<a id="community-sops"></a>
#### community\.sops

* all modules and plugins \- allow retrieving private age keys and private SSH keys through commands with the new <code>age\_key\_cmd</code> and <code>age\_ssh\_private\_key\_cmd</code> options \([https\://github\.com/ansible\-collections/community\.sops/issues/282](https\://github\.com/ansible\-collections/community\.sops/issues/282)\, [https\://github\.com/ansible\-collections/community\.sops/pull/286](https\://github\.com/ansible\-collections/community\.sops/pull/286)\)\.
* all modules and plugins \- allow to configure GCP access with the <code>gcp\_oauth\_access\_token</code> and <code>gcp\_kms\_client\_type</code> options \([https\://github\.com/ansible\-collections/community\.sops/issues/282](https\://github\.com/ansible\-collections/community\.sops/issues/282)\, [https\://github\.com/ansible\-collections/community\.sops/pull/286](https\://github\.com/ansible\-collections/community\.sops/pull/286)\)\.
* load\_vars \- now supports ansible\-core 2\.21\'s way of actually loading variables\, instead of returning <code>ansible\_facts</code>\. The behavior for this can be controlled through the new <code>return\_method</code> option\, which is by default set to <code>auto</code>\. On ansible\-core 2\.21\+\, <code>auto</code> behaves the same as <code>vars\-only</code> \(return proper variables\)\, and for ansible\-core before 2\.21 the same as <code>facts\-only</code> \(return <code>ansible\_facts</code>\) \([https\://github\.com/ansible\-collections/community\.sops/pull/283](https\://github\.com/ansible\-collections/community\.sops/pull/283)\)\.
* sops\_encrypt \- support providing HuaweiCloud KMS key IDs with the <code>huawei\_cloud\_kms</code> option \([https\://github\.com/ansible\-collections/community\.sops/issues/282](https\://github\.com/ansible\-collections/community\.sops/issues/282)\, [https\://github\.com/ansible\-collections/community\.sops/pull/286](https\://github\.com/ansible\-collections/community\.sops/pull/286)\)\.

<a id="community-zabbix"></a>
#### community\.zabbix

* host \- Added support for vault passwords\.
* web role \- added support for IPv6
* zabbix frontend and server encryption support\: [https\://www\.zabbix\.com/documentation/7\.4/en/manual/introduction/whatsnew\#tls\-encryption\-between\-frontend\-and\-server](https\://www\.zabbix\.com/documentation/7\.4/en/manual/introduction/whatsnew\#tls\-encryption\-between\-frontend\-and\-server) \& [https\://www\.zabbix\.com/documentation/current/en/manual/appendix/install/frontend\_encrypt](https\://www\.zabbix\.com/documentation/current/en/manual/appendix/install/frontend\_encrypt)
* zabbix\_agent \- \[WINDOWS\] Add INSTALLFOLDER parameter to msi install
* zabbix\_agent \- add variable for customizing releases url \([https\://services\.zabbix\.com/updates/v1](https\://services\.zabbix\.com/updates/v1)\)
* zabbix\_triggerprototype \- use templated and templateid\=0 when host\_name is given\, only templated for template\_name
* zabbix\_valuemap \- add value mappings type suboption which specifies the mapping match type \([https\://github\.com/ansible\-collections/community\.zabbix/issues/1636](https\://github\.com/ansible\-collections/community\.zabbix/issues/1636)\)\.

<a id="containers-podman"></a>
#### containers\.podman

* Add \-\-platform option to podman\_image

<a id="dellemc-openmanage"></a>
#### dellemc\.openmanage

* Added support for OpenManage Enterprise version 4\.4 and 4\.5\.
* The OpenManage Enterprise\, OpenManage Enterprise Modular and OpenManage Enterprise Integration for VMware vCenter modules are now compatible with Ansible Core version 2\.20\.

<a id="google-cloud"></a>
#### google\.cloud

* gcp\_colab\_\* \- added four new modules \(gcp\_colab\_notebook\_execution\, gcp\_colab\_runtime\, gcp\_colab\_runtime\_template\, and gcp\_colab\_schedule\) \([https\://github\.com/ansible\-collections/google\.cloud/pull/747](https\://github\.com/ansible\-collections/google\.cloud/pull/747)\)\.
* gcp\_compute\_instance\_\* \- renamed the <em class="title-reference">tags\.items</em> field to <em class="title-reference">tags\.tag\_values</em>\. The old naming is still available but will be removed in a future release\. \([https\://github\.com/ansible\-collections/google\.cloud/pull/750](https\://github\.com/ansible\-collections/google\.cloud/pull/750)\)\.

<a id="graphiant-naas"></a>
#### graphiant\.naas

* Minimum <code>graphiant\-sdk</code> raised to <code>\>\= 26\.3\.0</code> \(see <code>\_version\.py</code> <code>DEPENDENCIES</code>\)
* Portal authentication\: optional <code>access\_token</code> module option and <code>GRAPHIANT\_ACCESS\_TOKEN</code> environment variable \(e\.g\. after <code>graphiant login</code>\)\; invalid or missing token falls back to username/password when provided

<a id="ibm-storage-virtualize"></a>
#### ibm\.storage\_virtualize

* ibm\_svc\_initial\_setup \- Added support for managing anomaly settings
* ibm\_svc\_manage\_volume \- Added support for addressing volume via UID

<a id="lowlydba-sqlserver"></a>
#### lowlydba\.sqlserver

* user\_role \- Added <code>roles</code> parameter with <code>add</code>/<code>remove</code>/<code>set</code> pattern to manage multiple roles\. The existing <code>role</code> parameter is deprecated and will be removed in 3\.0\.0\. \(\#352\)

<a id="theforeman-foreman"></a>
#### theforeman\.foreman

* Support OAuth1 authentication by passing <code>oauth1\_consumer\_key</code> and <code>oauth1\_consumer\_secret</code> instead of <code>username</code> and <code>password</code>\.
* registration\_command \- add support for the setup\_container\_registry\_certs parameter \([https\://github\.com/theforeman/foreman\-ansible\-modules/pull/1966](https\://github\.com/theforeman/foreman\-ansible\-modules/pull/1966)\)

<a id="deprecated-features"></a>
### Deprecated Features

* The <code>cisco\.dnac</code> collection has been deprecated\.
  It will be removed from Ansible 14 if no one starts maintaining it again before Ansible 14\.
  See [Collections Removal Process for unmaintained collections](https\://docs\.ansible\.com/projects/ansible/devel/community/collection\_contributors/collection\_package\_removal\.html\#unmaintained\-collections) for more details \([https\://forum\.ansible\.com/t/45609](https\://forum\.ansible\.com/t/45609)\)\.

<a id="ansible-netcommon-1"></a>
#### ansible\.netcommon

* network\_cli \- The in\-collection paramiko support \(used when ssh\_type is paramiko\) is a compatibility layer for environments where ansible\-core\'s paramiko connection is no longer available\. This layer is deprecated and will be removed in a release after 2028\-02\-01\. Migrate to ssh\_type\=libssh by installing the ansible\-pylibssh package\.

<a id="community-routeros-1"></a>
#### community\.routeros

* api\_modify \- all existing <code>numbers</code> fields are deprecated for writing and support for them will be removed in community\.routeros 4\.0\.0 \([https\://github\.com/ansible\-collections/community\.routeros/pull/460](https\://github\.com/ansible\-collections/community\.routeros/pull/460)\)\.
* api\_modify \- in <code>routing bfd configuration</code>\, the fields <code>copy\-from</code> and <code>place\-before</code> are deprecated for writing and support for them will be removed in community\.routeros 4\.0\.0 \([https\://github\.com/ansible\-collections/community\.routeros/pull/460](https\://github\.com/ansible\-collections/community\.routeros/pull/460)\)\.

<a id="bugfixes"></a>
### Bugfixes

<a id="ansible-core-2"></a>
#### Ansible\-core

* Fix <code>validate\_argspec</code> when tags are defined on the play\. The <code>always</code> tag is only added if the play has no tags\.
* <code>\-\-start\-at\-task</code> \- fix starting at the requested task instead of starting at the next block or play\. Play level tasks run first\. \([https\://github\.com/ansible/ansible/issues/86268](https\://github\.com/ansible/ansible/issues/86268)\)
* ansible\-galaxy collection \- Fix using the server configuration for <code>validate\_certs</code> when downloading collections\. \([https\://github\.com/ansible/ansible/issues/86694](https\://github\.com/ansible/ansible/issues/86694)\)
* ansible\_facts\[os\_\*\] \- Contained wrong information\, if ClearLinux parsing was tried before falling back to general os\-release parsing
* templating \- Fix traceback when using <code>deepcopy</code> on an imported template \([https\://github\.com/ansible/ansible/issues/86723](https\://github\.com/ansible/ansible/issues/86723)\)\.

<a id="ansible-netcommon-2"></a>
#### ansible\.netcommon

* filter plugins \- Add plugin\_routing redirects for <code>ipaddr</code>\, <code>ipv4</code>\, and <code>ipv6</code> to <code>ansible\.utils</code> so short names work when <code>ansible\.netcommon</code> is in the play\'s collection list \([https\://github\.com/ansible\-collections/ansible\.utils/issues/404](https\://github\.com/ansible\-collections/ansible\.utils/issues/404)\)\.
* filter plugins \- Convert filter arguments to native Python types before <code>AnsibleArgSpecValidator</code> so filters work with Ansible 2\.19\+ lazy containers that cannot be deep\-copied \(e\.g\. <code>vlan\_parser</code>\, <code>vlan\_expander</code>\, <code>hash\_salt</code>\, <code>type5\_pw</code>\, <code>comp\_type5</code>\, <code>parse\_cli</code>\, <code>parse\_cli\_textfsm</code>\, <code>parse\_xml</code>\, <code>pop\_ace</code>\)\.
* libssh connection \- Fixed test\_libssh\_put\_file unit test so the put\_file code path \(used by net\_put\, copy module\, and other file transfer over libssh\) is properly tested in CI\. The test now sets connection options and mocks Session so put\_file does not trigger a real connection attempt with an unset host \(was failing with \"Hostname required\"\)\.
* network action plugin \- Fall back when remove\_internal\_keys is not importable from ansible\.vars\.clean \(e\.g\. some ansible\-core builds\)\, so direct module execution still cleans module return data\.
* network\_cli \- Fixed file transfer \(net\_put / net\_get\) when ssh\_type\=libssh\. For put\_file\, no longer call\_connect\_uncached\(\) before delegating to the libssh connection the libssh plugin\'s put\_file\(\) calls \_connect\(\) internally\. For fetch\_file\, call \_connect\(\) then fetch\_file\(\) for libssh instead of \_connect\_uncached\(\)\, so connection caching and the correct flow are used\. Paramiko branch unchanged \(still uses \_connect\_uncached\(\) for scp/sftp\)\.

<a id="ansible-utils"></a>
#### ansible\.utils

* cidr\_merge \- Fix filter failing when used inside a Jinja2 macro called with <code>with context</code> by unwrapping Ansible lazy template lists before validation\.
* cli\_parse \- Honor ttp\_results\.results flat\_list in TTP parser so output is a single\-level list instead of double\-wrapped \([https\://github\.com/ansible\-collections/ansible\.utils/issues/402](https\://github\.com/ansible\-collections/ansible\.utils/issues/402)\)\.
* ipaddress\_utils \- Support Python 3\.14\+ by using the public <code>version</code> attribute instead of the removed private <code>\_version</code> on <code>ipaddress</code> network objects \(bpo\-118710\)\.
* update\_fact \- Use task\_vars at top\-level instead of the deprecated <code>vars</code> key for compatibility with ansible\-core 2\.24 \(ansible/ansible issue

<a id="cisco-iosxr-1"></a>
#### cisco\.iosxr

* Fixed iosxr\_user module to correctly handle MD5 hashed passwords when updating user credentials\.

<a id="cisco-meraki"></a>
#### cisco\.meraki

* devices\_switch\_ports \- Fixed AttributeError crash in <code>update\(\)</code> caused by <code>get\_object\_by\_name</code> returning the full port list instead of <code>None</code> when no port matched by name\. Added <code>isinstance\(prev\_obj\_name\, dict\)</code> guard to prevent calling <code>\.get\(\)</code> on a list\.
* devices\_switch\_ports \- Fixed idempotency regression where the module always reported <code>changed</code> due to <code>serial</code> \(a path parameter absent from the API response\) and <code>portId</code> \(int/string type mismatch\) being incorrectly included in the <code>requires\_update</code> comparison\.

<a id="community-crypto-1"></a>
#### community\.crypto

* acme\_\* modules \- improve handling of authz deactivation\, and improve error message in case of bad authz states \([https\://github\.com/ansible\-collections/community\.crypto/pull/998](https\://github\.com/ansible\-collections/community\.crypto/pull/998)\)\.

<a id="community-dns"></a>
#### community\.dns

* Update Public Suffix List\.

<a id="community-general-1"></a>
#### community\.general

* alternatives \- normalize locale environment for <code>run\_command\(\)</code> calls to <code>LANGUAGE\=C</code>\, <code>LC\_ALL\=C</code> \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11738](https\://github\.com/ansible\-collections/community\.general/pull/11738)\)\.
* apache2\_module \- ensure <code>LANGUAGE\=C</code> and <code>LC\_ALL\=C</code> are set when running commands that parse output \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11768](https\://github\.com/ansible\-collections/community\.general/pull/11768)\)\.
* apk \- normalize locale environment for <code>run\_command\(\)</code> calls to <code>LANGUAGE\=C</code>\, <code>LC\_ALL\=C</code> \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11738](https\://github\.com/ansible\-collections/community\.general/pull/11738)\)\.
* apt\_repo \- set <code>LANGUAGE</code> and <code>LC\_ALL</code> to <code>C</code> in <code>run\_command\(\)</code> calls to ensure locale\-independent output parsing \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11782](https\://github\.com/ansible\-collections/community\.general/pull/11782)\)\.
* apt\_rpm \- normalize locale environment for <code>run\_command\(\)</code> calls to <code>LANGUAGE\=C</code>\, <code>LC\_ALL\=C</code> \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11738](https\://github\.com/ansible\-collections/community\.general/pull/11738)\)\.
* awall \- set <code>LANGUAGE</code> and <code>LC\_ALL</code> to <code>C</code> in <code>run\_command\(\)</code> calls to ensure locale\-independent output parsing \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11784](https\://github\.com/ansible\-collections/community\.general/pull/11784)\)\.
* beadm \- set <code>LANGUAGE</code> and <code>LC\_ALL</code> to <code>C</code> in <code>run\_command\(\)</code> calls to ensure locale\-independent output parsing \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11780](https\://github\.com/ansible\-collections/community\.general/pull/11780)\)\.
* bower \- set <code>LANGUAGE</code> and <code>LC\_ALL</code> to <code>C</code> in <code>run\_command\(\)</code> calls to ensure locale\-independent output parsing \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11783](https\://github\.com/ansible\-collections/community\.general/pull/11783)\)\.
* btrfs module\_utils \- set <code>LANGUAGE</code> and <code>LC\_ALL</code> environment variables to <code>C</code> in all <code>run\_command\(\)</code> calls \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11787](https\://github\.com/ansible\-collections/community\.general/pull/11787)\)\.
* bundler \- set <code>LANGUAGE</code> and <code>LC\_ALL</code> to <code>C</code> in <code>run\_command\(\)</code> calls to ensure locale\-independent output parsing \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11783](https\://github\.com/ansible\-collections/community\.general/pull/11783)\)\.
* bzr \- set <code>LANGUAGE</code> and <code>LC\_ALL</code> to <code>C</code> in <code>run\_command\(\)</code> calls to ensure locale\-independent output parsing \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11785](https\://github\.com/ansible\-collections/community\.general/pull/11785)\)\.
* capabilities \- set <code>LANGUAGE</code> and <code>LC\_ALL</code> to <code>C</code> in <code>run\_command\(\)</code> calls to ensure locale\-independent output parsing \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11779](https\://github\.com/ansible\-collections/community\.general/pull/11779)\)\.
* cargo \- normalize locale environment for <code>run\_command\(\)</code> calls to <code>LANGUAGE\=C</code>\, <code>LC\_ALL\=C</code> \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11738](https\://github\.com/ansible\-collections/community\.general/pull/11738)\)\.
* composer \- ensure <code>LANGUAGE\=C</code> and <code>LC\_ALL\=C</code> are set when running commands that parse output \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11768](https\://github\.com/ansible\-collections/community\.general/pull/11768)\)\.
* cronvar \- ensure <code>LANGUAGE\=C</code> and <code>LC\_ALL\=C</code> are set when running commands that parse output \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11773](https\://github\.com/ansible\-collections/community\.general/pull/11773)\)\.
* dconf \- ensure <code>LANGUAGE\=C</code> and <code>LC\_ALL\=C</code> are set when running commands that parse output \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11765](https\://github\.com/ansible\-collections/community\.general/pull/11765)\)\.
* dnf\_versionlock \- ensure <code>LANGUAGE\=C</code> and <code>LC\_ALL\=C</code> are set when running commands that parse output \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11773](https\://github\.com/ansible\-collections/community\.general/pull/11773)\)\.
* dpkg\_divert \- ensure <code>LANGUAGE\=C</code> and <code>LC\_ALL\=C</code> are set when running commands that parse output \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11773](https\://github\.com/ansible\-collections/community\.general/pull/11773)\)\.
* easy\_install \- set <code>LANGUAGE</code> and <code>LC\_ALL</code> to <code>C</code> in <code>run\_command\(\)</code> calls to ensure locale\-independent output parsing \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11782](https\://github\.com/ansible\-collections/community\.general/pull/11782)\)\.
* etcd3 lookup plugin \- improve HTTPS endpoint handling by stripping URL schemes from the <code>host</code> option and warning when <code>ca\_cert</code> is not provided for HTTPS endpoints \([https\://github\.com/ansible\-collections/community\.general/issues/1664](https\://github\.com/ansible\-collections/community\.general/issues/1664)\, [https\://github\.com/ansible\-collections/community\.general/pull/11861](https\://github\.com/ansible\-collections/community\.general/pull/11861)\)\.
* facter\_facts \- ensure <code>LANGUAGE\=C</code> and <code>LC\_ALL\=C</code> are set when running commands that parse output \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11768](https\://github\.com/ansible\-collections/community\.general/pull/11768)\)\.
* filesystem \- normalize locale environment for <code>run\_command\(\)</code> calls to <code>LANGUAGE\=C</code>\, <code>LC\_ALL\=C</code> \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11738](https\://github\.com/ansible\-collections/community\.general/pull/11738)\)\.
* flatpak \- fix removal of runtimes\, which was broken because the module was filtering the installed flatpak list to apps only\, so runtimes could never be matched for uninstallation \([https\://github\.com/ansible\-collections/community\.general/issues/553](https\://github\.com/ansible\-collections/community\.general/issues/553)\, [https\://github\.com/ansible\-collections/community\.general/pull/11688](https\://github\.com/ansible\-collections/community\.general/pull/11688)\)\.
* flatpak \- support new output message when an update resulted in no action that appears on Fedora 44 \([https\://github\.com/ansible\-collections/community\.general/pull/11836](https\://github\.com/ansible\-collections/community\.general/pull/11836)\)\.
* flatpak\_remote \- ensure <code>LANGUAGE\=C</code> and <code>LC\_ALL\=C</code> are set when running commands that parse output \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11773](https\://github\.com/ansible\-collections/community\.general/pull/11773)\)\.
* git\_config \- normalize locale environment for <code>run\_command\(\)</code> calls to <code>LANGUAGE\=C</code>\, <code>LC\_ALL\=C</code> \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11738](https\://github\.com/ansible\-collections/community\.general/pull/11738)\)\.
* git\_config\_info \- normalize locale environment for <code>run\_command\(\)</code> calls to <code>LANGUAGE\=C</code>\, <code>LC\_ALL\=C</code> \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11738](https\://github\.com/ansible\-collections/community\.general/pull/11738)\)\.
* gitlab\_project\_members \- fail with a clear error when multiple projects match the given name\, instead of silently operating on the first result \([https\://github\.com/ansible\-collections/community\.general/issues/2767](https\://github\.com/ansible\-collections/community\.general/issues/2767)\, [https\://github\.com/ansible\-collections/community\.general/pull/11851](https\://github\.com/ansible\-collections/community\.general/pull/11851)\)\.
* gitlab\_project\_variable \- use <code>find\_project\(\)</code> from module utils for project lookup\, consistent with all other GitLab modules in the collection \([https\://github\.com/ansible\-collections/community\.general/issues/3157](https\://github\.com/ansible\-collections/community\.general/issues/3157)\, [https\://github\.com/ansible\-collections/community\.general/pull/11878](https\://github\.com/ansible\-collections/community\.general/pull/11878)\)\.
* hg \- ensure <code>LANGUAGE\=C</code> and <code>LC\_ALL\=C</code> are set when running commands that parse output \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11773](https\://github\.com/ansible\-collections/community\.general/pull/11773)\)\.
* homebrew \- normalize locale environment for <code>run\_command\(\)</code> calls to <code>LANGUAGE\=C</code>\, <code>LC\_ALL\=C</code> \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11740](https\://github\.com/ansible\-collections/community\.general/pull/11740)\)\.
* homebrew\_cask \- fix <code>sudo\_password</code> failing when the password contains single quotes or other special shell characters \([https\://github\.com/ansible\-collections/community\.general/issues/4957](https\://github\.com/ansible\-collections/community\.general/issues/4957)\, [https\://github\.com/ansible\-collections/community\.general/pull/11850](https\://github\.com/ansible\-collections/community\.general/pull/11850)\)\.
* homebrew\_cask \- fix failure when <code>brew \-\-version</code> returns a placeholder version string \([https\://github\.com/ansible\-collections/community\.general/issues/4708](https\://github\.com/ansible\-collections/community\.general/issues/4708)\, [https\://github\.com/ansible\-collections/community\.general/pull/11849](https\://github\.com/ansible\-collections/community\.general/pull/11849)\)\.
* homebrew\_cask \- fix false task failure when upgrading casks with <code>version\=latest</code>\; the post\-upgrade check incorrectly re\-ran <code>brew outdated</code> \(which always lists <code>latest</code> casks as outdated under <code>\-\-greedy</code>\)\, now uses the command exit code instead \([https\://github\.com/ansible\-collections/community\.general/issues/1647](https\://github\.com/ansible\-collections/community\.general/issues/1647)\, [https\://github\.com/ansible\-collections/community\.general/pull/11838](https\://github\.com/ansible\-collections/community\.general/pull/11838)\)\.
* homebrew\_cask \- normalize locale environment for <code>run\_command\(\)</code> calls to <code>LANGUAGE\=C</code>\, <code>LC\_ALL\=C</code> \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11740](https\://github\.com/ansible\-collections/community\.general/pull/11740)\)\.
* homebrew\_tap \- fix <code>None</code> being passed as a command argument when adding a tap without a URL \([https\://github\.com/ansible\-collections/community\.general/pull/11848](https\://github\.com/ansible\-collections/community\.general/pull/11848)\)\.
* homectl \- allow to use passlib instead of legacycrypt for Python 3\.13\+ \([https\://github\.com/ansible\-collections/community\.general/pull/11860](https\://github\.com/ansible\-collections/community\.general/pull/11860)\)\.
* homectl \- set <code>LANGUAGE</code> and <code>LC\_ALL</code> to <code>C</code> in <code>run\_command\(\)</code> calls to ensure locale\-independent output parsing \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11774](https\://github\.com/ansible\-collections/community\.general/pull/11774)\)\.
* icinga2\_feature \- normalize locale environment for <code>run\_command\(\)</code> calls to <code>LANGUAGE\=C</code>\, <code>LC\_ALL\=C</code> \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11740](https\://github\.com/ansible\-collections/community\.general/pull/11740)\)\.
* imgadm \- set <code>LANGUAGE</code> and <code>LC\_ALL</code> to <code>C</code> in <code>run\_command\(\)</code> calls to ensure locale\-independent output parsing \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11781](https\://github\.com/ansible\-collections/community\.general/pull/11781)\)\.
* incus connection plugin \- work when the active become plugin sets <code>require\_tty</code> instead of failing silently \([https\://github\.com/ansible\-collections/community\.general/pull/11771](https\://github\.com/ansible\-collections/community\.general/pull/11771)\)\.
* ip\_netns \- set <code>LANGUAGE</code> and <code>LC\_ALL</code> to <code>C</code> in <code>run\_command\(\)</code> calls to ensure locale\-independent output parsing \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11779](https\://github\.com/ansible\-collections/community\.general/pull/11779)\)\.
* ipa module utils \- fix failure to detect errors reported in the <code>failed</code> field of the IPA API response\, which is returned with HTTP 200 on partial or full failures in member add/remove operations \([https\://github\.com/ansible\-collections/community\.general/issues/1239](https\://github\.com/ansible\-collections/community\.general/issues/1239)\, [https\://github\.com/ansible\-collections/community\.general/pull/11698](https\://github\.com/ansible\-collections/community\.general/pull/11698)\)\.
* ipa\_dnsrecord \- fix errors when module is used with existing record with default TTL \([https\://github\.com/ansible\-collections/community\.general/pull/11717](https\://github\.com/ansible\-collections/community\.general/pull/11717)\)\.
* ipa\_host \- fix logic to disable existing hosts \([https\://github\.com/ansible\-collections/community\.general/issues/11483](https\://github\.com/ansible\-collections/community\.general/issues/11483)\, [https\://github\.com/ansible\-collections/community\.general/pull/11487](https\://github\.com/ansible\-collections/community\.general/pull/11487)\)\.
* iptables\_state \- normalize locale environment for <code>run\_command\(\)</code> calls to <code>LANGUAGE\=C</code>\, <code>LC\_ALL\=C</code> \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11740](https\://github\.com/ansible\-collections/community\.general/pull/11740)\)\.
* iso\_extract \- retry <code>umount</code> up to 5 times preventing <code>OSError</code> on cleanup \([https\://github\.com/ansible\-collections/community\.general/issues/5333](https\://github\.com/ansible\-collections/community\.general/issues/5333)\, [https\://github\.com/ansible\-collections/community\.general/pull/11837](https\://github\.com/ansible\-collections/community\.general/pull/11837)\)\.
* iso\_extract \- strip leading path separator from file entries so files with a leading <code>/</code> are extracted correctly \([https\://github\.com/ansible\-collections/community\.general/issues/5283](https\://github\.com/ansible\-collections/community\.general/issues/5283)\, [https\://github\.com/ansible\-collections/community\.general/pull/11825](https\://github\.com/ansible\-collections/community\.general/pull/11825)\)\.
* java\_cert \- set <code>LANGUAGE</code> and <code>LC\_ALL</code> to <code>C</code> in <code>run\_command\(\)</code> calls to ensure locale\-independent output parsing \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11774](https\://github\.com/ansible\-collections/community\.general/pull/11774)\)\.
* java\_keystore \- normalize locale environment for <code>run\_command\(\)</code> calls to <code>LANGUAGE\=C</code>\, <code>LC\_ALL\=C</code> \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11740](https\://github\.com/ansible\-collections/community\.general/pull/11740)\)\.
* keyring \- set <code>LANGUAGE</code> and <code>LC\_ALL</code> to <code>C</code> in <code>run\_command\(\)</code> calls to ensure locale\-independent output parsing \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11774](https\://github\.com/ansible\-collections/community\.general/pull/11774)\)\.
* keyring\_info \- set <code>LANGUAGE</code> and <code>LC\_ALL</code> to <code>C</code> in <code>run\_command\(\)</code> calls to ensure locale\-independent output parsing \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11786](https\://github\.com/ansible\-collections/community\.general/pull/11786)\)\.
* kibana\_plugin \- set <code>LANGUAGE</code> and <code>LC\_ALL</code> to <code>C</code> in <code>run\_command\(\)</code> calls to ensure locale\-independent output parsing \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11783](https\://github\.com/ansible\-collections/community\.general/pull/11783)\)\.
* known\_hosts module utils \- ensure <code>LANGUAGE\=C</code> and <code>LC\_ALL\=C</code> are set when running commands that parse output \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11768](https\://github\.com/ansible\-collections/community\.general/pull/11768)\)\.
* launchd \- set <code>LANGUAGE</code> and <code>LC\_ALL</code> to <code>C</code> in <code>run\_command\(\)</code> calls to ensure locale\-independent output parsing \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11774](https\://github\.com/ansible\-collections/community\.general/pull/11774)\)\.
* lbu \- set <code>LANGUAGE</code> and <code>LC\_ALL</code> to <code>C</code> in <code>run\_command\(\)</code> calls to ensure locale\-independent output parsing \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11781](https\://github\.com/ansible\-collections/community\.general/pull/11781)\)\.
* listen\_ports\_facts \- set <code>LANGUAGE</code> and <code>LC\_ALL</code> to <code>C</code> in <code>run\_command\(\)</code> calls to ensure locale\-independent output parsing \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11774](https\://github\.com/ansible\-collections/community\.general/pull/11774)\)\.
* lldp \- set <code>LANGUAGE</code> and <code>LC\_ALL</code> to <code>C</code> in <code>run\_command\(\)</code> calls to ensure locale\-independent output parsing \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11785](https\://github\.com/ansible\-collections/community\.general/pull/11785)\)\.
* locale\_gen \- add missing locale entries to <code>/etc/locale\.gen</code> when not already present \([https\://github\.com/ansible\-collections/community\.general/issues/2399](https\://github\.com/ansible\-collections/community\.general/issues/2399)\, [https\://github\.com/ansible\-collections/community\.general/pull/11824](https\://github\.com/ansible\-collections/community\.general/pull/11824)\)\.
* logrotate \- adds missing default values for <code>state</code> and <code>config\_dir</code> parameters\, and adds <code>required\_by</code> declarations for shred and compression parameters \([https\://github\.com/ansible\-collections/community\.general/pull/11764](https\://github\.com/ansible\-collections/community\.general/pull/11764)\)\.
* logrotate \- fixes <code>TypeError</code> when <code>shred\_cycles</code> is <code>None</code> and corrects <code>enabled\=None</code> handling in <code>get\_config\_path\(\)</code> \([https\://github\.com/ansible\-collections/community\.general/pull/11764](https\://github\.com/ansible\-collections/community\.general/pull/11764)\)\.
* logrotate \- writes configuration files to a temporary file first and validates before atomically moving to the destination\, and properly wraps all <code>os\.remove\(\)</code> and <code>atomic\_move\(\)</code> calls in error handling \([https\://github\.com/ansible\-collections/community\.general/pull/11764](https\://github\.com/ansible\-collections/community\.general/pull/11764)\)\.
* logstash\_plugin \- set <code>LANGUAGE</code> and <code>LC\_ALL</code> to <code>C</code> in <code>run\_command\(\)</code> calls to ensure locale\-independent output parsing \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11775](https\://github\.com/ansible\-collections/community\.general/pull/11775)\)\.
* lvg \- set <code>LANGUAGE</code> and <code>LC\_ALL</code> to <code>C</code> in <code>run\_command\(\)</code> calls to ensure locale\-independent output parsing \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11775](https\://github\.com/ansible\-collections/community\.general/pull/11775)\)\.
* lvol \- fix LVM version parsing \([https\://github\.com/ansible\-collections/community\.general/issues/5445](https\://github\.com/ansible\-collections/community\.general/issues/5445)\, [https\://github\.com/ansible\-collections/community\.general/pull/11823](https\://github\.com/ansible\-collections/community\.general/pull/11823)\)\.
* lvol \- normalize locale environment for <code>run\_command\(\)</code> calls to <code>LANGUAGE\=C</code>\, <code>LC\_ALL\=C</code> \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11740](https\://github\.com/ansible\-collections/community\.general/pull/11740)\)\.
* lxc\_container \- set <code>LANGUAGE</code> and <code>LC\_ALL</code> to <code>C</code> in <code>run\_command\(\)</code> calls to ensure locale\-independent output parsing \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11779](https\://github\.com/ansible\-collections/community\.general/pull/11779)\)\.
* machinectl become plugin \- prevent printing ANSI terminal color sequences \([https\://github\.com/ansible\-collections/community\.general/pull/11771](https\://github\.com/ansible\-collections/community\.general/pull/11771)\)\.
* macports \- ensure <code>LANGUAGE\=C</code> and <code>LC\_ALL\=C</code> are set when running commands that parse output \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11768](https\://github\.com/ansible\-collections/community\.general/pull/11768)\)\.
* mas \- set <code>LANGUAGE</code> and <code>LC\_ALL</code> to <code>C</code> in <code>run\_command\(\)</code> calls to ensure locale\-independent output parsing \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11775](https\://github\.com/ansible\-collections/community\.general/pull/11775)\)\.
* modprobe \- ensure <code>LANGUAGE\=C</code> and <code>LC\_ALL\=C</code> are set when running commands that parse output \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11768](https\://github\.com/ansible\-collections/community\.general/pull/11768)\)\.
* monit \- ensure <code>LANGUAGE\=C</code> and <code>LC\_ALL\=C</code> are set when running commands that parse output \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11768](https\://github\.com/ansible\-collections/community\.general/pull/11768)\)\.
* mssql\_db \- fail with a clear error message when a named instance \(<code>server\\instance</code> format\) is used together with <code>login\_port</code>\, since these are mutually exclusive connection methods \([https\://github\.com/ansible\-collections/community\.general/issues/5693](https\://github\.com/ansible\-collections/community\.general/issues/5693)\, [https\://github\.com/ansible\-collections/community\.general/pull/11664](https\://github\.com/ansible\-collections/community\.general/pull/11664)\)\.
* mssql\_script \- fail with a clear error message when a named instance \(<code>server\\instance</code> format\) is used together with <code>login\_port</code>\, since these are mutually exclusive connection methods \([https\://github\.com/ansible\-collections/community\.general/issues/5693](https\://github\.com/ansible\-collections/community\.general/issues/5693)\, [https\://github\.com/ansible\-collections/community\.general/pull/11664](https\://github\.com/ansible\-collections/community\.general/pull/11664)\)\.
* mssql\_script \- only passes <code>params</code> to <code>cursor\.execute\(\)</code> when the user actually provides them \([https\://github\.com/ansible\-collections/community\.general/issues/11699](https\://github\.com/ansible\-collections/community\.general/issues/11699)\, [https\://github\.com/ansible\-collections/community\.general/pull/11754](https\://github\.com/ansible\-collections/community\.general/pull/11754)\)\.
* nmcli \- use <code>get\_best\_parsable\_locale\(\)</code> to set locale environment for <code>run\_command\(\)</code> calls\, fixing UTF\-8 connection names being corrupted to <code>\?\?\?\?</code> under <code>LC\_ALL\=C</code> \([https\://github\.com/ansible\-collections/community\.general/issues/10384](https\://github\.com/ansible\-collections/community\.general/issues/10384)\, [https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11742](https\://github\.com/ansible\-collections/community\.general/pull/11742)\)\.
* nsupdate \- fix GSS\-TSIG support \(accidentally broken by [https\://github\.com/ansible\-collections/community\.general/pull/11461](https\://github\.com/ansible\-collections/community\.general/pull/11461)\, [https\://github\.com/ansible\-collections/community\.general/pull/11712](https\://github\.com/ansible\-collections/community\.general/pull/11712)\)
* ohai \- set <code>LANGUAGE</code> and <code>LC\_ALL</code> to <code>C</code> in <code>run\_command\(\)</code> calls to ensure locale\-independent output parsing \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11785](https\://github\.com/ansible\-collections/community\.general/pull/11785)\)\.
* onepassword\_info \- set <code>LANGUAGE</code> and <code>LC\_ALL</code> to <code>C</code> in <code>run\_command\(\)</code> calls to ensure locale\-independent output parsing \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11786](https\://github\.com/ansible\-collections/community\.general/pull/11786)\)\.
* open\_iscsi \- ensure <code>LANGUAGE\=C</code> and <code>LC\_ALL\=C</code> are set when running commands that parse output \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11768](https\://github\.com/ansible\-collections/community\.general/pull/11768)\)\.
* openbsd\_pkg \- ensure <code>LANGUAGE\=C</code> and <code>LC\_ALL\=C</code> are set when running commands that parse output \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11767](https\://github\.com/ansible\-collections/community\.general/pull/11767)\)\.
* openwrt\_init \- set <code>LANGUAGE</code> and <code>LC\_ALL</code> to <code>C</code> in <code>run\_command\(\)</code> calls to ensure locale\-independent output parsing \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11784](https\://github\.com/ansible\-collections/community\.general/pull/11784)\)\.
* osx\_defaults \- set <code>LANGUAGE</code> and <code>LC\_ALL</code> to <code>C</code> in <code>run\_command\(\)</code> calls to ensure locale\-independent output parsing \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11775](https\://github\.com/ansible\-collections/community\.general/pull/11775)\)\.
* pacemaker\_resource\, pacemaker\_stonith \- fix resource and stonith creation race condition by polling PCS status \([https\://github\.com/ansible\-collections/community\.general/issues/11574](https\://github\.com/ansible\-collections/community\.general/issues/11574)\, [https\://github\.com/ansible\-collections/community\.general/pull/11750](https\://github\.com/ansible\-collections/community\.general/pull/11750)\)\.
* pacman \- normalize locale environment for <code>run\_command\(\)</code> calls to <code>LANGUAGE\=C</code>\, <code>LC\_ALL\=C</code> \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11740](https\://github\.com/ansible\-collections/community\.general/pull/11740)\)\.
* pacman\_key \- ensure <code>LANGUAGE\=C</code> and <code>LC\_ALL\=C</code> are set when running commands that parse output \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11768](https\://github\.com/ansible\-collections/community\.general/pull/11768)\)\.
* parted \- normalize locale environment for <code>run\_command\(\)</code> calls to <code>LANGUAGE\=C</code>\, <code>LC\_ALL\=C</code> \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11740](https\://github\.com/ansible\-collections/community\.general/pull/11740)\)\.
* pear \- set <code>LANGUAGE</code> and <code>LC\_ALL</code> to <code>C</code> in <code>run\_command\(\)</code> calls to ensure locale\-independent output parsing \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11782](https\://github\.com/ansible\-collections/community\.general/pull/11782)\)\.
* pip\_package\_info \- set <code>LANGUAGE</code> and <code>LC\_ALL</code> to <code>C</code> in <code>run\_command\(\)</code> calls to ensure locale\-independent output parsing \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11784](https\://github\.com/ansible\-collections/community\.general/pull/11784)\)\.
* pkg5 \- set <code>LANGUAGE</code> and <code>LC\_ALL</code> to <code>C</code> in <code>run\_command\(\)</code> calls to ensure locale\-independent output parsing \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11780](https\://github\.com/ansible\-collections/community\.general/pull/11780)\)\.
* pkg5\_publisher \- set <code>LANGUAGE</code> and <code>LC\_ALL</code> to <code>C</code> in <code>run\_command\(\)</code> calls to ensure locale\-independent output parsing \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11780](https\://github\.com/ansible\-collections/community\.general/pull/11780)\)\.
* pkgin \- normalize locale environment for <code>run\_command\(\)</code> calls to <code>LANGUAGE\=C</code>\, <code>LC\_ALL\=C</code> \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11741](https\://github\.com/ansible\-collections/community\.general/pull/11741)\)\.
* pkgng \- ensure <code>LANGUAGE\=C</code> and <code>LC\_ALL\=C</code> are set when running commands that parse output \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11765](https\://github\.com/ansible\-collections/community\.general/pull/11765)\)\.
* pkgutil \- set <code>LANGUAGE</code> and <code>LC\_ALL</code> to <code>C</code> in <code>run\_command\(\)</code> calls to ensure locale\-independent output parsing \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11775](https\://github\.com/ansible\-collections/community\.general/pull/11775)\)\.
* pnpm \- set <code>LANGUAGE</code> and <code>LC\_ALL</code> to <code>C</code> in <code>run\_command\(\)</code> calls to ensure locale\-independent output parsing \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11776](https\://github\.com/ansible\-collections/community\.general/pull/11776)\)\.
* portage \- set <code>LANGUAGE</code> and <code>LC\_ALL</code> to <code>C</code> in <code>run\_command\(\)</code> calls to ensure locale\-independent output parsing \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11781](https\://github\.com/ansible\-collections/community\.general/pull/11781)\)\.
* portinstall \- set <code>LANGUAGE</code> and <code>LC\_ALL</code> to <code>C</code> in <code>run\_command\(\)</code> calls to ensure locale\-independent output parsing \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11781](https\://github\.com/ansible\-collections/community\.general/pull/11781)\)\.
* redhat\_subscription \- normalize locale environment for <code>run\_command\(\)</code> calls to <code>LANGUAGE\=C</code>\, <code>LC\_ALL\=C</code> \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11741](https\://github\.com/ansible\-collections/community\.general/pull/11741)\)\.
* rhsm\_release \- ensure <code>LANGUAGE\=C</code> and <code>LC\_ALL\=C</code> are set when running commands that parse output \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11768](https\://github\.com/ansible\-collections/community\.general/pull/11768)\)\.
* rhsm\_repository \- normalize locale environment for <code>run\_command\(\)</code> calls to <code>LANGUAGE\=C</code>\, <code>LC\_ALL\=C</code> \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11741](https\://github\.com/ansible\-collections/community\.general/pull/11741)\)\.
* riak \- set <code>LANGUAGE</code> and <code>LC\_ALL</code> to <code>C</code> in <code>run\_command\(\)</code> calls to ensure locale\-independent output parsing \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11786](https\://github\.com/ansible\-collections/community\.general/pull/11786)\)\.
* rpm\_ostree\_pkg \- ensure <code>LANGUAGE\=C</code> and <code>LC\_ALL\=C</code> are set when running commands that parse output \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11768](https\://github\.com/ansible\-collections/community\.general/pull/11768)\)\.
* run0 become plugin \- mark the plugin as incompatible with connection pipelining \(see [https\://github\.com/ansible/ansible/issues/81254](https\://github\.com/ansible/ansible/issues/81254)\, [https\://github\.com/ansible\-collections/community\.general/pull/11771](https\://github\.com/ansible\-collections/community\.general/pull/11771)\)\.
* run0 become plugin \- prevent printing ANSI terminal color sequences \([https\://github\.com/ansible\-collections/community\.general/pull/11771](https\://github\.com/ansible\-collections/community\.general/pull/11771)\)\.
* runit \- normalize locale environment for <code>run\_command\(\)</code> calls to <code>LANGUAGE\=C</code>\, <code>LC\_ALL\=C</code> \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11741](https\://github\.com/ansible\-collections/community\.general/pull/11741)\)\.
* sefcontext \- flush the in\-process <code>matchpathcon</code> cache after applying changes\, so subsequent tasks running in the same process \(for example via the Mitogen connection plugin\) see the updated SELinux file context rules instead of stale cached data \([https\://github\.com/ansible\-collections/community\.general/issues/888](https\://github\.com/ansible\-collections/community\.general/issues/888)\, [https\://github\.com/ansible\-collections/community\.general/pull/11812](https\://github\.com/ansible\-collections/community\.general/pull/11812)\)\.
* smartos\_image\_info \- set <code>LANGUAGE</code> and <code>LC\_ALL</code> to <code>C</code> in <code>run\_command\(\)</code> calls to ensure locale\-independent output parsing \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11781](https\://github\.com/ansible\-collections/community\.general/pull/11781)\)\.
* snmp\_facts \- the module now also supports pysnmp \>\= 7\.1 \([https\://github\.com/ansible\-collections/community\.general/issues/8852](https\://github\.com/ansible\-collections/community\.general/issues/8852)\, [https\://github\.com/ansible\-collections/community\.general/pull/11683](https\://github\.com/ansible\-collections/community\.general/pull/11683)\)\.
* sorcery \- ensure <code>LANGUAGE\=C</code> and <code>LC\_ALL\=C</code> are set when running commands that parse output \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11767](https\://github\.com/ansible\-collections/community\.general/pull/11767)\)\.
* supervisorctl \- normalize locale environment for <code>run\_command\(\)</code> calls to <code>LANGUAGE\=C</code>\, <code>LC\_ALL\=C</code> \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11741](https\://github\.com/ansible\-collections/community\.general/pull/11741)\)\.
* svc \- normalize locale environment for <code>run\_command\(\)</code> calls to <code>LANGUAGE\=C</code>\, <code>LC\_ALL\=C</code> \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11741](https\://github\.com/ansible\-collections/community\.general/pull/11741)\)\.
* swdepot \- set <code>LANGUAGE</code> and <code>LC\_ALL</code> to <code>C</code> in <code>run\_command\(\)</code> calls to ensure locale\-independent output parsing \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11780](https\://github\.com/ansible\-collections/community\.general/pull/11780)\)\.
* syspatch \- set <code>LANGUAGE</code> and <code>LC\_ALL</code> to <code>C</code> in <code>run\_command\(\)</code> calls to ensure locale\-independent output parsing \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11781](https\://github\.com/ansible\-collections/community\.general/pull/11781)\)\.
* sysrc \- set <code>LANGUAGE</code> and <code>LC\_ALL</code> to <code>C</code> in <code>run\_command\(\)</code> calls to ensure locale\-independent output parsing \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11776](https\://github\.com/ansible\-collections/community\.general/pull/11776)\)\.
* sysupgrade \- ensure <code>LANGUAGE\=C</code> and <code>LC\_ALL\=C</code> are set when running commands that parse output \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11768](https\://github\.com/ansible\-collections/community\.general/pull/11768)\)\.
* terraform \- ensure <code>LANGUAGE\=C</code> and <code>LC\_ALL\=C</code> are set when running commands that parse output \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11765](https\://github\.com/ansible\-collections/community\.general/pull/11765)\)\.
* timezone \- set <code>LANGUAGE</code> and <code>LC\_ALL</code> to <code>C</code> in <code>run\_command\(\)</code> calls to ensure locale\-independent output parsing \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11776](https\://github\.com/ansible\-collections/community\.general/pull/11776)\)\.
* udm\_user \- allow to use passlib instead of legacycrypt for Python 3\.13\+ \([https\://github\.com/ansible\-collections/community\.general/issues/4690](https\://github\.com/ansible\-collections/community\.general/issues/4690)\, [https\://github\.com/ansible\-collections/community\.general/pull/11860](https\://github\.com/ansible\-collections/community\.general/pull/11860)\)\.
* udm\_user \- fix alias\-to\-canonical parameter name mismatch that caused all camelCase\-aliased parameters such as <code>display\_name</code> and <code>primary\_group</code> to be silently ignored \([https\://github\.com/ansible\-collections/community\.general/issues/2950](https\://github\.com/ansible\-collections/community\.general/issues/2950)\, [https\://github\.com/ansible\-collections/community\.general/issues/3691](https\://github\.com/ansible\-collections/community\.general/issues/3691)\, [https\://github\.com/ansible\-collections/community\.general/pull/11859](https\://github\.com/ansible\-collections/community\.general/pull/11859)\)\.
* ufw \- normalize locale environment for <code>run\_command\(\)</code> calls to <code>LANGUAGE\=C</code>\, <code>LC\_ALL\=C</code> \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11741](https\://github\.com/ansible\-collections/community\.general/pull/11741)\)\.
* xattr \- set <code>LANGUAGE</code> and <code>LC\_ALL</code> to <code>C</code> in <code>run\_command\(\)</code> calls to ensure locale\-independent output parsing \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11776](https\://github\.com/ansible\-collections/community\.general/pull/11776)\)\.
* xbps \- set <code>LANGUAGE</code> and <code>LC\_ALL</code> to <code>C</code> in <code>run\_command\(\)</code> calls to ensure locale\-independent output parsing \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11781](https\://github\.com/ansible\-collections/community\.general/pull/11781)\)\.
* xenserver\_guest \- fix an issue where booting from ISO is not possible because CD\-ROM device is placed in position above number 3\. Position number 3 is now reserved for CD\-ROM device and cannot be occupied by a disk \([https\://github\.com/ansible\-collections/community\.general/issues/11624](https\://github\.com/ansible\-collections/community\.general/issues/11624)\, [https\://github\.com/ansible\-collections/community\.general/pull/11702](https\://github\.com/ansible\-collections/community\.general/pull/11702)\)\.
* yarn \- set <code>LANGUAGE</code> and <code>LC\_ALL</code> to <code>C</code> in <code>run\_command\(\)</code> calls to ensure locale\-independent output parsing \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11776](https\://github\.com/ansible\-collections/community\.general/pull/11776)\)\.
* yum\_versionlock \- set <code>LANGUAGE</code> and <code>LC\_ALL</code> to <code>C</code> in <code>run\_command\(\)</code> calls to ensure locale\-independent output parsing \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11777](https\://github\.com/ansible\-collections/community\.general/pull/11777)\)\.
* zfs \- set <code>LANGUAGE</code> and <code>LC\_ALL</code> to <code>C</code> in <code>run\_command\(\)</code> calls to ensure locale\-independent output parsing \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11778](https\://github\.com/ansible\-collections/community\.general/pull/11778)\)\.
* zfs\_delegate\_admin \- set <code>LANGUAGE</code> and <code>LC\_ALL</code> to <code>C</code> in <code>run\_command\(\)</code> calls to ensure locale\-independent output parsing \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11778](https\://github\.com/ansible\-collections/community\.general/pull/11778)\)\.
* zfs\_facts \- set <code>LANGUAGE</code> and <code>LC\_ALL</code> to <code>C</code> in <code>run\_command\(\)</code> calls to ensure locale\-independent output parsing \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11778](https\://github\.com/ansible\-collections/community\.general/pull/11778)\)\.
* zpool\_facts \- set <code>LANGUAGE</code> and <code>LC\_ALL</code> to <code>C</code> in <code>run\_command\(\)</code> calls to ensure locale\-independent output parsing \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11778](https\://github\.com/ansible\-collections/community\.general/pull/11778)\)\.
* zypper \- normalize locale environment for <code>run\_command\(\)</code> calls to <code>LANGUAGE\=C</code>\, <code>LC\_ALL\=C</code> \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11741](https\://github\.com/ansible\-collections/community\.general/pull/11741)\)\.
* zypper\_repository \- set <code>LANGUAGE</code> and <code>LC\_ALL</code> to <code>C</code> in <code>run\_command\(\)</code> calls to ensure locale\-independent output parsing \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11777](https\://github\.com/ansible\-collections/community\.general/pull/11777)\)\.
* zypper\_repository\_info \- set <code>LANGUAGE</code> and <code>LC\_ALL</code> to <code>C</code> in <code>run\_command\(\)</code> calls to ensure locale\-independent output parsing \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11782](https\://github\.com/ansible\-collections/community\.general/pull/11782)\)\.

<a id="community-libvirt-1"></a>
#### community\.libvirt

* libvirt\_qemu \- Vendor <code>\_parse\_clixml</code> locally to fix <code>ImportError</code> on ansible\-core devel \(2\.21\+\)\.

<a id="community-zabbix-1"></a>
#### community\.zabbix

* Added \'status\' handling to sanatize\_params in zabbix\_itemprototype module to allow for \'enabled\'/\'disabled\' values\.
* Updated tests to reflect the change in parameter handling\.
* add zabbix\_agent 7\.4 as valid for windows
* all modules \- fixed password handeling
* fix zabbix\_agent\_version\_long version comparison
* server role \- fixed issues with mysql import
* use architecture2 in map for amd64/i386
* web role \- Fixed ownership of <em class="title-reference">/etc/zabbix/web</em> directory to match Debian distributions packages
* zabbix\_agent \- add fallback to first ipv4 address if default cant be determined for zabbix\_agent\_ip
* zabbix\_proxy \- add fallback to first ipv4 address if default cant be determined for zabbix\_proxy\_ip
* zabbix\_server \- Adapt all the PostgresDB related task to be schema aware \([https\://github\.com/ansible\-collections/community\.zabbix/issues/1647](https\://github\.com/ansible\-collections/community\.zabbix/issues/1647)\)\.
* zabbix\_template \- prevent false reporting of password change
* zabbix\_trigger \- add selectDependencies and selectTags when requesting triggers to detect changes to those values
* zabbix\_valuemap \- add missing host\_name option which is required by the Zabbix API \([https\://github\.com/ansible\-collections/community\.zabbix/issues/1636](https\://github\.com/ansible\-collections/community\.zabbix/issues/1636)\)\.
* zabbix\_web \- define zabbix\_server\_dbschema default value
* zabbix\_web \- nginx vhost template did not support http2 configuration \([https\://github\.com/ansible\-collections/community\.zabbix/issues/1668](https\://github\.com/ansible\-collections/community\.zabbix/issues/1668)\)\.

<a id="containers-podman-1"></a>
#### containers\.podman

* podman\_container \- Fix quadlet\_options placement when restart\_policy is set
* podman\_network \- Add diff and idempotency to ip\_ranges in net\_config

<a id="dellemc-openmanage-1"></a>
#### dellemc\.openmanage

* idrac\_job\_queue \- \(Issue 1067\) \- Fails to find the file in role due to incorrect name \([https\://github\.com/dell/dellemc\-openmanage\-ansible\-modules/issues/1067](https\://github\.com/dell/dellemc\-openmanage\-ansible\-modules/issues/1067)\)
* idrac\_system\_info \- \(Issue 1044\) \- FC section is missing \([https\://github\.com/dell/dellemc\-openmanage\-ansible\-modules/issues/1044](https\://github\.com/dell/dellemc\-openmanage\-ansible\-modules/issues/1044)\)
* idrac\_system\_info \- powersupply\.get\_red\_type\_set fails with TypeError due to unhandled None values when joining mapped redundancy types
* idrac\_user \- \(Issue 1059\) \- Bad User Privileges when creating idrac user using \"custom\_privilege\" \([https\://github\.com/dell/dellemc\-openmanage\-ansible\-modules/issues/1059](https\://github\.com/dell/dellemc\-openmanage\-ansible\-modules/issues/1059)\)

<a id="fortinet-fortios-1"></a>
#### fortinet\.fortios

* Fixed an issue where parameters ending with \_dict always returned changed\, even in check mode or when no changes were made\.
* Fixed an issue where some modules could not be configured globally\.
* Fixed an issue where the generate\-key\.system\.api\-user selector in the fortios\_monitor module required an admin password to function\.

<a id="ibm-storage-virtualize-1"></a>
#### ibm\.storage\_virtualize

* ibm\_svc\_manage\_ip \- Fixed issue related to VLAN while updating

<a id="known-issues"></a>
### Known Issues

<a id="dellemc-openmanage-2"></a>
#### dellemc\.openmanage

* Formal qualification of module ome\_smart\_fabric\_info for Ansible Core version 2\.19 is still pending\.
* idrac\_diagnostics \- This module does not support export of diagnostics file to HTTP and HTTPS share via SOCKS proxy\.
* idrac\_license \- Due to API limitation\, proxy parameters are ignored during the import operation\.
* idrac\_license \- The module will give different error messages for iDRAC9 and iDRAC10 when user imports license with invalid share name\.
* idrac\_os\_deployment \- The module continues to return a 200 response and marks the job as completed\, even when an outdated date is supplied in the Expose duration\.
* idrac\_redfish\_storage\_controller \- PatrolReadRatePercent attribute cannot be set in iDRAC10\.
* idrac\_server\_config\_profile \- When attempting to revert iDRAC settings using a previously exported SCP file\, the import operation will complete with errors if a new user was created after the export \(Instead of restoring the system to its previous state\, including the removal of newly added users\)\.
* ome\_smart\_fabric\_uplink \- The module supported by OpenManage Enterprise Modular\, however it does not allow the creation of multiple uplinks of the same name\. If an uplink is created using the same name as an existing uplink\, then the existing uplink is modified\.
* redfish\_storage\_volume \- Encryption type and block\_io\_size bytes will be read only property in iDRAC9 and iDRAC10 and hence the module ignores these parameters\.

<a id="new-plugins"></a>
### New Plugins

<a id="filter"></a>
#### Filter

* community\.crypto\.acme\_dns\_persist\_record \- Craft a DNS record for ACME <code>dns\-persist\-01</code> challenges\.
* community\.crypto\.acme\_dns\_persist\_record\_parse \- Parse a DNS record for ACME <code>dns\-persist\-01</code> challenges\.

<a id="new-modules"></a>
### New Modules

<a id="community-general-2"></a>
#### community\.general

* community\.general\.snap\_connect \- Manages snap interface connections\.

<a id="unchanged-collections"></a>
### Unchanged Collections

* amazon\.aws \(still version 10\.3\.0\)
* ansible\.posix \(still version 2\.1\.0\)
* ansible\.windows \(still version 3\.5\.0\)
* arista\.eos \(still version 12\.0\.1\)
* awx\.awx \(still version 24\.6\.1\)
* azure\.azcollection \(still version 3\.16\.0\)
* check\_point\.mgmt \(still version 6\.9\.0\)
* cisco\.aci \(still version 2\.13\.0\)
* cisco\.dnac \(still version 6\.48\.0\)
* cisco\.ios \(still version 11\.3\.0\)
* cisco\.mso \(still version 2\.13\.0\)
* cisco\.nxos \(still version 11\.1\.3\)
* cisco\.ucs \(still version 1\.16\.0\)
* cloudscale\_ch\.cloud \(still version 2\.5\.3\)
* community\.aws \(still version 10\.1\.0\)
* community\.ciscosmb \(still version 1\.0\.11\)
* community\.clickhouse \(still version 2\.1\.0\)
* community\.grafana \(still version 2\.3\.0\)
* community\.hashi\_vault \(still version 7\.1\.0\)
* community\.hrobot \(still version 2\.7\.1\)
* community\.library\_inventory\_filtering\_v1 \(still version 1\.1\.5\)
* community\.mongodb \(still version 1\.7\.12\)
* community\.mysql \(still version 4\.2\.0\)
* community\.okd \(still version 5\.0\.0\)
* community\.postgresql \(still version 4\.2\.0\)
* community\.proxmox \(still version 1\.6\.0\)
* community\.proxysql \(still version 1\.7\.0\)
* community\.rabbitmq \(still version 1\.6\.0\)
* community\.sap\_libs \(still version 1\.7\.0\)
* community\.vmware \(still version 6\.2\.0\)
* community\.windows \(still version 3\.1\.0\)
* cyberark\.conjur \(still version 1\.3\.9\)
* cyberark\.pas \(still version 1\.0\.39\)
* dellemc\.enterprise\_sonic \(still version 3\.2\.0\)
* dellemc\.powerflex \(still version 3\.0\.0\)
* dellemc\.unity \(still version 2\.1\.0\)
* f5networks\.f5\_modules \(still version 1\.39\.0\)
* fortinet\.fortimanager \(still version 2\.13\.0\)
* grafana\.grafana \(still version 6\.0\.6\)
* hetzner\.hcloud \(still version 6\.8\.0\)
* hitachivantara\.vspone\_block \(still version 4\.6\.1\)
* hitachivantara\.vspone\_object \(still version 1\.1\.1\)
* ieisystem\.inmanage \(still version 4\.0\.0\)
* infinidat\.infinibox \(still version 1\.6\.3\)
* infoblox\.nios\_modules \(still version 1\.9\.0\)
* inspur\.ispim \(still version 2\.2\.4\)
* junipernetworks\.junos \(still version 11\.0\.0\)
* kaytus\.ksmanage \(still version 2\.0\.0\)
* kubernetes\.core \(still version 6\.3\.0\)
* kubevirt\.core \(still version 2\.2\.4\)
* microsoft\.ad \(still version 1\.10\.0\)
* microsoft\.iis \(still version 1\.1\.0\)
* netapp\.cloudmanager \(still version 21\.24\.0\)
* netapp\.ontap \(still version 23\.4\.0\)
* netapp\.storagegrid \(still version 21\.16\.0\)
* netapp\_eseries\.santricity \(still version 1\.4\.1\)
* netbox\.netbox \(still version 3\.22\.0\)
* ngine\_io\.cloudstack \(still version 3\.0\.0\)
* openstack\.cloud \(still version 2\.5\.0\)
* ovirt\.ovirt \(still version 3\.2\.2\)
* pcg\.alpaca\_operator \(still version 2\.2\.0\)
* purestorage\.flasharray \(still version 1\.42\.0\)
* purestorage\.flashblade \(still version 1\.24\.0\)
* ravendb\.ravendb \(still version 1\.0\.4\)
* splunk\.es \(still version 4\.0\.0\)
* telekom\_mms\.icinga\_director \(still version 2\.5\.1\)
* vmware\.vmware \(still version 2\.8\.0\)
* vmware\.vmware\_rest \(still version 4\.10\.0\)
* vultr\.cloud \(still version 1\.14\.0\)
* vyos\.vyos \(still version 6\.0\.0\)
* wti\.remote \(still version 1\.0\.11\)

<a id="v13-5-0"></a>
## v13\.5\.0

- <a href="#release-summary-1">Release Summary</a>
- <a href="#added-collections">Added Collections</a>
- <a href="#ansible-core-3">Ansible\-core</a>
- <a href="#changed-collections-1">Changed Collections</a>
- <a href="#major-changes-1">Major Changes</a>
    - <a href="#community-proxmox">community\.proxmox</a>
    - <a href="#community-routeros-2">community\.routeros</a>
    - <a href="#fortinet-fortios-2">fortinet\.fortios</a>
    - <a href="#netapp-ontap">netapp\.ontap</a>
- <a href="#minor-changes-1">Minor Changes</a>
    - <a href="#ansible-core-4">Ansible\-core</a>
    - <a href="#amazon-aws">amazon\.aws</a>
    - <a href="#ansible-windows">ansible\.windows</a>
    - <a href="#cisco-meraki-1">cisco\.meraki</a>
    - <a href="#cisco-mso">cisco\.mso</a>
    - <a href="#community-clickhouse">community\.clickhouse</a>
    - <a href="#community-docker-1">community\.docker</a>
    - <a href="#community-general-3">community\.general</a>
    - <a href="#community-mysql">community\.mysql</a>
    - <a href="#community-proxmox-1">community\.proxmox</a>
    - <a href="#community-routeros-3">community\.routeros</a>
    - <a href="#community-sap-libs">community\.sap\_libs</a>
    - <a href="#fortinet-fortimanager">fortinet\.fortimanager</a>
    - <a href="#google-cloud-1">google\.cloud</a>
    - <a href="#hetzner-hcloud">hetzner\.hcloud</a>
    - <a href="#netapp-ontap-1">netapp\.ontap</a>
    - <a href="#theforeman-foreman-1">theforeman\.foreman</a>
    - <a href="#vmware-vmware">vmware\.vmware</a>
    - <a href="#vultr-cloud">vultr\.cloud</a>
- <a href="#breaking-changes--porting-guide">Breaking Changes / Porting Guide</a>
    - <a href="#community-mysql-1">community\.mysql</a>
    - <a href="#community-proxmox-2">community\.proxmox</a>
- <a href="#deprecated-features-1">Deprecated Features</a>
    - <a href="#community-general-4">community\.general</a>
    - <a href="#community-proxmox-3">community\.proxmox</a>
- <a href="#security-fixes">Security Fixes</a>
    - <a href="#amazon-aws-1">amazon\.aws</a>
    - <a href="#ansible-windows-1">ansible\.windows</a>
- <a href="#bugfixes-1">Bugfixes</a>
    - <a href="#ansible-core-5">Ansible\-core</a>
    - <a href="#amazon-aws-2">amazon\.aws</a>
    - <a href="#ansible-windows-2">ansible\.windows</a>
    - <a href="#cisco-meraki-2">cisco\.meraki</a>
    - <a href="#community-dns-1">community\.dns</a>
    - <a href="#community-general-5">community\.general</a>
    - <a href="#community-hrobot">community\.hrobot</a>
    - <a href="#community-mysql-2">community\.mysql</a>
    - <a href="#community-proxmox-4">community\.proxmox</a>
    - <a href="#community-routeros-4">community\.routeros</a>
    - <a href="#fortinet-fortios-3">fortinet\.fortios</a>
    - <a href="#netapp-ontap-2">netapp\.ontap</a>
    - <a href="#theforeman-foreman-2">theforeman\.foreman</a>
    - <a href="#vmware-vmware-1">vmware\.vmware</a>
    - <a href="#vultr-cloud-1">vultr\.cloud</a>
- <a href="#known-issues-1">Known Issues</a>
    - <a href="#community-routeros-5">community\.routeros</a>
- <a href="#new-modules-1">New Modules</a>
    - <a href="#ansible-windows-3">ansible\.windows</a>
    - <a href="#cisco-mso-1">cisco\.mso</a>
    - <a href="#community-general-6">community\.general</a>
    - <a href="#community-proxmox-5">community\.proxmox</a>
    - <a href="#fortinet-fortimanager-1">fortinet\.fortimanager</a>
    - <a href="#netapp-ontap-3">netapp\.ontap</a>
    - <a href="#theforeman-foreman-3">theforeman\.foreman</a>
    - <a href="#vultr-cloud-2">vultr\.cloud</a>
- <a href="#unchanged-collections-1">Unchanged Collections</a>

<a id="release-summary-1"></a>
### Release Summary

Release Date\: 2026\-03\-25

[Porting Guide](https\://docs\.ansible\.com/projects/ansible/devel/porting\_guides\.html)

<a id="added-collections"></a>
### Added Collections

* graphiant\.naas \(version 26\.2\.4\)

<a id="ansible-core-3"></a>
### Ansible\-core

Ansible 13\.5\.0 contains ansible\-core version 2\.20\.4\.
This is a newer version than version 2\.20\.3 contained in the previous Ansible release\.

The changes are reported in the combined changelog below\.

<a id="changed-collections-1"></a>
### Changed Collections

If not mentioned explicitly\, the changes are reported in the combined changelog below\.

| Collection            | Ansible 13.4.0 | Ansible 13.5.0 | Notes                                                                                                                        |
| --------------------- | -------------- | -------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| amazon.aws            | 10.2.0         | 10.3.0         |                                                                                                                              |
| ansible.windows       | 3.3.0          | 3.5.0          |                                                                                                                              |
| azure.azcollection    | 3.14.0         | 3.16.0         | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
| check_point.mgmt      | 6.8.0          | 6.9.0          | The collection did not have a changelog in this version.                                                                     |
| cisco.intersight      | 2.12.0         | 2.16.0         | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
| cisco.meraki          | 2.22.1         | 2.23.1         |                                                                                                                              |
| cisco.mso             | 2.12.0         | 2.13.0         |                                                                                                                              |
| community.clickhouse  | 2.0.0          | 2.1.0          |                                                                                                                              |
| community.dns         | 3.5.2          | 3.5.3          |                                                                                                                              |
| community.docker      | 5.0.6          | 5.1.0          |                                                                                                                              |
| community.general     | 12.4.0         | 12.5.0         |                                                                                                                              |
| community.hrobot      | 2.7.0          | 2.7.1          |                                                                                                                              |
| community.mysql       | 4.1.0          | 4.2.0          |                                                                                                                              |
| community.proxmox     | 1.5.0          | 1.6.0          |                                                                                                                              |
| community.routeros    | 3.16.0         | 3.18.0         |                                                                                                                              |
| community.sap_libs    | 1.6.0          | 1.7.0          |                                                                                                                              |
| cyberark.pas          | 1.0.36         | 1.0.39         | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
| fortinet.fortimanager | 2.12.0         | 2.13.0         |                                                                                                                              |
| fortinet.fortios      | 2.4.2          | 2.5.0          |                                                                                                                              |
| google.cloud          | 1.11.0         | 1.12.0         |                                                                                                                              |
| graphiant.naas        |                | 26.2.4         | The collection was added to Ansible                                                                                          |
| hetzner.hcloud        | 6.7.0          | 6.8.0          |                                                                                                                              |
| kubevirt.core         | 2.2.3          | 2.2.4          | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
| netapp.ontap          | 23.3.0         | 23.4.0         |                                                                                                                              |
| theforeman.foreman    | 5.8.0          | 5.10.0         |                                                                                                                              |
| vmware.vmware         | 2.7.0          | 2.8.0          |                                                                                                                              |
| vultr.cloud           | 1.13.0         | 1.14.0         |                                                                                                                              |
| wti.remote            | 1.0.10         | 1.0.11         | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |

<a id="major-changes-1"></a>
### Major Changes

<a id="community-proxmox"></a>
#### community\.proxmox

* proxmox \- Add ca\_path option to specify a ca\-certificate for tls validation \([https\://github\.com/ansible\-collections/community\.proxmox/pull/256](https\://github\.com/ansible\-collections/community\.proxmox/pull/256)\)\.

<a id="community-routeros-2"></a>
#### community\.routeros

* api\_info\, api\_modify \- multiple parameters can no longer be disabled for the\`\`tool netwatch\`\` path \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- parameter <code>name\-format</code> can no longer be disabled for the <code>interface wifi provisioning</code> path \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- parameter <code>script</code> can no longer be disabled for the <code>ip dhcp\-client</code> path \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.

<a id="fortinet-fortios-2"></a>
#### fortinet\.fortios

* Supported new versions 7\.6\.5 and 7\.6\.6\.
* Updated the Q\&A for using the default\_group feature in modules\.

<a id="netapp-ontap"></a>
#### netapp\.ontap

* na\_ontap\_autoupdate\_config \- REST only support for managing configurations for automatic updates\, requires ONTAP 9\.10\.1 or later\.
* na\_ontap\_cg \- REST only support for managing consistency groups\, requires ONTAP 9\.10\.1 or later\.
* na\_ontap\_cifs \- AWS Lambda support added to the module\.
* na\_ontap\_cifs\_acl \- AWS Lambda support added to the module\.
* na\_ontap\_cifs\_local\_group \- AWS Lambda support added to the module\.
* na\_ontap\_cifs\_local\_group\_member \- AWS Lambda support added to the module\.
* na\_ontap\_cifs\_local\_user \- AWS Lambda support added to the module\.
* na\_ontap\_cifs\_local\_user\_set\_password \- AWS Lambda support added to the module\.
* na\_ontap\_cifs\_privileges \- AWS Lambda support added to the module\.
* na\_ontap\_cifs\_server \- AWS Lambda support added to the module\.
* na\_ontap\_cifs\_unix\_symlink\_mapping \- AWS Lambda support added to the module\.
* na\_ontap\_cluster\_peer \- AWS Lambda support added to the module\.
* na\_ontap\_igroup \- AWS Lambda support added to the module\.
* na\_ontap\_igroup\_initiator \- AWS Lambda support added to the module\.
* na\_ontap\_lun\_copy \- AWS Lambda support added to the module\.
* na\_ontap\_lun\_map \- AWS Lambda support added to the module\.
* na\_ontap\_lun\_map\_reporting\_nodes \- AWS Lambda support added to the module\.
* na\_ontap\_s3\_buckets \- AWS Lambda support added to the module\.
* na\_ontap\_s3\_groups \- AWS Lambda support added to the module\.
* na\_ontap\_s3\_policies \- AWS Lambda support added to the module\.
* na\_ontap\_s3\_services \- AWS Lambda support added to the module\.
* na\_ontap\_s3\_users \- AWS Lambda support added to the module\.
* na\_ontap\_snapmirror \- AWS Lambda support added to the module\.
* na\_ontap\_volume\_autosize \- AWS Lambda support added to the module\.
* na\_ontap\_volume\_clone \- AWS Lambda support added to the module\.
* na\_ontap\_vserver\_peer \- AWS Lambda support added to the module\.

<a id="minor-changes-1"></a>
### Minor Changes

<a id="ansible-core-4"></a>
#### Ansible\-core

* ansible\-test \- Add container/remote aliases for more loosely specifying managed test environments\.
* ansible\-test \- Add support for using the Ansible Core CI service from GitHub Actions\.

<a id="amazon-aws"></a>
#### amazon\.aws

* meta/runtime\.yml \- Lowered the <code>ansible\-core</code> minimum version to <code>2\.16</code>\. This expands compatibility and does not change or remove existing functionality\.

<a id="ansible-windows"></a>
#### ansible\.windows

* PowerShell 7 \- Add initial support for running modules against PowerShell 7 interpreters\. Support for PowerShell 7 varies across each module\, see module documentation for more information\.
* ansible\.windows\.win\_package \- Add optional Authenticode signature validation for installer files via the new <code>verify\_signature</code> parameter\.
* win\_file \- is aligned with <code>ansible\.builtin\.file</code> and now supports options <code>access\_time</code>\, <code>access\_time\_format</code>\, <code>modification\_time</code>\, and <code>modification\_time\_format</code>\. \([https\://github\.com/ansible\-collections/ansible\.windows/issues/798](https\://github\.com/ansible\-collections/ansible\.windows/issues/798)\)
* win\_shell \- Add <code>cmd</code> module option that can be used instead of the free form input\. This aligns the options to the POSIX <code>shell</code> module\.
* win\_shell \- Support using <code>pwsh\.exe</code> as the executable in a mode similar to how <code>powershell\.exe</code> is run\.

<a id="cisco-meraki-1"></a>
#### cisco\.meraki

* Added new modules and action plugins for Cisco Umbrella account connect/disconnect\, Wireless AutoRF \(RRM\) settings\, third\-party VPN peers\, organization integrations\, inventory EoX overview\, network moves\, SASE eligible networks\, and wireless device provisioning deployments\.
* networks\_wireless\_settings\: added multicast\-to\-unicast conversion support\.
* organizations\_inventory\_devices\_info\: added eoxStatuses filtering and included EoX fields in returned inventory device data\.

<a id="cisco-mso"></a>
#### cisco\.mso

* Add support to deploy and undeploy non\-schema templates in ndo\_template\_deploy \(formerly ndo\_schema\_template\_deploy\)\.

<a id="community-clickhouse"></a>
#### community\.clickhouse

* clickhouse\_user \- added new <code>authentication</code> dict parameter supporting LDAP\, hashed\, and plain\-text password authentication for created users\. Cannot be used together with the existing <code>type\_password</code> and <code>password</code> parameters \([https\://github\.com/ansible\-collections/community\.clickhouse/issues/142](https\://github\.com/ansible\-collections/community\.clickhouse/issues/142)\)\.

<a id="community-docker-1"></a>
#### community\.docker

* docker\_compose\_v2\_pull \- adds <code>ignore\_pull\_failures</code> parameter that passes <code>\-\-ignore\-pull\-failures</code> to the <code>docker compose pull</code> call when set to <code>true</code> \([https\://github\.com/ansible\-collections/community\.docker/pull/1248](https\://github\.com/ansible\-collections/community\.docker/pull/1248)\)\.

<a id="community-general-3"></a>
#### community\.general

* ansible\_galaxy\_install \- add parameter <code>executable</code> \([https\://github\.com/ansible\-collections/community\.general/issues/7261](https\://github\.com/ansible\-collections/community\.general/issues/7261)\, [https\://github\.com/ansible\-collections/community\.general/pull/11646](https\://github\.com/ansible\-collections/community\.general/pull/11646)\)\.
* api module utils \- use Python\-defined constants for HTTP return codes \([https\://github\.com/ansible\-collections/community\.general/pull/11561](https\://github\.com/ansible\-collections/community\.general/pull/11561)\)\.
* bitbucket module utils \- use Python\-defined constants for HTTP return codes \([https\://github\.com/ansible\-collections/community\.general/pull/11561](https\://github\.com/ansible\-collections/community\.general/pull/11561)\)\.
* consul module utils \- use Python\-defined constants for HTTP return codes \([https\://github\.com/ansible\-collections/community\.general/pull/11561](https\://github\.com/ansible\-collections/community\.general/pull/11561)\, [https\://github\.com/ansible\-collections/community\.general/pull/11573](https\://github\.com/ansible\-collections/community\.general/pull/11573)\)\.
* doas become plugin \- add new option <code>allow\_pipelining</code> to explicitly allow the use of pipelining with this plugin\. This should only be set to <code>true</code> with ansible\-core 2\.19\+ when <code>doas</code> does not require a password \([https\://github\.com/ansible\-collections/community\.general/issues/11411](https\://github\.com/ansible\-collections/community\.general/issues/11411)\, [https\://github\.com/ansible\-collections/community\.general/pull/11481](https\://github\.com/ansible\-collections/community\.general/pull/11481)\)\.
* gandi\_livedns\_api module utils \- use Python\-defined constants for HTTP return codes \([https\://github\.com/ansible\-collections/community\.general/pull/11561](https\://github\.com/ansible\-collections/community\.general/pull/11561)\)\.
* github\_app\_access\_token lookup plugin \- use Python\-defined constants for HTTP return codes \([https\://github\.com/ansible\-collections/community\.general/pull/11561](https\://github\.com/ansible\-collections/community\.general/pull/11561)\)\.
* hwc\_utils module utils \- use Python\-defined constants for HTTP return codes \([https\://github\.com/ansible\-collections/community\.general/pull/11561](https\://github\.com/ansible\-collections/community\.general/pull/11561)\, [https\://github\.com/ansible\-collections/community\.general/pull/11573](https\://github\.com/ansible\-collections/community\.general/pull/11573)\)\.
* icinga2 inventory plugin \- use Python\-defined constants for HTTP return codes \([https\://github\.com/ansible\-collections/community\.general/pull/11561](https\://github\.com/ansible\-collections/community\.general/pull/11561)\, [https\://github\.com/ansible\-collections/community\.general/pull/11573](https\://github\.com/ansible\-collections/community\.general/pull/11573)\)\.
* incus inventory plugin \- add support for constructing project\-independent FQDNs \([https\://github\.com/ansible\-collections/community\.general/pull/11555](https\://github\.com/ansible\-collections/community\.general/pull/11555)\)\.
* ipa module utils \- use Python\-defined constants for HTTP return codes \([https\://github\.com/ansible\-collections/community\.general/pull/11561](https\://github\.com/ansible\-collections/community\.general/pull/11561)\)\.
* keycloak module utils \- use Python\-defined constants for HTTP return codes \([https\://github\.com/ansible\-collections/community\.general/pull/11561](https\://github\.com/ansible\-collections/community\.general/pull/11561)\)\.
* keycloak\_realm \- add <code>first\_broker\_login\_flow</code> parameter \([https\://github\.com/ansible\-collections/community\.general/pull/11622](https\://github\.com/ansible\-collections/community\.general/pull/11622)\)\.
* ldap\_attrs \- add <code>binary\_attributes</code> and <code>honor\_binary</code> parameters to handle binary attribute values \([https\://github\.com/ansible\-collections/community\.general/pull/11558](https\://github\.com/ansible\-collections/community\.general/pull/11558)\)\.
* ldap\_entry \- add <code>binary\_attributes</code> and <code>honor\_binary</code> parameters to handle creating objects with attributes set to binary values \([https\://github\.com/ansible\-collections/community\.general/pull/11558](https\://github\.com/ansible\-collections/community\.general/pull/11558)\)\.
* lookup plugin passwordstore \- modernize internal <code>check\_output2\(\)</code> helper using <code>subprocess\.run\(\)</code> and rename it to <code>run\_backend\_cmd\(\)</code> \([https\://github\.com/ansible\-collections/community\.general/pull/11655](https\://github\.com/ansible\-collections/community\.general/pull/11655)\)\.
* memset module utils \- use Python\-defined constants for HTTP return codes \([https\://github\.com/ansible\-collections/community\.general/pull/11561](https\://github\.com/ansible\-collections/community\.general/pull/11561)\)\.
* merge\_variables lookup plugin \- extended merging capabilities added \([https\://github\.com/ansible\-collections/community\.general/pull/11536](https\://github\.com/ansible\-collections/community\.general/pull/11536)\)\.
* nmcli \- fix idempotency for MAC VLAN interfaces when using <code>macvlan\.tap</code> \([https\://github\.com/ansible\-collections/community\.general/pull/11551](https\://github\.com/ansible\-collections/community\.general/pull/11551)\)\.
* nsupdate \- replace <code>list\(map\(\.\.\.\)\)</code> constructs with Python comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/11590](https\://github\.com/ansible\-collections/community\.general/pull/11590)\)\.
* ocapi\_utils module utils \- use Python\-defined constants for HTTP return codes \([https\://github\.com/ansible\-collections/community\.general/pull/11561](https\://github\.com/ansible\-collections/community\.general/pull/11561)\)\.
* oci\_utils module utils \- use Python\-defined constants for HTTP return codes \([https\://github\.com/ansible\-collections/community\.general/pull/11561](https\://github\.com/ansible\-collections/community\.general/pull/11561)\)\.
* online module utils \- use Python\-defined constants for HTTP return codes \([https\://github\.com/ansible\-collections/community\.general/pull/11561](https\://github\.com/ansible\-collections/community\.general/pull/11561)\)\.
* osx\_defaults \- add support for <code>dict</code> type values\, including <code>dict\_mode</code> option to merge keys into an existing dictionary \([https\://github\.com/ansible\-collections/community\.general/issues/238](https\://github\.com/ansible\-collections/community\.general/issues/238)\, [https\://github\.com/ansible\-collections/community\.general/pull/11659](https\://github\.com/ansible\-collections/community\.general/pull/11659)\)\.
* redfish\_utils module utils \- use Python\-defined constants for HTTP return codes \([https\://github\.com/ansible\-collections/community\.general/pull/11561](https\://github\.com/ansible\-collections/community\.general/pull/11561)\, [https\://github\.com/ansible\-collections/community\.general/pull/11573](https\://github\.com/ansible\-collections/community\.general/pull/11573)\)\.
* rundeck module utils \- use Python\-defined constants for HTTP return codes \([https\://github\.com/ansible\-collections/community\.general/pull/11561](https\://github\.com/ansible\-collections/community\.general/pull/11561)\, [https\://github\.com/ansible\-collections/community\.general/pull/11573](https\://github\.com/ansible\-collections/community\.general/pull/11573)\)\.
* scaleway module utils \- use Python\-defined constants for HTTP return codes \([https\://github\.com/ansible\-collections/community\.general/pull/11561](https\://github\.com/ansible\-collections/community\.general/pull/11561)\)\.
* supervisorctl \- added an additional condition for generating the error \'no such process\' \([https\://github\.com/ansible\-collections/community\.general/issues/11621](https\://github\.com/ansible\-collections/community\.general/issues/11621)\, [https\://github\.com/ansible\-collections/community\.general/pull/11632](https\://github\.com/ansible\-collections/community\.general/pull/11632)\)\.
* timezone \- replace <code>list\(map\(\.\.\.\)\)</code> constructs with Python comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/11590](https\://github\.com/ansible\-collections/community\.general/pull/11590)\)\.
* utm\_utils module utils \- use Python\-defined constants for HTTP return codes \([https\://github\.com/ansible\-collections/community\.general/pull/11561](https\://github\.com/ansible\-collections/community\.general/pull/11561)\, [https\://github\.com/ansible\-collections/community\.general/pull/11573](https\://github\.com/ansible\-collections/community\.general/pull/11573)\)\.

<a id="community-mysql"></a>
#### community\.mysql

* Update imports from ansible\.module\_utils\.\_text to use ansible\.module\_utils\.common\.text\.converters

<a id="community-proxmox-1"></a>
#### community\.proxmox

* inventory plugin \- add want\_post\_filtering\_facts to delay fact gathering until filtering has completed \([https\://github\.com/ansible\-collections/community\.proxmox/pull/261](https\://github\.com/ansible\-collections/community\.proxmox/pull/261)\)\.
* proxmox \- Add api\_timeout option for all modules \([https\://github\.com/ansible\-collections/community\.proxmox/pull/253](https\://github\.com/ansible\-collections/community\.proxmox/pull/253)\)\.
* proxmox\_role \- add role\'s privs on the return data \([https\://github\.com/ansible\-collections/community\.proxmox/pull/283](https\://github\.com/ansible\-collections/community\.proxmox/pull/283)\)\.
* proxmox\_storage \- Add support for ZFS thin\-provisioning \([https\://github\.com/ansible\-collections/community\.proxmox/pull/265](https\://github\.com/ansible\-collections/community\.proxmox/pull/265)\)\.
* proxmox\_storage \- Add the option namespace for PBS storage \([https\://github\.com/ansible\-collections/community\.proxmox/pull/282](https\://github\.com/ansible\-collections/community\.proxmox/pull/282)\)
* proxmox\_storage \- refactor the validation of storage options \([https\://github\.com/ansible\-collections/community\.proxmox/pull/266](https\://github\.com/ansible\-collections/community\.proxmox/pull/266)\)\.
* proxmox\_storage\_contents\_info \- Add support for content type <code>import</code> \([https\://github\.com/ansible\-collections/community\.proxmox/pull/260](https\://github\.com/ansible\-collections/community\.proxmox/pull/260)\)\.
* proxmox\_zone\, proxmox\_vnet\, proxmox\_subnet \- make sdn modules compatible with pve8 \([https\://github\.com/ansible\-collections/community\.proxmox/pull/254](https\://github\.com/ansible\-collections/community\.proxmox/pull/254)\)\.

<a id="community-routeros-3"></a>
#### community\.routeros

* api\_info \- adds support for the <code>app</code> path for RouterOS \>\= 7\.21 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info \- adds support for the <code>caps\-man actual\-interface\-configuration</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info \- adds support for the <code>disk btrfs filesystem</code> path for RouterOS \>\=7\.18 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info \- adds support for the <code>dude ros health</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info \- adds support for the <code>dude ros interface</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info \- adds support for the <code>dude ros neighbor</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info \- adds support for the <code>dude ros resource</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info \- adds support for the <code>dude ros routerboard</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info \- adds support for the <code>interface bridge port\-controller port</code> path for RouterOS \>\= 7\.15\, \< 7\.18 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info \- adds support for the <code>interface ethernet switch qos port</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/issues/319](https\://github\.com/ansible\-collections/community\.routeros/issues/319)\, [https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info \- adds support for the <code>interface ethernet switch qos tx\-manager queue</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/issues/319](https\://github\.com/ansible\-collections/community\.routeros/issues/319)\, [https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info \- adds support for the <code>interface lte</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/issues/282](https\://github\.com/ansible\-collections/community\.routeros/issues/282)\, [https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info \- adds support for the <code>interface wifi steering neighbor\-group</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info \- adds support for the <code>interface wireless manual\-tx\-power\-table</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info \- adds support for the <code>interface wireless nstreme</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info \- adds support for the <code>interface</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info \- adds support for the <code>iot bluetooth advertisers</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info \- adds support for the <code>iot bluetooth peripheral\-devices</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info \- adds support for the <code>iot bluetooth scanners</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info \- adds support for the <code>iot bluetooth</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info \- adds support for the <code>iot lora channels</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info \- adds support for the <code>iot lora radios</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info \- adds support for the <code>iot lora</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info \- adds support for the <code>ip ipsec key</code> path for RouterOS \>\= 7\.15\, \< 7\.20 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info \- adds support for the <code>ip pool used</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info \- adds support for the <code>ip proxy connections</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info \- adds support for the <code>ip socks connections</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info \- adds support for the <code>lcd screen</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info \- adds support for the <code>lora channels</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info \- adds support for the <code>lora radios</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info \- adds support for the <code>lora</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info \- adds support for the <code>partitions</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info \- adds support for the <code>port</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info \- adds support for the <code>routing isis interface</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/issues/356](https\://github\.com/ansible\-collections/community\.routeros/issues/356)\, [https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info \- adds support for the <code>routing isis lsp</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/issues/356](https\://github\.com/ansible\-collections/community\.routeros/issues/356)\, [https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info \- adds support for the <code>routing isis neighbor</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/issues/356](https\://github\.com/ansible\-collections/community\.routeros/issues/356)\, [https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info \- adds support for the <code>routing ospf neighbor</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info \- adds support for the <code>routing pimsm igmp\-interface\-template</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info \- adds support for the <code>routing route rule</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info \- adds support for the <code>routing route</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info \- adds support for the <code>system package local\-update</code> path for RouterOS \>\= 7\.17 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info \- adds support for the <code>system routerboard usb</code> path for RouterOS \>\= 7\.15\, \< 7\.20 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info \- adds support for the <code>system script environment</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info \- adds support for the <code>system script job</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info \- adds support for the <code>system upgrade</code> path for RouterOS \>\= 7\.15\, \< 7\.17 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- add default values for fields <code>ciphers</code> in <code>ip ssh</code>\, <code>mvrp</code> in  <code>interface vlan</code>\, and <code>mvrp\-forbidden</code> in <code>interface bridge vlan</code> \([https\://github\.com/ansible\-collections/community\.routeros/pull/439/](https\://github\.com/ansible\-collections/community\.routeros/pull/439/)\)\.
* api\_info\, api\_modify \- adds default value and removes required being true for parameter <code>address\-pool</code> in the <code>ipv6 dhcp\-server</code> path \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the  <code>lacp\-mode</code> \(\>\= 7\.19\)\, <code>lacp\-system\-id</code> \(\>\= 7\.21\) and <code>lacp\-system\-priority</code> \(\>\= 7\.21\) parameters in the <code>interface bonding</code> path \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>3gpp\-info\-raw</code> \(\>\= 7\.21\)\, and <code>realms\-raw</code> \(\>\= 7\.21\) parameters in the <code>interface wifi interworking</code> path \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>accept\-prefix\-without\-address</code> \(\>\= 7\.20\)\, <code>allow\-reconfigure</code> \(\>\= 7\.17\)\, <code>check\-gateway</code> \(\>\= 7\.19\)\, <code>custom\-iana\-id</code> \(\>\= 7\.20\)\, <code>custom\-iapd\-id</code> \(\>\= 7\.20\)\, <code>default\-route\-tables</code> \(\>\= 7\.19\)\, <code>prefix\-address\-lists</code> \(\>\= 7\.17\) and <code>rapid\-commit</code> \(\>\= 7\.17\) parameters in the <code>ipv6 dhcp\-client</code> path \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>accept\-proto\-version</code>\, <code>accept\-pseudowire\-type</code>\, <code>l2tpv3\-circuit\-id</code>\, <code>l2tpv3\-cookie\-length</code>\, <code>l2tpv3\-digest\-hash</code> and <code>l2tpv3\-ether\-interface\-list</code> parameters in the <code>interface l2tp\-server server</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>accept\-router\-advertisements\-on</code> parameters in the <code>ipv6 settings</code> path for RouterOS \>\= 7\.21 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>accept\-untagged</code> \(\>\= 7\.20\)\, and <code>pppoe\-over\-vlan\-range</code> \(\>\= 7\.17\) parameters in the <code>interface pppoe\-server server</code> path \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>add\-arp</code> \(\>\= 7\.15\)\, <code>address\-lists</code> \(\>\= 7\.17\) and <code>use\-reconfigure</code> \(\>\= 7\.19\) parameters in the <code>ip dhcp\-server</code> path \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>address\-list\-extra\-time</code> and <code>vrf</code> parameters in the <code>ip dns</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>address\-lists</code> \(\>\= 7\.17\)\, <code>ignore\-ia\-na\-bindings</code> \(\>\= 7\.20\)\, <code>prefix\-pool</code> \(\>\= 7\.17\) and <code>use\-reconfigure</code> \(\>\= 7\.17\) parameters in the <code>ipv6 dhcp\-server</code> path \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>agent\-circuit\-id</code> and <code>agent\-remote\-id</code> parameters in the <code>ip dhcp\-server lease</code> path for RouterOS \>\= 7\.21 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>allow\-dual\-stack\-queue</code>\, <code>block\-access</code>\, <code>dhcp\-option\-set</code>\, <code>lease\-time</code>\, <code>parent\-queue</code>\, <code>queue\-type</code>\, <code>rate\-limit</code>\, <code>routes</code> and <code>use\-src\-mac</code> parameters in the <code>ip dhcp\-server lease</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>allow\-reconfigure</code> \(\>\= 7\.19\)\, <code>check\-gateway</code> \(\>\= 7\.19\)\, <code>default\-route\-tables</code> \(\>\= 7\.18\)\, <code>dscp</code> \(\>\= 7\.20\)\, <code>use\-broadcast</code> \(\>\= 7\.20\) and <code>vlan\-priority</code> \(\>\= 7\.20\) parameters in the <code>ip dhcp\-client</code> path \([https\://github\.com/ansible\-collections/community\.routeros/issues/407](https\://github\.com/ansible\-collections/community\.routeros/issues/407)\, [https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>allowed\-addresses4</code> and <code>allowed\-addresses6</code> parameters in the <code>tool bandwidth\-server</code> path for RouterOS \>\= 7\.18 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>app settings</code> path for RouterOS \>\= 7\.21 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>authentication</code>\, <code>comment</code>\, <code>ip\-type</code>\, <code>ipv6\-interface</code>\, <code>passthrough\-interface</code>\, <code>passthrough\-mac</code>\, <code>passthrough\-subnet\-size</code>\, <code>password</code>\, <code>use\-network\-apn</code> and <code>user</code> parameters in the <code>interface lte apn</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/issues/282](https\://github\.com/ansible\-collections/community\.routeros/issues/282)\, [https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>auto\-link\-local</code> parameter in the <code>ipv6 address</code> path for RouterOS \>\= 7\.18 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>back\-to\-home\-vpn</code> and <code>vpn\-prefer\-relay\-code</code> parameters in the <code>ip cloud</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>beacon\-protection</code> parameter in the <code>interface wifi security</code> path for RouterOS \>\= 7\.21 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>boot\-os</code>\, <code>cpu\-mode</code>\, <code>disable\-pci</code>\, <code>etherboot\-port</code>\, <code>gpio\-function</code>\, <code>init\-delay</code> and <code>regulatory\-domain\-ce</code> parameters in the <code>system routerboard settings</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>bridge\-port\-trusted</code> \(\>\= 7\.17\)\, <code>bridge\-port\-vid</code> \(\>\= 7\.217\)\, <code>comment</code> \(\>\= 7\.15\)\, <code>dhcpv6\-lease\-time</code> \(\>\= 7\.20\)\, <code>dhcpv6\-pd\-pool \(\>\= 7\.15\)</code>\, <code>dhcpv6\-use\-radius</code> \(\>\= 7\.20\)\, <code>remote\-ipv6\-prefix\-pool</code> \(\>\= 7\.15\) and <code>remote\-ipv6\-prefix\-reuse</code> \(\>\= 7\.20\) parameters in the <code>ppp profile</code> path \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>broadcast</code> and <code>netmask</code> parameters in the <code>ip address</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>builtin\-trust\-anchors</code> \(\>\= 7\.19\) and <code>builtin\-trust\-store</code> \(\>\= 7\.21\) parameters in the <code>certificate settings</code> path \([https\://github\.com/ansible\-collections/community\.routeros/issues/379](https\://github\.com/ansible\-collections/community\.routeros/issues/379)\, [https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>burst\-time</code>\, <code>prism\-cardtype</code>\, <code>vht\-basic\-mcs</code> and <code>vht\-supported\-mcs</code> parameters in the <code>interface wireless</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>cable\-settings</code> \(\>\= 7\.15\.3\)\, <code>disable\-running\-check</code> \(\>\= 7\.15\.3\)\, <code>numbers</code> \(\>\= 7\.15\)\, <code>sfp\-ignore\-rx\-los</code> \(\>\= 7\.15\) parameters in the <code>interface ethernet</code> path \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>caps\-man interface</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>caps\-man rates</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>certificate crl</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>certificate scep\-server ra</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>certificate scep\-server</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>certificate\-verification</code> parameters in the <code>tool e\-mail</code> path for RouterOS \>\= 7\.21 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>certificate</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>certificate</code>\, <code>enable\-tun\-ipv6</code>\, <code>ipv6\-prefix\-len</code>\, <code>push\-routes</code>\, <code>redirect\-gateway</code>\, <code>reneg\-sec</code>\, <code>tls\-version</code> and <code>certtun\-server\-ipv6ificate</code> parameters in the <code>interface ovpn\-server server</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>channel\.deprioritize\-unii\-3\-4</code> \(\>\= 7\.20\)\, <code>channel\.reselect\-interval</code> \(\>\= 7\.15\)\, <code>channel\.reselect\-time</code> \(\>\= 7\.19\)\, <code>configuration\.distance</code> \(\>\= 7\.15\)\, <code>configuration\.installation</code> \(\>\= 7\.17\)\, <code>configuration\.max\-clients</code> \(\>\=7\.18\)\, <code>configuration\.station\-roaming</code> \(\>\= 7\.17\)\, <code>configuration\.tx\-chains</code> \(\>\= 7\.15\)\, <code>datapath\.openflow\-switch</code> \(\>\= 7\.20\)\, <code>security\.multi\-passphrase\-group</code> \(\>\= 7\.17\) and <code>steering\.2g\-probe\-delay</code> \(\>\=7\.18\) parameters in the <code>interface wifi</code> path \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>ciphers</code> parameter in the <code>ip ssh</code> path for RouterOS \>\= 7\.17 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>ciphers</code> parameters in the <code>interface sstp\-server server</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>client\-address</code>\, <code>client\-dns</code>\, <code>client\-endpoint</code>\, <code>client\-keepalive</code>\, <code>client\-listen\-port</code>\, and <code>private\-key</code> parameters in the <code>interface wireguard peers</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>client\-allowed\-address</code> parameter in the <code>interface wireguard peers</code> path for RouterOS \>\= 7\.21 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>comment</code> and <code>pref64</code> parameters in the <code>ipv6 nd</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>comment</code> parameter in the <code>interface wireless security\-profiles</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/issues/388](https\://github\.com/ansible\-collections/community\.routeros/issues/388)\, [https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>comment</code> parameter in the <code>ip dhcp\-client option</code> path for RouterOS \>\= 7\.16 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>comment</code> parameter in the <code>ip ipsec policy group</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>comment</code> parameter in the <code>ip ipsec proposal</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>comment</code> parameter in the <code>ip smb users</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>comment</code> parameter in the <code>ipv6 dhcp\-server option</code> path for RouterOS \>\= 7\.16 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>comment</code> parameter in the <code>port remote\-access</code> path for RouterOS \>\= 7\.21 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>comment</code> parameter in the <code>ppp secret</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>comment</code> parameter in the <code>tool romon port</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>configuration\.hw\-protection\-mode</code>\, <code>interworking\.3gpp\-info\-raw</code>\, <code>interworking\.realms\-raw</code>\, <code>security\.beacon\-protection</code>\, <code>steering\.transition\-request\-count</code>\, <code>steering\.transition\-request\-period</code>\, <code>steering\.transition\-threshold</code>\, <code>steering\.transition\-threshold\-time</code> and <code>steering\.transition\-time</code> parameters in the <code>interface wifi</code> path for RouterOS \>\= 7\.21 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>connection\-mark</code> and <code>use\-responder\-dns</code> parameters in the <code>ip ipsec mode\-config</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>connection\-nat\-state</code> parameter in the <code>ipv6 firewall mangle</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>connection\-nat\-state</code>\, <code>routing\-mark</code> and <code>tls\-host</code> parameters in the <code>ipv6 firewall filter</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>connection\-tracking\-mode</code> \(\>\= 7\.20\)\, <code>connection\-tracking\-port</code> \(\>\= 7\.20\)\, and <code>group\-authority</code> \(\>\= 7\.15\) parameters in the <code>interface vrrp</code> path \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>console settings</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>container config</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>container envs</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>container mounts</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>container</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>datapath\.openflow\-switch</code> \(\>\= 7\.20\)\, <code>distance</code> \(\>\= 7\.15\)\, <code>installation</code> \(\>\= 7\.17\)\, <code>interworking\.wan\-symmetric</code> \(\>\= 7\.15\)\, <code>max\-clients</code> \(\>\=7\.18\) and <code>station\-roaming</code> \(\>\= 7\.17\) parameters in the <code>interface wifi configuration</code> path \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>days</code> \(\>\= 7\.21\) and  <code>multi\-passphrase\-group</code> \(\>\= 7\.17\) parameters in the <code>interface wifi access\-list</code> path \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>dhcp\-server\-vrf</code> \(\>\= 7\.15\) and <code>local\-address\-as\-src\-ip</code> \(\>\= 7\.17\) parameters in the <code>ip dhcp\-relay</code> path \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>disable\-security\-rules</code> parameter in the <code>iot modbus</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>disk btrfs subvolume</code> path for RouterOS \>\=7\.18 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>disk btrfs transfer</code> path for RouterOS \>\=7\.18 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>disk</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>dns\-server</code> \(\>\= 7\.16\)\, <code>early\-failure\-detection</code> \(\>\= 7\.20\)\, <code>early\-success\-detection</code> \(\>\= 7\.205\)\, <code>ignore\-initial\-down</code> \(\>\= 7\.17\)\, <code>ignore\-initial\-up</code> \(\>\= 7\.17\) and <code>record\-type</code> \(\>\= 7\.16\) parameters in the <code>tool netwatch</code> path \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>dont\-fragment</code> parameter in the <code>interface gre6</code> path for RouterOS \>\= 7\.21 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>dude agent</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>dude device\-type</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>dude device</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>dude notification</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>dude probe</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>dude ros address</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>dude ros arp</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>dude ros lease</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>dude ros queue</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>dude ros route</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>dude service</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>dude</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>dynamic\-lease\-identifiers</code> and <code>support\-broadband\-tr101</code> parameters in the <code>ip dhcp\-server</code> path for RouterOS \>\= 7\.21 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>dynamic</code> and <code>timeout</code> parameters in the <code>ip firewall address\-list</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>dynamic</code> and <code>timeout</code> parameters in the <code>ipv6 firewall address\-list</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>egress\-rate</code>\, <code>ingress\-rate</code>\, <code>l3\-hw\-offloading</code>\, <code>limit\-broadcasts</code>\, <code>limit\-unknown\-multicasts</code>\, <code>limit\-unknown\-unicasts</code>\, <code>mirror\-egress</code>\, <code>mirror\-ingress</code>\, <code>mirror\-ingress\-target</code>\, <code>numbers</code> and <code>storm\-rate</code> parameters in the <code>interface ethernet switch port</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>enable\-ipv6\-accounting</code> parameter in the <code>port aaa</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>file rsync\-daemon</code> path for RouterOS \>\= 7\.16 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>file sync</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>file</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>filter\-dst\-ip\-address</code> \(\>\= 7\.15\)\, <code>filter\-dst\-ipv6\-address</code> \(\>\= 7\.15\)\, <code>filter\-dst\-mac\-address</code> \(\>\= 7\.15\)\, <code>filter\-dst\-port</code> \(\>\= 7\.15\)\, <code>filter\-src\-ip\-address</code> \(\>\= 7\.15\)\, <code>filter\-src\-ipv6\-address</code> \(\>\= 7\.15\)\, <code>filter\-src\-mac\-address</code> \(\>\= 7\.15\)\, <code>filter\-src\-port</code> \(\>\= 7\.15\)\, <code>filter\-vlan</code> \(\>\= 7\.15\)\, <code>max\-packet\-size</code> \(\>\= 7\.19\)\, <code>quick\-rows</code> \(\>\= 7\.15\) and <code>quick\-show\-frame</code> \(\>\= 7\.15\) parameters in the <code>tool sniffer</code> path \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>headers</code>\, <code>hop\-limit</code>\, <code>nth</code> and <code>to\-address</code> parameters in the <code>ipv6 firewall nat</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>heartbeat</code> \(\>\= 7\.18\) and <code>priority</code> \(\>\= 7\.17\) parameters in the <code>interface bridge mlag</code> path \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>hw\-protection\-mode</code>\, <code>distance</code>\, <code>interworking\.3gpp\-info\-raw</code>\, <code>interworking\.realms\-raw</code>\, <code>security\.beacon\-protection</code>\, <code>steering\.transition\-request\-coun</code>\, <code>steering\.transition\-request\-period</code>\, <code>steering\.transition\-threshold</code>\, <code>steering\.transition\-threshold\-time</code> and <code>steering\.transition\-time</code> parameters in the <code>interface wifi configuration</code> path for RouterOS \>\= 7\.21 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>icmp\-errors\-use\-inbound\-interface\-address</code> and <code>tcp\-timestamps</code> parameters in the <code>ip settings</code> path for RouterOS \>\= 7\.17 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>inactivity\-policy</code> \(\>\= 7\.16\) and <code>inactivity\-timeout</code> \(\>\= 7\.16\) parameters in the <code>user</code> path \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>input\.attr\-error\-handling</code> \(\>\= 7\.21\.2\)\, <code>input\.filter\-communities</code> \(\>\= 7\.19\)\, <code>input\.filter\-ext\-communities</code> \(\>\= 7\.19\)\, <code>input\.filter\-large\-communities</code> \(\>\= 7\.19\)\, <code>input\.filter\-nlri</code> \(\>\= 7\.20\)\, <code>input\.filter\-unknown</code> \(\>\= 7\.19\)\, <code>output\.as\-override</code> \(\>\= 7\.15\)\, <code>output\.default\-prepend</code> \(\>\= 7\.15\) and <code>output\.network\-blackhole</code> \(\>\= 7\.20\.1\) parameters in the <code>routing bgp template</code> path \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>input\.attr\-error\-handling</code> parameter in the <code>routing bgp connection</code> path for RouterOS \>\= 7\.21\.2 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>input</code> parameter in the <code>mpls interface</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>interface amt</code> for RotuerOS 7\.18 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>interface bridge calea</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>interface bridge filter</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>interface bridge host</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>interface bridge mdb</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>interface bridge msti</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>interface bridge nat</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>interface bridge port mst\-override</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>interface bridge port\-controller device</code> path for RouterOS \>\= 7\.15\, \< 7\.18 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>interface eoipv6</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>interface ethernet switch host</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>interface ethernet switch l3hw\-settings advanced</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>interface ethernet switch l3hw\-settings</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>interface ethernet switch qos map ip</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/issues/319](https\://github\.com/ansible\-collections/community\.routeros/issues/319)\, [https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>interface ethernet switch qos map vlan</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/issues/319](https\://github\.com/ansible\-collections/community\.routeros/issues/319)\, [https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>interface ethernet switch qos map</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/issues/319](https\://github\.com/ansible\-collections/community\.routeros/issues/319)\, [https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>interface ethernet switch qos priority\-flow\-control</code> path for RouterOS \>\= 7\.15\, \< 7\.16 \([https\://github\.com/ansible\-collections/community\.routeros/issues/319](https\://github\.com/ansible\-collections/community\.routeros/issues/319)\, [https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>interface ethernet switch qos profile</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/issues/319](https\://github\.com/ansible\-collections/community\.routeros/issues/319)\, [https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>interface ethernet switch qos settings</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/issues/319](https\://github\.com/ansible\-collections/community\.routeros/issues/319)\, [https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>interface ethernet switch qos tx\-manager</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/issues/319](https\://github\.com/ansible\-collections/community\.routeros/issues/319)\, [https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>interface ethernet switch rule</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/issues/319](https\://github\.com/ansible\-collections/community\.routeros/issues/319)\, [https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>interface ethernet switch vlan</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>interface ipip</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/issues/365](https\://github\.com/ansible\-collections/community\.routeros/issues/365)\, [https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>interface ipipv6</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>interface l2tp\-ether</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>interface l2tp\-server</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>interface lte settings</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/issues/282](https\://github\.com/ansible\-collections/community\.routeros/issues/282)\, [https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>interface macsec profile</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>interface macsec</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>interface macvlan</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>interface mesh port</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>interface mesh</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>interface ovpn\-server</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>interface ppp\-server</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>interface pppoe\-server</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>interface pptp\-client</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>interface pptp\-server</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>interface sstp\-client</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>interface sstp\-server</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>interface veth</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>interface vpls</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>interface vxlan vteps</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>interface vxlan</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>interface wifi radio settings</code> path for RouterOS \>\= 7\.17 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>interface wifi security multi\-passphrase</code> path for RouterOS \>\= 7\.17 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>interface wireless channels</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>interface wireless interworking\-profiles</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>interface wireless nstreme\-dual</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>interface wireless wds</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>invalid\-users</code>\,\`\`read\-only\`\`\,\`\`require\-encryption\`\` and <code>valid\-users</code> parameters in the <code>ip smb shares</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>iot bluetooth advertisers ad\-structures</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>iot bluetooth whitelist</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>iot lora joineui</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>iot lora netid</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>iot lora servers</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>iot lora traffic options</code> path for RouterOS \>\= 7\.17 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>iot modbus security\-rules</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>iot mqtt brokers</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>iot mqtt subscriptions</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>ip cloud back\-to\-home\-file settings</code> path for RouterOS \>\= 7\.18 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>ip cloud back\-to\-home\-file</code> path for RouterOS \>\= 7\.18 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>ip cloud back\-to\-home\-user</code> path for RouterOS \>\= 7\.18 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>ip cloud back\-to\-home\-users</code> path for RouterOS \>\= 7\.15\, \< 7\.18 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>ip dhcp\-server alert</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>ip firewall calea</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>ip hotspot ip\-binding</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>ip ipsec key psk</code> path for RouterOS \>\= 7\.21 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>ip ipsec key qkd</code> path for RouterOS \>\= 7\.21 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>ip ipsec key rsa</code> path for RouterOS \>\= 7\.20 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>ip kid\-control device</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>ip kid\-control</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>ip media settings</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>ip media</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>ip nat\-pmp interfaces</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>ip nat\-pmp</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>ip packing</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>ip proxy access</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>ip proxy cache</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>ip proxy direct</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>ip service webserver</code> path for RouterOS \>\= 7\.21 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>ip socks users</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>ip socksify</code> path for RouterOS \>\= 7\.20 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>ip tftp</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>ipv6 dhcp\-client option</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>ipv6 dhcp\-relay option</code> path for RouterOS \>\= 7\.21 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>ipv6 dhcp\-relay</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>ipv6 dhcp\-server binding</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>ipv6 dhcp\-server option sets</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>ipv6 nd proxy</code> path for RouterOS \>\= 7\.20 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>ipv6 neighbor</code> path for RouterOS \>\= 7\.18 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>ipv6 pool</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>l2tpv3\-circuit\-id</code> \(\>\= 7\.15\) and <code>random\-source\-port</code> \(\>\=7\.18\) parameters in the <code>interface gre6</code> path \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>l3\-hw\-offloading</code>\, <code>mirror\-egress\-target</code>\, <code>numbers</code>\, <code>qos\-hw\-offloading</code>\, <code>rspan</code>\, <code>rspan\-egress\-vlan\-id</code>\, <code>rspan\-ingress\-vlan\-id</code> and <code>switch\-all\-ports</code> parameters in the <code>interface ethernet switch</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>lcd interface pages</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>lcd interface</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>lcd pin</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>lcd</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>liberal\-tcp\-tracking</code> parameters in the <code>ip firewall connection tracking</code> path for RouterOS \>\= 7\.20 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>lldp\-dcbx</code> \(\>\= 7\.17\)\, <code>lldp\-max\-frame\-size</code> \(\>\= 7\.15\) and <code>lldp\-poe\-power</code> \(\>\= 7\.15\) parameters in the <code>ip neighbor discovery\-settings</code> \([https\://github\.com/ansible\-collections/community\.routeros/issues/363](https\://github\.com/ansible\-collections/community\.routeros/issues/363)\, [https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>local\-address</code> parameter in the <code>port remote\-access</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>lora joineui</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>lora netid</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>lora servers</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>lora traffic options</code> path for RouterOS \>\= 7\.17 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>mpls ldp local\-mapping</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>mpls ldp neighbor</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>mpls ldp remote\-mapping</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>mpls mangle</code> path for RouterOS \>\= 7\.17 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>mpls settings</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>mpls traffic\-eng interface</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>mpls traffic\-eng path</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>mpls traffic\-eng tunnel</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>mvrp\-forbidden</code> parameter in the <code>interface bridge vlan</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>mvrp</code> \(\>\= 7\.15\) and <code>l3\-hw\-offloading</code> \(\>\= 7\.21\) parameters in the <code>interface vlan</code> path \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>network\-mode</code> \(\>\= 7\.20\) and <code>remote\-address</code> \(\>\= 7\.15\) parameters in the <code>interface ppp\-client</code> path \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>ntp\-none</code> parameter in the <code>ip dhcp\-server network</code> path for RouterOS \>\= 7\.20 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>numbers</code> parameters in the <code>interface ethernet poe</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>numbers</code> parameters in the <code>interface ethernet switch port\-isolation</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>numbers</code> parameters in the <code>ip firewall service\-port</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>numbers</code> parameters in the <code>ip hotspot service\-port</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>numbers</code> parameters in the <code>ip service</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>numbers</code> parameters in the <code>queue interface</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>numbers</code> parameters in the <code>system resource irq rps</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>on\-login</code> and <code>on\-logout</code> parameters in the <code>ip hotspot user profile</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>openflow port</code> path for RouterOS \>\= 7\.20 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>openflow\-switch</code> parameter in the <code>interface wifi datapath</code> for RouterOS \>\= 7\.20 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>openflow</code> path for RouterOS \>\= 7\.20 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>password\-authentication</code> and <code>publickey\-authentication\-options</code> parameters in the <code>ip ssh</code> path for RouterOS \>\= 7\.21 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>password</code> parameter in the <code>interface dot1x client</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>polling</code> \(\>\= 7\.16\)\, <code>remove\-sent\-sms\-after\-send</code> \(\>\= 7\.20\) and <code>sms\-storage</code> \(\>\= 7\.15\) parameters in the <code>tool sms</code> path \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>ppk\-secret</code> parameter in the <code>ip ipsec peer</code> path for RouterOS \>\= 7\.21 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>ppk</code> parameter in the <code>ip ipsec profile</code> path for RouterOS \>\= 7\.21 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>ppp l2tp\-secret</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>pref\-src</code> \(\>\= 7\.20\)\, <code>suppress\-hw\-offload</code> \(\>\= 7\.15\) parameters in the <code>ipv6 route</code> path \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>push\-routes\-ipv6</code> parameter in the <code>interface ovpn\-server server</code> path for RouterOS \>\= 7\.21 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>radius\-password</code> parameters in the <code>ip dhcp\-server config</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>regex</code> \(\>\= 7\.17\) parameter in the <code>system logging</code> path \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>routing bgp evpn</code> path for RouterOS \>\= 7\.20 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>routing bgp instance</code> path for RouterOS \>\= 7\.20 \([https\://github\.com/ansible\-collections/community\.routeros/issues/437](https\://github\.com/ansible\-collections/community\.routeros/issues/437)\, [https\://github\.com/ansible\-collections/community\.routeros/pull/438](https\://github\.com/ansible\-collections/community\.routeros/pull/438)\)\.
* api\_info\, api\_modify \- adds support for the <code>routing bgp vpls</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>routing bgp vpn</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>routing fantasy</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>routing filter community\-ext\-list</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>routing filter community\-large\-list</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>routing gmp</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>routing igmp\-proxy mfc</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>routing isis instance</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/issues/356](https\://github\.com/ansible\-collections/community\.routeros/issues/356)\, [https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>routing isis interface\-template</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/issues/356](https\://github\.com/ansible\-collections/community\.routeros/issues/356)\, [https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>routing pimsm bsr candidate</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>routing pimsm bsr rp\-candidate</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>routing pimsm static\-rp</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>routing rip instance</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>routing rip interface\-template</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>routing rip keys</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>routing rip static\-neighbor</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>routing rpki</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>routing settings</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>rsync\-daemon</code> path for RouterOS \>\= 7\.15\, \< 7\.16 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>rx\-switch\-offset</code> parameter in the <code>iot modbus</code> path for RouterOS \>\= 7\.21 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>sa\-dst\-address</code>\, <code>sa\-src\-address</code> parameters in the <code>ip ipsec policy</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>slave\-name\-format</code> parameter in the <code>interface wifi interworking</code> path for RouterOS \>\= 7\.16 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>socks5\-port</code> \(\>\= 7\.20\)\, <code>socks5\-server</code> \(\>\= 7\.20\) and <code>socksify\-service</code> \(\>\= 7\.20\) parameters in the <code>ip firewall nat</code> path \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>special\-login</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>src\-port</code> parameter in the <code>ip socks access</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>stale\-neighbor\-detect\-interval</code> parameters in the <code>ipv6 settings</code> path for RouterOS \>\= 7\.17 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>system console screen</code> path for RouterOS \>\= 7\.15\, \< 7\.16\.1 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>system console</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>system gps</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>system hardware</code> path for RouterOS \>\= 7\.15\, \< 7\.16\.1 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>system health</code> path for RouterOS \>\= 7\.15\.3\, \< 7\.16\.1 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>system leds</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>system ntp key</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>system package local\-update mirror</code> path for RouterOS \>\= 7\.17 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>system package local\-update update\-package\-source</code> path for RouterOS \>\= 7\.17 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>system resource hardware usb\-settings</code> path for RouterOS \>\= 7\.20 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>system resource usb settings</code> path for RouterOS \>\= 7\.15\, \< 7\.20 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>system resource usb</code> path for RouterOS \>\= 7\.15\, \< 7\.20 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>system routerboard mode\-button</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>system routerboard reset\-button</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>system routerboard wps\-button</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>system swos</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>system upgrade upgrade\-package\-source</code> path for RouterOS \>\= 7\.15\, \< 7\.17 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>task</code> path for RouterOS \>\= 7\.15\, \< 7\.17 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>tool calea</code> path for RouterOS \>\= 7\.15\, \< 7\.17 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>tool graphing queue</code> path for RouterOS \>\= 7\.15\, \< 7\.17 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>tool mac\-server sessions</code> path for RouterOS \>\= 7\.15\, \< 7\.17 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>tool traffic\-generator packet\-template</code> path for RouterOS \>\= 7\.15\, \< 7\.17 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>tool traffic\-generator port</code> path for RouterOS \>\= 7\.15\, \< 7\.17 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>tool traffic\-generator raw\-packet\-template</code> path for RouterOS \>\= 7\.15\, \< 7\.17 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>tool traffic\-generator stream</code> path for RouterOS \>\= 7\.15\, \< 7\.17 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>tool traffic\-monitor</code> path for RouterOS \>\= 7\.15\, \< 7\.17 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>tos</code> parameter in the <code>ip firewall filter</code> path for RouterOS \>\= 7\.21 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>tos</code> parameter in the <code>ip firewall mangle</code> path for RouterOS \>\= 7\.21 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>tos</code> parameter in the <code>ip firewall nat</code> path for RouterOS \>\= 7\.21 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>tos</code> parameter in the <code>ip firewall raw</code> path for RouterOS \>\= 7\.21 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>tos</code> parameter in the <code>ipv6 firewall filter</code> path for RouterOS \>\= 7\.21 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>tos</code> parameter in the <code>ipv6 firewall mangle</code> path for RouterOS \>\= 7\.21 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>tos</code> parameter in the <code>ipv6 firewall nat</code> path for RouterOS \>\= 7\.21 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>tos</code> parameter in the <code>ipv6 firewall raw</code> path for RouterOS \>\= 7\.21 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>total\-bucket\-size</code>\, <code>total\-burst\-limit</code>\, <code>total\-burst\-threshold</code>\, <code>total\-burst\-time</code>\, <code>total\-limit\-at</code>\, <code>total\-max\-limit</code>\, <code>total\-priority</code> and <code>total\-queue</code> parameters in the <code>queue simple</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>totp\-secret</code> parameter in the <code>ip hotspot user</code> path for RouterOS \>\= 7\.21 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>tr069\-client</code> path for RouterOS \>\= 7\.15\, \< 7\.17 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>transition\-request\-count</code>\, <code>transition\-request\-period</code>\, <code>transition\-threshold</code>\, <code>transition\-threshold\-time</code> and <code>transition\-time</code> parameters in the <code>interface wifi steering</code> path for RouterOS \>\= 7\.21 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>user ssh\-keys</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>user\-manager advanced</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>user\-manager attribute</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>user\-manager database</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>user\-manager limitation</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>user\-manager payment</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>user\-manager profile\-limitation</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>user\-manager profile</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>user\-manager router</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>user\-manager user group</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>user\-manager user\-profile</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>user\-manager user</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>user\-manager</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>vrf</code> parameter in the <code>interface wireguard</code> path for RouterOS \>\= 7\.21 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>vrf</code> parameters in the <code>ip socks</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>vrf</code> parameters in the <code>radius incoming</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>vrf</code> parameters in the <code>tool e\-mail</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>zerotier controller member</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>zerotier controller</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>zerotier interface</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>zerotier</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- allow multiple parameters to be disabled in the <code>interface wifi configuration</code> path \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- allow the parameter <code>forwarding\-override</code> to be disabled in the <code>interface ethernet switch port\-isolation</code> path \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- allow the parameter <code>mac\-cookie\-timeout</code> to be disabled for the <code>ip hotspot user profile</code> path \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- allow the parameter <code>mpls\-mtu</code> to be disabled for the <code>mpls interface</code> path \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- allow the parameter <code>multi\-passphrase\-group</code> to be disabled for the <code>interface wifi security</code> path \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- allow the parameter <code>relay\-info\-remote\-id</code> to be disabled for the <code>ip dhcp\-relay</code> path \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- allow the parameter <code>sfp\-shutdown\-temperature</code> to be disabled in the <code>interface ethernet</code> path \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- allow the parameter <code>time</code> to be disabled for the <code>interface wireless access\-list</code> path \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- allow the parameter <code>traffic\-processing</code> to be disabled for the <code>interface wifi datapath</code> path \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- allow the parameter <code>use\-bfd</code> to be disabled for the <code>routing ospf interface\-template</code> path \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- allow the parameters <code>action</code> to be disabled for the <code>interface wifi access\-list</code> path \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- allow the parameters <code>ca\-certificate</code>\, <code>certificate</code> and <code>interfaces</code> to be disabled for the <code>interface wifi capsman</code> path \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- allow the parameters <code>caps\-man\-addresses</code>\, <code>caps\-man\-certificate\-common\-names</code>\, <code>caps\-man\-names</code>\, <code>certificate</code>\, <code>discovery\-interfaces</code>\, <code>lock\-to\-caps\-man</code>\, <code>slaves\-datapath</code> and <code>slaves\-static</code> to be disabled for the <code>interface wifi cap</code> path \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- allow the parameters <code>certificate</code>\, <code>down\-script</code>\, <code>http\-codes</code>\, <code>interval</code>\, <code>packet\-interval</code>\, <code>port</code>\, <code>src\-address</code>\, <code>start\-delay</code>\, <code>startup\-delay</code>\, <code>test\-script</code>\, <code>thr\-avg</code>\, <code>thr\-http\-time</code>\, <code>thr\-jitter</code>\, <code>thr\-loss\-count</code>\, <code>thr\-loss\-percent</code>\, <code>thr\-max</code>\, <code>thr\-stdev</code>\, <code>thr\-tcp\-conn\-time</code>\, <code>timeout</code> and <code>up\-script</code> to be disabled in the <code>tool netwatch</code> path \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- allow the parameters <code>datapath\.traffic\-processing</code>\, <code>l2mtu</code>\, <code>master\-interface</code>\, <code>mtu</code> and <code>radio\-mac</code> to be disabled for the <code>interface wifi</code> path \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- allow the parameters <code>deprioritize\-unii\-3\-4</code>\, <code>reselect\-interval</code> and <code>reselect\-time</code> to be disabled for the <code>interface wifi channel</code> path \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- allow the parameters <code>internal\-path\-cost</code> and <code>path\-cost</code> to be disabled in the <code>interface bridge port</code> path for RouterOS \>\= 7\.13 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- changed support for the parameter <code>group\-master</code> in the <code>interface vrrp</code> path to write\-only for RouterOS \>\= 7\.11 \(deprecated and replaced by <code>group\-authority</code>\) \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- fix default value for field <code>mvrp\-forbidden</code> in <code>interface bridge vlan</code> \([https\://github\.com/ansible\-collections/community\.routeros/issues/440](https\://github\.com/ansible\-collections/community\.routeros/issues/440)\, [https\://github\.com/ansible\-collections/community\.routeros/pull/441/](https\://github\.com/ansible\-collections/community\.routeros/pull/441/)\)\.
* api\_info\, api\_modify \- parameters <code>copy\-from</code> and <code>place\-before</code> are now write\-only for the <code>routing bfd configuration</code> path \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- removed default value for parameters <code>internal\-path\-cost</code> and <code>path\-cost</code> in the <code>interface bridge port</code> path for RouterOS \>\= 7\.13 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- removed support for the <code>interface bridge port port\-controller</code> path for RouterOS \>\= 7\.18 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- removed support for the <code>interface bridge port\-extender</code> path for RouterOS \>\= 7\.18 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- removed support for the <code>ip accounting web\-access</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- removed support for the <code>ip accounting</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- removed support for the <code>mpls</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- removed support for the <code>port firmware</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- removed support for the <code>routing bgp aggregate</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- removed support for the <code>routing bgp instance</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- removed support for the <code>routing bgp network</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- removed support for the <code>routing bgp peer</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- removed support for the <code>routing mme</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- removed support for the <code>routing rip</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- removed support for the <code>system upgrade mirror</code> path for RouterOS \>\= 7\.17 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- removed support for the parameter <code>address</code> in the <code>ip traffic\-flow target</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- removed support for the parameter <code>allow\-guests</code> in the <code>ip smb</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- removed support for the parameter <code>allow\-none\-crypto</code> in the <code>ip ssh</code> path for RouterOS \>\= 7\.17 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- removed support for the parameter <code>always\-allow\-password\-login</code> in the <code>ip ssh</code> path for RouterOS \>\= 7\.21 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- removed support for the parameter <code>auto\-erase</code> in the <code>tool sms</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- removed support for the parameter <code>bsd\-syslog</code> in the <code>system logging action</code> path for RouterOS \>\= 7\.18 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- removed support for the parameter <code>comment</code> in the <code>ip ipsec mode\-config</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- removed support for the parameter <code>default\-mount\-point\-template</code> in the <code>disk settings</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- removed support for the parameter <code>default</code> in the <code>caps\-man manager interface</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- removed support for the parameter <code>default</code> in the <code>interface lte apn</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- removed support for the parameter <code>default</code> in the <code>ip ipsec policy group</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- removed support for the parameter <code>default</code> in the <code>ip smb users</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- removed support for the parameter <code>default</code> in the <code>snmp community</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- removed support for the parameter <code>disabled</code> in the <code>interface wireless security\-profiles</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- removed support for the parameter <code>force\-aes</code> in the <code>interface sstp\-server server</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- removed support for the parameter <code>full\-duplex</code> in the <code>interface ethernet</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- removed support for the parameter <code>gmt\-offset</code> in the <code>system clock</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- removed support for the parameter <code>info</code> in the <code>mpls interface</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- removed support for the parameter <code>input\.accept\-unknown</code> in the <code>routing bgp connection</code> path for RouterOS \>\= 7\.19 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- removed support for the parameter <code>input\.accept\-unknown</code> in the <code>routing bgp template</code> path for RouterOS \>\= 7\.19 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- removed support for the parameter <code>memory\-frequency</code> in the <code>system routerboard settings</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- removed support for the parameter <code>mtu</code> in the <code>interface vrrp</code> path for RouterOS \>\= 7\.20 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- removed support for the parameter <code>route\-cache</code> in the <code>ip settings</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- removed support for the parameter <code>routing\-table</code> in the <code>ip firewall filter</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- removed support for the parameter <code>routing\-table</code> in the <code>ip firewall mangle</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- removed support for the parameter <code>tls\-host</code> in the <code>ip firewall nat</code> path for RouterOS \>\= 7\.16 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- removed support for the parameter <code>tls\-host</code> in the <code>ipv6 firewall nat</code> path for RouterOS \>\= 7\.16 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- removed support for the parameters <code>as\-override</code>\, <code>input\.limit\-nlri\-diversity</code> and <code>output\.default\-prepent</code> in the <code>routing bgp template</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- removed support for the parameters <code>cluster\-id</code> and <code>input\.ignore\-as\-path\-len</code> in the <code>routing bgp connection</code> path for RouterOS \>\= 7\.20 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- removed support for the parameters <code>cluster\-id</code> and <code>input\.ignore\-as\-path\-len</code> in the <code>routing bgp template</code> path for RouterOS \>\= 7\.20 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- removed support for the parameters <code>default</code> and <code>max\-sessions</code> in the <code>ip smb shares</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- removed support for the parameters <code>installed\-version</code>\, <code>latest\-version</code> and <code>status</code> in the <code>system package update</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- removed support for the parameters <code>layer7\-protocol</code> and <code>to\-addresses</code> in the <code>ipv6 firewall nat</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- removed support for the parameters <code>primary\-ntp</code>\, <code>secondary\-ntp</code> and <code>server\-dns\-names</code> in the <code>system ntp client</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- removed support for the parameters <code>route\-tag</code>\, <code>routing\-mark</code> and <code>type</code> in the <code>ip route</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- treat parameters <code>list</code> and <code>key</code> as primary keys for the <code>container envs</code> path on RouterOS versions \>\= 7\.20 \([https\://github\.com/ansible\-collections/community\.routeros/issues/449](https\://github\.com/ansible\-collections/community\.routeros/issues/449)\, [https\://github\.com/ansible\-collections/community\.routeros/pull/451](https\://github\.com/ansible\-collections/community\.routeros/pull/451)\)\.
* api\_modify \- defined <code>name</code> as primary key\, added default for <code>container\-mac\-address</code>\, allowed <code>comment</code> to be disabled for RouterOS path <code>interface veth</code> \([https\://github\.com/ansible\-collections/community\.routeros/issues/454](https\://github\.com/ansible\-collections/community\.routeros/issues/454)\, [https\://github\.com/ansible\-collections/community\.routeros/pull/455](https\://github\.com/ansible\-collections/community\.routeros/pull/455)\)\.
* api\_modify \- make <code>name</code> a primary key \(and thus required\) for the <code>container</code> path for RouterOS \>\=7\.19 \([https\://github\.com/ansible\-collections/community\.routeros/issues/443](https\://github\.com/ansible\-collections/community\.routeros/issues/443)\, [https\://github\.com/ansible\-collections/community\.routeros/pull/445](https\://github\.com/ansible\-collections/community\.routeros/pull/445)\)\.

<a id="community-sap-libs"></a>
#### community\.sap\_libs

* collection \- Update all license headers \([https\://github\.com/sap\-linuxlab/community\.sap\_libs/pull/82](https\://github\.com/sap\-linuxlab/community\.sap\_libs/pull/82)\)
* sap\_control\_exec\, sap\_hostctrl\_exec \- QoL and Error handling \([https\://github\.com/sap\-linuxlab/community\.sap\_libs/pull/81](https\://github\.com/sap\-linuxlab/community\.sap\_libs/pull/81)\)
* sap\_control\_exec\, sap\_hostctrl\_exec \- Refactor to use shared utilities \([https\://github\.com/sap\-linuxlab/community\.sap\_libs/pull/78](https\://github\.com/sap\-linuxlab/community\.sap\_libs/pull/78)\)
* sap\_hdbsql \- Add error handling and secure flags for hdbsql \([https\://github\.com/sap\-linuxlab/community\.sap\_libs/pull/75](https\://github\.com/sap\-linuxlab/community\.sap\_libs/pull/75)\)
* sap\_hdbsql \- Add new parameter named properties \([https\://github\.com/sap\-linuxlab/community\.sap\_libs/pull/79](https\://github\.com/sap\-linuxlab/community\.sap\_libs/pull/79)\)
* sap\_system\_facts \- Add SID and permission check to facts module \([https\://github\.com/sap\-linuxlab/community\.sap\_libs/pull/73](https\://github\.com/sap\-linuxlab/community\.sap\_libs/pull/73)\)
* sapcar\_extract \- Add overwrite mode and improve exist validation \([https\://github\.com/sap\-linuxlab/community\.sap\_libs/pull/77](https\://github\.com/sap\-linuxlab/community\.sap\_libs/pull/77)\)

<a id="fortinet-fortimanager"></a>
#### fortinet\.fortimanager

* Supported new environment variable \"ANSIBLE\_FORTIMANAGER\_ENABLE\_LOG\" to enable/disable logging for FortiManager Ansible Collection\.
* Supported new environment variable \"ANSIBLE\_FORTIMANAGER\_VERSION\_CHECK\" to enable/disable version checking performed by the FortiManager Ansible Collection\.
* Supported new schemas in FortiManager 7\.0\.16\, 7\.2\.12\, 7\.4\.9\, 7\.4\.10\, 7\.6\.5\, 7\.6\.6

<a id="google-cloud-1"></a>
#### google\.cloud

* gcp\_sql\_instance \- add <em class="title-reference">allocated\_ip\_range</em> to <em class="title-reference">settings\.ip\_configuration</em> for private IP Cloud SQL instances \(name of the allocated IP range in the VPC\) \([https\://github\.com/ansible\-collections/google\.cloud/pull/744](https\://github\.com/ansible\-collections/google\.cloud/pull/744)\)\.
* gcp\_vertexai\_\* \- added 18 Vertex AI modules \(gcp\_vertexai\_dataset\, gcp\_vertexai\_deployment\_resource\_pool\, gcp\_vertexai\_endpoint\, gcp\_vertexai\_endpoint\_with\_model\_garden\_deployment\, gcp\_vertexai\_feature\_group\, gcp\_vertexai\_feature\_group\_feature\, gcp\_vertexai\_feature\_online\_store\, gcp\_vertexai\_feature\_online\_store\_featureview\, gcp\_vertexai\_featurestore\, gcp\_vertexai\_featurestore\_entitytype\, gcp\_vertexai\_featurestore\_entitytype\_feature\, gcp\_vertexai\_index\, gcp\_vertexai\_index\_endpoint\, gcp\_vertexai\_index\_endpoint\_deployed\_index\, gcp\_vertexai\_metadata\_store\, gcp\_vertexai\_rag\_engine\_config\, gcp\_vertexai\_reasoning\_engine\, gcp\_vertexai\_tensorboard\) \([https\://github\.com/ansible\-collections/google\.cloud/pull/743](https\://github\.com/ansible\-collections/google\.cloud/pull/743)\)\.

<a id="hetzner-hcloud"></a>
#### hetzner\.hcloud

* primary\_ip \- Assign to new server if <code>server</code> is changed\.
* primary\_ip \- Unassign primary\_ip if <code>server</code> is null\.

<a id="netapp-ontap-1"></a>
#### netapp\.ontap

* na\_ontap\_lun \- updated documentation for unsupported REST parameters\.
* na\_ontap\_nfs \- new option <em class="title-reference">credential\_cache</em> added in REST\.
* na\_ontap\_snapmirror \- new options <em class="title-reference">time\_out</em>\, <em class="title-reference">wait\_for\_completion</em> added in REST\.
* na\_ontap\_snapmirror \- updated documentation for <em class="title-reference">identity\_preserve</em> and <em class="title-reference">max\_transfer\_rate</em>\.
* na\_ontap\_volume\_efficiency\- AWS Lambda support added to the module\.
* na\_ontap\_volume\_efficiency\- Added <em class="title-reference">wait\_for\_completion</em> and <em class="title-reference">time\_out</em> parameters to fix time out errors for long running operations\.

<a id="theforeman-foreman-1"></a>
#### theforeman\.foreman

* content\_view \- add support for lifecycle environments in rolling content views
* convert2rhel role \- removed subscription support as it\'s been unused since Katello 4\.12 \(05/2024\)
* locations role \- Added <code>state</code> parameter to manage resource presence\.

<a id="vmware-vmware"></a>
#### vmware\.vmware

* cluster\_ha \- Add value to allow disabling admission control policy Fixes [https\://github\.com/ansible\-collections/vmware\.vmware/issues/227](https\://github\.com/ansible\-collections/vmware\.vmware/issues/227)
* vm \- Add the ability to set the annotation of a VM\. Fixes [https\://github\.com/ansible\-collections/vmware\.vmware/issues/310](https\://github\.com/ansible\-collections/vmware\.vmware/issues/310)
* vm\_list\_group\_by\_clusters\_info \- Add the ability to use the absolute path for the group name\. This can be used to avoid group name collisions\. Fixes [https\://github\.com/ansible\-collections/vmware\.vmware/issues/297](https\://github\.com/ansible\-collections/vmware\.vmware/issues/297)
* vms \- Add setting to disable population of ansible\_host to the inventory Fixes [https\://github\.com/ansible\-collections/vmware\.vmware/pull/317](https\://github\.com/ansible\-collections/vmware\.vmware/pull/317)

<a id="vultr-cloud"></a>
#### vultr\.cloud

* Added pagination support by adding <code>api\_results\_per\_page</code> to the common attributes\.
* bare\_metal \- Added support for multi\-disk operation mode by adding <code>mdisk\_mode</code> to the attributes \([https\://github\.com/vultr/ansible\-collection\-vultr/issues/165](https\://github\.com/vultr/ansible\-collection\-vultr/issues/165)\)\.
* object\_storage \- Object storage subscriptions require specifying a tier upon creation\, added <code>tier</code> to the attributes \([https\://github\.com/vultr/ansible\-collection\-vultr/issues/135](https\://github\.com/vultr/ansible\-collection\-vultr/issues/135)\)\.
* snapshot \- Added UEFI support adding <code>uefi</code> to the attributes \([https\://github\.com/vultr/ansible\-collection\-vultr/pull/160](https\://github\.com/vultr/ansible\-collection\-vultr/pull/160)\)\.

<a id="breaking-changes--porting-guide"></a>
### Breaking Changes / Porting Guide

<a id="community-mysql-1"></a>
#### community\.mysql

* Update imports from ansible\.module\_utils\.six to use their python3 equivalent\. This change will make this collection incompatible for managed hosts on python2\.7\.

<a id="community-proxmox-2"></a>
#### community\.proxmox

* proxmox \- set <code>state</code> as not <code>optional</code> and assign default value <code>present</code> \([https\://github\.com/ansible\-collections/community\.proxmox/pull/292](https\://github\.com/ansible\-collections/community\.proxmox/pull/292)\)\.

<a id="deprecated-features-1"></a>
### Deprecated Features

<a id="community-general-4"></a>
#### community\.general

* aix\_devices \- module is superseded by equivalent in <code>ibm\.power\_aix</code> collection\. It will be removed from community\.general 15\.0\.0 \([https\://github\.com/ansible\-collections/community\.general/issues/11290](https\://github\.com/ansible\-collections/community\.general/issues/11290)\, [https\://github\.com/ansible\-collections/community\.general/pull/11540](https\://github\.com/ansible\-collections/community\.general/pull/11540)\)\.
* aix\_filesystem \- module is superseded by equivalent in <code>ibm\.power\_aix</code> collection\. It will be removed from community\.general 15\.0\.0 \([https\://github\.com/ansible\-collections/community\.general/issues/11290](https\://github\.com/ansible\-collections/community\.general/issues/11290)\, [https\://github\.com/ansible\-collections/community\.general/pull/11540](https\://github\.com/ansible\-collections/community\.general/pull/11540)\)\.
* aix\_inittab \- module is superseded by equivalent in <code>ibm\.power\_aix</code> collection\. It will be removed from community\.general 15\.0\.0 \([https\://github\.com/ansible\-collections/community\.general/issues/11290](https\://github\.com/ansible\-collections/community\.general/issues/11290)\, [https\://github\.com/ansible\-collections/community\.general/pull/11540](https\://github\.com/ansible\-collections/community\.general/pull/11540)\)\.
* aix\_lvg \- module is superseded by equivalent in <code>ibm\.power\_aix</code> collection\. It will be removed from community\.general 15\.0\.0 \([https\://github\.com/ansible\-collections/community\.general/issues/11290](https\://github\.com/ansible\-collections/community\.general/issues/11290)\, [https\://github\.com/ansible\-collections/community\.general/pull/11540](https\://github\.com/ansible\-collections/community\.general/pull/11540)\)\.
* aix\_lvol \- module is superseded by equivalent in <code>ibm\.power\_aix</code> collection\. It will be removed from community\.general 15\.0\.0 \([https\://github\.com/ansible\-collections/community\.general/issues/11290](https\://github\.com/ansible\-collections/community\.general/issues/11290)\, [https\://github\.com/ansible\-collections/community\.general/pull/11540](https\://github\.com/ansible\-collections/community\.general/pull/11540)\)\.
* monit \- support for Monit version 5\.18 or older is deprecated and will be removed in community\.general 14\.0\.0 \([https\://github\.com/ansible\-collections/community\.general/pull/11254](https\://github\.com/ansible\-collections/community\.general/pull/11254)\)\.
* puppet \- the <code>timeout</code> parameter is deprecated and will be removed in community\.general 14\.0\.0\. \([https\://github\.com/ansible\-collections/community\.general/pull/11658](https\://github\.com/ansible\-collections/community\.general/pull/11658)\)\.

<a id="community-proxmox-3"></a>
#### community\.proxmox

* proxmox \- Certificate verification default changes from <code>false</code> to <code>true</code> with version 2\.0\.0 \([https\://github\.com/ansible\-collections/community\.proxmox/pull/256](https\://github\.com/ansible\-collections/community\.proxmox/pull/256)\)\.

<a id="security-fixes"></a>
### Security Fixes

<a id="amazon-aws-1"></a>
#### amazon\.aws

* arn \- fix potential ReDoS vulnerability in ARN parsing regex by using negated character class instead of non\-greedy quantifier \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2884](https\://github\.com/ansible\-collections/amazon\.aws/pull/2884)\)\.
* ec2\_security\_group \- fix potential ReDoS vulnerability in security group ID parsing regex by using negated character classes and adding end anchor \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2884](https\://github\.com/ansible\-collections/amazon\.aws/pull/2884)\)\.

<a id="ansible-windows-1"></a>
#### ansible\.windows

* win\_dns\_record \- Fixed a security risk where <code>AllowUpdateAny</code> was hardcoded for non\-SRV records\, allowing any authenticated user to update DNS records\. Added a new parameter <code>allow\_update\_any</code> which defaults to <code>false</code> \([https\://issues\.redhat\.com/browse/ACA\-5193](https\://issues\.redhat\.com/browse/ACA\-5193)\)\.

<a id="bugfixes-1"></a>
### Bugfixes

<a id="ansible-core-5"></a>
#### Ansible\-core

* Fix up <code>powershell</code> shell commands when using a connection plugin that does not support stdin/pipeline input \- [https\://github\.com/ansible/ansible/issues/86397](https\://github\.com/ansible/ansible/issues/86397)
* ansible\-connection \- Prevent unpickling failures in module contexts by ensuring that AnsibleTaggedObjects in pickled responses are converted to plain types in <code>JsonRpcServer</code>\.
* config lookup now uses preexisting constants for templating when needed\.
* rpm\_key \- Use librpm library API instead of gpg utility to support version 6 PGP keys \([https\://github\.com/ansible/ansible/issues/86157](https\://github\.com/ansible/ansible/issues/86157)\)\.
* yaml loading \- Fix traceback when parsing YAML strings \(not files\) when using the pure Python implementation of PyYAML\.

<a id="amazon-aws-2"></a>
#### amazon\.aws

* aws\_ssm \- Fixed connection being re\-established on every loop iteration\. The plugin now properly establishes a single connection for a loop \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2869](https\://github\.com/ansible\-collections/amazon\.aws/pull/2869)\)\.
* elb\_application\_lb \- fixed comparison of multi\-rule default actions to properly handle the <code>Order</code> field when determining if listener modifications are needed \([https\://github\.com/ansible\-collections/amazon\.aws/issues/2537](https\://github\.com/ansible\-collections/amazon\.aws/issues/2537)\)\.
* elb\_application\_lb \- fixed error where creating a new application load balancer with listener rules would fail with <code>Parameter validation failed\: Invalid type for parameter ListenerArn\, value\: None</code> \([https\://github\.com/ansible\-collections/amazon\.aws/issues/2400](https\://github\.com/ansible\-collections/amazon\.aws/issues/2400)\)\.
* s3\_object \- fixed error when using PUT with an empty <code>content</code> string \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2810](https\://github\.com/ansible\-collections/amazon\.aws/pull/2810)\)

<a id="ansible-windows-2"></a>
#### ansible\.windows

* Stop using the deprecated text module\_utils in Ansible that will be removed in Ansible <code>2\.24</code>\.
* win\_dhcp\_lease \- when creating a reservation\, the dns\_name will be used as reservation\_name in case that is not provided\; will be discarded otherwise as the parameter HostName is not supported by Add\-DhcpServerv4Reservation \([https\://github\.com/ansible\-collections/ansible\.windows/issues/813](https\://github\.com/ansible\-collections/ansible\.windows/issues/813)\)
* win\_file \- Fix idempotency issues when using <code>state\: touch</code> \([https\://github\.com/ansible\-collections/ansible\.windows/issues/798](https\://github\.com/ansible\-collections/ansible\.windows/issues/798)\)
* win\_hotfix \- Fix a bug in Get\-HotfixMetadataFromKB fallback logic where it would fail to return metadata even if the hotfix was found\.
* win\_hotfix \- Fix idempotency issue where some multi\-package MSUs \(e\.g\. SSU \+ CU\) were incorrectly reported as installed by DISM even if the CU was missing\. Added a secondary check using Get\-Hotfix to verify installation\.
* win\_products\_facts \- return string for all the license related facts \([https\://github\.com/ansible\-collections/community\.windows/issues/661](https\://github\.com/ansible\-collections/community\.windows/issues/661)\)\.
* win\_reboot \- fix unhandled error when <code>\.exe</code> not present in <code>PATHEXT</code> environment variable
* win\_shell \- Ensure the default <code>executable</code> uses the absolute path to <code>powershell\.exe</code> rather than looking it up in the <code>PATH</code> environment\.

<a id="cisco-meraki-2"></a>
#### cisco\.meraki

* Fixing problem of naming in organizations\_appliance\_vpn\_third\_party\_vpnpeers\_info\.
* Restructuring README\.md file\.

<a id="community-dns-1"></a>
#### community\.dns

* Update Public Suffix List\.
* hetzner\_\* modules and hetzner\_dns\_records inventory plugin \- retry on network problems and certain HTTP codes \(502\, 503\, 504\) \([https\://github\.com/ansible\-collections/community\.dns/pull/313](https\://github\.com/ansible\-collections/community\.dns/pull/313)\)\.
* hetzner\_dns\_record\_sets \- when doing batch updates\, do not request status updates for too many actions at once \([https\://github\.com/ansible\-collections/community\.dns/issues/312](https\://github\.com/ansible\-collections/community\.dns/issues/312)\, [https\://github\.com/ansible\-collections/community\.dns/pull/313](https\://github\.com/ansible\-collections/community\.dns/pull/313)\)\.
* hosttech\_\* modules and hosttech\_dns\_records inventory plugin \- when using the JSON API\, retry on network problems and certain HTTP codes \(502\, 503\, 504\) \([https\://github\.com/ansible\-collections/community\.dns/pull/313](https\://github\.com/ansible\-collections/community\.dns/pull/313)\)\.

<a id="community-general-5"></a>
#### community\.general

* counter\_enabled callback plugin \- fix plugin not observing <code>display\_ok\_hosts</code> option \([https\://github\.com/ansible\-collections/community\.general/issues/3978](https\://github\.com/ansible\-collections/community\.general/issues/3978)\, [https\://github\.com/ansible\-collections/community\.general/pull/11656](https\://github\.com/ansible\-collections/community\.general/pull/11656)\)\.
* ipa\_dnsrecord \- fix idempotency bug when using <code>dnsttl</code> due to wrong Python types \([https\://github\.com/ansible\-collections/community\.general/pull/11559](https\://github\.com/ansible\-collections/community\.general/pull/11559)\)\.
* keycloak\_authentication \- fix <code>TypeError</code> crash when a flow is defined without <code>authenticationExecutions</code> \([https\://github\.com/ansible\-collections/community\.general/issues/11547](https\://github\.com/ansible\-collections/community\.general/issues/11547)\, [https\://github\.com/ansible\-collections/community\.general/pull/11548](https\://github\.com/ansible\-collections/community\.general/pull/11548)\)\.
* nictagadm \- add a condition to the if statement so that <code>is\_valid\_mac\(\)</code> does not get called if <code>etherstub</code> is false \([https\://github\.com/ansible\-collections/community\.general/pull/11589](https\://github\.com/ansible\-collections/community\.general/pull/11589)\)\.
* nmcli \- add missing <code>ipv6\.routing\-rules</code> to <code>settings\_type\(\)</code> list type\, preventing <code>routing\_rules6</code> list from being corrupted \([https\://github\.com/ansible\-collections/community\.general/issues/11630](https\://github\.com/ansible\-collections/community\.general/issues/11630)\, [https\://github\.com/ansible\-collections/community\.general/pull/11635](https\://github\.com/ansible\-collections/community\.general/pull/11635)\)\.
* open\_iscsi \- fix IPv6 portal address formatting\; iscsiadm requires bracket notation for IPv6 addresses but the module was producing an incorrect format \([https\://github\.com/ansible\-collections/community\.general/issues/4467](https\://github\.com/ansible\-collections/community\.general/issues/4467)\, [https\://github\.com/ansible\-collections/community\.general/pull/11657](https\://github\.com/ansible\-collections/community\.general/pull/11657)\)\.
* xfconf \- representation of boolean properties was not consistent between Python and <code>xfconf\-query</code>\, leading to broken idempotency \([https\://github\.com/ansible\-collections/community\.general/pull/11645](https\://github\.com/ansible\-collections/community\.general/pull/11645)\)\.

<a id="community-hrobot"></a>
#### community\.hrobot

* Remove unnecessary Python 2 compatibilty code \([https\://github\.com/ansible\-collections/community\.hrobot/pull/187](https\://github\.com/ansible\-collections/community\.hrobot/pull/187)\)\.

<a id="community-mysql-2"></a>
#### community\.mysql

* mysql\_user \- When creating a new user\, and specifying parsec as plugin it wil generate the wrong SQL query\. It should be added to the same plugin check as ed25519 so that it generates a query using USING PASSWORDS\(\%s\) instead of BY \%s \([https\://github\.com/ansible\-collections/community\.mysql/pull/779](https\://github\.com/ansible\-collections/community\.mysql/pull/779)\)\.

<a id="community-proxmox-4"></a>
#### community\.proxmox

* proxmox\_cluster \- make cluster join idempotent \([https\://github\.com/ansible\-collections/community\.proxmox/pull/244](https\://github\.com/ansible\-collections/community\.proxmox/pull/244)\)\.
* proxmox\_disk \- make none iso disk idempotent \([https\://github\.com/ansible\-collections/community\.proxmox/pull/288](https\://github\.com/ansible\-collections/community\.proxmox/pull/288)\)\.
* proxmox\_firewall \- Enable ipsets on vm level and fix bugs regarding the cidr notation the proxmox api expects \([https\://github\.com/ansible\-collections/community\.proxmox/pull/248](https\://github\.com/ansible\-collections/community\.proxmox/pull/248)\)\.
* proxmox\_role \- when privs is omitted\, keep existing role privileges unchanged instead of treating it as no privileges \([https\://github\.com/ansible\-collections/community\.proxmox/pull/284](https\://github\.com/ansible\-collections/community\.proxmox/pull/284)\)\.

<a id="community-routeros-4"></a>
#### community\.routeros

* api\_info\, api\_modify \- removed support for several parameters \(<code>shared\-buffers\-color</code>\, <code>shared\-pool0</code>\-<code>shared\-pool7</code>\, <code>treat\-yellow\-as</code>\, <code>wred\-shared\-threshold</code>\, <code>wred\-threshold</code>\) in the <code>interface ethernet switch qos settings</code> path for RouterOS \<7\.16 \([https\://github\.com/ansible\-collections/community\.routeros/pull/450](https\://github\.com/ansible\-collections/community\.routeros/pull/450)\)\.
* api\_info\, api\_modify \- removed support for the parameter <code>color</code> in the <code>interface ethernet switch qos profile</code> path for RouterOS \<7\.16 \([https\://github\.com/ansible\-collections/community\.routeros/pull/450](https\://github\.com/ansible\-collections/community\.routeros/pull/450)\)\.
* api\_info\, api\_modify \- removed support for the parameter <code>ecn</code> in the <code>interface ethernet switch qos tx\-manager</code> path for RouterOS \<7\.16 \([https\://github\.com/ansible\-collections/community\.routeros/pull/450](https\://github\.com/ansible\-collections/community\.routeros/pull/450)\)\.
* api\_info\, api\_modify \- removed support for the parameter <code>enabled</code> in the <code>interface ovpn\-server server</code> path for RouterOS \>\=7\.17 \([https\://github\.com/ansible\-collections/community\.routeros/pull/450](https\://github\.com/ansible\-collections/community\.routeros/pull/450)\)\.
* api\_info\, api\_modify \- removed support for the parameter <code>envlist</code> \(replaced by <code>envlists</code>\) in the <code>container</code> path for RouterOS \<7\.20 \([https\://github\.com/ansible\-collections/community\.routeros/pull/450](https\://github\.com/ansible\-collections/community\.routeros/pull/450)\)\.
* api\_info\, api\_modify \- removed support for the parameter <code>fasttrack\-hw</code> in the <code>interface ethernet switch l3hw\-settings</code> path for RouterOS \<7\.16 \([https\://github\.com/ansible\-collections/community\.routeros/pull/450](https\://github\.com/ansible\-collections/community\.routeros/pull/450)\)\.
* api\_info\, api\_modify \- removed support for the parameter <code>import\.router\-id</code> in the <code>routing bgp vpn</code> path for RouterOS \<7\.20 \([https\://github\.com/ansible\-collections/community\.routeros/pull/450](https\://github\.com/ansible\-collections/community\.routeros/pull/450)\)\.
* api\_info\, api\_modify \- removed support for the parameter <code>min\-echo\-rx</code> in the <code>routing bfd configuration</code> path for RouterOS \<7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/450](https\://github\.com/ansible\-collections/community\.routeros/pull/450)\)\.
* api\_info\, api\_modify \- removed support for the parameter <code>mounts</code> \(replaced by <code>mount</code>\) in the <code>container</code> path for RouterOS \<7\.21 \([https\://github\.com/ansible\-collections/community\.routeros/pull/450](https\://github\.com/ansible\-collections/community\.routeros/pull/450)\)\.
* api\_info\, api\_modify \- removed support for the parameter <code>name</code> in the <code>container envs</code> path for RouterOS \<7\.20 \([https\://github\.com/ansible\-collections/community\.routeros/pull/450](https\://github\.com/ansible\-collections/community\.routeros/pull/450)\)\.
* api\_info\, api\_modify \- removed support for the parameter <code>name</code> in the <code>container mounts</code> path for RouterOS \<7\.21 \([https\://github\.com/ansible\-collections/community\.routeros/pull/450](https\://github\.com/ansible\-collections/community\.routeros/pull/450)\)\.
* api\_info\, api\_modify \- removed support for the parameter <code>nvme\-tcp\-name</code> in the <code>disk</code> path for RouterOS \<7\.21 \([https\://github\.com/ansible\-collections/community\.routeros/pull/450](https\://github\.com/ansible\-collections/community\.routeros/pull/450)\)\.
* api\_info\, api\_modify \- removed support for the parameter <code>partial\-offload\-chunk</code> in the <code>interface ethernet switch l3hw\-settings advanced</code> path for RouterOS \<7\.18 \([https\://github\.com/ansible\-collections/community\.routeros/pull/450](https\://github\.com/ansible\-collections/community\.routeros/pull/450)\)\.
* api\_info\, api\_modify \- removed support for the parameter <code>pfc</code> in the <code>interface ethernet switch qos port</code> path for RouterOS \<7\.16 \([https\://github\.com/ansible\-collections/community\.routeros/pull/450](https\://github\.com/ansible\-collections/community\.routeros/pull/450)\)\.
* api\_info\, api\_modify \- removed support for the parameter <code>port</code> in the <code>interface vxlan vteps</code> path for RouterOS \<7\.18 \([https\://github\.com/ansible\-collections/community\.routeros/pull/450](https\://github\.com/ansible\-collections/community\.routeros/pull/450)\)\.
* api\_info\, api\_modify \- removed support for the parameter <code>ports</code> in the <code>interface bridge mdb</code> path for RouterOS \<7\.19 \([https\://github\.com/ansible\-collections/community\.routeros/pull/450](https\://github\.com/ansible\-collections/community\.routeros/pull/450)\)\.
* api\_info\, api\_modify \- removed support for the parameter <code>ram\-high</code> in the <code>container config</code> path for RouterOS \<7\.20 \([https\://github\.com/ansible\-collections/community\.routeros/pull/450](https\://github\.com/ansible\-collections/community\.routeros/pull/450)\)\.
* api\_info\, api\_modify \- removed support for the parameter <code>remote\-addrs</code> \(replaced by <code>remote\-address</code>\) and <code>status</code> in the <code>file sync</code> path for RouterOS \<7\.16 \([https\://github\.com/ansible\-collections/community\.routeros/pull/450](https\://github\.com/ansible\-collections/community\.routeros/pull/450)\)\.
* api\_info\, api\_modify \- removed support for the parameter <code>src\-address</code> in the <code>iot lora</code> and <code>lora</code> paths for RouterOS \<7\.19 \([https\://github\.com/ansible\-collections/community\.routeros/pull/450](https\://github\.com/ansible\-collections/community\.routeros/pull/450)\)\.
* api\_info\, api\_modify \- removed support for the parameter <code>start\-tls</code> \(default <code>False</code>\) in the <code>tool e\-mail</code> path for RouterOS \<7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/450](https\://github\.com/ansible\-collections/community\.routeros/pull/450)\)\.
* api\_info\, api\_modify \- removed support for the parameter <code>vrf</code> in the <code>interface vxlan</code> path for RouterOS \<7\.20 \([https\://github\.com/ansible\-collections/community\.routeros/pull/450](https\://github\.com/ansible\-collections/community\.routeros/pull/450)\)\.
* api\_info\, api\_modify \- removed support for the parameters <code>rssi\-off</code> and <code>tx\-enabled</code> in the <code>iot lora radios</code> and <code>lora radios</code> paths for RouterOS \<7\.17 \([https\://github\.com/ansible\-collections/community\.routeros/pull/450](https\://github\.com/ansible\-collections/community\.routeros/pull/450)\)\.
* api\_info\, api\_modify \- removed support for the parameters <code>shared\-pool\-index</code> and <code>wred</code> in the <code>interface ethernet switch qos tx\-manager queue</code> path for RouterOS \<7\.16 \([https\://github\.com/ansible\-collections/community\.routeros/pull/450](https\://github\.com/ansible\-collections/community\.routeros/pull/450)\)\.
* api\_modify \- fix idempotency for <code>container mounts</code> path on RouterOS 7\.22\+ where for <code>dst</code> and <code>src</code>\, values without a leading <code>/</code> \(e\.g\. <code>TEST</code>\) were not recognised as matching the normalised value returned by RouterOS \(<code>/TEST</code>\)\, causing spurious updates on every run \([https\://github\.com/ansible\-collections/community\.routeros/issues/449](https\://github\.com/ansible\-collections/community\.routeros/issues/449)\, [https\://github\.com/ansible\-collections/community\.routeros/pull/452](https\://github\.com/ansible\-collections/community\.routeros/pull/452)\)\.

<a id="fortinet-fortios-3"></a>
#### fortinet\.fortios

* Fixed an issue where users were required to specify a password confirmation when using the system\_admin and system\_api\_user modules in FortiOS 7\.6\.5 and later\.
* Fixed the issue that getting an error \"BadGzipFile\" when using token for authentication in new versions of FortiOS\.

<a id="netapp-ontap-2"></a>
#### netapp\.ontap

* na\_ontap\_export\_policy\_rule \- Fixed issue where rule\_index was not being applied to create body\, and added logic to detect when a create action is actually a re\-index of an existing rule\.
* na\_ontap\_lun \- Updated module with alias <em class="title-reference">volume\_name</em> for <em class="title-reference">flexvol\_name</em>\.
* na\_ontap\_qtree \- Updated module with alias <em class="title-reference">volume\_name</em> for <em class="title-reference">flexvol\_name</em>\.
* na\_ontap\_service\_processor\_network \- fixed issue with interface state not being applied correctly\, resolved ipv6 comparison issue and idempotency issue with ZAPI abd REST\.
* na\_ontap\_snapmirror\_policy \- updated examples for creating and modifying snapmirror policy\.
* na\_ontap\_user\_role \- Removed special handling of <em class="title-reference">DEFAULT</em> path and normalized empty query in privileges to None for consistency\.
* na\_ontap\_volume \- Fixed issue with volume rename\.
* na\_ontap\_vserver\_audit \- updated documentation for <em class="title-reference">log</em>\.

<a id="theforeman-foreman-2"></a>
#### theforeman\.foreman

* content\_view\_filter\_rule \- fix content\_filter\_rule\_deb\_spec to take into account desired versions

<a id="vmware-vmware-1"></a>
#### vmware\.vmware

* cluster\_info \- When a user does not specify a cluster name\, the module will now search recursively for clusters in the datacenter\. Fixes [https\://github\.com/ansible\-collections/vmware\.vmware/issues/303](https\://github\.com/ansible\-collections/vmware\.vmware/issues/303)
* cluster\_info \- When a user specifies a datacenter name\, the module will now fail if that datacenter is not found instead of silently continuing\. Fixes [https\://github\.com/ansible\-collections/vmware\.vmware/issues/303](https\://github\.com/ansible\-collections/vmware\.vmware/issues/303)
* inventory plugins \- fix handling of encrypted strings in inventory plugin username and password options for ansible\-core\<\=2\.19 fixes [https\://github\.com/ansible\-collections/vmware\.vmware/issues/304](https\://github\.com/ansible\-collections/vmware\.vmware/issues/304)

<a id="vultr-cloud-1"></a>
#### vultr\.cloud

* dns\_domain \- Removed requirement for the <code>ip</code> argument when creating a new domain \([https\://github\.com/vultr/ansible\-collection\-vultr/issues/140](https\://github\.com/vultr/ansible\-collection\-vultr/issues/140)\)\.
* instance\, bare\_metal \- Fixed an issue where the <code>user\_data</code> response returned a JSON serialization error \([https\://github\.com/vultr/ansible\-collection\-vultr/issues/156](https\://github\.com/vultr/ansible\-collection\-vultr/issues/156)\)\.
* startup\_script \- Fixed an issue where the <code>script</code> response returned a JSON serialization error \([https\://github\.com/vultr/ansible\-collection\-vultr/pull/162](https\://github\.com/vultr/ansible\-collection\-vultr/pull/162)\)\.

<a id="known-issues-1"></a>
### Known Issues

<a id="community-routeros-5"></a>
#### community\.routeros

* api\_modify \- to create or modify entries in the <code>container</code> path\, you need librouteros 4\.0\.0 or newer due to a bug preventing older versions from setting or modifying properties named <code>cmd</code> \([https\://github\.com/ansible\-collections/community\.routeros/issues/442](https\://github\.com/ansible\-collections/community\.routeros/issues/442)\)\.

<a id="new-modules-1"></a>
### New Modules

<a id="ansible-windows-3"></a>
#### ansible\.windows

* ansible\.windows\.dsc3 \- Sets or checks DSC v3 configuration state

<a id="cisco-mso-1"></a>
#### cisco\.mso

* cisco\.mso\.ndo\_endpoint\_ip\_tag\_policy \- Manage Endpoint IP Tag Policies on Cisco Nexus Dashboard Orchestrator \(NDO\)\.
* cisco\.mso\.ndo\_endpoint\_mac\_tag\_policy \- Manage Endpoint MAC Tag Policies on Cisco Nexus Dashboard Orchestrator \(NDO\)\.
* cisco\.mso\.ndo\_template\_deploy \- Deploy templates to sites on Cisco Nexus Dashboard Orchestrator \(NDO\)\.
* cisco\.mso\.ndo\_tenant\_netflow\_record \- Manage NetFlow Record on Cisco Nexus Dashboard Orchestrator \(NDO\)\.

<a id="community-general-6"></a>
#### community\.general

* community\.general\.github\_secrets \- Manage GitHub repository or organization secrets\.
* community\.general\.github\_secrets\_info \- List GitHub repository or organization secrets\.
* community\.general\.keycloak\_authentication\_v2 \- Configure authentication flows in Keycloak in an idempotent and safe manner\.
* community\.general\.logrotate \- Manage logrotate configurations\.

<a id="community-proxmox-5"></a>
#### community\.proxmox

* community\.proxmox\.proxmox\_role \- Role management for Proxmox VE cluster\.

<a id="fortinet-fortimanager-1"></a>
#### fortinet\.fortimanager

* fortinet\.fortimanager\.fmgr\_devprof\_system\_template\_interface \- System template system template interface
* fortinet\.fortimanager\.fmgr\_devprof\_system\_template\_interface\_iprange \- System template system template interface ip range
* fortinet\.fortimanager\.fmgr\_fmg\_script \- Fmg script
* fortinet\.fortimanager\.fmgr\_fmg\_script\_schedule \- Fmg script schedule
* fortinet\.fortimanager\.fmgr\_securityconsole\_template\_validate \- Securityconsole template validate
* fortinet\.fortimanager\.fmgr\_system\_locallog\_tacacsaccounting\_filter \- Cli system locallog tacacs\+accounting filter
* fortinet\.fortimanager\.fmgr\_system\_locallog\_tacacsaccounting\_setting \- Cli system locallog tacacs\+accounting setting
* fortinet\.fortimanager\.fmgr\_system\_log\_apiratelimit \- Cli system log api ratelimit
* fortinet\.fortimanager\.fmgr\_system\_log\_settings\_clientcertauth \- Cli system log settings client cert auth

<a id="netapp-ontap-3"></a>
#### netapp\.ontap

* netapp\.ontap\.na\_ontap\_autoupdate\_config \- NetApp ONTAP module to manage configurations for automatic updates\.
* netapp\.ontap\.na\_ontap\_cg \- NetApp ONTAP module to manage operations related to consistency groups\.

<a id="theforeman-foreman-3"></a>
#### theforeman\.foreman

* theforeman\.foreman\.smart\_proxy\_refresh \- Refresh Smart Proxy features

<a id="vultr-cloud-2"></a>
#### vultr\.cloud

* vultr\.cloud\.load\_balancer \- Manages load balancers on Vultr
* vultr\.cloud\.load\_balancer\_info \- Get information about Vultr load balancers
* vultr\.cloud\.object\_storage\_cluster\_info \- Get information about the Vultr object storage clusters
* vultr\.cloud\.object\_storage\_info \- Get information about the Vultr object stores

<a id="unchanged-collections-1"></a>
### Unchanged Collections

* ansible\.netcommon \(still version 8\.4\.0\)
* ansible\.posix \(still version 2\.1\.0\)
* ansible\.utils \(still version 6\.0\.1\)
* arista\.eos \(still version 12\.0\.1\)
* awx\.awx \(still version 24\.6\.1\)
* chocolatey\.chocolatey \(still version 1\.5\.3\)
* cisco\.aci \(still version 2\.13\.0\)
* cisco\.dnac \(still version 6\.48\.0\)
* cisco\.ios \(still version 11\.3\.0\)
* cisco\.iosxr \(still version 12\.1\.1\)
* cisco\.nxos \(still version 11\.1\.3\)
* cisco\.ucs \(still version 1\.16\.0\)
* cloudscale\_ch\.cloud \(still version 2\.5\.3\)
* community\.aws \(still version 10\.1\.0\)
* community\.ciscosmb \(still version 1\.0\.11\)
* community\.crypto \(still version 3\.1\.1\)
* community\.grafana \(still version 2\.3\.0\)
* community\.hashi\_vault \(still version 7\.1\.0\)
* community\.library\_inventory\_filtering\_v1 \(still version 1\.1\.5\)
* community\.libvirt \(still version 2\.1\.0\)
* community\.mongodb \(still version 1\.7\.12\)
* community\.okd \(still version 5\.0\.0\)
* community\.postgresql \(still version 4\.2\.0\)
* community\.proxysql \(still version 1\.7\.0\)
* community\.rabbitmq \(still version 1\.6\.0\)
* community\.sops \(still version 2\.2\.7\)
* community\.vmware \(still version 6\.2\.0\)
* community\.windows \(still version 3\.1\.0\)
* community\.zabbix \(still version 4\.1\.1\)
* containers\.podman \(still version 1\.19\.0\)
* cyberark\.conjur \(still version 1\.3\.9\)
* dellemc\.enterprise\_sonic \(still version 3\.2\.0\)
* dellemc\.openmanage \(still version 10\.0\.1\)
* dellemc\.powerflex \(still version 3\.0\.0\)
* dellemc\.unity \(still version 2\.1\.0\)
* f5networks\.f5\_modules \(still version 1\.39\.0\)
* grafana\.grafana \(still version 6\.0\.6\)
* hitachivantara\.vspone\_block \(still version 4\.6\.1\)
* hitachivantara\.vspone\_object \(still version 1\.1\.1\)
* ibm\.storage\_virtualize \(still version 3\.2\.0\)
* ieisystem\.inmanage \(still version 4\.0\.0\)
* infinidat\.infinibox \(still version 1\.6\.3\)
* infoblox\.nios\_modules \(still version 1\.9\.0\)
* inspur\.ispim \(still version 2\.2\.4\)
* junipernetworks\.junos \(still version 11\.0\.0\)
* kaytus\.ksmanage \(still version 2\.0\.0\)
* kubernetes\.core \(still version 6\.3\.0\)
* lowlydba\.sqlserver \(still version 2\.7\.0\)
* microsoft\.ad \(still version 1\.10\.0\)
* microsoft\.iis \(still version 1\.1\.0\)
* netapp\.cloudmanager \(still version 21\.24\.0\)
* netapp\.storagegrid \(still version 21\.16\.0\)
* netapp\_eseries\.santricity \(still version 1\.4\.1\)
* netbox\.netbox \(still version 3\.22\.0\)
* ngine\_io\.cloudstack \(still version 3\.0\.0\)
* openstack\.cloud \(still version 2\.5\.0\)
* ovirt\.ovirt \(still version 3\.2\.2\)
* pcg\.alpaca\_operator \(still version 2\.2\.0\)
* purestorage\.flasharray \(still version 1\.42\.0\)
* purestorage\.flashblade \(still version 1\.24\.0\)
* ravendb\.ravendb \(still version 1\.0\.4\)
* splunk\.es \(still version 4\.0\.0\)
* telekom\_mms\.icinga\_director \(still version 2\.5\.1\)
* vmware\.vmware\_rest \(still version 4\.10\.0\)
* vyos\.vyos \(still version 6\.0\.0\)

<a id="v13-4-0"></a>
## v13\.4\.0

- <a href="#release-summary-2">Release Summary</a>
- <a href="#ansible-core-6">Ansible\-core</a>
- <a href="#changed-collections-2">Changed Collections</a>
- <a href="#major-changes-2">Major Changes</a>
    - <a href="#containers-podman-2">containers\.podman</a>
- <a href="#minor-changes-2">Minor Changes</a>
    - <a href="#ansible-core-7">Ansible\-core</a>
    - <a href="#ansible-netcommon-3">ansible\.netcommon</a>
    - <a href="#cisco-dnac">cisco\.dnac</a>
    - <a href="#cisco-ios">cisco\.ios</a>
    - <a href="#community-aws">community\.aws</a>
    - <a href="#community-general-7">community\.general</a>
    - <a href="#community-libvirt-2">community\.libvirt</a>
    - <a href="#community-mysql-3">community\.mysql</a>
    - <a href="#containers-podman-3">containers\.podman</a>
    - <a href="#hitachivantara-vspone-block">hitachivantara\.vspone\_block</a>
    - <a href="#kubernetes-core">kubernetes\.core</a>
    - <a href="#vmware-vmware-rest">vmware\.vmware\_rest</a>
- <a href="#deprecated-features-2">Deprecated Features</a>
    - <a href="#community-aws-1">community\.aws</a>
    - <a href="#kubernetes-core-1">kubernetes\.core</a>
    - <a href="#vmware-vmware-rest-1">vmware\.vmware\_rest</a>
- <a href="#security-fixes-1">Security Fixes</a>
    - <a href="#kubernetes-core-2">kubernetes\.core</a>
- <a href="#bugfixes-2">Bugfixes</a>
    - <a href="#ansible-core-8">Ansible\-core</a>
    - <a href="#arista-eos">arista\.eos</a>
    - <a href="#cisco-ios-1">cisco\.ios</a>
    - <a href="#cisco-meraki-3">cisco\.meraki</a>
    - <a href="#community-aws-2">community\.aws</a>
    - <a href="#community-crypto-2">community\.crypto</a>
    - <a href="#community-dns-2">community\.dns</a>
    - <a href="#community-docker-2">community\.docker</a>
    - <a href="#community-general-8">community\.general</a>
    - <a href="#community-libvirt-3">community\.libvirt</a>
    - <a href="#containers-podman-4">containers\.podman</a>
    - <a href="#kubernetes-core-3">kubernetes\.core</a>
    - <a href="#purestorage-flasharray">purestorage\.flasharray</a>
- <a href="#new-plugins-1">New Plugins</a>
    - <a href="#callback">Callback</a>
- <a href="#new-modules-2">New Modules</a>
    - <a href="#cisco-ios-2">cisco\.ios</a>
    - <a href="#community-general-9">community\.general</a>
    - <a href="#community-libvirt-4">community\.libvirt</a>
    - <a href="#containers-podman-5">containers\.podman</a>
    - <a href="#hitachivantara-vspone-block-1">hitachivantara\.vspone\_block</a>
- <a href="#unchanged-collections-2">Unchanged Collections</a>

<a id="release-summary-2"></a>
### Release Summary

Release Date\: 2026\-02\-24

[Porting Guide](https\://docs\.ansible\.com/projects/ansible/devel/porting\_guides\.html)

<a id="ansible-core-6"></a>
### Ansible\-core

Ansible 13\.4\.0 contains ansible\-core version 2\.20\.3\.
This is a newer version than version 2\.20\.2 contained in the previous Ansible release\.

The changes are reported in the combined changelog below\.

<a id="changed-collections-2"></a>
### Changed Collections

If not mentioned explicitly\, the changes are reported in the combined changelog below\.

| Collection                  | Ansible 13.3.0 | Ansible 13.4.0 | Notes                                                    |
| --------------------------- | -------------- | -------------- | -------------------------------------------------------- |
| ansible.netcommon           | 8.2.1          | 8.4.0          |                                                          |
| arista.eos                  | 12.0.0         | 12.0.1         |                                                          |
| cisco.dnac                  | 6.44.0         | 6.48.0         |                                                          |
| cisco.ios                   | 11.2.0         | 11.3.0         |                                                          |
| cisco.meraki                | 2.22.0         | 2.22.1         |                                                          |
| community.aws               | 10.0.0         | 10.1.0         |                                                          |
| community.crypto            | 3.1.0          | 3.1.1          |                                                          |
| community.dns               | 3.5.1          | 3.5.2          |                                                          |
| community.docker            | 5.0.5          | 5.0.6          |                                                          |
| community.general           | 12.3.0         | 12.4.0         |                                                          |
| community.libvirt           | 2.0.0          | 2.1.0          |                                                          |
| community.mongodb           | 1.7.11         | 1.7.12         | There are no changes recorded in the changelog.          |
| community.mysql             | 4.0.1          | 4.1.0          |                                                          |
| containers.podman           | 1.18.1         | 1.19.0         |                                                          |
| hitachivantara.vspone_block | 4.5.1          | 4.6.1          |                                                          |
| kubernetes.core             | 6.2.0          | 6.3.0          |                                                          |
| pcg.alpaca_operator         | 2.1.1          | 2.2.0          | The collection did not have a changelog in this version. |
| purestorage.flasharray      | 1.41.0         | 1.42.0         |                                                          |
| vmware.vmware_rest          | 4.9.0          | 4.10.0         |                                                          |

<a id="major-changes-2"></a>
### Major Changes

<a id="containers-podman-2"></a>
#### containers\.podman

* Add podman Quadlet modules

<a id="minor-changes-2"></a>
### Minor Changes

<a id="ansible-core-7"></a>
#### Ansible\-core

* ansible\-test \- Update URL used to download FreeBSD wheels for managed remotes\.
* ansible\-test \- Use the new API endpoint for the Ansible Core CI service\.

<a id="ansible-netcommon-3"></a>
#### ansible\.netcommon

* Option to use libssh as transport while using netconf\, is added\.
* The ssh\-python module is needed\, which will ensure libssh as transport for netconf operations\. When use\_libssh is enabled\.

<a id="cisco-dnac"></a>
#### cisco\.dnac

* Added \'802\_11\_be\_profiles\'  attribute in wireless\_design\_workflow\_manager module
* Added build\_ignore configuration to optimize Ansible Galaxy collection packaging\.
* Changes in accesspoint\_workflow\_manager module
* Changes in device\_configs\_backup\_workflow\_manager module
* Changes in inventory\_workflow\_manager module
* Changes in lan\_automation\_workflow\_manager module
* Changes in network\_profile\_wireless\_workflow\_manager module
* Changes in pnp\_workflow\_manager module
* Changes in provision\_workflow\_manager module
* Changes in sda\_fabric\_devices\_workflow\_manager module
* Changes in sda\_host\_port\_onboarding\_workflow\_manager module
* Changes in swim\_workflow\_manager module
* Changes in template\_workflow\_manager module
* Changes in wireless\_design\_workflow\_manager module
* Code formatting and ansible\-lint compliance updates for Red Hat standards
* Standardized README format and content to match Catalyst Center Ansible collection documentation practices\.
* access\_groups \- new module to manage access groups
* access\_groups\_count\_info \- new module to retrieve access groups count
* access\_groups\_info \- new module to retrieve access groups information
* cisco\.dnac collection \- New service system\_software\_upgrade added for Catalyst Center 3\.1\.6\.0
* cisco\.dnac collection \- SDK updated to dnacentersdk 2\.11\.0 with support for Cisco Catalyst Center 3\.1\.6\.0
* client\_enrichment\_details\_v2\_info \- new module to retrieve client enrichment details \(v2\)
* compliance\_network\_devices\_detail\_policys\_info \- new module to retrieve compliance policies for network devices
* compliance\_network\_devices\_detail\_policys\_violations\_info \- new module to retrieve compliance policy violations for network devices
* compliance\_policys \- new module to manage compliance policies
* compliance\_policys\_count\_info \- new module to retrieve compliance policies count
* compliance\_policys\_info \- new module to retrieve compliance policies information
* compliance\_policys\_rules \- new module to manage compliance policy rules
* compliance\_policys\_rules\_conditions \- new module to manage compliance policy rule conditions
* compliance\_policys\_rules\_conditions\_count\_info \- new module to retrieve compliance policy rule conditions count
* compliance\_policys\_rules\_conditions\_info \- new module to retrieve compliance policy rule conditions information
* compliance\_policys\_rules\_count\_info \- new module to retrieve compliance policy rules count
* compliance\_policys\_rules\_info \- new module to retrieve compliance policy rules information
* compliance\_policys\_rules\_variables \- new module to manage compliance policy rule variables
* compliance\_policys\_rules\_variables\_count\_info \- new module to retrieve compliance policy rule variables count
* compliance\_policys\_rules\_variables\_info \- new module to retrieve compliance policy rule variables information
* compliance\_policys\_site\_assignments \- new module to manage compliance policy site assignments
* compliance\_policys\_site\_assignments\_info \- new module to retrieve compliance policy site assignments information
* compliance\_policys\_sites\_rules\_variables \- new module to manage compliance policy site rule variables
* compliance\_policys\_sites\_rules\_variables\_info \- new module to retrieve compliance policy site rule variables information
* device\_enrichment\_details\_v2\_info \- new module to retrieve device enrichment details \(v2\)
* discoverys \- new module to manage device discoveries
* discoverys\_count\_info \- new module to retrieve device discoveries count
* discoverys\_info \- new module to retrieve device discoveries information
* discoverys\_jobs \- new module to manage discovery jobs
* discoverys\_jobs\_count\_info \- new module to retrieve discovery jobs count
* discoverys\_jobs\_discovered\_network\_devices\_count\_info \- new module to retrieve discovered network devices count
* discoverys\_jobs\_discovered\_network\_devices\_info \- new module to retrieve discovered network devices from discovery jobs
* discoverys\_jobs\_info \- new module to retrieve discovery jobs information
* discoverys\_jobs\_stop\_create \- new module to stop discovery jobs
* discoverys\_jobs\_summarys\_info \- new module to retrieve discovery jobs summaries
* download\_software\_release\_create \- new module to download software releases
* download\_software\_release\_delete \- new module to delete software release downloads
* download\_software\_release\_update \- new module to update software release downloads
* filter\_group\_aassociations\_delete \- new module to delete filter group associations
* filter\_group\_associations \- new module to manage filter group associations
* filter\_group\_associations\_info \- new module to retrieve filter group associations information
* filter\_groups \- new module to manage filter groups
* filter\_groups\_info \- new module to retrieve filter groups information
* global\_credentials \- new module to manage global credentials
* global\_credentials\_count\_info \- new module to retrieve global credentials count
* global\_credentials\_info \- new module to retrieve global credentials information
* images\_delete \- new module to delete software images
* install\_optional\_packages\_create \- new module to install optional packages
* installed\_release\_info \- new module to retrieve installed release information
* iot\_fabric\_rep\_rings\_delete \- new module to delete IoT fabric REP rings
* iot\_non\_fabric\_rep\_rings\_delete \- new module to delete IoT non\-fabric REP rings
* issue\_enrichment\_details\_info \- new module to retrieve issue enrichment details
* network\_devices\_create \- new module to create network devices
* network\_devices\_export\_credentials\_create \- new module to export network device credentials
* network\_devices\_update \- new module to update network devices
* network\_devices\_update\_create \- new module to trigger network device updates
* network\_devices\_validate\_device\_create \- new module to validate network devices
* product\_series\_count\_info \- new module to retrieve product series count
* releases\_info \- new module to retrieve available releases information
* releases\_release\_summary\_info \- new module to retrieve release summary
* roles\_permissions\_info \- new module to retrieve roles permissions
* roles\_v2 \- new module to manage roles \(v2\)
* roles\_v2\_info \- new module to retrieve roles information \(v2\)
* sda\_layer3\_virtual\_networks\_delete \- new module to delete SDA layer 3 virtual networks
* sda\_transit\_networks\_delete \- new module to delete SDA transit networks
* site\_delete \- new module to delete sites
* site\_update \- new module to update sites
* software\_management\_executions\_info \- new module to retrieve software management execution details
* uninstall\_optional\_packages\_create \- new module to uninstall optional packages
* upgrade\_software\_release\_create \- new module to upgrade software releases
* user\_enrichment\_details\_v2\_info \- new module to retrieve user enrichment details \(v2\)
* wireless\_controllers\_certificate\_renewal\_create \- new module to trigger wireless controller certificate renewal
* wireless\_controllers\_site\_tags\_info \- new module to retrieve wireless controller site tags
* wireless\_profiles\_policy\_tags\_info \- new module to retrieve wireless profile policy tags
* wireless\_settings\_certificate\_renewal\_profiles \- new module to manage wireless certificate renewal profiles
* wireless\_settings\_certificate\_renewal\_profiles\_count\_info \- new module to retrieve wireless certificate renewal profiles count
* wireless\_settings\_certificate\_renewal\_profiles\_info \- new module to retrieve wireless certificate renewal profiles information

<a id="cisco-ios"></a>
#### cisco\.ios

* Adds a new Resource Module <em class="title-reference">ios\_bfd\_interfaces</em> to configure BFD on interfaces\.
* Adds a new Resource Module <em class="title-reference">ios\_bfd\_templates</em> to configure BFD  using templates\.
* ios\_l3\_interfaces \- Add support for \'redirects\' and \'unreachables\' attributes to configure ICMP redirect and unreachable messages\.

<a id="community-aws"></a>
#### community\.aws

* cloudfront\_distribution \- Added <code>elements</code> key to <code>active\_trusted\_signers</code> \([https\://github\.com/ansible\-collections/community\.aws/pull/2354](https\://github\.com/ansible\-collections/community\.aws/pull/2354)\)\.
* cloudfront\_distribution \- Added <code>elements</code> key to <code>aliases</code> \([https\://github\.com/ansible\-collections/community\.aws/pull/2354](https\://github\.com/ansible\-collections/community\.aws/pull/2354)\)\.
* cloudfront\_distribution \- Added <code>elements</code> key to <code>cache\_behaviors\.items\.allowed\_methods\.cached\_methods</code> \([https\://github\.com/ansible\-collections/community\.aws/pull/2354](https\://github\.com/ansible\-collections/community\.aws/pull/2354)\)\.
* cloudfront\_distribution \- Added <code>elements</code> key to <code>cache\_behaviors\.items\.allowed\_methods</code> \([https\://github\.com/ansible\-collections/community\.aws/pull/2354](https\://github\.com/ansible\-collections/community\.aws/pull/2354)\)\.
* cloudfront\_distribution \- Added <code>elements</code> key to <code>cache\_behaviors\.items\.forwarded\_values\.cookies\.whitelisted\_names</code> \([https\://github\.com/ansible\-collections/community\.aws/pull/2354](https\://github\.com/ansible\-collections/community\.aws/pull/2354)\)\.
* cloudfront\_distribution \- Added <code>elements</code> key to <code>cache\_behaviors\.items\.forwarded\_values\.headers</code> \([https\://github\.com/ansible\-collections/community\.aws/pull/2354](https\://github\.com/ansible\-collections/community\.aws/pull/2354)\)\.
* cloudfront\_distribution \- Added <code>elements</code> key to <code>cache\_behaviors\.items\.forwarded\_values\.query\_string\_cache\_keys</code> \([https\://github\.com/ansible\-collections/community\.aws/pull/2354](https\://github\.com/ansible\-collections/community\.aws/pull/2354)\)\.
* cloudfront\_distribution \- Added <code>elements</code> key to <code>cache\_behaviors\.items\.lambda\_function\_associations</code> \([https\://github\.com/ansible\-collections/community\.aws/pull/2354](https\://github\.com/ansible\-collections/community\.aws/pull/2354)\)\.
* cloudfront\_distribution \- Added <code>elements</code> key to <code>cache\_behaviors</code> \([https\://github\.com/ansible\-collections/community\.aws/pull/2354](https\://github\.com/ansible\-collections/community\.aws/pull/2354)\)\.
* cloudfront\_distribution \- Added <code>elements</code> key to <code>custom\_error\_responses</code> \([https\://github\.com/ansible\-collections/community\.aws/pull/2354](https\://github\.com/ansible\-collections/community\.aws/pull/2354)\)\.
* cloudfront\_distribution \- Added <code>elements</code> key to <code>default\_cache\_behavior\.allowed\_methods\.cached\_methods</code> \([https\://github\.com/ansible\-collections/community\.aws/pull/2354](https\://github\.com/ansible\-collections/community\.aws/pull/2354)\)\.
* cloudfront\_distribution \- Added <code>elements</code> key to <code>default\_cache\_behavior\.allowed\_methods</code> \([https\://github\.com/ansible\-collections/community\.aws/pull/2354](https\://github\.com/ansible\-collections/community\.aws/pull/2354)\)\.
* cloudfront\_distribution \- Added <code>elements</code> key to <code>default\_cache\_behavior\.forwarded\_values\.cookies\.whitelisted\_names</code> \([https\://github\.com/ansible\-collections/community\.aws/pull/2354](https\://github\.com/ansible\-collections/community\.aws/pull/2354)\)\.
* cloudfront\_distribution \- Added <code>elements</code> key to <code>default\_cache\_behavior\.forwarded\_values\.headers</code> \([https\://github\.com/ansible\-collections/community\.aws/pull/2354](https\://github\.com/ansible\-collections/community\.aws/pull/2354)\)\.
* cloudfront\_distribution \- Added <code>elements</code> key to <code>default\_cache\_behavior\.forwarded\_values\.query\_string\_cache\_keys</code> \([https\://github\.com/ansible\-collections/community\.aws/pull/2354](https\://github\.com/ansible\-collections/community\.aws/pull/2354)\)\.
* cloudfront\_distribution \- Added <code>elements</code> key to <code>default\_cache\_behavior\.lambda\_function\_associations</code> \([https\://github\.com/ansible\-collections/community\.aws/pull/2354](https\://github\.com/ansible\-collections/community\.aws/pull/2354)\)\.
* cloudfront\_distribution \- Added <code>elements</code> key to <code>origins\.items\.custom\_origin\_config\.origin\_ssl\_protocols</code> \([https\://github\.com/ansible\-collections/community\.aws/pull/2354](https\://github\.com/ansible\-collections/community\.aws/pull/2354)\)\.
* cloudfront\_distribution \- Added <code>elements</code> key to <code>origins</code> \([https\://github\.com/ansible\-collections/community\.aws/pull/2354](https\://github\.com/ansible\-collections/community\.aws/pull/2354)\)\.
* cloudfront\_distribution \- Added <code>elements</code> key to <code>restrictions\.geo\_restriction</code> \([https\://github\.com/ansible\-collections/community\.aws/pull/2354](https\://github\.com/ansible\-collections/community\.aws/pull/2354)\)\.
* cloudfront\_distribution \- move misplaced options out of <code>forwarded\_values</code> <code>suboptions</code>\. \([https\://github\.com/ansible\-collections/community\.aws/pull/2342](https\://github\.com/ansible\-collections/community\.aws/pull/2342)\)\.
* cloudfront\_invalidation \- Added <code>elements</code> key to <code>invalidation\.invalidation\_batch\.paths</code> \([https\://github\.com/ansible\-collections/community\.aws/pull/2354](https\://github\.com/ansible\-collections/community\.aws/pull/2354)\)\.

<a id="community-general-7"></a>
#### community\.general

* ModuleHelper module utils \- allow to ignore specific exceptions in <code>module\_fails\_on\_exception</code> decorator \([https\://github\.com/ansible\-collections/community\.general/pull/11488](https\://github\.com/ansible\-collections/community\.general/pull/11488)\)\.
* from\_ini filter plugin \- add <code>delimiters</code> parameter to allow correctly parsing more INI documents \([https\://github\.com/ansible\-collections/community\.general/issues/11506](https\://github\.com/ansible\-collections/community\.general/issues/11506)\, [https\://github\.com/ansible\-collections/community\.general/pull/11512](https\://github\.com/ansible\-collections/community\.general/pull/11512)\)\.
* keycloak\_client \- add <code>valid\_post\_logout\_redirect\_uris</code> option to configure post logout redirect URIs for a client\, and <code>backchannel\_logout\_url</code> option to configure the backchannel logout URL for a client \([https\://github\.com/ansible\-collections/community\.general/issues/6812](https\://github\.com/ansible\-collections/community\.general/issues/6812)\, [https\://github\.com/ansible\-collections/community\.general/issues/4892](https\://github\.com/ansible\-collections/community\.general/issues/4892)\, [https\://github\.com/ansible\-collections/community\.general/pull/11473](https\://github\.com/ansible\-collections/community\.general/pull/11473)\)\.
* keycloak\_client\_rolemapping\, keycloak\_realm\_rolemapping\, keycloak\_group \- optimize retrieval of groups by name to use Keycloak search API with exact matching instead of fetching all groups \([https\://github\.com/ansible\-collections/community\.general/pull/11503](https\://github\.com/ansible\-collections/community\.general/pull/11503)\)\.
* keycloak\_realm \- add support for <code>localizationTexts</code> option in Keycloak realms \([https\://github\.com/ansible\-collections/community\.general/pull/11513](https\://github\.com/ansible\-collections/community\.general/pull/11513)\)\.
* keycloak\_realm\_key \- add support for auto\-generated key providers \(<code>rsa\-generated</code>\, <code>rsa\-enc\-generated</code>\, <code>hmac\-generated</code>\, <code>aes\-generated</code>\, <code>ecdsa\-generated</code>\, <code>ecdh\-generated</code>\, <code>eddsa\-generated</code>\)\, <code>java\-keystore</code> provider\, additional algorithms \(HMAC\, ECDSA\, ECDH\, EdDSA\, AES\)\, and new config options \(<code>secret\_size</code>\, <code>key\_size</code>\, <code>elliptic\_curve</code>\, <code>keystore</code>\, <code>keystore\_password</code>\, <code>key\_alias</code>\, <code>key\_password</code>\)\. Also makes <code>config\.private\_key</code> and <code>config\.certificate</code> optional as they are only required for imported key providers \([https\://github\.com/ansible\-collections/community\.general/pull/11468](https\://github\.com/ansible\-collections/community\.general/pull/11468)\)\.
* redfish\_info \- add Redfish Root data to results of successful <code>CheckAvailability</code> command \([https\://github\.com/ansible\-collections/community\.general/pull/11504](https\://github\.com/ansible\-collections/community\.general/pull/11504)\)\.
* seport \- adds support for DCCP and SCTP protocols \([https\://github\.com/ansible\-collections/community\.general/pull/11486](https\://github\.com/ansible\-collections/community\.general/pull/11486)\)\.

<a id="community-libvirt-2"></a>
#### community\.libvirt

* virt\_install \- added support for memoryBacking source type configuration\, including memfd for shared memory \([https\://github\.com/ansible\-collections/community\.libvirt/issues/228](https\://github\.com/ansible\-collections/community\.libvirt/issues/228)\)\.
* virt\_install \- added support for primary value attribute \(\_value or value\) in dynamic dict options that require a primary value alongside additional attributes\.
* virt\_install \- enhanced cloud\_init configuration handling for sub\-options \(meta\-data\, user\-data\, and network\-config\) to support both string and dictionary inputs\.
* virt\_install \- refactored common virt\-install functionality into module\_utils and doc\_fragments to enable code reuse between modules\.
* virt\_volume \- New return key/value pairs \'Type\'\, \'Capacity\' and \'Allocation\' were added to command \'list\_volumes\' \([https\://github\.com/ansible\-collections/community\.libvirt/issues/187](https\://github\.com/ansible\-collections/community\.libvirt/issues/187)\)
* virt\_volume \- added ability to resize volumes if defined capacity is different\. If volume already exists and defined capacity in XML differs a resize is attempted\.

<a id="community-mysql-3"></a>
#### community\.mysql

* mysql\_role \- add <code>sql\_log\_bin</code> option to disable binary logging for the connection \([https\://github\.com/ansible\-collections/community\.mysql/issues/742](https\://github\.com/ansible\-collections/community\.mysql/issues/742)\)\.

<a id="containers-podman-3"></a>
#### containers\.podman

* Fix tests for new Podman

<a id="hitachivantara-vspone-block"></a>
#### hitachivantara\.vspone\_block

* Added \"playbooks/vsp\_direct/vsp\_storage\_connection\_session\_example\.yml\" as a sample playbook demonstrating session\-based storage operations\.
* Added a new \"hv\_pav\_alias\" module to manage PAV \(Parallel Access Volume\) alias assignments for Mainframe based VSP block storage systems\.
* Added a new \"hv\_pav\_alias\_facts\" module to gather facts about PAV aliases from Mainframe based VSP block storage systems\.
* Added a new \"hv\_sds\_block\_audit\_log\_setting\" module to support configuration of audit log settings on VSP One SDS Block and Cloud systems\.
* Added a new \"hv\_sds\_block\_audit\_log\_setting\_facts\" module to retrieve audit log setting from VSP One SDS Block and Cloud systems\.
* Added a new \"hv\_sds\_block\_dump\_log\_file\" module to retrieve and dump log information from VSP One SDS Block and Cloud systems\.
* Added a new \"hv\_sds\_block\_dump\_log\_status\_facts\" module to retrieve and dump log status information from VSP One SDS Block and Cloud systems\.
* Added a new \"hv\_sds\_block\_event\_log\_setting\_facts\" module to retrieve event log setting from VSP One SDS Block and Cloud systems\.
* Added a new \"hv\_sds\_block\_event\_logs\_facts\" module to retrieve event logs with various filtering options from VSP One SDS Block and Cloud systems\.
* Added a new \"hv\_sds\_block\_journal\" module to create and update journals on VSP One SDS Block and Cloud systems\.
* Added a new \"hv\_sds\_block\_journal\_facts\" module to retrieve journal details from VSP One SDS Block and Cloud systems\.
* Added a new \"hv\_sds\_block\_license\" module to manage license on VSP One SDS Block and Cloud systems\.
* Added a new \"hv\_sds\_block\_license\_facts\" module to retrieve license from VSP One SDS Block and Cloud systems\.
* Added a new \"hv\_sds\_block\_license\_setting\" module to modify license warning threshold settings for VSP One SDS Block and Cloud systems\.
* Added a new \"hv\_sds\_block\_license\_setting\_facts\" module to retrieve license setting from VSP One SDS Block and Cloud systems\.
* Added a new \"hv\_sds\_block\_login\_message\" module to update the message configured to be displayed on the GUI login window and CLI warning banner of the VSP One SDS Block and Cloud systems\.
* Added a new \"hv\_sds\_block\_login\_message\_facts\" module to retrieve the message configured to be displayed on the GUI login window and CLI warning banner of the VSP One SDS Block and Cloud systems\.
* Added a new \"hv\_sds\_block\_storage\_external\_auth\_server\_setting\" module to configure external authentication server settings on VSP One SDS Block and Cloud systems\.
* Added a new \"hv\_sds\_block\_storage\_external\_auth\_server\_setting\_facts\" module to retrieve external authentication server settings from the VSP One SDS Block and Cloud systems\.
* Added a new \"hv\_sds\_block\_storage\_user\_auth\_setting\" module to configure external authentication server settings on VSP One SDS Block and Cloud systems\.
* Added a new \"hv\_sds\_block\_storage\_user\_auth\_setting\_facts\" module to retrieve user authentication settings from VSP One SDS Block and Cloud systems\.
* Added a new \"hv\_session\" module to generate and discard session on VSP block storage systems\.
* Added a new \"hv\_session\_facts\" module to retrieve information about sessions on VSP block storage systems\.
* Added a new \"hv\_snapshot\_family\_facts\" module to retrieve information about snapshot family of the provided LDEV ID from VSP block storage systems\.
* Added a new \"hv\_supported\_host\_mode\_facts\" module to retrieve detailed information about supported host mode options available in a given VSP block storage system\.
* Added a new \"hv\_vclone\_parent\_volume\_facts\" module to retrieve information about virtual clone parent volume from VSP block storage systems\.
* Added notes to module documentation indicating that a few modules are not supported for BHE and higher models\.
* Added support for Mainframe z16\.
* Added support for SVOS 10\.5\.1\.
* Added support to \"hv\_ddp\_pool\" module for DDP pool creation with RAID6\.
* Added support to \"hv\_hg\" module for present/unpresent multiple LDEVs to/from hostgroups across multiple ports\.
* Added support to \"hv\_hg\" module to support host group\'s lun paths\.
* Added support to \"hv\_ldev\" module to create DRS LDEV without deduplication and compression\.
* Added support to \"hv\_ldev\" module to create ESE Mainframe LDEV with cylinder and emulation type\.
* Added support to \"hv\_ldev\" module to create Mainframe LDEV with cylinder and emulation type in a parity group\.
* Added support to \"hv\_ldev\" module to create Mainframe LDEV with cylinder and emulation type\.
* Added support to \"hv\_ldev\" module to create TSE Mainframe LDEV with cylinder and emulation type\.
* Added support to \"hv\_ldev\" module to stop the normal format for all volumes\.
* Added support to \"hv\_ldev\_facts\" module output to include Mainframe\, vClone and other new properties\.
* Added support to \"hv\_ldev\_facts\" module to get information about multiple LDEVs by their IDs\.
* Added support to \"hv\_paritygroup\_facts\" module output to include Mainframe and other new properties\.
* Added support to \"hv\_resource\_group\_facts\" module to get basic information about all resource groups including meta resource group information\.
* Added support to \"hv\_sds\_block\_cluster\" module to stop the storage cluster\.
* Added support to \"hv\_snapshot\" module to create or convert a snapshot pair to vClone depending on the snapshot pair status\.
* Added support to \"hv\_snapshot\" module to optionally delete secondary volume using should\_delete\_svol parameter\.
* Added support to \"hv\_snapshot\" module to restore a snapshot pair from vClone\.
* Added support to \"hv\_snapshot\_facts\" module output to include vClone\-related properties\.
* Added support to \"hv\_snapshot\_group\" module to create or convert a snapshot pair to vClone by snapshot group name\.
* Added support to \"hv\_snapshot\_group\" module to restore snapshot group from vClone\.
* Added support to \"hv\_snapshot\_group\" module to restore the snapshot pairs using group name and wait for the final state of all snapshots\.
* Added support to \"hv\_snapshot\_group\_facts\" module output to include vClone\-related properties\.
* Added support to \"hv\_storage\_port\_facts\" module output to include Mainframe and other new properties\.
* Added support to \"hv\_storagepool\" module output to include pool volumes information\.
* Added support to \"hv\_storagepool\" module to create a mainframe HDP storage pool using parity group and cylinder\.
* Added support to \"hv\_storagepool\" module to shrink a storage pool using list of pool volume IDs and delete pool volumes\.
* Added support to \"hv\_storagepool\" module to shrink a storage pool using list of pool volume IDs\.
* Added support to \"hv\_storagepool\" module to shrink a storage pool using start and end pool volume IDs\.
* Added support to \"hv\_storagepool\" module to stop the shrink operation of a storage pool\.
* Added support to \"hv\_storagepool\_facts\" module output to include pool volumes information\.
* Added support to \"hv\_storagepool\_facts\" module to get all mainframe storage pools with cache info for VSP 5XXX series storage\.
* Added support to \"hv\_storagepool\_facts\" module to get all mainframe storage pools with extended info\.
* Added support to \"hv\_storagepool\_facts\" module to get all mainframe storage pools\.
* Added support to \"hv\_storagesystem\_facts\" module output to include \"is\_compression\_acceleration\_available\" status\.
* Added support to \"hv\_vsp\_one\_volume\" module to create DRS volume without deduplication and compression\.
* Added support to \"hv\_vsp\_one\_volume\_facts\" module output to include Mainframe\, vClone and other new properties\.
* Enhanced the performance of the \"hv\_gad\_facts\" module\'s task by implementing thread pool and batch processing\.
* Enhanced the performance of the \"hv\_hg\_facts\" module\'s task by implementing parallel calls\.
* Enhanced the performance of the \"hv\_ldev\_facts\" module\'s task by implementing thread pool and batch processing\.
* Other minor bug fixes\.

<a id="kubernetes-core"></a>
#### kubernetes\.core

* Remove deprecated import from <code>ansible\.module\_utils\.\_text</code> \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/1053](https\://github\.com/ansible\-collections/kubernetes\.core/pull/1053)\)\.
* helm \- add <code>release\_values</code> key to <code>status</code> return value that can be accessed using Jinja2 dot notation \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/1056](https\://github\.com/ansible\-collections/kubernetes\.core/pull/1056)\)\.
* helm\_info \- add <code>release\_values</code> key to <code>status</code> return value that can be accessed using Jinja2 dot notation \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/1056](https\://github\.com/ansible\-collections/kubernetes\.core/pull/1056)\)\.

<a id="vmware-vmware-rest"></a>
#### vmware\.vmware\_rest

* Disable check mode for all non\-info modules in this collection\. Check mode was never supported for these modules\. Fixes [https\://github\.com/ansible\-collections/vmware\.vmware\_rest/issues/363](https\://github\.com/ansible\-collections/vmware\.vmware\_rest/issues/363)

<a id="deprecated-features-2"></a>
### Deprecated Features

* The awx\.awx collection will be removed from Ansible 14\.
  The collection is undergoing a heavy [refactoring](https\://forum\.ansible\.com/t/7404) and currently does not align with the standards for the community package\.
  See [the removal discussion for details](https\://forum\.ansible\.com/t/44706)\.
  After removal\, users can still install this collection with <code>ansible\-galaxy collection install awx\.awx</code>\.

<a id="community-aws-1"></a>
#### community\.aws

* The alias <code>aws\_acm\_info</code> for the <code>acm\_certificate\_info</code> module has been deprecated\. Please use <code>community\.aws\.acm\_certificate\_info</code> instead \([https\://github\.com/ansible\-collections/community\.aws/pull/2387](https\://github\.com/ansible\-collections/community\.aws/pull/2387)\)\.
* The alias <code>aws\_acm</code> for the <code>acm\_certificate</code> module has been deprecated\. Please use <code>community\.aws\.acm\_certificate</code> instead \([https\://github\.com/ansible\-collections/community\.aws/pull/2387](https\://github\.com/ansible\-collections/community\.aws/pull/2387)\)\.
* The alias <code>aws\_api\_gateway\_domain</code> for the <code>api\_gateway\_domain</code> module has been deprecated\. Please use <code>community\.aws\.api\_gateway\_domain</code> instead \([https\://github\.com/ansible\-collections/community\.aws/pull/2387](https\://github\.com/ansible\-collections/community\.aws/pull/2387)\)\.
* The alias <code>aws\_api\_gateway</code> for the <code>api\_gateway</code> module has been deprecated\. Please use <code>community\.aws\.api\_gateway</code> instead \([https\://github\.com/ansible\-collections/community\.aws/pull/2387](https\://github\.com/ansible\-collections/community\.aws/pull/2387)\)\.
* The alias <code>aws\_application\_scaling\_policy</code> for the <code>application\_autoscaling\_policy</code> module has been deprecated\. Please use <code>community\.aws\.application\_autoscaling\_policy</code> instead \([https\://github\.com/ansible\-collections/community\.aws/pull/2387](https\://github\.com/ansible\-collections/community\.aws/pull/2387)\)\.
* The alias <code>aws\_batch\_compute\_environment</code> for the <code>batch\_compute\_environment</code> module has been deprecated\. Please use <code>community\.aws\.batch\_compute\_environment</code> instead \([https\://github\.com/ansible\-collections/community\.aws/pull/2387](https\://github\.com/ansible\-collections/community\.aws/pull/2387)\)\.
* The alias <code>aws\_batch\_job\_definition</code> for the <code>batch\_job\_definition</code> module has been deprecated\. Please use <code>community\.aws\.batch\_job\_definition</code> instead \([https\://github\.com/ansible\-collections/community\.aws/pull/2387](https\://github\.com/ansible\-collections/community\.aws/pull/2387)\)\.
* The alias <code>aws\_batch\_job\_queue</code> for the <code>batch\_job\_queue</code> module has been deprecated\. Please use <code>community\.aws\.batch\_job\_queue</code> instead \([https\://github\.com/ansible\-collections/community\.aws/pull/2387](https\://github\.com/ansible\-collections/community\.aws/pull/2387)\)\.
* The alias <code>aws\_codebuild</code> for the <code>codebuild\_project</code> module has been deprecated\. Please use <code>community\.aws\.codebuild\_project</code> instead \([https\://github\.com/ansible\-collections/community\.aws/pull/2387](https\://github\.com/ansible\-collections/community\.aws/pull/2387)\)\.
* The alias <code>aws\_codecommit</code> for the <code>codecommit\_repository</code> module has been deprecated\. Please use <code>community\.aws\.codecommit\_repository</code> instead \([https\://github\.com/ansible\-collections/community\.aws/pull/2387](https\://github\.com/ansible\-collections/community\.aws/pull/2387)\)\.
* The alias <code>aws\_codepipeline</code> for the <code>codepipeline</code> module has been deprecated\. Please use <code>community\.aws\.codepipeline</code> instead \([https\://github\.com/ansible\-collections/community\.aws/pull/2387](https\://github\.com/ansible\-collections/community\.aws/pull/2387)\)\.
* The alias <code>aws\_config\_aggregation\_authorization</code> for the <code>config\_aggregation\_authorization</code> module has been deprecated\. Please use <code>community\.aws\.config\_aggregation\_authorization</code> instead \([https\://github\.com/ansible\-collections/community\.aws/pull/2387](https\://github\.com/ansible\-collections/community\.aws/pull/2387)\)\.
* The alias <code>aws\_config\_aggregator</code> for the <code>config\_aggregator</code> module has been deprecated\. Please use <code>community\.aws\.config\_aggregator</code> instead \([https\://github\.com/ansible\-collections/community\.aws/pull/2387](https\://github\.com/ansible\-collections/community\.aws/pull/2387)\)\.
* The alias <code>aws\_config\_delivery\_channel</code> for the <code>config\_delivery\_channel</code> module has been deprecated\. Please use <code>community\.aws\.config\_delivery\_channel</code> instead \([https\://github\.com/ansible\-collections/community\.aws/pull/2387](https\://github\.com/ansible\-collections/community\.aws/pull/2387)\)\.
* The alias <code>aws\_config\_recorder</code> for the <code>config\_recorder</code> module has been deprecated\. Please use <code>community\.aws\.config\_recorder</code> instead \([https\://github\.com/ansible\-collections/community\.aws/pull/2387](https\://github\.com/ansible\-collections/community\.aws/pull/2387)\)\.
* The alias <code>aws\_config\_rule</code> for the <code>config\_rule</code> module has been deprecated\. Please use <code>community\.aws\.config\_rule</code> instead \([https\://github\.com/ansible\-collections/community\.aws/pull/2387](https\://github\.com/ansible\-collections/community\.aws/pull/2387)\)\.
* The alias <code>aws\_direct\_connect\_confirm\_connection</code> for the <code>directconnect\_confirm\_connection</code> module has been deprecated\. Please use <code>community\.aws\.directconnect\_confirm\_connection</code> instead \([https\://github\.com/ansible\-collections/community\.aws/pull/2387](https\://github\.com/ansible\-collections/community\.aws/pull/2387)\)\.
* The alias <code>aws\_direct\_connect\_connection</code> for the <code>directconnect\_connection</code> module has been deprecated\. Please use <code>community\.aws\.directconnect\_connection</code> instead \([https\://github\.com/ansible\-collections/community\.aws/pull/2387](https\://github\.com/ansible\-collections/community\.aws/pull/2387)\)\.
* The alias <code>aws\_direct\_connect\_gateway</code> for the <code>directconnect\_gateway</code> module has been deprecated\. Please use <code>community\.aws\.directconnect\_gateway</code> instead \([https\://github\.com/ansible\-collections/community\.aws/pull/2387](https\://github\.com/ansible\-collections/community\.aws/pull/2387)\)\.
* The alias <code>aws\_direct\_connect\_link\_aggregation\_group</code> for the <code>directconnect\_link\_aggregation\_group</code> module has been deprecated\. Please use <code>community\.aws\.directconnect\_link\_aggregation\_group</code> instead \([https\://github\.com/ansible\-collections/community\.aws/pull/2387](https\://github\.com/ansible\-collections/community\.aws/pull/2387)\)\.
* The alias <code>aws\_direct\_connect\_virtual\_interface</code> for the <code>directconnect\_virtual\_interface</code> module has been deprecated\. Please use <code>community\.aws\.directconnect\_virtual\_interface</code> instead \([https\://github\.com/ansible\-collections/community\.aws/pull/2387](https\://github\.com/ansible\-collections/community\.aws/pull/2387)\)\.
* The alias <code>aws\_eks\_cluster</code> for the <code>eks\_cluster</code> module has been deprecated\. Please use <code>community\.aws\.eks\_cluster</code> instead \([https\://github\.com/ansible\-collections/community\.aws/pull/2387](https\://github\.com/ansible\-collections/community\.aws/pull/2387)\)\.
* The alias <code>aws\_elasticbeanstalk\_app</code> for the <code>elasticbeanstalk\_app</code> module has been deprecated\. Please use <code>community\.aws\.elasticbeanstalk\_app</code> instead \([https\://github\.com/ansible\-collections/community\.aws/pull/2387](https\://github\.com/ansible\-collections/community\.aws/pull/2387)\)\.
* The alias <code>aws\_glue\_connection</code> for the <code>glue\_connection</code> module has been deprecated\. Please use <code>community\.aws\.glue\_connection</code> instead \([https\://github\.com/ansible\-collections/community\.aws/pull/2387](https\://github\.com/ansible\-collections/community\.aws/pull/2387)\)\.
* The alias <code>aws\_glue\_crawler</code> for the <code>glue\_crawler</code> module has been deprecated\. Please use <code>community\.aws\.glue\_crawler</code> instead \([https\://github\.com/ansible\-collections/community\.aws/pull/2387](https\://github\.com/ansible\-collections/community\.aws/pull/2387)\)\.
* The alias <code>aws\_glue\_job</code> for the <code>glue\_job</code> module has been deprecated\. Please use <code>community\.aws\.glue\_job</code> instead \([https\://github\.com/ansible\-collections/community\.aws/pull/2387](https\://github\.com/ansible\-collections/community\.aws/pull/2387)\)\.
* The alias <code>aws\_inspector\_target</code> for the <code>inspector\_target</code> module has been deprecated\. Please use <code>community\.aws\.inspector\_target</code> instead \([https\://github\.com/ansible\-collections/community\.aws/pull/2387](https\://github\.com/ansible\-collections/community\.aws/pull/2387)\)\.
* The alias <code>aws\_kms\_info</code> for the <code>kms\_key\_info</code> module has been deprecated\. Please use <code>amazon\.aws\.kms\_key\_info</code> instead \([https\://github\.com/ansible\-collections/community\.aws/pull/2387](https\://github\.com/ansible\-collections/community\.aws/pull/2387)\)\.
* The alias <code>aws\_kms</code> for the <code>kms\_key</code> module has been deprecated\. Please use <code>amazon\.aws\.kms\_key</code> instead \([https\://github\.com/ansible\-collections/community\.aws/pull/2387](https\://github\.com/ansible\-collections/community\.aws/pull/2387)\)\.
* The alias <code>aws\_msk\_cluster</code> for the <code>msk\_cluster</code> module has been deprecated\. Please use <code>community\.aws\.msk\_cluster</code> instead \([https\://github\.com/ansible\-collections/community\.aws/pull/2387](https\://github\.com/ansible\-collections/community\.aws/pull/2387)\)\.
* The alias <code>aws\_msk\_config</code> for the <code>msk\_config</code> module has been deprecated\. Please use <code>community\.aws\.msk\_config</code> instead \([https\://github\.com/ansible\-collections/community\.aws/pull/2387](https\://github\.com/ansible\-collections/community\.aws/pull/2387)\)\.
* The alias <code>aws\_s3\_bucket\_info</code> for the <code>s3\_bucket\_info</code> module has been deprecated\. Please use <code>amazon\.aws\.s3\_bucket\_info</code> instead \([https\://github\.com/ansible\-collections/community\.aws/pull/2387](https\://github\.com/ansible\-collections/community\.aws/pull/2387)\)\.
* The alias <code>aws\_s3\_cors</code> for the <code>s3\_cors</code> module has been deprecated\. Please use <code>community\.aws\.s3\_cors</code> instead \([https\://github\.com/ansible\-collections/community\.aws/pull/2387](https\://github\.com/ansible\-collections/community\.aws/pull/2387)\)\.
* The alias <code>aws\_secret</code> for the <code>secretsmanager\_secret</code> module has been deprecated\. Please use <code>community\.aws\.secretsmanager\_secret</code> instead \([https\://github\.com/ansible\-collections/community\.aws/pull/2387](https\://github\.com/ansible\-collections/community\.aws/pull/2387)\)\.
* The alias <code>aws\_ses\_identity\_policy</code> for the <code>ses\_identity\_policy</code> module has been deprecated\. Please use <code>community\.aws\.ses\_identity\_policy</code> instead \([https\://github\.com/ansible\-collections/community\.aws/pull/2387](https\://github\.com/ansible\-collections/community\.aws/pull/2387)\)\.
* The alias <code>aws\_ses\_identity</code> for the <code>ses\_identity</code> module has been deprecated\. Please use <code>community\.aws\.ses\_identity</code> instead \([https\://github\.com/ansible\-collections/community\.aws/pull/2387](https\://github\.com/ansible\-collections/community\.aws/pull/2387)\)\.
* The alias <code>aws\_ses\_rule\_set</code> for the <code>ses\_rule\_set</code> module has been deprecated\. Please use <code>community\.aws\.ses\_rule\_set</code> instead \([https\://github\.com/ansible\-collections/community\.aws/pull/2387](https\://github\.com/ansible\-collections/community\.aws/pull/2387)\)\.
* The alias <code>aws\_sgw\_info</code> for the <code>storagegateway\_info</code> module has been deprecated\. Please use <code>community\.aws\.storagegateway\_info</code> instead \([https\://github\.com/ansible\-collections/community\.aws/pull/2387](https\://github\.com/ansible\-collections/community\.aws/pull/2387)\)\.
* The alias <code>aws\_ssm\_parameter\_store</code> for the <code>ssm\_parameter</code> module has been deprecated\. Please use <code>community\.aws\.ssm\_parameter</code> instead \([https\://github\.com/ansible\-collections/community\.aws/pull/2387](https\://github\.com/ansible\-collections/community\.aws/pull/2387)\)\.
* The alias <code>aws\_step\_functions\_state\_machine\_execution</code> for the <code>stepfunctions\_state\_machine\_execution</code> module has been deprecated\. Please use <code>community\.aws\.stepfunctions\_state\_machine\_execution</code> instead \([https\://github\.com/ansible\-collections/community\.aws/pull/2387](https\://github\.com/ansible\-collections/community\.aws/pull/2387)\)\.
* The alias <code>aws\_step\_functions\_state\_machine</code> for the <code>stepfunctions\_state\_machine</code> module has been deprecated\. Please use <code>community\.aws\.stepfunctions\_state\_machine</code> instead \([https\://github\.com/ansible\-collections/community\.aws/pull/2387](https\://github\.com/ansible\-collections/community\.aws/pull/2387)\)\.
* The alias <code>aws\_waf\_condition</code> for the <code>waf\_condition</code> module has been deprecated\. Please use <code>community\.aws\.waf\_condition</code> instead \([https\://github\.com/ansible\-collections/community\.aws/pull/2387](https\://github\.com/ansible\-collections/community\.aws/pull/2387)\)\.
* The alias <code>aws\_waf\_info</code> for the <code>waf\_info</code> module has been deprecated\. Please use <code>community\.aws\.waf\_info</code> instead \([https\://github\.com/ansible\-collections/community\.aws/pull/2387](https\://github\.com/ansible\-collections/community\.aws/pull/2387)\)\.
* The alias <code>aws\_waf\_rule</code> for the <code>waf\_rule</code> module has been deprecated\. Please use <code>community\.aws\.waf\_rule</code> instead \([https\://github\.com/ansible\-collections/community\.aws/pull/2387](https\://github\.com/ansible\-collections/community\.aws/pull/2387)\)\.
* The alias <code>aws\_waf\_web\_acl</code> for the <code>waf\_web\_acl</code> module has been deprecated\. Please use <code>community\.aws\.waf\_web\_acl</code> instead \([https\://github\.com/ansible\-collections/community\.aws/pull/2387](https\://github\.com/ansible\-collections/community\.aws/pull/2387)\)\.
* The alias <code>cloudfront\_info</code> for the <code>cloudfront\_distribution\_info</code> module has been deprecated\. Please use <code>community\.aws\.cloudfront\_distribution\_info</code> instead \([https\://github\.com/ansible\-collections/community\.aws/pull/2387](https\://github\.com/ansible\-collections/community\.aws/pull/2387)\)\.
* The alias <code>cloudtrail</code> for the <code>cloudtrail</code> module has been deprecated\. Please use <code>amazon\.aws\.cloudtrail</code> instead \([https\://github\.com/ansible\-collections/community\.aws/pull/2387](https\://github\.com/ansible\-collections/community\.aws/pull/2387)\)\.
* The alias <code>ec2\_asg\_info</code> for the <code>autoscaling\_group\_info</code> module has been deprecated\. Please use <code>amazon\.aws\.autoscaling\_group\_info</code> instead \([https\://github\.com/ansible\-collections/community\.aws/pull/2387](https\://github\.com/ansible\-collections/community\.aws/pull/2387)\)\.
* The alias <code>ec2\_asg\_instance\_refresh\_info</code> for the <code>autoscaling\_instance\_refresh\_info</code> module has been deprecated\. Please use <code>amazon\.aws\.autoscaling\_instance\_refresh\_info</code> instead \([https\://github\.com/ansible\-collections/community\.aws/pull/2387](https\://github\.com/ansible\-collections/community\.aws/pull/2387)\)\.
* The alias <code>ec2\_asg\_instance\_refresh</code> for the <code>autoscaling\_instance\_refresh</code> module has been deprecated\. Please use <code>amazon\.aws\.autoscaling\_instance\_refresh</code> instead \([https\://github\.com/ansible\-collections/community\.aws/pull/2387](https\://github\.com/ansible\-collections/community\.aws/pull/2387)\)\.
* The alias <code>ec2\_asg\_lifecycle\_hook</code> for the <code>autoscaling\_lifecycle\_hook</code> module has been deprecated\. Please use <code>community\.aws\.autoscaling\_lifecycle\_hook</code> instead \([https\://github\.com/ansible\-collections/community\.aws/pull/2387](https\://github\.com/ansible\-collections/community\.aws/pull/2387)\)\.
* The alias <code>ec2\_asg\_scheduled\_action</code> for the <code>autoscaling\_scheduled\_action</code> module has been deprecated\. Please use <code>community\.aws\.autoscaling\_scheduled\_action</code> instead \([https\://github\.com/ansible\-collections/community\.aws/pull/2387](https\://github\.com/ansible\-collections/community\.aws/pull/2387)\)\.
* The alias <code>ec2\_asg</code> for the <code>autoscaling\_group</code> module has been deprecated\. Please use <code>amazon\.aws\.autoscaling\_group</code> instead \([https\://github\.com/ansible\-collections/community\.aws/pull/2387](https\://github\.com/ansible\-collections/community\.aws/pull/2387)\)\.
* The alias <code>ec2\_lc\_find</code> for the <code>autoscaling\_launch\_config\_find</code> module has been deprecated\. Please use <code>community\.aws\.autoscaling\_launch\_config\_find</code> instead \([https\://github\.com/ansible\-collections/community\.aws/pull/2387](https\://github\.com/ansible\-collections/community\.aws/pull/2387)\)\.
* The alias <code>ec2\_lc\_info</code> for the <code>autoscaling\_launch\_config\_info</code> module has been deprecated\. Please use <code>community\.aws\.autoscaling\_launch\_config\_info</code> instead \([https\://github\.com/ansible\-collections/community\.aws/pull/2387](https\://github\.com/ansible\-collections/community\.aws/pull/2387)\)\.
* The alias <code>ec2\_lc</code> for the <code>autoscaling\_launch\_config</code> module has been deprecated\. Please use <code>community\.aws\.autoscaling\_launch\_config</code> instead \([https\://github\.com/ansible\-collections/community\.aws/pull/2387](https\://github\.com/ansible\-collections/community\.aws/pull/2387)\)\.
* The alias <code>ec2\_metric\_alarm</code> for the <code>cloudwatch\_metric\_alarm</code> module has been deprecated\. Please use <code>amazon\.aws\.cloudwatch\_metric\_alarm</code> instead \([https\://github\.com/ansible\-collections/community\.aws/pull/2387](https\://github\.com/ansible\-collections/community\.aws/pull/2387)\)\.
* The alias <code>ec2\_scaling\_policy</code> for the <code>autoscaling\_policy</code> module has been deprecated\. Please use <code>community\.aws\.autoscaling\_policy</code> instead \([https\://github\.com/ansible\-collections/community\.aws/pull/2387](https\://github\.com/ansible\-collections/community\.aws/pull/2387)\)\.
* The alias <code>execute\_lambda</code> for the <code>lambda\_execute</code> module has been deprecated\. Please use <code>amazon\.aws\.lambda\_execute</code> instead \([https\://github\.com/ansible\-collections/community\.aws/pull/2387](https\://github\.com/ansible\-collections/community\.aws/pull/2387)\)\.
* cloudfront\_distribution \- The <code>items</code> return value in <code>active\_trusted\_signers</code> has been deprecated and will be removed in a release after 2026\-12\-15\. Use <code>elements</code> instead \([https\://github\.com/ansible\-collections/community\.aws/pull/2354](https\://github\.com/ansible\-collections/community\.aws/pull/2354)\)\.
* cloudfront\_distribution \- The <code>items</code> return value in <code>aliases</code> has been deprecated and will be removed in a release after 2026\-12\-15\. Use <code>elements</code> instead \([https\://github\.com/ansible\-collections/community\.aws/pull/2354](https\://github\.com/ansible\-collections/community\.aws/pull/2354)\)\.
* cloudfront\_distribution \- The <code>items</code> return value in <code>cache\_behaviors\.items\.allowed\_methods\.cached\_methods</code> has been deprecated and will be removed in a release after 2026\-12\-15\. Use <code>elements</code> instead \([https\://github\.com/ansible\-collections/community\.aws/pull/2354](https\://github\.com/ansible\-collections/community\.aws/pull/2354)\)\.
* cloudfront\_distribution \- The <code>items</code> return value in <code>cache\_behaviors\.items\.allowed\_methods</code> has been deprecated and will be remove in a release after 2026\-12\-15\. Use <code>elements</code> instead \([https\://github\.com/ansible\-collections/community\.aws/pull/2354](https\://github\.com/ansible\-collections/community\.aws/pull/2354)\)\.
* cloudfront\_distribution \- The <code>items</code> return value in <code>cache\_behaviors\.items\.forwarded\_values\.cookies\.whitelisted\_names</code> has been deprecated and will be remove in a release after 2026\-12\-15\. Use <code>elements</code> instead \([https\://github\.com/ansible\-collections/community\.aws/pull/2354](https\://github\.com/ansible\-collections/community\.aws/pull/2354)\)\.
* cloudfront\_distribution \- The <code>items</code> return value in <code>cache\_behaviors\.items\.forwarded\_values\.headers</code> has been deprecated and will be remove in a release after 2026\-12\-15\. Use <code>elements</code> instead \([https\://github\.com/ansible\-collections/community\.aws/pull/2354](https\://github\.com/ansible\-collections/community\.aws/pull/2354)\)\.
* cloudfront\_distribution \- The <code>items</code> return value in <code>cache\_behaviors\.items\.forwarded\_values\.query\_string\_cache\_keys</code> has been deprecated and will be remove in a release after 2026\-12\-15\. Use <code>elements</code> instead \([https\://github\.com/ansible\-collections/community\.aws/pull/2354](https\://github\.com/ansible\-collections/community\.aws/pull/2354)\)\.
* cloudfront\_distribution \- The <code>items</code> return value in <code>cache\_behaviors\.items\.lambda\_function\_associations</code> has been deprecated and will be remove in a release after 2026\-12\-15\. Use <code>elements</code> instead \([https\://github\.com/ansible\-collections/community\.aws/pull/2354](https\://github\.com/ansible\-collections/community\.aws/pull/2354)\)\.
* cloudfront\_distribution \- The <code>items</code> return value in <code>cache\_behaviors</code> has been deprecated and will be remove in a release after 2026\-12\-15\. Use <code>elements</code> instead \([https\://github\.com/ansible\-collections/community\.aws/pull/2354](https\://github\.com/ansible\-collections/community\.aws/pull/2354)\)\.
* cloudfront\_distribution \- The <code>items</code> return value in <code>custom\_error\_responses</code> has been deprecated and will be remove in a release after 2026\-12\-15\. Use <code>elements</code> instead \([https\://github\.com/ansible\-collections/community\.aws/pull/2354](https\://github\.com/ansible\-collections/community\.aws/pull/2354)\)\.
* cloudfront\_distribution \- The <code>items</code> return value in <code>default\_cache\_behavior\.allowed\_methods\.cached\_methods</code> has been deprecated and will be remove in a release after 2026\-12\-15\. Use <code>elements</code> instead \([https\://github\.com/ansible\-collections/community\.aws/pull/2354](https\://github\.com/ansible\-collections/community\.aws/pull/2354)\)\.
* cloudfront\_distribution \- The <code>items</code> return value in <code>default\_cache\_behavior\.allowed\_methods</code> has been deprecated and will be remove in a release after 2026\-12\-15\. Use <code>elements</code> instead \([https\://github\.com/ansible\-collections/community\.aws/pull/2354](https\://github\.com/ansible\-collections/community\.aws/pull/2354)\)\.
* cloudfront\_distribution \- The <code>items</code> return value in <code>default\_cache\_behavior\.forwarded\_values\.cookies\.whitelisted\_names</code> has been deprecated and will be remove in a release after 2026\-12\-15\. Use <code>elements</code> instead \([https\://github\.com/ansible\-collections/community\.aws/pull/2354](https\://github\.com/ansible\-collections/community\.aws/pull/2354)\)\.
* cloudfront\_distribution \- The <code>items</code> return value in <code>default\_cache\_behavior\.forwarded\_values\.headers</code> has been deprecated and will be remove in a release after 2026\-12\-15\. Use <code>elements</code> instead \([https\://github\.com/ansible\-collections/community\.aws/pull/2354](https\://github\.com/ansible\-collections/community\.aws/pull/2354)\)\.
* cloudfront\_distribution \- The <code>items</code> return value in <code>default\_cache\_behavior\.forwarded\_values\.query\_string\_cache\_keys</code> has been deprecated and will be remove in a release after 2026\-12\-15\. Use <code>elements</code> instead \([https\://github\.com/ansible\-collections/community\.aws/pull/2354](https\://github\.com/ansible\-collections/community\.aws/pull/2354)\)\.
* cloudfront\_distribution \- The <code>items</code> return value in <code>default\_cache\_behavior\.lambda\_function\_associations</code> has been deprecated and will be remove in a release after 2026\-12\-15\. Use <code>elements</code> instead \([https\://github\.com/ansible\-collections/community\.aws/pull/2354](https\://github\.com/ansible\-collections/community\.aws/pull/2354)\)\.
* cloudfront\_distribution \- The <code>items</code> return value in <code>origins\.items\.custom\_origin\_config\.origin\_ssl\_protocols</code> has been deprecated and will be remove in a release after 2026\-12\-15\. Use <code>elements</code> instead \([https\://github\.com/ansible\-collections/community\.aws/pull/2354](https\://github\.com/ansible\-collections/community\.aws/pull/2354)\)\.
* cloudfront\_distribution \- The <code>items</code> return value in <code>origins</code> has been deprecated and will be remove in a release after 2026\-12\-15\. Use <code>elements</code> instead \([https\://github\.com/ansible\-collections/community\.aws/pull/2354](https\://github\.com/ansible\-collections/community\.aws/pull/2354)\)\.
* cloudfront\_distribution \- The <code>items</code> return value in <code>restrictions\.geo\_restriction</code> has been deprecated and will be remove in a release after 2026\-12\-15\. Use <code>elements</code> instead \([https\://github\.com/ansible\-collections/community\.aws/pull/2354](https\://github\.com/ansible\-collections/community\.aws/pull/2354)\)\.
* cloudfront\_invalidation \- The <code>items</code> return value in <code>invalidation\.invalidation\_batch\.paths</code> has been deprecated and will be remove in a release after 2026\-12\-15\. Use <code>elements</code> instead \([https\://github\.com/ansible\-collections/community\.aws/pull/2354](https\://github\.com/ansible\-collections/community\.aws/pull/2354)\)\.
* cloudfront\_invalidation \- The <code>items</code> return value in <code>invalidation\.invalidation\_batch\.paths</code> has been deprecated and will be removed in a release after 2026\-12\-15\. Use <code>elements</code> instead \([https\://github\.com/ansible\-collections/community\.aws/pull/2354](https\://github\.com/ansible\-collections/community\.aws/pull/2354)\)\.
* waf\_condition \- The module has been deprecated as Amazon has retired the <code>WAF Classic</code> service\. Please use the <code>AWS WAF \(WAFv2\)</code> service and modules instead\. The module will be removed in version 12\.0\.0 \([https\://github\.com/ansible\-collections/community\.aws/pull/2389](https\://github\.com/ansible\-collections/community\.aws/pull/2389)\)\.
* waf\_info \- The module has been deprecated as Amazon has retired the <code>WAF Classic</code> service\. Please use the <code>AWS WAF \(WAFv2\)</code> service and modules instead\. The module will be removed in version 12\.0\.0 \([https\://github\.com/ansible\-collections/community\.aws/pull/2389](https\://github\.com/ansible\-collections/community\.aws/pull/2389)\)\.
* waf\_rule \- The module has been deprecated as Amazon has retired the <code>WAF Classic</code> service\. Please use the <code>AWS WAF \(WAFv2\)</code> service and modules instead\. The module will be removed in version 12\.0\.0 \([https\://github\.com/ansible\-collections/community\.aws/pull/2389](https\://github\.com/ansible\-collections/community\.aws/pull/2389)\)\.
* waf\_web\_acl \- The module has been deprecated as Amazon has retired the <code>WAF Classic</code> service\. Please use the <code>AWS WAF \(WAFv2\)</code> service and modules instead\. The module will be removed in version 12\.0\.0 \([https\://github\.com/ansible\-collections/community\.aws/pull/2389](https\://github\.com/ansible\-collections/community\.aws/pull/2389)\)\.

<a id="kubernetes-core-1"></a>
#### kubernetes\.core

* helm \- the <code>status\.values</code> return value has been deprecated and will be removed in a release after 2027\-01\-08\. Use <code>status\.release\_values</code> instead \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/1056](https\://github\.com/ansible\-collections/kubernetes\.core/pull/1056)\)\.
* helm\_info \- the <code>status\.values</code> return value has been deprecated and will be removed in a release after 2027\-01\-08\. Use <code>status\.release\_values</code> instead \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/1056](https\://github\.com/ansible\-collections/kubernetes\.core/pull/1056)\)\.

<a id="vmware-vmware-rest-1"></a>
#### vmware\.vmware\_rest

* Deprecate modules that have been moved to the new vmware\.vmware collection\. Includes vcenter\_vm\_guest\_customization\, vcenter\_vm\_hardware\_adapter\_sata\, vcenter\_vm\_hardware\_adapter\_scsi\, vcenter\_vm\_hardware\_cdrom\, vcenter\_vm\_hardware\_cpu\, vcenter\_vm\_hardware\_disk\, vcenter\_vm\_hardware\_ethernet\, vcenter\_vm\_hardware\_memory\, vcenter\_vm

<a id="security-fixes-1"></a>
### Security Fixes

<a id="kubernetes-core-2"></a>
#### kubernetes\.core

* Selectively redact sensitive info from kubeconfig instead of applying blanket <code>no\_log\=True</code> \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/1014](https\://github\.com/ansible\-collections/kubernetes\.core/pull/1014)\)\.

<a id="bugfixes-2"></a>
### Bugfixes

<a id="ansible-core-8"></a>
#### Ansible\-core

* Fix interpreter discovery on delegated <code>async</code> tasks \([https\://github\.com/ansible/ansible/issues/86491](https\://github\.com/ansible/ansible/issues/86491)\)
* Fix up the Action plugin <code>\_make\_tmp\_path</code> error to only include the command run rather than the shell\'s dataclass repr from <code>mkdtemp</code>\.
* local connection \- Pass correct type to become plugins when checking password \([https\://github\.com/ansible/ansible/issues/86458](https\://github\.com/ansible/ansible/issues/86458)\)

<a id="arista-eos"></a>
#### arista\.eos

* Fix eos\_vrf module to properly check existing interface configuration before making changes \([https\://github\.com/ansible\-collections/arista\.eos/issues/546](https\://github\.com/ansible\-collections/arista\.eos/issues/546)\)

<a id="cisco-ios-1"></a>
#### cisco\.ios

* Fixed delete and purged state function for ios\_bfd\_templates

<a id="cisco-meraki-3"></a>
#### cisco\.meraki

* Fix parameter naming in organizations\_inventory\_claim\.py to use camelCase for consistency with existing code\.

<a id="community-aws-2"></a>
#### community\.aws

* Remove <code>ansible\.module\_utils\.six</code> imports to avoid warnings \([https\://github\.com/ansible\-collections/community\.aws/pull/2338](https\://github\.com/ansible\-collections/community\.aws/pull/2338)\)\.
* ec2\_customer\_gateway \- Fix documentation for the return block \([https\://github\.com/ansible\-collections/community\.aws/pull/2354](https\://github\.com/ansible\-collections/community\.aws/pull/2354)\)\.

<a id="community-crypto-2"></a>
#### community\.crypto

* crypto\_info\, openssl\_privatekey\, openssl\_privatekey\_pipe \- fix detection of EC support for cryptography 46\.0\.5\+ \([https\://github\.com/ansible\-collections/community\.crypto/pull/981](https\://github\.com/ansible\-collections/community\.crypto/pull/981)\)\.

<a id="community-dns-2"></a>
#### community\.dns

* Update Public Suffix List\.

<a id="community-docker-2"></a>
#### community\.docker

* docker\_image\_pull\, docker\_container \- fix pulled image change detection for Docker 29\.2\+ \([https\://github\.com/ansible\-collections/community\.docker/pull/1242](https\://github\.com/ansible\-collections/community\.docker/pull/1242)\)\.

<a id="community-general-8"></a>
#### community\.general

* keycloak module utils \- fix <code>TypeError</code> crash when managing users whose username or email contains special characters such as <code>\+</code> \([https\://github\.com/ansible\-collections/community\.general/issues/10305](https\://github\.com/ansible\-collections/community\.general/issues/10305)\, [https\://github\.com/ansible\-collections/community\.general/pull/11472](https\://github\.com/ansible\-collections/community\.general/pull/11472)\)\.
* keycloak module utils \- use proper URL encoding \(<code>urllib\.parse\.quote</code>\) for query parameters in authorization permission name searches\, replacing fragile manual space replacement \([https\://github\.com/ansible\-collections/community\.general/pull/11472](https\://github\.com/ansible\-collections/community\.general/pull/11472)\)\.
* keycloak\_client \- fix idempotency bug caused by <code>null</code> flow overrides value differences for non\-existing flow overrides \([https\://github\.com/ansible\-collections/community\.general/issues/11430](https\://github\.com/ansible\-collections/community\.general/issues/11430)\, [https\://github\.com/ansible\-collections/community\.general/pull/11455](https\://github\.com/ansible\-collections/community\.general/pull/11455)\)\.
* keycloak\_client \- remove IDs as change from diff result for protocol mappers \([https\://github\.com/ansible\-collections/community\.general/issues/11453](https\://github\.com/ansible\-collections/community\.general/issues/11453)\, [https\://github\.com/ansible\-collections/community\.general/pull/11454](https\://github\.com/ansible\-collections/community\.general/pull/11454)\)\.
* keycloak\_realm\_key \- fix <code>KeyError</code> crash when managing realm keys where Keycloak does not return <code>active</code>\, <code>enabled</code>\, or <code>algorithm</code> fields in the config response \([https\://github\.com/ansible\-collections/community\.general/issues/11459](https\://github\.com/ansible\-collections/community\.general/issues/11459)\, [https\://github\.com/ansible\-collections/community\.general/pull/11470](https\://github\.com/ansible\-collections/community\.general/pull/11470)\)\.
* keycloak\_user\_federation \- mapper config item can be an array \([https\://github\.com/ansible\-collections/community\.general/issues/11502](https\://github\.com/ansible\-collections/community\.general/issues/11502)\, [https\://github\.com/ansible\-collections/community\.general/pull/11515](https\://github\.com/ansible\-collections/community\.general/pull/11515)\)\.
* keycloak\_user\_rolemapping \- fix <code>TypeError</code> crash when adding a client role to a user who has no existing roles for that client \([https\://github\.com/ansible\-collections/community\.general/issues/10960](https\://github\.com/ansible\-collections/community\.general/issues/10960)\, [https\://github\.com/ansible\-collections/community\.general/pull/11471](https\://github\.com/ansible\-collections/community\.general/pull/11471)\)\.
* maven\_artifact \- fix SNAPSHOT version resolution to pick the newest matching <code>\<snapshotVersion\></code> entry by <code>\<updated\></code> timestamp instead of the first\. Repositories like GitHub Packages keep all historical entries in <code>\<snapshotVersions\></code> \(oldest first\)\, causing the module to resolve to the oldest snapshot instead of the latest \([https\://github\.com/ansible\-collections/community\.general/issues/5117](https\://github\.com/ansible\-collections/community\.general/issues/5117)\, [https\://github\.com/ansible\-collections/community\.general/issues/11489](https\://github\.com/ansible\-collections/community\.general/issues/11489)\, [https\://github\.com/ansible\-collections/community\.general/pull/11501](https\://github\.com/ansible\-collections/community\.general/pull/11501)\)\.
* nsupdate \- fix <code>AttributeError</code> when using the module without TSIG authentication \([https\://github\.com/ansible\-collections/community\.general/issues/11460](https\://github\.com/ansible\-collections/community\.general/issues/11460)\, [https\://github\.com/ansible\-collections/community\.general/pull/11461](https\://github\.com/ansible\-collections/community\.general/pull/11461)\)\.
* python\_requirements\_info \- use <code>importlib\.metadata</code> if <code>pkg\_resources</code> from <code>setuptools</code> cannot be imported\. That module has been removed from setuptools 82\.0\.0 \([https\://github\.com/ansible\-collections/community\.general/issues/11491](https\://github\.com/ansible\-collections/community\.general/issues/11491)\, [https\://github\.com/ansible\-collections/community\.general/pull/11492](https\://github\.com/ansible\-collections/community\.general/pull/11492)\)\.
* splunk callback plugin \- replace deprecated callback function \([https\://github\.com/ansible\-collections/community\.general/pull/11485](https\://github\.com/ansible\-collections/community\.general/pull/11485)\)\.

<a id="community-libvirt-3"></a>
#### community\.libvirt

* virt\_install \- fixed cloud\_init configuration handling for meta\-data\, user\-data\, and network\-config\.
* virt\_install \- fixed the dict\-based options handling for events\, resource\, and sysinfo options\.

<a id="containers-podman-4"></a>
#### containers\.podman

* Fix Ansible warning about test utils

<a id="kubernetes-core-3"></a>
#### kubernetes\.core

* Add idempotency for <code>helm\_pull</code> module \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/1055](https\://github\.com/ansible\-collections/kubernetes\.core/pull/1055)\)\.
* Fixed a bug where setting <code>K8S\_AUTH\_VERIFY\_SSL\=true</code> \(or any string value\) caused the value to be treated as a separate <code>kubectl</code> command argument\. \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/1049](https\://github\.com/ansible\-collections/kubernetes\.core/pull/1049)\)\.
* Limit supported versions of Helm to \<4\.0\.0 \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/1039](https\://github\.com/ansible\-collections/kubernetes\.core/pull/1039)\)\.
* Replace passing <code>warnings</code> to <code>exit\_json</code> with <code>AnsibleModule\.warn</code> in the <code>k8s\_drain</code>\, <code>k8s\_rollback\.py</code> and <code>k8s\_scale\.py</code> modules as it deprecated in <code>ansible\-core\>\=2\.19\.0</code> and will be removed in <code>ansible\-core\>\=2\.23\.0</code> \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/1033](https\://github\.com/ansible\-collections/kubernetes\.core/pull/1033)\)\.
* k8s \- Fix return block from the module documentation \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/1056](https\://github\.com/ansible\-collections/kubernetes\.core/pull/1056)\)\.
* meta \- Add <code>k8s\_cluster\_info</code>\, <code>k8s\_json\_patch</code> and <code>k8s\_rollback</code> to k8s action group \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/992](https\://github\.com/ansible\-collections/kubernetes\.core/pull/992)\)\.

<a id="purestorage-flasharray"></a>
#### purestorage\.flasharray

* purefa\_certs \- Fix the syntax to generate a CSR
* purefa\_connect \- Fixed issue where incorrect transport type was passed\.
* purefa\_default\_protection \- Fixed issue adding new default protection group to the array scope
* purefa\_dsrole\_old \- Fixed incorrect parameter name for old version of functions
* purefa\_host \- Fixed AttributeError when deleting WWNs from a host
* purefa\_info \- Fixed AttributeError when subnet has no VLAN
* purefa\_info \- Fixed error with Resalms\-based API clients
* purefa\_info \- Fixed issue with shelf controllers not supporting uptime
* purefa\_info \- Resolved AttributeErrors in <code>default</code> info section
* purefa\_network \- Fixes issue caused by None meaning change in SDK
* purefa\_pgsched \- Fixed schedule deletion idempotency
* purefa\_policy \- Fixed AttributeError when modifying a password policy

<a id="new-plugins-1"></a>
### New Plugins

<a id="callback"></a>
#### Callback

* community\.general\.loganalytics\_ingestion \- Posts task results to an Azure Log Analytics workspace using the new Logs Ingestion API\.

<a id="new-modules-2"></a>
### New Modules

<a id="cisco-ios-2"></a>
#### cisco\.ios

* cisco\.ios\.ios\_bfd\_interfaces \- Resource module to configure bfd in interfaces\.
* cisco\.ios\.ios\_bfd\_templates \- Bidirectional Forwarding Detection \(BFD\) templates configurations

<a id="community-general-9"></a>
#### community\.general

* community\.general\.icinga2\_downtime \- Manages Icinga 2 downtimes\.
* community\.general\.keycloak\_realm\_localization \- Allows management of Keycloak realm localization overrides via the Keycloak API\.

<a id="community-libvirt-4"></a>
#### community\.libvirt

* community\.libvirt\.virt\_cloud\_instance \- Provision new virtual machines from cloud images via libvirt

<a id="containers-podman-5"></a>
#### containers\.podman

* containers\.podman\.podman\_quadlet \- Install or remove Podman Quadlets
* containers\.podman\.podman\_quadlet\_info \- Gather information about Podman Quadlets

<a id="hitachivantara-vspone-block-1"></a>
#### hitachivantara\.vspone\_block

<a id="sds-block"></a>
##### Sds Block

* hitachivantara\.vspone\_block\.hv\_sds\_block\_audit\_log\_setting \- Manages Hitachi SDS block storage system audit log settings\.
* hitachivantara\.vspone\_block\.hv\_sds\_block\_audit\_log\_setting\_facts \- Get audit log setting from SDS Block storage system\.
* hitachivantara\.vspone\_block\.hv\_sds\_block\_dump\_log\_file \- Dumps log information from SDS Block storage system\.
* hitachivantara\.vspone\_block\.hv\_sds\_block\_dump\_log\_status\_facts \- Dumps log status information from SDS Block storage system\.
* hitachivantara\.vspone\_block\.hv\_sds\_block\_event\_log\_setting \- Manages Hitachi SDS block storage system event log settings\.
* hitachivantara\.vspone\_block\.hv\_sds\_block\_event\_log\_setting\_facts \- Get event log setting from SDS Block storage system\.
* hitachivantara\.vspone\_block\.hv\_sds\_block\_journal \- Create and update Journals from storage system\.
* hitachivantara\.vspone\_block\.hv\_sds\_block\_journal\_facts \- Retrieve journal information from storage SDS Block storage system\.
* hitachivantara\.vspone\_block\.hv\_sds\_block\_license \- Manage licenses on SDS Block storage system\.
* hitachivantara\.vspone\_block\.hv\_sds\_block\_license\_facts \- Get license\(s\) from SDS Block storage system\.
* hitachivantara\.vspone\_block\.hv\_sds\_block\_license\_setting \- Manage license settings for SDS Block storage system\.
* hitachivantara\.vspone\_block\.hv\_sds\_block\_license\_setting\_facts \- Get license setting from SDS Block storage system\.
* hitachivantara\.vspone\_block\.hv\_sds\_block\_login\_message \- Update the login message displayed in the GUI login window and CLI warning banner\.
* hitachivantara\.vspone\_block\.hv\_sds\_block\_login\_message\_facts \- Get the login message displayed in the GUI login window and CLI warning banner\.
* hitachivantara\.vspone\_block\.hv\_sds\_block\_storage\_external\_auth\_server\_setting \- Manages external authentication server settings on VSP One SDS Block and Cloud systems\.
* hitachivantara\.vspone\_block\.hv\_sds\_block\_storage\_external\_auth\_server\_setting\_facts \- Get external authentication server settings from the storage system\.
* hitachivantara\.vspone\_block\.hv\_sds\_block\_storage\_user\_auth\_setting \- Manages external authentication server settings on VSP One SDS Block and Cloud systems\.
* hitachivantara\.vspone\_block\.hv\_sds\_block\_storage\_user\_auth\_setting\_facts \- Get user authentication settings from the storage system\.

<a id="vsp"></a>
##### Vsp

* hitachivantara\.vspone\_block\.hv\_pav\_alias \- Manages PAV \(Parallel Access Volume\) alias assignments for VSP block storage systems\.
* hitachivantara\.vspone\_block\.hv\_pav\_alias\_facts \- retrieves information about PAV aliases from VSP block storage systems\.
* hitachivantara\.vspone\_block\.hv\_session \- Manages sessions on VSP block storage systems\.
* hitachivantara\.vspone\_block\.hv\_session\_facts \- Retrieves information about sessions on VSP block storage systems\.
* hitachivantara\.vspone\_block\.hv\_snapshot\_family\_facts \- Retrieves snapshot family information of the provided LDEV ID from VSP block storage systems\.
* hitachivantara\.vspone\_block\.hv\_supported\_host\_mode\_facts \- Retrieves supported host mode options information from a specified VSP block storage system\.
* hitachivantara\.vspone\_block\.hv\_vclone\_parent\_volume\_facts \- Retrieves virtual clone parent volume information from VSP block storage systems\.

<a id="unchanged-collections-2"></a>
### Unchanged Collections

* amazon\.aws \(still version 10\.2\.0\)
* ansible\.posix \(still version 2\.1\.0\)
* ansible\.utils \(still version 6\.0\.1\)
* ansible\.windows \(still version 3\.3\.0\)
* awx\.awx \(still version 24\.6\.1\)
* azure\.azcollection \(still version 3\.14\.0\)
* check\_point\.mgmt \(still version 6\.8\.0\)
* chocolatey\.chocolatey \(still version 1\.5\.3\)
* cisco\.aci \(still version 2\.13\.0\)
* cisco\.intersight \(still version 2\.12\.0\)
* cisco\.iosxr \(still version 12\.1\.1\)
* cisco\.mso \(still version 2\.12\.0\)
* cisco\.nxos \(still version 11\.1\.3\)
* cisco\.ucs \(still version 1\.16\.0\)
* cloudscale\_ch\.cloud \(still version 2\.5\.3\)
* community\.ciscosmb \(still version 1\.0\.11\)
* community\.clickhouse \(still version 2\.0\.0\)
* community\.grafana \(still version 2\.3\.0\)
* community\.hashi\_vault \(still version 7\.1\.0\)
* community\.hrobot \(still version 2\.7\.0\)
* community\.library\_inventory\_filtering\_v1 \(still version 1\.1\.5\)
* community\.okd \(still version 5\.0\.0\)
* community\.postgresql \(still version 4\.2\.0\)
* community\.proxmox \(still version 1\.5\.0\)
* community\.proxysql \(still version 1\.7\.0\)
* community\.rabbitmq \(still version 1\.6\.0\)
* community\.routeros \(still version 3\.16\.0\)
* community\.sap\_libs \(still version 1\.6\.0\)
* community\.sops \(still version 2\.2\.7\)
* community\.vmware \(still version 6\.2\.0\)
* community\.windows \(still version 3\.1\.0\)
* community\.zabbix \(still version 4\.1\.1\)
* cyberark\.conjur \(still version 1\.3\.9\)
* cyberark\.pas \(still version 1\.0\.36\)
* dellemc\.enterprise\_sonic \(still version 3\.2\.0\)
* dellemc\.openmanage \(still version 10\.0\.1\)
* dellemc\.powerflex \(still version 3\.0\.0\)
* dellemc\.unity \(still version 2\.1\.0\)
* f5networks\.f5\_modules \(still version 1\.39\.0\)
* fortinet\.fortimanager \(still version 2\.12\.0\)
* fortinet\.fortios \(still version 2\.4\.2\)
* google\.cloud \(still version 1\.11\.0\)
* grafana\.grafana \(still version 6\.0\.6\)
* hetzner\.hcloud \(still version 6\.7\.0\)
* hitachivantara\.vspone\_object \(still version 1\.1\.1\)
* ibm\.storage\_virtualize \(still version 3\.2\.0\)
* ieisystem\.inmanage \(still version 4\.0\.0\)
* infinidat\.infinibox \(still version 1\.6\.3\)
* infoblox\.nios\_modules \(still version 1\.9\.0\)
* inspur\.ispim \(still version 2\.2\.4\)
* junipernetworks\.junos \(still version 11\.0\.0\)
* kaytus\.ksmanage \(still version 2\.0\.0\)
* kubevirt\.core \(still version 2\.2\.3\)
* lowlydba\.sqlserver \(still version 2\.7\.0\)
* microsoft\.ad \(still version 1\.10\.0\)
* microsoft\.iis \(still version 1\.1\.0\)
* netapp\.cloudmanager \(still version 21\.24\.0\)
* netapp\.ontap \(still version 23\.3\.0\)
* netapp\.storagegrid \(still version 21\.16\.0\)
* netapp\_eseries\.santricity \(still version 1\.4\.1\)
* netbox\.netbox \(still version 3\.22\.0\)
* ngine\_io\.cloudstack \(still version 3\.0\.0\)
* openstack\.cloud \(still version 2\.5\.0\)
* ovirt\.ovirt \(still version 3\.2\.2\)
* purestorage\.flashblade \(still version 1\.24\.0\)
* ravendb\.ravendb \(still version 1\.0\.4\)
* splunk\.es \(still version 4\.0\.0\)
* telekom\_mms\.icinga\_director \(still version 2\.5\.1\)
* theforeman\.foreman \(still version 5\.8\.0\)
* vmware\.vmware \(still version 2\.7\.0\)
* vultr\.cloud \(still version 1\.13\.0\)
* vyos\.vyos \(still version 6\.0\.0\)
* wti\.remote \(still version 1\.0\.10\)

<a id="v13-3-0"></a>
## v13\.3\.0

- <a href="#release-summary-3">Release Summary</a>
- <a href="#added-collections-1">Added Collections</a>
- <a href="#ansible-core-9">Ansible\-core</a>
- <a href="#changed-collections-3">Changed Collections</a>
- <a href="#major-changes-3">Major Changes</a>
    - <a href="#community-vmware">community\.vmware</a>
    - <a href="#containers-podman-6">containers\.podman</a>
- <a href="#minor-changes-3">Minor Changes</a>
    - <a href="#ansible-core-10">Ansible\-core</a>
    - <a href="#amazon-aws-3">amazon\.aws</a>
    - <a href="#cisco-dnac-1">cisco\.dnac</a>
    - <a href="#cisco-meraki-4">cisco\.meraki</a>
    - <a href="#cloudscale-ch-cloud">cloudscale\_ch\.cloud</a>
    - <a href="#community-dns-3">community\.dns</a>
    - <a href="#community-general-10">community\.general</a>
    - <a href="#community-routeros-6">community\.routeros</a>
    - <a href="#containers-podman-7">containers\.podman</a>
    - <a href="#google-cloud-2">google\.cloud</a>
    - <a href="#hetzner-hcloud-1">hetzner\.hcloud</a>
    - <a href="#ibm-storage-virtualize-2">ibm\.storage\_virtualize</a>
    - <a href="#infoblox-nios-modules">infoblox\.nios\_modules</a>
    - <a href="#netbox-netbox">netbox\.netbox</a>
    - <a href="#ovirt-ovirt">ovirt\.ovirt</a>
    - <a href="#theforeman-foreman-4">theforeman\.foreman</a>
    - <a href="#vmware-vmware-2">vmware\.vmware</a>
- <a href="#deprecated-features-3">Deprecated Features</a>
    - <a href="#amazon-aws-4">amazon\.aws</a>
    - <a href="#hetzner-hcloud-2">hetzner\.hcloud</a>
- <a href="#bugfixes-3">Bugfixes</a>
    - <a href="#ansible-core-11">Ansible\-core</a>
    - <a href="#amazon-aws-5">amazon\.aws</a>
    - <a href="#ansible-netcommon-4">ansible\.netcommon</a>
    - <a href="#ansible-utils-1">ansible\.utils</a>
    - <a href="#cisco-nxos">cisco\.nxos</a>
    - <a href="#community-dns-4">community\.dns</a>
    - <a href="#community-docker-3">community\.docker</a>
    - <a href="#community-general-11">community\.general</a>
    - <a href="#community-vmware-1">community\.vmware</a>
    - <a href="#containers-podman-8">containers\.podman</a>
    - <a href="#google-cloud-3">google\.cloud</a>
    - <a href="#hetzner-hcloud-3">hetzner\.hcloud</a>
    - <a href="#infoblox-nios-modules-1">infoblox\.nios\_modules</a>
    - <a href="#netbox-netbox-1">netbox\.netbox</a>
    - <a href="#ovirt-ovirt-1">ovirt\.ovirt</a>
    - <a href="#purestorage-flashblade">purestorage\.flashblade</a>
    - <a href="#vmware-vmware-3">vmware\.vmware</a>
- <a href="#new-plugins-2">New Plugins</a>
    - <a href="#filter-1">Filter</a>
- <a href="#new-modules-3">New Modules</a>
    - <a href="#ibm-storage-virtualize-3">ibm\.storage\_virtualize</a>
    - <a href="#netbox-netbox-2">netbox\.netbox</a>
- <a href="#unchanged-collections-3">Unchanged Collections</a>

<a id="release-summary-3"></a>
### Release Summary

Release Date\: 2026\-01\-29

[Porting Guide](https\://docs\.ansible\.com/projects/ansible/devel/porting\_guides\.html)

<a id="added-collections-1"></a>
### Added Collections

* community\.clickhouse \(version 2\.0\.0\)
* pcg\.alpaca\_operator \(version 2\.1\.1\)

<a id="ansible-core-9"></a>
### Ansible\-core

Ansible 13\.3\.0 contains ansible\-core version 2\.20\.2\.
This is a newer version than version 2\.20\.1 contained in the previous Ansible release\.

The changes are reported in the combined changelog below\.

<a id="changed-collections-3"></a>
### Changed Collections

If not mentioned explicitly\, the changes are reported in the combined changelog below\.

| Collection                  | Ansible 13.2.0 | Ansible 13.3.0 | Notes                                                                                                                        |
| --------------------------- | -------------- | -------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| amazon.aws                  | 10.1.2         | 10.2.0         |                                                                                                                              |
| ansible.netcommon           | 8.2.0          | 8.2.1          |                                                                                                                              |
| ansible.utils               | 6.0.0          | 6.0.1          |                                                                                                                              |
| azure.azcollection          | 3.12.0         | 3.14.0         | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
| cisco.dnac                  | 6.43.0         | 6.44.0         |                                                                                                                              |
| cisco.meraki                | 2.21.9         | 2.22.0         |                                                                                                                              |
| cisco.nxos                  | 11.1.1         | 11.1.3         |                                                                                                                              |
| cloudscale_ch.cloud         | 2.5.2          | 2.5.3          |                                                                                                                              |
| community.clickhouse        |                | 2.0.0          | The collection was added to Ansible                                                                                          |
| community.dns               | 3.4.2          | 3.5.1          |                                                                                                                              |
| community.docker            | 5.0.4          | 5.0.5          |                                                                                                                              |
| community.general           | 12.2.0         | 12.3.0         |                                                                                                                              |
| community.mongodb           | 1.7.10         | 1.7.11         | There are no changes recorded in the changelog.                                                                              |
| community.routeros          | 3.15.0         | 3.16.0         |                                                                                                                              |
| community.vmware            | 6.1.0          | 6.2.0          |                                                                                                                              |
| containers.podman           | 1.18.0         | 1.18.1         |                                                                                                                              |
| google.cloud                | 1.10.2         | 1.11.0         |                                                                                                                              |
| hetzner.hcloud              | 6.3.0          | 6.7.0          |                                                                                                                              |
| ibm.storage_virtualize      | 3.1.0          | 3.2.0          |                                                                                                                              |
| infoblox.nios_modules       | 1.8.0          | 1.9.0          |                                                                                                                              |
| netbox.netbox               | 3.21.0         | 3.22.0         |                                                                                                                              |
| ovirt.ovirt                 | 3.2.1          | 3.2.2          |                                                                                                                              |
| pcg.alpaca_operator         |                | 2.1.1          | The collection was added to Ansible                                                                                          |
| purestorage.flashblade      | 1.23.1         | 1.24.0         |                                                                                                                              |
| telekom_mms.icinga_director | 2.5.0          | 2.5.1          |                                                                                                                              |
| theforeman.foreman          | 5.7.0          | 5.8.0          |                                                                                                                              |
| vmware.vmware               | 2.6.0          | 2.7.0          |                                                                                                                              |

<a id="major-changes-3"></a>
### Major Changes

<a id="community-vmware"></a>
#### community\.vmware

* Bump required <code>vmware\.vmware</code> collection version to 2\.5\.0 \([https\://github\.com/ansible\-collections/community\.vmware/pull/2503](https\://github\.com/ansible\-collections/community\.vmware/pull/2503)\)\.

<a id="containers-podman-6"></a>
#### containers\.podman

* Rewrite podman and buildah connections

<a id="minor-changes-3"></a>
### Minor Changes

<a id="ansible-core-10"></a>
#### Ansible\-core

* ansible\-test \- Replace RHEL 10\.0 remote with 10\.1\.
* ansible\-test \- Replace RHEL 9\.6 remote with 9\.7\.

<a id="amazon-aws-3"></a>
#### amazon\.aws

* Add support for the io2 storage type for RDS \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2748](https\://github\.com/ansible\-collections/amazon\.aws/pull/2748)\)\.
* ec2\_launch\_template \- increase GP3 volume <code>throughput</code> limits in line with updated AWS limits \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2749](https\://github\.com/ansible\-collections/amazon\.aws/pull/2749)\)\.
* ec2\_vol \- increase <code>throughput</code> and <code>iops</code> limits for GP3 volumes in line with updated AWS limits \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2749](https\://github\.com/ansible\-collections/amazon\.aws/pull/2749)\)\.
* module\_utils\.s3 \- added \"501\" to the list of error codes thrown by S3 replacements \([https\://github\.com/ansible\-collections/amazon\.aws/issues/2447](https\://github\.com/ansible\-collections/amazon\.aws/issues/2447)\)\.
* module\_utils/\_s3/common \- use <code>is\_boto3\_error\_httpstatus</code> to handle HTTP 403 and 501 status codes from S3\-compatible services \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2776](https\://github\.com/ansible\-collections/amazon\.aws/pull/2776)\)\.
* module\_utils/botocore \- add <code>is\_boto3\_error\_httpstatus</code> helper function to catch boto3 exceptions based on HTTP status codes \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2776](https\://github\.com/ansible\-collections/amazon\.aws/pull/2776)\)\.
* route53 \- added <code>record\_values</code> key to <code>resource\_record\_sets</code> return value that can be accessed using Jinja2 dot notation \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2772](https\://github\.com/ansible\-collections/amazon\.aws/pull/2772)\)\.
* sts\_assume\_role \- improve error handling for <code>MalformedPolicyDocument</code> errors by providing a clearer error message when an invalid policy document is provided \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2778](https\://github\.com/ansible\-collections/amazon\.aws/pull/2778)\)\.

<a id="cisco-dnac-1"></a>
#### cisco\.dnac

* Added \'template\_content\_file\_path\'  attribute in template\_workflow\_manager module
* Changes in accesspoint\_location\_workflow\_manager module
* Changes in accesspoint\_workflow\_manager module
* Changes in application\_policy\_workflow\_manager module
* Changes in assurance\_device\_health\_score\_settings\_workflow\_manager module
* Changes in assurance\_icap\_settings\_workflow\_manager module
* Changes in device\_conigs\_backup\_workflow\_manager module
* Changes in inventory\_workflow\_manager module
* Changes in network\_settings\_workflow\_manager module
* Changes in provision\_workflow\_manager module
* Changes in reports\_workflow\_manager module
* Changes in sda\_fabric\_mulitcast\_workflow\_manager module
* Changes in sda\_fabric\_sites\_zones\_workflow\_manager module
* Changes in site\_workflow\_manager module
* Changes in swim\_workflow\_manager module
* Changes in template\_workflow\_manager module
* Changes in user\_role\_workflow\_manager module
* Changes in wireless\_design\_workflow\_manager module

<a id="cisco-meraki-4"></a>
#### cisco\.meraki

* Updated with v1\.66\.0 dashboard API\, adding new plugins and fixing bugs\.

<a id="cloudscale-ch-cloud"></a>
#### cloudscale\_ch\.cloud

* Added missing param when creating a health monitor

<a id="community-dns-3"></a>
#### community\.dns

* Hetzner DNS modules and plugins \- support the [new Hetzner DNS API](https\://docs\.hetzner\.com/networking/dns/faq/beta/) \([https\://github\.com/ansible\-collections/community\.dns/pull/301](https\://github\.com/ansible\-collections/community\.dns/pull/301)\)\.

<a id="community-general-10"></a>
#### community\.general

* alicloud\_ecs module utils \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11341](https\://github\.com/ansible\-collections/community\.general/pull/11341)\)\.
* android\_sdk \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11343](https\://github\.com/ansible\-collections/community\.general/pull/11343)\)\.
* archive \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11343](https\://github\.com/ansible\-collections/community\.general/pull/11343)\)\.
* bitbucket\_pipeline\_known\_host \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11343](https\://github\.com/ansible\-collections/community\.general/pull/11343)\)\.
* chroot connection plugin \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11341](https\://github\.com/ansible\-collections/community\.general/pull/11341)\)\.
* cobbler inventory plugin \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11341](https\://github\.com/ansible\-collections/community\.general/pull/11341)\)\.
* copr \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11343](https\://github\.com/ansible\-collections/community\.general/pull/11343)\)\.
* cronvar \- simplify handling unknown exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11340](https\://github\.com/ansible\-collections/community\.general/pull/11340)\)\.
* cronvar \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11343](https\://github\.com/ansible\-collections/community\.general/pull/11343)\)\.
* crypttab \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11343](https\://github\.com/ansible\-collections/community\.general/pull/11343)\)\.
* elasticsearch\_plugin \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11343](https\://github\.com/ansible\-collections/community\.general/pull/11343)\)\.
* gitlab\_group \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11343](https\://github\.com/ansible\-collections/community\.general/pull/11343)\)\.
* gitlab\_issue \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11343](https\://github\.com/ansible\-collections/community\.general/pull/11343)\)\.
* gitlab\_merge\_request \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11343](https\://github\.com/ansible\-collections/community\.general/pull/11343)\)\.
* gitlab\_project \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11343](https\://github\.com/ansible\-collections/community\.general/pull/11343)\)\.
* gunicorn \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11343](https\://github\.com/ansible\-collections/community\.general/pull/11343)\)\.
* htpasswd \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11343](https\://github\.com/ansible\-collections/community\.general/pull/11343)\)\.
* idrac\_redfish\_info \- add multiple manager support to <code>GetManagerAttributes</code> command \([https\://github\.com/ansible\-collections/community\.general/pull/11294](https\://github\.com/ansible\-collections/community\.general/pull/11294)\)\.
* imc\_rest \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11343](https\://github\.com/ansible\-collections/community\.general/pull/11343)\)\.
* incus connection plugin \- improve code readability \([https\://github\.com/ansible\-collections/community\.general/pull/11346](https\://github\.com/ansible\-collections/community\.general/pull/11346)\)\.
* incus connection plugin \- simplify regular expression matching commands \([https\://github\.com/ansible\-collections/community\.general/pull/11347](https\://github\.com/ansible\-collections/community\.general/pull/11347)\)\.
* ini\_file \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11343](https\://github\.com/ansible\-collections/community\.general/pull/11343)\)\.
* interfaces\_file \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11343](https\://github\.com/ansible\-collections/community\.general/pull/11343)\)\.
* iptables\_state \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11343](https\://github\.com/ansible\-collections/community\.general/pull/11343)\)\.
* jail connection plugin \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11341](https\://github\.com/ansible\-collections/community\.general/pull/11341)\)\.
* jenkins\_credential \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11343](https\://github\.com/ansible\-collections/community\.general/pull/11343)\)\.
* jenkins\_plugin \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11343](https\://github\.com/ansible\-collections/community\.general/pull/11343)\)\.
* jenkins\_script \- move <code>import</code> statemetns to the top of the file \([https\://github\.com/ansible\-collections/community\.general/pull/11396](https\://github\.com/ansible\-collections/community\.general/pull/11396)\)\.
* kdeconfig \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11343](https\://github\.com/ansible\-collections/community\.general/pull/11343)\)\.
* known\_hosts module utils \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11341](https\://github\.com/ansible\-collections/community\.general/pull/11341)\)\.
* layman \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11343](https\://github\.com/ansible\-collections/community\.general/pull/11343)\)\.
* linode \- move <code>import</code> statemetns to the top of the file \([https\://github\.com/ansible\-collections/community\.general/pull/11396](https\://github\.com/ansible\-collections/community\.general/pull/11396)\)\.
* linode inventory plugin \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11341](https\://github\.com/ansible\-collections/community\.general/pull/11341)\)\.
* listen\_ports\_facts \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11343](https\://github\.com/ansible\-collections/community\.general/pull/11343)\)\.
* locale\_gen \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11343](https\://github\.com/ansible\-collections/community\.general/pull/11343)\)\.
* logentries callback plugin \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11341](https\://github\.com/ansible\-collections/community\.general/pull/11341)\)\.
* lvm\_pv \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11343](https\://github\.com/ansible\-collections/community\.general/pull/11343)\)\.
* lxc connection plugin \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11341](https\://github\.com/ansible\-collections/community\.general/pull/11341)\)\.
* lxd inventory plugin \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11341](https\://github\.com/ansible\-collections/community\.general/pull/11341)\)\.
* lxd module utils \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11341](https\://github\.com/ansible\-collections/community\.general/pull/11341)\)\.
* manageiq module utils \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11341](https\://github\.com/ansible\-collections/community\.general/pull/11341)\)\.
* manageiq\_alert\_profiles \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11344](https\://github\.com/ansible\-collections/community\.general/pull/11344)\)\.
* modprobe \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11344](https\://github\.com/ansible\-collections/community\.general/pull/11344)\)\.
* mssql\_db \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11344](https\://github\.com/ansible\-collections/community\.general/pull/11344)\)\.
* nagios \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11344](https\://github\.com/ansible\-collections/community\.general/pull/11344)\)\.
* netcup\_dns \- support diff mode \([https\://github\.com/ansible\-collections/community\.general/pull/11376](https\://github\.com/ansible\-collections/community\.general/pull/11376)\)\.
* nmcli \- add idempotency check \([https\://github\.com/ansible\-collections/community\.general/pull/11114](https\://github\.com/ansible\-collections/community\.general/pull/11114)\)\.
* nmcli \- add support for IPv6 routing rules \([https\://github\.com/ansible\-collections/community\.general/issues/7094](https\://github\.com/ansible\-collections/community\.general/issues/7094)\, [https\://github\.com/ansible\-collections/community\.general/pull/11413](https\://github\.com/ansible\-collections/community\.general/pull/11413)\)\.
* nosh \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11344](https\://github\.com/ansible\-collections/community\.general/pull/11344)\)\.
* nsupdate \- add support for server FQDN and the GSS\-TSIG key algorithm \([https\://github\.com/ansible\-collections/community\.general/issues/5730](https\://github\.com/ansible\-collections/community\.general/issues/5730)\, [https\://github\.com/ansible\-collections/community\.general/pull/11425](https\://github\.com/ansible\-collections/community\.general/pull/11425)\)\.
* nsupdate modules plugin \- replace aliased errors with proper Python error \([https\://github\.com/ansible\-collections/community\.general/pull/11391](https\://github\.com/ansible\-collections/community\.general/pull/11391)\)\.
* oci\_utils module utils \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11341](https\://github\.com/ansible\-collections/community\.general/pull/11341)\)\.
* omapi\_host \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11344](https\://github\.com/ansible\-collections/community\.general/pull/11344)\)\.
* one\_image \- move <code>import</code> statemetns to the top of the file \([https\://github\.com/ansible\-collections/community\.general/pull/11396](https\://github\.com/ansible\-collections/community\.general/pull/11396)\)\.
* one\_image\_info \- move <code>import</code> statemetns to the top of the file \([https\://github\.com/ansible\-collections/community\.general/pull/11396](https\://github\.com/ansible\-collections/community\.general/pull/11396)\)\.
* one\_service \- move <code>import</code> statemetns to the top of the file \([https\://github\.com/ansible\-collections/community\.general/pull/11396](https\://github\.com/ansible\-collections/community\.general/pull/11396)\)\.
* one\_vm \- move <code>import</code> statemetns to the top of the file \([https\://github\.com/ansible\-collections/community\.general/pull/11396](https\://github\.com/ansible\-collections/community\.general/pull/11396)\)\.
* one\_vm \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11344](https\://github\.com/ansible\-collections/community\.general/pull/11344)\)\.
* opennebula inventory plugin \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11341](https\://github\.com/ansible\-collections/community\.general/pull/11341)\)\.
* pam\_limits \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11344](https\://github\.com/ansible\-collections/community\.general/pull/11344)\)\.
* pamd \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11344](https\://github\.com/ansible\-collections/community\.general/pull/11344)\)\.
* parted \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11344](https\://github\.com/ansible\-collections/community\.general/pull/11344)\)\.
* pmem \- simplify text tests without using regular expression \([https\://github\.com/ansible\-collections/community\.general/pull/11388](https\://github\.com/ansible\-collections/community\.general/pull/11388)\)\.
* pubnub\_blocks \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11344](https\://github\.com/ansible\-collections/community\.general/pull/11344)\)\.
* pulp\_repo \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11344](https\://github\.com/ansible\-collections/community\.general/pull/11344)\)\.
* read\_csv \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11344](https\://github\.com/ansible\-collections/community\.general/pull/11344)\)\.
* redfish\_utils module utils \- adds support of <code>\@Redfish\.Settings</code> in <code>ComputerSystem</code> attributes for <code>set\_boot\_override</code> function \([https\://github\.com/ansible\-collections/community\.general/issues/11297](https\://github\.com/ansible\-collections/community\.general/issues/11297)\, [https\://github\.com/ansible\-collections/community\.general/pull/11322](https\://github\.com/ansible\-collections/community\.general/pull/11322)\)\.
* redhat\_subscription \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11344](https\://github\.com/ansible\-collections/community\.general/pull/11344)\)\.
* rhsm\_repository \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11344](https\://github\.com/ansible\-collections/community\.general/pull/11344)\)\.
* runit \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11344](https\://github\.com/ansible\-collections/community\.general/pull/11344)\)\.
* scaleway\_ip \- added <code>project</code> parameter \([https\://github\.com/ansible\-collections/community\.general/issues/11367](https\://github\.com/ansible\-collections/community\.general/issues/11367)\, [https\://github\.com/ansible\-collections/community\.general/pull/11368](https\://github\.com/ansible\-collections/community\.general/pull/11368)\)\.
* scaleway\_security\_group \- added <code>project</code> parameter \([https\://github\.com/ansible\-collections/community\.general/issues/11364](https\://github\.com/ansible\-collections/community\.general/issues/11364)\, [https\://github\.com/ansible\-collections/community\.general/pull/11366](https\://github\.com/ansible\-collections/community\.general/pull/11366)\)\.
* sensu\_check \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11344](https\://github\.com/ansible\-collections/community\.general/pull/11344)\)\.
* sensu\_client \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11344](https\://github\.com/ansible\-collections/community\.general/pull/11344)\)\.
* sensu\_handler \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11344](https\://github\.com/ansible\-collections/community\.general/pull/11344)\)\.
* sensu\_subscription \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11344](https\://github\.com/ansible\-collections/community\.general/pull/11344)\)\.
* seport \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11344](https\://github\.com/ansible\-collections/community\.general/pull/11344)\)\.
* serverless \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11344](https\://github\.com/ansible\-collections/community\.general/pull/11344)\)\.
* slackpkg \- refactor function <code>query\_packages\(\)</code> \([https\://github\.com/ansible\-collections/community\.general/pull/11390](https\://github\.com/ansible\-collections/community\.general/pull/11390)\)\.
* solaris\_zone \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11344](https\://github\.com/ansible\-collections/community\.general/pull/11344)\)\.
* sorcery \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11344](https\://github\.com/ansible\-collections/community\.general/pull/11344)\)\.
* spotinst\_aws\_elastigroup \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11344](https\://github\.com/ansible\-collections/community\.general/pull/11344)\)\.
* sudoers \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11344](https\://github\.com/ansible\-collections/community\.general/pull/11344)\)\.
* svc \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11344](https\://github\.com/ansible\-collections/community\.general/pull/11344)\)\.
* timestamp callback plugin \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11341](https\://github\.com/ansible\-collections/community\.general/pull/11341)\)\.
* timezone \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11344](https\://github\.com/ansible\-collections/community\.general/pull/11344)\)\.
* univention\_umc module utils \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11341](https\://github\.com/ansible\-collections/community\.general/pull/11341)\)\.
* wakeonlan \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11344](https\://github\.com/ansible\-collections/community\.general/pull/11344)\)\.
* wsl connection plugin \- add option <code>wsl\_remote\_ssh\_shell\_type</code>\. Support PowerShell in addition to cmd as the Windows shell \([https\://github\.com/ansible\-collections/community\.general/issues/11307](https\://github\.com/ansible\-collections/community\.general/issues/11307)\, [https\://github\.com/ansible\-collections/community\.general/pull/11308](https\://github\.com/ansible\-collections/community\.general/pull/11308)\)\.
* wsl connection plugin \- replace aliased errors with proper Python error \([https\://github\.com/ansible\-collections/community\.general/pull/11391](https\://github\.com/ansible\-collections/community\.general/pull/11391)\)\.
* wsl connection plugin \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11341](https\://github\.com/ansible\-collections/community\.general/pull/11341)\)\.
* xfs\_quota \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11344](https\://github\.com/ansible\-collections/community\.general/pull/11344)\)\.
* yaml cache plugin \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11341](https\://github\.com/ansible\-collections/community\.general/pull/11341)\)\.
* zone connection plugin \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11341](https\://github\.com/ansible\-collections/community\.general/pull/11341)\)\.
* zypper \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11344](https\://github\.com/ansible\-collections/community\.general/pull/11344)\)\.
* zypper\_repository \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11344](https\://github\.com/ansible\-collections/community\.general/pull/11344)\)\.

<a id="community-routeros-6"></a>
#### community\.routeros

* api\_info\, api\_modify \- add <code>prefix\-pool</code> field to and fix default of <code>address\-pool</code> for <code>ipv6 dhcp\-server</code> path \([https\://github\.com/ansible\-collections/community\.routeros/pull/430](https\://github\.com/ansible\-collections/community\.routeros/pull/430)\)\.
* api\_info\, api\_modify \- add support for path <code>ip socks access</code> \([https\://github\.com/ansible\-collections/community\.routeros/pull/431](https\://github\.com/ansible\-collections/community\.routeros/pull/431)\)\.

<a id="containers-podman-7"></a>
#### containers\.podman

* Add configuration for new Ansible release
* Fix CI of Podman Search modul
* add passthrough and none log driver options

<a id="google-cloud-2"></a>
#### google\.cloud

* gcp\_cloudbuildv2\_\* \- added gcp\_cloudbuildv2\_connection and gcp\_cloudbuildv2\_repository modules \([https\://github\.com/ansible\-collections/google\.cloud/pull/729](https\://github\.com/ansible\-collections/google\.cloud/pull/729)\)\.

<a id="hetzner-hcloud-1"></a>
#### hetzner\.hcloud

* All <code>module\_utils</code> are now marked as <strong>private</strong>\. None of the modules were intended for public use\.
* floating\_ip \- Unassign Floating IP before deleting it\.
* primary\_ip \- Added the Primary IP <code>location</code> name to the return values \(<code>hcloud\_primary\_ip\.location</code>\)\.
* primary\_ip \- Added the <code>location</code> argument to create a Primary IP in a specific location\.
* primary\_ip \- Unassign Primary IP before deleting it\.
* primary\_ip\_info \- Added the Primary IPs <code>location</code> name to the return values \(<code>hcloud\_primary\_ip\_info\[\]\.location</code>\)\.
* server \- Rebuilding a Server now supports the <code>user\_data</code> argument\.
* storage\_box \- The module is no longer marked as experimental\.
* storage\_box\_info \- The module is no longer marked as experimental\.
* storage\_box\_snapshot \- The module is no longer marked as experimental\.
* storage\_box\_snapshot\_info \- The module is no longer marked as experimental\.
* storage\_box\_subaccount \- Replace the label based name workaround\, with the new Storage Box Subaccount name property in the API\.
* storage\_box\_subaccount \- The module is no longer marked as experimental\.
* storage\_box\_subaccount\_info \- Replace the label based name workaround\, with the new Storage Box Subaccount name property in the API\.
* storage\_box\_subaccount\_info \- The module is no longer marked as experimental\.
* storage\_box\_type\_info \- The module is no longer marked as experimental\.

<a id="ibm-storage-virtualize-2"></a>
#### ibm\.storage\_virtualize

* ibm\_sv\_manage\_replication\_policy \- Enabled support for logging in via partition ip
* ibm\_svc\_manage\_volume \- Added support for autoexpand\, preferrednode and cache parameters

<a id="infoblox-nios-modules"></a>
#### infoblox\.nios\_modules

* CI/CD \- Added PyGObject support and improved dependency handling
* nios\_dtc\_lbdn \- Added support for auth\_zones with enhanced change detection for string and object formats\, including proper handling when entries are removed

<a id="netbox-netbox"></a>
#### netbox\.netbox

* Add integration tests for contact groups
* Add support for custom headers for all modules
* Change <em class="title-reference">netbox\_contact\.contact\_group</em> to <em class="title-reference">contact\_groups</em>
* Fix ansible\-bad\-import\-from pylint errors
* Fix broken code path when using old api path on old netbox systems
* Make the unit\-test data structures more flexible\.
* Remove abandoned unit\-test data\.
* add workaround to \_build\_query\_params for services and Netbox 4\.3\.0 \- 4\.4\.3 \(wrong parent\_object\_type data type\)
* add yamllint to project pipeline\.
* improve version\_check\_greater to be more universal
* netbox\_circuit\_termination \- Add parameters termination\_id and termination\_type for NetBox 4\.2\+
* netbox\_tag \- Add support for object\_types on tags
* rename variable full\_version to netbox\_version\.
* rename variable version to api\_version\.
* sanitize netbox versions received from api
* test suite expanded to run on Python 3\.11\, 3\.12\, and 3\.13\.
* user\.groups\, user\.permissions\, user\_group\.permissions\, permission\.actions\, and permission\.object\_types are now treated as unordered sets for update comparison purposes\.

<a id="ovirt-ovirt"></a>
#### ovirt\.ovirt

* Fix linting issues <em class="title-reference">\(can only concatenate list \(not \"UndefinedMarker\"\) to list\)</em> \([https\://github\.com/oVirt/ovirt\-ansible\-collection/pull/771](https\://github\.com/oVirt/ovirt\-ansible\-collection/pull/771)\)
* Remove product type in engine\_setup role as Red Hat Virtualization is no longer supported \([https\://github\.com/oVirt/ovirt\-ansible\-collection/pull/779](https\://github\.com/oVirt/ovirt\-ansible\-collection/pull/779)\)
* Rework hosted\_engine\_setup to support new ovirt\-engine\-appliance\(s\) built with kiwi  \([https\://github\.com/oVirt/ovirt\-ansible\-collection/pull/778](https\://github\.com/oVirt/ovirt\-ansible\-collection/pull/778)\)

<a id="theforeman-foreman-4"></a>
#### theforeman\.foreman

* activation\_key \- add <code>content\_view\_environments</code> parameter to support multi CV \([https\://github\.com/theforeman/foreman\-ansible\-modules/pull/1935](https\://github\.com/theforeman/foreman\-ansible\-modules/pull/1935)\)
* job\_invocation \- add <code>feature</code> parameter \([https\://github\.com/theforeman/foreman\-ansible\-modules/pull/1923](https\://github\.com/theforeman/foreman\-ansible\-modules/pull/1923)\)

<a id="vmware-vmware-2"></a>
#### vmware\.vmware

* Add module vm\_snapshot\_revert to revert a virtual machine to a snapshot\. Fixes [https\://github\.com/ansible\-collections/vmware\.vmware/issues/281](https\://github\.com/ansible\-collections/vmware\.vmware/issues/281)

<a id="deprecated-features-3"></a>
### Deprecated Features

* The <code>netapp\.cloudmanager</code> collection is considered unmaintained and will be removed from Ansible 15 if no one starts maintaining it again before Ansible 15\.
  See [Collections Removal Process for unmaintained collections](https\://docs\.ansible\.com/projects/ansible/devel/community/collection\_contributors/collection\_package\_removal\.html\#unmaintained\-collections) for more details\, including for how this can be cancelled \([https\://forum\.ansible\.com/t/44891](https\://forum\.ansible\.com/t/44891)\)\.
  After removal\, users can still install this collection with <code>ansible\-galaxy collection install netapp\.cloudmanager</code>\.

<a id="amazon-aws-4"></a>
#### amazon\.aws

* ec2\_vpc\_dhcp\_option \- the <code>dhcp\_config</code> return value has been deprecated and will be removed in a release after 2026\-12\-01\. Use <code>dhcp\_options</code> instead \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2772](https\://github\.com/ansible\-collections/amazon\.aws/pull/2772)\)\.
* ec2\_vpc\_dhcp\_option\_info \- the <code>dhcp\_config</code> return value has been deprecated and will be removed in a release after 2026\-12\-01\. Use <code>dhcp\_options</code> instead \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2772](https\://github\.com/ansible\-collections/amazon\.aws/pull/2772)\)\.
* route53 \- the <code>values</code> key in the <code>resource\_record\_sets</code> return value has been deprecated in favor of <code>record\_values</code> for Jinja2 compatibility\. The <code>values</code> key will be removed in a release after 2026\-12\-01 \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2772](https\://github\.com/ansible\-collections/amazon\.aws/pull/2772)\)\.

<a id="hetzner-hcloud-2"></a>
#### hetzner\.hcloud

* hcloud inventory \- The <code>hcloud\_datacenter</code> host variable is deprecated and will be removed after 1 July 2026\. Please use the <code>hcloud\_location</code> host variable instead\.
* network\_info \- The <code>hcloud\_network\_info\[\]\.servers\[\]\.datacenter</code> return value is deprecated and will be removed after 1 July 2026\. Please use the <code>hcloud\_network\_info\[\]\.servers\[\]\.location</code> return value instead\.
* primary\_ip \- The <code>datacenter</code> argument is deprecated and will be removed after 1 July 2026\. Please use the <code>location</code> argument instead\.
* primary\_ip \- The <code>hcloud\_primary\_ip\.datacenter</code> return value is deprecated and will be removed after 1 July 2026\. Please use the <code>hcloud\_primary\_ip\.location</code> return value instead\.
* primary\_ip\_info \- The <code>hcloud\_primary\_ip\_info\[\]\.datacenter</code> return value is deprecated and will be removed after 1 July 2026\. Please use the <code>hcloud\_primary\_ip\_info\[\]\.location</code> return value instead\.
* server \- The <code>datacenter</code> argument is deprecated and will be removed after 1 July 2026\. Please use the <code>location</code> argument instead\.
* server \- The <code>hcloud\_server\.datacenter</code> return value is deprecated and will be removed after 1 July 2026\. Please use the <code>hcloud\_server\.location</code> return value instead\.
* server\_info \- The <code>hcloud\_server\_info\[\]\.datacenter</code> return value is deprecated and will be removed after 1 July 2026\. Please use the <code>hcloud\_server\_info\[\]\.location</code> return value instead\.

<a id="bugfixes-3"></a>
### Bugfixes

<a id="ansible-core-11"></a>
#### Ansible\-core

* Fix Windows LIB env var corruption \([https\://github\.com/ansible\-collections/ansible\.windows/issues/297](https\://github\.com/ansible\-collections/ansible\.windows/issues/297)\)\.
* <code>ansible</code>\, <code>ansible\-console</code> \- fix executing <code>\- meta\: end\_play</code> tasks\.
* ansible\-test \- Upgrade <code>expat</code> during provisioning of Fedora 42 remote instances\.
* ansible\_local will no longer trigger variable injection default value deprecation\.
* copy \- when a single\-file local directory was specified as the source\, <code>changed</code> used to be <code>false</code> even when the source was actually copied\. It now makes sure <code>changed</code> is <code>true</code> in this case\. \([https\://github\.com/ansible/ansible/issues/85833](https\://github\.com/ansible/ansible/issues/85833)\)
* deb822\_repository \- Remove <code>Install\-Python\-Debian</code> from files outputed by the <code>deb822\_repository</code> module \([https\://github\.com/ansible/ansible/issues/86395](https\://github\.com/ansible/ansible/issues/86395)\)
* dnf \- When installing a dnf module\, install and enable when missing\, upgrade when present \([https\://github\.com/ansible/ansible/issues/73457](https\://github\.com/ansible/ansible/issues/73457)\)
* dnf \- fix package installation when specifying architecture without version \(e\.g\.\, <code>libgcc\.i686</code>\) where a different architecture of the same package is already installed \([https\://github\.com/ansible/ansible/issues/86156](https\://github\.com/ansible/ansible/issues/86156)\)\.
* package\, service\, gather\_facts \- fix templating module\_defaults for modules executed by these action plugins\. \([https\://github\.com/ansible/ansible/issues/85848](https\://github\.com/ansible/ansible/issues/85848)\)
* winrm \- Provide a better error message if a domain user is specified using a User Principal Name \(<code>UPN</code>\) but the <code>pykerberos</code> library is not installed so Kerberos is unavailable\.

<a id="amazon-aws-5"></a>
#### amazon\.aws

* connection/aws\_ssm \- fixed ReferenceError in aws\_ssm connection plugin destructor during interpreter shutdown \([https\://github\.com/ansible\-collections/amazon\.aws/issues/2728](https\://github\.com/ansible\-collections/amazon\.aws/issues/2728)\)\.
* lambda\_info \- fixed invalid return value documentation that used dot notation \(<code>function\.TheName</code>\) which cannot be used in Jinja2 templates \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2772](https\://github\.com/ansible\-collections/amazon\.aws/pull/2772)\)\.
* s3\_bucket \- fix error when configuring AES256 bucket encryption with <code>bucket\_key\_enabled</code> explicitly set to <code>false</code> \([https\://github\.com/ansible\-collections/amazon\.aws/issues/2734](https\://github\.com/ansible\-collections/amazon\.aws/issues/2734)\)\.

<a id="ansible-netcommon-4"></a>
#### ansible\.netcommon

* Adds backward compatibility of handling src attributes\, functional consistency with ansible\-core \>\= 2\.19
* Adds deprecation warning for the jinja2 processing functionality for src attributes\, src attributes in collections would still support considering file path but they would not process template files directly once the functionality is deprecated\.
* It is suggested to use ansible\.builtin\.template module to process templates and use the processed template path in src attributes\.

<a id="ansible-utils-1"></a>
#### ansible\.utils

* Add a cleanup step that removes empty \{\} and \[\] values from lists in keep\_keys\_from\_dict\_n\_list\(\)

<a id="cisco-nxos"></a>
#### cisco\.nxos

* Fixed nxos\_facts module so it can handle VLAN interface facts without any issue even if addr is not defined
* Fixed nxos\_static\_routes module so to handle replaced and overridden state with vrf configuration\.
* cisco\.nxos\.nxos\_facts \- Fix AttributeError when interface has multiple IPv6 addrs and handle ROW\_addr as list\.

<a id="community-dns-4"></a>
#### community\.dns

* Update Public Suffix List\.
* converter module utils \- add <code>stacklevel\=2</code> to Python warnings\. This affects third\-party users of the module utils outside this collection \([https\://github\.com/ansible\-collections/community\.dns/pull/310](https\://github\.com/ansible\-collections/community\.dns/pull/310)\)\.
* hetzner\_dns\_record\_set\, hosttech\_dns\_record\_set \- fix <code>on\_existing \!\= \'replace\'</code> mis\-triggering when <code>state\=absent</code> and the values to delete do not show up in the list of records \([https\://github\.com/ansible\-collections/community\.dns/pull/301](https\://github\.com/ansible\-collections/community\.dns/pull/301)\)\.
* hosttech\_record\_sets\, hetzner\_record\_sets \- ensure stable order also with Python \< 3\.6 \([https\://github\.com/ansible\-collections/community\.dns/pull/301](https\://github\.com/ansible\-collections/community\.dns/pull/301)\)\.
* lookup\_rfc8427 lookup plugin \- remove unused code \([https\://github\.com/ansible\-collections/community\.dns/pull/308](https\://github\.com/ansible\-collections/community\.dns/pull/308)\)\.
* remove\_public\_suffix filter plugin \- fix plugin name in error message \([https\://github\.com/ansible\-collections/community\.dns/pull/308](https\://github\.com/ansible\-collections/community\.dns/pull/308)\)\.
* remove\_registrable\_domain filter plugin \- fix plugin name in error message \([https\://github\.com/ansible\-collections/community\.dns/pull/308](https\://github\.com/ansible\-collections/community\.dns/pull/308)\)\.

<a id="community-docker-3"></a>
#### community\.docker

* modules and plugins using the Docker SDK for Python \- do not automatically set <code>tls\_hostname</code> when <code>validate\_certs\=true</code> for Docker SDK for Python 7\.0\.0\+ \([https\://github\.com/ansible\-collections/community\.docker/issues/1225](https\://github\.com/ansible\-collections/community\.docker/issues/1225)\, [https\://github\.com/ansible\-collections/community\.docker/pull/1226](https\://github\.com/ansible\-collections/community\.docker/pull/1226)\)\.

<a id="community-general-11"></a>
#### community\.general

* cloudflare\_dns \- also allow <code>flag\=128</code> for CAA records \([https\://github\.com/ansible\-collections/community\.general/issues/11355](https\://github\.com/ansible\-collections/community\.general/issues/11355)\, [https\://github\.com/ansible\-collections/community\.general/pull/11377](https\://github\.com/ansible\-collections/community\.general/pull/11377)\)\.
* gem \- add compatibility with Ruby 4 rubygems \([https\://github\.com/ansible\-collections/community\.general/issues/11397](https\://github\.com/ansible\-collections/community\.general/issues/11397)\, [https\://github\.com/ansible\-collections/community\.general/pull/11442](https\://github\.com/ansible\-collections/community\.general/pull/11442)\)\.
* incus connection plugin \- fix parsing of commands for Windows\, enforcing a <code>\\</code> after the drive letter and colon symbol \([https\://github\.com/ansible\-collections/community\.general/pull/11347](https\://github\.com/ansible\-collections/community\.general/pull/11347)\)\.
* keycloak\_client \- fix idempotency bug caused by <code>null</code> client attribute value differences for non\-existing client attributes \([https\://github\.com/ansible\-collections/community\.general/issues/11443](https\://github\.com/ansible\-collections/community\.general/issues/11443)\, [https\://github\.com/ansible\-collections/community\.general/pull/11444](https\://github\.com/ansible\-collections/community\.general/pull/11444)\)\.
* logstash\_plugin \- fix argument order when using <code>version</code> parameter\. The plugin name must come after options like <code>\-\-version</code> for the <code>logstash\-plugin</code> CLI to work correctly \([https\://github\.com/ansible\-collections/community\.general/issues/10745](https\://github\.com/ansible\-collections/community\.general/issues/10745)\, [https\://github\.com/ansible\-collections/community\.general/pull/11440](https\://github\.com/ansible\-collections/community\.general/pull/11440)\)\.
* pmem \- fix test for invalid data input \([https\://github\.com/ansible\-collections/community\.general/pull/11388](https\://github\.com/ansible\-collections/community\.general/pull/11388)\)\.

<a id="community-vmware-1"></a>
#### community\.vmware

* vmware\_guest\_storage\_policy \- Fix storage policy search to return None if no policies are found\, instead of causing an exception\. fixes [https\://github\.com/ansible\-collections/community\.vmware/issues/2527](https\://github\.com/ansible\-collections/community\.vmware/issues/2527)

<a id="containers-podman-8"></a>
#### containers\.podman

* Fix idempotency for tagging local images
* Fix image idempotency in pull
* Fix issue with \-\-rm and service in Quadlet
* fix\(podman\_prune\) set top\-level changed status

<a id="google-cloud-3"></a>
#### google\.cloud

* connection plugin \- fix attribute error when using reset\_connection \([https\://github\.com/ansible\-collections/google\.cloud/issues/737](https\://github\.com/ansible\-collections/google\.cloud/issues/737)\)\.
* connection plugin \- fix ssh error in tasks with loops \([https\://github\.com/ansible\-collections/google\.cloud/issues/738](https\://github\.com/ansible\-collections/google\.cloud/issues/738)\)\.

<a id="hetzner-hcloud-3"></a>
#### hetzner\.hcloud

* Invalid redirects for Storage Box modules are now fixed by using fully qualified module names\.

<a id="infoblox-nios-modules-1"></a>
#### infoblox\.nios\_modules

* Fixed sanity and unit test execution in CI pipeline
* Fixed transform functions to handle <code>None</code> parameters and apply default values correctly

<a id="netbox-netbox-1"></a>
#### netbox\.netbox

* Add netbox version check to support service creation for netbox version prior of 4\.3
* Fix integration test for circuit termination\, missing assignment
* Fix integration test for service
* Fix task duplicate task name in documentation that cause ansible\-lint error
* Fix typos in tag integration tests\.
* Support for related\_object\_filter when related\_object\_type is \"object\"
* Use dedicated function to check netbox version istead of self\.full\_version for rack\.
* add parent\_object\_type and parent\_object\_id to services ALLOWED\_QUERY\_PARAMS
* nb\_device\_interface\: Fix specifying primary\_mac\_address objects by id for disambiguation
* nb\_inventory \- Fix service collection for version greater than 4\.3
* nb\_inventory \- Fixed empty inventory results when netbox server URL is a non\-root path
* netbox\_service \- Fix issue 1426 \- broken netbox\_service module

<a id="ovirt-ovirt-1"></a>
#### ovirt\.ovirt

* Fix missing cluster name when starting VM \([https\://github\.com/oVirt/ovirt\-ansible\-collection/pull/780](https\://github\.com/oVirt/ovirt\-ansible\-collection/pull/780)\)

<a id="purestorage-flashblade"></a>
#### purestorage\.flashblade

* purefb\_ad \- Ensure encryption algorithms used match the GUI values
* purefb\_certs \- Fix the syntax to generate a CSR
* purefb\_ds \- Fixed issue when creating pre\-enabled management directory service

<a id="vmware-vmware-3"></a>
#### vmware\.vmware

* deploy\_folder\_template \- Fixed issue where the vm folder was being cached in the placement service\, causing the module to skip the template folder lookup and fail\. Fixes [https\://github\.com/ansible\-collections/vmware\.vmware/issues/292](https\://github\.com/ansible\-collections/vmware\.vmware/issues/292)
* import\_content\_library\_ovf \- Fixed issue where OVFs with \.nvram files failed to import Fixes [https\://github\.com/ansible\-collections/vmware\.vmware/issues/257](https\://github\.com/ansible\-collections/vmware\.vmware/issues/257)
* vm \- Fixed issue where error handling failed when state is absent
* vm \- Remove check that prevents memory from being decreased regardless of power state\. Fixes [https\://github\.com/ansible\-collections/vmware\.vmware/issues/298](https\://github\.com/ansible\-collections/vmware\.vmware/issues/298)
* vm\_apply\_customization \- Fixed issue where the product ID\, user name\, and user org name were required by the API but not by the module

<a id="new-plugins-2"></a>
### New Plugins

<a id="filter-1"></a>
#### Filter

* community\.general\.to\_toml \- Convert variable to TOML string\.

<a id="new-modules-3"></a>
### New Modules

<a id="ibm-storage-virtualize-3"></a>
#### ibm\.storage\_virtualize

* ibm\.storage\_virtualize\.ibm\_sv\_manage\_clone \- This module manages clone and thinclone of volume and volumegroup\.

<a id="netbox-netbox-2"></a>
#### netbox\.netbox

* netbox\.netbox\.netbox\_contact\_assignment \- Manage contact assignments in NetBox
* netbox\.netbox\.netbox\_data\_source \- Manage data sources in NetBox

<a id="unchanged-collections-3"></a>
### Unchanged Collections

* ansible\.posix \(still version 2\.1\.0\)
* ansible\.windows \(still version 3\.3\.0\)
* arista\.eos \(still version 12\.0\.0\)
* awx\.awx \(still version 24\.6\.1\)
* check\_point\.mgmt \(still version 6\.8\.0\)
* chocolatey\.chocolatey \(still version 1\.5\.3\)
* cisco\.aci \(still version 2\.13\.0\)
* cisco\.intersight \(still version 2\.12\.0\)
* cisco\.ios \(still version 11\.2\.0\)
* cisco\.iosxr \(still version 12\.1\.1\)
* cisco\.mso \(still version 2\.12\.0\)
* cisco\.ucs \(still version 1\.16\.0\)
* community\.aws \(still version 10\.0\.0\)
* community\.ciscosmb \(still version 1\.0\.11\)
* community\.crypto \(still version 3\.1\.0\)
* community\.grafana \(still version 2\.3\.0\)
* community\.hashi\_vault \(still version 7\.1\.0\)
* community\.hrobot \(still version 2\.7\.0\)
* community\.library\_inventory\_filtering\_v1 \(still version 1\.1\.5\)
* community\.libvirt \(still version 2\.0\.0\)
* community\.mysql \(still version 4\.0\.1\)
* community\.okd \(still version 5\.0\.0\)
* community\.postgresql \(still version 4\.2\.0\)
* community\.proxmox \(still version 1\.5\.0\)
* community\.proxysql \(still version 1\.7\.0\)
* community\.rabbitmq \(still version 1\.6\.0\)
* community\.sap\_libs \(still version 1\.6\.0\)
* community\.sops \(still version 2\.2\.7\)
* community\.windows \(still version 3\.1\.0\)
* community\.zabbix \(still version 4\.1\.1\)
* cyberark\.conjur \(still version 1\.3\.9\)
* cyberark\.pas \(still version 1\.0\.36\)
* dellemc\.enterprise\_sonic \(still version 3\.2\.0\)
* dellemc\.openmanage \(still version 10\.0\.1\)
* dellemc\.powerflex \(still version 3\.0\.0\)
* dellemc\.unity \(still version 2\.1\.0\)
* f5networks\.f5\_modules \(still version 1\.39\.0\)
* fortinet\.fortimanager \(still version 2\.12\.0\)
* fortinet\.fortios \(still version 2\.4\.2\)
* grafana\.grafana \(still version 6\.0\.6\)
* hitachivantara\.vspone\_block \(still version 4\.5\.1\)
* hitachivantara\.vspone\_object \(still version 1\.1\.1\)
* ieisystem\.inmanage \(still version 4\.0\.0\)
* infinidat\.infinibox \(still version 1\.6\.3\)
* inspur\.ispim \(still version 2\.2\.4\)
* junipernetworks\.junos \(still version 11\.0\.0\)
* kaytus\.ksmanage \(still version 2\.0\.0\)
* kubernetes\.core \(still version 6\.2\.0\)
* kubevirt\.core \(still version 2\.2\.3\)
* lowlydba\.sqlserver \(still version 2\.7\.0\)
* microsoft\.ad \(still version 1\.10\.0\)
* microsoft\.iis \(still version 1\.1\.0\)
* netapp\.cloudmanager \(still version 21\.24\.0\)
* netapp\.ontap \(still version 23\.3\.0\)
* netapp\.storagegrid \(still version 21\.16\.0\)
* netapp\_eseries\.santricity \(still version 1\.4\.1\)
* ngine\_io\.cloudstack \(still version 3\.0\.0\)
* openstack\.cloud \(still version 2\.5\.0\)
* purestorage\.flasharray \(still version 1\.41\.0\)
* ravendb\.ravendb \(still version 1\.0\.4\)
* splunk\.es \(still version 4\.0\.0\)
* vmware\.vmware\_rest \(still version 4\.9\.0\)
* vultr\.cloud \(still version 1\.13\.0\)
* vyos\.vyos \(still version 6\.0\.0\)
* wti\.remote \(still version 1\.0\.10\)

<a id="v13-2-0"></a>
## v13\.2\.0

- <a href="#release-summary-4">Release Summary</a>
- <a href="#ansible-core-12">Ansible\-core</a>
- <a href="#changed-collections-4">Changed Collections</a>
- <a href="#major-changes-4">Major Changes</a>
    - <a href="#netapp-ontap-4">netapp\.ontap</a>
- <a href="#minor-changes-4">Minor Changes</a>
    - <a href="#cisco-ios-3">cisco\.ios</a>
    - <a href="#community-crypto-3">community\.crypto</a>
    - <a href="#community-general-12">community\.general</a>
    - <a href="#community-proxmox-6">community\.proxmox</a>
    - <a href="#community-routeros-7">community\.routeros</a>
    - <a href="#community-sap-libs-1">community\.sap\_libs</a>
    - <a href="#fortinet-fortimanager-2">fortinet\.fortimanager</a>
    - <a href="#hetzner-hcloud-4">hetzner\.hcloud</a>
    - <a href="#netapp-ontap-5">netapp\.ontap</a>
    - <a href="#netapp-storagegrid">netapp\.storagegrid</a>
    - <a href="#purestorage-flashblade-1">purestorage\.flashblade</a>
- <a href="#deprecated-features-4">Deprecated Features</a>
    - <a href="#community-general-13">community\.general</a>
    - <a href="#community-routeros-8">community\.routeros</a>
- <a href="#bugfixes-4">Bugfixes</a>
    - <a href="#cisco-ios-4">cisco\.ios</a>
    - <a href="#cisco-iosxr-2">cisco\.iosxr</a>
    - <a href="#cisco-nxos-1">cisco\.nxos</a>
    - <a href="#community-dns-5">community\.dns</a>
    - <a href="#community-general-14">community\.general</a>
    - <a href="#community-proxmox-7">community\.proxmox</a>
    - <a href="#fortinet-fortimanager-3">fortinet\.fortimanager</a>
    - <a href="#hitachivantara-vspone-block-2">hitachivantara\.vspone\_block</a>
    - <a href="#netapp-ontap-6">netapp\.ontap</a>
    - <a href="#netapp-storagegrid-1">netapp\.storagegrid</a>
    - <a href="#purestorage-flasharray-1">purestorage\.flasharray</a>
    - <a href="#purestorage-flashblade-2">purestorage\.flashblade</a>
- <a href="#new-modules-4">New Modules</a>
    - <a href="#community-general-15">community\.general</a>
    - <a href="#community-proxmox-8">community\.proxmox</a>
    - <a href="#fortinet-fortimanager-4">fortinet\.fortimanager</a>
    - <a href="#netapp-storagegrid-2">netapp\.storagegrid</a>
- <a href="#unchanged-collections-4">Unchanged Collections</a>

<a id="release-summary-4"></a>
### Release Summary

Release Date\: 2025\-12\-30

[Porting Guide](https\://docs\.ansible\.com/projects/ansible/devel/porting\_guides\.html)

<a id="ansible-core-12"></a>
### Ansible\-core

Ansible 13\.2\.0 contains ansible\-core version 2\.20\.1\.
This is the same version of ansible\-core as in the previous Ansible release\.

<a id="changed-collections-4"></a>
### Changed Collections

If not mentioned explicitly\, the changes are reported in the combined changelog below\.

| Collection                  | Ansible 13.1.0 | Ansible 13.2.0 | Notes                                                    |
| --------------------------- | -------------- | -------------- | -------------------------------------------------------- |
| check_point.mgmt            | 6.7.0          | 6.8.0          | The collection did not have a changelog in this version. |
| cisco.ios                   | 11.1.1         | 11.2.0         |                                                          |
| cisco.iosxr                 | 12.1.0         | 12.1.1         |                                                          |
| cisco.nxos                  | 11.1.0         | 11.1.1         |                                                          |
| community.crypto            | 3.0.5          | 3.1.0          |                                                          |
| community.dns               | 3.4.1          | 3.4.2          |                                                          |
| community.general           | 12.1.0         | 12.2.0         |                                                          |
| community.proxmox           | 1.4.0          | 1.5.0          |                                                          |
| community.routeros          | 3.14.0         | 3.15.0         |                                                          |
| community.sap_libs          | 1.5.0          | 1.6.0          |                                                          |
| fortinet.fortimanager       | 2.11.0         | 2.12.0         |                                                          |
| hetzner.hcloud              | 6.2.1          | 6.3.0          |                                                          |
| hitachivantara.vspone_block | 4.5.0          | 4.5.1          |                                                          |
| netapp.ontap                | 23.2.0         | 23.3.0         |                                                          |
| netapp.storagegrid          | 21.15.0        | 21.16.0        |                                                          |
| purestorage.flasharray      | 1.40.0         | 1.41.0         |                                                          |
| purestorage.flashblade      | 1.22.0         | 1.23.1         |                                                          |

<a id="major-changes-4"></a>
### Major Changes

<a id="netapp-ontap-4"></a>
#### netapp\.ontap

* na\_ontap\_interface \- AWS Lambda support added to the module\.
* na\_ontap\_lun \- AWS Lambda support added to the module\.
* na\_ontap\_snapshot \- AWS Lambda support added to the module\.
* na\_ontap\_svm \- AWS Lambda support added to the module\.

<a id="minor-changes-4"></a>
### Minor Changes

<a id="cisco-ios-3"></a>
#### cisco\.ios

* ios\_l2\_interfaces \- Added xconnect and encapsulation attributes for L2VPN pseudowire and MPLS services configuration\.

<a id="community-crypto-3"></a>
#### community\.crypto

* luks\_device \- add support for TPM2 enrollment using <code>systemd\-cryptsetup</code> \([https\://github\.com/ansible\-collections/community\.crypto/issues/850](https\://github\.com/ansible\-collections/community\.crypto/issues/850)\, [https\://github\.com/ansible\-collections/community\.crypto/pull/972](https\://github\.com/ansible\-collections/community\.crypto/pull/972)\)\.
* luks\_device \- add support for keyslot priority \([https\://github\.com/ansible\-collections/community\.crypto/issues/850](https\://github\.com/ansible\-collections/community\.crypto/issues/850)\, [https\://github\.com/ansible\-collections/community\.crypto/pull/972](https\://github\.com/ansible\-collections/community\.crypto/pull/972)\)\.

<a id="community-general-12"></a>
#### community\.general

* btrfs module utils \- make execution of external commands safer by passing arguments as list \([https\://github\.com/ansible\-collections/community\.general/pull/11240](https\://github\.com/ansible\-collections/community\.general/pull/11240)\)\.
* deps module utils \- change the internal representaion of dependency state \([https\://github\.com/ansible\-collections/community\.general/pull/11242](https\://github\.com/ansible\-collections/community\.general/pull/11242)\)\.
* keycloak\_userprofile \- add support for <code>selector</code> option \([https\://github\.com/ansible\-collections/community\.general/pull/11309](https\://github\.com/ansible\-collections/community\.general/pull/11309)\)\.
* keycloak\_userprofile \- add support for additional user profile attribute\-validations available in Keycloak \([https\://github\.com/ansible\-collections/community\.general/issues/9048](https\://github\.com/ansible\-collections/community\.general/issues/9048)\, [https\://github\.com/ansible\-collections/community\.general/pull/11285](https\://github\.com/ansible\-collections/community\.general/pull/11285)\)\.
* lxc\_container \- refactor function <code>create\_script</code>\, using <code>subprocess\.Popen\(\)</code>\, to a new module\_utils <code>\_lxc</code> \([https\://github\.com/ansible\-collections/community\.general/pull/11204](https\://github\.com/ansible\-collections/community\.general/pull/11204)\)\.
* lxc\_container \- use <code>tempfile\.TemporaryDirectory\(\)</code> instead of <code>mkdtemp\(\)</code> \([https\://github\.com/ansible\-collections/community\.general/pull/11323](https\://github\.com/ansible\-collections/community\.general/pull/11323)\)\.
* monit \- add <code>monit\_version</code> return value also when the module has succeeded \([https\://github\.com/ansible\-collections/community\.general/pull/11255](https\://github\.com/ansible\-collections/community\.general/pull/11255)\)\.
* monit \- use <code>Enum</code> to represent the possible states \([https\://github\.com/ansible\-collections/community\.general/pull/11245](https\://github\.com/ansible\-collections/community\.general/pull/11245)\)\.
* nmcli module \- add <code>vxlan\_parent</code> option required for multicast <code>vxlan\_remote</code> addresses\; add <code>vxlan</code> to list of bridgeable devices \([https\://github\.com/ansible\-collections/community\.general/pull/11182](https\://github\.com/ansible\-collections/community\.general/pull/11182)\)\.
* scaleway inventory plugin \- added support for <code>SCW\_PROFILE</code> environment variable for the <code>scw\_profile</code> option \([https\://github\.com/ansible\-collections/community\.general/issues/11310](https\://github\.com/ansible\-collections/community\.general/issues/11310)\, [https\://github\.com/ansible\-collections/community\.general/pull/11311](https\://github\.com/ansible\-collections/community\.general/pull/11311)\)\.
* scaleway module utils \- added <code>scw\_profile</code> parameter with <code>SCW\_PROFILE</code> environment variable support \([https\://github\.com/ansible\-collections/community\.general/issues/11313](https\://github\.com/ansible\-collections/community\.general/issues/11313)\, [https\://github\.com/ansible\-collections/community\.general/pull/11314](https\://github\.com/ansible\-collections/community\.general/pull/11314)\)\.

<a id="community-proxmox-6"></a>
#### community\.proxmox

* inventory plugin\, plugin\_utils \- replace deprecated <code>ansible\.module\_utils\.common\.\_collections\_compat</code> imports with <code>collections\.abc</code> from the Python standard library \([https\://github\.com/ansible\-collections/community\.proxmox/issues/241](https\://github\.com/ansible\-collections/community\.proxmox/issues/241)\)\.
* proxmox \- change disk size units to GiB \([https\://github\.com/ansible\-collections/community\.proxmox/pull/236](https\://github\.com/ansible\-collections/community\.proxmox/pull/236)\)\.
* proxmox\_disk \- change disk size units to GiB \([https\://github\.com/ansible\-collections/community\.proxmox/pull/236](https\://github\.com/ansible\-collections/community\.proxmox/pull/236)\)\.
* proxmox\_kvm \- add option to migrate local disks as well \([https\://github\.com/ansible\-collections/community\.proxmox/pull/240](https\://github\.com/ansible\-collections/community\.proxmox/pull/240)\)\.
* proxmox\_kvm \- change disk size units to GiB \([https\://github\.com/ansible\-collections/community\.proxmox/pull/236](https\://github\.com/ansible\-collections/community\.proxmox/pull/236)\)\.
* proxmox\_node\_info \- add information on node network interfaces to node information output \([https\://github\.com/ansible\-collections/community\.proxmox/pull/220](https\://github\.com/ansible\-collections/community\.proxmox/pull/220)\)\.
* proxmox\_node\_info \- add information on node\'s PVE version \([https\://github\.com/ansible\-collections/community\.proxmox/pull/225](https\://github\.com/ansible\-collections/community\.proxmox/pull/225)\)\.
* proxmox\_snap\_info \- Adds a new module to list snapshots or a specific snapshot for VM or container \([https\://github\.com/ansible\-collections/community\.proxmox/issues/229](https\://github\.com/ansible\-collections/community\.proxmox/issues/229)\)\.
* proxmox\_storage \- add feature of subdirectory in CIFS share\. \([https\://github\.com/ansible\-collections/community\.proxmox/pull/214](https\://github\.com/ansible\-collections/community\.proxmox/pull/214)\)\.
* proxmox\_storage \- fix passing nfs\_options to API payload \([https\://github\.com/ansible\-collections/community\.proxmox/issues/203](https\://github\.com/ansible\-collections/community\.proxmox/issues/203)\, [https\://github\.com/ansible\-collections/community\.proxmox/pull/221](https\://github\.com/ansible\-collections/community\.proxmox/pull/221)\)\.
* proxmox\_storage \- fixed CIFS authentication by sending username and password parameters to proxmoxer \([https\://github\.com/ansible\-collections/community\.proxmox/pull/214](https\://github\.com/ansible\-collections/community\.proxmox/pull/214)\)\.

<a id="community-routeros-7"></a>
#### community\.routeros

* api\_info\, api\_modify \- add <code>2g\-probe\-delay</code> field to path <code>interface wifi steering</code> \([https\://github\.com/ansible\-collections/community\.routeros/pull/428](https\://github\.com/ansible\-collections/community\.routeros/pull/428)\)\.
* api\_info\, api\_modify \- add <code>aaa\.\*</code>\, <code>channel\.\*</code>\, <code>datapath\.\*</code>\, <code>interworking\.\*</code>\, <code>security\.\*</code>\, <code>steering\.\*</code> sub\-fields to path <code>interface wifi configuration</code> \([https\://github\.com/ansible\-collections/community\.routeros/pull/428](https\://github\.com/ansible\-collections/community\.routeros/pull/428)\)\.
* api\_info\, api\_modify \- add <code>deprioritize\-unii\-3\-4</code>\, <code>reselect\-interval</code>\, <code>reselect\-time</code> fields to path <code>interface wifi channel</code> \([https\://github\.com/ansible\-collections/community\.routeros/pull/428](https\://github\.com/ansible\-collections/community\.routeros/pull/428)\)\.
* api\_info\, api\_modify \- add <code>multi\-passphrase\-group</code> field to path <code>interface wifi security</code> \([https\://github\.com/ansible\-collections/community\.routeros/pull/428](https\://github\.com/ansible\-collections/community\.routeros/pull/428)\)\.
* api\_info\, api\_modify \- add <code>send\-email\-from</code>\, <code>send\-email\-to</code> and <code>send\-smtp\-server</code> to <code>system watchdog</code> \([https\://github\.com/ansible\-collections/community\.routeros/pull/429](https\://github\.com/ansible\-collections/community\.routeros/pull/429)\)\.
* api\_info\, api\_modify \- add <code>traffic\-processing</code> field to path <code>interface wifi datapath</code> and <code>interface wifi configuration</code> \([https\://github\.com/ansible\-collections/community\.routeros/pull/424](https\://github\.com/ansible\-collections/community\.routeros/pull/424)\)\.
* api\_info\, api\_modify \- add <code>use\-bfd</code> to <code>routing ospf interface\-template</code> path \([https\://github\.com/ansible\-collections/community\.routeros/pull/425](https\://github\.com/ansible\-collections/community\.routeros/pull/425)\)\.
* api\_info\, api\_modify \- add <code>vrf</code> to <code>ip service</code> \([https\://github\.com/ansible\-collections/community\.routeros/pull/426](https\://github\.com/ansible\-collections/community\.routeros/pull/426)\)\.
* api\_info\, api\_modify \- add missing parameters to path <code>interface bridge</code> and <code>interface bridge port</code> \([https\://github\.com/ansible\-collections/community\.routeros/pull/423](https\://github\.com/ansible\-collections/community\.routeros/pull/423)\)\.
* api\_info\, api\_modify \- add support for path <code>disk settings</code> \([https\://github\.com/ansible\-collections/community\.routeros/pull/422](https\://github\.com/ansible\-collections/community\.routeros/pull/422)\)\.

<a id="community-sap-libs-1"></a>
#### community\.sap\_libs

* sap\_control\_exec \- Add local socket support \([https\://github\.com/sap\-linuxlab/community\.sap\_libs/pull/66](https\://github\.com/sap\-linuxlab/community\.sap\_libs/pull/66)\)
* sap\_hostctrl\_exec \- Add new module and tests \([https\://github\.com/sap\-linuxlab/community\.sap\_libs/pull/67](https\://github\.com/sap\-linuxlab/community\.sap\_libs/pull/67)\)

<a id="fortinet-fortimanager-2"></a>
#### fortinet\.fortimanager

* Supported new modules to configure FortiProxy\.
* Supported new schemas in FortiManager 7\.0\.15\, 7\.4\.8\, 7\.6\.4\.

<a id="hetzner-hcloud-4"></a>
#### hetzner\.hcloud

* storage\_box \- New module to create and manage Storage Boxes in Hetzner\.
* storage\_box\_info \- New module to gather infos about Hetzner Storage Boxes\.
* storage\_box\_snapshot \- New module to create and manage Storage Box Snapshots in Hetzner\.
* storage\_box\_snapshot\_info \- New module to gather infos about Hetzner Storage Box Snapshots\.
* storage\_box\_subaccount \- New module to create and manage Storage Box Subaccounts in Hetzner\.
* storage\_box\_subaccount\_info \- New module to gather infos about Hetzner Storage Box Subaccounts\.
* storage\_box\_type\_info \- New module to gather infos about Hetzner Storage Box Types\.

<a id="netapp-ontap-5"></a>
#### netapp\.ontap

* na\_ontap\_ems\_filter \- new option <em class="title-reference">parameter\_criteria</em> added in REST\, requires ONTAP 9\.13\.1 or later\.
* na\_ontap\_net\_ifgrp \- Update <em class="title-reference">mode</em> parameter to specify allowed values\.

<a id="netapp-storagegrid"></a>
#### netapp\.storagegrid

* all modules \- add support for failure responses to include additional error details for easier troubleshooting\.
* na\_sg\_grid\_alert\_receiver \- new option <em class="title-reference">smtp\_username</em> and <em class="title-reference">smtp\_password</em> added in place of <em class="title-reference">username</em> and <em class="title-reference">password</em>\.
* na\_sg\_grid\_audit\_destination \- new option <em class="title-reference">access\_logs\_send</em>\, <em class="title-reference">access\_logs\_facility</em>\, and <em class="title-reference">access\_logs\_severity</em> added to manage access log settings for syslog server\.
* na\_sg\_grid\_gateway \- new option <em class="title-reference">closed\_on\_untrusted\_client\_network</em>\. Requires StorageGRID 11\.8 or later\.
* na\_sg\_grid\_gateway \- parameter <em class="title-reference">default\_service\_type</em> allows option for <em class="title-reference">management</em>\. Requires StorageGRID 11\.8 or later\.
* na\_sg\_grid\_group \- new option <em class="title-reference">manage\_alerts</em> and <em class="title-reference">storage\_admin</em> added to management policy\.
* na\_sg\_grid\_info \- Added new endpoints for the grid info\.
* na\_sg\_org\_bucket \- user input for <em class="title-reference">capacity\_limit</em> option changed from bytes to GB\.
* na\_sg\_org\_container \- Enhanced the bucket policy\.
* na\_sg\_org\_container \- user input for <em class="title-reference">capacity\_limit</em> option changed from bytes to GB\.
* na\_sg\_org\_group \- new options <em class="title-reference">s3\_console</em> to control S3 console access and <em class="title-reference">view\_all\_containers</em> to view settings for all buckets added\, requires StorageGRID version 11\.8 or later\.
* na\_sg\_org\_info \- Added new endpoints for the org info\.

<a id="purestorage-flashblade-1"></a>
#### purestorage\.flashblade

* purefa\_ad \- Added support for local servers using the <code>server</code> parameter\.
* purefb\_ad \- Added test and rotate states
* purefb\_ad \- Remove doc references to FQDNs as SPNs are the required method\.
* purefb\_ad \- Updated encryption algorithms to use correct values
* purefb\_ds \- Allow directory services to be modified for internal NFS servers
* purefb\_ds \- Update test state to allow specific tests to be run
* purefb\_info \- Added MAC address information for LAGs

<a id="deprecated-features-4"></a>
### Deprecated Features

<a id="community-general-13"></a>
#### community\.general

* All module utils\, plugin utils\, and doc fragments will be made <strong>private</strong> in community\.general 13\.0\.0\. This means that they will no longer be part of the public API of the collection\, and can have breaking changes even in bugfix releases\. If you depend on importing code from the module or plugin utils\, or use one of the doc fragments\, please [comment in the issue to discuss this](https\://github\.com/ansible\-collections/community\.general/issues/11312)\. Note that this does not affect any use of community\.general in task files\, roles\, or playbooks \([https\://github\.com/ansible\-collections/community\.general/issues/11312](https\://github\.com/ansible\-collections/community\.general/issues/11312)\, [https\://github\.com/ansible\-collections/community\.general/pull/11320](https\://github\.com/ansible\-collections/community\.general/pull/11320)\)\.

<a id="community-routeros-8"></a>
#### community\.routeros

* api\_find\_and\_modify \- the current defaults for <code>ignore\_dynamic</code> and <code>ignore\_builtin</code> \(both <code>false</code>\) have been deprecated and will change to <code>true</code> in community\.routeros 4\.0\.0\. To avoid deprecation messages\, please set the value explicitly to <code>true</code> or <code>false</code>\, if you have not already done so\. We recommend to set them to <code>true</code>\, unless you have a good reason to set them to <code>false</code> \([https\://github\.com/ansible\-collections/community\.routeros/pull/399](https\://github\.com/ansible\-collections/community\.routeros/pull/399)\)\.

<a id="bugfixes-4"></a>
### Bugfixes

<a id="cisco-ios-4"></a>
#### cisco\.ios

* cisco\.ios\.ios\_acls \- Added support for converting numeric protocol values to real protocol options when gathered from the device\.
* cisco\.ios\.ios\_acls \- Gathered state showing incomplete configuration\.
* cisco\.ios\.ios\_hsrp\_intefaces \- Considers version 1 as default if configuration does not specify version\.
* cisco\.ios\.ios\_hsrp\_intefaces \- Corrects idempotency issue when version is not specified in configuration\.
* cisco\.ios\.ios\_l2\_interfaces \- Moved mode parser to below the trunk parsers\.

<a id="cisco-iosxr-2"></a>
#### cisco\.iosxr

* iosxr\_bgp\_address\_family \- Fixed label generation command handling under <em class="title-reference">address\_family</em> configuration\.

<a id="cisco-nxos-1"></a>
#### cisco\.nxos

* cisco\.nxos\.nxos\_hsrp\_intefaces \- Considers version 1 as default if configuration does not specify version\.
* cisco\.nxos\.nxos\_hsrp\_intefaces \- Corrects idempotency issue when version is not specified in configuration\.

<a id="community-dns-5"></a>
#### community\.dns

* Update Public Suffix List\.

<a id="community-general-14"></a>
#### community\.general

* apk \- fix <code>packages</code> return value for apk\-tools \>\= 3 \(Alpine 3\.23\) \([https\://github\.com/ansible\-collections/community\.general/issues/11264](https\://github\.com/ansible\-collections/community\.general/issues/11264)\)\.
* iptables\_state \- refactor code to avoid writing unnecessary temporary files \([https\://github\.com/ansible\-collections/community\.general/pull/11258](https\://github\.com/ansible\-collections/community\.general/pull/11258)\)\.
* keycloak\_realm \- fixed crash in <code>sanitize\_cr\(\)</code> when <code>realmrep</code> was <code>None</code> \([https\://github\.com/ansible\-collections/community\.general/pull/11260](https\://github\.com/ansible\-collections/community\.general/pull/11260)\)\.
* keycloak\_user\_rolemapping module \- fixed crash when assigning roles to users without an existing role \([https\://github\.com/ansible\-collections/community\.general/issues/10960](https\://github\.com/ansible\-collections/community\.general/issues/10960)\, [https\://github\.com/ansible\-collections/community\.general/pull/11256](https\://github\.com/ansible\-collections/community\.general/pull/11256)\)\.
* listen\_ports\_facts \- fix handling of empty PID lists when <code>command\=ss</code> \([https\://github\.com/ansible\-collections/community\.general/pull/11332](https\://github\.com/ansible\-collections/community\.general/pull/11332)\)\.
* monit \- add delay of 0\.5 seconds after state change and check for status \([https\://github\.com/ansible\-collections/community\.general/pull/11255](https\://github\.com/ansible\-collections/community\.general/pull/11255)\)\.
* monit \- internal state was not reflecting when operation is \"pending\" in <code>monit</code> \([https\://github\.com/ansible\-collections/community\.general/pull/11245](https\://github\.com/ansible\-collections/community\.general/pull/11245)\)\.

<a id="community-proxmox-7"></a>
#### community\.proxmox

* proxmox all \- add missing timeout parameter to proxmoxer object creation \([https\://github\.com/ansible\-collections/community\.proxmox/pull/218](https\://github\.com/ansible\-collections/community\.proxmox/pull/218)\)\.
* proxmox\_ipam\_info \- fix bug where selecting by vmid did not work \([https\://github\.com/ansible\-collections/community\.proxmox/pull/211](https\://github\.com/ansible\-collections/community\.proxmox/pull/211)\)\.
* proxmox\_zone \- fix validation logic for VXLAN zones to accept either <code>fabric</code> or <code>peers</code> parameter\. Previously\, only <code>fabric</code> was accepted\, but Proxmox VE also supports creating VXLAN zones with a peer address list \([https\://github\.com/ansible\-collections/community\.proxmox/issues/216](https\://github\.com/ansible\-collections/community\.proxmox/issues/216)\)\.
* remove wrong api endpoints and error messages from proxmod\_node certificate management\([https\://github\.com/ansible\-collections/community\.proxmox/pull/232](https\://github\.com/ansible\-collections/community\.proxmox/pull/232)\)\.

<a id="fortinet-fortimanager-3"></a>
#### fortinet\.fortimanager

* Improved the request sending logic in httpapi plugin\.

<a id="hitachivantara-vspone-block-2"></a>
#### hitachivantara\.vspone\_block

* Resolved resource group creation with VSP 5XXX series storage systems\.
* Various playbook fixes and improvements\.

<a id="netapp-ontap-6"></a>
#### netapp\.ontap

* na\_ontap\_aggregate \- fixed issue with disabling software encryption in REST\.
* na\_ontap\_cg\_snapshot \- fixed issue with ZAPI by removing default value for <em class="title-reference">consistency\_type</em>\.
* na\_ontap\_cifs\_local\_group \- fixed issue with idempotency\.
* na\_ontap\_firmware\_upgrade \- Updated documentation for <em class="title-reference">node</em> parameter and added examples\.
* na\_ontap\_job\_schedule \- Fix documentation formatting issue\.
* na\_ontap\_net\_vlan \- Fixed state detection when VLAN exists but is not in broadcast domain\.
* na\_ontap\_qtree \- Updated documentation for \'unix\_permissions\' parameter to clarify its usage\.

<a id="netapp-storagegrid-1"></a>
#### netapp\.storagegrid

* na\_sg\_grid\_alert\_receiver \- correct example section in the module for better understanding\.
* na\_sg\_grid\_autosupport \- add support to handle error response from the API\.
* na\_sg\_grid\_autosupport \- fix issue with setting up <em class="title-reference">destinations</em> option in the module\.
* na\_sg\_grid\_domain\_name \- fixed issue where additional domain names was not detected as changed\.
* na\_sg\_grid\_group \- fix issue where <em class="title-reference">activate\_features</em> parameter was deprecated but still present in code\.
* na\_sg\_grid\_group \- fix typo in parameter mapping for <em class="title-reference">alarm\_acknowledgement</em> option\.
* na\_sg\_grid\_ha\_group \- correct documentation section in the module for better understanding\.
* na\_sg\_grid\_identity\_federation \- fix issue with check mode response\.
* na\_sg\_grid\_info \- Fix issue where the module incorrectly reported tasks as changed\.
* na\_sg\_grid\_regions \- correct documentation section in the module for better understanding\.
* na\_sg\_org\_identity\_federation \- fix issue with check mode response\.
* na\_sg\_org\_info \- Fix issue where the module incorrectly reported tasks as changed\.
* na\_sg\_org\_user\_s3\_key \- unique\_user\_name is fixed as in the documents

<a id="purestorage-flasharray-1"></a>
#### purestorage\.flasharray

* purefa\_info \- Added version check to ensure tags are only used in appropriate Purity versions
* purefa\_info \- Fixed AttributeError when directory service role has no name
* purefa\_policy \- Multiple syntax errors fixed in the password policy update section

<a id="purestorage-flashblade-2"></a>
#### purestorage\.flashblade

* purefb\_alert \- Fixed issue with syntax error in update function
* purefb\_bucket\_replica \- Fixed IndexError crash in check loop
* purefb\_bucket\_replica \- Fixed issue with ItemIterator error
* purefb\_pingtrace \- Fiexed issue with XFM module when state is ping

<a id="new-modules-4"></a>
### New Modules

<a id="community-general-15"></a>
#### community\.general

* community\.general\.ip2location\_info \- Retrieve IP geolocation information of a host\'s IP address\.
* community\.general\.sssd\_info \- Check SSSD domain status using D\-Bus\.

<a id="community-proxmox-8"></a>
#### community\.proxmox

* community\.proxmox\.proxmox\_ceph\_mds \- Add or delete Ceph Mds\.
* community\.proxmox\.proxmox\_ceph\_mgr \- Add or delete Ceph Manager\.
* community\.proxmox\.proxmox\_ceph\_mon \- Add or delete Ceph Monitor\.
* community\.proxmox\.proxmox\_sendkey \- Send key presses to a Proxmox VM console\.

<a id="fortinet-fortimanager-4"></a>
#### fortinet\.fortimanager

* fortinet\.fortimanager\.fmgr\_devprof\_log\_syslogd\_setting\_logtemplates \- System template log syslogd setting log templates
* fortinet\.fortimanager\.fmgr\_dynamic\_log\_npuserver\_servergroup\_dynamicmapping \- Dynamic log npu server server group dynamic mapping
* fortinet\.fortimanager\.fmgr\_firewall\_pfcp \- Configure PFCP\.
* fortinet\.fortimanager\.fmgr\_firewall\_profileprotocoloptions\_proxyredirect \- Firewall profile protocol options proxy redirect
* fortinet\.fortimanager\.fmgr\_firewall\_profileprotocoloptions\_rtmp \- RTMP\.
* fortinet\.fortimanager\.fmgr\_firewall\_proxyaddress6 \- Firewall proxy address6
* fortinet\.fortimanager\.fmgr\_firewall\_proxyaddress6\_headergroup \- Firewall proxy address6 header group
* fortinet\.fortimanager\.fmgr\_firewall\_proxyaddress6\_tagging \- Firewall proxy address6 tagging
* fortinet\.fortimanager\.fmgr\_firewall\_proxyaddrgrp6 \- Firewall proxy addrgrp6
* fortinet\.fortimanager\.fmgr\_firewall\_proxyaddrgrp6\_tagging \- Firewall proxy addrgrp6 tagging
* fortinet\.fortimanager\.fmgr\_firewall\_shapingprofile\_classes \- Firewall shaping profile classes
* fortinet\.fortimanager\.fmgr\_firewall\_sslsshprofile\_sslclientcertificate \- Firewall ssl ssh profile ssl client certificate
* fortinet\.fortimanager\.fmgr\_icap\_remoteservergroup \- Icap remote server group
* fortinet\.fortimanager\.fmgr\_icap\_remoteservergroup\_serverlist \- Icap remote server group server list
* fortinet\.fortimanager\.fmgr\_isolator\_profile \- Isolator profile
* fortinet\.fortimanager\.fmgr\_isolator\_profile\_entries \- Isolator profile entries
* fortinet\.fortimanager\.fmgr\_pkg\_firewall\_responseshapingpolicy \- Policy package firewall response shaping policy
* fortinet\.fortimanager\.fmgr\_switchcontroller\_managedswitch\_routerstatic \- Configure static routes\.
* fortinet\.fortimanager\.fmgr\_switchcontroller\_managedswitch\_routervrf \- Configure VRF\.
* fortinet\.fortimanager\.fmgr\_switchcontroller\_managedswitch\_systemdhcpserver \- Configure DHCP servers\.
* fortinet\.fortimanager\.fmgr\_switchcontroller\_managedswitch\_systemdhcpserver\_options \- DHCP options\.
* fortinet\.fortimanager\.fmgr\_switchcontroller\_managedswitch\_systeminterface \- Configure system interface on FortiSwitch\.
* fortinet\.fortimanager\.fmgr\_switchcontroller\_securitypolicy\_localaccess \- Configure allowaccess list for mgmt and internal interfaces on managed FortiSwitch units\.
* fortinet\.fortimanager\.fmgr\_switchcontroller\_switchprofile \- Configure FortiSwitch switch profile\.
* fortinet\.fortimanager\.fmgr\_system\_dnsdatabase \- Configure DNS databases\.
* fortinet\.fortimanager\.fmgr\_system\_dnsdatabase\_dnsentry \- DNS entry\.
* fortinet\.fortimanager\.fmgr\_system\_localinpolicy6\_dport \- Cli system local in policy6 dport
* fortinet\.fortimanager\.fmgr\_system\_localinpolicy6\_dst \- Cli system local in policy6 dst
* fortinet\.fortimanager\.fmgr\_system\_localinpolicy6\_intf \- Cli system local in policy6 intf
* fortinet\.fortimanager\.fmgr\_system\_localinpolicy6\_src \- Cli system local in policy6 src
* fortinet\.fortimanager\.fmgr\_system\_localinpolicy\_dport \- Cli system local in policy dport
* fortinet\.fortimanager\.fmgr\_system\_localinpolicy\_dst \- Cli system local in policy dst
* fortinet\.fortimanager\.fmgr\_system\_localinpolicy\_intf \- Cli system local in policy intf
* fortinet\.fortimanager\.fmgr\_system\_localinpolicy\_src \- Cli system local in policy src
* fortinet\.fortimanager\.fmgr\_telemetrycontroller\_agent \- Configure FortiTelemetry agents managed by a FortiGate unit\.
* fortinet\.fortimanager\.fmgr\_user\_oidc \- User oidc
* fortinet\.fortimanager\.fmgr\_vpn\_certificate\_hsmlocal \- Local certificates whose keys are stored on HSM\.
* fortinet\.fortimanager\.fmgr\_vpn\_ipsec\_manualkey \- Configure IPsec manual keys\.
* fortinet\.fortimanager\.fmgr\_vpn\_ipsec\_phase1 \- Configure VPN remote gateway\.
* fortinet\.fortimanager\.fmgr\_vpn\_ipsec\_phase1\_ipv4excluderange \- Configuration Method IPv4 exclude ranges\.
* fortinet\.fortimanager\.fmgr\_vpn\_ipsec\_phase1\_ipv6excluderange \- Configuration method IPv6 exclude ranges\.
* fortinet\.fortimanager\.fmgr\_vpn\_kmipserver \- KMIP server entry configuration\.
* fortinet\.fortimanager\.fmgr\_vpn\_kmipserver\_serverlist \- KMIP server list\.
* fortinet\.fortimanager\.fmgr\_webfilter\_domainlist \- Webfilter domain list
* fortinet\.fortimanager\.fmgr\_webfilter\_domainlist\_entries \- Webfilter domain list entries
* fortinet\.fortimanager\.fmgr\_webfilter\_ftgdrisklevel \- Configure FortiGuard Web Filter risk level\.
* fortinet\.fortimanager\.fmgr\_webfilter\_urllist \- Webfilter url list
* fortinet\.fortimanager\.fmgr\_webfilter\_urllist\_entries \- Webfilter url list entries
* fortinet\.fortimanager\.fmgr\_webproxy\_explicitproxy \- Web proxy explicit proxy
* fortinet\.fortimanager\.fmgr\_webproxy\_redirectprofile \- Web proxy redirect profile
* fortinet\.fortimanager\.fmgr\_webproxy\_redirectprofile\_entries \- Web proxy redirect profile entries
* fortinet\.fortimanager\.fmgr\_ztna\_serviceconnector \- Ztna service connector
* fortinet\.fortimanager\.fmgr\_ztna\_trafficforwardproxy \- Configure ZTNA traffic forward proxy\.
* fortinet\.fortimanager\.fmgr\_ztna\_trafficforwardproxy\_sslserverciphersuites \- Ztna traffic forward proxy ssl server cipher suites
* fortinet\.fortimanager\.fmgr\_ztna\_trafficforwardproxy\_urlroute \- Ztna traffic forward proxy url route
* fortinet\.fortimanager\.fmgr\_ztna\_webportal \- Configure ztna web\-portal\.
* fortinet\.fortimanager\.fmgr\_ztna\_webportalbookmark \- Configure ztna web\-portal bookmark\.
* fortinet\.fortimanager\.fmgr\_ztna\_webportalbookmark\_bookmarks \- Bookmark table\.
* fortinet\.fortimanager\.fmgr\_ztna\_webproxy \- Configure ZTNA web\-proxy\.
* fortinet\.fortimanager\.fmgr\_ztna\_webproxy\_apigateway \- Set IPv4 API Gateway\.
* fortinet\.fortimanager\.fmgr\_ztna\_webproxy\_apigateway6 \- Set IPv6 API Gateway\.
* fortinet\.fortimanager\.fmgr\_ztna\_webproxy\_apigateway6\_realservers \- Select the real servers that this Access Proxy will distribute traffic to\.
* fortinet\.fortimanager\.fmgr\_ztna\_webproxy\_apigateway6\_sslciphersuites \- SSL/TLS cipher suites to offer to a server\, ordered by priority\.
* fortinet\.fortimanager\.fmgr\_ztna\_webproxy\_apigateway\_realservers \- Select the real servers that this Access Proxy will distribute traffic to\.

<a id="netapp-storagegrid-2"></a>
#### netapp\.storagegrid

* netapp\.storagegrid\.na\_sg\_grid\_firewall \- NetApp StorageGRID manage node firewall\.
* netapp\.storagegrid\.na\_sg\_grid\_login \- Login to StorageGRID grid/tenant\.
* netapp\.storagegrid\.na\_sg\_grid\_metrics \- NetApp StorageGRID grab metrics\.
* netapp\.storagegrid\.na\_sg\_grid\_recovery\_package \- Retrieve the recovery package from StorageGRID
* netapp\.storagegrid\.na\_sg\_grid\_ssh\_security \- Configure ssh security on StorageGRID\.
* netapp\.storagegrid\.na\_sg\_grid\_untrusted\_client\_network \- Configure untrusted Client Network on StorageGRID\.
* netapp\.storagegrid\.na\_sg\_org\_cloud\_mirror\_replication \- Manage Cloud Mirror Replication on StorageGRID\.
* netapp\.storagegrid\.na\_sg\_pge\_info \- NetApp StorageGRID node PGE information gatherer\.

<a id="unchanged-collections-4"></a>
### Unchanged Collections

* amazon\.aws \(still version 10\.1\.2\)
* ansible\.netcommon \(still version 8\.2\.0\)
* ansible\.posix \(still version 2\.1\.0\)
* ansible\.utils \(still version 6\.0\.0\)
* ansible\.windows \(still version 3\.3\.0\)
* arista\.eos \(still version 12\.0\.0\)
* awx\.awx \(still version 24\.6\.1\)
* azure\.azcollection \(still version 3\.12\.0\)
* chocolatey\.chocolatey \(still version 1\.5\.3\)
* cisco\.aci \(still version 2\.13\.0\)
* cisco\.dnac \(still version 6\.43\.0\)
* cisco\.intersight \(still version 2\.12\.0\)
* cisco\.meraki \(still version 2\.21\.9\)
* cisco\.mso \(still version 2\.12\.0\)
* cisco\.ucs \(still version 1\.16\.0\)
* cloudscale\_ch\.cloud \(still version 2\.5\.2\)
* community\.aws \(still version 10\.0\.0\)
* community\.ciscosmb \(still version 1\.0\.11\)
* community\.docker \(still version 5\.0\.4\)
* community\.grafana \(still version 2\.3\.0\)
* community\.hashi\_vault \(still version 7\.1\.0\)
* community\.hrobot \(still version 2\.7\.0\)
* community\.library\_inventory\_filtering\_v1 \(still version 1\.1\.5\)
* community\.libvirt \(still version 2\.0\.0\)
* community\.mongodb \(still version 1\.7\.10\)
* community\.mysql \(still version 4\.0\.1\)
* community\.okd \(still version 5\.0\.0\)
* community\.postgresql \(still version 4\.2\.0\)
* community\.proxysql \(still version 1\.7\.0\)
* community\.rabbitmq \(still version 1\.6\.0\)
* community\.sops \(still version 2\.2\.7\)
* community\.vmware \(still version 6\.1\.0\)
* community\.windows \(still version 3\.1\.0\)
* community\.zabbix \(still version 4\.1\.1\)
* containers\.podman \(still version 1\.18\.0\)
* cyberark\.conjur \(still version 1\.3\.9\)
* cyberark\.pas \(still version 1\.0\.36\)
* dellemc\.enterprise\_sonic \(still version 3\.2\.0\)
* dellemc\.openmanage \(still version 10\.0\.1\)
* dellemc\.powerflex \(still version 3\.0\.0\)
* dellemc\.unity \(still version 2\.1\.0\)
* f5networks\.f5\_modules \(still version 1\.39\.0\)
* fortinet\.fortios \(still version 2\.4\.2\)
* google\.cloud \(still version 1\.10\.2\)
* grafana\.grafana \(still version 6\.0\.6\)
* hitachivantara\.vspone\_object \(still version 1\.1\.1\)
* ibm\.storage\_virtualize \(still version 3\.1\.0\)
* ieisystem\.inmanage \(still version 4\.0\.0\)
* infinidat\.infinibox \(still version 1\.6\.3\)
* infoblox\.nios\_modules \(still version 1\.8\.0\)
* inspur\.ispim \(still version 2\.2\.4\)
* junipernetworks\.junos \(still version 11\.0\.0\)
* kaytus\.ksmanage \(still version 2\.0\.0\)
* kubernetes\.core \(still version 6\.2\.0\)
* kubevirt\.core \(still version 2\.2\.3\)
* lowlydba\.sqlserver \(still version 2\.7\.0\)
* microsoft\.ad \(still version 1\.10\.0\)
* microsoft\.iis \(still version 1\.1\.0\)
* netapp\.cloudmanager \(still version 21\.24\.0\)
* netapp\_eseries\.santricity \(still version 1\.4\.1\)
* netbox\.netbox \(still version 3\.21\.0\)
* ngine\_io\.cloudstack \(still version 3\.0\.0\)
* openstack\.cloud \(still version 2\.5\.0\)
* ovirt\.ovirt \(still version 3\.2\.1\)
* ravendb\.ravendb \(still version 1\.0\.4\)
* splunk\.es \(still version 4\.0\.0\)
* telekom\_mms\.icinga\_director \(still version 2\.5\.0\)
* theforeman\.foreman \(still version 5\.7\.0\)
* vmware\.vmware \(still version 2\.6\.0\)
* vmware\.vmware\_rest \(still version 4\.9\.0\)
* vultr\.cloud \(still version 1\.13\.0\)
* vyos\.vyos \(still version 6\.0\.0\)
* wti\.remote \(still version 1\.0\.10\)

<a id="v13-1-0"></a>
## v13\.1\.0

- <a href="#release-summary-5">Release Summary</a>
- <a href="#ansible-core-13">Ansible\-core</a>
- <a href="#changed-collections-5">Changed Collections</a>
- <a href="#major-changes-5">Major Changes</a>
    - <a href="#vmware-vmware-4">vmware\.vmware</a>
- <a href="#minor-changes-5">Minor Changes</a>
    - <a href="#ansible-netcommon-5">ansible\.netcommon</a>
    - <a href="#ansible-windows-4">ansible\.windows</a>
    - <a href="#cisco-aci">cisco\.aci</a>
    - <a href="#cisco-dnac-2">cisco\.dnac</a>
    - <a href="#cisco-mso-2">cisco\.mso</a>
    - <a href="#cisco-nxos-2">cisco\.nxos</a>
    - <a href="#community-general-16">community\.general</a>
    - <a href="#community-postgresql">community\.postgresql</a>
    - <a href="#community-routeros-9">community\.routeros</a>
    - <a href="#community-windows">community\.windows</a>
    - <a href="#google-cloud-4">google\.cloud</a>
    - <a href="#hetzner-hcloud-5">hetzner\.hcloud</a>
    - <a href="#hitachivantara-vspone-block-3">hitachivantara\.vspone\_block</a>
    - <a href="#hitachivantara-vspone-object">hitachivantara\.vspone\_object</a>
    - <a href="#microsoft-ad">microsoft\.ad</a>
    - <a href="#microsoft-iis">microsoft\.iis</a>
    - <a href="#purestorage-flasharray-2">purestorage\.flasharray</a>
    - <a href="#telekom-mms-icinga-director">telekom\_mms\.icinga\_director</a>
    - <a href="#vmware-vmware-5">vmware\.vmware</a>
- <a href="#deprecated-features-5">Deprecated Features</a>
    - <a href="#community-general-17">community\.general</a>
- <a href="#bugfixes-5">Bugfixes</a>
    - <a href="#ansible-core-14">Ansible\-core</a>
    - <a href="#ansible-netcommon-6">ansible\.netcommon</a>
    - <a href="#ansible-windows-5">ansible\.windows</a>
    - <a href="#cisco-aci-1">cisco\.aci</a>
    - <a href="#cisco-meraki-5">cisco\.meraki</a>
    - <a href="#cisco-mso-3">cisco\.mso</a>
    - <a href="#cisco-nxos-3">cisco\.nxos</a>
    - <a href="#community-dns-6">community\.dns</a>
    - <a href="#community-docker-4">community\.docker</a>
    - <a href="#community-general-18">community\.general</a>
    - <a href="#community-postgresql-1">community\.postgresql</a>
    - <a href="#community-routeros-10">community\.routeros</a>
    - <a href="#community-windows-1">community\.windows</a>
    - <a href="#google-cloud-5">google\.cloud</a>
    - <a href="#hetzner-hcloud-6">hetzner\.hcloud</a>
    - <a href="#hitachivantara-vspone-block-4">hitachivantara\.vspone\_block</a>
    - <a href="#inspur-ispim">inspur\.ispim</a>
    - <a href="#microsoft-ad-1">microsoft\.ad</a>
    - <a href="#microsoft-iis-1">microsoft\.iis</a>
    - <a href="#purestorage-flasharray-3">purestorage\.flasharray</a>
    - <a href="#telekom-mms-icinga-director-1">telekom\_mms\.icinga\_director</a>
    - <a href="#vmware-vmware-6">vmware\.vmware</a>
- <a href="#known-issues-2">Known Issues</a>
    - <a href="#community-docker-5">community\.docker</a>
- <a href="#new-modules-5">New Modules</a>
    - <a href="#cisco-aci-2">cisco\.aci</a>
    - <a href="#cisco-mso-4">cisco\.mso</a>
    - <a href="#community-general-19">community\.general</a>
    - <a href="#hitachivantara-vspone-block-5">hitachivantara\.vspone\_block</a>
- <a href="#unchanged-collections-5">Unchanged Collections</a>

<a id="release-summary-5"></a>
### Release Summary

Release Date\: 2025\-12\-09

[Porting Guide](https\://docs\.ansible\.com/projects/ansible/devel/porting\_guides\.html)

<a id="ansible-core-13"></a>
### Ansible\-core

Ansible 13\.1\.0 contains ansible\-core version 2\.20\.1\.
This is a newer version than version 2\.20\.0 contained in the previous Ansible release\.

The changes are reported in the combined changelog below\.

<a id="changed-collections-5"></a>
### Changed Collections

If not mentioned explicitly\, the changes are reported in the combined changelog below\.

| Collection                   | Ansible 13.0.0 | Ansible 13.1.0 | Notes                                                                                                                                                                                                        |
| ---------------------------- | -------------- | -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| ansible.netcommon            | 8.1.0          | 8.2.0          |                                                                                                                                                                                                              |
| ansible.windows              | 3.2.0          | 3.3.0          |                                                                                                                                                                                                              |
| azure.azcollection           | 3.10.1         | 3.12.0         | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.                                                                                 |
| check_point.mgmt             | 6.6.0          | 6.7.0          | The collection did not have a changelog in this version.                                                                                                                                                     |
| cisco.aci                    | 2.12.0         | 2.13.0         |                                                                                                                                                                                                              |
| cisco.dnac                   | 6.41.0         | 6.43.0         |                                                                                                                                                                                                              |
| cisco.intersight             | 2.7.0          | 2.12.0         | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.                                                                                 |
| cisco.meraki                 | 2.21.8         | 2.21.9         |                                                                                                                                                                                                              |
| cisco.mso                    | 2.11.0         | 2.12.0         |                                                                                                                                                                                                              |
| cisco.nxos                   | 11.0.0         | 11.1.0         |                                                                                                                                                                                                              |
| community.dns                | 3.4.0          | 3.4.1          |                                                                                                                                                                                                              |
| community.docker             | 5.0.1          | 5.0.4          |                                                                                                                                                                                                              |
| community.general            | 12.0.1         | 12.1.0         |                                                                                                                                                                                                              |
| community.postgresql         | 4.1.0          | 4.2.0          |                                                                                                                                                                                                              |
| community.routeros           | 3.13.0         | 3.14.0         |                                                                                                                                                                                                              |
| community.windows            | 3.0.1          | 3.1.0          |                                                                                                                                                                                                              |
| cyberark.conjur              | 1.3.8          | 1.3.9          | You can find the collection's changelog at [https://github.com/cyberark/ansible-conjur-collection/blob/master/CHANGELOG.md](https://github.com/cyberark/ansible-conjur-collection/blob/master/CHANGELOG.md). |
| google.cloud                 | 1.9.0          | 1.10.2         |                                                                                                                                                                                                              |
| hetzner.hcloud               | 6.0.0          | 6.2.1          |                                                                                                                                                                                                              |
| hitachivantara.vspone_block  | 4.4.0          | 4.5.0          |                                                                                                                                                                                                              |
| hitachivantara.vspone_object | 1.0.0          | 1.1.1          |                                                                                                                                                                                                              |
| inspur.ispim                 | 2.2.3          | 2.2.4          |                                                                                                                                                                                                              |
| microsoft.ad                 | 1.9.2          | 1.10.0         |                                                                                                                                                                                                              |
| microsoft.iis                | 1.0.3          | 1.1.0          |                                                                                                                                                                                                              |
| purestorage.flasharray       | 1.39.0         | 1.40.0         |                                                                                                                                                                                                              |
| telekom_mms.icinga_director  | 2.4.0          | 2.5.0          |                                                                                                                                                                                                              |
| vmware.vmware                | 2.4.0          | 2.6.0          |                                                                                                                                                                                                              |

<a id="major-changes-5"></a>
### Major Changes

<a id="vmware-vmware-4"></a>
#### vmware\.vmware

* Replace <code>ansible\.module\_utils\.\_text</code> \([https\://github\.com/ansible\-collections/vmware\.vmware/issues/268](https\://github\.com/ansible\-collections/vmware\.vmware/issues/268)\)\.
* Replace <code>ansible\.module\_utils\.common\.\_collections\_compat</code> \([https\://github\.com/ansible\-collections/vmware\.vmware/issues/271](https\://github\.com/ansible\-collections/vmware\.vmware/issues/271)\)\.

<a id="minor-changes-5"></a>
### Minor Changes

<a id="ansible-netcommon-5"></a>
#### ansible\.netcommon

* Exposes new libssh option to configure key\_exchange\_algorithms\. This requires ansible\-pylibssh v1\.3\.0 or higher\.

<a id="ansible-windows-4"></a>
#### ansible\.windows

* Add official support for Ansible 2\.20
* win\_environment \- Add the return value <code>env\_values</code> which is a copy of the existing <code>values</code> return value\. The documentation for <code>values</code> has been removed to discourage use of that version due to the inability to use <code>values</code> with dot notation in a Jinja2 template due to the conflict with the Python <code>values</code> attribute\.

<a id="cisco-aci"></a>
#### cisco\.aci

* Add contract\_type option to aci\_contract\_subject\_to\_filter and aci\_contract\_subject\.
* Add l3out\, l3out\_tenant\, external\_epg and redistribute options to aci\_l4l7\_device\_selection\_interface\_context\.
* Add normalize\_payload\_values option to aci\_rest for Ansible Core 2\.19 support\.
* Add set\_communities\, set\_as\_path and set\_policy\_tag options to aci\_tenant\_action\_rule\_profile\.

<a id="cisco-dnac-2"></a>
#### cisco\.dnac

* Added \'ap\_authorization\_list\_name\'\, \'authorize\_mesh\_and\_non\_mesh\_aps\'\, \'feature\_template\'  attributes in provision\_workflow\_manager module
* Added \'authorize\' attribute in network\_profile\_wireless\_workflow\_manager module
* Added \'backup\_task\_timeout\' and \'restore\_task\_timeout\'  attributes in backup\_and\_restore\_workflow\_manager module
* Added \'convert\_to\_wlc\'  attribute in swim\_workflow\_manager module
* Added \'feature\_template\_config\'  attribute in wireless\_design\_workflow\_manager module
* Added \'feature\_template\_designs\' attribute in network\_profile\_wireless\_workflow\_manager module
* Added \'image\_name\'\, sync\_cco\, image\_distribution\_timeout\, device\_tag\, image\_activation\_timeout\, compatible\_devices in swim\_workflow\_manager module
* Added \'profile\_names\' in template\_workflow\_manager module
* Added \'sda\_fabric\_port\_channel\_limit\'  attribute in sda\_host\_port\_onboarding\_workflow\_manager module
* Changes in accesspoint\_workflow\_manager module
* Changes in application\_policy\_workflow\_manager module
* Changes in backup\_and\_restore\_workflow\_manager module
* Changes in inventory\_workflow\_manager module
* Changes in ise\_radius\_integration\_workflow\_manager module
* Changes in lan\_automation\_workflow\_manager module
* Changes in network\_devices\_info\_workflow\_manager module
* Changes in network\_profile\_wireless\_workflow\_manager module
* Changes in network\_settings\_workflow\_manager module
* Changes in pnp\_workflow\_manager module
* Changes in provision\_workflow\_manager module
* Changes in reports\_workflow\_manager module
* Changes in sda\_fabric\_sites\_zones\_workflow\_manager module
* Changes in sda\_fabric\_virtual\_networks\_workflow\_manager module
* Changes in sda\_host\_port\_onboarding\_workflow\_manager module
* Changes in swim\_workflow\_manager module
* Changes in template\_workflow\_manager module
* Changes in wireless\_design\_workflow\_manager module
* Enhancements in \'lan\_automation\_workflow\_manager\' to support port channel
* Enhancements in \'pnp\_workflow\_manager\' to support authorization
* New module \'accesspoint\_location\_workflow\_manager\' to manage Access point planned position in the floor
* New module \'backup\_and\_restore\_workflow\_manager\' for backup and restore workflow management
* New module \'fabric\_devices\_info\_workflow\_manager\' for gathering fabric device information
* New module \'network\_devices\_info\_workflow\_manager\' for gathering network device information
* New module \'reports\_workflow\_manager\' for managing reports
* New module \'wired\_campus\_automation\_workflow\_manager\' for managing wired campus automation

<a id="cisco-mso-2"></a>
#### cisco\.mso

* Add parent\_type\, node\_id\, path\, port\_channel\, virtual\_port\_channel\, encapsulation\_type and encapsulation\_value options to ndo\_l3out\_bgp\_peer\.
* Add ptp option to ndo\_l3out\_routed\_interface and ndo\_l3out\_routed\_sub\_interface\.

<a id="cisco-nxos-2"></a>
#### cisco\.nxos

* Added alias for mode option as switchport\_mode for nxos\_l2\_interfaces

<a id="community-general-16"></a>
#### community\.general

* The last code included in the collection that was licensed under the PSF 2\.0 license was removed form the collection\. This means that now all code is either GPLv3\+ licensed\, MIT licensed\, or BSD\-2\-clause licensed \([https\://github\.com/ansible\-collections/community\.general/pull/11232](https\://github\.com/ansible\-collections/community\.general/pull/11232)\)\.
* \_mount module utils \- simplify return of boolean values in functions \([https\://github\.com/ansible\-collections/community\.general/pull/11119](https\://github\.com/ansible\-collections/community\.general/pull/11119)\)\.
* \_stormssh module utils \- fix cases of unused variables in loops \([https\://github\.com/ansible\-collections/community\.general/pull/11115](https\://github\.com/ansible\-collections/community\.general/pull/11115)\)\.
* a\_module test plugin \- add proper parameter checking and type hints \([https\://github\.com/ansible\-collections/community\.general/pull/11167](https\://github\.com/ansible\-collections/community\.general/pull/11167)\)\.
* aerospike\_migrations \- simplify return of boolean values in functions \([https\://github\.com/ansible\-collections/community\.general/pull/11119](https\://github\.com/ansible\-collections/community\.general/pull/11119)\)\.
* aix\_filesystem \- improve code by using native Python construct \([https\://github\.com/ansible\-collections/community\.general/pull/11215](https\://github\.com/ansible\-collections/community\.general/pull/11215)\)\.
* ali\_instance \- fix cases of unused variables in loops \([https\://github\.com/ansible\-collections/community\.general/pull/11115](https\://github\.com/ansible\-collections/community\.general/pull/11115)\)\.
* ansible\_type plugin utils \- add type hints \([https\://github\.com/ansible\-collections/community\.general/pull/11167](https\://github\.com/ansible\-collections/community\.general/pull/11167)\)\.
* ansible\_type test plugin \- add type hints \([https\://github\.com/ansible\-collections/community\.general/pull/11167](https\://github\.com/ansible\-collections/community\.general/pull/11167)\)\.
* apk \- simplify return of boolean values in functions \([https\://github\.com/ansible\-collections/community\.general/pull/11119](https\://github\.com/ansible\-collections/community\.general/pull/11119)\)\.
* apt\_rpm \- fix cases of unused variables in loops \([https\://github\.com/ansible\-collections/community\.general/pull/11115](https\://github\.com/ansible\-collections/community\.general/pull/11115)\)\.
* apt\_rpm \- simplify return of boolean values in functions \([https\://github\.com/ansible\-collections/community\.general/pull/11119](https\://github\.com/ansible\-collections/community\.general/pull/11119)\)\.
* atomic\_container \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11102](https\://github\.com/ansible\-collections/community\.general/pull/11102)\)\.
* atomic\_container modules \- replace <code>\%</code> templating with f\-strings or <code>format\(\)</code> \([https\://github\.com/ansible\-collections/community\.general/pull/11223](https\://github\.com/ansible\-collections/community\.general/pull/11223)\)\.
* atomic\_host \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11098](https\://github\.com/ansible\-collections/community\.general/pull/11098)\)\.
* atomic\_image \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11098](https\://github\.com/ansible\-collections/community\.general/pull/11098)\)\.
* atomic\_image modules \- replace <code>\%</code> templating with f\-strings or <code>format\(\)</code> \([https\://github\.com/ansible\-collections/community\.general/pull/11223](https\://github\.com/ansible\-collections/community\.general/pull/11223)\)\.
* awall \- simplify return of boolean values in functions \([https\://github\.com/ansible\-collections/community\.general/pull/11119](https\://github\.com/ansible\-collections/community\.general/pull/11119)\)\.
* beadm \- simplify return of boolean values in functions \([https\://github\.com/ansible\-collections/community\.general/pull/11119](https\://github\.com/ansible\-collections/community\.general/pull/11119)\)\.
* bigpanda \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11098](https\://github\.com/ansible\-collections/community\.general/pull/11098)\)\.
* binary\_file lookup plugin \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11095](https\://github\.com/ansible\-collections/community\.general/pull/11095)\)\.
* bitbucket module utils \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11112](https\://github\.com/ansible\-collections/community\.general/pull/11112)\)\.
* bitbucket\_access\_key modules \- replace <code>\%</code> templating with f\-strings or <code>format\(\)</code> \([https\://github\.com/ansible\-collections/community\.general/pull/11223](https\://github\.com/ansible\-collections/community\.general/pull/11223)\)\.
* bitbucket\_pipeline\_key\_pair modules \- replace <code>\%</code> templating with f\-strings or <code>format\(\)</code> \([https\://github\.com/ansible\-collections/community\.general/pull/11223](https\://github\.com/ansible\-collections/community\.general/pull/11223)\)\.
* bitbucket\_pipeline\_known\_host modules \- replace <code>\%</code> templating with f\-strings or <code>format\(\)</code> \([https\://github\.com/ansible\-collections/community\.general/pull/11223](https\://github\.com/ansible\-collections/community\.general/pull/11223)\)\.
* bitbucket\_pipeline\_variable modules \- replace <code>\%</code> templating with f\-strings or <code>format\(\)</code> \([https\://github\.com/ansible\-collections/community\.general/pull/11223](https\://github\.com/ansible\-collections/community\.general/pull/11223)\)\.
* chef\_databag lookup plugin \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11095](https\://github\.com/ansible\-collections/community\.general/pull/11095)\)\.
* chroot connection plugin \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11095](https\://github\.com/ansible\-collections/community\.general/pull/11095)\)\.
* circonus\_annotation \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11102](https\://github\.com/ansible\-collections/community\.general/pull/11102)\)\.
* cloudflare\_dns \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/1114](https\://github\.com/ansible\-collections/community\.general/pull/1114)\)\.
* cmd\_runner module utils \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11097](https\://github\.com/ansible\-collections/community\.general/pull/11097)\)\.
* cobbler inventory plugin \- fix cases of unused variables in loops \([https\://github\.com/ansible\-collections/community\.general/pull/11115](https\://github\.com/ansible\-collections/community\.general/pull/11115)\)\.
* cobbler\_sync \- remove conditional code handling SSL for unsupported versions of Python \([https\://github\.com/ansible\-collections/community\.general/pull/11078](https\://github\.com/ansible\-collections/community\.general/pull/11078)\)\.
* cobbler\_sync \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11105](https\://github\.com/ansible\-collections/community\.general/pull/11105)\)\.
* cobbler\_system \- remove conditional code handling SSL for unsupported versions of Python \([https\://github\.com/ansible\-collections/community\.general/pull/11078](https\://github\.com/ansible\-collections/community\.general/pull/11078)\)\.
* cobbler\_system \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11105](https\://github\.com/ansible\-collections/community\.general/pull/11105)\)\.
* collection\_version lookup plugin \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11095](https\://github\.com/ansible\-collections/community\.general/pull/11095)\)\.
* composer \- improve code by using native Python construct \([https\://github\.com/ansible\-collections/community\.general/pull/11215](https\://github\.com/ansible\-collections/community\.general/pull/11215)\)\.
* consul\_kv lookup plugin \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11095](https\://github\.com/ansible\-collections/community\.general/pull/11095)\)\.
* counter filter plugin \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11095](https\://github\.com/ansible\-collections/community\.general/pull/11095)\)\.
* credstash lookup plugin \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11095](https\://github\.com/ansible\-collections/community\.general/pull/11095)\)\.
* cronvar \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11097](https\://github\.com/ansible\-collections/community\.general/pull/11097)\)\.
* crypttab \- simplify return of boolean values in functions \([https\://github\.com/ansible\-collections/community\.general/pull/11119](https\://github\.com/ansible\-collections/community\.general/pull/11119)\)\.
* csv module utils \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11112](https\://github\.com/ansible\-collections/community\.general/pull/11112)\)\.
* csv module utils \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11097](https\://github\.com/ansible\-collections/community\.general/pull/11097)\)\.
* cyberarkpassword lookup plugin \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11095](https\://github\.com/ansible\-collections/community\.general/pull/11095)\)\.
* database module utils \- improve code by using native Python construct \([https\://github\.com/ansible\-collections/community\.general/pull/11215](https\://github\.com/ansible\-collections/community\.general/pull/11215)\)\.
* database module utils \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11097](https\://github\.com/ansible\-collections/community\.general/pull/11097)\)\.
* datadog\_event \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11098](https\://github\.com/ansible\-collections/community\.general/pull/11098)\)\.
* datadog\_monitor \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11098](https\://github\.com/ansible\-collections/community\.general/pull/11098)\)\.
* dconf \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/1114](https\://github\.com/ansible\-collections/community\.general/pull/1114)\)\.
* dependent lookup plugin \- improve templating of strings \([https\://github\.com/ansible\-collections/community\.general/pull/11189](https\://github\.com/ansible\-collections/community\.general/pull/11189)\)\.
* dependent lookup plugin \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11095](https\://github\.com/ansible\-collections/community\.general/pull/11095)\)\.
* deps module utils \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11112](https\://github\.com/ansible\-collections/community\.general/pull/11112)\)\.
* dig lookup plugin \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11095](https\://github\.com/ansible\-collections/community\.general/pull/11095)\)\.
* dimensiondata\_network \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11102](https\://github\.com/ansible\-collections/community\.general/pull/11102)\)\.
* dimensiondata\_network modules \- replace <code>\%</code> templating with f\-strings or <code>format\(\)</code> \([https\://github\.com/ansible\-collections/community\.general/pull/11223](https\://github\.com/ansible\-collections/community\.general/pull/11223)\)\.
* dnf\_config\_manager \- fix cases of unused variables in loops \([https\://github\.com/ansible\-collections/community\.general/pull/11115](https\://github\.com/ansible\-collections/community\.general/pull/11115)\)\.
* dnstxt lookup plugin \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11095](https\://github\.com/ansible\-collections/community\.general/pull/11095)\)\.
* dsv lookup plugin \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11095](https\://github\.com/ansible\-collections/community\.general/pull/11095)\)\.
* elastic callback plugin \- fix cases of unused variables in loops \([https\://github\.com/ansible\-collections/community\.general/pull/11115](https\://github\.com/ansible\-collections/community\.general/pull/11115)\)\.
* etcd3 lookup plugin \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11095](https\://github\.com/ansible\-collections/community\.general/pull/11095)\)\.
* exceptions module utils \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11112](https\://github\.com/ansible\-collections/community\.general/pull/11112)\)\.
* filesize \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11104](https\://github\.com/ansible\-collections/community\.general/pull/11104)\)\.
* filesize \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11106](https\://github\.com/ansible\-collections/community\.general/pull/11106)\)\.
* flatpak \- improve code by using native Python construct \([https\://github\.com/ansible\-collections/community\.general/pull/11215](https\://github\.com/ansible\-collections/community\.general/pull/11215)\)\.
* flatpak\_remote \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11106](https\://github\.com/ansible\-collections/community\.general/pull/11106)\)\.
* fqdn\_valid test plugin \- add proper parameter checking\, and add type hints \([https\://github\.com/ansible\-collections/community\.general/pull/11167](https\://github\.com/ansible\-collections/community\.general/pull/11167)\)\.
* from\_csv filter plugin \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11095](https\://github\.com/ansible\-collections/community\.general/pull/11095)\)\.
* from\_ini filter plugin \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11095](https\://github\.com/ansible\-collections/community\.general/pull/11095)\)\.
* gandi\_livedns\_api module utils \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11112](https\://github\.com/ansible\-collections/community\.general/pull/11112)\)\.
* github\_app\_access\_token lookup plugin \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11095](https\://github\.com/ansible\-collections/community\.general/pull/11095)\)\.
* gitlab\_group\_access\_token \- simplify return of boolean values in functions \([https\://github\.com/ansible\-collections/community\.general/pull/11119](https\://github\.com/ansible\-collections/community\.general/pull/11119)\)\.
* gitlab\_group\_members \- improve code by using native Python construct \([https\://github\.com/ansible\-collections/community\.general/pull/11215](https\://github\.com/ansible\-collections/community\.general/pull/11215)\)\.
* gitlab\_project\_access\_token \- simplify return of boolean values in functions \([https\://github\.com/ansible\-collections/community\.general/pull/11119](https\://github\.com/ansible\-collections/community\.general/pull/11119)\)\.
* gitlab\_project\_members \- improve code by using native Python construct \([https\://github\.com/ansible\-collections/community\.general/pull/11215](https\://github\.com/ansible\-collections/community\.general/pull/11215)\)\.
* gitlab\_runner \- allow maximum timeout to be disabled by passing <code>0</code> to <code>maximum\_timeout</code>  \([https\://github\.com/ansible\-collections/community\.general/pull/11174](https\://github\.com/ansible\-collections/community\.general/pull/11174)\)\.
* gitlab\_runners inventory plugin \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11095](https\://github\.com/ansible\-collections/community\.general/pull/11095)\)\.
* haproxy \- fix cases of unused variables in loops \([https\://github\.com/ansible\-collections/community\.general/pull/11115](https\://github\.com/ansible\-collections/community\.general/pull/11115)\)\.
* hashids filter \- replace <code>\%</code> templating with f\-strings or <code>format\(\)</code> \([https\://github\.com/ansible\-collections/community\.general/pull/11223](https\://github\.com/ansible\-collections/community\.general/pull/11223)\)\.
* hashids filter plugin \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11095](https\://github\.com/ansible\-collections/community\.general/pull/11095)\)\.
* hg \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11106](https\://github\.com/ansible\-collections/community\.general/pull/11106)\)\.
* hg \- simplify return of boolean values in functions \([https\://github\.com/ansible\-collections/community\.general/pull/11119](https\://github\.com/ansible\-collections/community\.general/pull/11119)\)\.
* hpilo\_info \- fix cases of unused variables in loops \([https\://github\.com/ansible\-collections/community\.general/pull/11115](https\://github\.com/ansible\-collections/community\.general/pull/11115)\)\.
* hpilo\_info \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11098](https\://github\.com/ansible\-collections/community\.general/pull/11098)\)\.
* htpasswd \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11098](https\://github\.com/ansible\-collections/community\.general/pull/11098)\)\.
* hwc\_ecs\_instance \- fix cases of unused variables in loops \([https\://github\.com/ansible\-collections/community\.general/pull/11115](https\://github\.com/ansible\-collections/community\.general/pull/11115)\)\.
* hwc\_utils module utils \- improve code by using native Python construct \([https\://github\.com/ansible\-collections/community\.general/pull/11215](https\://github\.com/ansible\-collections/community\.general/pull/11215)\)\.
* hwc\_utils module utils \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11097](https\://github\.com/ansible\-collections/community\.general/pull/11097)\)\.
* hwc\_vpc\_port \- fix cases of unused variables in loops \([https\://github\.com/ansible\-collections/community\.general/pull/11115](https\://github\.com/ansible\-collections/community\.general/pull/11115)\)\.
* ibm\_sa\_utils module utils \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11112](https\://github\.com/ansible\-collections/community\.general/pull/11112)\)\.
* icinga2 inventory plugin \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11095](https\://github\.com/ansible\-collections/community\.general/pull/11095)\)\.
* icinga2\_host \- simplify return of boolean values in functions \([https\://github\.com/ansible\-collections/community\.general/pull/11119](https\://github\.com/ansible\-collections/community\.general/pull/11119)\)\.
* identity\.keycloak\.keycloak module utils \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11097](https\://github\.com/ansible\-collections/community\.general/pull/11097)\)\.
* idrac\_redfish\_command \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11110](https\://github\.com/ansible\-collections/community\.general/pull/11110)\)\.
* idrac\_redfish\_command \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/1114](https\://github\.com/ansible\-collections/community\.general/pull/1114)\)\.
* idrac\_redfish\_config \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11098](https\://github\.com/ansible\-collections/community\.general/pull/11098)\)\.
* idrac\_redfish\_config \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11102](https\://github\.com/ansible\-collections/community\.general/pull/11102)\)\.
* idrac\_redfish\_config \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11110](https\://github\.com/ansible\-collections/community\.general/pull/11110)\)\.
* idrac\_redfish\_config \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/1114](https\://github\.com/ansible\-collections/community\.general/pull/1114)\)\.
* idrac\_redfish\_info \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11110](https\://github\.com/ansible\-collections/community\.general/pull/11110)\)\.
* idrac\_redfish\_info \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/1114](https\://github\.com/ansible\-collections/community\.general/pull/1114)\)\.
* ilo\_redfish\_command \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11110](https\://github\.com/ansible\-collections/community\.general/pull/11110)\)\.
* ilo\_redfish\_command \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/1114](https\://github\.com/ansible\-collections/community\.general/pull/1114)\)\.
* ilo\_redfish\_config \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11110](https\://github\.com/ansible\-collections/community\.general/pull/11110)\)\.
* ilo\_redfish\_config \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/1114](https\://github\.com/ansible\-collections/community\.general/pull/1114)\)\.
* imc\_rest modules \- replace <code>\%</code> templating with f\-strings or <code>format\(\)</code> \([https\://github\.com/ansible\-collections/community\.general/pull/11223](https\://github\.com/ansible\-collections/community\.general/pull/11223)\)\.
* incus connection plugin \- add support for Windows virtual machines \([https\://github\.com/ansible\-collections/community\.general/pull/11199](https\://github\.com/ansible\-collections/community\.general/pull/11199)\)\.
* influxdb\_query \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11098](https\://github\.com/ansible\-collections/community\.general/pull/11098)\)\.
* influxdb\_user \- fix cases of unused variables in loops \([https\://github\.com/ansible\-collections/community\.general/pull/11115](https\://github\.com/ansible\-collections/community\.general/pull/11115)\)\.
* influxdb\_user \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11098](https\://github\.com/ansible\-collections/community\.general/pull/11098)\)\.
* influxdb\_write \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11098](https\://github\.com/ansible\-collections/community\.general/pull/11098)\)\.
* iocage inventory plugin \- fix cases of unused variables in loops \([https\://github\.com/ansible\-collections/community\.general/pull/11115](https\://github\.com/ansible\-collections/community\.general/pull/11115)\)\.
* ip\_netns \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11104](https\://github\.com/ansible\-collections/community\.general/pull/11104)\)\.
* ip\_netns \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11105](https\://github\.com/ansible\-collections/community\.general/pull/11105)\)\.
* ip\_netns \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11106](https\://github\.com/ansible\-collections/community\.general/pull/11106)\)\.
* ipa module utils \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11112](https\://github\.com/ansible\-collections/community\.general/pull/11112)\)\.
* ipa module utils \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11097](https\://github\.com/ansible\-collections/community\.general/pull/11097)\)\.
* ipa\_config \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11098](https\://github\.com/ansible\-collections/community\.general/pull/11098)\)\.
* ipa\_dnsrecord \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11098](https\://github\.com/ansible\-collections/community\.general/pull/11098)\)\.
* ipa\_dnszone \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11098](https\://github\.com/ansible\-collections/community\.general/pull/11098)\)\.
* ipa\_group \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11098](https\://github\.com/ansible\-collections/community\.general/pull/11098)\)\.
* ipa\_hbacrule \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11098](https\://github\.com/ansible\-collections/community\.general/pull/11098)\)\.
* ipa\_host \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11098](https\://github\.com/ansible\-collections/community\.general/pull/11098)\)\.
* ipa\_hostgroup \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11098](https\://github\.com/ansible\-collections/community\.general/pull/11098)\)\.
* ipa\_otpconfig \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11098](https\://github\.com/ansible\-collections/community\.general/pull/11098)\)\.
* ipa\_otptoken \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11098](https\://github\.com/ansible\-collections/community\.general/pull/11098)\)\.
* ipa\_pwpolicy \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11098](https\://github\.com/ansible\-collections/community\.general/pull/11098)\)\.
* ipa\_pwpolicy \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11106](https\://github\.com/ansible\-collections/community\.general/pull/11106)\)\.
* ipa\_role \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11098](https\://github\.com/ansible\-collections/community\.general/pull/11098)\)\.
* ipa\_service \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11098](https\://github\.com/ansible\-collections/community\.general/pull/11098)\)\.
* ipa\_subca \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11104](https\://github\.com/ansible\-collections/community\.general/pull/11104)\)\.
* ipa\_sudocmd \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11098](https\://github\.com/ansible\-collections/community\.general/pull/11098)\)\.
* ipa\_sudocmdgroup \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11098](https\://github\.com/ansible\-collections/community\.general/pull/11098)\)\.
* ipa\_sudorule \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11098](https\://github\.com/ansible\-collections/community\.general/pull/11098)\)\.
* ipa\_user \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11098](https\://github\.com/ansible\-collections/community\.general/pull/11098)\)\.
* ipa\_vault \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11098](https\://github\.com/ansible\-collections/community\.general/pull/11098)\)\.
* iptables\_state action plugin \- add type hints \([https\://github\.com/ansible\-collections/community\.general/pull/11167](https\://github\.com/ansible\-collections/community\.general/pull/11167)\)\.
* iso\_customize \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11106](https\://github\.com/ansible\-collections/community\.general/pull/11106)\)\.
* jail connection plugin \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11095](https\://github\.com/ansible\-collections/community\.general/pull/11095)\)\.
* jc filter plugin \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11095](https\://github\.com/ansible\-collections/community\.general/pull/11095)\)\.
* jenkins\_job \- simplify return of boolean values in functions \([https\://github\.com/ansible\-collections/community\.general/pull/11119](https\://github\.com/ansible\-collections/community\.general/pull/11119)\)\.
* jenkins\_job\_info \- remove conditional code handling SSL for unsupported versions of Python \([https\://github\.com/ansible\-collections/community\.general/pull/11078](https\://github\.com/ansible\-collections/community\.general/pull/11078)\)\.
* jenkins\_plugin \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11102](https\://github\.com/ansible\-collections/community\.general/pull/11102)\)\.
* jenkins\_plugin \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/1114](https\://github\.com/ansible\-collections/community\.general/pull/1114)\)\.
* jenkins\_plugin \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11097](https\://github\.com/ansible\-collections/community\.general/pull/11097)\)\.
* jenkins\_plugin modules \- replace <code>\%</code> templating with f\-strings or <code>format\(\)</code> \([https\://github\.com/ansible\-collections/community\.general/pull/11223](https\://github\.com/ansible\-collections/community\.general/pull/11223)\)\.
* jenkins\_script \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/1114](https\://github\.com/ansible\-collections/community\.general/pull/1114)\)\.
* jira \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11104](https\://github\.com/ansible\-collections/community\.general/pull/11104)\)\.
* jira \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/1114](https\://github\.com/ansible\-collections/community\.general/pull/1114)\)\.
* jira \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11097](https\://github\.com/ansible\-collections/community\.general/pull/11097)\)\.
* json\_query filter plugin \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11095](https\://github\.com/ansible\-collections/community\.general/pull/11095)\)\.
* keycloak module utils \- fix cases of unused variables in loops \([https\://github\.com/ansible\-collections/community\.general/pull/11115](https\://github\.com/ansible\-collections/community\.general/pull/11115)\)\.
* keycloak module utils \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11112](https\://github\.com/ansible\-collections/community\.general/pull/11112)\)\.
* keycloak module\_utils \- replace <code>\%</code> templating with f\-strings or <code>format\(\)</code> \([https\://github\.com/ansible\-collections/community\.general/pull/11223](https\://github\.com/ansible\-collections/community\.general/pull/11223)\)\.
* keycloak\_authentication \- fix cases of unused variables in loops \([https\://github\.com/ansible\-collections/community\.general/pull/11115](https\://github\.com/ansible\-collections/community\.general/pull/11115)\)\.
* keycloak\_client\_rolemapping \- fix cases of unused variables in loops \([https\://github\.com/ansible\-collections/community\.general/pull/11115](https\://github\.com/ansible\-collections/community\.general/pull/11115)\)\.
* keycloak\_component \- fix cases of unused variables in loops \([https\://github\.com/ansible\-collections/community\.general/pull/11115](https\://github\.com/ansible\-collections/community\.general/pull/11115)\)\.
* keycloak\_realm \- add <code>webAuthnPolicyPasswordlessPasskeysEnabled</code> parameter \([https\://github\.com/ansible\-collections/community\.general/pull/11197](https\://github\.com/ansible\-collections/community\.general/pull/11197)\)\.
* keycloak\_realm\_key \- fix cases of unused variables in loops \([https\://github\.com/ansible\-collections/community\.general/pull/11115](https\://github\.com/ansible\-collections/community\.general/pull/11115)\)\.
* keycloak\_realm\_rolemapping \- fix cases of unused variables in loops \([https\://github\.com/ansible\-collections/community\.general/pull/11115](https\://github\.com/ansible\-collections/community\.general/pull/11115)\)\.
* keycloak\_user\_rolemapping \- fix cases of unused variables in loops \([https\://github\.com/ansible\-collections/community\.general/pull/11115](https\://github\.com/ansible\-collections/community\.general/pull/11115)\)\.
* keycloak\_userprofile \- fix cases of unused variables in loops \([https\://github\.com/ansible\-collections/community\.general/pull/11115](https\://github\.com/ansible\-collections/community\.general/pull/11115)\)\.
* keys\_filter plugin\_utils plugin \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11095](https\://github\.com/ansible\-collections/community\.general/pull/11095)\)\.
* keys\_filter\.py plugin utils \- add type hints \([https\://github\.com/ansible\-collections/community\.general/pull/11167](https\://github\.com/ansible\-collections/community\.general/pull/11167)\)\.
* known\_hosts module utils \- improve code by using native Python construct \([https\://github\.com/ansible\-collections/community\.general/pull/11215](https\://github\.com/ansible\-collections/community\.general/pull/11215)\)\.
* layman \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11097](https\://github\.com/ansible\-collections/community\.general/pull/11097)\)\.
* ldap module utils \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11112](https\://github\.com/ansible\-collections/community\.general/pull/11112)\)\.
* ldap\_attrs \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11102](https\://github\.com/ansible\-collections/community\.general/pull/11102)\)\.
* ldap\_entry \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11102](https\://github\.com/ansible\-collections/community\.general/pull/11102)\)\.
* ldap\_inc \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11102](https\://github\.com/ansible\-collections/community\.general/pull/11102)\)\.
* ldap\_search \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11104](https\://github\.com/ansible\-collections/community\.general/pull/11104)\)\.
* ldap\_search \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11106](https\://github\.com/ansible\-collections/community\.general/pull/11106)\)\.
* linode inventory plugin \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11095](https\://github\.com/ansible\-collections/community\.general/pull/11095)\)\.
* listen\_ports\_facts \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11098](https\://github\.com/ansible\-collections/community\.general/pull/11098)\)\.
* listen\_ports\_facts \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11097](https\://github\.com/ansible\-collections/community\.general/pull/11097)\)\.
* lmdb\_kv lookup plugin \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11095](https\://github\.com/ansible\-collections/community\.general/pull/11095)\)\.
* locale\_gen \- extend the search for available locales to include <code>/usr/local/share/i18n/SUPPORTED</code> in Debian and Ubuntu systems \([https\://github\.com/ansible\-collections/community\.general/issues/10964](https\://github\.com/ansible\-collections/community\.general/issues/10964)\, [https\://github\.com/ansible\-collections/community\.general/pull/11046](https\://github\.com/ansible\-collections/community\.general/pull/11046)\)\.
* logentries \- simplify return of boolean values in functions \([https\://github\.com/ansible\-collections/community\.general/pull/11119](https\://github\.com/ansible\-collections/community\.general/pull/11119)\)\.
* lxc connection plugin \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11095](https\://github\.com/ansible\-collections/community\.general/pull/11095)\)\.
* lxd connection plugin \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11095](https\://github\.com/ansible\-collections/community\.general/pull/11095)\)\.
* lxd inventory plugin \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11095](https\://github\.com/ansible\-collections/community\.general/pull/11095)\)\.
* lxd module utils \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11112](https\://github\.com/ansible\-collections/community\.general/pull/11112)\)\.
* lxd module utils \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11097](https\://github\.com/ansible\-collections/community\.general/pull/11097)\)\.
* lxd\_container \- improve code by using native Python construct \([https\://github\.com/ansible\-collections/community\.general/pull/11215](https\://github\.com/ansible\-collections/community\.general/pull/11215)\)\.
* macports \- simplify return of boolean values in functions \([https\://github\.com/ansible\-collections/community\.general/pull/11119](https\://github\.com/ansible\-collections/community\.general/pull/11119)\)\.
* mail \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/1114](https\://github\.com/ansible\-collections/community\.general/pull/1114)\)\.
* maven\_artifact \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/1114](https\://github\.com/ansible\-collections/community\.general/pull/1114)\)\.
* merge\_variables \- extend type detection failure message to allow users for easier failure debugging \([https\://github\.com/ansible\-collections/community\.general/pull/11107](https\://github\.com/ansible\-collections/community\.general/pull/11107)\)\.
* merge\_variables lookup plugin \- simplify return of boolean values in functions \([https\://github\.com/ansible\-collections/community\.general/pull/11119](https\://github\.com/ansible\-collections/community\.general/pull/11119)\)\.
* modprobe \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11098](https\://github\.com/ansible\-collections/community\.general/pull/11098)\)\.
* net\_tools\.pritunl\.api module utils \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11097](https\://github\.com/ansible\-collections/community\.general/pull/11097)\)\.
* nmap inventory plugin \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11095](https\://github\.com/ansible\-collections/community\.general/pull/11095)\)\.
* nmcli \- fix cases of unused variables in loops \([https\://github\.com/ansible\-collections/community\.general/pull/11115](https\://github\.com/ansible\-collections/community\.general/pull/11115)\)\.
* nmcli \- fix comparison of type \([https\://github\.com/ansible\-collections/community\.general/pull/11121](https\://github\.com/ansible\-collections/community\.general/pull/11121)\)\.
* nmcli modules \- replace <code>\%</code> templating with f\-strings or <code>format\(\)</code> \([https\://github\.com/ansible\-collections/community\.general/pull/11223](https\://github\.com/ansible\-collections/community\.general/pull/11223)\)\.
* nomad\_job \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11098](https\://github\.com/ansible\-collections/community\.general/pull/11098)\)\.
* nomad\_job \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11106](https\://github\.com/ansible\-collections/community\.general/pull/11106)\)\.
* nomad\_job\_info \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11098](https\://github\.com/ansible\-collections/community\.general/pull/11098)\)\.
* nomad\_token \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11098](https\://github\.com/ansible\-collections/community\.general/pull/11098)\)\.
* nosh \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11106](https\://github\.com/ansible\-collections/community\.general/pull/11106)\)\.
* ocapi\_command \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11106](https\://github\.com/ansible\-collections/community\.general/pull/11106)\)\.
* ocapi\_command \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11110](https\://github\.com/ansible\-collections/community\.general/pull/11110)\)\.
* ocapi\_info \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11106](https\://github\.com/ansible\-collections/community\.general/pull/11106)\)\.
* ocapi\_utils module utils \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11112](https\://github\.com/ansible\-collections/community\.general/pull/11112)\)\.
* oci\_utils module utils \- improve code by using native Python construct \([https\://github\.com/ansible\-collections/community\.general/pull/11215](https\://github\.com/ansible\-collections/community\.general/pull/11215)\)\.
* oci\_utils module utils \- improve templating of strings \([https\://github\.com/ansible\-collections/community\.general/pull/11189](https\://github\.com/ansible\-collections/community\.general/pull/11189)\)\.
* oneandone\_firewall\_policy \- simplify return of boolean values in functions \([https\://github\.com/ansible\-collections/community\.general/pull/11119](https\://github\.com/ansible\-collections/community\.general/pull/11119)\)\.
* oneandone\_load\_balancer \- simplify return of boolean values in functions \([https\://github\.com/ansible\-collections/community\.general/pull/11119](https\://github\.com/ansible\-collections/community\.general/pull/11119)\)\.
* oneandone\_monitoring\_policy \- simplify return of boolean values in functions \([https\://github\.com/ansible\-collections/community\.general/pull/11119](https\://github\.com/ansible\-collections/community\.general/pull/11119)\)\.
* oneandone\_private\_network \- simplify return of boolean values in functions \([https\://github\.com/ansible\-collections/community\.general/pull/11119](https\://github\.com/ansible\-collections/community\.general/pull/11119)\)\.
* oneandone\_server \- replace <code>\%</code> templating with f\-strings or <code>format\(\)</code> \([https\://github\.com/ansible\-collections/community\.general/pull/11231](https\://github\.com/ansible\-collections/community\.general/pull/11231)\)\.
* oneandone\_server modules \- mark <code>\%</code> templating as <code>noqa</code> \([https\://github\.com/ansible\-collections/community\.general/pull/11223](https\://github\.com/ansible\-collections/community\.general/pull/11223)\)\.
* onepassword lookup plugin \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11095](https\://github\.com/ansible\-collections/community\.general/pull/11095)\)\.
* onepassword\_info \- execute external commands using Ansible construct \([https\://github\.com/ansible\-collections/community\.general/pull/11193](https\://github\.com/ansible\-collections/community\.general/pull/11193)\)\.
* onepassword\_info \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11102](https\://github\.com/ansible\-collections/community\.general/pull/11102)\)\.
* onepassword\_info \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/1114](https\://github\.com/ansible\-collections/community\.general/pull/1114)\)\.
* oneview module utils \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11112](https\://github\.com/ansible\-collections/community\.general/pull/11112)\)\.
* online inventory plugin \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11095](https\://github\.com/ansible\-collections/community\.general/pull/11095)\)\.
* opennebula inventory plugin \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11095](https\://github\.com/ansible\-collections/community\.general/pull/11095)\)\.
* opentelemetry callback plugin \- fix cases of unused variables in loops \([https\://github\.com/ansible\-collections/community\.general/pull/11115](https\://github\.com/ansible\-collections/community\.general/pull/11115)\)\.
* osx\_defaults \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11097](https\://github\.com/ansible\-collections/community\.general/pull/11097)\)\.
* packet\_device \- replace <code>\%</code> templating with f\-strings or <code>format\(\)</code> \([https\://github\.com/ansible\-collections/community\.general/pull/11231](https\://github\.com/ansible\-collections/community\.general/pull/11231)\)\.
* packet\_device modules \- mark <code>\%</code> templating as <code>noqa</code> \([https\://github\.com/ansible\-collections/community\.general/pull/11223](https\://github\.com/ansible\-collections/community\.general/pull/11223)\)\.
* packet\_ip\_subnet \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11097](https\://github\.com/ansible\-collections/community\.general/pull/11097)\)\.
* packet\_project \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11106](https\://github\.com/ansible\-collections/community\.general/pull/11106)\)\.
* packet\_sshkey \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11097](https\://github\.com/ansible\-collections/community\.general/pull/11097)\)\.
* packet\_volume \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11106](https\://github\.com/ansible\-collections/community\.general/pull/11106)\)\.
* packet\_volume \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/1114](https\://github\.com/ansible\-collections/community\.general/pull/1114)\)\.
* pamd \- simplify return of boolean values in functions \([https\://github\.com/ansible\-collections/community\.general/pull/11119](https\://github\.com/ansible\-collections/community\.general/pull/11119)\)\.
* parted \- simplify return of boolean values in functions \([https\://github\.com/ansible\-collections/community\.general/pull/11119](https\://github\.com/ansible\-collections/community\.general/pull/11119)\)\.
* passwordstore lookup plugin \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11095](https\://github\.com/ansible\-collections/community\.general/pull/11095)\)\.
* pear \- fix cases of unused variables in loops \([https\://github\.com/ansible\-collections/community\.general/pull/11115](https\://github\.com/ansible\-collections/community\.general/pull/11115)\)\.
* pids \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11098](https\://github\.com/ansible\-collections/community\.general/pull/11098)\)\.
* pids \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11097](https\://github\.com/ansible\-collections/community\.general/pull/11097)\)\.
* portage \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11106](https\://github\.com/ansible\-collections/community\.general/pull/11106)\)\.
* pritunl\_org \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11098](https\://github\.com/ansible\-collections/community\.general/pull/11098)\)\.
* pritunl\_org\_info \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11098](https\://github\.com/ansible\-collections/community\.general/pull/11098)\)\.
* pritunl\_user \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11098](https\://github\.com/ansible\-collections/community\.general/pull/11098)\)\.
* pritunl\_user\_info \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11098](https\://github\.com/ansible\-collections/community\.general/pull/11098)\)\.
* pushbullet modules \- replace <code>\%</code> templating with f\-strings or <code>format\(\)</code> \([https\://github\.com/ansible\-collections/community\.general/pull/11223](https\://github\.com/ansible\-collections/community\.general/pull/11223)\)\.
* read\_csv \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11098](https\://github\.com/ansible\-collections/community\.general/pull/11098)\)\.
* redfish\_command \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11110](https\://github\.com/ansible\-collections/community\.general/pull/11110)\)\.
* redfish\_command \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/1114](https\://github\.com/ansible\-collections/community\.general/pull/1114)\)\.
* redfish\_config \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11110](https\://github\.com/ansible\-collections/community\.general/pull/11110)\)\.
* redfish\_config \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/1114](https\://github\.com/ansible\-collections/community\.general/pull/1114)\)\.
* redfish\_utils module utils \- fix cases of unused variables in loops \([https\://github\.com/ansible\-collections/community\.general/pull/11115](https\://github\.com/ansible\-collections/community\.general/pull/11115)\)\.
* redfish\_utils module utils \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11112](https\://github\.com/ansible\-collections/community\.general/pull/11112)\)\.
* redhat\_subscription \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11106](https\://github\.com/ansible\-collections/community\.general/pull/11106)\)\.
* redhat\_subscription \- simplify return of boolean values in functions \([https\://github\.com/ansible\-collections/community\.general/pull/11119](https\://github\.com/ansible\-collections/community\.general/pull/11119)\)\.
* redis cache plugin \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11095](https\://github\.com/ansible\-collections/community\.general/pull/11095)\)\.
* redis lookup plugin \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11095](https\://github\.com/ansible\-collections/community\.general/pull/11095)\)\.
* revbitspss lookup plugin \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11095](https\://github\.com/ansible\-collections/community\.general/pull/11095)\)\.
* rhevm \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11097](https\://github\.com/ansible\-collections/community\.general/pull/11097)\)\.
* riak \- simplify return of boolean values in functions \([https\://github\.com/ansible\-collections/community\.general/pull/11119](https\://github\.com/ansible\-collections/community\.general/pull/11119)\)\.
* rundeck module utils \- improve handling the return value <code>exception</code>\. It now contains the full stack trace of the exception\, while the message is included in <code>msg</code> \([https\://github\.com/ansible\-collections/community\.general/pull/11149](https\://github\.com/ansible\-collections/community\.general/pull/11149)\)\.
* scaleway inventory plugin \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11095](https\://github\.com/ansible\-collections/community\.general/pull/11095)\)\.
* scaleway\_user\_data modules \- replace <code>\%</code> templating with f\-strings or <code>format\(\)</code> \([https\://github\.com/ansible\-collections/community\.general/pull/11223](https\://github\.com/ansible\-collections/community\.general/pull/11223)\)\.
* selinux\_permissive \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11098](https\://github\.com/ansible\-collections/community\.general/pull/11098)\)\.
* sensu\_check \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11098](https\://github\.com/ansible\-collections/community\.general/pull/11098)\)\.
* sensu\_silence \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/1114](https\://github\.com/ansible\-collections/community\.general/pull/1114)\)\.
* sensu\_silence modules \- replace <code>\%</code> templating with f\-strings or <code>format\(\)</code> \([https\://github\.com/ansible\-collections/community\.general/pull/11223](https\://github\.com/ansible\-collections/community\.general/pull/11223)\)\.
* sensu\_subscription \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11098](https\://github\.com/ansible\-collections/community\.general/pull/11098)\)\.
* sensu\_subscription \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11102](https\://github\.com/ansible\-collections/community\.general/pull/11102)\)\.
* shelvefile lookup plugin \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11095](https\://github\.com/ansible\-collections/community\.general/pull/11095)\)\.
* shutdown action plugin \- add type hints \([https\://github\.com/ansible\-collections/community\.general/pull/11167](https\://github\.com/ansible\-collections/community\.general/pull/11167)\)\.
* shutdown action plugin \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11095](https\://github\.com/ansible\-collections/community\.general/pull/11095)\)\.
* slack \- simplify return of boolean values in functions \([https\://github\.com/ansible\-collections/community\.general/pull/11119](https\://github\.com/ansible\-collections/community\.general/pull/11119)\)\.
* slackpkg \- simplify return of boolean values in functions \([https\://github\.com/ansible\-collections/community\.general/pull/11119](https\://github\.com/ansible\-collections/community\.general/pull/11119)\)\.
* snap \- improve templating of strings \([https\://github\.com/ansible\-collections/community\.general/pull/11189](https\://github\.com/ansible\-collections/community\.general/pull/11189)\)\.
* snmp\_facts \- simplify and improve code using standard Ansible validations \([https\://github\.com/ansible\-collections/community\.general/pull/11148](https\://github\.com/ansible\-collections/community\.general/pull/11148)\)\.
* solaris\_zone \- execute external commands using Ansible construct \([https\://github\.com/ansible\-collections/community\.general/pull/11192](https\://github\.com/ansible\-collections/community\.general/pull/11192)\)\.
* solaris\_zone \- simplify return of boolean values in functions \([https\://github\.com/ansible\-collections/community\.general/pull/11119](https\://github\.com/ansible\-collections/community\.general/pull/11119)\)\.
* spectrum\_model\_attrs \- convert <code>\%</code> templating to f\-string \([https\://github\.com/ansible\-collections/community\.general/pull/11229](https\://github\.com/ansible\-collections/community\.general/pull/11229)\)\.
* statusio\_maintenance \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11102](https\://github\.com/ansible\-collections/community\.general/pull/11102)\)\.
* sudoers \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11098](https\://github\.com/ansible\-collections/community\.general/pull/11098)\)\.
* svc \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/1114](https\://github\.com/ansible\-collections/community\.general/pull/1114)\)\.
* svr4pkg \- simplify return of boolean values in functions \([https\://github\.com/ansible\-collections/community\.general/pull/11119](https\://github\.com/ansible\-collections/community\.general/pull/11119)\)\.
* swupd \- simplify return of boolean values in functions \([https\://github\.com/ansible\-collections/community\.general/pull/11119](https\://github\.com/ansible\-collections/community\.general/pull/11119)\)\.
* to\_ini filter plugin \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11095](https\://github\.com/ansible\-collections/community\.general/pull/11095)\)\.
* tss lookup plugin \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11095](https\://github\.com/ansible\-collections/community\.general/pull/11095)\)\.
* univention\_umc module utils \- update code to Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/11122](https\://github\.com/ansible\-collections/community\.general/pull/11122)\)\.
* unsafe\.py plugin utils \- add type hints \([https\://github\.com/ansible\-collections/community\.general/pull/11167](https\://github\.com/ansible\-collections/community\.general/pull/11167)\)\.
* urpmi \- simplify return of boolean values in functions \([https\://github\.com/ansible\-collections/community\.general/pull/11119](https\://github\.com/ansible\-collections/community\.general/pull/11119)\)\.
* utm\_aaa\_group \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11098](https\://github\.com/ansible\-collections/community\.general/pull/11098)\)\.
* utm\_aaa\_group\_info \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11098](https\://github\.com/ansible\-collections/community\.general/pull/11098)\)\.
* utm\_ca\_host\_key\_cert \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11098](https\://github\.com/ansible\-collections/community\.general/pull/11098)\)\.
* utm\_ca\_host\_key\_cert\_info \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11098](https\://github\.com/ansible\-collections/community\.general/pull/11098)\)\.
* utm\_dns\_host \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11098](https\://github\.com/ansible\-collections/community\.general/pull/11098)\)\.
* utm\_network\_interface\_address \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11098](https\://github\.com/ansible\-collections/community\.general/pull/11098)\)\.
* utm\_network\_interface\_address\_info \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11098](https\://github\.com/ansible\-collections/community\.general/pull/11098)\)\.
* utm\_proxy\_auth\_profile \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11098](https\://github\.com/ansible\-collections/community\.general/pull/11098)\)\.
* utm\_proxy\_exception \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11098](https\://github\.com/ansible\-collections/community\.general/pull/11098)\)\.
* utm\_proxy\_frontend \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11098](https\://github\.com/ansible\-collections/community\.general/pull/11098)\)\.
* utm\_proxy\_frontend\_info \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11098](https\://github\.com/ansible\-collections/community\.general/pull/11098)\)\.
* utm\_proxy\_location \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11098](https\://github\.com/ansible\-collections/community\.general/pull/11098)\)\.
* utm\_proxy\_location\_info \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11098](https\://github\.com/ansible\-collections/community\.general/pull/11098)\)\.
* utm\_utils module utils \- improve code by using native Python construct \([https\://github\.com/ansible\-collections/community\.general/pull/11215](https\://github\.com/ansible\-collections/community\.general/pull/11215)\)\.
* utm\_utils module utils \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11112](https\://github\.com/ansible\-collections/community\.general/pull/11112)\)\.
* vertica\_configuration \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11098](https\://github\.com/ansible\-collections/community\.general/pull/11098)\)\.
* vertica\_configuration \- simplify return of boolean values in functions \([https\://github\.com/ansible\-collections/community\.general/pull/11119](https\://github\.com/ansible\-collections/community\.general/pull/11119)\)\.
* vertica\_info \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11098](https\://github\.com/ansible\-collections/community\.general/pull/11098)\)\.
* vertica\_role \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11098](https\://github\.com/ansible\-collections/community\.general/pull/11098)\)\.
* vertica\_role \- simplify return of boolean values in functions \([https\://github\.com/ansible\-collections/community\.general/pull/11119](https\://github\.com/ansible\-collections/community\.general/pull/11119)\)\.
* vertica\_schema \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11098](https\://github\.com/ansible\-collections/community\.general/pull/11098)\)\.
* vertica\_schema \- simplify return of boolean values in functions \([https\://github\.com/ansible\-collections/community\.general/pull/11119](https\://github\.com/ansible\-collections/community\.general/pull/11119)\)\.
* vertica\_schema \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11097](https\://github\.com/ansible\-collections/community\.general/pull/11097)\)\.
* vertica\_user \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11098](https\://github\.com/ansible\-collections/community\.general/pull/11098)\)\.
* vertica\_user \- simplify return of boolean values in functions \([https\://github\.com/ansible\-collections/community\.general/pull/11119](https\://github\.com/ansible\-collections/community\.general/pull/11119)\)\.
* vertica\_user \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11097](https\://github\.com/ansible\-collections/community\.general/pull/11097)\)\.
* virtualbox inventory plugin \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11095](https\://github\.com/ansible\-collections/community\.general/pull/11095)\)\.
* vmadm \- in case of failure\, the module no longer returns the stderr output as <code>exception</code>\, but instead as <code>stderr</code>\. Other information \(<code>stdout</code>\, <code>rc</code>\) is now also returned \([https\://github\.com/ansible\-collections/community\.general/pull/11149](https\://github\.com/ansible\-collections/community\.general/pull/11149)\)\.
* vmadm \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11102](https\://github\.com/ansible\-collections/community\.general/pull/11102)\)\.
* wakeonlan \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11098](https\://github\.com/ansible\-collections/community\.general/pull/11098)\)\.
* wdc\_redfish\_command \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11110](https\://github\.com/ansible\-collections/community\.general/pull/11110)\)\.
* wdc\_redfish\_command \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/1114](https\://github\.com/ansible\-collections/community\.general/pull/1114)\)\.
* wdc\_redfish\_info \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11110](https\://github\.com/ansible\-collections/community\.general/pull/11110)\)\.
* wdc\_redfish\_info \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/1114](https\://github\.com/ansible\-collections/community\.general/pull/1114)\)\.
* wsl connection plugin \- adjust variable name for integration tests \([https\://github\.com/ansible\-collections/community\.general/pull/11190](https\://github\.com/ansible\-collections/community\.general/pull/11190)\)\.
* wsl connection plugin \- fix cases of unused variables in loops \([https\://github\.com/ansible\-collections/community\.general/pull/11115](https\://github\.com/ansible\-collections/community\.general/pull/11115)\)\.
* wsl connection plugin \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11095](https\://github\.com/ansible\-collections/community\.general/pull/11095)\)\.
* xbps \- fix cases of unused variables in loops \([https\://github\.com/ansible\-collections/community\.general/pull/11115](https\://github\.com/ansible\-collections/community\.general/pull/11115)\)\.
* xbps \- simplify return of boolean values in functions \([https\://github\.com/ansible\-collections/community\.general/pull/11119](https\://github\.com/ansible\-collections/community\.general/pull/11119)\)\.
* xcc\_redfish\_command \- fix cases of unused variables in loops \([https\://github\.com/ansible\-collections/community\.general/pull/11115](https\://github\.com/ansible\-collections/community\.general/pull/11115)\)\.
* xcc\_redfish\_command \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11110](https\://github\.com/ansible\-collections/community\.general/pull/11110)\)\.
* xcc\_redfish\_command \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/1114](https\://github\.com/ansible\-collections/community\.general/pull/1114)\)\.
* xenserver module utils \- improve code by using native Python construct \([https\://github\.com/ansible\-collections/community\.general/pull/11215](https\://github\.com/ansible\-collections/community\.general/pull/11215)\)\.
* xenserver module utils \- simplify return of boolean values in functions \([https\://github\.com/ansible\-collections/community\.general/pull/11119](https\://github\.com/ansible\-collections/community\.general/pull/11119)\)\.
* xenserver\_guest modules \- replace <code>\%</code> templating with f\-strings or <code>format\(\)</code> \([https\://github\.com/ansible\-collections/community\.general/pull/11223](https\://github\.com/ansible\-collections/community\.general/pull/11223)\)\.
* xml \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11106](https\://github\.com/ansible\-collections/community\.general/pull/11106)\)\.
* xml \- simplify return of boolean values in functions \([https\://github\.com/ansible\-collections/community\.general/pull/11119](https\://github\.com/ansible\-collections/community\.general/pull/11119)\)\.
* yum\_versionlock \- remove redundant conversion to unicode in command output \([https\://github\.com/ansible\-collections/community\.general/pull/11093](https\://github\.com/ansible\-collections/community\.general/pull/11093)\)\.
* zfs \- simplify return of boolean values in functions \([https\://github\.com/ansible\-collections/community\.general/pull/11119](https\://github\.com/ansible\-collections/community\.general/pull/11119)\)\.
* zone connection plugin \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11095](https\://github\.com/ansible\-collections/community\.general/pull/11095)\)\.

<a id="community-postgresql"></a>
#### community\.postgresql

* postgresql\_privs \- support MAINTAIN privilege on tables \(added in PostgreSQL 17\) \([https\://github\.com/ansible\-collections/community\.postgresql/pull/888](https\://github\.com/ansible\-collections/community\.postgresql/pull/888)\)\.

<a id="community-routeros-9"></a>
#### community\.routeros

* api\_info\, api\_modify \- add missing attribute <code>radsec\-timeout</code> for the <code>radius</code> path which exists since RouterOS version 7\.19\.6 \([https\://github\.com/ansible\-collections/community\.routeros/pull/412](https\://github\.com/ansible\-collections/community\.routeros/pull/412)\)\.
* api\_info\, api\_modify \- add support for path <code>interface dot1x client</code> \([https\://github\.com/ansible\-collections/community\.routeros/pull/414](https\://github\.com/ansible\-collections/community\.routeros/pull/414)\)\.
* api\_info\, api\_modify \- add support for path <code>interface dot1x server</code> \([https\://github\.com/ansible\-collections/community\.routeros/pull/413](https\://github\.com/ansible\-collections/community\.routeros/pull/413)\)\.
* api\_info\, api\_modify \- add support for paths <code>ip hotspot</code>\, <code>ip hotspot profile</code>\, <code>ip hotspot user</code>\, <code>ip hotspot user profile</code>\, <code>ip hotspot walled\-garden</code>\, and <code>ip hotspot walled\-garden ip</code> \([https\://github\.com/ansible\-collections/community\.routeros/pull/418](https\://github\.com/ansible\-collections/community\.routeros/pull/418)\)\.
* api\_info\, api\_modify \- allow the <code>fib</code> parameter to be disabled for the <code>routing table</code> path \([https\://github\.com/ansible\-collections/community\.routeros/issues/368](https\://github\.com/ansible\-collections/community\.routeros/issues/368)\, [https\://github\.com/ansible\-collections/community\.routeros/pull/417](https\://github\.com/ansible\-collections/community\.routeros/pull/417)\)\.
* api\_info\, api\_modify \- remove primary key constraint on \'peer\' for path <code>ip ipsec identity</code> \([https\://github\.com/ansible\-collections/community\.routeros/pull/421](https\://github\.com/ansible\-collections/community\.routeros/pull/421)\)\.

<a id="community-windows"></a>
#### community\.windows

* Add official support for Ansible 2\.20

<a id="google-cloud-4"></a>
#### google\.cloud

* gcp\_alloydb\_\* \- added gcp\_alloydb\_cluster\, gcp\_alloydb\_instance\, gcp\_alloydb\_backup\, and gcp\_alloydb\_user modules \([https\://github\.com/ansible\-collections/google\.cloud/pull/722](https\://github\.com/ansible\-collections/google\.cloud/pull/722)\)

<a id="hetzner-hcloud-5"></a>
#### hetzner\.hcloud

* DNS support is now generally available\.
* load\_balancer\_network \- Add <code>ip\_range</code> argument to attach a load balancer to a specific subnet\.
* server\_network \- Add <code>ip\_range</code> argument to attach a load balancer to a specific subnet\.
* txt\_record \- Add new txt\_record filter to help format TXT \, e\.g\. <code>\"\{\{ \'v\=spf1 include\:\_spf\.example\.net \~all\' \| hetzner\.hcloud\.txt\_record \}\}\"</code>\.

<a id="hitachivantara-vspone-block-3"></a>
#### hitachivantara\.vspone\_block

* Added a new \"hv\_sds\_block\_encryption\_environment\_setting\_facts\" module to retrieve encryption environment configuration settings from VSP One SDS Block and Cloud systems\.
* Added a new \"hv\_sds\_block\_encryption\_environment\_settings\" module to enable or disable encryption functionality on VSP One SDS Block and Cloud systems\.
* Added a new \"hv\_sds\_block\_encryption\_key\" module to create and delete encryption keys on VSP One SDS Block and Cloud systems\.
* Added a new \"hv\_sds\_block\_encryption\_key\_count\_facts\" module to retrieve information about the number of encryption keys from VSP One SDS Block and Cloud systems\.
* Added a new \"hv\_sds\_block\_encryption\_key\_facts\" module to retrieve detailed information about encryption keys from VSP One SDS Block and Cloud systems\.
* Added a new \"hv\_sds\_block\_protection\_domain\" module to manage protection domains including creation\, modification\, and data relocation operations on VSP One SDS Block and Cloud systems\.
* Added a new \"hv\_sds\_block\_remote\_path\_group\" module to create remote path group\, add remote path to a remote path group\, remove remote path from remote path group\, and delete remote path group on VSP One SDS Block systems\.
* Added a new \"hv\_sds\_block\_remote\_path\_group\_facts\" module to retrieve information about remote path groups from VSP One SDS Block systems\.
* Added a new \"hv\_sds\_block\_session\" module to generate and discard session on VSP One SDS Block and Cloud systems\.
* Added a new \"hv\_sds\_block\_session\_facts\" module to retrieve information about sessions on VSP One SDS Block and Cloud systems\.
* Added a new \"hv\_sds\_block\_snmp\_settings\" module to manage SNMP settings including agent enablement\, version configuration\, trap settings\, authentication settings\, and system group information on VSP One SDS Block and Cloud systems\.
* Added a new \"hv\_sds\_block\_snmp\_settings\_facts\" module to retrieve SNMP settings including agent status\, version configuration\, trap settings\, authentication settings\, and system group information from VSP One SDS Block and Cloud systems\.
* Added a new \"hv\_sds\_block\_spare\_node\" module to manage spare node configuration including node identification\, fault domain assignment\, network configuration\, and BMC settings on VSP One SDS Block and Cloud systems\.
* Added a new \"hv\_sds\_block\_spare\_node\_facts\" module to retrieves spare node information and configuration details from VSP One SDS Block and Cloud systems\.
* Added a new \"hv\_sds\_block\_storage\_system\" module to manage storage system configuration including certificate management\, cache settings\, and other system\-level configurations on VSP One SDS Block and Cloud systems\.
* Added a new \"hv\_sds\_block\_user\_group\" module to Create and update user groups on VSP One SDS Block and Cloud systems\.
* Added a new \"hv\_sds\_block\_user\_group\_facts\" module to retrieve user groups from VSP One SDS Block and Cloud systems\.
* Added a new \"hv\_sds\_block\_web\_server\" module to manages the web server access setting for VSP One SDS Block and Cloud systems\.
* Added a new \"hv\_sds\_block\_web\_server\_facts\" module to retrieve the web server access setting from VSP One SDS Block and Cloud systems\.
* Added support for latest software version 01\.18\.02 for VSP One SDS Block and Cloud systems\.
* Added support to \"Add user to user groups\" to hv\_sds\_block\_user module\.
* Added support to \"Delete a user\" to hv\_sds\_block\_user module\.
* Added support to \"Disable encryption for storage pool using ID\" to hv\_sds\_block\_storage\_pool module\.
* Added support to \"Disable encryption for storage pool\" to hv\_sds\_block\_storage\_pool module\.
* Added support to \"Enable encryption for storage pool by ID\" to hv\_sds\_block\_storage\_pool module\.
* Added support to \"Enable encryption for storage pool by name\" to hv\_sds\_block\_storage\_pool module\.
* Added support to \"Remove user from user groups\" to hv\_sds\_block\_user module\.
* Added support to \"Update user settings\" to hv\_sds\_block\_user module\.

<a id="hitachivantara-vspone-object"></a>
#### hitachivantara\.vspone\_object

* Enhanced <em class="title-reference">hv\_storage\_component</em> module to support storage components of type ARRAY for VSP One B20 series storage systems\.

<a id="microsoft-ad"></a>
#### microsoft\.ad

* Add official support for Ansible 2\.20

<a id="microsoft-iis"></a>
#### microsoft\.iis

* Add official support for Ansible 2\.20

<a id="purestorage-flasharray-2"></a>
#### purestorage\.flasharray

* purefa\_connection \- Add new parameters for key refresh and connection refresh\, as well as ability to update existing connection
* purefa\_info \- Added more data to hostgroup volume information to support NVMe connections
* purefa\_info \- Added tags info to entities that support them
* purefa\_network \- Addressed issues found in update\_interface
* purefa\_phonehome \- Added <code>excludes</code> parameter\, supported from Purity//FA 6\.10\.0
* purefa\_pod \- Fixed pydantic issue from lastest SDK version
* purefa\_policy \- Added Continuous Availability support for SMB policies

<a id="telekom-mms-icinga-director"></a>
#### telekom\_mms\.icinga\_director

* Feat\: add some parameters to the icinga service module \([https\://github\.com/telekom\-mms/ansible\-collection\-icinga\-director/pull/289](https\://github\.com/telekom\-mms/ansible\-collection\-icinga\-director/pull/289)\)

<a id="vmware-vmware-5"></a>
#### vmware\.vmware

* content\_library\_item\_info \- Add item storage information to item result
* esxi\_hosts \- Added option to rename reserved variables to avoid potential conflicts with ansible\-core and resolve warnings\. fixes [https\://github\.com/ansible\-collections/vmware\.vmware/issues/273](https\://github\.com/ansible\-collections/vmware\.vmware/issues/273)
* module\_deploy\_vm\_base \- Removed redundant code by using new vm placement service methods in deploy modules
* vm \- Add module to manage virtual machines
* vm\_apply\_customization \- Added module to apply different customization specs to a VM
* vms \- Added option to rename reserved variables to avoid potential conflicts with ansible\-core and resolve warnings\. fixes [https\://github\.com/ansible\-collections/vmware\.vmware/issues/273](https\://github\.com/ansible\-collections/vmware\.vmware/issues/273)

<a id="deprecated-features-5"></a>
### Deprecated Features

* The <code>junipernetworks\.junos</code> collection has been deprecated\.
  It will be removed from Ansible 14 if no one starts maintaining it again before Ansible 14\.
  See [Collections Removal Process for unmaintained collections](https\://docs\.ansible\.com/projects/ansible/devel/community/collection\_contributors/collection\_package\_removal\.html\#unmaintained\-collections) for more details \([https\://forum\.ansible\.com/t/44869](https\://forum\.ansible\.com/t/44869)\)\.

<a id="community-general-17"></a>
#### community\.general

* cloud module utils \- this module utils is not used by community\.general and will thus be removed from community\.general 13\.0\.0\. If you are using it from another collection\, please copy it over \([https\://github\.com/ansible\-collections/community\.general/pull/11205](https\://github\.com/ansible\-collections/community\.general/pull/11205)\)\.
* database module utils \- this module utils is not used by community\.general and will thus be removed from community\.general 13\.0\.0\. If you are using it from another collection\, please copy it over \([https\://github\.com/ansible\-collections/community\.general/pull/11205](https\://github\.com/ansible\-collections/community\.general/pull/11205)\)\.
* dconf \- deprecate fallback mechanism when <code>gi\.repository</code> is not available\; fallback will be removed in community\.general 15\.0\.0 \([https\://github\.com/ansible\-collections/community\.general/pull/11088](https\://github\.com/ansible\-collections/community\.general/pull/11088)\)\.
* known\_hosts module utils \- this module utils is not used by community\.general and will thus be removed from community\.general 13\.0\.0\. If you are using it from another collection\, please copy it over \([https\://github\.com/ansible\-collections/community\.general/pull/11205](https\://github\.com/ansible\-collections/community\.general/pull/11205)\)\.
* layman \- ClearLinux was made EOL in July 2025\.\; the module will be removed from community\.general 15\.0\.0 \([https\://github\.com/ansible\-collections/community\.general/pull/11087](https\://github\.com/ansible\-collections/community\.general/pull/11087)\)\.
* layman \- Gentoo deprecated <code>layman</code> in mid\-2023\; the module will be removed from community\.general 14\.0\.0 \([https\://github\.com/ansible\-collections/community\.general/pull/11070](https\://github\.com/ansible\-collections/community\.general/pull/11070)\)\.
* pushbullet \- module relies on Python package supporting Python 3\.2 only\; the module will be removed from community\.general 13\.0\.0 \([https\://github\.com/ansible\-collections/community\.general/pull/11224](https\://github\.com/ansible\-collections/community\.general/pull/11224)\)\.
* saslprep module utils \- this module utils is not used by community\.general and will thus be removed from community\.general 13\.0\.0\. If you are using it from another collection\, please copy it over \([https\://github\.com/ansible\-collections/community\.general/pull/11205](https\://github\.com/ansible\-collections/community\.general/pull/11205)\)\.
* spotinst\_aws\_elastigroup \- module relies on Python package supporting Python 2\.7 only\; the module will be removed from community\.general 13\.0\.0 \([https\://github\.com/ansible\-collections/community\.general/pull/11069](https\://github\.com/ansible\-collections/community\.general/pull/11069)\)\.

<a id="bugfixes-5"></a>
### Bugfixes

<a id="ansible-core-14"></a>
#### Ansible\-core

* Fix <code>AnsibleModule\.human\_to\_bytes\(\)</code>\, which was never adjusted after the standalone <code>human\_to\_bytes\(\)</code> got a new parameter <code>default\_unit</code> \([https\://github\.com/ansible/ansible/pull/85259](https\://github\.com/ansible/ansible/pull/85259)\)\.
* Variable loading now uses file source instead of variables when invalidly formmated vars file is loaded\.
* ansible\-test \- The runtime\-metadata sanity test now ignores pre\-release and build identifiers in collection versions\. This prevents errors if a tombstone version is <code>X\.0\.0</code>\, while the collection\'s version is <code>X\.0\.0\-prerelease</code> \([https\://github\.com/ansible/ansible/issues/85193](https\://github\.com/ansible/ansible/issues/85193)\)\.\"
* display \- Fix <code>getuser</code> fallback error handling on Python 3\.13 and later\. \([https\://github\.com/ansible/ansible/issues/86142](https\://github\.com/ansible/ansible/issues/86142)\)
* first\_found \- Correct the \"Include tasks only if one of the files exists\, otherwise skip\" example\.
* get\_url \- fix regex for GNU Digest line which is used in comparing checksums \([https\://github\.com/ansible/ansible/issues/86132](https\://github\.com/ansible/ansible/issues/86132)\)\.
* local connection \- Fix <code>getuser</code> fallback error handling on Python 3\.13 and later\.

<a id="ansible-netcommon-6"></a>
#### ansible\.netcommon

* Added support for private key passphrase in libssh connection plugin\, when using encrypted private keys specified by the C\(ansible\_private\_key\_file\) attribute\.
* Avoid legacy imports deprecated in ansible\-core 2\.20 \([https\://github\.com/ansible\-collections/ansible\.netcommon/pull/720](https\://github\.com/ansible\-collections/ansible\.netcommon/pull/720)\)\.
* Avoid merging module\_defaults for all ansible\.netcommon\.grpc\_\* modules\.
* Set libssh logging level to DEBUG when Ansible verbosity is greater than 3\, to aid in troubleshooting connection issues\.

<a id="ansible-windows-5"></a>
#### ansible\.windows

* Update various action plugin calls to avoid some deprecated or old methods\.
* win\_get\_url \- Fix force\=no not doing HEAD request if checksum is not set
* win\_powershell \- Fix up async support for Ansible 2\.19 when running <code>win\_powershell</code> \- [https\://github\.com/ansible\-collections/ansible\.windows/issues/828](https\://github\.com/ansible\-collections/ansible\.windows/issues/828)
* win\_reboot \- Use full path to <code>shutdown\.exe</code> to avoid relying on <code>PATH</code> lookups to find \- [https\://github\.com/ansible\-collections/ansible\.windows/issues/826](https\://github\.com/ansible\-collections/ansible\.windows/issues/826)

<a id="cisco-aci-1"></a>
#### cisco\.aci

* Fix allowed ranges of interface option in aci\_interface\_config module\.
* Fix descriptions of options in aci\_maintenance\_policy\.
* Fix querying description in aci\_l4l7\_service\_graph\_template\.

<a id="cisco-meraki-5"></a>
#### cisco\.meraki

* administered\_licensing\_subscription\_subscriptions\_bind \- Fixed parameter naming from \'subscription\_id\' to \'subscriptionId\' for proper API compatibility
* meraki\.py plugin utils \- Added type checking in has\_diff\_elem2 function to prevent errors when comparing lists of non\-dictionary elements
* networks\_appliance\_content\_filtering \- Enhanced idempotency by extracting category IDs from blockedUrlCategories before comparison

<a id="cisco-mso-3"></a>
#### cisco\.mso

* Fix updates of multicast\_route\_map\_policy in mso\_schema\_template\_vrf\_rp\.
* Fix updates of multicast\_route\_map\_source\_filter and multicast\_route\_map\_destination\_filter in mso\_schema\_template\_bd\.

<a id="cisco-nxos-3"></a>
#### cisco\.nxos

* cisco\.nxos\.nxos\_facts \- Fix handling of facts for httapi type connection\.
* cisco\.nxos\.nxos\_hsrp\_interfaces \- Fix parsers for preempt and priority
* cisco\.nxos\.nxos\_l2\_interfaces \- Fix cdp\_enable config parsing\.
* cisco\.nxos\.nxos\_l3\_interfaces \- Improved the code logic for handling redirects\.
* cisco\.nxos\.nxos\_snmp\_server \- fixed communities parsing issue
* cisco\.nxos\.nxos\_static\_routes \- Fix facts parser to filter inline VRF routes from global route collection preventing incorrect VRF route deletion\.

<a id="community-dns-6"></a>
#### community\.dns

* Update Public Suffix List\.

<a id="community-docker-4"></a>
#### community\.docker

* CLI\-based modules \- when parsing JSON output fails\, also provide standard error output\. Also provide information on the command and its result in machine\-readable way \([https\://github\.com/ansible\-collections/community\.docker/issues/1216](https\://github\.com/ansible\-collections/community\.docker/issues/1216)\, [https\://github\.com/ansible\-collections/community\.docker/pull/1221](https\://github\.com/ansible\-collections/community\.docker/pull/1221)\)\.
* Docker CLI based modules \- work around bug in Docker 29\.0\.0 that caused a breaking change in <code>docker version \-\-format json</code> output \([https\://github\.com/ansible\-collections/community\.docker/issues/1185](https\://github\.com/ansible\-collections/community\.docker/issues/1185)\, [https\://github\.com/ansible\-collections/community\.docker/pull/1187](https\://github\.com/ansible\-collections/community\.docker/pull/1187)\)\.
* docker\_compose\_v2\, docker\_compose\_v2\_pull \- adjust parsing from image pull events to changes in Docker Compose 5\.0\.0 \([https\://github\.com/ansible\-collections/community\.docker/pull/1219](https\://github\.com/ansible\-collections/community\.docker/pull/1219)\)\.
* docker\_container \- fix <code>pull</code> idempotency with Docker 29\.0\.0 \([https\://github\.com/ansible\-collections/community\.docker/pull/1192](https\://github\.com/ansible\-collections/community\.docker/pull/1192)\)\.
* docker\_container \- fix handling of exposed port ranges\. So far\, the module used an undocumented feature of Docker that was removed from Docker 29\.0\.0\, that allowed to pass the range to the deamon and let handle it\. Now the module explodes ranges into a list of all contained ports\, same as the Docker CLI does\. For backwards compatibility with Docker \< 29\.0\.0\, it also explodes ranges returned by the API for existing containers so that comparison should only indicate a difference if the ranges actually change \([https\://github\.com/ansible\-collections/community\.docker/pull/1192](https\://github\.com/ansible\-collections/community\.docker/pull/1192)\)\.
* docker\_container \- fix idempotency for IPv6 addresses with Docker 29\.0\.0 \([https\://github\.com/ansible\-collections/community\.docker/pull/1192](https\://github\.com/ansible\-collections/community\.docker/pull/1192)\)\.
* docker\_container \- when the same port is mapped more than once for the same protocol without specifying an interface\, a bug caused an invalid value to be passed for the interface \([https\://github\.com/ansible\-collections/community\.docker/issues/1213](https\://github\.com/ansible\-collections/community\.docker/issues/1213)\, [https\://github\.com/ansible\-collections/community\.docker/pull/1214](https\://github\.com/ansible\-collections/community\.docker/pull/1214)\)\.
* docker\_image \- fix <code>source\=pull</code> idempotency with Docker 29\.0\.0 \([https\://github\.com/ansible\-collections/community\.docker/pull/1192](https\://github\.com/ansible\-collections/community\.docker/pull/1192)\)\.
* docker\_image\, docker\_image\_push \- adjust image push detection to Docker 29 \([https\://github\.com/ansible\-collections/community\.docker/pull/1199](https\://github\.com/ansible\-collections/community\.docker/pull/1199)\)\.
* docker\_image\_pull \- fix idempotency with Docker 29\.0\.0 \([https\://github\.com/ansible\-collections/community\.docker/pull/1192](https\://github\.com/ansible\-collections/community\.docker/pull/1192)\)\.
* docker\_network \- fix idempotency for IPv6 addresses and networks with Docker 29\.0\.0 \([https\://github\.com/ansible\-collections/community\.docker/pull/1201](https\://github\.com/ansible\-collections/community\.docker/pull/1201)\)\.

<a id="community-general-18"></a>
#### community\.general

* \_filelock module utils \- add type hints\. Fix bug if <code>set\_lock\(\)</code> is called with <code>lock\_timeout\=None</code> \([https\://github\.com/ansible\-collections/community\.general/pull/11222](https\://github\.com/ansible\-collections/community\.general/pull/11222)\)\.
* aix\_filesystem \- remove compatibility code for ancient Python versions \([https\://github\.com/ansible\-collections/community\.general/pull/11232](https\://github\.com/ansible\-collections/community\.general/pull/11232)\)\.
* ansible\_type plugin utils \- avoid potential concatenation of non\-strings when <code>alias</code> has non\-string values \([https\://github\.com/ansible\-collections/community\.general/pull/11167](https\://github\.com/ansible\-collections/community\.general/pull/11167)\)\.
* ansible\_type test plugin \- fix parameter checking \([https\://github\.com/ansible\-collections/community\.general/pull/11167](https\://github\.com/ansible\-collections/community\.general/pull/11167)\)\.
* cobbler\_system \- compare the version as a float which is the type returned by the Cobbler API \([https\://github\.com/ansible\-collections/community\.general/issues/11044](https\://github\.com/ansible\-collections/community\.general/issues/11044)\)\.
* datetime module utils \- fix bug in <code>fromtimestamp\(\)</code> that caused the function to crash\. This function is not used in community\.general \([https\://github\.com/ansible\-collections/community\.general/pull/11206](https\://github\.com/ansible\-collections/community\.general/pull/11206)\)\.
* gitlab module utils \- add type hints\. Pass API version to python\-gitlab as string and not as integer \([https\://github\.com/ansible\-collections/community\.general/pull/11222](https\://github\.com/ansible\-collections/community\.general/pull/11222)\)\.
* homebrew\_service \- slightly refactor code \([https\://github\.com/ansible\-collections/community\.general/pull/11168](https\://github\.com/ansible\-collections/community\.general/pull/11168)\)\.
* ipinfoio\_facts \- fix handling of HTTP errors consulting the service \([https\://github\.com/ansible\-collections/community\.general/pull/11145](https\://github\.com/ansible\-collections/community\.general/pull/11145)\)\.
* keys\_filter\.py plugin utils \- fixed requirements check so that other sequences than lists and strings are checked\, and corrected broken formatting during error reporting \([https\://github\.com/ansible\-collections/community\.general/pull/11167](https\://github\.com/ansible\-collections/community\.general/pull/11167)\)\.
* mas \- parse CLI output correctly when listing installed apps with mas 3\.0\.0\+ \([https\://github\.com/ansible\-collections/community\.general/pull/11179](https\://github\.com/ansible\-collections/community\.general/pull/11179)\)\.
* pam\_limits \- remove <code>\%</code> templating no longer used in f\-string \([https\://github\.com/ansible\-collections/community\.general/pull/11229](https\://github\.com/ansible\-collections/community\.general/pull/11229)\)\.
* xcc\_redfish\_command \- fix templating of dictionary keys as list \([https\://github\.com/ansible\-collections/community\.general/pull/11144](https\://github\.com/ansible\-collections/community\.general/pull/11144)\)\.
* zfs \- mark change correctly when updating properties whose current value differs\, even if they already have a non\-default value \([https\://github\.com/ansible\-collections/community\.general/issues/11019](https\://github\.com/ansible\-collections/community\.general/issues/11019)\, [https\://github\.com/ansible\-collections/community\.general/pull/11172](https\://github\.com/ansible\-collections/community\.general/pull/11172)\)\.

<a id="community-postgresql-1"></a>
#### community\.postgresql

* postgresql\_db \- Fix connection limit not being set when value is \"0\" \([https\://github\.com/ansible\-collections/community\.postgresql/issues/879](https\://github\.com/ansible\-collections/community\.postgresql/issues/879)\)\.
* postgresql\_db \- fixed <code>session\_role</code> parameter that was being ignored for raw connections \([https\://github\.com/ansible\-collections/community\.postgresql/pull/865](https\://github\.com/ansible\-collections/community\.postgresql/pull/865)\)
* postgresql\_db \- restoring from <code>\.sql</code> files would execute the file twice\. The module now avoids using both <code>\-\-file</code> and stdin redirection simultaneously \([https\://github\.com/ansible\-collections/community\.postgresql/issues/882](https\://github\.com/ansible\-collections/community\.postgresql/issues/882)\)\.

<a id="community-routeros-10"></a>
#### community\.routeros

* api\_modify\, api\_info \- in the <code>routing bgp connection</code> and <code>bgp templates</code> paths\, fix spelling of the <code>output\.remove\-private\-as</code> parameter \([https\://github\.com/ansible\-collections/community\.routeros/issues/415](https\://github\.com/ansible\-collections/community\.routeros/issues/415)\, [https\://github\.com/ansible\-collections/community\.routeros/pull/416](https\://github\.com/ansible\-collections/community\.routeros/pull/416)\)\.
* api\_modify\, api\_info \- in the <code>routing bgp instance</code> path\, fix \'Cannot add new entry to this path\' error \([https\://github\.com/ansible\-collections/community\.routeros/issues/409](https\://github\.com/ansible\-collections/community\.routeros/issues/409)\, [https\://github\.com/ansible\-collections/community\.routeros/pull/420](https\://github\.com/ansible\-collections/community\.routeros/pull/420)\)\.
* api\_modify\, api\_info \- in the <code>routing bgp templates</code> path\, remove <code>address\-families</code> for RouterOS 7\.19\+ \([https\://github\.com/ansible\-collections/community\.routeros/issues/415](https\://github\.com/ansible\-collections/community\.routeros/issues/415)\, [https\://github\.com/ansible\-collections/community\.routeros/pull/416](https\://github\.com/ansible\-collections/community\.routeros/pull/416)\)\.
* api\_modify\, api\_info \- in the <code>routing bgp templates</code> path\, remove <code>router\-id</code> for RouterOS 7\.20\+ \([https\://github\.com/ansible\-collections/community\.routeros/issues/415](https\://github\.com/ansible\-collections/community\.routeros/issues/415)\, [https\://github\.com/ansible\-collections/community\.routeros/pull/416](https\://github\.com/ansible\-collections/community\.routeros/pull/416)\)\.
* api\_modify\, api\_info \- in the <code>routing bgp templates</code> path\, support <code>afi</code> \(RouterOS 7\.19\+\) \(RouterOS 7\.19 and before\) \([https\://github\.com/ansible\-collections/community\.routeros/issues/415](https\://github\.com/ansible\-collections/community\.routeros/issues/415)\, [https\://github\.com/ansible\-collections/community\.routeros/pull/416](https\://github\.com/ansible\-collections/community\.routeros/pull/416)\)\.

<a id="community-windows-1"></a>
#### community\.windows

* Unify the TLS protocol handling logic for the modules that need it to ensure they use the configured OS policies\.
* win\_disk\_facts \- fixed an issue when a disk may not have a number \([https\://github\.com/ansible\-collections/community\.windows/pull/652](https\://github\.com/ansible\-collections/community\.windows/pull/652)\)\.
* win\_initialize\_disk \- disks that are formatted but offline cannot be brought online without erasing them \([https\://github\.com/ansible\-collections/community\.windows/issues/149](https\://github\.com/ansible\-collections/community\.windows/issues/149)\)\.
* win\_psmodule \- Improve error message\, if a module exists in multiple repositories \- [https\://github\.com/ansible\-collections/community\.windows/issues/641](https\://github\.com/ansible\-collections/community\.windows/issues/641)
* win\_psrepository\_copy \- Fix idempotence check to not rely on \.NET runtime implementation details\. This should avoid any false positive changed indicators

<a id="google-cloud-5"></a>
#### google\.cloud

* Fix runtime\.yml to correctly note Ansible 2\.17 minimum version \([https\://github\.com/ansible\-collections/google\.cloud/pull/730](https\://github\.com/ansible\-collections/google\.cloud/pull/730)\)
* Revert removal of Ansible 2\.16 support \([https\://github\.com/ansible\-collections/google\.cloud/pull/734](https\://github\.com/ansible\-collections/google\.cloud/pull/734)\)
* gcp\_secret\_manager \- return the secret value as type <em class="title-reference">str</em> rather than <em class="title-reference">bytes</em> \([https\://github\.com/ansible\-collections/google\.cloud/pull/721](https\://github\.com/ansible\-collections/google\.cloud/pull/721)\)

<a id="hetzner-hcloud-6"></a>
#### hetzner\.hcloud

* firewall \- Ensure idempotency when using non canonical ipv6 representation in Firewall rules\.
* zone\_rrset \- Records order is not guaranteed\, the module will not generate a diff if the order of records changes\.
* zone\_rrset \- Records without comments will not generate a diff anymore\.

<a id="hitachivantara-vspone-block-4"></a>
#### hitachivantara\.vspone\_block

* Resolved issue during GAD pair creation when resource lock is enabled\.
* Resolved issue with quorum disk creation on VSP One Block 85 storage systems\.
* Resolved issue with remote connection creation on VSP One Block 85 storage systems\.
* Resolved issue with storage system facts retrieval module for VSP One Block 85 storage systems\.
* Various additional bug fixes and enhancements for VSP One Block 85 storage systems\.
* Various additional bug fixes and enhancements for VSP One storage systems and VSP One SDS Block storage systems\.

<a id="inspur-ispim"></a>
#### inspur\.ispim

* Edit ansible devel version tests to our CI test scripts  \([https\://github\.com/ispim/inspur\.ispim/pull/39](https\://github\.com/ispim/inspur\.ispim/pull/39)\)\.
* Modify the automated tests and add support for version 2\.18\. \([https\://github\.com/ispim/inspur\.ispim/pull/40](https\://github\.com/ispim/inspur\.ispim/pull/40)\)\.
* Modify the automated tests and add support for version 2\.18\. \([https\://github\.com/ispim/inspur\.ispim/pull/45](https\://github\.com/ispim/inspur\.ispim/pull/45)\)\.
* Modify the ism\.py file in the module\_utils directory\, and change the reference path of iteritems to be a reference from within Python\. \([https\://github\.com/ispim/inspur\.ispim/pull/46](https\://github\.com/ispim/inspur\.ispim/pull/46)\)\.

<a id="microsoft-ad-1"></a>
#### microsoft\.ad

* microsoft\.ad\.domain\_child \- Fix return document key so it displays when using the standard Ansible documentation tools\.
* microsoft\.ad\.ldap \- Fix issue where auth\_protocol config option was never used when creating the spnego client\.
* microsoft\.ad\.service\_account \- Fix return document key so it displays when using the standard Ansible documentation tools\.

<a id="microsoft-iis-1"></a>
#### microsoft\.iis

* website\_info \- Fix error when retrieving website information but none exist \- [https\://github\.com/ansible\-collections/microsoft\.iis/issues/44](https\://github\.com/ansible\-collections/microsoft\.iis/issues/44)

<a id="purestorage-flasharray-3"></a>
#### purestorage\.flasharray

* purefa\_info \- Resolves issue with hosthgroup info when NVMe connected volumes are in a hostgroup

<a id="telekom-mms-icinga-director-1"></a>
#### telekom\_mms\.icinga\_director

* Fix diff in check mode by normalising the boolean values \([https\://github\.com/telekom\-mms/ansible\-collection\-icinga\-director/pull/295](https\://github\.com/telekom\-mms/ansible\-collection\-icinga\-director/pull/295)\)
* Fix doc generation and remove need for iteritems \([https\://github\.com/telekom\-mms/ansible\-collection\-icinga\-director/pull/296](https\://github\.com/telekom\-mms/ansible\-collection\-icinga\-director/pull/296)\)
* Fix\: remove default for states parameter in icinga\_dependency\_apply \([https\://github\.com/telekom\-mms/ansible\-collection\-icinga\-director/pull/290](https\://github\.com/telekom\-mms/ansible\-collection\-icinga\-director/pull/290)\)

<a id="vmware-vmware-6"></a>
#### vmware\.vmware

* Fix issue where modules that used the proxy\_host and proxy\_port arguments were ignoring these arguments when initializing clients\. \([https\://github\.com/ansible\-collections/vmware\.vmware/issues/259](https\://github\.com/ansible\-collections/vmware\.vmware/issues/259)\)
* Updated common VM deployment module docs to mention that name or MOID can be used for the resource pool\, cluster\, datastore\, and datastore cluster parameters\. This allows users to work around issues where the name is not unique\. Fixes [https\://github\.com/ansible\-collections/vmware\.vmware/issues/239](https\://github\.com/ansible\-collections/vmware\.vmware/issues/239)
* deploy\_content\_library\_ovf \- Remove invalid storage provisioning option \'eagerzeroedthick\' from module\'s argument spec\. \(Fixes [https\://github\.com/ansible\-collections/vmware\.vmware/issues/278](https\://github\.com/ansible\-collections/vmware\.vmware/issues/278)\)

<a id="known-issues-2"></a>
### Known Issues

<a id="community-docker-5"></a>
#### community\.docker

* docker\_image\, docker\_image\_export \- idempotency for archiving images depends on whether the image IDs used by the image storage backend correspond to the IDs used in the tarball\'s <code>manifest\.json</code> files\. The new default backend in Docker 29 apparently uses image IDs that no longer correspond\, whence idempotency no longer works \([https\://github\.com/ansible\-collections/community\.docker/pull/1199](https\://github\.com/ansible\-collections/community\.docker/pull/1199)\)\.

<a id="new-modules-5"></a>
### New Modules

<a id="cisco-aci-2"></a>
#### cisco\.aci

* cisco\.aci\.aci\_fabric\_node\_decommission \- Manage the Commissioning and Decommissioning of the Fabric Node \(fabric\:RsDecommissionNode\)
* cisco\.aci\.aci\_management\_network\_instance\_profile \- Manage external management network instance profiles \(mgmt\:InstP\)\.
* cisco\.aci\.aci\_management\_network\_instance\_profile\_to\_contract \- Bind Consumed Contract to External Management Network Instance Profiles \(mgmt\:RsOoBCons\)
* cisco\.aci\.aci\_switch\_access\_config \- Manage Switch Access Policy Configuration of Leaf and Spine nodes \(infra\:NodeConfig\)\.
* cisco\.aci\.aci\_switch\_fabric\_config \- Manage Switch Fabric Policy Configuration of Leaf and Spine nodes \(fabric\:NodeConfig\)\.

<a id="cisco-mso-4"></a>
#### cisco\.mso

* cisco\.mso\.ndo\_l3out\_floating\_svi\_interface \- Manage L3Out Floating SVI Interfaces on Cisco Nexus Dashboard Orchestrator \(NDO\)\.
* cisco\.mso\.ndo\_l3out\_floating\_svi\_interface\_path\_attributes \- Manage L3Out Floating SVI Interface Path Attributes on Cisco Nexus Dashboard Orchestrator \(NDO\)\.
* cisco\.mso\.ndo\_l3out\_secondary\_ip \- Manage L3Out Secondary IP Address on Cisco Nexus Dashboard Orchestrator \(NDO\)\.
* cisco\.mso\.ndo\_l3out\_svi\_interface \- Manage L3Out SVI Interfaces on Cisco Nexus Dashboard Orchestrator \(NDO\)\.
* cisco\.mso\.ndo\_match\_rule\_community\_term \- Manage Match Community Terms on Cisco Nexus Dashboard Orchestrator \(NDO\)\.
* cisco\.mso\.ndo\_match\_rule\_policy \- Manage Match Rule Policies on Cisco Nexus Dashboard Orchestrator \(NDO\)\.
* cisco\.mso\.ndo\_match\_rule\_prefix \- Manage Match Prefix List on Cisco Nexus Dashboard Orchestrator \(NDO\)\.
* cisco\.mso\.ndo\_route\_map\_policy\_route\_control \- Manage Route Map Policy for Route Control on Cisco Nexus Dashboard Orchestrator \(NDO\)\.
* cisco\.mso\.ndo\_route\_map\_policy\_route\_control\_context \- Manage Route Map Policy for Route Control Context on Cisco Nexus Dashboard Orchestrator \(NDO\)\.
* cisco\.mso\.ndo\_set\_rule\_policy \- Manage Tenant Set Rule Policies on Cisco Nexus Dashboard Orchestrator \(NDO\)\.

<a id="community-general-19"></a>
#### community\.general

* community\.general\.file\_remove \- Remove files matching a pattern from a directory\.
* community\.general\.lxd\_storage\_pool\_info \- Retrieve information about LXD storage pools\.
* community\.general\.lxd\_storage\_volume\_info \- Retrieve information about LXD storage volumes\.

<a id="hitachivantara-vspone-block-5"></a>
#### hitachivantara\.vspone\_block

<a id="sds-block-1"></a>
##### Sds Block

* hitachivantara\.vspone\_block\.hv\_sds\_block\_encryption\_environment\_setting\_facts \- Retrieves encryption environment settings from VSP One SDS Block and Cloud systems\.
* hitachivantara\.vspone\_block\.hv\_sds\_block\_encryption\_environment\_settings \- Manages encryption environment settings on VSP One SDS Block and Cloud systems\.
* hitachivantara\.vspone\_block\.hv\_sds\_block\_encryption\_key \- Manage encryption keys on VSP One SDS Block and Cloud systems\.
* hitachivantara\.vspone\_block\.hv\_sds\_block\_encryption\_key\_count\_facts \- Get encryption key count information from VSP One SDS Block and Cloud systems\.
* hitachivantara\.vspone\_block\.hv\_sds\_block\_encryption\_key\_facts \- Retrieves encryption key information from VSP One SDS Block and Cloud systems\.
* hitachivantara\.vspone\_block\.hv\_sds\_block\_remote\_path\_group \- Manages remote path groups on VSP One SDS Block and Cloud systems\.
* hitachivantara\.vspone\_block\.hv\_sds\_block\_remote\_path\_group\_facts \- Get information about remote path groups from VSP One SDS Block and Cloud systems\.
* hitachivantara\.vspone\_block\.hv\_sds\_block\_session \- Manages sessions on VSP One SDS Block and Cloud systems\.
* hitachivantara\.vspone\_block\.hv\_sds\_block\_session\_facts \- Retrieves information about sessions on VSP One SDS Block and Cloud systems\.
* hitachivantara\.vspone\_block\.hv\_sds\_block\_user\_group \- Create and update user groups on the storage system\.
* hitachivantara\.vspone\_block\.hv\_sds\_block\_web\_server \- Manages the web server access setting for VSP One SDS Block and Cloud systems\.
* hitachivantara\.vspone\_block\.hv\_sds\_block\_web\_server\_facts \- Get the web server access setting from VSP One SDS Block and Cloud systems\.

<a id="unchanged-collections-5"></a>
### Unchanged Collections

* amazon\.aws \(still version 10\.1\.2\)
* ansible\.posix \(still version 2\.1\.0\)
* ansible\.utils \(still version 6\.0\.0\)
* arista\.eos \(still version 12\.0\.0\)
* awx\.awx \(still version 24\.6\.1\)
* chocolatey\.chocolatey \(still version 1\.5\.3\)
* cisco\.ios \(still version 11\.1\.1\)
* cisco\.iosxr \(still version 12\.1\.0\)
* cisco\.ucs \(still version 1\.16\.0\)
* cloudscale\_ch\.cloud \(still version 2\.5\.2\)
* community\.aws \(still version 10\.0\.0\)
* community\.ciscosmb \(still version 1\.0\.11\)
* community\.crypto \(still version 3\.0\.5\)
* community\.grafana \(still version 2\.3\.0\)
* community\.hashi\_vault \(still version 7\.1\.0\)
* community\.hrobot \(still version 2\.7\.0\)
* community\.library\_inventory\_filtering\_v1 \(still version 1\.1\.5\)
* community\.libvirt \(still version 2\.0\.0\)
* community\.mongodb \(still version 1\.7\.10\)
* community\.mysql \(still version 4\.0\.1\)
* community\.okd \(still version 5\.0\.0\)
* community\.proxmox \(still version 1\.4\.0\)
* community\.proxysql \(still version 1\.7\.0\)
* community\.rabbitmq \(still version 1\.6\.0\)
* community\.sap\_libs \(still version 1\.5\.0\)
* community\.sops \(still version 2\.2\.7\)
* community\.vmware \(still version 6\.1\.0\)
* community\.zabbix \(still version 4\.1\.1\)
* containers\.podman \(still version 1\.18\.0\)
* cyberark\.pas \(still version 1\.0\.36\)
* dellemc\.enterprise\_sonic \(still version 3\.2\.0\)
* dellemc\.openmanage \(still version 10\.0\.1\)
* dellemc\.powerflex \(still version 3\.0\.0\)
* dellemc\.unity \(still version 2\.1\.0\)
* f5networks\.f5\_modules \(still version 1\.39\.0\)
* fortinet\.fortimanager \(still version 2\.11\.0\)
* fortinet\.fortios \(still version 2\.4\.2\)
* grafana\.grafana \(still version 6\.0\.6\)
* ibm\.storage\_virtualize \(still version 3\.1\.0\)
* ieisystem\.inmanage \(still version 4\.0\.0\)
* infinidat\.infinibox \(still version 1\.6\.3\)
* infoblox\.nios\_modules \(still version 1\.8\.0\)
* junipernetworks\.junos \(still version 11\.0\.0\)
* kaytus\.ksmanage \(still version 2\.0\.0\)
* kubernetes\.core \(still version 6\.2\.0\)
* kubevirt\.core \(still version 2\.2\.3\)
* lowlydba\.sqlserver \(still version 2\.7\.0\)
* netapp\.cloudmanager \(still version 21\.24\.0\)
* netapp\.ontap \(still version 23\.2\.0\)
* netapp\.storagegrid \(still version 21\.15\.0\)
* netapp\_eseries\.santricity \(still version 1\.4\.1\)
* netbox\.netbox \(still version 3\.21\.0\)
* ngine\_io\.cloudstack \(still version 3\.0\.0\)
* openstack\.cloud \(still version 2\.5\.0\)
* ovirt\.ovirt \(still version 3\.2\.1\)
* purestorage\.flashblade \(still version 1\.22\.0\)
* ravendb\.ravendb \(still version 1\.0\.4\)
* splunk\.es \(still version 4\.0\.0\)
* theforeman\.foreman \(still version 5\.7\.0\)
* vmware\.vmware\_rest \(still version 4\.9\.0\)
* vultr\.cloud \(still version 1\.13\.0\)
* vyos\.vyos \(still version 6\.0\.0\)
* wti\.remote \(still version 1\.0\.10\)

<a id="v13-0-0"></a>
## v13\.0\.0

- <a href="#release-summary-6">Release Summary</a>
- <a href="#removed-collections">Removed Collections</a>
- <a href="#added-collections-2">Added Collections</a>
- <a href="#ansible-core-15">Ansible\-core</a>
- <a href="#included-collections">Included Collections</a>
- <a href="#major-changes-6">Major Changes</a>
    - <a href="#ansible-core-16">Ansible\-core</a>
    - <a href="#community-vmware-2">community\.vmware</a>
    - <a href="#containers-podman-9">containers\.podman</a>
    - <a href="#dellemc-openmanage-3">dellemc\.openmanage</a>
    - <a href="#fortinet-fortios-4">fortinet\.fortios</a>
    - <a href="#grafana-grafana">grafana\.grafana</a>
    - <a href="#ieisystem-inmanage">ieisystem\.inmanage</a>
    - <a href="#ngine-io-cloudstack">ngine\_io\.cloudstack</a>
- <a href="#minor-changes-6">Minor Changes</a>
    - <a href="#ansible-core-17">Ansible\-core</a>
    - <a href="#check-point-mgmt">check\_point\.mgmt</a>
    - <a href="#cisco-dnac-3">cisco\.dnac</a>
    - <a href="#cisco-ios-5">cisco\.ios</a>
    - <a href="#cisco-iosxr-3">cisco\.iosxr</a>
    - <a href="#community-dns-7">community\.dns</a>
    - <a href="#community-docker-6">community\.docker</a>
    - <a href="#community-general-20">community\.general</a>
    - <a href="#community-hashi-vault">community\.hashi\_vault</a>
    - <a href="#community-hrobot-1">community\.hrobot</a>
    - <a href="#community-mysql-4">community\.mysql</a>
    - <a href="#community-proxmox-9">community\.proxmox</a>
    - <a href="#community-proxysql">community\.proxysql</a>
    - <a href="#community-routeros-11">community\.routeros</a>
    - <a href="#community-sap-libs-2">community\.sap\_libs</a>
    - <a href="#community-sops-1">community\.sops</a>
    - <a href="#community-vmware-3">community\.vmware</a>
    - <a href="#community-zabbix-2">community\.zabbix</a>
    - <a href="#containers-podman-10">containers\.podman</a>
    - <a href="#dellemc-enterprise-sonic">dellemc\.enterprise\_sonic</a>
    - <a href="#dellemc-openmanage-4">dellemc\.openmanage</a>
    - <a href="#dellemc-powerflex">dellemc\.powerflex</a>
    - <a href="#fortinet-fortimanager-5">fortinet\.fortimanager</a>
    - <a href="#fortinet-fortios-5">fortinet\.fortios</a>
    - <a href="#google-cloud-6">google\.cloud</a>
    - <a href="#hetzner-hcloud-7">hetzner\.hcloud</a>
    - <a href="#hitachivantara-vspone-block-6">hitachivantara\.vspone\_block</a>
    - <a href="#ibm-storage-virtualize-4">ibm\.storage\_virtualize</a>
    - <a href="#kubernetes-core-4">kubernetes\.core</a>
    - <a href="#netapp-ontap-7">netapp\.ontap</a>
    - <a href="#purestorage-flasharray-4">purestorage\.flasharray</a>
    - <a href="#purestorage-flashblade-3">purestorage\.flashblade</a>
    - <a href="#theforeman-foreman-5">theforeman\.foreman</a>
    - <a href="#vmware-vmware-7">vmware\.vmware</a>
- <a href="#breaking-changes--porting-guide-1">Breaking Changes / Porting Guide</a>
    - <a href="#ansible-core-18">Ansible\-core</a>
    - <a href="#community-docker-7">community\.docker</a>
    - <a href="#community-general-21">community\.general</a>
    - <a href="#community-mysql-5">community\.mysql</a>
    - <a href="#community-vmware-4">community\.vmware</a>
    - <a href="#hetzner-hcloud-8">hetzner\.hcloud</a>
    - <a href="#ibm-storage-virtualize-5">ibm\.storage\_virtualize</a>
- <a href="#deprecated-features-6">Deprecated Features</a>
    - <a href="#ansible-core-19">Ansible\-core</a>
    - <a href="#community-general-22">community\.general</a>
    - <a href="#community-hrobot-2">community\.hrobot</a>
    - <a href="#community-vmware-5">community\.vmware</a>
    - <a href="#community-zabbix-3">community\.zabbix</a>
    - <a href="#dellemc-powerflex-1">dellemc\.powerflex</a>
    - <a href="#hetzner-hcloud-9">hetzner\.hcloud</a>
    - <a href="#purestorage-flasharray-5">purestorage\.flasharray</a>
- <a href="#removed-features-previously-deprecated">Removed Features \(previously deprecated\)</a>
    - <a href="#ansible-core-20">Ansible\-core</a>
    - <a href="#community-docker-8">community\.docker</a>
    - <a href="#community-general-23">community\.general</a>
    - <a href="#community-vmware-6">community\.vmware</a>
- <a href="#security-fixes-2">Security Fixes</a>
    - <a href="#community-general-24">community\.general</a>
- <a href="#bugfixes-6">Bugfixes</a>
    - <a href="#ansible-core-21">Ansible\-core</a>
    - <a href="#amazon-aws-6">amazon\.aws</a>
    - <a href="#cisco-ios-6">cisco\.ios</a>
    - <a href="#cisco-meraki-6">cisco\.meraki</a>
    - <a href="#community-crypto-4">community\.crypto</a>
    - <a href="#community-dns-8">community\.dns</a>
    - <a href="#community-docker-9">community\.docker</a>
    - <a href="#community-general-25">community\.general</a>
    - <a href="#community-hrobot-3">community\.hrobot</a>
    - <a href="#community-library-inventory-filtering-v1">community\.library\_inventory\_filtering\_v1</a>
    - <a href="#community-mysql-6">community\.mysql</a>
    - <a href="#community-proxmox-10">community\.proxmox</a>
    - <a href="#community-routeros-12">community\.routeros</a>
    - <a href="#community-sops-2">community\.sops</a>
    - <a href="#community-vmware-7">community\.vmware</a>
    - <a href="#community-zabbix-4">community\.zabbix</a>
    - <a href="#containers-podman-11">containers\.podman</a>
    - <a href="#dellemc-enterprise-sonic-1">dellemc\.enterprise\_sonic</a>
    - <a href="#dellemc-openmanage-5">dellemc\.openmanage</a>
    - <a href="#fortinet-fortimanager-6">fortinet\.fortimanager</a>
    - <a href="#fortinet-fortios-6">fortinet\.fortios</a>
    - <a href="#google-cloud-7">google\.cloud</a>
    - <a href="#hetzner-hcloud-10">hetzner\.hcloud</a>
    - <a href="#ibm-storage-virtualize-6">ibm\.storage\_virtualize</a>
    - <a href="#ieisystem-inmanage-1">ieisystem\.inmanage</a>
    - <a href="#kubernetes-core-5">kubernetes\.core</a>
    - <a href="#netapp-ontap-8">netapp\.ontap</a>
    - <a href="#ngine-io-cloudstack-1">ngine\_io\.cloudstack</a>
    - <a href="#purestorage-flasharray-6">purestorage\.flasharray</a>
    - <a href="#purestorage-flashblade-4">purestorage\.flashblade</a>
    - <a href="#vmware-vmware-8">vmware\.vmware</a>
- <a href="#known-issues-3">Known Issues</a>
    - <a href="#ansible-core-22">Ansible\-core</a>
    - <a href="#community-sops-3">community\.sops</a>
    - <a href="#dellemc-openmanage-6">dellemc\.openmanage</a>
- <a href="#new-plugins-3">New Plugins</a>
    - <a href="#callback-1">Callback</a>
    - <a href="#filter-2">Filter</a>
    - <a href="#inventory">Inventory</a>
    - <a href="#lookup">Lookup</a>
- <a href="#new-modules-6">New Modules</a>
    - <a href="#check-point-mgmt-1">check\_point\.mgmt</a>
    - <a href="#community-general-26">community\.general</a>
    - <a href="#community-proxmox-11">community\.proxmox</a>
    - <a href="#community-proxysql-1">community\.proxysql</a>
    - <a href="#containers-podman-12">containers\.podman</a>
    - <a href="#dellemc-enterprise-sonic-2">dellemc\.enterprise\_sonic</a>
    - <a href="#dellemc-powerflex-2">dellemc\.powerflex</a>
    - <a href="#hitachivantara-vspone-block-7">hitachivantara\.vspone\_block</a>
    - <a href="#ibm-storage-virtualize-7">ibm\.storage\_virtualize</a>
    - <a href="#ieisystem-inmanage-2">ieisystem\.inmanage</a>
    - <a href="#ngine-io-cloudstack-2">ngine\_io\.cloudstack</a>
    - <a href="#purestorage-flashblade-5">purestorage\.flashblade</a>
    - <a href="#theforeman-foreman-6">theforeman\.foreman</a>
- <a href="#unchanged-collections-6">Unchanged Collections</a>

<a id="release-summary-6"></a>
### Release Summary

Release Date\: 2025\-11\-19

[Porting Guide](https\://docs\.ansible\.com/projects/ansible/devel/porting\_guides\.html)

<a id="removed-collections"></a>
### Removed Collections

* community\.digitalocean \(previously included version\: 1\.27\.0\)
* ibm\.qradar \(previously included version\: 4\.0\.0\)

You can still install a removed collection manually with <code>ansible\-galaxy collection install \<name\-of\-collection\></code>\.

<a id="added-collections-2"></a>
### Added Collections

* hitachivantara\.vspone\_object \(version 1\.0\.0\)
* ravendb\.ravendb \(version 1\.0\.4\)

<a id="ansible-core-15"></a>
### Ansible\-core

Ansible 13\.0\.0 contains ansible\-core version 2\.20\.0\.
This is a newer version than version 2\.19\.1 contained in the previous Ansible release\.

The changes are reported in the combined changelog below\.

<a id="included-collections"></a>
### Included Collections

If not mentioned explicitly\, the changes are reported in the combined changelog below\.

| Collection                               | Ansible 12.0.0 | Ansible 13.0.0 | Notes                                                                                                                                                                                                        |
| ---------------------------------------- | -------------- | -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| amazon.aws                               | 10.1.1         | 10.1.2         |                                                                                                                                                                                                              |
| azure.azcollection                       | 3.8.0          | 3.10.1         | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.                                                                                 |
| check_point.mgmt                         | 6.4.1          | 6.6.0          |                                                                                                                                                                                                              |
| cisco.dnac                               | 6.39.0         | 6.41.0         |                                                                                                                                                                                                              |
| cisco.intersight                         | 2.2.0          | 2.7.0          | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.                                                                                 |
| cisco.ios                                | 11.0.0         | 11.1.1         |                                                                                                                                                                                                              |
| cisco.iosxr                              | 12.0.0         | 12.1.0         |                                                                                                                                                                                                              |
| cisco.meraki                             | 2.21.4         | 2.21.8         |                                                                                                                                                                                                              |
| community.crypto                         | 3.0.3          | 3.0.5          |                                                                                                                                                                                                              |
| community.dns                            | 3.3.2          | 3.4.0          |                                                                                                                                                                                                              |
| community.docker                         | 4.7.0          | 5.0.1          |                                                                                                                                                                                                              |
| community.general                        | 11.2.1         | 12.0.1         |                                                                                                                                                                                                              |
| community.hashi_vault                    | 7.0.0          | 7.1.0          |                                                                                                                                                                                                              |
| community.hrobot                         | 2.5.0          | 2.7.0          |                                                                                                                                                                                                              |
| community.library_inventory_filtering_v1 | 1.1.1          | 1.1.5          |                                                                                                                                                                                                              |
| community.mysql                          | 3.15.0         | 4.0.1          |                                                                                                                                                                                                              |
| community.proxmox                        | 1.3.0          | 1.4.0          |                                                                                                                                                                                                              |
| community.proxysql                       | 1.6.0          | 1.7.0          |                                                                                                                                                                                                              |
| community.routeros                       | 3.10.0         | 3.13.0         |                                                                                                                                                                                                              |
| community.sap_libs                       | 1.4.2          | 1.5.0          |                                                                                                                                                                                                              |
| community.sops                           | 2.2.2          | 2.2.7          |                                                                                                                                                                                                              |
| community.vmware                         | 5.7.2          | 6.1.0          |                                                                                                                                                                                                              |
| community.zabbix                         | 4.1.0          | 4.1.1          |                                                                                                                                                                                                              |
| containers.podman                        | 1.17.0         | 1.18.0         |                                                                                                                                                                                                              |
| cyberark.conjur                          | 1.3.7          | 1.3.8          | You can find the collection's changelog at [https://github.com/cyberark/ansible-conjur-collection/blob/master/CHANGELOG.md](https://github.com/cyberark/ansible-conjur-collection/blob/master/CHANGELOG.md). |
| cyberark.pas                             | 1.0.35         | 1.0.36         | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.                                                                                 |
| dellemc.enterprise_sonic                 | 3.0.0          | 3.2.0          |                                                                                                                                                                                                              |
| dellemc.openmanage                       | 9.12.3         | 10.0.1         |                                                                                                                                                                                                              |
| dellemc.powerflex                        | 2.6.1          | 3.0.0          |                                                                                                                                                                                                              |
| f5networks.f5_modules                    | 1.38.0         | 1.39.0         | There are no changes recorded in the changelog.                                                                                                                                                              |
| fortinet.fortimanager                    | 2.10.0         | 2.11.0         |                                                                                                                                                                                                              |
| fortinet.fortios                         | 2.4.0          | 2.4.2          |                                                                                                                                                                                                              |
| google.cloud                             | 1.7.0          | 1.9.0          |                                                                                                                                                                                                              |
| grafana.grafana                          | 6.0.3          | 6.0.6          |                                                                                                                                                                                                              |
| hetzner.hcloud                           | 5.2.0          | 6.0.0          |                                                                                                                                                                                                              |
| hitachivantara.vspone_block              | 4.1.0          | 4.4.0          |                                                                                                                                                                                                              |
| hitachivantara.vspone_object             |                | 1.0.0          | The collection was added to Ansible                                                                                                                                                                          |
| ibm.storage_virtualize                   | 2.7.4          | 3.1.0          |                                                                                                                                                                                                              |
| ieisystem.inmanage                       | 3.0.0          | 4.0.0          |                                                                                                                                                                                                              |
| kubernetes.core                          | 6.1.0          | 6.2.0          |                                                                                                                                                                                                              |
| netapp.ontap                             | 23.1.0         | 23.2.0         |                                                                                                                                                                                                              |
| ngine_io.cloudstack                      | 2.5.0          | 3.0.0          |                                                                                                                                                                                                              |
| openstack.cloud                          | 2.4.1          | 2.5.0          | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.                                                                                 |
| purestorage.flasharray                   | 1.36.0         | 1.39.0         |                                                                                                                                                                                                              |
| purestorage.flashblade                   | 1.20.0         | 1.22.0         |                                                                                                                                                                                                              |
| ravendb.ravendb                          |                | 1.0.4          | The collection was added to Ansible                                                                                                                                                                          |
| theforeman.foreman                       | 5.5.0          | 5.7.0          |                                                                                                                                                                                                              |
| vmware.vmware                            | 2.3.0          | 2.4.0          |                                                                                                                                                                                                              |

<a id="major-changes-6"></a>
### Major Changes

<a id="ansible-core-16"></a>
#### Ansible\-core

* ansible \- Add support for Python 3\.14\.
* ansible \- Drop support for Python 3\.11 on the controller\.
* ansible \- Drop support for Python 3\.8 on targets\.

<a id="community-vmware-2"></a>
#### community\.vmware

* Re\-use code from <code>vmware\.vmware</code> \([https\://github\.com/ansible\-collections/community\.vmware/pull/2459](https\://github\.com/ansible\-collections/community\.vmware/pull/2459)\)\.
* Replace <code>ansible\.module\_utils\.\_text</code> \([https\://github\.com/ansible\-collections/community\.vmware/issues/2497](https\://github\.com/ansible\-collections/community\.vmware/issues/2497)\)\.
* Replace <code>ansible\.module\_utils\.common\.\_collections\_compat</code> \([https\://github\.com/ansible\-collections/community\.vmware/issues/2497](https\://github\.com/ansible\-collections/community\.vmware/issues/2497)\)\.
* Replace <code>ansible\.module\_utils\.six</code> \([https\://github\.com/ansible\-collections/community\.vmware/pull/2495](https\://github\.com/ansible\-collections/community\.vmware/pull/2495)\)\.

<a id="containers-podman-9"></a>
#### containers\.podman

* Add inventory plugins for buildah and podman
* Add podman system connection modules

<a id="dellemc-openmanage-3"></a>
#### dellemc\.openmanage

* The OpenManage Enterprise\, OpenManage Enterprise Modular and OpenManage Enterprise Integration for VMware vCenter modules are now compatible with Ansible Core version 2\.19\.
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

<a id="fortinet-fortios-4"></a>
#### fortinet\.fortios

* Supported new versions 7\.6\.3 and 7\.6\.4\.
* Supported the authentication method when using username and password in v7\.6\.4\.

<a id="grafana-grafana"></a>
#### grafana\.grafana

* Add SUSE support to Alloy role by \@pozsa in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/423](https\://github\.com/grafana/grafana\-ansible\-collection/pull/423)
* Fallback to empty dict in case grafana\_ini is undefined by \@root\-expert in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/403](https\://github\.com/grafana/grafana\-ansible\-collection/pull/403)
* Fix Mimir config file validation task by \@Windos in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/428](https\://github\.com/grafana/grafana\-ansible\-collection/pull/428)
* Fixes issue by \@digiserg in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/421](https\://github\.com/grafana/grafana\-ansible\-collection/pull/421)
* Fixes to foldersFromFilesStructure option by \@root\-expert in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/351](https\://github\.com/grafana/grafana\-ansible\-collection/pull/351)
* Import custom dashboards only when directory exists by \@mahendrapaipuri in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/430](https\://github\.com/grafana/grafana\-ansible\-collection/pull/430)
* Migrate RedHat install to ansible\.builtin\.package by \@r65535 in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/431](https\://github\.com/grafana/grafana\-ansible\-collection/pull/431)
* Restore default listen address and port in Mimir by \@56quarters in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/456](https\://github\.com/grafana/grafana\-ansible\-collection/pull/456)
* Updated YUM repo urls from <em class="title-reference">packages\.grafana\.com</em> to <em class="title-reference">rpm\.grafana\.com</em> by \@DejfCold in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/414](https\://github\.com/grafana/grafana\-ansible\-collection/pull/414)
* Use credentials from grafana\_ini when importing dashboards by \@root\-expert in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/402](https\://github\.com/grafana/grafana\-ansible\-collection/pull/402)
* add macOS support to alloy role by \@l50 in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/418](https\://github\.com/grafana/grafana\-ansible\-collection/pull/418)
* do not skip scrape latest github version even in check\_mode by \@cmehat in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/408](https\://github\.com/grafana/grafana\-ansible\-collection/pull/408)
* fix broken Grafana apt repository addition by \@kleini in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/454](https\://github\.com/grafana/grafana\-ansible\-collection/pull/454)
* fix datasource documentation by \@jeremad in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/437](https\://github\.com/grafana/grafana\-ansible\-collection/pull/437)
* fix mimir\_download\_url\_deb \& mimir\_download\_url\_rpm by \@germebl in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/400](https\://github\.com/grafana/grafana\-ansible\-collection/pull/400)
* replace None with \[\] for safe length checks by \@voidquark in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/426](https\://github\.com/grafana/grafana\-ansible\-collection/pull/426)
* update catalog info by \@Duologic in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/434](https\://github\.com/grafana/grafana\-ansible\-collection/pull/434)
* use deb822 for newer debian versions by \@Lukas\-Heindl in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/440](https\://github\.com/grafana/grafana\-ansible\-collection/pull/440)

<a id="ieisystem-inmanage"></a>
#### ieisystem\.inmanage

* The edit\_m6\_log\_setting\.py module has added the \'server\_status\' attribute\; The edit\_network\_bond\.py module modifies the attribute descriptions\; The edit\_snmp\.py and edit\_snmp\_trap\.py module modifies the allowable value ranges for the auth\_protocol and priv\_protocol attributes\. \([https\://github\.com/ieisystem/ieisystem\.inmanage/pull/30](https\://github\.com/ieisystem/ieisystem\.inmanage/pull/30)\)\.

<a id="ngine-io-cloudstack"></a>
#### ngine\_io\.cloudstack

* Ensuring backwards compatibility and integration tests with CloudStack 4\.17 and 4\.18\.
* General overhaul \(black code style\) and renaming of all modules \(dropping <code>cs\_</code> prefix\) \([https\://github\.com/ngine\-io/ansible\-collection\-cloudstack/pull/141](https\://github\.com/ngine\-io/ansible\-collection\-cloudstack/pull/141)\)\.
* Update cs dependency to \>\=3\.4\.0\.

<a id="minor-changes-6"></a>
### Minor Changes

<a id="ansible-core-17"></a>
#### Ansible\-core

* Add tech preview play argument spec validation\, which can be enabled by setting the play keyword <code>validate\_argspec</code> to <code>True</code> or the name of an argument spec\. When <code>validate\_argspec</code> is set to <code>True</code>\, a play <code>name</code> is required and used as the argument spec name\. When enabled\, the argument spec is loaded from a file matching the pattern \<playbook\_name\>\.meta\.yml\. At minimum\, this file should contain <code>\{\"argument\_specs\"\: \{\"name\"\: \{\"options\"\: \{\}\}\}\}</code>\, where \"name\" is the name of the play or configured argument spec\.
* Added Univention Corporate Server as a part of Debian OS distribution family \([https\://github\.com/ansible/ansible/issues/85490](https\://github\.com/ansible/ansible/issues/85490)\)\.
* AnsibleModule \- Add temporary internal monkeypatch\-able hook to alter module result serialization by splitting serialization from <code>\_return\_formatted</code> into <code>\_record\_module\_result</code>\.
* DataLoader \- Update <code>DataLoader\.get\_basedir</code> to be an abspath
* Python type hints applied to <code>to\_text</code> and <code>to\_bytes</code> functions for better type hint interactions with code utilizing these functions\.
* ansible now warns if you use reserved tags that were only meant for selection and not for use in play\.
* ansible\-doc \- Return a more verbose error message when the <code>description</code> field is missing\.
* ansible\-doc \- show <code>notes</code>\, <code>seealso</code>\, and top\-level <code>version\_added</code> for role entrypoints \([https\://github\.com/ansible/ansible/pull/81796](https\://github\.com/ansible/ansible/pull/81796)\)\.
* ansible\-doc adds support for RETURN documentation to support doc fragment plugins
* ansible\-test \- Default to Python 3\.14 in the <code>base</code> and <code>default</code> test containers\.
* ansible\-test \- Filter out pylint messages for invalid filenames and display a notice when doing so\.
* ansible\-test \- Implement new authentication methods for accessing the Ansible Core CI service\.
* ansible\-test \- Improve formatting of generated coverage config file\.
* ansible\-test \- Removed support for automatic provisioning of obsolete instances for network\-integration tests\.
* ansible\-test \- Replace FreeBSD 14\.2 with 14\.3\.
* ansible\-test \- Replace RHEL 9\.5 with 9\.6\.
* ansible\-test \- Update Ubuntu containers\.
* ansible\-test \- Update astroid imports in custom pylint checkers\.
* ansible\-test \- Update base/default containers to include Python 3\.14\.0\.
* ansible\-test \- Update default containers\.
* ansible\-test \- Update pinned <code>pip</code> version to 25\.2\.
* ansible\-test \- Update pinned sanity test requirements\, including upgrading to pylint 4\.0\.0\.
* ansible\-test \- Update pinned sanity test requirements\.
* ansible\-test \- Update test containers\.
* ansible\-test \- Update the pylint sanity test to pylint 4\.0\.2\.
* ansible\-test \- Upgrade Alpine 3\.21 to 3\.22\.
* ansible\-test \- Upgrade Fedora 41 to Fedora 42\.
* ansible\-test \- Upgrade to <code>coverage</code> version 7\.10\.7 for Python 3\.9 and later\.
* ansible\-test \- Use OS packages to satisfy controller requirements on FreeBSD 13\.5 during managed instance bootstrapping\.
* apt\_repository \- use correct debug method to print debug message\.
* blockinfile \- add new module option <code>encoding</code> to support files in encodings other than UTF\-8 \([https\://github\.com/ansible/ansible/pull/85291](https\://github\.com/ansible/ansible/pull/85291)\)\.
* deb822\_repository \- Add automatic installation of the <code>python3\-debian</code> package if it is missing by adding the parameter <code>install\_python\_debian</code>
* default callback plugin \- add option to configure indentation for JSON and YAML output \([https\://github\.com/ansible/ansible/pull/85497](https\://github\.com/ansible/ansible/pull/85497)\)\.
* encrypt \- check datatype of salt\_size in password\_hash filter\.
* fetch\_file \- add ca\_path and cookies parameter arguments \([https\://github\.com/ansible/ansible/issues/85172](https\://github\.com/ansible/ansible/issues/85172)\)\.
* include\_vars \- Raise an error if \'extensions\' is not specified as a list\.
* include\_vars \- Raise an error if \'ignore\_files\' is not specified as a list\.
* known\_hosts \- return rc and stderr when ssh\-keygen command fails for further debugging \([https\://github\.com/ansible/ansible/issues/85850](https\://github\.com/ansible/ansible/issues/85850)\)\.
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

* Support check mode \(\-\-check\)
* added new parameter \'ips\_settings\' to \'cp\_mgmt\_simple\_cluster\' and \'cp\_mgmt\_simple\_gateway\' modules\.
* added new parameter \'override\_vpn\_domains\' to \'cp\_mgmt\_set\_vpn\_community\_remote\_access\' module\.
* added new parameter \'show\_installation\_targets\' to \'cp\_mgmt\_package\_facts\' module\.
* added new parameters \(such as \'permanent\_tunnels\'\, excluded\_services\, etc\.\) to \'cp\_mgmt\_vpn\_community\_meshed\' and \'cp\_mgmt\_vpn\_community\_star\' modules\.
* check\_point\.mgmt\.cp\_mgmt\_access\_rule\_facts \- support async\-response with customized HF\.

<a id="cisco-dnac-3"></a>
#### cisco\.dnac

* Added attribute \'slots\' in assurance\_icap\_settings\_workflow\_manager module
* Added attribute \'transit\_site\_hierarchy\' in sda\_fabric\_transits\_workflow\_manager module
* Added attribute native\_vlan\_id and allowed\_vlan\_ranges in sda\_host\_port\_onboarding\_workflow\_manager module
* Added attributes \'wireless\_flooding\_enable\'\, \'resource\_guard\_enable\'\, \'flooding\_address\_assignment\'\, \'flooding\_address\' in sda\_fabric\_transits\_workflow\_manager module
* Changes in assurance\_icap\_settings\_workflow\_manager module
* Changes in assurance\_issue\_workflow\_manager module
* Changes in inventory\_workflow\_manager module
* Changes in network\_profile\_switching\_workflow\_manager module
* Changes in network\_settings\_workflow\_manager module
* Changes in path\_trace\_workflow\_manager module
* Changes in sda\_fabric\_devices\_workflow\_manager module
* Changes in sda\_fabric\_sites\_zones\_workflow\_manager module
* Changes in sda\_fabric\_transits\_workflow\_manager module
* Changes in sda\_fabric\_virtual\_networks\_workflow\_manager module
* Changes in sda\_host\_port\_onboarding\_workflow\_manager module
* Changes in sda\_virtual\_networks\_workflow\_manager module
* Changes in template\_workflow\_manager module
* Changes limit and offset from float to int in all info modules
* Removed attribute \'slot\' in assurance\_icap\_settings\_workflow\_manager module

<a id="cisco-ios-5"></a>
#### cisco\.ios

* ios\_config \- added answering prompt functionality while working in config mode on ios device
* ios\_facts \- Add chassis\_id value to ansible\_net\_neighbors dictionary for lldp neighbours\.

<a id="cisco-iosxr-3"></a>
#### cisco\.iosxr

* Added few parameters to iosxr\_l3\_interface module to support new features\.

<a id="community-dns-7"></a>
#### community\.dns

* Note that some new code in <code>plugins/module\_utils/\_six\.py</code> is MIT licensed \([https\://github\.com/ansible\-collections/community\.dns/pull/287](https\://github\.com/ansible\-collections/community\.dns/pull/287)\)\.
* lookup\_\* plugins \- support <code>type\=HTTPS</code> and <code>type\=SVCB</code> \([https\://github\.com/ansible\-collections/community\.dns/issues/299](https\://github\.com/ansible\-collections/community\.dns/issues/299)\, [https\://github\.com/ansible\-collections/community\.dns/pull/300](https\://github\.com/ansible\-collections/community\.dns/pull/300)\)\.
* nameserver\_record\_info \- support <code>type\=HTTPS</code> and <code>type\=SVCB</code> \([https\://github\.com/ansible\-collections/community\.dns/issues/299](https\://github\.com/ansible\-collections/community\.dns/issues/299)\, [https\://github\.com/ansible\-collections/community\.dns/pull/300](https\://github\.com/ansible\-collections/community\.dns/pull/300)\)\.
* nameserver\_record\_info \- the return value <code>results\[\]\.result\[\]\.values</code> has been renamed to <code>results\[\]\.result\[\]\.entries</code>\. The old name will still be available for a longer time \([https\://github\.com/ansible\-collections/community\.dns/issues/289](https\://github\.com/ansible\-collections/community\.dns/issues/289)\, [https\://github\.com/ansible\-collections/community\.dns/pull/298](https\://github\.com/ansible\-collections/community\.dns/pull/298)\)\.
* wait\_for\_txt \- the option <code>records\[\]\.values</code> now has an alias <code>records\[\]\.entries</code> \([https\://github\.com/ansible\-collections/community\.dns/pull/298](https\://github\.com/ansible\-collections/community\.dns/pull/298)\)\.
* wait\_for\_txt \- the return value <code>records\[\]\.values</code> has been renamed to <code>records\[\]\.entries</code>\. The old name will still be available for a longer time \([https\://github\.com/ansible\-collections/community\.dns/issues/289](https\://github\.com/ansible\-collections/community\.dns/issues/289)\, [https\://github\.com/ansible\-collections/community\.dns/pull/298](https\://github\.com/ansible\-collections/community\.dns/pull/298)\)\.

<a id="community-docker-6"></a>
#### community\.docker

* Note that some new code in <code>plugins/module\_utils/\_six\.py</code> is MIT licensed \([https\://github\.com/ansible\-collections/community\.docker/pull/1138](https\://github\.com/ansible\-collections/community\.docker/pull/1138)\)\.
* docker\_container \- add <code>driver\_opts</code> option in <code>networks</code> \([https\://github\.com/ansible\-collections/community\.docker/issues/1142](https\://github\.com/ansible\-collections/community\.docker/issues/1142)\, [https\://github\.com/ansible\-collections/community\.docker/pull/1143](https\://github\.com/ansible\-collections/community\.docker/pull/1143)\)\.
* docker\_container \- add <code>gw\_priority</code> option in <code>networks</code> \([https\://github\.com/ansible\-collections/community\.docker/issues/1142](https\://github\.com/ansible\-collections/community\.docker/issues/1142)\, [https\://github\.com/ansible\-collections/community\.docker/pull/1143](https\://github\.com/ansible\-collections/community\.docker/pull/1143)\)\.
* docker\_container \- support missing fields and new mount types in <code>mounts</code> \([https\://github\.com/ansible\-collections/community\.docker/issues/1129](https\://github\.com/ansible\-collections/community\.docker/issues/1129)\, [https\://github\.com/ansible\-collections/community\.docker/pull/1134](https\://github\.com/ansible\-collections/community\.docker/pull/1134)\)\.

<a id="community-general-20"></a>
#### community\.general

* Modernize code for Python 3\.7\+\. This includes code reformatting\, and adding new checks to CI\, including a type checker \(mypy\)\. Most of the code does not have type hints yet\, but now it is possible to add typing hints and have these validated \([https\://github\.com/ansible\-collections/community\.general/pull/10285](https\://github\.com/ansible\-collections/community\.general/pull/10285)\, [https\://github\.com/ansible\-collections/community\.general/pull/10886](https\://github\.com/ansible\-collections/community\.general/pull/10886)\, [https\://github\.com/ansible\-collections/community\.general/pull/10891](https\://github\.com/ansible\-collections/community\.general/pull/10891)\, [https\://github\.com/ansible\-collections/community\.general/pull/10892](https\://github\.com/ansible\-collections/community\.general/pull/10892)\, [https\://github\.com/ansible\-collections/community\.general/pull/10897](https\://github\.com/ansible\-collections/community\.general/pull/10897)\, [https\://github\.com/ansible\-collections/community\.general/pull/10899](https\://github\.com/ansible\-collections/community\.general/pull/10899)\, [https\://github\.com/ansible\-collections/community\.general/pull/10902](https\://github\.com/ansible\-collections/community\.general/pull/10902)\, [https\://github\.com/ansible\-collections/community\.general/pull/10903](https\://github\.com/ansible\-collections/community\.general/pull/10903)\, [https\://github\.com/ansible\-collections/community\.general/pull/10904](https\://github\.com/ansible\-collections/community\.general/pull/10904)\, [https\://github\.com/ansible\-collections/community\.general/pull/10907](https\://github\.com/ansible\-collections/community\.general/pull/10907)\, [https\://github\.com/ansible\-collections/community\.general/pull/10908](https\://github\.com/ansible\-collections/community\.general/pull/10908)\, [https\://github\.com/ansible\-collections/community\.general/pull/10909](https\://github\.com/ansible\-collections/community\.general/pull/10909)\, [https\://github\.com/ansible\-collections/community\.general/pull/10939](https\://github\.com/ansible\-collections/community\.general/pull/10939)\, [https\://github\.com/ansible\-collections/community\.general/pull/10940](https\://github\.com/ansible\-collections/community\.general/pull/10940)\, [https\://github\.com/ansible\-collections/community\.general/pull/10941](https\://github\.com/ansible\-collections/community\.general/pull/10941)\, [https\://github\.com/ansible\-collections/community\.general/pull/10942](https\://github\.com/ansible\-collections/community\.general/pull/10942)\, [https\://github\.com/ansible\-collections/community\.general/pull/10945](https\://github\.com/ansible\-collections/community\.general/pull/10945)\, [https\://github\.com/ansible\-collections/community\.general/pull/10947](https\://github\.com/ansible\-collections/community\.general/pull/10947)\, [https\://github\.com/ansible\-collections/community\.general/pull/10958](https\://github\.com/ansible\-collections/community\.general/pull/10958)\, [https\://github\.com/ansible\-collections/community\.general/pull/10959](https\://github\.com/ansible\-collections/community\.general/pull/10959)\, [https\://github\.com/ansible\-collections/community\.general/pull/10968](https\://github\.com/ansible\-collections/community\.general/pull/10968)\, [https\://github\.com/ansible\-collections/community\.general/pull/10969](https\://github\.com/ansible\-collections/community\.general/pull/10969)\, [https\://github\.com/ansible\-collections/community\.general/pull/10970](https\://github\.com/ansible\-collections/community\.general/pull/10970)\, [https\://github\.com/ansible\-collections/community\.general/pull/10971](https\://github\.com/ansible\-collections/community\.general/pull/10971)\, [https\://github\.com/ansible\-collections/community\.general/pull/10973](https\://github\.com/ansible\-collections/community\.general/pull/10973)\, [https\://github\.com/ansible\-collections/community\.general/pull/10974](https\://github\.com/ansible\-collections/community\.general/pull/10974)\, [https\://github\.com/ansible\-collections/community\.general/pull/10975](https\://github\.com/ansible\-collections/community\.general/pull/10975)\, [https\://github\.com/ansible\-collections/community\.general/pull/10976](https\://github\.com/ansible\-collections/community\.general/pull/10976)\, [https\://github\.com/ansible\-collections/community\.general/pull/10977](https\://github\.com/ansible\-collections/community\.general/pull/10977)\, [https\://github\.com/ansible\-collections/community\.general/pull/10978](https\://github\.com/ansible\-collections/community\.general/pull/10978)\, [https\://github\.com/ansible\-collections/community\.general/pull/10979](https\://github\.com/ansible\-collections/community\.general/pull/10979)\, [https\://github\.com/ansible\-collections/community\.general/pull/10980](https\://github\.com/ansible\-collections/community\.general/pull/10980)\, [https\://github\.com/ansible\-collections/community\.general/pull/10981](https\://github\.com/ansible\-collections/community\.general/pull/10981)\, [https\://github\.com/ansible\-collections/community\.general/pull/10992](https\://github\.com/ansible\-collections/community\.general/pull/10992)\, [https\://github\.com/ansible\-collections/community\.general/pull/10993](https\://github\.com/ansible\-collections/community\.general/pull/10993)\, [https\://github\.com/ansible\-collections/community\.general/pull/10997](https\://github\.com/ansible\-collections/community\.general/pull/10997)\, [https\://github\.com/ansible\-collections/community\.general/pull/10999](https\://github\.com/ansible\-collections/community\.general/pull/10999)\, [https\://github\.com/ansible\-collections/community\.general/pull/11015](https\://github\.com/ansible\-collections/community\.general/pull/11015)\, [https\://github\.com/ansible\-collections/community\.general/pull/11016](https\://github\.com/ansible\-collections/community\.general/pull/11016)\, [https\://github\.com/ansible\-collections/community\.general/pull/11017](https\://github\.com/ansible\-collections/community\.general/pull/11017)\)\.
* aerospike\_migrations \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10494](https\://github\.com/ansible\-collections/community\.general/pull/10494)\)\.
* airbrake\_deployment \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10494](https\://github\.com/ansible\-collections/community\.general/pull/10494)\)\.
* android\_sdk \- minor refactor to improve readability \([https\://github\.com/ansible\-collections/community\.general/pull/10712](https\://github\.com/ansible\-collections/community\.general/pull/10712)\)\.
* apk \- using safer mechanism to run external command \([https\://github\.com/ansible\-collections/community\.general/issues/10479](https\://github\.com/ansible\-collections/community\.general/issues/10479)\, [https\://github\.com/ansible\-collections/community\.general/pull/10520](https\://github\.com/ansible\-collections/community\.general/pull/10520)\)\.
* bigpanda \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10494](https\://github\.com/ansible\-collections/community\.general/pull/10494)\)\.
* bootc\_manage \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10494](https\://github\.com/ansible\-collections/community\.general/pull/10494)\)\.
* bower \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10494](https\://github\.com/ansible\-collections/community\.general/pull/10494)\)\.
* btrfs\_subvolume \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10494](https\://github\.com/ansible\-collections/community\.general/pull/10494)\)\.
* bundler \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10494](https\://github\.com/ansible\-collections/community\.general/pull/10494)\)\.
* bzr \- using safer mechanism to run external command \([https\://github\.com/ansible\-collections/community\.general/pull/10523](https\://github\.com/ansible\-collections/community\.general/pull/10523)\)\.
* campfire \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10494](https\://github\.com/ansible\-collections/community\.general/pull/10494)\)\.
* capabilities \- using safer mechanism to run external command \([https\://github\.com/ansible\-collections/community\.general/pull/10524](https\://github\.com/ansible\-collections/community\.general/pull/10524)\)\.
* cargo \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10494](https\://github\.com/ansible\-collections/community\.general/pull/10494)\)\.
* catapult \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10494](https\://github\.com/ansible\-collections/community\.general/pull/10494)\)\.
* cisco\_webex \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10494](https\://github\.com/ansible\-collections/community\.general/pull/10494)\)\.
* cloudflare\_dns \- adds support for PTR records \([https\://github\.com/ansible\-collections/community\.general/pull/10267](https\://github\.com/ansible\-collections/community\.general/pull/10267)\)\.
* cloudflare\_dns \- remove redundant brackets in conditionals\, no functional changes \([https\://github\.com/ansible\-collections/community\.general/pull/10328](https\://github\.com/ansible\-collections/community\.general/pull/10328)\)\.
* cloudflare\_dns \- simplify validations and refactor some code\, no functional changes \([https\://github\.com/ansible\-collections/community\.general/pull/10269](https\://github\.com/ansible\-collections/community\.general/pull/10269)\)\.
* composer \- using safer mechanism to run external command \([https\://github\.com/ansible\-collections/community\.general/pull/10525](https\://github\.com/ansible\-collections/community\.general/pull/10525)\)\.
* consul\_kv \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10494](https\://github\.com/ansible\-collections/community\.general/pull/10494)\)\.
* consul\_policy \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10494](https\://github\.com/ansible\-collections/community\.general/pull/10494)\)\.
* copr \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10494](https\://github\.com/ansible\-collections/community\.general/pull/10494)\)\.
* crypttab \- remove redundant brackets in conditionals\, no functional changes \([https\://github\.com/ansible\-collections/community\.general/pull/10328](https\://github\.com/ansible\-collections/community\.general/pull/10328)\)\.
* datadog\_downtime \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10494](https\://github\.com/ansible\-collections/community\.general/pull/10494)\)\.
* datadog\_monitor \- remove redundant brackets in conditionals\, no functional changes \([https\://github\.com/ansible\-collections/community\.general/pull/10328](https\://github\.com/ansible\-collections/community\.general/pull/10328)\)\.
* datadog\_monitor \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10494](https\://github\.com/ansible\-collections/community\.general/pull/10494)\)\.
* datetime module utils \- remove code for unsupported Python version \([https\://github\.com/ansible\-collections/community\.general/pull/11048](https\://github\.com/ansible\-collections/community\.general/pull/11048)\)\.
* dconf \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10494](https\://github\.com/ansible\-collections/community\.general/pull/10494)\)\.
* dimensiondata\_network \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10494](https\://github\.com/ansible\-collections/community\.general/pull/10494)\)\.
* dimensiondata\_vlan \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10494](https\://github\.com/ansible\-collections/community\.general/pull/10494)\)\.
* django module utils \- remove deprecated parameter <code>\_DjangoRunner</code> call \([https\://github\.com/ansible\-collections/community\.general/pull/10574](https\://github\.com/ansible\-collections/community\.general/pull/10574)\)\.
* django module utils \- simplify/consolidate the common settings for the command line \([https\://github\.com/ansible\-collections/community\.general/pull/10684](https\://github\.com/ansible\-collections/community\.general/pull/10684)\)\.
* django\_check \- rename parameter <code>database</code> to <code>databases</code>\, add alias for compatibility \([https\://github\.com/ansible\-collections/community\.general/pull/10700](https\://github\.com/ansible\-collections/community\.general/pull/10700)\)\.
* django\_check \- simplify/consolidate the common settings for the command line \([https\://github\.com/ansible\-collections/community\.general/pull/10684](https\://github\.com/ansible\-collections/community\.general/pull/10684)\)\.
* django\_createcachetable \- simplify/consolidate the common settings for the command line \([https\://github\.com/ansible\-collections/community\.general/pull/10684](https\://github\.com/ansible\-collections/community\.general/pull/10684)\)\.
* dnf\_config\_manager \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10494](https\://github\.com/ansible\-collections/community\.general/pull/10494)\)\.
* dnsimple\_info \- use Ansible construct to validate parameters \([https\://github\.com/ansible\-collections/community\.general/pull/11052](https\://github\.com/ansible\-collections/community\.general/pull/11052)\)\.
* dnsmadeeasy \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10494](https\://github\.com/ansible\-collections/community\.general/pull/10494)\)\.
* dpkg\_divert \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10494](https\://github\.com/ansible\-collections/community\.general/pull/10494)\)\.
* easy\_install \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10494](https\://github\.com/ansible\-collections/community\.general/pull/10494)\)\.
* easy\_install \- using safer mechanism to run external command \([https\://github\.com/ansible\-collections/community\.general/pull/10526](https\://github\.com/ansible\-collections/community\.general/pull/10526)\)\.
* elasticsearch\_plugin \- minor refactor to improve readability \([https\://github\.com/ansible\-collections/community\.general/pull/10712](https\://github\.com/ansible\-collections/community\.general/pull/10712)\)\.
* elasticsearch\_plugin \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10494](https\://github\.com/ansible\-collections/community\.general/pull/10494)\)\.
* facter \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10494](https\://github\.com/ansible\-collections/community\.general/pull/10494)\)\.
* filesize \- minor refactor to simplify string formatting \([https\://github\.com/ansible\-collections/community\.general/pull/10727](https\://github\.com/ansible\-collections/community\.general/pull/10727)\)\.
* filesystem \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10494](https\://github\.com/ansible\-collections/community\.general/pull/10494)\)\.
* filetree \- add <code>exclude</code> option \([https\://github\.com/ansible\-collections/community\.general/issues/10936](https\://github\.com/ansible\-collections/community\.general/issues/10936)\, [https\://github\.com/ansible\-collections/community\.general/pull/10936](https\://github\.com/ansible\-collections/community\.general/pull/10936)\)\.
* gem \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10505](https\://github\.com/ansible\-collections/community\.general/pull/10505)\)\.
* git\_config\_info \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10505](https\://github\.com/ansible\-collections/community\.general/pull/10505)\)\.
* github\_app\_access\_token lookup plugin \- add support for GitHub Enterprise Server \([https\://github\.com/ansible\-collections/community\.general/issues/10879](https\://github\.com/ansible\-collections/community\.general/issues/10879)\, [https\://github\.com/ansible\-collections/community\.general/pull/10880](https\://github\.com/ansible\-collections/community\.general/pull/10880)\)\.
* github\_app\_access\_token lookup plugin \- support both <code>jwt</code> and <code>pyjwt</code> to avoid conflict with other modules requirements \([https\://github\.com/ansible\-collections/community\.general/issues/10299](https\://github\.com/ansible\-collections/community\.general/issues/10299)\)\.
* github\_deploy\_key \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10505](https\://github\.com/ansible\-collections/community\.general/pull/10505)\)\.
* github\_repo \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10505](https\://github\.com/ansible\-collections/community\.general/pull/10505)\)\.
* github\_webhook \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10505](https\://github\.com/ansible\-collections/community\.general/pull/10505)\)\.
* github\_webhook\_info \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10505](https\://github\.com/ansible\-collections/community\.general/pull/10505)\)\.
* gitlab\_branch \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10505](https\://github\.com/ansible\-collections/community\.general/pull/10505)\)\.
* gitlab\_deploy\_key \- remove redundant brackets in conditionals\, no functional changes \([https\://github\.com/ansible\-collections/community\.general/pull/10328](https\://github\.com/ansible\-collections/community\.general/pull/10328)\)\.
* gitlab\_group\_access\_token \- add <code>planner</code> access level \([https\://github\.com/ansible\-collections/community\.general/pull/10679](https\://github\.com/ansible\-collections/community\.general/pull/10679)\)\.
* gitlab\_group\_access\_token \- add missing scopes \([https\://github\.com/ansible\-collections/community\.general/pull/10785](https\://github\.com/ansible\-collections/community\.general/pull/10785)\)\.
* gitlab\_group\_access\_token \- remove redundant brackets in conditionals\, no functional changes \([https\://github\.com/ansible\-collections/community\.general/pull/10328](https\://github\.com/ansible\-collections/community\.general/pull/10328)\)\.
* gitlab\_group\_access\_token \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10505](https\://github\.com/ansible\-collections/community\.general/pull/10505)\)\.
* gitlab\_group\_variable \- add <code>description</code> option \([https\://github\.com/ansible\-collections/community\.general/pull/10812](https\://github\.com/ansible\-collections/community\.general/pull/10812)\)\.
* gitlab\_group\_variable \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10505](https\://github\.com/ansible\-collections/community\.general/pull/10505)\)\.
* gitlab\_group\_variable \- support masked\-and\-hidden variables \([https\://github\.com/ansible\-collections/community\.general/pull/10787](https\://github\.com/ansible\-collections/community\.general/pull/10787)\)\.
* gitlab\_hook \- remove redundant brackets in conditionals\, no functional changes \([https\://github\.com/ansible\-collections/community\.general/pull/10328](https\://github\.com/ansible\-collections/community\.general/pull/10328)\)\.
* gitlab\_hook \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10505](https\://github\.com/ansible\-collections/community\.general/pull/10505)\)\.
* gitlab\_instance\_variable \- add <code>description</code> option \([https\://github\.com/ansible\-collections/community\.general/pull/10812](https\://github\.com/ansible\-collections/community\.general/pull/10812)\)\.
* gitlab\_instance\_variable \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10505](https\://github\.com/ansible\-collections/community\.general/pull/10505)\)\.
* gitlab\_issue \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10505](https\://github\.com/ansible\-collections/community\.general/pull/10505)\)\.
* gitlab\_label \- minor refactor to improve readability \([https\://github\.com/ansible\-collections/community\.general/pull/10711](https\://github\.com/ansible\-collections/community\.general/pull/10711)\)\.
* gitlab\_label \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10505](https\://github\.com/ansible\-collections/community\.general/pull/10505)\)\.
* gitlab\_merge\_request \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10505](https\://github\.com/ansible\-collections/community\.general/pull/10505)\)\.
* gitlab\_milestone \- minor refactor to improve readability \([https\://github\.com/ansible\-collections/community\.general/pull/10711](https\://github\.com/ansible\-collections/community\.general/pull/10711)\)\.
* gitlab\_milestone \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10505](https\://github\.com/ansible\-collections/community\.general/pull/10505)\)\.
* gitlab\_project \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10505](https\://github\.com/ansible\-collections/community\.general/pull/10505)\)\.
* gitlab\_project\_access\_token \- add <code>planner</code> access level \([https\://github\.com/ansible\-collections/community\.general/pull/10679](https\://github\.com/ansible\-collections/community\.general/pull/10679)\)\.
* gitlab\_project\_access\_token \- add missing scopes \([https\://github\.com/ansible\-collections/community\.general/pull/10785](https\://github\.com/ansible\-collections/community\.general/pull/10785)\)\.
* gitlab\_project\_access\_token \- remove redundant brackets in conditionals\, no functional changes \([https\://github\.com/ansible\-collections/community\.general/pull/10328](https\://github\.com/ansible\-collections/community\.general/pull/10328)\)\.
* gitlab\_project\_access\_token \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10505](https\://github\.com/ansible\-collections/community\.general/pull/10505)\)\.
* gitlab\_project\_variable \- add <code>description</code> option \([https\://github\.com/ansible\-collections/community\.general/pull/10812](https\://github\.com/ansible\-collections/community\.general/pull/10812)\, [https\://github\.com/ansible\-collections/community\.general/issues/8584](https\://github\.com/ansible\-collections/community\.general/issues/8584)\, [https\://github\.com/ansible\-collections/community\.general/issues/10809](https\://github\.com/ansible\-collections/community\.general/issues/10809)\)\.
* gitlab\_project\_variable \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10505](https\://github\.com/ansible\-collections/community\.general/pull/10505)\)\.
* gitlab\_project\_variable \- support masked\-and\-hidden variables \([https\://github\.com/ansible\-collections/community\.general/pull/10787](https\://github\.com/ansible\-collections/community\.general/pull/10787)\)\.
* gitlab\_protected\_branch \- add <code>allow\_force\_push</code>\, <code>code\_owner\_approval\_required</code> \([https\://github\.com/ansible\-collections/community\.general/pull/10795](https\://github\.com/ansible\-collections/community\.general/pull/10795)\, [https\://github\.com/ansible\-collections/community\.general/issues/6432](https\://github\.com/ansible\-collections/community\.general/issues/6432)\, [https\://github\.com/ansible\-collections/community\.general/issues/10289](https\://github\.com/ansible\-collections/community\.general/issues/10289)\, [https\://github\.com/ansible\-collections/community\.general/issues/10765](https\://github\.com/ansible\-collections/community\.general/issues/10765)\)\.
* gitlab\_protected\_branch \- update protected branches if possible instead of recreating them \([https\://github\.com/ansible\-collections/community\.general/pull/10795](https\://github\.com/ansible\-collections/community\.general/pull/10795)\)\.
* gitlab\_runner \- remove redundant brackets in conditionals\, no functional changes \([https\://github\.com/ansible\-collections/community\.general/pull/10328](https\://github\.com/ansible\-collections/community\.general/pull/10328)\)\.
* grove \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10505](https\://github\.com/ansible\-collections/community\.general/pull/10505)\)\.
* hg \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10505](https\://github\.com/ansible\-collections/community\.general/pull/10505)\)\.
* homebrew \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10505](https\://github\.com/ansible\-collections/community\.general/pull/10505)\)\.
* homebrew\_cask \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10505](https\://github\.com/ansible\-collections/community\.general/pull/10505)\)\.
* homebrew\_tap \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10505](https\://github\.com/ansible\-collections/community\.general/pull/10505)\)\.
* honeybadger\_deployment \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10505](https\://github\.com/ansible\-collections/community\.general/pull/10505)\)\.
* htpasswd \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10505](https\://github\.com/ansible\-collections/community\.general/pull/10505)\)\.
* icinga2\_host \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10505](https\://github\.com/ansible\-collections/community\.general/pull/10505)\)\.
* imgadm \- using safer mechanism to run external command \([https\://github\.com/ansible\-collections/community\.general/pull/10536](https\://github\.com/ansible\-collections/community\.general/pull/10536)\)\.
* infinity \- consolidate double and triple whitespaces \([https\://github\.com/ansible\-collections/community\.general/pull/11029](https\://github\.com/ansible\-collections/community\.general/pull/11029)\)\.
* influxdb\_user \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10505](https\://github\.com/ansible\-collections/community\.general/pull/10505)\)\.
* ini\_file \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10505](https\://github\.com/ansible\-collections/community\.general/pull/10505)\)\.
* iocage inventory plugin \- minor refactor to improve readability \([https\://github\.com/ansible\-collections/community\.general/pull/10712](https\://github\.com/ansible\-collections/community\.general/pull/10712)\)\.
* ipa\_dnsrecord \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10505](https\://github\.com/ansible\-collections/community\.general/pull/10505)\)\.
* ipa\_dnszone \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10505](https\://github\.com/ansible\-collections/community\.general/pull/10505)\)\.
* ipa\_group \- remove redundant brackets in conditionals\, no functional changes \([https\://github\.com/ansible\-collections/community\.general/pull/10328](https\://github\.com/ansible\-collections/community\.general/pull/10328)\)\.
* ipa\_host \- add <code>userclass</code> and <code>locality</code> parameters \([https\://github\.com/ansible\-collections/community\.general/pull/10935](https\://github\.com/ansible\-collections/community\.general/pull/10935)\)\.
* ipa\_host \- minor refactor to improve readability \([https\://github\.com/ansible\-collections/community\.general/pull/10711](https\://github\.com/ansible\-collections/community\.general/pull/10711)\)\.
* ipa\_otptoken \- consolidate double and triple whitespaces \([https\://github\.com/ansible\-collections/community\.general/pull/11029](https\://github\.com/ansible\-collections/community\.general/pull/11029)\)\.
* ipa\_service \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10505](https\://github\.com/ansible\-collections/community\.general/pull/10505)\)\.
* ipbase\_info \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10505](https\://github\.com/ansible\-collections/community\.general/pull/10505)\)\.
* iptables\_state \- minor refactor to simplify string formatting \([https\://github\.com/ansible\-collections/community\.general/pull/10727](https\://github\.com/ansible\-collections/community\.general/pull/10727)\)\.
* ipwcli\_dns \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10505](https\://github\.com/ansible\-collections/community\.general/pull/10505)\)\.
* irc \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10505](https\://github\.com/ansible\-collections/community\.general/pull/10505)\)\.
* irc \- use proper boolean value in loops \([https\://github\.com/ansible\-collections/community\.general/pull/11076](https\://github\.com/ansible\-collections/community\.general/pull/11076)\)\.
* jabber \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10505](https\://github\.com/ansible\-collections/community\.general/pull/10505)\)\.
* java\_keystore \- remove redundant function \([https\://github\.com/ansible\-collections/community\.general/pull/10905](https\://github\.com/ansible\-collections/community\.general/pull/10905)\)\.
* jenkins\_build \- remove redundant brackets in conditionals\, no functional changes \([https\://github\.com/ansible\-collections/community\.general/pull/10328](https\://github\.com/ansible\-collections/community\.general/pull/10328)\)\.
* jenkins\_build\_info \- remove redundant brackets in conditionals\, no functional changes \([https\://github\.com/ansible\-collections/community\.general/pull/10328](https\://github\.com/ansible\-collections/community\.general/pull/10328)\)\.
* jenkins\_credential \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10505](https\://github\.com/ansible\-collections/community\.general/pull/10505)\)\.
* jenkins\_job \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10505](https\://github\.com/ansible\-collections/community\.general/pull/10505)\)\.
* jenkins\_node \- remove code for unsupported Python version \([https\://github\.com/ansible\-collections/community\.general/pull/11048](https\://github\.com/ansible\-collections/community\.general/pull/11048)\)\.
* jenkins\_plugin \- install dependencies for specific version \([https\://github\.com/ansible\-collections/community\.general/issue/4995](https\://github\.com/ansible\-collections/community\.general/issue/4995)\, [https\://github\.com/ansible\-collections/community\.general/pull/10346](https\://github\.com/ansible\-collections/community\.general/pull/10346)\)\.
* jenkins\_script \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10505](https\://github\.com/ansible\-collections/community\.general/pull/10505)\)\.
* keycloak \- add support for <code>grant\_type\=client\_credentials</code> to all keycloak modules\, so that specifying <code>auth\_client\_id</code> and <code>auth\_client\_secret</code> is sufficient for authentication \([https\://github\.com/ansible\-collections/community\.general/pull/10231](https\://github\.com/ansible\-collections/community\.general/pull/10231)\)\.
* keycloak module utils \- remove redundant brackets in conditionals\, no functional changes \([https\://github\.com/ansible\-collections/community\.general/pull/10328](https\://github\.com/ansible\-collections/community\.general/pull/10328)\)\.
* keycloak\_authz\_authorization\_scope \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10507](https\://github\.com/ansible\-collections/community\.general/pull/10507)\)\.
* keycloak\_authz\_permission \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10507](https\://github\.com/ansible\-collections/community\.general/pull/10507)\)\.
* keycloak\_client \- add idempotent support for <code>optional\_client\_scopes</code> and <code>optional\_client\_scopes</code>\, and ensure consistent change detection between check mode and live run \([https\://github\.com/ansible\-collections/community\.general/issues/5495](https\://github\.com/ansible\-collections/community\.general/issues/5495)\, [https\://github\.com/ansible\-collections/community\.general/pull/10842](https\://github\.com/ansible\-collections/community\.general/pull/10842)\)\.
* keycloak\_identity\_provider – add support for <code>fromUrl</code> to automatically fetch OIDC endpoints from the well\-known discovery URL\, simplifying identity provider configuration \([https\://github\.com/ansible\-collections/community\.general/pull/10527](https\://github\.com/ansible\-collections/community\.general/pull/10527)\)\.
* keycloak\_realm \- add support for WebAuthn policy configuration options\, including both regular and passwordless WebAuthn policies \([https\://github\.com/ansible\-collections/community\.general/pull/10791](https\://github\.com/ansible\-collections/community\.general/pull/10791)\)\.
* keycloak\_realm \- add support for <code>brute\_force\_strategy</code> and <code>max\_temporary\_lockouts</code> \([https\://github\.com/ansible\-collections/community\.general/issues/10412](https\://github\.com/ansible\-collections/community\.general/issues/10412)\, [https\://github\.com/ansible\-collections/community\.general/pull/10415](https\://github\.com/ansible\-collections/community\.general/pull/10415)\)\.
* keycloak\_realm \- add support for client\-related options and Oauth2 device \([https\://github\.com/ansible\-collections/community\.general/pull/10538](https\://github\.com/ansible\-collections/community\.general/pull/10538)\)\.
* keycloak\_role \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10507](https\://github\.com/ansible\-collections/community\.general/pull/10507)\)\.
* keycloak\_user \- return user created boolean flag \([https\://github\.com/ansible\-collections/community\.general/pull/10950](https\://github\.com/ansible\-collections/community\.general/pull/10950)\)\.
* keycloak\_userprofile \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10507](https\://github\.com/ansible\-collections/community\.general/pull/10507)\)\.
* keyring \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10507](https\://github\.com/ansible\-collections/community\.general/pull/10507)\)\.
* kibana\_plugin \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10507](https\://github\.com/ansible\-collections/community\.general/pull/10507)\)\.
* layman \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10507](https\://github\.com/ansible\-collections/community\.general/pull/10507)\)\.
* ldap\_attrs \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10507](https\://github\.com/ansible\-collections/community\.general/pull/10507)\)\.
* ldap\_inc \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10507](https\://github\.com/ansible\-collections/community\.general/pull/10507)\)\.
* librato\_annotation \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10507](https\://github\.com/ansible\-collections/community\.general/pull/10507)\)\.
* linode module utils \- remove redundant code for ancient versions of Ansible \([https\://github\.com/ansible\-collections/community\.general/pull/10906](https\://github\.com/ansible\-collections/community\.general/pull/10906)\)\.
* lldp \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10507](https\://github\.com/ansible\-collections/community\.general/pull/10507)\)\.
* logentries \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10507](https\://github\.com/ansible\-collections/community\.general/pull/10507)\)\.
* logstash callback plugin \- remove redundant brackets in conditionals\, no functional changes \([https\://github\.com/ansible\-collections/community\.general/pull/10328](https\://github\.com/ansible\-collections/community\.general/pull/10328)\)\.
* logstash\_plugin \- using safer mechanism to run external command \([https\://github\.com/ansible\-collections/community\.general/issues/10479](https\://github\.com/ansible\-collections/community\.general/issues/10479)\, [https\://github\.com/ansible\-collections/community\.general/pull/10520](https\://github\.com/ansible\-collections/community\.general/pull/10520)\)\.
* lvg\_rename \- minor refactor to improve readability \([https\://github\.com/ansible\-collections/community\.general/pull/10711](https\://github\.com/ansible\-collections/community\.general/pull/10711)\)\.
* lxca\_cmms \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10507](https\://github\.com/ansible\-collections/community\.general/pull/10507)\)\.
* lxca\_nodes \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10507](https\://github\.com/ansible\-collections/community\.general/pull/10507)\)\.
* macports \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10507](https\://github\.com/ansible\-collections/community\.general/pull/10507)\)\.
* mail \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10507](https\://github\.com/ansible\-collections/community\.general/pull/10507)\)\.
* manageiq \- minor refactor to improve readability \([https\://github\.com/ansible\-collections/community\.general/pull/10712](https\://github\.com/ansible\-collections/community\.general/pull/10712)\)\.
* manageiq\_alert\_profiles \- minor refactor to improve readability \([https\://github\.com/ansible\-collections/community\.general/pull/10712](https\://github\.com/ansible\-collections/community\.general/pull/10712)\)\.
* manageiq\_alerts \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10507](https\://github\.com/ansible\-collections/community\.general/pull/10507)\)\.
* manageiq\_group \- minor refactor to simplify string formatting \([https\://github\.com/ansible\-collections/community\.general/pull/10727](https\://github\.com/ansible\-collections/community\.general/pull/10727)\)\.
* manageiq\_group \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10507](https\://github\.com/ansible\-collections/community\.general/pull/10507)\)\.
* manageiq\_policies \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10507](https\://github\.com/ansible\-collections/community\.general/pull/10507)\)\.
* manageiq\_policies\_info \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10507](https\://github\.com/ansible\-collections/community\.general/pull/10507)\)\.
* manageiq\_tags \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10507](https\://github\.com/ansible\-collections/community\.general/pull/10507)\)\.
* manageiq\_tenant \- minor refactor to simplify string formatting \([https\://github\.com/ansible\-collections/community\.general/pull/10727](https\://github\.com/ansible\-collections/community\.general/pull/10727)\)\.
* manageiq\_tenant \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10507](https\://github\.com/ansible\-collections/community\.general/pull/10507)\)\.
* matrix \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10507](https\://github\.com/ansible\-collections/community\.general/pull/10507)\)\.
* mattermost \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10507](https\://github\.com/ansible\-collections/community\.general/pull/10507)\)\.
* maven\_artifact \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10507](https\://github\.com/ansible\-collections/community\.general/pull/10507)\)\.
* memset\_dns\_reload \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10507](https\://github\.com/ansible\-collections/community\.general/pull/10507)\)\.
* memset\_zone \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10507](https\://github\.com/ansible\-collections/community\.general/pull/10507)\)\.
* memset\_zone\_record \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10507](https\://github\.com/ansible\-collections/community\.general/pull/10507)\)\.
* mqtt \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10507](https\://github\.com/ansible\-collections/community\.general/pull/10507)\)\.
* mssql\_db \- minor refactor to simplify string formatting \([https\://github\.com/ansible\-collections/community\.general/pull/10727](https\://github\.com/ansible\-collections/community\.general/pull/10727)\)\.
* mssql\_db \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10507](https\://github\.com/ansible\-collections/community\.general/pull/10507)\)\.
* mssql\_script \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10507](https\://github\.com/ansible\-collections/community\.general/pull/10507)\)\.
* nagios \- make parameter <code>services</code> a <code>list</code> instead of a <code>str</code> \([https\://github\.com/ansible\-collections/community\.general/pull/10493](https\://github\.com/ansible\-collections/community\.general/pull/10493)\)\.
* netcup\_dns \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10507](https\://github\.com/ansible\-collections/community\.general/pull/10507)\)\.
* newrelic\_deployment \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10507](https\://github\.com/ansible\-collections/community\.general/pull/10507)\)\.
* nmcli \- remove redundant brackets in conditionals\, no functional changes \([https\://github\.com/ansible\-collections/community\.general/pull/10328](https\://github\.com/ansible\-collections/community\.general/pull/10328)\)\.
* nmcli \- simplify validations and refactor some code\, no functional changes \([https\://github\.com/ansible\-collections/community\.general/pull/10323](https\://github\.com/ansible\-collections/community\.general/pull/10323)\)\.
* npm \- improve parameter validation using Ansible construct \([https\://github\.com/ansible\-collections/community\.general/pull/10983](https\://github\.com/ansible\-collections/community\.general/pull/10983)\)\.
* nsupdate \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10507](https\://github\.com/ansible\-collections/community\.general/pull/10507)\)\.
* oci\_vcn \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10512](https\://github\.com/ansible\-collections/community\.general/pull/10512)\)\.
* one\_image\_info \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10512](https\://github\.com/ansible\-collections/community\.general/pull/10512)\)\.
* one\_template \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10512](https\://github\.com/ansible\-collections/community\.general/pull/10512)\)\.
* one\_vm \- minor refactor to improve readability \([https\://github\.com/ansible\-collections/community\.general/pull/10712](https\://github\.com/ansible\-collections/community\.general/pull/10712)\)\.
* one\_vnet \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10512](https\://github\.com/ansible\-collections/community\.general/pull/10512)\)\.
* oneandone\_firewall\_policy \- remove redundant brackets in conditionals\, no functional changes \([https\://github\.com/ansible\-collections/community\.general/pull/10328](https\://github\.com/ansible\-collections/community\.general/pull/10328)\)\.
* oneandone\_load\_balancer \- remove redundant brackets in conditionals\, no functional changes \([https\://github\.com/ansible\-collections/community\.general/pull/10328](https\://github\.com/ansible\-collections/community\.general/pull/10328)\)\.
* oneandone\_monitoring\_policy \- remove redundant brackets in conditionals\, no functional changes \([https\://github\.com/ansible\-collections/community\.general/pull/10328](https\://github\.com/ansible\-collections/community\.general/pull/10328)\)\.
* onepassword\_info \- remove redundant brackets in conditionals\, no functional changes \([https\://github\.com/ansible\-collections/community\.general/pull/10328](https\://github\.com/ansible\-collections/community\.general/pull/10328)\)\.
* onepassword\_info \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10512](https\://github\.com/ansible\-collections/community\.general/pull/10512)\)\.
* oneview\_fc\_network\_info \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10512](https\://github\.com/ansible\-collections/community\.general/pull/10512)\)\.
* open\_iscsi \- using safer mechanism to run external command \([https\://github\.com/ansible\-collections/community\.general/pull/10599](https\://github\.com/ansible\-collections/community\.general/pull/10599)\)\.
* openbsd\_pkg \- add <code>autoremove</code> parameter to remove unused dependencies \([https\://github\.com/ansible\-collections/community\.general/pull/10705](https\://github\.com/ansible\-collections/community\.general/pull/10705)\)\.
* openbsd\_pkg \- minor refactor to simplify string formatting \([https\://github\.com/ansible\-collections/community\.general/pull/10727](https\://github\.com/ansible\-collections/community\.general/pull/10727)\)\.
* opendj\_backendprop \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10512](https\://github\.com/ansible\-collections/community\.general/pull/10512)\)\.
* opendj\_backendprop \- use Ansible construct to perform check for external commands \([https\://github\.com/ansible\-collections/community\.general/pull/11072](https\://github\.com/ansible\-collections/community\.general/pull/11072)\)\.
* osx\_defaults \- remove redundant brackets in conditionals\, no functional changes \([https\://github\.com/ansible\-collections/community\.general/pull/10328](https\://github\.com/ansible\-collections/community\.general/pull/10328)\)\.
* ovh\_ip\_loadbalancing\_backend \- remove redundant brackets in conditionals\, no functional changes \([https\://github\.com/ansible\-collections/community\.general/pull/10328](https\://github\.com/ansible\-collections/community\.general/pull/10328)\)\.
* ovh\_monthly\_billing \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10512](https\://github\.com/ansible\-collections/community\.general/pull/10512)\)\.
* pacemaker\_cluster \- add <code>state\=maintenance</code> for managing pacemaker maintenance mode \([https\://github\.com/ansible\-collections/community\.general/issues/10200](https\://github\.com/ansible\-collections/community\.general/issues/10200)\, [https\://github\.com/ansible\-collections/community\.general/pull/10227](https\://github\.com/ansible\-collections/community\.general/pull/10227)\)\.
* pacemaker\_cluster \- rename <code>node</code> to <code>name</code> and add <code>node</code> alias \([https\://github\.com/ansible\-collections/community\.general/pull/10227](https\://github\.com/ansible\-collections/community\.general/pull/10227)\)\.
* pacemaker\_resource \- add <code>state\=cleanup</code> for cleaning up pacemaker resources \([https\://github\.com/ansible\-collections/community\.general/pull/10413](https\://github\.com/ansible\-collections/community\.general/pull/10413)\)
* pacemaker\_resource \- add <code>state\=cloned</code> for cloning pacemaker resources or groups \([https\://github\.com/ansible\-collections/community\.general/issues/10322](https\://github\.com/ansible\-collections/community\.general/issues/10322)\, [https\://github\.com/ansible\-collections/community\.general/pull/10665](https\://github\.com/ansible\-collections/community\.general/pull/10665)\)\.
* pacemaker\_resource \- enhance module by removing duplicative code \([https\://github\.com/ansible\-collections/community\.general/pull/10227](https\://github\.com/ansible\-collections/community\.general/pull/10227)\)\.
* pacemaker\_resource \- the parameter <code>name</code> is no longer a required parameter in community\.general 11\.3\.0 \([https\://github\.com/ansible\-collections/community\.general/pull/10413](https\://github\.com/ansible\-collections/community\.general/pull/10413)\)
* packet\_device \- remove redundant brackets in conditionals\, no functional changes \([https\://github\.com/ansible\-collections/community\.general/pull/10328](https\://github\.com/ansible\-collections/community\.general/pull/10328)\)\.
* pagerduty \- remove redundant brackets in conditionals\, no functional changes \([https\://github\.com/ansible\-collections/community\.general/pull/10328](https\://github\.com/ansible\-collections/community\.general/pull/10328)\)\.
* pagerduty \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10512](https\://github\.com/ansible\-collections/community\.general/pull/10512)\)\.
* pagerduty\_change \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10512](https\://github\.com/ansible\-collections/community\.general/pull/10512)\)\.
* pagerduty\_user \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10512](https\://github\.com/ansible\-collections/community\.general/pull/10512)\)\.
* pam\_limits \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10512](https\://github\.com/ansible\-collections/community\.general/pull/10512)\)\.
* parted \- using safer mechanism to run external command \([https\://github\.com/ansible\-collections/community\.general/pull/10642](https\://github\.com/ansible\-collections/community\.general/pull/10642)\)\.
* pear \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10512](https\://github\.com/ansible\-collections/community\.general/pull/10512)\)\.
* pear \- using safer mechanism to run external command \([https\://github\.com/ansible\-collections/community\.general/pull/10601](https\://github\.com/ansible\-collections/community\.general/pull/10601)\)\.
* pingdom \- remove redundant brackets in conditionals\, no functional changes \([https\://github\.com/ansible\-collections/community\.general/pull/10328](https\://github\.com/ansible\-collections/community\.general/pull/10328)\)\.
* pipx module\_utils \- use <code>PIPX\_USE\_EMOJI</code> to disable emojis in the output of <code>pipx</code> 1\.8\.0 \([https\://github\.com/ansible\-collections/community\.general/pull/10874](https\://github\.com/ansible\-collections/community\.general/pull/10874)\)\.
* pkgng \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10512](https\://github\.com/ansible\-collections/community\.general/pull/10512)\)\.
* pnpm \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10512](https\://github\.com/ansible\-collections/community\.general/pull/10512)\)\.
* portage \- add a <code>changed\_deps</code> option \([https\://github\.com/ansible\-collections/community\.general/pull/11023](https\://github\.com/ansible\-collections/community\.general/pull/11023)\)\.
* portage \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10512](https\://github\.com/ansible\-collections/community\.general/pull/10512)\)\.
* portage \- using safer mechanism to run external command \([https\://github\.com/ansible\-collections/community\.general/pull/10602](https\://github\.com/ansible\-collections/community\.general/pull/10602)\)\.
* pritunl\_org \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10512](https\://github\.com/ansible\-collections/community\.general/pull/10512)\)\.
* pritunl\_org\_info \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10512](https\://github\.com/ansible\-collections/community\.general/pull/10512)\)\.
* pritunl\_user \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10512](https\://github\.com/ansible\-collections/community\.general/pull/10512)\)\.
* pritunl\_user\_info \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10512](https\://github\.com/ansible\-collections/community\.general/pull/10512)\)\.
* pubnub\_blocks \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10512](https\://github\.com/ansible\-collections/community\.general/pull/10512)\)\.
* pushbullet \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10512](https\://github\.com/ansible\-collections/community\.general/pull/10512)\)\.
* pushover \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10512](https\://github\.com/ansible\-collections/community\.general/pull/10512)\)\.
* python\_runner module utils \- remove redundant brackets in conditionals\, no functional changes \([https\://github\.com/ansible\-collections/community\.general/pull/10328](https\://github\.com/ansible\-collections/community\.general/pull/10328)\)\.
* random\_string lookup plugin \- allow to specify seed while generating random string \([https\://github\.com/ansible\-collections/community\.general/issues/5362](https\://github\.com/ansible\-collections/community\.general/issues/5362)\, [https\://github\.com/ansible\-collections/community\.general/pull/10710](https\://github\.com/ansible\-collections/community\.general/pull/10710)\)\.
* redis\_data \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10512](https\://github\.com/ansible\-collections/community\.general/pull/10512)\)\.
* redis\_data\_incr \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10512](https\://github\.com/ansible\-collections/community\.general/pull/10512)\)\.
* rhevm \- consolidate double and triple whitespaces \([https\://github\.com/ansible\-collections/community\.general/pull/11029](https\://github\.com/ansible\-collections/community\.general/pull/11029)\)\.
* rhevm \- remove redundant brackets in conditionals\, no functional changes \([https\://github\.com/ansible\-collections/community\.general/pull/10328](https\://github\.com/ansible\-collections/community\.general/pull/10328)\)\.
* riak \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10512](https\://github\.com/ansible\-collections/community\.general/pull/10512)\)\.
* riak \- using safer mechanism to run external command \([https\://github\.com/ansible\-collections/community\.general/pull/10603](https\://github\.com/ansible\-collections/community\.general/pull/10603)\)\.
* rocketchat \- remove redundant brackets in conditionals\, no functional changes \([https\://github\.com/ansible\-collections/community\.general/pull/10328](https\://github\.com/ansible\-collections/community\.general/pull/10328)\)\.
* rocketchat \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10512](https\://github\.com/ansible\-collections/community\.general/pull/10512)\)\.
* rollbar\_deployment \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10512](https\://github\.com/ansible\-collections/community\.general/pull/10512)\)\.
* say \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10512](https\://github\.com/ansible\-collections/community\.general/pull/10512)\)\.
* scaleway modules \- add a <code>scaleway</code> group to use <code>module\_defaults</code> \([https\://github\.com/ansible\-collections/community\.general/pull/10647](https\://github\.com/ansible\-collections/community\.general/pull/10647)\)\.
* scaleway\_\* modules\, scaleway inventory plugin \- update available zones and API URLs \([https\://github\.com/ansible\-collections/community\.general/issues/10383](https\://github\.com/ansible\-collections/community\.general/issues/10383)\, [https\://github\.com/ansible\-collections/community\.general/pull/10424](https\://github\.com/ansible\-collections/community\.general/pull/10424)\)\.
* scaleway\_container \- add a <code>cpu\_limit</code> argument \([https\://github\.com/ansible\-collections/community\.general/pull/10646](https\://github\.com/ansible\-collections/community\.general/pull/10646)\)\.
* scaleway\_database\_backup \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10512](https\://github\.com/ansible\-collections/community\.general/pull/10512)\)\.
* sendgrid \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10512](https\://github\.com/ansible\-collections/community\.general/pull/10512)\)\.
* sensu\_silence \- remove redundant brackets in conditionals\, no functional changes \([https\://github\.com/ansible\-collections/community\.general/pull/10328](https\://github\.com/ansible\-collections/community\.general/pull/10328)\)\.
* sensu\_silence \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10512](https\://github\.com/ansible\-collections/community\.general/pull/10512)\)\.
* sensu\_subscription \- normalize quotes in the module output \([https\://github\.com/ansible\-collections/community\.general/pull/10483](https\://github\.com/ansible\-collections/community\.general/pull/10483)\)\.
* sl\_vm \- remove redundant brackets in conditionals\, no functional changes \([https\://github\.com/ansible\-collections/community\.general/pull/10328](https\://github\.com/ansible\-collections/community\.general/pull/10328)\)\.
* slack \- consolidate double and triple whitespaces \([https\://github\.com/ansible\-collections/community\.general/pull/11029](https\://github\.com/ansible\-collections/community\.general/pull/11029)\)\.
* solaris\_zone \- using safer mechanism to run external command \([https\://github\.com/ansible\-collections/community\.general/pull/10604](https\://github\.com/ansible\-collections/community\.general/pull/10604)\)\.
* sorcery \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10512](https\://github\.com/ansible\-collections/community\.general/pull/10512)\)\.
* ssh\_config \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10512](https\://github\.com/ansible\-collections/community\.general/pull/10512)\)\.
* statusio\_maintenance \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10512](https\://github\.com/ansible\-collections/community\.general/pull/10512)\)\.
* svr4pkg \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10512](https\://github\.com/ansible\-collections/community\.general/pull/10512)\)\.
* swdepot \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10512](https\://github\.com/ansible\-collections/community\.general/pull/10512)\)\.
* swupd \- using safer mechanism to run external command \([https\://github\.com/ansible\-collections/community\.general/pull/10605](https\://github\.com/ansible\-collections/community\.general/pull/10605)\)\.
* syslogger \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10512](https\://github\.com/ansible\-collections/community\.general/pull/10512)\)\.
* sysrc \- adjustments to the code \([https\://github\.com/ansible\-collections/community\.general/pull/10417](https\://github\.com/ansible\-collections/community\.general/pull/10417)\)\.
* sysrc \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10512](https\://github\.com/ansible\-collections/community\.general/pull/10512)\)\.
* systemd\_creds\_decrypt \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10512](https\://github\.com/ansible\-collections/community\.general/pull/10512)\)\.
* systemd\_creds\_encrypt \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10512](https\://github\.com/ansible\-collections/community\.general/pull/10512)\)\.
* taiga\_issue \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10513](https\://github\.com/ansible\-collections/community\.general/pull/10513)\)\.
* tasks\_only callback plugin \- add <code>result\_format</code> and <code>pretty\_results</code> options similarly to the default callback \([https\://github\.com/ansible\-collections/community\.general/pull/10422](https\://github\.com/ansible\-collections/community\.general/pull/10422)\)\.
* terraform \- minor refactor to improve readability \([https\://github\.com/ansible\-collections/community\.general/pull/10711](https\://github\.com/ansible\-collections/community\.general/pull/10711)\)\.
* timezone \- using safer mechanism to run external command \([https\://github\.com/ansible\-collections/community\.general/pull/10612](https\://github\.com/ansible\-collections/community\.general/pull/10612)\)\.
* tss lookup plugin \- fixed <code>AccessTokenAuthorizer</code> initialization to include <code>base\_url</code> parameter for proper token authentication \([https\://github\.com/ansible\-collections/community\.general/pull/11031](https\://github\.com/ansible\-collections/community\.general/pull/11031)\)\.
* twilio \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10513](https\://github\.com/ansible\-collections/community\.general/pull/10513)\)\.
* ufw \- minor refactor to simplify string formatting \([https\://github\.com/ansible\-collections/community\.general/pull/10727](https\://github\.com/ansible\-collections/community\.general/pull/10727)\)\.
* urpmi \- remove redundant brackets in conditionals\, no functional changes \([https\://github\.com/ansible\-collections/community\.general/pull/10328](https\://github\.com/ansible\-collections/community\.general/pull/10328)\)\.
* urpmi \- using safer mechanism to run external command \([https\://github\.com/ansible\-collections/community\.general/pull/10606](https\://github\.com/ansible\-collections/community\.general/pull/10606)\)\.
* utm\_aaa\_group \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10513](https\://github\.com/ansible\-collections/community\.general/pull/10513)\)\.
* utm\_ca\_host\_key\_cert \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10513](https\://github\.com/ansible\-collections/community\.general/pull/10513)\)\.
* utm\_dns\_host \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10513](https\://github\.com/ansible\-collections/community\.general/pull/10513)\)\.
* utm\_network\_interface\_address \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10513](https\://github\.com/ansible\-collections/community\.general/pull/10513)\)\.
* utm\_proxy\_auth\_profile \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10513](https\://github\.com/ansible\-collections/community\.general/pull/10513)\)\.
* utm\_proxy\_exception \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10513](https\://github\.com/ansible\-collections/community\.general/pull/10513)\)\.
* utm\_proxy\_frontend \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10513](https\://github\.com/ansible\-collections/community\.general/pull/10513)\)\.
* utm\_proxy\_location \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10513](https\://github\.com/ansible\-collections/community\.general/pull/10513)\)\.
* vertica\_configuration \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10513](https\://github\.com/ansible\-collections/community\.general/pull/10513)\)\.
* vertica\_info \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10513](https\://github\.com/ansible\-collections/community\.general/pull/10513)\)\.
* vertica\_role \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10513](https\://github\.com/ansible\-collections/community\.general/pull/10513)\)\.
* xattr \- remove redundant brackets in conditionals\, no functional changes \([https\://github\.com/ansible\-collections/community\.general/pull/10328](https\://github\.com/ansible\-collections/community\.general/pull/10328)\)\.
* xbps \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10513](https\://github\.com/ansible\-collections/community\.general/pull/10513)\)\.
* xbps \- using safer mechanism to run external command \([https\://github\.com/ansible\-collections/community\.general/pull/10608](https\://github\.com/ansible\-collections/community\.general/pull/10608)\)\.
* xenserver module utils \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10769](https\://github\.com/ansible\-collections/community\.general/pull/10769)\)\.
* xenserver\_facts \- minor refactor to simplify string formatting \([https\://github\.com/ansible\-collections/community\.general/pull/10727](https\://github\.com/ansible\-collections/community\.general/pull/10727)\)\.
* xfconf \- minor adjustments the the code \([https\://github\.com/ansible\-collections/community\.general/pull/10311](https\://github\.com/ansible\-collections/community\.general/pull/10311)\)\.
* xfs\_quota \- using safer mechanism to run external command \([https\://github\.com/ansible\-collections/community\.general/pull/10609](https\://github\.com/ansible\-collections/community\.general/pull/10609)\)\.
* xml \- remove redundant brackets in conditionals\, no functional changes \([https\://github\.com/ansible\-collections/community\.general/pull/10328](https\://github\.com/ansible\-collections/community\.general/pull/10328)\)\.
* yarn \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10513](https\://github\.com/ansible\-collections/community\.general/pull/10513)\)\.
* zfs\_facts \- minor refactor to simplify string formatting \([https\://github\.com/ansible\-collections/community\.general/pull/10727](https\://github\.com/ansible\-collections/community\.general/pull/10727)\)\.
* zfs\_facts \- use Ansible construct to check result of external command \([https\://github\.com/ansible\-collections/community\.general/pull/11054](https\://github\.com/ansible\-collections/community\.general/pull/11054)\)\.
* zypper \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10513](https\://github\.com/ansible\-collections/community\.general/pull/10513)\)\.
* zypper \- support the <code>\-\-gpg\-auto\-import\-keys</code> option in zypper \([https\://github\.com/ansible\-collections/community\.general/issues/10660](https\://github\.com/ansible\-collections/community\.general/issues/10660)\, [https\://github\.com/ansible\-collections/community\.general/pull/10661](https\://github\.com/ansible\-collections/community\.general/pull/10661)\)\.
* zypper\_repository \- remove redundant constructs from argument specs \([https\://github\.com/ansible\-collections/community\.general/pull/10513](https\://github\.com/ansible\-collections/community\.general/pull/10513)\)\.

<a id="community-hashi-vault"></a>
#### community\.hashi\_vault

* community\.hashi\_vault collection \- add support for <code>gcp</code> auth method \([https\://github\.com/ansible\-collections/community\.hashi\_vault/pull/442](https\://github\.com/ansible\-collections/community\.hashi\_vault/pull/442)\)\.

<a id="community-hrobot-1"></a>
#### community\.hrobot

* storagebox\_subaccount \- filter by username when looking for existing accounts by username \([https\://github\.com/ansible\-collections/community\.hrobot/pull/182](https\://github\.com/ansible\-collections/community\.hrobot/pull/182)\)\.
* storagebox\_subaccount \- use the new <code>change\_home\_directory</code> action to update a subaccount\'s home directory\, instead of using the now deprecated way using the <code>update\_access\_settings</code> action \([https\://github\.com/ansible\-collections/community\.hrobot/pull/181](https\://github\.com/ansible\-collections/community\.hrobot/pull/181)\)\.

<a id="community-mysql-4"></a>
#### community\.mysql

* <em class="title-reference">mysql\_query</em> \- add new <em class="title-reference">session\_vars</em> argument\, similar to ansible\-collections/community\.mysql\#489\.

<a id="community-proxmox-9"></a>
#### community\.proxmox

* proxmox \- Add delete parameter to delete settings \([https\://github\.com/ansible\-collections/community\.proxmox/pull/195](https\://github\.com/ansible\-collections/community\.proxmox/pull/195)\)\.
* proxmox\_cluster \-  Add master\_api\_password for authentication against master node \([https\://github\.com/ansible\-collections/community\.proxmox/pull/140](https\://github\.com/ansible\-collections/community\.proxmox/pull/140)\)\.
* proxmox\_cluster \- added link0 and link1 to join command \([https\://github\.com/ansible\-collections/community\.proxmox/issues/168](https\://github\.com/ansible\-collections/community\.proxmox/issues/168)\, [https\://github\.com/ansible\-collections/community\.proxmox/pull/172](https\://github\.com/ansible\-collections/community\.proxmox/pull/172)\)\.
* proxmox\_kvm \- update description of machine parameter in proxmox\_kvm\.py \([https\://github\.com/ansible\-collections/community\.proxmox/pull/186](https\://github\.com/ansible\-collections/community\.proxmox/pull/186)\)
* proxmox\_storage \- added <em class="title-reference">dir</em> and <em class="title-reference">zfspool</em> storage types \([https\://github\.com/ansible\-collections/community\.proxmox/pull/184](https\://github\.com/ansible\-collections/community\.proxmox/pull/184)\)
* proxmox\_tasks\_info \- add source option to specify tasks to consider \([https\://github\.com/ansible\-collections/community\.proxmox/pull/179](https\://github\.com/ansible\-collections/community\.proxmox/pull/179)\)
* proxmox\_template \-  Add \'import\' to allowed content types of proxmox\_template\, so disk images and can be used as disk images on VM creation \([https\://github\.com/ansible\-collections/community\.proxmox/pull/162](https\://github\.com/ansible\-collections/community\.proxmox/pull/162)\)\.

<a id="community-proxysql"></a>
#### community\.proxysql

* proxysql\_mysql\_users \- Creating users with the <code>caching\_sha2\_password</code> plugin \([https\://github\.com/ansible\-collections/community\.proxysql/pull/173](https\://github\.com/ansible\-collections/community\.proxysql/pull/173)\)\.

<a id="community-routeros-11"></a>
#### community\.routeros

* api\_find\_and\_modify\, api\_modify \- instead of comparing supplied values as\-is to values retrieved from the API and converted to some types \(int\, bool\) by librouteros\, instead compare values by converting them to strings first\, using similar conversion rules that librouteros uses \([https\://github\.com/ansible\-collections/community\.routeros/issues/389](https\://github\.com/ansible\-collections/community\.routeros/issues/389)\, [https\://github\.com/ansible\-collections/community\.routeros/issues/370](https\://github\.com/ansible\-collections/community\.routeros/issues/370)\, [https\://github\.com/ansible\-collections/community\.routeros/issues/325](https\://github\.com/ansible\-collections/community\.routeros/issues/325)\, [https\://github\.com/ansible\-collections/community\.routeros/issues/169](https\://github\.com/ansible\-collections/community\.routeros/issues/169)\, [https\://github\.com/ansible\-collections/community\.routeros/pull/397](https\://github\.com/ansible\-collections/community\.routeros/pull/397)\)\.
* api\_modify \- add <code>vrf</code> for <code>snmp</code> with a default of <code>main</code> for RouterOS 7\.3 and newer \([https\://github\.com/ansible\-collections/community\.routeros/pull/411](https\://github\.com/ansible\-collections/community\.routeros/pull/411)\)\.
* api\_modify \- add <code>vrf</code> for <code>system logging action</code> with a default of <code>main</code> for RouterOS 7\.19 and newer \([https\://github\.com/ansible\-collections/community\.routeros/pull/401](https\://github\.com/ansible\-collections/community\.routeros/pull/401)\)\.
* api\_modify\, api\_info \- field <code>instance</code> in <code>routing bgp connection</code> path is required\, and <code>router\-id</code> has been moved to <code>routing bgp instance</code> by RouterOS 7\.20 and newer \([https\://github\.com/ansible\-collections/community\.routeros/pull/404](https\://github\.com/ansible\-collections/community\.routeros/pull/404)\)\.
* api\_modify\, api\_info \- support for field <code>new\-priority</code> in API path <code>ipv6 firewall mangle\`</code> \([https\://github\.com/ansible\-collections/community\.routeros/pull/402](https\://github\.com/ansible\-collections/community\.routeros/pull/402)\)\.

<a id="community-sap-libs-2"></a>
#### community\.sap\_libs

* collection \- Enhance <em class="title-reference">ansible\-test\`</em> CI action\, remove Python 2 and fix detected issues \([https\://github\.com/sap\-linuxlab/community\.sap\_libs/pull/60](https\://github\.com/sap\-linuxlab/community\.sap\_libs/pull/60)\)
* collection \- Pipeline fixes and drop test support for ansible below 2\.13 \([https\://github\.com/sap\-linuxlab/community\.sap\_libs/pull/43](https\://github\.com/sap\-linuxlab/community\.sap\_libs/pull/43)\)
* collection \- Update documentation and changelog for <em class="title-reference">1\.5\.0</em> release \([https\://github\.com/sap\-linuxlab/community\.sap\_libs/pull/61](https\://github\.com/sap\-linuxlab/community\.sap\_libs/pull/61)\)
* collection \- Update workflow <em class="title-reference">ansible\-test</em> to include latest versions \([https\://github\.com/sap\-linuxlab/community\.sap\_libs/pull/54](https\://github\.com/sap\-linuxlab/community\.sap\_libs/pull/54)\)
* sap\_control\_exec \- Remove unsupported functions \([https\://github\.com/sap\-linuxlab/community\.sap\_libs/pull/45](https\://github\.com/sap\-linuxlab/community\.sap\_libs/pull/45)\)
* sap\_hdbsql \- add \-E option to filepath command \([https\://github\.com/sap\-linuxlab/community\.sap\_libs/pull/42](https\://github\.com/sap\-linuxlab/community\.sap\_libs/pull/42)\)

<a id="community-sops-1"></a>
#### community\.sops

* Note that some new code in <code>plugins/module\_utils/\_six\.py</code> is MIT licensed \([https\://github\.com/ansible\-collections/community\.sops/pull/268](https\://github\.com/ansible\-collections/community\.sops/pull/268)\)\.

<a id="community-vmware-3"></a>
#### community\.vmware

* vcenter\_license \- Add support for VCF license keys\. \([https\://github\.com/ansible\-collections/community\.vmware/pull/2451](https\://github\.com/ansible\-collections/community\.vmware/pull/2451)\)
* vmware\_dvs\_portgroup \- add <code>portgroup\_description</code> parameter \([https\://github\.com/ansible\-collections/community\.vmware/issues/2487](https\://github\.com/ansible\-collections/community\.vmware/issues/2487)\)\.
* vsphere\_file \- Remove <code>ansible\.module\_utils\.six\.PY2</code> \([https\://github\.com/ansible\-collections/community\.vmware/pull/2475](https\://github\.com/ansible\-collections/community\.vmware/pull/2475)\)\.

<a id="community-zabbix-2"></a>
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

<a id="containers-podman-10"></a>
#### containers\.podman

* Add building Podman from source
* Add podman image scp option
* Add unittests for podman\_image
* Improve docs and guides
* Rewrite podman\_image and add tests
* Update docs and script

<a id="dellemc-enterprise-sonic"></a>
#### dellemc\.enterprise\_sonic

* bgp\_af \- Add support for \'dup\-addr\-detection\' commands \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/452](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/452)\)\.
* sonic\_aaa \- Add MFA support for AAA module \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/532](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/532)\)\.
* sonic\_bgp \- Add support for graceful restart attributes \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/538](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/538)\)\.
* sonic\_bgp \- Added Ansible support for the bandwidth option \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/557](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/557)\)\.
* sonic\_bgp\_neighbors \- Add support for discard\-extra option for BGP peer\-group maximum\-prefix\([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/545](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/545)\)\.
* sonic\_bgp\_neighbors \- Added Ansible support for the extended\_link\_bandwidth option \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/557](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/557)\)\.
* sonic\_bgp\_neighbors \- Remove mutual exclusion for peer\_group allowas\_in options \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/586](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/586)\)\.
* sonic\_bgp\_neighbors\_af \- Add support for discard\-extra option for BGP neighbor maximum\-prefix\([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/545](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/545)\)\.
* sonic\_bgp\_neighbors\_af \- Remove mutual exclusion for neighbor allowas\_in options \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/586](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/586)\)\.
* sonic\_copp \- Add \'copp\_traps\' to CoPP module \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/461](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/461)\)\.
* sonic\_interfaces \- Add support for configuring speed and advertised speed for 800 GB interfaces \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/590](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/590)\)\.
* sonic\_interfaces \- Add support for speed 200GB \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/534](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/534)\)\.
* sonic\_interfaces \- Enhancing port\-group and interface speed error handling \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/487](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/487)\)\.
* sonic\_l3\_interfaces \- Add support for ipv6 \'anycast\_addresses\' option \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/491](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/491)\)\.
* sonic\_l3\_interfaces \- Added support for Proxy\-ARP/ND\-Proxy feature \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/576](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/576)\)\.
* sonic\_lag\_interfaces \- Add support for \'fallback\'\, \'fast\_rate\'\, \'graceful\_shutdown\'\, \'lacp\_individual\'\, \'min\_links\' and \'system\_mac\' options \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/475](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/475)\)\.
* sonic\_lldp\_interfaces \- Add playbook check and diff modes support for lldp\_interfaces module \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/524](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/524)\)\.
* sonic\_lldp\_interfaces \- Add support for LLDP TLVs i\.e\.\, \'port\_vlan\_id\'\, \'vlan\_name\'\, \'link\_aggregation\'\, \'max\_frame\_size\'\, and \'vlan\_name\_tlv\' attributes \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/406](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/406)\)\.
* sonic\_lldp\_interfaces \- Add support for network policy configuration \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/582](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/582)\)\.
* sonic\_logging \- Add support for \'security\_profile\' option \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/555](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/555)\)\.
* sonic\_logging \- Adding the ability to delete a specific attribute of a logging server into the logging module \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/486](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/486)\)\.
* sonic\_mclag \- Added Ansible support for the yang leafs added as part of the  MCLAG Split Brain Detection and Recovery feature \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/496](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/496)\)\.
* sonic\_port\_breakout \- Add support for modes 1x800G\, 2x400G\, 4x200G\, and 8x100G \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/585](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/585)\)\.
* sonic\_port\_group \- Add support for speed 200GB \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/534](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/534)\)\.
* sonic\_qos\_interfaces \- Add \'cable\_length\' attribute \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/468](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/468)\)\.
* sonic\_route\_maps \- Add support for set ARS object \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/581](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/581)\)\.
* sonic\_route\_maps \- Added Ansible support for bandwidth feature and suboptions bandwidth\_value and transitive\_value \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/557](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/557)\)\.
* sonic\_sflow \- Add max header size support in sonic\_sflow module \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/419](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/419)\)\.
* sonic\_system \- Add concurrent session limit support for sonic\_system module \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/505](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/505)\)\.
* sonic\_system \- Add password complexity support for sonic\_system module \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/519](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/519)\)\.
* sonic\_system \- Add support for Tx/Rx clock frequency adjustment \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/562](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/562)\)\.
* sonic\_system \- Add switching\-mode functionality to the sonic\_system module \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/504](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/504)\)\.
* sonic\_users \- Add support for user ssh key configuration \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/512](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/512)\)\.
* sonic\_vlans \- Add support for autostate attribute configuration on a VLAN \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/533](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/533)\)\.

<a id="dellemc-openmanage-4"></a>
#### dellemc\.openmanage

* idrac\_support\_assist \- Introduced aliases for the module parameters share\_username and share\_password to align with the naming conventions used across other modules\, ensuring consistency and improving usability\.

<a id="dellemc-powerflex"></a>
#### dellemc\.powerflex

* Added support for executing activemq\, lia\, mdm and tb roles on PowerFlex Gen2\.
* Added support for executing mdm\_cluster\, nvme\_host\, sdc\, sdt and snapshot\_policy modules on PowerFlex Gen2\.

<a id="fortinet-fortimanager-5"></a>
#### fortinet\.fortimanager

* Supported new schemas in FortiManager 7\.0\.14\, 7\.2\.10\, 7\.2\.11\.

<a id="fortinet-fortios-5"></a>
#### fortinet\.fortios

* Supported default\_group feature for all of the modules\.

<a id="google-cloud-6"></a>
#### google\.cloud

* iap \- added scp\_if\_ssh option \([https\://github\.com/ansible\-collections/google\.cloud/pull/716](https\://github\.com/ansible\-collections/google\.cloud/pull/716)\)\.
* iap \- enable use of Identity Aware Proxy ssh connections to compute instances \([https\://github\.com/ansible\-collections/google\.cloud/pull/709](https\://github\.com/ansible\-collections/google\.cloud/pull/709)\)\.

<a id="hetzner-hcloud-7"></a>
#### hetzner\.hcloud

* server\_type\_info \- Return new Server Type <code>category</code> property\.
* server\_type\_info \- Return new Server Type <code>locations</code> property\.
* zone \- New module to manage DNS Zones in Hetzner Cloud\.
* zone\_info \- New module to fetch DNS Zones details\.
* zone\_rrset \- New module to manage DNS Zone RRSets in the Hetzner Cloud\.
* zone\_rrset\_info \- New module to fetch DNS RRSets details\.

<a id="hitachivantara-vspone-block-6"></a>
#### hitachivantara\.vspone\_block

* Added a new \"hv\_sds\_block\_compute\_port\" module to change the settings and protocol of the compute port on Hitachi SDS Block storage systems\.
* Added a new \"hv\_sds\_block\_remote\_iscsi\_port\" module to register a remote iSCSI port and delete information about registered remote iSCSI ports on Hitachi SDS Block storage systems\.
* Added a new \"hv\_sds\_block\_remote\_iscsi\_port\_facts\" module to retrieve remote iSCSI ports from Hitachi SDS Block storage systems\.
* Added a new \"hv\_sds\_block\_software\_update\_file\_facts\" module to retrieve information of the update file of the storage software which performed transfer \(upload\) in the Hitachi SDS Block storage systems\.
* Added a new \"hv\_sds\_block\_storage\_node\_bmc\_connection\" module allows to update the BMC connection settings of Hitachi SDS Block storage systems\.
* Added a new \"hv\_sds\_block\_storage\_software\_update\" module allows software update and downgrade on Hitachi SDS Block storage systems\.
* Added a new \"hv\_vsp\_one\_port\" module to retrieve volume\'s information from servers on VSP E series and VSP One B2X storages\.
* Added a new \"hv\_vsp\_one\_port\_facts\" module to retrieve port information from VSP E series and VSP One B2X storages\.
* Added a new \"hv\_vsp\_one\_server\" module enables register\, modification\, and deletion of servers\, as well as various server operations on VSP E series and VSP One B2X storages\.
* Added a new \"hv\_vsp\_one\_server\_facts\" module to retrieve information about servers from servers on VSP E series and VSP One B2X storages\.
* Added a new \"hv\_vsp\_one\_server\_hba\_facts\" module to retrieve HBA \(Host Bus Adapter\) information about servers from servers on VSP E series and VSP One B2X storages\.
* Added a new \"hv\_vsp\_one\_snapshot\" module to create\, modify and delete snapshots on VSP E series and VSP One B2X storages\.
* Added a new \"hv\_vsp\_one\_snapshot\_facts\" module to retrieve snapshot information from VSP E series and VSP One B2X storages\.
* Added a new \"hv\_vsp\_one\_snapshot\_group\" module to manage snapshot group operations on VSP E series and VSP One B2X storages\.
* Added a new \"hv\_vsp\_one\_snapshot\_group\_facts\" module to retrieve snapshot group information from VSP E series and VSP One B2X storages\.
* Added a new <em class="title-reference">\"hv\_sds\_block\_capacity\_management\_settings\_facts\"</em> module to retrieve capacity management settings from SDS block cluster\.
* Added a new <em class="title-reference">\"hv\_sds\_block\_drive\"</em> module to turn ON and Off the drive locator LED\, remove a drive from SDS block cluster\.
* Added a new <em class="title-reference">\"hv\_sds\_block\_storage\_controller\"</em> module to edit storage controller settings on SDS block cluster\.
* Added a new <em class="title-reference">\"hv\_sds\_block\_storage\_node\_bmc\_connection\_facts\"</em> module to retrieve BMC connection details from SDS block cluster\.
* Added a new <em class="title-reference">\"hv\_sds\_block\_storage\_pool\_estimated\_capacity\_facts\"</em> module to retrieve storage pool estimated capacity from SDS block cluster on AWS\.
* Added a new <em class="title-reference">\"hv\_vsp\_one\_volume\"</em> module to enable creation\, modification\, and deletion of volumes\, as well as attaching and detaching to servers on VSP E series and VSP One B2X storages\.
* Added a new <em class="title-reference">\"hv\_vsp\_one\_volume\_facts\"</em> module to retrieve volumes information from servers on VSP E series and VSP One B2X storages\.
* Added support for SDS block cluster on Microsoft Azure\.
* Added support for latest software version 1\.18\.1 for SDS block on AWS\, GCP and Bare metal\.
* Added support for listing storage node primary role status in the output to hv\_sds\_block\_storage\_node\_facts module\.
* Added support to \"Add storage node to the SDS cluster on AWS cloud\" to hv\_sds\_block\_cluster module\.
* Added support to \"Allow CHAP users to access the compute port\" to hv\_sds\_block\_compute\_port\_authentication module
* Added support to \"Attach multiple volumes to multiple servers in one operation\" to hv\_vsp\_one\_volume module\.
* Added support to \"Cancel compute port access permission for CHAP users\" to hv\_sds\_block\_compute\_port\_authentication module
* Added support to \"Create a VPS\" to hv\_sds\_block\_vps module\.
* Added support to \"Create a compute node in a VPS by VPS ID\" to hv\_sds\_block\_compute\_node module\.
* Added support to \"Create a compute node in a VPS by VPS name\" to hv\_sds\_block\_compute\_node module\.
* Added support to \"Create a volume in a VPS by VPS ID\" to hv\_sds\_block\_volume module\.
* Added support to \"Create a volume in a VPS by VPS name\" to hv\_sds\_block\_volume module\.
* Added support to \"Create the cluster configuration file for replace\_storage\_node export file type for AWS\" to hv\_sds\_block\_cluster module\.
* Added support to \"Create the cluster configuration file for replace\_storage\_node export file type for GCP\" to hv\_sds\_block\_cluster module\.
* Added support to \"Delete a VPS by ID\" to hv\_sds\_block\_vps module\.
* Added support to \"Delete a VPS by name\" to hv\_sds\_block\_vps module\.
* Added support to \"Delete compute node by name in a VPS by VPS ID\" to hv\_sds\_block\_compute\_node module\.
* Added support to \"Delete compute node by name in a VPS by VPS name\" to hv\_sds\_block\_compute\_node module\.
* Added support to \"Delete volume by name in a VPS by VPS ID\" to hv\_sds\_block\_volume module\.
* Added support to \"Delete volume by name in a VPS by VPS name\" to hv\_sds\_block\_volume module\.
* Added support to \"Edit storage pool settings\" to hv\_sds\_block\_storage\_pool module\.
* Added support to \"Edit the capacity balancing settings\" to hv\_sds\_block\_cluster module\.
* Added support to \"Get Drive by ID\" to hv\_sds\_block\_drives\_facts module
* Added support to \"Get Protection Domain Information by ID\" to hv\_sds\_block\_protection\_domain\_facts module
* Added support to \"Get Snapshots using master volume name in a VPS\" to hv\_sds\_block\_snapshot\_facts module\.
* Added support to \"Get compute nodes for a VPS by VPS ID\" to hv\_sds\_block\_compute\_node\_facts module\.
* Added support to \"Get compute nodes for a VPS by VPS name\" to hv\_sds\_block\_compute\_node\_facts module\.
* Added support to \"Get volumes for a VPS by VPS ID\" to hv\_sds\_block\_volume\_facts module\.
* Added support to \"Get volumes for a VPS by VPS name\" to hv\_sds\_block\_volume\_facts module\.
* Added support to \"Import system requirements file for performing replace storage node on Bare metal\" to hv\_sds\_block\_cluster module\.
* Added support to \"Replace storage node in the cluster by storage node ID on AWS\" to hv\_sds\_block\_cluster module\.
* Added support to \"Replace storage node in the cluster by storage node ID on Azure\" to hv\_sds\_block\_cluster module\.
* Added support to \"Replace storage node in the cluster by storage node ID on Bare Metal\" to hv\_sds\_block\_cluster module\.
* Added support to \"Replace storage node in the cluster by storage node ID on GCP\" to hv\_sds\_block\_cluster module\.
* Added support to \"Stop removing storage nodes\" to hv\_sds\_block\_cluster module\.
* Added support to \"Update settings of a VPS\" to hv\_sds\_block\_vps module\.
* Added support to take ldev input in HEX value in all hitachivantara\.vspone\_block\.vsp modules\.
* Added support with new parameters \"start\_ldev\"\, \"end\_ldev\"\, \"external\_parity\_groups\" to hv\_resource\_group module\.
* Updated input parameter name from \"saving\_setting\" to \"capacity\_saving\" in hv\_vsp\_one\_volume module\.

<a id="ibm-storage-virtualize-4"></a>
#### ibm\.storage\_virtualize

* ibm\_sv\_manage\_flashsystem\_grid \- Added support for new FlashSystem grid APIs
* ibm\_sv\_manage\_storage\_partition \- Added support for management portset and renaming partition
* ibm\_sv\_manage\_truststore\_for\_replication \- Added support for new FlashSystem grid APIs
* ibm\_svc\_hostcluster \- Added support for partition and for managing host mappings during hostcluster deletion
* ibm\_svc\_info \- Added support for new FlashSystem grid APIs
* ibm\_svc\_manage\_ip \- Changes for management portset
* ibm\_svc\_manage\_ip \- Changes for updating VLAN\, gateway and IP address
* ibm\_svc\_manage\_portset \- Added support for management portset
* ibm\_svc\_manage\_volume \- Added support for HA volumes volume expansion\, volumegroup\, volume rename and grainsize
* ibm\_svc\_utils \- Improved error message for unreachable systems

<a id="kubernetes-core-4"></a>
#### kubernetes\.core

* Add support of skip\-schema\-validation in <code>helm</code> module \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/995](https\://github\.com/ansible\-collections/kubernetes\.core/pull/995)\)
* kustomize \- Add support of local environ \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/786](https\://github\.com/ansible\-collections/kubernetes\.core/pull/786)\)\.

<a id="netapp-ontap-7"></a>
#### netapp\.ontap

* Modified ZAPI deprecation messages and warnings\.
* na\_ontap\_aggregate \- AWS Lambda support added to the module\.
* na\_ontap\_autosupport \- Replaced private cli with REST API\.
* na\_ontap\_cg\_snapshot \- new option <em class="title-reference">consistency\_type</em> added in REST\.
* na\_ontap\_job\_schedule \- new option <em class="title-reference">interval</em> added in REST\.
* na\_ontap\_job\_schedule \- new option <em class="title-reference">vserver</em> added in REST\.
* na\_ontap\_lun \- new option <em class="title-reference">provisioning\_options</em> added in REST\, requires ONTAP 9\.16\.1 or later\.
* na\_ontap\_net\_port \- Added REST support for <em class="title-reference">flowcontrol\_admin</em> and <em class="title-reference">ipspace</em>\.
* na\_ontap\_nfs \- added REST support for the option <em class="title-reference">nfsv3\_fsid\_change</em> \(requires ONTAP 9\.11\.0 or later\)\, and for <em class="title-reference">nfsv4\_fsid\_change</em>\, <em class="title-reference">nfsv40\_referrals</em>\, and <em class="title-reference">nfsv41\_referrals</em> \(requires ONTAP 9\.13\.1 or later\)\.
* na\_ontap\_nfs \- new protocol options added in REST\.
* na\_ontap\_quotas \- updated docs for \'quota\_target\' and \'type\'\.
* na\_ontap\_rest\_info \- support added for <em class="title-reference">application/consistency\-groups/metrics</em>\.
* na\_ontap\_rest\_info \- support added for <em class="title-reference">application/consistency\-groups/snapshots</em>\.
* na\_ontap\_security\_ssh \- new option <em class="title-reference">host\_key\_algorithms</em>\, requires ONTAP 9\.16\.1 or later\.
* na\_ontap\_snapshot \- new option <em class="title-reference">snaplock\_expiry\_time</em> added in REST\, requires ONTAP 9\.15\.1 or later\.
* na\_ontap\_software\_update \- Updated documentation for <em class="title-reference">validate\_after\_download</em> parameter\.
* na\_ontap\_svm \- new option <em class="title-reference">storage\_limit\_threshold\_alert</em> added in REST\, requires ONTAP 9\.13\.1 or later\.
* na\_ontap\_svm \- new options <em class="title-reference">auto\_enable\_analytics</em>\, <em class="title-reference">auto\_enable\_activity\_tracking</em> added in REST\, requires ONTAP 9\.12\.1 or later\.
* na\_ontap\_user \- updated docs for \'vserver\' option\.
* na\_ontap\_volume \- AWS Lambda support added to the module\.
* na\_ontap\_volume\_autosize \- updated docs for <em class="title-reference">increment\_size</em> \& <em class="title-reference">reset</em>\.
* na\_ontap\_volume\_clone \- new options <em class="title-reference">time\_out</em>\, <em class="title-reference">wait\_for\_completion</em> added in REST\.
* updated <em class="title-reference">README</em> template\; added \'Support\' section\.

<a id="purestorage-flasharray-4"></a>
#### purestorage\.flasharray

* plugins/module\_utils/purefa\.py \- Removed <code>get\_system</code> function as REST v1 no longer supported by Collection
* purefa\_arrayname \- Added Fusion support
* purefa\_audits \- Added Fusion support
* purefa\_banner \- Added Fusion support
* purefa\_connect \- Added Fusion support
* purefa\_connect \- Allow asynchronous FC\-based replication
* purefa\_console \- Added Fusion support
* purefa\_default\_protection \- Added Fusion support\.
* purefa\_directory \- Added Fusion support
* purefa\_dirsnap \- Added Fusion support
* purefa\_ds \- Added Fusion support
* purefa\_dsrole \- Added Fusion support
* purefa\_dsrole\_old \- Upgraded to REST v2
* purefa\_endpoint \- Added Fusion support
* purefa\_eradication \- Added Fusion support
* purefa\_export \- Added Fusion support
* purefa\_fs \- Added Fusion support
* purefa\_info \- Added new subsets <code>workloads</code> and <code>presets</code>
* purefa\_info \- Converted to use REST 2
* purefa\_maintenance \- Timeout window updated
* purefa\_messages \- Added Fusion support
* purefa\_network \- Converted to REST v2
* purefa\_ntp \- Added Fusion support\.
* purefa\_offload \- Added Fusion support
* purefa\_pod \- Added support for SafeMode protection group configuration
* purefa\_policy \- Added Fusion support
* purefa\_policy \- Upgraded to REST v2
* purefa\_syslog \- Added Fusion support\.
* purefa\_syslog\_settings \- Added Fusion support
* purefa\_timeout \- Added Fusion support
* purefa\_user \- All AD users to have SSH keys and/or API tokens assigned\, even if they have never accessed the FlashArray before\. AD users must have <code>ad\_user</code> set as <code>true</code>\.
* purefa\_volume\_tags \- Add <em class="title-reference">tag</em> parameter to specify tag to be deleted by key name
* purefa\_volume\_tags \- Upgraded to REST v2 and added Fusion support

<a id="purestorage-flashblade-3"></a>
#### purestorage\.flashblade

* module\_utils/purefb \- Remove <em class="title-reference">get\_blade\(\)</em> function as not required for REST v2
* purefb\_ad \- Revert removal of <code>service</code> parameter \(breaking change\)\. Added more logic to use of <code>service</code> parameter and recommend use of <code>service\_principals</code> with service incorporated\.
* purefb\_ad \- <code>service</code> parameter removed to comply with underlying API structure\. <code>service</code> should be included in the <code>service\_principals</code> strings as shown in the documentation\.
* purefb\_admin \- Remove references to unsupported API versions
* purefb\_alert \- Add new <code>state</code> of <code>test</code> to check alert manager configuration
* purefb\_alert \- Upgraded to REST v2
* purefb\_banner \- Upgraded to REST v2
* purefb\_bladename \- Upgraded to REST v2
* purefb\_bucket \- Added Fusion support
* purefb\_bucket \- Updated to REST v2
* purefb\_bucket\_access \- Fusion support added
* purefb\_bucket\_replica \- Add Fusion support
* purefb\_bucket\_replica \- Upgraded to REST v2
* purefb\_certgrp \- Upgraded to REST v2
* purefb\_connect \- Added Fusion support
* purefb\_connect \- Remove references to unsupported API versions
* purefb\_connect \- Upgraded to REST v2
* purefb\_ds \- Added new state of <code>test</code> to enable directory services to run diagnostics test
* purefb\_ds \- Updated to REST v2
* purefb\_dsrole \- Upgraded to REST v2
* purefb\_eula \- Converted to REST v2
* purefb\_fs \- Added support for Fusion
* purefb\_fs \- Upgraded to use REST 2
* purefb\_fs\_replica \- Upgraded to REST v2
* purefb\_groupquota \- Fusion support added
* purefb\_groupquota \- Upgraded to REST v2
* purefb\_info \- Upgraded to REST v2
* purefb\_inventory \- Upgraded to REST v2
* purefb\_lifecycle \- Fusion support added
* purefb\_lifecycle \- Upgraded to REST v2
* purefb\_network \- Upgraded to REST v2
* purefb\_ntp \- Upgraded to REST v2
* purefb\_phonehome \- Add new <code>state</code> of <code>test</code> to check phonehome configuration
* purefb\_phonehome \- Upgrwded to REST v2
* purefb\_pingtrace \- Ehanced JSON response for ping
* purefb\_policy \- Add Fusion support
* purefb\_policy \- Remove references to unsupported API versions
* purefb\_policy \- Upgraded to REST v2
* purefb\_ra \- Add new <code>state</code> of <code>test</code> to check remote support configuration
* purefb\_remote\_cred \- Fusion support added
* purefb\_remote\_cred \- Upgraded to REST v2
* purefb\_s3acc \- Fusion support added
* purefb\_s3acc \- Remove references to unsupported API versions
* purefb\_s3user \- Fusion support added
* purefb\_saml \- Added <code>entity\_id</code> parameter
* purefb\_snamp\_agent \- Upgraded to REST v2
* purefb\_snap \- Add support to delete/eradicate remote snapshots\, including the latest replica
* purefb\_snap \- Fusion support added
* purefb\_snap \- Upgraded to REST v2
* purefb\_snmp\_mgr \- Add new <code>state</code> of <code>test</code> to check SNMP manager configuration
* purefb\_snmp\_mgr \- Upgraded to REST v2
* purefb\_subnet \- Upgraded to REST v2
* purefb\_syslog \- Converted to REST v2
* purefb\_target \- Upgraded to REST v2
* purefb\_user \- All AD users to have SSH keys and/or API tokens assigned\, even if they have never accessed the FlashArray before\. AD users must have <code>ad\_user</code> set as <code>true</code>\.
* purefb\_userpolicy \- Fusion support added
* purefb\_userquota \- Added Fusion support
* purefb\_userquota \- Upgraded to REST v2
* purefb\_virtualhost \- Fusion support added

<a id="theforeman-foreman-5"></a>
#### theforeman\.foreman

* content\_upload \- fall\-back to rpm binary when library can\'t be imported
* registration\_command \- clarify example to show where the generated command needs to be executed

<a id="vmware-vmware-7"></a>
#### vmware\.vmware

* Add module for importing iso images to content library\.
* Remove six imports from \_facts\.py and \_vsphere\_tasks\.py due to new sanity rules\. Python 2 \(already not supported\) will fail to execute these files\.
* tag\_associations \- Add module to manage tag associations with objects
* tag\_categories \- Add module to manage tag categories
* tags \- Add module to manage tags
* vms \- Add option to inventory plugin to gather cluster and ESXi host name for VMs\. \(Fixes [https\://github\.com/ansible\-collections/vmware\.vmware/issues/215](https\://github\.com/ansible\-collections/vmware\.vmware/issues/215)\)

<a id="breaking-changes--porting-guide-1"></a>
### Breaking Changes / Porting Guide

<a id="ansible-core-18"></a>
#### Ansible\-core

* powershell \- Removed code that tried to remote quotes from paths when performing Windows operations like copying and fetching file\. This should not affect normal playbooks unless a value is quoted too many times\.

<a id="community-docker-7"></a>
#### community\.docker

* All doc fragments\, module utils\, and plugin utils are from now on private\. They can change at any time\, and have breaking changes even in bugfix releases \([https\://github\.com/ansible\-collections/community\.docker/pull/1144](https\://github\.com/ansible\-collections/community\.docker/pull/1144)\)\.

<a id="community-general-21"></a>
#### community\.general

* mh\.base module utils \- <code>debug</code> will now always be delegated to the underlying <code>AnsibleModule</code> object \([https\://github\.com/ansible\-collections/community\.general/pull/10883](https\://github\.com/ansible\-collections/community\.general/pull/10883)\)\.
* oneview module utils \- remove import of standard library <code>os</code> \([https\://github\.com/ansible\-collections/community\.general/pull/10644](https\://github\.com/ansible\-collections/community\.general/pull/10644)\)\.
* slack \- the default of <code>prepend\_hash</code> changed from <code>auto</code> to <code>never</code> \([https\://github\.com/ansible\-collections/community\.general/pull/10883](https\://github\.com/ansible\-collections/community\.general/pull/10883)\)\.

<a id="community-mysql-5"></a>
#### community\.mysql

* Since version 4\.0\.0\, the collection accepts code written in Python 3\. Modules aren\'t tested against Python 2 and might not work in Python 2 environments\.
* collection \- stop testing against mysqlclient connector as its support was deprecated in this collection \- use PyMySQL connector instead\! It\'ll stop working in 5\.0\.0 when we remove all related code \([https\://github\.com/ansible\-collections/community\.mysql/issues/654](https\://github\.com/ansible\-collections/community\.mysql/issues/654)\)\.
* mysql\_db \- the <code>pipefail</code> argument\'s default value is set to <code>true</code>\.  If your target machines do not use <code>bash</code> as a default interpreter\, set <code>pipefail</code> to <code>false</code> explicitly\. However\, we strongly recommend setting up <code>bash</code> as a default and <code>pipefail\=true</code> as it will protect you from getting broken dumps you don\'t know about \([https\://github\.com/ansible\-collections/community\.mysql/issues/407](https\://github\.com/ansible\-collections/community\.mysql/issues/407)\)\.
* mysql\_info \- The <code>users\_info</code> filter does not return the <code>plugin\_auth\_string</code> field anymore\. Use the <em class="title-reference">plugin\_hash\_string</em> return value instead \([https\://github\.com/ansible\-collections/community\.mysql/pull/629](https\://github\.com/ansible\-collections/community\.mysql/pull/629)\)\.
* mysql\_role \- the <code>column\_case\_sensitive</code> argument\'s default value has been changed to <code>true</code>\. If your playbook expected the column to be automatically uppercased for your users privileges\, you should set this to <code>false</code> explicitly \([https\://github\.com/ansible\-collections/community\.mysql/issues/578](https\://github\.com/ansible\-collections/community\.mysql/issues/578)\)\.
* mysql\_user \- the <code>column\_case\_sensitive</code> argument\'s default value has been changed to <code>true</code>\. If your playbook expected the column to be automatically uppercased for your users privileges\, you should set this to <code>false</code> explicitly \([https\://github\.com/ansible\-collections/community\.mysql/issues/577](https\://github\.com/ansible\-collections/community\.mysql/issues/577)\)\.

<a id="community-vmware-4"></a>
#### community\.vmware

* Removed support for ansible\-core \< 2\.19\.0\.
* Removed support for vmware\.vmware \< 2\.0\.0\.
* Replace the dependencies on <code>pyvmomi</code>\, <code>vmware\-vcenter</code> and <code>vmware\-vapi\-common\-client</code> with <code>vcf\-sdk</code> \([https\://github\.com/ansible\-collections/community\.vmware/pull/2457](https\://github\.com/ansible\-collections/community\.vmware/pull/2457)\)\.

<a id="hetzner-hcloud-8"></a>
#### hetzner\.hcloud

* Drop support for Python 3\.9
* Drop support for ansible\-core 2\.17

<a id="ibm-storage-virtualize-5"></a>
#### ibm\.storage\_virtualize

* ibm\_sv\_manage\_flashsystem\_grid \- The flashsystem grid module now uses newer FlashSystem REST APIs to perform tasks\.

<a id="deprecated-features-6"></a>
### Deprecated Features

<a id="ansible-core-19"></a>
#### Ansible\-core

* Deprecated the shell plugin\'s <code>wrap\_for\_exec</code> function\. This API is not used in Ansible or any known collection and is being removed to simplify the plugin API\. Plugin authors should wrap their command to execute within an explicit shell or other known executable\.
* INJECT\_FACTS\_AS\_VARS configuration currently defaults to <code>True</code>\, this is now deprecated and it will switch to <code>False</code> by Ansible 2\.24\. You will only get notified if you are accessing \'injected\' facts \(for example\, ansible\_os\_distribution vs ansible\_facts\[\'os\_distribution\'\]\)\.
* hash\_params function in roles/\_\_init\_\_ is being deprecated as it is not in use\.
* include\_vars \- Specifying \'ignore\_files\' as a string is deprecated\.
* vars\, the internal variable cache will be removed in 2\.24\. This cache\, once used internally exposes variables in inconsistent states\, the \'vars\' and \'varnames\' lookups should be used instead\.

<a id="community-general-22"></a>
#### community\.general

* catapult \- module is deprecated and will be removed in community\.general 13\.0\.0 \([https\://github\.com/ansible\-collections/community\.general/issues/10318](https\://github\.com/ansible\-collections/community\.general/issues/10318)\, [https\://github\.com/ansible\-collections/community\.general/pull/10329](https\://github\.com/ansible\-collections/community\.general/pull/10329)\)\.
* cpanm \- deprecate <code>mode\=compatibility</code>\, <code>mode\=new</code> should be used instead \([https\://github\.com/ansible\-collections/community\.general/pull/10434](https\://github\.com/ansible\-collections/community\.general/pull/10434)\)\.
* dimensiondata doc\_fragments plugin \- fragments is deprecated and will be removed in community\.general 13\.0\.0 \([https\://github\.com/ansible\-collections/community\.general/pull/10986](https\://github\.com/ansible\-collections/community\.general/pull/10986)\)\.
* dimensiondata module\_utils plugin \- utils is deprecated and will be removed in community\.general 13\.0\.0 \([https\://github\.com/ansible\-collections/community\.general/pull/10986](https\://github\.com/ansible\-collections/community\.general/pull/10986)\)\.
* dimensiondata\_network \- module is deprecated and will be removed in community\.general 13\.0\.0 \([https\://github\.com/ansible\-collections/community\.general/pull/10986](https\://github\.com/ansible\-collections/community\.general/pull/10986)\)\.
* dimensiondata\_vlan \- module is deprecated and will be removed in community\.general 13\.0\.0 \([https\://github\.com/ansible\-collections/community\.general/pull/10986](https\://github\.com/ansible\-collections/community\.general/pull/10986)\)\.
* dimensiondata\_wait doc\_fragments plugin \- fragments is deprecated and will be removed in community\.general 13\.0\.0 \([https\://github\.com/ansible\-collections/community\.general/pull/10986](https\://github\.com/ansible\-collections/community\.general/pull/10986)\)\.
* github\_repo \- deprecate <code>force\_defaults\=true</code> \([https\://github\.com/ansible\-collections/community\.general/pull/10435](https\://github\.com/ansible\-collections/community\.general/pull/10435)\)\.
* hiera lookup plugin \- retrieving data with Hiera has been deprecated a long time ago\; because of that this plugin will be removed from community\.general 13\.0\.0\. If you disagree with this deprecation\, please create an issue in the community\.general repository \([https\://github\.com/ansible\-collections/community\.general/issues/4462](https\://github\.com/ansible\-collections/community\.general/issues/4462)\, [https\://github\.com/ansible\-collections/community\.general/pull/10779](https\://github\.com/ansible\-collections/community\.general/pull/10779)\)\.
* oci\_utils module utils \- utils is deprecated and will be removed in community\.general 13\.0\.0 \([https\://github\.com/ansible\-collections/community\.general/issues/10318](https\://github\.com/ansible\-collections/community\.general/issues/10318)\, [https\://github\.com/ansible\-collections/community\.general/pull/10652](https\://github\.com/ansible\-collections/community\.general/pull/10652)\)\.
* oci\_vcn \- module is deprecated and will be removed in community\.general 13\.0\.0 \([https\://github\.com/ansible\-collections/community\.general/issues/10318](https\://github\.com/ansible\-collections/community\.general/issues/10318)\, [https\://github\.com/ansible\-collections/community\.general/pull/10652](https\://github\.com/ansible\-collections/community\.general/pull/10652)\)\.
* oneandone module utils \- DNS fails to resolve the API endpoint used by the module\. The module is deprecated and will be removed in community\.general 13\.0\.0 \([https\://github\.com/ansible\-collections/community\.general/pull/10994](https\://github\.com/ansible\-collections/community\.general/pull/10994)\)\.
* oneandone\_firewall\_policy \- DNS fails to resolve the API endpoint used by the module\. The module is deprecated and will be removed in community\.general 13\.0\.0 \([https\://github\.com/ansible\-collections/community\.general/pull/10994](https\://github\.com/ansible\-collections/community\.general/pull/10994)\)\.
* oneandone\_load\_balancer \- DNS fails to resolve the API endpoint used by the module\. The module is deprecated and will be removed in community\.general 13\.0\.0 \([https\://github\.com/ansible\-collections/community\.general/pull/10994](https\://github\.com/ansible\-collections/community\.general/pull/10994)\)\.
* oneandone\_monitoring\_policy \- DNS fails to resolve the API endpoint used by the module\. The module is deprecated and will be removed in community\.general 13\.0\.0 \([https\://github\.com/ansible\-collections/community\.general/pull/10994](https\://github\.com/ansible\-collections/community\.general/pull/10994)\)\.
* oneandone\_private\_network \- DNS fails to resolve the API endpoint used by the module\. The module is deprecated and will be removed in community\.general 13\.0\.0 \([https\://github\.com/ansible\-collections/community\.general/pull/10994](https\://github\.com/ansible\-collections/community\.general/pull/10994)\)\.
* oneandone\_public\_ip \- DNS fails to resolve the API endpoint used by the module\. The module is deprecated and will be removed in community\.general 13\.0\.0 \([https\://github\.com/ansible\-collections/community\.general/pull/10994](https\://github\.com/ansible\-collections/community\.general/pull/10994)\)\.
* oneandone\_server \- DNS fails to resolve the API endpoint used by the module\. The module is deprecated and will be removed in community\.general 13\.0\.0 \([https\://github\.com/ansible\-collections/community\.general/pull/10994](https\://github\.com/ansible\-collections/community\.general/pull/10994)\)\.
* oracle\* doc fragments \- fragments are deprecated and will be removed in community\.general 13\.0\.0 \([https\://github\.com/ansible\-collections/community\.general/issues/10318](https\://github\.com/ansible\-collections/community\.general/issues/10318)\, [https\://github\.com/ansible\-collections/community\.general/pull/10652](https\://github\.com/ansible\-collections/community\.general/pull/10652)\)\.
* pacemaker\_cluster \- the state <code>cleanup</code> will be removed from community\.general 14\.0\.0 \([https\://github\.com/ansible\-collections/community\.general/pull/10741](https\://github\.com/ansible\-collections/community\.general/pull/10741)\)\.
* rocketchat \- the default value for <code>is\_pre740</code>\, currently <code>true</code>\, is deprecated and will change to <code>false</code> in community\.general 13\.0\.0 \([https\://github\.com/ansible\-collections/community\.general/pull/10490](https\://github\.com/ansible\-collections/community\.general/pull/10490)\)\.
* typetalk \- module is deprecated and will be removed in community\.general 13\.0\.0 \([https\://github\.com/ansible\-collections/community\.general/pull/9499](https\://github\.com/ansible\-collections/community\.general/pull/9499)\)\.

<a id="community-hrobot-2"></a>
#### community\.hrobot

* storagebox\* modules \- membership in the <code>community\.hrobot\.robot</code> action group \(module defaults group\) is deprecated\; the modules will be removed from the group in community\.hrobot 3\.0\.0\. Use <code>community\.hrobot\.api</code> instead \([https\://github\.com/ansible\-collections/community\.hrobot/pull/178](https\://github\.com/ansible\-collections/community\.hrobot/pull/178)\)\.
* storagebox\* modules \- the <code>hetzner\_token</code> option for these modules will be required from community\.hrobot 3\.0\.0 on \([https\://github\.com/ansible\-collections/community\.hrobot/pull/178](https\://github\.com/ansible\-collections/community\.hrobot/pull/178)\)\.
* storagebox\* modules \- the <code>hetzner\_user</code> and <code>hetzner\_pass</code> options for these modules are deprecated\; support will be removed in community\.hrobot 3\.0\.0\. Use <code>hetzner\_token</code> instead \([https\://github\.com/ansible\-collections/community\.hrobot/pull/178](https\://github\.com/ansible\-collections/community\.hrobot/pull/178)\)\.
* storagebox\_info \- the <code>storageboxes\[\]\.login</code>\, <code>storageboxes\[\]\.disk\_quota</code>\, <code>storageboxes\[\]\.disk\_usage</code>\, <code>storageboxes\[\]\.disk\_usage\_data</code>\, <code>storageboxes\[\]\.disk\_usage\_snapshot</code>\, <code>storageboxes\[\]\.webdav</code>\, <code>storageboxes\[\]\.samba</code>\, <code>storageboxes\[\]\.ssh</code>\, <code>storageboxes\[\]\.external\_reachability</code>\, and <code>storageboxes\[\]\.zfs</code> return values are deprecated and will be removed from community\.routeros\. Check out the documentation to find out their new names according to the new API \([https\://github\.com/ansible\-collections/community\.hrobot/pull/178](https\://github\.com/ansible\-collections/community\.hrobot/pull/178)\)\.
* storagebox\_snapshot\_info \- the <code>snapshots\[\]\.timestamp</code>\, <code>snapshots\[\]\.size</code>\, <code>snapshots\[\]\.filesystem\_size</code>\, <code>snapshots\[\]\.automatic</code>\, and <code>snapshots\[\]\.comment</code> return values are deprecated and will be removed from community\.routeros\. Check out the documentation to find out their new names according to the new API \([https\://github\.com/ansible\-collections/community\.hrobot/pull/178](https\://github\.com/ansible\-collections/community\.hrobot/pull/178)\)\.
* storagebox\_snapshot\_plan \- the <code>plans\[\]\.month</code> return value is deprecated\, since it only returns <code>null</code> with the new API and cannot be set to any other value \([https\://github\.com/ansible\-collections/community\.hrobot/pull/178](https\://github\.com/ansible\-collections/community\.hrobot/pull/178)\)\.
* storagebox\_snapshot\_plan\_info \- the <code>plans\[\]\.month</code> return value is deprecated\, since it only returns <code>null</code> with the new API and cannot be set to any other value \([https\://github\.com/ansible\-collections/community\.hrobot/pull/178](https\://github\.com/ansible\-collections/community\.hrobot/pull/178)\)\.
* storagebox\_subaccount \- <code>password\_mode\=set\-to\-random</code> is deprecated and will be removed from community\.hrobot 3\.0\.0\. Hetzner\'s new API does not support this anyway\, it can only be used with the legacy API \([https\://github\.com/ansible\-collections/community\.hrobot/pull/183](https\://github\.com/ansible\-collections/community\.hrobot/pull/183)\)\.
* storagebox\_subaccount \- the <code>subaccount\.homedirectory</code>\, <code>subaccount\.samba</code>\, <code>subaccount\.ssh</code>\, <code>subaccount\.external\_reachability</code>\, <code>subaccount\.webdav</code>\, <code>subaccount\.readonly</code>\, <code>subaccount\.createtime</code>\, and <code>subaccount\.comment</code> return values are deprecated and will be removed from community\.routeros\. Check out the documentation to find out their new names according to the new API \([https\://github\.com/ansible\-collections/community\.hrobot/pull/178](https\://github\.com/ansible\-collections/community\.hrobot/pull/178)\)\.
* storagebox\_subaccount\_info \- the <code>subaccounts\[\]\.accountid</code>\, <code>subaccounts\[\]\.homedirectory</code>\, <code>subaccounts\[\]\.samba</code>\, <code>subaccounts\[\]\.ssh</code>\, <code>subaccounts\[\]\.external\_reachability</code>\, <code>subaccounts\[\]\.webdav</code>\, <code>subaccounts\[\]\.readonly</code>\, <code>subaccounts\[\]\.createtime</code>\, and <code>subaccounts\[\]\.comment</code> return values are deprecated and will be removed from community\.routeros\. Check out the documentation to find out their new names according to the new API \([https\://github\.com/ansible\-collections/community\.hrobot/pull/178](https\://github\.com/ansible\-collections/community\.hrobot/pull/178)\)\.

<a id="community-vmware-5"></a>
#### community\.vmware

* vmware\_guest\_snapshot \- the module has been deprecated and will be removed in community\.vmware 8\.0\.0 \([https\://github\.com/ansible\-collections/community\.vmware/pull/2467](https\://github\.com/ansible\-collections/community\.vmware/pull/2467)\)\.

<a id="community-zabbix-3"></a>
#### community\.zabbix

* zabbix\_maintenance module \- Depreicated <em class="title-reference">minutes</em> argument for <em class="title-reference">time\_periods</em>

<a id="dellemc-powerflex-1"></a>
#### dellemc\.powerflex

* The device\, info\, protection\_domain\, snapshot\, storagepool and volume modules are supported only on PowerFlex Gen1\. They are replaced by v2 modules on PowerFlex Gen2\.
* The fault\_set\, replication\_consistency\_group\, replication\_pair\, resource\_group and sds modules are not supported on PowerFlex Gen2\.

<a id="hetzner-hcloud-9"></a>
#### hetzner\.hcloud

* server\_type\_info \- Deprecate Server Type <code>deprecation</code> property\.

<a id="purestorage-flasharray-5"></a>
#### purestorage\.flasharray

* purefa\_volume\_tags \- Deprecated due to removal of REST 1\.x support\. Will be removed in Collection 2\.0\.0

<a id="removed-features-previously-deprecated"></a>
### Removed Features \(previously deprecated\)

* The deprecated <code>community\.digitalocean</code> collection has been removed \([https\://forum\.ansible\.com/t/44602](https\://forum\.ansible\.com/t/44602)\)\.
* The deprecated <code>ibm\.qradar</code> collection has been removed \([https\://forum\.ansible\.com/t/44259](https\://forum\.ansible\.com/t/44259)\)\.

<a id="ansible-core-20"></a>
#### Ansible\-core

* Removed the option to set the <code>DEFAULT\_TRANSPORT</code> configuration to <code>smart</code> that selects the default transport as either <code>ssh</code> or <code>paramiko</code> based on the underlying platform configuraton\.
* <code>vault</code>/<code>unvault</code> filters \- remove the deprecated <code>vaultid</code> parameter\.
* ansible\-doc \- role entrypoint attributes are no longer shown
* ansible\-galaxy \- remove support for resolvelib \>\= 0\.5\.3\, \< 0\.8\.0\.
* ansible\-galaxy \- removed the v2 Galaxy server API\. Galaxy servers hosting collections must support v3\.
* dnf/dnf5 \- remove deprecated <code>install\_repoquery</code> option\.
* encrypt \- remove deprecated passlib\_or\_crypt API\.
* paramiko \- Removed the <code>PARAMIKO\_HOST\_KEY\_AUTO\_ADD</code> and <code>PARAMIKO\_LOOK\_FOR\_KEYS</code> configuration keys\, which were previously deprecated\.
* py3compat \- remove deprecated <code>py3compat\.environ</code> call\.
* vars plugins \- removed the deprecated <code>get\_host\_vars</code> or <code>get\_group\_vars</code> fallback for vars plugins that do not inherit from <code>BaseVarsPlugin</code> and define a <code>get\_vars</code> method\.
* yum\_repository \- remove deprecated <code>keepcache</code> option\.

<a id="community-docker-8"></a>
#### community\.docker

* Remove support for Docker SDK for Python version 1\.x\.y\, also known as <code>docker\-py</code>\. Modules and plugins that use Docker SDK for Python require version 2\.0\.0\+ \([https\://github\.com/ansible\-collections/community\.docker/pull/1171](https\://github\.com/ansible\-collections/community\.docker/pull/1171)\)\.
* The collection no longer supports Python 3\.6 and before\. Note that this coincides with the Python requirements of ansible\-core 2\.17\+ \([https\://github\.com/ansible\-collections/community\.docker/pull/1123](https\://github\.com/ansible\-collections/community\.docker/pull/1123)\)\.
* The collection no longer supports ansible\-core 2\.15 and 2\.16\. You need ansible\-core 2\.17\.0 or newer to use community\.docker 5\.x\.y \([https\://github\.com/ansible\-collections/community\.docker/pull/1123](https\://github\.com/ansible\-collections/community\.docker/pull/1123)\)\.

<a id="community-general-23"></a>
#### community\.general

* Ansible\-core 2\.16 is no longer supported\. This also means that the collection now requires Python 3\.7\+ \([https\://github\.com/ansible\-collections/community\.general/pull/10884](https\://github\.com/ansible\-collections/community\.general/pull/10884)\)\.
* bearychat \- the module has been removed as the chat service is no longer available \([https\://github\.com/ansible\-collections/community\.general/pull/10883](https\://github\.com/ansible\-collections/community\.general/pull/10883)\)\.
* cmd\_runner module utils \- the parameter <code>ignore\_value\_none</code> to <code>CmdRunner\.\_\_call\_\_\(\)</code> has been removed \([https\://github\.com/ansible\-collections/community\.general/pull/10883](https\://github\.com/ansible\-collections/community\.general/pull/10883)\)\.
* cmd\_runner\_fmt module utils \- the parameter <code>ctx\_ignore\_none</code> to argument formatters has been removed \([https\://github\.com/ansible\-collections/community\.general/pull/10883](https\://github\.com/ansible\-collections/community\.general/pull/10883)\)\.
* facter \- the module has been replaced by <code>community\.general\.facter\_facts</code> \([https\://github\.com/ansible\-collections/community\.general/pull/10883](https\://github\.com/ansible\-collections/community\.general/pull/10883)\)\.
* mh\.deco module utils \- the parameters <code>on\_success</code> and <code>on\_failure</code> of <code>cause\(\)</code> have been removed\; use <code>when\=\"success\"</code> and <code>when\=\"failure\"</code> instead \([https\://github\.com/ansible\-collections/community\.general/pull/10883](https\://github\.com/ansible\-collections/community\.general/pull/10883)\)\.
* opkg \- the value <code>\"\"</code> for the option <code>force</code> is no longer allowed\. Omit <code>force</code> instead \([https\://github\.com/ansible\-collections/community\.general/pull/10883](https\://github\.com/ansible\-collections/community\.general/pull/10883)\)\.
* pacemaker\_cluster \- the option <code>state</code> is now required \([https\://github\.com/ansible\-collections/community\.general/pull/10883](https\://github\.com/ansible\-collections/community\.general/pull/10883)\)\.
* pure module utils \- the modules using this module utils have been removed from community\.general 3\.0\.0 \([https\://github\.com/ansible\-collections/community\.general/pull/10883](https\://github\.com/ansible\-collections/community\.general/pull/10883)\)\.
* purestorage doc fragment \- the modules using this doc fragment have been removed from community\.general 3\.0\.0 \([https\://github\.com/ansible\-collections/community\.general/pull/10883](https\://github\.com/ansible\-collections/community\.general/pull/10883)\)\.
* yaml callback plugin \- the deprecated plugin has been removed\. Use the default callback with <code>result\_format\=yaml</code> instead \([https\://github\.com/ansible\-collections/community\.general/pull/10883](https\://github\.com/ansible\-collections/community\.general/pull/10883)\)\.

<a id="community-vmware-6"></a>
#### community\.vmware

* vmware\_cluster \- The deprecated module has been removed\. Use <code>vmware\.vmware\.cluster</code> instead \([https\://github\.com/ansible\-collections/community\.vmware/pull/2455](https\://github\.com/ansible\-collections/community\.vmware/pull/2455)\)\.
* vmware\_cluster\_dpm \- The deprecated module has been removed\. Use <code>vmware\.vmware\.cluster\_dpm</code> instead \([https\://github\.com/ansible\-collections/community\.vmware/pull/2455](https\://github\.com/ansible\-collections/community\.vmware/pull/2455)\)\.
* vmware\_cluster\_drs \- The deprecated module has been removed\. Use <code>vmware\.vmware\.cluster\_drs</code> instead \([https\://github\.com/ansible\-collections/community\.vmware/pull/2455](https\://github\.com/ansible\-collections/community\.vmware/pull/2455)\)\.
* vmware\_cluster\_drs\_recommendations \- The deprecated module has been removed\. Use <code>vmware\.vmware\.cluster\_drs\_recommendations</code> instead \([https\://github\.com/ansible\-collections/community\.vmware/pull/2455](https\://github\.com/ansible\-collections/community\.vmware/pull/2455)\)\.
* vmware\_cluster\_vcls \- The deprecated module has been removed\. Use <code>vmware\.vmware\.cluster\_vcls</code> instead \([https\://github\.com/ansible\-collections/community\.vmware/pull/2455](https\://github\.com/ansible\-collections/community\.vmware/pull/2455)\)\.

<a id="security-fixes-2"></a>
### Security Fixes

<a id="community-general-24"></a>
#### community\.general

* keycloak\_user \- the parameter <code>credentials\[\]\.value</code> is now marked as <code>no\_log\=true</code>\. Before it was logged by Ansible\, unless the task was marked as <code>no\_log\: true</code>\. Since this parameter can be used for passwords\, this resulted in credential leaking \([https\://github\.com/ansible\-collections/community\.general/issues/11000](https\://github\.com/ansible\-collections/community\.general/issues/11000)\, [https\://github\.com/ansible\-collections/community\.general/pull/11005](https\://github\.com/ansible\-collections/community\.general/pull/11005)\)\.

<a id="bugfixes-6"></a>
### Bugfixes

<a id="ansible-core-21"></a>
#### Ansible\-core

* Do not re\-add <code>tags</code> on blocks from within <code>import\_tasks</code>\.
* Fix issue where play tags prevented executing notified handlers \([https\://github\.com/ansible/ansible/issues/85475](https\://github\.com/ansible/ansible/issues/85475)\)
* Fix issues with keywords being incorrectly validated on <code>import\_tasks</code> \([https\://github\.com/ansible/ansible/issues/85855](https\://github\.com/ansible/ansible/issues/85855)\, [https\://github\.com/ansible/ansible/issues/85856](https\://github\.com/ansible/ansible/issues/85856)\)
* Fix traceback when trying to import non\-existing file via nested <code>import\_tasks</code> \([https\://github\.com/ansible/ansible/issues/69882](https\://github\.com/ansible/ansible/issues/69882)\)
* SIGINT/SIGTERM Handling \- Make SIGINT/SIGTERM handling more robust by splitting concerns between forks and the parent\.
* The <code>ansible\_failed\_task</code> variable is now correctly exposed in a rescue section\, even when a failing handler is triggered by the <code>flush\_handlers</code> task in the corresponding <code>block</code> \([https\://github\.com/ansible/ansible/issues/85682](https\://github\.com/ansible/ansible/issues/85682)\)
* Windows \- ignore temporary file cleanup warning when using AnsibleModule to compile C\# utils\. This should reduce the number of warnings that can safely be ignored when running PowerShell modules \- [https\://github\.com/ansible/ansible/issues/85976](https\://github\.com/ansible/ansible/issues/85976)
* Windows async \- Handle running PowerShell modules with trailing data after the module result
* <code>ansible\-galaxy collection list</code> \- fail when none of the configured collection paths exist\.
* <code>ternary</code> filter \- evaluate values lazily \([https\://github\.com/ansible/ansible/issues/85743](https\://github\.com/ansible/ansible/issues/85743)\)
* ansible\-doc \- prevent crash when scanning collections in paths that have more than one <code>ansible\_collections</code> in it \([https\://github\.com/ansible/ansible/issues/84909](https\://github\.com/ansible/ansible/issues/84909)\, [https\://github\.com/ansible/ansible/pull/85361](https\://github\.com/ansible/ansible/pull/85361)\)\.
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
* config lookup now properly factors in variables and show\_origin when checking entries from the global configuration\.
* display \- Fixed reference to undefined <em class="title-reference">\_DeferredWarningContext</em> when issuing early warnings during startup\. \([https\://github\.com/ansible/ansible/issues/85886](https\://github\.com/ansible/ansible/issues/85886)\)
* dnf \- Check if installroot is directory or not \([https\://github\.com/ansible/ansible/issues/85680](https\://github\.com/ansible/ansible/issues/85680)\)\.
* failed\_when \- When using <code>failed\_when</code> to suppress an error\, the <code>exception</code> key in the result is renamed to <code>failed\_when\_suppressed\_exception</code>\. This prevents the error from being displayed by callbacks after being suppressed\. \([https\://github\.com/ansible/ansible/issues/85505](https\://github\.com/ansible/ansible/issues/85505)\)
* fetch \- also return <code>file</code> in the result when changed is <code>True</code> \([https\://github\.com/ansible/ansible/pull/85729](https\://github\.com/ansible/ansible/pull/85729)\)\.
* import\_tasks \- fix templating parent include arguments\.
* include\_role \- allow host specific values in all <code>\*\_from</code> arguments \([https\://github\.com/ansible/ansible/issues/66497](https\://github\.com/ansible/ansible/issues/66497)\)
* option argument deprecations now have a proper alternative help text\.
* package\_facts \- typecast bytes to string while returning facts \([https\://github\.com/ansible/ansible/issues/85937](https\://github\.com/ansible/ansible/issues/85937)\)\.
* pip \- Fix pip module output so that it returns changed when the only operation is initializing a venv\.
* plugins config\, get\_option\_and\_origin now correctly displays the value and origin of the option\.
* psrp \- ReadTimeout exceptions now mark host as unreachable instead of fatal \([https\://github\.com/ansible/ansible/issues/85966](https\://github\.com/ansible/ansible/issues/85966)\)
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

<a id="amazon-aws-6"></a>
#### amazon\.aws

* Remove <code>ansible\.module\_utils\.six</code> imports to avoid warnings \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2727](https\://github\.com/ansible\-collections/amazon\.aws/pull/2727)\)\.
* amazon\.aws\.autoscaling\_instance \- setting the state to <code>terminated</code> had no effect\. The fix implements missing instance termination state \([https\://github\.com/ansible\-collections/amazon\.aws/issues/2719](https\://github\.com/ansible\-collections/amazon\.aws/issues/2719)\)\.
* ec2\_vpc\_nacl \- Fix issue when trying to update existing Network ACL rule \([https\://github\.com/ansible\-collections/amazon\.aws/issues/2592](https\://github\.com/ansible\-collections/amazon\.aws/issues/2592)\)\.
* s3\_object \- Honor headers for content and content\_base64 uploads by promoting supported keys \(e\.g\. ContentType\, ContentDisposition\, CacheControl\) to top\-level S3 arguments and placing remaining keys under Metadata\. This makes content uploads consistent with src uploads\. \([https\://github\.com/ansible\-collections/amazon\.aws](https\://github\.com/ansible\-collections/amazon\.aws)\)

<a id="cisco-ios-6"></a>
#### cisco\.ios

* Fixed an issue where configuration within an address family \(ipv6\) was ignored by the parser\.
* cisco\.ios\.ios\_bgp\_address\_family \- Encrypted strings as password are not evaluated rather treated as string forcefully\.
* cisco\.ios\.ios\_hsrp\_interfaces \- Fixed default values for version and priority\.
* cisco\.ios\.ios\_hsrp\_interfaces \- Fixed overridden state to be idempotent with ipv6 configuration\.
* cisco\.ios\.ios\_hsrp\_interfaces \- Fixed parsers to group HSRP configuration and optimize parsing time\.
* cisco\.ios\.ios\_hsrp\_interfaces \- Fixed removal of HSRP configuration when state is deleted\, replaced\, overridden\.
* cisco\.ios\.ios\_hsrp\_interfaces \- Fixed rendered output for standby redirect advertisement authentication key\-chain\.
* cisco\.ios\.ios\_hsrp\_interfaces \- Fixed rendered output for standby redirect advertisement authentication key\-string with encryption\.
* cisco\.ios\.ios\_hsrp\_interfaces \- Fixed rendered output for standby redirect advertisement authentication\.
* cisco\.ios\.ios\_hsrp\_interfaces \- Handle operation of list attributes like ipv6\, ip\, track\.
* cisco\.ios\.ios\_l2\_interfaces \- Add private\-vlan support to switchport\.
* cisco\.ios\.ios\_vrf\_global \- fixed issue preventing idempotent configuration of multiple import/export route\-targets for a VRF\.
* ios\_hsrp\_interfaces \- Device defaults version to 1 if standby\_groups is present but version is not configured\. and module would also consider priority as 100 if not configured\, to maintain idempotency\.
* ios\_hsrp\_interfaces \- Fixed operation for ipv6 standby configuration\.
* ios\_static\_routes \- Fix parsing of static routes with interface and distance in gathered state

<a id="cisco-meraki-6"></a>
#### cisco\.meraki

* Enhanced networks\_switch\_qos\_rules\_order object lookup logic to properly match QoS rules by vlan\, protocol\, srcPort\, and dstPort parameters
* Fixed VLAN parameter handling in networks\_switch\_qos\_rules\_order changed name parameter to vlan parameter for proper object lookup
* Fixed comparison function call in networks\_switch\_dscp\_to\_cos\_mappings changed \'meraki\_compare\_equality2\' to \'meraki\_compare\_equality\'
* Fixed function name typo in organizations\_appliance\_vpn\_third\_party\_vpnpeers changed \'getOrganizationApplianceVpnThirdPartyVpnpeers\' to \'getOrganizationApplianceVpnThirdPartyVPNPeers\'
* Fixed function name typo in organizations\_appliance\_vpn\_third\_party\_vpnpeers changed \'updateOrganizationApplianceVpnThirdPartyVpnpeers\' to \'updateOrganizationApplianceVpnThirdPartyVPNPeers\'
* Fixed parameter handling in networks\_switch\_qos\_rules\_order to use qosRuleId instead of id for object identification
* Improved dictionary comparison logic in meraki\.py plugin utils to handle nested dictionaries correctly
* Improved meraki\_compare\_equality2 function to handle None value comparisons more accurately
* Updated networks\_switch\_qos\_rules\_order playbook with corrected parameter values and VLAN configuration
* cisco\.meraki\.devices\_appliance\_uplinks\_settings \- fix idempotency error\.
* networks\_switch\_qos\_rules\_order\: extend object lookup to include srcPortRange and dstPortRange when matching existing QoS rules to improve idempotency

<a id="community-crypto-4"></a>
#### community\.crypto

* Avoid deprecated functionality in ansible\-core 2\.20 \([https\://github\.com/ansible\-collections/community\.crypto/pull/953](https\://github\.com/ansible\-collections/community\.crypto/pull/953)\)\.
* Smaller code cleanup \([https\://github\.com/ansible\-collections/community\.crypto/pull/963](https\://github\.com/ansible\-collections/community\.crypto/pull/963)\)\.

<a id="community-dns-8"></a>
#### community\.dns

* Avoid using <code>ansible\.module\_utils\.six</code> in more places to avoid deprecation warnings with ansible\-core 2\.20 \([https\://github\.com/ansible\-collections/community\.dns/pull/291](https\://github\.com/ansible\-collections/community\.dns/pull/291)\)\.
* Avoid using <code>ansible\.module\_utils\.six</code> to avoid deprecation warnings with ansible\-core 2\.20 \([https\://github\.com/ansible\-collections/community\.dns/pull/287](https\://github\.com/ansible\-collections/community\.dns/pull/287)\)\.
* Update Public Suffix List\.

<a id="community-docker-9"></a>
#### community\.docker

* Avoid deprecated functionality in ansible\-core 2\.20 \([https\://github\.com/ansible\-collections/community\.docker/pull/1117](https\://github\.com/ansible\-collections/community\.docker/pull/1117)\)\.
* Avoid remaining usages of deprecated <code>ansible\.module\_utils\.six</code> \([https\://github\.com/ansible\-collections/community\.docker/pull/1133](https\://github\.com/ansible\-collections/community\.docker/pull/1133)\)\.
* Avoid usage of deprecated <code>ansible\.module\_utils\.six</code> in all code that does not have to support Python 2 \([https\://github\.com/ansible\-collections/community\.docker/pull/1137](https\://github\.com/ansible\-collections/community\.docker/pull/1137)\, [https\://github\.com/ansible\-collections/community\.docker/pull/1139](https\://github\.com/ansible\-collections/community\.docker/pull/1139)\)\.
* Avoid usage of deprecated <code>ansible\.module\_utils\.six</code> in some of the code that still supports Python 2 \([https\://github\.com/ansible\-collections/community\.docker/pull/1138](https\://github\.com/ansible\-collections/community\.docker/pull/1138)\)\.
* docker connection plugin \- fix crash instead of warning if Docker version does not support <code>remote\_user</code> \([https\://github\.com/ansible\-collections/community\.docker/pull/1161](https\://github\.com/ansible\-collections/community\.docker/pull/1161)\)\.
* docker\, nsenter connection plugins \- fix handling of <code>become</code> plugin password prompt handling in case multiple events arrive at the same time \([https\://github\.com/ansible\-collections/community\.docker/pull/1158](https\://github\.com/ansible\-collections/community\.docker/pull/1158)\)\.
* docker\_api connection plugin \- fix bug that could lead to loss of data when waiting for <code>become</code> plugin prompt \([https\://github\.com/ansible\-collections/community\.docker/pull/1152](https\://github\.com/ansible\-collections/community\.docker/pull/1152)\)\.
* docker\_compose\_v2\_exec \- fix crash instead of reporting error if <code>detach\=true</code> and <code>stdin</code> is provided \([https\://github\.com/ansible\-collections/community\.docker/pull/1161](https\://github\.com/ansible\-collections/community\.docker/pull/1161)\)\.
* docker\_compose\_v2\_run \- fix crash instead of reporting error if <code>detach\=true</code> and <code>stdin</code> is provided \([https\://github\.com/ansible\-collections/community\.docker/pull/1161](https\://github\.com/ansible\-collections/community\.docker/pull/1161)\)\.
* docker\_compose\_v2\_run \- when <code>detach\=true</code>\, ensure that the returned container ID is not a bytes string \([https\://github\.com/ansible\-collections/community\.docker/pull/1183](https\://github\.com/ansible\-collections/community\.docker/pull/1183)\)\.
* docker\_container\_exec \- fix bug that could lead to loss of stdout/stderr data \([https\://github\.com/ansible\-collections/community\.docker/pull/1152](https\://github\.com/ansible\-collections/community\.docker/pull/1152)\)\.
* docker\_container\_exec \- make <code>detach\=true</code> work\. So far this resulted in no execution being done \([https\://github\.com/ansible\-collections/community\.docker/pull/1145](https\://github\.com/ansible\-collections/community\.docker/pull/1145)\)\.
* docker\_image \- fix \'Cannot locate specified Dockerfile\' error \([https\://github\.com/ansible\-collections/community\.docker/pull/1184](https\://github\.com/ansible\-collections/community\.docker/pull/1184)\)\.
* docker\_plugin \- fix diff mode for plugin options \([https\://github\.com/ansible\-collections/community\.docker/pull/1146](https\://github\.com/ansible\-collections/community\.docker/pull/1146)\)\.

<a id="community-general-25"></a>
#### community\.general

* Avoid deprecated functionality in ansible\-core 2\.20 \([https\://github\.com/ansible\-collections/community\.general/pull/10687](https\://github\.com/ansible\-collections/community\.general/pull/10687)\)\.
* Avoid usage of deprecated <code>ansible\.module\_utils\.six</code> in all code that does not have to support Python 2 \([https\://github\.com/ansible\-collections/community\.general/pull/10873](https\://github\.com/ansible\-collections/community\.general/pull/10873)\)\.
* Remove all usage of <code>ansible\.module\_utils\.six</code> \([https\://github\.com/ansible\-collections/community\.general/pull/10888](https\://github\.com/ansible\-collections/community\.general/pull/10888)\)\.
* \_filelock module utils \- improve Python code \([https\://github\.com/ansible\-collections/community\.general/pull/11043](https\://github\.com/ansible\-collections/community\.general/pull/11043)\)\.
* aerospike\_migrations \- improve Python code by removing unnecessary variables \([https\://github\.com/ansible\-collections/community\.general/pull/11049](https\://github\.com/ansible\-collections/community\.general/pull/11049)\)\.
* aix\_lvol \- improve Python code by removing unnecessary variables \([https\://github\.com/ansible\-collections/community\.general/pull/11049](https\://github\.com/ansible\-collections/community\.general/pull/11049)\)\.
* ali\_instance \- improve Python code \([https\://github\.com/ansible\-collections/community\.general/pull/11043](https\://github\.com/ansible\-collections/community\.general/pull/11043)\)\.
* ali\_instance \- improve Python code by removing unnecessary variables \([https\://github\.com/ansible\-collections/community\.general/pull/11049](https\://github\.com/ansible\-collections/community\.general/pull/11049)\)\.
* ali\_instance\_info \- improve Python code \([https\://github\.com/ansible\-collections/community\.general/pull/11043](https\://github\.com/ansible\-collections/community\.general/pull/11043)\)\.
* apache2\_module \- avoid ansible\-core 2\.19 deprecation \([https\://github\.com/ansible\-collections/community\.general/pull/10459](https\://github\.com/ansible\-collections/community\.general/pull/10459)\)\.
* apache2\_module \- check the <code>cgi</code> module restrictions only during activation \([https\://github\.com/ansible\-collections/community\.general/pull/10423](https\://github\.com/ansible\-collections/community\.general/pull/10423)\)\.
* apk \- fix check for empty/whitespace\-only package names \([https\://github\.com/ansible\-collections/community\.general/pull/10532](https\://github\.com/ansible\-collections/community\.general/pull/10532)\)\.
* apk \- handle empty name strings properly \([https\://github\.com/ansible\-collections/community\.general/issues/10441](https\://github\.com/ansible\-collections/community\.general/issues/10441)\, [https\://github\.com/ansible\-collections/community\.general/pull/10442](https\://github\.com/ansible\-collections/community\.general/pull/10442)\)\.
* apt\_rpm \- improve Python code \([https\://github\.com/ansible\-collections/community\.general/pull/11043](https\://github\.com/ansible\-collections/community\.general/pull/11043)\)\.
* apt\_rpm \- improve Python code by removing unnecessary variables \([https\://github\.com/ansible\-collections/community\.general/pull/11049](https\://github\.com/ansible\-collections/community\.general/pull/11049)\)\.
* btrfs module utils \- improve Python code \([https\://github\.com/ansible\-collections/community\.general/pull/11043](https\://github\.com/ansible\-collections/community\.general/pull/11043)\)\.
* btrfs module utils \- improve Python code by removing unnecessary variables \([https\://github\.com/ansible\-collections/community\.general/pull/11049](https\://github\.com/ansible\-collections/community\.general/pull/11049)\)\.
* btrfs\_subvolume \- improve Python code \([https\://github\.com/ansible\-collections/community\.general/pull/11043](https\://github\.com/ansible\-collections/community\.general/pull/11043)\)\.
* btrfs\_subvolume \- improve Python code by removing unnecessary variables \([https\://github\.com/ansible\-collections/community\.general/pull/11049](https\://github\.com/ansible\-collections/community\.general/pull/11049)\)\.
* capabilities \- using invalid path \(symlink/directory/\.\.\.\) returned unrelated and incoherent error messages \([https\://github\.com/ansible\-collections/community\.general/issues/5649](https\://github\.com/ansible\-collections/community\.general/issues/5649)\, [https\://github\.com/ansible\-collections/community\.general/pull/10455](https\://github\.com/ansible\-collections/community\.general/pull/10455)\)\.
* chef\_databag lookup plugin \- improve Python code by removing unnecessary variables \([https\://github\.com/ansible\-collections/community\.general/pull/11049](https\://github\.com/ansible\-collections/community\.general/pull/11049)\)\.
* cloudflare\_dns \- roll back changes to CAA record validation \([https\://github\.com/ansible\-collections/community\.general/issues/10934](https\://github\.com/ansible\-collections/community\.general/issues/10934)\, [https\://github\.com/ansible\-collections/community\.general/pull/10956](https\://github\.com/ansible\-collections/community\.general/pull/10956)\)\.
* cloudflare\_dns \- roll back changes to SRV record validation \([https\://github\.com/ansible\-collections/community\.general/issues/10934](https\://github\.com/ansible\-collections/community\.general/issues/10934)\, [https\://github\.com/ansible\-collections/community\.general/pull/10937](https\://github\.com/ansible\-collections/community\.general/pull/10937)\)\.
* consul \- improve Python code \([https\://github\.com/ansible\-collections/community\.general/pull/11043](https\://github\.com/ansible\-collections/community\.general/pull/11043)\)\.
* consul\_kv lookup plugin \- improve Python code by removing unnecessary variables \([https\://github\.com/ansible\-collections/community\.general/pull/11049](https\://github\.com/ansible\-collections/community\.general/pull/11049)\)\.
* cronvar \- fix crash on missing <code>cron\_file</code> parent directories \([https\://github\.com/ansible\-collections/community\.general/issues/10460](https\://github\.com/ansible\-collections/community\.general/issues/10460)\, [https\://github\.com/ansible\-collections/community\.general/pull/10461](https\://github\.com/ansible\-collections/community\.general/pull/10461)\)\.
* cronvar \- handle empty strings on <code>value</code> properly  \([https\://github\.com/ansible\-collections/community\.general/issues/10439](https\://github\.com/ansible\-collections/community\.general/issues/10439)\, [https\://github\.com/ansible\-collections/community\.general/pull/10445](https\://github\.com/ansible\-collections/community\.general/pull/10445)\)\.
* cronvar \- improve Python code \([https\://github\.com/ansible\-collections/community\.general/pull/11043](https\://github\.com/ansible\-collections/community\.general/pull/11043)\)\.
* dependent lookup plugin \- avoid deprecated ansible\-core 2\.19 functionality \([https\://github\.com/ansible\-collections/community\.general/pull/10359](https\://github\.com/ansible\-collections/community\.general/pull/10359)\)\.
* discord \- improve Python code by removing unnecessary variables \([https\://github\.com/ansible\-collections/community\.general/pull/11049](https\://github\.com/ansible\-collections/community\.general/pull/11049)\)\.
* dnf\_versionlock \- improve Python code \([https\://github\.com/ansible\-collections/community\.general/pull/11043](https\://github\.com/ansible\-collections/community\.general/pull/11043)\)\.
* dnsmadeeasy \- improve Python code \([https\://github\.com/ansible\-collections/community\.general/pull/11043](https\://github\.com/ansible\-collections/community\.general/pull/11043)\)\.
* doas become plugin \- disable pipelining on ansible\-core 2\.19\+\. The plugin does not work with pipelining\, and since ansible\-core 2\.19 become plugins can indicate that they do not work with pipelining \([https\://github\.com/ansible\-collections/community\.general/issues/9977](https\://github\.com/ansible\-collections/community\.general/issues/9977)\, [https\://github\.com/ansible\-collections/community\.general/pull/10537](https\://github\.com/ansible\-collections/community\.general/pull/10537)\)\.
* dpkg\_divert \- improve Python code by removing unnecessary variables \([https\://github\.com/ansible\-collections/community\.general/pull/11049](https\://github\.com/ansible\-collections/community\.general/pull/11049)\)\.
* elastic callback plugin \- improve Python code by removing unnecessary variables \([https\://github\.com/ansible\-collections/community\.general/pull/11049](https\://github\.com/ansible\-collections/community\.general/pull/11049)\)\.
* filesystem \- avoid false positive change detection on XFS resize due to unusable slack space \([https\://github\.com/ansible\-collections/community\.general/pull/11033](https\://github\.com/ansible\-collections/community\.general/pull/11033)\)\.
* gem \- fix soundness issue when uninstalling default gems on Ubuntu  \([https\://github\.com/ansible\-collections/community\.general/issues/10451](https\://github\.com/ansible\-collections/community\.general/issues/10451)\, [https\://github\.com/ansible\-collections/community\.general/pull/10689](https\://github\.com/ansible\-collections/community\.general/pull/10689)\)\.
* github\_app\_access\_token lookup plugin \- fix compatibility imports for using jwt \([https\://github\.com/ansible\-collections/community\.general/issues/10807](https\://github\.com/ansible\-collections/community\.general/issues/10807)\, [https\://github\.com/ansible\-collections/community\.general/pull/10810](https\://github\.com/ansible\-collections/community\.general/pull/10810)\)\.
* github\_deploy\_key \- fix bug during error handling if no body was present in the result \([https\://github\.com/ansible\-collections/community\.general/issues/10853](https\://github\.com/ansible\-collections/community\.general/issues/10853)\, [https\://github\.com/ansible\-collections/community\.general/pull/10857](https\://github\.com/ansible\-collections/community\.general/pull/10857)\)\.
* github\_release \- support multiple types of GitHub tokens\; no longer failing when <code>ghs\_</code> token type is provided \([https\://github\.com/ansible\-collections/community\.general/issues/10338](https\://github\.com/ansible\-collections/community\.general/issues/10338)\, [https\://github\.com/ansible\-collections/community\.general/pull/10339](https\://github\.com/ansible\-collections/community\.general/pull/10339)\)\.
* gitlab module utils \- improve Python code by removing unnecessary variables \([https\://github\.com/ansible\-collections/community\.general/pull/11049](https\://github\.com/ansible\-collections/community\.general/pull/11049)\)\.
* gitlab\_branch \- improve Python code by removing unnecessary variables \([https\://github\.com/ansible\-collections/community\.general/pull/11049](https\://github\.com/ansible\-collections/community\.general/pull/11049)\)\.
* gitlab\_group\_members \- improve Python code by removing unnecessary variables \([https\://github\.com/ansible\-collections/community\.general/pull/11049](https\://github\.com/ansible\-collections/community\.general/pull/11049)\)\.
* gitlab\_issue \- improve Python code \([https\://github\.com/ansible\-collections/community\.general/pull/11043](https\://github\.com/ansible\-collections/community\.general/pull/11043)\)\.
* gitlab\_merge\_request \- improve Python code \([https\://github\.com/ansible\-collections/community\.general/pull/11043](https\://github\.com/ansible\-collections/community\.general/pull/11043)\)\.
* gitlab\_project \- improve Python code \([https\://github\.com/ansible\-collections/community\.general/pull/11043](https\://github\.com/ansible\-collections/community\.general/pull/11043)\)\.
* gitlab\_project\_members \- improve Python code by removing unnecessary variables \([https\://github\.com/ansible\-collections/community\.general/pull/11049](https\://github\.com/ansible\-collections/community\.general/pull/11049)\)\.
* gitlab\_protected\_branch \- improve Python code by removing unnecessary variables \([https\://github\.com/ansible\-collections/community\.general/pull/11049](https\://github\.com/ansible\-collections/community\.general/pull/11049)\)\.
* gitlab\_runner \- fix exception in check mode when a new runner is created \([https\://github\.com/ansible\-collections/community\.general/issues/8854](https\://github\.com/ansible\-collections/community\.general/issues/8854)\)\.
* gitlab\_user \- improve Python code \([https\://github\.com/ansible\-collections/community\.general/pull/11043](https\://github\.com/ansible\-collections/community\.general/pull/11043)\)\.
* haproxy \- improve Python code \([https\://github\.com/ansible\-collections/community\.general/pull/11043](https\://github\.com/ansible\-collections/community\.general/pull/11043)\)\.
* homebrew \- do not fail when cask or formula name has changed in homebrew repo \([https\://github\.com/ansible\-collections/community\.general/issues/10804](https\://github\.com/ansible\-collections/community\.general/issues/10804)\, [https\://github\.com/ansible\-collections/community\.general/pull/10805](https\://github\.com/ansible\-collections/community\.general/pull/10805)\)\.
* homebrew \- improve Python code \([https\://github\.com/ansible\-collections/community\.general/pull/11043](https\://github\.com/ansible\-collections/community\.general/pull/11043)\)\.
* homebrew\_services \- improve Python code \([https\://github\.com/ansible\-collections/community\.general/pull/11043](https\://github\.com/ansible\-collections/community\.general/pull/11043)\)\.
* hpilo\_boot \- improve Python code \([https\://github\.com/ansible\-collections/community\.general/pull/11043](https\://github\.com/ansible\-collections/community\.general/pull/11043)\)\.
* htpasswd \- avoid ansible\-core 2\.19 deprecation \([https\://github\.com/ansible\-collections/community\.general/pull/10459](https\://github\.com/ansible\-collections/community\.general/pull/10459)\)\.
* icinga2 inventory plugin \- avoid using deprecated option when templating options \([https\://github\.com/ansible\-collections/community\.general/pull/10271](https\://github\.com/ansible\-collections/community\.general/pull/10271)\)\.
* incus connection plugin \- fix error handling to return more useful Ansible errors to the user \([https\://github\.com/ansible\-collections/community\.general/issues/10344](https\://github\.com/ansible\-collections/community\.general/issues/10344)\, [https\://github\.com/ansible\-collections/community\.general/pull/10349](https\://github\.com/ansible\-collections/community\.general/pull/10349)\)\.
* infinity \- improve Python code by removing unnecessary variables \([https\://github\.com/ansible\-collections/community\.general/pull/11049](https\://github\.com/ansible\-collections/community\.general/pull/11049)\)\.
* ini\_file \- improve Python code \([https\://github\.com/ansible\-collections/community\.general/pull/11043](https\://github\.com/ansible\-collections/community\.general/pull/11043)\)\.
* interfaces\_file \- improve Python code by removing unnecessary variables \([https\://github\.com/ansible\-collections/community\.general/pull/11049](https\://github\.com/ansible\-collections/community\.general/pull/11049)\)\.
* ipa\_group \- improve Python code by removing unnecessary variables \([https\://github\.com/ansible\-collections/community\.general/pull/11049](https\://github\.com/ansible\-collections/community\.general/pull/11049)\)\.
* ipa\_otptoken \- improve Python code \([https\://github\.com/ansible\-collections/community\.general/pull/11043](https\://github\.com/ansible\-collections/community\.general/pull/11043)\)\.
* ipa\_vault \- improve Python code by removing unnecessary variables \([https\://github\.com/ansible\-collections/community\.general/pull/11049](https\://github\.com/ansible\-collections/community\.general/pull/11049)\)\.
* ipmi\_boot \- improve Python code by removing unnecessary variables \([https\://github\.com/ansible\-collections/community\.general/pull/11049](https\://github\.com/ansible\-collections/community\.general/pull/11049)\)\.
* irc \- pass hostname to <code>wrap\_socket\(\)</code> if <code>use\_tls\=true</code> and <code>validate\_certs\=true</code> \([https\://github\.com/ansible\-collections/community\.general/issues/10472](https\://github\.com/ansible\-collections/community\.general/issues/10472)\, [https\://github\.com/ansible\-collections/community\.general/pull/10491](https\://github\.com/ansible\-collections/community\.general/pull/10491)\)\.
* jenkins\_build \- improve Python code by removing unnecessary variables \([https\://github\.com/ansible\-collections/community\.general/pull/11049](https\://github\.com/ansible\-collections/community\.general/pull/11049)\)\.
* jenkins\_build\_info \- improve Python code by removing unnecessary variables \([https\://github\.com/ansible\-collections/community\.general/pull/11049](https\://github\.com/ansible\-collections/community\.general/pull/11049)\)\.
* jenkins\_credential \- improve Python code \([https\://github\.com/ansible\-collections/community\.general/pull/11043](https\://github\.com/ansible\-collections/community\.general/pull/11043)\)\.
* jenkins\_plugin \- improve Python code \([https\://github\.com/ansible\-collections/community\.general/pull/11043](https\://github\.com/ansible\-collections/community\.general/pull/11043)\)\.
* jenkins\_plugin \- improve Python code by removing unnecessary variables \([https\://github\.com/ansible\-collections/community\.general/pull/11049](https\://github\.com/ansible\-collections/community\.general/pull/11049)\)\.
* jenkins\_plugin \- install latest compatible version instead of latest \([https\://github\.com/ansible\-collections/community\.general/issues/854](https\://github\.com/ansible\-collections/community\.general/issues/854)\, [https\://github\.com/ansible\-collections/community\.general/pull/10346](https\://github\.com/ansible\-collections/community\.general/pull/10346)\)\.
* jenkins\_plugin \- separate Jenkins and external URL credentials \([https\://github\.com/ansible\-collections/community\.general/issues/4419](https\://github\.com/ansible\-collections/community\.general/issues/4419)\, [https\://github\.com/ansible\-collections/community\.general/pull/10346](https\://github\.com/ansible\-collections/community\.general/pull/10346)\)\.
* json\_patch filter plugin \- improve Python code \([https\://github\.com/ansible\-collections/community\.general/pull/11043](https\://github\.com/ansible\-collections/community\.general/pull/11043)\)\.
* json\_query filter plugin \- make compatible with lazy evaluation list and dictionary types of ansible\-core 2\.19 \([https\://github\.com/ansible\-collections/community\.general/pull/10539](https\://github\.com/ansible\-collections/community\.general/pull/10539)\)\.
* kdeconfig \- <code>kwriteconfig</code> executable could not be discovered automatically on systems with only <code>kwriteconfig6</code> installed\. <code>kwriteconfig6</code> can now be discovered by Ansible \([https\://github\.com/ansible\-collections/community\.general/issues/10746](https\://github\.com/ansible\-collections/community\.general/issues/10746)\, [https\://github\.com/ansible\-collections/community\.general/pull/10751](https\://github\.com/ansible\-collections/community\.general/pull/10751)\)\.
* kea\_command \- improve Python code \([https\://github\.com/ansible\-collections/community\.general/pull/11043](https\://github\.com/ansible\-collections/community\.general/pull/11043)\)\.
* keycloak\_authz\_permission \- improve Python code \([https\://github\.com/ansible\-collections/community\.general/pull/11043](https\://github\.com/ansible\-collections/community\.general/pull/11043)\)\.
* keycloak\_clientscope\_type \- improve Python code \([https\://github\.com/ansible\-collections/community\.general/pull/11043](https\://github\.com/ansible\-collections/community\.general/pull/11043)\)\.
* keycloak\_clientsecret\, keycloak\_clientsecret\_info \- make <code>client\_auth</code> work \([https\://github\.com/ansible\-collections/community\.general/issues/10932](https\://github\.com/ansible\-collections/community\.general/issues/10932)\, [https\://github\.com/ansible\-collections/community\.general/pull/10933](https\://github\.com/ansible\-collections/community\.general/pull/10933)\)\.
* keycloak\_component \- improve Python code by removing unnecessary variables \([https\://github\.com/ansible\-collections/community\.general/pull/11049](https\://github\.com/ansible\-collections/community\.general/pull/11049)\)\.
* keycloak\_group \- fixes an issue where module ignores realm when searching subgroups by name \([https\://github\.com/ansible\-collections/community\.general/pull/10840](https\://github\.com/ansible\-collections/community\.general/pull/10840)\)\.
* keycloak\_realm \- support setting <code>adminPermissionsEnabled</code> for a realm \([https\://github\.com/ansible\-collections/community\.general/issues/10962](https\://github\.com/ansible\-collections/community\.general/issues/10962)\)\.
* keycloak\_realm\_key \- improve Python code by removing unnecessary variables \([https\://github\.com/ansible\-collections/community\.general/pull/11049](https\://github\.com/ansible\-collections/community\.general/pull/11049)\)\.
* keycloak\_role \- fixes an issue where the module incorrectly returns <code>changed\=true</code> when using the alias <code>clientId</code> in composite roles \([https\://github\.com/ansible\-collections/community\.general/pull/10829](https\://github\.com/ansible\-collections/community\.general/pull/10829)\)\.
* keycloak\_user\_execute\_actions\_email \- improve Python code \([https\://github\.com/ansible\-collections/community\.general/pull/11043](https\://github\.com/ansible\-collections/community\.general/pull/11043)\)\.
* keycloak\_user\_federation \- improve Python code \([https\://github\.com/ansible\-collections/community\.general/pull/11043](https\://github\.com/ansible\-collections/community\.general/pull/11043)\)\.
* keycloak\_userprofile \- improve Python code by removing unnecessary variables \([https\://github\.com/ansible\-collections/community\.general/pull/11049](https\://github\.com/ansible\-collections/community\.general/pull/11049)\)\.
* launchd \- improve Python code by removing unnecessary variables \([https\://github\.com/ansible\-collections/community\.general/pull/11049](https\://github\.com/ansible\-collections/community\.general/pull/11049)\)\.
* linode inventory plugin \- avoid using deprecated option when templating options \([https\://github\.com/ansible\-collections/community\.general/pull/10271](https\://github\.com/ansible\-collections/community\.general/pull/10271)\)\.
* linode inventory plugin \- improve Python code \([https\://github\.com/ansible\-collections/community\.general/pull/11043](https\://github\.com/ansible\-collections/community\.general/pull/11043)\)\.
* listen\_port\_facts \- avoid crash when required commands are missing \([https\://github\.com/ansible\-collections/community\.general/issues/10457](https\://github\.com/ansible\-collections/community\.general/issues/10457)\, [https\://github\.com/ansible\-collections/community\.general/pull/10458](https\://github\.com/ansible\-collections/community\.general/pull/10458)\)\.
* listen\_ports\_facts \- improve Python code \([https\://github\.com/ansible\-collections/community\.general/pull/11043](https\://github\.com/ansible\-collections/community\.general/pull/11043)\)\.
* listen\_ports\_facts \- improve Python code by removing unnecessary variables \([https\://github\.com/ansible\-collections/community\.general/pull/11049](https\://github\.com/ansible\-collections/community\.general/pull/11049)\)\.
* logentries callback plugin \- improve Python code by removing unnecessary variables \([https\://github\.com/ansible\-collections/community\.general/pull/11049](https\://github\.com/ansible\-collections/community\.general/pull/11049)\)\.
* logstash callback plugin \- remove reference to Python 2 library \([https\://github\.com/ansible\-collections/community\.general/pull/10345](https\://github\.com/ansible\-collections/community\.general/pull/10345)\)\.
* lvm\_pv \- properly detect SCSI or NVMe devices to rescan \([https\://github\.com/ansible\-collections/community\.general/issues/10444](https\://github\.com/ansible\-collections/community\.general/issues/10444)\, [https\://github\.com/ansible\-collections/community\.general/pull/10596](https\://github\.com/ansible\-collections/community\.general/pull/10596)\)\.
* lxc\_container \- improve Python code \([https\://github\.com/ansible\-collections/community\.general/pull/11043](https\://github\.com/ansible\-collections/community\.general/pull/11043)\)\.
* lxd\_container \- improve Python code \([https\://github\.com/ansible\-collections/community\.general/pull/11043](https\://github\.com/ansible\-collections/community\.general/pull/11043)\)\.
* machinectl become plugin \- disable pipelining on ansible\-core 2\.19\+\. The plugin does not work with pipelining\, and since ansible\-core 2\.19 become plugins can indicate that they do not work with pipelining \([https\://github\.com/ansible\-collections/community\.general/pull/10537](https\://github\.com/ansible\-collections/community\.general/pull/10537)\)\.
* manageiq\_alert\_profiles \- improve Python code by removing unnecessary variables \([https\://github\.com/ansible\-collections/community\.general/pull/11049](https\://github\.com/ansible\-collections/community\.general/pull/11049)\)\.
* manageiq\_provider \- improve Python code by removing unnecessary variables \([https\://github\.com/ansible\-collections/community\.general/pull/11049](https\://github\.com/ansible\-collections/community\.general/pull/11049)\)\.
* manageiq\_tenant \- improve Python code by removing unnecessary variables \([https\://github\.com/ansible\-collections/community\.general/pull/11049](https\://github\.com/ansible\-collections/community\.general/pull/11049)\)\.
* matrix \- improve Python code \([https\://github\.com/ansible\-collections/community\.general/pull/11043](https\://github\.com/ansible\-collections/community\.general/pull/11043)\)\.
* maven\_artifact \- improve Python code \([https\://github\.com/ansible\-collections/community\.general/pull/11043](https\://github\.com/ansible\-collections/community\.general/pull/11043)\)\.
* memset\_memstore\_info \- improve Python code by removing unnecessary variables \([https\://github\.com/ansible\-collections/community\.general/pull/11049](https\://github\.com/ansible\-collections/community\.general/pull/11049)\)\.
* memset\_server\_info \- improve Python code by removing unnecessary variables \([https\://github\.com/ansible\-collections/community\.general/pull/11049](https\://github\.com/ansible\-collections/community\.general/pull/11049)\)\.
* memset\_zone \- improve Python code by removing unnecessary variables \([https\://github\.com/ansible\-collections/community\.general/pull/11049](https\://github\.com/ansible\-collections/community\.general/pull/11049)\)\.
* merge\_variables lookup plugin \- avoid deprecated functionality from ansible\-core 2\.19 \([https\://github\.com/ansible\-collections/community\.general/pull/10566](https\://github\.com/ansible\-collections/community\.general/pull/10566)\)\.
* module\_helper module utils \- improve Python code \([https\://github\.com/ansible\-collections/community\.general/pull/11043](https\://github\.com/ansible\-collections/community\.general/pull/11043)\)\.
* monit \- fix crash caused by an unknown status value returned from the monit service \([https\://github\.com/ansible\-collections/community\.general/issues/10742](https\://github\.com/ansible\-collections/community\.general/issues/10742)\, [https\://github\.com/ansible\-collections/community\.general/pull/10743](https\://github\.com/ansible\-collections/community\.general/pull/10743)\)\.
* monit \- improve Python code \([https\://github\.com/ansible\-collections/community\.general/pull/11043](https\://github\.com/ansible\-collections/community\.general/pull/11043)\)\.
* netcup\_dns \- improve Python code \([https\://github\.com/ansible\-collections/community\.general/pull/11043](https\://github\.com/ansible\-collections/community\.general/pull/11043)\)\.
* nmcli \- improve Python code \([https\://github\.com/ansible\-collections/community\.general/pull/11043](https\://github\.com/ansible\-collections/community\.general/pull/11043)\)\.
* nomad\_job \- improve Python code \([https\://github\.com/ansible\-collections/community\.general/pull/11043](https\://github\.com/ansible\-collections/community\.general/pull/11043)\)\.
* nosh \- improve Python code by removing unnecessary variables \([https\://github\.com/ansible\-collections/community\.general/pull/11049](https\://github\.com/ansible\-collections/community\.general/pull/11049)\)\.
* npm \- improve Python code \([https\://github\.com/ansible\-collections/community\.general/pull/11043](https\://github\.com/ansible\-collections/community\.general/pull/11043)\)\.
* odbc \- improve Python code by removing unnecessary variables \([https\://github\.com/ansible\-collections/community\.general/pull/11049](https\://github\.com/ansible\-collections/community\.general/pull/11049)\)\.
* omapi\_host \- make return values compatible with ansible\-core 2\.19 and Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/11001](https\://github\.com/ansible\-collections/community\.general/pull/11001)\)\.
* one\_host \- improve Python code \([https\://github\.com/ansible\-collections/community\.general/pull/11043](https\://github\.com/ansible\-collections/community\.general/pull/11043)\)\.
* one\_image \- improve Python code \([https\://github\.com/ansible\-collections/community\.general/pull/11043](https\://github\.com/ansible\-collections/community\.general/pull/11043)\)\.
* one\_service \- improve Python code by removing unnecessary variables \([https\://github\.com/ansible\-collections/community\.general/pull/11049](https\://github\.com/ansible\-collections/community\.general/pull/11049)\)\.
* one\_template \- improve Python code \([https\://github\.com/ansible\-collections/community\.general/pull/11043](https\://github\.com/ansible\-collections/community\.general/pull/11043)\)\.
* one\_vm \- improve Python code \([https\://github\.com/ansible\-collections/community\.general/pull/11043](https\://github\.com/ansible\-collections/community\.general/pull/11043)\)\.
* one\_vm \- improve Python code by removing unnecessary variables \([https\://github\.com/ansible\-collections/community\.general/pull/11049](https\://github\.com/ansible\-collections/community\.general/pull/11049)\)\.
* one\_vnet \- improve Python code \([https\://github\.com/ansible\-collections/community\.general/pull/11043](https\://github\.com/ansible\-collections/community\.general/pull/11043)\)\.
* oneandone module utils \- improve Python code \([https\://github\.com/ansible\-collections/community\.general/pull/11043](https\://github\.com/ansible\-collections/community\.general/pull/11043)\)\.
* onepassword\_doc and onepassword\_ssh\_key lookup plugins \- ensure that all connection parameters are passed to CLI class \([https\://github\.com/ansible\-collections/community\.general/pull/10965](https\://github\.com/ansible\-collections/community\.general/pull/10965)\)\.
* onepassword\_info \- improve Python code \([https\://github\.com/ansible\-collections/community\.general/pull/11043](https\://github\.com/ansible\-collections/community\.general/pull/11043)\)\.
* online inventory plugin \- improve Python code by removing unnecessary variables \([https\://github\.com/ansible\-collections/community\.general/pull/11049](https\://github\.com/ansible\-collections/community\.general/pull/11049)\)\.
* opendj\_backendprop \- improve Python code by removing unnecessary variables \([https\://github\.com/ansible\-collections/community\.general/pull/11049](https\://github\.com/ansible\-collections/community\.general/pull/11049)\)\.
* opennebula module utils \- improve Python code \([https\://github\.com/ansible\-collections/community\.general/pull/11043](https\://github\.com/ansible\-collections/community\.general/pull/11043)\)\.
* opentelemetry callback plugin \- improve Python code by removing unnecessary variables \([https\://github\.com/ansible\-collections/community\.general/pull/11049](https\://github\.com/ansible\-collections/community\.general/pull/11049)\)\.
* ovh\_monthly\_billing \- improve Python code by removing unnecessary variables \([https\://github\.com/ansible\-collections/community\.general/pull/11049](https\://github\.com/ansible\-collections/community\.general/pull/11049)\)\.
* pacemaker \- use regex for matching <code>maintenance\-mode</code> output to determine cluster maintenance status \([https\://github\.com/ansible\-collections/community\.general/issues/10426](https\://github\.com/ansible\-collections/community\.general/issues/10426)\, [https\://github\.com/ansible\-collections/community\.general/pull/10707](https\://github\.com/ansible\-collections/community\.general/pull/10707)\)\.
* pacemaker\_resource \- fix <code>resource\_type</code> parameter formatting \([https\://github\.com/ansible\-collections/community\.general/issues/10426](https\://github\.com/ansible\-collections/community\.general/issues/10426)\, [https\://github\.com/ansible\-collections/community\.general/pull/10663](https\://github\.com/ansible\-collections/community\.general/pull/10663)\)\.
* pamd \- improve Python code \([https\://github\.com/ansible\-collections/community\.general/pull/11043](https\://github\.com/ansible\-collections/community\.general/pull/11043)\)\.
* parted \- variable is a list\, not text \([https\://github\.com/ansible\-collections/community\.general/pull/10823](https\://github\.com/ansible\-collections/community\.general/pull/10823)\, [https\://github\.com/ansible\-collections/community\.general/issues/10817](https\://github\.com/ansible\-collections/community\.general/issues/10817)\)\.
* pids \- prevent error when an empty string is provided for <code>name</code> \([https\://github\.com/ansible\-collections/community\.general/issues/10672](https\://github\.com/ansible\-collections/community\.general/issues/10672)\, [https\://github\.com/ansible\-collections/community\.general/pull/10688](https\://github\.com/ansible\-collections/community\.general/pull/10688)\)\.
* pkgin \- improve Python code \([https\://github\.com/ansible\-collections/community\.general/pull/11043](https\://github\.com/ansible\-collections/community\.general/pull/11043)\)\.
* portinstall \- improve Python code by removing unnecessary variables \([https\://github\.com/ansible\-collections/community\.general/pull/11049](https\://github\.com/ansible\-collections/community\.general/pull/11049)\)\.
* pritunl\_user \- improve resilience when comparing user parameters if remote fields are <code>null</code> or missing\. List parameters \(<code>groups</code>\, <code>mac\_addresses</code>\) now safely default to empty lists for comparison and avoids <code>KeyError</code> issues \([https\://github\.com/ansible\-collections/community\.general/issues/10954](https\://github\.com/ansible\-collections/community\.general/issues/10954)\, [https\://github\.com/ansible\-collections/community\.general/pull/10955](https\://github\.com/ansible\-collections/community\.general/pull/10955)\)\.
* pulp\_repo \- improve Python code \([https\://github\.com/ansible\-collections/community\.general/pull/11043](https\://github\.com/ansible\-collections/community\.general/pull/11043)\)\.
* random\_string lookup plugin \- replace <code>random\.SystemRandom\(\)</code> with <code>secrets\.SystemRandom\(\)</code> when generating strings\. This has no practical effect\, as both are the same \([https\://github\.com/ansible\-collections/community\.general/pull/10893](https\://github\.com/ansible\-collections/community\.general/pull/10893)\)\.
* redfish\_utils module utils \- improve Python code by removing unnecessary variables \([https\://github\.com/ansible\-collections/community\.general/pull/11049](https\://github\.com/ansible\-collections/community\.general/pull/11049)\)\.
* redhat\_subscription \- improve Python code \([https\://github\.com/ansible\-collections/community\.general/pull/11043](https\://github\.com/ansible\-collections/community\.general/pull/11043)\)\.
* redhat\_subscription \- improve Python code by removing unnecessary variables \([https\://github\.com/ansible\-collections/community\.general/pull/11049](https\://github\.com/ansible\-collections/community\.general/pull/11049)\)\.
* redis\_data\_incr \- improve Python code by removing unnecessary variables \([https\://github\.com/ansible\-collections/community\.general/pull/11049](https\://github\.com/ansible\-collections/community\.general/pull/11049)\)\.
* rhevm \- improve Python code \([https\://github\.com/ansible\-collections/community\.general/pull/11043](https\://github\.com/ansible\-collections/community\.general/pull/11043)\)\.
* rocketchat \- fix message delivery in Rocket Chat \>\= 7\.5\.3 by forcing <code>Content\-Type</code> header to <code>application/json</code> instead of the default <code>application/x\-www\-form\-urlencoded</code> \([https\://github\.com/ansible\-collections/community\.general/issues/10796](https\://github\.com/ansible\-collections/community\.general/issues/10796)\, [https\://github\.com/ansible\-collections/community\.general/pull/10796](https\://github\.com/ansible\-collections/community\.general/pull/10796)\)\.
* scaleway module utils \- improve Python code by removing unnecessary variables \([https\://github\.com/ansible\-collections/community\.general/pull/11049](https\://github\.com/ansible\-collections/community\.general/pull/11049)\)\.
* scaleway\_sshkey \- improve Python code by removing unnecessary variables \([https\://github\.com/ansible\-collections/community\.general/pull/11049](https\://github\.com/ansible\-collections/community\.general/pull/11049)\)\.
* selective callback plugin \- specify <code>ansible\_loop\_var</code> instead of the explicit value <code>item</code> when printing task result \([https\://github\.com/ansible\-collections/community\.general/pull/10752](https\://github\.com/ansible\-collections/community\.general/pull/10752)\)\.
* sensu\_check \- improve Python code \([https\://github\.com/ansible\-collections/community\.general/pull/11043](https\://github\.com/ansible\-collections/community\.general/pull/11043)\)\.
* simpleinit\_msb \- improve Python code \([https\://github\.com/ansible\-collections/community\.general/pull/11043](https\://github\.com/ansible\-collections/community\.general/pull/11043)\)\.
* sorcery \- improve Python code \([https\://github\.com/ansible\-collections/community\.general/pull/11043](https\://github\.com/ansible\-collections/community\.general/pull/11043)\)\.
* spectrum\_model\_attrs \- improve Python code by removing unnecessary variables \([https\://github\.com/ansible\-collections/community\.general/pull/11049](https\://github\.com/ansible\-collections/community\.general/pull/11049)\)\.
* spotinst\_aws\_elastigroup \- improve Python code by removing unnecessary variables \([https\://github\.com/ansible\-collections/community\.general/pull/11049](https\://github\.com/ansible\-collections/community\.general/pull/11049)\)\.
* svc \- improve Python code by removing unnecessary variables \([https\://github\.com/ansible\-collections/community\.general/pull/11049](https\://github\.com/ansible\-collections/community\.general/pull/11049)\)\.
* syslog\_json callback plugin \- improve Python code by removing unnecessary variables \([https\://github\.com/ansible\-collections/community\.general/pull/11049](https\://github\.com/ansible\-collections/community\.general/pull/11049)\)\.
* syspatch \- avoid ansible\-core 2\.19 deprecation \([https\://github\.com/ansible\-collections/community\.general/pull/10459](https\://github\.com/ansible\-collections/community\.general/pull/10459)\)\.
* sysrc \- fixes parsing with multi\-line variables \([https\://github\.com/ansible\-collections/community\.general/issues/10394](https\://github\.com/ansible\-collections/community\.general/issues/10394)\, [https\://github\.com/ansible\-collections/community\.general/pull/10417](https\://github\.com/ansible\-collections/community\.general/pull/10417)\)\.
* sysupgrade \- avoid ansible\-core 2\.19 deprecation \([https\://github\.com/ansible\-collections/community\.general/pull/10459](https\://github\.com/ansible\-collections/community\.general/pull/10459)\)\.
* terraform \- fix bug when <code>null</code> values inside complex vars are throwing error instead of being passed to terraform\. Now terraform can handle <code>null\`\`s in \`\`complex\_vars</code> itself \([https\://github\.com/ansible\-collections/community\.general/pull/10961](https\://github\.com/ansible\-collections/community\.general/pull/10961)\)\.
* terraform \- improve Python code \([https\://github\.com/ansible\-collections/community\.general/pull/11043](https\://github\.com/ansible\-collections/community\.general/pull/11043)\)\.
* timestamp callback plugin \- improve Python code \([https\://github\.com/ansible\-collections/community\.general/pull/11043](https\://github\.com/ansible\-collections/community\.general/pull/11043)\)\.
* timezone \- improve Python code \([https\://github\.com/ansible\-collections/community\.general/pull/11043](https\://github\.com/ansible\-collections/community\.general/pull/11043)\)\.
* to\_\* time filter plugins \- improve Python code \([https\://github\.com/ansible\-collections/community\.general/pull/11043](https\://github\.com/ansible\-collections/community\.general/pull/11043)\)\.
* to\_prettytable filter plugin \- improve Python code by removing unnecessary variables \([https\://github\.com/ansible\-collections/community\.general/pull/11049](https\://github\.com/ansible\-collections/community\.general/pull/11049)\)\.
* vmadm \- improve Python code by removing unnecessary variables \([https\://github\.com/ansible\-collections/community\.general/pull/11049](https\://github\.com/ansible\-collections/community\.general/pull/11049)\)\.
* wsl connection plugin \- avoid deprecated ansible\-core paramiko import helper\, import paramiko directly instead \([https\://github\.com/ansible\-collections/community\.general/issues/10515](https\://github\.com/ansible\-collections/community\.general/issues/10515)\, [https\://github\.com/ansible\-collections/community\.general/pull/10531](https\://github\.com/ansible\-collections/community\.general/pull/10531)\)\.
* wsl connection plugin \- improve Python code \([https\://github\.com/ansible\-collections/community\.general/pull/11043](https\://github\.com/ansible\-collections/community\.general/pull/11043)\)\.
* wsl connection plugin \- rename variable to fix type checking \([https\://github\.com/ansible\-collections/community\.general/pull/11030](https\://github\.com/ansible\-collections/community\.general/pull/11030)\)\.
* xen\_orchestra inventory plugin \- improve Python code by removing unnecessary variables \([https\://github\.com/ansible\-collections/community\.general/pull/11049](https\://github\.com/ansible\-collections/community\.general/pull/11049)\)\.
* xenserver module utils \- improve Python code by removing unnecessary variables \([https\://github\.com/ansible\-collections/community\.general/pull/11049](https\://github\.com/ansible\-collections/community\.general/pull/11049)\)\.
* xenserver\_guest \- improve Python code \([https\://github\.com/ansible\-collections/community\.general/pull/11043](https\://github\.com/ansible\-collections/community\.general/pull/11043)\)\.
* xenserver\_guest \- improve Python code by removing unnecessary variables \([https\://github\.com/ansible\-collections/community\.general/pull/11049](https\://github\.com/ansible\-collections/community\.general/pull/11049)\)\.
* xfconf \- fix handling of empty array properties \([https\://github\.com/ansible\-collections/community\.general/pull/11026](https\://github\.com/ansible\-collections/community\.general/pull/11026)\)\.
* xfconf\_info \- fix handling of empty array properties \([https\://github\.com/ansible\-collections/community\.general/pull/11026](https\://github\.com/ansible\-collections/community\.general/pull/11026)\)\.
* xfs\_quota \- improve Python code by removing unnecessary variables \([https\://github\.com/ansible\-collections/community\.general/pull/11049](https\://github\.com/ansible\-collections/community\.general/pull/11049)\)\.
* xml \- improve Python code by removing unnecessary variables \([https\://github\.com/ansible\-collections/community\.general/pull/11049](https\://github\.com/ansible\-collections/community\.general/pull/11049)\)\.
* yaml cache plugin \- make compatible with ansible\-core 2\.19 \([https\://github\.com/ansible\-collections/community\.general/issues/10849](https\://github\.com/ansible\-collections/community\.general/issues/10849)\, [https\://github\.com/ansible\-collections/community\.general/issues/10852](https\://github\.com/ansible\-collections/community\.general/issues/10852)\)\.
* zypper\_repository \- avoid ansible\-core 2\.19 deprecation \([https\://github\.com/ansible\-collections/community\.general/pull/10459](https\://github\.com/ansible\-collections/community\.general/pull/10459)\)\.
* zypper\_repository \- improve Python code \([https\://github\.com/ansible\-collections/community\.general/pull/11043](https\://github\.com/ansible\-collections/community\.general/pull/11043)\)\.

<a id="community-hrobot-3"></a>
#### community\.hrobot

* Avoid deprecated functionality in ansible\-core 2\.20 \([https\://github\.com/ansible\-collections/community\.hrobot/pull/174](https\://github\.com/ansible\-collections/community\.hrobot/pull/174)\)\.
* Avoid using <code>ansible\.module\_utils\.six</code> in more places to avoid deprecation warnings with ansible\-core 2\.20 \([https\://github\.com/ansible\-collections/community\.hrobot/pull/179](https\://github\.com/ansible\-collections/community\.hrobot/pull/179)\)\.
* Avoid using <code>ansible\.module\_utils\.six</code> to avoid deprecation warnings with ansible\-core 2\.20 \([https\://github\.com/ansible\-collections/community\.hrobot/pull/177](https\://github\.com/ansible\-collections/community\.hrobot/pull/177)\)\.

<a id="community-library-inventory-filtering-v1"></a>
#### community\.library\_inventory\_filtering\_v1

* Avoid deprecated functionality in ansible\-core 2\.20 \([https\://github\.com/ansible\-collections/community\.library\_inventory\_filtering/pull/38](https\://github\.com/ansible\-collections/community\.library\_inventory\_filtering/pull/38)\)\.
* Fix accidental type extensions \([https\://github\.com/ansible\-collections/community\.library\_inventory\_filtering/pull/40](https\://github\.com/ansible\-collections/community\.library\_inventory\_filtering/pull/40)\)\.
* Improve and stricten typing information \([https\://github\.com/ansible\-collections/community\.library\_inventory\_filtering/pull/42](https\://github\.com/ansible\-collections/community\.library\_inventory\_filtering/pull/42)\)\.
* Stop using <code>ansible\.module\_utils\.six</code> to avoid user\-facing deprecation messages with ansible\-core 2\.20\, while still supporting older ansible\-core versions \([https\://github\.com/ansible\-collections/community\.library\_inventory\_filtering/pull/39](https\://github\.com/ansible\-collections/community\.library\_inventory\_filtering/pull/39)\)\.

<a id="community-mysql-6"></a>
#### community\.mysql

* mysql\_info \- Fix slave status for source terminology introduced in MySQL 8\.0\.23 \([https\://github\.com/ansible\-collections/community\.mysql/issues/682](https\://github\.com/ansible\-collections/community\.mysql/issues/682)\)\.
* mysql\_user\, mysql\_role \- fix not existent grant when revoking perms on user/role which do not have any other perms than grant option \([https\://github\.com/ansible\-collections/community\.mysql/issues/664](https\://github\.com/ansible\-collections/community\.mysql/issues/664)\)\.

<a id="community-proxmox-10"></a>
#### community\.proxmox

* proxmox inventory plugin and proxmox module utils \- avoid Python 2 compatibility imports \([https\://github\.com/ansible\-collections/community\.proxmox/pull/175](https\://github\.com/ansible\-collections/community\.proxmox/pull/175)\)\.
* proxmox\_kvm \- remove limited choice for vga option in proxmox\_kvm \([https\://github\.com/ansible\-collections/community\.proxmox/pull/185](https\://github\.com/ansible\-collections/community\.proxmox/pull/185)\)
* proxmox\_kvm\, proxmox\_template \- remove <code>ansible\.module\_utils\.six</code> dependency \([https\://github\.com/ansible\-collections/community\.proxmox/pull/201](https\://github\.com/ansible\-collections/community\.proxmox/pull/201)\)\.
* proxmox\_storage \- fixed adding PBS\-type storage by ensuring its parameters \(server\, datastore\, etc\.\) are correctly sent to the Proxmox API \([https\://github\.com/ansible\-collections/community\.proxmox/pull/171](https\://github\.com/ansible\-collections/community\.proxmox/pull/171)\)\.
* proxmox\_user \- added a third case when testing for not\-yet\-existant user \([https\://github\.com/ansible\-collections/community\.proxmox/issues/163](https\://github\.com/ansible\-collections/community\.proxmox/issues/163)\)
* proxmox\_vm\_info \- do not throw exception when iterating through machines and optional api results are missing \([https\://github\.com/ansible\-collections/community\.proxmox/pull/191](https\://github\.com/ansible\-collections/community\.proxmox/pull/191)\)

<a id="community-routeros-12"></a>
#### community\.routeros

* Avoid using <code>ansible\.module\_utils\.six</code> to avoid deprecation warnings with ansible\-core 2\.20 \([https\://github\.com/ansible\-collections/community\.routeros/pull/405](https\://github\.com/ansible\-collections/community\.routeros/pull/405)\)\.
* Fix accidental type extensions \([https\://github\.com/ansible\-collections/community\.routeros/pull/406](https\://github\.com/ansible\-collections/community\.routeros/pull/406)\)\.
* api \- allow querying for keys containing <code>id</code>\, as long as the key itself is not <code>id</code> \([https\://github\.com/ansible\-collections/community\.routeros/issues/396](https\://github\.com/ansible\-collections/community\.routeros/issues/396)\, [https\://github\.com/ansible\-collections/community\.routeros/pull/398](https\://github\.com/ansible\-collections/community\.routeros/pull/398)\)\.

<a id="community-sops-2"></a>
#### community\.sops

* Avoid using <code>ansible\.module\_utils\.six</code> to avoid deprecation warnings with ansible\-core 2\.20 \([https\://github\.com/ansible\-collections/community\.sops/pull/268](https\://github\.com/ansible\-collections/community\.sops/pull/268)\)\.
* Clean up plugin code that does not run on the target \([https\://github\.com/ansible\-collections/community\.sops/pull/275](https\://github\.com/ansible\-collections/community\.sops/pull/275)\)\.
* Fix accidental type extensions \([https\://github\.com/ansible\-collections/community\.sops/pull/269](https\://github\.com/ansible\-collections/community\.sops/pull/269)\)\.
* Note that the MIT licenced code in <code>plugins/module\_utils/\_six\.py</code> has been removed \([https\://github\.com/ansible\-collections/community\.sops/pull/275](https\://github\.com/ansible\-collections/community\.sops/pull/275)\)\.
* load\_vars action \- avoid another deprecated module utils from ansible\-core \([https\://github\.com/ansible\-collections/community\.sops/pull/270](https\://github\.com/ansible\-collections/community\.sops/pull/270)\)\.
* load\_vars action \- avoid deprecated import from ansible\-core that will be removed in ansible\-core 2\.21 \([https\://github\.com/ansible\-collections/community\.sops/pull/272](https\://github\.com/ansible\-collections/community\.sops/pull/272)\)\.
* sops vars plugin \- ensure that loaded vars are evaluated also with ansible\-core 2\.19\+ \([https\://github\.com/ansible\-collections/community\.sops/pull/273](https\://github\.com/ansible\-collections/community\.sops/pull/273)\)\.

<a id="community-vmware-7"></a>
#### community\.vmware

* vmware\_guest\_file\_operation \- fix <code>replace\(\) argument 2 must be str\, not int</code> error \([https\://github\.com/ansible\-collections/community\.vmware/issues/2447](https\://github\.com/ansible\-collections/community\.vmware/issues/2447)\)\.
* vmware\_tools \- fix <code>replace\(\) argument 2 must be str\, not int</code> error \([https\://github\.com/ansible\-collections/community\.vmware/issues/2447](https\://github\.com/ansible\-collections/community\.vmware/issues/2447)\)\.

<a id="community-zabbix-4"></a>
#### community\.zabbix

* Proxy Role \- Fixed a deprication error with <em class="title-reference">ProxyConfigFrequency</em>
* web role \- Fixed a value test in nginx\_vhost\.conf
* zabbix\_agent \- Fix all variables related to windows installation paths
* zabbix\_agent role \- Fix windows paths to download and install zabbix agent msi
* zabbix\_agent role \- fixes too many requests to check latest zabbix release
* zabbix\_maintenance \- Fixed a bug that caused start time to update across multiple runs
* zabbix\_template \- Removed need for PY2
* zabbix\_template\_info \- Removed need for PY2

<a id="containers-podman-11"></a>
#### containers\.podman

* Fix podman logout for newer Podman
* Fix podman\_image correct delimiter logic for [version\@digest](mailto\:version\@digest) tags
* Remove quiet mode from pulling image

<a id="dellemc-enterprise-sonic-1"></a>
#### dellemc\.enterprise\_sonic

* sonic\-vlan\-mapping \- Avoid sending a deletion REST API containing a comma\-separated list of vlan IDs \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/563](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/563)\)\.
* sonic\_aaa \- Update AAA module to account for SONiC code changes \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/495](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/495)\)\.
* sonic\_bgp \- Remove CLI regression test cases for BGP \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/566](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/566)\)\.
* sonic\_bgp\_nbr \- Fix \'auth\_pwd\' diff calculation bug \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/583](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/583)\)\.
* sonic\_evpn\_esi\_multihome \- Fix EVPN ESI multihome delete all bug \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/578](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/578)\)\.
* sonic\_interfaces \- Fix port\-group interface error handling for speed configuration \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/575](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/575)\)\.
* sonic\_l2\_interfaces \- Fix VLAN deletion bug \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/526](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/526)\)\.
* sonic\_l3\_interfaces \- Fix check mode behavior for ipv4 primary address \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/491](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/491)\)\.
* sonic\_lag\_interfaces \- Fix \'mode\' value not retrieved in facts \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/475](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/475)\)\.
* sonic\_logging \- Addressing bug found in [https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/issues/508](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/issues/508) where a traceback is thrown if the \"severity\" value is not specified in the incoming playbook or if the incoming playbook specifies a \'severity\' value of None\. \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/537](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/537)\)\.
* sonic\_mclag \- Fix domain ID creation bug \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/591](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/591)\)\.
* sonic\_mirroring \- Fix mirroring regression test failures \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/577](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/577)\)\.
* sonic\_ospf\_area \- Fix OSPF area bug \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/541](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/541)\)\.
* sonic\_qos\_buffer \- Modify buffer profile handling to match new CVL requirements \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/543](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/543)\)\.
* sonic\_stp \- Add handling for removal of empty data structures for merge state \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/511](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/511)\)\.
* sonic\_stp \- Fix STP check mode bug \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/518](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/518)\)\.
* sonic\_stp \- Update request method to use post for enabled\_protocol \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/587](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/587)\)\.
* sonic\_tacacs\_server \- Add sleep to allow TACACS server config updates to apply to SONiC PAM modules \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/509](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/509)\)\.
* sonic\_vrfs \- Fix VRFs bug for overridden state \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/569](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/569)\)\.
* sonic\_vxlans \- Fix evpn\_nvo request bug \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/589](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/589)\)\.

<a id="dellemc-openmanage-5"></a>
#### dellemc\.openmanage

* Fixed the UT test execution through ansible\-test \- \(Issue 1003\) \- Tests Pass Using Tox But Not Ansible\-Test \([https\://github\.com/dell/dellemc\-openmanage\-ansible\-modules](https\://github\.com/dell/dellemc\-openmanage\-ansible\-modules)\)
* idrac\_server\_config\_profile \- \(Issue 959\) Can\'t export SCP \(Server configuration profile\) on iDRAC 10\. \([https\://github\.com/dell/dellemc\-openmanage\-ansible\-modules/issues/959](https\://github\.com/dell/dellemc\-openmanage\-ansible\-modules/issues/959)\)
* idrac\_support\_assist \- Updated module playbook examples to use the correct casing for protocol names\, for CIFS and HTTPS\.
* idrac\_system\_info \- \(Issue 1017\) \- System info not being returned on gen17s with v10\.0\.0 \([https\://github\.com/dell/dellemc\-openmanage\-ansible\-modules/issues/1017](https\://github\.com/dell/dellemc\-openmanage\-ansible\-modules/issues/1017)\)
* idrac\_system\_info \- \(Issue 967\) \- idrac\_system\_info fails on iDRAC10 with GPU\. \([https\://github\.com/dell/dellemc\-openmanage\-ansible\-modules/issues/967](https\://github\.com/dell/dellemc\-openmanage\-ansible\-modules/issues/967)\)
* redfish\_storage\_volume \- \(Issue 1027\) Module fails on force reboot\. \([https\://github\.com/dell/dellemc\-openmanage\-ansible\-modules/issues/1027](https\://github\.com/dell/dellemc\-openmanage\-ansible\-modules/issues/1027)\)

<a id="fortinet-fortimanager-6"></a>
#### fortinet\.fortimanager

* Changed the logic of getting FortiManager system information to prevent permission denied error\.
* Supported module\_defaults\. General variables can be specified in one place by using module\_defaults\.

<a id="fortinet-fortios-6"></a>
#### fortinet\.fortios

* Fix the issue in check\_modu when backend returns invallid IP address\.
* Fix the issue in configuration\_fact and monitor\_fact when omitting vdom or assigning vdom to \"\"\.
* Fixed authentication issue in v7\.6\.4 when using access\_token\.

<a id="google-cloud-7"></a>
#### google\.cloud

* gcp\_compute\_instance \- add suppport for attaching disks to compute instances \([https\://github\.com/ansible\-collections/google\.cloud/pull/711](https\://github\.com/ansible\-collections/google\.cloud/pull/711)\)\.
* gcp\_secret\_manager \- use service\_account\_contents instead of service\_account\_info \([https\://github\.com/ansible\-collections/google\.cloud/pull/703](https\://github\.com/ansible\-collections/google\.cloud/pull/703)\)\.

<a id="hetzner-hcloud-10"></a>
#### hetzner\.hcloud

* floating\_ip \- Wait for the Floating IP assign action to complete to reduce chances of running into <code>locked</code> errors\.
* server \- Also check server type deprecation after server creation\.

<a id="ibm-storage-virtualize-6"></a>
#### ibm\.storage\_virtualize

* ibm\_svc\_manage\_ip \- Fixed issues with IP address probe
* ibm\_svc\_manage\_volume \- Fixed data\-type conversion issue for grainsize
* ibm\_svc\_mdiskgrp \- Removed mandatory system mask setting during pool\-linking
* ibm\_svc\_start\_stop\_flashcopy \- Fixed flashcopy start issues when mapping belonged to flashcopy consistency group

<a id="ieisystem-inmanage-1"></a>
#### ieisystem\.inmanage

* Modify the automated tests and add support for version 2\.18\. \([https\://github\.com/ieisystem/ieisystem\.inmanage/pull/28](https\://github\.com/ieisystem/ieisystem\.inmanage/pull/28)\)\.
* Modify the failure details returned in module\_utils \([https\://github\.com/ieisystem/ieisystem\.inmanage/pull/26](https\://github\.com/ieisystem/ieisystem\.inmanage/pull/26)\)\.
* Modify the inmanage\.py file in the module\_utils directory\, and change the reference path of iteritems to be a reference from within Python\. \([https\://github\.com/ieisystem/ieisystem\.inmanage/pull/29](https\://github\.com/ieisystem/ieisystem\.inmanage/pull/29)\)\.
* Modify the method referenced in the support\_info\.py file to be support\_info\_nf \. \([https\://github\.com/ieisystem/ieisystem\.inmanage/pull/31](https\://github\.com/ieisystem/ieisystem\.inmanage/pull/31)\)\.

<a id="kubernetes-core-5"></a>
#### kubernetes\.core

* Remove <code>ansible\.module\_utils\.six</code> imports to avoid warnings \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/998](https\://github\.com/ansible\-collections/kubernetes\.core/pull/998)\)\.
* Update the <em class="title-reference">k8s\_cp</em> module to also work for init containers \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/971](https\://github\.com/ansible\-collections/kubernetes\.core/pull/971)\)\.

<a id="netapp-ontap-8"></a>
#### netapp\.ontap

* Added manual utf\-8 encoding to handle unicode characters in passwords for HTTP Basic Authentication in netapp module utilities\.
* na\_ontap\_ntfs\_dacl \- fixed typo in short description\.
* na\_ontap\_rest\_info \- added error handling when API doesn\'t return zero records\.
* na\_ontap\_snapmirror \- fixed intermittent issue with creating relationship\.
* na\_ontap\_volume \- fix idempotency issue with <em class="title-reference">nas\_application\_template</em> and <em class="title-reference">size\_change\_threshold</em>\.

<a id="ngine-io-cloudstack-1"></a>
#### ngine\_io\.cloudstack

* Ensure tags are applied when creating or updating a template \([https\://github\.com/ngine\-io/ansible\-collection\-cloudstack/pull/154](https\://github\.com/ngine\-io/ansible\-collection\-cloudstack/pull/154)\)\.

<a id="purestorage-flasharray-6"></a>
#### purestorage\.flasharray

* purefa\_certs \- Resolved error with incorrect use of <code>key\_size</code> for imported certificates
* purefa\_connect \- Ensured that encrypted connections use encrypted connection keys
* purefa\_eradication \- Fixed idempotency issue
* purefa\_eradication \- Idempotency fix
* purefa\_eula \- Fix AttributeError when first sogning EULA
* purefa\_host \- Fixed Pydantic error when updating preferred\_arrays
* purefa\_info \- Ensured that volumes\, hosts\, host\_groups and transfers are correctly listed for protection groups
* purefa\_info \- Fixed AttributeError for hgroups subset
* purefa\_info \- Fixed AttributeError in config section related to SSO SAML2
* purefa\_info \- Fixed issue with replication connection throttle reporting
* purefa\_info \- Fixed issue with undo\-demote pods not reporting correctly
* purefa\_info \- Resolved AttributeError in volume subset
* purefa\_network \- Resolve typo that causes network updates to not apply correctly
* purefa\_pg \- Changing target for PG no longer requires a <code>FixedReference</code>
* purefa\_pg \- Fixed AttributeError adding target to PG
* purefa\_subnet \- Fixed failure when trying to update a subnet with no gateway defined

<a id="purestorage-flashblade-4"></a>
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

<a id="vmware-vmware-8"></a>
#### vmware\.vmware

* Drop incorrect requirement on aiohttp \([https\://github\.com/ansible\-collections/vmware\.vmware/pull/230](https\://github\.com/ansible\-collections/vmware\.vmware/pull/230)\)\.
* cluster\_ha \- Fix admission control policy not being updated when ac is disabled
* content\_template \- Fix typo in code for check mode that tried to access a module param which doesn\'t exist\.
* import\_content\_library\_ovf \- Fix large file import by using requests instead of open\_url\. Requests allows for streaming uploads\, instead of reading the entire file into memory\. \(Fixes [https\://github\.com/ansible\-collections/vmware\.vmware/issues/220](https\://github\.com/ansible\-collections/vmware\.vmware/issues/220)\)
* vm\_powerstate \- Ensure timeout option also applies to the shutdown\-guest state

<a id="known-issues-3"></a>
### Known Issues

<a id="ansible-core-22"></a>
#### Ansible\-core

* templating \- Exceptions raised in a Jinja <code>set</code> or <code>with</code> block which are not accessed by the template are ignored in the same manner as undefined values\.
* templating \- Passing a container created in a Jinja <code>set</code> or <code>with</code> block to a method results in a copy of that container\. Mutations to that container which are not returned by the method will be discarded\.

<a id="community-sops-3"></a>
#### community\.sops

* When using the <code>community\.sops\.load\_vars</code> with ansible\-core 2\.20\, note that the deprecation of <code>INJECT\_FACTS\_AS\_VARS</code> causes deprecation warnings to be shown every time a variable loaded with <code>community\.sops\.load\_vars</code> is used\. This is due to ansible\-core deprecating <code>INJECT\_FACTS\_AS\_VARS</code> without providing an alternative for modules like <code>community\.sops\.load\_vars</code> to use\. If you do not like these deprecation warnings\, you have to explicitly set <code>INJECT\_FACTS\_AS\_VARS</code> to <code>true</code>\. <strong>DO NOT</strong> change the use of SOPS encrypted variables to <code>ansible\_facts</code>\. The situation will hopefully improve in ansible\-core 2\.21 through the promised API that allows action plugins to set variables\; community\.sops will adapt to use it\, which will make the warning go away\. \(The API was originally promised for ansible\-core 2\.20\, but then delayed\.\)

<a id="dellemc-openmanage-6"></a>
#### dellemc\.openmanage

* Formal qualification of module ome\_smart\_fabric\_info for Ansible Core version 2\.19 is still pending\.
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
* redfish\_storage\_volume \- Encryption type and block\_io\_size bytes will be read only property in iDRAC9 and iDRAC10 and hence the module ignores these parameters\.

<a id="new-plugins-3"></a>
### New Plugins

<a id="callback-1"></a>
#### Callback

* community\.general\.tasks\_only \- Only show tasks\.

<a id="filter-2"></a>
#### Filter

* community\.general\.to\_nice\_yaml \- Convert variable to YAML string\.
* community\.general\.to\_yaml \- Convert variable to YAML string\.

<a id="inventory"></a>
#### Inventory

* community\.general\.incus \- Incus inventory source\.
* containers\.podman\.buildah\_containers \- Inventory plugin that discovers Buildah working containers as hosts
* containers\.podman\.podman\_containers \- Inventory plugin that discovers Podman containers as hosts

<a id="lookup"></a>
#### Lookup

* community\.dns\.lookup\_rfc8427 \- Look up DNS records and return RFC 8427 JSON format\.
* community\.general\.binary\_file \- Read binary file and return it Base64 encoded\.

<a id="new-modules-6"></a>
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

<a id="community-general-26"></a>
#### community\.general

* community\.general\.django\_dumpdata \- Wrapper for <code>django\-admin dumpdata</code>\.
* community\.general\.django\_loaddata \- Wrapper for <code>django\-admin loaddata</code>\.
* community\.general\.jenkins\_credential \- Manage Jenkins credentials and domains through API\.
* community\.general\.kea\_command \- Submits generic command to ISC KEA server on target\.
* community\.general\.keycloak\_user\_execute\_actions\_email \- Send a Keycloak execute\-actions email to a user\.
* community\.general\.lvm\_pv\_move\_data \- Move data between LVM Physical Volumes \(PVs\)\.
* community\.general\.pacemaker\_info \- Gather information about Pacemaker cluster\.
* community\.general\.pacemaker\_stonith \- Manage Pacemaker STONITH\.

<a id="community-proxmox-11"></a>
#### community\.proxmox

* community\.proxmox\.proxmox\_cluster\_ha\_rules \- Management of HA rules\.
* community\.proxmox\.proxmox\_firewall \- Manage firewall rules in Proxmox\.
* community\.proxmox\.proxmox\_firewall\_info \- Manage firewall rules in Proxmox\.
* community\.proxmox\.proxmox\_ipam\_info \- Retrieve information about IPAMs\.
* community\.proxmox\.proxmox\_subnet \- Create/Update/Delete subnets from SDN\.
* community\.proxmox\.proxmox\_vnet \- Manage virtual networks in Proxmox SDN\.
* community\.proxmox\.proxmox\_vnet\_info \- Retrieve information about one or more Proxmox VE SDN vnets\.
* community\.proxmox\.proxmox\_zone \- Manage Proxmox zone configurations\.
* community\.proxmox\.proxmox\_zone\_info \- Get Proxmox zone info\.

<a id="community-proxysql-1"></a>
#### community\.proxysql

* community\.proxysql\.proxysql\_mysql\_hostgroup\_attributes \- Manages hostgroup attributes using the ProxySQL admin interface

<a id="containers-podman-12"></a>
#### containers\.podman

* containers\.podman\.podman\_system\_connection \- Manage Podman system connections
* containers\.podman\.podman\_system\_connection\_info \- Get info about Podman system connections

<a id="dellemc-enterprise-sonic-2"></a>
#### dellemc\.enterprise\_sonic

* dellemc\.enterprise\_sonic\.sonic\_ars \- Manage adaptive routing and switching \(ARS\) configuration on SONiC\.
* dellemc\.enterprise\_sonic\.sonic\_br\_l2pt \- Manage L2PT configurations on SONiC\.
* dellemc\.enterprise\_sonic\.sonic\_dcbx \- Manage DCBx configurations on SONiC\.
* dellemc\.enterprise\_sonic\.sonic\_drop\_counter \- Manage drop counter configuration on SONiC\.
* dellemc\.enterprise\_sonic\.sonic\_ecmp\_load\_share \- IP ECMP load share mode configuration handling for SONiC\.
* dellemc\.enterprise\_sonic\.sonic\_evpn\_esi\_multihome \- Manage EVPN ESI multihoming configuration on SONiC\.
* dellemc\.enterprise\_sonic\.sonic\_fbs\_classifiers \- Manage flow based services \(FBS\) classifiers configuration on SONiC\.
* dellemc\.enterprise\_sonic\.sonic\_fbs\_groups \- Manage flow based services \(FBS\) groups configuration on SONiC\.
* dellemc\.enterprise\_sonic\.sonic\_fbs\_policies \- Manage flow based services \(FBS\) policies configuration on SONiC\.
* dellemc\.enterprise\_sonic\.sonic\_ip\_neighbor\_interfaces \- Manage interface\-specific IP neighbor configurations on SONiC\.
* dellemc\.enterprise\_sonic\.sonic\_ipv6\_router\_advertisement \- Manage interface\-specific IPv6 Router Advertisement configurations on SONiC\.
* dellemc\.enterprise\_sonic\.sonic\_lst \- Manage link state tracking \(LST\) configuration on SONiC\.
* dellemc\.enterprise\_sonic\.sonic\_mirroring \- Manage port mirroring configuration on SONiC\.
* dellemc\.enterprise\_sonic\.sonic\_network\_policy \- Manage network policy configuration on SONiC\.
* dellemc\.enterprise\_sonic\.sonic\_ospfv3 \- Configure global OSPFv3 protocol settings on SONiC\.
* dellemc\.enterprise\_sonic\.sonic\_ospfv3\_area \- Configure OSPFv3 area settings on SONiC\.
* dellemc\.enterprise\_sonic\.sonic\_ospfv3\_interfaces \- Configure OSPFv3 interface mode protocol settings on SONiC\.
* dellemc\.enterprise\_sonic\.sonic\_pms \- Configure interface mode port security settings on SONiC\.
* dellemc\.enterprise\_sonic\.sonic\_ptp\_default\_ds \- Manage global PTP configurations on SONiC\.
* dellemc\.enterprise\_sonic\.sonic\_ptp\_port\_ds \- Manage port specific PTP configurations on SONiC\.
* dellemc\.enterprise\_sonic\.sonic\_ssh\_server \- Manage SSH server configurations on SONiC\.

<a id="dellemc-powerflex-2"></a>
#### dellemc\.powerflex

* dellemc\.powerflex\.device\_v2 \- Manage device on Dell PowerFlex Gen2
* dellemc\.powerflex\.info\_v2 \- Gathering information about Dell PowerFlex Gen2
* dellemc\.powerflex\.protection\_domain\_v2 \- Manage Protection Domain on Dell PowerFlex Gen2
* dellemc\.powerflex\.snapshot\_v2 \- Manage Snapshots on Dell PowerFlex Gen2
* dellemc\.powerflex\.storagepool\_v2 \- Managing Dell PowerFlex storage pool Gen2
* dellemc\.powerflex\.volume\_v2 \- Manage volumes on Dell PowerFlex Gen2

<a id="hitachivantara-vspone-block-7"></a>
#### hitachivantara\.vspone\_block

<a id="sds-block-2"></a>
##### Sds Block

* hitachivantara\.vspone\_block\.hv\_sds\_block\_capacity\_management\_settings\_facts \- Get capacity management settings from storage system\.
* hitachivantara\.vspone\_block\.hv\_sds\_block\_compute\_port \- Manages compute port on Hitachi SDS Block storage systems\.
* hitachivantara\.vspone\_block\.hv\_sds\_block\_drive \- Manages drive on Hitachi SDS Block storage systems\.
* hitachivantara\.vspone\_block\.hv\_sds\_block\_software\_update\_file\_facts \- Get the information of the update file of the storage software which performed transfer \(upload\) in the storage cluster\.
* hitachivantara\.vspone\_block\.hv\_sds\_block\_storage\_controller \- Edits the settings for the storage controller on Hitachi SDS Block storage systems\.
* hitachivantara\.vspone\_block\.hv\_sds\_block\_storage\_node\_bmc\_connection \- Manages BMC connection settings for a storage node on Hitachi SDS Block storage systems\.
* hitachivantara\.vspone\_block\.hv\_sds\_block\_storage\_node\_bmc\_connection\_facts \- Get storage node BMC access settings from storage system\.
* hitachivantara\.vspone\_block\.hv\_sds\_block\_storage\_pool\_estimated\_capacity\_facts \- Obtains the preliminary calculation results of the storage pool logical capacity \(unit TiB\)\.
* hitachivantara\.vspone\_block\.hv\_sds\_block\_storage\_software\_update \- Manages software update and downgrade on Hitachi SDS Block storage systems\.

<a id="vsp-1"></a>
##### Vsp

* hitachivantara\.vspone\_block\.hv\_vsp\_one\_port \- Manages port configuration on Hitachi VSP One storage systems\.
* hitachivantara\.vspone\_block\.hv\_vsp\_one\_port\_facts \- Retrieves port information from Hitachi VSP One storage systems\.
* hitachivantara\.vspone\_block\.hv\_vsp\_one\_server \- Manages servers on Hitachi VSP One storage systems\.
* hitachivantara\.vspone\_block\.hv\_vsp\_one\_server\_facts \- Retrieves server information from Hitachi VSP One storage systems\.
* hitachivantara\.vspone\_block\.hv\_vsp\_one\_server\_hba\_facts \- Retrieves server HBA information from Hitachi VSP One storage systems\.
* hitachivantara\.vspone\_block\.hv\_vsp\_one\_snapshot \- Manages snapshots on Hitachi VSP One storage systems\.
* hitachivantara\.vspone\_block\.hv\_vsp\_one\_snapshot\_facts \- Retrieves snapshot information from Hitachi VSP One storage systems\.
* hitachivantara\.vspone\_block\.hv\_vsp\_one\_snapshot\_group \- Manages snapshot group operations in Hitachi VSP One storage systems\.
* hitachivantara\.vspone\_block\.hv\_vsp\_one\_snapshot\_group\_facts \- Retrieves snapshot group information from Hitachi VSP One storage systems\.
* hitachivantara\.vspone\_block\.hv\_vsp\_one\_volume \- Manages volumes on Hitachi VSP One storage systems\.
* hitachivantara\.vspone\_block\.hv\_vsp\_one\_volume\_facts \- Retrieves facts about Hitachi VSP One storage system volumes\.

<a id="ibm-storage-virtualize-7"></a>
#### ibm\.storage\_virtualize

* ibm\.storage\_virtualize\.ibm\_sv\_manage\_system\_certificate \- Manages system certificates and truststore for replication\, high availability and FlashSystem grid on IBM Storage Virtualize family systems

<a id="ieisystem-inmanage-2"></a>
#### ieisystem\.inmanage

* ieisystem\.inmanage\.generate\_ssl \- Generate SSL certificate
* ieisystem\.inmanage\.ssl\_info \- Get SSL certificate information
* ieisystem\.inmanage\.upload\_ssl \- Upload SSL certificate

<a id="ngine-io-cloudstack-2"></a>
#### ngine\_io\.cloudstack

* ngine\_io\.cloudstack\.configuration\_info \- Gathering information about configurations from Apache CloudStack based clouds\.

<a id="purestorage-flashblade-5"></a>
#### purestorage\.flashblade

* purestorage\.flashblade\.purefb\_kmip \- Manage FlashBlade KMIP server objects

<a id="theforeman-foreman-6"></a>
#### theforeman\.foreman

* theforeman\.foreman\.content\_view\_history\_info \- Fetch history of a Content View

<a id="unchanged-collections-6"></a>
### Unchanged Collections

* ansible\.netcommon \(still version 8\.1\.0\)
* ansible\.posix \(still version 2\.1\.0\)
* ansible\.utils \(still version 6\.0\.0\)
* ansible\.windows \(still version 3\.2\.0\)
* arista\.eos \(still version 12\.0\.0\)
* awx\.awx \(still version 24\.6\.1\)
* chocolatey\.chocolatey \(still version 1\.5\.3\)
* cisco\.aci \(still version 2\.12\.0\)
* cisco\.mso \(still version 2\.11\.0\)
* cisco\.nxos \(still version 11\.0\.0\)
* cisco\.ucs \(still version 1\.16\.0\)
* cloudscale\_ch\.cloud \(still version 2\.5\.2\)
* community\.aws \(still version 10\.0\.0\)
* community\.ciscosmb \(still version 1\.0\.11\)
* community\.grafana \(still version 2\.3\.0\)
* community\.libvirt \(still version 2\.0\.0\)
* community\.mongodb \(still version 1\.7\.10\)
* community\.okd \(still version 5\.0\.0\)
* community\.postgresql \(still version 4\.1\.0\)
* community\.rabbitmq \(still version 1\.6\.0\)
* community\.windows \(still version 3\.0\.1\)
* dellemc\.unity \(still version 2\.1\.0\)
* infinidat\.infinibox \(still version 1\.6\.3\)
* infoblox\.nios\_modules \(still version 1\.8\.0\)
* inspur\.ispim \(still version 2\.2\.3\)
* junipernetworks\.junos \(still version 11\.0\.0\)
* kaytus\.ksmanage \(still version 2\.0\.0\)
* kubevirt\.core \(still version 2\.2\.3\)
* lowlydba\.sqlserver \(still version 2\.7\.0\)
* microsoft\.ad \(still version 1\.9\.2\)
* microsoft\.iis \(still version 1\.0\.3\)
* netapp\.cloudmanager \(still version 21\.24\.0\)
* netapp\.storagegrid \(still version 21\.15\.0\)
* netapp\_eseries\.santricity \(still version 1\.4\.1\)
* netbox\.netbox \(still version 3\.21\.0\)
* ovirt\.ovirt \(still version 3\.2\.1\)
* splunk\.es \(still version 4\.0\.0\)
* telekom\_mms\.icinga\_director \(still version 2\.4\.0\)
* vmware\.vmware\_rest \(still version 4\.9\.0\)
* vultr\.cloud \(still version 1\.13\.0\)
* vyos\.vyos \(still version 6\.0\.0\)
* wti\.remote \(still version 1\.0\.10\)
